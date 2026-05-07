"""LIT-DB Wave 15 — C34: Literary Theory retry (+40 concepts).

Subfield: lit_theory (id=22), region='横断'.
Adds 40 NEW NON-OVERLAPPING concepts (existing 130 → target 170).
Coverage:
  A: Marxist criticism extension (Adorno, Benjamin, Althusser
     interpellation literary, Bourdieu literary field, Williams
     structures of feeling, Jameson cognitive mapping) — 6
  B: Reader-response / reception (Iser act of reading, Bleich
     subjective, Riffaterre semiotics of poetry, Hirsch validity,
     Tompkins reader-response) — 5
  C: Psychoanalytic (Caruth unclaimed experience, Abraham/Torok
     crypt, Brooks Melodramatic Imagination, Mahlendorf,
     Felman crisis of witnessing) — 5
  D: Narratology (Herman storyworld/cognitive, Ryan
     transmedial, Jahn focalization revisited, Margolin
     character, Nünning unreliable narrator, Schmid event) — 6
  E: Book history / material text (Genette paratexts,
     Greetham textual scholarship, Gerard Genette Seuils,
     Stallybrass material text) — 4
  F: Affect/cognitive/post-critique (Berlant intimate publics,
     Cvetkovich archive of feelings, Stewart ordinary affects,
     Gallagher historicizing form, Moi ordinary language,
     Anker/Felski critique reform) — 6
  G: Digital / quantitative (Piper enumerations, Algee-Hewitt
     stanford lab, Long/So computational, Liu DH ideologies) — 4
  H: Recent material/category (Ngai Theory of Gimmick book,
     Ahmed queer phenomenology, Berlant Female Complaint,
     Cheng ornamentalism) — 4

>= 60% primary tier; fourth_transform_tags >= 18; cross_domain >= 14.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("マルクス主義文学批評期", "Marxist Literary Criticism", 1920, 1990,
     "ルカーチに始まる社会経済的文学批評期。"),
    ("受容理論期", "Reader-Response / Reception Theory", 1965, 1995,
     "コンスタンツ学派と米国読者反応批評期。"),
    ("精神分析文学批評期", "Psychoanalytic Literary Criticism",
     1900, 2010,
     "フロイトからラカン・トラウマ理論までの精神分析文学批評。"),
    ("古典・古典後ナラトロジー期", "Classical & Post-Classical Narratology",
     1972, 2025,
     "ジュネット以後の認知・修辞・トランスメディア物語論期。"),
    ("書物史・受容史期", "Book History & History of Reading",
     1979, 2015,
     "ダーントン・マッケンジーら書物史・物質的テクスト批評期。"),
    ("情動・認知・ポスト批評期", "Affect, Cognitive, Post-Critique",
     2000, 2025,
     "情動論・ポスト批評・現代米国批評の21世紀理論期。"),
    ("デジタル・量的文学研究期", "Digital / Quantitative Literary Studies",
     2000, 2025,
     "モレッティ・ジョッカーズ以後のDH・計算批評期。"),
    ("価値・現代物質批評期", "Value & Recent Material Criticism",
     2010, 2025,
     "ガイ・ベウィスら現代物質批評・カテゴリー批評期。"),
]

WIKI_EN = "https://en.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
ARCH = "https://archive.org/details/"
JSTOR = "https://www.jstor.org/"
MARX = "https://www.marxists.org/"
DUKE = "https://read.dukeupress.edu/"
OXF = "https://academic.oup.com/"
PUP = "https://press.princeton.edu/"
COL = "https://cup.columbia.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_theory", region="横断", original_script="roman")


# ============================================================
# A: Marxist literary criticism extension (6)
# ============================================================
add(**C, name_ja="アドルノ『美の理論』",
    name_en="Adorno's Aesthetic Theory",
    name_original="Ästhetische Theorie",
    period_key="マルクス主義文学批評期",
    definition="テオドール・W・アドルノ(1903-1969)の遺著(1970)。芸術作品の自律性と社会性の弁証法を論じ、近代芸術の「謎の性格」を後期資本主義への否定的批判と捉える。",
    background="フランクフルト学派批判理論、ヘーゲル=マルクス美学、ベンヤミン芸術論との対話。",
    development="ジェイムソン、イーグルトン、現代ポストモダン芸術論への影響大。",
    historical_context="1960年代西ドイツ批判理論成熟期。",
    primary_source_url=WIKI_EN+"Aesthetic_Theory",
    primary_source_type="Wikipedia: Aesthetic Theory",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"自律的芸術と社会の弁証法は、AI生成芸術が両者の境界を再編する状況を理論化する基盤。",
         "related_ai_phenomenon":"AI生成芸術の自律性問題"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"批判理論美学",
         "description":"アドルノ美学はフランクフルト批判理論の文学・芸術論的中核。"}])

add(**C, name_ja="ベンヤミン「複製技術時代の芸術作品」",
    name_en="Benjamin's Work of Art in Mechanical Reproduction",
    name_original="Das Kunstwerk im Zeitalter seiner technischen Reproduzierbarkeit",
    period_key="マルクス主義文学批評期",
    definition="ヴァルター・ベンヤミン(1892-1940)が1936年に発表した論文。複製技術によるアウラ(本物性)の喪失と、政治的芸術への可能性を論じた20世紀メディア・芸術論の古典。",
    background="フランクフルト学派周縁、ブレヒト的政治芸術、ファシズム下の文化危機。",
    development="メディア論・文化研究・ポスト構造主義芸術論の出発点。",
    historical_context="1930年代ドイツ亡命知識人とファシズム下のメディア論。",
    primary_source_url=MARX+"reference/subject/philosophy/works/ge/benjamin.htm",
    primary_source_type="Marxists.org: Benjamin",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"アウラ喪失論はAI複製による作者性・本物性概念の再編を理論化する基盤。",
         "related_ai_phenomenon":"AI生成物のアウラとオリジナリティ"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"複製技術と本物性",
         "description":"AIによる無限複製は、ベンヤミンのアウラ論を21世紀的に再活性化させる。"}])

add(**C, name_ja="アルチュセール「文学とイデオロギー」",
    name_en="Althusser on literature and ideology",
    name_original="Althusser sur la littérature et l'idéologie",
    period_key="マルクス主義文学批評期",
    definition="ルイ・アルチュセール(1918-1990)が1966-71年に展開した文学・イデオロギー論。文学はイデオロギーから「内的距離」を取ることで認識を可能にすると論じ、マシュレに継承された。",
    background="構造主義マルクス主義、スピノザ的読解、フランス共産党理論期。",
    development="マシュレ「文学的生産の理論」、イーグルトン批評論への決定的影響。",
    historical_context="1960年代フランス構造主義マルクス主義の展開期。",
    primary_source_url=MARX+"reference/archive/althusser/",
    primary_source_type="Marxists.org: Althusser archive",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"イデオロギーと呼びかけ",
         "description":"アルチュセールのイデオロギー論は文学批評と哲学を架橋する中核理論。"}])

add(**C, name_ja="ブルデュー文学場の理論",
    name_en="Bourdieu's theory of the literary field",
    name_original="champ littéraire",
    period_key="マルクス主義文学批評期",
    definition="ピエール・ブルデュー(1930-2002)の『芸術の規則』(1992)で展開された理論。文学を相対的自律性をもつ「場(champ)」として捉え、象徴資本・ハビトゥスで作家戦略を分析した。",
    background="社会学的相対化、フローベール研究、フランス構造主義以後の文化社会学。",
    development="文化社会学・出版研究・グローバル文学社会学に決定的影響。",
    historical_context="1990年代フランス文化社会学成熟期。",
    primary_source_url=WIKI_EN+"Pierre_Bourdieu",
    primary_source_type="Wikipedia: Bourdieu",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"文学場理論は、AI時代の作家・出版・象徴資本の再編を分析する社会学的基盤。",
         "related_ai_phenomenon":"AI時代の文学場再編"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"場(champ)とハビトゥス",
         "description":"ブルデュー社会学は人類学・文学・社会科学を架橋する中心理論。"}])

add(**C, name_ja="ウィリアムズ「感情の構造」",
    name_en="Williams's structures of feeling",
    name_original="structures of feeling",
    period_key="マルクス主義文学批評期",
    definition="レイモンド・ウィリアムズ(1921-1988)が『マルクス主義と文学』(1977)で提示した中心概念。確立された制度的イデオロギーに先立つ、生きられた経験の構造を捉える批評道具。",
    background="バーミンガム学派文化研究、ホガート文化批評、グラムシ的左派批評。",
    development="現代カルチュラル・スタディーズ、情動論、フェルスキ批評の理論的源泉。",
    historical_context="1970年代英国新左派文化研究期。",
    primary_source_url=WIKI_EN+"Structure_of_feeling",
    primary_source_type="Wikipedia: Structure of feeling",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"感情の構造概念はAI時代に新たに生成される集合的情動を捉える理論的道具となる。",
         "related_ai_phenomenon":"AI時代の集合的情動構造"}])

add(**C, name_ja="ジェイムソン「認知地図」",
    name_en="Jameson's cognitive mapping",
    name_original="cognitive mapping",
    period_key="マルクス主義文学批評期",
    definition="フレドリック・ジェイムソン(1934-2024)が『ポストモダニズム』(1991)で提示した概念。後期資本主義の不可視な全体性を表象する美学的・政治的実践を「認知地図」と呼んだ。",
    background="ルカーチ全体性論、リンチ都市像、ポストモダン地理学。",
    development="ハーヴェイ地理学、ポストモダン文学批評、空間的批評の理論的中核。",
    historical_context="1990年代グローバル資本主義への文化的応答期。",
    primary_source_url=WIKI_EN+"Cognitive_map",
    primary_source_type="Wikipedia: Cognitive map",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"後期資本主義の全体性",
         "description":"認知地図はマルクス主義全体性論をポストモダン地理学と結合する。"}])


# ============================================================
# B: Reader-response / reception (5)
# ============================================================
add(**C, name_ja="イーザー『読書行為』",
    name_en="Iser's The Act of Reading",
    name_original="Der Akt des Lesens",
    period_key="受容理論期",
    definition="ヴォルフガング・イーザー(1926-2007)の主著(1976)。テクストの「不確定性」と読者の「具体化」の相互作用を理論化し、読者反応理論の体系を確立した。",
    background="コンスタンツ学派、現象学的解釈学、インガルデンの文学的具体化論。",
    development="ヤウス受容美学と並ぶドイツ受容理論の双璧、米国読者反応批評の理論的基盤。",
    historical_context="1970年代ドイツ受容理論成熟期。",
    primary_source_url=WIKI_EN+"Wolfgang_Iser",
    primary_source_type="Wikipedia: Wolfgang Iser",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"読書行為論は、AIが読者として動作する状況での具体化過程を理論化する基盤となる。",
         "related_ai_phenomenon":"AI読者による具体化と不確定性処理"}])

add(**C, name_ja="ブライク主観批評",
    name_en="Bleich's subjective criticism",
    name_original="subjective criticism",
    period_key="受容理論期",
    definition="デイヴィッド・ブライクが『主観批評』(1978)で展開した米国読者反応批評。読者の心理的反応を批評の出発点とし、客観主義批評を批判した。",
    background="コロンビア大学英文学、心理批評、フェミニスト読者論との対話。",
    development="フェミニスト読者反応批評、教育的批評、解釈共同体論への影響。",
    historical_context="1970年代米国読者反応批評の方法論的多様化期。",
    primary_source_url=WIKI_EN+"Reader-response_criticism",
    primary_source_type="Wikipedia: Reader-response criticism",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リファテール『詩の記号論』",
    name_en="Riffaterre's Semiotics of Poetry",
    name_original="Semiotics of Poetry",
    period_key="受容理論期",
    definition="ミカエル・リファテール(1924-2006)の主著(1978)。詩を「ハイポグラム」からの逸脱として捉え、読者の二段階解釈プロセスを理論化した記号論的詩学。",
    background="フランス構造主義、米国受容理論、ヤコブソン詩学の継承。",
    development="記号論的詩学、米国受容理論、現代ナラトロジーへの影響。",
    historical_context="1970年代米仏記号論詩学交流期。",
    primary_source_url=WIKI_EN+"Michael_Riffaterre",
    primary_source_type="Wikipedia: Michael Riffaterre",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"記号論的詩学",
         "description":"リファテール詩学は記号論と詩学を架橋する。"}])

add(**C, name_ja="ハーシュ『解釈の妥当性』",
    name_en="Hirsch's Validity in Interpretation",
    name_original="Validity in Interpretation",
    period_key="受容理論期",
    definition="E. D. ハーシュ(1928-)の主著(1967)。作者意図に基づく解釈の客観的妥当性を擁護し、ニュー・クリティシズムの「意図の誤謬」と読者反応批評を批判した。",
    background="ガダマー解釈学、ニュー・クリティシズム反省、米国保守的人文主義。",
    development="作者意図擁護派、解釈学的論争の中心テキスト、現代著作権論との接続。",
    historical_context="1960年代米国解釈論争期。",
    primary_source_url=WIKI_EN+"E._D._Hirsch_Jr.",
    primary_source_type="Wikipedia: E. D. Hirsch Jr.",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者意図中心の妥当性論は、AI生成テキストの作者意図概念を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI生成テキストの作者意図問題"}])

add(**C, name_ja="トンプキンズ編『読者反応批評』",
    name_en="Tompkins (ed.) Reader-Response Criticism",
    name_original="Reader-Response Criticism: From Formalism to Post-Structuralism",
    period_key="受容理論期",
    definition="ジェイン・トンプキンズが編んだ読者反応批評アンソロジー(1980)。フィッシュ、ホランド、イーザー、カラーらの主要論文を収録し、英米読者反応批評の正典化に貢献した。",
    background="米国フェミニスト批評、構造主義以後の批評理論。",
    development="米国大学院での読者反応批評教育の標準アンソロジー。",
    historical_context="1980年米国批評理論の正典化期。",
    primary_source_url=WIKI_EN+"Reader-response_criticism",
    primary_source_type="Wikipedia: Reader-response criticism",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: Psychoanalytic literary criticism (5)
# ============================================================
add(**C, name_ja="カルース『取り返しのつかない経験』",
    name_en="Caruth's Unclaimed Experience",
    name_original="Unclaimed Experience: Trauma, Narrative, and History",
    period_key="精神分析文学批評期",
    definition="キャシー・カルースの主著(1996)。フロイト・ラカンを継承し、トラウマを「経験不可能な経験」として理論化、文学・歴史・精神分析を架橋する20世紀末トラウマ理論の中核。",
    background="イェール大学脱構築派、ホロコースト研究、フロイト『快感原則の彼岸』の再読。",
    development="トラウマ理論、戦争文学批評、フェルマン証言論との対話、現代ポストコロニアル批評への影響。",
    historical_context="1990年代米国トラウマ理論成熟期。",
    primary_source_url=WIKI_EN+"Cathy_Caruth",
    primary_source_type="Wikipedia: Cathy Caruth",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"トラウマと物語の関係論は、AI生成物語が経験不可能性をどう扱うかを理論化する基盤。",
         "related_ai_phenomenon":"AI生成トラウマ物語の倫理"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"トラウマと記憶",
         "description":"カルースのトラウマ論は人類学的記憶研究と接続する。"}])

add(**C, name_ja="アブラハム/トロック「クリプト」",
    name_en="Abraham/Torok's crypt",
    name_original="la crypte",
    period_key="精神分析文学批評期",
    definition="ニコラ・アブラハム(1919-1975)とマリア・トロック(1925-1998)の精神分析理論。喪の不可能な対象が無意識内に「クリプト(墓室)」として閉じ込められる構造を理論化、デリダに継承された。",
    background="ハンガリー精神分析、フランス・ラカン派以後、家族トラウマの世代間継承研究。",
    development="デリダ『フォール』、ポストコロニアル・トラウマ批評、世代間トラウマ理論の中核。",
    historical_context="1970年代フランス精神分析文学批評期。",
    primary_source_url=WIKI_EN+"Nicolas_Abraham",
    primary_source_type="Wikipedia: Nicolas Abraham",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"喪と他者性",
         "description":"クリプト論はデリダ脱構築哲学と精神分析を架橋する。"}])

add(**C, name_ja="ブルックス『メロドラマ的想像力』",
    name_en="Brooks's The Melodramatic Imagination",
    name_original="The Melodramatic Imagination",
    period_key="精神分析文学批評期",
    definition="ピーター・ブルックスの主著(1976)。バルザック・ジェイムズ・メロドラマを精神分析的に分析し、近代の「道徳的隠秘」の表象様式としてメロドラマ的想像力を理論化した。",
    background="イェール大学比較文学、フランス精神分析、19世紀フランス小説研究。",
    development="メロドラマ研究、感情批評、ハリウッド映画研究、現代情動論への影響。",
    historical_context="1970年代米国精神分析文学批評期。",
    primary_source_url=WIKI_EN+"Peter_Brooks_(literary_critic)",
    primary_source_type="Wikipedia: Peter Brooks",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ライト『精神分析批評』",
    name_en="Wright's Psychoanalytic Criticism",
    name_original="Psychoanalytic Criticism: Theory in Practice",
    period_key="精神分析文学批評期",
    definition="エリザベス・ライトの主著(1984)。フロイト派・対象関係派・ラカン派・ポスト構造主義派の精神分析批評を体系的に分類した英国精神分析批評の標準教科書。",
    background="英国ロンドン大学、英国対象関係学派、フランス・ラカン派の英米紹介。",
    development="英国大学院での精神分析批評教育の標準教科書、英米批評理論教育の中核。",
    historical_context="1980年代英国精神分析批評教育期。",
    primary_source_url=WIKI_EN+"Psychoanalytic_literary_criticism",
    primary_source_type="Wikipedia: Psychoanalytic literary criticism",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="フェルマン「証言の危機」",
    name_en="Felman's crisis of witnessing",
    name_original="crisis of witnessing",
    period_key="精神分析文学批評期",
    definition="ショシャナ・フェルマンとドリ・ローブが共著『証言』(1992)で展開した概念。ホロコースト証言を精神分析的・文学的に分析し、現代の証言文学批評の理論的基盤を確立した。",
    background="イェール大学ラカン派、ホロコースト研究、米国精神分析文学批評。",
    development="トラウマ研究、戦争文学批評、ポストコロニアル証言批評、現代記憶研究への影響。",
    historical_context="1990年代米国ホロコースト・トラウマ研究期。",
    primary_source_url=WIKI_EN+"Shoshana_Felman",
    primary_source_type="Wikipedia: Shoshana Felman",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"証言の危機論は、AI生成証言の真正性問題を理論化する精神分析的基盤となる。",
         "related_ai_phenomenon":"AI生成証言の倫理と真正性"}])


# ============================================================
# D: Narratology post-classical (6)
# ============================================================
add(**C, name_ja="ハーマン『物語論の基礎』",
    name_en="Herman's Basic Elements of Narrative",
    name_original="Basic Elements of Narrative",
    period_key="古典・古典後ナラトロジー期",
    definition="デイヴィッド・ハーマンの主著(2009)。認知物語論を体系化し、ストーリーワールド・経験性・状況依存性を物語の基本要素として理論化した21世紀ナラトロジーの中核。",
    background="米国オハイオ大学、認知科学的物語論、古典ナラトロジー以後の認知転回。",
    development="ストーリーワールド理論、認知物語論、現代トランスメディア物語論の理論的基盤。",
    historical_context="2000年代認知ナラトロジー成熟期。",
    primary_source_url=WIKI_EN+"David_Herman_(narratologist)",
    primary_source_type="Wikipedia: David Herman",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"認知物語論はAI生成ストーリーワールドの認知的構造を分析する理論的基盤。",
         "related_ai_phenomenon":"AI生成ストーリーワールドの認知分析"}])

add(**C, name_ja="ライアン・トランスメディア物語論",
    name_en="Ryan's transmedial narratology",
    name_original="transmedial narratology",
    period_key="古典・古典後ナラトロジー期",
    definition="マリー=ロール・ライアンが『物語としての世界、メディアとしての世界』(2014)等で展開した理論。物語を媒体横断的に分析する理論枠組みを提示、デジタル物語論の中核となった。",
    background="米国デジタル物語論、メディア研究、ハイパーテクスト理論。",
    development="デジタルゲーム物語論、トランスメディア・ストーリーテリング研究、AI物語論の理論的基盤。",
    historical_context="2010年代米国デジタル物語論成熟期。",
    primary_source_url=WIKI_EN+"Marie-Laure_Ryan",
    primary_source_type="Wikipedia: Marie-Laure Ryan",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"トランスメディア物語論はAI生成物語が複数媒体を横断する状況を理論化する基盤。",
         "related_ai_phenomenon":"AI生成トランスメディア物語"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"AI物語生成",
         "description":"トランスメディア物語論はAI物語生成研究と理論的に接続する。"}])

add(**C, name_ja="ヤーン焦点化再検討",
    name_en="Jahn's revisited focalization",
    name_original="focalization revisited",
    period_key="古典・古典後ナラトロジー期",
    definition="マンフレッド・ヤーン(1959-)が1990-2000年代に展開した焦点化理論再検討。ジュネット焦点化論を認知科学的に拡張、ウィンドウ・フィルター・スロットの三層モデルを提示した。",
    background="ドイツ・ケルン大学、認知ナラトロジー、ジュネット理論の再検討。",
    development="認知物語論、ストーリーワールド理論、現代物語論教育の標準モデル。",
    historical_context="1990-2000年代ドイツ認知ナラトロジー期。",
    primary_source_url=WIKI_EN+"Focalisation",
    primary_source_type="Wikipedia: Focalisation",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マルゴリン・キャラクター理論",
    name_en="Margolin's character theory",
    name_original="character theory",
    period_key="古典・古典後ナラトロジー期",
    definition="ウリ・マルゴリンが1980-2000年代に展開したナラトロジー的キャラクター理論。フィクション人物を可能世界論・認知科学・テキスト機能論から複層的に理論化した。",
    background="イスラエル・テル・アヴィヴ大学、可能世界論、ロシア・フォルマリズム後継研究。",
    development="認知ナラトロジー、フィクション人物研究、ザンシャイン・キャラクター心理批評の理論的基盤。",
    historical_context="1980-2000年代ナラトロジー的キャラクター研究期。",
    primary_source_url=WIKI_EN+"Character_(arts)",
    primary_source_type="Wikipedia: Character",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ニュンニング信頼できない語り手",
    name_en="Nünning's unreliable narrator",
    name_original="unreliable narrator",
    period_key="古典・古典後ナラトロジー期",
    definition="アンスガー・ニュンニング(1959-)が1990-2000年代に展開した信頼できない語り手の認知的再定義。ブースの修辞的定義を認知科学的に拡張、読者の認知的不一致として理論化。",
    background="ドイツ・ギーセン大学、認知ナラトロジー、ブース修辞批評の継承。",
    development="認知物語論、信頼性研究、現代ナラトロジー教育の標準モデル。",
    historical_context="1990-2000年代ドイツ認知ナラトロジー期。",
    primary_source_url=WIKI_EN+"Unreliable_narrator",
    primary_source_type="Wikipedia: Unreliable narrator",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"信頼できない語り手の認知論は、AI語り手の信頼性判定を理論化する基盤となる。",
         "related_ai_phenomenon":"AI語り手の信頼性問題"}])

add(**C, name_ja="シュミット出来事性理論",
    name_en="Schmid's eventfulness theory",
    name_original="Ereignishaftigkeit",
    period_key="古典・古典後ナラトロジー期",
    definition="ヴォルフ・シュミット(1944-)の『物語論』(2010)で展開された出来事性理論。物語の最小単位「出来事」の段階性(関連性・予測不可能性・不可逆性等)を理論化したドイツ・ナラトロジー。",
    background="ドイツ・ハンブルク大学、ロシア・フォルマリズム継承、独露ナラトロジー対話。",
    development="ドイツ認知ナラトロジー、現代物語論教育の標準理論、欧州ナラトロジー研究の基盤。",
    historical_context="2000-2010年代ドイツ・ナラトロジー期。",
    primary_source_url=WIKI_EN+"Wolf_Schmid",
    primary_source_type="Wikipedia: Wolf Schmid",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# E: Book history / material text (4)
# ============================================================
add(**C, name_ja="ジュネット『パラテクスト』",
    name_en="Genette's Paratexts",
    name_original="Seuils",
    period_key="書物史・受容史期",
    definition="ジェラール・ジュネット(1930-2018)の主著(1987)。書物の本文を取り囲む周縁的要素(タイトル・序文・注・装丁等)を「パラテクスト」と命名し、その機能を体系的に理論化した書物批評の古典。",
    background="フランス構造主義、ジュネット『物語のディスクール』後の物質的テクスト論への展開。",
    development="書物史、編集学、デジタル・パラテクスト研究、現代物質的批評の中核理論。",
    historical_context="1980年代フランス書物批評期。",
    primary_source_url=WIKI_EN+"Paratext",
    primary_source_type="Wikipedia: Paratext",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"パラテクスト論はAI生成書物の周縁的要素(プロンプト・メタデータ等)を理論化する基盤。",
         "related_ai_phenomenon":"AI生成書物のパラテクスト"}])

add(**C, name_ja="グリーサム『テクスト学』",
    name_en="Greetham's Textual Scholarship",
    name_original="Textual Scholarship: An Introduction",
    period_key="書物史・受容史期",
    definition="デイヴィッド・グリーサム(1941-2020)の主著(1994)。書誌学・編集学・テクスト批評を体系的に統合した英米編集学の標準教科書、現代物質的批評の理論的基盤。",
    background="ニューヨーク市立大学院、書誌学・編集学伝統、マッケンジー継承。",
    development="現代編集学、デジタル編集論、物質的批評教育の標準テキスト。",
    historical_context="1990年代英米編集学成熟期。",
    primary_source_url=WIKI_EN+"David_Greetham",
    primary_source_type="Wikipedia: David Greetham",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="スタリーブラス物質的テクスト批評",
    name_en="Stallybrass's material text criticism",
    name_original="material text criticism",
    period_key="書物史・受容史期",
    definition="ピーター・スタリーブラス(1947-)が1990-2000年代に展開した物質的テクスト批評。シェイクスピア時代の書物・印刷・読書実践を物質文化史的に分析、ペンシルベニア大学書物史拠点を主導した。",
    background="ペンシルベニア大学英文学、英国ルネサンス研究、書物史研究。",
    development="現代物質的書物史、近代英米書物文化研究、デジタル時代の書物批評。",
    historical_context="1990-2000年代米国書物史成熟期。",
    primary_source_url=WIKI_EN+"Peter_Stallybrass",
    primary_source_type="Wikipedia: Peter Stallybrass",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ジョンス『印刷の本性』",
    name_en="Johns's The Nature of the Book",
    name_original="The Nature of the Book",
    period_key="書物史・受容史期",
    definition="エイドリアン・ジョンスの主著(1998)。近世英国印刷文化の物質性・社会性を実証的に分析し、印刷の本物性が社会的に構築されたことを論じた書物史の重要著作。",
    background="シカゴ大学科学史、近代英国書物史、エリザベス・アイゼンスタイン論争。",
    development="近代書物史、科学史、現代物質的批評、デジタル時代の本物性論の理論的基盤。",
    historical_context="1990年代末英米書物史論争期。",
    primary_source_url=WIKI_EN+"Adrian_Johns",
    primary_source_type="Wikipedia: Adrian Johns",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"印刷の本性とAI生成物の真正性",
         "description":"ジョンス印刷史はAI生成物の真正性問題と歴史的に対比される。"}])


# ============================================================
# F: Affect / cognitive / post-critique (6)
# ============================================================
add(**C, name_ja="バーラント「親密な公共性」",
    name_en="Berlant's intimate publics",
    name_original="intimate publics",
    period_key="情動・認知・ポスト批評期",
    definition="ローレン・バーラントが『女の不満』(2008)等で展開した概念。大衆メディア・女性文化が形成する情動的共同体を「親密な公共性」として理論化、現代米国情動批評の中核概念。",
    background="シカゴ大学英文学、フェミニスト情動研究、米国大衆文化研究。",
    development="情動公共圏研究、現代女性文化批評、デジタル親密性研究の理論的基盤。",
    historical_context="2000年代米国情動研究成熟期。",
    primary_source_url=WIKI_EN+"Lauren_Berlant",
    primary_source_type="Wikipedia: Lauren Berlant",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"親密な公共性概念は、AIが媒介する情動的共同体を理論化する基盤となる。",
         "related_ai_phenomenon":"AI媒介の親密な公共性"}])

add(**C, name_ja="クヴェコヴィッチ『感情のアーカイヴ』",
    name_en="Cvetkovich's An Archive of Feelings",
    name_original="An Archive of Feelings",
    period_key="情動・認知・ポスト批評期",
    definition="アン・クヴェコヴィッチの主著(2003)。レズビアン公共圏のトラウマ・情動を「感情のアーカイヴ」として理論化、フェミニスト・クィア情動研究の中核著作。",
    background="テキサス大学英文学、クィア理論、フェミニスト・トラウマ研究。",
    development="クィア情動研究、フェミニスト・アーカイヴ理論、現代パーソナル・アーカイヴ研究の基盤。",
    historical_context="2000年代米国クィア情動研究期。",
    primary_source_url=WIKI_EN+"Ann_Cvetkovich",
    primary_source_type="Wikipedia: Ann Cvetkovich",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="スチュアート『日常の情動』",
    name_en="Stewart's Ordinary Affects",
    name_original="Ordinary Affects",
    period_key="情動・認知・ポスト批評期",
    definition="キャスリーン・スチュアートの主著(2007)。日常生活の微細な情動を散文詩的に記述する人類学的・批評的方法論、現代情動人類学・批評の中核著作。",
    background="テキサス大学人類学、情動研究、エスノグラフィー的批評。",
    development="情動人類学、批評的散文の方法論、現代日常性研究の理論的基盤。",
    historical_context="2000年代米国情動人類学期。",
    primary_source_url=WIKI_EN+"Kathleen_Stewart",
    primary_source_type="Wikipedia: Kathleen Stewart",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"情動人類学",
         "description":"スチュアート方法論は人類学と文学批評を架橋する。"}])

add(**C, name_ja="ギャラガー歴史化形式論",
    name_en="Gallagher's historicizing form",
    name_original="historicizing form",
    period_key="情動・認知・ポスト批評期",
    definition="キャサリン・ギャラガー(1945-)が2000-2010年代に展開した形式論。ニュー・ヒストリシズム以後、文学形式そのものを歴史的に構築されたものとして分析する米国批評。",
    background="UCバークレー英文学、ニュー・ヒストリシズム、19世紀英国小説研究。",
    development="ニュー・フォルマリズム、現代歴史化形式論、米国批評理論の方法論的基盤。",
    historical_context="2000-2010年代米国批評理論期。",
    primary_source_url=WIKI_EN+"Catherine_Gallagher",
    primary_source_type="Wikipedia: Catherine Gallagher",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="モイ『普通の言葉のテキスト』",
    name_en="Moi's ordinary language criticism",
    name_original="ordinary language criticism",
    period_key="情動・認知・ポスト批評期",
    definition="トリル・モイ(1953-)が『言葉を改めて書く』(2017)で展開した批評。ウィトゲンシュタイン・カヴェル日常言語哲学に基づき、批評の哲学的再生を提唱、ポスト批評運動と並走する。",
    background="デューク大学比較文学、フェミニスト批評、日常言語哲学。",
    development="現代ポスト批評運動、日常言語批評、フェミニスト批評の方法論的基盤。",
    historical_context="2010年代米国ポスト批評期。",
    primary_source_url=WIKI_EN+"Toril_Moi",
    primary_source_type="Wikipedia: Toril Moi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"日常言語批評は、AI生成テキストと日常言語の関係を理論化する哲学的基盤となる。",
         "related_ai_phenomenon":"AI生成テキストと日常言語"}])

add(**C, name_ja="アンカー/フェルスキ『批評と感情の改革』",
    name_en="Anker/Felski Critique and Postcritique",
    name_original="Critique and Postcritique",
    period_key="情動・認知・ポスト批評期",
    definition="エリザベス・アンカーとリタ・フェルスキ編のアンソロジー(2017)。ポスト批評運動の主要論文を収録し、20世紀「症候読み」批評の歴史化と再評価を体系的に提示した。",
    background="ヴァージニア大学英文学、ポスト批評運動、ラトゥールANT批評。",
    development="現代ポスト批評運動の正典化、米国大学院批評理論教育の標準アンソロジー。",
    historical_context="2010年代米国ポスト批評運動成熟期。",
    primary_source_url=DUKE+"critique-and-postcritique",
    primary_source_type="Duke UP: Critique and Postcritique",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: Digital / quantitative DH (4)
# ============================================================
add(**C, name_ja="パイパー『列挙』",
    name_en="Piper's Enumerations",
    name_original="Enumerations: Data and Literary Study",
    period_key="デジタル・量的文学研究期",
    definition="アンドリュー・パイパーの主著(2018)。文学を量的データとして分析する方法論を体系的に提示、デジタル文学研究の方法論的基盤を確立した21世紀DHの中核著作。",
    background="マギル大学比較文学、デジタル人文学、計算文学批評。",
    development="現代計算文学批評、AIによる文学分析、デジタル文学研究教育の標準テキスト。",
    historical_context="2010年代デジタル文学研究成熟期。",
    primary_source_url=WIKI_EN+"Digital_humanities",
    primary_source_type="Wikipedia: Digital humanities",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"量的文学研究は、AI時代の文学分析方法論の理論的基盤を提供する。",
         "related_ai_phenomenon":"AIによる量的文学分析"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"計算文学分析",
         "description":"パイパー量的文学研究はAI文学分析と直結する。"}])

add(**C, name_ja="アルジー=ヒューイット・スタンフォード文学ラボ",
    name_en="Algee-Hewitt Stanford Literary Lab",
    name_original="Stanford Literary Lab",
    period_key="デジタル・量的文学研究期",
    definition="マーク・アルジー=ヒューイットらが主導するスタンフォード文学ラボ(2010-)の批評実践。モレッティ遠読を継承し、計算文学批評のパンフレット・シリーズを展開した。",
    background="スタンフォード大学、モレッティ計算批評、デジタル人文学研究拠点。",
    development="現代計算文学批評、AI文学分析、デジタル文学批評教育の中核拠点。",
    historical_context="2010年代米国DH研究拠点形成期。",
    primary_source_url=WIKI_EN+"Stanford_Literary_Lab",
    primary_source_type="Wikipedia: Stanford Literary Lab",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ロング/ソー計算文学批評",
    name_en="Long/So computational criticism",
    name_original="computational literary criticism",
    period_key="デジタル・量的文学研究期",
    definition="ホイット・ロングとリチャード・ジーン・ソーが2010-2020年代に展開した計算文学批評。機械学習・テキストマイニングで小説・詩を分析する米国デジタル文学研究の方法論。",
    background="シカゴ大学・ダートマス大学、機械学習文学批評、計算詩学。",
    development="現代AI文学分析、計算詩学、デジタル文学批評教育の方法論的基盤。",
    historical_context="2010-2020年代米国計算文学批評期。",
    primary_source_url=WIKI_EN+"Distant_reading",
    primary_source_type="Wikipedia: Distant reading",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リウ『デジタル人文学のイデオロギー』",
    name_en="Liu's ideologies of DH",
    name_original="ideologies of digital humanities",
    period_key="デジタル・量的文学研究期",
    definition="アラン・リウ(1953-)が2012-2020年代に展開したDH批判理論。デジタル人文学の政治的・イデオロギー的位置を批判的に分析し、DHの自己反省的批評を主導した。",
    background="UCサンタバーバラ大学、デジタル人文学、批判理論。",
    development="現代DH批判理論、デジタル文学批評の自己反省、AI時代のDH倫理論の理論的基盤。",
    historical_context="2010-2020年代DH自己反省期。",
    primary_source_url=WIKI_EN+"Alan_Liu",
    primary_source_type="Wikipedia: Alan Liu",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"DH批判理論は、AI時代の文学研究のイデオロギー的位置を分析する基盤となる。",
         "related_ai_phenomenon":"AI文学研究のイデオロギー批判"}])


# ============================================================
# H: Recent material/category criticism (4)
# ============================================================
add(**C, name_ja="ガイ『ギミックの理論』",
    name_en="Ngai's Theory of the Gimmick",
    name_original="Theory of the Gimmick",
    period_key="価値・現代物質批評期",
    definition="シアン・ガイの主著(2020)。資本主義美学的カテゴリー「ギミック」を、労働・時間・価値の不調和として理論化、21世紀価値・カテゴリー批評の中核著作。",
    background="シカゴ大学英文学、マルクス主義美学、ガイの先行著作『興味深さ』『キュート』との連続性。",
    development="現代価値批評、カテゴリー美学、ポスト批評運動と並走する21世紀理論。",
    historical_context="2020年代米国カテゴリー批評期。",
    primary_source_url=WIKI_EN+"Sianne_Ngai",
    primary_source_type="Wikipedia: Sianne Ngai",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"ギミック理論は、AI生成物が「ギミック」化する状況を批評的に理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成物のギミック化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"資本主義美学カテゴリー",
         "description":"ガイのカテゴリー批評はマルクス主義美学を21世紀的に再構築する。"}])

add(**C, name_ja="アハメド『クィア現象学』",
    name_en="Ahmed's Queer Phenomenology",
    name_original="Queer Phenomenology",
    period_key="価値・現代物質批評期",
    definition="サラ・アハメド(1969-)の主著(2006)。クィア理論と現象学を統合し、性的・人種的・空間的志向性を理論化、現代クィア批評・空間批評の中核著作。",
    background="ロンドン大学・ゴールドスミス、フェミニスト現象学、クィア理論。",
    development="現代クィア空間批評、フェミニスト現象学、ポストコロニアル空間論との接続。",
    historical_context="2000年代英国クィア批評期。",
    primary_source_url=WIKI_EN+"Sara_Ahmed",
    primary_source_type="Wikipedia: Sara Ahmed",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"クィア現象学",
         "description":"アハメドはクィア理論と現象学を架橋する。"}])

add(**C, name_ja="バーラント『女の不満』",
    name_en="Berlant's Female Complaint",
    name_original="The Female Complaint",
    period_key="価値・現代物質批評期",
    definition="ローレン・バーラントの主著(2008)。米国大衆女性文化(センチメンタル小説・大衆映画)を「女の不満」のジャンルとして理論化、フェミニスト情動批評の中核著作。",
    background="シカゴ大学英文学、フェミニスト情動批評、米国センチメンタル文学研究。",
    development="現代フェミニスト批評、情動公共圏研究、女性文化批評の方法論的基盤。",
    historical_context="2000年代米国フェミニスト情動批評期。",
    primary_source_url=DUKE+"the-female-complaint",
    primary_source_type="Duke UP: The Female Complaint",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="チェン『オーナメンタリズム』",
    name_en="Cheng's Ornamentalism",
    name_original="Ornamentalism",
    period_key="価値・現代物質批評期",
    definition="アン・アンリン・チェン(1965-)の主著(2018)。アジア女性身体の「オーナメンタル化(装飾化)」を理論化、人種・ジェンダー・物質性を架橋する21世紀アジア系米国批評の中核著作。",
    background="プリンストン大学英文学、アジア系米国批評、人種・物質性研究。",
    development="現代アジア系米国批評、人種ジェンダー物質性研究、ポストコロニアル批評の理論的基盤。",
    historical_context="2010年代米国アジア系批評期。",
    primary_source_url=WIKI_EN+"Anne_Anlin_Cheng",
    primary_source_type="Wikipedia: Anne Anlin Cheng",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"オーナメンタリズム論は、AI生成のアジア女性身体表象を批評する理論的基盤となる。",
         "related_ai_phenomenon":"AI生成アジア女性身体表象"}])


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
        print(f"[c34-retry40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c34-retry40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
