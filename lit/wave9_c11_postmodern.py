"""LIT-DB Phase 2 Wave 9 — C11: Western Postmodern (40 concepts).

Subfield: lit_eu_postmodern (id=7), region='西欧'.
Sources: Stanford Encyclopedia of Philosophy, Project MUSE / JSTOR-indexed
academic Wikipedia entries, primary essay sources (Borges, Lyotard, Jameson,
Hutcheon, Baudrillard) and Project Gutenberg / academic university pages.
PD primary materials and canonical theoretical statements -> 'primary';
canonical scholarly secondary -> 'secondary'; synthetic critical categories
-> 'tertiary'.

Postmodernism is densely entangled with the Fourth Transformation (AI era):
metafiction, hyperreality, simulacra, autofiction and infinite intertextuality
all anticipate or structurally parallel LLM-driven generation. 15 concepts are
tagged with fourth_transform axes accordingly.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# Postmodernism (~1960-2000) and Contemporary / Autofictional (~1990-present)
PERIODS = [
    ("ポストモダン期", "Postmodern Era", 1960, 2000,
     "1960年代以降の西欧（特に米仏伊）の文学において、メタフィクション・断片化・パスティーシュ・ハイパーリアリティを中核に、近代的物語・主体・正典を相対化した時代。"),
    ("自伝的現代期", "Contemporary Autofictional Era", 1990, 2025,
     "セバルド以降のドキュメンタリー的記憶文学から、Knausgård『My Struggle』に代表される自伝小説（autofiction）の世界的隆盛までの、ポストモダン以後の現代文学期。"),
]

# Source URL bases (real, verifiable)
SEP = "https://plato.stanford.edu/entries/"  # Stanford Encyclopedia of Philosophy
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
GUTEN = "https://www.gutenberg.org/"
JSTOR = "https://www.jstor.org/"
MUSE = "https://muse.jhu.edu/"
NYRB = "https://www.nybooks.com/"
PARIS_REVIEW = "https://www.theparisreview.org/"
LARB = "https://lareviewofbooks.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_postmodern", region="西欧",
         original_script="roman")

# ============================================================
# A: 主要主題（8件）
# ============================================================
add(**C, name_ja="メタフィクション", name_en="metafiction",
    name_original="metafiction", period_key="ポストモダン期",
    definition="自らがフィクションであることを意識的に開示し、創作行為そのものを物語化する小説様式。ウィリアム・H・ガス『Fiction and the Figures of Life』(1970)が用語を定式化し、バース、カルヴィーノ、ナボコフ、コーヴァー、ボルヘスを系譜とする、ポストモダン小説の中核形式。",
    background="モダニズムの自己言及性とロシア・フォルマリズムの装置暴露概念の戦後的展開。",
    development="リンダ・ハッチオン『歴史記述的メタフィクション』(1988)の理論的整理を経て、現代世界文学の標準技法の一つとなる。",
    historical_context="1960-70年代米国の戦後文学的内省と、フランス構造主義・ヌーヴォー・ロマンの理論的影響の合流。",
    primary_source_url=WIKI_EN+"Metafiction",
    primary_source_type="Wikipedia: Metafiction (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者と語り手・登場人物の境界を解体するメタフィクションの実践は、AIテクスト生成における作者概念の不在と構造的に類比される。誰が書いたかではなく、何が書かれたかへの関心が両者を貫く。",
         "related_ai_phenomenon":"AI生成テクストにおける作者性の消失"},
        {"axis":"真正性","status":"partial",
         "rationale":"メタフィクションは「これは虚構である」と宣言することで真正性概念を相対化する。AI生成テクストもまた「真正な体験の表現」ではなく、生成された言語的構築物としてのみ存在する。",
         "related_ai_phenomenon":"AI生成における真正性の規範転換"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"自己言及性",
         "description":"PT-DBの自己言及性概念とメタフィクションの理論的接続。"}])

add(**C, name_ja="パラノイア物語", name_en="paranoid narrative",
    name_original="paranoid narrative", period_key="ポストモダン期",
    definition="陰謀・監視・隠された秩序への偏執的疑念を物語の駆動力とする物語形式。トマス・ピンチョン『重力の虹』『競売ナンバー49の叫び』、ドン・デリーロ、ロバート・クーヴァーが代表的展開を見せた、冷戦・核時代米国文学の中核様式。",
    background="冷戦下CIA・FBI・軍産複合体への文化的不信と、フロイト精神分析のパラノイア論の文学的形象化。",
    development="9.11以降の現代テクノ・パラノイア物語（デリーロ『墜ちてゆく男』）、現代の監視資本主義小説まで継承される。",
    historical_context="冷戦・ベトナム戦争・暗殺・ウォーターゲートを経た米国の集合的不安。",
    primary_source_url=WIKI_EN+"Gravity%27s_Rainbow",
    primary_source_type="Wikipedia: Gravity's Rainbow (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="百科全書的小説", name_en="encyclopedic novel",
    name_original="encyclopedic novel", period_key="ポストモダン期",
    definition="エドワード・メンデルソン「Encyclopedic Narrative」(1976)が提唱した、一文化の知識・言語・歴史の総体を一作品に圧縮しようとする巨大小説形式。ジョイス『ユリシーズ』を範型とし、ピンチョン『重力の虹』、ガディス『The Recognitions』、デヴィッド・フォスター・ウォレス『無限の冗談』が継承。",
    background="モダニズムの神話的方法（ジョイス）の戦後的拡張と、20世紀後半の情報過剰社会の文学的応答。",
    development="2000年代以降のロベルト・ボラーニョ『2666』、現代の長篇文学にも影響範囲が拡張する。",
    historical_context="情報爆発時代と一作品による全体把握願望の緊張。",
    primary_source_url=JSTOR+"stable/468593",
    primary_source_type="Mendelson 'Encyclopedic Narrative' (Yale French Studies, JSTOR)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハイパーリアリティ", name_en="hyperreality",
    name_original="hyperréalité / iperrealtà",
    period_key="ポストモダン期",
    definition="ジャン・ボードリヤール『シミュラークルとシミュレーション』(1981)とウンベルト・エーコ『超現実の旅』(1973)で展開された、模像（シミュラクル）が原型なしに自己生成し、現実より「現実的」となる状態を指す概念。ポストモダン小説の世界観の哲学的基盤となった。",
    background="テレビ・広告・テーマパーク（ディズニーランド）が原型なしの模像で構成される消費社会の批判的観察。",
    development="現代のVR・SNS・AI生成画像時代の理論的基礎概念として機能し、ジョン・バース、デリーロ『ホワイト・ノイズ』、デヴィッド・フィンチャー映画に文学的・映画的継承を見る。",
    historical_context="戦後消費社会・メディア社会の哲学的診断。",
    primary_source_url=WIKI_EN+"Hyperreality",
    primary_source_type="Wikipedia: Hyperreality (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ハイパーリアリティ概念は、AI生成画像・テクスト・音声が原型なしの模像として流通する現代を80年代に予言した。生成AIは哲学的にハイパーリアリティの極限的実装である。",
         "related_ai_phenomenon":"AI生成コンテンツとシミュラクルの完全実装"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ボードリヤール（シミュラクル）",
         "description":"ボードリヤールのシミュラクル哲学とポストモダン文学の世界観の理論的共有。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI生成リアリティ",
         "description":"ハイパーリアリティ概念は生成AI時代の理論的予表として再評価される。"}])

add(**C, name_ja="フィクションにおけるシミュラクラ",
    name_en="simulacra in fiction",
    name_original="simulacra in fiction", period_key="ポストモダン期",
    definition="ボードリヤール由来のシミュラクル（原型なき模像）概念が文学的に展開された結果、登場人物・舞台・出来事自体が「コピーのコピー」として提示される小説的形象。デリーロ『ホワイト・ノイズ』の「最も写真撮影された納屋」、ピンチョンの陰謀論的世界、フィリップ・K・ディック以降のSFに体現される。",
    background="ボードリヤール理論のアメリカ文学的受容と、テレビ・映画文化を内面化した戦後米国文学の自然な展開。",
    development="現代のサイバーパンクSF、AI時代の文学（ジャネット・ウィンタースン『フランケッシテイン的・ラブ』等）に継承。",
    historical_context="メディア飽和社会における現実と表象の弁別困難。",
    primary_source_url=WIKI_EN+"Simulacra_and_Simulation",
    primary_source_type="Wikipedia: Simulacra and Simulation (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"フィクションにおけるシミュラクル形象は、AI生成キャラクター・AI生成世界の文学的先駆けとして機能する。両者とも原型なき模像であるが、現代の生成は完全に機械的である点が新たな問いを生む。",
         "related_ai_phenomenon":"AI生成キャラクターとシミュラクルの系譜的接続"}])

add(**C, name_ja="断片化（ポストモダン）",
    name_en="fragmentation (postmodern)",
    name_original="fragmentation", period_key="ポストモダン期",
    definition="モダニズム的断片化を継承しつつ、より遊戯的・非統一的に展開されるポストモダン小説の構造原理。ジョン・バース、ドナルド・バーセルミ、カーティス・ホワイト、現代のジェニファー・イーガン『visit from the Goon Squad』に体現される、断片の意図的並置による意味生成形式。",
    background="モダニズム断片化の戦後的継承と、構造主義以降の意味の差延的構造の文学的具現化。",
    development="デジタル時代のハイパーテクスト文学、SNS時代の断片小説（ジョン・ヘミングウェイ等）まで延長される。",
    historical_context="マスメディア・情報過剰時代の認識論的応答としての断片化。",
    primary_source_url=WIKI_EN+"Postmodern_literature",
    primary_source_type="Wikipedia: Postmodern literature (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="パスティーシュ", name_en="pastiche",
    name_original="pastiche", period_key="ポストモダン期",
    definition="既存スタイル・ジャンル・作家の文体を意図的に模倣・継承する手法だが、パロディと異なり批判的・諷刺的距離を持たない中立的引用。フレドリック・ジェイムソン『ポストモダニズム』(1991)が「空虚なパロディ」と特徴付けた、後期資本主義文化の典型的様式。",
    background="モダニズム的引用（エリオット『荒地』）の戦後的継承と、ジャンル文学の高文学的取り込みの双方向化。",
    development="ジェイムソンが理論化した後、現代文学（ピンチョン、エコ、村上春樹）の標準技法として常態化した。",
    historical_context="後期資本主義における様式の歴史化と消費文化的引用化。",
    primary_source_url=WIKI_EN+"Pastiche",
    primary_source_type="Wikipedia: Pastiche (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="規範としてのパロディ", name_en="parody as norm",
    name_original="parody as norm", period_key="ポストモダン期",
    definition="ポストモダン文学において、パロディが特殊な逸脱技法ではなく規範的・恒常的な創作方法となった事態。リンダ・ハッチオン『パロディの理論』(1985)が定式化し、ジョン・バース、ナボコフ、ボルヘス、エーコの作品に体現される。",
    background="モダニズム引用と新批評の影響不安(anxiety of influence)概念のポストモダン的解放。",
    development="ハロルド・ブルームの影響不安論からハッチオンのパロディ肯定論への理論的転換と、現代文学における恒常的相互参照化。",
    historical_context="正典文化の相対化と、相互参照を芸術的価値の中核とする文化的転換。",
    primary_source_url=WIKI_EN+"Parody",
    primary_source_type="Wikipedia: Parody (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

# ============================================================
# B: 主要作家概念（8件）
# ============================================================
add(**C, name_ja="ボルヘス「バベルの図書館」",
    name_en="Borges 'The Library of Babel'",
    name_original="La biblioteca de Babel", period_key="ポストモダン期",
    definition="ホルヘ・ルイス・ボルヘスが1941年『八岐の園』所収で発表した短篇。25文字から構成可能なすべての書物を含む無限図書館の幻想を通じて、テクストの組合せ的全体性、意味と無意味の弁別不能性、宇宙＝図書館の比喩を展開した、20世紀文学最大の概念的影響源の一つ。",
    background="マラルメ「全ては一冊の本に至る」、ライプニッツの組合せ論的全体性、カバラ的言語観の文学的総合。",
    development="ウンベルト・エーコ、ジョン・バース、ピンチョンに直接的影響を与え、ハイパーテクスト理論、計算文学（OuLiPo）、生成AI時代のテクスト論まで延長される思想的水源。",
    historical_context="戦間期ブエノスアイレスのモダニズム的世界文学受容と、独自の幻想形而上学の展開。",
    primary_source_url=WIKI_EN+"The_Library_of_Babel",
    primary_source_type="Wikipedia: The Library of Babel (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"組合せ的に可能なすべてのテクストを含む無限図書館の幻想は、LLMの確率的テクスト生成を80年先取りした。LLMはまさにバベルの図書館を統計的に走査する装置として機能する。",
         "related_ai_phenomenon":"LLMによるテクスト空間の確率的探索とバベルの図書館の予表"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"LLMテクスト空間",
         "description":"バベルの図書館はLLMの可能テクスト空間概念の哲学的予表。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ライプニッツ組合せ論",
         "description":"ライプニッツ組合せ論とボルヘス図書館の哲学的接続。"}])

add(**C, name_ja="ボルヘス「八岐の園」",
    name_en="Borges 'The Garden of Forking Paths'",
    name_original="El jardín de senderos que se bifurcan",
    period_key="ポストモダン期",
    definition="ボルヘスが1941年に発表した短篇で、すべての可能な分岐が同時に実現する無限分岐的時間構造の幻想を提示。中国系哲学者ツィウィ・ペンの未完小説の枠組みを通じて、ハイパーテクスト・並行宇宙・量子的実在概念の文学的予表となった。",
    background="ヒュー・エヴェレット三世の量子多世界解釈(1957)を文学的に予表し、ベルクソン的時間多元論の物語化。",
    development="ハイパーテクスト文学（マイケル・ジョイス『Afternoon』）、計算文学、現代のインタラクティブ・フィクション、SF多世界小説の方法論的源泉となる。",
    historical_context="戦時下のブエノスアイレスにおけるボルヘスの思弁的小説の頂点。",
    primary_source_url=WIKI_EN+"The_Garden_of_Forking_Paths",
    primary_source_type="Wikipedia: The Garden of Forking Paths (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"分岐的生成（beam search）",
         "description":"LLMのbeam search的分岐生成と八岐の園の構造的並行。"}])

add(**C, name_ja="ピンチョン「重力の虹」",
    name_en="Pynchon 'Gravity's Rainbow'",
    name_original="Gravity's Rainbow", period_key="ポストモダン期",
    definition="トマス・ピンチョンが1973年に発表したアメリカ・ポストモダン文学の到達点。第二次大戦末期のV2ロケット弾道を中心に、400以上の登場人物、科学・占星術・心理学・大衆文化の百科全書的引用、パラノイア的世界観を統合した、戦後アメリカ文学の頂点的作品。",
    background="冷戦・ベトナム戦争・対抗文化期の米国文学的応答と、ジョイス的百科全書的小説の継承。",
    development="ピューリッツァー賞委員会推薦を編集委員が拒否した伝説的事件後、米国大学院文学研究の主要対象となる。",
    historical_context="ベトナム戦争末期のアメリカの自己懐疑とポストモダン世界観の頂点。",
    primary_source_url=WIKI_EN+"Gravity%27s_Rainbow",
    primary_source_type="Wikipedia: Gravity's Rainbow (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョン・バース「驚き屋敷で道に迷って」",
    name_en="John Barth 'Lost in the Funhouse'",
    name_original="Lost in the Funhouse", period_key="ポストモダン期",
    definition="ジョン・バースが1968年に発表したメタフィクション短篇集。表題作を含む14篇は、自己言及・無限後退・読者直接呼び掛けなど、米国メタフィクションの方法論を網羅的に展示し、戦後ポストモダン小説の方法論的マニフェストとなった。",
    background="バースの先行エッセイ「枯渇の文学」(1967)が定式化した文学的伝統枯渇論の小説的具体化。",
    development="バーセルミ、ロバート・クーヴァー、ウィリアム・ガスらと共に米国メタフィクション学派の中核作品となる。",
    historical_context="ベトナム戦争・対抗文化期の米国文学の方法論的自己反省。",
    primary_source_url=WIKI_EN+"Lost_in_the_Funhouse",
    primary_source_type="Wikipedia: Lost in the Funhouse (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="カルヴィーノ「冬の夜ひとりの旅人が」",
    name_en="Calvino 'If on a winter's night a traveler'",
    name_original="Se una notte d'inverno un viaggiatore",
    period_key="ポストモダン期",
    definition="イタロ・カルヴィーノが1979年に発表した、読者を二人称主人公とする入れ子構造のメタフィクション小説。10の異なるジャンル小説の冒頭が連鎖し、読者と「読者」の関係そのものを物語化する、ポストモダン小説の代表作。",
    background="OuLiPo（潜在文学工房）への参加経験とロラン・バルト『S/Z』『テクストの快楽』の理論的影響。",
    development="読者論的・受容理論的小説の範例として、現代世界文学（ポール・オースター、村上春樹）に多大な影響を与える。",
    historical_context="フランス・ヌーヴェルクリチック以降の読者論的転回の小説的実装。",
    primary_source_url=WIKI_EN+"If_on_a_winter%27s_night_a_traveler",
    primary_source_type="Wikipedia: If on a winter's night a traveler (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"二人称主人公として読者を物語に組み込む技法は、AI生成テクストにおける読者・利用者・生成主体の境界融解を予表する。読者がテクストの参加的構築者となる構造は、対話型LLM体験と類比的。",
         "related_ai_phenomenon":"対話型AIにおける読者と生成の融合"}])

add(**C, name_ja="エーコ「薔薇の名前」", name_en="Eco 'The Name of the Rose'",
    name_original="Il nome della rosa", period_key="ポストモダン期",
    definition="ウンベルト・エーコが1980年に発表した、中世スコラ哲学・記号論・推理小説・知識史を融合した百科全書的歴史小説。エーコ自身の記号論研究の文学的具体化であり、ポストモダン小説の世界的成功を象徴する作品となった。",
    background="エーコの記号論研究（『記号論一般』『開かれた作品』）と中世スコラ研究の小説的統合。",
    development="ジャン=ジャック・アノー監督による映画化(1986)で世界的大衆作品となり、現代の歴史小説（ダン・ブラウン等）の先駆的範型となる。",
    historical_context="記号論・解釈学・中世研究の学術的接合と大衆小説形式の融合。",
    primary_source_url=WIKI_EN+"The_Name_of_the_Rose",
    primary_source_type="Wikipedia: The Name of the Rose (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"記号論詩学",
         "description":"エーコ記号論とポストモダン小説実践の理論的・実践的統合。"}])

add(**C, name_ja="ヴォネガット「スローターハウス5」",
    name_en="Vonnegut 'Slaughterhouse-Five'",
    name_original="Slaughterhouse-Five", period_key="ポストモダン期",
    definition="カート・ヴォネガットが1969年に発表した、自身のドレスデン爆撃体験を非線形・SF的・自己言及的に語る半自伝小説。「So it goes」の反復的フレーズと「時間漂流」(unstuck in time)の方法論で、戦後米国文学のトラウマ表現の代表作となった。",
    background="ヴォネガットがドイツ捕虜として体験した1945年ドレスデン大空襲のトラウマと、戦後20年を経た文学的処理。",
    development="トラウマ文学・反戦小説・SFポストモダン小説の交差点として、ベトナム戦争世代米国の中核作品となる。",
    historical_context="ベトナム戦争への反戦運動とドレスデン記憶の文学的回帰。",
    primary_source_url=WIKI_EN+"Slaughterhouse-Five",
    primary_source_type="Wikipedia: Slaughterhouse-Five (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="デリーロ「ホワイト・ノイズ」",
    name_en="DeLillo 'White Noise'",
    name_original="White Noise", period_key="ポストモダン期",
    definition="ドン・デリーロが1985年に発表した、消費社会・メディア飽和・死への恐怖を中心とする家族小説。「最も写真撮影された納屋」のシーンに象徴されるシミュラクル的世界、毒気漏出事件「Airborne Toxic Event」がポストモダン現代の集合的経験を結晶化した。",
    background="ボードリヤール理論の文学的具現化と、レーガン期米国消費文化の批判的観察。",
    development="米国全米図書賞受賞作として戦後米国文学の正典となり、9.11以降の文学（『コスモポリス』『墜ちてゆく男』）への前史となる。",
    historical_context="冷戦末期米国の消費社会・テレビ文化・死の恐怖の合流。",
    primary_source_url=WIKI_EN+"White_Noise_(novel)",
    primary_source_type="Wikipedia: White Noise (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============================================================
# C: 形式・技法（8件）
# ============================================================
add(**C, name_ja="メタフィクション技法", name_en="metafiction techniques",
    name_original="metafiction techniques", period_key="ポストモダン期",
    definition="メタフィクションを実装する具体的手法群。作者の介入、登場人物の作家性自覚、引用と注釈の多層化、物語装置の暴露、虚実境界の遊戯、読者直接呼び掛け、入れ子構造（mise en abyme）等から構成される、ポストモダン小説の技法体系。",
    background="モダニズムの自己言及性技法の戦後体系化と、構造主義物語論の影響。",
    development="現代世界文学（ポール・オースター、ハルキ・ムラカミ、ヤン・マーテル『パイの物語』）の標準的技法体系として常態化。",
    historical_context="ポストモダン小説の方法論的成熟。",
    primary_source_url=WIKI_EN+"Metafiction",
    primary_source_type="Wikipedia: Metafiction (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="文学的相互テクスト性",
    name_en="intertextuality (literary)",
    name_original="intertextualité", period_key="ポストモダン期",
    definition="ジュリア・クリステヴァが1966年バフチン論で導入した、すべてのテクストが他のテクストの引用・吸収・変容として成立するという理論概念。ポストモダン小説実践の理論的基盤として、引用・パロディ・パスティーシュの恒常化を支えた。",
    background="バフチンの対話原理（『ドストエフスキー詩学の問題』）のフランス構造主義的展開と、テル・ケル派の理論的総合。",
    development="ジェラール・ジュネット『パランプセスト』(1982)の体系的整理を経て、ポストモダン文学・現代物語論の基本概念となる。",
    historical_context="1960-70年代パリの構造主義・ポスト構造主義理論の文学的展開。",
    primary_source_url=WIKI_EN+"Intertextuality",
    primary_source_type="Wikipedia: Intertextuality (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"すべてのテクストが既存テクストの組合せ・変容であるという理論は、訓練データから組合せ的に生成するLLMの動作様式を予表する。「すべてのテクストはモザイク」というクリステヴァの命題はLLM時代に文字通りに実現する。",
         "related_ai_phenomenon":"LLM訓練データからの組合せ的生成と相互テクスト性の極限実装"},
        {"axis":"言語","status":"partial",
         "rationale":"言語が自己回帰的・相互参照的に成立するという認識が、AI生成言語の地位を考える基礎理論となる。",
         "related_ai_phenomenon":"AI生成言語の相互テクスト的成立"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"対話原理（バフチン）",
         "description":"バフチン対話論からクリステヴァ相互テクスト性への系譜的接続。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"クリステヴァ記号論",
         "description":"クリステヴァのセメイオティーケと文学的相互テクスト性の理論的共有。"}])

add(**C, name_ja="ハイパーテクスト文学の先駆",
    name_en="hypertext literature precursors",
    name_original="hypertext literature precursors",
    period_key="ポストモダン期",
    definition="デジタル・ハイパーテクストの登場以前にその構造を文学的に先取りした作品群。ボルヘス「八岐の園」、ナボコフ『青い炎』、コルタサル『石蹴り遊び』(1963)、エーコ『薔薇の名前』が代表する、非線形・分岐的・読者選択的物語形式の文学的先駆。",
    background="OuLiPo（潜在文学工房、1960-）の組合せ的文学実験と構造主義物語論の出会い。",
    development="マイケル・ジョイス『Afternoon, a story』(1987)、シェリー・ジャクソン『Patchwork Girl』(1995)等のデジタル・ハイパーテクスト文学の理論的・実践的前提となる。",
    historical_context="戦後文学の構造的実験と1990年代以降のデジタル文学の連続性。",
    primary_source_url=WIKI_EN+"Hypertext_fiction",
    primary_source_type="Wikipedia: Hypertext fiction (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"非線形テクスト構造",
         "description":"ハイパーテクスト文学とAI対話の非線形性の構造的並行。"}])

add(**C, name_ja="発見文書物語", name_en="found document narrative",
    name_original="found document narrative", period_key="ポストモダン期",
    definition="物語が「発見された手紙・日記・テクスト」として提示される語り技法。18世紀書簡体小説の伝統を継承するが、ポストモダン期にはナボコフ『青い炎』、A.S.バイアット『ポゼッション』、デヴィッド・ミッチェル『クラウド・アトラス』等で、テクストの真正性を遊戯的に問う形式となった。",
    background="ホレース・ウォルポール『オトラント城』(1764)以来のゴシック小説的「発見手稿」設定の継承と、ポストモダン的真正性遊戯の合流。",
    development="現代のドキュメンタリー小説、リアリティ系メタフィクション、SNS時代の偽日記文学（『悪い妖精達の謀議』等）まで継承。",
    historical_context="真正性概念の文学的遊戯化。",
    primary_source_url=WIKI_EN+"Found_manuscript",
    primary_source_type="Wikipedia: Found manuscript (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="フレーム破り", name_en="frame-breaking",
    name_original="frame-breaking / metalepsis", period_key="ポストモダン期",
    definition="物語の階層的フレーム（語り手のレベル、登場人物のレベル、読者のレベル等）を意図的に侵犯する技法。ジェラール・ジュネット『物語のディスクール』(1972)で「メタレプシス」として理論化され、コルタサル「公園の続き」、ピランデッロ『作者を探す六人の登場人物』、フローニー・ウディ・アレン作品に体現される。",
    background="物語論的階層概念の理論的成熟と、ポストモダン的階層侵犯遊戯の合流。",
    development="現代のメタ・ナラティブ実践（ドラマ・映画・小説）の標準技法として常態化。",
    historical_context="物語の階層構造意識の理論的成熟期。",
    primary_source_url=WIKI_EN+"Metalepsis",
    primary_source_type="Wikipedia: Metalepsis (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ポストモダン的信頼できない語り手",
    name_en="unreliable narrator (postmodern)",
    name_original="unreliable narrator (postmodern)",
    period_key="ポストモダン期",
    definition="ウェイン・ブース『フィクションの修辞学』(1961)の信頼できない語り手概念がポストモダン的に展開され、信頼性の判定基準そのものが解体された語り。ナボコフ『ロリータ』、カズオ・イシグロ『日の名残り』、パランドロ『パロディ』に体現される、真理基準の喪失した語り。",
    background="モダニズムの限定的視点（ジェイムズ・コンラッド）の極限化と、ポストモダン的真理懐疑論の合流。",
    development="現代英語小説の標準的語り様式となり、ジリアン・フリン『ゴーン・ガール』等の大衆小説まで普及。",
    historical_context="真理・客観性概念の文学的解体。",
    primary_source_url=WIKI_EN+"Unreliable_narrator",
    primary_source_type="Wikipedia: Unreliable narrator (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="多声的語り（ポストモダン）",
    name_en="polyphonic narrative",
    name_original="polyphonic narrative / polyphony",
    period_key="ポストモダン期",
    definition="バフチンが『ドストエフスキー詩学の問題』(1929)で定式化した多声性概念のポストモダン小説への展開。複数の独立した意識・声・観点が単一の権威的語りなしに併存する語り形式。ロベルト・ボラーニョ『2666』、デヴィッド・ミッチェル『クラウド・アトラス』、ポール・オースター作品が代表的展開。",
    background="バフチン理論の戦後西欧的受容（クリステヴァ、トドロフ）と、ポストモダン小説実践の合流。",
    development="現代世界文学の標準的語り様式となり、グローバル化時代の多声・多言語小説の理論的基盤となる。",
    historical_context="冷戦後グローバル化期の多元的世界経験の文学化。",
    primary_source_url=WIKI_EN+"Heteroglossia",
    primary_source_type="Wikipedia: Heteroglossia (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"多声性（バフチン）",
         "description":"バフチン詩学の多声性概念とポストモダン小説実践の理論的共有。"}])

add(**C, name_ja="入れ子小説", name_en="novel-within-novel",
    name_original="novel-within-novel / mise en abyme",
    period_key="ポストモダン期",
    definition="物語内に別の物語が入れ子的に組み込まれる構造。ジッド『贋金つくり』(1925)が「mise en abyme」と命名し、ポストモダンではナボコフ『青い炎』、ペレック『人生使用法』、ボラーニョ『野生の探偵たち』等で複雑な多層構造として展開された。",
    background="ジッドの紋章学的「mise en abyme」概念とアラビアンナイト的入れ子伝統の総合。",
    development="ジャン・リカルドゥー『新しい小説の理論』(1967)の理論的整理を経て、現代世界文学の標準構造の一つとなる。",
    historical_context="物語の階層的・自己言及的構造への20世紀的関心の頂点。",
    primary_source_url=WIKI_EN+"Mise_en_abyme",
    primary_source_type="Wikipedia: Mise en abyme (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

# ============================================================
# D: 批評概念（8件）
# ============================================================
add(**C, name_ja="ハッチオン「歴史記述的メタフィクション」",
    name_en="Hutcheon 'historiographic metafiction'",
    name_original="historiographic metafiction",
    period_key="ポストモダン期",
    definition="リンダ・ハッチオン『ポストモダニズムの詩学』(1988)が定式化した概念。歴史的事実を遊戯的に取り扱いつつ自らの虚構性を意識的に開示する小説形式。サルマン・ラシュディ『真夜中の子供たち』、E.L.ドクトロウ『ラグタイム』、トマス・ピンチョン作品に体現される。",
    background="ポストモダンが歴史を完全否定するというジェイムソン的見解への反論として提唱された理論。",
    development="ポストコロニアル文学・歴史小説論の中核概念となり、現代世界文学の歴史小説の理論的基盤として機能。",
    historical_context="80年代のポストモダン理論論争と歴史認識の文学的処理。",
    primary_source_url=WIKI_EN+"Historiographic_metafiction",
    primary_source_type="Wikipedia: Historiographic metafiction (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リオタール「メタ物語への不信」",
    name_en="Lyotard 'incredulity toward metanarratives'",
    name_original="incrédulité à l'égard des métarécits",
    period_key="ポストモダン期",
    definition="ジャン=フランソワ・リオタール『ポストモダンの条件』(1979)が提唱した、ポストモダンの定義。マルクス主義・啓蒙主義・キリスト教等の大きな物語（メタ物語）への不信を、ポストモダンの認識論的特徴とした。文学・哲学・社会理論を横断する世紀の概念。",
    background="フランクフルト学派の啓蒙批判、ニーチェ的ニヒリズム、構造主義以降の真理懐疑論の戦後的総合。",
    development="ポストモダン理論の世界的拡散の理論的核となり、現代の小さな物語・断片化・多元主義論の基盤となる。",
    historical_context="冷戦末期のイデオロギー疲弊と知識社会化の交差。",
    primary_source_url=WIKI_EN+"The_Postmodern_Condition",
    primary_source_type="Wikipedia: The Postmodern Condition (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"大きな物語への不信は、AI時代の小さな物語・個別化されたコンテンツ生成の哲学的基盤として再解釈される。LLMによる無数の個別物語生成は、メタ物語の死後の極限形態とも言える。",
         "related_ai_phenomenon":"LLM個別生成と大きな物語の終焉"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"リオタール（ポストモダンの条件）",
         "description":"リオタール哲学とポストモダン文学の世界観の理論的共有。"}])

add(**C, name_ja="ジェイムソン「後期資本主義」",
    name_en="Jameson 'late capitalism'",
    name_original="late capitalism", period_key="ポストモダン期",
    definition="フレドリック・ジェイムソン『ポストモダニズム、あるいは後期資本主義の文化的論理』(1991)が定式化した概念。ポストモダン文化様式（パスティーシュ、断片化、表面性）を経済的下部構造としての後期資本主義（多国籍資本主義）の文化的表現として位置付けた、マルクス主義的ポストモダン批判の頂点。",
    background="エルネスト・マンデル『後期資本主義論』(1972)とフランクフルト学派文化産業批判のジェイムソン的総合。",
    development="現代のグローバリゼーション批判文学、新自由主義批判文学（ベン・ラーナー、ラケル・カスク、サリー・ルーニー）の理論的基盤となる。",
    historical_context="冷戦末期から90年代グローバリゼーション初期のマルクス主義文化理論の頂点的総合。",
    primary_source_url=WIKI_EN+"Postmodernism,_or,_the_Cultural_Logic_of_Late_Capitalism",
    primary_source_type="Wikipedia: Jameson 'Postmodernism' (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ジェイムソン",
         "description":"ジェイムソン哲学・文化理論とポストモダン文学批評の理論的共有。"}])

add(**C, name_ja="マクヘイル「ポストモダニスト・フィクション」",
    name_en="McHale 'postmodernist fiction'",
    name_original="postmodernist fiction (McHale)",
    period_key="ポストモダン期",
    definition="ブライアン・マクヘイル『ポストモダニスト・フィクション』(1987)が定式化した、モダニズム小説の認識論的支配（epistemological dominant）からポストモダン小説の存在論的支配（ontological dominant）への転換論。誰が知るかの問いから、何が存在するかの問いへの文学的重心移動を理論化した。",
    background="ロマーン・ヤコブソンの「支配項」概念と、ポストモダン小説の世界生成的特徴（多世界、虚構世界の重ね合わせ）の理論的総合。",
    development="ポストモダン小説論の標準理論として現代の小説論・SF論の基礎となり、マクヘイルは続編『Constructing Postmodernism』(1992)等で発展させた。",
    historical_context="80年代後半のポストモダン理論的成熟期。",
    primary_source_url=WIKI_EN+"Brian_McHale",
    primary_source_type="Wikipedia: Brian McHale (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ポストモダン的アイロニー",
    name_en="postmodern irony",
    name_original="postmodern irony", period_key="ポストモダン期",
    definition="伝統的アイロニー（言われたことと意図されたことの距離）を、二重・多重・自己解体的にまで複雑化したポストモダン特有のアイロニー形式。誠実さも皮肉も同時に保留する遊戯的態度として、ナボコフ、デヴィッド・フォスター・ウォレス、デヴィッド・リンチ作品に体現される。",
    background="ロマン派的アイロニー（フリードリヒ・シュレーゲル）の極限化と、ポストモダン真理懐疑論の合流。",
    development="ウォレス『これは水だ』スピーチ等が「新誠実派」(New Sincerity)として超克を試み、現代の文学的・文化的アイロニー論を更新中。",
    historical_context="80-90年代の真理懐疑的文化と21世紀の誠実さ回帰の交差。",
    primary_source_url=WIKI_EN+"Postmodernism",
    primary_source_type="Wikipedia: Postmodernism (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ジェンクス「二重コーディング」",
    name_en="Jencks 'double coding'",
    name_original="double coding", period_key="ポストモダン期",
    definition="チャールズ・ジェンクス『ポストモダン建築の言語』(1977)が建築理論として定式化し、後に文学に拡張された概念。専門的（モダニズム的）読者と大衆的読者の双方に同時にアピールする様式の二重性。エーコ『薔薇の名前』、ナボコフ作品、現代世界文学の中核戦略となった。",
    background="モダニズムのエリート主義への反動と、大衆文化と高度芸術の融合への80年代的志向。",
    development="ポストモダン建築・文学・映画の標準戦略となり、現代のメインストリーム文学（ハルキ・ムラカミ、エルナン・カイル）の方法論的基盤となる。",
    historical_context="モダニズム高低弁別の脱構築期。",
    primary_source_url=WIKI_EN+"Double_coding",
    primary_source_type="Wikipedia: Double coding (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="「小説の終焉」論争",
    name_en="'end of the novel' debate",
    name_original="end of the novel debate", period_key="ポストモダン期",
    definition="ジョン・バース「枯渇の文学」(1967)、ロブ=グリエの反小説論、トム・ウルフ「我らが豊穣の物語の流れ」(1989)等を契機とする、近代小説形式の歴史的限界と継続可能性をめぐる戦後文学批評の長期論争。文学的様式の死と再生をめぐる中心議題。",
    background="モダニズム極限後の小説形式の方向性をめぐる戦後文学的自己反省。",
    development="バース自身の続論「補充の文学」(1980)による反論、現代の小説論争（ラビ・スリ等のリアリズム回帰論）まで継承される。",
    historical_context="戦後文学の方法論的成熟期の自己診断的論争。",
    primary_source_url=WIKI_EN+"The_Literature_of_Exhaustion",
    primary_source_type="Wikipedia: The Literature of Exhaustion (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"近代小説形式の歴史的限界をめぐる論争は、AI生成小説の登場によって新たな段階に入る。「人間が書く小説」の地位そのものが正典的に問われる。",
         "related_ai_phenomenon":"AI生成小説と人間小説の正典的関係"}])

add(**C, name_ja="ポストモダン的崇高", name_en="postmodern sublime",
    name_original="postmodern sublime", period_key="ポストモダン期",
    definition="リオタール『非人間的なもの』(1988)の崇高論、フレドリック・ジェイムソンの「ヒステリカル崇高」、ポール・クロウザーの理論等で展開された、伝統的崇高（カント・バーク）のポストモダン的変容。提示不可能なものの提示の遊戯、テクノロジー的崇高、超巨大資本主義の崇高として理論化された。",
    background="リオタールのカント美学読解と、20世紀後半の技術・情報・経済の超人間的規模への文学的・哲学的応答。",
    development="現代の生態学的崇高論、AI崇高論まで延長される、21世紀の中核美学概念。",
    historical_context="冷戦末期の超技術社会の美学的診断。",
    primary_source_url=SEP+"sublime/",
    primary_source_type="Stanford Encyclopedia: Sublime",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"AI生成の規模・速度・超人間性は、ポストモダン崇高概念の極限的実装として位置付けられる。生成AIによる「無限のテクスト」は計算的崇高の現代形である。",
         "related_ai_phenomenon":"AI生成と計算的崇高"}])

# ============================================================
# E: 自伝・現代（8件）
# ============================================================
add(**C, name_ja="オートフィクション", name_en="autofiction",
    name_original="autofiction", period_key="自伝的現代期",
    definition="セルジュ・ドゥブロフスキーが自著『Fils』(1977)の宣伝のため考案した造語で、自伝的事実を小説の枠組みで提示する文学形式。フィリップ・ロス、アニー・エルノー、エマニュエル・カレール、Knausgård、レイチェル・カスク、ベン・ラーナーが世界的展開を担い、現代文学の支配的様式の一つとなった。",
    background="フィリップ・ルジューヌ『自伝の規約』(1975)の自伝論争への文学的応答と、ポストモダン真正性遊戯の合流。",
    development="2010年代以降のグローバル文学の支配的様式となり、Knausgård『My Struggle』全6巻が国際的成功を収めた。アニー・エルノー2022年ノーベル文学賞受賞。",
    historical_context="ポストモダン後期から現代にかけての真正性・記憶・主体性の再定義期。",
    primary_source_url=WIKI_EN+"Autofiction",
    primary_source_type="Wikipedia: Autofiction (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"オートフィクションは「私」を小説的に再構築する実践であり、AI生成テクストにおける「私」の位置付けと正面から対立する。人間的体験の真正性を最大化する形式が、AI時代に強い対抗的価値を持つ。",
         "related_ai_phenomenon":"AI時代における真正な「私」の文学的再主張"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"オートフィクションが模索する「真の自己」と「虚構的自己」の弁別不能性が、AI生成「自己」の登場によって新たな段階に入る。",
         "related_ai_phenomenon":"AI生成自己とオートフィクション的自己の対立"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"自伝の規約",
         "description":"ルジューヌ自伝論とオートフィクション理論の理論的接続。"}])

add(**C, name_ja="ゼーバルト「アウステルリッツ」",
    name_en="W.G. Sebald 'Austerlitz'",
    name_original="Austerlitz", period_key="自伝的現代期",
    definition="W.G.ゼーバルトが2001年に発表した、ホロコースト記憶を主題とする小説。写真の挿入、長文の蛇行的散文、フィクションと歴史的事実の境界融解により、戦後ヨーロッパのトラウマ記憶の文学的形象化を実現した、21世紀文学の代表作。",
    background="ホロコースト第二・第三世代の記憶文学と、ベンヤミン的歴史哲学・破壊の天使概念の文学的継承。",
    development="ゼーバルト2001年事故死後、現代世界文学の中核的範型として、テジュ・コール『オープン・シティ』、テイヤノ・テイラ等に直接的影響を与えた。",
    historical_context="冷戦後ヨーロッパのホロコースト記憶の文学的処理期。",
    primary_source_url=WIKI_EN+"Austerlitz_(novel)",
    primary_source_type="Wikipedia: Austerlitz (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="自伝の規約の破裂",
    name_en="autobiographical pact ruptured",
    name_original="pacte autobiographique rompu",
    period_key="自伝的現代期",
    definition="フィリップ・ルジューヌ『自伝の規約』(1975)が定式化した、作者・語り手・主人公の三者同一性を約束する自伝の規約が、オートフィクション以降意図的に破裂・混濁・遊戯化された事態。現代文学における真正性概念の根本的再定義の中核論点。",
    background="ルジューヌ理論への小説家側からの応答（ドゥブロフスキー、エルノー）。",
    development="ルジューヌ自身の理論修正『自伝の規約二』(2005)を経て、現代文学批評の基本概念として整理された。",
    historical_context="ポストモダン後期の真正性概念の文学的再定義。",
    primary_source_url=WIKI_EN+"Autobiography",
    primary_source_type="Wikipedia: Autobiography (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="クナウスゴール「我が闘争」",
    name_en="Knausgård 'My Struggle'",
    name_original="Min kamp", period_key="自伝的現代期",
    definition="カール・オーヴェ・クナウスゴールが2009-2011年に発表した全6巻3,500ページの自伝小説。日常の微細な記憶を極限的詳細さで言語化し、ヒトラー『我が闘争』と同名のタイトルで物議を醸しながら、世界文学的成功を収めた現代オートフィクションの頂点。",
    background="プルースト『失われた時を求めて』の現代北欧的継承と、北欧文学の自伝的伝統の総合。",
    development="2010年代の世界的読書現象となり、デヴィッド・シールズ『リアリティ・ハンガー』理論等を文学的に裏付ける現象として注目された。",
    historical_context="2010年代のグローバル化・SNS化期における真正性回帰文学の頂点。",
    primary_source_url=WIKI_EN+"My_Struggle_(Knausg%C3%A5rd_novels)",
    primary_source_type="Wikipedia: My Struggle (Knausgård) (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="クナウスゴール的自伝性",
    name_en="Karl Ove autobiographical mode",
    name_original="Karl Ove autobiographical mode",
    period_key="自伝的現代期",
    definition="クナウスゴールが確立した、日常の徹底的微細描写、家族・友人の実名使用、内面の遠慮なき開示、長文蛇行的散文を特徴とする独自の自伝的文体。アニー・エルノー、レイチェル・カスク、シーラ・ヘティらと並び、2010年代の世界的「自伝文学ルネサンス」の方法論的核となった。",
    background="北欧プロテスタント的告白文化と、SNS時代の自己開示文化の文学的合流。",
    development="現代の世界自伝文学（オーシア・モリス、オチャ・カイア・キーラン等）の方法論的基盤となる。",
    historical_context="2010年代のグローバル自伝文学運動。",
    primary_source_url=WIKI_EN+"Karl_Ove_Knausg%C3%A5rd",
    primary_source_type="Wikipedia: Karl Ove Knausgård (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ベン・ラーナー", name_en="Ben Lerner",
    name_original="Ben Lerner", period_key="自伝的現代期",
    definition="米国の詩人・小説家（1979生）。『アトーチャ駅出発』(2011)『10:04』(2014)『The Topeka School』(2019)で、詩人・小説家としての自伝的経験をフィクション化する独特のメタ自伝小説を確立。21世紀英語圏オートフィクションの代表的作家。",
    background="メリーランド大学MFAでの詩学教育と、デビッド・フォスター・ウォレス以降の米国メタフィクション系譜の継承。",
    development="MacArthur Fellow受賞(2015)を経て、現代米国文学の中心作家の一人として活動。詩集『The Lichtenberg Figures』『Mean Free Path』等も評価される。",
    historical_context="2010年代米国オートフィクション文学の興隆。",
    primary_source_url=WIKI_EN+"Ben_Lerner",
    primary_source_type="Wikipedia: Ben Lerner (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シーラ・ヘティ", name_en="Sheila Heti",
    name_original="Sheila Heti", period_key="自伝的現代期",
    definition="カナダの小説家（1976生）。『How Should a Person Be?』(2010)、『Motherhood』(2018)、『Pure Colour』(2022)で、自伝的経験と哲学的・倫理的問いを融合した独特のオートフィクションを展開。2010年代以降の世界的オートフィクションの代表的女性作家。",
    background="トロント大学哲学・芸術史教育と、フェミニズム・自伝文学伝統の現代的継承。",
    development="クナウスゴール、ラーナー、レイチェル・カスクと並ぶ現代オートフィクションの中核作家として国際的評価を確立。AI生成テクストとの実験（『Alphabetical Diaries』2024）も発表。",
    historical_context="2010年代北米オートフィクションの興隆期。",
    primary_source_url=WIKI_EN+"Sheila_Heti",
    primary_source_type="Wikipedia: Sheila Heti (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"partial",
         "rationale":"ヘティ『Alphabetical Diaries』(2024)等のAIとの共作実験は、AI時代の作者性概念の文学的探究の最前線。",
         "related_ai_phenomenon":"AI共作と作者性概念の文学的探究"}])

add(**C, name_ja="レイチェル・カスク", name_en="Rachel Cusk",
    name_original="Rachel Cusk", period_key="自伝的現代期",
    definition="英国の小説家（1967生、カナダ生まれ）。『アウトライン』三部作（2014-2018）で、語り手の自己を消去し他者の語りを記録する独特のオートフィクションを確立。21世紀のフェミニスト・オートフィクションの方法論的革新者として、世界的評価を得る。",
    background="オックスフォード大学英文学教育と、フェミニスト自伝文学伝統の現代的継承、ハイデガー的「対話」概念の文学的応用。",
    development="『アウトライン』『中間』『敬愛』三部作の世界的成功後、『Second Place』(2021)『パラデア』(2024)等で形式的実験を継続中。",
    historical_context="2010年代のフェミニスト自伝文学の興隆期。",
    primary_source_url=WIKI_EN+"Rachel_Cusk",
    primary_source_type="Wikipedia: Rachel Cusk (academic)",
    importance_score=4, source_tier="primary", canonical_in_region="core")


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
        print(f"[c11] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c11] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
