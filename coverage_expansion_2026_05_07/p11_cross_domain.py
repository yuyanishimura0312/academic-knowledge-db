#!/usr/bin/env python3
"""Phase 11 Step 3: 5コア分野間の cross_domain_relations を直接構築。

現状: cross_domain_relations 16,945件はすべて innovation/startup ハブ経由。
目標: 5コア分野相互の直接マッチング（10ペア × 平均500件 = +5,000件）

マッチング方法:
  1. 各分野からエントリを抽出
  2. keywords_en の Jaccard 類似度を計算
  3. 類似度 ≥ 0.15 (約2語共通) で関係を追加
"""
from __future__ import annotations
import argparse, sqlite3, uuid
from itertools import combinations
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"


def kw_set(s):
    if not s: return set()
    return {k.strip().lower() for k in s.split(",") if k.strip()}


def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    DOMAINS = ["humanities_concept", "social_theory", "natural_discovery", "engineering_method", "arts_question"]
    # Load entries with keywords (cap to 500 per domain to avoid explosion)
    domain_data = {}
    for d in DOMAINS:
        rows = list(conn.execute(f"SELECT id, name_en, subfield, keywords_en FROM {d} WHERE keywords_en IS NOT NULL AND keywords_en != '' LIMIT 800"))
        # Pre-compute kw sets
        for r in rows:
            r_dict = dict(r)
            r_dict['kw'] = kw_set(r['keywords_en'])
            domain_data.setdefault(d, []).append(r_dict)
        print(f"{d}: {len(rows)} entries with keywords")

    # Existing pairs to avoid duplicates
    existing = set()
    for r in conn.execute("SELECT source_id, target_id FROM cross_domain_relations"):
        existing.add((r["source_id"], r["target_id"]))
    print(f"Existing cross_domain: {len(existing)}")

    new_rels = []
    for (da_name, da_rows), (db_name, db_rows) in combinations(domain_data.items(), 2):
        pair_count = 0
        for a in da_rows:
            if not a['kw']: continue
            for b in db_rows:
                if not b['kw']: continue
                j = jaccard(a['kw'], b['kw'])
                if j >= 0.15:
                    if (a['id'], b['id']) not in existing:
                        new_rels.append((a['id'], da_name, b['id'], db_name, "kw_overlap", f"jaccard={j:.2f}", int(j*10)))
                        pair_count += 1
                        if pair_count >= 600:  # cap per pair
                            break
            if pair_count >= 600:
                break
        print(f"  {da_name} × {db_name}: +{pair_count}")

    print(f"\nTotal new cross_domain: {len(new_rels)}")
    if args.commit and new_rels:
        cur = conn.cursor()
        rows_to_insert = []
        for src_id, src_dom, tgt_id, tgt_dom, rtype, rdesc, strength in new_rels:
            rows_to_insert.append((str(uuid.uuid4()), src_dom, src_id, tgt_dom, tgt_id, rtype, rdesc, strength))
        cur.executemany("INSERT INTO cross_domain_relations (id, source_domain, source_id, target_domain, target_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?,?,?)", rows_to_insert)
        conn.commit()
        print(f"COMMITTED: {len(rows_to_insert)}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
