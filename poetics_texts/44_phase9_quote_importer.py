#!/usr/bin/env python3
"""Phase 9-A importer: ingest /tmp/poetics_quotes_p9/*.json into concept_original_source."""
import json
import re
import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
QUOTES_DIR = Path("/tmp/poetics_quotes_p9")


def parse_lenient(raw):
    raw = raw.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", raw, re.DOTALL)
    if m:
        raw = m.group(1)
    if not raw.startswith("{"):
        s, e = raw.find("{"), raw.rfind("}")
        if s != -1 and e != -1:
            raw = raw[s:e+1]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM humanities_concept")
    valid_concepts = {r[0] for r in cur.fetchall()}

    cur.execute("SELECT concept_id FROM concept_original_source")
    existing_concepts_with_quote = set(r[0] for r in cur.fetchall())

    inserted = skipped_no_concept = skipped_existing = skipped_invalid = 0
    files_loaded = 0

    for f in sorted(QUOTES_DIR.glob("*.json")):
        d = parse_lenient(f.read_text())
        if not d or "quotes" not in d:
            continue
        files_loaded += 1
        for q in d["quotes"]:
            cid = q.get("concept_id")
            if not cid:
                skipped_invalid += 1
                continue
            if cid not in valid_concepts:
                skipped_no_concept += 1
                continue
            if cid in existing_concepts_with_quote:
                skipped_existing += 1
                continue
            quote_orig = q.get("quote_original")
            if not quote_orig:
                skipped_invalid += 1
                continue
            existing_concepts_with_quote.add(cid)
            cur.execute("""INSERT INTO concept_original_source
                (id, concept_id, source_type, source_work_title, source_locator,
                 source_year, source_author, source_language, quote_original,
                 quote_japanese, quote_english, quote_significance,
                 source_url, source_archive, public_domain_status)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), cid, q.get("source_type", "founding_text"),
                 q.get("source_work_title"), q.get("source_locator"),
                 q.get("source_year"), q.get("source_author"),
                 q.get("source_language"), quote_orig,
                 q.get("quote_japanese"), q.get("quote_english"),
                 q.get("quote_significance"), q.get("source_url"),
                 q.get("source_archive"),
                 q.get("public_domain_status", "PD-original")))
            inserted += 1

    conn.commit()

    print(f"=== Phase 9-A quote import ===")
    print(f"Files loaded: {files_loaded}")
    print(f"Inserted: {inserted}")
    print(f"Skipped (concept already has quote): {skipped_existing}")
    print(f"Skipped (no concept): {skipped_no_concept}")
    print(f"Skipped (invalid): {skipped_invalid}")

    cur.execute("SELECT COUNT(*) FROM concept_original_source")
    print(f"\nTotal concept_original_source: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM concept_original_source")
    print(f"Distinct concepts with quotes: {cur.fetchone()[0]}")
    cur.execute("""SELECT source_author, COUNT(*) FROM concept_original_source
                   WHERE source_author IS NOT NULL GROUP BY source_author
                   ORDER BY 2 DESC LIMIT 15""")
    print("\nTop authors:")
    for a, n in cur.fetchall():
        print(f"  {a}: {n}")
    conn.close()


if __name__ == "__main__":
    main()
