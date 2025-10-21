#!/bin/bash
set -euo pipefail

export WANDB_API_KEY=5aa1eaca490f698ba1dfb353d4a79e9c0cf3f915

# === Pin the interpreter ===
PYTHON="/home/work/.shared/miniconda3/envs/mobile_agent_v3/bin/python"

# If not already under MPI, self-launch via mpirun (single-command entrypoint)
SCRIPT_PATH=$(readlink -f "$0" 2>/dev/null || echo "$0")
if [ -z "${OMPI_COMM_WORLD_SIZE-}" ] && [ -z "${PMI_SIZE-}" ]; then
  PROCS=${PROCS:-16}
  HOSTS=${HOSTS:-"sub9:8,sub8:8"}
  MASTER_ADDR=${MASTER_ADDR:-sub9}
  MASTER_PORT=${MASTER_PORT:-23456}
  NCCL_SOCKET_IFNAME=${NCCL_SOCKET_IFNAME:-eth0}
  NCCL_DEBUG=${NCCL_DEBUG:-INFO}
  NCCL_ASYNC_ERROR_HANDLING=${NCCL_ASYNC_ERROR_HANDLING:-1}

  exec mpirun -np ${PROCS} \
    -H ${HOSTS} \
    --bind-to none \
    --map-by ppr:8:node \
    -x MASTER_ADDR=${MASTER_ADDR} \
    -x MASTER_PORT=${MASTER_PORT} \
    -x NCCL_SOCKET_IFNAME=${NCCL_SOCKET_IFNAME} \
    -x NCCL_DEBUG=${NCCL_DEBUG} \
    -x NCCL_ASYNC_ERROR_HANDLING=${NCCL_ASYNC_ERROR_HANDLING} \
    -x WANDB_API_KEY \
    -x PATH -x LD_LIBRARY_PATH -x PYTHONPATH -x CUDA_VISIBLE_DEVICES \
    bash -lc "${SCRIPT_PATH}"
fi

############################################
# Cluster layout (edit as needed)
############################################
DEFAULT_MASTER_ADDR="sub9"     # main node
DEFAULT_MASTER_PORT="23456"    # choose an open fixed port for all ranks

############################################
# Distributed env from MPI (OpenMPI or MPICH)
############################################
# Prefer OpenMPI env vars if present
# -------- MPI-only distributed env mapping --------
# These are populated automatically by mpirun/mpiexec.
# -------- Robust MPI env mapping (no Slurm) --------
# Helper: return first non-empty from a list
first_non_empty() {
  for v in "$@"; do
    if [ -n "$v" ]; then
      echo "$v"
      return 0
    fi
  done
  echo ""
}

# Collect raw values from env (may be empty)
_raw_ws="${WORLD_SIZE-}"
_raw_rank="${RANK-}"
_raw_lrank="${LOCAL_RANK-}"
_raw_node_rank="${NODE_RANK-}"

# Prefer MPI-provided vars if ours are empty
WORLD_SIZE="$(first_non_empty "$_raw_ws" "${OMPI_COMM_WORLD_SIZE-}" "${PMI_SIZE-}" "1")"
RANK="$(first_non_empty "$_raw_rank" "${OMPI_COMM_WORLD_RANK-}" "${PMI_RANK-}" "0")"
LOCAL_RANK="$(first_non_empty "$_raw_lrank" "${OMPI_COMM_WORLD_LOCAL_RANK-}" "0")"
NODE_RANK="$(first_non_empty "$_raw_node_rank" "${OMPI_COMM_WORLD_NODE_RANK-}" "0")"

# If any is still empty or non-numeric, coerce to safe defaults
[[ "$WORLD_SIZE" =~ ^[0-9]+$ ]] || WORLD_SIZE=1
[[ "$RANK" =~ ^[0-9]+$ ]] || RANK=0
[[ "$LOCAL_RANK" =~ ^[0-9]+$ ]] || LOCAL_RANK=0
[[ "$NODE_RANK" =~ ^[0-9]+$ ]] || NODE_RANK=0

export WORLD_SIZE RANK LOCAL_RANK NODE_RANK
# ---------------------------------------------------

# (Optional) sanity log
echo "[DIST] host=$(hostname)  WS=$WORLD_SIZE R=$RANK LR=$LOCAL_RANK NR=$NODE_RANK  MASTER=${MASTER_ADDR:-?}:${MASTER_PORT:-?}"

# --------------------------------------------------



# Master address/port (same for every rank)
export MASTER_ADDR="${MASTER_ADDR:-$DEFAULT_MASTER_ADDR}"
export MASTER_PORT="${MASTER_PORT:-$DEFAULT_MASTER_PORT}"
export NNODES="${WORLD_SIZE:-1}"

############################################
# NCCL / networking (tune to your fabric)
############################################
# If you know your interface, set it explicitly, e.g. "eno1", "eth0", "ib0"
export NCCL_SOCKET_IFNAME="${NCCL_SOCKET_IFNAME:-eth0}"
export NCCL_DEBUG="${NCCL_DEBUG:-WARN}"
export NCCL_ASYNC_ERROR_HANDLING=1
export CUDA_DEVICE_MAX_CONNECTIONS="${CUDA_DEVICE_MAX_CONNECTIONS:-1}"

# Increase file descriptors & shared memory safety
ulimit -n 1048576 || true

############################################
# DeepSpeed / training config
############################################
deepspeed=./scripts/zero2.json

# Model
llm="Qwen/Qwen2.5-VL-7B-Instruct"
# llm="Qwen/Qwen3-VL-8B-Instruct"

# Hparams
lr=2e-7
batch_size=1
grad_accum_steps=4

# Entry
entry_file=qwenvl/train/train_qwen.py

# Datasets
datasets="amex"

# Logging / output
run_name="qwen2_5vl-sanity_check"
output_dir=./outputs/output

# Common args (array to avoid quoting issues)
args=(
    --deepspeed "${deepspeed}"
    --model_name_or_path "${llm}"
    --dataset_use "${datasets}"
    --data_flatten True
    --use_dummy_handler True
    --tune_mm_vision False
    --tune_mm_mlp True
    --tune_mm_llm True
    --bf16
    --output_dir "${output_dir}"
    --num_train_epochs 0.5
    --per_device_train_batch_size "${batch_size}"
    --per_device_eval_batch_size "$((batch_size*2))"
    --gradient_accumulation_steps "${grad_accum_steps}"
    --max_pixels 50176
    --min_pixels 784
    --eval_strategy no
    --save_strategy steps
    --save_steps 1000
    --save_total_limit 1
    --learning_rate "${lr}"
    --weight_decay 0
    --warmup_ratio 0.03
    --max_grad_norm 1
    --lr_scheduler_type cosine
    --logging_steps 1
    --model_max_length 8192
    --gradient_checkpointing True
    --dataloader_num_workers 4
    --run_name "${run_name}"
)

echo "[INFO] MASTER_ADDR=${MASTER_ADDR} MASTER_PORT=${MASTER_PORT} WORLD_SIZE=${WORLD_SIZE} RANK=${RANK} LOCAL_RANK=${LOCAL_RANK} NODE_RANK=${NODE_RANK}"

############################################
# Launch: when under mpirun, this process is one rank.
# DO NOT call torchrun/mpirun here (MPI already spawned the ranks).
############################################
exec "$PYTHON" -u "$entry_file" "${args[@]}"