#!/usr/bin/env python3
"""Phase 2 unified importer: Codex bucket outputs + Claude-direct batch.

Handles:
- /tmp/poetics_texts_p2/B*.json (Codex output, may have markdown wrappers)
- 07_batch_generated.json (Claude direct)

Idempotent: skips already-imported text IDs.
"""

import json
import re
import sqlite3
import uuid
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
CODEX_DIR = Path("/tmp/poetics_texts_p2")
BATCH_FILE = ROOT / "07_batch_generated.json"


def load_codex_json(path: Path):
    raw = path.read_text()
    # Strip markdown fences if present
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if m:
        raw = m.group(1)
    raw = raw.strip()
    if not raw.startswith("{"):
        return None
    try:
        d = json.loads(raw)
        return d.get("texts", [])
    except json.JSONDecodeError:
        return None


def load_all_texts():
    texts = []
    # Codex bucket files
    for f in sorted(CODEX_DIR.glob("B*.json")):
        items = load_codex_json(f)
        if items:
            print(f"  {f.name}: {len(items)} texts")
            texts.extend(items)
    # Claude batch
    if BATCH_FILE.exists():
        d = json.loads(BATCH_FILE.read_text())
        items = d.get("texts", [])
        print(f"  {BATCH_FILE.name}: {len(items)} texts")
        texts.extend(items)
    return texts


def main():
    texts = load_all_texts()
    print(f"Total candidate texts: {len(texts)}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=OFF")
    cur = conn.cursor()

    cur.execute("SELECT id FROM humanities_concept")
    valid_concepts = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM poetics_text")
    existing_text_ids = {r[0] for r in cur.fetchall()}

    text_inserted = trans_inserted = link_inserted = motif_inserted = 0
    link_skipped = 0
    skipped_existing = skipped_invalid = 0
    seen_ids = set(existing_text_ids)

    for t in texts:
        tid = t.get("id")
        if not tid or not t.get("title_ja") or not t.get("culture_region"):
            skipped_invalid += 1
            continue
        if tid in seen_ids:
            skipped_existing += 1
            continue
        seen_ids.add(tid)
        cur.execute("""
            INSERT OR IGNORE INTO poetics_text
            (id, title_original, title_ja, title_en, author_id, author_name_display,
             era_year, era_period, culture_region, language_original, form_genre,
             meter_prosody, length_lines, full_text_or_excerpt, excerpt_note,
             public_domain_status, source_url, source_archive, license,
             canonical_tier, notes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            tid, t.get("title_original"), t["title_ja"], t.get("title_en"),
            t.get("author_id"), t.get("author_name_display"),
            t.get("era_year"), t.get("era_period"), t["culture_region"],
            t.get("language_original"), t.get("form_genre"),
            t.get("meter_prosody"), t.get("length_lines"),
            t.get("full_text_or_excerpt"), t.get("excerpt_note"),
            t.get("public_domain_status"), t.get("source_url"),
            t.get("source_archive"), t.get("license"),
            t.get("canonical_tier"), t.get("notes")
        ))
        if cur.rowcount:
            text_inserted += 1

        for tr in t.get("translations") or []:
            cur.execute("""
                INSERT INTO poetics_text_translation
                (id, text_id, translator_name, translator_year, language,
                 translation_text, translation_type, source_url, license, notes)
                VALUES (?,?,?,?,?,?,?,?,?,?)
            """, (str(uuid.uuid4()), tid, tr.get("translator_name"),
                  tr.get("translator_year"), tr["language"],
                  tr.get("translation_text"), tr.get("translation_type"),
                  tr.get("source_url"), tr.get("license"), tr.get("notes")))
            trans_inserted += 1

        for ln in t.get("concept_links") or []:
            if ln.get("concept_id") not in valid_concepts:
                link_skipped += 1
                continue
            cur.execute("""
                INSERT INTO poetics_text_concept_link
                (id, text_id, concept_id, link_type, discussed_by_researcher_id,
                 discussion_locus, strength, notes)
                VALUES (?,?,?,?,?,?,?,?)
            """, (str(uuid.uuid4()), tid, ln["concept_id"],
                  ln.get("link_type"), ln.get("discussed_by_researcher_id"),
                  ln.get("discussion_locus"), ln.get("strength", 5),
                  ln.get("notes")))
            link_inserted += 1

        for m in t.get("motifs") or []:
            cur.execute("""
                INSERT INTO poetics_text_motif
                (id, text_id, motif_label, motif_category, tradition_specific, notes)
                VALUES (?,?,?,?,?,?)
            """, (str(uuid.uuid4()), tid, m["motif_label"],
                  m.get("motif_category"), m.get("tradition_specific"),
                  m.get("notes")))
            motif_inserted += 1

    conn.commit()

    print(f"\n=== Phase 2 import results ===")
    print(f"Texts inserted: {text_inserted}")
    print(f"Translations inserted: {trans_inserted}")
    print(f"Concept links inserted: {link_inserted}")
    print(f"Concept links skipped: {link_skipped}")
    print(f"Motifs inserted: {motif_inserted}")
    print(f"Skipped (already exists): {skipped_existing}")
    print(f"Skipped (invalid): {skipped_invalid}")

    cur.execute("SELECT culture_region, COUNT(*) FROM poetics_text GROUP BY culture_region ORDER BY 2 DESC")
    print("\nFinal by culture_region:")
    for cr, n in cur.fetchall():
        print(f"  {cr}: {n}")

    cur.execute("SELECT COUNT(*) FROM poetics_text")
    print(f"\nTotal poetics_text: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM poetics_text_concept_link")
    print(f"Total concept_links: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM poetics_text_motif")
    print(f"Total motifs: {cur.fetchone()[0]}")

    conn.close()


if __name__ == "__main__":
    main()
