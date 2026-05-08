#!/usr/bin/env python3
"""Tasks 2+3 を13並列実行: natural_discovery 拡張 + 全分野 2015+ 補強。"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "task23_outputs"
LOG_DIR = ROOT / "task23_logs"
OUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TASKS = json.loads((ROOT / "task23_specs.json").read_text(encoding="utf-8"))["tasks"]
TAXONOMY = json.loads((ROOT / "step1_taxonomy" / "taxonomy_v1.json").read_text(encoding="utf-8"))
MAX_PARALLEL = 6

PROMPT_T2 = """「{subfield}」分野の重要概念{target}件を JSON 配列で出力してください。

必須概念（10件）:
{must_inc}

形式:
[{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上の定義","impact_summary":"50文字以上","subfield":"{subfield}","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"カンマ区切り","keywords_en":"k1,k2","key_researchers":["名前"],"key_works":["著作 (年)"]}}]

要件:
- 内部知識のみ（web検索不要）
- subfield フィールドは必ず「{subfield}」
- 創設期から最新2025年まで時代分布均等
- 重複なし、{target}件出力
- JSON配列のみ（コードフェンス・説明文禁止）"""

PROMPT_T3 = """{table_label}（{focus}）の重要概念{target}件を JSON 配列で出力。

必須概念:
{must_inc}

形式:
[{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上","impact_summary":"50文字以上","subfield":"{subfield_list の中から1つ}","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"k","keywords_en":"k","key_researchers":["名前"],"key_works":["著作 (年)"]}}]

要件:
- 内部知識のみ使用、web検索しない
- 主に 2015-2025 年の理論
- subfield は次のいずれか: {subfield_list}
- 重複なし、{target}件、JSON配列のみ出力"""

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
    log = LOG_DIR / f"{tid}.log"
    if out.exists() and out.stat().st_size > 1000:
        return tid, 0, out.stat().st_size

    must_inc = "、".join(task["must_include"])

    if task.get("subfield_distribute"):
        # T3: subfield is distributed
        subfields = TAXONOMY["domains"][task["table"]]["subfields"]
        prompt = PROMPT_T3.format(
            table_label=DOMAIN_LABELS[task["table"]],
            focus=task["focus"],
            target=task["target"],
            must_inc=must_inc,
            subfield_list="、".join(subfields),
        )
    else:
        # T2: single subfield
        prompt = PROMPT_T2.format(
            subfield=task["subfield"],
            target=task["target"],
            must_inc=must_inc,
        )

    print(f"[t23] {tid} ({task.get('subfield', task.get('focus'))}, target={task['target']}) start at {time.strftime('%H:%M:%S')}", flush=True)
    try:
        with open(out, "wb") as fout, open(log, "wb") as flog:
            rc = subprocess.run(
                ["codex", "exec", "--full-auto", prompt],
                stdout=fout,
                stderr=flog,
                timeout=900,
            ).returncode
    except subprocess.TimeoutExpired:
        rc = 124
        print(f"[t23] {tid} TIMEOUT", flush=True)
    sz = out.stat().st_size if out.exists() else 0
    print(f"[t23] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[t23] {len(TASKS)} tasks, MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in TASKS}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=1200))
            except Exception as e:
                print(f"[t23] task raised: {e}", flush=True)
    print("\n[t23] complete")
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"Success: {success}/{len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
