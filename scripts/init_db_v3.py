#!/usr/bin/env python3
"""
Initialize academic knowledge database v3.
Aligned with anthropology-concepts DB schema for consistency.
Supports domain-specific concept tables with shared researcher/publication tables.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"

DOMAIN_CONFIGS = {
    "humanities": {
        "table": "humanities_concept",
        "specific_fields": """
            blind_spot_addressed TEXT,
            reinterpretation_history TEXT,
            cultural_context TEXT
        """,
        "relation_types": "('derived_from','critiques','reinterprets','extends','opposes','synthesizes','complements','related_to')",
    },
    "social_sciences": {
        "table": "social_theory",
        "specific_fields": """
            predictive_power TEXT,
            operationalization TEXT,
            empirical_support TEXT,
            policy_implications TEXT
        """,
        "relation_types": "('derived_from','critiques','extends','empirically_tests','synthesizes','competes_with','applies_to_policy','complements','related_to','influenced')",
    },
    "natural_sciences": {
        "table": "natural_discovery",
        "specific_fields": """
            mathematical_formulation TEXT,
            experimental_verification TEXT,
            applicable_scale TEXT,
            precision_level TEXT
        """,
        "relation_types": "('derived_from','generalizes','experimentally_confirms','contradicts','supersedes','enables','complements','related_to')",
    },
    "engineering": {
        "table": "engineering_method",
        "specific_fields": """
            technology_readiness_level INTEGER,
            related_patents TEXT,
            industry_applications TEXT,
            problem_type TEXT,
            scientific_basis TEXT
        """,
        "relation_types": "('derived_from','improves','supersedes','combines','based_on','standardizes','complements','related_to')",
    },
    "arts": {
        "table": "arts_question",
        "specific_fields": """
            target_assumption TEXT,
            medium TEXT,
            representative_works TEXT,
            movement_affiliation TEXT,
            sensory_dimension TEXT
        """,
        "relation_types": "('derived_from','deepens','counters','translates_medium','revives','inspires','complements','related_to')",
    },
}

# Common fields shared by all domain tables (aligned with anthropology DB)
COMMON_FIELDS = """
    id TEXT PRIMARY KEY,
    name_ja TEXT NOT NULL,
    name_en TEXT,
    name_original TEXT,
    definition TEXT,
    impact_summary TEXT,
    subfield TEXT,
    school_of_thought TEXT,
    era_start INTEGER,
    era_end INTEGER,
    methodology_level TEXT,
    target_domain TEXT,
    application_conditions TEXT,
    when_to_apply TEXT,
    framing_questions TEXT,
    opposing_concept_names TEXT,
    keywords_ja TEXT,
    keywords_en TEXT,
    status TEXT DEFAULT 'active',
    source_reliability TEXT DEFAULT 'secondary',
    data_completeness INTEGER DEFAULT 70,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
"""


def init_db(reset=False):
    if reset and DB_PATH.exists():
        DB_PATH.unlink()
        print(f"Deleted existing database: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # ── Shared: researchers (aligned with anthropology DB) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS researchers (
        id TEXT PRIMARY KEY,
        name_full TEXT NOT NULL,
        name_ja TEXT,
        birth_year INTEGER,
        death_year INTEGER,
        nationality TEXT,
        primary_institution TEXT,
        research_themes TEXT,
        biography_brief TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Shared: publications (aligned with anthropology DB) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS publications (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        title_ja TEXT,
        pub_year INTEGER,
        pub_venue TEXT,
        pub_type TEXT,
        abstract_summary TEXT,
        doi_or_isbn TEXT,
        url TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain tables ──
    for domain, config in DOMAIN_CONFIGS.items():
        table = config["table"]

        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            {COMMON_FIELDS},
            {config['specific_fields']}
        )
        """)

        # Concept relations (aligned with anthropology DB)
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}_relations (
            id TEXT PRIMARY KEY,
            source_concept_id TEXT NOT NULL REFERENCES {table}(id),
            target_concept_id TEXT NOT NULL REFERENCES {table}(id),
            relation_type TEXT NOT NULL,
            relation_description TEXT,
            evidence_publication_id TEXT REFERENCES publications(id),
            strength INTEGER DEFAULT 5,
            is_confirmed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT (datetime('now'))
        )
        """)

        # Concept-Researcher links (aligned with anthropology DB)
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}_researchers (
            concept_id TEXT NOT NULL REFERENCES {table}(id),
            researcher_id TEXT NOT NULL REFERENCES researchers(id),
            role TEXT,
            year_associated INTEGER,
            note TEXT,
            PRIMARY KEY (concept_id, researcher_id, role)
        )
        """)

        # Concept-Publication links (aligned with anthropology DB)
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}_publications (
            concept_id TEXT NOT NULL REFERENCES {table}(id),
            publication_id TEXT NOT NULL REFERENCES publications(id),
            relevance_type TEXT,
            is_primary INTEGER DEFAULT 0,
            note TEXT,
            PRIMARY KEY (concept_id, publication_id)
        )
        """)

    # ── Cross-domain relation ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS cross_domain_relations (
        id TEXT PRIMARY KEY,
        source_domain TEXT NOT NULL,
        source_id TEXT NOT NULL,
        target_domain TEXT NOT NULL,
        target_id TEXT NOT NULL,
        relation_type TEXT NOT NULL,
        relation_description TEXT,
        strength INTEGER DEFAULT 5,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Survey frame ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS survey_frame (
        id TEXT PRIMARY KEY,
        domain TEXT NOT NULL,
        level INTEGER NOT NULL,
        parent_id TEXT REFERENCES survey_frame(id),
        name TEXT NOT NULL,
        name_en TEXT,
        description TEXT,
        estimated_unit_count INTEGER,
        survey_status TEXT DEFAULT 'not_started',
        survey_priority INTEGER DEFAULT 3,
        key_references TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Indexes ──
    for domain, config in DOMAIN_CONFIGS.items():
        table = config["table"]
        c.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_name ON {table}(name_ja)")
        c.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_subfield ON {table}(subfield)")
        c.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_era ON {table}(era_start)")
        c.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_status ON {table}(status)")

    c.execute("CREATE INDEX IF NOT EXISTS idx_researchers_name ON researchers(name_full)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_publications_year ON publications(pub_year)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sf_domain ON survey_frame(domain)")

    conn.commit()

    # Report
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    print(f"Database initialized: {DB_PATH}")
    print(f"Tables: {len(tables)}")
    for t in tables:
        print(f"  - {t[0]}")

    conn.close()


if __name__ == "__main__":
    reset = "--reset" in sys.argv
    init_db(reset=reset)
