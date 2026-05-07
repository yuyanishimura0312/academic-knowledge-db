#!/usr/bin/env python3
"""Phase 6 unified importer: Codex p6 + Claude agent batches + earlier batches."""
import json
import re
import sqlite3
import uuid
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
CODEX_P6 = Path("/tmp/poetics_texts_p6")
CODEX_P2 = Path("/tmp/poetics_texts_p2")
CODEX_P7 = Path("/tmp/poetics_texts_p7")


def parse_json_lenient(raw: str):
    """Handle markdown fences, leading/trailing junk."""
    raw = raw.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", raw, re.DOTALL)
    if m:
        raw = m.group(1)
    if not raw.startswith("{"):
        # Try to find first { ... last }
        s = raw.find("{")
        e = raw.rfind("}")
        if s != -1 and e != -1:
            raw = raw[s:e+1]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def load_all_texts():
    texts = []
    sources = []

    # Codex p6 (40-worker round)
    for f in sorted(CODEX_P6.glob("*.json")):
        d = parse_json_lenient(f.read_text())
        if d and "texts" in d:
            n = len(d["texts"])
            if n > 0:
                sources.append((f.name, n, "codex_p6"))
                texts.extend(d["texts"])

    # Codex p7 (Phase 7 diversified)
    for f in sorted(CODEX_P7.glob("*.json")):
        d = parse_json_lenient(f.read_text())
        if d and "texts" in d and d["texts"]:
            sources.append((f.name, len(d["texts"]), "codex_p7"))
            texts.extend(d["texts"])

    # Codex p2 (Phase 2 round) — already imported but include in case
    for f in sorted(CODEX_P2.glob("B*.json")):
        d = parse_json_lenient(f.read_text())
        if d and "texts" in d and d["texts"]:
            sources.append((f.name, len(d["texts"]), "codex_p2"))
            texts.extend(d["texts"])

    # Claude batches (07, 10, 11, 12, 15, 16)
    for batch_name in ["07_batch_generated.json", "10_batch2_greek_roman_china.json",
                       "11_batch3_japan_buddhist_indic.json", "12_batch4_european.json",
                       "15_batch5_chinese_canon.json", "16_batch6_japan_canon.json",
                       "17_batch7_sanskrit_persian.json",
                       "18_batch8_european_extended.json",
                       "19_batch9_gaps_fill.json",
                       "21_batch_bengali.json",
                       "22_batch_vietnamese_korean.json",
                       "23_batch_african_indigenous.json",
                       "24_batch_european_eastern.json",
                       "25_batch_anglo_modern.json",
                       "26_batch_misc_filler.json",
                       "27_batch_european_more.json"]:
        bf = ROOT / batch_name
        if bf.exists():
            d = json.loads(bf.read_text())
            n = len(d.get("texts", []))
            sources.append((bf.name, n, "claude_phase2-5"))
            texts.extend(d["texts"])

    # Claude phase6 agents (A-J)
    for f in sorted(ROOT.glob("agent_*.json")):
        d = parse_json_lenient(f.read_text())
        if d and "texts" in d:
            n = len(d["texts"])
            sources.append((f.name, n, "claude_p6"))
            texts.extend(d["texts"])

    return texts, sources


def main():
    texts, sources = load_all_texts()
    print("=== Source files ===")
    for name, n, kind in sources:
        print(f"  [{kind}] {name}: {n}")
    print(f"\nTotal candidate texts: {len(texts)}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=OFF")
    cur = conn.cursor()

    cur.execute("SELECT id FROM humanities_concept")
    valid_concepts = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT id FROM poetics_text")
    seen_ids = set(r[0] for r in cur.fetchall())

    text_ins = trans_ins = link_ins = motif_ins = 0
    skipped_existing = skipped_invalid = skipped_dup_in_batch = 0
    link_skipped = 0

    for t in texts:
        tid = t.get("id")
        if not tid or not t.get("title_ja") or not t.get("culture_region"):
            skipped_invalid += 1
            continue
        if tid in seen_ids:
            skipped_dup_in_batch += 1
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
            text_ins += 1

        for tr in t.get("translations") or []:
            cur.execute("""
                INSERT INTO poetics_text_translation
                (id, text_id, translator_name, translator_year, language,
                 translation_text, translation_type, source_url, license, notes)
                VALUES (?,?,?,?,?,?,?,?,?,?)
            """, (str(uuid.uuid4()), tid, tr.get("translator_name"),
                  tr.get("translator_year"), tr.get("language") or "en",
                  tr.get("translation_text"), tr.get("translation_type"),
                  tr.get("source_url"), tr.get("license"), tr.get("notes")))
            trans_ins += 1

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
            link_ins += 1

        for m in t.get("motifs") or []:
            if not m.get("motif_label"):
                continue
            cur.execute("""
                INSERT INTO poetics_text_motif
                (id, text_id, motif_label, motif_category, tradition_specific, notes)
                VALUES (?,?,?,?,?,?)
            """, (str(uuid.uuid4()), tid, m["motif_label"],
                  m.get("motif_category"), m.get("tradition_specific"),
                  m.get("notes")))
            motif_ins += 1

    conn.commit()

    print(f"\n=== Phase 6 import results ===")
    print(f"Texts inserted: {text_ins}")
    print(f"Translations inserted: {trans_ins}")
    print(f"Concept links inserted: {link_ins}  (skipped: {link_skipped})")
    print(f"Motifs inserted: {motif_ins}")
    print(f"Skipped (already exists): {skipped_dup_in_batch}")
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
