#!/usr/bin/env python3
"""
Export genealogy data for D3.js visualization.
Produces a JSON file with nodes (concepts) and links (relations) for timeline tree view.
"""

import json
import sqlite3
from pathlib import Path
from collections import defaultdict

DB_PATH = Path(__file__).parent.parent / "academic.db"
OUTPUT = Path(__file__).parent.parent / "genealogy_data.json"

DOMAINS = {
    "humanities_concept": {"label": "人文学", "color": "#CC1400"},
    "social_theory": {"label": "社会科学", "color": "#2563EB"},
    "natural_discovery": {"label": "自然科学", "color": "#16A34A"},
    "engineering_method": {"label": "工学", "color": "#7C3AED"},
    "arts_question": {"label": "芸術", "color": "#EA580C"},
}


def export():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    nodes = []
    links = []
    node_ids = set()

    for table, meta in DOMAINS.items():
        # Get all concepts
        rows = conn.execute(
            f"SELECT id, name_ja, name_en, era_start, era_end, subfield, "
            f"school_of_thought, definition, status "
            f"FROM {table} ORDER BY era_start"
        ).fetchall()

        for r in rows:
            node = {
                "id": r["id"],
                "name_ja": r["name_ja"] or "",
                "name_en": r["name_en"] or "",
                "era_start": r["era_start"],
                "era_end": r["era_end"],
                "domain": table,
                "domain_label": meta["label"],
                "color": meta["color"],
                "subfield": r["subfield"] or "",
                "school": r["school_of_thought"] or "",
                "definition": (r["definition"] or "")[:200],
                "status": r["status"] or "active",
            }
            nodes.append(node)
            node_ids.add(r["id"])

        # Get relations
        rel_table = f"{table}_relations"
        rels = conn.execute(
            f"SELECT source_concept_id, target_concept_id, relation_type, "
            f"strength, relation_description "
            f"FROM {rel_table}"
        ).fetchall()

        for r in rels:
            src = r["source_concept_id"]
            tgt = r["target_concept_id"]
            if src in node_ids and tgt in node_ids and src != tgt:
                links.append({
                    "source": src,
                    "target": tgt,
                    "type": r["relation_type"] or "related_to",
                    "strength": r["strength"] or 5,
                    "description": r["relation_description"] or "",
                })

    # Cross-domain relations
    cross = conn.execute(
        "SELECT source_id, target_id, source_domain, target_domain, "
        "relation_type, strength, relation_description "
        "FROM cross_domain_relations"
    ).fetchall()

    for r in cross:
        if r["source_id"] in node_ids and r["target_id"] in node_ids:
            links.append({
                "source": r["source_id"],
                "target": r["target_id"],
                "type": r["relation_type"] or "cross_domain",
                "strength": r["strength"] or 5,
                "description": r["relation_description"] or "",
                "cross_domain": True,
            })

    conn.close()

    # Compute statistics
    era_counts = defaultdict(int)
    for n in nodes:
        era = n["era_start"]
        if era is None:
            continue
        if era < 0:
            bucket = "BCE"
        elif era < 500:
            bucket = "0-500"
        elif era < 1500:
            bucket = "500-1500"
        elif era < 1800:
            bucket = "1500-1800"
        elif era < 1900:
            bucket = "1800-1900"
        elif era < 1960:
            bucket = "1900-1960"
        else:
            bucket = "1960+"
        era_counts[bucket] += 1

    domain_counts = defaultdict(int)
    for n in nodes:
        domain_counts[n["domain"]] += 1

    # Identify root nodes (no incoming derived_from/extends links)
    targets_of_derivation = set()
    for l in links:
        if l["type"] in ("derived_from", "extends", "supersedes", "generalizes"):
            targets_of_derivation.add(l["target"])

    roots = [n["id"] for n in nodes if n["id"] not in targets_of_derivation and n["era_start"] is not None]

    output = {
        "nodes": nodes,
        "links": links,
        "roots": roots[:100],  # Limit for performance
        "stats": {
            "total_nodes": len(nodes),
            "total_links": len(links),
            "era_distribution": dict(era_counts),
            "domain_distribution": {DOMAINS[k]["label"]: v for k, v in domain_counts.items()},
        },
        "domains": {k: v for k, v in DOMAINS.items()},
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False)

    print(f"Exported: {OUTPUT}")
    print(f"  Nodes: {len(nodes)}")
    print(f"  Links: {len(links)}")
    print(f"  Roots: {len(roots)}")
    print(f"  File size: {OUTPUT.stat().st_size:,} bytes")


if __name__ == "__main__":
    export()
