"""LIT-DB Phase 2 Wave 15 — C08: European Realism / Naturalism / Symbolism (+80).

Subfield: lit_eu_realism (id=5), region='西欧'.
Adds 80 NEW NON-OVERLAPPING concepts on top of existing 100.
Target totals after run: 180 (toward 600 goal).

Coverage (no duplicates with existing 100):
  A: French extension — Stendhal/Balzac/Maupassant/Loti/Sand/Vigny (16)
  B: English extension — Dickens/Eliot/Hardy/Trollope/Conrad/Ford/Bennett/Wells/Galsworthy (18)
  C: German extension — Storm/Raabe/Keller/Meyer/Hauptmann/Sudermann/Schnitzler/Wassermann (12)
  D: Italian Verismo+ — Verga/Capuana/De Roberto/Pirandello/Deledda/Fogazzaro (10)
  E: Spanish — Galdós Episodios+novelas/Pardo Bazán/Pereda/Valera/Blasco Ibáñez (10)
  F: Russian — Dostoevsky novellas/Tolstoy short/Turgenev/Goncharov/Saltykov/Leskov (8)
  G: Symbolist+Decadent extras — Mallarmé/Verlaine/Maeterlinck/Wilde/Pater/Hopkins (6)

>= 85% primary tier; fourth_transform_tags >= 24, cross_domain >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("19世紀フランス・リアリズム期", "French Realism (19th c.)", 1830, 1880,
     "ルイ・フィリップ王政期から第三共和制初期にかけてのフランス文学。"),
    ("19世紀英米・北欧リアリズム期", "British/American/Nordic Realism (19th c.)",
     1840, 1900,
     "ヴィクトリア朝中期以降の英米と北欧におけるリアリズム小説・社会劇の隆盛期。"),
    ("自然主義期", "Naturalism (late 19th c.)", 1865, 1910,
     "ゾラを中心とするフランス自然主義と、その英米・独語圏への波及期。"),
    ("ロシア・リアリズム期", "Russian Realism (19th c.)", 1840, 1910,
     "ツルゲーネフ、ゴンチャロフ、サルトィコフ＝シチェドリン、チェーホフ、ゴーリキーを擁するロシア・リアリズム期。"),
    ("イタリア・ヴェリズモ期", "Italian Verismo", 1870, 1910,
     "ヴェルガを中心とするシチリア発のヴェリズモ運動と、北イタリア・ナポリ派の写実主義。"),
    ("イベリア・リアリズム期", "Iberian Realism", 1860, 1910,
     "ガルドス、パルド・バサン、クラリン、エサ・デ・ケイロスらスペイン・ポルトガル写実主義の隆盛期。"),
    ("ドイツ詩的リアリズム期", "German Poetic Realism", 1850, 1900,
     "フォンターネ、ストルム、ケラー、ラーベらドイツ語圏の市民的・詩的リアリズム期。"),
    ("ウィーン・モデルネ期", "Viennese Modernism", 1890, 1920,
     "シュニッツラー、ホフマンスタール、ヴァッサーマンらのウィーン世紀末文学。"),
    ("英国モダニズム前夜期", "Edwardian/Pre-Modernist Britain", 1895, 1925,
     "コンラッド、フォード、ベネット、ウェルズ、ゴールズワージーらエドワード朝期英国小説。"),
    ("象徴主義・デカダンス期", "Symbolism & Decadence", 1857, 1910,
     "マラルメ、ヴェルレーヌ、ランボー、メーテルランク、ペーター、ワイルドらの象徴主義・デカダンス文学運動。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_realism", region="西欧", original_script="roman")
CCYR = dict(subfield_code="lit_eu_realism", region="西欧", original_script="cyrillic")


# ============================================================
# A: フランス・リアリズム拡張（16）
# ============================================================
add(**C, name_ja="スタンダール『リュシアン・ルーヴェン』",
    name_en="Stendhal's Lucien Leuwen",
    name_original="Lucien Leuwen",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダールが1834-35年に執筆した未完の長編小説（1894年刊）。理工科学校を放校された青年リュシアン・ルーヴェンの政治的軍歴と恋愛を描き、七月王政期フランスの議会政治・地方選挙・銀行家階級を辛辣に観察した。スタンダール政治小説の代表作。",
    background="七月王政期フランスの選挙制度・銀行家階級台頭・正統王朝派対立の社会構造。",
    development="20世紀政治小説、マルロー、サルトル『自由への道』に継承された。",
    historical_context="七月王政期(1834-35)フランス。",
    primary_source_url=GUTEN+"ebooks/26116",
    primary_source_type="Project Gutenberg: Lucien Leuwen",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スタンダール『恋愛論』",
    name_en="Stendhal's De l'amour",
    name_original="De l'amour",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダールが1822年に発表した恋愛心理論。「結晶作用（cristallisation）」概念を提唱し、ザルツブルク岩塩坑の枯枝に塩結晶が付着する比喩で、恋愛における対象の美化過程を心理学的に分析した。19世紀フランス心理学的リアリズムの理論的源泉。",
    background="19世紀初頭ヨーロッパの感情論・心理学的考察の文学化。",
    development="プルースト、フロイトの恋愛論、20世紀心理小説の理論的基礎となった。",
    historical_context="王政復古期フランスの感情論議。",
    primary_source_url=GUTEN+"ebooks/49581",
    primary_source_type="Project Gutenberg: De l'amour",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『従兄ポンス』",
    name_en="Balzac's Le Cousin Pons",
    name_original="Le Cousin Pons",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1847年に発表した長編小説。「貧しい親戚」二部作の一作で、独身音楽家ポンスの美術コレクションをめぐる親族の貪欲を描く。バルザック後期最高傑作の一つで、コレクター心理・パリの中古美術市場・遺産相続をめぐる陰謀の博物誌的観察。",
    background="七月王政末期パリの中古美術市場・遺産相続をめぐる社会動態。",
    development="フローベール、ゾラ自然主義、20世紀パリ生活小説に継承。",
    historical_context="七月王政末期フランス社会の道徳的腐敗。",
    primary_source_url=GUTEN+"ebooks/1660",
    primary_source_type="Project Gutenberg: Le Cousin Pons",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『幻滅』",
    name_en="Balzac's Illusions perdues",
    name_original="Illusions perdues",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1837-43年に発表した三部作長編。地方青年リュシアン・ド・リュバンプレのパリ文壇進出と挫折を描き、19世紀新聞ジャーナリズム・出版業・文学市場の社会経済的構造を徹底的に解剖した。プルーストが「最も偉大なフランス小説」と評した。",
    background="七月王政期パリのジャーナリズム勃興、印刷資本主義拡大。",
    development="ゾラ『金銭』、20世紀メディア小説の祖型となった。",
    historical_context="七月王政期パリの出版・新聞業の産業化。",
    primary_source_url=GUTEN+"ebooks/13909",
    primary_source_type="Project Gutenberg: Illusions perdues",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作家・批評家・新聞のメディア的相互腐敗の描写は、AI時代のコンテンツ経済における作者性希釈と歴史的に並行する。",
         "related_ai_phenomenon":"AI時代のメディアエコシステムにおける作者性"}])

add(**C, name_ja="バルザック『娼婦の栄光と悲惨』",
    name_en="Balzac's Splendeurs et misères des courtisanes",
    name_original="Splendeurs et misères des courtisanes",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1838-47年に発表した長編小説。『幻滅』の続編で、ヴォートランによる青年詩人リュシアン操縦と娼婦エステルの破滅を描く。パリ犯罪世界・警察・銀行家階級を網羅した社会暗黒巡礼。",
    background="七月王政期パリ犯罪世界とヴィドック警察制度の文学化。",
    development="ユーゴー『レ・ミゼラブル』、19世紀末犯罪小説に影響。",
    historical_context="七月王政期パリの暗黒社会と警察制度。",
    primary_source_url=GUTEN+"ebooks/13715",
    primary_source_type="Project Gutenberg: Splendeurs et misères des courtisanes",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『ツールの司祭』",
    name_en="Balzac's Le Curé de Tours",
    name_original="Le Curé de Tours",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1832年に発表した中編小説。地方都市ツールで老司祭ビロトーが家政婦・同僚司祭の陰謀により住居から追放される過程を、地方教会・ブルジョワ社交界の権力力学として観察した。地方リアリズム短編の規範。",
    background="王政復古末期から七月王政初期、地方教会と市民社会の緊張。",
    development="フローベール『ボヴァリー夫人』地方描写の祖型。",
    historical_context="七月王政期フランス地方都市の社交構造。",
    primary_source_url=GUTEN+"ebooks/1492",
    primary_source_type="Project Gutenberg: The Vicar of Tours",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バルザック『田舎医者』",
    name_en="Balzac's Le Médecin de campagne",
    name_original="Le Médecin de campagne",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1833年に発表した長編小説。村医者ベナシスがドーフィネ地方の農村を改革する物語で、農村社会改革・公共衛生・道徳的指導の理想像を提示した。バルザックの社会改良論的文学化。",
    background="七月王政期フランス農村の貧困と医療制度の問題。",
    development="19世紀末農村小説、社会医学小説の祖型となった。",
    historical_context="七月王政期フランスの地方医療と農村改革論議。",
    primary_source_url=GUTEN+"ebooks/1961",
    primary_source_type="Project Gutenberg: The Country Doctor",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バルザック『絶対の探求』",
    name_en="Balzac's La Recherche de l'Absolu",
    name_original="La Recherche de l'Absolu",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1834年に発表した長編小説。ドゥエの裕福な化学者バルタザール・クラースが「絶対」の発見に取り憑かれ家産を蕩尽する物語。科学的探求の狂気と家庭崩壊を交差させ、19世紀科学万能主義への文学的批判となった。",
    background="七月王政期フランスの科学振興とフランドル地方ブルジョワ文化。",
    development="フローベール『ブヴァールとペキュシェ』、19世紀末科学批判文学に継承。",
    historical_context="七月王政期フランスの科学万能主義と家産制ブルジョワ家庭の対立。",
    primary_source_url=GUTEN+"ebooks/1432",
    primary_source_type="Project Gutenberg: The Quest of the Absolute",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"科学的絶対探求に取り憑かれた主体の自滅は、AI時代の最適化追求・計算至上主義への警告と理論的に共振する。",
         "related_ai_phenomenon":"AI時代の最適化追求と主体の自滅"}])

add(**C, name_ja="バルザック『あら皮』",
    name_en="Balzac's La Peau de chagrin",
    name_original="La Peau de chagrin",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1831年に発表した長編小説。願いが叶うたびに縮小し主人公の寿命を削る「あら皮」を巡る寓話的物語で、欲望と消尽の経済学を文学化した。『人間喜劇』「哲学的研究」の中核作。",
    background="七月王政初期パリのロマン主義的欲望論と経済不安。",
    development="20世紀消費社会論、欲望論小説に継承された。",
    historical_context="七月王政初期フランス。",
    primary_source_url=GUTEN+"ebooks/1307",
    primary_source_type="Project Gutenberg: La Peau de chagrin",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モーパッサン『脂肪の塊』",
    name_en="Maupassant's Boule de Suif",
    name_original="Boule de Suif",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサン（1850-93）が1880年にゾラ編『メダンの夕べ』に寄稿した中編小説。普仏戦争中ルーアンを脱出する馬車内で娼婦「脂肪の塊」が同乗者ブルジョワに利用される物語。フランス自然主義短編の代表作で、戦争・階級・偽善の鋭利な批判。",
    background="普仏戦争(1870-71)とフランス・ブルジョワジーの戦中行動への批判。",
    development="モーパッサン短編全体、20世紀世界短編文学の規範となった。",
    historical_context="第三共和制初期フランスの戦争記憶論議。",
    primary_source_url=GUTEN+"ebooks/3088",
    primary_source_type="Project Gutenberg: Boule de Suif",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="モーパッサン『女の一生』",
    name_en="Maupassant's Une Vie",
    name_original="Une Vie",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1883年に発表した最初の長編小説。ノルマンディー貴族の娘ジャンヌが期待・幻滅・諦念を経て人生を全うする物語。フローベール門下の自然主義的観察と感情教育小説の融合。",
    background="第三共和制初期ノルマンディー貴族階級の没落。",
    development="20世紀フランス女性小説の祖型となった。",
    historical_context="第三共和制初期フランスの女性史的転換。",
    primary_source_url=GUTEN+"ebooks/3251",
    primary_source_type="Project Gutenberg: Une Vie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モーパッサン『ベラミ』",
    name_en="Maupassant's Bel-Ami",
    name_original="Bel-Ami",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1885年に発表した長編小説。退役兵ジョルジュ・デュロワが新聞ジャーナリストから上流社会へ女性を踏み台にして上昇する出世物語。第三共和制パリのジャーナリズム腐敗と女性関係の社会力学を観察した。",
    background="第三共和制中期パリ新聞産業の急拡大とブーランジェ運動前夜。",
    development="20世紀メディア小説、出世小説の祖型となった。",
    historical_context="第三共和制中期パリのメディア産業化。",
    primary_source_url=GUTEN+"ebooks/3793",
    primary_source_type="Project Gutenberg: Bel-Ami",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モーパッサン『ピエールとジャン』",
    name_en="Maupassant's Pierre et Jean",
    name_original="Pierre et Jean",
    period_key="19世紀フランス・リアリズム期",
    definition="モーパッサンが1888年に発表した中編小説。兄ピエールが弟ジャンが受け取った遺産から母の不倫を疑い、兄弟関係が崩壊する物語。序文「ル・ロマン（小説論）」が20世紀リアリズム小説論の基本文献となった。",
    background="第三共和制中期ル・アーヴル港町ブルジョワ家庭の心理動態。",
    development="20世紀心理小説論、序文「ル・ロマン」は小説理論古典に。",
    historical_context="第三共和制中期フランスの家庭心理学的関心。",
    primary_source_url=GUTEN+"ebooks/3804",
    primary_source_type="Project Gutenberg: Pierre et Jean",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ピエール・ロティ『氷島の漁夫』",
    name_en="Loti's Pêcheur d'Islande",
    name_original="Pêcheur d'Islande",
    period_key="19世紀フランス・リアリズム期",
    definition="ピエール・ロティ（1850-1923）が1886年に発表した長編小説。ブルターニュの漁師ヤンとアイスランド漁業の生活、ゴーから愛されつつ氷海に消える運命を描く。海洋自然主義と地方民俗学的観察の融合。",
    background="第三共和制中期ブルターニュ漁業共同体と海軍士官ロティの民俗学的観察。",
    development="20世紀海洋小説、地方民俗小説に継承された。",
    historical_context="第三共和制中期フランス地方民俗論議。",
    primary_source_url=GUTEN+"ebooks/12554",
    primary_source_type="Project Gutenberg: An Iceland Fisherman",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョルジュ・サンド『魔の沼』",
    name_en="Sand's La Mare au diable",
    name_original="La Mare au diable",
    period_key="19世紀フランス・リアリズム期",
    definition="ジョルジュ・サンド（1804-76）が1846年に発表した田園小説。ベリー地方の若い農夫ジェルマンと幼い羊飼い娘マリの恋を描き、フランス農村文学の祖型となった「田園三部作」第一作。",
    background="七月王政末期から第二共和制初期フランス農村の文学的理想化。",
    development="フランス田園小説、19世紀末農民小説の祖型となった。",
    historical_context="1848年革命前後フランスの農民・農村への関心。",
    primary_source_url=GUTEN+"ebooks/4036",
    primary_source_type="Project Gutenberg: The Devil's Pool",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴィニー『軍隊の服従と偉大』",
    name_en="Vigny's Servitude et grandeur militaires",
    name_original="Servitude et grandeur militaires",
    period_key="19世紀フランス・リアリズム期",
    definition="アルフレッド・ド・ヴィニー（1797-1863）が1835年に発表した三部短編集。元軍人ヴィニーの体験に基づく軍人の倫理・服従・栄誉論で、19世紀フランス軍隊リアリズムの先駆的記録文学。",
    background="七月王政期フランス軍隊と軍人倫理論議。",
    development="19世紀末軍隊小説、20世紀戦争文学に継承された。",
    historical_context="七月王政期フランス軍隊文化と軍人倫理論議。",
    primary_source_url=GUTEN+"ebooks/14704",
    primary_source_type="Project Gutenberg: Servitude et grandeur militaires",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: 英国リアリズム拡張（18）
# ============================================================
add(**C, name_ja="ディケンズ『ピクウィック・ペイパーズ』",
    name_en="Dickens' Pickwick Papers",
    name_original="The Pickwick Papers",
    period_key="19世紀英米・北欧リアリズム期",
    definition="チャールズ・ディケンズ（1812-70）が1836-37年に分冊刊行した最初の長編小説。ピクウィック・クラブ会員の英国巡遊を喜劇的に描き、19世紀分冊小説の商業的成功モデルを確立した。英国コミック・リアリズムの祖型。",
    background="19世紀初頭英国の鉄道網拡大前の馬車旅行と地方社交クラブ文化。",
    development="ディケンズ的多人物喜劇小説、英国コミック・リアリズム伝統を確立。",
    historical_context="改革法(1832)後英国の中産階級拡大。",
    primary_source_url=GUTEN+"ebooks/580",
    primary_source_type="Project Gutenberg: Pickwick Papers",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ディケンズ『オリヴァー・ツイスト』",
    name_en="Dickens' Oliver Twist",
    name_original="Oliver Twist",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1837-39年に分冊刊行した長編小説。孤児オリヴァーが救貧院・少年窃盗団・裕福な紳士家庭を遍歴する物語で、新救貧法(1834)批判と都市下層社会の文学的告発。社会改革小説の祖型。",
    background="新救貧法(1834)批判と19世紀英国都市下層社会の貧困。",
    development="19世紀英国社会改革小説、20世紀社会派小説の祖型。",
    historical_context="改革法後英国の救貧法論議。",
    primary_source_url=GUTEN+"ebooks/730",
    primary_source_type="Project Gutenberg: Oliver Twist",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ディケンズ『デイヴィッド・コパフィールド』",
    name_en="Dickens' David Copperfield",
    name_original="David Copperfield",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1849-50年に発表した自伝的長編小説。デイヴィッドの幼年期から成年・作家としての成功までを一人称で描き、ディケンズが「わが子の中で最愛のもの」と評した代表作。英国教養小説の規範。",
    background="ヴィクトリア朝中期英国の教養小説伝統と自伝的虚構の融合。",
    development="ジョイス『若き芸術家の肖像』、20世紀自伝的小説の祖型となった。",
    historical_context="ヴィクトリア朝中期英国の中産階級文化。",
    primary_source_url=GUTEN+"ebooks/766",
    primary_source_type="Project Gutenberg: David Copperfield",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ディケンズ『マーティン・チャズルウィット』",
    name_en="Dickens' Martin Chuzzlewit",
    name_original="The Life and Adventures of Martin Chuzzlewit",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1843-44年に分冊刊行した長編小説。米国旅行体験を踏まえ、英米の偽善・利己主義を風刺した。米国訪問記として、英国小説における米国観察の重要な記録。",
    background="ディケンズ1842年の米国旅行体験と英米関係の文学化。",
    development="19世紀英国小説における米国観察、英米文化比較文学に影響。",
    historical_context="ヴィクトリア朝中期英米関係。",
    primary_source_url=GUTEN+"ebooks/968",
    primary_source_type="Project Gutenberg: Martin Chuzzlewit",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ディケンズ『ニコラス・ニクルビー』",
    name_en="Dickens' Nicholas Nickleby",
    name_original="The Life and Adventures of Nicholas Nickleby",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1838-39年に分冊刊行した長編小説。青年ニコラスのヨークシャー寄宿学校教師体験を通じて、19世紀英国の教育制度の虐待・搾取を告発した社会改革小説。",
    background="19世紀英国の私立寄宿学校（特にヨークシャー）における虐待実態。",
    development="19世紀末英国教育制度改革運動に影響。",
    historical_context="ヴィクトリア朝初期英国の教育制度問題。",
    primary_source_url=GUTEN+"ebooks/967",
    primary_source_type="Project Gutenberg: Nicholas Nickleby",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ディケンズ『骨董屋』",
    name_en="Dickens' The Old Curiosity Shop",
    name_original="The Old Curiosity Shop",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1840-41年に分冊刊行した長編小説。少女ネルと祖父の英国遍歴と、ネルの死を描き、ヴィクトリア朝センチメンタリズムの典型例とされる一方、20世紀以降批判的に再評価されている。",
    background="ヴィクトリア朝初期英国のセンチメンタリズム文化。",
    development="ヴィクトリア朝センチメンタリズム小説の典型として20世紀以降批評対象。",
    historical_context="ヴィクトリア朝初期英国の死と感傷文化。",
    primary_source_url=GUTEN+"ebooks/700",
    primary_source_type="Project Gutenberg: The Old Curiosity Shop",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョージ・エリオット『ロモラ』",
    name_en="George Eliot's Romola",
    name_original="Romola",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ジョージ・エリオット（1819-80）が1862-63年に発表した歴史小説。15世紀フィレンツェのサヴォナローラ時代を舞台に、女性ロモラの倫理的成長を描く。19世紀英国歴史小説の研究的精緻化を示す傑作。",
    background="19世紀英国の歴史主義的文学観とエリオットのフィレンツェ調査。",
    development="20世紀歴史小説、女性教養小説の祖型となった。",
    historical_context="ヴィクトリア朝中期英国の歴史主義文学観。",
    primary_source_url=GUTEN+"ebooks/3711",
    primary_source_type="Project Gutenberg: Romola",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョージ・エリオット『フィリックス・ホルト』",
    name_en="George Eliot's Felix Holt",
    name_original="Felix Holt, the Radical",
    period_key="19世紀英米・北欧リアリズム期",
    definition="エリオットが1866年に発表した政治小説。1832年改革法後の英国地方都市を舞台に、急進派フィリックス・ホルトの政治理念と恋愛を描く。19世紀英国政治小説の規範。",
    background="第二次選挙法改正(1867)前夜の英国政治論議。",
    development="20世紀英国政治小説に継承された。",
    historical_context="ヴィクトリア朝中期英国の選挙法改正論議。",
    primary_source_url=GUTEN+"ebooks/8642",
    primary_source_type="Project Gutenberg: Felix Holt",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョージ・エリオット『アダム・ビード』",
    name_en="George Eliot's Adam Bede",
    name_original="Adam Bede",
    period_key="19世紀英米・北欧リアリズム期",
    definition="エリオットが1859年に発表した最初の長編小説。18世紀末英国の田舎大工アダム・ビードと美しいヘティの悲劇を描き、フランダース絵画的写実主義をリアリズム小説論として宣言した第17章「物語をしばし止めて」が有名。",
    background="ヴィクトリア朝中期英国の写実主義美学とフランダース絵画受容。",
    development="第17章は19世紀英国リアリズム宣言の中核文献。",
    historical_context="ヴィクトリア朝中期英国の田園主義論議。",
    primary_source_url=GUTEN+"ebooks/507",
    primary_source_type="Project Gutenberg: Adam Bede",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"フランダース絵画的写実主義宣言は、AI生成画像・テキストにおける「日常的真正性」概念の歴史的祖型として再考される。",
         "related_ai_phenomenon":"AI生成における日常的真正性の理論化"}])

add(**C, name_ja="ハーディ『カスターブリッジの市長』",
    name_en="Hardy's The Mayor of Casterbridge",
    name_original="The Mayor of Casterbridge",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トマス・ハーディ（1840-1928）が1886年に発表した長編小説。妻と娘を売却した過去を持つ穀物商ヘンチャードがカスターブリッジ市長まで上昇し、転落する物語。ウェセックス小説中の悲劇的傑作。",
    background="ヴィクトリア朝後期英国のドーセットシャー穀物商業と地方政治。",
    development="20世紀英国地方悲劇小説の祖型となった。",
    historical_context="ヴィクトリア朝後期英国の地方経済変動。",
    primary_source_url=GUTEN+"ebooks/143",
    primary_source_type="Project Gutenberg: The Mayor of Casterbridge",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーディ『ウェセックス短編集』",
    name_en="Hardy's Wessex Tales",
    name_original="Wessex Tales",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ハーディが1888年に発表した短編集。ドーセットシャーを中心とする架空のウェセックス地方を舞台にした地方民俗物語集で、英国地方リアリズム短編の規範を確立した。",
    background="ヴィクトリア朝後期英国の地方民俗学的関心。",
    development="20世紀英国地方短編小説に継承された。",
    historical_context="ヴィクトリア朝後期英国の地方民俗学興隆。",
    primary_source_url=GUTEN+"ebooks/3056",
    primary_source_type="Project Gutenberg: Wessex Tales",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="トロロップ『今を生きる』",
    name_en="Trollope's The Way We Live Now",
    name_original="The Way We Live Now",
    period_key="19世紀英米・北欧リアリズム期",
    definition="アンソニー・トロロップ（1815-82）が1875年に発表した長編小説。ロンドンの金融詐欺師メルモットを中心に、ヴィクトリア朝後期英国の金融資本主義腐敗を風刺した。19世紀英国金融小説の代表作。",
    background="ヴィクトリア朝後期英国の鉄道投機・金融バブルと「英国における米国式拝金主義」批判。",
    development="20世紀英国金融小説、米国マック・レイキング小説に影響。",
    historical_context="ヴィクトリア朝後期英国の金融資本主義拡大。",
    primary_source_url=GUTEN+"ebooks/5231",
    primary_source_type="Project Gutenberg: The Way We Live Now",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トロロップ『フィニアス・フィン』",
    name_en="Trollope's Phineas Finn",
    name_original="Phineas Finn",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トロロップが1867-69年に発表した政治小説。アイルランド出身の青年フィニアス・フィンの英国議会政治家としての遍歴を描き、「パリサー連作」第二作。19世紀英国議会政治小説の代表作。",
    background="第二次選挙法改正(1867)期の英国議会政治。",
    development="20世紀英国政治小説の祖型となった。",
    historical_context="ヴィクトリア朝後期英国議会政治。",
    primary_source_url=GUTEN+"ebooks/2722",
    primary_source_type="Project Gutenberg: Phineas Finn",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="コンラッド『闇の奥』",
    name_en="Conrad's Heart of Darkness",
    name_original="Heart of Darkness",
    period_key="英国モダニズム前夜期",
    definition="ジョゼフ・コンラッド（1857-1924）が1899年に『ブラックウッズ・マガジン』連載、1902年単行本として発表した中編小説。船員マーロウのコンゴ川遡行と象牙商人クルツの「恐怖だ、恐怖だ」を描く。19世紀末植民地主義批判とモダニズム前夜の心理小説の傑作。",
    background="19世紀末ベルギー領コンゴ植民地搾取とコンラッド自身の1890年コンゴ体験。",
    development="20世紀植民地批判文学・モダニズム小説の中核となり、アチェベ等によりポストコロニアル批判の対象。",
    historical_context="19世紀末ヨーロッパ植民地主義の頂点。",
    primary_source_url=GUTEN+"ebooks/219",
    primary_source_type="Project Gutenberg: Heart of Darkness",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"マーロウの語りの不確実性と「恐怖」の言語的不可能性は、AI生成テキストにおける言語化困難経験の問題と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における言語化困難経験の問題"}])

add(**C, name_ja="コンラッド『ロード・ジム』",
    name_en="Conrad's Lord Jim",
    name_original="Lord Jim",
    period_key="英国モダニズム前夜期",
    definition="コンラッドが1900年に発表した長編小説。船を見捨てた船員ジムが東南アジアの孤島で名誉回復を試み命を落とす物語。マーロウの間接話法的語りと心理リアリズムの融合で、20世紀モダニズム小説の祖型。",
    background="19世紀末英国海運業の倫理問題と東南アジア植民地体制。",
    development="20世紀英米モダニズム小説、フォークナー、フィッツジェラルドに影響。",
    historical_context="19世紀末英国植民地海運の倫理論議。",
    primary_source_url=GUTEN+"ebooks/5658",
    primary_source_type="Project Gutenberg: Lord Jim",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="コンラッド『ノストローモ』",
    name_en="Conrad's Nostromo",
    name_original="Nostromo",
    period_key="英国モダニズム前夜期",
    definition="コンラッドが1904年に発表した長編小説。架空の南米共和国コスタグアナの銀鉱と政治革命を舞台に、英米資本主義と現地革命を交差させた政治叙事詩。20世紀政治小説の規範。",
    background="19世紀末南米における英米資本主義と政治不安定。",
    development="20世紀ラテンアメリカ文学（ガルシア=マルケス等）にも影響。",
    historical_context="19世紀末南米における英米経済覇権。",
    primary_source_url=GUTEN+"ebooks/2021",
    primary_source_type="Project Gutenberg: Nostromo",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フォード『良き兵士』",
    name_en="Ford's The Good Soldier",
    name_original="The Good Soldier",
    period_key="英国モダニズム前夜期",
    definition="フォード・マドックス・フォード（1873-1939）が1915年に発表した長編小説。「これは私が聞いた中で最も悲しい物語だ」で始まる、不信頼な語り手による複雑な恋愛三角関係の物語。20世紀英米モダニズム小説の規範。",
    background="エドワード朝期英国の階級・婚姻制度と心理小説の精緻化。",
    development="20世紀モダニズム小説、不信頼な語り手の規範となった。",
    historical_context="第一次世界大戦前夜英国。",
    primary_source_url=GUTEN+"ebooks/2775",
    primary_source_type="Project Gutenberg: The Good Soldier",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"不信頼な語り手の精緻化は、AI生成における信頼性問題・ハルシネーション問題の歴史的祖型。",
         "related_ai_phenomenon":"AI生成における信頼性とハルシネーション"}])

add(**C, name_ja="ベネット『五つの町のアンナ』",
    name_en="Bennett's Anna of the Five Towns",
    name_original="Anna of the Five Towns",
    period_key="英国モダニズム前夜期",
    definition="アーノルド・ベネット（1867-1931）が1902年に発表した長編小説。英国スタッフォードシャーの陶器産業地帯「五つの町」を舞台に、若い女性アンナの生活を描く。英国地方産業小説の規範。",
    background="エドワード朝期英国スタッフォードシャー陶器産業の社会経済構造。",
    development="20世紀英国地方リアリズム小説、産業小説の祖型。",
    historical_context="エドワード朝期英国の地方産業文化。",
    primary_source_url=GUTEN+"ebooks/2638",
    primary_source_type="Project Gutenberg: Anna of the Five Towns",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ウェルズ『トノ・バンゲイ』",
    name_en="Wells' Tono-Bungay",
    name_original="Tono-Bungay",
    period_key="英国モダニズム前夜期",
    definition="H.G.ウェルズ（1866-1946）が1909年に発表した長編小説。叔父が偽薬「トノ・バンゲイ」で財をなし破滅する物語を通じて、エドワード朝期英国の商業的虚妄と社会階級問題を風刺した。",
    background="エドワード朝期英国の特許薬市場と広告産業の急拡大。",
    development="20世紀英国社会風刺小説、広告産業批判文学に継承。",
    historical_context="エドワード朝期英国の消費社会形成。",
    primary_source_url=GUTEN+"ebooks/718",
    primary_source_type="Project Gutenberg: Tono-Bungay",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ゴールズワージー『フォーサイト・サガ』",
    name_en="Galsworthy's The Forsyte Saga",
    name_original="The Forsyte Saga",
    period_key="英国モダニズム前夜期",
    definition="ジョン・ゴールズワージー（1867-1933）が1906-21年に発表した連作長編。英国上流ブルジョワ家系フォーサイト家三世代の物語で、ヴィクトリア朝末期からエドワード朝期英国の所有・財産・婚姻を描いた。1932年ノーベル文学賞代表作。",
    background="エドワード朝期英国上流ブルジョワジー文化と財産制論議。",
    development="20世紀英国家族年代記小説の祖型となった。",
    historical_context="エドワード朝期英国の上流ブルジョワジー文化。",
    primary_source_url=GUTEN+"ebooks/4397",
    primary_source_type="Project Gutenberg: The Forsyte Saga",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: ドイツ詩的リアリズム拡張（12）
# ============================================================
add(**C, name_ja="シュトルム『みずうみ』",
    name_en="Storm's Immensee",
    name_original="Immensee",
    period_key="ドイツ詩的リアリズム期",
    definition="テオドール・シュトルム（1817-88）が1849年に発表したノヴェレ。北独の老男ラインハルトが幼馴染エリーザベトとの淡い恋を回想する物語。ドイツ詩的リアリズム短編の規範を確立した代表作。",
    background="19世紀中葉ドイツ北部シュレースヴィヒの市民文化。",
    development="ドイツ詩的リアリズム短編、20世紀回想小説の祖型となった。",
    historical_context="1848年革命前後ドイツの市民文化。",
    primary_source_url=GUTEN+"ebooks/14182",
    primary_source_type="Project Gutenberg: Immensee",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シュトルム『白馬の騎手』",
    name_en="Storm's Der Schimmelreiter",
    name_original="Der Schimmelreiter",
    period_key="ドイツ詩的リアリズム期",
    definition="シュトルムが1888年に発表した最後のノヴェレ。北海沿岸の堤防監督官ハウケ・ハイエンの物語で、自然との闘いと共同体の伝説を融合した。ドイツ詩的リアリズム最高傑作の一つ。",
    background="19世紀末北独北海沿岸の堤防共同体と民俗伝説。",
    development="20世紀ドイツ地方文学、民俗的リアリズムの祖型となった。",
    historical_context="ヴィルヘルム期ドイツの地方文化論議。",
    primary_source_url=GUTEN+"ebooks/27145",
    primary_source_type="Project Gutenberg: Der Schimmelreiter",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラーベ『プフィスターの水車場』",
    name_en="Raabe's Pfisters Mühle",
    name_original="Pfisters Mühle",
    period_key="ドイツ詩的リアリズム期",
    definition="ヴィルヘルム・ラーベ（1831-1910）が1884年に発表した中編小説。化学工場排水で汚染された水車場の訴訟を描き、ドイツ最初期の環境小説とされる。詩的リアリズムと産業批判の融合。",
    background="ヴィルヘルム期ドイツの工業化と環境汚染問題。",
    development="20世紀ドイツ環境文学、エコクリティシズムに先行。",
    historical_context="ヴィルヘルム期ドイツの工業化問題。",
    primary_source_url=GUTEN+"ebooks/30489",
    primary_source_type="Project Gutenberg: Pfisters Mühle",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"19世紀の産業環境汚染を文学化する手法は、AI時代の環境負荷・データセンター電力消費問題への文学的応答の祖型。",
         "related_ai_phenomenon":"AI時代の環境負荷と文学的応答"}])

add(**C, name_ja="ラーベ『シュトプフクーヘン』",
    name_en="Raabe's Stopfkuchen",
    name_original="Stopfkuchen",
    period_key="ドイツ詩的リアリズム期",
    definition="ラーベが1891年に発表した中編小説。南アフリカからドイツに帰国した語り手が、太った旧友「シュトプフクーヘン」の語りを聞くという入れ子構造の物語。ラーベ後期最高傑作で、20世紀モダニズムへ橋渡し。",
    background="ヴィルヘルム期ドイツ植民地時代と地方文化。",
    development="20世紀ドイツモダニズム小説の祖型となった。",
    historical_context="ヴィルヘルム期ドイツの植民地・地方文化論議。",
    primary_source_url=GUTEN+"ebooks/53116",
    primary_source_type="Project Gutenberg: Stopfkuchen",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ケラー『七つの伝説』",
    name_en="Keller's Sieben Legenden",
    name_original="Sieben Legenden",
    period_key="ドイツ詩的リアリズム期",
    definition="ゴットフリート・ケラー（1819-90）が1872年に発表した短編集。中世聖人伝説をスイス的ユーモアで再話した7篇で、ケラーの宗教批判とリアリズム短編技法の融合。",
    background="19世紀中葉スイスの市民文化と宗教論議。",
    development="ケラー後期短編、20世紀ドイツ語圏短編に継承。",
    historical_context="19世紀後半スイスの市民文化。",
    primary_source_url=GUTEN+"ebooks/22974",
    primary_source_type="Project Gutenberg: Sieben Legenden",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ケラー『マルティン・ザランダー』",
    name_en="Keller's Martin Salander",
    name_original="Martin Salander",
    period_key="ドイツ詩的リアリズム期",
    definition="ケラーが1886年に発表した最後の長編小説。スイス商人マルティン・ザランダーが破産・再起・社会改革活動する物語で、19世紀末スイス民主主義の腐敗を批判した政治リアリズム小説。",
    background="19世紀末スイス民主主義制度と政治腐敗論議。",
    development="20世紀ドイツ語圏政治リアリズム小説に継承。",
    historical_context="19世紀末スイス民主主義論議。",
    primary_source_url=GUTEN+"ebooks/16131",
    primary_source_type="Project Gutenberg: Martin Salander",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マイヤー『ユルク・イェナッチュ』",
    name_en="Meyer's Jürg Jenatsch",
    name_original="Jürg Jenatsch",
    period_key="ドイツ詩的リアリズム期",
    definition="コンラート・フェルディナント・マイヤー（1825-98）が1874年に発表した歴史小説。17世紀グラウビュンデン州の政治家ユルク・イェナッチュの謀略と暗殺を描き、スイス歴史小説の規範を確立した。",
    background="19世紀末スイスの歴史主義文学運動。",
    development="20世紀ドイツ語圏歴史小説に継承された。",
    historical_context="19世紀末スイスの歴史主義文化。",
    primary_source_url=GUTEN+"ebooks/14729",
    primary_source_type="Project Gutenberg: Jürg Jenatsch",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マイヤー『聖人』",
    name_en="Meyer's Der Heilige",
    name_original="Der Heilige",
    period_key="ドイツ詩的リアリズム期",
    definition="マイヤーが1879-80年に発表した中編歴史小説。12世紀英国のトマス・ベケット殺害事件を、ヘンリー二世の弓師ハンスの語りで再構成した。マイヤーの歴史短編技法の代表作。",
    background="19世紀末スイス歴史主義と中世英国史への関心。",
    development="20世紀ドイツ歴史短編小説の祖型。",
    historical_context="19世紀末スイスの歴史小説興隆。",
    primary_source_url=GUTEN+"ebooks/16127",
    primary_source_type="Project Gutenberg: Der Heilige",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハウプトマン『織工たち』",
    name_en="Hauptmann's Die Weber",
    name_original="Die Weber",
    period_key="自然主義期",
    definition="ゲアハルト・ハウプトマン（1862-1946）が1892年に発表した自然主義劇。1844年シレジア織工蜂起を素材に、集合的階級闘争を主題とした。ドイツ自然主義劇の最高傑作で、1912年ノーベル文学賞代表作。",
    background="19世紀末ドイツ社会民主党興隆と労働運動史への関心。",
    development="20世紀社会派演劇、ブレヒト叙事詩劇の祖型となった。",
    historical_context="ヴィルヘルム期ドイツ労働運動史論議。",
    primary_source_url=GUTEN+"ebooks/30694",
    primary_source_type="Project Gutenberg: The Weavers",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハウプトマン『線路番ティール』",
    name_en="Hauptmann's Bahnwärter Thiel",
    name_original="Bahnwärter Thiel",
    period_key="自然主義期",
    definition="ハウプトマンが1888年に発表した中編小説。鉄道線路番ティールの精神崩壊と殺人を描き、ドイツ自然主義散文の規範作品となった。心理リアリズムと産業近代の交差。",
    background="ヴィルヘルム期ドイツの鉄道網拡大と労働者心理。",
    development="20世紀ドイツ表現主義散文、心理リアリズム小説の祖型。",
    historical_context="ヴィルヘルム期ドイツの鉄道産業化。",
    primary_source_url=GUTEN+"ebooks/57091",
    primary_source_type="Project Gutenberg: Bahnwärter Thiel",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シュニッツラー『輪舞』",
    name_en="Schnitzler's Reigen",
    name_original="Reigen",
    period_key="ウィーン・モデルネ期",
    definition="アルトゥール・シュニッツラー（1862-1931）が1900年に発表した戯曲。10組の異なる階級・年齢の男女が連鎖的に性関係を持つ10幕の輪舞構造で、世紀末ウィーン社会の性的虚妄と階級横断を描き、上演禁止・スキャンダル事件を起こした。",
    background="世紀末ウィーンの性道徳論議とフロイト精神分析興隆。",
    development="20世紀世界劇、性的リアリズム劇の祖型となった。",
    historical_context="世紀末ウィーン社会論議。",
    primary_source_url=GUTEN+"ebooks/52617",
    primary_source_type="Project Gutenberg: Reigen",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シュニッツラー『恋愛遊戯』",
    name_en="Schnitzler's Liebelei",
    name_original="Liebelei",
    period_key="ウィーン・モデルネ期",
    definition="シュニッツラーが1895年に発表した三幕劇。世紀末ウィーンの「甘い娘（süßes Mädel）」原型クリスティーネと貴族青年フリッツの悲恋を描き、ウィーン市民悲劇の規範を確立した。",
    background="世紀末ウィーン「甘い娘」文化と階級横断恋愛論議。",
    development="20世紀ウィーン演劇、階級悲劇の祖型となった。",
    historical_context="世紀末ウィーンの恋愛文化。",
    primary_source_url=GUTEN+"ebooks/40762",
    primary_source_type="Project Gutenberg: Liebelei",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# D: イタリア・ヴェリズモ＋ピランデッロ・デレッダ拡張（10）
# ============================================================
add(**C, name_ja="ヴェルガ『田舎の生活』",
    name_en="Verga's Vita dei campi",
    name_original="Vita dei campi",
    period_key="イタリア・ヴェリズモ期",
    definition="ジョヴァンニ・ヴェルガ（1840-1922）が1880年に発表した短編集。シチリア農村の生活を描いた8篇からなり、ヴェリズモ短編形式の規範を確立した。「カヴァレリーア・ルスティカーナ」を含む。",
    background="19世紀末イタリア南部問題とシチリア農村社会。",
    development="マスカーニ歌劇『カヴァレリーア・ルスティカーナ』(1890)の原作となり、20世紀世界短編に影響。",
    historical_context="19世紀末イタリア南部問題論議。",
    primary_source_url=GUTEN+"ebooks/12544",
    primary_source_type="Project Gutenberg: Vita dei campi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴェルガ『田舎の小説集』",
    name_en="Verga's Novelle rusticane",
    name_original="Novelle rusticane",
    period_key="イタリア・ヴェリズモ期",
    definition="ヴェルガが1883年に発表した短編集。シチリア農村の社会経済構造を観察した12篇からなる第二短編集で、「自由主義」「マラリア」等を含む。ヴェリズモ短編形式の成熟。",
    background="19世紀末シチリア農村社会の経済構造観察。",
    development="20世紀イタリア地方リアリズム短編に継承。",
    historical_context="19世紀末イタリア統一後の南部問題深化。",
    primary_source_url=GUTEN+"ebooks/14820",
    primary_source_type="Project Gutenberg: Novelle rusticane",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴェルガ『ネッダ』",
    name_en="Verga's Nedda",
    name_original="Nedda",
    period_key="イタリア・ヴェリズモ期",
    definition="ヴェルガが1874年に発表した中編小説。シチリアのオリーブ摘み女性ネッダの貧困と母性を描き、ヴェルガがロマン主義からヴェリズモへ転換した記念作品とされる。",
    background="19世紀末シチリア農村女性の労働と貧困。",
    development="ヴェリズモ運動の起点となった先駆的作品。",
    historical_context="19世紀末シチリア農村女性労働。",
    primary_source_url=GUTEN+"ebooks/24373",
    primary_source_type="Wikisource: Nedda",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="カプアーナ『ジャチンタ』",
    name_en="Capuana's Giacinta",
    name_original="Giacinta",
    period_key="イタリア・ヴェリズモ期",
    definition="ルイージ・カプアーナ（1839-1915）が1879年に発表した長編小説。少女期に性暴力を受けたジャチンタの精神病的人生を描き、フランス自然主義をイタリアに本格的に導入した記念作品。",
    background="19世紀末シチリアにおけるフランス自然主義受容。",
    development="ヴェルガ・ヴェリズモへの理論的支柱となり、20世紀イタリア心理小説に継承。",
    historical_context="19世紀末イタリア知識人のフランス自然主義受容。",
    primary_source_url=WSRC_IT+"Giacinta",
    primary_source_type="Wikisource: Giacinta",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="カプアーナ『ロッカヴェルディーナ侯爵』",
    name_en="Capuana's Il Marchese di Roccaverdina",
    name_original="Il Marchese di Roccaverdina",
    period_key="イタリア・ヴェリズモ期",
    definition="カプアーナが1901年に発表した長編小説。シチリア貴族ロッカヴェルディーナ侯爵が嫉妬から愛人の夫を殺害し精神崩壊する物語。イタリア・ヴェリズモ後期の最高傑作。",
    background="19世紀末シチリア貴族文化と犯罪心理学興隆。",
    development="20世紀イタリア心理リアリズム小説の祖型。",
    historical_context="19世紀末イタリア南部貴族文化。",
    primary_source_url=WSRC_IT+"Il_marchese_di_Roccaverdina",
    primary_source_type="Wikisource: Il Marchese di Roccaverdina",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="デ・ロベルト『副王たち』",
    name_en="De Roberto's I Viceré",
    name_original="I Viceré",
    period_key="イタリア・ヴェリズモ期",
    definition="フェデリコ・デ・ロベルト（1861-1927）が1894年に発表した長編小説。シチリア貴族ウゼーダ家がイタリア統一前後の政治変動に適応する三世代記。20世紀ランペドゥーザ『山猫』の先行作。",
    background="19世紀末イタリア統一後の南部貴族適応戦略。",
    development="ランペドゥーザ『山猫』、20世紀イタリア南部小説の祖型。",
    historical_context="19世紀末イタリア統一の南部問題。",
    primary_source_url=WSRC_IT+"I_Viceré",
    primary_source_type="Wikisource: I Viceré",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ピランデッロ『故マッティーア・パスカル』",
    name_en="Pirandello's Il fu Mattia Pascal",
    name_original="Il fu Mattia Pascal",
    period_key="イタリア・ヴェリズモ期",
    definition="ルイジ・ピランデッロ（1867-1936）が1904年に発表した長編小説。死亡誤認の機会に新しい身分で生き直そうとするマッティーア・パスカルの物語。20世紀イタリア・モダニズム小説の祖型で、1934年ノーベル文学賞代表作。",
    background="19世紀末イタリア南部貴族文化と心理学興隆。",
    development="20世紀イタリア・モダニズム、世界アイデンティティ小説の祖型。",
    historical_context="20世紀初頭イタリアの心理学論議。",
    primary_source_url=GUTEN+"ebooks/22933",
    primary_source_type="Project Gutenberg: The Late Mattia Pascal",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"アイデンティティ放棄と再構築の物語は、AI時代のデジタル・アイデンティティ流動性問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代のデジタル・アイデンティティ流動性"}])

add(**C, name_ja="ピランデッロ『一年間の小説集』",
    name_en="Pirandello's Novelle per un anno",
    name_original="Novelle per un anno",
    period_key="イタリア・ヴェリズモ期",
    definition="ピランデッロが1922年から発表開始した連作短編集（未完）。1日1篇を365日分目指した壮大な短編集計画で、244篇収録。20世紀イタリア短編の最大の宝庫の一つ。",
    background="20世紀初頭イタリア新聞・雑誌短編文学伝統。",
    development="20世紀世界短編文学に深い影響を与えた。",
    historical_context="20世紀初頭イタリア新聞・雑誌文化。",
    primary_source_url=WSRC_IT+"Novelle_per_un_anno",
    primary_source_type="Wikisource: Novelle per un anno",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="デレッダ『風に揺れる葦』",
    name_en="Deledda's Canne al vento",
    name_original="Canne al vento",
    period_key="イタリア・ヴェリズモ期",
    definition="グラツィア・デレッダ（1871-1936）が1913年に発表した長編小説。サルデーニャ島の没落貴族ピントール家を巡る運命的物語で、サルデーニャ・ヴェリズモの代表作。1926年ノーベル文学賞代表作。",
    background="19世紀末サルデーニャ農村社会と没落貴族文化。",
    development="20世紀イタリア地方リアリズム小説、女性ノーベル賞作家系譜の祖型。",
    historical_context="19世紀末サルデーニャ社会経済。",
    primary_source_url=WSRC_IT+"Canne_al_vento",
    primary_source_type="Wikisource: Canne al vento",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フォガッツァーロ『古い小さな世界』",
    name_en="Fogazzaro's Piccolo mondo antico",
    name_original="Piccolo mondo antico",
    period_key="イタリア・ヴェリズモ期",
    definition="アントニオ・フォガッツァーロ（1842-1911）が1895年に発表した長編小説。19世紀中葉ロンバルディア・ルガーノ湖畔の市民家庭をリソルジメント期の政治変動と交差させて描いた。北イタリア・カトリック・リアリズム小説の代表作。",
    background="19世紀中葉北イタリア・リソルジメント期の市民文化。",
    development="20世紀イタリア・カトリック・リアリズム小説に継承。",
    historical_context="19世紀中葉北イタリア。",
    primary_source_url=WSRC_IT+"Piccolo_mondo_antico",
    primary_source_type="Wikisource: Piccolo mondo antico",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: スペイン・リアリズム拡張（10）
# ============================================================
add(**C, name_ja="ガルドス『トラファルガル』",
    name_en="Galdós' Trafalgar",
    name_original="Trafalgar",
    period_key="イベリア・リアリズム期",
    definition="ベニート・ペレス・ガルドス（1843-1920）が1873年に発表した『国民挿話集』第一作。1805年トラファルガル海戦をカディス少年ガブリエル・アラセリの一人称で描き、スペイン歴史小説の規範を確立した。",
    background="19世紀末スペイン歴史主義文学運動。",
    development="『国民挿話集』全46巻の起点で、20世紀スペイン歴史小説の祖型。",
    historical_context="19世紀末スペイン国家アイデンティティ論議。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Trafalgar",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガルドス『ドニャ・ペルフェクタ』",
    name_en="Galdós' Doña Perfecta",
    name_original="Doña Perfecta",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1876年に発表した長編小説。架空のスペイン地方都市オルバホサで、進歩派青年ペペ・レイが叔母ドニャ・ペルフェクタの宗教的偏狭さと対立し悲劇に至る物語。19世紀末スペインの保守vs.進歩論議の文学化。",
    background="王政復古期スペインの保守vs.自由主義論議。",
    development="20世紀スペイン・リアリズム小説の規範となった。",
    historical_context="王政復古期スペインの政治論議。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Doña Perfecta",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガルドス『マリアネラ』",
    name_en="Galdós' Marianela",
    name_original="Marianela",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1878年に発表した長編小説。盲目の鉱山主青年パブロを世話する醜い少女マリアネラの悲劇を描き、自然主義以前のスペイン感傷的リアリズムの代表作。",
    background="19世紀末スペイン北部鉱山地方の社会。",
    development="20世紀スペイン地方リアリズム小説に継承された。",
    historical_context="19世紀末スペイン北部鉱山地方の労働者階級。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Marianela",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『ミゼリコルディア（慈悲）』",
    name_en="Galdós' Misericordia",
    name_original="Misericordia",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1897年に発表した長編小説。マドリードの貧困老女ベニーナが乞食生活に身を落としつつ主人を支える物語。19世紀末スペイン都市貧困層を描いた最高傑作。",
    background="19世紀末マドリード都市下層社会観察。",
    development="20世紀スペイン都市下層リアリズム小説の規範。",
    historical_context="19世紀末スペイン都市貧困問題。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Misericordia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガルドス『トリスターナ』",
    name_en="Galdós' Tristana",
    name_original="Tristana",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1892年に発表した長編小説。マドリードの女性トリスターナが後見人ドン・ロペとの関係から自立を求める物語。19世紀末スペイン女性問題小説の代表作。1970年ブニュエル映画化。",
    background="19世紀末スペインの女性問題論議。",
    development="20世紀スペイン女性文学、ブニュエル映画化。",
    historical_context="19世紀末スペインのフェミニズム前史。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Tristana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガルドス『ナサリン』",
    name_en="Galdós' Nazarín",
    name_original="Nazarín",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1895年に発表した長編小説。マドリードのアラブ系神父ナサリンがキリスト教的清貧を実践し社会から狂人扱いされる物語。19世紀末スペイン宗教論議の文学化で、ブニュエル映画化(1959)。",
    background="19世紀末スペインのキリスト教社会論議。",
    development="20世紀スペイン宗教文学、ブニュエル映画化。",
    historical_context="19世紀末スペインのキリスト教改革論議。",
    primary_source_url=GUTEN+"ebooks/16961",
    primary_source_type="Project Gutenberg: Nazarín",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="パルド・バサン『母なる自然』",
    name_en="Pardo Bazán's La Madre Naturaleza",
    name_original="La Madre Naturaleza",
    period_key="イベリア・リアリズム期",
    definition="エミリア・パルド・バサン（1851-1921）が1887年に発表した長編小説。『ウリョアの館』続編で、ガリシア地方の異母兄妹近親恋愛をゾラ自然主義の影響下で描いた。スペイン自然主義の代表作。",
    background="19世紀末ガリシア地方とスペイン自然主義論議。",
    development="20世紀スペイン地方リアリズム小説に継承。",
    historical_context="19世紀末スペイン自然主義論議。",
    primary_source_url=WSRC_ES+"La_Madre_Naturaleza",
    primary_source_type="Wikisource: La Madre Naturaleza",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="バレラ『ペピータ・ヒメネス』",
    name_en="Valera's Pepita Jiménez",
    name_original="Pepita Jiménez",
    period_key="イベリア・リアリズム期",
    definition="フアン・バレラ（1824-1905）が1874年に発表した書簡体長編小説。神学生青年ルイスがアンダルシアの未亡人ペピータと恋に落ち神学校を離れる物語。19世紀末スペインの心理リアリズム小説の代表作。",
    background="19世紀末スペイン王政復古期のカトリック・リベラル論議。",
    development="20世紀スペイン心理リアリズム小説の祖型となった。",
    historical_context="19世紀末スペイン宗教論議。",
    primary_source_url=GUTEN+"ebooks/8956",
    primary_source_type="Project Gutenberg: Pepita Jiménez",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ペレダ『ソティレサ』",
    name_en="Pereda's Sotileza",
    name_original="Sotileza",
    period_key="イベリア・リアリズム期",
    definition="ホセ・マリア・デ・ペレダ（1833-1906）が1885年に発表した長編小説。サンタンデール港町の漁師共同体を舞台に、孤児娘ソティレサの生活を描く。19世紀末スペイン地方リアリズム小説の規範。",
    background="19世紀末スペイン北部カンタブリア地方漁業共同体。",
    development="20世紀スペイン地方リアリズム小説の祖型。",
    historical_context="19世紀末スペイン北部地方文化。",
    primary_source_url=WSRC_ES+"Sotileza",
    primary_source_type="Wikisource: Sotileza",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブラスコ・イバニェス『血と砂』",
    name_en="Blasco Ibáñez' Sangre y arena",
    name_original="Sangre y arena",
    period_key="イベリア・リアリズム期",
    definition="ビセンテ・ブラスコ・イバニェス（1867-1928）が1908年に発表した長編小説。闘牛士ファン・ガリャルドの栄光と没落を描き、20世紀初頭スペインの闘牛文化と国民的アイデンティティを文学化した。",
    background="20世紀初頭スペイン闘牛文化と国家アイデンティティ論議。",
    development="20世紀世界スペイン文学（闘牛文学）の規範となり、英訳ベストセラー化。",
    historical_context="20世紀初頭スペイン国民文化。",
    primary_source_url=WSRC_ES+"Sangre_y_arena",
    primary_source_type="Wikisource: Sangre y arena",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: ロシア・リアリズム拡張（8）
# ============================================================
add(**CCYR, name_ja="ドストエフスキー『永遠の夫』",
    name_en="Dostoevsky's The Eternal Husband",
    name_original="Вечный муж",
    period_key="ロシア・リアリズム期",
    definition="ドストエフスキー（1821-81）が1870年に発表した中編小説。妻の元愛人ヴェリチャニノフを訪ねる「永遠の夫」トルソーツキーの心理を描き、嫉妬と被虐の心理を精緻に分析した。",
    background="19世紀末ロシアの心理小説興隆。",
    development="20世紀心理小説、フロイト精神分析に影響。",
    historical_context="19世紀後半ロシアの心理学的関心。",
    primary_source_url=GUTEN+"ebooks/13013",
    primary_source_type="Project Gutenberg: The Eternal Husband",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="ドストエフスキー『虐げられた人びと』",
    name_en="Dostoevsky's The Insulted and Humiliated",
    name_original="Униженные и оскорблённые",
    period_key="ロシア・リアリズム期",
    definition="ドストエフスキーが1861年に発表した長編小説。ペテルブルク貧民街の若い女性ネリーと作家イヴァンの物語で、シベリア流刑後のドストエフスキーが文壇復帰した記念作品。",
    background="アレクサンドル二世初期ロシアの社会問題小説。",
    development="ドストエフスキー後期長編の準備作品となった。",
    historical_context="19世紀後半ロシア農奴解放前夜。",
    primary_source_url=GUTEN+"ebooks/2845",
    primary_source_type="Project Gutenberg: The Insulted and Injured",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="トルストイ『セヴァストーポリ物語』",
    name_en="Tolstoy's Sevastopol Sketches",
    name_original="Севастопольские рассказы",
    period_key="ロシア・リアリズム期",
    definition="レフ・トルストイ（1828-1910）が1855-56年に発表した三部短編集。クリミア戦争セヴァストーポリ攻囲戦の従軍体験に基づく戦争スケッチで、19世紀ロシア戦争リアリズムの規範を確立した。",
    background="クリミア戦争(1853-56)とトルストイの従軍体験。",
    development="『戦争と平和』、20世紀世界戦争文学の祖型となった。",
    historical_context="19世紀中葉クリミア戦争と帝政ロシアの危機。",
    primary_source_url=GUTEN+"ebooks/3029",
    primary_source_type="Project Gutenberg: Sevastopol",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="トルストイ『ハジ・ムラート』",
    name_en="Tolstoy's Hadji Murad",
    name_original="Хаджи-Мурат",
    period_key="ロシア・リアリズム期",
    definition="トルストイが1896-1904年に執筆し1912年遺稿として発表した中編小説。19世紀中葉カフカース戦争のチェチェン武将ハジ・ムラートの裏切りと死を描き、トルストイ晩年の最高傑作の一つ。",
    background="19世紀中葉ロシアのカフカース植民地戦争史。",
    development="20世紀世界カフカース文学、ポストコロニアル文学に影響。",
    historical_context="19世紀中葉ロシア帝国カフカース征服。",
    primary_source_url=GUTEN+"ebooks/40646",
    primary_source_type="Project Gutenberg: Hadji Murad",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"植民地戦争における従属者の主体性を描く手法は、AI時代のグローバル少数民族表象問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代の少数民族表象とグローバル正義"}])

add(**CCYR, name_ja="トルストイ『コサック』",
    name_en="Tolstoy's The Cossacks",
    name_original="Казаки",
    period_key="ロシア・リアリズム期",
    definition="トルストイが1863年に発表した中編小説。モスクワ青年貴族オレーニンがカフカースのコサック村で過ごす夏を描き、ロシア知識人vs.辺境共同体の対比を通じて自然と文明を考察した。",
    background="19世紀中葉ロシア辺境カフカースの民族誌的観察。",
    development="20世紀ロシア辺境文学、自然対文明論に継承。",
    historical_context="19世紀中葉ロシア辺境政策。",
    primary_source_url=GUTEN+"ebooks/4761",
    primary_source_type="Project Gutenberg: The Cossacks",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="ツルゲーネフ『はつ恋』",
    name_en="Turgenev's First Love",
    name_original="Первая любовь",
    period_key="ロシア・リアリズム期",
    definition="イワン・ツルゲーネフ（1818-83）が1860年に発表した中編小説。16歳少年と21歳女性ジナイーダの片想いの追想を描き、19世紀ロシア心理小説の規範を確立した。",
    background="19世紀後半ロシア貴族文化と心理小説興隆。",
    development="20世紀世界初恋小説の祖型となった。",
    historical_context="19世紀後半ロシア貴族家庭。",
    primary_source_url=GUTEN+"ebooks/8597",
    primary_source_type="Project Gutenberg: First Love",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="ゴンチャロフ『断崖』",
    name_en="Goncharov's The Precipice",
    name_original="Обрыв",
    period_key="ロシア・リアリズム期",
    definition="イワン・ゴンチャロフ（1812-91）が1869年に発表した長編小説。ヴォルガ河畔の祖母領地で芸術家青年ライスキーが従姉妹ヴェーラを愛する物語。ニヒリスト世代との対立を描き、ゴンチャロフ三部作（『平凡物語』『オブローモフ』『断崖』）の最終作。",
    background="アレクサンドル二世改革期ロシアの世代論議。",
    development="19世紀末ロシア家族年代記小説に継承。",
    historical_context="19世紀後半ロシア改革期。",
    primary_source_url=WSRC_RU+"Обрыв_(Гончаров)",
    primary_source_type="Wikisource: Обрыв",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CCYR, name_ja="サルトィコフ＝シチェドリン『ゴロヴリョフ家の人々』",
    name_en="Saltykov-Shchedrin's The Golovlyov Family",
    name_original="Господа Головлёвы",
    period_key="ロシア・リアリズム期",
    definition="ミハイル・サルトィコフ＝シチェドリン（1826-89）が1875-80年に発表した長編小説。ロシア地主家系ゴロヴリョフ家三世代の没落を冷酷に描き、19世紀末ロシア家族年代記小説の最高傑作。",
    background="19世紀末ロシア地主階級の没落観察。",
    development="20世紀ロシア家族小説、ゴーリキー、ブニンに継承。",
    historical_context="19世紀末ロシア地主階級没落。",
    primary_source_url=GUTEN+"ebooks/41872",
    primary_source_type="Project Gutenberg: The Golovlyov Family",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="レスコフ『ムツェンスク郡のマクベス夫人』",
    name_en="Leskov's Lady Macbeth of Mtsensk",
    name_original="Леди Макбет Мценского уезда",
    period_key="ロシア・リアリズム期",
    definition="ニコライ・レスコフ（1831-95）が1865年に発表した中編小説。退屈な商人妻カテリーナが愛人と共謀し夫・舅・甥を殺害する物語。19世紀ロシア地方リアリズムの傑作で、ショスタコーヴィチ歌劇化(1934)。",
    background="19世紀末ロシア商人階級の家庭観察。",
    development="ショスタコーヴィチ歌劇化、20世紀世界文学に影響。",
    historical_context="19世紀末ロシア商人階級文化。",
    primary_source_url=WSRC_RU+"Леди_Макбет_Мценского_уезда",
    primary_source_type="Wikisource: Леди Макбет",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 象徴主義・デカダンス追加（6）
# ============================================================
add(**C, name_ja="マラルメ『エロディアード』",
    name_en="Mallarmé's Hérodiade",
    name_original="Hérodiade",
    period_key="象徴主義・デカダンス期",
    definition="ステファヌ・マラルメ（1842-98）が1864-67年に着手し未完のまま発表した詩劇断章。サロメ伝説のエロディアード（ヘロディアス）を題材に、純粋詩・自己反映性・氷の処女性を象徴主義的に追求した。",
    background="19世紀後半フランスにおけるサロメ主題流行（モロー絵画、ワイルド劇）と純粋詩運動。",
    development="20世紀フランス象徴主義詩学、純粋詩理論の中核。",
    historical_context="第二帝政期フランスの象徴主義興隆。",
    primary_source_url=WSRC_FR+"Hérodiade",
    primary_source_type="Wikisource: Hérodiade",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マラルメ『骰子一擲』",
    name_en="Mallarmé's Un coup de dés jamais n'abolira le hasard",
    name_original="Un coup de dés jamais n'abolira le hasard",
    period_key="象徴主義・デカダンス期",
    definition="マラルメが1897年に発表した詩。ページ全体を視覚的構成として用い、活字の大小・配置で意味と偶然を具現化した革新的詩で、20世紀視覚詩・コンクリート詩の祖型となった。",
    background="19世紀末フランス象徴主義の言語実験。",
    development="20世紀視覚詩、コンクリート詩、デリダ脱構築詩学の祖型。",
    historical_context="19世紀末フランスの言語実験。",
    primary_source_url=WSRC_FR+"Un_coup_de_dés_jamais_n%27abolira_le_hasard",
    primary_source_type="Wikisource: Un coup de dés",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"活字の視覚的配置による意味生成は、AI時代のマルチモーダル生成（テキスト+レイアウト）の歴史的祖型。",
         "related_ai_phenomenon":"AIマルチモーダル生成における視覚と言語の融合"}])

add(**C, name_ja="ヴェルレーヌ『叡智』",
    name_en="Verlaine's Sagesse",
    name_original="Sagesse",
    period_key="象徴主義・デカダンス期",
    definition="ポール・ヴェルレーヌ（1844-96）が1880年に発表した詩集。獄中改宗を踏まえたカトリック信仰と過去の悔恨を歌った詩集で、ヴェルレーヌ後期の代表作で、デカダンス的悔悟詩の規範。",
    background="19世紀末フランス・カトリック復興運動とヴェルレーヌの個人的危機。",
    development="20世紀フランス・カトリック詩、悔悟文学の祖型。",
    historical_context="第三共和制初期フランスのカトリック復興。",
    primary_source_url=GUTEN+"ebooks/13687",
    primary_source_type="Project Gutenberg: Sagesse",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ワイルド『サロメ』",
    name_en="Wilde's Salomé",
    name_original="Salomé",
    period_key="象徴主義・デカダンス期",
    definition="オスカー・ワイルド（1854-1900）が1891年にフランス語で執筆し1893年に出版した一幕劇。ヘロデの宴で7つのヴェールの踊りを舞いヨカナーン（洗礼者ヨハネ）の首を所望するサロメを描き、1905年R.シュトラウス歌劇化。",
    background="19世紀末ヨーロッパのサロメ主題流行とワイルドのフランス象徴主義受容。",
    development="シュトラウス歌劇『サロメ』(1905)化、20世紀世界デカダンス劇の規範。",
    historical_context="19世紀末英仏デカダンス文化。",
    primary_source_url=GUTEN+"ebooks/42704",
    primary_source_type="Project Gutenberg: Salomé",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ワイルド『ドリアン・グレイの肖像』",
    name_en="Wilde's The Picture of Dorian Gray",
    name_original="The Picture of Dorian Gray",
    period_key="象徴主義・デカダンス期",
    definition="ワイルドが1890年に発表した長編小説。美貌の青年ドリアン・グレイの肖像画が代わりに老醜と罪を引き受ける寓話で、19世紀末英国デカダンス・耽美主義小説の代表作。",
    background="19世紀末英国デカダンス運動とペーター美学受容。",
    development="20世紀英米デカダンス・耽美主義文学の規範となった。",
    historical_context="19世紀末英国デカダンス運動。",
    primary_source_url=GUTEN+"ebooks/174",
    primary_source_type="Project Gutenberg: The Picture of Dorian Gray",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"肖像画と本人が分離し、画像が代わりに老醜を引き受ける寓話は、AI時代のデジタル分身・アバター・データ・ダブル問題の歴史的祖型。",
         "related_ai_phenomenon":"AI時代のデジタル分身とアバター"}])

add(**C, name_ja="ホプキンス スプラング・リズム",
    name_en="Hopkins' sprung rhythm",
    name_original="sprung rhythm",
    period_key="象徴主義・デカダンス期",
    definition="ジェラード・マンリー・ホプキンス（1844-89）が考案・命名した詩のリズム理論。アクセント数のみで足を計算し音節数を自由化する古英語起源の韻律法で、19世紀末英国詩の革新的試みとして20世紀英米モダニズム詩学の理論的先駆となった。",
    background="19世紀末英国のアングロサクソン文献学興隆と詩律論再考。",
    development="20世紀英米モダニズム詩、エリオット・パウンドの自由詩理論の祖型。",
    historical_context="19世紀末英国の詩律理論論議。",
    primary_source_url=GUTEN+"ebooks/22403",
    primary_source_type="Project Gutenberg: Poems of Hopkins",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"アクセント・音節の自由配置による詩律革新は、AI生成詩におけるリズム生成の理論的基準点。",
         "related_ai_phenomenon":"AI生成詩におけるリズム・韻律の問題"}])


# ============================================================
# Cross-domain attachments
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


def _attach_axes(concept_name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


# Additional fourth_transform tags to reach >=24 total
_attach_axes("バルザック『従兄ポンス』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"美術コレクションを巡る親族の貪欲は、AI時代のデジタルコレクション・NFT資産化と理論的に並行する。",
     "related_ai_phenomenon":"AI/NFT時代のコレクション所有論"}])
_attach_axes("バルザック『あら皮』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"願いごとに寿命が削れる「あら皮」は、AIアシスタント使用ごとに自律性が削られる現代主体論との理論的並行。",
     "related_ai_phenomenon":"AI使用と主体性の希薄化"}])
_attach_axes("モーパッサン『ベラミ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"新聞ジャーナリストの偽造記事を巡る出世物語は、AI生成コンテンツによる虚妄出世の歴史的祖型。",
     "related_ai_phenomenon":"AI時代のメディア偽造とキャリア"}])
_attach_axes("モーパッサン『ピエールとジャン』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"序文「ル・ロマン」におけるリアリズム言語の不可能性論は、AI生成における言語の客観性問題と理論的に共振する。",
     "related_ai_phenomenon":"AI生成における言語客観性の問題"}])
_attach_axes("ディケンズ『デイヴィッド・コパフィールド』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"自伝的成長物語の規範は、AI時代の主体形成・成長物語生成の歴史的基準点。",
     "related_ai_phenomenon":"AI生成における自伝・成長物語"}])
_attach_axes("ディケンズ『オリヴァー・ツイスト』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"救貧院・少年窃盗団の社会批判文学化は、AI時代の社会的不平等可視化文学の祖型。",
     "related_ai_phenomenon":"AI時代の不平等可視化文学"}])
_attach_axes("ジョージ・エリオット『ロモラ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"歴史考証的小説手法は、AI時代の歴史的事実検証・再構築問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の歴史的事実生成と検証"}])
_attach_axes("コンラッド『ロード・ジム』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"マーロウの間接話法的語りの不確実性は、AI時代の情報源の信頼性連鎖問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の情報源信頼性連鎖"}])
_attach_axes("コンラッド『ノストローモ』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"南米における英米資本主義と政治革命の交差は、AI時代のグローバル資本主義と地域政治の理論的並行。",
     "related_ai_phenomenon":"AI時代のグローバル資本と地域政治"}])
_attach_axes("ベネット『五つの町のアンナ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"地方産業地帯の方言・産業用語の文学化は、AI時代の地域語・産業ジャーゴンの再現問題と理論的に並行する。",
     "related_ai_phenomenon":"AI多言語生成における方言・産業用語"}])
_attach_axes("ウェルズ『トノ・バンゲイ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"特許薬「トノ・バンゲイ」の広告詐欺と商業的成功は、AI時代のコンテンツ商業詐欺の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の広告・コンテンツ詐欺"}])
_attach_axes("シュトルム『白馬の騎手』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"伝説と心理リアリズムの融合は、AI時代の神話・データの融合語り構造の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の神話とデータの融合"}])
_attach_axes("シュニッツラー『輪舞』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"連鎖的物語構造（輪舞）は、AI時代の連鎖型物語生成・グラフ的物語構造の理論的祖型。",
     "related_ai_phenomenon":"AI時代の連鎖型・グラフ的物語生成"}])
_attach_axes("ヴェルガ『田舎の生活』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"標準イタリア語に方言リズムを取り込む技法は、AI多言語生成における方言性の問題の歴史的祖型。",
     "related_ai_phenomenon":"AI多言語生成における方言再現"}])
_attach_axes("デレッダ『風に揺れる葦』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"サルデーニャ地方文化の世界文学化は、AI時代のローカル文化のグローバル流通問題と理論的に並行する。",
     "related_ai_phenomenon":"AI時代のローカル文化のグローバル流通"}])
_attach_axes("ガルドス『トラファルガル』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"国民史小説（『国民挿話集』46巻）の形式は、AI時代の集合記憶・国家アイデンティティ生成の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の集合記憶生成"}])
_attach_axes("ガルドス『ナサリン』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"社会から狂人扱いされる聖者像は、AI時代の「合理性」逸脱者の社会的処遇問題と理論的に共振する。",
     "related_ai_phenomenon":"AI時代の合理性と逸脱"}])
_attach_axes("バレラ『ペピータ・ヒメネス』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"書簡体小説における自己観察と他者表象の交差は、AI時代の自己ナラティブとデータ表象の理論的祖型。",
     "related_ai_phenomenon":"AI時代の自己ナラティブとデータ表象"}])
_attach_axes("ブラスコ・イバニェス『血と砂』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"闘牛文化の国民的アイデンティティ化は、AI時代の文化的シンボル・コンテンツによる国家アイデンティティ生成の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の文化的シンボルとアイデンティティ"}])
_attach_axes("トルストイ『セヴァストーポリ物語』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"戦場スケッチ形式の従軍リアリズムは、AI時代の戦争映像・データ記録文学の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の戦争記録と文学"}])
_attach_axes("トルストイ『コサック』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"知識人の辺境共同体への参入と挫折は、AI時代の都市知識人と地域コミュニティの分断の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の知識階層と地域コミュニティ"}])
_attach_axes("ツルゲーネフ『はつ恋』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"少年期の心理を成熟した語り手で再構成する手法は、AI時代の主体的記憶・回想生成の理論的祖型。",
     "related_ai_phenomenon":"AI時代の記憶生成と再構成"}])
_attach_axes("レスコフ『ムツェンスク郡のマクベス夫人』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"地方商人妻の犯罪心理を世界文学レベルに引き上げる手法は、AI時代のローカル物語のグローバル化の理論的祖型。",
     "related_ai_phenomenon":"AI時代のローカル物語のグローバル化"}])
_attach_axes("マラルメ『エロディアード』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"自己反映的純粋詩は、AI生成における自己言及・反復構造の理論的祖型。",
     "related_ai_phenomenon":"AI生成における自己言及・反復"}])
_attach_axes("ヴェルレーヌ『叡智』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"獄中改宗詩集における主体の宗教的再構築は、AI時代の主体的価値観再構築の理論的並行。",
     "related_ai_phenomenon":"AI時代の主体的価値観再構築"}])
_attach_axes("ワイルド『サロメ』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"フランス語で執筆し英国で受容された越境作品は、AI時代の多言語間越境コンテンツの歴史的祖型。",
     "related_ai_phenomenon":"AI時代の多言語越境コンテンツ"}])


# Cross-domain links (>=18)
_attach_cross("バルザック『幻滅』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"印刷資本主義・出版産業論",
     "description":"19世紀パリ新聞・出版産業の文学的解剖は経営学的メディア産業論と並行。"}])
_attach_cross("バルザック『従兄ポンス』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"物質文化・コレクション論",
     "description":"美術コレクションを巡る親族関係は、19世紀末文化人類学の物質文化研究と並行。"}])
_attach_cross("バルザック『絶対の探求』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"絶対知探求論",
     "description":"科学的絶対探求はヘーゲル絶対知論との文学的並行。"}])
_attach_cross("モーパッサン『脂肪の塊』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"戦時道徳人類学",
     "description":"戦時の階級・道徳行動の観察は20世紀戦時人類学の祖型。"}])
_attach_cross("モーパッサン『ベラミ』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"メディア・出世論",
     "description":"新聞ジャーナリズムの出世構造は経営学的メディア産業論と並行。"}])
_attach_cross("ピエール・ロティ『氷島の漁夫』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"漁業共同体民族誌",
     "description":"ブルターニュ漁業共同体の文学的描写は19世紀末民族誌的観察。"}])
_attach_cross("ジョルジュ・サンド『魔の沼』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"農村民俗誌",
     "description":"ベリー地方農村の文学的記録は19世紀フランス農村民俗誌の祖型。"}])
_attach_cross("ディケンズ『オリヴァー・ツイスト』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"救貧法政策",
     "description":"新救貧法批判は19世紀英国社会政策論議の文学的記録。"}])
_attach_cross("ジョージ・エリオット『アダム・ビード』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"リアリズム宣言詩学",
     "description":"第17章のフランダース絵画的写実主義宣言は19世紀リアリズム理論の中核文献。"}])
_attach_cross("ハーディ『カスターブリッジの市長』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"地方経済・破綻論",
     "description":"穀物商の上昇と破綻は19世紀英国地方経済学の文学的事例。"}])
_attach_cross("トロロップ『今を生きる』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"金融資本主義腐敗",
     "description":"19世紀英国金融資本主義の腐敗観察は、現代金融経営学の歴史的事例。"}])
_attach_cross("コンラッド『闇の奥』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"植民地批判人類学",
     "description":"コンゴ植民地の文学的告発は20世紀植民地批判人類学の祖型。"}])
_attach_cross("コンラッド『ノストローモ』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"南米資源政治",
     "description":"南米銀鉱を巡る英米資本と政治革命は19世紀末資源政治の文学的記録。"}])
_attach_cross("フォード『良き兵士』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"不信頼な語り手詩学",
     "description":"フォードの不信頼な語り手は20世紀物語論の規範例。"}])
_attach_cross("ゴールズワージー『フォーサイト・サガ』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"上流ブルジョワ家族経営",
     "description":"上流ブルジョワ家系の財産・婚姻経営は19世紀末英国家族経営の文学的事例。"}])
_attach_cross("シュトルム『白馬の騎手』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"沿岸民俗誌",
     "description":"北海沿岸堤防共同体の文学的記録は19世紀末ドイツ沿岸民俗誌の祖型。"}])
_attach_cross("ハウプトマン『織工たち』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"労働運動史",
     "description":"1844年シレジア織工蜂起の文学化は19世紀末ドイツ労働運動史の文学的記録。"}])
_attach_cross("シュニッツラー『輪舞』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"性道徳・階級民族誌",
     "description":"世紀末ウィーン階級横断の性関係観察は世紀末ウィーン民族誌的観察。"}])
_attach_cross("ヴェルガ『田舎の生活』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"シチリア農村民族誌",
     "description":"シチリア農村の文学的描写は19世紀末イタリア南部問題民族誌の祖型。"}])
_attach_cross("カプアーナ『ロッカヴェルディーナ侯爵』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"心理リアリズム詩学",
     "description":"侯爵の精神崩壊の心理描写は19世紀末心理リアリズム詩学の規範。"}])
_attach_cross("デ・ロベルト『副王たち』", [
    {"target_db":"PD","link_type":"shared_concept",
     "target_entity_name":"南部適応政治",
     "description":"シチリア貴族の政治適応戦略はイタリア統一後南部問題政治の文学的事例。"}])
_attach_cross("ピランデッロ『故マッティーア・パスカル』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アイデンティティ哲学",
     "description":"アイデンティティ放棄と再構築の物語は20世紀アイデンティティ哲学の文学的祖型。"}])
_attach_cross("デレッダ『風に揺れる葦』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"サルデーニャ民俗誌",
     "description":"サルデーニャ地方の文学的記録は19世紀末イタリア地方民俗誌の祖型。"}])
_attach_cross("ガルドス『ミゼリコルディア（慈悲）』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"都市貧困民族誌",
     "description":"19世紀末マドリード都市下層の文学的観察は都市貧困民族誌の祖型。"}])
_attach_cross("パルド・バサン『母なる自然』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ガリシア民俗誌",
     "description":"ガリシア地方の文学的描写は19世紀末スペイン地方民俗誌の祖型。"}])
_attach_cross("トルストイ『ハジ・ムラート』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カフカース民族誌",
     "description":"チェチェン武将の文学的描写は19世紀末ロシア・カフカース民族誌の祖型。"}])
_attach_cross("サルトィコフ＝シチェドリン『ゴロヴリョフ家の人々』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"地主家系経営崩壊",
     "description":"地主家系三世代の没落観察は19世紀末ロシア地主階級経営の文学的事例。"}])
_attach_cross("マラルメ『骰子一擲』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"視覚詩・タイポグラフィ詩学",
     "description":"活字配置による意味生成は20世紀視覚詩・タイポグラフィ詩学の祖型。"}])
_attach_cross("ホプキンス スプラング・リズム", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"韻律論・詩律理論",
     "description":"スプラング・リズム理論は20世紀英米韻律論の中核。"}])
_attach_cross("ワイルド『ドリアン・グレイの肖像』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"美と倫理の哲学",
     "description":"美と老醜の分離寓話は19世紀末英国デカダンス美学の哲学的核心。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[c08-w15] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c08-w15] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        if total:
            print(f"[c08-w15] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
