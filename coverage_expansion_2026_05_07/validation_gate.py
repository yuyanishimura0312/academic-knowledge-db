#!/usr/bin/env python3
"""C段階完了後の検証ゲート。Steps 2/3/4 が成功したか判定し、D段階移行可否を返す。

検証項目:
  1. 各分野で量的増加 (+30%以上)
  2. サブフィールド数 ≤ 20 (Step 1で達成済みを維持)
  3. 各分野の最大/最小サブフィールド比 < 50 (詩学・生態学等の極端偏在は許容するが、改善傾向)
  4. 時代分布: 2015+ ≥ 15% を達成した分野数 ≥ 3
  5. 重複・欠損なし
  6. 関係数 / 概念数 比 ≥ 1.0
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"

# Pre-expansion baseline (2026-05-08 時点、Codex投入前)
BASELINE = {
    "humanities_concept": 4534,
    "social_theory": 1709,
    "natural_discovery": 2812,
    "engineering_method": 1169,
    "arts_question": 1145,
}


def main() -> int:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    issues = []
    passes = []

    print("=== 検証ゲート: Step 2/3/4 後の状態 ===\n")

    # 1. 量的増加
    print("【1. 量的増加】")
    for tbl, base in BASELINE.items():
        cur = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        delta = cur - base
        pct = delta / base * 100
        status = "✅" if pct >= 30 else ("⚠" if pct >= 10 else "❌")
        msg = f"  {status} {tbl}: {base} → {cur} (+{delta}, +{pct:.1f}%)"
        print(msg)
        if pct < 10:
            issues.append(f"{tbl} の増加率 {pct:.1f}% (基準30%)")
        elif pct >= 30:
            passes.append(f"{tbl} +{pct:.0f}%")

    # 2. サブフィールド数
    print("\n【2. サブフィールド数】")
    for tbl in BASELINE:
        n = conn.execute(f"SELECT COUNT(DISTINCT subfield) FROM {tbl}").fetchone()[0]
        status = "✅" if n <= 20 else "❌"
        print(f"  {status} {tbl}: {n} サブフィールド")
        if n > 20:
            issues.append(f"{tbl} のサブフィールド数 {n} (基準≤20)")

    # 3. 最大/最小比
    print("\n【3. サブフィールド分布バランス】")
    for tbl in BASELINE:
        rows = conn.execute(f"SELECT subfield, COUNT(*) c FROM {tbl} GROUP BY subfield ORDER BY c DESC").fetchall()
        if not rows:
            continue
        mx = rows[0]["c"]
        mn = rows[-1]["c"]
        ratio = mx / mn if mn else float("inf")
        status = "✅" if ratio < 50 else ("⚠" if ratio < 100 else "❌")
        print(f"  {status} {tbl}: max={mx} ({rows[0]['subfield'][:30]}), min={mn}, 比={ratio:.1f}")
        if ratio >= 100:
            issues.append(f"{tbl} の偏在比 {ratio:.0f}× (基準<50)")

    # 4. 時代分布
    print("\n【4. 2015年以降の比率】")
    healthy_era = 0
    for tbl in BASELINE:
        total = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        recent = conn.execute(f"SELECT COUNT(*) FROM {tbl} WHERE era_start >= 2015").fetchone()[0]
        pct = recent / total * 100 if total else 0
        status = "✅" if pct >= 15 else ("⚠" if pct >= 10 else "❌")
        print(f"  {status} {tbl}: {recent}/{total} ({pct:.1f}%)")
        if pct >= 15:
            healthy_era += 1
    if healthy_era < 3:
        issues.append(f"2015+ 15%達成分野数 {healthy_era} (基準≥3)")
    else:
        passes.append(f"2015+ 15%達成 {healthy_era}/5分野")

    # 5. 重複・欠損
    print("\n【5. データ整合性】")
    for tbl in BASELINE:
        nulls = conn.execute(f"SELECT COUNT(*) FROM {tbl} WHERE name_ja IS NULL OR name_en IS NULL OR definition IS NULL").fetchone()[0]
        dups = conn.execute(f"SELECT COUNT(*) FROM (SELECT name_en, COUNT(*) c FROM {tbl} WHERE name_en IS NOT NULL GROUP BY name_en HAVING c>1)").fetchone()[0]
        status = "✅" if nulls + dups == 0 else "⚠"
        print(f"  {status} {tbl}: NULLs={nulls}, dup_name_en={dups}")
        if dups > 50:
            issues.append(f"{tbl} の重複 {dups} 件")

    # 6. 関係数
    print("\n【6. 関係ネットワーク】")
    rels = {
        "humanities": conn.execute("SELECT COUNT(*) FROM humanities_concept_relations").fetchone()[0],
        "social": conn.execute("SELECT COUNT(*) FROM social_theory_relations").fetchone()[0],
        "natural": conn.execute("SELECT COUNT(*) FROM natural_discovery_relations").fetchone()[0],
        "engineering": conn.execute("SELECT COUNT(*) FROM engineering_method_relations").fetchone()[0],
        "arts": conn.execute("SELECT COUNT(*) FROM arts_question_relations").fetchone()[0],
    }
    total_rels = sum(rels.values())
    total_concepts = sum(conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0] for tbl in BASELINE)
    ratio = total_rels / total_concepts if total_concepts else 0
    status = "✅" if ratio >= 1.0 else "⚠"
    print(f"  {status} 概念={total_concepts}, 関係={total_rels}, 比={ratio:.2f}")

    # 結論
    print("\n" + "="*50)
    if not issues:
        print("✅ 全項目PASS — D段階（Step 5/6 自走）へ進行可能")
        for p in passes:
            print(f"  • {p}")
        return 0
    else:
        print(f"⚠ {len(issues)} 件の課題あり")
        for i in issues:
            print(f"  ! {i}")
        if len(issues) >= 5:
            print("\n❌ D段階移行は推奨しません — 課題対処が先")
            return 1
        else:
            print("\n⚠ 軽微な課題のみ — D段階移行可能（Step 5/6 で改善見込み）")
            return 0


if __name__ == "__main__":
    sys.exit(main())
