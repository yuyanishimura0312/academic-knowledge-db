#!/bin/bash
# launch_codex_40.sh — 40 Codex agents in parallel for academic DB coverage expansion
# Output: outputs/{TASK_ID}.json
set -u

ROOT="$(cd "$(dirname "$0")" && pwd)"
PROMPTS_DIR="$ROOT/prompts"
OUTPUT_DIR="$ROOT/outputs"
LOG_DIR="$ROOT/logs"
mkdir -p "$OUTPUT_DIR" "$LOG_DIR"

# Concurrency control: codex API has rate limits. Run 8 at a time.
MAX_PARALLEL="${MAX_PARALLEL:-8}"

echo "[launch_codex_40] Starting at $(date)"
echo "[launch_codex_40] Prompts dir: $PROMPTS_DIR"
echo "[launch_codex_40] Output dir:  $OUTPUT_DIR"
echo "[launch_codex_40] Max parallel: $MAX_PARALLEL"
echo "---"

run_one() {
  local prompt_file="$1"
  local task_id
  task_id=$(basename "$prompt_file" .md | cut -d_ -f1)
  local out="$OUTPUT_DIR/${task_id}.json"
  local log="$LOG_DIR/${task_id}.log"

  if [ -s "$out" ]; then
    echo "[skip] $task_id already has output ($(wc -c < "$out") bytes)"
    return 0
  fi

  echo "[start] $task_id at $(date +%H:%M:%S)"
  codex exec --full-auto < "$prompt_file" > "$out" 2> "$log"
  local rc=$?
  echo "[done]  $task_id rc=$rc bytes=$(wc -c < "$out" 2>/dev/null || echo 0) at $(date +%H:%M:%S)"
}

export -f run_one
export OUTPUT_DIR LOG_DIR

# Launch in parallel with bounded concurrency
# Use background jobs + wait pattern
running=0
pids=()

for prompt_file in "$PROMPTS_DIR"/*.md; do
  if [ "$running" -ge "$MAX_PARALLEL" ]; then
    wait -n 2>/dev/null || wait "${pids[0]}"
    pids=("${pids[@]:1}")
    running=$((running - 1))
  fi
  run_one "$prompt_file" &
  pids+=($!)
  running=$((running + 1))
done

# Wait for remaining
for pid in "${pids[@]}"; do
  wait "$pid" 2>/dev/null || true
done

echo "---"
echo "[launch_codex_40] All complete at $(date)"
echo "Output sizes:"
for f in "$OUTPUT_DIR"/*.json; do
  printf "  %-12s %10d bytes\n" "$(basename "$f")" "$(wc -c < "$f")"
done
