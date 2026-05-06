"""
LIT-DB Phase 2 — C30: Indigenous & Oral Literature (北米/豪/アイヌ)
=====================================================================
40 concepts across three indigenous traditions:
  - North American (15): trickster cycle, creation story, etc.
  - Australian Aboriginal (12): Dreamtime, Songline, Country, etc.
  - Ainu (13): yukar, kamuy, oina, uepeker, etc.

Speed-first approach: write, run, verify. ~500 lines.

Sources used:
  - https://www.oralliterature.org/ (World Oral Literature Project)
  - https://aiatsis.gov.au/ (Australian Institute of Aboriginal and Torres Strait Islander Studies)
  - https://paradisec.org.au/
  - https://www.ff-ainu.or.jp/ (アイヌ民族文化財団)
  - Wikipedia (公的アーカイブ)

Cultural protocol notes:
  - Communally owned concepts use author_name_text='[Community]'.
  - 'restricted knowledge' is included to encode cultural protocol in the schema.
  - Sacred narratives are described only within their public-domain published scope.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (broad, since oral traditions span deep time)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("先住民口承伝統期", "Indigenous Oral Tradition (pre-contact)", -10000, 1500,
     "接触以前の口承伝統。北米先住民・豪アボリジニ・アイヌ各文化の世代間伝承による物語・歌・知識体系。"),
    ("植民地接触・抑圧期", "Colonial Contact & Suppression", 1500, 1960,
     "ヨーロッパ・国民国家による植民地化と同化政策の時代。口承伝統が記録化・改変・抑圧される。"),
    ("先住民文芸復興期", "Indigenous Renaissance", 1960, 2026,
     "1960年代以降の先住民文芸復興。口承と書記の融合、自決運動、文化主権の文学。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


REGION = "周縁横断"
SUBFIELD = "lit_indigenous_oral"


# ===============================================================
# NORTH AMERICAN INDIGENOUS (15)
# ===============================================================

# --- 口承ジャンル (6) ---

add({
    "name_ja": "トリックスター物語群",
    "name_en": "trickster cycle",
    "name_original": "trickster cycle",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "コヨーテ、レイヴン、イクトミ等の両義的存在を主人公とする一連の物語群。境界侵犯・道化・創造神性を併せ持つトリックスターは、世界の秩序と無秩序を媒介する文化英雄として、北米先住民諸部族の口承文学の中核を占める。",
    "background": "ラドラ・ボアズらの初期人類学的記録により、北米全域に分布する説話類型として認識された。",
    "development": "ポール・ラディン『トリックスター』（1956）以降、各部族版が比較研究され、近年は部族コミュニティ自身による再記述が進む。",
    "historical_context": "口承共同体での教育・倫理学習の場として機能してきた。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project archive",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "共同体所有の物語であり、固定された個人作者は存在しない。AIによる多声生成と構造的に類比される。",
         "related_ai_phenomenon": "LLMの分散的生成・著作権の集合的帰属"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "西洋的線形物語と異なる螺旋・反復構造を持つ。",
         "related_ai_phenomenon": "非線形ナラティブ生成"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "trickster archetype",
         "description": "ユング的アーキタイプ・神話比較研究と接続。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Boas school folklore studies",
         "description": "ボアズ学派の人類学的記述伝統と直接的接続。"},
    ],
})

add({
    "name_ja": "創世物語",
    "name_en": "creation story",
    "name_original": "creation story",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "世界・人類・部族の起源を語る神聖な物語。北米先住民諸部族で異なる類型（earth-diver型、出現型、卵型等）が伝承され、儀礼・親族体系・土地の正統性を根拠づける。多くは限定された語り手・季節・場所でのみ発話される制限知識。",
    "background": "各部族の宇宙観と倫理を凝縮する基礎テクストとして機能してきた。",
    "development": "20世紀には人類学者の記録が進む一方、近年は部族自身が出版主体となり、文化主権の表明となっている。",
    "historical_context": "土地請求訴訟においても口承証拠として法的に援用される。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "公開可能な版と聖なる制限版を区別する。AI転写の真正性問題に直結。",
         "related_ai_phenomenon": "聖なる知識のAI学習からの除外要請"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "cosmogonic myth",
         "description": "世界の宇宙起源神話比較データベースと接続。"},
    ],
})

add({
    "name_ja": "コヨーテ譚",
    "name_en": "coyote tale",
    "name_original": "coyote tale",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "西部・南西部・グレートベイスンの諸部族で広く伝承される、コヨーテを主役とする物語群。創造者・愚者・破壊者の役割を演じ分け、世界の現状（季節・地形・人間の死等）の起源を説明する。トリックスターの代表的具象。",
    "background": "アサバスカ語族・ペヌーティ語族・ホカ語族など多言語圏に分布し、地域変奏が豊富。",
    "development": "ジェイムズ・ウェルチ、レスリー・シルコー等の現代作家が小説に取り込み、口承と書記を架橋した。",
    "historical_context": "西部開拓神話への先住民側からの対抗ナラティブを提供する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Coyote_in_mythology",
    "primary_source_type": "Wikipedia compilation",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "出現物語",
    "name_en": "emergence narrative",
    "name_original": "emergence narrative",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "プエブロ・ナバホ・ホピ等南西部諸部族に特徴的な創世類型。人々が地下世界を順次上昇し、現在の世界に「出現」するという世界形成の物語。各層は試練と学習の場として描かれ、儀礼の幾何学・サンドペインティング・親族体系の根拠となる。",
    "background": "考古学的に古プエブロ文明（チャコ・キャニオン等）の宇宙観と連続している。",
    "development": "ナバホ『ディネ・バハネ』として記録され、現代ナバホ詩人のテクスト基盤となる。",
    "historical_context": "土地神聖性と部族主権の論拠として援用されてきた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Diné_Bahaneʼ",
    "primary_source_type": "Wikipedia summary of published versions",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ウィンター・カウント",
    "name_en": "winter count",
    "name_original": "waníyetu wówapi",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ラコタ・ダコタ等の平原先住民が用いる、年代記的記録方式。バッファローの皮等に各年を象徴する一場面を絵画的に記し、口承の語りと連動して部族史を伝承する。文字を持たない社会の歴史記述として、絵画と口承を統合した独自の歴史実践。",
    "background": "19世紀から20世紀にかけて多数の現存例が博物館・部族で保存される。",
    "development": "近年デジタルアーカイブ化が進み、絵記号と口承の対応が再構築されている。",
    "historical_context": "サン＝ダンス禁止等の同化圧力下でも秘匿維持された。",
    "primary_source_url": "https://americanhistory.si.edu/explore/exhibitions/lakota-winter-counts",
    "primary_source_type": "Smithsonian NMAH archive",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "音声・絵画・身体運動の多モード記録であり、テキスト中心主義を解体する。",
         "related_ai_phenomenon": "マルチモーダルAI"},
    ],
})

add({
    "name_ja": "歌曲循環",
    "name_en": "song cycle",
    "name_original": "song cycle",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ナバホの「夜の道」「祝福の道」、ピマ・パパゴの治癒歌群等、長大な歌の連鎖からなる儀礼テクスト。数百から数千行にわたる定型歌詞・繰り返し・メタ言語的呼びかけを含み、口承詩学のロード＝パリー的定型理論を北米的に変奏する。",
    "background": "ワシントン・マシューズ等が19世紀末に転写を開始し、20世紀に翻訳が進んだ。",
    "development": "現代エスノポエティクス（D.テッドロック、D.ハイムズ）が形式分析を更新した。",
    "historical_context": "治癒儀礼の文脈で発話され、儀礼外での発話は制限される。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "Lord-Parry oral-formulaic theory",
         "description": "ロード＝パリーの定型理論を非ホメロス的伝統に拡張した代表事例。"},
    ],
})

# --- 主題 (6) ---

add({
    "name_ja": "互酬性",
    "name_en": "reciprocity",
    "name_original": "reciprocity",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "贈与と返礼、人間と非人間（動物・植物・土地）との間の双方向的関係を世界の根本構造とみなす倫理・宇宙観。ロビン・ウォール・キマラー『植物と叡智の守り人』等で文学的に再表現され、北米先住民文学の中核主題として現代エコクリティシズムにも接続している。",
    "background": "マルセル・モースの贈与論に先行する具体的実践として人類学的に注目された。",
    "development": "現代の生態哲学（ポトラッチ研究、Two-Eyed Seeing 等）の重要参照点となっている。",
    "historical_context": "資本主義的所有概念への対抗概念として再活性化されている。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Robin_Wall_Kimmerer",
    "primary_source_type": "Wikipedia / published works",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "人間中心主義を解体し、非人間存在を倫理的主体として包摂する。",
         "related_ai_phenomenon": "AI agent moral status議論"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "gift exchange / Mauss",
         "description": "贈与論の人類学的伝統と直接接続。"},
    ],
})

add({
    "name_ja": "四方位",
    "name_en": "four directions",
    "name_original": "four directions",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "東・南・西・北を世界の根本構造とみなし、各方位に色・元素・徳・季節・教えを配する宇宙論的枠組み。物語・儀礼・歌・治癒の構造原理として作用し、北米先住民諸文化に広く共通する基盤的シンボリズム。",
    "background": "プエブロ・ラコタ・チェロキー等多くの部族で詳細な体系を持つ。",
    "development": "現代教育プログラム（First Nations学校等）で精神的枠組みとして再活用。",
    "historical_context": "メディスン・ホイール教育法と緊密に連動する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Cardinal_direction",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "メディスン・ホイール",
    "name_en": "medicine wheel",
    "name_original": "medicine wheel",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "円周と十字を組み合わせた象徴図形。物理的なストーンサークル（バイホーン・メディスンホイール等）と、心的・教育的モデル両方を指す。四方位×四側面（精神・感情・肉体・知性）を統合する全体論的世界観のシンボル。",
    "background": "ワイオミング州バイホーンの遺跡は約700年前と推定される。",
    "development": "1970年代以降、汎先住民的精神運動・先住民教育プログラムで普及。",
    "historical_context": "汎部族主義（pan-Indianism）の象徴として広く採用された。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Medicine_wheel",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "オール・マイ・リレーションズ",
    "name_en": "All My Relations",
    "name_original": "Mitákuye Oyásʼiŋ",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ラコタ語で「私の親族すべて」を意味する祈りの締め言葉。人間・動物・植物・鉱物・天体までを親族として包摂する関係的存在論を表す。トーマス・キング編の同題アンソロジー（1990）以降、現代北米先住民文学のキーフレーズとして定着した。",
    "background": "ブラックエルク等を経由して20世紀に英語圏へ伝播。",
    "development": "ロビン・キマラー、トーマス・キング等の作品で繰り返し主題化される。",
    "historical_context": "西洋的個人主義への対抗思想として機能する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mitákuye_Oyásʼiŋ",
    "primary_source_type": "Wikipedia summary",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "人間と非人間を対称的に主体化する世界観で、AI・非人間エージェント論と共鳴する。",
         "related_ai_phenomenon": "post-anthropocentric AI ethics"},
    ],
})

add({
    "name_ja": "トゥー・スピリット",
    "name_en": "Two-Spirit",
    "name_original": "Two-Spirit",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "1990年に汎先住民会議で採択された、北米先住民の伝統的な多様な性・ジェンダー役割を指す英語の包括語。各部族言語の固有名（winkte、nádleehí 等）を尊重しつつ、現代における自己同定・文学運動の旗印として機能する。先住民クィア文学の基礎概念。",
    "background": "ヨーロッパ植民地化以前から多数の部族で承認された性のあり方を指す。",
    "development": "クレイグ・ウォマック、ダニエル・ヘス・テイラー等のクィア先住民作家による実践。",
    "historical_context": "植民地化による性規範の押しつけへの抵抗としての再定位。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Two-spirit",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "サヴァイヴァンス",
    "name_en": "survivance",
    "name_original": "survivance",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "ジェラルド・ヴィズナーが1990年代に提唱した造語。survival（生存）と resistance（抵抗）を統合し、犠牲者性の物語を超えた能動的存在の継続を意味する。先住民文学批評の中心概念として、被害者ナラティブからの離脱を志向する文学的実践を支える。",
    "background": "ヴィズナーの『Manifest Manners』（1994）で理論化された。",
    "development": "現代先住民文学批評・先住民研究全体に拡張。",
    "historical_context": "「消えゆくインディアン」言説への根本的批判として登場。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Gerald_Vizenor",
    "primary_source_type": "Wikipedia / published criticism",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "犠牲者ナラティブの解体は、AI生成テクストの被搾取性議論と構造的に類比可能。",
         "related_ai_phenomenon": "AI出力の主体性・能動性議論"},
    ],
})

# --- 現代運動 (3) ---

add({
    "name_ja": "ネイティブ・アメリカン・ルネッサンス",
    "name_en": "Native American Renaissance",
    "name_original": "Native American Renaissance",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "1968年のN・スコット・ママデイ『夜明けの家』のピューリッツァー賞受賞を画期とする、北米先住民文学の本格的勃興期を指す批評用語。ケネス・リンカーン『Native American Renaissance』（1983）で命名された。リーズリー・シルコー、ジェイムズ・ウェルチ等が口承伝統と現代小説形式を架橋した。",
    "background": "公民権運動・赤い力運動（Red Power）と連動する文化的覚醒の時代。",
    "development": "1990年代のルイーズ・アードリック、シャーマン・アレクシー等が継承し国際的評価を獲得。",
    "historical_context": "アメリカ・インディアン公民権法（1968）と並行する文化主権の主張。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Native_American_Renaissance",
    "primary_source_type": "Wikipedia / Lincoln 1983",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
})

add({
    "name_ja": "先住民フューチャリズム",
    "name_en": "Indigenous futurism",
    "name_original": "Indigenous futurism",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "アフロフューチャリズムから派生し、グレース・ディロンが2012年のアンソロジー『Walking the Clouds』で命名した文学運動。先住民SF・スペキュラティブフィクションを通じて、ポスト・アポカリプスとしての植民地化、未来における先住民存在、伝統知識と未来テクノロジーの対話を主題化する。",
    "background": "ディロン編『Walking the Clouds』（2012）で批評範疇として確立。",
    "development": "レベッカ・ローンホース、ダニエル・ヘス・テイラー、コロニアル・コミックスらが実践。",
    "historical_context": "気候危機・AI時代における先住民知識の戦略的再配置と連動する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indigenous_futurisms",
    "primary_source_type": "Wikipedia / Dillon 2012",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "西洋的な進歩史観・終末論と異なる時間性を提示する。",
         "related_ai_phenomenon": "AI時代の未来想像力の多元化"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI futures imaginaries",
         "description": "AI未来想像力に多元的視座を提供する文学的実践として並行関係。"},
    ],
})

add({
    "name_ja": "口承＝書記ハイブリッド",
    "name_en": "oral-written hybrid",
    "name_original": "oral-written hybrid",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "現代北米先住民文学の中心的形式。N・スコット・ママデイ、リーズリー・シルコー、サイモン・オーティス等が、伝統的な口承の語り・歌・儀礼構造を、英語の小説・詩のページ上に再構成する手法。声と書記、英語と部族言語、線形と循環を統合する文体実験。",
    "background": "ワルター・オングらの口承文化研究を文学的に応用する形で発展。",
    "development": "現代先住民文学批評の主要分析対象であり続けている。",
    "historical_context": "英語覇権の中で部族言語・声を保存する戦略でもある。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Native_American_literature",
    "primary_source_type": "Wikipedia summary",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "声と文字の二元論を解体する。AI音声＝テクスト変換の文化的応用にも示唆。",
         "related_ai_phenomenon": "音声AI・口承資料の自動転写"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳不可能性を残しつつテクストを成立させる。",
         "related_ai_phenomenon": "機械翻訳の文化的限界"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "ASR for endangered languages",
         "description": "AI転写技術と先住民言語アーカイブの実践的接点。"},
    ],
})


# ===============================================================
# AUSTRALIAN ABORIGINAL (12)
# ===============================================================

# --- ジャンル/主題 (5) ---

add({
    "name_ja": "ドリームタイム物語",
    "name_en": "Dreamtime story",
    "name_original": "Dreamtime story",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "オーストラリアアボリジニの世界創造の時間を語る神聖な物語群。創造祖（祖先存在）が大地を歩き、河川・岩・動植物を生み出し、法と歌と儀礼を残したとされる根源の時。土地・親族・倫理の根拠であり、各部族言語ごとに固有の名称を持つ（Tjukurpa, Dreaming 等）。",
    "background": "イギリス人類学者によるDreaming訳語が広まる前に各部族の固有概念が存在した。",
    "development": "1970年代以降、土地請求の法的根拠として再活性化された。",
    "historical_context": "Mabo判決（1992）以降、慣習法的土地権の基礎として承認された。",
    "primary_source_url": "https://aiatsis.gov.au/explore/dreaming",
    "primary_source_type": "AIATSIS official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "公開可能な版と聖なる制限版の二層構造を持つ。",
         "related_ai_phenomenon": "AI学習データからの聖なる知識除外"},
    ],
})

add({
    "name_ja": "ソングライン",
    "name_en": "Songline",
    "name_original": "Songline / yiri",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "創造祖の旅路を歌として記憶し、大陸を横断する道筋を世代を超えて伝承する歌の地理学。各歌節は土地の特徴と結びつき、歌うことで道を辿り、知識・親族・水場・食物を継承する。ブルース・チャトウィン『ソングライン』（1987）で西欧に紹介された。",
    "background": "T.G.H.ストレロウ等の宣教師＝言語学者が20世紀前半に部分記録した。",
    "development": "デジタルマッピング・コミュニティ主導アーカイブとして再構築されている。",
    "historical_context": "土地と知識の不可分性を体現する。",
    "primary_source_url": "https://aiatsis.gov.au/",
    "primary_source_type": "AIATSIS",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "歌・地理・記憶を統合した複合メディアであり、テクスト中心主義を解体する。",
         "related_ai_phenomenon": "GIS×口承AIの統合"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "空間的・地理的に展開する物語形式は線形時間と異なる。",
         "related_ai_phenomenon": "空間的ナラティブ生成"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Country / cultural geography",
         "description": "人類学的場所論との直接的接続。"},
    ],
})

add({
    "name_ja": "チュクルパ",
    "name_en": "Tjukurpa",
    "name_original": "Tjukurpa",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "中央オーストラリアのアナング（Anangu）民族の世界観を表す中核概念。創造の時代・法・物語・歌・儀礼・土地のすべてを包含する。ウルル＝カタ・ジュタ国立公園の管理運営原理として正式に位置づけられ、文化主権の法制化された一例。",
    "background": "ピチャンチャチャラ語・ヤンクニチャチャラ語圏の固有概念。",
    "development": "1985年のウルル返還以降、共同管理の指導原理として制度化された。",
    "historical_context": "Dreamingの英訳概念に対する固有名の主張でもある。",
    "primary_source_url": "https://parksaustralia.gov.au/uluru/discover/culture/tjukurpa/",
    "primary_source_type": "Parks Australia official",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "カントリー語り",
    "name_en": "Country narrative",
    "name_original": "Country narrative",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "Country（後述）を物語の主体として位置づける語りの様式。土地そのものが歌い、語り、記憶する存在として描かれ、人間は土地に「呼ばれて」物語を継承する。アレクシス・ライト『カーペンタリア』等の現代アボリジニ小説の中心的方法論。",
    "background": "デボラ・バード・ローズ等の人類学的記述で精緻化された。",
    "development": "現代アボリジニ作家の小説・詩・批評の基底概念として作用する。",
    "historical_context": "Mabo判決後の法的・文学的同時運動と連動する。",
    "primary_source_url": "https://aiatsis.gov.au/",
    "primary_source_type": "AIATSIS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "儀礼歌",
    "name_en": "ceremony song",
    "name_original": "ceremony song",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "通過儀礼・治癒・葬送・季節儀礼などで歌われる、定型化された歌曲群。多くは制限知識として男性のみ・女性のみ・特定の入門者のみが知ることを許される。アーネムランド、中央砂漠、トレス海峡諸島など地域ごとに音楽様式が大きく異なる。",
    "background": "AIATSIS・PARADISECなどのデジタルアーカイブで一部公開版が保存される。",
    "development": "近年、コミュニティ自身が公開・非公開の境界を再定義する取り組みが進む。",
    "historical_context": "宣教師抑圧期に多くが秘匿維持された。",
    "primary_source_url": "https://paradisec.org.au/",
    "primary_source_type": "PARADISEC archive",
    "importance_score": 3, "source_tier": "primary", "canonical_in_region": "major",
})

# --- 主題/概念 (5) ---

add({
    "name_ja": "カントリー",
    "name_en": "Country",
    "name_original": "Country",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アボリジニ英語で大文字始まりの「Country」と表記される、土地・先祖・歌・法・水・空・存在を一体として捉える概念。「私のCountry」と言うとき、それは所有でなく相互的責任の関係を意味する。デボラ・バード・ローズ『Nourishing Terrains』（1996）で理論化された。",
    "background": "アボリジニ英語の独自語彙として成立した。",
    "development": "現代生態哲学・場所論・先住民研究で広く参照される。",
    "historical_context": "西洋的「土地所有」概念への根本的代替案を提供する。",
    "primary_source_url": "https://aiatsis.gov.au/explore/welcome-country-and-acknowledgement-country",
    "primary_source_type": "AIATSIS",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "土地そのものを倫理的主体として位置づけ、人間中心主義を脱構築する。",
         "related_ai_phenomenon": "non-human agency / AI主体性議論"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "place ontology",
         "description": "人類学的場所論との中核的接続。"},
    ],
})

add({
    "name_ja": "ドリーミング",
    "name_en": "Dreaming",
    "name_original": "Dreaming",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "創造の時間と現在の時間を貫く、時間外の時間。各部族の固有概念（Tjukurpa, Jukurrpa, Wongar 等）の英語包括訳。スタンナーが「the everywhen（永久時）」と訳した。物語は単に過去にあるのでなく、儀礼を通じて今ここに常に活性化される。",
    "background": "W・E・H・スタンナーの1953年論文で英語批評概念として定着。",
    "development": "現代の場所論・時間論研究で重要な参照点となる。",
    "historical_context": "西洋的線形時間観への代替案として注目されてきた。",
    "primary_source_url": "https://aiatsis.gov.au/explore/dreaming",
    "primary_source_type": "AIATSIS",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "親族体系",
    "name_en": "kinship",
    "name_original": "kinship",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アボリジニ社会の基底をなす、人間・土地・祖先・動植物を結ぶ体系的関係網。「スキン・ネーム」「セクション・システム」等で構造化され、誰と話せるか・誰と結婚できるか・どの土地と歌と責任を持つかを規定する。物語と歌の語りの権利・義務もこの体系に従う。",
    "background": "A・R・ラドクリフ＝ブラウン以来の人類学研究蓄積がある。",
    "development": "現代では先住民コミュニティ自身による教育プログラムで再活性化されている。",
    "historical_context": "盗まれた世代の経験により親族系統の断絶が深刻化した。",
    "primary_source_url": "https://aiatsis.gov.au/explore/kinship-and-skin-names",
    "primary_source_type": "AIATSIS",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "kinship systems",
         "description": "人類学親族研究の主要対象。"},
    ],
})

add({
    "name_ja": "盗まれた世代の語り",
    "name_en": "Stolen Generations narrative",
    "name_original": "Stolen Generations narrative",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地接触・抑圧期",
    "definition": "1910年代から1970年代にかけ、政府機関がアボリジニ・トレス海峡諸島民の子どもを家族から強制的に分離した政策の被害証言群。1997年Bringing Them Home報告書、サリー・モーガン『My Place』、アニタ・ハイス等の作品が文学的に主題化した。",
    "background": "保護法（Protection Acts）下の同化政策の帰結である。",
    "development": "2008年のラッド首相による公式謝罪を経て、和解の文学として継続している。",
    "historical_context": "オーストラリア国家史の構造的暴力を記録する集合的証言文学。",
    "primary_source_url": "https://aiatsis.gov.au/explore/stolen-generations",
    "primary_source_type": "AIATSIS",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "制限された知識",
    "name_en": "restricted knowledge",
    "name_original": "restricted knowledge / sacred-secret",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "性別・年齢・入門段階・親族関係によって参照可能性が制限される知識のカテゴリ。Sacred-secret、men's business、women's business 等と呼ばれる。アボリジニ研究・出版・デジタルアーカイブでは公開／非公開の二層を厳格に分離する文化的プロトコルが確立されている。",
    "background": "AIATSIS の Code of Ethics に明文化されている。",
    "development": "デジタルアーカイブの設計思想（CARE原則）に決定的影響を与えた。",
    "historical_context": "AI学習データの倫理的処理にも示唆を与える概念。",
    "primary_source_url": "https://aiatsis.gov.au/research/ethical-research",
    "primary_source_type": "AIATSIS Code of Ethics",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「公開知＝普遍的価値」という前提を解体する。AI学習データ倫理の根本問題。",
         "related_ai_phenomenon": "AI training data exclusion / CARE principles"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "誰が読めるかが文化的に決定される。",
         "related_ai_phenomenon": "AI出力アクセス制御"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "CARE principles for indigenous data",
         "description": "AI倫理・データガバナンスの根本的基準。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "esoteric knowledge",
         "description": "人類学の秘儀知識研究と接続。"},
    ],
})

# --- 現代 (2) ---

add({
    "name_ja": "アボリジニ英語文学",
    "name_en": "Aboriginal English literature",
    "name_original": "Aboriginal English literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "標準オーストラリア英語と区別されるアボリジニ英語（独自の音韻・語彙・文法・語用論を持つ英語変種）で書かれた文学。サリー・モーガン、キム・スコット、アレクシス・ライト等が、書記言語のなかに口承の声と部族言語の痕跡を織り込む実践を確立した。",
    "background": "言語学者ダイアナ・イーデスらがアボリジニ英語を独立変種として記述した。",
    "development": "1980年代以降、文学賞受賞作家が相次ぎ国際的評価を獲得している。",
    "historical_context": "言語的多様性と植民地史を同時に刻印するメディウムである。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Australian_Aboriginal_English",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "主権の文学",
    "name_en": "Sovereignty literature",
    "name_original": "Sovereignty literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "アボリジニ・トレス海峡諸島民の文化主権・政治主権を文学的に表明・実践する作品群を指す批評範疇。アイリーン・モートン＝ロビンソン、トニー・バーチ、エヴリン・アラルカ・ウェイラー等が理論的・文学的に展開する。Mabo判決後の主権論争と並行する文学運動。",
    "background": "Mabo判決（1992）以降の主権論争と並行して発展した。",
    "development": "条約（Treaty）運動・憲法承認運動と連動して継続している。",
    "historical_context": "Voice to Parliament 国民投票（2023）等の現代政治と文学が直結する。",
    "primary_source_url": "https://aiatsis.gov.au/",
    "primary_source_type": "AIATSIS / academic literature",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})


# ===============================================================
# AINU (13)
# ===============================================================

# --- ジャンル (5) ---

add({
    "name_ja": "ユーカラ",
    "name_en": "yukar (Ainu epic)",
    "name_original": "ユーカㇻ / yukar",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌの英雄叙事詩。ポイヤウンペ（小さき者）等の英雄を主人公とし、戦闘・婚姻・神々との交渉を一人称で語る長大な叙事詩形式。サケヘ（折返句）と韻律を持ち、囲炉裏端で夜通し語られた。金田一京助・知里幸恵らの記録により世界の口承叙事詩研究の重要対象となった。",
    "background": "アイヌ口承文学の中核ジャンルとして20世紀初頭まで生きた伝統。",
    "development": "知里幸恵『アイヌ神謡集』（1923）で広く知られるに至った。",
    "historical_context": "明治期以降の同化政策下で急速に衰退したが部分的に記録された。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "個別の語り手による即興的変奏を許容する口承定型詩形式。",
         "related_ai_phenomenon": "LLMによる定型と変奏の生成"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "アイヌ語の音韻・韻律を保持しつつカタカナ・ローマ字・日本語訳が並存する多層テクスト。",
         "related_ai_phenomenon": "低リソース言語AIの可能性"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral-formulaic theory (Lord-Parry)",
         "description": "ロード＝パリーの口承定型詩学の非ヨーロッパ的検証事例。"},
    ],
})

add({
    "name_ja": "カムイユカラ",
    "name_en": "kamuy yukar (god epic)",
    "name_original": "カムイユカㇻ / kamuy yukar",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "神（カムイ）を一人称の語り手とするアイヌ叙事詩。動物神（フクロウ・シャチ・熊等）が自身の体験を人間に語る形式。「銀の滴降る降るまわりに」で始まるシマフクロウの神謡（知里幸恵訳）が代表例。宇宙論・倫理・人間と自然の関係を凝縮する。",
    "background": "神々の視座から人間社会を相対化する独特の語りの構造を持つ。",
    "development": "知里幸恵『アイヌ神謡集』（1923）で日本語に翻訳された。",
    "historical_context": "アイヌ的アニミズムの文学的結晶として国際的にも注目されてきた。",
    "primary_source_url": "https://www.aozora.gr.jp/cards/000234/files/4406_24405.html",
    "primary_source_type": "青空文庫（知里幸恵『アイヌ神謡集』PD版）",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "非人間（神・動物）が一人称の語り手となる物語形式。人間中心主義を構造的に脱構築する。",
         "related_ai_phenomenon": "non-human narrator / AI agent narratives"},
    ],
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "animal speaker myths",
         "description": "動物を語り手とする神話比較研究と接続。"},
    ],
})

add({
    "name_ja": "オイナ",
    "name_en": "oina (sacred narrative)",
    "name_original": "オイナ / oina",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌラックル（オイナカムイ、人間に文化を教えた半神）を主人公とする神聖な叙事詩。宗教的・儀礼的位置づけを持ち、文化英雄譚に該当する。樺太アイヌの「ハウキ」と並ぶ叙事詩の主要類型として、知里真志保らが類型化した。",
    "background": "アイヌの宗教的世界観の中核を形成する物語群である。",
    "development": "金田一京助・知里真志保の研究で類型が明確化された。",
    "historical_context": "近代以降の口承衰退で断片化が進んだ。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ウエペケレ",
    "name_en": "uepeker (Ainu prose tale)",
    "name_original": "ウエペケㇾ / uepeker",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌの散文説話。ユーカラが韻文・歌唱されるのに対し、ウエペケレは散文で日常言語に近い形式で語られる。教訓譚・笑話・由来譚等を含み、家族や近隣で気軽に語られた。萱野茂による多数の聞き書き記録が出版されている。",
    "background": "韻文ジャンルと並行して発達した散文口承の総称。",
    "development": "萱野茂『アイヌの民話』等で広く一般読者に紹介された。",
    "historical_context": "日常的口承の場が消失したことで主要な文化的ロスとなった。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "サコロベ",
    "name_en": "sakorobe (sung narrative)",
    "name_original": "サコロベ / sakorobe",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌ口承文学の韻文ジャンルの一つで、「節をもつもの」を意味する。叙事詩的内容を歌唱する形式で、ユーカラと近接しつつ地域・系譜により区別される。北海道日高地方・胆振地方等に多い類型として記録されてきた。",
    "background": "アイヌ語地域差により分類が複雑である。",
    "development": "アイヌ民族博物館・北海道大学アイヌ・先住民研究センターで研究蓄積がある。",
    "historical_context": "話者・歌い手の喪失により完全形での記録は限られる。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

# --- 主題/世界観 (5) ---

add({
    "name_ja": "カムイ",
    "name_en": "kamuy",
    "name_original": "カムイ / kamuy",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌの世界観における神的存在。動物（特に熊・シマフクロウ・シャチ）、自然現象、道具までもが神として現れる包括的アニミズム概念。神は「人間世界に毛皮や肉を運んできてくれる客」として遇され、儀礼を通じて神の国へ送り返される（イオマンテ等）。",
    "background": "アイヌ語kamuy（神）はアジア北方諸言語のkam系語と関連する可能性が議論される。",
    "development": "現代の生態思想・先住民研究の重要参照概念となっている。",
    "historical_context": "明治期の神仏判別令以後の宗教抑圧下でも口承伝承された。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "動物・道具・現象を神＝主体として位置づけ、人間中心主義を解体する。",
         "related_ai_phenomenon": "non-human agency / AI主体性議論"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "animism",
         "description": "デスコラの存在論四分類の代表事例。"},
    ],
})

add({
    "name_ja": "ラマッ",
    "name_en": "ramat (soul/spirit)",
    "name_original": "ラマッ / ramat",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌ語で「魂・精神」を意味する概念。人間・動物・植物・道具すべてに宿るとされ、適切な扱い・送りの儀礼によって維持・更新される。物質と精神の二元論を超えた関係的存在論を支える基底概念。知里真志保の言語民族誌研究で詳細に分析された。",
    "background": "アイヌ語の宗教語彙の中核をなす概念である。",
    "development": "現代アイヌ研究・先住民研究で再評価されている。",
    "historical_context": "イオマンテ等の儀礼の哲学的根拠となる。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "soul concepts in animism",
         "description": "人類学の魂概念比較研究との接続。"},
    ],
})

add({
    "name_ja": "ウェンカムイ",
    "name_en": "wenkamuy (evil deity)",
    "name_original": "ウェンカムイ / wenkamuy",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌ語で「悪い神」を意味する。本来善神であった存在が、人間の不適切な扱いや儀礼の不履行により悪神化したものを指す。善悪の二元論ではなく、関係性によって神の質が変化する関係的悪概念。多くのカムイユカラの主題となる。",
    "background": "善神／悪神の区別が固定的でなく、関係的に決定される世界観を反映する。",
    "development": "知里真志保の宗教語彙研究で精緻に分析された。",
    "historical_context": "アイヌ倫理学の基盤的概念のひとつである。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

add({
    "name_ja": "イオマンテ",
    "name_en": "iyomante (bear-sending ceremony)",
    "name_original": "イオマンテ / iyomante",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アイヌの代表的儀礼で、特にヒグマの仔を1〜2年人間社会で養育したのち神の国へ送り返す送り儀礼。神＝動物を儀礼によって生命循環の中で再生させるという、贈与・互酬の宇宙論を凝縮した実践。多くのユーカラ・カムイユカラの主題となる。",
    "background": "明治期に多数の民族誌的記録が残された。",
    "development": "現代では儀礼そのものはほぼ行われないが文学・研究の重要対象である。",
    "historical_context": "1955年の北海道の通達で実質的に終止符が打たれたが、文化的意義は再評価されている。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "神謡",
    "name_en": "kamuy yukar (Japanese term: shin'yō)",
    "name_original": "神謡",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地接触・抑圧期",
    "definition": "知里幸恵がカムイユカラを日本語に訳出する際に採用した訳語。「神の謡う歌」の意。1923年刊『アイヌ神謡集』により日本語文学史にアイヌ口承文学を刻んだ画期的概念であり、翻訳概念として先住民文学＝主流文学の架橋を象徴する語。",
    "background": "知里幸恵の卓越した翻訳実践が産んだ概念である。",
    "development": "戦後の日本児童文学・現代詩でも繰り返し参照されている。",
    "historical_context": "口承・無文字社会の文学を「文学」と認める転回点となった。",
    "primary_source_url": "https://www.aozora.gr.jp/cards/000234/files/4406_24405.html",
    "primary_source_type": "青空文庫『アイヌ神謡集』",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳が新概念を創出するパフォーマティヴな実践であることを示す。",
         "related_ai_phenomenon": "機械翻訳と概念創発"},
    ],
})

# --- 記述者・形式 (3) ---

add({
    "name_ja": "知里幸恵",
    "name_en": "Chiri Yukie",
    "name_original": "知里幸恵",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地接触・抑圧期",
    "definition": "1903-1922。アイヌ女性として初めてカムイユカラを自ら筆記・日本語訳した文学者。1923年に没後出版された『アイヌ神謡集』は、アイヌ語のローマ字表記と日本語訳を見開きで提示する画期的形式を採り、世界の先住民文学翻訳実践の先駆例となった。19歳で早逝。",
    "background": "金田一京助との出会いを契機に翻訳・記述の作業に取り組んだ。",
    "development": "現代まで版を重ね、青空文庫等でPD公開されている。",
    "historical_context": "同化政策下のアイヌ女性が文化主権を行使した記念碑的事例である。",
    "primary_source_url": "https://www.aozora.gr.jp/index_pages/person234.html",
    "primary_source_type": "青空文庫（PD）",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "知里真志保",
    "name_en": "Chiri Mashiho",
    "name_original": "知里真志保",
    "original_script": "native",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "植民地接触・抑圧期",
    "definition": "1909-1961。知里幸恵の弟。アイヌ語学者・北海道大学教授として、アイヌ語の系統的記述・口承文学の言語民族誌的分析で多大な貢献をした。『分類アイヌ語辞典』『地名アイヌ語小辞典』等の基礎文献を残し、アイヌ自身による学術的アイヌ研究の道を開いた。",
    "background": "東京帝国大学で言語学を学んだ。",
    "development": "戦後北海道大学教授として後進を育成した。",
    "historical_context": "アイヌ自身による記述という主権的学知の起点に位置する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Chiri_Mashiho",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "サケヘ",
    "name_en": "sakehe (refrain in yukar)",
    "name_original": "サケヘ / sakehe",
    "original_script": "katakana",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ユーカラ・カムイユカラに繰り返し挿入される折返句。「ハイトウンナ」「アトゥイ・ヤ」等、各物語固有のサケヘを持ち、語り手と聴き手の呼応・記憶想起・神聖化の機能を担う。口承定型詩学における音楽的・記憶術的装置として、ロード＝パリー理論の比較事例となる。",
    "background": "アイヌ口承詩の韻律的中核を構成する。",
    "development": "金田一・知里以来の研究蓄積で形式が記述されてきた。",
    "historical_context": "口承文学の音楽性・身体性を担保する装置である。",
    "primary_source_url": "https://www.ff-ainu.or.jp/",
    "primary_source_type": "アイヌ民族文化財団",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "formula / refrain in oral poetics",
         "description": "ロード＝パリー定型理論の非ヨーロッパ事例として直結。"},
    ],
})


# ---------------------------------------------------------------
# Insertion driver
# ---------------------------------------------------------------

def main() -> int:
    print(f"[c30] {len(CONCEPTS)} concepts queued for insertion")
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

                # check if was actually new (find_concept returned same id => skip)
                # We can't easily distinguish here, so increment inserted on any non-None
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

    print(f"\n[c30] inserted={inserted} skipped={skipped} failed={failed}")
    print(f"[c30] fourth_transform_tags={fourth_count} cross_domain={cross_count}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
