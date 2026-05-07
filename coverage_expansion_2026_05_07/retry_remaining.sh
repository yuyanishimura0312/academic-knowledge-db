#!/bin/bash
# retry_remaining.sh — A6, E5, S3 を確実に取得するためのシンプル版
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1

run_one() {
  local tid="$1"
  local cluster="$2"
  local prompt="あなたは学術概念の専門エージェントです。${cluster} の重要な理論・概念・モデル・運動を120件、JSON配列で出力してください。

各エントリは以下の形式：
{
  \"name_ja\": \"日本語名\",
  \"name_en\": \"English Name\",
  \"definition\": \"100文字以上の定義\",
  \"impact_summary\": \"50文字以上の影響まとめ\",
  \"subfield\": \"クラスター内サブフィールド名\",
  \"school_of_thought\": \"学派・流派\",
  \"era_start\": 整数年,
  \"era_end\": 整数年または null,
  \"keywords_ja\": \"カンマ区切り\",
  \"keywords_en\": \"keyword1,keyword2\",
  \"key_researchers\": [\"主要研究者\"],
  \"key_works\": [\"主要著作 (年)\"]
}

要件:
- 創設期から最新2025年まで時代分布を均等に
- 確実に存在する概念のみ
- 重複なし
- JSON配列のみ出力（コードフェンス・説明文不要）"

  local out="outputs/${tid}.json"
  local log="logs/${tid}.remaining.log"
  echo "[remaining] $tid start at $(date +%H:%M:%S)"
  codex exec --full-auto "$prompt" > "$out" 2> "$log"
  local rc=$?
  echo "[remaining] $tid done rc=$rc bytes=$(wc -c < $out)"
}

# Sequential execution to avoid contention
run_one A6 "デザイン理論（デザインリサーチ・デザインシンキング・プロダクトデザイン論・サービスデザイン・インタラクションデザイン論・ソーシャルデザイン・デザイン史・デザイン哲学）"
run_one E5 "化学工学・材料工学（プロセス工学・分離工学・反応工学・触媒工学・材料科学・先端材料・ナノ材料・ナノテクノロジー・高分子工学・電池・エネルギー材料）"
run_one S3 "経済学理論（行動経済学・実験経済学・制度経済学・新制度派・進化経済学・複雑系経済学・エコロジカル経済学・脱成長論・金融経済学・金融不安定性仮説・開発経済学・貧困・不平等）"

echo "[remaining] all done at $(date)"
ls -la outputs/A6.json outputs/E5.json outputs/S3.json
