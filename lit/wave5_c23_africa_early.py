"""
LIT-DB Phase 2 — C23: Africa Early (アフリカ文学・口承伝統と植民地期)
========================================================================
40 concepts across five categories:
  A. 口承伝統 (8): griot, mvet, ifa divination poetry, praise poetry,
     folktale, ananse stories, izibongo, oriki
  B. 主要主題・世界観 (8): ubuntu, négritude, African personality,
     ethnophilosophy, ancestral memory, totemism in narrative,
     communal vs individual self, oral-literate divide
  C. 植民地期文学 (8): mission school literature, francophone West African
     early novels, anglophone West African early novels, Onitsha market
     literature, South African early black writing, Lusophone African early,
     Hausa Kano press literature, Kiswahili early modern
  D. ネグリチュード・反植民地運動 (8): Présence Africaine, négritude vs
     Tigritude, anti-colonial verse, Aimé Césaire Cahier, Senghor rhythm,
     David Diop, Birago Diop contes, Camara Laye L'Enfant noir
  E. 主要批評概念 (8): oral genres taxonomy, pidginization in literature,
     language choice debate, decolonizing the mind, African literary aesthetics,
     ujamaa literature, dialogic ancestral form, oraliture

Sources used:
  - African Storybook (https://africanstorybook.org/)
  - AJOL — African Journals Online (https://www.ajol.info/)
  - JSTOR (public abstracts)
  - UNESCO ICH Lists (https://ich.unesco.org/)
  - Présence Africaine (https://www.presenceafricaine.com/)
  - Wikipedia (public archive)

subfield_id=15, code='lit_africa', region='グローバルサウス'
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("アフリカ口承伝統期", "African Oral Tradition (pre-colonial)", -1000, 1880,
     "サハラ以南アフリカの口承伝統が世代間で伝承された深い時間。グリオ・吟遊詩人・宮廷詩人による系譜・神話・歴史の語り。"),
    ("植民地期", "Colonial Period in Africa", 1880, 1960,
     "ベルリン会議（1884-85）以降の本格的植民地化期。ミッションスクール文学・初期近代小説・新聞文芸の成立期。"),
    ("ネグリチュード・反植民地期", "Négritude & Anti-Colonial Era", 1930, 1970,
     "1930年代のパリ留学生グループに端を発するネグリチュード運動と独立闘争期の文学。"),
    ("独立後初期", "Early Post-Independence", 1960, 1980,
     "アフリカ諸国の独立直後の文学的高揚期。脱植民地化・言語論争・新しい美学の模索。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


REGION = "グローバルサウス"
SUBFIELD = "lit_africa"


# ===============================================================
# A. 口承伝統 (8)
# ===============================================================

add({
    "name_ja": "グリオ",
    "name_en": "griot",
    "name_original": "griot / jeli",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "西アフリカ・マンデ語圏（マリ・セネガル・ギニア等）の世襲的語り部・系譜記録者・宮廷詩人。「ジェリ（jeli）」「ジャリ（jali）」とも呼ばれ、コラ・ンゴニ等の弦楽器を伴奏しつつ、王家の系譜・歴史叙事詩（『スンジャタ叙事詩』等）・社会的記憶を口承で伝える。文字を持たぬ社会の歴史記録の中核を担い、共同体の記憶機関として機能した。",
    "background": "マリ帝国（13-16世紀）以来の宮廷制度に深く組み込まれた職能的階層。",
    "development": "現代では音楽家・歴史家・現代作家として活動範囲を広げる（ママドゥ・クヤテ等）。",
    "historical_context": "UNESCO無形文化遺産に関連語が登録され、世界の口承伝統の代表事例とされる。",
    "primary_source_url": "https://ich.unesco.org/en/RL/cultural-space-of-the-yaaral-and-degal-00132",
    "primary_source_type": "UNESCO ICH related listings",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "個人作者ではなく世襲的職能と共同体記憶の結節点として作用する。AIによる集合的記憶の生成と構造的に類比される。",
         "related_ai_phenomenon": "LLMの集合的記憶生成・著作権の集合性"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "演奏ごとに変奏される定型即興形式は固定テクスト概念を解体する。",
         "related_ai_phenomenon": "プロンプト依存の生成多様性"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Mande oral history / Hampaté Bâ",
         "description": "アマドゥ・ハンパテ・バの『口承の言葉は燃える』など人類学的証言研究と直結。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral-formulaic theory",
         "description": "ロード＝パリーの口承定型詩学のアフリカ的検証事例。"},
    ],
})

add({
    "name_ja": "ムヴェット",
    "name_en": "mvet",
    "name_original": "mvet",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "中央アフリカのファン族（カメルーン・ガボン・赤道ギニア）に伝わる長大な英雄叙事詩、およびその伴奏楽器（弦楽器）の名。エコン・エンドン（不死の人々）と地上の人々との戦いを語る『ムヴェット叙事詩』を中核に、夜通しの語りで演じられる。20世紀後半にツォギモ・エネ・ンクァ等の語り手の記録が進められた。",
    "background": "ファン族の伝統的世界観を凝縮する叙事詩文化として継承された。",
    "development": "コンゴ系作家ダニエル・アシマ・ムベゴらが文字テクスト化・翻訳を進めた。",
    "historical_context": "中央アフリカ口承文学の代表事例として人類学的・文学的に注目されている。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mvet",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "音楽・身体・声・物語が分離不能に統合された複合メディアであり、テクスト中心主義を解体する。",
         "related_ai_phenomenon": "マルチモーダル生成AI"},
    ],
})

add({
    "name_ja": "イファ卜占詩",
    "name_en": "Ifá divination poetry",
    "name_original": "ese Ifá",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "ヨルバ族（ナイジェリア南西部・ベナン等）のイファ卜占体系で詠まれる詩文群。256の「オドゥ」と呼ばれる卜占記号それぞれに数千の「エセ・イファ（卜占詩）」が結びつき、卜占師（ババラウォ）が記憶のなかから引き出して問題に応答する。哲学・歴史・倫理を内包する膨大な口承知識体系。",
    "background": "ヨルバ宗教と知の中核として数百年継承されてきた。",
    "development": "ウォーレ・ショインカ、ワンデ・アビンボラ等が文学的・学問的に再記述している。",
    "historical_context": "2005年にUNESCO世界無形遺産（人類の口承および無形遺産の傑作）に宣言された。",
    "primary_source_url": "https://ich.unesco.org/en/RL/ifa-divination-system-00146",
    "primary_source_type": "UNESCO ICH official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "読者・問い手・状況によって毎回異なる詩編が選択・演奏される非線形的・確率的物語形式。",
         "related_ai_phenomenon": "プロンプト依存型生成・確率的物語化"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "卜占師の記憶と聴き手の問いが共同で意味を生成する対話的形式。",
         "related_ai_phenomenon": "対話的AI生成"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Yoruba divination philosophy",
         "description": "ヨルバ哲学の口承知識体系として直結。"},
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "divination narratives",
         "description": "卜占を通じた物語生成の世界比較研究と接続。"},
    ],
})

add({
    "name_ja": "賛歌詩",
    "name_en": "praise poetry",
    "name_original": "imbongi / jali praise",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "南部アフリカ（ズールー・コーサ・バソト等）と西アフリカ（マンデ等）に共通する、王・首長・英雄・氏族・動物・場所等を称える詩形式。南部ではimbongi（コーサ）・isibongo（ズールー）の呼称で、宮廷儀礼や政治集会で詠唱される。即興・定型・反復・語勢の累積を特徴とし、社会的記憶と政治的批評の両機能を持つ。",
    "background": "シャカ王時代以降のズールー社会で高度に発達した。",
    "development": "ネルソン・マンデラ就任式でも公式に詠唱され、現代南アフリカ政治儀礼に継承されている。",
    "historical_context": "21世紀のアフリカ国家儀礼でも生きた伝統として機能する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Praise_poetry",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "praise poetics",
         "description": "詩学における称揚詩・頌詩の比較研究と接続。"},
    ],
})

add({
    "name_ja": "民話",
    "name_en": "African folktale",
    "name_original": "folktale / conte",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "サハラ以南アフリカ全域で夕食後・葬送・季節儀礼等に語られる散文説話の総称。動物寓話（蜘蛛・兎・亀・ハイエナ等）・由来譚・教訓譚を中心とし、子どもの社会化・倫理教育を担う。バントゥ系・ニジェール・コンゴ系・ナイル＝サハラ系の各語族で類型変奏を持つ。",
    "background": "アフリカ各社会の家庭的口承の中核ジャンル。",
    "development": "20世紀にエイモス・チュチュオラ、ビラゴ・ディオプ等が文学的に書き直した。",
    "historical_context": "African Storybookプロジェクト等で多言語デジタル版が公開されている。",
    "primary_source_url": "https://africanstorybook.org/",
    "primary_source_type": "African Storybook",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "アナンセ物語",
    "name_en": "Ananse stories",
    "name_original": "Anansesem",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "ガーナ・コートジボワール等のアカン語族（アシャンティ・ファンテ）に伝わる、蜘蛛のアナンセを主人公とするトリックスター物語群。「アナンセセム（アナンセ物語）」とも。狡知と愚行を兼ねるアナンセは創造神ニャメと交渉し物語を地上に持ち帰った文化英雄として描かれる。奴隷貿易を経てカリブ海地域にも伝播した。",
    "background": "アシャンティ王国の口承文学の中核を構成する。",
    "development": "現代の児童文学・批評・カリブ海文学（ブラスウェイト等）に継承されている。",
    "historical_context": "アフリカディアスポラの記憶基盤となる象徴的物語群でもある。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Anansi",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "trickster archetype",
         "description": "世界トリックスター比較研究のアフリカ的中核事例。"},
    ],
})

add({
    "name_ja": "イジボンゴ",
    "name_en": "izibongo",
    "name_original": "izibongo",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "ズールー語で「賛辞・讃詠詩」を意味する公式詩形式。王・戦士・部族・氏族の系譜と功績を、定型句と即興を織り交ぜて吟ずる。imbongi（吟遊詩人）が宮廷・公的集会で詠唱し、シャカ王以降の南部アフリカ政治儀礼の基盤となった。文学批評ではマザーシ・カネネ等の研究で詩形式が詳細に分析された。",
    "background": "ズールー王国の宮廷詩学として19世紀に高度化した。",
    "development": "現代南アフリカでマンデラ追悼式でも詠唱されるなど生きた伝統として持続している。",
    "historical_context": "アパルトヘイト後の国家儀礼にも組み込まれた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Izibongo",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "オリキ",
    "name_en": "oríkì",
    "name_original": "oríkì",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "ヨルバ族の本質称揚詩。個人・家系・町・神（オリシャ）・動植物の本質を凝縮した称揚句の連鎖からなる。誕生時に与えられる個人オリキから、共同体全員が共有する家系オリキまで多層を持ち、人格・帰属・歴史を一体化する詩学的装置として機能する。カリン・バーバー等が学術研究を進めた。",
    "background": "ヨルバ社会の自己同定・系譜記憶の根本装置である。",
    "development": "現代ヨルバ語文学・宗教詩・ナイジェリア英語小説の重要参照源として持続している。",
    "historical_context": "サンテリア・カンドンブレ等ディアスポラ宗教にも継承される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Oriki",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "epithet poetics",
         "description": "本質称揚句・エピセットの詩学比較事例。"},
    ],
})


# ===============================================================
# B. 主要主題・世界観 (8)
# ===============================================================

add({
    "name_ja": "ウブントゥ",
    "name_en": "ubuntu",
    "name_original": "ubuntu",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "ンゴニ語族・バントゥ語族（ズールー・コーサ等）の語で、「人は他の人々を通じて人となる」という関係的人間観を意味する。「Umuntu ngumuntu ngabantu」（人は人々によって人なり）という箴言で表現される。デズモンド・トゥトゥが真実和解委員会の哲学的基盤として提示し、世界的に注目される共同体倫理。",
    "background": "南部アフリカ・バントゥ語族圏の哲学的土壌である。",
    "development": "ジョン・ンビティ、ムリンジ、ラムボール等のアフリカ哲学者が理論化した。",
    "historical_context": "アパルトヘイト後の和解と国民統合の倫理的基礎となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ubuntu_philosophy",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "個人主義的主体概念を解体し、関係性のなかでの存在として人間を再定義する。AI agent論・分散主体性議論と構造的に共鳴する。",
         "related_ai_phenomenon": "AI agent moral status / 関係的存在論"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Ubuntu philosophy",
         "description": "アフリカ哲学の中核概念として直結。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "personhood / dividual self",
         "description": "人類学の人格・関係的個人研究と接続。"},
    ],
})

add({
    "name_ja": "ネグリチュード",
    "name_en": "négritude",
    "name_original": "négritude",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "1930年代のパリでセネガル人サンゴール、マルティニック人セゼール、仏領ギアナ人ダマスらが共同で提示した黒人文化的覚醒運動・概念。植民地的同化主義に対抗し、黒人としてあること（黒さ negritude）を肯定的に取り戻すフランス語圏黒人文学・思想運動。1934年の雑誌『L'Étudiant noir』で初出。",
    "background": "1930年代パリの黒人留学生コミュニティで形成された。",
    "development": "Présence Africaine誌（1947）と1956年・1959年の黒人作家芸術家会議で制度化された。",
    "historical_context": "カリブ海・アフリカ大陸両方の独立運動と思想的に連動した。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine archive",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "植民地的同化により内面化された主体性を、文化的・人種的にラディカルに再定義する運動。",
         "related_ai_phenomenon": "AIにおけるバイアス・主体性議論"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "支配者の言語フランス語を奪用しつつ、リズム・声・身体性を導入することで脱植民地化する戦略。",
         "related_ai_phenomenon": "支配的言語モデルの脱植民地化"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Africana philosophy / pan-Africanism",
         "description": "アフリカーナ哲学・汎アフリカ主義との中核的接続。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Black diaspora identity",
         "description": "黒人ディアスポラ・人種人類学との接続。"},
    ],
})

add({
    "name_ja": "アフリカン・パーソナリティ",
    "name_en": "African personality",
    "name_original": "African personality",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "19世紀末エドワード・ブライデン（リベリア）が提唱し、ガーナ初代大統領クワメ・エンクルマが汎アフリカ主義の基軸概念として再活性化した思想。アフリカ人固有の精神・倫理・社会性を肯定し、植民地的劣等視を反転する自尊宣言。ネグリチュードと並走する英語圏アフリカ思想潮流。",
    "background": "ブライデン『キリスト教・イスラム・黒人種』（1887）等で原型が示された。",
    "development": "エンクルマ『コンシエンシズム』（1964）で汎アフリカ哲学体系として理論化された。",
    "historical_context": "独立期のガーナの国家思想として機能した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/African_Personality",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "民族哲学",
    "name_en": "ethnophilosophy",
    "name_original": "ethnophilosophie",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ベルギー人宣教師プラシード・タンペルス『バントゥ哲学』（1945）に始まり、アフリカ社会の集団的世界観を「哲学」として記述する潮流。ジョン・ンビティ『アフリカの宗教と哲学』（1969）等が代表例。一方、パウラン・ホーンタンジ『アフリカ哲学：神話と現実』（1976）は集合的・無時間的記述として批判した。",
    "background": "タンペルスのバントゥ存在論記述が起点となった。",
    "development": "ホーンタンジ・カーゴジ等の批判を経てアフリカ哲学のメタ議論となっている。",
    "historical_context": "アフリカ哲学のアイデンティティ論争の中心軸を形成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/African_philosophy",
    "primary_source_type": "Wikipedia / Hountondji 1976",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "African philosophy debates",
         "description": "アフリカ哲学のメタ議論として直結。"},
    ],
})

add({
    "name_ja": "祖先記憶",
    "name_en": "ancestral memory",
    "name_original": "ancestral memory",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "サハラ以南アフリカ社会において、生者と死者を連続体として捉え、祖先（ancestors / amadlozi / aza­ka）が現世の生者を指導・監視・庇護するとする世界観。文学的にはチヌア・アチェベ『神の矢』、ベン・オクリ『満たされぬ道』などで主題化される。共同体記憶の時間構造を規定する基底概念。",
    "background": "西アフリカ・東アフリカ・南部アフリカ各地に共通の宗教・倫理基盤。",
    "development": "現代アフリカ小説の重要モチーフとして、写実主義と霊的世界観を融合する。",
    "historical_context": "植民地化・キリスト教化のなかでも持続した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Veneration_of_the_dead",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ancestor veneration",
         "description": "人類学の祖先崇拝研究と直結。"},
    ],
})

add({
    "name_ja": "物語のなかのトーテミズム",
    "name_en": "totemism in narrative",
    "name_original": "totemism in narrative",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "アフリカ口承伝統期",
    "definition": "氏族・家系を特定の動植物（トーテム）と結びつけるアフリカ諸社会の信仰体系の、物語的表現。氏族の起源譚、トーテム動物との婚姻譚、禁忌譚等が口承文学の重要主題を形成する。ジョージ・グリン・ジョーンズ等が南部アフリカの事例を研究、レヴィ＝ストロース『今日のトーテミズム』が比較人類学的に整理した。",
    "background": "フレーザー・モースなどの古典人類学が記述してきた現象。",
    "development": "アチェベ、ンゴーギ等の現代作家の小説的世界観の基底層を成す。",
    "historical_context": "氏族同定・婚姻規制・倫理規範の物語的根拠となる。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Totem",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "totemism / Lévi-Strauss",
         "description": "人類学のトーテミズム研究と直結。"},
    ],
})

add({
    "name_ja": "共同体的自己と個人的自己",
    "name_en": "communal vs individual self",
    "name_original": "communal vs individual self",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アフリカ思想・文学が西洋近代的個人主義と対比的に提示する自己観。ウブントゥや拡張的親族体系が示すように、「個」は共同体・祖先・未来世代を含む関係網のなかで成立する。アチェベ、エメチェタ等の小説における主人公構築と、デカルト的個人主義の対比として批評の中心テーマとなる。",
    "background": "ンビティ、ムビリ、サンゴール等が哲学的に言語化した。",
    "development": "現代アフリカ文学批評と人格論争の根本軸として持続する。",
    "historical_context": "個人主義／共同体主義の二項対立の問い直しに貢献する。",
    "primary_source_url": "https://www.ajol.info/index.php/sajpem",
    "primary_source_type": "AJOL — South African Journal of Philosophy",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "西洋的個人主義・自律的主体観への根本的代替案を提供する。AI agent・分散主体性議論と直結。",
         "related_ai_phenomenon": "分散的AI主体性 / 関係的人格"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "personhood debates",
         "description": "アフリカ哲学の人格論と接続。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "dividual / personhood",
         "description": "人類学の関係的人格研究（マリリン・ストラザーン等）と接続。"},
    ],
})

add({
    "name_ja": "口承＝書記の分割",
    "name_en": "oral-literate divide",
    "name_original": "oral-literate divide",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ジャック・グーディ、ウォルター・オングらが理論化した、口承文化と書記文化の認識論的・社会組織的差異の議論。アフリカ研究において、ルース・フィネガン『アフリカの口承文学』（1970）はこの二元論を批判し連続性を主張した。アフリカ文学・批評におけるテクスト概念の根本的問い直しの起点。",
    "background": "1970年代の口承研究勃興と並行して理論化された。",
    "development": "フィネガン、カリン・バーバー、リズ・ガンナー等が脱二項対立化を進めた。",
    "historical_context": "アフリカ書記文学の地位をめぐる根本論争となった。",
    "primary_source_url": "https://www.ajol.info/",
    "primary_source_type": "AJOL — Research in African Literatures",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "声と文字の二元論を解体する議論はAI時代の音声・テクスト境界の流動化と直結する。",
         "related_ai_phenomenon": "音声AI・マルチモーダル生成"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "口承の書記化は単純な転記でなく文化的翻訳実践である。",
         "related_ai_phenomenon": "音声テクスト変換と文化的損失"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Goody literacy thesis",
         "description": "グーディの識字仮説と直結。"},
    ],
})


# ===============================================================
# C. 植民地期文学 (8)
# ===============================================================

add({
    "name_ja": "ミッションスクール文学",
    "name_en": "mission school literature",
    "name_original": "mission school literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "19世紀末から20世紀前半にかけ、キリスト教ミッションスクールでヨーロッパ言語（英・仏・葡）と聖書翻訳を通じて教育を受けた最初期のアフリカ人作家層が産んだ文学。ソロモン・プラーチェ『ムフディ』、ヨゼフ・カゼコ等が代表。植民地教育の枠内で書きながらアフリカ的主題を導入する両義性を持つ。",
    "background": "ロベルト・モファット等の宣教師による聖書現地語翻訳が文字文化の起点となった。",
    "development": "ロブモ・モフォロ『チャカ』（1925）等の歴史小説に結実した。",
    "historical_context": "植民地教育と土着文化の最初の合流点を形成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/African_literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "仏語圏西アフリカ初期小説",
    "name_en": "francophone West African early novels",
    "name_original": "francophone West African early novels",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "1920-50年代の仏領西アフリカで成立した小説群。バカリ・ディアロ『力――善』（1926、塞内ガル人初の仏語小説）、ポール・アザン『黒人霊』、ウスマン・ソセ『カリム』（1935）、カマラ・ライエ『黒人少年』（1953）等が代表。植民地教育を受けた知識人層がフランス語を奪用しつつ、口承伝統・アフリカ的経験を表現する実験期。",
    "background": "ダカール・サンルイ等の仏領学校網が著者層を生み出した。",
    "development": "サンゴール・ネグリチュード運動と並走しつつ独自の小説形式を模索した。",
    "historical_context": "1947年のPrésence Africaine誌創刊と並行する文学的成熟期。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine archive",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "英語圏西アフリカ初期小説",
    "name_en": "anglophone West African early novels",
    "name_original": "anglophone West African early novels",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "1930-50年代の英領西アフリカで成立した小説群。エイモス・チュチュオラ『やし酒飲み』（1952）、シプリアン・エクウェンシ『ジャグア・ナナ』、チヌア・アチェベ『崩れゆく絆』（1958）が代表。口承伝承の英語的書き直し、植民地都市生活、伝統社会と植民地化の衝突を主題化し、現代アフリカ英語小説の基盤を形成した。",
    "background": "ナイジェリア・イバダン大学・アチモタ学校等の高等教育機関が著者層を育成した。",
    "development": "1958年のアチェベ『崩れゆく絆』がHeinemann African Writers Series（1962-）の起点となった。",
    "historical_context": "1957年ガーナ独立・1960年ナイジェリア独立と文学的高揚が連動した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Heinemann_African_Writers_Series",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
})

add({
    "name_ja": "オニチャ市場文学",
    "name_en": "Onitsha market literature",
    "name_original": "Onitsha market literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "1940-70年代にナイジェリア南東部オニチャ市の市場周辺で印刷・流通した、安価な小冊子（チャップブック）文学。恋愛指南・道徳説話・都市生活ガイド・大衆小説等を含み、植民地後期から独立直後のナイジェリアで広く読まれた。フィリップ・ニタブズ等の研究で文学的価値が再評価された。",
    "background": "ナイジェリア独立前後の都市化と識字率上昇が市場を産んだ。",
    "development": "1970年代の内戦（ビアフラ戦争）後に衰退した。",
    "historical_context": "アフリカ大衆文学・チャップブック文化の代表事例として研究される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Onitsha_Market_Literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "正典中心の文学観に対し、大衆的読者層・流通経路を中心に据えた事例。AI時代のロングテール出版と類比的に読み得る。",
         "related_ai_phenomenon": "AI生成大衆コンテンツ・分散出版"},
    ],
})

add({
    "name_ja": "南アフリカ初期黒人文学",
    "name_en": "South African early black writing",
    "name_original": "South African early black writing",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "1910-50年代の南アフリカ連邦下で書かれた黒人作家による文学。ソロモン・プラーチェ『ムフディ』（1930、英語による南アフリカ黒人初の小説）、サモン・モフォロ『チャカ』（1925、ソト語）、ピーター・エイブラハムズ『鉱山街』等が代表。アパルトヘイト体制（1948-）以前のセグリゲーション期の人種的経験を記録する。",
    "background": "セグリゲーション法体系下の都市・鉱山労働経験を主題とする。",
    "development": "アパルトヘイト下でドラム誌世代（エス・キア・ムパエ等）に継承された。",
    "historical_context": "南アフリカ近代文学の基層を形成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sol_Plaatje",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "葡語圏アフリカ初期文学",
    "name_en": "Lusophone African early literature",
    "name_original": "literatura africana de língua portuguesa",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "1940-60年代のアンゴラ・モザンビーク・カーボベルデ等葡領アフリカで形成された初期近代文学。アゴスティーニョ・ネト（後のアンゴラ初代大統領）の詩、ノエミア・デ・ソウザ、ジョゼ・クラヴェイリーニャ（モザンビーク）、コルセン（カーボベルデ）等が独立闘争と並行して書いた。MPLA・FRELIMO等の解放運動と文学が直結する点に特徴。",
    "background": "サラザール独裁下の長い植民地期末に文学覚醒が起こった。",
    "development": "1975年の独立革命で多くの作家が政府指導者となった（ネト等）。",
    "historical_context": "解放戦争（1961-75）と詩・小説が直接連動した稀有な事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Lusophone_African_literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ハウサ語カノ印刷文学",
    "name_en": "Hausa Kano press literature",
    "name_original": "littattafan soyayya / Kano market",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "ナイジェリア北部カノを中心に20世紀前半から成立したハウサ語近代文学。植民地官僚ラップトンが主導した1933年のNorthern Nigerian Literature Bureauの賞によりアブバカル・イマム『マガナ・ジャリ・チェ（語ることの効用）』等が成立。1980年代以降は女性作家中心のロマンス文学（littattafan soyayya）へ発展した。",
    "background": "イスラム教ハウサ語圏の長いアジャミ（アラビア文字ハウサ語）文学伝統を背景に、ローマ字ボコ表記による近代文学が成立した。",
    "development": "現代では数千の小説が出版される活発な大衆文学市場となっている。",
    "historical_context": "アフリカ大陸最大の現地語近代小説市場のひとつ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Hausa_literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

add({
    "name_ja": "スワヒリ語初期近代文学",
    "name_en": "Kiswahili early modern literature",
    "name_original": "fasihi ya Kiswahili",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地期",
    "definition": "東アフリカ沿岸（タンザニア・ケニア・ザンジバル等）の長いスワヒリ語アジャミ文学伝統（『ウテンディ・ワ・タンブカ』等18世紀以降の叙事詩）を背景に、植民地期にローマ字表記で発展した近代文学。シャーバン・ロバート（1909-62）の詩・自伝・寓話、ムハンマド・キジュンビ等が植民地末期から独立期にかけ言語運動と連動した。",
    "background": "アラブ・スワヒリ文化のアジャミ古典詩学が基盤となる。",
    "development": "独立後タンザニアで国語ニェレレ政策と並行して国民文学に拡張した。",
    "historical_context": "ニェレレ大統領自らシェイクスピアをスワヒリ語に翻訳するなど国家プロジェクトと文学が直結した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Swahili_literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "アジャミ（アラビア文字）からローマ字への複層的書記システム移行を経験した言語の文学。AI時代の文字システム多元性に示唆を与える。",
         "related_ai_phenomenon": "多文字システムOCR・低リソース言語AI"},
    ],
})


# ===============================================================
# D. ネグリチュード・反植民地運動 (8)
# ===============================================================

add({
    "name_ja": "プレザンス・アフリケーヌ",
    "name_en": "Présence Africaine",
    "name_original": "Présence Africaine",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "1947年にセネガル人アリウン・ジョップがパリで創刊した文芸・批評誌、および出版社・書店。サルトル、サンゴール、セゼール、リシャール・ライト、エメ・セゼールらが寄稿。1956年と1959年の黒人作家芸術家会議をパリ・ローマで主催し、ネグリチュード・汎アフリカ主義の制度的中心となった。",
    "background": "戦後パリの脱植民地的知識空間で形成された。",
    "development": "現在も書店・出版社として活動を継続している。",
    "historical_context": "アフリカディアスポラ知識ネットワークの中核となった。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "ネグリチュード対タイガリチュード",
    "name_en": "négritude vs Tigritude",
    "name_original": "négritude vs Tigritude",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "1962年カンパラの英語圏アフリカ作家会議でナイジェリア人ウォーレ・ショインカが投じた批判：「虎は自らの虎性（tigritude）を宣言しない――虎は襲いかかる」。すなわち真の黒人性は宣言ではなく行為で示すべきだとし、サンゴール的ネグリチュードのレトリック性・本質主義を批判した。英語圏／仏語圏アフリカ文学の方法論的分岐点となった重要論争。",
    "background": "1962年マケレレ大学カンパラ会議が舞台となった。",
    "development": "ショインカ自身の劇作・小説の方法論として展開された。",
    "historical_context": "アフリカ文学の英仏分割と並行する美学的論争となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Wole_Soyinka",
    "primary_source_type": "Wikipedia / Soyinka biographical sources",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "反植民地詩",
    "name_en": "anti-colonial verse",
    "name_original": "anti-colonial verse",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "1940-60年代に植民地支配批判・独立運動高揚を主題とした詩の総称。フランツ・ファノン的暴力論を文学的に表現するダヴィッド・ジョップ「禿鷲」、アゴスティーニョ・ネト『神聖な希望』、デニス・ブルータス（南ア）等が代表。直接的政治詩・戦闘詩としての美学を確立した。",
    "background": "アルジェリア戦争・モーモー運動・MPLA等の解放闘争と並行して発展した。",
    "development": "アパルトヘイト期南アフリカ詩、ビアフラ戦争詩等に継承された。",
    "historical_context": "詩と政治運動が分かちがたく結びついた稀有な時代を象徴する。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine anthologies",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "セゼール『帰郷ノート』",
    "name_en": "Aimé Césaire 'Cahier d'un retour au pays natal'",
    "name_original": "Cahier d'un retour au pays natal",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "マルティニック詩人エメ・セゼールによる長編散文詩（1939初出、1947改訂）。ネグリチュード文学最大の達成とされ、「私のネグリチュードは大聖堂でも記念碑でもなく…」の有名な行句で植民地的疎外と帰郷の決意を歌う。シュルレアリスム的言語実験と政治的覚醒を統合し、20世紀世界詩の正典に組み込まれた作品。",
    "background": "1934年Étudiant noir誌でnégritude造語を初使用したセゼール自身の出発点。",
    "development": "アンドレ・ブルトンが「20世紀最大の記念碑」と評価した。",
    "historical_context": "戦時下執筆・戦後刊行の歴史的タイミングが作品の象徴性を高めた。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine 1956 edition",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "サンゴールのリズム",
    "name_en": "Senghor's rhythm",
    "name_original": "rythme nègre / rhythme",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "セネガル詩人・初代大統領レオポルド・セダール・サンゴールが理論化した、黒人美学の中核としてのリズム概念。詩学エッセイ「黒人アフリカ美学」（1956）等で、ヨーロッパ的「論理」に対する黒人的「感性」「リズム」「拍動」を肯定的に対置した。後に本質主義との批判を受けるが、20世紀アフリカ詩学の基礎概念として持続する。",
    "background": "サンゴール『影の歌』（1945）等の詩集の方法論的支柱となった。",
    "development": "ショインカらから本質主義批判を受けるが、現代音楽研究等で再評価が進む。",
    "historical_context": "セネガル国家形成と詩学が直結した稀有な事例である。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Léopold_Sédar_Senghor",
    "primary_source_type": "Wikipedia / Senghor essays",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "西洋的論理／アフリカ的感性の二項対立を本質化する一方、AIによる「論理」生成に対しリズム・身体性のオルタナティブを提示する。",
         "related_ai_phenomenon": "身体性なきAI生成への批判"},
    ],
})

add({
    "name_ja": "ダヴィッド・ジョップ",
    "name_en": "David Diop",
    "name_original": "David Diop",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "1927-1960。仏領セネガル系の詩人。33歳で航空機事故により早逝したが、唯一の詩集『ハンマーのもとで』（1956）でネグリチュードの戦闘的・反植民地的版を確立した。「禿鷲」「アフリカ」「行進する者たち」等の詩で、植民地暴力を直視しつつ抵抗を歌った。サンゴールよりも明示的な反植民地姿勢を取った世代。",
    "background": "若くしてフランス・カメルーン・セネガルを行き来した。",
    "development": "早逝にもかかわらず20世紀アフリカ詩のアンソロジー必出の詩人となった。",
    "historical_context": "アルジェリア戦争・脱植民地化期に書かれた詩の代表的事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/David_Diop",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ビラゴ・ジョップ『コント』",
    "name_en": "Birago Diop 'Contes'",
    "name_original": "Les Contes d'Amadou Koumba",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "セネガル人作家・獣医ビラゴ・ジョップ（1906-89）によるウォロフ語民話の仏語再話集（1947, 1958, 1963）。グリオ・アマドゥ・クンバから聞いた物語を仏語で書き直し、口承の語り口を文字テクストに移植した先駆的実践。「死者は死なず…」（『生のあいだに』）の詩は世界アフリカ詩アンソロジーの定番。",
    "background": "口承継承者から直接聞き書きした素材を文学化した。",
    "development": "アフリカ口承文学のヨーロッパ言語化のモデルとなった。",
    "historical_context": "Présence Africaineから刊行され制度的にネグリチュード文学に組み込まれた。",
    "primary_source_url": "https://www.presenceafricaine.com/",
    "primary_source_type": "Présence Africaine",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "口承から文字へ・ウォロフ語から仏語への二重翻訳が新たな文学的形式を生む。AI翻訳の文化的創造性議論に直結。",
         "related_ai_phenomenon": "機械翻訳と概念創発"},
    ],
})

add({
    "name_ja": "カマラ・ライエ『黒人少年』",
    "name_en": "Camara Laye 'L'Enfant noir'",
    "name_original": "L'Enfant noir",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "ネグリチュード・反植民地期",
    "definition": "ギニア人作家カマラ・ライエ（1928-1980）の自伝的小説（1953）。ギニア・クールサ村の伝統的鍛冶師の息子として育ち、コナクリ・パリへ留学する若者の自伝として、伝統社会の精神性と都市・植民地教育の世界を架橋する。詩的散文と祖母・父の魔術的存在の描写が高く評価された一方、政治色の薄さがモンゴ・ベティらから批判された。",
    "background": "パリ留学中に書かれた、植民地的疎外を扱う代表作。",
    "development": "アフリカ自伝小説の正典として継続して読まれている。",
    "historical_context": "ネグリチュード文学のうち、政治的でなく内省的・詩的な側面を体現した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Camara_Laye",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})


# ===============================================================
# E. 主要批評概念 (8)
# ===============================================================

add({
    "name_ja": "口承ジャンル分類",
    "name_en": "oral genres taxonomy",
    "name_original": "oral genres taxonomy",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アフリカ口承伝統の体系的分類学。ルース・フィネガン『アフリカの口承文学』（1970）はパフォーマンス・ジャンル論を確立し、賛歌・叙事詩・系譜・諺・謎・民話・歌等を相互関係的に分析した。イゾゾミ・オクペウォ『アフリカ口承文学』（1992）等が分類を更新した。アフリカ文学批評の基礎枠組み。",
    "background": "1960-70年代の英米口承文学研究の成熟と並行して発展した。",
    "development": "現代パフォーマンス研究・民族詩学に継承されている。",
    "historical_context": "西洋的「文学」概念の枠を口承表現で拡張する効果をもたらした。",
    "primary_source_url": "https://www.ajol.info/index.php/jhsa",
    "primary_source_type": "AJOL — Journal of the Historical Society",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "genre theory",
         "description": "詩学のジャンル理論との接続。"},
    ],
})

add({
    "name_ja": "文学におけるピジン化",
    "name_en": "pidginization in literature",
    "name_original": "pidginization in literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ナイジェリア・ピジン英語、カメルーン・ピジン、シエラレオネ・クリオ等のピジン・クレオール言語を文学言語として使用する実践。エイモス・チュチュオラ『やし酒飲み』（1952）の「若き英語」、ケン・サロ＝ウィワ『ソザボーイ』（1985）等が代表。植民地英語の純化規範に対するラディカルな脱中心化を担う。",
    "background": "ナイジェリア港湾都市の労働者言語が文学化された。",
    "development": "現代ナイジェリア英語小説（チママンダ・アディーチェ等）の重要構成要素となる。",
    "historical_context": "規範英語と土着英語のあいだの政治的緊張を可視化した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nigerian_Pidgin",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "規範言語の権威を解体し、混淆言語を正統な文学言語に格上げする実践。AIの言語規範形成バイアスへの対抗的事例。",
         "related_ai_phenomenon": "LLMの低リソース言語・混淆言語処理"},
    ],
})

add({
    "name_ja": "言語選択論争",
    "name_en": "language choice debate",
    "name_original": "language choice debate",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アフリカ作家が植民地言語（英・仏・葡）と土着言語のいずれで書くかを巡る根本論争。チヌア・アチェベ「アフリカ作家と英語」（1965）は英語の創造的奪用を擁護し、ンギュギ・ワ・ジオンゴ『精神の脱植民地化』（1986）はギクユ語復帰を宣言した。1962年マケレレ会議以来、アフリカ文学の中心論争となっている。",
    "background": "1962年マケレレ大学カンパラの英語圏アフリカ作家会議が起点となった。",
    "development": "ンギュギの英語放棄宣言（1986）が論争を決定的に変えた。",
    "historical_context": "脱植民地化の文化的次元の象徴的論争として継続している。",
    "primary_source_url": "https://www.ajol.info/index.php/ral",
    "primary_source_type": "AJOL — Research in African Literatures",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "支配言語と土着言語の選択は単なる媒体選択でなく主体性の根本問題。AI時代の英語覇権・LLM言語バイアス論争と直結する。",
         "related_ai_phenomenon": "LLM多言語性・言語覇権"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "誰が読めるか・誰のために書くかを言語選択が規定する。",
         "related_ai_phenomenon": "AI翻訳の受容文脈再編"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "linguistic anthropology",
         "description": "言語人類学の植民地言語研究と直結。"},
    ],
})

add({
    "name_ja": "精神の脱植民地化",
    "name_en": "decolonizing the mind",
    "name_original": "Decolonising the Mind",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ケニア人作家ンギュギ・ワ・ジオンゴ（Ngũgĩ wa Thiong'o）の批評書（1986）の題および中核概念。アフリカ文学が植民地言語で書かれる限り精神的従属は続くと主張し、自身は英語からギクユ語への完全な移行を宣言した。母語優位論争・言語選択論争の決定的著作。「精神植民地化」という概念は世界の批評理論に多大な影響を与えた。",
    "background": "1977年の戯曲「私が結婚するときは私が望むときに」（ギクユ語）執筆と投獄経験が起点。",
    "development": "母語文学運動・先住民言語復興運動の理論的基礎となった。",
    "historical_context": "ポストコロニアル批評の必読古典として継続して参照されている。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Decolonising_the_Mind",
    "primary_source_type": "Wikipedia / Ngũgĩ 1986",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「精神の言語」という根本問題提起は、AI時代のLLM言語覇権・母語AIの倫理問題に決定的影響を与えうる。",
         "related_ai_phenomenon": "LLMの言語覇権・母語AI"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "誰が文学の読者でありうるかという根本問題を再定義する。",
         "related_ai_phenomenon": "AIの読者構成バイアス"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "decolonial philosophy",
         "description": "脱植民地哲学の文学的展開として直結。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "decolonial anthropology",
         "description": "脱植民地人類学と並走する理論的基盤。"},
    ],
})

add({
    "name_ja": "アフリカ文学美学",
    "name_en": "African literary aesthetics",
    "name_original": "African literary aesthetics",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アフリカ文学固有の美学理論を構築する批評潮流。チヌワ・ンウォガ『アフリカ文学の批評的伝統』、エメニュ『アフリカ文学美学に向けて』、アビオラ・イレレ『アフリカの想像力』（1990）等が、口承との連続性・共同体性・パフォーマンス性・倫理的目的性を中核要素として理論化した。",
    "background": "1960-80年代のアフリカ批評の自律的方法論探究と並行して発展した。",
    "development": "現代アフロポリタン批評・グローバル南文学批評にも継承されている。",
    "historical_context": "西欧批評輸入への対抗として自律的批評体系を構築する試みである。",
    "primary_source_url": "https://www.ajol.info/index.php/ral",
    "primary_source_type": "AJOL — Research in African Literatures",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ウジャマー文学",
    "name_en": "ujamaa literature",
    "name_original": "fasihi ya ujamaa",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "1967年タンザニア・ニェレレ大統領のアルーシャ宣言が打ち出したアフリカ社会主義（ujamaa, スワヒリ語で「家族・共同体」）の理念のもとに発展したスワヒリ語文学。エブラヒム・フセイン『キンジェケティレ』、シャアバン・ロバート後期作品、ペネナ・ムフムブシ等が国民文学の建設と社会主義的価値観を表現した。",
    "background": "ニェレレのアフリカ社会主義国家ビジョンと文学が直結した。",
    "development": "1980年代以降の自由化で内省的・個人主義的方向へ転換した。",
    "historical_context": "国家プロジェクトと文学の結合の代表事例である。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ujamaa",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

add({
    "name_ja": "対話的祖先形式",
    "name_en": "dialogic ancestral form",
    "name_original": "dialogic ancestral form",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アフリカ小説に特有とされる、生者と祖先・神々・非人間存在のあいだの絶え間ない対話を構造原理とする物語形式の批評概念。アチェベ『神の矢』、ベン・オクリ『満たされぬ道』、ベシー・ヘッド等の作品で、写実主義的時空の枠を超え祖先の声が現在に介入する語りが体系化された。バフチンの対話論をアフリカ的世界観に翻訳する批評的試み。",
    "background": "アビオラ・イレレ、エメニュ等が理論化した。",
    "development": "ポストコロニアル批評・魔術的写実主義論との対話で深化した。",
    "historical_context": "ラテンアメリカ魔術的写実主義との対比で議論される。",
    "primary_source_url": "https://www.ajol.info/index.php/ral",
    "primary_source_type": "AJOL — Research in African Literatures",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

add({
    "name_ja": "オラリテュール",
    "name_en": "oraliture",
    "name_original": "oraliture",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "マルティニック作家パトリック・シャモワゾーらが提唱した造語（oralité+littérature）。書記文学（littérature）と口承文化（oralité）の二元論を解体し、両者を融合した第三の文学的範疇を指す。シャモワゾー『クレオール礼賛』（1989）等で理論化され、カリブ海・アフリカのクレオール文学批評に拡張された。",
    "background": "クレオリテ運動の中核概念として1989年に提示された。",
    "development": "アフリカ文学批評（ンガル等）にも応用された。",
    "historical_context": "アフリカ＝カリブ海文学の方法論的橋渡しとなった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Créolité",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "口承と書記の二元論そのものを解体する造語的試み。AI時代の音声・テクスト境界の流動化と構造的に共鳴する。",
         "related_ai_phenomenon": "音声・テクスト統合AI"},
    ],
})


# ---------------------------------------------------------------
# Insertion driver
# ---------------------------------------------------------------

def main() -> int:
    print(f"[c23] {len(CONCEPTS)} concepts queued for insertion")
    inserted = 0
    skipped = 0
    failed = 0
    fourth_count = 0
    cross_count = 0

    with LitDB() as db:
        # seed periods
        period_ids: dict[str, int] = {}
        for name_ja, name_en, start, end, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=name_ja, region=REGION,
                start_year=start, end_year=end,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"[period] {name_ja} -> id={pid}")

        for entry in CONCEPTS:
            try:
                fourth_axes = entry.pop("fourth_axes", [])
                cross_domain = entry.pop("cross_domain", [])
                period_key = entry.pop("period_key", None)
                if period_key:
                    entry["period_id"] = period_ids[period_key]

                cid = db.insert_concept(**entry)
                if cid is None:
                    failed += 1
                    continue

                inserted += 1

                for axis in fourth_axes:
                    try:
                        db.tag_fourth_transform(cid, **axis)
                        fourth_count += 1
                    except LitDBError as e:
                        print(f"[warn] axis fail for {entry['name_ja']}: {e}")

                for cd in cross_domain:
                    try:
                        db.insert_cross_domain(
                            lit_entity_type="concept",
                            lit_entity_id=cid,
                            **cd,
                        )
                        cross_count += 1
                    except LitDBError as e:
                        print(f"[warn] cross fail for {entry['name_ja']}: {e}")

            except LitDBError as e:
                print(f"[error] {entry.get('name_ja','?')}: {e}")
                failed += 1
            except Exception as e:
                print(f"[fatal] {entry.get('name_ja','?')}: {e}")
                failed += 1

        # summary
        summary = db.progress_summary()
        print("\n[summary] table counts:")
        for k, v in summary.items():
            print(f"  {k}: {v}")

    print(f"\n[c23] inserted={inserted} skipped={skipped} failed={failed}")
    print(f"[c23] fourth_transform_tags={fourth_count} cross_domain={cross_count}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
