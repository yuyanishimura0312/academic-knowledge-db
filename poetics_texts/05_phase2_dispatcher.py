#!/usr/bin/env python3
"""Phase 2 dispatcher: launch 28 Codex workers in parallel for 28 culture-region buckets.

Each worker collects ~30-50 canonical poetic texts for its bucket.
Outputs JSON files to /tmp/poetics_texts_p2/B##_<id>.json
Logs to /tmp/poetics_texts_p2_logs/B##_<id>.log
"""
import json
import subprocess
import os
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT_DIR = Path("/tmp/poetics_texts_p2")
LOG_DIR = Path("/tmp/poetics_texts_p2_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

BUCKETS = json.loads((ROOT / "02_skeleton_buckets.json").read_text())["buckets"]

# Practical target per bucket for Phase 2 (will not aim for full skeleton target —
# instead each bucket gets a manageable batch of ~30-50 highest canonical items).
PER_BUCKET_TARGET = 35

EXISTING_CONCEPTS_FILE = OUTPUT_DIR / "_existing_concept_ids.txt"
EXISTING_RESEARCHERS_FILE = OUTPUT_DIR / "_existing_researcher_ids.txt"


def export_existing_ids():
    """Export current concept/researcher IDs so Codex avoids duplicates."""
    import sqlite3
    db = ROOT.parent / "academic.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT id, name_ja FROM humanities_concept WHERE subfield IN ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム','近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学','受容理論','認知詩学','比較詩学','デジタル詩学')")
    with open(EXISTING_CONCEPTS_FILE, "w") as f:
        for cid, name in cur.fetchall():
            f.write(f"{cid}\t{name}\n")
    cur.execute("SELECT id, COALESCE(name_ja, name_full) FROM researchers")
    with open(EXISTING_RESEARCHERS_FILE, "w") as f:
        for rid, name in cur.fetchall():
            f.write(f"{rid}\t{name or ''}\n")
    conn.close()
    print(f"Exported existing IDs: {EXISTING_CONCEPTS_FILE}, {EXISTING_RESEARCHERS_FILE}")


def build_prompt(bucket: dict) -> str:
    examples = ", ".join(bucket["examples"][:20])
    return f"""You are collecting canonical poetic texts for the Poetics DB v2.0 (詩文層).
Your task: collect {PER_BUCKET_TARGET} canonical poetic texts for ONE bucket.

BUCKET: {bucket['id']}
culture_region: {bucket['culture_region']}
era_period: {bucket['era_period']}
era_year_range: {bucket['era_year_range']}
languages: {bucket['languages']}
source_archive: {bucket['source_archive']}
canonical examples: {examples}

REQUIREMENTS:
1. Output ONLY a single JSON object to stdout (no other text), with this structure:
   {{"bucket_id": "{bucket['id']}", "texts": [...]}}

2. Each text in the array must include:
   - id: snake_case unique, prefixed "pt_text_" (e.g. pt_text_libai_yuexia_duzhuo)
   - title_original: original-script title (Greek/Latin/Chinese/Japanese/Sanskrit/Arabic/Persian as appropriate)
   - title_ja: Japanese title
   - title_en: English title (transliterated when needed)
   - author_name_display: author name (PD authors only)
   - era_year: integer year (negative = BCE)
   - era_period: short period label
   - culture_region: "{bucket['culture_region']}"
   - language_original: ISO 639-3 code
   - form_genre: poetic form
   - meter_prosody: meter when known
   - length_lines: number of lines in the excerpt or full poem
   - full_text_or_excerpt: the actual text (REAL content, not placeholder).
     For long poems, include only the canonical opening passage (4-12 lines).
     For short poems, include the full text.
     Use original-script characters (Chinese hanzi, Greek, Sanskrit Devanagari, Arabic, etc.)
   - excerpt_note: which part of the work this excerpts (e.g. "Book 1.1-9")
   - public_domain_status: "PD-original" for pre-1929 works
   - source_url: a stable URL to a recognized PD archive (Perseus / Project Gutenberg / Wikisource / 維基文庫 / 青空文庫 / GRETIL / Ganjoor / Bibliotheca Augustana / The Latin Library)
   - source_archive: name of that archive
   - canonical_tier: 1 (canon), 2 (theory-linked), or 3 (cross-cultural) per bucket distribution
   - motifs: optional array [{{"motif_label":"...","motif_category":"..."}}]
   - concept_links: optional array [{{"concept_id":"existing_id","link_type":"例証|分析対象|批判対象|影響源","discussion_locus":"..."}}]

3. CRITICAL ACCURACY RULES:
   - Only include works that are genuinely public-domain (author died before 1929, or pre-modern).
   - Use REAL canonical opening lines you are confident about. Do NOT fabricate text.
   - When uncertain about exact wording, use a shorter excerpt (2-4 lines) you are sure of.
   - source_url must point to a real archive page that hosts the work.
   - Avoid duplicating works (one entry per work; if multi-canto, pick one representative passage).

4. Do not output any explanation, only the JSON object.
"""


def main():
    export_existing_ids()
    procs = []
    for b in BUCKETS:
        out_file = OUTPUT_DIR / f"{b['id']}.json"
        log_file = LOG_DIR / f"{b['id']}.log"
        if out_file.exists() and out_file.stat().st_size > 500:
            print(f"Skip {b['id']} (already has output)")
            continue
        prompt = build_prompt(b)
        # Codex CLI invocation: write prompt to stdin, capture stdout to JSON file.
        # Using `codex exec` for non-interactive mode.
        cmd = [
            "codex", "exec",
            "--skip-git-repo-check",
            "--sandbox", "read-only",
            "--output-last-message", str(out_file),
            prompt,
        ]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((b["id"], p, log))
        print(f"Launched {b['id']} (pid {p.pid})")

    print(f"\n{len(procs)} workers launched. Waiting...")
    for bid, p, log in procs:
        rc = p.wait()
        log.close()
        print(f"  {bid}: exit {rc}")

    print("\nAll done. Outputs:")
    for f in sorted(OUTPUT_DIR.glob("B*.json")):
        size = f.stat().st_size
        print(f"  {f.name}: {size} bytes")


if __name__ == "__main__":
    main()
