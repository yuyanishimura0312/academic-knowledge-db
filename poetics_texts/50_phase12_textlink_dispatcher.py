#!/usr/bin/env python3
"""Phase 12-A: 引用付き概念→詩文リンクの大規模生成。

Each worker takes ~30 quoted concepts (with their quote metadata) plus a
sampled corpus of relevant poetics_text entries, and produces concept→text
links based on era proximity, author overlap, theme, culture region.
"""
import sqlite3
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT.parent / "academic.db"
OUTPUT_DIR = Path("/tmp/poetics_textlinks_p12")
LOG_DIR = Path("/tmp/poetics_textlinks_p12_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

POETICS_SUBFIELDS = ('古典詩学','修辞学・弁論術','構造主義詩学','ロシア・フォルマリズム',
    '近代美学・詩学','現象学的詩学','中世・ルネサンス詩学','ポスト構造主義詩学',
    '受容理論','認知詩学','比較詩学','デジタル詩学')

PER_WORKER = 25  # concepts per worker
MAX_TEXTS_HINT = 30  # candidate texts shown to worker


def fetch_quoteless_textlink_concepts():
    """Concepts with quote but no text-link (poetics cp_ prefix)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT hc.id, hc.name_ja, hc.name_en, hc.subfield,
               hc.school_of_thought, hc.era_start,
               cos.source_work_title, cos.source_author, cos.source_year, cos.source_language
        FROM humanities_concept hc
        JOIN concept_original_source cos ON cos.concept_id = hc.id
        WHERE hc.id LIKE 'cp_%'
        AND hc.id NOT IN (SELECT concept_id FROM poetics_text_concept_link)
        ORDER BY COALESCE(hc.era_start, 9999), hc.id
    """)
    rows = cur.fetchall()
    conn.close()
    # Dedup by concept_id (a concept may have multiple quotes)
    seen = set()
    deduped = []
    for r in rows:
        if r[0] not in seen:
            seen.add(r[0])
            deduped.append(r)
    return deduped


def get_text_corpus_for_era_culture(era_min, era_max, culture_hint=None, limit=30):
    """Sample relevant poetics_text entries."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    if culture_hint:
        cur.execute("""SELECT id, title_ja, author_name_display, culture_region, era_year, form_genre
                       FROM poetics_text
                       WHERE COALESCE(era_year, 0) BETWEEN ? AND ?
                       AND culture_region = ?
                       ORDER BY canonical_tier, id LIMIT ?""",
                    (era_min, era_max, culture_hint, limit))
    else:
        cur.execute("""SELECT id, title_ja, author_name_display, culture_region, era_year, form_genre
                       FROM poetics_text
                       WHERE COALESCE(era_year, 0) BETWEEN ? AND ?
                       ORDER BY canonical_tier, id LIMIT ?""",
                    (era_min, era_max, limit))
    rows = cur.fetchall()
    conn.close()
    return rows


def era_to_culture_hint(era_min, era_max, sf):
    """Heuristic: pick a culture hint based on era + subfield."""
    if sf == "比較詩学":
        return None  # cross-cultural
    if era_min < -200:
        return "古代ギリシャ・ローマ"
    if era_min < 500:
        return "古代ギリシャ・ローマ"
    if era_min < 1500:
        return "中世ヨーロッパ"
    return "近代ヨーロッパ"


def make_batches(concepts):
    groups = {}
    for c in concepts:
        cid, name, en, sf, school, era_s, work, author, src_year, src_lang = c
        # Bucket by era
        era = era_s if era_s else (src_year if src_year else 1900)
        if era < -200:
            era_bucket = "ancient"
        elif era < 500:
            era_bucket = "classical"
        elif era < 1500:
            era_bucket = "medieval"
        elif era < 1800:
            era_bucket = "early_modern"
        elif era < 1900:
            era_bucket = "19c"
        elif era < 1950:
            era_bucket = "early_20c"
        else:
            era_bucket = "late_20c"
        key = (sf, era_bucket)
        groups.setdefault(key, []).append((c, era, era_bucket))

    batches = []
    for (sf, era_bucket), items in groups.items():
        for i in range(0, len(items), PER_WORKER):
            chunk = items[i:i + PER_WORKER]
            wid = f"{sf[:6]}_{era_bucket}_{i//PER_WORKER:02d}"
            wid = wid.replace("・", "_").replace("/", "_").replace(" ", "_")
            batches.append((wid, sf, era_bucket, chunk))
    return batches


def build_prompt(wid, sf, era_bucket, chunk):
    # Era ranges for sampling text corpus
    era_ranges = {"ancient": (-2000, -200), "classical": (-200, 500),
                  "medieval": (500, 1500), "early_modern": (1500, 1800),
                  "19c": (1800, 1900), "early_20c": (1900, 1950), "late_20c": (1950, 2030)}
    era_min, era_max = era_ranges.get(era_bucket, (-2000, 2030))
    # widen a bit for relevance
    text_corpus = get_text_corpus_for_era_culture(era_min - 500, era_max + 500, None, 50)

    concept_lines = []
    for (cid, name, en, _sf, school, era_s, work, author, src_year, src_lang), era, _ in chunk:
        line = f"  - {cid}: {name}"
        if en:
            line += f" ({en})"
        line += f" / 引用元: {author or '?'} 『{work or '?'}』"
        if era:
            line += f" / 概念era: {era}"
        concept_lines.append(line)

    text_lines = []
    for tid, ttitle, tauthor, tculture, tyear, tform in text_corpus:
        text_lines.append(f"  - {tid}: 『{ttitle}』 {tauthor or ''} ({tculture}, {tyear or '?'}, {tform or ''})")

    return f"""For these {len(chunk)} poetics concepts (each with founding-source quote), match them to relevant primary poetic texts that exemplify the concept.

SUBFIELD: {sf}
ERA BUCKET: {era_bucket}

CONCEPTS (use these EXACT concept_id strings):
{chr(10).join(concept_lines)}

CANDIDATE TEXTS (use these EXACT text_id strings; you may also reference texts NOT in this list if you are confident a real poetics_text entry exists):
{chr(10).join(text_lines)}

Match each concept to 1-3 relevant texts. Pick texts where:
- The concept's founding source author analyzed/discussed this text (e.g., Aristotle Poetics → Sophocles Oedipus)
- The text exemplifies the concept (e.g., 異化 → Tolstoy War and Peace)
- The text is from a similar tradition/era

OUTPUT (only this JSON, no commentary):
{{"worker_id": "{wid}", "links": [
  {{"concept_id": "<exact_id>",
    "text_id": "<exact_text_id from candidates above, OR a real id you remember>",
    "link_type": "<例証|分析対象|批判対象|影響源|由来>",
    "discussion_locus": "<e.g. 'Aristotle Poetics 11.1452a' or 'Shklovsky 1917 Theory of Prose ch.1'>",
    "strength": <integer 1-10>
  }},
  ... (1-3 per concept)
]}}

Output JSON only.
"""


def main():
    concepts = fetch_quoteless_textlink_concepts()
    print(f"Found {len(concepts)} quoted concepts without text-links")
    batches = make_batches(concepts)
    print(f"Made {len(batches)} batches")

    # Limit to 60 workers
    batches = batches[:60]

    procs = []
    log_files = []
    for wid, sf, era_bucket, chunk in batches:
        out_file = OUTPUT_DIR / f"P12L_{wid}.json"
        log_file = LOG_DIR / f"P12L_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1000:
            print(f"Skip {out_file.name}")
            continue
        prompt = build_prompt(wid, sf, era_bucket, chunk)
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(out_file), prompt]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P12L_{wid} (pid {p.pid}, {len(chunk)} concepts)")

    print(f"\n{len(procs)} workers running")
    for wid, p in procs:
        rc = p.wait()
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
