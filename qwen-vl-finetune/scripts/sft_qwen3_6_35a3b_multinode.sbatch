#!/bin/bash

#SBATCH --job-name=sft_qwen3_6_35a3b_mn
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --partition=p0
#SBATCH --gres=gpu:8
#SBATCH --output=logs/%j.out
#SBATCH --mem=0

# Multi-node SFT of Qwen/Qwen3.6-35B-A3B (MoE, 35B total / ~3B active).
# Default: 4 nodes x 8 GPU (32x80GB) with DeepSpeed ZeRO-2.
# Bump --nodes= above for more throughput. ZeRO-2 matches the recommendation in
# sft_30a3b.sh (MoE+ZeRO-3 has known stability issues at this scale).
#
# Before sbatch: `export WANDB_API_KEY=<your_key>` (or set in ~/.netrc).

ulimit -l unlimited
ulimit -n 65536

export NCCL_IB_DISABLE=0
export NCCL_IB_HCA=mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_6,mlx5_7,mlx5_8,mlx5_9
export NCCL_IB_PKEY=1
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

source /mnt/vast/trillion/env/miniconda3/etc/profile.d/conda.sh
conda activate qwen-vl

REPO_DIR=/mnt/vast/trillion/hyungguk/Qwen3-VL/qwen-vl-finetune
cd "$REPO_DIR"
mkdir -p logs

MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n1)
MASTER_PORT=$(( 20000 + SLURM_JOB_ID % 10000 ))
NNODES=$SLURM_NNODES
NPROC_PER_NODE=8

deepspeed_config=./scripts/zero2.json

llm=Qwen/Qwen3.6-35B-A3B
lr=1e-5
batch_size=1
grad_accum_steps=4

datasets=public_dataset1,public_dataset2

run_name="sft_qwen3_6_35a3b_mn"
output_dir=./output/${run_name}

args="
    --deepspeed ${deepspeed_config} \
    --model_name_or_path ${llm} \
    --use_dummy_handler False \
    --dataset_use ${datasets} \
    --data_flatten True \
    --tune_mm_vision False \
    --tune_mm_mlp True \
    --tune_mm_llm True \
    --bf16 \
    --output_dir ${output_dir} \
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
    --nnodes=${NNODES} \
    --nproc_per_node=${NPROC_PER_NODE} \
    --node_rank=${SLURM_NODEID} \
    --rdzv_backend=c10d \
    --rdzv_endpoint=${MASTER_ADDR}:${MASTER_PORT} \
    qwenvl/train/train_qwen.py ${args}
