#!/usr/bin/env python3
"""Phase 11 Step 2: arts 2015+補強 6並列。"""
from __future__ import annotations
import json, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "p11_step2_outputs"
LOG_DIR = ROOT / "p11_step2_logs"
OUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
TASKS = json.loads((ROOT / "p11_step2_tasks.json").read_text(encoding="utf-8"))["tasks"]
MAX_PARALLEL = 6

PROMPT = """「{subfield}」分野の 2015-2025年 の重要概念60件を JSON 配列で出力。

必須概念:
{must_inc}

各エントリ:
{{"name_ja":"日本語","name_en":"English","definition":"100字以上","subfield":"{subfield}","school_of_thought":"学派","era_start":年(2015以上),"era_end":null,"keywords_en":"k1,k2","key_researchers":["名前"]}}

要件: 内部知識のみ、subfield統一、era_start ≥ 2015、60件、JSON配列のみ。"""


def run_one(task):
    tid = task["id"]
    out = OUT_DIR / f"{tid}.json"
    log = LOG_DIR / f"{tid}.log"
    if out.exists() and out.stat().st_size > 1000:
        return tid, 0, out.stat().st_size
    must_inc = "、".join(task["must_include"][:5])
    prompt = PROMPT.format(subfield=task["subfield"], must_inc=must_inc)
    print(f"[p11s2] {tid} start at {time.strftime('%H:%M:%S')}", flush=True)
    try:
        with open(out, "wb") as fout, open(log, "wb") as flog:
            rc = subprocess.run(["codex", "exec", "--full-auto", prompt], stdout=fout, stderr=flog, timeout=300).returncode
    except subprocess.TimeoutExpired:
        rc = 124
    sz = out.stat().st_size if out.exists() else 0
    print(f"[p11s2] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main():
    print(f"[p11s2] {len(TASKS)} tasks", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in TASKS}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=600))
            except Exception as e:
                print(f"raised: {e}", flush=True)
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"\nSuccess: {success}/{len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
