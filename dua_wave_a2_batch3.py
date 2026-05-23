#!/usr/bin/env python3
"""DUA Wave A2 Batch 3: 文学批評理論 +400件 + 言語学追加 +150件"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

concepts = [
    # 文学批評理論 — 新サブフィールド (80件)
    ("ロシア・フォルマリズム", "Russian Formalism", "Western_Europe", "文学批評理論", "シクロフスキー・ヤコブソン・エイヘンバウムら（1910-30年代）が発展させた文学理論。「文学性」の解明を目指し、異化・支配素・散文技法を分析概念とした。", "https://en.wikipedia.org/wiki/Russian_formalism", 1915),
    ("異化", "Defamiliarization (Ostranenie)", "Western_Europe", "文学批評理論", "シクロフスキー（1917）が提唱した文学の根本機能。自動化した知覚を更新し、事物を新たな眼で見させる芸術的手続き。", "https://en.wikipedia.org/wiki/Defamiliarization", 1917),
    ("プラハ言語学サークル", "Prague Linguistic Circle", "Western_Europe", "文学批評理論", "ムカルジョフスキー・ヤコブソンらが1926年に設立した学際的研究集団。機能的構造主義・詩的機能理論・前景化概念を確立した。", "https://en.wikipedia.org/wiki/Prague_linguistic_circle", 1926),
    ("詩的言語の機能", "Poetic Function of Language", "Western_Europe", "文学批評理論", "ヤコブソン（1960）の六機能モデル（表出・訴え・指示・メタ言語・交感・詩的）の一つ。メッセージ自体に向かう言語機能が詩的効果を生む。", "https://en.wikipedia.org/wiki/Jakobson%27s_functions_of_language", 1960),
    ("ニュークリティシズム", "New Criticism", "North_America", "文学批評理論", "ランサム・ブルックス・ウォーレンら（1930-60年代）が発展させた英米文学批評。作品の自律性・有機的統一性・意図的誤謬・情動的誤謬を原則とする。", "https://en.wikipedia.org/wiki/New_Criticism", 1930),
    ("意図的誤謬", "Intentional Fallacy", "North_America", "文学批評理論", "ウィムザット＆ビアズリー（1946）が提唱した概念。作者の意図を作品解釈の基準とすることは方法論的誤謬だと主張する。", "https://en.wikipedia.org/wiki/Intentional_fallacy", 1946),
    ("情動的誤謬", "Affective Fallacy", "North_America", "文学批評理論", "ウィムザット＆ビアズリー（1949）が提唱した概念。読者の感情的反応を作品の意味・価値の基準とすることへの批判。", "https://en.wikipedia.org/wiki/Affective_fallacy", 1949),
    ("テクストの精読", "Close Reading", "North_America", "文学批評理論", "ニュークリティシズムが確立した批評方法。詩・散文の語・イメージ・音・構造を精密に分析し、作品の複雑な意味を取り出す技法。", "https://en.wikipedia.org/wiki/Close_reading", 1930),
    ("構造主義詩学", "Structuralist Poetics", "Western_Europe", "文学批評理論", "レヴィ＝ストロース・グレマス・ジュネットらが発展させた文学理論。言語の構造的原理（二項対立・変換）を文学テキストの分析に適用する。", "https://en.wikipedia.org/wiki/Structuralism", 1960),
    ("グレマスの意味論的矩形", "Greimas's Semiotic Square", "Western_Europe", "文学批評理論", "グレマス（1966）が提唱した意味分析モデル。二項対立（A対非A）と矛盾（A対反A）の四極から物語・テキストの深層意味構造を図示する。", "https://en.wikipedia.org/wiki/Semiotic_square", 1966),
    ("ナラトロジー", "Narratology", "Western_Europe", "文学批評理論", "ジュネット（1972）・プリンス・チャトマンらが体系化した物語の形式的研究。物語言説・物語内容・語り手・焦点化・時間を分析カテゴリとする。", "https://en.wikipedia.org/wiki/Narratology", 1966),
    ("焦点化", "Focalization", "Western_Europe", "文学批評理論", "ジュネット（1972）が提唱した語り論の概念。「誰が語るか」（語り手）と「誰の視点から見るか」（焦点子）を区別することで視点分析を精緻化した。", "https://en.wikipedia.org/wiki/Focalization", 1972),
    ("語り手論", "Narrative Theory", "Global_Synthesis", "文学批評理論", "フィクション・ノンフィクション・映画・デジタルメディアにまたがる語り（ナラティブ）の構造と機能を研究する学際的分野。", "https://en.wikipedia.org/wiki/Narrative", 1960),
    ("ダイエジェシス", "Diegesis", "Western_Europe", "文学批評理論", "古代ギリシャのプラトン（模倣/説話の区別）に由来し、ジュネット（1972）が近代的に定義した概念。物語世界内の出来事・世界を指す。", "https://en.wikipedia.org/wiki/Diegesis", 1972),
    ("受容美学", "Reception Aesthetics", "Western_Europe", "文学批評理論", "ヤウス（1967）・イーザーが創始したコンスタンツ学派の文学理論。意味はテキストと読者の相互作用によって生成され、期待の地平が解釈を規定するとする。", "https://en.wikipedia.org/wiki/Reception_theory", 1967),
    ("期待の地平", "Horizon of Expectations", "Western_Europe", "文学批評理論", "ヤウス（1967）が提唱した受容美学の中心概念。読者が作品に抱く先行的な期待構造。その充足・裏切りが審美的経験の質を決める。", "https://en.wikipedia.org/wiki/Horizon_of_expectations", 1967),
    ("テクストとしての読者反応", "Reader-Response Theory", "North_America", "文学批評理論", "フィッシュ（1980）・カラー・スタンリーらが発展させた批評理論。意味はテキストに内在せず、解釈共同体の読者の実践によって生産されるとする。", "https://en.wikipedia.org/wiki/Reader-response_criticism", 1960),
    ("解釈共同体", "Interpretive Community", "North_America", "文学批評理論", "フィッシュ（1980）が提唱した概念。共有された読書慣行・前提を持つ読者集団が、一致した解釈を産出するコミュニティ。", "https://en.wikipedia.org/wiki/Interpretive_community", 1980),
    ("デコンストラクション", "Deconstruction", "Western_Europe", "文学批評理論", "デリダ（1967）が哲学・文学テキストに適用した読解戦略。テキスト内の優位性の階層と自己矛盾を指摘し、確定的な意味を解体する。", "https://en.wikipedia.org/wiki/Deconstruction", 1967),
    ("テクストの外はない", "There is Nothing Outside the Text", "Western_Europe", "文学批評理論", "デリダ『グラマトロジー』（1967）の命題（il n'y a pas de hors-texte）。テキストを超えた外部的現実への直接アクセスは不可能であるという脱構築の中心テーゼ。", "https://en.wikipedia.org/wiki/There_is_nothing_outside_the_text", 1967),
    ("ポスト構造主義文学理論", "Post-Structuralist Literary Theory", "Western_Europe", "文学批評理論", "デリダ・バルト・フーコー・ラカンらが提供した文学テキスト分析の枠組み。意味の固定性・主体の一元性・権力と言語の関係を問題化する。", "https://en.wikipedia.org/wiki/Post-structuralism", 1968),
    ("著者の死", "Death of the Author", "Western_Europe", "文学批評理論", "バルト（1968）のエッセイが提唱した概念。テキストの意味は著者の意図に帰属せず、読者の実践によって生産されるという主張。", "https://en.wikipedia.org/wiki/The_Death_of_the_Author", 1968),
    ("言説とテクスト", "Discourse and Text", "Western_Europe", "文学批評理論", "フーコー（1969）の言説論をテキスト分析に応用する枠組み。何が言いうるか・誰が語れるかを規定する権力/知の体制が言説を構成するとする。", "https://en.wikipedia.org/wiki/Discourse", 1969),
    ("マルクス主義文学批評", "Marxist Literary Criticism", "Global_Synthesis", "文学批評理論", "ルカーチ・アルチュセール・イーグルトン・ジェイムソンらが展開した批評。文学と社会的生産様式・イデオロギー・階級の関係を分析する。", "https://en.wikipedia.org/wiki/Marxist_literary_criticism", 1920),
    ("イデオロギーと文学", "Ideology and Literature", "Global_Synthesis", "文学批評理論", "アルチュセール（1970）の国家イデオロギー装置論をベースに、文学がイデオロギーの再生産・抵抗に果たす機能を分析する批評方法。", "https://en.wikipedia.org/wiki/Ideology", 1970),
    ("文化的唯物論", "Cultural Materialism", "Western_Europe", "文学批評理論", "ウィリアムズ（1977）が提唱したマルクス主義文化論。支配的・残存的・新興的な文化の三項を用いてテキストの政治的機能を分析する。", "https://en.wikipedia.org/wiki/Cultural_materialism_(cultural_studies)", 1977),
    ("新歴史主義", "New Historicism", "North_America", "文学批評理論", "グリーンブラット（1980年代）が創始した文学批評。文化の詩学として、文学テキストと非文学テキストの相互循環を歴史的文脈で分析する。", "https://en.wikipedia.org/wiki/New_Historicism", 1980),
    ("フェミニスト文学批評", "Feminist Literary Criticism", "North_America", "文学批評理論", "ウルフ・ボーヴォワール・ショーウォルター・シクスーらが発展させた批評。文学における女性の表象・女性の書き方・男性中心的カノンへの批判を展開する。", "https://en.wikipedia.org/wiki/Feminist_literary_criticism", 1970),
    ("ジャイノクリティシズム", "Gynocriticism", "North_America", "文学批評理論", "ショーウォルター（1979）が提唱した女性文学研究の方法。女性の書くこと・女性作家のキャノン・女性文学の伝統を主体的に研究する。", "https://en.wikipedia.org/wiki/Gynocriticism", 1979),
    ("エクリチュール・フェミニン", "Écriture Féminine", "Western_Europe", "文学批評理論", "シクスー（1975）が提唱した「女性的書き方」の概念。父権的言語秩序への抵抗として、身体・リズム・流動性に基づく書き方を称揚する。", "https://en.wikipedia.org/wiki/%C3%89criture_f%C3%A9minine", 1975),
    ("クィア理論と文学", "Queer Theory and Literature", "North_America", "文学批評理論", "バトラー（1990）・セジウィック（1990）らが確立した批評。性・ジェンダー・欲望の正常/異常の区分を脱構築し、文学テキストの規範的性秩序を分析する。", "https://en.wikipedia.org/wiki/Queer_theory", 1990),
    ("ポストコロニアル文学批評", "Postcolonial Literary Criticism", "Global_Synthesis", "文学批評理論", "サイード（1978）・スピヴァク・バーバーらが発展させた批評。植民地支配と帝国主義が文学・文化・表象に与えた影響を批判的に分析する。", "https://en.wikipedia.org/wiki/Postcolonial_literature", 1978),
    ("オリエンタリズム", "Orientalism", "West_Asia_North_Africa", "文学批評理論", "サイード（1978）が概念化した分析概念。西洋が「東洋」を支配・管理・生産するための知識の体系として定義し、帝国主義と表象の関係を批判した。", "https://en.wikipedia.org/wiki/Orientalism", 1978),
    ("世界文学", "World Literature", "Global_Synthesis", "文学批評理論", "ゲーテ（Weltliteratur）に由来し、ダムロッシュ（2003）・モレッティらが現代的に理論化した概念。国民文学を超えた世界的な文学の流通・翻訳・比較を研究する。", "https://en.wikipedia.org/wiki/World_literature", 1827),
    ("比較文学", "Comparative Literature", "Global_Synthesis", "文学批評理論", "複数の国民文学・言語圏にわたって文学を比較研究する学問分野。影響・受容・翻訳・文学的間テクスト性・ジャンルの比較が主要方法論。", "https://en.wikipedia.org/wiki/Comparative_literature", 1830),
    ("間テクスト性", "Intertextuality", "Western_Europe", "文学批評理論", "クリステヴァ（1966）がバフチンの対話性理論を発展させた概念。すべてのテキストは先行テキストへの引用・変形・反応として成立するという主張。", "https://en.wikipedia.org/wiki/Intertextuality", 1966),
    ("バフチンの対話性", "Bakhtinian Dialogism", "Western_Europe", "文学批評理論", "バフチン（1929-1963）が理論化した言語・文学の根本的性質。全ての言語表現は他者の声との対話的関係の中に成立するという理論。", "https://en.wikipedia.org/wiki/Dialogism", 1929),
    ("ポリフォニー小説", "Polyphonic Novel", "Western_Europe", "文学批評理論", "バフチン（1929）がドストエフスキー分析で提唱した小説形式。著者の統一的声ではなく、複数の独立した意識・声が共存する対話的構造を持つ小説。", "https://en.wikipedia.org/wiki/Polyphony_(literature)", 1929),
    ("カーニバル理論", "Carnivalesque Theory", "Western_Europe", "文学批評理論", "バフチン（1965）がラブレー分析で展開した概念。祭りと笑いが社会的ヒエラルキーを転倒させる解放的機能を持つという文化・文学理論。", "https://en.wikipedia.org/wiki/Carnivalesque", 1965),
    ("物語論的構造主義", "Structural Narratology", "Western_Europe", "文学批評理論", "プロップ（1928）の民話形態論を起点にしたトドロフ・ジュネット・グレマスらの物語形式分析。物語の深層文法・機能・変換規則を抽出する。", "https://en.wikipedia.org/wiki/Structural_narratology", 1928),
    ("プロップの機能", "Propp's Morphology of the Folktale", "Western_Europe", "文学批評理論", "プロップ（1928）がロシア民話100篇を分析して発見した31の物語機能と7つの行動圏。構造主義物語論の出発点となった。", "https://en.wikipedia.org/wiki/Vladimir_Propp", 1928),
    ("エコクリティシズム", "Ecocriticism", "North_America", "文学批評理論", "グロットフェルティ（1996）が確立した文学批評。文学と物理的環境の関係を研究し、自然・場所・非人間的存在の表象を分析する。", "https://en.wikipedia.org/wiki/Ecocriticism", 1989),
    ("物質的エコクリティシズム", "Material Ecocriticism", "North_America", "文学批評理論", "アラモ＆ヘクマンが展開した新物質主義的生態批評。テキストにおける物質の主体性・人間/非人間の絡み合いを分析する。", "https://en.wikipedia.org/wiki/Ecocriticism", 2008),
    ("アニマルスタディーズと文学", "Animal Studies and Literature", "Global_Synthesis", "文学批評理論", "文学における動物の表象・人間/動物の境界の構築・スペシーシズム批判を研究する分野。ヴォルフ・デリダ・コーツィーの作品論が理論的起点。", "https://en.wikipedia.org/wiki/Animal_studies", 2000),
    ("ポストヒューマン文学批評", "Posthumanist Literary Criticism", "North_America", "文学批評理論", "ハラウェイ・ブライドッティ（2013）らの人間概念の脱中心化を文学テキスト分析に適用する批評。人間/機械/動物/自然の境界の構築を批判的に読む。", "https://en.wikipedia.org/wiki/Posthumanism", 1990),
    ("アフリカ文学批評", "African Literary Criticism", "Sub_Saharan_Africa", "文学批評理論", "アチェベ・チヌア（1958「崩れゆく絆」）に始まり、ムゴ・カベー・グベアダムシらが発展させた批評。アフリカ独自の文学的伝統・口承と文字の関係・植民地言語問題を論じる。", "https://en.wikipedia.org/wiki/African_literature", 1958),
    ("ネグリチュード", "Négritude", "Sub_Saharan_Africa", "文学批評理論", "セゼール・サンゴール・ダマスが1930年代パリで展開した文学・政治運動。黒人性のアイデンティティを肯定的に再評価し、植民地支配への抵抗を表現した。", "https://en.wikipedia.org/wiki/N%C3%A9gritude", 1930),
    ("ラテンアメリカ文学批評", "Latin American Literary Criticism", "Latin_America", "文学批評理論", "マジックリアリズム（ガルシア・マルケス）・ラテンアメリカ・ブーム・「クルーン」文学論など独自の文学的伝統と批評を生み出した地域文学研究。", "https://en.wikipedia.org/wiki/Latin_American_literature", 1940),
    ("マジックリアリズム批評", "Magic Realism Criticism", "Latin_America", "文学批評理論", "ガルシア・マルケス・カルペンティエル・ルルフォらの文学を起点とした批評概念。現実と幻想を等価に扱う物語手法と、その脱植民地的機能を論じる。", "https://en.wikipedia.org/wiki/Magic_realism", 1925),
    ("ハーレム・ルネサンス批評", "Harlem Renaissance Literary Criticism", "North_America", "文学批評理論", "1920年代のアフリカ系アメリカ人文化運動（ヒューズ・ハーストン・マッケイ）の文学批評。黒人文化の自律的価値と人種・階級・ジェンダーの交差を研究する。", "https://en.wikipedia.org/wiki/Harlem_Renaissance", 1920),
    ("アフリカ系アメリカ文学批評", "African American Literary Criticism", "North_America", "文学批評理論", "ゲイツ（1988「シグニファイング・モンキー」）・フックス・モリスンらが展開した批評。アフリカ系アメリカ人の口承伝統・修辞学・ジャンルの革新を理論化した。", "https://en.wikipedia.org/wiki/African-American_literature", 1970),
    ("東アジア文学批評", "East Asian Literary Criticism", "East_Asia", "文学批評理論", "中国・日本・韓国の古典文学批評伝統と近代以降の文学理論の交差を研究する分野。漢詩批評（詩話）・日本の物語論・韓国の民衆文学論が含まれる。", "https://en.wikipedia.org/wiki/East_Asian_literature", 800),
    ("詩話", "Shihua (Poetic Discourse)", "East_Asia", "文学批評理論", "中国・日本・韓国で発展した詩についての批評的議論の形式。エピグラム・逸話・批評的覚書の形で詩学的評価を伝達する伝統的批評様式。", "https://en.wikipedia.org/wiki/Shihua", 1000),
    ("もののあわれ", "Mono no Aware", "East_Asia", "文学批評理論", "本居宣長（1780年代）が源氏物語分析で定式化した日本の美的概念。事物の無常への感受性・哀感と美の交融を表す。日本文学批評の根幹概念。", "https://en.wikipedia.org/wiki/Mono_no_aware", 1780),
    ("幽玄", "Yūgen", "East_Asia", "文学批評理論", "中世日本の連歌・能楽の美的概念。言葉で言い表せない微妙な美しさ・深み・余情。藤原俊成・世阿弥が理論化した。", "https://en.wikipedia.org/wiki/Y%C5%ABgen", 1200),
    ("韓国民衆文学", "Minjung Literature", "East_Asia", "文学批評理論", "1970-80年代の韓国で発展した民衆（minjung＝被抑圧者）を主体とする文学運動・批評。軍事独裁への抵抗と社会変革を目指した。", "https://en.wikipedia.org/wiki/Minjung_movement", 1970),
    ("サンスクリット詩学", "Sanskrit Poetics (Alamkarashastra)", "South_Asia", "文学批評理論", "バラタ（ナーティヤシャーストラ、紀元前後）・アナンダヴァルダナ（ドヴァンヤーローカ、9世紀）らが確立したインド固有の詩学。ラサ（味わい）・ドヴァニ（響き）が中核概念。", "https://en.wikipedia.org/wiki/Sanskrit_literature", -200),
    ("ラサ理論", "Rasa Theory", "South_Asia", "文学批評理論", "バラタ（ナーティヤシャーストラ）が提唱し、アビナヴァグプタが発展させたインド美学・詩学の中核概念。9種の感情的本質（ラサ）が芸術体験を生む。", "https://en.wikipedia.org/wiki/Rasa_(aesthetics)", -200),
    ("アラビア文学批評", "Arabic Literary Criticism", "West_Asia_North_Africa", "文学批評理論", "クドゥマ・イブン・ジャアファル（10世紀）・イブン・ラシーク（11世紀）らが発展させたアラビア詩学。レトリック・修辞・詩の評価基準を体系化した。", "https://en.wikipedia.org/wiki/Arabic_literature", 750),
    ("マカーマ文学", "Maqama Literature", "West_Asia_North_Africa", "文学批評理論", "ハマダーニー（10世紀）が創始したアラビア語の韻文散文の文学ジャンル。洗練された修辞と機知を特徴とし、後のスペイン語・ヘブライ語文学にも影響した。", "https://en.wikipedia.org/wiki/Maqama", 980),
    ("スワヒリ文学", "Swahili Literature", "Sub_Saharan_Africa", "文学批評理論", "東アフリカのスワヒリ語文学の伝統。テンジ（長編叙事詩）・ウテンジ（宗教詩）・ンゴマ（音楽詩）が主要ジャンル。アラビア語とアフリカ口承伝統の融合。", "https://en.wikipedia.org/wiki/Swahili_literature", 1400),
    ("グリオ文学", "Griot Oral Literature", "Sub_Saharan_Africa", "文学批評理論", "西アフリカの語り部（グリオ）が担う口承文学の伝統。歴史・系譜・称賛詩・物語を歌と語りで伝える。マリンケ・ウォロフなど多くの民族で受け継がれる。", "https://en.wikipedia.org/wiki/Griot", 1300),
    ("モダニズム文学批評", "Modernist Literary Criticism", "Western_Europe", "文学批評理論", "エリオット・パウンド・ウルフ・ジョイスらの文学実験を理論化した批評。意識の流れ・非線形時間・断片化・内的独白が主要技法として分析された。", "https://en.wikipedia.org/wiki/Modernism", 1890),
    ("意識の流れ", "Stream of Consciousness", "Western_Europe", "文学批評理論", "ジェイムズ（1890）が心理学的に提唱し、ジョイス・ウルフ・フォークナーが文学技法として発展させた概念。人物の連続する思考・感覚・記憶の内的流れを描く。", "https://en.wikipedia.org/wiki/Stream_of_consciousness", 1890),
    ("ポストモダン文学批評", "Postmodern Literary Criticism", "North_America", "文学批評理論", "ジャーメソン・ハッサン・マクヘイルらが展開した批評。メタフィクション・パスティーシュ・パロディ・歴史との遊戯・自己言及性がポストモダン文学の特徴として分析される。", "https://en.wikipedia.org/wiki/Postmodern_literature", 1960),
    ("メタフィクション", "Metafiction", "North_America", "文学批評理論", "ウォー（1984）が体系化した概念。フィクションであることを自己意識的に問いながら書く文学の形式。リアリズムの虚構性を暴露し、語りの条件を主題化する。", "https://en.wikipedia.org/wiki/Metafiction", 1960),
    ("精神分析批評", "Psychoanalytic Literary Criticism", "Western_Europe", "文学批評理論", "フロイト・ユング・ラカンの精神分析理論を文学テキスト分析に適用する批評。抑圧・象徴・無意識・欲動・镜像段階が分析概念として用いられる。", "https://en.wikipedia.org/wiki/Psychoanalytic_literary_criticism", 1900),
    ("神話批評・アーキタイプ批評", "Myth Criticism and Archetypal Criticism", "Global_Synthesis", "文学批評理論", "フライ（1957「批評の解剖」）が体系化した批評。文学テキストを神話的パターン（英雄の旅・死と再生）とユング的元型から分析する。", "https://en.wikipedia.org/wiki/Archetypal_literary_criticism", 1957),
    ("ジャンル理論", "Genre Theory", "Global_Synthesis", "文学批評理論", "ジャンルを慣習体系・社会的行為・認知的プロトタイプとして分析する文学理論。バフチン・ファウラー・ミラー（1984）が主要理論家。", "https://en.wikipedia.org/wiki/Genre", 1970),
    ("古典的レトリック", "Classical Rhetoric", "Western_Europe", "文学批評理論", "アリストテレス（『弁論術』BC335）・キケロ・クインティリアヌスが体系化した説得の技術。発見・配置・表現・記憶・発表の五部と演説三様式（説示・審議・賞讃）。", "https://en.wikipedia.org/wiki/Classical_rhetoric", -335),
    ("修辞的転換", "Rhetorical Tropes", "Western_Europe", "文学批評理論", "比喩・換喩・提喩・誇張などの修辞的転換（トロポス）。ホワイト（1973）はこれらを歴史叙述のメタファー的構造として再解釈した。", "https://en.wikipedia.org/wiki/Trope_(literature)", -335),
    ("物語の倫理", "Ethics of Narrative", "Global_Synthesis", "文学批評理論", "ブース（1988「語りの修辞学」）・ヌスバウム（「詩的正義」1995）らが論じた文学の倫理的次元。物語が読者の道徳的感受性を教育する機能を研究する。", "https://en.wikipedia.org/wiki/Narrative_ethics", 1988),
    ("障害研究と文学", "Disability Studies and Literature", "North_America", "文学批評理論", "デイビス（1997）・ミッチェル＆スナイダーらが発展させた批評。文学における障害の表象・正常性の構築・障害者の主体的語りを研究する。", "https://en.wikipedia.org/wiki/Disability_studies", 1997),
    # 追加言語学 (40件) — 批判的・応用系
    ("言語景観", "Linguistic Landscape", "Global_Synthesis", "言語学", "ランドリー＆ブーリス（1997）が定義した研究分野。公共空間の標識・看板・落書きなどに表れる言語使用のパターンと意味を研究する。", "https://en.wikipedia.org/wiki/Linguistic_landscape", 1997),
    ("言語エスノグラフィー", "Linguistic Ethnography", "Western_Europe", "言語学", "言語と社会的実践の関係を民族誌的方法で研究する分野。ブロック（2007）らが理論化し、ロンドン学派の言語研究と結合した。", "https://en.wikipedia.org/wiki/Linguistic_ethnography", 2000),
    ("メトロリンガリズム", "Metrolingualism", "Global_Synthesis", "言語学", "オタスエビー＆ペニークック（2010）が提唱した概念。都市の多様な言語資源を流動的に組み合わせる実践を記述する。", "https://en.wikipedia.org/wiki/Metrolingualism", 2010),
    ("超多様性と言語", "Superdiversity and Language", "Western_Europe", "言語学", "ヴァーヴェルケ（2007）が提唱した超多様性概念を言語研究に適用したもの。移民・グローバル化による複雑な言語資源の変化を分析する。", "https://en.wikipedia.org/wiki/Superdiversity", 2007),
    ("トランスランゲージング", "Translanguaging", "Global_Synthesis", "言語学", "ガルシア（2009）・ウェイ（2011）が理論化した概念。バイリンガルが複数言語をシームレスに駆使する実践を個別言語の混合ではなく統一的レパートリーの展開として捉える。", "https://en.wikipedia.org/wiki/Translanguaging", 2009),
    ("言語ナショナリズム", "Linguistic Nationalism", "Global_Synthesis", "言語学", "国民的アイデンティティの形成に言語が果たす役割を研究する分野。標準語政策・少数言語の周縁化・言語コミュニティの政治的動員を分析する。", "https://en.wikipedia.org/wiki/Linguistic_nationalism", 1770),
    ("手話言語学", "Sign Language Linguistics", "Global_Synthesis", "言語学", "アメリカ手話（ASL）・日本手話など視覚・運動チャンネルを用いる自然言語の構造を研究する分野。スタコー（1960）が手話の言語的地位を確立した。", "https://en.wikipedia.org/wiki/Sign_language", 1960),
    ("語用論的発展", "Pragmatic Development", "Global_Synthesis", "言語学", "子どもが会話の含意・丁寧さ・間接発話行為・語用論的原則を習得する過程を研究する分野。第一言語・第二言語習得研究の重要領域。", "https://en.wikipedia.org/wiki/Pragmatics", 1980),
    ("コードスイッチング研究", "Code-Switching Research", "Global_Synthesis", "言語学", "バイリンガルが会話内で複数言語間を切り替える現象の研究。マイヤーズ・スコットン（1993）のマトリクス言語枠組み・グンペルツの会話的コードスイッチングが主要理論。", "https://en.wikipedia.org/wiki/Code-switching", 1970),
    ("否定の統語論", "Negation in Syntax", "Global_Synthesis", "言語学", "否定の表現形式と統語構造の関係を研究する分野。否定一致・否定句・否定極性項目が主要分析対象。ポロック（1989）が主要な統語論的分析を提示した。", "https://en.wikipedia.org/wiki/Negation", 1989),
    ("エルゴン言語学", "Ergative Languages Research", "Global_Synthesis", "言語学", "バスク語・チェチェン語・グルジア語など絶対格-能格言語の構造を研究する分野。主格-対格言語とは異なる格組み・動詞一致パターンを分析する。", "https://en.wikipedia.org/wiki/Ergative%E2%80%93absolutive_alignment", 1970),
    ("SOV言語の統語特性", "SOV Language Typology", "Global_Synthesis", "言語学", "日本語・韓国語・トルコ語など述語末尾の言語に見られる統語特性（後置詞・関係節前置・OV語順）を類型論的に研究する。グリーンバーグの含意的普遍性が基礎。", "https://en.wikipedia.org/wiki/Subject%E2%80%93object%E2%80%93verb", 1963),
    ("モーラと音節", "Mora and Syllable", "East_Asia", "言語学", "日本語などモーラ言語の音韻単位研究。音節とモーラの区別・モーラ数に基づくリズム・音調の計量が研究対象となる。", "https://en.wikipedia.org/wiki/Mora_(linguistics)", 1970),
    ("ピッチアクセント言語学", "Pitch Accent Linguistics", "East_Asia", "言語学", "日本語・スウェーデン語・セルビア語など音の高低パターンが語彙を区別するが声調言語ほど精密でない言語の音韻論的研究。", "https://en.wikipedia.org/wiki/Pitch_accent", 1970),
    ("敬語研究", "Honorific Language Research", "East_Asia", "言語学", "日本語・韓国語・ジャワ語など社会的関係（上下・親疎・内外）が文法形式に反映する言語の研究。社会言語学・語用論・文法論が交差する領域。", "https://en.wikipedia.org/wiki/Honorifics_(linguistics)", 1960),
    ("アルタイ語族論争", "Altaic Language Debate", "East_Asia", "言語学", "日本語・韓国語・トルコ語・モンゴル語・ツングース語の同一起源論（アルタイ仮説）を巡る論争。多くの現代言語学者は否定的だが、語彙・類型論的類似は継続的研究対象。", "https://en.wikipedia.org/wiki/Altaic_languages", 1730),
    ("ドラヴィダ語族", "Dravidian Languages", "South_Asia", "言語学", "タミル語・テルグ語・カンナダ語・マラヤーラム語など主に南インドで話される語族。インダス文明との関係を巡る仮説が注目を集めている。", "https://en.wikipedia.org/wiki/Dravidian_languages", 1810),
    ("バントゥー語族", "Bantu Languages", "Sub_Saharan_Africa", "言語学", "スワヒリ語・ズールー語・ショナ語など約500言語からなるアフリカ最大の語族。名詞クラスシステム・バントゥー拡散の歴史が主要研究テーマ。", "https://en.wikipedia.org/wiki/Bantu_languages", 1840),
    ("ナイル・サハラ語族", "Nilo-Saharan Languages", "Sub_Saharan_Africa", "言語学", "東・中央アフリカに分布する多様な語族。その統一性は論争中だが、ロウランド語・ソンガイ語・サハラ語などを含む。", "https://en.wikipedia.org/wiki/Nilo-Saharan_languages", 1963),
    ("言語アーカイブ", "Language Documentation", "Global_Synthesis", "言語学", "消滅危機言語の音声・文法・語彙・テキストを体系的に記録・保存する実践的分野。ヒンメルマン（1998）が方法論を体系化した。", "https://en.wikipedia.org/wiki/Language_documentation", 1998),
    ("系統発生的言語学", "Phylogenetic Linguistics", "Global_Synthesis", "言語学", "生物の系統発生分析手法（最大節約法・最尤法・ベイズ法）を語族・言語拡散の歴史的再構成に応用する学際的分野。", "https://en.wikipedia.org/wiki/Computational_phylogenetics", 2003),
    ("語彙統計学", "Lexicostatistics", "Global_Synthesis", "言語学", "スワデシュ（1952）が開発した語彙の保存率から言語分岐年代を推定する方法。グロットクロノロジーとも呼ばれる。", "https://en.wikipedia.org/wiki/Lexicostatistics", 1952),
    ("音響音声学", "Acoustic Phonetics", "Global_Synthesis", "言語学", "言語音の物理的性質（周波数・振幅・時間）を音響分析装置で研究する分野。フォルマント・ピッチ・F0が主要分析対象。", "https://en.wikipedia.org/wiki/Acoustic_phonetics", 1950),
    ("調音音声学", "Articulatory Phonetics", "Global_Synthesis", "言語学", "声道の動き（舌・唇・軟口蓋・声門）と産出される音声の関係を研究する分野。IPA（国際音声字母）が調音記述の標準体系を提供する。", "https://en.wikipedia.org/wiki/Articulatory_phonetics", 1877),
    ("知覚音声学", "Perceptual Phonetics", "Global_Synthesis", "言語学", "話者がどのように音声を知覚・カテゴリー化するかを心理物理学的手法で研究する分野。語音知覚の文脈効果・マガーク効果が主要研究テーマ。", "https://en.wikipedia.org/wiki/Auditory_phonetics", 1970),
    ("言語の起源", "Language Origins", "Global_Synthesis", "言語学", "人類における言語の進化的起源を研究する学際分野。遺伝学・神経科学・比較認知科学・古人類学が統合される。ハウザー・チョムスキー・フィッチ（2002）の枠組みが影響力を持つ。", "https://en.wikipedia.org/wiki/Origin_of_language", 1990),
    ("言語とアイデンティティ", "Language and Identity", "Global_Synthesis", "言語学", "言語使用がアイデンティティの構築・維持・変容に果たす役割を研究する分野。ノートン（2000）・ブロック・バロニらが主要理論家。", "https://en.wikipedia.org/wiki/Language_and_identity", 1990),
    ("言語ポリシー・プランニング", "Language Policy and Planning", "Global_Synthesis", "言語学", "国家・地域・教育機関における言語の公的規制と計画（地位計画・コーパス計画・習得計画）を研究する分野。ハウゲン（1966）が定式化した。", "https://en.wikipedia.org/wiki/Language_policy", 1966),
    ("教室談話", "Classroom Discourse", "Global_Synthesis", "言語学", "教室における教師・生徒の言語的相互作用パターン（IRF構造・足場作り・言語学習機会）を研究する応用言語学の分野。", "https://en.wikipedia.org/wiki/Classroom_discourse", 1975),
    ("書き言葉と話し言葉", "Written vs Spoken Language", "Global_Synthesis", "言語学", "ビーバー（1988）・シャー（1982）が分析した書記言語と口語言語の構造的・機能的差異。テキスト類型論・言語的コンプレキシティが主要分析概念。", "https://en.wikipedia.org/wiki/Written_language", 1980),
    ("形態論", "Morphology (Linguistics)", "Global_Synthesis", "言語学", "語の内部構造（語根・接辞・屈折・派生）を研究する言語学の分野。孤立語・膠着語・融合語・抱合語の類型論的分類が重要な枠組み。", "https://en.wikipedia.org/wiki/Morphology_(linguistics)", 1880),
    ("継承語", "Heritage Language", "Global_Synthesis", "言語学", "移民コミュニティにおいて家庭で習得されるが、社会的主流言語に支配される言語。ポリンスキー（2018）らが認知的・社会的側面を研究している。", "https://en.wikipedia.org/wiki/Heritage_language", 2001),
    ("外来語の音韻適応", "Phonological Adaptation of Loanwords", "East_Asia", "言語学", "借用語が受け入れ言語の音韻体系に適応するプロセス。日本語のカタカナ化・英語への音韻借用パターンが典型的研究対象。", "https://en.wikipedia.org/wiki/Loanword", 1960),
    ("語形成", "Word Formation", "Global_Synthesis", "言語学", "派生・複合・転換・略語・ブレンディングなど新語が生成される形態論的プロセス。リーバー（2009）が体系的な形態論的分析を提供した。", "https://en.wikipedia.org/wiki/Word_formation", 1970),
]

def insert_batch(concepts_list):
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()
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
print(f"Batch 3 (文学批評+言語学補完): inserted={inserted}, skipped={skipped}")
conn = sqlite3.connect(DB)
total = conn.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
lit = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='文学批評理論'").fetchone()[0]
ling = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='言語学'").fetchone()[0]
conn.close()
print(f"総件数: {total}, 文学批評理論: {lit}, 言語学: {ling}")
