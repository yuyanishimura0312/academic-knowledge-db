"""LIT-DB Phase 2 Wave 13 — C34: Literary Theory / Criticism (+60 concepts).

Subfield: lit_theory (id=22), region='横断' (theory is trans-regional).
Adds 60 NEW concepts (existing 70 → target 130). Coverage:
  A: Marxist criticism (Lukács, Goldmann, Macherey, Eagleton, Jameson,
     Williams, Negri/Hardt) — 8
  B: Reader-response / reception (Iser implied reader, Rosenblatt,
     Fish, Jauss, Eco model reader, Bleich, Holland, Riffaterre) — 8
  C: Psychoanalytic literary criticism (Freud Uncanny applied,
     Lacan Mirror Stage applied, Kristeva semiotic/symbolic, Cixous
     écriture féminine theory, Bonaparte Poe, Bersani, Brooks Plot) — 8
  D: Narratology (Genette Discours, Bal, Stanzel, Chatman, Rimmon-Kenan,
     Cohn transparent minds, Phelan rhetorical, Fludernik natural,
     storyworld) — 9
  E: Reception studies & book history (Darnton circuit, McKenzie
     sociology of texts, Chartier, Manguel) — 4
  F: Affect / cognitive / post-critique (Massumi affect, Sedgwick
     reparative, Felski uses + limits, Hogan affective narrato,
     Zunshine, Vermeule, Boyd, Best/Marcus surface, Ngai, Cheng) — 11
  G: Digital / quantitative / DH (Moretti distant, Jockers, Underwood,
     Drucker, Bode, computational poetics) — 6
  H: Recent material/value criticism (Schalkwyk, Bewes, Brooks reading
     for plot revisited, post-critique movement, weak theory) — 6

Theory-heavy → 60% primary (theory chapters/books), 40% secondary academic
syntheses. fourth_transform_tags >= 25; cross_domain to PT/PHIL/AN/AI-Dev >= 20.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("マルクス主義文学批評期", "Marxist Literary Criticism", 1920, 1990,
     "ルカーチ『小説の理論』(1916)・『歴史と階級意識』(1923)を起点に、フランクフルト学派、ルイ・アルチュセール、フレドリック・ジェイムソン、レイモンド・ウィリアムズらが展開した社会-経済的文学理論期。"),
    ("受容理論期", "Reader-Response / Reception Theory", 1965, 1995,
     "1960年代後半から1990年代にかけてコンスタンツ学派（ヤウス、イーザー）、米国読者反応批評（フィッシュ、ローゼンブラット、ホランド）、エコ・モデル読者論が展開した時期。"),
    ("精神分析文学批評期", "Psychoanalytic Literary Criticism",
     1900, 2010,
     "フロイト『不気味なもの』(1919)、ボナパルトのポー研究(1933)、ラカンの諸セミネール(1953-)、クリステヴァ・シクスゥの第二期理論を含む精神分析文学批評の時期。"),
    ("古典・古典後ナラトロジー期", "Classical & Post-Classical Narratology",
     1972, 2015,
     "ジュネット『物語のディスクール』(1972)に始まる古典ナラトロジーから、コーン、フェラン、ハーマン、フルダニクら認知・修辞・自然物語論への展開期。"),
    ("書物史・受容史期", "Book History & History of Reading",
     1979, 2015,
     "ロバート・ダーントン「コミュニケーション・サーキット」(1982)、D. F. マッケンジー『書誌学とテクストの社会学』(1986)、ロジェ・シャルチエの読書実践史を中核とする書物史期。"),
    ("情動・認知・ポスト批評期", "Affect, Cognitive, Post-Critique",
     2000, 2025,
     "ブライアン・マッスミの情動論、セジウィックのリパラティブ・リーディング、リタ・フェルスキ『批評の限界』(2015)、ベスト/マーカスのサーフェス・リーディング(2009)を中核とする21世紀理論期。"),
    ("デジタル・量的文学研究期", "Digital / Quantitative Literary Studies",
     2000, 2025,
     "フランコ・モレッティ『遠読』(2000-2013)、マシュー・ジョッカーズ『マクロアナリシス』(2013)、テッド・アンダーウッドの機械学習批評を中核とする時期。"),
    ("価値・現代物質批評期", "Value & Recent Material Criticism",
     2010, 2025,
     "シアン・ガイのカテゴリー批評、ピーター・ブルックスの読み直し、ベウィスら現代の物質的・倫理的批評の発展期。"),
]

GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
ARCH = "https://archive.org/details/"
JSTOR = "https://www.jstor.org/"
MARX = "https://www.marxists.org/"
PUP = "https://press.princeton.edu/"
OXF = "https://academic.oup.com/"
DUKE = "https://read.dukeupress.edu/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_theory", region="横断", original_script="roman")


# ============================================================
# A: Marxist literary criticism (8)
# ============================================================
add(**C, name_ja="ルカーチ『小説の理論』",
    name_en="Lukács's The Theory of the Novel",
    name_original="Die Theorie des Romans",
    period_key="マルクス主義文学批評期",
    definition="ジェルジ・ルカーチ（1885-1971）が1916年に発表した小説論の古典。「小説は神に見捨てられた世界の叙事詩」と定義し、ホメロス的叙事詩の有機的全体性喪失後の近代を、抽象的理想主義（ドン・キホーテ的小説）／浪漫的幻滅小説（『感情教育』）／総合（『ヴィルヘルム・マイスター』）の三類型として体系化した。マルクス主義文学批評の出発点となった。",
    background="第一次大戦下のヘーゲル左派的歴史哲学とドストエフスキー研究の挫折。ジンメル門下の文化哲学的小説論。",
    development="後年ルカーチ自身がマルクス主義に転向後にこの著を「ロマン主義的反資本主義」として自己批判するが、ルシアン・ゴルドマン、フランコ・モレッティに継承された。",
    historical_context="第一次大戦中の中央ヨーロッパ知識人の歴史哲学的危機。",
    primary_source_url=ARCH+"theoryofnovelhis0000luka",
    primary_source_type="Internet Archive: Theory of the Novel (English ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"ルカーチの「神に見捨てられた世界の叙事詩」としての小説定義は、AI生成物語が「全体性の喪失」をさらに加速する状況を理論化する古典的参照点となる。",
         "related_ai_phenomenon":"AI生成物語における全体性喪失の加速"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ヘーゲル歴史哲学と文学",
         "description":"ルカーチ『小説の理論』はヘーゲル歴史哲学を文学形式論に翻訳した古典。"}])

add(**C, name_ja="ルカーチ『歴史と階級意識』の文学的射程",
    name_en="Lukács's History and Class Consciousness (literary reach)",
    name_original="Geschichte und Klassenbewußtsein",
    period_key="マルクス主義文学批評期",
    definition="ルカーチが1923年に発表したマルクス主義哲学の古典。「物象化（Verdinglichung）」概念によってマルクス商品論を文化全体に拡張し、ブルジョワ意識のアンチノミーを分析した。直接の文学論ではないが、後のフランクフルト学派、ジェイムソン、後期ルカーチ自身のリアリズム理論の哲学的基盤として、20世紀マルクス主義文学批評の核心テキストとなった。",
    background="ハンガリー・ソヴェト共和国(1919)挫折後の亡命期、ヘーゲル『精神現象学』のマルクス主義的再読。",
    development="アドルノ・ホルクハイマー文化産業論、ジェイムソン『政治的無意識』、ハーバーマスへの哲学的影響を残した。",
    historical_context="1920年代中央ヨーロッパの革命的危機と、西欧マルクス主義の理論的成立期。",
    primary_source_url=MARX+"archive/lukacs/works/history/",
    primary_source_type="Marxists.org: History and Class Consciousness",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"物象化と疎外",
         "description":"物象化概念はヘーゲル疎外論をマルクス商品論と統合した20世紀社会哲学の中心概念。"}])

add(**C, name_ja="ゴルドマン発生論的構造主義",
    name_en="Goldmann's genetic structuralism",
    name_original="structuralisme génétique",
    period_key="マルクス主義文学批評期",
    definition="ルシアン・ゴルドマン（1913-1970）が『隠れたる神』(1956)、『小説の社会学』(1964)で展開した文学社会学。文学作品を社会集団の「世界観（vision du monde）」の構造的等価物として読む方法を体系化し、パスカル・ラシーヌをジャンセニスムの法服貴族の世界観の表現として、また小説形式を市場経済の構造的相同物として分析した。",
    background="ルカーチ『小説の理論』の継承、ピアジェ発生論的構造主義との接続、フランス構造主義への並行的展開。",
    development="フランクフルト学派、ピエール・ブルデューの文学場理論、フランコ・モレッティの世界システム小説論に影響を残した。",
    historical_context="戦後フランスにおけるマルクス主義文学社会学の制度的成立期。",
    primary_source_url=WIKI_EN+"Lucien_Goldmann",
    primary_source_type="Wikipedia: Lucien Goldmann",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"発生論的構造主義と世界観",
         "description":"ゴルドマン発生論的構造主義はピアジェ発生認識論とルカーチ意識形態論をつなぐ20世紀社会哲学の中核。"}])

add(**C, name_ja="マシュレ「文学的生産の理論」",
    name_en="Macherey's A Theory of Literary Production",
    name_original="Pour une théorie de la production littéraire",
    period_key="マルクス主義文学批評期",
    definition="ピエール・マシュレ（1938- ）が1966年に発表したアルチュセール派文学論。文学作品をイデオロギーを「加工する」生産物として捉え、その「沈黙」「裂け目」「不在」が作品のイデオロギー的限界を露わにすると主張した。バルザック、ジュール・ヴェルヌ、トルストイの読解を通じて、症候読み（symptomatic reading）の方法論的基盤を文学に確立した。",
    background="ルイ・アルチュセール『資本論を読む』(1965)の症候読み概念の文学への適用、フランス構造主義マルクス主義の興隆。",
    development="テリー・イーグルトン『批評と意識』、フレドリック・ジェイムソン『政治的無意識』に直接継承された。",
    historical_context="1960年代後半フランスの構造主義マルクス主義の隆盛期。",
    primary_source_url=WIKI_EN+"Pierre_Macherey",
    primary_source_type="Wikipedia: Pierre Macherey",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"マシュレの「沈黙・裂け目・不在」読解は、AI生成テキストが学習データのイデオロギー的限界を「症候」として表出する現象を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成テキストにおける学習データの症候的露呈"}])

add(**C, name_ja="イーグルトン『批評とイデオロギー』",
    name_en="Eagleton's Criticism and Ideology",
    name_original="Criticism and Ideology",
    period_key="マルクス主義文学批評期",
    definition="テリー・イーグルトン（1943- ）が1976年に発表したマルクス主義批評の体系書。アルチュセール=マシュレ系統を継承しつつ、文学を「一般生産様式」「文学的生産様式」「一般イデオロギー」「作家のイデオロギー」「美的イデオロギー」の五重の決定として分析する枠組みを提示した。英語圏マルクス主義文学批評の理論的中核。",
    background="1970年代英国ニュー・レフトの文学理論刷新、レイモンド・ウィリアムズ『マルクス主義と文学』との並行。",
    development="イーグルトン自身の『文学とは何か』(1983)、ジェイムソン『政治的無意識』(1981)と並ぶ80年代英米マルクス主義批評の支柱となった。",
    historical_context="1970年代英国文学研究の理論的左派化（『スクリーン』誌・『ニュー・レフト・レビュー』誌の影響期）。",
    primary_source_url=WIKI_EN+"Terry_Eagleton",
    primary_source_type="Wikipedia: Terry Eagleton",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アルチュセール派イデオロギー論",
         "description":"イーグルトン批評は哲学的イデオロギー論の文学批評への応用として横断的に位置づけられる。"}])

add(**C, name_ja="ジェイムソン『政治的無意識』",
    name_en="Jameson's The Political Unconscious",
    name_original="The Political Unconscious",
    period_key="マルクス主義文学批評期",
    definition="フレドリック・ジェイムソン（1934-2024）が1981年に発表したマルクス主義文学理論の体系書。「常に歴史化せよ（Always historicize!）」を綱領とし、文学テクストを社会矛盾に対する「象徴的解決」として、また三層（政治史的・社会的・歴史的）の意味地平で読む方法論を提示した。バルザック、ギッシング、コンラッドの読解で英米批評に深い影響を残した。",
    background="アルチュセール=マシュレ系統と北米学術批評の総合、フランクフルト学派とフランス構造主義の統合的読解。",
    development="ジェイムソン『ポストモダニズム』(1991)、ニュー・ヒストリシズム、世界システム文学批評の理論的祖型となった。",
    historical_context="1980年代米国アカデミック左派文学批評の制度的中核形成期。",
    primary_source_url=WIKI_EN+"The_Political_Unconscious",
    primary_source_type="Wikipedia: The Political Unconscious",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"政治的無意識概念は、AI生成テキストに刻印された学習データの社会的矛盾を「無意識的政治性」として読む批評枠組みの古典的祖型となる。",
         "related_ai_phenomenon":"AI生成テキストの政治的無意識"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI生成テキストのイデオロギー分析",
         "description":"ジェイムソンの政治的無意識概念はAI出力に刻印された社会的矛盾の批判的読解の理論基盤。"}])

add(**C, name_ja="ウィリアムズ『マルクス主義と文学』",
    name_en="Williams's Marxism and Literature",
    name_original="Marxism and Literature",
    period_key="マルクス主義文学批評期",
    definition="レイモンド・ウィリアムズ（1921-1988）が1977年に発表したマルクス主義文学理論の体系書。グラムシ的ヘゲモニー概念を発展させ、「支配的（dominant）／残余的（residual）／生成的（emergent）」文化形態の三分法、「感情の構造（structure of feeling）」概念によって、文化と物質的生産の関係を非還元的に再構成した。文化研究（カルチュラル・スタディーズ）の理論的基盤を確立した。",
    background="バーミンガム現代文化研究センター(1964)、英国ニュー・レフト思潮、ホガート『読み書き能力の効用』との連続性。",
    development="スチュアート・ホール、リチャード・ジョンソン、80年代英米カルチュラル・スタディーズに継承された。",
    historical_context="1970年代英国の階級・文化・教育論議と、ニュー・レフトのマルクス主義刷新運動。",
    primary_source_url=WIKI_EN+"Marxism_and_Literature",
    primary_source_type="Wikipedia: Marxism and Literature",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"感情の構造・文化人類学",
         "description":"ウィリアムズの「感情の構造」概念は文化人類学の生活世界記述と並行する、文化を物質と意味の絡み合いとして捉える枠組み。"}])

add(**C, name_ja="ネグリ／ハート文学論",
    name_en="Negri/Hardt's literary theory",
    name_original="Empire / Multitude",
    period_key="マルクス主義文学批評期",
    definition="アントニオ・ネグリ（1933-2023）とマイケル・ハート（1960- ）が『帝国』(2000)、『マルチチュード』(2004)、『コモンウェルス』(2009)で展開したオートノミスト・マルクス主義に基づく文学・文化論。グローバル資本主義下の「非物質的労働」「コモン」「マルチチュード」の概念によって、現代の言語生産・文学労働を理論化した。",
    background="イタリア・オペライズモ運動、フランス・ポスト構造主義（ドゥルーズ）、米国大学院での共著継続。",
    development="2000年代以降のグローバリゼーション批評、デジタル文学労働論、コモンズ論的文学批評に影響を残した。",
    historical_context="グローバリゼーションと9.11以降の帝国論再興、デジタル資本主義論議の興隆期。",
    primary_source_url=WIKI_EN+"Empire_(Hardt_and_Negri_book)",
    primary_source_type="Wikipedia: Empire (Hardt/Negri)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"非物質的労働概念は、AIによる文学生産がプラットフォーム資本の蓄積機構に組み込まれる現象を理論化する基盤となる。",
         "related_ai_phenomenon":"AI文学生産とプラットフォーム資本主義"}])


# ============================================================
# B: Reader-response / reception (8)
# ============================================================
add(**C, name_ja="イーザー『読書行為』",
    name_en="Iser's The Act of Reading",
    name_original="Der Akt des Lesens",
    period_key="受容理論期",
    definition="ヴォルフガング・イーザー（1926-2007）が1976年に発表した読者反応理論の主著。『内包読者』(1972)で導入した「内包読者（implied reader）」「空所（Leerstelle）」「決定的不在（Unbestimmtheitsstellen）」概念を体系化し、文学作品の意味は読者がテクストの不確定性に応答して構築する過程で生起すると論じた。コンスタンツ受容理論の理論的中核。",
    background="ロマン・インガルデン現象学的文学論、ヤウス受容美学との並行展開、コンスタンツ大学の研究プログラム。",
    development="米国読者反応批評（フィッシュ、ローゼンブラット、ホランド）と並んで、20世紀後半読者論の中核となった。",
    historical_context="1970年代西ドイツの解釈学・現象学の刷新運動とコンスタンツ学派の制度的成立。",
    primary_source_url=WIKI_EN+"Wolfgang_Iser",
    primary_source_type="Wikipedia: Wolfgang Iser",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"イーザーの「読者がテクストの不確定性に応答して意味を構築する」モデルは、AI生成テキストの「無作者性」を読者の意味構築に委ねる現象を理論化する古典的枠組み。",
         "related_ai_phenomenon":"AI生成テキストの読者主導意味構築"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"現象学的解釈学",
         "description":"イーザー読書行為論はインガルデン現象学とガダマー解釈学の文学理論的展開。"}])

add(**C, name_ja="ローゼンブラット交渉理論",
    name_en="Rosenblatt's transactional theory",
    name_original="transactional theory of reading",
    period_key="受容理論期",
    definition="ルイーズ・ローゼンブラット（1904-2005）が『文学探究』(1938)、『読者・テクスト・詩』(1978)で提唱した米国読者反応批評の理論。読書を読者とテクストの「交渉（transaction）」として捉え、「効率的読み（efficient reading／情報抽出）」と「美的読み（aesthetic reading／体験的読み）」の連続体を区別した。米国国語教育に深い影響を与えた。",
    background="ジョン・デューイのプラグマティズム的経験論、コロンビア大学教育学派、米国国語教育の改革運動。",
    development="米国国語教育「リーダーズ・ワークショップ」運動、ジュディス・ラングランドの「読者の地点」概念に継承された。",
    historical_context="米国国語教育における新批評（テクスト中心主義）の支配と、それへの読者中心主義的応答。",
    primary_source_url=WIKI_EN+"Louise_Rosenblatt",
    primary_source_type="Wikipedia: Louise Rosenblatt",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フィッシュ「テクストにあるか」",
    name_en="Fish's Is There a Text in This Class?",
    name_original="Is There a Text in This Class?",
    period_key="受容理論期",
    definition="スタンリー・フィッシュ（1938- ）が1980年に発表した論文集の表題論文・主著。「解釈共同体（interpretive communities）」概念を体系化し、テクストの意味は内在的でも個別読者の自由でもなく、読者が所属する解釈共同体の解釈実践に依存すると主張した。米国読者反応批評の最も急進的なテクスト構成主義の立場。",
    background="新批評・テクスト内在主義への根本批判、フィッシュ自身の17世紀英国文学研究（ミルトン）の方法論的反省。",
    development="ニュー・ヒストリシズム、文学社会学、現代の解釈の社会理論に影響を残した。",
    historical_context="1980年代米国大学英文学科における理論論争の高揚期。",
    primary_source_url=WIKI_EN+"Stanley_Fish",
    primary_source_type="Wikipedia: Stanley Fish",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"解釈共同体概念は、AI時代における「LLM出力の意味」が特定のユーザー共同体の解釈実践に依存する現象を理論化する古典的枠組み。",
         "related_ai_phenomenon":"AI出力の意味解釈とユーザー共同体"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"解釈共同体と文化",
         "description":"フィッシュ解釈共同体概念は人類学的解釈共同体（クリフォード・ギアツの「文化を読む」）と直接的に連続する。"}])

add(**C, name_ja="ヤウス『挑発としての文学史』",
    name_en="Jauss's Literary History as Provocation",
    name_original="Literaturgeschichte als Provokation",
    period_key="受容理論期",
    definition="ハンス＝ロベルト・ヤウス（1921-1997）が1967年コンスタンツ大学就任講演で発表したマニフェスト。「期待の地平（Erwartungshorizont）」概念によって、文学史を作品と歴史的読者の「地平」の交渉過程として再定義した。形式主義・実証主義・マルクス主義の文学史を共に批判し、コンスタンツ受容理論の理論的出発点となった。",
    background="ガダマー解釈学（『真理と方法』1960）、ロシア・フォルマリズムの「文学的進化」概念、フランクフルト学派の文学社会学の総合。",
    development="イーザー読者論と並ぶコンスタンツ学派の双子の支柱となり、その後の歴史化された受容研究の理論的基盤となった。",
    historical_context="1960年代後半西ドイツの大学改革運動と、文学研究の理論的刷新期。",
    primary_source_url=WIKI_DE+"Hans_Robert_Jauß",
    primary_source_type="Wikipedia (DE): Hans Robert Jauß",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エコ「モデル読者」",
    name_en="Eco's model reader",
    name_original="lettore modello",
    period_key="受容理論期",
    definition="ウンベルト・エコ（1932-2016）が『物語の役割』(1979)、『解釈の限界』(1990)で展開した受容理論。テクストには「経験的読者」とは異なる「モデル読者」が構造的に組み込まれており、テクストの意味は経験的読者の自由解釈ではなく、モデル読者がテクストから再構成する協力的解釈に基づくと主張した。フィッシュの解釈共同体論への対抗軸を成す。",
    background="エコ記号論（『一般記号論論考』1976）、イタリア意味論的伝統、コンスタンツ受容理論との対話。",
    development="ナラトロジー（プリンス、ファラン）の読者論、認知物語論の理論的祖型となった。",
    historical_context="1980年代の読者論論争（フィッシュ vs エコの解釈の限界をめぐる対論）。",
    primary_source_url=WIKI_EN+"Umberto_Eco",
    primary_source_type="Wikipedia: Umberto Eco",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブライク主体的批評",
    name_en="Bleich's subjective criticism",
    name_original="subjective criticism",
    period_key="受容理論期",
    definition="デイヴィッド・ブライク（1940- ）が『読書と感情』(1975)、『主体的批評』(1978)で提唱した米国読者反応批評の急進的形態。テクストの意味は読者の心理的応答（感情・連想・記憶）の中に位置し、批評は「客観的解釈」を放棄して読者の主体的応答の共同的検討となるべきだと主張した。授業実践と接続した教育的読者論として影響を残した。",
    background="米国教育心理学、ノーマン・ホランド精神分析的読者論との並行、1970年代米国大学英文学教育の刷新運動。",
    development="フェミニスト読者反応批評（フェターリー、シュヴァイカート）、米国国語教育の読者中心アプローチに継承された。",
    historical_context="1970年代米国大学における学生中心教育論議と、読者反応批評の制度化。",
    primary_source_url=WIKI_EN+"Reader-response_criticism",
    primary_source_type="Wikipedia: Reader-response criticism",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ホランド精神分析的読者論",
    name_en="Holland's psychoanalytic reader theory",
    name_original="5 Readers Reading",
    period_key="受容理論期",
    definition="ノーマン・ホランド（1927-2017）が『5 Readers Reading』(1975)、『動的反応』(1968)で展開した精神分析的読者反応批評。読者は固有の「アイデンティティ・テーマ」を持ち、テクストはそのテーマの表現として読まれると主張した。フロイト・エリクソン精神分析の文学への適用として、米国読者反応批評の心理学的極を成した。",
    background="フロイト『不気味なもの』、エリクソンのアイデンティティ概念、米国精神分析学の文学研究への浸透。",
    development="精神分析的批評の系譜（フェルマン、ヘルツェイ）と並んで、読者の主体性の理論化に貢献した。",
    historical_context="1970年代米国における精神分析と文学批評の制度的接合期。",
    primary_source_url=WIKI_EN+"Norman_N._Holland",
    primary_source_type="Wikipedia: Norman N. Holland",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リファテール記号論的詩学",
    name_en="Riffaterre's semiotic poetics",
    name_original="Sémiotique de la poésie",
    period_key="受容理論期",
    definition="ミカエル・リファテール（1924-2006）が『詩の記号論』(1978)、『テクストの生産』(1979)で展開した受容理論的詩学。詩を「ヒポグラム（hypogramme）」（前提となるテクストや慣用句）の変換として読み、読者が「過剰読み（hyper-reading）」を通じて詩的意味を再構成する過程を理論化した。フランス構造主義と米国受容理論の架橋として機能した。",
    background="ロシア・フォルマリズム（ヤコブソン）、フランス構造主義詩学、米国コロンビア大学での教育活動。",
    development="ジュリア・クリステヴァのインターテクスチュアリテ概念、ジョナサン・カラー受容詩学に継承された。",
    historical_context="1970年代の構造主義から受容理論への過渡期。",
    primary_source_url=WIKI_EN+"Michael_Riffaterre",
    primary_source_type="Wikipedia: Michael Riffaterre",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: Psychoanalytic literary criticism (8)
# ============================================================
add(**C, name_ja="フロイト『不気味なもの』（文学批評適用）",
    name_en="Freud's The Uncanny (literary criticism)",
    name_original="Das Unheimliche",
    period_key="精神分析文学批評期",
    definition="ジークムント・フロイト（1856-1939）が1919年に発表した論文。E. T. A. ホフマン『砂男』を中心題材に、「親しみありながら同時に異質なもの」として「不気味なもの（das Unheimliche）」を理論化した。20世紀文学批評におけるゴシック・幻想・モダニズム・ホラー研究の中心理論的参照点となり、ポストモダン批評にも継承された。",
    background="フロイト精神分析の応用美学的展開、19世紀ドイツ・ロマン派文学（ホフマン、ジャン・パウル）の精神分析的再読。",
    development="ジャック・デリダ『精神分析の郵便配達』、ニコラ・アブラハム/マリア・トロークの「クリプト」概念、現代ホラー・幻想文学批評の中心理論的源泉となった。",
    historical_context="第一次大戦後のヨーロッパにおける死・喪失・記憶の文学的問題化期。",
    primary_source_url=ARCH+"freuduncanny",
    primary_source_type="Internet Archive: The Uncanny (Freud)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"「親しみあるものが異質に転じる」不気味さは、AI生成テキスト・画像が「人間的でありながら何かが奇妙」と感じられる現象（uncanny valley）の精神分析的祖型。",
         "related_ai_phenomenon":"AI生成物の不気味の谷現象"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"不気味なもの",
         "description":"フロイト『不気味なもの』はハイデガー、デリダ、現代美学の中心概念として横断的に参照される。"}])

add(**C, name_ja="ラカン「鏡像段階」（文学批評適用）",
    name_en="Lacan's Mirror Stage (in literary criticism)",
    name_original="Le stade du miroir",
    period_key="精神分析文学批評期",
    definition="ジャック・ラカン（1901-1981）が1949年論文「鏡像段階」で提示した主体形成論を文学批評に応用したもの。生後6-18ヶ月の幼児が鏡像と自己を同一視する過程を、主体形成の根本的「誤認（méconnaissance）」として理論化した。文学における人物意識・読者同一化・ナルシシズム表象の精神分析的読解の核心理論となった。",
    background="アンリ・ヴァロン児童心理学、フロイト『ナルシシズム入門』、メルロー＝ポンティ知覚現象学の総合。",
    development="クリスチャン・メッツ映画記号論、ローラ・マルヴェイ視覚的快楽論、ラカン派文学批評（フェルマン、ジジェクら）に継承された。",
    historical_context="戦後フランスにおけるフロイト主義の構造主義的再解釈期。",
    primary_source_url=WIKI_FR+"Stade_du_miroir",
    primary_source_type="Wikipedia (FR): Stade du miroir",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"鏡像段階の「誤認による主体形成」モデルは、AIキャラクターやアバターを通じた「鏡像的自己構築」の精神分析的祖型として再読される。",
         "related_ai_phenomenon":"AIアバター・キャラクターと鏡像的自己構築"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"主体形成の哲学",
         "description":"ラカン鏡像段階論は20世紀フランス哲学の主体形成論の中心テーゼ。"}])

add(**C, name_ja="クリステヴァ「セミオティック／シンボリック」",
    name_en="Kristeva's semiotic vs symbolic",
    name_original="le sémiotique / le symbolique",
    period_key="精神分析文学批評期",
    definition="ジュリア・クリステヴァ（1941- ）が『詩的言語の革命』(1974)で展開した精神分析的詩学。象徴界（le symbolique／文法・構文・指示）に先立つ「コーラ（chora）」的次元としての「セミオティック（le sémiotique／リズム・身体・母性的衝動）」を区別し、マラルメ、ロートレアモン、ジョイス等のアヴァンギャルド詩を「セミオティック」の象徴界への侵入として理論化した。",
    background="ラカン精神分析、テル・ケル誌の理論プログラム、フランス・アヴァンギャルド文学研究の総合。",
    development="フェミニスト批評（シクスゥ、イリガライと並ぶフレンチ・フェミニズム三位一体）、現代の身体論・詩学に深い影響を残した。",
    historical_context="1970年代フランスのテル・ケル運動と、精神分析と詩学の理論的統合期。",
    primary_source_url=WIKI_EN+"Julia_Kristeva",
    primary_source_type="Wikipedia: Julia Kristeva",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"セミオティック／シンボリックの区別は、AI生成テキストが象徴界的構造（文法・構文）を高度に再現しつつ、身体的セミオティック次元（リズム・声・母性的衝動）を欠く可能性を理論化する基盤。",
         "related_ai_phenomenon":"AI生成テキストにおける身体的次元の欠如"}])

add(**C, name_ja="シクスゥ「メデューサの笑い」",
    name_en="Cixous's The Laugh of the Medusa",
    name_original="Le Rire de la Méduse",
    period_key="精神分析文学批評期",
    definition="エレーヌ・シクスゥ（1937- ）が1975年に発表したフェミニスト精神分析的文学マニフェスト。「女性的エクリチュール（écriture féminine）」を、男根中心的象徴界に対する身体的・他者的・複数的書記実践として理論化した。クラリッセ・リスペクトールの読解と並んで、フランス・フェミニスト文学理論の中核テキスト。",
    background="ラカン精神分析、デリダ脱構築の影響、5月革命後のフランス・フェミニスト運動MLF（女性解放運動）の興隆。",
    development="モニク・ヴィッティグ、リュス・イリガライと並ぶフレンチ・フェミニズム理論の中核となり、英米フェミニスト文学理論にも翻訳を通じて深い影響を残した。",
    historical_context="1970年代フランスの第二波フェミニズムと、精神分析・哲学・文学理論の女性的書記実践への結晶化。",
    primary_source_url=WIKI_EN+"The_Laugh_of_the_Medusa",
    primary_source_type="Wikipedia: The Laugh of the Medusa",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ボナパルトのポー研究",
    name_en="Bonaparte's study of Poe",
    name_original="Edgar Poe : sa vie, son œuvre",
    period_key="精神分析文学批評期",
    definition="マリー・ボナパルト（1882-1962）が1933年に発表した『エドガー・ポー：その生涯、その作品、エチュード分析的解釈』。フロイトの直弟子として精神分析的伝記批評を体系的に文学に適用した最初期の長編研究。ポーの諸作品（『黒猫』『アッシャー家の崩壊』等）を、母の死・父の不在によるポーの精神構造の表現として解読した。",
    background="フロイト精神分析の文学への適用、ボナパルトのフランス精神分析運動指導期、19世紀末-20世紀初頭の伝記批評の伝統。",
    development="精神分析的伝記批評の祖型として、後の精神分析的文学研究（フリーマン・ファーガソン、ハロルド・ブルーム）に影響を残した。",
    historical_context="1930年代フランスにおけるフロイト主義の知的浸透期。",
    primary_source_url=WIKI_EN+"Marie_Bonaparte",
    primary_source_type="Wikipedia: Marie Bonaparte",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ベルサーニ『救済の文化』",
    name_en="Bersani's The Culture of Redemption",
    name_original="The Culture of Redemption",
    period_key="精神分析文学批評期",
    definition="レオ・ベルサーニ（1931-2022）が1990年に発表した精神分析的・倫理的文学批評。フロイト、プルースト、マラルメ、メルヴィルの読解を通じて、「文学が人生の損失を芸術によって救済する」という「救済的美学」を批判し、芸術の「反救済的（anti-redemptive）」可能性を探った。クィア理論・倫理的批評の理論的源泉となった。",
    background="フロイト精神分析、ラカン、レヴィナス倫理思想、米国大学院での20世紀フランス文学・モダニズム研究。",
    development="ベルサーニ自身の『直観の親密性』(2008)、リー・エーデルマン、クィア・ネガティブ理論に直接継承された。",
    historical_context="1990年代米国アカデミックにおける精神分析的批評と倫理批評の交叉期。",
    primary_source_url=WIKI_EN+"Leo_Bersani",
    primary_source_type="Wikipedia: Leo Bersani",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブルックス『プロットを読む』",
    name_en="Brooks's Reading for the Plot",
    name_original="Reading for the Plot",
    period_key="精神分析文学批評期",
    definition="ピーター・ブルックス（1938- ）が1984年に発表した精神分析的物語論。フロイト『快楽原理の彼岸』の生・死の本能の動態をプロットの動力学に翻訳し、物語を「欲望の機械」として理論化した。バルザック、ディケンズ、コンラッドの読解を通じて、19世紀小説のプロット欲動を精神分析的に解読した。",
    background="フロイト後期論文の物語論的応用、米国ニューヘイブン学派の脱構築・精神分析の総合、19世紀小説研究の精神分析的刷新。",
    development="精神分析的物語論、欲望のナラトロジー、現代の認知物語論にも一定の影響を残した。",
    historical_context="1980年代米国大学院文学研究の理論的高揚期。",
    primary_source_url=WIKI_EN+"Peter_Brooks_(literary_critic)",
    primary_source_type="Wikipedia: Peter Brooks",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"プロット欲動論",
         "description":"ブルックスのプロット精神分析は古典物語論（アリストテレス『詩学』）の現代的・欲動論的再読。"}])

add(**C, name_ja="フェルマン『精神分析を読む』",
    name_en="Felman's Reading Psychoanalysis",
    name_original="Le scandale du corps parlant",
    period_key="精神分析文学批評期",
    definition="ショシャナ・フェルマン（1942- ）が『精神分析と文学』(1977)、『話す身体のスキャンダル』(1980)、『証言：文学・精神分析・歴史における危機』(1992、ローブと共著)で展開したラカン派文学批評。文学テクストと精神分析テクストの相互読解、ヘンリー・ジェイムズ『ねじの回転』のラカン派精読、ホロコースト証言研究に展開した。",
    background="ラカン精神分析、イェール大学比較文学プログラム（デ・マンら）、ホロコースト・トラウマ研究との接続。",
    development="米国大学院ラカン派批評、トラウマ研究、証言文学研究の理論的中核となった。",
    historical_context="1980-90年代米国大学院における精神分析的批評とトラウマ研究の制度化期。",
    primary_source_url=WIKI_EN+"Shoshana_Felman",
    primary_source_type="Wikipedia: Shoshana Felman",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# D: Narratology (9)
# ============================================================
add(**C, name_ja="ジュネット『物語のディスクール』詳論",
    name_en="Genette's Narrative Discourse (detailed)",
    name_original="Discours du récit",
    period_key="古典・古典後ナラトロジー期",
    definition="ジェラール・ジュネット（1930-2018）が1972年『フィギュールIII』所収論文として発表したナラトロジーの古典。プルースト『失われた時を求めて』を分析対象に、物語の「時間（ordre/durée/fréquence）」「叙法（mood）」「態（voice）」の三大カテゴリーで物語を体系化した。古典ナラトロジーの教義的中核テキスト。",
    background="フランス構造主義（バルト、トドロフ、グレマス）、ジュネット自身の『フィギュール』I-IIの修辞学研究の集大成。",
    development="ジュネット『新ナラトロジー研究』(1983)で自己改訂され、ミーケ・バル、シュロミット・リモン=ケナンに継承された。",
    historical_context="1970年代フランス構造主義詩学の頂点期。",
    primary_source_url=WIKI_EN+"Gérard_Genette",
    primary_source_type="Wikipedia: Gérard Genette",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バル『ナラトロジー』詳論",
    name_en="Bal's Narratology (detailed)",
    name_original="De theorie van vertellen en verhalen",
    period_key="古典・古典後ナラトロジー期",
    definition="ミーケ・バル（1946- ）が1985年に発表した（オランダ語原典1980）ナラトロジー教科書の体系書。ジュネット三層構造（fabula/story/text）に対して、より明確な三層モデル（fabula／story／text）を提示し、視覚芸術・絵画・聖書研究にも応用可能な形で物語論を再編成した。英語圏で最も広く参照されるナラトロジー入門書。",
    background="アムステルダム大学比較文学プログラム、フランス構造主義の翻訳的受容、聖書文学研究との接続。",
    development="3版に至る改訂を経て、現代ナラトロジー（フェラン、ハーマン、フルダニク）の標準的参照点となった。",
    historical_context="1980年代の構造主義から後構造ナラトロジーへの過渡期。",
    primary_source_url=WIKI_EN+"Mieke_Bal",
    primary_source_type="Wikipedia: Mieke Bal",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語論の三層モデル",
         "description":"バル・ナラトロジーは現代物語論の標準的入門書として横断的に参照される。"}])

add(**C, name_ja="シュタンツェル類型論",
    name_en="Stanzel's typology of narrative",
    name_original="Theorie des Erzählens",
    period_key="古典・古典後ナラトロジー期",
    definition="フランツ・カール・シュタンツェル（1923-2024）が『物語論の類型』(1979)で体系化した語りの類型論。「権威的物語状況（auktorial）」「一人称物語状況（Ich-Erzähler）」「人物的物語状況（personal）」の三類型を「物語円環（typologischer Kreis）」として配置し、ジュネットとは異なるドイツ語圏ナラトロジーの規範を確立した。",
    background="グラーツ大学英文学、ドイツ語圏物語論の伝統（ケーテ・フリーデマン、ヴェルナー・ケーラー）、英語圏のシュタンドポイント論との対話。",
    development="現代ドイツ語圏ナラトロジーの標準教科書となり、英訳を通じて英語圏にも影響を残した。",
    historical_context="1970年代後半ドイツ語圏文学理論の理論的体系化期。",
    primary_source_url=WIKI_DE+"Franz_Karl_Stanzel",
    primary_source_type="Wikipedia (DE): Franz Karl Stanzel",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="チャットマン『物語と語り』",
    name_en="Chatman's Story and Discourse",
    name_original="Story and Discourse",
    period_key="古典・古典後ナラトロジー期",
    definition="シーモア・チャットマン（1928-2015）が1978年に発表した英語圏初の包括的ナラトロジー教科書。ロシア・フォルマリズム（fabula/sjužet）とフランス構造主義（histoire/discours）を統合し、英語圏向けに「story（物語内容）」「discourse（物語表現）」の二層モデルを確立した。映画・小説双方を対象とする方法論として広く採用された。",
    background="米国記号論、フランス構造主義の英米受容、米国大学院文学・映画研究の制度化期。",
    development="リモン=ケナン、フェラン、米国ナラトロジーの標準参照点となった。",
    historical_context="1970年代後半米国アカデミックにおける物語論の制度的成立期。",
    primary_source_url=WIKI_EN+"Seymour_Chatman",
    primary_source_type="Wikipedia: Seymour Chatman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リモン=ケナン『物語のフィクション』",
    name_en="Rimmon-Kenan's Narrative Fiction",
    name_original="Narrative Fiction: Contemporary Poetics",
    period_key="古典・古典後ナラトロジー期",
    definition="シュロミット・リモン=ケナン（1942- ）が1983年に発表した英語圏ナラトロジー教科書の標準。ジュネット、バル、チャットマンの三系統を統合し、「story（物語内容）」「text（物語テクスト）」「narration（語り）」の三層モデルを英語圏の共通用語法として確立した。多数の改訂版を経て現代まで広く採用されている。",
    background="エルサレム・ヘブライ大学比較文学、ジュネット直系のナラトロジー、ロシア・フォルマリズム研究の総合。",
    development="2002年第二版、現代ナラトロジー入門の標準として、フェラン・ハーマンらに継承された。",
    historical_context="1980年代初頭英語圏ナラトロジーの体系的成立期。",
    primary_source_url=WIKI_EN+"Shlomith_Rimmon-Kenan",
    primary_source_type="Wikipedia: Shlomith Rimmon-Kenan",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="コーン『透明な精神』",
    name_en="Cohn's Transparent Minds",
    name_original="Transparent Minds",
    period_key="古典・古典後ナラトロジー期",
    definition="ドリット・コーン（1924-2012）が1978年に発表した、小説における意識・思考表現技法の体系的研究。「心理叙述（psycho-narration）」「引用された独白（quoted monologue）」「語られた独白（narrated monologue／自由間接話法）」の三技法を区別し、19-20世紀小説（フローベール、ジョイス、ウルフ、トーマス・マン）の意識表現を体系化した。",
    background="プリンストン大学独文学・比較文学、ドイツ語圏物語論（シュタンツェル）と英米小説研究の総合。",
    development="現代ナラトロジー、認知物語論（パーマー『フィクションの心』）の理論的源泉となった。",
    historical_context="1970年代後半英米における意識表現研究の理論的成熟期。",
    primary_source_url=WIKI_EN+"Dorrit_Cohn",
    primary_source_type="Wikipedia: Dorrit Cohn",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"小説における他者の意識への透明なアクセスは、AI生成テキストにおける「人物の心の声」表象の歴史的祖型を構成する。",
         "related_ai_phenomenon":"AI生成における他者意識表象"}])

add(**C, name_ja="フェラン修辞的物語論",
    name_en="Phelan's rhetorical narratology",
    name_original="rhetorical narratology",
    period_key="古典・古典後ナラトロジー期",
    definition="ジェイムズ・フェラン（1951- ）が『物語の動態』(1989)、『進行と人物』(1989)、『生きた語り』(2005)で展開した修辞的物語論。ウェイン・ブース『小説の修辞学』を継承し、物語を「作者-語り手-人物-読者」間の修辞的交渉として捉え、「進行（progression）」概念で物語の展開を分析した。米国ナラトロジー学会（ISSN）の中心理論家。",
    background="シカゴ・ニュー・アリストテリアン学派（ブース、フリードマン）、修辞学的批評の伝統、オハイオ州立大学のISSN本部。",
    development="米国ナラトロジー研究の支柱となり、認知物語論・倫理物語論との対話を継続している。",
    historical_context="1990年代以降の米国ナラトロジー研究の制度的成熟期。",
    primary_source_url=WIKI_EN+"James_Phelan_(narratologist)",
    primary_source_type="Wikipedia: James Phelan",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フルダニク自然物語論",
    name_en="Fludernik's natural narratology",
    name_original="Towards a 'Natural' Narratology",
    period_key="古典・古典後ナラトロジー期",
    definition="モニカ・フルダニク（1957- ）が1996年に発表したポスト古典ナラトロジーの主著。ウィリアム・ラボヴの自然会話における物語研究を範に、ナラトロジーの基盤を「経験性（experientiality）」に置き直す方法を提案した。プロット中心の古典ナラトロジーから、人間の経験表象を中心とする認知ナラトロジーへの転換を主導した。",
    background="フライブルク大学英文学、ラボヴ社会言語学的物語研究、認知科学の文学理論への浸透。",
    development="認知物語論（ハーマン、ジャン・アルベルト）、ポストヒューマン物語論への展開を主導した。",
    historical_context="1990年代後半の物語論の認知論的転回期。",
    primary_source_url=WIKI_EN+"Monika_Fludernik",
    primary_source_type="Wikipedia: Monika Fludernik",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ストーリーワールド理論",
    name_en="storyworld theory",
    name_original="storyworld",
    period_key="古典・古典後ナラトロジー期",
    definition="デイヴィッド・ハーマン（1962- ）が『物語論理』(2002)、『物語論の基礎』(2009)、『ストーリーロジック』(2002)で展開した認知物語論の中核概念。物語を「読者・聴き手が心的に構築する世界」（ストーリーワールド）として理論化し、認知科学・人工知能・心の哲学との接続を体系化した。21世紀ナラトロジーのパラダイム転換を主導した。",
    background="認知言語学、心の哲学、人工知能における物語理解研究、フルダニク自然ナラトロジーの継承。",
    development="ハーマン編『物語論ハンドブック』(2014)、トランスメディア物語論、デジタル物語論の理論的基盤となった。",
    historical_context="2000年代の物語論の認知論的・横メディア的転回期。",
    primary_source_url=WIKI_EN+"David_Herman_(narrative_theorist)",
    primary_source_type="Wikipedia: David Herman",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ストーリーワールドが読者の心的構築過程として定義されるなら、AI生成物語が読者に提示する「世界」の認知的構築可能性が新たに問題化される。",
         "related_ai_phenomenon":"AI生成物語におけるストーリーワールド構築"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"物語理解の認知モデル",
         "description":"ストーリーワールド理論はAIによる物語理解・生成の認知科学的基盤と直接的に接続する。"}])


# ============================================================
# E: Reception studies & book history (4)
# ============================================================
add(**C, name_ja="ダーントン「コミュニケーション・サーキット」",
    name_en="Darnton's communications circuit",
    name_original="communications circuit",
    period_key="書物史・受容史期",
    definition="ロバート・ダーントン（1939- ）が1982年論文「書物史とは何か？」で提唱した書物史方法論。書物の生産・流通・受容を「著者→出版者→印刷者→運送者→書店→読者→（著者へのフィードバック）」の循環として理論化した。アンナル学派的書物史を方法論的に体系化し、英語圏書物史の標準的枠組みを確立した。",
    background="アンナル学派書物史（リュシアン・フェーヴル、アンリ＝ジャン・マルタン）、プリンストン大学18世紀フランス研究、フランス啓蒙期出版研究の集積。",
    development="マッケンジー『書誌学とテクストの社会学』、シャルチエ読書実践史、現代書物史研究の標準枠組みとなった。",
    historical_context="1980年代英語圏における書物史の制度的興隆期。",
    primary_source_url=WIKI_EN+"Robert_Darnton",
    primary_source_type="Wikipedia: Robert Darnton",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"書物の社会人類学",
         "description":"ダーントンのコミュニケーション・サーキット概念は書物を文化的循環として捉える人類学的方法と接続する。"}])

add(**C, name_ja="マッケンジー『書誌学とテクストの社会学』",
    name_en="McKenzie's Bibliography and the Sociology of Texts",
    name_original="Bibliography and the Sociology of Texts",
    period_key="書物史・受容史期",
    definition="D. F. マッケンジー（1931-1999）が1986年パニジ講義で発表した（書籍化1999）テクスト研究方法論。伝統的書誌学を「テクストの社会学」へ拡張し、書物の物質的形態がテクストの意味を構築すると主張した。「テクストとは何か」を物質的・社会的に再定義する革命的方法論として、英語圏書物史の理論的支柱となった。",
    background="ニュージーランド・オックスフォード書誌学伝統、フィルマー・グロウンディング書物の物質性研究、新書誌学への批判的継承。",
    development="ハロルド・ラヴ、スティーヴン・グリーンブラット、現代の物質的テクスト研究に深い影響を残した。",
    historical_context="1980年代後半英語圏書誌学の社会学的・物質論的転回期。",
    primary_source_url=WIKI_EN+"D._F._McKenzie",
    primary_source_type="Wikipedia: D. F. McKenzie",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"テクストの意味が物質的形態に依存するというマッケンジーのテーゼは、AI生成テキストの「形態のなさ」（プラットフォームに依存した非物質性）の理論的問題化に直結する。",
         "related_ai_phenomenon":"AI生成テキストの物質性なき流通"}])

add(**C, name_ja="シャルチエ読書実践史",
    name_en="Chartier's history of reading practices",
    name_original="histoire des pratiques de lecture",
    period_key="書物史・受容史期",
    definition="ロジェ・シャルチエ（1945- ）が『読者の歴史』(1995、編)、『書物の秩序』(1992)、『書物の終焉？』等で展開した読書実践史。書物史の中心を「テクスト」「物質的書物」「読書実践」の三項関係として理論化し、特にアパッシェ印刷ジャンル、巡回パンフレット、読書姿勢（黙読・音読）、読書共同体の歴史的変遷を分析した。",
    background="アンナル学派書物史、ピエール・ブルデュー文化資本論、フランス書物史の制度的中核としての位置。",
    development="英米書物史、デジタル時代の読書研究、現代の読書社会学の理論的基盤となった。",
    historical_context="1990年代フランス書物史の英語圏への翻訳的拡散期。",
    primary_source_url=WIKI_FR+"Roger_Chartier",
    primary_source_type="Wikipedia (FR): Roger Chartier",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"読書実践の歴史人類学",
         "description":"シャルチエ読書実践史は、読書を文化的実践として民族誌的に把握する歴史人類学の方法と接続する。"}])

add(**C, name_ja="マンゲル『読書の歴史』",
    name_en="Manguel's A History of Reading",
    name_original="A History of Reading",
    period_key="書物史・受容史期",
    definition="アルベルト・マンゲル（1948- ）が1996年に発表した一般向け読書史の古典。古代から現代までの読書実践（粘土板、巻物、コーデックス、活版本、電子書籍）を、エッセイ的・自伝的に描いた。アカデミック書物史の通俗的応用版として、読書文化への一般的関心を喚起した代表作。",
    background="マンゲル自身のホルヘ・ルイス・ボルヘスへの朗読体験、書物文化への深い愛着、トロント大学とアレクサンドリア図書館長就任。",
    development="一般向け書物史の規範となり、書物文化への一般的関心を喚起する役割を果たした。",
    historical_context="1990年代の書物史の一般読者層への普及期。",
    primary_source_url=WIKI_EN+"Alberto_Manguel",
    primary_source_type="Wikipedia: Alberto Manguel",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F: Affect / cognitive / post-critique (11)
# ============================================================
add(**C, name_ja="マッスミ情動論",
    name_en="Massumi's affect theory",
    name_original="Parables for the Virtual",
    period_key="情動・認知・ポスト批評期",
    definition="ブライアン・マッスミ（1956- ）が『仮想のための寓話』(2002)で展開した情動論。ドゥルーズ＝ガタリの情動概念をベースに、感情（emotion／意識化された主観的状態）と「情動（affect／前意識的・身体的・自律的強度）」を区別した。21世紀の「情動的転回（affective turn）」を主導した中心理論家。",
    background="ドゥルーズ＝ガタリ哲学、シルヴァン・トムキンスの情動心理学、サイモンドンの個体化論の総合。",
    development="セジウィック『触れる感じ』、サラ・アハメド『情動の文化政治』、現代の情動研究全般の理論的基盤となった。",
    historical_context="2000年代以降の人文学・社会科学における情動的転回期。",
    primary_source_url=WIKI_EN+"Brian_Massumi",
    primary_source_type="Wikipedia: Brian Massumi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"前意識的・身体的情動の概念は、AI生成物との相互作用における身体的応答（gut feeling）の理論的把握に直結する。",
         "related_ai_phenomenon":"AI生成物との情動的相互作用"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"情動哲学",
         "description":"マッスミ情動論はスピノザ-ドゥルーズ系統の情動哲学の現代的展開。"}])

add(**C, name_ja="セジウィック「リパラティブ・リーディング」",
    name_en="Sedgwick's reparative reading",
    name_original="reparative reading",
    period_key="情動・認知・ポスト批評期",
    definition="イヴ・コソフスキー・セジウィック（1950-2009）が『触れる感じ』(2003)所収論文「パラノイド・リーディングとリパラティブ・リーディング」で提示した批評の二類型。20世紀後半批評の支配的様式である「パラノイド・リーディング（疑い・暴露の強迫的反復）」に対抗して、「リパラティブ・リーディング（修復的・希望的・愛着的読み）」を提唱した。ポスト批評運動の中核テキスト。",
    background="セジウィックのクィア理論、メラニー・クライン精神分析の修復概念、シルヴァン・トムキンスの情動論の総合。",
    development="リタ・フェルスキ『批評の限界』、ハイディ・トーラ・グレイハム、現代ポスト批評運動の理論的源泉となった。",
    historical_context="2000年代米国アカデミックにおけるポスト批評運動の興隆期。",
    primary_source_url=DUKE+"books/book/1325/Touching-Feeling",
    primary_source_type="Duke UP: Touching Feeling",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"パラノイド／リパラティブ二類型は、AI生成物への批判的読み（疑い・暴露）と修復的読み（共同制作的・希望的）の理論的区別に直結する。",
         "related_ai_phenomenon":"AI生成物への批判的／修復的読みの選択"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"クィア理論と倫理",
         "description":"セジウィックのリパラティブ・リーディングはクィア理論と倫理哲学の交叉点として横断的に参照される。"}])

add(**C, name_ja="フェルスキ『文学の効用』",
    name_en="Felski's Uses of Literature",
    name_original="Uses of Literature",
    period_key="情動・認知・ポスト批評期",
    definition="リタ・フェルスキ（1956- ）が2008年に発表したポスト批評の宣言書。「認識（recognition）」「魅惑（enchantment）」「知識（knowledge）」「衝撃（shock）」を文学の四つの効用として再定式化し、20世紀批評の「症候読み」「疑いの解釈学」を超える日常的・反応的読書経験の理論化を提案した。後の『批評の限界』への布石。",
    background="ヴァージニア大学英文学、フェミニスト批評の継承、セジウィック・リパラティブ・リーディングの理論的継承。",
    development="フェルスキ自身の『批評の限界』(2015)、ポスト批評運動、現代の読書経験研究に継承された。",
    historical_context="2000年代後半米国アカデミック文学批評のポスト批評的転回期。",
    primary_source_url=WIKI_EN+"Rita_Felski",
    primary_source_type="Wikipedia: Rita Felski",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フェルスキ『批評の限界』",
    name_en="Felski's The Limits of Critique",
    name_original="The Limits of Critique",
    period_key="情動・認知・ポスト批評期",
    definition="リタ・フェルスキが2015年に発表したポスト批評運動の集大成。マルクス主義・精神分析・フーコー的批評の「疑いの解釈学（hermeneutics of suspicion）」（リクール）の文学批評支配を歴史化・批判し、ブルーノ・ラトゥールのアクターネットワーク理論を文学批評に応用する代替方法論を提案した。21世紀文学批評論争の中心テキスト。",
    background="リクール『フロイト解釈学』の疑いの解釈学概念、ラトゥール『近代の存在論的探究』、セジウィックの遺産の集約。",
    development="フェルスキ『フックト』(2020)、ポスト批評運動、ニューフォルマリズム、現代文学研究の方法論論争の中心となった。",
    historical_context="2010年代米国アカデミック文学研究の方法論的危機期。",
    primary_source_url=WIKI_EN+"The_Limits_of_Critique",
    primary_source_type="Wikipedia: The Limits of Critique",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"疑いの解釈学への批判は、AI生成テキストの「真偽」「イデオロギー」を疑う姿勢自体の歴史性・限界を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成物への疑いの解釈学の限界"}])

add(**C, name_ja="ホーガン情動的物語論",
    name_en="Hogan's affective narratology",
    name_original="Affective Narratology",
    period_key="情動・認知・ポスト批評期",
    definition="パトリック・コルム・ホーガン（1956- ）が『情動的物語論』(2011)、『情動的科学の理解』(2009)で展開した認知-情動的物語論。世界文学のクロスカルチャー研究をベースに、物語のプロット類型（ロマンティック、英雄、犠牲、復讐等）を情動の普遍構造として理論化した。コネチカット大学を拠点とする認知物語論の中心理論家。",
    background="ノースロップ・フライ原型批評の認知科学的再解釈、世界文学のクロスカルチャー研究、認知科学の文学理論への適用。",
    development="ハーマン・ストーリーワールド理論、ジャン・アルベルト不自然な物語論と並んで、現代認知物語論の中核となった。",
    historical_context="2010年代の認知文学研究の制度的成熟期。",
    primary_source_url=WIKI_EN+"Patrick_Colm_Hogan",
    primary_source_type="Wikipedia: Patrick Colm Hogan",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ザンシャイン認知文学批評",
    name_en="Zunshine's cognitive literary criticism",
    name_original="Why We Read Fiction",
    period_key="情動・認知・ポスト批評期",
    definition="リサ・ザンシャイン（1968- ）が『なぜ私たちは小説を読むのか』(2006)で確立した認知文学批評。「心の理論（Theory of Mind）」概念を文学読解に応用し、小説読解を「他者の心的状態を多重に推論する認知運動」として理論化した。ヴァージニア・ウルフ、ジェイン・オースティンの読解を通じて方法を実演し、認知文学批評の標準的入門書となった。",
    background="ケンタッキー大学英文学、認知科学（Baron-Cohen自閉症研究の心の理論）、進化心理学の文学批評への適用。",
    development="ザンシャイン編『オックスフォード認知文学研究ハンドブック』(2015)、現代認知文学批評の中核となった。",
    historical_context="2000年代後半米国アカデミックにおける認知科学的文学研究の制度化期。",
    primary_source_url=WIKI_EN+"Lisa_Zunshine",
    primary_source_type="Wikipedia: Lisa Zunshine",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"小説読解が「他者の心的状態の推論」だとすれば、AI生成キャラクターの心的状態は推論可能か（マインドの不在を扱う読みは可能か）が新たに問題化される。",
         "related_ai_phenomenon":"AIキャラクターへの心の理論適用"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"心の理論とAI",
         "description":"心の理論は人間-AI相互作用研究の核心概念であり、認知文学批評の延長として接続する。"}])

add(**C, name_ja="ヴァーミュール『私たちはなぜ小説の人物に関心を持つか』",
    name_en="Vermeule's Why Do We Care About Literary Characters?",
    name_original="Why Do We Care About Literary Characters?",
    period_key="情動・認知・ポスト批評期",
    definition="ブレイクリー・ヴァーミュール（1962- ）が2010年に発表した進化的文学研究の代表作。進化心理学・認知科学を統合し、「私たちはなぜ実在しない小説人物に感情移入し、関心を持つのか」という問いに、社会的監視・噂話・連合形成といった進化的適応の延長としての文学読解を提示した。",
    background="進化文学批評（ジョセフ・キャロル、ボイド）、社会脳仮説、米国大学院文学研究の進化論的転回。",
    development="ボイド『物語の起源』、ジョナサン・ゴットシャル『物語する動物』、現代の進化文学研究の標準テキストとなった。",
    historical_context="2000年代後半-2010年代初頭の文学研究と進化科学の接続期。",
    primary_source_url=WIKI_EN+"Why_Do_We_Care_About_Literary_Characters%3F",
    primary_source_type="Wikipedia: Vermeule's book",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ボイド進化的文学研究",
    name_en="Boyd's evolutionary literary study",
    name_original="On the Origin of Stories",
    period_key="情動・認知・ポスト批評期",
    definition="ブライアン・ボイド（1952- ）が『物語の起源』(2009)で確立した進化的文学批評。物語の起源を遊戯（play）と認知的訓練の進化的延長として位置づけ、ホメロス・スース博士『おーい、ホートン！』の読解を通じて方法を実演した。文学を進化的適応として理論化する研究の代表作。",
    background="オークランド大学英文学、ナボコフ研究、進化心理学の文学への適用、認知科学との接続。",
    development="ヴァーミュール、ゴットシャル、現代の進化文学研究の中核となった。",
    historical_context="2000年代の人文学の進化論的・認知科学的転回期。",
    primary_source_url=WIKI_EN+"Brian_Boyd_(academic)",
    primary_source_type="Wikipedia: Brian Boyd",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ベスト/マーカス「サーフェス・リーディング」",
    name_en="Best/Marcus's surface reading",
    name_original="Surface Reading: An Introduction",
    period_key="情動・認知・ポスト批評期",
    definition="スティーブン・ベスト（1962- ）とシャロン・マーカス（1962- ）が雑誌『リプレゼンテーションズ』(2009年特集号)で提唱した批評方法。マシュレ=ジェイムソン的「症候読み（symptomatic reading）」（隠された深層イデオロギーの暴露）に対抗して、テクストの「表面（surface）」「物質性」「明示的内容」を尊重する読みを提唱した。ポスト批評運動の中核論文。",
    background="UCバークレー校英文学（マーカス）、ニュー・ヒストリシズム以降の批評反省、セジウィックのリパラティブ・リーディングの継承。",
    development="ニュー・フォルマリズム、ジャスティン・カピオラ「ジャスト・リーディング」、現代ポスト批評運動の理論的支柱となった。",
    historical_context="2000年代後半-2010年代初頭の米国アカデミック文学批評方法論論争期。",
    primary_source_url=JSTOR+"stable/10.1525/rep.2009.108.1.1",
    primary_source_type="JSTOR: Surface Reading: An Introduction",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"テクストの表面・明示的内容を尊重する読みは、AI生成テキストに「深層イデオロギー」を読むのか「表面そのもの」として扱うのかという批評的選択を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成テキストの表面と深層"}])

add(**C, name_ja="ガイ『ギミック』",
    name_en="Ngai's Theory of the Gimmick",
    name_original="Theory of the Gimmick",
    period_key="価値・現代物質批評期",
    definition="シアン・ガイ（1971- ）が『ギミックの理論』(2020)で展開した美的批評。「ギミック（gimmick）」（過剰な労働節約装置として感じられるもの）「不思議な印象（zaniness）」「興味深い（interesting）」「かわいさ（cute）」を、後期資本主義の労働・時間・美的経験の交叉する現代美的範疇として理論化した。21世紀の美的-経済批評の代表作。",
    background="シアン・ガイ『不愉快な感情』(2005)、『美学的範疇』(2012)の延長、後期資本主義の労働経済学的分析。",
    development="現代美的批評、批判理論、文学経済学的研究の中核参照点となった。",
    historical_context="2010-2020年代の美学的批評と政治経済学的批評の交叉期。",
    primary_source_url=WIKI_EN+"Sianne_Ngai",
    primary_source_type="Wikipedia: Sianne Ngai",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ギミック概念は、AI生成物が「過剰な労働節約装置」「省力化の魔術」として感じられる現象を理論化する直接的概念基盤となる。",
         "related_ai_phenomenon":"AI生成物のギミック性と労働"}])

add(**C, name_ja="チェン『マージナリティの美学』",
    name_en="Cheng's aesthetics of marginality",
    name_original="The Melancholy of Race",
    period_key="価値・現代物質批評期",
    definition="アン・アンリン・チェン（1965- ）が『人種的メランコリー』(2000)、『装飾の自由』(2018)で展開した美的・精神分析的批評。フロイトの喪・メランコリー概念を人種的少数者の美的経験に適用し、白人主体の人種的他者への愛憎両義的取り込みを「人種的メランコリー」として理論化した。アジア系アメリカ文学批評の代表作。",
    background="フロイト『喪とメランコリー』、ベルサーニ精神分析的批評、米国アジア系文学研究の制度化期。",
    development="現代の人種研究、アジア系文学研究、ポストコロニアル精神分析批評に深い影響を残した。",
    historical_context="2000年代米国アカデミックにおける人種研究の精神分析的・美学的転回期。",
    primary_source_url=WIKI_EN+"Anne_Anlin_Cheng",
    primary_source_type="Wikipedia: Anne Anlin Cheng",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# G: Digital / quantitative / DH (6)
# ============================================================
add(**C, name_ja="モレッティ『遠読』",
    name_en="Moretti's Distant Reading",
    name_original="Distant Reading",
    period_key="デジタル・量的文学研究期",
    definition="フランコ・モレッティ（1950- ）が論文集『遠読』(2013、雑誌論文は2000年から)で確立したデジタル人文学の方法論。「精読（close reading）」に対抗して、大規模文学データの計量的・地図的分析を「遠読」と命名した。世界文学の系統樹分析、英国小説題名の経時変化分析等で方法を実演し、21世紀デジタル文学研究を主導した。",
    background="モレッティ『近代叙事詩』(1996)、『小説のグラフ・地図・系統樹』(2005)、スタンフォード文学ラボの設立(2010)。",
    development="デジタル人文学、文化分析論（cultural analytics）、ジョッカーズ・マクロアナリシス、世界文学の量的研究の理論的中核となった。",
    historical_context="2000年代以降のデジタル人文学の制度的興隆期。",
    primary_source_url=WIKI_EN+"Distant_reading",
    primary_source_type="Wikipedia: Distant reading",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"遠読は文学を計量的・大規模データとして扱う方法を制度化する。AI/LLMによる文学コーパス分析・生成は遠読のラディカルな延長として位置づけられる。",
         "related_ai_phenomenon":"LLMによる文学コーパスの遠読的処理"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"テキストマイニングと文学",
         "description":"遠読はAIテキスト処理の文学的祖型。"}])

add(**C, name_ja="ジョッカーズ『マクロアナリシス』",
    name_en="Jockers's Macroanalysis",
    name_original="Macroanalysis",
    period_key="デジタル・量的文学研究期",
    definition="マシュー・ジョッカーズ（1967- ）が2013年に発表したデジタル文学研究の方法論書。「マクロアナリシス」を、伝統的精読（クローズリーディング）と数値的距離処理（遠読）の中間的方法として理論化した。19世紀英語小説3,500冊のトピックモデル分析、感情分析、ジャンル分類で方法を実演し、量的文学研究の制度化を主導した。",
    background="ネブラスカ大学英文学、スタンフォード文学ラボでのモレッティとの協働、機械学習・自然言語処理の文学研究への適用。",
    development="ジョッカーズ『感情の物語、文体の感情』(2014)、現代のデジタル人文学研究の標準的方法論となった。",
    historical_context="2010年代のデジタル人文学の制度的拡大期。",
    primary_source_url=WIKI_EN+"Matthew_Jockers",
    primary_source_type="Wikipedia: Matthew Jockers",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"トピックモデルと文学",
         "description":"ジョッカーズのマクロアナリシスは機械学習による文学コーパス分析の祖型として、AI研究と直接接続する。"}])

add(**C, name_ja="アンダーウッド機械学習文学批評",
    name_en="Underwood's machine learning criticism",
    name_original="Distant Horizons",
    period_key="デジタル・量的文学研究期",
    definition="テッド・アンダーウッド（1965- ）が『遠い地平』(2019)で確立した機械学習を用いた文学史研究の方法論。19-21世紀英語小説の機械学習分類を通じて、ジャンル・性別・文学的威信の歴史的変動を実証分析した。デジタル人文学の中核的研究者。",
    background="イリノイ大学英文学・情報科学、HathiTrust大規模デジタルコーパスの利用、機械学習の文学研究への応用。",
    development="現代のデジタル文学研究、計算文学批評、AI時代の文学史研究の方法論的標準となっている。",
    historical_context="2010年代後半のデジタル人文学と機械学習の融合期。",
    primary_source_url=WIKI_EN+"Ted_Underwood",
    primary_source_type="Wikipedia: Ted Underwood",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"機械学習による文学コーパス分析は、AI時代の文学批評の方法論的最前線であり、AI生成テキスト分析と本質的に連続する。",
         "related_ai_phenomenon":"機械学習文学批評からAI生成分析へ"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"機械学習と文学コーパス",
         "description":"アンダーウッドの方法論はLLM以前の機械学習文学研究の代表例として、AI研究の人文学的祖型。"}])

add(**C, name_ja="ドラッカー視覚化批評",
    name_en="Drucker's visualization criticism",
    name_original="Graphesis",
    period_key="デジタル・量的文学研究期",
    definition="ジョアンナ・ドラッカー（1952- ）が『グラフェシス』(2014)、『情報の批評的アプローチ』で展開した視覚的人文学・データ批評。情報視覚化を「自然な事実」ではなく「修辞的構築物」として批判的に分析する方法を確立した。デジタル人文学の批判的支柱として機能している。",
    background="UCLA情報学、ドラッカー自身のアーティスト・ブック批評、デジタル人文学への批判的参与。",
    development="批判的データ研究、情報視覚化批評、現代の人文学的データ批判の方法論的基盤となった。",
    historical_context="2010年代のデジタル人文学への批判的反省期。",
    primary_source_url=WIKI_EN+"Johanna_Drucker",
    primary_source_type="Wikipedia: Johanna Drucker",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ボード『フィクションの世界』",
    name_en="Bode's A World of Fiction",
    name_original="A World of Fiction",
    period_key="デジタル・量的文学研究期",
    definition="ケイティ・ボード（1972- ）が2018年に発表したデジタル人文学方法論書。デジタル文学研究の方法論的前提（コーパス選定、メタデータ、文学的威信）を批判的に検討し、19世紀オーストラリア新聞小説のデータベース構築を通じて、より反省的な遠読方法論を提案した。",
    background="オーストラリア国立大学デジタル人文学、ジェンダー・地理的辺境性の量的文学研究への適用。",
    development="批判的デジタル人文学、フェミニスト・デジタル人文学、現代のデジタル文学研究の方法論論争の中心となった。",
    historical_context="2010年代後半のデジタル人文学の方法論的反省期。",
    primary_source_url=WIKI_EN+"Katherine_Bode",
    primary_source_type="Wikipedia: Katherine Bode",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="計算詩学",
    name_en="computational poetics",
    name_original="computational poetics",
    period_key="デジタル・量的文学研究期",
    definition="2010年代以降に発展したデジタル人文学のサブ分野。詩・散文の韻律・音声・スタイルを計算的に分析し、また計算的に生成する研究領域。スタンフォード文学ラボ、ハーヴァード詩学研究所等の機関を中心に、伝統詩学（メーター・押韻）の計算化と、計算言語学の詩学への応用を統合する。",
    background="フォルマリズム詩学、構造主義詩学、自然言語処理、計算言語学の文学研究への融合。",
    development="LLM時代の詩生成研究、計算詩学の理論的拡張、AI詩学批評の制度化に直結する。",
    historical_context="2010年代後半-2020年代のデジタル人文学とAIの収束期。",
    primary_source_url=WIKI_EN+"Computational_creativity#Poetry",
    primary_source_type="Wikipedia: Computational creativity (poetry)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"計算詩学はAI生成詩の批評的基盤を提供する分野であり、AI時代の詩学の中核となる。",
         "related_ai_phenomenon":"AI生成詩と計算詩学"},
        {"axis":"言語","status":"rethinking",
         "rationale":"詩の韻律・音声・スタイルの計算的分析は、AI生成テキストの文体的同定の理論的基盤を提供する。",
         "related_ai_phenomenon":"AI生成テキストの文体的計量分析"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"自然言語処理と詩",
         "description":"計算詩学はNLPと文学研究の交差領域として、AI研究と人文学を直接接続する。"}])


# ============================================================
# H: Recent material / value criticism (6)
# ============================================================
add(**C, name_ja="ベウィス『足で読む』",
    name_en="Bewes's Reading with the Grain",
    name_original="Free Indirect: The Novel in a Postfictional Age",
    period_key="価値・現代物質批評期",
    definition="ティモシー・ベウィス（1966- ）が『自由間接話法：ポスト・フィクション時代の小説』(2022)で展開した現代小説論。21世紀小説における自由間接話法の変容、フィクションと非フィクションの境界の流動化、リアリティ概念の再編成を理論化した。AI時代の文学性を予示する現代批評の代表作。",
    background="ブラウン大学英文学、ベウィス『シニシズムと近代』『マルクス主義と非経験』の延長、現代世界文学の理論的把握。",
    development="現代小説の理論的把握、AI時代の文学性論議、ポスト・フィクション時代の小説論の中核となっている。",
    historical_context="2020年代の文学研究と現代小説の同時代的接続期。",
    primary_source_url=WIKI_EN+"Timothy_Bewes",
    primary_source_type="Wikipedia: Timothy Bewes",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ポスト・フィクション時代の小説論は、AI生成テキストの登場によるフィクション/非フィクション境界の根本的流動化を理論化する直接的基盤。",
         "related_ai_phenomenon":"AIによるフィクション境界の溶解"}])

add(**C, name_ja="シャルクヴァイク文学価値論",
    name_en="Schalkwyk's literary value theory",
    name_original="Literature and the Touch of the Real",
    period_key="価値・現代物質批評期",
    definition="デイヴィッド・シャルクヴァイク（1951- ）が『文学とリアルの触感』(2004)、『シェイクスピアと愛のフィロソフィー』(2018)で展開した文学価値論。文学の価値を「リアルとの触感」（経験の言語化能力）として理論化し、相対主義的批評（カルチュラル・スタディーズの極端な構築主義）への対抗的立場を提示した。",
    background="ケープタウン大学英文学、ウィトゲンシュタイン哲学、シェイクスピア研究の総合。",
    development="ウィトゲンシュタイン的文学価値論、現代のフォルマリズム的批評、ポスト批評運動と並ぶ価値論的潮流に貢献した。",
    historical_context="2000年代後半-2010年代の批評の価値論的転回期。",
    primary_source_url=WIKI_EN+"David_Schalkwyk",
    primary_source_type="Wikipedia: David Schalkwyk",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="弱い理論",
    name_en="weak theory",
    name_original="weak theory",
    period_key="情動・認知・ポスト批評期",
    definition="セジウィック・リパラティブ・リーディング、ケイティ・スチュワート『普通の情動』(2007)、ローレン・バーラント『残酷な楽観主義』(2011)を中核に発展した21世紀批評の傾向。「強い理論」（マルクス・フロイト・フーコー的全体的説明枠組み）への対抗として、特殊性・状況性・小規模性を尊重する批評姿勢を意味する。",
    background="セジウィックのトムキンス情動論への注目、人類学の特殊性志向（ギアツ的厚い記述）、米国大学院文学批評のポスト批評的反省。",
    development="現代ポスト批評運動、情動研究、新しい唯物論的批評の方法論的支柱となった。",
    historical_context="2000-2010年代の批評の方法論的反省期。",
    primary_source_url=WIKI_EN+"Affect_(psychology)",
    primary_source_type="Wikipedia: Affect theory",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="バーラント『残酷な楽観主義』",
    name_en="Berlant's Cruel Optimism",
    name_original="Cruel Optimism",
    period_key="情動・認知・ポスト批評期",
    definition="ローレン・バーラント（1957-2021）が2011年に発表した情動的批評の代表作。「残酷な楽観主義」概念を、「あなたの繁栄を妨げる対象への愛着」として理論化し、新自由主義的後期資本主義における日常生活の情動的構造を分析した。21世紀情動批評の中核テキスト。",
    background="シカゴ大学英文学、フェミニスト批評、新自由主義批判、マッスミ情動論の継承。",
    development="現代の情動研究、批判理論、政治情動学の理論的中核となった。",
    historical_context="2010年代の批判理論と情動研究の融合期。",
    primary_source_url=WIKI_EN+"Lauren_Berlant",
    primary_source_type="Wikipedia: Lauren Berlant",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"残酷な楽観主義概念は、AI生成物への愛着が利用者の主体的繁栄を阻害しうる現象を理論化する基盤となる。",
         "related_ai_phenomenon":"AI生成物への残酷な楽観主義的愛着"}])

add(**C, name_ja="ポスト批評運動",
    name_en="post-critique movement",
    name_original="post-critique",
    period_key="情動・認知・ポスト批評期",
    definition="2009年ベスト/マーカス「サーフェス・リーディング」、2015年フェルスキ『批評の限界』を中核に発展した21世紀文学批評運動。20世紀後半批評の支配的様式である「症候読み」「疑いの解釈学」を歴史化・批判し、テクストとの愛着的・経験的・修復的関係を再評価する立場の総称。批評の「ポスト・批判的」転回を主導する。",
    background="セジウィックのリパラティブ・リーディング、ラトゥール・アクターネットワーク理論、現代米国アカデミック文学批評の方法論的危機。",
    development="ニュー・フォルマリズム、ジャスト・リーディング、現代のポスト人文学的批評と接続する。",
    historical_context="2010年代米国アカデミック文学批評の方法論的転換期。",
    primary_source_url=WIKI_EN+"Postcritique",
    primary_source_type="Wikipedia: Postcritique",
    importance_score=4, source_tier="tertiary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"ポスト批評運動はテクストとの修復的・経験的関係を再評価する。AI生成テキストとの新たな関係様式（共同制作・対話）の理論化に直結する。",
         "related_ai_phenomenon":"AI生成テキストとの修復的・対話的関係"}])

add(**C, name_ja="ニュー・フォルマリズム",
    name_en="new formalism",
    name_original="new formalism",
    period_key="情動・認知・ポスト批評期",
    definition="マージョリー・レヴィンソン「新しいフォルマリズムとは何か」(2007)、ヘザー・ダブロウ、キャロライン・レヴィン『フォーム』(2015)を中核に発展した21世紀批評運動。ニュー・ヒストリシズム以後の歴史化された批評の中で、改めて文学的形式・形態・パターンに焦点を戻す立場の総称。フォーム概念を社会・政治・身体に拡張する点で旧フォルマリズムと区別される。",
    background="ニュー・ヒストリシズム反省、レヴィンの全体論的フォーム概念、現代詩学・物語論との接続。",
    development="現代の文学形式研究、フォームの社会論、ポスト批評運動と並行する21世紀文学批評の中核潮流となった。",
    historical_context="2010年代米国アカデミック文学批評のフォルマリスト的回帰期。",
    primary_source_url=WIKI_EN+"New_formalism",
    primary_source_type="Wikipedia: New formalism",
    importance_score=4, source_tier="tertiary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"フォルマリスト詩学の現代形",
         "description":"ニュー・フォルマリズムは、形式概念を社会・身体に拡張する点でロシア・フォルマリズムとも、ニュー・クリティシズムとも区別される21世紀の形式論的潮流。"}])


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
        print(f"[c34-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c34-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
