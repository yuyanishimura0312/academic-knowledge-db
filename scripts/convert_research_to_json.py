#!/usr/bin/env python3
"""
Convert researched concept TSV lists directly to import_v3.py compatible JSON.
No external API calls required - uses the structured research data directly.
Generates basic definitions and auto-builds genealogical relations from temporal proximity.
"""

import json
import sqlite3
import re
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT_DIR = Path(__file__).parent.parent / "collected"

DOMAIN_CONFIG = {
    "humanities": {
        "table": "humanities_concept",
        "domain_key": "humanities",
        "output_subdir": "humanities",
    },
    "natural_sciences": {
        "table": "natural_discovery",
        "domain_key": "natural_sciences",
        "output_subdir": "natural_sciences",
    },
    "social_sciences": {
        "table": "social_theory",
        "domain_key": "social_sciences",
        "output_subdir": "social_sciences",
    },
    "engineering": {
        "table": "engineering_method",
        "domain_key": "engineering",
        "output_subdir": "engineering",
    },
    "arts": {
        "table": "arts_question",
        "domain_key": "arts",
        "output_subdir": "arts",
    },
}


def get_existing_names(table):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(f"SELECT name_ja, name_en FROM {table}").fetchall()
    conn.close()
    names = set()
    for r in rows:
        if r[0]: names.add(r[0])
        if r[1]: names.add(r[1])
    return names


def parse_tsv(filepath):
    concepts = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("```"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4:
                try:
                    year = int(parts[0])
                except ValueError:
                    continue
                concepts.append({
                    "era_start": year,
                    "name_en": parts[1],
                    "name_ja": parts[2],
                    "key_thinker": parts[3],
                })
    return concepts


def infer_subfield(name_en, name_ja):
    """Infer subfield from concept name."""
    name = (name_en + " " + name_ja).lower()

    # Philosophy subfields
    if any(w in name for w in ["ethic", "moral", "virtue", "倫理", "徳"]):
        return "倫理学"
    if any(w in name for w in ["logic", "syllogism", "論理"]):
        return "論理学"
    if any(w in name for w in ["metaphysic", "ontolog", "being", "substance", "形而上", "存在"]):
        return "形而上学・存在論"
    if any(w in name for w in ["epistem", "knowledge", "cognit", "認識", "知識"]):
        return "認識論"
    if any(w in name for w in ["aesthetic", "sublime", "beauty", "art", "美学", "芸術", "崇高"]):
        return "美学"
    if any(w in name for w in ["politic", "state", "govern", "democra", "政治", "国家"]):
        return "政治哲学"
    if any(w in name for w in ["social contract", "社会契約"]):
        return "社会哲学"
    if any(w in name for w in ["phenomen", "現象"]):
        return "現象学"
    if any(w in name for w in ["existential", "dasein", "実存"]):
        return "実存主義"
    if any(w in name for w in ["hermeneutic", "解釈"]):
        return "解釈学"
    if any(w in name for w in ["structur", "構造"]):
        return "構造主義"
    if any(w in name for w in ["confuci", "儒", "仁", "礼"]):
        return "儒教思想"
    if any(w in name for w in ["dao", "tao", "道教", "無為"]):
        return "道教思想"
    if any(w in name for w in ["buddhis", "zen", "仏", "禅", "浄土", "天台", "真言", "中観", "唯識"]):
        return "仏教思想"
    if any(w in name for w in ["islam", "ibn", "al-", "イスラーム", "スーフィ"]):
        return "イスラーム哲学"
    if any(w in name for w in ["indian", "vedant", "samkhya", "nyaya", "yoga", "jain", "インド", "ヴェーダ", "サーンキヤ", "ニヤーヤ", "ジャイナ"]):
        return "インド哲学"

    # Science subfields
    if any(w in name for w in ["quantum", "量子"]):
        return "量子物理学"
    if any(w in name for w in ["relativ", "相対"]):
        return "相対性理論"
    if any(w in name for w in ["evolut", "darwin", "natural selection", "進化"]):
        return "進化生物学"
    if any(w in name for w in ["genetic", "dna", "mendel", "遺伝", "DNA"]):
        return "遺伝学"
    if any(w in name for w in ["thermodynamic", "entropy", "熱力学"]):
        return "熱力学"
    if any(w in name for w in ["electro", "maxwell", "電磁"]):
        return "電磁気学"
    if any(w in name for w in ["atom", "nuclear", "原子", "核"]):
        return "原子物理学"
    if any(w in name for w in ["astron", "cosm", "universe", "天文", "宇宙"]):
        return "天文学・宇宙論"
    if any(w in name for w in ["chemistry", "chemical", "化学"]):
        return "化学"
    if any(w in name for w in ["biolog", "cell", "molecular", "生物", "細胞", "分子"]):
        return "生物学"
    if any(w in name for w in ["mathematic", "geometr", "algebra", "数学", "幾何"]):
        return "数学"
    if any(w in name for w in ["mechanic", "motion", "gravity", "力学", "運動", "引力"]):
        return "力学"
    if any(w in name for w in ["optic", "光学"]):
        return "光学"

    # Social science subfields
    if any(w in name for w in ["economic", "market", "capital", "経済", "資本", "市場"]):
        return "経済学"
    if any(w in name for w in ["sociolog", "social", "社会"]):
        return "社会学"
    if any(w in name for w in ["psycholog", "cognit", "心理", "認知"]):
        return "心理学"
    if any(w in name for w in ["anthropolog", "人類"]):
        return "人類学"
    if any(w in name for w in ["linguist", "grammar", "言語", "文法"]):
        return "言語学"

    # Engineering subfields
    if any(w in name for w in ["comput", "program", "software", "コンピュ", "プログラ", "ソフト"]):
        return "コンピュータ科学"
    if any(w in name for w in ["electric", "electron", "circuit", "電気", "電子", "回路"]):
        return "電気・電子工学"
    if any(w in name for w in ["mechan", "engine", "機械", "エンジン"]):
        return "機械工学"
    if any(w in name for w in ["civil", "bridge", "building", "土木", "建築"]):
        return "土木工学"
    if any(w in name for w in ["communic", "telegraph", "telephone", "internet", "通信"]):
        return "通信工学"
    if any(w in name for w in ["chemical", "材料", "化学"]):
        return "化学工学"

    # Arts subfields
    if any(w in name for w in ["paint", "abstract", "impress", "cubis", "絵画", "印象", "抽象"]):
        return "絵画・視覚芸術"
    if any(w in name for w in ["music", "compos", "tone", "chant", "音楽", "音"]):
        return "音楽"
    if any(w in name for w in ["architect", "建築"]):
        return "建築"
    if any(w in name for w in ["theater", "drama", "opera", "tragedy", "演劇", "悲劇", "オペラ"]):
        return "演劇・舞台芸術"
    if any(w in name for w in ["cinema", "film", "video", "映画", "ビデオ"]):
        return "映像芸術"
    if any(w in name for w in ["poetry", "literary", "novel", "詩", "文学"]):
        return "文学"
    if any(w in name for w in ["sculpture", "彫刻"]):
        return "彫刻"
    if any(w in name for w in ["design", "デザイン"]):
        return "デザイン"

    return "一般"


def build_relations(concepts):
    """Build genealogical relations based on temporal proximity and shared subfields."""
    relations = []
    by_subfield = {}
    for c in concepts:
        sf = c.get("subfield", "")
        if sf not in by_subfield:
            by_subfield[sf] = []
        by_subfield[sf].append(c)

    for sf, group in by_subfield.items():
        # Sort by era_start
        group.sort(key=lambda x: x["era_start"])

        # Connect chronologically adjacent concepts in same subfield
        for i in range(1, len(group)):
            prev = group[i-1]
            curr = group[i]
            # Only connect if within reasonable time distance
            gap = curr["era_start"] - prev["era_start"]
            if gap <= 200:  # within 200 years
                strength = max(3, min(9, 9 - gap // 30))
                relations.append({
                    "source": prev["name_ja"],
                    "target": curr["name_ja"],
                    "relation_type": "derived_from",
                    "description": f"{prev['name_en']}から{curr['name_en']}への知的発展",
                    "strength": strength,
                })

    return relations


def convert_domain(domain):
    cfg = DOMAIN_CONFIG[domain]
    existing = get_existing_names(cfg["table"])

    tsv_path = OUTPUT_DIR / cfg["output_subdir"] / "research_lists" / "concepts.tsv"
    if not tsv_path.exists():
        print(f"No concept list found: {tsv_path}")
        return

    raw = parse_tsv(tsv_path)
    print(f"Parsed {len(raw)} concepts from {tsv_path}")

    # Filter duplicates
    new = [c for c in raw if c["name_ja"] not in existing and c["name_en"] not in existing]
    print(f"After dedup: {len(new)} new concepts")

    # Build concept records
    concepts = []
    for c in new:
        subfield = infer_subfield(c["name_en"], c["name_ja"])
        concept = {
            "name_ja": c["name_ja"],
            "name_en": c["name_en"],
            "definition": f"{c['name_ja']}（{c['name_en']}）は、{c['key_thinker']}によって{abs(c['era_start'])}年{'BCE' if c['era_start'] < 0 else ''}に提唱された学術的概念。",
            "impact_summary": f"{c['key_thinker']}による{subfield}の基盤的貢献。",
            "subfield": subfield,
            "school_of_thought": c["key_thinker"],
            "era_start": c["era_start"],
            "era_end": None,
            "methodology_level": "theoretical",
            "target_domain": subfield,
            "keywords_ja": f"{c['name_ja']}, {c['key_thinker']}, {subfield}",
            "keywords_en": f"{c['name_en']}, {c['key_thinker']}",
            "status": "foundational",
            "source_reliability": "primary",
            "data_completeness": 70,
        }
        concepts.append(concept)

    # Build relations
    relations = build_relations(concepts)
    print(f"Generated {len(relations)} relations")

    # Merge with existing enriched data if any
    output_path = OUTPUT_DIR / cfg["output_subdir"] / "historical_enriched.json"
    existing_data = {"domain": cfg["domain_key"], "concepts": [], "relations": []}
    if output_path.exists():
        with open(output_path) as f:
            existing_data = json.load(f)
        existing_names_in_file = {c.get("name_en") for c in existing_data.get("concepts", [])}
        # Only add concepts not already in the file
        concepts = [c for c in concepts if c["name_en"] not in existing_names_in_file]
        print(f"After merging with existing file: adding {len(concepts)} new concepts")

    existing_data["concepts"].extend(concepts)
    existing_data["relations"].extend(relations)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"Saved: {output_path}")
    print(f"Total: {len(existing_data['concepts'])} concepts, {len(existing_data['relations'])} relations")
    return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", choices=list(DOMAIN_CONFIG.keys()) + ["all"])
    args = parser.parse_args()

    if args.domain == "all":
        for d in DOMAIN_CONFIG:
            print(f"\n{'='*60}")
            print(f"Processing: {d}")
            print(f"{'='*60}")
            convert_domain(d)
    else:
        convert_domain(args.domain)
