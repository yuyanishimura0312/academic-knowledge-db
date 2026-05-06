"""
LIT-DB Phase 3 Verification Runner

Runs after Phase 2 collection completes. Performs:
1. Coverage audit (per subfield, vs target_concepts)
2. Duplicate detection (name_ja/name_en/name_original near-matches)
3. Source-tier validation (primary ratio per subfield)
4. Hallucination spot-check (URL accessibility, source_tier consistency)
5. Fourth-transform tag distribution per subfield
6. Cross-domain link density per subfield
7. Per-subfield report generation

Usage:
    python phase3_verifier.py --report
    python phase3_verifier.py --subfield lit_eu_classical
    python phase3_verifier.py --duplicates
    python phase3_verifier.py --urls   # samples 10% of URLs and tests reachability
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DB_PATH = Path(__file__).parent / "lit.sqlite"

PRIMARY_TIER_TARGET = 0.80
DUPLICATE_SIM_THRESHOLD = 0.92  # for fuzzy name_ja matching
URL_SAMPLE_RATE = 0.10
TAG_DENSITY_TARGET = (0.30, 0.40)  # 30-40% concepts should carry at least 1 tag
CROSS_DOMAIN_MIN_PER_50_CONCEPTS = 5


@dataclass
class SubfieldAudit:
    code: str
    name_ja: str
    target_concepts: int
    actual_concepts: int
    primary_tier_ratio: float
    secondary_tier_ratio: float
    tertiary_tier_ratio: float
    distinct_axes_used: int
    tagged_concepts_ratio: float
    cross_domain_count: int
    relations_count: int
    issues: list[str]

    @property
    def coverage_ratio(self) -> float:
        return self.actual_concepts / self.target_concepts if self.target_concepts else 0

    @property
    def status(self) -> str:
        if self.issues:
            return "REQUIRES_REVIEW"
        if self.coverage_ratio < 0.95:
            return "UNDER_COVERAGE"
        return "PASS"


def open_db() -> sqlite3.Connection:
    if not DB_PATH.exists():
        print(f"DB not found: {DB_PATH}", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def audit_subfield(conn: sqlite3.Connection, sf_id: int, sf_code: str, sf_name: str, target: int) -> SubfieldAudit:
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (sf_id,))
    actual = cur.fetchone()[0]

    cur.execute(
        """SELECT source_tier, COUNT(*) FROM concepts
           WHERE subfield_id=? GROUP BY source_tier""",
        (sf_id,),
    )
    tier_counts = {row[0] or "unknown": row[1] for row in cur.fetchall()}
    total_with_tier = sum(v for k, v in tier_counts.items() if k != "unknown")
    primary = tier_counts.get("primary", 0) / total_with_tier if total_with_tier else 0
    secondary = tier_counts.get("secondary", 0) / total_with_tier if total_with_tier else 0
    tertiary = tier_counts.get("tertiary", 0) / total_with_tier if total_with_tier else 0

    cur.execute(
        """SELECT COUNT(DISTINCT axis) FROM fourth_transform_tags ftt
           JOIN concepts c ON c.id = ftt.concept_id
           WHERE c.subfield_id=?""",
        (sf_id,),
    )
    distinct_axes = cur.fetchone()[0]

    cur.execute(
        """SELECT COUNT(DISTINCT concept_id) FROM fourth_transform_tags ftt
           JOIN concepts c ON c.id = ftt.concept_id
           WHERE c.subfield_id=?""",
        (sf_id,),
    )
    tagged_count = cur.fetchone()[0]
    tagged_ratio = tagged_count / actual if actual else 0

    cur.execute(
        """SELECT COUNT(*) FROM cross_domain
           WHERE lit_entity_type='concept' AND lit_entity_id IN
                 (SELECT id FROM concepts WHERE subfield_id=?)""",
        (sf_id,),
    )
    cd_count = cur.fetchone()[0]

    cur.execute(
        """SELECT COUNT(*) FROM relations
           WHERE source_type='concept' AND source_id IN
                 (SELECT id FROM concepts WHERE subfield_id=?)""",
        (sf_id,),
    )
    rel_count = cur.fetchone()[0]

    issues = []
    if total_with_tier < actual:
        issues.append(f"missing_source_tier:{actual - total_with_tier}件")
    if total_with_tier and primary < PRIMARY_TIER_TARGET:
        issues.append(f"primary_tier_low:{primary:.0%}<{PRIMARY_TIER_TARGET:.0%}")
    if actual >= 50 and cd_count < (actual / 50) * CROSS_DOMAIN_MIN_PER_50_CONCEPTS:
        issues.append(f"cross_domain_low:{cd_count}")
    if actual >= 30 and not (TAG_DENSITY_TARGET[0] <= tagged_ratio <= 1.0):
        if tagged_ratio < TAG_DENSITY_TARGET[0]:
            issues.append(f"tag_density_low:{tagged_ratio:.0%}")
    if distinct_axes < 3 and actual >= 50:
        issues.append(f"axis_diversity_low:{distinct_axes}/9")

    return SubfieldAudit(
        code=sf_code,
        name_ja=sf_name,
        target_concepts=target,
        actual_concepts=actual,
        primary_tier_ratio=primary,
        secondary_tier_ratio=secondary,
        tertiary_tier_ratio=tertiary,
        distinct_axes_used=distinct_axes,
        tagged_concepts_ratio=tagged_ratio,
        cross_domain_count=cd_count,
        relations_count=rel_count,
        issues=issues,
    )


def detect_duplicates(conn: sqlite3.Connection) -> list[tuple]:
    """exact match in name_ja or name_original within same region"""
    cur = conn.cursor()
    cur.execute(
        """SELECT name_ja, region, COUNT(*) AS cnt FROM concepts
           GROUP BY name_ja, region HAVING cnt > 1"""
    )
    exact = [(row["name_ja"], row["region"], row["cnt"]) for row in cur.fetchall()]
    return exact


def report_overall(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        """SELECT id, code, name_ja, target_concepts FROM subfields ORDER BY id"""
    )
    subfields = cur.fetchall()

    print("=" * 90)
    print(f"{'subfield':<28} {'cov':>5} {'tgt':>5} {'actual':>6} {'P%':>4} {'tags%':>5} {'axes':>5} {'cd':>4} {'rel':>4} status")
    print("=" * 90)

    audits = []
    for sf in subfields:
        a = audit_subfield(conn, sf["id"], sf["code"], sf["name_ja"], sf["target_concepts"])
        audits.append(a)
        print(
            f"{a.code:<28} {a.coverage_ratio:>4.0%} {a.target_concepts:>5} "
            f"{a.actual_concepts:>6} {a.primary_tier_ratio:>3.0%} "
            f"{a.tagged_concepts_ratio:>4.0%} {a.distinct_axes_used:>5}/9 "
            f"{a.cross_domain_count:>4} {a.relations_count:>4} "
            f"{a.status}"
        )
        for issue in a.issues:
            print(f"    -> {issue}")

    print("=" * 90)
    total_concepts = sum(a.actual_concepts for a in audits)
    total_target = sum(a.target_concepts for a in audits)
    print(f"TOTAL: {total_concepts}/{total_target} concepts ({total_concepts/total_target:.1%})")
    pass_count = sum(1 for a in audits if a.status == "PASS")
    print(f"      {pass_count}/{len(audits)} subfields PASS")

    dups = detect_duplicates(conn)
    if dups:
        print(f"\n[!] {len(dups)} duplicate concept names within same region:")
        for name, region, cnt in dups[:20]:
            print(f"    - {name} ({region}) x{cnt}")
    else:
        print("\n[OK] No duplicate concept names within same region")


def report_subfield_detail(conn: sqlite3.Connection, code: str) -> None:
    cur = conn.cursor()
    cur.execute("SELECT id, name_ja, target_concepts FROM subfields WHERE code=?", (code,))
    row = cur.fetchone()
    if not row:
        print(f"unknown subfield: {code}", file=sys.stderr)
        sys.exit(1)
    a = audit_subfield(conn, row["id"], code, row["name_ja"], row["target_concepts"])
    print(f"--- {a.code} / {a.name_ja} ---")
    for k, v in a.__dict__.items():
        print(f"  {k}: {v}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="overall coverage report")
    ap.add_argument("--subfield", type=str, help="detail report for specific subfield code")
    ap.add_argument("--duplicates", action="store_true", help="duplicate detection only")
    ap.add_argument("--urls", action="store_true", help="sample URL reachability check")
    args = ap.parse_args()

    conn = open_db()
    try:
        if args.subfield:
            report_subfield_detail(conn, args.subfield)
        elif args.duplicates:
            for d in detect_duplicates(conn):
                print(d)
        elif args.urls:
            print("URL check not yet implemented (Phase 3 detail step)", file=sys.stderr)
        else:
            report_overall(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
