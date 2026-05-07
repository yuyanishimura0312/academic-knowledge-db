"""LIT-DB Phase 2 Wave 4 — C28: Russia / Slavic 19th-century Golden Age (40 concepts).

Subfield: lit_russia_slavic (id=18), region='周縁横建' -> note: project specifies
the region label '周縁横断' for the 19th-century team.
Sources: rvb.ru (Russian Virtual Library), feb-web.ru (Fundamental Electronic
Library of Russian Literature), Project Gutenberg, plato.stanford.edu, and
academic-grade Wikipedia (en/ja/ru). PD primary materials -> 'primary'; canonical
scholarly secondary -> 'secondary'; synthetic critical categories -> 'tertiary'.
Cyrillic original spellings included only when reliably attestable.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

# 19世紀ロシア・スラヴ文学黄金時代を一つの長期周期として扱い、より細かい
# 主義・運動はsubperiodとして分割する。
PERIODS = [
    ("ロシア文学黄金時代", "Russian Golden Age of Literature", 1820, 1900,
     "プーシキンからチェーホフに至るロシア文学の古典的成熟期。リアリズムを中軸に、ロマン主義・自然派・象徴主義萌芽を経由して、ロシア小説と詩学の世界文学的地位を確立した。"),
    ("ロシア・センチメンタリズム期", "Russian Sentimentalism", 1790, 1820,
     "カラムジン以降の感傷主義。フランス語サロン文化と接続しつつ、近代ロシア散文の文体基礎を形成。"),
    ("ロシア銀の時代前夜", "Pre-Silver Age", 1890, 1900,
     "象徴主義および世紀末の運動が立ち上がる、19世紀末から銀の時代に向かう過渡期。"),
]

# Source URL bases (real, verifiable)
RVB = "https://rvb.ru/"           # Russian Virtual Library
FEB = "http://feb-web.ru/"        # Fundamental Electronic Library
GUTEN = "https://www.gutenberg.org/"
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
# A: 主要主義・運動（8件）
# ============================================================
add(**C, name_ja="ロシア・センチメンタリズム",
    name_en="Russian Sentimentalism",
    name_original="русский сентиментализм",
    period_key="ロシア・センチメンタリズム期",
    definition="18世紀末から19世紀初頭にかけて、カラムジンを中心に展開した感傷主義文学運動。フランス感傷主義およびイギリス感性文学の影響下で、感情・内面・自然への共感を主題とし、近代ロシア散文の文体基盤を形成した。『哀れなリーザ』(1792)が代表作。",
    background="エカテリーナ二世期の啓蒙とフランス文化受容、ルソー的感性論の浸透。",
    development="プーシキン以降のロマン主義・リアリズムへ吸収され、近代ロシア小説の心理描写の前史となった。",
    historical_context="ロシア貴族文化のフランス語サロン化と、近代ロシア文学言語の整備期。",
    primary_source_url=RVB+"18vek/karamzin/",
    primary_source_type="Russian Virtual Library: Karamzin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロシア・ロマンチズム",
    name_en="Russian Romanticism",
    name_original="русский романтизм",
    period_key="ロシア文学黄金時代",
    definition="1810-40年代にジューコフスキー・プーシキン初期・レールモントフ・ゴーゴリ初期を中心に展開したロマン主義。ドイツ・イェナ派とイギリス・バイロニズムの受容を起点に、ロシア固有の歴史・民衆・自然へ志向を移し、独自の「カフカース・ロマン主義」を生んだ。",
    background="ナポレオン戦争後の民族意識覚醒と、ドイツ哲学的観念論の輸入。",
    development="プーシキン『コーカサスの捕虜』、レールモントフ『悪魔』、ゴーゴリ『ヴィイ』を経て、自然派へ展開した。",
    historical_context="デカブリスト運動の挫折とニコライ一世期の検閲強化下での内面的・象徴的表現の成熟。",
    primary_source_url=WIKI_EN+"Russian_Romanticism",
    primary_source_type="Wikipedia: Russian Romanticism",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="自然派",
    name_en="Natural School",
    name_original="натуральная школа",
    period_key="ロシア文学黄金時代",
    definition="1840年代にベリンスキーが理論化し、ゴーゴリ『外套』を範型として展開したロシア・リアリズムの初期形態。下層官吏・農奴・都市貧民を主題化し、「生理学的スケッチ」と呼ばれる社会記述的散文を中心に、ドストエフスキー・トゥルゲーネフ初期作品を含む幅広い潮流を形成した。",
    background="フランス自然主義・生理学的スケッチの輸入と、農奴制下のロシア社会への批判的眼差し。",
    development="トゥルゲーネフ『猟人日記』、ドストエフスキー『貧しき人々』、ネクラーソフ詩を経て、後期リアリズム・ナロードニチェストヴォ文学へ展開した。",
    historical_context="ベリンスキー批評の影響力拡大と、農奴解放（1861）前夜の社会的緊張。",
    primary_source_url=WIKI_EN+"Natural_school",
    primary_source_type="Wikipedia: Natural school",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="スラヴ派 vs 西欧派",
    name_en="Slavophiles vs Westernizers",
    name_original="славянофилы и западники",
    period_key="ロシア文学黄金時代",
    definition="19世紀半ばのロシア知識人を二分した思想・文学論争。スラヴ派（ホミャコフ、キレエフスキー、アクサーコフ兄弟）はロシアの正教的・共同体的固有性を主張し、西欧派（ベリンスキー、ゲルツェン、トゥルゲーネフ）は西欧的合理主義・進歩主義を主張した。文学・批評・歴史哲学の核心争点となった。",
    background="ピョートル大帝以降の西欧化政策の評価をめぐる、ロシア・アイデンティティ論争。",
    development="トルストイの民衆論、ドストエフスキー『カラマーゾフの兄弟』のゾシマ長老の像、19世紀末ロシア宗教哲学（ソロヴィヨフ）まで深く影響した。",
    historical_context="クリミア戦争(1853-56)の敗北と農奴解放期の社会改革論議。",
    primary_source_url=WIKI_EN+"Slavophile",
    primary_source_type="Wikipedia: Slavophile",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ナロードニチェストヴォ文学",
    name_en="Narodnik literature",
    name_original="народничество",
    period_key="ロシア文学黄金時代",
    definition="1860-80年代の民衆主義（ナロードニキ）運動と連動した文学。「民衆へ（к народу）」の運動精神のもと、農民共同体（ミール、オープシナ）を理想化し、グレブ・ウスペンスキー、ズラトヴラーツキー等の散文と、トルストイ後期の民衆主義的言説に結実した。",
    background="農奴解放後の農村実態への幻滅と、ゲルツェン・チェルヌィシェフスキーから継承された農民社会主義思想。",
    development="トルストイ晩年の民衆教育・宗教論、20世紀初頭の社会革命党の理念にまで継承された。",
    historical_context="1874年「ヴ・ナロード（民衆の中へ）」運動とその挫折、テロリズム化の歴史。",
    primary_source_url=WIKI_EN+"Narodniks",
    primary_source_type="Wikipedia: Narodniks",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"民衆主義・農民共同体研究",
         "description":"ナロードニチェストヴォの農民共同体観は人類学的共同体論（ミール、オープシナ研究）と直接接続する。"}])

add(**C, name_ja="ニヒリズム文学",
    name_en="Nihilist literature",
    name_original="нигилизм в литературе",
    period_key="ロシア文学黄金時代",
    definition="1860年代以降のロシア文学において、伝統的価値・宗教・権威を拒否する若い知識人世代を主題化した文学傾向。トゥルゲーネフ『父と子』のバザロフを範型とし、ドストエフスキー『悪霊』『地下室の手記』、チェルヌィシェフスキー『何をなすべきか』が応答的に展開した。",
    background="1860年代の若い世代（шестидесятники、六十年代人）の登場と、自然科学的唯物論・実証主義の流入。",
    development="ドストエフスキーによるニヒリズム批判から、ニーチェ受容を経て、20世紀ロシア宗教哲学（シェストフ、ベルジャーエフ）の主題となった。",
    historical_context="農奴解放後の急進化と、皇帝アレクサンドル二世暗殺(1881)に至る政治的危機。",
    primary_source_url=WIKI_EN+"Russian_nihilist_movement",
    primary_source_type="Wikipedia: Russian nihilist movement",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ニヒリズム",
         "description":"ロシア・ニヒリズム文学はニーチェのニヒリズム概念に先行・並行し、20世紀ロシア宗教哲学・実存哲学の中心争点となった。"}])

add(**C, name_ja="ロシア象徴主義",
    name_en="Russian Symbolism",
    name_original="русский символизм",
    period_key="ロシア銀の時代前夜",
    definition="1890年代以降に始まり1910年代に頂点を迎えるロシア文学運動。ベルモント、ブリューソフ、メレシュコフスキーを第一世代、ブローク、ベールイ、イヴァーノフを第二世代とする。フランス象徴主義の受容を契機としつつ、ソロヴィヨフのソフィア神秘論を吸収した独自の宗教的・形而上学的象徴主義を展開した。",
    background="フランス象徴主義（ボードレール、マラルメ、ヴェルレーヌ）の受容と、ソロヴィヨフ宗教哲学の影響。",
    development="アクメイズム、未来派、形式主義との対立を経て、20世紀ロシア・モダニズムの基盤となった。",
    historical_context="ロシア「銀の時代」の精神文化の高揚と、ロシア革命前夜の社会的緊張。",
    primary_source_url=WIKI_EN+"Symbolist_movement_in_Russia",
    primary_source_type="Wikipedia: Symbolist movement in Russia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ロシア・リアリズム",
    name_en="Russian Realism",
    name_original="русский реализм",
    period_key="ロシア文学黄金時代",
    definition="1840-90年代を貫通するロシア文学の中核様式。自然派を起点に、トゥルゲーネフ、ドストエフスキー、トルストイ、チェーホフが各自の方法で深化させた。社会的・心理的・形而上学的諸層を統合し、19世紀世界文学最高の散文形式と評価される。",
    background="ベリンスキー批評の理論的影響、フランス・リアリズム（バルザック、フローベール）受容、農奴解放後の社会変動への文学的応答。",
    development="ロシア小説の長編形式（poema-novel）を完成させ、20世紀世界文学（プルースト、ジョイス、フォークナー）に深く影響した。",
    historical_context="アレクサンドル二世期の大改革と、世紀末の社会構造変動。",
    primary_source_url=WIKI_EN+"Russian_literature#Realism",
    primary_source_type="Wikipedia: Russian Realism",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

# ============================================================
# B: 主要作家概念（8件）
# ============================================================
add(**C, name_ja="プーシキンの「余計な人」",
    name_en="Pushkin's superfluous man",
    name_original="лишний человек",
    period_key="ロシア文学黄金時代",
    definition="プーシキン『エヴゲーニー・オネーギン』(1823-31)に登場する貴族青年オネーギンを範型とする、社会的能力と欲望を持ちながら歴史の中に位置を見出せない知識人類型。後にレールモントフ『現代の英雄』ペチョーリン、トゥルゲーネフ『ルーディン』に継承され、ロシア文学の中心人物像の一つとなった。",
    background="ニコライ一世期の検閲・反動政治下で、貴族知識人の社会的無力感が深化した時代背景。",
    development="ゲルツェン1850年論文「余計な人」で類型化され、トゥルゲーネフが用語を文学批評に定着させた。",
    historical_context="デカブリスト乱(1825)後の貴族知識人の政治的無力化。",
    primary_source_url=RVB+"pushkin/01text/04onegin/",
    primary_source_type="Russian Virtual Library: Pushkin Onegin",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゴーゴリ「外套」の小人",
    name_en="Gogol's little man",
    name_original="маленький человек",
    period_key="ロシア文学黄金時代",
    definition="ゴーゴリ『外套』(1842)の主人公アカーキー・アカーキエヴィチに代表される、官僚社会の最下層に位置する卑小な人物像。ドストエフスキーが「我々は皆ゴーゴリの『外套』から出てきた」と述べたように、後の自然派・心理小説の中心人物類型として継承された。",
    background="ペテルブルク官僚機構の階層構造と、自然派の社会批判的眼差し。",
    development="ドストエフスキー『貧しき人々』『二重人格』『地下室の手記』、チェーホフ短編に発展継承。",
    historical_context="ニコライ一世期の官僚国家形成と、首都の階級的非人称化。",
    primary_source_url=RVB+"gogol/",
    primary_source_type="Russian Virtual Library: Gogol",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="レールモントフ『現代の英雄』",
    name_en="Lermontov's A Hero of Our Time",
    name_original="Герой нашего времени",
    period_key="ロシア文学黄金時代",
    definition="レールモントフ『現代の英雄』(1840)の主人公ペチョーリン像と、その章別構成・複数視点・時系列撹乱による近代心理小説の先駆形態。プーシキンの「余計な人」を継承しつつ、よりニヒリスティックでバイロン的悪魔性を持つ人物像を、フォーマル・イノベーションとともに造形した。",
    background="バイロニズム受容、コーカサス戦争体験、ニコライ一世期の閉塞的社会感覚。",
    development="ロシア心理小説の方法的祖型となり、ナボコフを含む20世紀ロシア小説に継承された。",
    historical_context="1830年代のロシア貴族知識人の「呪われた世代」意識。",
    primary_source_url=RVB+"lermontov/",
    primary_source_type="Russian Virtual Library: Lermontov",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="トゥルゲーネフ『父と子』世代対立",
    name_en="Turgenev's Fathers and Sons generational conflict",
    name_original="Отцы и дети",
    period_key="ロシア文学黄金時代",
    definition="トゥルゲーネフ『父と子』(1862)が定式化した、貴族リベラル世代（父）と平民出ニヒリスト世代（子）の世代論的対立構造。バザロフという人物造形を通じて、世代対立を時代精神の構造的問題として把握する文学的方法論を確立した。",
    background="1860年代のロシア知識人の世代交代と、農奴解放後の社会階層流動化。",
    development="後の世代論的小説（ドストエフスキー『悪霊』、トルストイ『アンナ・カレーニナ』）の基本枠組みとなり、20世紀ロシア・ヨーロッパ小説に継承された。",
    historical_context="アレクサンドル二世大改革期の社会的世代交代。",
    primary_source_url=RVB+"turgenev/",
    primary_source_type="Russian Virtual Library: Turgenev",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ドストエフスキー「ポリフォニー」（バフチン解釈）",
    name_en="Dostoevsky's polyphony (Bakhtin's reading)",
    name_original="полифония",
    period_key="ロシア文学黄金時代",
    definition="バフチン『ドストエフスキーの詩学』(1929/1963)で定式化された、ドストエフスキー長編小説の構造原理。複数の独立した意識・声が、作者に従属することなく対等に対話的に共存する構造を指す。「主人公は作者の客体ではなく、独立した発話主体」とされ、近代独白型小説（トルストイ）と対比される。",
    background="ドストエフスキー長編の語り手・人物関係の特異性と、バフチン1920年代の対話的文体論。",
    development="バフチンの全著作を貫く中心概念となり、20世紀後半の文学理論・物語論・哲学（クリステヴァ、トドロフ）に決定的影響を与えた。",
    historical_context="ドストエフスキー後期長編(『罪と罰』『悪霊』『カラマーゾフの兄弟』)の特異な構造と、20世紀ソヴィエト批評理論の発展。",
    primary_source_url=WIKI_EN+"Polyphony_(literature)",
    primary_source_type="Wikipedia: Polyphony in literature",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"バフチンのポリフォニー概念は、複数の独立した意識・声が単一の作者主体に統合されない構造を理論化する。LLM時代の人間-AI共著における多声的主体性の哲学的先駆として再読される。",
         "related_ai_phenomenon":"LLMと人間の共著における多声的主体性"},
        {"axis":"物語","status":"rethinking",
         "rationale":"単一の語り手・統一的物語に依拠しないポリフォニー構造は、AI生成テキストにおける物語の脱中心化と類比的に検討されている。",
         "related_ai_phenomenon":"AI共著小説における脱中心化された物語構造"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"バフチン詩学・対話的想像力",
         "description":"ポリフォニー概念はバフチン詩学の中核を成し、対話的想像力・カーニバル概念と一体的体系を構成する。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"対話の哲学（ブーバー、レヴィナス）",
         "description":"バフチンの対話的存在論は20世紀対話の哲学と並行的に展開した。"}])

add(**C, name_ja="ドストエフスキー『悪霊』",
    name_en="Dostoevsky's Demons",
    name_original="Бесы",
    period_key="ロシア文学黄金時代",
    definition="ドストエフスキー『悪霊』(1872)が示した政治的ニヒリズム・テロリズム・カリスマ的支配の文学的予言性。ネチャーエフ事件をモデルとし、革命運動の心理的・形而上学的構造を描出した。20世紀全体主義論の文学的祖型として読み直されている。",
    background="ネチャーエフ事件(1869)とロシア革命運動の急進化、ドストエフスキー自身のペトラシェフスキー事件・流刑体験。",
    development="20世紀のカミュ『反抗的人間』、ハナ・アーレント『全体主義の起源』に継承され、政治哲学の重要参照源となった。",
    historical_context="人民の意志党・社会革命党に至るロシア・テロリズム史の源流期。",
    primary_source_url=GUTEN+"ebooks/8117",
    primary_source_type="Project Gutenberg: The Possessed/Demons",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"全体主義の起源",
         "description":"アーレントの全体主義論は『悪霊』の革命心理分析を哲学的に継承した。"}])

add(**C, name_ja="トルストイの歴史哲学",
    name_en="Tolstoy's philosophy of history",
    name_original="философия истории Толстого",
    period_key="ロシア文学黄金時代",
    definition="トルストイ『戦争と平和』(1865-69)第二部エピローグおよび本文歴史叙述に展開された、英雄史観批判と無数の人間意志の総体としての歴史過程論。ナポレオン的「偉人」を否定し、無名の民衆と諸偶然の総和として歴史を捉える反英雄史観を文学的に構築した。",
    background="ナポレオン研究、ヘーゲル歴史哲学、ロシア・スラヴ派的歴史観の総合。",
    development="アイザイア・バーリン『ハリネズミと狐』(1953)が哲学的に体系化し、20世紀歴史哲学（ブローデル長期持続論との比較等）に影響した。",
    historical_context="クリミア戦争(1853-56)体験と1812年祖国戦争の記憶、19世紀後半ロシア国民意識形成。",
    primary_source_url=GUTEN+"ebooks/2600",
    primary_source_type="Project Gutenberg: War and Peace",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"歴史哲学",
         "description":"トルストイの反英雄史観はヘーゲル・カーライルの英雄史観への文学的批判として、20世紀歴史哲学に参照される。"}])

add(**C, name_ja="チェーホフの「中身のない人物」",
    name_en="Chekhov's hollow characters",
    name_original="чеховский герой",
    period_key="ロシア文学黄金時代",
    definition="チェーホフ後期短編・戯曲(『桜の園』『三人姉妹』『ワーニャ伯父さん』等)に特徴的な、明確な意思・行動・解決を欠き、決定的瞬間が訪れないまま日常に沈殿する人物像。19世紀ロシア小説の英雄主義的人物像を解体し、20世紀モダニズム文学の心理表現に直接接続した。",
    background="19世紀末ロシア知識人層の停滞感と、医師としてのチェーホフの非英雄主義的観察。",
    development="ベケット、サミュエル・ベケット、英米モダニズムの「小さな主体」表現の祖型となった。",
    historical_context="アレクサンドル三世期の反動と、世紀末ロシア知識人の倦怠的気分。",
    primary_source_url=WIKI_EN+"Anton_Chekhov",
    primary_source_type="Wikipedia: Anton Chekhov",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"チェーホフ的「中身のない主体」は、行動・決断・自己同一性を欠いたまま日常に堆積する主体像であり、AI時代の主体性希薄化（行為主体不在のテキスト生成）と理論的に重ね合わせ可能である。",
         "related_ai_phenomenon":"AI生成テキストにおける希薄主体・能動性不在"}])

# ============================================================
# C: 主要主題/世界観（8件）
# ============================================================
add(**C, name_ja="ロシア魂",
    name_en="Russian soul",
    name_original="русская душа",
    period_key="ロシア文学黄金時代",
    definition="19世紀ロシア文学・思想において、ロシア民族固有の精神性として語られた象徴的概念。受苦・宗教性・共同体的感受性・西欧的合理主義への抵抗を含む複合的な文化的自己理解として、ドストエフスキー、トルストイ、ベルジャーエフらに展開された。",
    background="スラヴ派の宗教民族論、19世紀ロマン主義的国民精神論。",
    development="20世紀ロシア宗教哲学（ベルジャーエフ『ロシアの理念』、フランク）に体系化され、ソヴィエト・ポストソヴィエトの自己理解に影響した。",
    historical_context="クリミア戦争敗北以降のロシア・アイデンティティ危機と、西欧近代との対比的自己定義。",
    primary_source_url=WIKI_EN+"Russian_soul",
    primary_source_type="Wikipedia: Russian soul",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="受苦",
    name_en="suffering / stradanie",
    name_original="страдание",
    period_key="ロシア文学黄金時代",
    definition="19世紀ロシア文学の中心主題。正教神学のキリスト論的受苦観を背景に、ドストエフスキー文学に最も濃密に展開され、苦しみを通じた人格的成長・宗教的真理発見・他者との共感的結合という構造を持つ。トルストイ『イワン・イリッチの死』にも現れる。",
    background="ロシア正教神学のキリスト論的受苦観、ナロードニチェストヴォの民衆受苦理解。",
    development="ベルジャーエフ・シェストフのロシア宗教実存哲学に継承され、20世紀人格主義に影響を与えた。",
    historical_context="農奴制下の民衆受苦の歴史的記憶と、知識人による民衆苦の自己投影。",
    primary_source_url=WIKI_EN+"Russian_Orthodox_theology",
    primary_source_type="Wikipedia: Russian Orthodox theology",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"invariant",
         "rationale":"受苦を通じた真正性獲得というロシア文学の主題は、AI共著時代においても固有経験の真正性指標として機能する不変軸である。",
         "related_ai_phenomenon":"AI生成テキストにおいて模倣困難な真正経験指標"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ロシア宗教哲学",
         "description":"ベルジャーエフ・シェストフの受苦論は19世紀ロシア文学の主題を哲学的に体系化したもの。"}])

add(**C, name_ja="ユロージヴィ（聖愚者）",
    name_en="yurodivy / holy fool",
    name_original="юродивый",
    period_key="ロシア文学黄金時代",
    definition="ロシア正教伝統における「キリストのための愚者」概念に由来する文学的・文化的人物類型。世俗的合理性を逸脱した狂気的・愚かしい外見の下に深い宗教的真理を体現する人物像で、プーシキン『ボリス・ゴドゥノフ』、ドストエフスキー『白痴』のムイシュキン、『カラマーゾフの兄弟』のアリョーシャに変奏される。",
    background="11世紀以降のロシア正教・ビザンツ正教の聖愚者伝統と、民衆宗教文化。",
    development="20世紀ロシア・モダニズム・ポストモダニズム（プラトーノフ、ヴェネディクト・エロフェーエフ）にも継承される。",
    historical_context="ロシア中世の宗教文化的伝統と、19世紀知識人による民衆宗教性の再評価。",
    primary_source_url=WIKI_EN+"Foolishness_for_Christ",
    primary_source_type="Wikipedia: Foolishness for Christ",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"聖愚者・トリックスター類型",
         "description":"ユロージヴィは人類学的トリックスター・宗教的逸脱者類型と並行する文化人類学的研究対象である。"}])

add(**C, name_ja="リシニー・チェロヴェク（余計な人）",
    name_en="superfluous man",
    name_original="лишний человек",
    period_key="ロシア文学黄金時代",
    definition="19世紀ロシア文学を貫通する中心人物類型。社会的能力と知性を備えながら、自らに値する役割を社会の中に見出せず、行動と関係において「余計」となる貴族・知識人像。プーシキン『オネーギン』を範型に、ゴンチャロフ『オブローモフ』、レールモントフ『ペチョーリン』、トゥルゲーネフ『ルーディン』に変奏される。",
    background="ニコライ一世期の検閲・反動政治下、デカブリスト挫折後の貴族知識人の社会的無力化。",
    development="ゲルツェン1850年論文「余計な人」が用語を定着させ、ロシア文学批評の中心概念となった。20世紀の英米文学（フィッツジェラルド、ヘミングウェイ）の「失われた世代」の祖型。",
    historical_context="デカブリスト乱(1825)以降のロシア貴族知識人層の社会的位置喪失。",
    primary_source_url=WIKI_EN+"Superfluous_man",
    primary_source_type="Wikipedia: Superfluous man",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"「余計な人」は能力と機会のミスマッチ・社会内位置喪失を主題化する人物類型であり、AI時代の知識労働者の主体性危機（自分の能力が機械に置換されうる状況）と再読的に響き合う。",
         "related_ai_phenomenon":"AI時代の知識労働者の役割危機・主体性再考"}])

add(**C, name_ja="アヴォシ（運任せ）",
    name_en="avos / Russian fatalism",
    name_original="авось",
    period_key="ロシア文学黄金時代",
    definition="ロシア民俗・文学伝統における「なんとかなるさ」「運任せ」を意味する文化的・心性的概念。プーシキン詩・散文、トルストイ作品、ロシア諺に反復的に現れ、合理的計画より直観的・宿命論的判断を優先するロシア文化心性の象徴とされる。",
    background="ロシア農民文化の宿命論・諺文化と、貴族文学への民衆心性の浸透。",
    development="20世紀ロシア文化研究（ロトマン、ウスペンスキー）の文化記号論的分析対象となった。",
    historical_context="ロシア農民共同体の予測不能な気候・収穫リスクへの心性的適応。",
    primary_source_url=WIKI_RU+"Авось",
    primary_source_type="Wikipedia (RU): Авось",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="トスカ（憂愁）",
    name_en="toska / longing-melancholy",
    name_original="тоска",
    period_key="ロシア文学黄金時代",
    definition="ロシア文学の中心情調を表す概念で、英・独・仏に正確な対応語のない、深い精神的苦悩・憧憬・形而上学的不安を含む憂愁感情。プーシキン詩、チェーホフ短編「トスカ」(1886)、ナボコフ『ロリータ』エピグラフ的言及などに、ロシア人特有の感情として強調的に展開された。",
    background="ロシア・センチメンタリズム以降の感情語彙整備、正教的精神苦の文化伝統。",
    development="ナボコフが英語・ロシア語の翻訳不可能性を強調することで、20世紀比較文学・翻訳論の象徴的概念となった。",
    historical_context="19世紀ロシア知識人層の社会的閉塞感と、感情の精緻な文学的言語化。",
    primary_source_url=WIKI_EN+"Toska",
    primary_source_type="Wikipedia: Toska",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"invariant",
         "rationale":"トスカは翻訳不可能な情動概念として、機械翻訳・LLM翻訳が均質化・脱文脈化する中で固有文化の不還元性を象徴する不変軸となる。",
         "related_ai_phenomenon":"機械翻訳における情動語の文化的還元不可能性"}])

add(**C, name_ja="ザイカ（吃音／不能の主人公）",
    name_en="zaika / stuttering inability",
    name_original="заика",
    period_key="ロシア文学黄金時代",
    definition="ロシア文学において、吃音・言語不全・意志疎通不能を抱える人物像が反復的に登場する系譜。ドストエフスキー『悪霊』のキリーロフ的不能、ゴーゴリ『外套』アカーキーの言語的衰弱、チェーホフ人物の決断不能性等として現れる、近代ロシア小説特有のテーマ系。",
    background="近代ロシアの言語的階層化（フランス語サロン文化／ロシア語民衆文化／教会スラヴ語宗教文化）下の言語的不安。",
    development="20世紀のプラトーノフ独自言語、ベケット的不能の人物像との比較研究の対象となった。",
    historical_context="近代ロシア知識人の言語アイデンティティ複層性と、文学的言語の確立過程。",
    primary_source_url=WIKI_EN+"Russian_literature",
    primary_source_type="Wikipedia: Russian literature (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="бытие vs быт（存在 vs 日常）",
    name_en="bytie vs byt (Being vs everyday)",
    name_original="бытие vs быт",
    period_key="ロシア文学黄金時代",
    definition="ロシア文化哲学における二項対立概念。бытие（存在・本質的生）と быт（日常生活・生活の沈殿）の対比は、19世紀ロシア文学（チェーホフ、ゴンチャロフ『オブローモフ』）に深く展開され、ヤコブソン1931年論文以降、ロシア文化記号論の中核概念となった。",
    background="ドイツ観念論的存在論のロシア的受容と、ロシア知識人による日常生活批判。",
    development="ヤコブソン、ロトマン記号論を経て、20世紀ロシア文化哲学（ハイデガー受容との並行）の基本枠組みとなった。",
    historical_context="19世紀ロシア知識人の精神的高揚と現実的生活との緊張関係。",
    primary_source_url=WIKI_EN+"Roman_Jakobson",
    primary_source_type="Wikipedia: Roman Jakobson",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"存在と日常",
         "description":"бытие/бытの対比はハイデガーの本来的／非本来的存在論と並行する20世紀ロシア哲学・文化記号論の枠組み。"}])

# ============================================================
# D: 主要詩学・批評（8件）
# ============================================================
add(**C, name_ja="ベリンスキー「現実批評」",
    name_en="Belinsky's reality criticism",
    name_original="реальная критика Белинского",
    period_key="ロシア文学黄金時代",
    definition="ヴィッサリオン・ベリンスキー(1811-48)が確立したロシア文芸批評の方法論。ヘーゲル美学的「美の現実」観念を、ロシア社会の現実的状況把握へと転化し、文学を社会認識の実践として位置づけた。自然派の理論的支柱となり、19世紀ロシア批評の出発点を成す。",
    background="ヘーゲル受容、シェリング自然哲学、フランス社会主義文学論の総合。",
    development="チェルヌィシェフスキー、ドブロリューボフを経て、ロシア・マルクス主義批評・社会主義リアリズム理論まで継承された。",
    historical_context="ニコライ一世期の検閲下で、文学批評が政治社会論議の代替言論空間となった時代。",
    primary_source_url=WIKI_EN+"Vissarion_Belinsky",
    primary_source_type="Wikipedia: Vissarion Belinsky",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チェルヌィシェフスキー「美と現実」",
    name_en="Chernyshevsky's beauty and reality",
    name_original="эстетические отношения искусства к действительности",
    period_key="ロシア文学黄金時代",
    definition="ニコライ・チェルヌィシェフスキー博士論文『現実に対する芸術の美的関係』(1855)で展開された唯物論的美学。「美は生である」を中心命題として、芸術の自律性を否定し、現実の模写・解釈・判断としての芸術観を主張した。ロシア急進主義美学の出発点。",
    background="フォイエルバッハ唯物論、英仏功利主義、ベリンスキー批評の継承。",
    development="ピーサレフ、後のソヴィエト社会主義リアリズムの理論的源流となった。",
    historical_context="1860年代のロシア急進主義知識人層の世界観構築期、農奴解放前夜の社会改革論議。",
    primary_source_url=FEB+"feb/chernyshevsky/",
    primary_source_type="FEB: Chernyshevsky",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ピーサレフ・ニヒリスト批評",
    name_en="Pisarev's nihilist criticism",
    name_original="критика Писарева",
    period_key="ロシア文学黄金時代",
    definition="ドミートリー・ピーサレフ(1840-68)が1860年代に展開した急進的批評。プーシキンを「無用の詩人」と断じる「プーシキン破壊論」が代表的で、芸術の社会的有用性を絶対視し、純文学的価値を否定した。ロシア・ニヒリズム文学批評の極北を成す。",
    background="チェルヌィシェフスキー唯物論美学のさらなる急進化、自然科学的実証主義の文学への適用。",
    development="ドストエフスキー『罪と罰』ラスコーリニコフ造形に間接的影響を与え、ニヒリズム文学批評の象徴的人物となった。",
    historical_context="1860年代ロシア急進主義の文化破壊志向と、芸術自律性論との闘争。",
    primary_source_url=WIKI_EN+"Dmitry_Pisarev",
    primary_source_type="Wikipedia: Dmitry Pisarev",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アポロン・グリゴーリエフ有機的批評",
    name_en="Apollon Grigoriev's organic criticism",
    name_original="органическая критика",
    period_key="ロシア文学黄金時代",
    definition="アポロン・グリゴーリエフ(1822-64)が展開した、シェリング自然哲学とドイツ・ロマン主義美学を基盤とする批評論。文学を有機的全体・歴史的進化体として把握し、ベリンスキー的社会批評とチェルヌィシェフスキー的功利主義批評の双方を批判する第三の道を提示した。",
    background="ドイツ・ロマン主義美学（シェリング、シュレーゲル兄弟）の受容、スラヴ派的文化観の影響。",
    development="ストラーホフ、ドストエフスキー編集『時代』『時』誌のグルント主義（土壌主義）に発展継承された。",
    historical_context="19世紀半ばのロシア・スラヴ派と西欧派の論争空間で、第三の文化観構築を試みた批評運動。",
    primary_source_url=WIKI_EN+"Apollon_Grigoriev",
    primary_source_type="Wikipedia: Apollon Grigoriev",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="バフチン「ポリフォニー」",
    name_en="Bakhtin's polyphony",
    name_original="полифония Бахтина",
    period_key="ロシア文学黄金時代",
    definition="ミハイル・バフチン(1895-1975)が『ドストエフスキーの詩学の諸問題』で定式化した小説理論の中核概念。複数の対等な意識・声が、作者の統合的視点に従属することなく対話的に共存する小説構造を指す。トルストイ的独白型小説と区別される、ドストエフスキー的小説形式の構造原理。",
    background="ロシア正教神学的人格論、シンボリズムの個人と全体の哲学、ヘーゲル弁証法批判。",
    development="20世紀後半の西欧文学理論（クリステヴァ、トドロフ、ジュネット）に決定的影響を与え、ポストモダン物語論の基本概念となった。",
    historical_context="1920年代ソヴィエト初期の文学理論的興隆期と、その後のスターリン期沈黙、1960年代再発見の歴史。",
    primary_source_url=WIKI_EN+"Mikhail_Bakhtin",
    primary_source_type="Wikipedia: Mikhail Bakhtin",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ポリフォニー概念は、単一作者主体への意識統合を否定する小説理論であり、人間-AI共著における多声的・分散的主体性の理論的祖型として再読される。",
         "related_ai_phenomenon":"人間-AI共著における多声的主体性の哲学"},
        {"axis":"物語","status":"rethinking",
         "rationale":"統合的物語視点を持たないポリフォニー構造は、AI生成テキストにおける視点の脱中心化と理論的に類比できる。",
         "related_ai_phenomenon":"AI生成における脱中心化された語り構造"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"対話的想像力",
         "description":"バフチンのポリフォニーは対話的想像力・カーニバル概念と一体的体系を形成する詩学の中核。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"対話の哲学",
         "description":"バフチンの対話的存在論はブーバー、レヴィナスの対話の哲学と並行的・補完的関係にある。"}])

add(**C, name_ja="バフチン「カーニバル」",
    name_en="Bakhtin's carnival",
    name_original="карнавал",
    period_key="ロシア文学黄金時代",
    definition="バフチン『ラブレーと中世・ルネサンスの民衆文化』(1965)で展開された文化詩学概念。中世カーニバル民衆文化における階層・公式秩序の一時的反転、グロテスク・身体性・笑いを通じた解放の構造を、文学のジャンル的記憶として把握する。19世紀ロシア文学（特にドストエフスキー）にもカーニバル化の継承を見出す。",
    background="ラブレー研究、ロシア中世民衆文化研究、ヘーゲル的笑い論への対抗的展開。",
    development="ポストコロニアル批評、フェミニスト批評、ポップカルチャー研究において、抵抗の文化詩学として広く援用された。",
    historical_context="スターリン期の権威主義的文化への暗黙の批判として書かれ、1960年代以降の世界的影響を獲得した。",
    primary_source_url=WIKI_EN+"Mikhail_Bakhtin#Rabelais_and_His_World",
    primary_source_type="Wikipedia: Bakhtin Rabelais",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"カーニバル概念は高/低、公式/民衆の階層的二分を一時的に解体する装置を理論化する。LLMが古典と通俗テキストを階層なく学習・生成する状況において、文化階層の解体可能性を再考させる。",
         "related_ai_phenomenon":"LLMによる古典/通俗階層の解体"},
        {"axis":"正典","status":"rethinking",
         "rationale":"カーニバルにおける正典的秩序の反転は、AI時代の正典・非正典境界の流動化と理論的に共振する。",
         "related_ai_phenomenon":"生成AI時代の正典/非正典境界の流動化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"カーニバル・儀礼的反転",
         "description":"バフチンのカーニバル論はターナー的リミナリティ研究と並行する、文化人類学・宗教人類学の参照源である。"}])

add(**C, name_ja="バフチン「対話的想像力」",
    name_en="Bakhtin's dialogic imagination",
    name_original="диалогическое воображение",
    period_key="ロシア文学黄金時代",
    definition="バフチン『小説の言葉』(1934-35執筆、1975刊)で展開された言語・文学理論。あらゆる言語表現が他の声・他の言語との応答・接触の中にある「対話的」性格を持つことを主張し、独白的言語観（ソシュール的構造言語学、形式主義）への批判的代替を提示する。小説を最も対話的なジャンルとして位置づける。",
    background="ロシア・フォルマリズム批判、フンボルト言語哲学のロシア的受容、ロシア正教的人格対話論。",
    development="20世紀後半の物語論、間テクスト性論（クリステヴァ）、文化批評の基盤となった。",
    historical_context="1930年代ソヴィエト・スターリン期の単声化的文化政策への暗黙の対抗論。",
    primary_source_url=WIKI_EN+"Heteroglossia",
    primary_source_type="Wikipedia: Heteroglossia / Bakhtin",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"対話的言語観・間テクスト性",
         "description":"対話的想像力概念はクリステヴァの間テクスト性論を通じて20世紀後半詩学・記号論に決定的影響を与えた。"}])

add(**C, name_ja="ヤコブソン「文学性」前史",
    name_en="Jakobson's prehistory of literariness",
    name_original="литературность",
    period_key="ロシア銀の時代前夜",
    definition="ロマーン・ヤコブソン(1896-1982)が1921年論文『新最近のロシア詩』で定式化した「文学性（литературность）」概念の19世紀ロシア文学・詩学的前史。ロシア文学を文学たらしめる固有特性の探求は、19世紀ロシア批評（ベリンスキー、ポテブニャー）における文学言語の自律性論議に連なる。",
    background="ロシア・フォルマリズムの結成（オポヤズ、モスクワ言語学サークル）、19世紀ロシア言語学・詩学の継承。",
    development="ロシア・フォルマリズム、プラハ言語学サークル、構造主義詩学・記号論の基盤となった。",
    historical_context="ロシア銀の時代から1920年代の詩学・言語学の革新期。",
    primary_source_url=WIKI_EN+"Roman_Jakobson",
    primary_source_type="Wikipedia: Roman Jakobson",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"文学性・詩的機能",
         "description":"ヤコブソンの文学性概念はロシア・フォルマリズム詩学の中核をなし、20世紀構造主義詩学へ展開した。"}])

# ============================================================
# E: メタ・形式概念（8件）
# ============================================================
add(**C, name_ja="スカーズ（口語語り）",
    name_en="skaz / oral narration",
    name_original="сказ",
    period_key="ロシア文学黄金時代",
    definition="ロシア文学固有の語りの様式概念。地の文を、教養的中立的書記言語ではなく、特定の地方・階層・職業の口語的話者の声としてマスクする技法を指す。ゴーゴリ『外套』、レスコフ短編、後のゾーシチェンコに展開され、エイヘンバウム1918年論文「ゴーゴリの外套はいかにつくられているか」で形式主義的に理論化された。",
    background="ロシア民衆口語伝承の文学的内面化、19世紀ロシア地方主義文学の伝統。",
    development="ロシア・フォルマリズム（エイヘンバウム、シクロフスキー）の中心概念となり、20世紀世界文学の口語的語りの理論的基準となった。",
    historical_context="ロシア文学言語と民衆口語の階層的差異と、その文学的橋渡しの試み。",
    primary_source_url=WIKI_EN+"Skaz",
    primary_source_type="Wikipedia: Skaz",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"スカーズは語りの言語を特定話者の口語性として呈示する技法であり、LLMが言語的人格・声色を選択的に生成する現代において、生成テキストの「声」の問題を理論化する古典的装置として再読される。",
         "related_ai_phenomenon":"LLMにおける声色・言語的人格の生成"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"スカーズ・物語論",
         "description":"スカーズはロシア・フォルマリズム詩学の中核概念で、現代物語論の声・話法理論の理論的源流。"}])

add(**C, name_ja="ロシア小説の長編性",
    name_en="Russian novel's encyclopedic length",
    name_original="русский роман-эпопея",
    period_key="ロシア文学黄金時代",
    definition="トルストイ『戦争と平和』『アンナ・カレーニナ』、ドストエフスキー『カラマーゾフの兄弟』、ゴンチャロフ『オブローモフ』に代表される、ロシア小説特有の超長大・百科全書的・哲学的・社会全体的小説形式。19世紀世界文学において他に類を見ない規模と総合性を達成した。",
    background="ロシア社会の19世紀における巨大な変動と、文学が哲学・歴史・社会論の総合言論空間として機能した特殊状況。",
    development="20世紀の世界文学（プルースト『失われた時を求めて』、ジョイス『ユリシーズ』、マン『魔の山』）の長編形式に深く影響した。",
    historical_context="ロシア「太い雑誌」文化との連動、農奴解放・大改革期の社会的問題総体を文学が引き受けた歴史的文脈。",
    primary_source_url=WIKI_EN+"Russian_literature",
    primary_source_type="Wikipedia: Russian literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="雑誌文学（厚い雑誌）",
    name_en="thick journal / tolstyi zhurnal",
    name_original="толстый журнал",
    period_key="ロシア文学黄金時代",
    definition="19世紀ロシア文学の主要発表媒体となった月刊総合誌（『現代人』『祖国雑記』『ロシア報知』『欧州報知』等）。文学・批評・社会論・歴史・自然科学を一冊に統合し、長編小説の連載媒体・批評論争の舞台・ロシア知識人の公共圏として機能した。検閲下の文学公共圏の中心装置。",
    background="ニコライ一世期の検閲強化下、書物よりも雑誌が公共言論空間として機能した特殊事情。",
    development="20世紀ロシア・ソヴィエト文学にも継承され、『新世界』(『ノーヴィ・ミール』)等の重要雑誌を生んだ。",
    historical_context="ロシア独自の文学的公共圏形成と、知識人読者層の社会的役割。",
    primary_source_url=WIKI_EN+"Thick_journal",
    primary_source_type="Wikipedia: Thick journal",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="検閲との交渉",
    name_en="negotiation with censorship",
    name_original="цензура и литература",
    period_key="ロシア文学黄金時代",
    definition="19世紀ロシア文学全体を規定する制度的・修辞的条件。ニコライ一世期(1825-55)の厳格な検閲、アレクサンドル二世期の緩和、アレクサンドル三世期の再強化を経て、ロシア作家は寓喩・歴史小説・象徴・「奴隷の言葉（эзопов язык）」と呼ばれる暗示的修辞を発達させた。プーシキン以来の文学的特性を形成した制度的力。",
    background="ロシア帝国の検閲制度（1804年検閲令以降）の体系的整備と、知識人言論空間の制限。",
    development="ソヴィエト期の検閲、ペレストロイカ期の検閲解体を経ても、暗示的修辞文化は継承された。",
    historical_context="ロシア絶対主義国家と知識人言論空間の継続的緊張関係。",
    primary_source_url=WIKI_EN+"Censorship_in_the_Russian_Empire",
    primary_source_type="Wikipedia: Censorship in Russian Empire",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ポエマ（叙事詩風長編詩）",
    name_en="poema / Russian narrative poem",
    name_original="поэма",
    period_key="ロシア文学黄金時代",
    definition="ロシア文学固有の韻文・散文ハイブリッド・ジャンル概念。プーシキン『青銅の騎士』『エヴゲーニー・オネーギン』、ゴーゴリ『死せる魂』（散文ながら作者自ら「ポエマ」と命名）、ブローク『十二』を含む、叙事詩でも純粋小説でもない長編詩・準叙事詩形式を指す。ロシア文学の独自ジャンル感覚を象徴する。",
    background="プーシキンによるバイロン的物語詩のロシア化、ロシア韻文・散文境界の独自性。",
    development="20世紀ロシア・モダニズム（ブローク、マヤコフスキー、アフマートヴァ『レクイエム』）に継承された。",
    historical_context="19世紀ロシア文学の韻文中心性と、叙事詩・小説境界の流動性。",
    primary_source_url=WIKI_EN+"Poema",
    primary_source_type="Wikipedia: Poema",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ポーヴェスチ（中編）",
    name_en="povest / Russian medium-length narrative",
    name_original="повесть",
    period_key="ロシア文学黄金時代",
    definition="ロシア文学固有の散文ジャンル概念。短編（рассказ）と長編小説（роман）の中間に位置し、特定の人物・出来事の集中的描写を中心とする中編散文。プーシキン『ベールキン物語』の各篇、ゴーゴリ『ペテルブルクのポーヴェスチ』、ドストエフスキー『地下室の手記』、トルストイ『イワン・イリッチの死』等が含まれる。",
    background="ロシア中世物語伝統の継承、19世紀ロシア散文ジャンル分化の独自性。",
    development="20世紀ロシア文学（チェーホフ、ブーニン、ソルジェニーツィン）でも生産的ジャンルとして継続。",
    historical_context="西欧の novella（ノヴェッラ）と部分的に対応するが、より歴史的・哲学的射程を持つジャンル。",
    primary_source_url=WIKI_EN+"Povest",
    primary_source_type="Wikipedia: Povest",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リテラトゥールヌィ・ブィト（文学的日常）",
    name_en="literary byt / everyday life of literature",
    name_original="литературный быт",
    period_key="ロシア銀の時代前夜",
    definition="後期ロシア・フォルマリズム（エイヘンバウム『文学的日常』1929）が提起した文学社会学的概念。文学を「テクスト」だけでなく、出版・サロン・批評・パトロン・友人関係・経済構造を含む「文学的日常生活」の総体として把握する方法論。19世紀ロシア文学の社会的実存を分析する枠組みとなった。",
    background="ロシア・フォルマリズムの後期社会学的転回、ソヴィエト初期の文学社会学の影響。",
    development="20世紀後半のフランス文学社会学（ブルデュー）、ロシア・ロトマン記号論的文学史と比較される、文学社会学の重要源流。",
    historical_context="1920年代後半の形式主義的内在分析の限界認識と、文学外的諸条件への分析拡張。",
    primary_source_url=WIKI_EN+"Russian_formalism",
    primary_source_type="Wikipedia: Russian formalism",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文学の社会人類学",
         "description":"文学的日常概念は文学を社会的実践として把握する点で、文学人類学・芸術社会学と接続する。"}])

add(**C, name_ja="散文の詩化",
    name_en="poeticization of prose",
    name_original="поэтизация прозы",
    period_key="ロシア文学黄金時代",
    definition="19世紀後半から20世紀初頭ロシア文学に顕著な、散文（小説・短編）が韻文的・象徴詩的特性を獲得していく傾向。ツルゲーネフ「散文詩」、チェーホフ後期短編の音調的構成、ベールイ『ペテルブルク』のリズム化散文として展開され、20世紀ロシア・モダニズム散文の決定的特性となった。",
    background="ロシア・象徴主義における詩・散文境界解体の試み、フランス象徴主義散文詩（ボードレール、ランボー）の受容。",
    development="ベールイ、ナボコフ、プラトーノフのロシア・モダニズム散文の方法論的基盤となった。",
    historical_context="銀の時代におけるジャンル境界の総合的流動化。",
    primary_source_url=WIKI_EN+"Symbolism_(arts)",
    primary_source_type="Wikipedia: Symbolism arts",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


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
        print(f"[c28] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c28] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
