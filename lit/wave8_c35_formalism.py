"""
LIT-DB Phase 2 — C35: Theory-Formalism (形式主義・新批評・記号論)
================================================================
Inserts 40 canonical concepts spanning 5 categories:
  A. Russian Formalism (8)
  B. Czech Structuralism / Prague School (8)
  C. Anglo-American New Criticism (8)
  D. Semiotics / Structuralist Poetics (8)
  E. Major critical concepts (8)

Sources: SEP, JSTOR (PD/open citations), Project MUSE abstracts,
Cambridge Companions, Critical Inquiry, university press OA pages.
'primary' tier = direct theorist's published essay/book reference.
'secondary' = standard scholarly reference work surveys.

Pattern: Formalism/Structuralism school knowledge core. Region='理論'.
subfield_code='lit_theory' (id=22).

This file is non-overlapping with C34 (postcolonial), C36 (feminist),
C37 (eco-criticism) — those occupy theory subfield concurrently but
in distinct theoretical regions of the field.
"""
from __future__ import annotations

import sys
from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (theory periods relevant to formalism/structuralism)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("ロシア・フォルマリズム期", "Russian Formalism Era", 1914, 1930,
     "OPOJAZ・モスクワ言語学サークルを起点とする、文学性（literariness）を科学的対象として確立した時代。"),
    ("プラハ言語学サークル期", "Prague Linguistic Circle Era", 1926, 1948,
     "Mukarovsky・Jakobsonらが構造主義詩学・美的機能論・前景化理論を体系化した時代。"),
    ("英米新批評期", "Anglo-American New Criticism Era", 1929, 1960,
     "I.A. Richards・Empson・Brooks・Wimsatt らが close reading とテクスト内在批評を確立した時代。"),
    ("構造主義詩学期", "Structuralist Poetics Era", 1957, 1975,
     "Saussure言語学を継承し、Jakobson・Greimas・Hjelmslev らが文学言語の体系記述を進めた時代。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Russian Formalism (8)
# ===============================================================

add({
    "name_ja": "OPOJAZ（詩的言語研究会）",
    "name_en": "OPOJAZ (Society for the Study of Poetic Language)",
    "name_original": "ОПОЯЗ (Общество изучения поэтического языка)",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "1916年ペトログラードで Shklovsky・Eikhenbaum・Tynianov・Brik らが結成した詩的言語研究会。詩的言語と日常言語の差異を科学的に記述し、文学性（literariness）を分析対象として確立した。モスクワ言語学サークル（Jakobson主導）と並ぶロシア・フォルマリズム双翼の一極。",
    "background": "象徴主義の神秘主義的詩論への反動と、ボードゥアン・ド・クルトネに源流をもつ言語学的客観主義の合流として成立した。",
    "development": "1930年頃ソヴィエト体制下で解散させられたが、その理論的遺産はプラハ学派・チェコ構造主義・テル・アヴィヴ詩学に継承され、1960年代以降の西側構造主義の前史として再発見された。",
    "historical_context": "ロシア革命前後のアヴァンギャルド芸術運動と並走した文学科学化の試み。",
    "primary_source_url": "https://plato.stanford.edu/entries/literary-theory/",
    "primary_source_type": "SEP — Literary Theory entry",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "形式主義の創設",
    "name_en": "founding of formalism",
    "name_original": "формализм",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Shklovsky「言語の復活」（1914）「手法としての芸術」（1917）を起点とする、文学を社会的・心理的還元から切り離し「形式」「手法（priem）」「文学性」として研究する学派の成立。テクスト内在的詩学の20世紀的最初の体系化。",
    "background": "文献学的伝統批判と、詩的言語の自律性主張という二つの方向の接合点として現れた。",
    "development": "Eikhenbaum・Tynianov・Jakobson・Tomashevsky らが共同で詩学・物語論・文学史理論を発展させ、後のプラハ構造主義・記号論・ナラトロジーの母胎となった。",
    "historical_context": "前衛芸術（フトゥーリズム）と科学的言語学の同時代的接合。",
    "primary_source_url": "https://www.jstor.org/stable/468475",
    "primary_source_type": "JSTOR — Eichenbaum 'The Theory of the Formal Method'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "形式主義の「文学性」概念は、AI生成テクストが文学テクストとして識別可能かを問う現代的議論の歴史的尺度として再活性化している。",
         "related_ai_phenomenon": "AI生成テクストの文学性判定問題"},
    ],
})

add({
    "name_ja": "「ゴーゴリの『外套』はいかにして作られたか」",
    "name_en": "How Gogol's 'Overcoat' Is Made",
    "name_original": "Как сделана «Шинель» Гоголя",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Eikhenbaum 1919年の論文。ゴーゴリ短編『外套』を社会批評的「小役人への同情」読解から解放し、滑稽な語り口（skaz）と悲哀的場面の交替という形式手法の連鎖として再記述した、形式主義的読みの範例的実践。",
    "background": "リベラル批評がゴーゴリを「リアリズムの祖」として読んできた伝統に対する、形式手法分析による解体。",
    "development": "skaz（語り口）概念は Bakhtin の対話性論・ナラトロジーの voice 概念へと継承された。",
    "historical_context": "ロシア社会批評と形式主義との方法論的衝突の象徴的著作。",
    "primary_source_url": "https://www.jstor.org/stable/467324",
    "primary_source_type": "JSTOR — Eichenbaum essay translation",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Tynianov 文学的進化論",
    "name_en": "Tynianov's literary evolution",
    "name_original": "литературная эволюция",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Tynianov『文学的進化について』（1927）が提示した、文学を作品連続でなく「関係システムの変動」として捉える歴史理論。先行体系の支配的要素が周縁化し新要素が中心へ移行する力学が文学史を駆動するとする。",
    "background": "形式主義の非歴史的批判への自己応答として、形式と歴史の媒介を志向した。",
    "development": "プラハ学派の構造-体系論、Bakhtin のクロノトポス論、ロトマンの記号圏論、Even-Zohar のポリシステム論へと展開した。",
    "historical_context": "形式主義後期の歴史理論への自己反省段階。",
    "primary_source_url": "https://www.jstor.org/stable/1772349",
    "primary_source_type": "JSTOR — Tynianov essay",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ドミナント（支配的要素）",
    "name_en": "the dominant",
    "name_original": "доминанта",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Jakobson が定式化した、芸術作品中で他の構成要素を統御し変形させる中心的要素の概念。作品・ジャンル・時代様式それぞれにドミナントが存在し、その移行が芸術史の力学を構成するとされた。",
    "background": "Tynianov の文学的進化論の発展形として、構造の階層化原理を導入した。",
    "development": "プラハ構造主義の階層的体系論、Mukarovsky 美学、ジャコブソンの「言語の六機能」におけるドミナント機能論へと連続する。",
    "historical_context": "形式主義後期からプラハ学派への理論的橋渡し。",
    "primary_source_url": "https://www.jstor.org/stable/2906018",
    "primary_source_type": "JSTOR — Jakobson 'The Dominant'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "シュジェートとファーブラ",
    "name_en": "sjuzhet and fabula",
    "name_original": "сюжет / фабула",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Shklovsky・Tomashevsky による物語の二層区分。ファーブラ（fabula）は出来事の年代的因果連鎖の素材、シュジェート（sjuzhet）はそれをテクスト上で配列・遅延・変形した形式構成。物語の「何」と「いかに」を分離する装置。",
    "background": "アリストテレス『詩学』のmythos/logos区分の近代言語学的再定式化。",
    "development": "Genette の histoire/récit/narration三層論、Chatman の story/discourse、Bal のナラトロジーへと体系化された。",
    "historical_context": "物語論を自律的研究領域として確立した最初の概念対。",
    "primary_source_url": "https://www.jstor.org/stable/1772313",
    "primary_source_type": "JSTOR — Tomashevsky 'Thematics'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "モチヴェーション（動機づけ）",
    "name_en": "motivation",
    "name_original": "мотивировка",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Tomashevsky『主題論』（1925）が定式化した、文学的手法を作品内で正当化する装置。リアリズム的・構成的・芸術的の三型に分類され、形式主義は手法の自律性を、それを覆い隠す「動機づけ」と区別して論じた。",
    "background": "リアリズム小説における細部の機能を形式手法として再分析する必要から導入された。",
    "development": "Barthes の「現実効果」、Genette のverisimilitude論、現代の物語技法分析へと継承された。",
    "historical_context": "リアリズム読解を形式主義的に脱構築する装置。",
    "primary_source_url": "https://www.jstor.org/stable/1772313",
    "primary_source_type": "JSTOR — Tomashevsky 'Thematics'",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "異化（理論的定式）",
    "name_en": "ostranenie / defamiliarization (theoretical formulation)",
    "name_original": "остранение",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Shklovsky『手法としての芸術』（1917）が中心理論として定式化した、自動化された日常知覚を脱慣習化し対象を「初めて見るように」現出させる芸術の根本機能。形式主義における芸術の存在論的定義。",
    "background": "象徴主義詩学の神秘主義的霊感論を、知覚の現象学的更新原理へと置き換えた理論的革新。",
    "development": "Brecht の異化効果（V-Effekt）、現象学的美学、Mukarovsky の前景化理論、生成芸術論まで連続する。",
    "historical_context": "ロシア・アヴァンギャルドの知覚革命と並走する理論化。",
    "primary_source_url": "https://warwick.ac.uk/fac/arts/english/currentstudents/undergraduate/modules/fulllist/special/en304/syllabus2017-18/shklovsky.pdf",
    "primary_source_type": "Shklovsky 'Art as Technique' English translation (PD)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "AI生成出力が「自動化された慣習」の延長か、それとも新たな異化を生むかという議論において、Shklovsky の理論は中心的尺度として参照される。",
         "related_ai_phenomenon": "AI生成テクストの新鮮さ／陳腐さ判定"},
    ],
})


# ===============================================================
# CATEGORY B — Czech Structuralism / Prague School (8)
# ===============================================================

add({
    "name_ja": "プラハ言語学サークル",
    "name_en": "Prague Linguistic Circle",
    "name_original": "Pražský lingvistický kroužek",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "1926年プラハで Vilém Mathesius らが創設した言語学・詩学共同体。亡命ロシア人 Jakobson・Trubetzkoy が合流し、機能主義的構造主義を確立。文学研究では Mukarovsky を中心に美学・記号論を展開した、20世紀構造主義の主要発生地。",
    "background": "ロシア・フォルマリズムの方法論をチェコ言語学伝統と接合し、より体系的・哲学的に深化させた。",
    "development": "1948年共産党政権下で解散したが、Jakobson が米国に亡命し1950-60年代の構造主義国際化の起点となった。Tartu-Moscow 学派・パリ構造主義への直接的影響源。",
    "historical_context": "戦間期中欧の知的コスモポリタニズムの結晶点。",
    "primary_source_url": "https://plato.stanford.edu/entries/structuralism/",
    "primary_source_type": "SEP — Structuralism entry",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Mukarovsky 美的機能",
    "name_en": "Mukarovsky's aesthetic function",
    "name_original": "estetická funkce",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "Jan Mukarovsky『美的機能・規範・価値』（1936）が提示した、対象の実用的機能を背景化し記号自体への注意を前景化する社会的に変動する機能。美的価値の客観性を社会的規範と価値の関係として記述した構造主義美学の基本概念。",
    "background": "形式主義の手法論を、社会的記号過程の枠組みへと拡張した。",
    "development": "Eco の美的機能論、Bourdieu の文化生産場理論、現代の制度的美学論へと展開した。",
    "historical_context": "戦間期チェコ機能主義美学の中核。",
    "primary_source_url": "https://www.jstor.org/stable/430349",
    "primary_source_type": "JSTOR — Mukarovsky scholarship",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Vodicka 具現化（コンクレチザツィオン）",
    "name_en": "Vodicka's concretization",
    "name_original": "konkretizace",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "Felix Vodicka が Ingarden の具現化概念を発展させ、文学作品が異なる時代の読者規範のもとで具体化される歴史的過程として理論化したもの。テクストの構造的不確定箇所と読者期待地平の相互作用として作品受容史を記述する。",
    "background": "プラハ学派の構造主義をテクスト受容の歴史化へと拡張した試み。",
    "development": "Iser・Jauss の受容美学、現代の reception studies の理論的祖型となった。",
    "historical_context": "東欧構造主義における歴史性の組み込み。",
    "primary_source_url": "https://www.jstor.org/stable/468474",
    "primary_source_type": "JSTOR — Vodicka translation",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "前景化",
    "name_en": "foregrounding",
    "name_original": "aktualisace / foregrounding",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "Mukarovsky・Havránek が定式化した、詩的言語が標準言語の規範からの体系的逸脱によって言語形式自体への注意を喚起する作用。Shklovsky の異化を言語学的に精密化し、文体論・詩学の科学的基盤を提供する概念。",
    "background": "ロシア形式主義の異化を、機能主義言語学の枠組みで再定式化した。",
    "development": "英語圏では Garvin の翻訳経由で Halliday の機能文体論、Leech の詩学、現代の認知文体論へ継承された。",
    "historical_context": "形式主義から構造主義言語学への概念連続の象徴。",
    "primary_source_url": "https://www.jstor.org/stable/468475",
    "primary_source_type": "JSTOR — Garvin Prague School Reader",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "「言語学と詩学」",
    "name_en": "Linguistics and Poetics",
    "name_original": "Linguistics and Poetics",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Roman Jakobson 1958年Indiana 学際会議閉会講演（1960年Sebeok 編 Style in Language 所収）。詩学を言語学の不可欠な部門と位置づけ、コミュニケーション六要素・六機能モデルを提示し、詩的機能をメッセージ自体への配向として定義した記念碑的論考。",
    "background": "プラハ学派の機能主義詩学を、Shannon-Weaver の情報理論的伝達モデルと接合した。",
    "development": "Barthes・Todorov・Genette らの構造主義詩学、Culler の文学言語学、現代のスタイロメトリーまで影響を与え続ける。",
    "historical_context": "戦後米国における構造主義導入の起点。",
    "primary_source_url": "https://www.jstor.org/stable/40290672",
    "primary_source_type": "JSTOR — Jakobson 'Linguistics and Poetics'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "Jakobson の六機能モデルは、AIエージェントとの対話における機能配分（参照／詩的／メタ言語的等）の分析枠組みとしてHCI研究で再活性化している。",
         "related_ai_phenomenon": "AI対話におけるコミュニケーション機能の配分分析"},
    ],
})

add({
    "name_ja": "言語の六機能",
    "name_en": "six functions of language",
    "name_original": "six functions",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Jakobson が提示した、コミュニケーション六要素（送信者・受信者・コンテクスト・メッセージ・コンタクト・コード）に対応する六機能モデル：表出的・能動的・指示的・詩的・交話的・メタ言語的。各テクストはこれら機能の配分構造として記述される。",
    "background": "Bühler の三機能モデル（表出・喚起・表象）の三要素拡張版。",
    "development": "メタ言語機能論はメタフィクション批評、交話的機能はオンライン・コミュニケーション分析へと応用された。",
    "historical_context": "言語学的詩学の最も流通した理論モデル。",
    "primary_source_url": "https://www.jstor.org/stable/40290672",
    "primary_source_type": "JSTOR — Jakobson 'Linguistics and Poetics'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "AIエージェントの応答における六機能配分（特にメタ言語機能と詩的機能の比率）は、AI対話の様式論的分析の基盤として再注目されている。",
         "related_ai_phenomenon": "AI生成テクストの言語機能プロファイル分析"},
    ],
})

add({
    "name_ja": "ドミナント機能",
    "name_en": "dominant function",
    "name_original": "dominant function",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Jakobson 六機能モデルにおいて、特定テクストで他機能を従属化させ全体構造を規定する中心的機能。詩的テクストでは詩的機能、科学テクストでは指示的機能、儀礼的テクストでは交話的機能が支配的になり、ジャンル分類の言語学的基準を提供する。",
    "background": "形式主義のドミナント概念を機能モデルに適用した。",
    "development": "テクスト類型論、機能主義スタイロメトリー、ジャンル分析の理論的基盤として継続使用される。",
    "historical_context": "構造主義詩学のジャンル理論の定式。",
    "primary_source_url": "https://www.jstor.org/stable/2906018",
    "primary_source_type": "JSTOR — Jakobson 'The Dominant'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ロシア=チェコ理論的接続",
    "name_en": "Russian-Czech theoretical connection",
    "name_original": "Russian-Czech connection",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "1920年代後半、亡命ロシア人 Jakobson・Bogatyrev・Trubetzkoy がプラハに移り、ロシア・フォルマリズムの方法論をチェコ言語学伝統に接合することで生まれた知的継承関係。形式主義の文学性概念を構造主義的体系論として展開する移行を可能にした。",
    "background": "ロシア革命期の知識人亡命と、チェコスロヴァキア共和国の知的開放性の交差。",
    "development": "戦後の Tartu-Moscow 学派は形式主義-プラハ学派遺産の再活性化として位置づけられる。",
    "historical_context": "東中欧構造主義の地政学的成立条件。",
    "primary_source_url": "https://plato.stanford.edu/entries/structuralism/",
    "primary_source_type": "SEP — Structuralism entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY C — Anglo-American New Criticism (8)
# ===============================================================

add({
    "name_ja": "『実践批評』",
    "name_en": "Practical Criticism",
    "name_original": "Practical Criticism: A Study of Literary Judgment",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "I.A. Richards 1929年刊。著者・年代を伏せた詩を学生に読ませた「プロトコル実験」を分析し、読者が陥る四種の障害（紋切型反応・教義的偏見・感傷性・技法盲目）を体系化。close reading 教育の方法論的起点。",
    "background": "Cambridge 英文学批評の心理学的基礎づけ運動の成果。",
    "development": "Empson・Brooks・Wimsatt の実践に直接影響し、英米批評教育の標準モデルとなった。",
    "historical_context": "英文学を大学制度的学問として確立する過程。",
    "primary_source_url": "https://archive.org/details/practicalcritici030144mbp",
    "primary_source_type": "Internet Archive — Richards Practical Criticism",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "『曖昧性の七つの型』",
    "name_en": "Seven Types of Ambiguity",
    "name_original": "Seven Types of Ambiguity",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "William Empson 1930年刊。詩の言語が複数の意味を同時に作動させる現象を七型に分類した著作（語の複数義、文法的曖昧性、二語文脈、二意味文脈、明白なアナロジー、矛盾、根本的二重性）。close reading の理論的精度を画期的に高めた。",
    "background": "Richards の指導下、Cambridge の精緻な詩読解実践から生まれた。",
    "development": "Brooks の paradox 論、Hartman の脱構築的読解、Empson 自身の後期『複合語の構造』までの理論的拡張へ連続。",
    "historical_context": "20世紀英米批評史の方法論的画期点。",
    "primary_source_url": "https://archive.org/details/seventypesofambi0000emps",
    "primary_source_type": "Internet Archive — Empson Seven Types",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "『よく作られた壺』",
    "name_en": "The Well Wrought Urn",
    "name_original": "The Well Wrought Urn: Studies in the Structure of Poetry",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Cleanth Brooks 1947年刊。Donne「列聖」からYeats まで10篇の詩の close reading を通じ、詩の本質をパラドクスとアイロニーによる矛盾要素の有機的統一として規定した、新批評の代表的方法論的著作。",
    "background": "新批評の方法論的成熟期に書かれた、close reading の範例集。",
    "development": "1950-60年代の英米詩学教育の標準教科書として絶大な影響を持ち、Wimsatt-Beardsley 論文と共に新批評の正典を構成した。",
    "historical_context": "戦後米国大学英文学プログラムの方法論的標準化。",
    "primary_source_url": "https://archive.org/details/wellwroughturn00broo",
    "primary_source_type": "Internet Archive — Brooks Well Wrought Urn",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "意図の誤謬",
    "name_en": "intentional fallacy",
    "name_original": "intentional fallacy",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "W.K. Wimsatt と M.C. Beardsley「意図の誤謬」（Sewanee Review 1946）が提唱した、作者の意図を作品意味の判定基準とする誤謬。意味は作品自体に客観的に存在し、作者意図への遡及は判定の根拠とならないとする新批評の中核原理。",
    "background": "ロマン派批評の作者中心主義への体系的批判として登場した。",
    "development": "1960年代以降 Hirsch の意図主義復権・Knapp/Michaels の反論などを経て長期論争を生み、Barthes「作者の死」と並ぶ反作者主義の起点となった。",
    "historical_context": "新批評のテクスト内在主義の理論的支柱。",
    "primary_source_url": "https://www.jstor.org/stable/27537676",
    "primary_source_type": "JSTOR — Wimsatt & Beardsley 'Intentional Fallacy'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "AI共著・LLM生成テクストにおける「作者意図」の所在問題は、意図の誤謬論を新たな次元で再考させる。誰の意図を参照するのか自体が再定義されている。",
         "related_ai_phenomenon": "AI共著テクストの作者性・意図帰属問題"},
    ],
})

add({
    "name_ja": "感情の誤謬",
    "name_en": "affective fallacy",
    "name_original": "affective fallacy",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Wimsatt と Beardsley「感情の誤謬」（Sewanee Review 1949）が提唱した、読者の心理的反応を作品評価の基準とする誤謬。判定は作品自体の構造的特性に基づくべきで、読者効果への還元は批評を心理学・印象論へ解消するとする。",
    "background": "意図の誤謬と対をなす、新批評のテクスト客観主義の二本柱の片方。",
    "development": "受容美学・読者反応批評（Iser・Fish）はこの誤謬論への直接の挑戦として展開された。",
    "historical_context": "新批評期の批評客観性主張の極限的定式。",
    "primary_source_url": "https://www.jstor.org/stable/27538420",
    "primary_source_type": "JSTOR — Wimsatt & Beardsley 'Affective Fallacy'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "クロース・リーディング（精読法）",
    "name_en": "close reading method",
    "name_original": "close reading",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "テクストの語・句・修辞構造を逐一精査し、内的整合性と緊張関係を詳細に分析する読みの方法。新批評が制度化し、英米大学文学教育の中核を成してきた。形式主義的細部精査と批評的判断を統合する実践技法。",
    "background": "Richards の実践批評と Empson の曖昧性分析が共同で確立した。",
    "development": "脱構築・新歴史主義は close reading を批判的に拡張・対抗した。Moretti の distant reading が量的反対概念として提案された。",
    "historical_context": "20世紀英文学制度の方法論的中核。",
    "primary_source_url": "https://www.jstor.org/stable/24590110",
    "primary_source_type": "JSTOR — Critical Inquiry close reading retrospective",
    "importance_score": 5,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "AI による distant reading の自動化と、人間の close reading の役割再定義は、文学研究方法論の現代的中心論争を構成する。",
         "related_ai_phenomenon": "AI による distant reading vs 人間 close reading の役割分担"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "distant reading / 量的文学分析",
         "description": "close reading の対立概念として AI による distant reading が出現し、両者の役割分担が現代文学研究の方法論的論争点となっている。"},
    ],
})

add({
    "name_ja": "詩におけるパラドクス",
    "name_en": "paradox in poetry",
    "name_original": "paradox",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Brooks『よく作られた壺』第1章「詩の言語としてのパラドクス」が定式化した、詩の言語が論理的矛盾を恒常的に包含し統一する性質。日常言語の指示的明晰性に対し、詩は両立不可能な要素を同時に肯定する独自の論理空間を形成するとされる。",
    "background": "Donne 形而上詩派研究を通じて、詩的言語の本質的特性として理論化された。",
    "development": "脱構築批評は新批評のパラドクス論を、有機的統一を脅かす差異の戯れへと再解釈した。",
    "historical_context": "新批評期の有機的統一説の中核命題。",
    "primary_source_url": "https://archive.org/details/wellwroughturn00broo",
    "primary_source_type": "Internet Archive — Brooks Ch.1",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "構造的アイロニー",
    "name_en": "irony as structural principle",
    "name_original": "structural irony",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Brooks が定式化した、詩の意味を構成する諸要素が文脈的圧力下で相互に修正・限定し合う構造原理としてのアイロニー。修辞的アイロニー（言葉の表裏）を超え、テクスト全体の意味生成の動的様式とされる。",
    "background": "Empson の曖昧性論を、構造的緊張原理へと拡張した。",
    "development": "de Man の修辞的読解、現代の物語的アイロニー理論まで継承された。",
    "historical_context": "新批評の有機的統一説を支える緊張原理。",
    "primary_source_url": "https://www.jstor.org/stable/27538420",
    "primary_source_type": "JSTOR — Brooks 'Irony as Principle of Structure'",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY D — Semiotics / Structuralist Poetics (8)
# ===============================================================

add({
    "name_ja": "Saussure 記号",
    "name_en": "Saussurean signe",
    "name_original": "signe",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Ferdinand de Saussure『一般言語学講義』（1916）が定式化した、シニフィアン（音響イメージ）とシニフィエ（概念）の不可分な結合体としての記号概念。記号の恣意性・体系内差異性原理は構造主義言語学・記号論・文学理論の出発点となった。",
    "background": "新文法派・歴史言語学への反動として、共時的体系記述の優位を主張した。",
    "development": "Hjelmslev・Jakobson によって精緻化され、Barthes・Lévi-Strauss・Lacan を経て、Derrida の脱構築によって批判的に再展開された。",
    "historical_context": "20世紀人文学全体の言語論的転回の起点。",
    "primary_source_url": "https://plato.stanford.edu/entries/saussure/",
    "primary_source_type": "SEP — Saussure entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "言語哲学における記号論",
         "description": "Saussure 記号論は20世紀言語哲学（言語論的転回）の基盤を構成する。"},
    ],
})

add({
    "name_ja": "シニフィアンとシニフィエ",
    "name_en": "signifier and signified",
    "name_original": "signifiant / signifié",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Saussure 記号の二側面。シニフィアン（音響イメージ）は感覚的形式、シニフィエ（概念）は精神的内容を指し、両者の結合は社会慣習による恣意的なものとされる。両者間の関係様式が記号の理論的核心。",
    "background": "ストア派・スコラ哲学の signum-significatum 区別の近代言語学的再定式化。",
    "development": "Lacan は精神分析にこの区別を導入しシニフィアン優位を主張、Derrida は両者の純粋区別自体を脱構築した。",
    "historical_context": "現代記号論の理論的最小単位。",
    "primary_source_url": "https://plato.stanford.edu/entries/saussure/",
    "primary_source_type": "SEP — Saussure entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "統合体軸と範列体軸",
    "name_en": "syntagmatic and paradigmatic axes",
    "name_original": "syntagmatique / paradigmatique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Saussure が言語記号の関係を分析する二軸。統合体軸（syntagmatic）は線状的連鎖（隣接・組み合わせ）、範列体軸（paradigmatic）は記憶上の対立・選択関係。Jakobson は前者をメトニミー、後者をメタファーに対応づけて文学言語分析に応用した。",
    "background": "Saussure の体系内差異性原理を関係軸として精密化したもの。",
    "development": "構造主義人類学（Lévi-Strauss）、記号論、Greimas 意味論、現代の認知言語学まで広く展開された。",
    "historical_context": "構造主義方法論の基本ツール。",
    "primary_source_url": "https://plato.stanford.edu/entries/saussure/",
    "primary_source_type": "SEP — Saussure entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ラングとパロール",
    "name_en": "langue and parole",
    "name_original": "langue / parole",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Saussure の言語の二層区分。ラング（langue）は社会的・体系的言語規則の総体、パロール（parole）は個別話者の具体的発話実践。言語学はラングを科学的対象とすべきとされ、構造主義方法論の基本姿勢となった。",
    "background": "個別事象と一般体系の区分問題への言語学的応答。",
    "development": "Chomsky の competence/performance 区別、Bakhtin の発話論によるパロール側からの反論、社会言語学による相対化を経て継続使用される。",
    "historical_context": "構造主義の方法論的基盤。",
    "primary_source_url": "https://plato.stanford.edu/entries/saussure/",
    "primary_source_type": "SEP — Saussure entry",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Jakobson メタファー／メトニミーの二軸",
    "name_en": "Jakobson's metaphor and metonymy axes",
    "name_original": "metaphor / metonymy axes",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Jakobson『言語の二側面と失語症の二型』（1956）が提示した、言語選択（範列軸＝類似性＝メタファー）と結合（統合軸＝隣接性＝メトニミー）の根本対立。詩はメタファー軸の優位、散文はメトニミー軸の優位として体系化された。",
    "background": "失語症の臨床観察を体系的言語学的二分法へと一般化した試み。",
    "development": "Lacan の精神分析（隠喩-換喩-無意識）、構造主義文体論、認知言語学のメタファー論まで広く影響を与えた。",
    "historical_context": "失語症学と詩学の交差点。",
    "primary_source_url": "https://www.jstor.org/stable/40290672",
    "primary_source_type": "JSTOR — Jakobson 'Two Aspects of Language'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Greimas 記号論四角形",
    "name_en": "Greimas's semiotic square",
    "name_original": "carré sémiotique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Algirdas Julien Greimas『構造意味論』（1966）が提示した、意味体系を二項対立（S1-S2）と各々の否定（非S1-非S2）の四角形で記述する形式モデル。物語論・神話分析・社会記号論の構造記述ツールとして広く応用された。",
    "background": "Saussure の差異原理と Hjelmslev の形式論を物語意味論に応用した試み。",
    "development": "Jameson『政治的無意識』が文学批評に応用、ナラトロジー・社会記号論・現代の概念分析に広く採用される。",
    "historical_context": "パリ構造主義記号論の中核形式装置。",
    "primary_source_url": "https://www.jstor.org/stable/468477",
    "primary_source_type": "JSTOR — Greimas semiotic square scholarship",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "Hjelmslev 言理学",
    "name_en": "Hjelmslev's glossematics",
    "name_original": "glossématique",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Louis Hjelmslev『言語理論序説』（1943）が提示した、Saussure 言語学を最も形式化した理論体系。表現面と内容面それぞれが質料と形式に分かれ、計四象限の組み合わせとして記号過程を記述する。文学理論には Barthes・Eco を経て影響した。",
    "background": "コペンハーゲン学派の言語哲学的厳密化志向の極限。",
    "development": "Barthes『記号学要綱』、Eco『記号論』、現代のメディア記号論で継続使用される。",
    "historical_context": "20世紀構造主義の最も抽象的形式化。",
    "primary_source_url": "https://plato.stanford.edu/entries/structuralism/",
    "primary_source_type": "SEP — Structuralism entry",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "セミオーシス（記号過程）",
    "name_en": "semiosis",
    "name_original": "semiosis",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "C.S. Peirce が定式化し Eco が継承した、記号が解釈項を生み解釈項が新たな記号となる無限の意味生成過程。Saussure の二項記号モデルに対し、Peirce は記号-対象-解釈項の三項モデルを提示し、開放的意味過程として記号活動を記述した。",
    "background": "Peirce の現象論的論理学を基礎とする三項記号論の核心概念。",
    "development": "Eco『開かれた作品』『読者の役割』、現代のバイオセミオティクス、Hoffmeyer の進化記号論まで展開された。",
    "historical_context": "Saussure 系構造主義への米国記号論からの根本的代案。",
    "primary_source_url": "https://plato.stanford.edu/entries/peirce-semiotics/",
    "primary_source_type": "SEP — Peirce's Theory of Signs",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ===============================================================
# CATEGORY E — Major critical concepts (8)
# ===============================================================

add({
    "name_ja": "文学性",
    "name_en": "literariness",
    "name_original": "литературность",
    "original_script": "cyrillic",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Jakobson が定式化した、テクストを文学たらしめる固有の質。「文学研究の対象は文学ではなく文学性である」というスローガンに集約され、形式主義の研究対象規定の中核となった。日常言語との関係における詩的言語の差異的特性として記述される。",
    "background": "文学研究を社会史・心理学・文化史への還元から自立させる試みの中心概念。",
    "development": "プラハ学派の前景化、ジャコブソンの詩的機能、Culler の文学慣習論、現代のスタイロメトリーによる定量的接近まで継続課題。",
    "historical_context": "20世紀文学研究の自律化運動の中核標語。",
    "primary_source_url": "https://www.jstor.org/stable/468475",
    "primary_source_type": "JSTOR — Eichenbaum 'Theory of Formal Method'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "AI生成テクストが文学的か否かを判定する尺度として、文学性概念は形式主義以来初めて実証的検証の対象となっている。",
         "related_ai_phenomenon": "AI生成テクストの文学性検出・スタイロメトリー"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "AI生成テクストの文学性検出",
         "description": "AI開発DBの文学性検出研究の歴史的概念基盤として文学性概念が参照される。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩学における文学性",
         "description": "Poetics DBの中核概念との直接共有。"},
    ],
})

add({
    "name_ja": "異化（理論的精緻化）",
    "name_en": "defamiliarization (theoretical refinement)",
    "name_original": "defamiliarization",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "プラハ言語学サークル期",
    "definition": "Shklovsky の ostranenie 概念をプラハ学派・英米批評が理論的に精緻化した形態。Mukarovsky の前景化、Brecht の V-Effekt、現代の認知文体論における「文体的逸脱」効果まで連続する、異化機構の汎理論的定式。",
    "background": "ロシア形式主義の中核概念の各国翻訳・転用過程で多層化された。",
    "development": "認知文体論・現代神経美学が異化効果の脳科学的相関を実証研究するまでに至る。",
    "historical_context": "ロシア形式主義から現代美学への概念継承の象徴。",
    "primary_source_url": "https://www.jstor.org/stable/468475",
    "primary_source_type": "JSTOR — Shklovsky scholarship survey",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "創造性", "status": "rethinking",
         "rationale": "AI出力の「新鮮さ」を異化効果として測定する研究、また AI が異化効果を意図的に生成可能かという論争は、defamiliarization の理論的射程を再定義しつつある。",
         "related_ai_phenomenon": "AI による意図的異化効果の生成と測定"},
    ],
})

add({
    "name_ja": "有機的統一",
    "name_en": "organic unity",
    "name_original": "organic unity",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Coleridge を起点とし新批評が継承・体系化した、芸術作品が部分の有機的相互依存により全体が部分の総和を超える統一性を持つとする原理。Brooks の構造的アイロニー論はこの統一を緊張要素間の動的均衡として再定義した。",
    "background": "ロマン派美学の有機体論を、テクスト分析の方法論的前提へと制度化した。",
    "development": "脱構築・新歴史主義は有機的統一説を批判対象とし、テクストの内的亀裂・外的決定要因を強調する方向へ展開した。",
    "historical_context": "新批評の存在論的前提。",
    "primary_source_url": "https://archive.org/details/wellwroughturn00broo",
    "primary_source_type": "Internet Archive — Brooks Well Wrought Urn",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "アイロニー類型論",
    "name_en": "typology of irony",
    "name_original": "typology of irony",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Frye『批評の解剖』、Booth『アイロニーの修辞学』が体系化した、アイロニーの種別（言語的・状況的・劇的・宇宙的・ロマン主義的等）の理論的分類。新批評・構造主義詩学を経て、修辞学・物語論・ジャンル論を貫く分析装置となった。",
    "background": "新批評の構造的アイロニー論と、修辞学的伝統の合流。",
    "development": "現代のメタアイロニー論、ポストモダン批評のアイロニー再評価まで継続課題として残る。",
    "historical_context": "20世紀後半の修辞批評の中核装置。",
    "primary_source_url": "https://www.jstor.org/stable/27538420",
    "primary_source_type": "JSTOR — Booth 'Rhetoric of Irony' reviews",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "曖昧性の類型",
    "name_en": "ambiguity types",
    "name_original": "types of ambiguity",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "英米新批評期",
    "definition": "Empson が分類した詩的曖昧性の七型（複数義的語、文法的曖昧、文脈的二義、二意味重畳、明白なアナロジー、自己矛盾、根本的二重性）が起点となり、現代の語用論・修辞学・認知詩学において継続発展されている、テクスト的多義性の体系的記述。",
    "background": "Empson の精密読解実践と分析哲学の意味論的関心の交差。",
    "development": "Riffaterre の生成的読解、現代の認知文体論、AI 自然言語処理の意味曖昧性解消（WSD）の概念基盤となった。",
    "historical_context": "新批評と意味論研究の交差点。",
    "primary_source_url": "https://archive.org/details/seventypesofambi0000emps",
    "primary_source_type": "Internet Archive — Empson Seven Types",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "AI の自然言語理解における意味曖昧性解消（WSD）は、Empson の七型の現代的工学化と見なせる。",
         "related_ai_phenomenon": "AI の意味曖昧性解消・多義語処理"},
        {"axis": "受容", "status": "partial",
         "rationale": "曖昧性が読者に開く解釈の自由度は、AI による「最尤解釈」の選択と緊張関係に立つ。",
         "related_ai_phenomenon": "AI 解釈の収束 vs 人間読解の発散"},
    ],
})

add({
    "name_ja": "構造的アイロニー（理論的拡張）",
    "name_en": "structural irony (theoretical extension)",
    "name_original": "structural irony (extended)",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Brooks の構造的アイロニー概念を、構造主義詩学が物語全体構造を規定する原理として拡張したもの。テクストの諸層（語り・人物・出来事）間の不一致が体系的に意味を生成する装置として理論化された。",
    "background": "新批評の修辞的アイロニーと、ナラトロジーの語り手-人物関係論の結合。",
    "development": "Genette の焦点化論、Booth の信頼できない語り手、現代のメタフィクション批評まで継承された。",
    "historical_context": "新批評と構造主義詩学の方法論的接続点。",
    "primary_source_url": "https://www.jstor.org/stable/468474",
    "primary_source_type": "JSTOR — structural irony scholarship",
    "importance_score": 3,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "物語文法",
    "name_en": "narrative grammar",
    "name_original": "narrative grammar",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "構造主義詩学期",
    "definition": "Propp『昔話の形態学』（1928）を起点とし、Greimas・Todorov・Bremond らが体系化した、物語を有限の機能・行為項の規則的組み合わせとして記述する形式理論。文学を文法的体系として分析する構造主義詩学の到達点の一つ。",
    "background": "Propp のロシア魔法昔話分析（31機能）が、フランス構造主義によって全物語に拡張された。",
    "development": "Genette のナラトロジー、Bal の語りの理論、現代のコンピュテーショナル物語論まで連続する。",
    "historical_context": "形式主義から構造主義への物語論的継承の頂点。",
    "primary_source_url": "https://www.jstor.org/stable/468477",
    "primary_source_type": "JSTOR — Propp/Greimas narrative grammar surveys",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "モチーフ分析",
    "name_en": "motif analysis",
    "name_original": "motif analysis",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ロシア・フォルマリズム期",
    "definition": "Veselovsky『歴史詩学』を起点とし、Tomashevsky『主題論』（1925）が体系化した、物語の最小主題単位（モチーフ）と、それを連結する束（主題）の関係としてプロットを分析する方法。物語論・比較文学・民俗学を貫く方法論。",
    "background": "比較文学的主題索引（Aarne-Thompson）の理論的基礎づけ。",
    "development": "プラハ学派の主題論、Frye の元型批評、現代の認知物語論におけるスキーマ理論まで継承された。",
    "historical_context": "ロシア比較文学伝統の形式主義的再定式化。",
    "primary_source_url": "https://www.jstor.org/stable/1772313",
    "primary_source_type": "JSTOR — Tomashevsky 'Thematics'",
    "importance_score": 3,
    "source_tier": "primary",
    "canonical_in_region": "major",
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------

RELATIONS: list[tuple[str, str, str, str]] = [
    # Within Russian Formalism
    ("OPOJAZ（詩的言語研究会）", "形式主義の創設", "contains",
     "OPOJAZ は形式主義創設の制度的母体を成した。"),
    ("形式主義の創設", "「ゴーゴリの『外套』はいかにして作られたか」", "contains",
     "Eikhenbaum の『外套』論は形式主義方法論の範例的実践。"),
    ("形式主義の創設", "異化（理論的定式）", "contains",
     "Shklovsky の異化論は形式主義創設期の中核理論。"),
    ("形式主義の創設", "シュジェートとファーブラ", "contains",
     "シュジェート/ファーブラ区分は形式主義物語論の基本装置。"),
    ("形式主義の創設", "モチヴェーション（動機づけ）", "contains",
     "モチヴェーション概念は形式主義リアリズム分析の中核。"),
    ("形式主義の創設", "文学性", "contains",
     "文学性は形式主義の研究対象規定の中核標語。"),
    ("Tynianov 文学的進化論", "ドミナント（支配的要素）", "extends",
     "ドミナント概念は文学的進化論の構造化原理として展開された。"),
    ("形式主義の創設", "Tynianov 文学的進化論", "extends",
     "文学的進化論は形式主義後期の歴史理論への自己反省。"),
    ("モチーフ分析", "シュジェートとファーブラ", "influences",
     "モチーフ分析はファーブラ層の最小単位記述を提供する。"),

    # Russian to Czech
    ("OPOJAZ（詩的言語研究会）", "ロシア=チェコ理論的接続", "extends",
     "OPOJAZ メンバーの亡命がプラハ学派形成の起点となった。"),
    ("ロシア=チェコ理論的接続", "プラハ言語学サークル", "extends",
     "プラハ学派はロシア形式主義の理論的継承体として成立した。"),
    ("異化（理論的定式）", "前景化", "extends",
     "プラハ学派の前景化はロシア異化論の言語学的精緻化。"),
    ("異化（理論的定式）", "異化（理論的精緻化）", "extends",
     "プラハ学派・英米批評での精緻化が異化論を多層化した。"),
    ("ドミナント（支配的要素）", "ドミナント機能", "extends",
     "形式主義のドミナントが Jakobson 機能モデルでドミナント機能として再定式化された。"),

    # Within Czech
    ("プラハ言語学サークル", "Mukarovsky 美的機能", "contains",
     "Mukarovsky 美学はプラハ学派文学理論の中核。"),
    ("プラハ言語学サークル", "前景化", "contains",
     "前景化概念はプラハ学派の文体論的核心。"),
    ("プラハ言語学サークル", "Vodicka 具現化（コンクレチザツィオン）", "contains",
     "Vodicka 具現化論はプラハ学派の受容理論。"),
    ("Mukarovsky 美的機能", "Vodicka 具現化（コンクレチザツィオン）", "influences",
     "美的機能の社会的可変性が具現化理論の前提となる。"),

    # Czech to Jakobson Structuralism
    ("プラハ言語学サークル", "「言語学と詩学」", "influences",
     "プラハ学派詩学の集大成として Jakobson の言語学詩学講演が展開された。"),
    ("「言語学と詩学」", "言語の六機能", "contains",
     "六機能モデルは「言語学と詩学」で初めて体系的提示された。"),
    ("言語の六機能", "ドミナント機能", "contains",
     "六機能モデルはドミナント機能による配分構造として作動する。"),
    ("Jakobson メタファー／メトニミーの二軸", "「言語学と詩学」", "extends",
     "メタファー/メトニミー二軸論は Jakobson 詩学講演の前提理論。"),

    # Saussure structuralism
    ("Saussure 記号", "シニフィアンとシニフィエ", "contains",
     "Saussure 記号は signifiant/signifié の不可分結合として定義される。"),
    ("Saussure 記号", "統合体軸と範列体軸", "contains",
     "Saussure 言語学は記号関係を統合/範列の二軸で分析する。"),
    ("Saussure 記号", "ラングとパロール", "contains",
     "Saussure はラング/パロール区分を言語学の対象規定に置いた。"),
    ("統合体軸と範列体軸", "Jakobson メタファー／メトニミーの二軸", "extends",
     "Jakobson は範列軸=メタファー、統合軸=メトニミーとして文学言語に適用した。"),
    ("Saussure 記号", "Hjelmslev 言理学", "extends",
     "Hjelmslev は Saussure 言語学を最も形式化した体系として展開した。"),
    ("Hjelmslev 言理学", "Greimas 記号論四角形", "influences",
     "Greimas 四角形は Hjelmslev 形式論を物語意味論に応用した形式装置。"),
    ("Saussure 記号", "セミオーシス（記号過程）", "criticizes",
     "Peirce の三項記号論は Saussure 二項モデルへの代替的代案。"),

    # New Criticism internal
    ("『実践批評』", "『曖昧性の七つの型』", "influences",
     "Richards の指導下で Empson の曖昧性論が生まれた。"),
    ("『曖昧性の七つの型』", "曖昧性の類型", "contains",
     "Empson の七型分類が曖昧性類型論の起点。"),
    ("『実践批評』", "クロース・リーディング（精読法）", "extends",
     "Richards のプロトコル分析が close reading 教育の起点となった。"),
    ("クロース・リーディング（精読法）", "『よく作られた壺』", "contains",
     "Brooks 詩読解は close reading の方法論的範例。"),
    ("『よく作られた壺』", "詩におけるパラドクス", "contains",
     "Brooks 第1章はパラドクスを詩の言語の本質と定義した。"),
    ("『よく作られた壺』", "構造的アイロニー", "contains",
     "Brooks は構造的アイロニーを詩の組織原理と論じた。"),
    ("『よく作られた壺』", "有機的統一", "contains",
     "Brooks の構造論は有機的統一説の新批評的定式。"),
    ("意図の誤謬", "感情の誤謬", "extends",
     "Wimsatt-Beardsley の二誤謬論はテクスト客観主義の双柱。"),
    ("意図の誤謬", "クロース・リーディング（精読法）", "influences",
     "意図の誤謬論は close reading のテクスト内在主義を理論的に支える。"),
    ("詩におけるパラドクス", "曖昧性の類型", "influences",
     "Brooks のパラドクス論は Empson の曖昧性論の構造化的継承。"),
    ("構造的アイロニー", "構造的アイロニー（理論的拡張）", "extends",
     "Brooks のアイロニー論が構造主義詩学で物語全体構造へと拡張された。"),

    # Cross-school
    ("文学性", "前景化", "influences",
     "文学性概念は前景化として言語学的に操作的定義を得た。"),
    ("文学性", "クロース・リーディング（精読法）", "influences",
     "文学性概念は close reading のテクスト精査対象を規定する。"),
    ("物語文法", "シュジェートとファーブラ", "extends",
     "物語文法は形式主義の二層モデルを構造主義的に拡張した形式。"),
    ("物語文法", "Greimas 記号論四角形", "contains",
     "物語文法は Greimas 四角形を行為項体系の記述に組み込む。"),
    ("セミオーシス（記号過程）", "解釈の開放性", "extends",
     "セミオーシスは解釈の無限開放性として記号過程を描く（Eco『開かれた作品』への展開）。"),
    ("Mukarovsky 美的機能", "前景化", "influences",
     "美的機能は前景化として実装される、というのが Mukarovsky の中心命題。"),
]


# ---------------------------------------------------------------
# Cross-domain links to add post-insertion
# Format: (concept_name_ja, target_db, link_type, target_entity_name, description)
# ---------------------------------------------------------------

EXTRA_CROSS_DOMAIN: list[tuple[str, str, str, str, str]] = [
    # PHIL connections
    ("シニフィアンとシニフィエ", "PHIL", "shared_concept",
     "言語哲学における記号論",
     "Saussure 記号論は言語哲学（Ricoeur・Derrida）の中核概念として継承された。"),
    ("ラングとパロール", "PHIL", "shared_concept",
     "言語哲学における体系と発話",
     "Wittgenstein 後期の言語ゲーム論との比較哲学的接点を持つ。"),
    ("Jakobson メタファー／メトニミーの二軸", "PHIL", "shared_concept",
     "認知意味論におけるメタファー",
     "Lakoff-Johnson 概念メタファー理論の言語学的祖型。"),
    ("セミオーシス（記号過程）", "PHIL", "shared_concept",
     "Peirce のプラグマティズム記号論",
     "Peirce 哲学体系の中核概念として PHIL DBで参照される。"),
    # PT (Poetics) connections
    ("「言語学と詩学」", "PT", "shared_concept",
     "言語学的詩学の確立",
     "Poetics DBの言語学的詩学パラダイムの起点文献として参照される。"),
    ("シュジェートとファーブラ", "PT", "shared_concept",
     "プロット理論の二層モデル",
     "Poetics DBのプロット理論の中核装置。"),
    ("物語文法", "PT", "shared_concept",
     "ナラトロジーの形式理論",
     "Poetics DBの物語論パラダイムの構造主義的定式。"),
    # AN (Anthropology) connections
    ("統合体軸と範列体軸", "AN", "shared_concept",
     "Lévi-Strauss 構造人類学の方法論",
     "Lévi-Strauss は神話分析に Saussure 二軸論を直接応用した。"),
    ("物語文法", "AN", "shared_concept",
     "Lévi-Strauss 神話素分析",
     "Propp 形態学から Lévi-Strauss 神話論への継承は構造主義の中軸。"),
    ("Greimas 記号論四角形", "AN", "shared_concept",
     "構造人類学における意味四角形",
     "Greimas 四角形は構造人類学の親族・神話分析にも適用された。"),
    # AI-Development connections
    ("文学性", "AI-Development", "parallel",
     "AI生成テクスト識別研究",
     "AI開発DBの文学性検出・スタイロメトリー研究の歴史的概念基盤。"),
    ("クロース・リーディング（精読法）", "AI-Development", "parallel",
     "distant reading / 量的文学分析",
     "Moretti の distant reading 提案は AI 文学分析時代の方法論的対立軸を構成する。"),
    ("曖昧性の類型", "AI-Development", "parallel",
     "意味曖昧性解消（WSD）",
     "Empson 七型は AI の WSD タスクの概念的祖型。"),
    ("意図の誤謬", "AI-Development", "parallel",
     "AI共著テクストの意図帰属問題",
     "意図の誤謬論は LLM 共著時代の作者性論争で再活性化される。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave8_c35_formalism] inserting {len(CONCEPTS)} concepts...")
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
                name_ja=name_ja, region="理論",
                start_year=sy, end_year=ey,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"  period: {name_ja!r} -> id={pid}")

        # 2) Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)  # shallow copy
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
                    print(f"  [error fourth] {entry['name_ja']}: {e}")

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
                    print(f"  [error cross_domain] {entry['name_ja']}: {e}")

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r}"
                      f" (sid={sid}, tid={tid})")
                continue
            try:
                db.insert_relation(
                    source_type="concept", source_id=sid,
                    target_type="concept", target_id=tid,
                    relation_type=rtype,
                    description=desc,
                    confidence=4,
                )
                relation_count += 1
            except LitDBError as e:
                print(f"  [error relation] {src_name} -> {tgt_name}: {e}")

        # 4) Extra cross-domain links
        for concept_name, target_db, link_type, target_name, desc in EXTRA_CROSS_DOMAIN:
            cid = name_to_id.get(concept_name)
            if not cid:
                print(f"  [warn] cross_domain skipped: concept missing {concept_name!r}")
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
                print(f"  [error extra cross_domain] {concept_name}: {e}")

        # 5) Summary
        summary = db.progress_summary()
        # Cumulative subfield 22 count
        sub22 = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id=22"
        ).fetchone()
        print()
        print("[wave8_c35_formalism] inserted:")
        print(f"  concepts (total): {summary['concepts']}")
        print(f"  concepts (subfield_id=22 cumulative): {sub22['c']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")
        print(f"  source_tier dist: {db.tier_distribution()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
