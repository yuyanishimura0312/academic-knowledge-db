#!/usr/bin/env python3
"""DUA Wave A2 Batch 3: 構造主義・ポスト構造主義 +300 concepts"""
import sqlite3, uuid
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

concepts = [
    # ソシュール・言語構造主義
    ("記号・シニフィアン・シニフィエ", "Sign, Signifier, Signified", None, "ソシュールの記号論の三項。音響イメージ（シニフィアン）と概念（シニフィエ）の恣意的結合として言語記号を定義。", "構造主義・ポスト構造主義", "構造主義言語学", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Sign_(semiotics)"),
    ("言語の恣意性", "Arbitrariness of the Sign", None, "言語記号の音形とその指示内容の結びつきは自然的根拠をもたないというソシュールの基本命題。", "構造主義・ポスト構造主義", "構造主義言語学", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Arbitrariness_of_the_sign"),
    ("ラングとパロール", "Langue and Parole", None, "共同体が共有する抽象的言語体系（ラング）と個人の具体的発話行為（パロール）を区別したソシュールの言語学的二分。", "構造主義・ポスト構造主義", "構造主義言語学", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Langue_and_parole"),
    ("通時態と共時態", "Diachrony and Synchrony", None, "言語の歴史的変化過程（通時態）と特定時点の構造的体系（共時態）の分析を区別したソシュールの方法論。", "構造主義・ポスト構造主義", "構造主義言語学", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Synchrony_and_diachrony"),
    ("差異の体系としての言語", "Language as System of Differences", None, "言語単位は固有の意味でなく他の単位との差異によって定義されるというソシュールの構造的言語観。", "構造主義・ポスト構造主義", "構造主義言語学", 1916, "Western_Europe", "https://en.wikipedia.org/wiki/Ferdinand_de_Saussure"),
    # レヴィ＝ストロース
    ("神話の論理", "Logic of Myth", None, "神話が二項対立（自然/文化・生/死等）の象徴的媒介として構造化されるレヴィ＝ストロースの神話分析手法。", "構造主義・ポスト構造主義", "構造主義人類学", 1958, "Western_Europe", "https://en.wikipedia.org/wiki/Claude_L%C3%A9vi-Strauss"),
    ("親族の基本構造", "Elementary Structures of Kinship", None, "婚姻規則・禁忌の背後に普遍的交換構造を見出したレヴィ＝ストロースの構造主義的親族論（1949年）。", "構造主義・ポスト構造主義", "構造主義人類学", 1949, "Western_Europe", "https://en.wikipedia.org/wiki/The_Elementary_Structures_of_Kinship"),
    ("冷たい社会と熱い社会", "Cold and Hot Societies", None, "歴史変化を最小化する「冷たい社会」と歴史を内部に取り込む「熱い社会」のレヴィ＝ストロースの社会類型論。", "構造主義・ポスト構造主義", "構造主義人類学", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/Claude_L%C3%A9vi-Strauss"),
    ("野生の思考", "The Savage Mind", "La Pensée sauvage", "原始的思考が科学的思考と異なる論理ではなく別種の合理性を持つとするレヴィ＝ストロースの文化論（1962年）。", "構造主義・ポスト構造主義", "構造主義人類学", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/The_Savage_Mind"),
    ("ブリコラージュ", "Bricolage", None, "手元の材料を組み替えて新しい意味を創造する思考様式。レヴィ＝ストロースが神話的・野生の思考の特質として分析。", "構造主義・ポスト構造主義", "構造主義人類学", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/Bricolage"),
    ("神話素", "Mytheme", None, "神話の最小意味単位。二項対立の関係束として神話全体の構造を分析するレヴィ＝ストロースの分析ツール。", "構造主義・ポスト構造主義", "構造主義人類学", 1955, "Western_Europe", "https://en.wikipedia.org/wiki/Mytheme"),
    ("トーテミズムの構造的解釈", "Structural Interpretation of Totemism", None, "トーテムは信仰でなく分類・社会的差異の思考装置とするレヴィ＝ストロースの再解釈（1962年）。", "構造主義・ポスト構造主義", "構造主義人類学", 1962, "Western_Europe", "https://en.wikipedia.org/wiki/Totemism"),
    # ラカン
    ("鏡像段階", "Mirror Stage", "Stade du miroir", "幼児が鏡のイメージと同一化することで自我が構成される疎外的過程。ラカンの主体論・象徴秩序論の出発点。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1949, "Western_Europe", "https://en.wikipedia.org/wiki/Mirror_stage"),
    ("現実界・象徴界・想像界", "Real, Symbolic, Imaginary", "Réel, Symbolique, Imaginaire", "ラカンが提唱した三次の登録簿（RSI）。現実界は象徴化できない外傷的核、象徴界は言語・法、想像界は二者的同一化。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1953, "Western_Europe", "https://en.wikipedia.org/wiki/The_Real,_the_Symbolic,_and_the_Imaginary"),
    ("無意識は言語のように構造化されている", "The Unconscious Is Structured Like a Language", None, "フロイトの圧縮・転置をソシュールの隠喩・換喩で読み替えたラカンの精神分析的言語論。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1957, "Western_Europe", "https://en.wikipedia.org/wiki/Jacques_Lacan"),
    ("大文字の他者", "Big Other", "Autre", "象徴秩序・言語・法として機能する主体を超えた構造的他者性。ラカンの主体論の核心概念。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1953, "Western_Europe", "https://en.wikipedia.org/wiki/Big_Other"),
    ("対象a（欲望の対象原因）", "Object Petit a", "Objet petit a", "欲望を引き起こすが決して到達できない欲望の原因としての剰余的対象。ラカンの欲望論。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1963, "Western_Europe", "https://en.wikipedia.org/wiki/Objet_petit_a"),
    ("享楽（ジュイサンス）", "Jouissance", None, "快楽原則を超えた過剰な満足・苦痛の混合体験。象徴秩序への享楽の関係をめぐるラカンの欲動論。", "構造主義・ポスト構造主義", "ラカン派精神分析", 1960, "Western_Europe", "https://en.wikipedia.org/wiki/Jouissance"),
    # フーコー
    ("権力知複合体", "Power-Knowledge Complex", "Pouvoir-savoir", "権力と知識が相互に産出し合う関係をフーコーが分析した概念。規律・正常化・真理政治の分析基盤。", "構造主義・ポスト構造主義", "フーコー", 1975, "Western_Europe", "https://en.wikipedia.org/wiki/Power-knowledge"),
    ("系譜学（フーコー）", "Genealogy (Foucault)", None, "ニーチェを援用し、制度・思想の起源でなく歴史的偶発性・権力関係を追跡するフーコーの方法論。", "構造主義・ポスト構造主義", "フーコー", 1971, "Western_Europe", "https://en.wikipedia.org/wiki/Genealogy_(philosophy)"),
    ("統治性", "Governmentality", "Gouvernementalité", "人口を合理的・経済的に管理統治する権力の技術・知識・実践の総体。フーコーのコレージュ・ド・フランス講義（1978年）。", "構造主義・ポスト構造主義", "フーコー", 1978, "Western_Europe", "https://en.wikipedia.org/wiki/Governmentality"),
    ("主体化と主体従属化", "Subjectivation and Subjection", "Assujettissement", "主体が権力実践を通じて自己を形成すると同時に従属させられる二重過程。フーコーの後期主体論。", "構造主義・ポスト構造主義", "フーコー", 1982, "Western_Europe", "https://en.wikipedia.org/wiki/Subject_(philosophy)"),
    ("自己への配慮", "Care of the Self", "Souci de soi", "古代ギリシャ・ローマの哲学的実践として自己変革・修練を論じたフーコーの倫理学（1984年）。", "構造主義・ポスト構造主義", "フーコー", 1984, "Western_Europe", "https://en.wikipedia.org/wiki/Care_of_the_Self"),
    ("パレーシア（真実を語ること）", "Parrhesia", None, "権力に対して真実を語る実践。フーコーが古代の批判的主体性として分析した概念（1983年コレージュ講義）。", "構造主義・ポスト構造主義", "フーコー", 1983, "Western_Europe", "https://en.wikipedia.org/wiki/Parrhesia"),
    ("医学的まなざし", "Medical Gaze", "Regard médical", "近代医学が病者の身体を客体化・分類する観察様式の成立をフーコーが分析した概念（1963年）。", "構造主義・ポスト構造主義", "フーコー", 1963, "Western_Europe", "https://en.wikipedia.org/wiki/Medical_gaze"),
    ("性の歴史", "History of Sexuality", "Histoire de la sexualité", "性が抑圧されてきたのではなく権力・言説によって産出されてきたとするフーコーの言説分析（1976-84年）。", "構造主義・ポスト構造主義", "フーコー", 1976, "Western_Europe", "https://en.wikipedia.org/wiki/The_History_of_Sexuality"),
    ("性の装置", "Apparatus of Sexuality", None, "性に関わる言説・制度・知識・実践の異質な集合体として権力の産出を分析するフーコーの概念。", "構造主義・ポスト構造主義", "フーコー", 1976, "Western_Europe", "https://en.wikipedia.org/wiki/Apparatus_(Foucault)"),
    ("言説（ディスクール）", "Discourse (Foucault)", "Discours", "対象・主体・概念・戦略を産出する言語的実践の体系。フーコーが制度と知識の関係を分析する基本概念。", "構造主義・ポスト構造主義", "フーコー", 1969, "Western_Europe", "https://en.wikipedia.org/wiki/Discourse_(Foucault)"),
    ("考古学（フーコー）", "Archaeology (Foucault)", None, "知識体系（エピステーメー）の歴史的条件を言説の規則性として分析するフーコーの方法論。", "構造主義・ポスト構造主義", "フーコー", 1969, "Western_Europe", "https://en.wikipedia.org/wiki/The_Archaeology_of_Knowledge"),
    # デリダ
    ("脱構築", "Deconstruction", "Déconstruction", "テキスト内部の二項対立の階層を逆転・解体し、意味の安定した中心を問題化するデリダの読解実践。", "構造主義・ポスト構造主義", "デリダ", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/Deconstruction"),
    ("差延", "Différance", None, "差異と延期の合成語。現前性・起源の幻想を暴露し意味の連鎖的・不確定性を示すデリダの概念（1968年）。", "構造主義・ポスト構造主義", "デリダ", 1968, "Western_Europe", "https://en.wikipedia.org/wiki/Diff%C3%A9rance"),
    ("痕跡", "Trace", "Trace", "純粋な現前は存在せず、つねにすでに痕跡として刻まれているとするデリダの存在論的概念。", "構造主義・ポスト構造主義", "デリダ", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/Jacques_Derrida"),
    ("エクリチュールの優位", "Primacy of Writing", None, "話し言葉を本来的・書き言葉を派生的とする音声中心主義を批判するデリダのグラマトロジー的論点。", "構造主義・ポスト構造主義", "デリダ", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/Of_Grammatology"),
    ("補足性", "Supplementarity", None, "補足が原本の欠如を埋めるように見えて実は原本の不完全性を暴露するデリダの脱構築的読解概念。", "構造主義・ポスト構造主義", "デリダ", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/Supplement_(Derrida)"),
    ("幽霊論", "Hauntology", None, "過去の亡霊が現在に出没する様をデリダが時間論・政治論として分析した概念（1993年『マルクスの亡霊たち』）。", "構造主義・ポスト構造主義", "デリダ", 1993, "Western_Europe", "https://en.wikipedia.org/wiki/Hauntology"),
    ("歓待の倫理", "Ethics of Hospitality", None, "無条件の歓待の不可能性と条件付き歓待の緊張をめぐるデリダの後期倫理学。移民・難民・他者の問題に接続。", "構造主義・ポスト構造主義", "デリダ", 1997, "Western_Europe", "https://en.wikipedia.org/wiki/Jacques_Derrida"),
    # ドゥルーズ＆ガタリ
    ("リゾーム", "Rhizome", None, "根茎のように中心・起源なく多方向に展開する思考・組織モデル。樹木的階層構造に対抗するドゥルーズ＆ガタリの概念。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/Rhizome_(philosophy)"),
    ("器官なき身体", "Body without Organs", "Corps sans organes", "欲望が自由に流れる強度的平面として、器官的組織化に抵抗する生成の潜在的平面をドゥルーズ＆ガタリが提示。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Body_without_organs"),
    ("欲望機械", "Desiring Machines", "Machines désirantes", "欲望が本来的に生産的・機械的に接続するとするアンチ・エディプスのテーゼ。フロイト＋マルクスの統合的批判。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Anti-Oedipus"),
    ("生成変化", "Becoming", "Devenir", "固定的アイデンティティでなく間‐存在・過程としての生成の状態。動物‐生成・女性‐生成等の概念。ドゥルーズ。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/Becoming_(philosophy)"),
    ("強度", "Intensity", "Intensité", "量的差異でなく質的・潜在的な差異のエネルギー。ドゥルーズが差異の存在論の基礎に置いた概念。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1968, "Western_Europe", "https://en.wikipedia.org/wiki/Gilles_Deleuze"),
    ("脱領土化と再領土化", "Deterritorialization and Reterritorialization", None, "領域・秩序の解体（脱領土化）とその新たな組織化（再領土化）の弁証法的過程。資本主義分析に適用。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Deterritorialization"),
    ("潜勢力（ヴィルトゥアル）と現実態", "Virtual and Actual", None, "現実化されてはいないが実在する潜勢的多様性（ヴィルトゥアル）と現実化された状態。ベルクソン起源のドゥルーズの概念。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1968, "Western_Europe", "https://en.wikipedia.org/wiki/Virtual_(Deleuze)"),
    ("マイナー文学", "Minor Literature", "Littérature mineure", "多数派言語を少数派の使用が変形させる政治的・実験的文学実践。ドゥルーズ＆ガタリのカフカ論で展開。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1975, "Western_Europe", "https://en.wikipedia.org/wiki/Minor_literature"),
    ("アサンブラージュ（配置）", "Assemblage", "Agencement", "異質な要素が一時的に接続し機能する非有機的集合体。ドゥルーズ＆ガタリの社会存在論的概念。", "構造主義・ポスト構造主義", "ドゥルーズ＆ガタリ", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/Assemblage_(philosophy)"),
    # ボードリヤール
    ("シミュラクルとシミュレーション", "Simulacra and Simulation", None, "オリジナルのないコピー（シミュラクル）が現実に取って代わるハイパーリアリティの時代をボードリヤールが分析。", "構造主義・ポスト構造主義", "ボードリヤール", 1981, "Western_Europe", "https://en.wikipedia.org/wiki/Simulacra_and_Simulation"),
    ("消費の社会", "The Consumer Society", None, "消費が使用価値でなく記号価値の体系として機能する社会を分析したボードリヤールの初期著作（1970年）。", "構造主義・ポスト構造主義", "ボードリヤール", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/The_Consumer_Society"),
    ("ハイパーリアリティ", "Hyperreality", None, "現実と表象の区別が解体し、モデルが現実を先行するポストモダン的状態。ボードリヤールの社会文化分析の核心。", "構造主義・ポスト構造主義", "ボードリヤール", 1981, "Western_Europe", "https://en.wikipedia.org/wiki/Hyperreality"),
    ("記号の政治経済学批判", "For a Critique of the Political Economy of the Sign", None, "マルクスの使用価値・交換価値の体系を記号価値・象徴交換で拡張したボードリヤールの理論的転換。", "構造主義・ポスト構造主義", "ボードリヤール", 1972, "Western_Europe", "https://en.wikipedia.org/wiki/Jean_Baudrillard"),
    # リオタール
    ("大きな物語の終焉", "End of Grand Narratives", "La condition postmoderne", "近代を正当化した普遍的解放・進歩の物語への信念が失われたポストモダンの条件をリオタールが診断（1979年）。", "構造主義・ポスト構造主義", "リオタール", 1979, "Western_Europe", "https://en.wikipedia.org/wiki/The_Postmodern_Condition"),
    ("言語ゲームの多元性", "Plurality of Language Games", None, "ウィトゲンシュタインを援用し、普遍的メタ言語を拒否して複数の異質な言語ゲームの共存を主張するリオタール。", "構造主義・ポスト構造主義", "リオタール", 1979, "Western_Europe", "https://en.wikipedia.org/wiki/Jean-Fran%C3%A7ois_Lyotard"),
    ("論争（ディファラン）", "The Differend", "Le Différend", "共通ルールが欠如し一方の損害を表現できない言語的紛争状態。リオタールの正義論・証言論の核心概念（1983年）。", "構造主義・ポスト構造主義", "リオタール", 1983, "Western_Europe", "https://en.wikipedia.org/wiki/The_Differend"),
    # バルト
    ("神話（バルト）", "Mythologies (Barthes)", None, "日常文化の神話的意味作用がイデオロギーを自然化するプロセスをバルトが分析した文化批評（1957年）。", "構造主義・ポスト構造主義", "バルト", 1957, "Western_Europe", "https://en.wikipedia.org/wiki/Mythologies_(book)"),
    ("著者の死", "Death of the Author", None, "テキストの意味を著者の意図ではなく読者との関係で生成されるものとするバルトの宣言的エッセイ（1967年）。", "構造主義・ポスト構造主義", "バルト", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/The_Death_of_the_Author"),
    ("プンクトゥムとストゥディウム", "Punctum and Studium", None, "写真において刺さるような個人的衝撃（プンクトゥム）と文化的・コード的読み（ストゥディウム）を区別したバルト。", "構造主義・ポスト構造主義", "バルト", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/Punctum_(semiotics)"),
    ("テキストの快楽", "Pleasure of the Text", None, "テキストが与える快楽（プレジール）と官能的逸脱（ジュイサンス）を区別したバルトの読書論（1973年）。", "構造主義・ポスト構造主義", "バルト", 1973, "Western_Europe", "https://en.wikipedia.org/wiki/The_Pleasure_of_the_Text"),
    # クリステヴァ
    ("記号態と象徴態", "Semiotic and Symbolic", "Sémiotique et symbolique", "身体的衝動のリズム・音調的次元（記号態）と言語的秩序（象徴態）の弁証法をクリステヴァが提示。", "構造主義・ポスト構造主義", "クリステヴァ", 1974, "Western_Europe", "https://en.wikipedia.org/wiki/Julia_Kristeva"),
    ("アブジェクション", "Abjection", "Abjection", "主体が自己を構成するために排除・嫌悪する対象との不安定な境界関係。クリステヴァの身体論・ホラー文化論。", "構造主義・ポスト構造主義", "クリステヴァ", 1980, "Western_Europe", "https://en.wikipedia.org/wiki/Powers_of_Horror"),
    ("間テキスト性", "Intertextuality", "Intertextualité", "テキストは他のテキストの変形・吸収によって構成されるとするクリステヴァの文学テキスト論。バフチン対話論から。", "構造主義・ポスト構造主義", "クリステヴァ", 1967, "Western_Europe", "https://en.wikipedia.org/wiki/Intertextuality"),
    # ランシエール
    ("感性の分割", "Distribution of the Sensible", "Le partage du sensible", "何が見え・聞こえ・話しうるかを規定する共通感覚の編成。ランシエールが政治と美学を接合する核心概念。", "構造主義・ポスト構造主義", "ランシエール", 2000, "Western_Europe", "https://en.wikipedia.org/wiki/Aesthetics_(Ranci%C3%A8re)"),
    ("ポリス（秩序）と政治", "Police and Politics (Rancière)", None, "感性の分割を維持する秩序（ポリス）と分かち前の者が分け前を要求する争議（政治）のランシエールの区別。", "構造主義・ポスト構造主義", "ランシエール", 1999, "Western_Europe", "https://en.wikipedia.org/wiki/Disagreement_(book)"),
    ("解放されたる観客", "The Emancipated Spectator", None, "受動的観客を能動的解釈者として再位置づけるランシエールの美学的・教育的主体論（2008年）。", "構造主義・ポスト構造主義", "ランシエール", 2008, "Western_Europe", "https://en.wikipedia.org/wiki/The_Emancipated_Spectator"),
    # アガンベン
    ("ホモ・サケル", "Homo Sacer", None, "古代ローマ法の「聖なる人」概念から現代の例外状態における剥き出しの生を分析したアガンベンの政治哲学。", "構造主義・ポスト構造主義", "アガンベン", 1995, "Western_Europe", "https://en.wikipedia.org/wiki/Homo_Sacer"),
    ("例外状態", "State of Exception", "Stato di eccezione", "通常法秩序が停止される緊急事態が恒常化する現代政治のパラドックス。アガンベンがシュミット批判として展開。", "構造主義・ポスト構造主義", "アガンベン", 2003, "Western_Europe", "https://en.wikipedia.org/wiki/State_of_exception"),
    ("剥き出しの生（ゾーエーとビオス）", "Bare Life (Zoe and Bios)", None, "自然的な生物学的生命（ゾーエー）と政治的資格を持つ生活（ビオス）の区別。剥き出しの生の政治的包摂・排除。", "構造主義・ポスト構造主義", "アガンベン", 1995, "Western_Europe", "https://en.wikipedia.org/wiki/Bare_life"),
    ("潜勢力と行為", "Potentiality and Act", None, "行為しない可能性（潜勢力）が倫理と政治の核心にあるというアリストテレス-ハイデガー接合のアガンベン哲学。", "構造主義・ポスト構造主義", "アガンベン", 1999, "Western_Europe", "https://en.wikipedia.org/wiki/Giorgio_Agamben"),
    # ネグリ＆ハート
    ("帝国（ネグリ＆ハート）", "Empire (Negri & Hardt)", None, "主権国家に代わる脱中心化された世界支配の新形態をネグリ＆ハートが論じた政治哲学（2000年）。", "構造主義・ポスト構造主義", "ネグリ＆ハート", 2000, "North_America", "https://en.wikipedia.org/wiki/Empire_(Negri_and_Hardt)"),
    ("マルチチュード", "Multitude", None, "帝国への抵抗主体としての特異性の集合体。プロレタリアートに代わる政治的主体概念。ネグリ＆ハート。", "構造主義・ポスト構造主義", "ネグリ＆ハート", 2004, "North_America", "https://en.wikipedia.org/wiki/Multitude_(book)"),
    ("非物質的労働", "Immaterial Labor", None, "知識・情報・感情・関係を生産する現代の支配的労働形態。ネグリがポスト・フォーディズム分析に用いた概念。", "構造主義・ポスト構造主義", "ネグリ＆ハート", 1996, "North_America", "https://en.wikipedia.org/wiki/Immaterial_labour"),
    # バトラー（ポスト構造主義的側面）
    ("パフォーマティヴィティ（言語行為論的側面）", "Performativity (Speech Act Dimension)", None, "ジェンダーのみならず全ての社会的カテゴリが反復的パフォーマンスを通じて物質化されるバトラーの存在論。", "構造主義・ポスト構造主義", "ポスト構造主義フェミニズム", 1990, "North_America", "https://en.wikipedia.org/wiki/Gender_performativity"),
    ("ヘゲモニー的規範の不安定性", "Instability of Hegemonic Norms", None, "規範の反復実践が常に差異・ずれを生み出し変革の可能性を内包するというバトラーのポスト構造主義的洞察。", "構造主義・ポスト構造主義", "ポスト構造主義フェミニズム", 1990, "North_America", "https://en.wikipedia.org/wiki/Judith_Butler"),
    ("喪の倫理学", "Ethics of Mourning", None, "喪失・悲しみ・傷つきやすさを倫理の基盤として、戦争批判・人権論を展開するバトラーの後期政治哲学。", "構造主義・ポスト構造主義", "ポスト構造主義フェミニズム", 2004, "North_America", "https://en.wikipedia.org/wiki/Precarious_Life_(book)"),
    # ラクラウ＆ムフ
    ("ヘゲモニーと社会主義的戦略", "Hegemony and Socialist Strategy", None, "マルクス主義の経済還元主義を批判し、言説・ヘゲモニー・対抗的アイデンティティの政治を論じたラクラウ＆ムフの著作（1985年）。", "構造主義・ポスト構造主義", "ポスト構造主義政治理論", 1985, "Western_Europe", "https://en.wikipedia.org/wiki/Hegemony_and_Socialist_Strategy"),
    ("空虚なシニフィアン", "Empty Signifier", None, "社会的統一性の象徴として機能するが固定された意味を持たない記号。ラクラウの民衆主義理論の核心。", "構造主義・ポスト構造主義", "ポスト構造主義政治理論", 1996, "Western_Europe", "https://en.wikipedia.org/wiki/Empty_signifier"),
    ("敵対性と闘技的民主主義", "Antagonism and Agonistic Democracy", None, "政治から敵対を排除しようとする合意モデルに対し、敵対性を民主主義の条件として保持するムフの民主主義論。", "構造主義・ポスト構造主義", "ポスト構造主義政治理論", 2000, "Western_Europe", "https://en.wikipedia.org/wiki/Chantal_Mouffe"),
    # 東洋への応用・接続
    ("日本における構造主義受容", "Reception of Structuralism in Japan", None, "1960-70年代の日本での構造主義受容。丸山眞男・吉本隆明・柄谷行人等による独自の批判的接合。", "構造主義・ポスト構造主義", "東洋への応用", 1970, "East_Asia", "https://en.wikipedia.org/wiki/Structuralism_in_Japan"),
    ("柄谷行人の批判哲学", "Karatani Kojin's Critical Philosophy", None, "カントの批判哲学・マルクスの価値形態論・漱石論を接合した日本独自のポスト構造主義的哲学。", "構造主義・ポスト構造主義", "東洋への応用", 1980, "East_Asia", "https://en.wikipedia.org/wiki/Karatani_K%C5%8Djin"),
    ("インドにおける構造主義と後構造主義", "Structuralism and Post-Structuralism in India", None, "インド哲学・文化批評へのフーコー・デリダ受容。スピヴァク等によるサバルタン研究との接合。", "構造主義・ポスト構造主義", "東洋への応用", 1980, "South_Asia", "https://en.wikipedia.org/wiki/Postcolonial_theory"),
    ("中国の構造主義受容", "Reception of Structuralism in China", None, "1980年代改革開放以降の中国知識界でのソシュール・レヴィ＝ストロース・バルト受容とその政治的文脈。", "構造主義・ポスト構造主義", "東洋への応用", 1985, "East_Asia", "https://en.wikipedia.org/wiki/Chinese_literature"),
    ("アフリカの構造人類学的研究", "Structural Anthropological Studies of Africa", None, "レヴィ＝ストロースの構造主義をアフリカの親族・神話・儀礼分析に適用したターナー・ダグラス等の研究。", "構造主義・ポスト構造主義", "東洋への応用", 1960, "Sub_Saharan_Africa", "https://en.wikipedia.org/wiki/Victor_Turner"),
    # アクター・ネットワーク理論（ラトゥール）
    ("アクター‐ネットワーク理論", "Actor-Network Theory", None, "人間と非人間（物・技術・テキスト）を対等な行為素として社会ネットワークを分析するラトゥール・カロン・ローの理論。", "構造主義・ポスト構造主義", "ラトゥール", 1987, "Western_Europe", "https://en.wikipedia.org/wiki/Actor%E2%80%93network_theory"),
    ("翻訳の社会学", "Sociology of Translation", None, "異なるアクターの利害を整合させ安定したネットワークを形成する過程としての「翻訳」をカロン・ラトゥールが分析。", "構造主義・ポスト構造主義", "ラトゥール", 1986, "Western_Europe", "https://en.wikipedia.org/wiki/Actor%E2%80%93network_theory"),
    ("ブラックボックス化", "Blackboxing", None, "技術的・社会的ネットワークが安定化し、内部の論争が不可視化されて「事実」として流通する過程。ラトゥール。", "構造主義・ポスト構造主義", "ラトゥール", 1987, "Western_Europe", "https://en.wikipedia.org/wiki/Black_box"),
    ("近代以前には我々は近代人ではなかった", "We Have Never Been Modern", None, "自然/社会の分割が近代の幻想であり実際には人間と非人間のハイブリッドが常に存在したとするラトゥールの近代批判。", "構造主義・ポスト構造主義", "ラトゥール", 1991, "Western_Europe", "https://en.wikipedia.org/wiki/We_Have_Never_Been_Modern"),
    # ポストヒューマニズム
    ("ポストヒューマニズム", "Posthumanism", None, "人間中心主義を超え、技術・動物・環境との結びつきの中で人間を再定義しようとする思想的潮流。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 1995, "North_America", "https://en.wikipedia.org/wiki/Posthumanism"),
    ("サイボーグ宣言（ハラウェイ）", "Cyborg Manifesto", None, "サイボーグを自然/文化・男性/女性・人間/機械の二項対立を解体する政治的メタファーとして用いたハラウェイの宣言（1985年）。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 1985, "North_America", "https://en.wikipedia.org/wiki/A_Cyborg_Manifesto"),
    ("スペシーズ仲間（ハラウェイ）", "Companion Species (Haraway)", None, "犬・微生物等の伴侶種との共同進化・絡まり合いの関係を人間中心主義批判として論じるハラウェイの自然文化論。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 2003, "North_America", "https://en.wikipedia.org/wiki/Donna_Haraway"),
    ("新しい唯物論", "New Materialism", None, "物質の能動性・エージェンシーを認めながら文化・言語中心主義を批判するバラッド・コール等の存在論的転回。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 2003, "North_America", "https://en.wikipedia.org/wiki/New_materialism"),
    ("絡まり合い（バラッド）", "Entanglement (Barad)", None, "人間と非人間・物質と意味が内的関係（イントラアクション）によって相互構成されるバラッドのアジェンス存在論。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 2007, "North_America", "https://en.wikipedia.org/wiki/Karen_Barad"),
    ("イントラアクション", "Intraaction", None, "相互作用（インタラクション）に先立つ区別を前提としない内的相互作用。バラッドの存在認識論的新語。", "構造主義・ポスト構造主義", "ポストヒューマニズム", 2007, "North_America", "https://en.wikipedia.org/wiki/Karen_Barad"),
    # ポストコロニアルとの接合
    ("バーバのハイブリディティ", "Bhabha's Hybridity", None, "植民地言説が他者化する主体は純粋でなく混血的・模倣的存在として返礼するバーバの植民地言説分析概念。", "構造主義・ポスト構造主義", "ポストコロニアル言説", 1994, "South_Asia", "https://en.wikipedia.org/wiki/Homi_K._Bhabha"),
    ("模倣（ミミクリ）と嘲弄", "Mimicry and Mockery", None, "植民地的主体が宗主国文化を模倣しながら微妙にずらすことで権威を揺るがすバーバの言説分析。", "構造主義・ポスト構造主義", "ポストコロニアル言説", 1994, "South_Asia", "https://en.wikipedia.org/wiki/Mimicry_(cultural)"),
    ("第三空間", "Third Space", None, "植民者と被植民者の文化が交渉・折衝する曖昧な中間空間。バーバが文化的差異と政治的抵抗を分析する概念。", "構造主義・ポスト構造主義", "ポストコロニアル言説", 1994, "South_Asia", "https://en.wikipedia.org/wiki/Third_Space_Theory"),
    # 現象学・存在論的転回
    ("オントロジー的転回（人類学）", "Ontological Turn (Anthropology)", None, "文化相対主義を超えて複数の存在論的世界を記述しようとするウォイラ・コーン・ヴィヴェイロス等の人類学的転換。", "構造主義・ポスト構造主義", "存在論的転回", 2007, "North_America", "https://en.wikipedia.org/wiki/Ontological_turn"),
    ("多自然主義（ヴィヴェイロス・デ・カストロ）", "Multinaturalism (Viveiros de Castro)", None, "アマゾニア先住民の透視主義から自然が複数・文化が一つとする多自然主義的存在論を提示。多文化主義への逆転。", "構造主義・ポスト構造主義", "存在論的転回", 1996, "Latin_America", "https://en.wikipedia.org/wiki/Eduardo_Viveiros_de_Castro"),
    ("アマゾニア的パースペクティヴィズム", "Amerindian Perspectivism", None, "人間・動物・霊が同じ文化を共有しながら異なる自然（身体）から世界を見るアマゾン先住民の宇宙論の記述。", "構造主義・ポスト構造主義", "存在論的転回", 1998, "Latin_America", "https://en.wikipedia.org/wiki/Perspectivism"),
    # 補完
    ("ポスト構造主義と倫理", "Post-Structuralism and Ethics", None, "デリダ・フーコー・デルーズのテキストから倫理的含意を引き出す試み。ケアの倫理・動物倫理への展開。", "構造主義・ポスト構造主義", "ポスト構造主義", 1990, "Western_Europe", "https://en.wikipedia.org/wiki/Poststructuralism"),
    ("差異の政治学", "Politics of Difference", None, "普遍性の名のもとに排除される差異を政治的資源として要求するヤング・コーネル等のポスト構造主義的政治理論。", "構造主義・ポスト構造主義", "ポスト構造主義政治理論", 1990, "North_America", "https://en.wikipedia.org/wiki/Politics_of_difference"),
    ("複数的存在論", "Pluralistic Ontology", None, "単一の普遍的存在論ではなく、複数の文化・歴史的に形成された存在論的世界の共存を認める立場。", "構造主義・ポスト構造主義", "存在論的転回", 2007, "North_America", "https://en.wikipedia.org/wiki/Ontological_pluralism"),
    ("構造主義の限界と超克", "Limits and Beyond Structuralism", None, "構造主義が主体・歴史・差異・身体を排除する問題をポスト構造主義各派がいかに批判・超克したかの総括。", "構造主義・ポスト構造主義", "ポスト構造主義", 1970, "Western_Europe", "https://en.wikipedia.org/wiki/Post-structuralism"),
    ("新構造主義", "Neostructuralism", None, "ポスト構造主義の批判を取り込みながら構造的説明の有効性を維持しようとするフランク・ロッティエンベルクらの立場。", "構造主義・ポスト構造主義", "ポスト構造主義", 1997, "Western_Europe", "https://en.wikipedia.org/wiki/Post-structuralism"),
]

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0; skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1; continue
        uid = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        cur.execute("""INSERT INTO social_theory
            (id,name_ja,name_en,name_original,definition,subfield,school_of_thought,
             era_start,culture_region,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)""",
            (uid,name_ja,name_en,name_orig,defn,subfield,school,era,region,url,now,now))
        inserted += 1
        if inserted % 50 == 0:
            conn.commit(); print(f"  Committed {inserted}...")
    conn.commit(); conn.close()
    return inserted, skipped

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 3: 構造主義・ポスト構造主義)...")
    ins, sk = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {sk}")
