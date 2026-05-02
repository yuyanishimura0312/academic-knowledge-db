-- 事業開発・BMI ドメイン DB スキーマ
-- ターゲット: ~/projects/research/academic-knowledge-db/academic.db
-- 適用方法: sqlite3 academic.db < business_dev_schema.sql

PRAGMA foreign_keys = ON;

-- ============================================================
-- メインテーブル: 概念・理論
-- ============================================================
CREATE TABLE IF NOT EXISTS business_development_bm_theory (
    id TEXT PRIMARY KEY,                    -- 形式: BDBM_NNN
    name_ja TEXT NOT NULL,
    name_en TEXT NOT NULL,
    name_original TEXT,                     -- 母国語名 (e.g. ドイツ語/フランス語の用語)
    definition TEXT NOT NULL,               -- 50字以上、平均100-150字
    impact_summary TEXT,                    -- 学術的・実務的インパクト

    subfield TEXT NOT NULL CHECK(subfield IN (
        'bmi_theory',
        'bmi_process',
        'digital_platform',
        'alliance',
        'corp_venture',
        'market_entry',
        'open_innov',
        'lean_startup',
        'disruptive',
        'subscription_saas',
        'sustainable_bm',
        'channel_gtm',
        'b2b_enterprise',
        'ma_corp_dev'
    )),
    school_of_thought TEXT NOT NULL,        -- e.g. Activity System / Resource-based / Transaction Cost / Lean / Disruption School

    era_start INTEGER NOT NULL,             -- 西暦4桁
    era_end INTEGER,                         -- 継続中なら NULL

    opposing_concept_names TEXT,             -- 対立概念 (JSON配列文字列)
    keywords_ja TEXT NOT NULL,               -- comma-separated
    keywords_en TEXT NOT NULL,
    key_researchers TEXT NOT NULL,           -- JSON array, e.g. ["Osterwalder, A.","Pigneur, Y."]
    key_works TEXT NOT NULL,                 -- JSON array, e.g. [{"title":"...","year":2010,"venue":"..."}]

    -- 分野固有カラム (Phase 0 で設計)
    industry_applicability TEXT,             -- multi-value: B2B|B2C|B2B2C|Platform|All (JSON array)
    case_companies TEXT,                     -- JSON array, e.g. ["Salesforce","Netflix","Airbnb"]
    implementation_complexity INTEGER CHECK(implementation_complexity BETWEEN 1 AND 5),

    -- 共通メタ
    status TEXT DEFAULT 'active' CHECK(status IN ('active','deprecated','merged')),
    source_reliability TEXT DEFAULT 'secondary' CHECK(source_reliability IN ('primary','secondary','tertiary')),
    data_completeness INTEGER DEFAULT 80 CHECK(data_completeness BETWEEN 0 AND 100),

    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

-- ============================================================
-- 関係テーブル
-- ============================================================
CREATE TABLE IF NOT EXISTS business_development_bm_theory_relations (
    id TEXT PRIMARY KEY,                    -- 形式: BDBMR_NNNN
    source_concept_id TEXT NOT NULL REFERENCES business_development_bm_theory(id) ON DELETE CASCADE,
    target_concept_id TEXT NOT NULL REFERENCES business_development_bm_theory(id) ON DELETE CASCADE,
    relation_type TEXT NOT NULL CHECK(relation_type IN (
        'derived_from',          -- AはBから派生
        'extends',               -- AはBを拡張
        'critiques',             -- AはBを批判
        'empirically_tests',     -- AはBを実証
        'synthesizes',           -- AはBを統合
        'competes_with',         -- AとBは競合理論
        'applies_to_policy',     -- AはBの政策的応用
        'complements',           -- AとBは補完
        'related_to',            -- 関連 (デフォルト)
        'influenced'             -- 影響を受けた
    )),
    relation_description TEXT,              -- 30-200字、関係の具体性
    strength INTEGER DEFAULT 5 CHECK(strength BETWEEN 1 AND 10),
    created_at TEXT DEFAULT (datetime('now'))
);

-- ============================================================
-- インデックス
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_bdbm_subfield ON business_development_bm_theory(subfield);
CREATE INDEX IF NOT EXISTS idx_bdbm_school ON business_development_bm_theory(school_of_thought);
CREATE INDEX IF NOT EXISTS idx_bdbm_era ON business_development_bm_theory(era_start);
CREATE INDEX IF NOT EXISTS idx_bdbm_status ON business_development_bm_theory(status);

CREATE INDEX IF NOT EXISTS idx_bdbm_rel_src ON business_development_bm_theory_relations(source_concept_id);
CREATE INDEX IF NOT EXISTS idx_bdbm_rel_tgt ON business_development_bm_theory_relations(target_concept_id);
CREATE INDEX IF NOT EXISTS idx_bdbm_rel_type ON business_development_bm_theory_relations(relation_type);

-- ============================================================
-- 完全性ビュー (Phase 3 検証で使用)
-- ============================================================
CREATE VIEW IF NOT EXISTS v_bdbm_completeness AS
SELECT
    subfield,
    COUNT(*) as total,
    SUM(CASE WHEN definition IS NULL OR definition = '' THEN 1 ELSE 0 END) as missing_definition,
    SUM(CASE WHEN key_researchers IS NULL OR key_researchers = '' OR key_researchers = '[]' THEN 1 ELSE 0 END) as missing_researchers,
    SUM(CASE WHEN key_works IS NULL OR key_works = '' OR key_works = '[]' THEN 1 ELSE 0 END) as missing_works,
    SUM(CASE WHEN era_start IS NULL THEN 1 ELSE 0 END) as missing_era,
    AVG(LENGTH(definition)) as avg_definition_length,
    MIN(era_start) as earliest_era,
    MAX(era_start) as latest_era
FROM business_development_bm_theory
GROUP BY subfield;

-- 期間分布ビュー
CREATE VIEW IF NOT EXISTS v_bdbm_era_distribution AS
SELECT
    CASE
        WHEN era_start < 1960 THEN 'Pre-1960'
        WHEN era_start < 1985 THEN '1960-1984'
        WHEN era_start < 2000 THEN '1985-1999'
        WHEN era_start < 2015 THEN '2000-2014'
        ELSE '2015-'
    END as era_band,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM business_development_bm_theory), 1) as pct
FROM business_development_bm_theory
GROUP BY 1
ORDER BY MIN(era_start);

-- 関係分布ビュー
CREATE VIEW IF NOT EXISTS v_bdbm_relation_distribution AS
SELECT
    relation_type,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM business_development_bm_theory_relations), 1) as pct
FROM business_development_bm_theory_relations
GROUP BY relation_type
ORDER BY COUNT(*) DESC;

-- 孤立エントリ検出ビュー (Phase 4 接続率検証用)
CREATE VIEW IF NOT EXISTS v_bdbm_isolated AS
SELECT t.id, t.name_ja, t.subfield
FROM business_development_bm_theory t
WHERE NOT EXISTS (
    SELECT 1 FROM business_development_bm_theory_relations r
    WHERE r.source_concept_id = t.id OR r.target_concept_id = t.id
);

-- ============================================================
-- cross_domain_relations は academic.db に既存と仮定 (innovation_theory, management_studies 等)
-- もし無ければ:
-- CREATE TABLE cross_domain_relations (
--     id TEXT PRIMARY KEY,
--     source_table TEXT, source_id TEXT,
--     target_table TEXT, target_id TEXT,
--     relation_type TEXT,
--     description TEXT,
--     created_at TEXT DEFAULT (datetime('now'))
-- );
-- ============================================================

-- 確認クエリ (適用後に手動実行推奨)
-- .schema business_development_bm_theory
-- SELECT name FROM sqlite_master WHERE type='view' AND name LIKE 'v_bdbm%';
