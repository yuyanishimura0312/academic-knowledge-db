#!/usr/bin/env python3
"""
Export data from the academic knowledge database to JSON or CSV.
"""

import sqlite3
import json
import csv
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


def dict_factory(cursor, row):
    """Convert sqlite3 rows to dictionaries."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def export_domain_json(domain, output_path=None):
    """Export all data for a domain as a single JSON file."""
    if domain not in DOMAIN_TABLES:
        print(f"Error: unknown domain '{domain}'")
        return

    table = DOMAIN_TABLES[domain]
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory

    # Entities
    entities = conn.execute(f"SELECT * FROM {table} ORDER BY year_proposed").fetchall()

    # Parse JSON array fields
    for e in entities:
        for field in ["keywords", "related_patents", "representative_works",
                       "affiliated_institutions", "notable_awards"]:
            if field in e and e[field] and isinstance(e[field], str):
                try:
                    e[field] = json.loads(e[field])
                except json.JSONDecodeError:
                    pass

    # Relations
    rel_table = f"{table}_relation"
    relations = conn.execute(f"SELECT * FROM {rel_table}").fetchall()

    # Researchers linked to this domain
    link_table = f"{table}_researcher_link"
    links = conn.execute(f"SELECT * FROM {link_table}").fetchall()
    researcher_ids = set(l["researcher_id"] for l in links)

    researchers = []
    if researcher_ids:
        placeholders = ",".join(["?"] * len(researcher_ids))
        researchers = conn.execute(
            f"SELECT * FROM researcher WHERE id IN ({placeholders})",
            list(researcher_ids)
        ).fetchall()
        for r in researchers:
            for field in ["affiliated_institutions", "notable_awards"]:
                if r.get(field) and isinstance(r[field], str):
                    try:
                        r[field] = json.loads(r[field])
                    except json.JSONDecodeError:
                        pass

    # Cross-domain relations involving this domain
    cross = conn.execute(
        "SELECT * FROM cross_domain_relation WHERE source_domain=? OR target_domain=?",
        (domain, domain)
    ).fetchall()

    conn.close()

    result = {
        "domain": domain,
        "export_date": __import__("datetime").datetime.now().isoformat(),
        "entities": entities,
        "entity_count": len(entities),
        "relations": relations,
        "relation_count": len(relations),
        "researchers": researchers,
        "researcher_count": len(researchers),
        "cross_domain_relations": cross,
        "cross_domain_count": len(cross),
    }

    if output_path is None:
        output_path = Path(__file__).parent.parent / "reports" / f"export_{domain}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Exported {domain}:")
    print(f"  Entities: {len(entities)}")
    print(f"  Relations: {len(relations)}")
    print(f"  Researchers: {len(researchers)}")
    print(f"  Cross-domain: {len(cross)}")
    print(f"  Output: {output_path}")


def export_domain_csv(domain, output_dir=None):
    """Export domain entities as CSV."""
    if domain not in DOMAIN_TABLES:
        print(f"Error: unknown domain '{domain}'")
        return

    table = DOMAIN_TABLES[domain]
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory

    entities = conn.execute(f"SELECT * FROM {table} ORDER BY year_proposed").fetchall()
    conn.close()

    if not entities:
        print(f"No data for domain: {domain}")
        return

    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "reports"

    output_path = output_dir / f"export_{domain}.csv"
    fieldnames = list(entities[0].keys())

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entities)

    print(f"Exported {len(entities)} entities to {output_path}")


def export_all(format="json"):
    """Export all domains."""
    for domain in DOMAIN_TABLES:
        if format == "csv":
            export_domain_csv(domain)
        else:
            export_domain_json(domain)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python export_data.py <domain> [json|csv]  Export a domain")
        print("  python export_data.py --all [json|csv]     Export all domains")
        print(f"  Domains: {', '.join(DOMAIN_TABLES.keys())}")
        sys.exit(1)

    fmt = "json"
    if len(sys.argv) > 2:
        fmt = sys.argv[2]

    if sys.argv[1] == "--all":
        export_all(fmt)
    else:
        domain = sys.argv[1]
        if fmt == "csv":
            export_domain_csv(domain)
        else:
            export_domain_json(domain)
