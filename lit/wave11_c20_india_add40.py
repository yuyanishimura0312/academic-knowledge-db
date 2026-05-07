"""LIT-DB Phase 2 Wave 11 — C20 India ADD40 (40 new concepts).

Subfield: lit_india (id=12), region='南アジア'.
Adds 40 NEW concepts under-covered in Phase 2 (initial 80):
  A: Bhakti poetry traditions (regional) — 8
  B: Sangam Tamil + early Dravidian literature — 5
  C: Bengal Renaissance + Indian English novel post-Rushdie — 7
  D: Dalit + partition + women's writing — 7
  E: Regional language novels (Marathi/Malayalam/Kannada/Punjabi) — 7
  F: Oral epics + film/script + new poetics — 6

Sources: GRETIL, SARIT, Project Madurai, Wikisource Hindi/Bengali/Tamil/Marathi,
JSTOR, Britannica, SEP, academic-grade Wikipedia.

Verification policy:
  primary -> PD original-language text or contemporaneous critical document online
  secondary -> canonical scholarly synthesis / encyclopedia entry
  tertiary -> taxonomic critical category constructed for completeness.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("バクティ運動期（地域言語）", "Regional Bhakti Period", 1200, 1700,
     "12-17世紀インド亜大陸でサンスクリットを離れ各地域言語（ヒンディー、マラーティー、ベンガル、タミル、グジャラーティ）で展開したバクティ詩歌運動の時代。"),
    ("サンガム古典期", "Sangam Classical Period", -300, 300,
     "紀元前3世紀から紀元後3世紀にかけて南インド・タミル地方で展開した古典タミル文学の黄金期。アハム・プラム二系列の詩学を確立した。"),
    ("ベンガル・ルネサンス期", "Bengal Renaissance", 1800, 1947,
     "19世紀初頭ラム・モーハン・ローイ以降、植民地支配下のベンガル地方で展開した文化・宗教・文学的近代化運動の時代。"),
    ("印英文学現代期", "Contemporary Indian English Literature", 1980, 2025,
     "ラシュディ『真夜中の子供たち』(1981)以降の印英文学の世界文学的隆盛期。マジック・リアリズム、ディアスポラ、ポストコロニアル主題の交錯。"),
    ("ダリット・周縁文学期", "Dalit and Marginal Literature Period", 1960, 2025,
     "1960年代マハーラーシュトラ・ダリット・パンサーズ運動以降、被抑圧カースト・部族・女性の主体的文学表現が確立した時代。"),
    ("地域言語近現代小説期", "Modern Regional Novel Period", 1900, 2025,
     "20世紀以降のマラーティー、マラヤーラム、カンナダ、パンジャービーなど地域言語による近現代小説の成熟期。"),
    ("インド口承叙事詩・大衆文化期", "Indian Oral Epic and Popular Culture",
     1100, 2025,
     "ラージャスターン・パーブージー、北インド・アールハ、各地の口承叙事詩から、20世紀以降の映画脚本・大衆文化文学までを横断する民衆的物語形式の時代。"),
]


GRETIL = "https://gretil.sub.uni-goettingen.de/gretil.html"
SARIT = "https://sarit.indology.info/"
PMADURAI = "https://www.projectmadurai.org/"
WSRC_HI = "https://hi.wikisource.org/wiki/"
WSRC_BN = "https://bn.wikisource.org/wiki/"
WSRC_TA = "https://ta.wikisource.org/wiki/"
WSRC_MR = "https://mr.wikisource.org/wiki/"
WSRC_PA = "https://pa.wikisource.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_TA = "https://ta.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"
SEP = "https://plato.stanford.edu/entries/"
JSTOR = "https://www.jstor.org/"
GUTEN = "https://www.gutenberg.org/"
ARCHIVE = "https://archive.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_india", region="南アジア")


# ============================================================
# A: バクティ詩歌（地域言語）— 8件
# ============================================================
add(**C, name_ja="トゥカーラーム『アバンガ』",
    name_en="Tukaram's Abhangas",
    name_original="तुकारामांचे अभंग",
    original_script="devanagari",
    period_key="バクティ運動期（地域言語）",
    definition="マハーラーシュトラのワールカリー派バクティ聖人トゥカーラーム（1608頃-1650頃）が遺した約4,500首のマラーティー語抒情詩。ヴィッタル神（パンダルプル）への帰依を中心に、カースト批判・形式儀礼批判・自己の罪意識を率直な口語で表現する。マラーティー文学および南アジア・バクティ運動の頂点を成す。",
    background="13世紀ニャーネーシュワル以来のマハーラーシュトラ・ワールカリー派伝統、シヴァージー期のバクティ復興。",
    development="マハートマー・ガンディーの愛唱詩となり、20世紀マラーティー文学・近代インド精神文化の中核となった。",
    historical_context="17世紀デカン高原のムガル・マラーター抗争期。",
    primary_source_url=ARCHIVE+"details/tukaram-gatha",
    primary_source_type="Internet Archive: Tukaram Gatha (Marathi original)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"トゥカーラームの自己批判的バクティ主体は、現代AI時代における「弱い主体」「確信なき主体」の宗教的祖型として再読できる。",
         "related_ai_phenomenon":"AI時代における自己批判的主体の再構築"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"バクティと身体性",
         "description":"トゥカーラームの口語詩は人類学的に、文字宗教と口承宗教の境界領域を示す事例として研究される。"}])

add(**C, name_ja="ラーマプラサード・セーン",
    name_en="Ramprasad Sen",
    name_original="রামপ্রসাদ সেন",
    original_script="bengali",
    period_key="バクティ運動期（地域言語）",
    definition="18世紀ベンガルのシャークタ派バクティ詩人（1718頃-1775）。母神カーリーへの「シャーマー・サンギート（母神歌）」をベンガル語で創作し、ベンガル・シャークタ・バクティ詩歌の頂点を成した。約350編の歌が伝存し、息子と母の関係性を比喩としてカーリー帰依を歌う。",
    background="18世紀ベンガル・ナワーブ朝期の宗教文化、タントラ系シャークタ伝統とバクティ抒情詩の融合。",
    development="19世紀ラーマクリシュナ・パラマハンサに直接的影響を与え、ベンガル・ルネサンス期の精神文化基盤となった。",
    historical_context="プラッシーの戦い(1757)前後、英国東インド会社支配確立期のベンガル。",
    primary_source_url=WSRC_BN+"লেখক:রামপ্রসাদ_সেন",
    primary_source_type="Bengali Wikisource: Ramprasad Sen",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"母神信仰と非二元論",
         "description":"ラーマプラサードのカーリー信仰はシャークタ系非二元論の抒情的表現であり、インド宗教哲学の重要な実践形態。"}])

add(**C, name_ja="アンダール詩集（ナーラーヤイラ・ディヴィヤ・プラバンダム）",
    name_en="Andal's poems / Tiruppavai",
    name_original="ஆண்டாள் / திருப்பாவை",
    original_script="tamil",
    period_key="バクティ運動期（地域言語）",
    definition="9世紀タミル・アルワール詩人アンダール（女性、唯一の女性アルワール）が遺した『ティルッパーヴァイ』30詩節および『ナーチヤール・ティルモリ』143詩節。ヴィシュヌ神への花嫁的愛を娘の視点から歌う。タミル・ヴィシュヌ・バクティの頂点であり、インド宗教文学における女性的声の古典的範例。",
    background="9世紀タミル・パッラヴァ朝末期のヴィシュヌ・バクティ運動、女性聖人の希少な制度的承認。",
    development="シュリー・ヴィシュヌ派の聖典として「ナーラーヤイラ・ディヴィヤ・プラバンダム」(4,000詩節)に組み込まれ、ラーマーヌジャ哲学体系に取り込まれた。",
    historical_context="9世紀南インド・パッラヴァ王権下のヴィシュヌ寺院文化。",
    primary_source_url=PMADURAI+"pmworks/pm0151.html",
    primary_source_type="Project Madurai: Tiruppavai (Tamil original)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"アンダールの女性的バクティ主体は、AI時代におけるジェンダー化された主体性の宗教的祖型として再読される。",
         "related_ai_phenomenon":"AI時代におけるジェンダー化された主体性の再考"}])

add(**C, name_ja="ナームデーヴ",
    name_en="Namdev",
    name_original="नामदेव",
    original_script="devanagari",
    period_key="バクティ運動期（地域言語）",
    definition="13-14世紀マハーラーシュトラのワールカリー派バクティ聖人（1270-1350）。マラーティー語およびヒンディー語で詩を遺し、シク教聖典『グル・グラント・サーヒブ』にも61首が収められる、地域言語横断的バクティ詩人。仕立て屋カースト出身として、カースト批判の早期典型を示した。",
    background="13世紀デヴギリ・ヤーダヴァ朝期マハーラーシュトラのバクティ運動勃興期、ニャーネーシュワル同時代。",
    development="トゥカーラーム以前のワールカリー派伝統の中核を成し、シク・グル・ナーナクへの間接的影響経路となった。",
    historical_context="13-14世紀デカン地方ヒンドゥー王権末期、ハルジー朝侵入前夜。",
    primary_source_url=WSRC_MR+"लेखक:नामदेव",
    primary_source_type="Marathi Wikisource: Namdev",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジャヤデーヴァ『ギータ・ゴーヴィンダ』",
    name_en="Jayadeva's Gita Govinda",
    name_original="गीतगोविन्दम्",
    original_script="devanagari",
    period_key="バクティ運動期（地域言語）",
    definition="12世紀ベンガル詩人ジャヤデーヴァ（1170頃-1245頃）のサンスクリット抒情詩劇。クリシュナとラーダーの恋愛を12章24歌で歌い、後のヴィシュヌ派バクティ詩歌（特にチャイタニヤ派）の正典となった。サンスクリット古典詩と地域言語バクティを橋渡しする位置を占める。",
    background="12世紀ベンガル・セーナ朝期、サンスクリット古典詩伝統と新興地域言語バクティの接点。",
    development="チャイタニヤ・マハープラブ（1486-1534）以降のガウディーヤ派バクティの中核経典となり、インド古典舞踊・音楽の主要主題となった。",
    historical_context="12世紀北インドのテュルク系侵入前夜、ベンガル・セーナ朝の文化興隆期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Gita Govinda (Sanskrit critical edition)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="チャンディーダース",
    name_en="Chandidas",
    name_original="চণ্ডীদাস",
    original_script="bengali",
    period_key="バクティ運動期（地域言語）",
    definition="14-15世紀ベンガルのヴィシュヌ・バクティ詩人。ラーダーとクリシュナの愛をベンガル民衆語で歌い、「ベンガル抒情詩の祖」と称される。チャイタニヤ派バクティの重要な先駆者であり、近代ベンガル文学（タゴール『マーナシー』等）の言語的・主題的源流となった。",
    background="14-15世紀ベンガル・スルタン朝期の地域言語文学興隆、ジャヤデーヴァ・サンスクリット抒情詩のベンガル化。",
    development="チャイタニヤ派バクティの中核詩源となり、19-20世紀ベンガル・ルネサンス期文学の祖型として再評価された。",
    historical_context="ベンガル・スルタン朝文化政策下の地域言語興隆期。",
    primary_source_url=WSRC_BN+"লেখক:চণ্ডীদাস",
    primary_source_type="Bengali Wikisource: Chandidas",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スールダース",
    name_en="Surdas",
    name_original="सूरदास",
    original_script="devanagari",
    period_key="バクティ運動期（地域言語）",
    definition="15-16世紀北インドのブラージ・バーシャー詩人（1478頃-1583頃）。盲目の詩人としてヴァッラブ派に属し、『スール・サーガラ』(伝承上10万詩節、批判校訂版で約5,000詩節)を遺した。クリシュナの幼児期・青年期愛を詠み、ブラージ・バーシャー文学の頂点を成す。",
    background="ヴァッラブ派バクティ運動、北インド・ムガル前期のブラージ地方文化興隆。",
    development="近代ヒンディー文学の古典的基盤となり、20世紀ヒンディー詩（チャーヤーヴァード等）への系譜的影響源となった。",
    historical_context="アクバル朝期(1556-1605)のヒンドゥー文化諸派の制度的承認期。",
    primary_source_url=WSRC_HI+"रचनाकार:सूरदास",
    primary_source_type="Hindi Wikisource: Surdas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ナナク『グル・グラント・サーヒブ』所収讃歌",
    name_en="Guru Nanak's hymns in the Adi Granth",
    name_original="ਜਪੁ ਜੀ ਸਾਹਿਬ",
    original_script="gurmukhi",
    period_key="バクティ運動期（地域言語）",
    definition="シク教開祖グル・ナーナク（1469-1539）が遺し、第五代グル・アルジュンが編集した『アーディ・グラント』(1604、後の『グル・グラント・サーヒブ』)に収められたパンジャービー語讃歌群。一神教的バクティを核とし、カースト・性別・宗教境界を超える普遍的霊性を主張した。シク教聖典であり、パンジャービー文学の起点。",
    background="15-16世紀北インドのバクティ・スーフィー融合期、カビール・ニルグン伝統との同時代性。",
    development="シク教団の確立(1604正典化、1708最終形成)、パンジャービー文学・北インド宗教詩の中核となった。",
    historical_context="ロディー朝末期からムガル朝初期のパンジャーブ地方の宗教的多元性。",
    primary_source_url=WIKI_EN+"Guru_Granth_Sahib",
    primary_source_type="Wikipedia: Guru Granth Sahib (academic)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"一神教的バクティとシク神学",
         "description":"ナーナク讃歌は宗教多元主義と一神教的バクティを統合する哲学的詩歌であり、南アジア宗教思想史の中核。"}])


# ============================================================
# B: サンガム・タミル古典 — 5件
# ============================================================
add(**C, name_ja="エトゥトハカイ（八集成）",
    name_en="Ettuthokai (Eight Anthologies)",
    name_original="எட்டுத்தொகை",
    original_script="tamil",
    period_key="サンガム古典期",
    definition="サンガム期タミル古典詩の八つの主要詩集（『ナットリナイ』『クルントカイ』『アインクルヌール』『パディットルッパットゥ』『パリパーダル』『カリットカイ』『アハナーヌール』『プラナーヌール』）の総称。約2,381編の詩を収め、アハム（内的・恋愛主題）とプラム（外的・公的主題）の二系列に分類される。古典タミル文学の中核正典。",
    background="紀元前3世紀-紀元後3世紀の南インド・タミル王国群（チェーラ・チョーラ・パーンディヤ）の宮廷文学。",
    development="11世紀以降に編集・注釈化され、19-20世紀U・V・スワーミナータ・アイヤルの校訂出版でタミル国民文学の基盤となった。",
    historical_context="北インドのサンスクリット文化と並立する独自のドラヴィダ古典文化形成期。",
    primary_source_url=PMADURAI+"pmworks/pm0040.html",
    primary_source_type="Project Madurai: Sangam Anthologies",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"古代タミル社会の人類学",
         "description":"サンガム詩集は古代南インド社会の生活・儀礼・政治構造を伝える人類学的一次資料としても重要。"}])

add(**C, name_ja="パットゥパーットゥ（十長詩）",
    name_en="Pattuppattu (Ten Idylls)",
    name_original="பத்துப்பாட்டு",
    original_script="tamil",
    period_key="サンガム古典期",
    definition="サンガム期タミル古典詩の十の長詩集（『ティルムルガールルッパダイ』『ポルナルアールルッパダイ』『シルパディカーラム前駆体』等）。エトゥトハカイと並ぶサンガム詩学の主要正典で、王宮讃歌・案内詩・恋愛長詩を含む。",
    background="サンガム後期の宮廷文学興隆と詩形式の長大化傾向。",
    development="11世紀ナッキーラル等の注釈伝統で正典化され、近代タミル国民文学運動の基盤となった。",
    historical_context="古代南インド王権の文学的儀礼装置としての宮廷詩。",
    primary_source_url=PMADURAI+"pmworks/pm0091.html",
    primary_source_type="Project Madurai: Pattuppattu",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トルカーッピヤム",
    name_en="Tolkappiyam",
    name_original="தொல்காப்பியம்",
    original_script="tamil",
    period_key="サンガム古典期",
    definition="現存最古のタミル文法・詩学書。トルカーッピヤナールに帰せられ、『エルッタディカーラム（音論）』『ソッラディカーラム（語論）』『ポルラディカーラム（事象論）』の3部から成る。アハム・プラム詩学、ティナイ（地理-感情類型）論、メイッパーッドゥ（八情）論を体系化した、ドラヴィダ独自の詩学典籍。",
    background="サンガム期タミル詩実践の理論化要請、サンスクリット『ナーティヤ・シャーストラ』との同時代的並行。",
    development="ドラヴィダ詩学の独自性主張の根拠とされ、20世紀タミル民族主義文化運動の中核典拠となった。",
    historical_context="古代タミル知識人共同体（プラヴァール・サンガム）の制度的成熟期。",
    primary_source_url=PMADURAI+"pmworks/pm0153.html",
    primary_source_type="Project Madurai: Tolkappiyam",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"アハム・プラム詩学",
         "description":"トルカーッピヤムのアハム・プラム二分法はサンスクリット詩学とは独立したドラヴィダ系詩学体系として比較詩学の重要対象。"}])

add(**C, name_ja="ティナイ（地理-感情類型）",
    name_en="Tinai (landscape-emotion typology)",
    name_original="திணை",
    original_script="tamil",
    period_key="サンガム古典期",
    definition="サンガム詩学の中心概念。アハム（恋愛）詩を5つの自然地形（クリンジ山地・ムッライ森林・マルタン耕作地・ネイダル海岸・パーライ荒野）と対応する5感情状態（密会・期待・口論・別離・別離後の苦難）に分類する詩学的類型論。タミル古典詩学の独創性を象徴する範疇。",
    background="古代南インド・タミル地方の地形多様性と、地形-感情の象徴的対応の文学化。",
    development="20世紀タミル文化運動が「ドラヴィダ詩学独自性」の根拠とし、世界比較詩学（A・K・ラマヌジャン『The Interior Landscape』1967）の対象となった。",
    historical_context="古代タミル地方の生態的多様性と、文学的象徴体系化。",
    primary_source_url=WIKI_EN+"Sangam_landscape",
    primary_source_type="Wikipedia: Sangam landscape (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"invariant",
         "rationale":"地形と感情の象徴的対応というティナイ概念は、AI時代の生態-感情モデル化の祖型として再評価される一方、その地理的具体性はAI抽象化に還元されない。",
         "related_ai_phenomenon":"AIによる生態-感情マッピングの限界"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"地形と感情の象徴的対応",
         "description":"ティナイは人類学的に、生態と感情の文化的構造化の典型事例として研究される。"}])

add(**C, name_ja="シラッパディカーラム",
    name_en="Silappatikaram",
    name_original="சிலப்பதிகாரம்",
    original_script="tamil",
    period_key="サンガム古典期",
    definition="紀元後5-6世紀頃のタミル叙事詩。イランゴ・アディガル（チェーラ王族）作とされる。商人カンナガンの妻カンナギが、誤って王に処刑された夫の名誉を取り戻すため首都マドゥライを焼き滅ぼす物語。タミル五大叙事詩の筆頭で、古代タミル女性主体の力強い表象として国民文学の象徴となった。",
    background="サンガム後期から後サンガム期の叙事詩興隆、ジャイナ教文学の影響。",
    development="20世紀タミル民族主義（ドラヴィダ運動）がカンナギを国民英雄化し、現在もマドゥライにカンナギ像が建つ。",
    historical_context="古代タミル王国群（チェーラ・チョーラ・パーンディヤ）の文化交流と都市文化。",
    primary_source_url=PMADURAI+"pmworks/pm0188.html",
    primary_source_type="Project Madurai: Silappatikaram",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# C: ベンガル・ルネサンス + 印英文学現代 — 7件
# ============================================================
add(**C, name_ja="ラム・モーハン・ローイ散文",
    name_en="Ram Mohan Roy's Bengali prose",
    name_original="রামমোহন রায়ের গদ্য",
    original_script="bengali",
    period_key="ベンガル・ルネサンス期",
    definition="近代ベンガル語散文の祖ラム・モーハン・ローイ（1772-1833）の散文著作群。『ヴェーダーンタ・チャンドリカー』(1817)、『ブラフモパサナ』(1828)等の宗教改革論考、サティー（寡婦殉死）廃止論。サンスクリット・ペルシア語・英語の三言語伝統をベンガル語散文に統合し、近代インド散文の起源を形成した。",
    background="19世紀初頭ベンガル・ルネサンス期の宗教改革（ブラフモ・サマージ設立1828）、植民地支配下の文化的近代化。",
    development="近代ベンガル散文の規範を確立し、後のバンキム・チャンドラ、タゴール、ベンガル近代文学全体の言語的基盤となった。",
    historical_context="サティー禁止令(1829、ベンティンク総督)成立期、英印混合文化の制度形成期。",
    primary_source_url=WSRC_BN+"লেখক:রামমোহন_রায়",
    primary_source_type="Bengali Wikisource: Ram Mohan Roy",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベンガル語小説の誕生",
    name_en="birth of Bengali novel",
    name_original="বাংলা উপন্যাসের জন্ম",
    original_script="bengali",
    period_key="ベンガル・ルネサンス期",
    definition="バンキム・チャンドラ・チャットパッダエ『ドゥルゲシュノンディニ』(1865)を起点とするベンガル語近代小説の確立過程。歴史小説・社会小説・心理小説の各様式が同時的に展開し、19世紀後半までに英語以外の南アジア地域言語で初めて成熟した近代小説文化を形成した。",
    background="ベンガル・ルネサンス、英国小説（スコット、サッカレー）の受容、印刷文化の確立。",
    development="シャラトチャンドラ、タゴール、後のヒンディー（プレームチャンド）・タミル等他地域言語小説の規範となった。",
    historical_context="セポイ反乱(1857)後の植民地統治再編期、印刷出版文化の黄金期。",
    primary_source_url=WSRC_BN+"লেখক:বঙ্কিমচন্দ্র_চট্টোপাধ্যায়",
    primary_source_type="Bengali Wikisource: Bankim Chandra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジボナナンド・ダース",
    name_en="Jibanananda Das",
    name_original="জীবনানন্দ দাশ",
    original_script="bengali",
    period_key="ベンガル・ルネサンス期",
    definition="ベンガル語近代詩の最高峰の一人（1899-1954）。詩集『バナラタ・セン』(1942)、『七つの星のささやき』(1948)等で、タゴール後のベンガル詩を象徴主義・モダニズムへ方向転換した。「私が再び帰ってこよう、このベンガルへ……」の有名な詩節は、ベンガル文学的アイデンティティの象徴となっている。",
    background="20世紀前半ベンガル知識人層のヨーロッパ・モダニズム受容、タゴール詩への方法的応答。",
    development="ポストコロニアル期ベンガル・バングラデシュ近代詩の規範となり、ベンガル文学の二大柱（タゴールと並ぶ）として位置づけられる。",
    historical_context="分離独立期(1947)のベンガル分割、東パキスタン・西ベンガル両地域の文学的中心性。",
    primary_source_url=WIKI_EN+"Jibanananda_Das",
    primary_source_type="Wikipedia: Jibanananda Das",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アミタヴ・ゴーシュ『闇の河』",
    name_en="Amitav Ghosh's River of Smoke trilogy",
    name_original="Sea of Poppies / River of Smoke / Flood of Fire",
    original_script="roman",
    period_key="印英文学現代期",
    definition="アミタヴ・ゴーシュ（1956-）の『アイビス三部作』（『芥子の海』2008、『煙の河』2011、『火の海』2015）。19世紀アヘン戦争前後のインド洋世界を多言語多人種多階級の視点から描く歴史小説。印英文学が「アジア間関係史」を主題化する重要な転回点となった。",
    background="ポストコロニアル印英文学の歴史化、アジア間貿易・帝国・移民史の文学的再構成。",
    development="ディアスポラ印英文学の世界文学的地位確立、英文学カノンへの統合。",
    historical_context="21世紀初頭のグローバル化批判、世界文学の主題的多元化。",
    primary_source_url=WIKI_EN+"Ibis_trilogy",
    primary_source_type="Wikipedia: Ibis trilogy (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"インド洋世界の人類学",
         "description":"ゴーシュ三部作は人類学的にインド洋世界の多文化交渉史を文学化する事例として研究される。"}])

add(**C, name_ja="キラン・デサイ『喪失の継承』",
    name_en="Kiran Desai's The Inheritance of Loss",
    name_original="The Inheritance of Loss",
    original_script="roman",
    period_key="印英文学現代期",
    definition="キラン・デサイ（1971-）の長編小説（2006年刊、ブッカー賞受賞）。1980年代後半西ベンガル・カリンポンを舞台に、引退した判事・孫娘・コック・ニューヨークの不法移民を、ゴルカ民族運動を背景に描く。グローバリゼーション下のディアスポラと帰属の喪失を主題化した21世紀印英文学の代表作。",
    background="アニタ・デサイの娘である作家の世代的継承、21世紀グローバル化下の印英文学。",
    development="ジュンパ・ラーヒリ、その他世界印僑文学の同時代的潮流の中核作品となった。",
    historical_context="2000年代の印英文学世界市場での確立、ブッカー賞による国際的承認。",
    primary_source_url=WIKI_EN+"The_Inheritance_of_Loss",
    primary_source_type="Wikipedia: The Inheritance of Loss",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジュンパ・ラーヒリ",
    name_en="Jhumpa Lahiri",
    name_original="Jhumpa Lahiri",
    original_script="roman",
    period_key="印英文学現代期",
    definition="ジュンパ・ラーヒリ（1967-、ベンガル系米国作家）。短編集『停電の夜に』(1999、ピューリッツァー賞)、長編『その名にちなんで』(2003)、『低地』(2013)で、米国移民第一・第二世代インド系の生を抑制された散文で描いた。21世紀ディアスポラ印英文学の代表作家。",
    background="米国・インド・イタリアにわたる多言語的越境的アイデンティティ、21世紀世界文学の制度的舞台。",
    development="近年のイタリア語創作転換（『別の言葉で』2015）で、世界文学における言語的越境の理論的事例となった。",
    historical_context="2000年代以降の世界文学市場におけるディアスポラ作家の確立。",
    primary_source_url=WIKI_EN+"Jhumpa_Lahiri",
    primary_source_type="Wikipedia: Jhumpa Lahiri",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アラヴィンド・アディガ『白い虎』",
    name_en="Aravind Adiga's The White Tiger",
    name_original="The White Tiger",
    original_script="roman",
    period_key="印英文学現代期",
    definition="アラヴィンド・アディガ（1974-）の長編小説（2008年刊、ブッカー賞受賞）。低カースト出身のバルラム・ハルワーイがデリーで運転手として働き、雇い主を殺害して起業家として成功する物語を、本人による中国首相宛書簡形式で描く。21世紀インドのグローバル化の暗部を諷刺する現代印英文学の代表作。",
    background="2000年代インド経済成長下の階層格差拡大、ポストコロニアル印英文学の批判的方向性。",
    development="アジア新興国の階層構造を主題化する世界文学の系列に位置づけられる。",
    historical_context="2000年代のインド「シャイニング・インディア」言説と、その文学的批判。",
    primary_source_url=WIKI_EN+"The_White_Tiger_(novel)",
    primary_source_type="Wikipedia: The White Tiger (novel)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: ダリット・分離独立・女性文学 — 7件
# ============================================================
add(**C, name_ja="ダリット自伝（マラーティー）",
    name_en="Dalit autobiography (Marathi)",
    name_original="दलित आत्मकथा",
    original_script="devanagari",
    period_key="ダリット・周縁文学期",
    definition="ダヤー・パワール『バルテ』(1978)、ラクシュマン・マネ『ウパラー』(1980)、シャラン・クマール・リンバーレ『アクラマック』(1984)等を中核とする、マハーラーシュトラ被抑圧カースト出身者による1970-80年代マラーティー語自伝群。アンベードカル思想を背景にカースト経験を一人称で語る形式で、ダリット文学の制度的中核を成した。",
    background="アンベードカル思想とダリット・パンサーズ運動(1972)、マハーラーシュトラ・ダリット文学誌『アスミタ』創刊。",
    development="他言語ダリット文学（ヒンディー、タミル、グジャラーティ等）に範型を提供し、21世紀英訳によって世界文学に登場した。",
    historical_context="1970-80年代インドの非常事態体制と、被抑圧層の文学的主体化運動。",
    primary_source_url=WIKI_EN+"Dalit_literature",
    primary_source_type="Wikipedia: Dalit literature (academic)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ダリット自伝の被抑圧者主体は、AI時代における「データから周縁化される主体」の問題と理論的に共振する。",
         "related_ai_phenomenon":"AI学習データにおける周縁化と主体化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"被抑圧者の主体的言説",
         "description":"ダリット自伝は人類学的にサバルタンの自己語りの代表的事例として研究される。"}])

add(**C, name_ja="バーマー『カルッカ』",
    name_en="Bama's Karukku",
    name_original="கருக்கு",
    original_script="tamil",
    period_key="ダリット・周縁文学期",
    definition="タミル・ダリット女性作家バーマーの自伝（1992年刊、英訳2000）。タミル・ナードゥのカトリック・ダリット女性として、カースト・宗教・性別の三重抑圧経験を口語タミルで語る。タミル・ダリット文学の代表作として、また女性ダリット主体の確立として国際的承認を得た。",
    background="1990年代タミル・ダリット運動、カトリック・ダリット社会の覚醒。",
    development="2000年英訳出版で世界文学的承認を得て、世界のサバルタン文学研究の中心テクストとなった。",
    historical_context="1990年代インドの新自由主義改革下のカースト政治再編期。",
    primary_source_url=WIKI_EN+"Bama_(author)",
    primary_source_type="Wikipedia: Bama (author)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"交差的抑圧と主体形成",
         "description":"バーマー『カルッカ』は人類学的にカースト・性別・宗教の交差的抑圧の事例として研究される。"}])

add(**C, name_ja="アムリター・プリータム",
    name_en="Amrita Pritam",
    name_original="ਅੰਮ੍ਰਿਤਾ ਪ੍ਰੀਤਮ",
    original_script="gurmukhi",
    period_key="ダリット・周縁文学期",
    definition="パンジャービー語女性作家・詩人（1919-2005）。分離独立を題材にした詩「アジ・アーカン・ワーリス・シャー・ヌーン」(1948、ワーリス・シャーへの呼びかけ)で分離独立期女性受難の象徴的詩人となった。長編『ピンジャル（骸骨）』(1950)は分離独立期に誘拐された女性の運命を描く。パンジャービー語近代女性文学の中核。",
    background="分離独立(1947)期の女性暴力、パンジャービー語近代文学運動。",
    development="サハーティヤ・アカデミー賞(1956)、ジュナーンピート賞(1981)受賞、20世紀インド女性文学の象徴的存在。",
    historical_context="1947年印パ分離期の人口移動と性暴力、その文学的記憶化。",
    primary_source_url=WIKI_EN+"Amrita_Pritam",
    primary_source_type="Wikipedia: Amrita Pritam",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クリシュナ・ソーバティー",
    name_en="Krishna Sobti",
    name_original="कृष्णा सोबती",
    original_script="devanagari",
    period_key="ダリット・周縁文学期",
    definition="ヒンディー語女性作家（1925-2019）。長編『ミトロー・マルジャーニー』(1966)、『ジンダギーナーマー』(1979)、『ディロー・ダーニシュ』(1993)で、女性的欲望・分離独立記憶・パンジャーブ-デリー文化交差を多層的なヒンディー散文で描いた。20世紀ヒンディー文学の最高峰の一人。",
    background="分離独立期の越境体験、ヒンディー語近代文学の女性的更新。",
    development="ジュナーンピート賞(2017)受賞、21世紀ヒンディー文学の制度的中心となった。",
    historical_context="1947年分離からインド独立後70年間のヒンディー語文学的記憶化過程。",
    primary_source_url=WIKI_EN+"Krishna_Sobti",
    primary_source_type="Wikipedia: Krishna Sobti",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヤシュパール『ジューター・サチ』",
    name_en="Yashpal's Jhutha Sach",
    name_original="झूठा सच",
    original_script="devanagari",
    period_key="ダリット・周縁文学期",
    definition="ヤシュパール（1903-1976）が1958-60年に発表したヒンディー語2巻長編。分離独立期ラホールの中産階級ベディー家を中心に、1947年印パ分離の混乱・暴力・女性誘拐・難民化を描く。ヒンディー語分離独立小説の最高傑作。",
    background="分離独立期の集団暴力体験、ヒンディー語進歩主義作家運動。",
    development="ヒンディー語分離独立文学の規範となり、21世紀英訳によって世界文学に再登場した。",
    historical_context="1947-48年パンジャーブ・ラホール周辺での集団殺戮と人口移動。",
    primary_source_url=WIKI_EN+"Yashpal_(author)",
    primary_source_type="Wikipedia: Yashpal",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クリシュナ・バルデーオ・ヴァイド",
    name_en="Krishna Baldev Vaid",
    name_original="कृष्ण बलदेव वैद",
    original_script="devanagari",
    period_key="ダリット・周縁文学期",
    definition="ヒンディー語実験小説作家（1927-2020）。長編『ウーシャー（夜明け）』(1957)、『ビーマル・ウルフ・ジャーエン・ハム・ジャヘナーム』(1974)、『カラー・コーラハル』(1975)、『マヤー・ローカ』(1999)で、ヒンディー語小説に意識流・断片化・形式実験を導入した。20世紀ヒンディー語ポストモダン小説の先駆者。",
    background="分離独立期の越境体験、20世紀後半のヒンディー語前衛文学運動。",
    development="ヒンディー語実験小説の系譜（ニルマル・ヴァルマー、ヴィノード・クマール・シュクラに連なる）の中核作家として位置づけられる。",
    historical_context="20世紀後半ヒンディー語文学のモダニズム・ポストモダニズム展開期。",
    primary_source_url=WIKI_EN+"Krishna_Baldev_Vaid",
    primary_source_type="Wikipedia: Krishna Baldev Vaid",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="部族（アディヴァースィー）口承文学",
    name_en="Adivasi oral literature",
    name_original="आदिवासी मौखिक साहित्य",
    original_script="devanagari",
    period_key="ダリット・周縁文学期",
    definition="サンタール、ゴーンド、ビール、ナーガ、ミーゾ等インド亜大陸の部族集団に伝わる口承文学群。神話・叙事詩・労働歌・葬送歌・恋愛歌を含み、20世紀後半以降ヴェリエル・エルウィン、G・N・デヴィー（ブッダーン・トラスト）等の収集・出版で活字化が進んだ。インド文学のサンスクリット-地域言語二項図式を超える第三の系統。",
    background="20世紀インド人類学・部族研究の発展、ポストコロニアル批評による多文化主義志向。",
    development="ハンサダー・スワーランダール、テムスラ・アオ、マムン・ダース等の部族出身作家による文学的主体化への展開。",
    historical_context="独立後インドの部族政策論議、1990年代以降の先住民権利運動。",
    primary_source_url=WIKI_EN+"Adivasi_literature",
    primary_source_type="Wikipedia: Adivasi literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"先住民口承文学",
         "description":"アディヴァースィー口承文学は人類学的に先住民知識体系の中核として研究される。"}])


# ============================================================
# E: 地域言語近現代小説 — 7件
# ============================================================
add(**C, name_ja="ハリ・ナーラーヤン・アープテー",
    name_en="Hari Narayan Apte",
    name_original="हरि नारायण आपटे",
    original_script="devanagari",
    period_key="地域言語近現代小説期",
    definition="マラーティー近代小説の祖（1864-1919）。雑誌『カランドック・ニリーキシャク』を主宰し、社会小説『パン・ラクシャート・コン・ゲートー』(1893)、歴史小説『ウシャーカール』『チャンドラグプタ』等で、マラーティー語近代小説の規範を確立した。",
    background="19世紀後半マハーラーシュトラの社会改革運動、英国小説（スコット）の翻訳的受容。",
    development="ナラヤン・S・パーンセー、V・S・カーンデーカル、後の20世紀マラーティー小説の祖型を提供した。",
    historical_context="1890年代英領インドの言語別文学制度確立期。",
    primary_source_url=WSRC_MR+"लेखक:हरि_नारायण_आपटे",
    primary_source_type="Marathi Wikisource: Hari Narayan Apte",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヴィジャイ・テンドゥルカル",
    name_en="Vijay Tendulkar",
    name_original="विजय तेंडुलकर",
    original_script="devanagari",
    period_key="地域言語近現代小説期",
    definition="マラーティー近代劇作家（1928-2008）。『シャーンタター！コールト・チャール・アーヘ』(1967、『沈黙！法廷は審理中』)、『ガッダーリー・チ・ニアタ』(1972、『ガッダリーの陰謀』)、『サカーラム・ビーンダル』(1974)で、性暴力・カースト・政治的暴力をマラーティー演劇に正面から取り込み、20世紀インド近代演劇の方法的革新を達成した。",
    background="ベンガル・ブブラトー演劇のマラーティー受容、戦後インド都市演劇の興隆。",
    development="ジュナーンピート賞(2008)受賞、21世紀インド演劇の規範となった。",
    historical_context="1960-70年代インドの政治的危機（非常事態体制1975-77等）の演劇的反映。",
    primary_source_url=WIKI_EN+"Vijay_Tendulkar",
    primary_source_type="Wikipedia: Vijay Tendulkar",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="O・V・ヴィジャヤン『カサーキンテ・イティハーサム』",
    name_en="O.V. Vijayan's Khasakkinte Itihasam",
    name_original="ഖസാക്കിന്റെ ഇതിഹാസം",
    original_script="malayalam",
    period_key="地域言語近現代小説期",
    definition="O・V・ヴィジャヤン（1930-2005）が1969年に発表したマラヤーラム語長編小説（『カサークの伝説』）。ケララ州パールカード地方の架空村カサークを舞台に、若い教師ラヴィの精神的探求と村落共同体の神話的時間を、モダニズム的散文で描く。マラヤーラム語小説の方法的転換点となった作品。",
    background="1960年代ケララのマルクス主義政治・モダニズム文学運動、ガルシア・マルケス受容前のラテンアメリカ的方法の独立的展開。",
    development="マラヤーラム語小説のモダニズム的成熟を象徴し、21世紀英訳で世界文学的承認を得た。",
    historical_context="1957年世界初の選挙によるマルクス主義政権成立(ケララ)後のケララ近代文化。",
    primary_source_url=WIKI_EN+"Khasakkinte_Itihasam",
    primary_source_type="Wikipedia: Khasakkinte Itihasam",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シヴァラーマ・カーラント",
    name_en="Shivarama Karanth",
    name_original="ಶಿವರಾಮ ಕಾರಂತ",
    original_script="kannada",
    period_key="地域言語近現代小説期",
    definition="カンナダ語百科全書的作家（1902-1997）。長編『マライェガラ・マダゲ（雨の中の子供たち）』(1968、ジュナーンピート賞)、『チョーマナ・ドゥディ（チョーマの太鼓）』(1933)等で、カルナータカ・トゥル海岸社会を多角的に描いた。長編・児童文学・科学教育・舞踊（ヤクシャガーナ）研究を含む50冊超の著作。",
    background="20世紀前半カンナダ語文学運動、民俗芸能ヤクシャガーナとの結合。",
    development="ジュナーンピート賞(1977)受賞、20世紀カンナダ語文学の代表的作家として確立。",
    historical_context="独立期から独立後のカルナータカ州地方文化の文学化。",
    primary_source_url=WIKI_EN+"Shivaram_Karanth",
    primary_source_type="Wikipedia: Shivaram Karanth",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ガールシヤ・マールケスとマラヤーラム小説",
    name_en="Marquez and Malayalam novel",
    name_original="മാർക്കേസും മലയാള നോവലും",
    original_script="malayalam",
    period_key="地域言語近現代小説期",
    definition="ガブリエル・ガルシア・マルケス『百年の孤独』(1967)のマラヤーラム語受容と、それが契機となった1980-90年代マラヤーラム語マジック・リアリズム小説運動。M・ムクンダン、アナンド、N・S・マダワン等の作品を含む。マラヤーラム語が英語以外の地域言語で初めて世界文学的潮流に直接接続した事例。",
    background="1980年代ケララ知識人層のラテンアメリカ文学受容、世界文学市場のグローバル化。",
    development="他地域言語（ベンガル、タミル、ヒンディー）のマジック・リアリズム小説の祖型となった。",
    historical_context="1980-90年代インド経済自由化期の世界文学受容拡大。",
    primary_source_url=WIKI_EN+"Malayalam_literature",
    primary_source_type="Wikipedia: Malayalam literature (academic)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="ナビプダラ・トゥップティル『ジュガリー（廃材集め）』",
    name_en="Punjabi novel of partition",
    name_original="ਪੰਜਾਬੀ ਵੰਡ ਨਾਵਲ",
    original_script="gurmukhi",
    period_key="地域言語近現代小説期",
    definition="アムリター・プリータム『ピンジャル』(1950)、グルディヤール・スィン『マルヒー・ダ・ディーヴァー』(1964)、ナーナク・スィン『カトラ・ヴィッチ・カトラ』、シヴ・クマール・バターロヴィー詩等を中核とする、パンジャービー語による分離独立体験文学群。1947年分離の集団記憶のパンジャービー語形式。",
    background="1947年分離期のパンジャーブ集団暴力経験、東西パンジャーブの言語文化的分裂。",
    development="シーク教徒・ヒンドゥー教徒・ムスリムの三重視点を保持する世界唯一の分離文学伝統となった。",
    historical_context="1947年印パ分離期の人口移動と暴力（パンジャーブ地方が最大被害地）。",
    primary_source_url=WSRC_PA,
    primary_source_type="Punjabi Wikisource: partition novels",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="U・R・アナンタムールティ『バーラティープラ』",
    name_en="Anantamurthy's Bharatipura",
    name_original="ಭಾರತೀಪುರ",
    original_script="kannada",
    period_key="地域言語近現代小説期",
    definition="U・R・アナンタムールティ（1932-2014）が1973年に発表したカンナダ語長編。英国留学帰りの主人公ジャガンナータが故郷の村寺院に被差別カーストを入場させようとする企てを軸に、伝統と近代の葛藤を描く。アナンタムールティ『サンスカーラ』(1965)に続く代表作。",
    background="1960-70年代カルナータカのカースト改革論議、ナヴャ（新派）カンナダ運動。",
    development="ナヴャ運動の中核作品となり、20世紀後半カンナダ近代小説の規範となった。",
    historical_context="1960-70年代インドの社会改革論議、地方寺院の社会的地位再編期。",
    primary_source_url=WIKI_EN+"Bharathipura",
    primary_source_type="Wikipedia: Bharathipura",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F: 口承叙事詩・映画脚本・新詩学 — 6件
# ============================================================
add(**C, name_ja="パーブージー口承叙事詩",
    name_en="Pabuji oral epic",
    name_original="पाबूजी की फड़",
    original_script="devanagari",
    period_key="インド口承叙事詩・大衆文化期",
    definition="ラージャスターン州の14世紀ラージプート英雄パーブージーを主人公とする口承叙事詩。ボーパー（職業歌い手）が「フォール（巻物絵画）」を背景に夜通し朗唱する形式で伝承される。ジョン・スミス『パーブージーの叙事詩』(1991)で英語学術界に紹介された、世界口承叙事詩研究の重要事例。",
    background="14世紀ラージャスターンの英雄崇拝、ラージプート社会の口承伝統。",
    development="20世紀末以降の口承叙事詩研究（ロード、パリー流派の応用）の中核対象となり、無形文化遺産保護論議の対象。",
    historical_context="14世紀ラージプート王権興隆期、地方英雄崇拝の制度化。",
    primary_source_url=WIKI_EN+"Pabuji",
    primary_source_type="Wikipedia: Pabuji (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"口承叙事詩演奏",
         "description":"パーブージー叙事詩は人類学的に口承叙事詩演奏の典型事例として研究される。"}])

add(**C, name_ja="アールハ・カンド",
    name_en="Alha-Khand",
    name_original="आल्हा-खण्ड",
    original_script="devanagari",
    period_key="インド口承叙事詩・大衆文化期",
    definition="北インド・ブンデルカンド地方の口承叙事詩。12世紀後半のチャンデーラ朝勇者アールハとウーダルの兄弟英雄物語を歌う。雨期に儀礼的に歌われ、北インド民衆の英雄物語伝統の最大傑作。19世紀チャールズ・エリオット卿による文字化、現代まで活発な歌唱伝統が継続している。",
    background="12世紀後半デリー・スルタン朝侵入期の北インド地方王権抵抗、英雄崇拝の口承化。",
    development="19世紀以降の文字化を経て、現代北インド民衆文化の中核口承資源となった。",
    historical_context="12世紀末ムハンマド・ゴール侵入期の北インド政治変動。",
    primary_source_url=WIKI_EN+"Alha",
    primary_source_type="Wikipedia: Alha (academic)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ボリウッド脚本としての文学",
    name_en="Bollywood screenplay as literature",
    name_original="हिन्दी सिनेमा पटकथा",
    original_script="devanagari",
    period_key="インド口承叙事詩・大衆文化期",
    definition="サリム・ハーン-ジャーヴェード・アクタル『ザンジール』(1973)、『シャーレ』(1975)、『ディーワール』(1975)以降の、ヒンディー語映画脚本を文学形式として捉える研究的視座。台詞・物語構造・歌詞の文学的研究は、20世紀後半インド文学研究の制度的拡張として展開した。",
    background="1970年代ヒンディー語映画の脚本書き手の文学的地位確立、大衆文化研究の興隆。",
    development="21世紀ボリウッド研究、映画文学批評の中核対象となった。",
    historical_context="1970年代インド非常事態体制期の社会的怒りを映画化したアクション・メロドラマの興隆期。",
    primary_source_url=WIKI_EN+"Salim%E2%80%93Javed",
    primary_source_type="Wikipedia: Salim-Javed",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"映画脚本の集団的作者性は、AI生成文学の集団的・分散的作者性の祖型として再読できる。",
         "related_ai_phenomenon":"AI生成と集団的作者性"}])

add(**C, name_ja="ウルドゥー・ナズム（近代詩形式）",
    name_en="Urdu nazm (modern poem)",
    name_original="نظم",
    original_script="urdu",
    period_key="インド口承叙事詩・大衆文化期",
    definition="19世紀末アルターフ・フセイン・ハーリーが提唱した、伝統ガザル形式と異なる主題的統一を持つ近代ウルドゥー詩形式。アッラーマ・イクバール、サーヒル・ルディヤーンヴィー、ファイズ・アフマド・ファイズ等の作品で確立し、20世紀ウルドゥー詩の主要形式となった。社会・政治・歴史を主題化する近代ウルドゥー詩の核。",
    background="19世紀末ウルドゥー文学近代化運動、英国浪漫詩の影響受容。",
    development="20世紀インド・パキスタン両国のウルドゥー社会主義詩・現代詩の規範形式となった。",
    historical_context="ハーリー『ムサッダス』(1879)以降のウルドゥー文学制度的近代化期。",
    primary_source_url=WIKI_EN+"Nazm",
    primary_source_type="Wikipedia: Nazm (Urdu)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"近代詩形式",
         "description":"ナズムはウルドゥー文学詩学における近代詩形式の中核範疇であり、ガザル詩学との対比軸を成す。"}])

add(**C, name_ja="A・K・ラマヌジャン詩学",
    name_en="A.K. Ramanujan's poetics",
    name_original="A.K. Ramanujan",
    original_script="roman",
    period_key="インド口承叙事詩・大衆文化期",
    definition="A・K・ラマヌジャン（1929-1993）の詩学的著作群。古典タミル詩英訳『The Interior Landscape』(1967)、エッセイ『Is There an Indian Way of Thinking?』(1989)、『Three Hundred Ramayanas』(1991)で、インド古典詩学の英語圏比較詩学への翻訳的紹介と、インド思想の多元性論を展開した。21世紀世界比較詩学の中核的参照点。",
    background="シカゴ大学南アジア研究の制度的成熟、英語圏インド研究の世界的影響力。",
    development="21世紀世界比較詩学・ポストコロニアル批評の中核的参照点となり、ラーマーヤナ300種研究は教科書配布禁止論争(2011)を引き起こした。",
    historical_context="1990年代以降のインド古典学の世界的英語学術化。",
    primary_source_url=WIKI_EN+"A._K._Ramanujan",
    primary_source_type="Wikipedia: A.K. Ramanujan",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"インド比較詩学",
         "description":"ラマヌジャン詩学はインド古典詩学を世界比較詩学の中に位置づける制度的中核。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"インド思想の多元性",
         "description":"ラマヌジャンの『Indian Way of Thinking』論はインド思想の多元論的解釈の参照点。"}])

add(**C, name_ja="ガネーシュ・デヴィー『脱マイナー化文学論』",
    name_en="G.N. Devy's Of Many Heroes / Bhasha Movement",
    name_original="G.N. Devy",
    original_script="roman",
    period_key="インド口承叙事詩・大衆文化期",
    definition="ガネーシュ・デヴィー（1950-）の批評著作および「ブハーシャー・センター」(1996設立)による地域言語・部族言語文学の制度的承認運動。著作『After Amnesia』(1992)、『Of Many Heroes』(1998)、『The G.N. Devy Reader』(2009)で、英印文学中心主義への批判と、消滅言語文学の救出論を展開した。21世紀インド多言語文学論の中核。",
    background="1990年代インド経済自由化下の英語文学化への批判的応答、ユネスコ無形文化遺産論議の影響。",
    development="People's Linguistic Survey of India(2010-13、780言語調査)、消滅言語文学保護運動の制度化。",
    historical_context="1990年代以降のインド言語政策論議、グローバル化下の地域言語危機。",
    primary_source_url=WIKI_EN+"Ganesh_Devy",
    primary_source_type="Wikipedia: Ganesh Devy",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"デヴィーの言語多元論は、AI時代における低リソース言語消滅・データ支配的英語化と直接的に対峙する理論。",
         "related_ai_phenomenon":"AI低リソース言語の消滅と保全論"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"言語多様性と文化保全",
         "description":"デヴィー運動は人類学的に言語多様性保全と先住民権利論の実践的事例として研究される。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    skipped: list[str] = []
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="南アジア",
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
                print(f"  [skip] {entry['name_ja']}: {e}")
                skipped.append(entry['name_ja'])
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
        print(f"[c20-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c20-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        if skipped:
            print(f"[c20-add40] skipped duplicates ({len(skipped)}): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
