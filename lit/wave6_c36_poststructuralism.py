"""LIT-DB Phase 2 Wave 6 — C36: Structuralism & Poststructuralism (40 concepts).

Subfield: lit_theory (id=22), region='理論'.

40 concepts across 5 categories of 8 each:
  A. 構造主義 (Structuralism)
  B. ポスト構造主義主要概念 (Post-structuralism core)
  C. ナラトロジー (Narratology)
  D. 受容理論・解釈学 (Reception theory & Hermeneutics)
  E. 関連批評概念 (Related critical concepts)

Sources: Stanford Encyclopedia of Philosophy (SEP), JSTOR, Project MUSE,
Critical Inquiry, Cambridge/Oxford university presses, and academic-grade
encyclopedic entries. Primary text URLs are used where the original essay
or canonical translation is openly accessible (Internet Archive, JSTOR open).
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# ------------------------------------------------------------
# Period (theoretical timeframe). The "理論" region has no period yet,
# so we create one umbrella period covering structuralism through
# post-structuralism (1916 Saussure Cours -> ~2000 mature reception).
# ------------------------------------------------------------
PERIODS = [
    ("構造主義・ポスト構造主義期", "Structuralist & Post-Structuralist Era",
     1916, 2000,
     "ソシュール『一般言語学講義』刊行(1916)を起点とし、レヴィ=ストロース、バルト、フーコー、デリダ、ラカン、クリステヴァ、ジュネットらによる記号論・脱構築・ナラトロジー・受容美学が展開された20世紀理論期。"),
]

# Canonical reference URLs (real, verifiable open-access sources)
SEP = "https://plato.stanford.edu/entries/"
JSTOR = "https://www.jstor.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
ARCHIVE = "https://archive.org/"
MUSE = "https://muse.jhu.edu/"
CI = "https://www.journals.uchicago.edu/journals/ci"  # Critical Inquiry
IEP = "https://iep.utm.edu/"  # Internet Encyclopedia of Philosophy
GUTEN = "https://www.gutenberg.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_theory", region="理論", original_script="roman")

# ============================================================
# A. 構造主義 (8件)
# ============================================================

add(**C, name_ja="ラング／パロール（ソシュール）",
    name_en="langue / parole (Saussure)",
    name_original="langue / parole",
    period_key="構造主義・ポスト構造主義期",
    definition="フェルディナン・ド・ソシュールが『一般言語学講義』(1916)で導入した、言語体系（ラング）と個別発話行為（パロール）を区別する根本的二項対立。ラングは社会的・体系的・共時的な記号体系を、パロールは個人的・偶発的な言語使用を指す。20世紀構造主義の言語学的基盤を成し、文化・神話・物語の構造分析に拡張された。",
    background="19世紀比較言語学の歴史主義的・通時的研究方法への反動として、共時的体系性を新たな研究対象として確立する必要があった。",
    development="レヴィ=ストロースの神話分析、バルトの記号論、ヤーコブソンの音韻論等、構造主義の方法論的基盤として全領域に拡散した。",
    historical_context="20世紀初頭の人文科学における言語論的転回の出発点。",
    primary_source_url=ARCHIVE+"details/courseingenerall00saus",
    primary_source_type="Internet Archive: Course in General Linguistics 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ラング／パロール区分は人間共同体の社会的言語体系を前提とするが、LLMが大規模言語モデルとして人間共同体外で「ラング」を再構成する可能性は、この区分自体の歴史的根拠を問い直す。",
         "related_ai_phenomenon":"LLMによる統計的言語体系の再構成"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ソシュール記号論",
         "description":"言語哲学・分析哲学の出発点としてSaussure記号論はPHIL-DBにも収録される横断概念。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"記号論的詩学",
         "description":"詩学の構造主義的方法論はPT-DBの中核概念群と直接接続する。"}])

add(**C, name_ja="レヴィ=ストロース神話の構造分析",
    name_en="Lévi-Strauss myth structures",
    name_original="structure du mythe / structural analysis of myth",
    period_key="構造主義・ポスト構造主義期",
    definition="クロード・レヴィ=ストロースが「神話の構造的研究」(1955)等で展開した、神話を音素類比的な「神話素（mythème）」の組み合わせとして分析する方法。神話は二項対立の解決を試みる思考装置とされ、『神話論理』四部作(1964-71)で世界規模の比較分析が試みられた。",
    background="ソシュール言語学・ヤーコブソン音韻論・トルベツコイの構造論を文化人類学に応用する試み。",
    development="バルト『神話作用』、グレマス記号論的物語論、トドロフ物語論への直接的影響。後にデリダ・リクールから内在批判を受ける。",
    historical_context="戦後フランス構造主義の中心人物による人文諸学の方法論的統合。",
    primary_source_url=JSTOR+"stable/536768",
    primary_source_type="JSTOR: 'The Structural Study of Myth' (1955)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"神話を二項対立の解決装置とする普遍的構造主義は、LLMが多文化神話を統計的に学習・生成する時代において、人類普遍構造の経験的根拠を再考する必要がある。",
         "related_ai_phenomenon":"LLMによる神話・物語の統計的生成"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"レヴィ=ストロース構造人類学",
         "description":"構造人類学の中核としてAN-DBにも収録される横断概念。"},
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"神話の構造分析",
         "description":"神話研究DBの理論的基盤。"}])

add(**C, name_ja="バルト『神話作用』",
    name_en="Barthes 'Mythologies'",
    name_original="Mythologies",
    period_key="構造主義・ポスト構造主義期",
    definition="ロラン・バルト『神話作用』(1957)が展開した、現代社会の日常的事象（プロレス・ストリップ・洗剤広告等）を「現代神話」として記号論的に分析する批評実践。第二記号系（connotation）の概念で、ブルジョワ的イデオロギーが「自然」として中立化される機構を暴く。",
    background="サルトル実存主義の批評を脱イデオロギー的・記号論的に置換する試み。",
    development="バルト後期『S/Z』『恋愛のディスクール・断章』へと展開し、ボードリヤール『物の体系』、カルチュラル・スタディーズの方法論的源流となる。",
    historical_context="戦後フランス批評の構造主義的転換期。",
    primary_source_url=ARCHIVE+"details/mythologies0000bart",
    primary_source_type="Internet Archive: Mythologies 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"バルトが暴いた「自然化されたイデオロギーとしての神話」の機構は、AI生成コンテンツが「中立的情報」として流通する時代の批評的読解にとって基盤的方法論である。",
         "related_ai_phenomenon":"AI生成テクストのイデオロギー的中立化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"記号論的文化分析",
         "description":"文化人類学の記号論的展開と接続。"},
        {"target_db":"Cultural-Intelligence","link_type":"parallel",
         "target_entity_name":"現代神話の批判的読解",
         "description":"日常文化の批評的解読の方法論的祖型。"}])

add(**C, name_ja="グレマス記号論的方陣",
    name_en="Greimas semiotic square",
    name_original="carré sémiotique",
    period_key="構造主義・ポスト構造主義期",
    definition="アルジルダス・J・グレマスが『構造意味論』(1966)以降展開した、二項対立を四項関係（A／非A／B／非B）に拡張する意味分析の図式。物語の深層構造（actantial model）と意味生成の論理的・記号論的基盤を提供する。",
    background="ヤーコブソンの対立論理とロジック方陣（square of opposition）を意味論に応用する試み。",
    development="ナラトロジー（特にプロップ機能論との統合）、トドロフ・ブレモン物語論、文化記号論（ロトマン）、現代の批評記号論まで継承。",
    historical_context="パリ記号論学派の理論的中核期。",
    primary_source_url=SEP+"semiotics/",
    primary_source_type="SEP: Semiotics",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"記号論的詩学・物語論",
         "description":"PT-DBの記号論的詩学に直結。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"記号論",
         "description":"哲学的記号論の文学的応用。"}])

add(**C, name_ja="ジュネット・ナラトロジー",
    name_en="Genette narratology",
    name_original="narratologie (Genette)",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラール・ジュネットが『物語のディスクール』(1972)で体系化した、物語を「物語内容(histoire)／物語言説(récit)／語り(narration)」の三層に分け、時間・叙法・態の各カテゴリで分析する方法論。20世紀後半物語論の標準装置となった。",
    background="トドロフ・ブレモン・グレマスらフランス構造主義物語論の総合化と、プルースト『失われた時を求めて』を範型素材とする実例分析。",
    development="プリンス、バル、リモン=ケナンらにより英語圏に拡散し、認知ナラトロジー・ポストクラシカル・ナラトロジー（フルダニク等）へと発展継承される。",
    historical_context="構造主義の最も精密な物語分析装置の確立期。",
    primary_source_url=ARCHIVE+"details/narrativediscour0000gene",
    primary_source_type="Internet Archive: Narrative Discourse 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"ジュネットの三層構造は人間語り手と人間読者を前提とするが、LLMがこれら三層を区別なく生成する時代に、語り手概念の人間中心性が再考対象となる。",
         "related_ai_phenomenon":"LLM生成物語における語り手概念の希薄化"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語論",
         "description":"PT-DBの中核領域。"}])

add(**C, name_ja="トドロフ幻想論・物語論",
    name_en="Tzvetan Todorov narrative theory",
    name_original="Tzvetan Todorov",
    period_key="構造主義・ポスト構造主義期",
    definition="ツヴェタン・トドロフが『散文の詩学』(1971)・『幻想文学序説』(1970)で展開した、構造主義的物語論とジャンル理論。幻想文学を「ためらい(hésitation)」の体験として定義し、物語を変形（transformation）の体系として分析した。",
    background="ロシア・フォルマリズム翻訳紹介者としての出自と、フランス構造主義への参加。",
    development="ジャンル理論への影響大。後年は人文主義・倫理批評へ転換し、構造主義から離脱した。",
    historical_context="ブルガリア出自の構造主義者によるフランス批評への東欧理論輸入期。",
    primary_source_url=ARCHIVE+"details/fantasticstructu00todo",
    primary_source_type="Internet Archive: The Fantastic 英訳版",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="プロップ昔話形態学",
    name_en="Propp's morphology of folktale",
    name_original="Морфология сказки",
    period_key="構造主義・ポスト構造主義期",
    definition="ウラジーミル・プロップが『昔話の形態学』(1928)で示した、ロシア魔法昔話100話を分析し31の機能（function）と7つの行為者圏（dramatis personae）から成る不変構造を抽出する方法。1958年英訳によって西側に発見され、構造主義物語論の出発点となった。",
    background="ロシア・フォルマリズムとサンクトペテルブルク民俗学派の交点で誕生した先駆的構造分析。",
    development="レヴィ=ストロースが批判的に継承（構造論的批判、1960）し、グレマス・ブレモン物語論の出発点に。後にキャンベル『千の顔を持つ英雄』英雄旅程論にも影響。",
    historical_context="戦間期ソビエト民俗学から戦後西側構造主義への継承。",
    primary_source_url=ARCHIVE+"details/morphologyoffolk0000prop",
    primary_source_type="Internet Archive: Morphology of the Folktale 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"プロップ機能分析",
         "description":"神話・民話DBの基本フレームワーク。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語形態論",
         "description":"PT-DBの構造主義詩学の起点。"}])

add(**C, name_ja="ヤーコブソン言語の機能",
    name_en="Roman Jakobson functions of language",
    name_original="six functions of language (Jakobson)",
    period_key="構造主義・ポスト構造主義期",
    definition="ロマン・ヤーコブソンが「言語学と詩学」(1960)で示した、コミュニケーションの六要素（送り手・受け手・コンテクスト・メッセージ・接触・コード）に対応する六機能（情動的・働きかけ的・指示的・詩的・交話的・メタ言語的）の図式。詩的機能をメッセージ自体への焦点化と定義した。",
    background="プラハ言語学派の機能主義とロシア・フォルマリズム詩学を統合する戦後アメリカでの集大成。",
    development="文体論・詩学・記号論・コミュニケーション論の標準モデルとして全領域に拡散。バルト・ジュネット・カラーらの理論に必修概念として組み込まれた。",
    historical_context="戦後アメリカに移住した東欧理論家による構造主義詩学の英語圏定着期。",
    primary_source_url=WIKI_EN+"Jakobson%27s_functions_of_language",
    primary_source_type="Wikipedia: Jakobson's functions of language (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"言語の六機能図式は人間コミュニケーションを前提とするが、AI送り手・AI受け手の介在によりコンテクスト・接触・コードの各要素が再定義される。",
         "related_ai_phenomenon":"AI介在型コミュニケーション"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"詩的機能",
         "description":"詩学の核心概念としてPT-DBに収録。"}])

# ============================================================
# B. ポスト構造主義主要概念 (8件)
# ============================================================

add(**C, name_ja="デリダ「差延」",
    name_en="Derrida différance",
    name_original="différance",
    period_key="構造主義・ポスト構造主義期",
    definition="ジャック・デリダが講演「差延」(1968)・『散種』(1972)等で展開した、差異(différence)と遅延(différer)を綴り字「a」の差し換えで結合した造語。意味は他の記号との差異の戯れによって絶えず先送り（遅延）されるとし、現前の形而上学を解体する脱構築の中核概念。",
    background="ソシュールの差異の体系（記号は他の記号との差異からのみ意味を得る）論を、ハイデガー存在論的差異と接続する形で過激化。",
    development="脱構築批評（ヒリス・ミラー、ポール・ド・マン、ジェフリー・ハートマン等イェール学派）、フェミニズム批評、ポストコロニアル批評の理論的基盤となる。",
    historical_context="1968年五月革命前後のフランス哲学の構造主義超克期。",
    primary_source_url=SEP+"derrida/",
    primary_source_type="SEP: Jacques Derrida",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"記号の意味が他の記号との差異の戯れに依存するという差延の論理は、LLMの埋め込み空間における意味のベクトル的差異構造と直接的な構造的類比を示す。",
         "related_ai_phenomenon":"LLM埋め込み空間における意味の差異的構造"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"現前の形而上学批判は、AI生成テクストにおける「真正なオリジナル」概念の解体と直接的に共鳴する。",
         "related_ai_phenomenon":"AI生成における真正性概念の解体"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"差延・脱構築",
         "description":"哲学DBの中核概念として共有。"}])

add(**C, name_ja="デリダ脱構築",
    name_en="Derrida deconstruction",
    name_original="déconstruction",
    period_key="構造主義・ポスト構造主義期",
    definition="ジャック・デリダが『グラマトロジーについて』(1967)『エクリチュールと差異』(1967)『散種』(1972)で確立した、テクストの内的二項対立（音声／文字、男／女、自然／文化等）を脱中心化し、その階層性を解体する読みの実践。批評の方法ではなく「テクストに既に起こっていること」とされる。",
    background="ハイデガー『存在と時間』のDestruktion概念と、ソシュール記号論内在批判の総合。",
    development="米英文学批評（イェール学派）、フェミニズム（クリステヴァ、エレーヌ・シクスー）、ポストコロニアリズム（ガヤトリ・スピヴァク翻訳経由）に多大な影響。",
    historical_context="1968年前後フランス哲学のポスト構造主義的転回期。",
    primary_source_url=SEP+"derrida/",
    primary_source_type="SEP: Jacques Derrida",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者の意図を超えてテクストが自己解体する脱構築の論理は、AIが生成するテクストにおける作者意図不在の状況を読み解く批評資源となる。",
         "related_ai_phenomenon":"AI生成テクストの作者意図不在"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"脱構築",
         "description":"哲学DBの主要概念として横断。"}])

add(**C, name_ja="フーコー「エピステーメー」",
    name_en="Foucault episteme",
    name_original="épistémè",
    period_key="構造主義・ポスト構造主義期",
    definition="ミシェル・フーコーが『言葉と物』(1966)で展開した、各時代に固有の知の根本的配置・条件を指す概念。ルネサンス（類似）／古典主義（表象）／近代（人間）という三エピステーメー区分を提示し、知の歴史を断絶的に把握する考古学的方法論を構築した。",
    background="バシュラール認識論的切断、カンギレム科学史の方法論をニーチェ系譜学と統合する試み。",
    development="後期フーコーが「権力／知」「ディスポジティフ」概念に接続し、ポストコロニアリズム（サイード『オリエンタリズム』）、フェミニズム、新歴史主義の理論的基盤となる。",
    historical_context="フランス60年代ポスト構造主義の知の歴史化期。",
    primary_source_url=SEP+"foucault/",
    primary_source_type="SEP: Michel Foucault",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"知の根本配置が時代ごとに断絶するというエピステーメー論は、AI時代という新エピステーメーへの移行を考えるための批評資源である。",
         "related_ai_phenomenon":"AI時代の新エピステーメー成立"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"エピステーメー",
         "description":"哲学・知識史の中核概念として共有。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"知の人類学",
         "description":"知の歴史性をめぐる人類学的考察と接続。"}])

add(**C, name_ja="フーコー「作者機能」",
    name_en="Foucault author function",
    name_original="fonction-auteur",
    period_key="構造主義・ポスト構造主義期",
    definition="ミシェル・フーコーが講演「作者とは何か」(1969)で示した、作者は実体的個人ではなく特定のディスクールの所有・分類・解釈を統御する機能だという概念。書物の流通・所有・権威付与の社会的機構として作者を再定義した。",
    background="バルト「作者の死」(1968)に応答する形で、作者問題をディスクール分析の文脈に置き直した。",
    development="ポスト構造主義批評・新歴史主義の作者観の基礎となり、知的所有権・著作者人格権論議にも波及。AI時代の生成テクストの作者問題で再注目される。",
    historical_context="1968年五月革命前後の主体批判運動の文学理論的展開。",
    primary_source_url=ARCHIVE+"details/whatisanauthor",
    primary_source_type="Internet Archive: 'What Is an Author?' 英訳",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者を実体ではなくディスクール統御機能とする視座は、AIが生成するテクストの作者問題を考える上で最も直接的な理論資源となる。",
         "related_ai_phenomenon":"AI生成テクストの作者機能再分配"},
        {"axis":"主体","status":"rethinking",
         "rationale":"作者主体の脱実体化は、AI生成における人間／非人間の主体性区分の流動化と直接対応する。",
         "related_ai_phenomenon":"AI生成における主体概念の脱実体化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"作者機能",
         "description":"哲学的主体論の中核概念として横断。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"AI生成テクストの作者性問題",
         "description":"フーコー作者機能論はAI著作権論争の理論的祖型。"}])

add(**C, name_ja="ラカン三界（象徴界・想像界・現実界）",
    name_en="Lacan symbolic / imaginary / real",
    name_original="le symbolique / l'imaginaire / le réel",
    period_key="構造主義・ポスト構造主義期",
    definition="ジャック・ラカンがセミネール（1953-80）で展開した、人間心的構造を三つの「位相（registres）」に分ける枠組み。象徴界は言語・法・他者の秩序、想像界は鏡像段階の自我形成領域、現実界は象徴化を逃れる残余として相互に絡み合う（ボロメオの結び目）。",
    background="フロイト精神分析をソシュール記号論・コジェーヴのヘーゲル講義の影響下で再読する試み。",
    development="ジジェク、ジョアン・コプチェク等の現代ラカン派批評、シネマ・スタディーズ、フェミニズム批評（ジュリエット・ミッチェル、ジェイクリン・ローズ）、文学批評全般に多大な影響。",
    historical_context="戦後フランス精神分析の構造主義的転換期。",
    primary_source_url=SEP+"lacan/",
    primary_source_type="SEP: Jacques Lacan",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"言語＝象徴界の中で構成される主体というラカン理論は、AI／LLMが象徴界の生成・媒介に介入する時代の主体性を考える理論資源である。",
         "related_ai_phenomenon":"AI介在による象徴界の再構成"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ラカン精神分析",
         "description":"哲学・精神分析の中核理論として共有。"}])

add(**C, name_ja="クリステヴァ「インターテクスチュアリテ」",
    name_en="Kristeva intertextuality",
    name_original="intertextualité",
    period_key="構造主義・ポスト構造主義期",
    definition="ジュリア・クリステヴァが論文「言葉、対話、小説」(1966)『セメイオチケ』(1969)で導入し、テル・ケル誌に紹介された概念。すべてのテクストは他のテクストの引用・吸収・変換のモザイクであり、自律した起源を持たないとする視座。バフチン対話主義のフランス受容を通じて生まれた。",
    background="バフチン『ドストエフスキイの詩学の諸問題』『フランソワ・ラブレーの作品と中世・ルネサンスの民衆文化』(クリステヴァが1960年代後半フランス紹介)の創造的読解。",
    development="ジュネット『パランプセスト』(1982)が「トランステクスチュアリテ」概念で精緻化。バルト『テクストの快楽』『S/Z』、リファテール詩学、現代カルチュラル・スタディーズの基本概念となる。",
    historical_context="テル・ケル運動とフランス批評理論のロシア・東欧受容期。",
    primary_source_url=ARCHIVE+"details/desireinlanguage0000kris",
    primary_source_type="Internet Archive: Desire in Language",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"すべてのテクストが先行テクストの引用・変換であるとするインターテクスチュアリテは、LLMが大量学習テクストの組み換えとして出力する時代の創造性概念に根本的視座を提供する。",
         "related_ai_phenomenon":"LLMによる学習テクストの組み換え生成"},
        {"axis":"言語","status":"rethinking",
         "rationale":"テクストの自律的起源を否定する視座は、AI生成テクストの「起源」概念を再考する基盤となる。",
         "related_ai_phenomenon":"AI生成テクストの起源不在"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"インターテクスチュアリテ",
         "description":"哲学的言語論の中核概念。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"対話主義詩学",
         "description":"バフチン詩学経由でPT-DBに接続。"}])

add(**C, name_ja="バルト「作者の死」",
    name_en="Barthes 'The Death of the Author'",
    name_original="La mort de l'auteur",
    period_key="構造主義・ポスト構造主義期",
    definition="ロラン・バルトが英語雑誌Aspen 5+6(1967)で初出、仏Manteia誌(1968)で再録した短いマニフェスト的論文。テクストの意味は作者の意図ではなく読者の側で誕生するとし、「作者の死」と「読者の誕生」を宣言した。20世紀後半の読者中心主義批評の象徴的テクスト。",
    background="ニュー・クリティシズムの「意図主義の誤謬」批判（Wimsatt-Beardsley 1946）を構造主義的・ポスト構造主義的に過激化した形。",
    development="フーコー「作者とは何か」(1969)の応答を引き出し、受容理論・脱構築批評・読者反応批評・ポストモダニズム文学理論の象徴的根拠となる。",
    historical_context="1968年前後の主体批判運動の文学理論版。",
    primary_source_url=ARCHIVE+"details/imagemusictext0000bart",
    primary_source_type="Internet Archive: Image-Music-Text",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者の死テーゼは、AI生成テクストの作者問題における最重要先行理論である。生成AIにおいて作者は再び別の意味で「死ぬ」のか、あるいは「分散」するのか、AI時代の作者性概念再考の中心軸となる。",
         "related_ai_phenomenon":"AI生成における作者性の解体・分散"},
        {"axis":"主体","status":"rethinking",
         "rationale":"作者主体の死と読者主体の誕生という構図は、AI時代に作者主体・読者主体・AI主体の三項関係へと再編される。",
         "related_ai_phenomenon":"AI介在による主体三項関係化"},
        {"axis":"受容","status":"rethinking",
         "rationale":"受容の側で意味が誕生するという原理は、AI生成テクストの受容実践の理論的基盤を提供する。",
         "related_ai_phenomenon":"AI生成テクストの受容主体化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"主体の死",
         "description":"哲学的主体論の文学版。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"AI著作権・作者性論争",
         "description":"AI生成における作者性論争の理論的祖型。"}])

add(**C, name_ja="バルト『S/Z』",
    name_en="Barthes 'S/Z'",
    name_original="S/Z",
    period_key="構造主義・ポスト構造主義期",
    definition="ロラン・バルト『S/Z』(1970)が展開した、バルザック中編『サラジーヌ』を561の「読みの単位（lexies）」に分解し、五つのコード（解釈学・意味素・象徴・行為・文化）で精読する大規模批評実験。「読み込み可能なテクスト(lisible)／書き込み可能なテクスト(scriptible)」の区別を提示し、構造主義から「テクスト」概念への移行を画する作品。",
    background="バルト前期の構造主義的物語論（『物語の構造分析』1966）から、ポスト構造主義的「テクスト性」へと移行する転換点。",
    development="ジュネット『パランプセスト』、ジョナサン・カラー詩学、リファテール記号論詩学、後の電子文学のレクシア概念に直接影響。",
    historical_context="1970年代初頭テル・ケル誌周辺のテクスト理論隆盛期。",
    primary_source_url=ARCHIVE+"details/sz0000bart",
    primary_source_type="Internet Archive: S/Z 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"テクストを能動的に書き込み可能なものとする「scriptible」概念は、生成AIによる読者参加型テクストの先駆的理論。",
         "related_ai_phenomenon":"AI協働による書き込み可能テクスト"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"テクスト分析",
         "description":"PT-DBの基礎方法論。"}])

# ============================================================
# C. ナラトロジー (8件)
# ============================================================

add(**C, name_ja="ジュネット『物語のディスクール』",
    name_en="Genette 'Narrative Discourse'",
    name_original="Discours du récit",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラール・ジュネット『物語のディスクール』(1972、原題は『フィギュールIII』所収論文)が確立した、物語を時間（順序・継続・頻度）／叙法（距離・パースペクティヴ）／態（語りの時間・語りの水準・人称）の三大カテゴリで分析する体系。プルースト『失われた時を求めて』を範型素材とする。",
    background="ロシア・フォルマリズムのファーブラ／シュジェート区分とフランス構造主義物語論を、文献学的精密さで総合する試み。",
    development="プリンス、バル、リモン=ケナンらにより英語圏の標準ナラトロジー教科書概念体系として確立。後期『物語の言説 新論』(1983)で自己批判的に補充。",
    historical_context="フランス構造主義詩学の頂点期の代表作。",
    primary_source_url=ARCHIVE+"details/narrativediscour0000gene",
    primary_source_type="Internet Archive: Narrative Discourse 英訳版",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語論の体系化",
         "description":"PT-DB物語論の代表的体系。"}])

add(**C, name_ja="焦点化",
    name_en="focalization",
    name_original="focalisation",
    period_key="構造主義・ポスト構造主義期",
    definition="ジュネット『物語のディスクール』(1972)が「視点(point of view)」概念を精密化して導入した語り論的概念。「誰が見るか(qui voit)」と「誰が語るか(qui parle)」を区別し、内的焦点化（人物の意識からの世界把握）／外的焦点化（外面のみの観察）／非焦点化（全知）の三類型を提案した。",
    background="ジェイムズ・パーシー・ラボックの視点論（『小説の手法』1921）の構造主義的精密化。",
    development="ミーケ・バル『ナラトロジー』(1985)が焦点者(focalizer)概念で精緻化。認知ナラトロジー、ポストクラシカル・ナラトロジーの基礎概念。",
    historical_context="戦後フランス物語論の精密化期。",
    primary_source_url=ARCHIVE+"details/narrativediscour0000gene",
    primary_source_type="Internet Archive: Narrative Discourse 英訳版",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"視点論",
         "description":"PT-DB詩学の中核概念。"}])

add(**C, name_ja="自由間接話法理論",
    name_en="theory of free indirect discourse",
    name_original="style indirect libre / free indirect discourse",
    period_key="構造主義・ポスト構造主義期",
    definition="登場人物の声・思考と語り手の声を融合し、引用符や報告動詞の挿入なしに人物意識を地の文として提示する語り法の理論。バリー(Charles Bally, 1912)の独仏比較から始まり、バフチン「二重音声性」、コーン(Dorrit Cohn)『透明な精神』(1978)、フルダニク認知ナラトロジーまで継承される物語論の中心概念。",
    background="フローベール『ボヴァリー夫人』(1856)の文体的革新を出発点とする20世紀文体論・物語論の中心問題。",
    development="バフチン『小説の言葉』(1934-35執筆、1975刊)が「二重音声性」概念で哲学的に深化。コーンが「物語化された独白(narrated monologue)」と再命名し、英語圏で標準化。",
    historical_context="20世紀文体論・物語論を横断する古典的論題。",
    primary_source_url=ARCHIVE+"details/transparentminds00cohn",
    primary_source_type="Internet Archive: Transparent Minds (Cohn)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"二重音声性",
         "description":"バフチン詩学経由でPT-DBに接続。"}])

add(**C, name_ja="ミーケ・バル・ナラトロジー",
    name_en="Mieke Bal narratology",
    name_original="Narratologie (Bal)",
    period_key="構造主義・ポスト構造主義期",
    definition="ミーケ・バル『物語論』(1985英訳；蘭原書1980)が確立した、ジュネット体系を批判的に再構成する物語論。物語を「ファブラ／物語(story)／物語テクスト」の三層に再編し、焦点者(focalizer)概念で焦点化を行為主体的に精緻化した。学生向け体系的教科書として英米で標準化。",
    background="オランダの記号論・物語論の伝統と、英米フェミニズム批評の合流点。",
    development="ジェンダー論・視覚文化論・聖書物語論への応用。バル自身の『読みの主体』『書く女性』等で実践展開。",
    historical_context="1980年代英語圏ナラトロジーの教科書的体系化期。",
    primary_source_url=ARCHIVE+"details/narratologyintro0000balm",
    primary_source_type="Internet Archive: Narratology",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジェラルド・プリンス・ナラトロジー",
    name_en="Gerald Prince narratology",
    name_original="Gerald Prince",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラルド・プリンスが『物語論辞典』(1987)・『物語論』(1982)で展開した、英語圏ナラトロジー標準教科書群。「ナラティ(narratee)」（語り手に対する語られ手）概念の精緻化、ジュネット体系の英語圏定着、ナラティヴィティ(narrativity)概念の体系化が主要貢献。",
    background="フランス構造主義物語論の英語圏輸入と教科書化の試み。",
    development="認知ナラトロジー・ポストクラシカル・ナラトロジー（フルダニク、ジェイムズ・フィラン）の基礎を提供。",
    historical_context="英語圏物語論の体系化期。",
    primary_source_url=ARCHIVE+"details/dictionaryofnarra0000prin",
    primary_source_type="Internet Archive: Dictionary of Narratology",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ウェイン・ブース『小説の修辞学』",
    name_en="Wayne Booth 'Rhetoric of Fiction'",
    name_original="The Rhetoric of Fiction",
    period_key="構造主義・ポスト構造主義期",
    definition="ウェイン・ブース『小説の修辞学』(1961)が提示した、小説を作者と読者の修辞的コミュニケーションとして分析する英米物語論の古典。「内包作者(implied author)」「内包読者(implied reader)」「信頼できない語り手(unreliable narrator)」概念を確立した、ナラトロジー前史を画す決定的著作。",
    background="シカゴ学派ネオ・アリストテレス批評（R.S.クレイン、エルダー・オルソン）と、新批評の「客観的相関物」の限界を超克する試み。",
    development="フランス構造主義ナラトロジーと並行した英米物語論の古典として、内包作者・信頼できない語り手概念は現代まで継承される。",
    historical_context="米国ナラトロジー前史を画する1960年代初頭の修辞批評。",
    primary_source_url=ARCHIVE+"details/rhetoricoffictio00boot",
    primary_source_type="Internet Archive: The Rhetoric of Fiction",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"内包作者概念は、AI生成テクストの「テクストから推論される作者像」を考える上で直接的理論資源を提供する。",
         "related_ai_phenomenon":"AI生成テクストの内包作者性"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"内包作者・修辞批評",
         "description":"PT-DB詩学の中核概念。"}])

add(**C, name_ja="物語の水準（ディエゲーシス）",
    name_en="narrative levels (diegesis)",
    name_original="diégèse / narrative levels",
    period_key="構造主義・ポスト構造主義期",
    definition="ジュネット『物語のディスクール』(1972)が確立した、物語の入れ子構造を分析する概念体系。「外的物語(extradiégétique)／内的物語(intradiégétique)／メタ物語(métadiégétique)」の階層と、語り手と物語世界の関係（同一物語内/異物語内）を分析する。プラトン『国家』第三巻のディエゲーシス（語り）／ミメーシス（模倣）区分の継承的精緻化。",
    background="プラトン的詩学の根本区分のフランス構造主義的精緻化。",
    development="メタフィクション論、ミーケ・バル物語論、認知ナラトロジー、デジタル物語論まで継承される基本概念体系。",
    historical_context="20世紀物語論の根本枠組みの確立期。",
    primary_source_url=ARCHIVE+"details/narrativediscour0000gene",
    primary_source_type="Internet Archive: Narrative Discourse 英訳版",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"物語の水準",
         "description":"PT-DB物語論の基礎。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"プラトン詩学",
         "description":"プラトン『国家』詩学論との哲学的接続。"}])

add(**C, name_ja="内包作者／内包読者",
    name_en="implied author / implied reader",
    name_original="implied author / implied reader",
    period_key="構造主義・ポスト構造主義期",
    definition="ウェイン・ブース『小説の修辞学』(1961)が「内包作者」を、ヴォルフガング・イーザー『暗黙の読者』(1972)が「内包読者」を概念化した、テクストから推論される作者像・読者像。実在の作者・読者と区別される、テクスト内的構築物としての作者・読者。",
    background="米国シカゴ学派の修辞批評（ブース）と、ドイツ・コンスタンツ学派の受容美学（イーザー）の戦後並行発展。",
    development="ナラトロジーと受容美学の双方の中心概念として確立。AI時代の作者・読者問題で再注目される。",
    historical_context="米独の戦後文学理論を横断する基本概念。",
    primary_source_url=ARCHIVE+"details/impliedreaderpat0000iser",
    primary_source_type="Internet Archive: The Implied Reader (Iser)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"テクストから推論される作者像という内包作者概念は、AI生成テクストにおける作者性の在り方の理論資源として直接機能する。",
         "related_ai_phenomenon":"AI生成における内包作者性"},
        {"axis":"受容","status":"rethinking",
         "rationale":"テクストが想定する読者像という内包読者概念は、AI生成テクストの受容構造分析の基礎となる。",
         "related_ai_phenomenon":"AI生成テクストの内包読者構造"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"内包作者・内包読者",
         "description":"PT-DB詩学の中核概念。"}])

# ============================================================
# D. 受容理論・解釈学 (8件)
# ============================================================

add(**C, name_ja="ヤウス受容美学",
    name_en="Hans Robert Jauss reception aesthetics",
    name_original="Rezeptionsästhetik",
    period_key="構造主義・ポスト構造主義期",
    definition="ハンス・ロベルト・ヤウスがコンスタンツ大学就任講演「文学史への挑戦としての文学研究」(1967)で創始した受容美学。文学史を作品の生産と受容の歴史として書き直し、各時代の読者の「期待の地平」を再構成することを文学史の中心課題とした。",
    background="ガダマー解釈学（『真理と方法』1960）と、ヤーコブソン以来の構造主義詩学を統合する試み。",
    development="イーザーと並ぶコンスタンツ学派双璧として、戦後ドイツ文学理論の最大運動を成し、英米でも『受容の美学』『美的経験と文学的解釈学』が標準テクストとなる。",
    historical_context="戦後西ドイツ文学理論の中心運動。",
    primary_source_url=ARCHIVE+"details/towardanaestheti0000jaus",
    primary_source_type="Internet Archive: Toward an Aesthetic of Reception",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"読者の期待の地平を文学史の中心とする視座は、AI受容（AIによる読み・AIへの読まれ）が新たな受容主体として加わる時代の文学史を考える基盤となる。",
         "related_ai_phenomenon":"AI受容主体の登場"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"解釈学的美学",
         "description":"哲学的解釈学との接続。"}])

add(**C, name_ja="イーザー「内包読者」",
    name_en="Wolfgang Iser 'implied reader'",
    name_original="impliziter Leser",
    period_key="構造主義・ポスト構造主義期",
    definition="ヴォルフガング・イーザー『暗黙の読者』(1972)『行為としての読書』(1976)で展開した、テクストが構造的に読者の能動的補完を要求するという読書行為論。テクスト内の「空所(Leerstelle)」が読者の意味補完を引き出し、読みは作者と読者の動的相互作用となる。",
    background="フィンガレットン受容美学とロマン・インガルデン現象学的美学の総合化。",
    development="ヤウスと並ぶコンスタンツ学派双璧として確立し、英米読者反応批評（スタンリー・フィッシュ、ノーマン・ホランド）への影響大。",
    historical_context="戦後ドイツ受容美学の頂点期。",
    primary_source_url=ARCHIVE+"details/impliedreaderpat0000iser",
    primary_source_type="Internet Archive: The Implied Reader",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"読者の能動的補完を要求するテクスト観は、AIプロンプト＝AIによるテクスト補完という新たな読書行為形態の理論的祖型である。",
         "related_ai_phenomenon":"AIによるテクスト補完的読み"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"現象学的読書論",
         "description":"インガルデン経由でPHIL-DBと接続。"}])

add(**C, name_ja="フィッシュ「解釈共同体」",
    name_en="Stanley Fish 'interpretive communities'",
    name_original="interpretive communities",
    period_key="構造主義・ポスト構造主義期",
    definition="スタンリー・フィッシュ『このクラスにテクストはあるか』(1980)が提示した、テクストの意味は固有の特性ではなく、解釈共同体が共有する解釈戦略によって構築されるという主張。意味の客観性を否定し、解釈の社会的・制度的決定を強調する読者反応批評の極限形態。",
    background="ニュー・クリティシズムのテクスト客観性主義への反動と、エルンスト・カッシーラー象徴形式論の継承。",
    development="ジョナサン・カラー詩学、ピエール・ブルデュー文学社会学、フェミニズム・カルチュラル・スタディーズの読み実践理論として広範に影響。",
    historical_context="1980年代米国読者反応批評の極限的展開。",
    primary_source_url=ARCHIVE+"details/isthereatextint00fish",
    primary_source_type="Internet Archive: Is There a Text in This Class?",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"意味は解釈共同体に依存するというテーゼは、AI訓練データを共有する解釈共同体としてのAIモデルを位置づける新たな理論視座を提供する。",
         "related_ai_phenomenon":"AIモデルを解釈共同体として捉える視座"}])

add(**C, name_ja="ガダマー解釈学",
    name_en="Gadamer hermeneutics",
    name_original="philosophische Hermeneutik (Gadamer)",
    period_key="構造主義・ポスト構造主義期",
    definition="ハンス=ゲオルク・ガダマー『真理と方法』(1960)が確立した哲学的解釈学。「効果史的意識(wirkungsgeschichtliches Bewusstsein)」「地平の融合(Horizontverschmelzung)」「先入見(Vorurteil)の生産的役割」「解釈学的循環」等の概念で、理解を伝統との対話とする立場。",
    background="ハイデガー『存在と時間』の解釈学的存在論を、人文諸科学の方法論問題に応用する試み。",
    development="ヤウス・イーザーの受容美学、ポール・リクール解釈学、現代批評理論の哲学的基盤として広範に影響。",
    historical_context="戦後ドイツ哲学の解釈学的転回の頂点。",
    primary_source_url=SEP+"gadamer/",
    primary_source_type="SEP: Hans-Georg Gadamer",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"理解を伝統との対話とするガダマー解釈学は、AI（伝統の統計的集約）との対話としての読みという新形式を考える理論基盤となる。",
         "related_ai_phenomenon":"AI（伝統の集約体）との解釈学的対話"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"哲学的解釈学",
         "description":"哲学DBの中核領域。"}])

add(**C, name_ja="解釈学的循環",
    name_en="hermeneutic circle",
    name_original="hermeneutischer Zirkel",
    period_key="構造主義・ポスト構造主義期",
    definition="シュライアーマハー、ディルタイ、ハイデガー、ガダマーへと継承される解釈学の根本概念。部分の理解は全体の予備的理解を、全体の理解は部分の理解を相互前提する循環構造。理解は循環的に深化していく過程として把握される。",
    background="シュライアーマハー解釈学（19世紀初頭）から始まり、ハイデガー『存在と時間』(1927)で存在論化、ガダマー『真理と方法』(1960)で完成された理論。",
    development="解釈学・現象学のみならず、構造主義・ポスト構造主義・現代批評理論の根本問題として継承。",
    historical_context="近代解釈学の根本概念の構造主義時代における精緻化。",
    primary_source_url=SEP+"hermeneutics/",
    primary_source_type="SEP: Hermeneutics",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"解釈学的循環",
         "description":"哲学的解釈学の中核概念。"}])

add(**C, name_ja="期待の地平",
    name_en="horizon of expectations",
    name_original="Erwartungshorizont",
    period_key="構造主義・ポスト構造主義期",
    definition="ヤウス受容美学の中核概念。ある時代の読者がテクストに対して持つ、ジャンル・形式・主題・規範等についての先入観の総体。テクストはこの期待を充足するか「審美的距離(ästhetische Distanz)」をもって裏切るかによって評価される。文学史は期待の地平の歴史的変遷として書き直される。",
    background="ガダマー「地平」概念、マンハイム知識社会学、フッサール現象学的「地平」概念の総合化。",
    development="文学史記述の方法論として標準化し、ジャンル理論・読者反応批評・カルチュラル・スタディーズに継承。",
    historical_context="戦後ドイツ受容美学の中核概念。",
    primary_source_url=ARCHIVE+"details/towardanaestheti0000jaus",
    primary_source_type="Internet Archive: Toward an Aesthetic of Reception",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"地平の融合",
         "description":"ガダマー解釈学の中核概念と接続。"}])

add(**C, name_ja="読者反応批評",
    name_en="reader-response criticism",
    name_original="reader-response criticism",
    period_key="構造主義・ポスト構造主義期",
    definition="1970-80年代米国で展開した、テクストの意味を読者の側に置く批評運動の総称。スタンリー・フィッシュ「Affective Stylistics」(1970)、ノーマン・ホランド精神分析的読書論、ジョナサン・カラー、ジェイン・トムキンス編『読者反応批評』(1980)を主柱とする。",
    background="ニュー・クリティシズムの「テクスト自体」主義への反動と、ドイツ受容美学の英訳紹介。",
    development="フェミニズム読み、クィア・リーディング、ポストコロニアル読書論等の文化研究的読書実践の理論的基盤。",
    historical_context="米国1970-80年代批評理論百花繚乱期。",
    primary_source_url=ARCHIVE+"details/readerresponsec00toml",
    primary_source_type="Internet Archive: Reader-Response Criticism (Tompkins ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"読者の側に意味を置く運動全体は、AI受容主体の登場という新事態の理論資源として再活性化する。",
         "related_ai_phenomenon":"AI読者の登場と受容理論の拡張"}])

add(**C, name_ja="空所（Leerstelle）",
    name_en="blank / Leerstelle",
    name_original="Leerstelle",
    period_key="構造主義・ポスト構造主義期",
    definition="ヴォルフガング・イーザーが現象学的美学（ロマン・インガルデン「不確定箇所」）から発展させた中核概念。テクストが意図的に残す「空隙」が読者の能動的補完を引き出し、読みの動的構造を生み出す。テクストの「決定不能性」と読者の「具体化(Konkretisation)」の相互作用の場所。",
    background="インガルデン『文学作品の認識』(1968 独訳)の「不確定箇所(Unbestimmtheitsstelle)」概念のイーザーによる継承。",
    development="受容美学・読者反応批評の中心概念として標準化。デジタル・テクストの「ハイパーテクスト的空所」へと現代的展開。",
    historical_context="戦後ドイツ受容美学のコア概念。",
    primary_source_url=ARCHIVE+"details/actofreadingthe00iser",
    primary_source_type="Internet Archive: The Act of Reading",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"読者が能動的に補完する「空所」の論理は、AI／LLMがプロンプトの空所を補完する論理と直接対応する。",
         "related_ai_phenomenon":"LLMによるプロンプト空所の補完"}])

# ============================================================
# E. 関連批評概念 (8件)
# ============================================================

add(**C, name_ja="インターテクスチュアリテ（クリステヴァ・ジュネット）",
    name_en="intertextuality (Kristeva, Genette)",
    name_original="intertextualité",
    period_key="構造主義・ポスト構造主義期",
    definition="クリステヴァ(1966-69)が導入し、ジュネット『パランプセスト』(1982)が「トランステクスチュアリテ」概念で精緻化した、テクスト間の引用・吸収・変換関係の総体。ジュネットは引用・パロディ・パスティーシュ・パランプセスト等の具体的形式を区別する分類学を提示。",
    background="バフチン対話主義のクリステヴァによるフランス紹介と、ジュネットによる構造主義的形式分析の総合。",
    development="ポストモダン文学理論、ジョン・フィスケ、リンダ・ハッチオン『パロディの理論』、現代カルチュラル・スタディーズの基本概念。",
    historical_context="1960-80年代のフランス文学理論の中核概念。",
    primary_source_url=ARCHIVE+"details/palimpsestslit00gene",
    primary_source_type="Internet Archive: Palimpsests (Genette)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"テクスト間の引用・変換としての創造性概念は、LLMが学習データから組み換えとして生成する時代の創造性論の理論資源を提供する。",
         "related_ai_phenomenon":"LLMによる学習データの組み換え生成"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"インターテクスチュアリテ詩学",
         "description":"PT-DB詩学の中核領域。"}])

add(**C, name_ja="ハイパーテクスト理論（ジュネット）",
    name_en="hypertext theory (Genette)",
    name_original="hypertextualité",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラール・ジュネット『パランプセスト』(1982)が定義した、テクストB（ハイパーテクスト）が先行テクストA（ハイポテクスト）に変換・模倣・パロディ等で関わる関係。『オデュッセイア』に対する『ユリシーズ』、『アエネイス』に対する『失われた時を求めて』等を分析対象とする。",
    background="クリステヴァ・インターテクスチュアリテ概念の構造主義的精密化と、形式的分類化の試み。",
    development="ポストモダン文学・パロディ・アダプテーション研究の基本フレームワーク。電子文学のハイパーテクスト概念とは別系統だが理論的接点あり。",
    historical_context="1980年代フランス構造主義詩学の精密化期。",
    primary_source_url=ARCHIVE+"details/palimpsestslit00gene",
    primary_source_type="Internet Archive: Palimpsests",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"テクスト間関係論",
         "description":"PT-DB詩学の中核領域。"}])

add(**C, name_ja="パラテクスト（ジュネット）",
    name_en="paratext (Genette)",
    name_original="paratexte",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラール・ジュネット『閾』(1987)が体系化した、テクスト本体を取り巻く周辺要素群。表題・序文・献辞・章題・注・帯・著者写真・インタビュー等。「ペリテクスト(péritexte)」（書物内）と「エピテクスト(épitexte)」（書物外）に分類され、テクストの読みを枠づける装置として分析される。",
    background="物理的書物の形式的・歴史的研究と、構造主義詩学の総合化。",
    development="書誌学・文学社会学（ピエール・ブルデュー、ジェラール・ジュネット自身）、デジタル時代のメタデータ論まで継承される基本概念。",
    historical_context="書物文化の構造的分析の理論化期。",
    primary_source_url=ARCHIVE+"details/paratextsthresho0000gene",
    primary_source_type="Internet Archive: Paratexts (Genette)",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"テクストを枠づけるパラテクスト装置は、AI生成テクストにおけるシステムプロンプト・モデルカード・利用規約等の新パラテクストの位置を考える基盤となる。",
         "related_ai_phenomenon":"AI生成における新パラテクスト（システムプロンプト等）"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"パラテクスト論",
         "description":"PT-DB詩学の重要概念。"}])

add(**C, name_ja="トランステクスチュアリテ",
    name_en="transtextuality",
    name_original="transtextualité",
    period_key="構造主義・ポスト構造主義期",
    definition="ジェラール・ジュネット『パランプセスト』(1982)が、クリステヴァ・インターテクスチュアリテ概念をより包括的に再定義した上位概念。テクストが「他のテクストとの関係において」存在するすべての類型を指し、五つの下位範疇（インターテクスチュアリテ／パラテクスチュアリテ／メタテクスチュアリテ／ハイパーテクスチュアリテ／アルキテクスチュアリテ）に分類される。",
    background="クリステヴァ概念の曖昧性を構造主義的精密性で解消する試み。",
    development="現代テクスト理論の基本分類体系として標準化。",
    historical_context="1980年代フランス構造主義詩学の精密化期。",
    primary_source_url=ARCHIVE+"details/palimpsestslit00gene",
    primary_source_type="Internet Archive: Palimpsests",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"テクスト関係論",
         "description":"PT-DB詩学に直接接続。"}])

add(**C, name_ja="ダブル・コーディング",
    name_en="double coding",
    name_original="double coding",
    period_key="構造主義・ポスト構造主義期",
    definition="チャールズ・ジェンクスがポストモダン建築論『ポストモダン建築の言語』(1977)で導入し、ウンベルト・エーコ『薔薇の名前』(1980)後記やリンダ・ハッチオンがポストモダン文学に拡張した概念。エリート読者向けの高級コードと大衆読者向けの俗コードを同時に作動させる、ポストモダン特有の表現戦略。",
    background="ポストモダン芸術がモダニズムの「高級／低俗」分割を解体する試みの理論化。",
    development="ハッチオン『ポストモダニズムの詩学』(1988)、ジェンクスの建築理論を経て、現代カルチュラル・スタディーズの基本概念に。",
    historical_context="1970-80年代ポストモダン理論隆盛期。",
    primary_source_url=ARCHIVE+"details/poeticsofpostmod0000hutc",
    primary_source_type="Internet Archive: A Poetics of Postmodernism (Hutcheon)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"高級／低俗コードの同時作動は、AI生成における異なる読者層への同時最適化の理論的祖型を提供する。",
         "related_ai_phenomenon":"AI生成テクストの多層読者向け最適化"}])

add(**C, name_ja="シミュラークル（ボードリヤール）",
    name_en="simulacra (Baudrillard)",
    name_original="simulacre",
    period_key="構造主義・ポスト構造主義期",
    definition="ジャン・ボードリヤール『シミュラークルとシミュレーション』(1981)が展開した、もはやオリジナルを持たない複製＝シミュラークルが現実を覆い尽くしたとするポストモダン社会理論。記号の四段階（反映／隠蔽／不在の隠蔽／関係なし）を経て純粋なシミュラークル時代に至るとされる。",
    background="マルクス疎外論・ドゥボール『スペクタクルの社会』(1967)と、構造主義記号論の総合的過激化。",
    development="ポストモダン文学批評（フレドリック・ジェイムソン、リンダ・ハッチオン）、サイバースペース論、メディア研究、AI生成論まで広範に影響。",
    historical_context="1980年代フランス・ポストモダン理論の頂点期。",
    primary_source_url=ARCHIVE+"details/simulacrasimulat0000baud",
    primary_source_type="Internet Archive: Simulacra and Simulation",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"オリジナル不在の純粋シミュラークルというボードリヤール理論は、AI生成テクスト・画像が「オリジナルなき複製」として流通する時代の批評の最重要先行理論である。",
         "related_ai_phenomenon":"AI生成における純粋シミュラークル時代の到来"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"シミュラークル",
         "description":"哲学・メディア論の中核概念。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"AI生成画像・テクストの真正性",
         "description":"AI生成における真正性論争の理論的祖型。"}])

add(**C, name_ja="スキゾ分析（ドゥルーズ＝ガタリ）",
    name_en="schizoanalysis (Deleuze-Guattari)",
    name_original="schizoanalyse",
    period_key="構造主義・ポスト構造主義期",
    definition="ジル・ドゥルーズ＝フェリックス・ガタリ『アンチ・オイディプス』(1972)『千のプラトー』(1980)が展開した、精神分析を超克する欲望の流れ・機械論的分析法。エディプス的家族構造に固定された主体ではなく、多方向に流れる欲望の機械として欲望を捉え直す。",
    background="68年五月革命後のフランス哲学のラカン精神分析批判運動。",
    development="ロザリオ・ブライドッティ等の現代ポストヒューマニズム、現代SF批評、サイバーフェミニズムの理論的基盤として継承。",
    historical_context="1970年代フランス哲学の反主流派形成期。",
    primary_source_url=SEP+"deleuze/",
    primary_source_type="SEP: Gilles Deleuze",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"主体を欲望の流れ・機械として捉える視座は、AI／人間ハイブリッドの主体性を考える理論資源となる。",
         "related_ai_phenomenon":"AI／人間ハイブリッド主体の理論化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ドゥルーズ＝ガタリ哲学",
         "description":"哲学DBの中核領域。"}])

add(**C, name_ja="リゾーム文学",
    name_en="rhizome literature",
    name_original="rhizome",
    period_key="構造主義・ポスト構造主義期",
    definition="ドゥルーズ＝ガタリ『千のプラトー』(1980)序章「リゾーム」が示した、樹木型階層構造に対比される非階層的・非中心的・多方向的な接続構造。文学にあっては、線形物語に対する非線形多接続的物語、ポストモダン百科全書的小説（ピンチョン・カルヴィーノ等）の理論的範型となる。",
    background="ポスト構造主義哲学の反階層的存在論の文学理論的応用。",
    development="ハイパーテクスト文学理論（ボルター、ランドウ）、現代電子文学、ネットワーク社会論まで継承。",
    historical_context="1980年代ポスト構造主義の文学・メディア理論的展開期。",
    primary_source_url=ARCHIVE+"details/thousandplateaus0000dele",
    primary_source_type="Internet Archive: A Thousand Plateaus",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"非線形・多接続的なリゾーム構造は、LLMがアテンション機構で生成する多接続的・非線形なテクスト構造と直接的構造的類比を示す。",
         "related_ai_phenomenon":"LLMアテンション機構のリゾーム的構造"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"リゾーム",
         "description":"哲学DBの中核概念。"},
        {"target_db":"AI-Development","link_type":"parallel",
         "target_entity_name":"アテンション機構の非線形性",
         "description":"LLMアテンション機構との構造的類比。"}])


# ============================================================
# main
# ============================================================

def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    expected = 40
    if len(CONCEPTS) != expected:
        print(f"[c36] WARNING: expected {expected} concepts, got {len(CONCEPTS)}")
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
        print(f"[c36] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c36] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        print(f"[c36] table totals: ft_tags={summary['fourth_transform_tags']}, cross_domain={summary['cross_domain']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
