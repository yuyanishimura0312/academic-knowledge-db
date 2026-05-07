"""
LIT-DB Phase 2 — C19 Wave3: Indian Classical Literature (インド古典文学)
======================================================================
Inserts 40 representative concepts spanning 5 categories:
  A. ヴェーダ・サンスクリット古典 (8)
  B. サンスクリット叙事詩・詩学 (8)
  C. バクティ詩・中世 (8)
  D. 主要詩学・批評概念 (8)
  E. 近代諸言語文学・現代 (8)

subfield_id=12, code='lit_india', region='南西アジア'

Sources: GRETIL (Goettingen Register of Electronic Texts in Indian
Languages), SARIT (Search and Retrieval of Indic Texts), Sanskrit
Heritage, Encyclopaedia Iranica, Wikipedia (English) where canonical
concept entries exist.
"""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("ヴェーダ期", "Vedic Period", -1500, -500,
     "リグ・ヴェーダ等の聖典が口承で伝承された時代。サンスクリット詩文化の起源。"),
    ("古典サンスクリット期", "Classical Sanskrit", -500, 1200,
     "マハーバーラタ・ラーマーヤナ・カーリダーサ・バーナの叙事詩・カーヴィヤが成立した時代。"),
    ("中世バクティ期", "Medieval Bhakti", 700, 1700,
     "南インドのアルワール・ナーヤナールから北インドのカビール・トゥルシーダースまで、諸言語によるバクティ詩が栄えた時代。"),
    ("インド近代期", "Modern Indian", 1800, 1947,
     "ベンガル・ルネサンス、タゴール、プレームチャンドらによる諸言語文学の近代化。"),
    ("現代インド期", "Contemporary Indian", 1947, 2025,
     "独立後のダリット文学・英印文学・タミル現代文学等の多言語的展開。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — ヴェーダ・サンスクリット古典 (8)
# ===============================================================

add({
    "name_ja": "ヴェーダ",
    "name_en": "Veda",
    "name_original": "वेद",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "ヴェーダ期",
    "definition": "「知識」を意味するインド最古の聖典群で、リグ・サーマ・ヤジュル・アタルヴァの四ヴェーダから成る。BC1500年以降長期にわたり口承で完璧に伝承され、サンスクリット文学の起源かつインド宗教思想の根本聖典として位置づけられる。",
    "background": "アーリヤ系部族のインド亜大陸への移動に伴う祭祀・儀礼の言語化として成立した。",
    "development": "シュルティ（天啓）として絶対的権威を保ち、後のすべてのインド思想・文学の出発点となった。",
    "historical_context": "口承伝承の精緻さ（パダパータ等）はインド文化の言語的精度の源泉となった。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/1_rv/rv_hn00.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リグ・ヴェーダ",
    "name_en": "Rig Veda",
    "name_original": "ऋग्वेद",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "ヴェーダ期",
    "definition": "四ヴェーダ最古にして最重要の讃歌集。10巻1028讃歌から成り、インドラ・アグニ・ソーマ等への祭祀讃歌を中心とする。インド・ヨーロッパ語族最古の文学的記念碑の一つで、世界記憶遺産（ユネスコ）にも登録された。",
    "background": "インド・アーリヤ系祭官（ホートリ）の口承讃歌が編纂された。",
    "development": "後代の哲学・詩学・神話のすべての源泉となった。",
    "historical_context": "BC1500-1200年頃編纂されたとされる人類最古級の韻文記念碑。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/1_rv/rv_hn00.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ウパニシャッド",
    "name_en": "Upanishad",
    "name_original": "उपनिषद्",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "ヴェーダ期",
    "definition": "ヴェーダ文献の末尾を成す哲学的散文・韻文集。ブリハッド・アーラニヤカ、チャーンドーギャ等の古ウパニシャッド11篇が中核とされ、ブラフマン（宇宙原理）とアートマン（自我）の同一性、輪廻と解脱の思想を展開した。インド哲学の基礎文献。",
    "background": "ヴェーダ祭祀主義への内面化的応答として森林修行者の知の結晶として成立した。",
    "development": "ヴェーダーンタ哲学の出発点となり、ショーペンハウアー・エマーソン等を経て世界思想史に影響を与えた。",
    "historical_context": "祭祀から内省への転回を文学的・哲学的に体現した。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/4_upa/upanisad.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ブラーフマナ",
    "name_en": "Brahmana",
    "name_original": "ब्राह्मण",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "ヴェーダ期",
    "definition": "ヴェーダのサンヒター（讃歌集）に付随する祭祀注釈散文。アイタレーヤ・シャタパタ等が代表で、祭式の手順・象徴・神話的根拠を散文で詳述する。インド最古の散文文学であり、神話的物語の源泉でもある。",
    "background": "祭式の標準化と象徴解釈の必要から祭官学派が散文形式で編纂した。",
    "development": "アーラニヤカ・ウパニシャッドへと内省化され、サンスクリット散文の起源となった。",
    "historical_context": "韻文ヴェーダから散文哲学への過渡期文献。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/2_bra/satapath.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "イティハーサ（神話的物語）",
    "name_en": "itihasa",
    "name_original": "इतिहास",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "「かくの如く起こりき」を語源とするインド古典の歴史的・神話的物語ジャンル。マハーバーラタとラーマーヤナを正典的二大itihasaとし、神話・歴史・倫理・哲学を統合した叙事詩的散文・韻文体を指す。",
    "background": "口承叙事詩スータの伝承が文字化を経てジャンル化した。",
    "development": "プラーナと並ぶ「第五ヴェーダ」と位置づけられ、民衆教育の主要媒体となった。",
    "historical_context": "歴史と神話の境界を独自に組織するインド固有の叙述形式。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/mbh.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "プラーナ",
    "name_en": "Purana",
    "name_original": "पुराण",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "「古き物語」を意味する宗教的百科全書文学。マハー・プラーナ18篇（ヴィシュヌ、シヴァ、バーガヴァタ等）と多数のウパ・プラーナから成り、宇宙論・神話・系譜・聖地・儀礼を網羅する。バクティ運動の主要基盤となった。",
    "background": "ヴェーダの権威に届かない民衆的宗教知識を体系化する必要から発達した。",
    "development": "バーガヴァタ・プラーナはクリシュナ信仰の中核聖典となり、現代までインド大衆宗教の基盤を成す。",
    "historical_context": "サンスクリット古典文学と民衆信仰の架橋装置。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp_pu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シュルティ・スムリティ区分",
    "name_en": "shruti vs smriti",
    "name_original": "श्रुति / स्मृति",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "インド聖典分類の基本区分。シュルティ（天啓・「聞かれたもの」）はヴェーダ・ウパニシャッド等の絶対的権威を持つ聖典群、スムリティ（伝承・「記憶されたもの」）はマヌ法典・叙事詩・プラーナ等の人間的権威に依拠する文献群を指す。",
    "background": "聖典の権威階層を体系化する必要からブラフマン教の伝統が発達させた。",
    "development": "近代ヒンドゥー法の整理にも援用され、ダルマ・シャーストラ研究の基本枠組となった。",
    "historical_context": "インド文学・宗教における正典性の中核区分。",
    "primary_source_url": "https://en.wikipedia.org/wiki/%C5%9Aruti",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スートラ",
    "name_en": "sutra",
    "name_original": "सूत्र",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "「糸」「綱」を語源とする極度に圧縮されたアフォリズム形式の散文。パーニニ『アシュターディヤーイー』の文法スートラを最高峰とし、ヨーガ・ニヤーヤ・ヴェーダーンタ等の哲学諸派、ダルマ・シャーストラの諸領域で採用された。簡潔性が暗記伝承の前提となる。",
    "background": "口承伝承における暗記効率を最大化する必要から発達した。",
    "development": "全ての古典学知の体系化形式となり、長大な注釈伝統（バーシャ）を生んだ。",
    "historical_context": "インド学知の形式的核心。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/yoga/yogasutu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY B — サンスクリット叙事詩・詩学 (8)
# ===============================================================

add({
    "name_ja": "マハーバーラタ",
    "name_en": "Mahabharata",
    "name_original": "महाभारत",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "約10万シュローカ（韻文対句）から成る世界最長の叙事詩。クル族とパーンダヴァ族の戦争を主題とし、バガヴァッド・ギーターを内包する哲学的・倫理的百科全書。伝承上はヴィヤーサ作とされ、BC400頃-AD400頃に長期間で編纂された。",
    "background": "クル族・パンチャーラ族の歴史的戦争伝承が口承叙事詩として伝承され文字化された。",
    "development": "ジャワ・バリ等東南アジアにも広く伝播し、世界最大の宗教文学となった。",
    "historical_context": "「ここに無きものはどこにも無し」と自称する世界包摂的叙事詩。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/mbh.htm",
    "primary_source_type": "GRETIL critical text (Pune edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラーマーヤナ",
    "name_en": "Ramayana",
    "name_original": "रामायण",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "ヴァールミーキ作と伝承される7巻24,000シュローカの叙事詩。ラーマ王子の流浪、シーターのラーヴァナによる誘拐、ラーマの勝利と帰還を語る。理想王・理想夫としてのラーマ像を通じてインド倫理の規範を確立し、東南アジア全域に伝播した。",
    "background": "コーサラ国王朝伝承が口承で結晶化された。",
    "development": "トゥルシーダース『ラームチャリトマーナス』（ヒンディー版）、タイ『ラーマキエン』、ジャワ『カカウィン・ラーマーヤナ』等地域版を生んだ。",
    "historical_context": "東南アジアまで広がる文化圏の倫理的基盤を提供した。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/ramayana/ramayana.htm",
    "primary_source_type": "GRETIL critical text (Baroda edition)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "カーヴィヤ",
    "name_en": "kavya",
    "name_original": "काव्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "古典サンスクリットの洗練された宮廷詩・散文ジャンル。叙事詩マハーカーヴィヤ（カーリダーサ『クマーラ・サンバヴァ』等）、抒情詩、散文カターを含み、修辞美（アランカーラ）の駆使と感情（ラサ）の喚起を目指した。",
    "background": "古代インド宮廷の文化的洗練が詩的職人精神を生んだ。",
    "development": "ペルシア語ガザル・カンボジアの宮廷文学等、周辺文化圏に影響を与えた。",
    "historical_context": "サンスクリット古典美学の精華を担うジャンル。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/5_poetry/1_kavya/kalidasa/ksku_w.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ナータカ（劇）",
    "name_en": "nataka",
    "name_original": "नाटक",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "サンスクリット古典演劇のジャンル。バーサ、カーリダーサ『シャクンタラー』、シュードラカ『ムリッチャカティカ（土の小車）』、バヴァブーティ等の宮廷劇作家により発達した。バラタ『ナーティヤ・シャーストラ』が理論的基礎を提供し、サンスクリット・プラークリット・上演方式が制度化された。",
    "background": "古代インドの祭祀演劇が宮廷文化のなかで洗練された。",
    "development": "近代インド演劇・タゴール劇への系譜を形成した。",
    "historical_context": "ラサ理論の制度的実践場。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/5_poetry/2_drama/kalidasa/abhij_pu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラサ（味）",
    "name_en": "rasa",
    "name_original": "रस",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "「味」「情趣」を意味するインド古典詩学・演劇論の中核概念。バラタ『ナーティヤ・シャーストラ』が八種（後にシャーンタが加わり九種）のラサ（恋愛・笑・悲・怒・勇・恐・嫌・驚・寂静）を定義し、観客が舞台のバーヴァ（情）から普遍的情趣を味わう機制を理論化した。",
    "background": "演劇上演における観客の美的経験の本質を理論化する必要から発達した。",
    "development": "アビナヴァグプタの注釈で形而上学的に深化し、現代まで南アジア美学の中核を成す。",
    "historical_context": "古典的「読者反応理論」と評されるインド独自の受容美学。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/bhanats3.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バーヴァ（情）",
    "name_en": "bhava",
    "name_original": "भाव",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "ラサ理論の基礎概念で、登場人物・観客の心理的情動。スターイ・バーヴァ（基調情）、ヴィバーヴァ（誘発因）、アヌバーヴァ（表出）、ヴィヤビチャーリ・バーヴァ（過渡情）に分類され、それらの結合からラサ（味）が顕現するとされる。",
    "background": "心理現象を体系化することで美的経験の発生メカニズムを説明した。",
    "development": "アビナヴァグプタにより観客の主観的経験論として精緻化された。",
    "historical_context": "ラサ理論の構成要素として不可分。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/bhanats3.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ドヴァニ（暗示）",
    "name_en": "dhvani",
    "name_original": "ध्वनि",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "9世紀カシミールの詩学者アーナンダヴァルダナ『ドヴァニャーローカ』が体系化した、詩的言語の暗示的意味理論。文字通りの意味（ヴァーチャ）と派生的意味（ラクシャナー）を超え、含意される第三の意味（ヴィヤンギャ）こそが詩の魂であると主張した。",
    "background": "詩の本質を直接表現でなく暗示に求める伝統が修辞学（アランカーラ）の限界を超えて発達した。",
    "development": "アビナヴァグプタの注釈でラサ理論と統合され、サンスクリット詩学の頂点を形成した。",
    "historical_context": "西欧の含意論・記号論と独立に成立したインド独自の意味論。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/anandhsu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アランカーラ（修辞）",
    "name_en": "alankara",
    "name_original": "अलंकार",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "「装飾」を意味する古典サンスクリット修辞学の総称。バーマハ・ダンディン以来、シャブダ・アランカーラ（音的修辞：脚韻・頭韻等）とアルタ・アランカーラ（意味的修辞：直喩・隠喩・誇張等）に二分し、百を超える修辞技法を体系化した。",
    "background": "詩の魅力を分析するための実用的分類が学派を生んだ。",
    "development": "10世紀以降ドヴァニ理論に従属する位置に置かれたが、修辞分類装置として継承された。",
    "historical_context": "インド詩学の最古の理論的中核。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/dandkavu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — バクティ詩・中世 (8)
# ===============================================================

add({
    "name_ja": "バクティ運動",
    "name_en": "bhakti movement",
    "name_original": "भक्ति",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "個人的神への帰依（バクティ）を中核とする中世インドの宗教文学運動。7-9世紀の南インド・タミルのアルワール（ヴィシュヌ派）・ナーヤナール（シヴァ派）から始まり、12-17世紀に北インド諸言語へ拡大した。サンスクリット中心の正統に対抗し、地方語による民衆的霊性を確立した。",
    "background": "サンスクリット祭祀的バラモン教と仏教衰退のなかで個人救済の神学が要請された。",
    "development": "カビール、ミーラー・バーイー、トゥルシーダース、チャイタンニャ等が地方諸言語に展開した。",
    "historical_context": "インド諸言語文学の独立的発達と民衆宗教の確立に決定的役割を果たした。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Bhakti_movement",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ブラージ・バーシャー詩",
    "name_en": "Braj Bhasha poetry",
    "name_original": "ब्रज भाषा",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "ヤムナー川流域のブラージ地方（マトゥラー周辺）で発達したヒンディー語方言で書かれた、クリシュナ信仰の中世詩文学。スールダース『スール・サーガル』、ナンダダース、ヴィッタル・ナート等を代表とし、クリシュナとラーダーの愛遊（リーラー）を抒情的に展開した。",
    "background": "ヴラブハーチャーリヤのヴァッラバ派・ニンバールカ派など、クリシュナ信仰諸派が地方語詩を後援した。",
    "development": "近代ヒンディー文学の古典的源泉となり、現代の宗教歌謡（バジャン）にも継承される。",
    "historical_context": "クリシュナ信仰の文学的中核を形成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Surdas",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "タミル・サンガム文学",
    "name_en": "Tamil Sangam literature",
    "name_original": "சங்க இலக்கியம்",
    "original_script": "tamil",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "BC300頃-AD300頃のタミル古典文学群。八つのアンソロジー（エットゥトハイ）と十の長詩（パットゥパーットゥ）から成り、内的世界（アハム：恋愛）と外的世界（プラム：戦争・徳）の主題分類を持つ。サンスクリット中心の北インド古典伝統と独立に成立したドラヴィダ系古典文学。",
    "background": "古代タミル王朝（チェーラ・チョーラ・パーンディヤ）の文化的後援が「サンガム（詩人会議）」を成立させたとされる。",
    "development": "中世タミル・バクティ詩、近代タミル・ナショナリズムの文学的基盤となった。",
    "historical_context": "サンスクリット中心主義に対抗するドラヴィダ系古典の存在を確立した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sangam_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アルワール詩人",
    "name_en": "Alvars",
    "name_original": "ஆழ்வார்",
    "original_script": "tamil",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "6-9世紀の南インドで活動した12人のヴィシュヌ派バクティ詩人。アンダール（女性詩人）、ナンマールワール、ティルマンガイらが代表で、4000編から成るタミル語讃歌集『ナーラーイラ・ディヴィヤ・プラバンダム』を残した。北インドのバクティ運動に先行した。",
    "background": "南インドのヴィシュヌ寺院文化と民衆信仰がタミル語詩文学を生んだ。",
    "development": "シュリー・ヴァイシュナヴァ派の正典となり、ラーマーヌジャ哲学の文学的基盤を提供した。",
    "historical_context": "インド・バクティ運動の発祥源。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Alvars",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ナーヤナール詩人",
    "name_en": "Nayanars",
    "name_original": "நாயன்மார்",
    "original_script": "tamil",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "6-9世紀の南インドで活動した63人のシヴァ派バクティ詩人聖者。アッパル、サンバンダル、スンダラル、マーニッカヴァーチャカルらの讃歌が『テーヴァーラム』『ティルヴァーチャカム』に集成され、後のシヴァ・シッダーンタ哲学の聖典基盤を成した。",
    "background": "ナーヤナールはアルワールと並行してタミル・シヴァ寺院文化を中核に活動した。",
    "development": "シヴァ・シッダーンタ12聖典体系の中核に位置づけられ、現代タミル・シヴァ派の信仰実践を支える。",
    "historical_context": "南インド・シヴァ信仰の文学的・神学的基盤。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nayanars",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "カビール",
    "name_en": "Kabir",
    "name_original": "कबीर",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "15世紀の北インドの神秘詩人（伝承1398-1518）。ヒンドゥー教徒とイスラーム教徒の両者から尊崇され、形なき絶対者への信仰を地方ヒンディー語で歌った。短詩形式ドーハー、サキ、シャブドで知られ、現代に至るまで民衆口承に生きる。",
    "background": "ヒンドゥー・イスラーム両伝統の混淆地ヴァーラーナシーで織職人として育ち、ラーマーナンダの弟子と伝えられる。",
    "development": "シーク教典『グル・グラント・サーヒブ』に収録され、カビール・パンタ宗派を生んだ。",
    "historical_context": "インド宗教融合（サマンヴァヤ）の文学的象徴。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kabir",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ミーラー・バーイー",
    "name_en": "Mira Bai",
    "name_original": "मीराबाई",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "16世紀のラージプート王女・クリシュナ信仰女性詩人（伝承1498-1547）。クリシュナを唯一の夫と定めて家を捨て、ラジャスターニー・ブラージ語の抒情的バクティ歌（パダ）を残した。女性的バクティの典型として現代まで尊崇される。",
    "background": "メワール王家に嫁ぎながら王家の宗派的圧迫と寡婦慣習に抗して放浪生活に入った。",
    "development": "現代インドの女性独立性・芸術的自由の象徴的人物となった。",
    "historical_context": "中世インド女性の宗教的・芸術的主体性を体現した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mirabai",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "トゥルシーダース",
    "name_en": "Tulsidas",
    "name_original": "तुलसीदास",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "中世バクティ期",
    "definition": "16-17世紀の北インド詩人（1532-1623）。アワディー方言のヒンディー語による『ラームチャリトマーナス』はラーマーヤナの中世的再話で、北インド民衆のラーマ信仰の聖典となった。サンスクリット文化と地方語民衆文化の架橋を象徴する。",
    "background": "ヴァーラーナシーを拠点にラーマ信仰のバクティ運動を主導した。",
    "development": "現代まで北インドのラーマ・リーラー（演劇上演）の基本台本として上演される。",
    "historical_context": "北インド・ヒンドゥー文化の中核聖典の一つを生んだ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tulsidas",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY D — 主要詩学・批評概念 (8)
# ===============================================================

add({
    "name_ja": "ナーティヤ・シャーストラ",
    "name_en": "Natyashastra",
    "name_original": "नाट्यशास्त्र",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "聖賢バラタ作と伝承される古代インドの演劇・舞踊・音楽論の集大成（BC200頃-AD200頃成立）。36章6000シュローカ前後から成り、ラサ・バーヴァ理論、舞台構造、所作・台詞・装飾、音楽・舞踊の全要素を体系化した。世界最古の演劇理論書の一つ。",
    "background": "古代インドの宮廷演劇と祭祀演劇の伝統を理論化する必要から成立した。",
    "development": "アビナヴァグプタ『アビナヴァ・バーラティー』（10世紀）が決定的注釈を提供し、近代まで南アジア舞台芸術の規範を成す。",
    "historical_context": "ラサ理論の起源を成す根本聖典。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/bhanats3.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ドヴァニャーローカ",
    "name_en": "Dhvanyaloka",
    "name_original": "ध्वन्यालोक",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "9世紀カシミールのアーナンダヴァルダナによる詩学論書。詩の魂は文字通りの意味でも修辞でもなく、暗示される意味（ドヴァニ）にあると主張し、サンスクリット詩学を装飾論（アランカーラ・シャーストラ）から意味論的詩学へと転回させた金字塔的著作。",
    "background": "アランカーラ理論の限界とラサ経験の本質を統合的に説明する必要から成立した。",
    "development": "アビナヴァグプタの注釈『ロチャナ』により決定的地位を獲得した。",
    "historical_context": "サンスクリット詩学の頂点。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/anandhsu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラサ・シッダーンタ（味の理論）",
    "name_en": "rasa siddhanta",
    "name_original": "रस सिद्धान्त",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "バラタからアビナヴァグプタに至るインド古典美学の中核理論。観客が舞台のバーヴァ（情）から普遍化された情趣（ラサ）を受け取る経験論で、アビナヴァは個人的情動を脱した普遍的「味わい」をブラフマン経験と類比的に位置づけた。",
    "background": "演劇上演における観客美的経験の説明から発達した。",
    "development": "現代インド美学・パンディット・ジャガンナータまで継承された。",
    "historical_context": "西欧美学と独立に成立した受容論的美学。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/anandhsu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヴァクロークティ（曲言）",
    "name_en": "vakrokti",
    "name_original": "वक्रोक्ति",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "11世紀カシミールのクンタカが『ヴァクロークティ・ジーヴィタ』で提唱した詩論。「曲がった発話」を意味し、詩の本質は表現の独創的逸脱（直接言明からの「曲げ」）にあるとした。ドヴァニ理論への対抗的代替理論として注目される。",
    "background": "詩の独自性を意味論ではなく表現法に見出す視点から発達した。",
    "development": "ロシア・フォルマリストの「異化」概念との並行性が現代に再評価されている。",
    "historical_context": "サンスクリット詩学内の代替的詩本質論。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kuntaka",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "リーティ（風格）",
    "name_en": "riti",
    "name_original": "रीति",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "9世紀のヴァーマナが『カーヴィヤーランカーラ・スートラ』で詩学の中核に据えた「文体・風格」概念。ヴァイダルビー（南方優美調）、ガウディー（東方華麗調）、パーンチャーリー（中道調）等の地域的文体類型を区別し、文体を詩の魂と位置づけた。",
    "background": "地域的詩風の差異を理論化する必要から発達した。",
    "development": "後にドヴァニ理論に従属したが、北インド・ヒンディー詩学の「リーティ・カーヴィヤ」流派に継承された。",
    "historical_context": "サンスクリット文体論の独自的展開。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Vamana_(scholar)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "アウチティヤ（適切性）",
    "name_en": "aucitya",
    "name_original": "औचित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "11世紀カシミールのクシェーメンドラが『アウチティヤ・ヴィチャーラ・チャルチャー』で論じた「適切性」概念。語彙・修辞・性格描写・風景・行動などすべての詩的要素は文脈に応じた「適切さ」を要求するとし、適切性こそラサ経験の前提条件とした。",
    "background": "ラサ理論の前提条件を明確化する必要から提示された。",
    "development": "現代の文体論的「適切性」概念にも対応する分析装置を提供した。",
    "historical_context": "サンスクリット詩学のメタ規範概念。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kshemendra",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "グナ（質）",
    "name_en": "guna",
    "name_original": "गुण",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "サンスクリット詩学における詩的徳目（質）の概念。ダンディン以来、明晰（プラサーダ）・優美（マーダリヤ）・力強さ（オージャス）等10種前後の徳目が分類され、文体（リーティ）の構成要素として位置づけられた。",
    "background": "詩文の優れた性質を体系的に分析する必要から発達した。",
    "development": "アランカーラ・グナ・ドーシャの三項関係でサンスクリット詩学の評価軸を構成した。",
    "historical_context": "詩的価値の規範的分類装置。",
    "primary_source_url": "http://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/5_alank/dandkavu.htm",
    "primary_source_type": "GRETIL critical text",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "ドーシャ（瑕疵）",
    "name_en": "dosha",
    "name_original": "दोष",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "古典サンスクリット期",
    "definition": "サンスクリット詩学における詩的欠点・瑕疵の概念。語彙的・文法的・意味的・修辞的・ラサ的不適切等が分類され、グナ（徳目）と対をなす否定的評価軸を構成する。マンマタ『カーヴィヤ・プラカーシャ』が標準的分類を確立した。",
    "background": "詩文の規範違反を体系化する分析的必要から発達した。",
    "development": "近代インド学校の詩学教育の中核項目となった。",
    "historical_context": "古典詩学の規範的・批評的中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mammata",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY E — 近代諸言語文学・現代 (8)
# ===============================================================

add({
    "name_ja": "ベンガル・ルネサンス",
    "name_en": "Bengali Renaissance",
    "name_original": "বঙ্গীয় নবজাগরণ",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "19世紀後半から20世紀前半のベンガル地方に起こった文学・思想・社会改革の総合的近代化運動。ラーム・モーハン・ローイの社会改革、バンキム・チョンドロ・チョットパッダエの近代ベンガル小説、タゴールの世界文学への展開を含み、インド近代文学の中核的源泉となった。",
    "background": "東インド会社統治下のカルカッタを拠点に英語教育を受けたベンガル知識人層が形成された。",
    "development": "ベンガル国民意識からインド民族独立運動の知的基盤を提供した。",
    "historical_context": "アジアの近代化と文学的近代の交差点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Bengali_Renaissance",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "タゴール『ギーターンジャリ』",
    "name_en": "Tagore's Gitanjali",
    "name_original": "গীতাঞ্জলি",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ロビンドロナト・タゴール（1861-1941）のベンガル語宗教抒情詩集（1910）。タゴール自身による英語自由詩翻訳（1912）がW・B・イェイツの序文を得て世界的に流通し、1913年アジア初のノーベル文学賞をもたらした。バクティ伝統と西欧近代抒情の融合を体現する。",
    "background": "ベンガル・ルネサンスの精神的成熟点で、インド古典伝統の世界文学への翻訳的提示が達成された。",
    "development": "タゴール翻訳論を通じて翻訳論・世界文学論の主要事例となった。",
    "historical_context": "アジア文学の世界文学への参入の象徴的契機。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Gitanjali",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "プレームチャンド『ニルマラー』",
    "name_en": "Premchand's Nirmala",
    "name_original": "निर्मला",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ヒンディー・ウルドゥー文学の近代写実主義の祖プレームチャンド（1880-1936）の長編小説（1928）。年若い女性ニルマラーが年長の寡夫と結婚を強いられる悲劇を通じて、植民地下インドの女性問題・婚姻制度・社会改革の必要性を写実的に描いた。",
    "background": "ガンディー期インド社会改革運動の文学的応答として書かれた。",
    "development": "近代ヒンディー小説の規範的作品となり、ヒンディー文学教育の中核を成す。",
    "historical_context": "プレームチャンドはガンディー的な社会改革理念とロシア社会主義写実主義の双方の影響を受けた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Premchand",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "チャーヤーヴァード（ヒンディー文学運動）",
    "name_en": "Chhayavad",
    "name_original": "छायावाद",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "1920-30年代のヒンディー語ロマン主義詩運動。「影主義」を意味し、ジャヤシャンカル・プラサード、スーリヤカーント・トリパーティー・ニラーラー、スミトラーナンダン・パント、マハーデーヴィー・ヴァルマーの「四柱」が中核を成した。バクティ伝統と英ロマン主義の融合により近代ヒンディー詩を確立した。",
    "background": "リーティ・カーヴィヤ（装飾詩）への反動と西欧ロマン主義受容が運動を生んだ。",
    "development": "現代ヒンディー詩の主要源泉となり、進歩主義詩運動・実験主義詩への基盤を提供した。",
    "historical_context": "近代ヒンディー詩の核心的近代化運動。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Chhayavaad",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ウルドゥー近代ガザル",
    "name_en": "modern Urdu ghazal",
    "name_original": "غزل",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "19世紀以降のウルドゥー語ガザル詩の近代的展開。ミルザー・ガーリブ（1797-1869）が古典ガザルを哲学的内省詩へと深化させ、ファイズ・アフマド・ファイズ（1911-1984）はガザルを革命詩・抵抗詩へと展開した。インド・パキスタン両国で愛唱される。",
    "background": "ムガル帝国末期デリー・ラクナウーの宮廷詩文化が植民地化のなかで近代化を経験した。",
    "development": "現代インド亜大陸の歌謡（カッワーリー、映画歌謡）の文学的中核となった。",
    "historical_context": "ペルシア・アラブ古典伝統と近代インド亜大陸文学の架橋。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mirza_Ghalib",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ダリット文学",
    "name_en": "Dalit literature",
    "name_original": "दलित साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "1960年代以降、被差別カースト（ダリット、旧称「不可触民」）出身作家による反カースト・反差別文学運動。マハーラーシュトラ州マラーティー語のダリット・パンサー運動を起点とし、ナームデーオ・ダサル詩、シャラン・クマール・リムバーレ自伝『アクラマシャク』等が代表作。",
    "background": "B・R・アンベードカル（1891-1956）の社会改革思想と1960年代の米国黒人公民権運動の影響から運動が生まれた。",
    "development": "ヒンディー語・タミル語・カンナダ語等諸言語のダリット作家へ拡大し、インド文学の正典再考を促した。",
    "historical_context": "サンスクリット中心・上層カースト中心の正典に対する根本的挑戦。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Dalit_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "英印文学",
    "name_en": "Indo-Anglian literature",
    "name_original": "Indian English literature",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "インド人作家による英語文学。R・K・ナーラーヤン、ムルク・ラージ・アーナンドの近代写実主義、サルマーン・ラシュディ『真夜中の子供たち』（1981）のマジック・リアリズム、アルンダティ・ロイ『小さきものたちの神』、アミタヴ・ゴーシュらが代表的存在。20世紀末に世界文学の中心の一つを形成した。",
    "background": "植民地下英語教育の遺産が独立後にインド人英語作家を生んだ。",
    "development": "ラシュディ以降、ブッカー賞・ノーベル賞候補が続出する世界文学の中心の一つとなった。",
    "historical_context": "ポストコロニアル文学の世界的代表事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indian_English_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "現代タミル文学",
    "name_en": "modern Tamil literature",
    "name_original": "நவீன தமிழ் இலக்கியம்",
    "original_script": "tamil",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "20世紀以降のタミル語文学。バーラティー（1882-1921）の革命詩・近代化詩、プドゥマイピッタンの近代短編、ジャヤカーンタンの社会派小説、現代のC・S・ラクシュミー（アンバイ）、ペルマール・ムルガンらの多元的展開を含む。サンガム古典伝統の継承と近代化の交差を示す。",
    "background": "サンガム古典伝統と20世紀ドラヴィダ・ナショナリズムが現代タミル文学の独自性を生んだ。",
    "development": "21世紀ペルマール・ムルガンの『マーダルラル・ピラヴィ（半女神）』論争が示すように、伝統と現代の緊張が続く。",
    "historical_context": "サンスクリット中心主義に独立する南インド文学の現代的展開。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tamil_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (12+ entries per requirement)
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "ラサ（味）": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "観客のバーヴァからラサが顕現する受容論的美学は古典的「読者反応理論」と評され、AI生成テクストへの読者経験論の理論的先駆として再評価される。",
         "ai_phenomenon": "AI生成コンテンツへの受容者経験の理論化"},
    ],
    "ラサ・シッダーンタ（味の理論）": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "アビナヴァグプタの普遍化された美的経験論は、AI生成テクストにおける受容経験の構造分析に応用可能な独自的枠組を提供する。",
         "ai_phenomenon": "AI生成コンテンツの普遍化された美的経験"},
    ],
    "ドヴァニ（暗示）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "字義を超えた暗示こそ詩の魂とするドヴァニ理論は、LLMの含意生成・プロンプト含意理解の理論的枠組として再考される。",
         "ai_phenomenon": "LLMの含意・暗示生成と意味解釈"},
    ],
    "バクティ運動": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "個人的神への帰依を主体性の核に据えるバクティの主体論は、AI時代における人間主体の超越性・関係性の再考と直接接続する。",
         "ai_phenomenon": "AI仲介関係性における主体性の再考"},
    ],
    "ダリット文学": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "被差別主体の経験的真正性を文学的真理の核に据えるダリット文学は、AI生成テクストの真正性・経験的根拠論争と直接対応する。",
         "ai_phenomenon": "AI生成テクストにおける経験的真正性の問い"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "周縁的主体の発話権を中心化するダリット文学の主体論は、AI時代の発話主体・代表性の問題と構造的に類比される。",
         "ai_phenomenon": "AI生成テクストにおける周縁的主体の発話"},
    ],
    "ヴェーダ": [
        {"axis": "正典", "status": "partial",
         "rationale": "口承伝承の絶対的正確性を基盤とするシュルティ正典概念は、AIコーパスの完全性・正典化機制との部分的類比を提供する。",
         "ai_phenomenon": "AI訓練コーパスの正典化機制"},
    ],
    "ウパニシャッド": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "アートマンとブラフマンの同一性を説くウパニシャッド主体論は、AI時代の自己・宇宙・知性の関係再考の哲学的源泉となる。",
         "ai_phenomenon": "AI時代の自己と知性の関係再考"},
    ],
    "アランカーラ（修辞）": [
        {"axis": "言語", "status": "partial",
         "rationale": "百を超える修辞技法の体系化はLLMの表現生成能力分析の理論的基盤として部分的に類比される。",
         "ai_phenomenon": "LLMの修辞的表現生成能力"},
    ],
    "イティハーサ（神話的物語）": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "歴史と神話を統合する叙事詩的散文形式は、AI時代の事実・物語・証言の境界再編問題と直接接続する。",
         "ai_phenomenon": "AI生成における事実・物語境界の流動化"},
    ],
    "英印文学": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "母語経験を植民地言語英語で表現する英印文学の翻訳的本質は、AI翻訳が新たな多言語表現様式を生む現代に直接対応する。",
         "ai_phenomenon": "AI翻訳による多言語的表現実践"},
        {"axis": "真正性", "status": "partial",
         "rationale": "「英語で書くインド」の真正性論争はAI生成テクストの文化的真正性論争と並行する。",
         "ai_phenomenon": "AI翻訳・生成における文化的真正性"},
    ],
    "ベンガル・ルネサンス": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "印刷技術と翻訳運動を通じた近代化はAI翻訳・受容変容の現代と構造的に類比される。",
         "ai_phenomenon": "AI翻訳による文化的近代化と受容再編"},
    ],
    "タゴール『ギーターンジャリ』": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "作者自身による翻訳が原作と独立した世界文学的価値を生む現象は、AI翻訳時代の翻訳論・作者性論議と直接接続する。",
         "ai_phenomenon": "AI翻訳における原作・翻訳・作者性の再編"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>= 8)
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("ラサ（味）", "PT", "shared_concept", "rasa / reader response",
     "インド古典美学のラサ理論は西欧読者反応理論と並ぶ受容美学の独立した伝統として詩学・批評理論DBと共有される。"),
    ("ドヴァニ（暗示）", "PT", "shared_concept", "implicature / poetic meaning",
     "ドヴァニ理論は西欧の含意論・記号論と独立に成立した暗示意味論として詩学DBの基盤的対比対象となる。"),
    ("アランカーラ（修辞）", "PT", "shared_concept", "rhetoric / tropes",
     "サンスクリット修辞学は古代ギリシャ修辞学・アラブ・バラーガと並ぶ独立した修辞理論伝統。"),
    ("ヴェーダ", "PHIL", "shared_concept", "Hindu philosophy / shruti",
     "ヴェーダはインド哲学の根本聖典として哲学DBと一体に発展した。"),
    ("ウパニシャッド", "PHIL", "shared_concept", "Vedanta / Brahman-Atman",
     "ウパニシャッドはヴェーダーンタ哲学の出発点として哲学DBと完全共有される。"),
    ("バクティ運動", "AN", "shared_concept", "religious movement / vernacular",
     "バクティ運動の地方語による民衆宗教運動は人類学的宗教運動研究の中核的対象。"),
    ("イティハーサ（神話的物語）", "Myth-Narratives", "shared_concept", "epic / itihasa",
     "マハーバーラタ・ラーマーヤナの叙事詩構造は神話・物語DBと完全共有される世界叙事詩素材。"),
    ("プラーナ", "Myth-Narratives", "shared_concept", "puranic mythology",
     "18マハー・プラーナの宇宙論・神話・系譜は神話・物語DBの主要素材。"),
    ("バクティ運動", "PHIL", "parallel", "personal devotion / theism",
     "個人的神への帰依を哲学化したバクティ思想はラーマーヌジャ・マドヴァ哲学と一体に発展した。"),
    ("ダリット文学", "AN", "shared_concept", "caste system / subaltern voice",
     "カースト制度下の被差別経験を扱うダリット文学は人類学的サバルタン研究と直接接続する。"),
]


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main() -> None:
    with LitDB() as db:
        # Seed periods
        period_id_by_key: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=nj, region="南西アジア",
                start_year=sy, end_year=ey,
                name_en=ne, description=desc,
            )
            period_id_by_key[nj] = pid

        # Insert concepts
        name_to_id: dict[str, int] = {}
        inserted = 0
        skipped = 0
        for entry in CONCEPTS:
            ent = dict(entry)
            period_key = ent.pop("period_key", None)
            if period_key:
                ent["period_id"] = period_id_by_key.get(period_key)
            try:
                cid = db.insert_concept(**ent)
                name_to_id[ent["name_ja"]] = cid
                inserted += 1
            except LitDBError as e:
                print(f"[error] insert failed for {ent.get('name_ja')!r}: {e}")
                skipped += 1

        # Fourth-transform tags
        ft_count = 0
        for name_ja, tags in FOURTH_TRANSFORM_TAGS.items():
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for fourth-transform: {name_ja!r}")
                continue
            for tag in tags:
                try:
                    db.tag_fourth_transform(
                        cid,
                        axis=tag["axis"],
                        status=tag["status"],
                        rationale=tag.get("rationale"),
                        related_ai_phenomenon=tag.get("ai_phenomenon"),
                    )
                    ft_count += 1
                except LitDBError as e:
                    print(f"[error] tag failed for {name_ja!r}/{tag['axis']}: {e}")

        # Cross-domain links
        cd_count = 0
        for name_ja, target_db, link_type, target_name, desc in CROSS_DOMAIN_LINKS:
            cid = name_to_id.get(name_ja)
            if not cid:
                print(f"[warn] no concept id for cross-domain: {name_ja!r}")
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=target_db,
                    link_type=link_type,
                    target_entity_name=target_name,
                    description=desc,
                )
                cd_count += 1
            except LitDBError as e:
                print(f"[error] cross-domain failed for {name_ja!r}: {e}")

        print(f"\n=== C19 India Classical completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        print(f"  total concepts in subfield 12: ", end="")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 12"
        ).fetchone()
        print(row["c"])


if __name__ == "__main__":
    main()
