#!/usr/bin/env python3
"""Step 5: 全分野で 2015-2025 の最新理論を補強。
内部知識のみ使用（web検索無効）の明示。"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "step5_outputs"
LOG_DIR = ROOT / "step5_logs"
OUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TASKS = json.loads((ROOT / "step56_tasks.json").read_text(encoding="utf-8"))["step5_tasks"]
MAX_PARALLEL = 4

PROMPT_TPL = """{table}（{focus}）の重要概念120件を JSON 配列で出力してください。

必須概念: {must_inc}

各エントリの形式:
{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上の定義","impact_summary":"50文字以上の影響","subfield":"分野横断 - 該当サブフィールド名","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"キーワード","keywords_en":"keyword","key_researchers":["名前"],"key_works":["著作 (年)"]}}

要件:
- 主に 2015-2025 年の理論・概念に焦点
- 内部知識のみ使用、web検索しない
- subfield フィールドは {table_subfields} のいずれかを指定
- 重複なし、120件出力
- JSON配列のみ（説明・コードフェンス禁止）
"""

# Map table → list of canonical subfields (from taxonomy_v1)
TAXONOMY = json.loads((ROOT / "step1_taxonomy" / "taxonomy_v1.json").read_text(encoding="utf-8"))


def run_one(task: dict) -> tuple[str, int, int]:
    tid = task["id"]
    out = OUT_DIR / f"{tid}.json"
    log = LOG_DIR / f"{tid}.log"
    if out.exists() and out.stat().st_size > 1000:
        return tid, 0, out.stat().st_size

    must_inc = "、".join(task["must_include"])
    table = task["table"]
    subfields = TAXONOMY["domains"][table]["subfields"]
    prompt = PROMPT_TPL.format(
        table=table,
        focus=task["focus"],
        must_inc=must_inc,
        table_subfields="、".join(subfields),
    )
    print(f"[step5] {tid} ({task['focus']}) start at {time.strftime('%H:%M:%S')}", flush=True)
    try:
        with open(out, "wb") as fout, open(log, "wb") as flog:
            rc = subprocess.run(
                ["codex", "exec", "--full-auto", prompt],
                stdout=fout,
                stderr=flog,
                timeout=600,  # 10 min
            ).returncode
    except subprocess.TimeoutExpired:
        rc = 124
        print(f"[step5] {tid} TIMEOUT", flush=True)
    sz = out.stat().st_size if out.exists() else 0
    print(f"[step5] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[step5] {len(TASKS)} tasks, MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in TASKS}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=900))
            except Exception as e:
                print(f"[step5] task raised: {e}", flush=True)
    print("\n[step5] complete")
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"Success: {success}/{len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
