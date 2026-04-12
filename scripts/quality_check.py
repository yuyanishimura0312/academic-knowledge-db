#!/usr/bin/env python3
"""
Quality check for the academic knowledge database.
Calculates coverage, completeness, relation density, and reliability metrics.
"""

import sqlite3
import json
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"

DOMAIN_TABLES = {
    "humanities": "humanities_concept",
    "social_sciences": "social_theory",
    "natural_sciences": "natural_discovery",
    "engineering": "engineering_method",
    "arts": "arts_question",
}

# Quality thresholds
THRESHOLDS = {
    "coverage_rate": 0.70,       # 70% of estimated entities collected
    "completeness_rate": 0.80,   # 80% of fields non-empty
    "relation_density": 2.0,     # 2+ relations per entity
    "primary_source_rate": 0.50, # 50% primary sources
    "cross_domain_rate": 0.10,   # 10% entities have cross-domain links
}


def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def check_domain(conn, domain):
    """Run quality checks for a single domain."""
    table = DOMAIN_TABLES[domain]
    rel_table = f"{table}_relation"

    # 1. Entity count
    entity_count = conn.execute(f"SELECT COUNT(*) as c FROM {table}").fetchone()["c"]

    # 2. Survey frame coverage
    frames = conn.execute(
        "SELECT name, estimated_unit_count, survey_status FROM survey_frame WHERE domain=?",
        (domain,)
    ).fetchall()

    total_estimated = sum(f["estimated_unit_count"] or 0 for f in frames)
    coverage_rate = entity_count / total_estimated if total_estimated > 0 else 0

    # 3. Data completeness (check non-null fields)
    if entity_count > 0:
        sample = conn.execute(f"SELECT * FROM {table} LIMIT 1").fetchone()
        fields = [k for k in sample.keys() if k not in ("id", "created_at", "updated_at")]
        total_cells = entity_count * len(fields)

        non_null = 0
        for field in fields:
            cnt = conn.execute(
                f"SELECT COUNT(*) as c FROM {table} WHERE {field} IS NOT NULL AND {field} != ''"
            ).fetchone()["c"]
            non_null += cnt

        completeness_rate = non_null / total_cells if total_cells > 0 else 0

        # Per-field completeness
        field_completeness = {}
        for field in fields:
            cnt = conn.execute(
                f"SELECT COUNT(*) as c FROM {table} WHERE {field} IS NOT NULL AND {field} != ''"
            ).fetchone()["c"]
            field_completeness[field] = cnt / entity_count if entity_count > 0 else 0
    else:
        completeness_rate = 0
        field_completeness = {}

    # 4. Relation density
    relation_count = conn.execute(f"SELECT COUNT(*) as c FROM {rel_table}").fetchone()["c"]
    relation_density = relation_count / entity_count if entity_count > 0 else 0

    # 5. Source reliability distribution
    reliability_dist = {}
    for level in ("primary", "secondary", "tertiary"):
        cnt = conn.execute(
            f"SELECT COUNT(*) as c FROM {table} WHERE source_reliability=?",
            (level,)
        ).fetchone()["c"]
        reliability_dist[level] = cnt

    no_source = conn.execute(
        f"SELECT COUNT(*) as c FROM {table} WHERE source_reliability IS NULL"
    ).fetchone()["c"]
    reliability_dist["unspecified"] = no_source

    primary_rate = reliability_dist.get("primary", 0) / entity_count if entity_count > 0 else 0

    # 6. Cross-domain relations
    cross_count = conn.execute(
        "SELECT COUNT(*) as c FROM cross_domain_relation WHERE source_domain=? OR target_domain=?",
        (domain, domain)
    ).fetchone()["c"]
    cross_rate = cross_count / entity_count if entity_count > 0 else 0

    # 7. Status distribution
    status_dist = {}
    rows = conn.execute(
        f"SELECT status, COUNT(*) as c FROM {table} GROUP BY status"
    ).fetchall()
    for row in rows:
        status_dist[row["status"] or "null"] = row["c"]

    return {
        "domain": domain,
        "entity_count": entity_count,
        "estimated_total": total_estimated,
        "coverage_rate": round(coverage_rate, 3),
        "completeness_rate": round(completeness_rate, 3),
        "relation_count": relation_count,
        "relation_density": round(relation_density, 2),
        "primary_source_rate": round(primary_rate, 3),
        "cross_domain_count": cross_count,
        "cross_domain_rate": round(cross_rate, 3),
        "reliability_distribution": reliability_dist,
        "status_distribution": status_dist,
        "field_completeness": {
            k: round(v, 2) for k, v in sorted(field_completeness.items(), key=lambda x: x[1])
        },
        "survey_frames": [
            {"name": f["name"], "estimated": f["estimated_unit_count"], "status": f["survey_status"]}
            for f in frames
        ],
    }


def evaluate(metrics):
    """Evaluate metrics against thresholds and return pass/fail with recommendations."""
    issues = []
    passes = []

    checks = [
        ("coverage_rate", THRESHOLDS["coverage_rate"],
         "Coverage rate {val:.0%} < {thresh:.0%}. More entities needed."),
        ("completeness_rate", THRESHOLDS["completeness_rate"],
         "Completeness rate {val:.0%} < {thresh:.0%}. Fill in missing fields."),
        ("relation_density", THRESHOLDS["relation_density"],
         "Relation density {val:.1f} < {thresh:.1f}. Run Genealogy Tracer on more entities."),
        ("primary_source_rate", THRESHOLDS["primary_source_rate"],
         "Primary source rate {val:.0%} < {thresh:.0%}. Verify more entries against primary sources."),
        ("cross_domain_rate", THRESHOLDS["cross_domain_rate"],
         "Cross-domain rate {val:.0%} < {thresh:.0%}. Run Cross-Domain Linker."),
    ]

    for key, threshold, msg_template in checks:
        val = metrics.get(key, 0)
        if val < threshold:
            issues.append(msg_template.format(val=val, thresh=threshold))
        else:
            passes.append(f"{key}: {val:.2f} (threshold: {threshold})")

    return passes, issues


def print_report(metrics):
    """Print a formatted quality report."""
    domain = metrics["domain"]
    print(f"\n{'='*60}")
    print(f"  Quality Report: {domain}")
    print(f"{'='*60}")

    print(f"\n  Entities:        {metrics['entity_count']} / {metrics['estimated_total']} estimated")
    print(f"  Coverage:        {metrics['coverage_rate']:.0%}")
    print(f"  Completeness:    {metrics['completeness_rate']:.0%}")
    print(f"  Relations:       {metrics['relation_count']} (density: {metrics['relation_density']:.1f})")
    print(f"  Primary sources: {metrics['primary_source_rate']:.0%}")
    print(f"  Cross-domain:    {metrics['cross_domain_count']} (rate: {metrics['cross_domain_rate']:.0%})")

    # Status distribution
    if metrics["status_distribution"]:
        print(f"\n  Status distribution:")
        for status, count in sorted(metrics["status_distribution"].items()):
            print(f"    {status}: {count}")

    # Source reliability
    if metrics["reliability_distribution"]:
        print(f"\n  Source reliability:")
        for level, count in metrics["reliability_distribution"].items():
            print(f"    {level}: {count}")

    # Incomplete fields (below 50%)
    low_fields = {k: v for k, v in metrics["field_completeness"].items() if v < 0.5}
    if low_fields:
        print(f"\n  Fields with low completeness (<50%):")
        for field, rate in low_fields.items():
            print(f"    {field}: {rate:.0%}")

    # Survey frame status
    if metrics["survey_frames"]:
        print(f"\n  Survey frames:")
        for sf in metrics["survey_frames"]:
            print(f"    [{sf['status']}] {sf['name']} (est. {sf['estimated']})")

    # Evaluation
    passes, issues = evaluate(metrics)
    if issues:
        print(f"\n  ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"    - {issue}")
    if passes:
        print(f"\n  PASSED ({len(passes)}):")
        for p in passes:
            print(f"    + {p}")

    overall = "PASS" if not issues else "NEEDS WORK"
    print(f"\n  Overall: {overall}")
    print(f"{'='*60}")

    return overall


def check_all():
    """Run quality checks for all domains."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory

    results = {}
    for domain in DOMAIN_TABLES:
        metrics = check_domain(conn, domain)
        results[domain] = metrics
        print_report(metrics)

    conn.close()

    # Summary
    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    total_entities = sum(r["entity_count"] for r in results.values())
    total_relations = sum(r["relation_count"] for r in results.values())
    total_cross = sum(r["cross_domain_count"] for r in results.values()) // 2  # avoid double count
    print(f"  Total entities:  {total_entities}")
    print(f"  Total relations: {total_relations}")
    print(f"  Cross-domain:    {total_cross}")

    # Save report as JSON
    report_path = Path(__file__).parent.parent / "reports" / "quality_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n  Report saved: {report_path}")


if __name__ == "__main__":
    if not DB_PATH.exists():
        print(f"Database not found: {DB_PATH}")
        print("Run init_db.py first.")
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] in DOMAIN_TABLES:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = dict_factory
        metrics = check_domain(conn, sys.argv[1])
        conn.close()
        print_report(metrics)
    else:
        check_all()
