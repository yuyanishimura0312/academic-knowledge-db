"""
LIT-DB Phase 2 — C07: Western European Romanticism (西欧ロマン主義)
======================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Major themes / motifs (8)
  B. Major British Romantic author-concepts / works (8)
  C. Major German / French Romantic author-concepts / works (8)
  D. Major poetics / criticism (8)
  E. Form / movement concepts (8)

subfield_code='lit_eu_enlightenment' (id=4), region='西欧'
(C06: Enlightenment / C07: Romanticism share subfield_id=4 by design.)

Primary sources: Project Gutenberg, Romantic Circles, Deutsches Textarchiv,
Bibliothèque nationale de France (Gallica), British Library digitized texts.

Pattern: P1 (Canonical Primary Pursuit) — anchored to PD primary texts of
Wordsworth, Coleridge, Keats, Shelley, Byron, Mary Shelley, Goethe, Novalis,
Schlegel brothers, Hugo, Lamartine, Chateaubriand, Hoffmann, plus their
canonical critical-edition lineage.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding — Western European Romanticism
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("シュトゥルム・ウント・ドラング期", "Sturm und Drang", 1765, 1785,
     "ヘルダー・若きゲーテ・シラーらが主導した独語圏疾風怒濤期。理性偏重への反動として情念・天才・自然を称揚した前期ロマン主義の母胎。"),
    ("初期ロマン主義（独・英）", "Early Romanticism (German Frühromantik / British)",
     1785, 1815,
     "イェナ派（シュレーゲル兄弟、ノヴァーリス、シェリング）と英湖水詩人（ワーズワース・コールリッジ）が並行して詩学革命を起こした時期。『リリカル・バラッズ』1798年序文を画期とする。"),
    ("盛期ロマン主義（英・仏・独）", "High Romanticism", 1815, 1832,
     "第二世代英ロマン派（バイロン・シェリー・キーツ）、仏ロマン派の宣言期（ユゴー『クロムウェル』序文1827）、独後期ロマン主義（ホフマン、アイヒェンドルフ）が同時に開花した時期。"),
    ("後期ロマン主義（独・英・仏）", "Late Romanticism / Spätromantik", 1832, 1850,
     "ユゴー、ラマルティーヌ、シャトーブリアンら仏ロマン派盛期と、独後期ロマン派（メルヘン・幻想譚）の展開期。リアリズムへの移行を準備する。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


SUB = "lit_eu_enlightenment"
REG = "西欧"


# ===============================================================
# CATEGORY A — Major themes / motifs (8)
# ===============================================================

add({
    "name_ja": "想像力（ロマン主義的）",
    "name_en": "imagination (Romantic)",
    "name_original": "imagination",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "ロマン主義詩学の中核概念で、外的世界を能動的に構成し新たな現実を産出する精神能力。コールリッジ『文学的自伝』が「第一次想像力」（知覚の前提）と「第二次想像力」（詩的創造）に区分し、近代主観性の形而上学的基礎として理論化した。古典主義の模倣（mimesis）に代わる近代詩学の創造原理。",
    "background": "カント『判断力批判』の構想力（Einbildungskraft）論と独イェナ派の受容を、英国でコールリッジが詩学的に翻案した。",
    "development": "シェリー『詩の擁護』、エマソン、ボードレール、現代の創造性論まで連続。AI生成時代に「人間固有の創造能力」概念として再活性化される。",
    "historical_context": "啓蒙の理性中心主義への反動として近代主観性の中核能力に昇格した。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6081",
    "primary_source_type": "Project Gutenberg — Coleridge Biographia Literaria",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "ロマン主義が確立した「想像力こそ人間固有の創造原理」という前提は、生成AIが画像・テキスト・音楽を産出する現代において根本的再考を迫られる中心軸である。",
         "related_ai_phenomenon": "生成AIによる「創造性の脱人間化」論争"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "構想力（Einbildungskraft）",
         "description": "カント・シェリング哲学の構想力論と詩学的に共有。"},
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "生成AIの創造性",
         "description": "ロマン主義想像力概念がAI創造性論争の参照枠を提供。"},
    ],
})

add({
    "name_ja": "有機的形式",
    "name_en": "organic form",
    "name_original": "organic form",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "作品が外的規則によって付与された機械的形式（mechanical form）ではなく、内的生命の自己展開によって形を獲得するというロマン主義詩学の中核原理。コールリッジがA. W. シュレーゲル『演劇芸術論』を典拠にシェイクスピア論で英語圏に導入し、新批評・現代詩学にまで影響した。",
    "background": "ゲーテ『植物変態論』『動物変態論』の有機体論と、シェリングの自然哲学を文芸批評に転用した。",
    "development": "新批評（クリーンス・ブルックス、W. K. ウィムサット）の作品有機体観、生態批評（エコクリティシズム）の自然観念にまで連続。",
    "historical_context": "古典主義の三一致則・規範詩学への根本的対抗概念として提出された。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/8492",
    "primary_source_type": "Project Gutenberg — Coleridge Lectures on Shakespeare",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「作品が内的生命によって自ずと形をなす」という有機的形式論は、AIがプロンプトに応じて統計的に最適化された形式を産出する現代に対し、形式の発生論を根本から再考させる。",
         "related_ai_phenomenon": "AI生成における形式の統計的最適化と「有機性」の不在論争"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "有機的形式",
         "description": "Poetics DB近代詩学の中核概念として共有。"},
    ],
})

add({
    "name_ja": "崇高（ロマン主義的）",
    "name_en": "sublime (Romantic)",
    "name_original": "the sublime",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "美の調和を超え、計り知れぬ巨大さ・恐怖・無限性によって主体を圧倒し、その圧倒を通じて精神の超越的能力を顕示する美的経験。バーク『崇高と美の起源』（1757）、カント『判断力批判』を経て、ワーズワース『序曲』のアルプス越え場面、シェリー『モン・ブラン』、ターナー絵画に文学的・視覚的範例化された。",
    "background": "古代ロンギノス『崇高論』の18世紀再発見と英バーク・独カントの哲学的精緻化。",
    "development": "ロマン主義風景詩、ニーチェ・ハイデガーの存在論、リオタール『非人間的なもの』、現代エコ崇高論にまで連続。",
    "historical_context": "アルプス・大洋・宇宙の発見と産業革命の機械崇高が並行した時代背景。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/15083",
    "primary_source_type": "Project Gutenberg — Burke Sublime and Beautiful",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "崇高（カント）",
         "description": "カント美学の崇高論と直接共有。"},
    ],
})

add({
    "name_ja": "メランコリー（ロマン主義的）",
    "name_en": "Romantic melancholy",
    "name_original": "melancholy",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "ロマン主義が継承・再構成した憂鬱の主題。ルネサンス期の医学的体液論を超え、近代主観の自己疎外・喪失感・存在論的孤独として内面化された。キーツ『憂鬱に寄せるオード』、ノヴァーリス『夜の讃歌』、シャトーブリアン『ルネ』に範例化された「世紀病（mal du siècle）」の中核情調。",
    "background": "ルネサンスのバートン『憂鬱の解剖』伝統とゲーテ『ウェルテル』の自殺主題を継承。",
    "development": "ボードレール『憂鬱と理想』、ベンヤミン『パッセージ論』の憂鬱論、現代の鬱病文化論まで連続。",
    "historical_context": "革命後の幻滅と産業化による疎外がロマン主義主体性の中核情動を規定した。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/23684",
    "primary_source_type": "Project Gutenberg — Keats Poems",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "エキゾチシズム",
    "name_en": "exotic / exoticism",
    "name_original": "exotisme",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "オリエント・スペイン・スコットランド・ギリシアなど時空的に隔たった「他」を詩的霊感の源泉とするロマン主義の主題的志向。バイロン『チャイルド・ハロルドの巡礼』『東方物語群』、ユゴー『東方詩集』（1829）、シャトーブリアン『アタラ』が範例を成し、サイード『オリエンタリズム』が後に批判的に再読した。",
    "background": "18世紀の旅行記文学、ナポレオン遠征によるエジプト学、ガラン仏訳『千夜一夜物語』の流行が背景。",
    "development": "フローベール『サランボー』、象徴主義、20世紀植民地文学批評に連続。",
    "historical_context": "帝国主義拡張期の文化的他者表象として両義的位置を占めた。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/5131",
    "primary_source_type": "Project Gutenberg — Byron Childe Harold's Pilgrimage",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "オリエンタリズム",
         "description": "人類学DB批判理論の歴史的範例。"},
    ],
})

add({
    "name_ja": "中世復興",
    "name_en": "medievalism revival",
    "name_original": "medievalism",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "啓蒙が「暗黒時代」と切断した中世を、民族精神・有機的共同体・神秘的霊性の理想郷として復活させたロマン主義の歴史志向。スコット『アイヴァンホー』、ノヴァーリス『キリスト教世界またはヨーロッパ』、ハイデルベルク派民謡集、ノイシュヴァンシュタイン城建築まで広範囲に展開した。",
    "background": "オシアン詩・古英語バラッド復興・ヘルダーの民族精神論が前史を成す。",
    "development": "プレラファエライト派、ワーグナー楽劇、19世紀ゴシック復興建築、トールキン『指輪物語』に直接連続。",
    "historical_context": "ナポレオン戦争後のナショナリズム勃興と中世主義が相互に強化された。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/82",
    "primary_source_type": "Project Gutenberg — Scott Ivanhoe",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "道徳的力としての自然",
    "name_en": "nature as moral force",
    "name_original": "nature as moral force",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "自然が単なる風景や資源ではなく、人間の道徳的・霊的形成を導く能動的教師であるとするロマン主義の核心思想。ワーズワース『ティンタン・アビー』『序曲』が「自然は私の道徳的存在の魂、すべての楽しい思想の養い手」と謳い、エマソン・ソロー、現代エコクリティシズムへ連続する。",
    "background": "シャフツベリ・ルソーの自然賛美と独自然哲学（シェリング）を継承。",
    "development": "アメリカ超絶主義、現代の生態批評、ディープ・エコロジー運動に直接連続。",
    "historical_context": "産業化と都市化が進行する中での自然の倫理化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/12145",
    "primary_source_type": "Project Gutenberg — Wordsworth Lyrical Ballads",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "自然観の文化的構築",
         "description": "人類学DB自然概念史の近代範例。"},
    ],
})

add({
    "name_ja": "個人天才",
    "name_en": "individual genius",
    "name_original": "Genie / genius",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "シュトゥルム・ウント・ドラング期",
    "definition": "規則を超え自らに法を与える創造的個人としての「天才」概念。シュトゥルム・ウント・ドラング期の独「天才崇拝（Geniekult）」に発し、カント『判断力批判』が「天才は芸術に規則を与える才能」と理論化、ロマン主義的作家性の核となった。著作権・近代著者性制度の思想的基盤。",
    "background": "ヤング『独創的作品論』（1759）、ゲーテ『シェイクスピア記念日のために』が独天才崇拝を起動した。",
    "development": "19世紀の天才崇拝、20世紀の作家中心主義、フーコー「作者とは何か」の批判、現代の著作権論争まで連続。",
    "historical_context": "市民社会成立期の個人主義と職業作家制度の確立期。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/kant_kritik_1790",
    "primary_source_type": "Deutsches Textarchiv — Kant Kritik der Urteilskraft",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "ロマン主義が確立した「規則を超える創造的個人」としての作者像は、AIが共同・分散的に生成する現代において、近代著者性制度の形而上学的根拠そのものが再考対象となる。",
         "related_ai_phenomenon": "AI共同創作と著作権・作者性の解体論争"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "天才（Genie）",
         "description": "カント美学の天才論と直接共有。"},
    ],
})


# ===============================================================
# CATEGORY B — Major British Romantic author-concepts / works (8)
# ===============================================================

add({
    "name_ja": "ワーズワース『リリカル・バラッズ』序文",
    "name_en": "Wordsworth, Preface to Lyrical Ballads",
    "name_original": "Preface to Lyrical Ballads",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "1800年版・1802年増補版でワーズワースが付した英ロマン主義の綱領的詩論。「日常人の本物の言語」を詩語とし、詩を「強い感情の自発的なあふれ出し（spontaneous overflow of powerful feelings）」、その感情を「平静の中で回想（emotion recollected in tranquility）」したものと定義した。古典主義詩学への根本的対抗綱領。",
    "background": "コールリッジとの共作詩集『リリカル・バラッズ』（1798）の理論化。仏革命の挫折経験と湖水地方の隠遁生活が背景。",
    "development": "シェリー『詩の擁護』、コールリッジ『文学的自伝』、20世紀新批評・現代英米詩学の出発点となった。",
    "historical_context": "宮廷的詩語と階級的詩学への民主主義的挑戦。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/12145",
    "primary_source_type": "Project Gutenberg — Wordsworth Lyrical Ballads",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コールリッジ『文学的自伝』",
    "name_en": "Coleridge, Biographia Literaria",
    "name_original": "Biographia Literaria",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "コールリッジ1817年刊の自伝的批評書。第13章で第一次想像力（知覚の能動的綜合）と第二次想像力（詩的創造）、想像力（imagination）と空想（fancy）を区分し、第14章で「不信の自発的停止」（willing suspension of disbelief）を理論化した。英ロマン主義詩学の中核理論書。",
    "background": "シェリング自然哲学・カント超越論哲学の英国受容と、ワーズワースとの十数年来の対話の理論化。",
    "development": "リチャーズ『コールリッジの想像力論』、新批評の作品論、現代の認知詩学まで連続的影響。",
    "historical_context": "独哲学の英国輸入経路として近代英文芸批評の源流を成す。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6081",
    "primary_source_type": "Project Gutenberg — Coleridge Biographia Literaria",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コールリッジ『クブラ・カーン』とインスピレーション",
    "name_en": "Coleridge, Kubla Khan and inspiration",
    "name_original": "Kubla Khan",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "1797年作・1816年刊の断片詩。コールリッジ自身の序文によれば阿片夢の中で完璧に構成された詩を覚醒後に書きとめている最中に「ポーロックからの来訪者」によって中断され未完となった。インスピレーション・夢・無意識・断片美学のロマン主義的範例として神話化された。",
    "background": "パーチャス『パーチャス紀行』のクビライ汗記述と阿片の影響、深い無意識への関心。",
    "development": "象徴主義（ボードレール『人工楽園』）、シュルレアリスム自動筆記、現代の創作論・神経美学まで影響。",
    "historical_context": "理性的構成詩学に対する非合理的霊感詩学の典型。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/15396",
    "primary_source_type": "Project Gutenberg — Coleridge Sibylline Leaves",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "キーツ『ギリシア壺のオード』",
    "name_en": "Keats, Ode on a Grecian Urn",
    "name_original": "Ode on a Grecian Urn",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "キーツ1819年作の頌詩。古代ギリシア壺の絵画的場面を観想し、最終行「美は真であり、真は美である」（Beauty is truth, truth beauty）でエクフラシス詩の頂点に達した。芸術と時間、永遠と一瞬、表象と実在をめぐる近代詩学最高峰の名作とされる。",
    "background": "1819年の「奇跡の年」連作頌詩の一篇。エルギン・マーブルズの大英博物館展示の衝撃が背景。",
    "development": "新批評（クリーンス・ブルックス『よく出来た壺』）の理想テクスト、現代エクフラシス論の出発点。",
    "historical_context": "古典主義復興とロマン主義の独自的綜合。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/23684",
    "primary_source_type": "Project Gutenberg — Keats Poems",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "キーツ「消極的能力」",
    "name_en": "Keats, negative capability",
    "name_original": "negative capability",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "キーツが1817年12月の弟宛書簡で定式化した詩人の根本能力。「事実や理性に苛立たしく手を伸ばすことなく、不確実性、神秘、疑念のなかに留まることができる」精神状態を指す。シェイクスピア的な多面的共感力の本質を捉えた概念として20世紀以降批評の中核語彙となった。",
    "background": "コールリッジの哲学的体系化志向への対比として書簡で表明された。",
    "development": "リオネル・トリリングの自我論、ハロルド・ブルームの影響不安論、ジョン・キーガンの戦争史叙述論まで広範な領域で借用された。",
    "historical_context": "詩人の主体性をめぐるロマン主義内部の分岐点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/35698",
    "primary_source_type": "Project Gutenberg — Keats Letters",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「不確実性に留まる」消極的能力は、AIが即座に確定的解答を生成する現代において、人間固有の認知的態度として再評価されつつある。",
         "related_ai_phenomenon": "AIの即答志向と人間的不確実性保持能力の対比"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "詩人主体を「自己同一性を持たない」ものと規定するキーツの主体観は、AIが多様なペルソナを瞬時に演じ分ける現代の主体性論議と構造的に共鳴する。",
         "related_ai_phenomenon": "AIマルチペルソナと主体の脱中心化"},
    ],
})

add({
    "name_ja": "シェリー『詩の擁護』",
    "name_en": "Shelley, A Defence of Poetry",
    "name_original": "A Defence of Poetry",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "シェリーが1821年に執筆し1840年に没後刊行された詩論。ピーコック『詩の四時代』の詩衰退論への反駁として、想像力こそ道徳の原理、詩人を「世界の公認されざる立法者」（unacknowledged legislators of the world）と規定した。ロマン主義詩論の到達点。",
    "background": "シドニー『詩の擁護』伝統の継承と功利主義への対抗。",
    "development": "プラトン『国家』詩人追放論への近代的応答として、20世紀文学の社会的役割論まで連続。",
    "historical_context": "産業革命期の詩の地位防衛。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/5428",
    "primary_source_type": "Project Gutenberg — Shelley Defence of Poetry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バイロン的英雄",
    "name_en": "Byronic hero",
    "name_original": "Byronic hero",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "バイロン『チャイルド・ハロルド』『マンフレッド』『海賊』に範例化された反逆的・憂鬱的・知的に過剰な孤独な英雄類型。社会規範を超越し過去の罪に苛まれつつ運命に挑戦する。19世紀ヨーロッパ文学に絶大な影響を与え、ヒースクリフ（『嵐が丘』）、ロチェスター（『ジェイン・エア』）、ドストエフスキー諸主人公の祖型となった。",
    "background": "ミルトン『失楽園』のサタン像、ゲーテ『ファウスト』、シラーの強盗カールの遺産の融合。",
    "development": "ブロンテ姉妹小説の主人公、ドストエフスキー『悪霊』スタヴローギン、20世紀アンチヒーロー、現代のダーク・ヒーロー類型まで直接連続。",
    "historical_context": "ナポレオン的英雄像の文学的内面化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/5131",
    "primary_source_type": "Project Gutenberg — Byron Childe Harold's Pilgrimage",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "メアリー・シェリー『フランケンシュタイン』",
    "name_en": "Mary Shelley, Frankenstein",
    "name_original": "Frankenstein; or, The Modern Prometheus",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "メアリー・シェリー1818年刊の小説。ジュネーヴ湖畔の幽霊物語競作で着想され、科学者フランケンシュタインが死体から人造人間を創造する物語を通じて、近代科学の越境的創造力、創造主の責任、創造物の主体性を問う。SF・ゴシック・ロマン主義の交差点に立ち、AI時代の人造創造物論の祖型として再活性化されている。",
    "background": "ガルヴァーニ電気生理学・新プロメテウス神話・ロマン主義天才論の合流。",
    "development": "現代SF全般、人造人間・サイボーグ・AI論争の参照枠、ハラウェイ『サイボーグ宣言』に至る系譜。",
    "historical_context": "産業革命と科学革新がもたらす存在論的不安の文学化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/84",
    "primary_source_type": "Project Gutenberg — Shelley Frankenstein",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "創造主と被造物の関係を「親と子」の倫理として描いた『フランケンシュタイン』は、AI設計者と生成AIの関係をめぐる現代の責任倫理論争の祖型として直接参照される。",
         "related_ai_phenomenon": "AI開発者責任論・AIアラインメント論争"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "「人間が知能を持つ存在を造ることの是非」を初めて文学化した本作は、AGI開発の倫理論議における歴史的範例として現役の参照点であり続ける。",
         "related_ai_phenomenon": "AGI創造の倫理（OpenAI/Anthropic安全性議論）"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "人造創造物・AGI予表",
         "description": "AI開発DBの倫理論争歴史的祖型として参照。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "技術倫理・人造人間論",
         "description": "哲学DB技術倫理史の近代範例。"},
    ],
})


# ===============================================================
# CATEGORY C — German / French Romantic author-concepts (8)
# ===============================================================

add({
    "name_ja": "ゲーテ『若きウェルテルの悩み』",
    "name_en": "Goethe, Die Leiden des jungen Werthers",
    "name_original": "Die Leiden des jungen Werthers",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "シュトゥルム・ウント・ドラング期",
    "definition": "ゲーテ1774年刊の書簡体小説。婚約者を持つロッテへの叶わぬ恋に苦悩する若者ウェルテルが自殺に至る物語。汎ヨーロッパ的なベストセラーとなり「ウェルテル熱」（Wertherfieber）模倣自殺現象を引き起こした。シュトゥルム・ウント・ドラングを代表し、ロマン主義的主観性・感受性・憂鬱の起点を成す作品。",
    "background": "ゲーテ自身のシャルロッテ・ブッフへの恋愛体験とイェルザレム自殺事件の融合。",
    "development": "仏革命期『新エロイーズ』と並ぶ感受性小説の頂点、ナポレオンの愛読書、ロマン主義的自殺の文学的祖型。",
    "historical_context": "理性主義啓蒙への反動としての感情の解放と過剰。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/goethe_werther01_1774",
    "primary_source_type": "Deutsches Textarchiv — Goethe Werther",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ゲーテ『ファウスト』",
    "name_en": "Goethe, Faust",
    "name_original": "Faust. Eine Tragödie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "ゲーテが60余年をかけて執筆した二部構成の悲劇詩。第一部（1808）は学者ファウストとメフィストフェレスの契約とグレートヒェン悲劇、第二部（1832）は古典ヘレナ救出と近代化事業を通じた人間意志の壮大な探究。近代精神の総合的肖像、独語圏文学の最高峰。",
    "background": "民衆本『ファウスト博士』伝統、マーロウ『フォースタス博士』、シュトゥルム・ウント・ドラング期断片の生涯にわたる発展。",
    "development": "ヴァレリー、トーマス・マン『ファウスト博士』、現代の浮遊する近代主体論まで広範な影響。",
    "historical_context": "啓蒙の知的野心とロマン主義的超越志向の総合。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/goethe_faust01_1808",
    "primary_source_type": "Deutsches Textarchiv — Goethe Faust I",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シュレーゲル兄弟のロマン主義理論",
    "name_en": "Schlegel brothers' Romantic theory",
    "name_original": "Frühromantische Theorie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "フリードリヒ・シュレーゲルとアウグスト・ヴィルヘルム・シュレーゲル兄弟が雑誌『アテネーウム』（1798–1800）を中心に展開したイェナ派初期ロマン主義の理論体系。「ロマン主義詩は進歩的普遍詩」（progressive Universalpoesie）を掲げ、詩・哲学・批評・断片・アイロニーを統合する全体論的詩学を構築した。",
    "background": "カント・フィヒテ哲学の文芸批評への展開、ノヴァーリス・ティーク・シェリングらイェナ派の集団的協働。",
    "development": "A.W.シュレーゲル『演劇芸術と文学に関する講義』が英コールリッジに移植、現代比較文学の起点を成す。",
    "historical_context": "独語圏初の組織的文芸批評運動。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/schlegel_athenaeum01_1798",
    "primary_source_type": "Deutsches Textarchiv — Athenäum Fragmente",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ノヴァーリス『夜の讃歌』",
    "name_en": "Novalis, Hymnen an die Nacht",
    "name_original": "Hymnen an die Nacht",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "ノヴァーリス1800年『アテネーウム』掲載の散文詩・韻文混合作品。早世した婚約者ゾフィーへの哀悼を起点に、夜・死・無限・神秘的合一を讃える六部構成。啓蒙の昼の理性に対し、ロマン主義の夜の神秘の美学を最高度に表現した独前期ロマン主義の代表作。",
    "background": "婚約者ゾフィー・フォン・キューンの早世（1797）と神秘主義的回心体験。",
    "development": "象徴主義の夜・死の主題、リルケの哀歌、20世紀の存在論的詩まで連続。",
    "historical_context": "啓蒙の昼の理性に対する夜の形而上学の確立。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/novalis_hymnen_1800",
    "primary_source_type": "Deutsches Textarchiv — Novalis Hymnen an die Nacht",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ホフマンの幻想性",
    "name_en": "E. T. A. Hoffmann's fantastic",
    "name_original": "Hoffmanns Fantastisches",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "E. T. A. ホフマン（1776–1822）の小説群（『砂男』『黄金の壺』『悪魔の霊液』）に体現された、日常と幻想・自我と分身・正気と狂気の境界を曖昧化する文学的様式。フロイト『不気味なもの』論文が『砂男』を範例にした近代心理分析の文学的祖型として機能した。",
    "background": "独後期ロマン主義のメルヘン伝統と、ホフマン自身の音楽家・法律家・作家としての多重生活。",
    "development": "ポー、ドストエフスキー『分身』、カフカ、現代マジック・リアリズム、ホラー文学全般に絶大な影響。",
    "historical_context": "市民社会の合理性とその裂け目への近代的眼差し。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/hoffmann_sandmann_1816",
    "primary_source_type": "Deutsches Textarchiv — Hoffmann Der Sandmann",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ユゴー『クロムウェル』序文",
    "name_en": "Hugo, Préface de Cromwell",
    "name_original": "Préface de Cromwell",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "ヴィクトル・ユゴー1827年戯曲『クロムウェル』に付した綱領的序文。仏古典主義の三一致則を撤廃し、グロテスクと崇高の対比を本質とする「ロマン主義的ドラマ」を提唱。仏ロマン主義の宣言文書として機能し、1830年『エルナニ』初演の劇場乱闘事件（La bataille d'Hernani）に至る論争を起動した。",
    "background": "シェイクスピア・カルデロンの仏受容と、シャトーブリアン・スタール夫人によるロマン主義準備期の集大成。",
    "development": "ユゴー戯曲群、ロマン主義劇場の制度化、自然主義リアリズム劇への展開まで連続。",
    "historical_context": "復古王政期の文化保守主義への前衛宣言。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k375194d",
    "primary_source_type": "Gallica BnF — Hugo Cromwell",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラマルティーヌ『瞑想詩集』",
    "name_en": "Lamartine, Méditations poétiques",
    "name_original": "Méditations poétiques",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "アルフォンス・ド・ラマルティーヌ1820年刊の処女詩集。「湖」「孤独」「秋」など二十四篇を収め、亡き恋人エルヴィールへの哀悼を通じて自然・記憶・神への憧憬を歌う。仏ロマン主義抒情詩の出発点を成し、その出版が仏文学史上のロマン主義開始期として記憶される。",
    "background": "ジュリー・シャルル（エルヴィール）との恋愛と1817年の彼女の死、シャトーブリアン文体の継承。",
    "development": "ヴィニー、ミュッセ、ユゴー抒情詩への直接連続、仏抒情詩の近代的起点。",
    "historical_context": "復古王政期の貴族的感受性とキリスト教的精神性の文学化。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k1042458d",
    "primary_source_type": "Gallica BnF — Lamartine Méditations poétiques",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シャトーブリアン『ルネ』",
    "name_en": "Chateaubriand, René",
    "name_original": "René",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "シャトーブリアン1802年『キリスト教精髄』内の挿話、1805年単行本化された短編。アメリカ亡命者ルネが姉アメリーへの近親愛的感情と漠然たる憂鬱（vague des passions）を語る告白体小説。仏「世紀病」（mal du siècle）を体現し、ウェルテル系譜の仏的展開として近代仏小説の主観性を開いた。",
    "background": "革命亡命体験とウェルテル受容、自身の北米旅行（1791）の文学的昇華。",
    "development": "コンスタン『アドルフ』、ミュッセ『世紀児の告白』、フローベール『感情教育』に至る世紀病系譜の起点。",
    "historical_context": "革命と亡命が生み出した世代の存在論的不安の文学化。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k816684",
    "primary_source_type": "Gallica BnF — Chateaubriand René",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY D — Major poetics / criticism (8)
# ===============================================================

add({
    "name_ja": "自発的なあふれ出し（ワーズワース）",
    "name_en": "spontaneous overflow (Wordsworth)",
    "name_original": "spontaneous overflow of powerful feelings",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "ワーズワース『リリカル・バラッズ』1800年序文の中核命題。「すべての良い詩は強い感情の自発的なあふれ出しである」と詩を規定し、創作の起点を規則ではなく内的情動に置いた。古典主義の理性的構成詩学に対するロマン主義的表現論詩学の宣言として、近代詩学のパラダイム転換点を成す。",
    "background": "アリストテレス『詩学』のミメーシス論への対抗としての近代表現論。",
    "development": "クローチェ表現論美学、20世紀ロマン主義批評（M. H. エイブラムス『鏡と灯』）の中心命題。",
    "historical_context": "創作論の中心が外部規則から内的情動へ移行した近代詩学転換点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/12145",
    "primary_source_type": "Project Gutenberg — Wordsworth Lyrical Ballads",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "表現論詩学",
         "description": "Poetics DBの近代表現論の根本概念として共有。"},
    ],
})

add({
    "name_ja": "有機的形式（コールリッジ）",
    "name_en": "organic form (Coleridge)",
    "name_original": "organic form",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "コールリッジがシェイクスピア論で展開した詩学概念。機械的形式（mechanical form）が外部から押しつけられる規則であるのに対し、有機的形式（organic form）は内的生命が自ら適切な形を産み出す原理である。植物の成長になぞらえ、A. W. シュレーゲル経由で英国に導入された独自然哲学の詩学的応用。",
    "background": "シェリング自然哲学・ゲーテ植物変態論の批評的応用。",
    "development": "新批評の作品有機体観、現代エコクリティシズムの自然観念にまで連続。",
    "historical_context": "古典主義の三一致則・規範詩学への根本的対抗概念。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/8492",
    "primary_source_type": "Project Gutenberg — Coleridge Lectures on Shakespeare",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "空想と想像力",
    "name_en": "fancy vs imagination",
    "name_original": "fancy and imagination",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "コールリッジ『文学的自伝』第13章の中心区分。空想（fancy）が既存の像を機械的に組み合わせる連想能力に過ぎないのに対し、想像力（imagination）は対立物を融合し新たな全体を産出する能動的綜合能力である。詩的創造性を凡庸な才能から区別する近代詩学の中核区分。",
    "background": "ジョン・ロックの連想心理学への対抗として、カント・シェリングの能動的綜合論を移植した。",
    "development": "I. A. リチャーズ『コールリッジの想像力論』、新批評を経て現代の創造性研究まで連続。",
    "historical_context": "経験論心理学と独観念論の対決の詩学的反映。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6081",
    "primary_source_type": "Project Gutenberg — Coleridge Biographia Literaria",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "第一次想像力と第二次想像力",
    "name_en": "primary vs secondary imagination",
    "name_original": "primary and secondary imagination",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "コールリッジ『文学的自伝』第13章の最重要区分。第一次想像力（primary imagination）はすべての人間知覚の能動的綜合（無限なる「我あり」（I AM）の有限な反復）、第二次想像力（secondary imagination）は意識的・選択的にこの能力を行使する詩的創造能力。日常的知覚と芸術的創造の連続性と差異を理論化した。",
    "background": "シェリング超越論的観念論の詩学的翻案。",
    "development": "現代認知詩学・神経美学の出発点として再評価。",
    "historical_context": "近代主観性論の詩学的応用の頂点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/6081",
    "primary_source_type": "Project Gutenberg — Coleridge Biographia Literaria",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヴィジョナリー（幻視者）",
    "name_en": "the visionary",
    "name_original": "the visionary",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "感覚を超え目に見えぬ霊的真理を「見る」ロマン主義詩人の自己規定。ブレイク『無垢と経験の歌』『預言詩』、シェリー『縛られざるプロメテウス』、ノヴァーリスに範例化された。詩人を社会の周縁にあって超越的真理を媒介する預言者・神秘家として位置づけるロマン主義的作家像の核。",
    "background": "聖書預言者伝統と近世神秘思想（ベーメ、スウェーデンボリ）の世俗化的継承。",
    "development": "ランボー『見者の手紙』、象徴主義、20世紀予言詩学（イェイツ）、現代の啓示文学まで連続。",
    "historical_context": "啓蒙の理性主義に対する非合理的霊性の擁護。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/1934",
    "primary_source_type": "Project Gutenberg — Blake Songs of Innocence and Experience",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ロマン主義的アイロニー",
    "name_en": "Romantic irony",
    "name_original": "romantische Ironie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "F. シュレーゲルが定式化した独前期ロマン主義詩学の中心概念。芸術家が自己の創作物との距離を保ち、作品内部で創作行為そのものを反省的に折り返す自己反省的態度。ティーク『長靴をはいた猫』、ホフマン『黄金の壺』、後にハイネ詩に範例化された近代的自己意識の文学的形式。",
    "background": "ソクラテス的アイロニーとフィヒテ自我論の融合的継承。",
    "development": "キェルケゴール『アイロニーの概念について』、20世紀メタフィクション、ポストモダン文学の系譜の出発点。",
    "historical_context": "近代主観性の自己反省能力の詩学的反映。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/schlegel_athenaeum01_1798",
    "primary_source_type": "Deutsches Textarchiv — Schlegel Athenäum",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "形式としての断片",
    "name_en": "fragment as form",
    "name_original": "Fragment als Form",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "イェナ派が積極的詩形式として確立した断片（Fragment）の文学的位置。シュレーゲル兄弟『リュケーウム断章』『アテネーウム断章』、ノヴァーリス『花粉』が代表例。完結した体系性を斥け、暗示・省略・跳躍によって全体を喚起する近代的形式美学を打ち立てた。コールリッジ『クブラ・カーン』も英国側の範例。",
    "background": "啓蒙体系哲学への対抗としての非体系的思考様式。",
    "development": "ニーチェの箴言、ベンヤミン『パッセージ論』、現代エッセイ・断章文学に連続。",
    "historical_context": "近代主観性が完結した体系を不可能と感受した時代の形式選択。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/schlegel_athenaeum01_1798",
    "primary_source_type": "Deutsches Textarchiv — Athenäum Fragmente",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "進歩的普遍詩",
    "name_en": "Romantic universal poetry",
    "name_original": "progressive Universalpoesie",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "F. シュレーゲル『アテネーウム断章』116の規定。「ロマン主義詩は進歩的普遍詩」であり、詩・哲学・批評・小説・歴史をすべて統合し、永遠に未完で生成途上にある全体的詩形式。ジャンル区分を超え、生と芸術の境界を解消する独前期ロマン主義の最大綱領。",
    "background": "シラー『素朴文学と感傷文学について』のジャンル超克論を急進化した。",
    "development": "20世紀ロマン主義研究（ベンヤミン『独ロマン主義における芸術批評の概念』）、現代総合芸術論の起点。",
    "historical_context": "啓蒙的ジャンル分化に対する綜合的詩学の樹立。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/schlegel_athenaeum01_1798",
    "primary_source_type": "Deutsches Textarchiv — Athenäum 116",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "ジャンル境界・国民文学境界・芸術と生の境界をすべて解消するシュレーゲルの普遍詩構想は、AIが文学・絵画・音楽を横断生成する現代において、近代正典制度の基盤を再考させる。",
         "related_ai_phenomenon": "AIマルチモーダル生成と正典・ジャンル境界の解消"},
    ],
})


# ===============================================================
# CATEGORY E — Form / movement concepts (8)
# ===============================================================

add({
    "name_ja": "ロマン主義対古典主義論争",
    "name_en": "Romanticism vs Classicism debate",
    "name_original": "Romanticism vs Classicism",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "19世紀前半の汎ヨーロッパ的文学論争。仏ではスタール夫人『独逸論』（1810）、ユゴー『クロムウェル』序文（1827）、1830年『エルナニ』乱闘がロマン主義側の宣言、独ではA.W.シュレーゲル『演劇芸術と文学に関する講義』、英ではコールリッジ・ハズリットがロマン主義詩学を確立。古典主義の規範詩学とロマン主義の表現詩学の根本対立。",
    "background": "新旧論争（17世紀末仏）伝統の19世紀的継承と急進化。",
    "development": "19世紀後半リアリズム・自然主義論争、20世紀モダニズム・ポストモダニズム論争への系譜的祖型。",
    "historical_context": "国民文学形成期の詩学的アイデンティティ闘争。",
    "primary_source_url": "https://gallica.bnf.fr/ark:/12148/bpt6k375194d",
    "primary_source_type": "Gallica BnF — Hugo Préface de Cromwell",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シュトゥルム・ウント・ドラング",
    "name_en": "Sturm und Drang",
    "name_original": "Sturm und Drang",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "シュトゥルム・ウント・ドラング期",
    "definition": "1770年代独語圏の文学運動。クリンガー戯曲『シュトゥルム・ウント・ドラング』（1776）が運動名の起源。ヘルダー・若きゲーテ・若きシラーが主導し、啓蒙の理性主義への反動として情念・自然・天才・民族を称揚した。ロマン主義の母胎であり、近代独文学の自立的起点。",
    "background": "ハーマン・ヘルダーの理性主義批判、ヤング『独創的作品論』『シェイクスピアの精神』翻訳の影響。",
    "development": "シラー『群盗』『たくらみと恋』、ゲーテ『ウェルテル』『ゲッツ』を経て、独ロマン主義に直接連続。",
    "historical_context": "宮廷的啓蒙文化に対する市民的青年世代の文学的反抗。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/klinger_sturm_1776",
    "primary_source_type": "Deutsches Textarchiv — Klinger Sturm und Drang",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "前期ロマン主義と後期ロマン主義",
    "name_en": "Frühromantik vs Spätromantik",
    "name_original": "Frühromantik und Spätromantik",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期ロマン主義（独・英・仏）",
    "definition": "独ロマン主義の二期区分。前期ロマン主義（Frühromantik、1797–1801頃）はイェナ派（シュレーゲル兄弟、ノヴァーリス、ティーク、シェリング）による哲学的・理論的な詩学革新期。後期ロマン主義（Spätromantik、1815頃以降）はハイデルベルク派（ブレンターノ、アルニム）・ベルリン派（ホフマン、シャミッソー）による民族学・幻想文学の展開期。",
    "background": "イェナ派の解散・ナポレオン戦争・復古王政期の文化的雰囲気変化。",
    "development": "ハイデルベルク派民謡集『少年の魔法の角笛』、グリム兄弟『童話集』、ホフマン幻想文学が後期の中核成果。",
    "historical_context": "革命の理想から復古的民族主義への移行。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/grimm_maerchen01_1812",
    "primary_source_type": "Deutsches Textarchiv — Grimm Kinder- und Hausmärchen",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "バラッド復興",
    "name_en": "ballad revival",
    "name_original": "ballad revival",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "シュトゥルム・ウント・ドラング期",
    "definition": "18世紀後半の英・独・スコットランドにおける民衆バラッド復興運動。パーシー『英国古歌の遺品』（1765）、ヘルダー『民謡集』、スコット『スコットランド辺境地方歌謡集』（1802–03）が出発点となり、ワーズワース＝コールリッジ『リリカル・バラッズ』（1798）の理論的綱領化を通じてロマン主義詩学の中核ジャンルとなった。",
    "background": "オシアン詩の流行（1760年代）と民衆文化への新たな関心の合流。",
    "development": "ゲーテ『魔王』、シラー芸術バラッド、独ロマン主義民謡、19世紀国民文学運動全般に連続。",
    "historical_context": "宮廷文化への対抗としての民衆口承文芸の発見。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/22535",
    "primary_source_type": "Project Gutenberg — Percy Reliques of Ancient English Poetry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ゴシック小説の成熟",
    "name_en": "Gothic novel mature",
    "name_original": "Gothic novel mature",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "盛期ロマン主義（英・仏・独）",
    "definition": "ウォルポール『オトラント城』（1764）に始まり、ラドクリフ『ユードルフォの謎』、ルイス『マンク』を経て、メアリー・シェリー『フランケンシュタイン』、マチューリン『放浪者メルモス』、ホフマン『悪魔の霊液』に至るロマン主義期に成熟したジャンル。中世城・廃墟・超自然・幻想・恐怖を素材とし、近代主観性の暗部を可視化した。",
    "background": "中世復興・廃墟趣味・崇高美学の交点で誕生。",
    "development": "ポー、ホーソーン、ブロンテ、ストーカー『ドラキュラ』を経て、現代ホラー・ゴシック・幻想文学に直接連続。",
    "historical_context": "啓蒙合理性の影として近代精神の暗部を表象。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/696",
    "primary_source_type": "Project Gutenberg — Walpole Castle of Otranto",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "オシアン真贋論争",
    "name_en": "Ossian fakery and authenticity debate",
    "name_original": "Ossian authenticity controversy",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "シュトゥルム・ウント・ドラング期",
    "definition": "ジェイムズ・マクファーソンが1760–63年に「3世紀ゲール語詩人オシアンからの翻訳」として出版した詩集をめぐる真贋論争。サミュエル・ジョンソンらが偽作と告発、後に大部分がマクファーソン創作と判明したが、それでもなおナポレオン・ゲーテ・若きヘルダーを熱狂させ、ロマン主義の祖典として絶大な影響を与えた古典版「ディープフェイク」事件。",
    "background": "啓蒙的考証学と原始的詩想への憧憬の衝突。",
    "development": "近代の真正性概念・著者性概念・翻訳概念をめぐる議論の歴史的祖型として現代まで参照される。",
    "historical_context": "民族文学探求と18世紀古文書偽作流行の交点。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/30505",
    "primary_source_type": "Project Gutenberg — Macpherson Poems of Ossian",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「真作か偽作か」が問題化された最初の近代的文学事件であるオシアン論争は、AI生成コンテンツの真正性判定問題（古典版ディープフェイク）の歴史的祖型として直接参照される。",
         "related_ai_phenomenon": "AI生成テキスト・画像のディープフェイク検出論争"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "ディープフェイク・AI生成真贋判定",
         "description": "AI開発DBの真正性論争歴史的祖型として参照。"},
    ],
})

add({
    "name_ja": "教養小説の成熟（『ヴィルヘルム・マイスター』）",
    "name_en": "Bildungsroman mature (Wilhelm Meister)",
    "name_original": "Bildungsroman / Wilhelm Meisters Lehrjahre",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "初期ロマン主義（独・英）",
    "definition": "ゲーテ『ヴィルヘルム・マイスターの修業時代』（1795–96）が確立した、若き主人公が経験を通じて自己形成（Bildung）に至る近代独語圏小説ジャンル。F. シュレーゲルが『ヴィルヘルム・マイスター論』で時代の三大事件（仏革命・フィヒテ哲学・マイスター）の一つに数え、ロマン主義の中心ジャンルとして理論化した。",
    "background": "ヴィーラント『アガトン物語』など啓蒙期教育小説の継承的展開。",
    "development": "ノヴァーリス『青い花』、シュティフター『晩夏』、ケラー『緑のハインリヒ』、トーマス・マン『魔の山』、現代教養小説全般の祖型。",
    "historical_context": "市民社会成立期の自己形成プロジェクトの文学的形式化。",
    "primary_source_url": "https://www.deutschestextarchiv.de/book/show/goethe_lehrjahre01_1795",
    "primary_source_type": "Deutsches Textarchiv — Goethe Wilhelm Meisters Lehrjahre",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ドラマティック・モノローグの先駆",
    "name_en": "dramatic monologue precursor",
    "name_original": "dramatic monologue precursor",
    "original_script": "roman",
    "subfield_code": SUB, "region": REG,
    "period_key": "後期ロマン主義（独・英・仏）",
    "definition": "ヴィクトリア朝のブラウニング・テニソンが完成させるドラマティック・モノローグの直接的先駆形式。ワーズワース「狂った母」、コールリッジ「老水夫の歌」の語り手の劇的構築、バイロン『マンフレッド』の独白形式が、抒情的「私」を歴史的・心理的「キャラクター」として劇化する技法を準備した。",
    "background": "ロマン主義抒情詩の主観性とシェイクスピア独白の融合的展開。",
    "development": "ブラウニング『男と女』『指輪と本』、テニソン『ユリシーズ』、エリオット『プルーフロック』、現代の独白詩学に連続。",
    "historical_context": "抒情と劇のジャンル境界の揺らぎとロマン主義主観性の歴史化。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/151",
    "primary_source_type": "Project Gutenberg — Coleridge Rime of the Ancient Mariner",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Relations (intra-Romantic conceptual links)
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    ("想像力（ロマン主義的）", "有機的形式",
     "influences",
     "想像力の能動的綜合作用が有機的形式として現象する。"),
    ("想像力（ロマン主義的）", "コールリッジ『文学的自伝』",
     "contains",
     "コールリッジの想像力論は『文学的自伝』第13章で集大成される。"),
    ("コールリッジ『文学的自伝』", "第一次想像力と第二次想像力",
     "contains",
     "第一次/第二次想像力区分は『文学的自伝』第13章の中核理論。"),
    ("コールリッジ『文学的自伝』", "空想と想像力",
     "contains",
     "空想と想像力の区分は『文学的自伝』第13章の核心理論。"),
    ("有機的形式", "有機的形式（コールリッジ）",
     "contains",
     "コールリッジ版有機的形式論は包括概念のロマン主義的定式化。"),
    ("ワーズワース『リリカル・バラッズ』序文", "自発的なあふれ出し（ワーズワース）",
     "contains",
     "「自発的なあふれ出し」定式は『リリカル・バラッズ』1800年序文の核心命題。"),
    ("シュトゥルム・ウント・ドラング", "個人天才",
     "contains",
     "シュトゥルム・ウント・ドラング期の天才崇拝（Geniekult）が個人天才概念を確立。"),
    ("シュトゥルム・ウント・ドラング", "ゲーテ『若きウェルテルの悩み』",
     "contains",
     "『ウェルテル』はシュトゥルム・ウント・ドラング期の代表作。"),
    ("シュトゥルム・ウント・ドラング", "前期ロマン主義と後期ロマン主義",
     "influences",
     "シュトゥルム・ウント・ドラングが独ロマン主義全体の母胎を成す。"),
    ("シュレーゲル兄弟のロマン主義理論", "進歩的普遍詩",
     "contains",
     "進歩的普遍詩構想はF. シュレーゲル『アテネーウム断章』116の中核命題。"),
    ("シュレーゲル兄弟のロマン主義理論", "ロマン主義的アイロニー",
     "contains",
     "ロマン主義的アイロニーはF. シュレーゲルの中心理論。"),
    ("シュレーゲル兄弟のロマン主義理論", "形式としての断片",
     "contains",
     "断片形式はシュレーゲル兄弟『アテネーウム断章』が範例化した詩形式。"),
    ("シュレーゲル兄弟のロマン主義理論", "有機的形式",
     "influences",
     "A.W.シュレーゲル『演劇芸術論』が有機的形式論をコールリッジに媒介。"),
    ("教養小説の成熟（『ヴィルヘルム・マイスター』）", "シュレーゲル兄弟のロマン主義理論",
     "influences",
     "F. シュレーゲルがマイスターをロマン主義の中心ジャンルとして理論化。"),
    ("メアリー・シェリー『フランケンシュタイン』", "ゴシック小説の成熟",
     "contains",
     "『フランケンシュタイン』はロマン主義期ゴシック小説の頂点を成す。"),
    ("中世復興", "ゴシック小説の成熟",
     "influences",
     "中世復興の城・廃墟趣味がゴシック小説の素材を提供。"),
    ("オシアン真贋論争", "中世復興",
     "influences",
     "オシアン詩流行が原始的・中世的詩想復興の起爆剤となった。"),
    ("オシアン真贋論争", "バラッド復興",
     "influences",
     "オシアンの「翻訳」形式がバラッド復興の発見的姿勢を準備した。"),
    ("バラッド復興", "ワーズワース『リリカル・バラッズ』序文",
     "influences",
     "バラッド復興運動が『リリカル・バラッズ』の理論化を直接準備。"),
    ("ゲーテ『若きウェルテルの悩み』", "メランコリー（ロマン主義的）",
     "influences",
     "『ウェルテル』が近代的憂鬱の文学的範例を確立した。"),
    ("シャトーブリアン『ルネ』", "メランコリー（ロマン主義的）",
     "extends",
     "『ルネ』が「世紀病」として独語圏ウェルテル系譜を仏に翻案・展開。"),
    ("バイロン的英雄", "エキゾチシズム",
     "influences",
     "バイロン『チャイルド・ハロルド』『東方物語群』がエキゾチシズム文学を確立。"),
    ("崇高（ロマン主義的）", "道徳的力としての自然",
     "influences",
     "崇高美学が自然を道徳的力として神聖化する詩学を支えた。"),
    ("ワーズワース『リリカル・バラッズ』序文", "道徳的力としての自然",
     "contains",
     "ワーズワースの自然観が道徳的力としての自然概念の中核を成す。"),
    ("キーツ「消極的能力」", "シェリー『詩の擁護』",
     "influences",
     "消極的能力の理念がシェリー詩論の想像力共感原理に影響。"),
    ("ユゴー『クロムウェル』序文", "ロマン主義対古典主義論争",
     "contains",
     "『クロムウェル』序文が仏ロマン主義対古典主義論争の宣言文書。"),
    ("ホフマンの幻想性", "ゴシック小説の成熟",
     "extends",
     "ホフマン幻想文学が独語圏ゴシック小説の中核を成す。"),
    ("ノヴァーリス『夜の讃歌』", "シュレーゲル兄弟のロマン主義理論",
     "contains",
     "ノヴァーリスはイェナ派同人として兄弟の理論実践を共同で担った。"),
    ("ロマン主義的アイロニー", "形式としての断片",
     "influences",
     "ロマン主義的アイロニーが断片形式の自己反省性を理論的に支える。"),
    ("ヴィジョナリー（幻視者）", "想像力（ロマン主義的）",
     "extends",
     "ヴィジョナリー詩人像はロマン主義的想像力の極限的形態を体現。"),
    ("コールリッジ『クブラ・カーン』とインスピレーション", "形式としての断片",
     "extends",
     "『クブラ・カーン』は断片形式の英国側範例として機能した。"),
    ("ドラマティック・モノローグの先駆", "後期ロマン主義（独・英・仏）",
     "contains",
     "ドラマティック・モノローグ先駆形式は後期ロマン主義詩の主要展開。"),
    ("個人天才", "ワーズワース『リリカル・バラッズ』序文",
     "influences",
     "ロマン主義的天才観が『リリカル・バラッズ』序文の詩人像を規定する。"),
    ("バイロン的英雄", "メアリー・シェリー『フランケンシュタイン』",
     "influences",
     "バイロン的英雄像がメアリー・シェリー創作環境（ジュネーヴ湖畔）を規定した。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave8_c07_romantic] inserting {len(CONCEPTS)} concepts...")
    if len(CONCEPTS) != 40:
        print(f"  WARNING: expected 40 concepts, got {len(CONCEPTS)}")

    name_to_id: dict[str, int] = {}
    fourth_count = 0
    cd_count = 0
    relation_count = 0

    with LitDB() as db:
        # 1) Seed periods
        period_ids: dict[str, int] = {}
        for name_ja, name_en, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=name_ja, region=REG,
                start_year=sy, end_year=ey,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"  period: {name_ja!r} -> id={pid}")

        # 2) Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            period_key = entry.pop("period_key", None)
            if period_key:
                entry["period_id"] = period_ids[period_key]

            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid

            for axis_entry in fourth_axes:
                db.tag_fourth_transform(cid, **axis_entry)
                fourth_count += 1

            for cd in cross_domain:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=cd["target_db"],
                    link_type=cd["link_type"],
                    target_entity_id=cd.get("target_entity_id"),
                    target_entity_name=cd.get("target_entity_name"),
                    description=cd.get("description"),
                )
                cd_count += 1

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r}"
                      f" (sid={sid}, tid={tid})")
                continue
            db.insert_relation(
                source_type="concept", source_id=sid,
                target_type="concept", target_id=tid,
                relation_type=rtype,
                description=desc,
                confidence=4,
            )
            relation_count += 1

        # 4) Summary
        summary = db.progress_summary()
        print()
        print("[wave8_c07_romantic] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  fourth_transform_tags (total): {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain (total): {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations (total): {summary['relations']} "
              f"(this run: +{relation_count})")

        # Subfield-4 specific count
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 4"
        ).fetchone()
        print(f"  concepts in subfield_id=4 (Enlightenment+Romanticism): {row['c']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
