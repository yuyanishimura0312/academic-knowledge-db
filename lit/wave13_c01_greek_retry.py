"""LIT-DB Phase 2 Wave 13 RETRY — C01: Classical Antiquity (+50).

Subfield: lit_eu_classical (id=1), region='西欧'.
Sources: Perseus, TLG, Loeb, Latin Library, Sefaria, Project Gutenberg, Wikisource.
>= 80% primary tier; fourth_transform_tags >= 12; cross_domain >= 10.

Adds 50 NEW concepts on top of existing 90, covering:
  A: Greek lyric (9)
  B: Hellenistic (5)
  C: Greek prose / Imperial (8)
  D: Late Latin / Apuleius / Petronius / Boethius / Augustine (7)
  E: Early Christian Latin (7)
  F: Byzantine (6)
  G: Late antique misc / theory (8)
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("古拙期（アルカイック）", "Archaic Greek", -800, -480, "ホメロス以後アルカイック期。"),
    ("古典期（クラシック）", "Classical Greek", -480, -323, "ペルシア戦争後の古典期。"),
    ("ヘレニズム期", "Hellenistic Greek", -323, -31, "アレクサンドロス没後からアクティウム海戦まで。"),
    ("帝政ローマ時代（白銀期）", "Imperial Roman", 14, 200, "白銀期からアントニヌス朝期。"),
    ("後期ローマ・教父期", "Late Roman / Patristic", 200, 600,
     "セウェルス朝以後の後期ローマ帝国期、ラテン教父・初期ビザンツへの移行期。"),
    ("ビザンツ期", "Byzantine", 600, 1453,
     "ヘラクレイオス朝以降のビザンツ帝国期、コンスタンティノープル陥落まで。"),
]


PERSEUS = "https://www.perseus.tufts.edu/hopper/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_GR = "https://el.wikisource.org/wiki/"
WSRC_LA = "https://la.wikisource.org/wiki/"
GUTEN = "https://www.gutenberg.org/"
LATLIB = "https://www.thelatinlibrary.com/"
LOEB = "https://www.loebclassics.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_classical", region="西欧", original_script="greek")
CL = dict(subfield_code="lit_eu_classical", region="西欧", original_script="latin")


# ============================================================
# A: ギリシア抒情詩（9）
# ============================================================
add(**C, name_ja="サッポー断片",
    name_en="Sappho fragments",
    name_original="Σαπφώ",
    period_key="古拙期（アルカイック）",
    definition="レスボス島の女性詩人サッポー(c.630-570 BCE)が残した抒情詩断片群。「断片1（アフロディテ讃歌）」「断片31（彼は神に等しい）」が代表。サッポー詩形（Sapphic stanza）を確立し、女性的エロスの主観的表白を西欧抒情詩の祖型とした。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0202",
    primary_source_type="Perseus: Sappho",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ピンダロス勝利歌（オリュンピア・ピューティア）",
    name_en="Pindar's Olympian/Pythian Odes",
    name_original="Πίνδαρος Ἐπινίκια",
    period_key="古典期（クラシック）",
    definition="テーバイの詩人ピンダロス(c.518-438 BCE)が競技勝利者を讃える形式で書いた合唱抒情詩集。『オリュンピア祝勝歌』『ピューティア祝勝歌』『ネメア祝勝歌』『イストミア祝勝歌』の四集が現存。神話・倫理・名誉論を高度に凝縮した最高峰の合唱抒情詩。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0162",
    primary_source_type="Perseus: Pindar",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="バッキュリデス頌歌",
    name_en="Bacchylides' Odes",
    name_original="Βακχυλίδης",
    period_key="古典期（クラシック）",
    definition="ケオス島の合唱抒情詩人バッキュリデス(c.518-451 BCE)の祝勝歌・ディテュランボス。1896年エジプト出土パピルスで再発見され、ピンダロスと並ぶ古典期合唱抒情詩の柱として再評価された。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0061",
    primary_source_type="Perseus: Bacchylides",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アナクレオン詩",
    name_en="Anacreon",
    name_original="Ἀνακρέων",
    period_key="古拙期（アルカイック）",
    definition="テオス出身の宮廷詩人アナクレオン(c.582-485 BCE)の酒・恋愛・遊戯の抒情詩。ヘレニズム期に偽作群『アナクレオンテア（Anacreontea）』が編まれ、ルネサンス以降の欧州抒情詩に「アナクレオン調」を伝えた。",
    primary_source_url=WSRC_GR+"%CE%91%CE%BD%CE%B1%CE%BA%CF%81%CE%AD%CF%89%CE%BD",
    primary_source_type="Greek Wikisource: Anacreon",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アルクマン乙女歌",
    name_en="Alcman's Partheneia",
    name_original="Ἀλκμάν Παρθένεια",
    period_key="古拙期（アルカイック）",
    definition="スパルタの合唱抒情詩人アルクマン(c.7世紀BCE)の乙女合唱歌。1855年ルーヴル・パピルスで断片再発見。スパルタ少女合唱団の儀礼歌として、合唱抒情詩の最古形態を示す。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0481",
    primary_source_type="Perseus: Alcman",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ステシコロス合唱抒情詩",
    name_en="Stesichorus",
    name_original="Στησίχορος",
    period_key="古拙期（アルカイック）",
    definition="ヒメラの合唱抒情詩人ステシコロス(c.630-555 BCE)の叙事的合唱歌断片。『ゲリュオネイス』『パリノディア（ヘレネ撤回歌）』が知られ、叙事詩と抒情詩を架橋する形式として古典期悲劇の合唱抒情詩学に影響した。",
    primary_source_url=WIKI_EN+"Stesichorus",
    primary_source_type="Wikipedia: Stesichorus",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アルキロコスのイアンボス",
    name_en="Archilochus' iambic poetry",
    name_original="Ἀρχίλοχος",
    period_key="古拙期（アルカイック）",
    definition="パロス島の傭兵詩人アルキロコス(c.680-645 BCE)の風刺的・諷刺的イアンボス詩。罵倒・自嘲・戦場体験の率直な一人称表白を、後のホラティウス諷刺詩・西欧諷刺文学の祖型として確立した。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0479",
    primary_source_type="Perseus: Archilochus",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="テュルタイオス戦闘エレゲイア",
    name_en="Tyrtaeus' martial elegies",
    name_original="Τυρταῖος",
    period_key="古拙期（アルカイック）",
    definition="スパルタの戦闘エレゲイア詩人テュルタイオス(c.7世紀BCE)が第二次メッセニア戦争期に作ったとされる戦闘鼓舞詩。市民戦士の徳と祖国愛のエレゲイア定型を確立し、古典期市民徳論の文学的基盤となった。",
    primary_source_url=WIKI_EN+"Tyrtaeus",
    primary_source_type="Wikipedia: Tyrtaeus",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="テオグニスのエレゲイア",
    name_en="Theognis of Megara",
    name_original="Θέογνις",
    period_key="古拙期（アルカイック）",
    definition="メガラの貴族詩人テオグニス(c.6世紀BCE)のエレゲイア詩集（『テオグニデア』）。少年キュルノスへの教訓詩として、貴族階層の倫理規範・古典期エリート教育の文学的基盤を提供した。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0479",
    primary_source_type="Perseus: Theognis",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: ヘレニズム期（5）
# ============================================================
add(**C, name_ja="カリマコス『アイティア』",
    name_en="Callimachus' Aetia",
    name_original="Καλλίμαχος Αἴτια",
    period_key="ヘレニズム期",
    definition="アレクサンドリア図書館詩人カリマコス(c.310-240 BCE)の起源譚詩集。希少語彙・学識・断片的詩学を特徴とし、ヘレニズム文献学詩学の規範となり、ローマのカトゥッルス・プロペルティウス・オウィディウスへ直接継承された。",
    primary_source_url=WIKI_EN+"Aetia_(Callimachus)",
    primary_source_type="Wikipedia: Aetia",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="カリマコス讃歌",
    name_en="Callimachus' Hymns",
    name_original="Καλλιμάχου Ὕμνοι",
    period_key="ヘレニズム期",
    definition="カリマコスの『讃歌六篇』（ゼウス・アポロン・アルテミス・デロス・浴身・デメテル）。ホメロス讃歌の伝統を学識的・形式的洗練で更新し、ヘレニズム的古典回帰の典型として後代詩学に影響した。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:2008.01.0498",
    primary_source_type="Perseus: Callimachus Hymns",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="テオクリトス『田園詩』",
    name_en="Theocritus' Idylls",
    name_original="Θεόκριτος Εἰδύλλια",
    period_key="ヘレニズム期",
    definition="シラクサの詩人テオクリトス(c.300-260 BCE)の田園詩・牧歌集（30編現存）。シチリア牧人の生活描写を文学化し、ウェルギリウス『牧歌』を介して西欧牧歌伝統(pastoral)の祖型を確立した。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0231",
    primary_source_type="Perseus: Theocritus",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アポロニオス・ロディオス『アルゴナウティカ』",
    name_en="Apollonius Rhodius' Argonautica",
    name_original="Ἀπολλώνιος Ῥόδιος Ἀργοναυτικά",
    period_key="ヘレニズム期",
    definition="ロドスのアポロニオス(c.295-215 BCE)が4巻で書いたヘレニズム叙事詩。イアソンとアルゴナウタイの航海とメデイアの恋を描く。ホメロス模倣ではない学識的・心理的叙事詩としてウェルギリウス『アエネーイス』に直接影響。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0224",
    primary_source_type="Perseus: Argonautica",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="メレアグロス『花冠（ステファノス）』",
    name_en="Meleager's Garland",
    name_original="Μελέαγρος Στέφανος",
    period_key="ヘレニズム期",
    definition="ガダラの詩人メレアグロス(c.140-70 BCE)が編んだヘレニズム抒情詩・エピグラム選集。後の『ギリシア詞華集（Anthologia Graeca）』の核となり、エピグラム文学伝統の制度的起源を成した。ポセイディッポスら同時代詩人を含む。",
    primary_source_url=WIKI_EN+"Meleager_of_Gadara",
    primary_source_type="Wikipedia: Meleager",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: ギリシア散文・帝政期（8）
# ============================================================
add(**C, name_ja="プルタルコス『対比列伝』",
    name_en="Plutarch's Parallel Lives",
    name_original="Πλούταρχος Βίοι Παράλληλοι",
    period_key="帝政ローマ時代（白銀期）",
    definition="プルタルコス(c.46-120)の伝記対比集。ギリシア人とローマ人を一対にして比較する形式で、政治家の徳・性格を主題化する。ノース英訳を介してシェイクスピア『ジュリアス・シーザー』『アントニーとクレオパトラ』の直接源泉となった。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:2008.01.0007",
    primary_source_type="Perseus: Plutarch Lives",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="プルタルコス『モラリア』",
    name_en="Plutarch's Moralia",
    name_original="Πλούταρχος Ἠθικά",
    period_key="帝政ローマ時代（白銀期）",
    definition="プルタルコスの倫理・哲学・宗教論集（78編）。古代ギリシア・ローマの倫理学・教育論・宗教論の集大成として、ルネサンス人文主義（モンテーニュ『随想録』）に決定的影響を与えた。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:2008.01.0244",
    primary_source_type="Perseus: Plutarch Moralia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルキアノス諷刺対話",
    name_en="Lucian's satirical dialogues",
    name_original="Λουκιανός",
    period_key="帝政ローマ時代（白銀期）",
    definition="サモサタのルキアノス(c.125-180)の諷刺対話・寓話（『神々の対話』『死者の対話』『真実の話』等）。ギリシア哲学・宗教・社会の諷刺的脱構築を展開し、ルネサンス・啓蒙期欧州諷刺文学（エラスムス、ヴォルテール、スウィフト）の祖型となった。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:2008.01.0426",
    primary_source_type="Perseus: Lucian",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヘリオドロス『エチオピア物語』",
    name_en="Heliodorus' Aethiopica",
    name_original="Ἡλιόδωρος Αἰθιοπικά",
    period_key="帝政ローマ時代（白銀期）",
    definition="エメサのヘリオドロス(c.3-4世紀)が10巻で書いたギリシア恋愛小説の最高峰。テアゲネスとカリクレイアの冒険を非線形構成で描き、ルネサンス・近世欧州小説（セルバンテス、シドニー、ラシーヌ）の祖型となった。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:2008.01.0635",
    primary_source_type="Perseus: Heliodorus Aethiopica",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロンゴス『ダフニスとクロエ』",
    name_en="Longus' Daphnis and Chloe",
    name_original="Λόγγος Δάφνις καὶ Χλόη",
    period_key="帝政ローマ時代（白銀期）",
    definition="2-3世紀のロンゴスが書いた牧歌的恋愛小説。レスボス島の養い子ダフニスとクロエの牧歌的恋愛を描き、田園小説(pastoral romance)の祖型として、ルネサンス田園詩・近代田園小説（ルソー、ゲーテ）に影響を与えた。",
    primary_source_url=WIKI_EN+"Daphnis_and_Chloe",
    primary_source_type="Wikipedia: Daphnis and Chloe",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アキレウス・タティオス『レウキッペとクレイトポン』",
    name_en="Achilles Tatius' Leucippe and Clitophon",
    name_original="Ἀχιλλεὺς Τάτιος",
    period_key="帝政ローマ時代（白銀期）",
    definition="アレクサンドリアのアキレウス・タティオス(2世紀)による8巻のギリシア恋愛小説。一人称語りと感覚的描写を特徴とし、ヘレニズム=帝政期ギリシア小説の主要形式を代表する。",
    primary_source_url=WIKI_EN+"Leucippe_and_Clitophon",
    primary_source_type="Wikipedia: Achilles Tatius",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カリトン『カイレアスとカリロエ』",
    name_en="Chariton's Callirhoe",
    name_original="Χαρίτων",
    period_key="帝政ローマ時代（白銀期）",
    definition="アフロディシアスのカリトン(1世紀)が書いた現存最古のギリシア恋愛小説。カイレアスとカリロエの離別と再会を歴史的舞台で描き、古代恋愛小説ジャンルの形式を確立した。",
    primary_source_url=WIKI_EN+"Chariton",
    primary_source_type="Wikipedia: Chariton",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="フィロストラトス『ティアナのアポロニオス伝』",
    name_en="Philostratus' Life of Apollonius of Tyana",
    name_original="Φιλόστρατος",
    period_key="帝政ローマ時代（白銀期）",
    definition="フィロストラトス(c.170-247)の聖人伝記。新ピタゴラス派賢者アポロニオスの生涯を描き、福音書ナラティブとの比較対象として古代後期宗教文学・聖人伝の重要文献となった。",
    primary_source_url=WIKI_EN+"Life_of_Apollonius_of_Tyana",
    primary_source_type="Wikipedia: Apollonius of Tyana",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: ラテン後期・古代後期（7）
# ============================================================
add(**CL, name_ja="アプレイウス『黄金のロバ（変身物語）』詳述",
    name_en="Apuleius' Metamorphoses (full)",
    name_original="Apuleius Metamorphoses",
    period_key="帝政ローマ時代（白銀期）",
    definition="アプレイウス(c.124-170)の11巻ラテン散文小説。ロバに変身したルキウスの遍歴と、内挿物語『プシュケとクピド』を含む。ラテン散文小説の唯一完全な現存例で、ボッカチオ・セルバンテス・ゴールディング英訳を介してシェイクスピアにも影響。",
    primary_source_url=LATLIB+"apuleius.html",
    primary_source_type="Latin Library: Apuleius",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CL, name_ja="ペトロニウス『サテュリコン』詳述",
    name_en="Petronius' Satyricon (full)",
    name_original="Petronius Satyricon",
    period_key="帝政ローマ時代（白銀期）",
    definition="ネロ朝廷臣ペトロニウス(c.27-66)が書いた断片的ラテン散文小説。エンコルピオス一行の冒険と『トリマルキオの饗宴』を含み、ラテン口語・社会風俗の貴重資料として、ジョイス『ユリシーズ』フェリーニ映画に直接影響。",
    primary_source_url=LATLIB+"petronius.html",
    primary_source_type="Latin Library: Petronius",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CL, name_ja="アウルス・ゲッリウス『アッティカ夜話』",
    name_en="Aulus Gellius' Attic Nights",
    name_original="Noctes Atticae",
    period_key="帝政ローマ時代（白銀期）",
    definition="アウルス・ゲッリウス(c.125-180)による20巻の博学雑録集。ラテン文献学・古代法制・文法・哲学逸話を集成し、後代ヨーロッパ博学伝統（モンテーニュ・ベイル『歴史批評辞典』）の規範的祖型となった。",
    primary_source_url=LATLIB+"gellius.html",
    primary_source_type="Latin Library: Aulus Gellius",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="マクロビウス『サトゥルナリア』",
    name_en="Macrobius' Saturnalia",
    name_original="Saturnalia",
    period_key="後期ローマ・教父期",
    definition="マクロビウス(c.4-5世紀)による7巻の対話形式博学雑録。サトゥルナリア祭の三日間に古典文献・ウェルギリウス註解・古代習俗を論じ、中世カロリング・ルネサンス古典学の主要参照源となった。",
    primary_source_url=LATLIB+"macrobius.html",
    primary_source_type="Latin Library: Macrobius",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="ボエティウス『哲学の慰め』",
    name_en="Boethius' Consolation of Philosophy",
    name_original="De Consolatione Philosophiae",
    period_key="後期ローマ・教父期",
    definition="ボエティウス(c.480-524)が獄中で書いたラテン散文・韻文混合の哲学対話。哲学を擬人化した女神との対話を通じて運命・善・摂理を論じる。中世ヨーロッパ最重要古典の一つで、アルフレッド大王・チョーサー・エリザベス1世が翻訳。",
    primary_source_url=LATLIB+"boethius.html",
    primary_source_type="Latin Library: Boethius",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CL, name_ja="アウグスティヌス『告白』",
    name_en="Augustine's Confessions",
    name_original="Confessiones",
    period_key="後期ローマ・教父期",
    definition="ヒッポのアウグスティヌス(354-430)が400年頃に書いた13巻のラテン自伝・神学書。母モニカへの祈りの形式で回心を語り、西欧自伝文学の祖型・内省的主体性の原点として、ルソー『告白』近代自伝伝統の起点となった。",
    primary_source_url=LATLIB+"august.html",
    primary_source_type="Latin Library: Augustine",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CL, name_ja="アウグスティヌス『神の国』",
    name_en="Augustine's City of God",
    name_original="De Civitate Dei",
    period_key="後期ローマ・教父期",
    definition="アウグスティヌスが410年ローマ陥落後の弁神論として22巻で書いた歴史神学書。地上の国と神の国の二重構造論を提示し、中世キリスト教歴史哲学・政治神学の基盤となった。",
    primary_source_url=LATLIB+"august.html",
    primary_source_type="Latin Library: Augustine City of God",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# E: 初期キリスト教ラテン文学（7）
# ============================================================
add(**CL, name_ja="テルトゥリアヌス弁証",
    name_en="Tertullian's Apologetics",
    name_original="Tertullianus Apologeticum",
    period_key="後期ローマ・教父期",
    definition="カルタゴのテルトゥリアヌス(c.155-220)が書いた最初期ラテン教父弁証論。『弁証論（Apologeticum）』『異端論駁』等で初期キリスト教ラテン語神学術語を確立し、ラテン教父文学の祖型を成した。",
    primary_source_url=LATLIB+"tertullian.html",
    primary_source_type="Latin Library: Tertullian",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CL, name_ja="キプリアヌス書簡集",
    name_en="Cyprian's Letters and Treatises",
    name_original="Cyprianus",
    period_key="後期ローマ・教父期",
    definition="カルタゴ司教キプリアヌス(c.200-258)の書簡81通と『教会一致論』等の論考。3世紀キリスト教共同体の組織・倫理・殉教を記録し、初期キリスト教ラテン散文の規範となった。",
    primary_source_url=LATLIB+"cyprian.html",
    primary_source_type="Latin Library: Cyprian",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="ラクタンティウス『神学綱要』",
    name_en="Lactantius' Divine Institutes",
    name_original="Divinae Institutiones",
    period_key="後期ローマ・教父期",
    definition="ラクタンティウス(c.250-325)による7巻の体系的キリスト教ラテン神学書。古典修辞学的雅文体で書かれ、「キリスト教のキケロ」と称された。ルネサンス人文主義者に最も読まれた古代キリスト教文献の一つ。",
    primary_source_url=LATLIB+"lactantius.html",
    primary_source_type="Latin Library: Lactantius",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="ヒエロニムス『ウルガタ訳』",
    name_en="Jerome's Vulgate",
    name_original="Biblia Vulgata",
    period_key="後期ローマ・教父期",
    definition="ヒエロニムス(c.347-420)が382-405年に完成したラテン語聖書翻訳。ヘブライ語旧約から直接翻訳した点で画期的で、トリエント公会議(1546)で公式聖書とされ、中世西欧キリスト教文化の言語的基盤となった。",
    primary_source_url=LATLIB+"bible.html",
    primary_source_type="Latin Library: Vulgata",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**CL, name_ja="アンブロシウス讃美歌・論考",
    name_en="Ambrose's Hymns and Treatises",
    name_original="Ambrosius",
    period_key="後期ローマ・教父期",
    definition="ミラノ司教アンブロシウス(c.340-397)のラテン讃美歌（『アンブロジオ聖歌』）と神学論考。讃美歌の四行詩定型「アンブロジアン讃歌律」を確立し、西欧讃美歌伝統の祖となった。アウグスティヌスを回心させた人物。",
    primary_source_url=LATLIB+"ambrose.html",
    primary_source_type="Latin Library: Ambrose",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CL, name_ja="グレゴリウス1世『対話』『道徳論』",
    name_en="Gregory the Great's Dialogues and Moralia",
    name_original="Gregorius Magnus",
    period_key="後期ローマ・教父期",
    definition="教皇グレゴリウス1世(c.540-604)の『対話四書』『ヨブ記註解（モラリア）』等。聖人伝の祖型『聖ベネディクトゥス伝』を含み、中世初期ヨーロッパの霊性・教会組織・聖人伝伝統の基盤を築いた。",
    primary_source_url=LATLIB+"gregory.html",
    primary_source_type="Latin Library: Gregory the Great",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CL, name_ja="プルデンティウス『プシュコマキア』",
    name_en="Prudentius' Psychomachia",
    name_original="Psychomachia",
    period_key="後期ローマ・教父期",
    definition="ヒスパニアの詩人プルデンティウス(c.348-413)による寓意叙事詩。徳と悪徳を擬人化した魂の戦いを描き、中世西欧寓意文学（『薔薇物語』『神曲』）の直接的祖型となった。",
    primary_source_url=LATLIB+"prudentius.html",
    primary_source_type="Latin Library: Prudentius",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: ビザンツ文学（6）
# ============================================================
add(**C, name_ja="プロコピオス『秘史（アネクドタ）』",
    name_en="Prokopios' Anekdota (Secret History)",
    name_original="Προκόπιος Ἀνέκδοτα",
    period_key="ビザンツ期",
    definition="カエサレイアのプロコピオス(c.500-565)が書いた皇帝ユスティニアヌス・テオドラ皇后への暴露書。公的著述『戦史』『建築物について』と対をなすビザンツ歴史叙述の重要文献。",
    primary_source_url=GUTEN+"ebooks/3837",
    primary_source_type="Project Gutenberg: Procopius Secret History",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アンナ・コムネナ『アレクシアス』",
    name_en="Anna Komnene's Alexiad",
    name_original="Ἄννα Κομνηνή Ἀλεξιάς",
    period_key="ビザンツ期",
    definition="皇女アンナ・コムネナ(1083-1153)が父アレクシオス1世の治世(1081-1118)を15巻で書いた歴史書。第一次十字軍をビザンツ側から記録した唯一文献で、女性歴史家の中世最重要著作。",
    primary_source_url=WIKI_EN+"Alexiad",
    primary_source_type="Wikipedia: Alexiad",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="フォティオス『ビブリオテーケー』",
    name_en="Photios' Bibliotheca",
    name_original="Φώτιος Μυριόβιβλος",
    period_key="ビザンツ期",
    definition="コンスタンティノープル総主教フォティオス(c.810-893)による280冊の古代・中世初期書物の要約・批評集。多くの散逸古典の唯一の証言として、ヘレニズム・初期ビザンツ文学史の根本資料となった。",
    primary_source_url=WIKI_EN+"Bibliotheca_(Photius)",
    primary_source_type="Wikipedia: Bibliotheca",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『スーダ』辞典",
    name_en="Suda lexicon",
    name_original="Σοῦδα",
    period_key="ビザンツ期",
    definition="10世紀末ビザンツ世界で編纂された約3万項目の歴史百科辞典。古代ギリシア・ローマ・初期ビザンツの人物・概念・文献を集成し、古典研究最重要中世参照源となった。",
    primary_source_url=WIKI_EN+"Suda",
    primary_source_type="Wikipedia: Suda",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="『ディゲニス・アクリタス』叙事詩",
    name_en="Digenes Akritas",
    name_original="Διγενῆς Ἀκρίτας",
    period_key="ビザンツ期",
    definition="12世紀頃成立したビザンツ口承叙事詩。アラブ系父・ビザンツ系母をもつ国境守備英雄ディゲニスの物語で、近代ギリシア語文学の祖型・ビザンツ叙事詩の最重要例として位置づけられる。",
    primary_source_url=WSRC_GR+"%CE%92%CE%B1%CF%83%CE%AF%CE%BB%CE%B5%CE%B9%CE%BF%CF%82_%CE%94%CE%B9%CE%B3%CE%B5%CE%BD%CE%AE%CF%82_%CE%91%CE%BA%CF%81%CE%AF%CF%84%CE%B7%CF%82",
    primary_source_type="Greek Wikisource: Digenes Akritas",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロマノス・メロドス『コンタキオン』",
    name_en="Romanos the Melodist's Kontakia",
    name_original="Ῥωμανὸς ὁ Μελωδός Κοντάκια",
    period_key="ビザンツ期",
    definition="ロマノス・メロドス(c.490-556)が作詞作曲したビザンツ典礼讃歌コンタキオン。物語的・劇的構造をもつ長篇典礼讃歌で、ビザンツ宗教詩・東方教会音楽の頂点として中世ギリシア詩の最高峰の一つ。",
    primary_source_url=WIKI_EN+"Romanos_the_Melodist",
    primary_source_type="Wikipedia: Romanos",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 古代後期諸論・諷刺・補遺（8）
# ============================================================
add(**C, name_ja="アリスティデス『ローマ頌』",
    name_en="Aelius Aristides' Roman Oration",
    name_original="Αἴλιος Ἀριστείδης Εἰς Ῥώμην",
    period_key="帝政ローマ時代（白銀期）",
    definition="アリスティデス(117-181)が155年頃に行った修辞演説。ローマ帝国の世界統治を讃美し、第二次ソフィスト運動・ローマ帝政期ギリシア弁論術の頂点とされる。",
    primary_source_url=WIKI_EN+"Aelius_Aristides",
    primary_source_type="Wikipedia: Aristides",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**CL, name_ja="ポセイディッポス・エピグラム",
    name_en="Posidippus' epigrams",
    name_original="Ποσείδιππος",
    period_key="ヘレニズム期",
    definition="ペッラのポセイディッポス(c.310-240 BCE)のエピグラム集。2001年公刊のミラノ・パピルス(P.Mil.Vogl. VIII 309)で108編が再発見され、ヘレニズム・エピグラム研究を一新した。",
    primary_source_url=WIKI_EN+"Posidippus_(epigrammatist)",
    primary_source_type="Wikipedia: Posidippus",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="セウェルス朝ラテン散文",
    name_en="Severan Latin prose",
    name_original="Latina Severiana",
    period_key="後期ローマ・教父期",
    definition="セウェルス朝期(193-235)のラテン散文文化。テルトゥリアヌス、ミヌキウス・フェリクス『オクタウィウス』、初期キリスト教護教論者のラテン文体形成期で、ラテン散文の世俗・宗教二重伝統の分岐点。",
    primary_source_url=WIKI_EN+"Latin_literature",
    primary_source_type="Wikipedia: Latin literature",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**CL, name_ja="アウソニウス『モセラ』ほか",
    name_en="Ausonius' Mosella and others",
    name_original="Ausonius Mosella",
    period_key="後期ローマ・教父期",
    definition="ボルドーの詩人アウソニウス(c.310-395)による教育・地理詩。『モセラ（ライン河支流モーゼル川を讃える地理詩）』『毎日の詩』等で、4世紀ガリア・ローマ詩文化の頂点を成した。",
    primary_source_url=LATLIB+"ausonius.html",
    primary_source_type="Latin Library: Ausonius",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="クラウディアヌス叙事詩",
    name_en="Claudian's epics",
    name_original="Claudianus",
    period_key="後期ローマ・教父期",
    definition="アレクサンドリア出身のラテン詩人クラウディアヌス(c.370-404)による政治叙事詩・讃美詩。『ホノリウス帝執政官就任讃』『プロセルピナの掠奪』等で、古代ラテン異教詩の最後の輝きを代表する。",
    primary_source_url=LATLIB+"claudian.html",
    primary_source_type="Latin Library: Claudian",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**CL, name_ja="シドニウス・アポリナリス書簡",
    name_en="Sidonius Apollinaris' letters",
    name_original="Sidonius Apollinaris",
    period_key="後期ローマ・教父期",
    definition="ガリアのシドニウス・アポリナリス(c.430-489)の書簡9巻と讃美詩。西ローマ帝国崩壊期(5世紀後半)の貴族・司教生活を記録し、古代ラテン書簡文学伝統の最後の主要作品となった。",
    primary_source_url=LATLIB+"sidonius.html",
    primary_source_type="Latin Library: Sidonius",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ロンギノス『崇高について』",
    name_en="Pseudo-Longinus' On the Sublime",
    name_original="Περὶ Ὕψους",
    period_key="帝政ローマ時代（白銀期）",
    definition="1世紀頃の作者不詳ギリシア語文学批評書（伝ロンギノス）。「崇高（hypsos）」概念を中心に文体論・霊感論を展開し、ボワロー1674年仏訳以降、近代美学・崇高論の祖型として決定的影響を与えた。",
    primary_source_url=PERSEUS+"text?doc=Perseus:text:1999.01.0258",
    primary_source_type="Perseus: Longinus",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ノンノス『ディオニュソス物語』",
    name_en="Nonnus' Dionysiaca",
    name_original="Νόννος Διονυσιακά",
    period_key="後期ローマ・教父期",
    definition="パノポリスのノンノス(c.5世紀)による48巻のギリシア最後の異教叙事詩。ディオニュソスのインド遠征を主題とし、古代ギリシア叙事詩伝統の最終形態として中世ビザンツ・近世欧州神話文学に影響した。",
    primary_source_url=WIKI_EN+"Dionysiaca",
    primary_source_type="Wikipedia: Dionysiaca",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# fourth_transform_axes attachments (>= 12)
# ============================================================
def _attach_axes(name: str, axes: list[dict]):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("fourth_axes", []).extend(axes)
            return


def _attach_cross(name: str, cds: list[dict]):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("cross_domain", []).extend(cds)
            return


_attach_axes("サッポー断片", [
    {"axis":"主体","status":"rethinking",
     "rationale":"女性的エロスの一人称主観的表白は、AI生成における主観的感情表出の真正性問題と理論的に対比される古典的祖型。",
     "related_ai_phenomenon":"AI生成における一人称感情表出の真正性"}])

_attach_axes("ピンダロス勝利歌（オリュンピア・ピューティア）", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"競技勝者を讃える定型的高唱形式は、AI生成における称賛・評価表現のパターン化と理論的に共振する。",
     "related_ai_phenomenon":"AI生成における評価・称賛文の定型化"}])

_attach_axes("テオクリトス『田園詩』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"牧歌的シミュレーション言語は、AI生成における仮想空間・牧歌的世界生成の祖型として理論化される。",
     "related_ai_phenomenon":"AI生成における牧歌的・仮想世界生成"}])

_attach_axes("ルキアノス諷刺対話", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"『真実の話』の自己言及的虚構宣言は、AI生成テキストにおける虚構性・真偽境界の問題を理論化する古典的祖型。",
     "related_ai_phenomenon":"AI生成における虚構性宣言と真偽境界"}])

_attach_axes("アプレイウス『黄金のロバ（変身物語）』詳述", [
    {"axis":"主体","status":"rethinking",
     "rationale":"動物変身による主体の変容と非人称化は、AI生成における主体の脱人称化・形態変容と理論的に並行する。",
     "related_ai_phenomenon":"AI環境における主体の非人称化・変容"}])

_attach_axes("アウグスティヌス『告白』", [
    {"axis":"主体","status":"rethinking",
     "rationale":"内省的自伝主体の発明は、AI時代の自己記述・ライフログにおける主体性問題の歴史的祖型。",
     "related_ai_phenomenon":"AI環境におけるライフログ・自己記述主体"}])

_attach_axes("ボエティウス『哲学の慰め』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"獄中で哲学を擬人化対話相手として召喚する構造は、AI対話エージェントとの哲学的対話の中世的祖型。",
     "related_ai_phenomenon":"AI対話エージェントとの哲学的対話"}])

_attach_axes("ヒエロニムス『ウルガタ訳』", [
    {"axis":"言語","status":"rethinking",
     "rationale":"原典から直接翻訳する規範形式は、AI多言語翻訳の権威性・規範性問題を理論化する歴史的祖型。",
     "related_ai_phenomenon":"AI多言語翻訳における権威性・規範形成"}])

_attach_axes("『スーダ』辞典", [
    {"axis":"受容","status":"rethinking",
     "rationale":"百科全書的編纂と要約は、現代の検索・要約AIによる知識集成の中世的祖型。",
     "related_ai_phenomenon":"AI要約・知識集成と百科全書性"}])

_attach_axes("プロコピオス『秘史（アネクドタ）』", [
    {"axis":"作者性","status":"rethinking",
     "rationale":"公的著述と秘密暴露書の二重執筆構造は、AI時代の表向き発信と暴露チャンネルの分裂と理論的に対比される。",
     "related_ai_phenomenon":"AI時代の表向き発信と暴露チャンネルの分裂"}])

_attach_axes("ロンギノス『崇高について』", [
    {"axis":"真正性","status":"rethinking",
     "rationale":"崇高（hypsos）の文体論はAI生成テキストの「強度」「感動」評価可能性を理論化する古典的祖型。",
     "related_ai_phenomenon":"AI生成における崇高性・強度の評価"}])

_attach_axes("プルタルコス『対比列伝』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"伝記対比形式は、AI生成における人物比較・並列叙述の機械的構築可能性と理論的に並行する。",
     "related_ai_phenomenon":"AI生成における人物比較・並列叙述"}])

_attach_axes("ヘリオドロス『エチオピア物語』", [
    {"axis":"物語","status":"rethinking",
     "rationale":"非線形・回想的物語構造は、AI生成における非線形物語生成・時系列再構築の古典的祖型。",
     "related_ai_phenomenon":"AI生成における非線形物語の構築"}])


# ============================================================
# cross_domain links (>= 10)
# ============================================================
_attach_cross("プルタルコス『対比列伝』", [
    {"target_db":"MG","link_type":"shared_concept",
     "target_entity_name":"リーダーシップ伝記論",
     "description":"古代ギリシア・ローマ政治家伝記対比は、近代経営学の比較リーダーシップ研究の歴史的祖型。"}])

_attach_cross("ルキアノス諷刺対話", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"諷刺・対話形式詩学",
     "description":"古代諷刺対話形式は、エラスムス・スウィフト・ヴォルテールを介して近代諷刺詩学の規範となった。"}])

_attach_cross("テオクリトス『田園詩』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"パストラル詩学",
     "description":"テオクリトス田園詩はウェルギリウス・ルネサンス田園詩・近代パストラル詩学の祖型。"}])

_attach_cross("ヘリオドロス『エチオピア物語』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"古代恋愛小説詩学",
     "description":"古代恋愛小説形式はバフチン『小説の詩学』のクロノトポス論の主要研究対象。"}])

_attach_cross("ロンゴス『ダフニスとクロエ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"パストラル恋愛小説詩学",
     "description":"ロンゴスはルネサンス田園小説・近代田園詩学（ルソー、ゲーテ）の直接祖型。"}])

_attach_cross("アウグスティヌス『告白』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"内省的主体の哲学",
     "description":"アウグスティヌス内省的主体はデカルト・ルソー以降の近代主体哲学の歴史的祖型。"}])

_attach_cross("アウグスティヌス『神の国』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"歴史哲学・政治神学",
     "description":"二つの国の構造論は中世以降の歴史哲学・政治神学の基盤理論。"}])

_attach_cross("ボエティウス『哲学の慰め』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"運命論・摂理論",
     "description":"ボエティウスの運命・摂理論は中世ヨーロッパ哲学・神学の中心主題となった。"}])

_attach_cross("アンナ・コムネナ『アレクシアス』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"女性歴史叙述・ジェンダー史",
     "description":"中世女性史家による政治史叙述として、現代ジェンダー史・人類学的歴史記述の祖型。"}])

_attach_cross("ヒエロニムス『ウルガタ訳』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"翻訳詩学・聖典翻訳論",
     "description":"ヒエロニムス翻訳論は近代翻訳詩学・聖典翻訳論の歴史的祖型。"}])

_attach_cross("『スーダ』辞典", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"百科全書的知識集成",
     "description":"中世ビザンツ百科辞典は、古典学・知識史研究の根本資料・参照源。"}])

_attach_cross("ロンギノス『崇高について』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"崇高論・近代美学",
     "description":"ロンギノス崇高論はボワロー仏訳以降、バーク・カント崇高論・近代美学の祖型。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
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
        print(f"[c01-w13-retry] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c01-w13-retry] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c01-w13-retry] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
