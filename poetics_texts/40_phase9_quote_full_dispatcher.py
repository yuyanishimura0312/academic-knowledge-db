#!/usr/bin/env python3
"""Phase 9-A: 全概念への founding_quote 拡充。
60ワーカーで残2,700+概念をsubfield×era別にバッチ処理。
各worker: 30-40概念ずつ担当、Codex並列で原典引用を生成。
"""
import sqlite3
import subprocess
import json
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
OUTPUT_DIR = Path("/tmp/poetics_quotes_p9")
LOG_DIR = Path("/tmp/poetics_quotes_p9_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

POETICS_SUBFIELDS = ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学',
    '受容理論','認知詩学','比較詩学','デジタル詩学')

PER_WORKER = 35


def fetch_quoteless_concepts():
    """Get concepts without founding quotes, grouped by subfield × era_bucket."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    placeholders = ",".join("?" * len(POETICS_SUBFIELDS))
    cur.execute(f"""
        SELECT hc.id, hc.name_ja, hc.name_en, hc.name_original, hc.subfield,
               hc.school_of_thought, hc.era_start, hc.era_end
        FROM humanities_concept hc
        LEFT JOIN concept_original_source cos ON cos.concept_id = hc.id
        WHERE hc.subfield IN ({placeholders})
        AND cos.id IS NULL
        ORDER BY hc.subfield, COALESCE(hc.era_start, 9999), hc.id
    """, POETICS_SUBFIELDS)
    rows = cur.fetchall()
    conn.close()
    return rows


def era_bucket(year):
    if year is None:
        return "unknown"
    if year < -500:
        return "ancient"
    if year < 500:
        return "classical"
    if year < 1500:
        return "medieval"
    if year < 1800:
        return "early_modern"
    if year < 1900:
        return "19c"
    if year < 1950:
        return "early_20c"
    return "late_20c"


def make_batches(concepts):
    """Group concepts into worker batches by subfield × era × school."""
    groups = {}
    for c in concepts:
        cid, name_ja, name_en, name_orig, sf, school, era_s, era_e = c
        key = (sf, era_bucket(era_s))
        groups.setdefault(key, []).append(c)
    batches = []
    for (sf, era), items in groups.items():
        for i in range(0, len(items), PER_WORKER):
            chunk = items[i:i+PER_WORKER]
            wid = f"{sf[:6]}_{era}_{i//PER_WORKER:02d}"
            wid = wid.replace("・", "_").replace("/", "_").replace(" ", "_")
            batches.append((wid, sf, era, chunk))
    return batches


def build_prompt(wid, sf, era, chunk):
    concept_lines = []
    for cid, name_ja, name_en, name_orig, _, school, era_s, era_e in chunk:
        line = f"  - {cid}: {name_ja}"
        if name_en:
            line += f" ({name_en})"
        if name_orig:
            line += f" [{name_orig}]"
        if school:
            line += f" — {school}"
        concept_lines.append(line)
    cl = "\n".join(concept_lines)
    return f"""For these {len(chunk)} existing poetics concepts in subfield "{sf}" (era: {era}), generate founding-source quotes from original poetics texts.

CONCEPTS (use these EXACT concept_id strings):
{cl}

For each concept, output a single founding_quote record linking it to its founding/key original-source passage. Use your knowledge of the canonical works in this tradition.

OUTPUT (only this JSON, no commentary):
{{"worker_id": "{wid}", "quotes": [
  {{"concept_id": "<exact_id_from_above>",
    "source_type": "founding_text",
    "source_work_title": "<work title>",
    "source_locator": "<book.chapter or page or 巻etc>",
    "source_year": <year>,
    "source_author": "<author>",
    "source_language": "<ISO 639-3>",
    "quote_original": "<2-6 lines of original-language passage>",
    "quote_japanese": "<日本語訳 2-4行>",
    "quote_english": "<English translation 2-4 lines>",
    "quote_significance": "<150-250字 in Japanese: why this passage founds/defines the concept>",
    "source_url": "<URL to PD archive or canonical citation>",
    "source_archive": "<archive name>",
    "public_domain_status": "PD-original or fair-use-excerpt"
  }},
  ... (one per concept above)
]}}

Requirements:
- Use the EXACT concept_id strings (do not invent new ones)
- Original passage in original script (Greek/Sanskrit Devanagari/Chinese/Japanese/Latin/Arabic/Persian/etc)
- Quote MUST be a real attested passage where the concept is established
- If the concept is more recent or no clear founding text exists, use the most representative scholar's key formulation
- Output JSON only."""


def main():
    concepts = fetch_quoteless_concepts()
    print(f"Found {len(concepts)} concepts without quotes")
    batches = make_batches(concepts)
    print(f"Made {len(batches)} batches of ~{PER_WORKER} concepts each")

    # Limit to 60 workers max in this run
    batches = batches[:60]

    procs = []
    log_files = []
    for wid, sf, era, chunk in batches:
        out_file = OUTPUT_DIR / f"P9Q_{wid}.json"
        log_file = LOG_DIR / f"P9Q_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1500:
            print(f"Skip {out_file.name}")
            continue
        prompt = build_prompt(wid, sf, era, chunk)
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(out_file), prompt]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P9Q_{wid} (pid {p.pid}, {len(chunk)} concepts)")

    print(f"\n{len(procs)} quote workers running...")
    for wid, p in procs:
        rc = p.wait()
        print(f"  P9Q_{wid}: exit {rc}")
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
