"""LIT-DB Phase 2 Wave 19 — C19 India ADD60.

Subfield: lit_india (id=12), region='南アジア'.
Adds 60 NEW non-overlapping concepts covering:
  A: ヴェーダ深掘り (10)
  B: Ramayana 諸版・kanda (8)
  C: Mahabharata 詳細 + Bhagavad Gita (6)
  D: Buddhist literature (8)
  E: Jain & Sikh literature (6)
  F: Sanskrit kavya 補完 (6)
  G: 中世Bhakti詩補完 + Sufi-Bhakti (8)
  H: 南インド詳細 (4)
  I: 近代深掘り (4)

Sources: GRETIL/SARIT/Project Madurai/Sanskrit Heritage/Gita Press
primary tier >= 80%.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("ヴェーダ期", "Vedic Period", -1500, -500,
     "リグ・サーマ・ヤジュル・アタルヴァ4ヴェーダおよびブラーフマナ・アーラニヤカ・ウパニシャッドのヴェーダ文献期。"),
    ("古代叙事詩期", "Ancient Epic Period", -400, 400,
     "マハーバーラタ・ラーマーヤナ等の古代叙事詩成立期。"),
    ("中世ラーマーヤナ諸版期", "Medieval Ramayana Recensions", 800, 1700,
     "アディヤートマ・ヨーガ・ヴァーシシュタ・カンバン・トゥルシーダース等の各地ラーマーヤナ再話期。"),
    ("仏教文学期", "Buddhist Literature Period", -300, 800,
     "上座部三蔵から大乗・密教経典に至る仏教文学期。"),
    ("ジャイナ文学期", "Jaina Literature Period", -300, 1200,
     "アーガマ文献・ウマースヴァーティから中世ジャイナ哲学・宇宙論文学期。"),
    ("シク文学期", "Sikh Literature Period", 1500, 1900,
     "アーディ・グラント、ダサム・グラント、ジャナムサーキー等のシク聖典文学期。"),
    ("古典サンスクリット詩学期", "Classical Sanskrit Kavya & Poetics", 100, 1700,
     "古典サンスクリット叙事詩・宮廷詩・抒情詩の発展期。"),
    ("中世バクティ・スーフィー期", "Medieval Bhakti & Sufi", 1000, 1700,
     "全インドにおけるバクティ運動とスーフィー詩の融合期。"),
    ("サンガム古典期", "Sangam Classical Period", -300, 300,
     "紀元前3世紀から紀元後3世紀の南インド・タミル古典期。"),
    ("タミル中世文学期", "Medieval Tamil Literature", 500, 1400,
     "シャイヴァ・ヴァイシュナヴァ・バクティ詩の南インド中世期。"),
    ("インド近代思想文学期", "Indian Modern Thought & Literature", 1850, 1980,
     "近代インドにおける社会改革・宗教改革・反植民地思想の文学化期。"),
]


GRETIL = "https://gretil.sub.uni-goettingen.de/gretil.html"
SARIT = "https://sarit.indology.info/"
PMADURAI = "https://www.projectmadurai.org/"
SANSHER = "https://sanskrit.inria.fr/"
GITAPRESS = "https://www.gitapress.org/"
WSRC_SA = "https://sa.wikisource.org/wiki/"
WSRC_HI = "https://hi.wikisource.org/wiki/"
WSRC_BN = "https://bn.wikisource.org/wiki/"
WSRC_TA = "https://ta.wikisource.org/wiki/"
WSRC_PA = "https://pa.wikisource.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
ARCHIVE = "https://archive.org/"
SBE = "https://www.sacred-texts.com/hin/"
DSBC = "https://www.dsbcproject.org/"
CBETA = "https://cbeta.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C_DEV = dict(subfield_code="lit_india", region="南アジア", original_script="devanagari")
C_BEN = dict(subfield_code="lit_india", region="南アジア", original_script="bengali")
C_TAM = dict(subfield_code="lit_india", region="南アジア", original_script="tamil")
C_GUR = dict(subfield_code="lit_india", region="南アジア", original_script="gurmukhi")
C_TIB = dict(subfield_code="lit_india", region="南アジア", original_script="tibetan")
C_ROM = dict(subfield_code="lit_india", region="南アジア", original_script="roman")


# ============================================================
# A: ヴェーダ深掘り (10)
# ============================================================
add(**C_DEV, name_ja="リグ・ヴェーダ・マンダラ構成",
    name_en="Rigveda Mandala Structure",
    name_original="ऋग्वेदसंहिता",
    period_key="ヴェーダ期",
    definition="リグ・ヴェーダは10巻（マンダラ）構成。家系巻（2-7巻）が古層、第1・8・10巻が新層、第9巻はソーマ讃歌専門巻。各巻の家系帰属と韻律分布が成立年代の指標となる。",
    background="紀元前1500-1000年頃の段階的編纂、家系（リシ）伝承の体系化。",
    development="マックス・ミュラーの校訂以降、層位学的批判研究の中核となった。",
    historical_context="後期青銅器時代のインド・アーリア部族社会。",
    primary_source_url=GRETIL+"#Rigveda",
    primary_source_type="GRETIL: Rigveda Samhita (Devanagari)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="サーマ・ヴェーダ詠唱",
    name_en="Samaveda Chants",
    name_original="सामवेदसंहिता",
    period_key="ヴェーダ期",
    definition="ソーマ祭で歌われる旋律集。リグ・ヴェーダから抜粋された讃歌（リチャー）に旋律（サーマン）を付した詠唱体系で、ガーナ4部に分類。インド音楽の祖型として古典音楽理論に影響した。",
    background="ヤジュニャの旋律担当ウドガートリ祭官の伝承体系。",
    development="ジャイミニーヤ派・カウトゥマ派・ラーナーヤニーヤ派の伝承分岐を経て、インド古典音楽の起源とされた。",
    historical_context="ヴェーダ期祭式音楽の体系化。",
    primary_source_url=GRETIL+"#Samaveda",
    primary_source_type="GRETIL: Samaveda Samhita",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ヤジュル・ヴェーダ二派",
    name_en="Shukla and Krishna Yajurveda",
    name_original="यजुर्वेदसंहिता",
    period_key="ヴェーダ期",
    definition="ヤジュル・ヴェーダは白（シュクラ、マンダーンディナ・カーンヴァ二派）と黒（クリシュナ、タイッティリーヤ・マイトラーヤニー他）に分岐。白派は本文と注釈を分離、黒派は混在。祭式マントラ集として古代祭式の中軸を成す。",
    background="アドゥヴァリュ祭官系統の伝承分岐、紀元前1000-500年頃。",
    development="シャタパタ・ブラーフマナ等の散文神学発展の母体となった。",
    historical_context="後期ヴェーダ期祭式神学の体系化。",
    primary_source_url=GRETIL+"#Yajurveda",
    primary_source_type="GRETIL: Vajasaneyi Samhita / Taittiriya Samhita",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アタルヴァ・ヴェーダ",
    name_en="Atharvaveda",
    name_original="अथर्ववेदसंहिता",
    period_key="ヴェーダ期",
    definition="呪術・治癒・護符・呪詛を中心とする第4ヴェーダ。シャウナカ派・パイッパラーダ派の二伝承。家庭祭式・呪医術・哲学讃歌（クシェートラ・スークタ等）を含み、ヴェーダ世界観の周縁・民俗層を伝える。",
    background="バラモン祭式正統と並走した呪術民俗伝承の文献化。",
    development="20世紀に呪術医学・宗教民族学の中核資料として再評価された。",
    historical_context="後期ヴェーダ期民俗・呪術文化。",
    primary_source_url=GRETIL+"#Atharvaveda",
    primary_source_type="GRETIL: Atharvaveda (Shaunaka)",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="シャタパタ・ブラーフマナ",
    name_en="Shatapatha Brahmana",
    name_original="शतपथब्राह्मण",
    period_key="ヴェーダ期",
    definition="白ヤジュル・ヴェーダ所属の散文ブラーフマナ。100章構成で祭式の意味解釈・神話・宇宙論を展開。プラジャーパティ宇宙開闢神話、洪水神話（マヌ伝説）等、後代ヒンドゥー神話の祖型を多数含む。",
    background="後期ヴェーダ期祭式神学の集大成、ヤージュニャヴァルキヤ系統の伝承。",
    development="エッゲリンク英訳（SBE）以降、インド学・比較神話学の中核資料となった。",
    historical_context="紀元前800-600年頃の後期ヴェーダ祭式期。",
    primary_source_url=GRETIL+"#Shatapatha",
    primary_source_type="GRETIL: Shatapatha Brahmana (Madhyandina)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ナーサディーヤ・スークタ",
    name_en="Nasadiya Sukta (Hymn of Creation)",
    name_original="नासदीयसूक्तम्",
    period_key="ヴェーダ期",
    definition="リグ・ヴェーダ第10巻第129讃歌『有もなく無もなき時』。創造以前の状態と創造神の不可知性を哲学的に問う讃歌で、ウパニシャッド哲学の祖型・インド哲学的詩の頂点として世界哲学史に位置づけられる。",
    background="リグ・ヴェーダ後期層の哲学的内省の到達点。",
    development="ドイッセン・ラーダークリシュナンを経て20世紀比較哲学の中核資料となった。",
    historical_context="後期ヴェーダ期哲学的詩の発生。",
    primary_source_url=GRETIL+"#RV-10.129",
    primary_source_type="GRETIL: Rigveda 10.129",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="プルシャ・スークタ",
    name_en="Purusha Sukta",
    name_original="पुरुषसूक्तम्",
    period_key="ヴェーダ期",
    definition="リグ・ヴェーダ第10巻第90讃歌。原人プルシャの自己犠牲から世界・社会階層（四姓ヴァルナ）が生じたとする宇宙論的犠牲讃歌。ヴァルナ起源の聖典的根拠として、後代ダルマ思想・カースト批判言説の中核となった。",
    background="リグ・ヴェーダ末期の宇宙論的思弁と社会秩序の聖典化。",
    development="アンベードカル等の批判的読解を経て、20世紀インド社会思想の中軸テクストとなった。",
    historical_context="後期ヴェーダ期社会階層形成期。",
    primary_source_url=GRETIL+"#RV-10.90",
    primary_source_type="GRETIL: Rigveda 10.90",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ブリハダーラニヤカ・ウパニシャッド",
    name_en="Brihadaranyaka Upanishad",
    name_original="बृहदारण्यकोपनिषद्",
    period_key="ヴェーダ期",
    definition="シャタパタ・ブラーフマナ末尾に位置する最古かつ最大のウパニシャッド。ヤージュニャヴァルキヤとマイトレーイーの対話、五火二道説、不死探求の倫理的内省を含み、アートマン＝ブラフマン同一性思想の中核典拠。",
    background="後期ヴェーダ期の哲学的思弁の集成。",
    development="シャンカラ注以降、ヴェーダーンタ哲学の根本聖典となった。",
    historical_context="紀元前700-500年頃の哲学的ウパニシャッド成立期。",
    primary_source_url=GRETIL+"#Brihadaranyaka",
    primary_source_type="GRETIL: Brihadaranyaka Upanishad",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="チャーンドーギヤ・ウパニシャッド",
    name_en="Chandogya Upanishad",
    name_original="छान्दोग्योपनिषद्",
    period_key="ヴェーダ期",
    definition="サーマ・ヴェーダ系大ウパニシャッド。8章構成でウッダーラカとシュヴェータケートゥの『汝はそれである（タット・トヴァム・アシ）』対話、サット・チット・アーナンダ思想、五火説等、ヴェーダーンタ哲学の根幹を担う。",
    background="サーマ・ヴェーダ・ジャイミニーヤ系の哲学的内省。",
    development="不二一元論ヴェーダーンタの中核典拠として中世以降強い影響を与えた。",
    historical_context="後期ヴェーダ期哲学ウパニシャッド成熟期。",
    primary_source_url=GRETIL+"#Chandogya",
    primary_source_type="GRETIL: Chandogya Upanishad",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="マーンドゥーキヤ・ウパニシャッド",
    name_en="Mandukya Upanishad",
    name_original="माण्डूक्योपनिषद्",
    period_key="ヴェーダ期",
    definition="アタルヴァ・ヴェーダ系の最短12詩節ウパニシャッド。オーム音節を意識四状態（覚醒・夢・熟睡・第四＝トゥリーヤ）と関連付け、純粋意識の理論化を行う。ガウダパーダ『カーリカー』を通じて不二一元論の核心テクストとなった。",
    background="ウパニシャッド末期の意識哲学的精緻化。",
    development="ガウダパーダ・シャンカラを経て、不二一元論ヴェーダーンタの哲学的中核となった。",
    historical_context="後期ウパニシャッド期意識哲学発展。",
    primary_source_url=GRETIL+"#Mandukya",
    primary_source_type="GRETIL: Mandukya Upanishad",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# B: Ramayana 諸版・kanda 詳細 (8)
# ============================================================
add(**C_DEV, name_ja="ラーマーヤナ7カーンダ構造",
    name_en="Ramayana Seven Kandas",
    name_original="रामायणम्",
    period_key="古代叙事詩期",
    definition="ヴァールミーキ・ラーマーヤナ7巻構成。バーラ（少年）・アヨーディヤー・アラニヤ（森）・キシュキンダー・スンダラ（美）・ユッダ（戦）・ウッタラ（後）の各カーンダが叙事詩的時間構造を形成し、第1・7巻は後代付加層と推定される。",
    background="紀元前4世紀-紀元後2世紀の段階的編纂。",
    development="バローダ批判校訂版（1960-75）が層位学的研究の基盤となった。",
    historical_context="古代北インド王権神話形成期。",
    primary_source_url=GRETIL+"#Ramayana",
    primary_source_type="GRETIL: Valmiki Ramayana (Baroda Critical Edition)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アディヤートマ・ラーマーヤナ",
    name_en="Adhyatma Ramayana",
    name_original="अध्यात्मरामायणम्",
    period_key="中世ラーマーヤナ諸版期",
    definition="ブラフマーンダ・プラーナ所収の哲学的ラーマーヤナ（14世紀頃）。ラーマをヴィシュヌの完全顕現（パラ・ブラフマン）として描き、不二一元論ヴェーダーンタとバクティを統合。トゥルシーダース『ラーム・チャリト・マーナス』の直接的源泉。",
    background="中世北インドのヴェーダーンタ的バクティ思潮。",
    development="トゥルシーダース、エルッタッチャン（マラヤーラム版）の直接的母胎となった。",
    historical_context="14世紀北インド・ラーマ・バクティ運動。",
    primary_source_url=GRETIL+"#AdhyatmaRamayana",
    primary_source_type="GRETIL: Adhyatma Ramayana",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ヨーガ・ヴァーシシュタ",
    name_en="Yoga Vasishtha",
    name_original="योगवासिष्ठम्",
    period_key="中世ラーマーヤナ諸版期",
    definition="若きラーマと聖仙ヴァシシュタの対話で展開する大規模哲学詩（10-12世紀、3万2千詩節）。世界の幻影性（マーヤー）と意識の唯一実在性をカシミール・シャイヴィズム的に説く、不二一元論詩学の頂点。",
    background="カシミール・シャイヴィズムとヴェーダーンタの詩的統合。",
    development="モーハン・ラール・サーダ等の英訳を経て、20世紀比較哲学の重要資料となった。",
    historical_context="10-12世紀カシミール哲学詩。",
    primary_source_url=GRETIL+"#YogaVasishtha",
    primary_source_type="GRETIL: Yoga Vasishtha",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_BEN, name_ja="クリッティバース・ラーマーヤン",
    name_en="Krittibasi Ramayan",
    name_original="কৃত্তিবাসী রামায়ণ",
    period_key="中世ラーマーヤナ諸版期",
    definition="クリッティバース・オジャー（15世紀）によるベンガル語ラーマーヤナ（パンチャーリー形式）。ベンガル民衆語で語り直した最初期の地方ラーマーヤナで、東ベンガル民俗・口承伝統と融合し、近代ベンガル文学の地下水脈となった。",
    background="15世紀ベンガル・スルタン期の地方語文学興隆。",
    development="ベンガル民衆ラーマ・バクティの中軸として、近代ベンガル文学への影響源となった。",
    historical_context="中世ベンガル地方語文学期。",
    primary_source_url=WSRC_BN+"কৃত্তিবাসী_রামায়ণ",
    primary_source_type="Bengali Wikisource: Krittibasi Ramayan",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="トゥルシーダース『ラーム・チャリト・マーナス』",
    name_en="Tulsidas's Ramcharitmanas",
    name_original="रामचरितमानस",
    period_key="中世ラーマーヤナ諸版期",
    definition="ゴースワーミー・トゥルシーダース（1532-1623）によるアワディー語ラーマーヤナ。7カーンダ構成・ドーハー＋チョウパーイー韻律。北インド・ラーマ・バクティの聖典として現代まで毎日朗誦され、ヒンディー圏の宗教文学の中核を成す。",
    background="ムガル期北インドのバクティ運動の高揚。",
    development="ガンディー期ナショナリズムの精神的基盤となり、ギーターと並ぶ大衆聖典となった。",
    historical_context="16世紀末ムガル期北インド・バクティ。",
    primary_source_url=GITAPRESS+"hindi/ramcharitmanas",
    primary_source_type="Gita Press: Ramcharitmanas",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アドブタ・ラーマーヤナ",
    name_en="Adbhuta Ramayana",
    name_original="अद्भुतरामायणम्",
    period_key="中世ラーマーヤナ諸版期",
    definition="ヴァールミーキ作と仮託される中世ラーマーヤナ（14-15世紀頃）。シーターをカーリー＝マハーカーリーと同一化し、ラーマの代わりにシーターが千頭ラーヴァナを倒す女神主義版。シャークタ・タントラとラーマ伝承の融合作。",
    background="中世シャークタ運動とラーマ伝承の交差。",
    development="20世紀フェミニスト読解の重要資料となった。",
    historical_context="中世シャークタ・タントラ系ラーマーヤナ。",
    primary_source_url=GRETIL+"#AdbhutaRamayana",
    primary_source_type="GRETIL: Adbhuta Ramayana",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_TAM, name_ja="カンバ・ラーマーヤナム7カーンダ",
    name_en="Kamba Ramayanam Seven Books",
    name_original="கம்பராமாயணம்",
    period_key="タミル中世文学期",
    definition="カンバン（12世紀）によるタミル語ラーマーヤナ『イラーマーヴァターラム』。ヴァールミーキの7巻構成のうちウッタラ・カーンダを除く6巻＋独自エピソードで再構築。タミル文学最高峰の宮廷叙事詩でヴィシシュターディヴァイタ的解釈。",
    background="チョーラ朝期タミル・ヴァイシュナヴァ・バクティの隆盛。",
    development="タミル文学正典の頂点として現代まで朗誦・注釈され続ける。",
    historical_context="12世紀チョーラ朝タミル宮廷文学期。",
    primary_source_url=PMADURAI+"pmworks.html",
    primary_source_type="Project Madurai: Kamba Ramayanam",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アーナンダ・ラーマーヤナ",
    name_en="Ananda Ramayana",
    name_original="आनन्दरामायणम्",
    period_key="中世ラーマーヤナ諸版期",
    definition="15-17世紀頃成立の後期ラーマーヤナ。ラーマ即位後の物語（ラージヤ・カーンダ等9カーンダ）を展開し、ラーマ寺院巡礼地の起源譚を集積。マハーラーシュトラ・ラーマ・バクティ伝承の聖典的源泉。",
    background="中世末期ラーマ巡礼伝承の聖典化。",
    development="マハーラーシュトラ・ラーマ・バクティ実践の経典的基盤となった。",
    historical_context="近世初期ラーマ・バクティ巡礼文化。",
    primary_source_url=GRETIL+"#AnandaRamayana",
    primary_source_type="GRETIL: Ananda Ramayana",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: Mahabharata 詳細 + Bhagavad Gita (6)
# ============================================================
add(**C_DEV, name_ja="マハーバーラタ18パルヴァ構成",
    name_en="Mahabharata Eighteen Parvas",
    name_original="महाभारतम्",
    period_key="古代叙事詩期",
    definition="アーディ・サバー・ヴァナ・ヴィラータ・ウディヨーガ・ビーシュマ・ドローナ・カルナ・シャリヤ・サウプティカ・ストリー・シャーンティ・アヌシャーサナ・アシュヴァメーディカ・アーシュラマヴァースィカ・マウサラ・マハープラスターニカ・スヴァルガーローハナの18巻構成。",
    background="紀元前4世紀-紀元後4世紀の長期段階的編纂。",
    development="プーナ批判校訂版（1933-66）が層位学的研究の基盤となった。",
    historical_context="古代北インド王権・ダルマ思想形成期。",
    primary_source_url=GRETIL+"#Mahabharata",
    primary_source_type="GRETIL: Mahabharata (BORI Critical Edition)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="バガヴァッド・ギーター18章構成",
    name_en="Bhagavad Gita Eighteen Chapters",
    name_original="भगवद्गीता",
    period_key="古代叙事詩期",
    definition="マハーバーラタ・ビーシュマ・パルヴァ所収700詩節18章。アルジュナの懐疑（1）、サーンキヤ（2）、カルマ（3-5）、ディヤーナ（6）、ジニャーナ（7-12 バクティ含む）、グナ・モークシャ（13-18）の三部構成で三道（ジニャーナ・バクティ・カルマ）を統合する。",
    background="マハーバーラタ後期層に挿入された宗教哲学詩。",
    development="シャンカラ・ラーマーヌジャ・マドゥヴァ・ガンディー・ティラク等の注釈伝統を生んだ。",
    historical_context="古代叙事詩期宗教哲学詩の頂点。",
    primary_source_url=GITAPRESS+"hindi/srimadbhagavadgita",
    primary_source_type="Gita Press: Srimad Bhagavad Gita",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="マハーバーラタ・シャーンティ・パルヴァ",
    name_en="Mahabharata Shanti Parva",
    name_original="शान्तिपर्व",
    period_key="古代叙事詩期",
    definition="マハーバーラタ第12巻『平和の書』。死の床のビーシュマがユディシティラに王道（ラージャダルマ）・解脱（モークシャダルマ）・苦難時の規範（アーパッダルマ）を説く百科事典的章で、古代インド政治思想・倫理思想の集大成。",
    background="古代インド政治哲学・ダルマ思想の体系化。",
    development="アルタシャーストラと並ぶ古代政治思想資料として20世紀以降研究された。",
    historical_context="紀元前後の古代インド政治倫理思想期。",
    primary_source_url=GRETIL+"#MBh-Shanti",
    primary_source_type="GRETIL: Mahabharata Shanti Parva",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="マハーバーラタ・アヌシャーサナ・パルヴァ",
    name_en="Mahabharata Anushasana Parva",
    name_original="अनुशासनपर्व",
    period_key="古代叙事詩期",
    definition="マハーバーラタ第13巻『教説の書』。ビーシュマが説く社会倫理・贈与論（ダーナ）・女性論・タパス論・先祖供養を集成した百科事典的章。古代インド社会倫理・贈与経済の主要典拠。",
    background="古代インド社会倫理思想の体系化。",
    development="20世紀社会人類学（モースの贈与論）と比較研究される資料となった。",
    historical_context="古代社会倫理形成期。",
    primary_source_url=GRETIL+"#MBh-Anushasana",
    primary_source_type="GRETIL: Mahabharata Anushasana Parva",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="ハリヴァンシャ",
    name_en="Harivamsha",
    name_original="हरिवंशम्",
    period_key="古代叙事詩期",
    definition="マハーバーラタ付録（キラ）として伝えられるクリシュナ系譜。3部構成（ハリヴァンシャ・パルヴァ、ヴィシュヌ・パルヴァ、バヴィシュヤ・パルヴァ）でクリシュナ伝記の最古層を伝え、後代ハリヴァンシャ・プラーナ等のクリシュナ・バクティ文学の源泉。",
    background="古代叙事詩期末の付加伝説層。",
    development="バーガヴァタ・プラーナ等クリシュナ・バクティ文学の祖型となった。",
    historical_context="叙事詩末期-プラーナ期過渡期。",
    primary_source_url=GRETIL+"#Harivamsha",
    primary_source_type="GRETIL: Harivamsha",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="マハーバーラタ・サウプティカ・パルヴァ",
    name_en="Mahabharata Sauptika Parva",
    name_original="सौप्तिकपर्व",
    period_key="古代叙事詩期",
    definition="マハーバーラタ第10巻『眠れる戦士たちの書』。アシュヴァッターマンによるパーンダヴァ陣営夜襲・無抵抗者殺害を扱う暗黒章。戦争倫理の崩壊とダルマの限界を主題化し、現代戦争倫理研究の重要参照点。",
    background="クルクシェートラ戦争末期の倫理的破綻の文学化。",
    development="20世紀戦争倫理学（マイケル・ウォルツァー等）の比較資料となった。",
    historical_context="古代戦争倫理思想形成期。",
    primary_source_url=GRETIL+"#MBh-Sauptika",
    primary_source_type="GRETIL: Mahabharata Sauptika Parva",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: Buddhist literature (8)
# ============================================================
add(**C_ROM, name_ja="パーリ三蔵（ティピタカ）",
    name_en="Pali Tipitaka",
    name_original="Tipiṭaka",
    period_key="仏教文学期",
    definition="上座部仏教正典。ヴィナヤ・ピタカ（律）、スッタ・ピタカ（経、5ニカーヤ）、アビダンマ・ピタカ（論、7書）の三蔵構成。紀元前1世紀スリランカで文書化され、現存最古の完備した仏教正典として南方仏教の規範。",
    background="紀元前3-1世紀インド・スリランカ上座部の口頭伝承の文書化。",
    development="チャッタ・サンガーヤナ版・PTS版を経て20世紀世界仏教学の基盤資料となった。",
    historical_context="マウリヤ朝以降スリランカでの仏教正典化。",
    primary_source_url="https://www.tipitaka.org/",
    primary_source_type="VRI Tipitaka (Chattha Sangayana)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_ROM, name_ja="ジャータカ547本生譚",
    name_en="Jataka 547 Birth Stories",
    name_original="Jātaka",
    period_key="仏教文学期",
    definition="クッダカ・ニカーヤ所収の釈迦本生譚集。547話で構成され、菩薩の前世譚を韻文＋散文注釈で語る。ヴェッサンタラ・ジャータカ等の波羅蜜行物語が中核で、東南アジア仏教文化の物語的源泉となった。",
    background="紀元前3-紀元前1世紀の物語的仏教教化文学の集成。",
    development="バルフット・サーンチー浮彫を経て、東南アジア仏教美術・文学の規範物語となった。",
    historical_context="古代インド仏教民衆教化期。",
    primary_source_url="https://www.tipitaka.org/romn/cscd/s0513m.mul0.xml",
    primary_source_type="VRI Tipitaka: Jataka",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アシュヴァゴーシャ『ブッダチャリタ』",
    name_en="Ashvaghosha's Buddhacarita",
    name_original="बुद्धचरितम्",
    period_key="仏教文学期",
    definition="アシュヴァゴーシャ（1-2世紀）の梵語仏伝叙事詩28章（現存17章）。サンスクリット古典詩学の規範に従い釈迦伝を再構成した最初期の仏教マハーカーヴィヤで、後代カーリダーサにも影響したカーヴィヤ詩学の先駆作。",
    background="クシャーン朝期の仏教サンスクリット文学の成立。",
    development="チベット訳・漢訳『仏所行讃』を経て東アジア仏教伝記文学の祖型となった。",
    historical_context="2世紀クシャーン朝仏教サンスクリット文学期。",
    primary_source_url=GRETIL+"#Buddhacarita",
    primary_source_type="GRETIL: Buddhacarita (Ashvaghosha)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ラリタヴィスタラ",
    name_en="Lalitavistara",
    name_original="ललितविस्तरः",
    period_key="仏教文学期",
    definition="3-4世紀頃の大乗仏伝『遊戯の詳細』。釈迦の降誕・出家・成道までを散文＋ガーター韻文（ヴァイプルヤ形式）で華麗に再構成し、中央アジア・東アジア仏伝の図像源泉となった。説一切有部－大乗過渡期テクスト。",
    background="部派仏教から大乗仏教への過渡期の仏伝再編。",
    development="チベット訳・漢訳『方広大荘厳経』を経て東アジア仏教美術の図像源泉となった。",
    historical_context="3-4世紀仏伝文学過渡期。",
    primary_source_url=GRETIL+"#Lalitavistara",
    primary_source_type="GRETIL: Lalitavistara",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="法華経（サッダルマプンダリーカ）",
    name_en="Lotus Sutra (Saddharmapundarika)",
    name_original="सद्धर्मपुण्डरीकसूत्रम्",
    period_key="仏教文学期",
    definition="紀元前後成立の大乗最重要経典。一仏乗思想・方便（ウパーヤ）・久遠仏陀観を譬喩物語（火宅・三車・化城等）で展開し、東アジア仏教（天台・日蓮）の中軸経典として、宗教文学・物語文学に巨大な影響を与えた。",
    background="大乗仏教初期の革新的経典文学。",
    development="鳩摩羅什漢訳『妙法蓮華経』を経て東アジア仏教文化の中軸となった。",
    historical_context="紀元前後大乗仏教興起期。",
    primary_source_url=GRETIL+"#Saddharmapundarika",
    primary_source_type="GRETIL: Saddharmapundarika Sutra",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ナーガールジュナ『中論』",
    name_en="Nagarjuna's Mulamadhyamakakarika",
    name_original="मूलमध्यमककारिका",
    period_key="仏教文学期",
    definition="ナーガールジュナ（2-3世紀）の中観派根本論書。27章で空（シューニヤター）・縁起・二諦説を四句否定（テトラレンマ）論理で展開し、大乗哲学詩学の頂点。世界哲学史における否定弁証法の極北。",
    background="大乗仏教哲学的体系化期。",
    development="チベット仏教中観派・東アジア三論宗・現代分析哲学（ガーフィールド等）に影響した。",
    historical_context="2-3世紀大乗哲学黄金期。",
    primary_source_url=GRETIL+"#MMK",
    primary_source_type="GRETIL: Mulamadhyamakakarika (Nagarjuna)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TIB, name_ja="チベット大蔵経カンギュル・テンギュル",
    name_en="Tibetan Kangyur and Tengyur",
    name_original="བཀའ་འགྱུར་བསྟན་འགྱུར",
    period_key="仏教文学期",
    definition="14世紀ナルタン版以降確立したチベット仏典正典。カンギュル（仏説部、約108巻）とテンギュル（論疏部、約225巻）から構成され、サンスクリット原典消失後の大乗・密教文献の最重要伝承体系。",
    background="11-14世紀チベット翻訳事業（ロー・ツァーバー）の集大成。",
    development="20世紀以降、サンスクリット原典再構築の中核資料となった。",
    historical_context="チベット仏教正典化期。",
    primary_source_url="https://www.bdrc.io/",
    primary_source_type="BDRC: Tibetan Buddhist Resource Center",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TIB, name_ja="ミラレパ十万歌",
    name_en="Hundred Thousand Songs of Milarepa",
    name_original="མི་ལ་རས་པའི་མགུར་འབུམ",
    period_key="仏教文学期",
    definition="11-12世紀チベット詩人僧ミラレパの即興教歌集。ヘーラム編（15世紀）でドハー形式の60章に編纂され、チベット民衆口承詩・タントラ実践詩の頂点として、現代まで歌い継がれるチベット文学の中核。",
    background="11-12世紀チベット・カギュ派タントラ実践の詩化。",
    development="20世紀世界宗教詩アンソロジーの中核作品となった。",
    historical_context="中世チベット民衆仏教詩期。",
    primary_source_url="https://www.bdrc.io/MilarepaSongs",
    primary_source_type="BDRC: Milarepa Mgur 'bum",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: Jain & Sikh literature (6)
# ============================================================
add(**C_DEV, name_ja="ウマースヴァーティ『タットヴァールタ・スートラ』",
    name_en="Umasvati's Tattvarthasutra",
    name_original="तत्त्वार्थसूत्रम्",
    period_key="ジャイナ文学期",
    definition="ウマースヴァーティ（2-5世紀）の梵語ジャイナ綱要書。10章350スートラで七真理（タットヴァ）・業論・宇宙論・解脱論を体系化。ディガンバラ・シュヴェーターンバラ両派が共通正典として認める唯一の梵語ジャイナ哲学典。",
    background="ジャイナ哲学の体系化と梵語化。",
    development="シッダセーナ・プージャパーダ・ヘーマチャンドラ等の注釈伝統を生んだ。",
    historical_context="グプタ朝期ジャイナ哲学体系化期。",
    primary_source_url=GRETIL+"#Tattvarthasutra",
    primary_source_type="GRETIL: Tattvarthasutra (Umasvati)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アーチャーラーンガ・スートラ",
    name_en="Acharanga Sutra",
    name_original="आयारंगसुत्तं",
    period_key="ジャイナ文学期",
    definition="シュヴェーターンバラ・ジャイナ最古の正典（アングの第1書、紀元前4-3世紀）。アルダ・マーガディー語で記され、マハーヴィーラの言行・修行倫理・アヒンサー（不殺生）哲学を伝える、ジャイナ思想の根本聖典。",
    background="ジャイナ最初期のアルダ・マーガディー語伝承の聖典化。",
    development="近代以降ヘルマン・ヤコービ等の校訂を経て世界宗教学の中軸資料となった。",
    historical_context="紀元前4-3世紀シュヴェーターンバラ正典化期。",
    primary_source_url=SBE+"jain/index.htm",
    primary_source_type="Sacred Books of the East: Acharanga Sutra (Jacobi)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ヘーマチャンドラ『トリシャシュティシャラーカープルシャチャリタ』",
    name_en="Hemachandra's Trishashtishalakapurushacharitra",
    name_original="त्रिषष्टिशलाकापुरुषचरितम्",
    period_key="ジャイナ文学期",
    definition="ヘーマチャンドラ（1089-1172）の大規模梵語ジャイナ叙事詩『63聖人伝』。24ティールタンカラ・12チャクラヴァルティン・27ヴァースデーヴァ・バラデーヴァ・プラティヴァースデーヴァの63聖人伝を10巻37000詩節で網羅した中世ジャイナ文学最大作。",
    background="チャウルキヤ朝グジャラート期ジャイナ文化の隆盛。",
    development="中世西インド・ジャイナ正典補完文学の頂点となった。",
    historical_context="12世紀グジャラート・ジャイナ宮廷文化。",
    primary_source_url=GRETIL+"#Trishashti",
    primary_source_type="GRETIL: Trishashtishalakapurushacharitra",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_GUR, name_ja="アーディ・グラント／グル・グラント・サーヒブ",
    name_en="Adi Granth / Guru Granth Sahib",
    name_original="ਆਦਿ ਗ੍ਰੰਥ",
    period_key="シク文学期",
    definition="シク教聖典。1604年第5代グル・アルジャンが編纂、1708年第10代グル・ゴービンド・シングが最終確定。1430頁、6グル・15バガト（カビール、ラヴィダース等）・11バット詩人の詩を31ラーガで編成、シク教永遠のグルとされる。",
    background="ムガル期パンジャーブ・シク教団の聖典化。",
    development="シク教世界共同体の中核として現代まで朝晩の儀礼で朗誦され続ける。",
    historical_context="17世紀ムガル期シク教団形成期。",
    primary_source_url=WSRC_PA+"ਸ੍ਰੀ_ਗੁਰੂ_ਗ੍ਰੰਥ_ਸਾਹਿਬ",
    primary_source_type="Punjabi Wikisource: Sri Guru Granth Sahib",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_GUR, name_ja="ジャナムサーキー伝承",
    name_en="Janamsakhi Narratives",
    name_original="ਜਨਮਸਾਖੀ",
    period_key="シク文学期",
    definition="グル・ナーナク（1469-1539）の伝記伝承群。バーラ・サーキー、ミハルバーン・サーキー、プラータン・サーキー等の異本があり、16-18世紀パンジャーブ語の聖伝記文学の中核を成し、初期シク教義の物語的展開を伝える。",
    background="16-18世紀パンジャーブ・シク聖伝記文学の発生。",
    development="シク教育・大衆信仰の中軸文献として近世まで広く流布した。",
    historical_context="近世シク聖伝記文学期。",
    primary_source_url=ARCHIVE+"details/janamsakhi",
    primary_source_type="Internet Archive: Janamsakhi (various recensions)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_GUR, name_ja="ダサム・グラント",
    name_en="Dasam Granth",
    name_original="ਦਸਮ ਗ੍ਰੰਥ",
    period_key="シク文学期",
    definition="第10代グル・ゴービンド・シング（1666-1708）作と伝えられる第二聖典。1428頁、ジャプ・サーヒブ、アカール・ウスタト、バチットラ・ナータク、チャンディー・チャリットラ等を含み、シク武装戦士伝統（カールサー）の精神的基盤。",
    background="17世紀末シク武装戦士伝統の聖典化。",
    development="シク・カールサー精神的基盤として現代まで論争的解釈を生む。",
    historical_context="17世紀末ムガル末期シク武装期。",
    primary_source_url=WSRC_PA+"ਦਸਮ_ਗ੍ਰੰਥ",
    primary_source_type="Punjabi Wikisource: Dasam Granth",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: Sanskrit kavya 補完 (6)
# ============================================================
add(**C_DEV, name_ja="バーナバッタ『ハルシャチャリタ』",
    name_en="Banabhatta's Harshacharita",
    name_original="हर्षचरितम्",
    period_key="古典サンスクリット詩学期",
    definition="バーナバッタ（7世紀）によるハルシャ王（606-647）の伝記散文（アーキヤーイカー）。8ウッチュヴァーサ構成で、サンスクリット散文芸術の頂点とされ、古典サンスクリット史伝散文（チャリタ・カーヴィヤ）の祖型を確立した。",
    background="ハルシャ朝期宮廷散文文学の隆盛。",
    development="後代の宮廷史伝（ヴィクラマーンカデーヴァチャリタ等）の規範となった。",
    historical_context="7世紀ハルシャ朝宮廷文学期。",
    primary_source_url=GRETIL+"#Harshacharita",
    primary_source_type="GRETIL: Harshacharita (Banabhatta)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="バーナバッタ『カーダンバリー』",
    name_en="Banabhatta's Kadambari",
    name_original="कादम्बरी",
    period_key="古典サンスクリット詩学期",
    definition="バーナバッタの梵語散文ロマンス（カター）。チャンドラピーダ王子とカーダンバリー姫の三世にわたる愛と転生を語る複雑な入れ子物語で、世界文学史最古級の長編小説の一つとされ、サンスクリット散文芸術の頂点。",
    background="7世紀宮廷散文ロマンスの成熟。",
    development="プシュパダンタ・スバンドゥ等を経て、近代インド長編小説の祖型となった。",
    historical_context="7世紀ハルシャ朝散文ロマンス期。",
    primary_source_url=GRETIL+"#Kadambari",
    primary_source_type="GRETIL: Kadambari (Banabhatta)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ダンディン『ダシャクマーラチャリタ』",
    name_en="Dandin's Dashakumaracharita",
    name_original="दशकुमारचरितम्",
    period_key="古典サンスクリット詩学期",
    definition="ダンディン（7-8世紀）の梵語散文ロマンス『十王子物語』。10王子の冒険・恋愛・盗賊・悪行を絡めた写実的諷刺散文で、古典インドのピカレスク小説の祖型。後代の地方語小説伝統に影響した。",
    background="7-8世紀宮廷散文の写実主義的展開。",
    development="ジャンビー・ヘーマチャンドラ等中世注釈を経て、近代地方語小説伝統に影響した。",
    historical_context="7-8世紀古典散文成熟期。",
    primary_source_url=GRETIL+"#Dashakumaracharita",
    primary_source_type="GRETIL: Dashakumaracharita (Dandin)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="ダンディン『カーヴィヤーダルシャ』",
    name_en="Dandin's Kavyadarsha",
    name_original="काव्यादर्शः",
    period_key="古典サンスクリット詩学期",
    definition="ダンディンの梵語詩学綱要書『詩の鑑』3章。ガウディー・ヴァイダルビー二風格論、35アランカーラ（修辞）、10グナ（質）を体系化し、サンスクリット詩学の規範を確立。チベット・スリランカ詩学にも影響した。",
    background="7-8世紀古典詩学体系化期。",
    development="チベット語訳・タミル詩学への翻案を経て、汎アジア詩学規範となった。",
    historical_context="古典詩学黎明期。",
    primary_source_url=GRETIL+"#Kavyadarsha",
    primary_source_type="GRETIL: Kavyadarsha (Dandin)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="バルトリハリ『シャタカトラヤ』",
    name_en="Bhartrihari's Shatakatraya",
    name_original="शतकत्रयम्",
    period_key="古典サンスクリット詩学期",
    definition="バルトリハリ（5世紀頃）の三百詩集『ニーティ・シュリンガーラ・ヴァイラーギヤ・シャタカ』。各100詩で処世訓・恋愛・離欲を主題化したスバーシタ（金言）詩の頂点で、汎インド・スバーシタ伝統の規範となった。",
    background="5世紀古典スバーシタ詩の成熟。",
    development="近代まで朗誦され続け、19世紀以降英訳を経て世界的金言詩集となった。",
    historical_context="グプタ朝期スバーシタ伝統。",
    primary_source_url=GRETIL+"#Shatakatraya",
    primary_source_type="GRETIL: Shatakatraya (Bhartrihari)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ジャヤデーヴァ『ギータ・ゴーヴィンダ』詳細",
    name_en="Jayadeva's Gita Govinda Detail",
    name_original="गीतगोविन्दम्",
    period_key="古典サンスクリット詩学期",
    definition="ジャヤデーヴァ（12世紀）の梵語抒情劇詩。12サルガ・24プラバンダ（歌）でクリシュナとラーダーの愛と離別を音楽的構造（ラーガ・ターラ指定付き）で歌う。サンスクリット叙情詩とバクティ詩を統合した東インド宮廷詩の頂点。",
    background="12世紀東インド・ヴィシュヌ・バクティ宮廷詩。",
    development="ベンガル・オディヤー・南インド舞踊音楽の中軸テクストとなった。",
    historical_context="セーナ朝末期東インド宮廷文化。",
    primary_source_url=GRETIL+"#GitaGovinda",
    primary_source_type="GRETIL: Gita Govinda (Jayadeva)",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# G: 中世Bhakti詩補完 + Sufi-Bhakti (8)
# ============================================================
add(**C_DEV, name_ja="ミーラーバーイー・パダ集",
    name_en="Mirabai Padas",
    name_original="मीराबाई पद",
    period_key="中世バクティ・スーフィー期",
    definition="ミーラーバーイー（1498-1547頃）のラージャスターニー・ブラジ・グジャラーティー混成詩。クリシュナへの愛を主題とする数百のパダ（短歌）で女性バクティ詩の頂点を成し、汎インド大衆音楽伝承の中軸となった。",
    background="ラージプート王女の宗教的反逆としてのクリシュナ・バクティ。",
    development="20世紀ヒンドゥスターニー音楽・映画音楽を通じて汎インド大衆遺産となった。",
    historical_context="16世紀ラージャスターン・バクティ運動。",
    primary_source_url=ARCHIVE+"details/mirabaipadasangraha",
    primary_source_type="Internet Archive: Mirabai Padasangraha",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="トゥルシーダース『ヴィナヤ・パトリカー』",
    name_en="Tulsidas's Vinaya Patrika",
    name_original="विनयपत्रिका",
    period_key="中世バクティ・スーフィー期",
    definition="トゥルシーダースの『嘆願書』。ラーマへの祈願体279短詩で構成され、自伝的告白・社会批判・宗教的内省を含む。『マーナス』と並ぶトゥルシーダース後期の代表作で、北インド・バクティ抒情詩の頂点。",
    background="16世紀末北インド・バクティ運動の内省的展開。",
    development="北インド大衆バクティ実践の中軸抒情詩集として現代まで朗誦された。",
    historical_context="ムガル期北インド・バクティ抒情詩。",
    primary_source_url=GITAPRESS+"hindi/vinaypatrika",
    primary_source_type="Gita Press: Vinaya Patrika",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="カビール『ビージャク』",
    name_en="Kabir's Bijak",
    name_original="बीजक",
    period_key="中世バクティ・スーフィー期",
    definition="カビール（15世紀）の詩集『種子の書』。ラーマイニー・シャブダ・サキー三部構成で、サント運動の最重要正典版。ヒンドゥー・イスラーム両伝統を超克するニルグナ（無形）バクティ哲学を展開し、カビール・パンタの聖典となった。",
    background="ガンジス上流域サント運動の聖典化。",
    development="20世紀ラビンドラナート・タゴール英訳を経て世界宗教詩アンソロジーの中軸となった。",
    historical_context="15世紀北インド・サント運動。",
    primary_source_url=ARCHIVE+"details/kabir-bijak",
    primary_source_type="Internet Archive: Kabir Bijak",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="トゥカーラーム『アバンガ』詳細",
    name_en="Tukaram Abhangas Detail",
    name_original="तुकारामाची अभंगवाणी",
    period_key="中世バクティ・スーフィー期",
    definition="トゥカーラーム（1608-49）のマラーティー語ヴィッタル神讃歌約4,500首。ヴァールカリ・バクティ運動の中核として、現代までパンダルプル巡礼で歌い継がれ、マラーティー文学の不朽の規範を成す。",
    background="17世紀マハーラーシュトラ・ヴァールカリ運動の頂点。",
    development="近代マラーティー文学（パターヴァルダン等）の中軸インスピレーション源となった。",
    historical_context="17世紀マハーラーシュトラ・バクティ。",
    primary_source_url=ARCHIVE+"details/tukaramabhangawani",
    primary_source_type="Internet Archive: Tukaram Abhangawani",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="アーンダール『ティルッパーヴァイ』",
    name_en="Andal's Tiruppavai",
    name_original="திருப்பாவை",
    period_key="タミル中世文学期",
    definition="アーンダール（8世紀）のタミル語クリシュナ讃歌30詩節。マルガリ月の処女祭儀（パーヴァイ・ノンブ）を主題化し、女性バクティ詩の頂点として現代まで南インド・ヴィシュヌ寺院で毎日朗誦される、タミル女性詩人最古の中核作品。",
    background="8世紀タミル・ヴァイシュナヴァ・アールヴァール・バクティの女性的展開。",
    development="ラーマーヌジャ哲学的解釈を経て、南インド・ヴィシュヌ寺院儀礼の中軸となった。",
    historical_context="8世紀タミル・バクティ女性詩人期。",
    primary_source_url=PMADURAI+"pmworks.html#Andal",
    primary_source_type="Project Madurai: Tiruppavai",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="ナンマールヴァール『ティルヴァーイモリ』",
    name_en="Nammalvar's Tiruvaymoli",
    name_original="திருவாய்மொழி",
    period_key="タミル中世文学期",
    definition="ナンマールヴァール（9世紀）のタミル語ヴィシュヌ讃歌1,102詩節。10章100連歌で『口で語る神聖』を主題化し、タミル・ヴァイシュナヴァ・バクティ詩の頂点。ラーマーヌジャがタミル・ヴェーダと位置付け、現代まで寺院朗誦の中核。",
    background="9世紀パッラヴァ末期タミル・バクティの哲学化。",
    development="ラーマーヌジャ哲学的体系化を経てヴィシシュターディヴァイタ哲学の聖典基盤となった。",
    historical_context="9世紀タミル・アールヴァール後期。",
    primary_source_url=PMADURAI+"pmworks.html#Nammalvar",
    primary_source_type="Project Madurai: Tiruvaymoli",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_GUR, name_ja="ブッレー・シャー詩",
    name_en="Bulleh Shah Poetry",
    name_original="ਬੁੱਲ੍ਹੇ ਸ਼ਾਹ",
    period_key="中世バクティ・スーフィー期",
    definition="ブッレー・シャー（1680-1757）のパンジャーブ語スーフィー詩。カーフィー形式で内的霊性・カースト批判・正統宗教批判を歌い、シャー・フセイン・シャー・アブドゥル・ラティーフと並ぶパンジャーブ・スーフィー三大詩人の中核。",
    background="ムガル末期パンジャーブ・スーフィー・バクティ融合。",
    development="20世紀パキスタン・パンジャーブ大衆音楽（カウワーリー・スーフィー・ロック）の中軸となった。",
    historical_context="18世紀パンジャーブ・スーフィー詩期。",
    primary_source_url=WSRC_PA+"ਬੁੱਲ੍ਹੇ_ਸ਼ਾਹ",
    primary_source_type="Punjabi Wikisource: Bulleh Shah",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="ラル・デード ヴァーク",
    name_en="Lal Ded Vakhs",
    name_original="लल्ल वाक्य",
    period_key="中世バクティ・スーフィー期",
    definition="ラル・デード／ラッレーシュヴァリー（14世紀）のカシミール語ヴァーク（金言詩）。シャイヴァ・タントラとスーフィズムを融合した最古層カシミール文学で、カシミール語文学・カシミール・ムスリム-ヒンドゥー両伝統共有の精神的祖型。",
    background="14世紀カシミール・シャイヴァ-スーフィー融合期。",
    development="20世紀カシミール文学・アイデンティティ論争の中核象徴となった。",
    historical_context="14世紀カシミール宗教融合期。",
    primary_source_url=ARCHIVE+"details/lal-ded-vakhs",
    primary_source_type="Internet Archive: Lal Ded Vakhs",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: 南インド詳細 (4)
# ============================================================
add(**C_TAM, name_ja="トルカーッピヤム・エルットゥ・ソル篇",
    name_en="Tolkappiyam Eluttu and Sol",
    name_original="தொல்காப்பியம்",
    period_key="サンガム古典期",
    definition="トルカーッピヤル（紀元前2世紀-紀元後5世紀）のタミル最古文法書3篇のうちエルットゥ（音論）・ソル（語論）。タミル音韻論・形態論を体系化し、ドラヴィダ言語学の祖型を確立した古典タミル語学の規範書。",
    background="サンガム期タミル言語学の体系化。",
    development="近代ドラヴィダ言語学（カルドウェル等）の起源資料となった。",
    historical_context="サンガム期タミル言語学黎明。",
    primary_source_url=PMADURAI+"pmworks.html#Tolkappiyam",
    primary_source_type="Project Madurai: Tolkappiyam",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="シャイヴァ・ティルムライ12典籍",
    name_en="Shaiva Tirumurai Twelve Books",
    name_original="பன்னிரு திருமுறை",
    period_key="タミル中世文学期",
    definition="11世紀ナンビ・アーンダール・ナンビが編纂したタミル・シャイヴァ正典12巻。テーヴァーラム3詩人・ティルヴァーチャカム・ティルマンディラム・ペリヤ・プラーナム等を含み、タミル・シャイヴァ・バクティ伝統の聖典体系を成す。",
    background="チョーラ朝期タミル・シャイヴァ正典化。",
    development="現代までタミル・シャイヴァ寺院儀礼の中軸となった。",
    historical_context="11世紀チョーラ朝シャイヴァ正典期。",
    primary_source_url=PMADURAI+"pmworks.html#Tirumurai",
    primary_source_type="Project Madurai: Tirumurai",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="ペリヤ・プラーナム63ナーヤナール",
    name_en="Periya Puranam 63 Nayanmars",
    name_original="பெரிய புராணம்",
    period_key="タミル中世文学期",
    definition="チェーッキラール（12世紀）のタミル・シャイヴァ聖人列伝『大プラーナ』。63ナーヤナール（シヴァ聖者）の伝記4,286詩節をシャイヴァ・ティルムライ第12巻として編纂、南インド・シャイヴァ伝記文学の規範を確立した。",
    background="12世紀チョーラ朝シャイヴァ聖伝記文学の集大成。",
    development="タミル・シャイヴァ寺院教育・絵画図像伝統の中軸となった。",
    historical_context="12世紀チョーラ朝シャイヴァ伝記期。",
    primary_source_url=PMADURAI+"pmworks.html#PeriyaPuranam",
    primary_source_type="Project Madurai: Periya Puranam",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_TAM, name_ja="ティルムーラル『ティルマンディラム』",
    name_en="Tirumular's Tirumantiram",
    name_original="திருமந்திரம்",
    period_key="タミル中世文学期",
    definition="ティルムーラル（7世紀）のタミル語シャイヴァ・タントラ詩3,000詩節。シャイヴァ哲学・ヨーガ・タントラ実践を体系化し、シャイヴァ・シッダーンタ哲学の祖型を確立、シャイヴァ・ティルムライ第10巻として聖典化された。",
    background="7世紀タミル・シャイヴァ・タントラ思想の黎明。",
    development="シャイヴァ・シッダーンタ学派の哲学的基盤となった。",
    historical_context="7世紀タミル・タントラ・ヨーガ期。",
    primary_source_url=PMADURAI+"pmworks.html#Tirumantiram",
    primary_source_type="Project Madurai: Tirumantiram",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# I: 近代深掘り (4)
# ============================================================
add(**C_DEV, name_ja="アンベードカル『カースト撲滅』",
    name_en="Ambedkar's Annihilation of Caste",
    name_original="जातिप्रथेचे निर्मूलन",
    period_key="インド近代思想文学期",
    definition="B・R・アンベードカル（1891-1956）の1936年講演原稿（ジャート・パート・トーダク・マンダル招聘で行われず）。ヒンドゥー・ヴァルナ制度を聖典・経済・社会的に根本批判し、20世紀インド・ダリット解放運動の理論的基盤を確立した。",
    background="独立前インド・ダリット運動の理論化。",
    development="20世紀インド社会思想・ダリット文学の中核となり、現代まで論争を生み続ける。",
    historical_context="20世紀前半インド・ダリット解放運動期。",
    primary_source_url=ARCHIVE+"details/AnnihilationOfCaste",
    primary_source_type="Internet Archive: Annihilation of Caste (Ambedkar)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="アンベードカル『ブッダとそのダンマ』",
    name_en="Ambedkar's Buddha and His Dhamma",
    name_original="भगवान बुद्ध आणि त्यांचा धम्म",
    period_key="インド近代思想文学期",
    definition="アンベードカル晩年の代表著（1957年遺著）。仏教を社会的・合理主義的に再解釈し、ナヴァ・ヤーナ（新しい乗り物）として再定式化、1956年ダリット集団改宗の経典的基盤となり、現代インド新仏教運動の聖典となった。",
    background="20世紀ダリット解放運動の宗教的展開。",
    development="現代インド・新仏教運動（ナヴァ・ヤーナ）の聖典として機能している。",
    historical_context="独立直後インド宗教改革運動。",
    primary_source_url=ARCHIVE+"details/buddha-and-his-dhamma",
    primary_source_type="Internet Archive: Buddha and His Dhamma",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C_DEV, name_ja="シュリー・オーロビンド『サーヴィトリー』",
    name_en="Sri Aurobindo's Savitri",
    name_original="सावित्री",
    period_key="インド近代思想文学期",
    definition="シュリー・オーロビンド（1872-1950）の英語スピリチュアル叙事詩『サーヴィトリー：象徴・伝説』。マハーバーラタのサーヴィトリー伝説を素材に、12巻24,000詩行で意識進化哲学を展開した20世紀世界最長のスピリチュアル叙事詩。",
    background="20世紀インド・スピリチュアル・モダニズムの頂点。",
    development="アシュラム共同体の中核テクストとして現代まで研究・朗誦されている。",
    historical_context="20世紀インド・新ヴェーダーンタ思想文学期。",
    primary_source_url="https://www.sriaurobindoashram.org/",
    primary_source_type="Sri Aurobindo Ashram: Savitri",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C_DEV, name_ja="パンディタ・ラマーバーイー『高位カースト・ヒンドゥー女性』",
    name_en="Pandita Ramabai's High Caste Hindu Woman",
    name_original="The High-Caste Hindu Woman",
    period_key="インド近代思想文学期",
    definition="パンディタ・ラマーバーイー（1858-1922）の英語社会批判書（1887年）。高位カースト・ヒンドゥー女性の児童婚・寡婦虐待・教育排除を内側からの証言として記録、19世紀後半インド女性運動の理論的基盤を確立した先駆作。",
    background="19世紀末インド女性改革運動の国際化。",
    development="20世紀インド・フェミニズム文学の祖型となり、現代まで再評価されている。",
    historical_context="19世紀末インド改革・女性運動期。",
    primary_source_url=ARCHIVE+"details/highcastehinduwo00rama",
    primary_source_type="Internet Archive: High Caste Hindu Woman (Ramabai)",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# Cross-domain links (>= 14) and fourth_transform tags (>= 18)
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


# fourth_transform tags (>= 18)
_attach_axes("リグ・ヴェーダ・マンダラ構成", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"家系（リシ）共同伝承の集合的作者性は、AI共同生成における集団的作者性問題の古典的祖型となる。",
     "related_ai_phenomenon":"AI共同生成における集団的作者性"}])
_attach_axes("ナーサディーヤ・スークタ", [
    {"axis":"言語","status":"rethinking",
     "rationale":"創造以前の状態を語る言語の不可能性は、AI生成における前言語的状態の表現問題と理論的に並行する。",
     "related_ai_phenomenon":"AI生成における前言語的状態の表現"}])
_attach_axes("プルシャ・スークタ", [
    {"axis":"受容","status":"rethinking",
     "rationale":"宇宙論的犠牲による社会階層生成神話は、AI生成データセットによる社会階層化（バイアス）問題の理論的祖型。",
     "related_ai_phenomenon":"AI生成における階層化的バイアスの理論化"}])
_attach_axes("ブリハダーラニヤカ・ウパニシャッド", [
    {"axis":"主体","status":"rethinking",
     "rationale":"アートマン＝ブラフマン同一性思想は、AI意識・主観性問題における自他境界の哲学的基盤を提供する。",
     "related_ai_phenomenon":"AI意識における自他境界の哲学化"}])
_attach_axes("マーンドゥーキヤ・ウパニシャッド", [
    {"axis":"主体","status":"rethinking",
     "rationale":"オーム四状態における純粋意識（トゥリーヤ）論は、AI意識のメタ認知層の理論化に資する古典的祖型。",
     "related_ai_phenomenon":"AI意識のメタ認知層の理論化"}])
_attach_axes("ラーマーヤナ7カーンダ構造", [
    {"axis":"物語","status":"rethinking",
     "rationale":"7段階叙事構造の固定化と地方版多様化は、AI生成における物語構造のテンプレート化と多様化の弁証法と並行する。",
     "related_ai_phenomenon":"AI生成物語のテンプレート化と多様化"}])
_attach_axes("トゥルシーダース『ラーム・チャリト・マーナス』", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"梵語原典のアワディー大衆語翻案は、AI翻訳・要約における言語階層を超える伝達問題の歴史的祖型となる。",
     "related_ai_phenomenon":"AI翻訳における言語階層を超える伝達"}])
_attach_axes("カンバ・ラーマーヤナム7カーンダ", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"梵語原典の地方語完全再創造は、AI翻訳における文化的再創造可能性の理論化に資する古典的祖型。",
     "related_ai_phenomenon":"AI翻訳における文化的再創造の限界"}])
_attach_axes("マハーバーラタ18パルヴァ構成", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"千年規模の集合的編纂と層位的増殖は、AI訓練データの長期的累積と層位構造問題の歴史的並行。",
     "related_ai_phenomenon":"AI訓練データの長期的累積と層位"}])
_attach_axes("バガヴァッド・ギーター18章構成", [
    {"axis":"主体","status":"rethinking",
     "rationale":"行為（カルマ）・知（ジニャーナ）・愛（バクティ）の三道統合は、AI意思決定における倫理・認識・関係性の統合問題と理論的に並行する。",
     "related_ai_phenomenon":"AI意思決定における三道統合"}])
_attach_axes("マハーバーラタ・サウプティカ・パルヴァ", [
    {"axis":"受容","status":"rethinking",
     "rationale":"戦争倫理破綻の文学化は、AI兵器・自律兵器の倫理的限界問題の理論化に資する古典的祖型。",
     "related_ai_phenomenon":"AI兵器の倫理的限界の文学的祖型"}])
_attach_axes("パーリ三蔵（ティピタカ）", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"口承伝承から文書化へのメディア転換は、AI時代の知識保存メディア転換問題の歴史的祖型。",
     "related_ai_phenomenon":"AI時代の知識保存メディア転換"}])
_attach_axes("法華経（サッダルマプンダリーカ）", [
    {"axis":"翻訳","status":"rethinking",
     "rationale":"方便（ウパーヤ）思想は、AI生成における対象適応的説明戦略の理論化に資する古典的祖型を提供する。",
     "related_ai_phenomenon":"AI生成における方便的適応説明"}])
_attach_axes("ナーガールジュナ『中論』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"四句否定（テトラレンマ）論理は、AI論理推論における二値論理を超える論理体系の古典的祖型。",
     "related_ai_phenomenon":"AI論理推論における二値論理の超克"}])
_attach_axes("ウマースヴァーティ『タットヴァールタ・スートラ』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"アネカーンタヴァーダ（多面真理説）は、AI生成における複数視点同時保持問題の理論的祖型。",
     "related_ai_phenomenon":"AI生成における多面真理の保持"}])
_attach_axes("アーディ・グラント／グル・グラント・サーヒブ", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"6グル＋15バガト集合的作者性とテクストのグル化は、AI集団的作者性とテクストの権威化問題の祖型。",
     "related_ai_phenomenon":"AI集団的作者性のテクスト権威化"}])
_attach_axes("バルトリハリ『シャタカトラヤ』", [
    {"axis":"創造性","status":"rethinking",
     "rationale":"金言（スバーシタ）形式の極限的圧縮表現は、AI短文生成における意味密度の理論化に資する祖型。",
     "related_ai_phenomenon":"AI短文生成における意味密度"}])
_attach_axes("カビール『ビージャク』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"宗教的差異を超克する民衆語表現は、AI生成における言語的・宗教的多元性統合問題の古典的祖型。",
     "related_ai_phenomenon":"AI生成における宗教的多元性の統合"}])
_attach_axes("アンベードカル『ブッダとそのダンマ』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"宗教伝統の合理主義的再解釈は、AI生成による伝統的テクストの再解釈・更新問題の理論化に資する。",
     "related_ai_phenomenon":"AI生成による伝統テクスト再解釈"}])
_attach_axes("シュリー・オーロビンド『サーヴィトリー』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"意識進化論的詩学は、AI意識発展問題（意識のレベル進化）の哲学的詩的祖型を提供する。",
     "related_ai_phenomenon":"AI意識のレベル進化の詩的祖型"}])


# Cross-domain links (>= 14)
_attach_cross("リグ・ヴェーダ・マンダラ構成", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ヴェーダーンタ哲学の典拠",
     "description":"リグ・ヴェーダ末期讃歌（ナーサディーヤ等）はウパニシャッド・ヴェーダーンタ哲学の根本典拠。"}])
_attach_cross("ナーサディーヤ・スークタ", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"創造論否定哲学",
     "description":"ナーサディーヤは比較哲学において創造論を内在的に問う最古の哲学詩として参照される。"}])
_attach_cross("プルシャ・スークタ", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カースト人類学",
     "description":"プルシャ・スークタはデュモン『ホモ・ヒエラルキクス』等のカースト人類学の聖典的根拠資料。"}])
_attach_cross("ブリハダーラニヤカ・ウパニシャッド", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"アートマン哲学",
     "description":"ブリハダーラニヤカはシャンカラ不二一元論ヴェーダーンタの根本典拠として哲学史の中軸。"}])
_attach_cross("マハーバーラタ18パルヴァ構成", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"世界叙事詩アーキタイプ",
     "description":"マハーバーラタは比較神話学（デュメジル等）の三機能論検証の中核テクスト。"}])
_attach_cross("バガヴァッド・ギーター18章構成", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"三道統合哲学",
     "description":"ギーターはシャンカラ・ラーマーヌジャ・マドゥヴァのヴェーダーンタ三派論争の中核テクスト。"}])
_attach_cross("マハーバーラタ・シャーンティ・パルヴァ", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"古代政治経営思想",
     "description":"シャーンティ・パルヴァはアルタシャーストラと並ぶ古代インド政治経営思想の源泉。"}])
_attach_cross("パーリ三蔵（ティピタカ）", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"上座部哲学",
     "description":"パーリ三蔵は世界哲学史における上座部仏教哲学の根本典拠資料。"}])
_attach_cross("ナーガールジュナ『中論』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"中観哲学",
     "description":"中論はチベット中観派・東アジア三論宗・現代分析哲学（ガーフィールド）の中軸典拠。"}])
_attach_cross("ジャータカ547本生譚", [
    {"target_db":"Myth-Narratives","link_type":"shared_concept",
     "target_entity_name":"民話・寓話伝播",
     "description":"ジャータカは比較民話学において、イソップ寓話・パンチャタントラと並ぶ世界寓話伝播の源泉。"}])
_attach_cross("ウマースヴァーティ『タットヴァールタ・スートラ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ジャイナ哲学",
     "description":"タットヴァールタ・スートラはジャイナ哲学体系の根本綱要書として哲学史の中核資料。"}])
_attach_cross("アーディ・グラント／グル・グラント・サーヒブ", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"宗教共同体形成",
     "description":"アーディ・グラントはシク教共同体形成の人類学研究（マクラウド等）の中核資料。"}])
_attach_cross("ジャヤデーヴァ『ギータ・ゴーヴィンダ』詳細", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"宗教抒情詩学",
     "description":"ギータ・ゴーヴィンダは比較詩学において、雅歌・スーフィー詩と並ぶ宗教的エロス詩の中核。"}])
_attach_cross("カビール『ビージャク』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"ニルグナ・バクティ哲学",
     "description":"カビールはタゴール英訳を経て20世紀世界宗教思想史におけるニルグナ・バクティの中核象徴。"}])
_attach_cross("アンベードカル『カースト撲滅』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"カースト批判人類学",
     "description":"アンベードカルは20世紀インド人類学・社会学（ベテイユ・ディルク等）のカースト批判の中核典拠。"}])
_attach_cross("アンベードカル『ブッダとそのダンマ』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"新仏教運動哲学",
     "description":"『ブッダとそのダンマ』は20世紀ナヴァ・ヤーナ仏教の思想的中核典拠。"}])
_attach_cross("シュリー・オーロビンド『サーヴィトリー』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"統合ヨーガ哲学",
     "description":"サーヴィトリーは20世紀新ヴェーダーンタ・統合ヨーガ哲学の詩的展開として哲学史的に位置づけられる。"}])
_attach_cross("パンディタ・ラマーバーイー『高位カースト・ヒンドゥー女性』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"インド・フェミニズム人類学",
     "description":"ラマーバーイーは19-20世紀インド女性運動・フェミニズム人類学の祖型として参照される。"}])


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
        print(f"[c19-w19] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c19-w19] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c19-w19] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
        print(f"[c19-w19] concepts defined: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
