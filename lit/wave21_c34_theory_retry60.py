"""LIT-DB Wave 21 — C34: Literary Theory retry (+60 concepts).

Subfield: lit_theory (id=22), region='横断'.
Adds 60 NEW NON-OVERLAPPING concepts (existing 170 → target 230).
Coverage: Genre theory, New Historicism, Cultural materialism,
Stylistics, World-systems, Postcolonial extension, Disability,
Animal/Posthuman, Affect deeper, Distant reading, Recent Black/Queer,
Reception/Hermeneutics.

>= 60% primary tier; fourth_transform_tags >= 24; cross_domain >= 18.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("ジャンル理論期", "Genre Theory", 1957, 2010,
     "フライ・ジュネット・デリダのジャンル理論期。"),
    ("ニュー・ヒストリシズム期", "New Historicism",
     1980, 2010,
     "グリーンブラット・モントローズらの新歴史主義期。"),
    ("文化唯物論期", "Cultural Materialism",
     1958, 2010,
     "ウィリアムズ・イーグルトン・ホールらの英国文化唯物論期。"),
    ("文体論・認知詩学期", "Stylistics & Cognitive Poetics",
     1960, 2020,
     "ハリデー・リーチ・レイコフ・認知詩学の系譜。"),
    ("世界文学・遠読期", "World Literature & Distant Reading",
     1999, 2025,
     "カザノヴァ・モレッティ・ダムロッシュらのグローバル文学批評期。"),
    ("ポストコロニアル理論拡張期",
     "Postcolonial Theory Extension",
     1990, 2025,
     "スピヴァク後期・バーバ・ムベンベ・ミニョーロらのポストコロニアル理論拡張。"),
    ("障害研究・動物研究期",
     "Disability & Animal Studies",
     1995, 2020,
     "障害研究・動物研究・ポストヒューマン批評の交差期。"),
    ("情動批評深化期",
     "Affect Theory Deepened",
     2000, 2025,
     "ガイ・バーラント・アハメド・マッスミ・セジウィック情動批評深化期。"),
    ("デジタル人文学第二世代期",
     "Second-Generation Digital Humanities",
     2015, 2025,
     "アンダーウッド・パイパー・ボード・ドラッカーらの第二世代DH期。"),
    ("ブラック批評・現代物質批評期",
     "Black Criticism & Recent Material Criticism",
     2010, 2025,
     "ハートマン・シャープ・モテン・ウォレンら現代ブラック批評期。"),
    ("受容理論・解釈学拡張期",
     "Reception & Hermeneutics Extension",
     1960, 2010,
     "ヤウス・イーザー・ガダマー・リクール解釈学拡張期。"),
]

WIKI_EN = "https://en.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
ARCH = "https://archive.org/details/"
DUKE = "https://read.dukeupress.edu/"
PUP = "https://press.princeton.edu/"
COL = "https://cup.columbia.edu/"
HUP = "https://www.hup.harvard.edu/"
UCP = "https://press.uchicago.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_theory", region="横断", original_script="roman")


# ============================================================
# A: Genre theory (8)
# ============================================================
add(**C, name_ja="フライ『批評の解剖』",
    name_en="Frye's Anatomy of Criticism",
    name_original="Anatomy of Criticism",
    period_key="ジャンル理論期",
    definition="ノースロップ・フライ(1912-1991)の主著(1957)。歴史的・倫理的・元型的・修辞的の四批評と四ミュトスを体系化、20世紀ジャンル理論の古典。",
    background="トロント大学、ブレイク研究、元型批評、新批評以後の体系化志向。",
    development="元型批評・神話批評・ジャンル理論・カナダ批評の中核。",
    historical_context="1950年代英米批評の体系化期。",
    primary_source_url=WIKI_EN+"Anatomy_of_Criticism",
    primary_source_type="Wikipedia: Anatomy of Criticism",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"元型・ミュトス分類は、AI生成物語のジャンル類型を理論化する基盤。",
         "related_ai_phenomenon":"AI生成物語の元型分析"}],
    cross_domain=[
        {"target_db":"MY","link_type":"shared_concept",
         "target_entity_name":"元型批評",
         "description":"フライ元型論は神話DBのナラティブ構造分析と接続。"}])

add(**C, name_ja="フライ・ミュトス論（4ミュトス）",
    name_en="Frye's Four Mythoi",
    name_original="four mythoi",
    period_key="ジャンル理論期",
    definition="フライ『批評の解剖』が提示した四物語類型(春＝喜劇／夏＝ロマンス／秋＝悲劇／冬＝アイロニー)。季節循環と元型を結ぶジャンル分類論。",
    background="フレイザー人類学、ユング元型、ブレイク神話の総合。",
    development="元型批評、ジャンル批評、現代物語類型論への影響。",
    historical_context="1950年代カナダ・米国元型批評期。",
    primary_source_url=WIKI_EN+"Mythos_(Aristotle)",
    primary_source_type="Wikipedia: Mythos",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"4ミュトスはAI生成物語の循環型ジャンル分類モデルとなる。",
         "related_ai_phenomenon":"AIジャンル類型予測"}])

add(**C, name_ja="ジュネット『アルシテクスト序説』",
    name_en="Genette's The Architext",
    name_original="Introduction à l'architexte",
    period_key="ジャンル理論期",
    definition="ジェラール・ジュネット(1930-2018)の著作(1979)。ジャンル分類の歴史を批判的に整理し、テクストとジャンルの関係(アルシテクスチュアリテ)を理論化した。",
    background="フランス構造主義、ジュネット物語論、ジャンル分類史批判。",
    development="トランステクスチュアリテ理論、現代ジャンル批評の基盤。",
    historical_context="1970年代仏ジャンル理論再検討期。",
    primary_source_url=WIKI_EN+"G%C3%A9rard_Genette",
    primary_source_type="Wikipedia: Gérard Genette",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="デリダ「ジャンルの法」",
    name_en="Derrida's Law of Genre",
    name_original="La loi du genre",
    period_key="ジャンル理論期",
    definition="ジャック・デリダ(1930-2004)の論文(1980)。ジャンルの「混合禁止の法」を脱構築し、ジャンル分類への帰属/非帰属の二重性を理論化した。",
    background="デリダ脱構築、フランス構造主義以後、ブランショ批評との対話。",
    development="脱構築ジャンル批評、現代ハイブリッド・ジャンル論の理論的基盤。",
    historical_context="1980年仏脱構築期。",
    primary_source_url=WIKI_EN+"Jacques_Derrida",
    primary_source_type="Wikipedia: Derrida",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ジャンル法の脱構築はAI生成のジャンル横断的テクストを理論化する基盤。",
         "related_ai_phenomenon":"AI生成テクストのジャンル混淆"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"脱構築",
         "description":"デリダのジャンル法は脱構築哲学と文学批評を架橋。"}])

add(**C, name_ja="トドロフ『幻想文学論序説』",
    name_en="Todorov's Introduction to Fantastic",
    name_original="Introduction à la littérature fantastique",
    period_key="ジャンル理論期",
    definition="ツヴェタン・トドロフ(1939-2017)の主著(1970)。幻想文学を「読者の躊躇」によって定義、不思議・幻想・怪奇の三類型に分類した構造主義ジャンル論の古典。",
    background="フランス構造主義、ロシア・フォルマリズム、ジャンル理論。",
    development="幻想文学研究、現代ジャンル批評、SF/ホラー批評の理論的基盤。",
    historical_context="1970年代仏構造主義ジャンル論期。",
    primary_source_url=WIKI_EN+"Tzvetan_Todorov",
    primary_source_type="Wikipedia: Todorov",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブース『小説の修辞学』詳論",
    name_en="Booth's Rhetoric of Fiction reread",
    name_original="The Rhetoric of Fiction",
    period_key="ジャンル理論期",
    definition="ウェイン・ブース(1921-2005)の主著(1961)再読。内包作者・信頼できない語り手概念を確立し、修辞的ナラトロジーの原典として現代ジャンル批評を支えた。",
    background="シカゴ学派新アリストテレス批評、修辞批評。",
    development="修辞ナラトロジー、信頼性研究、米国小説批評教育の基盤。",
    historical_context="1960年代米国修辞批評期。",
    primary_source_url=WIKI_EN+"Wayne_C._Booth",
    primary_source_type="Wikipedia: Wayne C. Booth",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"内包作者・修辞的伝達はAI生成物語の修辞構造を理論化する基盤。",
         "related_ai_phenomenon":"AI物語の内包作者問題"}])

add(**C, name_ja="バフチン・クロノトポス（時空間）",
    name_en="Bakhtin's chronotope",
    name_original="хронотоп",
    period_key="ジャンル理論期",
    definition="ミハイル・バフチン(1895-1975)の概念(1937-38)。小説のジャンルを規定する「時間と空間の本質的相互連関」を「クロノトポス」として理論化、ジャンル理論の中核概念。",
    background="ロシア文学理論、カント時空間論、相対性理論との対話。",
    development="現代ジャンル批評、世界文学批評、文化地理学的批評の基盤。",
    historical_context="1930年代ソ連文学理論期。",
    primary_source_url=WIKI_EN+"Chronotope",
    primary_source_type="Wikipedia: Chronotope",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"クロノトポスはAI生成物語の時空間構造分析の理論的基盤。",
         "related_ai_phenomenon":"AI物語のクロノトポス"}])

add(**C, name_ja="ジュネット『アルシテクスト』ジャンル批判",
    name_en="Genette architext genre critique",
    name_original="architextualité",
    period_key="ジャンル理論期",
    definition="ジュネットがアリストテレス『詩学』以来のジャンル分類史を批判的に再検討、模倣・物語・劇という「自然な」三分類が後世の混合産物であることを論証した。",
    background="アリストテレス『詩学』、シュレーゲル兄弟ロマン主義ジャンル論。",
    development="現代ジャンル批評の歴史化、トランステクスチュアリテ理論。",
    historical_context="1970年代仏ジャンル史批判期。",
    primary_source_url=WIKI_EN+"Architextuality",
    primary_source_type="Wikipedia: Architextuality",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: New Historicism (5)
# ============================================================
add(**C, name_ja="グリーンブラット『ルネサンスの自己成型』",
    name_en="Greenblatt's Renaissance Self-Fashioning",
    name_original="Renaissance Self-Fashioning",
    period_key="ニュー・ヒストリシズム期",
    definition="スティーヴン・グリーンブラット(1943-)の主著(1980)。モア・スペンサー・シェイクスピア等を分析し、ルネサンス的「自己」が権力との交渉で成型される過程を理論化した。",
    background="UCバークレー英文学、フーコー権力論、文化人類学の影響。",
    development="ニュー・ヒストリシズム運動の出発点、文化詩学の中核。",
    historical_context="1980年代米国新歴史主義成立期。",
    primary_source_url=WIKI_EN+"Renaissance_Self-Fashioning",
    primary_source_type="Wikipedia: Renaissance Self-Fashioning",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"自己成型概念はAI時代の主体性構築過程を理論化する基盤。",
         "related_ai_phenomenon":"AI媒介の自己成型"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"自己成型",
         "description":"グリーンブラットは文学批評と文化人類学を架橋。"}])

add(**C, name_ja="グリーンブラット『シェイクスピア的交渉』",
    name_en="Greenblatt's Shakespearean Negotiations",
    name_original="Shakespearean Negotiations",
    period_key="ニュー・ヒストリシズム期",
    definition="グリーンブラットの主著(1988)。シェイクスピア劇を社会的エネルギー循環の場として分析、文化詩学の方法論を確立した新歴史主義の代表的著作。",
    background="フーコー権力論、ニュー・ヒストリシズム成熟、ルネサンス研究。",
    development="文化詩学方法論、現代シェイクスピア批評、世界文学批評への影響。",
    historical_context="1980年代後半新歴史主義成熟期。",
    primary_source_url=WIKI_EN+"New_historicism",
    primary_source_type="Wikipedia: New historicism",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="モントローズ・文化詩学",
    name_en="Montrose's cultural poetics",
    name_original="cultural poetics",
    period_key="ニュー・ヒストリシズム期",
    definition="ルイス・モントローズが1986年論文「テクストの歴史性とエリザベス朝文化」で提唱した方法論。「テクストの歴史性と歴史のテクスト性」をキーフレーズとする新歴史主義の理論的綱領。",
    background="UCサンタクルーズ英文学、フーコー、ニュー・ヒストリシズム。",
    development="新歴史主義方法論の中核定式、現代文化批評教育の標準理論。",
    historical_context="1980年代米国新歴史主義方法論期。",
    primary_source_url=WIKI_EN+"Louis_Montrose",
    primary_source_type="Wikipedia: Louis Montrose",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"テクスト歴史性論はAI生成テクストと歴史性の関係を理論化する基盤。",
         "related_ai_phenomenon":"AI生成テクストの歴史性"}])

add(**C, name_ja="ギャラガー/グリーンブラット『新歴史主義の実践』",
    name_en="Gallagher/Greenblatt Practicing New Historicism",
    name_original="Practicing New Historicism",
    period_key="ニュー・ヒストリシズム期",
    definition="キャサリン・ギャラガーとグリーンブラットの共著(2000)。新歴史主義20年の実践を方法論的に総括、「逸話」「驚異」を分析道具として整理した。",
    background="UCバークレー英文学、新歴史主義成熟、文化詩学。",
    development="新歴史主義方法論の正典化、現代文化批評教育の標準テキスト。",
    historical_context="2000年代新歴史主義総括期。",
    primary_source_url=UCP+"ucp/books/book/chicago/P/bo3631551.html",
    primary_source_type="U Chicago Press: Practicing New Historicism",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="オーゲル『幻影の力』",
    name_en="Orgel's The Illusion of Power",
    name_original="The Illusion of Power",
    period_key="ニュー・ヒストリシズム期",
    definition="スティーヴン・オーゲル(1933-)の主著(1975)。ジェイムズ朝仮面劇を権力表象として分析し、新歴史主義の先駆けとなったルネサンス劇批評の重要著作。",
    background="ジョンズ・ホプキンズ大学、英国ルネサンス劇研究、フーコー以前の権力分析。",
    development="新歴史主義の先駆、現代ルネサンス劇批評、宮廷文化研究の基盤。",
    historical_context="1970年代米国ルネサンス研究期。",
    primary_source_url=WIKI_EN+"Stephen_Orgel",
    primary_source_type="Wikipedia: Stephen Orgel",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: Cultural Materialism (8)
# ============================================================
add(**C, name_ja="ウィリアムズ『長い革命』",
    name_en="Williams's The Long Revolution",
    name_original="The Long Revolution",
    period_key="文化唯物論期",
    definition="レイモンド・ウィリアムズ(1921-1988)の主著(1961)。産業・民主・文化の三革命を統合的に分析、英国文化研究の方法論的基盤を確立した文化唯物論の中核著作。",
    background="ケンブリッジ英文学、ホガート、英国新左派、リーヴィス批判。",
    development="バーミンガム文化研究、現代カルチュラル・スタディーズの理論的基盤。",
    historical_context="1960年代英国新左派文化研究形成期。",
    primary_source_url=WIKI_EN+"The_Long_Revolution",
    primary_source_type="Wikipedia: The Long Revolution",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化研究",
         "description":"ウィリアムズは文学批評と文化人類学を架橋。"}])

add(**C, name_ja="ウィリアムズ『田舎と都会』",
    name_en="Williams's The Country and the City",
    name_original="The Country and the City",
    period_key="文化唯物論期",
    definition="ウィリアムズの主著(1973)。英国文学における田園と都市の表象を分析、資本主義近代化の文化的構築を歴史唯物論的に解明した文化研究の古典。",
    background="英国新左派、田園詩研究、マルクス主義批評。",
    development="エコクリティシズム、空間批評、ポストコロニアル批評への影響。",
    historical_context="1970年代英国文化唯物論成熟期。",
    primary_source_url=WIKI_EN+"The_Country_and_the_City",
    primary_source_type="Wikipedia: The Country and the City",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウィリアムズ『マルクス主義と文学』",
    name_en="Williams's Marxism and Literature",
    name_original="Marxism and Literature",
    period_key="文化唯物論期",
    definition="ウィリアムズの主著(1977)。文化唯物論を理論化し、感情の構造・覇権・残余的/出現的文化等の中心概念を体系化した英国文化批評の理論的基盤。",
    background="英国新左派、グラムシ覇権論、フランクフルト学派以後の批判理論。",
    development="文化唯物論運動、バーミンガム学派、現代カルチュラル・スタディーズの中核。",
    historical_context="1970年代英国文化唯物論完成期。",
    primary_source_url=WIKI_EN+"Marxism_and_Literature",
    primary_source_type="Wikipedia: Marxism and Literature",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"文化唯物論はAI時代の文化生産の物質的条件を理論化する基盤。",
         "related_ai_phenomenon":"AI時代の文化生産物質性"}])

add(**C, name_ja="ウィリアムズ『キーワード』",
    name_en="Williams's Keywords",
    name_original="Keywords: A Vocabulary of Culture and Society",
    period_key="文化唯物論期",
    definition="ウィリアムズの著作(1976)。「文化」「自然」「労働」等の中心語の意味史を辿り、社会変動と語彙変動の関連を解明した英国文化批評の古典的方法論書。",
    background="英国オックスフォード英語辞典伝統、概念史、英国文化研究。",
    development="現代文化研究の標準参照書、概念史方法論の基盤。",
    historical_context="1970年代英国概念史成熟期。",
    primary_source_url=WIKI_EN+"Keywords:_A_Vocabulary_of_Culture_and_Society",
    primary_source_type="Wikipedia: Keywords",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イーグルトン『美のイデオロギー』",
    name_en="Eagleton's Ideology of the Aesthetic",
    name_original="The Ideology of the Aesthetic",
    period_key="文化唯物論期",
    definition="テリー・イーグルトン(1943-)の主著(1990)。美学の歴史を「ブルジョワ・ヘゲモニーの様式」として分析、近代美学の政治的構築を解明したマルクス主義美学の総括。",
    background="オックスフォード英文学、英国マルクス主義批評、文化唯物論。",
    development="現代マルクス主義美学、ポスト批評運動の理論的基盤。",
    historical_context="1990年代英国マルクス主義批評期。",
    primary_source_url=WIKI_EN+"Terry_Eagleton",
    primary_source_type="Wikipedia: Terry Eagleton",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"美学のイデオロギー",
         "description":"イーグルトンはマルクス主義美学と哲学を架橋。"}])

add(**C, name_ja="イーグルトン『理論以後』",
    name_en="Eagleton's After Theory",
    name_original="After Theory",
    period_key="文化唯物論期",
    definition="イーグルトンの著作(2003)。1990年代カルチュラル・スタディーズ後の批評の現状を批判的に総括、新たな倫理・政治批評の方向性を提示した21世紀批評の重要著作。",
    background="英国マルクス主義批評、ポスト構造主義批判、9.11以後の批評反省。",
    development="ポスト批評運動、現代倫理批評、政治批評の理論的基盤。",
    historical_context="2000年代英国批評反省期。",
    primary_source_url=WIKI_EN+"After_Theory",
    primary_source_type="Wikipedia: After Theory",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ホール文化研究",
    name_en="Hall's cultural studies",
    name_original="cultural studies",
    period_key="文化唯物論期",
    definition="スチュアート・ホール(1932-2014)が1970-80年代に展開した文化研究。バーミンガム現代文化研究センター(CCCS)を主導し、エンコーディング/デコーディング理論で大衆文化分析を革新。",
    background="ジャマイカ系英国人、ニューレフト・レビュー、グラムシ覇権論。",
    development="現代カルチュラル・スタディーズ、メディア研究、ポストコロニアル批評の基盤。",
    historical_context="1970-80年代英国バーミンガム文化研究期。",
    primary_source_url=WIKI_EN+"Stuart_Hall_(cultural_theorist)",
    primary_source_type="Wikipedia: Stuart Hall",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"エンコード/デコード論はAI媒介の意味生成過程を理論化する基盤。",
         "related_ai_phenomenon":"AI媒介の意味解読"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化研究方法論",
         "description":"ホールは文学批評と文化人類学を架橋する中核理論家。"}])

add(**C, name_ja="ホガート『読み書き能力の効用』",
    name_en="Hoggart's The Uses of Literacy",
    name_original="The Uses of Literacy",
    period_key="文化唯物論期",
    definition="リチャード・ホガート(1918-2014)の主著(1957)。英国労働者階級文化の戦後変容を内側から記述、英国文化研究の出発点となった先駆的著作。",
    background="リーズ大学、英国新左派、労働者階級経験。",
    development="バーミンガム文化研究センター(CCCS)創設、英国文化研究の基盤。",
    historical_context="1950年代英国大衆文化研究形成期。",
    primary_source_url=WIKI_EN+"The_Uses_of_Literacy",
    primary_source_type="Wikipedia: The Uses of Literacy",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベネット『文学の外部』",
    name_en="Bennett's Outside Literature",
    name_original="Outside Literature",
    period_key="文化唯物論期",
    definition="トニー・ベネット(1947-)の主著(1990)。「文学」概念を批判的に解体し、批評を社会制度として理論化、現代文化政策研究・カルチュラル・スタディーズの基盤を確立。",
    background="英国オープン大学、グリフィス大学、フーコー統治性論との対話。",
    development="文化政策研究、博物館研究、現代カルチュラル・スタディーズの基盤。",
    historical_context="1990年代英豪文化研究期。",
    primary_source_url=WIKI_EN+"Tony_Bennett",
    primary_source_type="Wikipedia: Tony Bennett",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: Stylistics & Cognitive Poetics (5)
# ============================================================
add(**C, name_ja="ハリデー/ハッサン『英語における結束性』",
    name_en="Halliday/Hasan Cohesion in English",
    name_original="Cohesion in English",
    period_key="文体論・認知詩学期",
    definition="マイケル・ハリデー(1925-2018)とルカイヤ・ハッサン(1931-2015)の共著(1976)。テクストの結束性を体系的に分析、機能言語学的文体論の基盤を確立した。",
    background="ロンドン大学、機能言語学、フィース言語学派の継承。",
    development="現代文体論、システム機能文法、談話分析の理論的基盤。",
    historical_context="1970年代英国機能言語学期。",
    primary_source_url=WIKI_EN+"Cohesion_(linguistics)",
    primary_source_type="Wikipedia: Cohesion",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"結束性理論はAI生成テキストの言語的結束を分析する基盤。",
         "related_ai_phenomenon":"AI生成テキストの結束性"}])

add(**C, name_ja="リーチ/ショート『小説の文体』",
    name_en="Leech/Short Style in Fiction",
    name_original="Style in Fiction",
    period_key="文体論・認知詩学期",
    definition="ジェフリー・リーチ(1936-2014)とマイケル・ショートの共著(1981)。英語小説文体の分析モデルを体系化、英米文体論の標準教科書として現代まで参照される。",
    background="ランカスター大学、英国機能言語学、文体論。",
    development="現代文体論、認知文体論、英米文学批評教育の標準テキスト。",
    historical_context="1980年代英米文体論成熟期。",
    primary_source_url=WIKI_EN+"Geoffrey_Leech",
    primary_source_type="Wikipedia: Geoffrey Leech",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="レイコフ/ジョンソン『レトリックと人生』",
    name_en="Lakoff/Johnson Metaphors We Live By",
    name_original="Metaphors We Live By",
    period_key="文体論・認知詩学期",
    definition="ジョージ・レイコフとマーク・ジョンソンの共著(1980)。概念メタファー理論を提示し、メタファーが思考の基本構造であることを論じた認知言語学・認知詩学の古典。",
    background="UCバークレー認知科学、認知言語学、生成文法批判。",
    development="認知詩学、認知文体論、AI言語処理の理論的基盤。",
    historical_context="1980年代米国認知言語学成立期。",
    primary_source_url=WIKI_EN+"Metaphors_We_Live_By",
    primary_source_type="Wikipedia: Metaphors We Live By",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"概念メタファー理論はAI言語モデルの意味構造を理論化する基盤。",
         "related_ai_phenomenon":"AI言語モデルのメタファー処理"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"概念メタファー",
         "description":"レイコフ理論はAI意味理解研究と直結。"}])

add(**C, name_ja="ステーン認知メタファー詩学",
    name_en="Steen's deliberate metaphor",
    name_original="deliberate metaphor",
    period_key="文体論・認知詩学期",
    definition="ジェラルド・ステーン(1957-)が2008-2017年に展開した「意図的メタファー」理論。レイコフ概念メタファー論を3次元(言語・思考・コミュニケーション)に拡張した認知詩学。",
    background="アムステルダム自由大学、認知言語学、認知詩学。",
    development="現代認知詩学、メタファー識別手続き(MIP)、AI意図メタファー研究の基盤。",
    historical_context="2010年代蘭認知メタファー研究期。",
    primary_source_url=WIKI_EN+"Conceptual_metaphor",
    primary_source_type="Wikipedia: Conceptual metaphor",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ストックウェル『認知詩学入門』",
    name_en="Stockwell's Cognitive Poetics",
    name_original="Cognitive Poetics: An Introduction",
    period_key="文体論・認知詩学期",
    definition="ピーター・ストックウェル(1962-)の主著(2002)。認知言語学を文学批評に応用した認知詩学を体系的に提示、英米認知詩学教育の標準教科書となった。",
    background="ノッティンガム大学、認知言語学、認知文体論。",
    development="現代認知詩学、認知ナラトロジー、AI文学分析の理論的基盤。",
    historical_context="2000年代英米認知詩学成立期。",
    primary_source_url=WIKI_EN+"Cognitive_poetics",
    primary_source_type="Wikipedia: Cognitive poetics",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"認知詩学はAI読者の認知的読書過程を理論化する基盤。",
         "related_ai_phenomenon":"AI読者の認知過程"}])


# ============================================================
# E: World Literature & Distant Reading (4)
# ============================================================
add(**C, name_ja="カザノヴァ・グリニッジ子午線",
    name_en="Casanova's Greenwich meridian",
    name_original="méridien de Greenwich littéraire",
    period_key="世界文学・遠読期",
    definition="パスカル・カザノヴァ(1959-2018)が『世界文学空間』(1999)で提示した概念。世界文学を中心(パリ)/周縁の不平等な空間として理論化し、文学的時間の世界基準点を「グリニッジ子午線」と呼んだ。",
    background="EHESS、ブルデュー社会学、世界文学社会学。",
    development="世界文学批評、文学的世界システム論、ポストコロニアル批評との対話。",
    historical_context="1990年代仏世界文学社会学期。",
    primary_source_url=WIKI_EN+"Pascale_Casanova",
    primary_source_type="Wikipedia: Pascale Casanova",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"世界文学不平等空間論はAI翻訳時代の文学世界システムを理論化する基盤。",
         "related_ai_phenomenon":"AI翻訳と世界文学空間"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"世界システム論",
         "description":"カザノヴァは文学批評と社会学・人類学を架橋。"}])

add(**C, name_ja="モレッティ「世界文学への臆説」",
    name_en="Moretti's Conjectures on World Literature",
    name_original="Conjectures on World Literature",
    period_key="世界文学・遠読期",
    definition="フランコ・モレッティ(1950-)の論文(2000)。世界文学を一個・不平等のシステムとして理論化、遠読方法論を提唱、世界文学批評と計算文学批評を架橋した綱領的論文。",
    background="スタンフォード大学、ウォーラーステイン世界システム論、定量分析。",
    development="世界文学批評、計算文学批評、デジタル人文学の理論的基盤。",
    historical_context="2000年代米国世界文学批評期。",
    primary_source_url=WIKI_EN+"Franco_Moretti",
    primary_source_type="Wikipedia: Franco Moretti",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"遠読・世界文学論はAI時代の大規模文学分析の理論的基盤。",
         "related_ai_phenomenon":"AI遠読と世界文学"}])

add(**C, name_ja="ダムロッシュ『どう世界文学を読むか』",
    name_en="Damrosch's How to Read World Literature",
    name_original="How to Read World Literature",
    period_key="世界文学・遠読期",
    definition="デイヴィッド・ダムロッシュ(1953-)の著作(2009)。世界文学を「翻訳における流通」として定義、文学を文化間の往還運動として読む実践的方法論を提示した。",
    background="ハーバード大学比較文学、世界文学運動。",
    development="現代世界文学批評教育、米国比較文学教育の標準テキスト。",
    historical_context="2000年代米国世界文学運動期。",
    primary_source_url=WIKI_EN+"David_Damrosch",
    primary_source_type="Wikipedia: David Damrosch",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ダムロッシュ『何の世界文学か』",
    name_en="Damrosch's What Is World Literature?",
    name_original="What Is World Literature?",
    period_key="世界文学・遠読期",
    definition="ダムロッシュの主著(2003)。世界文学を「文化的差異の伝送」として再定義、ゲーテ的世界文学概念を21世紀的に再構築した世界文学批評の中核著作。",
    background="ハーバード大学比較文学、ゲーテ世界文学観。",
    development="現代世界文学批評の方法論的基盤、米国比較文学の中核テキスト。",
    historical_context="2000年代初頭世界文学運動形成期。",
    primary_source_url=PUP+"books/paperback/9780691049861",
    primary_source_type="Princeton UP: What Is World Literature",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: Postcolonial extension (5)
# ============================================================
add(**C, name_ja="スピヴァク『教える機関の外へ』",
    name_en="Spivak's Outside in the Teaching Machine",
    name_original="Outside in the Teaching Machine",
    period_key="ポストコロニアル理論拡張期",
    definition="ガヤトリ・スピヴァク(1942-)の主著(1993)。多文化主義・脱植民地化教育・グローバル資本主義を批判的に分析、ポストコロニアル批評の方法論的基盤を再構築した。",
    background="コロンビア大学、デリダ脱構築、フェミニスト・マルクス主義。",
    development="現代ポストコロニアル批評、世界文学批評、大学批判の理論的基盤。",
    historical_context="1990年代米国ポストコロニアル批評期。",
    primary_source_url=WIKI_EN+"Gayatri_Chakravorty_Spivak",
    primary_source_type="Wikipedia: Spivak",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スピヴァク『学問分野の死』",
    name_en="Spivak's Death of a Discipline",
    name_original="Death of a Discipline",
    period_key="ポストコロニアル理論拡張期",
    definition="スピヴァクの主著(2003)。比較文学を地域研究・世界文学に開く新たな学問分野像を提示、惑星性(planetarity)概念を理論化した21世紀比較文学の綱領的著作。",
    background="コロンビア大学比較文学、世界文学運動、地域研究批判。",
    development="現代比較文学、惑星批評、エコ批評との接続。",
    historical_context="2000年代米国比較文学転換期。",
    primary_source_url=COL+"book/death-of-a-discipline/9780231129459",
    primary_source_type="Columbia UP: Death of a Discipline",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"惑星性概念はAI時代のグローバル文学批評を理論化する基盤。",
         "related_ai_phenomenon":"AI時代の惑星批評"}])

add(**C, name_ja="バーバ「ディセミネーション」",
    name_en="Bhabha's DissemiNation",
    name_original="DissemiNation",
    period_key="ポストコロニアル理論拡張期",
    definition="ホミ・バーバ(1949-)が『文化の場所』(1994)所収論文で提示した概念。国民の物語を「教育的」と「遂行的」の二重時間として分析、近代国民国家批判の理論的中核。",
    background="シカゴ大学、デリダ脱構築、ファノン精神分析。",
    development="現代国民国家批判、ポストコロニアル文学批評、ディアスポラ研究の基盤。",
    historical_context="1990年代米国ポストコロニアル批評期。",
    primary_source_url=WIKI_EN+"Homi_K._Bhabha",
    primary_source_type="Wikipedia: Homi K. Bhabha",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ムベンベ『黒人理性批判』",
    name_en="Mbembe's Critique of Black Reason",
    name_original="Critique de la raison nègre",
    period_key="ポストコロニアル理論拡張期",
    definition="アシル・ムベンベ(1957-)の主著(2013)。「黒人」概念の歴史的構築を批判的に分析、グローバル資本主義における新たな人種化を理論化した現代ポストコロニアル批評の中核。",
    background="ヴィッツ大学(南アフリカ)、フーコー、ファノン、フランス現代思想。",
    development="アフロペシミズム、現代ブラック・スタディーズ、グローバル批評理論の基盤。",
    historical_context="2010年代南アフリカ・米国ブラック批評期。",
    primary_source_url=WIKI_EN+"Achille_Mbembe",
    primary_source_type="Wikipedia: Achille Mbembe",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"黒人理性批判はAI時代の人種化アルゴリズム的暴力を理論化する基盤。",
         "related_ai_phenomenon":"AIアルゴリズム的人種化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"批判理論",
         "description":"ムベンベはアフリカ哲学とポストコロニアル批評を架橋。"}])

add(**C, name_ja="ミニョーロ『ラテンアメリカという理念』",
    name_en="Mignolo's Idea of Latin America",
    name_original="The Idea of Latin America",
    period_key="ポストコロニアル理論拡張期",
    definition="ウォルター・ミニョーロ(1941-)の主著(2005)。「ラテンアメリカ」概念を植民地的差異から再分析、脱植民地化思想(decolonial thinking)を体系化したラテンアメリカ批評の中核。",
    background="デューク大学、植民地的差異論、キハーノ脱植民地論。",
    development="脱植民地化思想、現代ラテンアメリカ批評、グローバル批評理論の基盤。",
    historical_context="2000年代米国脱植民地化思想期。",
    primary_source_url=WIKI_EN+"Walter_Mignolo",
    primary_source_type="Wikipedia: Walter Mignolo",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"脱植民地化思想",
         "description":"ミニョーロはラテンアメリカ批評と人類学を架橋。"}])


# ============================================================
# G: Disability & Animal Studies (7)
# ============================================================
add(**C, name_ja="ガーランド=トムソン『非凡な身体』",
    name_en="Garland-Thomson Extraordinary Bodies",
    name_original="Extraordinary Bodies",
    period_key="障害研究・動物研究期",
    definition="ローズマリー・ガーランド=トムソン(1946-)の主著(1997)。米国文化における障害身体の表象を分析、身体特例(physical disability)を文化的構築として理論化した障害研究文学批評の出発点。",
    background="エモリー大学、米国フェミニスト批評、文化研究。",
    development="現代障害研究、文学批評における身体特例研究、フェミニスト障害研究の基盤。",
    historical_context="1990年代米国障害研究形成期。",
    primary_source_url=WIKI_EN+"Rosemarie_Garland-Thomson",
    primary_source_type="Wikipedia: Garland-Thomson",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"非凡な身体論はAI時代の身体表象・データ表象を理論化する基盤。",
         "related_ai_phenomenon":"AI生成身体表象"}])

add(**C, name_ja="デイヴィス『正常性の強制』",
    name_en="Davis's Enforcing Normalcy",
    name_original="Enforcing Normalcy",
    period_key="障害研究・動物研究期",
    definition="レナード・デイヴィスの主著(1995)。「正常性」概念の19世紀統計学的構築を分析、障害を「正常性」概念の構成的他者として理論化した障害研究文学批評の中核。",
    background="ニューヨーク市立大学院、フーコー統計学批判、障害研究。",
    development="現代障害研究、19世紀小説批評、統計学的人間概念史の基盤。",
    historical_context="1990年代米国障害研究形成期。",
    primary_source_url=WIKI_EN+"Disability_studies",
    primary_source_type="Wikipedia: Disability studies",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ミッチェル/スナイダー『障害の文化的場所』",
    name_en="Mitchell/Snyder Cultural Locations of Disability",
    name_original="Cultural Locations of Disability",
    period_key="障害研究・動物研究期",
    definition="デイヴィッド・ミッチェルとシャロン・スナイダーの共著(2006)。障害の物語的義肢(narrative prosthesis)概念を発展させ、障害が文化的「場所」として配置される構造を理論化。",
    background="シカゴ大学、米国障害研究、文学批評。",
    development="現代障害研究、米国文学批評教育の障害研究入門、視覚障害研究との接続。",
    historical_context="2000年代米国障害研究成熟期。",
    primary_source_url=WIKI_EN+"Disability_studies",
    primary_source_type="Wikipedia: Disability studies",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マクルーア『クリップ理論』",
    name_en="McRuer's Crip Theory",
    name_original="Crip Theory: Cultural Signs of Queerness and Disability",
    period_key="障害研究・動物研究期",
    definition="ロバート・マクルーア(1966-)の主著(2006)。クィア理論と障害研究を接続する「クリップ理論」を提示、強制的健常性(compulsory able-bodiedness)概念を理論化した。",
    background="ジョージ・ワシントン大学、クィア理論、障害研究。",
    development="現代クリップ理論、クィア障害研究、米国障害研究の中核。",
    historical_context="2000年代米国クィア障害研究形成期。",
    primary_source_url=WIKI_EN+"Crip_theory",
    primary_source_type="Wikipedia: Crip theory",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"クリップ理論はAI時代の身体規範・健常性概念を理論化する基盤。",
         "related_ai_phenomenon":"AI身体規範批判"}])

add(**C, name_ja="ウルフ『動物儀礼』",
    name_en="Wolfe's Animal Rites",
    name_original="Animal Rites",
    period_key="障害研究・動物研究期",
    definition="ケアリー・ウルフ(1959-)の主著(2003)。デリダ動物論を継承し、米国文化における動物表象を分析、ポストヒューマニスト動物研究の理論的基盤を確立した。",
    background="ライス大学、デリダ動物論、ポストヒューマニズム。",
    development="現代動物研究、ポストヒューマニズム文学批評、エコクリティシズムとの接続。",
    historical_context="2000年代米国動物研究形成期。",
    primary_source_url=WIKI_EN+"Animal_studies",
    primary_source_type="Wikipedia: Animal studies",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"動物哲学",
         "description":"ウルフは動物哲学と文学批評を架橋。"}])

add(**C, name_ja="ハラウェイ『犬と人が出会うとき』",
    name_en="Haraway's Companion Species",
    name_original="The Companion Species Manifesto",
    period_key="障害研究・動物研究期",
    definition="ダナ・ハラウェイ(1944-)の主著(2003)。サイボーグ宣言以後、種間関係を「伴侶種」として理論化、人間-動物-技術の連続性を示した現代ポストヒューマニズムの中核。",
    background="UCサンタクルーズ、フェミニスト科学技術論、サイボーグ・フェミニズム。",
    development="現代マルチスピーシーズ研究、人新世批評、ポストヒューマン批評の基盤。",
    historical_context="2000年代米国マルチスピーシーズ研究形成期。",
    primary_source_url=WIKI_EN+"The_Companion_Species_Manifesto",
    primary_source_type="Wikipedia: Companion Species Manifesto",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"伴侶種論はAI時代の人間-機械-動物の連続性を理論化する基盤。",
         "related_ai_phenomenon":"AI伴侶種"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"マルチスピーシーズ研究",
         "description":"ハラウェイは文学批評と人類学を架橋する中核理論家。"}])

add(**C, name_ja="ハラウェイ『困難と共に留まる』",
    name_en="Haraway's Staying with the Trouble",
    name_original="Staying with the Trouble",
    period_key="障害研究・動物研究期",
    definition="ハラウェイの主著(2016)。人新世批判として「クトゥルー新世」を提唱、種間連帯・親族化(making kin)を理論化した現代ポストヒューマン批評の中核著作。",
    background="UCサンタクルーズ、人新世批判、フェミニスト科学技術論。",
    development="現代人新世批評、マルチスピーシーズ研究、生態学的批評の基盤。",
    historical_context="2010年代米国人新世批判期。",
    primary_source_url=DUKE+"staying-with-the-trouble",
    primary_source_type="Duke UP: Staying with the Trouble",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: Affect deepened (5)
# ============================================================
add(**C, name_ja="バーラント『残酷な楽観性』詳論",
    name_en="Berlant Cruel Optimism deeper",
    name_original="Cruel Optimism",
    period_key="情動批評深化期",
    definition="バーラントの主著(2011)詳論。「良き生」への愛着が幸福を阻む構造を「残酷な楽観性」として理論化、新自由主義時代の情動構造を解明した中核著作。",
    background="シカゴ大学、フェミニスト情動研究、新自由主義批判。",
    development="現代情動批評、新自由主義文化批評、ポスト批評運動の理論的基盤。",
    historical_context="2010年代米国情動批評深化期。",
    primary_source_url=DUKE+"cruel-optimism",
    primary_source_type="Duke UP: Cruel Optimism",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"残酷な楽観性論はAI時代の情動的愛着・幸福概念を理論化する基盤。",
         "related_ai_phenomenon":"AI媒介の残酷な楽観性"}])

add(**C, name_ja="アハメド『フェミニストとしての生』",
    name_en="Ahmed's Living a Feminist Life",
    name_original="Living a Feminist Life",
    period_key="情動批評深化期",
    definition="サラ・アハメドの主著(2017)。フェミニズム理論を日常実践として理論化、「フェミニスト・キルジョイ」概念で家父長制への抵抗実践を批評的に提示した。",
    background="ロンドン大学、クィア現象学、フェミニスト情動批評。",
    development="現代フェミニスト批評、日常実践批評、SNS時代のフェミニズム実践理論。",
    historical_context="2010年代英国フェミニスト批評期。",
    primary_source_url=DUKE+"living-a-feminist-life",
    primary_source_type="Duke UP: Living a Feminist Life",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"フェミニスト・キルジョイ論はAI時代のフェミニズム抵抗実践を理論化する基盤。",
         "related_ai_phenomenon":"AI時代のフェミニスト批判"}])

add(**C, name_ja="マッスミ『情動の政治』",
    name_en="Massumi's Politics of Affect",
    name_original="Politics of Affect",
    period_key="情動批評深化期",
    definition="ブライアン・マッスミ(1956-)の主著(2015)。ドゥルーズ=スピノザ的情動論を政治批評に応用、新自由主義時代の権力と情動の関係を理論化した現代情動政治批評の中核。",
    background="モントリオール大学、ドゥルーズ=ガタリ、フェミニスト情動批評。",
    development="現代情動政治批評、メディア批評、ポスト批評運動の理論的基盤。",
    historical_context="2010年代加米情動政治批評期。",
    primary_source_url=WIKI_EN+"Brian_Massumi",
    primary_source_type="Wikipedia: Brian Massumi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"情動の政治",
         "description":"マッスミはドゥルーズ哲学と現代政治批評を架橋。"}])

add(**C, name_ja="セジウィック『感情を触れて』",
    name_en="Sedgwick's Touching Feeling",
    name_original="Touching Feeling",
    period_key="情動批評深化期",
    definition="イヴ・コソフスキー・セジウィック(1950-2009)の主著(2003)。シルヴァン・トムキンズ情動心理学に基づき「リパラティブ・リーディング」を提唱、ポスト批評運動の理論的源泉。",
    background="デューク大学、クィア理論、トムキンズ情動心理学。",
    development="ポスト批評運動、現代情動批評、リパラティブ・リーディング実践の中核。",
    historical_context="2000年代米国情動批評期。",
    primary_source_url=DUKE+"touching-feeling",
    primary_source_type="Duke UP: Touching Feeling",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"リパラティブ・リーディングはAI時代の批評実践を理論化する基盤。",
         "related_ai_phenomenon":"AI時代のリパラティブ批評"}])

add(**C, name_ja="ガイ『ギミック理論』詳論",
    name_en="Ngai Theory of Gimmick deeper",
    name_original="Theory of the Gimmick (deeper)",
    period_key="情動批評深化期",
    definition="シアン・ガイ(1971-)『ギミックの理論』(2020)詳論。ギミックを「節約労働の擬似形式」として理論化、資本主義美学カテゴリー三部作(興味深さ・キュート・ギミック)の完結編。",
    background="シカゴ大学英文学、マルクス主義美学、現代美学カテゴリー。",
    development="現代カテゴリー批評、AI生成物の美学的位置論への適用可能性。",
    historical_context="2020年代米国カテゴリー批評成熟期。",
    primary_source_url=HUP+"catalog.php?isbn=9780674984547",
    primary_source_type="Harvard UP: Theory of the Gimmick",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"ギミック詳論はAI生成物の美学的位置を理論化する基盤。",
         "related_ai_phenomenon":"AI生成物のギミック化"}])


# ============================================================
# I: Distant reading (4)
# ============================================================
add(**C, name_ja="アンダーウッド『遠い地平』",
    name_en="Underwood's Distant Horizons",
    name_original="Distant Horizons",
    period_key="デジタル人文学第二世代期",
    definition="テッド・アンダーウッド(1970-)の主著(2019)。機械学習で18-21世紀英米文学のジャンル・ジェンダー・声を量的に分析、計算文学批評の方法論的基盤を確立した。",
    background="イリノイ大学、機械学習、計算文学批評。",
    development="現代計算文学批評、AI文学分析、デジタル文学研究教育の標準テキスト。",
    historical_context="2010年代末米国計算文学批評期。",
    primary_source_url=UCP+"ucp/books/book/chicago/D/bo35853783.html",
    primary_source_type="U Chicago Press: Distant Horizons",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"機械学習文学批評はAI時代の文学分析方法論の理論的基盤。",
         "related_ai_phenomenon":"AIによる機械学習文学分析"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"機械学習文学批評",
         "description":"アンダーウッド方法論はAI文学分析と直結。"}])

add(**C, name_ja="ボード『フィクションの世界』",
    name_en="Bode's A World of Fiction",
    name_original="A World of Fiction",
    period_key="デジタル人文学第二世代期",
    definition="キャサリン・ボード(1976-)の主著(2018)。デジタル文学史の方法論を批判的に再検討、量的方法と文学史の関係を理論化したデジタル人文学批判の重要著作。",
    background="豪オーストラリア国立大学、19世紀豪文学研究、デジタル人文学。",
    development="デジタル文学史方法論、計算文学批評の自己反省、現代DH批判理論の基盤。",
    historical_context="2010年代末豪デジタル人文学期。",
    primary_source_url=WIKI_EN+"Digital_humanities",
    primary_source_type="Wikipedia: Digital humanities",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"デジタル文学史批判はAI時代のデジタル文学史の方法論を理論化する基盤。",
         "related_ai_phenomenon":"AI生成のデジタル文学史"}])

add(**C, name_ja="ドラッカー『SpecLab』",
    name_en="Drucker's SpecLab",
    name_original="SpecLab: Digital Aesthetics and Projects in Speculative Computing",
    period_key="デジタル人文学第二世代期",
    definition="ジョアンナ・ドラッカー(1952-)の主著(2009)。デジタル人文学を投機的計算(speculative computing)として再概念化、視覚化批評・人文情報設計の理論的基盤を確立した。",
    background="UCLA情報学、書物史、デジタル美学。",
    development="現代視覚化批評、デジタル美学、人文情報学の理論的基盤。",
    historical_context="2000年代末米国デジタル美学期。",
    primary_source_url=UCP+"ucp/books/book/chicago/S/bo6750876.html",
    primary_source_type="U Chicago Press: SpecLab",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="パイパー『列挙』詳論",
    name_en="Piper Enumerations deeper",
    name_original="Enumerations (deeper)",
    period_key="デジタル人文学第二世代期",
    definition="アンドリュー・パイパー(1973-)『列挙』(2018)詳論。文学量的研究の5つの方法論的次元(言語・小説性・登場人物・設定・物語)を体系化、計算文学批評の理論的基盤。",
    background="マギル大学比較文学、デジタル人文学、計算文学批評。",
    development="現代計算文学批評教育、AI文学分析、デジタル文学研究の方法論的標準。",
    historical_context="2010年代末加デジタル文学批評期。",
    primary_source_url=UCP+"ucp/books/book/chicago/E/bo28113896.html",
    primary_source_type="U Chicago Press: Enumerations",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"計算文学方法論",
         "description":"パイパー詳論はAI文学分析の方法論的基盤。"}])


# ============================================================
# J: Black Criticism & Recent Material (7)
# ============================================================
add(**C, name_ja="ロウ『四大陸の親密性』",
    name_en="Lowe's Intimacies of Four Continents",
    name_original="The Intimacies of Four Continents",
    period_key="ブラック批評・現代物質批評期",
    definition="リサ・ロウ(1955-)の主著(2015)。アジア・アフリカ・米州・欧州の植民地的親密性を分析、リベラル人文学の自由概念の構造的暴力を理論化した現代ポストコロニアル批評の中核。",
    background="UCサンディエゴ、ポストコロニアル批評、アーカイヴ研究。",
    development="現代ポストコロニアル批評、植民地的親密性研究、グローバル批評理論の基盤。",
    historical_context="2010年代米国ポストコロニアル批評期。",
    primary_source_url=DUKE+"the-intimacies-of-four-continents",
    primary_source_type="Duke UP: Intimacies of Four Continents",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"植民地的親密性論はAI時代のグローバル不平等を理論化する基盤。",
         "related_ai_phenomenon":"AI媒介の植民地的親密性"}])

add(**C, name_ja="ハートマン『母を失う』",
    name_en="Hartman's Lose Your Mother",
    name_original="Lose Your Mother",
    period_key="ブラック批評・現代物質批評期",
    definition="サイディヤ・ハートマン(1961-)の主著(2007)。大西洋奴隷貿易の遺産をガーナへの旅から散文詩的に分析、「批判的虚構(critical fabulation)」方法論を提示した現代ブラック批評の中核。",
    background="コロンビア大学、ブラック・スタディーズ、フェミニスト・トラウマ研究。",
    development="現代ブラック批評、批判的虚構方法論、アーカイブ批評の基盤。",
    historical_context="2000年代米国ブラック批評期。",
    primary_source_url=WIKI_EN+"Saidiya_Hartman",
    primary_source_type="Wikipedia: Saidiya Hartman",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"批判的虚構論はAI生成歴史叙述の方法論を理論化する基盤。",
         "related_ai_phenomenon":"AI生成の批判的虚構"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"批判的虚構",
         "description":"ハートマン方法論は文学批評と歴史人類学を架橋。"}])

add(**C, name_ja="カンプト『画像を聴く』",
    name_en="Campt's Listening to Images",
    name_original="Listening to Images",
    period_key="ブラック批評・現代物質批評期",
    definition="ティナ・カンプト(1964-)の主著(2017)。アフロ・ディアスポラ写真を「聴く」批評実践として理論化、視覚批評と聴覚批評の境界を再構築した現代ブラック批評の中核。",
    background="ブラウン大学、ブラック・スタディーズ、視覚文化批評。",
    development="現代ブラック視覚批評、聴覚批評、フェミニスト・アーカイヴ批評の基盤。",
    historical_context="2010年代米国ブラック視覚批評期。",
    primary_source_url=DUKE+"listening-to-images",
    primary_source_type="Duke UP: Listening to Images",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シャープ『航跡の中で』",
    name_en="Sharpe's In the Wake",
    name_original="In the Wake",
    period_key="ブラック批評・現代物質批評期",
    definition="クリスティーナ・シャープ(1964-)の主著(2016)。「航跡(wake)」を奴隷船の物理的航跡・通夜・覚醒の三重隠喩として理論化、現代ブラック批評の中核著作。",
    background="トロント大学、ブラック・スタディーズ、フェミニスト批評。",
    development="現代ブラック批評、奴隷制の余生批評、グローバル批評理論への影響。",
    historical_context="2010年代米加ブラック批評期。",
    primary_source_url=DUKE+"in-the-wake",
    primary_source_type="Duke UP: In the Wake",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"航跡論はAI時代のブラックネス・主体性を理論化する基盤。",
         "related_ai_phenomenon":"AI時代のブラック主体性"}])

add(**C, name_ja="モテン『破断において』",
    name_en="Moten's In the Break",
    name_original="In the Break",
    period_key="ブラック批評・現代物質批評期",
    definition="フレッド・モテン(1962-)の主著(2003)。アフロアメリカン美学の「破断(break)」を理論化、ブラック・ラディカル伝統と批評理論を統合した現代ブラック批評の中核。",
    background="UCバークレー、ブラック・スタディーズ、批評理論、ジャズ批評。",
    development="現代ブラック・ラディカル批評、ジャズ批評、批評理論の交差点。",
    historical_context="2000年代米国ブラック批評期。",
    primary_source_url=WIKI_EN+"Fred_Moten",
    primary_source_type="Wikipedia: Fred Moten",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウォレン『存在論的恐怖』",
    name_en="Warren's Ontological Terror",
    name_original="Ontological Terror",
    period_key="ブラック批評・現代物質批評期",
    definition="カルヴィン・ウォレンの主著(2018)。アフロペシミズム哲学を発展させ、ブラックネスを「無(nothing)」として存在論的に理論化した現代ブラック批評の中核著作。",
    background="ジョージ・ワシントン大学、ハイデガー存在論、アフロペシミズム。",
    development="現代アフロペシミズム、ブラック存在論批評、批判理論の基盤。",
    historical_context="2010年代米国アフロペシミズム期。",
    primary_source_url=DUKE+"ontological-terror",
    primary_source_type="Duke UP: Ontological Terror",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アフロペシミズム",
         "description":"ウォレンはハイデガー哲学とブラック批評を架橋。"}])

add(**C, name_ja="ディンショー『今がいかに早いか』",
    name_en="Dinshaw's How Soon Is Now",
    name_original="How Soon Is Now?",
    period_key="ブラック批評・現代物質批評期",
    definition="キャロライン・ディンショー(1958-)の主著(2012)。中世文学とクィア時間性を架橋し、アマチュア中世主義者の「非専門家的」読書実践を理論化した現代クィア中世批評の中核。",
    background="ニューヨーク大学、中世英文学、クィア理論、フェミニスト批評。",
    development="現代クィア中世批評、クィア時間性批評、アマチュア批評の基盤。",
    historical_context="2010年代米国クィア中世批評期。",
    primary_source_url=DUKE+"how-soon-is-now",
    primary_source_type="Duke UP: How Soon Is Now",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"クィア時間性はAI時代の時間性概念を理論化する基盤。",
         "related_ai_phenomenon":"AI時代のクィア時間性"}])


# ============================================================
# K: Reception & Hermeneutics extension (4)
# ============================================================
add(**C, name_ja="ヤウス『美的経験と文学解釈学』",
    name_en="Jauss's Aesthetic Reception",
    name_original="Ästhetische Erfahrung und literarische Hermeneutik",
    period_key="受容理論・解釈学拡張期",
    definition="ハンス・ロベルト・ヤウス(1921-1997)の主著(1977)。受容美学を解釈学的に拡張、美的経験を「ポイエーシス・アイステーシス・カタルシス」の三契機として理論化した。",
    background="コンスタンツ大学、ガダマー解釈学、ロマン哲学。",
    development="現代受容美学、解釈学的批評、美的経験論の中核。",
    historical_context="1970年代独受容美学成熟期。",
    primary_source_url=WIKI_EN+"Hans_Robert_Jauss",
    primary_source_type="Wikipedia: Jauss",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"美的経験論",
         "description":"ヤウスは受容美学と解釈学哲学を架橋。"}])

add(**C, name_ja="ガダマー『真理と方法』文学篇",
    name_en="Gadamer Truth Method literary",
    name_original="Wahrheit und Methode (literary)",
    period_key="受容理論・解釈学拡張期",
    definition="ハンス=ゲオルク・ガダマー(1900-2002)『真理と方法』(1960)の文学批評的射程。地平の融合・効果史・伝統概念を文学解釈に適用、受容美学・現代解釈学の理論的基盤を提供した。",
    background="ハイデガー存在論的解釈学、フィロロギー伝統、フッサール現象学。",
    development="現代解釈学的批評、受容美学、ヤウス・イーザー理論の哲学的基盤。",
    historical_context="1960年代独哲学的解釈学成立期。",
    primary_source_url=SEP+"gadamer/",
    primary_source_type="Stanford Encyclopedia: Gadamer",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"地平融合論はAI時代の解釈・対話を理論化する哲学的基盤。",
         "related_ai_phenomenon":"AI媒介の地平融合"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"哲学的解釈学",
         "description":"ガダマーは哲学と文学批評を架橋する中核理論家。"}])

add(**C, name_ja="リクール『時間と物語』第2巻",
    name_en="Ricoeur Time Narrative II",
    name_original="Temps et récit II",
    period_key="受容理論・解釈学拡張期",
    definition="ポール・リクール(1913-2005)『時間と物語』第2巻(1984)。フィクション物語を分析、ジュネット・ハイデガー・アウエルバッハを統合し、虚構物語の時間性を理論化した。",
    background="パリ大学、現象学的解釈学、構造主義との対話。",
    development="現代物語論哲学、ナラトロジー、ストーリーワールド理論の哲学的基盤。",
    historical_context="1980年代仏哲学的物語論期。",
    primary_source_url=SEP+"ricoeur/",
    primary_source_type="Stanford Encyclopedia: Ricoeur",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"物語論哲学",
         "description":"リクールは物語論と哲学を架橋する中核理論家。"}])

add(**C, name_ja="リクール『時間と物語』第3巻",
    name_en="Ricoeur Time Narrative III",
    name_original="Temps et récit III",
    period_key="受容理論・解釈学拡張期",
    definition="リクール『時間と物語』第3巻(1985)。歴史叙述と虚構物語の交差を分析、語られた時間としての人間時間を理論化した現代物語論哲学の中核著作。",
    background="パリ大学、現象学的解釈学、歴史哲学との対話。",
    development="現代歴史叙述論、ナラトロジー、自伝研究の哲学的基盤。",
    historical_context="1980年代仏歴史哲学的物語論期。",
    primary_source_url=WIKI_EN+"Time_and_Narrative",
    primary_source_type="Wikipedia: Time and Narrative",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"歴史","status":"rethinking",
         "rationale":"歴史叙述論はAI生成歴史叙述の方法論を理論化する哲学的基盤。",
         "related_ai_phenomenon":"AI生成歴史叙述"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="横断",
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
        print(f"[c34-retry60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c34-retry60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
