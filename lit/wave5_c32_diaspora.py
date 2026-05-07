"""
LIT-DB Phase 2 — C32 Wave5: Diaspora & Migration Literature
================================================================
Inserts 40 representative concepts spanning 5 categories:
  A. 主要主題・世界観 (8)
  B. 主要文化圏ディアスポラ文学 (8)
  C. 主要技法・形式 (8)
  D. 主要作家概念 (8)
  E. 批評概念・理論 (8)

subfield_id=20, code='lit_diaspora', region='周縁横断'

Sources: JSTOR / Project MUSE (canonical postcolonial-diaspora studies),
Asian American Writers' Workshop (https://aaww.org/), postcolonial.net,
Cambridge Companion volumes, public author/book pages, scholarly handbooks.
Tier: primary = direct canonical source quotation/edition (Bhabha,
Gilroy, Pratt, Said, Du Bois, Rushdie); secondary = widely-cited
critical accounts; tertiary = synthetic concept names whose attestation
rests on multiple secondary sources.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (周縁横断)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("近代奴隷制・初期ディアスポラ期", "Early Modern Diaspora",
     1500, 1900,
     "大西洋奴隷貿易、ユダヤ離散、華僑・印僑契約労働の世界規模拡散期。"
     "Du Bois『黒人の魂』(1903)直前までの長期形成段階。"),
    ("脱植民地・初期移民文学期", "Decolonization / Early Migrant Lit",
     1900, 1965,
     "二度の世界大戦と脱植民地化に伴う大規模移動・離散の文学的言語化期。"
     "Du Bois、Mahjar詩人、初期Caribbean Voicesらの活動期。"),
    ("ポストコロニアル・ディアスポラ期", "Postcolonial Diaspora",
     1965, 2000,
     "1965年米国移民法改正後の南アジア・東アジア系移民増、"
     "Naipaul・Rushdie・Bhabha・Gilroy・Saidらによる理論化が進展した時代。"),
    ("グローバル・ディアスポラ期", "Global Diaspora",
     2000, 2026,
     "Lahiri・Adichie・Hamid・Díazらの世界市場小説、"
     "翻訳/多言語/トランスナショナルが標準条件となるグローバル文学期。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — 主要主題・世界観 (8)
# ===============================================================

add({
    "name_ja": "ハイフン化アイデンティティ",
    "name_en": "hyphenated identity",
    "name_original": "hyphenated identity",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Asian-American、African-American、Indo-Caribbeanのように"
                  "二重の帰属を「ハイフン」で連結する自己呼称形式。"
                  "出身地と居住地の両方を放棄せず双方に二重の負債を負う"
                  "ディアスポラ的主体の文学的標識として、20世紀後半以降の"
                  "移民文学で制度化された。",
    "background": "Theodore Roosevelt 1915年演説の「hyphenated American」批判が"
                  "逆説的に当事者表現として奪還された経緯を持つ。",
    "development": "1980-90年代のWerner Sollors『Beyond Ethnicity』、"
                   "Asian American文学の制度化と並行して批評概念化。"
                   "Lahiri『The Namesake』が世界文学化した。",
    "historical_context": "米国移民法1965年改正後の多文化主義論争の核心概念。",
    "primary_source_url": "https://www.jstor.org/stable/2713295",
    "primary_source_type": "JSTOR — Sollors 'Beyond Ethnicity'",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "ハイフンで連結された二重帰属主体は単一国民・単一言語前提を解体し、"
                      "AI時代の分散的アイデンティティ表象（マルチプロファイル運用）と構造的に類比される。",
         "related_ai_phenomenon": "AIによるマルチペルソナ生成・複数言語間の人格表現"},
    ],
})

add({
    "name_ja": "間の空間（in-between space）",
    "name_en": "in-between space",
    "name_original": "in-between space",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Homi K. Bhabha『The Location of Culture』(1994)が定式化した"
                  "二項対立的文化区分（植民/被植民、東/西、母国/移住先）の"
                  "あいだで成立する文化交渉の場。固定的本質ではなく差異の"
                  "継続的交渉として文化を再定義する基盤概念。",
    "background": "ファノン・サイードを継承しつつ、ラカン精神分析と"
                  "差延（デリダ）を統合した1990年代理論化の中核。",
    "development": "Bhabha「third space」論へ展開、世界文学・ポストコロニアル研究の"
                   "標準語彙化。多文化都市・移民二世コミュニティ研究に応用。",
    "historical_context": "1990年代の文化的グローバル化と多文化主義論争を背景にする。",
    "primary_source_url": "https://www.routledge.com/The-Location-of-Culture/Bhabha/p/book/9780415336390",
    "primary_source_type": "Routledge — Bhabha 'The Location of Culture'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「あいだ」を主体性の場として理論化する枠組みは、"
                      "AI/人間の境界が交渉的になる時代の主体論と構造的に親和する。",
         "related_ai_phenomenon": "ヒューマン-AI協働における主体性の中間化"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Bhabha と差延・他者性",
         "description": "デリダ・ラカンを継承するBhabha理論との哲学的接続。"},
    ],
})

add({
    "name_ja": "第三の空間（third space）",
    "name_en": "third space",
    "name_original": "third space",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Bhabhaが「第一」「第二」の固定的文化に還元できない、"
                  "発話・翻訳・混淆が起こる象徴的場として概念化。"
                  "あらゆる発話行為が「第三の空間」を経由することで、"
                  "意味は本質的に交渉的・翻訳的になる。",
    "background": "Bhabhaのインタビュー1990(『Identity: Community, Culture, Difference』所収)"
                  "が概念の初出として広く参照される。",
    "development": "Edward Sojaが地理学的空間論として再展開、"
                   "教育学（Gutiérrez）、Asian American studies、"
                   "都市論まで領域拡張した。",
    "historical_context": "1990年代の文化研究の空間論的転回と並走。",
    "primary_source_url": "https://www.routledge.com/The-Location-of-Culture/Bhabha/p/book/9780415336390",
    "primary_source_type": "Routledge — Bhabha 'The Location of Culture' Ch.1",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "発話・翻訳・混淆が起こる「第三の場」の概念は、"
                      "LLMが生成する言語空間が既存テクストの混淆点である事実と直結する。",
         "related_ai_phenomenon": "LLMの混淆的テクスト生成空間"},
        {"axis": "受容", "status": "partial",
         "rationale": "受容も翻訳も「第三の空間」で起こるという考えは、"
                      "AIメディエーションが既定値となる時代の受容論を再考させる。",
         "related_ai_phenomenon": "AIキュレーションを介した文学受容"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "third space / contact zone",
         "description": "人類学DBにおける文化的境界・接触領域の理論との共有。"},
    ],
})

add({
    "name_ja": "トランスナショナル主体",
    "name_en": "transnational subject",
    "name_original": "transnational subject",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "単一国民国家の枠を超えて複数国家・複数文化に同時帰属する"
                  "主体性。Aihwa Ong『Flexible Citizenship』(1999)、"
                  "Gloria Anzaldúa『Borderlands/La Frontera』(1987)らが"
                  "批評概念として体系化、グローバル化文学の基本前提となった。",
    "background": "1990年代の人類学・文化研究におけるglobal flows論を背景にする。",
    "development": "Vertovec/Cohen『Migration, Diasporas and Transnationalism』(1999)、"
                   "現代の「ディアスポラ的市民権」研究まで継続的に拡張。",
    "historical_context": "冷戦後グローバル化と国民国家の相対化。",
    "primary_source_url": "https://www.dukeupress.edu/flexible-citizenship",
    "primary_source_type": "Duke UP — Ong 'Flexible Citizenship'",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ダブル・コンシャスネス（二重意識）",
    "name_en": "double consciousness",
    "name_original": "double consciousness",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "脱植民地・初期移民文学期",
    "definition": "W.E.B. Du Bois『The Souls of Black Folk』(1903)が定式化した、"
                  "黒人がつねに「自己の眼」と「他者の眼で見られた自己」の"
                  "両方から自分を見ざるを得ない分裂した自己意識。"
                  "ディアスポラ主体性論の最古層に位置する古典概念。",
    "background": "ヘーゲル『精神現象学』の主奴弁証法とアメリカ黒人経験の交差。",
    "development": "Paul Gilroy『The Black Atlantic』が大西洋規模に拡張、"
                   "Asian American/Latino研究にも転用される基盤概念へ。",
    "historical_context": "Reconstruction期以後のJim Crow体制と人種隔離の経験。",
    "primary_source_url": "https://www.gutenberg.org/ebooks/408",
    "primary_source_type": "Project Gutenberg — Du Bois 'Souls of Black Folk'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "他者の眼差しと自己の眼差しの分裂的同居というDu Bois的定式は、"
                      "AI観測下にある自己（社会信用スコア、レコメンドアルゴリズム）の主体性論と直結する。",
         "related_ai_phenomenon": "アルゴリズム的監視下の二重的自己意識"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "borrowed_from",
         "target_entity_name": "ヘーゲル主奴弁証法",
         "description": "Du Boisの二重意識論はヘーゲル弁証法を黒人経験で読み替えた。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "二重意識・自己他者性",
         "description": "人類学DBの自己-他者構造論との共有概念。"},
    ],
})

add({
    "name_ja": "亡命・流謫（exilic condition）",
    "name_en": "exile / exilic condition",
    "name_original": "exile",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Edward Said『Reflections on Exile』(2000)が定式化した、"
                  "強制的・非選択的離散状態を文学的・知的姿勢へと転換する条件。"
                  "祖国喪失の悲嘆を「対位法的（contrapuntal）視点」と"
                  "知的批判性の源泉として再価値化する20世紀後半の主要主題。",
    "background": "Saidのパレスチナ系亡命知識人としての自伝的経験を理論的に昇華。",
    "development": "Brodsky『Less Than One』、Kundera亡命論、"
                   "Mahmood Darwish詩学、現代の難民文学研究まで継続的展開。",
    "historical_context": "20世紀の強制移住・難民問題の文学的言語化。",
    "primary_source_url": "https://www.hup.harvard.edu/catalog.php?isbn=9780674004931",
    "primary_source_type": "Harvard UP — Said 'Reflections on Exile'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "亡命的視点を「対位法」として価値化するSaidの定式は、"
                      "AI時代の脱中心化された知的観察主体の理論的源流となる。",
         "related_ai_phenomenon": "AI観測者としての脱中心化された知的視座"},
        {"axis": "真正性", "status": "partial",
         "rationale": "亡命者の「真の祖国」喪失をめぐる真正性論は、"
                      "AI生成コンテンツが取り組む「起源なき表現」の問題系と接続する。",
         "related_ai_phenomenon": "起源・出自を問えないAI生成テクスト"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Said と知的亡命",
         "description": "哲学DBにおけるSaidポジションとの直接共有。"},
    ],
})

add({
    "name_ja": "多言語的自己（multilingual self）",
    "name_en": "multilingual self",
    "name_original": "multilingual self",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "複数言語間で生成・分裂・再統合される主体の文学的形象化。"
                  "Aneta Pavlenko『Emotions and Multilingualism』(2005)、"
                  "Yoko Tawada・Theresa Hak Kyung Cha『Dictée』らの"
                  "実験的散文で形式化された、ディアスポラ文学固有の主体形態。",
    "background": "応用言語学のmultilingual identity研究と文学的実験の合流。",
    "development": "Lahiri『In Other Words』(2016)のイタリア語移行記、"
                   "Tawada「エクソフォニー」論、Cha『Dictée』の継続的再評価。",
    "historical_context": "グローバル化時代の翻訳的自己形成の制度化。",
    "primary_source_url": "https://www.cambridge.org/core/books/emotions-and-multilingualism/A05DDDD7E5C7AB7DA88D88BD0CE7A7C5",
    "primary_source_type": "Cambridge UP — Pavlenko",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "複数言語間で揺れる主体形成は、多言語LLMが「言語間で意味を媒介する」"
                      "あり方と直接的に類比される。",
         "related_ai_phenomenon": "多言語LLMの言語間意味媒介・転移学習"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "言語選択ごとに人格・記憶・感情が異なる多言語主体は、"
                      "AIエージェントの言語別ペルソナと構造的に類似する。",
         "related_ai_phenomenon": "AIエージェントの言語別パーソナリティ"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "shared_concept",
         "target_entity_name": "多言語LLM",
         "description": "AI開発DBの多言語モデル研究との直接接続。"},
    ],
})

add({
    "name_ja": "脱領土化（deterritorialization）",
    "name_en": "deterritorialization",
    "name_original": "déterritorialisation",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Deleuze & Guattari『Kafka: pour une littérature mineure』"
                  "(1975)が定式化、もとの土地・言語・文化的固有性から"
                  "切り離された状態を、欠如ではなく生産的潜勢力として捉える概念。"
                  "マイナー文学論の中核で、ディアスポラ文学批評の標準語彙となった。",
    "background": "Deleuze哲学の流動性・リゾーム的世界観を背景にする。",
    "development": "Caren Kaplan『Questions of Travel』(1996)、"
                   "Arjun Appadurai『Modernity at Large』のディアスポラ的応用、"
                   "ディアスポラ・グローバル化研究の標準語彙化。",
    "historical_context": "1970-80年代フランス現代思想と移民文学批評の合流。",
    "primary_source_url": "https://www.upress.umn.edu/book-division/books/kafka",
    "primary_source_type": "U Minnesota P — Deleuze/Guattari 'Kafka'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "borrowed_from",
         "target_entity_name": "Deleuze 脱領土化",
         "description": "哲学DBのDeleuze概念群からディアスポラ文学が借用。"},
    ],
})


# ===============================================================
# CATEGORY B — 主要文化圏ディアスポラ文学 (8)
# ===============================================================

add({
    "name_ja": "ブラック・アトランティック",
    "name_en": "Black Atlantic",
    "name_original": "Black Atlantic",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Paul Gilroy『The Black Atlantic: Modernity and Double Consciousness』"
                  "(1993)が提示した、奴隷貿易を通じて大西洋規模で形成された"
                  "黒人ディアスポラの文化空間。アフリカ・カリブ・南北アメリカ・"
                  "英国を結ぶ循環的近代性として、国民文学枠組みを根本的に問い直した。",
    "background": "Du Bois「二重意識」を空間化・地政学化する試み。",
    "development": "アフロ・アメリカ研究、カリブ研究、Black British studiesの統合枠組みとなり、"
                   "現代のサブサハラ・アフリカ文学と北米黒人文学の架橋に展開。",
    "historical_context": "大西洋奴隷貿易400年の文化的負債の言語化。",
    "primary_source_url": "https://www.hup.harvard.edu/catalog.php?isbn=9780674076068",
    "primary_source_type": "Harvard UP — Gilroy 'The Black Atlantic'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ブラック・アトランティック",
         "description": "人類学DBの大西洋黒人ディアスポラ研究との共有。"},
    ],
})

add({
    "name_ja": "カリブ・ディアスポラ文学",
    "name_en": "Caribbean diaspora literature",
    "name_original": "Caribbean diaspora literature",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "ロンドン・ニューヨーク・トロント・パリ等を拠点に展開する"
                  "カリブ出身作家の文学群。Sam Selvon『The Lonely Londoners』(1956)、"
                  "V.S. Naipaul、Jamaica Kincaid、Edwidge Danticat、Caryl Phillipsらが代表。"
                  "クレオール性・帰還不能性・植民地後の主体性を中心主題とする。",
    "background": "1948年Empire Windrush号到着以後のカリブからの戦後移民の波。",
    "development": "Caribbean Voices（BBCラジオ）からBooker McConnell受賞作家群へ展開、"
                   "現代のグローバル・カリブ文学（NoViolet Bulawayo、Marlon Jamesら）を準備。",
    "historical_context": "戦後英連邦移民法と植民地解体の文学的応答。",
    "primary_source_url": "https://www.cambridge.org/core/books/cambridge-companion-to-the-postcolonial-novel/96B5D52B7B5",
    "primary_source_type": "Cambridge Companion — Postcolonial Novel",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "南アジア系ディアスポラ文学",
    "name_en": "South Asian diaspora literature",
    "name_original": "South Asian diaspora literature",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "インド・パキスタン・バングラデシュ・スリランカ系作家による"
                  "英語/英語以外の文学。Salman Rushdie『Midnight's Children』(1981)、"
                  "Bharati Mukherjee、Jhumpa Lahiri、Kiran Desai、Mohsin Hamid、"
                  "Hanif Kureishiらが代表。1965年米国移民法・英連邦の歴史を二重に背負う。",
    "background": "1947年印パ分離・1960-80年代英米移民法改正の歴史。",
    "development": "Booker受賞作（Rushdie 1981, K.Desai 2006, Adiga 2008）に象徴される世界市場化、"
                   "AAWW(Asian American Writers' Workshop)等プラットフォームでの制度化。",
    "historical_context": "南アジア独立後ディアスポラの世界文学市場参入。",
    "primary_source_url": "https://aaww.org/",
    "primary_source_type": "AAWW — Asian American Writers' Workshop",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "華人ディアスポラ文学",
    "name_en": "Chinese diaspora literature",
    "name_original": "華人ディアスポラ文学 / 海外華文文学",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "華僑・華人による中国本土外で生産される文学群。"
                  "Maxine Hong Kingston『The Woman Warrior』(1976)、"
                  "Ha Jin、Ng Kim Chew、Yiyun Li、Tash Awらが代表。"
                  "中華圏の「華語語系（Sinophone）」(Shu-mei Shih)概念で再編されつつある。",
    "background": "19世紀後半の苦力貿易、20世紀の中国革命・文革期亡命の波が累積。",
    "development": "Sinophone Studies（Shu-mei Shih, David Wang）が中心-周縁モデルを再編、"
                   "アジア系米文学・東南アジア華語文学・台湾文学を横断的に統合。",
    "historical_context": "中国近現代史の亡命・移民の累積結果。",
    "primary_source_url": "https://cup.columbia.edu/book/sinophone-studies/9780231157513",
    "primary_source_type": "Columbia UP — Shih/Tsai/Bernards 'Sinophone Studies'",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ユダヤ・ディアスポラ文学",
    "name_en": "Jewish diaspora literature",
    "name_original": "Jewish diaspora literature",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "脱植民地・初期移民文学期",
    "definition": "ユダヤ離散の文学伝統。Sholem Aleichem、Isaac Bashevis Singer、"
                  "Saul Bellow、Philip Roth、Cynthia Ozick、Bernard Malamud、"
                  "Edmond Jabès、Aharon Appelfeld、Patrick Modianoらの「祖国なき言語」"
                  "（イディッシュ・英語・フランス語・ヘブライ語）における"
                  "記憶・離散・ホロコースト後の表象を中心とする。",
    "background": "ガルート（galut）の宗教的概念から世俗化された離散概念への変容。",
    "development": "ホロコースト文学（Celan, Levi）、ポストホロコースト第二世代（Appelfeld）、"
                   "Sephardi/Mizrahi文学、現代Israeli-American 二重ディアスポラ文学へ拡張。",
    "historical_context": "ユダヤ離散2000年の累積とホロコースト後の再構築。",
    "primary_source_url": "https://www.jewishvirtuallibrary.org/yiddish-literature",
    "primary_source_type": "Jewish Virtual Library",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アラブ・ディアスポラ文学（マフジャル）",
    "name_en": "Arab diaspora literature (Mahjar)",
    "name_original": "أدب المهجر (Adab al-Mahjar)",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "脱植民地・初期移民文学期",
    "definition": "20世紀初頭、北米・南米へ移住したアラブ系作家による文学運動。"
                  "Khalil Gibran『The Prophet』(1923)、Ameen Rihaniが代表で、"
                  "ニューヨークの「ペン・リーグ（al-Rabita al-Qalamiya）」(1920)が制度化。"
                  "現代ではEdward Said、Rabih Alameddine、Hisham Matarらが継承。",
    "background": "オスマン帝国期から20世紀の二度の世界大戦、アラブ独立後の継続的離散。",
    "development": "中東ディアスポラ第一世代（Mahjar）から第二世代（9/11後の英語アラブ系作家）へ展開、"
                   "Naomi Shihab Nye、Mohja Kahfらアラブ系米文学の制度化。",
    "historical_context": "オスマン帝国崩壊・パレスチナ問題・近年のシリア難民危機の累積。",
    "primary_source_url": "https://www.britannica.com/art/Mahjar-school",
    "primary_source_type": "Britannica — Mahjar school",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コリアン・ディアスポラ文学",
    "name_en": "Korean diaspora literature",
    "name_original": "Korean diaspora literature / 재외 한인 문학",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "韓国系米国・在日・中国朝鮮族・中央アジア高麗人らによる文学。"
                  "Theresa Hak Kyung Cha『Dictée』(1982)、Chang-rae Lee、Min Jin Lee"
                  "『Pachinko』(2017)、柳美里・李良枝（在日）、ユ・ミリ"
                  "らが代表。植民地期日本・朝鮮戦争・分断・移民の三重の歴史を背負う。",
    "background": "日本植民地期(1910-45)・朝鮮戦争(1950-53)・分断・冷戦期離散の連続史。",
    "development": "Korean American文学制度化（KoreanLit、AAWW）、在日朝鮮人文学の世界化、"
                   "中国朝鮮族文学・中央アジア高麗人文学の再評価まで多領域化。",
    "historical_context": "20世紀朝鮮半島の植民・戦争・分断の累積結果。",
    "primary_source_url": "https://aaww.org/",
    "primary_source_type": "AAWW — Korean American 著者特集",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ラテン米移民文学（チカーノ／チカーナ）",
    "name_en": "Chicano/a literature",
    "name_original": "literatura chicana",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "メキシコ系米国人作家による文学。Rodolfo Anaya『Bless Me, Ultima』(1972)、"
                  "Sandra Cisneros、Gloria Anzaldúa、Tomás Rivera、Helena María Viramontesらが代表。"
                  "1965年のチカーノ運動以降に制度化、英語/スペイン語/Spanglishの複言語性、"
                  "メキシコ・米国境界(borderlands)を中核空間とする。",
    "background": "1848年米墨戦争後の併合領土と1965年公民権運動以降のチカーノ運動。",
    "development": "Anzaldúa『Borderlands/La Frontera』(1987)で理論化、"
                   "メスティーサ意識・第三世界フェミニズム理論を米文学に統合。",
    "historical_context": "米国南西部のラティーノ人口拡大と公民権運動の文学的応答。",
    "primary_source_url": "https://www.auntlute.com/borderlands-la-frontera",
    "primary_source_type": "Aunt Lute Books — Anzaldúa 'Borderlands'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — 主要技法・形式 (8)
# ===============================================================

add({
    "name_ja": "コードスイッチング",
    "name_en": "code-switching",
    "name_original": "code-switching",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "発話・文章中で複数言語を文脈に応じて切り替える言語実践。"
                  "ディアスポラ文学では Junot Díaz、Sandra Cisneros、Gloria Anzaldúa "
                  "らがSpanglish、ヒンドゥー混じり英語、日本語混じり英語などの形で"
                  "中核技法とし、二重的主体性の言語表現として制度化した。",
    "background": "社会言語学のCode-Switching研究（Gumperz, Myers-Scotton）が文学批評に流入。",
    "development": "Asian American、ラテンアメリカ系、アラブ系米文学の標準技法に。"
                   "Adichie、Lahiri、Hamidらの世界市場小説でも継続的に活用。",
    "historical_context": "1960年代の言語学的記述から1980年代の文学技法化への移行。",
    "primary_source_url": "https://www.cambridge.org/core/journals/applied-linguistics",
    "primary_source_type": "Cambridge — Applied Linguistics 査読論文群",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "言語間切替を芸術的技法として恒常化するコードスイッチングは、"
                      "多言語LLMの言語混在生成と直接的に類比される。",
         "related_ai_phenomenon": "多言語LLMによる言語混在テクスト生成"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "多言語混在生成",
         "description": "LLMの混在言語生成能力が文学的コードスイッチング技法と並走する。"},
    ],
})

add({
    "name_ja": "トランスリンガル・ライティング",
    "name_en": "translingual writing",
    "name_original": "translingual writing",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "母語以外の言語で書く実践、もしくは複数言語を貫通して書く実践。"
                  "Steven G. Kellman『The Translingual Imagination』(2000)、"
                  "Lahiri『In Other Words』(2016)、Yoko Tawada「エクソフォニー」、"
                  "Joseph Conrad、Vladimir Nabokovが古典的祖先、現代の標準語彙化された概念。",
    "background": "Conrad（ポーランド語→英語）、Nabokov（露→英）の20世紀古典に発する系譜。",
    "development": "応用言語学のtranslingual approach、Modern Language Associationの議論を経て"
                   "文学批評の標準語彙化、Lahiri / Tawadaを世界文学化した。",
    "historical_context": "グローバル化期の母語/書記言語非対称の制度化。",
    "primary_source_url": "https://www.nebraskapress.unl.edu/nebraska/9780803227458",
    "primary_source_type": "Nebraska UP — Kellman 'Translingual Imagination'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "母語/非母語の境界を芸術的に踏み越える実践は、"
                      "AIが言語間で滑らかに表現を移送する能力と構造的に近接する。",
         "related_ai_phenomenon": "言語間転移生成・スタイル移送"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳と創作の境界の曖昧化が、AI翻訳/生成の境界曖昧化と直結する。",
         "related_ai_phenomenon": "AI翻訳/生成の境界曖昧化"},
    ],
})

add({
    "name_ja": "未訳外国語挿入",
    "name_en": "untranslated foreign words insertion",
    "name_original": "untranslated foreign words",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "本文中に外国語語彙を翻訳・注釈なしで挿入する技法。"
                  "Junot Díaz『The Brief Wondrous Life of Oscar Wao』(2007)が"
                  "スペイン語をイタリック化さえせずに英語に組み込んだ実例で象徴される。"
                  "「読者を排除する権利」を主張し、ディアスポラ的読者層の制度化を促進した。",
    "background": "Chinua Achebe『Things Fall Apart』のイボ語挿入が祖型。",
    "development": "Adichie、Cisneros、Hamid、Mohsin Hamid、現代の世界文学標準技法へ。"
                   "電子書籍時代にはホバー翻訳機能との緊張関係を持つ。",
    "historical_context": "1960年代以降のグローバル英語文学の言語ヘゲモニー批判。",
    "primary_source_url": "https://www.jstor.org/stable/40468109",
    "primary_source_type": "JSTOR — postcolonial linguistic strategy 査読論文",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "未訳挿入は読者を翻訳の不在に直面させる実践であり、"
                      "AI自動翻訳が標準化する時代の翻訳/非翻訳の境界政策と直結する。",
         "related_ai_phenomenon": "AI即時翻訳と未訳化の倫理的緊張"},
    ],
})

add({
    "name_ja": "多言語パン（多言語的言葉遊び）",
    "name_en": "multilingual punning",
    "name_original": "multilingual punning",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "二言語以上の音韻・意味・字義を交差させた言葉遊び技法。"
                  "Joyce『Finnegans Wake』が祖型、Anzaldúa『Borderlands』、"
                  "Tawada『犬婿入り』、Nabokov『Lolita』、Vikram Seth"
                  "らディアスポラ作家がSpanglish、独英、日英の交差で多用する。",
    "background": "ジョイス的多言語遊戯のディアスポラ的継承と再活用。",
    "development": "現代の世界市場文学（Hamid、Mohsin、現代Adichie等）でも"
                   "局所的ハイライトとして継承される。",
    "historical_context": "モダニズム多言語実験のディアスポラ的延長。",
    "primary_source_url": "https://www.jstor.org/stable/3110066",
    "primary_source_type": "JSTOR — multilingual wordplay 査読論文",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "亡命回想録",
    "name_en": "exile memoir",
    "name_original": "exile memoir",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "亡命・離散の経験を一人称回想として再構成するノンフィクション形式。"
                  "Edward Said『Out of Place』(1999)、Vladimir Nabokov『Speak, Memory』(1951)、"
                  "André Aciman『Out of Egypt』(1994)、Hisham Matarが代表。"
                  "失われた祖国の地理・言語・家族の記憶を再構築する自己物語形式。",
    "background": "20世紀亡命知識人の自伝的記録の累積（Stefan Zweig、Walter Benjamin等）。",
    "development": "現代の難民回想録（Eddie Huang、Sabrina Imblerなど多様化）、"
                   "ハイブリッド回想録（フィクション混入）への発展。",
    "historical_context": "20-21世紀の強制移住・難民経験の累積。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/15428/out-of-place-by-edward-w-said/",
    "primary_source_type": "Penguin Random House — Said 'Out of Place'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "世代サーガ",
    "name_en": "generational saga",
    "name_original": "generational saga",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "三世代以上にわたる家族史を通じて移民の世代変容を描く長編形式。"
                  "Min Jin Lee『Pachinko』(2017)、Jhumpa Lahiri『The Namesake』(2003)、"
                  "Amy Tan『The Joy Luck Club』(1989)、Yaa Gyasi『Homegoing』(2016)が代表。"
                  "祖国を知る世代から知らない世代への漸進的喪失と再発見を構造化する。",
    "background": "19世紀ヨーロッパ家族小説（Mann『ブッデンブローク家の人々』）の系譜の更新。",
    "development": "1990-2010年代の北米ディアスポラ文学の主要形式に。"
                   "Netflix等映像化で世界市場展開。",
    "historical_context": "戦後の北米移民世代の二・三世化のタイミングと一致。",
    "primary_source_url": "https://www.hachettebookgroup.com/titles/min-jin-lee/pachinko/9781455563937/",
    "primary_source_type": "Hachette — Min Jin Lee 'Pachinko'",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "世代間トラウマ・ナラティブ",
    "name_en": "transgenerational trauma narrative",
    "name_original": "transgenerational trauma narrative",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "親・祖父母世代のトラウマ（戦争・大量殺戮・強制移住）が"
                  "後続世代に転移・継承される過程を描く文学形式。"
                  "Marianne Hirschの「ポストメモリ」(postmemory)概念で理論化、"
                  "Art Spiegelman『Maus』、Edwidge Danticat、ヴィエト・タン・ウェン"
                  "らが代表。ホロコースト第二世代研究を起点に世界化した。",
    "background": "1990年代のホロコースト第二・三世代研究（Hirsch, Hoffman）。",
    "development": "アルメニア・カンボジア・難民第二世代文学全般へ拡張、"
                   "現代的なヤング・アダルト小説市場でも標準テーマ化。",
    "historical_context": "20世紀大量暴力後の世代記憶の文学的構造化。",
    "primary_source_url": "https://cup.columbia.edu/book/the-generation-of-postmemory/9780231156523",
    "primary_source_type": "Columbia UP — Hirsch 'The Generation of Postmemory'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "パリンプセスト的物語",
    "name_en": "palimpsestic narrative",
    "name_original": "palimpsestic narrative",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "複数の物語層・歴史層・言語層を上書きしつつ下層を保持する物語形式。"
                  "羊皮紙の重ね書き（パリンプセスト）に由来する比喩で、"
                  "Salman Rushdie『Midnight's Children』、Michael Ondaatje『The English Patient』、"
                  "Caryl Phillipsらが利用。ディアスポラ文学の重層的時間意識の形式化。",
    "background": "ジェネット詩学の「パランプセスト」(1982)概念が文学批評に流入。",
    "development": "ポストコロニアル文学批評の標準語彙化、"
                   "現代のクライメイトフィクション・歴史小説でも応用される。",
    "historical_context": "1980-90年代のポストコロニアル時間意識論の制度化。",
    "primary_source_url": "https://www.upress.umn.edu/book-division/books/palimpsests",
    "primary_source_type": "U Minnesota P — Genette 'Palimpsests' 英訳",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "物語の重ね書き・下書き保持の構造は、"
                      "AI生成テクストの先行テクスト潜在的内包と類比される。",
         "related_ai_phenomenon": "LLMの先行テクスト埋め込み・暗黙の参照"},
    ],
})


# ===============================================================
# CATEGORY D — 主要作家概念 (8)
# ===============================================================

add({
    "name_ja": "想像の故郷（Rushdie）",
    "name_en": "imaginary homelands",
    "name_original": "imaginary homelands",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Salman Rushdie『Imaginary Homelands』(1991)が定式化した、"
                  "移民・亡命作家にとって祖国は再現的に取り戻せず、"
                  "記憶と想像の合成体として「想像の故郷（Indias of the mind）」"
                  "として再構築されるしかないとする命題。ディアスポラ文学批評の中核命題化した。",
    "background": "Rushdie自身のインド-英国二重移動経験の理論的精錬。",
    "development": "Lahiri、Hamid、Adichie、Hosseiniら次世代作家の前提となり、"
                   "「ディアスポラ的真正性」の批判的再考の起点となった。",
    "historical_context": "1981年Booker Prize後のRushdie言説の制度化。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/16921/imaginary-homelands-by-salman-rushdie/",
    "primary_source_type": "Penguin Random House — Rushdie 'Imaginary Homelands'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「想像で再構築された故郷」概念は、"
                      "AI生成された「擬似的記憶」「合成的祖国」表象との直接的類比を示す。",
         "related_ai_phenomenon": "AI合成による故郷・記憶の再構築"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "記憶と想像の合成として故郷を物語ることは、"
                      "AIが断片から物語的全体性を生成する操作と類比的である。",
         "related_ai_phenomenon": "AI物語生成における記憶合成"},
    ],
})

add({
    "name_ja": "条件としての翻訳（Lahiri）",
    "name_en": "translation as condition",
    "name_original": "translation as condition",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "Jhumpa Lahiri『In Other Words』(2016)・『Translating Myself and Others』(2022)が"
                  "定式化した、ディアスポラ作家にとって翻訳は職業的選択ではなく実存的条件であるとする命題。"
                  "母語(ベンガル語)・第一書記語(英語)・選択的翻訳語(イタリア語)の三層構造で生きる作家性の理論化。",
    "background": "Lahiriの2012年ローマ移住・イタリア語による執筆実験の文学的精錬。",
    "development": "現代の翻訳論・世界文学論の中心命題に。Tawada「エクソフォニー」、"
                   "Aciman、Mohsin Hamidらの作家論的言説で並走的に発展。",
    "historical_context": "21世紀グローバル化文学の翻訳的本性の自己認識。",
    "primary_source_url": "https://press.princeton.edu/books/hardcover/9780691231167/translating-myself-and-others",
    "primary_source_type": "Princeton UP — Lahiri 'Translating Myself and Others'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "翻訳が実存的条件となる作家性は、AIが言語間翻訳を即時的に行う時代の"
                      "翻訳概念の根本的変容と直結する。",
         "related_ai_phenomenon": "AI翻訳の即時化と作家的翻訳実践の差異化"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "翻訳論",
         "description": "詩学DBの翻訳・翻案論との接続。"},
    ],
})

add({
    "name_ja": "Spanglish（Díaz）",
    "name_en": "Spanglish (Díaz)",
    "name_original": "Spanglish",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Junot Díaz『The Brief Wondrous Life of Oscar Wao』(2007)で"
                  "中核技法として制度化された、英語とドミニカ・スペイン語の"
                  "コードスイッチング・混淆形式。スペイン語イタリック化を拒否、"
                  "イスパニック・ナードカルチャー・歴史を密に縫い込んだ独自の語り口。",
    "background": "ニュージャージー州ドミニカ系移民共同体の日常的混合言語が芸術化された。",
    "development": "Pulitzer Prize受賞(2008)で世界文学化、後続のSandra Cisneros、Daniel José Older、"
                   "Helena María Viramontesらラテン米系作家の標準技法に。",
    "historical_context": "1990-2000年代の米国ラティーノ文学の制度的成熟期。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/103157/the-brief-wondrous-life-of-oscar-wao-by-junot-diaz/",
    "primary_source_type": "Penguin Random House — Díaz 'Oscar Wao'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "境界の声（Cisneros）",
    "name_en": "border voice",
    "name_original": "border voice",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Sandra Cisneros『The House on Mango Street』(1984)で"
                  "確立された、米墨境界地域(borderlands)に住むラティーナの"
                  "断章的な短散文形式の声。詩と散文の境界を曖昧化し、"
                  "Anzaldúaのメスティーサ意識と並走する文体的革新。",
    "background": "1980年代チカーナ・フェミニズム運動と短散文的伝統の合流。",
    "development": "若い女性主体の語り、Spanglish混入、断章形式が"
                   "後続のラティーナ作家・YA市場の標準モデル化。",
    "historical_context": "チカーノ運動以降の女性的声の制度的可視化。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/123213/the-house-on-mango-street-by-sandra-cisneros/",
    "primary_source_type": "Penguin Random House — Cisneros 'Mango Street'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "祖先の記憶（Danticat）",
    "name_en": "ancestral memory (Danticat)",
    "name_original": "ancestral memory",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "Edwidge Danticat『Krik? Krak!』(1995)・『Brother, I'm Dying』(2007)が"
                  "形式化した、ハイチからの女性的口承伝統の記憶を文学化する手法。"
                  "祖母世代・母世代の語りを米国生まれ世代が継承する三世代的伝承の構造化。",
    "background": "ハイチの女性的物語伝統(マルキノス)と移民後の継承断絶の交渉。",
    "development": "現代のCaribbean Diaspora文学の標準モデル化、"
                   "Yaa Gyasi、NoViolet Bulawayoらアフリカ系世代サーガにも影響。",
    "historical_context": "1980-2000年代の米国ハイチ系移民第二世代の文学的成熟。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/11537/krik-krak-by-edwidge-danticat/",
    "primary_source_type": "Penguin Random House — Danticat 'Krik? Krak!'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "拒絶される根本主義者（Hamid）",
    "name_en": "reluctant fundamentalism",
    "name_original": "reluctant fundamentalism",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "Mohsin Hamid『The Reluctant Fundamentalist』(2007)で"
                  "形式化された、9/11後の南アジア系米国人の主体性の揺れを"
                  "「反西洋」の単純化に抗して描く一人称独白形式。"
                  "西洋エリート教育を受けた主体が母国へ「不本意に」回帰する過程を描く。",
    "background": "9/11後の南アジア系・ムスリム系米国人への差別と監視の経験。",
    "development": "現代の世界市場小説の標準形式となり、Booker shortlist入り。"
                   "映画化(2012)でグローバル文学市場に定着。",
    "historical_context": "9/11以降の「テロとの戦争」期の文学的応答。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/77027/the-reluctant-fundamentalist-by-mohsin-hamid/",
    "primary_source_type": "Penguin Random House — Hamid 'Reluctant Fundamentalist'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "言語政治（Ngũgĩ）",
    "name_en": "language politics (Ngũgĩ)",
    "name_original": "Ngũgĩ wa Thiong'o language politics",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Ngũgĩ wa Thiong'o『Decolonising the Mind』(1986)が定式化した、"
                  "ポストコロニアル作家は植民地者の言語(英語)を捨てて"
                  "母語(ギクユ語)で書くべきであるとする言語選択倫理。"
                  "ディアスポラ作家のRushdie / Achebe的「英語拡張派」と対立する基本軸。",
    "background": "ケニア独立(1963)後のNgũgĩの言語的・政治的ラディカル化、亡命経験。",
    "development": "Ngũgĩ自身の継続的母語実践、"
                   "アフリカ文学批評の主要争点となり現在も継続的論争。",
    "historical_context": "1980年代アフリカ脱植民地化文学の言語選択論争。",
    "primary_source_url": "https://www.boydellandbrewer.com/9781847014368/decolonising-the-mind/",
    "primary_source_type": "James Currey — Ngũgĩ 'Decolonising the Mind'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "partial",
         "rationale": "「植民地者の言語を捨てよ」というNgũgĩ的命題は、"
                      "AI言語モデルが英語中心である現状の批判的検討に直結する。",
         "related_ai_phenomenon": "LLMの英語中心性とアフリカ諸言語の不均衡"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "LLM言語的不均衡",
         "description": "AI開発DBの言語資源不均衡論との並走的関係。"},
    ],
})

add({
    "name_ja": "媒介（Hosseini）",
    "name_en": "mediation (Hosseini)",
    "name_original": "mediation",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "Khaled Hosseini『The Kite Runner』(2003)・『A Thousand Splendid Suns』(2007)が"
                  "実現した、アフガニスタン経験を西洋読者向けに翻訳・媒介する作家性。"
                  "ディアスポラ作家を「文化翻訳者」として位置づける現代の主要モードで、"
                  "市場成功と「真正性」批判の両方を生む争点的形式。",
    "background": "9/11後のアフガニスタンへの西洋的関心と作家自身の医師-亡命者的来歴。",
    "development": "9/11以降のディアスポラ作家による母国の西洋向け媒介の批評的議論を喚起。"
                   "Adichie、Lahiri、Hamidらと比較する批評の標準軸に。",
    "historical_context": "21世紀初頭の「テロとの戦争」期の文化媒介者需要。",
    "primary_source_url": "https://www.penguinrandomhouse.com/books/55987/the-kite-runner-by-khaled-hosseini/",
    "primary_source_type": "Penguin Random House — Hosseini 'Kite Runner'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — 批評概念・理論 (8)
# ===============================================================

add({
    "name_ja": "ディアスポラ的美学",
    "name_en": "diasporic aesthetics",
    "name_original": "diasporic aesthetics",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "ディアスポラ条件から固有に生まれる美学的特性—多言語性・断片性・"
                  "重層的時間性・文化交渉—を体系的に理論化する批評枠組み。"
                  "Stuart Hall、James Cliffordらが1990年代に枠組み化、"
                  "現代の世界文学批評・カルチュラル・スタディーズの中核語彙。",
    "background": "Cultural Studiesと文学批評の合流による1990年代の理論的精錬。",
    "development": "Brent Hayes Edwards『The Practice of Diaspora』(2003)、"
                   "現代世界文学論の基底概念として定着。",
    "historical_context": "1990年代多文化主義論争のなかで美学領域に拡張。",
    "primary_source_url": "https://www.hup.harvard.edu/catalog.php?isbn=9780674011038",
    "primary_source_type": "Harvard UP — Edwards 'Practice of Diaspora'",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ハイブリディティ（Bhabha）",
    "name_en": "hybridity (Bhabha)",
    "name_original": "hybridity",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Bhabha『The Location of Culture』(1994)で再概念化された、"
                  "植民者と被植民者、「自己」と「他者」が混淆を通じて生成する文化形態。"
                  "純粋性・本質を解体し、文化を継続的混淆過程として捉え直す枠組みで、"
                  "ディアスポラ批評の中心語彙となった。",
    "background": "生物学的・植物学的概念の文化研究的転用と、"
                  "Robert Young『Colonial Desire』らの批判的検討を含む。",
    "development": "ディアスポラ批評の標準語彙化と並行して、"
                   "「ハイブリッドの政治的中立化」批判（Aijaz Ahmad, Arif Dirlik）も累積。",
    "historical_context": "1980-90年代多文化主義・グローバル化論争の中核概念。",
    "primary_source_url": "https://www.routledge.com/The-Location-of-Culture/Bhabha/p/book/9780415336390",
    "primary_source_type": "Routledge — Bhabha 'Location of Culture'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ハイブリディティ",
         "description": "人類学DBにおける文化混淆論との直接共有。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Bhabha 哲学的位置",
         "description": "哲学DBのBhabha項との接続。"},
    ],
})

add({
    "name_ja": "擬態（mimicry, 植民地的）",
    "name_en": "mimicry (colonial)",
    "name_original": "mimicry",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Bhabha「Of Mimicry and Man」(1984)が定式化した、"
                  "被植民者が植民者を模倣しつつ「ほぼ同じだが完全には同じでない」"
                  "差異を発生させ、結果的に植民地権威を脅かす逆説的実践。"
                  "ディアスポラ主体の二重的位置を分析する基本概念。",
    "background": "Macaulay 1835年「インド教育覚書」の英国化政策の批判的再読。",
    "development": "Naipaul『The Mimic Men』を批評的に再評価し、"
                   "現代のglobal English文学・コードスイッチング論まで延長。",
    "historical_context": "脱植民地化期の文化政策・英語教育の批判的解読。",
    "primary_source_url": "https://www.jstor.org/stable/778467",
    "primary_source_type": "JSTOR — Bhabha 'Of Mimicry and Man' October 28",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "コンタクト・ゾーン（Pratt）",
    "name_en": "contact zone",
    "name_original": "contact zone",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Mary Louise Pratt『Imperial Eyes』(1992)が定式化した、"
                  "歴史的に分離していた人々が植民地拡大・移住等で出会い、"
                  "非対称な権力関係のなかで文化交渉が起こる場。"
                  "ディアスポラ文学・批評の標準的分析単位として制度化された。",
    "background": "言語学のpidginization研究と歴史研究の合流。",
    "development": "教育学（writing in contact zones）、人類学、博物館研究まで多領域化。"
                   "ディアスポラ文学の主要分析枠組みに。",
    "historical_context": "1990年代多文化主義教育論争のなかで制度化。",
    "primary_source_url": "https://www.routledge.com/Imperial-Eyes-Travel-Writing-and-Transculturation/Pratt/p/book/9780415438179",
    "primary_source_type": "Routledge — Pratt 'Imperial Eyes'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "コンタクト・ゾーン",
         "description": "人類学DBにおける接触領域論との直接共有。"},
    ],
})

add({
    "name_ja": "文化翻訳（Asad）",
    "name_en": "cultural translation",
    "name_original": "cultural translation",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Talal Asad『Genealogies of Religion』(1993)が定式化した、"
                  "言語間翻訳を超えた異文化間の意味体系の翻訳実践。"
                  "翻訳には不可避の権力非対称が伴うことを強調し、"
                  "Bhabha、Spivakの翻訳論と並走する批評枠組み。",
    "background": "文化人類学の翻訳問題（Lienhardt, Geertz）の批判的継承。",
    "development": "現代の翻訳論・ディアスポラ文学批評の標準語彙化、"
                   "AI翻訳時代の文化翻訳論争まで継続。",
    "historical_context": "1980-90年代の人類学的翻訳問題の文学批評流入。",
    "primary_source_url": "https://www.press.jhu.edu/books/title/3094/genealogies-religion",
    "primary_source_type": "Johns Hopkins UP — Asad 'Genealogies of Religion'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "borrowed_from",
         "target_entity_name": "Asad 文化翻訳",
         "description": "人類学DBのAsadからの直接借用。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "翻訳論",
         "description": "詩学DBの翻訳論との接続。"},
    ],
})

add({
    "name_ja": "旅する理論（Said）",
    "name_en": "traveling theory",
    "name_original": "traveling theory",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "ポストコロニアル・ディアスポラ期",
    "definition": "Edward Said「Traveling Theory」(1983)が定式化した、"
                  "理論が起源の文脈から別の文脈に「旅する」過程で必然的に変容する命題。"
                  "理論輸入・移植の不純化を擁護し、ディアスポラ的批評実践の自己理論化として機能する。",
    "background": "Saidのパレスチナ-米国二重亡命位置の理論的精錬。",
    "development": "Saidが後年「Traveling Theory Reconsidered」(1994)で再考、"
                   "現代の世界批評・グローバル理論論の基本枠組みに。",
    "historical_context": "1980年代の理論「輸入」批判のなかで定式化。",
    "primary_source_url": "https://www.hup.harvard.edu/catalog.php?isbn=9780674922297",
    "primary_source_type": "Harvard UP — Said 'The World, the Text, and the Critic'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Said 理論的位置",
         "description": "哲学DBのSaid項との接続。"},
    ],
})

add({
    "name_ja": "エクソフォニック・ライティング",
    "name_en": "exophonic writing",
    "name_original": "exophonic writing / Exophonie",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "母語以外の言語で書く実践を「エクソフォニー」と呼び、"
                  "Susan Arndt et al.『Exophonie: Anders-Sprachigkeit (in) der Literatur』(2007)"
                  "が独語圏で理論化、Yoko Tawadaが日本語圏に紹介した概念。"
                  "translingual writing と並ぶ姉妹概念で、独自の制度化過程を持つ。",
    "background": "ドイツ語圏でのトルコ系・東欧系作家の累積による批評必要性の発生。",
    "development": "Tawada、Aciman、Lahiriら世界文学化作家を統合的に再評価、"
                   "translingual writingと並走する批評語彙として制度化。",
    "historical_context": "21世紀ドイツ語圏多文化文学の理論的成熟。",
    "primary_source_url": "https://www.kulturverlag-kadmos.de/exophonie",
    "primary_source_type": "Kadmos — Arndt et al. 'Exophonie'",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "母語からの離脱を芸術的選択とするエクソフォニー実践は、"
                      "AIが言語を「外側から」操作するあり方と並走的に理論化される。",
         "related_ai_phenomenon": "AIによる「言語の外」からの言語操作"},
    ],
})

add({
    "name_ja": "トランスローカリティ",
    "name_en": "translocality",
    "name_original": "translocality",
    "original_script": "roman",
    "subfield_code": "lit_diaspora",
    "region": "周縁横断",
    "period_key": "グローバル・ディアスポラ期",
    "definition": "Ulrike Freitag/Achim von Oppen『Translocality: The Study of Globalising Processes』(2010)"
                  "が体系化した、グローバルとローカルの二項を超えて、複数のローカルが"
                  "翻訳的につながる文化空間の概念。トランスナショナルが国家枠を含意するのに対し、"
                  "トランスローカルは「場所と場所」の直接的連関を強調する。",
    "background": "1990-2000年代のglobalization研究の批判的精錬。",
    "development": "ディアスポラ文学批評・移民研究の標準語彙化、"
                   "現代の世界文学研究で多用される。",
    "historical_context": "21世紀の脱中心化されたグローバル化研究の制度化。",
    "primary_source_url": "https://brill.com/display/title/16798",
    "primary_source_type": "Brill — Freitag/von Oppen 'Translocality'",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "ローカル間の翻訳的連関というトランスローカリティ概念は、"
                      "AI翻訳が場所間の連関を即時化する現象と直結する。",
         "related_ai_phenomenon": "AI翻訳による場所間連関の即時化"},
        {"axis": "主体", "status": "partial",
         "rationale": "国民国家を経由しない場所主体は、AIネットワーク上の脱国家的主体と並走する。",
         "related_ai_phenomenon": "AIネットワーク上の脱国家的主体"},
    ],
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------
RELATIONS: list[tuple[str, str, str, str]] = [
    ("ハイフン化アイデンティティ", "トランスナショナル主体", "extends",
     "ハイフン化アイデンティティはトランスナショナル主体性の言語的標識として機能する。"),
    ("間の空間（in-between space）", "第三の空間（third space）", "extends",
     "Bhabhaの「間の空間」と「第三の空間」は理論的に連続した概念対。"),
    ("ハイブリディティ（Bhabha）", "間の空間（in-between space）", "extends",
     "ハイブリディティが起こる場としての「間の空間」が理論的前提となる。"),
    ("擬態（mimicry, 植民地的）", "ハイブリディティ（Bhabha）", "extends",
     "Bhabhaの擬態論はハイブリディティ論の発生論的前段階。"),
    ("ダブル・コンシャスネス（二重意識）", "ブラック・アトランティック", "influences",
     "Du Boisの二重意識論をGilroyが空間化したものがブラック・アトランティック。"),
    ("亡命・流謫（exilic condition）", "旅する理論（Said）", "extends",
     "Saidの亡命的視点が「旅する理論」の批評実践の基礎を成す。"),
    ("旅する理論（Said）", "文化翻訳（Asad）", "influences",
     "理論の旅は文化翻訳の不純化過程として理論化される。"),
    ("脱領土化（deterritorialization）", "トランスローカリティ", "influences",
     "Deleuze的脱領土化概念がトランスローカリティの理論的祖型を提供する。"),
    ("多言語的自己（multilingual self）", "コードスイッチング", "contains",
     "多言語的自己はコードスイッチングを言語実践として体現する。"),
    ("多言語的自己（multilingual self）", "トランスリンガル・ライティング", "extends",
     "多言語的自己がトランスリンガル・ライティングの主体を成す。"),
    ("トランスリンガル・ライティング", "エクソフォニック・ライティング", "extends",
     "エクソフォニック・ライティングはトランスリンガル・ライティングの欧州語圏版同義概念。"),
    ("コードスイッチング", "多言語パン（多言語的言葉遊び）", "extends",
     "多言語パンはコードスイッチングを意図的言葉遊びとして特殊化したもの。"),
    ("コードスイッチング", "Spanglish（Díaz）", "contains",
     "Díaz文体はコードスイッチングを中核技法として組み込む。"),
    ("Spanglish（Díaz）", "未訳外国語挿入", "extends",
     "Díaz文体は未訳スペイン語挿入を体系化した代表例。"),
    ("ラテン米移民文学（チカーノ／チカーナ）", "境界の声（Cisneros）", "contains",
     "Cisnerosの「境界の声」はチカーナ文学の中核形式。"),
    ("ラテン米移民文学（チカーノ／チカーナ）", "Spanglish（Díaz）", "contains",
     "Spanglishはラテン米系米文学全般の特徴的言語実践でDíazで芸術化された。"),
    ("カリブ・ディアスポラ文学", "祖先の記憶（Danticat）", "contains",
     "Danticatの「祖先の記憶」はカリブディアスポラ文学の中核形式。"),
    ("南アジア系ディアスポラ文学", "想像の故郷（Rushdie）", "contains",
     "Rushdieの「想像の故郷」概念は南アジア系ディアスポラ文学の中核命題。"),
    ("南アジア系ディアスポラ文学", "条件としての翻訳（Lahiri）", "contains",
     "Lahiriの「条件としての翻訳」は南アジア系ディアスポラ文学の世代的進化を示す。"),
    ("南アジア系ディアスポラ文学", "拒絶される根本主義者（Hamid）", "contains",
     "Hamid作品は9/11後南アジア系ディアスポラ文学の主要形式を確立した。"),
    ("世代サーガ", "世代間トラウマ・ナラティブ", "extends",
     "世代間トラウマ・ナラティブは世代サーガに記憶論的次元を加えた発展形。"),
    ("亡命回想録", "亡命・流謫（exilic condition）", "extends",
     "亡命回想録は亡命的条件を一人称形式で文学化する形式。"),
    ("ブラック・アトランティック", "脱領土化（deterritorialization）", "influences",
     "Gilroyのブラック・アトランティック論は脱領土化された文化空間を提示する。"),
    ("コンタクト・ゾーン（Pratt）", "第三の空間（third space）", "extends",
     "Prattのコンタクト・ゾーンとBhabhaの第三の空間は重層的に並走する。"),
    ("コンタクト・ゾーン（Pratt）", "文化翻訳（Asad）", "influences",
     "文化翻訳はコンタクト・ゾーンの分析装置として機能する。"),
    ("ハイブリディティ（Bhabha）", "ディアスポラ的美学", "influences",
     "ハイブリディティ論がディアスポラ的美学の理論的基盤を成す。"),
    ("条件としての翻訳（Lahiri）", "トランスリンガル・ライティング", "extends",
     "Lahiriの「条件としての翻訳」はトランスリンガル・ライティングの作家論的精錬。"),
    ("言語政治（Ngũgĩ）", "トランスリンガル・ライティング", "criticizes",
     "Ngũgĩの母語回帰論はトランスリンガル・ライティングの英語拡張派と理論的に対立する。"),
    ("拒絶される根本主義者（Hamid）", "媒介（Hosseini）", "contains",
     "Hamidの一人称独白とHosseiniの媒介は9/11後ディアスポラ作家の代替的モデル。"),
    ("祖先の記憶（Danticat）", "世代間トラウマ・ナラティブ", "extends",
     "Danticatの「祖先の記憶」は世代間トラウマ・ナラティブの代表的事例。"),
    ("世代間トラウマ・ナラティブ", "パリンプセスト的物語", "extends",
     "世代間トラウマは物語の重層化（パリンプセスト性）として形式化される。"),
    ("ユダヤ・ディアスポラ文学", "世代間トラウマ・ナラティブ", "contains",
     "ホロコースト第二世代文学が世代間トラウマ理論の発生地。"),
    ("ハイブリディティ（Bhabha）", "コンタクト・ゾーン（Pratt）", "extends",
     "ハイブリディティとコンタクト・ゾーンは並走的にディアスポラ批評の中核語彙を成す。"),
    ("華人ディアスポラ文学", "トランスローカリティ", "extends",
     "華人ディアスポラ文学（Sinophone）はトランスローカル的文化空間を文学化する。"),
    ("コリアン・ディアスポラ文学", "世代間トラウマ・ナラティブ", "contains",
     "コリアン・ディアスポラ文学は植民地・戦争・分断の世代間トラウマを継承する。"),
    ("アラブ・ディアスポラ文学（マフジャル）", "亡命・流謫（exilic condition）", "extends",
     "マフジャル文学はアラブ離散の亡命的条件を文学化した先駆。"),
    ("亡命・流謫（exilic condition）", "亡命回想録", "contains",
     "亡命的条件は亡命回想録の主題的核となる。"),
    ("脱領土化（deterritorialization）", "ハイブリディティ（Bhabha）", "influences",
     "Deleuze的脱領土化はBhabha的ハイブリディティの理論的隣接概念。"),
    ("想像の故郷（Rushdie）", "亡命回想録", "influences",
     "Rushdieの「想像の故郷」概念は亡命回想録の認識論的前提となる。"),
    ("ディアスポラ的美学", "パリンプセスト的物語", "contains",
     "パリンプセスト的物語はディアスポラ的美学の代表的形式の一つ。"),
    ("ハイフン化アイデンティティ", "ダブル・コンシャスネス（二重意識）", "extends",
     "ハイフン化アイデンティティはDu Bois的二重意識のミクロ言語学的形式化。"),
    ("ダブル・コンシャスネス（二重意識）", "亡命・流謫（exilic condition）", "influences",
     "Du Boisの二重意識論はSaidの亡命的視点論の理論的祖先。"),
    ("文化翻訳（Asad）", "条件としての翻訳（Lahiri）", "influences",
     "Asadの文化翻訳論はLahiriの実存的翻訳概念と理論的に並走する。"),
    ("エクソフォニック・ライティング", "言語政治（Ngũgĩ）", "criticizes",
     "エクソフォニーは母語回帰論と緊張関係を持つ理論的対極。"),
    ("Spanglish（Díaz）", "境界の声（Cisneros）", "extends",
     "DíazのSpanglishはCisnerosの境界の声を新世代版に発展させた。"),
]


def main() -> int:
    print(f"[wave5_c32_diaspora] inserting {len(CONCEPTS)} concepts...")
    if len(CONCEPTS) != 40:
        print(f"  WARNING: expected 40 concepts, got {len(CONCEPTS)}")

    name_to_id: dict[str, int] = {}
    fourth_count = 0
    cd_count = 0
    relation_count = 0

    with LitDB() as db:
        # 1) Seed periods
        period_ids: dict[str, int] = {}
        for name_ja, name_en, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=name_ja, region="周縁横断",
                start_year=sy, end_year=ey,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"  period: {name_ja!r} -> id={pid}")

        # 2) Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            period_key = entry.pop("period_key", None)
            if period_key:
                entry["period_id"] = period_ids[period_key]

            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid

            for axis_entry in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **axis_entry)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform failed for {entry['name_ja']}: {e}")

            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept",
                        lit_entity_id=cid,
                        target_db=cd["target_db"],
                        link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"),
                    )
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r}"
                      f" (sid={sid}, tid={tid})")
                continue
            db.insert_relation(
                source_type="concept", source_id=sid,
                target_type="concept", target_id=tid,
                relation_type=rtype,
                description=desc,
                confidence=4,
            )
            relation_count += 1

        # 4) Summary
        summary = db.progress_summary()
        print()
        print("[wave5_c32_diaspora] inserted:")
        print(f"  concepts (DB total): {summary['concepts']}")
        print(f"  fourth_transform_tags (DB total): {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain (DB total): {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations (DB total): {summary['relations']} "
              f"(this run: +{relation_count})")
        print(f"  source_tier dist: {db.tier_distribution()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
