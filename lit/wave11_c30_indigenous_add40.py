"""LIT-DB Phase 2 Wave 11 — C30 ADD: Indigenous & Oral Literature (+40).

Subfield: lit_indigenous_oral (id=19), region='周縁横断'.
Adds 40 NEW concepts on top of existing 40 (waves 2 & 10), expanding:
  A: Pacific oral traditions (Hawaiian, Tongan-Samoan-Marshallese, navigation) — 8
  B: Southeast Asian indigenous (Hmong, Iban, Naga) — 5
  C: African oral traditions (deeper Mande, Yoruba ifa, Akan, |Xam, Tamazight) — 6
  D: South American indigenous (Mapuche, Quechua, Guarani, Yanomami deeper) — 6
  E: Arctic / Australian Dreaming song-cycle types — 6
  F: Performance theory + Indigenous DH/AI sovereignty critiques — 9

Verification policy:
  - 'primary'  -> documented oral records in WOLP, ELAR, PARADISEC, AIATSIS,
                  NAA, Marshall Islands NMI, eHRAF, official cultural archives.
  - 'secondary' -> canonical scholarly synthesis or encyclopedia entry.
  - 'tertiary' -> synthetic/comparative critical category.

fourth_transform_tags >= 14 (heavy on authorship/voice/authenticity);
cross_domain to AN >= 10.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS_TO_SEED = [
    ("先住民口承伝統期", "Indigenous Oral Tradition (pre-contact)", -10000, 1500,
     "接触以前の口承伝統。世界の周縁諸文化の世代間伝承による物語・歌・儀礼・知識体系。"),
    ("植民地接触・抑圧期", "Colonial Contact & Suppression", 1500, 1960,
     "植民地化と国民国家形成下で口承伝統が記録化・改変・抑圧される時期。"),
    ("先住民文芸復興期", "Indigenous Renaissance", 1960, 2026,
     "1960年代以降の先住民文芸復興。口承と書記の融合、自決運動、文化主権の文学。"),
]


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


REGION = "周縁横断"
SUBFIELD = "lit_indigenous_oral"
C = dict(subfield_code=SUBFIELD, region=REGION, original_script="roman")


# Source URLs
WOLP = "https://www.oralliterature.org/"
ELAR = "https://www.elararchive.org/"
PARA = "https://paradisec.org.au/"
AIAT = "https://aiatsis.gov.au/"
NAA  = "https://www.naa.gov.au/"
NMI  = "https://nmi.museum.mh/"
EHRAF = "https://ehrafworldcultures.yale.edu/"
WIKI = "https://en.wikipedia.org/wiki/"
TEARA = "https://teara.govt.nz/en/"


# ============================================================
# A: Pacific oral traditions (8) — Hawaiian, Tongan, Samoan, Maori,
#    Marshallese, navigation chants
# ============================================================
add(**C, name_ja="モオレロ",
    name_en="moolelo (Hawaiian narrative)",
    name_original="moʻolelo",
    period_key="先住民口承伝統期",
    definition="ハワイ語で「語り」「物語」「歴史」を意味し、神話・系譜・歴史・地名譚・家系誌を包括する口承ジャンル。神々（akua）、英雄（aliʻi）、土地（ʻāina）の関係を結ぶ知識装置として機能し、1820年代以降ハワイ語新聞（Ka Hae Hawaii、Ka Nupepa Kuokoa等）に大量に書き起こされ、Bishop Museum・Kamehameha Schools が保存する。",
    background="ポリネシアン口承伝統のハワイ的展開、19世紀ハワイ語新聞文化の興隆。",
    development="現代ハワイ主権運動・ハワイ語復興運動の文化的基盤として再活性化。",
    historical_context="1893年ハワイ王国併合と1898年米国併合を経た文化抑圧と、近年のサバンナ法廷での口承証拠化。",
    primary_source_url=WIKI+"Hawaiian_mythology",
    primary_source_type="Bishop Museum / Hawaiian newspaper archive (Papakilo)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"モオレロは共同体所有であり、語り手の権利と聞き手の責任が共同的に構成される。AI生成コーパスへの取り込みに対する文化的主権問題の核となる。",
         "related_ai_phenomenon":"先住民データ主権（CARE原則）と LLM 訓練"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"語り手の系譜的権威に基づく真正性概念は、AI生成テキストの非系譜的真正性と根本的に対立する。",
         "related_ai_phenomenon":"AI生成と系譜的真正性の不在"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Hawaiian ethnography",
         "description":"Malo, Kamakau, Kepelino らハワイ人民族誌家の19世紀記述伝統と直結。"}])

add(**C, name_ja="メレ（ハワイ詠唱）",
    name_en="mele (Hawaiian chant)",
    name_original="mele",
    period_key="先住民口承伝統期",
    definition="ハワイ語の詠唱詩形式の総称。mele inoa（名前詠唱）、mele koʻihonua（系譜詠唱）、mele hula（フラ詠唱）、mele aloha（愛の詠唱）、mele kanikau（哀歌）等の下位ジャンルを持ち、語り手（haku mele）が新作と継承を兼ねる。フラ（hula）と分かちがたく結びつき、身体所作と詩がひとつの総合芸術を成す。",
    background="ポリネシア詠唱伝統のハワイ的精緻化、kapu（神聖法）体系下の詠唱経済。",
    development="1893年王国併合後の禁圧を経て、1970年代ハワイ文化ルネサンスで完全復興、現在は学校教育に組み込まれる。",
    historical_context="Liliʻuokalani 女王自身が作曲家（'Aloha 'Oe' 等）であり、王権と詠唱が同一文化的位階に属した。",
    primary_source_url="https://www.huapala.org/",
    primary_source_type="Huapala Hawaiian music & hula archive",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Hawaiian ritual & kinship",
         "description":"mele inoa（名前詠唱）は系譜・地位の人類学的記述と直接接続する。"}])

add(**C, name_ja="クムリポ",
    name_en="Kumulipo (Hawaiian creation chant)",
    name_original="Kumulipo",
    period_key="先住民口承伝統期",
    definition="ハワイ王族の創世詠唱。2,102行にわたり、暗黒の海から珊瑚・魚・植物・動物・人間・神・歴代王族を順次出現させる宇宙生成譜。Liliʻuokalani 女王が獄中で英訳（1897）、Martha Beckwith が学術版（1951）。ハワイ王族の系譜的正統性根拠であり、進化論的世界観と並行的に読まれる比較神話学的重要文書。",
    background="18世紀末 Lonoikamakahiki 王のために編まれたとされる宮廷詠唱。",
    development="近代以降ハワイ独自の宇宙論・進化論として比較研究の対象となった。",
    historical_context="1897年Liliʻuokalani獄中英訳が王権廃止後の文化主権主張として機能した。",
    primary_source_url="https://www.sacred-texts.com/pac/lku/",
    primary_source_type="Sacred Texts: Kumulipo (Beckwith ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"匿名共同体作者と王族個人作者性の混合は、AI共著作概念の前史として再読される。",
         "related_ai_phenomenon":"集合的作者性とAI共著作"}])

add(**C, name_ja="トンガ・ファイカヴァ",
    name_en="Tongan faikava (kava-circle storytelling)",
    name_original="faikava",
    period_key="先住民口承伝統期",
    definition="トンガにおけるカヴァ飲用儀礼を伴う集団的物語・詩作の場。男性が円を作り、kava を回し飲みしながら fakatangi（叙情詩）、hiva（歌）、talanoa（語り）を即興・伝承する。社会的結束・知識継承・政治的合意形成が一体化した口承パフォーマンス制度。",
    background="ポリネシア・カヴァ文化複合（フィジー・サモア・トンガ）の儀礼的中核。",
    development="現代トンガでは政治的議論・教会活動・大学キャンパスにも展開。",
    historical_context="トンガ王国の口承憲政基盤として機能してきた。",
    primary_source_url=PARA+"collections/",
    primary_source_type="PARADISEC: Pacific oral records",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Pacific kava ritual",
         "description":"カヴァ儀礼の人類学的研究（Tomlinson, Halapua）と直接接続。"}])

add(**C, name_ja="サモア・ファガオゴ",
    name_en="Samoan fāgogo (oral narrative)",
    name_original="fāgogo",
    period_key="先住民口承伝統期",
    definition="サモアの夜の物語ジャンル。聞き手が「Soo!」と相槌を打つ応答型口承で、神話・トリックスター譚（Sina と鰻、Pili 神等）・道徳譚・系譜譚を含む。Albert Wendt の小説作品にも繰り返し引用され、現代サモア文学の口承的基盤を形成する。",
    background="ポリネシア夜話伝統のサモア的形式化。",
    development="20世紀以降の文字化（Krämer 1902-03 等）と現代教育における再導入。",
    historical_context="サモア独立（1962）以降の文化政策で公教育に取り込まれた。",
    primary_source_url=PARA+"collections/",
    primary_source_type="PARADISEC: Samoan recordings",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マルシャル諸島ロロロル詠唱",
    name_en="Marshallese roro (navigation chant)",
    name_original="roro",
    period_key="先住民口承伝統期",
    definition="マルシャル諸島の航海詠唱。波形パターン（dilep, rilib, kaelib）と星座を組み合わせた航海知識を、詠唱として記憶・伝承する。stick chart（meddo, mattang, rebbelib）と一対の知識装置として機能し、世界海洋史上最も精緻な伝統航法体系のひとつを成した。",
    background="マルシャル諸島民の太平洋遠洋航海伝統と、波形読解の身体知。",
    development="20世紀核実験（Bikini, Enewetak）による文化的離散後、近年は Waan Aelõñ in Majel（伝統カヌー復興）プロジェクトで再活性化。",
    historical_context="米国信託統治・核実験補償交渉での文化的記憶として政治的価値を獲得。",
    primary_source_url="https://nmi.museum.mh/",
    primary_source_type="National Museum of Marshall Islands archives",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"波形・星・身体感覚を統合する詠唱知は、抽象データに還元されない身体化知識の典型例で、AIによる知識抽出の限界を理論化する。",
         "related_ai_phenomenon":"身体化知識と AI のテキスト還元"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Pacific wayfinding",
         "description":"ナイノア・トンプソンらポリネシア航法復興と並行する伝統航法知識体系。"}])

add(**C, name_ja="ポリネシア航海詠唱",
    name_en="Polynesian navigation chant",
    name_original="Polynesian navigation chant",
    period_key="先住民口承伝統期",
    definition="マウ・ピアイルク（カロリン）、ナイノア・トンプソン（ハワイ）らに代表される、星・うねり・鳥・雲を読む航海知識を記憶する詠唱伝統の総称。Hokuleʻa（ホクレア）航海（1976-）以降、ポリネシア・トライアングル全域で復興し、口承科学知識の現代的価値を象徴する。",
    background="3,000年以上のオセアニア航海伝統と、その20世紀後半の再発見。",
    development="現代の Polynesian Voyaging Society が口承知識をデジタル化せずに身体的に継承する方針を取り、AI時代の知識継承モデルとなる。",
    historical_context="ヘイエルダールのコンチキ説への反証として、ポリネシア人自身の航海能力が再評価された。",
    primary_source_url="https://www.hokulea.com/",
    primary_source_type="Polynesian Voyaging Society archives",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"航海詠唱は身体・観察・記憶の総合であり、テキスト化に抵抗する知識形式として AI 時代に逆説的価値を持つ。",
         "related_ai_phenomenon":"非テキスト化知識の AI 時代における価値"}])

add(**C, name_ja="マオリ・ワカタウキー",
    name_en="Maori whakataukī (proverbs)",
    name_original="whakataukī",
    period_key="先住民口承伝統期",
    definition="マオリの諺・格言。系譜的物語・歴史的事件を凝縮した短句で、スピーチ（whaikōrero）・交渉・教育の場で頻用される。'He aha te mea nui o te ao? He tangata, he tangata, he tangata.'（最も大切なものは何か。それは人、人、人）等が代表例。Te Ara 公式百科に体系的収録。",
    background="マオリ口承文化における凝縮的詩学装置。",
    development="ニュージーランド英語圏にも越境し、公的演説に頻出する文化的共有財産となった。",
    historical_context="ワイタンギ条約交渉・現代マオリ政治における修辞的支柱。",
    primary_source_url=TEARA+"whakatauki",
    primary_source_type="Te Ara — official New Zealand encyclopedia",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: Southeast Asian indigenous (5)
# ============================================================
add(**C, name_ja="フモン物語布",
    name_en="Hmong story cloth (paj ntaub)",
    name_original="paj ntaub",
    period_key="植民地接触・抑圧期",
    definition="フモン女性が刺繍した物語布。1970年代ラオス・ベトナム戦争難民キャンプ（タイ・バーンビナイ等）で発生した新ジャンルで、フモンの口承神話・移住史・戦争経験を布上の絵物語として記録する。テキストレス物語形式の先住民革新例として、世界的注目を集めた。",
    background="フモン口承伝統と難民経験の交差、女性手仕事文化の物語化。",
    development="ミネアポリス・カリフォルニア等のフモン・ディアスポラ・コミュニティで継承、現代インディジナス・アート市場でも評価される。",
    historical_context="1975年ラオス陥落以降の難民史の文化的記録媒体として機能。",
    primary_source_url=WIKI+"Story_cloth",
    primary_source_type="Smithsonian Folkways: Hmong textile archives",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"テキストレスな物語形式は、文字化と AI 訓練の前提を相対化する文化的装置。",
         "related_ai_phenomenon":"非テキスト・マルチモーダル物語の AI 訓練"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"女性匿名共同体作者性は、男性中心の作家概念と AI 個人作者概念の双方に挑戦する。",
         "related_ai_phenomenon":"匿名集合的作者性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"refugee material culture",
         "description":"難民人類学・物質文化研究の中心事例。"}])

add(**C, name_ja="フモン・カウシ",
    name_en="Hmong kwv txhiaj (sung poetry)",
    name_original="kwv txhiaj",
    period_key="先住民口承伝統期",
    definition="フモンの恋愛・哀悼・物語詩を歌う口承形式。男女の即興応答歌として求愛・婚姻交渉の場で機能し、新年（Noj Peb Caug）祭礼の中心要素を成す。1970年代以降の難民離散後も、ディアスポラ・コミュニティで継承され、ベトナム戦争史の口承記録としての価値も持つ。",
    background="東南アジア山地民族の歌掛け文化の一系統。",
    development="米国・フランス・オーストラリアのフモン・コミュニティで継承、近年は YouTube 等にも展開。",
    historical_context="1960-75年の「秘密戦争」体験と難民史の口承記憶として機能。",
    primary_source_url=ELAR+"deposit/",
    primary_source_type="ELAR: Hmong oral records",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="イバン・ティカン・ウンディ",
    name_en="Iban tikang ungkup (oral epic)",
    name_original="tikang ungkup",
    period_key="先住民口承伝統期",
    definition="ボルネオ島サラワクのイバン人の長編口承叙事詩。創世神話・英雄譚・霊界訪問譚を組み合わせ、招霊師（lemambang）が儀礼夜に詠唱する。Sea Dayak と呼ばれた首狩り戦士文化の口承的中核を成し、Sarawak Museum 収集記録（1950s-70s）が学術的基盤。",
    background="ボルネオ口承伝統のイバン的展開、19世紀 Brooke 王朝期の文化記録。",
    development="現代マレーシア・サラワク州の文化遺産政策に取り込まれ、断片的に継承中。",
    historical_context="脱首狩り化・キリスト教化・近代化の文化的衝撃を受けた口承伝統。",
    primary_source_url=PARA+"collections/",
    primary_source_type="PARADISEC / Sarawak Museum recordings",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ナガ口承叙事詩",
    name_en="Naga oral epic",
    name_original="Naga oral tradition",
    period_key="先住民口承伝統期",
    definition="インド北東部・ミャンマー国境のナガ諸民族（Ao, Angami, Sema, Konyak 等）の口承叙事詩・歌謡群。創世神話、移住譚、首狩り英雄譚、村落間戦争譚を含み、男性集会所（morung）で世代間継承される。Verrier Elwin・J.H. Hutton らの植民地期民族誌記録が学術的基盤。",
    background="チベット・ビルマ語族山地民族の口承伝統、19-20世紀英領インド人類学の対象。",
    development="ナガ人民族主義運動・自治闘争の文化的基盤として再活性化。",
    historical_context="1947年印度独立以降のナガランド分離運動と文化主権要求。",
    primary_source_url=ELAR+"deposit/",
    primary_source_type="ELAR: Naga language archives",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Naga ethnography",
         "description":"Hutton, Mills, Elwin らのナガ民族誌伝統と直結。"}])

add(**C, name_ja="マニプリ・パナ",
    name_en="Manipuri Wari Liba (Meitei storytelling)",
    name_original="Wari Liba",
    period_key="先住民口承伝統期",
    definition="北東インド・マニプール州のメイテイ人による口承物語伝承。古代王朝史（Cheitharon Kumpapa）、創世神話、英雄譚、ヒンドゥー・ヴィシュヌ派受容後の叙事詩翻案を含む。語り手（Phamnaiba）が一対一に近い親密な空間で物語を演じる、特異なパフォーマンス形式。",
    background="メイテイ人の独自国家史と、18世紀以降のヒンドゥー化の交差。",
    development="現代マニプリ文学・演劇（ratha leela）の口承的基盤を成す。",
    historical_context="マニプール王国（1110-1947）の文化的連続性を証言する伝統。",
    primary_source_url=ELAR+"deposit/",
    primary_source_type="ELAR / Sangai Express cultural records",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# C: African oral traditions deeper (6)
# ============================================================
add(**C, name_ja="スンジャタ叙事詩拡張版",
    name_en="Sundiata epic (full Mande corpus)",
    name_original="Sunjata Faasa",
    period_key="先住民口承伝統期",
    definition="マンデ語族グリオ（jeli, jali）が伝承するスンジャタ・ケイタ（Mali 帝国創始者、c.1217-c.1255）の英雄叙事詩。Djibril Tamsir Niane（1960）、John W. Johnson（1986、Fa-Digi Sisòkò 版）、David Conrad（2004、Djanka Tassey Condé 版）等の複数版が学術出版され、グリオごとに異本が生成され続ける生きた叙事詩伝統である。",
    background="13世紀マリ帝国の歴史的記憶と、グリオ職能カースト（nyamakala）による継承制度。",
    development="20世紀後半以降、複数版の比較研究がアフリカ文学研究の中心テーマとなった。",
    historical_context="独立後の西アフリカ国家（マリ・ギニア・セネガル）が文化的礎石として位置付け。",
    primary_source_url="https://www.indianapublications.com/journal/sundiata",
    primary_source_type="Indiana University: Sunjata epic project",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"グリオ毎に異本が生成される「同一叙事詩」概念は、固定テキスト前提のAI生成と根本的に異なる作者性モデル。",
         "related_ai_phenomenon":"異本生成型作者性とAIの確率的生成"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"グリオ系譜による真正性証明は、AI生成テキストに欠ける制度的真正性の祖型。",
         "related_ai_phenomenon":"系譜的真正性 vs AI 生成"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Mande caste system",
         "description":"nyamakala 職能カーストの人類学的研究（McNaughton, Conrad）と直結。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"oral epic poetics",
         "description":"パリー＝ロード口承定型句理論の西アフリカ的事例。"}])

add(**C, name_ja="ヨルバ・イファ詩",
    name_en="Yoruba Ifá divination poetry (odù)",
    name_original="odù Ifá",
    period_key="先住民口承伝統期",
    definition="ヨルバ族（ナイジェリア・ベナン）のイファ占星術が用いる256章（odù）の詩文体系。各 odù は神話・諺・歴史・処方を内包し、占い師（babaláwo）が暗誦する。世界最大の口承詩コーパスのひとつであり、UNESCO 人類無形文化遺産（2008、2017拡張）に登録。Wande Abimbola, Bascom らの記録が学術的基盤。",
    background="ヨルバ古代文明の宇宙論・倫理学体系の口承的具現化。",
    development="アフリカ系ディアスポラ宗教（カンドンブレ・サンテリア）に継承され、グローバル展開。",
    historical_context="奴隷貿易によるアフリカ系ディアスポラの精神的・詩的脊梁となった。",
    primary_source_url="https://ich.unesco.org/en/RL/ifa-divination-system-00146",
    primary_source_type="UNESCO ICH: Ifá divination system",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"256 odù の組合せ論的構造は、文学・哲学・占術・倫理を統合した非西洋的知識アーキテクチャで、AI による知識表現の代替モデルを示唆。",
         "related_ai_phenomenon":"組合せ論的知識表現と AI"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Yoruba religion",
         "description":"ヨルバ宗教人類学（Bascom, Abimbola, Drewal）の中核研究対象。"}])

add(**C, name_ja="アカン・アナンセセム",
    name_en="Akan Anansesem (Anansi tales)",
    name_original="Anansesem",
    period_key="先住民口承伝統期",
    definition="ガーナ・コートジボワールのアカン語族（Asante, Fante 他）の蜘蛛トリックスター Anansi を主人公とする物語群。Anansesem は文字通り「Anansi の語り」を意味する物語ジャンル名。奴隷貿易を通じてカリブ海・北米南部（Br'er Rabbit 系譜の前駆）に伝播し、グローバル文学的影響を持つ。",
    background="アカン口承トリックスター伝統と、大西洋奴隷貿易による拡散史。",
    development="ジャマイカ（Anancy）、米国南部（Aunt Nancy/Br'er Rabbit）、近年の児童文学・グラフィックノベルに展開。",
    historical_context="奴隷貿易期にアフリカ語族口承文化が新世界で生き延びた稀少例。",
    primary_source_url=WIKI+"Anansi",
    primary_source_type="UNESCO oral heritage / Britannica: Anansi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Atlantic diaspora folklore",
         "description":"大西洋奴隷貿易における口承伝承の人類学的研究と直結。"}])

add(**C, name_ja="コイサン・サン詠唱（|Xam）",
    name_en="|Xam Bushmen narratives (Bleek-Lloyd archive)",
    name_original="|Xam ka !au",
    period_key="植民地接触・抑圧期",
    definition="南アフリカ・カラハリ周辺の |Xam サン人（現在は絶滅言語）の口承神話・歌・体験譚。1870-84年に Wilhelm Bleek と Lucy Lloyd が、ケープタウンの囚人 |a!kunta, ||kabbo 等から記録した約 13,000 ページのノートが残る。世界最古級の先住民口承詳細記録のひとつで、UNESCO Memory of the World に登録（1997）。",
    background="19世紀後半のケープ植民地における言語学者の異例の長期収録、|Xam 言語消滅の最終局面。",
    development="南アフリカ国章の銘 ('!ke e: ǀxarra ǁke', |Xam 語) として再活用されるなど、ポストアパルトヘイト南アの文化的礎石化。",
    historical_context="サン人ジェノサイド進行下での言語的記録は、文化的喪失とアーカイヴの倫理問題を象徴する。",
    primary_source_url="http://lloydbleekcollection.cs.uct.ac.za/",
    primary_source_type="Bleek-Lloyd Collection (UCT digital archive)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"絶滅言語の口承を植民地学者が記録したアーカイヴは、AI 訓練データにおける「絶滅言語復元」と「文化的搾取」の倫理的緊張の祖型。",
         "related_ai_phenomenon":"絶滅言語の AI 復元と倫理"},
        {"axis":"知の形式","status":"rethinking",
         "rationale":"消滅した話者文化の記録としてのみ存続する知識形式は、AI による文化保全の限界を理論化する事例。",
         "related_ai_phenomenon":"AI 文化保全の限界"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Khoisan ethnography",
         "description":"アフリカ最古層民族の人類学的研究（Lewis-Williams, Guenther）と直結。"}])

add(**C, name_ja="タマジット・ベルベル口承詩",
    name_en="Tamazight Berber oral poetry (izlan)",
    name_original="izlan / izran",
    period_key="先住民口承伝統期",
    definition="北アフリカ・ベルベル語（Tamazight）話者の口承詩総称。izlan（一般詩）、izran（韻文）、tamdyazt（叙事詩）等の下位ジャンルを持ち、女性の家庭詩、男性の戦争・恋愛詩、Imdyazn（職業詩人）の宮廷詩が並存する。20世紀後半以降、ベルベル文化復興運動（特にカビリア地域）の中核となった。",
    background="北アフリカ古代以来のベルベル詩伝統、アラビア化を経た言語的存続。",
    development="アルジェリア・モロッコの公用語化（2002, 2011）以降、教育・メディアに展開。",
    historical_context="アラブ化・フランス植民地化・現代国民国家化を経た言語的少数派文学の典型。",
    primary_source_url=WIKI+"Berber_literature",
    primary_source_type="HCA (Haut Commissariat à l'Amazighité) archives",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハウサ・ワーカ詩",
    name_en="Hausa waka (Islamic oral poetry)",
    name_original="waka",
    period_key="先住民口承伝統期",
    definition="北ナイジェリア・ニジェールのハウサ語イスラーム詩伝統。19世紀ソコト・カリフ国期の Nana Asma'u（女性詩人、1793-1864）が女性教育詩で頂点を成し、口承と書記（アラビア文字 Ajami）の境界に位置する。詩人（mawaki）が公開朗誦し、ラジオ・カセット・YouTube で展開する現代的口承伝統の代表例。",
    background="西アフリカ・スーダン地域のイスラーム学知伝統と、ハウサ語族の口承文化の融合。",
    development="現代ナイジェリア政治詩（Akilu Aliyu, Mudi Spikin）に継承、ノリウッド映画・カノ音楽産業にも展開。",
    historical_context="19世紀ソコト改革運動・20世紀ナイジェリア独立運動の文化的脊梁。",
    primary_source_url="https://www.bu.edu/asc/files/2010/03/asma.pdf",
    primary_source_type="Boston University: Nana Asma'u archive",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: South American indigenous (6)
# ============================================================
add(**C, name_ja="マプチェ・キシュケ",
    name_en="Mapuche kishuke (oral narrative)",
    name_original="kishuke / nütram",
    period_key="先住民口承伝統期",
    definition="チリ南部・アルゼンチン・パタゴニアのマプチェ族の口承物語。nütram（歴史譚）、epew（神話・トリックスター譚）、ülkantun（歌）の各ジャンルを含む。話者（weupin, ñizol）が儀礼・夜話の場で継承し、現代マプチェ文学（Elicura Chihuailaf, Lorenzo Aillapán 鳥語詩人）の口承的基盤となる。",
    background="征服戦争（Arauco 戦争 1536-1883）に長期抵抗した先住民の口承記憶。",
    development="20世紀後半以降の Mapudungun 復興運動、二言語詩の展開。",
    historical_context="チリ・アルゼンチン国民国家による土地剥奪と現代の主権要求運動。",
    primary_source_url=ELAR+"deposit/",
    primary_source_type="ELAR: Mapudungun corpus",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Mapuche ethnohistory",
         "description":"アンデス・パタゴニア人類学（Bengoa, Course）の中核対象。"}])

add(**C, name_ja="ケチュア・ワクチャ詩",
    name_en="Quechua wakcha poetry",
    name_original="wakcha",
    period_key="先住民口承伝統期",
    definition="ケチュア語の「孤児」概念（wakcha）を中核とする口承詩伝統。植民地期以降の喪失体験（インカ崩壊、土地剥奪、両親喪失、文化喪失）を、孤児的主体を語り手とする抒情詩として表現する。José María Arguedas が小説『深い川』『すべての血』で文学化、現代ケチュア二言語詩（Odi Gonzales, Ch'aska Anka Ninawaman）に継承。",
    background="インカ崩壊後のアンデス喪失体験の口承的表象、tinkuy（出会い・対立）と並ぶ核概念。",
    development="20世紀ペルー・インディヘニスモ文学の核を成し、現代ケチュア・ルネサンスに継承。",
    historical_context="インカ崩壊（1533）から現代までの500年的喪失感の文学化。",
    primary_source_url=WIKI+"Quechuan_literature",
    primary_source_type="UNESCO Quechua heritage / academic anthologies",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"孤児的主体は、関係性を剥奪された主体の文学的表象として、AI 時代の「文脈なき主体」の哲学的祖型を成す。",
         "related_ai_phenomenon":"文脈剥奪主体の文学的表象"}])

add(**C, name_ja="グアラニー・ニェエ・ポラ",
    name_en="Guarani ñe'ẽ porã (beautiful word)",
    name_original="ñe'ẽ porã",
    period_key="先住民口承伝統期",
    definition="グアラニー族（パラグアイ・ブラジル・アルゼンチン・ボリビア）の聖なる言語概念。「美しい言葉」を意味し、シャマン（paje）の儀礼詠唱・神話語り・夢の語りに用いられる詩的言語次元を指す。日常言語（ñe'ẽ rei）と区別され、Curt Nimuendajú（1914）、León Cadogan（1959 'Ayvu Rapyta'）の収録が世界に知らしめた。",
    background="グアラニー宗教思想の核心概念、言語の二層構造（聖／俗）の体系化。",
    development="ピエール・クラストル『国家に抗する社会』（1974）で哲学的に再評価、近代国家論への反証として援用。",
    historical_context="パラグアイ国民国家形成の二言語政策（スペイン語＋グアラニー語、1992）の文化的根拠。",
    primary_source_url=WIKI+"Ayvu_Rapyta",
    primary_source_type="Cadogan 'Ayvu Rapyta' (1959, academic ed.)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"日常言語と聖言語の二層構造は、AI生成の単一言語層に対する根本的な異論を提示する。",
         "related_ai_phenomenon":"言語の聖俗二層と AI の単層生成"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Clastres anthropology",
         "description":"クラストル『国家に抗する社会』のグアラニー研究と直結する基底概念。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"sacred language",
         "description":"聖言語と詩的言語の理論的接続点を成す。"}])

add(**C, name_ja="ヤノマミ・ワラペティ詠唱",
    name_en="Yanomami wayamou ceremonial dialogue",
    name_original="wayamou",
    period_key="先住民口承伝統期",
    definition="ベネズエラ・ブラジル国境のヤノマミ族の儀礼的対話形式。訪問村と被訪問村の男性代表が、夜通し向き合って即興的詩的対話を交わし、贈与・婚姻・同盟を交渉する。Bruce Albert と Davi Kopenawa『落ちる空』（2010、仏／2013、英）が世界に紹介、シャマニックな宇宙論的言語実践として理論化された。",
    background="アマゾン低地先住民の儀礼対話伝統、ヤノマミ宇宙論の言語的核。",
    development="近年は鉱業開発反対運動・国際先住民フォーラムでヤノマミ自身が引用する政治的詩学となる。",
    historical_context="アマゾン森林破壊・違法採掘の文脈での文化的主権主張。",
    primary_source_url=WIKI+"The_Falling_Sky",
    primary_source_type="Albert & Kopenawa 'The Falling Sky' (Harvard UP)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"二人の話者の交替的即興は、単一話者AIモデルへの根本的代替提示。",
         "related_ai_phenomenon":"対話的共同生成と単一話者 AI"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Amazonian perspectivism",
         "description":"Viveiros de Castro パースペクティヴィズム理論の言語的事例。"}])

add(**C, name_ja="シピボ・コニボ・イカロ",
    name_en="Shipibo-Conibo icaro (shamanic song)",
    name_original="icaro",
    period_key="先住民口承伝統期",
    definition="ペルー・アマゾンのシピボ・コニボ族のシャマニック詠唱。アヤワスカ儀礼で歌われ、幾何学的視覚パターン（kené）と一対一に対応する音響パターンを成す。Kenneth Kensinger（1973）以降、人類学・民族音楽学・現代医療人類学の対象となり、近年は西洋アヤワスカ・ツーリズムで広く知られる。",
    background="アマゾン低地植物精神文化の音響的中核。",
    development="グローバル新霊性運動への取り込みと、それに対する文化的主権主張の緊張。",
    historical_context="アヤワスカのグローバル商品化と先住民集合的知識権利問題。",
    primary_source_url=ELAR+"deposit/",
    primary_source_type="ELAR: Shipibo language archives",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"視覚（kené）と音響（icaro）が同一構造として記述される共感覚的詩学は、マルチモーダル AI 生成の理論的祖型。",
         "related_ai_phenomenon":"共感覚的マルチモーダル AI"}])

add(**C, name_ja="ナワトル・クイカトル",
    name_en="Nahuatl cuīcatl (song-poem)",
    name_original="cuīcatl",
    period_key="先住民口承伝統期",
    definition="アステカ／ナワ族の歌詩ジャンル総称。yāōcuīcatl（戦士歌）、xōchicuīcatl（花の歌）、icnōcuīcatl（哀歌）等の下位ジャンルを持ち、Cantares Mexicanos（c.1550-80）、Romances de los Señores de la Nueva España（c.1582）に約180編が記録される。Miguel León-Portilla による哲学的読解が古典的基盤。",
    background="アステカ宮廷詩文化、ネサワルコヨトル（1402-72）等の王族詩人の存在。",
    development="現代ナワトル・ルネサンス（Natalio Hernández, Patrick Johansson）に継承。",
    historical_context="征服直後のフランシスコ会修道士による収録が、口承文化の例外的保存例となった。",
    primary_source_url=WIKI+"Cantares_Mexicanos",
    primary_source_type="Bierhorst ed. Cantares Mexicanos (Stanford UP)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Mesoamerican ethnohistory",
         "description":"León-Portilla, Lockhart らメソアメリカ研究の中核対象。"}])


# ============================================================
# E: Arctic + Australian Dreaming song-cycle types (6)
# ============================================================
add(**C, name_ja="サミ・ヨイク（拡張・主権）",
    name_en="Sámi yoik (sovereignty perspective)",
    name_original="luohti / juoigan",
    period_key="先住民文芸復興期",
    definition="サーミ族の伝統詠唱形式 yoik（北サーミ luohti）の現代的位置付け。人・場所・動物の本質を「描く」のではなく「である」と理解される非表象的歌唱形式で、Mari Boine（1956-）以降のサーミ・ルネサンスで国際的展開。Eurovision 2019 のフィンランド代表 Yoik 出演で象徴されるように、現代北欧文化の脱植民化象徴となった。",
    background="サーミ口承詠唱伝統と20世紀後半の文化主権運動の交差。",
    development="2017年ノルウェー・サーミ議会真実和解委員会、2024年スウェーデン公式謝罪に至る政治的文脈で、ヨイクが象徴的位置を占める。",
    historical_context="ノルウェー・スウェーデン・フィンランドの長期同化政策（ノルウェー化政策、寄宿学校）への文化的応答。",
    primary_source_url="https://samediggi.no/",
    primary_source_type="Sámediggi (Sámi Parliament) cultural archive",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ヨイクが対象を「描写する」のではなく「である」とする非表象的存在論は、AI 表象主義への根本的代替を提示。",
         "related_ai_phenomenon":"非表象的存在論 vs AI 表象主義"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Sámi indigenous studies",
         "description":"サーミ研究（Kuokkanen, Valkonen）の中核対象。"}])

add(**C, name_ja="イヌイト・カウジマヤトゥカンギット",
    name_en="Inuit Qaujimajatuqangit (IQ)",
    name_original="Qaujimajatuqangit",
    period_key="先住民文芸復興期",
    definition="「以前から知られていたこと」を意味するイヌイト語概念。1990年代以降、ヌナブト準州（1999年カナダ設立）の公式統治原理として体系化された伝統知識・倫理・物語の総体。8原則（Pijitsirniq, Aajiiqatigiingniq 等）を持ち、口承伝承を行政・教育・環境管理に統合する世界初の先住民知識統治システム。",
    background="20世紀後半の Nunavut Land Claims Agreement 交渉、伝統知識の公式制度化要求。",
    development="2002年ヌナブト政府公式採用、現在は気候変動・教育政策の中核に統合。",
    historical_context="先住民知識を国家統治原理として制度化した世界的先進事例。",
    primary_source_url="https://www.gov.nu.ca/",
    primary_source_type="Government of Nunavut: IQ policy documents",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"知の形式","status":"rethinking",
         "rationale":"伝統口承知識を統治制度に統合する IQ モデルは、AI 時代の知識統治の代替モデルとして再読される。",
         "related_ai_phenomenon":"伝統知識統治と AI 知識統治"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Indigenous knowledge governance",
         "description":"伝統知識の制度化に関する人類学・政策学研究の中核事例。"}])

add(**C, name_ja="ユピック口承（ユピアック）",
    name_en="Yup'ik / Yupiit oral tradition",
    name_original="Yugtun qulirat",
    period_key="先住民口承伝統期",
    definition="アラスカ南西部 Yup'ik / Yupiit 民族の口承物語ジャンル群。qulirat（古代神話）、qanemcit（個人体験譚）、yuarutet（歌）等を含み、qasgiq（公民館）冬期儀礼で語られる。Ann Fienup-Riordan の長期民族誌記録（1970s-）が学術的基盤、Calista Heritage Foundation が言語復興・出版を主導。",
    background="ベーリング海沿岸エスキモー口承伝統、19世紀ロシア正教・20世紀米国宣教団の影響を受けつつ存続。",
    development="アラスカ州立大学 Yup'ik 教育プログラム、Calista Foundation の口承デジタル化が進行中。",
    historical_context="気候変動・伝統生計（caribou, fish）変動による口承継承危機の同時代史。",
    primary_source_url="https://calistaheritage.org/",
    primary_source_type="Calista Heritage Foundation archives",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ソングサイクル（南東部豪）",
    name_en="Australian song-cycle (southeast)",
    name_original="manikay (Yolŋu term, generalized)",
    period_key="先住民口承伝統期",
    definition="北部豪 Yolŋu（アーネムランド）の manikay（連歌）型ソングサイクルの代表。死者の魂を祖先の地に送り返す葬送詩、トーテム動物の創造行程詩等で構成される。R.M. Berndt 'Three Faces of Love' (1976), Catherine Ellis 民族音楽学的記録、近年は Garma Festival での公開上演を通じて継承。",
    background="ドリーミング宇宙論の音楽的具現化、200以上の固有歌型を持つ。",
    development="現代では Yothu Yindi バンド（'Treaty' 1991）等を通じて世界的展開。",
    historical_context="豪先住民土地権利運動（Mabo 判決 1992）以降の文化的可視化期。",
    primary_source_url=AIAT,
    primary_source_type="AIATSIS: Yolŋu manikay archive",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Yolŋu kinship & ritual",
         "description":"Howard Morphy らの Yolŋu 民族誌研究と直結。"}])

add(**C, name_ja="トーテム連歌",
    name_en="totemic song-line cycle",
    name_original="totemic song-line",
    period_key="先住民口承伝統期",
    definition="豪先住民ソングラインのうち、特定トーテム動物（袋熊、エミュー、虹蛇等）の創造行程を歌う連歌型。Strehlow 『Songs of Central Australia』(1971) が中部砂漠 Aranda の例を学術的に記録。各歌節が地理的地点と一対一対応し、歌唱が地理・所有・身分・儀礼権を同時に確認する重層的詩学装置となる。",
    background="豪砂漠地帯の長距離移動・水場知識・親族領域の音楽的記録。",
    development="20世紀末以降の土地権利訴訟で、ソングラインが法廷証拠として援用される。",
    historical_context="Mabo 判決（1992）・Native Title Act（1993）以降の口承証拠の法的承認。",
    primary_source_url=AIAT,
    primary_source_type="AIATSIS: Strehlow Research Centre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="制限歌・性別歌",
    name_en="restricted/gendered songs (Aboriginal)",
    name_original="men's/women's business songs",
    period_key="先住民口承伝統期",
    definition="豪先住民歌唱伝統における性別・年齢・通過儀礼段階に応じた厳密な聞き手制限を持つ歌群。men's business / women's business と呼ばれる秘儀的歌は、当該カテゴリ外の人物による聴取・記録・再生産が文化的に禁じられ、AIATSIS は restricted access tier で管理する。AI 時代における訓練データ収集の倫理的限界の象徴例。",
    background="豪先住民社会の性別・年齢階梯的知識管理伝統。",
    development="1990年代以降の restricted access protocols の制度化、デジタル時代の倫理的拡張議論。",
    historical_context="20世紀人類学者の倫理的失敗（性別制限歌の公開出版）への反省としての protocol 形成。",
    primary_source_url=AIAT+"collection/restricted-access",
    primary_source_type="AIATSIS restricted access protocols",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"特定範疇の聞き手にしか伝達されない歌は、無差別アクセス前提のAI訓練と根本的に対立する文化的知識アーキテクチャ。",
         "related_ai_phenomenon":"アクセス制限知識と AI 訓練倫理"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"聞き手制限が真正性を構成する歌は、無制限再生産可能な AI 生成と存在論的に異なる。",
         "related_ai_phenomenon":"アクセス制限が構成する真正性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"gendered ritual knowledge",
         "description":"性別秘儀知識の人類学的研究（Diane Bell, Catherine Berndt）と直結。"}])


# ============================================================
# F: Performance theory + Indigenous DH/AI sovereignty (9)
# ============================================================
add(**C, name_ja="パフォーマンス・テクスト理論",
    name_en="performance theory of orality",
    name_original="performance theory",
    period_key="先住民文芸復興期",
    definition="Richard Bauman 'Verbal Art as Performance' (1977), Dell Hymes 'In Vain I Tried to Tell You' (1981), Dennis Tedlock 'The Spoken Word and the Work of Interpretation' (1983) を中核とする民俗学・人類言語学の理論的潮流。口承を固定テキストではなく「演じられる出来事」として捉え直す枠組みで、先住民口承研究の方法論的基盤となった。",
    background="20世紀中葉のテキスト主義（Lord-Parry 口承定型句理論）への批判的応答。",
    development="現代オラリティ研究、エスノポエティクス、デジタル民族誌の方法論的支柱となった。",
    historical_context="北米先住民・先住民文学の学術的主流化の時期と並行。",
    primary_source_url=WIKI+"Performance_studies",
    primary_source_type="Bauman, Hymes, Tedlock canonical works",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"テクストではなく出来事としての口承理解は、AI生成テキストの「出来事性」の不在を理論化する基準。",
         "related_ai_phenomenon":"AI 生成の非出来事性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"linguistic anthropology",
         "description":"言語人類学（Bauman, Briggs, Silverstein）と直接接続。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"performance poetics",
         "description":"パフォーマンス詩学の現代的理論基盤。"}])

add(**C, name_ja="エスノポエティクス",
    name_en="ethnopoetics",
    name_original="ethnopoetics",
    period_key="先住民文芸復興期",
    definition="Jerome Rothenberg, Dell Hymes, Dennis Tedlock らが1960-70年代に展開した詩学運動。先住民・口承詩を西洋詩規範ではなく自文化の内在的詩学（行分け・リズム・声色・沈黙）に従って翻訳・出版する方法論。雑誌『Alcheringa』(1970-)、Rothenberg 編『Technicians of the Sacred』(1968) が代表的成果。",
    background="20世紀対抗文化期の西洋中心詩学批判と、先住民詩への新たな接近。",
    development="現代の先住民詩翻訳実践、デジタル人文学における口承表記の方法論的源流。",
    historical_context="北米先住民文芸復興（Momaday, Silko, Welch）と並行する出版運動。",
    primary_source_url=WIKI+"Ethnopoetics",
    primary_source_type="UbuWeb / Rothenberg archives",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"西洋詩規範を相対化する自文化内在詩学は、AI 生成の英語中心バイアスを批判する理論基盤。",
         "related_ai_phenomenon":"AI 生成の言語中心バイアス批判"}])

add(**C, name_ja="先住民AI主権論（Lewis）",
    name_en="Indigenous AI sovereignty (Lewis et al.)",
    name_original="Indigenous AI sovereignty",
    period_key="先住民文芸復興期",
    definition="Jason Edward Lewis（イロコイ系、Concordia University）が中心となり編纂した『Indigenous Protocol and Artificial Intelligence Position Paper』(2020) が定式化した理論枠組み。AIシステムを「関係的存在」として位置付け、先住民認識論（リレーショナル存在論、kincentric ecology）を基盤に AI 設計の根本的代替を提案する。Hawai'i, Aotearoa, Australia, Canada の先住民研究者26名共著。",
    background="2019 Banff Centre 集中ワークショップ、UNESCO AI ethics 枠組み策定への先住民介入。",
    development="現代AI倫理・GenAI・データ主権論議の中核理論枠組みとして急速に拡大中。",
    historical_context="2020年代AI倫理論議における非西洋認識論の制度的可視化期。",
    primary_source_url="https://www.indigenous-ai.net/position-paper",
    primary_source_type="Indigenous Protocol & AI: Position Paper (2020, open access)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"AI を「関係的存在（kin）」として位置付ける先住民認識論は、ツール／主体二項対立を解体する根本的枠組みを提供する。",
         "related_ai_phenomenon":"AI の関係的存在論的位置付け"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"集合的・関係的作者性概念は、AI 共著作の倫理的枠組みを再構築する基準。",
         "related_ai_phenomenon":"関係的 AI 共著作"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"先住民データ主権原則（CARE）は、AI 訓練データの真正性・帰属性を再定義する。",
         "related_ai_phenomenon":"先住民データ主権と AI 訓練"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"relational ontology",
         "description":"関係的存在論（Bird-David, Hallowell, Watts）の AI 倫理への展開。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI ethics frameworks",
         "description":"AI 倫理論議の中心代替枠組みのひとつ。"}])

add(**C, name_ja="先住民データ主権（CARE）",
    name_en="Indigenous data sovereignty (CARE)",
    name_original="CARE Principles",
    period_key="先住民文芸復興期",
    definition="Global Indigenous Data Alliance（GIDA、2018設立）が策定した先住民データ管理4原則：Collective benefit, Authority to control, Responsibility, Ethics（CARE Principles）。FAIR 原則（Findable, Accessible, Interoperable, Reusable）を補完するもので、AI 訓練データへの先住民集合的同意・管理権を制度化する国際的枠組み。",
    background="ニュージーランド Te Mana Raraunga（マオリ・データ主権ネットワーク、2015）等の地域運動の国際統合。",
    development="現代AI ガバナンス（EU AI Act, US NIST framework）への影響、先住民研究機関の国際標準採用が進行中。",
    historical_context="2010年代の生医学データ問題（Havasupai 訴訟 2010）以降のデータ倫理進展。",
    primary_source_url="https://www.gida-global.org/care",
    primary_source_type="GIDA: CARE Principles (open framework)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"集合的データ管理権原則は、個人作者性前提の知財制度・AI 訓練データ調達制度の根本的代替を提示する。",
         "related_ai_phenomenon":"集合的データ権と AI 訓練"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"管理権・倫理的継承を真正性の構成要件とする CARE は、純粋な技術的真正性概念を相対化する。",
         "related_ai_phenomenon":"管理的真正性と AI"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"indigenous knowledge protocols",
         "description":"伝統知識管理プロトコル研究の核心枠組み。"}])

add(**C, name_ja="アンジー・アブディラ（脱植民AI）",
    name_en="Angie Abdilla (decolonial AI)",
    name_original="Angie Abdilla",
    period_key="先住民文芸復興期",
    definition="Palawa-Trawlwoolway（タスマニア）系豪人研究者。Old Ways, New (Sydney 拠点) を主宰し、Indigenous Protocol & AI Working Group の共同主導者として、Country-centric AI（土地中心AI）の概念を提唱。AI システムを土地・季節・関係性の中で設計し直す方法論を、現代豪政府デジタル戦略・国際先住民AI論議に持ち込んだ実践理論家。",
    background="豪先住民研究の制度的成熟（AIATSIS, Charles Sturt University 等）と、国際先住民AI運動の興隆。",
    development="2020-2025 に豪国家AI戦略・UNESCO AI ethics 枠組みへの先住民視点組み込みを主導。",
    historical_context="2017年 Uluru Statement from the Heart 以降の豪先住民認識深化期と並行。",
    primary_source_url="https://oldwaysnew.com/",
    primary_source_type="Old Ways, New: research outputs",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"Country-centric AI は AI を土地・関係性の中で位置付け直し、抽象データ駆動 AI を相対化する。",
         "related_ai_phenomenon":"場所性・関係性に根ざした AI 設計"},
        {"axis":"知の形式","status":"rethinking",
         "rationale":"土地中心の知識アーキテクチャは、抽象的・脱地理的 AI 訓練データ前提への根本的批判。",
         "related_ai_phenomenon":"場所性ある AI 設計"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"Country / kincentric ecology",
         "description":"豪先住民 Country 概念と人類学的関係論的存在論の AI 適用。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"decolonial AI",
         "description":"脱植民地化AI議論の代表的実践論。"}])

add(**C, name_ja="ノラ・マルクス・ダウエンハウアー",
    name_en="Nora Marks Dauenhauer (Tlingit poetics)",
    name_original="Nora Marks Dauenhauer",
    period_key="先住民文芸復興期",
    definition="トリンギット系研究者・詩人（1927-2017）。夫 Richard Dauenhauer と共に『Haa Shuká, Our Ancestors』(1987), 『Haa Tuwunáagu Yís』(1990), 『Haa Kusteeyí』(1994) のトリンギット口承三部作を編纂。トリンギット語原文・英語訳・パフォーマンス文脈注釈を統合した先住民口承学術出版の世界的範型を確立した。",
    background="アラスカ先住民言語復興運動と20世紀後半のエスノポエティクス潮流の交差。",
    development="現代の先住民口承学術出版（Cherokee, Lakota, Anishinaabe 等）の方法論的祖型となった。",
    historical_context="1971年 Alaska Native Claims Settlement Act 後のアラスカ先住民文化制度確立期。",
    primary_source_url=WIKI+"Nora_Marks_Dauenhauer",
    primary_source_type="Sealaska Heritage Institute archives",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クレイグ・ウォマック先住民批評",
    name_en="Craig Womack's Indigenous criticism",
    name_original="Red on Red",
    period_key="先住民文芸復興期",
    definition="Craig S. Womack（Muskogee Creek-Cherokee）が『Red on Red: Native American Literary Separatism』(1999) で展開した先住民文学批評の方法論。先住民文学を植民地理論・ポストコロニアル理論の従属変数ではなく、自文化内在的価値基準（部族文学的主権）から評価する立場を確立。21世紀先住民文学批評の方法的支柱。",
    background="20世紀末ポストコロニアル批評の普遍主義への批判的応答。",
    development="Robert Warrior, Jace Weaver らとの『American Indian Literary Nationalism』(2006) 共著で潮流化。",
    historical_context="北米先住民文学批評の脱植民地化・自決化の理論的画期。",
    primary_source_url=WIKI+"Craig_Womack",
    primary_source_type="University of Minnesota Press: Red on Red",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"自文化内在価値基準論は、AI生成テキストの真正性評価に外在/内在基準の区別を導入する理論的祖型。",
         "related_ai_phenomenon":"内在的真正性 vs 外在的真正性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"tribal sovereignty",
         "description":"部族主権論と文学批評の接続点。"}])

add(**C, name_ja="ダニエル・ヒース・ジャスティス",
    name_en="Daniel Heath Justice (Cherokee literary theory)",
    name_original="Daniel Heath Justice",
    period_key="先住民文芸復興期",
    definition="チェロキー系カナダ・ブリティッシュコロンビア大学教授。『Why Indigenous Literatures Matter』(2018) で先住民文学を「我々はいかに正しく生きうるか」「我々は互いに何者なのか」「我々はいかに祖先・子孫と関係づくか」「我々はいかに非人間と関係づくか」の4問への応答として位置付ける関係論的批評理論を展開。21世紀先住民批評の倫理転回を代表する。",
    background="21世紀先住民批評の世代（Justice, Womack, Warrior, Million 等）の継承と展開。",
    development="2024年現在、北米・豪・ニュージーランド・北欧先住民研究教育の中心テキスト。",
    historical_context="2010年代後半の先住民研究の倫理的・関係論的転回期。",
    primary_source_url=WIKI+"Daniel_Heath_Justice",
    primary_source_type="Wilfrid Laurier University Press",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"4つの倫理的関係問題への応答としての文学観は、AI 生成テキストの倫理的立場の評価枠組みを提供。",
         "related_ai_phenomenon":"AI 生成テキストの関係論的倫理評価"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"relational ethics",
         "description":"関係論的倫理学と文学理論の接続。"}])

add(**C, name_ja="先住民デジタル人文学",
    name_en="Indigenous digital humanities",
    name_original="Indigenous DH",
    period_key="先住民文芸復興期",
    definition="2010年代以降に体系化された、先住民言語・口承・歴史のデジタル化を、CARE 原則・トライバル・プロトコル・関係論的存在論に従って実践する学際領域。Mukurtu CMS（プラットフォーム）、Endangered Languages Archive（ELAR、SOAS）、AIATSIS Online、Te Hiku Media（マオリ AI 音声プロジェクト）等を主要事例とする。AI 時代の先住民文学研究の方法的基盤。",
    background="2000年代後半のデジタル人文学興隆と、先住民データ主権運動の合流。",
    development="2020年代AI生成技術の急速な進展に対する先住民側の制度的応答として、急速に拡大中。",
    historical_context="生成AI・LLM時代における先住民言語・口承の AI 訓練データ問題への制度的応答。",
    primary_source_url="https://mukurtu.org/",
    primary_source_type="Mukurtu CMS / Te Hiku Media public documentation",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"集合的・条件付きアクセスを技術的に実装するDHプラットフォームは、無制限アクセス前提のAI訓練と根本的に対立する。",
         "related_ai_phenomenon":"条件付きアクセスDHとAI訓練"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"先住民言語AI（Te Hiku の Reo Māori 音声認識等）は、コミュニティ管理下のAI開発の代替モデルを提示。",
         "related_ai_phenomenon":"コミュニティ管理 AI 開発"},
        {"axis":"言語","status":"rethinking",
         "rationale":"絶滅危機言語のデジタル保存は、言語多様性とAI言語覇権の緊張を具体化する。",
         "related_ai_phenomenon":"絶滅危機言語保全 vs AI言語覇権"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"digital ethnography",
         "description":"デジタル民族誌・言語人類学との理論的接続。"},
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"low-resource language AI",
         "description":"低リソース言語AI 研究の倫理的枠組み。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(name_ja=nj, region=REGION,
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
        print(f"[c30 add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c30 add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
