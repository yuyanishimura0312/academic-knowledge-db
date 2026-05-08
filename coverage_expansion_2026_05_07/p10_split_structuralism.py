#!/usr/bin/env python3
"""Phase 10: arts/構造主義・記号論 (619) を era×keyword で細分化。

新サブフィールド:
  - 言語構造主義 (era 1900-1949, 言語/ソシュール/形式主義)
  - 文化構造主義 (era 1950-1969, レヴィ=ストロース/神話/親族)
  - 記号論・テクスト分析 (era 1960-1979, バルト/ロラン/シニフィエ)
  - 物語論的構造主義 (era 1965+, ジュネット/プロップ/グレマス)
"""
from __future__ import annotations
import argparse, sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = list(conn.execute("SELECT id, era_start, name_ja, name_en, keywords_ja, keywords_en FROM arts_question WHERE subfield = '構造主義・記号論'"))
    print(f"Source: {len(rows)} entries")

    keyword_rules = [
        (["記号", "semiotic", "semiology", "sign", "code"], "記号論・テクスト分析"),
        (["narrative", "narratology", "物語", "ジュネット", "プロップ", "グレマス"], "物語論的構造主義"),
        (["神話", "myth", "レヴィ=ストロース", "levi-strauss", "親族", "kinship"], "文化構造主義"),
        (["言語", "linguistic", "ソシュール", "saussure", "形式主義", "formalism", "シニフィエ", "シニフィアン"], "言語構造主義"),
    ]

    bucket = {}
    updates = []
    for r in rows:
        haystack = " ".join(filter(None, [r["name_ja"], r["name_en"], r["keywords_ja"], r["keywords_en"]])).lower()
        matched = False
        for keywords, name in keyword_rules:
            if any(kw.lower() in haystack for kw in keywords):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                matched = True
                break
        if not matched:
            era = r["era_start"] or 0
            if era < 1950:
                name = "言語構造主義"
            elif era < 1970:
                name = "文化構造主義"
            else:
                name = "物語論的構造主義"
            bucket[name] = bucket.get(name, 0) + 1
            updates.append((name, r["id"]))

    print("\n=== 分割結果 ===")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")

    if args.commit and updates:
        conn.executemany("UPDATE arts_question SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)
        conn.commit()
        print(f"\nCOMMITTED: {len(updates)} updates")
    else:
        print("\nDRY-RUN")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
