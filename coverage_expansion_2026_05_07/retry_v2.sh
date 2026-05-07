#!/bin/bash
# retry_v2.sh — pass prompts as positional args (stdin doesn't work in some contexts)
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" || exit 1

declare -A CLUSTER
CLUSTER[A2]="音楽学（音楽理論・音楽美学・民族音楽学・音楽認知科学・音楽社会学・ポピュラー音楽研究）"
CLUSTER[A6]="デザイン理論（デザインリサーチ・デザインシンキング・プロダクトデザイン論・サービスデザイン・インタラクションデザイン論・ソーシャルデザイン・デザイン史・デザイン哲学）"
CLUSTER[E5]="化学工学・材料工学（プロセス工学・分離工学・反応工学・触媒工学・材料科学・先端材料・ナノ材料・ナノテクノロジー・高分子工学・電池・エネルギー材料）"
CLUSTER[H3]="大陸哲学・現象学（現象学・実存主義・解釈学・哲学的解釈学・ポスト構造主義・フーコー・デリダ・批判理論・フランクフルト学派・新唯物論・思弁的実在論）"
CLUSTER[N8]="宇宙物理・天文学（観測宇宙論・宇宙背景放射・ブラックホール・重力波天文学・恒星進化・超新星・系外惑星・宇宙生物学・銀河形成・宇宙構造・暗黒物質・暗黒エネルギー・高エネルギー天体物理・天文観測機器・サーベイ）"
CLUSTER[S3]="経済学理論（行動経済学・実験経済学・制度経済学・新制度派・進化経済学・複雑系経済学・エコロジカル経済学・脱成長論・金融経済学・金融不安定性仮説・開発経済学・貧困・不平等）"

declare -A TABLE
TABLE[A2]="arts_question"; TABLE[A6]="arts_question"
TABLE[E5]="engineering_method"
TABLE[H3]="humanities_concept"
TABLE[N8]="natural_discovery"
TABLE[S3]="social_theory"

run_one() {
  local tid="$1"
  local cluster="${CLUSTER[$tid]}"
  local prompt="あなたは学術概念の専門エージェントです。${cluster} の重要な理論・概念・モデル・運動を150件、JSON配列で出力してください。

各エントリは以下の形式：
{
  \"name_ja\": \"日本語名\",
  \"name_en\": \"English Name\",
  \"definition\": \"100文字以上の定義\",
  \"impact_summary\": \"50文字以上の影響まとめ\",
  \"subfield\": \"上記列挙の中黒区切りリストから1つ選ぶ\",
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
- JSON配列のみ出力（コードフェンス・説明文不要）
- 150件全て出力するまで止めない"

  local out="outputs/${tid}.json"
  local log="logs/${tid}.retry2.log"
  echo "[retry2] $tid start at $(date +%H:%M:%S)"
  codex exec --full-auto "$prompt" > "$out" 2> "$log"
  local rc=$?
  echo "[retry2] $tid done rc=$rc bytes=$(wc -c < $out)"
}

export -f run_one
export -A CLUSTER TABLE 2>/dev/null

# Run sequentially to avoid resource contention
for tid in A2 A6 E5 H3 N8 S3; do
  run_one "$tid"
done

echo "[retry2] all done at $(date)"
ls -la outputs/{A2,A6,E5,H3,N8,S3}.json
