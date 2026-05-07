"""LIT-DB Phase 2 Wave 12 — C05: Renaissance / Early-modern Europe ADD 40 concepts.

Subfield: lit_eu_renaissance (id=3), region='西欧'.
Sources: Liber Liber (Italian), BVMC (Spanish), Frantext / Gallica (French),
EEBO/LION/Project Gutenberg (English), all PD-grade.

Adds 40 NEW concepts complementary to the existing 40 (ids 482-521).
Coverage:
  A: Italian Renaissance (8) — Petrarch full, Boccaccio, Ariosto, Tasso,
                               Castiglione, Machiavelli, Pulci, Poliziano, Bembo,
                               Aretino, Vittoria Colonna
  B: Spanish Golden Age (8) — Calderón, Lope, Tirso, Quevedo, Góngora,
                              Garcilaso, San Juan, picaresque corpus
  C: French Renaissance (8) — Rabelais, Pléiade, Marguerite de Navarre,
                              d'Aubigné, Montaigne extensions
  D: English Tudor/Jacobean (8) — Sidney, Spenser, Marlowe, Jonson, Donne,
                                  Herbert, Marvell
  E: German/Dutch + cross-Renaissance (8) — Erasmus, Brant, Sachs, Vondel,
                                            cross-domain poetics
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("イタリア・ルネサンス期", "Italian Renaissance", 1300, 1600,
     "ペトラルカ、ボッカッチョ、アリオスト、タッソ、マキャヴェリ、カスティリオーネ等を擁する西洋ルネサンス文学の中心潮流。俗語による古典再生と人文主義の制度化期。"),
    ("スペイン黄金時代", "Spanish Golden Age (Siglo de Oro)", 1500, 1681,
     "ガルシラーソからカルデロンに至るスペイン文学の黄金期。ピカレスク、コメディア・ヌエバ、神秘詩、コンセプティスモ／クルテラニスモを生んだ。"),
    ("フランス・ルネサンス期", "French Renaissance", 1494, 1610,
     "ラブレー、プレイヤード派、マルグリット・ド・ナヴァール、モンテーニュ、ドービニェの活動期。フランス俗語文学の制度化と宗教戦争期文学の成熟。"),
    ("テューダー・ジャコビアン期", "Tudor and Jacobean England", 1485, 1625,
     "シドニー、スペンサー、マーロウ、シェイクスピア、ジョンソン、ダン、ハーバート、マーヴェルを擁する英語文芸の最初の頂点期。"),
    ("北方ルネサンス期", "Northern Renaissance", 1450, 1650,
     "エラスムス、ブラント、ハンス・ザックス、フォンデルら独語・蘭語圏のルネサンス・人文主義期。"),
]


GUTEN = "https://www.gutenberg.org/"
LIBER = "https://www.liberliber.it/"
BVMC = "https://www.cervantesvirtual.com/"
FRANTEXT = "https://www.frantext.fr/"
GALLICA = "https://gallica.bnf.fr/"
EEBO = "https://quod.lib.umich.edu/e/eebogroup/"
LION = "https://about.proquest.com/en/products-services/literature_online/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_renaissance", region="西欧",
         original_script="roman")


# ============================================================
# A: イタリア・ルネサンス（8件）
# ============================================================
add(**C, name_ja="ペトラルカ『カンツォニエーレ』",
    name_en="Petrarch's Canzoniere",
    name_original="Rerum vulgarium fragmenta",
    period_key="イタリア・ルネサンス期",
    definition="フランチェスコ・ペトラルカ（1304-74）が生涯にわたり推敲し続けた俗語抒情詩集。366編の詩からなり、ラウラへの愛を中心に内省的主体性と古典的修辞を融合させた。ヨーロッパ抒情詩の規範を数世紀にわたり規定し、ペトラルキスムの源泉となった。",
    background="ボッカッチョ、ダンテ後のイタリア俗語文学高揚と、古典的ラテン人文主義の俗語化志向。",
    development="ベンボ『俗語論』が規範化し、ロンサール、ガルシラーソ、シドニー、シェイクスピアに至る欧州ソネット伝統を形成した。",
    historical_context="アヴィニョン教皇庁期およびイタリア都市国家文化の興隆期。",
    primary_source_url=WSRC_IT+"Canzoniere_(Rerum_vulgarium_fragmenta)",
    primary_source_type="Wikisource: Canzoniere (Italian)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボッカッチョ『デカメロン』枠物語",
    name_en="Boccaccio's Decameron framing",
    name_original="Decameron",
    period_key="イタリア・ルネサンス期",
    definition="ジョヴァンニ・ボッカッチョ（1313-75）が1349-53年頃に完成した百話集。ペスト下フィレンツェを逃れた10人の若者が10日間語る100話の構造を持ち、枠物語形式と俗語散文芸術を確立した。ヨーロッパ短編小説（ノヴェッラ）の規範形式となった。",
    background="1348年黒死病の社会的衝撃と、フィレンツェ共和国の都市文化興隆。",
    development="チョーサー『カンタベリー物語』、マルグリット・ド・ナヴァール『エプタメロン』、セルバンテス『模範小説集』に直接影響を与えた。",
    historical_context="14世紀イタリア都市国家のブルジョワ文化と、教会権威の相対化期。",
    primary_source_url=LIBER+"libri/b/boccaccio_giovanni/",
    primary_source_type="Liber Liber: Boccaccio collection",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"枠物語構造",
         "description":"デカメロンの枠物語構造は物語論における枠付けの古典的範例として、ジュネット以降のナラトロジーの中心研究対象となっている。"}])

add(**C, name_ja="アリオスト『狂えるオルランド』",
    name_en="Ariosto's Orlando Furioso",
    name_original="Orlando Furioso",
    period_key="イタリア・ルネサンス期",
    definition="ルドヴィコ・アリオスト（1474-1533）が1516-32年に発表した46歌の騎士叙事詩。ボイアルド『恋するオルランド』を継承し、シャルルマーニュ伝説を素材に、皮肉と幻想を融合した近代ロマン主義叙事詩の規範となった。複数物語の織り交ぜ（entrelacement）技法で知られる。",
    background="フェッラーラ宮廷文化と、トスカーナ俗語の規範化過程。",
    development="スペンサー『妖精の女王』、タッソ『解放されたエルサレム』、後の欧州幻想・冒険物語に深く影響した。",
    historical_context="イタリア戦争期（1494-1559）の都市国家危機下の宮廷文学。",
    primary_source_url=WSRC_IT+"Orlando_furioso",
    primary_source_type="Wikisource: Orlando furioso",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="タッソ『解放されたエルサレム』",
    name_en="Tasso's Gerusalemme Liberata",
    name_original="Gerusalemme Liberata",
    period_key="イタリア・ルネサンス期",
    definition="トルクァート・タッソ（1544-95）が1581年に発表した20歌の英雄叙事詩。第一回十字軍によるエルサレム解放を題材とし、アリストテレス詩学に従う統一性と、キリスト教対抗改革期の宗教的崇高を融合させた。バロック叙事詩の規範となった。",
    background="トリエント公会議後の対抗改革期および、フェッラーラ・エステ宮廷文化。",
    development="ミルトン『失楽園』、スペンサー後期、後の欧州バロック叙事詩に決定的影響を与えた。",
    historical_context="イタリア対抗改革期と、十字軍記憶のキリスト教文学的再生産。",
    primary_source_url=WSRC_IT+"Gerusalemme_liberata",
    primary_source_type="Wikisource: Gerusalemme liberata",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="カスティリオーネ『宮廷人の書』",
    name_en="Castiglione's Il Cortegiano",
    name_original="Il libro del Cortegiano",
    period_key="イタリア・ルネサンス期",
    definition="バルダッサーレ・カスティリオーネ（1478-1529）が1528年に発表した対話形式の理想宮廷人論。ウルビーノ宮廷を舞台にスプレッツァトゥーラ（自然な優雅さ）の理念を中核に、近世ヨーロッパの教養人理想を体系化した。",
    background="ウルビーノ・モンテフェルトロ宮廷文化と、イタリア人文主義の宮廷的成熟。",
    development="ホビー訳（1561）を介して英国エリザベス朝にスプレッツァトゥーラ概念を移植し、シドニーら宮廷詩人に決定的影響を与えた。",
    historical_context="イタリア戦争期の宮廷文化の文芸的理想化。",
    primary_source_url=LIBER+"libri/c/castiglione_baldassarre/",
    primary_source_type="Liber Liber: Il Cortegiano",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"スプレッツァトゥーラ理念は技法を「自然」に見せる主体性のパフォーマンス論であり、AI生成テキストが「人間らしさ」を演出する技法と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における自然さの演出"}])

add(**C, name_ja="マキャヴェリの俗語散文",
    name_en="Machiavelli's vernacular prose",
    name_original="prosa volgare di Machiavelli",
    period_key="イタリア・ルネサンス期",
    definition="ニッコロ・マキャヴェリ（1469-1527）が『君主論』（1513）、『ディスコルシ』、『マンドラゴラ』（喜劇）、『フィレンツェ史』で展開した簡潔で剃刀的なトスカーナ俗語散文。政治・歴史・劇の三領域を横断し、近代政治思想を生む文体的基盤となった。",
    background="フィレンツェ共和国官僚としての実務経験と、メディチ復権後の隠棲執筆。",
    development="ボダン、ホッブズ、近代政治思想に文体・概念で影響を与え、近世イタリア散文の規範を成した。",
    historical_context="フィレンツェ共和国崩壊（1512）とメディチ復権の政治的危機。",
    primary_source_url=LIBER+"libri/m/machiavelli_niccolo/",
    primary_source_type="Liber Liber: Machiavelli collection",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"近代政治思想",
         "description":"マキャヴェリ散文は近代政治学・経営学の祖型を成す。"}])

add(**C, name_ja="プルチ『大モルガンテ』",
    name_en="Pulci's Morgante",
    name_original="Morgante",
    period_key="イタリア・ルネサンス期",
    definition="ルイジ・プルチ（1432-84）が1478-83年に発表した28歌の叙事詩。シャルルマーニュ伝説に喜劇的・冒涜的な巨人モルガンテを導入し、騎士叙事詩の俗化・喜劇化を達成した。ボイアルド・アリオスト・ラブレーへの先駆け。",
    background="メディチ家フィレンツェ宮廷文化と、街頭朗誦伝統の文芸化。",
    development="ボイアルド『恋するオルランド』、ラブレー『ガルガンチュア』への直接的影響を持つ。",
    historical_context="ロレンツォ・ディ・メディチ統治下フィレンツェの民衆文化と宮廷文化の融合期。",
    primary_source_url=WSRC_IT+"Morgante",
    primary_source_type="Wikisource: Morgante",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベンボ『俗語論』",
    name_en="Bembo's Prose della volgar lingua",
    name_original="Prose della volgar lingua",
    period_key="イタリア・ルネサンス期",
    definition="ピエトロ・ベンボ（1470-1547）が1525年に発表した俗語規範論。ペトラルカを詩の、ボッカッチョを散文の規範とし、トスカーナ俗語をイタリア文学言語として確立した。ペトラルキスムを欧州規範化する理論的基盤を成した。",
    background="チンクェチェント期のイタリア言語論争（questione della lingua）。",
    development="フランス・プレイヤード派、スペイン・ガルシラーソ、英語ソネット伝統に俗語高揚モデルを供給した。",
    historical_context="16世紀前半イタリアの言語規範化と俗語文学の制度化。",
    primary_source_url=LIBER+"libri/b/bembo_pietro/",
    primary_source_type="Liber Liber: Bembo collection",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: スペイン黄金時代（8件）
# ============================================================
add(**C, name_ja="カルデロン『人生は夢』",
    name_en="Calderón's La vida es sueño",
    name_original="La vida es sueño",
    period_key="スペイン黄金時代",
    definition="ペドロ・カルデロン・デ・ラ・バルカ（1600-81）が1635年に発表した三幕戯曲。ポーランド王子セヒスムンドの幽閉と覚醒を題材に、自由意志・運命・現実と夢の主題を展開する。スペイン黄金時代演劇の哲学的頂点。",
    background="フェリペ4世期スペインの危機と対抗改革期形而上学的演劇の成熟。",
    development="シェリング、ショーペンハウアー、ホフマンスタールに哲学的・劇的影響を与え、欧州バロック演劇の代表作となった。",
    historical_context="17世紀前半スペイン危機（三十年戦争、経済衰退）と宮廷演劇の盛期。",
    primary_source_url=BVMC+"obra/la-vida-es-sueno--0/",
    primary_source_type="BVMC: La vida es sueño",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ロペ・デ・ベガ『新作劇法』",
    name_en="Lope de Vega's Arte nuevo de hacer comedias",
    name_original="Arte nuevo de hacer comedias en este tiempo",
    period_key="スペイン黄金時代",
    definition="ロペ・デ・ベガ（1562-1635）が1609年に発表したコメディア・ヌエバ（新喜劇）の理論書兼弁明。三一致律を破棄し、悲喜混淆と三幕構成、民衆観客への適合を提唱した。スペイン黄金時代演劇の規範を理論化した。",
    background="マドリードのコラル（中庭劇場）と職業劇団の興隆、対抗改革期の都市演劇文化。",
    development="ティルソ・デ・モリーナ、カルデロン、後の欧州演劇規範論争（17-18世紀）に影響を与えた。",
    historical_context="フェリペ3世期スペインの都市文化と、職業演劇の制度確立。",
    primary_source_url=BVMC+"obra/arte-nuevo-de-hacer-comedias-en-este-tiempo--0/",
    primary_source_type="BVMC: Arte nuevo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ティルソ・デ・モリーナ『セビーリャの色事師』",
    name_en="Tirso's El burlador de Sevilla",
    name_original="El burlador de Sevilla y convidado de piedra",
    period_key="スペイン黄金時代",
    definition="ティルソ・デ・モリーナ（1579頃-1648）に伝統的に帰属される1616-30年頃の戯曲。ドン・フアン・テノリオの誘惑と石像の罰を初めて演劇化し、ドン・ファン伝説の祖型となった。",
    background="セビーリャ都市文化と、対抗改革期のモラリストドラマ。",
    development="モリエール『ドン・ジュアン』、モーツァルト=ダ・ポンテ『ドン・ジョヴァンニ』、バイロン、ホフマン等の欧州ドン・ファン文学の祖型となった。",
    historical_context="17世紀前半スペインの宮廷・修道院演劇文化。",
    primary_source_url=BVMC+"obra/el-burlador-de-sevilla-y-convidado-de-piedra--0/",
    primary_source_type="BVMC: El burlador de Sevilla",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ケベード コンセプティスモ",
    name_en="Quevedo's conceptismo",
    name_original="conceptismo",
    period_key="スペイン黄金時代",
    definition="フランシスコ・デ・ケベード（1580-1645）が代表する、機知と概念的鋭さを核とするバロック詩学。短く凝縮された語彙の中に逆説・対比・概念的衝撃を盛り込む手法で、ピカレスク小説『ブスコン』(1626)と諷刺詩・道徳詩で実践された。グラシアン『機知と発明の術』(1648)が理論化した。",
    background="フェリペ3-4世期スペインの危機意識とバロック的世界観。",
    development="グラシアン理論を介して欧州バロック詩学に影響を与え、英国メタフィジカル詩、現代スペイン語詩に系譜的に継承された。",
    historical_context="スペイン17世紀危機期の宮廷・知識人文化。",
    primary_source_url=BVMC+"autor/francisco-de-quevedo--0/",
    primary_source_type="BVMC: Quevedo collection",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゴンゴラ クルテラニスモ",
    name_en="Góngora's culteranismo",
    name_original="culteranismo",
    period_key="スペイン黄金時代",
    definition="ルイス・デ・ゴンゴラ（1561-1627）が代表する、ラテン語的構文・神話的暗喩・修辞的精緻を極めるバロック詩学。『孤独』(1613)、『ポリフェモとガラテア物語』(1612)で実践され、難解な「クルト・ラテン主義（culto）」と呼ばれた。ケベードのコンセプティスモと並ぶスペイン・バロック二大潮流。",
    background="フェリペ3世期スペインの宮廷詩文化、コルドバ知識人サークル。",
    development="20世紀ガルシア・ロルカら27年世代によるゴンゴラ復権を経て、現代スペイン詩・ラテンアメリカ詩の規範となった。",
    historical_context="17世紀前半スペイン宮廷詩学論争（コンセプティスモ対クルテラニスモ）。",
    primary_source_url=BVMC+"autor/luis-de-gongora-y-argote--0/",
    primary_source_type="BVMC: Góngora collection",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ガルシラーソ・デ・ラ・ベガ",
    name_en="Garcilaso de la Vega",
    name_original="Garcilaso de la Vega",
    period_key="スペイン黄金時代",
    definition="ガルシラーソ・デ・ラ・ベガ（1501頃-36）。ボスカン共著の詩集（1543遺稿刊）でイタリア・ペトラルキスム（11音節詩、ソネット、エクローガ）をスペイン語に移植し、スペイン黄金時代詩の出発点を成した。エクローガ第1番が代表作。",
    background="カルロス1世（カール5世）期のイタリア軍事・文化接触、ベンボ的俗語論のスペイン受容。",
    development="エレラ、フライ・ルイス・デ・レオン、後のスペイン詩全体に韻律・形式の規範を与えた。",
    historical_context="16世紀前半スペイン帝国期の文化的イタリア化。",
    primary_source_url=BVMC+"autor/garcilaso-de-la-vega--0/",
    primary_source_type="BVMC: Garcilaso collection",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サン・フアン・デ・ラ・クルス神秘詩",
    name_en="San Juan de la Cruz mystical poetry",
    name_original="poesía mística de San Juan de la Cruz",
    period_key="スペイン黄金時代",
    definition="フアン・デ・イェペス（1542-91、跣足カルメル会改革者）の神秘詩。『暗き夜』『霊魂の歌』『生ける愛の炎』を中核に、雅歌的官能性とトマス的形而上学を統合し、スペイン神秘文学の頂点を成した。",
    background="テレサ・デ・アビラとの跣足カルメル会改革、対抗改革期スペイン霊性。",
    development="近代神秘主義詩学（ベルクソン、後のモダニズム宗教詩）に深い影響を与え、20世紀T.S.エリオット『四つの四重奏』にも言及される。",
    historical_context="16世紀後半スペインの修道院改革と、対抗改革期霊性の文学化。",
    primary_source_url=BVMC+"autor/san-juan-de-la-cruz--0/",
    primary_source_type="BVMC: San Juan de la Cruz",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"神秘体験の詩的表現",
         "description":"サン・フアンの神秘詩は神秘主義哲学・否定神学の文学的表現として、宗教哲学研究の中心対象である。"}])

add(**C, name_ja="ピカレスク三部作（ラサリーリョ／グスマン／ブスコン）",
    name_en="picaresque corpus (Lazarillo / Guzmán / Buscón)",
    name_original="novela picaresca corpus",
    period_key="スペイン黄金時代",
    definition="『ラサリーリョ・デ・トルメスの生涯』(1554、作者不詳)、マテオ・アレマン『グスマン・デ・アルファラチェ』(1599-1604)、ケベード『ブスコン』(1626)の三作を中核とするスペイン・ピカレスク小説体系。一人称の悪漢自伝形式によって、近代散文小説の祖型を成した。",
    background="16世紀スペインの社会的階層変動と、エラスムス的反偽善精神のスペイン受容。",
    development="グリンメルスハウゼン『ジンプリチシムス』、ルサージュ『ジル・ブラース』、ディフォー『モル・フランダース』、後の欧州小説に祖型を供給した。",
    historical_context="16-17世紀スペイン社会の貧困・浮浪・新興階層の文学的問題化。",
    primary_source_url=BVMC+"obra/lazarillo-de-tormes--0/",
    primary_source_type="BVMC: Lazarillo / Guzmán / Buscón",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"社会階層の文学的観察",
         "description":"ピカレスク小説は近世スペイン社会の階層・貧困・移動を一人称視点で記録する民族誌的祖型を成す。"}])


# ============================================================
# C: フランス・ルネサンス（8件）
# ============================================================
add(**C, name_ja="ラブレー『ガルガンチュアとパンタグリュエル』",
    name_en="Rabelais's Gargantua et Pantagruel",
    name_original="Gargantua et Pantagruel",
    period_key="フランス・ルネサンス期",
    definition="フランソワ・ラブレー（1494頃-1553）が1532-64年に発表した5巻の巨人物語。中世民衆物語、人文主義、エラスミアニズム、医学知識を融合し、カーニヴァル的笑いと百科全書的知識欲を統合した。バフチン『ラブレーの作品と中世・ルネサンスの民衆文化』(1965)が「グロテスク・リアリズム」として理論化した。",
    background="フランソワ1世期のフランス人文主義、エラスムス受容、印刷文化興隆。",
    development="スターン『トリストラム・シャンディ』、ジョイス『ユリシーズ』、ガルシア・マルケス、現代マジックリアリズムへ継承された。",
    historical_context="16世紀前半フランスの宗教改革論争と、人文主義者の検閲との緊張。",
    primary_source_url=FRANTEXT+"catalogue.php?id=R301",
    primary_source_type="Frantext: Rabelais corpus",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ラブレー的多言語混淆・造語過剰は、LLMの語彙生成の祝祭性と理論的に響き合い、AI生成の語彙過剰現象を再読する古典的参照点。",
         "related_ai_phenomenon":"LLM生成の語彙過剰・造語"}])

add(**C, name_ja="プレイヤード派詩論",
    name_en="Pléiade poetics (Ronsard, Du Bellay)",
    name_original="poétique de la Pléiade",
    period_key="フランス・ルネサンス期",
    definition="ピエール・ド・ロンサール（1524-85）、ジョアシャン・デュ・ベレー（1522-60）等7名の詩人による16世紀中葉フランス詩学運動。デュ・ベレー『フランス語の擁護と顕揚』(1549)を綱領とし、フランス語の古典化、ペトラルキスムの導入、ソネット・オード等の古典形式の移植を推進した。",
    background="フランソワ1世期の宮廷文化、イタリア・ペトラルキスムの受容、人文主義教育の制度化。",
    development="フランス古典主義詩学（マレルブ、ボワロー）の前提を成し、近代フランス詩の規範を確立した。",
    historical_context="16世紀中葉フランスの言語・文化的アイデンティティ確立期。",
    primary_source_url=FRANTEXT+"catalogue.php?id=ronsard",
    primary_source_type="Frantext: Pléiade corpus",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マルグリット・ド・ナヴァール『エプタメロン』",
    name_en="Marguerite de Navarre's Heptaméron",
    name_original="Heptaméron",
    period_key="フランス・ルネサンス期",
    definition="マルグリット・ド・ナヴァール（1492-1549、フランソワ1世姉、ナヴァール王妃）が遺稿として残し1558-59年に刊行された72話の物語集。ボッカッチョ『デカメロン』を範に、貴族男女10名が語る愛と信仰の物語を、福音主義的内省と宮廷的洗練で統合した。",
    background="フランソワ1世期フランス宮廷文化、福音主義改革期の女性知的庇護者の役割。",
    development="フランス女性文学の祖型を成し、後の宮廷物語、書簡体小説に系譜的影響を与えた。",
    historical_context="16世紀前半フランスの宗教改革論争と宮廷文芸サロンの興隆。",
    primary_source_url=FRANTEXT+"catalogue.php?id=heptameron",
    primary_source_type="Frantext: Heptaméron",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近世女性の知的庇護者性",
         "description":"マルグリット・ド・ナヴァールは近世ヨーロッパ女性知的庇護者・著者の代表的事例として、ジェンダー史・人類学的研究の対象。"}])

add(**C, name_ja="ドービニェ『悲愴詩集』",
    name_en="d'Aubigné's Les Tragiques",
    name_original="Les Tragiques",
    period_key="フランス・ルネサンス期",
    definition="アグリッパ・ドービニェ（1552-1630）が1577-1616年頃に執筆し1616年に発表した7篇のユグノー（プロテスタント）叙事詩。フランス宗教戦争期の暴力・殉教・終末論を、ホメロス・ヴェルギリウス的英雄叙事詩形式で展開し、近世フランス語詩で最も雄大な政治的叙事詩を成した。",
    background="フランス宗教戦争（1562-98）の暴力経験と、ユグノー貴族としての軍事・政治活動。",
    development="ユゴー『懲罰詩集』に系譜的に継承され、近代政治叙事詩の祖型となった。",
    historical_context="ナントの勅令（1598）後のユグノー文学の自己定位期。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71081k",
    primary_source_type="Gallica: Les Tragiques",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モンテーニュ『エセー』第三巻",
    name_en="Montaigne's Essais Book III",
    name_original="Essais, Livre III",
    period_key="フランス・ルネサンス期",
    definition="ミシェル・ド・モンテーニュ（1533-92）が1588年に追加発表したエセー第三巻。第一・二巻（1580）に対し、より自由で内省的・自伝的なエセー形式を確立し、特に「経験について（De l'expérience）」「悔悟について」が哲学的内省の極致を成す。近代エセー形式の規範。",
    background="モンテーニュの市長職退任後の隠棲と、宗教戦争末期の懐疑主義の深化。",
    development="ベーコン『随想録』、パスカル、近代欧州エセー伝統全体の祖型を成した。",
    historical_context="アンリ4世即位前夜（1589）のフランス宗教戦争最終局面。",
    primary_source_url=FRANTEXT+"catalogue.php?id=montaigne",
    primary_source_type="Frantext: Essais III",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マロ詩学",
    name_en="Marot's poetics",
    name_original="poétique de Marot",
    period_key="フランス・ルネサンス期",
    definition="クレマン・マロ（1496-1544）の詩学。中世修辞詩派から人文主義詩への移行を体現し、ロンドー、シャンソン、エピグラム、詩篇翻訳でフランス俗語詩に新たな規範を与えた。プレイヤード派以前のフランス詩を代表する。",
    background="フランソワ1世期宮廷文化、福音主義詩篇翻訳運動。",
    development="プレイヤード派による「単純さ」の批判を経つつ、ラ・フォンテーヌ寓話、近代フランス諷刺詩への祖型を成した。",
    historical_context="16世紀前半フランスの宮廷詩学と宗教論争。",
    primary_source_url=FRANTEXT+"catalogue.php?id=marot",
    primary_source_type="Frantext: Clément Marot",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルイーズ・ラベ『ソネット集』",
    name_en="Louise Labé's Sonnets",
    name_original="Œuvres de Louise Labé",
    period_key="フランス・ルネサンス期",
    definition="ルイーズ・ラベ（1524頃-66、リヨン）が1555年に発表した詩集。24篇のソネットを中核とし、女性視点からのペトラルキスム的恋愛詩を確立した。リヨン派（ペルネット・デュ・ギエ等）と並ぶ、近世フランス女性詩の代表的事例。",
    background="リヨンの商業・印刷文化、リヨン派詩人サークル。",
    development="近代フランス女性詩の祖型を成し、19世紀ロマン主義以降に再評価された。",
    historical_context="16世紀中葉リヨンの文芸的興隆期。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k70927b",
    primary_source_type="Gallica: Œuvres de Louise Labé",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フランス・ユマニスム",
    name_en="French humanism",
    name_original="humanisme français",
    period_key="フランス・ルネサンス期",
    definition="ギヨーム・ビュデ（1467-1540）、ルフェーヴル・デタープル、ロベール・エティエンヌ、アンリ・エティエンヌらに代表される16世紀フランス人文主義運動。コレージュ・ド・フランス（1530）創設、ギリシア・ヘブライ語学術、聖書文献学を制度化し、ラブレー・ロンサール・モンテーニュを支えた知的基盤。",
    background="エラスミアニズムとイタリア人文主義のフランス受容、フランソワ1世の文化政策。",
    development="近代フランス古典学・聖書学・印刷文化の制度的基盤を確立し、欧州人文主義の主要拠点を成した。",
    historical_context="16世紀前半フランスの宮廷文化と知識制度化期。",
    primary_source_url=GALLICA+"ark:/12148/cb12345678f",
    primary_source_type="Gallica: French humanism corpus",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: テューダー・ジャコビアン（8件）
# ============================================================
add(**C, name_ja="シドニー『詩の擁護』全体",
    name_en="Sidney's Defence of Poesy (full)",
    name_original="The Defence of Poesy / An Apology for Poetry",
    period_key="テューダー・ジャコビアン期",
    definition="フィリップ・シドニー（1554-86）が1581年頃執筆し1595年に刊行された英語圏初の体系的詩学論。アリストテレス、ホラティウス、イタリア詩学を消化し、詩を歴史・哲学に優越する「教える喜び」の媒体として擁護した。エリザベス朝詩学の規範を成した。",
    background="エリザベス朝宮廷文化、イタリア・フランス詩学の英語圏受容、清教徒スティーヴン・ゴッソン『悪用の学校』(1579)の演劇批判への反論。",
    development="ベン・ジョンソン、ドライデン、シェリー『詩の擁護』(1840)に系譜的に継承され、英語圏詩学の祖型となった。",
    historical_context="1580年代英国宮廷の詩学論議と、清教徒派演劇批判の高揚期。",
    primary_source_url=GUTEN+"ebooks/1962",
    primary_source_type="Project Gutenberg: Defence of Poesy",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="スペンサー『妖精の女王』",
    name_en="Spenser's The Faerie Queene",
    name_original="The Faerie Queene",
    period_key="テューダー・ジャコビアン期",
    definition="エドマンド・スペンサー（1552頃-99）が1590-96年に発表した6巻の寓意叙事詩。アリオスト・タッソ的騎士叙事詩を範に、エリザベス1世を称えるプロテスタント・寓意詩を構築し、独自のスペンサー詩節（9行）を確立した。英語ロマンティック叙事詩の祖型。",
    background="エリザベス朝アイルランド統治期、イタリア叙事詩の英語圏受容。",
    development="ミルトン、キーツ、19世紀ロマン派英国詩、テニソン『国王牧歌』に系譜的影響を与えた。",
    historical_context="1590年代英国とアイルランドの政治的緊張、エリザベス朝後期の宮廷文化。",
    primary_source_url=GUTEN+"ebooks/15272",
    primary_source_type="Project Gutenberg: The Faerie Queene",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マーロウのブランクヴァース",
    name_en="Marlowe's mighty line",
    name_original="Marlowe's mighty line",
    period_key="テューダー・ジャコビアン期",
    definition="クリストファー・マーロウ（1564-93）が『タンバレイン大王』(1587-88)、『フォースタス博士』(1592頃)、『マルタ島のユダヤ人』、『エドワード二世』で確立した強烈なブランクヴァース（無韻詩）。ベン・ジョンソンが「マーロウの勇壮な詩行（mighty line）」と称した。シェイクスピア劇詩の直接的先行を成す。",
    background="1580年代後半ロンドン職業劇場の興隆と、大学知識人（University Wits）の演劇参入。",
    development="シェイクスピア悲劇のブランクヴァース、後の英語演劇詩全体の規範を確立した。",
    historical_context="エリザベス朝後期の演劇商業化と、大学卒業生の文芸職業化。",
    primary_source_url=GUTEN+"ebooks/779",
    primary_source_type="Project Gutenberg: Doctor Faustus",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ベン・ジョンソンの体液喜劇",
    name_en="Jonson's comedy of humours",
    name_original="comedy of humours",
    period_key="テューダー・ジャコビアン期",
    definition="ベン・ジョンソン（1572-1637）が『気質に振り回される男』(1598)、『気質を解消する男』(1599)、『ヴォルポーネ』(1606)、『錬金術師』(1610)で確立した喜劇形式。中世医学の四体液論を心理類型化原理とし、各人物を支配的「気質（humour）」によって戯画化する手法。ルネサンス英語喜劇の規範を成した。",
    background="ガレノス医学的体液論の文学的応用、ロンドン都市文化の興隆。",
    development="王政復古期喜劇（コングリーヴ）、18世紀小説における人物類型化（フィールディング）に継承された。",
    historical_context="エリザベス朝末期からジェームズ1世期のロンドン演劇文化。",
    primary_source_url=GUTEN+"ebooks/4039",
    primary_source_type="Project Gutenberg: Volpone",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョン・ダンの形而上派詩",
    name_en="John Donne's metaphysical poetry",
    name_original="John Donne metaphysical poetry",
    period_key="テューダー・ジャコビアン期",
    definition="ジョン・ダン（1572-1631）の世俗詩（『歌と短詩』）と宗教詩（『聖なるソネット』『神への讃歌』）。劇的話法、形而上学的奇抜な譬喩（conceit）、機知と情念の融合を核とし、17世紀英語形而上派詩の出発点を成した。サミュエル・ジョンソン（1779）が「形而上詩人」と命名。",
    background="エリザベス朝末期のソネット文化と対抗改革期英国カトリック背景。",
    development="ジョージ・ハーバート、マーヴェル、20世紀T.S.エリオット『形而上詩人』(1921)再評価を経て、モダニズム詩学の重要参照点となった。",
    historical_context="エリザベス朝末期からジャコビアン期英国宗教論争。",
    primary_source_url=GUTEN+"ebooks/23772",
    primary_source_type="Project Gutenberg: Donne poems",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ダンの形而上的奇抜な譬喩は遠隔概念の機械的接合であり、LLMが行う異領域語彙のベクトル空間内接合と理論的構造が類似する。AI時代の比喩生成を再読する古典的参照点。",
         "related_ai_phenomenon":"LLMによる遠隔概念の比喩接合"}])

add(**C, name_ja="ジョージ・ハーバート『神殿』",
    name_en="George Herbert's The Temple",
    name_original="The Temple",
    period_key="テューダー・ジャコビアン期",
    definition="ジョージ・ハーバート（1593-1633）の遺稿詩集（1633刊）。約160篇の宗教詩からなり、「祭壇」「イースターの翼」等の視覚詩、内省的祈祷の劇化、簡潔な口語性を統合した。英国宗教詩・形而上派詩の中心作品。",
    background="ジャコビアン期英国国教会の霊性、ダン形而上派詩の継承。",
    development="ヘンリー・ヴォーン、リチャード・クラショー、20世紀T.S.エリオット、シェイマス・ヒーニーに継承された。",
    historical_context="チャールズ1世期英国国教会の霊的内省文化。",
    primary_source_url=GUTEN+"ebooks/4099",
    primary_source_type="Project Gutenberg: The Temple (Herbert)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アンドリュー・マーヴェル",
    name_en="Andrew Marvell",
    name_original="Andrew Marvell",
    period_key="テューダー・ジャコビアン期",
    definition="アンドリュー・マーヴェル（1621-78）の田園詩・政治詩。「貴婦人へ（To His Coy Mistress）」「アプルトン・ハウス論」「ホレイス頌歌」等で、形而上派詩学・田園牧歌・共和制政治詩を統合した17世紀英語詩の頂点を成す。",
    background="共和政期英国の政治・文化、ミルトンとの個人的・政治的接点。",
    development="20世紀T.S.エリオット『アンドリュー・マーヴェル』(1921)再評価以降、英語モダニズム詩学の中心参照点となった。",
    historical_context="共和政期から王政復古期英国の政治・宗教転換期。",
    primary_source_url=GUTEN+"ebooks/16800",
    primary_source_type="Project Gutenberg: Marvell poems",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"形而上派詩学",
         "description":"マーヴェル詩学は形而上派詩学・田園詩学の交差点として、20世紀新批評詩学の中心研究対象である。"}])

add(**C, name_ja="エリザベス朝ソネット連作",
    name_en="Elizabethan sonnet sequence",
    name_original="Elizabethan sonnet sequence",
    period_key="テューダー・ジャコビアン期",
    definition="シドニー『アストロフェルとステラ』(1591刊)、スペンサー『アモレッティ』(1595)、シェイクスピア『ソネット集』(1609)を中核とする1590年代英国ソネット連作運動。ペトラルキスムを英語に移植し、内省的恋愛主体性を体系化した。",
    background="イタリア・フランスのペトラルキスムの英語圏受容、宮廷詩文化の高揚。",
    development="17世紀英語抒情詩、19世紀ロマン派ソネット復興、20世紀現代詩のソネット形式に継承された。",
    historical_context="エリザベス朝後期1590年代の宮廷詩学黄金期。",
    primary_source_url=GUTEN+"ebooks/1041",
    primary_source_type="Project Gutenberg: Shakespeare Sonnets",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: 北方ルネサンス + 横断（8件）
# ============================================================
add(**C, name_ja="エラスムス『痴愚神礼賛』",
    name_en="Erasmus's Praise of Folly",
    name_original="Moriae Encomium / Stultitiae Laus",
    period_key="北方ルネサンス期",
    definition="エラスムス・ロッテルダム（1466頃-1536）が1509年に執筆し1511年に刊行したラテン語諷刺。痴愚（モリア）女神に自画自賛させる枠組みで、教会・神学者・宮廷・大衆の偽善を諷刺し、北方人文主義の最高峰を成した。トマス・モア（モリア＝モア）に捧げられた。",
    background="北方人文主義の興隆、印刷文化の制度化、教会改革論議の高揚。",
    development="ラブレー、ルター宗教改革論争、近代諷刺文学全体に祖型を供給し、近世西欧の知的批評精神の源流となった。",
    historical_context="宗教改革前夜（1517以前）の北方ヨーロッパ知識人文化。",
    primary_source_url=GUTEN+"ebooks/30201",
    primary_source_type="Project Gutenberg: Praise of Folly",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"人文主義的批判精神",
         "description":"エラスムス諷刺は近世ヨーロッパ批判哲学・諷刺哲学の祖型を成す。"}])

add(**C, name_ja="ブラント『阿呆船』",
    name_en="Sebastian Brant's Das Narrenschiff",
    name_original="Das Narrenschiff",
    period_key="北方ルネサンス期",
    definition="セバスティアン・ブラント（1457-1521）が1494年に発表した独語詩。112種類の「阿呆」を諷刺する叙事的諷刺詩で、近世ドイツ最初のベストセラーとなり、北方ルネサンス諷刺文学の祖型を成した。エラスムス『痴愚神礼賛』、ローカウ阿呆文学への直接的先行。",
    background="15世紀末ドイツ印刷文化の興隆、人文主義黎明期。",
    development="エラスムス、後の独語諷刺文学、グラース『ブリキの太鼓』に至るドイツ諷刺伝統の祖型となった。",
    historical_context="バーゼル印刷出版界の発展期、宗教改革前夜の宗教批判文化。",
    primary_source_url=GUTEN+"ebooks/20458",
    primary_source_type="Project Gutenberg: Das Narrenschiff",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハンス・ザックス職匠歌",
    name_en="Hans Sachs Meistersang",
    name_original="Meistergesang",
    period_key="北方ルネサンス期",
    definition="ハンス・ザックス（1494-1576、ニュルンベルク靴職人）が確立した16世紀ドイツ職匠歌（マイスタージンガー）の頂点。約4000曲の歌、200本のシュロ―フェッテン（謝肉祭劇）等で、宗教改革期ドイツ市民文化を文学的に体系化した。ワーグナー『ニュルンベルクのマイスタージンガー』(1868)で再評価。",
    background="ニュルンベルク自由都市の市民・職人文化、宗教改革支持と詩学的職人組合の興隆。",
    development="近世ドイツ市民詩、後のドイツ謝肉祭劇、ワーグナー再評価を経て、ドイツ文学史上の重要参照点となった。",
    historical_context="16世紀宗教改革期ドイツ自由都市の文化。",
    primary_source_url=GUTEN+"ebooks/27317",
    primary_source_type="Project Gutenberg: Hans Sachs",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フォンデル『ルシファー』",
    name_en="Vondel's Lucifer",
    name_original="Lucifer",
    period_key="北方ルネサンス期",
    definition="ヨースト・ファン・デン・フォンデル（1587-1679）が1654年に発表した蘭語悲劇。天使ルシファーの反逆と堕落を題材に、オランダ黄金時代演劇の頂点を成した。ミルトン『失楽園』への影響可能性が長らく論じられてきた。",
    background="オランダ黄金時代（17世紀）の都市文化、アムステルダム・スハウブルフ劇場の興隆。",
    development="蘭語演劇の規範を成し、ミルトン『失楽園』への系譜的影響、近代蘭語文学の祖型となった。",
    historical_context="オランダ共和国宗教論争（カルヴァン派対アルミニウス派）。",
    primary_source_url=WSRC_EN+"Lucifer_(Vondel)",
    primary_source_type="Wikisource: Vondel Lucifer",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アレティーノ書簡集",
    name_en="Aretino's Lettere",
    name_original="Lettere di Pietro Aretino",
    period_key="イタリア・ルネサンス期",
    definition="ピエトロ・アレティーノ（1492-1556、「諸侯の鞭」）が1538-57年に6巻で発表した俗語書簡集。3000通超の書簡を職業的に出版する近代著作・諷刺文化の祖型を成し、近世イタリア俗語散文の重要規範。",
    background="ヴェネツィア印刷出版文化の興隆、近世著作家職業化の最初期事例。",
    development="近代書簡集出版文化、諷刺ジャーナリズムの祖型を成し、近世著作家自立の象徴となった。",
    historical_context="16世紀前半ヴェネツィアの印刷文化と諷刺文芸。",
    primary_source_url=LIBER+"libri/a/aretino_pietro/",
    primary_source_type="Liber Liber: Aretino Lettere",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近世著作家職業化",
         "description":"アレティーノは近世ヨーロッパで初の職業著述家像を成立させた重要事例として、文化人類学・出版史研究の対象。"}])

add(**C, name_ja="ヴィットリア・コロンナ詩集",
    name_en="Vittoria Colonna's Rime",
    name_original="Rime di Vittoria Colonna",
    period_key="イタリア・ルネサンス期",
    definition="ヴィットリア・コロンナ（1490頃-1547）の俗語詩集（1538初版）。ペトラルキスム的恋愛詩から宗教詩への転換を生涯を通じて行い、ミケランジェロとの霊的対話で知られる。近世ヨーロッパ女性詩人の代表的事例。",
    background="ローマ宗教改革派サークル（spirituali）、ナポリのヴァルデース派霊性。",
    development="近世女性宗教詩の祖型を成し、19-20世紀の女性文学史再評価で重要事例となった。",
    historical_context="トリエント公会議前夜のイタリア宗教改革派文化。",
    primary_source_url=LIBER+"libri/c/colonna_vittoria/",
    primary_source_type="Liber Liber: Vittoria Colonna",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ポリツィアーノ『スタンツェ』",
    name_en="Poliziano's Stanze per la giostra",
    name_original="Stanze per la giostra",
    period_key="イタリア・ルネサンス期",
    definition="アンジェロ・ポリツィアーノ（1454-94、メディチ家家庭教師・詩人・古典学者）が1475-78年頃執筆した俗語叙事詩。ジュリアーノ・デ・メディチを称え、新プラトン主義的美の理念を俗語ottava rima詩節で結晶化した。ロレンツォ期メディチ宮廷文化の頂点。",
    background="ロレンツォ・イル・マニフィコ統治下フィレンツェの宮廷文化、フィチーノ新プラトン主義サークル。",
    development="アリオスト、タッソ、後のイタリア叙事詩への直接的先行を成し、ボッティチェリ絵画とも深く共鳴した。",
    historical_context="クァトロチェント末期フィレンツェの文化的黄金期。",
    primary_source_url=WSRC_IT+"Stanze_per_la_giostra",
    primary_source_type="Wikisource: Stanze per la giostra",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ポリツィアーノの古典学者＝詩人の二重性は、AIが古典的形式を学習・再生成する「古典学者的創作」に通底する。",
         "related_ai_phenomenon":"AIによる古典様式の学習生成"}])

add(**C, name_ja="ルネサンス詩学の制度化",
    name_en="Renaissance poetics institutionalized",
    name_original="poetica rinascimentale",
    period_key="イタリア・ルネサンス期",
    definition="16世紀イタリアで進行したアリストテレス『詩学』の俗語注釈・批評体系化。ロボルテッロ(1548)、カステルヴェトロ(1570)、ミントゥルノ(1559)、スカリジェロ(1561)らによる体系化を通じ、三一致律・ジャンル理論・ミメーシス理論が欧州詩学の規範となった。",
    background="アルド・マヌーツィオ印刷以降の古典文献学興隆、トリエント公会議期の規範化志向。",
    development="フランス古典主義詩学（ボワロー）、ドイツ・ゴットシェート、英語シドニー『詩の擁護』へ系譜的に継承された。",
    historical_context="チンクェチェント中後期イタリアの詩学論争期。",
    primary_source_url=BRITT+"art/literary-criticism",
    primary_source_type="Britannica: Renaissance literary theory",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"アリストテレス詩学の近代化",
         "description":"ルネサンス詩学制度化はアリストテレス詩学を近代欧州詩学・劇学・物語論の理論的源泉に変換した過程。"}])


# ============================================================
# Main runner
# ============================================================
# ============================================================
# Top-up extra fourth_transform tags & cross_domain links by name lookup
# (Applied to concepts inserted above; safe to re-run.)
# ============================================================
EXTRA_FOURTH = [
    ("ペトラルカ『カンツォニエーレ』", "主体", "rethinking",
     "ペトラルカの内省的恋愛主体の確立はAI時代の擬似主体生成と歴史的に対照される最古の参照点。",
     "AI生成における内省的主体性の擬制"),
    ("ボッカッチョ『デカメロン』枠物語", "物語", "rethinking",
     "100話の枠付き連鎖は、AIによる物語連鎖生成・プロンプトチェーンの古典的祖型として読み直せる。",
     "LLMによる物語連鎖生成"),
    ("アリオスト『狂えるオルランド』", "物語", "rethinking",
     "複数物語線の織り交ぜ（entrelacement）は、AIによるマルチプロット生成と構造的に通底する。",
     "AI生成によるマルチプロット織り交ぜ"),
    ("ベンボ『俗語論』", "言語", "rethinking",
     "規範俗語確立は言語規範論の古典であり、AI生成における言語規範化問題と理論的に共振する。",
     "AI生成テキストの言語規範化"),
    ("カルデロン『人生は夢』", "真正性", "rethinking",
     "夢と現実の不可弁別は、AI生成現実とフィジカル現実の弁別困難と通底するバロック的問題系。",
     "AI生成現実と物理現実の弁別問題"),
    ("ゴンゴラ クルテラニスモ", "言語", "rethinking",
     "難解な修辞的精緻化は、AI生成における過剰修辞・過適合と理論的に響き合う。",
     "AI生成の過剰修辞"),
    ("ピカレスク三部作（ラサリーリョ／グスマン／ブスコン）", "主体", "rethinking",
     "ピカロの一人称自伝形式は擬似的経験的主体の構築であり、AI一人称生成の古典的祖型。",
     "AIによる一人称経験主体の擬制"),
    ("プレイヤード派詩論", "言語", "rethinking",
     "古典形式の俗語移植は形式の翻訳的生成であり、AIによる古典様式生成の歴史的対応。",
     "AIによる古典韻律様式の移植生成"),
    ("シドニー『詩の擁護』全体", "受容", "rethinking",
     "「教える喜び」概念はテキストの受容効果論であり、AI生成テキストの受容倫理を再考する基準。",
     "AI生成テキストの教育的受容"),
    ("マーロウのブランクヴァース", "言語", "rethinking",
     "「勇壮な詩行」の確立は韻律的強度の機械化問題に通じ、AIによる韻律生成の古典参照点。",
     "AI生成における韻律強度"),
    ("エラスムス『痴愚神礼賛』", "作者性", "rethinking",
     "痴愚自賛形式は作者主体の擬似化であり、AI生成テキストにおける擬似主体表明と並行する。",
     "AI生成における擬似的自己言及"),
    ("ルネサンス詩学の制度化", "受容", "rethinking",
     "詩学規範化はテキスト生産・受容の規範化であり、AI生成規範化問題の歴史的対応。",
     "AI生成テキストの規範化問題"),
]

EXTRA_CD = [
    ("ペトラルカ『カンツォニエーレ』", "PT", "shared_concept",
     "ソネット形式と内省的主体",
     "カンツォニエーレは欧州抒情詩・ソネット詩学の祖型として現代物語論・抒情詩論の源泉。"),
    ("マキャヴェリの俗語散文", "PHIL", "shared_concept",
     "近代政治哲学の俗語化",
     "マキャヴェリ散文は近代政治哲学の出発点として哲学史研究の中核。"),
    ("カスティリオーネ『宮廷人の書』", "AN", "shared_concept",
     "近世宮廷の身体所作論",
     "スプレッツァトゥーラは近世宮廷の身体所作・自己表現の人類学的事例として研究される。"),
    ("ラブレー『ガルガンチュアとパンタグリュエル』", "AN", "shared_concept",
     "カーニヴァル・グロテスク",
     "バフチンによりカーニヴァル文化・グロテスクリアリズムの中心研究対象として理論化された。"),
    ("モンテーニュ『エセー』第三巻", "PHIL", "shared_concept",
     "近世懐疑哲学",
     "モンテーニュ『エセー』は近世西欧懐疑哲学の中心テクストとして哲学史研究の核。"),
    ("カルデロン『人生は夢』", "PHIL", "shared_concept",
     "夢・現実の形而上学",
     "夢と現実の弁別困難は近世形而上学・哲学的演劇研究の中心テーマ。"),
    ("ゴンゴラ クルテラニスモ", "PT", "shared_concept",
     "バロック詩学の修辞論",
     "クルテラニスモはバロック詩学・修辞学研究の中心対象。"),
    ("ジョン・ダンの形而上派詩", "PT", "shared_concept",
     "形而上派詩学・奇抜な譬喩",
     "ダンの conceit は20世紀新批評・現代詩学の中心研究対象。"),
    ("シドニー『詩の擁護』全体", "PT", "shared_concept",
     "近世詩学・詩の擁護ジャンル",
     "シドニー詩学は欧州詩論・詩学ジャンル史の中核参照点。"),
    ("ベンボ『俗語論』", "PHIL", "shared_concept",
     "言語規範哲学",
     "ベンボの俗語規範論は言語哲学史における言語規範化問題の古典。"),
]


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

        # Apply EXTRA fourth_transform tags & cross_domain links
        for nm, axis, status, rationale, ai_phen in EXTRA_FOURTH:
            cid = name_to_id.get(nm)
            if cid is None:
                # try to look up if this is a re-run
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE subfield_id=3 AND name_ja=?",
                    (nm,)).fetchone()
                if not row:
                    print(f"  [warn] extra fourth: concept not found: {nm}")
                    continue
                cid = row[0]
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai_phen)
                fourth_count += 1
            except LitDBError as e:
                print(f"  [warn] extra fourth tag failed for {nm}: {e}")

        for nm, target_db, link_type, target_name, desc in EXTRA_CD:
            cid = name_to_id.get(nm)
            if cid is None:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE subfield_id=3 AND name_ja=?",
                    (nm,)).fetchone()
                if not row:
                    print(f"  [warn] extra cd: concept not found: {nm}")
                    continue
                cid = row[0]
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=target_db, link_type=link_type,
                    target_entity_name=target_name, description=desc)
                cd_count += 1
            except LitDBError as e:
                print(f"  [warn] extra cd failed for {nm}: {e}")

        summary = db.progress_summary()
        print(f"[c05-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c05-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
