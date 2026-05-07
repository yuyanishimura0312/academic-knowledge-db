"""
LIT-DB Phase 2 — C31: Indigenous & Oral Literature (Other Cultures)
=====================================================================
40 concepts across five categories outside C30 (北米/豪/アイヌ):
  - A: Maori / Polynesia / Pacific (8)
  - B: African oral (non-C23) (8)
  - C: Northern indigenous (Sami / Inuit / Yakut / Buryat / Mongol etc.) (8)
  - D: South American indigenous (8)
  - E: Cross-cutting concepts (8)

Speed-first: write, run, verify. ~700 lines.

Sources:
  - https://www.oralliterature.org/ (World Oral Literature Project)
  - https://paradisec.org.au/ (Pacific And Regional Archive)
  - https://www.elararchive.org/ (Endangered Languages Archive)
  - https://ich.unesco.org/ (UNESCO Intangible Cultural Heritage)
  - http://www.endangeredlanguages.com/ (UCLA endangered languages project)
  - Wikipedia public-domain summaries

Cultural protocol notes (same as C30):
  - Communally owned concepts use author_name_text='[Community]'.
  - Sacred/restricted narratives are described only within their public-domain published scope.
  - subfield_id=19, code='lit_indigenous_oral', region='周縁横断'.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (oral traditions span deep time)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("先住民口承伝統期", "Indigenous Oral Tradition (pre-contact)", -10000, 1500,
     "接触以前の口承伝統。世界の周縁諸文化の世代間伝承による物語・歌・儀礼・知識体系。"),
    ("植民地接触・抑圧期", "Colonial Contact & Suppression", 1500, 1960,
     "植民地化と国民国家形成下で口承伝統が記録化・改変・抑圧される時期。"),
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
# A. MAORI / POLYNESIA / PACIFIC (8)
# ===============================================================

add({
    "name_ja": "ファカパパ",
    "name_en": "whakapapa (genealogical recitation)",
    "name_original": "whakapapa",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "マオリ語で「層を重ねる」を意味し、人間・神・大地・動植物の系譜を一連の系統的詠唱として記憶・伝承する実践。創世神話から現代の語り手までを連結する系譜的アイデンティティの中核装置であり、口承による「生きた百科事典」として土地・身分・物語の権利を根拠づける。",
    "background": "マオリ社会の基本構造原理であり、議論・スピーチ・儀礼の基盤となる。",
    "development": "現代ではマオリ自決運動・ワイタンギ条約交渉の歴史証拠としても援用される。",
    "historical_context": "Te Tiriti o Waitangi（1840）後の主権論争で口承証拠として価値を獲得した。",
    "primary_source_url": "https://teara.govt.nz/en/whakapapa-genealogy",
    "primary_source_type": "Te Ara — The Encyclopedia of New Zealand (official)",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "西洋的な線形物語と異なる系譜的・包摂的物語構造。",
         "related_ai_phenomenon": "知識グラフ・系譜ネットワーク生成"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "人間と非人間（土地・神・動植物）を同一の系譜内に配置する関係的存在論。",
         "related_ai_phenomenon": "non-human agency in AI ethics"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "kinship and genealogy",
         "description": "人類学の親族・系譜研究と直接接続。"},
    ],
})

add({
    "name_ja": "カラキア",
    "name_en": "karakia (incantation/prayer)",
    "name_original": "karakia",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "マオリの祈り・詠唱。儀礼・場の開閉・癒し・移動の際に発話される定型詠唱で、神々（atua）・祖先（tūpuna）への呼びかけを韻律的に行う。tapu（聖性）とnoa（日常性）を媒介する言語行為であり、現代マオリ文学・公式行事でも積極的に保持される。",
    "background": "マオリ宗教実践の中心的言語形式。",
    "development": "現代では非宗教的場面でも文化的アイデンティティの表明として用いられる。",
    "historical_context": "宣教師期以降、変質と再活性化を経た。",
    "primary_source_url": "https://teara.govt.nz/en/karakia-prayer-and-rituals",
    "primary_source_type": "Te Ara",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ワイアタ",
    "name_en": "waiata (Maori song)",
    "name_original": "waiata",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "マオリの歌曲形式の総称。哀歌（waiata tangi）、愛歌（waiata aroha）、子守歌（oriori）等多様な類型を持ち、口承による感情・歴史・知識の伝達装置として機能する。歌詞のメタファーは非マオリ話者には解読困難な複層を持ち、文化的内側と外側の境界を保つ機能を果たす。",
    "background": "マオリ言語と歌の不可分性が口承文学の中核を形成する。",
    "development": "20世紀後半のマオリ・ルネサンスで再活性化された。",
    "historical_context": "マオリ語復興運動の主要な担い手のひとつ。",
    "primary_source_url": "https://teara.govt.nz/en/waiata-traditional-maori-songs",
    "primary_source_type": "Te Ara",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ハカ",
    "name_en": "haka",
    "name_original": "haka",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "マオリの集団詠唱・舞踊の総称で、戦の鬨（peruperu）から歓迎（manawa wera）まで多岐にわたる。身体・声・表情を統合する全身的言語行為であり、テクスト・パフォーマンス・身体の不可分性を体現する。Ka Mate（テ・ラウパラハ作）が最も国際的に知られる。",
    "background": "マオリ社会のあらゆる重要な場で発話される文化的核装置。",
    "development": "ラグビー代表チームの儀礼などで世界的に認知された。",
    "historical_context": "観光化と本来的価値の緊張が継続している。",
    "primary_source_url": "https://teara.govt.nz/en/haka-maori-posture-dance",
    "primary_source_type": "Te Ara",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ウィティ・イヒマエラ",
    "name_en": "Witi Ihimaera",
    "name_original": "Witi Ihimaera",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "1944年生まれのマオリ作家。1972年『Pounamu Pounamu』により、マオリ作家として初めて短編集・1973年に長編『Tangi』を出版。マオリ口承の語りと近代英語小説形式を架橋する作家として国際的評価を獲得し、『The Whale Rider』（1987）が映画化された。",
    "background": "マオリ・ルネサンスの中核作家。",
    "development": "マオリ文学批評・教育プログラムの基盤的存在となった。",
    "historical_context": "マオリ作家の英語圏文学市場進出の先駆。",
    "primary_source_url": "https://teara.govt.nz/en/biographies/6i4/ihimaera-witi",
    "primary_source_type": "Te Ara biographies",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "indigenous storytelling ethnography",
         "description": "人類学的な口承記述伝統との交差点として機能する作品群。"},
    ],
})

add({
    "name_ja": "パトリシア・グレイス",
    "name_en": "Patricia Grace",
    "name_original": "Patricia Grace",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "1937年生まれのマオリ女性作家。1975年『Waiariki』はマオリ女性作家初の出版短編集。『Potiki』（1986）でマオリ集団のランドの保護闘争を描き、口承の語り手・マラエ（集会場）の声を小説形式に組み込む独自の文体を確立した。マオリ女性の文学的主体化を象徴する。",
    "background": "マオリ女性文学運動の先駆者。",
    "development": "ニュージーランド勲章ONZMを2001年に受勲。",
    "historical_context": "マオリ女性の声と土地問題を結ぶ作品群を残した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Patricia_Grace",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
})

add({
    "name_ja": "アルバート・ウェント",
    "name_en": "Albert Wendt",
    "name_original": "Albert Wendt",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "1939年サモア生まれの作家・批評家。『Sons for the Return Home』（1973）でサモア出身者のニュージーランドでの経験を描き、太平洋諸島文学の国際的可視化に決定的な役割を果たした。批評論文「Towards a New Oceania」（1976）で「新しい海洋」という太平洋的アイデンティティ概念を提唱した。",
    "background": "ポリネシア／メラネシア／ミクロネシアを横断する文学的視座を確立した。",
    "development": "オークランド大学・ハワイ大学等で教育者としても影響を持つ。",
    "historical_context": "ポストコロニアル太平洋文学の理論的支柱。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Albert_Wendt",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
})

add({
    "name_ja": "海洋諸島論",
    "name_en": "Sea of Islands",
    "name_original": "Our Sea of Islands",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "トンガ系フィジー人類学者・作家エペリ・ハウオファ（Epeli Hauʻofa）が1993年に提唱した概念。太平洋を「孤立した小島々」ではなく「島々の海＝つながりの世界」として再定式化。植民地的・経済学的「小ささ」観に対抗し、太平洋諸島民の海洋的繋がりと文化的拡がりを再評価する文学・思想的枠組み。",
    "background": "ハウオファ「Our Sea of Islands」（1993）が宣言的テクストとなった。",
    "development": "現代太平洋研究・気候変動アクティヴィズムの基本フレームとなっている。",
    "historical_context": "気候危機下で太平洋諸国の主権論を支える概念。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Epeli_Hauʻofa",
    "primary_source_type": "Wikipedia / published essays",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "中心−周縁構造を解体し、海洋的・関係的物語空間を提示する。",
         "related_ai_phenomenon": "ネットワーク的・分散的ナラティブ生成"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Pacific anthropology",
         "description": "太平洋人類学の枠組みを更新した理論的貢献。"},
    ],
})


# ===============================================================
# B. AFRICAN ORAL (non-C23, distinct from West African griot etc.) (8)
# ===============================================================

add({
    "name_ja": "ンベット",
    "name_en": "mvet",
    "name_original": "mvet",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "中央アフリカのファング族（カメルーン・赤道ギニア・ガボン）の口承叙事詩・楽器の総称。同名の竪琴に伴奏されつつ語られる長大な英雄叙事で、エンクー族（Ekang）の戦士たちの不死世界をめぐる戦いを主題とする。口承定型理論の非西アフリカ的検証事例。",
    "background": "20世紀半ばに人類学者H.プペートが本格的記録を開始。",
    "development": "現代ではUNESCO ICHにファング族のmvet口承が登録されている。",
    "historical_context": "国境を越えるファング族文化の保持媒体。",
    "primary_source_url": "https://ich.unesco.org/en/USL/oral-heritage-of-gelede-00002",
    "primary_source_type": "UNESCO ICH directory",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral-formulaic theory",
         "description": "ロード＝パリーの口承定型詩学のアフリカ的検証事例。"},
    ],
})

add({
    "name_ja": "スンジャタ叙事詩",
    "name_en": "Sundiata epic",
    "name_original": "Sundiata Keita / l'épopée mandingue",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "13世紀マリ帝国の創始者スンジャタ・ケイタを主人公とする西アフリカ・マンディング諸民族の口承叙事詩。グリオによって800年以上にわたり伝承され、Djibril Tamsir Niane『Sundiata: An Epic of Old Mali』（1960）の散文記録で世界的に知られる。アフリカ口承叙事詩の代表例。",
    "background": "ニアネが伝統的グリオ Djeli Mamadou Kouyaté の語りを記録した。",
    "development": "アフリカ文学批評・人類学・歴史学の交差点に位置する。",
    "historical_context": "マリ帝国の歴史実体を口承で保持する稀有な事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sundiata_Keita",
    "primary_source_type": "Wikipedia / Niane 1960",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "個別作者ではなく集合的かつ世代を超えるグリオ系譜が作者性を担う。",
         "related_ai_phenomenon": "LLM分散的著作・集合的作者性"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral epic tradition",
         "description": "口承叙事詩学の代表事例。"},
    ],
})

add({
    "name_ja": "ディンカ口承",
    "name_en": "Dinka oral tradition",
    "name_original": "Dinka oral tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "南スーダンのディンカ族の口承文学。雄牛詩（ox songs）・即興歌・血讐譚・系譜詠唱を含む複層的伝統で、各個人が自身を称える「雄牛の名前（ox-name）」を持ち詩を作るという独自の個人即興詩文化を持つ。Francis Mading Deng『The Dinka and Their Songs』（1973）が標準的記録。",
    "background": "ナイル川流域の半遊牧牧畜文化と密接に結びつく。",
    "development": "南北スーダン内戦・南スーダン独立を経て継承の危機にある。",
    "historical_context": "戦争・難民化により伝承共同体が分散した。",
    "primary_source_url": "https://www.endangeredlanguages.com/lang/1067",
    "primary_source_type": "UCLA endangered languages project",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "アカンバ説話",
    "name_en": "Akamba narratives",
    "name_original": "Akamba narratives",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ケニアのカンバ族（Akamba）の口承説話群。Mukamba／Akambaの語り部（ndalani）が伝承する動物寓話・教訓譚・由来譚で、Gerhard Lindblom『The Akamba in British East Africa』（1920）が初期記録となった。スワヒリ世界周縁の口承文化として、東アフリカ口承文学の重要事例。",
    "background": "バンツー系言語（カンバ語）口承の体系的記録の対象。",
    "development": "現代ではNgūgĩ wa Thiongʼoの口承再評価論で批評対象となっている。",
    "historical_context": "宣教師教育以後の世代差で伝承縮小が進む。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kamba_people",
    "primary_source_type": "Wikipedia",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ベルベル・イマジゲン口承",
    "name_en": "Berber Imazighen oral tradition",
    "name_original": "Imazighen / Berber oral",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "北アフリカ（モロッコ・アルジェリア・チュニジア・リビア・サハラ）に広がるベルベル諸語（タマズィグト等）の口承文学。動物寓話・愛歌（izlan）・諺・即興詩を含み、女性語り手による家庭内伝承の比重が高い。20世紀後半以降の文化復興運動で言語と並行して再活性化されている。",
    "background": "ティフィナグ文字復興と並行して口承記録が進む。",
    "development": "1990年代以降、モロッコ・アルジェリアでの公用語化と並行して文学化される。",
    "historical_context": "アラブ化政策下で抑圧された後、文化復興運動の中核となった。",
    "primary_source_url": "https://www.elararchive.org/dk0395",
    "primary_source_type": "ELAR Endangered Languages Archive",
    "importance_score": 3, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "トゥアレグ詩",
    "name_en": "Tuareg poetry",
    "name_original": "Tuareg poetry / izli",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "サハラ砂漠の遊牧民トゥアレグ族（Imuhagh）の口承詩。タマシェク語による定型詩で、愛歌・戦詩・哀歌・移動詩を含む。砂漠の地理と移動性に深く根ざした詩学で、女性詩人の比重が大きい。現代ではティナリウェン等の音楽グループが詩の音楽化を世界へ媒介する。",
    "background": "リビュコ・ベルベル系言語の詩的伝統を代表する。",
    "development": "1960年代以降の独立運動・砂漠化問題と詩が連動する。",
    "historical_context": "ニジェール・マリ・アルジェリア・リビアの国境を超える口承共同体。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tuareg_music",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "コイサン語族口承",
    "name_en": "Khoisan click-language narratives",
    "name_original": "Khoisan oral",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "南部アフリカのコイサン諸族（San、Khoekhoe等）の口承文学。クリック子音を多用する言語による物語・詩・歌謡で、19世紀末のWilhelm Bleek/Lucy Lloyd の |Xam（カム）語記録が初期重要文書。動物変身譚・トリックスター（Heitsi-Eibib等）・創世譚を含む独自の宇宙観を持つ。",
    "background": "Bleek/Lloyd Collection（南アフリカUCT保存）が世界の口承研究の里程標。",
    "development": "現代ではUNESCO世界記憶遺産に登録されたBleek/Lloyd Collection が公開される。",
    "historical_context": "言語消滅の極端な事例として記録の意義が重大。",
    "primary_source_url": "https://www.unesco.org/en/memory-world/bleek-collection",
    "primary_source_type": "UNESCO Memory of the World",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "クリック音をもつ言語の音韻構造はテキスト中心主義を解体する。",
         "related_ai_phenomenon": "低リソース言語のAI処理"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "trickster archetype",
         "description": "Heitsi-Eibibはトリックスター神話の代表事例。"},
    ],
})

add({
    "name_ja": "ゲエズ典礼文学",
    "name_en": "Ethiopian Geez liturgical literature",
    "name_original": "Ge'ez liturgical literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "エチオピア正教会の典礼語ゲエズ（古代エチオピア語）による聖歌・讃美詩・聖人伝の伝統。聖イアレッド（6世紀）が体系化したとされる zema（聖歌学）と、qene（即興詩）の伝統は世界最古級の宗教文学口承の一つ。文字記録と口承の両者で生き続ける稀有な事例。",
    "background": "アクスム王国（4世紀キリスト教化）以来の連続的伝統。",
    "development": "エチオピア聖歌（zema）はUNESCO ICHに登録されている。",
    "historical_context": "アフリカ最古の文字文化と口承の並存的事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ge%27ez",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})


# ===============================================================
# C. NORTHERN INDIGENOUS (non-North America/Australia/Ainu) (8)
# ===============================================================

add({
    "name_ja": "ヨイク",
    "name_en": "joik (Sami traditional song)",
    "name_original": "joik / juoiggus",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "北極圏のサーミ人の伝統的歌唱。「人・場所・動物について歌う」のではなく「その存在になる」と説明される独自の音楽詩で、定型歌詞より発声・音色・身体性が中心。キリスト教化政策下で「悪魔の歌」として禁止された歴史を経て、20世紀後半の文化復興で再評価された。",
    "background": "サーミ語圏（ノルウェー・スウェーデン・フィンランド・ロシア）の中核口承伝統。",
    "development": "Mari Boine等の現代歌手が国際的に普及させた。",
    "historical_context": "1980年代以降のサーミ自決運動と並行して再活性化された。",
    "primary_source_url": "https://www.unesco.org/en/articles/joik-traditional-sami-song",
    "primary_source_type": "UNESCO ICH",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "歌詞・身体・音響の不可分性が「テクスト」概念を再定義する。",
         "related_ai_phenomenon": "音声AI・マルチモーダル生成"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "対象を「歌う」のでなく「として存在する」という関係的真正性。",
         "related_ai_phenomenon": "AI生成音声の真正性議論"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "animism / shamanic vocal traditions",
         "description": "シャーマニズム・アニミズム研究との接続。"},
    ],
})

add({
    "name_ja": "イヌイト・カヤク叙事詩",
    "name_en": "Inuit qajaq narratives",
    "name_original": "qajaq narratives",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "イヌイトの口承叙事詩・物語群でカヤック（qajaq）操船・狩猟を主題とするもの。極北の海洋環境下で生存技術・空間記憶・倫理を歌・物語・喉歌（katajjaq）で伝承する複合的口承。Knud Rasmussen の第5次トゥーレ探検（1921-1924）で多数記録された。",
    "background": "Rasmussen記録は極北口承文学研究の世界的基礎資料。",
    "development": "現代ではヌナヴト準州設立（1999）以降、自治体支援で再活性化されている。",
    "historical_context": "気候変動と海氷消失が物語環境を破壊しつつある。",
    "primary_source_url": "https://www.oralliterature.org/collections/krasmussen.html",
    "primary_source_type": "World Oral Literature Project / Rasmussen archive",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "グリーンランド口承",
    "name_en": "Greenlandic Kalaallit oral tradition",
    "name_original": "Kalaallit oral tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "グリーンランド・イヌイト（Kalaallit）の口承文学。神話・英雄譚・幽霊譚に加え、宣教師期以降に発展した文字（カラーリスト語）文学を持つユニークな事例。Hans Egede（18世紀）以来の宣教民族誌、Knud Rasmussenの記録、現代のNiviaq Korneliussenら作家へと連続している。",
    "background": "デンマーク植民地下で18世紀から文字化が進んだ希少な北方先住民事例。",
    "development": "21世紀には英訳でNiviaq Korneliussen等の作家が国際的評価を得た。",
    "historical_context": "自治政府（Naalakkersuisut, 2009-）下で文化復興が進む。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Greenlandic_literature",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "オロンホ",
    "name_en": "olonkho (Yakut epic)",
    "name_original": "олонхо / olonkho",
    "original_script": "cyrillic",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ヤクート（サハ）人のテュルク系英雄叙事詩。Nyurgun Bootur 等の英雄が三層宇宙（上界・中界・下界）を旅する長大な物語で、語り手は登場人物を歌い分ける即興口承詩人（olonkhohut）。10,000-15,000行に及ぶ規模を持ち、UNESCO「人類の口承および無形遺産の傑作」（2005）に指定された。",
    "background": "シベリアのテュルク・モンゴル系叙事詩伝統の代表事例。",
    "development": "ソ連崩壊後のサハ共和国でolonkho復興が制度化された（olonkho研究所設立）。",
    "historical_context": "ソ連期の宗教抑圧を経た後、サハ自決運動と並行して再活性化された。",
    "primary_source_url": "https://ich.unesco.org/en/RL/olonkho-yakut-heroic-epos-00145",
    "primary_source_type": "UNESCO ICH official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "三層宇宙構造の長大叙事詩は西洋的小説形式と全く異なる時間性をもつ。",
         "related_ai_phenomenon": "長文ナラティブのAI生成"},
        {"axis": "作者性", "status": "rethinking",
         "rationale": "語り部olonkhohutは即興と伝承の境界に立つ集合的作者。",
         "related_ai_phenomenon": "即興・分散的著作のLLMモデル"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "Lord-Parry oral-formulaic theory",
         "description": "ロード＝パリー口承定型詩学のテュルク系検証事例。"},
    ],
})

add({
    "name_ja": "ゲセル叙事詩",
    "name_en": "Geser epic (Buryat)",
    "name_original": "Гэсэр / Geser",
    "original_script": "cyrillic",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ブリヤート・モンゴル・チベットを横断する英雄ゲセル王の叙事詩。中央アジア最大の口承叙事詩のひとつで、ブリヤート版（rhalbar Geser）はシベリアのバイカル湖周辺の口承詩人 ülgershin によって伝承された。仏教・シャマニズム・テュルク・モンゴル文化が融合する独自の叙事詩。",
    "background": "チベット起源の物語が中央アジア全域に拡散・地域変奏した結果。",
    "development": "20世紀後半のソ連民族学者により大規模記録が進んだ。",
    "historical_context": "ブリヤート民族復興運動の象徴の一つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Epic_of_King_Gesar",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "trans-Asian heroic myth",
         "description": "横断的英雄神話研究と接続。"},
    ],
})

add({
    "name_ja": "マグタール",
    "name_en": "magtaal (Mongolian praise poetry)",
    "name_original": "магтаал / magtaal",
    "original_script": "cyrillic",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "モンゴルの賛歌（praise poetry）口承形式。山岳・河川・馬・偉人を讃える定型詩で、ナーダム祭・婚礼・儀礼で詠唱される。英雄叙事詩 tuuli と並ぶモンゴル口承詩学の主要ジャンル。urtyn duu（長歌）と限られた呼吸法で連続する独自の音楽性を持つ。",
    "background": "モンゴル草原文化の儀礼的口承の中核。",
    "development": "UNESCO ICH登録のurtyn duuと密接に関連する。",
    "historical_context": "社会主義期の抑圧後、民主化（1990）以降に復興した。",
    "primary_source_url": "https://ich.unesco.org/en/RL/urtiin-duu-traditional-folk-long-song-00115",
    "primary_source_type": "UNESCO ICH",
    "importance_score": 3, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "ユピック口承",
    "name_en": "Yupik oral tradition",
    "name_original": "Yupik oral tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "アラスカ西部・ベーリング海沿岸のユピック（Yupʼik / Yupiit）の口承文学。qulirat（古代の物語）と qanemcit（最近の出来事の語り）の二範疇区分が特徴的で、季節儀礼qasgiq（カシム）で長老が語る伝統が継承されてきた。Ann Fienup-Riordanの民族誌的記録が英語圏での主要参照点。",
    "background": "アラスカ先住民言語法（1990）後の言語復興と並行する記録。",
    "development": "ベーセル（Bethel）地域のユピック語学校が口承の継承拠点。",
    "historical_context": "石油経済・気候変動が伝承共同体を圧迫している。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Central_Alaskan_Yupʼik_language",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "チュクチ口承",
    "name_en": "Chukchi oral tradition",
    "name_original": "Chukchi oral tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ロシア極東チュコト半島のチュクチ族の口承文学。動物変身譚・シャマン的物語・季節儀礼歌が中心で、Vladimir Bogoraz（1930年代）の民族誌的記録がソ連民族学の里程標。20世紀末のYuri Rytkheu等のロシア語作家経由でチュクチ口承の主題が世界文学に流入した。",
    "background": "チュクチ語は緊急的危機言語に分類されている。",
    "development": "ソ連崩壊後、ロシア連邦少数民族言語政策の対象として記録が進む。",
    "historical_context": "気候変動による生計システムの崩壊で口承共同体が縮小している。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Chukchi_language",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})


# ===============================================================
# D. SOUTH AMERICAN INDIGENOUS (8)
# ===============================================================

add({
    "name_ja": "ハイリ",
    "name_en": "haylli (Quechua war hymn)",
    "name_original": "haylli",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ケチュア語の戦勝歌・凱歌の総称。インカ帝国期に儀礼・農耕・戦勝祝祭で歌われた定型詠唱の伝統で、Garcilaso de la Vega『Comentarios reales』（1609）等の植民地期記録に部分的に保存される。現代ペルー・ボリビアでは収穫祝祭で再演奏される。",
    "background": "インカ口承伝統の一断片を植民地期スペイン語記録から再構成する。",
    "development": "20世紀のエスノミュージコロジー研究で詳細記述された。",
    "historical_context": "ケチュア語復興運動と並行して再評価される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Quechuan_languages",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "タキ",
    "name_en": "taki (Quechua song)",
    "name_original": "taki",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ケチュア語で「歌」「歌うこと」を意味する一般語。インカ社会では taki uyay（聞く歌）、taki rimay（語る歌）等多様な類型があった。植民地期の Taki Onqoy（歌の病、1564-1572）はインカ復興運動として知られ、歌が政治的・宗教的抵抗の媒介となった事例。",
    "background": "ハイリと並んでケチュア口承詩の基本範疇。",
    "development": "Taki Onqoyは植民地期先住民抵抗運動の代表的事例として研究されている。",
    "historical_context": "歌が単なる芸能でなく集合的政治行動の媒体となった事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Taki_Unquy",
    "primary_source_type": "Wikipedia",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "歌が政治的抵抗運動を発動する事例で、芸術受容の能動的・集合的側面を示す。",
         "related_ai_phenomenon": "AI生成コンテンツの社会運動的受容"},
    ],
})

add({
    "name_ja": "ウルカントゥン",
    "name_en": "ülkantun (Mapuche song)",
    "name_original": "ülkantun",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "チリ・アルゼンチンのマプチェ族の口承歌唱。マプドゥングン語による即興詩・哀歌・夢の歌（pewma）を含み、語りエピシオドと連動しつつ歌い継がれる。マプチェ女性詩人 Elicura Chihuailaf、Liliana Ancalao等の現代詩がülkantunの形式を書記詩に翻訳する実践を行う。",
    "background": "マプドゥングン語は危機言語でELAR等で記録される。",
    "development": "1990年代以降のマプチェ自決運動と並行して文学化が進む。",
    "historical_context": "チリ国家との土地紛争の文脈で詩が政治化される。",
    "primary_source_url": "https://www.elararchive.org/dk0394",
    "primary_source_type": "ELAR Endangered Languages Archive",
    "importance_score": 3, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "アイマラ口承",
    "name_en": "Aymara oral tradition",
    "name_original": "Aymara oral tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ボリビア・ペルー・チリのアイマラ族の口承文学。jaylli（歌）、wayñu（恋歌）、神話的説話を含み、独特な言語類型（証拠性接尾辞、認識的階層）を反映した語りの構造を持つ。Silvia Rivera Cusicanqui等のアイマラ知識人によるアイマラ思想の理論化が現代の文学的展開を支える。",
    "background": "ティティカカ湖周辺のアイマラ社会の口承体系。",
    "development": "ボリビアのEvo Morales政権期（2006-2019）に文化主権が制度化された。",
    "historical_context": "「世界視（cosmovisión）」概念により先住民思想として理論化されている。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Aymara_people",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "アランドゥクア",
    "name_en": "arandukua (Guaraní wisdom)",
    "name_original": "arandukua / arandu",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "パラグアイ・ブラジル・ボリビア・アルゼンチン国境の Guaraní 諸族の知恵・口承知識を意味する語。「ñe'ẽ porã（美しい言葉）」と並んでグアラニー語口承文学の中核概念。Bartolomeu Meliàのフィールドワークで「Mbyá-Guarani の宗教的口承」が世界に知られた。",
    "background": "グアラニー語はパラグアイ公用語化（1992）以降、書記文学化が進んだ。",
    "development": "Augusto Roa Bastos等のグアラニー語要素を含むスペイン語文学に影響を与えた。",
    "historical_context": "イエズス会レドゥクシオン期の文字化と口承の長い葛藤の歴史を持つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Guaraní_mythology",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「美しい言葉」という言語観は、テクスト効率主義のAI生成と対照をなす。",
         "related_ai_phenomenon": "言語生成の倫理・美学"},
    ],
})

add({
    "name_ja": "ヤノマミ・シャマン詠唱",
    "name_en": "Yanomami shamanic narratives",
    "name_original": "Yanomami xapiri",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ブラジル・ベネズエラ国境のアマゾン熱帯林ヤノマミ族のシャマン的口承。シャマンが xapiri（精霊）を呼び出し対話する一連の詠唱で、Davi Kopenawa『La chute du ciel』（仏訳2010）が世界的に知られる。アマゾン破壊への先住民予言として機能する政治的・宇宙論的テクスト。",
    "background": "Bruce Albertがコペナワとの共同制作として25年にわたり記録した。",
    "development": "気候危機・アマゾン保護運動の重要参照テクストとなった。",
    "historical_context": "違法採掘・侵略下の先住民証言として国際的影響を持つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Davi_Kopenawa_Yanomami",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Amazonian shamanism",
         "description": "アマゾン人類学のシャマニズム研究と直結。"},
    ],
})

add({
    "name_ja": "ワユー口承",
    "name_en": "Wayuu oral tradition",
    "name_original": "Wayuu / Wayuunaiki oral",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "コロンビア・ベネズエラ国境のラ・グアヒラ半島のワユー族の口承文学。母系社会の系譜詠唱、夢の解釈（lapü）、紛争解決の話者（pütchipüʼü）の伝統を持つ。Vito Apüshana、Estercilia Simanca等のワユー詩人がワユーナイキ語とスペイン語の双方で執筆する現代運動を担う。",
    "background": "母系・口承中心社会の特徴的事例。",
    "development": "ラテンアメリカ先住民詩運動の重要な担い手。",
    "historical_context": "マラカイボ湖鉱産資源紛争の中心地で口承が政治化される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Wayuu_people",
    "primary_source_type": "Wikipedia overview",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "トゥピ＝グアラニー神話",
    "name_en": "Tupi-Guaraní mythology",
    "name_original": "Tupi-Guaraní mythology",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ブラジル沿岸・内陸のトゥピ＝グアラニー語族諸民族の神話・口承。「悪の地（terra sem mal）」を求める移住神話、双子英雄の物語等を含み、André Thevet・Jean de Léry等の16世紀フランス人による記録が初期文献。Pierre Clastres『大いなる語り部』（1972）で人類学的に再構成された。",
    "background": "16世紀の植民地接触期記録が世界の口承記録として古い事例。",
    "development": "Eduardo Viveiros de Castroの透視主義人類学の主要参照点。",
    "historical_context": "アマゾン人類学・先住民思想研究の中核的伝統。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tupi_people",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "Myth-Narratives", "link_type": "shared_concept",
         "target_entity_name": "South American myth corpus",
         "description": "南米神話比較データベースとの主要接点。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Amerindian perspectivism",
         "description": "Viveiros de Castroの透視主義人類学と接続。"},
    ],
})


# ===============================================================
# E. CROSS-CUTTING CONCEPTS (8)
# ===============================================================

add({
    "name_ja": "口承叙事詩のグローバル伝統",
    "name_en": "global oral epic tradition",
    "name_original": "global oral epic tradition",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "ホメロス研究を起点としたMilman Parry/Albert Lordの口承定型理論を、アフリカ（mvet, Sundiata）、アジア（olonkho, Geser, mvet）、太平洋（whakapapa）等に拡張する比較研究の総称。Ruth Finnegan、John Foley、Karin Barberの理論的貢献により、口承叙事詩は世界的・普遍的伝統として再定式化された。",
    "background": "Lord『The Singer of Tales』（1960）以来の口承定型詩学の世界的拡張。",
    "development": "JOFAL（Journal of Folklore and African Literature）等の専門誌で継続研究。",
    "historical_context": "西欧中心的な「文学」概念を解体した重要な学術運動。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "個別作者性ではなく語り手の系譜的・即興的作者性を中心に置く。",
         "related_ai_phenomenon": "LLMの分散的・即興的著作性"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "西欧的小説形式を相対化する物語形式の多元性を提示する。",
         "related_ai_phenomenon": "ナラティブ生成の文化的多元性"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral-formulaic theory",
         "description": "口承詩学の世界的検証ネットワーク。"},
    ],
})

add({
    "name_ja": "正典としての儀礼詠唱",
    "name_en": "ritual recitation as canon",
    "name_original": "ritual recitation as canon",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "聖典・正典の文書中心主義に対して、口承儀礼における詠唱（karakia, mvet, joik, olonkho等）が事実上の「正典」として機能することを概念化する批評的視座。文字化・文書化を経ない正統性の継承様式は、印刷文化中心の文学正典論を根底から問い直す。",
    "background": "Walter Ong『Orality and Literacy』（1982）の口承文化論を発展させた批評視座。",
    "development": "Karin Barber等のアフリカ口承研究で精緻化されている。",
    "historical_context": "ポストコロニアル文学批評・先住民研究の理論的基礎の一つ。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "文書としての正典概念そのものを口承詠唱が解体する。",
         "related_ai_phenomenon": "AI訓練データの正典構造の文化的偏向"},
    ],
})

add({
    "name_ja": "言語消滅と文学",
    "name_en": "linguistic endangerment and literature",
    "name_original": "linguistic endangerment and literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "世界の言語の半数が今世紀中に消滅すると予測される状況下で、口承文学・先住民文学が直面する根本的危機を主題化する批評的視座。ELAR、PARADISEC、UCLA Endangered Languages等のデジタルアーカイブ運動と並行する文学・批評実践。Daniel Heath Justice等が理論化する。",
    "background": "Krauss（1992）以来の言語多様性危機の言語学的議論を文学に拡張した。",
    "development": "AI転写技術と口承記録の倫理が交差する領域。",
    "historical_context": "気候変動・グローバリゼーションと並行する文化的緊急事態。",
    "primary_source_url": "http://www.endangeredlanguages.com/",
    "primary_source_type": "UCLA Endangered Languages Project",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "言語そのものの消滅は、文学概念の前提を根本から揺るがす。",
         "related_ai_phenomenon": "AIによる絶滅危惧言語の自動転写・再生成"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳によってのみ存続する言語と、原語不可逆性の倫理問題。",
         "related_ai_phenomenon": "機械翻訳と低リソース言語倫理"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "ASR for endangered languages",
         "description": "AI転写・自動音声認識が絶滅危惧言語に応用される倫理的領域。"},
    ],
})

add({
    "name_ja": "口承ジャンル分類の拡張",
    "name_en": "expanded oral genre taxonomy",
    "name_original": "expanded oral genre taxonomy",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "西欧由来の「叙事詩・抒情詩・戯曲」三分類に対し、口承文学が示す膨大なジャンル多様性（系譜詠唱・即興詩・夢の歌・送り歌・地名連鎖等）を体系化する批評運動。Ruth Finnegan『Oral Poetry』（1977）以来の蓄積を経て、UNESCO ICHの口承伝統リスト等で制度化された。",
    "background": "西欧文学ジャンル論の脱中心化を志向する批評運動。",
    "development": "UNESCO Intangible Cultural Heritage の体系で実装された。",
    "historical_context": "比較文学のグローバル化・脱植民地化と並行する。",
    "primary_source_url": "https://ich.unesco.org/en/lists",
    "primary_source_type": "UNESCO ICH lists",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
})

add({
    "name_ja": "先住民学術翻訳問題",
    "name_en": "indigenous-academic translation issues",
    "name_original": "indigenous-academic translation issues",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "先住民口承文学を学術的記述・翻訳に変換する過程で発生する倫理・方法論問題。誰が翻訳するか・誰が利益を得るか・誰の語彙で枠づけるかをめぐる議論で、Linda Tuhiwai Smith『Decolonizing Methodologies』（1999）が決定的影響力を持つ。CARE原則・OCAP原則の理論的基盤。",
    "background": "ポストコロニアル批評と先住民研究の交差点。",
    "development": "Indigenous Data Sovereignty運動・CARE原則として実装された。",
    "historical_context": "20世紀の人類学的記述の倫理的検証に端を発する。",
    "primary_source_url": "https://www.gida-global.org/care",
    "primary_source_type": "Global Indigenous Data Alliance / CARE Principles",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳の主体・倫理を根本から問い直す。",
         "related_ai_phenomenon": "AI翻訳の倫理・データ主権"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "CARE principles for indigenous data",
         "description": "AI訓練・データガバナンスの根本的倫理基盤と直結。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "decolonizing methodologies",
         "description": "脱植民地化方法論の人類学的展開と接続。"},
    ],
})

add({
    "name_ja": "聖俗境界",
    "name_en": "sacred-secular boundary in oral",
    "name_original": "sacred-secular boundary",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民口承伝統期",
    "definition": "口承文学において、誰が・いつ・どこで・誰に対して語ることが許されるかを決定する文化的プロトコル。マオリのtapu/noa、アボリジニのrestricted knowledge、ナバホのhózhó、アイヌの聖なる詠唱等、多くの口承伝統に共通する文化的境界の体系化。AI学習データ倫理の根本問題。",
    "background": "AIATSIS、AILLA等の先住民データアーカイブが制度化した概念。",
    "development": "CARE原則・OCAP原則の中核要素となった。",
    "historical_context": "AI時代における「公開／非公開」二分法の限界を露呈する概念。",
    "primary_source_url": "https://www.gida-global.org/care",
    "primary_source_type": "GIDA / CARE Principles",
    "importance_score": 4, "source_tier": "primary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "誰が読めるかが文化的に決定される受容概念は、AI出力アクセス管理に直結する。",
         "related_ai_phenomenon": "AI出力アクセス制御・倫理的フィルタリング"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「公開知＝普遍的価値」前提を解体する。",
         "related_ai_phenomenon": "AI訓練データの倫理的除外"},
    ],
})

add({
    "name_ja": "パフォーマンス＝テクスト乖離",
    "name_en": "performance vs text gap",
    "name_original": "performance vs text gap",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "口承文学を文字テクストに変換する際に必然的に失われる、声・身体・場・聴衆の存在を理論化する批評視座。Dennis Tedlock、Dell Hymesの「エスノポエティクス」運動が1970年代に体系化し、「テクスト」概念そのものを問い直した。マルチモーダルAIによる口承記録の新しい可能性をも開く。",
    "background": "Tedlock『The Spoken Word and the Work of Interpretation』（1983）が古典。",
    "development": "音声・映像アーカイブのデジタル化と並行して理論的展開を続ける。",
    "historical_context": "文学批評の物質性・身体性への転回の重要起点。",
    "primary_source_url": "https://www.oralliterature.org/",
    "primary_source_type": "World Oral Literature Project",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "テクストとパフォーマンスの不可分性を提示する。",
         "related_ai_phenomenon": "マルチモーダルAIによる口承の再現"},
    ],
})

add({
    "name_ja": "先住民フューチャリズム拡張",
    "name_en": "indigenous futurism extension",
    "name_original": "indigenous futurism (extended)",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "先住民文芸復興期",
    "definition": "Grace Dillon提唱の北米起点「先住民フューチャリズム」を、マオリ・サモア・サーミ・アイマラ・ヤノマミ等の各地域に拡張する近年の文学運動。Witi Ihimaera、Tina Makereti（マオリ）、Linda Hogan（チカソ）、Sami Earth Trilogy等が、各文化の宇宙論を未来想像力に接続する実践を行う。",
    "background": "Dillon『Walking the Clouds』（2012）後の地理的拡張。",
    "development": "気候危機・AI時代における先住民知識の戦略的再配置として広域に展開。",
    "historical_context": "アフロフューチャリズム、太平洋フューチャリズム等の隣接運動と相互参照する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indigenous_futurisms",
    "primary_source_type": "Wikipedia",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "西洋的進歩史観と異なる時間性・宇宙論的多元性を未来想像力に接続する。",
         "related_ai_phenomenon": "AI時代の未来想像力の文化的多元化"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI futures imaginaries / cultural diversification",
         "description": "AI未来想像力の脱中心化を支える文学的実践。"},
    ],
})


# ---------------------------------------------------------------
# Insertion driver
# ---------------------------------------------------------------

def main() -> int:
    print(f"[c31] {len(CONCEPTS)} concepts queued for insertion")
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

    print(f"\n[c31] inserted={inserted} skipped={skipped} failed={failed}")
    print(f"[c31] fourth_transform_tags={fourth_count} cross_domain={cross_count}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
