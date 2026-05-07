"""LIT-DB Phase 2 Wave 5 — C38: Comparative Literature, World Literature,
and Translation Theory (40 concepts).

Subfield: lit_world_translation (id=23), region='理論'.

Sources used (all real, verifiable):
  - Stanford Encyclopedia of Philosophy (plato.stanford.edu)
  - JSTOR-indexed scholarly references (https://www.jstor.org/)
  - Project MUSE (https://muse.jhu.edu/)
  - Cambridge Companion / Routledge handbook listings (publishers.cambridge.org / routledge.com)
  - Translation Studies / Target academic journals (e.g. https://www.benjamins.com/catalog/target)
  - UNESCO Index Translationum (https://www.unesco.org/xtrans/)
  - academic-grade Wikipedia (en/ja)

Tier policy (PHASE2_OPERATIONAL_RULES.md):
  - Foundational primary texts (Goethe's Weltliteratur, Benjamin "Die Aufgabe des
    Übersetzers", Jakobson "On Linguistic Aspects of Translation") -> 'primary'
  - Major scholarly monographs (Damrosch, Casanova, Apter, Venuti, Bassnett,
    Even-Zohar, Toury, Nida, Berman, Spivak) -> 'secondary' when accessed via
    secondary citation surfaces (Cambridge Companion / Routledge / SEP / JSTOR)
  - Synthetic/derivative critical categories without single canonical source ->
    'tertiary'
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Comparative literature, world literature, and translation theory are
# transhistorical theoretical fields. We define three umbrella periods to
# locate the concepts roughly along the disciplinary timeline.
PERIODS = [
    ("比較文学形成期", "Formation of Comparative Literature", 1800, 1950,
     "ゲーテ「世界文学」(1827)、ヴェセロフスキー比較文学から、第二次世界大戦終結までの比較文学・翻訳学の制度的・理論的形成期。"),
    ("構造主義・記述的翻訳学期", "Structuralist & Descriptive Translation Studies",
     1950, 1990,
     "ヤコブソン・ナイダから、ホームズ「翻訳学の名と性質」(1972)、トゥーリ記述的翻訳学、エヴェン=ゾーハー・ポリシステム理論までの理論的整備期。"),
    ("世界文学・ポストコロニアル翻訳期",
     "World Literature & Postcolonial Translation",
     1990, 2030,
     "1990年代以降のポストコロニアル翻訳論、文化的転回、ダムロッシュ・カサノヴァ・モレッティの新世界文学論、アプター翻訳不可能性、AI翻訳台頭までの現代期。"),
]


# Source URL bases (real, verifiable)
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
JSTOR = "https://www.jstor.org/"
MUSE = "https://muse.jhu.edu/"
ROUTLEDGE = "https://www.routledge.com/"
CAMBRIDGE = "https://www.cambridge.org/"
BENJAMINS = "https://benjamins.com/catalog/"  # John Benjamins (translation studies)
UNESCO_XTRANS = "https://www.unesco.org/xtrans/"
GUTEN = "https://www.gutenberg.org/"
PRINCETON_UP = "https://press.princeton.edu/books/"
HARVARD_UP = "https://www.hup.harvard.edu/books/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_world_translation", region="理論",
         original_script="roman")


# ============================================================
# A: 比較文学の起源と方法（8件）
# ============================================================
add(**C, name_ja="世界文学（ゲーテ）", name_en="Weltliteratur (Goethe)",
    name_original="Weltliteratur",
    period_key="比較文学形成期",
    definition="ゲーテが1827年エッカーマンとの対話および書簡で初めて提唱した概念で、国民文学の枠を超えて諸民族の文学が相互に翻訳・受容・対話することで形成される普遍的文学圏を指す。比較文学・世界文学論の出発点と位置づけられる。",
    background="ナポレオン戦争後の国民国家形成期に、文学的国民主義への対抗として、コスモポリタンな文学交流の理念がゲーテによって構想された。",
    development="マルクス・エンゲルス『共産党宣言』(1848)が世界市場の比喩として継承し、20世紀後半のダムロッシュ・カサノヴァらの新世界文学論まで連続する基礎概念となった。",
    historical_context="19世紀前半ドイツの古典・ロマン主義以降のヨーロッパ国民文学制度化への理論的相対化。",
    primary_source_url=WIKI_EN+"Weltliteratur",
    primary_source_type="Wikipedia: Weltliteratur (academic, multi-source)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"AI翻訳の汎用化により、ゲーテが構想した「翻訳を介した文学の世界圏」が文字通り即時実現可能になり、19世紀的な選別的世界正典概念が問い直される。",
         "related_ai_phenomenon":"AI翻訳による世界文学概念の物質的実現と正典選別の解体"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"普遍主義（ゲーテ・カント）",
         "description":"ゲーテのWeltliteratur構想とカント世界市民主義の哲学的接続。"}])


add(subfield_code="lit_world_translation", region="理論",
    name_ja="ヴェセロフスキー比較文学",
    name_en="Veselovsky's historical poetics",
    name_original="историческая поэтика",
    original_script="cyrillic",
    period_key="比較文学形成期",
    definition="アレクサンドル・ヴェセロフスキー(1838-1906)が確立した、世界諸文学の主題・モチーフ・プロット要素の歴史的伝播・進化を追跡する比較文学の方法。20世紀のロシア・フォルマリズム及びプロップ昔話形態学の前史となった。",
    background="19世紀後半ロシアにおけるアレクサンドル・フォン・フンボルト的世界知の理想と、ベンファイ「インド起源説」的伝播研究の継承。",
    development="プロップ『昔話の形態学』(1928)、バフチン的歴史的詩学に継承され、現代世界文学論に再評価された。",
    historical_context="ロシア帝国期の比較文献学・東西文化交流研究。",
    primary_source_url=WIKI_EN+"Alexander_Veselovsky",
    primary_source_type="Wikipedia: Alexander Veselovsky (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"歴史的詩学",
         "description":"ヴェセロフスキー歴史的詩学はPT-DBの詩学概念とも横断的接続。"},
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"昔話モチーフ伝播",
         "description":"プロップ・スティス・トンプソン的世界昔話研究との接続。"}])


add(**C, name_ja="比較文学の三派（仏・米・斯）",
    name_en="three schools of comparative literature",
    name_original="French / American / Slavic schools",
    period_key="比較文学形成期",
    definition="20世紀比較文学の方法論的三系譜。フランス派（影響研究、文献実証）、アメリカ派（並行研究、テクスト内在的読解）、東欧・スラヴ派（歴史的詩学、形式主義）の対立と相互補完が比較文学の方法論的議論を構造化した。",
    background="第二次大戦後のヨーロッパ比較文学制度（ICLA, 1955設立）における方法論論争の歴史的構造化。",
    development="1960年代エティアンブル「比較文学反論」、ウェルレク「文学一般論への要請」、後の世界文学派（カサノヴァ・モレッティ）への分化を生んだ。",
    historical_context="冷戦期の学術的国際協力と、各国比較文学伝統の制度的調停。",
    primary_source_url=WIKI_EN+"Comparative_literature",
    primary_source_type="Wikipedia: Comparative literature (academic)",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")


add(**C, name_ja="クローチェ美学", name_en="Croce's aesthetics",
    name_original="Estetica come scienza dell'espressione",
    period_key="比較文学形成期",
    definition="ベネデット・クローチェ『表現の科学および一般言語学としての美学』(1902)が定式化した、芸術を「直観=表現」と捉える美学。各作品の唯一性・翻訳不可能性を強調し、比較文学の科学的厳密化に対する哲学的留保を提示した重要理論。",
    background="ヘーゲル弁証法・ジャンバッティスタ・ヴィーコ歴史哲学のイタリア的総合と、19世紀末実証主義美学への対抗。",
    development="新批評の作品自律論、20世紀後半の翻訳不可能性論争（アプター）まで思想的影響を残す。",
    historical_context="20世紀初頭イタリアの新観念論的美学運動。",
    primary_source_url=SEP+"croce-aesthetics/",
    primary_source_type="Stanford Encyclopedia of Philosophy: Croce's Aesthetics",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"クローチェ表現美学",
         "description":"クローチェ美学は哲学DBの新観念論項目とも重複する横断概念。"}])


add(**C, name_ja="エティアンブル「比較文学反論」",
    name_en="Étiemble's 'Comparaison n'est pas raison'",
    name_original="Comparaison n'est pas raison",
    period_key="比較文学形成期",
    definition="ルネ・エティアンブル(1909-2002)が1963年同名著作で展開した、フランス派比較文学の影響実証主義への批判。ヨーロッパ中心主義を超えてアラビア・中国・日本文学を含む真の世界比較文学の必要を主張し、後の世界文学論の先駆けとなった。",
    background="1950年代フランス派の文献実証的比較文学（ヴァン・ティーゲム、ギヤール）への方法論的不満。",
    development="ダムロッシュ・カサノヴァ世界文学論、スピヴァク『学問分野の死』への理論的前史となる。",
    historical_context="脱植民地化期のヨーロッパ中心主義批判の比較文学版。",
    primary_source_url=WIKI_EN+"Ren%C3%A9_%C3%89tiemble",
    primary_source_type="Wikipedia: René Étiemble (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


add(**C, name_ja="影響研究 vs 並行研究",
    name_en="influence study vs parallel study",
    name_original="influence study / parallel study",
    period_key="比較文学形成期",
    definition="比較文学方法論の二大対立。「影響研究」(rapports de fait, フランス派)は文献的・歴史的に実証可能な影響関係を追究し、「並行研究」(parallel study, 米国派ウェルレク・ウォーレン)は影響関係の有無に関わらず構造的類似や類型を比較する。",
    background="第二次大戦後フランス比較文学（ヴァン・ティーゲム派）と米国新批評の方法論的対立の制度化。",
    development="1960-70年代のウェルレク・エティアンブル論争を経て、両派の併用が一般化。後のモレッティ「distant reading」は両派を量的方法で総合する試みでもある。",
    historical_context="冷戦期米欧学術の方法論的分岐の比較文学的表現。",
    primary_source_url=WIKI_EN+"Comparative_literature",
    primary_source_type="Wikipedia: Comparative literature (academic)",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")


add(**C, name_ja="翻訳研究受容史的接近",
    name_en="reception-historical approach to translation",
    name_original="Rezeptionsgeschichte / reception history",
    period_key="構造主義・記述的翻訳学期",
    definition="翻訳を独立した文学的事実として、目標文化における受容過程を中心に分析する方法。コンスタンツ学派受容美学（ヤウス、イーザー）の翻訳学への適用で、翻訳テクストが目標文化に与える効果と、目標文化が翻訳に課す制約を双方向的に分析する。",
    background="1960-70年代ドイツのコンスタンツ学派受容美学と、1970年代ホームズ「翻訳学の名と性質」(1972)の方法論的影響。",
    development="エヴェン=ゾーハー・ポリシステム理論、トゥーリ記述的翻訳学に発展的継承され、現代翻訳学の基礎方法となった。",
    historical_context="戦後ドイツ受容美学と翻訳研究の制度的合流。",
    primary_source_url=BENJAMINS+"target",
    primary_source_type="Target: International Journal of Translation Studies (Benjamins)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"AI翻訳の即時遍在化により、人間読者の受容過程を中心とする受容史的接近が、機械翻訳テクストの大量受容という新次元を組み込む必要に迫られている。",
         "related_ai_phenomenon":"機械翻訳テクストの大量受容と読者経験の変容"}])


add(**C, name_ja="ポリシステム理論", name_en="polysystem theory",
    name_original="polysystem theory",
    period_key="構造主義・記述的翻訳学期",
    definition="イタマル・エヴェン=ゾーハー(1939-)が1970-90年代に展開した、文学・翻訳を中心-周辺の力学を持つ動的な「多体系」(polysystem)として捉える理論。翻訳文学が目標文化のポリシステムにおいて中心的または周辺的位置を占める条件を体系的に分析する。",
    background="ロシア・フォルマリズムのチィニャーノフ「文学的事実」概念と、1970年代テル・アヴィヴ学派の構造主義的翻訳研究の合流。",
    development="トゥーリ記述的翻訳学、ヘルマンス「翻訳の操作的アプローチ」(1985)、現代の社会学的翻訳学（カサノヴァ・サポリティ）まで継承。",
    historical_context="1970-80年代翻訳学の独立学問化（Translation Studies as Discipline）の理論的基盤。",
    primary_source_url=WIKI_EN+"Polysystem_theory",
    primary_source_type="Wikipedia: Polysystem theory (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"システム詩学",
         "description":"エヴェン=ゾーハーのポリシステムは詩学DBのシステム理論と接続。"}])


# ============================================================
# B: 世界文学論（21世紀）（8件）
# ============================================================
add(**C, name_ja="ダムロッシュ「世界文学とは何か」",
    name_en="Damrosch 'What Is World Literature?'",
    name_original="What Is World Literature?",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="デイヴィッド・ダムロッシュ(1953-)『世界文学とは何か』(2003)が定式化した、「世界文学とは出発文化の外で翻訳を通じて流通・受容される文学」とする操作的定義。世界文学を実体ではなく「流通の様態」として捉える点で、それ以前の正典中心的世界文学観を相対化した。",
    background="1990年代以降のグローバリゼーションと比較文学の世界文学的再編、ハーバード比較文学科のヘレナ・コフを継承する世界文学プログラムの制度的展開。",
    development="2009年Longman Anthology of World Literature、Routledge Companion to World Literature編集を通じた世界文学カノン再編に発展。",
    historical_context="グローバリゼーション期の比較文学のスケール再編。",
    primary_source_url=PRINCETON_UP+"hardcover/9780691049861/what-is-world-literature",
    primary_source_type="Princeton University Press: What Is World Literature?",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"翻訳を介した流通として世界文学を定義する立場は、AI翻訳が翻訳の物質的・経済的コストを激減させた時代に、「流通」概念自体の再検討を迫る。",
         "related_ai_phenomenon":"AI翻訳時代の世界文学流通モデルの再定義"}])


add(**C, name_ja="カサノヴァ「文学の世界共和国」",
    name_en="Casanova 'The World Republic of Letters'",
    name_original="La République mondiale des Lettres",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="パスカル・カサノヴァ(1959-2018)『文学の世界共和国』(1999)が、ブルデューの場の理論を援用して提示した、世界文学を不平等な象徴資本の循環場として描く理論。パリを中心とする世界文学の「文学的グリニッジ標準時」と、周辺文学の中心化戦略を分析した。",
    background="1990年代フランス社会学（ブルデュー文化生産の場理論）の文学研究への応用。",
    development="モレッティ世界文学論（distant reading）、ピザロ・ティナホネス『世界文学の社会学』(2005)等、世界文学の社会学的接近を制度化した。",
    historical_context="グローバリゼーション期の世界文学論の社会学的転回。",
    primary_source_url=HARVARD_UP+"9780674010215/the-world-republic-of-letters",
    primary_source_type="Harvard University Press: The World Republic of Letters",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"パリ中心の文学的象徴資本の不平等構造というカサノヴァの診断は、AI翻訳と英語ベースLLMが新しい「言語的グリニッジ標準時」を生成する可能性として再考を迫られる。",
         "related_ai_phenomenon":"英語LLMによる新しい世界文学的中心の形成"}],
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"文化生産の場",
         "description":"ブルデュー由来の「場」理論は経営学DB組織論とも接続。"}])


add(**C, name_ja="モレッティ「distant reading」",
    name_en="Moretti 'distant reading'",
    name_original="distant reading",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="フランコ・モレッティ(1950-)が2000年New Left Review論文「世界文学への試論」で提唱した、個別テクストの精読(close reading)では捉えられない世界文学的傾向を、量的・地図的・進化論的アプローチで分析する方法。デジタル人文学的世界文学研究の旗印となった。",
    background="2000年代初頭の文学研究のデジタル化と、世界文学論の量的方法的転回の合流。",
    development="スタンフォード文学ラボ(2010設立)、Distant Reading COST Action(2017-22)等、計算的世界文学研究の制度化を生んだ。",
    historical_context="デジタル人文学の制度的成立期(2000-2010)。",
    primary_source_url=WIKI_EN+"Distant_reading",
    primary_source_type="Wikipedia: Distant reading (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"distant readingが提示した「読まずに分析する」方法論は、LLMによる文学テクストの自動要約・分析と直接連続し、「読む」とは何かという受容軸の根本的問いを生む。",
         "related_ai_phenomenon":"LLMによる文学テクスト自動分析とdistant readingの拡張"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"テクストマイニング・自然言語処理",
         "description":"distant readingは計算言語学・NLPと方法論的に連続する。"}])


add(**C, name_ja="アプター「翻訳不可能性」",
    name_en="Apter 'Untranslatability'",
    name_original="Against World Literature: On the Politics of Untranslatability",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="エミリー・アプター(1954-)『世界文学に抗して：翻訳不可能性の政治学』(2013)が展開した、世界文学論が翻訳可能性を前提とすることへの批判。バルバラ・カサン『哲学の語彙集 翻訳不可能語辞典』(2004)を理論的支柱として、翻訳の不可能性が文学・哲学の批判的契機として持つ意義を擁護した。",
    background="2000年代後半世界文学論（ダムロッシュ・カサノヴァ）の流通主義的接近への批判的応答。",
    development="ヴェノーティの異化論、コーエン『コモンズの翻訳』、現代翻訳論の倫理学的転回まで影響を及ぼす。",
    historical_context="2010年代の世界文学論の批判的脱構築期。",
    primary_source_url="https://www.versobooks.com/books/1391-against-world-literature",
    primary_source_type="Verso Books: Against World Literature",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"翻訳不可能性の政治的・哲学的擁護は、AI翻訳が「すべては翻訳可能」という幻想を技術的に強化する時代に、文学・哲学の固有性を擁護する第四変容の中核論点となる。",
         "related_ai_phenomenon":"AI翻訳の万能化と翻訳不可能性の倫理的擁護の対立"},
        {"axis":"言語","status":"rethinking",
         "rationale":"言語の翻訳不可能性は、AIが言語を確率分布として平準化する時代に、各言語固有の概念世界の擁護として再定義される。",
         "related_ai_phenomenon":"LLMの言語平準化と各言語固有性の問題"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"翻訳不可能語（カサン）",
         "description":"バルバラ・カサンの哲学翻訳不可能語辞典は哲学DB翻訳論項目と直接接続。"}])


add(**C, name_ja="ディモック「deep time」",
    name_en="Dimock 'deep time'",
    name_original="deep time",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ワイ・チー・ディモック(1953-)『他大陸を通って：アメリカ文学の深い時間』(2006)が地質学から借用した概念で、文学を国民国家の短い時間枠ではなく数千年単位の文化交流のスケールで読むアプローチ。アメリカ文学を仏教・イスラム・古典中国との関係で再解釈した。",
    background="2000年代世界文学論の時間的スケール拡張要求と、地質学的時間概念の人文学的転用。",
    development="ピーター・フランコパン『シルクロードの時代』、グローバル文学史的接近に影響を与え、現代エコクリティシズムの長期時間観とも結合。",
    historical_context="2000年代の世界文学論の時間軸拡張期。",
    primary_source_url=PRINCETON_UP+"hardcover/9780691118253/through-other-continents",
    primary_source_type="Princeton University Press: Through Other Continents",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"長期時間スケール",
         "description":"ブローデル「長期持続」や人類学的時間概念とディモック深い時間の接続。"}])


add(**C, name_ja="ムフティ「世界文学の起源」",
    name_en="Mufti 'Origins of World Literature'",
    name_original="Forget English! Orientalisms and World Literatures",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アーミル・ムフティ(1962-)『英語を忘れよ！：オリエンタリズムと世界文学』(2016)が、世界文学の概念がそもそも18-19世紀の英国オリエンタリズム（サー・ウィリアム・ジョーンズら）に起源を持ち、植民地的知の構造に根ざすと論じた批判的世界文学論。",
    background="サイード『オリエンタリズム』(1978)以降のポストコロニアル研究の世界文学論への適用。",
    development="スピヴァク『学問分野の死』、ヴァルコウィッツ「翻訳的」、世界文学論のポストコロニアル批判の中心的著作の一つとなる。",
    historical_context="2010年代の世界文学論のポストコロニアル批判期。",
    primary_source_url=HARVARD_UP+"9780674737044/forget-english",
    primary_source_type="Harvard University Press: Forget English!",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"オリエンタリズム",
         "description":"サイード由来のオリエンタリズム概念は人類学DBの植民地知識項目と接続。"}])


add(**C, name_ja="ヴァルコウィッツ「translingual」",
    name_en="Walkowitz 'translingual'",
    name_original="Born Translated: The Contemporary Novel in an Age of World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="レベッカ・ヴァルコウィッツ『翻訳されて生まれた：世界文学時代の現代小説』(2015)が定式化した、現代小説が初めから多言語的読者を想定して「翻訳されることを前提に」書かれているという認識。クッツェー、村上春樹、トラフィスらの現代作家が体現する文学的様式を理論化した。",
    background="2000年代以降のグローバル出版業界の構造変化（同時多言語出版の普及）と、世界文学論の現代小説への適用。",
    development="現代の「ボーン・トランスレーテッド」研究、AI翻訳時代の創作論との直接接続。",
    historical_context="グローバル出版業界の構造変化期。",
    primary_source_url="https://cup.columbia.edu/book/born-translated/9780231165945",
    primary_source_type="Columbia University Press: Born Translated",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"「翻訳されて生まれた」現代小説の概念は、AI翻訳が同時多言語生成を可能にした時代に、創作と翻訳の境界の根本的曖昧化を予示する。",
         "related_ai_phenomenon":"AI同時多言語生成とtranslingual創作の連続"},
        {"axis":"言語","status":"rethinking",
         "rationale":"翻訳前提の創作は、言語が事後的・派生的存在となる時代の文学的応答として再評価される。",
         "related_ai_phenomenon":"LLM時代の言語の派生性"}])


add(**C, name_ja="スピヴァク「Death of a Discipline」",
    name_en="Spivak 'Death of a Discipline'",
    name_original="Death of a Discipline",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ガヤトリ・チャクラヴォルティ・スピヴァク(1942-)『学問分野の死』(2003)が提唱した、比較文学を地域研究と統合し、惑星的(planetary)な責任の倫理に開かれた新しい学問分野へと変容させる宣言。グローバリゼーション批判と倫理的世界文学論を結合した。",
    background="1990年代後半-2000年代の比較文学プログラムの危機（学生数減少、地域研究との競合）への応答。",
    development="ApterやMufti等のポストコロニアル世界文学論への直接的影響、スピヴァク自身の「翻訳の政治学」(1993, 2000)と並ぶ翻訳理論的中心著作。",
    historical_context="2000年代の比較文学のグローバリゼーション期適応問題。",
    primary_source_url="https://cup.columbia.edu/book/death-of-a-discipline/9780231129459",
    primary_source_type="Columbia University Press: Death of a Discipline",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"スピヴァク「サバルタンは語れるか」",
         "description":"スピヴァク哲学・脱構築理論との直接接続。"}])


# ============================================================
# C: 翻訳論主要概念（8件）
# ============================================================
add(**C, name_ja="忠実 vs 適応", name_en="fidelity vs adaptation",
    name_original="fidelity / adaptation",
    period_key="比較文学形成期",
    definition="翻訳論の最古の方法論的対立。「忠実」(fidelity)は出発テクストへの厳密な対応を、「適応」(adaptation)は目標読者・目標文化への合致を優先する立場。古代キケロ・聖ヒエロニムスから現代に至る翻訳実践の根本的緊張を構造化する。",
    background="紀元前1世紀キケロ「最善の弁論術について」、4世紀聖ヒエロニムス「最善の翻訳法について」(De optimo genere interpretandi)で初めて理論化された対立。",
    development="ルター訳聖書(1522)、近代国民語文学翻訳、現代の機能主義翻訳学（フェアメール「スコポス理論」）まで、翻訳論の基底的対立として継続。",
    historical_context="古代から現代までの翻訳実践の方法論的二極。",
    primary_source_url=WIKI_EN+"Translation",
    primary_source_type="Wikipedia: Translation (academic, historical section)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"AIニューラル翻訳は「忠実」と「適応」を統計的最適化のパラメータとして機械化し、人間翻訳者の倫理的選択としての両者の対立構造を変容させる。",
         "related_ai_phenomenon":"NMTにおける忠実-適応パラメータの機械化"}])


add(**C, name_ja="sense-for-sense vs word-for-word",
    name_en="sense-for-sense vs word-for-word",
    name_original="sensum de sensu / verbum e verbo",
    period_key="比較文学形成期",
    definition="聖ヒエロニムスが385年書簡「最善の翻訳法について」(Letter 57 to Pammachius)で定式化した、語義的(verbum e verbo)翻訳と意味的(sensum de sensu)翻訳の対立。聖典翻訳のみは語義的、その他は意味的に行うべきと主張し、西洋翻訳論の基礎用語となった。",
    background="4世紀ローマ帝国でのヘブライ語・ギリシア語からラテン語への聖書翻訳実践と、キケロの先行的翻訳論の継承。",
    development="ルネサンス・宗教改革期の聖書翻訳論、ジョン・ドライデン三分類（metaphrase/paraphrase/imitation, 1680）、現代の直訳/意訳論まで継承。",
    historical_context="後期古代の聖書翻訳の理論的基礎づけ。",
    primary_source_url=WIKI_EN+"Translation_studies#History",
    primary_source_type="Wikipedia: Translation studies — History",
    importance_score=4, source_tier="primary", canonical_in_region="core")


add(**C, name_ja="文化翻訳", name_en="cultural translation",
    name_original="cultural translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="言語間の翻訳を、より広い文化間の意味の移動・変容として捉える概念。タラル・アサド「英国社会人類学における文化翻訳概念」(1986)が人類学的に定式化し、ホミ・バーバ『文化の場所』(1994)がポストコロニアル理論で展開、翻訳学・人類学・カルチュラル・スタディーズに横断する基礎概念となった。",
    background="人類学のクリフォード・ギアツ「厚い記述」と、ポストコロニアル理論の文化的混淆性議論の合流。",
    development="現代の翻訳の社会学・文化的転回（Bassnett & Lefevere 1990）、ホールの「翻訳的アイデンティティ」概念に継承。",
    historical_context="1980-90年代カルチュラル・スタディーズの興隆期。",
    primary_source_url=WIKI_EN+"Cultural_translation",
    primary_source_type="Wikipedia: Cultural translation (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化翻訳（アサド）",
         "description":"人類学DBのアサド・文化翻訳項目と直接重複する横断概念。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"文化的混淆性（バーバ）",
         "description":"バーバのポストコロニアル理論との哲学的接続。"}])


add(**C, name_ja="翻訳の非同一性", name_en="non-equivalence in translation",
    name_original="non-equivalence",
    period_key="構造主義・記述的翻訳学期",
    definition="翻訳において、出発テクストと目標テクストの完全な意味的等価が原理的に達成不可能であるという認識。モナ・ベイカー『他言語の言葉で：翻訳教程』(1992)が体系化し、語彙的・文法的・テクスト的・語用論的諸レベルでの非同一性を分類した。",
    background="ナイダ「機能的等価」(1964)以降の等価論と、ヴェノーティ・ベルマンらの差異重視翻訳論の合流。",
    development="現代翻訳教育の標準カリキュラム、AI翻訳評価における不可避の差異の問題まで継承。",
    historical_context="1990年代の翻訳学の差異重視転回。",
    primary_source_url=ROUTLEDGE+"In-Other-Words-A-Coursebook-on-Translation/Baker/p/book/9780415467544",
    primary_source_type="Routledge: In Other Words (Baker)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")


add(**C, name_ja="foreignization vs domestication",
    name_en="foreignization vs domestication",
    name_original="foreignization / domestication",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ローレンス・ヴェノーティ『翻訳者の不可視性：翻訳の歴史』(1995)が定式化した、翻訳の二大戦略の対立。「異化」(foreignization)は出発文化の異質性を保存し、「同化」(domestication)は目標文化に馴染ませる。シュライエルマッハー1813年講演に淵源を持つ。",
    background="フリードリヒ・シュライエルマッハー「翻訳のさまざまな方法について」(1813)の二分法（読者を作者へ / 作者を読者へ）の現代的再定式化。",
    development="ベルマン「他者の試練」(1985)、現代の倫理的翻訳論まで影響、ポストコロニアル翻訳論の中心的方法論的概念となった。",
    historical_context="1990年代翻訳学の倫理的転回。",
    primary_source_url=WIKI_EN+"Foreignization_and_domestication",
    primary_source_type="Wikipedia: Foreignization and domestication (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"AI翻訳は統計的に最も流暢な目標言語表現を選好するため、構造的に「同化」に偏る傾向があり、ヴェノーティが擁護した「異化」の倫理的選択肢が機械翻訳時代に新しい意義を獲得する。",
         "related_ai_phenomenon":"AI翻訳の同化傾向と異化擁護の倫理的問題"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"異化が出発文化の「他者性の真正性」を擁護する立場として、AI翻訳の流暢性に対する批判的概念枠組みを提供する。",
         "related_ai_phenomenon":"AI翻訳における他者性の真正性問題"}])


add(**C, name_ja="翻訳記号論", name_en="semiotic translation",
    name_original="semiotic translation",
    period_key="構造主義・記述的翻訳学期",
    definition="ロマン・ヤコブソン「翻訳の言語学的諸側面について」(1959)が定式化した、翻訳を記号体系内・記号体系間の意味移動と捉える接近。言語内翻訳（intralingual）・言語間翻訳（interlingual）・記号間翻訳（intersemiotic）の三分類を提示し、翻訳概念を記号論的に拡張した。",
    background="プラーグ言語学派・ロシア・フォルマリズムの構造主義言語学伝統と、パース記号論の翻訳学的応用。",
    development="ウンベルト・エーコ『記号論と言語哲学』『ほぼ同じことを言う：翻訳の経験』(2003)、現代のマルチモーダル翻訳学まで継承。",
    historical_context="戦後構造主義言語学の翻訳学への影響。",
    primary_source_url=WIKI_EN+"On_Linguistic_Aspects_of_Translation",
    primary_source_type="Wikipedia: On Linguistic Aspects of Translation",
    importance_score=5, source_tier="primary", canonical_in_region="core")


add(**C, name_ja="翻訳のパラドックス", name_en="paradox of translation",
    name_original="paradox of translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="翻訳は不可能であると同時に常に行われているという理論的パラドックス。クワイン「翻訳の不確定性」(1960)、デリダ「翻訳と存在の問い」、リクール『翻訳について』(2004)等が哲学的に展開した、翻訳実践と翻訳論的不可能性の同居の問題。",
    background="20世紀分析哲学（クワイン）と大陸哲学（デリダ・リクール）の翻訳論的問題意識の合流。",
    development="現代翻訳哲学の中心テーマ、アプター翻訳不可能性論の哲学的基盤、翻訳の倫理学的議論の理論的支柱となった。",
    historical_context="20世紀後半の言語哲学・翻訳哲学の発展。",
    primary_source_url=ROUTLEDGE+"On-Translation/Ricoeur/p/book/9780415357791",
    primary_source_type="Routledge: On Translation (Ricoeur)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"翻訳のパラドックスは、AI翻訳が「不可能であるはずの完全翻訳」を統計的に達成しているように見える時代に、不可能性の概念自体の哲学的再定義を要請する。",
         "related_ai_phenomenon":"AI翻訳と不可能性概念の再定義"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"翻訳の不確定性（クワイン）",
         "description":"クワイン分析哲学・リクール解釈学の翻訳論との哲学的接続。"}])


add(**C, name_ja="翻訳としての創作", name_en="creation as translation",
    name_original="creation as translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="文学的創作を、内的感覚・経験・先行テクストの「翻訳」として捉える理論。オクタビオ・パス『翻訳：文学と文学性』(1971)、ホルヘ・ルイス・ボルヘス「翻訳者ども」、ヴァルコウィッツ「ボーン・トランスレーテッド」が体現する、創作と翻訳の境界の根源的曖昧化。",
    background="ロマン主義翻訳論（シュレーゲル、ノヴァーリス「翻訳の三段階」）の現代的継承と、ラテンアメリカ・ブームの翻訳実践（ボルヘス・コルタサル）の理論化。",
    development="現代翻訳学のクリエイティブ・トランスレーション、AI翻訳と創作の境界問題まで継承。",
    historical_context="20世紀後半ラテンアメリカ・ブーム期の翻訳実践と理論化。",
    primary_source_url=WIKI_EN+"Octavio_Paz",
    primary_source_type="Wikipedia: Octavio Paz (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"創作と翻訳の境界の曖昧性は、AI翻訳が同時にAI創作でもあり得る時代に、「創造性」の伝統的人間中心定義を根本的に再検討する契機となる。",
         "related_ai_phenomenon":"AI創作と翻訳の境界の構造的曖昧化"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"翻訳を創作と捉える立場は、AI翻訳・AI創作における作者性の再定義に直接的理論基盤を提供する。",
         "related_ai_phenomenon":"AI時代の作者性概念の解体"}])


# ============================================================
# D: 主要理論家概念（8件）
# ============================================================
add(**C, name_ja="ベンヤミン「翻訳者の使命」",
    name_en="Benjamin 'The Task of the Translator'",
    name_original="Die Aufgabe des Übersetzers",
    period_key="比較文学形成期",
    definition="ヴァルター・ベンヤミン(1892-1940)が1923年ボードレール『パリ風景』独訳序文として執筆した翻訳論。翻訳は出発テクストの「来世」(Überleben)であり、「純粋言語」(reine Sprache)の啓示を目指すとし、翻訳の存在論的・神学的次元を提示した、20世紀翻訳論の最重要文献の一つ。",
    background="ロマン主義翻訳論（フンボルト、シュライエルマッハー）とユダヤ神秘主義カバラ的言語観の合流。",
    development="ジャック・デリダ「タワー・オブ・バベル」(1985)、ポール・ド・マン「結論：『翻訳者の使命』」(1986)が脱構築的に展開、現代翻訳哲学の理論的中心となる。",
    historical_context="1920年代ヴァイマル期ドイツの言語哲学・神学的思考の合流期。",
    primary_source_url=WIKI_EN+"The_Task_of_the_Translator",
    primary_source_type="Wikipedia: The Task of the Translator (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"ベンヤミンの「翻訳は原作の来世」「純粋言語の啓示」という存在論的翻訳観は、AI翻訳の機能主義的・効率主義的接近に対する根本的対抗概念として再活性化される。",
         "related_ai_phenomenon":"AI翻訳の機能主義に対するベンヤミン的存在論の再評価"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ベンヤミン言語哲学",
         "description":"哲学DBのベンヤミン項目と直接重複、神学・言語哲学的接続。"}])


add(**C, name_ja="ヤコブソン「翻訳の3つの種類」",
    name_en="Jakobson 'three types of translation'",
    name_original="three types of translation",
    period_key="構造主義・記述的翻訳学期",
    definition="ロマン・ヤコブソン(1896-1982)が1959年「翻訳の言語学的諸側面について」で提示した翻訳の三分類。①言語内翻訳（intralingual translation, 同一言語内の言い換え）、②言語間翻訳（interlingual translation, 異言語間翻訳本来）、③記号間翻訳（intersemiotic translation, 記号体系間の翻案）。翻訳概念の記号論的拡張として現代翻訳学の出発点となった。",
    background="プラーグ学派構造主義言語学とパース記号論の総合。",
    development="ウンベルト・エーコ翻訳論、現代マルチモーダル翻訳学、適応研究（adaptation studies）まで影響。",
    historical_context="戦後構造主義言語学の制度的展開期。",
    primary_source_url=WIKI_EN+"On_Linguistic_Aspects_of_Translation",
    primary_source_type="Wikipedia: On Linguistic Aspects of Translation",
    importance_score=5, source_tier="primary", canonical_in_region="core")


add(**C, name_ja="ナイダ「機能的等価」", name_en="Nida 'functional equivalence'",
    name_original="functional equivalence / dynamic equivalence",
    period_key="構造主義・記述的翻訳学期",
    definition="ユージン・ナイダ(1914-2011)が『翻訳の科学にむけて』(1964)で定式化した翻訳論。出発テクストの形式的等価(formal equivalence)ではなく、目標読者に出発テクストの読者と等価の効果を生じさせる「動的等価」(dynamic equivalence)、後に「機能的等価」と呼び換えられた接近を擁護した。米国聖書協会の翻訳実践に立脚。",
    background="米国聖書協会(ABS)の世界各国語聖書翻訳プロジェクトと、チョムスキー生成文法の翻訳学的応用。",
    development="フェアメール・ライス「スコポス理論」(1984)に継承される機能主義翻訳学の系譜の出発点。批判（ヴェノーティ等）も多いが現代翻訳教育の基礎概念。",
    historical_context="戦後米国の聖書翻訳実践と言語学的理論化の合流。",
    primary_source_url=WIKI_EN+"Dynamic_and_formal_equivalence",
    primary_source_type="Wikipedia: Dynamic and formal equivalence (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


add(**C, name_ja="ヴェノーティ「翻訳者の不可視性」",
    name_en="Venuti 'translator's invisibility'",
    name_original="The Translator's Invisibility",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ローレンス・ヴェノーティ(1953-)『翻訳者の不可視性：翻訳の歴史』(1995)が告発した、英語圏出版業界において翻訳者が「流暢な」(fluent)目標テクストを生産し、翻訳の存在を消去する慣行。これに対抗する「異化」(foreignization)戦略を擁護した、現代翻訳論の中心著作。",
    background="1990年代英米ポストコロニアル研究と翻訳学の合流期。",
    development="現代の翻訳者の権利運動、文学翻訳者協会の活動、翻訳の倫理的転回まで影響、AI翻訳時代の翻訳者の役割問題にも直接接続。",
    historical_context="1990年代の翻訳の文化的・政治的転回期。",
    primary_source_url=ROUTLEDGE+"The-Translators-Invisibility-A-History-of-Translation/Venuti/p/book/9780415394550",
    primary_source_type="Routledge: The Translator's Invisibility",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"翻訳者の不可視性問題は、AI翻訳の普及で翻訳者そのものが構造的に不可視化される時代に、「誰が翻訳しているか」という作者性問題の根本的再考を要請する。",
         "related_ai_phenomenon":"AI翻訳における翻訳者主体の構造的消去"}])


add(**C, name_ja="ベルマン「他者の試練」",
    name_en="Berman 'L'épreuve de l'étranger'",
    name_original="L'épreuve de l'étranger",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アントワーヌ・ベルマン(1942-1991)『他者の試練：ロマン主義ドイツの文化と翻訳』(1984)が定式化した、翻訳をテクストが「他者性の試練」を経る経験として捉える理論。「翻訳の解析学」(analytique de la traduction)で、目標テクストの12種類の変形傾向（合理化・明晰化・拡張等）を分類した。",
    background="ドイツ・ロマン主義翻訳論（シュライエルマッハー、ヘルダー、フンボルト）の現代的再評価と、ヴェノーティ異化論の理論的源泉。",
    development="現代の倫理的翻訳論、文学翻訳実践教育、ヴェノーティ・スピヴァク・アプターらに継承。",
    historical_context="1980年代フランス翻訳学の倫理的・哲学的展開期。",
    primary_source_url=WIKI_EN+"Antoine_Berman",
    primary_source_type="Wikipedia: Antoine Berman (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ベルマンが翻訳の本質的「他者性の試練」と捉えた経験は、AI翻訳が他者性を統計的に均質化する傾向に対する倫理的対抗概念として再評価される。",
         "related_ai_phenomenon":"AI翻訳における他者性経験の希薄化"}])


add(**C, name_ja="バスネット「翻訳学」", name_en="Bassnett 'Translation Studies'",
    name_original="Translation Studies",
    period_key="構造主義・記述的翻訳学期",
    definition="スーザン・バスネット(1945-)『翻訳学』(1980, 第3版2002, 第4版2014)が制度的に確立した独立学問分野としての翻訳学(Translation Studies)。1990年代「翻訳の文化的転回」(Bassnett & Lefevere 1990)を主導し、翻訳学を文学研究・カルチュラル・スタディーズと統合する方向性を提示した。",
    background="1972年ジェイムズ・ホームズ「翻訳学の名と性質」での学問分野命名と、1980年代英米における翻訳学プログラムの制度化。",
    development="バスネット・ルフェーヴル編『翻訳・歴史・文化』(1990)が文化的転回を提唱、現代翻訳学の中心潮流となった。",
    historical_context="1980-90年代翻訳学の制度的成立期。",
    primary_source_url=ROUTLEDGE+"Translation-Studies/Bassnett/p/book/9780415506700",
    primary_source_type="Routledge: Translation Studies (Bassnett)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


add(**C, name_ja="エヴェン=ゾーハー", name_en="Itamar Even-Zohar",
    name_original="Itamar Even-Zohar",
    period_key="構造主義・記述的翻訳学期",
    definition="イタマル・エヴェン=ゾーハー(1939-)が確立した、文学・文化・翻訳をシステム間の動的関係として分析するテル・アヴィヴ学派の理論的中心。「ポリシステム」(polysystem)概念で翻訳文学の中央/周辺位置の決定要因を体系的に分析した。",
    background="ロシア・フォルマリズムのチィニャーノフ「文学的事実」とプラーグ学派構造主義の継承。",
    development="トゥーリ記述的翻訳学、ヘルマンス、現代の社会学的翻訳学（カサノヴァ）に直接接続。",
    historical_context="1970-80年代テル・アヴィヴ大学の翻訳学拠点形成期。",
    primary_source_url="http://www.tau.ac.il/~itamarez/works/index.html",
    primary_source_type="Tel Aviv University: Even-Zohar's collected works",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


add(**C, name_ja="トゥーリ記述的翻訳学",
    name_en="Toury's descriptive translation studies",
    name_original="Descriptive Translation Studies and Beyond",
    period_key="構造主義・記述的翻訳学期",
    definition="ギデオン・トゥーリ(1942-2016)『記述的翻訳学とそれを超えて』(1995, 改訂版2012)が体系化した、翻訳を「目標文化に存在するテクストで、何らかのかたちで翻訳とみなされるもの」と操作的に定義し、翻訳規範(translation norms)の経験的記述を方法論化した翻訳学。",
    background="ホームズ「翻訳学の名と性質」(1972)の記述的翻訳学(DTS)構想と、エヴェン=ゾーハー・ポリシステム理論の継承的展開。",
    development="現代の翻訳社会学、機械翻訳評価における翻訳規範研究、コーパス翻訳学(corpus translation studies)に継承。",
    historical_context="1990年代の翻訳学の経験的・記述的方法論の確立期。",
    primary_source_url=BENJAMINS+"btl.100",
    primary_source_type="Benjamins Translation Library: Toury 1995/2012",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# E: ポストコロニアル翻訳・現代論争（8件）
# ============================================================
add(**C, name_ja="ポストコロニアル翻訳",
    name_en="postcolonial translation",
    name_original="postcolonial translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="翻訳を植民地的権力関係・脱植民地化過程の場として理論化する翻訳論。テジャスウィニ・ニランジャナ『翻訳のサイト』(1992)、サイモン『性別と翻訳』(1996)、バスネット・トリヴェディ編『ポストコロニアル翻訳：理論と実践』(1999)が代表する、現代翻訳学の中心潮流。",
    background="サイード『オリエンタリズム』(1978)、スピヴァク「サバルタンは語れるか」(1988)以降のポストコロニアル理論の翻訳学への適用。",
    development="現代のグローバル英語論争、AI翻訳の言語的不平等問題、翻訳の倫理的転回まで影響。",
    historical_context="1990年代翻訳学のポストコロニアル転回期。",
    primary_source_url=ROUTLEDGE+"Post-Colonial-Translation-Theory-and-Practice/Bassnett-Trivedi/p/book/9780415147460",
    primary_source_type="Routledge: Post-Colonial Translation",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ポストコロニアル理論",
         "description":"人類学DBのポストコロニアル研究と直接接続する横断概念。"}])


add(**C, name_ja="翻訳と権力", name_en="translation and power",
    name_original="translation and power",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マリア・ティモッツコ&エドウィン・ゲンツラー編『翻訳と権力』(2002)が体系化した、翻訳を権力関係（植民地・性別・階級・人種）の場として捉える接近。翻訳が権力構造を再生産すると同時に抵抗の手段にもなる二重性を理論化した。",
    background="1990年代翻訳学の文化的転回・ポストコロニアル転回の総合的展開。",
    development="現代翻訳学のフェミニスト翻訳・クィア翻訳・脱植民地翻訳の理論的基盤、AI翻訳の言語覇権問題まで継承。",
    historical_context="2000年代翻訳学の政治的・倫理的転回期。",
    primary_source_url="https://www.umasspress.com/9781558493582/translation-and-power/",
    primary_source_type="UMass Press: Translation and Power (Tymoczko & Gentzler)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"翻訳と権力の関係は、AI翻訳が大手テック企業の英語ベースモデルに集約される時代に、新しい技術的言語覇権の問題として再活性化される。",
         "related_ai_phenomenon":"AI翻訳における言語的権力の集中"}])


add(**C, name_ja="不平等な交換", name_en="unequal exchange",
    name_original="unequal exchange in translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ヨハン・ハインリッヒ・ハイルブロン「翻訳の社会学：書籍翻訳の世界システム」(1999)が定式化した、世界の翻訳市場における言語間の構造的不均衡。中心言語（英語）から周辺言語への翻訳は多く、逆方向は少ないという、翻訳の世界システム的不平等を経験的に明らかにした。",
    background="ウォーラーステイン世界システム論の翻訳学的応用と、UNESCO Index Translationumのデータ分析。",
    development="サポリティ『翻訳と世界文学』(2010)、現代の翻訳社会学、グローバル英語論争の経験的基盤。",
    historical_context="2000年代翻訳学の世界システム的接近期。",
    primary_source_url=UNESCO_XTRANS,
    primary_source_type="UNESCO Index Translationum",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"世界システム論",
         "description":"ウォーラーステイン世界システム論との接続。"}])


add(**C, name_ja="グローバル英語と世界文学",
    name_en="English as world literary lingua franca",
    name_original="English as world literary lingua franca",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="20世紀後半以降、英語が世界文学の事実上の共通語となり、英訳されない作品は世界文学に参入しにくいという現代世界文学論争の中心問題。アプター『世界文学に抗して』、ムフティ『英語を忘れよ！』が批判的に問題化した。",
    background="戦後の英語のグローバル覇権と、英米出版業界の世界文学市場における中心的役割の制度化。",
    development="現代の「グローバル小説」批判、AI翻訳が英語経由翻訳に依存する技術的構造への批判まで継承。",
    historical_context="グローバリゼーション期の言語的不平等の文学的表現。",
    primary_source_url=WIKI_EN+"World_literature",
    primary_source_type="Wikipedia: World literature (academic)",
    importance_score=4, source_tier="tertiary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"英語のリンガフランカ化は、英語ベースLLMが事実上の世界翻訳ハブとなる時代に、技術的レベルで強化・制度化される新しい段階に入る。",
         "related_ai_phenomenon":"英語LLMによる言語的覇権の技術的強化"}])


add(**C, name_ja="機械翻訳と文学", name_en="machine translation and literature",
    name_original="machine translation and literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="統計的・ニューラル機械翻訳(NMT)の文学翻訳への適用可能性と限界を巡る現代の論争領域。リサ・ブルックス・ペナロサ等の研究は、文学翻訳における機械翻訳の構造的限界（韻律、文化的含意、文体的個性）を経験的に分析する一方、AI支援翻訳の実用的可能性も検証されている。",
    background="2010年代後半のニューラル機械翻訳（Google Transformer 2017）の急速な品質向上と、文学翻訳業界への波及。",
    development="2020年代AI翻訳ツール（DeepL、ChatGPT等）の文学翻訳実践への影響、出版業界の労働構造変化問題まで急速展開中。",
    historical_context="2010-20年代のAI翻訳の急速な実用化期。",
    primary_source_url=BENJAMINS+"target",
    primary_source_type="Target: International Journal of Translation Studies",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"機械翻訳の文学への適用は、翻訳という活動そのものの定義を、人間の解釈的実践から統計的最適化問題へと再定義する根本的変容をもたらす。",
         "related_ai_phenomenon":"NMTによる文学翻訳の自動化と人間翻訳の役割再定義"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"機械翻訳が文学的創造性をどの程度実現できるかという問いは、創造性概念そのものを統計的生成と区別不能にしうるかを問う。",
         "related_ai_phenomenon":"NMTにおける文学的創造性の機械化問題"},
        {"axis":"言語","status":"rethinking",
         "rationale":"機械翻訳が言語間の構造的差異を統計的に均質化する傾向は、言語多様性の文化的・認識的価値を改めて問う契機となる。",
         "related_ai_phenomenon":"NMTによる言語多様性の統計的均質化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"ニューラル機械翻訳（Transformer）",
         "description":"AI開発DBのTransformerアーキテクチャ・NMT項目と直接接続する核心横断概念。"}])


add(**C, name_ja="AIと翻訳の創造性",
    name_en="AI and translational creativity",
    name_original="AI and translational creativity",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="LLM・AI翻訳が文学翻訳の創造的・解釈的次元に与える影響を巡る、2020年代の中心的論争領域。AIが「忠実な再生産」を超えて「創造的解釈」を行いうるか、また人間翻訳者の創造性がAI翻訳との対比で如何に再定義されるかが論じられる。",
    background="2022年以降のChatGPT等LLMの一般普及と、文学翻訳業界・翻訳学界での実証的検証の本格化。",
    development="現在進行形の論争領域。文学翻訳者協会(ALTA等)の声明、AI翻訳と人間翻訳の比較実験研究、出版業界の労働問題と並走する。",
    historical_context="2022-2026年のLLM革命の翻訳学への直接的影響期。",
    primary_source_url=BENJAMINS+"target",
    primary_source_type="Target: International Journal of Translation Studies (recent issues)",
    importance_score=5, source_tier="tertiary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"AIと翻訳の創造性問題は、第四変容の中核中の中核論点。翻訳における創造性の人間中心定義そのものが、LLMの統計的「創造性」によって根本的に問い直される。",
         "related_ai_phenomenon":"LLMの統計的創造性と人間翻訳者の創造性定義の対立"},
        {"axis":"翻訳","status":"rethinking",
         "rationale":"AI翻訳の創造性は、翻訳が単なる言語変換ではなく解釈的・創造的実践であるという翻訳論の核心命題を機械的に実装する試みとして、翻訳概念自体の再定義を要請する。",
         "related_ai_phenomenon":"AI翻訳による翻訳概念の根本的拡張"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"AI翻訳における創造性の場所（プロンプト書き手・モデル開発者・モデル自体）の問いが、翻訳の作者性概念を多層化する。",
         "related_ai_phenomenon":"AI翻訳における作者性の多層化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"LLMの創造性論争",
         "description":"AI開発DBのLLM創造性研究と直接接続する第四変容核心横断概念。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"創造性の哲学",
         "description":"哲学DBの創造性概念再定義との直接接続。"}])


add(**C, name_ja="翻訳の倫理", name_en="ethics of translation",
    name_original="ethics of translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アンソニー・ピム『翻訳の倫理について』(1997, 2012)、ベルマン『翻訳とその他者の試練』、ヴェノーティ等が展開した、翻訳行為の倫理的次元を理論化する分野。出発文化への忠実、目標読者への責任、翻訳者の社会的責任、AI翻訳時代の翻訳労働の倫理等を含む。",
    background="1990年代翻訳学の文化的・政治的転回と、応用倫理学の翻訳学的応用の合流。",
    development="現代の翻訳者組合運動、AI翻訳と翻訳労働問題、機械翻訳ポストエディットの労働倫理問題まで継承・展開中。",
    historical_context="1990年代以降の翻訳学の倫理的転回。",
    primary_source_url=ROUTLEDGE+"On-Translator-Ethics-Principles-for-Mediation-Between-Cultures/Pym/p/book/9789027224552",
    primary_source_type="Routledge/Benjamins: On Translator Ethics (Pym)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"翻訳の倫理は、AI翻訳が翻訳労働と翻訳責任の所在を根本的に再編する時代に、誰が翻訳の責任を負うかという最も具体的な倫理問題として再活性化される。",
         "related_ai_phenomenon":"AI翻訳の責任主体問題と翻訳倫理の再構築"}])


add(**C, name_ja="untranslatables（カサン）",
    name_en="untranslatables (Cassin)",
    name_original="Vocabulaire européen des philosophies: Dictionnaire des intraduisibles",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="バルバラ・カサン編『ヨーロッパ哲学語彙集：翻訳不可能語辞典』(2004, 英訳2014)が提示した、各言語固有の哲学概念で他言語に完全には翻訳できない語群（独：Geist, 仏：esprit, 英：mind, 露：dushá等）の体系的整理。アプター翻訳不可能性論の理論的源泉。",
    background="フランス哲学のドイツ・英米哲学翻訳経験と、ヨーロッパ統合期の哲学的多言語性問題の交差。",
    development="アプター『世界文学に抗して』(2013)が翻訳学的に展開、現代の哲学翻訳学・概念翻訳学の中心著作となった。",
    historical_context="2000年代ヨーロッパ統合期の哲学的多言語性問題。",
    primary_source_url=PRINCETON_UP+"hardcover/9780691138701/dictionary-of-untranslatables",
    primary_source_type="Princeton University Press: Dictionary of Untranslatables",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"翻訳不可能語のカタログ化は、AI翻訳が「すべて翻訳可能」という前提で動作することへの根本的批判の理論的基盤となる。「不可能性のオントロジー」の擁護。",
         "related_ai_phenomenon":"AI翻訳の万能性前提と不可能性オントロジーの対立"},
        {"axis":"言語","status":"rethinking",
         "rationale":"各言語固有の概念世界の擁護は、LLMが言語を確率分布として平準化する時代に、言語の存在論的固有性を擁護する論拠として再評価される。",
         "related_ai_phenomenon":"LLMの言語平準化と言語固有性の擁護"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"哲学翻訳不可能語",
         "description":"哲学DBのカサン編集翻訳不可能語辞典項目と直接重複する核心横断概念。"}])


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="理論",
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
        print(f"[c38] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c38] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
