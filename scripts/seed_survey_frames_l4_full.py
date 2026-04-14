"""
Level 4 細目（包括的版）を survey_frame に投入するスクリプト
5分野×各L3あたり8-15件 = 合計2,000-4,000件を目標

生成済みの /tmp/l4_*.py ファイルを読み込んで一括投入する。
既存 L4 を全削除してから再投入（L1/L2/L3 は保持）。
"""

import sqlite3, os, uuid, sys, importlib.util

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

DOMAIN_FILES = {
    "social_theory":      "/tmp/l4_social_theory.py",
    "natural_discovery":   "/tmp/l4_natural_discovery.py",
    "humanities_concept":  "/tmp/l4_humanities_concept.py",
    "engineering_method":  "/tmp/l4_engineering_method.py",
    "arts_question":       "/tmp/l4_arts_question.py",
}

DOMAIN_VARNAMES = {
    "social_theory":      "SOCIAL_THEORY_L4",
    "natural_discovery":   "NATURAL_DISCOVERY_L4",
    "humanities_concept":  "HUMANITIES_CONCEPT_L4",
    "engineering_method":  "ENGINEERING_METHOD_L4",
    "arts_question":       "ARTS_QUESTION_L4",
}


def load_l4_data(filepath, varname):
    """Load L4 list from a generated Python file."""
    spec = importlib.util.spec_from_file_location("l4mod", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, varname)


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Build L3 lookup: (domain, name) -> id
    rows = cur.execute(
        "SELECT domain, name, id FROM survey_frame WHERE level=3"
    ).fetchall()
    l3_map = {(r[0], r[1]): r[2] for r in rows}

    # Delete existing L4
    cur.execute("DELETE FROM survey_frame WHERE level=4")
    print(f"Existing L4 deleted")

    total = 0
    skip = 0
    domain_counts = {}

    for domain, filepath in DOMAIN_FILES.items():
        if not os.path.exists(filepath):
            print(f"  SKIP {domain}: {filepath} not found")
            continue

        varname = DOMAIN_VARNAMES[domain]
        entries = load_l4_data(filepath, varname)
        count = 0

        for entry in entries:
            parent_name, name, name_en, desc, priority = entry
            parent_id = l3_map.get((domain, parent_name))

            if not parent_id:
                print(f"  WARNING: L3 '{parent_name}' not found in {domain}, skipping '{name}'")
                skip += 1
                continue

            uid = str(uuid.uuid4())
            cur.execute(
                """INSERT INTO survey_frame
                   (id, domain, level, parent_id, name, name_en, description,
                    survey_priority)
                   VALUES (?, ?, 4, ?, ?, ?, ?, ?)""",
                (uid, domain, parent_id, name, name_en, desc, priority)
            )
            count += 1

        domain_counts[domain] = count
        total += count

    conn.commit()
    conn.close()

    print(f"\nL4 insertion complete: {total} entries, {skip} skipped")
    for domain, count in domain_counts.items():
        print(f"  {domain}: {count}")
    print(f"  Total: {total}")


if __name__ == "__main__":
    main()
