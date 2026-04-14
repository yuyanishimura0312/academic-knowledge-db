"""
全5分野の調査フレーム（分野構造）を survey_frame テーブルに投入するスクリプト

【v3修正版の考え方】
- 目標は「件数」ではなく「年代カバー率」で設定する
  - 1990年以降 ≥ 50%
  - 2000年以降 ≥ 30%
  - 2010年以降 ≥ 20%
  - 2020年以降 ≥ 10%
- level 3 (小分野) の name は domain table の subfield カラム値と一致させる
  → 実績件数を直接 COUNT(subfield = name) で取得できる
- estimated_unit_count は廃止・使用しない（件数目標はLLMの古典偏りを増幅する）
"""

import sqlite3, os, uuid, json

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

# ---------------------------------------------------------------
# 構造: (level, parent_name_or_None, name, name_en, description, priority, refs)
#   level 1 = 大分野  level 2 = 中分野  level 3 = 小分野 (DBのsubfield値と一致)
# ---------------------------------------------------------------

FRAMES = {

# ================================================================
# 社会科学 / social_theory
# ================================================================
"social_theory": [
  # ---- 大分野 ----
  (1, None, "心理学", "Psychology",
   "人間の認知・感情・行動・発達・精神病理を科学的に研究する学問。",
   1, ["Annual Review of Psychology", "APA Handbook"]),
  (1, None, "社会学", "Sociology",
   "社会構造・制度・集団・不平等・文化を分析する学問。",
   1, ["Annual Review of Sociology"]),
  (1, None, "経済学", "Economics",
   "希少資源の配分・市場・意思決定・マクロ経済を研究する学問。",
   2, ["Journal of Economic Literature"]),
  (1, None, "政治学", "Political Science",
   "権力・国家・政策・国際関係・民主主義を研究する学問。",
   2, ["Annual Review of Political Science"]),
  (1, None, "文化人類学", "Cultural Anthropology",
   "文化・社会・象徴・儀礼・日常実践をフィールドワークで研究する学問。",
   1, ["Annual Review of Anthropology"]),
  (1, None, "教育学", "Education Studies",
   "学習・教授・カリキュラム・教育制度を研究する学問。",
   3, ["Review of Educational Research"]),
  (1, None, "コミュニケーション論", "Communication Studies",
   "メディア・言語・対人・組織・マスコミュニケーション研究。",
   3, ["Journal of Communication"]),

  # ---- 心理学 中分野 → 小分野 ----
  (2, "心理学", "認知心理学", "Cognitive Psychology",
   "知覚・注意・記憶・思考・言語・意思決定を研究する領域。",
   1, ["Neisser (1967)", "Kahneman (2011)"]),
  (3, "認知心理学", "知覚・注意", "Perception & Attention", "", 1, []),
  (3, "認知心理学", "記憶・学習", "Memory & Learning", "", 1, []),
  (3, "認知心理学", "判断・意思決定", "Judgment & Decision Making", "", 1, []),
  (3, "認知心理学", "認知神経科学", "Cognitive Neuroscience", "", 1, []),
  (3, "認知心理学", "言語・思考・推論", "Language, Thought & Reasoning", "", 2, []),

  (2, "心理学", "社会心理学", "Social Psychology",
   "他者・集団・態度・説得・偏見が行動に与える影響を研究する領域。",
   1, ["Asch (1955)", "Milgram (1963)"]),
  (3, "社会心理学", "態度・説得", "Attitudes & Persuasion", "", 1, []),
  (3, "社会心理学", "社会的認知・帰属", "Social Cognition & Attribution", "", 1, []),
  (3, "社会心理学", "社会的影響・同調・服従", "Social Influence & Conformity", "", 1, []),
  (3, "社会心理学", "偏見・ステレオタイプ", "Prejudice & Stereotypes", "", 1, []),
  (3, "社会心理学", "集団プロセス", "Group Processes", "", 1, []),
  (3, "社会心理学", "対人関係・愛着", "Interpersonal Relationships & Attachment", "", 2, []),
  (3, "社会心理学", "感情心理学", "Emotion Psychology", "", 1, []),
  (3, "社会心理学", "文化心理学・異文化心理学", "Cultural & Cross-Cultural Psychology", "", 1, []),
  (3, "社会心理学", "進化心理学", "Evolutionary Psychology", "", 2, []),

  (2, "心理学", "発達心理学", "Developmental Psychology",
   "乳幼児期から老年期にわたる認知・感情・社会性の変化を研究する領域。",
   1, ["Piaget", "Vygotsky", "Bronfenbrenner"]),
  (3, "発達心理学", "乳幼児・児童発達", "Infant & Child Development", "", 1, []),
  (3, "発達心理学", "青年期・アイデンティティ", "Adolescence & Identity", "", 1, []),
  (3, "発達心理学", "成人期・老年期", "Adult & Aging Development", "", 2, []),
  (3, "発達心理学", "発達障害", "Developmental Disorders", "", 1, []),
  (3, "発達心理学", "生態学的・文化的発達", "Ecological & Cultural Development", "", 2, []),

  (2, "心理学", "臨床・異常心理学", "Clinical & Abnormal Psychology",
   "精神疾患の診断・治療・予防を研究する領域。",
   1, ["DSM-5", "ICD-11"]),
  (3, "臨床・異常心理学", "精神病理学・障害モデル", "Psychopathology & Disorder Models", "", 1, []),
  (3, "臨床・異常心理学", "心理療法・介入", "Psychotherapy & Interventions", "", 1, []),
  (3, "臨床・異常心理学", "臨床心理学・心理療法", "Clinical Psychology", "", 1, []),
  (3, "臨床・異常心理学", "心理アセスメント", "Psychological Assessment", "", 2, []),
  (3, "臨床・異常心理学", "共通要因・メタ理論", "Common Factors & Meta-Theory", "", 2, []),

  (2, "心理学", "パーソナリティ心理学", "Personality Psychology",
   "個人差・特性・自己概念・動機を研究する領域。",
   2, ["Big Five", "McCrae & Costa"]),
  (3, "パーソナリティ心理学", "特性論・パーソナリティ構造", "Trait Theory & Personality Structure", "", 1, []),
  (3, "パーソナリティ心理学", "動機・自己・人間性", "Motivation, Self & Humanistic Psychology", "", 1, []),

  (2, "心理学", "神経心理学", "Neuropsychology",
   "脳と行動・認知の関係を研究する領域。",
   2, ["Luria", "Damasio"]),
  (3, "神経心理学", "神経心理学", "Neuropsychology (clinical)", "", 1, []),

  (2, "心理学", "産業・組織心理学", "Industrial-Organizational Psychology",
   "職場・リーダーシップ・動機づけ・組織行動を研究する領域。",
   2, ["Herzberg", "Bandura"]),
  (3, "産業・組織心理学", "産業・組織心理学", "Industrial-Organizational Psychology", "", 1, []),
  (3, "産業・組織心理学", "学習動機づけ", "Learning Motivation", "", 1, []),

  (2, "心理学", "健康心理学", "Health Psychology",
   "心理・行動が健康・疾病に与える影響を研究する領域。",
   2, ["Engel biopsychosocial model"]),
  (3, "健康心理学", "健康心理学・行動医学", "Health Psychology & Behavioral Medicine", "", 1, []),
  (3, "健康心理学", "環境心理学", "Environmental Psychology", "", 2, []),
  (3, "健康心理学", "コミュニティ心理学", "Community Psychology", "", 3, []),
  (3, "健康心理学", "スポーツ心理学", "Sport Psychology", "", 3, []),

  (2, "心理学", "教育心理学", "Educational Psychology",
   "学習・動機・教授法の心理学的研究。",
   2, ["Bloom", "Dweck"]),
  (3, "教育心理学", "教育心理学", "Educational Psychology", "", 1, []),

  (2, "心理学", "法・犯罪心理学", "Forensic & Criminal Psychology",
   "犯罪行動・司法判断の心理学的研究。",
   2, ["Hare"]),
  (3, "法・犯罪心理学", "法・犯罪心理学", "Forensic & Criminal Psychology", "", 1, []),

  (2, "心理学", "コミュニケーション心理学", "Communication Psychology",
   "メディア・対人・言語コミュニケーションの心理学的研究。",
   3, []),
  (3, "コミュニケーション心理学", "コミュニケーション・メディア心理学", "Communication & Media Psychology", "", 2, []),

  # ---- 社会学 中分野 → 小分野 ----
  (2, "社会学", "社会構造・階層論", "Social Stratification", "", 1, ["Bourdieu", "Weber"]),
  (3, "社会構造・階層論", "社会階層・不平等", "Social Stratification & Inequality", "", 1, []),
  (3, "社会構造・階層論", "社会移動・資本", "Social Mobility & Capital", "", 2, []),

  (2, "社会学", "文化社会学", "Cultural Sociology", "", 1, ["Durkheim", "CCCS"]),
  (3, "文化社会学", "文化・アイデンティティ", "Culture & Identity", "", 1, []),
  (3, "文化社会学", "消費・ライフスタイル", "Consumption & Lifestyle", "", 2, []),

  (2, "社会学", "科学・技術社会学 (STS)", "Science & Technology Studies", "", 1, ["Latour", "Bijker"]),
  (3, "科学・技術社会学 (STS)", "アクターネットワーク論", "Actor-Network Theory", "", 1, []),
  (3, "科学・技術社会学 (STS)", "技術の社会的構成", "Social Construction of Technology", "", 1, []),

  (2, "社会学", "組織社会学", "Organizational Sociology", "", 2, ["Weber", "DiMaggio"]),
  (3, "組織社会学", "制度論・新制度主義", "Institutional Theory & Neo-Institutionalism", "", 1, []),

  (2, "社会学", "ネットワーク社会学", "Network Sociology", "", 2, ["Granovetter", "Burt"]),
  (3, "ネットワーク社会学", "社会的ネットワーク分析", "Social Network Analysis", "", 1, []),
  (3, "ネットワーク社会学", "社会関係資本", "Social Capital", "", 1, []),

  # ---- 経済学 中分野 → 小分野 ----
  (2, "経済学", "行動経済学", "Behavioral Economics", "", 1, ["Thaler", "Kahneman"]),
  (3, "行動経済学", "ヒューリスティクス・バイアス", "Heuristics & Biases", "", 1, []),
  (3, "行動経済学", "ナッジ・行動政策", "Nudges & Behavioral Policy", "", 1, []),
  (3, "行動経済学", "時間選好・非合理性", "Time Preferences & Irrationality", "", 2, []),

  (2, "経済学", "制度経済学", "Institutional Economics", "", 2, ["Coase", "North"]),
  (3, "制度経済学", "取引費用理論", "Transaction Cost Theory", "", 1, []),
  (3, "制度経済学", "経路依存・制度変化", "Path Dependence & Institutional Change", "", 1, []),

  (2, "経済学", "開発経済学", "Development Economics", "", 2, ["Sen", "Banerjee"]),
  (3, "開発経済学", "ランダム化比較試験・RCT", "RCT & Field Experiments", "", 1, []),
  (3, "開発経済学", "ケイパビリティアプローチ", "Capability Approach", "", 1, []),

  (2, "経済学", "情報・ゲーム理論", "Information & Game Theory", "", 2, ["Nash", "Akerlof"]),
  (3, "情報・ゲーム理論", "ゲーム理論・均衡概念", "Game Theory & Equilibrium", "", 1, []),
  (3, "情報・ゲーム理論", "情報の非対称性", "Information Asymmetry", "", 1, []),

  # ---- 文化人類学 中分野 → 小分野 ----
  (2, "文化人類学", "医療人類学", "Medical Anthropology", "", 1, ["Kleinman", "Farmer"]),
  (3, "医療人類学", "病いの語り・説明モデル", "Illness Narratives & Explanatory Models", "", 1, []),
  (3, "医療人類学", "グローバルヘルス・構造的暴力", "Global Health & Structural Violence", "", 1, []),

  (2, "文化人類学", "象徴人類学", "Symbolic Anthropology", "", 1, ["Turner", "Geertz", "Douglas"]),
  (3, "象徴人類学", "儀礼・リミナリティ", "Ritual & Liminality", "", 1, []),
  (3, "象徴人類学", "シック・ディスクリプション", "Thick Description", "", 1, []),
  (3, "象徴人類学", "汚染・タブー・象徴秩序", "Pollution, Taboo & Symbolic Order", "", 2, []),

  (2, "文化人類学", "経済人類学", "Economic Anthropology", "", 2, ["Mauss", "Polanyi"]),
  (3, "経済人類学", "贈与・互酬性", "Gift & Reciprocity", "", 1, []),
  (3, "経済人類学", "非公式経済・モラルエコノミー", "Informal Economy & Moral Economy", "", 2, []),

  (2, "文化人類学", "政治人類学", "Political Anthropology", "", 2, ["Clastres", "Scott"]),
  (3, "政治人類学", "国家・権力・抵抗", "State, Power & Resistance", "", 1, []),

  (2, "文化人類学", "感覚・物質文化研究", "Sensory & Material Culture Studies", "", 1, ["Miller", "Ingold"]),
  (3, "感覚・物質文化研究", "マテリアリティ・モノ論", "Materiality & Thing Theory", "", 1, []),
  (3, "感覚・物質文化研究", "身体・感覚・知覚の人類学", "Anthropology of Body & Senses", "", 1, []),
],

# ================================================================
# 自然科学 / natural_discovery
# ================================================================
"natural_discovery": [
  # ---- 大分野 ----
  (1, None, "生態学", "Ecology",
   "生物と環境の相互作用・生物多様性・生態系機能を研究する学問。",
   1, ["Annual Review of Ecology", "Ecology"]),
  (1, None, "物理学", "Physics",
   "物質・エネルギー・時空の基本法則を研究する学問。",
   1, ["Physical Review Letters", "Reviews of Modern Physics"]),
  (1, None, "化学", "Chemistry",
   "物質の構造・性質・変化・合成を研究する学問。",
   2, ["JACS", "Nature Chemistry"]),
  (1, None, "生物学", "Biology",
   "生命現象・進化・分子機構を研究する学問（生態学を除く）。",
   1, ["Cell", "Nature"]),
  (1, None, "地球科学", "Earth Sciences",
   "地球の構造・気候・地質・海洋・大気を研究する学問。",
   2, ["EPSL"]),
  (1, None, "天文学・宇宙物理学", "Astronomy & Astrophysics",
   "宇宙・天体・宇宙論を研究する学問。",
   2, ["ApJ", "Annual Review of Astronomy"]),
  (1, None, "数学", "Mathematics",
   "抽象的構造・論理・証明を研究する純粋・応用数学。",
   2, ["Annals of Mathematics"]),

  # ---- 生態学 中分野 → 小分野 (DB実値と一致) ----
  (2, "生態学", "生態系生態学", "Ecosystem Ecology",
   "物質循環・エネルギーフロー・生態系サービスを研究する領域。",
   1, ["Odum", "Likens"]),
  (3, "生態系生態学", "生態系生態学", "Ecosystem Ecology", "", 1, []),
  (3, "生態系生態学", "地球システム生態学", "Earth System Ecology", "", 1, []),
  (3, "生態系生態学", "微生物生態学", "Microbial Ecology", "", 1, []),

  (2, "生態学", "群集生態学", "Community Ecology",
   "種間相互作用・競争・捕食・多様性維持機構を研究する領域。",
   1, ["MacArthur", "Wilson"]),
  (3, "群集生態学", "群集生態学", "Community Ecology", "", 1, []),
  (3, "群集生態学", "生物多様性科学", "Biodiversity Science", "", 1, []),

  (2, "生態学", "個体群生態学", "Population Ecology",
   "個体群動態・成長・絶滅・侵入を研究する領域。",
   1, ["Lotka-Volterra", "May"]),
  (3, "個体群生態学", "個体群生態学", "Population Ecology", "", 1, []),

  (2, "生態学", "進化生態学", "Evolutionary Ecology",
   "自然選択・種分化・適応・系統進化を研究する領域。",
   1, ["Darwin", "Hamilton", "Mayr"]),
  (3, "進化生態学", "進化生態学", "Evolutionary Ecology", "", 1, []),
  (3, "進化生態学", "行動生態学", "Behavioral Ecology", "", 1, []),
  (3, "進化生態学", "理論生態学", "Theoretical Ecology", "", 1, []),

  (2, "生態学", "保全生態学", "Conservation Ecology",
   "絶滅危惧種・生息地保全・回復生態学を研究する領域。",
   1, ["Soulé", "Wilcox"]),
  (3, "保全生態学", "保全生態学", "Conservation Ecology", "", 1, []),
  (3, "保全生態学", "景観生態学", "Landscape Ecology", "", 1, []),
  (3, "保全生態学", "生物地理学", "Biogeography", "", 2, []),
  (3, "保全生態学", "応用生態学", "Applied Ecology", "", 2, []),

  # ---- 物理学 中分野 → 小分野 ----
  (2, "物理学", "量子力学・量子情報", "Quantum Mechanics & Quantum Information",
   "量子現象・量子コンピュータ・量子通信。",
   1, ["Dirac", "Feynman", "Nielsen"]),
  (3, "量子力学・量子情報", "量子情報・量子計算", "Quantum Information & Computing", "", 1, []),
  (3, "量子力学・量子情報", "量子場理論", "Quantum Field Theory", "", 1, []),
  (3, "量子力学・量子情報", "量子光学", "Quantum Optics", "", 2, []),

  (2, "物理学", "凝縮系物理学", "Condensed Matter Physics",
   "固体・液体・超伝導・トポロジカル物質。",
   2, ["Landau", "Anderson"]),
  (3, "凝縮系物理学", "超伝導・超流動", "Superconductivity & Superfluidity", "", 1, []),
  (3, "凝縮系物理学", "トポロジカル物質", "Topological Materials", "", 1, []),
  (3, "凝縮系物理学", "相転移・臨界現象", "Phase Transitions & Critical Phenomena", "", 1, []),

  (2, "物理学", "素粒子物理学", "Particle Physics",
   "素粒子・標準模型・ヒッグス機構。",
   2, ["Weinberg", "Glashow"]),
  (3, "素粒子物理学", "標準模型・素粒子論", "Standard Model & Particle Theory", "", 1, []),
  (3, "素粒子物理学", "ニュートリノ物理学", "Neutrino Physics", "", 2, []),

  (2, "物理学", "非線形物理学・複雑系", "Nonlinear Physics & Complex Systems",
   "カオス・自己組織化・創発・フラクタル。",
   1, ["Lorenz", "Prigogine"]),
  (3, "非線形物理学・複雑系", "カオス・動力学系", "Chaos & Dynamical Systems", "", 1, []),
  (3, "非線形物理学・複雑系", "自己組織化・創発", "Self-Organization & Emergence", "", 1, []),
  (3, "非線形物理学・複雑系", "ネットワーク科学", "Network Science", "", 1, []),

  (2, "物理学", "相対性理論・重力", "Relativity & Gravity",
   "時空・重力波・ブラックホール。",
   2, ["Einstein", "Hawking"]),
  (3, "相対性理論・重力", "一般相対性理論・重力波", "General Relativity & Gravitational Waves", "", 1, []),
  (3, "相対性理論・重力", "宇宙論・ダークマター", "Cosmology & Dark Matter", "", 1, []),

  (2, "物理学", "統計力学・熱力学", "Statistical Mechanics & Thermodynamics",
   "系の統計的性質・エントロピー・相転移。",
   2, ["Boltzmann", "Gibbs"]),
  (3, "統計力学・熱力学", "統計力学・情報エントロピー", "Statistical Mechanics & Information Entropy", "", 1, []),

  # ---- 生物学 中分野 → 小分野 ----
  (2, "生物学", "分子生物学・ゲノミクス", "Molecular Biology & Genomics",
   "DNA・RNA・タンパク質・ゲノム解析。",
   1, ["Crick", "Sanger"]),
  (3, "分子生物学・ゲノミクス", "ゲノミクス・エピゲノミクス", "Genomics & Epigenomics", "", 1, []),
  (3, "分子生物学・ゲノミクス", "RNAi・遺伝子発現制御", "Gene Regulation & RNAi", "", 1, []),
  (3, "分子生物学・ゲノミクス", "タンパク質構造・プロテオミクス", "Protein Structure & Proteomics", "", 1, []),

  (2, "生物学", "神経科学", "Neuroscience",
   "神経系・脳機能・シナプス可塑性・意識。",
   1, ["Cajal", "Kandel"]),
  (3, "神経科学", "シナプス可塑性・学習・記憶", "Synaptic Plasticity, Learning & Memory", "", 1, []),
  (3, "神経科学", "神経回路・コネクトーム", "Neural Circuits & Connectome", "", 1, []),
  (3, "神経科学", "計算論的神経科学", "Computational Neuroscience", "", 1, []),
  (3, "神経科学", "神経変性疾患・精神疾患の神経基盤", "Neurodegeneration & Psychiatric Neuroscience", "", 1, []),

  (2, "生物学", "進化生物学", "Evolutionary Biology",
   "自然選択・種分化・進化ゲノミクス。",
   1, ["Darwin", "Hamilton"]),
  (3, "進化生物学", "自然選択・適応進化", "Natural Selection & Adaptive Evolution", "", 1, []),
  (3, "進化生物学", "分子進化・系統推定", "Molecular Evolution & Phylogenetics", "", 1, []),

  (2, "生物学", "細胞生物学", "Cell Biology", "", 1, ["Alberts"]),
  (3, "細胞生物学", "細胞シグナル伝達", "Cell Signaling", "", 1, []),
  (3, "細胞生物学", "細胞周期・アポトーシス", "Cell Cycle & Apoptosis", "", 1, []),

  (2, "生物学", "免疫学", "Immunology", "", 2, ["Burnet", "Jerne"]),
  (3, "免疫学", "自然免疫・獲得免疫", "Innate & Adaptive Immunity", "", 1, []),
  (3, "免疫学", "自己免疫・免疫寛容", "Autoimmunity & Immune Tolerance", "", 1, []),

  # ---- 地球科学 中分野 → 小分野 ----
  (2, "地球科学", "気候科学", "Climate Science", "", 1, ["IPCC", "Hansen"]),
  (3, "気候科学", "気候変動・温暖化機構", "Climate Change & Global Warming", "", 1, []),
  (3, "気候科学", "大気・海洋相互作用", "Atmosphere-Ocean Interaction", "", 1, []),
  (3, "気候科学", "古気候学", "Paleoclimatology", "", 2, []),

  (2, "地球科学", "地質学・構造地質学", "Geology & Tectonics", "", 2, ["Wegener"]),
  (3, "地質学・構造地質学", "プレートテクトニクス", "Plate Tectonics", "", 1, []),
  (3, "地質学・構造地質学", "地震学・火山学", "Seismology & Volcanology", "", 1, []),

  # ---- 天文学 中分野 → 小分野 ----
  (2, "天文学・宇宙物理学", "宇宙論・ダークエネルギー", "Cosmology & Dark Energy",
   "宇宙の起源・膨張・暗黒エネルギー・CMB。",
   1, ["Hubble", "Penzias & Wilson"]),
  (3, "宇宙論・ダークエネルギー", "宇宙の大規模構造", "Large-Scale Structure of Universe", "", 1, []),
  (3, "宇宙論・ダークエネルギー", "インフレーション宇宙論", "Inflationary Cosmology", "", 1, []),

  (2, "天文学・宇宙物理学", "恒星物理・銀河天文学", "Stellar Physics & Galactic Astronomy",
   "恒星の進化・銀河形成・ブラックホール。",
   2, ["Chandrasekhar"]),
  (3, "恒星物理・銀河天文学", "恒星進化・超新星", "Stellar Evolution & Supernovae", "", 1, []),
  (3, "恒星物理・銀河天文学", "系外惑星・惑星形成", "Exoplanets & Planet Formation", "", 1, []),

  # ---- 数学 中分野 → 小分野 ----
  (2, "数学", "代数学・数論", "Algebra & Number Theory",
   "群・環・体・素数・楕円曲線。",
   2, ["Galois", "Euler"]),
  (3, "代数学・数論", "代数幾何学", "Algebraic Geometry", "", 1, []),
  (3, "代数学・数論", "整数論・素数分布", "Number Theory & Prime Distribution", "", 1, []),

  (2, "数学", "確率論・統計学", "Probability & Statistics",
   "確率・確率過程・推定・ベイズ推論。",
   1, ["Kolmogorov", "Fisher"]),
  (3, "確率論・統計学", "ベイズ推論", "Bayesian Inference", "", 1, []),
  (3, "確率論・統計学", "確率過程・ランダムウォーク", "Stochastic Processes & Random Walk", "", 1, []),
  (3, "確率論・統計学", "因果推論", "Causal Inference", "", 1, []),

  (2, "数学", "位相幾何学・幾何学", "Topology & Geometry",
   "多様体・ホモトピー・リーマン幾何。",
   2, ["Poincaré", "Riemann"]),
  (3, "位相幾何学・幾何学", "代数的位相幾何学", "Algebraic Topology", "", 1, []),
  (3, "位相幾何学・幾何学", "微分幾何学・リーマン幾何", "Differential Geometry", "", 1, []),

  (2, "数学", "最適化・応用数学", "Optimization & Applied Mathematics",
   "線形計画・変分法・偏微分方程式・数値解析。",
   1, ["Dantzig", "Nash"]),
  (3, "最適化・応用数学", "凸最適化・線形計画", "Convex Optimization", "", 1, []),
  (3, "最適化・応用数学", "偏微分方程式論", "Partial Differential Equations", "", 1, []),
  (3, "最適化・応用数学", "数値解析・シミュレーション", "Numerical Analysis & Simulation", "", 1, []),
],

# ================================================================
# 人文学 / humanities_concept
# ================================================================
"humanities_concept": [
  # ---- 大分野 ----
  (1, None, "哲学", "Philosophy",
   "存在・認識・倫理・言語・論理の根本問題を研究する学問。",
   1, ["Stanford Encyclopedia of Philosophy"]),
  (1, None, "歴史学", "History",
   "過去の人間活動・事件・構造を史料に基づき研究する学問。",
   2, ["American Historical Review"]),
  (1, None, "言語学", "Linguistics",
   "言語の構造・意味・使用・変化・習得を研究する学問。",
   1, ["Language", "Annual Review of Linguistics"]),
  (1, None, "文学・文芸批評", "Literary Studies",
   "文学作品の解釈・批評・理論・比較研究を行う学問。",
   3, ["PMLA"]),
  (1, None, "宗教学・宗教哲学", "Religious Studies",
   "宗教現象・神学・神話・儀礼・比較宗教を研究する学問。",
   2, ["History of Religions"]),
  (1, None, "考古学・先史学", "Archaeology & Prehistory",
   "物質的遺物から過去の人間社会を研究する学問。",
   2, ["Journal of Archaeological Method"]),
  (1, None, "美学・芸術哲学", "Aesthetics & Philosophy of Art",
   "美・崇高・芸術的経験・批評の哲学的基礎を研究する学問。",
   1, ["Journal of Aesthetics and Art Criticism"]),

  # ---- 哲学 中分野 → 小分野 ----
  (2, "哲学", "存在論・形而上学", "Ontology & Metaphysics", "", 1, ["Aristotle", "Heidegger"]),
  (3, "存在論・形而上学", "存在論・オントロジー", "Ontology", "", 1, []),
  (3, "存在論・形而上学", "時間・持続・変化の哲学", "Philosophy of Time & Change", "", 1, []),
  (3, "存在論・形而上学", "因果論・決定論・自由意志", "Causation, Determinism & Free Will", "", 1, []),
  (3, "存在論・形而上学", "心の哲学・クオリア", "Philosophy of Mind & Qualia", "", 1, []),

  (2, "哲学", "認識論", "Epistemology", "", 1, ["Descartes", "Hume", "Gettier"]),
  (3, "認識論", "知識・正当化・真理", "Knowledge, Justification & Truth", "", 1, []),
  (3, "認識論", "社会認識論・証言認識論", "Social & Testimonial Epistemology", "", 1, []),
  (3, "認識論", "科学哲学・理論変化", "Philosophy of Science & Theory Change", "", 1, []),
  (3, "認識論", "現象学・フッサール・ハイデガー", "Phenomenology", "", 1, []),

  (2, "哲学", "倫理学", "Ethics", "", 1, ["Kant", "Mill", "Rawls"]),
  (3, "倫理学", "規範倫理学・義務論・功利主義", "Normative Ethics: Deontology & Utilitarianism", "", 1, []),
  (3, "倫理学", "徳倫理学・実践的知恵", "Virtue Ethics & Practical Wisdom", "", 1, []),
  (3, "倫理学", "応用倫理学・生命倫理", "Applied Ethics & Bioethics", "", 1, []),
  (3, "倫理学", "ケアの倫理・フェミニスト倫理", "Ethics of Care & Feminist Ethics", "", 1, []),
  (3, "倫理学", "メタ倫理学", "Metaethics", "", 2, []),

  (2, "哲学", "言語哲学", "Philosophy of Language", "", 1, ["Frege", "Wittgenstein", "Austin"]),
  (3, "言語哲学", "意味・指示・真理条件", "Meaning, Reference & Truth Conditions", "", 1, []),
  (3, "言語哲学", "言語行為論・語用論的哲学", "Speech Act Theory", "", 1, []),
  (3, "言語哲学", "後期ウィトゲンシュタイン・言語ゲーム", "Language Games & Forms of Life", "", 1, []),

  (2, "哲学", "政治哲学", "Political Philosophy", "", 1, ["Rawls", "Nozick", "Arendt"]),
  (3, "政治哲学", "正義論・分配的正義", "Theory of Justice", "", 1, []),
  (3, "政治哲学", "民主主義論・熟議民主主義", "Democracy & Deliberation", "", 1, []),
  (3, "政治哲学", "承認・アイデンティティ政治", "Recognition & Identity Politics", "", 1, []),

  (2, "哲学", "大陸哲学", "Continental Philosophy", "", 1, ["Hegel", "Nietzsche", "Foucault"]),
  (3, "大陸哲学", "批判理論・フランクフルト学派", "Critical Theory & Frankfurt School", "", 1, []),
  (3, "大陸哲学", "ポスト構造主義・フーコー・デリダ", "Post-Structuralism", "", 1, []),
  (3, "大陸哲学", "実存主義・ハイデガー・サルトル", "Existentialism", "", 2, []),

  # ---- 言語学 中分野 → 小分野 ----
  (2, "言語学", "統語論・形式言語学", "Syntax & Formal Linguistics", "", 2, ["Chomsky"]),
  (3, "統語論・形式言語学", "生成文法・ミニマリスト・プログラム", "Generative Grammar & Minimalist Program", "", 1, []),
  (3, "統語論・形式言語学", "依存文法・LFG・HPSG", "Dependency Grammar & LFG", "", 2, []),

  (2, "言語学", "意味論・語用論", "Semantics & Pragmatics", "", 1, ["Grice", "Levinson"]),
  (3, "意味論・語用論", "形式意味論・モデル理論的意味論", "Formal & Model-Theoretic Semantics", "", 1, []),
  (3, "意味論・語用論", "語用論・関連性理論", "Pragmatics & Relevance Theory", "", 1, []),
  (3, "意味論・語用論", "談話分析・テクスト言語学", "Discourse Analysis & Text Linguistics", "", 1, []),

  (2, "言語学", "社会言語学", "Sociolinguistics", "", 1, ["Labov", "Gumperz"]),
  (3, "社会言語学", "言語変異・変化", "Language Variation & Change", "", 1, []),
  (3, "社会言語学", "多言語主義・コードスイッチング", "Multilingualism & Code-Switching", "", 1, []),
  (3, "社会言語学", "言語イデオロギー・言語政策", "Language Ideology & Policy", "", 1, []),

  (2, "言語学", "認知言語学", "Cognitive Linguistics", "", 1, ["Lakoff", "Langacker"]),
  (3, "認知言語学", "メタファー・メトニミー理論", "Metaphor & Metonymy Theory", "", 1, []),
  (3, "認知言語学", "身体化認知・アフォーダンス言語学", "Embodied Cognition & Affordance", "", 1, []),
  (3, "認知言語学", "フレーム意味論・構文文法", "Frame Semantics & Construction Grammar", "", 1, []),

  (2, "言語学", "歴史言語学・類型論", "Historical Linguistics & Typology", "", 2, ["Greenberg"]),
  (3, "歴史言語学・類型論", "言語変化・言語接触", "Language Change & Contact", "", 1, []),
  (3, "歴史言語学・類型論", "言語類型論・普遍性", "Linguistic Typology & Universals", "", 1, []),

  # ---- 歴史学 中分野 → 小分野 ----
  (2, "歴史学", "社会史・文化史", "Social & Cultural History", "", 1, ["Ginzburg", "Natalie Davis"]),
  (3, "社会史・文化史", "日常生活史・ミクロ史", "Everyday History & Microhistory", "", 1, []),
  (3, "社会史・文化史", "労働史・社会運動史", "Labor History & Social Movements", "", 1, []),
  (3, "社会史・文化史", "文化史・メンタリテ", "Cultural History & Mentalités", "", 1, []),

  (2, "歴史学", "グローバル史・世界史", "Global & World History", "", 1, ["Bayly", "Manning"]),
  (3, "グローバル史・世界史", "帝国史・植民地史", "Imperial & Colonial History", "", 1, []),
  (3, "グローバル史・世界史", "交流史・コネクテッドヒストリー", "Connected History & Entangled History", "", 1, []),
  (3, "グローバル史・世界史", "移民・ディアスポラ史", "Migration & Diaspora History", "", 1, []),

  (2, "歴史学", "歴史理論・史学史", "Theory of History & Historiography", "", 2, ["White", "Collingwood"]),
  (3, "歴史理論・史学史", "ナラティブ・歴史的説明", "Narrative & Historical Explanation", "", 1, []),
  (3, "歴史理論・史学史", "記憶・アーカイブ・歴史意識", "Memory, Archive & Historical Consciousness", "", 1, []),

  (2, "歴史学", "ポストコロニアル史", "Postcolonial History", "", 1, ["Spivak", "Chakrabarty"]),
  (3, "ポストコロニアル史", "サバルタン研究", "Subaltern Studies", "", 1, []),
  (3, "ポストコロニアル史", "脱植民地化・ポストコロニアル批評", "Decolonization & Postcolonial Critique", "", 1, []),

  # ---- 美学 中分野 → 小分野 ----
  (2, "美学・芸術哲学", "美と崇高の美学", "Aesthetics of Beauty & Sublime", "", 1, ["Kant", "Burke"]),
  (3, "美と崇高の美学", "カントの美学・崇高論", "Kantian Aesthetics & the Sublime", "", 1, []),
  (3, "美と崇高の美学", "美的経験・趣味判断", "Aesthetic Experience & Taste", "", 1, []),

  (2, "美学・芸術哲学", "芸術定義・批評理論", "Definition of Art & Critical Theory", "", 1, ["Danto", "Dickie"]),
  (3, "芸術定義・批評理論", "芸術の制度論・芸術世界", "Institutional Theory of Art & Artworld", "", 1, []),
  (3, "芸術定義・批評理論", "表現・再現・図像論", "Expression, Representation & Iconology", "", 1, []),

  (2, "美学・芸術哲学", "身体・パフォーマンスの美学", "Aesthetics of Body & Performance", "", 1, ["Schechner"]),
  (3, "身体・パフォーマンスの美学", "パフォーマンス美学・演劇論", "Performance Aesthetics & Theatre Theory", "", 1, []),
  (3, "身体・パフォーマンスの美学", "身体・感覚・情動の美学", "Somaesthetics & Affect", "", 1, []),
],

# ================================================================
# 工学 / engineering_method
# ================================================================
"engineering_method": [
  # ---- 大分野 ----
  (1, None, "情報工学・コンピュータ科学", "Computer Science & Engineering",
   "アルゴリズム・AI・ソフトウェア・ネットワークを研究する学問。",
   1, ["CACM", "IEEE Transactions", "ACM"]),
  (1, None, "機械工学", "Mechanical Engineering",
   "熱流体・機械設計・ロボット・製造プロセスを研究する学問。",
   2, ["ASME Journal"]),
  (1, None, "電気・電子工学", "Electrical & Electronic Engineering",
   "回路・電力・通信・半導体・センサーを研究する学問。",
   2, ["IEEE Transactions"]),
  (1, None, "システム工学・制御工学", "Systems & Control Engineering",
   "複雑システムの設計・制御・最適化・信頼性を研究する学問。",
   1, ["Systems Engineering Journal"]),
  (1, None, "建築・土木工学", "Architecture & Civil Engineering",
   "構造・材料・都市基盤・環境設計を研究する学問。",
   3, ["ASCE"]),
  (1, None, "化学工学", "Chemical Engineering",
   "化学反応・プロセス設計・輸送現象を研究する学問。",
   3, ["AIChE Journal"]),
  (1, None, "バイオエンジニアリング", "Bioengineering",
   "医療機器・バイオインフォ・合成生物学を研究する学問。",
   1, ["Nature Biotechnology"]),
  (1, None, "環境・エネルギー工学", "Environmental & Energy Engineering",
   "廃水処理・大気汚染・再生可能エネルギーを研究する学問。",
   2, ["Environmental Science & Technology"]),

  # ---- 情報工学 中分野 → 小分野 ----
  (2, "情報工学・コンピュータ科学", "機械学習・AI", "Machine Learning & AI",
   "学習アルゴリズム・深層学習・強化学習・自然言語処理。",
   1, ["LeCun", "Bengio", "Hinton"]),
  (3, "機械学習・AI", "深層学習・ニューラルネットワーク", "Deep Learning & Neural Networks", "", 1, []),
  (3, "機械学習・AI", "強化学習・逐次意思決定", "Reinforcement Learning", "", 1, []),
  (3, "機械学習・AI", "自然言語処理・大規模言語モデル", "NLP & Large Language Models", "", 1, []),
  (3, "機械学習・AI", "コンピュータビジョン・画像認識", "Computer Vision & Image Recognition", "", 1, []),
  (3, "機械学習・AI", "説明可能AI・信頼できるAI", "Explainable & Trustworthy AI", "", 1, []),
  (3, "機械学習・AI", "グラフニューラルネットワーク", "Graph Neural Networks", "", 1, []),

  (2, "情報工学・コンピュータ科学", "アルゴリズム・計算理論", "Algorithms & Theory",
   "計算複雑性・アルゴリズム設計・数理最適化。",
   2, ["Knuth", "Sipser"]),
  (3, "アルゴリズム・計算理論", "近似アルゴリズム・組合せ最適化", "Approximation & Combinatorial Optimization", "", 1, []),
  (3, "アルゴリズム・計算理論", "計算複雑性・P対NP", "Computational Complexity", "", 1, []),
  (3, "アルゴリズム・計算理論", "ランダムアルゴリズム・オンラインアルゴリズム", "Randomized & Online Algorithms", "", 2, []),

  (2, "情報工学・コンピュータ科学", "ソフトウェア工学", "Software Engineering",
   "ソフトウェア設計・アーキテクチャ・テスト・プロセス。",
   2, ["Fowler", "Brooks"]),
  (3, "ソフトウェア工学", "アーキテクチャパターン・設計原則", "Architecture Patterns & Design Principles", "", 1, []),
  (3, "ソフトウェア工学", "アジャイル・DevOps・継続的デリバリー", "Agile, DevOps & Continuous Delivery", "", 1, []),
  (3, "ソフトウェア工学", "形式検証・プログラム解析", "Formal Verification & Program Analysis", "", 2, []),

  (2, "情報工学・コンピュータ科学", "データベース・情報検索", "Databases & Information Retrieval",
   "データモデル・クエリ最適化・検索エンジン。",
   2, ["Codd", "Gray"]),
  (3, "データベース・情報検索", "リレーショナルDB・SQL最適化", "Relational DB & Query Optimization", "", 1, []),
  (3, "データベース・情報検索", "分散DB・NoSQL・NewSQL", "Distributed DB & NoSQL", "", 1, []),
  (3, "データベース・情報検索", "情報検索・推薦システム", "Information Retrieval & Recommendation", "", 1, []),

  (2, "情報工学・コンピュータ科学", "HCI・インタラクション設計", "HCI & Interaction Design",
   "ユーザビリティ・インタフェース設計・認知工学。",
   1, ["Norman", "Card"]),
  (3, "HCI・インタラクション設計", "ユーザビリティ・ユーザーリサーチ", "Usability & User Research", "", 1, []),
  (3, "HCI・インタラクション設計", "拡張・複合現実 (AR/MR/VR)", "AR, MR & VR", "", 1, []),
  (3, "HCI・インタラクション設計", "身体化インタラクション・具現化設計", "Embodied Interaction", "", 1, []),

  (2, "情報工学・コンピュータ科学", "セキュリティ・暗号理論", "Security & Cryptography",
   "暗号理論・認証・プロトコル・サイバーセキュリティ。",
   1, ["Diffie & Hellman", "Rivest"]),
  (3, "セキュリティ・暗号理論", "公開鍵暗号・格子暗号", "Public-Key & Lattice-Based Cryptography", "", 1, []),
  (3, "セキュリティ・暗号理論", "ゼロ知識証明・秘密計算", "Zero-Knowledge Proofs & Secure Computation", "", 1, []),
  (3, "セキュリティ・暗号理論", "サイバーセキュリティ・脆弱性分析", "Cybersecurity & Vulnerability Analysis", "", 1, []),

  (2, "情報工学・コンピュータ科学", "ネットワーク・分散システム", "Networks & Distributed Systems",
   "プロトコル・P2P・クラウド・分散アルゴリズム。",
   2, ["Lamport", "Cerf"]),
  (3, "ネットワーク・分散システム", "分散コンセンサス・Byzantine耐障害性", "Distributed Consensus & BFT", "", 1, []),
  (3, "ネットワーク・分散システム", "クラウドコンピューティング・マイクロサービス", "Cloud Computing & Microservices", "", 1, []),

  # ---- システム工学 中分野 → 小分野 ----
  (2, "システム工学・制御工学", "制御理論", "Control Theory",
   "フィードバック制御・最適制御・適応制御。",
   2, ["Bode", "Kalman"]),
  (3, "制御理論", "古典制御・周波数領域設計", "Classical Control & Frequency Domain", "", 2, []),
  (3, "制御理論", "最適制御・カルマンフィルタ", "Optimal Control & Kalman Filter", "", 1, []),
  (3, "制御理論", "モデル予測制御 (MPC)", "Model Predictive Control", "", 1, []),

  (2, "システム工学・制御工学", "ロボティクス・自律システム", "Robotics & Autonomous Systems",
   "ロボット機構・制御・センサー融合・自律移動。",
   1, ["Craig", "Siciliano"]),
  (3, "ロボティクス・自律システム", "自律移動ロボット・SLAM", "Autonomous Robots & SLAM", "", 1, []),
  (3, "ロボティクス・自律システム", "ヒューマンロボットインタラクション", "Human-Robot Interaction", "", 1, []),
  (3, "ロボティクス・自律システム", "ソフトロボティクス", "Soft Robotics", "", 1, []),

  (2, "システム工学・制御工学", "オペレーションズ・リサーチ", "Operations Research",
   "線形計画・整数計画・ネットワーク最適化・待行列。",
   2, ["Dantzig", "Bellman"]),
  (3, "オペレーションズ・リサーチ", "整数計画・組合せ最適化", "Integer Programming & Combinatorial Optimization", "", 1, []),
  (3, "オペレーションズ・リサーチ", "待行列理論・シミュレーション", "Queueing Theory & Simulation", "", 2, []),

  # ---- バイオエンジニアリング 中分野 → 小分野 ----
  (2, "バイオエンジニアリング", "合成生物学", "Synthetic Biology",
   "遺伝回路設計・代謝工学・CRISPR応用。",
   1, ["Venter", "Doudna"]),
  (3, "合成生物学", "CRISPR・ゲノム編集", "CRISPR & Genome Editing", "", 1, []),
  (3, "合成生物学", "代謝工学・バイオものづくり", "Metabolic Engineering & Biomanufacturing", "", 1, []),

  (2, "バイオエンジニアリング", "バイオインフォマティクス", "Bioinformatics",
   "ゲノム解析・タンパク質構造予測・パスウェイ解析。",
   1, ["BLAST", "AlphaFold"]),
  (3, "バイオインフォマティクス", "シングルセル解析・マルチオミクス", "Single-Cell & Multi-Omics Analysis", "", 1, []),
  (3, "バイオインフォマティクス", "タンパク質構造予測・ドッキング", "Protein Structure Prediction & Docking", "", 1, []),

  (2, "バイオエンジニアリング", "組織工学・再生医療", "Tissue Engineering & Regenerative Medicine",
   "スキャフォールド・幹細胞・オルガノイド。",
   1, ["Langer", "Vacanti"]),
  (3, "組織工学・再生医療", "幹細胞工学・iPS細胞", "Stem Cell Engineering & iPS", "", 1, []),
  (3, "組織工学・再生医療", "オルガノイド・臓器チップ", "Organoids & Organ-on-a-Chip", "", 1, []),

  # ---- 環境・エネルギー工学 中分野 → 小分野 ----
  (2, "環境・エネルギー工学", "再生可能エネルギー", "Renewable Energy",
   "太陽光・風力・水素・エネルギー貯蔵。",
   1, ["IRENA"]),
  (3, "再生可能エネルギー", "太陽光発電・薄膜太陽電池", "Photovoltaics & Thin-Film Solar", "", 1, []),
  (3, "再生可能エネルギー", "風力発電・洋上風力", "Wind Power & Offshore Wind", "", 1, []),
  (3, "再生可能エネルギー", "水素製造・燃料電池", "Hydrogen Production & Fuel Cells", "", 1, []),

  (2, "環境・エネルギー工学", "廃水・廃棄物処理", "Water & Waste Treatment",
   "廃水処理技術・廃棄物管理・循環経済。",
   2, ["EST"]),
  (3, "廃水・廃棄物処理", "膜処理・高度水処理", "Membrane & Advanced Water Treatment", "", 2, []),
  (3, "廃水・廃棄物処理", "バイオレメディエーション", "Bioremediation", "", 2, []),
],

# ================================================================
# 芸術 / arts_question
# ================================================================
"arts_question": [
  # ---- 大分野 ----
  (1, None, "美術・視覚芸術", "Visual Arts",
   "絵画・彫刻・版画・インスタレーション・写真の制作と批評。",
   1, ["October", "Artforum"]),
  (1, None, "音楽", "Music",
   "作曲・演奏・音楽学・音楽理論・民族音楽学を含む学問。",
   2, ["JAMS"]),
  (1, None, "デザイン", "Design",
   "グラフィック・プロダクト・建築・UX・社会デザイン。",
   1, ["Design Studies"]),
  (1, None, "映像・映画", "Film & Moving Image",
   "映画・映像・アニメーション・ゲームの制作と批評。",
   2, ["Cinema Journal", "Screen"]),
  (1, None, "演劇・パフォーマンス", "Theatre & Performance",
   "演劇・ダンス・パフォーマンスアートの実践と理論。",
   2, ["Theatre Journal", "TDR"]),
  (1, None, "建築デザイン", "Architectural Design",
   "建築の造形・理念・歴史・批評（美学的側面）。",
   2, ["Journal of Architecture"]),
  (1, None, "芸術理論・批評", "Art Theory & Criticism",
   "芸術的価値・解釈・美学・批評理論の横断的研究。",
   1, ["Art Bulletin", "Critical Inquiry"]),
  (1, None, "メディアアート・デジタル表現", "Media Art & Digital Expression",
   "電子・デジタル・インタラクティブ・ネットアートの実践と理論。",
   1, ["Leonardo"]),

  # ---- 美術 中分野 → 小分野 ----
  (2, "美術・視覚芸術", "現代美術", "Contemporary Art",
   "1960年代以降の概念・プロセス・インスタレーション・社会的実践。",
   1, ["Kosuth", "Duchamp"]),
  (3, "現代美術", "コンセプチュアルアート", "Conceptual Art", "", 1, []),
  (3, "現代美術", "インスタレーション・場所特定型アート", "Installation & Site-Specific Art", "", 1, []),
  (3, "現代美術", "ソーシャリー・エンゲージド・アート", "Socially Engaged Art", "", 1, []),
  (3, "現代美術", "ポストコロニアル・アート", "Postcolonial Art", "", 1, []),

  (2, "美術・視覚芸術", "写真・映像アート", "Photography & Video Art",
   "写真理論・映像インスタレーション・ドキュメンタリー。",
   1, ["Benjamin", "Barthes", "Sontag"]),
  (3, "写真・映像アート", "写真理論・インデックス性", "Photography Theory & Indexicality", "", 1, []),
  (3, "写真・映像アート", "ドキュメンタリー写真・社会的記録", "Documentary Photography", "", 1, []),
  (3, "写真・映像アート", "映像インスタレーション・シングルチャンネル", "Video Installation & Single-Channel", "", 1, []),

  (2, "美術・視覚芸術", "絵画・版画", "Painting & Printmaking", "", 2, ["Greenberg"]),
  (3, "絵画・版画", "抽象表現主義・ミニマリズム", "Abstract Expressionism & Minimalism", "", 1, []),
  (3, "絵画・版画", "具象画・批判的リアリズム", "Figurative Painting & Critical Realism", "", 2, []),

  (2, "美術・視覚芸術", "彫刻・立体造形", "Sculpture & 3D Arts", "", 2, ["Judd", "Serra"]),
  (3, "彫刻・立体造形", "ミニマリスト彫刻・オブジェ", "Minimalist Sculpture & Objects", "", 1, []),
  (3, "彫刻・立体造形", "パブリックアート・都市彫刻", "Public Art & Urban Sculpture", "", 2, []),

  # ---- 音楽 中分野 → 小分野 ----
  (2, "音楽", "音楽理論・作曲", "Music Theory & Composition",
   "和声・対位法・形式・スペクトル楽派・電子音楽。",
   2, ["Schenker", "Messiaen"]),
  (3, "音楽理論・作曲", "調性・和声論", "Tonal Harmony Theory", "", 1, []),
  (3, "音楽理論・作曲", "スペクトル作曲・微分音音楽", "Spectral Composition & Microtonal Music", "", 1, []),
  (3, "音楽理論・作曲", "電子・電気音響音楽", "Electronic & Electroacoustic Music", "", 1, []),

  (2, "音楽", "音楽学・音楽史", "Musicology & Music History",
   "音楽史・音楽テクスト・演奏実践研究。",
   2, ["Taruskin"]),
  (3, "音楽学・音楽史", "ニューミュージコロジー・批評音楽学", "New Musicology & Critical Musicology", "", 1, []),
  (3, "音楽学・音楽史", "歴史的演奏実践・HIP", "Historically Informed Performance", "", 2, []),

  (2, "音楽", "民族音楽学・世界音楽", "Ethnomusicology & World Music",
   "非西洋音楽・音楽文化・フィールドワーク。",
   1, ["Merriam", "Blacking"]),
  (3, "民族音楽学・世界音楽", "サウンドスケープ・音楽地理学", "Soundscape & Music Geography", "", 1, []),
  (3, "民族音楽学・世界音楽", "音楽とアイデンティティ・ディアスポラ", "Music, Identity & Diaspora", "", 1, []),

  (2, "音楽", "ポピュラー音楽研究", "Popular Music Studies",
   "ロック・ヒップホップ・Kポップ・産業構造・ファン文化。",
   1, ["Frith", "Hall"]),
  (3, "ポピュラー音楽研究", "ヒップホップ・ラップ研究", "Hip-Hop & Rap Studies", "", 1, []),
  (3, "ポピュラー音楽研究", "音楽産業・プラットフォーム・ストリーミング", "Music Industry & Streaming Platforms", "", 1, []),
  (3, "ポピュラー音楽研究", "ファンダム・音楽文化研究", "Fandom & Music Culture", "", 1, []),

  # ---- デザイン 中分野 → 小分野 ----
  (2, "デザイン", "インタラクション・UXデザイン", "Interaction & UX Design",
   "人間中心設計・使いやすさ・サービスデザイン。",
   1, ["Norman", "IDEO"]),
  (3, "インタラクション・UXデザイン", "人間中心デザイン・HCD", "Human-Centered Design", "", 1, []),
  (3, "インタラクション・UXデザイン", "サービスデザイン", "Service Design", "", 1, []),
  (3, "インタラクション・UXデザイン", "デザインリサーチ・エスノグラフィー的デザイン", "Design Research & Ethnographic Design", "", 1, []),

  (2, "デザイン", "社会デザイン・トランジションデザイン", "Social & Transition Design",
   "社会課題への創造的アプローチ・共創・フューチャーデザイン。",
   1, ["Manzini", "IDEO"]),
  (3, "社会デザイン・トランジションデザイン", "フューチャーデザイン・投機的デザイン", "Future Design & Speculative Design", "", 1, []),
  (3, "社会デザイン・トランジションデザイン", "コデザイン・参加型デザイン", "Co-design & Participatory Design", "", 1, []),
  (3, "社会デザイン・トランジションデザイン", "サステナブルデザイン・循環設計", "Sustainable & Circular Design", "", 1, []),

  (2, "デザイン", "グラフィック・タイポグラフィ", "Graphic Design & Typography",
   "視覚コミュニケーション・情報デザイン・文字設計。",
   2, ["Müller-Brockmann", "Lupton"]),
  (3, "グラフィック・タイポグラフィ", "情報デザイン・データビジュアライゼーション", "Information Design & Data Visualization", "", 1, []),
  (3, "グラフィック・タイポグラフィ", "タイポグラフィ・文字デザイン", "Typography & Type Design", "", 2, []),

  # ---- 映画 中分野 → 小分野 ----
  (2, "映像・映画", "映画理論・批評", "Film Theory & Criticism",
   "映画的装置・ナラティブ・ジャンル・リアリズム論。",
   1, ["Metz", "Bazin", "Mulvey"]),
  (3, "映画理論・批評", "スペクタトール論・視線の理論", "Spectatorship & Gaze Theory", "", 1, []),
  (3, "映画理論・批評", "ジャンル論・ナラティブ理論", "Genre Theory & Narrative", "", 1, []),
  (3, "映画理論・批評", "世界映画・ポストコロニアル映画論", "World Cinema & Postcolonial Film Theory", "", 1, []),

  (2, "映像・映画", "アニメーション・ゲーム研究", "Animation & Game Studies",
   "アニメーション理論・ゲームスタディーズ・インタラクティブナラティブ。",
   1, ["Manovich", "Juul"]),
  (3, "アニメーション・ゲーム研究", "アニメーション理論・セル・3DCG", "Animation Theory", "", 1, []),
  (3, "アニメーション・ゲーム研究", "ゲームスタディーズ・ルドロジー", "Game Studies & Ludology", "", 1, []),

  # ---- 演劇 中分野 → 小分野 ----
  (2, "演劇・パフォーマンス", "パフォーマンス理論", "Performance Theory",
   "身体・儀礼・社会的パフォーマンス・リミナリティ。",
   1, ["Schechner", "Turner"]),
  (3, "パフォーマンス理論", "パフォーマンス研究・社会的ドラマ", "Performance Studies & Social Drama", "", 1, []),
  (3, "パフォーマンス理論", "ポストドラマ演劇", "Postdramatic Theatre", "", 1, []),

  (2, "演劇・パフォーマンス", "ダンス・動作研究", "Dance & Movement Studies",
   "ダンス理論・振付・身体技法・コレオグラフィー。",
   2, ["Foster"]),
  (3, "ダンス・動作研究", "コンテンポラリーダンス・コレオグラフィー", "Contemporary Dance & Choreography", "", 1, []),
  (3, "ダンス・動作研究", "身体技法・ソマティクス", "Body Techniques & Somatics", "", 1, []),

  # ---- 芸術理論 中分野 → 小分野 ----
  (2, "芸術理論・批評", "ポスト構造主義・批判理論的批評", "Post-Structuralist & Critical Theory",
   "デリダ・フーコー・ボードリヤールの芸術批評応用。",
   1, ["Derrida", "Foucault"]),
  (3, "ポスト構造主義・批判理論的批評", "表象批判・脱構築的美術批評", "Deconstruction & Representation Critique", "", 1, []),
  (3, "ポスト構造主義・批判理論的批評", "スペクタクル論・消費社会と芸術", "Spectacle Theory & Art in Consumer Society", "", 1, []),

  (2, "芸術理論・批評", "フェミニスト・クィア・批評", "Feminist & Queer Art Criticism",
   "ジェンダー・身体・アイデンティティの芸術的表象。",
   1, ["Pollock", "Butler"]),
  (3, "フェミニスト・クィア・批評", "フェミニスト美術史・ジェンダー表象", "Feminist Art History & Gender Representation", "", 1, []),
  (3, "フェミニスト・クィア・批評", "クィア理論・LGBTQ+芸術", "Queer Theory & LGBTQ+ Art", "", 1, []),

  (2, "芸術理論・批評", "マテリアル・感覚的転回", "Material & Sensory Turn",
   "物・マテリアリティ・感覚の芸術論的探究。",
   1, ["Bennett", "Ingold"]),
  (3, "マテリアル・感覚的転回", "新物質主義・事物の力", "New Materialism & Thing Power", "", 1, []),
  (3, "マテリアル・感覚的転回", "触覚・嗅覚・身体感覚の美学", "Haptic, Olfactory & Somatic Aesthetics", "", 1, []),

  # ---- メディアアート 中分野 → 小分野 ----
  (2, "メディアアート・デジタル表現", "インタラクティブアート・ネットアート", "Interactive & Net Art",
   "参加型・インタラクティブ・ネット上の芸術実践。",
   1, ["Ascott", "Lovink"]),
  (3, "インタラクティブアート・ネットアート", "パーティシパトリーアート・コレクティブプラクティス", "Participatory Art", "", 1, []),
  (3, "インタラクティブアート・ネットアート", "AIアート・生成芸術", "AI Art & Generative Art", "", 1, []),

  (2, "メディアアート・デジタル表現", "ニューメディア理論", "New Media Theory",
   "デジタルメディア・インターフェース・データ表現の理論。",
   1, ["Manovich", "Lev"]),
  (3, "ニューメディア理論", "データ美学・コードとしての芸術", "Data Aesthetics & Code Art", "", 1, []),
  (3, "ニューメディア理論", "ポストヒューマン・テクノロジーと身体", "Posthuman & Body-Technology Interface", "", 1, []),
],

}


def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DELETE FROM survey_frame")
    print("既存データを削除しました")

    name_to_id = {}
    rows_to_insert = []

    for domain, entries in FRAMES.items():
        for entry in entries:
            level, parent_name, name, name_en, desc, priority, refs = entry
            uid = str(uuid.uuid4())
            name_to_id[(domain, name)] = uid
            rows_to_insert.append((domain, level, parent_name, name, name_en, desc, priority, refs, uid))

    inserted = 0
    for domain, level, parent_name, name, name_en, desc, priority, refs, uid in rows_to_insert:
        parent_id = None
        if parent_name:
            parent_id = name_to_id.get((domain, parent_name))

        cur.execute("""
            INSERT INTO survey_frame
              (id, domain, level, parent_id, name, name_en, description,
               survey_priority, key_references, survey_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'not_started')
        """, (uid, domain, level, parent_id, name, name_en, desc, priority,
              json.dumps(refs, ensure_ascii=False)))
        inserted += 1

    conn.commit()
    conn.close()
    print(f"投入完了: {inserted} 件")

    conn = sqlite3.connect(DB_PATH)
    domain_names = {
        "social_theory": "社会科学",
        "natural_discovery": "自然科学",
        "humanities_concept": "人文学",
        "engineering_method": "工学",
        "arts_question": "芸術"
    }
    total = 0
    for domain in FRAMES.keys():
        l1 = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=1", (domain,)).fetchone()[0]
        l2 = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=2", (domain,)).fetchone()[0]
        l3 = conn.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=3", (domain,)).fetchone()[0]
        cnt = l1 + l2 + l3
        total += cnt
        print(f"  {domain_names[domain]}: {cnt}件 (大{l1} / 中{l2} / 小{l3})")
    print(f"  合計: {total}件")
    conn.close()


if __name__ == "__main__":
    seed()
