#!/usr/bin/env python3
"""
Import collected JSON data into the academic knowledge database.
Handles all 5 domain tables, researchers, publications, and relations.
"""

import sqlite3
import json
import uuid
import os
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"
COLLECTED_DIR = Path(__file__).parent.parent / "collected"

# Map domain names to table names and their specific fields
DOMAIN_CONFIG = {
    "humanities": {
        "table": "humanities_concept",
        "specific_fields": [
            "blind_spot_addressed", "reinterpretation_history", "cultural_context"
        ],
        "relation_table": "humanities_concept_relation",
        "valid_relations": [
            "derived_from", "critiques", "reinterprets",
            "extends", "opposes", "synthesizes"
        ],
    },
    "social_sciences": {
        "table": "social_theory",
        "specific_fields": [
            "predictive_power", "operationalization",
            "empirical_support", "policy_implications"
        ],
        "relation_table": "social_theory_relation",
        "valid_relations": [
            "derived_from", "critiques", "extends", "empirically_tests",
            "synthesizes", "competes_with", "applies_to_policy"
        ],
    },
    "natural_sciences": {
        "table": "natural_discovery",
        "specific_fields": [
            "mathematical_formulation", "experimental_verification",
            "applicable_scale", "precision_level"
        ],
        "relation_table": "natural_discovery_relation",
        "valid_relations": [
            "derived_from", "generalizes", "experimentally_confirms",
            "contradicts", "supersedes", "enables"
        ],
    },
    "engineering": {
        "table": "engineering_method",
        "specific_fields": [
            "technology_readiness_level", "related_patents",
            "industry_applications", "problem_type", "scientific_basis"
        ],
        "relation_table": "engineering_method_relation",
        "valid_relations": [
            "derived_from", "improves", "supersedes",
            "combines", "based_on", "standardizes"
        ],
    },
    "arts": {
        "table": "arts_question",
        "specific_fields": [
            "target_assumption", "medium", "representative_works",
            "movement_affiliation", "sensory_dimension"
        ],
        "relation_table": "arts_question_relation",
        "valid_relations": [
            "derived_from", "deepens", "counters",
            "translates_medium", "revives", "inspires"
        ],
    },
}

# Common fields shared across all domain tables
COMMON_FIELDS = [
    "name", "name_en", "name_original", "description", "description_detailed",
    "impact", "year_proposed", "year_range", "geographic_origin", "status",
    "paradigm_school", "keywords", "source_reliability"
]


def generate_id():
    return str(uuid.uuid4())


def serialize_list(value):
    """Convert list to JSON string for storage."""
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return value


def import_entities(conn, domain, data):
    """Import entities (concepts/theories/discoveries/methods/questions) into the domain table."""
    config = DOMAIN_CONFIG[domain]
    table = config["table"]
    fields = COMMON_FIELDS + config["specific_fields"]

    imported = 0
    id_map = {}  # name -> id mapping for relation building

    for item in data:
        entity_id = item.get("id") or generate_id()
        id_map[item.get("name", "")] = entity_id
        if item.get("name_en"):
            id_map[item["name_en"]] = entity_id

        values = {"id": entity_id}
        for f in fields:
            val = item.get(f)
            # Serialize lists (keywords, related_patents, representative_works)
            if isinstance(val, list):
                val = json.dumps(val, ensure_ascii=False)
            values[f] = val

        cols = ", ".join(values.keys())
        placeholders = ", ".join(["?"] * len(values))
        sql = f"INSERT OR REPLACE INTO {table} ({cols}) VALUES ({placeholders})"

        try:
            conn.execute(sql, list(values.values()))
            imported += 1
        except sqlite3.IntegrityError as e:
            print(f"  Warning: skipped {item.get('name', '?')}: {e}")

    return imported, id_map


def import_researcher(conn, item):
    """Import a single researcher, return their ID."""
    researcher_id = item.get("id") or generate_id()

    values = {
        "id": researcher_id,
        "name": item.get("name"),
        "name_en": item.get("name_en"),
        "name_original": item.get("name_original"),
        "birth_year": item.get("birth_year"),
        "death_year": item.get("death_year"),
        "nationality": item.get("nationality"),
        "primary_domain": item.get("primary_domain"),
        "affiliated_institutions": serialize_list(item.get("affiliated_institutions")),
        "overall_research_theme": item.get("overall_research_theme"),
        "bio_summary": item.get("bio_summary"),
        "h_index": item.get("h_index"),
        "notable_awards": serialize_list(item.get("notable_awards")),
    }

    cols = ", ".join(values.keys())
    placeholders = ", ".join(["?"] * len(values))
    conn.execute(
        f"INSERT OR REPLACE INTO researcher ({cols}) VALUES ({placeholders})",
        list(values.values())
    )
    return researcher_id


def import_researchers(conn, data):
    """Import a list of researchers."""
    imported = 0
    name_to_id = {}
    for item in data:
        rid = import_researcher(conn, item)
        name_to_id[item.get("name", "")] = rid
        if item.get("name_en"):
            name_to_id[item["name_en"]] = rid
        imported += 1
    return imported, name_to_id


def import_relations(conn, domain, data, id_map):
    """Import relations between entities within a domain."""
    config = DOMAIN_CONFIG[domain]
    table = config["relation_table"]
    valid = set(config["valid_relations"])

    imported = 0
    for item in data:
        rel_type = item.get("relation_type")
        if rel_type not in valid:
            print(f"  Warning: invalid relation type '{rel_type}' for {domain}, skipped")
            continue

        source_id = id_map.get(item.get("source")) or item.get("source_id")
        target_id = id_map.get(item.get("target")) or item.get("target_id")

        if not source_id or not target_id:
            print(f"  Warning: could not resolve relation {item.get('source')} -> {item.get('target')}")
            continue

        values = {
            "id": generate_id(),
            "source_id": source_id,
            "target_id": target_id,
            "relation_type": rel_type,
            "description": item.get("description"),
            "evidence_source": item.get("evidence_source"),
            "year": item.get("year"),
        }

        cols = ", ".join(values.keys())
        placeholders = ", ".join(["?"] * len(values))
        try:
            conn.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})",
                         list(values.values()))
            imported += 1
        except sqlite3.IntegrityError as e:
            print(f"  Warning: relation skipped: {e}")

    return imported


def import_cross_domain(conn, data):
    """Import cross-domain relations."""
    imported = 0
    for item in data:
        values = {
            "id": generate_id(),
            "source_domain": item.get("source_domain"),
            "source_id": item.get("source_id"),
            "target_domain": item.get("target_domain"),
            "target_id": item.get("target_id"),
            "relation_type": item.get("relation_type"),
            "description": item.get("description"),
            "evidence_source": item.get("evidence_source"),
            "year": item.get("year"),
        }
        cols = ", ".join(values.keys())
        placeholders = ", ".join(["?"] * len(values))
        try:
            conn.execute(
                f"INSERT INTO cross_domain_relation ({cols}) VALUES ({placeholders})",
                list(values.values())
            )
            imported += 1
        except sqlite3.IntegrityError as e:
            print(f"  Warning: cross-domain relation skipped: {e}")
    return imported


def import_file(filepath):
    """Import a single JSON file. The file should contain a top-level object with keys:
    - domain: str (required)
    - entities: list (domain entities)
    - researchers: list (researcher records)
    - relations: list (intra-domain relations)
    - cross_domain_relations: list (cross-domain relations)
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    domain = data.get("domain")
    if not domain or domain not in DOMAIN_CONFIG:
        print(f"Error: invalid or missing 'domain' in {filepath}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    print(f"\nImporting: {filepath}")
    print(f"  Domain: {domain}")

    id_map = {}

    # Import entities
    entities = data.get("entities", [])
    if entities:
        count, id_map = import_entities(conn, domain, entities)
        print(f"  Entities imported: {count}")

    # Import researchers
    researchers = data.get("researchers", [])
    researcher_name_to_id = {}
    if researchers:
        count, researcher_name_to_id = import_researchers(conn, researchers)
        print(f"  Researchers imported: {count}")

    # Auto-link entities to their originators via researcher_link table
    config = DOMAIN_CONFIG[domain]
    link_table = f"{config['table']}_researcher_link"
    link_count = 0
    for item in entities:
        originator = item.get("originator")
        entity_name = item.get("name", "")
        entity_id = id_map.get(entity_name)
        if originator and entity_id:
            researcher_id = researcher_name_to_id.get(originator)
            if researcher_id:
                try:
                    conn.execute(
                        f"INSERT OR IGNORE INTO {link_table} (id, entity_id, researcher_id, role, year) "
                        f"VALUES (?, ?, ?, 'originator', ?)",
                        (generate_id(), entity_id, researcher_id, item.get("year_proposed"))
                    )
                    link_count += 1
                except sqlite3.IntegrityError:
                    pass
    if link_count:
        print(f"  Researcher links created: {link_count}")

    # Import relations
    relations = data.get("relations", [])
    if relations:
        count = import_relations(conn, domain, relations, id_map)
        print(f"  Relations imported: {count}")

    # Import cross-domain relations
    cross = data.get("cross_domain_relations", [])
    if cross:
        count = import_cross_domain(conn, cross)
        print(f"  Cross-domain relations imported: {count}")

    conn.commit()
    conn.close()
    print("  Done.")


def import_directory(domain=None):
    """Import all JSON files from the collected directory."""
    if domain:
        search_dir = COLLECTED_DIR / domain
        if not search_dir.exists():
            print(f"No collected data for domain: {domain}")
            return
        files = sorted(search_dir.glob("*.json"))
    else:
        files = sorted(COLLECTED_DIR.rglob("*.json"))

    if not files:
        print("No JSON files found to import.")
        return

    for f in files:
        import_file(f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python import_data.py <file.json>        Import a single file")
        print("  python import_data.py --all               Import all collected files")
        print("  python import_data.py --domain <domain>   Import all files for a domain")
        sys.exit(1)

    if sys.argv[1] == "--all":
        import_directory()
    elif sys.argv[1] == "--domain" and len(sys.argv) > 2:
        import_directory(sys.argv[2])
    else:
        import_file(sys.argv[1])
