#!/bin/bash

#SBATCH --job-name=sft_qwen3_6_35a3b
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --partition=p0
#SBATCH --gres=gpu:8
#SBATCH --output=logs/%j.out
#SBATCH --mem=0

# Single-node SFT of Qwen/Qwen3.6-35B-A3B (MoE, 35B total / ~3B active) on 1x8x80GB.
# Uses DeepSpeed ZeRO-3 for full parameter sharding (35B fits with margin on 8x80GB).
# For larger-scale (multi-node) runs, see sft_qwen3_6_35a3b_multinode.sbatch.
#
# Before sbatch: `export WANDB_API_KEY=<your_key>` (or set in ~/.netrc).
# flash-attn is required by --attn_implementation flash_attention_2 in train_qwen.py.

ulimit -l unlimited
ulimit -n 65536

: "${WANDB_API_KEY:?WANDB_API_KEY must be set in the environment (e.g. via ~/.netrc or 'export WANDB_API_KEY=...' before sbatch)}"
export WANDB_API_KEY
export NCCL_IB_DISABLE=0
export NCCL_IB_HCA=mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_6,mlx5_7,mlx5_8,mlx5_9
export NCCL_IB_PKEY=1
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

source /mnt/vast/trillion/env/miniconda3/etc/profile.d/conda.sh
conda activate qwen-vl

REPO_DIR=/mnt/vast/trillion/hyungguk/Qwen3-VL/qwen-vl-finetune
cd "$REPO_DIR"
mkdir -p logs

MASTER_ADDR=127.0.0.1
MASTER_PORT=$(shuf -i 20001-29999 -n 1)
NPROC_PER_NODE=8

deepspeed_config=./scripts/zero3.json

llm=Qwen/Qwen3.6-35B-A3B
lr=1e-5
batch_size=1
grad_accum_steps=8

datasets=mmmu_r1

run_name="sft_qwen3_6_35a3b_mmmu_r1_smoke"
output_dir=./output/${run_name}

args="
    --deepspeed ${deepspeed_config} \
    --model_name_or_path ${llm} \
    --use_dummy_handler False \
    --dataset_use ${datasets} \
    --data_flatten False \
    --tune_mm_vision False \
    --tune_mm_mlp True \
    --tune_mm_llm True \
    --bf16 \
    --output_dir ${output_dir} \
    --max_steps 2 \
    --num_train_epochs 1 \
    --per_device_train_batch_size ${batch_size} \
    --per_device_eval_batch_size $((batch_size*2)) \
    --gradient_accumulation_steps ${grad_accum_steps} \
    --max_pixels 50176 \
    --min_pixels 784 \
    --eval_strategy no \
    --save_strategy steps \
    --save_steps 1000 \
    --save_total_limit 1 \
    --learning_rate ${lr} \
    --weight_decay 0 \
    --warmup_ratio 0.03 \
    --max_grad_norm 1 \
    --lr_scheduler_type cosine \
    --logging_steps 1 \
    --model_max_length 8192 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --run_name ${run_name} \
    --report_to wandb"

srun -l torchrun \
    --nproc_per_node=${NPROC_PER_NODE} \
    --master_addr=${MASTER_ADDR} \
    --master_port=${MASTER_PORT} \
    qwenvl/train/train_qwen.py ${args}
