"""DUA Wave A2 Batch 15 — 哲学・言語学・歴史学・宗教学・古典学・美学 新規概念 (~400 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def uid():
    return "dua_" + uuid.uuid4().hex[:12]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()

# 新規概念のみ — 既存スキップを最小化するため既出でない専門的概念を選定
records = [
    # ===== 分析哲学・心の哲学 (新規) (~50) =====
    ("物理主義", "Physicalism", "すべての存在は物理的であるとする形而上学的立場。トークン物理主義とタイプ物理主義の区別、心身問題への適用、スーパーヴィーニエンス論が中心的議論。", "哲学・倫理学", "North_America", 1950, "https://en.wikipedia.org/wiki/Physicalism"),
    ("機能主義（心の哲学）", "Functionalism in Philosophy of Mind", "心的状態はその機能的役割によって定義されるという心身論の立場。パトナム、フォドーが代表的論者。チューリングマシンや計算主義との連動が特徴的。", "哲学・倫理学", "North_America", 1960, "https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)"),
    ("表象主義（心の哲学）", "Representationalism in Philosophy of Mind", "心的内容は世界の表象であるとする理論。ドレツキ、ミリカン、フォドーが代表的論者。知覚・信念・意図の表象的内容を分析する。", "哲学・倫理学", "North_America", 1988, "https://en.wikipedia.org/wiki/Representationism"),
    ("直接実在論（知覚論）", "Direct Realism", "知覚は外的世界の対象を直接知覚するとする認識論的立場。感覚与件を介在物とする間接実在論への対案。マクドウェル、プライスが代表的論者。", "哲学・倫理学", "Western_Europe", 1910, "https://en.wikipedia.org/wiki/Direct_and_indirect_realism"),
    ("意図性（志向性）", "Intentionality", "心的状態が何かについてある、何かに向かうという性質。ブレンターノが現象学への架け橋として論じ、フッサール・サールが体系化。命題態度の分析の基礎概念。", "哲学・倫理学", "Western_Europe", 1874, "https://en.wikipedia.org/wiki/Intentionality"),
    ("内容の広義・狭義区別", "Wide Content and Narrow Content", "心的内容が外部環境（広義内容）に依存するか内部状態のみ（狭義内容）に依存するかの区別。パトナムの「双子の地球」思考実験が発端。バーゲが外部主義を発展させた。", "哲学・倫理学", "North_America", 1975, "https://en.wikipedia.org/wiki/Semantic_externalism"),
    ("行為論", "Action Theory", "人間の行為とは何か、意図・欲求・信念がどのように行為を引き起こすかを分析する哲学の分野。アンスコム、ダヴィドソンが代表的論者。自由意志論と連動する。", "哲学・倫理学", "Western_Europe", 1957, "https://en.wikipedia.org/wiki/Action_theory_(philosophy)"),
    ("実用主義（古典）", "Classical Pragmatism", "パース、ジェームズ、デューイが発展させたアメリカの哲学的伝統。概念の意味はその実際的結果によって決まるとし、真理を有用性・検証可能性と連動させる。", "哲学・倫理学", "North_America", 1878, "https://en.wikipedia.org/wiki/Pragmatism"),
    ("新プラグマティズム", "Neopragmatism", "ローティ、ブランダム、ミサックが代表的論者。古典的プラグマティズムを分析哲学の文脈で再解釈する20世紀後半の哲学的潮流。表象主義批判と推論主義が特徴。", "哲学・倫理学", "North_America", 1979, "https://en.wikipedia.org/wiki/Neopragmatism"),
    ("推論主義", "Inferentialism", "ブランダムが提唱した意味の理論。言語表現の意味は推論的役割によって構成されるとし、表象主義的意味論に対抗する。ヘーゲルのカント解釈から影響を受ける。", "哲学・倫理学", "North_America", 1994, "https://en.wikipedia.org/wiki/Inferentialism"),
    ("分析存在論", "Analytic Ontology", "分析哲学の手法を用いた存在論の探求。存在・部分・量・本質・依存・基底関係等の概念の分析的明確化を目指す。サイダー、ハーレ、ファインが代表的論者。", "哲学・倫理学", "North_America", 1990, "https://en.wikipedia.org/wiki/Ontology"),
    ("メタ形而上学", "Metametaphysics", "形而上学的問いの意義・方法・認識論を問うメタレベルの探求。チャルマーズ、ハーレ、サイダーが代表的論者。形而上学的問いが本当の問いかどうかを問う立場も含む。", "哲学・倫理学", "North_America", 2009, "https://en.wikipedia.org/wiki/Metametaphysics"),
    ("規範性の哲学", "Philosophy of Normativity", "規則・規範・理由に関する哲学的問い。規範的事実の存在論（実在論対反実在論）、理由の構造、意図と理由の関係を論じる。スキャンロン、コリガン、パーフィットが代表。", "哲学・倫理学", "Western_Europe", 1990, "https://en.wikipedia.org/wiki/Normativity"),
    ("実験哲学", "Experimental Philosophy", "哲学的問いへの人々の直観を実証的に調査する哲学研究の新手法。知識・道徳・自由意志・概念に関する一般人の判断を実験的に収集し哲学理論の検討に用いる。", "哲学・倫理学", "North_America", 2001, "https://en.wikipedia.org/wiki/Experimental_philosophy"),
    ("哲学的懐疑主義", "Philosophical Skepticism", "知識の可能性・範囲・正当化を疑う哲学的立場。デカルトの方法的懐疑、外界懐疑論、他者心問題、帰納の問題が主要な形態。懐疑論への応答として認識論の様々な立場が発展した。", "哲学・倫理学", "Western_Europe", -300, "https://en.wikipedia.org/wiki/Philosophical_skepticism"),
    ("数学の哲学", "Philosophy of Mathematics", "数学的対象の存在・数学的真理の性質・数学的知識の正当化を問う。プラトン主義・形式主義（ヒルベルト）・直観主義（ブラウワー）・フィクション主義が主要立場。", "哲学・倫理学", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Philosophy_of_mathematics"),
    ("科学的説明論", "Scientific Explanation", "科学的説明とは何かを分析する科学哲学の中心的問い。ヘンペルの被覆法則モデル、統一論（フリードマン、キッチャー）、因果的メカニズム論が主要アプローチ。", "哲学・倫理学", "North_America", 1948, "https://en.wikipedia.org/wiki/Scientific_explanation"),
    ("理論の構造と確証", "Theory Structure and Confirmation", "科学理論の論理的構造と観察証拠による確証の関係を論じる科学哲学の分野。ヘンペルの確証理論、ベイズ主義的確証論、クーン・ラカトシュ・ラウダンの歴史的アプローチが対話する。", "哲学・倫理学", "North_America", 1945, "https://en.wikipedia.org/wiki/Confirmation_holism"),
    ("決定論と科学", "Determinism in Science", "物理世界が完全に決定されているかという問いと量子力学的非決定性の関係を論じる。ラプラスの悪魔から量子論・カオス理論まで、決定論の哲学的含意を探る。", "哲学・倫理学", "Western_Europe", 1814, "https://en.wikipedia.org/wiki/Determinism"),
    ("真理の理論", "Theories of Truth", "命題・文・信念の真理の性質を分析する哲学的探求。対応説・整合説・プラグマティズム的真理論・縮小論（デフレーショニズム）が主要立場。クリプキの固定指示子論も関連する。", "哲学・倫理学", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Truth"),
    ("意味の使用理論", "Use Theory of Meaning", "後期ウィトゲンシュタインの言語論。語の意味はその使用であるとし、言語ゲームと生活形式の概念によって意味論を再構成する。哲学的混乱は文法の誤用から生じるとする。", "哲学・倫理学", "Western_Europe", 1953, "https://en.wikipedia.org/wiki/Use-mention_distinction"),
    # ===== 現象学・存在論 (新規) (~30) =====
    ("フランス現象学", "French Phenomenology", "フランスにおけるフッサール・ハイデガーの受容と独自発展。メルロ=ポンティの身体論、サルトルの実存主義現象学、レヴィナスの他者論、アンリの生の現象学が代表。", "哲学・倫理学", "Western_Europe", 1945, "https://en.wikipedia.org/wiki/Phenomenology_(philosophy)"),
    ("生の現象学", "Phenomenology of Life", "ミシェル・アンリが展開した哲学的立場。生の自己顕現（auto-affection）を現象性の根拠とし、フッサール以来の志向性中心の現象学を批判する。", "哲学・倫理学", "Western_Europe", 1963, "https://en.wikipedia.org/wiki/Michel_Henry"),
    ("解釈学的現象学", "Hermeneutical Phenomenology", "ハイデガー・ガダマー・リクールが展開した現象学と解釈学の統合。理解は先入見からなる地平を持ち、テキスト解釈は地平融合によって生じるとする。", "哲学・倫理学", "Western_Europe", 1927, "https://en.wikipedia.org/wiki/Hermeneutics"),
    ("存在論的差異", "Ontological Difference", "ハイデガーが強調した存在（Sein）と存在者（Seiendes）の根本的差異。形而上学の歴史が存在忘却の歴史であるという診断と連動し、基礎存在論の核心をなす。", "哲学・倫理学", "Western_Europe", 1927, "https://en.wikipedia.org/wiki/Ontological_difference"),
    ("現存在分析", "Dasein Analysis", "ハイデガーが展開した人間存在（現存在/Dasein）の存在論的分析。世界内存在・気分・了解・語り・時間性を軸に人間存在の構造を明らかにする。", "哲学・倫理学", "Western_Europe", 1927, "https://en.wikipedia.org/wiki/Dasein"),
    ("他者論（レヴィナス）", "Levinas's Philosophy of the Other", "エマニュエル・レヴィナスが展開した倫理的他者論。他者の顔（visage）が絶対的に超越し、私に無限の責任を課すとする。全体性に対する無限性の優位を論じる。", "哲学・倫理学", "Western_Europe", 1961, "https://en.wikipedia.org/wiki/Emmanuel_Levinas"),
    ("身体の哲学", "Philosophy of the Body", "メルロ=ポンティの身体論を中心に、身体が世界経験の基盤であることを論じる哲学的探求。身体図式、身体知、能動的身体の概念が中核。認知科学の身体化認知と連動する。", "哲学・倫理学", "Western_Europe", 1945, "https://en.wikipedia.org/wiki/Phenomenology_of_the_body"),
    ("技術哲学", "Philosophy of Technology", "技術の本質・意味・社会的役割を問う哲学的探求。ハイデガーの技術論（立て-立て/Gestell）、エルールの技術体制批判、スティグラーのファルマコン論が代表的アプローチ。", "哲学・倫理学", "Western_Europe", 1954, "https://en.wikipedia.org/wiki/Philosophy_of_technology"),
    ("生態学的哲学", "Ecological Philosophy", "人間と環境の関係を存在論・倫理学的に再考する哲学的立場。アルネ・ネスの深い生態学、ノルウェー・エコ哲学、バタイユの汎エロティシズムと自然観が含まれる。", "哲学・倫理学", "Western_Europe", 1973, "https://en.wikipedia.org/wiki/Deep_ecology"),
    ("現象学的社会学", "Phenomenological Sociology", "シュッツがフッサール現象学を社会学に適用した学問領域。日常生活の意味構造、間主観性、自然的態度を分析する。バーガー＆ルックマンの知識社会学に継承された。", "哲学・倫理学", "Western_Europe", 1932, "https://en.wikipedia.org/wiki/Alfred_Schutz"),
    # ===== 歴史学 (新規専門分野) (~50) =====
    ("大西洋奴隷貿易の歴史", "History of the Atlantic Slave Trade", "15〜19世紀に大西洋を横断して行われた奴隷貿易の歴史的研究。ラヴジョイ、エルティス、クリントンが代表的研究者。奴隷の経験、中間航路、廃止運動の歴史を含む。", "歴史学", "North_America", 1444, "https://en.wikipedia.org/wiki/Atlantic_slave_trade"),
    ("ハプスブルク帝国史", "Habsburg Empire History", "中央ヨーロッパを支配したハプスブルク家の帝国（1282〜1918年）の政治・文化・社会史。多民族・多言語帝国としての特性、ウィーン・バロック文化、帝国解体の過程が主要研究対象。", "歴史学", "Western_Europe", 1282, "https://en.wikipedia.org/wiki/Habsburg_monarchy"),
    ("フランス革命史", "History of the French Revolution", "1789年から1799年にかけてのフランス政治・社会変革の歴史的研究。フュレ、ハント、ランデが代表的論者。恐怖政治・ナポレオン体制への移行・世界史的影響が主要論点。", "歴史学", "Western_Europe", 1789, "https://en.wikipedia.org/wiki/French_Revolution"),
    ("ロシア革命史", "History of the Russian Revolution", "1917年のロシア革命（二月革命・十月革命）とその後のソ連形成過程の歴史的研究。パイプス、ファイジェス、コッチャーが代表的論者。", "歴史学", "Western_Europe", 1917, "https://en.wikipedia.org/wiki/Russian_Revolution"),
    ("冷戦史", "Cold War History", "1947〜1991年の米ソ対立の歴史的研究。ガッディス（修正主義批判）、ウィリアムズ（修正主義）が代表的論者。核抑止・代理戦争・イデオロギー対立・経済競争が主要論点。", "歴史学", "North_America", 1947, "https://en.wikipedia.org/wiki/Cold_War"),
    ("ナチズムとホロコースト史", "History of Nazism and Holocaust", "ナチス・ドイツによるユダヤ人大虐殺とヨーロッパ支配の歴史的研究。イェルシャルミ、ラウル・ヒルバーグ、プリモ・レーヴィが代表的論者・証言者。記憶・証言・比較研究が主要論点。", "歴史学", "Western_Europe", 1933, "https://en.wikipedia.org/wiki/The_Holocaust"),
    ("植民地後期アフリカ史", "Late Colonial African History", "19〜20世紀のアフリカ植民地化と独立運動の歴史的研究。パデモア、ンクルマ、ファノンが代表的思想家。植民地経済・民族主義運動・パン・アフリカニズムが主要論点。", "歴史学", "Sub_Saharan_Africa", 1884, "https://en.wikipedia.org/wiki/Scramble_for_Africa"),
    ("オスマン帝国史", "Ottoman Empire History", "1299〜1922年にかけてのオスマン帝国の政治・社会・文化史。フィンケル、コリン・イマベール、アケームが代表的研究者。多民族・多宗教帝国の統治、タンジマート改革が主要論点。", "歴史学", "West_Asia_North_Africa", 1299, "https://en.wikipedia.org/wiki/Ottoman_Empire"),
    ("東南アジア史", "Southeast Asian History", "東南アジア諸国の古代から近代に至る歴史的発展の研究。ウォルターズの曼陀羅国家概念、ビルマ・タイ・ジャワ・ベトナムの地域史、植民地化と独立運動が主要テーマ。", "歴史学", "East_Asia", 500, "https://en.wikipedia.org/wiki/History_of_Southeast_Asia"),
    ("朝鮮半島史", "History of Korea", "古朝鮮から現代大韓民国・朝鮮民主主義人民共和国に至る朝鮮半島の歴史。三国時代・高麗・朝鮮王朝・日本植民地期・分断が主要時代区分。エッカートが代表的研究者。", "歴史学", "East_Asia", -2333, "https://en.wikipedia.org/wiki/History_of_Korea"),
    ("ヴェトナム戦争史", "History of Vietnam War", "1955〜1975年のヴェトナム戦争の歴史的研究。カロー、タリー、フィッツジェラルドが代表的論者。冷戦・民族解放・アメリカの介入・反戦運動が主要論点。", "歴史学", "East_Asia", 1955, "https://en.wikipedia.org/wiki/Vietnam_War"),
    ("トランスナショナル・ヒストリー", "Transnational History", "国民国家の枠を超えて移動・交流・相互影響を歴史的に分析する方法論。アーミテッジ、ベイリン、シャナハンが代表的論者。移民・宗教・商品・思想の越境的流通が主要論点。", "歴史学", "North_America", 1997, "https://en.wikipedia.org/wiki/Transnational_history"),
    ("公衆衛生史", "History of Public Health", "疾病・医療・衛生の歴史的発展と公衆衛生制度の形成を研究する分野。マクニール（疫病と世界史）、ポーター、ローゼンバーグが代表的論者。感染症・都市衛生・医療政策が主要論点。", "歴史学", "North_America", 1967, "https://en.wikipedia.org/wiki/Public_health_history"),
    ("都市史", "Urban History", "都市の形成・発展・変容を歴史的に研究する分野。ハワード（田園都市）、マンフォード（都市の文化）、スコットの見えにくい国家理論が代表的論者・著作。", "歴史学", "North_America", 1961, "https://en.wikipedia.org/wiki/Urban_history"),
    ("科学技術史", "History of Science and Technology", "科学的知識と技術の歴史的発展を研究する分野。クーン（科学革命の構造）、サルトン、シェイピン、デストルが代表的論者。科学革命・科学者共同体・技術と社会が主要論点。", "歴史学", "North_America", 1962, "https://en.wikipedia.org/wiki/History_of_science"),
    ("帝国主義と経済史", "History of Imperialism and Economics", "帝国主義的拡張と資本主義発展の歴史的関係を研究する分野。レーニン（帝国主義論）、ホブスン、ウォーラーステイン（世界システム論）が代表的論者。", "歴史学", "Western_Europe", 1902, "https://en.wikipedia.org/wiki/History_of_capitalism"),
    ("ウィーン文化史", "History of Viennese Culture", "19世紀末から20世紀初頭のウィーンにおける芸術・思想・科学の革命的展開の研究。フロイトの精神分析、マーラー・シェーンベルクの音楽、クリムト・シーレの美術、マッハの実証主義が焦点。", "歴史学", "Western_Europe", 1870, "https://en.wikipedia.org/wiki/Vienna_Secession"),
    # ===== 宗教学 (新規) (~40) =====
    ("比較宗教学", "Comparative Religion", "異なる宗教的伝統を体系的に比較研究する学問的アプローチ。マックス・ミュラー（比較神話学の創始）、フレイザー、エリアーデが代表的論者。聖なるものの普遍性と文化的特殊性の緊張を論じる。", "宗教学", "Western_Europe", 1867, "https://en.wikipedia.org/wiki/Comparative_religion"),
    ("世俗化論", "Secularization Theory", "近代化に伴い宗教が社会的影響力を失っていくという社会学的仮説。デュルケーム・ウェーバー・バーガーが古典的論者。反世俗化論（スタークとバインブリッジ）や「脱世俗化」論が対抗する。", "宗教学", "Western_Europe", 1922, "https://en.wikipedia.org/wiki/Secularization"),
    ("宗教的経験の研究", "Study of Religious Experience", "ウィリアム・ジェームズ（宗教的経験の諸相）以来の宗教的経験の類型・性質・認識論的地位の研究。神秘体験・回心・恩寵・幻視・霊的感覚が主要な研究対象。", "宗教学", "North_America", 1902, "https://en.wikipedia.org/wiki/Religious_experience"),
    ("宗教的資本主義論", "Religious Capitalism Theory", "マックス・ウェーバーの「プロテスタンティズムの倫理と資本主義の精神」に端を発する宗教と経済発展の関係研究。ベラー、スウォーミナサン、ミンクスが現代的発展を担う。", "宗教学", "Western_Europe", 1905, "https://en.wikipedia.org/wiki/The_Protestant_Ethic_and_the_Spirit_of_Capitalism"),
    ("黒人教会と宗教", "Black Church and Religion", "アフリカ系アメリカ人の宗教的伝統・黒人教会の歴史と社会的役割の研究。キング・ジュニア、ダグラス・ケリー・ブラウン、コーネル・ウェストが代表的論者。公民権運動との連動が中心。", "宗教学", "North_America", 1773, "https://en.wikipedia.org/wiki/Black_church"),
    ("イスラーム改革主義", "Islamic Reformism", "19〜20世紀のイスラーム世界における宗教改革・近代化の潮流。アフガニー・アブドゥ・リダーの近代イスラーム思想、サラフィー主義、ムスリム同胞団が代表的運動。", "宗教学", "West_Asia_North_Africa", 1870, "https://en.wikipedia.org/wiki/Islamic_modernism"),
    ("ヒンドゥー改革主義", "Hindu Reformism", "19〜20世紀のヒンドゥー教の近代的改革運動。ラームモーハン・ロイのブラフモ・サマージ、ヴィヴェーカーナンダのラームクリシュナ運動、アウロビンドの統合ヨーガが代表。", "宗教学", "South_Asia", 1828, "https://en.wikipedia.org/wiki/Hindu_reform_movements"),
    ("解放の神学", "Liberation Theology", "グティエレス（グアテマラ）が提唱したラテンアメリカ・カトリック神学の一潮流。貧しい人々の視点からの聖書解釈と社会変革を結びつける。ボフ、セグンドも代表的論者。", "宗教学", "Latin_America", 1971, "https://en.wikipedia.org/wiki/Liberation_theology"),
    ("原理主義研究", "Fundamentalism Studies", "宗教的原理主義の発生・伝播・社会的機能を比較研究する学術的アプローチ。マーティン・マルティ、サリーン・ファセイ、アームストロングが代表的論者。キリスト教・イスラーム・ユダヤ教・ヒンドゥー教等を横断的に分析。", "宗教学", "North_America", 1991, "https://en.wikipedia.org/wiki/Fundamentalism"),
    ("宗教的多元主義", "Religious Pluralism", "複数の宗教的伝統が同様に真理・救済に接近しうるという立場。ジョン・ヒック（神中心的多元論）、クノッター、スウィドラーが代表的論者。宗教間対話の哲学的基礎を提供する。", "宗教学", "Western_Europe", 1980, "https://en.wikipedia.org/wiki/Religious_pluralism"),
    ("スピリチュアリティ研究", "Spirituality Studies", "制度的宗教に限定されない霊的経験・実践・意識の状態を研究する学際的分野。「宗教なき霊性」「後世俗的スピリチュアリティ」「ニューエイジ運動」が主要研究対象。ウッドヘッドが代表的論者。", "宗教学", "Western_Europe", 1996, "https://en.wikipedia.org/wiki/Spirituality"),
    ("仏教現代化", "Buddhist Modernism", "植民地・近代化に応じた仏教の再解釈と改革の研究。ダルマパーラのシンハラ仏教復興、禅の西洋化（鈴木大拙）、ティク・ナット・ハンの engaged Buddhism が代表。", "宗教学", "East_Asia", 1880, "https://en.wikipedia.org/wiki/Buddhist_modernism"),
    ("道教の研究", "Daoist Studies", "中国の老荘思想を起源とする道教（道家と道教宗教）の学術的研究。ウォーレン、ジアラルデ、シュナイダーが代表的論者。内丹・外丹・清談・民間道教を含む総合的研究。", "宗教学", "East_Asia", -600, "https://en.wikipedia.org/wiki/Taoism"),
    ("儒教の研究", "Confucian Studies", "孔子を始祖とする中国の思想体系（儒教）の学術的研究。宋学（朱子学）、陽明学、清代考証学、現代の新儒家（唐君毅、牟宗三）、ロービーが代表的研究者。", "宗教学", "East_Asia", -551, "https://en.wikipedia.org/wiki/Confucianism"),
    # ===== 古典学 (新規) (~40) =====
    ("ギリシア哲学史", "History of Greek Philosophy", "ソクラテス以前の自然哲学者から新プラトン主義まで古代ギリシアの哲学的伝統の研究。グスリー（ギリシア哲学の歴史）、ロス、バーネットが代表的研究者。", "古典学", "Western_Europe", -585, "https://en.wikipedia.org/wiki/Ancient_Greek_philosophy"),
    ("ローマ法の研究", "Roman Law Studies", "古代ローマの法体系（十二表法・ユスティニアヌス法典）の歴史的・比較法的研究。ポンポニウス、ガイウスが古代の法学者。ドイツ歴史法学派（サヴィニー）が近代的研究の基盤を確立。", "古典学", "Western_Europe", -450, "https://en.wikipedia.org/wiki/Roman_law"),
    ("ビザンティン学", "Byzantine Studies", "東ローマ帝国（330〜1453年）の歴史・文化・芸術・神学を研究する学問分野。カジダン、ウィトウ、グレゴリーが代表的研究者。ギリシア教父・東方正教会神学・モザイク芸術が主要研究対象。", "古典学", "Western_Europe", 330, "https://en.wikipedia.org/wiki/Byzantine_studies"),
    ("中世ラテン文学", "Medieval Latin Literature", "5〜15世紀のラテン語文学の研究。アウグスティヌス（神の国）、トマス・アクィナス（神学大全）、ダンテ以前のラテン詩（ゴリアール詩人）が主要研究対象。クルティウスが基礎研究を確立。", "古典学", "Western_Europe", 400, "https://en.wikipedia.org/wiki/Medieval_Latin"),
    ("古代東アジアの書写材料", "Ancient East Asian Writing Materials", "中国・日本・韓国における甲骨・青銅器・竹簡・木簡・絹・紙の歴史的展開と書写文化の研究。殷代甲骨文・周代金文・漢代竹簡が中核的研究対象。", "古典学", "East_Asia", -1600, "https://en.wikipedia.org/wiki/Oracle_bone"),
    ("ペルシア古典文学", "Persian Classical Literature", "イラン高原を中心とするペルシア語古典文学の研究。フィルダウスィー（シャーナーメ）、ルーミー（マスナヴィー）、ハーフィズ（ディーワーン）が代表的詩人。", "古典学", "West_Asia_North_Africa", 977, "https://en.wikipedia.org/wiki/Persian_literature"),
    ("アラビア古典文学", "Arabic Classical Literature", "7〜15世紀のアラビア語古典文学の研究。ムアッラカート（前イスラーム詩）、千夜一夜物語、アル＝マアッリー、イブン・バトゥータの旅行記が代表的テキスト。", "古典学", "West_Asia_North_Africa", 600, "https://en.wikipedia.org/wiki/Arabic_literature"),
    ("ギリシア・ローマの哲学テキスト伝達", "Transmission of Greco-Roman Philosophical Texts", "古代ギリシア・ローマの哲学テキストの写本伝達・アラビア語翻訳・ヨーロッパ中世への伝播を研究する文献学分野。バグダッドの翻訳運動（フナイン・イブン・イスハーク）が重要中継点。", "古典学", "West_Asia_North_Africa", 830, "https://en.wikipedia.org/wiki/Translation_movement"),
    ("インド論理学の伝統", "Indian Logic Tradition", "インド哲学における推論・論証・誤謬の理論的伝統。ニヤーヤ学派（ゴータマ）、バウッダ因明（ディグナーガ・ダルマキールティ）、ジャイナ認識論が主要流派。", "古典学", "South_Asia", 400, "https://en.wikipedia.org/wiki/Indian_logic"),
    ("マヤ文書・碑文研究", "Maya Epigraphy", "マヤ文字（ヒエログリフ）の解読と碑文・コデックスの文献学的研究。プロスクリアコフ（歴史的解釈）、コーとヴァン・スティーン（音読法）が解読を大幅に進展させた。", "古典学", "Latin_America", -300, "https://en.wikipedia.org/wiki/Maya_script"),
    ("アステカ写本研究", "Aztec Manuscript Studies", "アステカ（メシカ）文明の絵文書（コデックス）の研究。メンドーサ写本、ボルジア写本が代表的写本。スペイン征服前の歴史・暦・神話・税制の記録を含む。", "古典学", "Latin_America", 1300, "https://en.wikipedia.org/wiki/Aztec_codices"),
    ("古代インド医学文献", "Ancient Indian Medical Texts", "インドの伝統医学（アーユルヴェーダ）の古典文献研究。チャラカ本集・スシュルタ本集・アーシュタンガフリダヤムが代表的テキスト。手術技法・薬草・哲学的身体論を含む。", "古典学", "South_Asia", -600, "https://en.wikipedia.org/wiki/Ayurveda"),
    ("古代ケルト文化研究", "Celtic Studies", "ケルト語族の言語・文学・神話・考古学を研究する学問分野。アイルランド神話（ウルスター・サイクル）、ウェールズのマビノギオン、ドルイド教が主要研究対象。", "古典学", "Western_Europe", -700, "https://en.wikipedia.org/wiki/Celtic_studies"),
    ("ゲルマン古典文学", "Germanic Classical Literature", "古代ゲルマン語族（古英語・古ノルド語・古高ドイツ語）の文学的伝統研究。ベオウルフ、エッダ（詩のエッダ・散文エッダ）、ニーベルンゲンの歌が代表的テキスト。", "古典学", "Western_Europe", 700, "https://en.wikipedia.org/wiki/Old_Norse_literature"),
    # ===== 美学・芸術理論 (新規) (~30) =====
    ("美学の制度論", "Institutional Theory of Art", "ジョージ・ダントー（芸術界）とディキー（芸術の制度的定義）が提唱。芸術作品は芸術界という制度によって芸術として地位づけられるとする。ウォーホルの「ブリロ・ボックス」が発端となる思考実験。", "美学・芸術理論", "North_America", 1964, "https://en.wikipedia.org/wiki/Institutional_theory_of_art"),
    ("美学的態度論", "Aesthetic Attitude Theory", "審美的経験には特定の態度（無関心的注意）が必要だとする立場。ストールニッツ、バルドリーが代表的論者。デューイ、グロス等の批判を経て精緻化された。", "美学・芸術理論", "North_America", 1961, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("芸術の認識論的価値", "Epistemic Value of Art", "芸術が知識・理解・洞察を提供しうるかを問う美学的問い。キャロル（芸術の認識論）、オルタ、ゴールマンが代表的論者。倫理と美学の関係論とも連動する。", "美学・芸術理論", "North_America", 2000, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("芸術の倫理的価値", "Ethical Value of Art", "芸術の倫理的内容が美的価値に影響するかを問う美学的問い。道徳主義（不道徳作品の美的欠如）・自律主義（倫理と美の分離）・穏健な道徳主義（キャロル）が対立する。", "美学・芸術理論", "North_America", 1996, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("ポピュラー美学", "Popular Aesthetics", "大衆文化・ポピュラーアート・エンターテインメントの審美的価値を論じる美学の分野。キャロル（大衆文化の美学）、シュスターマン（プラグマティスト美学）が代表的論者。ハイアートとポップアートの境界論争を含む。", "美学・芸術理論", "North_America", 1992, "https://en.wikipedia.org/wiki/Popular_culture"),
    ("美的相対主義と普遍主義", "Aesthetic Relativism and Universalism", "美的判断が文化・個人に相対的か普遍的に妥当するかを問う美学の根本問題。カントの美的判断の共通感覚（sensus communis）理論、文化相対主義美学、ヒュームの趣味の基準論が代表的立場。", "美学・芸術理論", "Western_Europe", 1757, "https://en.wikipedia.org/wiki/Aesthetics"),
    ("工芸の美学", "Aesthetics of Craft", "工芸・デザイン・機能的対象の審美的価値を論じる美学の分野。モリス（芸術工芸運動）、マクラッケン、ベイカーが代表的論者。民藝運動（柳宗悦）との比較が行われる。", "美学・芸術理論", "Western_Europe", 1880, "https://en.wikipedia.org/wiki/Arts_and_Crafts_movement"),
    ("伝統的日本美学", "Traditional Japanese Aesthetics", "日本の伝統美学概念の体系的研究。もののあわれ（本居宣長）・幽玄（世阿弥）・侘び・寂び（千利休）・いき（九鬼周造）・間・物のかたちが主要概念。", "美学・芸術理論", "East_Asia", 1798, "https://en.wikipedia.org/wiki/Japanese_aesthetics"),
    ("インド美学", "Indian Aesthetics", "古代インドで発展した芸術・詩学・音楽の美学的理論体系。ラサ理論（ナーティヤ・シャーストラ）、バラタの8つのラサ、アビナヴァグプタの拡張（シャーンタ・ラサ追加）、ドワニ理論が代表。", "美学・芸術理論", "South_Asia", 200, "https://en.wikipedia.org/wiki/Rasa_(aesthetics)"),
    ("中国美学", "Chinese Aesthetics", "中国の芸術・詩学・書道・絵画における美学的理論体系。気韻生動（謝赫の六法）、文人画理論（蘇軾）、南宗画・北宗画の区別、空白の美学が代表的概念。", "美学・芸術理論", "East_Asia", 500, "https://en.wikipedia.org/wiki/Chinese_art"),
    # ===== 言語学（専門分野追加） (~30) =====
    ("談話マーカー研究", "Discourse Markers Research", "会話や書き言葉において談話の組織化・話者の態度・対人的関係を示す語・句（なお・つまり・だから・まあ等）の語用論的・文法的研究。シフリン、フレイザーが代表的研究者。", "言語学", "North_America", 1987, "https://en.wikipedia.org/wiki/Discourse_marker"),
    ("フレーム問題と言語", "Frame Problem in Language", "文脈・背景知識・世界の変化を言語理解にどう組み込むかという認知科学・AI的問題。フィルモアのフレーム意味論、スキーマ理論（バートレット）が関連する言語学的解決策を提供する。", "言語学", "North_America", 1969, "https://en.wikipedia.org/wiki/Frame_problem"),
    ("アナフォラ解析", "Anaphora Resolution", "代名詞・指示表現が先行詞とどのように結びつくかを分析する言語学・計算言語学の研究分野。制約ベース解析（センタリング理論）、文法的拘束（バインディング理論・チョムスキー）が代表的アプローチ。", "言語学", "North_America", 1981, "https://en.wikipedia.org/wiki/Anaphora_(linguistics)"),
    ("語順と情報構造", "Word Order and Information Structure", "焦点・トピック・与件性・対比等の情報的区別が語順・強勢・形態に反映されるメカニズムを研究する言語学分野。チェコ言語学派（マテジウス）、ランブレクトが代表的論者。", "言語学", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Information_structure"),
    ("バイリンガリズム研究", "Bilingualism Research", "2言語以上を習得・使用する個人と社会の言語的・認知的側面を研究する分野。コードスイッチング、言語混合、認知的利点（抑制制御）、二言語能力の計測が主要論点。グロスジャンが代表的研究者。", "言語学", "Western_Europe", 1967, "https://en.wikipedia.org/wiki/Bilingualism"),
    ("言語とジェンダー", "Language and Gender", "言語使用におけるジェンダー差・ジェンダーの言語的構築を研究する分野。タネン（異文化としての男女コミュニケーション）、ラッコフの女性語研究、クレスとバン・ルーウェンのマルチモーダル分析が代表。", "言語学", "North_America", 1975, "https://en.wikipedia.org/wiki/Language_and_gender"),
    ("認知文体論", "Cognitive Stylistics", "認知言語学の理論（メタファー・スキーマ・視点・フレーミング等）を文学テキストの文体分析に応用する研究分野。スティーンゼン、ストックウェル、テイラーが代表的論者。", "言語学", "Western_Europe", 1995, "https://en.wikipedia.org/wiki/Cognitive_stylistics"),
    ("語彙プラグマティクス", "Lexical Pragmatics", "単語の慣習的意味と文脈における解釈の乖離を分析する語用論の下位分野。語彙の特定化・弱化・メタファー的使用のメカニズムを関連性理論等の枠組みで分析する。", "言語学", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/Pragmatics"),
    ("言語進化論", "Language Evolution", "人間の言語能力と言語システムがどのように進化したかを研究する学際分野。ピンカー（言語本能）、クリスチャンセン、ホーキンスが代表的論者。文化的・生物学的共進化が主要論点。", "言語学", "North_America", 1990, "https://en.wikipedia.org/wiki/Language_evolution"),
    ("音韻習得研究", "Phonological Acquisition", "子供が母語の音声体系を習得するプロセスの研究。子音・母音のマイルストーン、音節構造の習得、韻律の発達が主要論点。音韻的意識の発達と読み書き習得との関係も重要。", "言語学", "North_America", 1979, "https://en.wikipedia.org/wiki/Language_acquisition"),
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
