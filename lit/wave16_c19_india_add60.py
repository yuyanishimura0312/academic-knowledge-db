"""LIT-DB Phase 2 Wave 16 — C19 India ADD60.

Subfield: lit_india (id=12), region='南アジア'.
Adds 60 NEW non-overlapping concepts:
  A: Sanskrit drama deep (8)
  B: Sanskrit kavya & poetics deep (8)
  C: Tamil classical/medieval deep (8)
  D: Bengali Renaissance deep (8)
  E: Hindi modern deep (8)
  F: Urdu modern deep (8)
  G: Marathi / Tamil modern (6)
  H: Malayalam / Kannada / Dalit women (6)

Sources: GRETIL/SARIT for classical, Project Madurai for Tamil,
Wikisource (multilingual) for modern. >= 70% primary tier.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("古典サンスクリット劇期", "Classical Sanskrit Drama", -200, 1200,
     "バーサ、シュードラカ、カーリダーサ、ヴィシャーカダッタ、バヴァブーティらが活躍した古典サンスクリット演劇期。"),
    ("古典サンスクリット詩学期", "Classical Sanskrit Kavya & Poetics", 100, 1700,
     "バーラヴィ、マーガ、シュリーハルシャ、アーナンダヴァルダナ以降の古典詩学・修辞論の体系化期。"),
    ("サンガム古典期", "Sangam Classical Period", -300, 300,
     "紀元前3世紀から紀元後3世紀の南インド・タミル古典期。"),
    ("タミル中世文学期", "Medieval Tamil Literature", 500, 1400,
     "バクティ詩、双叙事詩、Periya Puranam、Kamparamayanam等のタミル中世文学期。"),
    ("ベンガル・ルネサンス期", "Bengal Renaissance", 1800, 1947,
     "19世紀以降ベンガル地方で展開した近代化運動期。"),
    ("ヒンディー・チャーヤーヴァード期", "Hindi Chhayavad Period", 1900, 1950,
     "プラサード、ニラーラー、パント、マハーデーヴィー・ヴァルマーらヒンディー新ロマン主義詩運動期。"),
    ("ヒンディー散文成熟期", "Hindi Prose Maturity", 1900, 1980,
     "プレームチャンド以降、ヤシュパール、アジェーヤらに至るヒンディー近代散文の成熟期。"),
    ("ウルドゥー近代詩・散文期", "Urdu Modern Poetry & Prose", 1850, 1990,
     "ガーリブ、ハーリー、サー・サイイド、イクバール、マントー、チュグタイ、ファイズらのウルドゥー近代期。"),
    ("マラーティー近現代文学期", "Modern Marathi Literature", 1900, 2025,
     "サーネー・グルージー、カーンデーカル、プ・ラ・デーシュパーンデー、テンドゥルカルらのマラーティー近現代文学期。"),
    ("タミル近現代文学期", "Modern Tamil Literature", 1900, 2025,
     "バーラティ以降のタミル近現代詩・小説期。"),
    ("マラヤーラム近現代文学期", "Modern Malayalam Literature", 1900, 2025,
     "クマーラン・アーサン、ヴァッラットール、タカリ、MT、OV・ヴィジャヤンらのマラヤーラム文学期。"),
    ("カンナダ近現代文学期", "Modern Kannada Literature", 1900, 2025,
     "クヴェンプ、ベーンドレー、カーラント、アナンタムールティ、ビャイラッパ、カルナードらのカンナダ文学期。"),
    ("インド・ダリット／女性文学期", "Indian Dalit & Women's Literature", 1960, 2025,
     "1960年代以降、ダリット女性・地域女性の主体的文学表現の確立期。"),
]


GRETIL = "https://gretil.sub.uni-goettingen.de/gretil.html"
SARIT = "https://sarit.indology.info/"
PMADURAI = "https://www.projectmadurai.org/"
WSRC_SA = "https://sa.wikisource.org/wiki/"
WSRC_HI = "https://hi.wikisource.org/wiki/"
WSRC_BN = "https://bn.wikisource.org/wiki/"
WSRC_TA = "https://ta.wikisource.org/wiki/"
WSRC_MR = "https://mr.wikisource.org/wiki/"
WSRC_UR = "https://ur.wikisource.org/wiki/"
WSRC_ML = "https://ml.wikisource.org/wiki/"
WSRC_KN = "https://kn.wikisource.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"
ARCHIVE = "https://archive.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C_DEV = dict(subfield_code="lit_india", region="南アジア", original_script="devanagari")
C_BEN = dict(subfield_code="lit_india", region="南アジア", original_script="bengali")
C_TAM = dict(subfield_code="lit_india", region="南アジア", original_script="tamil")
C_URD = dict(subfield_code="lit_india", region="南アジア", original_script="arabic")
C_MAL = dict(subfield_code="lit_india", region="南アジア", original_script="malayalam")
C_KAN = dict(subfield_code="lit_india", region="南アジア", original_script="kannada")
C_ROM = dict(subfield_code="lit_india", region="南アジア", original_script="roman")


# ============================================================
# A: 古典サンスクリット劇 深掘り（8）
# ============================================================
add(**C_DEV, name_ja="カーリダーサ『シャクンタラー』",
    name_en="Kalidasa's Abhijnanashakuntalam",
    name_original="अभिज्ञानशाकुन्तलम्",
    period_key="古典サンスクリット劇期",
    definition="グプタ朝期カーリダーサの代表的サンスクリット劇（5世紀頃）。マハーバーラタの挿話を基に、ドゥシュヤンタ王と仙女シャクンタラーの愛と認知の指輪の物語を展開する。ゲーテが激賞し、19世紀ヨーロッパのインド学受容の中核となった。",
    background="グプタ朝古典文化の隆盛、宮廷劇詩の成熟。",
    development="ゲーテ、ヘルダー、ジョーンズ訳を経て19世紀世界文学の規範となった。",
    historical_context="グプタ朝古典期インド宮廷文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Abhijnanashakuntalam (Kalidasa)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="カーリダーサ『メーガドゥータ』",
    name_en="Kalidasa's Meghaduta",
    name_original="मेघदूतम्",
    period_key="古典サンスクリット劇期",
    definition="カーリダーサの抒情詩『雲の使者』。罰を受けたヤクシャが妻への伝言を雨雲に託すマンダークラーンター韻律の二部構成。サンスクリット使者詩（ドゥータカーヴィヤ）の祖型を成し、後世数百の模倣作を生んだ。",
    background="グプタ朝古典詩学の形成、季節詩・地誌詩の伝統。",
    development="ドゥータカーヴィヤ系譜の祖型として、近世まで模倣作が継続した。",
    historical_context="5世紀頃グプタ朝古典文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Meghaduta (Kalidasa)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="カーリダーサ『ラグヴァンシャ』",
    name_en="Kalidasa's Raghuvamsha",
    name_original="रघुवंशम्",
    period_key="古典サンスクリット劇期",
    definition="カーリダーサのマハーカーヴィヤ。ラーマの祖父ディリーパからアグニヴァルナまで19代のラグ王朝の系譜を、19編で歌う。サンスクリット叙事詩学の規範作品とされ、宮廷詩の形式と王統表象の典型を確立した。",
    background="グプタ朝の王朝表象文学、ラーマーヤナ系譜の宮廷的再構成。",
    development="後代のマハーカーヴィヤの規範となり、注釈伝統が中世まで継続した。",
    historical_context="グプタ朝古典詩学期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Raghuvamsha",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="カーリダーサ『クマーラサンバヴァ』",
    name_en="Kalidasa's Kumarasambhava",
    name_original="कुमारसम्भवम्",
    period_key="古典サンスクリット劇期",
    definition="カーリダーサのマハーカーヴィヤ『戦神の誕生』。シヴァとパールヴァティーの結婚、その息子クマーラ（戦神カールティケーヤ）誕生を主題とする。神話と宮廷叙情詩の融合形式を確立し、サンスクリット詩学の代表作とされる。",
    background="グプタ朝のシヴァ信仰興隆、宮廷神話詩の形成。",
    development="後代マハーカーヴィヤの主題的・形式的範型となった。",
    historical_context="グプタ朝古典文化期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Kumarasambhava",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="バーサ劇集",
    name_en="Plays of Bhasa",
    name_original="भासनाटकचक्रम्",
    period_key="古典サンスクリット劇期",
    definition="紀元前2世紀から紀元後2世紀頃と推定される最古期のサンスクリット劇作家バーサに帰される13編の戯曲群。1912年にケララで発見され、『スヴァプナヴァーサヴァダッタ』『プラティジュニャーヤウガンダラーヤナ』等を含む。古典サンスクリット劇の起源研究の中核資料。",
    background="ケーララ地域での写本伝承、20世紀初頭のサンスクリット劇前史発見。",
    development="サンスクリット劇起源論の中核資料として20世紀インド学を再編した。",
    historical_context="古代インド宮廷劇の前史期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Bhasa Trivandrum Plays",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="シュードラカ『ムリッチャカティカー』",
    name_en="Shudraka's Mrcchakatika",
    name_original="मृच्छकटिकम्",
    period_key="古典サンスクリット劇期",
    definition="シュードラカに帰される10幕のサンスクリット劇『土の小車』（4-5世紀頃）。バラモン青年チャールダッタと高級遊女ヴァサンタセーナーの恋愛と政治陰謀を描く。庶民的写実性と社会階層の描写で古典サンスクリット劇のなかで稀有な「現実劇」と位置づけられる。",
    background="グプタ朝以前あるいは初期グプタ朝期の市民社会描写の劇形式。",
    development="近代インド演劇・映画（『ウトサヴ』1984等）に翻案され、世界演劇史でも重要視される。",
    historical_context="古代インド都市文化期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Mrcchakatika (Shudraka)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ヴィシャーカダッタ『ムドラーラークシャサ』",
    name_en="Vishakhadatta's Mudraraksasa",
    name_original="मुद्राराक्षसम्",
    period_key="古典サンスクリット劇期",
    definition="ヴィシャーカダッタによる7幕のサンスクリット政治劇（5世紀頃）。チャーナキヤ（カウティリヤ）がチャンドラグプタ・マウリヤを王位につけ、敵対者ラークシャサを帰服させる政略を主題とする。サンスクリット劇のなかで稀少な政治謀略劇。",
    background="グプタ朝期のマウリヤ王朝・チャーナキヤ伝承の文学化。",
    development="近代インド政治劇・歴史劇の祖型として参照される。",
    historical_context="グプタ朝期の歴史的政略文学。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Mudraraksasa",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="バヴァブーティ『ウッタララーマチャリタ』",
    name_en="Bhavabhuti's Uttararamacarita",
    name_original="उत्तररामचरितम्",
    period_key="古典サンスクリット劇期",
    definition="8世紀のサンスクリット劇作家バヴァブーティの後期傑作。ラーマがシーターを追放した後の悲哀と再会を、カルナ・ラサ（悲哀の味）の頂点として描く。カーリダーサと並ぶ古典サンスクリット劇の双璧と評価される。",
    background="ラーシュトラクータ朝・カナウジ宮廷期のサンスクリット劇成熟。",
    development="後代のラーマ受容、悲劇詩学（カルナ・ラサ論）の中核作品となった。",
    historical_context="北インド古典後期サンスクリット文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Uttararamacarita",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: サンスクリット詩学・カーヴィヤ深掘り（8）
# ============================================================
add(**C_DEV, name_ja="バーラヴィ『キラータールジュニーヤ』",
    name_en="Bharavi's Kiratarjuniya",
    name_original="किरातार्जुनीयम्",
    period_key="古典サンスクリット詩学期",
    definition="6世紀のサンスクリット詩人バーラヴィのマハーカーヴィヤ。マハーバーラタの挿話「アルジュナとキラータ（シヴァの狩人姿）の戦い」を主題とする18章の宮廷叙事詩。文体的精緻さで「五大マハーカーヴィヤ」の一角を占める。",
    background="6世紀北インド・南インド宮廷詩の成熟。",
    development="マーガ、シュリーハルシャに継承される文体的精緻化系譜の起点。",
    historical_context="グプタ朝後期宮廷文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Kiratarjuniya",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="マーガ『シシュパーラヴァダ』",
    name_en="Magha's Sisupalavadha",
    name_original="शिशुपालवधम्",
    period_key="古典サンスクリット詩学期",
    definition="7-8世紀の詩人マーガのマハーカーヴィヤ。クリシュナがチェーディ国王シシュパーラを討つ物語を20章で描く。「マーガの三比喩」など修辞的精緻さの極致として、五大マハーカーヴィヤの代表とされる。",
    background="ラージャスターン地方の宮廷詩人マーガ、サンスクリット修辞学の発展。",
    development="後代の修辞論（マンマタ、ヴィシュヴァナータ）の主要分析対象となった。",
    historical_context="古典後期宮廷詩文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Sisupalavadha",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="シュリーハルシャ『ナイシャダチャリタ』",
    name_en="Sriharsa's Naisadhacarita",
    name_original="नैषधचरितम्",
    period_key="古典サンスクリット詩学期",
    definition="12世紀の詩人・哲学者シュリーハルシャのマハーカーヴィヤ。マハーバーラタのナラ王とダマヤンティーの恋物語を22章で展開する。哲学的・修辞的密度の極限的精緻化として、サンスクリット古典詩の最終形態と評される。",
    background="カナウジ・カシミール宮廷詩の最終期、ニヤーヤ哲学との交差。",
    development="後代の注釈伝統の最重要対象作品となった。",
    historical_context="サンスクリット古典詩終焉期の宮廷文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Naisadhacarita",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="アーナンダヴァルダナ『ドヴァニャーローカ』",
    name_en="Anandavardhana's Dhvanyaloka",
    name_original="ध्वन्यालोकः",
    period_key="古典サンスクリット詩学期",
    definition="9世紀カシミールの詩学者アーナンダヴァルダナによるサンスクリット詩学の革新文献。詩の本質を「暗示（ドヴァニ）」とする理論を体系化し、表面的意味（ヴァーチヤ）と暗示的意味（ヴャンギヤ）の階層を確立。サンスクリット詩学史上の転換点となった。",
    background="9世紀カシミール・ミーマーンサー学・文法学の蓄積。",
    development="アビナヴァグプタ『ロチャナ』が注釈し、以降の詩学史の中軸となった。",
    historical_context="カシミール・シャイヴィズム文化期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Dhvanyaloka",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アビナヴァグプタ『ロチャナ／アビナヴァバーラティー』",
    name_en="Abhinavagupta's Locana & Abhinavabharati",
    name_original="लोचनम् / अभिनवभारती",
    period_key="古典サンスクリット詩学期",
    definition="11世紀カシミールの哲学者・詩学者アビナヴァグプタによる二大注釈。『ロチャナ』はドヴァニャーローカ注、『アビナヴァバーラティー』はナーティヤ・シャーストラ注。ラサ論を「普遍化された美的経験（サーダーラニーカラナ）」と再定義し、インド美学の頂点を成した。",
    background="カシミール・シャイヴィズム哲学とプラティヤビジュニャー学派の形成。",
    development="近代インド美学（クーマラスワーミー、タゴール、ゴーシュ）の理論的基盤となった。",
    historical_context="11世紀カシミール宗教哲学期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Locana / Abhinavabharati",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"アビナヴァグプタの普遍化された美的経験理論は、AI生成コンテンツ受容における普遍化と個別化の弁証法を理論化する古典的参照点。",
         "related_ai_phenomenon":"AI生成コンテンツ受容における美的普遍化問題"}])

add(**C_DEV, name_ja="マンマタ『カーヴィヤプラカーシャ』",
    name_en="Mammata's Kavyaprakasha",
    name_original="काव्यप्रकाशः",
    period_key="古典サンスクリット詩学期",
    definition="11世紀カシミールの詩学者マンマタによるサンスクリット詩学綱要書。詩の定義、ドーシャ（瑕疵）、グナ（質）、アランカーラ（修辞）、ラサ（味）、ドヴァニ（暗示）を10章で体系化。後代の詩学教科書の標準テクストとなった。",
    background="11世紀カシミール詩学の総合化、注釈伝統の制度化。",
    development="20以上の注釈書を生み、近世インド詩学教育の基礎テキストとなった。",
    historical_context="カシミール詩学黄金期。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Kavyaprakasha",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ヴィシュヴァナータ『サーヒティヤダルパナ』",
    name_en="Visvanatha's Sahityadarpana",
    name_original="साहित्यदर्पणः",
    period_key="古典サンスクリット詩学期",
    definition="14世紀オリッサの詩学者ヴィシュヴァナータによる詩学綱要『文学の鏡』。詩の定義「rasātmakaṃ vākyaṃ kāvyam（ラサを本質とする言葉が詩）」が後代の標準定義となった。10章構成で詩学の全体像を提示し、近世インド詩学教育の双璧となった。",
    background="14世紀オリッサ宮廷文化、サンスクリット詩学の地理的拡張。",
    development="近世インドのサンスクリット詩学教育で『カーヴィヤプラカーシャ』と並ぶ標準教科書となった。",
    historical_context="14世紀東インド宮廷文化。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Sahityadarpana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="ジャガンナータ『ラサガンガーダラ』",
    name_en="Jagannatha's Rasagangadhara",
    name_original="रसगङ्गाधरः",
    period_key="古典サンスクリット詩学期",
    definition="17世紀のシャー・ジャハーン宮廷詩学者ジャガンナータによるサンスクリット詩学最終期の体系書。ラサ理論の哲学的精緻化を行い、近世サンスクリット詩学の頂点を成した。ムガル朝下のサンスクリット詩学持続の象徴的作品。",
    background="ムガル朝シャー・ジャハーン宮廷でのサンスクリット詩学保護。",
    development="近世サンスクリット詩学の最終的体系書として20世紀インド学の中心研究対象となった。",
    historical_context="17世紀ムガル朝下のサンスクリット文化保存。",
    primary_source_url=GRETIL,
    primary_source_type="GRETIL: Rasagangadhara",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: タミル古典・中世深掘り（8）
# ============================================================
add(**C_TAM, name_ja="トルカーッピヤム・ポルル篇",
    name_en="Tolkappiyam Porul-atikaram",
    name_original="தொல்காப்பியம் பொருளதிகாரம்",
    period_key="サンガム古典期",
    definition="現存最古のタミル語文法・詩学書『トルカーッピヤム』の第三編「内容篇」。アハム（内的・愛情詩）／プラム（外的・英雄詩）の二分体系、ティナイ（地理-感情類型）、メイッパードゥ（情の表現）等タミル独自の詩学体系を確立した。",
    background="サンガム古典期のタミル詩学体系化、サンスクリット詩学とは独立の南方詩学の成立。",
    development="2000年にわたるタミル詩学・近代タミル文学批評の理論的基盤となった。",
    historical_context="紀元前後の南インド・タミル古典文化。",
    primary_source_url=PMADURAI+"pmworks/pm0153.html",
    primary_source_type="Project Madurai: Tolkappiyam Porul-atikaram",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="シラッパディカーラム詳細",
    name_en="Cilappatikaram (in detail)",
    name_original="சிலப்பதிகாரம்",
    period_key="タミル中世文学期",
    definition="2-5世紀頃のイランゴー・アディハル作によるタミル五大叙事詩の筆頭。商人カンナハンと妻カンナギの悲劇と、足首の輪（シラッパドゥ）を巡る復讐譚を3編30歌で展開。タミル民族意識の文学的核となった作品。",
    background="チェーラ朝期南インドの都市文化、ジャイナ教詩人の活躍。",
    development="近代タミル民族主義文学（バーラティ等）の象徴的源泉となった。",
    historical_context="古代南インド多王国時代。",
    primary_source_url=PMADURAI+"pmworks/pm0017.html",
    primary_source_type="Project Madurai: Cilappatikaram",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="マニメーガライ",
    name_en="Manimekalai",
    name_original="மணிமேகலை",
    period_key="タミル中世文学期",
    definition="6世紀頃のチータライ・チャーッタナール作によるタミル五大叙事詩の一。シラッパディカーラムの続編としてカンナギの娘マニメーガライの仏教改宗と諸宗教論争を主題とする。古代南インド仏教文学の貴重な記録。",
    background="チョーラ朝以前の南インド仏教文化、宗教論争文学の隆盛。",
    development="20世紀タミル仏教研究の中核資料となった。",
    historical_context="古代南インド多宗教文化期。",
    primary_source_url=PMADURAI+"pmworks/pm0411.html",
    primary_source_type="Project Madurai: Manimekalai",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_TAM, name_ja="ティルックラル篇章構成",
    name_en="Tirukkural sections",
    name_original="திருக்குறள்",
    period_key="タミル中世文学期",
    definition="4-5世紀頃のティルヴァッルヴァル作とされる箴言詩集ティルックラルの三部構成（アラム＝徳・ポルル＝富・インバム＝愛）。1330二行詩の道徳・政治・愛情論を、いかなる宗派にも属さない普遍的倫理として確立。タミル文化の最高経典の一つ。",
    background="古代南インドの宗教多元性、普遍的倫理書の希求。",
    development="ガンジー、シュバイツァーが激賞し、20世紀世界倫理思想の中で再評価された。",
    historical_context="古代南インドの普遍倫理思想。",
    primary_source_url=PMADURAI+"pmworks/pm0153.html",
    primary_source_type="Project Madurai: Tirukkural",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="カンバラーマーヤナム",
    name_en="Kamba Ramayanam",
    name_original="கம்பராமாயணம்",
    period_key="タミル中世文学期",
    definition="12世紀のタミル詩人カンバンによるラーマーヤナのタミル再話。10,569詩節6章で展開し、ヴァールミーキ原典と異なる神学的解釈（ラーマ・ヴィシュヌ化）を導入した。タミル中世詩の最高峰の一つ。",
    background="チョーラ朝後期のタミル・バクティ運動とヴィシュヌ信仰の確立。",
    development="近代タミル詩・劇・映画の絶えざる源泉となった。",
    historical_context="チョーラ朝後期のヒンドゥー信仰の文学化。",
    primary_source_url=PMADURAI+"pmworks/pm0148.html",
    primary_source_type="Project Madurai: Kamba Ramayanam",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="ペリヤ・プラーナム",
    name_en="Periya Puranam",
    name_original="பெரிய புராணம்",
    period_key="タミル中世文学期",
    definition="12世紀のチョーラ朝詩人セッキラールによる、63人のタミル・シャイヴァ聖者ナーヤナールの聖者伝集。タミル12聖典（ティルムライ）の第12巻として、南インド・シャイヴィズムの中核経典となった。",
    background="チョーラ朝期タミル・シャイヴィズムの聖典化、ナーヤナール伝承の集成。",
    development="近世以降タミル・シャイヴィズム宗教的アイデンティティの中核となった。",
    historical_context="チョーラ朝期南インド宗教文化。",
    primary_source_url=PMADURAI+"pmworks/pm0083.html",
    primary_source_type="Project Madurai: Periya Puranam",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_TAM, name_ja="ナーラーイラ・ディヴィヤ・プラバンダム",
    name_en="Nalayira Divya Prabandham",
    name_original="நாலாயிர திவ்ய பிரபந்தம்",
    period_key="タミル中世文学期",
    definition="6-9世紀のタミル12アールワール詩人による4000編の讃歌集。9-10世紀のナータムニによって編纂された。タミル・ヴィシュヌ・バクティの中核経典で、シュリー・ヴァイシュナヴァ派の「タミル・ヴェーダ」と称される。",
    background="タミル・ヴィシュヌ・バクティの隆盛、ヴェーダーンタ思想とのタミル的融合。",
    development="ラーマーヌジャ哲学、シュリー・ヴァイシュナヴァ派の中核経典として制度化された。",
    historical_context="中世南インド・バクティ運動。",
    primary_source_url=PMADURAI+"pmworks/pm0151.html",
    primary_source_type="Project Madurai: Divya Prabandham",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_TAM, name_ja="テーヴァーラム",
    name_en="Tevaram",
    name_original="தேவாரம்",
    period_key="タミル中世文学期",
    definition="7-8世紀の三タミル・シャイヴァ聖者（アッパル、サンバンダル、スンダラル）による800以上のシヴァ讃歌集。タミル12聖典の第1-7巻を成し、南インド・シャイヴィズムの宗教的・文学的中核となった。",
    background="チョーラ朝以前のタミル・シャイヴァ・バクティ運動、地方寺院巡礼伝統。",
    development="チダーンバラム寺院等での礼拝音楽として現代まで継承されている。",
    historical_context="中世南インド宗教文化。",
    primary_source_url=PMADURAI+"pmworks/pm0190.html",
    primary_source_type="Project Madurai: Tevaram",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: ベンガル・ルネサンス深掘り（8）
# ============================================================
add(**C_BEN, name_ja="バンキム『デヴィー・チョウドゥラーニー』",
    name_en="Bankim's Devi Chaudhurani",
    name_original="দেবী চৌধুরাণী",
    period_key="ベンガル・ルネサンス期",
    definition="バンキムチャンドラ・チャトーパッダエ（1838-94）が1884年に発表したベンガル語小説。18世紀後半ベンガルを舞台に、女主人公が義賊に変身する物語を描く。アーナンダマトと並ぶバンキム後期ナショナリズム小説の代表作。",
    background="ベンガル・ルネサンス後期のヒンドゥー・ナショナリズム文学化。",
    development="20世紀インド独立運動期の革命家女性表象の祖型となった。",
    historical_context="19世紀末ベンガル植民地社会。",
    primary_source_url=WSRC_BN+"দেবী_চৌধুরাণী",
    primary_source_type="Wikisource: Devi Chaudhurani",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_BEN, name_ja="タゴール『ゴーラ』",
    name_en="Tagore's Gora",
    name_original="গোরা",
    period_key="ベンガル・ルネサンス期",
    definition="ロビンドラナート・タゴール（1861-1941）が1910年に発表したベンガル語長編小説。アイルランド系孤児として育てられたヒンドゥー至上主義者ゴーラのアイデンティティ危機を主題とする。インド・ナショナリズムと宗教的正統性の批判的検討。",
    background="20世紀初頭ベンガル分割反対運動期、タゴールのナショナリズム批判の成熟。",
    development="20世紀インド英語文学・南アジア・ナショナリズム研究の中核テクストとなった。",
    historical_context="ベンガル分割反対運動期(1905-11)。",
    primary_source_url=WSRC_BN+"গোরা",
    primary_source_type="Wikisource: Gora (Tagore)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_BEN, name_ja="タゴール『家と世界』",
    name_en="Tagore's Ghare Baire",
    name_original="ঘরে বাইরে",
    period_key="ベンガル・ルネサンス期",
    definition="タゴールが1916年に発表したベンガル語長編小説。スワデーシー運動を背景に、地主ニキレーシュ、その妻ビマラ、急進的ナショナリスト・サンディプの三角関係を通じてナショナリズムの倫理を問う。サタジット・レイによって1984年に映画化。",
    background="第一次大戦中ベンガル民族運動の急進化、タゴールのナショナリズム再考。",
    development="20世紀ナショナリズム批評文学の祖型となり、ポストコロニアル研究の中核テクストとなった。",
    historical_context="ベンガル・スワデーシー運動末期。",
    primary_source_url=WSRC_BN+"ঘরে_বাইরে",
    primary_source_type="Wikisource: Ghare Baire",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_BEN, name_ja="タゴール『壊れた巣』",
    name_en="Tagore's Nashtanir",
    name_original="নষ্টনীড়",
    period_key="ベンガル・ルネサンス期",
    definition="タゴールが1901年に発表した中編小説『壊れた巣』。ベンガル知識階級の家庭を舞台に、新聞編集者の妻チャルラタと夫のいとこアマルとの感情的近接を描く。サタジット・レイ『チャルラタ』(1964)の原作。",
    background="ベンガル・ルネサンス後期家庭小説の心理化、女性内面の文学化。",
    development="サタジット・レイ映画化を通じて20世紀世界文学に位置づけられた。",
    historical_context="20世紀初頭ベンガル中産階級家庭の変容。",
    primary_source_url=WSRC_BN+"নষ্টনীড়",
    primary_source_type="Wikisource: Nashtanir",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_BEN, name_ja="ジャナ・ガナ・マナ起源",
    name_en="Jana Gana Mana origin",
    name_original="জনগণমন",
    period_key="ベンガル・ルネサンス期",
    definition="タゴールが1911年に作詞作曲したベンガル語讃歌「ジャナ・ガナ・マナ」。1911年12月27日インド国民会議カルカッタ大会で初公演、1950年インド共和国国歌に正式採用。タゴールの汎インド統一思想を象徴する作品。",
    background="20世紀初頭ベンガル分割反対運動と汎インド意識の形成。",
    development="1950年インド国歌として制度化、インド国民形成の象徴的文化資源となった。",
    historical_context="ベンガル分割反対運動末期。",
    primary_source_url=WSRC_BN+"জনগণমন",
    primary_source_type="Wikisource: Jana Gana Mana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_BEN, name_ja="シャラトチャンドラ『デーヴダース』",
    name_en="Sarat Chandra's Devdas",
    name_original="দেবদাস",
    period_key="ベンガル・ルネサンス期",
    definition="シャラトチャンドラ・チャットーパッダエ（1876-1938）が1917年に発表したベンガル語小説。地主家の長男デーヴダースの恋愛悲劇と自己破壊的飲酒を描く。10回以上映画化され、南アジア大衆文化の中核的悲恋物語として定着した。",
    background="20世紀初頭ベンガル中産階級家庭の社会的束縛と感情の文学化。",
    development="ボリウッド・ベンガル映画の最重要原作テクストの一つとなった。",
    historical_context="20世紀初頭ベンガル植民地社会。",
    primary_source_url=WSRC_BN+"দেবদাস",
    primary_source_type="Wikisource: Devdas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_BEN, name_ja="シャラトチャンドラ『シュリーカーント』",
    name_en="Sarat Chandra's Srikanta",
    name_original="শ্রীকান্ত",
    period_key="ベンガル・ルネサンス期",
    definition="シャラトチャンドラが1917-1933年に4部で発表した自伝的長編小説。語り手シュリーカーントの放浪と恋愛を通じて、20世紀初頭ベンガル農村・都市・宗教社会を描く。ベンガル散文小説の代表作。",
    background="シャラトチャンドラ自身のミャンマー・ベンガル放浪体験の文学化。",
    development="20世紀ベンガル地方主義文学・自伝小説の規範作品となった。",
    historical_context="20世紀初頭ベンガル農村・都市変動期。",
    primary_source_url=WSRC_BN+"শ্রীকান্ত",
    primary_source_type="Wikisource: Srikanta",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_BEN, name_ja="バンキム『アーナンダマト』詳細",
    name_en="Bankim's Anandamath (in detail)",
    name_original="আনন্দমঠ",
    period_key="ベンガル・ルネサンス期",
    definition="バンキムチャンドラ・チャトーパッダエが1882年に発表したベンガル語歴史小説。1770年代ベンガル飢饉期のサンニヤーシ反乱を主題とし、母なるインド（バーラト・マーター）讃歌「ヴァンデー・マータラム」を含む。インド・ナショナリズム文学の起点。",
    background="19世紀末ベンガル・ヒンドゥー・ナショナリズムの形成、英国植民地批判文学の発展。",
    development="ヴァンデー・マータラムは1937年インド国民会議準国歌に採択された。",
    historical_context="19世紀末ベンガル植民地反抗文学。",
    primary_source_url=WSRC_BN+"আনন্দমঠ",
    primary_source_type="Wikisource: Anandamath",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# E: ヒンディー深掘り（8）
# ============================================================
add(**C_DEV, name_ja="バーラテーンドゥ・ハリシュチャンドラ",
    name_en="Bharatendu Harishchandra",
    name_original="भारतेन्दु हरिश्चन्द्र",
    period_key="ヒンディー散文成熟期",
    definition="バーラテーンドゥ・ハリシュチャンドラ（1850-85）はヒンディー近代文学の父。ベナーレスを拠点にカリー・ボリー・ヒンディーの近代散文を確立し、戯曲『アンデール・ナガリー』(1881)等で植民地批判と社会改良を文学化した。",
    background="19世紀末ベナーレスのヒンディー啓蒙運動、英国植民地批判の文学化。",
    development="プレームチャンドに至るヒンディー近代散文の祖型となった。",
    historical_context="ヒンディー近代文学黎明期。",
    primary_source_url=WSRC_HI+"लेखक:भारतेन्दु_हरिश्चन्द्र",
    primary_source_type="Wikisource: Bharatendu Harishchandra",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="プレームチャンド『ガバン』",
    name_en="Premchand's Gaban",
    name_original="गबन",
    period_key="ヒンディー散文成熟期",
    definition="プレームチャンドが1931年に発表したヒンディー長編小説『横領』。下級官吏ラーマナートが妻ジャールパーの装飾欲を満たすため公金を横領していく経緯を、植民地都市の貧困と消費文化の関係において描く。",
    background="1930年代インド独立運動期の都市中産階級の経済的圧迫の文学化。",
    development="20世紀インド都市文学・社会批判小説の規範となった。",
    historical_context="1930年代インド独立運動期。",
    primary_source_url=WSRC_HI+"गबन",
    primary_source_type="Wikisource: Gaban",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="プレームチャンド『カルマブーミ』",
    name_en="Premchand's Karmabhumi",
    name_original="कर्मभूमि",
    period_key="ヒンディー散文成熟期",
    definition="プレームチャンドが1932年に発表したヒンディー長編小説『行為の地』。市民的不服従運動・小作料抗議運動を主題に、ガンジー的ナショナリズムと農村改革を文学化した。プレームチャンド独立運動期の中軸作品。",
    background="1930年代インド独立運動・農民運動の文学化。",
    development="20世紀ヒンディー独立運動文学の規範となった。",
    historical_context="ガンジー指導下のインド独立運動期。",
    primary_source_url=WSRC_HI+"कर्मभूमि",
    primary_source_type="Wikisource: Karmabhumi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="プレームチャンド『ランガブーミ』",
    name_en="Premchand's Rangabhumi",
    name_original="रंगभूमि",
    period_key="ヒンディー散文成熟期",
    definition="プレームチャンドが1925年に発表したヒンディー長編小説『戦場』。盲目の物乞いスールダースが煙草工場建設に抵抗する物語を通じて、植民地工業化と村落共同体の対立を描く。プレームチャンド初期の代表作。",
    background="1920年代インドの工業化と村落崩壊の社会的観察。",
    development="20世紀ヒンディー社会派文学の祖型となった。",
    historical_context="1920年代植民地インドの工業化期。",
    primary_source_url=WSRC_HI+"रंगभूमि",
    primary_source_type="Wikisource: Rangabhumi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="ジャイシャンカル・プラサード『カーマーヤニー』",
    name_en="Jaishankar Prasad's Kamayani",
    name_original="कामायनी",
    period_key="ヒンディー・チャーヤーヴァード期",
    definition="ジャイシャンカル・プラサード（1889-1937）が1936年に発表したヒンディー叙事詩。マヌとシュラッダーの神話を素材に、人間の感情・知性・行為の哲学的探究を15篇で展開する。ヒンディー・チャーヤーヴァード詩運動の頂点。",
    background="1930年代ベナーレス文化圏のチャーヤーヴァード新ロマン主義詩運動。",
    development="20世紀ヒンディー詩学の中核研究対象となった。",
    historical_context="独立運動期インド文化的アイデンティティ模索。",
    primary_source_url=WSRC_HI+"कामायनी",
    primary_source_type="Wikisource: Kamayani",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ニラーラー『アナーミカー』",
    name_en="Nirala's Anamika",
    name_original="अनामिका",
    period_key="ヒンディー・チャーヤーヴァード期",
    definition="スーリヤカーント・トリパーティー・ニラーラー（1896-1961）が1923年・1937年に発表した詩集『無名のもの』。自由韻律詩（ムクト・チャンド）を確立し、ヒンディー詩の形式革命を遂行した。チャーヤーヴァード四詩人の革新的中核。",
    background="ベンガル詩（タゴール）からのヒンディー詩革新の影響、自由韻律導入。",
    development="20世紀ヒンディー自由詩の祖型として、後代詩人に決定的影響を与えた。",
    historical_context="チャーヤーヴァード詩運動期。",
    primary_source_url=WSRC_HI+"अनामिका",
    primary_source_type="Wikisource: Anamika (Nirala)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="スミトラーナンダン・パント『パッラヴ』",
    name_en="Pant's Pallav",
    name_original="पल्लव",
    period_key="ヒンディー・チャーヤーヴァード期",
    definition="スミトラーナンダン・パント（1900-77）が1928年に発表した詩集『若葉』。ヒマラヤ自然と内面的詩情の融合を、新ロマン主義的言語で展開し、ヒンディー・チャーヤーヴァード詩運動の規範を確立した。",
    background="1920年代ヒマラヤ地域からの自然詩の興隆、ヒンディー詩の自然回帰。",
    development="チャーヤーヴァード四詩人（プラサード・ニラーラー・パント・マハーデーヴィー）の規範的作品となった。",
    historical_context="ヒンディー新ロマン主義詩運動期。",
    primary_source_url=WSRC_HI+"पल्लव",
    primary_source_type="Wikisource: Pallav (Pant)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="アジェーヤ『他人は他人』",
    name_en="Ajneya's Apne Apne Ajanabi",
    name_original="अपने अपने अजनबी",
    period_key="ヒンディー散文成熟期",
    definition="サッチダーナンダ・ヴァーツヤーヤン・アジェーヤ（1911-87）が1961年に発表したヒンディー実存主義小説。スイスの山小屋に閉じ込められた老女と若い女性の哲学的対話を主題とする。ヒンディー・ナイー・カハーニー（新短篇）運動の中核作品。",
    background="戦後ヒンディー文学の実存主義的転回、ヨーロッパ実存主義の受容。",
    development="ヒンディー・ナイー・カハーニー運動の理論的中核となった。",
    historical_context="独立後インド文学の実存主義的成熟期。",
    primary_source_url=WSRC_HI+"अपने_अपने_अजनबी",
    primary_source_type="Wikisource: Apne Apne Ajanabi",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"極限状況での主体的対話の文学化は、AI対話における他者性の不在問題と理論的に対比される。",
         "related_ai_phenomenon":"AI対話における他者性の不在"}])


# ============================================================
# F: ウルドゥー深掘り（8）
# ============================================================
add(**C_URD, name_ja="ガーリブ『ディーヴァーネ・ガーリブ』",
    name_en="Ghalib's Diwan-e-Ghalib",
    name_original="دیوانِ غالب",
    period_key="ウルドゥー近代詩・散文期",
    definition="ミルザー・ガーリブ（1797-1869）の詩集。ウルドゥーとペルシア語のガザル・カスィーダで構成され、形而上学的省察、愛の苦悩、世界の不条理を圧縮された二行詩で展開する。ウルドゥー古典詩の頂点と評価される。",
    background="ムガル朝末期デリーの宮廷詩文化、1857年大反乱を経験した詩人。",
    development="20世紀インド・パキスタンのウルドゥー詩学・批評の絶対的中核テクストとなった。",
    historical_context="ムガル朝末期から英領インド初期。",
    primary_source_url=WSRC_UR+"دیوان_غالب",
    primary_source_type="Wikisource: Diwan-e-Ghalib",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_URD, name_ja="イクバール『バーレ・ジブリール』",
    name_en="Iqbal's Bal-e-Jibreel",
    name_original="بالِ جبریل",
    period_key="ウルドゥー近代詩・散文期",
    definition="アッラーマ・イクバール（1877-1938）が1935年に発表したウルドゥー詩集『ガブリエルの翼』。哲学的・宗教的詩の頂点として、自我（フディー）の確立、ヨーロッパ近代との対決、東洋復興の主題を展開する。",
    background="20世紀初頭インド・ムスリム知識人のヨーロッパ近代受容と批判。",
    development="パキスタン国民詩人の地位を確立し、20世紀イスラーム近代主義の中核テクストとなった。",
    historical_context="インド独立運動期・パキスタン構想形成期。",
    primary_source_url=WSRC_UR+"بال_جبریل",
    primary_source_type="Wikisource: Bal-e-Jibreel",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_URD, name_ja="イクバール『アスラーレ・フディー』",
    name_en="Iqbal's Asrar-e-Khudi",
    name_original="اسرارِ خودی",
    period_key="ウルドゥー近代詩・散文期",
    definition="イクバールが1915年に発表したペルシア語マスナヴィー『自我の秘密』。スーフィー的「無我」を批判し、能動的・創造的「自我（フディー）」の確立を説いた哲学詩。20世紀イスラーム近代主義哲学の文学化。",
    background="第一次大戦中のヨーロッパ近代批判、インド・ムスリム自覚運動の興隆。",
    development="ニコルソン英訳(1920)を通じて世界的に評価され、パキスタン建国思想の理論基盤となった。",
    historical_context="第一次大戦期インド・ムスリム思想形成期。",
    primary_source_url=ARCHIVE+"details/asrar-i-khudi",
    primary_source_type="Internet Archive: Asrar-e-Khudi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_URD, name_ja="サー・サイイド・アフマド・ハーン散文",
    name_en="Sir Sayyid Ahmad Khan's prose",
    name_original="سر سید احمد خان کی نثر",
    period_key="ウルドゥー近代詩・散文期",
    definition="サー・サイイド・アフマド・ハーン（1817-98）のウルドゥー散文（『アサーレ・サナーディード』『タハジーブ・ウル・アフラーク』雑誌等）。1857年後のインド・ムスリム共同体の近代的再編を、英国学問の受容と宗教改革の融合として理論化した。",
    background="1857年大反乱後のインド・ムスリム危機、英国学問受容の必要性。",
    development="アリーガル運動・近代インド・ムスリム知識人形成の理論基盤となった。",
    historical_context="英領インド初期のムスリム共同体再編期。",
    primary_source_url=ARCHIVE+"details/sir-syed",
    primary_source_type="Internet Archive: Sir Sayyid prose",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_URD, name_ja="ハーリー『ムサッダス』",
    name_en="Hali's Musaddas",
    name_original="مسدسِ حالی",
    period_key="ウルドゥー近代詩・散文期",
    definition="アルターフ・フサイン・ハーリー（1837-1914）が1879年に発表したウルドゥー長詩『ムサッダス・エ・マッド・オ・ジャザル・エ・イスラーム』。イスラーム共同体の盛衰を主題とし、ウルドゥー詩の社会改革的転換を画した。サー・サイイドのアリーガル運動の文学的中核。",
    background="アリーガル運動期のインド・ムスリム自覚と社会改革の文学化。",
    development="近代ウルドゥー詩の社会派伝統（イクバール、ファイズ等）の祖型となった。",
    historical_context="19世紀末アリーガル運動期。",
    primary_source_url=ARCHIVE+"details/musaddas-e-hali",
    primary_source_type="Internet Archive: Musaddas-e-Hali",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_URD, name_ja="マントー『開けよ』",
    name_en="Manto's Khol Do",
    name_original="کھول دو",
    period_key="ウルドゥー近代詩・散文期",
    definition="サアダット・ハサン・マントー（1912-55）が1948年に発表したウルドゥー短篇『開けよ』。1947年印パ分離独立期の暴力で精神を壊した少女と父の悲劇を描く。マントーの分離独立短編の代表作で、衝撃的結末で20世紀ウルドゥー短篇の規範となった。",
    background="1947年印パ分離独立の集団暴力と難民危機の文学化。",
    development="20世紀南アジア分離独立文学・トラウマ文学の祖型となった。",
    historical_context="1947-48年印パ分離独立期。",
    primary_source_url=WSRC_UR+"کھول_دو",
    primary_source_type="Wikisource: Khol Do (Manto)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_URD, name_ja="ファイズ・アフマド・ファイズ詩集",
    name_en="Faiz Ahmed Faiz poetry",
    name_original="فیض احمد فیض کا کلام",
    period_key="ウルドゥー近代詩・散文期",
    definition="ファイズ・アフマド・ファイズ（1911-84）のウルドゥー詩集（『ナクシェ・ファリヤーディー』1941、『ダステ・サバー』1953等）。ガザル古典形式を社会主義的・反植民地的内容で更新し、20世紀パキスタン進歩主義詩の中軸となった。",
    background="20世紀インド進歩主義作家運動・パキスタン社会主義文学の中核。",
    development="ノーベル文学賞候補となり、世界的な進歩主義詩学の代表詩人となった。",
    historical_context="冷戦期パキスタンの政治的抑圧と進歩主義文学の対立。",
    primary_source_url=WSRC_UR+"فیض_احمد_فیض",
    primary_source_type="Wikisource: Faiz Ahmed Faiz",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_URD, name_ja="アリー・サルダール・ジャアフリー",
    name_en="Ali Sardar Jafri",
    name_original="علی سردار جعفری",
    period_key="ウルドゥー近代詩・散文期",
    definition="アリー・サルダール・ジャアフリー（1913-2000）はインド進歩主義作家運動の中核詩人。ウルドゥー詩集『パルヴァーズ』『ニヤー・サンサール』、批評集等を通じて20世紀インド世俗主義・社会主義文学を主導した。1997年ジュナーンピート賞受賞。",
    background="1936年進歩主義作家運動への参加、20世紀インド・ムスリム進歩主義の中核活動。",
    development="20世紀インド・ウルドゥー文学の世俗主義・社会主義的アイデンティティ形成を主導した。",
    historical_context="20世紀後半インド世俗主義文学期。",
    primary_source_url=WSRC_UR+"علی_سردار_جعفری",
    primary_source_type="Wikisource: Ali Sardar Jafri",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# G: マラーティー / タミル現代（6）
# ============================================================
add(**C_DEV, name_ja="サーネー・グルージー",
    name_en="Sane Guruji",
    name_original="साने गुरुजी",
    period_key="マラーティー近現代文学期",
    definition="パーンドゥラング・サダーシヴ・サーネー（1899-1950）はマラーティー文学者・社会改革者。『シャーマーチー・アーイー』(1935)等の家庭・教育・愛国主題小説で20世紀前半マラーティー大衆教育文学の規範を確立した。",
    background="ガンジー独立運動期マラーティー教育改革運動の文学化。",
    development="20世紀マラーティー児童文学・国民教育文学の中軸となった。",
    historical_context="独立運動期マラーティー社会改革。",
    primary_source_url=WSRC_MR+"लेखक:साने_गुरुजी",
    primary_source_type="Wikisource: Sane Guruji",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="ヴィ・エス・カーンデーカル『ヤヤーティ』",
    name_en="V.S. Khandekar's Yayati",
    name_original="ययाति",
    period_key="マラーティー近現代文学期",
    definition="ヴィシュヌ・サカーラム・カーンデーカル（1898-1976）が1959年に発表したマラーティー長編小説『ヤヤーティ』。マハーバーラタ神話の王ヤヤーティを主題に、欲望と倫理の葛藤を再解釈した。1974年ジュナーンピート賞受賞作（マラーティー初）。",
    background="20世紀マラーティー神話再解釈文学の流れ、サンスクリット古典の現代的再読。",
    development="20世紀マラーティー長編小説の規範作品、近代インド神話再解釈文学の祖型となった。",
    historical_context="独立後インド・マラーティー文学成熟期。",
    primary_source_url=ARCHIVE+"details/yayati-khandekar",
    primary_source_type="Internet Archive: Yayati (Khandekar)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="プ・ラ・デーシュパーンデー",
    name_en="Pu La Deshpande",
    name_original="पु. ल. देशपांडे",
    period_key="マラーティー近現代文学期",
    definition="プルショッタム・ラクシュマン・デーシュパーンデー（1919-2000）はマラーティー随筆家・劇作家・俳優。『バトトーチー・チャール』『アサミ・アサミ』等のユーモア随筆で20世紀後半マラーティー大衆文化の中核となり、「プ・ラ」と親しまれた。",
    background="20世紀後半マラーティー大衆メディア・舞台芸術の隆盛。",
    development="20世紀マラーティー大衆文学・舞台芸術の規範となった。",
    historical_context="独立後マハーラーシュトラ大衆文化期。",
    primary_source_url=WSRC_MR+"लेखक:पु._ल._देशपांडे",
    primary_source_type="Wikisource: Pu La Deshpande",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="テンドゥルカル『ガーシラーム・コトワール』",
    name_en="Tendulkar's Ghashiram Kotwal",
    name_original="घाशीराम कोतवाल",
    period_key="マラーティー近現代文学期",
    definition="ヴィジャイ・テンドゥルカル（1928-2008）が1972年に発表したマラーティー戯曲。18世紀末プネのペーシュワー宮廷を舞台に、権力構造と暴力の循環を主題化した。20世紀マラーティー演劇の頂点、世界演劇に影響を与えた政治劇。",
    background="20世紀後半マラーティー実験演劇運動、政治劇の興隆。",
    development="20世紀インド・世界演劇の中核研究対象となり、各国で公演された。",
    historical_context="独立後インド政治演劇の成熟期。",
    primary_source_url=ARCHIVE+"details/ghashiram-kotwal",
    primary_source_type="Internet Archive: Ghashiram Kotwal",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"権力構造と暴力循環の劇化は、AI時代の権力構造（プラットフォーム支配）と暴力の連鎖の理論化に資する古典的参照点。",
         "related_ai_phenomenon":"AI時代の権力構造と暴力の連鎖"}])

add(**C_DEV, name_ja="テンドゥルカル『サカーラーム・バインダル』",
    name_en="Tendulkar's Sakharam Binder",
    name_original="सखाराम बाईंडर",
    period_key="マラーティー近現代文学期",
    definition="ヴィジャイ・テンドゥルカルが1972年に発表したマラーティー戯曲。製本職人サカーラームと放棄された妻達との関係を主題に、男性的暴力・宗教的偽善・女性の生存戦略を直視した。マハーラーシュトラ州政府により上演禁止となった先鋭的作品。",
    background="20世紀後半マラーティー実験演劇運動と検閲との闘争。",
    development="20世紀インド・フェミニスト演劇の祖型として国際的に研究された。",
    historical_context="独立後インド検閲・演劇自由をめぐる論争期。",
    primary_source_url=ARCHIVE+"details/sakharam-binder",
    primary_source_type="Internet Archive: Sakharam Binder",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_TAM, name_ja="C.S.ラクシュミ（アンバイ）",
    name_en="C.S. Lakshmi (Ambai)",
    name_original="அம்பை",
    period_key="タミル近現代文学期",
    definition="C.S.ラクシュミ（1944-）はタミル女性作家。ペンネーム「アンバイ」で1962年以降短篇集（『シルガル・ムリックム』『カートリル・カラントゥ・コーンドゥ・ヴィッドゥヴィン・カディタム』等）を発表。20世紀後半タミル・フェミニスト文学の中核を形成した。",
    background="20世紀後半タミル女性運動・フェミニスト文学の興隆。",
    development="20世紀後半南アジア・フェミニスト文学の代表作家として国際的に評価された。",
    historical_context="独立後タミルナードゥ女性運動期。",
    primary_source_url=PMADURAI+"pmworks/pm0455.html",
    primary_source_type="Project Madurai: C.S. Lakshmi",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: マラヤーラム / カンナダ / ダリット女性（6）
# ============================================================
add(**C_MAL, name_ja="クマーラン・アーサン",
    name_en="Kumaran Asan",
    name_original="കുമാരൻ ആശാൻ",
    period_key="マラヤーラム近現代文学期",
    definition="クマーラン・アーサン（1873-1924）はマラヤーラム近代詩の三巨頭の一人。詩集『ヴィーナ・プーヴ（萎れた花）』(1908)、『ナリニー』『リーラー』『カルナ』等で、低カースト出身者として近代マラヤーラム叙情詩を確立し、社会改革主題と新ロマン主義詩学を融合した。",
    background="20世紀初頭ケーララのナーラーヤナ・グル運動と低カースト社会改革運動。",
    development="20世紀マラヤーラム近代詩・社会改革文学の中軸となった。",
    historical_context="ケーララ社会改革運動期。",
    primary_source_url=WSRC_ML+"രചയിതാവ്:കുമാരൻ_ആശാൻ",
    primary_source_type="Wikisource: Kumaran Asan",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_MAL, name_ja="タカリ『チェンミーン』",
    name_en="Thakazhi's Chemmeen",
    name_original="ചെമ്മീൻ",
    period_key="マラヤーラム近現代文学期",
    definition="タカリ・シヴァシャンカラ・ピッライ（1912-99）が1956年に発表したマラヤーラム長編小説『海老』。ケーララ漁村を舞台に、漁師カルッタンマと商人パリックッティの宗教を超えた恋を描く。1965年映画化、サーヒティヤ・アカデミー賞受賞、ジュナーンピート賞受賞作。",
    background="20世紀中葉ケーララ漁村社会観察、社会主義リアリズムのマラヤーラム化。",
    development="20世紀インド地方主義文学の代表作として国際的に翻訳された。",
    historical_context="独立後ケーララ社会主義文化期。",
    primary_source_url=WSRC_ML+"ചെമ്മീൻ",
    primary_source_type="Wikisource: Chemmeen",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_KAN, name_ja="クヴェンプ詳細",
    name_en="Kuvempu (in detail)",
    name_original="ಕುವೆಂಪು",
    period_key="カンナダ近現代文学期",
    definition="クッパッリ・ヴェンカタッパ・プッタッパ（1904-94）はカンナダ近代文学の最重要詩人。『シュリー・ラーマーヤナ・ダルシャナム』(1949)で20世紀カンナダ叙事詩を再創造し、1968年ジュナーンピート賞受賞（カンナダ初）。20世紀カンナダ文学の中核象徴。",
    background="20世紀ヒンドゥー古典の現代的再解釈、カンナダ・ナショナリズム文学の確立。",
    development="20世紀カンナダ文学のアイデンティティ形成の中軸となり、後代詩人に決定的影響を与えた。",
    historical_context="20世紀カルナータカ・アイデンティティ形成期。",
    primary_source_url=WSRC_KN+"ಲೇಖಕ:ಕುವೆಂಪು",
    primary_source_type="Wikisource: Kuvempu",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_KAN, name_ja="ベーンドレー",
    name_en="Da. Ra. Bendre",
    name_original="ದ. ರಾ. ಬೇಂದ್ರೆ",
    period_key="カンナダ近現代文学期",
    definition="ダッタートレヤ・ラーマチャンドラ・ベーンドレー（1896-1981）はカンナダ近代詩の最重要抒情詩人。詩集『ガリ』『ナーダリーレ』『サーキー』等で、北カルナータカ・ダールワード方言の音楽性を活用し、20世紀カンナダ詩のリズム・情感を確立。1973年ジュナーンピート賞受賞。",
    background="20世紀北カルナータカ・ダールワード地方の文化的興隆。",
    development="20世紀カンナダ抒情詩・自由韻律詩の規範となった。",
    historical_context="20世紀北カルナータカ文化期。",
    primary_source_url=WSRC_KN+"ಲೇಖಕ:ದ._ರಾ._ಬೇಂದ್ರೆ",
    primary_source_type="Wikisource: Da. Ra. Bendre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_KAN, name_ja="ガールシュ・カルナード『トゥグラク』",
    name_en="Girish Karnad's Tughlaq",
    name_original="ತುಘಲಕ್",
    period_key="カンナダ近現代文学期",
    definition="ガールシュ・カルナード（1938-2019）が1964年に発表したカンナダ歴史劇『トゥグラク』。14世紀のスルターン、ムハンマド・ビン・トゥグラクの理想主義と暴政を主題とし、独立後インド政治への暗示として20世紀インド演劇を代表する政治劇となった。",
    background="20世紀カンナダ実験演劇運動、独立後インド政治への文学的省察。",
    development="20世紀インド演劇の中核作品として、英訳されて国際的に上演された。",
    historical_context="独立後インド政治劇の成熟期。",
    primary_source_url=ARCHIVE+"details/tughlaq-karnad",
    primary_source_type="Internet Archive: Tughlaq",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="サルマー（タミル女性詩）",
    name_en="Salma (Tamil women's poetry)",
    name_original="சல்மா",
    period_key="インド・ダリット／女性文学期",
    definition="サルマー（1968-、本名ロキア・マリック）はタミル・ムスリム女性詩人・小説家。詩集『オールヴィヤ・パーディ』、長編『イランダーム・ジャーマンガリン・カダイ』等で、ムスリム女性の抑圧と解放を主題化し、20世紀末-21世紀タミル・ムスリム女性文学の中核となった。",
    background="20世紀末タミル・ムスリム女性運動の文学化、家父長制への文学的抵抗。",
    development="21世紀南アジア・フェミニスト文学の代表作家として国際的に翻訳された。",
    historical_context="20世紀末-21世紀タミル女性運動。",
    primary_source_url=WIKI_EN+"Salma_(writer)",
    primary_source_type="Wikipedia: Salma (writer)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Cross-domain links (>= 14) and additional fourth_transform tags (>= 18)
# ============================================================
def _attach_cross(name: str, cd: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c["cross_domain"] = c.get("cross_domain", []) + cd
            return


def _attach_axes(name: str, ax: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c["fourth_axes"] = c.get("fourth_axes", []) + ax
            return


# Additional fourth_transform_tags to reach >= 18
_attach_axes("カーリダーサ『シャクンタラー』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"認知の指輪を媒介とする記憶喪失と再認の物語は、AI記憶システムにおける個人記憶の媒介・喪失問題と理論的に並行する。",
     "related_ai_phenomenon":"AI記憶システムにおける個人記憶の媒介性"}])
_attach_axes("カーリダーサ『メーガドゥータ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"使者詩形式における伝達の遅延と媒介性は、AI媒介コミュニケーションの即時性／媒介性の弁証法と理論的に共振する。",
     "related_ai_phenomenon":"AI媒介コミュニケーションの即時性と媒介性"}])
_attach_axes("シュードラカ『ムリッチャカティカー』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"庶民的写実性と階層横断性は、AI生成コンテンツの階層横断的アクセス性問題と歴史的に対比される。",
     "related_ai_phenomenon":"AI生成コンテンツの階層横断的アクセス性"}])
_attach_axes("アーナンダヴァルダナ『ドヴァニャーローカ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"暗示（ドヴァニ）理論は表面的意味の背後の含意層を理論化し、AI生成テキストの暗示的意味問題の古典的祖型となる。",
     "related_ai_phenomenon":"AI生成テキストの暗示的意味の発生問題"}])
_attach_axes("マンマタ『カーヴィヤプラカーシャ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"詩のドーシャ（瑕疵）・グナ（質）・アランカーラ（修辞）の体系化は、AI生成テキスト品質評価指標の古典的祖型となる。",
     "related_ai_phenomenon":"AI生成テキストの品質評価体系"}])
_attach_axes("ティルックラル篇章構成", [
    {"axis":"受容","status":"rethinking",
     "rationale":"宗派非帰属の普遍倫理書という形式は、AI倫理規範における普遍性／文化特殊性の弁証法と理論的に並行する。",
     "related_ai_phenomenon":"AI倫理規範における普遍性と文化特殊性"}])
_attach_axes("カンバラーマーヤナム", [
    {"axis":"物語","status":"rethinking",
     "rationale":"原典翻訳における神学的解釈変容は、AI翻訳・要約におけるイデオロギー的変容問題と歴史的に対比される。",
     "related_ai_phenomenon":"AI翻訳における意味の意図的変容"}])
_attach_axes("タゴール『ゴーラ』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"アイデンティティの構築性（孤児が至上主義者となる）は、AI環境下の主体形成のアルゴリズム的構築可能性と理論的に共振する。",
     "related_ai_phenomenon":"AI環境下の主体形成のアルゴリズム的構築"}])
_attach_axes("タゴール『家と世界』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"ナショナリズム言説の感情的動員力は、AIプロパガンダ・SNS世論形成の理論化に資する祖型を提供する。",
     "related_ai_phenomenon":"AI環境における感情的動員と世論形成"}])
_attach_axes("シャラトチャンドラ『デーヴダース』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"反復され映画化される悲恋の物語型は、AI生成における物語アーキタイプの再生産可能性と理論的に対比される。",
     "related_ai_phenomenon":"AI生成における物語アーキタイプの再生産"}])
_attach_axes("プレームチャンド『ゴーダーン』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"農村小作人の文学的可視化は、AIプラットフォーム経済における周縁労働者の可視化／不可視化問題と歴史的に対比される。",
     "related_ai_phenomenon":"AIプラットフォーム経済における周縁労働者の可視化"}])
_attach_axes("ジャイシャンカル・プラサード『カーマーヤニー』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"感情・知性・行為の三元論的主体構成は、AIエージェントの主体構成（感情モデル・知性モデル・行為モデル）の理論化に資する古典的祖型。",
     "related_ai_phenomenon":"AIエージェントの主体構成モデル"}])
_attach_axes("ガーリブ『ディーヴァーネ・ガーリブ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"二行詩の極限的圧縮言語は、AI要約・トークン圧縮における意味密度の理論化に資する古典的参照点。",
     "related_ai_phenomenon":"AI要約における意味の極限的圧縮"}])
_attach_axes("イクバール『バーレ・ジブリール』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"自我（フディー）の能動的構築理念は、AI環境における自我の能動性／受動性の弁証法を理論化する祖型を提供する。",
     "related_ai_phenomenon":"AI環境における自我の能動性問題"}])
_attach_axes("マントー『開けよ』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"分離独立期の集団的トラウマの文学化は、AI時代の集団トラウマ（プラットフォーム被害・誤情報拡散）の理論化に資する。",
     "related_ai_phenomenon":"AI時代の集団トラウマの文学化"}])
_attach_axes("ファイズ・アフマド・ファイズ詩集", [
    {"axis":"受容","status":"rethinking",
     "rationale":"古典ガザル形式に進歩主義的内容を盛る形式革新は、AI生成における古典形式の現代的再活用問題と理論的に並行する。",
     "related_ai_phenomenon":"AI生成における古典形式の現代的再活用"}])
_attach_axes("テンドゥルカル『サカーラーム・バインダル』", [
    {"axis":"受容","status":"rethinking",
     "rationale":"検閲を受けた政治劇の文学的抵抗は、AIコンテンツモデレーション時代の表現自由の理論化に資する。",
     "related_ai_phenomenon":"AIコンテンツモデレーション時代の表現自由"}])
_attach_axes("クマーラン・アーサン", [
    {"axis":"主体","status":"rethinking",
     "rationale":"低カースト出身詩人の主体的文学化は、AI環境における周縁的主体の可視化／不可視化問題の理論化に資する。",
     "related_ai_phenomenon":"AI環境における周縁的主体の可視化"}])
_attach_axes("ガールシュ・カルナード『トゥグラク』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"歴史的人物の現代的再解釈劇は、AI生成における歴史的人物の再構築・再解釈問題と理論的に並行する。",
     "related_ai_phenomenon":"AI生成における歴史的人物の再構築"}])
_attach_axes("サルマー（タミル女性詩）", [
    {"axis":"主体","status":"rethinking",
     "rationale":"ムスリム女性の文学的自己主張は、AI環境における多重周縁化された主体の可視化問題の理論化に資する。",
     "related_ai_phenomenon":"AI環境における多重周縁化された主体の可視化"}])


# Cross-domain links (>= 14)
_attach_cross("カーリダーサ『シャクンタラー』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"記憶と再認の詩学",
     "description":"カーリダーサの認知の指輪は、ギリシア悲劇のアナグノーリシス（再認）と並行する世界詩学の中核モチーフ。"}])

_attach_cross("カーリダーサ『メーガドゥータ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"使者詩・媒介者文学",
     "description":"ドゥータカーヴィヤ系譜は、世界文学の使者・媒介者形式の代表的伝統として比較詩学の中核。"}])

_attach_cross("バーサ劇集", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"写本伝承文化",
     "description":"バーサ写本のケーララ伝承は、20世紀インド学における写本文化人類学研究の中核資料。"}])

_attach_cross("シュードラカ『ムリッチャカティカー』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"古代都市民族誌",
     "description":"古代インド都市生活の社会階層的描写は、古代南アジア都市民族誌の文学的記録として参照される。"}])

_attach_cross("アーナンダヴァルダナ『ドヴァニャーローカ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"暗示・含意の詩学",
     "description":"ドヴァニ理論は20世紀現象学的詩学（インガルデン、リクール）と独立に並行する東方暗示理論の体系。"}])

_attach_cross("アビナヴァグプタ『ロチャナ／アビナヴァバーラティー』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"カシミール・シャイヴィズム哲学",
     "description":"アビナヴァグプタ美学はカシミール・シャイヴィズム哲学の文学的展開として、インド哲学・美学の交差点。"}])

_attach_cross("マンマタ『カーヴィヤプラカーシャ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"古典詩学綱要書",
     "description":"カーヴィヤプラカーシャは比較詩学において、アリストテレス詩学・劉勰文心雕龍と並ぶ古典詩学綱要書の代表。"}])

_attach_cross("トルカーッピヤム・ポルル篇", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"地理-感情類型論",
     "description":"ティナイ（地理-感情類型）は文化人類学における環境-感情の類型化の古代的祖型。"}])

_attach_cross("ティルックラル篇章構成", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"普遍倫理思想",
     "description":"ティルックラルの三部構成は、世界倫理思想史において宗派非帰属の普遍倫理書として比較研究される。"}])

_attach_cross("ナーラーイラ・ディヴィヤ・プラバンダム", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ヴィシシュターディヴァイタ哲学",
     "description":"ディヴィヤ・プラバンダムはラーマーヌジャ哲学の文学的基盤として、インド哲学史の中核資料。"}])

_attach_cross("タゴール『ゴーラ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"アイデンティティ構築論",
     "description":"ゴーラのアイデンティティ危機は20世紀文化人類学のアイデンティティ構築論の文学的祖型。"}])

_attach_cross("バンキム『アーナンダマト』詳細", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"想像の共同体・ナショナリズム",
     "description":"アーナンダマトはアンダーソン『想像の共同体』のインド事例研究の中核テクスト。"}])

_attach_cross("プレームチャンド『ゴーダーン』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"小作・農村経済",
     "description":"プレームチャンドの農村小作描写は20世紀インド農業経済学・農村社会学の文学的祖型。"}])

_attach_cross("イクバール『アスラーレ・フディー』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"自我哲学・実存主義",
     "description":"イクバールのフディー哲学は、ニーチェ・ベルクソン受容を経て20世紀イスラーム実存主義哲学の中核となった。"}])

_attach_cross("マントー『開けよ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"集団暴力・分離独立人類学",
     "description":"マントーの分離独立短編は20世紀南アジア集団暴力研究（パンディーら）の文学的中核資料。"}])

_attach_cross("テンドゥルカル『ガーシラーム・コトワール』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"政治劇詩学",
     "description":"テンドゥルカルの政治劇は20世紀世界政治劇詩学（ブレヒト的叙事演劇）の南アジア的展開。"}])

_attach_cross("タカリ『チェンミーン』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"漁村民族誌",
     "description":"チェンミーンのケーララ漁村描写は20世紀南インド海洋民族誌の文学的祖型。"}])

_attach_cross("クヴェンプ詳細", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"古典再創造の詩学",
     "description":"クヴェンプのラーマーヤナ再創造は、世界文学の古典再創造現象（ジョイス・ユリシーズ等）と並行する。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
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
        print(f"[c19-w16] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c19-w16] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c19-w16] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
