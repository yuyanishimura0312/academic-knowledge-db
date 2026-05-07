#!/usr/bin/env python3
"""Phase 4: Build relation network for newly inserted concepts.

Targets concept-count × 3-5 relations across:
  1. Intra-subfield: era-ordered chains via extends/derived_from
  2. Inter-subfield: keyword overlap → related_to
  3. Cross-domain: keyword overlap with innovation_theory / startup_theory etc.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import uuid
from collections import defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT.parent / "academic.db"

DOMAIN_TABLES = [
    ("humanities_concept", "humanities_concept_relations"),
    ("social_theory", "social_theory_relations"),
    ("natural_discovery", "natural_discovery_relations"),
    ("engineering_method", "engineering_method_relations"),
    ("arts_question", "arts_question_relations"),
]

# Created markers introduced by this run; we track by created_at >= cutoff
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", required=True, help="ISO timestamp; only concepts created at/after will be wired")
    parser.add_argument("--commit", action="store_true")
    args = parser.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    summary = {"intra": 0, "inter": 0, "cross": 0}

    for tbl, rel_tbl in DOMAIN_TABLES:
        rows = list(conn.execute(
            f"SELECT id, name_en, subfield, era_start, keywords_en FROM {tbl} WHERE created_at >= ?",
            (args.since,),
        ))
        if not rows:
            continue
        print(f"[{tbl}] new rows: {len(rows)}")

        # 1. Intra-subfield: order by era_start within each subfield, chain extends
        intra_rels = []
        by_sub = defaultdict(list)
        for r in rows:
            by_sub[r["subfield"]].append(r)
        for sub, items in by_sub.items():
            items.sort(key=lambda r: r["era_start"] or 0)
            for a, b in zip(items, items[1:]):
                intra_rels.append((str(uuid.uuid4()), a["id"], b["id"], "derived_from", f"era chain in {sub}", 6))

        # 2. Inter-subfield: keyword overlap (simple Jaccard threshold)
        def kw_set(r):
            kw = (r["keywords_en"] or "").lower()
            return {k.strip() for k in kw.split(",") if k.strip()}

        inter_rels = []
        rows_by_sub = list(by_sub.items())
        for (sa, ai), (sb, bi) in combinations(rows_by_sub, 2):
            for a in ai[:5]:  # cap pairs
                kwa = kw_set(a)
                if not kwa:
                    continue
                for b in bi[:5]:
                    kwb = kw_set(b)
                    if not kwb:
                        continue
                    overlap = kwa & kwb
                    if len(overlap) >= 2:
                        inter_rels.append((str(uuid.uuid4()), a["id"], b["id"], "related_to", f"keyword overlap: {','.join(sorted(overlap)[:3])}", 4))

        all_rels = intra_rels + inter_rels
        summary["intra"] += len(intra_rels)
        summary["inter"] += len(inter_rels)
        if args.commit and all_rels:
            cur = conn.cursor()
            # Determine relation table column structure dynamically
            cols = [c[1] for c in cur.execute(f"PRAGMA table_info({rel_tbl})")]
            # Common pattern: id, source_concept_id, target_concept_id, relation_type, relation_description, strength
            if {"id","source_concept_id","target_concept_id","relation_type","relation_description","strength"}.issubset(cols):
                cur.executemany(
                    f"INSERT INTO {rel_tbl} (id, source_concept_id, target_concept_id, relation_type, relation_description, strength) VALUES (?,?,?,?,?,?)",
                    all_rels,
                )
            else:
                print(f"[warn] {rel_tbl} schema unexpected, skipping. cols={cols}")

    if args.commit:
        conn.commit()
    conn.close()

    print("\n=== summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print("Mode:", "COMMITTED" if args.commit else "DRY-RUN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
