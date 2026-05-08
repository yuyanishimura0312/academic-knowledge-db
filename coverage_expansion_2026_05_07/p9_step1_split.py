#!/usr/bin/env python3
"""Phase 9 Step 1: 4 大規模サブフィールドを era_start ベースで細分化。

対象:
  1. arts/古典詩学 (1,310) → 5サブ (古代/中世/ルネサンス/近世/19世紀)
  2. natural/生態学 (1,049) → 5サブ (個体群/群集/進化/生態系/応用)  ← keyword基準
  3. humanities/文化人類学・民族誌 (714) → 5サブ (古典/象徴解釈/政治経済/存在論/方法論)
  4. social/心理学 (681) → 5サブ (認知/社会/発達/臨床/人格)

natural と humanities は keywords に基づくルール分類。
"""
from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"


def split_classical_poetics(conn, commit: bool):
    """arts/古典詩学 → 5サブ (era 基準)"""
    rules = [
        (lambda y: y < 500, "古代詩学"),
        (lambda y: 500 <= y < 1400, "中世詩学"),
        (lambda y: 1400 <= y < 1700, "ルネサンス詩学"),
        (lambda y: 1700 <= y < 1850, "近世詩学"),
        (lambda y: y >= 1850, "19世紀古典詩学"),
    ]
    rows = list(conn.execute("SELECT id, era_start FROM arts_question WHERE subfield = '古典詩学'"))
    bucket = {}
    updates = []
    for r in rows:
        era = r["era_start"] or 0
        for fn, name in rules:
            if fn(era):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                break
    print(f"\n[1.1 古典詩学 → 5分割] source={len(rows)}")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")
    if commit and updates:
        conn.executemany("UPDATE arts_question SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)


def split_ecology(conn, commit: bool):
    """natural/生態学 → 5サブ (keyword 基準)"""
    rules = [
        (["個体群", "population", "metapopulation"], "個体群生態学"),
        (["群集", "community", "competition", "coexistence"], "群集生態学"),
        (["進化生態", "evolutionary ecology", "adaptation", "selection"], "進化生態学"),
        (["生態系", "ecosystem", "biogeochemistry", "nutrient"], "生態系生態学"),
        (["保全", "conservation", "biodiversity", "応用", "applied"], "応用・保全生態学"),
    ]
    rows = list(conn.execute("SELECT id, name_ja, name_en, keywords_ja, keywords_en FROM natural_discovery WHERE subfield = '生態学'"))
    bucket = {}
    updates = []
    for r in rows:
        haystack = " ".join(filter(None, [r["name_ja"], r["name_en"], r["keywords_ja"], r["keywords_en"]])).lower()
        matched = False
        for keywords, name in rules:
            if any(kw.lower() in haystack for kw in keywords):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                matched = True
                break
        if not matched:
            bucket["理論生態学"] = bucket.get("理論生態学", 0) + 1
            updates.append(("理論生態学", r["id"]))
    print(f"\n[1.2 生態学 → 5分割] source={len(rows)}")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")
    if commit and updates:
        conn.executemany("UPDATE natural_discovery SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)


def split_anthropology(conn, commit: bool):
    """humanities/文化人類学・民族誌 → 5サブ"""
    rules_kw = [
        (["象徴", "解釈", "symbolic", "interpretive", "geertz", "thick description", "ritual"], "象徴・解釈人類学"),
        (["政治", "経済", "political", "economic", "marxist", "subaltern"], "政治・経済人類学"),
        (["存在論", "ontology", "ontological", "multispecies", "posthuman", "新唯物論", "anthropocene"], "存在論的転回・現代人類学"),
        (["方法", "method", "ethnography", "fieldwork", "民族誌", "auto-ethnography", "digital ethnography"], "民族誌方法論"),
    ]
    rows = list(conn.execute("SELECT id, era_start, name_ja, name_en, keywords_ja, keywords_en FROM humanities_concept WHERE subfield = '文化人類学・民族誌'"))
    bucket = {}
    updates = []
    for r in rows:
        haystack = " ".join(filter(None, [r["name_ja"], r["name_en"], r["keywords_ja"], r["keywords_en"]])).lower()
        matched = False
        for keywords, name in rules_kw:
            if any(kw.lower() in haystack for kw in keywords):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                matched = True
                break
        if not matched:
            era = r["era_start"] or 0
            if era < 1960:
                bucket["古典文化人類学"] = bucket.get("古典文化人類学", 0) + 1
                updates.append(("古典文化人類学", r["id"]))
            else:
                bucket["民族誌方法論"] = bucket.get("民族誌方法論", 0) + 1
                updates.append(("民族誌方法論", r["id"]))
    print(f"\n[1.3 文化人類学・民族誌 → 5分割] source={len(rows)}")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")
    if commit and updates:
        conn.executemany("UPDATE humanities_concept SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)


def split_psychology(conn, commit: bool):
    """social/心理学 → 5サブ"""
    rules_kw = [
        (["認知", "cognitive", "memory", "attention", "perception", "知覚", "判断", "意思決定"], "認知心理学"),
        (["社会心理", "social psychology", "態度", "説得", "集団", "同調", "ステレオタイプ", "偏見"], "社会心理学"),
        (["発達", "developmental", "幼児", "児童", "青年期", "アイデンティティ", "lifespan"], "発達心理学"),
        (["臨床", "clinical", "セラピー", "療法", "精神病理", "障害", "ptsd", "うつ"], "臨床心理学"),
        (["パーソナリティ", "personality", "特性論", "性格", "個人差", "情動", "emotion"], "人格・パーソナリティ心理学"),
    ]
    rows = list(conn.execute("SELECT id, name_ja, name_en, keywords_ja, keywords_en FROM social_theory WHERE subfield = '心理学'"))
    bucket = {}
    updates = []
    for r in rows:
        haystack = " ".join(filter(None, [r["name_ja"], r["name_en"], r["keywords_ja"], r["keywords_en"]])).lower()
        matched = False
        for keywords, name in rules_kw:
            if any(kw.lower() in haystack for kw in keywords):
                bucket[name] = bucket.get(name, 0) + 1
                updates.append((name, r["id"]))
                matched = True
                break
        if not matched:
            bucket["一般心理学"] = bucket.get("一般心理学", 0) + 1
            updates.append(("一般心理学", r["id"]))
    print(f"\n[1.4 心理学 → 6分割] source={len(rows)}")
    for n, c in sorted(bucket.items(), key=lambda x: -x[1]):
        print(f"  {n}: {c}")
    if commit and updates:
        conn.executemany("UPDATE social_theory SET subfield=?, updated_at=datetime('now') WHERE id=?", updates)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    split_classical_poetics(conn, args.commit)
    split_ecology(conn, args.commit)
    split_anthropology(conn, args.commit)
    split_psychology(conn, args.commit)
    if args.commit:
        conn.commit()
        print("\nCOMMITTED")
    else:
        print("\nDRY-RUN")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
