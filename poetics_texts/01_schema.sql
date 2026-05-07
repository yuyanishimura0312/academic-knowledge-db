-- Poetics DB v2.0: poetics_text expansion schema
-- Adds primary text layer to existing humanities_concept (poetics) layer
-- Created: 2026-05-07

-- 1. Primary text table
CREATE TABLE IF NOT EXISTS poetics_text (
    id TEXT PRIMARY KEY,
    title_original TEXT,           -- e.g. "Ἰλιάς", "詩經"
    title_ja TEXT NOT NULL,        -- e.g. "イーリアス"
    title_en TEXT,                 -- e.g. "Iliad"
    author_id TEXT,                -- FK to researchers (poet) when known
    author_name_display TEXT,      -- displayable form when no FK match
    era_year INTEGER,              -- approximate composition year (negative = BCE)
    era_period TEXT,               -- e.g. "古代ギリシャ", "盛唐", "ロマン派"
    culture_region TEXT NOT NULL,  -- one of: 古代ギリシャ・ローマ, 中国古典, 日本古典, アラビア・ペルシア, サンスクリット, 中世ヨーロッパ, 近代ヨーロッパ, 20-21世紀グローバル, アフリカ, 先住民・口承, 仏典詩偈
    language_original TEXT,        -- ISO 639-3 or descriptive (grc, lat, zho, jpn, ara, fas, san, en, fr, de, etc.)
    form_genre TEXT,               -- 叙事詩, 抒情詩, ソネット, ガザル, 俳諧, 短歌, 漢詩, 散文詩, 詩劇, 口承詩, etc.
    meter_prosody TEXT,            -- ヘクサメトロス, アレクサンドラン, 五七五, 七言絶句, etc.
    length_lines INTEGER,
    full_text_or_excerpt TEXT,     -- the actual text (PD or fair-use excerpt)
    excerpt_note TEXT,             -- describes which part if excerpt
    public_domain_status TEXT,     -- "PD-original", "PD-via-translation-only", "fair-use-excerpt", "CC-licensed"
    source_url TEXT,
    source_archive TEXT,           -- "Perseus", "Gutenberg", "青空文庫", "GRETIL", "CBETA", etc.
    license TEXT,
    canonical_tier INTEGER,        -- 1=正典級, 2=理論連結, 3=多文化補完
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES researchers(id)
);

-- 2. Translations
CREATE TABLE IF NOT EXISTS poetics_text_translation (
    id TEXT PRIMARY KEY,
    text_id TEXT NOT NULL,
    translator_name TEXT,
    translator_year INTEGER,
    language TEXT NOT NULL,        -- ISO 639-3
    translation_text TEXT,
    translation_type TEXT,         -- "literal", "poetic", "scholarly", "summary"
    source_url TEXT,
    license TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (text_id) REFERENCES poetics_text(id)
);

-- 3. Concept-text linkage (theory <-> example)
CREATE TABLE IF NOT EXISTS poetics_text_concept_link (
    id TEXT PRIMARY KEY,
    text_id TEXT NOT NULL,
    concept_id TEXT NOT NULL,      -- FK to humanities_concept
    link_type TEXT,                -- "例証", "批判対象", "分析対象", "影響源", "由来"
    discussed_by_researcher_id TEXT, -- FK to researchers
    discussion_locus TEXT,         -- e.g. "Aristotle Poetics 6.1450a", "Shklovsky Theory of Prose ch.1"
    strength INTEGER DEFAULT 5,    -- 1-10
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (text_id) REFERENCES poetics_text(id),
    FOREIGN KEY (concept_id) REFERENCES humanities_concept(id),
    FOREIGN KEY (discussed_by_researcher_id) REFERENCES researchers(id)
);

-- 4. Motifs / themes
CREATE TABLE IF NOT EXISTS poetics_text_motif (
    id TEXT PRIMARY KEY,
    text_id TEXT NOT NULL,
    motif_label TEXT NOT NULL,
    motif_category TEXT,           -- 愛, 死, 戦争, 季節, 神話, 政治, 自然, 都市, 旅, 宗教, アイデンティティ, etc.
    tradition_specific TEXT,       -- e.g. "和歌における月" specific to one tradition
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (text_id) REFERENCES poetics_text(id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_pt_text_culture ON poetics_text(culture_region);
CREATE INDEX IF NOT EXISTS idx_pt_text_era ON poetics_text(era_period);
CREATE INDEX IF NOT EXISTS idx_pt_text_form ON poetics_text(form_genre);
CREATE INDEX IF NOT EXISTS idx_pt_text_tier ON poetics_text(canonical_tier);
CREATE INDEX IF NOT EXISTS idx_pt_text_author ON poetics_text(author_id);
CREATE INDEX IF NOT EXISTS idx_pt_trans_text ON poetics_text_translation(text_id);
CREATE INDEX IF NOT EXISTS idx_pt_trans_lang ON poetics_text_translation(language);
CREATE INDEX IF NOT EXISTS idx_pt_link_text ON poetics_text_concept_link(text_id);
CREATE INDEX IF NOT EXISTS idx_pt_link_concept ON poetics_text_concept_link(concept_id);
CREATE INDEX IF NOT EXISTS idx_pt_link_researcher ON poetics_text_concept_link(discussed_by_researcher_id);
CREATE INDEX IF NOT EXISTS idx_pt_motif_text ON poetics_text_motif(text_id);
CREATE INDEX IF NOT EXISTS idx_pt_motif_label ON poetics_text_motif(motif_label);
CREATE INDEX IF NOT EXISTS idx_pt_motif_category ON poetics_text_motif(motif_category);
