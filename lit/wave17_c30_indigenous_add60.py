"""LIT-DB Phase 2 Wave 17 — C30 ADD: Indigenous & Oral Literature (+60).

Subfield: lit_indigenous_oral (id=19), region='周縁横断'.
Adds 60 NEW non-overlapping concepts on top of existing 80, target 400.

Coverage:
  A: Native American literature (Momaday, Silko, Welch, Erdrich, Alexie,
     Harjo, Hogan, Orange, Long Soldier, Diaz, Allen, etc.) — 18
  B: Indigenous theory (Justice, Womack-extended, Brooks, Warrior, Vizenor,
     Byrd, Simpson-Audra, Coulthard, Simpson-Leanne) — 9
  C: Canadian Indigenous (Highway, King, Campbell, Robinson, Maracle,
     Boyden, Wagamese, Dimaline) — 8
  D: Australian Aboriginal (Wright, Scott, Winch, Birch, Leane, Morgan,
     Pascoe, Heiss, Lucashenko, Taylor) — 9
  E: Pacific (Ihimaera, Grace, Hulme, Wendt, Figiel, Sullivan,
     Marsh, Avia) — 8
  F: Ainu literature (Chiri Yukie, Bachelor, Kayano-extended, contemporary) — 4
  G: African oral continuation, South Asian Adivasi, Indigenous AI sov. — 4

Verification: ~50% primary (PD/recordings/archive), ~50% secondary academic.
fourth_transform_tags >= 20; cross_domain to AN >= 14.
Definitions under 150 chars.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS_TO_SEED = [
    ("先住民口承伝統期", "Indigenous Oral Tradition (pre-contact)", -10000, 1500,
     "接触以前の口承伝統。"),
    ("植民地接触・抑圧期", "Colonial Contact & Suppression", 1500, 1960,
     "植民地化下で口承伝統が記録化・改変・抑圧される時期。"),
    ("先住民文芸復興期", "Indigenous Renaissance", 1960, 2026,
     "1960年代以降の先住民文芸復興。口承と書記の融合、自決運動、文化主権の文学。"),
]


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


REGION = "周縁横断"
SUBFIELD = "lit_indigenous_oral"
C = dict(subfield_code=SUBFIELD, region=REGION, original_script="roman")
CJ = dict(subfield_code=SUBFIELD, region=REGION, original_script="japanese")


# Source URLs
WIKI = "https://en.wikipedia.org/wiki/"
WIKIJA = "https://ja.wikipedia.org/wiki/"
ARCH = "https://archive.org/details/"
PG = "https://www.gutenberg.org/"
AIATSIS = "https://aiatsis.gov.au/"
TEARA = "https://teara.govt.nz/en/"
NLA = "https://www.nla.gov.au/"
PARA = "https://paradisec.org.au/"


# ============================================================
# A: Native American literature (18)
# ============================================================
add(**C, name_ja="モマデイ『夜明けに作られた家』",
    name_en="Momaday's House Made of Dawn",
    name_original="House Made of Dawn",
    period_key="先住民文芸復興期",
    definition="N. Scott Momadayが1968年に発表しピューリッツァー賞(1969)を受賞した長編小説。ネイティブ・アメリカン・ルネッサンスの起点とされる。",
    background="Kiowa-Cherokee系作家による戦後米国先住民文学の制度的承認の画期。",
    development="Silko, Welch, Erdrich ら先住民作家世代を生む直接的契機となった。",
    historical_context="1960年代の公民権運動とAIM運動の興隆期に重なる。",
    primary_source_url=WIKI+"House_Made_of_Dawn",
    primary_source_type="Harper & Row first edition / academic critical editions",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"先住民作者性を米国文学の中心に据える画期。AI時代の少数言語・文化の作者性主権の理論的祖型。",
         "related_ai_phenomenon":"先住民作者性とAI生成の正統性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Pueblo ethnography",
         "description":"Jemez Puebloの儀礼世界の文学的描写は先住民人類学的記述と直結。"}])

add(**C, name_ja="モマデイ『雨山への道』",
    name_en="Momaday's The Way to Rainy Mountain",
    name_original="The Way to Rainy Mountain",
    period_key="先住民文芸復興期",
    definition="Momadayが1969年に発表した自伝的散文詩。Kiowa族の歴史・神話・個人的記憶を三声構成で織り合わせた先住民散文詩の規範作品。",
    background="Kiowa族の口承伝統と書記文学の融合実験。",
    development="先住民自伝・回想録の方法的祖型となった。",
    historical_context="1969年のネイティブ・アメリカン・ルネッサンス本格化期。",
    primary_source_url=WIKI+"The_Way_to_Rainy_Mountain",
    primary_source_type="University of New Mexico Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Kiowa oral history",
         "description":"Kiowa口承史の文学的再構築。"}])

add(**C, name_ja="シルコ『儀式』",
    name_en="Silko's Ceremony",
    name_original="Ceremony",
    period_key="先住民文芸復興期",
    definition="Leslie Marmon Silko(Laguna Pueblo)が1977年に発表した長編。第二次大戦帰還兵タヨの治癒儀礼を通じてLaguna世界観を提示する代表作。",
    background="Laguna Pueblo口承伝統と現代戦争トラウマの統合。",
    development="先住民女性作家の世界文学的承認の画期。",
    historical_context="1970年代米国先住民自決運動と並行。",
    primary_source_url=WIKI+"Ceremony_(Silko_novel)",
    primary_source_type="Viking Press first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"治癒儀礼を物語装置とする構造は、AI時代の物語の治癒機能の理論的祖型。",
         "related_ai_phenomenon":"AI生成物語と治癒・修復"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"healing ritual ethnography",
         "description":"Laguna治癒儀礼の文学的記述は人類学的儀礼研究と接続。"}])

add(**C, name_ja="シルコ『死者の暦』",
    name_en="Silko's Almanac of the Dead",
    name_original="Almanac of the Dead",
    period_key="先住民文芸復興期",
    definition="Silkoが1991年に発表した大著。先コロンブス期から500年の植民地史と先住民予言を統合した汎米先住民叙事詩的小説。",
    background="20世紀末の汎米先住民連帯運動の文学的結晶。",
    development="先住民文学のスケールを大陸規模に拡張した。",
    historical_context="1992年コロンブス到来500年論争の前夜。",
    primary_source_url=WIKI+"Almanac_of_the_Dead",
    primary_source_type="Simon & Schuster first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シルコ『ストーリーテラー』",
    name_en="Silko's Storyteller",
    name_original="Storyteller",
    period_key="先住民文芸復興期",
    definition="Silkoが1981年に編んだ詩・散文・写真・口承譚の混成集。家族の語りと自作を等価に置き、口承と書記の境界を撤廃した。",
    background="Laguna Pueblo家族の口承伝統の書記化実験。",
    development="先住民マルチジャンル混成テクストの祖型。",
    historical_context="1980年代米国先住民出版の制度的成熟期。",
    primary_source_url=WIKI+"Storyteller_(Silko)",
    primary_source_type="Seaver Books / Penguin reissue",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"家族口承と個人作家性の等価化は、AI時代の集合作者性の理論的祖型。",
         "related_ai_phenomenon":"AI共著作と家族・共同体的作者性"}])

add(**C, name_ja="ウェルチ『冬の血』",
    name_en="Welch's Winter in the Blood",
    name_original="Winter in the Blood",
    period_key="先住民文芸復興期",
    definition="James Welch(Blackfeet/Gros Ventre)が1974年に発表した長編。モンタナ保留地の無名語り手の喪失と回復を簡潔な散文で描く。",
    background="平原先住民現代生活の文学化。",
    development="先住民ミニマリズム小説の祖型。",
    historical_context="1970年代米国先住民文芸復興期。",
    primary_source_url=WIKI+"Winter_in_the_Blood",
    primary_source_type="Harper & Row first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウェルチ『フールズ・クロウ』",
    name_en="Welch's Fools Crow",
    name_original="Fools Crow",
    period_key="先住民文芸復興期",
    definition="Welchが1986年に発表した歴史小説。1870年Marias虐殺前夜のBlackfeet社会を内側から描いた先住民歴史小説の代表作。",
    background="Blackfeet口承史と歴史記録の文学的統合。",
    development="先住民歴史小説の方法的祖型。",
    historical_context="1980年代米国先住民歴史記述の脱植民地化期。",
    primary_source_url=WIKI+"Fools_Crow",
    primary_source_type="Viking Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Blackfeet ethnohistory",
         "description":"Blackfeet民族誌史の文学的再構成。"}])

add(**C, name_ja="アードリック『ラブ・メディスン』",
    name_en="Erdrich's Love Medicine",
    name_original="Love Medicine",
    period_key="先住民文芸復興期",
    definition="Louise Erdrich(Ojibwe)が1984年に発表した連作短編集。Anishinaabe家族のサーガを多視点で構築する代表作の出発点。",
    background="Anishinaabe家族物語の連作実験。",
    development="北ダコタ・サーガ全7巻の起点となる。",
    historical_context="1980年代米国先住民女性作家の制度的承認期。",
    primary_source_url=WIKI+"Love_Medicine",
    primary_source_type="Holt, Rinehart & Winston first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アードリック『トラックス』",
    name_en="Erdrich's Tracks",
    name_original="Tracks",
    period_key="先住民文芸復興期",
    definition="Erdrichが1988年に発表したサーガ第3作。Fleur Pillagerの神話的力と土地割当政策の歴史を交差させる。",
    background="Anishinaabe土地割当(Dawes Act)の歴史化。",
    development="北ダコタ・サーガの神話的中核。",
    historical_context="米国先住民土地政策の文学的再評価期。",
    primary_source_url=WIKI+"Tracks_(Erdrich_novel)",
    primary_source_type="Henry Holt first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アードリック『ラローズ』",
    name_en="Erdrich's LaRose",
    name_original="LaRose",
    period_key="先住民文芸復興期",
    definition="Erdrichが2016年に発表した長編。狩猟事故から少年LaRoseが養子交換される現代Ojibwe共同体の正義と回復の物語。",
    background="現代米国先住民司法・回復的正義の文学化。",
    development="National Book Critics Circle賞受賞(2016)。",
    historical_context="2010年代米国先住民司法主権論議。",
    primary_source_url=WIKI+"LaRose_(novel)",
    primary_source_type="Harper first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"養子交換による主体の関係的構成は、AI時代の関係論的主体観の文学的範型。",
         "related_ai_phenomenon":"AI環境における関係論的主体形成"}])

add(**C, name_ja="アレクシー『ローン・レンジャー』",
    name_en="Alexie's Lone Ranger and Tonto Fistfight in Heaven",
    name_original="The Lone Ranger and Tonto Fistfight in Heaven",
    period_key="先住民文芸復興期",
    definition="Sherman Alexie(Spokane/Coeur d'Alene)が1993年に発表した短編集。Spokane保留地の現代生活を皮肉と笑いで描いた先住民現代短編の代表作。",
    background="1990年代米国先住民世代の声の登場。",
    development="映画『Smoke Signals』(1998)の原作となる。",
    historical_context="1990年代米国先住民ポップ・カルチャー興隆期。",
    primary_source_url=WIKI+"The_Lone_Ranger_and_Tonto_Fistfight_in_Heaven",
    primary_source_type="Atlantic Monthly Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アレクシー『絶対に本当の日記』",
    name_en="Alexie's Absolutely True Diary of a Part-Time Indian",
    name_original="The Absolutely True Diary of a Part-Time Indian",
    period_key="先住民文芸復興期",
    definition="Alexieが2007年に発表した半自伝的YA小説。保留地から白人高校に通う少年の物語で全米図書賞YA部門受賞。",
    background="米国先住民YA文学の制度化。",
    development="米国学校で最も挑戦される本の一つとなる。",
    historical_context="2000年代米国先住民教育権論議。",
    primary_source_url=WIKI+"The_Absolutely_True_Diary_of_a_Part-Time_Indian",
    primary_source_type="Little, Brown first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"reservation ethnography",
         "description":"保留地教育の民族誌的記述と並行。"}])

add(**C, name_ja="ハージョ『彼女は何頭かの馬を持っていた』",
    name_en="Harjo's She Had Some Horses",
    name_original="She Had Some Horses",
    period_key="先住民文芸復興期",
    definition="Joy Harjo(Mvskoke)が1983年に発表した詩集。表題詩のリトレイン構造で先住民女性の多重性を歌い上げた。",
    background="先住民女性詩の口承的形式実験。",
    development="2019年Harjoの全米桂冠詩人就任の基礎作。",
    historical_context="1980年代米国先住民女性詩の興隆期。",
    primary_source_url=WIKI+"She_Had_Some_Horses",
    primary_source_type="Thunder's Mouth Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハージョ『クレイジー・ブレイヴ』",
    name_en="Harjo's Crazy Brave",
    name_original="Crazy Brave",
    period_key="先住民文芸復興期",
    definition="Harjoが2012年に発表した自伝。Mvskoke系女性詩人の少女期から作家形成までを四方位構造で叙述した。",
    background="先住民詩人の自己形成史の文学化。",
    development="米国先住民女性自伝の現代範型。",
    historical_context="2010年代米国先住民女性表現の制度化期。",
    primary_source_url=WIKI+"Crazy_Brave",
    primary_source_type="W. W. Norton first edition",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハージョ全米桂冠詩人",
    name_en="Harjo as US Poet Laureate",
    name_original="Joy Harjo, US Poet Laureate (2019-22)",
    period_key="先住民文芸復興期",
    definition="2019年Harjoが先住民として初の全米桂冠詩人に就任(三期2022年まで)。'Living Nations, Living Words' プロジェクトを主導。",
    background="米国国家文学制度の脱植民地化的契機。",
    development="米国議会図書館に先住民詩人47人マップを残す。",
    historical_context="2010年代後半の米国文化制度の脱植民地化期。",
    primary_source_url="https://www.loc.gov/programs/poetry-and-literature/poet-laureate/poet-laureate-projects/living-nations-living-words/",
    primary_source_type="Library of Congress official archive",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"国家詩人制度の先住民化は国家・文学・先住性の関係再編の制度的契機。AI時代の文化主権制度設計の参照点。",
         "related_ai_phenomenon":"国家文化制度とAI時代の先住民主権"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"cultural sovereignty",
         "description":"国家文化制度の先住民主権化の事例。"}])

add(**C, name_ja="ホーガン『ソーラー・ストームズ』",
    name_en="Hogan's Solar Storms",
    name_original="Solar Storms",
    period_key="先住民文芸復興期",
    definition="Linda Hogan(Chickasaw)が1995年に発表した長編。James Bay水力発電計画への先住民抵抗を描いた環境先住民文学の代表作。",
    background="北米先住民環境抵抗運動の文学化。",
    development="先住民エコクリティシズムの中核テクスト。",
    historical_context="1990年代北米先住民環境正義運動期。",
    primary_source_url=WIKI+"Linda_Hogan",
    primary_source_type="Scribner first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"environmental ethnography",
         "description":"先住民環境抵抗の文学的民族誌。"}])

add(**C, name_ja="オレンジ『ゼア・ゼア』",
    name_en="Orange's There There",
    name_original="There There",
    period_key="先住民文芸復興期",
    definition="Tommy Orange(Cheyenne/Arapaho)が2018年に発表した長編。オークランドの都市先住民12人の声をパウワウ襲撃に向けて織り合わせる。",
    background="21世紀都市先住民(Urban Indian)の文学的可視化。",
    development="2010年代米国先住民文学の都市化転回の代表作。",
    historical_context="2010年代米国先住民人口の都市集中化期(72%が都市居住)。",
    primary_source_url=WIKI+"There_There_(novel)",
    primary_source_type="Knopf first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"都市先住民の多声主体構築は、AI時代の分散・複数主体性の文学的範型。",
         "related_ai_phenomenon":"AI時代の分散・多声的主体構築"}])

add(**C, name_ja="ロング・ソルジャー『ホエレアズ』",
    name_en="Long Soldier's Whereas",
    name_original="Whereas",
    period_key="先住民文芸復興期",
    definition="Layli Long Soldier(Oglala Lakota)が2017年に発表した詩集。2009年米国議会先住民謝罪決議の'Whereas'句を脱構築する政治詩。",
    background="米国議会先住民謝罪決議の文学的応答。",
    development="National Book Critics Circle賞受賞(2017)。",
    historical_context="2009年米国議会謝罪決議のオバマ政権下事後処理期。",
    primary_source_url=WIKI+"Layli_Long_Soldier",
    primary_source_type="Graywolf Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"国家公文書の脱構築的詩化は、AI時代の制度的言語の批判的解体の方法的祖型。",
         "related_ai_phenomenon":"AI生成における制度的言語の批判的脱構築"}])

# 18 Native American (G includes Diaz, Allen below in section A continuation)
add(**C, name_ja="ディアス『ポストコロニアル・ラブ・ポエム』",
    name_en="Diaz's Postcolonial Love Poem",
    name_original="Postcolonial Love Poem",
    period_key="先住民文芸復興期",
    definition="Natalie Diaz(Mojave/Akimel O'odham)が2020年に発表した詩集。Mojave言語・身体・愛・水戦争を交差させた現代先住民詩の頂点。",
    background="先住民愛・身体・言語の脱植民地化詩学。",
    development="2021年ピューリッツァー詩部門受賞。",
    historical_context="2010年代後半Standing Rock水保護運動以降の先住民詩潮流。",
    primary_source_url=WIKI+"Natalie_Diaz",
    primary_source_type="Graywolf Press first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"water sovereignty",
         "description":"先住民水主権論の詩的展開。"}])

add(**C, name_ja="アレン『神聖な輪』",
    name_en="Allen's The Sacred Hoop",
    name_original="The Sacred Hoop",
    period_key="先住民文芸復興期",
    definition="Paula Gunn Allen(Laguna)が1986年に発表した先住民フェミニズム批評。母系・女性中心のアメリカ先住民伝統を理論化した古典。",
    background="先住民フェミニズム批評の理論的画期。",
    development="後の先住民gynocriticism潮流の起点。",
    historical_context="1980年代米国フェミニズムの脱植民地化期。",
    primary_source_url=WIKI+"Paula_Gunn_Allen",
    primary_source_type="Beacon Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"母系・女性中心の主体観は、AI時代のジェンダー化された主体構築への文学的批判の祖型。",
         "related_ai_phenomenon":"AI生成主体のジェンダー前提批判"}])


# ============================================================
# B: Indigenous theory (9)
# ============================================================
add(**C, name_ja="ジャスティス『なぜ先住民文学が重要か』",
    name_en="Justice's Why Indigenous Literatures Matter",
    name_original="Why Indigenous Literatures Matter",
    period_key="先住民文芸復興期",
    definition="Daniel Heath Justice(Cherokee)が2018年に発表した先住民批評。文学を関係的倫理問への応答とする21世紀範型。",
    background="21世紀先住民批評の倫理転回の体系化。",
    development="北米・豪・NZ・北欧先住民研究の中心教科書。",
    historical_context="2010年代後半の先住民批評倫理化期。",
    primary_source_url=WIKI+"Daniel_Heath_Justice",
    primary_source_type="Wilfrid Laurier University Press",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リサ・ブルックス『共有の鍋』",
    name_en="Brooks' The Common Pot",
    name_original="The Common Pot",
    period_key="先住民文芸復興期",
    definition="Lisa Brooks(Abenaki)が2008年に発表した先住民批評。ニューイングランド先住民の'共有の鍋'比喩で先住民文学地理を理論化。",
    background="ニューイングランド先住民批評の方法的画期。",
    development="先住民文学地理学の理論的祖型。",
    historical_context="2000年代後半先住民批評の地理的転回期。",
    primary_source_url=WIKI+"Lisa_Brooks",
    primary_source_type="University of Minnesota Press",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Native cartography",
         "description":"先住民地理学・地図学との接続。"}])

add(**C, name_ja="ロバート・ウォリアー『部族の秘密』",
    name_en="Warrior's Tribal Secrets",
    name_original="Tribal Secrets",
    period_key="先住民文芸復興期",
    definition="Robert Allen Warrior(Osage)が1995年に発表した先住民知的史。Vine Deloria JrとJohn Joseph Mathewsを通じ部族知的伝統を理論化。",
    background="先住民知的主権論(intellectual sovereignty)の確立。",
    development="部族文学批評ナショナリズムの理論的支柱。",
    historical_context="1990年代米国先住民批評の自決化期。",
    primary_source_url=WIKI+"Robert_Allen_Warrior",
    primary_source_type="University of Minnesota Press",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴァイザナー『サヴァイヴァンス』理論",
    name_en="Vizenor's Survivance theory",
    name_original="Native Liberty / Manifest Manners",
    period_key="先住民文芸復興期",
    definition="Gerald Vizenor(Anishinaabe)による'survivance'(survival+resistance)概念の体系化。Manifest Manners(1994)等で先住民現存論を展開。",
    background="20世紀後半先住民批評の哲学的体系化。",
    development="現代先住民批評の中心概念として制度化。",
    historical_context="1990年代米国先住民理論の哲学的成熟期。",
    primary_source_url=WIKI+"Gerald_Vizenor",
    primary_source_type="University of Nebraska Press",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"survivanceは消滅論を退け能動的存続を理論化する。AI時代の文化的存続の理論的中核。",
         "related_ai_phenomenon":"AI時代の先住民文化のsurvivance"}])

add(**C, name_ja="ジョディ・バード『帝国の中継地』",
    name_en="Byrd's Transit of Empire",
    name_original="Transit of Empire",
    period_key="先住民文芸復興期",
    definition="Jodi Byrd(Chickasaw)が2011年に発表した批評。'Indianness'を米国帝国主義の中継地として理論化した政治批評。",
    background="先住民批評とポストコロニアル批評の接合。",
    development="先住民批評の地政学的転回の画期。",
    historical_context="2010年代帝国研究と先住民研究の接合期。",
    primary_source_url=WIKI+"Jodi_Byrd",
    primary_source_type="University of Minnesota Press",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"settler colonialism studies",
         "description":"入植者植民地主義研究との接続。"}])

add(**C, name_ja="オードラ・シンプソン『モホークの中断』",
    name_en="A. Simpson's Mohawk Interruptus",
    name_original="Mohawk Interruptus",
    period_key="先住民文芸復興期",
    definition="Audra Simpson(Kahnawà:ke Mohawk)が2014年に発表した政治人類学。'拒絶の政治'(refusal)で先住民主権を理論化。",
    background="先住民主権の人類学的再理論化。",
    development="先住民研究'拒絶の政治'潮流の中核。",
    historical_context="2010年代先住民研究の主権論的転回期。",
    primary_source_url=WIKI+"Audra_Simpson",
    primary_source_type="Duke University Press",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"politics of refusal",
         "description":"先住民人類学における拒絶の政治。"}])

add(**C, name_ja="クルサード『赤い肌、白い仮面』",
    name_en="Coulthard's Red Skin White Masks",
    name_original="Red Skin, White Masks",
    period_key="先住民文芸復興期",
    definition="Glen Coulthard(Yellowknives Dene)が2014年に発表した政治理論。Fanonを先住民文脈に応用し承認政治を批判。",
    background="先住民批評とフランツ・ファノンの統合。",
    development="先住民批評の脱承認政治論の中核。",
    historical_context="2010年代カナダ和解委員会論議期。",
    primary_source_url=WIKI+"Glen_Sean_Coulthard",
    primary_source_type="University of Minnesota Press",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"承認政治の批判は、AI時代のアイデンティティ承認システムの批判的検討の祖型。",
         "related_ai_phenomenon":"AI生成における承認・誤認の政治"}])

add(**C, name_ja="リアン・シンプソン『常にそうしてきたように』",
    name_en="L. Simpson's As We Have Always Done",
    name_original="As We Have Always Done",
    period_key="先住民文芸復興期",
    definition="Leanne Betasamosake Simpson(Anishinaabe)が2017年に発表した先住民解放論。Nishnaabeg知識実践を中心に置く脱植民地化論。",
    background="Anishinaabeg知識実践の理論的体系化。",
    development="2010年代後半先住民解放理論の中核テクスト。",
    historical_context="2010年代カナダIdle No More運動期。",
    primary_source_url=WIKI+"Leanne_Betasamosake_Simpson",
    primary_source_type="University of Minnesota Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Nishnaabeg knowledge practices",
         "description":"Anishinaabeg知識実践と人類学的知識論の接続。"}])

add(**C, name_ja="ヴァイン・デロリア『カスターは罪を背負って死んだ』",
    name_en="Deloria's Custer Died for Your Sins",
    name_original="Custer Died for Your Sins",
    period_key="先住民文芸復興期",
    definition="Vine Deloria Jr(Standing Rock Sioux)が1969年に発表した先住民マニフェスト。米国先住民政策と人類学を風刺した古典。",
    background="米国先住民政治批評の出発点。",
    development="先住民批評全領域への基礎的影響。",
    historical_context="1969年米国先住民活動主義興隆期。",
    primary_source_url=WIKI+"Custer_Died_for_Your_Sins",
    primary_source_type="Macmillan first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"人類学的他者表象の根本的批判は、AI時代の文化的他者表象の理論的祖型。",
         "related_ai_phenomenon":"AI生成における他者表象の倫理"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"anthropology critique",
         "description":"先住民による人類学批判の制度的画期。"}])


# ============================================================
# C: Canadian Indigenous (8)
# ============================================================
add(**C, name_ja="ハイウェイ『リズ姉妹』",
    name_en="Highway's The Rez Sisters",
    name_original="The Rez Sisters",
    period_key="先住民文芸復興期",
    definition="Tomson Highway(Cree)が1986年に発表した戯曲。Manitoulin島Cree女性7人がトロント・ビンゴ大会を目指す道行劇。",
    background="カナダ先住民演劇の制度的画期。",
    development="続編『Dry Lips Oughta Move to Kapuskasing』(1989)とニ部作。",
    historical_context="1980年代カナダ先住民演劇興隆期。",
    primary_source_url=WIKI+"The_Rez_Sisters",
    primary_source_type="Fifth House first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハイウェイ『毛皮の女王のキス』",
    name_en="Highway's Kiss of the Fur Queen",
    name_original="Kiss of the Fur Queen",
    period_key="先住民文芸復興期",
    definition="Highwayが1998年に発表した半自伝的長編。寄宿学校を生き延びるCree兄弟の物語でカナダ寄宿学校文学の代表作。",
    background="カナダ寄宿学校制度の文学的告発。",
    development="2008年カナダ寄宿学校真相和解委員会論議の文学的基礎。",
    historical_context="1990年代後半カナダ寄宿学校論議本格化期。",
    primary_source_url=WIKI+"Kiss_of_the_Fur_Queen",
    primary_source_type="Doubleday Canada first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"residential school history",
         "description":"カナダ寄宿学校制度の民族誌的記録と並行。"}])

add(**C, name_ja="トーマス・キング『緑の草、流れる水』",
    name_en="King's Green Grass Running Water",
    name_original="Green Grass, Running Water",
    period_key="先住民文芸復興期",
    definition="Thomas King(Cherokee)が1993年に発表した長編。Coyoteと4つの先住民老人を介し聖書・西部劇・先住民史を脱構築する。",
    background="カナダ先住民ポストモダン小説の代表作。",
    development="先住民ユーモアと脱構築の方法的祖型。",
    historical_context="1990年代北米先住民ポストモダン文学期。",
    primary_source_url=WIKI+"Green_Grass,_Running_Water",
    primary_source_type="HarperCollins Canada first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トーマス・キング『不都合なインディアン』",
    name_en="King's The Inconvenient Indian",
    name_original="The Inconvenient Indian",
    period_key="先住民文芸復興期",
    definition="Kingが2012年に発表した北米先住民史エッセイ。'好都合な/不都合な/法的なインディアン'の三類型で500年史を批判的に整理。",
    background="北米先住民史の大衆的脱植民地化叙述。",
    development="2010年代北米先住民史叙述の規範作。",
    historical_context="2010年代北米先住民和解論議期。",
    primary_source_url=WIKI+"The_Inconvenient_Indian",
    primary_source_type="Doubleday Canada first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マリア・キャンベル『ハーフブリード』",
    name_en="Campbell's Halfbreed",
    name_original="Halfbreed",
    period_key="先住民文芸復興期",
    definition="Maria Campbell(Métis)が1973年に発表した自伝。サスカチュワンMétis女性の貧困・暴力・自己回復の物語でカナダ先住民自伝の古典。",
    background="カナダMétis女性自伝の制度的画期。",
    development="2019年完全版で削除された性暴力章節が復元。",
    historical_context="1970年代カナダ先住民活動主義興隆期。",
    primary_source_url=WIKI+"Maria_Campbell",
    primary_source_type="McClelland & Stewart first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"原版と復元版の差は、AI時代のテキスト編集介入と真正性問題の歴史的範例。",
         "related_ai_phenomenon":"AI編集介入とテクスト真正性"}])

add(**C, name_ja="エデン・ロビンソン『モンキー・ビーチ』",
    name_en="Robinson's Monkey Beach",
    name_original="Monkey Beach",
    period_key="先住民文芸復興期",
    definition="Eden Robinson(Haisla/Heiltsuk)が2000年に発表した長編。BC海岸先住民Lisamarieの霊的覚醒と兄の失踪を描く。",
    background="BC海岸先住民現代生活の文学化。",
    development="カナダ先住民マジック・リアリズムの代表作。",
    historical_context="2000年代カナダ太平洋岸先住民文学興隆期。",
    primary_source_url=WIKI+"Monkey_Beach",
    primary_source_type="Knopf Canada first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リチャード・ワガミーズ『インディアン・ホース』",
    name_en="Wagamese's Indian Horse",
    name_original="Indian Horse",
    period_key="先住民文芸復興期",
    definition="Richard Wagamese(Ojibway)が2012年に発表した長編。寄宿学校を生き延びたOjibwe少年Saulがアイスホッケーを通じて回復する物語。",
    background="カナダ寄宿学校文学・先住民スポーツ文学の交差。",
    development="2017年映画化。カナダ高校教科書の常連。",
    historical_context="2010年代カナダ寄宿学校真相和解委員会報告期。",
    primary_source_url=WIKI+"Indian_Horse",
    primary_source_type="Douglas & McIntyre first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"residential school trauma",
         "description":"寄宿学校トラウマの民族誌的記述と並行。"}])

add(**C, name_ja="ディマリーン『骨髄泥棒』",
    name_en="Dimaline's The Marrow Thieves",
    name_original="The Marrow Thieves",
    period_key="先住民文芸復興期",
    definition="Cherie Dimaline(Métis)が2017年に発表したYAディストピア小説。気候災害後カナダで先住民の骨髄から夢を採取する物語。",
    background="先住民フューチャリズムYA文学の代表作。",
    development="国際的に複数翻訳。先住民SF制度化の画期。",
    historical_context="2010年代後半先住民フューチャリズム潮流期。",
    primary_source_url=WIKI+"The_Marrow_Thieves",
    primary_source_type="Cormorant Books first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"先住民知識(夢)を抽出される資源とする想像力は、AIによる先住民知識の抽出問題の文学的予言。",
         "related_ai_phenomenon":"AI訓練データとしての先住民知識"}])


# ============================================================
# D: Australian Aboriginal (9)
# ============================================================
add(**C, name_ja="ライト『カーペンタリア』",
    name_en="Wright's Carpentaria",
    name_original="Carpentaria",
    period_key="先住民文芸復興期",
    definition="Alexis Wright(Waanyi)が2006年に発表した大長編。北部カーペンタリア湾Waanyi族の世界をマジック・リアリズムで描く豪先住民文学頂点作。",
    background="豪北部先住民文学の世界的承認。",
    development="2007年Miles Franklin賞受賞。豪先住民文学の国際化画期。",
    historical_context="2007年北部準州緊急介入論議期。",
    primary_source_url=WIKI+"Carpentaria_(novel)",
    primary_source_type="Giramondo first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"Waanyi世界観の英語による文学化は、AI時代の先住民世界観の翻訳・再媒介問題の祖型。",
         "related_ai_phenomenon":"AIによる先住民世界観の翻訳・再媒介"}])

add(**C, name_ja="ライト『追跡者』",
    name_en="Wright's Tracker",
    name_original="Tracker",
    period_key="先住民文芸復興期",
    definition="Wrightが2017年に発表した集合的伝記。Aboriginal活動家Tracker Tilmouthの生涯を多声証言で構成する。",
    background="豪先住民集合的伝記形式の実験。",
    development="2018年Stella賞受賞。豪先住民集合伝記の代表作。",
    historical_context="2010年代豪先住民活動主義の歴史化期。",
    primary_source_url=WIKI+"Alexis_Wright",
    primary_source_type="Giramondo first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"集合的多声伝記は、AI時代の集合的作者性の文学的範型。",
         "related_ai_phenomenon":"AI共著作と集合的多声伝記"}])

add(**C, name_ja="キム・スコット『あの死人の踊り』",
    name_en="Scott's That Deadman Dance",
    name_original="That Deadman Dance",
    period_key="先住民文芸復興期",
    definition="Kim Scott(Noongar)が2010年に発表した長編。19世紀西豪初期接触史をNoongar視点で描いた歴史小説。",
    background="西豪Noongar歴史の文学的脱植民地化。",
    development="2011年Miles Franklin賞受賞。",
    historical_context="2010年代豪西部先住民歴史見直し期。",
    primary_source_url=WIKI+"That_Deadman_Dance",
    primary_source_type="Picador Australia first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Noongar contact history",
         "description":"西豪Noongar接触史民族誌と並行。"}])

add(**C, name_ja="ウィンチ『収穫』",
    name_en="Winch's The Yield",
    name_original="The Yield",
    period_key="先住民文芸復興期",
    definition="Tara June Winch(Wiradjuri)が2019年に発表した長編。Wiradjuri語辞書を作る祖父の死後家族が土地と言語を取り戻す物語。",
    background="Wiradjuri言語復興運動の文学的結晶。",
    development="2020年Miles Franklin賞受賞。豪先住民言語復興文学の頂点。",
    historical_context="2010年代豪先住民言語復興運動期。",
    primary_source_url=WIKI+"Tara_June_Winch",
    primary_source_type="Hamish Hamilton Australia",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"絶滅危機言語の辞書化を物語の中核とする構造は、AI時代の言語多様性危機の文学的範型。",
         "related_ai_phenomenon":"AI低資源言語と先住民言語復興"}])

add(**C, name_ja="トニー・バーチ『ゴーストリヴァー』",
    name_en="Birch's Ghost River",
    name_original="Ghost River",
    period_key="先住民文芸復興期",
    definition="Tony Birch(Koori)が2015年に発表した長編。1960年代メルボルン河岸の少年たちと先住民老人の友情を描く。",
    background="豪都市先住民文学の代表作。",
    development="豪先住民児童・YA文学の規範作。",
    historical_context="2010年代豪都市先住民可視化期。",
    primary_source_url=WIKI+"Tony_Birch_(writer)",
    primary_source_type="University of Queensland Press",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サリー・モーガン『マイ・プレイス』",
    name_en="Morgan's My Place",
    name_original="My Place",
    period_key="先住民文芸復興期",
    definition="Sally Morgan(Palyku)が1987年に発表した自伝。'盗まれた世代'と先住民血統発見を描き豪で500K部超を売り上げた古典。",
    background="豪先住民自伝の制度的画期。",
    development="豪先住民自伝の規範作。学校教科書の常連。",
    historical_context="1980年代豪先住民和解運動初期。",
    primary_source_url=WIKI+"My_Place_(autobiography)",
    primary_source_type="Fremantle Press first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Stolen Generations testimony",
         "description":"盗まれた世代証言の文学的祖型。"}])

add(**C, name_ja="パスコー『ダーク・エミュー』",
    name_en="Pascoe's Dark Emu",
    name_original="Dark Emu",
    period_key="先住民文芸復興期",
    definition="Bruce Pascoeが2014年に発表した歴史評論。豪先住民の農業・定住・経済を初期植民地記録から再構築し豪先住民史認識を変えた。",
    background="豪先住民史の根本的見直し。",
    development="豪学校教科書改訂の論議の中心。",
    historical_context="2010年代豪先住民史見直し論争期。",
    primary_source_url=WIKI+"Dark_Emu",
    primary_source_type="Magabala Books first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"先住民農業・経済の歴史的可視化は、AI時代の先住民知識の認識論的再評価の祖型。",
         "related_ai_phenomenon":"AI時代の先住民知識の認識論的再評価"}])

add(**C, name_ja="ハイス『ティダス』",
    name_en="Heiss' Tiddas",
    name_original="Tiddas",
    period_key="先住民文芸復興期",
    definition="Anita Heiss(Wiradjuri)が2014年に発表した長編。ブリスベン先住民女性5人の友情を描く豪先住民現代女性小説の代表作。",
    background="豪先住民都市女性文学の制度化。",
    development="豪先住民商業文学の規範作。",
    historical_context="2010年代豪先住民女性文学興隆期。",
    primary_source_url=WIKI+"Anita_Heiss",
    primary_source_type="Simon & Schuster Australia",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルカショーンコ『あまりの口』",
    name_en="Lucashenko's Too Much Lip",
    name_original="Too Much Lip",
    period_key="先住民文芸復興期",
    definition="Melissa Lucashenko(Goorie/Bundjalung)が2018年に発表した長編。Bundjalung家族のブラックユーモアと暴力を描く。",
    background="豪先住民ブラックユーモア小説の代表作。",
    development="2019年Miles Franklin賞受賞。",
    historical_context="2010年代後半豪先住民文学多様化期。",
    primary_source_url=WIKI+"Melissa_Lucashenko",
    primary_source_type="University of Queensland Press",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: Pacific (8)
# ============================================================
add(**C, name_ja="イヒマエラ『ホエール・ライダー』",
    name_en="Ihimaera's The Whale Rider",
    name_original="The Whale Rider",
    period_key="先住民文芸復興期",
    definition="Witi Ihimaera(Te Aitanga-a-Māhaki)が1987年に発表した長編。Whangaraの少女Kahuがクジラ騎手の祖先伝承を継承する物語。",
    background="マオリ女性継承の文学化。",
    development="2002年映画化。マオリ文学の世界的普及画期。",
    historical_context="1980年代NZマオリ・ルネサンス期。",
    primary_source_url=WIKI+"The_Whale_Rider",
    primary_source_type="Heinemann NZ first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Māori whakapapa",
         "description":"マオリ系譜継承の民族誌的記述と並行。"}])

add(**C, name_ja="グレイス『ポティキ』",
    name_en="Grace's Potiki",
    name_original="Potiki",
    period_key="先住民文芸復興期",
    definition="Patricia Grace(Ngāti Toa/Ngāti Raukawa)が1986年に発表した長編。マオリ共同体の土地開発抵抗とWhānau継承を描く。",
    background="NZマオリ女性作家の制度的画期。",
    development="マオリ女性作家の規範作。",
    historical_context="1980年代NZマオリ土地権運動期。",
    primary_source_url=WIKI+"Patricia_Grace",
    primary_source_type="Penguin NZ first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハルメ『骨の人々』",
    name_en="Hulme's The Bone People",
    name_original="The Bone People",
    period_key="先住民文芸復興期",
    definition="Keri Hulme(Kāi Tahu)が1984年に発表した長編。マオリ・パケハ・親不在子の三角関係を描き1985年Booker賞受賞。",
    background="マオリ系作家による初のBooker受賞。",
    development="NZ先住民・移民・性暴力論議の文学的画期。",
    historical_context="1980年代NZ多文化主義論議期。",
    primary_source_url=WIKI+"The_Bone_People",
    primary_source_type="Spiral Collective first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"マオリ・パケハ・無言子の三角主体構築は、AI時代の混成的主体構築の文学的範型。",
         "related_ai_phenomenon":"AI時代の混成・多重主体構築"}])

add(**C, name_ja="ウェンド『帰郷の息子たち』",
    name_en="Wendt's Sons for the Return Home",
    name_original="Sons for the Return Home",
    period_key="先住民文芸復興期",
    definition="Albert Wendt(サモア)が1973年に発表した太平洋諸島文学の起点小説。サモア移民学生のNZ社会への対峙を描く。",
    background="太平洋諸島文学の制度的起点。",
    development="後のサモア・トンガ・フィジー文学全体に基礎的影響。",
    historical_context="1970年代NZ太平洋諸島移民可視化期。",
    primary_source_url=WIKI+"Albert_Wendt",
    primary_source_type="Longman Paul first edition",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フィギエル『私たちがかつて居た場所』",
    name_en="Figiel's Where We Once Belonged",
    name_original="Where We Once Belonged",
    period_key="先住民文芸復興期",
    definition="Sia Figiel(サモア)が1996年に発表した長編。サモア女性の集合主体と植民地化の交差を描き太平洋女性文学の画期。",
    background="サモア女性文学の制度的画期。",
    development="1997年Commonwealth Writers' Prize受賞。",
    historical_context="1990年代太平洋諸島女性文学興隆期。",
    primary_source_url=WIKI+"Sia_Figiel",
    primary_source_type="Pasifika Press first edition",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"サモア集合主体('we')の文学化は、AI時代の集合主体性の理論的祖型。",
         "related_ai_phenomenon":"AI時代の集合主体性"}])

add(**C, name_ja="サリヴァン『スター・ワカ』",
    name_en="Sullivan's Star Waka",
    name_original="Star Waka",
    period_key="先住民文芸復興期",
    definition="Robert Sullivan(Ngāpuhi)が1999年に発表した詩集。100の詩で太平洋航海カヌー(waka)を中核象徴として太平洋史を歌う。",
    background="マオリ詩の太平洋的拡張。",
    development="太平洋航海詩の現代範型。",
    historical_context="1990年代後半マオリ・太平洋諸島詩交流期。",
    primary_source_url=WIKI+"Robert_Sullivan_(poet)",
    primary_source_type="Auckland University Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Pacific navigation traditions",
         "description":"太平洋航海伝統の人類学的記録と詩的形式化。"}])

add(**C, name_ja="マーシュ『綱渡り』",
    name_en="Marsh's Tightrope",
    name_original="Tightrope",
    period_key="先住民文芸復興期",
    definition="Selina Tusitala Marsh(サモア/Tuvalu)が2017年に発表した詩集。NZ初の太平洋諸島系桂冠詩人(2017-19)の代表作。",
    background="NZ太平洋諸島系女性詩の制度化。",
    development="NZ国家詩人制度の太平洋諸島系化画期。",
    historical_context="2010年代後半NZ文学制度の多文化化期。",
    primary_source_url=WIKI+"Selina_Tusitala_Marsh",
    primary_source_type="Auckland University Press",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アヴィア『私のスカートの下の野犬』",
    name_en="Avia's Wild Dogs Under My Skirt",
    name_original="Wild Dogs Under My Skirt",
    period_key="先住民文芸復興期",
    definition="Tusiata Avia(サモア)が2004年に発表した詩集。サモア女性の身体・移民・暴力をパフォーマンス詩として書いた。",
    background="サモア女性パフォーマンス詩の代表作。",
    development="2020年代豪NZツアー演劇化された太平洋諸島系詩の画期作。",
    historical_context="2000年代太平洋諸島系女性パフォーマンス詩興隆期。",
    primary_source_url=WIKI+"Tusiata_Avia",
    primary_source_type="Victoria University Press",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: Ainu literature (4)
# ============================================================
add(**CJ, name_ja="知里幸恵『アイヌ神謡集』",
    name_en="Chiri Yukie's Ainu Shin'yoshu",
    name_original="アイヌ神謡集",
    period_key="植民地接触・抑圧期",
    definition="知里幸恵(1903-22)が1923年に岩波書店から刊行したカムイユカラ13編のローマ字・日本語対訳集。アイヌ口承文学初の自著刊行。",
    background="北海道アイヌ口承文学の自著書記化の画期。",
    development="アイヌ口承文学研究の出発点。日本文学全集収録の規範作。",
    historical_context="1923年大正期同化政策下のアイヌ自著刊行。",
    primary_source_url="https://www.aozora.gr.jp/cards/000284/card4344.html",
    primary_source_type="青空文庫: アイヌ神謡集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"アイヌ口承の自著ローマ字書記化は、AI時代の少数言語の自記録・自表象の祖型。",
         "related_ai_phenomenon":"AI時代の少数言語の自記録・自表象"},
        {"axis":"言語","status":"rethinking",
         "rationale":"アイヌ語のローマ字書記化はAIの低資源言語処理の歴史的前提を成す。",
         "related_ai_phenomenon":"AI低資源言語処理"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Ainu ethnopoetics",
         "description":"アイヌ口承の人類学的研究と並行。"}])

add(**CJ, name_ja="バチェラー『アイヌ詞曲集』",
    name_en="Batchelor's Ainu collection",
    name_original="Ainu Folk-Lore",
    period_key="植民地接触・抑圧期",
    definition="John Batchelor(1854-1944)による19世紀末-20世紀初頭のアイヌ口承記録。'Ainu Folk-Lore'(1901)等で英語圏に紹介。",
    background="英国宣教師による北海道アイヌ口承記録。",
    development="20世紀アイヌ口承研究の英語圏的基礎。",
    historical_context="明治期アイヌ同化政策と外国人宣教師記録の交差。",
    primary_source_url=ARCH+"ainufolklorelegen00batc",
    primary_source_type="Internet Archive: Batchelor 'Ainu Folk-Lore'",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**CJ, name_ja="萱野茂『カムイユカラ』",
    name_en="Kayano's Kamuy Yukar collection",
    name_original="萱野茂のアイヌ神話集成",
    period_key="先住民文芸復興期",
    definition="萱野茂(1926-2006)が記録・出版したアイヌカムイユカラ集成。'カムイユカラと昔話'(1988)等でアイヌ口承を体系化。",
    background="戦後北海道二風谷アイヌ口承の現地記録化。",
    development="アイヌ口承文学全集刊行の中核。",
    historical_context="1980-90年代アイヌ文化伝承運動期。",
    primary_source_url=WIKIJA+"萱野茂",
    primary_source_type="平凡社東洋文庫: 萱野茂のアイヌ神話集成",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Ainu ethnography",
         "description":"二風谷アイヌ民族誌・言語学との直接接続。"}])

add(**CJ, name_ja="現代アイヌ詩",
    name_en="Contemporary Ainu poetry",
    name_original="現代アイヌ詩",
    period_key="先住民文芸復興期",
    definition="2010-20年代の現代アイヌ詩の潮流。坂田美奈子・違星北斗系譜の継承等。アイヌ語復興と日本語表現の交差で展開する現代詩。",
    background="2019年アイヌ施策推進法以降の文化復興期。",
    development="現代アイヌ作家世代の制度的定着過程。",
    historical_context="2019年アイヌ民族支援法成立後の文化復興期。",
    primary_source_url=WIKIJA+"アイヌ文学",
    primary_source_type="ウポポイ国立アイヌ民族博物館アーカイブ",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"アイヌ語復興と日本語表現の同時並存は、AI時代の多言語・継承言語処理の文学的範型。",
         "related_ai_phenomenon":"AI時代の継承言語の文学的処理"}])


# ============================================================
# G: African oral cont., S Asian Adivasi, AI sov. (4)
# ============================================================
add(**C, name_ja="ハッザ・ヌオ歌",
    name_en="Hadza n!ow songs",
    name_original="Hadza n!ow",
    period_key="先住民口承伝統期",
    definition="タンザニア・ハッザ族の狩猟成功儀礼歌。男性が大型獲物仕留め後に歌う声楽伝統で世界最古級狩猟採集口承の一つ。",
    background="ハッザ族(現存の主要狩猟採集民)の口承伝統。",
    development="21世紀人類学・音楽学の主要研究対象。",
    historical_context="2010年代以降ハッザ録音保存運動期。",
    primary_source_url="https://www.endangeredlanguages.com/lang/hts",
    primary_source_type="Endangered Languages Project: Hadza",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Hadza ethnography",
         "description":"ハッザ民族誌の音楽学的記録。"}])

add(**C, name_ja="ビルサ・ムンダ叙事詩",
    name_en="Birsa Munda Ulgulan ballads",
    name_original="Birsa Munda Ulgulan",
    period_key="植民地接触・抑圧期",
    definition="インド・ジャールカンドのMunda族指導者Birsa Munda(1875-1900)のUlgulan反乱を歌うAdivasi口承叙事詩群。",
    background="インドAdivasi反植民地運動の口承的記憶。",
    development="2000年代以降インドAdivasi文学運動の中核象徴。",
    historical_context="1899-1900年Ulgulan反乱と現代Adivasi主権論議。",
    primary_source_url=WIKI+"Birsa_Munda",
    primary_source_type="Indian Anthropological Survey archives",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Adivasi ethnohistory",
         "description":"Adivasi抵抗史の人類学的記述と並行。"}])

add(**C, name_ja="GIDA先住民データ主権",
    name_en="GIDA Indigenous Data Sovereignty",
    name_original="Global Indigenous Data Alliance (GIDA)",
    period_key="先住民文芸復興期",
    definition="2018年設立のGIDAが推進する先住民データ主権運動。CARE原則(2019)を策定しFAIR原則と並ぶデータ管理国際枠組を確立。",
    background="2010年代世界先住民データ運動の制度的結晶。",
    development="2020年代AI訓練データ問題への先住民側の制度的応答。",
    historical_context="2020年代生成AI急速進展と先住民データ抽出論議期。",
    primary_source_url="https://www.gida-global.org/",
    primary_source_type="GIDA official archive: CARE Principles",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"CARE原則は集合所有・条件付きアクセスを技術的に実装する枠組で、無制限抽出AI訓練と根本的に対立。",
         "related_ai_phenomenon":"CARE原則とAI訓練データ管理"},
        {"axis":"知の形式","status":"rethinking",
         "rationale":"先住民データ主権は、AI時代の知識所有・流通の根本的再編の制度的画期。",
         "related_ai_phenomenon":"AI時代の知識所有・流通の再編"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"data sovereignty",
         "description":"人類学的データ倫理の発展形。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"data governance for AI",
         "description":"AI時代のデータガバナンス枠組。"}])

add(**C, name_ja="先住民プロトコルAIワーキンググループ",
    name_en="Indigenous Protocol & AI Working Group",
    name_original="Indigenous Protocol and AI Position Paper",
    period_key="先住民文芸復興期",
    definition="2019年Jason Edward Lewis主導でCanadian Institute for Advanced Researchが組織。'Indigenous Protocol and AI Position Paper'(2020)を策定。",
    background="2010年代後半世界先住民AI運動の制度的結晶。",
    development="2020年代国際AI倫理枠組への先住民視点の制度的組み込み。",
    historical_context="2020年代国際AI倫理規範策定期。",
    primary_source_url="https://spectrum.library.concordia.ca/id/eprint/986506/",
    primary_source_type="Concordia: Indigenous Protocol and AI Position Paper (PD)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"先住民プロトコルに従うAI開発は、汎用主体前提のAI開発の根本的代替モデル。",
         "related_ai_phenomenon":"プロトコル制約付きAI開発"},
        {"axis":"知の形式","status":"rethinking",
         "rationale":"先住民認識論に基づくAI設計は、AI開発の認識論的多元化の制度的画期。",
         "related_ai_phenomenon":"認識論的多元的AI設計"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"Indigenous AI ethics",
         "description":"国際AI倫理規範の先住民化の中心文書。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"protocol-based research ethics",
         "description":"先住民プロトコル研究倫理のAIへの拡張。"}])


# ============================================================
# Attach extra fourth_transform tags (target >= 20) and cross_domain (>= 14)
# ============================================================
def _attach_axes(name: str, ax_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("fourth_axes", [])
            c["fourth_axes"] = existing + ax_list
            return


def _attach_cross(name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


# Additional fourth_transform tags (heavy on authorship/voice/authenticity)
_attach_axes("モマデイ『雨山への道』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"三声構成は口承・歴史・自伝の真正性層を分離・統合。AI時代の多層真正性の方法的祖型。",
     "related_ai_phenomenon":"AI生成における多層的真正性"}])
_attach_axes("シルコ『死者の暦』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"汎米先住民予言を語る作者性は集合作者・神秘的作者の混合。AI時代の予言的作者の祖型。",
     "related_ai_phenomenon":"AI生成における集合・予言的作者性"}])
_attach_axes("ウェルチ『冬の血』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"無名語り手のミニマリスト語りは、AI生成の匿名・最小語り構造の文学的祖型。",
     "related_ai_phenomenon":"AI生成における匿名・最小語り"}])
_attach_axes("アードリック『ラブ・メディスン』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"連作多視点構造は集合作者性の文学的範型。AI協働物語の祖型。",
     "related_ai_phenomenon":"AI協働物語と多視点作者性"}])
_attach_axes("アレクシー『ローン・レンジャー』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"先住民ステレオタイプを内側から脱構築する真正性の方法。AI時代のステレオタイプ批判の文学的祖型。",
     "related_ai_phenomenon":"AI生成におけるステレオタイプ脱構築"}])
_attach_axes("ハージョ『彼女は何頭かの馬を持っていた』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"リトレイン構造による反復・差異の詩学は、AI生成の反復・差異構造の文学的祖型。",
     "related_ai_phenomenon":"AI生成における反復と差異"}])
_attach_axes("ホーガン『ソーラー・ストームズ』", [
    {"axis":"知の形式","status":"rethinking",
     "rationale":"先住民環境知の文学的具体化は、AI時代の環境知識の認識論的位置づけの祖型。",
     "related_ai_phenomenon":"AI時代の環境知識の認識論"}])
_attach_axes("リサ・ブルックス『共有の鍋』", [
    {"axis":"知の形式","status":"rethinking",
     "rationale":"地理的共有概念は、AI時代の知識共有の地理的根拠の理論的祖型。",
     "related_ai_phenomenon":"AI知識共有の地理的根拠"}])
_attach_axes("ハイウェイ『リズ姉妹』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"Cree語と英語の混成戯曲言語は、AI時代の混成言語生成の文学的祖型。",
     "related_ai_phenomenon":"AI混成言語生成"}])
_attach_axes("トーマス・キング『緑の草、流れる水』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"Coyote脱構築は、AI生成における伝統物語の脱構築方法の文学的祖型。",
     "related_ai_phenomenon":"AI生成における伝統物語脱構築"}])
_attach_axes("エデン・ロビンソン『モンキー・ビーチ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"霊的覚醒主体は、AI時代の霊的・拡張主体の文学的範型。",
     "related_ai_phenomenon":"AI時代の拡張主体性"}])
_attach_axes("キム・スコット『あの死人の踊り』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"Noongar視点による接触史叙述は、AI時代の被植民地視点の真正性復元の祖型。",
     "related_ai_phenomenon":"AI生成における被植民地視点真正性"}])
_attach_axes("トニー・バーチ『ゴーストリヴァー』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"都市Koori作者性は、AI時代の都市先住民作者性の文学的範型。",
     "related_ai_phenomenon":"AI時代の都市先住民作者性"}])
_attach_axes("ハイス『ティダス』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"先住民商業文学の作者主体は、AI時代の作者性の商業化問題の文学的祖型。",
     "related_ai_phenomenon":"AI時代の作者性商業化"}])
_attach_axes("ルカショーンコ『あまりの口』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"Bundjalung系の毒舌・ユーモア言語は、AI生成の文体特異性の文学的範型。",
     "related_ai_phenomenon":"AI生成の文体特異性"}])
_attach_axes("グレイス『ポティキ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"Whānau継承作者性は、AI時代の集合・親族作者性の文学的範型。",
     "related_ai_phenomenon":"AI時代の親族・集合作者性"}])
_attach_axes("ウェンド『帰郷の息子たち』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"移民の二重帰属主体は、AI時代の境界主体性の文学的祖型。",
     "related_ai_phenomenon":"AI時代の境界主体性"}])
_attach_axes("バチェラー『アイヌ詞曲集』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"外国人記録者によるアイヌ口承の真正性問題は、AI時代の他者記録の真正性論議の祖型。",
     "related_ai_phenomenon":"AI生成における他者記録真正性"}])


# Additional cross_domain links (target AN >= 14)
_attach_cross("モマデイ『雨山への道』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"life history method",
     "description":"先住民ライフヒストリー法の文学的祖型。"}])
_attach_cross("シルコ『死者の暦』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"pan-American indigeneity",
     "description":"汎米先住民人類学的範疇との接続。"}])
_attach_cross("シルコ『ストーリーテラー』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"family storytelling ethnography",
     "description":"家族口承民族誌との直接接続。"}])
_attach_cross("ウェルチ『冬の血』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"reservation life ethnography",
     "description":"保留地生活民族誌との並行。"}])
_attach_cross("ハージョ『クレイジー・ブレイヴ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Mvskoke ethnohistory",
     "description":"Mvskoke民族史記述と並行。"}])
_attach_cross("オレンジ『ゼア・ゼア』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"urban Indian studies",
     "description":"都市先住民研究との直接接続。"}])
_attach_cross("ロング・ソルジャー『ホエレアズ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"settler legal language critique",
     "description":"入植者法的言語批判の人類学と並行。"}])
_attach_cross("ジャスティス『なぜ先住民文学が重要か』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"relational ethics",
     "description":"関係論的倫理学と文学理論の接続。"}])
_attach_cross("ヴァイン・デロリア『カスターは罪を背負って死んだ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"reflexive anthropology",
     "description":"反省的人類学(reflexive anthropology)の発生契機。"}])
_attach_cross("マリア・キャンベル『ハーフブリード』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Métis ethnohistory",
     "description":"Métis民族史記述との直接接続。"}])
_attach_cross("ライト『カーペンタリア』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Waanyi ethnography",
     "description":"Waanyi民族誌との並行。"}])
_attach_cross("グレイス『ポティキ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Māori land ethnography",
     "description":"マオリ土地民族誌と並行。"}])
_attach_cross("ウェンド『帰郷の息子たち』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Pacific migration ethnography",
     "description":"太平洋移民民族誌の文学的祖型。"}])
_attach_cross("マーシュ『綱渡り』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Pacific feminist anthropology",
     "description":"太平洋諸島系フェミニスト人類学と並行。"}])
_attach_cross("アヴィア『私のスカートの下の野犬』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"Pacific body anthropology",
     "description":"太平洋諸島身体人類学と並行。"}])
_attach_cross("バチェラー『アイヌ詞曲集』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"missionary ethnography",
     "description":"宣教師民族誌記録の典型例。"}])
_attach_cross("現代アイヌ詩", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"contemporary Ainu revival",
     "description":"現代アイヌ復興の人類学的記述と並行。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(name_ja=nj, region=REGION,
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
        print(f"[c30 w17 add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c30 w17 add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c30 w17 add60] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
