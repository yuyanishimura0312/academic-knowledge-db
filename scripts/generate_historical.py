#!/usr/bin/env python3
"""
Generate historical foundational concepts for the academic knowledge database.
Uses Claude API to produce era-batched concepts with genealogical relations.
Output: import_v3.py compatible JSON files in collected/{domain}/
"""

import json
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT_DIR = Path(__file__).parent.parent / "collected"

DOMAIN_CONFIG = {
    "humanities": {
        "table": "humanities_concept",
        "domain_key": "humanities",
        "name_ja": "人文学",
        "specific_fields": ["blind_spot_addressed", "reinterpretation_history", "cultural_context"],
        "relation_types": ["derived_from", "critiques", "reinterprets", "extends", "opposes", "synthesizes", "complements"],
        "eras": [
            {"name": "ancient", "start": -500, "end": 500, "count": 40,
             "guidance": "古代ギリシャ哲学（プラトン、アリストテレス、ストア派、エピクロス派）、古代インド哲学（ヴェーダーンタ、仏教論理学、ニヤーヤ学派）、古代中国哲学（儒教、道教、墨家、法家）、イスラーム哲学の基盤"},
            {"name": "medieval", "start": 500, "end": 1500, "count": 30,
             "guidance": "スコラ哲学（トマス・アクィナス、オッカム）、イスラーム哲学（イブン・ルシュド、イブン・シーナー）、中国宋明理学（朱子学、陽明学）、日本仏教思想（天台、禅）、ビザンティン思想"},
            {"name": "early_modern", "start": 1500, "end": 1800, "count": 40,
             "guidance": "ルネサンス人文主義、合理論（デカルト、スピノザ、ライプニッツ）、経験論（ロック、ヒューム、バークリー）、カント批判哲学、啓蒙思想、社会契約論、美学の成立"},
            {"name": "19c", "start": 1800, "end": 1900, "count": 50,
             "guidance": "ドイツ観念論（ヘーゲル、フィヒテ、シェリング）、マルクス主義哲学、ニーチェ、功利主義（ベンサム、ミル）、実存主義の萌芽（キェルケゴール）、歴史主義、新カント派、プラグマティズムの成立、文献学・解釈学"},
            {"name": "early_20c", "start": 1900, "end": 1960, "count": 40,
             "guidance": "現象学（フッサール、メルロ＝ポンティ）、実存主義（ハイデガー、サルトル）、分析哲学（フレーゲ、ラッセル、前期ウィトゲンシュタイン）、論理実証主義、フランクフルト学派、構造主義の萌芽（ソシュール）、解釈学（ガダマー）"},
        ],
    },
    "natural_sciences": {
        "table": "natural_discovery",
        "domain_key": "natural_sciences",
        "name_ja": "自然科学",
        "specific_fields": ["mathematical_formulation", "experimental_verification", "applicable_scale", "precision_level"],
        "relation_types": ["derived_from", "generalizes", "experimentally_confirms", "contradicts", "supersedes", "enables", "complements"],
        "eras": [
            {"name": "pre1700", "start": -500, "end": 1700, "count": 30,
             "guidance": "アリストテレス自然学、ユークリッド幾何学、プトレマイオス天文学、アルキメデスの原理、イスラーム科学（代数学、光学）、コペルニクス地動説、ガリレオの実験科学、ケプラーの法則、ニュートン力学・万有引力"},
            {"name": "18c", "start": 1700, "end": 1800, "count": 30,
             "guidance": "リンネ分類学、ラヴォアジエ近代化学、フランクリン電気学、オイラー数学、ラプラス力学的決定論、ベルヌーイ流体力学、酸素説、フロギストン説の否定"},
            {"name": "19c", "start": 1800, "end": 1900, "count": 50,
             "guidance": "ダーウィン進化論、メンデル遺伝学、マクスウェル電磁気学、ボルツマン統計力学、熱力学三法則、周期表（メンデレーエフ）、細菌学（パスツール、コッホ）、ファラデーの電磁誘導、非ユークリッド幾何学、原子論の発展"},
            {"name": "early_20c", "start": 1900, "end": 1950, "count": 50,
             "guidance": "量子力学（プランク、ボーア、シュレーディンガー、ハイゼンベルク）、特殊・一般相対性理論（アインシュタイン）、DNA構造の前史、大陸移動説（ウェゲナー）、ビッグバン理論の基礎、量子電磁力学、原子核物理学"},
            {"name": "mid_20c", "start": 1950, "end": 1990, "count": 40,
             "guidance": "DNA二重らせん構造、プレートテクトニクス、標準模型の発展、分子生物学セントラルドグマ、カオス理論、情報理論（シャノン）、計算複雑性理論"},
        ],
    },
    "social_sciences": {
        "table": "social_theory",
        "domain_key": "social_sciences",
        "name_ja": "社会科学",
        "specific_fields": ["predictive_power", "operationalization", "empirical_support", "policy_implications"],
        "relation_types": ["derived_from", "critiques", "extends", "empirically_tests", "synthesizes", "competes_with", "applies_to_policy", "complements"],
        "eras": [
            {"name": "pre1800", "start": -500, "end": 1800, "count": 20,
             "guidance": "社会契約論（ホッブズ、ロック、ルソー）、国富論（アダム・スミス）、法の精神（モンテスキュー）、イブン・ハルドゥーンの歴史哲学、マキャヴェリ政治学"},
            {"name": "19c", "start": 1800, "end": 1900, "count": 40,
             "guidance": "マルクス（資本論、階級論）、ウェーバー（官僚制、プロ倫）、デュルケーム（社会的事実、自殺論）、ジンメル（形式社会学）、スペンサー（社会進化論）、コント（実証主義）、トクヴィル、ミル、限界効用理論"},
            {"name": "early_20c", "start": 1900, "end": 1950, "count": 40,
             "guidance": "シカゴ学派、パーソンズ構造機能主義、ミード象徴的相互作用論、マンハイム知識社会学、ポランニー大転換、ケインズ経済学、ゲーム理論（フォン・ノイマン）、行動主義心理学"},
            {"name": "mid_20c", "start": 1950, "end": 1980, "count": 30,
             "guidance": "ゴフマン（ドラマトゥルギー）、フーコー（権力・知）、ブルデュー（文化資本・ハビトゥス）、ルーマン社会システム論、合理的選択理論、依存理論、世界システム論（ウォーラーステイン）、認知革命"},
            {"name": "late_20c", "start": 1980, "end": 2000, "count": 20,
             "guidance": "ギデンズ構造化理論、ベック危険社会、ハーバーマスコミュニケーション理論、新制度主義、行動経済学の基礎（カーネマン、トベルスキー）、社会構成主義、ポストコロニアリズム"},
        ],
    },
    "engineering": {
        "table": "engineering_method",
        "domain_key": "engineering",
        "name_ja": "工学",
        "specific_fields": ["technology_readiness_level", "related_patents", "industry_applications", "problem_type", "scientific_basis"],
        "relation_types": ["derived_from", "improves", "supersedes", "combines", "based_on", "standardizes", "complements"],
        "eras": [
            {"name": "pre1800", "start": -500, "end": 1800, "count": 20,
             "guidance": "ローマ水道橋・土木工学、活版印刷術（グーテンベルク）、時計技術、レオナルド・ダ・ヴィンチの工学設計、蒸気機関の前史（ニューコメン）、織物機械（飛び杼）、冶金学の基礎"},
            {"name": "19c", "start": 1800, "end": 1900, "count": 40,
             "guidance": "蒸気機関（ワット改良）、ベッセマー製鋼法、電信（モールス）、電話（ベル）、電力系統（エジソン、テスラ）、内燃機関、鉄道工学、土木の構造計算、テイラー科学的管理法、写真技術"},
            {"name": "early_20c", "start": 1900, "end": 1950, "count": 40,
             "guidance": "ライト兄弟航空工学、フォード式量産方式、レーダー、初期コンピューティング（チューリング、ENIAC）、オペレーションズリサーチ、品質管理（シューハート管理図）、原子力工学、ロケット工学、プラスチック工学"},
            {"name": "mid_20c", "start": 1950, "end": 1980, "count": 30,
             "guidance": "トランジスタ→集積回路、ARPANET、構造化プログラミング、CAD、制御理論、信号処理（FFT）、半導体工学、人間工学、ソフトウェア工学の成立、品質管理（デミング、TQC）"},
            {"name": "late_20c", "start": 1980, "end": 2000, "count": 20,
             "guidance": "TCP/IP・インターネット、リレーショナルDB、オブジェクト指向設計、VLSI設計、光ファイバー通信、GPS、ロボティクス基盤、Linux・オープンソース、バイオテクノロジー工学"},
        ],
    },
    "arts": {
        "table": "arts_question",
        "domain_key": "arts",
        "name_ja": "芸術",
        "specific_fields": ["target_assumption", "medium", "representative_works", "movement_affiliation", "sensory_dimension"],
        "relation_types": ["derived_from", "deepens", "counters", "translates_medium", "revives", "inspires", "complements"],
        "eras": [
            {"name": "ancient_medieval", "start": -500, "end": 1400, "count": 25,
             "guidance": "ギリシャ悲劇（カタルシス理論）、ローマ修辞学、ビザンティンイコン神学、ゴシック建築美学、中国画論（六法論）、日本雅楽・能楽の美学、イスラーム幾何学装飾、インド古典舞踊（ナーティヤ・シャーストラ）"},
            {"name": "renaissance_baroque", "start": 1400, "end": 1700, "count": 30,
             "guidance": "線遠近法（アルベルティ）、レオナルドの芸術理論、ミケランジェロの人体表現、バロック美学（ベルニーニ）、対位法・和声法の成立、オペラの誕生、日本の茶の美学（利休）、浮世絵の成立"},
            {"name": "18_19c", "start": 1700, "end": 1900, "count": 40,
             "guidance": "崇高論（バーク、カント）、ロマン主義、写実主義、印象派、後期印象派、ワーグナー総合芸術、ウィリアム・モリスのアーツ・アンド・クラフツ運動、アール・ヌーヴォー、日本画の近代化、写真の芸術性論争"},
            {"name": "early_20c", "start": 1900, "end": 1960, "count": 35,
             "guidance": "キュビスム、ダダイスム、シュルレアリスム、バウハウス、抽象表現主義、フルクサス、コンクリート・ポエトリー、十二音技法（シェーンベルク）、日本の具体美術、モンドリアンのデ・ステイル"},
            {"name": "late_20c", "start": 1960, "end": 2000, "count": 20,
             "guidance": "ポップアート、ミニマリズム、コンセプチュアルアート、パフォーマンスアート、ポストモダン建築、ビデオアート、インスタレーション、デコンストラクション建築、もの派"},
        ],
    },
}


def get_api_key():
    """Get Anthropic API key from macOS keychain."""
    result = subprocess.run(
        ["security", "find-generic-password", "-a", "anthropic", "-w"],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def get_existing_concepts(table):
    """Get list of existing concept names to avoid duplicates."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(f"SELECT name_ja, name_en, era_start FROM {table}").fetchall()
    conn.close()
    return rows


def build_prompt(domain_cfg, era_cfg, existing_names):
    """Build the generation prompt for Claude API."""
    domain_name = domain_cfg["name_ja"]
    specific_fields = domain_cfg["specific_fields"]
    relation_types = domain_cfg["relation_types"]

    existing_sample = "\n".join(
        f"  - {n[0]} ({n[1]}, {n[2]}年)" for n in existing_names[:50]
    )

    field_descriptions = {
        "blind_spot_addressed": "この概念が照らす学問的盲点",
        "reinterpretation_history": "再解釈の歴史",
        "cultural_context": "文化的文脈",
        "predictive_power": "予測力の評価",
        "operationalization": "操作化の方法",
        "empirical_support": "経験的裏付け",
        "policy_implications": "政策的含意",
        "mathematical_formulation": "数学的定式化",
        "experimental_verification": "実験的検証",
        "applicable_scale": "適用スケール",
        "precision_level": "精度レベル",
        "technology_readiness_level": "技術成熟度レベル(1-9の整数)",
        "related_patents": "関連特許",
        "industry_applications": "産業応用",
        "problem_type": "問題タイプ",
        "scientific_basis": "科学的基盤",
        "target_assumption": "問い直す前提",
        "medium": "媒体",
        "representative_works": "代表作品",
        "movement_affiliation": "所属運動",
        "sensory_dimension": "感覚次元",
    }

    specific_field_desc = "\n".join(
        f'    "{f}": "{field_descriptions.get(f, f)}"' for f in specific_fields
    )

    return f"""あなたは{domain_name}の学術史の専門家です。
{era_cfg['start']}年〜{era_cfg['end']}年の時期に誕生した重要な学術概念・理論・発見を{era_cfg['count']}件生成してください。

## ガイダンス
{era_cfg['guidance']}

## 既存概念（重複禁止）
以下の概念は既にデータベースに存在します。これらと重複しない概念を生成してください：
{existing_sample}
（他にも{len(existing_names)}件の概念が登録済み）

## 出力形式
以下のJSON形式で出力してください。JSONのみ出力し、他のテキストは含めないでください。

{{
  "domain": "{domain_cfg['domain_key']}",
  "concepts": [
    {{
      "name_ja": "概念の日本語名",
      "name_en": "English name",
      "definition": "概念の定義（2-3文、学術的に正確に）",
      "impact_summary": "学問的影響の要約（1-2文）",
      "subfield": "所属サブフィールド（日本語）",
      "school_of_thought": "所属学派（日本語）",
      "era_start": {era_cfg['start']},
      "era_end": null,
      "methodology_level": "theoretical/empirical/meta-theoretical のいずれか",
      "target_domain": "適用対象領域",
      "application_conditions": "適用条件",
      "when_to_apply": "この概念を使うべき場面",
      "framing_questions": "この概念が提起する問い",
      "opposing_concept_names": "対立する概念名",
      "keywords_ja": "キーワード1, キーワード2, キーワード3",
      "keywords_en": "keyword1, keyword2, keyword3",
      "status": "foundational",
      "source_reliability": "primary",
      "data_completeness": 80,
{specific_field_desc}
    }}
  ],
  "relations": [
    {{
      "source": "概念Aの日本語名",
      "target": "概念Bの日本語名",
      "relation_type": "{relation_types[0]}",
      "description": "関係の説明",
      "strength": 7
    }}
  ]
}}

## 重要な注意事項
1. era_startは概念が誕生・提唱された年を正確に記入（整数）。{era_cfg['start']}〜{era_cfg['end']}の範囲内
2. 各概念に2-3の系譜的関係(relations)を含めること。同バッチ内の概念同士の関係を優先
3. relation_typeは以下のみ使用可能: {', '.join(relation_types)}
4. 名前は学術的に正確な表記を使用
5. 概念は{era_cfg['count']}件ちょうど生成すること
6. strengthは1-9の整数（系譜的に重要な関係ほど高い値）
"""


def call_claude_api(prompt, api_key):
    """Call Claude API and return the response text."""
    import urllib.request

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 16000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())

    return result["content"][0]["text"]


def extract_json(text):
    """Extract JSON from response text, handling markdown code blocks."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        start = 1
        end = len(lines) - 1
        if lines[-1].strip() == "```":
            text = "\n".join(lines[start:end])
        else:
            text = "\n".join(lines[start:])
    return json.loads(text)


def generate_domain(domain_key, era_name=None, dry_run=False):
    """Generate historical concepts for a domain."""
    cfg = DOMAIN_CONFIG[domain_key]
    api_key = get_api_key()
    existing = get_existing_concepts(cfg["table"])

    eras = cfg["eras"]
    if era_name:
        eras = [e for e in eras if e["name"] == era_name]
        if not eras:
            print(f"Error: era '{era_name}' not found for {domain_key}")
            return

    for era in eras:
        output_path = OUTPUT_DIR / domain_key.replace("_sciences", "_sciences") / f"historical_{era['name']}.json"
        if domain_key == "natural_sciences":
            output_path = OUTPUT_DIR / "natural_sciences" / f"historical_{era['name']}.json"
        elif domain_key == "social_sciences":
            output_path = OUTPUT_DIR / "social_sciences" / f"historical_{era['name']}.json"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists():
            print(f"  Skipping {output_path} (already exists)")
            # Add existing batch concepts to avoid duplicates in next era
            with open(output_path) as f:
                batch = json.load(f)
                for c in batch.get("concepts", []):
                    existing.append((c.get("name_ja", ""), c.get("name_en", ""), c.get("era_start", 0)))
            continue

        print(f"\n{'='*60}")
        print(f"Generating: {cfg['name_ja']} / {era['name']} ({era['start']}〜{era['end']}) x{era['count']}")
        print(f"{'='*60}")

        prompt = build_prompt(cfg, era, existing)

        if dry_run:
            print(f"  [DRY RUN] Would generate {era['count']} concepts")
            print(f"  Output: {output_path}")
            continue

        try:
            response_text = call_claude_api(prompt, api_key)
            data = extract_json(response_text)

            # Validate basic structure
            concepts = data.get("concepts", [])
            relations = data.get("relations", [])
            print(f"  Generated: {len(concepts)} concepts, {len(relations)} relations")

            # Save
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Saved: {output_path}")

            # Add to existing list for next era
            for c in concepts:
                existing.append((c.get("name_ja", ""), c.get("name_en", ""), c.get("era_start", 0)))

            # Rate limiting
            time.sleep(2)

        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            continue


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate historical academic concepts")
    parser.add_argument("domain", choices=list(DOMAIN_CONFIG.keys()) + ["all"],
                        help="Domain to generate for")
    parser.add_argument("--era", help="Specific era to generate (e.g., 'ancient', '19c')")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated without calling API")
    args = parser.parse_args()

    if args.domain == "all":
        for dk in DOMAIN_CONFIG:
            generate_domain(dk, args.era, args.dry_run)
    else:
        generate_domain(args.domain, args.era, args.dry_run)
