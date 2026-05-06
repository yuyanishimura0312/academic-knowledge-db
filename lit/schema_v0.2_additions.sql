-- LIT-DB schema v0.2 additions（2026-05-07 西村承認）
-- A: source_tier カラム追加（ハルシネーション防止）
-- B: canonical_in_region カラム追加（地域別正典、西欧中心主義回避）

-- ============================================
-- concepts テーブル拡張
-- ============================================
ALTER TABLE concepts ADD COLUMN source_tier TEXT;
-- 値: 'primary' (PD原典直接) / 'secondary' (批判校訂版) / 'tertiary' (複数二次文献合致)

ALTER TABLE concepts ADD COLUMN canonical_in_region TEXT;
-- 値: 'core' / 'major' / 'minor' / 'marginal'（地域内正典度）

CREATE INDEX IF NOT EXISTS idx_concepts_tier ON concepts(source_tier);
CREATE INDEX IF NOT EXISTS idx_concepts_canonical ON concepts(canonical_in_region);

-- ============================================
-- authors テーブル拡張
-- ============================================
ALTER TABLE authors ADD COLUMN source_tier TEXT;
ALTER TABLE authors ADD COLUMN canonical_in_region TEXT;

CREATE INDEX IF NOT EXISTS idx_authors_tier ON authors(source_tier);
CREATE INDEX IF NOT EXISTS idx_authors_canonical ON authors(canonical_in_region);

-- ============================================
-- works テーブル拡張
-- ============================================
ALTER TABLE works ADD COLUMN source_tier TEXT;
ALTER TABLE works ADD COLUMN canonical_in_region TEXT;

CREATE INDEX IF NOT EXISTS idx_works_tier ON works(source_tier);
CREATE INDEX IF NOT EXISTS idx_works_canonical ON works(canonical_in_region);

-- ============================================
-- movements テーブル拡張
-- ============================================
ALTER TABLE movements ADD COLUMN source_tier TEXT;
ALTER TABLE movements ADD COLUMN canonical_in_region TEXT;

-- ============================================
-- 第四変容9軸の操作的定義テーブル（Phase 1冒頭で確定するためのスケルトン）
-- ============================================
CREATE TABLE IF NOT EXISTS fourth_transform_axes (
    axis TEXT PRIMARY KEY,           -- 作者性/創造性/物語/主体/正典/受容/翻訳/真正性/言語
    operational_definition TEXT,     -- 操作的定義（Phase 1で確定）
    classical_concept TEXT,          -- 古典的概念
    ai_era_phenomenon TEXT,          -- AI時代の対応現象
    rethink_indicator TEXT,          -- 「再考対象」と判定するための指標
    related_disciplines TEXT,        -- 関連する他DB（PHIL/AN/MG等）
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO fourth_transform_axes (axis) VALUES
('作者性'),
('創造性'),
('物語'),
('主体'),
('正典'),
('受容'),
('翻訳'),
('真正性'),
('言語');
