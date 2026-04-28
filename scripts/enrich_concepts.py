#!/usr/bin/env python3
"""
Enrich a list of researched concepts with detailed fields via Claude API.
Input: TSV file with columns: era_start | name_en | name_ja | key_thinker
Output: import_v3.py compatible JSON files.

This script takes a research-verified concept list and adds the detailed
academic fields required by the database schema.
"""

import json
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT_DIR = Path(__file__).parent.parent / "collected"

DOMAIN_SPECIFIC_FIELDS = {
    "humanities": {
        "table": "humanities_concept",
        "domain_key": "humanities",
        "fields": ["blind_spot_addressed", "reinterpretation_history", "cultural_context"],
        "relation_types": ["derived_from", "critiques", "reinterprets", "extends", "opposes", "synthesizes", "complements"],
    },
    "natural_sciences": {
        "table": "natural_discovery",
        "domain_key": "natural_sciences",
        "fields": ["mathematical_formulation", "experimental_verification", "applicable_scale", "precision_level"],
        "relation_types": ["derived_from", "generalizes", "experimentally_confirms", "contradicts", "supersedes", "enables", "complements"],
    },
    "social_sciences": {
        "table": "social_theory",
        "domain_key": "social_sciences",
        "fields": ["predictive_power", "operationalization", "empirical_support", "policy_implications"],
        "relation_types": ["derived_from", "critiques", "extends", "empirically_tests", "synthesizes", "competes_with", "applies_to_policy", "complements"],
    },
    "engineering": {
        "table": "engineering_method",
        "domain_key": "engineering",
        "fields": ["technology_readiness_level", "related_patents", "industry_applications", "problem_type", "scientific_basis"],
        "relation_types": ["derived_from", "improves", "supersedes", "combines", "based_on", "standardizes", "complements"],
    },
    "arts": {
        "table": "arts_question",
        "domain_key": "arts",
        "fields": ["target_assumption", "medium", "representative_works", "movement_affiliation", "sensory_dimension"],
        "relation_types": ["derived_from", "deepens", "counters", "translates_medium", "revives", "inspires", "complements"],
    },
}


def get_api_key():
    result = subprocess.run(
        ["security", "find-generic-password", "-a", "anthropic", "-w"],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def get_existing_names(table):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(f"SELECT name_ja, name_en FROM {table}").fetchall()
    conn.close()
    names = set()
    for r in rows:
        if r[0]: names.add(r[0])
        if r[1]: names.add(r[1])
    return names


def parse_concept_list(filepath):
    """Parse a TSV/pipe-separated concept list file."""
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


def call_claude_api(prompt, api_key, max_tokens=8000):
    import urllib.request

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=180) as resp:
        result = json.loads(resp.read())

    return result["content"][0]["text"]


def extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        start = 1
        end = len(lines) - 1
        if lines[-1].strip() == "```":
            text = "\n".join(lines[start:end])
        else:
            text = "\n".join(lines[start:])
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in text
        start = text.find("{")
        if start >= 0:
            # Try progressively shorter substrings to find valid JSON
            for end_pos in range(len(text), start, -1):
                try:
                    return json.loads(text[start:end_pos])
                except json.JSONDecodeError:
                    continue
        raise


def build_enrichment_prompt(domain, concepts_batch, existing_names):
    cfg = DOMAIN_SPECIFIC_FIELDS[domain]
    specific = cfg["fields"]
    rel_types = cfg["relation_types"]

    concept_list = "\n".join(
        f"  {i+1}. {c['name_ja']} ({c['name_en']}, {c['era_start']}年, {c['key_thinker']})"
        for i, c in enumerate(concepts_batch)
    )

    field_descriptions = {
        "blind_spot_addressed": "この概念が照らす学問的盲点（1-2文）",
        "reinterpretation_history": "再解釈の歴史（1-2文）",
        "cultural_context": "文化的文脈（1-2文）",
        "predictive_power": "予測力の評価（1文）",
        "operationalization": "操作化の方法（1文）",
        "empirical_support": "経験的裏付け（1文）",
        "policy_implications": "政策的含意（1文）",
        "mathematical_formulation": "数学的定式化（あれば）",
        "experimental_verification": "実験的検証の状態",
        "applicable_scale": "適用スケール",
        "precision_level": "精度レベル",
        "technology_readiness_level": "技術成熟度（1-9の整数）",
        "related_patents": "関連特許（あれば）",
        "industry_applications": "産業応用",
        "problem_type": "問題タイプ",
        "scientific_basis": "科学的基盤",
        "target_assumption": "問い直す前提",
        "medium": "媒体",
        "representative_works": "代表作品",
        "movement_affiliation": "所属運動",
        "sensory_dimension": "感覚次元",
    }

    specific_desc = "\n".join(f'      "{f}": "{field_descriptions.get(f, f)}"' for f in specific)

    return f"""以下のリサーチ済み学術概念に対して、データベース登録用の詳細フィールドを補完してください。

## 概念リスト（リサーチ検証済み）
{concept_list}

## 出力形式
JSONのみ出力してください。

{{
  "domain": "{cfg['domain_key']}",
  "concepts": [
    {{
      "name_ja": "概念の日本語名（上記リストのまま）",
      "name_en": "English name（上記リストのまま）",
      "era_start": 年（上記リストのまま）,
      "era_end": null,
      "definition": "概念の定義（2-3文、学術的に正確に）",
      "impact_summary": "学問的影響の要約（1-2文）",
      "subfield": "所属サブフィールド（日本語）",
      "school_of_thought": "所属学派（日本語）",
      "methodology_level": "theoretical/empirical/meta-theoretical",
      "target_domain": "適用対象領域",
      "application_conditions": "適用条件",
      "when_to_apply": "この概念を使うべき場面",
      "framing_questions": "この概念が提起する問い",
      "opposing_concept_names": "対立する概念名",
      "keywords_ja": "キーワード1, キーワード2, キーワード3",
      "keywords_en": "keyword1, keyword2, keyword3",
      "status": "foundational",
      "source_reliability": "primary",
      "data_completeness": 85,
{specific_desc}
    }}
  ],
  "relations": [
    {{
      "source": "概念Aの日本語名",
      "target": "概念Bの日本語名",
      "relation_type": "derived_from等",
      "description": "関係の説明（1文）",
      "strength": 7
    }}
  ]
}}

## 注意事項
1. name_ja, name_en, era_startはリサーチ済みなのでそのまま使用
2. 各概念に2-3のrelationsを含めること（バッチ内概念同士の関係を優先）
3. relation_typeは: {', '.join(rel_types)} のみ使用可能
4. definitionは学術的に正確に記述
5. strengthは1-9（系譜的に重要な関係ほど高い値）
"""


def enrich_and_save(domain, concept_list_file, batch_size=10):
    """Enrich researched concepts and save as import-ready JSON."""
    cfg = DOMAIN_SPECIFIC_FIELDS[domain]
    api_key = get_api_key()
    existing = get_existing_names(cfg["table"])

    # Parse concept list
    concepts = parse_concept_list(concept_list_file)
    print(f"Parsed {len(concepts)} concepts from {concept_list_file}")

    # Filter out existing
    new_concepts = [c for c in concepts if c["name_ja"] not in existing and c["name_en"] not in existing]
    print(f"After dedup: {len(new_concepts)} new concepts")

    # Load existing enriched data if any
    output_dir = OUTPUT_DIR / domain.replace("_sciences", "_sciences")
    if domain == "natural_sciences":
        output_dir = OUTPUT_DIR / "natural_sciences"
    elif domain == "social_sciences":
        output_dir = OUTPUT_DIR / "social_sciences"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "historical_enriched.json"

    all_enriched = {"domain": cfg["domain_key"], "concepts": [], "relations": []}
    if output_path.exists():
        with open(output_path) as f:
            all_enriched = json.load(f)
        already_done = {c.get("name_en") for c in all_enriched.get("concepts", [])}
        new_concepts = [c for c in new_concepts if c["name_en"] not in already_done]
        print(f"Resuming: {len(all_enriched['concepts'])} already enriched, {len(new_concepts)} remaining")

    # Process in batches
    for i in range(0, len(new_concepts), batch_size):
        batch = new_concepts[i:i+batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(new_concepts) + batch_size - 1) // batch_size

        print(f"\n  Batch {batch_num}/{total_batches} ({len(batch)} concepts)...")

        prompt = build_enrichment_prompt(domain, batch, existing)

        try:
            response = call_claude_api(prompt, api_key)
            data = extract_json(response)

            concepts_out = data.get("concepts", [])
            relations_out = data.get("relations", [])
            all_enriched["concepts"].extend(concepts_out)
            all_enriched["relations"].extend(relations_out)

            print(f"    Enriched: {len(concepts_out)} concepts, {len(relations_out)} relations")

            # Save after each batch for resilience
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(all_enriched, f, ensure_ascii=False, indent=2)

            # Rate limit
            time.sleep(1)

        except Exception as e:
            print(f"    ERROR: {e}")
            # Continue to next batch instead of stopping
            time.sleep(2)
            continue

    # Save output
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_enriched, f, ensure_ascii=False, indent=2)

    print(f"\nSaved: {output_path}")
    print(f"Total: {len(all_enriched['concepts'])} concepts, {len(all_enriched['relations'])} relations")
    return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Enrich researched concepts with detailed fields")
    parser.add_argument("domain", choices=list(DOMAIN_SPECIFIC_FIELDS.keys()))
    parser.add_argument("concept_list", help="Path to pipe-separated concept list file")
    parser.add_argument("--batch-size", type=int, default=10, help="Concepts per API call")
    args = parser.parse_args()

    enrich_and_save(args.domain, args.concept_list, args.batch_size)
