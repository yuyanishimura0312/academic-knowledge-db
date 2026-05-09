#!/usr/bin/env python3
"""Phase 11 Step 1: 民族誌方法論 (449) を keyword で細分化。

Target subfields:
  - 医療・身体人類学
  - 環境・気候人類学
  - 都市・デジタル人類学
  - ポストコロニアル・批判人類学
  - 民族誌方法論 (純粋方法論のみ)
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
    rows = list(conn.execute("SELECT id, name_ja, name_en, keywords_ja, keywords_en, definition FROM humanities_concept WHERE subfield = '民族誌方法論'"))
    print(f"Source: {len(rows)} entries")

    keyword_rules = [
        (["医療", "medical", "苦悩", "suffering", "ヘルス", "health", "身体", "body", "看護", "ケア", "病い", "illness", "治癒", "biomedical"], "医療・身体人類学"),
        (["環境", "environment", "気候", "climate", "ecology", "生態", "anthropocene", "人新世", "土地", "land", "野生", "wilderness"], "環境・気候人類学"),
        (["都市", "urban", "city", "メトロ", "ゲーテッド", "デジタル", "digital", "プラットフォーム", "インフラ", "インターネット", "infrastructure", "サイバー", "ai"], "都市・デジタル人類学"),
        (["ポストコロニアル", "postcolonial", "脱植民地", "decolon", "サバルタン", "subaltern", "ファノン", "fanon", "race", "人種", "ジェンダー", "gender", "feminism", "queer", "クィア", "subaltern", "周縁", "marginal"], "ポストコロニアル・批判人類学"),
        (["象徴", "symbolic", "ritual", "儀礼", "myth", "神話", "宗教", "religion"], "象徴・解釈人類学"),
    ]

    bucket = {}
    updates = []
    for r in rows:
        haystack = " ".join(filter(None, [r["name_ja"], r["name_en"], r["keywords_ja"], r["keywords_en"], (r["definition"] or "")[:200]])).lower()
        matched = False
        for keywords, name in keyword_rules:
            if any(kw.lower() in haystack for kw in keywords):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                matched = True
                break
        if not matched:
            # Keep as 民族誌方法論 if truly methodological/general
            bucket["民族誌方法論"] = bucket.get("民族誌方法論", 0) + 1
            updates.append(("民族誌方法論", r["id"]))

    print("\n=== 分割結果 ===")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")

    if args.commit and updates:
        conn.executemany("UPDATE humanities_concept SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)
        conn.commit()
        print(f"\nCOMMITTED: {len(updates)} updates")
    else:
        print("\nDRY-RUN")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
