-- LIT-DB サブフィールド24領域 シードデータ
-- 西村承認: 2026-05-06
-- 合計目標: 11,000概念（西欧3,500 / 東アジア2,000 / 南西アジア1,200 / グローバルサウス1,200 / 周縁横断1,500 / 理論1,600）

INSERT OR IGNORE INTO subfields (code, name_ja, name_en, macro_region, target_concepts, description) VALUES
-- 西欧文学系譜（7領域・3,500）
('lit_eu_classical',     '古典古代文学',         'Classical Antiquity Literature',     '西欧',           500, 'ホメロス、ギリシャ悲劇、ラテン文学、聖書文学'),
('lit_eu_medieval',      '中世文学',             'Medieval Literature',                '西欧',           400, '騎士道物語、寓意文学、宗教文学、吟遊詩人'),
('lit_eu_renaissance',   'ルネサンス・近世文学', 'Renaissance & Early Modern Lit',     '西欧',           500, '人文主義、シェイクスピア、バロック'),
('lit_eu_enlightenment', '啓蒙・ロマン主義',     'Enlightenment & Romanticism',        '西欧',           500, '小説の勃興、ゴシック、ロマン派'),
('lit_eu_realism',       'リアリズム・自然主義・象徴主義', 'Realism, Naturalism & Symbolism', '西欧',  600, '19世紀小説、象徴詩'),
('lit_eu_modernism',     'モダニズム',           'Modernism',                          '西欧',           500, 'ジョイス、プルースト、カフカ、意識の流れ'),
('lit_eu_postmodern',    'ポストモダン・現代',   'Postmodern & Contemporary',          '西欧',           500, 'メタフィクション、自伝小説、AI時代の文学'),

-- 東アジア文学系譜（4領域・2,000）
('lit_cn_classical',     '中国古典文学',         'Chinese Classical Literature',       '東アジア',       600, '詩経、楚辞、唐詩、宋詞、章回小説、四大奇書'),
('lit_cn_modern',        '中国近現代文学',       'Modern Chinese Literature',          '東アジア',       400, '五四運動以降、魯迅、現代中国小説'),
('lit_jp_classical',     '日本古典文学',         'Japanese Classical Literature',      '東アジア',       500, '万葉集、源氏物語、能・狂言、俳諧、近世小説'),
('lit_jp_modern',        '日本近現代文学',       'Modern Japanese Literature',         '東アジア',       500, '明治以降、私小説、戦後文学、現代'),

-- 南西アジア文学（3領域・1,200）
('lit_india',            'インド文学',           'Indian Literature',                  '南西アジア',     500, 'ヴェーダ、サンスクリット叙事詩、バクティ詩、近代諸言語文学'),
('lit_arabic',           'アラブ文学',           'Arabic Literature',                  '南西アジア',     400, 'ジャーヒリーヤ詩、千夜一夜、現代アラブ小説'),
('lit_persian_turkish',  'ペルシア・トルコ文学', 'Persian & Turkish Literature',       '南西アジア',     300, 'フェルドウスィー、ハーフェズ、近代トルコ文学'),

-- グローバル・サウス（3領域・1,200）
('lit_africa',           'アフリカ文学',         'African Literature',                 'グローバルサウス', 400, '口承伝統、アフリカ近代小説、ネグリチュード'),
('lit_latin_america',    'ラテンアメリカ文学',   'Latin American Literature',          'グローバルサウス', 500, '魔術的リアリズム、ブーム期、先住民文学'),
('lit_se_asia_korea',    '東南アジア・韓国文学', 'SE Asian & Korean Literature',       'グローバルサウス', 300, 'ベトナム、フィリピン、インドネシア、韓国近現代'),

-- 周縁・横断（4領域・1,500）
('lit_russia_slavic',    'ロシア・スラヴ文学',   'Russian & Slavic Literature',        '周縁横断',       400, 'ドストエフスキー、トルストイ、銀の時代'),
('lit_indigenous_oral',  '先住民・口承文学',     'Indigenous & Oral Literature',       '周縁横断',       400, 'ネイティブアメリカン、アボリジニ、アイヌ'),
('lit_diaspora',         'ディアスポラ・移民文学', 'Diaspora & Migrant Literature',    '周縁横断',       400, '越境文学、多言語文学'),
('lit_genre',            '児童・大衆・ジャンル文学', 'Children/Popular/Genre Lit',     '周縁横断',       300, 'SF、ミステリ、児童文学、グラフィックノベル'),

-- 理論・横断（3領域・1,600）
('lit_theory',           '文学理論・批評',       'Literary Theory & Criticism',        '理論',           700, '形式主義、構造主義、ポスト構造主義、ジェンダー、エコクリティシズム'),
('lit_world_translation','比較文学・世界文学・翻訳論', 'Comparative & World Lit',      '理論',           500, 'Goethe Weltliteratur、Casanova、翻訳研究'),
('lit_digital_ai',       'デジタル人文学・AI時代', 'Digital Humanities & AI Era',      '理論',           400, '電子文学、生成文学、作者性の解体、第四変容期');
