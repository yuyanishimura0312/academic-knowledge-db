#!/usr/bin/env python3
"""Phase 8 unified importer: concepts + founding quotes."""
import json
import re
import sqlite3
import uuid
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
CONCEPTS_DIR = Path("/tmp/poetics_concepts_p8")
QUOTES_DIR = Path("/tmp/poetics_quotes_p8")

POETICS_SUBFIELDS = {
    '古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学',
    'ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学'
}


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


def import_concepts():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM humanities_concept")
    existing = {r[0] for r in cur.fetchall()}

    inserted = skipped_existing = skipped_invalid = invalid_subfield = 0
    files_loaded = 0

    for f in sorted(CONCEPTS_DIR.glob("*.json")):
        d = parse_lenient(f.read_text())
        if not d or "concepts" not in d:
            continue
        files_loaded += 1
        for c in d["concepts"]:
            cid = c.get("id")
            if not cid or not c.get("name_ja"):
                skipped_invalid += 1
                continue
            if cid in existing:
                skipped_existing += 1
                continue
            sf = c.get("subfield")
            if sf not in POETICS_SUBFIELDS:
                invalid_subfield += 1
                continue
            existing.add(cid)
            cur.execute("""INSERT INTO humanities_concept
                (id, name_ja, name_en, name_original, definition, impact_summary,
                 subfield, school_of_thought, era_start, era_end, methodology_level,
                 keywords_ja, keywords_en, status, source_reliability, data_completeness)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (cid, c["name_ja"], c.get("name_en"), c.get("name_original"),
                 c.get("definition"), c.get("impact_summary"), sf,
                 c.get("school_of_thought"), c.get("era_start"), c.get("era_end"),
                 c.get("methodology_level"), c.get("keywords_ja"),
                 c.get("keywords_en"), "active", "secondary", 70))
            inserted += 1

    conn.commit()
    conn.close()
    print(f"[concepts] files={files_loaded}, inserted={inserted}, "
          f"skip_existing={skipped_existing}, invalid={skipped_invalid}, "
          f"invalid_subfield={invalid_subfield}")
    return inserted


def import_quotes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM humanities_concept")
    valid_concepts = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT concept_id FROM concept_original_source")
    existing_pairs = {r[0] for r in cur.fetchall()}  # one quote per concept rule (simplified)

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
            quote_orig = q.get("quote_original")
            if not quote_orig:
                skipped_invalid += 1
                continue
            cur.execute("""INSERT INTO concept_original_source
                (id, concept_id, source_type, source_work_title, source_locator,
                 source_year, source_author, source_language, quote_original,
                 quote_japanese, quote_english, quote_significance, related_text_id,
                 source_url, source_archive, public_domain_status)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (str(uuid.uuid4()), cid, q.get("source_type", "founding_text"),
                 q.get("source_work_title"), q.get("source_locator"),
                 q.get("source_year"), q.get("source_author"),
                 q.get("source_language"), quote_orig,
                 q.get("quote_japanese"), q.get("quote_english"),
                 q.get("quote_significance"), q.get("related_text_id"),
                 q.get("source_url"), q.get("source_archive"),
                 q.get("public_domain_status", "PD-original")))
            inserted += 1

    conn.commit()
    conn.close()
    print(f"[quotes] files={files_loaded}, inserted={inserted}, "
          f"skip_no_concept={skipped_no_concept}, invalid={skipped_invalid}")


def main():
    n_concepts = import_concepts()
    import_quotes()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(f"""SELECT subfield, COUNT(*) FROM humanities_concept
                    WHERE subfield IN ({','.join('?'*len(POETICS_SUBFIELDS))})
                    GROUP BY subfield ORDER BY 2 DESC""",
                tuple(POETICS_SUBFIELDS))
    print("\n=== Concepts by subfield ===")
    total = 0
    for sf, n in cur.fetchall():
        print(f"  {sf}: {n}")
        total += n
    print(f"  TOTAL: {total}")

    cur.execute("SELECT COUNT(*) FROM concept_original_source")
    print(f"\nFounding quotes: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM concept_original_source")
    print(f"Concepts with quotes: {cur.fetchone()[0]}")
    cur.execute("SELECT source_author, COUNT(*) FROM concept_original_source WHERE source_author IS NOT NULL GROUP BY source_author ORDER BY 2 DESC LIMIT 10")
    print("\nTop quote authors:")
    for a, n in cur.fetchall():
        print(f"  {a}: {n}")
    conn.close()


if __name__ == "__main__":
    main()
