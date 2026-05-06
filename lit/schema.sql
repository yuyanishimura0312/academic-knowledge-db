-- LIT-DB: 文学学術知識DB スキーマ v0.1
-- 2026-05-06 西村勇也承認版
-- 規模: 10K概念、3K作家、5K作品、500運動、30K関係

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- ========================================
-- 1. 概念テーブル（10K件目標）
-- ========================================
CREATE TABLE IF NOT EXISTS concepts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT,
    name_original TEXT,            -- 原語表記（必須に近い）
    original_script TEXT,           -- 原語のスクリプト種別（kanji/sanskrit/arabic/greek等）
    subfield_id INTEGER NOT NULL,
    region TEXT NOT NULL,           -- 西欧/東アジア/南アジア/西アジア/アフリカ/ラテンアメリカ/横断
    period_id INTEGER,
    definition TEXT NOT NULL,
    background TEXT,                -- 背景・成立文脈
    development TEXT,               -- その後の系譜展開
    historical_context TEXT,        -- 時代背景
    primary_source_url TEXT,        -- 一次資料URL（Gutenberg/青空文庫/CTEXT等）
    primary_source_type TEXT,       -- 一次資料タイプ
    importance_score INTEGER DEFAULT 3,  -- 1-5
    fourth_transform_status TEXT,   -- 'rethinking'/'invariant'/'partial' の3値
    fourth_transform_note TEXT,     -- 第四変容期における再考論点
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name_ja, region, period_id),
    FOREIGN KEY(subfield_id) REFERENCES subfields(id),
    FOREIGN KEY(period_id) REFERENCES periods(id)
);

CREATE INDEX IF NOT EXISTS idx_concepts_subfield ON concepts(subfield_id);
CREATE INDEX IF NOT EXISTS idx_concepts_region ON concepts(region);
CREATE INDEX IF NOT EXISTS idx_concepts_fourth ON concepts(fourth_transform_status);

-- ========================================
-- 2. 作家・作者テーブル（3K件目標）
-- ========================================
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT,
    name_original TEXT,
    birth_year INTEGER,             -- 負数=BCE
    death_year INTEGER,
    region TEXT NOT NULL,
    nationality TEXT,
    primary_language TEXT,
    period_id INTEGER,
    biography TEXT,
    contributions TEXT,             -- 文学史への貢献
    movements_belonged TEXT,        -- 所属運動（カンマ区切り）
    importance_score INTEGER DEFAULT 3,
    primary_source_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name_ja, birth_year),
    FOREIGN KEY(period_id) REFERENCES periods(id)
);

CREATE INDEX IF NOT EXISTS idx_authors_region ON authors(region);
CREATE INDEX IF NOT EXISTS idx_authors_period ON authors(period_id);

-- ========================================
-- 3. 作品テーブル（5K件目標、文学DB固有）
-- ========================================
CREATE TABLE IF NOT EXISTS works (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_ja TEXT NOT NULL,
    title_en TEXT,
    title_original TEXT,
    original_script TEXT,
    author_id INTEGER,
    author_name_text TEXT,          -- 作者不詳/集合作の場合のフリーテキスト
    publication_year INTEGER,
    period_id INTEGER,
    region TEXT NOT NULL,
    genre TEXT,                     -- 詩/小説/戯曲/叙事詩/口承等
    language TEXT,
    summary TEXT,
    significance TEXT,              -- 文学史的意義
    influence_summary TEXT,         -- 後代への影響
    primary_source_url TEXT,
    importance_score INTEGER DEFAULT 3,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(author_id) REFERENCES authors(id),
    FOREIGN KEY(period_id) REFERENCES periods(id)
);

CREATE INDEX IF NOT EXISTS idx_works_author ON works(author_id);
CREATE INDEX IF NOT EXISTS idx_works_region ON works(region);
CREATE INDEX IF NOT EXISTS idx_works_period ON works(period_id);

-- ========================================
-- 4. 文学運動・流派テーブル（500件目標）
-- ========================================
CREATE TABLE IF NOT EXISTS movements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT,
    name_original TEXT,
    region TEXT NOT NULL,
    start_year INTEGER,
    end_year INTEGER,
    description TEXT,
    key_principles TEXT,
    historical_context TEXT,
    legacy TEXT,
    primary_source_url TEXT,
    UNIQUE(name_ja, region)
);

-- ========================================
-- 5. 時代区分テーブル（地域別）
-- ========================================
CREATE TABLE IF NOT EXISTS periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja TEXT NOT NULL,
    name_en TEXT,
    region TEXT NOT NULL,
    start_year INTEGER,
    end_year INTEGER,
    description TEXT,
    UNIQUE(name_ja, region)
);

-- ========================================
-- 6. サブフィールド（24領域）
-- ========================================
CREATE TABLE IF NOT EXISTS subfields (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,      -- 'lit_eu_classical', 'lit_china_classical' 等
    name_ja TEXT NOT NULL,
    name_en TEXT,
    macro_region TEXT NOT NULL,     -- 西欧/東アジア/南西アジア/グローバルサウス/周縁横断/理論
    target_concepts INTEGER,        -- 目標概念数
    description TEXT
);

-- ========================================
-- 7. 関係性テーブル（30K件目標）
-- ========================================
CREATE TABLE IF NOT EXISTS relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_type TEXT NOT NULL,      -- 'concept'/'author'/'work'/'movement'
    source_id INTEGER NOT NULL,
    target_type TEXT NOT NULL,
    target_id INTEGER NOT NULL,
    relation_type TEXT NOT NULL,    -- 'influences'/'criticizes'/'extends'/'contains'/'translates'等
    description TEXT,
    bidirectional INTEGER DEFAULT 0,
    confidence INTEGER DEFAULT 3,   -- 1-5
    source_evidence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_relations_source ON relations(source_type, source_id);
CREATE INDEX IF NOT EXISTS idx_relations_target ON relations(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_relations_type ON relations(relation_type);

-- ========================================
-- 8. 系譜リンク（影響・継承・批判の特化テーブル）
-- ========================================
CREATE TABLE IF NOT EXISTS geneal_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ancestor_concept_id INTEGER NOT NULL,
    descendant_concept_id INTEGER NOT NULL,
    transformation_type TEXT,       -- 'extension'/'inversion'/'critique'/'translation'/'syncretism'
    description TEXT,
    transmission_path TEXT,         -- 文化圏間の伝播経路
    FOREIGN KEY(ancestor_concept_id) REFERENCES concepts(id),
    FOREIGN KEY(descendant_concept_id) REFERENCES concepts(id)
);

-- ========================================
-- 9. 他DBへのクロスドメインリンク
-- ========================================
CREATE TABLE IF NOT EXISTS cross_domain (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lit_entity_type TEXT NOT NULL,  -- 'concept'/'author'/'work'/'movement'
    lit_entity_id INTEGER NOT NULL,
    target_db TEXT NOT NULL,        -- 'PHIL'/'PT'/'AN'/'MG'/'Era-Talents'/'SI'
    target_entity_id TEXT,          -- 他DB側の参照ID
    target_entity_name TEXT,
    link_type TEXT,                 -- 'shared_concept'/'borrowed_from'/'parallel'
    description TEXT
);

CREATE INDEX IF NOT EXISTS idx_cross_lit ON cross_domain(lit_entity_type, lit_entity_id);
CREATE INDEX IF NOT EXISTS idx_cross_target ON cross_domain(target_db);

-- ========================================
-- 10. 第四変容タグ（クロスカット）
-- ========================================
CREATE TABLE IF NOT EXISTS fourth_transform_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    concept_id INTEGER NOT NULL,
    axis TEXT NOT NULL,             -- 作者性/創造性/物語/主体/正典/受容/翻訳/真正性/言語
    status TEXT NOT NULL,           -- 'rethinking'/'invariant'/'partial'
    rationale TEXT,                 -- なぜAI時代に再考対象か
    related_ai_phenomenon TEXT,     -- 関連するAI現象（生成AI/共著/合成データ等）
    FOREIGN KEY(concept_id) REFERENCES concepts(id),
    UNIQUE(concept_id, axis)
);

CREATE INDEX IF NOT EXISTS idx_ft_axis ON fourth_transform_tags(axis);
CREATE INDEX IF NOT EXISTS idx_ft_status ON fourth_transform_tags(status);
