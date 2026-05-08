#!/usr/bin/env python3
"""Step 6: 関係ネットワーク強化。

目標: 関係数 / 概念数 比 ≥ 2.5 (現状 約1.34)

3層構築:
1. intra-subfield: era_start チェーン (extends/derived_from)
2. inter-subfield: keyword overlap (related_to)
3. cross-domain: keyword overlap across 5 domains (cross_domain_relations)
"""
from __future__ import annotations

import argparse
import sqlite3
import uuid
from collections import defaultdict
from itertools import combinations
from pathlib import Path

DB = Path(__file__).parent.parent / "academic.db"

DOMAIN_CONFIG = [
    ("humanities_concept", "humanities_concept_relations"),
    ("social_theory", "social_theory_relations"),
    ("natural_discovery", "natural_discovery_relations"),
    ("engineering_method", "engineering_method_relations"),
    ("arts_question", "arts_question_relations"),
]


def kw_set(s: str | None) -> set[str]:
    if not s:
        return set()
    return {k.strip().lower() for k in s.split(",") if k.strip()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", action="store_true")
    args = p.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    summary = {"intra_added": 0, "inter_added": 0, "cross_added": 0}

    # === 1. intra-subfield era_chain ===
    print("=== Step 6.1: intra-subfield era_chain ===")
    for tbl, rel_tbl in DOMAIN_CONFIG:
        rows = conn.execute(f"""
            SELECT id, name_en, subfield, era_start, keywords_en
            FROM {tbl}
            WHERE subfield IS NOT NULL AND subfield != '' AND subfield != '未分類'
        """).fetchall()
        # Existing relation pairs (to avoid duplicates)
        existing = set()
        for r in conn.execute(f"SELECT source_concept_id, target_concept_id FROM {rel_tbl}"):
            existing.add((r["source_concept_id"], r["target_concept_id"]))

        by_sub = defaultdict(list)
        for r in rows:
            by_sub[r["subfield"]].append(r)

        new_rels = []
        for sub, items in by_sub.items():
            items.sort(key=lambda r: r["era_start"] or 0)
            for a, b in zip(items, items[1:]):
                if (a["id"], b["id"]) in existing:
                    continue
                new_rels.append((str(uuid.uuid4()), a["id"], b["id"], "derived_from", f"era_chain in {sub}", 5))

        print(f"  [{tbl}] +{len(new_rels)} intra relations")
        summary["intra_added"] += len(new_rels)
        if args.commit and new_rels:
            conn.executemany(
                f"INSERT INTO {rel_tbl} (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?)",
                new_rels,
            )

    # === 2. inter-subfield keyword overlap ===
    print("\n=== Step 6.2: inter-subfield keyword overlap ===")
    for tbl, rel_tbl in DOMAIN_CONFIG:
        rows = list(conn.execute(f"SELECT id, name_en, subfield, keywords_en FROM {tbl} WHERE subfield != '未分類'").fetchall())
        existing = set()
        for r in conn.execute(f"SELECT source_concept_id, target_concept_id FROM {rel_tbl}"):
            existing.add((r["source_concept_id"], r["target_concept_id"]))

        by_sub = defaultdict(list)
        for r in rows:
            by_sub[r["subfield"]].append(r)

        new_rels = []
        sub_pairs = list(combinations(by_sub.keys(), 2))
        for sa, sb in sub_pairs:
            # cap to avoid explosion
            ai = by_sub[sa][:30]
            bi = by_sub[sb][:30]
            for a in ai:
                kwa = kw_set(a["keywords_en"])
                if not kwa:
                    continue
                for b in bi:
                    kwb = kw_set(b["keywords_en"])
                    if not kwb:
                        continue
                    overlap = kwa & kwb
                    if len(overlap) >= 2 and (a["id"], b["id"]) not in existing:
                        new_rels.append((str(uuid.uuid4()), a["id"], b["id"], "related_to", f"kw: {','.join(sorted(overlap)[:3])}", 3))
                        if len(new_rels) > 5000:  # cap per domain
                            break
                if len(new_rels) > 5000:
                    break
            if len(new_rels) > 5000:
                break

        print(f"  [{tbl}] +{len(new_rels)} inter relations")
        summary["inter_added"] += len(new_rels)
        if args.commit and new_rels:
            conn.executemany(
                f"INSERT INTO {rel_tbl} (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?)",
                new_rels,
            )

    # === 3. cross_domain_relations ===
    print("\n=== Step 6.3: cross_domain_relations ===")
    # Schema check
    cols = [c[1] for c in conn.execute("PRAGMA table_info(cross_domain_relations)").fetchall()]
    print(f"  cross_domain_relations cols: {cols}")
    if not cols:
        print("  no table, skipping")
    else:
        existing_cross = set()
        # Use actual schema column names
        if "source_id" in cols and "target_id" in cols:
            for r in conn.execute("SELECT source_id, target_id FROM cross_domain_relations LIMIT 100000"):
                existing_cross.add((r["source_id"], r["target_id"]))
        elif "source_concept_id" in cols and "target_concept_id" in cols:
            for r in conn.execute("SELECT source_concept_id, target_concept_id FROM cross_domain_relations LIMIT 100000"):
                existing_cross.add((r["source_concept_id"], r["target_concept_id"]))

        # Collect concepts per domain (sample for cross-domain matching, cap each)
        domain_data = {}
        for tbl, _ in DOMAIN_CONFIG:
            rows = list(conn.execute(f"SELECT id, name_en, subfield, keywords_en FROM {tbl} WHERE keywords_en IS NOT NULL AND subfield != '未分類' LIMIT 1000").fetchall())
            domain_data[tbl] = rows

        new_cross = []
        for (ta, da), (tb, db) in combinations(domain_data.items(), 2):
            for a in da[:300]:
                kwa = kw_set(a["keywords_en"])
                if not kwa:
                    continue
                for b in db[:300]:
                    kwb = kw_set(b["keywords_en"])
                    if not kwb:
                        continue
                    overlap = kwa & kwb
                    if len(overlap) >= 3:
                        if (a["id"], b["id"]) not in existing_cross:
                            new_cross.append((a["id"], ta, b["id"], tb, "cross_domain_kw_overlap", f"kw: {','.join(sorted(overlap)[:3])}"))

        print(f"  +{len(new_cross)} cross_domain candidates")
        summary["cross_added"] = len(new_cross)
        if args.commit and new_cross:
            # Schema: id, source_domain, source_id, target_domain, target_id, relation_type, relation_description, strength, created_at
            rows = []
            for src_id, src_tbl, tgt_id, tgt_tbl, rtype, rdesc in new_cross:
                rows.append((str(uuid.uuid4()), src_tbl, src_id, tgt_tbl, tgt_id, rtype, rdesc, 3))
            sql = "INSERT INTO cross_domain_relations (id, source_domain, source_id, target_domain, target_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?,?,?)"
            conn.executemany(sql, rows)

    if args.commit:
        conn.commit()
    conn.close()

    print("\n=== summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"Mode: {'COMMITTED' if args.commit else 'DRY-RUN'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
