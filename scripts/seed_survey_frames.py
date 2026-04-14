"""
全5分野の調査フレーム（分野構造）を survey_frame テーブルに投入するスクリプト
"""
import sqlite3, os, uuid, json

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

# ---------------------------------------------------------------
# 分野構造定義
# (domain, level, parent_name, name, name_en, description, est_count, priority, refs)
# level 1 = 大分野, level 2 = 中分野, level 3 = 小分野
# ---------------------------------------------------------------

FRAMES = {

# ================================================================
# 社会科学 / social_theory
# ================================================================
"social_theory": [
  # ---- 大分野 ----
  (1, None, "心理学", "Psychology",
   "人間の認知・感情・行動・発達・精神病理を科学的に研究する学問。",
   350, 1, ["Annual Review of Psychology", "APA Handbook"]),
  (1, None, "社会学", "Sociology",
   "社会構造・制度・集団・不平等・文化を分析する学問。",
   200, 1, ["Annual Review of Sociology"]),
  (1, None, "経済学", "Economics",
   "希少資源の配分・市場・意思決定・マクロ経済を研究する学問。",
   200, 2, ["Journal of Economic Literature", "Handbook of Economics"]),
  (1, None, "政治学", "Political Science",
   "権力・国家・政策・国際関係・民主主義を研究する学問。",
   150, 2, ["Annual Review of Political Science"]),
  (1, None, "文化人類学", "Cultural Anthropology",
   "人間の文化・社会・象徴・儀礼・日常実践をフィールドワークで研究する学問。",
   150, 1, ["Annual Review of Anthropology"]),
  (1, None, "教育学", "Education Studies",
   "学習・教授・カリキュラム・教育制度・発達を研究する学問。",
   120, 3, ["Review of Educational Research"]),
  (1, None, "コミュニケーション論", "Communication Studies",
   "メディア・言語・対人・組織・マスコミュニケーションを研究する学問。",
   100, 3, ["Journal of Communication"]),
  (1, None, "法社会学", "Sociology of Law",
   "法・制度・規範・正義を社会科学的に分析する学問。",
   80, 3, ["Law & Society Review"]),

  # ---- 心理学 中分野 ----
  (2, "心理学", "認知心理学", "Cognitive Psychology",
   "知覚・注意・記憶・思考・言語・意思決定を研究する領域。",
   80, 1, ["Neisser (1967)", "Kahneman (2011)"]),
  (2, "心理学", "社会心理学", "Social Psychology",
   "他者・集団・態度・説得・偏見・規範が行動に与える影響を研究する領域。",
   70, 1, ["Asch (1955)", "Milgram (1963)", "Zimbardo (1971)"]),
  (2, "心理学", "発達心理学", "Developmental Psychology",
   "乳幼児期から老年期にわたる認知・感情・社会性の変化を研究する領域。",
   60, 1, ["Piaget", "Vygotsky", "Bronfenbrenner"]),
  (2, "心理学", "臨床・異常心理学", "Clinical & Abnormal Psychology",
   "精神疾患の診断・治療・予防を研究する領域。",
   60, 1, ["DSM-5", "ICD-11"]),
  (2, "心理学", "パーソナリティ心理学", "Personality Psychology",
   "個人差・特性・自己概念・動機を研究する領域。",
   40, 2, ["Big Five", "McCrae & Costa"]),
  (2, "心理学", "神経心理学", "Neuropsychology",
   "脳と行動・認知の関係を研究する領域。",
   40, 2, ["Luria", "Damasio"]),
  (2, "心理学", "産業・組織心理学", "Industrial-Organizational Psychology",
   "職場・リーダーシップ・動機づけ・組織行動を研究する領域。",
   40, 2, ["Herzberg", "Bandura"]),
  (2, "心理学", "健康心理学", "Health Psychology",
   "心理・行動が健康・疾病に与える影響を研究する領域。",
   30, 2, ["Engel biopsychosocial model"]),

  # ---- 社会学 中分野 ----
  (2, "社会学", "社会構造・階層論", "Social Stratification",
   "階級・不平等・社会移動・資本を分析する領域。",
   50, 1, ["Bourdieu", "Weber", "Giddens"]),
  (2, "社会学", "文化社会学", "Cultural Sociology",
   "文化・意味・アイデンティティ・消費を分析する領域。",
   40, 1, ["Durkheim", "CCCS Birmingham"]),
  (2, "社会学", "組織社会学", "Organizational Sociology",
   "組織・制度・官僚制・新制度論を研究する領域。",
   40, 2, ["Weber", "DiMaggio & Powell"]),
  (2, "社会学", "ネットワーク社会学", "Network Sociology",
   "社会的紐帯・ネットワーク構造・社会関係資本を研究する領域。",
   30, 2, ["Granovetter", "Burt"]),
  (2, "社会学", "科学・技術社会学 (STS)", "Science & Technology Studies",
   "科学・技術・社会の相互構成を研究する領域。",
   30, 1, ["Latour", "Bijker"]),

  # ---- 経済学 中分野 ----
  (2, "経済学", "行動経済学", "Behavioral Economics",
   "心理学的知見を経済学に統合し人間の意思決定を研究する領域。",
   50, 1, ["Thaler & Sunstein", "Kahneman & Tversky"]),
  (2, "経済学", "制度経済学", "Institutional Economics",
   "制度・ルール・取引費用が経済に与える影響を研究する領域。",
   40, 2, ["Coase", "North", "Williamson"]),
  (2, "経済学", "開発経済学", "Development Economics",
   "途上国の貧困・成長・援助・不平等を研究する領域。",
   40, 2, ["Sen", "Banerjee & Duflo"]),
  (2, "経済学", "マクロ経済学", "Macroeconomics",
   "国民経済全体の成長・景気循環・金融政策を研究する領域。",
   40, 3, ["Keynes", "Friedman"]),
  (2, "経済学", "情報・ゲーム理論", "Information & Game Theory",
   "戦略的相互作用・情報の非対称性を数理的に研究する領域。",
   30, 2, ["Nash", "Akerlof", "Spence"]),

  # ---- 文化人類学 中分野 ----
  (2, "文化人類学", "医療人類学", "Medical Anthropology",
   "疾病・健康・身体・治療の文化的構築を研究する領域。",
   30, 1, ["Kleinman", "Farmer"]),
  (2, "文化人類学", "経済人類学", "Economic Anthropology",
   "贈与・互酬・交換・資本主義の人類学的分析。",
   30, 2, ["Mauss", "Polanyi", "Sahlins"]),
  (2, "文化人類学", "象徴人類学", "Symbolic Anthropology",
   "象徴・儀礼・神話・意味体系を研究する領域。",
   30, 1, ["Turner", "Geertz", "Douglas"]),
  (2, "文化人類学", "政治人類学", "Political Anthropology",
   "権力・国家・暴力・統治を人類学的に研究する領域。",
   25, 2, ["Clastres", "Scott"]),
  (2, "文化人類学", "感覚・物質文化研究", "Sensory & Material Culture Studies",
   "物・身体・感覚・マテリアリティの人類学。",
   20, 1, ["Miller", "Ingold", "Howes"]),
],

# ================================================================
# 自然科学 / natural_discovery
# ================================================================
"natural_discovery": [
  # ---- 大分野 ----
  (1, None, "物理学", "Physics",
   "物質・エネルギー・時空の基本法則を研究する学問。",
   400, 1, ["Physical Review Letters", "Reviews of Modern Physics"]),
  (1, None, "化学", "Chemistry",
   "物質の構造・性質・変化・合成を研究する学問。",
   350, 2, ["JACS", "Nature Chemistry"]),
  (1, None, "生物学", "Biology",
   "生命現象・進化・生態・分子機構を研究する学問。",
   400, 1, ["Cell", "Nature", "Annual Review of Biology"]),
  (1, None, "地球科学", "Earth Sciences",
   "地球の構造・気候・地質・海洋・大気を研究する学問。",
   200, 2, ["Earth and Planetary Science Letters"]),
  (1, None, "天文学・宇宙物理学", "Astronomy & Astrophysics",
   "宇宙・天体・宇宙論を研究する学問。",
   150, 2, ["The Astrophysical Journal", "Annual Review of Astronomy"]),
  (1, None, "数学", "Mathematics",
   "抽象的構造・論理・証明を研究する純粋・応用数学。",
   200, 2, ["Annals of Mathematics", "Bulletin of AMS"]),
  (1, None, "生態学", "Ecology",
   "生物と環境の相互作用・生物多様性・生態系機能を研究する学問。",
   300, 1, ["Ecology", "Annual Review of Ecology"]),

  # ---- 物理学 中分野 ----
  (2, "物理学", "量子力学・量子情報", "Quantum Mechanics & Quantum Information",
   "量子現象・量子コンピュータ・量子通信を研究する領域。",
   80, 1, ["Dirac", "Feynman", "Nielsen & Chuang"]),
  (2, "物理学", "相対性理論・重力", "Relativity & Gravity",
   "時空・重力波・ブラックホールを研究する領域。",
   50, 1, ["Einstein", "Hawking"]),
  (2, "物理学", "凝縮系物理学", "Condensed Matter Physics",
   "固体・液体・超伝導・トポロジカル物質を研究する領域。",
   80, 2, ["Landau", "Anderson"]),
  (2, "物理学", "素粒子物理学", "Particle Physics",
   "素粒子・標準模型・ヒッグス機構を研究する領域。",
   60, 2, ["Weinberg", "Glashow", "Salam"]),
  (2, "物理学", "統計力学・熱力学", "Statistical Mechanics & Thermodynamics",
   "系の統計的性質・エントロピー・相転移を研究する領域。",
   50, 2, ["Boltzmann", "Gibbs"]),
  (2, "物理学", "非線形物理学・複雑系", "Nonlinear Physics & Complex Systems",
   "カオス・自己組織化・創発・フラクタルを研究する領域。",
   40, 1, ["Lorenz", "Prigogine", "Mandelbrot"]),

  # ---- 化学 中分野 ----
  (2, "化学", "有機化学", "Organic Chemistry",
   "炭素化合物の構造・反応・合成を研究する領域。",
   80, 2, ["Woodward", "Corey"]),
  (2, "化学", "無機化学・材料化学", "Inorganic & Materials Chemistry",
   "金属・セラミクス・新材料・触媒を研究する領域。",
   60, 2, ["Cotton"]),
  (2, "化学", "物理化学", "Physical Chemistry",
   "化学反応の速度・熱力学・分光を研究する領域。",
   50, 3, ["Atkins"]),
  (2, "化学", "生化学・分子生物学", "Biochemistry & Molecular Biology",
   "生体分子・代謝・遺伝情報を研究する領域。",
   80, 1, ["Watson & Crick", "Lehninger"]),
  (2, "化学", "計算化学", "Computational Chemistry",
   "量子化学計算・分子動力学シミュレーションを研究する領域。",
   40, 2, ["Pople", "Kohn"]),

  # ---- 生物学 中分野 ----
  (2, "生物学", "分子生物学・ゲノミクス", "Molecular Biology & Genomics",
   "DNA・RNA・タンパク質・ゲノム解析を研究する領域。",
   80, 1, ["Crick", "Sanger"]),
  (2, "生物学", "細胞生物学", "Cell Biology",
   "細胞構造・シグナル伝達・細胞分裂を研究する領域。",
   60, 1, ["Alberts"]),
  (2, "生物学", "発生生物学", "Developmental Biology",
   "受精卵から個体への形態形成・パターン形成を研究する領域。",
   50, 1, ["Waddington", "Wolpert"]),
  (2, "生物学", "進化生物学", "Evolutionary Biology",
   "自然選択・種分化・系統進化・進化ゲノミクスを研究する領域。",
   60, 1, ["Darwin", "Hamilton", "Mayr"]),
  (2, "生物学", "神経科学", "Neuroscience",
   "神経系・脳機能・シナプス可塑性・意識を研究する領域。",
   80, 1, ["Cajal", "Kandel"]),
  (2, "生物学", "免疫学", "Immunology",
   "免疫応答・抗体・炎症・免疫記憶を研究する領域。",
   50, 2, ["Burnet", "Jerne"]),

  # ---- 生態学 中分野 ----
  (2, "生態学", "生態系生態学", "Ecosystem Ecology",
   "物質循環・エネルギーフロー・生態系サービスを研究する領域。",
   60, 1, ["Odum", "Likens"]),
  (2, "生態学", "群集生態学", "Community Ecology",
   "種間相互作用・競争・捕食・多様性維持機構を研究する領域。",
   50, 1, ["MacArthur", "Wilson"]),
  (2, "生態学", "個体群生態学", "Population Ecology",
   "個体群動態・成長・絶滅・侵入を研究する領域。",
   40, 1, ["Lotka-Volterra", "May"]),
  (2, "生態学", "保全生態学", "Conservation Ecology",
   "絶滅危惧種・生息地保全・回復生態学を研究する領域。",
   40, 1, ["Soulé", "Wilcox"]),
  (2, "生態学", "行動生態学", "Behavioral Ecology",
   "動物行動の進化的適応・フォレジング・繁殖戦略を研究する領域。",
   30, 2, ["Krebs & Davies"]),

  # ---- 地球科学 中分野 ----
  (2, "地球科学", "気候科学", "Climate Science",
   "気候変動・気候系・大気-海洋相互作用を研究する領域。",
   60, 1, ["IPCC", "Hansen"]),
  (2, "地球科学", "地質学・構造地質学", "Geology & Tectonics",
   "プレートテクトニクス・地層・火山・地震を研究する領域。",
   50, 2, ["Wegener", "McKenzie"]),
  (2, "地球科学", "海洋学", "Oceanography",
   "海洋循環・海洋生物・海洋化学を研究する領域。",
   40, 2, ["Stommel", "Sverdrup"]),
],

# ================================================================
# 人文学 / humanities_concept
# ================================================================
"humanities_concept": [
  # ---- 大分野 ----
  (1, None, "哲学", "Philosophy",
   "存在・認識・倫理・言語・論理の根本問題を研究する学問。",
   300, 1, ["Stanford Encyclopedia of Philosophy"]),
  (1, None, "歴史学", "History",
   "過去の人間活動・事件・構造を史料に基づき研究する学問。",
   250, 2, ["American Historical Review"]),
  (1, None, "言語学", "Linguistics",
   "言語の構造・意味・使用・変化・習得を研究する学問。",
   200, 1, ["Language", "Annual Review of Linguistics"]),
  (1, None, "文学", "Literary Studies",
   "文学作品の解釈・批評・理論・比較研究を行う学問。",
   150, 3, ["PMLA", "New Literary History"]),
  (1, None, "宗教学", "Religious Studies",
   "宗教現象・神学・神話・儀礼・比較宗教を研究する学問。",
   100, 2, ["History of Religions"]),
  (1, None, "考古学", "Archaeology",
   "物質的遺物から過去の人間社会を研究する学問。",
   100, 2, ["Journal of Archaeological Method"]),
  (1, None, "美学・芸術哲学", "Aesthetics & Philosophy of Art",
   "美・崇高・芸術的経験・批評の哲学的基礎を研究する学問。",
   80, 1, ["Journal of Aesthetics and Art Criticism"]),

  # ---- 哲学 中分野 ----
  (2, "哲学", "存在論・形而上学", "Ontology & Metaphysics",
   "存在・実在・時間・因果・同一性を研究する領域。",
   60, 1, ["Aristotle", "Heidegger", "Quine"]),
  (2, "哲学", "認識論", "Epistemology",
   "知識・正当化・懐疑・真理の哲学的分析。",
   50, 1, ["Descartes", "Hume", "Gettier"]),
  (2, "哲学", "倫理学", "Ethics",
   "道徳的価値・義務・徳・功利・正義を研究する領域。",
   60, 1, ["Kant", "Mill", "Rawls"]),
  (2, "哲学", "言語哲学", "Philosophy of Language",
   "意味・指示・言語行為・真理条件を研究する領域。",
   40, 1, ["Frege", "Wittgenstein", "Austin"]),
  (2, "哲学", "心の哲学", "Philosophy of Mind",
   "意識・クオリア・志向性・心脳問題を研究する領域。",
   40, 1, ["Dennett", "Chalmers", "Nagel"]),
  (2, "哲学", "科学哲学", "Philosophy of Science",
   "科学的説明・反証・理論変化・実在論を研究する領域。",
   40, 1, ["Popper", "Kuhn", "Lakatos"]),
  (2, "哲学", "政治哲学", "Political Philosophy",
   "正義・自由・権力・民主主義・国家の規範的研究。",
   40, 1, ["Rawls", "Nozick", "Arendt"]),

  # ---- 言語学 中分野 ----
  (2, "言語学", "統語論・形式言語学", "Syntax & Formal Linguistics",
   "文法規則・生成文法・統語構造を研究する領域。",
   40, 2, ["Chomsky"]),
  (2, "言語学", "意味論・語用論", "Semantics & Pragmatics",
   "意味・指示・発話行為・含意を研究する領域。",
   40, 2, ["Grice", "Levinson"]),
  (2, "言語学", "社会言語学", "Sociolinguistics",
   "言語変異・多言語使用・言語イデオロギーを研究する領域。",
   30, 1, ["Labov", "Gumperz"]),
  (2, "言語学", "認知言語学", "Cognitive Linguistics",
   "メタファー・フレーム・概念化・身体性を研究する領域。",
   30, 1, ["Lakoff & Johnson", "Langacker"]),
  (2, "言語学", "歴史言語学・類型論", "Historical Linguistics & Typology",
   "言語変化・言語系統・言語の普遍性を研究する領域。",
   30, 2, ["Greenberg"]),
  (2, "言語学", "談話・テクスト分析", "Discourse & Text Analysis",
   "発話・テクスト・批判的談話分析を研究する領域。",
   25, 1, ["Fairclough", "van Dijk"]),

  # ---- 歴史学 中分野 ----
  (2, "歴史学", "社会史・文化史", "Social & Cultural History",
   "日常生活・周縁・メンタリテ・微視史を研究する領域。",
   50, 1, ["Ginzburg", "Natalie Davis"]),
  (2, "歴史学", "グローバル史・世界史", "Global & World History",
   "比較・接続・帝国・移動・グローバル化を研究する領域。",
   40, 1, ["Bayly", "Manning"]),
  (2, "歴史学", "歴史理論・史学史", "Theory of History & Historiography",
   "歴史認識・ナラティブ・メモリーを研究する領域。",
   30, 2, ["White", "Collingwood"]),
  (2, "歴史学", "ポストコロニアル史", "Postcolonial History",
   "植民地・帝国主義・サバルタン・グローバルサウスを研究する領域。",
   30, 1, ["Spivak", "Chakrabarty"]),
],

# ================================================================
# 工学 / engineering_method
# ================================================================
"engineering_method": [
  # ---- 大分野 ----
  (1, None, "情報工学・コンピュータ科学", "Computer Science & Engineering",
   "アルゴリズム・データ構造・OS・ネットワーク・AI・ソフトウェア工学を研究する学問。",
   400, 1, ["CACM", "IEEE Transactions", "ACM SIGPLAN"]),
  (1, None, "機械工学", "Mechanical Engineering",
   "熱流体・機械設計・ロボット・製造プロセスを研究する学問。",
   250, 2, ["Journal of Mechanical Engineering"]),
  (1, None, "電気・電子工学", "Electrical & Electronic Engineering",
   "回路・電力・通信・半導体・センサーを研究する学問。",
   250, 2, ["IEEE Transactions on Circuits"]),
  (1, None, "システム工学", "Systems Engineering",
   "複雑システムの設計・制御・最適化・信頼性を研究する学問。",
   150, 1, ["Systems Engineering Journal"]),
  (1, None, "建築・土木工学", "Architecture & Civil Engineering",
   "構造・材料・都市基盤・環境設計を研究する学問。",
   150, 3, ["ASCE Journals"]),
  (1, None, "化学工学", "Chemical Engineering",
   "化学反応・プロセス設計・輸送現象・分離操作を研究する学問。",
   150, 3, ["AIChE Journal"]),
  (1, None, "バイオエンジニアリング", "Bioengineering",
   "医療機器・バイオインフォ・組織工学・合成生物学を研究する学問。",
   150, 1, ["Nature Biotechnology"]),
  (1, None, "環境工学", "Environmental Engineering",
   "廃水処理・大気汚染・廃棄物管理・環境システムを研究する学問。",
   100, 2, ["Environmental Science & Technology"]),

  # ---- 情報工学 中分野 ----
  (2, "情報工学・コンピュータ科学", "アルゴリズム・計算理論", "Algorithms & Theory of Computation",
   "計算複雑性・アルゴリズム設計・数理最適化を研究する領域。",
   70, 2, ["Knuth", "Sipser"]),
  (2, "情報工学・コンピュータ科学", "機械学習・AI", "Machine Learning & AI",
   "学習アルゴリズム・深層学習・強化学習・自然言語処理を研究する領域。",
   100, 1, ["LeCun", "Bengio", "Hinton"]),
  (2, "情報工学・コンピュータ科学", "ソフトウェア工学", "Software Engineering",
   "ソフトウェア設計・アーキテクチャ・テスト・プロセスを研究する領域。",
   60, 2, ["Fowler", "Brooks"]),
  (2, "情報工学・コンピュータ科学", "ネットワーク・分散システム", "Networks & Distributed Systems",
   "プロトコル・P2P・クラウド・分散アルゴリズムを研究する領域。",
   50, 2, ["Lamport", "Cerf & Kahn"]),
  (2, "情報工学・コンピュータ科学", "データベース・情報検索", "Databases & Information Retrieval",
   "データモデル・クエリ最適化・検索エンジンを研究する領域。",
   40, 2, ["Codd", "Gray"]),
  (2, "情報工学・コンピュータ科学", "HCI・インタラクション", "Human-Computer Interaction",
   "ユーザビリティ・インタフェース設計・認知工学を研究する領域。",
   40, 1, ["Norman", "Card"]),
  (2, "情報工学・コンピュータ科学", "セキュリティ・暗号", "Security & Cryptography",
   "暗号理論・認証・プロトコル・サイバーセキュリティを研究する領域。",
   40, 1, ["Diffie & Hellman", "Rivest"]),

  # ---- システム工学 中分野 ----
  (2, "システム工学", "制御工学", "Control Engineering",
   "フィードバック制御・最適制御・適応制御を研究する領域。",
   50, 2, ["Bode", "Kalman"]),
  (2, "システム工学", "オペレーションズ・リサーチ", "Operations Research",
   "線形計画・整数計画・ネットワーク最適化・待行列を研究する領域。",
   40, 2, ["Dantzig", "Bellman"]),
  (2, "システム工学", "信頼性工学", "Reliability Engineering",
   "故障解析・FMEA・冗長設計・保全を研究する領域。",
   30, 2, ["IEEE Reliability Society"]),

  # ---- 機械工学 中分野 ----
  (2, "機械工学", "熱流体工学", "Thermal & Fluid Engineering",
   "熱伝導・流体力学・燃焼・ターボ機械を研究する領域。",
   60, 2, ["Incropera"]),
  (2, "機械工学", "ロボティクス・メカトロニクス", "Robotics & Mechatronics",
   "ロボット機構・制御・センサー融合・自律移動を研究する領域。",
   50, 1, ["Craig", "Siciliano"]),
  (2, "機械工学", "製造・生産工学", "Manufacturing & Production Engineering",
   "加工プロセス・品質管理・リーン生産・DXを研究する領域。",
   40, 2, ["Taylor", "Shingo"]),

  # ---- バイオエンジニアリング 中分野 ----
  (2, "バイオエンジニアリング", "合成生物学", "Synthetic Biology",
   "遺伝回路設計・代謝工学・CRISPR応用を研究する領域。",
   30, 1, ["Venter", "Doudna"]),
  (2, "バイオエンジニアリング", "バイオインフォマティクス", "Bioinformatics",
   "ゲノム解析・タンパク質構造予測・パスウェイ解析を研究する領域。",
   40, 1, ["Altschul (BLAST)", "AlphaFold"]),
  (2, "バイオエンジニアリング", "組織工学・再生医療", "Tissue Engineering & Regenerative Medicine",
   "スキャフォールド・幹細胞・オルガノイドを研究する領域。",
   30, 1, ["Langer", "Vacanti"]),
],

# ================================================================
# 芸術 / arts_question
# ================================================================
"arts_question": [
  # ---- 大分野 ----
  (1, None, "美術・視覚芸術", "Visual Arts",
   "絵画・彫刻・版画・インスタレーション・写真の制作と批評。",
   200, 1, ["October", "Artforum"]),
  (1, None, "音楽", "Music",
   "作曲・演奏・音楽学・音楽理論・民族音楽学を含む学問。",
   200, 2, ["Journal of the American Musicological Society"]),
  (1, None, "デザイン", "Design",
   "グラフィック・プロダクト・建築・UX・社会デザインを研究する学問。",
   150, 1, ["Design Studies", "Design Issues"]),
  (1, None, "映像・映画", "Film & Moving Image",
   "映画・映像・アニメーション・ゲームの制作と批評。",
   150, 2, ["Cinema Journal", "Screen"]),
  (1, None, "演劇・パフォーマンス", "Theatre & Performance",
   "演劇・ダンス・パフォーマンスアートの実践と理論。",
   100, 2, ["Theatre Journal", "TDR"]),
  (1, None, "文学・詩", "Literature & Poetry",
   "詩・小説・エッセイ・脚本の創作と批評理論。",
   100, 3, ["PMLA"]),
  (1, None, "建築デザイン", "Architectural Design",
   "建築の造形・理念・歴史・批評を研究する学問（美学的側面）。",
   80, 2, ["Journal of Architecture"]),
  (1, None, "芸術理論・批評", "Art Theory & Criticism",
   "芸術的価値・解釈・美学・批評理論を横断的に研究する学問。",
   100, 1, ["Art Bulletin", "Critical Inquiry"]),

  # ---- 美術 中分野 ----
  (2, "美術・視覚芸術", "現代美術・コンセプチュアルアート", "Contemporary & Conceptual Art",
   "1960年代以降の概念・プロセス・インスタレーション・社会的実践。",
   50, 1, ["Kosuth", "Duchamp"]),
  (2, "美術・視覚芸術", "写真・映像アート", "Photography & Video Art",
   "写真理論・映像インスタレーション・ドキュメンタリー。",
   40, 1, ["Benjamin", "Barthes", "Sontag"]),
  (2, "美術・視覚芸術", "絵画・版画", "Painting & Printmaking",
   "西洋・東洋・現代絵画の技法と批評。",
   40, 2, ["Greenberg"]),
  (2, "美術・視覚芸術", "彫刻・立体造形", "Sculpture & 3D Arts",
   "素材・空間・身体をめぐる立体的表現。",
   30, 2, ["Judd", "Serra"]),

  # ---- 音楽 中分野 ----
  (2, "音楽", "音楽理論・作曲", "Music Theory & Composition",
   "和声・対位法・形式・スペクトル楽派・電子音楽。",
   50, 2, ["Schenker", "Messiaen"]),
  (2, "音楽", "音楽学・音楽史", "Musicology & Music History",
   "音楽史・音楽テクスト・演奏実践研究。",
   40, 2, ["Taruskin"]),
  (2, "音楽", "民族音楽学・世界音楽", "Ethnomusicology & World Music",
   "非西洋音楽・音楽文化・フィールドワーク。",
   30, 1, ["Merriam", "Blacking"]),
  (2, "音楽", "電子音楽・サウンドアート", "Electronic Music & Sound Art",
   "電子音響・ノイズ・空間音響・サウンドスタディーズ。",
   30, 1, ["Schaeffer", "Cage"]),
  (2, "音楽", "ポピュラー音楽研究", "Popular Music Studies",
   "ロック・ヒップホップ・Kポップ・産業構造・ファン文化。",
   30, 1, ["Frith", "Hall"]),

  # ---- デザイン 中分野 ----
  (2, "デザイン", "グラフィック・タイポグラフィ", "Graphic Design & Typography",
   "視覚コミュニケーション・情報デザイン・文字設計。",
   30, 2, ["Müller-Brockmann", "Lupton"]),
  (2, "デザイン", "プロダクト・インダストリアルデザイン", "Product & Industrial Design",
   "機能・形態・素材・製造のデザイン実践。",
   30, 2, ["Rams", "Dreyfuss"]),
  (2, "デザイン", "インタラクション・UXデザイン", "Interaction & UX Design",
   "人間中心設計・使いやすさ・サービスデザイン。",
   40, 1, ["Norman", "IDEO"]),
  (2, "デザイン", "社会デザイン・デザイン思考", "Social Design & Design Thinking",
   "社会課題への創造的アプローチ・共創・フューチャーデザイン。",
   30, 1, ["IDEO", "Ezio Manzini"]),

  # ---- 芸術理論 中分野 ----
  (2, "芸術理論・批評", "ポストモダン・ポスト構造主義的批評", "Postmodern & Post-structuralist Criticism",
   "デリダ・フーコー・ボードリヤールの芸術批評応用。",
   30, 1, ["Derrida", "Foucault", "Baudrillard"]),
  (2, "芸術理論・批評", "フェミニスト・クィア批評", "Feminist & Queer Art Criticism",
   "ジェンダー・身体・アイデンティティの芸術的表象。",
   25, 1, ["Pollock", "Butler"]),
  (2, "芸術理論・批評", "マテリアル・感覚的転回", "Material & Sensory Turn",
   "物・マテリアリティ・感覚の芸術論的探究。",
   20, 1, ["Bennett", "Ingold"]),
]

}


def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 既存データを消去してから入れ直す
    cur.execute("DELETE FROM survey_frame")
    print("既存データを削除しました")

    # IDマップ（name → id）でparent_id解決
    name_to_id = {}
    rows_to_insert = []

    for domain, entries in FRAMES.items():
        for entry in entries:
            level, parent_name, name, name_en, desc, est, priority, refs = entry
            uid = str(uuid.uuid4())
            name_to_id[(domain, name)] = uid
            rows_to_insert.append((domain, level, parent_name, name, name_en, desc, est, priority, refs, uid))

    # Insert
    inserted = 0
    for domain, level, parent_name, name, name_en, desc, est, priority, refs, uid in rows_to_insert:
        parent_id = None
        if parent_name:
            parent_id = name_to_id.get((domain, parent_name))

        cur.execute("""
            INSERT INTO survey_frame
              (id, domain, level, parent_id, name, name_en, description,
               estimated_unit_count, survey_priority, key_references, survey_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'not_started')
        """, (uid, domain, level, parent_id, name, name_en, desc, est, priority,
              json.dumps(refs, ensure_ascii=False)))
        inserted += 1

    conn.commit()
    conn.close()
    print(f"投入完了: {inserted} 件")

    # 確認
    conn = sqlite3.connect(DB_PATH)
    for domain in FRAMES.keys():
        cnt = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=?", (domain,)).fetchone()[0]
        l1  = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=1", (domain,)).fetchone()[0]
        l2  = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=2", (domain,)).fetchone()[0]
        # name_ja
        domain_names = {"social_theory":"社会科学","natural_discovery":"自然科学",
                        "humanities_concept":"人文学","engineering_method":"工学","arts_question":"芸術"}
        print(f"  {domain_names[domain]}: {cnt}件 (大分野{l1}件 / 中分野{l2}件)")
    conn.close()


if __name__ == "__main__":
    seed()
