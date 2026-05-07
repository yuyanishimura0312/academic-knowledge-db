"""LIT-DB Phase 2 Wave 13 — C08: European Realism / Naturalism / Symbolism (+60).

Subfield: lit_eu_realism (id=5), region='西欧'.
Sources: Project Gutenberg, Wikisource (en/fr/de/it/es/ru), Frantext, Britannica.
>= 85% primary tier; fourth_transform_tags >= 18; cross_domain >= 14.

Adds 60 new concepts on top of the existing 40, covering:
  A: French Realism / Naturalism extensions (12)
  B: English Victorian / Henry James (14)
  C: Russian Realism extensions (6)
  D: Italian Verismo / Iberian / Portuguese Realism (8)
  E: German Realism (5)
  F: American Realism / Naturalism extensions (8)
  G: Symbolism / Decadence (7)
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
    ("リアリズム理論成熟期", "Mature Realist Poetics", 1850, 1900,
     "リアリズム・自然主義の自己理論化期。"),
    ("ロシア・リアリズム期", "Russian Realism (19th c.)", 1840, 1910,
     "ツルゲーネフ、ゴンチャロフ、サルトィコフ＝シチェドリン、チェーホフ、ゴーリキーを擁するロシア・リアリズム期。"),
    ("イタリア・ヴェリズモ期", "Italian Verismo", 1870, 1910,
     "ヴェルガを中心とするシチリア発のヴェリズモ運動と、北イタリア・ナポリ派の写実主義。"),
    ("イベリア・リアリズム期", "Iberian Realism", 1860, 1910,
     "ガルドス、パルド・バサン、クラリン、エサ・デ・ケイロスらスペイン・ポルトガル写実主義の隆盛期。"),
    ("ドイツ詩的リアリズム期", "German Poetic Realism", 1850, 1900,
     "フォンターネ、ストルム、ケラー、ラーベらドイツ語圏の市民的・詩的リアリズム期。"),
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
BRITT = "https://www.britannica.com/"
ARTFL = "https://artfl-project.uchicago.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_realism", region="西欧", original_script="roman")
CCYR = dict(subfield_code="lit_eu_realism", region="西欧", original_script="cyrillic")


# ============================================================
# A: フランス・リアリズム／自然主義 拡張（12）
# ============================================================
add(**C, name_ja="スタンダール『パルムの僧院』",
    name_en="Stendhal's La Chartreuse de Parme",
    name_original="La Chartreuse de Parme",
    period_key="19世紀フランス・リアリズム期",
    definition="スタンダールが1839年に発表した長編小説。ナポレオン没落後のイタリア・パルマ公国を舞台に、青年貴族ファブリス・デル・ドンゴの恋愛と政治的陰謀を描く。バルザックがレヴュー・パリジエンヌ誌(1840)で激賞し、リアリズムと心理ロマンスの融合として19世紀小説史に位置づけられる。",
    background="ナポレオン崇拝と王政復古期イタリアの政治的反動の歴史的背景。",
    development="プルーストはスタンダールを最重要先行者の一人と認め、20世紀心理小説に継承された。",
    historical_context="メッテルニヒ体制下イタリアの政治的閉塞と、フランス七月王政期の自由主義への文学的応答。",
    primary_source_url=GUTEN+"ebooks/14857",
    primary_source_type="Project Gutenberg: La Chartreuse de Parme",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『ゴリオ爺さん』",
    name_en="Balzac's Le Père Goriot",
    name_original="Le Père Goriot",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1834-35年に発表した長編小説。パリの下宿屋ヴォーケル館を舞台に、退役製麺業者ゴリオの父性愛と、地方青年ラスティニャックのパリ社会上昇譚を交差させる。『人間喜劇』の中核作品で、ヴォートランの登場やラスティニャックの「人物再登場（personnages reparaissants）」原理を確立した。",
    background="七月王政期パリの経済階層流動化と、地方青年のパリ集中という社会現象。",
    development="ドストエフスキー『罪と罰』、フローベール『感情教育』、20世紀パリ小説の祖型となった。",
    historical_context="王政復古末期から七月王政初期のパリ社会変動。",
    primary_source_url=GUTEN+"ebooks/1237",
    primary_source_type="Project Gutenberg: Le Père Goriot",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バルザック『ウジェニー・グランデ』",
    name_en="Balzac's Eugénie Grandet",
    name_original="Eugénie Grandet",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1833年に発表した長編小説。地方都市ソミュールの吝嗇家グランデと娘ウジェニーの生活を描き、地方ブルジョワ家庭の蓄財・婚姻・道徳を観察的に分析した。『人間喜劇』「地方生活の場面」の中核作品で、地方リアリズム小説の規範を確立した。",
    background="七月王政期フランス地方都市のブルジョワ蓄財文化、相続・婚姻法制の社会的重み。",
    development="フローベール『ボヴァリー夫人』、フランス地方リアリズム小説の祖型となった。",
    historical_context="七月王政期フランスにおける地方ブルジョワジー台頭。",
    primary_source_url=GUTEN+"ebooks/13007",
    primary_source_type="Project Gutenberg: Eugénie Grandet",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バルザック『従妹ベット』",
    name_en="Balzac's La Cousine Bette",
    name_original="La Cousine Bette",
    period_key="19世紀フランス・リアリズム期",
    definition="バルザックが1846年に発表した長編小説。「貧しい親戚（Les Parents pauvres）」二部作の一作で、独身女性ベットの嫉妬と復讐がユロ家の崩壊を導く。バルザック後期の傑作で、欲望・復讐・社会的腐敗を緻密な観察で描き、自然主義的決定論への橋渡しとなった。",
    background="七月王政末期パリ社会の道徳的腐敗と、女性の社会的孤立の文学化。",
    development="ゾラ自然主義、20世紀心理小説に継承された。",
    historical_context="七月王政末期(1846-48)の社会的不安と1848年革命前夜の文化情勢。",
    primary_source_url=GUTEN+"ebooks/1660",
    primary_source_type="Project Gutenberg: La Cousine Bette",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フローベール『感情教育』",
    name_en="Flaubert's L'Éducation sentimentale",
    name_original="L'Éducation sentimentale",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが1869年に発表した長編小説。地方青年フレデリック・モローのパリでの恋愛と政治的経験を、1840年から1851年12月クーデタまでの歴史的時間に重ね合わせて描く。「幻滅の小説（Roman der Desillusion）」の規範例として、ルカーチ『小説の理論』が中心類型化した。",
    background="フローベール自身の青年期体験と、1848年革命の歴史的記憶。",
    development="プルースト『失われた時を求めて』、20世紀モダニズム長編に深い影響を与えた。",
    historical_context="第二帝政末期から第三共和制初期にかけての歴史的回顧。",
    primary_source_url=GUTEN+"ebooks/13715",
    primary_source_type="Project Gutenberg: L'Éducation sentimentale",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"『感情教育』の脱劇的・幻滅的構成は、AI生成における物語的目的論の希薄化と理論的に共振する。",
         "related_ai_phenomenon":"AI生成テキストにおける幻滅・脱目的論的物語構造"}])

add(**C, name_ja="フローベール『ブヴァールとペキュシェ』",
    name_en="Flaubert's Bouvard et Pécuchet",
    name_original="Bouvard et Pécuchet",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが1881年に未完で遺した長編小説。二人の写字生が遺産で田舎に隠居し、農学・医学・歴史・哲学・宗教・教育の諸知識を順次試みて失敗していく百科事典的構造を持つ。19世紀ブルジョワ知識の空虚を風刺し、20世紀メタフィクションの先駆として再評価された。",
    background="19世紀後半の知識民主化と、百科事典的言説の文化的飽和。",
    development="ジョイス『ユリシーズ』、ボルヘス、20世紀メタフィクション小説の祖型となった。",
    historical_context="第三共和制初期フランスの世俗化・知識民主化期。",
    primary_source_url=GUTEN+"ebooks/14152",
    primary_source_type="Project Gutenberg: Bouvard et Pécuchet",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"19世紀知識の引用・反復・組み合わせを文学的に呈示する構造は、LLMの学習データ反復・組み合わせ的生成と理論的に並行する。",
         "related_ai_phenomenon":"LLMの百科事典的引用・組み合わせ的生成"}])

add(**C, name_ja="フローベール『三つの物語』",
    name_en="Flaubert's Trois contes",
    name_original="Trois contes",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが1877年に発表した三短編集（『純な心』『聖ジュリアン伝』『ヘロディアス』）。リアリズム的現代描写・中世聖人伝・古代史的再構成という三つの時代を往還し、フローベール後期の文体的成熟を示す。「純な心」はナラトロジーにおける自由間接話法の代表例として研究された。",
    background="フローベール晩年の文体的精錬と、ジャンル横断的実験の到達点。",
    development="20世紀短編小説論、自由間接話法理論の中心研究対象となった。",
    historical_context="第三共和制初期フランスの文学的成熟期。",
    primary_source_url=GUTEN+"ebooks/14154",
    primary_source_type="Project Gutenberg: Trois contes",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フローベール書簡集",
    name_en="Flaubert's Correspondance",
    name_original="Correspondance",
    period_key="19世紀フランス・リアリズム期",
    definition="フローベールが生涯にわたり書き続けた約4,500通の書簡。特にルイーズ・コレ宛書簡（1846-55）に「正確な言葉（le mot juste）」「非個人性（impassibilité）」「文体への絶対的献身」等のリアリズム文体論が結晶する。19世紀リアリズム作家の方法論的自意識の最重要原典資料。",
    background="フローベールの修道院的執筆実践と、書簡を介した文学的自己理論化。",
    development="20世紀リアリズム理論・モダニズム文体論の最重要参照源となった。",
    historical_context="19世紀フランス文学界における書簡文化と作家的自意識の制度化。",
    primary_source_url=GUTEN+"ebooks/28178",
    primary_source_type="Project Gutenberg: Flaubert Correspondance",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゾラ『居酒屋』",
    name_en="Zola's L'Assommoir",
    name_original="L'Assommoir",
    period_key="自然主義期",
    definition="ゾラが1877年に発表した長編小説。『ルーゴン=マッカール叢書』第7巻。パリ労働者街の洗濯女ジェルヴェーズの没落をアルコール依存症と環境決定論のもとで描く。フランス自然主義の社会派小説の代表作で、出版時に大論争を呼び、ゾラの大衆的成功を確立した。",
    background="第二帝政期パリ労働者街の風俗、19世紀フランスのアルコール依存社会問題。",
    development="ゾラ自然主義の制度的成功を画し、英米自然主義（ノリス、ドライサー）に直接影響した。",
    historical_context="第三共和制初期フランスの労働者問題・公衆衛生論議の文学化。",
    primary_source_url=GUTEN+"ebooks/8558",
    primary_source_type="Project Gutenberg: L'Assommoir",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゾラ『ジェルミナール』",
    name_en="Zola's Germinal",
    name_original="Germinal",
    period_key="自然主義期",
    definition="ゾラが1885年に発表した長編小説。『ルーゴン=マッカール叢書』第13巻。北フランス炭鉱地帯のストライキと労働者の蜂起を描き、19世紀労働文学の頂点を成す。タイトルは革命暦の月名「ジェルミナル（萌芽月）」を指し、社会主義革命の予兆を含意する。",
    background="1860-80年代フランス北部炭鉱地帯の労働争議、第三共和制初期の社会主義運動興隆。",
    development="20世紀社会派長編小説、プロレタリア文学の祖型となった。",
    historical_context="第三共和制初期の労働運動と社会主義思想の文学的反映。",
    primary_source_url=GUTEN+"ebooks/5711",
    primary_source_type="Project Gutenberg: Germinal",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゴンクール兄弟",
    name_en="Goncourt brothers",
    name_original="Edmond et Jules de Goncourt",
    period_key="19世紀フランス・リアリズム期",
    definition="エドモン（1822-96）とジュール（1830-70）のゴンクール兄弟は、フランス自然主義の先駆的長編作家。『ジェルミニー・ラセルトゥー』(1865、女中の二重生活)、『シャルル・ドマイイ』(1860)等で社会下層の精密観察を行い、ゾラに先行した。エドモンの遺志により1903年「ゴンクール賞」が創設された。",
    background="フランス第二帝政期の文学界と、フランス文学アカデミーへの対抗。",
    development="ゾラ自然主義の直接的先駆となり、フランス文学賞制度の中心ゴンクール賞を遺産として残した。",
    historical_context="第二帝政期フランス文学界の制度的多様化期。",
    primary_source_url=GUTEN+"ebooks/13877",
    primary_source_type="Project Gutenberg: Germinie Lacerteux",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ユイスマンス『さかしま』",
    name_en="Huysmans's À rebours",
    name_original="À rebours",
    period_key="象徴主義・デカダンス期",
    definition="ジョリス＝カルル・ユイスマンス（1848-1907）が1884年に発表した長編小説。ゾラ自然主義から離脱し、隠遁する貴族デ・ゼッサントの倒錯的耽美生活を描く。デカダンス文学の聖典とされ、ワイルド『ドリアン・グレイの肖像』に「黄色い本」として登場し、世紀末ヨーロッパ文化に決定的影響を与えた。",
    background="1880年代フランス自然主義の制度的飽和と、デカダンス・象徴主義への移行期。",
    development="ワイルド、シモンズ、英国デカダンス文学、20世紀世紀末文学の聖典となった。",
    historical_context="第三共和制中期の文化的飽和と、世紀末感覚の文学的形式化。",
    primary_source_url=GUTEN+"ebooks/12341",
    primary_source_type="Project Gutenberg: À rebours",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"デ・ゼッサントの孤独な人工楽園生活は、AI時代のデジタル隠遁・人工的環境による主体構築と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における人工的主体構築・デジタル隠遁"}])


# ============================================================
# B: 英国ヴィクトリア朝・ヘンリー・ジェイムズ拡張（14）
# ============================================================
add(**C, name_ja="ディケンズ『リトル・ドリット』",
    name_en="Dickens's Little Dorrit",
    name_original="Little Dorrit",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1855-57年に発表した長編小説。マーシャルシー債務監獄を中心に、債務・官僚制（架空官庁「迂遠局 Circumlocution Office」）・金融詐欺を交錯させる社会批判長編。ディケンズ後期の社会批判の頂点を成し、官僚制・資本主義批判の文学的範型となった。",
    background="クリミア戦争後の英国官僚制批判、ディケンズ自身の幼少期マーシャルシー監獄体験。",
    development="20世紀英国社会派長編、カフカ官僚制小説の祖型的位置を占める。",
    historical_context="ヴィクトリア朝中期英国の行政改革論議と金融恐慌。",
    primary_source_url=GUTEN+"ebooks/963",
    primary_source_type="Project Gutenberg: Little Dorrit",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ディケンズ『我らが共通の友』",
    name_en="Dickens's Our Mutual Friend",
    name_original="Our Mutual Friend",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ディケンズが1864-65年に発表した最後の完成長編。テムズ川とロンドンの塵芥山を中心象徴に、貨幣・偽装・階級越境を網状に交錯させる成熟期長編。T・S・エリオットが『荒地』に「Our Mutual Friend」を引用し、20世紀モダニズムへの橋渡しとして再評価された。",
    background="ヴィクトリア朝後期英国の都市・産業・階級構造の文学的全体把握。",
    development="エリオット『荒地』、20世紀英国都市小説（ウルフ『ダロウェイ夫人』）に深い影響を与えた。",
    historical_context="1860年代英国資本主義の成熟と、都市インフラ近代化期。",
    primary_source_url=GUTEN+"ebooks/883",
    primary_source_type="Project Gutenberg: Our Mutual Friend",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョージ・エリオット『フロス河の水車場』",
    name_en="George Eliot's The Mill on the Floss",
    name_original="The Mill on the Floss",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ジョージ・エリオットが1860年に発表した長編小説。マギー・タリヴァーという感受性豊かな少女の知的・道徳的成長と、社会的制約の悲劇を描く。半自伝的要素を含み、19世紀英国女性小説の金字塔として、後の女性教育・道徳論議の中心テクストとなった。",
    background="19世紀中葉英国地方社会の女性教育問題、エリオット自身の知的成長体験。",
    development="ヴァージニア・ウルフのエリオット評価、20世紀フェミニスト批評の中心研究対象となった。",
    historical_context="ヴィクトリア朝中期英国の女性教育論議と地方社会の社会変動。",
    primary_source_url=GUTEN+"ebooks/6688",
    primary_source_type="Project Gutenberg: The Mill on the Floss",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョージ・エリオット『ダニエル・デロンダ』",
    name_en="George Eliot's Daniel Deronda",
    name_original="Daniel Deronda",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ジョージ・エリオットが1876年に発表した最後の長編小説。英国上流社会のグウェンドレンとユダヤ系青年デロンダの並行物語を、シオニズム前史の歴史的契機において展開した。F・R・リーヴィスは前半部のみを高く評価したが、後にユダヤ系部分の文学的・歴史的意義が再評価された。",
    background="19世紀後半英国のユダヤ問題、シオニズム運動の前史。",
    development="20世紀ユダヤ文学批評、エドワード・サイード『文化と帝国主義』のエリオット論で再評価された。",
    historical_context="ヴィクトリア朝後期英国の人種・宗教・帝国論議。",
    primary_source_url=GUTEN+"ebooks/7469",
    primary_source_type="Project Gutenberg: Daniel Deronda",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーディ『テス』",
    name_en="Hardy's Tess of the d'Urbervilles",
    name_original="Tess of the d'Urbervilles",
    period_key="19世紀英米・北欧リアリズム期",
    definition="トマス・ハーディ（1840-1928）が1891年に発表した長編小説。副題「純潔な女（A Pure Woman）」が物議を醸した。ウェセックス地方の少女テスの悲劇を、自然主義的決定論と道徳的問題提起の交錯のもとに描く。後期ヴィクトリア朝「問題小説」の代表作。",
    background="ハーディのウェセックス連作の中心と、後期ヴィクトリア朝道徳論議の文学化。",
    development="20世紀英国小説・フェミニスト批評・自然主義文学評価の中心テクストとなった。",
    historical_context="後期ヴィクトリア朝英国の女性問題・農村変容・宗教論議。",
    primary_source_url=GUTEN+"ebooks/110",
    primary_source_type="Project Gutenberg: Tess of the d'Urbervilles",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ハーディ『日陰者ジュード』",
    name_en="Hardy's Jude the Obscure",
    name_original="Jude the Obscure",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ハーディが1895年に発表した最後の長編小説。労働者ジュードの大学進学願望と婚姻制度との衝突を悲劇的に描き、後期ヴィクトリア朝の道徳的偽善を強烈に批判した。受容の悪さがハーディの小説執筆を終結させ、以降詩作に転じる契機となった。",
    background="後期ヴィクトリア朝の階級・教育・婚姻問題、ハーディ自身の建築・教育体験。",
    development="20世紀英国社会派長編、フェミニスト批評の中心研究対象となった。",
    historical_context="1890年代英国の世紀末社会論議と離婚法・大学開放問題。",
    primary_source_url=GUTEN+"ebooks/153",
    primary_source_type="Project Gutenberg: Jude the Obscure",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トロロップ『バーチェスター物語』",
    name_en="Trollope's Barchester Chronicles",
    name_original="Chronicles of Barsetshire",
    period_key="19世紀英米・北欧リアリズム期",
    definition="アンソニー・トロロップ（1815-82）が1855-67年に発表した6巻連作小説。架空の地方教区バーセットシャーを舞台に、英国国教会聖職者社会と地方ジェントリ階級を緻密な観察で描く。ヴィクトリア朝中期英国地方社会の制度的記録として、リアリズム連作小説の英国における規範を確立した。",
    background="1850-60年代英国国教会論議（高教会派・低教会派対立）、地方ジェントリ社会。",
    development="後の英国地方連作小説（C・P・スノウ「奇人と異邦人」連作等）の祖型となった。",
    historical_context="ヴィクトリア朝中期英国の宗教・地方制度の文学的記録。",
    primary_source_url=GUTEN+"ebooks/3045",
    primary_source_type="Project Gutenberg: The Warden",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガスケル『北と南』",
    name_en="Gaskell's North and South",
    name_original="North and South",
    period_key="19世紀英米・北欧リアリズム期",
    definition="エリザベス・ガスケル（1810-65）が1854-55年に発表した長編小説。南部英国のマーガレットが北部産業都市ミルトン（モデル：マンチェスター）に移住し、工場主ソーントンとの相互理解を獲得していく過程を描く。「英国状況小説（condition-of-England novel）」の中心作で、産業化下の階級対立を女性主人公の経験から描いた。",
    background="1840-50年代英国産業化進展、マンチェスター工業地帯の労使対立、ガスケル自身のマンチェスター生活。",
    development="20世紀英国社会派長編、フェミニズム批評の中心研究対象となった。",
    historical_context="1840年代「飢餓の40年代」とチャーチスト運動退潮期の英国社会。",
    primary_source_url=GUTEN+"ebooks/4276",
    primary_source_type="Project Gutenberg: North and South",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シャーロット・ブロンテ『ジェイン・エア』",
    name_en="Charlotte Brontë's Jane Eyre",
    name_original="Jane Eyre",
    period_key="19世紀英米・北欧リアリズム期",
    definition="シャーロット・ブロンテ（1816-55）が1847年に発表した長編小説。孤児ジェインの成長と、ロチェスターとの恋愛を一人称で描く。英国小説における女性の主体性表現の画期となり、19世紀英国リアリズム・ロマン主義の融合形式を確立した。後にジーン・リース『広い藻の海』(1966)が「屋根裏の狂女」バーサの視点から再構築した。",
    background="ヨークシャー荒野の地理的環境、ブロンテ姉妹の家庭教師経験、ヴィクトリア朝初期女性教育問題。",
    development="20世紀フェミニスト批評（ギルバート・グーバー『屋根裏の狂女』1979）の中心テクストとなった。",
    historical_context="ヴィクトリア朝初期英国の女性教育・婚姻論議。",
    primary_source_url=GUTEN+"ebooks/1260",
    primary_source_type="Project Gutenberg: Jane Eyre",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エミリー・ブロンテ『嵐が丘』",
    name_en="Emily Brontë's Wuthering Heights",
    name_original="Wuthering Heights",
    period_key="19世紀英米・北欧リアリズム期",
    definition="エミリー・ブロンテ（1818-48）が1847年に発表した唯一の長編小説。ヨークシャー荒野を舞台に、ヒースクリフとキャサリンの破滅的情熱を、複数の語り手による枠物語構造で展開する。リアリズム期英国小説のなかで突出した形式実験性を持ち、20世紀モダニズム・ナラトロジーの中心研究対象となった。",
    background="ヨークシャー荒野の地理的・気候的特徴、ブロンテ姉妹の隔絶的成長環境。",
    development="ヴァージニア・ウルフ、F・R・リーヴィス、20世紀ナラトロジーが中心研究対象とした。",
    historical_context="ヴィクトリア朝初期英国地方の閉鎖性と、文学による激情表現の限界探究。",
    primary_source_url=GUTEN+"ebooks/768",
    primary_source_type="Project Gutenberg: Wuthering Heights",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="サッカレー『虚栄の市』",
    name_en="Thackeray's Vanity Fair",
    name_original="Vanity Fair",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ウィリアム・サッカレー（1811-63）が1847-48年に発表した長編小説。副題「英雄なき小説（A Novel without a Hero）」で、ベッキー・シャープという女性悪漢を中心にナポレオン戦争前後の英国社会を風刺的に描く。ディケンズと並ぶヴィクトリア朝中期英国リアリズムの巨匠で、語り手の介入的・諷刺的態度を特徴とする。",
    background="サッカレーのジャーナリズム背景と、19世紀英国の社会風刺文学伝統。",
    development="ジョイス『ユリシーズ』のサッカレー的諷刺性、20世紀英国諷刺小説に継承された。",
    historical_context="ヴィクトリア朝中期英国における社会的成功・偽装の文学化。",
    primary_source_url=GUTEN+"ebooks/599",
    primary_source_type="Project Gutenberg: Vanity Fair",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヘンリー・ジェイムズ『ある婦人の肖像』",
    name_en="Henry James's The Portrait of a Lady",
    name_original="The Portrait of a Lady",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ヘンリー・ジェイムズが1881年に発表した長編小説。米国娘イザベル・アーチャーが欧州旅行を通じて結婚と幻滅を経験する物語。ジェイムズ「国際的主題（international theme）」の代表作で、心理リアリズムと意識中心化の方法を確立した。20世紀米国大学英文学科のリアリズム必読書として地位を確立した。",
    background="19世紀末米国上流階級の欧州旅行文化と、ジェイムズの欧米往還的経歴。",
    development="20世紀米国新批評・ジェイムズ研究の中心テクストとなり、後の心理小説に深い影響を与えた。",
    historical_context="19世紀後半の英米文化的越境期と、米国上流階級のヨーロッパ志向。",
    primary_source_url=GUTEN+"ebooks/2833",
    primary_source_type="Project Gutenberg: The Portrait of a Lady",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ジェイムズの中心意識小説における主体の精緻な再現は、AI生成における擬似的内的独白との比較理論化点となる。",
         "related_ai_phenomenon":"AI生成における擬似的中心意識・内的独白"}])

add(**C, name_ja="ヘンリー・ジェイムズ『大使たち』",
    name_en="Henry James's The Ambassadors",
    name_original="The Ambassadors",
    period_key="リアリズム理論成熟期",
    definition="ヘンリー・ジェイムズが1903年に発表した後期長編小説。米国の中年男ストレザーがパリで青年チャドを連れ戻す使命を引き受け、欧州的体験のなかで変容していく物語。ジェイムズが自身の長編小説中最高傑作と評し、中心意識による限定視点の極致を成した。",
    background="ジェイムズ後期の文体的精錬期、19世紀末欧米文化越境の文学的総括。",
    development="20世紀新批評（パーシー・ラボック『小説の技術』1921）がジェイムズ「視点」論の規範例として中心研究対象とした。",
    historical_context="世紀転換期の欧米文化的越境論議、ジェイムズの英国帰化(1915)前夜。",
    primary_source_url=GUTEN+"ebooks/432",
    primary_source_type="Project Gutenberg: The Ambassadors",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヘンリー・ジェイムズ『鳩の翼』",
    name_en="Henry James's The Wings of the Dove",
    name_original="The Wings of the Dove",
    period_key="リアリズム理論成熟期",
    definition="ヘンリー・ジェイムズが1902年に発表した後期長編小説。死期の近い米国娘ミリー・シールと、英国カップル（ケート・クロイ＋マートン・デンシャー）の三角関係を、複数中心意識による多視点構造で展開した。ジェイムズ後期文体の頂点を成し、20世紀心理小説の方法論的範型となった。",
    background="ジェイムズ後期文体実験期と、米英文化的越境主題の精緻化。",
    development="20世紀心理小説、ナラトロジー、ジェイムズ研究の中心テクストとなった。",
    historical_context="世紀転換期英米文化越境論議。",
    primary_source_url=GUTEN+"ebooks/30059",
    primary_source_type="Project Gutenberg: The Wings of the Dove",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: ロシア・リアリズム拡張（6）
# ============================================================
add(**CCYR, name_ja="ツルゲーネフ『猟人日記』",
    name_en="Turgenev's A Sportsman's Sketches",
    name_original="Записки охотника",
    period_key="ロシア・リアリズム期",
    definition="イワン・ツルゲーネフ（1818-83）が1847-52年に雑誌『現代人』に連載し、1852年に単行本化した連作短編集。猟人の視点から農奴制下ロシア農村の人間像を温かい観察で描く。アレクサンドル2世の農奴解放(1861)に思想的影響を与えたとされ、19世紀ロシア・リアリズムの開幕を画した。",
    background="ニコライ1世期ロシアの農奴制と、知識人による農村観察の文学化。",
    development="ロシア・リアリズム小説の出発点となり、トルストイ、チェーホフ、ロシア農村文学の祖型となった。",
    historical_context="1840-50年代ロシアの農奴制論議と、ヨーロッパ革命への反動期。",
    primary_source_url=GUTEN+"ebooks/8597",
    primary_source_type="Project Gutenberg: A Sportsman's Sketches",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="ツルゲーネフ『父と子』",
    name_en="Turgenev's Fathers and Sons",
    name_original="Отцы и дети",
    period_key="ロシア・リアリズム期",
    definition="ツルゲーネフが1862年に発表した長編小説。青年バザーロフを中心に、ロシア「ニヒリズム」運動と父世代との対立を主題化した。「ニヒリスト」という語を社会論議に定着させ、ロシア知識人世代論の文学的範型となった。19世紀ロシア・リアリズム小説の代表作。",
    background="アレクサンドル2世「大改革」期(1860年代初頭)のロシア知識人論議、世代対立。",
    development="ロシア・ナロードニチェストヴォ運動への思想的影響、20世紀世代小説の祖型となった。",
    historical_context="農奴解放(1861)直後のロシア社会変動期。",
    primary_source_url=GUTEN+"ebooks/30723",
    primary_source_type="Project Gutenberg: Fathers and Sons",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CCYR, name_ja="ゴンチャロフ『オブローモフ』",
    name_en="Goncharov's Oblomov",
    name_original="Обломов",
    period_key="ロシア・リアリズム期",
    definition="イワン・ゴンチャロフ（1812-91）が1859年に発表した長編小説。地方貴族オブローモフが寝椅子から起き上がれない倦怠的生活を送る様を描き、「オブローモフ主義（обломовщина）」というロシア社会論的概念を生んだ。ニコライ・ドブロリュボフ「オブローモフ主義とは何か」(1859)が社会批評として体系化した。",
    background="19世紀中葉ロシア地方貴族社会の経済的衰退と精神的停滞の文学化。",
    development="20世紀ロシア社会論・文学論の中心テクストとなり、「オブローモフ主義」は社会学概念として定着した。",
    historical_context="農奴解放前夜のロシア地方貴族社会の精神的危機。",
    primary_source_url=GUTEN+"ebooks/54700",
    primary_source_type="Project Gutenberg: Oblomov",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"オブローモフ的倦怠は、AI環境における人間の能動性希薄化（推奨アルゴリズムへの受動的依存）と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における主体能動性希薄化"}])

add(**CCYR, name_ja="サルトィコフ＝シチェドリン",
    name_en="Saltykov-Shchedrin",
    name_original="Михаил Салтыков-Щедрин",
    period_key="ロシア・リアリズム期",
    definition="ミハイル・サルトィコフ＝シチェドリン（1826-89）はロシア19世紀後半の風刺作家。『ある町の歴史』(1869-70、架空地方都市の年代記）、『ゴロヴリョフ家の人々』(1880、地主家族の崩壊)で、ロシア官僚制・地主制の暗黒面を風刺的に解剖した。トルストイ、ドストエフスキーと並ぶロシア19世紀後半リアリズムの巨匠。",
    background="アレクサンドル2世期から3世期の反動的官僚制下ロシアの社会風刺の必要性。",
    development="20世紀ロシア・ソ連風刺文学（ブルガーコフ等）の祖型となった。",
    historical_context="アレクサンドル2世大改革期から3世反動期のロシア社会。",
    primary_source_url=GUTEN+"ebooks/45914",
    primary_source_type="Project Gutenberg: The Golovlyov Family",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CCYR, name_ja="チェーホフ後期戯曲",
    name_en="Chekhov's late plays",
    name_original="поздние пьесы Чехова",
    period_key="ロシア・リアリズム期",
    definition="アントン・チェーホフ（1860-1904）が1896-1904年に発表した4戯曲（『かもめ』『ワーニャ伯父さん』『三人姉妹』『桜の園』）。伝統的劇構造を解体し、登場人物の日常的会話の中に時代変動と精神的孤立を浸透させる「内的劇（subtext）」を確立した。スタニスラフスキー演技理論、20世紀世界演劇の方法的範型となった。",
    background="19世紀末ロシア社会の精神的閉塞、モスクワ芸術座(1898)とチェーホフの協働。",
    development="スタニスラフスキー・システム、20世紀世界演劇（ベケット、ピンター）に深い影響を与えた。",
    historical_context="ロシア帝国末期(1905年革命前夜)の精神的危機。",
    primary_source_url=GUTEN+"ebooks/7986",
    primary_source_type="Project Gutenberg: The Cherry Orchard",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CCYR, name_ja="ゴーリキー『母』",
    name_en="Gorky's Mother",
    name_original="Мать",
    period_key="ロシア・リアリズム期",
    definition="マクシム・ゴーリキー（1868-1936）が1906-07年に発表した長編小説。労働者の母ペラゲーヤが息子の革命運動に加わり、自身も革命家として覚醒する過程を描く。20世紀ソ連社会主義リアリズムの祖型として位置づけられ、ジダーノフ社会主義リアリズム綱領(1934)が規範例とした。",
    background="1905年ロシア革命の失敗と、ロシア社会民主労働党ボリシェヴィキ派の文学的応答。",
    development="ソ連社会主義リアリズム文学の規範作品となり、20世紀世界プロレタリア文学の祖型となった。",
    historical_context="1905年革命失敗からロシア帝国末期の革命運動高揚期。",
    primary_source_url=GUTEN+"ebooks/12097",
    primary_source_type="Project Gutenberg: Mother (Gorky)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: イタリア・ヴェリズモ／イベリア／ポルトガル（8）
# ============================================================
add(**C, name_ja="ヴェルガ『マラヴォリア家の人々』",
    name_en="Verga's I Malavoglia",
    name_original="I Malavoglia",
    period_key="イタリア・ヴェリズモ期",
    definition="ジョヴァンニ・ヴェルガ（1840-1922）が1881年に発表した長編小説。シチリア漁村アーチ・トレッツァのマラヴォリア家の没落を、漁民方言のリズムを取り込んだイタリア語散文で描く。「敗者たち（I Vinti）」連作の第一巻で、イタリア・ヴェリズモ運動の中心作品となった。",
    background="統一イタリア(1861)後のシチリア社会の経済的後進性、ヴェルガのカターニア生活体験。",
    development="ルキノ・ヴィスコンティ映画『揺れる大地』(1948)が忠実に映画化し、20世紀イタリア・ネオレアリズモへの直接的橋渡しとなった。",
    historical_context="リソルジメント後イタリア南部の「南部問題（questione meridionale）」論議。",
    primary_source_url=WSRC_IT+"I_Malavoglia",
    primary_source_type="Wikisource: I Malavoglia",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヴェルガ『マストロ＝ドン・ジェズアルド』",
    name_en="Verga's Mastro-don Gesualdo",
    name_original="Mastro-don Gesualdo",
    period_key="イタリア・ヴェリズモ期",
    definition="ヴェルガが1889年に発表した長編小説。「敗者たち」連作の第二巻。シチリア南部の小作人ジェズアルドの社会的上昇と精神的孤立を描く。D・H・ロレンスが英訳(1923)して英米ヴェリズモ受容の中心テクストとなった。",
    background="統一イタリア後のシチリア社会変動と、土地所有・階級越境の問題化。",
    development="ロレンス英訳を契機に英米のヴェリズモ受容を促し、20世紀イタリア南部文学の祖型となった。",
    historical_context="リソルジメント後イタリアの土地問題と階級変動。",
    primary_source_url=WSRC_IT+"Mastro-don_Gesualdo",
    primary_source_type="Wikisource: Mastro-don Gesualdo",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カプアーナ",
    name_en="Luigi Capuana",
    name_original="Luigi Capuana",
    period_key="イタリア・ヴェリズモ期",
    definition="ルイージ・カプアーナ（1839-1915）はヴェルガと並ぶヴェリズモ運動の理論家・作家。『ジャチンタ』(1879)、『侯爵夫人ロウマリーノ』(1901)等の長編で、シチリア社会の精神病理を描いた。批評集『同時代研究』(1880)、『新しい同時代研究』(1882)でヴェリズモを理論化した。",
    background="シチリア・ミネオの士族出身、ゾラ自然主義の選択的受容。",
    development="ヴェルガとともにヴェリズモ運動の制度的中心を成し、20世紀イタリア南部文学に継承された。",
    historical_context="統一イタリア後のシチリア知識人社会。",
    primary_source_url=WSRC_IT+"Autore:Luigi_Capuana",
    primary_source_type="Wikisource: Luigi Capuana",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ガルドス『フォルトゥナータとハシンタ』",
    name_en="Galdós's Fortunata y Jacinta",
    name_original="Fortunata y Jacinta",
    period_key="イベリア・リアリズム期",
    definition="ベニート・ペレス・ガルドス（1843-1920）が1886-87年に発表した長編小説。マドリードのブルジョワ妻ハシンタと労働者階級の女性フォルトゥナータの並行物語を、王政復古期マドリードの社会的全体像のもとに展開する。スペイン19世紀リアリズムの最高峰として、しばしば「スペインの『戦争と平和』」と称される。",
    background="王政復古(1874)後マドリードの社会変動、ガルドスのマドリード社会観察。",
    development="20世紀スペイン文学・カミロ・ホセ・セラ等への深い影響、現代スペイン文学批評の中心テクスト。",
    historical_context="王政復古期(1874-1923)スペインの政治的安定とブルジョワ社会形成期。",
    primary_source_url=WSRC_ES+"Fortunata_y_Jacinta",
    primary_source_type="Wikisource: Fortunata y Jacinta",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルドス『国民挿話集』",
    name_en="Galdós's Episodios Nacionales",
    name_original="Episodios Nacionales",
    period_key="イベリア・リアリズム期",
    definition="ガルドスが1873-1912年にわたり発表した46巻の歴史小説連環。トラファルガル海戦(1805)から19世紀末復古期までのスペイン近代史を、架空の人物群を通じて全景化した。19世紀世界文学における最大規模の歴史小説連環の一つで、スペイン国民国家の文学的記憶の基盤となった。",
    background="19世紀スペインの政治的混乱（カルリスタ戦争、革命、復古）と国民史叙述の必要性。",
    development="20世紀スペイン国民史叙述・歴史小説の祖型となった。",
    historical_context="王政復古期スペインの国民統合論議と歴史的記憶の制度化。",
    primary_source_url=WSRC_ES+"Episodios_Nacionales",
    primary_source_type="Wikisource: Episodios Nacionales",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パルド・バサン『ウリョアの館』",
    name_en="Pardo Bazán's Los Pazos de Ulloa",
    name_original="Los Pazos de Ulloa",
    period_key="イベリア・リアリズム期",
    definition="エミリア・パルド・バサン（1851-1921）が1886-87年に発表した長編小説。ガリシア地方の没落貴族館「ウリョアの館」を舞台に、貴族の堕落と農民世界の暴力を自然主義的方法で描く。スペイン自然主義の中心作品で、パルド・バサン論文「燃える問題（La cuestión palpitante）」(1883)とともにスペイン自然主義論争の核となった。",
    background="ガリシア地方の貴族社会衰退、フランス自然主義のスペイン受容。",
    development="20世紀スペイン・ガリシア文学・フェミニスト批評の中心研究対象となった。",
    historical_context="王政復古期スペインのカトリック・自然主義論争。",
    primary_source_url=WSRC_ES+"Los_Pazos_de_Ulloa",
    primary_source_type="Wikisource: Los Pazos de Ulloa",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クラリン『ラ・レヘンタ』",
    name_en="Clarín's La Regenta",
    name_original="La Regenta",
    period_key="イベリア・リアリズム期",
    definition="レオポルド・アラス（筆名クラリン、1852-1901）が1884-85年に発表した長編小説。架空の地方都市ベトゥスタ（モデル：オビエド）を舞台に、判事夫人アナ・オソレスの婚姻外恋愛と精神的危機を描く。フローベール『ボヴァリー夫人』のスペイン版とされ、スペイン19世紀地方リアリズムの頂点を成す。",
    background="19世紀後半スペイン地方都市のカトリック社会、クラリンのオビエド大学教員生活。",
    development="20世紀スペイン文学批評の中心テクストとなり、現代スペイン文学評価の基準作品となった。",
    historical_context="王政復古期スペイン地方都市の精神的閉塞。",
    primary_source_url=WSRC_ES+"La_Regenta",
    primary_source_type="Wikisource: La Regenta",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エサ・デ・ケイロス『マイア家の人々』",
    name_en="Eça de Queirós's Os Maias",
    name_original="Os Maias",
    period_key="イベリア・リアリズム期",
    definition="ジョゼ・マリア・エサ・デ・ケイロス（1845-1900）が1888年に発表した長編小説。リスボンのマイア家三世代の物語を通じて、19世紀後半ポルトガル上流社会の精神的衰退を描く。ポルトガル・リアリズムの最高峰として、ヴェリズモ・スペイン・リアリズムと並ぶイベリア半島リアリズムの頂点を成す。",
    background="19世紀後半ポルトガルの植民地経済衰退、ブラジル独立(1822)後の経済停滞、コインブラ大学世代の文学運動。",
    development="20世紀ポルトガル文学（ペソア、サラマーゴ）の祖型となった。",
    historical_context="ポルトガル・コンスティテューション期(1820-1910)末期の社会的衰退。",
    primary_source_url=WSRC_FR+"Auteur:José_Maria_de_Eça_de_Queirós",
    primary_source_type="Wikisource: Eça de Queirós",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: ドイツ詩的リアリズム（5）
# ============================================================
add(**C, name_ja="フォンターネ『エフィ・ブリースト』",
    name_en="Fontane's Effi Briest",
    name_original="Effi Briest",
    period_key="ドイツ詩的リアリズム期",
    definition="テオドール・フォンターネ（1819-98）が1894-95年に発表した長編小説。プロイセン貴族令嬢エフィの不本意な結婚と婚姻外恋愛、決闘による破滅を描く。フローベール『ボヴァリー夫人』、トルストイ『アンナ・カレーニナ』と並ぶ19世紀「姦通小説」三大傑作とされ、ドイツ詩的リアリズムの頂点を成す。",
    background="ヴィルヘルム期プロイセン貴族社会の婚姻制度・名誉観念、フォンターネ晩年期の社会観察。",
    development="20世紀ドイツ文学批評の中心テクストとなり、トーマス・マン『ブッデンブローク家』への直接的影響を与えた。",
    historical_context="ヴィルヘルム2世期ドイツ帝国の貴族社会と道徳論議。",
    primary_source_url=GUTEN+"ebooks/12791",
    primary_source_type="Project Gutenberg: Effi Briest",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フォンターネ『シュテヒリン』",
    name_en="Fontane's Der Stechlin",
    name_original="Der Stechlin",
    period_key="ドイツ詩的リアリズム期",
    definition="フォンターネが1898年に発表した最後の長編小説。マルク・ブランデンブルクのシュテヒリン湖畔を舞台に、老貴族デュブスラフを中心とする世代対話を展開する。「あまり何も起きない（es passiert wenig）」とフォンターネ自身評した会話中心の脱劇的構成は、ドイツ詩的リアリズムの最終形式を示す。",
    background="ヴィルヘルム期ドイツ貴族社会の終焉感、フォンターネ晩年の対話的形式実験。",
    development="20世紀ドイツ会話小説（トーマス・マン後期）の祖型となった。",
    historical_context="ヴィルヘルム2世期ドイツ帝国末期の貴族社会変容。",
    primary_source_url=GUTEN+"ebooks/13965",
    primary_source_type="Project Gutenberg: Der Stechlin",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シュトルム ノヴェレ",
    name_en="Storm's novellas",
    name_original="Novellen Theodor Storms",
    period_key="ドイツ詩的リアリズム期",
    definition="テオドール・シュトルム（1817-88）の中短編（ノヴェレ）58編。『みずうみ』(1849)、『白馬の騎手』(1888、遺作)を代表作とし、北独シュレスヴィヒ＝ホルシュタイン地方の風土・気候・伝説を背景に、回想・哀愁・運命の主題を抒情的散文で展開した。19世紀ドイツ・ノヴェレ形式の頂点を成す。",
    background="シュレスヴィヒ＝ホルシュタイン問題(1864、1866、1871)とシュトルムの政治的経験、北独抒情詩伝統。",
    development="20世紀ドイツ・ノヴェレ理論（パウル・ハイゼ「鷹理論」）の中心研究対象となった。",
    historical_context="ドイツ統一前後の地方アイデンティティ問題。",
    primary_source_url=GUTEN+"ebooks/35140",
    primary_source_type="Project Gutenberg: Der Schimmelreiter",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ケラー『緑のハインリヒ』",
    name_en="Keller's Der grüne Heinrich",
    name_original="Der grüne Heinrich",
    period_key="ドイツ詩的リアリズム期",
    definition="ゴットフリート・ケラー（1819-90）が1854-55年（第一稿）、1879-80年（第二稿）に発表した教養小説。スイス・チューリヒの青年画家ハインリヒの遍歴と道徳的成長を描く。ゲーテ『ヴィルヘルム・マイスターの修業時代』の系譜を継ぐドイツ語圏教養小説の中心作品で、スイス・ドイツ詩的リアリズムの頂点を成す。",
    background="ケラー自身の青年期画家修業体験、ドイツ語圏教養小説伝統。",
    development="トーマス・マン『魔の山』、20世紀ドイツ語圏教養小説に継承された。",
    historical_context="1848年革命前後のスイス・ドイツの政治的・知的状況。",
    primary_source_url=GUTEN+"ebooks/7592",
    primary_source_type="Project Gutenberg: Der grüne Heinrich",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ケラー『ゼルトヴィラの人々』",
    name_en="Keller's Die Leute von Seldwyla",
    name_original="Die Leute von Seldwyla",
    period_key="ドイツ詩的リアリズム期",
    definition="ケラーが1856年（第一巻）、1873-74年（第二巻）に発表したノヴェレ集。架空のスイス小都市「ゼルトヴィラ」を舞台に、ブルジョワ社会の道徳・経済・愛情の諸相をユーモアとアイロニーで描く。「村のロメオとユリア」(1856)はワーグナー支援者デリウスのオペラ題材となった。",
    background="19世紀中葉スイス・ブルジョワ社会のケラー的観察。",
    development="20世紀ドイツ語圏ユーモア文学・地方文学の祖型となった。",
    historical_context="19世紀中葉スイス連邦成立(1848)後の社会的安定期。",
    primary_source_url=GUTEN+"ebooks/24064",
    primary_source_type="Project Gutenberg: Die Leute von Seldwyla",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# F: アメリカ・リアリズム／自然主義拡張（8）
# ============================================================
add(**C, name_ja="ハウエルズ『サイラス・ラパムの立身』",
    name_en="Howells's The Rise of Silas Lapham",
    name_original="The Rise of Silas Lapham",
    period_key="19世紀英米・北欧リアリズム期",
    definition="ウィリアム・ディーン・ハウエルズが1885年に発表した長編小説。塗料製造業者サイラス・ラパムの経済的成功と道徳的「立身」を描く。米国リアリズム長編の規範作品で、ボストン上流社会と新興産業ブルジョワジーの接点を倫理的に問う。米国大学英文学科のリアリズム必読書として地位を確立した。",
    background="米国「金ぴか時代」の新興ブルジョワジー台頭、ハウエルズのボストン文壇経験。",
    development="米国リアリズム長編の規範となり、シンクレア・ルイス『バビット』等の20世紀米国社会派長編に継承された。",
    historical_context="再建期米国の経済成長と道徳論議。",
    primary_source_url=GUTEN+"ebooks/154",
    primary_source_type="Project Gutenberg: The Rise of Silas Lapham",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ノリス『マクティーグ』",
    name_en="Norris's McTeague",
    name_original="McTeague",
    period_key="自然主義期",
    definition="フランク・ノリスが1899年に発表した長編小説。サンフランシスコ移民社会の歯科技工士マクティーグの遺伝的暴力性が、結婚・金銭・嫉妬を通じて爆発する物語。ゾラ自然主義の決定論を米国西部に移植した最初期の本格作品で、エリック・フォン・シュトロハイム監督サイレント映画『グリード』(1924)の原作。",
    background="ゾラ自然主義の米国受容、19世紀末サンフランシスコの移民労働者社会。",
    development="20世紀米国自然主義（ドライサー、シンクレア）への直接的橋渡しとなった。",
    historical_context="米国「金ぴか時代」末期の都市移民社会観察。",
    primary_source_url=GUTEN+"ebooks/47672",
    primary_source_type="Project Gutenberg: McTeague",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウォートン『歓楽の家』",
    name_en="Wharton's The House of Mirth",
    name_original="The House of Mirth",
    period_key="自然主義期",
    definition="イーディス・ウォートン（1862-1937）が1905年に発表した長編小説。ニューヨーク上流社会の女性リリー・バートが、結婚と社会的地位を巡る経済的判断ミスを通じて没落していく過程を描く。米国上流階級リアリズムの代表作で、ジェイムズ的心理リアリズムと自然主義的決定論の融合を示す。",
    background="ウォートン自身のニューヨーク上流階級経験、ヘンリー・ジェイムズとの友情。",
    development="20世紀米国女性作家系譜（キャザー、フィッツジェラルド研究におけるウォートン参照）の中心テクストとなった。",
    historical_context="進歩主義時代米国の上流階級と新興富豪の社会変動。",
    primary_source_url=GUTEN+"ebooks/284",
    primary_source_type="Project Gutenberg: The House of Mirth",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ウォートン『無垢の時代』",
    name_en="Wharton's The Age of Innocence",
    name_original="The Age of Innocence",
    period_key="自然主義期",
    definition="イーディス・ウォートンが1920年に発表した長編小説。1870年代ニューヨーク上流社会を舞台に、ニューランド・アーチャーとオランスカ伯爵夫人の恋愛と社会的束縛を描く。1921年女性として初のピューリッツァー賞受賞作。米国「金ぴか時代」の社会的記録として、リアリズム長編の集大成的位置を占める。",
    background="ウォートンの「失われた古いニューヨーク」への懐古と、第一次大戦後の文化的位置づけ。",
    development="20世紀米国女性作家研究、米国階級小説研究の中心テクストとなった。",
    historical_context="第一次大戦後米国の19世紀懐古的反省期。",
    primary_source_url=GUTEN+"ebooks/541",
    primary_source_type="Project Gutenberg: The Age of Innocence",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キャザー『おお開拓者よ！』",
    name_en="Cather's O Pioneers!",
    name_original="O Pioneers!",
    period_key="自然主義期",
    definition="ウィラ・キャザー（1873-1947）が1913年に発表した長編小説。ネブラスカ州の北欧系移民開拓者アレクサンドラ・ベルグソンの土地経営と家族悲劇を描く。米国西部開拓地のリアリズム的記述として、米国地方主義（リージョナリズム）と自然主義の融合形式を示す。",
    background="キャザー自身のネブラスカ移民地体験、19世紀後半米国西部開拓の歴史的記憶。",
    development="20世紀米国地方主義文学・移民文学・女性作家研究の中心テクストとなった。",
    historical_context="19世紀末から20世紀初頭の米国西部開拓終結期。",
    primary_source_url=GUTEN+"ebooks/24",
    primary_source_type="Project Gutenberg: O Pioneers!",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キャザー『マイ・アントニーア』",
    name_en="Cather's My Ántonia",
    name_original="My Ántonia",
    period_key="自然主義期",
    definition="キャザーが1918年に発表した長編小説。ネブラスカ移民地のチェコ系移民娘アントーニアの生涯を、語り手ジムの回想で描く。米国地方主義文学の頂点を成し、米国西部移民史の文学的記録として、20世紀米国文学批評の中心研究対象となった。",
    background="キャザーのネブラスカ少女時代、米国西部移民世代の歴史化。",
    development="20世紀米国地方主義・女性作家研究の中心作品となった。",
    historical_context="第一次大戦後米国の西部開拓記憶の文学的回顧。",
    primary_source_url=GUTEN+"ebooks/242",
    primary_source_type="Project Gutenberg: My Ántonia",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="クレイン『街の女マギー』",
    name_en="Crane's Maggie: A Girl of the Streets",
    name_original="Maggie: A Girl of the Streets",
    period_key="自然主義期",
    definition="スティーヴン・クレインが1893年に自費出版した中編小説。ニューヨーク・バワリー街のスラム少女マギーの没落と自殺を、フランス自然主義の決定論的フレームと印象主義的描写で描いた。米国自然主義の出発点とされ、ハウエルズが激賞して米国自然主義の制度的承認を獲得した。",
    background="1890年代ニューヨーク移民スラム街の社会的可視化、フランス自然主義の米国受容。",
    development="ノリス、ドライサー、20世紀米国都市文学の祖型となった。",
    historical_context="進歩主義時代米国の都市貧困問題と、ジャーナリスティック社会観察興隆。",
    primary_source_url=GUTEN+"ebooks/447",
    primary_source_type="Project Gutenberg: Maggie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トウェイン『コネチカット・ヤンキー』",
    name_en="Twain's A Connecticut Yankee",
    name_original="A Connecticut Yankee in King Arthur's Court",
    period_key="19世紀英米・北欧リアリズム期",
    definition="マーク・トウェインが1889年に発表した長編小説。19世紀コネチカットの工場長ハンクが6世紀アーサー王宮廷にタイムスリップし、近代産業を導入する物語。米国産業文明・進歩理念への風刺的省察として、米国リアリズムの社会批評機能を凝縮した作品。",
    background="19世紀末米国産業資本主義の文化的反省、トウェインの時代風刺の成熟。",
    development="20世紀SF・タイムトラベル文学の祖型となり、米国産業文明批評の文学的範型となった。",
    historical_context="米国「金ぴか時代」末期の文化的反省期。",
    primary_source_url=GUTEN+"ebooks/86",
    primary_source_type="Project Gutenberg: A Connecticut Yankee",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"技術","status":"rethinking",
         "rationale":"近代技術を異時代に持ち込む構造は、AI技術がもたらす時代錯誤・歴史的非対称性問題と理論的に並行する。",
         "related_ai_phenomenon":"AI技術導入における時代錯誤・歴史非対称性"}])


# ============================================================
# G: 象徴主義・デカダンス（7）
# ============================================================
add(**C, name_ja="マラルメ散文",
    name_en="Mallarmé prose",
    name_original="prose de Mallarmé",
    period_key="象徴主義・デカダンス期",
    definition="ステファヌ・マラルメ（1842-98)の批評・エッセイ散文（『ディヴァガシオン Divagations』1897収録）。「危機の場（Crise de vers）」（1897）「文学の魔法（Le mystère dans les lettres）」等で、近代詩の言語的危機と象徴主義の理論的綱領を展開した。19世紀末フランス象徴主義の方法論的核心文献。",
    background="フランス第三共和制初期の文学言語の危機論議、ボードレール後の詩学的展開。",
    development="20世紀モダニズム詩学（ヴァレリー、エリオット、パウンド）、ポスト構造主義（デリダ、クリステヴァ）の中心研究対象となった。",
    historical_context="19世紀末フランスの言語・芸術の自律性論議。",
    primary_source_url=GUTEN+"ebooks/49587",
    primary_source_type="Project Gutenberg: Divagations (Mallarmé)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"マラルメの言語の物質性・自律性理念は、AI生成における言語の意味剥離・パターン的生成と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における言語の物質的・パターン的自律性"}])

add(**C, name_ja="ヴェルレーヌ『無言の恋歌』",
    name_en="Verlaine's Romances sans paroles",
    name_original="Romances sans paroles",
    period_key="象徴主義・デカダンス期",
    definition="ポール・ヴェルレーヌ（1844-96）が1874年に発表した詩集。ランボーとの放浪期に書かれた音楽的抒情詩集で、「音楽性（musicalité）」「印象性（impressionnisme）」を象徴主義詩学の核として確立した。後の「詩法（Art poétique）」(1882)とともにフランス象徴主義詩の方法的範型を成した。",
    background="ヴェルレーヌとランボーの放浪関係、1870年代フランスの詩的革新期。",
    development="ドビュッシー、フォーレらの音楽化を通じてフランス象徴主義の文化的浸透を実現した。",
    historical_context="第三共和制初期フランスの文学・音楽文化の交差。",
    primary_source_url=WSRC_FR+"Romances_sans_paroles",
    primary_source_type="Wikisource: Romances sans paroles",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ランボー『イリュミナシオン』",
    name_en="Rimbaud's Illuminations",
    name_original="Illuminations",
    period_key="象徴主義・デカダンス期",
    definition="アルチュール・ランボー（1854-91)が1872-75年に書き、1886年にヴェルレーヌの編集で刊行された散文詩集。「私とは一個の他者である（Je est un autre）」の主体解体、断片的散文詩形式、視覚的飛躍によって、19世紀末フランス象徴主義詩の革命的形式を確立した。20世紀シュルレアリスムの直接的先駆。",
    background="ランボー自身の青年期創作集中（17-20歳）、フランス第三共和制初期の文学的危機。",
    development="ブルトン・シュルレアリスム宣言(1924)がランボーを最重要先行者とし、20世紀世界詩の祖型となった。",
    historical_context="パリ・コミューン(1871)後の文化的危機と詩的革新。",
    primary_source_url=WSRC_FR+"Illuminations_(Rimbaud)",
    primary_source_type="Wikisource: Illuminations",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"「私とは他者」の主体解体宣言は、AI生成における主体の脱中心化・非人称化と理論的に響き合う古典的祖型。",
         "related_ai_phenomenon":"AI生成における主体の非人称化・脱中心化"},
        {"axis":"言語","status":"rethinking",
         "rationale":"ランボーの言語的飛躍と意味の断片化は、LLM生成の意味断片組み合わせ的構造と理論的に共振する。",
         "related_ai_phenomenon":"LLM生成における意味断片の飛躍的組み合わせ"}])

add(**C, name_ja="メーテルランク『青い鳥』",
    name_en="Maeterlinck's L'Oiseau bleu",
    name_original="L'Oiseau bleu",
    period_key="象徴主義・デカダンス期",
    definition="モーリス・メーテルランク（1862-1949）が1908年に発表した象徴主義劇。子供二人が幸福の青い鳥を求めて旅する寓話劇で、象徴主義劇の代表作として20世紀世界演劇に深い影響を与えた。1911年メーテルランクのノーベル文学賞受賞の代表作。",
    background="ベルギー象徴主義運動、19世紀末ヨーロッパの寓話劇復興。",
    development="20世紀世界演劇、児童文学、寓話劇の祖型となった。",
    historical_context="ベル・エポック期ヨーロッパの精神的探究文化。",
    primary_source_url=GUTEN+"ebooks/8606",
    primary_source_type="Project Gutenberg: The Blue Bird",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ペーター『ルネサンス』",
    name_en="Pater's The Renaissance",
    name_original="Studies in the History of the Renaissance",
    period_key="象徴主義・デカダンス期",
    definition="ウォルター・ペーター（1839-94）が1873年に発表した美学批評集。「結語（Conclusion）」の「絶えず宝石のような硬く明晰な炎で燃えること」が世紀末耽美主義の綱領となり、ワイルドら英国デカダンス運動に決定的影響を与えた。19世紀末英国象徴主義・デカダンスの理論的中核文献。",
    background="ヴィクトリア朝中後期英国のラスキン美学への対抗、オックスフォード美学講座の制度化。",
    development="ワイルド、シモンズ、英国デカダンス運動の理論的範型となり、20世紀モダニズム美学（ジョイス『若き芸術家の肖像』）にも継承された。",
    historical_context="ヴィクトリア朝後期英国の美学・道徳論議。",
    primary_source_url=GUTEN+"ebooks/2398",
    primary_source_type="Project Gutenberg: The Renaissance (Pater)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ペーター『マリウス』",
    name_en="Pater's Marius the Epicurean",
    name_original="Marius the Epicurean",
    period_key="象徴主義・デカダンス期",
    definition="ウォルター・ペーターが1885年に発表した哲学的歴史小説。アントニヌス朝期ローマの青年マリウスがエピクロス主義から原始キリスト教へと精神的遍歴する物語。デカダンス的耽美主義と倫理的探求の融合形式として、ジョイス『若き芸術家の肖像』に直接影響を与えた。",
    background="ヴィクトリア朝後期英国の宗教論議、ペーターのオックスフォード古代哲学研究。",
    development="ジョイス『若き芸術家の肖像』、20世紀英米モダニズム美学小説の祖型となった。",
    historical_context="ヴィクトリア朝後期英国の宗教的危機期。",
    primary_source_url=GUTEN+"ebooks/4057",
    primary_source_type="Project Gutenberg: Marius the Epicurean",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ワイルド批評",
    name_en="Wilde's criticism",
    name_original="Wilde's critical essays",
    period_key="象徴主義・デカダンス期",
    definition="オスカー・ワイルド（1854-1900）の批評集『意図 Intentions』(1891)所収のエッセイ群（「批評家としての芸術家」「嘘の衰退」等）。ペーター美学を継承しつつ、芸術の自律性・反自然主義・批評の創造性を主張し、19世紀末英国デカダンス美学の理論的中核となった。",
    background="ヴィクトリア朝後期英国のラスキン・アーノルド批評伝統への対抗、ペーター美学の継承。",
    development="20世紀英米モダニズム批評（エリオット、フライ）、ポスト構造主義批評の中心源流となった。",
    historical_context="1890年代英国デカダンス運動と、芸術の自律性論議。",
    primary_source_url=GUTEN+"ebooks/887",
    primary_source_type="Project Gutenberg: Intentions (Wilde)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ワイルドの「批評の創造性」「嘘の真理性」理念は、AI生成テキストにおける真偽・創造性の境界問題を理論化する古典的参照点。",
         "related_ai_phenomenon":"AI生成における真偽境界・創造性問題"}])


# ============================================================
# Cross-domain links (separate, to ensure >= 14)
# ============================================================
# We attach cross_domain inline below by enriching key concepts.
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("バルザック『ゴリオ爺さん』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"都市民族誌・人類学的観察",
     "description":"パリの下宿屋を社会観察の場とする手法は、19世紀都市民族誌（パリ生理学的スケッチ）と並行する。"}])

_attach_cross("ゾラ『ジェルミナール』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"労働・組織社会学",
     "description":"炭鉱労働組織の文学的全体像化は、19世紀労働社会学・組織論の文学的並行物として位置づけられる。"}])

_attach_cross("ハーディ『テス』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"悲劇・運命論詩学",
     "description":"ハーディの自然主義的決定論はギリシア悲劇受容と接続し、20世紀悲劇詩学に継承された。"}])

_attach_cross("ヘンリー・ジェイムズ『ある婦人の肖像』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"中心意識・焦点化理論",
     "description":"ジェイムズの中心意識小説はジュネット焦点化理論の歴史的祖型。"}])

_attach_cross("ヘンリー・ジェイムズ『大使たち』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"視点理論・現代物語論",
     "description":"『大使たち』はパーシー・ラボック『小説の技術』が中心研究対象とした視点理論の規範例。"}])

_attach_cross("ツルゲーネフ『父と子』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"世代論・社会変動",
     "description":"ロシア知識人世代論はマンハイム『世代論』(1928)等の社会学的世代論に先行。"}])

_attach_cross("ゴンチャロフ『オブローモフ』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"行動経済学・主体能動性",
     "description":"オブローモフ主義は経済的非合理・無為性の社会学的概念として20世紀ロシア社会学・経営学に影響。"}])

_attach_cross("チェーホフ後期戯曲", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"内的劇・サブテクスト",
     "description":"チェーホフ的サブテクストはスタニスラフスキー演技理論を介して20世紀演劇詩学の中核となった。"}])

_attach_cross("ヴェルガ『マラヴォリア家の人々』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"南部問題・周辺地域民族誌",
     "description":"シチリア漁村の民族誌的描写は19世紀末イタリア「南部問題」社会学・人類学と並行。"}])

_attach_cross("ガルドス『フォルトゥナータとハシンタ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"都市民族誌・階級観察",
     "description":"19世紀末マドリード都市階級観察は、19世紀末スペイン社会学・人類学の祖型。"}])

_attach_cross("クラリン『ラ・レヘンタ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"地方リアリズム・舞台空間詩学",
     "description":"地方都市ベトゥスタの空間構築はバフチン的クロノトポスの典型例として現代詩学が研究。"}])

_attach_cross("フォンターネ『エフィ・ブリースト』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"姦通小説詩学",
     "description":"フォンターネはトニー・タナー『姦通と小説』(1979)の比較対象の中心。"}])

_attach_cross("ウォートン『歓楽の家』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"上流階級民族誌",
     "description":"ニューヨーク上流社会の文学的民族誌は、19世紀末米国社会学・上流階級研究の祖型。"}])

_attach_cross("ランボー『イリュミナシオン』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"散文詩形式の詩学",
     "description":"ランボー散文詩は20世紀散文詩詩学・シュルレアリスム詩学の中心研究対象。"}])

_attach_cross("マラルメ散文", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"近代詩学の言語論",
     "description":"マラルメの言語論はクリステヴァ、デリダの近代詩学読解の中心研究対象。"}])

_attach_cross("ペーター『ルネサンス』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"美学的受容理論",
     "description":"ペーターの感覚的経験美学は19世紀末英国の文化人類学的経験論と並行。"}])


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
        print(f"[c08-w13] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c08-w13] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        # Tier breakdown for this run
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c08-w13] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
