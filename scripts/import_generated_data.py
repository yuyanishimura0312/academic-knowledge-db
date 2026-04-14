"""
Import generated JSON data into domain tables.
Handles engineering_method and arts_question domains.
"""

import sqlite3, json, os, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"

# Column mappings per domain
COMMON_COLS = [
    "id", "name_ja", "name_en", "name_original", "definition",
    "impact_summary", "subfield", "school_of_thought",
    "era_start", "era_end", "methodology_level", "target_domain",
    "application_conditions", "when_to_apply", "framing_questions",
    "opposing_concept_names", "keywords_ja", "keywords_en",
    "status", "source_reliability", "data_completeness",
]

ENGINEERING_COLS = COMMON_COLS + [
    "technology_readiness_level", "related_patents",
    "industry_applications", "problem_type", "scientific_basis",
]

ARTS_COLS = COMMON_COLS + [
    "target_assumption", "medium", "representative_works",
    "movement_affiliation", "sensory_dimension",
]

DOMAIN_CONFIG = {
    "engineering": {
        "table": "engineering_method",
        "cols": ENGINEERING_COLS,
    },
    "arts": {
        "table": "arts_question",
        "cols": ARTS_COLS,
    },
}


def import_file(json_path, domain_key):
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return 0

    with open(json_path, "r") as f:
        data = json.load(f)

    config = DOMAIN_CONFIG[domain_key]
    table = config["table"]
    cols = config["cols"]

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    existing = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    if existing > 0:
        print(f"{table} already has {existing} records. Clearing first.")
        cur.execute(f"DELETE FROM {table}")

    inserted = 0
    skipped = 0
    for concept in data.get("concepts", []):
        values = []
        for col in cols:
            val = concept.get(col)
            # Convert lists/dicts to JSON strings
            if isinstance(val, (list, dict)):
                val = json.dumps(val, ensure_ascii=False)
            values.append(val)

        placeholders = ", ".join(["?"] * len(cols))
        col_names = ", ".join(cols)
        try:
            cur.execute(f"INSERT INTO {table} ({col_names}) VALUES ({placeholders})", values)
            inserted += 1
        except Exception as e:
            print(f"  Skip {concept.get('id', '?')}: {e}")
            skipped += 1

    conn.commit()

    # Verify
    total = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table}: inserted {inserted}, skipped {skipped}, total {total}")

    # Show subfield distribution
    subs = cur.execute(f"SELECT subfield, COUNT(*) FROM {table} GROUP BY subfield ORDER BY COUNT(*) DESC LIMIT 10").fetchall()
    for s, c in subs:
        print(f"  {s}: {c}")

    conn.close()
    return inserted


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python import_generated_data.py <json_path> <domain_key>")
        print("  domain_key: engineering or arts")
        sys.exit(1)

    json_path = sys.argv[1]
    domain_key = sys.argv[2]

    if domain_key not in DOMAIN_CONFIG:
        print(f"Unknown domain: {domain_key}")
        sys.exit(1)

    import_file(json_path, domain_key)
