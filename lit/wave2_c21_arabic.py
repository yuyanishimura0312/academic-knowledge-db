"""
LIT-DB Phase 2 — C21 Wave2: Arabic Literature (アラブ文学)
============================================================
Inserts 40 representative concepts spanning 5 categories:
  A. ジャーヒリーヤ詩学 (8)
  B. 古典アラブ詩学・修辞学 (8)
  C. 散文ジャンル (8)
  D. 主題と世界観 (8)
  E. ナフダ以降近代 (8)

subfield_id=13, code='lit_arabic', region='南西アジア'

Sources: shamela.ws (PD Arabic library), OpenITI (open Arabic
text initiative), Encyclopaedia Iranica (for cross-cultural),
Wikipedia (English) where canonical concept entries exist.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    ("ジャーヒリーヤ期", "Jahiliyya (Pre-Islamic)", -500, 622,
     "イスラーム以前のアラビア半島。口承詩文化が栄え、カスィーダ・ムアッラカートが成立。"),
    ("初期イスラーム・ウマイヤ朝期", "Early Islamic / Umayyad", 622, 750,
     "イスラーム成立後、アラビア語が宗教・行政言語として広域化、ハディース・伝記文学が成立。"),
    ("アッバース朝古典期", "Abbasid Classical", 750, 1258,
     "バグダード中心の文化的隆盛。アダブ・修辞学・マカーマ・千夜一夜物語が完成形を取る。"),
    ("ポストモンゴル・マムルーク期", "Post-Mongol / Mamluk", 1258, 1798,
     "中心の分散と注釈学の展開、イブン・ハルドゥーンや百科全書的散文の時代。"),
    ("ナフダ期（近代復興）", "Nahda (Modern Revival)", 1798, 1945,
     "ナポレオンのエジプト遠征以降、近代化と西欧文学受容、新ジャンル（小説・短編・演劇）の誕生。"),
    ("現代アラブ文学期", "Modern / Contemporary Arabic", 1945, 2025,
     "脱植民地化・自由詩運動・iltizam（コミットメント文学）・ノーベル賞作家の登場。"),
]


CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — ジャーヒリーヤ詩学 (8)
# ===============================================================

add({
    "name_ja": "カスィーダ",
    "name_en": "qasida",
    "name_original": "قصيدة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "ジャーヒリーヤ期に確立した長編単韻頌詩で、ナスィーブ（恋愛的前奏）・ラヒール（旅）・マディーフ（賛歌）の三部構成を典型とする。各行が同一脚韻を持ち、アラブ詩の正統形式として千年以上にわたり継承された。",
    "background": "遊牧ベドウィン社会の口承詩人（シャーイル）が部族の名誉と歴史を歌う形式として発達した。",
    "development": "ウマイヤ朝・アッバース朝で宮廷頌詩へと変容し、ペルシア語・ウルドゥー語・スワヒリ語詩に伝播した。",
    "historical_context": "部族社会の集合的記憶装置であり、文字化以前から数百年継承された。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Qasida",
    "primary_source_type": "Wikipedia canonical entry / shamela.ws diwans",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ムアッラカート（懸詩）",
    "name_en": "Mu'allaqat",
    "name_original": "المعلقات",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "ジャーヒリーヤ期を代表する七編（または十編）の長編カスィーダの選集で、伝承上カアバ神殿に黄金の文字で「懸けられた」とされる。イムル・ル・カイス、ターラファ、ズハイル、ラビードらの作品からなり、アラブ古典詩の正典を形成する。",
    "background": "前イスラーム期ウカーズ詩市での詩競演で選定されたとされ、後代のアブー・ザイド編纂で確立した。",
    "development": "アンソロジー文化の起点となり、現代に至るまで詩教育の核とされる。",
    "historical_context": "アラブ口承詩の頂点を示す正典として標準化された。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Mu%27allaqat",
    "primary_source_type": "Wikipedia / OpenITI texts",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マディーフ（賛歌）",
    "name_en": "madh",
    "name_original": "مدح",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "部族の長や君主、預言者を讃えるための賛詩のジャンル。カスィーダの末尾部に配置されるのが典型で、被讃者の徳・寛大さ・武勲を誇張的修辞で描く。アッバース朝には宮廷詩人の主要収入源となった。",
    "background": "部族社会の名誉と恩顧の関係を言語化する儀礼的詩形式として発達した。",
    "development": "預言者讃詩（マディーフ・ナバウィー）として宗教化し、ブースィーリーの『マントの賦』に結実した。",
    "historical_context": "口承詩から宮廷詩、宗教詩へと制度的役割を変えた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Madih_nabawi",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ヒジャー（諷刺詩）",
    "name_en": "hija",
    "name_original": "هجاء",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "敵対部族や個人を嘲笑・誹謗する諷刺詩のジャンル。ジャーヒリーヤ期には呪詛的な力を持つと信じられ、戦闘の代替手段としても機能した。アッバース朝期にイブン・アル＝ルーミーやアル＝ムタナッビーが洗練された政治諷刺へと展開した。",
    "background": "部族間紛争における言語的攻撃手段として発達し、口承で広く伝播した。",
    "development": "ジャリールとファラズダクの「諷刺合戦」（naqa'id）で芸術的頂点を迎え、近代ではアフマド・シャウキーらに継承された。",
    "historical_context": "言葉を物理的武器と等価視するアラブ詩の力学を体現した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Hija_(poetry)",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "リサー（哀歌）",
    "name_en": "ritha",
    "name_original": "رثاء",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "死者を悼む哀悼詩のジャンルで、故人の徳・武勲・寛容を回想し、運命の無情を嘆く。女流詩人ハンサーの兄サフルへの哀歌が古典的範例とされる。後にカルバラーの悲劇を悼むシーア派哀歌へと展開した。",
    "background": "部族社会において葬礼儀礼と結びついた追悼の言語芸術として発達した。",
    "development": "中世アンダルスの都市哀歌（ritha al-mudun）に発展し、グラナダ陥落を悼む詩などに継承された。",
    "historical_context": "口承詩の社会的機能のうち集合的喪の表象を担った。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Al-Khansa",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ガザル（恋愛詩）",
    "name_en": "ghazal",
    "name_original": "غزل",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "初期イスラーム・ウマイヤ朝期",
    "definition": "恋愛・別離・憧憬を主題とする短い抒情詩のジャンルで、カスィーダの前奏部ナスィーブから自立して独自形式となった。ウマイヤ朝のウマル・イブン・アビー・ラビーアによる都市的官能詩、ジャミールらによるウズル恋（純愛）詩の二系統を生み、ペルシア・ウルドゥー詩に決定的影響を与えた。",
    "background": "ベドウィン恋愛詩の前奏部が都市文化のなかで自立的ジャンル化した。",
    "development": "ペルシア語ガザル（ハーフィズ）、ウルドゥー語ガザル（ガーリブ）に伝播し、世界詩史の主要形式となった。",
    "historical_context": "ジャーヒリーヤから初期イスラームへの社会変動を抒情の私的内面化として記録した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ghazal",
    "primary_source_type": "Wikipedia / OpenITI diwans",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ワスフ（描写詩）",
    "name_en": "wasf",
    "name_original": "وصف",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "ラクダ・馬・砂漠・夜・雷雨など対象を細密に描写するアラブ詩の修辞的中核。カスィーダの中間部ラヒールでしばしば壮大なラクダ描写として展開され、視覚的精緻さが詩の卓越性を測る基準となった。",
    "background": "遊牧生活に密着した観察眼が言語化された結果として発達した。",
    "development": "アッバース朝にイブン・アル＝ルーミーらが都市風物・食物の描写詩へと拡張した。",
    "historical_context": "アラブ詩学の写実精神の根幹をなす修辞的徳目とされた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Arabic_poetry",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ナスィーブ（前奏部）",
    "name_en": "nasib",
    "name_original": "نسيب",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "カスィーダの開幕部で、廃墟（atlal）の前で去った愛人を回想する定型的恋愛序詩。詩人の感情的世界を確立しつつ聴衆を本題（賛歌・諷刺）へと引き込む機能を持ち、後にガザルとして自立した。",
    "background": "遊牧民の移動生活における野営跡（atlal）の文化的記憶が詩的トポスとなった。",
    "development": "アッバース朝の「現代派」（muhdathun）詩人がナスィーブの儀礼性を批判し、新たな抒情を追求した。",
    "historical_context": "ジャーヒリーヤ詩学の三部構成の根幹をなす規範的部位だった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nasib_(poetry)",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY B — 古典アラブ詩学・修辞学 (8)
# ===============================================================

add({
    "name_ja": "バラーガ（雄弁術）",
    "name_en": "balagha",
    "name_original": "بلاغة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "アラブ古典修辞学の総称で、状況に適った言語表現の卓越性を理論化する学問。ジュルジャーニーの『イジャーズの諸証』により体系化され、bayan（明示論）、ma'ani（意味論）、badi（修辞美）の三部門に分かれる。クルアーンの修辞的奇跡（i'jaz）論と一体に発展した。",
    "background": "クルアーンの言語的卓越性を分析する神学的要請から修辞学が制度化した。",
    "development": "サッカーキー、カズウィーニーらによる教科書化を経て、近代まで詩学・神学の基礎科目とされた。",
    "historical_context": "イスラーム文明の言語観の中核を形成し、ペルシア・トルコ・ウルドゥー詩学に伝播した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ilm_al-balagha",
    "primary_source_type": "Wikipedia / shamela.ws (Jurjani PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "バヤーン（明示論）",
    "name_en": "bayan",
    "name_original": "بيان",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "バラーガ三部門の一つで、同一意味を異なる方法で表現する技法を扱う。直喩（tashbih）・隠喩（isti'ara）・換喩（kinaya）を中心に分類し、表現の明晰さと暗示の濃淡を分析する。",
    "background": "クルアーン解釈における比喩理解の必要から発達した。",
    "development": "ジュルジャーニー『修辞の秘密』が比喩を意味産出の中核と位置づけ、近代アラブ詩学にも継承された。",
    "historical_context": "アラブ修辞学の最も影響力ある分析装置となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ilm_al-bayan",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "バディーウ（修辞美）",
    "name_en": "badi",
    "name_original": "بديع",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "バラーガ三部門の一つで、対句・反語・パラノマシア（同音異義の遊び）など装飾的修辞技法の体系。イブン・アル＝ムウタッズ『キターブ・アル＝バディーウ』で初めて理論化され、ムタワッキル朝期の宮廷詩の華麗な技巧を支えた。",
    "background": "アッバース朝の都市文化と詩の専門化のなかで装飾性が体系化された。",
    "development": "後期マムルーク期にバディーウ志向が極端化し、ブースィーリーらの「バディーイヤ」詩を生んだ。",
    "historical_context": "アラブ詩学を装飾性の体系として整理する基礎を提供した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Ibn_al-Mu%27tazz",
    "primary_source_type": "Wikipedia / shamela.ws (Ibn al-Mu'tazz PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マアーニー（意味論）",
    "name_en": "ma'ani",
    "name_original": "معاني",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "バラーガ三部門の一つで、文の構造的選択（語順・省略・接続・断絶）が状況・聴衆に応じてどう意味を産出するかを論じる学問。ジュルジャーニーの「ナズム理論」（語順による意味生成説）が決定的貢献をした。",
    "background": "クルアーンの統語的特異性を解明する必要から発達した。",
    "development": "アラブ語法学（nahw）と修辞学を架橋し、近代の文体論に通じる議論を提供した。",
    "historical_context": "アラブ言語思想の最も独創的な領域とされる。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Abd_al-Qahir_al-Jurjani",
    "primary_source_type": "Wikipedia / shamela.ws (Jurjani PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ファサーハ（明晰）",
    "name_en": "fasaha",
    "name_original": "فصاحة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "個々の語と句の発音的・意味的な明晰さ、すなわち発音の容易さ・俗語の不在・文法的正しさを指す修辞的徳目。バラーガ（状況適合性）と対をなし、両者を満たす言語が「雄弁」と判定された。",
    "background": "アラブ語の純粋性をベドウィン口承に求める言語観に根差す。",
    "development": "ハリーリーの『マカーマ』など技巧文学はファサーハ追求の極点を示した。",
    "historical_context": "アラブ言語純粋主義（fasahah）の規範を形成した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Eloquence#Arabic_eloquence",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ジナース（同音異義）",
    "name_en": "jinas",
    "name_original": "جناس",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "発音や綴りが類似する異義語を対比的に並置する修辞技法（パラノマシア）。完全一致のジナース・ターム、子音配列が同一のジナース・ナーキスなど分類が精緻化され、バディーウの代表的装飾とされる。",
    "background": "アラブ語の三子音語根構造が同音異義を豊富に生む言語的基盤を提供した。",
    "development": "マムルーク期のシハーブッディーン・アル＝ヒッリーらが極端な技巧詩を生んだ。",
    "historical_context": "アラブ詩の音楽性と知的遊戯性の象徴となった。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Tajnis",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})

add({
    "name_ja": "カーフィヤ（押韻）",
    "name_en": "qafiya",
    "name_original": "قافية",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "アラブ詩の脚韻論で、詩全行を貫く単一の脚韻（rawi）を原則とする。アル＝ハリール・イブン・アフマドが韻律学（'arud）と並行して理論化し、後の詩人は16の伝統的韻律と単一脚韻の制約のもとで作詩した。",
    "background": "口承詩の音楽性を支える単韻原則が文字化を経て理論化された。",
    "development": "20世紀の自由詩運動（shi'r hurr）が単韻原則を解体する近代的転回を引き起こした。",
    "historical_context": "アラブ詩の形式的同一性を1500年にわたり保証した装置。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Arabic_prosody",
    "primary_source_type": "Wikipedia / shamela.ws (Khalil PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シナーア（技巧）",
    "name_en": "sina'a",
    "name_original": "صناعة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "詩や散文を「技芸（craft）」として捉える概念。アブー・ヒラール・アル＝アスカリー『二技芸論』（散文と韻文の技芸論）に代表され、文学を職人的修練と規範習得の対象とする見方を確立した。",
    "background": "アッバース朝期の都市文化で詩人・散文家が職業的アイデンティティを獲得した。",
    "development": "近代以降、芸術的天才観との緊張関係のなかで再解釈された。",
    "historical_context": "アラブ文学を学習可能な技芸体系と捉える視座の根幹をなす。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Abu_Hilal_al-Askari",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "minor",
})


# ===============================================================
# CATEGORY C — 散文ジャンル (8)
# ===============================================================

add({
    "name_ja": "マカーマ",
    "name_en": "maqama",
    "name_original": "مقامة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "10世紀末ハマダーニーが創始した押韻散文（saj'）と詩を交互に挿入する短編連作形式。流浪の詐欺師主人公が機知と修辞で人を欺き続ける筋書きを定型とし、ハリーリー『マカーマート』が頂点を成した。世界文学最古のピカレスク的形式の一つ。",
    "background": "アダブ文学の伝統と都市的話術文化が結合し新ジャンルを生んだ。",
    "development": "ヘブライ語マカーマ（アル＝ハリージーの翻訳）を経てヨーロッパのピカレスク小説へ間接的影響を与えた。19世紀ナフダ期にナースィーフ・アル＝ヤージジーが復興した。",
    "historical_context": "アラブ語修辞学の極致を物語形式に統合した点で文学史的意義をもつ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Maqama",
    "primary_source_type": "Wikipedia / shamela.ws (Hariri PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リサーラ（書簡）",
    "name_en": "risala",
    "name_original": "رسالة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "書簡形式の文学・思想散文。行政書簡（diwan al-rasa'il）の形式美から派生し、イブン・アル＝ムカッファウからジャーヒズへと展開した。アル＝マアッリー『赦しの書（リサーラト・アル＝グフラーン）』は来世訪問記の形式で文学批評を展開し、ダンテ『神曲』との比較研究の対象となる。",
    "background": "ペルシア由来の書簡行政文化がアラブ散文体に取り入れられ文芸化した。",
    "development": "ナフダ期に新聞論説・公開書簡へと近代的転用がなされた。",
    "historical_context": "アラブ散文の哲学的・文芸的可能性を切り開いた。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Risalat_al-Ghufran",
    "primary_source_type": "Wikipedia / shamela.ws (Ma'arri PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "千夜一夜物語",
    "name_en": "Alf Layla wa-Layla",
    "name_original": "ألف ليلة وليلة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "シャハラザードが王に夜ごと物語を語り続ける枠物語形式の説話集。ペルシア・インド・アラブ・エジプトの民話層が長期にわたり集積され、9-10世紀から19世紀まで増補が続いた。アラビアンナイトとして西欧オリエンタリズムの中心的テクストとなった。",
    "background": "中世イスラーム都市の夜話文化と多文化的説話伝承が結合した。",
    "development": "ガランの仏訳（1704-）以降、西欧文学（ボルヘス、プルースト、カルヴィーノ）に決定的影響を与えた。",
    "historical_context": "口承と書承の境界、民衆文学とアダブ伝統の境界を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights",
    "primary_source_type": "Wikipedia / shamela.ws (Bulaq edition PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アダブ（教養文学）",
    "name_en": "adab",
    "name_original": "أدب",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "「教養」「礼節」「文学」を意味する多義語で、9世紀以降は教養人（adib）が知っておくべき詩・散文・逸話・歴史・倫理を網羅する百科全書的散文ジャンルを指す。ジャーヒズ『動物の書』、イブン・クタイバ『知の泉』が代表作。",
    "background": "宮廷官僚（katib）の必要教養を体系化する社会的要請から発達した。",
    "development": "現代アラビア語で「文学」一般を意味する語となり、文学概念そのものの基盤となった。",
    "historical_context": "アラブ文化における「教養」と「文学」の不可分性を体現する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Adab_(Islam)",
    "primary_source_type": "Wikipedia / shamela.ws (Jahiz PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "シーラ（伝記）",
    "name_en": "sira",
    "name_original": "سيرة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "初期イスラーム・ウマイヤ朝期",
    "definition": "預言者ムハンマドの伝記（sirat rasul Allah）を原型とする伝記文学ジャンル。イブン・イスハーク／イブン・ヒシャームの古典的伝記に始まり、英雄叙事詩的伝記（sirat 'Antar、sirat Bani Hilalなど民衆ロマンス）へ拡張した。",
    "background": "ハディース学の発達と並行して預言者伝記の必要が生じ、文学化された。",
    "development": "民衆口承叙事『シーラト・バヌー・ヒラール』はユネスコ無形文化遺産に登録された。",
    "historical_context": "宗教史と民衆叙事を架橋するアラブ独自のジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Prophetic_biography",
    "primary_source_type": "Wikipedia / shamela.ws (Ibn Hisham PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ハバル（逸話）",
    "name_en": "khabar",
    "name_original": "خبر",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "初期イスラーム・ウマイヤ朝期",
    "definition": "「報せ」「逸話」を意味し、伝承者の連鎖（isnad）と本文（matn）の二部構造を持つ短い物語単位。アラブ歴史叙述・アダブ・ハディース学に共通する基本形式で、タバリーの大歴史書もハバルの集積として構成される。",
    "background": "口承伝達の信頼性検証技術がイスナード制度として整備された結果、独自の散文形式となった。",
    "development": "現代の新聞用語「ハバル」（ニュース）まで連続する語彙史を持つ。",
    "historical_context": "事実・物語・証言の境界を組織する独自の叙述様式。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Khabar_(literature)",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "リフラ（旅行記）",
    "name_en": "rihla",
    "name_original": "رحلة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "巡礼・修学・旅程を主題とする旅行記ジャンル。イブン・ジュバイル『旅行記』、イブン・バットゥータ『諸都市の珍奇と旅路の異聞についての贈物』が代表作で、後者は14世紀の東半球を網羅する世界文学的価値をもつ。",
    "background": "イスラーム圏の広域ネットワーク（ウンマ）と巡礼制度が長距離移動を恒常化した。",
    "development": "ナフダ期にリファーア・アッ＝タフターウィー『パリ要録』が西欧旅行記の新ジャンルを開いた。",
    "historical_context": "アラブの世界認識と他者表象の主要装置。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Rihla",
    "primary_source_type": "Wikipedia / shamela.ws (Ibn Battuta PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "マカーラ（論説）",
    "name_en": "maqala",
    "name_original": "مقالة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ナフダ期（近代復興）",
    "definition": "論説・エッセイのジャンルで、ナフダ期の新聞・雑誌文化のなかで近代散文として確立した。ファーリス・アッ＝シディヤク、ムハンマド・アブドゥらが宗教改革・文学改革・社会批判の論壇を形成し、20世紀の知識人言説の主要媒体となった。",
    "background": "印刷術導入と新聞創刊（『アル＝アハラーム』1875年など）が論説文化を生んだ。",
    "development": "タハ・フサインら近代知識人の論争空間を形成した。",
    "historical_context": "古典アダブと近代ジャーナリズムを橋渡しするジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nahda",
    "primary_source_type": "Wikipedia",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — 主題と世界観 (8)
# ===============================================================

add({
    "name_ja": "シューウービーヤ（民族意識論争）",
    "name_en": "shu'ubiyya",
    "name_original": "شعوبية",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "8-10世紀のアッバース朝期に展開された、アラブ人優位主義に対する非アラブ（特にペルシア）系知識人による反論運動・文学的論争。詩・散文を介して諸民族の対等性を主張し、後のイスラーム文化の多元性を方向づけた。",
    "background": "アラブ人征服支配下の非アラブ・ムスリム（マワーリー）の社会的上昇が論争を生んだ。",
    "development": "現代の脱植民地主義文学批評にも比較対象として参照される。",
    "historical_context": "イスラーム文明の多民族性と単一性の緊張を文学的に表象した。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Shu%27ubiyya",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アトラール（廃墟詩）",
    "name_en": "talal / atlal",
    "name_original": "أطلال",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "去った愛人の野営跡（廃墟）の前に立ち止まり過去を回想するナスィーブの定型場面。ジャーヒリーヤ詩学の中核トポスであり、時間・喪失・記憶の文学的形象として千年以上継承された。20世紀ウンム・クルスーム歌唱の『アトラール』が現代的再生を果たした。",
    "background": "遊牧民の移動生活において野営跡が記憶の物質的指標となった。",
    "development": "アンダルス都市哀歌、近代パレスチナ・ナクバ詩へとトポスが転用された。",
    "historical_context": "アラブ詩学の時間意識・喪失感の根源的形象。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Atlal",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "フトゥウワ（騎士道）",
    "name_en": "futuwwa",
    "name_original": "فتوة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "「青年性」「寛大」「義侠」を意味し、寛容・勇気・自己犠牲を徳目とする倫理体系。アッバース朝以降、都市職人組合・スーフィー集団・若者集団に広がり、文学の英雄像（'Antarのような騎士的人物）の倫理的核となった。",
    "background": "イスラーム都市文化の組合的連帯と義侠倫理が結合して制度化した。",
    "development": "ナギーブ・マフフーズ『Awlad Haratina（我らが街路の子たち）』にも近代変奏として登場する。",
    "historical_context": "アラブ・イスラーム文学の倫理的英雄観の中核。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Futuwwa",
    "primary_source_type": "Wikipedia",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ズフド（禁欲詩）",
    "name_en": "zuhd",
    "name_original": "زهد",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "現世放擲・死の想起・来世志向を主題とする宗教的禁欲詩のジャンル。8世紀のアブー・ル＝アターヒヤが創始者とされ、宮廷詩の華麗さに対する批判的対抗詩として確立した。後のスーフィー文学への準備段階となった。",
    "background": "アッバース朝の物質的繁栄に対する宗教的批判が詩形式を生んだ。",
    "development": "アル＝マアッリーの懐疑的禁欲詩へと哲学的に深化した。",
    "historical_context": "アラブ詩の世俗性に対する宗教的対抗運動を象徴する。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Abu_al-Atahiyya",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "タサウウフ文学（スーフィー文学）",
    "name_en": "Sufi literature",
    "name_original": "أدب الصوفية",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "イスラーム神秘主義の体験を詩・散文で表現する文学。ラービア、アル＝ハッラージ、イブン・アラビー、イブン・アル＝ファーリドらによって発展し、神への愛・合一・消失（fana）を象徴詩で描いた。ペルシア語スーフィー詩（ルーミー、ハーフィズ）と相互作用しつつアラブ世界全体に深い影響を残した。",
    "background": "9世紀以降の禁欲運動が神秘的内面化を経て独自の文学を生んだ。",
    "development": "現代アラブ詩人アドニスのスーフィー批評にも継承される。",
    "historical_context": "アラブ・イスラーム文学の精神的深層を担う。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Sufi_poetry",
    "primary_source_type": "Wikipedia / shamela.ws (Ibn al-Farid PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ファフル（自賛詩）",
    "name_en": "fakhr",
    "name_original": "فخر",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "詩人自身または部族の武勲・寛容・血統を誇示する自賛詩のジャンル。マディーフ（他者賛歌）と対をなし、カスィーダの一部または独立詩として用いられた。アル＝ムタナッビーの自賛詩は古典文学史上の頂点とされる。",
    "background": "部族社会の名誉文化が詩的自己提示の制度を生んだ。",
    "development": "ナフダ期以降、近代的自意識の表現へと転回された。",
    "historical_context": "アラブ詩における自我表現の最古の様式。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Al-Mutanabbi",
    "primary_source_type": "Wikipedia / shamela.ws (Mutanabbi PD)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "イルド（名誉）",
    "name_en": "ird",
    "name_original": "عرض",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ジャーヒリーヤ期",
    "definition": "個人と家族・部族の名誉概念で、女性の貞節と男性の保護義務に結びつく。アラブ詩・物語の倫理的中軸であり、ヒジャーは敵のイルドへの攻撃を、ファフルは自己のイルドの誇示を機能とした。",
    "background": "部族社会の連帯と血讐の論理が名誉概念を制度化した。",
    "development": "現代アラブ小説（タイイブ・サーリフ等）でも家族名誉は中心テーマとなる。",
    "historical_context": "アラブ文化の道徳的核心の一つ。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Honor_in_Arab_culture",
    "primary_source_type": "Wikipedia",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ディーワーン（詩集）",
    "name_en": "diwan",
    "name_original": "ديوان",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "アッバース朝古典期",
    "definition": "個人または時代の詩を集成した詩集形式。元来は行政台帳を意味したが、9世紀以降は詩人の全作品集の意となり、アル＝ムタナッビー、アブー・ヌワース、ブフトゥリーらの『ディーワーン』として継承された。アラブ詩の伝承単位。",
    "background": "詩の口承伝承が文字化・編纂を経て個人詩集として制度化した。",
    "development": "ゲーテ『西東詩集（West-östlicher Divan）』が西欧にこの語を導入した。",
    "historical_context": "アラブ詩の伝承と正典化の主要装置。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Diwan_(poetry)",
    "primary_source_type": "Wikipedia / shamela.ws",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — ナフダ以降近代 (8)
# ===============================================================

add({
    "name_ja": "ナフダ（復興運動）",
    "name_en": "nahda",
    "name_original": "نهضة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ナフダ期（近代復興）",
    "definition": "19世紀後半から20世紀初頭にかけてのアラブ世界の文学的・知的復興運動。ナポレオンのエジプト遠征（1798）、印刷技術導入、西欧文学翻訳、新聞創刊が結合し、古典文学の復興と新ジャンル（小説・短編・自由詩・演劇）の導入を同時に推進した。",
    "background": "オスマン帝国衰退と植民地接触のなかでアラブ近代意識が形成された。",
    "development": "20世紀の自由詩運動・iltizam（コミットメント文学）の前提条件を整えた。",
    "historical_context": "アラブ文学の古典/近代の分水嶺。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Nahda",
    "primary_source_type": "Wikipedia",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "リワーヤ（小説）",
    "name_en": "riwaya",
    "name_original": "رواية",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ナフダ期（近代復興）",
    "definition": "ナフダ期に西欧小説の翻訳・翻案を経て誕生した近代散文ジャンル。ジュルジー・ザイダーンの歴史小説、ムハンマド・フサイン・ハイカル『ザイナブ』（1913、最初のエジプト小説とされる）から、ナギーブ・マフフーズの三部作（1956-57）でアラブ小説は世界文学に到達した（1988年ノーベル文学賞）。",
    "background": "ナフダ期の翻訳運動と新聞連載文化が小説受容の土壌となった。",
    "development": "現代アラブ女性作家（ハナーン・アッ＝シャイフ、アフラム・ムスタガーニミー）へと多元化した。",
    "historical_context": "アラブ文学の近代性の中心ジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Arabic_literature#Modern",
    "primary_source_type": "Wikipedia",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "キッサ・カスィーラ（短編小説）",
    "name_en": "qissa qasira",
    "name_original": "قصة قصيرة",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "現代アラブ文学期",
    "definition": "近代アラブ短編小説のジャンル。マフムード・タイムールが先駆者となり、ユースフ・イドリースが社会主義的写実主義の頂点を築いた。マカーマ・ハバル等の古典短形式と西欧短編（モーパッサン、チェーホフ）の交差から成立した。",
    "background": "新聞・雑誌文化が短編形式の発表媒体を提供した。",
    "development": "ザカリア・ターミルらシリア前衛が寓話的短編へと展開した。",
    "historical_context": "アラブ近代文学の社会批判的中核形式。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Yusuf_Idris",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "カスィーダ・ナスル（散文詩）",
    "name_en": "qasidat al-nathr",
    "name_original": "قصيدة النثر",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "現代アラブ文学期",
    "definition": "1960年代以降、ベイルート誌『シウル』を中心にユースフ・アル＝ハール、アドニス、ウンスィー・アル＝ハージュらが提唱した自由形式の詩。古典韻律と脚韻の双方を放棄し、ボードレール／ランボーの散文詩に着想を得つつアラブ詩の境界を拡張した。",
    "background": "自由詩運動を超える形式革命の必要が前衛詩誌から提起された。",
    "development": "現代アラブ詩の主流形式の一つとして定着した。",
    "historical_context": "アラブ詩の形式的近代性の最終段階。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Adunis",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シウル・フッル（自由詩）",
    "name_en": "shi'r hurr",
    "name_original": "شعر حر",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "現代アラブ文学期",
    "definition": "1947年バグダードのナーズィク・アル＝マラーイカとバドル・シャーキル・アッ＝サイヤーブが先導した近代詩運動で、伝統的16韻律と単一脚韻の制約を解体し、行ごとに変動する韻脚と自由な行長を採用した。アラブ詩史上最大の形式革命。",
    "background": "T.S.エリオットなど英米モダニズムの受容と古典詩への閉塞感が運動を生んだ。",
    "development": "現代アラブ詩の主要形式となり、世界文学への参入を可能にした。",
    "historical_context": "1500年続いた古典詩規範の決定的転換点。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Free_verse#Arabic_free_verse",
    "primary_source_type": "Wikipedia",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "マスラフ（演劇）",
    "name_en": "masrah",
    "name_original": "مسرح",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "ナフダ期（近代復興）",
    "definition": "ナフダ期に西欧演劇の翻訳・翻案を経て成立した近代演劇ジャンル。マールーン・アン＝ナッカーシュ（1847）が嚆矢とされ、20世紀にトーフィーク・アル＝ハキームが哲学的劇作を、サアドゥッラー・ワンヌースが政治劇を確立した。古典アラブ文化に演劇伝統が乏しいため近代輸入ジャンルとされる。",
    "background": "古典イスラーム文化に偶像表象忌避があり演劇は周縁的だった。",
    "development": "ベイルート・カイロ・ダマスカスを中心に独自の政治劇伝統が形成された。",
    "historical_context": "アラブ近代化における西欧文化受容の象徴的ジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Arabic_theatre",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ナクド（批評）",
    "name_en": "naqd",
    "name_original": "نقد",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "現代アラブ文学期",
    "definition": "古典バラーガから連続する文学批評の伝統と、20世紀の西欧批評理論受容が交差する近代批評ジャンル。タハ・フサイン『ジャーヒリーヤ詩について』（1926）が古典正典への実証主義的疑義を呈し、アラブ近代批評の起点となった。アドニス『定常と変動』が伝統批評の集大成を提示した。",
    "background": "古典バラーガと近代西欧批評（マルクス主義・構造主義）の対話から発達した。",
    "development": "脱構築・ポストコロニアル批評（エドワード・サイード）と接続した。",
    "historical_context": "アラブ近代知の自己反省の核となるジャンル。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Taha_Hussein",
    "primary_source_type": "Wikipedia",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "イルティザーム（コミットメント文学）",
    "name_en": "iltizam",
    "name_original": "التزام",
    "original_script": "arabic",
    "subfield_code": "lit_arabic",
    "region": "南西アジア",
    "period_key": "現代アラブ文学期",
    "definition": "サルトルの「エンガジュマン」を翻訳概念として受容したアラブ・コミットメント文学運動。1948年パレスチナ喪失（ナクバ）以降、ベイルート誌『アル＝アーダーブ』（スハイル・イドリス創刊）を中心に、文学者の社会的・政治的責任を文学創造の前提とする立場を確立した。",
    "background": "ナクバの衝撃と冷戦下のアラブ社会主義運動が文学の政治化を促した。",
    "development": "ガッサーン・カナファーニー、マフムード・ダルウィーシュらパレスチナ抵抗文学を生んだ。",
    "historical_context": "現代アラブ文学の倫理的・政治的核を形成した概念。",
    "primary_source_url": "https://en.wikipedia.org/wiki/Suheil_Idris",
    "primary_source_type": "Wikipedia",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})


# ---------------------------------------------------------------
# Fourth-transform tagging (12-15 entries)
# ---------------------------------------------------------------
# Maps name_ja -> list of {axis, status, rationale, ai_phenomenon}
FOURTH_TRANSFORM_TAGS = {
    "シウル・フッル（自由詩）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "1500年続いた古典韻律と単一脚韻を放棄しアラブ詩の言語形式を再構築した自由詩運動は、AIによる多言語生成・形式自由化と構造的に類比される。",
         "ai_phenomenon": "LLMによる形式拘束を伴わない多言語詩生成"},
    ],
    "ナフダ（復興運動）": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "印刷技術導入と翻訳運動を通じてアラブ文学の正典・ジャンル体系を再構築したナフダは、AI時代の翻訳・受容の再編と構造的に類比される。",
         "ai_phenomenon": "AI翻訳による文学受容の地球規模再編"},
    ],
    "イルティザーム（コミットメント文学）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "文学者の社会的責任を主体性の核に据えたiltizam概念は、生成AI時代の作家主体・責任所在の再考と直接接続する。",
         "ai_phenomenon": "AI生成テクストの作者責任・倫理問題"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「コミットメント」がテクストの真正性を主体の政治的姿勢に置く点は、AI生成テクストの真正性論争と構造的に対応する。",
         "ai_phenomenon": "AI生成コンテンツの真正性・人間性の問い"},
    ],
    "マカーマ": [
        {"axis": "物語", "status": "rethinking",
         "rationale": "押韻散文と詩を交互配する形式実験的物語構造は、AI生成インタラクティブテクストの形式実験と類比される。",
         "ai_phenomenon": "AI生成のハイブリッド形式テクスト"},
    ],
    "千夜一夜物語": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "ガラン仏訳経由の西欧オリエンタリズム的受容を経た複層的テクスト史は、AI時代の文化的翻訳・誤訳・再正典化の問題系と直接接続する。",
         "ai_phenomenon": "AI翻訳による文化的他者表象の再編"},
    ],
    "バラーガ（雄弁術）": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "状況適合性を核とする修辞学体系balaghaは、AI時代の文脈適応的言語生成（プロンプト・状況応答）の理論的先駆として再評価される。",
         "ai_phenomenon": "LLMの状況依存的修辞生成"},
    ],
    "カスィーダ・ナスル（散文詩）": [
        {"axis": "言語", "status": "partial",
         "rationale": "古典韻律の完全放棄により詩と散文の境界を曖昧化した散文詩は、AI生成テクストにおけるジャンル境界の流動化と部分的に類比される。",
         "ai_phenomenon": "AI生成テクストのジャンル横断性"},
    ],
    "アダブ（教養文学）": [
        {"axis": "正典", "status": "partial",
         "rationale": "教養人の必須知識を網羅する百科全書的アダブ概念は、LLMが事実上の「全教養」を内蔵する現代において正典概念の再考を要請する。",
         "ai_phenomenon": "LLMの百科全書的知識内蔵と正典の機能変容"},
    ],
    "ナクド（批評）": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "タハ・フサインのジャーヒリーヤ詩懐疑論は実証的作者同定問題を提起し、現代のAI生成テクスト・スタイロメトリーによる作者推定論と直接接続する。",
         "ai_phenomenon": "AI援用スタイロメトリーによる作者推定"},
    ],
    "シューウービーヤ（民族意識論争）": [
        {"axis": "正典", "status": "partial",
         "rationale": "アラブ中心主義的正典観への民族多元主義的反論は、AI時代のグローバル文学正典の再構築論議に部分的に対応する。",
         "ai_phenomenon": "AI翻訳によるグローバル正典の多元化"},
    ],
    "タサウウフ文学（スーフィー文学）": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "神秘的合一・主体消失（fana）の文学的表現は、AI生成における主体性の希薄化・分散化と存在論的に類比される。",
         "ai_phenomenon": "AI生成テクストにおける主体性の分散"},
    ],
    "ディーワーン（詩集）": [
        {"axis": "正典", "status": "partial",
         "rationale": "個人詩集の編纂が詩人の正典化を担う伝統的装置は、AI時代のコーパス学習・正典再生産機構と部分的に類比される。",
         "ai_phenomenon": "AI訓練コーパスにおける正典再生産"},
    ],
    "リワーヤ（小説）": [
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "西欧小説の翻訳・翻案を起点とするアラブ小説の成立史は、AI翻訳が新たな文学ジャンル形成を加速する現代に再帰的に対応する。",
         "ai_phenomenon": "AI翻訳による新興地域文学の生成"},
    ],
    "アトラール（廃墟詩）": [
        {"axis": "物語", "status": "invariant"},
    ],
}


# ---------------------------------------------------------------
# Cross-domain links (>= 8)
# ---------------------------------------------------------------
# (lit_concept_name_ja, target_db, link_type, target_entity_name, description)
CROSS_DOMAIN_LINKS = [
    ("バラーガ（雄弁術）", "PT", "shared_concept", "rhetoric / poetics",
     "アラブ修辞学balaghaは古代ギリシャ修辞学・西欧詩学と並ぶ独立した修辞理論伝統で、状況適合性を中核とする点で独自性をもつ。"),
    ("バヤーン（明示論）", "PT", "parallel", "trope theory",
     "比喩・隠喩・換喩を中心とする比喩理論は西欧文学理論の比喩論と並行的に発展した。"),
    ("マアーニー（意味論）", "PT", "parallel", "stylistics",
     "ジュルジャーニーのナズム理論は西欧文体論・統語論的詩学と理論的に並行する。"),
    ("タサウウフ文学（スーフィー文学）", "PHIL", "shared_concept", "Sufi philosophy / Ibn Arabi",
     "イブン・アラビーらのスーフィー文学はイスラーム神秘主義哲学と一体に発展し、哲学DBと共有される。"),
    ("シューウービーヤ（民族意識論争）", "PHIL", "shared_concept", "ethnic identity / cosmopolitanism",
     "アラブ人/非アラブの平等を主張するshu'ubiyya論争はイスラーム哲学のエスニシティ論と直接接続する。"),
    ("カスィーダ", "AN", "shared_concept", "oral tradition / Bedouin culture",
     "ベドウィン口承詩学は人類学的口承伝承研究の主要対象であり、人類学DBと共有される。"),
    ("シウル・フッル（自由詩）", "AI-Development", "parallel", "LLM multilingual generation",
     "古典韻律放棄の自由詩運動はLLMの形式拘束を超えた多言語詩生成と歴史的に類比される。"),
    ("ナフダ（復興運動）", "AI-Development", "parallel", "LLM and translation revival",
     "印刷・翻訳による文学復興のナフダは、AI翻訳による現代の地域文学復興と構造的に類比される。"),
    ("千夜一夜物語", "Myth-Narratives", "shared_concept", "frame narrative / Scheherazade",
     "枠物語形式と説話集積構造は神話・物語DBと直接共有される世界文学的素材。"),
    ("ムアッラカート（懸詩）", "AN", "shared_concept", "oral canon formation",
     "ウカーズ詩市での選定と正典化は人類学的口承正典形成の代表事例として共有される。"),
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

        print(f"\n=== C21 Arabic completed ===")
        print(f"  concepts inserted: {inserted} (skipped: {skipped})")
        print(f"  fourth-transform tags: {ft_count}")
        print(f"  cross-domain links: {cd_count}")
        print(f"  total concepts in subfield 13: ", end="")
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 13"
        ).fetchone()
        print(row["c"])


if __name__ == "__main__":
    main()
