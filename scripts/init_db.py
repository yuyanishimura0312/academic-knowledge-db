#!/usr/bin/env python3
"""
Initialize the academic knowledge database.
Creates all tables based on the v2 schema design.
"""

import sqlite3
import os
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "academic.db"


def init_db():
    """Create all tables for the academic knowledge database."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # ── Shared: researcher ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS researcher (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        birth_year INTEGER,
        death_year INTEGER,
        nationality TEXT,
        primary_domain TEXT CHECK(primary_domain IN
            ('humanities','social_sciences','natural_sciences','engineering','arts')),
        affiliated_institutions TEXT,  -- JSON array
        overall_research_theme TEXT,
        bio_summary TEXT,
        h_index INTEGER,
        notable_awards TEXT,  -- JSON array
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Shared: publication ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS publication (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        title_en TEXT,
        publication_type TEXT CHECK(publication_type IN
            ('journal_article','book','chapter','conference_paper',
             'patent','artwork','performance','exhibition','standard','report')),
        year INTEGER,
        venue TEXT,
        doi TEXT,
        isbn TEXT,
        url TEXT,
        abstract TEXT,
        summary TEXT,
        citation_count INTEGER,
        domain TEXT CHECK(domain IN
            ('humanities','social_sciences','natural_sciences','engineering','arts')),
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain 1: humanities_concept ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS humanities_concept (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        description TEXT,
        description_detailed TEXT,
        impact TEXT,
        year_proposed INTEGER,
        year_range TEXT,
        geographic_origin TEXT,
        status TEXT CHECK(status IN ('active','dormant','reinterpreted','contested')),
        paradigm_school TEXT,
        keywords TEXT,  -- JSON array
        source_reliability TEXT CHECK(source_reliability IN ('primary','secondary','tertiary')),
        blind_spot_addressed TEXT,
        reinterpretation_history TEXT,
        cultural_context TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS humanities_concept_relation (
        id TEXT PRIMARY KEY,
        source_id TEXT NOT NULL REFERENCES humanities_concept(id),
        target_id TEXT NOT NULL REFERENCES humanities_concept(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('derived_from','critiques','reinterprets','extends','opposes','synthesizes')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain 2: social_theory ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS social_theory (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        description TEXT,
        description_detailed TEXT,
        impact TEXT,
        year_proposed INTEGER,
        year_range TEXT,
        geographic_origin TEXT,
        status TEXT CHECK(status IN ('active','dormant','incorporated','abandoned','contested')),
        paradigm_school TEXT,
        keywords TEXT,  -- JSON array
        source_reliability TEXT CHECK(source_reliability IN ('primary','secondary','tertiary')),
        predictive_power TEXT,
        operationalization TEXT,
        empirical_support TEXT CHECK(empirical_support IN
            ('supported','partially_supported','contested','refuted')),
        policy_implications TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS social_theory_relation (
        id TEXT PRIMARY KEY,
        source_id TEXT NOT NULL REFERENCES social_theory(id),
        target_id TEXT NOT NULL REFERENCES social_theory(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('derived_from','critiques','extends','empirically_tests',
             'synthesizes','competes_with','applies_to_policy')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain 3: natural_discovery ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS natural_discovery (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        description TEXT,
        description_detailed TEXT,
        impact TEXT,
        year_proposed INTEGER,
        year_range TEXT,
        geographic_origin TEXT,
        status TEXT CHECK(status IN
            ('established','partially_confirmed','hypothetical','refuted','superseded')),
        paradigm_school TEXT,
        keywords TEXT,  -- JSON array
        source_reliability TEXT CHECK(source_reliability IN ('primary','secondary','tertiary')),
        mathematical_formulation TEXT,
        experimental_verification TEXT,
        applicable_scale TEXT,
        precision_level TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS natural_discovery_relation (
        id TEXT PRIMARY KEY,
        source_id TEXT NOT NULL REFERENCES natural_discovery(id),
        target_id TEXT NOT NULL REFERENCES natural_discovery(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('derived_from','generalizes','experimentally_confirms',
             'contradicts','supersedes','enables')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain 4: engineering_method ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS engineering_method (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        description TEXT,
        description_detailed TEXT,
        impact TEXT,
        year_proposed INTEGER,
        year_range TEXT,
        geographic_origin TEXT,
        status TEXT CHECK(status IN ('active','mature','declining','obsolete','superseded')),
        paradigm_school TEXT,
        keywords TEXT,  -- JSON array
        source_reliability TEXT CHECK(source_reliability IN ('primary','secondary','tertiary')),
        technology_readiness_level INTEGER CHECK(
            technology_readiness_level BETWEEN 1 AND 9),
        related_patents TEXT,  -- JSON array
        industry_applications TEXT,
        problem_type TEXT,
        scientific_basis TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS engineering_method_relation (
        id TEXT PRIMARY KEY,
        source_id TEXT NOT NULL REFERENCES engineering_method(id),
        target_id TEXT NOT NULL REFERENCES engineering_method(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('derived_from','improves','supersedes','combines',
             'based_on','standardizes')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Domain 5: arts_question ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS arts_question (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        name_en TEXT,
        name_original TEXT,
        description TEXT,
        description_detailed TEXT,
        impact TEXT,
        year_proposed INTEGER,
        year_range TEXT,
        geographic_origin TEXT,
        status TEXT CHECK(status IN ('active','dormant','revived','absorbed','contested')),
        paradigm_school TEXT,
        keywords TEXT,  -- JSON array
        source_reliability TEXT CHECK(source_reliability IN ('primary','secondary','tertiary')),
        target_assumption TEXT,
        medium TEXT,
        representative_works TEXT,  -- JSON array
        movement_affiliation TEXT,
        sensory_dimension TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS arts_question_relation (
        id TEXT PRIMARY KEY,
        source_id TEXT NOT NULL REFERENCES arts_question(id),
        target_id TEXT NOT NULL REFERENCES arts_question(id),
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('derived_from','deepens','counters','translates_medium',
             'revives','inspires')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Bridge tables: entity <-> researcher ──
    for domain, table in [
        ('humanities', 'humanities_concept'),
        ('social_sciences', 'social_theory'),
        ('natural_sciences', 'natural_discovery'),
        ('engineering', 'engineering_method'),
        ('arts', 'arts_question'),
    ]:
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}_researcher_link (
            id TEXT PRIMARY KEY,
            entity_id TEXT NOT NULL REFERENCES {table}(id),
            researcher_id TEXT NOT NULL REFERENCES researcher(id),
            role TEXT CHECK(role IN
                ('originator','co_creator','major_contributor',
                 'critic','reinterpreter','popularizer')),
            contribution_description TEXT,
            year INTEGER,
            created_at TEXT DEFAULT (datetime('now'))
        )
        """)

    # ── Bridge tables: entity <-> publication ──
    for domain, table in [
        ('humanities', 'humanities_concept'),
        ('social_sciences', 'social_theory'),
        ('natural_sciences', 'natural_discovery'),
        ('engineering', 'engineering_method'),
        ('arts', 'arts_question'),
    ]:
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table}_publication_link (
            id TEXT PRIMARY KEY,
            entity_id TEXT NOT NULL REFERENCES {table}(id),
            publication_id TEXT NOT NULL REFERENCES publication(id),
            role TEXT CHECK(role IN
                ('founding_work','major_elaboration','empirical_test',
                 'critique','review','application')),
            is_primary INTEGER DEFAULT 0,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )
        """)

    # ── researcher <-> publication ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS researcher_publication (
        id TEXT PRIMARY KEY,
        researcher_id TEXT NOT NULL REFERENCES researcher(id),
        publication_id TEXT NOT NULL REFERENCES publication(id),
        role TEXT CHECK(role IN ('author','editor','translator','artist','performer')),
        position INTEGER,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Cross-domain relation ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS cross_domain_relation (
        id TEXT PRIMARY KEY,
        source_domain TEXT NOT NULL CHECK(source_domain IN
            ('humanities','social_sciences','natural_sciences','engineering','arts')),
        source_id TEXT NOT NULL,
        target_domain TEXT NOT NULL CHECK(target_domain IN
            ('humanities','social_sciences','natural_sciences','engineering','arts')),
        target_id TEXT NOT NULL,
        relation_type TEXT NOT NULL CHECK(relation_type IN
            ('transfers_concept','applies','inspires','reframes','enables')),
        description TEXT,
        evidence_source TEXT,
        year INTEGER,
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Survey frame ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS survey_frame (
        id TEXT PRIMARY KEY,
        domain TEXT NOT NULL CHECK(domain IN
            ('humanities','social_sciences','natural_sciences','engineering','arts')),
        level INTEGER NOT NULL CHECK(level BETWEEN 1 AND 3),
        parent_id TEXT REFERENCES survey_frame(id),
        name TEXT NOT NULL,
        name_en TEXT,
        description TEXT,
        estimated_unit_count INTEGER,
        survey_status TEXT DEFAULT 'not_started' CHECK(survey_status IN
            ('not_started','in_progress','completed','needs_review')),
        survey_priority INTEGER CHECK(survey_priority BETWEEN 1 AND 5),
        key_references TEXT,  -- JSON array
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ── Data provenance ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS data_provenance (
        id TEXT PRIMARY KEY,
        entity_domain TEXT NOT NULL,
        entity_id TEXT NOT NULL,
        source_type TEXT CHECK(source_type IN
            ('academic_paper','book','encyclopedia','database',
             'expert_review','ai_generated')),
        source_reference TEXT,
        confidence_level TEXT CHECK(confidence_level IN ('high','medium','low')),
        verified_by TEXT,
        verified_at TEXT,
        notes TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )
    """)

    # ��─ Indexes for performance ──
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_hc_name ON humanities_concept(name)",
        "CREATE INDEX IF NOT EXISTS idx_hc_status ON humanities_concept(status)",
        "CREATE INDEX IF NOT EXISTS idx_hc_year ON humanities_concept(year_proposed)",
        "CREATE INDEX IF NOT EXISTS idx_st_name ON social_theory(name)",
        "CREATE INDEX IF NOT EXISTS idx_st_status ON social_theory(status)",
        "CREATE INDEX IF NOT EXISTS idx_nd_name ON natural_discovery(name)",
        "CREATE INDEX IF NOT EXISTS idx_nd_status ON natural_discovery(status)",
        "CREATE INDEX IF NOT EXISTS idx_em_name ON engineering_method(name)",
        "CREATE INDEX IF NOT EXISTS idx_em_status ON engineering_method(status)",
        "CREATE INDEX IF NOT EXISTS idx_aq_name ON arts_question(name)",
        "CREATE INDEX IF NOT EXISTS idx_aq_status ON arts_question(status)",
        "CREATE INDEX IF NOT EXISTS idx_researcher_name ON researcher(name)",
        "CREATE INDEX IF NOT EXISTS idx_researcher_domain ON researcher(primary_domain)",
        "CREATE INDEX IF NOT EXISTS idx_pub_year ON publication(year)",
        "CREATE INDEX IF NOT EXISTS idx_pub_domain ON publication(domain)",
        "CREATE INDEX IF NOT EXISTS idx_sf_domain ON survey_frame(domain)",
        "CREATE INDEX IF NOT EXISTS idx_sf_status ON survey_frame(survey_status)",
        "CREATE INDEX IF NOT EXISTS idx_cdr_source ON cross_domain_relation(source_domain, source_id)",
        "CREATE INDEX IF NOT EXISTS idx_cdr_target ON cross_domain_relation(target_domain, target_id)",
    ]
    for idx in indexes:
        c.execute(idx)

    # ── FTS5 full-text search ──
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS fts_search USING fts5(
        entity_type, entity_id, name, name_en, description, keywords,
        content='', contentless_delete=1
    )
    """)

    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_PATH}")
    print(f"Tables created: 5 domain tables + 5 relation tables + "
          f"10 researcher links + 10 publication links + "
          f"shared tables + FTS index")


def show_schema():
    """Print the current database schema."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','index') ORDER BY type, name")
    rows = c.fetchall()
    conn.close()

    tables = [r for r in rows if r[1] == 'table']
    indexes = [r for r in rows if r[1] == 'index']
    print(f"\nTables ({len(tables)}):")
    for name, _ in tables:
        print(f"  - {name}")
    print(f"\nIndexes ({len(indexes)}):")
    for name, _ in indexes:
        print(f"  - {name}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "schema":
        show_schema()
    else:
        init_db()
        show_schema()
