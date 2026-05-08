#!/usr/bin/env python3
"""Phase 8 v2: Target 60件/タスクに縮小、シンプルプロンプトで安定動作。"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "phase8_outputs"
LOG_DIR = ROOT / "phase8_logs"
OUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TASKS = json.loads((ROOT / "phase8_tasks.json").read_text(encoding="utf-8"))["tasks"]
TAXONOMY = json.loads((ROOT / "step1_taxonomy" / "taxonomy_v1.json").read_text(encoding="utf-8"))
MAX_PARALLEL = 6
TARGET_OVERRIDE = 60  # All tasks → 60 entries to fit codex window

PROMPT_FIXED = """「{subfield}」分野の重要概念{target}件を JSON 配列で出力。

必須概念5件:
{must_inc}

各エントリ:
{{"name_ja":"日本語","name_en":"English","definition":"100字以上","subfield":"{subfield}","school_of_thought":"学派","era_start":年,"era_end":null,"keywords_en":"k1,k2","key_researchers":["名前"]}}

要件: 内部知識のみ、subfield統一、{target}件、JSON配列のみ（説明なし）。"""

PROMPT_DISTRIB = """{table_label}（{focus}）の概念{target}件を JSON 配列で出力。

必須5件:
{must_inc}

各エントリ:
{{"name_ja":"日本語","name_en":"English","definition":"100字以上","subfield":"<下記から1つ>","school_of_thought":"学派","era_start":年,"era_end":null,"keywords_en":"k1,k2","key_researchers":["名前"]}}

subfield候補: {subfield_list}

要件: 主に2015-2025年、内部知識のみ、{target}件、JSON配列のみ。"""

DOMAIN_LABELS = {
    "humanities_concept": "人文学",
    "social_theory": "社会科学",
    "natural_discovery": "自然科学",
    "engineering_method": "工学",
    "arts_question": "芸術",
}


def run_one(task: dict) -> tuple[str, int, int]:
    tid = task["id"]
    out = OUT_DIR / f"{tid}.json"
    log = LOG_DIR / f"{tid}.v2.log"
    if out.exists() and out.stat().st_size > 1000:
        return tid, 0, out.stat().st_size

    must_inc = "、".join(task["must_include"][:5])

    if task.get("subfield_distribute"):
        subfields = TAXONOMY["domains"][task["table"]]["subfields"]
        prompt = PROMPT_DISTRIB.format(
            table_label=DOMAIN_LABELS[task["table"]],
            focus=task["focus"],
            target=TARGET_OVERRIDE,
            must_inc=must_inc,
            subfield_list="、".join(subfields[:8]),  # cap to 8 subfields
        )
    else:
        prompt = PROMPT_FIXED.format(
            subfield=task["subfield"],
            target=TARGET_OVERRIDE,
            must_inc=must_inc,
        )

    print(f"[p8v2] {tid} ({task.get('subfield', task.get('focus', '?'))[:30]}) start at {time.strftime('%H:%M:%S')}", flush=True)
    try:
        with open(out, "wb") as fout, open(log, "wb") as flog:
            rc = subprocess.run(
                ["codex", "exec", "--full-auto", prompt],
                stdout=fout,
                stderr=flog,
                timeout=300,  # 5 min per task
            ).returncode
    except subprocess.TimeoutExpired:
        rc = 124
        print(f"[p8v2] {tid} TIMEOUT", flush=True)
    sz = out.stat().st_size if out.exists() else 0
    print(f"[p8v2] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[p8v2] {len(TASKS)} tasks (target={TARGET_OVERRIDE} each), MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in TASKS}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=600))
            except Exception as e:
                print(f"[p8v2] task raised: {e}", flush=True)
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"\nSuccess: {success}/{len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
