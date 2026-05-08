#!/usr/bin/env python3
"""Phase 8 第1波: 29 Codex並列タスク (Steps 1+3+4)。
Codex 復旧後の効率実行。MAX_PARALLEL=8 (Codex は安定動作を確認済み)。"""
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
MAX_PARALLEL = 8

PROMPT_FIXED = """「{subfield}」分野の重要概念{target}件を JSON 配列で出力してください。

必須概念（10件）：
{must_inc}

各エントリ形式：
{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上の定義","impact_summary":"50文字以上","subfield":"{subfield}","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"k1,k2,k3","keywords_en":"k1,k2,k3","key_researchers":["名前"],"key_works":["著作 (年)"]}}

要件:
- 内部知識のみ（web検索不要、外部参照しない）
- subfield フィールドは必ず「{subfield}」に統一
- 創設期から最新2025年まで時代分布均等（特に2015-2025を25%以上）
- 重複なし、{target}件出力
- JSON配列のみ（コードフェンス・説明文禁止）"""

PROMPT_DISTRIB = """{table_label}（{focus}）の重要概念{target}件を JSON 配列で出力。

必須概念：
{must_inc}

各エントリ形式：
{{"name_ja":"日本語名","name_en":"English Name","definition":"100文字以上","impact_summary":"50文字以上","subfield":"<下記から1つ>","school_of_thought":"学派","era_start":整数年,"era_end":null,"keywords_ja":"k","keywords_en":"k","key_researchers":["名前"],"key_works":["著作 (年)"]}}

要件:
- 内部知識のみ使用、web検索しない
- 主に 2015-2025 年の理論
- subfield は次のいずれか: {subfield_list}
- 重複なし、{target}件出力、JSON配列のみ"""

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
        subfields = TAXONOMY["domains"][task["table"]]["subfields"]
        prompt = PROMPT_DISTRIB.format(
            table_label=DOMAIN_LABELS[task["table"]],
            focus=task["focus"],
            target=task["target"],
            must_inc=must_inc,
            subfield_list="、".join(subfields),
        )
    else:
        prompt = PROMPT_FIXED.format(
            subfield=task["subfield"],
            target=task["target"],
            must_inc=must_inc,
        )

    print(f"[p8] {tid} ({task.get('subfield', task.get('focus', '?'))[:30]}, target={task['target']}) start at {time.strftime('%H:%M:%S')}", flush=True)
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
        print(f"[p8] {tid} TIMEOUT", flush=True)
    sz = out.stat().st_size if out.exists() else 0
    print(f"[p8] {tid} done rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[p8] {len(TASKS)} tasks, MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = {ex.submit(run_one, t): t for t in TASKS}
        for fut in as_completed(futures):
            try:
                results.append(fut.result(timeout=1200))
            except Exception as e:
                print(f"[p8] task raised: {e}", flush=True)
    print("\n[p8] complete")
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"Success: {success}/{len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
