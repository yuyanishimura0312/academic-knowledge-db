-- Phase 9-B: 概念-詩文-原著引用 三項リンクテーブル
-- Models the full triangle: a concept is theorized via an original-source quote,
-- and instantiated/exemplified by a primary poetic text.

CREATE TABLE IF NOT EXISTS concept_text_source_triple (
    id TEXT PRIMARY KEY,
    concept_id TEXT NOT NULL,           -- FK humanities_concept
    text_id TEXT NOT NULL,              -- FK poetics_text (the example)
    source_id TEXT,                     -- FK concept_original_source (the founding theory passage)
    triple_type TEXT,                   -- "theory_example" | "critique_example" | "transmission" | "self_referential"
    relationship_note TEXT,             -- 100-300 chars: how the theory in the source applies to/is exemplified by this text
    confidence INTEGER DEFAULT 7,       -- 1-10 confidence score
    discussion_locator TEXT,            -- e.g. "Aristotle Poetics 11.1452a discusses Sophocles OT for peripeteia"
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (concept_id) REFERENCES humanities_concept(id),
    FOREIGN KEY (text_id) REFERENCES poetics_text(id),
    FOREIGN KEY (source_id) REFERENCES concept_original_source(id)
);

CREATE INDEX IF NOT EXISTS idx_triple_concept ON concept_text_source_triple(concept_id);
CREATE INDEX IF NOT EXISTS idx_triple_text ON concept_text_source_triple(text_id);
CREATE INDEX IF NOT EXISTS idx_triple_source ON concept_text_source_triple(source_id);
CREATE INDEX IF NOT EXISTS idx_triple_type ON concept_text_source_triple(triple_type);

-- View: triple display
CREATE VIEW IF NOT EXISTS v_concept_full_triple AS
SELECT
    hc.id AS concept_id,
    hc.name_ja AS concept_name,
    hc.subfield,
    cos.source_work_title,
    cos.source_locator,
    substr(cos.quote_original, 1, 100) AS quote_snip,
    pt.id AS text_id,
    pt.title_ja AS text_title,
    pt.author_name_display AS text_author,
    pt.culture_region,
    ctst.triple_type,
    ctst.relationship_note,
    ctst.confidence
FROM concept_text_source_triple ctst
JOIN humanities_concept hc ON ctst.concept_id = hc.id
JOIN poetics_text pt ON ctst.text_id = pt.id
LEFT JOIN concept_original_source cos ON ctst.source_id = cos.id;
