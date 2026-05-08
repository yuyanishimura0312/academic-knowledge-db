#!/usr/bin/env python3
"""Step 2: arts_question/文学理論・物語論 (2,862件) を era_start ベースで5サブフィールドに分割。

新サブフィールド:
  - 古典詩学 (Pre-1900)
  - 近代詩学・批評理論 (1900-1959)
  - 構造主義・記号論 (1960-1989)
  - ポスト構造主義詩学 (1990-2014)
  - 現代文学理論 (2015+)

全て arts_question テーブル内、subfield フィールドのみ更新。
"""
from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"

RULES = [
    (lambda y: y < 1900, "古典詩学"),
    (lambda y: 1900 <= y < 1960, "近代詩学・批評理論"),
    (lambda y: 1960 <= y < 1990, "構造主義・記号論"),
    (lambda y: 1990 <= y < 2015, "ポスト構造主義詩学"),
    (lambda y: y >= 2015, "現代文学理論"),
]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = list(conn.execute("SELECT id, era_start FROM arts_question WHERE subfield = '文学理論・物語論'").fetchall())
    print(f"Source: {len(rows)} entries")

    bucket = {}
    updates = []
    for r in rows:
        era = r["era_start"] or 0
        for fn, name in RULES:
            if fn(era):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                break
        else:
            bucket["未分類"] = bucket.get("未分類", 0) + 1

    print("\n=== 分割結果 ===")
    for name, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {name}: {c}")

    if args.commit:
        conn.executemany("UPDATE arts_question SET subfield = ?, updated_at = datetime('now') WHERE id = ?", updates)
        conn.commit()
        print(f"\nCOMMITTED: {len(updates)} updates")
    else:
        print("\nDRY-RUN. Use --commit to apply.")

    # Update taxonomy_v1.json reference (manual reminder)
    print("\n注: taxonomy_v1.json の arts_question サブフィールドリストに5新カテゴリを追加が必要")

    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
