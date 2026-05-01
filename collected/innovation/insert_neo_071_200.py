#!/usr/bin/env python3
"""Insert neo-Schumpeterian entries 071-200 into innovation_theory table."""

import json
import sqlite3
from pathlib import Path

DB_PATH = Path("/Users/nishimura+/projects/research/academic-knowledge-db/academic.db")
COLLECT_DIR = Path("/Users/nishimura+/projects/research/academic-knowledge-db/collected/innovation")

FILES = [
    "neo_schumpeterian_071_090.json",
    "neo_schumpeterian_091_120.json",
    "neo_schumpeterian_121_150.json",
    "neo_schumpeterian_151_175.json",
    "neo_schumpeterian_176_200.json",
]

INSERT_SQL = """
INSERT OR IGNORE INTO innovation_theory (
    id, name_ja, name_en, definition, impact_summary,
    subfield, school_of_thought, era_start, era_end,
    schumpeter_layer, innovation_type, cognitive_mechanism,
    key_researchers, key_works, keywords_ja, keywords_en,
    opposing_concept_names,
    status, source_reliability, data_completeness
) VALUES (
    :id, :name_ja, :name_en, :definition, :impact_summary,
    :subfield, :school_of_thought, :era_start, :era_end,
    :schumpeter_layer, :innovation_type, :cognitive_mechanism,
    :key_researchers, :key_works, :keywords_ja, :keywords_en,
    :opposing_concept_names,
    'active', 'secondary', 82
)
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    total_inserted = 0
    total_skipped = 0

    for fname in FILES:
        fpath = COLLECT_DIR / fname
        with open(fpath, encoding="utf-8") as f:
            records = json.load(f)

        for rec in records:
            # Convert lists to JSON strings for storage
            row = dict(rec)
            for field in ("key_researchers", "key_works"):
                if isinstance(row.get(field), list):
                    row[field] = json.dumps(row[field], ensure_ascii=False)

            try:
                cur.execute(INSERT_SQL, row)
                if cur.rowcount > 0:
                    total_inserted += 1
                else:
                    total_skipped += 1
                    print(f"  SKIP (already exists): {row['id']}")
            except Exception as e:
                print(f"  ERROR {row['id']}: {e}")

        conn.commit()
        print(f"Processed {fname}: {len(records)} records")

    conn.close()
    print(f"\nDone. Inserted: {total_inserted}, Skipped: {total_skipped}")

if __name__ == "__main__":
    main()
