"""LIT-DB Phase 2 Wave 14 — C03: European Medieval Literature (+60).

Subfield: lit_eu_medieval (id=2), region='西欧'.
Sources: Project Gutenberg, Wikisource, MGH Digital, Bibliotheca Augustana,
The Latin Library, Lyrik des Mittelalters, BnF Gallica.
>= 80% primary tier; fourth_transform_tags >= 16; cross_domain >= 12.

Adds 60 NEW concepts on top of existing 81, covering:
  A: Italian medieval extensions (10)
  B: Old French / Anglo-Norman extensions (10)
  C: Provençal / Troubadour expanded (8)
  D: Iberian medieval (10)
  E: German medieval extensions (8)
  F: English Middle expanded (7)
  G: Northern + Latin medieval + Slavic (7)
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("中世盛期イタリア", "Italian High Medieval", 1200, 1375,
     "シチリア派からドルチェ・スティル・ノーヴォ、ダンテ・ペトラルカ・ボッカッチョの世紀"),
    ("中世フランス古典期", "Old French Classical", 1100, 1300,
     "シャンソン・ド・ジェスト、宮廷ロマン、ファブリオー、寓意詩の隆盛期"),
    ("オック語抒情詩期", "Occitan Lyric", 1100, 1300,
     "プロヴァンス・トルバドゥール抒情詩の黄金期と十字軍以降の継承期"),
    ("イベリア中世", "Iberian Medieval", 1140, 1500,
     "カスティーリャ叙事詩・ガリシア=ポルトガル抒情詩・15世紀カンシオネーロ期"),
    ("中高ドイツ語期", "Middle High German", 1170, 1350,
     "ホーエンシュタウフェン期の宮廷叙事詩・抒情詩・中世神秘主義散文期"),
    ("中英語盛期", "Middle English High", 1300, 1500,
     "プランタジネット朝後期からテューダー初期にいたる中英語文学盛期"),
    ("北方中世", "Northern Medieval", 800, 1300,
     "古英語・古サクソン・古ノルド・古アイスランド文学の継承期"),
    ("中世ラテン文学", "Medieval Latin Literature", 800, 1400,
     "カロリング・ルネサンス以降の聖職者・宮廷ラテン詩・散文の発展期"),
    ("中世スラヴ", "Medieval Slavic", 1000, 1400,
     "キエフ・ルーシから中世ロシア語圏文学の生成期"),
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
WSRC_LA = "https://la.wikisource.org/wiki/"
WSRC_PT = "https://pt.wikisource.org/wiki/"
BIBA = "https://www.hs-augsburg.de/~harsch/augustana.html"
LATLIB = "https://www.thelatinlibrary.com/"
MGH = "https://www.dmgh.de/"
GALLICA = "https://gallica.bnf.fr/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_medieval", region="西欧", original_script="roman")
CCYR = dict(subfield_code="lit_eu_medieval", region="西欧", original_script="cyrillic")


# ============================================================
# A: イタリア中世 拡張（10）
# ============================================================
add(**C, name_ja="ダンテ『饗宴（コンヴィヴィオ）』",
    name_en="Dante's Convivio",
    name_original="Convivio",
    period_key="中世盛期イタリア",
    definition="ダンテが1304-07年頃イタリア俗語で著した未完の哲学的注釈集。3篇のカンツォーネに散文注釈を付し、知識の宴(convivium)として俗語による哲学的言説の正当性を主張した。アリストテレス・ボエティウス哲学の俗語化の先駆作で、『神曲』の知的母胎となった。",
    background="ダンテのフィレンツェ追放期の知的彷徨と、俗語による哲学的言説の制度化の試み。",
    development="『俗語論』『神曲』のラテン語＝俗語論争に直接連結し、ペトラルカ・ボッカッチョ俗語擁護論の先駆となった。",
    historical_context="14世紀初頭イタリア中部都市国家の知識人ネットワークと俗語学術文化の生成。",
    primary_source_url=WSRC_IT+"Convivio",
    primary_source_type="Wikisource (it): Convivio",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ダンテ『帝政論（モナルキア）』",
    name_en="Dante's Monarchia",
    name_original="De Monarchia",
    period_key="中世盛期イタリア",
    definition="ダンテが1313年頃ラテン語で著した政治論3巻。普遍的世界帝国の必要性、ローマ帝国の正当性、皇帝権と教皇権の独立を論証した。グェルフ・ギベリン抗争の思想的決算で、教皇権主義に対する文学者の政治論として中世ヨーロッパ政治思想史の主要文献となった。",
    background="14世紀初頭イタリア都市国家のグェルフ・ギベリン党争と、神聖ローマ皇帝ハインリヒ7世イタリア遠征。",
    development="ダンテ政治思想の集大成として、近代国家論・教皇権批判の先駆として再評価された。",
    historical_context="教皇権至上主義(papalism)に対する皇帝主義文学者の応答として、14世紀政治神学論争に位置する。",
    primary_source_url=LATLIB+"dante.monarchia.html",
    primary_source_type="Latin Library: Dante Monarchia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボッカッチョ『フィロストラート』",
    name_en="Boccaccio's Filostrato",
    name_original="Il Filostrato",
    period_key="中世盛期イタリア",
    definition="ボッカッチョが1335年頃ナポリで著したオッターヴァ・リーマによる長編物語詩。トロイア戦争を背景にトロイラスとクリセイダの恋愛悲劇を語り、チョーサー『トロイラスとクリセイデ』の直接の典拠となった。中世イタリア俗語ロマンスの代表作で、シェイクスピア『トロイラスとクレシダ』までの長い文学系譜を起こした。",
    background="アンジュー朝ナポリ宮廷文化と古代再受容の文脈、ボッカッチョのナポリ滞在期。",
    development="チョーサー、シェイクスピア『トロイラスとクレシダ』、近世トロイア物語の祖型となった。",
    historical_context="14世紀ナポリ宮廷の俗語文学興隆と、古代物語の中世化の文化的局面。",
    primary_source_url=WSRC_IT+"Filostrato",
    primary_source_type="Wikisource (it): Il Filostrato",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ボッカッチョ『テセイダ』",
    name_en="Boccaccio's Teseida",
    name_original="Teseida delle nozze d'Emilia",
    period_key="中世盛期イタリア",
    definition="ボッカッチョが1339-41年頃ナポリで著したオッターヴァ・リーマによる12巻叙事詩。テセウスの遠征を枠組としてアルチータとパラモンの恋愛抗争を描く。中世俗語による古典叙事詩模倣の先駆作で、チョーサー『騎士の物語』、シェイクスピア＝フレッチャー『高貴な親類』の典拠となった。",
    background="アンジュー朝ナポリ宮廷の古典再受容と俗語叙事詩確立の試み。",
    development="チョーサー『騎士の物語』、ルネサンス叙事詩、シェイクスピア『高貴な親類』に継承された。",
    historical_context="14世紀イタリア俗語による古典模倣の文化的制度化期。",
    primary_source_url=WSRC_IT+"Teseida",
    primary_source_type="Wikisource (it): Teseida",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="グイド・カヴァルカンティ『ドンナ・ミ・プレガ』",
    name_en="Cavalcanti's Donna me prega",
    name_original="Donna me prega",
    period_key="中世盛期イタリア",
    definition="グイド・カヴァルカンティ(c.1255-1300)が著した愛の本性に関する哲学的カンツォーネ。アヴェロエス的能動知性論を背景に、愛の生理学的・心理学的・形而上学的構造を論じた。ドルチェ・スティル・ノーヴォ理論詩の頂点で、ダンテ・ポンドの近代主義詩学にいたる長い系譜を起こした。",
    background="13世紀末フィレンツェ知識人サークルにおけるアヴェロエス受容と、宮廷恋愛論の哲学的精緻化。",
    development="ダンテ『新生』『神曲』、エズラ・パウンド『カントス』第36歌、20世紀近代主義詩学に継承された。",
    historical_context="13世紀末イタリア俗語抒情詩のスコラ哲学化と理論化の文化的局面。",
    primary_source_url=WSRC_IT+"Donna_me_prega",
    primary_source_type="Wikisource (it): Donna me prega",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"愛を能動知性の作用として論じる中世哲学詩学は、AI生成における「主体なき創造」概念と理論的に共振する。",
         "related_ai_phenomenon":"LLMにおける主体なき詩的生成と能動的処理の関係"}])

add(**C, name_ja="チーノ・ダ・ピストイア",
    name_en="Cino da Pistoia",
    name_original="Cino da Pistoia",
    period_key="中世盛期イタリア",
    definition="チーノ・ダ・ピストイア(c.1270-1336)はトスカーナ出身の法学者・詩人。ボローニャ・ナポリで法学を講じつつ、ドルチェ・スティル・ノーヴォ最晩期の代表詩人として137篇の俗語抒情詩を遺した。ダンテ・ペトラルカ双方に直接影響を与え、ペトラルキスム抒情詩の橋渡しとなった。",
    background="14世紀初頭イタリア法学界と俗語抒情詩界が交錯する知識人文化の典型。",
    development="ペトラルカはチーノを師の一人として明示的に言及し、近世イタリア抒情詩の主流に継承された。",
    historical_context="14世紀イタリア法学・文学・哲学が結節する都市知識人文化の中心局面。",
    primary_source_url=WSRC_IT+"Autore:Cino_da_Pistoia",
    primary_source_type="Wikisource (it): Cino da Pistoia",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラポ・ジャンニ",
    name_en="Lapo Gianni",
    name_original="Lapo Gianni",
    period_key="中世盛期イタリア",
    definition="ラポ・ジャンニ(13世紀後半-14世紀初頭活動)はフィレンツェのドルチェ・スティル・ノーヴォ詩人。ダンテのソネット『グイド、私は願う』(Vita Nuova以前)で名指しで言及され、カヴァルカンティ・ダンテと並ぶスティル・ノーヴォ初期サークルの中核メンバー。約20篇の抒情詩が遺り、軽やかな宮廷恋愛詩風を確立した。",
    background="13世紀末フィレンツェのスティル・ノーヴォ詩人サークル形成。",
    development="ペトラルキスム抒情詩の系譜に吸収され、近世イタリア抒情詩の素材となった。",
    historical_context="フィレンツェ俗語抒情詩のサークル制度化の局面。",
    primary_source_url=WSRC_IT+"Autore:Lapo_Gianni",
    primary_source_type="Wikisource (it): Lapo Gianni",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブルネット・ラティーニ『テゾレット』",
    name_en="Brunetto Latini's Tesoretto",
    name_original="Il Tesoretto",
    period_key="中世盛期イタリア",
    definition="ブルネット・ラティーニ(c.1220-94)が13世紀後半に著した俗語7音節詩による寓意詩。フランス亡命中の自伝的旅と、自然・徳・愛の女神らとの寓意的遭遇を語る。ダンテ『神曲』の地獄篇第15歌でラティーニが登場し、『神曲』寓意旅構造の直接的先駆と研究される。",
    background="13世紀フィレンツェ亡命知識人のフランス的寓意詩の摂取と俗語化。",
    development="ダンテ『神曲』の旅構造・寓意システムに直接影響した。",
    historical_context="13世紀後半グェルフ・ギベリン抗争期フィレンツェ亡命知識人の文化生産。",
    primary_source_url=WSRC_IT+"Il_Tesoretto",
    primary_source_type="Wikisource (it): Il Tesoretto",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジャコモ・ダ・レンティーニ",
    name_en="Giacomo da Lentini",
    name_original="Giacomo da Lentini",
    period_key="中世盛期イタリア",
    definition="ジャコモ・ダ・レンティーニ(c.1210-60頃活動)はシチリア派詩人で、ホーエンシュタウフェン皇帝フリードリヒ2世パレルモ宮廷の公証人。ソネット形式の発明者として伝統的に位置づけられ、約40篇の抒情詩が遺る。トルバドゥール抒情詩のシチリア俗語化を主導し、イタリア抒情詩の制度的起源を画した。",
    background="13世紀前半フリードリヒ2世パレルモ宮廷のトルバドゥール文化受容と俗語抒情詩生成。",
    development="ソネット形式は『新生』『カンツォニエーレ』を経て近世ヨーロッパ抒情詩の主要形式となった。",
    historical_context="ホーエンシュタウフェン宮廷文化の文学的多元性とイタリア俗語抒情詩の制度的開始。",
    primary_source_url=WSRC_IT+"Autore:Giacomo_da_Lentini",
    primary_source_type="Wikisource (it): Giacomo da Lentini",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヤコポーネ・ダ・トーディ『おお美しき母なる愛』",
    name_en="Iacopone da Todi's Donna de Paradiso",
    name_original="Donna de Paradiso (Lauda)",
    period_key="中世盛期イタリア",
    definition="ヤコポーネ・ダ・トーディ(c.1230-1306)が著した代表的ラウダ。マリアと十字架下の対話を劇形式で構成し、中世イタリア俗語劇詩の傑作とされる。フランチェスコ会・ジョッリーニ派(精神派)の宗教的緊張を背景に、感情的・劇的・俗語的な宗教詩学を確立した。",
    background="13世紀末フランチェスコ会精神派と教皇庁の対立、ボニファティウス8世投獄期。",
    development="14-15世紀ラウダ劇、サクラ・ラプレゼンタツィオーネ、近世宗教劇に継承された。",
    historical_context="13世紀末イタリア俗語宗教詩学とフランチェスコ会霊性運動の文学的結晶。",
    primary_source_url=WSRC_IT+"Donna_de_Paradiso",
    primary_source_type="Wikisource (it): Donna de Paradiso",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 古フランス語／アングロ＝ノルマン 拡張（10）
# ============================================================
add(**C, name_ja="『ロマン・ド・ルナール』",
    name_en="Roman de Renart",
    name_original="Le Roman de Renart",
    period_key="中世フランス古典期",
    definition="12-13世紀フランスで複数作者により編まれた狐ルナールを主人公とする叙事詩集。動物社会の風刺寓意を通じて封建社会・教会・宮廷を諷した。ヨーロッパ獣譚の最大集成で、ゲーテ『ライネケ狐』までの長い系譜を起こし、中世風刺文学の頂点を成した。",
    background="12-13世紀北フランス封建社会の制度的緊張と説教例話の獣譚化。",
    development="低地ドイツ『ライネケ』、ゲーテ詩劇、近代寓意風刺の祖型となった。",
    historical_context="12-13世紀北フランス・ロイヤル都市文化と封建批判詩学の生成。",
    primary_source_url=GALLICA+"ark:/12148/btv1b6000770b",
    primary_source_type="BnF Gallica: Roman de Renart manuscripts",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロベール・ド・ボロン『アリマタヤのヨセフ』",
    name_en="Robert de Boron's Joseph d'Arimathie",
    name_original="Joseph d'Arimathie",
    period_key="中世フランス古典期",
    definition="ロベール・ド・ボロンが12世紀末-13世紀初頭に著した韻文ロマン。聖杯のキリスト教化を主導し、最後の晩餐の聖杯がアリマタヤのヨセフによりブリテン島に運ばれる前史を構築した。後の『散文聖杯サイクル(ヴルガート)』の核となり、聖杯神話の正典化を画した。",
    background="第三十字軍以降の聖遺物崇敬と、アーサー王物語のキリスト教神学化の流れ。",
    development="散文聖杯サイクル、マロリー、19世紀以降ワーグナー『パルジファル』に継承された。",
    historical_context="13世紀初頭フランス王権・シトー会霊性・聖遺物崇敬が結節する宗教文化局面。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k5435596z",
    primary_source_type="BnF Gallica: Joseph d'Arimathie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァース『ブリュ物語』",
    name_en="Wace's Roman de Brut",
    name_original="Roman de Brut",
    period_key="中世フランス古典期",
    definition="ジャージー出身のヴァース(c.1110-1174)が1155年に著したアングロ・ノルマン語による叙事詩。ジェフリー・オブ・モンマス『ブリタニア列王史』をフランス語化し、アーサー王物語に「円卓」の発明を加えた。プランタジネット朝アンリ2世王妃エレオノール・ダキテーヌに献呈され、宮廷ロマンの基盤となった。",
    background="アンジュー帝国期(アンリ2世)のアーサー王物語の宮廷文学化と王朝正統化。",
    development="ラヤモン『ブルート』、クレチアン宮廷ロマン、円卓モチーフの全ヨーロッパ拡散の起点。",
    historical_context="12世紀後半プランタジネット宮廷の文学的多言語性と王権神話の制度化。",
    primary_source_url=WSRC_FR+"Roman_de_Brut",
    primary_source_type="Wikisource (fr): Roman de Brut",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァース『ル―物語』",
    name_en="Wace's Roman de Rou",
    name_original="Roman de Rou",
    period_key="中世フランス古典期",
    definition="ヴァースが1160-74年に著したアングロ・ノルマン語によるノルマンディー公家年代記詩。ヘンリー2世の依頼でロロ以降のノルマン公家の歴史を語り、未完で中断。中世王朝史詩の代表作で、ノルマン征服神話の文学的整備を主導した。",
    background="プランタジネット朝の王朝正統化事業の一環としてのノルマンディー公家史の文学化。",
    development="近世フランス王朝史詩、19世紀ノルマン研究の主要原典資料となった。",
    historical_context="12世紀後半アングロ・ノルマン宮廷における王朝記憶の文学的構築。",
    primary_source_url=WSRC_FR+"Roman_de_Rou",
    primary_source_type="Wikisource (fr): Roman de Rou",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ベルール『トリスタン』",
    name_en="Béroul's Tristan",
    name_original="Tristan (Béroul)",
    period_key="中世フランス古典期",
    definition="12世紀後半ノルマンディーで活動したベルールが著した古フランス語『トリスタン』断片。共通版(version commune)と分類され、原始的・口承的・粗野な伝統に近いとされる。トマ版と双璧をなすトリスタン物語の二大原典の一つで、ヨーロッパ恋愛神話の核心テクスト。",
    background="12世紀後半北フランスのケルト系恋愛神話の俗語文学化。",
    development="ゴットフリート・フォン・シュトラスブルク、ワーグナー、20世紀ベディエ再構成研究の基礎資料。",
    historical_context="12世紀北フランスにおける口承伝統と書記文学の交差局面。",
    primary_source_url=WSRC_FR+"Le_Roman_de_Tristan_(B%C3%A9roul)",
    primary_source_type="Wikisource (fr): Tristan (Béroul)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トマ『トリスタン』",
    name_en="Thomas of Britain's Tristan",
    name_original="Tristan (Thomas)",
    period_key="中世フランス古典期",
    definition="12世紀後半アングロ・ノルマン宮廷で活動したトマが著したアングロ・ノルマン語『トリスタン』断片。宮廷版(version courtoise)と分類され、洗練された宮廷的・心理的な恋愛分析を特徴とする。ゴットフリート・フォン・シュトラスブルク『トリスタン』の直接の典拠で、心理的恋愛詩学の系譜を起こした。",
    background="プランタジネット宮廷の宮廷文化と、洗練された恋愛心理学の文学化。",
    development="ゴットフリート、ワーグナー、20世紀宮廷恋愛研究の中心テクスト。",
    historical_context="12世紀後半アングロ・ノルマン宮廷の洗練された宮廷恋愛詩学の制度化。",
    primary_source_url=WSRC_FR+"Tristan_(Thomas)",
    primary_source_type="Wikisource (fr): Tristan (Thomas)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クレチアン・ド・トロワ『クリジェス』",
    name_en="Chrétien de Troyes's Cligès",
    name_original="Cligès",
    period_key="中世フランス古典期",
    definition="クレチアン・ド・トロワが1170年代に著した古フランス語ロマン。ビザンティン皇子クリジェスとアリス公女フェニスの恋愛を主題に、トリスタン物語の枠組を批判的に再演した「アンチ・トリスタン」と評される。クレチアン宮廷ロマンのトリスタン論の最重要テクスト。",
    background="12世紀後半シャンパーニュ伯マリ宮廷における宮廷恋愛論の精緻化。",
    development="13世紀以降のロマン詩学、シェイクスピア『シンベリン』までの恋愛擬死モチーフの起源。",
    historical_context="12世紀後半フランス・シャンパーニュ宮廷の宮廷恋愛論争。",
    primary_source_url=WSRC_FR+"Clig%C3%A8s",
    primary_source_type="Wikisource (fr): Cligès",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クレチアン・ド・トロワ『獅子の騎士イヴァン』",
    name_en="Chrétien de Troyes's Yvain",
    name_original="Yvain ou le Chevalier au Lion",
    period_key="中世フランス古典期",
    definition="クレチアンが1177-81年頃著した古フランス語ロマン。アーサー王の騎士イヴァンが泉の精ロディーヌと結婚し冒険のため離別、再会の試練を経て和解する物語。「冒険(aventure)と婚姻(mariage)の調停」というクレチアン宮廷ロマンの中心問題を深く展開した代表作。",
    background="12世紀後半シャンパーニュ宮廷における恋愛と冒険の倫理学的構造化。",
    development="ハルトマン・フォン・アウエ『イヴェイン』、中世ロマン文学全体に継承された。",
    historical_context="12世紀後半フランス宮廷文化の倫理的・心理的精緻化局面。",
    primary_source_url=WSRC_FR+"Yvain",
    primary_source_type="Wikisource (fr): Yvain",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="『オーカッサンとニコレット』",
    name_en="Aucassin et Nicolette",
    name_original="Aucassin et Nicolette",
    period_key="中世フランス古典期",
    definition="13世紀前半に成立した古フランス語のシャンテファーブル(歌物語)。散文と韻文(歌)の交替形式で、ボーケール伯子オーカッサンとサラセン娘ニコレットの恋愛を語る。中世フランス文学唯一のシャンテファーブル形式実例で、宮廷ロマンの常套を軽快に転倒したパロディ性が特徴。",
    background="13世紀前半北フランスにおける宮廷ロマンの自己反省化と、ジャンル混合の試み。",
    development="近代フランス文学愛好家の発見(18世紀末)以降、近代散文詩学・小オペラの題材となった。",
    historical_context="13世紀北フランスにおけるジャンル境界の流動化と、口承音楽文化との交差局面。",
    primary_source_url=WSRC_FR+"Aucassin_et_Nicolette",
    primary_source_type="Wikisource (fr): Aucassin et Nicolette",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"散文と韻文を交替する複合形式は、AI生成における異種テキスト混合・モード切替の中世的祖型である。",
         "related_ai_phenomenon":"LLMにおけるモード切替・マルチフォーマット生成"}])

add(**C, name_ja="ジャン・ド・マン『薔薇物語』後半",
    name_en="Jean de Meun's continuation of Roman de la Rose",
    name_original="Le Roman de la Rose (continuation)",
    period_key="中世フランス古典期",
    definition="ジャン・ド・マンが1275-80年頃にギヨーム・ド・ロリス未完作を引き継ぎ、約18,000行を加えた『薔薇物語』後半部。アリストテレス・ボエティウス・アラン・ド・リール哲学を駆使し、宮廷恋愛・自然・摂理・社会批判を百科事典的に扱う。中世俗語百科哲学詩の頂点で、14-15世紀『薔薇物語論争』(クリスティーヌ・ド・ピザン対ジャン・ド・モントルイユ)を引き起こした。",
    background="13世紀後半パリの大学知識人と俗語百科哲学詩の制度化。",
    development="チョーサー、クリスティーヌ・ド・ピザン論争、ルイス『薔薇物語訳』、近世女性論争の祖型。",
    historical_context="13世紀後半パリ大学スコラ哲学と俗語文学が結節する都市知的文化の局面。",
    primary_source_url=WSRC_FR+"Le_Roman_de_la_Rose",
    primary_source_type="Wikisource (fr): Roman de la Rose",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# C: プロヴァンス／トルバドゥール 拡張（8）
# ============================================================
add(**C, name_ja="ベルナール・ド・ヴァンタドゥール",
    name_en="Bernart de Ventadorn",
    name_original="Bernart de Ventadorn",
    period_key="オック語抒情詩期",
    definition="ベルナール・ド・ヴァンタドゥール(c.1135-1194活動)はリムーザン地方出身のトルバドゥールで、宮廷恋愛抒情詩の頂点詩人。約45篇のカンソが遺り、エレオノール・ダキテーヌの宮廷で活動したと推定される。「カン・ヴェイ・ラ・ルゼタ・モヴェル(雲雀を見て)」など内省的・心理的恋愛詩の規範を確立した。",
    background="12世紀後半リムーザン宮廷文化と、宮廷恋愛抒情詩の心理化局面。",
    development="ペトラルキスム抒情詩、20世紀パウンド再評価により近代主義詩学の祖型となった。",
    historical_context="12世紀後半オック語圏宮廷文化の最盛期と心理的抒情詩の制度化。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Bernart/ber_intr.html",
    primary_source_type="Bibliotheca Augustana: Bernart de Ventadorn",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ベルトラン・ド・ボルン",
    name_en="Bertran de Born",
    name_original="Bertran de Born",
    period_key="オック語抒情詩期",
    definition="ベルトラン・ド・ボルン(c.1140-1215頃)はペリゴール地方出身のトルバドゥールで、戦争詩(sirventes)の代表詩人。プランタジネット家王子若王ヘンリーの反乱を煽動した政治的抒情詩で名高く、ダンテ『神曲』地獄篇第28歌で「分裂の罪」のかどで首を切られた姿で登場する。",
    background="12世紀後半プランタジネット家内紛と、政治的抒情詩(sirventes)の制度化。",
    development="ダンテ『神曲』、近代政治抒情詩、エズラ・パウンド再評価の対象となった。",
    historical_context="12世紀後半オクシタニア封建抗争と政治的抒情詩の文化的位置。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Bertran/ber_intr.html",
    primary_source_type="Bibliotheca Augustana: Bertran de Born",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マルカブリュ",
    name_en="Marcabru",
    name_original="Marcabru",
    period_key="オック語抒情詩期",
    definition="マルカブリュ(c.1130-50活動)はガスコーニュ地方出身の初期トルバドゥールで、道徳的・批判的トルバドゥール詩学(trobar clus)の代表詩人。約45篇の詩が遺り、宮廷恋愛の堕落を批判した道徳的抒情詩・パストゥレラ(羊飼い詩)の祖として知られる。",
    background="12世紀前半オック語圏の初期トルバドゥール文化形成期、宮廷恋愛論の最初の批判化。",
    development="トロバル・クルス系列、後期諷刺抒情詩、近世宮廷恋愛批判の系譜の起点。",
    historical_context="12世紀前半オック語抒情詩の制度的形成と道徳的批判詩学の生成。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Marcabru/mar_intr.html",
    primary_source_type="Bibliotheca Augustana: Marcabru",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョフレ・リュデル『遠き愛』",
    name_en="Jaufré Rudel's amor de lonh",
    name_original="amor de lonh",
    period_key="オック語抒情詩期",
    definition="ジョフレ・リュデル(c.1125-48活動)はブライエ大公で、トルバドゥール抒情詩の代表詩人。「遠き愛(amor de lonh)」をめぐる7篇の詩が遺り、見ぬ人への純粋恋愛(amour de loin)を歌った。中世宮廷恋愛理論の核心概念を文学的に結晶化し、19世紀ロマン主義(エドモン・ロスタン『遠い王女』)まで再受容された。",
    background="12世紀前半オック語圏宮廷恋愛論の精神化局面。",
    development="ロスタン『遠い王女』、ブルックナー『遠き愛』20世紀オペラ化までの長い系譜を起こした。",
    historical_context="12世紀前半南仏宮廷文化における精神的恋愛論の制度的確立。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Jaufre/jau_intr.html",
    primary_source_type="Bibliotheca Augustana: Jaufré Rudel",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ライムバウト・ドランジュ",
    name_en="Raimbaut d'Aurenga",
    name_original="Raimbaut d'Aurenga",
    period_key="オック語抒情詩期",
    definition="ライムバウト・ドランジュ(c.1146-73)はオランジュ伯のトルバドゥールで、トロバル・クルス(難解詩学)派の代表詩人。約40篇の詩が遺り、技巧的・難解な韻律と語彙の実験で知られる。アルノー・ダニエルら後期トルバドゥール詩学の祖型。",
    background="12世紀後半オランジュ伯領の宮廷文化と、技巧主義抒情詩の制度化。",
    development="アルノー・ダニエル、ダンテ『俗語論』のトルバドゥール論、20世紀パウンド再評価の系譜。",
    historical_context="12世紀後半オクシタニア宮廷文化の技巧主義局面。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Raimbaut/rai_intr.html",
    primary_source_type="Bibliotheca Augustana: Raimbaut d'Aurenga",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アルノー・ダニエル",
    name_en="Arnaut Daniel",
    name_original="Arnaut Daniel",
    period_key="オック語抒情詩期",
    definition="アルノー・ダニエル(c.1180-1200活動)はペリゴール地方出身のトルバドゥールで、トロバル・リム(精緻詩学)・セスティーナ形式の発明者。約18篇の詩が遺る。ダンテ『神曲』煉獄篇第26歌で「優れた鍛冶屋(miglior fabbro)」と賛えられ、エズラ・パウンドが20世紀近代主義詩学の祖として再評価した。",
    background="12世紀末オクシタニア宮廷文化の技巧主義抒情詩の頂点。",
    development="ダンテ、ペトラルキスム、20世紀パウンド・エリオット近代主義詩学の系譜の核心。",
    historical_context="12世紀末オック語圏宮廷文化と精緻詩学の制度化。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/ArnautDaniel/arn_intr.html",
    primary_source_type="Bibliotheca Augustana: Arnaut Daniel",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ベアトリス・ド・ディア（女性トルバドゥール）",
    name_en="Beatriz de Dia (trobairitz)",
    name_original="Beatriz de Dia",
    period_key="オック語抒情詩期",
    definition="ベアトリス・ド・ディア(c.1140-1212頃)はディア伯領の貴婦人トルバドゥール(トロバリツ)で、女性トルバドゥール最大の名声を持つ詩人。4篇のカンソが遺り、特に「私は歌わなければならない(A chantar m'er)」は曲譜付きで現存する唯一の女性トルバドゥールの楽曲として中世女性詩学研究の中核資料。",
    background="12世紀後半オック語圏宮廷の女性歌人(トロバリツ)文化と女性主体的恋愛詩の制度化。",
    development="20世紀フェミニスト中世研究、ジュディス・ケリー女性詩学論の中心研究対象。",
    historical_context="12世紀後半オクシタニア宮廷の女性主体的文学活動の文化的可能性。",
    primary_source_url=BIBA+"~harsch/gallica/Chronologie/12siecle/Beatriz/bea_intr.html",
    primary_source_type="Bibliotheca Augustana: Beatriz de Dia",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"中世女性詩人の作者性は男性記録に依存して構築された複合作者性であり、AI生成における共著者性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI生成テキストの共著者性・作者帰属の歴史的祖型"}])

add(**C, name_ja="ヴィダス・エ・ラゾス（伝記・解題）",
    name_en="Vidas and Razos",
    name_original="vidas e razos",
    period_key="オック語抒情詩期",
    definition="13世紀北イタリアで編まれたトルバドゥール伝記(vidas)・詩解題(razos)集成。約100篇のトルバドゥールに短い散文伝記と詩の状況解説が付され、伝説と事実を混合する。後世のトルバドゥール伝承の主要源で、近代文芸批評の伝記主義の中世的祖型として再評価された。",
    background="13世紀北イタリアにおけるトルバドゥール文化の伝記的整理と正典化。",
    development="ダンテ『新生』『饗宴』の自己解題形式、近代伝記主義批評の祖型。",
    historical_context="13世紀北イタリアにおけるオック語抒情詩の伝記的制度化と継承。",
    primary_source_url=WSRC_LA+"Vidas",
    primary_source_type="Wikisource (la/fr): vidas e razos",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: イベリア中世（10）
# ============================================================
add(**C, name_ja="『わがシッドの歌』",
    name_en="Cantar de Mio Cid",
    name_original="Cantar de Mio Cid",
    period_key="イベリア中世",
    definition="12世紀末-13世紀初頭にカスティーリャで成立した古スペイン語叙事詩。歴史的人物ロドリゴ・ディアス・デ・ビバル(エル・シッド)の追放・征服・名誉回復を3篇に分けて語る。約3,730行の韻文で、中世カスティーリャ叙事詩(メステル・デ・フグラリア)の唯一の完全保存作で、スペイン国民叙事詩の規範。",
    background="12世紀末カスティーリャ王国のレコンキスタと、口承叙事詩の文字化局面。",
    development="近世スペイン国民詩学、19世紀メネンデス・ピダル叙事詩研究、現代スペイン文学教育の中核。",
    historical_context="12世紀末-13世紀初頭カスティーリャ王権形成期と叙事詩の文学化。",
    primary_source_url=WSRC_ES+"Cantar_de_mio_Cid",
    primary_source_type="Wikisource (es): Cantar de Mio Cid",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ベルセオ『聖母奇蹟譚』",
    name_en="Berceo's Milagros de Nuestra Señora",
    name_original="Milagros de Nuestra Señora",
    period_key="イベリア中世",
    definition="ゴンサロ・デ・ベルセオ(c.1196-1264)が13世紀前半に著したカスティーリャ語による聖母マリア奇蹟譚集25話。メステル・デ・クレレシア(聖職者詩)の代表作で、整然たるクアデルナ・ビア(モノライム四行)韻律で構成される。中世イベリア聖母崇敬文学の頂点で、ロマンス系俗語宗教詩学の制度化を画した。",
    background="13世紀前半カスティーリャの聖母崇敬と、サン・ミラン・デ・ラ・コゴリャ修道院文化。",
    development="アルフォンソ10世『聖母のカンティガス』、近世スペイン宗教詩、19世紀以降の中世文学研究。",
    historical_context="13世紀前半カスティーリャ俗語宗教詩学の制度的確立期。",
    primary_source_url=WSRC_ES+"Milagros_de_Nuestra_Se%C3%B1ora",
    primary_source_type="Wikisource (es): Milagros de Nuestra Señora",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フアン・ルイス『良き愛の書』",
    name_en="Juan Ruiz's Libro de Buen Amor",
    name_original="Libro de Buen Amor",
    period_key="イベリア中世",
    definition="イタ大司祭フアン・ルイス(c.1283-1350)が1330/1343年に著したカスティーリャ語による多形式長編詩。約1,728連、宮廷恋愛論・寓意・パロディ・教訓・諷刺・ピカレスク予兆を混合する中世イベリア最大の俗語文学傑作。中世スペイン文学の最重要原典。",
    background="14世紀前半カスティーリャ俗語文化の多形式的成熟と、中世スペイン語俗語宗教文学の頂点。",
    development="近世スペイン文学、ピカレスク小説、20世紀メネンデス・ピダル以降の中世研究の核心研究対象。",
    historical_context="14世紀前半カスティーリャ王権・教会・俗語文学が結節する文化的局面。",
    primary_source_url=WSRC_ES+"Libro_de_Buen_Amor",
    primary_source_type="Wikisource (es): Libro de Buen Amor",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ドン・フアン・マヌエル『ルカノル伯爵』",
    name_en="Don Juan Manuel's El Conde Lucanor",
    name_original="El Conde Lucanor",
    period_key="イベリア中世",
    definition="ドン・フアン・マヌエル(1282-1348)が1335年に著したカスティーリャ語による教訓説話集。ルカノル伯爵が顧問パトロニオに政治・倫理を諮問し51話の例話で答える形式で構成される。中世イベリア俗語散文の代表作で、アラビア・東方説話の西欧化と、近世スペイン散文の制度的祖型を画した。",
    background="14世紀前半カスティーリャ貴族の俗語散文学術文化と、東方説話の俗語的吸収。",
    development="セルバンテス『ドン・キホーテ』、シェイクスピア『じゃじゃ馬ならし』への伝播、近世スペイン散文の規範。",
    historical_context="14世紀前半カスティーリャ貴族文化の俗語散文化局面。",
    primary_source_url=WSRC_ES+"El_Conde_Lucanor",
    primary_source_type="Wikisource (es): El Conde Lucanor",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ホルヘ・マンリケ『父の死を悼むコプラス』",
    name_en="Jorge Manrique's Coplas a la muerte de su padre",
    name_original="Coplas por la muerte de su padre",
    period_key="イベリア中世",
    definition="ホルヘ・マンリケ(c.1440-79)が1476年頃に著したカスティーリャ語コプラ(短詩)による哀歌。父ロドリゴ・マンリケ将軍を悼み、無常観・死の平等性・名声論を結晶させた40連の長詩。中世末イベリア哀歌詩学の頂点で、近世スペイン詩・19世紀ロマン主義の主要源泉となった。",
    background="15世紀後半カスティーリャ騎士文化と無常観文学の交差局面。",
    development="ロングフェロー英訳、近世スペイン哀歌詩、19世紀ロマン主義詩学の主要参照源。",
    historical_context="15世紀後半カスティーリャ騎士文化の終焉期と中世末文学の結晶化。",
    primary_source_url=WSRC_ES+"Coplas_por_la_muerte_de_su_padre",
    primary_source_type="Wikisource (es): Coplas por la muerte de su padre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フェルナンド・デ・ロハス『セレスティーナ』",
    name_en="Fernando de Rojas's La Celestina",
    name_original="La Celestina (Tragicomedia de Calisto y Melibea)",
    period_key="イベリア中世",
    definition="フェルナンド・デ・ロハス(c.1465-1541)が1499年に著した対話劇形式長編。カリスト・メリベア恋愛悲劇に老婆セレスティーナの仲介を組み込み、中世末イベリアの宮廷恋愛・社会階層・道徳の総合像を提示。中世末から近世への転換を画する西欧文学最重要テクストの一つで、近世スペイン演劇の祖型となった。",
    background="15世紀末カスティーリャ・コンベルソ(改宗ユダヤ人)文化と、中世宮廷恋愛論の世俗化。",
    development="セルバンテス、シェイクスピア、近世スペイン演劇全体の祖型。",
    historical_context="15世紀末カスティーリャ・カトリック両王治世の宗教的緊張と俗語文学の頂点局面。",
    primary_source_url=WSRC_ES+"La_Celestina",
    primary_source_type="Wikisource (es): La Celestina",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"匿名第一幕とロハス改作の複合作者性は、AI共作・人間補完創作モデルの中世的祖型である。",
         "related_ai_phenomenon":"AI共作モデルにおける部分作者性・継承的著作性"}])

add(**C, name_ja="アルフォンソ10世『聖母のカンティガス』",
    name_en="Alfonso X's Cantigas de Santa María",
    name_original="Cantigas de Santa María",
    period_key="イベリア中世",
    definition="カスティーリャ王アルフォンソ10世(賢王、1221-1284)監修のもと13世紀後半に編纂されたガリシア=ポルトガル語による聖母マリア賛歌・奇蹟譚集。420篇のカンティガに楽譜・細密画を併せ持ち、中世イベリア俗語宗教詩・音楽・写本芸術の最大遺産。",
    background="13世紀後半カスティーリャ王権の文化政策とトレドにおける多文化(ラテン・アラビア・ヘブライ・ガリシア=ポルトガル)的知識生産。",
    development="中世音楽史・写本芸術史・ガリシア=ポルトガル語抒情詩研究の最重要原典資料。",
    historical_context="13世紀後半トレド翻訳学派の文化政策とイベリア俗語多元文化の頂点。",
    primary_source_url=WSRC_PT+"Cantigas_de_Santa_Maria",
    primary_source_type="Wikisource (pt): Cantigas de Santa María",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガリシア=ポルトガル語抒情詩",
    name_en="Galician-Portuguese cantigas",
    name_original="cantigas galego-portuguesas",
    period_key="イベリア中世",
    definition="12-14世紀イベリア半島北西部で発展したガリシア=ポルトガル語による抒情詩伝統。カンティガ・ダミーゴ(友のカンティガ、女性発話)・カンティガ・ダモール(愛のカンティガ、男性発話)・カンティガ・デスカルニョ・マルディジル(諷刺カンティガ)の三大ジャンルを形成し、約1,680篇が遺る。中世イベリア俗語抒情詩の独立系統。",
    background="12-14世紀ガリシア=ポルトガル語圏の宮廷文化と、トルバドゥール抒情詩の半島内独立化。",
    development="近世ポルトガル詩、20世紀ペソア再評価、現代イベリア中世研究の中核。",
    historical_context="12-14世紀イベリア半島北西部の宮廷文化と俗語抒情詩の三系統制度化。",
    primary_source_url=WSRC_PT+"Cancioneiro_da_Vaticana",
    primary_source_type="Wikisource (pt): Galician-Portuguese cantigas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="『カンシオネーロ・デ・バエナ』",
    name_en="Cancionero de Baena",
    name_original="Cancionero de Baena",
    period_key="イベリア中世",
    definition="フアン・アルフォンソ・デ・バエナが1430年頃カスティーリャ王フアン2世のために編纂した15世紀前半カスティーリャ抒情詩集。約60詩人・576篇の詩を収録し、中世末イベリア宮廷詩文化の最大コーパス。マンリケ家・サンティリャーナ侯爵ら15世紀前半カスティーリャ詩人サークルの全体像を伝える。",
    background="15世紀前半カスティーリャ宮廷詩人サークルの制度的整理と、中世末イベリア抒情詩の正典化。",
    development="近世スペイン抒情詩、19世紀メネンデス・ペラヨ以降の中世イベリア研究の中核資料。",
    historical_context="15世紀前半カスティーリャ宮廷文化と俗語抒情詩の編集制度化。",
    primary_source_url=WSRC_ES+"Cancionero_de_Baena",
    primary_source_type="Wikisource (es): Cancionero de Baena",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『カンシオネイロ・ダ・ヴァチカナ』",
    name_en="Cancioneiro da Vaticana",
    name_original="Cancioneiro da Vaticana",
    period_key="イベリア中世",
    definition="16世紀初頭イタリアで筆写された中世ガリシア=ポルトガル語抒情詩集成写本(Vat. lat. 4803)。約1,200篇のカンティガを収録し、コロッチ・カンシオネイロと並ぶガリシア=ポルトガル語抒情詩研究の二大原典写本。",
    background="13-14世紀ガリシア=ポルトガル語抒情詩の散逸を逃れた、16世紀初頭イタリア・人文主義者ベンボの周辺における中世写本収集の文化的位置。",
    development="19世紀中世イベリア研究、20世紀ガリシア=ポルトガル語抒情詩研究の中核資料。",
    historical_context="中世イベリア抒情詩のルネサンス期イタリアでの保存・伝承の文化的局面。",
    primary_source_url=WSRC_PT+"Cancioneiro_da_Vaticana",
    primary_source_type="Wikisource (pt): Cancioneiro da Vaticana",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: ドイツ中世 拡張（8）
# ============================================================
add(**C, name_ja="ハインリヒ・フォン・フェルデケ『エネアース・ロマン』",
    name_en="Heinrich von Veldeke's Eneasroman",
    name_original="Eneasroman",
    period_key="中高ドイツ語期",
    definition="ハインリヒ・フォン・フェルデケ(c.1140-90)が1170-90年に著した中高ドイツ語による長編宮廷ロマン。古フランス語『エネアース物語』を中高ドイツ語化し、ヴェルギリウス『アエネイス』の中世化を主導した。中高ドイツ語宮廷ロマンの制度的開始作で、ヴォルフラム・ゴットフリートら次世代詩人の規範を提供した。",
    background="12世紀後半ホーエンシュタウフェン宮廷文化のフランス文化受容と、中高ドイツ語俗語化局面。",
    development="ヴォルフラム・ゴットフリートら中高ドイツ語宮廷ロマンの祖型。",
    historical_context="12世紀後半ライン・低地地方における俗語宮廷文学の制度化。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/12Jh/Veldeke/vel_intr.html",
    primary_source_type="Bibliotheca Augustana: Heinrich von Veldeke",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴォルフラム『ヴィレハルム』",
    name_en="Wolfram's Willehalm",
    name_original="Willehalm",
    period_key="中高ドイツ語期",
    definition="ヴォルフラム・フォン・エッシェンバハ(c.1170-1220)が1210-20年頃著した中高ドイツ語による未完の宗教叙事詩。フランスの『アリスカン戦の歌』を典拠に、聖ギヨームの異教徒との戦争を語る。十字軍時代における異教徒との共感的対話(Gyburg演説)で知られ、宗教戦争詩学の中世的傑作。",
    background="13世紀前半ホーエンシュタウフェン宮廷文化と、十字軍以降の異教徒との共存問題の文学化。",
    development="近世ドイツ叙事詩、20世紀十字軍研究、宗教間対話論の中世的先駆。",
    historical_context="13世紀前半神聖ローマ帝国の十字軍と異教徒問題の文学化局面。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Wolfram/wol_intr.html",
    primary_source_type="Bibliotheca Augustana: Willehalm",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『クードルーン』",
    name_en="Kudrun",
    name_original="Kudrun (Kudrunlied)",
    period_key="中高ドイツ語期",
    definition="13世紀前半に成立した中高ドイツ語による英雄叙事詩。北海・バルト海沿岸を舞台に、ハーゲン王女ヒルデと孫娘クードルーンの三世代にわたる女性英雄物語を語る。『ニーベルンゲンの歌』と並ぶ中高ドイツ語英雄叙事詩で、女性主人公中心の英雄物語として中世ジェンダー研究で重視される。",
    background="13世紀前半ホーエンシュタウフェン宮廷文化と北方英雄伝承の融合局面。",
    development="近世ドイツ英雄詩、20世紀ジェンダー研究、北方英雄物語研究の中核資料。",
    historical_context="13世紀前半神聖ローマ帝国における英雄物語の文学化と女性主体性の文学的可能性。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Kudrun/kud_intr.html",
    primary_source_type="Bibliotheca Augustana: Kudrun",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴェルナー・デア・ガルテネーレ『ヘルムブレヒト』",
    name_en="Wernher der Gartenaere's Helmbrecht",
    name_original="Meier Helmbrecht",
    period_key="中高ドイツ語期",
    definition="ヴェルナー・デア・ガルテネーレが13世紀後半に著した中高ドイツ語による農民叙事詩。豪農の息子ヘルムブレヒトが宮廷騎士に憧れ盗賊化し処刑される物語で、中世社会階層批判と道徳的諷刺を融合する。中世ドイツ語農民文学の代表作で、近世ピカレスク文学の祖型。",
    background="13世紀後半オーストリア・バイエルン辺境地域の社会階層変動と、農民の社会上昇願望の文学化。",
    development="近世ドイツ農民文学、ピカレスク小説の系譜の祖型。",
    historical_context="13世紀後半神聖ローマ帝国辺境地域の社会階層緊張の文学化。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Wernher/wer_intr.html",
    primary_source_type="Bibliotheca Augustana: Helmbrecht",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マイスター・エックハルト説教",
    name_en="Meister Eckhart's German Sermons",
    name_original="Predigten",
    period_key="中高ドイツ語期",
    definition="マイスター・エックハルト(c.1260-1328)がドイツ語で行った約110篇の説教。ドミニコ会神学者でラテン語著作と並行して、中高ドイツ語神秘主義散文の最高水準を確立した。「神性の根底(Grunt)」「離脱(Abgeschiedenheit)」「魂の小さな火花(Fünklein)」等の概念で、中世ドイツ語神秘主義文学の頂点を成す。",
    background="14世紀初頭ドミニコ会神学者と俗語神秘主義女性運動(ベギン)の知的交差局面。",
    development="ハイデガー、トマス・マートン、20世紀東西宗教対話の中核参照源となった。",
    historical_context="14世紀初頭神聖ローマ帝国の俗語神学・教皇庁との緊張(死後異端宣告1329)局面。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/14Jh/Eckhart/eck_intr.html",
    primary_source_type="Bibliotheca Augustana: Meister Eckhart",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"エックハルトの「離脱した主体」「魂の根底」概念は、AI時代の主体性再考(主体なき認識)の中世的祖型である。",
         "related_ai_phenomenon":"AI時代の脱主体的認識・離脱的注意のモデル"}])

add(**C, name_ja="ヒルデガルト・フォン・ビンゲン文学作品",
    name_en="Hildegard von Bingen's literary works",
    name_original="Scivias / Liber Vitae Meritorum / Symphonia",
    period_key="中高ドイツ語期",
    definition="ヒルデガルト・フォン・ビンゲン(1098-1179)が著したラテン語幻視神学・自然学・楽曲集の総体。『道を知れ(Scivias)』『生の報いの書』『神の業の書』、71篇のラテン語典礼詩(Symphonia)、聖歌劇『諸力の演技』を遺し、中世女性著述家最大の体系的著作群を形成した。",
    background="12世紀後半神聖ローマ帝国における女子修道院文化と幻視神学の制度化。",
    development="20世紀フェミニスト中世研究、現代スピリチュアリティ運動の中核参照源。",
    historical_context="12世紀後半ライン地方における女性的霊性の文学化と神学化局面。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/12Jh/Hildegard/hil_intr.html",
    primary_source_type="Bibliotheca Augustana: Hildegard von Bingen",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ヒルデガルトは「神の声を響かせる女性」と自称し、複合的著作主体性をモデル化した。AI時代の代弁的・複合的著作性の祖型。",
         "related_ai_phenomenon":"AI時代の代弁的・媒介的著作性"}])

add(**C, name_ja="メヒティルト・フォン・マクデブルク『神性の流れる光』",
    name_en="Mechthild von Magdeburg's Das fließende Licht der Gottheit",
    name_original="Das fließende Licht der Gottheit",
    period_key="中高ドイツ語期",
    definition="メヒティルト・フォン・マクデブルク(c.1207-1282)が1250-80年に低地ドイツ語で著した7巻の神秘主義散文詩。ベギン共同体での幻視を韻文・散文混合形式で記し、ドイツ語俗語神秘主義女性文学の最高峰。エックハルト・ハインリヒ・ゾイゼら後期中世ドイツ神秘主義者の重要先行者。",
    background="13世紀ドイツのベギン女性運動と、女性的霊性の俗語文学化局面。",
    development="エックハルト、20世紀フェミニスト中世神秘主義研究の中核研究対象。",
    historical_context="13世紀ドイツ俗語神秘主義女性文学の制度的頂点。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Mechthild/mec_intr.html",
    primary_source_type="Bibliotheca Augustana: Mechthild von Magdeburg",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァルター・フォン・デア・フォーゲルヴァイデ『パレスチナ歌』",
    name_en="Walther von der Vogelweide's Palästinalied",
    name_original="Palästinalied",
    period_key="中高ドイツ語期",
    definition="ヴァルター・フォン・デア・フォーゲルヴァイデ(c.1170-1230)が1228年頃著した中高ドイツ語による十字軍詩。フリードリヒ2世の十字軍に随伴し、聖地巡礼を主題とする宗教的・政治的抒情詩で、楽譜付きで現存する貴重な中高ドイツ語抒情詩。中世ドイツ抒情詩の楽曲研究の中核資料。",
    background="13世紀前半フリードリヒ2世第6回十字軍と、ミンネザング詩人の宗教的・政治的役割の局面。",
    development="近世ドイツ宗教抒情詩、20世紀中世音楽研究の中核研究対象。",
    historical_context="13世紀前半神聖ローマ帝国十字軍政策とミンネザング詩人の宮廷的・政治的関与。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Walther/wal_pal.html",
    primary_source_type="Bibliotheca Augustana: Palästinalied",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: 中英語盛期 拡張（7）
# ============================================================
add(**C, name_ja="ガウェイン詩人写本（コットン・ネロA.x）",
    name_en="Gawain Poet manuscript (Cotton Nero A.x)",
    name_original="Cotton Nero A.x manuscript",
    period_key="中英語盛期",
    definition="14世紀後半成立の単一写本コットン・ネロA.x収録の4作品(『真珠』『清浄』『忍耐』『サー・ガウェインと緑の騎士』)。匿名同一作者(ガウェイン詩人/真珠詩人)による中英語頭韻復興の頂点とされ、北西部ミッドランド方言で書かれた中世英語文学の最重要写本の一つ。",
    background="14世紀後半中英語頭韻復興運動と、北西部ミッドランド地方における匿名宮廷詩人の活動局面。",
    development="20世紀トルキン編注以降、中英語文学研究の中核研究対象。",
    historical_context="14世紀後半プランタジネット朝後期の地方宮廷文化と中英語頭韻詩の頂点。",
    primary_source_url=WSRC_EN+"Sir_Gawain_and_the_Green_Knight",
    primary_source_type="Wikisource (en): Cotton Nero A.x",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="『農夫ピアズの夢』A・B・Cテクスト",
    name_en="Piers Plowman A/B/C texts",
    name_original="Piers Plowman (A/B/C versions)",
    period_key="中英語盛期",
    definition="ウィリアム・ラングランド(c.1332-86)が約30年にわたり改訂した『農夫ピアズの夢』のA(c.1370)・B(c.1378)・C(c.1385-86)の三バージョン。同一詩人による生涯にわたる改訂過程は、中英語写本文学・著作改訂研究の最大事例で、社会批判・寓意夢視・神学的探求を融合する。",
    background="14世紀後半英国農民反乱(1381)・ウィクリフ運動の社会的緊張と、写本文化における詩人改訂活動の制度化。",
    development="20世紀写本研究学派(Skeat、Kane-Donaldson)、デジタル人文学の中核研究対象。",
    historical_context="14世紀後半英国社会革命期と中英語社会批判詩学の制度的頂点。",
    primary_source_url=WSRC_EN+"Piers_Plowman",
    primary_source_type="Wikisource (en): Piers Plowman A/B/C",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ラングランドの30年改訂は単一作品の動的著作性を示す中世的事例で、AI時代の継続改訂モデルの祖型。",
         "related_ai_phenomenon":"AI生成における動的・継続的改訂モデル"}])

add(**C, name_ja="『マンドヴィル旅行記』",
    name_en="The Travels of Sir John Mandeville",
    name_original="The Book of Sir John Mandeville",
    period_key="中英語盛期",
    definition="14世紀中葉アングロ・ノルマン語で著された(後に中英語訳)架空旅行記。著者「ジョン・マンドヴィル卿」は虚構と推定され、聖地・インド・東アジア・プレスター・ジョンの王国を巡る世界誌的旅行記として中世末ヨーロッパで広く流布した。コロンブス、ローリーら近世探検家に直接影響した。",
    background="14世紀中葉ヨーロッパの世界地理関心とポロ・モンテコルヴィノ以降の東方知識の文学化局面。",
    development="近世探検記、コロンブス『航海日誌』、近代旅行文学の祖型となった。",
    historical_context="14世紀中葉ヨーロッパの世界拡張期と、虚構旅行記の文化的位置。",
    primary_source_url=GUTEN+"ebooks/782",
    primary_source_type="Project Gutenberg: Travels of Sir John Mandeville",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガワー『恋する男の告白』",
    name_en="Gower's Confessio Amantis",
    name_original="Confessio Amantis",
    period_key="中英語盛期",
    definition="ジョン・ガワー(c.1330-1408)が1386-90年に著した中英語による長編寓意詩。約33,000行で、恋人(Amans)が司祭ジェニウスに七大罪を告白する枠物語の中に約140話の例話を埋め込む。チョーサー『カンタベリー物語』と並ぶ中英語長編詩の二大作で、近世スペンサー寓意詩の祖型となった。",
    background="14世紀末英国宮廷文化と、ラテン・フランス・英語三言語並用の知的環境におけるガワーの英語擁護。",
    development="近世スペンサー、シェイクスピア『ペリクリーズ』源、近代中英語研究の中核資料。",
    historical_context="14世紀末英国宮廷文化と中英語文学の制度的頂点局面。",
    primary_source_url=GUTEN+"ebooks/267",
    primary_source_type="Project Gutenberg: Confessio Amantis",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョン・リドゲイト",
    name_en="John Lydgate",
    name_original="John Lydgate",
    period_key="中英語盛期",
    definition="ジョン・リドゲイト(c.1370-1451)はベリー・セント・エドマンズ修道院の修道士・詩人で、15世紀英国の最多産詩人。『トロイの書(Troy Book)』『君主の没落』『聖母の生涯』等約145,000行の詩を遺し、ヘンリー5世以降のランカスター朝宮廷文化を支えた。中英語末期から近世英語への過渡期の代表詩人。",
    background="15世紀前半ランカスター朝宮廷文化と修道院詩人の制度的位置。",
    development="15-16世紀英国詩学の制度的継承、近代中英語研究の中核研究対象。",
    historical_context="15世紀前半英国百年戦争期の宮廷文学と修道院文学が交差する局面。",
    primary_source_url=GUTEN+"ebooks/14264",
    primary_source_type="Project Gutenberg: Lydgate works",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョン・スケルトン",
    name_en="John Skelton",
    name_original="John Skelton",
    period_key="中英語盛期",
    definition="ジョン・スケルトン(c.1463-1529)はテューダー初期の宮廷詩人・聖職者で、中英語末から近世英語初期への過渡期の代表詩人。「スケルトニク韻律」と呼ばれる短行・連韻韻律を発明し、『ガースの女主人』『豪華な王宮』等で諷刺・宮廷批判詩を確立した。中英語伝統と近世詩学の橋渡し。",
    background="15世紀末-16世紀初頭テューダー朝宮廷文化と、中英語末から近世英語移行期の詩学的緊張。",
    development="近世英国諷刺詩、19世紀以降の韻律史研究の中心研究対象。",
    historical_context="テューダー朝初期英国宮廷文化と中英語末期文学の終焉局面。",
    primary_source_url=GUTEN+"ebooks/40066",
    primary_source_type="Project Gutenberg: Skelton works",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="キャクストン印刷の文学史的衝撃",
    name_en="Caxton's printing impact on literature",
    name_original="William Caxton's printing (1476-)",
    period_key="中英語盛期",
    definition="ウィリアム・キャクストン(c.1422-91)が1476年ウェストミンスターに英国初の印刷所を開設し、約100書を印刷した文化的衝撃。チョーサー『カンタベリー物語』(1478)、マロリー『アーサー王の死』(1485)、ガワー『恋する男の告白』(1483)を印刷化し、中英語文学の正典化と近代英語標準化を主導した。",
    background="15世紀後半英国印刷革命と、中英語写本文化の印刷文化への移行局面。",
    development="近代英語標準化、近世英国正典形成、現代英語史研究の中核研究対象。",
    historical_context="15世紀後半英国印刷革命と中英語文学の正典化局面。",
    primary_source_url=GUTEN+"ebooks/14082",
    primary_source_type="Project Gutenberg: Caxton's prefaces",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"キャクストン印刷による中英語写本の標準化は、AI時代におけるテキスト正規化・コーパス選別の中世末的祖型。",
         "related_ai_phenomenon":"AI時代のテキスト正規化・コーパス選別問題"}])


# ============================================================
# G: 北方＋中世ラテン＋スラヴ（7）
# ============================================================
add(**C, name_ja="王のエッダ写本（コーデックス・レギウス）",
    name_en="Codex Regius (Poetic Edda manuscript)",
    name_original="Codex Regius (GKS 2365 4to)",
    period_key="北方中世",
    definition="13世紀後半アイスランドで筆写された古エッダ唯一の主要写本(GKS 2365 4to)。45葉に29篇の古ノルド語英雄詩・神話詩を収録し、『巫女の予言』『ハーヴァマール』『エッダのシグルズ詩群』を含む。北欧神話・ゲルマン英雄伝承研究の最重要原典写本で、19世紀以降ロマン主義以降のヨーロッパ神話学の中核資料。",
    background="13世紀後半アイスランドにおける古ノルド語文学の写本化と、北欧キリスト教化以降の異教伝承保存局面。",
    development="ワーグナー『指輪』、トルキン、20世紀以降の北欧神話研究の中核資料。",
    historical_context="13世紀アイスランド連邦末期における北欧異教文化の文字化保存局面。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/13Jh/Edda/edd_intr.html",
    primary_source_type="Bibliotheca Augustana: Poetic Edda Codex Regius",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="『ヘーリアント』（古サクソン語救世主物語）",
    name_en="Heliand (Old Saxon Gospel epic)",
    name_original="Heliand",
    period_key="北方中世",
    definition="9世紀前半カロリング朝下のザクセン地方で著された古サクソン語による頭韻詩形式の救世主物語。約5,983行で福音書をゲルマン英雄叙事詩風に翻案し、キリストを「主君(drohtin)」、使徒を「家臣(thegnos)」として描く。古サクソン語文学唯一の長編詩で、中世初期ゲルマン語キリスト教化の文学的記念碑。",
    background="9世紀前半ルートヴィヒ敬虔王治世下、カロリング朝のザクセン宣教政策と異教ゲルマン文化のキリスト教化。",
    development="近代ゲルマン語学・北方頭韻詩研究の中核資料。",
    historical_context="9世紀前半カロリング朝のザクセン宣教局面と、頭韻詩のキリスト教化適応の祖型。",
    primary_source_url=BIBA+"~harsch/germanica/Chronologie/09Jh/Heliand/hel_intr.html",
    primary_source_type="Bibliotheca Augustana: Heliand",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『カルミナ・ブラーナ』",
    name_en="Carmina Burana",
    name_original="Carmina Burana (Codex Buranus)",
    period_key="中世ラテン文学",
    definition="13世紀前半南ドイツ・ベネディクトボイエルン修道院で編纂された世俗ラテン詩・中高ドイツ語詩集成。約254篇の詩を収録し、ゴリアール詩人(さすらい聖職者)による恋愛・酒・ギャンブル・諷刺詩の最大集成。20世紀カール・オルフのカンタータ化で世界的に有名化した。",
    background="13世紀前半南ドイツ修道院・大学文化におけるラテン語俗世詩人(ゴリアール)の制度的位置。",
    development="近代ラテン中世文学研究、20世紀オルフ音楽化、現代中世音楽研究の中核資料。",
    historical_context="13世紀前半南ドイツ・修道院・大学文化におけるラテン語世俗詩学の頂点局面。",
    primary_source_url=BIBA+"~harsch/Chronologie/13Jh/CarminaBurana/bur_intr.html",
    primary_source_type="Bibliotheca Augustana: Carmina Burana",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヴァルター・フォン・シャティヨン『アレクサンドレイス』",
    name_en="Walter of Châtillon's Alexandreis",
    name_original="Alexandreis",
    period_key="中世ラテン文学",
    definition="ヴァルター・フォン・シャティヨン(c.1135-1190頃)が1170-82年に著したラテン語10巻叙事詩。クルティウス・ルフス『アレクサンドロス史』に基づきアレクサンドロス大王の遠征を描き、中世ラテン古典模倣叙事詩の頂点として中世大学カリキュラムでウェルギリウス『アエネイス』に並ぶ規範となった。",
    background="12世紀後半ランス大学のラテン古典模倣詩学と、中世ルネサンス期の古典叙事詩制度化局面。",
    development="13-15世紀大学ラテン教育の規範、近代ラテン中世詩学研究の中核研究対象。",
    historical_context="12世紀後半フランス大学文化と中世ラテン古典模倣の制度的頂点局面。",
    primary_source_url=LATLIB+"alexandreis.html",
    primary_source_type="Latin Library: Alexandreis",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジェフリー・オブ・ヴィンソーフ『新しい詩学』",
    name_en="Geoffrey of Vinsauf's Poetria Nova",
    name_original="Poetria Nova",
    period_key="中世ラテン文学",
    definition="ジェフリー・オブ・ヴィンソーフ(c.1200活動)が1208-13年に著したラテン語六歩格による詩作論2,121行。教皇インノケンティウス3世に献呈され、ホラティウス『詩論』を踏まえて中世ラテン詩学の修辞技術を体系化した。中世大学詩学カリキュラムの規範書で、チョーサー『修道女の付随者の話』で言及される。",
    background="12-13世紀大学修辞学・詩学教育の制度化と、ラテン詩作技術の体系化局面。",
    development="13-15世紀大学詩学カリキュラムの規範、チョーサーら俗語詩人への影響、近代修辞学史研究の中核資料。",
    historical_context="13世紀初頭大学詩学教育の制度的頂点局面。",
    primary_source_url=LATLIB+"vinsauf.html",
    primary_source_type="Latin Library: Poetria Nova",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"中世詩学の修辞技術体系は、AI時代のプロンプト工学・テキスト生成術の中世的祖型と理論的に並行する。",
         "related_ai_phenomenon":"プロンプトエンジニアリング・修辞的生成技術の中世的祖型"}])

add(**C, name_ja="アベラール=エロイーズ書簡",
    name_en="Abelard-Heloise letters",
    name_original="Epistolae Heloissae et Abelardi",
    period_key="中世ラテン文学",
    definition="ピエール・アベラール(1079-1142)とエロイーズ(c.1095-1164)の往復書簡集。1130-35年頃編集され、悲恋・哲学・修道生活を主題とする8通のラテン語書簡。中世ラテン書簡文学の頂点で、女性主体的書簡の最重要原典として近代以降の伝記主義・フェミニスト中世研究の中核研究対象となった。",
    background="12世紀前半パリ大学スコラ哲学と、悲恋・修道生活が結節する文化的局面。",
    development="ルソー『新エロイーズ』、20世紀フェミニスト中世研究、書簡体小説の祖型。",
    historical_context="12世紀前半パリ知識人文化と、女性的書簡主体性の文学的可能性の頂点。",
    primary_source_url=LATLIB+"abelard.html",
    primary_source_type="Latin Library: Abelard-Heloise",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"エロイーズの書簡的主体性と男性編集者の介入問題は、AI時代の主体性編集・代弁的著作の中世的祖型。",
         "related_ai_phenomenon":"AI時代の主体性編集・代弁的著作問題"}])

add(**CCYR, name_ja="『イーゴリ軍記』",
    name_en="The Tale of Igor's Campaign",
    name_original="Слово о полку Игореве",
    period_key="中世スラヴ",
    definition="12世紀末古東スラヴ語(古ロシア語)で著された散文・韻文混合の叙事詩。1185年ノヴゴロド・セヴェルスキー公イーゴリの対ポロヴェツ遠征の失敗を主題とし、中世スラヴ文学の最高峰とされる。1795年発見・1800年刊行で、19世紀ロシア国民文学の核心となった。ボロディン歌劇『イーゴリ公』、ナボコフ英訳で世界化。",
    background="12世紀末キエフ・ルーシ封建的分裂期の対ポロヴェツ戦争と、宮廷叙事詩の文学化。",
    development="19世紀ロシア国民文学、ボロディン、20世紀ロマン・ヤコブソン以降の言語学的研究の核心。",
    historical_context="12世紀末キエフ・ルーシ末期の文化的成熟局面。",
    primary_source_url=WSRC_RU+"%D0%A1%D0%BB%D0%BE%D0%B2%D0%BE_%D0%BE_%D0%BF%D0%BE%D0%BB%D0%BA%D1%83_%D0%98%D0%B3%D0%BE%D1%80%D0%B5%D0%B2%D0%B5",
    primary_source_type="Wikisource (ru): Slovo o polku Igoreve",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# Cross-domain attachments
# ============================================================
def _attach_cross(concept_name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c.get("name_ja") == concept_name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("ダンテ『饗宴（コンヴィヴィオ）』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"俗語による哲学",
     "description":"ダンテ『饗宴』は俗語哲学の中世的先駆で、近代哲学言語論争の祖型。"}])

_attach_cross("ダンテ『帝政論（モナルキア）』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"中世政治神学",
     "description":"『モナルキア』は中世皇帝主義政治神学の代表テクストで、教皇権至上主義との対立軸。"}])

_attach_cross("グイド・カヴァルカンティ『ドンナ・ミ・プレガ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アヴェロエス能動知性論",
     "description":"カヴァルカンティ愛詩はアヴェロエス能動知性論の俗語詩学化で、中世イスラーム哲学の西洋詩学への影響経路。"}])

_attach_cross("ボッカッチョ『フィロストラート』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"オッターヴァ・リーマ詩学",
     "description":"ボッカッチョのオッターヴァ・リーマはルネサンス・近世イタリア叙事詩の規範形式となった。"}])

_attach_cross("『ロマン・ド・ルナール』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"動物寓意の人類学",
     "description":"獣譚は人類学・民俗学の動物象徴研究の中世的中核資料。"}])

_attach_cross("ロベール・ド・ボロン『アリマタヤのヨセフ』", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"聖杯神話の正典化",
     "description":"ロベール・ド・ボロンは聖杯神話のキリスト教化・正典化を主導し、近代ファンタジー神話の中核資料。"}])

_attach_cross("クレチアン・ド・トロワ『獅子の騎士イヴァン』", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"アーサー王円卓神話",
     "description":"クレチアン宮廷ロマンはアーサー王円卓神話の文学的整備の中核。"}])

_attach_cross("ジャン・ド・マン『薔薇物語』後半", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"中世俗語百科哲学",
     "description":"ジャン・ド・マン版はスコラ哲学の俗語百科化で、中世俗語知識学の頂点。"}])

_attach_cross("ベルナール・ド・ヴァンタドゥール", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"宮廷恋愛抒情詩理論",
     "description":"ベルナールは宮廷恋愛抒情詩の心理化規範を確立し、ペトラルキスムの祖型となった。"}])

_attach_cross("アルノー・ダニエル", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"セスティーナ形式",
     "description":"アルノー発明のセスティーナ形式は近代主義詩学(パウンド・エリオット)の中核研究対象。"}])

_attach_cross("ベアトリス・ド・ディア（女性トルバドゥール）", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"中世女性的主体性",
     "description":"トロバリツの女性的主体性は中世ジェンダー人類学の中核研究対象。"}])

_attach_cross("『わがシッドの歌』", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"レコンキスタ国民叙事詩",
     "description":"『シッド』はレコンキスタ国民叙事詩の代表で、スペイン国民神話の中核。"}])

_attach_cross("フアン・ルイス『良き愛の書』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"中世イベリア多文化民族誌",
     "description":"『良き愛の書』はキリスト・ユダヤ・イスラーム文化が交錯するイベリア多文化民族誌の文学化。"}])

_attach_cross("ドン・フアン・マヌエル『ルカノル伯爵』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"中世統治論",
     "description":"『ルカノル』は貴族向け統治助言文学の中世イベリア代表で、近世マキャヴェリ系統治論の祖型。"}])

_attach_cross("フェルナンド・デ・ロハス『セレスティーナ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"中世末コンベルソ文化",
     "description":"『セレスティーナ』はコンベルソ(改宗ユダヤ人)知識人の世俗化文学で、中世末文化人類学の中核資料。"}])

_attach_cross("アルフォンソ10世『聖母のカンティガス』", [
    {"target_db":"Cultural-Intelligence","link_type":"shared_concept",
     "target_entity_name":"中世イベリア多文化文芸",
     "description":"アルフォンソ10世時代のトレドはラテン・アラビア・ヘブライ・俗語が交錯する多文化的文芸生産局面。"}])

_attach_cross("マイスター・エックハルト説教", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"中世ドイツ神秘主義神学",
     "description":"エックハルト神秘主義は中世ドイツ神秘主義神学の頂点で、ハイデガー以降の近現代哲学の中核参照。"}])

_attach_cross("ヒルデガルト・フォン・ビンゲン文学作品", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"中世女性的霊性",
     "description":"ヒルデガルトは中世女性的霊性文化の総合的代表者で、ジェンダー文化人類学の中核研究対象。"}])

_attach_cross("メヒティルト・フォン・マクデブルク『神性の流れる光』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ベギン女性運動",
     "description":"メヒティルトはドイツ・ベギン女性運動の文学的代表で、中世女性社会史の中核資料。"}])

_attach_cross("ガウェイン詩人写本（コットン・ネロA.x）", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"中英語頭韻復興詩学",
     "description":"ガウェイン詩人は中英語頭韻復興運動の頂点で、英語詩学史の中核研究対象。"}])

_attach_cross("『農夫ピアズの夢』A・B・Cテクスト", [
    {"target_db":"SI","link_type":"shared_concept",
     "target_entity_name":"中世社会批判文学",
     "description":"『ピアズ』は1381年農民反乱期の中世社会批判文学の代表で、社会変革文学の中世的祖型。"}])

_attach_cross("キャクストン印刷の文学史的衝撃", [
    {"target_db":"Innovation","link_type":"shared_concept",
     "target_entity_name":"印刷革命と知識制度",
     "description":"キャクストン印刷は英語圏知識制度のメディア革命で、近代知識インフラの祖型。"}])

_attach_cross("王のエッダ写本（コーデックス・レギウス）", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"北欧神話正典",
     "description":"コーデックス・レギウスは北欧神話の唯一の主要原典で、ヨーロッパ神話学の中核資料。"}])

_attach_cross("『カルミナ・ブラーナ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"ゴリアール世俗ラテン詩",
     "description":"『カルミナ・ブラーナ』は中世ラテン世俗詩の最大集成で、ヨーロッパ世俗詩学の中世的核心。"}])

_attach_cross("アベラール=エロイーズ書簡", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アベラール論理学・倫理学",
     "description":"アベラールは12世紀パリ・スコラ哲学の中核で、エロイーズ書簡は哲学者の生の文学化。"}])

_attach_cross("『イーゴリ軍記』", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"スラヴ国民叙事詩",
     "description":"『イーゴリ軍記』はキエフ・ルーシ末期の唯一の叙事詩遺産で、ロシア国民神話の中核。"}])


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
        print(f"[c03-w14] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c03-w14] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c03-w14] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
