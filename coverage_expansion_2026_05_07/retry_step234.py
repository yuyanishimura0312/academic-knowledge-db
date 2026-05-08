#!/usr/bin/env python3
"""Retry the 11 failed step234 tasks with simpler prompts (no web search emphasis)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "step234_outputs"
LOG_DIR = ROOT / "step234_logs"
TASKS = json.loads((ROOT / "step234_tasks.json").read_text(encoding="utf-8"))["tasks"]
TASK_BY_ID = {t["id"]: t for t in TASKS}

FAILED = [
    "E3_telecom", "E3_civil", "S2_geography", "A3_literary",
    "H4_religion", "S2_law", "H4_aesthetics", "S2_politics",
    "H4_linguistics", "H4_history", "A3_music",
]
MAX_PARALLEL = 4  # smaller batches, less contention


def run_one(tid: str) -> tuple[str, int, int]:
    task = TASK_BY_ID[tid]
    out = OUT_DIR / f"{tid}.json"
    log = LOG_DIR / f"{tid}.retry.log"
    must_inc = "、".join(task["must_include"][:5])
    # Simpler prompt — no emphasis on web search
    prompt = f"""「{task['subfield']}」分野の重要概念100件を JSON 配列で出力してください。

必須概念: {must_inc}

形式:
[{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上の定義","impact_summary":"50文字以上の影響","subfield":"{task['subfield']}","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"キーワード","keywords_en":"keyword","key_researchers":["名前"],"key_works":["著作 (年)"]}}]

要件: 内部知識のみ使用（web検索不要）。subfield は必ず「{task['subfield']}」。100件出力。説明文・コードフェンス禁止。JSON配列のみ。"""

    print(f"[retry] {tid} start at {time.strftime('%H:%M:%S')}", flush=True)
    with open(out, "wb") as fout, open(log, "wb") as flog:
        rc = subprocess.run(
            ["codex", "exec", "--full-auto", prompt],
            stdout=fout,
            stderr=flog,
            timeout=900,  # 15 min hard timeout
        ).returncode if True else 1
    sz = out.stat().st_size
    print(f"[retry] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[retry] {len(FAILED)} tasks, MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in FAILED}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=1200))
            except Exception as e:
                print(f"[retry] {futures[fut]} raised: {e}", flush=True)
    print("\n[retry] complete")
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"Success: {success}/{len(FAILED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
