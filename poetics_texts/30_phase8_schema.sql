-- Phase 8: 概念-原著の構造化リンクテーブル
-- Adds quality layer: founding source quotes for concepts

CREATE TABLE IF NOT EXISTS concept_original_source (
    id TEXT PRIMARY KEY,
    concept_id TEXT NOT NULL,                  -- FK to humanities_concept
    source_type TEXT,                          -- "founding_text" | "key_discussion" | "later_elaboration" | "critique" | "primary_example"
    source_work_title TEXT,                    -- e.g. "Aristotle Poetics"
    source_locator TEXT,                       -- e.g. "1449b25-28" or "Book III Ch.6"
    source_year INTEGER,                       -- approximate composition year
    source_author TEXT,                        -- author of the source
    source_language TEXT,                      -- ISO 639-3
    quote_original TEXT NOT NULL,              -- original-language quote 2-8 lines
    quote_japanese TEXT,                       -- Japanese translation
    quote_english TEXT,                        -- English translation
    quote_significance TEXT,                   -- 100-300 chars: why this quote founds/defines the concept
    related_text_id TEXT,                      -- optional FK to poetics_text (when source is also a poetic text)
    source_url TEXT,                           -- URL to PD archive
    source_archive TEXT,
    public_domain_status TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (concept_id) REFERENCES humanities_concept(id),
    FOREIGN KEY (related_text_id) REFERENCES poetics_text(id)
);

CREATE INDEX IF NOT EXISTS idx_cos_concept ON concept_original_source(concept_id);
CREATE INDEX IF NOT EXISTS idx_cos_type ON concept_original_source(source_type);
CREATE INDEX IF NOT EXISTS idx_cos_text ON concept_original_source(related_text_id);
CREATE INDEX IF NOT EXISTS idx_cos_author ON concept_original_source(source_author);
