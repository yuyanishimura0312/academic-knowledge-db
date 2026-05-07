#!/usr/bin/env python3
"""Step 2/3/4 並列ランチャー — 42 Codex タスクを最大8並列で実行。"""
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
OUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TASKS = json.loads((ROOT / "step234_tasks.json").read_text(encoding="utf-8"))["tasks"]
MAX_PARALLEL = int(os.environ.get("MAX_PARALLEL", "8"))

PROMPT_TEMPLATE = """あなたは学術概念の専門エージェントです。「{subfield}」分野について、{target}件の重要な理論・概念・モデル・運動を JSON 配列で出力してください。

以下の必須概念を必ず含めてください：
{must_include}

各エントリは以下の形式：
{{
  "name_ja": "日本語名",
  "name_en": "English Name",
  "definition": "100文字以上の定義",
  "impact_summary": "50文字以上の影響まとめ",
  "subfield": "{subfield}",
  "school_of_thought": "学派・流派",
  "era_start": 整数年,
  "era_end": 整数年または null,
  "keywords_ja": "カンマ区切り",
  "keywords_en": "keyword1,keyword2",
  "key_researchers": ["主要研究者"],
  "key_works": ["主要著作 (年)"]
}}

重要要件:
- subfield フィールドは必ず「{subfield}」に統一する（変更不可）
- 創設期から最新2025年まで時代分布を均等に（特に2015-2025の最新理論を30%以上）
- 確実に存在する概念のみ。重複なし
- JSON配列のみ出力（コードフェンス・説明文不要）
- {target}件全て出力するまで止めない"""


def run_task(task: dict) -> tuple[str, int, int]:
    tid = task["id"]
    out = OUT_DIR / f"{tid}.json"
    log = LOG_DIR / f"{tid}.log"
    if out.exists() and out.stat().st_size > 100:
        return tid, 0, out.stat().st_size

    must_inc = "\n".join(f"- {m}" for m in task["must_include"])
    prompt = PROMPT_TEMPLATE.format(
        subfield=task["subfield"],
        target=task["target"],
        must_include=must_inc,
    )
    print(f"[start] {tid} ({task['subfield']}, target={task['target']}) at {time.strftime('%H:%M:%S')}", flush=True)
    with open(out, "wb") as fout, open(log, "wb") as flog:
        rc = subprocess.run(
            ["codex", "exec", "--full-auto", prompt],
            stdout=fout,
            stderr=flog,
        ).returncode
    sz = out.stat().st_size
    print(f"[done]  {tid} rc={rc} bytes={sz}", flush=True)
    return tid, rc, sz


def main() -> int:
    print(f"[launch] {len(TASKS)} tasks, MAX_PARALLEL={MAX_PARALLEL}", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as ex:
        futures = [ex.submit(run_task, t) for t in TASKS]
        for fut in as_completed(futures):
            results.append(fut.result())
    print("\n[launch] complete")
    print("\n=== Sizes ===")
    for tid, rc, sz in sorted(results, key=lambda x: x[2]):
        print(f"  {tid}: rc={rc} bytes={sz}")
    success = sum(1 for _, _, sz in results if sz > 1000)
    print(f"\nSuccess: {success}/{len(results)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
