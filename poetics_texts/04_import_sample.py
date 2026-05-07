#!/usr/bin/env python3
"""Import sample 50 poetic texts into academic.db (Phase 1 schema validation)."""

import json
import sqlite3
import uuid
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
SAMPLE = ROOT / "03_sample_50.json"


def main():
    data = json.loads(SAMPLE.read_text())
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=OFF")
    cur = conn.cursor()

    # Existing concept ids for FK validation
    cur.execute("SELECT id FROM humanities_concept")
    valid_concepts = {r[0] for r in cur.fetchall()}

    text_inserted = trans_inserted = link_inserted = motif_inserted = 0
    link_skipped_missing_concept = 0

    for t in data["texts"]:
        cur.execute("""
            INSERT OR IGNORE INTO poetics_text
            (id, title_original, title_ja, title_en, author_id, author_name_display,
             era_year, era_period, culture_region, language_original, form_genre,
             meter_prosody, length_lines, full_text_or_excerpt, excerpt_note,
             public_domain_status, source_url, source_archive, license,
             canonical_tier, notes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            t["id"], t.get("title_original"), t["title_ja"], t.get("title_en"),
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

        for tr in t.get("translations", []) or []:
            cur.execute("""
                INSERT INTO poetics_text_translation
                (id, text_id, translator_name, translator_year, language,
                 translation_text, translation_type, source_url, license, notes)
                VALUES (?,?,?,?,?,?,?,?,?,?)
            """, (str(uuid.uuid4()), t["id"], tr.get("translator_name"),
                  tr.get("translator_year"), tr["language"],
                  tr.get("translation_text"), tr.get("translation_type"),
                  tr.get("source_url"), tr.get("license"), tr.get("notes")))
            trans_inserted += 1

        for ln in t.get("concept_links", []) or []:
            if ln["concept_id"] not in valid_concepts:
                link_skipped_missing_concept += 1
                continue
            cur.execute("""
                INSERT INTO poetics_text_concept_link
                (id, text_id, concept_id, link_type, discussed_by_researcher_id,
                 discussion_locus, strength, notes)
                VALUES (?,?,?,?,?,?,?,?)
            """, (str(uuid.uuid4()), t["id"], ln["concept_id"],
                  ln.get("link_type"), ln.get("discussed_by_researcher_id"),
                  ln.get("discussion_locus"), ln.get("strength", 5),
                  ln.get("notes")))
            link_inserted += 1

        for m in t.get("motifs", []) or []:
            cur.execute("""
                INSERT INTO poetics_text_motif
                (id, text_id, motif_label, motif_category, tradition_specific, notes)
                VALUES (?,?,?,?,?,?)
            """, (str(uuid.uuid4()), t["id"], m["motif_label"],
                  m.get("motif_category"), m.get("tradition_specific"),
                  m.get("notes")))
            motif_inserted += 1

    conn.commit()

    print(f"Texts inserted: {text_inserted}")
    print(f"Translations inserted: {trans_inserted}")
    print(f"Concept links inserted: {link_inserted}")
    print(f"Concept links skipped (concept not in DB): {link_skipped_missing_concept}")
    print(f"Motifs inserted: {motif_inserted}")

    print("\n=== Verification queries ===")
    cur.execute("SELECT culture_region, COUNT(*) FROM poetics_text GROUP BY culture_region ORDER BY 2 DESC")
    print("By culture_region:")
    for cr, n in cur.fetchall():
        print(f"  {cr}: {n}")

    cur.execute("SELECT canonical_tier, COUNT(*) FROM poetics_text GROUP BY canonical_tier")
    print("By tier:", cur.fetchall())

    cur.execute("""
        SELECT hc.name_ja, COUNT(*) AS texts
        FROM poetics_text_concept_link l
        JOIN humanities_concept hc ON hc.id = l.concept_id
        GROUP BY hc.name_ja ORDER BY texts DESC LIMIT 10
    """)
    print("\nTop concepts by linked texts:")
    for n, c in cur.fetchall():
        print(f"  {n}: {c}")

    cur.execute("""
        SELECT t.title_ja, GROUP_CONCAT(hc.name_ja, ' | ') AS concepts
        FROM poetics_text t
        JOIN poetics_text_concept_link l ON l.text_id = t.id
        JOIN humanities_concept hc ON hc.id = l.concept_id
        GROUP BY t.id ORDER BY t.id LIMIT 10
    """)
    print("\nSample text → concept links:")
    for ti, cs in cur.fetchall():
        print(f"  {ti} → {cs}")

    conn.close()


if __name__ == "__main__":
    main()
