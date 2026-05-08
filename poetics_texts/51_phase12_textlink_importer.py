#!/usr/bin/env python3
"""Phase 12-A importer: ingest /tmp/poetics_textlinks_p12/*.json into poetics_text_concept_link."""
import json
import re
import sqlite3
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
LINKS_DIR = Path("/tmp/poetics_textlinks_p12")


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
    cur.execute("SELECT id FROM humanities_concept WHERE id LIKE 'cp_%'")
    valid_concepts = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM poetics_text")
    valid_texts = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT concept_id, text_id FROM poetics_text_concept_link")
    existing = {(r[0], r[1]) for r in cur.fetchall()}

    inserted = skipped_no_concept = skipped_no_text = skipped_existing = skipped_invalid = 0
    files_loaded = 0
    for f in sorted(LINKS_DIR.glob("*.json")):
        d = parse_lenient(f.read_text())
        if not d or "links" not in d:
            continue
        files_loaded += 1
        for ln in d["links"]:
            cid = ln.get("concept_id")
            tid = ln.get("text_id")
            if not cid or not tid:
                skipped_invalid += 1
                continue
            if cid not in valid_concepts:
                skipped_no_concept += 1
                continue
            if tid not in valid_texts:
                skipped_no_text += 1
                continue
            if (cid, tid) in existing:
                skipped_existing += 1
                continue
            existing.add((cid, tid))
            cur.execute("""INSERT INTO poetics_text_concept_link
                (id, text_id, concept_id, link_type, discussion_locus, strength, notes)
                VALUES (?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), tid, cid,
                 ln.get("link_type", "例証"),
                 ln.get("discussion_locus"),
                 ln.get("strength", 7), None))
            inserted += 1
    conn.commit()

    print(f"=== Phase 12-A textlink import ===")
    print(f"Files: {files_loaded}")
    print(f"Inserted: {inserted}")
    print(f"Skipped (existing): {skipped_existing}")
    print(f"Skipped (no concept): {skipped_no_concept}")
    print(f"Skipped (no text): {skipped_no_text}")
    print(f"Skipped (invalid): {skipped_invalid}")

    cur.execute("SELECT COUNT(*) FROM poetics_text_concept_link")
    print(f"\nTotal text-concept links: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM poetics_text_concept_link")
    print(f"Distinct concepts with text-links: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
