#!/bin/bash
# launch_step234.sh — Step 2 (social) + Step 3 (engineering+arts) + Step 4 (humanities) を並列起動
# Codex 46タスク並列。MAX_PARALLEL=8 で実行
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1

OUTPUT_DIR="$ROOT/step234_outputs"
LOG_DIR="$ROOT/step234_logs"
mkdir -p "$OUTPUT_DIR" "$LOG_DIR"
MAX_PARALLEL="${MAX_PARALLEL:-8}"

run_task() {
  local tid="$1"
  local subfield="$2"
  local target="$3"
  local must_include="$4"
  local prompt="あなたは学術概念の専門エージェントです。「${subfield}」分野について、${target}件の重要な理論・概念・モデル・運動を JSON 配列で出力してください。

以下の必須概念を必ず含めてください：
${must_include}

各エントリは以下の形式：
{
  \"name_ja\": \"日本語名\",
  \"name_en\": \"English Name\",
  \"definition\": \"100文字以上の定義\",
  \"impact_summary\": \"50文字以上の影響まとめ\",
  \"subfield\": \"${subfield}\",
  \"school_of_thought\": \"学派・流派\",
  \"era_start\": 整数年,
  \"era_end\": 整数年または null,
  \"keywords_ja\": \"カンマ区切り\",
  \"keywords_en\": \"keyword1,keyword2\",
  \"key_researchers\": [\"主要研究者\"],
  \"key_works\": [\"主要著作 (年)\"]
}

重要要件:
- subfield フィールドは必ず「${subfield}」に統一する（変更不可）
- 創設期から最新2025年まで時代分布を均等に（特に2015-2025の最新理論を30%以上）
- 確実に存在する概念のみ。重複なし
- JSON配列のみ出力（コードフェンス・説明文不要）
- ${target}件全て出力するまで止めない"

  local out="$OUTPUT_DIR/${tid}.json"
  local log="$LOG_DIR/${tid}.log"

  if [ -s "$out" ]; then
    echo "[skip] $tid already has output ($(wc -c < "$out") bytes)"
    return 0
  fi

  echo "[start] $tid ($subfield, target=$target) at $(date +%H:%M:%S)"
  codex exec --full-auto "$prompt" > "$out" 2> "$log"
  local rc=$?
  echo "[done]  $tid rc=$rc bytes=$(wc -c < "$out")"
}

# Read tasks from JSON
python3 -c "
import json
data = json.load(open('step234_tasks.json'))
for t in data['tasks']:
    must_inc = '\\n'.join(['- ' + m for m in t['must_include']])
    print(f'{t[\"id\"]}|||{t[\"subfield\"]}|||{t[\"target\"]}|||{must_inc}')
" > /tmp/step234_taskdata.txt

# Launch in parallel
running=0
pids=()

while IFS='|||' read -r tid f1 sub f2 target f3 must; do
  [ -z "$tid" ] && continue
  if [ "$running" -ge "$MAX_PARALLEL" ]; then
    wait -n 2>/dev/null || wait "${pids[0]}"
    pids=("${pids[@]:1}")
    running=$((running - 1))
  fi
  run_task "$tid" "$sub" "$target" "$must" &
  pids+=($!)
  running=$((running + 1))
done < /tmp/step234_taskdata.txt

for pid in "${pids[@]}"; do
  wait "$pid" 2>/dev/null || true
done

echo "[step234] all done at $(date)"
echo "Output sizes:"
for f in "$OUTPUT_DIR"/*.json; do
  printf "  %-25s %10d bytes\n" "$(basename "$f")" "$(wc -c < "$f")"
done | sort -k2 -n
