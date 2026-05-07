#!/bin/bash
# Retry the 6 failed tasks with a slightly more permissive prompt.
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1
mkdir -p outputs logs

FAILED=(A2 A6 E5 H3 N8 S3)

run_retry() {
  local tid="$1"
  local original_prompt
  original_prompt=$(cat "prompts/${tid}_"*.md 2>/dev/null)
  if [ -z "$original_prompt" ]; then
    echo "[err] no prompt for $tid"
    return 1
  fi
  # Append a softening instruction
  local prompt="$original_prompt

## 重要な追加指示
- 200件すべてが検証可能でなくても、確実なものから150-200件を出力する
- 完全なゼロ件で終わらせない（最低でも100件は確実な概念を含める）
- 体系的に知られている主要理論・概念から優先的に収集
- web検索が遅い場合は内部知識のみで十分。外部検索は必須ではない
"
  local out="outputs/${tid}.json"
  local log="logs/${tid}.retry.log"
  echo "[retry] $tid at $(date +%H:%M:%S)"
  echo "$prompt" | codex exec --full-auto > "$out" 2> "$log"
  local sz
  sz=$(wc -c < "$out")
  echo "[done] $tid bytes=$sz"
}

export -f run_retry

pids=()
for tid in "${FAILED[@]}"; do
  run_retry "$tid" &
  pids+=($!)
done

for pid in "${pids[@]}"; do
  wait "$pid" 2>/dev/null || true
done

echo "[retry] complete at $(date)"
ls -laS outputs/A2.json outputs/A6.json outputs/E5.json outputs/H3.json outputs/N8.json outputs/S3.json 2>/dev/null
