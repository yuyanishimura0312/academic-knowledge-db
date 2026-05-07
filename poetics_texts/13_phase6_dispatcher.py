#!/usr/bin/env python3
"""Phase 6 Codex dispatcher: 40 workers across 28 buckets for 10K texts target.

Improved prompt: less defensive, accept canonical knowledge from PD authors.
Each worker targets 80 canonical texts for its assigned bucket.
"""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT_DIR = Path("/tmp/poetics_texts_p6")
LOG_DIR = Path("/tmp/poetics_texts_p6_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

BUCKETS = json.loads((ROOT / "02_skeleton_buckets.json").read_text())["buckets"]

# Worker allocation (40 total): bigger buckets get multiple workers
WORKER_ALLOCATION = {
    "B01_greek_archaic": 1, "B02_greek_classical_hellenistic": 2,
    "B03_roman_late_republic_augustan": 2, "B04_roman_imperial_late_antique": 1,
    "B05_china_pre_qin": 1, "B06_china_han_six_dynasties": 1,
    "B07_china_tang": 2, "B08_china_song_yuan_ming_qing": 2,
    "B09_japan_ancient": 1, "B10_japan_heian": 1,
    "B11_japan_medieval": 1, "B12_japan_edo": 1, "B13_japan_modern": 1,
    "B14_buddhist_verse": 1, "B15_sanskrit_classical": 2,
    "B16_arabic_classical": 1, "B17_persian_classical": 2,
    "B18_european_medieval": 2, "B19_european_renaissance_baroque": 2,
    "B20_european_18c_neoclassical": 1, "B21_european_romantic": 3,
    "B22_european_19c_late_symbolist": 2, "B23_european_modernist_20c": 2,
    "B24_global_postwar_contemporary": 1, "B25_african_indigenous_oral": 1,
    "B26_indigenous_americas_pacific": 1, "B27_korean_classical_modern": 1,
    "B28_vietnamese_classical": 1,
}

PER_WORKER = 80


def build_prompt(bucket: dict, worker_idx: int, total_workers: int) -> str:
    examples = ", ".join(bucket["examples"][:25])
    diversity = ""
    if total_workers > 1:
        diversity = f"\nThis is worker {worker_idx+1} of {total_workers} for this bucket. Focus on different works than other workers (cover the breadth — different authors, eras, sub-genres)."
    return f"""Output a JSON object with {PER_WORKER} canonical poetic texts from this bucket. Use your knowledge of canonical world poetry — these are well-attested public-domain works.

BUCKET: {bucket['id']}
culture: {bucket['culture_region']}
era: {bucket['era_period']} ({bucket['era_year_range']})
languages: {bucket['languages']}
canonical examples: {examples}{diversity}

OUTPUT FORMAT (output ONLY the JSON, no commentary):
{{"bucket_id": "{bucket['id']}", "worker": {worker_idx+1}, "texts": [
  {{"id": "pt_text_<snake_case_unique>",
    "title_original": "<original-script title>",
    "title_ja": "<Japanese title>",
    "title_en": "<English title>",
    "author_name_display": "<author>",
    "era_year": <integer year, BCE negative>,
    "era_period": "<period>",
    "culture_region": "{bucket['culture_region']}",
    "language_original": "<ISO 639-3>",
    "form_genre": "<form>",
    "meter_prosody": "<meter if known>",
    "length_lines": <integer>,
    "full_text_or_excerpt": "<2-8 lines of the actual canonical opening or famous passage in original script>",
    "excerpt_note": "<which part>",
    "public_domain_status": "PD-original",
    "source_url": "<wikisource/perseus/gutenberg/gretil/ganjoor/CBETA/aozora/wikisource各言語 URL>",
    "source_archive": "<archive name>",
    "canonical_tier": <1, 2, or 3>
  }},
  ... ({PER_WORKER} entries total)
]}}

REQUIREMENTS:
- All authors PD (died before 1929 or pre-modern)
- Use original-script characters for non-Latin (中文/日文/サンスクリット/アラビア/ペルシア/ギリシア)
- Keep excerpts to 2-8 lines (canonical opening or famous passage)
- Diverse coverage: not just the same 5 most famous authors — include the broader canon
- Output the JSON object only, no other text.
"""


def main():
    procs = []
    log_files = []
    for bucket_id, n_workers in WORKER_ALLOCATION.items():
        bucket = next(b for b in BUCKETS if b["id"] == bucket_id)
        for w in range(n_workers):
            out_file = OUTPUT_DIR / f"{bucket_id}_w{w+1}.json"
            log_file = LOG_DIR / f"{bucket_id}_w{w+1}.log"
            if out_file.exists() and out_file.stat().st_size > 1000:
                print(f"Skip {out_file.name}")
                continue
            prompt = build_prompt(bucket, w, n_workers)
            cmd = [
                "codex", "exec",
                "--skip-git-repo-check",
                "--sandbox", "read-only",
                "--output-last-message", str(out_file),
                prompt,
            ]
            log = open(log_file, "w")
            p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
            procs.append((out_file.name, p))
            log_files.append(log)
            print(f"Launched {out_file.name} (pid {p.pid})")

    print(f"\n{len(procs)} workers running...")
    for name, p in procs:
        rc = p.wait()
        print(f"  {name}: exit {rc}")
    for lf in log_files:
        lf.close()

    print("\n=== Results ===")
    total_texts = 0
    for f in sorted(OUTPUT_DIR.glob("*.json")):
        try:
            d = json.loads(f.read_text())
            n = len(d.get("texts", []))
            total_texts += n
            print(f"  {f.name}: {n} texts")
        except Exception as e:
            print(f"  {f.name}: ERROR {e}")
    print(f"\nTotal: {total_texts} texts")


if __name__ == "__main__":
    main()
