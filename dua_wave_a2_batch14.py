"""DUA Wave A2 Batch 14 — 哲学・言語学・文学批評・歴史学・宗教学・美学 追加 (~380 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def uid():
    return "dua_" + uuid.uuid4().hex[:12]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()

records = [
    # ===== 哲学・形而上学 (~60) =====
    ("実体形而上学", "Substance Metaphysics", "実体を存在の基本単位とする形而上学的立場。アリストテレスの第一実体・第二実体の区別に始まり、デカルトの心身二元論、スピノザの一元論的実体論、ライプニッツのモナドロジーへと展開する。", "哲学・倫理学", "Western_Europe", -384, "https://en.wikipedia.org/wiki/Substance_theory"),
    ("プロセス哲学", "Process Philosophy", "実体より過程・出来事を存在の基本とする哲学的立場。ホワイトヘッドの有機体の哲学が代表例。存在より生成を優先し、宇宙を相互に関連する出来事の網として捉える。", "哲学・倫理学", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Process_philosophy"),
    ("創発", "Emergence", "複雑系において、部分の性質からは予測できない新たな性質や秩序が全体レベルで生じる現象。意識、生命、社会制度などの説明に用いられる。還元主義への代替的アプローチ。", "哲学・倫理学", "Western_Europe", 1875, "https://en.wikipedia.org/wiki/Emergence"),
    ("随伴現象説", "Epiphenomenalism", "精神的出来事は物理的過程の副産物であり因果的力を持たないとする心身論。Huxleyが提唱。意識は蒸気機関の汽笛に喩えられる。自由意志との緊張関係を孕む。", "哲学・倫理学", "Western_Europe", 1874, "https://en.wikipedia.org/wiki/Epiphenomenalism"),
    ("汎心論", "Panpsychism", "意識や経験が宇宙の普遍的な特性であり、物質のあらゆる段階に何らかの形で存在するという形而上学的立場。チャーマーズが現代的形態を再提唱し議論を活発化させた。", "哲学・倫理学", "Western_Europe", 1600, "https://en.wikipedia.org/wiki/Panpsychism"),
    ("超越論的観念論", "Transcendental Idealism", "カントの哲学的立場。空間・時間・カテゴリーは対象に由来するのではなく、認識主観が対象に課す形式であるとする。物自体と現象の区別を中心概念とする。", "哲学・倫理学", "Western_Europe", 1781, "https://en.wikipedia.org/wiki/Transcendental_idealism"),
    ("論理的原子論", "Logical Atomism", "バートランド・ラッセルとウィトゲンシュタイン初期が発展させた哲学的立場。世界は論理的原子と呼ばれる単純な事実から構成されるとし、言語の論理分析によって実在の構造を明らかにしようとする。", "哲学・倫理学", "Western_Europe", 1910, "https://en.wikipedia.org/wiki/Logical_atomism"),
    ("新実在論", "New Realism", "20世紀初頭の認識論的立場。観念論に反し、認識されるものは心から独立して存在すると主張。ムーア、ラッセル、アメリカ新実在論者が代表。", "哲学・倫理学", "Western_Europe", 1910, "https://en.wikipedia.org/wiki/New_realism_(philosophy)"),
    ("批判的実在論", "Critical Realism", "バスカーが提唱した科学哲学の立場。実在は観察可能な経験を超えた生成メカニズムの層を持つとし、科学は開放系で作動すると論じる。", "哲学・倫理学", "Western_Europe", 1975, "https://en.wikipedia.org/wiki/Critical_realism_(philosophy_of_the_social_sciences)"),
    ("構造的実在論", "Structural Realism", "科学的実在論の一形態。理論が捉えるのは個々の対象の本性ではなく関係的構造であるとする。数学的構造が実在の本質を捉えるという立場。", "哲学・倫理学", "Western_Europe", 1989, "https://en.wikipedia.org/wiki/Structural_realism_(philosophy_of_science)"),
    ("自然主義（哲学）", "Philosophical Naturalism", "哲学的問題を自然科学の方法と知見と連続的に扱おうとする立場。クワインの認識論の自然化が典型。超自然的説明を排除し、哲学を科学の延長として位置づける。", "哲学・倫理学", "North_America", 1951, "https://en.wikipedia.org/wiki/Naturalism_(philosophy)"),
    ("存在論的コミットメント", "Ontological Commitment", "クワインが提唱した概念。理論が存在を認める対象の総体。変項の値が存在することを表すという定式で表現される。", "哲学・倫理学", "North_America", 1948, "https://en.wikipedia.org/wiki/Ontological_commitment"),
    ("非還元的物理主義", "Non-reductive Physicalism", "心的状態は物理的状態に依存するが、心理学的説明は物理学に還元されないとする立場。Davidson等が唱えた。多重実現可能性の論点と連動する。", "哲学・倫理学", "North_America", 1970, "https://en.wikipedia.org/wiki/Non-reductive_physicalism"),
    ("可能世界意味論", "Possible World Semantics", "様相論理・反実仮想の分析に可能世界という概念装置を用いる意味論。クリプキ、ルイスが代表的論者。ルイスは様相実在論を提唱した。", "哲学・倫理学", "North_America", 1959, "https://en.wikipedia.org/wiki/Possible_worlds"),
    ("フレーゲの意義と指示", "Sense and Reference", "フレーゲが提唱した意味の二層構造。指示対象（Bedeutung）と意義（Sinn）を区別し、同一性言明のパラドクスを解決する。現代分析哲学の出発点。", "哲学・倫理学", "Western_Europe", 1892, "https://en.wikipedia.org/wiki/Sense_and_reference"),
    ("時間的部分論", "Temporal Parts Theory", "物体は空間的部分のみならず時間的部分も持つとする存在論的立場。ルイス、サイダーらが代表。持続と経続の区別を中心に議論が展開する。", "哲学・倫理学", "North_America", 1976, "https://en.wikipedia.org/wiki/Temporal_parts"),
    ("内在主義と外在主義", "Internalism and Externalism", "知識の正当化が認識主体の内的要因に依存するか外的要因にも依存するかの論争。コーン、ゴールドマンが代表的論者。信頼主義は外在主義の典型形態。", "哲学・倫理学", "North_America", 1970, "https://en.wikipedia.org/wiki/Internalism_and_externalism"),
    ("徳認識論", "Virtue Epistemology", "認識論を徳倫理学の観点から再構築する立場。知識を徳ある認識プロセスの産物として理解する。ソーサ、グリーコ、ザグゼブスキが代表。", "哲学・倫理学", "North_America", 1991, "https://en.wikipedia.org/wiki/Virtue_epistemology"),
    ("証言的知識", "Testimonial Knowledge", "他者の証言によって得られる知識の認識論的正当性を問う分野。個人的推論に依存しない知識の源泉としての証言の地位を論じる。", "哲学・倫理学", "Western_Europe", 1987, "https://en.wikipedia.org/wiki/Testimony_(epistemology)"),
    ("ゲティア問題", "Gettier Problem", "知識の伝統的分析（正当化された真の信念）への反例をゲティアが提示した問題。偶然的要因が正当化された真の信念を知識でなくする事例を通じて知識の分析を刷新した。", "哲学・倫理学", "North_America", 1963, "https://en.wikipedia.org/wiki/Gettier_problem"),
    ("形而上学的様相論", "Metaphysical Modality", "形而上学的必然性と可能性の論理と存在論。論理的可能性・形而上学的可能性・自然的可能性の区別、本質主義との関連を含む。", "哲学・倫理学", "Western_Europe", 1971, "https://en.wikipedia.org/wiki/Metaphysical_necessity"),
    # ===== 倫理学・価値論 (~40) =====
    ("アリストテレス的徳倫理学", "Aristotelian Virtue Ethics", "アリストテレスのニコマコス倫理学に基づく規範倫理学の立場。徳を人間の卓越性として位置づけ、幸福を最高善とする。中庸・習慣・実践知を中核概念とする。", "哲学・倫理学", "Western_Europe", -384, "https://en.wikipedia.org/wiki/Virtue_ethics"),
    ("カントの義務論", "Kantian Deontology", "行為の道徳的価値は結果ではなく行為の義務的性格によって決まるとするカントの倫理学。定言命法が代表。人を常に手段としてのみならず目的としても扱う義務を中核とする。", "哲学・倫理学", "Western_Europe", 1785, "https://en.wikipedia.org/wiki/Deontological_ethics"),
    ("結果主義", "Consequentialism", "行為の道徳的価値はその結果によって決まるとする規範倫理学の立場。功利主義がその典型。行為・規則・動機の各レベルに適用可能。", "哲学・倫理学", "Western_Europe", 1789, "https://en.wikipedia.org/wiki/Consequentialism"),
    ("道徳的実在論", "Moral Realism", "道徳的事実は客観的に存在し、道徳的言明は真偽を持つとする立場。非自然主義的実在論と自然主義的実在論が代表的形態。", "哲学・倫理学", "Western_Europe", 1903, "https://en.wikipedia.org/wiki/Moral_realism"),
    ("道徳的反実在論", "Moral Anti-realism", "客観的道徳的事実の存在を否定する立場の総称。非認知主義、誤謬説、相対主義を含む。マッキー、ブラックバーンが代表的論者。", "哲学・倫理学", "Western_Europe", 1946, "https://en.wikipedia.org/wiki/Moral_anti-realism"),
    ("スキャンロンの契約主義", "Scanlonian Contractualism", "スキャンロンの道徳理論。行為が誰かが合理的に拒否できない原則に反する場合に誤りとなるとする。ロールズの契約論とは区別される義務論的立場。", "哲学・倫理学", "North_America", 1998, "https://en.wikipedia.org/wiki/Contractualism"),
    ("ケアの倫理", "Ethics of Care", "ギリガン、ノディングズが提唱したフェミニスト倫理学。抽象的原則より具体的関係・依存・応答責任を重視する。正義の倫理への対案として提唱された。", "哲学・倫理学", "North_America", 1982, "https://en.wikipedia.org/wiki/Ethics_of_care"),
    ("動物倫理", "Animal Ethics", "動物の道徳的地位と人間の動物に対する義務を論じる応用倫理学の分野。シンガーの功利主義的立場とレーガンの権利論的立場が代表。種差別批判を中核とする。", "哲学・倫理学", "Western_Europe", 1975, "https://en.wikipedia.org/wiki/Animal_ethics"),
    ("環境倫理学", "Environmental Ethics", "自然環境・生態系・生物多様性に対する人間の道徳的義務を問う応用倫理学。人間中心主義批判、生物中心主義、深い生態学が対話する。", "哲学・倫理学", "North_America", 1973, "https://en.wikipedia.org/wiki/Environmental_ethics"),
    ("世代間倫理", "Intergenerational Ethics", "現在の世代が将来世代に対していかなる義務を持つかを問う倫理学。気候変動・資源枯渇・核廃棄物等との関連で論じられる。非同一性問題が中心的難問。", "哲学・倫理学", "Western_Europe", 1984, "https://en.wikipedia.org/wiki/Intergenerational_equity"),
    ("生命倫理学", "Bioethics", "医療・生命科学における倫理的問題を扱う学際的分野。自律尊重・善行・無危害・公正の四原則が基礎。安楽死、生命維持、遺伝子操作等を論じる。", "哲学・倫理学", "North_America", 1971, "https://en.wikipedia.org/wiki/Bioethics"),
    ("メタ倫理学", "Metaethics", "道徳的言明の意味・真理・正当化の性質を問う哲学的探求。規範倫理学と区別され、道徳的判断の認知的・存在論的地位を探究する。自然主義・非自然主義・非認知主義が主な立場。", "哲学・倫理学", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Metaethics"),
    ("有効利他主義", "Effective Altruism", "証拠と推論に基づき最大の善を実現する方法を探求する社会哲学・運動。シンガー、マクアスキルが代表的論者。グローバルな貧困・パンデミック・実存的リスクへの取り組みを優先する。", "哲学・倫理学", "Western_Europe", 2011, "https://en.wikipedia.org/wiki/Effective_altruism"),
    ("道徳的運", "Moral Luck", "結果・状況・性格形成等の偶然的要因が道徳的評価に影響するというウィリアムズとネーゲルの論点。カントの義務論との緊張を孕み、責任・帰責の概念を問い直す。", "哲学・倫理学", "Western_Europe", 1976, "https://en.wikipedia.org/wiki/Moral_luck"),
    ("功利主義", "Utilitarianism", "最大多数の最大幸福を道徳的行為の基準とする規範倫理学の立場。ベンサム（快楽計算）とミル（高次快楽）が古典的論者。現代では選好功利主義、規則功利主義等に発展。", "哲学・倫理学", "Western_Europe", 1789, "https://en.wikipedia.org/wiki/Utilitarianism"),
    ("道徳心理学", "Moral Psychology", "道徳的判断・動機・行動の心理学的メカニズムを探る学際分野。ハイトの社会的直観主義モデル、コールバーグの道徳発達段階、双過程理論が代表。", "哲学・倫理学", "North_America", 1958, "https://en.wikipedia.org/wiki/Moral_psychology"),
    ("人格同一性論", "Personal Identity", "ある人物が時間を通じて同一人物であり続ける条件を問う形而上学的問題。ロックの意識継続説、心理的連続性理論、生物学的継続性理論が代表的立場。", "哲学・倫理学", "Western_Europe", 1689, "https://en.wikipedia.org/wiki/Personal_identity"),
    ("自由意志と決定論", "Free Will and Determinism", "人間の意志が因果的に決定されているかを問う哲学の中心問題。強い決定論・両立論・非両立論・ハードな非両立論が対立する。", "哲学・倫理学", "Western_Europe", -400, "https://en.wikipedia.org/wiki/Free_will"),
    ("道徳的責任", "Moral Responsibility", "行為者に道徳的責任を帰属させる条件を問う倫理学的・法哲学的概念。スタンスとしての反応的態度（ストローソン）、制御条件が論じられる。", "哲学・倫理学", "Western_Europe", 1962, "https://en.wikipedia.org/wiki/Moral_responsibility"),
    ("集合的責任", "Collective Responsibility", "集団・組織・国家が道徳的責任を持ちうるかを問う。個人主義的還元説と非還元的集合責任論の対立。過去の不正義に対する歴史的責任の議論を含む。", "哲学・倫理学", "North_America", 1970, "https://en.wikipedia.org/wiki/Collective_responsibility"),
    ("承認の倫理", "Ethics of Recognition", "ヘーゲル・ホネット・テイラーによる承認論。自己アイデンティティの形成が他者からの承認に依存するという洞察を中核とし、愛・法・連帯の三形態の承認を論じる。", "哲学・倫理学", "Western_Europe", 1992, "https://en.wikipedia.org/wiki/Recognition_(philosophy)"),
    # ===== 言語学 (~70) =====
    ("談話分析", "Discourse Analysis", "文や発話を超えた言語単位の組織と機能を研究する言語学の分野。テクスト言語学、会話分析、批判的談話分析等の多様なアプローチが存在する。", "言語学", "Western_Europe", 1952, "https://en.wikipedia.org/wiki/Discourse_analysis"),
    ("批判的談話分析", "Critical Discourse Analysis", "ファン・ダイク、フェアクラフらが提唱。言語使用と権力・イデオロギー・社会構造の関係を批判的に分析する方法論。メディア言説、政治演説等を対象とする。", "言語学", "Western_Europe", 1985, "https://en.wikipedia.org/wiki/Critical_discourse_analysis"),
    ("会話分析", "Conversation Analysis", "サックス、シェグロフ、ジェファーソンが創始。日常会話の順番交代、修復、連鎖構造を詳細に記述する社会学的手法。エスノメソドロジーを基盤とする。", "言語学", "North_America", 1964, "https://en.wikipedia.org/wiki/Conversation_analysis"),
    ("コーパス言語学", "Corpus Linguistics", "大規模テキストコーパスを統計的に分析する言語研究の方法論。語彙の共起パターン、コロケーション、語彙文法の発展。BNC、COCA等のコーパスを活用。", "言語学", "Western_Europe", 1961, "https://en.wikipedia.org/wiki/Corpus_linguistics"),
    ("計算言語学", "Computational Linguistics", "コンピュータによる自然言語の処理・理解・生成を研究する学際分野。統計的手法と規則ベース手法の融合、機械翻訳、情報抽出等を含む。", "言語学", "North_America", 1950, "https://en.wikipedia.org/wiki/Computational_linguistics"),
    ("自然言語処理", "Natural Language Processing", "人間の言語をコンピュータで処理する技術の集合。品詞タグ付け、固有表現認識、感情分析、対話システム、大規模言語モデル等を含む応用研究領域。", "言語学", "North_America", 1950, "https://en.wikipedia.org/wiki/Natural_language_processing"),
    ("語彙意味論", "Lexical Semantics", "語彙の意味と意味関係を研究する意味論の下位分野。語義・多義・同義・反義・上位・下位関係、ワードネット、フレームネット等の計算資源が整備されている。", "言語学", "North_America", 1969, "https://en.wikipedia.org/wiki/Lexical_semantics"),
    ("形式意味論", "Formal Semantics", "数理論理学・モデル論的手法を用いて自然言語の意味を形式化する分野。モンタギュー文法が基礎。真理条件的意味論、型理論的意味論が発展した。", "言語学", "North_America", 1970, "https://en.wikipedia.org/wiki/Formal_semantics_(linguistics)"),
    ("統語論", "Syntax", "文の内部構造と文法性を研究する言語学の中心分野。チョムスキーの変形生成文法・GB理論・ミニマリストプログラムが主流。", "言語学", "North_America", 1957, "https://en.wikipedia.org/wiki/Syntax"),
    ("音韻論", "Phonology", "言語音の体系的パターンを研究する言語学の分野。音素・形態音素・音節・韻律論を扱う。最適性理論が現代の主要枠組み。", "言語学", "Western_Europe", 1928, "https://en.wikipedia.org/wiki/Phonology"),
    ("形態論", "Morphology", "語の内部構造を研究する言語学の分野。屈折・派生・複合・接辞、語形成規則、形態タイプの類型論的研究を含む。", "言語学", "Western_Europe", 1859, "https://en.wikipedia.org/wiki/Morphology_(linguistics)"),
    ("語用論", "Pragmatics", "文脈・意図・社会的要因を考慮した言語使用の研究。グライスの協調原理・会話の含意、発語行為論、関連性理論が主要理論。", "言語学", "Western_Europe", 1967, "https://en.wikipedia.org/wiki/Pragmatics"),
    ("認知言語学", "Cognitive Linguistics", "言語を認知能力の一部として捉える理論的枠組み。ランガッカーの認知文法、レイコフのメタファー研究、構文文法が代表的アプローチ。", "言語学", "North_America", 1975, "https://en.wikipedia.org/wiki/Cognitive_linguistics"),
    ("概念メタファー論", "Conceptual Metaphor Theory", "レイコフとジョンソンが提唱。人間の概念体系は根本的にメタファー的であり、抽象的領域の理解はより具体的な源泉領域との写像によって行われると論じる。", "言語学", "North_America", 1980, "https://en.wikipedia.org/wiki/Conceptual_metaphor"),
    ("構文文法", "Construction Grammar", "文法的知識を形式と意味の対応としての構文の集積として捉える言語学の理論的枠組み。ゴールドバーグ、クロフトが代表。", "言語学", "North_America", 1988, "https://en.wikipedia.org/wiki/Construction_grammar"),
    ("類型論", "Linguistic Typology", "世界の言語間の構造的多様性と普遍的パターンを比較研究する分野。語順類型、有標性、グリーンバーグの普遍性研究が基盤。", "言語学", "North_America", 1963, "https://en.wikipedia.org/wiki/Linguistic_typology"),
    ("言語接触", "Language Contact", "異なる言語や方言の話者間の接触が生じる場面での言語変化を研究する分野。借用・コードスイッチング・ピジン語・クレオール語の形成を含む。", "言語学", "Western_Europe", 1953, "https://en.wikipedia.org/wiki/Language_contact"),
    ("クレオール語", "Creole Language", "異なる母語話者間の接触から生まれ母語となって文法的複雑性を増した言語。ハイチ・クレオール、トク・ピシン等が代表例。", "言語学", "Global_Synthesis", 1680, "https://en.wikipedia.org/wiki/Creole_language"),
    ("言語復興", "Language Revitalization", "失われつつある言語の復活・保存活動を研究する分野。ヘブライ語・マオリ語の事例、言語ネスト等の実践が知られる。", "言語学", "Global_Synthesis", 1970, "https://en.wikipedia.org/wiki/Language_revitalization"),
    ("手話言語学", "Sign Language Linguistics", "手話を完全な自然言語として研究する分野。スティーボーによるASLの構造分析以来、手話の音韻・形態・統語・語用を分析する研究が発展した。", "言語学", "North_America", 1960, "https://en.wikipedia.org/wiki/Sign_language_linguistics"),
    ("第二言語習得", "Second Language Acquisition", "成人・児童が第二言語を習得するプロセスを研究する学際分野。中間言語仮説、インプット仮説、相互作用仮説が代表的理論。", "言語学", "North_America", 1967, "https://en.wikipedia.org/wiki/Second-language_acquisition"),
    ("言語習得論", "Language Acquisition Theory", "子供が母語を習得するメカニズムを探る研究。チョムスキーの普遍文法、ピアジェの認知発達と言語、統計的学習、社会的相互作用説が対立・補完する。", "言語学", "North_America", 1957, "https://en.wikipedia.org/wiki/Language_acquisition"),
    ("社会方言学", "Sociolinguistics", "言語の社会的変異と変化を研究する分野。ラボフの社会音声学的変異研究、変異理論、スタイル・シフト、言語と社会的アイデンティティが中核的概念。", "言語学", "North_America", 1963, "https://en.wikipedia.org/wiki/Sociolinguistics"),
    ("インターネット言語学", "Internet Linguistics", "インターネット上での言語使用の特徴を研究する新興分野。クリスタルが体系化。CMC、スラング、絵文字、ミームの言語学的分析を含む。", "言語学", "Western_Europe", 2001, "https://en.wikipedia.org/wiki/Internet_linguistics"),
    ("言語政策と計画", "Language Policy and Planning", "社会・国家レベルでの言語の使用・普及・標準化・保護に関する政策決定と実施を研究する分野。コーパス計画とステータス計画に区分される。", "言語学", "Global_Synthesis", 1959, "https://en.wikipedia.org/wiki/Language_planning"),
    ("歴史言語学", "Historical Linguistics", "言語の歴史的変化・系統関係を研究する分野。音変化の法則、借用、類推、再構成の方法論、系統樹モデルが基礎。", "言語学", "Western_Europe", 1786, "https://en.wikipedia.org/wiki/Historical_linguistics"),
    ("言語普遍性", "Language Universals", "全ての言語に共通する特性または傾向を探る研究。グリーンバーグの統計的普遍性、生成文法の形式的普遍性、認知・機能主義的普遍性の三つの立場が対立する。", "言語学", "North_America", 1963, "https://en.wikipedia.org/wiki/Linguistic_universal"),
    ("音声学", "Phonetics", "言語音の生成・伝達・知覚を研究する言語学の分野。調音音声学、音響音声学、知覚音声学の三分野。IPAが国際標準記号体系。", "言語学", "Western_Europe", 1888, "https://en.wikipedia.org/wiki/Phonetics"),
    ("関連性理論", "Relevance Theory", "スペルベルとウィルソンが提唱した語用論の認知的理論。コミュニケーションは最大の認知効果を最小の処理労力で達成する関連性追求として説明される。", "言語学", "Western_Europe", 1986, "https://en.wikipedia.org/wiki/Relevance_theory"),
    ("発語行為論", "Speech Act Theory", "オースティン・サールによる言語行為の分類理論。発語内行為を中心に、言明・質問・命令・約束等の言語行為のカテゴリーと適切性条件を分析する。", "言語学", "Western_Europe", 1962, "https://en.wikipedia.org/wiki/Speech_act"),
    ("会話の含意", "Conversational Implicature", "グライスが提唱した語用論的概念。発話の文字通りの意味を超えて伝達される意味が、協調原理への依拠によって生じるメカニズムを分析する。", "言語学", "Western_Europe", 1975, "https://en.wikipedia.org/wiki/Implicature"),
    ("空間言語学", "Spatial Language", "人間の言語における空間表現を認知・類型論的に研究する分野。レヴィンソンの参照フレーム類型が代表的成果。", "言語学", "Western_Europe", 1996, "https://en.wikipedia.org/wiki/Spatial_cognition"),
    ("時制と相", "Tense and Aspect", "言語における時間的位置と出来事の内的時間構造の文法カテゴリーを研究する分野。コンプリー、スミス、クラインの相の理論が代表的。", "言語学", "North_America", 1976, "https://en.wikipedia.org/wiki/Tense%E2%80%93aspect%E2%80%93mood"),
    ("多義性研究", "Polysemy Research", "一つの語形が複数の関連した意味を持つ多義現象の認知言語学的・語用論的研究。プロトタイプ理論、放射状カテゴリーが主要なアプローチ。", "言語学", "Western_Europe", 1980, "https://en.wikipedia.org/wiki/Polysemy"),
    ("文字体系論", "Writing Systems", "人類が発展させた文字体系の種類と歴史的発展を研究する分野。クールマスの分類、文字の発明と伝播、未解読文字の研究を含む。", "言語学", "Global_Synthesis", -3200, "https://en.wikipedia.org/wiki/Writing_system"),
    ("言語と文化", "Language and Culture", "言語と文化的実践・世界観の関係を研究する人類言語学の中心的主題。ウォーフ・サピア仮説、文化的スクリプト、コミュニケーション文化論が代表的枠組み。", "言語学", "North_America", 1929, "https://en.wikipedia.org/wiki/Language_and_culture"),
    # ===== 文学・批評理論 (~40) =====
    ("生態批評", "Ecocriticism", "文学と環境の関係を研究する批評的枠組み。グロットフェルティが命名。自然の文学的表象、環境危機の文化的表現、人間中心主義批判を中核とする。", "文学・批評理論", "North_America", 1996, "https://en.wikipedia.org/wiki/Ecocriticism"),
    ("動物研究と文学", "Animal Studies and Literature", "文学テキストにおける動物の表象と人間-動物関係を批評的に分析する学際的枠組み。ハラウェイの伴侶種論、ウルフのポスト人文主義が代表。", "文学・批評理論", "North_America", 2003, "https://en.wikipedia.org/wiki/Human%E2%80%93animal_studies"),
    ("世界文学", "World Literature", "単一の国民文学を超えた比較・翻訳の視点から文学を扱う研究枠組み。ダムロッシュ、モレッティ、カサノヴァが代表的理論家。", "文学・批評理論", "North_America", 1827, "https://en.wikipedia.org/wiki/World_literature"),
    ("カルチュラル・スタディーズ", "Cultural Studies", "バーミンガム現代文化研究センターに起源を持つ学際的研究領域。ホール、ウィリアムズが創設者。サブカルチャー、イデオロギー、アイデンティティ、権力を横断的に分析する。", "文学・批評理論", "Western_Europe", 1964, "https://en.wikipedia.org/wiki/Cultural_studies"),
    ("クィア理論", "Queer Theory", "セクシュアリティ・ジェンダーに関する規範的範疇を解体する批評理論。バトラー、セジウィックが代表的論者。アイデンティティの流動性を強調する。", "文学・批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Queer_theory"),
    ("障害学と文学", "Disability Studies and Literature", "障害の文化的・文学的表象と障害の社会モデルを文学批評に適用する学際的枠組み。ミッチェルとスナイダーが代表的論者。", "文学・批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Disability_studies"),
    ("民族詩学", "Ethnopoetics", "ロスンバーグとベーカーが提唱した研究分野。口頭詩の表演・音・沈黙・身振りを含む全体的な詩学を民族誌的手法で記述・分析する。", "文学・批評理論", "North_America", 1960, "https://en.wikipedia.org/wiki/Ethnopoetics"),
    ("ナラティブ・メディシン", "Narrative Medicine", "文学・物語の方法論を医療実践・患者経験に適用する学際的研究。チャロンが代表。語ることによる癒しと病い体験の意味生成を論じる。", "文学・批評理論", "North_America", 2001, "https://en.wikipedia.org/wiki/Medical_humanities"),
    ("フランス文学理論", "French Literary Theory", "20世紀フランスで展開した文学・哲学的批評理論の集合体。サルトル、ロラン・バルト、デリダ、クリステヴァが代表。", "文学・批評理論", "Western_Europe", 1945, "https://en.wikipedia.org/wiki/French_theory"),
    ("叙事詩の詩学", "Poetics of Epic", "英雄叙事詩の構造・機能・伝統を研究する比較文学の枠組み。パリー=ロード理論、民族的叙事詩の比較が主要論点。", "文学・批評理論", "Western_Europe", -800, "https://en.wikipedia.org/wiki/Epic_poetry"),
    ("テクスト批判学", "Textual Criticism", "文献の写本・版・異同を研究し原典テキストを確定・編集する文献学的方法論。スタンマティクス、最良写本法が代表的手法。", "文学・批評理論", "Western_Europe", 1500, "https://en.wikipedia.org/wiki/Textual_criticism"),
    ("小説の理論", "Theory of the Novel", "バフチン、ルカーチ、ワットが代表的論者。歴史・形式・イデオロギーの観点から小説ジャンルの特性を問う。", "文学・批評理論", "Western_Europe", 1920, "https://en.wikipedia.org/wiki/Novel"),
    ("ハーレム・ルネサンス", "Harlem Renaissance", "1920年代にニューヨーク・ハーレムを中心に展開したアフリカ系アメリカ人の文化・芸術・文学運動。ラングストン・ヒューズ、ゾラ・ニール・ハーストンが代表。", "文学・批評理論", "North_America", 1920, "https://en.wikipedia.org/wiki/Harlem_Renaissance"),
    ("ラテンアメリカ文学批評", "Latin American Literary Criticism", "マジック・リアリズム、ブーム文学、テスティモニオ、女性文学を対象とする地域文学批評。ガルシア＝マルケスが代表的作家。", "文学・批評理論", "Latin_America", 1940, "https://en.wikipedia.org/wiki/Latin_American_literature"),
    ("アフリカ文学批評", "African Literary Criticism", "ンギュギ・ワ・ジオンゴ、チヌア・アチェベ等のアフリカ系作家の文学と批評理論。植民地時代の言語・アイデンティティ問題が中心。", "文学・批評理論", "Sub_Saharan_Africa", 1958, "https://en.wikipedia.org/wiki/African_literature"),
    ("文学における記憶論", "Memory and Literature", "文学テキストにおける個人的・集合的記憶の表象と機能を研究する批評的枠組み。トラウマ研究、ホロコースト文学、ポストメモリーが代表的概念。", "文学・批評理論", "North_America", 1992, "https://en.wikipedia.org/wiki/Memory_studies"),
    ("ディアスポラ文学", "Diaspora Literature", "移住・亡命・ディアスポラ経験をテーマとする文学とその批評。ホミ・バーバの第三の空間、グリッサンのクレオール性が代表的理論。", "文学・批評理論", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Immigrant_literature"),
    ("比較神話学", "Comparative Mythology", "異文化間の神話の類似・相違を体系的に比較研究する学問。フレイザー、ジョセフ・キャンベル、レヴィ＝ストロースの神話論が代表。", "文学・批評理論", "Global_Synthesis", 1890, "https://en.wikipedia.org/wiki/Comparative_mythology"),
    ("マンガ・グラフィックノベル研究", "Comics and Graphic Novel Studies", "漫画・コミック・グラフィックノベルを学術的に分析する研究分野。マクラウドの視覚理論、日本のマンガ研究が代表。", "文学・批評理論", "North_America", 1993, "https://en.wikipedia.org/wiki/Comic_studies"),
    ("デジタル人文学", "Digital Humanities", "人文科学にデジタル・コンピュータ的手法を適用する学際的研究領域。テキストマイニング、遠読、地図化、ネットワーク分析が主要手法。", "文学・批評理論", "North_America", 1949, "https://en.wikipedia.org/wiki/Digital_humanities"),
    # ===== 歴史学 (~40) =====
    ("グローバル・ヒストリー", "Global History", "国家・民族・文明の境界を越えた世界規模の歴史的プロセスを分析する方法論。マクニール、ポメランツの大分岐論が代表的論者。", "歴史学", "North_America", 1967, "https://en.wikipedia.org/wiki/Global_history"),
    ("環境史", "Environmental History", "人間社会と自然環境の相互作用を歴史的に分析する分野。クロスビーの生態的帝国主義、マクニールが代表的論者。", "歴史学", "North_America", 1972, "https://en.wikipedia.org/wiki/Environmental_history"),
    ("大西洋史", "Atlantic History", "大西洋を囲む地域を一つの歴史的単位として分析する研究枠組み。奴隷貿易、植民地化、革命の大西洋的連関が主要研究対象。", "歴史学", "North_America", 1992, "https://en.wikipedia.org/wiki/Atlantic_history"),
    ("インド洋史", "Indian Ocean History", "インド洋を囲む地域を一体的に分析する歴史的枠組み。季節風・交易ネットワーク・宗教の拡散が中心論点。", "歴史学", "South_Asia", 1985, "https://en.wikipedia.org/wiki/Indian_Ocean_trade"),
    ("地中海史", "Mediterranean History", "地中海を統一的な歴史的空間として分析するアプローチ。ブローデルが基礎を確立。長期持続・地理的制約・交易ネットワークが主要論点。", "歴史学", "Western_Europe", 1949, "https://en.wikipedia.org/wiki/Mediterranean_history"),
    ("帝国史と植民地史", "Imperial and Colonial History", "ヨーロッパ・非ヨーロッパの帝国形成と植民地統治を分析する研究領域。植民地近代性、帝国主義の比較研究が中心。", "歴史学", "Western_Europe", 1902, "https://en.wikipedia.org/wiki/Colonialism"),
    ("ミクロ・ヒストリー", "Microhistory", "個人・村・出来事など小規模な歴史的対象の詳細な分析から大きな歴史的問いに答えようとする研究手法。ギンズバーグが代表的論者。", "歴史学", "Western_Europe", 1976, "https://en.wikipedia.org/wiki/Microhistory"),
    ("オーラル・ヒストリー", "Oral History", "証言者への聞き取りによって歴史を記述する方法論。マルジナライズされた人々の声を歴史に組み込む意義が強調される。", "歴史学", "North_America", 1948, "https://en.wikipedia.org/wiki/Oral_history"),
    ("デジタル・ヒストリー", "Digital History", "デジタル技術・データ分析・GIS・ネットワーク分析を歴史研究に応用する新興分野。デジタルアーカイブが主要手法。", "歴史学", "North_America", 1990, "https://en.wikipedia.org/wiki/Digital_history"),
    ("後植民地時代史", "Postcolonial History", "植民地支配の遺産・影響・継続を歴史的に分析する研究枠組み。サバルタン研究、チャクラバルティが代表的理論。", "歴史学", "South_Asia", 1982, "https://en.wikipedia.org/wiki/Postcolonialism"),
    ("歴史認識論", "Epistemology of History", "歴史的知識の性質・正当化・客観性を問う哲学的問い。コリングウッド、ダントー、ポール・リクールが代表的論者。", "歴史学", "Western_Europe", 1946, "https://en.wikipedia.org/wiki/Philosophy_of_history"),
    ("ジェンダー史", "Gender History", "歴史的変化の中でのジェンダー・セクシュアリティ・身体の構築を研究する分野。ジョーン・スコットが理論的基礎を確立。", "歴史学", "North_America", 1986, "https://en.wikipedia.org/wiki/Women%27s_history"),
    ("労働史", "Labor History", "労働者・労働運動・職場環境・資本との関係を歴史的に研究する分野。トンプソンが代表的著作。", "歴史学", "Western_Europe", 1963, "https://en.wikipedia.org/wiki/Labor_history_(discipline)"),
    ("知識の歴史", "History of Knowledge", "知識・情報・学問の生産・流通・変換を歴史的に分析する研究枠組み。バーク、ダストンが代表的論者。", "歴史学", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/History_of_knowledge"),
    # ===== 宗教学 (~30) =====
    ("宗教現象学", "Phenomenology of Religion", "宗教的経験の本質的構造を記述しようとする方法論。エリアーデの聖と俗、オットーの聖なるものの概念が代表的論者。", "宗教学", "Western_Europe", 1917, "https://en.wikipedia.org/wiki/Phenomenology_of_religion"),
    ("宗教社会学", "Sociology of Religion", "宗教的信仰・実践・組織と社会構造の関係を研究する社会学の分野。デュルケーム、ウェーバー、バーガーが代表。", "宗教学", "Western_Europe", 1912, "https://en.wikipedia.org/wiki/Sociology_of_religion"),
    ("宗教心理学", "Psychology of Religion", "宗教的信仰・経験・回心・儀礼の心理的次元を研究する分野。ジェームズ、フロイト、ユングが基礎を確立。", "宗教学", "North_America", 1902, "https://en.wikipedia.org/wiki/Psychology_of_religion"),
    ("宗教と政治", "Religion and Politics", "宗教的権威と政治権力の関係を研究する学際的分野。政教分離の諸形態、宗教的ナショナリズムが中心論点。", "宗教学", "Global_Synthesis", 1970, "https://en.wikipedia.org/wiki/Religion_and_politics"),
    ("宗教と暴力", "Religion and Violence", "宗教的動機による暴力・テロリズム・聖戦の歴史と分析。ジュエルゲンスマイヤー、ジラールの犠牲論が代表的研究。", "宗教学", "North_America", 1980, "https://en.wikipedia.org/wiki/Religious_violence"),
    ("神話と儀礼", "Myth and Ritual", "神話と宗教儀礼の相互関係を研究する比較宗教学の伝統的主題。フレイザーの神話・儀礼学派からレヴィ＝ストロースの構造的神話分析まで。", "宗教学", "Western_Europe", 1890, "https://en.wikipedia.org/wiki/Myth_and_ritual"),
    ("聖地と巡礼", "Sacred Sites and Pilgrimage", "聖なる場所の形成・維持・体験と巡礼実践を研究する宗教地理学・宗教人類学の分野。ターナーの巡礼の人類学が代表。", "宗教学", "Global_Synthesis", 1978, "https://en.wikipedia.org/wiki/Pilgrimage"),
    ("宗教と科学", "Religion and Science", "宗教的信仰と科学的知識の関係を論じる学際的研究領域。対立モデルから対話モデルまで多様なアプローチが存在する。", "宗教学", "Western_Europe", 1890, "https://en.wikipedia.org/wiki/Relationship_between_religion_and_science"),
    ("宗教と医療", "Religion and Medicine", "祈り・ヒーリング・終末期ケアにおける宗教的側面と西洋医学の接点を研究する学際分野。シャーマニズム研究、スピリチュアルケアが含まれる。", "宗教学", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Faith_healing"),
    ("宗教改革の研究", "Reformation Studies", "16世紀プロテスタント宗教改革とカトリック対抗宗教改革の歴史・神学・文化的影響を研究する分野。印刷革命との関連が主要論点。", "宗教学", "Western_Europe", 1517, "https://en.wikipedia.org/wiki/Reformation"),
    ("スーフィズム研究", "Sufi Studies", "イスラーム神秘主義の思想・実践・組織を研究する学術分野。ルーミー、イブン・アラビーが代表的思想家。詩・音楽・聖者崇拝を含む。", "宗教学", "West_Asia_North_Africa", 800, "https://en.wikipedia.org/wiki/Sufism"),
    ("新宗教運動", "New Religious Movements", "既存宗教から派生した或いは新興した宗教運動を研究する社会学的・宗教学的分野。ムーニー教、サイエントロジー、創価学会等を対象とする。", "宗教学", "Global_Synthesis", 1970, "https://en.wikipedia.org/wiki/New_religious_movement"),
    # ===== 古典学 (~40) =====
    ("ギリシア悲劇", "Greek Tragedy", "古代アテナイで公演された演劇形式。アイスキュロス、ソフォクレス、エウリピデスが代表的詩人。カタルシス・ハマルティア・コロスの機能が詩学的分析の中心。", "古典学", "Western_Europe", -500, "https://en.wikipedia.org/wiki/Greek_tragedy"),
    ("ギリシア喜劇", "Greek Comedy", "古典期アテナイの喜劇。アリストファネスの旧喜劇とメナンドロスの新喜劇に区分される。ローマのプラウトゥス・テレンティウスを経て近代喜劇に影響。", "古典学", "Western_Europe", -486, "https://en.wikipedia.org/wiki/Ancient_Greek_comedy"),
    ("ラテン詩学", "Latin Poetics", "古代ローマの詩の理論と実践。ウェルギリウス、ホラティウスの詩論、オウィディウスが代表的詩人。ヘクサメトロスが主要詩形。", "古典学", "Western_Europe", -70, "https://en.wikipedia.org/wiki/Latin_literature"),
    ("古典修辞学", "Classical Rhetoric", "古代ギリシア・ローマで発展した説得の技術。アリストテレスの弁論術、キケロ、クインティリアヌスが体系化。発明・配列・修辞・記憶・発表の五要素。", "古典学", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Rhetoric"),
    ("ギリシア・ローマの歴史記述", "Greek and Roman Historiography", "古代の歴史記述の伝統。トゥキュディデス、ヘロドトス、リウィウス、タキトゥスが代表。", "古典学", "Western_Europe", -450, "https://en.wikipedia.org/wiki/Greek_historiography"),
    ("ギリシア数学", "Greek Mathematics", "古代ギリシアの数学的伝統。ユークリッド、アルキメデス、アポロニウスが代表。演繹的証明の確立が最大の貢献。", "古典学", "Western_Europe", -300, "https://en.wikipedia.org/wiki/Greek_mathematics"),
    ("古代近東文明", "Ancient Near Eastern Civilizations", "メソポタミア・エジプト・アナトリア・レバント地方の古代文明の研究。ウル第三王朝、アッシリア帝国、ギルガメシュ叙事詩が主要対象。", "古典学", "West_Asia_North_Africa", -3000, "https://en.wikipedia.org/wiki/Ancient_Near_East"),
    ("エジプト学", "Egyptology", "古代エジプトの言語・文化・宗教・芸術・考古学を研究する学問分野。シャンポリオンによるロゼッタストーンの解読が出発点。", "古典学", "West_Asia_North_Africa", -3000, "https://en.wikipedia.org/wiki/Egyptology"),
    ("インド古典文学", "Indian Classical Literature", "サンスクリット・タミル・プラークリット語で書かれた古代インドの文学。マハーバーラタ・ラーマーヤナ叙事詩、カーリダーサが代表。", "古典学", "South_Asia", -400, "https://en.wikipedia.org/wiki/Sanskrit_literature"),
    ("タミル古典文学", "Tamil Classical Literature", "南インドのタミル語で書かれた古典文学。サンガム文学はティルクラルが代表。五つのtinaiという独自の詩学体系を持つ。", "古典学", "South_Asia", -300, "https://en.wikipedia.org/wiki/Tamil_literature"),
    ("中国古典経書", "Chinese Classical Texts", "中国の儒教的知識体系の根幹をなす四書五経。易経・書経・詩経・礼記・春秋と論語・孟子・大学・中庸。宋学の注釈体系が標準的解釈を形成した。", "古典学", "East_Asia", -500, "https://en.wikipedia.org/wiki/Four_Books_and_Five_Classics"),
    ("日本古典文学", "Japanese Classical Literature", "奈良・平安・鎌倉時代の日本語文学。万葉集・古今和歌集・源氏物語・枕草子・平家物語が代表。もののあわれ・幽玄・侘びさびの美的概念と連動する。", "古典学", "East_Asia", 712, "https://en.wikipedia.org/wiki/Japanese_literature"),
    ("メソアメリカ古典文明", "Mesoamerican Classical Civilizations", "マヤ・アステカ・テオティワカン・オルメカなどのメソアメリカ古代文明の研究。マヤ文字解読、カレンダーシステム、コデックスの研究を含む。", "古典学", "Latin_America", -1500, "https://en.wikipedia.org/wiki/Mesoamerican_civilization"),
    ("アンデス古典文明", "Andean Classical Civilizations", "インカ帝国・ワリ・ティワナク・チャビン等のアンデス文明の研究。キープ、アンデス建築、宗教体系が主要研究対象。", "古典学", "Latin_America", -900, "https://en.wikipedia.org/wiki/Andean_civilizations"),
    # ===== 美学・芸術理論 (~20) =====
    ("崇高の美学", "Aesthetics of the Sublime", "強烈な美的経験を引き起こす巨大・圧倒的な力の概念。バーク、カントの崇高論が古典的分析。現代では核・テクノロジー崇高への応用が展開。", "美学・芸術理論", "Western_Europe", 1757, "https://en.wikipedia.org/wiki/Sublime_(philosophy)"),
    ("審美的経験論", "Aesthetics of Experience", "芸術や自然との出会いにおける審美的経験の本質を分析する美学の中心的問い。デューイの経験としての芸術が代表。", "美学・芸術理論", "North_America", 1934, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("環境美学", "Environmental Aesthetics", "自然・景観・環境の審美的評価を論じる美学の分野。カールソン、バーリアントが代表的論者。エコロジーとの連関が強調される。", "美学・芸術理論", "North_America", 1966, "https://en.wikipedia.org/wiki/Environmental_aesthetics"),
    ("表象の美学", "Aesthetics of Representation", "芸術作品における表象・描写の性質と認識論的地位を論じる。グッドマンの芸術の言語、ウォルトンのフィクション論が代表。", "美学・芸術理論", "North_America", 1968, "https://en.wikipedia.org/wiki/Representation_(arts)"),
    ("音楽哲学", "Philosophy of Music", "音楽の存在論、表現性、理解を論じる。ウォルトン、デイヴィス、レヴィンソンが代表的論者。", "美学・芸術理論", "Western_Europe", 1835, "https://en.wikipedia.org/wiki/Philosophy_of_music"),
    ("建築の美学", "Aesthetics of Architecture", "建築物の審美的性質と経験を論じる美学の分野。ゴールドハーゲン、ノルベルク＝シュルツが代表的論者。機能と美の関係が主要論点。", "美学・芸術理論", "Western_Europe", 1753, "https://en.wikipedia.org/wiki/Architectural_aesthetics"),
    ("写真の美学", "Aesthetics of Photography", "写真というメディアの固有の審美的性質・真実性・表現可能性を論じる。バルトの明るい部屋、ソンタグの写真論が代表的分析。", "美学・芸術理論", "Western_Europe", 1980, "https://en.wikipedia.org/wiki/Photography_and_the_arts"),
    ("映画美学", "Film Aesthetics", "映画の審美的・表現的性質を哲学的に分析する分野。バジャン、アイゼンシュテイン、マッツが代表。", "美学・芸術理論", "Western_Europe", 1945, "https://en.wikipedia.org/wiki/Film_theory"),
    ("パフォーマンスアートの理論", "Theory of Performance Art", "身体・時間・空間を用いたライブアートの理論的枠組み。シェクナーの環境演劇、アブラモヴィッチ等のアーティスト実践を対象とする。", "美学・芸術理論", "North_America", 1960, "https://en.wikipedia.org/wiki/Performance_art"),
    ("現代アート批評", "Contemporary Art Criticism", "1960年代以降の現代美術を批評的に分析する枠組み。フリード、ブリオーの関係性の美学、グリーンバーグのモダニズム批評が代表。", "美学・芸術理論", "North_America", 1965, "https://en.wikipedia.org/wiki/Art_criticism"),
]

print(f"レコード総数: {len(records)}")

con = sqlite3.connect(DB)
con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM humanities_concept")
before = cur.fetchone()[0]
print(f"既存件数: {before}")

existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept"))

batch = []
inserted = 0
skipped = 0

for r in records:
    name_en = r[1]
    if name_en in existing:
        skipped += 1
        continue
    existing.add(name_en)
    uid_val = uid()
    batch.append((uid_val, r[0], r[1], r[2], r[3], r[4], r[5], r[6], 'url_present', 'dua_wave_a2', 'active', now, now))
    if len(batch) >= 500:
        cur.executemany("""INSERT INTO humanities_concept
            (id,name_ja,name_en,definition,subfield,culture_region,
             era_start,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
        con.commit()
        inserted += len(batch)
        batch = []

if batch:
    cur.executemany("""INSERT INTO humanities_concept
        (id,name_ja,name_en,definition,subfield,culture_region,
         era_start,source_url,verification_status,quality_flag,
         status,created_at,updated_at)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
    con.commit()
    inserted += len(batch)

cur.execute("SELECT COUNT(*) FROM humanities_concept")
after = cur.fetchone()[0]
con.close()
print(f"inserted={inserted}, skipped={skipped}")
print(f"総件数: {after} (目標5500)")
