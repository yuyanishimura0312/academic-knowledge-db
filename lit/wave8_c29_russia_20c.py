"""LIT-DB Phase 2 Wave 8 — C29: Russia / Slavic 20th-century onwards (40 concepts).

Subfield: lit_russia_slavic (id=18), region='周縁横断'.
Sources: rvb.ru (Russian Virtual Library), feb-web.ru (Fundamental Electronic
Library of Russian Literature, FEB), Project Gutenberg, ImWerden, Plato SEP,
academic-grade Wikipedia (en/ja/ru). Primary PD texts -> 'primary'; canonical
scholarly secondary -> 'secondary'; synthetic critical categories -> 'tertiary'.
Cyrillic original spellings included where reliably attestable.

Coverage: 銀の時代(A) -> ソヴィエト期(B) -> 抑圧・反体制(C) -> ポスト・ソヴィエト(D)
-> 主要批評・理論(E)。C28 (19c) と重複ゼロ。
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# Sub-period structure for the 20th-century-and-onwards Russian/Slavic field.
PERIODS = [
    ("ロシア銀の時代", "Russian Silver Age", 1890, 1925,
     "象徴主義からアクメイズム・未来派・イマジニズムに至る、ロシア・モダニズム文芸黄金期。革命前後の精神文化的高揚と国際的影響を生んだ。"),
    ("ソヴィエト期文学", "Soviet Literature", 1917, 1991,
     "1917年革命から1991年ソ連崩壊まで。社会主義リアリズム・反体制文学・サミズダート・タミズダートを含む、検閲下と表現闘争の70年余。"),
    ("ポスト・ソヴィエト文学", "Post-Soviet Literature", 1991, 2025,
     "1991年以降の文学状況。ポストモダニズム・コンセプチュアリズム・新リアリズムから、亡命作家・女性作家・ユーラシア主義文学までを含む現代地平。"),
]

# Source URL bases (real, verifiable)
RVB = "https://rvb.ru/"             # Russian Virtual Library
FEB = "http://feb-web.ru/"          # Fundamental Electronic Library
GUTEN = "https://www.gutenberg.org/"
IMWERDEN = "https://imwerden.de/"   # ImWerden academic Russian-text archive
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_russia_slavic", region="周縁横断",
         original_script="cyrillic")

# ============================================================
# A: 銀の時代（8件）
# ============================================================
# C28 で「ロシア象徴主義」を運動として基底登録済 → 重複回避のため
# 「象徴主義第二世代（младшие символисты）」として別概念を追加する。
add(**C, name_ja="象徴主義第二世代",
    name_en="Russian Symbolism (younger generation)",
    name_original="младшие символисты",
    period_key="ロシア銀の時代",
    definition="1900年代以降に登場するロシア象徴主義の第二世代。ブローク、ベールイ、ヴャチェスラフ・イヴァーノフを中心に、ソロヴィヨフ宗教哲学を継承し、神秘的・終末論的・ソフィオロジー的志向を強めた。第一世代（ブリューソフ、バリモント）の唯美主義に対して、世界変革の宗教的展望を文学に求めた。",
    background="ソロヴィヨフ宗教哲学・ソフィア論の継承、ニーチェ受容、19世紀末ロシア宗教思想の高揚。",
    development="1910年代に内的分裂を起こし、アクメイズム・未来派の批判対象となるが、20世紀ロシア・モダニズム精神文化の中核を成した。",
    historical_context="1905年革命と1917年革命の挟間にあるロシア精神文化の宗教的・形而上学的高揚期。",
    primary_source_url=WIKI_EN+"Symbolist_movement_in_Russia",
    primary_source_type="Wikipedia: Symbolist movement in Russia",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アクメイズム",
    name_en="Acmeism",
    name_original="акмеизм",
    period_key="ロシア銀の時代",
    definition="1910年代初頭に成立したロシア詩運動。グミリョフ、ゴロデツキイを理論家とし、アフマートヴァ、マンデリシュタム、ゼンケーヴィチを主要詩人とする。象徴主義の神秘的・抽象的傾向を批判し、明晰な形象・物質性・職人的言語精錬を主張した。「詩人組合（Цех поэтов）」を組織し、明示的綱領を持つ運動として活動した。",
    background="象徴主義第二世代の宗教的曖昧性への反動と、フランス・パルナッス派・古典主義の受容。",
    development="1921年グミリョフ銃殺、1930年代マンデリシュタム弾圧によって運動は壊滅したが、アフマートヴァ後期作品とソヴィエト後期再発見を通じて20世紀ロシア詩の規範を成した。",
    historical_context="ロシア銀の時代後期、革命前夜の文学運動の多元化期。",
    primary_source_url=WIKI_EN+"Acmeist_poetry",
    primary_source_type="Wikipedia: Acmeist poetry",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ロシア未来派",
    name_en="Russian Futurism",
    name_original="русский футуризм",
    period_key="ロシア銀の時代",
    definition="1912年宣言『社会の趣味への平手打ち』を起点とするロシア前衛詩運動。マヤコフスキー、フレーブニコフ、クルチョーヌィフ、ブルリュク兄弟を中心とする。イタリア未来派の影響を受けつつ、独自に「ザーウミ（超意味言語）」を発達させ、語の物質性・音響性・形態破壊を実験した。",
    background="イタリア未来派宣言（マリネッティ1909）の受容、ロシア絵画前衛（ラリオーノフ、ゴンチャローヴァ）との共闘、銀の時代詩学の急進化。",
    development="十月革命後はLEF（左翼芸術戦線）を組織し、革命芸術の前衛として展開したが、1930年代社会主義リアリズム公式化により壊滅した。",
    historical_context="20世紀初頭の世界前衛運動の中での、ロシア独自の言語実験運動。",
    primary_source_url=WIKI_EN+"Russian_Futurism",
    primary_source_type="Wikipedia: Russian Futurism",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ロシア未来派の「ザーウミ（超意味言語）」は語の意味的内容を解体し、音響・形態・物質性そのものを詩材とする実験で、LLMが意味-形式関係を統計的に学習する現代において、意味を超えた言語の物質性をどう扱うかという理論的問いの先駆である。",
         "related_ai_phenomenon":"LLM時代における意味を超えた言語の物質性"}])

add(**C, name_ja="ザーウミ（超意味言語）",
    name_en="zaum / transrational language",
    name_original="заумь",
    period_key="ロシア銀の時代",
    definition="ロシア未来派詩人クルチョーヌィフ、フレーブニコフが1912-13年に展開した詩的言語実験。通常の意味伝達を超え、音素・音韻・形態素そのものに詩的意義を持たせる「超意味（за-умь）」言語。フレーブニコフの「星の言語」「神の言語」構想や、クルチョーヌィフ「dyr bul shchyl」(1913)に結晶した。",
    background="象徴主義の音楽性・象徴的言語観の急進化、ロシア・フォルマリズムの音響詩研究との並行的展開。",
    development="ヤコブソン、シクロフスキーら形式主義者の理論的支柱となり、20世紀世界前衛詩（ダダイズム、シュルレアリスム自動筆記）と比較される音響詩実験の祖型。",
    historical_context="ロシア銀の時代末期の前衛詩学の極北。",
    primary_source_url=WIKI_EN+"Zaum",
    primary_source_type="Wikipedia: Zaum",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ザーウミは意味から切り離された言語の物質性を詩的経験の核とする。LLMが意味-形式の相関を学習するパラダイムにおいて、意味を欠いた言語生成の美学的可能性を再考させる古典的装置である。",
         "related_ai_phenomenon":"LLM生成における意味を欠いた言語パターンの美学"}])

add(**C, name_ja="ベールイ『ペテルブルク』",
    name_en="Bely's Petersburg",
    name_original="Петербург (Андрей Белый)",
    period_key="ロシア銀の時代",
    definition="アンドレイ・ベールイ(Андрей Белый, 1880-1934)による1913-22年の長編小説。象徴主義小説の頂点とされ、『ユリシーズ』『失われた時を求めて』と並ぶ20世紀モダニズム小説の三大傑作の一つ（ナボコフ）。1905年革命前夜のペテルブルクを舞台に、官僚と革命家の親子関係をリズム化された散文・色彩象徴・ライトモティーフ手法で描く。",
    background="ベールイ自身の象徴主義詩学、ソロヴィヨフ宗教哲学、ロシア・ドイツ表現主義の総合。",
    development="ロシア・モダニズム散文の方法論的祖型となり、ナボコフ、プラトーノフ、現代ロシア小説に影響した。",
    historical_context="ロシア銀の時代の総合的成果として、革命前夜の精神文化的緊張を結晶化した作品。",
    primary_source_url=IMWERDEN+"belyj-andrej",
    primary_source_type="ImWerden: Andrey Bely",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ブリューソフ詩学",
    name_en="Bryusov's poetics",
    name_original="поэтика Брюсова",
    period_key="ロシア銀の時代",
    definition="ヴァレーリー・ブリューソフ(Валерий Брюсов, 1873-1924)を中心とする、ロシア象徴主義第一世代の詩学。フランス象徴主義（ボードレール、ヴェルレーヌ、マラルメ）の翻訳・紹介を通じて、ロシア詩に新しい音律・象徴・歴史的視野を導入した。雑誌『天秤座（Весы）』の主宰者として、ロシア象徴主義の制度的中心を成した。",
    background="フランス象徴主義の体系的受容、ロシア・パルナッス派的歴史主義、19世紀末ロシア・デカダン文化。",
    development="第二世代象徴主義への基盤を提供し、ソヴィエト初期にも文化機関で活動した。",
    historical_context="ロシア銀の時代の制度的構築期、文学雑誌・出版社の精神文化的役割の頂点。",
    primary_source_url=RVB+"brusov/",
    primary_source_type="Russian Virtual Library: Bryusov",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アフマートヴァ『レクイエム』",
    name_en="Akhmatova's Requiem",
    name_original="Реквием",
    period_key="ソヴィエト期文学",
    definition="アンナ・アフマートヴァ(Анна Ахматова, 1889-1966)が1935-40年に執筆、長く非公式流通に留まり1963年ミュンヘンで初出版された連作詩。スターリン期の大粛清下、息子レフ・グミリョフの逮捕・収容を契機に、レニングラード監獄前で待つ母親たちの集団的受苦を、冷徹な簡素性のうちに記録した。20世紀ロシア詩の最高峰の一つ。",
    background="1930年代大粛清、1921年夫グミリョフ銃殺、1935年・1938年・1949年息子レフ三度の逮捕。",
    development="サミズダート・タミズダート流通を経て、ソ連内では1987年まで出版禁止。20世紀世界詩の証言文学の代表作として国際的評価を確立した。",
    historical_context="スターリン期大粛清と、検閲下で記憶を文学的に保存する詩的実践の極致。",
    primary_source_url=IMWERDEN+"axmatova-anna",
    primary_source_type="ImWerden: Akhmatova",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"invariant",
         "rationale":"『レクイエム』は固有歴史経験（粛清下監獄前で待つ母）の真正な証言として、模倣・代替不能な文学的真正性の指標を成す。AI共著時代においても、固有歴史的経験に根ざした証言の真正性は不変軸として機能する。",
         "related_ai_phenomenon":"AI時代における歴史的証言の固有真正性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"全体主義の証言文学",
         "description":"アフマートヴァの証言詩は20世紀全体主義論（アーレント、レーヴィ）の文学的並行例として参照される。"}])

add(**C, name_ja="マンデリシュタム詩学",
    name_en="Mandelstam's poetics",
    name_original="поэтика Мандельштама",
    period_key="ロシア銀の時代",
    definition="オシップ・マンデリシュタム(Осип Мандельштам, 1891-1938)の詩と詩論。アクメイズム第一詩集『石』(1913)以降、ヘレニズム・地中海・ペテルブルクを統合する歴史的記憶の詩学を展開した。詩論『言葉と文化』『ダンテに関する話』はアクメイズムの理論的中核を成す。1934年スターリン風刺詩で逮捕、1938年収容所で死亡。",
    background="アクメイズム理論、ヘレニズム古典学、ロシア銀の時代の歴史哲学的志向。",
    development="ナデジダ・マンデリシュタム『回想』(1970, 1972)を通じて1960年代以降に世界的受容が進み、20世紀ロシア詩の頂点として確立された。",
    historical_context="アクメイズムからスターリン期弾圧へ至る、20世紀ロシア詩の歴史的軌跡を凝縮した詩人の生涯。",
    primary_source_url=IMWERDEN+"mandelshtam-osip",
    primary_source_type="ImWerden: Mandelstam",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============================================================
# B: ソヴィエト期（8件）
# ============================================================
add(**C, name_ja="ロシア・フォルマリズム",
    name_en="Russian Formalism",
    name_original="русский формализм",
    period_key="ロシア銀の時代",
    definition="1915-30年に活動したロシア文学理論運動。サンクト・ペテルブルクのOPOJAZ（詩的言語研究会）と、モスクワ言語学サークルを二大拠点とする。ヤコブソン、シクロフスキー、エイヘンバウム、トィニャーノフを中心人物とし、文学を内在的な「文学性（литературность）」の研究対象として確立した。20世紀構造主義詩学の源流。",
    background="ロシア銀の時代詩学、フッサール現象学、ソシュール構造言語学の並行的影響。",
    development="プラハ言語学サークルを経由してフランス構造主義（バルト、ジュネット）に決定的影響を与え、20世紀世界文学理論の基盤を成した。1930年スターリン期に強制解散。",
    historical_context="ロシア革命前後の知的高揚期と、その後のソヴィエト・イデオロギー統制下での消滅。",
    primary_source_url=WIKI_EN+"Russian_formalism",
    primary_source_type="Wikipedia: Russian formalism",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"フォルマリズム詩学",
         "description":"ロシア・フォルマリズムは20世紀詩学・物語論の理論的源流であり、PT-DBの中核参照源。"}])

add(**C, name_ja="OPOJAZ（詩的言語研究会）",
    name_en="OPOJAZ / Society for the Study of Poetic Language",
    name_original="ОПОЯЗ",
    period_key="ロシア銀の時代",
    definition="1916年ペトログラードに結成された詩的言語研究会。シクロフスキー、エイヘンバウム、トィニャーノフ、ヤクビンスキーらが参加。ロシア・フォルマリズムのペテルブルク派の制度的基盤として、『詩的言語論集』(1916, 1917)、シクロフスキー『散文の理論』(1925)、エイヘンバウム『「外套」はいかに作られているか』(1918)等の理論的成果を生んだ。",
    background="ロシア未来派詩運動との同盟、銀の時代の言語学的・詩学的革新の総合化。",
    development="1923年以降モスクワ言語学サークルとの理論的交流を深め、1928年ヤコブソン・トィニャーノフ共同声明『言語と文学の研究の問題』に結実、1930年代に解散した。",
    historical_context="ロシア革命直後の理論的高揚期、ペテルブルク・モスクワ二大都市の知的生産の頂点。",
    primary_source_url=WIKI_EN+"OPOJAZ",
    primary_source_type="Wikipedia: OPOJAZ",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シクロフスキー「異化（オストラネニエ）」",
    name_en="Shklovsky's ostranenie / defamiliarization",
    name_original="остранение",
    period_key="ロシア銀の時代",
    definition="ヴィクトル・シクロフスキー(Виктор Шкловский, 1893-1984)が論文『手法としての芸術』(1917)で定式化した、ロシア・フォルマリズムの中核概念。日常的知覚の自動化を解除し、対象を「異物として（странным）」見せる芸術の本質的機能。トルストイ『ホルストメール』の馬の視点による所有概念の異化を範例とする。",
    background="ロシア銀の時代の認知刷新志向、19世紀ロシア小説（特にトルストイ）における知覚革新技法の理論化。",
    development="ブレヒトの「異化効果（Verfremdungseffekt）」、フランス構造主義詩学、認知文学理論にまで広く継承された20世紀文学理論の基本概念。",
    historical_context="ロシア・フォルマリズム創立期の最重要理論的貢献。",
    primary_source_url=WIKI_EN+"Defamiliarization",
    primary_source_type="Wikipedia: Defamiliarization",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"異化（オストラネニエ）は知覚の自動化を解除し新しい見え方を作る芸術の本質的機能を理論化する。LLMが既存パターンの統計的再生産に傾く時代において、「異化」を生成基準にすることが創造性の判定軸として再活性化される。",
         "related_ai_phenomenon":"AI生成における新規性・異化判定基準"},
        {"axis":"受容","status":"rethinking",
         "rationale":"異化は受容過程における知覚の刷新を中心化する概念。AI生成テキストの新鮮さ・退屈さの受容判定にも適用可能で、生成AI時代の受容理論の基盤として再読される。",
         "related_ai_phenomenon":"AI生成テキストの新鮮さ・退屈さの受容判定"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"異化・脱自動化",
         "description":"異化はPTフォルマリズム詩学の中核概念で、20世紀文学理論の基底をなす。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"創造性・新規性評価指標",
         "description":"異化概念はAI生成における新規性評価の理論的祖型として並行的に検討される。"}])

add(**C, name_ja="バフチン「言語の対話性」",
    name_en="Bakhtin's dialogism of language",
    name_original="диалогизм языка",
    period_key="ソヴィエト期文学",
    definition="バフチン(およびヴォロシノフ)『マルクス主義と言語哲学』(1929)、『言葉とロマンの言語』(1934-35)で展開された言語理論。すべての発話が他者の発話との応答・先取り・対話の中にあるという「言語の対話性」を主張し、ソシュール構造言語学（独白的言語観）への根本的批判を提示した。マルクス主義言語論として記述され、20世紀後半に再評価された。",
    background="フンボルト・ヴォスラー言語哲学のロシア的受容、マルクス主義的社会言語論、対話的人格論。",
    development="クリステヴァ「間テクスト性（intertextualité）」概念の理論的源泉となり、20世紀後半の言語論的転回・物語論・談話分析の基盤を成した。",
    historical_context="1920年代ソヴィエト初期の理論的興隆、その後のスターリン期沈黙、1960年代以降の世界的再発見。",
    primary_source_url=WIKI_EN+"Mikhail_Bakhtin",
    primary_source_type="Wikipedia: Mikhail Bakhtin",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"対話性・間テクスト性",
         "description":"バフチンの対話性論はクリステヴァを通じて20世紀後半の物語論・記号論の中核概念となった。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"言語哲学・対話の哲学",
         "description":"バフチンの対話的言語観はブーバー、レヴィナスの対話の哲学と並行する20世紀対話論の重要源流。"}])

add(**C, name_ja="社会主義リアリズム",
    name_en="Socialist Realism",
    name_original="социалистический реализм",
    period_key="ソヴィエト期文学",
    definition="1934年第一回ソヴィエト作家会議で公式化された、ソ連の唯一公認文芸方法。「現実をその革命的発展において歴史的に具体的・真実に描写する」と定式化された。「社会主義的内容」「民族的形式」「党性」「人民性」「典型性」を要件とし、1950年代まで支配的、ペレストロイカ期に解体した。",
    background="チェルヌィシェフスキー・ベリンスキー以来のロシア現実批評の急進化、レーニン党性論、ジダーノフ文化政策。",
    development="ゴーリキー『母』を範型とし、ファジェーエフ、ショーロホフ等が代表作を生んだ。1956年スターリン批判以降緩和、1980年代に公式枠組みとして崩壊。",
    historical_context="スターリン期の文化総動員政策と、文学の国家管理体制の確立期。",
    primary_source_url=WIKI_EN+"Socialist_realism",
    primary_source_type="Wikipedia: Socialist realism",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="マヤコフスキー革命詩",
    name_en="Mayakovsky's revolutionary poetry",
    name_original="революционная поэзия Маяковского",
    period_key="ソヴィエト期文学",
    definition="ウラジーミル・マヤコフスキー(Владимир Маяковский, 1893-1930)の革命期詩作。ロシア未来派出身でありながら十月革命に文学的に応答し、『左行進』『一億五千万』『よし！』等で、革命的内容と前衛的形式を統合した独自の革命詩を確立した。LEF（左翼芸術戦線）の中心人物として、革命芸術の制度的構築に関与。",
    background="ロシア未来派、十月革命前後の前衛芸術と政治の蜜月期。",
    development="1930年自殺以後、スターリン期に「ソヴィエト革命詩の最高峰」として公式聖典化され、社会主義リアリズム以前の前衛精神の象徴となった。",
    historical_context="1917-30年のロシア革命と前衛芸術の同盟、その後のスターリン期前衛弾圧の歴史。",
    primary_source_url=RVB+"mayakovsky/",
    primary_source_type="Russian Virtual Library: Mayakovsky",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パステルナーク『ドクトル・ジバゴ』",
    name_en="Pasternak's Doctor Zhivago",
    name_original="Доктор Живаго",
    period_key="ソヴィエト期文学",
    definition="ボリス・パステルナーク(Борис Пастернак, 1890-1960)による1957年長編小説。20世紀初頭からロシア革命・内戦・スターリン期に至る激動を、医師にして詩人ジバゴの生涯を通じて描く。ソ連内では出版を拒否され、1957年イタリアで初出版、1958年ノーベル文学賞授賞をめぐり国家的醜聞となった（パステルナークは受賞辞退強制）。",
    background="ロシア銀の時代詩人としての出自、20世紀ロシア知識人の革命体験総括の必要性。",
    development="タミズダート（亡命出版）の象徴的作品となり、1988年ペレストロイカ期にソ連内で初出版。20世紀後半冷戦下文化政治の象徴的事件となった。",
    historical_context="フルシチョフ「雪解け」期と検閲復活の挟間、東西冷戦下のソ連文化政策の縮図。",
    primary_source_url=WIKI_EN+"Doctor_Zhivago_(novel)",
    primary_source_type="Wikipedia: Doctor Zhivago",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ブルガーコフ『巨匠とマルガリータ』",
    name_en="Bulgakov's The Master and Margarita",
    name_original="Мастер и Маргарита",
    period_key="ソヴィエト期文学",
    definition="ミハイル・ブルガーコフ(Михаил Булгаков, 1891-1940)が1928-40年に執筆、生前未刊、1966-67年初出版された長編小説。1930年代モスクワを舞台に悪魔ヴォランドが訪れる枠物語と、エルサレムでイエスと総督ピラトを描く劇中劇を交錯させ、スターリン期文学制度・宗教・芸術の関係を寓喩的に描いた。20世紀ロシア小説最高峰の一つ。",
    background="ブルガーコフ自身の文学的・身体的迫害、聖書改作伝統、ファウスト神話、ロシア銀の時代終末論的志向。",
    development="サミズダート・タミズダート流通を経て1966-67年雑誌『モスクワ』で部分公刊、その後完全版が編まれた。世界文学カノンに参入。",
    historical_context="スターリン期文化迫害下の地下執筆と、ペレストロイカ期再評価の歴史。",
    primary_source_url=IMWERDEN+"bulgakov-mihail",
    primary_source_type="ImWerden: Bulgakov",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"『巨匠とマルガリータ』は聖書（マタイ伝・福音書）の改作を作中作として組み込み、原典-改作-再解釈の真正性を多層的に問題化する構造を持つ。AI時代の生成テキストにおける真正性・原典性の問題と理論的に共鳴する。",
         "related_ai_phenomenon":"AI生成における原典-改作-真正性の階層"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"作中作の作者「巨匠」が実在性を失い焼かれ、悪魔の介入で復元される入れ子構造は、作者性の所在を多層化する。AI共著における作者性の不確定性の文学的祖型として再読される。",
         "related_ai_phenomenon":"AI共著における作者性の所在の不確定性"}])

# ============================================================
# C: 抑圧・反体制文学（8件）
# ============================================================
add(**C, name_ja="ソルジェニーツィン『収容所群島』",
    name_en="Solzhenitsyn's The Gulag Archipelago",
    name_original="Архипелаг ГУЛАГ",
    period_key="ソヴィエト期文学",
    definition="アレクサンドル・ソルジェニーツィン(Александр Солженицын, 1918-2008)による1973年タミズダート出版の三部作。1918-56年のソヴィエト強制収容所制度の証言文学的・歴史記述的・文学的総合。227人の証言と自身の体験を統合した「文学的調査」を自称し、20世紀全体主義・収容所文学の代表作となった。",
    background="ソルジェニーツィン自身の1945-53年収容所体験、フルシチョフ雪解け期の『イワン・デニーソヴィチの一日』(1962)出版、その後ブレジネフ期の再弾圧。",
    development="1974年国外追放、1990年ソ連市民権回復、1994年帰国。1989年初めて『新世界』誌でソ連内出版。20世紀全体主義の主要証言として歴史的・哲学的影響を持つ。",
    historical_context="ソヴィエト体制下のグラーグ収容所制度総体の文学的告発と、それが体制崩壊に与えた精神的・国際的影響。",
    primary_source_url=WIKI_EN+"The_Gulag_Archipelago",
    primary_source_type="Wikipedia: The Gulag Archipelago",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"全体主義論",
         "description":"ソルジェニーツィンの収容所文学はアーレント全体主義論・レーヴィ証言文学と並ぶ20世紀全体主義の哲学的・文学的主要参照源。"}])

add(**C, name_ja="サミズダート文学",
    name_en="samizdat literature",
    name_original="самиздат",
    period_key="ソヴィエト期文学",
    definition="1950年代以降のソ連で発達した、検閲を経ずタイプ・手書きで複写・流通する地下出版・自家出版の総体。「自分で出版する（сам-издат）」の意。ブルガーコフ、ソルジェニーツィン、ブロツキー、シニャフスキー、サハロフ等の禁書がサミズダートで流通し、ソ連知識人の地下言論空間を形成した。",
    background="ソ連検閲制度（グラヴリート）下での合法出版経路の閉鎖、知識人言論空間の自主構築の必要性。",
    development="タミズダート（国外出版経路、ヨーロッパからの逆流通）と並行・連動し、ソ連体制崩壊までの主要な対抗的出版形態として機能した。",
    historical_context="1950-80年代ソ連の文化的二重構造の形成期、ソ連反体制運動（ディシデント運動）の制度的基盤。",
    primary_source_url=WIKI_EN+"Samizdat",
    primary_source_type="Wikipedia: Samizdat",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"サミズダートは制度外の流通網を通じてテキストが受容される独特の様態を示す。AI生成テキストが正規パブリッシングを経ずSNS・コミュニティ内で流通する現代と構造的類似があり、受容理論の新たな枠組みとして再読される。",
         "related_ai_phenomenon":"AI生成テキストの非公式流通と受容"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"サミズダートは流通リスクを引き受けて読まれるテキストとして、読み手と書き手の真正性が公式出版以上に強く担保される。AI時代の真正性問題の対比軸として参照される。",
         "related_ai_phenomenon":"AI時代における真正性の制度的担保"}])

add(**C, name_ja="タミズダート（国外出版）",
    name_en="tamizdat / publication abroad",
    name_original="тамиздат",
    period_key="ソヴィエト期文学",
    definition="ソ連で出版禁止された作品が国外（西欧・米国の亡命出版社）で出版される実践。「あちらで出版する（там-издат）」の意。YMCAプレス（パリ）、アルディス（米ミシガン）、ポセフ（フランクフルト）等の亡命出版社が中心となり、パステルナーク、ソルジェニーツィン、ブロツキー等を出版し、ソ連へ密輸入された。",
    background="冷戦下の東西文化的ネットワーク、ロシア亡命知識人共同体の出版活動。",
    development="1991年ソ連崩壊後、タミズダート出版社の多くが活動停止または本国回帰。20世紀後半の冷戦下文化政治の象徴的形態。",
    historical_context="冷戦下の東西言論空間の構造化と、ロシア文学の亡命的二重存在。",
    primary_source_url=WIKI_EN+"Tamizdat",
    primary_source_type="Wikipedia: Tamizdat",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヨシフ・ブロツキー",
    name_en="Joseph Brodsky",
    name_original="Иосиф Бродский",
    period_key="ソヴィエト期文学",
    definition="ヨシフ・ブロツキー(Иосиф Бродский, 1940-1996)はレニングラード生まれの詩人。1964年「社会的寄生者」として裁判・流刑、1972年国外追放。米国亡命中に英語と露語の双方で詩作・批評を展開し、1987年ノーベル文学賞、1991年米国桂冠詩人を受賞した。20世紀後半ロシア詩の最重要人物の一人で、アフマートヴァに直接師事した最後の詩人として位置づけられる。",
    background="アフマートヴァ晩年圏の詩的継承、ペテルブルク詩学の伝統、英米詩（オーデン、エリオット）の受容。",
    development="亡命詩人として、亡命言語論・帝国詩論の批評的著作（『一篇の詩より少なく』『悲嘆と理性について』）を発表し、20世紀亡命文学の中心的位置を占めた。",
    historical_context="ソヴィエト後期の知識人弾圧体制と、亡命作家の冷戦下国際的活動の典型例。",
    primary_source_url=WIKI_EN+"Joseph_Brodsky",
    primary_source_type="Wikipedia: Joseph Brodsky",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"亡命の哲学・帝国論",
         "description":"ブロツキーの亡命と帝国に関する批評的著作は20世紀亡命知識人哲学（アーレント、サイード）と並行的位置を占める。"}])

add(**C, name_ja="アフマートヴァ後期",
    name_en="late Akhmatova",
    name_original="поздняя Ахматова",
    period_key="ソヴィエト期文学",
    definition="1940-66年のアフマートヴァ後期作品群。『主人公なしの叙事詩（Поэма без героя）』(1940-65)を中心に、ロシア銀の時代の文化的記憶と20世紀の歴史的悲劇を、複層的な時代意識・複数の声・引用と暗示の織物として総合した。20世紀ロシア詩史記述的詩の頂点。",
    background="1946年ジダーノフ批判による出版禁止、1949年息子レフ三度目の逮捕、20世紀前半の生き残りとしての歴史的記憶の重荷。",
    development="1958年部分復権、1965年オックスフォード名誉博士号、世界的再評価。1966年没後、20世紀ロシア詩の規範的位置を確立した。",
    historical_context="スターリン期-雪解け期-停滞期を生き抜いた最後の銀の時代詩人としての歴史的位置。",
    primary_source_url=IMWERDEN+"axmatova-anna",
    primary_source_type="ImWerden: Akhmatova",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="グラーグ文学",
    name_en="gulag literature",
    name_original="лагерная литература",
    period_key="ソヴィエト期文学",
    definition="ソ連強制収容所体験を主題とする文学ジャンル。ソルジェニーツィン『イワン・デニーソヴィチの一日』『収容所群島』、シャラーモフ『コルィマ物語』、ギンズブルク『明るい夜・暗い昼』、ドンブロフスキー『無用なものの学』等が含まれる。20世紀全体主義文学の中核ジャンルを成し、ナチス収容所文学（レーヴィ、ヴィーゼル）と理論的に並行する。",
    background="ソ連グラーグ収容所制度（1918-1956本格運用）下の数千万人収容体験、雪解け期の証言文学解禁。",
    development="1956年第20回党大会以降の段階的解禁を経て、ペレストロイカ期にシャラーモフ等の出版が完成した。",
    historical_context="20世紀全体主義の主要証言文学ジャンルとして、世界文学・思想史の重要参照源。",
    primary_source_url=WIKI_EN+"Gulag_literature",
    primary_source_type="Wikipedia: Gulag literature",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"証言文学・全体主義論",
         "description":"グラーグ文学はナチス収容所文学（レーヴィ）と並ぶ20世紀全体主義の証言文学的核心。"}])

add(**C, name_ja="ディシデント詩",
    name_en="dissident poetry",
    name_original="диссидентская поэзия",
    period_key="ソヴィエト期文学",
    definition="1960-80年代のソヴィエト反体制（ディシデント）運動と連動した詩的実践。サミズダート流通の地下詩、公的場所での詩朗読、出版禁止作家による詩作を含む。ガリッチ、オクジャワ、ヴィソツキー等の「アヴァルド・バルド（吟遊詩人）」運動と、ブロツキー、サパギン等のテキスト中心詩運動の二系統がある。",
    background="フルシチョフ雪解け期の文化解放と、その後のブレジネフ期の再強化、サミズダート流通網の確立。",
    development="バルド詩はソ連晩期の都市文化現象として広範な大衆受容を獲得し、1991年以降もロシア文化の遺産として継続。",
    historical_context="1960-80年代ソヴィエト後期の文化的二重構造と、対抗的詩的実践の制度化。",
    primary_source_url=WIKI_EN+"Soviet_dissidents",
    primary_source_type="Wikipedia: Soviet dissidents",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シャラーモフ『コルィマ物語』",
    name_en="Shalamov's Kolyma Tales",
    name_original="Колымские рассказы",
    period_key="ソヴィエト期文学",
    definition="ヴァルラム・シャラーモフ(Варлам Шаламов, 1907-1982)による1954-73年執筆の短編集。シベリア・コルィマ収容所での17年間（1937-53）の体験を、極限状況下の人間の最低限への還元として凍結された散文で記録した。ソルジェニーツィンと対比される非ヒューマニズム的・非救済的グラーグ文学の代表作。",
    background="シャラーモフ自身のコルィマ収容所体験、1956年釈放後の地下執筆、文学的実存の極限的記述志向。",
    development="サミズダート流通を経て、1978年ロンドン初出版、1988年以降ソ連内出版。20世紀収容所文学の哲学的徹底性において、ソルジェニーツィンに匹敵する評価を確立。",
    historical_context="20世紀ロシア収容所文学の二大代表作の一つ、極限状況の記述文学の頂点。",
    primary_source_url=WIKI_EN+"Kolyma_Tales",
    primary_source_type="Wikipedia: Kolyma Tales",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============================================================
# D: ポスト・ソヴィエト（8件）
# ============================================================
add(**C, name_ja="ペレーヴィン・ポストモダン",
    name_en="Pelevin's postmodernism",
    name_original="постмодернизм Пелевина",
    period_key="ポスト・ソヴィエト文学",
    definition="ヴィクトル・ペレーヴィン(Виктор Пелевин, 1962-)を中心とするポスト・ソヴィエト・ロシア・ポストモダン文学。『チャパーエフと空虚』(1996)、『ジェネレーションP』(1999)、『t』(2009)等で、ソヴィエト崩壊後のロシア現実を、仏教・チベット密教・サイバーパンク・広告文化を素材に虚構化・脱中心化する独自の方法を展開した。",
    background="ソ連崩壊期の現実認識危機、西欧ポストモダン文学（ピンチョン、デリーロ）の受容、ロシア東洋主義・神秘主義の継承。",
    development="現代ロシア文学の国際的代表作家として、世界40言語以上に翻訳された。21世紀ロシア文学の主要潮流の一つを形成。",
    historical_context="1990年代ロシア社会の総体的変動期と、ポストモダン文学の世界的流行が交差した時代。",
    primary_source_url=WIKI_EN+"Victor_Pelevin",
    primary_source_type="Wikipedia: Victor Pelevin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウラジーミル・ソローキン",
    name_en="Vladimir Sorokin",
    name_original="Владимир Сорокин",
    period_key="ポスト・ソヴィエト文学",
    definition="ウラジーミル・ソローキン(Владимир Сорокин, 1955-)はモスクワ・コンセプチュアリズム出身のロシア作家。『行列』(1985)、『青脂』(1999)、『親衛隊員の日』(2006)、『砂糖のクレムリン』(2008)等で、ソ連的言語ステレオタイプの解体・パロディ・グロテスク化を通じて、ロシア社会の文化的無意識を文学的に発掘した。",
    background="モスクワ・コンセプチュアリズム（プリゴフ、ルビンシュテイン）の文学的展開、ソ連社会主義リアリズム言説の批判的継承。",
    development="プーチン期に入り、政治的寓話作品（『砂糖のクレムリン』『親衛隊員の日』）で現代ロシア政治体制の批判的写像を提示。21世紀ロシア・ディストピア文学の中心的人物。",
    historical_context="ソ連末期の地下文学から、ポスト・ソヴィエト文化政治の批判者への移行。",
    primary_source_url=WIKI_EN+"Vladimir_Sorokin",
    primary_source_type="Wikipedia: Vladimir Sorokin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モスクワ・コンセプチュアリズム",
    name_en="Moscow Conceptualism",
    name_original="московский концептуализм",
    period_key="ソヴィエト期文学",
    definition="1970年代後半から1980年代に発達したソ連地下芸術・文学運動。プリゴフ、ルビンシュテイン、モナストィルスキー、カバコフ等を中心とし、ソ連公式言説（社会主義リアリズム、党スローガン、官僚言語）を引用・反復・脱文脈化することで、その内的空虚を露呈させる方法を展開した。",
    background="ソヴィエト後期の言説的飽和、西欧コンセプチュアル・アートの間接的受容、地下芸術ネットワークの成熟。",
    development="ペレストロイカ・1990年代以降、国際的展示・出版を通じて世界的承認を獲得。ロシア・ポストモダニズム文学の理論的祖型となった。",
    historical_context="ソヴィエト後期の文化的二重構造の極期、地下芸術の制度的成熟。",
    primary_source_url=WIKI_EN+"Moscow_Conceptualists",
    primary_source_type="Wikipedia: Moscow Conceptualists",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"モスクワ・コンセプチュアリズムは公式言説の引用・反復・脱文脈化を通じて言語の意味空転を露呈させる。LLMが学習データの言語パターンを統計的に再生産する状況において、「公式言説の空転」をどう判定するかという問題と理論的に共鳴する。",
         "related_ai_phenomenon":"LLM生成における言説パターンの空転と意味"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"コンセプチュアリズムの「他者の言葉の引用」を主体化する戦略は、AI共著における借用・引用・真正性の問題の文学的祖型として再読される。",
         "related_ai_phenomenon":"AI共著における借用・引用と真正性"}])

add(**C, name_ja="ソツ・アート文学",
    name_en="sots-art literature",
    name_original="соц-арт",
    period_key="ソヴィエト期文学",
    definition="1970-80年代に成立した、社会主義リアリズム公式言説をパロディ的に引用・反復する文学・美術運動。コマール&メラミッド美術運動の文学版として、コマールらと連動した文学者（プリゴフ、ヴィクトル・エロフェーエフら）が、ソ連公式文学のステレオタイプを脱構築する作品を生んだ。モスクワ・コンセプチュアリズムと密接に連動。",
    background="社会主義リアリズム公式言説の硬直化、地下芸術における引用・パロディ戦略の発達。",
    development="ペレストロイカ以降、欧米美術市場でソ連美術の代表的潮流として国際化、文学的影響もポスト・ソ連散文に継承された。",
    historical_context="ソヴィエト後期の公式文化への内部からの解体運動。",
    primary_source_url=WIKI_EN+"Sots_Art",
    primary_source_type="Wikipedia: Sots Art",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ポスト・ソ連リアリズム",
    name_en="post-Soviet realism / new realism",
    name_original="постсоветский реализм",
    period_key="ポスト・ソヴィエト文学",
    definition="2000年代以降のロシア文学に登場した新リアリズム潮流。ザハール・プリレーピン、ローマン・センチン、アンドレイ・ゲラーシモフ等を中心とし、1990年代ポストモダンの言語遊戯から離れ、ロシア地方・労働者・チェチェン戦争・ロシア社会の傷をリアリズム的に描き直す志向を共有する。",
    background="1990年代ポストモダニズムの飽和、ロシア社会の経済的・地政学的危機への文学的応答必要性。",
    development="2000-10年代のロシア文学賞（『ボリシャヤ・クニーガ』『ロシア・ブッカー賞』等）を独占的に受賞し、現代ロシア文学の主要潮流の一つを形成。",
    historical_context="プーチン期ロシア社会の保守化と、文学による社会現実の再認識志向。",
    primary_source_url=WIKI_EN+"Russian_literature",
    primary_source_type="Wikipedia: Russian literature (contemporary)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="現代ロシア女性作家",
    name_en="contemporary Russian women writers",
    name_original="современные русские писательницы",
    period_key="ポスト・ソヴィエト文学",
    definition="ペレストロイカ以降に台頭した現代ロシア女性作家群。リュドミラ・ペトルシェフスカヤ、リュドミラ・ウリツカヤ、タチヤナ・トルスタヤ、グゼリ・ヤヒナ、マリア・ステパノヴァ等を含む。ソヴィエト的男性中心文学伝統を相対化し、家族史・身体・記憶・移民経験を主題に、20世紀ロシアの民間生活史を文学化する潮流を形成。",
    background="ペレストロイカ期の女性作家解禁、世界的フェミニズム文学の受容、ソ連時代の家族史的記憶への文学的アクセス必要性。",
    development="2010年代以降、国際的翻訳と国内文学賞の双方で主導的位置を獲得し、現代ロシア文学の中心的潮流の一つとなった。",
    historical_context="ソ連男性中心的文学カノンの相対化と、女性的視点による20世紀ロシア史再記述の動向。",
    primary_source_url=WIKI_EN+"Russian_literature",
    primary_source_type="Wikipedia: Russian literature (contemporary)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ユーラシア主義文学",
    name_en="Eurasianist literature",
    name_original="евразийская литература",
    period_key="ポスト・ソヴィエト文学",
    definition="1920年代亡命ロシア知識人のユーラシア主義（トルベツコイ、サヴィツキー）を起源とし、ポスト・ソ連期に文学的にも復興した思想・文学潮流。ロシアを単純な欧州・アジアではなく、両者を含む独自文化圏「ユーラシア」として把握する。プロハーノフ等の現代ナショナリスト文学にも継承される。",
    background="1920年代亡命知識人のユーラシア主義、ソ連崩壊後のロシア・アイデンティティ再構築の必要性。",
    development="2000年代以降、政治運動（ドゥーギン）と文学運動の連動として、ロシア国内ナショナリスト文学に影響。",
    historical_context="ポスト・ソ連ロシア社会のアイデンティティ模索と、文化思想的多元化の一つの軸。",
    primary_source_url=WIKI_EN+"Eurasianism",
    primary_source_type="Wikipedia: Eurasianism",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="現代亡命ロシア文学",
    name_en="contemporary Russian exile literature",
    name_original="современная эмигрантская литература",
    period_key="ポスト・ソヴィエト文学",
    definition="2000年代以降、特に2014年ウクライナ危機・2022年戦争以降に再活性化した、欧米・イスラエル・ジョージア等に居住するロシア語作家の文学。ボリス・アクーニン、ドミトリー・ブィコフ、ミハイル・シーシキン、リュドミラ・ウリツカヤ等が含まれる。20世紀の三波亡命文学（革命後・戦後・1970年代）に続く、第四波亡命文学を構成する。",
    background="ポスト・ソ連ロシア国内の言論統制強化、戦争状態下での作家の道徳的・物理的選択。",
    development="国際的翻訳・出版ネットワーク、デジタル出版・サミズダート的SNS流通を通じて、新たな亡命文学公共圏を形成中。",
    historical_context="21世紀ロシア言論空間の二重化と、亡命文学の歴史的再帰。",
    primary_source_url=WIKI_EN+"Russian_emigration",
    primary_source_type="Wikipedia: Russian emigration",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

# ============================================================
# E: 主要批評・理論概念（8件）
# ============================================================
add(**C, name_ja="バフチン「クロノトポス」",
    name_en="Bakhtin's chronotope",
    name_original="хронотоп",
    period_key="ソヴィエト期文学",
    definition="バフチン『小説における時間と時空間（クロノトポス）の形式』(1937-38, 1973刊)で展開された理論的概念。「クロノトポス（時空間）」とは、文学作品における時間と空間の内在的に結合された構造を指し、ジャンル・物語・人物造形を規定する基本枠組みとして把握される。「広場のクロノトポス」「街道のクロノトポス」等の類型化を提示。",
    background="アインシュタイン物理学の時空間概念のメタファー的援用、ロシア・フォルマリズムの内在的形式分析の継承。",
    development="20世紀後半物語論・ジャンル論の中核概念となり、文学地理学・場所論・空間論にも応用された。",
    historical_context="バフチン中期の主要理論的著作で、ジャンル論・物語論の基礎を築いた。",
    primary_source_url=WIKI_EN+"Chronotope",
    primary_source_type="Wikipedia: Chronotope",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"クロノトポス・物語の時空間",
         "description":"クロノトポスはバフチン詩学・物語論の中核概念であり、PT-DBの主要理論的参照対象。"}])

add(**C, name_ja="ロトマン文化記号論",
    name_en="Lotman's cultural semiotics",
    name_original="семиотика культуры Лотмана",
    period_key="ソヴィエト期文学",
    definition="ユーリ・ロトマン(Юрий Лотман, 1922-1993)を中心とするタルトゥ＝モスクワ記号論学派の理論。文化を「記号圏（семиосфера）」として構造化し、文化テクストの内在的構造分析と、文化間翻訳・境界・他者の構造的不可避性を理論化した。『プーシキン論』『ロシア文化に関する講義』等の歴史記号論的著作で実証された。",
    background="ロシア・フォルマリズムの継承、プラハ言語学サークル経由の構造主義、20世紀ソヴィエト・サイバネティクス・情報理論の影響。",
    development="20世紀後半の文化記号論・文化研究の主要源泉となり、西欧文学理論・人類学にも影響した。",
    historical_context="ソヴィエト後期の理論的革新、エストニア・タルトゥの相対的に自由な学術空間における記号論共同体形成。",
    primary_source_url=WIKI_EN+"Yuri_Lotman",
    primary_source_type="Wikipedia: Yuri Lotman",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化記号論・記号圏",
         "description":"ロトマンの文化記号論は人類学的文化分析と並行的に発展し、文化人類学・文学人類学の重要参照源。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"記号論・テクスト理論",
         "description":"ロトマンのテクスト理論は哲学的テクスト論（リクール、デリダ）と並行する20世紀記号論の独立的源泉。"}])

add(**C, name_ja="文学性（リテラトゥールノスチ）",
    name_en="literariness / literaturnost",
    name_original="литературность",
    period_key="ロシア銀の時代",
    definition="ヤコブソン『新最近のロシア詩』(1921)で定式化された、ロシア・フォルマリズムの中核概念。「文学研究の対象は文学そのものではなく、ある言語表現を文学的たらしめる『文学性』である」とする方法論的命題。ヤコブソン後年の「詩的機能」概念に発展継承された。",
    background="ロシア銀の時代詩学、フッサール本質直観論、ソシュール・ラング/パロル区別の方法論的並行。",
    development="プラハ言語学サークル「詩的機能」概念、フランス構造主義詩学（バルト「文学のゼロ度」）の理論的祖型となった。",
    historical_context="ロシア・フォルマリズム創立期の方法論的核心。",
    primary_source_url=WIKI_EN+"Russian_formalism",
    primary_source_type="Wikipedia: Russian formalism",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"文学性は「ある言語表現を文学的たらしめる」固有特性を理論化する。LLMが文学的・非文学的テキストを統計的に区別困難な状況において、「文学性」を判定する基準そのものが理論的争点として再活性化する。",
         "related_ai_phenomenon":"LLM時代における文学性の判定基準"},
        {"axis":"創造性","status":"rethinking",
         "rationale":"文学性概念はロシア・フォルマリズムの創造性論の中核。AI生成テキストの文学的価値判定の理論的軸として、現代に再読される。",
         "related_ai_phenomenon":"AI生成テキストの文学的価値判定"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"文学性・詩的機能",
         "description":"文学性概念はPTフォルマリズム詩学の中核で、20世紀構造主義詩学の理論的源泉。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"文学的テキスト判定指標",
         "description":"文学性概念はAI生成における文学的判定指標の理論的祖型として並行的に検討される。"}])

add(**C, name_ja="トィニャーノフ文学進化論",
    name_en="Tynyanov's literary evolution",
    name_original="литературная эволюция Тынянова",
    period_key="ロシア銀の時代",
    definition="ユーリ・トィニャーノフ(Юрий Тынянов, 1894-1943)が論文『文学進化について』(1927)で展開した、ロシア・フォルマリズム後期の文学史理論。文学を独立した体系（システム）として把握し、ジャンル・主題・スタイルの内的力動を「文学進化」として記述する方法論。中心と周縁、自動化と異化、規範と逸脱の弁証法を中核とする。",
    background="ロシア・フォルマリズム後期の体系論的転回、生物進化論・サイバネティクスのメタファー的援用。",
    development="1928年ヤコブソン共同声明『言語と文学の研究の問題』に結実し、20世紀文学史記述の理論的祖型となった。",
    historical_context="ロシア・フォルマリズム末期の方法論的成熟期。",
    primary_source_url=WIKI_EN+"Yury_Tynyanov",
    primary_source_type="Wikipedia: Yury Tynyanov",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シュジェート vs ファーブラ",
    name_en="sjuzhet vs fabula",
    name_original="сюжет и фабула",
    period_key="ロシア銀の時代",
    definition="ロシア・フォルマリズム（特にOPOJAZ）が定式化した物語論の二項対立。「ファーブラ（фабула）」は物語素材の年代順・因果順の総体（出来事の自然的順序）、「シュジェート（сюжет）」はテクストにおける物語素材の文学的構成・配列・歪曲を指す。プロップ、トドロフ、ジュネット物語論の理論的祖型を成す。",
    background="ロシア・フォルマリズム創立期、シクロフスキー・トマシェフスキー『文学理論』(1925)による定式化。",
    development="20世紀後半の物語論（ジュネット『物語の言説』、チャットマン）の中核区別となり、現代物語論の基礎概念。",
    historical_context="ロシア・フォルマリズム理論的体系化の中核成果。",
    primary_source_url=WIKI_EN+"Fabula_and_syuzhet",
    primary_source_type="Wikipedia: Fabula and syuzhet",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語素・物語の構成",
         "description":"シュジェート/ファーブラ区別はPT物語論の基礎概念として継承されている。"}])

add(**C, name_ja="プロップ後継：物語形態論",
    name_en="Propp's legacy: narrative morphology",
    name_original="морфология сказки (наследие)",
    period_key="ソヴィエト期文学",
    definition="ウラジーミル・プロップ(Владимир Пропп, 1895-1970)『昔話の形態学』(1928)以降の物語形態論の発展。プロップが定式化した31機能・7類型による魔法昔話分析を起点に、20世紀後半のフランス構造主義物語論（グレマス、ブレモン、トドロフ、ジュネット）に体系的に継承された。",
    background="ロシア・フォルマリズムの内在的構造分析、ロシア民俗学の蓄積（アファナシエフ昔話集）。",
    development="1958年英訳出版以降、レヴィ＝ストロース構造神話論との論争を経て、20世紀後半世界物語論の主要源泉となった。",
    historical_context="ロシア・フォルマリズムの民俗学的応用と、その20世紀後半の世界的継承。",
    primary_source_url=WIKI_EN+"Vladimir_Propp",
    primary_source_type="Wikipedia: Vladimir Propp",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語形態学・31機能",
         "description":"プロップ31機能はPT-DB物語論の基底参照点。"},
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"プロップ機能",
         "description":"プロップ物語形態論はMyth-Narratives DBの主要分析フレームの一つ。"}])

add(**C, name_ja="ロシア構造主義詩学",
    name_en="Russian structuralism in poetics",
    name_original="русский структурализм",
    period_key="ソヴィエト期文学",
    definition="1960-80年代のロシア（特にタルトゥ＝モスクワ学派）に展開した構造主義文学・文化研究。ロトマン、ウスペンスキー、トポロフ、イヴァーノフ等を中心人物とし、ロシア・フォルマリズム遺産とプラハ言語学サークル・西欧構造主義を独自に統合した。文学テクストの内在的構造分析・文化記号論・文学史記号論を主要領域とする。",
    background="ロシア・フォルマリズム遺産の1960年代再発見、サイバネティクス・情報理論の影響、エストニア・タルトゥの相対的自由な学術空間。",
    development="1990年代以降、英語訳出版を通じて世界的に再評価され、ロシア人文学最高水準の理論的成果として位置づけられた。",
    historical_context="ソヴィエト後期の理論的革新運動、ペレストロイカに先立つ知的解放の象徴。",
    primary_source_url=WIKI_EN+"Tartu%E2%80%93Moscow_Semiotic_School",
    primary_source_type="Wikipedia: Tartu-Moscow Semiotic School",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"構造主義・記号論",
         "description":"ロシア構造主義詩学は20世紀構造主義哲学の独立的源泉として、フランス構造主義と並行する位置を占める。"}])

add(**C, name_ja="ヤコブソン「詩的機能」",
    name_en="Jakobson's poetic function",
    name_original="поэтическая функция",
    period_key="ソヴィエト期文学",
    definition="ヤコブソン『言語学と詩学』(1958, 1960刊)で定式化された言語機能モデルの中核概念。コミュニケーションの六要素（送り手・受け手・文脈・メッセージ・接触・コード）に対応する六機能の一つで、メッセージそれ自体への志向を示す機能。「等価原理が選択軸から組み合わせ軸へ投影される」と定式化される。",
    background="ロシア・フォルマリズム『文学性』概念の発展、プラハ言語学サークル機能主義、ビューラー言語三機能論の継承。",
    development="20世紀後半構造主義詩学・記号論の中核概念となり、文学言語の内在的特性論の主要参照点となった。",
    historical_context="ヤコブソン米国時代の理論的成熟期、ロシア・フォルマリズム遺産の世界化の頂点。",
    primary_source_url=WIKI_EN+"Jakobson%27s_functions_of_language",
    primary_source_type="Wikipedia: Jakobson's functions of language",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"詩的機能・言語六機能",
         "description":"ヤコブソン詩的機能はPT詩学の中核理論であり、20世紀詩論の基礎概念。"}])


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="周縁横断",
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
        print(f"[c29] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c29] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
