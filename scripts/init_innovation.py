#!/usr/bin/env python3
"""
Initialize innovation_theory tables in academic knowledge database.
Follows the same pattern as init_db_v3.py but adds innovation-specific fields.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"


def init_innovation_tables():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # Main innovation theory table
    c.execute("""
    CREATE TABLE IF NOT EXISTS innovation_theory (
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
        updated_at TEXT DEFAULT (datetime('now')),
        predictive_power TEXT,
        operationalization TEXT,
        empirical_support TEXT,
        policy_implications TEXT,
        innovation_type TEXT,
        schumpeter_layer TEXT,
        industry_applicability TEXT,
        cognitive_mechanism TEXT,
        key_researchers TEXT,
        key_works TEXT,
        measurement_approach TEXT
    )
    """)

    # Relations
    c.execute("""
    CREATE TABLE IF NOT EXISTS innovation_theory_relations (
        id TEXT PRIMARY KEY,
        source_concept_id TEXT NOT NULL REFERENCES innovation_theory(id),
        target_concept_id TEXT NOT NULL REFERENCES innovation_theory(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN (
            'derived_from','critiques','extends','empirically_tests',
            'synthesizes','competes_with','applies_to_policy',
            'complements','related_to','influenced'
        )),
        relation_description TEXT,
        evidence_publication_id TEXT REFERENCES publications(id),
        strength INTEGER DEFAULT 5,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # Researcher links (shared researchers table)
    c.execute("""
    CREATE TABLE IF NOT EXISTS innovation_theory_researchers (
        concept_id TEXT NOT NULL REFERENCES innovation_theory(id),
        researcher_id TEXT NOT NULL REFERENCES researchers(id),
        role TEXT DEFAULT 'contributor',
        PRIMARY KEY (concept_id, researcher_id)
    )
    """)

    # Publication links (shared publications table)
    c.execute("""
    CREATE TABLE IF NOT EXISTS innovation_theory_publications (
        concept_id TEXT NOT NULL REFERENCES innovation_theory(id),
        publication_id TEXT NOT NULL REFERENCES publications(id),
        relationship TEXT DEFAULT 'primary_source',
        PRIMARY KEY (concept_id, publication_id)
    )
    """)

    # Cross-domain connections to existing DBs
    c.execute("""
    CREATE TABLE IF NOT EXISTS innovation_cross_domain (
        id TEXT PRIMARY KEY,
        innovation_theory_id TEXT NOT NULL REFERENCES innovation_theory(id),
        target_db TEXT NOT NULL,
        target_table TEXT,
        target_id TEXT,
        connection_type TEXT,
        connection_description TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # Indexes
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_subfield ON innovation_theory(subfield)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_era ON innovation_theory(era_start)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_layer ON innovation_theory(schumpeter_layer)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_type ON innovation_theory(innovation_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_rel_src ON innovation_theory_relations(source_concept_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_rel_tgt ON innovation_theory_relations(target_concept_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_inno_cross_db ON innovation_cross_domain(target_db)")

    conn.commit()

    # Verify
    count = c.execute("SELECT COUNT(*) FROM innovation_theory").fetchone()[0]
    print(f"innovation_theory: {count} rows")
    print("All innovation tables initialized successfully.")

    conn.close()


if __name__ == "__main__":
    init_innovation_tables()
