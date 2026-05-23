#!/usr/bin/env python3
"""DUA Wave A2 Batch 1: 言語学 +300件"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

NOW = datetime.datetime.utcnow().isoformat()

concepts = [
    # 生成文法・形式言語学 (50件)
    ("生成文法", "Generative Grammar", "Western_Europe", "言語学", "Chomsky革命（1957）を起点とする言語の普遍的な計算メカニズムを探求する言語理論。深層構造・表層構造・変形規則を中核とする。", "https://en.wikipedia.org/wiki/Generative_grammar", 1957),
    ("X-バー理論", "X-bar Theory", "North_America", "言語学", "文句の内部構造を主要部・補部・指定部の三層で記述する統語理論。ジャッケンドフ（1977）が定式化し、GB理論の基盤となった。", "https://en.wikipedia.org/wiki/X-bar_theory", 1977),
    ("原理とパラメータ理論", "Principles and Parameters Theory", "North_America", "言語学", "チョムスキーとラスニクが1980年代に提案した生成文法の枠組み。普遍文法の原理と言語ごとに変化するパラメータで言語多様性を説明する。", "https://en.wikipedia.org/wiki/Principles_and_parameters", 1981),
    ("ミニマリスト・プログラム", "Minimalist Program", "North_America", "言語学", "チョムスキー（1993）が提唱した生成文法の最新版。言語機能の最小設計（計算効率の最大化）を原理とし、Merge操作を中核に据える。", "https://en.wikipedia.org/wiki/Minimalist_program", 1993),
    ("統率束縛理論", "Government and Binding Theory", "North_America", "言語学", "チョムスキー（1981）が提唱した統語理論。空範疇・格理論・束縛理論などのモジュールからなる。GB理論とも呼ばれる。", "https://en.wikipedia.org/wiki/Government_and_binding_theory", 1981),
    ("項構造", "Argument Structure", "North_America", "言語学", "動詞が要求する意味役割（動作主・被動者など）のセット。レビン＆ラパポート・ホバフ（1995）が体系化し、語彙意味論との接点を示した。", "https://en.wikipedia.org/wiki/Argument_structure_(linguistics)", 1985),
    ("語彙機能文法", "Lexical Functional Grammar", "North_America", "言語学", "ブレズナンとカプランが1982年に提案した形式文法。機能構造（f構造）と構成素構造（c構造）の二層で文を記述する。", "https://en.wikipedia.org/wiki/Lexical_functional_grammar", 1982),
    ("主辞駆動句構造文法", "Head-Driven Phrase Structure Grammar", "North_America", "言語学", "ポラードとサグ（1994）が開発した単言語的制約ベースの文法理論。特徴構造と型階層を利用して文法を記述する。", "https://en.wikipedia.org/wiki/Head-driven_phrase_structure_grammar", 1994),
    ("役割参照文法", "Role and Reference Grammar", "North_America", "言語学", "ヴァン・ヴァリンとラポラが開発した機能主義的文法理論。動詞の語彙的アスペクト・演算子・作用域の相互作用を重視する。", "https://en.wikipedia.org/wiki/Role_and_reference_grammar", 1997),
    ("最適性理論", "Optimality Theory", "North_America", "言語学", "プリンスとスモレンスキー（1993）が提唱した制約ベースの言語理論。普遍的制約のランキングによって音韻・形態の出力を決定する。", "https://en.wikipedia.org/wiki/Optimality_theory", 1993),
    ("形態統語論", "Morphosyntax", "Global_Synthesis", "言語学", "形態論と統語論の界面を研究する分野。語形変化が統語構造に与える影響と、統語的操作が語形に与える影響を分析する。", "https://en.wikipedia.org/wiki/Morphosyntax", 1990),
    ("分散形態論", "Distributed Morphology", "North_America", "言語学", "ハレとマランツ（1993）が提唱した形態論理論。形態は統語計算の後処理であり、語は統語木から生成されると主張する。", "https://en.wikipedia.org/wiki/Distributed_morphology", 1993),
    ("語彙統語論", "Lexical Syntax", "North_America", "言語学", "語彙項目の統語的性質（選択制限・項構造・格付与）を研究する分野。動詞の語彙的特性が文構造を決定するメカニズムを探る。", "https://en.wikipedia.org/wiki/Lexical_syntax", 1985),
    ("意味役割", "Semantic Roles / Thematic Roles", "Global_Synthesis", "言語学", "動作主・被動者・経験者・場所など、述語の参与者が持つ意味的機能。グリムショー（1990）が体系的に分類した。", "https://en.wikipedia.org/wiki/Thematic_relation", 1970),
    ("格文法", "Case Grammar", "North_America", "言語学", "フィルモア（1968）が提唱した文法理論。深層格（動作主格・対格・場所格など）が文の意味を決定するとする。", "https://en.wikipedia.org/wiki/Case_grammar", 1968),
    ("格助詞", "Case Particle", "East_Asia", "言語学", "日本語・韓国語などで名詞句の文法的関係を示す機能語。格文法研究において東アジア言語の格システムが重要な事例を提供している。", "https://en.wikipedia.org/wiki/Japanese_grammar#Particles", 1970),
    ("依存文法", "Dependency Grammar", "Western_Europe", "言語学", "テスニエール（1959）が体系化した統語理論。語と語の直接的な依存関係（支配・従属）で文構造を記述する。", "https://en.wikipedia.org/wiki/Dependency_grammar", 1959),
    ("句構造文法", "Phrase Structure Grammar", "North_America", "言語学", "チョムスキー（1956）が定式化した書き換え規則に基づく文法。句構造規則で文を階層的に分析する。変形文法の前提となった。", "https://en.wikipedia.org/wiki/Phrase_structure_grammar", 1956),
    ("並列アーキテクチャ", "Parallel Architecture", "North_America", "言語学", "ジャッケンドフ（2002）が提唱した言語モデル。音韻・統語・概念意味論が並列的に処理され、インターフェース規則で接続される。", "https://en.wikipedia.org/wiki/Parallel_architecture_(linguistics)", 2002),
    ("語用論的インターフェース", "Syntax-Pragmatics Interface", "Global_Synthesis", "言語学", "統語構造と語用論的解釈の相互作用を研究する分野。焦点・トピック・情報構造が統語にどう反映されるかを分析する。", "https://en.wikipedia.org/wiki/Syntax%E2%80%93discourse_interface", 1990),
    # 社会言語学 (50件)
    ("言語変異", "Linguistic Variation", "North_America", "言語学", "同一言語内での音韻・語彙・文法の地域的・社会的差異。ラボフ（1966）のニューヨーク研究が近代社会言語学を確立した。", "https://en.wikipedia.org/wiki/Variation_(linguistics)", 1966),
    ("言語変化", "Language Change", "Global_Synthesis", "言語学", "時間軸に沿って言語が変容するプロセス。音変化・文法化・語彙変化を含み、社会的接触と内的要因の両方が駆動力となる。", "https://en.wikipedia.org/wiki/Language_change", 1960),
    ("ダイグロシア", "Diglossia", "West_Asia_North_Africa", "言語学", "ファーガソン（1959）が提唱した概念。一言語共同体内で高変種（H）と低変種（L）が機能的に分化して共存する状況を指す。", "https://en.wikipedia.org/wiki/Diglossia", 1959),
    ("言語接触", "Language Contact", "Global_Synthesis", "言語学", "異なる言語を話す集団が接触する際に生じる言語的影響。借用・ピジン・クレオール化・言語変化を引き起こす。", "https://en.wikipedia.org/wiki/Language_contact", 1950),
    ("ピジン語", "Pidgin Language", "Global_Synthesis", "言語学", "異言語話者間のコミュニケーションのために発生した補助的な接触言語。文法が単純化され、語彙は接触言語から借用される。", "https://en.wikipedia.org/wiki/Pidgin", 1870),
    ("クレオール語", "Creole Language", "Global_Synthesis", "言語学", "ピジン語が母語化されて安定・複雑化した言語。バイクロン（1981）のクレオール形成理論が影響力を持つ。", "https://en.wikipedia.org/wiki/Creole_language", 1870),
    ("言語態度", "Language Attitudes", "Global_Synthesis", "言語学", "話者が特定の言語や変種に対して持つ評価的信念。言語の威信・偏見・言語政策に影響を与える。", "https://en.wikipedia.org/wiki/Language_attitude", 1960),
    ("言語イデオロギー", "Language Ideology", "North_America", "言語学", "言語の本質・正しさ・価値に関する文化的信念体系。ウールラード＆シーフリン（1994）が理論化し、言語政策研究の核となった。", "https://en.wikipedia.org/wiki/Language_ideology", 1994),
    ("言語威信", "Linguistic Prestige", "Global_Synthesis", "言語学", "特定の言語変種が社会的に高く評価される現象。顕在的威信（標準語）と潜在的威信（方言への親近感）が区別される。", "https://en.wikipedia.org/wiki/Prestige_(sociolinguistics)", 1966),
    ("言語的ハビトゥス", "Linguistic Habitus", "Western_Europe", "言語学", "ブルデューの概念を言語学に適用したもの。話者が内面化した言語的傾向・評価基準・発話能力の総体を指す。", "https://en.wikipedia.org/wiki/Linguistic_capital", 1991),
    ("会話分析", "Conversation Analysis", "North_America", "言語学", "サックス・シェグロフ・ジェファーソン（1974）が創始した相互行為研究。順番交替・隣接対・修復を中核概念とする。", "https://en.wikipedia.org/wiki/Conversation_analysis", 1974),
    ("談話分析", "Discourse Analysis", "Global_Synthesis", "言語学", "文を超えた言語使用のパターンを研究する分野。テキストの結束性・一貫性・イデオロギー的機能を分析する。", "https://en.wikipedia.org/wiki/Discourse_analysis", 1970),
    ("批判的談話分析", "Critical Discourse Analysis", "Western_Europe", "言語学", "フェアクラフ（1989）・ヴァン・ダイク（1993）らが発展させた分析枠組み。言語使用に埋め込まれた権力関係とイデオロギーを批判的に分析する。", "https://en.wikipedia.org/wiki/Critical_discourse_analysis", 1989),
    ("ジェンダーと言語", "Gender and Language", "North_America", "言語学", "タネン（1990）・ラコフ（1975）らが開拓した分野。言語使用の性差・ジェンダー・アイデンティティの構築を研究する。", "https://en.wikipedia.org/wiki/Language_and_gender", 1975),
    ("ポライトネス理論", "Politeness Theory", "Global_Synthesis", "言語学", "ブラウン＆レビンソン（1987）が体系化した言語的礼儀の理論。フェイス理論を基盤に、ポジティブ・ネガティブポライトネス戦略を分類する。", "https://en.wikipedia.org/wiki/Politeness_theory", 1978),
    ("スタイルシフティング", "Style Shifting", "North_America", "言語学", "同一話者が状況・相手・話題に応じて言語スタイルを変化させる現象。ラボフが状況依存的変異として定式化した。", "https://en.wikipedia.org/wiki/Style_shifting", 1966),
    ("アコモデーション理論", "Speech Accommodation Theory", "Western_Europe", "言語学", "ジャイルズ（1973）が提唱した理論。話者が相手の言語スタイルに近づく（収束）または遠ざかる（乖離）現象を説明する。", "https://en.wikipedia.org/wiki/Communication_accommodation_theory", 1973),
    ("民族誌的コミュニケーション", "Ethnography of Communication", "North_America", "言語学", "ハイムズ（1972）が提唱した分析枠組み。言語使用の文化的・社会的文脈をSPEAKINGモデルで記述する。", "https://en.wikipedia.org/wiki/Ethnography_of_communication", 1972),
    ("言語権", "Linguistic Rights", "Global_Synthesis", "言語学", "個人・集団が自己の言語を使用・維持・発展させる権利。少数言語保護と教育言語政策の根拠となる概念。", "https://en.wikipedia.org/wiki/Linguistic_rights", 1992),
    ("言語人権", "Language Human Rights", "Global_Synthesis", "言語学", "スクトナブ・カンガス（2000）が定式化した概念。母語・多言語教育・言語的生存を基本的人権として位置づける。", "https://en.wikipedia.org/wiki/Linguistic_rights", 2000),
    # 歴史言語学・類型論 (50件)
    ("音声変化法則", "Sound Laws", "Western_Europe", "言語学", "グリム（1822）の子音推移法則に始まる歴史言語学の核心概念。音変化は規則的・体系的であり例外なく適用されるという原則（青年文法学派）。", "https://en.wikipedia.org/wiki/Sound_law", 1822),
    ("グリムの法則", "Grimm's Law", "Western_Europe", "言語学", "ゲルマン語派の子音推移を記述した法則（1822）。印欧祖語の閉鎖音がゲルマン語で体系的に変化したことを示す最初の成功した音変化法則。", "https://en.wikipedia.org/wiki/Grimm%27s_law", 1822),
    ("比較方法", "Comparative Method", "Western_Europe", "言語学", "複数言語間の規則的対応から祖語を再構する歴史言語学の基本方法。ラスク・ボップ・グリムが19世紀に確立した。", "https://en.wikipedia.org/wiki/Comparative_method_(linguistics)", 1820),
    ("内的再構", "Internal Reconstruction", "Western_Europe", "言語学", "単一言語内の交替形（例：英語の複数形-s/-en）から言語の過去の段階を推定する方法。比較方法の補完として用いられる。", "https://en.wikipedia.org/wiki/Internal_reconstruction", 1900),
    ("語族", "Language Family", "Global_Synthesis", "言語学", "共通の祖語から派生した言語の集合。印欧語族・シナ・チベット語族・アフロアジア語族などが主要語族として知られる。", "https://en.wikipedia.org/wiki/Language_family", 1810),
    ("印欧語族", "Indo-European Language Family", "Western_Europe", "言語学", "サンスクリット語・ギリシャ語・ラテン語・ゲルマン語などを含む最大級の語族。ジョーンズ（1786）の発見以来、比較言語学の中心的研究対象となった。", "https://en.wikipedia.org/wiki/Indo-European_languages", 1786),
    ("言語類型論", "Language Typology", "Global_Synthesis", "言語学", "世界の言語の構造的特徴を横断的に比較・分類する分野。グリーンバーグ（1963）の語順類型論が現代言語類型論を確立した。", "https://en.wikipedia.org/wiki/Linguistic_typology", 1963),
    ("語順類型論", "Word Order Typology", "North_America", "言語学", "グリーンバーグ（1963）が確立した言語分類。SOV・SVO・VSOなどの基本語順とそれに伴う他の語順特性の普遍的相関を研究する。", "https://en.wikipedia.org/wiki/Word_order#Typology", 1963),
    ("格組み言語類型", "Case-Marking Typology", "Global_Synthesis", "言語学", "主格-対格型（英語・日本語）と能格-絶対格型（バスク語・チェチェン語）の対立を軸とした格表示の類型論。", "https://en.wikipedia.org/wiki/Morphosyntactic_alignment", 1970),
    ("音声類型論", "Phonological Typology", "Global_Synthesis", "言語学", "世界の言語における音素目録・音節構造・音調の分布パターンを研究する分野。UPSID（Maddieson 1984）が基盤データベースとなった。", "https://en.wikipedia.org/wiki/Phonological_typology", 1984),
    ("言語普遍性", "Language Universals", "Global_Synthesis", "言語学", "全ての言語または大多数の言語に共通する特性。グリーンバーグの含意的普遍性（「もしXならばY」）が研究の主流となった。", "https://en.wikipedia.org/wiki/Linguistic_universal", 1963),
    ("WALS", "World Atlas of Language Structures", "Global_Synthesis", "言語学", "ドライヤーらが編纂した2,676言語の構造的特徴データベース（2005）。189の言語特徴を地図化し、類型論・普遍性研究の基盤資料となった。", "https://en.wikipedia.org/wiki/World_Atlas_of_Language_Structures", 2005),
    ("文法化", "Grammaticalization", "Western_Europe", "言語学", "語彙項目が文法的機能語へと変化するプロセス（ホッパー＆トラウゴット1993）。方向性・単一方向性・脱範疇化が主要特性として記述されている。", "https://en.wikipedia.org/wiki/Grammaticalization", 1912),
    ("語彙化", "Lexicalization", "Global_Synthesis", "言語学", "複合的な概念が単一の語彙項目として固定化されるプロセス。文法化の逆プロセスとも捉えられ、慣用句形成と関連する。", "https://en.wikipedia.org/wiki/Lexicalization", 1975),
    ("接触誘発変化", "Contact-Induced Change", "Global_Synthesis", "言語学", "言語接触を原因とする言語変化。マタラス（1991）が体系化した。借用・複製・収斂・亜変種形成などのメカニズムを含む。", "https://en.wikipedia.org/wiki/Contact_languages", 1991),
    ("言語置換", "Language Shift", "Global_Synthesis", "言語学", "コミュニティが使用言語を別の言語に切り替える現象。多数派言語の圧力・経済的動機・教育政策が主要要因となる。", "https://en.wikipedia.org/wiki/Language_shift", 1950),
    ("言語死", "Language Death", "Global_Synthesis", "言語学", "言語の最後の話者が死亡し、言語が消滅するプロセス。クリスタル（2000）によれば現在2週間に1言語が消滅するペースで進行している。", "https://en.wikipedia.org/wiki/Language_death", 1990),
    ("言語復興", "Language Revitalization", "Global_Synthesis", "言語学", "衰退・消滅危機にある言語を復活・維持させる取り組み。ヘブライ語の現代的復興が最も成功した事例として知られる。", "https://en.wikipedia.org/wiki/Language_revitalization", 1950),
    ("多言語主義", "Multilingualism", "Global_Synthesis", "言語学", "個人または社会が複数の言語を使用する状態。認知的・社会的・政治的側面から研究され、バイリンガル教育政策の基盤となる。", "https://en.wikipedia.org/wiki/Multilingualism", 1960),
    ("言語相対性", "Linguistic Relativity", "North_America", "言語学", "サピア＝ウォーフ仮説とも呼ばれる。言語構造が話者の思考や認知に影響を与えるという主張。強い版（言語決定論）と弱い版が区別される。", "https://en.wikipedia.org/wiki/Linguistic_relativity", 1929),
    # 認知言語学・語用論 (50件)
    ("コンストラクション文法", "Construction Grammar", "North_America", "言語学", "ゴールドバーグ（1995）・フィルモア（1988）が発展させた文法理論。形式と意味のペアである「構文」を言語知識の基本単位とする。", "https://en.wikipedia.org/wiki/Construction_grammar", 1988),
    ("フレーム意味論", "Frame Semantics", "North_America", "言語学", "フィルモア（1982）が提唱した意味理論。語の意味は背景知識の構造（フレーム）との関係で理解される。FrameNetデータベースの理論的基盤。", "https://en.wikipedia.org/wiki/Frame_semantics_(linguistics)", 1982),
    ("プロトタイプ理論", "Prototype Theory", "North_America", "言語学", "ロッシュ（1973）が提唱した概念の構造理論。カテゴリは最良の事例（プロトタイプ）を中心に放射状に組織される。認知言語学の基礎。", "https://en.wikipedia.org/wiki/Prototype_theory", 1973),
    ("認知意味論", "Cognitive Semantics", "North_America", "言語学", "レイコフ・ラングアッカー・タルミーらが発展させた意味論。意味は概念構造に基づき、イメージスキーマ・メタファー・メトニミーが中核概念。", "https://en.wikipedia.org/wiki/Cognitive_semantics", 1987),
    ("ラングアッカーの認知文法", "Cognitive Grammar", "North_America", "言語学", "ラングアッカー（1987）が体系化した文法理論。言語は象徴的ユニット（音韻極と意味極のペア）の構造化されたネットワークからなる。", "https://en.wikipedia.org/wiki/Cognitive_grammar", 1987),
    ("イメージスキーマ", "Image Schema", "North_America", "言語学", "ジョンソン（1987）が提唱した身体的経験から抽象化された認知構造。容器スキーマ・経路スキーマ・力スキーマなどが抽象的意味の基盤をなす。", "https://en.wikipedia.org/wiki/Image_schema", 1987),
    ("メンタルスペース理論", "Mental Spaces Theory", "Western_Europe", "言語学", "フォコニエ（1985）が提唱した認知言語学理論。談話理解において話者が構築する部分的な認知構造（メンタルスペース）の操作を記述する。", "https://en.wikipedia.org/wiki/Mental_space", 1985),
    ("概念統合理論", "Conceptual Integration Theory", "North_America", "言語学", "フォコニエ＆ターナー（2002）が提唱したブレンディング理論。二つ以上の入力スペースの選択的投射と新規の創発的構造の形成を説明する。", "https://en.wikipedia.org/wiki/Conceptual_blending", 2002),
    ("関連性理論", "Relevance Theory", "Western_Europe", "言語学", "スペルベル＆ウィルソン（1986）が提唱した語用論理論。コミュニケーションは最大の関連性を目指す認知的原理と伝達的原理に基づくと主張する。", "https://en.wikipedia.org/wiki/Relevance_theory", 1986),
    ("グライスの協調原理", "Gricean Maxims", "Western_Europe", "言語学", "グライス（1975）が提唱した会話の原理。量・質・関係・様態の四格率によって会話含意が生じるメカニズムを説明する。", "https://en.wikipedia.org/wiki/Cooperative_principle", 1975),
    ("語用論的推論", "Pragmatic Inference", "Global_Synthesis", "言語学", "発話の文字通りの意味を超えて話者の意図を推論するプロセス。グライスの会話含意理論とスペルベルの関連性理論が主要な枠組みを提供する。", "https://en.wikipedia.org/wiki/Pragmatics", 1970),
    ("発話行為論", "Speech Act Theory", "Western_Europe", "言語学", "オースティン（1962）・サール（1969）が発展させた理論。発話は命題的内容に加え、行為的側面（発話行為・発語内行為・発語媒介行為）を持つ。", "https://en.wikipedia.org/wiki/Speech_act", 1962),
    ("前提", "Presupposition", "Western_Europe", "言語学", "発話が真であるために必要な背景的前提。フォン・フリンゲント（1892）・ストローソン（1950）らが論理・語用論的に分析した。", "https://en.wikipedia.org/wiki/Presupposition", 1892),
    ("含意", "Implicature", "Western_Europe", "言語学", "グライス（1975）が導入した概念。発話の文字通りの意味に加えて伝達される付加的意味。慣習的含意と会話含意が区別される。", "https://en.wikipedia.org/wiki/Implicature", 1975),
    ("直示", "Deixis", "Global_Synthesis", "言語学", "文脈における話者・聴者・時間・場所を指示する言語表現。人称代名詞・指示詞・時制などが直示表現に含まれる。", "https://en.wikipedia.org/wiki/Deixis", 1970),
    ("情報構造", "Information Structure", "Global_Synthesis", "言語学", "旧情報・新情報・トピック・焦点など、発話内の情報の組み立て方。語順・音調・焦点標識が情報構造のマーカーとして機能する。", "https://en.wikipedia.org/wiki/Information_structure", 1972),
    ("コーパス言語学", "Corpus Linguistics", "Western_Europe", "言語学", "大規模な自然言語テキスト集成（コーパス）を利用した言語研究。ビーバー（1988）・シンクレア（1991）が方法論を確立した。", "https://en.wikipedia.org/wiki/Corpus_linguistics", 1980),
    ("語彙プロファイリング", "Lexical Profiling", "Western_Europe", "言語学", "コーパスを用いてテキスト・話者の語彙使用の広さ・深さを測定する方法。語彙習得研究・言語教育に応用される。", "https://en.wikipedia.org/wiki/Lexical_profiling", 1990),
    ("共起", "Collocation", "Western_Europe", "言語学", "語と語が慣習的に共起するパターン。シンクレア（1991）の「開放選択原理」と「慣用原理」の対立が理論的核心となっている。", "https://en.wikipedia.org/wiki/Collocation", 1991),
    ("自然言語処理", "Natural Language Processing", "North_America", "言語学", "コンピュータを用いて人間の言語を理解・生成・分析する学際分野。言語学・コンピュータ科学・機械学習が融合する。", "https://en.wikipedia.org/wiki/Natural_language_processing", 1950),
    # 音声学・音韻論 (50件)
    ("音声学", "Phonetics", "Western_Europe", "言語学", "言語音声の物理的・生理的側面を研究する分野。調音音声学・音響音声学・聴覚音声学に区分される。IPA（国際音声字母）が記述の標準ツール。", "https://en.wikipedia.org/wiki/Phonetics", 1877),
    ("音韻論", "Phonology", "Global_Synthesis", "言語学", "言語システムにおける音の機能的・抽象的側面を研究する分野。音素・音節・音調・音韻規則が主要研究対象。", "https://en.wikipedia.org/wiki/Phonology", 1916),
    ("音素", "Phoneme", "Western_Europe", "言語学", "意味を区別する最小の音声単位。ソシュール・ボードワン・ドゥ・クルトネ・ヤコブソンらが概念を確立した。", "https://en.wikipedia.org/wiki/Phoneme", 1911),
    ("変音", "Allophone", "Western_Europe", "言語学", "同一音素の音声的実現形。環境によって交替するが意味の区別には関与しない。例：英語の語頭・語末のp音の帯気/無帯気の違い。", "https://en.wikipedia.org/wiki/Allophone", 1920),
    ("弁別素性", "Distinctive Features", "North_America", "言語学", "ヤコブソン・ファント・ハレ（1952）が提唱した音韻理論の単位。音素を有声性・閉鎖性・鼻音性などの二項対立素性の束として分析する。", "https://en.wikipedia.org/wiki/Distinctive_feature", 1952),
    ("自律分節音韻論", "Autosegmental Phonology", "North_America", "言語学", "ゴールドスミス（1976）が提唱した音韻理論。音韻表示を複数の層（音段層・音調層・音節層）に分解し、それぞれが独立したティアをなすとする。", "https://en.wikipedia.org/wiki/Autosegmental_phonology", 1976),
    ("韻律音韻論", "Prosodic Phonology", "North_America", "言語学", "音節・フット・音韻語・音韻句・発話などの韻律単位の階層構造を研究する分野。セルカークとネスポル＆ヴォゲルが基盤を確立した。", "https://en.wikipedia.org/wiki/Prosodic_hierarchy", 1980),
    ("音調言語", "Tone Language", "Global_Synthesis", "言語学", "音の高低（声調）が語彙的意味を区別する言語。中国語・タイ語・ヨルバ語などが代表例。アフリカとアジアに特に多く分布する。", "https://en.wikipedia.org/wiki/Tone_language", 1890),
    ("アクセント", "Lexical Accent", "Global_Synthesis", "言語学", "語内の特定音節を際立たせる音声的特徴。日本語のピッチアクセント・英語の強弱アクセントなど言語によって実現形が異なる。", "https://en.wikipedia.org/wiki/Accent_(linguistics)", 1870),
    ("音節構造", "Syllable Structure", "Global_Synthesis", "言語学", "音節の内部構造（頭子音・核母音・末子音）を分析する音韻論の分野。CV・CVC・CCVC など言語ごとに許容される型が異なる。", "https://en.wikipedia.org/wiki/Syllable", 1970),
    # 計算言語学・応用言語学 (50件)
    ("言語習得", "Language Acquisition", "North_America", "言語学", "子どもが母語を習得するプロセスを研究する分野。チョムスキーの生得説・トマセロの使用基盤理論が主要な対立仮説を形成している。", "https://en.wikipedia.org/wiki/Language_acquisition", 1959),
    ("第二言語習得", "Second Language Acquisition", "Global_Synthesis", "言語学", "母語以外の言語を習得するプロセスを研究する分野。中間言語・入力仮説・モニター仮説が理論的中心。クラッシェン（1982）が影響力を持つ。", "https://en.wikipedia.org/wiki/Second-language_acquisition", 1967),
    ("中間言語", "Interlanguage", "North_America", "言語学", "セリンカー（1972）が提唱した概念。第二言語学習者が発達段階で使用する、母語でも目標言語でもない独自の言語システム。", "https://en.wikipedia.org/wiki/Interlanguage", 1972),
    ("入力仮説", "Input Hypothesis", "North_America", "言語学", "クラッシェン（1985）が提唱した第二言語習得仮説。学習者が現在の能力をわずかに超えた理解可能な入力（i+1）を受けることで習得が進む。", "https://en.wikipedia.org/wiki/Input_hypothesis", 1985),
    ("出力仮説", "Output Hypothesis", "North_America", "言語学", "スウェイン（1985）が提唱した習得仮説。言語産出（アウトプット）が気づきを促し、文法的知識の精緻化をもたらすと主張する。", "https://en.wikipedia.org/wiki/Output_hypothesis", 1985),
    ("バイリンガリズム研究", "Bilingualism Research", "Global_Synthesis", "言語学", "二言語使用者の言語処理・習得・維持・喪失を研究する分野。バイリンガル利点仮説（実行機能の強化）と批判的再検討が現在の争点。", "https://en.wikipedia.org/wiki/Bilingualism", 1960),
    ("言語障害学", "Aphasiology", "Western_Europe", "言語学", "脳損傷による言語機能の障害（失語症）を研究する分野。ブローカ（1861）・ウェルニッケ（1874）の古典的症例が理論の出発点。", "https://en.wikipedia.org/wiki/Aphasia", 1861),
    ("神経言語学", "Neurolinguistics", "Global_Synthesis", "言語学", "言語処理の神経基盤を研究する分野。脳画像技術（fMRI・EEG・MEG）を用いてブローカ野・ウェルニッケ野などの機能を明らかにする。", "https://en.wikipedia.org/wiki/Neurolinguistics", 1970),
    ("言語教育学", "Language Pedagogy", "Global_Synthesis", "言語学", "外国語・第二言語の効果的な教授法を研究する応用言語学の分野。コミュニカティブ・アプローチ・内容言語統合学習（CLIL）が主流的方法論。", "https://en.wikipedia.org/wiki/Language_education", 1960),
    ("語彙意味論", "Lexical Semantics", "Global_Synthesis", "言語学", "個々の語の意味・語義関係（同義・反義・上位・下位）・多義性を研究する意味論の分野。ワードネット（フェルバウム1998）が代表的リソース。", "https://en.wikipedia.org/wiki/Lexical_semantics", 1970),
    ("形式意味論", "Formal Semantics", "North_America", "言語学", "モンタギュー（1970）が確立した意味論。数理論理学（型理論・ラムダ計算・モデル理論）を用いて自然言語の意味を形式的に記述する。", "https://en.wikipedia.org/wiki/Formal_semantics_(linguistics)", 1970),
    ("指示意味論", "Reference Theory", "Western_Europe", "言語学", "言語表現と世界の対象の関係（指示・意味・真理条件）を研究する。フレーゲ（1892）・ラッセル・クリプキ（1980）が主要理論家。", "https://en.wikipedia.org/wiki/Reference_(linguistics)", 1892),
    ("テンス・アスペクト研究", "Tense and Aspect Theory", "Global_Synthesis", "言語学", "動詞の時制（発話時との時間関係）とアスペクト（事象の内的時間構造）を研究する意味論の分野。コムリー（1976）が類型論的基盤を確立した。", "https://en.wikipedia.org/wiki/Tense%E2%80%93aspect%E2%80%93mood", 1976),
    ("モダリティ", "Modality in Linguistics", "Global_Synthesis", "言語学", "話者の命題への態度（必然性・可能性・義務・許可）を表す言語カテゴリ。認識モダリティと当為モダリティが基本的区分として用いられる。", "https://en.wikipedia.org/wiki/Modality_(linguistics)", 1970),
    ("語彙拡散", "Lexical Diffusion", "North_America", "言語学", "王士元（1969）が提唱した音変化の伝播モデル。音変化は語を単位として段階的に語彙全体に広がるとする。青年文法学派の例外なき音変化論への対案。", "https://en.wikipedia.org/wiki/Lexical_diffusion", 1969),
]

def insert_batch(concepts_list):
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()

    # 既存 name_en を取得して重複チェック
    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept WHERE name_en IS NOT NULL").fetchall())

    inserted = 0
    skipped = 0

    for i, (name_ja, name_en, culture_region, subfield, definition, source_url, era_start) in enumerate(concepts_list):
        if name_en in existing:
            skipped += 1
            continue

        cid = gen_id()
        cur.execute("""
            INSERT INTO humanities_concept (
                id, name_ja, name_en, definition, subfield, culture_region,
                era_start, source_url, verification_status, quality_flag,
                status, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'url_present', 'dua_wave_a2',
                      'active', ?, ?)
        """, (cid, name_ja, name_en, definition, subfield, culture_region,
              era_start, source_url, NOW, NOW))
        existing.add(name_en)
        inserted += 1

        if (i + 1) % 500 == 0:
            conn.commit()

    conn.commit()
    conn.close()
    return inserted, skipped

inserted, skipped = insert_batch(concepts)
print(f"Batch 1 (言語学): inserted={inserted}, skipped={skipped}")

# 確認
conn = sqlite3.connect(DB)
total = conn.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
ling = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='言語学'").fetchone()[0]
conn.close()
print(f"総件数: {total}, 言語学: {ling}")
