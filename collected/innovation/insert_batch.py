#!/usr/bin/env python3
"""Insert innovation_theory JSON batch into academic.db"""
import json
import sqlite3
import sys
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"


def insert_batch(json_path: str) -> None:
    with open(json_path, encoding="utf-8") as f:
        records = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    inserted = 0
    skipped = 0
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    for r in records:
        try:
            cur.execute(
                """
                INSERT OR IGNORE INTO innovation_theory (
                    id, name_ja, name_en, definition, impact_summary,
                    subfield, category, era_start, schumpeter_layer,
                    key_researchers, key_works, industry_tags,
                    status, source_reliability, data_completeness,
                    created_at, updated_at
                ) VALUES (
                    :id, :name_ja, :name_en, :definition, :impact_summary,
                    :subfield, :category, :era_start, :schumpeter_layer,
                    :key_researchers, :key_works, :industry_tags,
                    'active', 'secondary', 80,
                    :now, :now
                )
                """,
                {
                    "id": r["id"],
                    "name_ja": r.get("name_ja", ""),
                    "name_en": r.get("name_en", ""),
                    "definition": r.get("definition", ""),
                    "impact_summary": r.get("impact_summary", ""),
                    "subfield": r.get("subfield", "sectoral_innovation_patterns"),
                    "category": r.get("category", "D_directionality"),
                    "era_start": r.get("era_start"),
                    "schumpeter_layer": r.get("schumpeter_layer", "meso"),
                    "key_researchers": json.dumps(r.get("key_researchers", []), ensure_ascii=False),
                    "key_works": json.dumps(r.get("key_works", []), ensure_ascii=False),
                    "industry_tags": r.get("industry_tags", ""),
                    "now": now,
                },
            )
            if cur.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"ERROR on {r.get('id')}: {e}", file=sys.stderr)

    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped (duplicate): {skipped}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: insert_batch.py <json_path>")
        sys.exit(1)
    insert_batch(sys.argv[1])
