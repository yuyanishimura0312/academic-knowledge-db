"""LIT-DB Phase 2 Wave 22 — C38 ADD: World Lit / Translation theory (+80).

Subfield: lit_world_translation (id=23). Existing 140. Target 500.
Adds 80 NEW non-overlapping concepts covering:
 A: 翻訳論深化 (12)
 B: 異文化翻訳・翻訳家エッセイ (14)
 C: 機械翻訳論 (16)
 D: 翻訳と権力 (8)
 E: 翻訳教育・規格 (8)
 F: 翻訳作品史・名訳 (10)
 G: 比較・世界文学方法論 (6)
 H: プロフェッショナル組織・翻訳賞 (6)

fourth_axes >= 30, cross_domain to PT/PHIL/AN >= 22.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("構造主義・記述的翻訳学期", "Structuralist & Descriptive Translation Studies",
     1950, 1990, None),
    ("世界文学・ポストコロニアル翻訳期", "World Literature & Postcolonial Translation",
     1990, 2030, None),
    ("比較文学形成期", "Formation of Comparative Literature", 1800, 1950, None),
]


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
ARXIV = "https://arxiv.org/abs/"
ACL = "https://aclanthology.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_world_translation", region="理論",
         original_script="roman")


# ============================================================
# A: 翻訳論深化 (12)
# ============================================================
add(**C, name_ja="ベルマン『翻訳批評に向けて』",
    name_en="Berman, Toward a Translation Criticism",
    name_original="Pour une critique des traductions: John Donne",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1995年アントワーヌ・ベルマン遺著、ジョン・ダンの仏訳を題材に翻訳批評の方法論を体系化。翻訳者の「立場」「企て」「地平」を分析する三段階モデルと「変形傾向（déformantes）」12類型を提示した翻訳批評論の決定版。",
    background="ベルマン『他者の試練』の方法論的継承と、文学翻訳批評の制度化要求。",
    development="フランス翻訳学の中核理論、メショニック詩学的翻訳論との対話。",
    historical_context="1990年代仏語圏翻訳学の理論的成熟期。",
    primary_source_url=WIKI_FR+"Antoine_Berman",
    primary_source_type="Wikipedia(fr): Antoine Berman",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ベルマンの12変形傾向はAI翻訳の系統的バイアス分析の理論的基盤。",
        "related_ai_phenomenon":"AI翻訳の系統的バイアス検出"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"解釈学的批評",
        "description":"ベルマン翻訳批評はリクール解釈学の文学翻訳論的展開。"}])

add(**C, name_ja="メショニック『翻訳の詩学』",
    name_en="Meschonnic, Poétique du traduire",
    name_original="Poétique du traduire",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1999年アンリ・メショニック著、翻訳を意味伝達ではなくリズム（rythme）の移行として捉える詩学的翻訳論。聖書翻訳実践に基づき、語の単位ではなく「言述（discours）」全体の運動を翻訳対象とする。",
    background="メショニック自身のヘブライ語聖書仏訳実践と、フランス詩学運動。",
    development="リトモロジー（韻律論）翻訳学、現代仏語圏翻訳詩学の中核。",
    historical_context="1990年代後半フランス翻訳学のロマン主義的詩学回帰。",
    primary_source_url=WIKI_FR+"Henri_Meschonnic",
    primary_source_type="Wikipedia(fr): Henri Meschonnic",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"リズム中心の翻訳論はLLM翻訳が苦手とする音律・呼吸の理論的基盤。",
        "related_ai_phenomenon":"LLM翻訳のリズム喪失問題"}],
    cross_domain=[{"target_db":"PT","link_type":"shared_concept",
        "target_entity_name":"リズム詩学",
        "description":"メショニック翻訳論はリズムを詩学の中心に置く理論の翻訳学的展開。"}])

add(**C, name_ja="ラドミラル『翻訳のための定理』",
    name_en="Ladmiral, Théorèmes pour la traduction",
    name_original="Théorèmes pour la traduction",
    period_key="構造主義・記述的翻訳学期",
    definition="1979年ジャン=ルネ・ラドミラル著、翻訳学を「翻訳論（traductologie）」として制度化した先駆的著作。「源泉派（sourciers）」と「目標派（ciblistes）」の対立軸を導入、仏語圏翻訳学の方法論的基盤を確立した。",
    background="フランス哲学翻訳実践（ハーバマス、フロイト等）と、応用言語学の隆盛。",
    development="ベルマン、メショニック、ピムらの翻訳学への直接影響、用語「traductologie」の定着。",
    historical_context="1970年代末仏語圏翻訳学の制度化期。",
    primary_source_url=WIKI_FR+"Jean-Ren%C3%A9_Ladmiral",
    primary_source_type="Wikipedia(fr): Jean-René Ladmiral",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーマンス『システムにおける翻訳』",
    name_en="Hermans, Translation in Systems",
    name_original="Translation in Systems: Descriptive and System-oriented Approaches Explained",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1999年テオ・ハーマンス著、ポリシステム理論・記述的翻訳学・規範研究を統合的に解説した翻訳学方法論の標準テクスト。トゥーリの規範論を発展させ、翻訳者の「声」と擬似翻訳問題を理論化した。",
    background="マニピュレーション学派の主導、ポリシステム理論の英語圏受容。",
    development="記述的翻訳学の標準教科書、翻訳者の声論議の出発点。",
    historical_context="1990年代末ロー・カントリー翻訳学の総合期。",
    primary_source_url=WIKI_EN+"Theo_Hermans_(translation_studies)",
    primary_source_type="Wikipedia: Theo Hermans",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ピム『翻訳史の方法』",
    name_en="Pym, Method in Translation History",
    name_original="Method in Translation History",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1998年アンソニー・ピム著、翻訳史研究の方法論を体系化した先駆的著作。翻訳者を社会的アクターとして中心化し、相互文化（interculture）概念で文化間翻訳を分析する歴史記述論。",
    background="ピムのスペイン語圏翻訳史研究と、社会学的翻訳学の萌芽。",
    development="社会学的翻訳学、翻訳者研究、翻訳史方法論の標準。",
    historical_context="1990年代末翻訳史研究の方法論的成熟期。",
    primary_source_url=WIKI_EN+"Anthony_Pym",
    primary_source_type="Wikipedia: Anthony Pym",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"相互文化分析",
        "description":"ピムの相互文化概念は人類学的境界研究と並行的に発展。"}])

add(**C, name_ja="ヴェヌーティ『翻訳のスキャンダル』",
    name_en="Venuti, The Scandals of Translation",
    name_original="The Scandals of Translation: Towards an Ethics of Difference",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1998年ローレンス・ヴェヌーティ著、翻訳が文化的・経済的・著作権的に周縁化されるスキャンダルを暴露し、「差異の倫理」を提唱。翻訳者著作権、英米中心主義、文学正典形成への翻訳の影響を批判的に分析。",
    background="『翻訳者の不可視性』の続編、米国出版産業の翻訳忌避への批判。",
    development="翻訳倫理論、翻訳者著作権論争、ポスト『不可視性』翻訳学の中核。",
    historical_context="1990年代末英語圏翻訳産業批判の高揚期。",
    primary_source_url=WIKI_EN+"Lawrence_Venuti",
    primary_source_type="Wikipedia: Lawrence Venuti",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"翻訳のスキャンダル論はAI翻訳の経済的非対称・著作権問題の批判的基盤。",
        "related_ai_phenomenon":"AI翻訳の著作権・経済的問題"}])

add(**C, name_ja="ヴェヌーティ『翻訳学リーダー』",
    name_en="Venuti, The Translation Studies Reader",
    name_original="The Translation Studies Reader",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2000/2012/2021年ローレンス・ヴェヌーティ編、翻訳学の代表論文集。キケロからベルマン・スピヴァクまで翻訳論の正典を編纂、世代別に翻訳学のパラダイム転換を一覧化した世界翻訳学教育の標準テクスト。",
    background="米国大学院翻訳学プログラムの教科書需要と、ヴェヌーティの編纂能力。",
    development="3版改訂を経て世界翻訳学教育の標準、翻訳学正典化の中軸。",
    historical_context="2000年代翻訳学制度化期の正典形成。",
    primary_source_url=WIKI_EN+"Lawrence_Venuti",
    primary_source_type="Wikipedia: Lawrence Venuti",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴェヌーティ『道具主義に抗して』",
    name_en="Venuti, Contra Instrumentalism",
    name_original="Contra Instrumentalism: A Translation Polemic",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2019年ローレンス・ヴェヌーティ著、翻訳を「等価性」モデルで考える「道具主義」を批判し、解釈的・差異的翻訳論を擁護する論争書。AI翻訳・機械翻訳が前提する道具主義観への根源的批判。",
    background="2010年代AI翻訳の隆盛と、それに対する人文学的反論の必要性。",
    development="2020年代AI翻訳論議の批判的基盤、ヴェヌーティ後期翻訳哲学の集大成。",
    historical_context="2010年代末NMT/LLM翻訳普及期の人文学的応答。",
    primary_source_url=WIKI_EN+"Lawrence_Venuti",
    primary_source_type="Wikipedia: Lawrence Venuti",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"道具主義批判はLLM翻訳の前提を根本から問い直す現代翻訳哲学。",
        "related_ai_phenomenon":"LLM翻訳の道具主義的前提"}])

add(**C, name_ja="ベイカー『他のことばで』",
    name_en="Baker, In Other Words",
    name_original="In Other Words: A Coursebook on Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1992/2018年モナ・ベイカー著、コーパス言語学・機能言語学に基づく翻訳実務の教科書。語彙・文法・テクスト・語用論の各レベルでの等価性問題を体系的に扱う、世界翻訳学教育の定番。",
    background="ベイカー自身のアラビア語英訳実践とコーパス翻訳学の創始。",
    development="3版改訂を経て翻訳実務教育の世界標準、コーパス翻訳学の出発点。",
    historical_context="1990年代翻訳実務教育の制度化期。",
    primary_source_url=WIKI_EN+"Mona_Baker",
    primary_source_type="Wikipedia: Mona Baker",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ノード『翻訳のためのテクスト分析』",
    name_en="Nord, Text Analysis in Translation",
    name_original="Textanalyse und Übersetzen",
    period_key="構造主義・記述的翻訳学期",
    definition="1988/2005年クリスティアーネ・ノード著、機能主義翻訳論の実践教科書。「翻訳指示（translation brief）」概念を中心に、原文分析と目標テクスト設計を方法論化。スコポス理論の実務応用版。",
    background="ライス・フェアメーアのスコポス理論の応用化要求。",
    development="機能主義翻訳教育の標準、産業翻訳・ローカリゼーション教育の理論基盤。",
    historical_context="1980年代末ドイツ語圏応用翻訳学の成熟期。",
    primary_source_url=WIKI_EN+"Christiane_Nord",
    primary_source_type="Wikipedia: Christiane Nord",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スネル=ホーンビー『翻訳学・統合的接近』",
    name_en="Snell-Hornby, Translation Studies: An Integrated Approach",
    name_original="Translation Studies: An Integrated Approach",
    period_key="構造主義・記述的翻訳学期",
    definition="1988/1995年メアリ・スネル=ホーンビー著、文学翻訳と特殊目的翻訳の二分法を超え、原型理論（prototype theory）に基づく統合的翻訳学を提唱。ドイツ語圏翻訳学の総合化を代表する著作。",
    background="ヴィーン応用翻訳学派の理論的基盤、認知意味論の翻訳学への応用。",
    development="EST（欧州翻訳学会）の設立基盤、『翻訳学の諸転回』(2006)に発展。",
    historical_context="1980年代末欧州翻訳学の制度的統合期。",
    primary_source_url=WIKI_EN+"Mary_Snell-Hornby",
    primary_source_type="Wikipedia: Mary Snell-Hornby",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バスネット=ルフェーヴル『翻訳・歴史・文化』",
    name_en="Bassnett & Lefevere, Translation, History, and Culture",
    name_original="Translation, History, and Culture",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1990年スーザン・バスネット＆アンドレ・ルフェーヴル編、翻訳学の「文化的転回（cultural turn）」を宣言した論集。等価性・忠実性議論から、翻訳をイデオロギー・パトロネージ・詩学の交渉として捉える文化研究的展開を確立。",
    background="ポリシステム理論、フーコー権力論、カルチュラル・スタディーズの合流。",
    development="文化的転回の宣言文書として、ポストコロニアル翻訳・社会学的翻訳学の出発点。",
    historical_context="冷戦終結期の翻訳学パラダイム転換。",
    primary_source_url=WIKI_EN+"Susan_Bassnett",
    primary_source_type="Wikipedia: Susan Bassnett",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"文化的転回",
        "description":"翻訳学の文化的転回は人類学のwriting culture論議と同期した知的運動。"}])


# ============================================================
# B: 異文化翻訳・翻訳家エッセイ (14)
# ============================================================
add(**C, name_ja="グロスマン『なぜ翻訳が重要か』",
    name_en="Grossman, Why Translation Matters",
    name_original="Why Translation Matters",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2010年エディス・グロスマン著、英訳『ドン・キホーテ』(2003)で名高い翻訳家のエッセイ。翻訳を「読みの最深の形態」と定義し、英米出版業界の翻訳忌避を批判、世界文学のための翻訳の必然性を訴えた。",
    background="グロスマン自身のセルバンテス・ガルシア=マルケス英訳実践。",
    development="2010年代英語圏翻訳家エッセイの先駆、出版業界の翻訳意識改革に貢献。",
    historical_context="2010年代英語圏世界文学読書運動の立ち上がり期。",
    primary_source_url=WIKI_EN+"Edith_Grossman",
    primary_source_type="Wikipedia: Edith Grossman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パークス『翻訳のスタイル』",
    name_en="Parks, Translating Style",
    name_original="Translating Style: A Literary Approach to Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1997/2007年ティム・パークス著、英伊翻訳実践に基づく文体論的翻訳論。ロレンス・ジョイス・ウルフ等のイタリア語訳を分析、文体の翻訳可能性を実例で論じる。",
    background="パークスのイタリア在住翻訳実践と、英文学のイタリア語訳問題。",
    development="文体翻訳論の標準テクスト、翻訳教育の定番。",
    historical_context="1990年代末英伊文学翻訳の理論化期。",
    primary_source_url=WIKI_EN+"Tim_Parks",
    primary_source_type="Wikipedia: Tim Parks",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベルノフスキー『ヴァルザー伝』",
    name_en="Bernofsky, Clairvoyant of the Small (Walser)",
    name_original="Clairvoyant of the Small: The Life of Robert Walser",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2021年スーザン・ベルノフスキー著、ローベルト・ヴァルザー英訳者による評伝。長年のヴァルザー独英翻訳経験から、翻訳家による作家論の可能性を示す。翻訳家=研究者の現代的成熟形。",
    background="ベルノフスキーのヴァルザー・カフカ翻訳実践と、コロンビア大翻訳教育。",
    development="翻訳家による作家評伝という新ジャンル、翻訳研究の制度的成熟。",
    historical_context="2020年代翻訳家の作家研究的成熟期。",
    primary_source_url=WIKI_EN+"Susan_Bernofsky",
    primary_source_type="Wikipedia: Susan Bernofsky",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クロフト『階級』『ヴォイスオーバー』",
    name_en="Croft, Class and Voiceover",
    name_original="Homesick / The Extinction of Irena Rey",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ジェニファー・クロフト（オルガ・トカルチュク英訳者、2018年マン・ブッカー国際賞）の創作と翻訳論。『The Extinction of Irena Rey』(2024)は翻訳家7人を主人公とする小説で、翻訳家の不可視性・連帯・著作権を扱う。",
    background="クロフトの#NameTheTranslator運動と、トカルチュク翻訳経験。",
    development="2020年代翻訳家アクティビズムの代表、翻訳家小説という新ジャンル。",
    historical_context="2020年代翻訳家可視化運動の高揚期。",
    primary_source_url=WIKI_EN+"Jennifer_Croft",
    primary_source_type="Wikipedia: Jennifer Croft",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"#NameTheTranslator運動はAI翻訳時代の翻訳者著作権・可視化議論の出発点。",
        "related_ai_phenomenon":"AI時代の翻訳者著作権"}])

add(**C, name_ja="アントン・ホー（韓国語翻訳）",
    name_en="Anton Hur, Korean translation",
    name_original="Cursed Bunny, Love in the Big City (translations)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アントン・ホーは韓国語英訳者・作家。チョン・ボラ『呪いのうさぎ』(2022)とパク・サンヨン『大都市の愛し方』(2022)が同年マン・ブッカー国際賞ロングリスト入選、韓国文学のグローバル化の中核翻訳者。",
    background="K文学グローバル化（『菜食主義者』『パチンコ』等）の波、KLTI（韓国文学翻訳院）支援。",
    development="2020年代韓国文学英訳ブームの代表的翻訳者、翻訳家の作家化。",
    historical_context="2020年代韓流文学世界化期。",
    primary_source_url=WIKI_EN+"Anton_Hur",
    primary_source_type="Wikipedia: Anton Hur",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゴールドスタイン（フェランテ英訳）",
    name_en="Goldstein, Ferrante translations",
    name_original="My Brilliant Friend etc. (translations)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アン・ゴールドスタインはニューヨーカー誌編集者、エレナ・フェランテ『ナポリ四部作』英訳者。2010-2010年代の英訳が世界的フェランテ・フィーバーの中核となり、隠れた著者と可視的翻訳者という稀な構造を作った。",
    background="フェランテの匿名作家政策と、ナポリ四部作の英米市場成功。",
    development="2010年代英語圏翻訳家可視化の代表事例、翻訳者ブランディングの先駆。",
    historical_context="2010年代世界文学翻訳の英米市場拡大期。",
    primary_source_url=WIKI_EN+"Ann_Goldstein_(translator)",
    primary_source_type="Wikipedia: Ann Goldstein (translator)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジュル・コスタ（サラマーゴ・リスペクトール）",
    name_en="Jull Costa, Saramago/Lispector translations",
    name_original="The Notebooks of Lispector etc.",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マーガレット・ジュル・コスタはポルトガル語・スペイン語英訳者。サラマーゴ、ペソア、リスペクトール、ハビエル・マリアスらの英訳で、イベリア・ラテンアメリカ文学の英語圏受容を主導。",
    background="20世紀末からのポルトガル語圏文学英訳需要と、コスタの長期実践。",
    development="OBE受勲、ポルトガル語圏文学英訳の標準的翻訳者。",
    historical_context="2000年代以降のイベリア語圏文学世界化期。",
    primary_source_url=WIKI_EN+"Margaret_Jull_Costa",
    primary_source_type="Wikipedia: Margaret Jull Costa",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラヒリ『自己翻訳』",
    name_en="Lahiri, Translating Myself and Others",
    name_original="Translating Myself and Others",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2022年ジュンパ・ラヒリ著、英→伊→英の自己翻訳実践に基づくエッセイ集。インド系米国作家がイタリア語で創作し自ら英訳する経験を、亡命・所属・言語の所有権を巡る思索として展開。",
    background="ラヒリの『他の言葉で』(2015)以後のイタリア語創作期。",
    development="自己翻訳論の現代的代表、ディアスポラ翻訳論の中核。",
    historical_context="2020年代ディアスポラ作家の言語選択論議。",
    primary_source_url=WIKI_EN+"Jhumpa_Lahiri",
    primary_source_type="Wikipedia: Jhumpa Lahiri",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"自己と言語",
        "description":"ラヒリの自己翻訳論はディアスポラ的自己と言語所有権の哲学的探究。"}])

add(**C, name_ja="ブリッグス『この小さな芸術』",
    name_en="Briggs, This Little Art",
    name_original="This Little Art",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2017年ケイト・ブリッグス著、ロラン・バルト英訳実践に基づくエッセイ的翻訳論。翻訳を「小さな芸術」として再評価、翻訳実践の身体的・時間的次元を詩的に論じた現代翻訳論の名著。",
    background="ブリッグスのバルト『中性』『小説の準備』英訳実践。",
    development="2010年代後半翻訳家エッセイの代表、翻訳実践哲学の文学的展開。",
    historical_context="2010年代後半英語圏翻訳家エッセイ隆盛期。",
    primary_source_url=WIKI_EN+"Kate_Briggs",
    primary_source_type="Wikipedia: Kate Briggs",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"翻訳の身体性・時間性論はAI翻訳の即時性・脱身体性との対比軸。",
        "related_ai_phenomenon":"AI翻訳の脱身体性問題"}])

add(**C, name_ja="ヒューズ（スペイン語圏翻訳）",
    name_en="Hughes, Spanish-language translations",
    name_original="Hurricane Season etc.",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ソフィー・ヒューズはスペイン語英訳者。フェルナンダ・メルチョール『ハリケーン・シーズン』(2020)、エンリケ・ビラ=マタス、リナ・メルアンらの英訳で、現代スペイン語圏文学のグローバル化を主導。",
    background="2010-20年代ラテンアメリカ・スペイン現代文学の英語圏受容。",
    development="マン・ブッカー国際賞ロングリスト常連、若手スペイン語英訳者の代表。",
    historical_context="2020年代スペイン語圏文学英訳ブーム期。",
    primary_source_url=WIKI_EN+"Sophie_Hughes_(translator)",
    primary_source_type="Wikipedia: Sophie Hughes (translator)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エミリー・ウィルソン『オデュッセイア』『イリアス』",
    name_en="Wilson, Odyssey & Iliad translations",
    name_original="The Odyssey (2017), The Iliad (2023)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="エミリー・ウィルソンによる『オデュッセイア』(2017)『イリアス』(2023)の英訳。女性による初の主要英訳ホメロスとして話題、現代的・批判的・ジェンダー意識的訳語選択（slave等の語）が古典翻訳論議を活性化した。",
    background="ペンシルベニア大古典学者ウィルソンの長年研究と、古典翻訳のジェンダー再考要求。",
    development="2020年代古典翻訳の方法論的革新、フェミニスト古典翻訳の代表。",
    historical_context="2010-20年代古典翻訳のジェンダー的再評価期。",
    primary_source_url=WIKI_EN+"Emily_Wilson_(classicist)",
    primary_source_type="Wikipedia: Emily Wilson (classicist)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"古典翻訳のジェンダー的再考はAI翻訳の歴史的バイアス批判の理論的基盤。",
        "related_ai_phenomenon":"AI翻訳の歴史的バイアス"}])

add(**C, name_ja="ロバートソン『アエネーイス』",
    name_en="Robertson, The Aeneid",
    name_original="The Aeneid (translation 2021)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2021年ロビン・ロバートソン著、ウェルギリウス『アエネーイス』英訳。スコットランド詩人による現代詩的英訳として、フィッツジェラルド・ファグルス・ヘイニーに続く20世紀後半-21世紀古典翻訳の系譜に位置。",
    background="ロバートソンのスコットランド詩風と古典への長年の関心。",
    development="2020年代古典詩翻訳の詩人的アプローチの代表。",
    historical_context="2020年代英語詩人による古典翻訳の系譜継承期。",
    primary_source_url=WIKI_EN+"Robin_Robertson",
    primary_source_type="Wikipedia: Robin Robertson",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アン・カーソン（サッポー・アイスキュロス）",
    name_en="Anne Carson, Sappho/Aeschylus translations",
    name_original="If Not, Winter / Antigonick",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アン・カーソンの『冬でなければ』(2002・サッポー)、『アンティゴニック』(2012・ソフォクレス)等の翻訳。古典学者・詩人として、断片性・ヴィジュアル詩・実験的翻訳を駆使する翻訳=創作の最先端実践。",
    background="カーソンの古典学と現代詩の両極を結ぶ知的実践。",
    development="実験的古典翻訳の代表、翻訳=創作論の現代的頂点。",
    historical_context="2000-20年代古典翻訳の実験的展開期。",
    primary_source_url=WIKI_EN+"Anne_Carson",
    primary_source_type="Wikipedia: Anne Carson",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PT","link_type":"shared_concept",
        "target_entity_name":"古典詩学の現代化",
        "description":"カーソン翻訳実践は古典詩学を現代詩学で再活性化する翻訳=創作論。"}])

add(**C, name_ja="マデリン・ミラー（古典再話）",
    name_en="Madeline Miller, classical retellings",
    name_original="The Song of Achilles / Circe",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="マデリン・ミラー『アキレウスの歌』(2011)、『キルケ』(2018)。古典の翻訳ではなく現代小説への翻案（retelling）として、古典の現代化・ジェンダー的再解釈の代表。広義の翻訳論の射程を拡張。",
    background="2010年代古典再話小説（Madeline Miller, Pat Barker, Natalie Haynes等）ブーム。",
    development="広義翻訳としての翻案論、ジェンダー的古典再解釈の中核。",
    historical_context="2010年代古典フェミニスト再話期。",
    primary_source_url=WIKI_EN+"Madeline_Miller",
    primary_source_type="Wikipedia: Madeline Miller",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: 機械翻訳論 (16)
# ============================================================
add(**C, name_ja="IBM Model 1-5（Brown et al. 1993）",
    name_en="IBM Models 1-5 (Brown et al. 1993)",
    name_original="The Mathematics of Statistical Machine Translation",
    period_key="構造主義・記述的翻訳学期",
    definition="1993年Peter Brown, Stephen Della Pietra, Vincent Della Pietra, Robert Mercerによる統計的機械翻訳の定礎論文。語アラインメントの確率モデル5段階（Model 1-5）を提示、SMTパラダイムの数学的基盤を確立した。",
    background="IBMワトソン研究所Candide翻訳プロジェクト、シャノン情報理論の翻訳応用。",
    development="1990-2000年代SMT全盛期の理論基盤、フレーズベースSMT、統計NLPの出発点。",
    historical_context="1990年代初頭NLPのコーパス転回期。",
    primary_source_url=ACL+"J93-2003/",
    primary_source_type="ACL Anthology: Brown et al. 1993",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"IBM Modelsは確率的翻訳の数学的基盤を確立、現代NMT/LLM翻訳の理論的源流。",
        "related_ai_phenomenon":"確率的言語モデルの起源"}])

add(**C, name_ja="Och & Ney 2003（アラインメント）",
    name_en="Och & Ney 2003, Alignment Templates",
    name_original="A Systematic Comparison of Various Statistical Alignment Models",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2003年Franz Josef Och & Hermann Ney著、IBM Modelsの体系的比較とHMM拡張モデルを提示。アラインメント・テンプレート手法はGoogle Translate初期版の中核アルゴリズム、Och単独で2002-2008年Google翻訳開発を主導した。",
    background="GIZA++ツールキット、フレーズベースSMTへの移行需要。",
    development="フレーズベースSMTの基盤、Google Translate Phase 1の核心技術。",
    historical_context="2000年代SMT工業化期。",
    primary_source_url=ACL+"J03-1002/",
    primary_source_type="ACL Anthology: Och & Ney 2003",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="Koehn『統計的機械翻訳』教科書",
    name_en="Koehn, Statistical Machine Translation",
    name_original="Statistical Machine Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2009年Philipp Koehn著、SMTの標準教科書。Mosesシステム（Koehn主導開発）と並び、フレーズベースSMTの世界標準を確立。NMT登場前のSMT全盛期の集大成。",
    background="Mosesプロジェクト（2007-）と、SMT教育需要の高まり。",
    development="2010年代前半翻訳学・NLP教育の標準テクスト、SMT工学の基盤。",
    historical_context="2010年前後SMT成熟期、NMT前夜。",
    primary_source_url=WIKI_EN+"Philipp_Koehn",
    primary_source_type="Wikipedia: Philipp Koehn",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="Sutskever Seq2seq 2014",
    name_en="Sutskever et al., Sequence to Sequence Learning",
    name_original="Sequence to Sequence Learning with Neural Networks",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2014年Ilya Sutskever, Oriol Vinyals, Quoc V. Le著、LSTMを用いたエンコーダ・デコーダ機械翻訳モデルseq2seqを提示。NMTパラダイムの直接の起点で、英仏翻訳でSMTを上回る性能を達成、深層学習翻訳の幕開け。",
    background="2010年代前半深層学習隆盛、Googleの音声・画像認識成功。",
    development="GNMT(2016)、Transformer(2017)へと直結する系譜の出発点。",
    historical_context="2014年深層学習NLPの臨界点。",
    primary_source_url=ARXIV+"1409.3215",
    primary_source_type="arXiv: Sutskever et al. 2014",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"Seq2seqはNMTの直接的起点、LLM時代翻訳パラダイムの基礎。",
        "related_ai_phenomenon":"NMTパラダイムの起源"}])

add(**C, name_ja="Vaswani et al. 2017『Attention is All You Need』",
    name_en="Vaswani et al., Attention is All You Need",
    name_original="Attention is All You Need",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2017年Ashish Vaswani等Google Brain著、Transformer架構を提示。RNN・CNNなしの自己注意機構のみで機械翻訳の新最高性能を達成、BERT・GPT・現代LLM全般の基礎架構となった、NLP史上最重要論文。",
    background="バーダナウ等の注意機構2014、Googleの大規模翻訳要件。",
    development="BERT(2018)、GPT-2/3/4、Llama等全LLMの基礎、AI革命の中核論文。",
    historical_context="2017年深層学習NLPの臨界点。",
    primary_source_url=ARXIV+"1706.03762",
    primary_source_type="arXiv: Vaswani et al. 2017",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"Transformerは現代LLM翻訳の架構基盤、AI言語革命の出発点。",
        "related_ai_phenomenon":"Transformer架構によるLLM翻訳"}])

add(**C, name_ja="Wu et al. 2016 GNMT",
    name_en="Wu et al., Google's Neural Machine Translation",
    name_original="Google's Neural Machine Translation System",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2016年Yonghui Wu等Google著、Google Translate全面NMT化の技術論文。8層LSTMエンコーダ・デコーダ、wordpiece分割、量子化技術等で工業規模NMTを実現、機械翻訳産業を一変させた。",
    background="2014-15年NMT研究進展と、Google Translate品質改善要請。",
    development="2016年11月Google Translate NMT展開、産業翻訳の全面的NMT転換の起点。",
    historical_context="2016年機械翻訳産業の臨界点。",
    primary_source_url=ARXIV+"1609.08144",
    primary_source_type="arXiv: Wu et al. 2016",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="Hassan et al. 2018 中英パリティ主張",
    name_en="Hassan et al. 2018, Chinese-English Parity Claim",
    name_original="Achieving Human Parity on Chinese-English Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2018年Hany Hassan等Microsoft著、ニュース領域中英機械翻訳でhuman parityを達成と主張した論文。後のToral等(2018)による方法論的批判を呼び、MT評価の基準論議を活性化させた歴史的論争点。",
    background="2017-18年NMT性能急上昇と、産業界の人間並み主張競争。",
    development="Läubli et al. 2018, Toral & Sánchez-Cartagena 2018等の方法論批判への波及。",
    historical_context="2018年MT human parity論争期。",
    primary_source_url=ARXIV+"1803.05567",
    primary_source_type="arXiv: Hassan et al. 2018",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="BLEU（Papineni 2002）",
    name_en="BLEU (Papineni et al. 2002)",
    name_original="BLEU: a Method for Automatic Evaluation of Machine Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2002年Kishore Papineni等IBM著、機械翻訳の自動評価指標BLEU（BiLingual Evaluation Understudy）を提示。n-gram精度+brevity penaltyの合成指標で、20年以上MT評価の事実上標準として機能した史上最影響力評価指標。",
    background="MT評価の人手依存問題、IBM SMT開発における自動評価需要。",
    development="2000-2020年代MT評価の標準、後にchrF・COMET等が改良として登場。",
    historical_context="2002年MT自動評価の確立期。",
    primary_source_url=ACL+"P02-1040/",
    primary_source_type="ACL Anthology: Papineni et al. 2002",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="METEOR（Banerjee & Lavie 2005）",
    name_en="METEOR (Banerjee & Lavie 2005)",
    name_original="METEOR: An Automatic Metric for MT Evaluation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2005年Satanjeev Banerjee & Alon Lavie著、BLEUの限界（同義語・語順）を補う評価指標METEORを提示。WordNet同義語マッチング、再現率重視、人間判断との相関で BLEU を上回る性能を示した。",
    background="BLEUの単純n-gramマッチングへの批判と、改良指標の必要性。",
    development="2010年代までMT評価の標準補助指標、現代COMET等の前駆。",
    historical_context="2000年代中盤MT評価多様化期。",
    primary_source_url=ACL+"W05-0909/",
    primary_source_type="ACL Anthology: Banerjee & Lavie 2005",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="chrF（Popović 2015）",
    name_en="chrF (Popović 2015)",
    name_original="chrF: character n-gram F-score",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2015年Maja Popović著、文字n-gramベースの機械翻訳評価指標chrF。語形変化豊富な言語に強く、トークナイザ依存性が低いことから2010年代後半WMTの標準指標の一つとなった。",
    background="形態論的に複雑な言語のMT評価における語ベースn-gram指標の限界。",
    development="WMT共通タスクの標準指標、多言語MT評価の中核。",
    historical_context="2010年代中盤多言語MT評価成熟期。",
    primary_source_url=ACL+"W15-3049/",
    primary_source_type="ACL Anthology: Popović 2015",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="BERTScore（Zhang 2019）",
    name_en="BERTScore (Zhang et al. 2019)",
    name_original="BERTScore: Evaluating Text Generation with BERT",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2019年Tianyi Zhang等著、BERTの文脈埋め込みを用いた評価指標BERTScore。トークンの意味的類似度を距離で測定し、表面n-gramを超えた評価を実現、生成評価のニューラル指標時代を開いた。",
    background="2018年BERT登場と、表面マッチング評価指標の限界認識。",
    development="2020年代COMET、BLEURT等のニューラル評価指標の前駆。",
    historical_context="2019年MT評価のニューラル化期。",
    primary_source_url=ARXIV+"1904.09675",
    primary_source_type="arXiv: Zhang et al. 2019",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="COMET（Rei et al. 2020）",
    name_en="COMET (Rei et al. 2020)",
    name_original="COMET: A Neural Framework for MT Evaluation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2020年Ricardo Rei等Unbabel著、人間判断データで訓練した参照付きMT評価指標COMET。WMT 2020以降人間判断との相関で BLEU を大きく上回り、産業翻訳評価の新標準となった。",
    background="ニューラル評価指標の隆盛と、人間判断回帰モデルの成熟。",
    development="WMT 2020-23の標準指標、産業翻訳品質管理の中核。",
    historical_context="2020年代MT評価のニューラル指標標準化期。",
    primary_source_url=ARXIV+"2009.09025",
    primary_source_type="arXiv: Rei et al. 2020",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="MQM評価フレーム（Lommel 2014）",
    name_en="MQM (Lommel et al. 2014)",
    name_original="Multidimensional Quality Metrics",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2014年Arle Lommel等QTLaunchPadプロジェクト主導、翻訳品質を多次元的にカテゴリ化する評価フレーム。誤訳・語法・スタイル等の階層的エラータイポロジーで、産業翻訳・機械翻訳の品質管理標準となった。",
    background="EU QTLaunchPad/QT21プロジェクト、産業翻訳品質管理需要。",
    development="2020年代産業翻訳評価の中核、Google・Microsoft等の品質管理基盤。",
    historical_context="2010年代中盤産業翻訳品質基準化期。",
    primary_source_url=WIKI_EN+"Multidimensional_Quality_Metrics",
    primary_source_type="Wikipedia: MQM",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="MTPE（機械翻訳ポストエディット）",
    name_en="MTPE (Machine Translation Post-Editing)",
    name_original="Machine Translation Post-Editing",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="機械翻訳出力を人間が編集する翻訳実務形態。light/full PE区分、ISO 18587規格、生産性測定研究等を含む産業翻訳の主要モード。NMT普及後の翻訳産業の中核作業形態となり、翻訳職業構造を変容させた。",
    background="2010年代SMT/NMT産業普及と、産業翻訳の生産性圧力。",
    development="ISO 18587:2017規格化、2020年代翻訳産業の主流化。",
    historical_context="2010-20年代翻訳産業のMTPE転換期。",
    primary_source_url=WIKI_EN+"Postediting",
    primary_source_type="Wikipedia: Postediting",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"MTPEはAI翻訳と人間翻訳の協働形態、職業構造再編の中核。",
        "related_ai_phenomenon":"AI-人間協働翻訳の標準化"}])

add(**C, name_ja="翻訳メモリ・CATツール史",
    name_en="Translation Memory & CAT Tools history",
    name_original="Trados / SDL / MemoQ / Smartcat / Phrase",
    period_key="構造主義・記述的翻訳学期",
    definition="1980年代末のTrados創業を起点とする翻訳メモリ（TM）・CAT（Computer-Assisted Translation）ツール産業史。SDL Tradosの市場支配、MemoQ・Smartcat・Phrase等の追随、クラウド・AI統合への進化が産業翻訳の生産性を変容させた。",
    background="1980年代パソコン普及と翻訳産業のデジタル化。",
    development="2000年代SDL Trados市場独占、2020年代AI統合TMS全面化。",
    historical_context="1990-2020年代翻訳産業のソフトウェア化期。",
    primary_source_url=WIKI_EN+"Translation_memory",
    primary_source_type="Wikipedia: Translation memory",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="NMTジェンダーバイアス（Stanovsky 2019）",
    name_en="Stanovsky et al., NMT Gender Bias",
    name_original="Evaluating Gender Bias in MT",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2019年Gabriel Stanovsky等著、機械翻訳の系統的ジェンダーバイアスを実証的に明らかにした論文。職業名翻訳における男性デフォルト化（doctor→男・nurse→女）等、訓練データバイアスの具体的体現を示し、翻訳AI倫理論議の起点となった。",
    background="2010年代後半AI公平性研究と、訓練データバイアス問題化。",
    development="MT公平性研究の基準論文、2020年代AI翻訳倫理ガイドラインの基盤。",
    historical_context="2019年AI公平性研究隆盛期。",
    primary_source_url=ACL+"P19-1164/",
    primary_source_type="ACL Anthology: Stanovsky et al. 2019",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"NMTジェンダーバイアス研究はAI翻訳倫理の理論的中核。",
        "related_ai_phenomenon":"AI翻訳のジェンダーバイアス"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"AI倫理・公平性",
        "description":"NMTバイアス研究はAI倫理研究の言語領域への展開。"}])


# ============================================================
# D: 翻訳と権力 (8)
# ============================================================
add(**C, name_ja="ラファエル『植民地の契約』",
    name_en="Rafael, Contracting Colonialism",
    name_original="Contracting Colonialism: Translation and Christian Conversion in Tagalog Society",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1988年ヴィセンテ・ラファエル著、スペイン植民地下フィリピンのタガログ語キリスト教翻訳が植民地権力と土着抵抗の交渉場として機能した過程を分析。植民地翻訳論・東南アジア・スタディーズの古典。",
    background="1980年代後半東南アジア・スタディーズの脱植民地化、ベネディクト・アンダーソン的国民論。",
    development="ポストコロニアル翻訳学の重要先行研究、ニランジャーナとの並行的展開。",
    historical_context="1980年代末ポストコロニアル理論興隆期。",
    primary_source_url=WIKI_EN+"Vicente_L._Rafael",
    primary_source_type="Wikipedia: Vicente L. Rafael",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"植民地宗教人類学",
        "description":"ラファエルの植民地翻訳論は宗教人類学の翻訳論的展開。"}])

add(**C, name_ja="ラファエル『母なきことば』",
    name_en="Rafael, Motherless Tongues",
    name_original="Motherless Tongues: The Insurgency of Language amid Wars of Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2016年ヴィセンテ・ラファエル著、フィリピン語・スペイン語・英語間の植民地・ポスト植民地翻訳と「テロとの戦争」期の翻訳実践を分析。母語概念自体の植民性を問う「母なきことば」論。",
    background="ラファエル『植民地の契約』の継承と、9.11後翻訳政治化への応答。",
    development="2010年代ポストコロニアル翻訳論の現代的展開、母語概念批判の中核。",
    historical_context="2010年代「テロとの戦争」期翻訳政治化。",
    primary_source_url=WIKI_EN+"Vicente_L._Rafael",
    primary_source_type="Wikipedia: Vicente L. Rafael",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"母語の哲学",
        "description":"ラファエルは母語概念の植民性を問う言語哲学的批判を展開。"}])

add(**C, name_ja="酒井直樹『翻訳と主体』",
    name_en="Sakai, Translation and Subjectivity",
    name_original="Translation and Subjectivity",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1997年酒井直樹著、日本における国民的・言語的主体性が翻訳実践を通じて構築された過程を分析。「同質的言語的言説」概念で、国語=国民=国家の三位一体形成における翻訳の役割を理論化。",
    background="酒井の日本思想史研究と、ポストコロニアル批評の日本適用。",
    development="日本翻訳論議の理論的中核、TRACES雑誌等の翻訳論議基盤。",
    historical_context="1990年代後半日本ポストコロニアル批評隆盛期。",
    primary_source_url=WIKI_EN+"Naoki_Sakai",
    primary_source_type="Wikipedia: Naoki Sakai",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"翻訳と主体構築論はAI翻訳が国民言語的主体を解体する可能性の理論的基盤。",
        "related_ai_phenomenon":"AI翻訳と国民言語的主体"}],
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"主体性の哲学",
        "description":"酒井翻訳論は主体性の言語論的構築を扱う哲学的探究。"}])

add(**C, name_ja="ティモシュコ『翻訳学の拡張』",
    name_en="Tymoczko, Enlarging Translation",
    name_original="Enlarging Translation, Empowering Translators",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2007年マリア・ティモシュコ著、西洋中心主義的翻訳学を、非西洋翻訳概念（中国「翻訳」、アラビア語「tarjama」、サンスクリット「anuvada」等）の調査により脱中心化することを提唱した方法論的著作。",
    background="ティモシュコのアイルランド古ゲール語翻訳実践と、世界翻訳学の脱西洋化要求。",
    development="非西洋翻訳概念研究の理論的基盤、翻訳学の地球的展開の中核。",
    historical_context="2000年代翻訳学グローバル化期。",
    primary_source_url=WIKI_EN+"Maria_Tymoczko",
    primary_source_type="Wikipedia: Maria Tymoczko",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"非西洋翻訳概念",
        "description":"ティモシュコの非西洋翻訳概念収集は人類学的多元的翻訳論。"}])

add(**C, name_ja="ティモシュコ『翻訳・抵抗・活動』",
    name_en="Tymoczko, Translation, Resistance, Activism",
    name_original="Translation, Resistance, Activism",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2010年マリア・ティモシュコ編、活動家翻訳論を体系化した論集。アイルランド独立運動、フェミニスト翻訳、人権翻訳、デジタル抵抗翻訳の事例を集積、翻訳者を社会変革の能動的エージェントとして位置づけた。",
    background="2000年代翻訳の政治化、市民メディア翻訳の興隆。",
    development="活動家翻訳学の中核テクスト、Translators Without Borders等の理論基盤。",
    historical_context="2000年代翻訳アクティビズム制度化期。",
    primary_source_url=WIKI_EN+"Maria_Tymoczko",
    primary_source_type="Wikipedia: Maria Tymoczko",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ブリセ『非合理性のソシオクリティック』",
    name_en="Brisset, A Sociocritique of Translation",
    name_original="Sociocritique de la traduction",
    period_key="構造主義・記述的翻訳学期",
    definition="1990/1996年アニー・ブリセ著、ケベック演劇翻訳の社会批判的分析。サン=ドニ・ガルノー、ラトレル等のケベック作家英訳が、ケベック国民的アイデンティティ構築と翻訳実践の交差を示す事例を分析。",
    background="ケベック・ナショナリズム運動と、翻訳学の社会批判的展開。",
    development="演劇翻訳論、地域文学翻訳論の中核、社会学的翻訳学の前駆。",
    historical_context="1990年代カナダ・ケベック翻訳学興隆期。",
    primary_source_url=WIKI_FR+"Annie_Brisset",
    primary_source_type="Wikipedia(fr): Annie Brisset",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アアルトネン『時のドラマ』",
    name_en="Aaltonen, Time-sharing on Stage",
    name_original="Time-sharing on Stage: Drama Translation in Theatre and Society",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2000年シルッカ・アアルトネン著、フィンランド演劇翻訳史を社会学的に分析。演劇翻訳における時間性（同時代化・歴史化）と社会的調停を理論化、北欧演劇翻訳論の代表。",
    background="フィンランド演劇翻訳実践と、北欧翻訳学の隆盛。",
    development="演劇翻訳論の標準テクスト、時間性翻訳論の中核。",
    historical_context="2000年前後北欧翻訳学興隆期。",
    primary_source_url=WIKI_EN+"Sirkku_Aaltonen",
    primary_source_type="Wikipedia: Sirkku Aaltonen",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴェヌーティ『翻訳がすべてを変える』",
    name_en="Venuti, Translation Changes Everything",
    name_original="Translation Changes Everything: Theory and Practice",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2013年ローレンス・ヴェヌーティ論文集、2000-2010年代論文を集成し、翻訳が哲学・宗教・科学・文学の各領域を変容させる過程を分析。「翻訳が変える」という能動的視座から、翻訳の世界文化的役割を再評価した。",
    background="ヴェヌーティ後期の論文蓄積と、翻訳学の制度的成熟。",
    development="ヴェヌーティ後期翻訳哲学の集大成、『道具主義に抗して』(2019)への橋渡し。",
    historical_context="2010年代翻訳学の総合化期。",
    primary_source_url=WIKI_EN+"Lawrence_Venuti",
    primary_source_type="Wikipedia: Lawrence Venuti",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: 翻訳教育・規格 (8)
# ============================================================
add(**C, name_ja="キラリ『社会構成主義翻訳教育』",
    name_en="Kiraly, Social Constructivist Translation Pedagogy",
    name_original="A Social Constructivist Approach to Translator Education",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2000年ドナルド・キラリ著、ヴィゴツキー社会構成主義に基づく翻訳教育論。教師中心から学生協働プロジェクト中心への転換を提案、欧州翻訳教育改革（マインツ大等）の理論的基盤となった。",
    background="2000年前後欧州翻訳教育改革と、構成主義教育論の翻訳学への移植。",
    development="EMT（European Master's in Translation）枠組の理論基盤、翻訳教育の世界標準。",
    historical_context="2000年代欧州翻訳教育標準化期。",
    primary_source_url=WIKI_EN+"Donald_Kiraly",
    primary_source_type="Wikipedia: Donald Kiraly",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ディアス=シンタス『視聴覚翻訳』",
    name_en="Díaz-Cintas, Audiovisual Translation",
    name_original="Audiovisual Translation: Subtitling",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2007年ホルヘ・ディアス=シンタス著、字幕翻訳の方法論を体系化した教科書。スペイン語圏視聴覚翻訳学の世界的中核として、Netflix時代の字幕翻訳教育の標準テクスト。",
    background="2000年代欧州視聴覚翻訳産業の隆盛、UCL翻訳学修士課程。",
    development="OFCOMガイドライン、Netflix字幕基準等の理論的源泉、AVT学会の中核。",
    historical_context="2000年代視聴覚翻訳学制度化期。",
    primary_source_url=WIKI_EN+"Audiovisual_translation",
    primary_source_type="Wikipedia: Audiovisual translation",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="オレロ『メディア・アクセシビリティ』",
    name_en="Orero, Media Accessibility",
    name_original="Topics in Audiovisual Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="ピラル・オレロを中心とするメディア・アクセシビリティ研究。聴覚障害者字幕（SDH）、音声解説（AD）、聴覚字幕の多言語化等、障害者アクセスの翻訳学的研究を制度化。EU指令の理論基盤。",
    background="欧州障害者権利条約、AVT研究のアクセシビリティ展開。",
    development="EBU・OFCOMガイドライン、ISO/IEC 20071基準の理論基盤。",
    historical_context="2010年代メディア・アクセシビリティ法制化期。",
    primary_source_url=WIKI_EN+"Audio_description",
    primary_source_type="Wikipedia: Audio description",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ISO 17100翻訳サービス規格",
    name_en="ISO 17100 Translation Services standard",
    name_original="ISO 17100:2015",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2015年制定のISO翻訳サービス国際規格。翻訳者資格、翻訳プロセス（翻訳・編集・校正）、品質管理、顧客対応の最低基準を規定。EN 15038(2006)の国際化、世界の翻訳産業の品質基準。",
    background="EN 15038欧州規格の成功と、翻訳産業のグローバル品質基準需要。",
    development="2017年ISO 18587（MTPE規格）と並ぶ翻訳産業基準の中核。",
    historical_context="2010年代中盤翻訳産業国際標準化期。",
    primary_source_url=WIKI_EN+"ISO_17100",
    primary_source_type="Wikipedia: ISO 17100",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ATA認証試験",
    name_en="ATA Certification Exam",
    name_original="American Translators Association Certification",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="米国翻訳者協会（ATA）が運営する翻訳者認証試験。30以上の言語ペアで実施され、米国翻訳業界の事実上の資格基準として機能。連邦裁判所通訳認証と並ぶ米国翻訳者プロフェッショナル化の中核。",
    background="1959年ATA設立と、米国翻訳業界の専門職化要求。",
    development="2020年代AI翻訳普及期に専門資格の意義が再焦点化。",
    historical_context="米国翻訳業界の制度化史。",
    primary_source_url=WIKI_EN+"American_Translators_Association",
    primary_source_type="Wikipedia: American Translators Association",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="NAATI認証（豪州）",
    name_en="NAATI Certification (Australia)",
    name_original="National Accreditation Authority for Translators and Interpreters",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="豪州NAATI（1977年設立）の翻訳者・通訳者認証制度。豪州移民政策の多言語サービス需要に対応し、約60言語の認証を実施。コミュニティ通訳・公的翻訳の世界的標準モデル。",
    background="1970年代豪州多文化主義政策と、移民言語サービス需要。",
    development="コミュニティ通訳論の世界的中核、医療・法廷通訳教育の理論基盤。",
    historical_context="豪州多文化主義制度化期。",
    primary_source_url=WIKI_EN+"NAATI",
    primary_source_type="Wikipedia: NAATI",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="EU DGT（翻訳総局）用語集",
    name_en="EU DGT Translation Memory & Terminology",
    name_original="Directorate-General for Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="EU欧州委員会翻訳総局（DGT）が管理する24公用語の翻訳メモリ・用語集IATE（Inter-Active Terminology for Europe）。世界最大規模の多言語翻訳資源として、機械翻訳訓練データ・産業翻訳基準の中核。",
    background="EU多言語政策と、欧州統合における翻訳量の指数関数的増加。",
    development="DGT-TM公開（2007）が機械翻訳訓練データ革命を牽引。",
    historical_context="EU多言語政策成熟期。",
    primary_source_url=WIKI_EN+"Directorate-General_for_Translation",
    primary_source_type="Wikipedia: DGT",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="メリンジャー『通訳教育』",
    name_en="Mellinger, Interpreter Education Research",
    name_original="Translation and Interpreting Studies",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="クリストファー・メリンジャーらのコミュニティ通訳・医療通訳教育研究。米国ヒスパニック系移民医療通訳需要への応答として、通訳教育の方法論・規格化を主導。",
    background="米国移民人口増加と医療・法廷通訳需要。",
    development="ATA認証通訳・医療通訳CCHI認証の理論基盤。",
    historical_context="2010年代米国コミュニティ通訳制度化期。",
    primary_source_url=WIKI_EN+"Community_interpreting",
    primary_source_type="Wikipedia: Community interpreting",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# F: 翻訳作品史・名訳 (10)
# ============================================================
add(**C, name_ja="ローブ古典叢書",
    name_en="Loeb Classical Library",
    name_original="Loeb Classical Library",
    period_key="比較文学形成期",
    definition="1911年ジェームズ・ローブ創設、ハーヴァード大学出版会刊行のギリシア・ラテン古典対訳叢書。原文と英訳を見開きで併置する形式が世界古典翻訳出版の標準モデル。530巻以上で古典英訳の世界的中軸。",
    background="20世紀初頭米国の古典学興隆と、ローブの古典普及理念。",
    development="現代までシリーズ継続、デジタル化（DLCL）でアクセス革命。",
    historical_context="20世紀初頭米国古典学制度化期。",
    primary_source_url=WIKI_EN+"Loeb_Classical_Library",
    primary_source_type="Wikipedia: Loeb Classical Library",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ペンギン・クラシックス翻訳方針",
    name_en="Penguin Classics translation policy",
    name_original="Penguin Classics",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1946年E・V・リュー編集者として創刊のペンギン・クラシックス。「現代英語による読みやすい古典」を理念に、20世紀後半英語圏古典翻訳の標準モデル。リュー訳『オデュッセイア』(1946)が出発点。",
    background="戦後英国文化政策と、古典の大衆普及理念。",
    development="1,000巻超の世界古典翻訳ライブラリ、現代英語訳の標準。",
    historical_context="20世紀中盤英国文化普及期。",
    primary_source_url=WIKI_EN+"Penguin_Classics",
    primary_source_type="Wikipedia: Penguin Classics",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="NYRB Classics",
    name_en="NYRB Classics",
    name_original="New York Review Books Classics",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1999年エドウィン・フランク編集者で創刊のニューヨーク・レビュー・ブックス・クラシックス叢書。20世紀の絶版・無視された世界文学の英訳復刊を方針とし、ヴァシリー・グロスマン、シモーナ・ヴェイユ等の英訳を体系化。",
    background="米国文学界の世界文学関心高揚と、独立系出版の役割。",
    development="現代英語圏世界文学翻訳出版の中核、復刊翻訳論の代表。",
    historical_context="2000年代米国独立系翻訳出版隆盛期。",
    primary_source_url=WIKI_EN+"NYRB_Classics",
    primary_source_type="Wikipedia: NYRB Classics",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ペヴェア=ヴォロホンスキー（ロシア文学英訳）",
    name_en="Pevear & Volokhonsky, Russian translations",
    name_original="Pevear-Volokhonsky translations",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="リチャード・ペヴェアとラリッサ・ヴォロホンスキー夫妻のロシア文学英訳プロジェクト。1990年『カラマーゾフの兄弟』以降、トルストイ・ドストエフスキー・チェーホフ等を再翻訳、ロシア文学英訳の現代的標準を作った。",
    background="20世紀英訳ロシア文学（コンスタンス・ガーネット訳等）の限界認識と再翻訳需要。",
    development="2000年代英語圏ロシア文学読書ブーム、再翻訳論の代表的事例。",
    historical_context="1990-2010年代再翻訳の黄金期。",
    primary_source_url=WIKI_EN+"Pevear_and_Volokhonsky",
    primary_source_type="Wikipedia: Pevear and Volokhonsky",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ペヴェア=ヴォロホンスキーの再翻訳は、AI翻訳時代における人間翻訳家の解釈的役割を示す。",
        "related_ai_phenomenon":"AI時代の人間翻訳家の役割"}])

add(**C, name_ja="ヒントン（唐宋詩翻訳）",
    name_en="Hinton, Tang/Song poetry translations",
    name_original="Classical Chinese Poetry: An Anthology",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="デイヴィッド・ヒントンの唐宋詩英訳プロジェクト。陶淵明・王維・杜甫・李白等の英訳で、道家・禅的世界観を翻訳哲学の中心に置く。中国古典詩英訳の現代的代表で、西洋自然観と東洋宇宙論の翻訳論議を活性化。",
    background="ヒントンの仏教・道家研究と、米国の中国古典受容。",
    development="2000-20年代中国古典詩英訳の標準、生態学的翻訳論との接続。",
    historical_context="2000年代以降英訳古典中国詩の哲学化期。",
    primary_source_url=WIKI_EN+"David_Hinton",
    primary_source_type="Wikipedia: David Hinton",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"道家・禅哲学",
        "description":"ヒントン翻訳論は道家・禅哲学の言語観を翻訳実践に応用。"}])

add(**C, name_ja="ワトソン（中国詩・仏典英訳）",
    name_en="Watson, Chinese poetry and Buddhist translations",
    name_original="The Columbia Book of Chinese Poetry",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="バートン・ワトソンの中国古典詩・仏典英訳事業。『法華経』『荘子』『史記』『漢詩選』等の英訳で、20世紀後半英語圏の中国古典・仏教学受容の中核翻訳者。コロンビア大東アジア研究を主導。",
    background="20世紀後半米国東アジア研究勃興と、ワトソンの長期実践。",
    development="20世紀英訳中国古典・仏典の決定版、東アジア研究教育の標準。",
    historical_context="20世紀後半米国東アジア研究黄金期。",
    primary_source_url=WIKI_EN+"Burton_Watson",
    primary_source_type="Wikipedia: Burton Watson",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ミッチェル『道徳経』『バガヴァッド・ギーター』",
    name_en="Mitchell, Tao Te Ching / Bhagavad Gita",
    name_original="Tao Te Ching: A New English Version (1988)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="スティーヴン・ミッチェルの『道徳経』(1988)『バガヴァッド・ギーター』(2000)等の翻訳=翻案。原文との直接的言語的対応より英語詩としての美的完成度を優先する自由翻訳が論議を呼んだ、現代スピリチュアル翻訳の代表事例。",
    background="ミッチェルの禅修行経験と、米国スピリチュアル文学市場。",
    development="自由翻訳/翻案論の論争点、東洋古典英訳論議の中核。",
    historical_context="1980-2000年代米国スピリチュアル翻訳隆盛期。",
    primary_source_url=WIKI_EN+"Stephen_Mitchell_(translator)",
    primary_source_type="Wikipedia: Stephen Mitchell",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="バークス（ルーミー翻案論争）",
    name_en="Coleman Barks, Rumi controversies",
    name_original="The Essential Rumi",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="コールマン・バークスの『精選ルーミー』(1995)等。ペルシア語原文を直接読まず英語学術訳から英詩化する翻案手法が、米国でルーミーをベストセラー詩人にした一方、東洋学者・ペルシア語話者から強い批判を受けた論争事例。",
    background="米国スピリチュアル市場のスーフィズム需要と、バークスの英詩家経験。",
    development="2010-20年代翻訳倫理論議の中核事例、文化的誤領有論議の発火点。",
    historical_context="米国ルーミーブーム期のオリエンタリズム論議。",
    primary_source_url=WIKI_EN+"Coleman_Barks",
    primary_source_type="Wikipedia: Coleman Barks",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"ルーミー翻案論争はAI翻訳時代の文化的誤領有・原典忠実性論議の先駆。",
        "related_ai_phenomenon":"AI翻訳と文化的誤領有"}],
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"文化的誤領有",
        "description":"バークス論争は人類学的文化的誤領有論議の翻訳実践版。"}])

add(**C, name_ja="ハミル（道徳経・禅詩）",
    name_en="Sam Hamill, Tao Te Ching / Zen poetry",
    name_original="Tao Te Ching translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="サム・ハミル（Copper Canyon Press創設者）の『道徳経』(2007)、禅詩・芭蕉等英訳。Poets Against the War（2003）創設者でもあり、翻訳と政治的アクティビズムを結ぶ実践の代表。",
    background="ハミルのCopper Canyon Press経営と、反戦運動。",
    development="米国詩人翻訳家の活動家系譜、東洋古典英訳の代表。",
    historical_context="2000年代米国詩人翻訳家アクティビズム期。",
    primary_source_url=WIKI_EN+"Sam_Hamill",
    primary_source_type="Wikipedia: Sam Hamill",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エドワード・スノウ（リルケ英訳）",
    name_en="Edward Snow, Rilke translations",
    name_original="Rilke translations (Sonnets to Orpheus etc.)",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="エドワード・スノウの『新詩集』『ドゥイノの悲歌』『オルフェウスへのソネット』等のリルケ英訳。20世紀後半-21世紀英語圏リルケ受容の決定版とされ、現代英訳ドイツ詩の代表的成果。",
    background="米国独語詩研究と、リルケの英語圏での神話化。",
    development="20世紀後半英訳リルケの世界的標準、独詩英訳教育の定番。",
    historical_context="20世紀後半米国独語詩翻訳黄金期。",
    primary_source_url=WIKI_EN+"Edward_Snow_(translator)",
    primary_source_type="Wikipedia: Edward Snow (translator)",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 比較・世界文学方法論 (6)
# ============================================================
add(**C, name_ja="ブリュヌティエール『進化的批評』",
    name_en="Brunetière, Evolutionary Comparative Criticism",
    name_original="L'Évolution des genres dans l'histoire de la littérature",
    period_key="比較文学形成期",
    definition="1890年代フェルディナン・ブリュヌティエール著、ダーウィン進化論を文学ジャンル変遷に応用した比較文学方法論。フランス比較文学第一世代の代表で、20世紀初頭の生物学的比較文学パラダイムを定立した。",
    background="19世紀末のダーウィン主義知的興奮と、比較文学制度化要求。",
    development="20世紀初頭生物学的文学史パラダイムの基盤、後にフォルマリスト・歴史主義文学史への転換。",
    historical_context="19世紀末フランス比較文学制度化期。",
    primary_source_url=WIKI_FR+"Ferdinand_Bruneti%C3%A8re",
    primary_source_type="Wikipedia(fr): Ferdinand Brunetière",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="レマック1961『比較文学の定義』",
    name_en="Remak 1961, Definition of Comparative Literature",
    name_original="Comparative Literature, Its Definition and Function",
    period_key="比較文学形成期",
    definition="1961年ヘンリー・レマック著、米国学派比較文学の決定的定義。「ある国の文学を他国・他言語の文学および他の知識領域と比較する研究」とし、米国学派の包括的定義を確立。仏学派の影響研究中心主義と対峙した。",
    background="米国比較文学制度化（インディアナ大プログラム等）と、仏学派批判。",
    development="ACLA（米国比較文学協会）の方法論的中核、世代を超えた比較文学定義の基準。",
    historical_context="1960年代米国比較文学黄金期。",
    primary_source_url=WIKI_EN+"Comparative_literature",
    primary_source_type="Wikipedia: Comparative Literature",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ダムロッシュ『世界文学を読む方法』",
    name_en="Damrosch, How to Read World Literature",
    name_original="How to Read World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2009/2017年デイヴィッド・ダムロッシュ著、世界文学読解の入門教科書。文化的距離・翻訳・正典問題を学部教育向けに整理し、世界文学教育の世界的標準テクストとなった。",
    background="2000年代世界文学講座普及と、教育需要への応答。",
    development="2010年代世界文学教育の標準、ダムロッシュ世界文学論の普及版。",
    historical_context="2010年代世界文学教育制度化期。",
    primary_source_url=WIKI_EN+"David_Damrosch",
    primary_source_type="Wikipedia: David Damrosch",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="チア『世界文学とは何か』",
    name_en="Cheah, What Is a World",
    name_original="What Is a World? On Postcolonial Literature as World Literature",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2016年ピン・チア著、世界文学概念をハイデガー『世界開示』とポストコロニアル理論で再定義。世界文学を「世界制作（world-making）」のポストコロニアル実践として捉え、カサノヴァ・モレッティの市場・形式中心主義を批判した理論書。",
    background="ハイデガー存在論のポストコロニアル批評への展開、グローバル資本主義批判。",
    development="2010年代世界文学論の哲学的深化、ポストコロニアル世界文学論の中核。",
    historical_context="2010年代世界文学論パラダイム拡張期。",
    primary_source_url=WIKI_EN+"Pheng_Cheah",
    primary_source_type="Wikipedia: Pheng Cheah",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"世界開示の哲学",
        "description":"チアの世界文学論はハイデガー世界開示概念のポストコロニアル展開。"}])

add(**C, name_ja="ヘルゲソン=ヴァーミューレン『世界文学の制度』",
    name_en="Helgesson & Vermeulen, Institutions of World Literature",
    name_original="Institutions of World Literature: Writing, Translation, Markets",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2015年ステファン・ヘルゲソン＆ピーター・ヴァーミューレン編、世界文学の制度的次元（出版社・翻訳賞・教育プログラム・市場）を分析した論集。世界文学論を抽象的概念から具体的制度分析へ転換した重要著作。",
    background="カサノヴァ・モレッティの世界文学論への制度的具体化要求。",
    development="2010年代世界文学制度研究の中核、社会学的世界文学論の出発点。",
    historical_context="2010年代中盤世界文学論の制度的転回期。",
    primary_source_url=WIKI_EN+"World_literature",
    primary_source_type="Wikipedia: World literature",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ムフティ『アウエルバッハ・イスタンブル』",
    name_en="Mufti, Auerbach in Istanbul",
    name_original="Auerbach in Istanbul: Edward Said, Secular Criticism",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="アーミル・ムフティ「アウエルバッハ・イスタンブル」(1998)論文と『英語を忘れよ』(2016)。エーリヒ・アウエルバッハのイスタンブル亡命中『ミメーシス』執筆を、世界文学制度の植民地的起源と関連付ける批判的論究。",
    background="サイード『オリエンタリズム』のアウエルバッハ評価、ポストコロニアル文学史。",
    development="ムフティ『英語を忘れよ』(2016)世界文学批判の理論的基礎。",
    historical_context="1990-2010年代ポストコロニアル世界文学論の理論化期。",
    primary_source_url=WIKI_EN+"Aamir_Mufti",
    primary_source_type="Wikipedia: Aamir Mufti",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"オリエンタリズム批判",
        "description":"ムフティのアウエルバッハ論はサイード・オリエンタリズム論の世界文学的応用。"}])


# ============================================================
# H: プロフェッショナル組織・翻訳賞 (6)
# ============================================================
add(**C, name_ja="FIT国際翻訳家連盟",
    name_en="FIT International Federation of Translators",
    name_original="Fédération Internationale des Traducteurs",
    period_key="構造主義・記述的翻訳学期",
    definition="1953年パリ創立、世界100以上の翻訳者協会を統合する国際組織。UNESCO関連NGO、9月30日「国際翻訳の日」（聖ヒエロニムス記念日）制定推進、翻訳者著作権・労働条件のグローバル擁護機関。",
    background="戦後欧州の文化交流復興と、翻訳者プロフェッショナル化要求。",
    development="2017年国連『国際翻訳の日』正式制定、翻訳者プロフェッショナル化の世界的中核。",
    historical_context="戦後翻訳プロフェッショナル化期。",
    primary_source_url=WIKI_EN+"International_Federation_of_Translators",
    primary_source_type="Wikipedia: FIT",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="AIIC国際会議通訳者協会",
    name_en="AIIC International Association of Conference Interpreters",
    name_original="Association Internationale des Interprètes de Conférence",
    period_key="構造主義・記述的翻訳学期",
    definition="1953年創立の会議通訳者の国際職能団体。ジュネーブ本部、加盟国際機関（国連・EU・NATO等）の通訳基準・労働条件を規定。世界の同時通訳プロフェッショナル化の中核機関。",
    background="国連・EU等の同時通訳隆盛と、通訳者労働条件統一要求。",
    development="同時通訳の世界的標準（30分交代等）の規定、通訳料金基準の国際化。",
    historical_context="戦後国際機関同時通訳制度化期。",
    primary_source_url=WIKI_EN+"International_Association_of_Conference_Interpreters",
    primary_source_type="Wikipedia: AIIC",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="EST欧州翻訳学会",
    name_en="EST European Society for Translation Studies",
    name_original="European Society for Translation Studies",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1992年ヴィーンで創立の翻訳学学会。スネル=ホーンビー等が主導、欧州翻訳学の制度的中核として機能、3年ごとの大会と若手研究者奨励プログラムが翻訳学のグローバル化を牽引する。",
    background="1990年代欧州翻訳学制度化と、学際的学会需要。",
    development="2020年代までの翻訳学グローバル化の中核学会、IATIS等への波及。",
    historical_context="1990年代翻訳学制度化期。",
    primary_source_url=WIKI_EN+"European_Society_for_Translation_Studies",
    primary_source_type="Wikipedia: EST",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ALTA米国文学翻訳家協会",
    name_en="ALTA American Literary Translators Association",
    name_original="American Literary Translators Association",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="1978年テキサス大ダラス校創立の米国文学翻訳家協会。年次大会、National Translation Award（年次優秀文学翻訳賞）、若手翻訳家奨励事業を運営、米国文学翻訳プロフェッショナル化の中核。",
    background="米国大学院翻訳プログラム勃興と、文学翻訳者ネットワーク需要。",
    development="2010年代以降の米国世界文学翻訳普及の中核、National Translation Awardは権威ある文学翻訳賞。",
    historical_context="1970年代末米国文学翻訳制度化期。",
    primary_source_url=WIKI_EN+"American_Literary_Translators_Association",
    primary_source_type="Wikipedia: ALTA",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="国際ブッカー賞",
    name_en="International Booker Prize",
    name_original="International Booker Prize",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2005年創設（2016年現名称）、英訳された世界文学小説に贈られる権威ある翻訳文学賞。賞金£50,000を作家・翻訳者で折半する原則が、英語圏文学翻訳家の経済的・象徴的地位向上を主導した。",
    background="マン・ブッカー賞拡張と、世界文学英訳普及運動。",
    development="2010年代以降英語圏世界文学読書ブームの中核、翻訳家可視化運動の象徴的勝利。",
    historical_context="2010-20年代英語圏世界文学読書ブーム期。",
    primary_source_url=WIKI_EN+"International_Booker_Prize",
    primary_source_type="Wikipedia: International Booker Prize",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[{"axis":"言語","status":"rethinking",
        "rationale":"国際ブッカー賞の翻訳者折半原則はAI時代の翻訳者著作権論議の先進事例。",
        "related_ai_phenomenon":"AI時代の翻訳者著作権"}])

add(**C, name_ja="サイフ・ガバシュ・バニパル賞",
    name_en="Saif Ghobash Banipal Prize",
    name_original="Saif Ghobash Banipal Prize for Arabic Literary Translation",
    period_key="世界文学・ポストコロニアル翻訳期",
    definition="2006年Banipal誌・英国作家協会主催のアラビア語英訳文学翻訳賞。Banipal誌（1998-、現代アラブ文学英訳専門誌）と連動し、現代アラブ文学英訳の世界的中核賞。地域文学翻訳賞の代表事例。",
    background="2000年代英語圏アラブ文学関心高揚と、専門翻訳賞需要。",
    development="2010年代以降アラブ文学英訳普及の中核、地域文学翻訳賞のモデル。",
    historical_context="2000年代地域文学翻訳賞制度化期。",
    primary_source_url=WIKI_EN+"Saif_Ghobash%E2%80%93Banipal_Prize",
    primary_source_type="Wikipedia: Saif Ghobash–Banipal Prize",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="理論",
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
        print(f"[wave22-c38-add80] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave22-c38-add80] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
