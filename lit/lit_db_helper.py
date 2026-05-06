"""
LIT-DB Phase 2 Insertion Helper

Provides database connection, validated insertion functions, duplicate detection,
and analytics queries for Codex 20 contributors during Phase 2 collection.

Usage:
    from lit_db_helper import LitDB

    db = LitDB()  # opens lit.sqlite next to this file
    cid = db.insert_concept(
        name_ja='異化', name_en='defamiliarization',
        name_original='остранение', original_script='cyrillic',
        subfield_code='lit_theory', region='ロシア',
        definition='...', source_tier='primary',
        importance_score=5, primary_source_url='https://...'
    )
    db.tag_fourth_transform(cid, axis='創造性', status='rethinking',
                            rationale='...', related_ai_phenomenon='LLM creativity debates')

Designed to be imported by all 20 Codex during Phase 2.
"""

from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import Iterable, Optional


DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")


VALID_SOURCE_TIERS = {"primary", "secondary", "tertiary"}
VALID_CANONICAL = {"core", "major", "minor", "marginal"}
VALID_FOURTH_STATUS = {"rethinking", "partial", "invariant"}
VALID_FOURTH_AXES = {
    "作者性", "創造性", "物語", "主体", "正典",
    "受容", "翻訳", "真正性", "言語",
}
VALID_ENTITY_TYPES = {"concept", "author", "work", "movement"}
VALID_TARGET_DBS = {"PHIL", "PT", "AN", "MG", "Era-Talents", "SI",
                    "Innovation", "AI-Development", "Cultural-Intelligence",
                    "Myth-Narratives"}


class LitDBError(Exception):
    """Base exception for LitDB validation/operation failures."""


def _validate_choice(value: Optional[str], choices: set, field: str,
                     allow_none: bool = False) -> None:
    if value is None:
        if allow_none:
            return
        raise LitDBError(f"{field} must not be None")
    if value not in choices:
        raise LitDBError(
            f"{field}={value!r} is not in allowed set {sorted(choices)}"
        )


def _validate_score(value: Optional[int], field: str, lo: int = 1, hi: int = 5,
                    allow_none: bool = False) -> None:
    if value is None:
        if allow_none:
            return
        raise LitDBError(f"{field} must not be None")
    if not isinstance(value, int) or value < lo or value > hi:
        raise LitDBError(f"{field}={value} must be int in [{lo},{hi}]")


class LitDB:
    """High-level helper around lit.sqlite for Phase 2 collection."""

    def __init__(self, db_path: str = DEFAULT_DB_PATH) -> None:
        self.db_path = db_path
        if not os.path.exists(db_path):
            raise LitDBError(f"DB not found: {db_path}")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._subfield_cache: dict[str, int] = {}
        self._period_cache: dict[tuple[str, str], int] = {}

    # ------------------------------------------------------------
    # Context management
    # ------------------------------------------------------------

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "LitDB":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.close()

    @contextmanager
    def transaction(self):
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    # ------------------------------------------------------------
    # Lookup helpers
    # ------------------------------------------------------------

    def subfield_id(self, code: str) -> int:
        if code in self._subfield_cache:
            return self._subfield_cache[code]
        row = self.conn.execute(
            "SELECT id FROM subfields WHERE code = ?", (code,)
        ).fetchone()
        if not row:
            raise LitDBError(f"unknown subfield code: {code}")
        self._subfield_cache[code] = row["id"]
        return row["id"]

    def get_or_create_period(self, name_ja: str, region: str,
                             start_year: Optional[int] = None,
                             end_year: Optional[int] = None,
                             name_en: Optional[str] = None,
                             description: Optional[str] = None) -> int:
        key = (name_ja, region)
        if key in self._period_cache:
            return self._period_cache[key]
        row = self.conn.execute(
            "SELECT id FROM periods WHERE name_ja = ? AND region = ?",
            (name_ja, region),
        ).fetchone()
        if row:
            self._period_cache[key] = row["id"]
            return row["id"]
        cur = self.conn.execute(
            """INSERT INTO periods(name_ja, name_en, region, start_year, end_year, description)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (name_ja, name_en, region, start_year, end_year, description),
        )
        pid = cur.lastrowid
        self._period_cache[key] = pid
        return pid

    # ------------------------------------------------------------
    # Duplicate detection
    # ------------------------------------------------------------

    def find_concept(self, name_ja: str, region: str,
                     period_id: Optional[int]) -> Optional[int]:
        row = self.conn.execute(
            """SELECT id FROM concepts
               WHERE name_ja = ? AND region = ?
                 AND ((period_id IS NULL AND ? IS NULL) OR period_id = ?)""",
            (name_ja, region, period_id, period_id),
        ).fetchone()
        return row["id"] if row else None

    def find_author(self, name_ja: str, birth_year: Optional[int]) -> Optional[int]:
        row = self.conn.execute(
            """SELECT id FROM authors
               WHERE name_ja = ?
                 AND ((birth_year IS NULL AND ? IS NULL) OR birth_year = ?)""",
            (name_ja, birth_year, birth_year),
        ).fetchone()
        return row["id"] if row else None

    def find_movement(self, name_ja: str, region: str) -> Optional[int]:
        row = self.conn.execute(
            "SELECT id FROM movements WHERE name_ja = ? AND region = ?",
            (name_ja, region),
        ).fetchone()
        return row["id"] if row else None

    # ------------------------------------------------------------
    # concepts
    # ------------------------------------------------------------

    def insert_concept(
        self,
        *,
        name_ja: str,
        subfield_code: str,
        region: str,
        definition: str,
        name_en: Optional[str] = None,
        name_original: Optional[str] = None,
        original_script: Optional[str] = None,
        period_id: Optional[int] = None,
        background: Optional[str] = None,
        development: Optional[str] = None,
        historical_context: Optional[str] = None,
        primary_source_url: Optional[str] = None,
        primary_source_type: Optional[str] = None,
        importance_score: int = 3,
        fourth_transform_status: Optional[str] = None,
        fourth_transform_note: Optional[str] = None,
        source_tier: Optional[str] = None,
        canonical_in_region: Optional[str] = None,
        skip_duplicates: bool = True,
    ) -> int:
        """Insert a concept with full validation. Returns new or existing id."""
        if not name_ja:
            raise LitDBError("name_ja is required")
        if not definition:
            raise LitDBError("definition is required")
        _validate_score(importance_score, "importance_score")
        _validate_choice(fourth_transform_status, VALID_FOURTH_STATUS,
                         "fourth_transform_status", allow_none=True)
        _validate_choice(source_tier, VALID_SOURCE_TIERS,
                         "source_tier", allow_none=True)
        _validate_choice(canonical_in_region, VALID_CANONICAL,
                         "canonical_in_region", allow_none=True)
        # Tier 3 entries should not have importance >= 4 without explicit
        # justification — flag this for downstream verification.
        if source_tier == "tertiary" and importance_score >= 4:
            # Soft warning; we still insert but note it.
            print(f"[warn] tertiary source with high importance for {name_ja!r}")

        sf_id = self.subfield_id(subfield_code)

        existing = self.find_concept(name_ja, region, period_id)
        if existing and skip_duplicates:
            print(f"[skip] concept exists: {name_ja!r} (id={existing})")
            return existing

        cur = self.conn.execute(
            """INSERT INTO concepts(
                name_ja, name_en, name_original, original_script,
                subfield_id, region, period_id,
                definition, background, development, historical_context,
                primary_source_url, primary_source_type,
                importance_score, fourth_transform_status, fourth_transform_note,
                source_tier, canonical_in_region
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                name_ja, name_en, name_original, original_script,
                sf_id, region, period_id,
                definition, background, development, historical_context,
                primary_source_url, primary_source_type,
                importance_score, fourth_transform_status, fourth_transform_note,
                source_tier, canonical_in_region,
            ),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # authors
    # ------------------------------------------------------------

    def insert_author(
        self,
        *,
        name_ja: str,
        region: str,
        name_en: Optional[str] = None,
        name_original: Optional[str] = None,
        birth_year: Optional[int] = None,
        death_year: Optional[int] = None,
        nationality: Optional[str] = None,
        primary_language: Optional[str] = None,
        period_id: Optional[int] = None,
        biography: Optional[str] = None,
        contributions: Optional[str] = None,
        movements_belonged: Optional[str] = None,
        importance_score: int = 3,
        primary_source_url: Optional[str] = None,
        source_tier: Optional[str] = None,
        canonical_in_region: Optional[str] = None,
        skip_duplicates: bool = True,
    ) -> int:
        if not name_ja:
            raise LitDBError("name_ja is required")
        _validate_score(importance_score, "importance_score")
        _validate_choice(source_tier, VALID_SOURCE_TIERS, "source_tier",
                         allow_none=True)
        _validate_choice(canonical_in_region, VALID_CANONICAL,
                         "canonical_in_region", allow_none=True)

        existing = self.find_author(name_ja, birth_year)
        if existing and skip_duplicates:
            print(f"[skip] author exists: {name_ja!r} (id={existing})")
            return existing

        cur = self.conn.execute(
            """INSERT INTO authors(
                name_ja, name_en, name_original,
                birth_year, death_year,
                region, nationality, primary_language, period_id,
                biography, contributions, movements_belonged,
                importance_score, primary_source_url,
                source_tier, canonical_in_region
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                name_ja, name_en, name_original,
                birth_year, death_year,
                region, nationality, primary_language, period_id,
                biography, contributions, movements_belonged,
                importance_score, primary_source_url,
                source_tier, canonical_in_region,
            ),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # works
    # ------------------------------------------------------------

    def insert_work(
        self,
        *,
        title_ja: str,
        region: str,
        title_en: Optional[str] = None,
        title_original: Optional[str] = None,
        original_script: Optional[str] = None,
        author_id: Optional[int] = None,
        author_name_text: Optional[str] = None,
        publication_year: Optional[int] = None,
        period_id: Optional[int] = None,
        genre: Optional[str] = None,
        language: Optional[str] = None,
        summary: Optional[str] = None,
        significance: Optional[str] = None,
        influence_summary: Optional[str] = None,
        primary_source_url: Optional[str] = None,
        importance_score: int = 3,
        source_tier: Optional[str] = None,
        canonical_in_region: Optional[str] = None,
    ) -> int:
        if not title_ja:
            raise LitDBError("title_ja is required")
        _validate_score(importance_score, "importance_score")
        _validate_choice(source_tier, VALID_SOURCE_TIERS, "source_tier",
                         allow_none=True)
        _validate_choice(canonical_in_region, VALID_CANONICAL,
                         "canonical_in_region", allow_none=True)
        if author_id is None and not author_name_text:
            raise LitDBError("either author_id or author_name_text required")

        cur = self.conn.execute(
            """INSERT INTO works(
                title_ja, title_en, title_original, original_script,
                author_id, author_name_text,
                publication_year, period_id, region,
                genre, language, summary, significance, influence_summary,
                primary_source_url, importance_score,
                source_tier, canonical_in_region
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                title_ja, title_en, title_original, original_script,
                author_id, author_name_text,
                publication_year, period_id, region,
                genre, language, summary, significance, influence_summary,
                primary_source_url, importance_score,
                source_tier, canonical_in_region,
            ),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # movements
    # ------------------------------------------------------------

    def insert_movement(
        self,
        *,
        name_ja: str,
        region: str,
        name_en: Optional[str] = None,
        name_original: Optional[str] = None,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
        description: Optional[str] = None,
        key_principles: Optional[str] = None,
        historical_context: Optional[str] = None,
        legacy: Optional[str] = None,
        primary_source_url: Optional[str] = None,
        source_tier: Optional[str] = None,
        canonical_in_region: Optional[str] = None,
        skip_duplicates: bool = True,
    ) -> int:
        if not name_ja:
            raise LitDBError("name_ja is required")
        _validate_choice(source_tier, VALID_SOURCE_TIERS, "source_tier",
                         allow_none=True)
        _validate_choice(canonical_in_region, VALID_CANONICAL,
                         "canonical_in_region", allow_none=True)

        existing = self.find_movement(name_ja, region)
        if existing and skip_duplicates:
            print(f"[skip] movement exists: {name_ja!r} (id={existing})")
            return existing

        cur = self.conn.execute(
            """INSERT INTO movements(
                name_ja, name_en, name_original, region,
                start_year, end_year,
                description, key_principles, historical_context, legacy,
                primary_source_url, source_tier, canonical_in_region
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                name_ja, name_en, name_original, region,
                start_year, end_year,
                description, key_principles, historical_context, legacy,
                primary_source_url, source_tier, canonical_in_region,
            ),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # relations / geneal_links / cross_domain
    # ------------------------------------------------------------

    def insert_relation(
        self,
        *,
        source_type: str,
        source_id: int,
        target_type: str,
        target_id: int,
        relation_type: str,
        description: Optional[str] = None,
        bidirectional: bool = False,
        confidence: int = 3,
        source_evidence: Optional[str] = None,
    ) -> int:
        _validate_choice(source_type, VALID_ENTITY_TYPES, "source_type")
        _validate_choice(target_type, VALID_ENTITY_TYPES, "target_type")
        _validate_score(confidence, "confidence")
        cur = self.conn.execute(
            """INSERT INTO relations(
                source_type, source_id, target_type, target_id,
                relation_type, description, bidirectional, confidence,
                source_evidence
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                source_type, source_id, target_type, target_id,
                relation_type, description, 1 if bidirectional else 0,
                confidence, source_evidence,
            ),
        )
        return cur.lastrowid

    def insert_geneal_link(
        self,
        *,
        ancestor_concept_id: int,
        descendant_concept_id: int,
        transformation_type: Optional[str] = None,
        description: Optional[str] = None,
        transmission_path: Optional[str] = None,
    ) -> int:
        if ancestor_concept_id == descendant_concept_id:
            raise LitDBError("ancestor and descendant must differ")
        valid_types = {"extension", "inversion", "critique",
                       "translation", "syncretism"}
        if transformation_type and transformation_type not in valid_types:
            raise LitDBError(
                f"transformation_type must be one of {sorted(valid_types)}"
            )
        cur = self.conn.execute(
            """INSERT INTO geneal_links(
                ancestor_concept_id, descendant_concept_id,
                transformation_type, description, transmission_path
            ) VALUES (?, ?, ?, ?, ?)""",
            (
                ancestor_concept_id, descendant_concept_id,
                transformation_type, description, transmission_path,
            ),
        )
        return cur.lastrowid

    def insert_cross_domain(
        self,
        *,
        lit_entity_type: str,
        lit_entity_id: int,
        target_db: str,
        link_type: str,
        target_entity_id: Optional[str] = None,
        target_entity_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> int:
        _validate_choice(lit_entity_type, VALID_ENTITY_TYPES, "lit_entity_type")
        _validate_choice(target_db, VALID_TARGET_DBS, "target_db")
        valid_link = {"shared_concept", "borrowed_from", "parallel"}
        _validate_choice(link_type, valid_link, "link_type")
        cur = self.conn.execute(
            """INSERT INTO cross_domain(
                lit_entity_type, lit_entity_id, target_db,
                target_entity_id, target_entity_name, link_type, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                lit_entity_type, lit_entity_id, target_db,
                target_entity_id, target_entity_name, link_type, description,
            ),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # fourth_transform_tags
    # ------------------------------------------------------------

    def tag_fourth_transform(
        self,
        concept_id: int,
        *,
        axis: str,
        status: str,
        rationale: Optional[str] = None,
        related_ai_phenomenon: Optional[str] = None,
    ) -> int:
        _validate_choice(axis, VALID_FOURTH_AXES, "axis")
        _validate_choice(status, VALID_FOURTH_STATUS, "status")
        if status in ("rethinking", "partial"):
            if not rationale:
                raise LitDBError(
                    f"rationale required when status={status!r}"
                )
            if not related_ai_phenomenon:
                raise LitDBError(
                    f"related_ai_phenomenon required when status={status!r}"
                )
        cur = self.conn.execute(
            """INSERT OR REPLACE INTO fourth_transform_tags(
                concept_id, axis, status, rationale, related_ai_phenomenon
            ) VALUES (?, ?, ?, ?, ?)""",
            (concept_id, axis, status, rationale, related_ai_phenomenon),
        )
        return cur.lastrowid

    # ------------------------------------------------------------
    # Analytics
    # ------------------------------------------------------------

    def progress_summary(self) -> dict:
        """Return current row counts per table for STATUS.md updates."""
        out: dict[str, int] = {}
        for tbl in ("concepts", "authors", "works", "movements",
                    "relations", "geneal_links", "cross_domain",
                    "fourth_transform_tags", "periods", "subfields"):
            row = self.conn.execute(f"SELECT COUNT(*) AS c FROM {tbl}").fetchone()
            out[tbl] = row["c"]
        return out

    def fourth_transform_distribution(self) -> list[dict]:
        rows = self.conn.execute(
            """SELECT axis, status, COUNT(*) AS c
               FROM fourth_transform_tags
               GROUP BY axis, status
               ORDER BY axis, status"""
        ).fetchall()
        return [dict(r) for r in rows]

    def critical_concepts(self, min_axes: int = 3) -> list[dict]:
        """Concepts with `min_axes` or more 'rethinking' tags."""
        rows = self.conn.execute(
            """SELECT c.id, c.name_ja, c.name_en, c.region,
                      COUNT(t.axis) AS rethinking_axes
               FROM concepts c
               JOIN fourth_transform_tags t ON t.concept_id = c.id
               WHERE t.status = 'rethinking'
               GROUP BY c.id
               HAVING rethinking_axes >= ?
               ORDER BY rethinking_axes DESC, c.name_ja""",
            (min_axes,),
        ).fetchall()
        return [dict(r) for r in rows]

    def coverage_by_subfield(self) -> list[dict]:
        rows = self.conn.execute(
            """SELECT s.code, s.name_ja, s.target_concepts,
                      COUNT(c.id) AS current
               FROM subfields s
               LEFT JOIN concepts c ON c.subfield_id = s.id
               GROUP BY s.id
               ORDER BY s.id"""
        ).fetchall()
        return [dict(r) for r in rows]

    def tier_distribution(self) -> list[dict]:
        rows = self.conn.execute(
            """SELECT source_tier, COUNT(*) AS c
               FROM concepts
               GROUP BY source_tier
               ORDER BY c DESC"""
        ).fetchall()
        return [dict(r) for r in rows]


# ----------------------------------------------------------------
# CLI smoke test
# ----------------------------------------------------------------

def _smoke_test() -> None:
    """Run a basic insertion-rollback sanity check (no permanent writes)."""
    print("[lit_db_helper] smoke test starting...")
    with LitDB() as db:
        # Verify subfield lookups work for a sample of codes
        for code in ("lit_eu_classical", "lit_jp_classical", "lit_theory"):
            sid = db.subfield_id(code)
            print(f"  subfield {code!r} -> id={sid}")

        # Verify analytics queries run
        summary = db.progress_summary()
        print("  progress_summary:")
        for k, v in summary.items():
            print(f"    {k}: {v}")
        print(f"  source_tier distribution: {db.tier_distribution()}")
        print(f"  9-axis distribution: {db.fourth_transform_distribution()}")

        # Validation must reject invalid choices
        try:
            db.insert_concept(
                name_ja="_test_invalid_tier",
                subfield_code="lit_eu_classical",
                region="西欧",
                definition="(test)",
                source_tier="bogus",  # invalid
            )
        except LitDBError as e:
            print(f"  validation OK (rejected invalid source_tier): {e}")

        # Rollback any test data on exit by raising an exception inside ctx
        # but we explicitly want to avoid writing anything — the smoke test
        # never inserts, so no rollback is needed.
    print("[lit_db_helper] smoke test passed.")


if __name__ == "__main__":
    _smoke_test()
