"""
LIT-DB Phase 2 — C20 Wave6: Indian Modern & Contemporary Literature
====================================================================
近現代インド諸言語文学（ベンガル・ヒンディー・ウルドゥー・南インド諸言語・英印・主題運動）

Inserts 40 representative concepts spanning 5 categories:
  A. ベンガル・ルネサンスとタゴール (8)
  B. ヒンディー・ウルドゥー文学 (8)
  C. 南インド諸言語文学 (8)
  D. 英印文学（Indo-Anglian） (8)
  E. 主要主題と運動 (8)

subfield_id=12, code='lit_india', region='南西アジア'

Sources: Sahitya Akademi, JSTOR, Murty Classical Library of India,
Encyclopaedia Britannica, Wikipedia (canonical biographical/work entries),
Project Gutenberg public domain editions, Internet Archive.

C19 (古典) との重複を避け、具体的な作品・人物を中心に近現代を担当。
"""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (C19の近代/現代期と整合)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("インド近代期", "Modern Indian", 1800, 1947,
     "ベンガル・ルネサンス、タゴール、プレームチャンドらによる諸言語文学の近代化。"),
    ("現代インド期", "Contemporary Indian", 1947, 2025,
     "独立後のダリット文学・英印文学・タミル現代文学等の多言語的展開。"),
    ("インド分離独立期", "Indian Partition", 1940, 1960,
     "1947年印パ分離独立とその文学的余波。マントー、ファイズらが直接体験を作品化。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — ベンガル・ルネサンスとタゴール (8)
# ===============================================================

add({
    "name_ja": "ブラフモ・サマージ運動",
    "name_en": "Brahmo Samaj movement",
    "name_original": "ব্রাহ্ম সমাজ",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "1828年ラーム・モーハン・ローイがカルカッタで創設した一神教的ヒンドゥー改革運動。ヴェーダーンタ普遍主義とキリスト教啓蒙合理主義の融合により偶像崇拝・サティー（寡婦殉死）を批判し、ベンガル知識人の文学的近代化の思想的基盤を提供した。タゴール家三代もこの運動の中核を担った。",
    "background": "東インド会社統治下のカルカッタにおける英語教育とヒンドゥー伝統批判の緊張のなかで成立した。",
    "development": "デヴェンドラナト・タゴール、ケーシャブ・チャンドラ・センを経てロビンドロナトに至るベンガル文学的近代の精神的源流となった。",
    "historical_context": "アジア最初の宗教的近代化運動として位置づけられる。",
    "primary_source_url": "https://www.britannica.com/topic/Brahmo-Samaj",
    "primary_source_type": "Encyclopaedia Britannica",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マイケル・モドゥシュドン・ドット",
    "name_en": "Michael Madhusudan Dutt",
    "name_original": "মাইকেল মধুসূদন দত্ত",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ベンガル近代詩の祖とされる詩人（1824-1873）。キリスト教改宗者で、ベンガル語に無韻詩（amitrakshar chhanda）を導入し、叙事詩『メーグナードボド・カーヴィヨ』（1861）でラーマーヤナの悪役メーグナードを悲劇的英雄として再解釈した。西欧古典主義の翻案によりベンガル詩を近代化した。",
    "background": "ヒンドゥー・カレッジでの英語教育を経てキリスト教改宗、英国留学を経験した境界的知識人。",
    "development": "無韻詩の導入はその後のベンガル詩・タゴールに決定的影響を与えた。",
    "historical_context": "正典の悪役を主人公化する近代的価値転換を達成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Michael_Madhusudan_Dutt",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "バンキム・チャンドラ『アーナンドマト』",
    "name_en": "Bankim Chandra's Anandamath",
    "name_original": "আনন্দমঠ",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "バンキム・チャンドラ・チャットパーディヤイ（1838-1894）の歴史小説（1882）。18世紀ベンガルのサンニャーシ反乱を題材に、母なる祖国（バーラト・マーター）への献身を歌う「ヴァンデー・マータラム」を内包し、後にインド独立運動の精神的賛歌となった。近代インド・ナショナリズム文学の起源。",
    "background": "英領植民地体制下の知的官吏として英語教育を受けつつベンガル散文小説を確立した。",
    "development": "「ヴァンデー・マータラム」はインド独立運動の象徴歌となり、独立後インドの国民歌として制度化された。",
    "historical_context": "宗教文学とナショナリズム文学の接続点を確立した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Anandamath",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "タゴール『ゴーラ』",
    "name_en": "Tagore's Gora",
    "name_original": "গোরা",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ロビンドロナト・タゴールの長編小説（1910）。アイルランド系孤児として生まれながら正統ヒンドゥー・ナショナリストとして育てられた青年ゴーラが、出自の真実を知ることで宗教的・国民的アイデンティティを再考する物語。インド近代の宗教・国民・人間観の根本的問い直しを文学化した。",
    "background": "ベンガル分割（1905）とスワデーシー運動の渦中で、ナショナリズムの限界をタゴールが反省する契機となった。",
    "development": "国民・宗教・カースト・性差別を超える普遍的人間観の文学的提示として現代まで読み継がれる。",
    "historical_context": "アジア・ナショナリズム文学の自己批判的傑作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Gora_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シャラトチャンドラ・チャットパッダエ",
    "name_en": "Sarat Chandra Chattopadhyay",
    "name_original": "শরৎচন্দ্র চট্টোপাধ্যায়",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "20世紀前半最大のベンガル小説家（1876-1938）。『デーヴダース』（1917）、『パリニーター』（1914）、『シュリーカーント』四部作などで、社会的禁忌に苦悩する人間の感情をベンガル中産階級の言語で描いた。映画化を通じて20世紀インド大衆文化に深い影響を与えた。",
    "background": "タゴールの観念的世界に対し、より日常的・感情的な人間像をベンガル語散文に確立した。",
    "development": "『デーヴダース』は20世紀インド映画の最も繰り返された原作の一つとなり、苦悩する恋人の文化的アーキタイプを提供した。",
    "historical_context": "近代インド大衆文学のパイオニア。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sarat_Chandra_Chattopadhyay",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ビブーティブシャン『パテール・パーンチャーリー』",
    "name_en": "Bibhutibhushan's Pather Panchali",
    "name_original": "পথের পাঁচালী",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ビブーティブシャン・ボンドパッダエ（1894-1950）の長編小説（1929）。ベンガル農村のバラモン家庭の貧困と兄妹オプ・ドゥルガーの幼年期を抒情的に描いた。サタジット・レイによる映画化（1955）で世界的に知られるようになり、世界文学の正典に位置づけられる。",
    "background": "農村教師としての著者の実体験が綿密な自然描写と心理描写を可能にした。",
    "development": "サタジット・レイのアプー三部作の原作として、20世紀後半に世界文学・世界映画両方で正典化された。",
    "historical_context": "ベンガル農村の生活誌的写実小説の頂点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Pather_Panchali_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "タゴール散文歌（ロビンドロ・ションギト）",
    "name_en": "Rabindra Sangeet",
    "name_original": "রবীন্দ্রসঙ্গীত",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "タゴールが作詞作曲した約2,200曲の歌曲群。ベンガル音楽伝統（バウル、キールタン、シャストリヤ・サンギート）と西欧音楽様式を融合し、季節・愛・神秘・自然を歌う。インド国歌『ジャナ・ガナ・マナ』とバングラデシュ国歌『アマール・ショナル・バングラ』も含み、ベンガル文化の言葉と音楽の統合を象徴する。",
    "background": "シャーンティニケトン教育実験のなかで詩と音楽の一体性が育まれた。",
    "development": "現代まで世界中のベンガル人コミュニティに歌い継がれる文化的中核。",
    "historical_context": "言葉と音楽を分離させない近代以前の詩学を近代に継承した稀有な伝統。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Rabindra_Sangeet",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シャーンティニケトン",
    "name_en": "Santiniketan",
    "name_original": "শান্তিনিকেতন",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "1901年タゴールがベンガル農村に創設した実験的教育機関で、後にヴィシュヴァ・バーラティ大学（1921）に発展した。自然との一体性・芸術と学問の統合・東西文化の対話を理念とし、近代インド文学・芸術・教育の中核拠点となった。アマルティア・セン、サタジット・レイら多くの知識人を育てた。",
    "background": "西欧式の閉鎖的学校教育への代替として、伝統的アーシュラム教育を近代化する試みであった。",
    "development": "2023年UNESCO世界遺産登録。タゴール思想とインド近代文学的思想の物理的・教育的拠点として継承される。",
    "historical_context": "近代インド文学的思想の制度的核心。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Visva-Bharati_University",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — ヒンディー・ウルドゥー文学 (8)
# ===============================================================

add({
    "name_ja": "プレームチャンド『ゴーダーン』",
    "name_en": "Premchand's Godan",
    "name_original": "गोदान",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "プレームチャンド最後の長編小説（1936）。北インド農村の貧農ホーリーが「ゴーダーン（牛の寄進）」という最後の宗教的義務を果たせないまま死ぬ過程を通じて、植民地期インド農村の高利貸経済・カースト・宗教の構造的暴力を写実的に描いた。近代ヒンディー写実主義の頂点。",
    "background": "ガンディー期インド社会改革運動の限界とロシア社会主義写実主義の影響が結晶した。",
    "development": "近代ヒンディー文学の最高傑作の一つとして、現代まで大学カリキュラムの中核を成す。",
    "historical_context": "南アジア農村社会の構造的問題を文学的に提示した古典。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Godaan",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マハーデーヴィー・ヴァルマー",
    "name_en": "Mahadevi Verma",
    "name_original": "महादेवी वर्मा",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "チャーヤーヴァード「四柱」の唯一の女性詩人（1907-1987）。『ニーハール』『ナーラジャーヤ』『サーンディヤ・ギート』等の詩集で、神秘的恋慕・自然・苦悩の女性的内面を新たな抒情的言語で表現した。「現代のミーラー」と呼ばれ、1982年女性として初めてジュナーンピート賞を受賞した。",
    "background": "高等教育を受けた女性として近代ヒンディー詩の女性的主体性を確立した。",
    "development": "プラヤーグ・マヒラ・ヴィッディヤピート（女子大）創立に貢献し、女性教育・文学の制度化を主導した。",
    "historical_context": "近代インド女性文学の独立した詩的主体の確立者。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mahadevi_Varma",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "スーリヤカーント・トリパーティー・ニラーラー",
    "name_en": "Suryakant Tripathi Nirala",
    "name_original": "सूर्यकांत त्रिपाठी निराला",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "チャーヤーヴァード「四柱」の中核詩人（1896-1961）。『パリマル』『ガーティ』等の詩集と長詩『ラーム・キー・シャクティプージャー』で知られ、伝統的バクティ題材を近代的自由律詩に再構築した。「ニラーラー」（独自）の名のとおり、ヒンディー詩の韻律革命と社会批判詩を主導した。",
    "background": "ベンガル文学（ロビンドロナト）の影響とサンスクリット古典伝統の融合を試みた。",
    "development": "ヒンディー自由詩の確立者として、現代の進歩主義詩・実験主義詩への基盤を提供した。",
    "historical_context": "近代ヒンディー詩の韻律革命の中心人物。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Suryakant_Tripathi_Nirala",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ミルザー・ガーリブ",
    "name_en": "Mirza Ghalib",
    "name_original": "مرزا غالب",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ムガル帝国末期の最大のウルドゥー・ペルシア語詩人（1797-1869）。ガザル・ディーワーン（詩集）でガザル形式を哲学的省察・宗教的懐疑・近代的実存意識へと深化させた。1857年インド大反乱期のデリーを目撃し、ペルシア語書簡集『ダストゥンブー』も残した。現代まで南アジア最も愛唱される詩人。",
    "background": "デリー宮廷詩文化の最終世代として、伝統と崩壊を直接経験した境界的人物。",
    "development": "ガザルの主題を恋愛から実存・哲学・神への懐疑にまで拡大し、近代ウルドゥー詩の規範を確立した。",
    "historical_context": "古典宮廷詩文化と近代の境界における巨人。",
    "primary_source_url": "https://www.britannica.com/biography/Ghalib",
    "primary_source_type": "Encyclopaedia Britannica",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アッラーマ・イクバール『バーンゲ・ダラー』",
    "name_en": "Allama Iqbal's Bang-i-Dara",
    "name_original": "بانگ درا",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "アッラーマ・ムハンマド・イクバール（1877-1938）の最初のウルドゥー語詩集（1924）。「隊商の鈴の音」を意味し、青年期から成熟期までの民族的覚醒を歌う詩を集めた。「サーレー・ジャハーン・セ・アッチャー（インドはあらゆる世界より優れる）」を含み、後に「パキスタンの精神的父」と称される思想家の詩的出発点。",
    "background": "ケンブリッジ・ミュンヘン留学を経て近代西欧哲学とイスラーム神秘主義を融合する独自の詩的・哲学的構想を発展させた。",
    "development": "後の『バーレ・ジブリール』『ザルベ・カリーム』等を経て独立パキスタン構想の精神的基礎を提供した。",
    "historical_context": "南アジア・イスラーム近代主義文学の中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Bang-i-Dara",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サーヒル・ルディヤーンヴィー",
    "name_en": "Sahir Ludhianvi",
    "name_original": "ساحر لدھیانوی",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ウルドゥー進歩主義詩運動の代表詩人・映画作詞家（1921-1980）。詩集『タルキャーン』（1944）はラホールの社会的偽善・戦争・搾取を批判し若者の象徴となった。インド独立後はボリウッド映画作詞家として『プヤーサー』『ハム・ドーノー』等で社会批判を大衆詩・映画歌詞に融合した。",
    "background": "進歩主義作家運動と映画産業を架橋する稀有な詩人として活動した。",
    "development": "ウルドゥー詩を映画歌詞として大衆化し、現代南アジア大衆文化の文学的基盤に貢献した。",
    "historical_context": "進歩主義詩と大衆映画文化の架橋者。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sahir_Ludhianvi",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ファイズ・アフマド・ファイズ",
    "name_en": "Faiz Ahmad Faiz",
    "name_original": "فیض احمد فیض",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "20世紀ウルドゥー進歩主義詩の最大の詩人（1911-1984）。ガザル形式を革命詩・抵抗詩・愛の詩に融合し、『ナクシェ・ファリヤーディー』『ダステ・サバー』等の詩集で南アジア左派文学の中心となった。詩「フム・デーケンゲー（我らは見るだろう）」は今もインド・パキスタン両国の抵抗の歌。1962年レーニン平和賞受賞。",
    "background": "進歩主義作家運動の中核として、英領インド・分離後パキスタン・投獄・亡命を経験した。",
    "development": "現代南アジア政治詩の最大の規範として、両国の社会運動で歌い継がれる。",
    "historical_context": "ウルドゥー古典ガザルの政治化と国際化を達成した詩人。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Faiz_Ahmad_Faiz",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "サアダット・ハサン・マントー『トーバー・テーク・スィン』",
    "name_en": "Saadat Hasan Manto's Toba Tek Singh",
    "name_original": "ٹوبہ ٹیک سنگھ",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド分離独立期",
    "definition": "サアダット・ハサン・マントー（1912-1955）の代表的短編（1955）。1947年インド・パキスタン分離独立時に両国の精神病院間で入院患者を交換するという狂気的実話を題材に、シク教徒老人ビシャン・スィンが両国境界の中間地点で死ぬ場面で結ぶ。分離文学（Partition literature）の最高傑作。",
    "background": "分離独立に伴う100万人規模の死と1500万人規模の強制移動を直接体験したマントーが、誰よりも早く狂気的不条理を文学化した。",
    "development": "分離文学の世界的代表作として、現代まで南アジア研究・トラウマ文学研究の中核テクストとなる。",
    "historical_context": "南アジア最大の歴史的トラウマの文学的記憶装置。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Toba_Tek_Singh",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY C — 南インド諸言語文学 (8)
# ===============================================================

add({
    "name_ja": "スブラマニヤ・バーラティ",
    "name_en": "Subramania Bharati",
    "name_original": "சுப்பிரமணிய பாரதி",
    "original_script": "tamil",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "近代タミル詩の最大の詩人（1882-1921）。「マハーカヴィ・バーラティヤール（偉大なる詩人バーラティ）」と尊称され、革命詩・愛国詩・女性解放詩・宗教詩を融合し、タミル詩を中世的バクティ伝統から近代的自由詩へと転回させた。短命ながらタミル・ナショナリズムと近代化双方の精神的源泉となった。",
    "background": "ヴァーラーナシーで学んだサンスクリット古典伝統と独立運動への参画が独特の詩的世界を生んだ。",
    "development": "現代タミル文学・タミル映画歌謡・タミル・ナショナリズム運動すべての精神的源泉となった。",
    "historical_context": "南インド近代文学の中核的英雄詩人。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Subramania_Bharati",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クヴェンプ",
    "name_en": "Kuvempu",
    "name_original": "ಕುವೆಂಪು",
    "original_script": "kannada",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "20世紀最大のカンナダ語詩人・小説家（1904-1994）。本名K・V・プッタッパ。叙事詩『シュリー・ラーマーヤナ・ダルシャナム』でジュナーンピート賞（1967、カンナダ語初）を受賞した。バクティ伝統と近代人文主義の融合により、神々を「人間」として描いた点で正統に挑戦した。",
    "background": "マルナード地方の小カースト出身で、独立運動とカンナダ・ナショナリズムを文学に結晶化した。",
    "development": "現代カルナータカ州歌『ジャヤ・バーラタ・ジャナニヤ・タヌジャテ』の作者。マイソール大学副学長としてカンナダ語教育・文学制度に貢献。",
    "historical_context": "カンナダ近代文学の中核的人物。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kuvempu",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "M・T・ヴァースデーヴァン・ナーイル",
    "name_en": "M.T. Vasudevan Nair",
    "name_original": "എം. ടി. വാസുദേവൻ നായർ",
    "original_script": "malayalam",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "現代マラヤーラム文学・映画の最大の作家（1933-2024）。長編『ナールケットゥ』（1958）で伝統的マトリリニア大家族制度の崩壊を描き、『ランドゥアーム ウーラム（第二章）』（1984）でマハーバーラタを敗者ビーマの視点から再構築した。1995年ジュナーンピート賞受賞。脚本家・監督としてもマラヤーラム映画黄金期を主導した。",
    "background": "ケーララ州の中産階級ナーイル・カースト出身で、伝統的家族制度の解体期に育った経験が小説の主題に直結した。",
    "development": "古典叙事詩の被害者視点による再話は世界文学のポストモダン的潮流と並行する。",
    "historical_context": "南インド近代文学・映画の中核的人物。",
    "primary_source_url": "https://en.wikipedia.org/wiki/M._T._Vasudevan_Nair",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マハーシュウェター・デーヴィー",
    "name_en": "Mahasweta Devi",
    "name_original": "মহাশ্বেতা দেবী",
    "original_script": "bengali",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ベンガル語小説家・社会活動家（1926-2016）。『ジャングルの権利』『1084の母』『火の中で』等で、ベンガル・ジャールカンド・ビハール地方の部族（アディヴァースィー）社会の歴史と現代的搾取を文学化した。サバルタン研究・ガヤトリ・スピヴァク英訳を通じて世界的ポストコロニアル文学の代表となる。1996年ジュナーンピート賞受賞。",
    "background": "ベンガル知的中産階級出身ながら、シャブール族・ロディー族など先住民社会との数十年に及ぶ共生から作品を生んだ。",
    "development": "スピヴァク翻訳『Imaginary Maps』『Breast Stories』等により、サバルタン・スタディーズの世界的標準テクストとなった。",
    "historical_context": "インド先住民・サバルタン文学の世界的代表。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mahasweta_Devi",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヴァイクム・ムハンマド・バシール",
    "name_en": "Vaikom Muhammad Basheer",
    "name_original": "വൈക്കം മുഹമ്മദ് ബഷീർ",
    "original_script": "malayalam",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "20世紀マラヤーラム文学の革新的小説家（1908-1994）。『パーッタムマーユーデ・アアトゥ（パーッタンマーの山羊）』『バールヤカーラサキー（幼少期の女友達）』『マンタリッカム（馬鹿者の馬鹿話）』等で、ケーララのムスリム下層民の口語的語り、貧困・愛・宗教の人間的滑稽さを独特の語り口で描いた。マラヤーラム小説に口語性と少数派視点を導入した。",
    "background": "独立運動への参加・投獄・流浪を経て、エリート的サンスクリット化したマラヤーラム文学に庶民の口語を持ち込んだ。",
    "development": "現代マラヤーラム作家の口語性・地方性・少数派視点の規範的源泉となった。",
    "historical_context": "南インド近現代文学の口語的革新者。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Vaikom_Muhammad_Basheer",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "U・R・アナンタムールティ『サンスカーラ』",
    "name_en": "U.R. Ananthamurthy's Samskara",
    "name_original": "ಸಂಸ್ಕಾರ",
    "original_script": "kannada",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "U・R・アナンタムールティ（1932-2014）のカンナダ語長編小説（1965）。バラモン共同体の異端者ナーラナッパの死後、その火葬（サンスカーラ）を巡って正統バラモン社会の偽善が暴露される過程を描く。インド・ナヴィヤ（新写実）運動の中核作品で、現代インド文学による正統批判の世界的代表作。",
    "background": "バーミンガム大学留学体験とプロテスタント実存哲学の影響が伝統的ヒンドゥー社会批判を可能にした。",
    "development": "1970年映画化（ガンガダル・パテール監督）が国際的評価を得、サンスカーラはインド近現代文学の正典となった。",
    "historical_context": "南インド・ナヴィヤ運動の最高傑作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Samskara_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "インディラ・ゴースワーミー",
    "name_en": "Indira Goswami",
    "name_original": "ইন্দিৰা গোস্বামী",
    "original_script": "assamese",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "アッサム語の小説家・エッセイスト（1942-2011）。『ニーラ・カントゥヤ・ニードゥル（青の鳴き声）』『ウーンエ・コアー・ハウダ（象の旅人）』等で、寡婦・低カースト女性・周縁的宗教共同体の苦難を内面から描いた。1976年タリーフ賞、2000年ジュナーンピート賞、2008年プリンシプ・クラウス賞を受賞。アッサム独立運動仲介者としても活動。",
    "background": "若年寡婦としての自身の経験が、ヒンドゥー寡婦社会の文学的記録に深い真実味を与えた。",
    "development": "ULFA（アッサム統一解放戦線）と政府との和平仲介者として文学を超えた社会的影響を持った。",
    "historical_context": "北東インド近現代文学の世界的代表。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Indira_Goswami",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "プラティバー・ラーイ",
    "name_en": "Pratibha Ray",
    "name_original": "ପ୍ରତିଭା ରାୟ",
    "original_script": "odia",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "オリヤー語の小説家（1943-）。『ヤージニャセニー』（1984）でマハーバーラタのドラウパディーを一人称で語り直し、女性の主体性と五人の夫との結婚の悲劇を再考した。『マハーモハ』『シーラパドマ』等の歴史小説と、サオラー族等の部族民の生活に基づく社会派小説を併行した。2011年ジュナーンピート賞受賞。",
    "background": "教育者として部族地域に長年住み、フィールドワーク的経験を文学化した。",
    "development": "古典叙事詩の女性視点からの再話は世界的フェミニスト・文学運動と並行する。",
    "historical_context": "現代オリヤー文学の最大の女性作家。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Pratibha_Ray",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — 英印文学（Indo-Anglian） (8)
# ===============================================================

add({
    "name_ja": "ムルク・ラージ・アーナンド『不可触民』",
    "name_en": "Mulk Raj Anand's Untouchable",
    "name_original": "Untouchable",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ムルク・ラージ・アーナンド（1905-2004）の最初の長編小説（1935）。便所掃除人バーカー少年の一日を辿りつつ、不可触民（チャマール）が経験するカースト的屈辱を写実的に描いた。E・M・フォースター序文を得て世界的に流通し、英印文学の社会派写実主義の起点となった。",
    "background": "ロンドンのブルームズベリー・グループと交流するなかで、インド社会改革の文学的方途を模索した著者の最初の傑作。",
    "development": "アーナンド『苦力』『二葉と一蕾』等を含む英印社会派写実主義の起源となった。",
    "historical_context": "英印文学の社会改革文学的伝統の起点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Untouchable_(novel)",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラージャー・ラオ『カーンタプラ』",
    "name_en": "Raja Rao's Kanthapura",
    "name_original": "Kanthapura",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "ラージャー・ラオ（1908-2006）の最初の長編小説（1938）。南インド・カルナータカの架空の村カーンタプラのガンディー独立運動への参加を、村の老婦人の口承的語りで描いた。著者前書きで「英語をインド的方法で使う」原理を宣言し、英印文学の言語論的課題を理論化した。",
    "background": "サンスクリット古典叙事詩のスタイルを英語に翻案する独自の文体実験により、英印文学の言語論的可能性を提示した。",
    "development": "後の英印文学の「翻訳的英語」「インド英語」の規範的先例となった。",
    "historical_context": "英印文学言語論の理論的・実践的起点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Kanthapura",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "R・K・ナーラーヤン マルグディ世界",
    "name_en": "R.K. Narayan's Malgudi",
    "name_original": "Malgudi",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "R・K・ナーラーヤン（1906-2001）が『スワーミーと友達』（1935）から『先生たち』『英語教師』『ガイド』等まで一貫して舞台にした南インドの架空都市マルグディ。植民地末期から独立後インドの中流ヒンドゥー社会の日常的滑稽と尊厳を、抑制された英語散文で描いた。グレアム・グリーンの推挙により世界文学に位置づけられた。",
    "background": "南インドのバラモン教師家庭の日常を文学化することで、政治化されすぎない「普通のインド」を提示した。",
    "development": "マルグディは英印文学における架空都市の規範となり、フォークナーのヨクナパトーファに比肩される。",
    "historical_context": "英印文学の世界文学的位置を確立した日常性の作家。",
    "primary_source_url": "https://en.wikipedia.org/wiki/R._K._Narayan",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アニタ・デサイ",
    "name_en": "Anita Desai",
    "name_original": "Anita Desai",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ベンガル人母とドイツ人父を持つ英印作家（1937-）。『山頂の火』『澄んだ昼の光』『ボーンビーの夏』『断食、御馳走』等で、近代インド中産階級の女性・知識人の内面的孤立と精神的危機を心理学的精度で描いた。三度ブッカー賞最終候補となり、英印文学の心理小説の規範を確立した。",
    "background": "二つの文化の間に生きる経験が、社会派写実主義から内面的写実主義への英印文学の転換を可能にした。",
    "development": "娘キラン・デサイ（『The Inheritance of Loss』）に英印文学の系譜を継承した。",
    "historical_context": "英印文学心理派の中核的人物。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Anita_Desai",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "サルマーン・ラシュディ『真夜中の子供たち』",
    "name_en": "Salman Rushdie's Midnight's Children",
    "name_original": "Midnight's Children",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "サルマーン・ラシュディ（1947-）の長編小説（1981）。1947年8月15日深夜に生まれインドの独立瞬間と運命を共有する千人余の「真夜中の子供たち」、特にテレパシー能力を持つサリーム・スィナイの一代記を、マジック・リアリズムと多言語的英語で語る。1981年ブッカー賞、2008年「Best of the Booker」を受賞した。",
    "background": "ラテン・アメリカのマジック・リアリズム（マルケス、ボルヘス）とインド多元的口承伝統の融合が独自の文学的言語を生んだ。",
    "development": "英印文学を世界文学の中核に押し上げた決定的作品となり、後続のアミタヴ・ゴーシュ・アルンダティ・ロイらの基盤を提供した。",
    "historical_context": "ポストコロニアル文学の世界的代表作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Midnight%27s_Children",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ヴィクラム・セート『A Suitable Boy』",
    "name_en": "Vikram Seth's A Suitable Boy",
    "name_original": "A Suitable Boy",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ヴィクラム・セート（1952-）の長編小説（1993）。1950年代独立直後のインドを舞台に、ベンガル中産階級の母親が娘ラタに「適切な相手（suitable boy）」を見つける過程を中心に、四つのヒンドゥー・ムスリム家族の交錯を1,400ページ以上の伝統的写実小説形式で描いた。19世紀英国小説（オースティン・トロロップ）の手法をインドに適用した独自の試み。",
    "background": "ラシュディのマジック・リアリズムと対照的に、伝統的写実小説の英印文学への適用を意識的に試みた。",
    "development": "2020年BBCドラマ化により世界的読者を獲得し、ラシュディとは異なる英印文学的可能性を示した。",
    "historical_context": "英印写実主義の世界的代表作。",
    "primary_source_url": "https://en.wikipedia.org/wiki/A_Suitable_Boy",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アルンダティ・ロイ『小さきものたちの神』",
    "name_en": "Arundhati Roy's The God of Small Things",
    "name_original": "The God of Small Things",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "アルンダティ・ロイ（1961-）の最初の長編小説（1997）。ケーララのシリア正教会キリスト教徒家族と低カースト男性の禁断の関係を中心に、「愛は誰を、いつ、いかに、どれほど愛してよいかという法則」が支配する社会の悲劇を、革新的詩的英語で描く。1997年ブッカー賞受賞、世界40言語以上に翻訳された。",
    "background": "建築学・脚本家経験を経た著者の最初の小説で、現代英印文学の言語的・主題的可能性を一新した。",
    "development": "受賞後ロイは社会活動家として核兵器・ダム建設・ナクサリート問題等を批評し、文学者・活動家の融合的役割を体現した。",
    "historical_context": "現代英印文学の世界的金字塔。",
    "primary_source_url": "https://en.wikipedia.org/wiki/The_God_of_Small_Things",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アミタヴ・ゴーシュ",
    "name_en": "Amitav Ghosh",
    "name_original": "Amitav Ghosh",
    "original_script": "roman",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ベンガル人英印小説家・人類学者（1956-）。『理性のサークル』『ガラスの宮殿』『シャドウ・ライン』『ハングリー・タイド』、特に『アヘン戦争三部作』（『The Sea of Poppies』『The River of Smoke』『Flood of Fire』）でアジア海域経済史の人類学的小説化を達成した。気候変動文学『The Great Derangement』も影響力大。",
    "background": "オックスフォード大学社会人類学博士論文（エジプト・フィールドワーク）の手法を歴史小説に応用した。",
    "development": "気候変動文学（cli-fi）を学術的に基礎付け、現代世界文学の理論的中心の一人となった。",
    "historical_context": "英印文学を歴史人類学・気候人類学に拡張した代表作家。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Amitav_Ghosh",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ===============================================================
# CATEGORY E — 主要主題と運動 (8)
# ===============================================================

add({
    "name_ja": "分離独立文学",
    "name_en": "Partition literature",
    "name_original": "विभाजन साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド分離独立期",
    "definition": "1947年印パ分離独立に伴う100万人規模の死と1500万人規模の強制移動を主題とする多言語文学群。マントー、ファイズ、ビーシャム・サーフニー『タマス』、クシュワント・スィン『パキスタンへの汽車』、アミルタ・プリータム『ピンジャル』等が代表作。世界的トラウマ文学・移動文学研究の中核的事例。",
    "background": "南アジア最大の歴史的トラウマを文学的に記憶化する集合的試みとして、ウルドゥー・ヒンディー・パンジャービー・ベンガル諸言語で同時並行的に展開した。",
    "development": "現代までドキュメンタリー・映画・ノンフィクションへと媒介を超えて拡大し続ける文学群。",
    "historical_context": "南アジア集合的記憶の文学的構築。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Partition_of_India_in_popular_culture",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "進歩主義作家運動",
    "name_en": "Progressive Writers' Movement",
    "name_original": "ترقی پسند تحریک",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "1936年ラクナウーで初の全インド大会が開催された左派文学運動。サッジャード・ザヒール、プレームチャンド、ファイズ、サーヒル、ムルク・ラージ・アーナンド、イスマット・チュグタイ等が参画し、ヒンディー・ウルドゥー・英語等多言語にわたって、社会主義リアリズムの観点からカースト・封建主義・植民地主義を批判する文学を生んだ。",
    "background": "ロンドン留学のインド人左派知識人グループが結成した全インド進歩主義作家協会（AIPWA）が運動の中核となった。",
    "development": "現代南アジア進歩主義文学の規範的源泉となり、独立後ファイズ等を通じてパキスタンにも継承された。",
    "historical_context": "20世紀南アジア左派文学の制度的中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Progressive_Writers%27_Movement",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "部族文学（アディヴァースィー文学）",
    "name_en": "Adivasi/Tribal literature",
    "name_original": "आदिवासी साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "インド部族民（アディヴァースィー）作家による母語または地方語文学。サンタリー語のサーディラム・ハーンスダー、ボーロ語、ガロ語、グーンディ語等によるノンサンスクリット系言語文学運動。マハーシュウェター・デーヴィー（部族民協力者）の小説と並び、植民地・近代化・カースト・国家による複合的搾取を文学化する。",
    "background": "サンスクリット中心・ヒンドゥー中心の正典伝統への根本的挑戦として、独立後特に1980年代以降本格化した。",
    "development": "サンタリー語『オル・チキ』文字の制定（1925）以降、各部族言語の独自文学が蓄積されてきた。",
    "historical_context": "インド最も周縁化された主体の文学的可視化。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Adivasi",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "インド・フェミニズム文学",
    "name_en": "Indian feminist literature",
    "name_original": "भारतीय नारीवादी साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "ターラブジ・ショールカル『シャラダ』（マラーティー1882）以降、ラシード・ジャハーン、イスマット・チュグタイ『リハーフ（毛布）』（ウルドゥー1942）、カマラ・ダース、シャシ・デーシュパーンデー、ナンタ・カケーラ等によるインド多言語フェミニズム文学。寡婦制度・カースト・性的禁忌・離婚・労働を主題化した。",
    "background": "19世紀ベンガル女性教育運動以来、女性の表現主体性確立は近代インド文学の重要主題であり続けた。",
    "development": "現代Tamil・Marathiのダリット・フェミニスト文学（バーマ『カルックー』）等への系譜を形成した。",
    "historical_context": "インド近代文学の主体性確立運動の中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Feminism_in_India",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "英印 vs バーシャ論争",
    "name_en": "Indo-English vs Bhasha debate",
    "name_original": "अंग्रेजी बनाम भाषा साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "英語で書くインド人作家（Indo-English）と諸地方言語（バーシャ）で書く作家との間の正統性論争。ラシュディが『The Vintage Book of Indian Writing』序文（1997）で「ポスト独立インドで英印文学が他言語より優れる」と主張したことが論争を激化させ、U・R・アナンタムールティらが地方言語文学の独立的価値を擁護した。",
    "background": "植民地遺産としての英語と土着言語の階層的分業の問題が、グローバル化時代に再燃した。",
    "development": "現代まで未解決の論争として、英印文学の世界的成功と諸地方言語文学のローカル的根強さの緊張を反映する。",
    "historical_context": "ポストコロニアル文学言語論の代表的論争。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Languages_of_India",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ポストコロニアル・インド文学",
    "name_en": "postcolonial Indian literature",
    "name_original": "उपनिवेशोत्तर भारतीय साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "1947年独立以降のインド多言語文学を植民地遺産との対峙として捉える批評的枠組。ラシュディのマジック・リアリズム、サバルタン研究（ラナジット・グハ）、ホーミ・バーバ『The Location of Culture』、ガヤトリ・スピヴァク『Can the Subaltern Speak?』等の批評理論と並行し、インド文学の世界文学的位置を理論化する。",
    "background": "サイード『オリエンタリズム』（1978）以降の批評的潮流が、英印文学とインド文学批評を世界的中心に押し上げた。",
    "development": "現代世界文学批評の主要な理論的枠組として継承される。",
    "historical_context": "20世紀末・21世紀初頭の世界文学的批評枠組。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Postcolonial_literature",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "インド・エコ文学",
    "name_en": "eco-literature in India",
    "name_original": "पारिस्थितिक साहित्य",
    "original_script": "devanagari",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "現代インド期",
    "definition": "アミタヴ・ゴーシュ『The Hungry Tide』『The Great Derangement』、アルンダティ・ロイ『The Cost of Living』、グルザール、アグニ・シェカール（カシミール）、サウスインド作家ペルマル・ムルガン等によるインド・エコ文学運動。シュンドル盆地、ナルマダー川流域、ラジャスターン砂漠化、ヒマラヤ氷河融解等の地域的環境問題を文学化する。",
    "background": "インドの急速な経済発展と気候変動の影響への文学的応答として2000年代以降本格化した。",
    "development": "ゴーシュ『The Great Derangement』が示すように、世界文学・気候人類学・環境正義運動を架橋する。",
    "historical_context": "気候変動時代の南アジア文学の新領域。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Climate_fiction",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "イスマット・チュグタイ『リハーフ（毛布）』",
    "name_en": "Ismat Chughtai's Lihaaf",
    "name_original": "لحاف",
    "original_script": "urdu",
    "subfield_code": "lit_india",
    "region": "南西アジア",
    "period_key": "インド近代期",
    "definition": "イスマット・チュグタイ（1915-1991）の短編（1942）。ムスリム上流家庭の年若い女主人ベーガム・ジャーンと女中召使ラッボーの同性愛的関係を、家庭の内側を覗く幼女視点で間接的に描いた。1944年ラホール法廷でわいせつ罪で告訴されたが（マントーと同日審理、共に無罪）、現代インド・ウルドゥー文学のクィア文学・フェミニズム文学の起源となった。",
    "background": "アリーガル・ムスリム女子学校で教育を受け、進歩主義作家運動の女性的中核を担った。",
    "development": "南アジアのフェミニズム・クィア文学の歴史的源流として、現代まで翻訳・舞台化・映画化が続く。",
    "historical_context": "ウルドゥー文学のセクシュアリティ表現の境界突破事例。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Lihaaf",
    "primary_source_type": "Wikipedia canonical entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (12+ entries per requirement)
# ---------------------------------------------------------------
FOURTH_TRANSFORM_TAGS = {
    "分離独立文学": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "数百万人規模の経験的トラウマを文学化する分離独立文学の真正性は、AI生成テクストでは複製不可能な経験的記憶の文学的真理性を問い直す試金石となる。",
         "ai_phenomenon": "AI生成テクストにおける歴史的トラウマの真正性"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "マントー『トーバー・テーク・スィン』に代表される分離文学の不条理的・断片的物語形式は、AI生成における歴史的記憶の物語的構築可能性を再考する基盤を提供する。",
         "ai_phenomenon": "AI時代の歴史的トラウマ物語化"},
    ],
    "進歩主義作家運動": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "プロレタリア・農民・女性の発話主体を中心化する進歩主義文学の主体論は、AI生成テクストにおける周縁的主体の発話表象問題と直接対応する。",
         "ai_phenomenon": "AI生成における周縁的主体の表象"},
        {"axis": "正典", "status": "rethinking",
         "rationale": "サンスクリット中心・上層カースト中心の正典に対する代替正典構築の試みは、AI訓練データにおける正典化機制の問題と直接接続する。",
         "ai_phenomenon": "AI訓練コーパスの代替的正典化"},
    ],
    "ラシュディ『真夜中の子供たち』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "マジック・リアリズムによる集合的・個人的歴史の融合的物語化は、AI生成における虚構と歴史の境界再編問題の文学的先駆である。",
         "ai_phenomenon": "AI生成における歴史と虚構の融合"},
    ],
    "サルマーン・ラシュディ『真夜中の子供たち』": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "マジック・リアリズムによる集合的・個人的歴史の融合的物語化は、AI生成における虚構と歴史の境界再編問題の文学的先駆である。",
         "ai_phenomenon": "AI生成における歴史と虚構の融合"},
        {"axis": "言語", "status": "rethinking",
         "rationale": "ヒンディー・ウルドゥー・英語の混淆的「チャトニー化された英語」は、LLMの多言語混淆生成と直接的に並行する文学的現象。",
         "ai_phenomenon": "LLMの多言語混淆生成（コードスイッチング）"},
    ],
    "英印 vs バーシャ論争": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "支配言語と地方言語の文学的階層問題は、英語中心LLM時代における多言語文学的真正性問題と直接対応する。",
         "ai_phenomenon": "英語中心LLMにおける多言語文学的真正性"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "世界文学的受容と地域的受容の階層化問題は、AI翻訳時代の文学的受容の世界的階層化問題と並行する。",
         "ai_phenomenon": "AI翻訳による文学的受容の階層再編"},
    ],
    "ポストコロニアル・インド文学": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "西欧中心正典に対するポストコロニアル批判の枠組は、AI訓練コーパスの英米中心性に対する批評的枠組として直接応用可能。",
         "ai_phenomenon": "AI訓練コーパスの西欧中心性批判"},
    ],
    "部族文学（アディヴァースィー文学）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "サンスクリット中心・ヒンドゥー中心の正典に対する部族民の発話主体性確立は、AI生成テクストの少数民族主体表象問題と直接対応する。",
         "ai_phenomenon": "AI生成における少数民族主体の表象"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "口承伝統と書記伝統の境界に位置する部族文学の真正性は、AIによる口承伝統の記録・生成可能性の倫理問題と直接接続する。",
         "ai_phenomenon": "AIによる口承文学の記録・生成倫理"},
    ],
    "アミタヴ・ゴーシュ": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "気候変動文学（cli-fi）における人新世物語論は、AI生成における長時間スケール（千年・百年）の物語化能力の理論的枠組を提供する。",
         "ai_phenomenon": "AI生成における人新世スケール物語化"},
    ],
    "インド・フェミニズム文学": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "女性発話主体の確立過程は、AI生成テクストにおけるジェンダー的主体表象の構造的問題への文学的先例を提供する。",
         "ai_phenomenon": "AI生成におけるジェンダー的主体表象"},
    ],
    "イスマット・チュグタイ『リハーフ（毛布）』": [
        {"axis": "真正性", "status": "rethinking",
         "rationale": "1944年わいせつ罪訴訟が示すクィア表象の社会的境界突破は、AI生成テクストの倫理的・法的境界問題への歴史的先例。",
         "ai_phenomenon": "AI生成テクストの倫理的境界突破"},
    ],
    "ファイズ・アフマド・ファイズ": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "国境を超えて愛唱される抵抗詩の受容構造は、AI翻訳時代の政治詩の越境的受容の文学的先例。",
         "ai_phenomenon": "AI翻訳による政治詩の越境的受容"},
    ],
    "マハーシュウェター・デーヴィー": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "スピヴァクによる英訳が原作と独立した世界文学的価値を獲得した現象は、AI翻訳時代の翻訳論・原作・受容の関係再編問題を予示する。",
         "ai_phenomenon": "AI翻訳における原作と翻訳の関係再編"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>= 8)
# ---------------------------------------------------------------
CROSS_DOMAIN_LINKS = [
    ("マハーデーヴィー・ヴァルマー", "PT", "shared_concept", "chhayavad poetics",
     "チャーヤーヴァード詩学はインド近代ロマン主義詩学として詩学・批評理論DBの主要対象。"),
    ("スーリヤカーント・トリパーティー・ニラーラー", "PT", "shared_concept", "free verse / Hindi prosody",
     "ニラーラーが確立したヒンディー自由律詩の韻律理論はインド近代詩学の中核として詩学DBと共有される。"),
    ("タゴール散文歌（ロビンドロ・ションギト）", "PT", "shared_concept", "lyric poetics / song-poem",
     "タゴール散文歌の歌詞と音楽の一体性は近代以前の詩学的伝統として詩学DBの参照対象。"),
    ("アッラーマ・イクバール『バーンゲ・ダラー』", "PHIL", "shared_concept", "Iqbal philosophy / khudi",
     "イクバールの「自我（フディー）」概念はイスラーム近代主義哲学として哲学DBの主要対象。"),
    ("ブラフモ・サマージ運動", "PHIL", "shared_concept", "Hindu modernism / Vedanta",
     "ブラフモ・サマージのヴェーダーンタ普遍主義は近代インド哲学の起源として哲学DBと一体。"),
    ("シャーンティニケトン", "PHIL", "shared_concept", "Tagore philosophy / education",
     "タゴール教育哲学はアジア近代教育思想として哲学DBの主要対象。"),
    ("部族文学（アディヴァースィー文学）", "AN", "shared_concept", "tribal/indigenous literature",
     "インド部族民文学は人類学的先住民研究と直接接続する文学的記録。"),
    ("マハーシュウェター・デーヴィー", "AN", "shared_concept", "subaltern / adivasi ethnography",
     "マハーシュウェター・デーヴィーの部族民フィールドワーク的小説は人類学的サバルタン研究と一体。"),
    ("分離独立文学", "AN", "shared_concept", "partition / forced migration",
     "南アジア分離独立は人類学的強制移動・トラウマ研究の中核事例として文学的記録と接続する。"),
    ("英印 vs バーシャ論争", "AI-Development", "parallel", "multilingual LLM / language hierarchy",
     "支配言語と地方言語の文学的階層問題は多言語LLMにおける言語階層問題と直接対応する。"),
    ("ポストコロニアル・インド文学", "AI-Development", "parallel", "AI training corpus / postcolonial critique",
     "西欧中心正典批判の枠組はAI訓練コーパスの英米中心性批判の理論的枠組として直接応用可能。"),
    ("ファイズ・アフマド・ファイズ", "Cultural-Intelligence", "parallel", "protest poetry / transnational reception",
     "国境を超えて愛唱される抵抗詩の受容構造は文化情報DBの越境的文化受容研究と直接接続する。"),
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

        print(f"\n=== C20 India Modern completed ===")
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
