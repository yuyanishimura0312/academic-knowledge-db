"""
Level 4 細目（超詳細サブフィールド）を survey_frame に追加するスクリプト
既存の L1/L2/L3 エントリを保持し、L4 のみ差分追加する。
L4 の parent = L3 の name (同domain内)
"""

import sqlite3, os, uuid, json

DB_PATH = os.path.expanduser("~/projects/research/academic-knowledge-db/academic.db")

# ---------------------------------------------------------------
# L4定義: (parent_l3_name, name, name_en, description, priority)
# ---------------------------------------------------------------

L4 = {

# ================================================================
# 社会科学 / social_theory
# ================================================================
"social_theory": [

  # 認知心理学 > 知覚・注意
  ("知覚・注意", "選択的注意・スポットライト理論", "Selective Attention & Spotlight Theory", "注意の選択的配分・フィルター理論・スポットライトモデル。", 1),
  ("知覚・注意", "特徴統合理論・変化盲", "Feature Integration Theory & Change Blindness", "Treismanの特徴統合・変化盲・非注意性盲目。", 1),
  ("知覚・注意", "多感覚統合・クロスモーダル知覚", "Multisensory Integration & Crossmodal Perception", "視聴覚・体性感覚の統合・マクガーク効果。", 2),
  ("知覚・注意", "予測符号化・ベイズ脳", "Predictive Coding & Bayesian Brain", "Helmholtz-Friston の予測符号化・自由エネルギー原理。", 1),

  # 認知心理学 > 記憶・学習
  ("記憶・学習", "作業記憶・バデリーモデル", "Working Memory & Baddeley Model", "中央実行系・音韻ループ・視空間スケッチパッドの多成分モデル。", 1),
  ("記憶・学習", "エピソード記憶・意味記憶", "Episodic & Semantic Memory", "タルヴィングの多記憶システム・記憶の符号化特定性原理。", 1),
  ("記憶・学習", "手続き記憶・潜在記憶", "Procedural & Implicit Memory", "手続き学習・プライミング・条件付け。", 2),
  ("記憶・学習", "符号化・検索・忘却理論", "Encoding, Retrieval & Forgetting", "処理水準説・転送適切性・忘却曲線・エビングハウス。", 1),
  ("記憶・学習", "文脈依存学習・間隔効果", "Context-Dependent Learning & Spacing Effect", "文脈依存性・間隔学習・分散練習の効果。", 2),

  # 認知心理学 > 判断・意思決定
  ("判断・意思決定", "プロスペクト理論・損失回避", "Prospect Theory & Loss Aversion", "カーネマン・トベルスキーの損失回避・価値関数・確率加重関数。", 1),
  ("判断・意思決定", "二重過程理論 (System 1/2)", "Dual Process Theory", "直感的・分析的処理の二重過程・Kahneman (2011)。", 1),
  ("判断・意思決定", "代表性・利用可能性ヒューリスティクス", "Representativeness & Availability Heuristics", "判断の近道・偏りのカタログ。", 1),
  ("判断・意思決定", "道徳判断・トロッコ問題", "Moral Judgment & Trolley Problem", "功利主義vs義務論的判断・感情の役割・文化差。", 1),
  ("判断・意思決定", "意思決定と感情・ソマティックマーカー仮説", "Decision-Making & Somatic Marker Hypothesis", "ダマジオのソマティックマーカー・感情の意思決定への統合。", 2),

  # 認知心理学 > 認知神経科学
  ("認知神経科学", "前頭前野と実行機能", "Prefrontal Cortex & Executive Function", "作業記憶・抑制制御・認知的柔軟性の神経基盤。", 1),
  ("認知神経科学", "扁桃体と感情処理", "Amygdala & Emotion Processing", "恐怖条件付け・感情の評価・LeDoux理論。", 1),
  ("認知神経科学", "デフォルトモードネットワーク", "Default Mode Network", "安静時脳活動・自己参照処理・マインドワンダリングの神経基盤。", 1),
  ("認知神経科学", "脳可塑性・経験依存的変化", "Brain Plasticity & Experience-Dependent Change", "シナプス可塑性・クリティカルピリオド・神経新生。", 1),

  # 認知心理学 > 言語・思考・推論
  ("言語・思考・推論", "言語理解・文処理モデル", "Language Comprehension & Sentence Processing", "文処理の段階モデル・構文解析・意味統合。", 2),
  ("言語・思考・推論", "概念・カテゴリー化", "Concepts & Categorization", "プロトタイプ理論・ベーシックレベル・家族的類似性。", 1),
  ("言語・思考・推論", "メタ認知・モニタリング", "Metacognition & Monitoring", "知ることの知・モニタリング・制御・フルエンシー。", 1),
  ("言語・思考・推論", "類推推論・創造的思考", "Analogical Reasoning & Creative Thinking", "ジェントナーの構造写像・創造性の認知モデル。", 2),

  # 社会心理学 > 態度・説得
  ("態度・説得", "精緻化可能性モデル (ELM)", "Elaboration Likelihood Model", "中心ルート・周辺ルートによる説得処理。", 1),
  ("態度・説得", "認知的不協和理論", "Cognitive Dissonance Theory", "フェスティンガーの不協和・態度変容・自己正当化。", 1),
  ("態度・説得", "暗黙的態度・IAT", "Implicit Attitudes & IAT", "潜在連合テスト・自動的評価・無意識の偏見。", 1),
  ("態度・説得", "フレーミング効果・スピン", "Framing Effects & Spin", "同一情報の枠組み変化による判断変容。", 1),

  # 社会心理学 > 社会的認知・帰属
  ("社会的認知・帰属", "基本的帰属錯誤・行為者-観察者バイアス", "Fundamental Attribution Error & Actor-Observer Bias", "状況vs行為者の過大評価・文化差。", 1),
  ("社会的認知・帰属", "自己奉仕バイアス・自己呈示", "Self-Serving Bias & Self-Presentation", "成功・失敗への内的帰属・印象管理。", 1),
  ("社会的認知・帰属", "社会的比較理論", "Social Comparison Theory", "フェスティンガーの上方・下方比較・自己評価動機。", 1),
  ("社会的認知・帰属", "心の理論・メンタライジング", "Theory of Mind & Mentalizing", "他者の心的状態推測・TPJ活動・ASD研究。", 1),

  # 社会心理学 > 集団プロセス
  ("集団プロセス", "社会的アイデンティティ理論・自己カテゴリー化", "Social Identity Theory & Self-Categorization", "タジフェル・ターナーの内集団同定・集団間差別化。", 1),
  ("集団プロセス", "集団極化・集団思考", "Group Polarization & Groupthink", "議論による態度極端化・ジャニスの集団思考。", 1),
  ("集団プロセス", "変革型リーダーシップ・フォロワーシップ", "Transformational Leadership & Followership", "バス・バーンズの変革型モデル・カリスマ。", 1),
  ("集団プロセス", "集合的行動・集団規範", "Collective Action & Group Norms", "フリーライダー問題・規範の形成と維持。", 2),

  # 社会心理学 > 偏見・ステレオタイプ
  ("偏見・ステレオタイプ", "接触仮説・オルポート", "Contact Hypothesis & Allport", "集団間接触の条件・副次的接触効果。", 1),
  ("偏見・ステレオタイプ", "ステレオタイプ脅威", "Stereotype Threat", "スティールの研究・パフォーマンスへの影響・介入。", 1),
  ("偏見・ステレオタイプ", "インターセクショナリティ・交差性", "Intersectionality", "クレンショーの交差性・複合的差別の分析。", 1),
  ("偏見・ステレオタイプ", "微細な差別・マイクロアグレッション", "Microaggressions & Subtle Discrimination", "日常的・無意識的差別の累積的影響。", 1),

  # 社会心理学 > 感情心理学
  ("感情心理学", "基本感情論・エクマン", "Basic Emotions & Ekman", "普遍的表情・6基本感情・文化横断研究。", 1),
  ("感情心理学", "構成主義的感情論・バレット", "Constructed Emotion Theory & Barrett", "感情は構成される・文化的変異・予測的脳。", 1),
  ("感情心理学", "感情調節・再評価・抑圧", "Emotion Regulation: Reappraisal & Suppression", "グロスの過程モデル・認知的再評価の効果。", 1),
  ("感情心理学", "感情と意思決定・評価の感情注入", "Affect & Decision-Making", "感情注入モデル・気分と情報処理様式。", 2),

  # 臨床・異常心理学 > 心理療法・介入
  ("心理療法・介入", "認知行動療法 (CBT)", "Cognitive Behavioral Therapy", "ベックの認知療法・不合理な信念・行動活性化。", 1),
  ("心理療法・介入", "受容コミットメント療法 (ACT)", "Acceptance & Commitment Therapy", "心理的柔軟性・マインドフルネス・価値に基づく行動。", 1),
  ("心理療法・介入", "弁証法的行動療法 (DBT)", "Dialectical Behavior Therapy", "リネハン・感情調節・BPD治療・スキルトレーニング。", 1),
  ("心理療法・介入", "精神力動的・精神分析療法", "Psychodynamic & Psychoanalytic Therapy", "無意識・転移・防衛機制・短期精神力動療法。", 1),
  ("心理療法・介入", "EMDR・暴露療法", "EMDR & Exposure Therapy", "シャピロのEMDR・恐怖記憶の消去・PE療法。", 1),
  ("心理療法・介入", "マインドフルネスベース介入 (MBSR/MBCT)", "MBSR & MBCT", "カバット-ジンのMBSR・慢性疼痛・うつ再発予防。", 1),

  # 臨床・異常心理学 > 精神病理学・障害モデル
  ("精神病理学・障害モデル", "うつ病・双極性障害の理論モデル", "Depression & Bipolar Disorder Models", "認知モデル・脆弱性ストレスモデル・神経生物学的モデル。", 1),
  ("精神病理学・障害モデル", "不安障害・PTSD・強迫性障害モデル", "Anxiety, PTSD & OCD Models", "恐怖条件付け・安全学習・侵入思考の過程モデル。", 1),
  ("精神病理学・障害モデル", "統合失調症の認知・神経発達モデル", "Schizophrenia: Cognitive & Neurodevelopmental Models", "ドーパミン仮説・予測誤差モデル・認知機能障害。", 1),
  ("精神病理学・障害モデル", "神経発達障害 (ASD・ADHD)", "Neurodevelopmental Disorders: ASD & ADHD", "自閉スペクトラム・実行機能・心の理論の障害。", 1),
  ("精神病理学・障害モデル", "トランスダイアグノスティックアプローチ", "Transdiagnostic Approach", "障害横断的なプロセス・感情調節不全・ルミネーション。", 1),

  # 発達心理学 > 乳幼児・児童発達
  ("乳幼児・児童発達", "ピアジェの認知発達段階論", "Piagetian Stages of Cognitive Development", "感覚運動期・前操作期・具体的操作期・形式的操作期。", 1),
  ("乳幼児・児童発達", "ヴィゴツキー・最近接発達領域 (ZPD)", "Vygotsky & Zone of Proximal Development", "ZPD・スキャフォールディング・内言化。", 1),
  ("乳幼児・児童発達", "愛着理論・ボウルビー・エインスワース", "Attachment Theory: Bowlby & Ainsworth", "愛着の4分類・内的作業モデル・ストレンジ・シチュエーション。", 1),
  ("乳幼児・児童発達", "社会的参照・共同注意・心の理論の発達", "Social Referencing, Joint Attention & ToM Development", "9ヶ月革命・false-belief課題・発達軌跡。", 1),
  ("乳幼児・児童発達", "道徳発達・コールバーグ・ギリガン", "Moral Development: Kohlberg & Gilligan", "道徳推論の段階・ケアの倫理・文化差。", 2),

  # パーソナリティ > 動機・自己・人間性
  ("動機・自己・人間性", "自己決定理論 (SDT)", "Self-Determination Theory", "デシ・ライアンの内発動機・BPNT・自律性・有能感・関係性。", 1),
  ("動機・自己・人間性", "自己効力感・バンデューラ", "Self-Efficacy & Bandura", "行動の予期・代理強化・社会的学習理論。", 1),
  ("動機・自己・人間性", "ポジティブ心理学・フロー・レジリエンス", "Positive Psychology, Flow & Resilience", "セリグマン・チクセントミハイのフロー体験・強みへのアプローチ。", 1),
  ("動機・自己・人間性", "目標設定理論・計画的行動理論", "Goal Setting Theory & Theory of Planned Behavior", "ロック&レイサムの目標設定・アジェンの計画的行動。", 2),

  # 産業・組織心理学
  ("産業・組織心理学", "変革型・取引型リーダーシップ", "Transformational vs Transactional Leadership", "バス・バーンズの変革型リーダーシップ・LMX理論。", 1),
  ("産業・組織心理学", "職務要求-資源モデル (JD-R)", "Job Demands-Resources Model", "バーンアウト予防・エンゲージメント向上のJD-Rモデル。", 1),
  ("産業・組織心理学", "心理的安全性・組織学習", "Psychological Safety & Organizational Learning", "エドモンドソンの心理的安全性・チームパフォーマンス。", 1),
  ("産業・組織心理学", "ダイバーシティ・インクルージョン研究", "Diversity, Equity & Inclusion Research", "集団多様性・帰属感・偏見介入の組織的取り組み。", 1),

  # 健康心理学
  ("健康心理学・行動医学", "健康行動理論・HBM・TTM", "Health Behavior Theories: HBM & TTM", "健康信念モデル・行動変容ステージモデル。", 1),
  ("健康心理学・行動医学", "ストレスと健康・アロスタシス", "Stress & Health: Allostasis", "ストレス・コーピング・アロスタティック負荷。", 1),
  ("健康心理学・行動医学", "慢性疾患の心理的管理・生物心理社会モデル", "Chronic Illness & Biopsychosocial Model", "エンゲルのモデル・慢性疼痛・自己管理。", 1),

  # 社会学 > 制度論
  ("制度論・新制度主義", "DiMaggio & Powellの組織フィールド", "Organizational Fields & Isomorphism", "強制・模倣・規範的同型化・組織フィールド理論。", 1),
  ("制度論・新制度主義", "制度的ロジック・制度的起業家", "Institutional Logics & Institutional Entrepreneurs", "競合する制度的論理・変化の担い手。", 1),

  # 社会学 > ネットワーク
  ("社会的ネットワーク分析", "弱い紐帯の強さ・橋渡し型資本", "Strength of Weak Ties & Bridging Capital", "グラノヴェッター・異集団接触による情報拡散。", 1),
  ("社会的ネットワーク分析", "構造的空隙・バートの理論", "Structural Holes & Burt's Theory", "情報ブローカー・競争優位の源泉としての空隙。", 1),

  # 経済学 > 行動経済学
  ("ヒューリスティクス・バイアス", "アンカリング効果・調整不足", "Anchoring Effect & Adjustment", "初期値への過度な依存・交渉・価格設定への応用。", 1),
  ("ヒューリスティクス・バイアス", "正常性バイアス・楽観主義バイアス", "Normalcy Bias & Optimism Bias", "リスク過小評価・計画錯誤・ダニング-クルーガー効果。", 2),
  ("ナッジ・行動政策", "デフォルト効果・選択アーキテクチャ", "Default Effects & Choice Architecture", "臓器提供・年金加入のデフォルト設定実験。", 1),
  ("ナッジ・行動政策", "社会規範ナッジ・記述的規範", "Social Norm Nudges & Descriptive Norms", "エネルギー消費・投票行動への規範的フィードバック。", 1),

  # 文化人類学 > 象徴人類学
  ("儀礼・リミナリティ", "通過儀礼・ファン・ヘネップ", "Rites of Passage & Van Gennep", "分離・過渡・統合の三段階・コムニタス。", 1),
  ("儀礼・リミナリティ", "象徴的汚染・ダグラスの枠組み", "Symbolic Pollution & Douglas", "カテゴリー侵犯・タブーの文化的分析。", 1),
  ("贈与・互酬性", "モースの贈与論・総体的社会的事実", "Mauss's Gift & Total Social Fact", "贈与の義務・反贈与・物のhau。", 1),
  ("贈与・互酬性", "ポランニーの互酬性・再分配・交換", "Polanyi's Reciprocity, Redistribution & Exchange", "経済の社会的埋め込み・市場社会批判。", 1),
],

# ================================================================
# 自然科学 / natural_discovery
# ================================================================
"natural_discovery": [

  # 生態学 > 生態系生態学
  ("生態系生態学", "炭素循環・ネットエコシステム生産量", "Carbon Cycling & Net Ecosystem Production", "GPP・NPP・NEP・土壌呼吸・C貯留の定量化。", 1),
  ("生態系生態学", "窒素循環・富栄養化", "Nitrogen Cycling & Eutrophication", "N固定・硝化・脱窒・富栄養化の機構と管理。", 1),
  ("生態系生態学", "食物網・栄養カスケード", "Food Webs & Trophic Cascades", "トップダウン・ボトムアップ制御・栄養カスケード効果。", 1),
  ("生態系生態学", "生態系エンジニアリング・ビーバー効果", "Ecosystem Engineering", "物理的生息地改変種・ビーバー・サンゴ礁・土壌形成者。", 2),

  ("地球システム生態学", "地球システム科学・Gaiaの枠組み", "Earth System Science & Gaia Framework", "ラブロックのGaia仮説・地球システムの自己調節。", 1),
  ("地球システム生態学", "バイオーム分布・気候エンベロープモデル", "Biome Distribution & Climate Envelope Models", "ケッペン・ホールドリッジ・SDMによる分布予測。", 1),

  # 生態学 > 群集生態学
  ("群集生態学", "競争排除原理・生態的地位理論", "Competitive Exclusion & Niche Theory", "Hutchinsonのn次元超体積・競争共存機構。", 1),
  ("群集生態学", "捕食・被食関係・Lotka-Volterraモデル", "Predator-Prey Dynamics & Lotka-Volterra", "個体群の周期振動・Rosenzweig-MacArthurモデル。", 1),
  ("群集生態学", "中立理論・HubbelのUNIFIED NEUTRAL THEORY", "Neutral Theory of Biodiversity", "生物多様性の中立メカニズム・種豊富度分布。", 1),
  ("群集生態学", "菌根ネットワーク・正の相互作用", "Mycorrhizal Networks & Facilitation", "共生・相利共生・過酷環境での正相互作用。", 2),

  ("生物多様性科学", "種多様性指数・アルファ・ベータ・ガンマ多様性", "Diversity Indices: Alpha, Beta, Gamma", "Shannon・Simpson・Whitakerのβ多様性。", 1),
  ("生物多様性科学", "機能的多様性・形質ベース生態学", "Functional Diversity & Trait-Based Ecology", "機能形質・CWM・機能多様性指数。", 1),

  # 生態学 > 進化生態学
  ("進化生態学", "自然選択の単位・包括適応度", "Units of Selection & Inclusive Fitness", "ハミルトンの包括適応度・血縁選択・利他行動。", 1),
  ("進化生態学", "性選択・繁殖戦略・親の投資", "Sexual Selection & Parental Investment", "ダーウィン・トリヴァース・Zahavianの理論。", 1),
  ("進化生態学", "共進化・軍拡競争・相利共生の進化", "Coevolution & Mutualism Evolution", "レッドクイーン仮説・共進化の地理的モザイク。", 1),
  ("進化生態学", "表現型可塑性・反応基準", "Phenotypic Plasticity & Reaction Norms", "環境応答・エピジェネティクスとの関係。", 2),

  ("行動生態学", "最適採餌理論・パッチ利用", "Optimal Foraging Theory & Patch Use", "限界価値定理・エネルギー最大化仮説。", 1),
  ("行動生態学", "警戒行動・利他的警告・マルチレベル選択", "Alarm Calling & Altruistic Behavior", "グランドスクワーレルの警告・血縁選択vs互恵的利他。", 2),

  ("理論生態学", "個体ベースモデル・エージェントベースモデル", "Individual-Based & Agent-Based Models", "個体の不均一性を考慮した生態モデル。", 1),
  ("理論生態学", "複雑系と生態学・ネットワーク生態学", "Complex Systems & Network Ecology", "生態ネットワーク・食物網の安定性・カスケード絶滅。", 1),

  # 生態学 > 保全生態学
  ("保全生態学", "最小存続可能個体群・絶滅の渦", "Minimum Viable Population & Extinction Vortex", "ショールとウィルコックスのMVP・遺伝的多様性の閾値。", 1),
  ("保全生態学", "生息地断片化・メタ個体群理論", "Habitat Fragmentation & Metapopulation Theory", "ハンスキーのメタ個体群・パッチダイナミクス。", 1),
  ("保全生態学", "侵略的外来種・生物的侵入の生態", "Invasive Species & Biological Invasion", "侵入の段階・影響・管理戦略・ブラックリスト。", 1),
  ("保全生態学", "再野生化・機能的絶滅回避", "Rewilding & Functional Extinction Prevention", "トロフィックカスケード回復・キーストーン種の再導入。", 1),

  ("景観生態学", "景観パターンとプロセス・パーコレーション理論", "Landscape Pattern-Process & Percolation Theory", "コネクティビティ・断片化指数・緑の回廊設計。", 1),
  ("景観生態学", "生態的連結性・ウィルダネスコリドー", "Ecological Connectivity & Wildlife Corridors", "移動の重要性・回廊の設計基準・分断効果。", 1),

  ("応用生態学", "生態系修復・リストレーション生態学", "Ecosystem Restoration Ecology", "自然再生事業・国連生態系回復の10年。", 1),
  ("応用生態学", "生態系サービスの評価・自然資本", "Ecosystem Services Assessment & Natural Capital", "TEEBフレームワーク・InVESTモデル。", 1),

  # 物理学 > 量子力学
  ("量子情報・量子計算", "量子回路・量子ゲートモデル", "Quantum Circuits & Gate Model", "ユニバーサル量子ゲートセット・クリフォード回路・T-ゲート。", 1),
  ("量子情報・量子計算", "量子誤り訂正・トポロジカル符号", "Quantum Error Correction & Topological Codes", "表面符号・Steane符号・フォールトトレラント計算。", 1),
  ("量子情報・量子計算", "NISQ アルゴリズム・VQE・QAOA", "NISQ Algorithms: VQE & QAOA", "変分量子固有値ソルバー・量子近似最適化。", 1),
  ("量子情報・量子計算", "量子もつれ・量子テレポーテーション・量子暗号", "Entanglement, Teleportation & QKD", "Bell不等式・BB84プロトコル・量子鍵配送。", 1),

  ("量子場理論", "経路積分法・ファインマンダイアグラム", "Path Integral & Feynman Diagrams", "量子電磁力学・摂動展開・ダイバージェンスの繰り込み。", 1),
  ("量子場理論", "対称性とノーターの定理・ゲージ理論", "Symmetry, Noether's Theorem & Gauge Theory", "局所ゲージ対称性・標準模型の構造。", 1),

  # 物理学 > 凝縮系
  ("超伝導・超流動", "BCS理論・クーパー対・ギャップ方程式", "BCS Theory & Cooper Pairs", "フォノン媒介・order parameter・高温超伝導謎。", 1),
  ("超伝導・超流動", "Josephson効果・SQUIDデバイス", "Josephson Effect & SQUID", "超伝導接合・量子干渉・精密磁場計測。", 2),

  ("トポロジカル物質", "トポロジカル絶縁体・表面状態", "Topological Insulators & Surface States", "バルク-境界対応・スピン-軌道相互作用・ARPES。", 1),
  ("トポロジカル物質", "ワイル半金属・カイラル異常", "Weyl Semimetals & Chiral Anomaly", "バンド交差点・フェルミアーク表面状態。", 1),

  # 物理学 > 複雑系
  ("カオス・動力学系", "ローレンツアトラクタ・バタフライ効果", "Lorenz Attractor & Butterfly Effect", "決定論的カオス・初期値敏感性・リャプノフ指数。", 1),
  ("カオス・動力学系", "分岐理論・標準形", "Bifurcation Theory & Normal Forms", "サドルノード・ホップ・ピッチフォーク分岐。", 2),

  ("自己組織化・創発", "散逸構造・プリゴジン", "Dissipative Structures & Prigogine", "非平衡定常状態・エントロピー生成・対流セル。", 1),
  ("自己組織化・創発", "臨界現象・べき乗則・自己組織化臨界", "Critical Phenomena & Self-Organized Criticality", "バック-タン-ワーゼンフェルト・砂山モデル・べき乗則。", 1),
  ("ネットワーク科学", "スケールフリーネットワーク・Barabasi-Albert", "Scale-Free Networks & Barabasi-Albert", "優先的接続・ハブの出現・べき乗則次数分布。", 1),
  ("ネットワーク科学", "小世界ネットワーク・Watts-Strogatz", "Small-World Networks & Watts-Strogatz", "クラスタリングと短い経路長の共存。", 1),

  # 生物学 > 分子生物学
  ("ゲノミクス・エピゲノミクス", "全ゲノム関連解析 (GWAS)・多遺伝子スコア", "GWAS & Polygenic Risk Scores", "複合形質のゲノム基盤・PRS・SNPの効果量。", 1),
  ("ゲノミクス・エピゲノミクス", "エピジェネティクス・DNAメチル化・ヒストン修飾", "Epigenetics: DNA Methylation & Histone Modification", "CpG島・H3K27me3・クロマチン制御。", 1),
  ("ゲノミクス・エピゲノミクス", "長鎖非コードRNA・エピジェノーム地図", "lncRNA & Epigenome Mapping", "ENCODE・FANTOM・Roadmap Epigenomics。", 2),
  ("ゲノミクス・エピゲノミクス", "染色体高次構造・TAD・Hi-C", "Chromosome Architecture: TADs & Hi-C", "位相的関連ドメイン・3Dゲノム・エンハンサー-プロモーター相互作用。", 1),

  ("タンパク質構造・プロテオミクス", "AlphaFold・タンパク質構造予測", "AlphaFold & Protein Structure Prediction", "ディープラーニングによる三次元構造予測の革命。", 1),
  ("タンパク質構造・プロテオミクス", "クライオ電子顕微鏡 (cryo-EM)", "Cryo-Electron Microscopy", "原子分解能での巨大複合体構造解析。", 1),

  # 生物学 > 神経科学
  ("シナプス可塑性・学習・記憶", "長期増強 (LTP) と長期抑圧 (LTD)", "LTP & LTD Mechanisms", "NMDA受容体・AMPA受容体・カルシウムシグナル。", 1),
  ("シナプス可塑性・学習・記憶", "スパイク時刻依存可塑性 (STDP)", "Spike-Timing-Dependent Plasticity", "因果関係に基づくシナプス修飾・ヘッブの変形。", 1),
  ("シナプス可塑性・学習・記憶", "グリア細胞・アストロサイトの役割", "Glial Cells & Astrocyte Function", "シナプス三位一体・グリオトランスミッション。", 2),

  ("神経回路・コネクトーム", "線虫・ショウジョウバエ・マウスのコネクトーム", "Connectomes: C. elegans, Drosophila & Mouse", "全シナプス接続地図の完成と回路機能の解読。", 1),
  ("神経回路・コネクトーム", "皮質コラム・局所回路", "Cortical Columns & Local Circuits", "バレルコルテックス・オリエンテーション選択性・抑制性介在ニューロン。", 1),

  ("計算論的神経科学", "ベイズ脳・自由エネルギー最小化", "Bayesian Brain & Free Energy Minimization", "Friston能動的推論・予測符号化・知覚と行動の統一理論。", 1),
  ("計算論的神経科学", "スパイキングニューラルネットワーク・神経符号化", "Spiking Neural Networks & Neural Coding", "レート符号化・時刻符号化・集団符号化。", 1),

  # 地球科学 > 気候科学
  ("気候変動・温暖化機構", "温室効果ガスの放射強制力・気候感度", "Radiative Forcing & Climate Sensitivity", "ECS・TCR・気候フィードバック（アルベド・水蒸気・雲）。", 1),
  ("気候変動・温暖化機構", "ティッピングポイント・不可逆変化", "Tipping Points & Irreversible Change", "AMOC崩壊・アマゾン転換・氷床消失の閾値。", 1),
  ("大気・海洋相互作用", "ENSO・太平洋十年変動", "ENSO & Pacific Decadal Oscillation", "エルニーニョ・ラニーニャの機構・予測・社会影響。", 1),
  ("大気・海洋相互作用", "熱塩循環・MOC・大西洋翻転流", "Thermohaline Circulation & AMOC", "深層水形成・世界の気候安定化への役割。", 1),

  # 数学 > 確率論・統計学
  ("ベイズ推論", "ベイズ定理・事前分布・事後分布", "Bayes' Theorem & Prior/Posterior Distributions", "共役事前分布・階層モデル・マルコフ連鎖モンテカルロ。", 1),
  ("ベイズ推論", "変分推論・確率的プログラミング", "Variational Inference & Probabilistic Programming", "ELBO最大化・Stan・PyMC・変分オートエンコーダ。", 1),
  ("因果推論", "構造因果モデル・do-calculus", "Structural Causal Models & do-Calculus", "Pearl の因果階層・介入・反事実推論。", 1),
  ("因果推論", "潜在結果モデル・Rubin因果モデル", "Potential Outcomes & Rubin Causal Model", "ATT・ATE・操作変数・傾向スコアマッチング。", 1),
],

# ================================================================
# 人文学 / humanities_concept
# ================================================================
"humanities_concept": [

  # 哲学 > 存在論
  ("存在論・オントロジー", "形式オントロジー・BFO・OBO", "Formal Ontology: BFO & OBO", "上位オントロジー・DOLCE・オントロジー工学。", 2),
  ("存在論・オントロジー", "プロセス哲学・ホワイトヘッド", "Process Philosophy & Whitehead", "出来事・有機体の哲学・実在の流動性。", 1),
  ("因果論・決定論・自由意志", "ヒュームの規則性説・反事実的条件法", "Humean Regularity & Counterfactual Theories of Causation", "Lewis の反事実的因果論・因果のメカニズム論。", 1),
  ("因果論・決定論・自由意志", "両立論・自由意志と決定論の調和", "Compatibilism: Free Will & Determinism", "階層的意欲理論・フランクファートのケース。", 1),
  ("心の哲学・クオリア", "意識のハード問題・チャーマーズ", "Hard Problem of Consciousness & Chalmers", "説明ギャップ・哲学的ゾンビ・汎心論。", 1),
  ("心の哲学・クオリア", "機能主義・多重実現可能性", "Functionalism & Multiple Realizability", "プットナムの機能主義・Turing機械主義・心脳同一説批判。", 1),

  # 哲学 > 認識論
  ("知識・正当化・真理", "ゲティア問題・知識の分析", "Gettier Problem & Analysis of Knowledge", "justified true beliefの反例・知識の4条件モデル。", 1),
  ("知識・正当化・真理", "真理の対応説・コヒーレンス説・プラグマティズム", "Correspondence, Coherence & Pragmatist Theories of Truth", "各真理論の比較と批判。", 2),
  ("社会認識論・証言認識論", "証言による知識・還元主義vs反還元主義", "Testimonial Knowledge: Reductionism vs Anti-Reductionism", "Coady・Lackey の証言認識論。", 1),
  ("科学哲学・理論変化", "クーンのパラダイム論・科学革命の構造", "Kuhn's Paradigm & Structure of Scientific Revolutions", "通常科学・危機・革命・不通約性。", 1),
  ("科学哲学・理論変化", "ポパーの反証主義・ラカトシュの研究プログラム", "Popper's Falsificationism & Lakatos's Research Programme", "反証可能性基準・理論の硬いコア・保護帯。", 1),
  ("現象学・フッサール・ハイデガー", "志向性・ノエシス・ノエマ", "Intentionality: Noesis & Noema", "フッサールの意識の志向的構造・超越論的現象学。", 1),
  ("現象学・フッサール・ハイデガー", "世界-内-存在・道具の存在論", "Being-in-the-World & Tool-Being", "ハイデガーの現存在・使用中の存在論・配慮的交渉。", 1),

  # 哲学 > 倫理学
  ("規範倫理学・義務論・功利主義", "カントの定言命法・義務論", "Kantian Deontology & Categorical Imperative", "3定式・普遍化可能性・人格目的定式。", 1),
  ("規範倫理学・義務論・功利主義", "功利主義・選好功利主義・結果主義", "Utilitarianism & Consequentialism", "ベンサム・ミル・ピーターシンガーの立場。", 1),
  ("徳倫理学・実践的知恵", "アリストテレスの徳・フロネーシス", "Aristotelian Virtues & Phronesis", "ニコマコス倫理学・徳の習慣化・幸福論。", 1),
  ("徳倫理学・実践的知恵", "ネオ・アリストテレス主義・マッキンタイア", "Neo-Aristotelianism & MacIntyre", "美徳と実践・制度・ナラティブ・After Virtue。", 1),
  ("ケアの倫理・フェミニスト倫理", "ギリガン・ノディングスのケアの倫理", "Ethics of Care: Gilligan & Noddings", "関係性・文脈感受性・女性の道徳発達の差異。", 1),

  # 哲学 > 大陸哲学
  ("批判理論・フランクフルト学派", "ホルクハイマー・アドルノの啓蒙の弁証法", "Dialectic of Enlightenment: Horkheimer & Adorno", "理性の道具的歪み・文化産業・大衆操作批判。", 1),
  ("批判理論・フランクフルト学派", "ハーバーマスのコミュニカティブ行為論", "Habermas's Theory of Communicative Action", "生活世界・システム・討議倫理・公共圏。", 1),
  ("ポスト構造主義・フーコー・デリダ", "フーコーの権力・知・装置", "Foucault: Power, Knowledge & Dispositive", "系譜学・パノプティコン・主体化の技法。", 1),
  ("ポスト構造主義・フーコー・デリダ", "デリダの脱構築・差延", "Derrida: Deconstruction & Différance", "二項対立の解体・テクストの多義性・スペクトル論。", 1),

  # 言語学 > 認知言語学
  ("メタファー・メトニミー理論", "概念メタファー理論・Lakoff & Johnson", "Conceptual Metaphor Theory", "「議論は戦争」・方向メタファー・容器メタファー。", 1),
  ("メタファー・メトニミー理論", "精神空間・ブレンディング理論・Fauconnier & Turner", "Mental Spaces & Blending Theory", "多入力ブレンド・創造的思考の認知基盤。", 1),
  ("身体化認知・アフォーダンス言語学", "身体化された意味・Embodied Simulation", "Embodied Meaning & Simulation", "ミラーニューロン・身体図式・行動と言語の統合。", 1),
  ("フレーム意味論・構文文法", "フレーム意味論・Fillmore", "Frame Semantics: Fillmore", "意味フレーム・FrameNet・語彙意味論への応用。", 1),

  # 言語学 > 社会言語学
  ("言語変異・変化", "社会的層化変異・Labovの研究", "Social Stratification of Linguistic Variation", "Martha's Vineyard・変化の動因・コミュニティ内伝播。", 1),
  ("言語変異・変化", "言語接触・借用・クレオール化", "Language Contact, Borrowing & Creolization", "Thomason & Kaufman・ピジン→クレオール連続体。", 1),
  ("言語イデオロギー・言語政策", "言語権・少数言語保護", "Language Rights & Minority Language Protection", "ユネスコの危機言語地図・言語再活性化。", 1),
  ("多言語主義・コードスイッチング", "コードスイッチングの社会的機能", "Social Functions of Code-Switching", "会話型・状況的スイッチング・アイデンティティ表示。", 1),

  # 歴史学 > グローバル史
  ("帝国史・植民地史", "植民地主義と近代性・コロニアリティ", "Colonialism, Modernity & Coloniality", "Quijanoのコロニアリティ・Mignolo・脱植民地思想。", 1),
  ("帝国史・植民地史", "比較帝国史・帝国システム", "Comparative Imperial History & Imperial Systems", "帝国間比較・ローマ~大英~ソビエト帝国の比較。", 2),
  ("交流史・コネクテッドヒストリー", "大西洋史・インド洋史・太平洋史", "Atlantic, Indian Ocean & Pacific Histories", "海洋圏からの歴史再構成・通商・奴隷・移民。", 1),
  ("サバルタン研究", "チャクラバルティの属州のヨーロッパ化", "Chakrabarty's Provincializing Europe", "歴史主義批判・過去の復数性・非線形歴史。", 1),

  # 美学 > 芸術定義
  ("芸術の制度論・芸術世界", "ダントのアートワールド・慣習主義", "Danto's Artworld & Conventionalism", "「芸術とは何か」問い・芸術世界の制度的定義。", 1),
  ("表現・再現・図像論", "パノフスキーのイコノロジー", "Panofsky's Iconology", "図像誌・図像学・象徴的意味の三層分析。", 1),
  ("美的経験・趣味判断", "カントの美的判断の4契機", "Kant's Four Moments of Aesthetic Judgment", "無関心的快・普遍的妥当・目的なき合目的性・必然性。", 1),
],

# ================================================================
# 工学 / engineering_method
# ================================================================
"engineering_method": [

  # 機械学習・AI > 深層学習
  ("深層学習・ニューラルネットワーク", "Transformerアーキテクチャ・Self-Attention", "Transformer Architecture & Self-Attention", "Attention is All You Need・BERT・GPT系列の設計。", 1),
  ("深層学習・ニューラルネットワーク", "畳み込みニューラルネット (CNN)・ResNet", "CNN & ResNet", "VGG・InceptionNet・スキップ接続・BatchNorm。", 1),
  ("深層学習・ニューラルネットワーク", "生成モデル (GAN・VAE・拡散モデル)", "Generative Models: GAN, VAE & Diffusion Models", "DCGAN・VQ-VAE・DDPMとスコアベース生成。", 1),
  ("深層学習・ニューラルネットワーク", "事前学習・ファインチューニング・PEFT", "Pre-training, Fine-tuning & PEFT", "大規模事前学習・LoRA・Adapter・Instruction Tuning。", 1),
  ("深層学習・ニューラルネットワーク", "マルチモーダルモデル・視覚言語モデル", "Multimodal & Vision-Language Models", "CLIP・LLaVA・GPT-4V・CrossModal Attention。", 1),

  # 機械学習・AI > 自然言語処理
  ("自然言語処理・大規模言語モデル", "大規模言語モデル (LLM) のスケーリング則", "Scaling Laws for LLMs", "Chinchilla則・パラメータ数とデータ量の最適比。", 1),
  ("自然言語処理・大規模言語モデル", "RLHF・Constitutional AI・DPO", "RLHF, Constitutional AI & DPO", "人間フィードバックによる強化学習・報酬モデル・安全AI。", 1),
  ("自然言語処理・大規模言語モデル", "RAG・知識グラフ統合LLM", "RAG & Knowledge Graph-Augmented LLM", "Retrieval-Augmented Generation・Graph RAG。", 1),
  ("自然言語処理・大規模言語モデル", "推論・Chain of Thought・コードLLM", "LLM Reasoning & Chain of Thought", "CoT・ToT・自己整合性デコーディング・CodeLLM。", 1),

  # 機械学習・AI > 強化学習
  ("強化学習・逐次意思決定", "深層強化学習・DQN・PPO", "Deep RL: DQN & PPO", "DeepMindのAtari・OpenAI Gymでの実験的基盤。", 1),
  ("強化学習・逐次意思決定", "モデルベース強化学習・World Models", "Model-Based RL & World Models", "Dreamer・MBPO・計画と学習の統合。", 1),
  ("強化学習・逐次意思決定", "マルチエージェント強化学習・協調・競争", "Multi-Agent RL: Cooperation & Competition", "MARL・AlphaStar・経済ゲームへの応用。", 1),
  ("強化学習・逐次意思決定", "逆強化学習・模倣学習・GAIL", "Inverse RL, Imitation Learning & GAIL", "人間の行動からの報酬推定・行動クローン。", 2),

  # 機械学習・AI > 説明可能AI
  ("説明可能AI・信頼できるAI", "SHAP・LIME・特徴重要度", "SHAP, LIME & Feature Importance", "予測の局所的説明・Shapley値・モデル非依存解釈。", 1),
  ("説明可能AI・信頼できるAI", "AIの公正性・バイアス検出・除去", "AI Fairness, Bias Detection & Mitigation", "統計的公平性・個人公平性・反事実公平性。", 1),
  ("説明可能AI・信頼できるAI", "ロバスト性・敵対的攻撃・防御", "Robustness, Adversarial Attacks & Defense", "FGSM・PGD・認証済みロバスト性。", 1),

  # 機械学習・AI > グラフニューラルネット
  ("グラフニューラルネットワーク", "メッセージパッシング・GCN・GraphSAGE", "Message Passing, GCN & GraphSAGE", "ノード分類・リンク予測・グラフ分類。", 1),
  ("グラフニューラルネットワーク", "知識グラフ補完・トランスE・RotatE", "Knowledge Graph Completion: TransE & RotatE", "エンティティ・関係の埋め込み・推論。", 2),

  # アルゴリズム
  ("近似アルゴリズム・組合せ最適化", "近似比保証・PTAS・APX困難", "Approximation Ratio, PTAS & APX-Hard", "Set Cover・TSP・Knapsackの近似スキーム。", 1),
  ("計算複雑性・P対NP", "NP完全・NP困難の証明手法", "NP-Completeness Proofs: Cook-Levin Theorem", "多項式時間帰着・NP-hard問題の全景。", 1),

  # ソフトウェア工学
  ("アーキテクチャパターン・設計原則", "マイクロサービス・DDD・イベント駆動", "Microservices, DDD & Event-Driven Architecture", "境界コンテキスト・SAGA・CQRSパターン。", 1),
  ("アーキテクチャパターン・設計原則", "SOLID原則・デザインパターン (GoF)", "SOLID Principles & GoF Design Patterns", "クリーンアーキテクチャ・依存性逆転・責任の分離。", 1),
  ("形式検証・プログラム解析", "型理論・Curry-Howard対応", "Type Theory & Curry-Howard Correspondence", "依存型・CoqによるProof Assistant・型安全性。", 1),

  # セキュリティ
  ("公開鍵暗号・格子暗号", "格子暗号・NTRU・MLWEの困難性", "Lattice Cryptography: NTRU & MLWE", "NIST耐量子暗号標準・Kyber・Dilithium。", 1),
  ("ゼロ知識証明・秘密計算", "ZK-SNARK・ZK-STARKの構成", "ZK-SNARK & ZK-STARK Construction", "Groth16・PLONKの効率的証明システム。", 1),
  ("ゼロ知識証明・秘密計算", "秘密分散・準同型暗号・MPC", "Secret Sharing, Homomorphic Encryption & MPC", "プライバシー保護機械学習・Shamir秘密分散。", 1),

  # ロボティクス
  ("自律移動ロボット・SLAM", "SLAM（同時自己位置推定・地図構築）", "Simultaneous Localization and Mapping", "EKF-SLAM・GraphSLAM・ORB-SLAM3。", 1),
  ("自律移動ロボット・SLAM", "運動計画・RRT・MPC", "Motion Planning: RRT & MPC", "確率的ロードマップ・RRT*・モデル予測制御。", 1),
  ("ヒューマンロボットインタラクション", "インテンション推定・プロアクティブ行動", "Intention Estimation & Proactive Behavior", "人間の行動予測・文脈理解・安全な協働。", 1),

  # 制御工学
  ("最適制御・カルマンフィルタ", "カルマンフィルタ・拡張カルマン・粒子フィルタ", "Kalman Filter, EKF & Particle Filter", "状態推定・センサーフュージョン・SLAM適用。", 1),
  ("モデル予測制御 (MPC)", "非線形MPC・学習ベースMPC", "Nonlinear MPC & Learning-Based MPC", "経済MPC・Gaussian Process MPCの統合。", 1),

  # バイオエンジニアリング
  ("CRISPR・ゲノム編集", "CRISPR-Cas9・base editing・prime editing", "CRISPR-Cas9, Base & Prime Editing", "Doudna・Zhang・Liu の精密ゲノム編集技術の展開。", 1),
  ("CRISPR・ゲノム編集", "CAR-T療法・ゲノム編集と細胞治療", "CAR-T Therapy & Genome-Edited Cell Therapy", "T細胞工学・CD19・GVHDフリーCAR-T。", 1),
  ("シングルセル解析・マルチオミクス", "シングルセルRNA-seq・細胞アトラス", "scRNA-seq & Cell Atlas Projects", "HCA・Seurat解析・細胞型の系統的マッピング。", 1),
  ("幹細胞工学・iPS細胞", "山中4因子・ダイレクトリプログラミング", "Yamanaka Factors & Direct Reprogramming", "Oct4・Sox2・Klf4・c-Myc・分化転換の機構。", 1),

  # 環境・エネルギー
  ("太陽光発電・薄膜太陽電池", "ペロブスカイト太陽電池・多接合セル", "Perovskite Solar Cells & Multi-Junction", "変換効率記録・安定性問題・タンデム構造。", 1),
  ("水素製造・燃料電池", "水電解・光触媒水分解", "Water Electrolysis & Photocatalytic Water Splitting", "PEM電解槽・光触媒Z-スキーム・グリーン水素。", 1),
],

# ================================================================
# 芸術 / arts_question
# ================================================================
"arts_question": [

  # 美術 > 現代美術
  ("コンセプチュアルアート", "脱物質化・テクストとしてのアート", "Dematerialization & Text-Based Art", "コスースの「一つと三つの椅子」・言語の芸術化。", 1),
  ("コンセプチュアルアート", "プロセスアート・ランドアート", "Process Art & Land Art", "Smithsonのスパイラル・ジェッティ・地形の彫刻。", 1),
  ("コンセプチュアルアート", "フルクサス・ハプニング・イベントスコア", "Fluxus, Happenings & Event Scores", "ケージ・マチューナス・偶然性と参加者の役割。", 1),

  ("ソーシャリー・エンゲージド・アート", "関係の美学・ブリュリオ", "Relational Aesthetics & Bourriaud", "対話・社会的交換・集合的経験の芸術。", 1),
  ("ソーシャリー・エンゲージド・アート", "コミュニティアート・プレース・ベースト実践", "Community Art & Place-Based Practice", "参加者との共同制作・場所と記憶の活性化。", 1),
  ("ソーシャリー・エンゲージド・アート", "アクティビスト・アート・政治的実践", "Activist Art & Political Practice", "AIDS危機・環境・人種問題への芸術的介入。", 1),

  ("インスタレーション・場所特定型アート", "没入型インスタレーション・空間の演出", "Immersive Installation & Spatial Staging", "タレルのGanzfeld・Olitskiの光の空間。", 1),
  ("インスタレーション・場所特定型アート", "サイト・スペシフィック・観客の身体", "Site-Specific Art & Bodily Experience", "Richard Serra・空間と身体の力学的相互作用。", 1),

  # 美術 > 写真・映像アート
  ("写真理論・インデックス性", "バルトの「明るい部屋」・プンクトゥム", "Barthes's Camera Lucida & Punctum", "スタジウム・プンクトゥム・写真と死の関係。", 1),
  ("写真理論・インデックス性", "ベンジャミンの複製技術時代の芸術作品", "Benjamin's Art in the Age of Mechanical Reproduction", "アウラの喪失・政治的潜在力・複製可能性。", 1),
  ("ドキュメンタリー写真・社会的記録", "社会的ドキュメンタリーの倫理", "Ethics of Social Documentary Photography", "苦痛の表象・スーザン・ソンタグ・証人の責任。", 1),

  # 音楽 > 音楽理論
  ("調性・和声論", "機能和声・ローマ数字分析", "Functional Harmony & Roman Numeral Analysis", "和声進行の機能分析・シェンカーの分析。", 2),
  ("スペクトル作曲・微分音音楽", "スペクトル作曲技法・倍音列への接続", "Spectral Composition Techniques", "Grisey・Murailの作法・自然倍音と微分音。", 1),
  ("電子・電気音響音楽", "具体音楽・ミュジック・コンクレート", "Musique Concrète & Concrete Music", "Schaefferの音響対象・変換の技法・IRCAM。", 1),
  ("電子・電気音響音楽", "ライブエレクトロニクス・インタラクティブ音楽", "Live Electronics & Interactive Music Systems", "MaxMSP・SuperCollider・リアルタイム変換。", 1),

  # 音楽 > 民族音楽学
  ("サウンドスケープ・音楽地理学", "シェーファーのサウンドスケープ論", "Schafer's Soundscape Theory", "サウンドスケープ・ハイファイ/ローファイ環境・ウォールドサウンド。", 1),
  ("音楽とアイデンティティ・ディアスポラ", "音楽と国民的アイデンティティ・民族音楽の政治", "Music, National Identity & Politics of Ethnomusicology", "民族音楽学の植民地的起源批判・再定義。", 1),

  # 音楽 > ポピュラー音楽
  ("ヒップホップ・ラップ研究", "サンプリング文化・ループ・ブレイクビーツ", "Sampling Culture, Loops & Breakbeats", "Afrikas Bambaataa・著作権・ブレイクダンス接続。", 1),
  ("ヒップホップ・ラップ研究", "ヒップホップフェミニズム・ウォーマニズム", "Hip-Hop Feminism & Womanism", "女性MCの表象・クイーンラティファ・Cardi B研究。", 1),
  ("音楽産業・プラットフォーム・ストリーミング", "ストリーミング経済・アルゴリズムキュレーション", "Streaming Economics & Algorithmic Curation", "Spotifyのエコシステム・インディペンデント音楽家の収益構造。", 1),

  # デザイン > インタラクション
  ("人間中心デザイン・HCD", "フィールド調査・コンテキスチュアルインクワイアリー", "Field Research & Contextual Inquiry", "ユーザーの文脈理解・シャドーイング・参加観察。", 1),
  ("人間中心デザイン・HCD", "プロトタイピング・ユーザビリティテスト", "Prototyping & Usability Testing", "紙プロト・高忠実度プロト・ニールセンのヒューリスティクス。", 1),
  ("サービスデザイン", "サービスブループリント・顧客旅程マップ", "Service Blueprint & Customer Journey Mapping", "フロントステージ・バックステージ・接点分析。", 1),
  ("デザインリサーチ・エスノグラフィー的デザイン", "デザインエスノグラフィー・デザイン人類学", "Design Ethnography & Design Anthropology", "人類学的視点・文化的プローブ・デザイン介入。", 1),

  # デザイン > 社会デザイン
  ("フューチャーデザイン・投機的デザイン", "投機的デザイン・Dunne & Raby", "Speculative Design: Dunne & Raby", "批判的デザイン・未来の道具・問いを立てる実践。", 1),
  ("フューチャーデザイン・投機的デザイン", "トランジションデザイン・持続可能な移行", "Transition Design & Sustainable Transitions", "Irwin のトランジションデザイン・システム変容。", 1),
  ("コデザイン・参加型デザイン", "共同デザイン・スカンジナビアン伝統", "Co-Design & Scandinavian Design Tradition", "労働者参加・PDの政治的次元・パワーと倫理。", 1),

  # 映像・映画
  ("スペクタトール論・視線の理論", "マルヴィのラカン的視線・男性的眼差し", "Mulvey's Male Gaze & Lacanian Gaze", "「ヴィジュアル・プレジャーとナラティブ・シネマ」・フェミニスト映画理論。", 1),
  ("ジャンル論・ナラティブ理論", "ノワール・ウェスタン・ホラーのジャンル研究", "Noir, Western & Horror Genre Studies", "イデオロギーとジャンル・繰り返しと変奏。", 1),
  ("世界映画・ポストコロニアル映画論", "第三映画・革命的映画論", "Third Cinema & Revolutionary Film Theory", "Solanas・Getino「第三映画に向けて」・脱植民地映画実践。", 1),

  # 演劇 > パフォーマンス理論
  ("パフォーマンス研究・社会的ドラマ", "Schechnerの演劇性の広がり・Twice-Behaved Behavior", "Schechner's Expanded Theatricality", "日常行動・儀礼・遊び・演劇の連続体。", 1),
  ("ポストドラマ演劇", "Lehmannのポストドラマ・テキストからの解放", "Lehmann's Postdramatic Theatre", "物質性・在性・観客との関係の再定義。", 1),
  ("コンテンポラリーダンス・コレオグラフィー", "概念的コレオグラフィー・非ダンス", "Conceptual Choreography & Non-Dance", "JérômeBel・Xavier Le Roy・観念と身体の探求。", 1),

  # 芸術理論
  ("表象批判・脱構築的美術批評", "Halはスチュアート・表象の理論", "Stuart Hall's Theory of Representation", "エンコーディング/デコーディング・表象の政治。", 1),
  ("フェミニスト美術史・ジェンダー表象", "Griselda Pollockのフェミニスト美術史", "Griselda Pollock's Feminist Art History", "近代性・女性性・分離された空間・アヴァンギャルド再読。", 1),
  ("クィア理論・LGBTQ+芸術", "Butler のパフォーマティヴィティと芸術実践", "Butler's Performativity & Art Practice", "ジェンダーの遂行性・クィア展示・アーカイブ実践。", 1),
  ("新物質主義・事物の力", "Bennett の Vibrant Matter・活性的物質", "Bennett's Vibrant Matter", "非人間的エージェンシー・アセンブラージュ・政治生態学。", 1),

  # メディアアート
  ("AIアート・生成芸術", "GAN・拡散モデルを用いた芸術生成", "GAN & Diffusion Model-Based Art Generation", "StyleGAN・DALL-E・Midjourney・著作権問題。", 1),
  ("AIアート・生成芸術", "アルゴリズミックアート・コーダーアーティスト", "Algorithmic Art & Coder-Artists", "Processing・p5.js・コードを媒体とした創作。", 1),
  ("データ美学・コードとしての芸術", "データ彫刻・インフォビジュアライゼーションアート", "Data Sculpture & InfoVis Art", "Aaron Koblin・データの美的表現。", 2),
  ("ポストヒューマン・テクノロジーと身体", "サイボーグ宣言・Haraway・技術と身体の融合", "Haraway's Cyborg Manifesto & Body-Technology Fusion", "STS・フェミニスト技術論・サイボーグ存在論。", 1),
],

}


def add_l4():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 既存のL3エントリを (domain, name) → id のマップに
    rows = cur.execute(
        "SELECT domain, name, id FROM survey_frame WHERE level=3"
    ).fetchall()
    l3_map = {(r[0], r[1]): r[2] for r in rows}

    # 既存のL4を削除して入れ直す
    cur.execute("DELETE FROM survey_frame WHERE level=4")
    print("既存L4を削除しました")

    inserted = 0
    skipped = 0
    for domain, entries in L4.items():
        for parent_name, name, name_en, desc, priority in entries:
            parent_id = l3_map.get((domain, parent_name))
            if parent_id is None:
                print(f"  [WARN] L3 parent not found: domain={domain}, parent='{parent_name}'")
                skipped += 1
                continue
            uid = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO survey_frame
                  (id, domain, level, parent_id, name, name_en, description,
                   survey_priority, key_references, survey_status)
                VALUES (?, ?, 4, ?, ?, ?, ?, ?, '[]', 'not_started')
            """, (uid, domain, parent_id, name, name_en, desc, priority))
            inserted += 1

    conn.commit()
    print(f"L4投入完了: {inserted}件 / スキップ: {skipped}件")

    # 確認
    domain_names = {
        "social_theory": "社会科学", "natural_discovery": "自然科学",
        "humanities_concept": "人文学", "engineering_method": "工学", "arts_question": "芸術"
    }
    grand = 0
    for domain in L4.keys():
        cnt = cur.execute("SELECT COUNT(*) FROM survey_frame WHERE domain=? AND level=4", (domain,)).fetchone()[0]
        grand += cnt
        print(f"  {domain_names[domain]} L4: {cnt}件")
    print(f"  L4合計: {grand}件")
    conn.close()


if __name__ == "__main__":
    add_l4()
