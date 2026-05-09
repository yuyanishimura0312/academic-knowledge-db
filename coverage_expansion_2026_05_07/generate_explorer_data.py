#!/usr/bin/env python3
"""探索ダッシュボード用データ生成。

ai_explorer.json: 全18,090概念を domain/subfield別にネストして書き出し。
"""
from __future__ import annotations
import json
import sqlite3
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DB = REPO_ROOT / "academic.db"

DOMAIN_LABELS = {
    "humanities_concept": "人文学",
    "social_theory": "社会科学",
    "natural_discovery": "自然科学",
    "engineering_method": "工学",
    "arts_question": "芸術・デザイン",
}


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    out = {"version": "1.9.1", "domains": {}}

    for tbl, label in DOMAIN_LABELS.items():
        rows = conn.execute(f"""
            SELECT name_ja, name_en, definition, impact_summary, subfield,
                   school_of_thought, era_start, era_end, keywords_ja, keywords_en
            FROM {tbl}
            WHERE name_ja IS NOT NULL AND TRIM(name_ja) != ''
            ORDER BY subfield, era_start
        """).fetchall()
        sub_map = defaultdict(list)
        for r in rows:
            sub_map[r["subfield"] or "未分類"].append({
                "name_ja": r["name_ja"],
                "name_en": r["name_en"],
                "definition": (r["definition"] or "")[:400],
                "impact": (r["impact_summary"] or "")[:200],
                "school": r["school_of_thought"] or "",
                "era": r["era_start"],
                "era_end": r["era_end"],
                "kw_ja": r["keywords_ja"] or "",
                "kw_en": r["keywords_en"] or "",
            })
        # Sort subfields by count desc
        sorted_subs = sorted(sub_map.items(), key=lambda x: -len(x[1]))
        out["domains"][tbl] = {
            "label": label,
            "total": len(rows),
            "subfields": [{"name": s, "count": len(c), "concepts": c} for s, c in sorted_subs],
        }
        print(f"{tbl}: {len(rows)} concepts in {len(sub_map)} subfields")

    out_path = REPO_ROOT / "explorer_data.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out_path} ({out_path.stat().st_size:,} bytes)")
    conn.close()


if __name__ == "__main__":
    main()
