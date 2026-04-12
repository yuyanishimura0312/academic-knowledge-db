#!/usr/bin/env python3
"""
Import collected JSON data into the v3 academic knowledge database.
Aligned with anthropology-concepts DB schema.

Expected JSON format:
{
  "domain": "social_sciences",
  "concepts": [...],        # domain entities
  "researchers": [...],     # researcher records
  "publications": [...],    # publication records
  "relations": [...],       # concept-concept relations
  "concept_researchers": [...],  # concept-researcher links
  "concept_publications": [...]  # concept-publication links
}
"""

import sqlite3
import json
import uuid
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

COMMON_FIELDS = [
    "name_ja", "name_en", "name_original", "definition", "impact_summary",
    "subfield", "school_of_thought", "era_start", "era_end",
    "methodology_level", "target_domain", "application_conditions",
    "when_to_apply", "framing_questions", "opposing_concept_names",
    "keywords_ja", "keywords_en", "status", "source_reliability", "data_completeness"
]

DOMAIN_SPECIFIC = {
    "humanities": ["blind_spot_addressed", "reinterpretation_history", "cultural_context"],
    "social_sciences": ["predictive_power", "operationalization", "empirical_support", "policy_implications"],
    "natural_sciences": ["mathematical_formulation", "experimental_verification", "applicable_scale", "precision_level"],
    "engineering": ["technology_readiness_level", "related_patents", "industry_applications", "problem_type", "scientific_basis"],
    "arts": ["target_assumption", "medium", "representative_works", "movement_affiliation", "sensory_dimension"],
}


def gen_id():
    return str(uuid.uuid4())


def import_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    domain = data.get("domain")
    if domain not in DOMAIN_TABLES:
        print(f"Error: unknown domain '{domain}'")
        return

    table = DOMAIN_TABLES[domain]
    fields = COMMON_FIELDS + DOMAIN_SPECIFIC.get(domain, [])

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    print(f"\nImporting: {filepath}")
    print(f"  Domain: {domain}, Table: {table}")

    name_to_id = {}
    researcher_name_to_id = {}
    pub_title_to_id = {}

    # 1. Import concepts
    concepts = data.get("concepts", [])
    c_count = 0
    for item in concepts:
        cid = item.get("id") or gen_id()
        name = item.get("name_ja") or item.get("name", "")
        name_to_id[name] = cid
        if item.get("name_en"):
            name_to_id[item["name_en"]] = cid

        vals = {"id": cid}
        for f in fields:
            v = item.get(f)
            if isinstance(v, (list, dict)):
                v = json.dumps(v, ensure_ascii=False)
            vals[f] = v

        # Handle field name mapping from old format
        if "name" in item and "name_ja" not in item:
            vals["name_ja"] = item["name"]

        cols = ", ".join(vals.keys())
        phs = ", ".join(["?"] * len(vals))
        try:
            conn.execute(f"INSERT OR REPLACE INTO {table} ({cols}) VALUES ({phs})", list(vals.values()))
            c_count += 1
        except Exception as e:
            print(f"  Warning: {name}: {e}")

    print(f"  Concepts: {c_count}")

    # 2. Import researchers
    researchers = data.get("researchers", [])
    r_count = 0
    for item in researchers:
        rid = item.get("id") or gen_id()
        name = item.get("name_full") or item.get("name_ja") or ""
        researcher_name_to_id[name] = rid
        if item.get("name_ja"):
            researcher_name_to_id[item["name_ja"]] = rid

        vals = {
            "id": rid,
            "name_full": name,
            "name_ja": item.get("name_ja"),
            "birth_year": item.get("birth_year"),
            "death_year": item.get("death_year"),
            "nationality": item.get("nationality"),
            "primary_institution": item.get("primary_institution"),
            "research_themes": item.get("research_themes"),
            "biography_brief": item.get("biography_brief"),
        }
        cols = ", ".join(vals.keys())
        phs = ", ".join(["?"] * len(vals))
        try:
            conn.execute(f"INSERT OR REPLACE INTO researchers ({cols}) VALUES ({phs})", list(vals.values()))
            r_count += 1
        except Exception as e:
            print(f"  Warning researcher: {e}")

    print(f"  Researchers: {r_count}")

    # 3. Import publications
    publications = data.get("publications", [])
    p_count = 0
    for item in publications:
        pid = item.get("id") or gen_id()
        title = item.get("title", "")
        pub_title_to_id[title] = pid

        vals = {
            "id": pid,
            "title": title,
            "title_ja": item.get("title_ja"),
            "pub_year": item.get("pub_year"),
            "pub_venue": item.get("pub_venue"),
            "pub_type": item.get("pub_type", "book"),
            "abstract_summary": item.get("abstract_summary"),
            "doi_or_isbn": item.get("doi_or_isbn"),
            "url": item.get("url"),
        }
        cols = ", ".join(vals.keys())
        phs = ", ".join(["?"] * len(vals))
        try:
            conn.execute(f"INSERT OR REPLACE INTO publications ({cols}) VALUES ({phs})", list(vals.values()))
            p_count += 1
        except Exception as e:
            print(f"  Warning publication: {e}")

    print(f"  Publications: {p_count}")

    # 4. Import relations
    relations = data.get("relations", [])
    rel_count = 0
    rel_table = f"{table}_relations"
    for item in relations:
        src = name_to_id.get(item.get("source")) or item.get("source_concept_id")
        tgt = name_to_id.get(item.get("target")) or item.get("target_concept_id")
        if not src or not tgt or src == tgt:
            continue
        vals = {
            "id": gen_id(),
            "source_concept_id": src,
            "target_concept_id": tgt,
            "relation_type": item.get("relation_type", "related_to"),
            "relation_description": item.get("relation_description") or item.get("description"),
            "strength": item.get("strength", 5),
            "is_confirmed": item.get("is_confirmed", 0),
        }
        cols = ", ".join(vals.keys())
        phs = ", ".join(["?"] * len(vals))
        try:
            conn.execute(f"INSERT INTO {rel_table} ({cols}) VALUES ({phs})", list(vals.values()))
            rel_count += 1
        except Exception as e:
            pass

    print(f"  Relations: {rel_count}")

    # 5. Import concept-researcher links
    cr_links = data.get("concept_researchers", [])
    cr_count = 0
    cr_table = f"{table}_researchers"
    for item in cr_links:
        cid = name_to_id.get(item.get("concept_name")) or item.get("concept_id")
        rid = researcher_name_to_id.get(item.get("researcher_name")) or item.get("researcher_id")
        if not cid or not rid:
            continue
        try:
            conn.execute(
                f"INSERT OR IGNORE INTO {cr_table} (concept_id, researcher_id, role, year_associated, note) VALUES (?, ?, ?, ?, ?)",
                (cid, rid, item.get("role", "originator"), item.get("year_associated"), item.get("note"))
            )
            cr_count += 1
        except:
            pass

    print(f"  Concept-Researcher links: {cr_count}")

    # 6. Import concept-publication links
    cp_links = data.get("concept_publications", [])
    cp_count = 0
    cp_table = f"{table}_publications"
    for item in cp_links:
        cid = name_to_id.get(item.get("concept_name")) or item.get("concept_id")
        pid = pub_title_to_id.get(item.get("publication_title")) or item.get("publication_id")
        if not cid or not pid:
            continue
        try:
            conn.execute(
                f"INSERT OR IGNORE INTO {cp_table} (concept_id, publication_id, relevance_type, is_primary, note) VALUES (?, ?, ?, ?, ?)",
                (cid, pid, item.get("relevance_type", "founding"), item.get("is_primary", 1), item.get("note"))
            )
            cp_count += 1
        except:
            pass

    print(f"  Concept-Publication links: {cp_count}")

    conn.commit()
    conn.close()
    print("  Done.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_v3.py <file.json> [file2.json ...]")
        sys.exit(1)
    for f in sys.argv[1:]:
        import_file(f)
