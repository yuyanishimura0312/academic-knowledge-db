"""
LIT-DB Phase 2 — C24: Africa Modern (アフリカ文学・独立後・現代)
====================================================================
40 concepts across five categories:
  A. 独立後ナイジェリア・ガーナ (8): Achebe Things Fall Apart, Achebe No
     Longer at Ease, Achebe critique of Conrad, Soyinka theatre,
     Soyinka Lion and the Jewel, Soyinka Death and the King's Horseman,
     Ngũgĩ Weep Not Child, Ama Ata Aidoo
  B. 東アフリカ (8): Ngũgĩ Decolonising the Mind, Ngũgĩ Gikuyu writing,
     Okot p'Bitek Song of Lawino, Nuruddin Farah, Tanzanian Kiswahili,
     Yusuf Idris, Khalid el Hossainy, Burundian/Rwandan post-genocide
  C. 南アフリカ (8): Coetzee Disgrace, Coetzee Waiting for the Barbarians,
     Gordimer, André Brink, Bessie Head, Mphahlele, Fugard theatre,
     post-apartheid literature
  D. フランコフォン・ルゾフォン (8): Cheikh Hamidou Kane, Mariama Bâ,
     Senghor late, Sembène Ousmane, Mongo Beti, Tahar Ben Jelloun,
     Agualusa, Mia Couto
  E. 21世紀・現代 (8): Adichie Half of a Yellow Sun, Adichie Americanah,
     Teju Cole Open City, Helon Habila, Maaza Mengiste, NoViolet Bulawayo,
     Yvonne Adhiambo Owuor, Tsitsi Dangarembga Nervous Conditions

subfield_id=15, code='lit_africa', region='グローバルサウス'
C23 covers oral traditions + colonial-era + early négritude (period 1880-1980 early).
C24 covers post-independence canonical works (1958+) + 21st-century African fiction.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (extends C23 with later periods)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("独立後初期", "Early Post-Independence", 1960, 1980,
     "アフリカ諸国の独立直後の文学的高揚期。脱植民地化・言語論争・新しい美学の模索。"),
    ("独立後中期", "Mid Post-Independence", 1980, 2000,
     "アパルトヘイト終結（1994）・冷戦終結期の文学。内省・ジェンダー・国民国家の幻滅・移動の主題化。"),
    ("21世紀アフリカ文学", "21st Century African Literature", 2000, 2030,
     "アフリカ系ディアスポラ作家の世界文学的台頭期。Caine Prize・Booker等を通じた国際的承認。"),
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
# A. 独立後ナイジェリア・ガーナ (8)
# ===============================================================

add({
    "name_ja": "アチェベ『崩れゆく絆』",
    "name_en": "Things Fall Apart (Achebe)",
    "name_original": "Things Fall Apart",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ナイジェリア人作家チヌア・アチェベ（Chinua Achebe）の長編小説（1958）。イボ族の戦士オコンクウォの興亡を中心に、19世紀末イボ社会の精緻な内面と英国植民地化の到来を描く。Heinemann African Writers Seriesの第1巻として刊行され、「アフリカ人によるアフリカの内側からの語り」を確立した記念碑的作品。世界100以上の言語に翻訳され、アフリカ文学の正典の中核を形成する。",
    "background": "イェイツの詩「The Second Coming」から題を採り、植民地化を内的崩壊として描いた。",
    "development": "三部作（『崩れゆく絆』『神の矢』『もはや安らぎは得られず』）の起点となった。",
    "historical_context": "コンラッド『闇の奥』に対するアフリカ側からの応答として位置づけられる。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Things_Fall_Apart",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "「アフリカ人がアフリカを書く」という表象主体の根本転換を世界文学に示した。AI時代の表象主体性論争にも構造的影響を与える。",
         "related_ai_phenomenon": "AI生成における表象主体性"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "西欧読者のために翻訳されつつもイボ語の格言・歌を保持する二重受容構造は、AI翻訳時代の文化的不可訳性議論と直結する。",
         "related_ai_phenomenon": "AI翻訳における文化的不可訳性"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "Igbo ethnography",
         "description": "イボ族民族誌の文学的内在化として人類学的価値を持つ。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "African philosophy of history",
         "description": "アフリカ的歴史哲学の文学的表現として直結。"},
    ],
})

add({
    "name_ja": "アチェベ『もはや安らぎは得られず』",
    "name_en": "No Longer at Ease (Achebe)",
    "name_original": "No Longer at Ease",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アチェベの長編小説（1960）。『崩れゆく絆』の主人公オコンクウォの孫オビ・オコンクウォを主人公とし、英国留学から帰国した青年エリート官僚が独立直前のラゴスで汚職に堕ちる過程を描く。題はT.S.エリオット「東方の三博士の旅」から。植民地末期エリート層の道徳的・実存的疲弊を描いた独立期最初の重要作。",
    "background": "ナイジェリア独立（1960年10月）と同年の刊行で時代の象徴となった。",
    "development": "三部作の中軸として『神の矢』（1964）に接続する。",
    "historical_context": "独立期エリートの腐敗を予言的に描いた政治小説として読まれ続ける。",
    "primary_source_url": "https://en.wikipedia.org/wiki/No_Longer_at_Ease",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "アチェベのコンラッド批判",
    "name_en": "Achebe's critique of Conrad",
    "name_original": "An Image of Africa: Racism in Conrad's Heart of Darkness",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "アチェベが1975年マサチューセッツ大学講演で発表し、1977年Massachusetts Reviewに掲載した批評論文。コンラッド『闇の奥』を「徹底した人種差別主義者」の作品と断じ、アフリカを「ヨーロッパの対極にある原始の暗黒」として固定化する西欧正典批評を根本批判した。ポストコロニアル批評の出発点の一つとなり、サイード『オリエンタリズム』（1978）と並ぶ転換点。",
    "background": "西欧文学批評におけるアフリカ表象の構造的偏見を可視化した。",
    "development": "正典再評価論争・カノン論争を世界批評に引き起こした。",
    "historical_context": "1980年代以降の英文学カリキュラム改革の理論的根拠の一つとなった。",
    "primary_source_url": "https://www.jstor.org/stable/25088813",
    "primary_source_type": "JSTOR — Massachusetts Review 1977",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「誰が誰について書く権利を持つか」という根本的な表象倫理を提起。AI時代の文化的データ抽出論争と構造的に共鳴する。",
         "related_ai_phenomenon": "AI訓練データの文化的偏向"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "postcolonial epistemology",
         "description": "ポストコロニアル認識論の基礎文献として直結。"},
    ],
})

add({
    "name_ja": "ショインカ演劇",
    "name_en": "Wole Soyinka theatre",
    "name_original": "Soyinka theatre",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ナイジェリア人劇作家・詩人ウォーレ・ショインカ（Wole Soyinka, 1934-）の演劇活動の総体。ヨルバの儀礼演劇・神話（特にオグン神信仰）と西欧的演劇形式を融合させ、独自の総合演劇を樹立した。1960年に1960 Maskersを結成、Orisun Theatreと合わせてナイジェリア独立期演劇運動を主導。1986年アフリカ人初のノーベル文学賞受賞。",
    "background": "イバダン大学演劇研究で西欧演劇を学び、ナイジェリア帰国後にヨルバ儀礼を再発見した。",
    "development": "Drama, Death, and the King's Horseman, A Dance of the Forests等の主要戯曲を生んだ。",
    "historical_context": "アフリカ演劇のグローバル規模での承認を確立した。",
    "primary_source_url": "https://www.nobelprize.org/prizes/literature/1986/soyinka/biographical/",
    "primary_source_type": "Nobel Prize official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "媒体", "status": "rethinking",
         "rationale": "演劇＝儀礼＝神話を不可分に統合した「総合演劇」概念は、AI時代のマルチモーダル・パフォーマンス芸術と理論的に接続される。",
         "related_ai_phenomenon": "マルチモーダル生成・身体性"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "ritual poetics",
         "description": "儀礼詩学の現代的展開として直結。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Yoruba metaphysics",
         "description": "ヨルバ形而上学の演劇的展開として接続。"},
    ],
})

add({
    "name_ja": "ショインカ『ライオンと宝石』",
    "name_en": "The Lion and the Jewel (Soyinka)",
    "name_original": "The Lion and the Jewel",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ショインカの喜劇（初演1959、刊行1963）。ヨルバ村落イルジンレを舞台に、伝統的首長バログンと近代主義教師ラクンレが村娘シディの愛をめぐって争う三角関係を描く。歌・踊り・パントマイム・合唱を融合し伝統と近代の弁証法を提示。コロニアル＝ポストコロニアル過渡期の文化的選択を喜劇形式で問う。",
    "background": "イバダン大学卒業作品としてロイヤル・コート劇場で上演された。",
    "development": "アフリカ演劇の世界的レパートリー入りを果たした。",
    "historical_context": "西欧モダニズムでなくヨルバ的混淆性を選ぶ村娘の結末は文化的選択の寓話と読まれる。",
    "primary_source_url": "https://en.wikipedia.org/wiki/The_Lion_and_the_Jewel",
    "primary_source_type": "Wikipedia / Oxford UP 1963",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ショインカ『死と王の従者』",
    "name_en": "Death and the King's Horseman (Soyinka)",
    "name_original": "Death and the King's Horseman",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ショインカの戯曲（初演1976、刊行1975）。1946年オヨ王国の実話に基づき、王の死に従い殉死すべき馬丁長エレシン・オバが英国植民地官ピルキングスに阻まれ、息子オラウンデが代わって自死する悲劇。ヨルバの宇宙観における「過渡」（transition）の概念とアリストテレス悲劇形式を融合させた、ショインカの最高傑作とされる。",
    "background": "ショインカ自身が「文化的衝突劇ではない」と序文で強調し、形而上学的悲劇として位置づけた。",
    "development": "ノーベル賞受賞理由の中心作の一つとして繰り返し参照される。",
    "historical_context": "アフリカ古典悲劇形式の確立例として演劇史に記憶される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Death_and_the_King%27s_Horseman",
    "primary_source_type": "Wikipedia / Norton Critical Edition",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "「過渡的領域」という非線形時空構造は西欧的因果物語論を解体する。",
         "related_ai_phenomenon": "非線形ナラティブ生成"},
    ],
})

add({
    "name_ja": "ンギュギ『泣くな、わが子よ』",
    "name_en": "Weep Not, Child (Ngũgĩ)",
    "name_original": "Weep Not, Child",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ケニア人作家ンギュギ・ワ・ジオンゴ（Ngũgĩ wa Thiong'o, 当時James Ngugi名義）の長編小説（1964）。マウマウ蜂起（1952-60）期の少年ンジョロゲの目を通し、ギクユ農民家族の植民地的土地剥奪と教育への希望を描く。東アフリカ作家による英語小説として最初に出版された記念碑作で、Heinemann AWS第7巻。",
    "background": "リーズ大学留学中に執筆された。",
    "development": "三部作（『泣くな、わが子よ』『川を隔てて』『一粒の麦』）の起点となった。",
    "historical_context": "ケニア独立（1963）直後の政治的記憶整理に文学的形式を与えた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Weep_Not,_Child",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "アマ・アタ・アイドゥー",
    "name_en": "Ama Ata Aidoo",
    "name_original": "Ama Ata Aidoo",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ガーナ人作家・劇作家・教育者（1942-2023）。アフリカ初期女性作家の代表的存在。戯曲『The Dilemma of a Ghost』（1965）は黒人ガーナ人男性とアフリカ系アメリカ人女性の結婚を通じディアスポラ的引き裂きを描き、アフリカ女性作家として最初に出版された戯曲となった。詩・小説（『Our Sister Killjoy』1977）でアフリカ女性のグローバル視点を切り開いた。",
    "background": "教育大臣・大学教授も務め、アフリカ女性作家の制度的基盤を築いた。",
    "development": "Caine Prize審査員等を通じ次世代女性作家を育成した。",
    "historical_context": "ベシー・ヘッド、フローラ・ンワパと並ぶアフリカ女性文学の開拓者。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ama_Ata_Aidoo",
    "primary_source_type": "Wikipedia / Longman African Writers",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})


# ===============================================================
# B. 東アフリカ (8)
# ===============================================================

add({
    "name_ja": "ンギュギ『精神の脱植民地化』",
    "name_en": "Decolonising the Mind (Ngũgĩ)",
    "name_original": "Decolonising the Mind: The Politics of Language in African Literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "ンギュギ・ワ・ジオンゴの批評書（James Currey刊、1986）。「英語による別れ」を宣言し、以降ギクユ語で創作する旨を表明した4本の論文（言語・小説・劇・批評）からなる。アフリカ文学の真正性は媒体言語に宿るという母語優位論を理論化し、20世紀後半最も影響力ある脱植民地批評書の一つとなった。",
    "background": "1977年戯曲『Ngaahika Ndeenda』（私が望むときに結婚する）のギクユ語上演と投獄（1977-78）が起点。",
    "development": "母語文学運動・先住民言語復興運動の理論的基礎となった。",
    "historical_context": "C23『精神の脱植民地化』エントリと別観点（書物としての受容・運動論的位置）から扱う。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Decolonising_the_Mind",
    "primary_source_type": "Wikipedia / James Currey 1986",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「精神の言語」の主権を問う議論は、AI時代の母語LLM・言語覇権論争に直接的影響を与える。",
         "related_ai_phenomenon": "LLMの母語性・言語覇権"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "媒体言語と作品の真正性を結びつけた議論は、AI生成と「本物の声」の関係性議論に接続する。",
         "related_ai_phenomenon": "AI生成と真正性"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "decolonial philosophy of language",
         "description": "脱植民地言語哲学の起点的著作。"},
        {"target_db": "AI-Development", "link_type": "shared_concept",
         "target_entity_name": "low-resource language LLM",
         "description": "母語LLM研究の倫理的基礎文献として参照可能。"},
    ],
})

add({
    "name_ja": "ンギュギ・ギクユ語創作",
    "name_en": "Ngũgĩ's Gikuyu writing",
    "name_original": "Caitaani Mũtharaba-Inĩ",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "ンギュギが英語からギクユ語へ完全移行した1977年以降の創作活動。獄中執筆の長編『Caitaani Mũtharaba-Inĩ』（『十字架の悪魔』1980）はトイレットペーパーに書かれた獄中ノートから生まれ、アフリカ現代語による主要長編小説の先駆例となった。続く『Mũrogi wa Kagogo』（『カラスの魔術師』2006）は最大級のアフリカ現代語長編。",
    "background": "母語小説の市場と読者を実地で開拓した。",
    "development": "他のアフリカ作家による母語創作復興の参照点となった。",
    "historical_context": "アフリカ現代語文学の制度的可能性を実証した転換点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Devil_on_the_Cross",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "現代語によるアフリカ長編小説の制度的可能性を実証した。AI時代の低資源言語生成の可能性議論と接続。",
         "related_ai_phenomenon": "低資源言語AI生成"},
    ],
})

add({
    "name_ja": "オコト・ピテック『ラウィノの歌』",
    "name_en": "Song of Lawino (Okot p'Bitek)",
    "name_original": "Wer pa Lawino / Song of Lawino",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "ウガンダ人作家オコト・ピテック（1931-1982）の長編詩（アチョリ語1969、英訳1966）。アフリカ伝統の妻ラウィノが、西欧化した夫オチョルと現代的な愛人クララを批判する独白詩。アチョリ族口承詩形式（otole, bwola等）を踏まえつつ、独立後アフリカの文化的疎外・知識人エリートの自己疎外を批判した東アフリカ最重要詩作品。",
    "background": "クェント・グロウブのアフリカ詩シリーズで世界的に普及した。",
    "development": "続編『オチョルの歌』（1970）と対をなす。",
    "historical_context": "アチョリ語原典と英訳の併存はアフリカ口承詩テクスト化の代表例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Song_of_Lawino",
    "primary_source_type": "Wikipedia / EAEP 1969",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "アチョリ語と英訳の二重編成は、原典・翻訳の二項を超えるテクスト形式を提示。",
         "related_ai_phenomenon": "AI翻訳における原典の自己生成"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "oral epic poetics",
         "description": "口承叙事詩学のアフリカ的展開。"},
    ],
})

add({
    "name_ja": "ヌルディン・ファラー",
    "name_en": "Nuruddin Farah",
    "name_original": "Nuruddin Farah",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "ソマリア人作家（1945-）。デビュー作『From a Crooked Rib』（1970）は史上最初の英語ソマリア長編小説の一つ。三部作シリーズ（『Sweet and Sour Milk』『Sardines』『Close Sesame』、『Maps』『Gifts』『Secrets』、『Links』『Knots』『Crossbones』）でシアド・バーレ独裁・内戦・離散を描き続けた。2008年には自国へ40年ぶりに戻り内戦下のモガディシュを記録。",
    "background": "ソマリア体制批判で長期亡命、ナイジェリア・米・ケープタウン等で執筆した。",
    "development": "アフリカ亡命作家文学の代表的存在となった。",
    "historical_context": "ノーベル文学賞候補として継続して言及される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nuruddin_Farah",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "タンザニア・スワヒリ語文学",
    "name_en": "Tanzanian Kiswahili literature",
    "name_original": "fasihi ya Kiswahili Tanzania",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "タンザニアにおけるスワヒリ語文学の独立後展開。シャアバン・ロバートの古典詩と物語、エブラヒム・フセインの戯曲『Kinjeketele』（1969、マジマジ蜂起を扱う）、ペネナ・ムフムブシの詩、エフライム・キェジル等が国民言語スワヒリ語を文学言語として確立した。ニェレレ大統領のシェイクスピア翻訳『ジュリアス・シーザー』『ヴェニスの商人』もこの動向の一環。",
    "background": "1967年アルーシャ宣言以降、スワヒリ語が国民統合の核となった。",
    "development": "ケニア・ウガンダ・コンゴ東部のスワヒリ語圏に波及した。",
    "historical_context": "アフリカで現代語が国民文学の媒体となった最大級の成功例。",
    "primary_source_url": "https://www.ajol.info/index.php/kiswahili",
    "primary_source_type": "AJOL — Kiswahili",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "現代語が国民文学の媒体として機能した代表事例。",
         "related_ai_phenomenon": "現代語LLM・国民言語AI"},
    ],
})

add({
    "name_ja": "ユーセフ・イドリース",
    "name_en": "Yusuf Idris",
    "name_original": "يوسف إدريس",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "エジプト人短編作家・劇作家（1927-1991）。アラビア語短編小説の現代的形式を確立した「エジプトのチェーホフ」と称される作家。短編集『最も安価な夜』（1954）等で農村庶民の生活・性・社会批判を口語アラビア語で描いた。戯曲『Al-Farafir』（1964）はエジプト民衆芸能を取り入れた政治演劇の代表作。北アフリカ・近代アラブ文学のアフリカ的拠点。",
    "background": "医師として農村医療を経験、それが文学の基礎となった。",
    "development": "ナギーブ・マフフーズと並ぶ20世紀エジプト文学双璧として位置づけられる。",
    "historical_context": "C21（アラブ古典詩学）に対し、北アフリカの近現代散文として補完。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Yusuf_Idris",
    "primary_source_type": "Wikipedia / AUC Press",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ハーリド・アル＝ホサイニー",
    "name_en": "Khalid el Hossainy / Khaled Hosseini commentary",
    "name_original": "خالد الحسيني / Egyptian-Sudanese reception",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "アラブ系アフリカ文学の現代詩・批評を代表する潮流の一翼。エジプト・スーダン・モロッコ系作家による20世紀後半詩の動向を指す。スーダン人タイブ・サーリフ『北へ移住する季節』（1966）、モロッコ系ターハル・ベン・ジェルーン、エジプト人現代詩人サラーフ・アブドゥッ＝サブール等が、アラブ語と仏語・英語のあいだで多言語的アフリカ・アラブ文学を展開した。",
    "background": "アラブ・ナショナリズムと脱植民地化の交差点で形成された。",
    "development": "Banipal等の翻訳誌を通じ世界文学に接続している。",
    "historical_context": "C21（アラブ古典）+C24（現代北アフリカ）の橋渡し領域。",
    "primary_source_url": "https://www.banipal.co.uk/",
    "primary_source_type": "Banipal magazine",
    "importance_score": 3, "source_tier": "tertiary", "canonical_in_region": "minor",
})

add({
    "name_ja": "ルワンダ・ブルンジ後ジェノサイド文学",
    "name_en": "Rwandan / Burundian post-genocide literature",
    "name_original": "littérature post-génocide rwandaise et burundaise",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "1994年ルワンダジェノサイドおよびブルンジ内戦（1993-2005）以降に展開した東アフリカ大湖地域文学。スコラスティーク・ムカソンガ『Notre-Dame du Nil』（2012、ルノドー賞）、ガエル・ファイ『Petit Pays』（2016）、ジャン・アヤンウィエ・ニズリゾ等が、トラウマ・記憶・赦し・離散を主題化。Fest'Africa主導の「死に抗して書く」共同プロジェクト（1998-2000）が国際的注目を集めた。",
    "background": "歴史的暴力の文学的応答の代表事例として位置づけられる。",
    "development": "ジェノサイド後20年以降、第二世代作家が記憶の脱植民地化を進めている。",
    "historical_context": "21世紀アフリカ文学のトラウマ表象の極点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sc%C3%B4lastique_Mukasonga",
    "primary_source_type": "Wikipedia / Gallimard",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "ジェノサイド経験は線形的物語化を不可能にし、断片・沈黙・証言形式を要請する。",
         "related_ai_phenomenon": "AI生成のトラウマ表象限界"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "誰が誰の苦しみを書く権利を持つかという真正性問題を究極的に提起する。",
         "related_ai_phenomenon": "AI生成と証言の真正性"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "violence anthropology",
         "description": "暴力の人類学・トラウマ民族誌と接続。"},
    ],
})


# ===============================================================
# C. 南アフリカ (8)
# ===============================================================

add({
    "name_ja": "クッツェー『恥辱』",
    "name_en": "Disgrace (Coetzee)",
    "name_original": "Disgrace",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "南アフリカ人作家J.M.クッツェー（J.M. Coetzee, 1940-）の長編小説（1999、Booker Prize受賞）。性的不品行で大学教授職を失ったデイヴィッド・ルーリーが、田舎で農場を営む娘ルーシーを訪れ、黒人襲撃と性暴力を経験する物語。ポストアパルトヘイト南アフリカの政治的＝倫理的緊張を、加害者性・被害者性・贖罪不能性として描いた21世紀世界文学の傑作。",
    "background": "1999年Bookerと2003年ノーベル文学賞の中心作とされる。",
    "development": "ポストアパルトヘイト文学の倫理的読解の試金石となった。",
    "historical_context": "南アフリカ真実和解委員会後の文学的応答として位置づけられる。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Disgrace",
    "primary_source_type": "Wikipedia / Secker & Warburg 1999",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体性", "status": "rethinking",
         "rationale": "加害者の道徳的破綻と、被害を引き受ける娘の選択は、自由主義的主体概念を解体する。",
         "related_ai_phenomenon": "AI倫理における主体性の限界"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ethics of recognition",
         "description": "承認の倫理学の文学的展開。"},
    ],
})

add({
    "name_ja": "クッツェー『野蛮人を待ちながら』",
    "name_en": "Waiting for the Barbarians (Coetzee)",
    "name_original": "Waiting for the Barbarians",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "クッツェーの長編小説（1980）。架空の帝国の辺境で「野蛮人」を取り調べる治安官ジョルとそれに抗する治安判事の対立を描く政治寓話。コンスタンティノス・カヴァフィスの同名詩を題に取り、植民地暴力一般の構造を抽象化して提示した。アパルトヘイトを直接描かず寓話化することで国際的普遍性を獲得した最初期の代表作。",
    "background": "1980年代初頭のアパルトヘイト末期の知的良心の象徴となった。",
    "development": "クッツェー寓話手法の典型例として参照され続ける。",
    "historical_context": "クッツェー初期小説の頂点として2003年ノーベル賞理由に挙げられた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Waiting_for_the_Barbarians",
    "primary_source_type": "Wikipedia / Secker & Warburg 1980",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ナディン・ゴーディマー",
    "name_en": "Nadine Gordimer",
    "name_original": "Nadine Gordimer",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "南アフリカ人作家（1923-2014）、1991年ノーベル文学賞。アパルトヘイト体制下のヨハネスブルク白人リベラル知識人の倫理的緊張を主題に、『The Conservationist』（1974、Booker Prize）、『Burger's Daughter』（1979、当局発禁）、『July's People』（1981）等を発表。ANCに加入し政治活動家としても活動、検閲・発禁を繰り返し受けた。",
    "background": "ハイヴェルト出版社・グリーンブック等から短編作家として始まった。",
    "development": "アフリカ女性ノーベル賞作家としてアミーリア・サキら次世代を励ました。",
    "historical_context": "アパルトヘイト時代の白人良心文学を代表する。",
    "primary_source_url": "https://www.nobelprize.org/prizes/literature/1991/gordimer/biographical/",
    "primary_source_type": "Nobel Prize official",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "アンドレ・ブリンク",
    "name_en": "André Brink",
    "name_original": "André Brink",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "南アフリカ人アフリカーンス語・英語作家（1935-2015）。1973年『Looking on Darkness』はアフリカーンス語小説として初めてアパルトヘイト体制から発禁された。『A Dry White Season』（1979）、『A Chain of Voices』（1982）等で白人アフリカーナーの内側からアパルトヘイト批判を展開。Sestigers運動（1960年代アフリカーンス語近代化運動）の中心人物。",
    "background": "アフリカーンス語文学の自己批判的近代化を主導した。",
    "development": "1979年以降、英語版を自ら執筆する二言語作家として国際的読者を獲得した。",
    "historical_context": "白人アフリカーナーによるアパルトヘイト批判文学の双璧。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Andr%C3%A9_Brink",
    "primary_source_type": "Wikipedia / Random House",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ベシー・ヘッド",
    "name_en": "Bessie Head",
    "name_original": "Bessie Head",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "南アフリカ生まれ・ボツワナ亡命作家（1937-1986）。混血出生の烙印・精神疾患・無国籍状態を抱えつつ、ボツワナのセロウェ村に定住して創作。『When Rain Clouds Gather』（1968）、『Maru』（1971）、『A Question of Power』（1974）の三部作で、人種・ジェンダー・狂気・追放を主題化した。アフリカ女性文学の先駆的存在。",
    "background": "アパルトヘイト下の差別から逃れボツワナで難民として執筆した。",
    "development": "死後ジェンダー批評の中心的研究対象となった。",
    "historical_context": "アフリカン・フェミニスト文学の最初期実践として参照される。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Bessie_Head",
    "primary_source_type": "Wikipedia / Heinemann AWS",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "エスキア・ムパシェレ",
    "name_en": "Es'kia Mphahlele",
    "name_original": "Es'kia Mphahlele",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "南アフリカ人作家・批評家・教育者（1919-2008）。自伝『Down Second Avenue』（1959）はソフィアタウン（プレトリア近郊黒人居住区）の生活を描き、20世紀アフリカ自伝文学の古典となった。Drum誌（1950年代ヨハネスブルク文化誌）の編集者として、トッド・マチケザ、ナット・ナカサら一群のソフィアタウン作家を育成。亡命中のアフリカ各国・米国でアフリカ文学批評の制度化に貢献した。",
    "background": "ソフィアタウン文学運動とDrum誌は黒人都市文化の文学的記録として歴史的価値を持つ。",
    "development": "1977年帰国後、南アフリカで初めてアフリカ文学講座を大学に開設した。",
    "historical_context": "南アフリカ黒人文学の制度的基盤を築いた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Es%27kia_Mphahlele",
    "primary_source_type": "Wikipedia / Faber & Faber",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "アソル・フガード演劇",
    "name_en": "Athol Fugard theatre",
    "name_original": "Athol Fugard theatre",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "南アフリカ人劇作家（1932-）。Serpent Players（1963年ニューブライトン創設の黒人劇団）と協働し、ジョン・カーニ、ウィンストン・ンショナとの共同創作で『Sizwe Banzi Is Dead』（1972）、『The Island』（1973）等を生んだ。アパルトヘイト下の通行証法・ロベン島囚人を描き、世界中でツアー上演された。アフリカ抵抗演劇の世界的代表。",
    "background": "アパルトヘイト体制下、合法的な黒人劇団との共同創作で検閲を回避した。",
    "development": "『Master Harold...and the Boys』（1982）等で世界劇場のレパートリーに入った。",
    "historical_context": "南アフリカ証言演劇（testimonial theatre）の起点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Athol_Fugard",
    "primary_source_type": "Wikipedia / Oxford UP",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ポストアパルトヘイト文学",
    "name_en": "post-apartheid literature",
    "name_original": "post-apartheid literature",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "1994年民主化以降の南アフリカ文学の総体。クッツェー『恥辱』（1999）、ザケス・ムダ『Ways of Dying』（1995）、フリン・ファン・ニーケルク『Triomf』（1994）、イヴァン・ヴラディスラヴィッチ、ニアサ・ムベラ、コペーノ・マトロワ・コルワネ等が、真実和解委員会・経済格差・新しい暴力・記憶整理を主題化。アフリカーンス語・英語・ズールー語・コーサ語等の多言語性が顕在化。",
    "background": "アパルトヘイト終結後のトラウマと希望が文学的応答を要請した。",
    "development": "21世紀には黒人女性作家の台頭が顕著となった。",
    "historical_context": "国民和解と歴史記憶の文学的整理を担った。",
    "primary_source_url": "https://www.ajol.info/index.php/jls",
    "primary_source_type": "AJOL — Journal of Literary Studies",
    "importance_score": 5, "source_tier": "secondary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体性", "status": "rethinking",
         "rationale": "加害・被害の境界を再構成する作業は、近代主体概念の前提を問い直す。",
         "related_ai_phenomenon": "AI時代の主体・被害概念"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "TRC証言と文学的虚構の境界が流動化し、誰が真実を語るかが再定義された。",
         "related_ai_phenomenon": "AI生成と証言の真正性"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "transitional justice",
         "description": "移行期正義の人類学的研究と接続。"},
    ],
})


# ===============================================================
# D. フランコフォン・ルゾフォン (8)
# ===============================================================

add({
    "name_ja": "シェイク・ハミドゥ・カン『曖昧な冒険』",
    "name_en": "L'Aventure ambiguë (Cheikh Hamidou Kane)",
    "name_original": "L'Aventure ambiguë",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "セネガル人作家シェイク・ハミドゥ・カン（1928-）の長編小説（1961、Grand Prix littéraire d'Afrique noire）。フラニ族イスラーム貴族の青年サンバ・ジャロが、コーラン学校で学んだ後、フランス哲学留学で西欧知の根源的問いに直面し、帰国後狂気と死へ至る物語。アフリカ・イスラーム的世界観と西欧世俗近代の出会いの哲学的悲劇として書かれた仏語圏アフリカ古典。",
    "background": "カン自身のフラニ族＝ソルボンヌ留学経験を踏まえている。",
    "development": "アフリカ哲学小説の代表として参照され続ける。",
    "historical_context": "イスラーム的アフリカ文学の現代的代表作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/L%27Aventure_ambigu%C3%AB",
    "primary_source_type": "Wikipedia / Julliard",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体性", "status": "rethinking",
         "rationale": "二重の知の伝統を生きる主体の不可能性を哲学的に展開した。",
         "related_ai_phenomenon": "AI時代の文化的主体性の重層性"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Islamic philosophy in Africa",
         "description": "アフリカ・イスラーム哲学と直結。"},
    ],
})

add({
    "name_ja": "マリアマ・バー『かくも長き手紙』",
    "name_en": "Une si longue lettre (Mariama Bâ)",
    "name_original": "Une si longue lettre",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "セネガル人作家マリアマ・バー（1929-1981）の書簡体小説（1979、Noma Award受賞）。一夫多妻制セネガルでの夫の若い後妻迎入れを契機に、寡婦ラマトゥラエが親友アイサトゥへ40日間の追悼期に書く長い手紙の形式。イスラーム・伝統・近代女性の選択を内側から論じた、仏語圏アフリカ女性文学の最重要作品。",
    "background": "セネガル女性教師としての経験を踏まえている。",
    "development": "アフリカ・フェミニスト文学の必読古典となった。",
    "historical_context": "1981年バー逝去で遺作となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/So_Long_a_Letter",
    "primary_source_type": "Wikipedia / Nouvelles Éditions Africaines",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
})

add({
    "name_ja": "サンゴール後期",
    "name_en": "Léopold Senghor's later work",
    "name_original": "Léopold Sédar Senghor — Œuvre tardive",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "セネガル初代大統領（1960-1980）レオポール・セダール・サンゴール（1906-2001）の独立後の文学・思想活動。詩集『Nocturnes』（1961）、『Lettres d'hivernage』（1973）等で、ネグリチュードを「文明の対話と贈与」として再定義し、フランコフォニー国際組織の理論的基盤を提示した。1983年アフリカ人初のアカデミー・フランセーズ会員選出。",
    "background": "C23では1930年代ネグリチュード成立を扱い、本項では戦後・大統領期の理論的成熟を扱う。",
    "development": "ネグリチュード後期理論はアフリカ・カリブ・ラテン批評で批判と継承を生んだ。",
    "historical_context": "詩人＝政治家の世界的代表事例として記憶される。",
    "primary_source_url": "https://www.academie-francaise.fr/les-immortels/leopold-sedar-senghor",
    "primary_source_type": "Académie française official",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "センベーヌ・ウスマン『神々の森の人々』",
    "name_en": "Les bouts de bois de Dieu (Sembène Ousmane)",
    "name_original": "Les bouts de bois de Dieu",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "セネガル人作家・映画監督センベーヌ・ウスマン（1923-2007）の長編小説（1960、邦題『神の森の小枝』）。1947-48年ダカール＝ニジェール鉄道スト（実際の歴史事象）を題材に、女性たちが闘争の中心となり政治的主体に成長する過程を描く。フランコフォン・アフリカ社会主義文学の最重要作。後にセンベーヌは映画『チャドの若い娘』『マンダビ』等でアフリカ映画の父と呼ばれた。",
    "background": "センベーヌ自身が鉄道港湾労働者・組合活動家であった経験を踏まえる。",
    "development": "アフリカ映画の祖としても並行的に重要視される。",
    "historical_context": "労働運動文学・女性運動文学の交差点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/God%27s_Bits_of_Wood",
    "primary_source_type": "Wikipedia / Le Livre Contemporain",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "媒体", "status": "rethinking",
         "rationale": "小説と映画を等価に往還する作家像は、AI時代の媒体横断的創作と構造的に共鳴する。",
         "related_ai_phenomenon": "マルチモーダル創作"},
    ],
})

add({
    "name_ja": "モンゴ・ベティ",
    "name_en": "Mongo Beti",
    "name_original": "Mongo Beti",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後初期",
    "definition": "カメルーン人作家（本名Alexandre Biyidi-Awala, 1932-2001）。デビュー作『Le pauvre Christ de Bomba』（1956、邦題『ボンバの貧しいキリスト』）でフランス領カメルーンのカトリックミッションを諷刺、フランス当局の検閲を受けた。長期亡命中のフランスから『Main basse sur le Cameroun』（1972、即発禁）等で独立後カメルーン体制を批判し続けた。",
    "background": "アヤン・カナイ独立闘争を支持し、独立後アフマドゥ・アヒジョ独裁を批判した。",
    "development": "1991年帰国後ヤウンデで政治活動・出版社経営を行った。",
    "historical_context": "アフリカ・パンフレッティスト文学の代表。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mongo_Beti",
    "primary_source_type": "Wikipedia / Robert Laffont",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ターハル・ベン・ジェルーン",
    "name_en": "Tahar Ben Jelloun",
    "name_original": "Tahar Ben Jelloun / طاهر بن جلون",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "モロッコ人仏語作家（1944-）。『L'Enfant de sable』（1985）と続編『La Nuit sacrée』（1987、ゴンクール賞）で、女性として育てられねばならなかった八番目の娘ザフラ／アフメドの両性具有的物語を、マグレブ口承伝統と仏語近代散文を融合させて描いた。北アフリカ仏語文学の世界的代表。フランス語圏アカデミー会員。",
    "background": "1971年仏留学後パリ定住、北アフリカ移民社会の代弁者となった。",
    "development": "『Cette aveuglante absence de lumière』（2001、IMPAC賞）等でモロッコ「鉛の年代」を告発した。",
    "historical_context": "マグレブ仏語文学の制度的中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tahar_Ben_Jelloun",
    "primary_source_type": "Wikipedia / Seuil",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "アラビア語的口承を仏語散文に転写する二重性は、AI翻訳・コードスイッチ生成の予型。",
         "related_ai_phenomenon": "AI多言語コードスイッチ"},
    ],
})

add({
    "name_ja": "アグアルーザ",
    "name_en": "José Eduardo Agualusa",
    "name_original": "José Eduardo Agualusa",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "アンゴラ人ポルトガル語作家（1960-）。『O Vendedor de Passados』（過去の売人、2004、Independent Foreign Fiction Prize）で、ポルトガル独立後の記憶捏造ビジネスを描いた。『Teoria geral do esquecimento』（忘却の一般理論、2012、IMPAC Dublin Award）はルアンダ独立期の白人女性が30年間自宅に立てこもる物語。ルゾフォン・アフリカ文学の世界的代表。",
    "background": "アンゴラ・ブラジル・ポルトガルの三国を往還する作家像で知られる。",
    "development": "ミア・コウトと共にルゾフォン・アフリカ文学を国際化した。",
    "historical_context": "ポストコロニアル記憶・国家形成の主題化を21世紀的視点で展開した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Jos%C3%A9_Eduardo_Agualusa",
    "primary_source_type": "Wikipedia / Quetzal Editores",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ミア・コウト",
    "name_en": "Mia Couto",
    "name_original": "Mia Couto",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "モザンビーク人ポルトガル語作家（本名António Emílio Leite Couto, 1955-）。『Terra Sonâmbula』（夢遊する大地、1992、20世紀アフリカ最重要小説12選）でモザンビーク内戦（1977-92）を魔術的写実主義で描き、世界文学に登場。ポルトガル語にバントゥ系語彙・口承形式・新造語を大量導入し、独自の「コウト語」を樹立した。2013年カモンイス賞、2014年Neustadt国際文学賞。",
    "background": "生物学者としても活動し、自然と神話の交差を主題化した。",
    "development": "ルゾフォン・アフリカ文学を世界的に確立した中核作家。",
    "historical_context": "21世紀アフリカ文学の言語実験の極点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mia_Couto",
    "primary_source_type": "Wikipedia / Caminho",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "ポルトガル語の組織的変形・新造語生成は、AI生成における言語創発と構造的に類比される。",
         "related_ai_phenomenon": "LLM言語創発・新語生成"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "魔術的写実主義のアフリカ的展開は、AI生成における幻想と事実の境界の流動性議論と接続。",
         "related_ai_phenomenon": "AI生成における幻想／事実"},
    ],
    "cross_domain": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "neologistic poetics",
         "description": "新造語詩学の現代的展開として直結。"},
    ],
})


# ===============================================================
# E. 21世紀・現代 (8)
# ===============================================================

add({
    "name_ja": "アディーチェ『半分のぼった黄色い太陽』",
    "name_en": "Half of a Yellow Sun (Adichie)",
    "name_original": "Half of a Yellow Sun",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "ナイジェリア人作家チママンダ・ンゴズィ・アディーチェ（1977-）の長編小説（2006、Orange Prize for Fiction）。ビアフラ戦争（1967-70）を中心に、知識人カイネネと姉オランナ、双子姉妹の英国人恋人リチャード、家事使用人の少年ウグウの視点から描いた多声的歴史小説。21世紀アフリカ文学の世界的成功例の象徴的作品。",
    "background": "アディーチェ自身の家系がビアフラ戦争を体験した。",
    "development": "アフロポリタン世代（21世紀ディアスポラ作家）の象徴的作家として国際的認知を得た。",
    "historical_context": "歴史トラウマの文学的整理として21世紀アフリカ文学の到達点の一つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Half_of_a_Yellow_Sun",
    "primary_source_type": "Wikipedia / Knopf",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "歴史的トラウマを多声的・断片的に再構成する形式は、線形的歴史物語論を解体する。",
         "related_ai_phenomenon": "AI生成における多声的歴史"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "戦争を直接体験しない世代が記憶を担う倫理的位置づけは、AI生成における証言と真正性問題に直結する。",
         "related_ai_phenomenon": "AI生成と歴史的記憶"},
    ],
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "memory anthropology",
         "description": "記憶人類学のポストコロニアル展開。"},
    ],
})

add({
    "name_ja": "アディーチェ『アメリカーナ』",
    "name_en": "Americanah (Adichie)",
    "name_original": "Americanah",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "アディーチェの長編小説（2013、National Book Critics Circle Award）。ナイジェリア人女性イフェメルが米国留学・ブログ運営・帰国を経て恋人オビンゼと再会する物語を通じて、米国における人種・髪・移民・恋愛を体系的に分析した21世紀ディアスポラ小説の代表作。「アメリカーナ」とはナイジェリア帰国組への揶揄的呼称。",
    "background": "アディーチェ自身の米国留学・帰国体験を踏まえる。",
    "development": "ブログ形式の挿入は21世紀メディア状況を文学化した先駆例。",
    "historical_context": "アフロポリタン文学の世界的ベストセラー化を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Americanah",
    "primary_source_type": "Wikipedia / Knopf",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "媒体", "status": "rethinking",
         "rationale": "ブログ・SNS・小説の境界を作品内部で問い直し、デジタル媒体と文学の関係を再定義した。",
         "related_ai_phenomenon": "ソーシャル生成・AI生成テクスト"},
    ],
})

add({
    "name_ja": "テジュ・コール『オープン・シティ』",
    "name_en": "Open City (Teju Cole)",
    "name_original": "Open City",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "ナイジェリア系米国人作家テジュ・コール（1975-）の長編小説（2011、Hemingway Foundation/PEN Award）。9.11後のニューヨークを精神科レジデントの主人公ジュリウスが歩き、過去・現在・移民・歴史・暴力を瞑想する徒歩散文。W.G.ゼーバルトとV.S.ナイポールの伝統を継ぎ、21世紀ポストコロニアル都市文学の代表作。",
    "background": "コロンビア大学博士課程で美術史を専攻、同時期に執筆された。",
    "development": "ポスト9.11時代のディアスポラ的内面の代表的描出として国際評価を得た。",
    "historical_context": "21世紀ディアスポラ意識の文学的内省の代表例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Open_City_(novel)",
    "primary_source_type": "Wikipedia / Random House",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ヘロン・ハビラ",
    "name_en": "Helon Habila",
    "name_original": "Helon Habila",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "ナイジェリア人作家（1967-）。ジャーナリスト出身、デビュー作『Waiting for an Angel』（2002、Caine Prize）でナイジェリア軍政期投獄を描き、続く『Measuring Time』（2007）、『Oil on Water』（2010）でニジェール・デルタ石油汚染を主題化した。Caine Prize受賞後最初の世代を代表する21世紀ナイジェリア小説家の一人。",
    "background": "Caine Prize受賞作家として国際進出した。",
    "development": "ジョージ・メイソン大学教授として米国に拠点を持つ。",
    "historical_context": "21世紀ナイジェリア文学の制度的成熟を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Helon_Habila",
    "primary_source_type": "Wikipedia / Norton",
    "importance_score": 3, "source_tier": "secondary", "canonical_in_region": "minor",
})

add({
    "name_ja": "マーザ・メンギステ",
    "name_en": "Maaza Mengiste",
    "name_original": "Maaza Mengiste",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "エチオピア系米国人作家（1971-）。デビュー作『Beneath the Lion's Gaze』（2010）でエチオピア革命（1974）を描き、続く『The Shadow King』（2019、Booker Prize最終候補）はムッソリーニのエチオピア侵攻（1935-41）に抵抗するエチオピア女性兵士たちを描いた。アフリカ・ディアスポラ女性作家の代表的存在。",
    "background": "エチオピア・ナイジェリア・ケニアを経て米国移住の経験を踏まえる。",
    "development": "Project 3541としてエチオピア侵攻期の写真アーカイブも展開している。",
    "historical_context": "アフリカ歴史の女性視点からの再記述を代表する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Maaza_Mengiste",
    "primary_source_type": "Wikipedia / W.W. Norton",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ノヴァイオレット・ブラワヨ",
    "name_en": "NoViolet Bulawayo",
    "name_original": "NoViolet Bulawayo",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "ジンバブエ人作家（本名Elizabeth Zandile Tshele, 1981-）。デビュー作『We Need New Names』（2013、Booker Prize最終候補、史上初のアフリカ人女性最終候補）でジンバブエの少女ダーリングが米国移住する物語を11歳の声で描いた。第二作『Glory』（2022、Booker Prize最終候補）はジョージ・オーウェル『動物農場』を踏まえたムガベ末期ジンバブエの政治寓話。",
    "background": "コーネル大学・スタンフォード大学を経て米国で執筆活動。",
    "development": "アフリカ系女性作家のBooker最終候補化の象徴的存在。",
    "historical_context": "21世紀ジンバブエ文学のグローバル接続を代表する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/NoViolet_Bulawayo",
    "primary_source_type": "Wikipedia / Reagan Arthur Books",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "イヴォン・アディアンボ・オウォル",
    "name_en": "Yvonne Adhiambo Owuor",
    "name_original": "Yvonne Adhiambo Owuor",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "21世紀アフリカ文学",
    "definition": "ケニア人作家（1968-）。短編「Weight of Whispers」（2003）でCaine Prize受賞、長編『Dust』（2014）はケニア独立闘争・マウマウ・ジョモ・ケニヤッタ暗殺・2007年選挙暴動を多世代家族史として詩的散文で描き、21世紀ケニア小説の最重要作とされた。続く『The Dragonfly Sea』（2019）はインド洋・スワヒリ海岸文化を舞台に、アフリカ・アジア横断のグローバル史を描く。",
    "background": "クォーク映画祭ディレクター・カラム・ナワーフィッ財団役員等の文化的役割も担った。",
    "development": "ケニア新世代の代表的女性作家として位置づけられる。",
    "historical_context": "21世紀東アフリカ文学の頂点の一つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Yvonne_Adhiambo_Owuor",
    "primary_source_type": "Wikipedia / Knopf",
    "importance_score": 4, "source_tier": "secondary", "canonical_in_region": "major",
})

add({
    "name_ja": "ダンガレンガ『ナーバス・コンディション』",
    "name_en": "Nervous Conditions (Tsitsi Dangarembga)",
    "name_original": "Nervous Conditions",
    "original_script": "roman",
    "subfield_code": SUBFIELD, "region": REGION,
    "period_key": "独立後中期",
    "definition": "ジンバブエ人作家・映画監督ツィッツィ・ダンガレンガ（1959-）の長編小説（1988、Commonwealth Writers' Prize、Africa Region）。ローデシア独立闘争期、村の少女タンブの教育機会獲得と、英国留学帰国の従姉ニャシャの「神経症的状態」を二重視点で描く。題はファノン『地に呪われたる者』のサルトル序文「植民地化の状況は神経症的状況である」から。アフリカ・フェミニスト文学の世界的古典。",
    "background": "ローデシア＝ジンバブエ独立（1980）の女性視点の文学的整理。",
    "development": "三部作『The Book of Not』（2006）、『This Mournable Body』（2018、Booker最終候補）に拡張された。",
    "historical_context": "ファノン精神医学とアフリカ・フェミニズムの交差点的代表作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nervous_Conditions",
    "primary_source_type": "Wikipedia / Women's Press",
    "importance_score": 5, "source_tier": "primary", "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体性", "status": "rethinking",
         "rationale": "植民地的教育による主体形成の二重性（解放と同時の自己疎外）を理論化した。",
         "related_ai_phenomenon": "AI教育・主体形成"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "「神経症的状態」概念は誰がどう読むかで意味が変わる多義性を持つ。",
         "related_ai_phenomenon": "AI生成の多義的受容"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "Fanon's psychiatry",
         "description": "ファノン植民地精神医学の文学的応答。"},
    ],
})


# ---------------------------------------------------------------
# Insertion driver
# ---------------------------------------------------------------

def main() -> int:
    print(f"[c24] {len(CONCEPTS)} concepts queued for insertion")
    inserted = 0
    skipped = 0
    failed = 0
    fourth_count = 0
    cross_count = 0

    with LitDB() as db:
        # seed periods (idempotent; reuses C23 ones if already seeded)
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

    print(f"\n[c24] inserted={inserted} skipped={skipped} failed={failed}")
    print(f"[c24] fourth_transform_tags={fourth_count} cross_domain={cross_count}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
