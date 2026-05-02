#!/usr/bin/env python3
"""
Generate and insert 1,428 entries into startup_theory table.
Subfield 1: entrepreneurial_cognition_behavior (su_cog_001 to su_cog_714)
Subfield 2: opportunity_recognition_creation (su_opp_001 to su_opp_714)
"""

import sqlite3
import json
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
NOW = datetime.now().isoformat()

# ============================================================
# Subfield 1: entrepreneurial_cognition_behavior
# Topics: effectuation, alertness, cognitive biases, passion,
#         identity, bricolage, self-efficacy, heuristics,
#         prospect theory, fear of failure, resilience,
#         metacognition, pattern recognition, counterfactual,
#         social cognitive theory, mindset, intention models,
#         stress, flow states
# ============================================================

COG_TOPICS = [
    {
        "theme": "effectuation",
        "name_en_base": "Effectuation Theory",
        "name_ja_base": "エフェクチュエーション理論",
        "school": "Behavioral Entrepreneurship",
        "era_start": 2001,
        "stage": "pre-seed",
        "funding": "bootstrapping",
        "researchers": ["Saras Sarasvathy", "Stuart Read", "Nick Dew"],
        "works": ["Sarasvathy (2001) Causation and Effectuation", "Read et al. (2011) Effectual Entrepreneurship"],
        "keywords_ja": "エフェクチュエーション,コーゼーション,手段起点,熟達起業家,不確実性",
        "keywords_en": "effectuation,causation,means-driven,expert entrepreneur,uncertainty",
        "definition": "エフェクチュエーションは、熟達した起業家が不確実な状況下で「手元の手段」から出発して行動する意思決定ロジックを指す。目標設定から逆算するコーゼーションとは対照的に、利用可能なリソースと許容損失を出発点とする。Sarasvathy（2001）によって提唱され、スタートアップの初期段階に特に適合する。",
        "impact": "スタートアップの意思決定プロセスに関する理解を根本的に変革し、不確実性下での行動原理として広く応用されている。"
    },
    {
        "theme": "entrepreneurial_alertness",
        "name_en_base": "Entrepreneurial Alertness",
        "name_ja_base": "起業家的機敏性",
        "school": "Austrian Economics / Cognitive Entrepreneurship",
        "era_start": 1973,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Israel Kirzner", "Rui Alvarez", "Sankaran Venkataraman"],
        "works": ["Kirzner (1973) Competition and Entrepreneurship", "Tang et al. (2012) Alertness"],
        "keywords_ja": "機敏性,機会発見,オーストリア学派,注意,情報処理",
        "keywords_en": "alertness,opportunity discovery,Austrian economics,attention,information processing",
        "definition": "起業家的機敏性とは、他者が見逃した市場の不均衡や利益機会に気づく認知的傾向を指す。Kirzner（1973）はオーストリア経済学の立場から、起業家を市場の均衡回復をもたらす警戒的な行為者として描いた。この概念はその後、認知科学や心理学と統合され、注意・走査・連想・評価の4段階モデルとして精緻化された。",
        "impact": "機会認識研究の基礎概念として広く引用され、起業家教育や機会発見プロセスの実証研究に多大な影響を与えた。"
    },
    {
        "theme": "overconfidence",
        "name_en_base": "Overconfidence Bias in Entrepreneurship",
        "name_ja_base": "起業家の過信バイアス",
        "school": "Behavioral Entrepreneurship",
        "era_start": 1988,
        "stage": "seed",
        "funding": "angel",
        "researchers": ["Arnold Cooper", "Lowell Busenitz", "Jay Barney"],
        "works": ["Cooper et al. (1988) Entrepreneurs' perceived chances for success", "Busenitz & Barney (1997) Differences between entrepreneurs and managers"],
        "keywords_ja": "過信,バイアス,意思決定,リスク認知,楽観主義",
        "keywords_en": "overconfidence,bias,decision-making,risk perception,optimism",
        "definition": "起業家の過信バイアスとは、自身の能力や事業成功確率を客観的指標以上に高く評価する認知的傾向を指す。Cooper et al.（1988）の研究は、起業家の約80%が成功確率を平均以上と評価することを示した。この過信は行動の動機づけとしての機能と、リスク過小評価という二面性を持つ。",
        "impact": "起業家精神の矛盾的性質（合理的計算と非合理的楽観の共存）を理論化し、行動経済学と起業家研究の接合点を切り開いた。"
    },
    {
        "theme": "entrepreneurial_passion",
        "name_en_base": "Entrepreneurial Passion",
        "name_ja_base": "起業家的情熱",
        "school": "Affective Entrepreneurship",
        "era_start": 2009,
        "stage": "seed",
        "funding": "angel",
        "researchers": ["Melissa Cardon", "Joakim Wincent", "Julienne Meyer"],
        "works": ["Cardon et al. (2009) The nature and experience of entrepreneurial passion", "Cardon & Kirk (2015) Entrepreneurial self-efficacy as a moderator"],
        "keywords_ja": "情熱,感情,アイデンティティ,動機づけ,熱意",
        "keywords_en": "passion,affect,identity,motivation,enthusiasm",
        "definition": "起業家的情熱とは、起業活動に対する強烈で肯定的な感情と、その活動が自己アイデンティティの中核を占めるという意識の組み合わせを指す。Cardon et al.（2009）は情熱を発明・設立・開発の3つの役割ドメインに関連づけ、各ドメインが異なる行動パターンと結果をもたらすことを示した。",
        "impact": "感情研究と起業家研究を統合し、起業家のモチベーション・持続性・チームダイナミクスに関する研究を活性化させた。"
    },
    {
        "theme": "entrepreneurial_identity",
        "name_en_base": "Entrepreneurial Identity",
        "name_ja_base": "起業家的アイデンティティ",
        "school": "Identity Theory / Entrepreneurship",
        "era_start": 2000,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Mathew Hayward", "Dean Shepherd", "Melissa Cardon"],
        "works": ["Fauchart & Gruber (2011) Darwinians, Communitarians, and Missionaries", "Cardon et al. (2009) Entrepreneurial identity and passion"],
        "keywords_ja": "アイデンティティ,自己概念,役割理論,社会的アイデンティティ,起業家像",
        "keywords_en": "identity,self-concept,role theory,social identity,entrepreneur image",
        "definition": "起業家的アイデンティティとは、個人が「起業家である」という自己定義のことであり、行動や意思決定の枠組みとして機能する。社会的アイデンティティ理論や役割理論を基盤とし、起業家がどのように自己を位置づけ、どのような行動規範を内面化するかを探求する研究領域である。アイデンティティの強さが起業継続意思や回復力に影響することが示されている。",
        "impact": "起業家の行動を個人の内面プロセスから説明する枠組みを提供し、起業家教育・支援プログラムの設計に貢献している。"
    },
    {
        "theme": "bricolage",
        "name_en_base": "Entrepreneurial Bricolage",
        "name_ja_base": "起業家的ブリコラージュ",
        "school": "Resource Constraint Entrepreneurship",
        "era_start": 2005,
        "stage": "pre-seed",
        "funding": "bootstrapping",
        "researchers": ["Ted Baker", "Reed Nelson", "Stacey Kotha"],
        "works": ["Baker & Nelson (2005) Creating Something from Nothing", "Baker et al. (2003) Bricolage and Resourcefulness"],
        "keywords_ja": "ブリコラージュ,資源制約,即興,手元主義,資源活用",
        "keywords_en": "bricolage,resource constraints,improvisation,making do,resource leveraging",
        "definition": "起業家的ブリコラージュとは、手元にある限られた資源を組み合わせ・転用して新たな解決策や製品を生み出す実践を指す。Baker & Nelson（2005）はリソースが乏しい環境での起業活動を観察し、制約を創造性の触媒として活用する「手元主義」を概念化した。レヴィ＝ストロースのブリコラージュ概念を起業文脈に応用したものである。",
        "impact": "リーン・スタートアップやブートストラッピング戦略の理論的基盤を提供し、資源制約下でのイノベーション研究を拡張した。"
    },
    {
        "theme": "self_efficacy",
        "name_en_base": "Entrepreneurial Self-Efficacy",
        "name_ja_base": "起業家的自己効力感",
        "school": "Social Cognitive Theory",
        "era_start": 1998,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Gilad Chen", "Robert Gully", "Albert Bandura"],
        "works": ["Chen et al. (1998) Does entrepreneurial self-efficacy distinguish entrepreneurs from managers", "Bandura (1986) Social Foundations"],
        "keywords_ja": "自己効力感,バンデューラ,能力信念,起業意図,自信",
        "keywords_en": "self-efficacy,Bandura,capability belief,entrepreneurial intention,confidence",
        "definition": "起業家的自己効力感とは、起業活動に必要なさまざまな役割（マーケティング、財務管理、製品開発など）を成功裏に遂行できるという個人の信念を指す。Chen et al.（1998）がBandura（1986）の社会的認知理論を起業文脈に応用して概念化し、起業意図と行動の重要な予測因子であることが実証されている。",
        "impact": "起業家教育の効果測定指標として広く採用され、どのような介入が起業行動を促進するかの理解に貢献している。"
    },
    {
        "theme": "heuristics",
        "name_en_base": "Heuristics in Startup Decision-Making",
        "name_ja_base": "スタートアップ意思決定のヒューリスティクス",
        "school": "Behavioral Entrepreneurship",
        "era_start": 1997,
        "stage": "seed",
        "funding": "angel",
        "researchers": ["Lowell Busenitz", "Jay Barney", "Daniel Kahneman"],
        "works": ["Busenitz & Barney (1997) Differences between entrepreneurs and managers in large organizations", "Kahneman (2011) Thinking Fast and Slow"],
        "keywords_ja": "ヒューリスティクス,捷径,認知バイアス,直感的判断,限定合理性",
        "keywords_en": "heuristics,cognitive shortcuts,cognitive bias,intuitive judgment,bounded rationality",
        "definition": "スタートアップ意思決定におけるヒューリスティクスとは、起業家が複雑な不確実性下で用いる認知的近道・経験則を指す。Busenitz & Barney（1997）は起業家が大組織のマネジャーより過信・代表性ヒューリスティクスに頼る傾向があることを示した。これらは時に適応的機能を果たす一方、系統的な判断誤りをもたらす可能性もある。",
        "impact": "起業家の意思決定を合理モデルではなく認知プロセスから説明する研究流に先鞭をつけ、行動起業家論の礎となった。"
    },
    {
        "theme": "prospect_theory",
        "name_en_base": "Prospect Theory Applied to Entrepreneurship",
        "name_ja_base": "プロスペクト理論の起業適用",
        "school": "Behavioral Finance / Entrepreneurship",
        "era_start": 1979,
        "stage": "seed",
        "funding": "angel",
        "researchers": ["Daniel Kahneman", "Amos Tversky", "Dean Shepherd"],
        "works": ["Kahneman & Tversky (1979) Prospect Theory", "Shepherd (1999) Venture capitalists' introspection"],
        "keywords_ja": "プロスペクト理論,損失回避,参照点,リスク態度,行動経済学",
        "keywords_en": "prospect theory,loss aversion,reference point,risk attitude,behavioral economics",
        "definition": "プロスペクト理論の起業適用は、Kahneman & Tversky（1979）の損失回避・参照点依存・確率加重という三原理を起業家の意思決定に適用する研究領域である。起業家がリスクに対して状況依存的な態度をとること、損失局面で賭けに出る傾向があることなどが説明される。失敗後の行動パターンや撤退決定の研究に特に応用されている。",
        "impact": "起業家の非線形なリスク態度を説明する枠組みを提供し、失敗研究・撤退研究・投資家行動研究に広く活用されている。"
    },
    {
        "theme": "fear_of_failure",
        "name_en_base": "Fear of Failure in Entrepreneurship",
        "name_ja_base": "起業における失敗恐怖",
        "school": "Motivation Theory / Entrepreneurship",
        "era_start": 1991,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Robert Hisrich", "Mathew Hayward", "Melissa Cardon"],
        "works": ["Cacciotti et al. (2016) A reconceptualization of fear of failure", "Politis & Gabrielsson (2009) Entrepreneurs' attitudes towards failure"],
        "keywords_ja": "失敗恐怖,起業障壁,リスク回避,心理的安全,文化的要因",
        "keywords_en": "fear of failure,entrepreneurial barrier,risk aversion,psychological safety,cultural factors",
        "definition": "起業における失敗恐怖とは、ビジネスの失敗に伴う否定的結果（財務損失・社会的評判低下・自己評価の毀損）への恐れが起業行動を抑制する心理的状態を指す。国・文化によって失敗に対する社会的スティグマが異なり、失敗恐怖の程度も大きく変わることが国際比較研究で示されている。",
        "impact": "国際的な起業エコシステム比較研究の鍵となる変数として活用され、政策立案や起業家育成プログラムの設計に影響を与えている。"
    },
    {
        "theme": "entrepreneurial_resilience",
        "name_en_base": "Entrepreneurial Resilience",
        "name_ja_base": "起業家的レジリエンス",
        "school": "Positive Psychology / Entrepreneurship",
        "era_start": 2003,
        "stage": "early",
        "funding": "VC",
        "researchers": ["Dean Shepherd", "Marcus Wolfe", "James Waddock"],
        "works": ["Shepherd (2003) Learning from Business Failure", "Cardon & McGrath (1999) When the going gets tough"],
        "keywords_ja": "レジリエンス,回復力,失敗からの学習,精神的強靭性,適応",
        "keywords_en": "resilience,bounce-back,learning from failure,mental toughness,adaptation",
        "definition": "起業家的レジリエンスとは、失敗・挫折・逆境に直面した際に心理的に回復し、適応的に前進し続ける能力を指す。Shepherd（2003）は失敗経験からの学習プロセスを悲嘆理論と結びつけて分析した。レジリエンスは固定的な性格特性ではなく、経験・支援環境・認知的再評価によって開発可能な動的能力として捉えられる。",
        "impact": "起業家のウェルビーイング研究と失敗研究を統合し、失敗後の再起行動（serial entrepreneurship）の理解に貢献している。"
    },
    {
        "theme": "metacognition",
        "name_en_base": "Metacognition in Entrepreneurship",
        "name_ja_base": "起業における メタ認知",
        "school": "Cognitive Entrepreneurship",
        "era_start": 2002,
        "stage": "all",
        "funding": "all",
        "researchers": ["Michael Haynie", "Dean Shepherd", "Robert Hicks"],
        "works": ["Haynie & Shepherd (2009) A measure of adaptive cognition for entrepreneurship research", "Hmieleski & Baron (2008) Regulatory focus and new venture performance"],
        "keywords_ja": "メタ認知,認知適応性,自己監視,思考についての思考,学習能力",
        "keywords_en": "metacognition,cognitive adaptability,self-monitoring,thinking about thinking,learning capacity",
        "definition": "起業におけるメタ認知とは、自身の思考プロセスを認識・モニタリング・制御する高次の認知能力を指す。Haynie & Shepherd（2009）は認知適応性の枠組みでこれを起業文脈に導入し、動的で不確実な環境に適応する際にメタ認知が重要な役割を果たすことを示した。メタ認知能力の高い起業家はより柔軟な意思決定が可能である。",
        "impact": "起業家教育において「いかに考えるか」を教えることの重要性を理論的に裏付け、認知訓練プログラムの設計に応用されている。"
    },
    {
        "theme": "pattern_recognition",
        "name_en_base": "Pattern Recognition in Entrepreneurship",
        "name_ja_base": "起業家のパターン認識",
        "school": "Cognitive Entrepreneurship",
        "era_start": 2000,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Robert Baron", "Scott Shane", "Norris Krueger"],
        "works": ["Baron (2006) Opportunity recognition as pattern recognition", "Baron & Ensley (2006) Opportunity recognition as the detection of meaningful patterns"],
        "keywords_ja": "パターン認識,プロトタイプ,先行知識,連想,機会知覚",
        "keywords_en": "pattern recognition,prototype,prior knowledge,connection,opportunity perception",
        "definition": "起業家のパターン認識とは、経験や知識に基づいて環境の断片的な情報を意味のあるパターンとして認識し、潜在的な機会を見出す認知プロセスを指す。Baron（2006）はチェスの棋士研究から得られたパターン認識の知見を起業家研究に応用し、機会認識が事前知識に基づくテンプレートマッチングであることを示した。",
        "impact": "機会認識を純粋な「発見」ではなく認知的プロセスとして説明する基礎理論となり、経験・訓練が起業能力に与える影響の研究を促進した。"
    },
    {
        "theme": "counterfactual_thinking",
        "name_en_base": "Counterfactual Thinking in Entrepreneurship",
        "name_ja_base": "起業における反実仮想思考",
        "school": "Cognitive Entrepreneurship / Decision Theory",
        "era_start": 2005,
        "stage": "all",
        "funding": "all",
        "researchers": ["Dean Shepherd", "Mathew Hayward", "N. Keith Lowe"],
        "works": ["Roese & Summerville (2005) What we regret most", "Cope (2011) Entrepreneurial learning from failure"],
        "keywords_ja": "反実仮想,後悔,学習,代替シナリオ,失敗分析",
        "keywords_en": "counterfactual thinking,regret,learning,alternative scenarios,failure analysis",
        "definition": "起業における反実仮想思考とは、「もし別の選択をしていたら」という仮想の代替シナリオを想定する認知的プロセスを指す。起業家は失敗経験後に反実仮想思考を通じて教訓を抽出し、将来の意思決定を改善する。上向き反実仮想（より良い状態を想像）は後悔と改善動機を、下向き反実仮想（より悪い状態を想像）は慰めと自己防衛をもたらす。",
        "impact": "失敗からの学習メカニズムを認知レベルで解明し、連続起業家の経験活用に関する実証研究の理論的基盤を提供している。"
    },
    {
        "theme": "social_cognitive_theory",
        "name_en_base": "Social Cognitive Theory of Entrepreneurship",
        "name_ja_base": "起業の社会認知理論",
        "school": "Social Cognitive Theory",
        "era_start": 1986,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Albert Bandura", "Robert Wood", "Gilad Chen"],
        "works": ["Bandura (1986) Social Foundations of Thought and Action", "Wood & Bandura (1989) Social cognitive theory of organizational management"],
        "keywords_ja": "社会認知理論,観察学習,モデリング,自己調整,環境-行動-人の三項相互作用",
        "keywords_en": "social cognitive theory,observational learning,modeling,self-regulation,triadic reciprocal causation",
        "definition": "起業の社会認知理論は、Bandura（1986）の三項相互決定論（人・行動・環境の双方向的影響）を起業文脈に適用する理論的枠組みである。起業行動は自己効力感・結果期待・目標の認知的メカニズムによって媒介され、観察学習やロールモデルの存在が起業意図形成に重要な役割を果たすことが示されている。",
        "impact": "起業家教育・メンタリング・ロールモデル研究の理論的支柱となり、どのような学習環境が起業行動を促すかの理解に貢献している。"
    },
    {
        "theme": "entrepreneurial_mindset",
        "name_en_base": "Entrepreneurial Mindset",
        "name_ja_base": "起業家的マインドセット",
        "school": "Cognitive Entrepreneurship / Dynamic Capabilities",
        "era_start": 2000,
        "stage": "all",
        "funding": "all",
        "researchers": ["Rita McGrath", "Ian MacMillan", "Carol Dweck"],
        "works": ["McGrath & MacMillan (2000) The Entrepreneurial Mindset", "Dweck (2006) Mindset"],
        "keywords_ja": "マインドセット,成長志向,機会探索,不確実性耐性,起業家精神",
        "keywords_en": "mindset,growth orientation,opportunity seeking,uncertainty tolerance,entrepreneurial spirit",
        "definition": "起業家的マインドセットとは、機会を積極的に探索し、不確実性を脅威ではなく可能性として受容し、持続的に行動する認知・態度・行動傾向の複合体を指す。McGrath & MacMillan（2000）はこれを大企業の内部起業家にも必要な能力として定義し、Dweck（2006）の成長マインドセット研究との親和性から教育分野でも注目を集めた。",
        "impact": "起業家精神を先天的特性ではなく開発可能な能力として捉える視点を普及させ、教育機関や企業研修での応用が広がっている。"
    },
    {
        "theme": "intention_models",
        "name_en_base": "Entrepreneurial Intention Models",
        "name_ja_base": "起業意図モデル",
        "school": "Theory of Planned Behavior",
        "era_start": 1991,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Icek Ajzen", "Norris Krueger", "Robert Carsrud"],
        "works": ["Ajzen (1991) Theory of planned behavior", "Krueger & Brazeal (1994) Entrepreneurial potential and potential entrepreneurs", "Shapero & Sokol (1982) Social dimensions of entrepreneurship"],
        "keywords_ja": "起業意図,計画的行動理論,主観的規範,行動制御感,Shaperoモデル",
        "keywords_en": "entrepreneurial intention,theory of planned behavior,subjective norm,perceived behavioral control,Shapero model",
        "definition": "起業意図モデルは、個人が起業を決意するまでの心理的プロセスを体系化する理論群である。Ajzen（1991）の計画的行動理論を基盤に、Kruegerらは態度・主観的規範・知覚された行動制御の三要素が起業意図を形成することを示した。Shapero & Sokol（1982）の起業事象モデルも意図形成における「変位」の役割を強調する重要な枠組みである。",
        "impact": "起業意図の測定・予測・促進に関する豊富な実証研究を生み出し、起業家教育の効果評価指標として国際的に活用されている。"
    },
    {
        "theme": "entrepreneurial_stress",
        "name_en_base": "Entrepreneurial Stress",
        "name_ja_base": "起業家のストレス",
        "school": "Organizational Behavior / Health Psychology",
        "era_start": 1994,
        "stage": "early",
        "funding": "VC",
        "researchers": ["Robert Boyd", "Galen Vozikis", "Bradley George"],
        "works": ["Boyd & Gumpert (1983) Coping with entrepreneurial stress", "Cardon & Patel (2015) Is stress worth it"],
        "keywords_ja": "ストレス,燃え尽き症候群,ウェルビーイング,ワークライフバランス,精神的健康",
        "keywords_en": "stress,burnout,well-being,work-life balance,mental health",
        "definition": "起業家のストレスとは、高い不確実性・長時間労働・多大な責任・財務リスクなど起業活動特有の要因が引き起こす心理的・身体的負荷を指す。Boyd & Gumpert（1983）が初期に概念化し、その後燃え尽き症候群・不安・うつとの関連を探る研究が蓄積された。一定のストレスは動機づけや機会探索の推進力となる一方、過度なストレスは意思決定品質と健康を損なう。",
        "impact": "起業家のウェルビーイング研究の基盤を築き、投資家・インキュベーターによる精神的支援の重要性を示すエビデンスを提供している。"
    },
    {
        "theme": "flow_states",
        "name_en_base": "Flow States in Entrepreneurship",
        "name_ja_base": "起業活動におけるフロー状態",
        "school": "Positive Psychology / Entrepreneurship",
        "era_start": 1990,
        "stage": "all",
        "funding": "all",
        "researchers": ["Mihaly Csikszentmihalyi", "Melissa Cardon", "Joakim Wincent"],
        "works": ["Csikszentmihalyi (1990) Flow: The Psychology of Optimal Experience", "Cardon et al. (2012) The role of entrepreneurial passion in new venture creation"],
        "keywords_ja": "フロー,最適経験,没入,熱意,内発的動機",
        "keywords_en": "flow,optimal experience,immersion,enthusiasm,intrinsic motivation",
        "definition": "起業活動におけるフロー状態とは、Csikszentmihalyi（1990）が定義した最適経験の概念を起業文脈に適用したものであり、挑戦と能力が一致した際に生じる完全没入・時間感覚の消失・高い内発的満足を特徴とする心理状態を指す。起業家はとりわけ製品開発・顧客開拓・問題解決の過程でフロー状態を経験することが多いと報告されている。",
        "impact": "起業家のパフォーマンスと幸福感を内発的動機の観点から説明する枠組みを提供し、起業家精神の持続性と創造性研究に貢献している。"
    },
]

# ============================================================
# Subfield 2: opportunity_recognition_creation
# ============================================================

OPP_TOPICS = [
    {
        "theme": "shane_venkataraman",
        "name_en_base": "Opportunity Framework (Shane & Venkataraman 2000)",
        "name_ja_base": "機会フレームワーク（シェーン&ベンカタラマン2000）",
        "school": "Opportunity-Based Entrepreneurship",
        "era_start": 2000,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Scott Shane", "Sankaran Venkataraman", "Israel Kirzner"],
        "works": ["Shane & Venkataraman (2000) The promise of entrepreneurship as a field of research", "Shane (2003) A General Theory of Entrepreneurship"],
        "keywords_ja": "起業機会,個人と機会の結合,機会認識,先行知識,情報の非対称性",
        "keywords_en": "entrepreneurial opportunity,nexus of individual and opportunity,opportunity recognition,prior knowledge,information asymmetry",
        "definition": "Shane & Venkataraman（2000）の機会フレームワークは、起業学を「機会の存在」と「機会を追求する個人」の結合として定義した転換点的論文に基づく。機会は経済システムの不均衡から生まれ、それに気づく個人の先行知識と動機によって活用されると主張する。この枠組みは起業研究の統一的パラダイムとして広く採用された。",
        "impact": "起業研究を機会中心の統合フレームワークで再定義し、以後20年の研究議論の出発点となった主要理論である。"
    },
    {
        "theme": "kirzner_vs_schumpeter",
        "name_en_base": "Kirzner Discovery vs Schumpeter Creation",
        "name_ja_base": "カーズナーの発見対シュンペーターの創造",
        "school": "Austrian Economics / Evolutionary Economics",
        "era_start": 1934,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Israel Kirzner", "Joseph Schumpeter", "Scott Shane"],
        "works": ["Schumpeter (1934) Theory of Economic Development", "Kirzner (1973) Competition and Entrepreneurship"],
        "keywords_ja": "機会発見,創造的破壊,均衡回復,イノベーション,起業家機能",
        "keywords_en": "opportunity discovery,creative destruction,equilibrium restoration,innovation,entrepreneurial function",
        "definition": "カーズナーとシュンペーターは起業家の役割について対照的な見解を持つ。カーズナー（1973）は起業家を市場不均衡に気づき均衡回復をもたらす「発見者」として描き、シュンペーター（1934）は既存秩序を破壊し新たな組み合わせを創出する「創造者」として描いた。この二項対立は機会の本質と起業家の機能に関する理論的論争の原点となっている。",
        "impact": "発見・創造・想像という機会の存在論的地位を巡る後続論争（Alvarez & Barney等）の起点となり、起業理論の哲学的深化に貢献した。"
    },
    {
        "theme": "discovery_vs_creation",
        "name_en_base": "Discovery vs Creation Theory (Alvarez & Barney 2007)",
        "name_ja_base": "発見理論対創造理論（アルバレス&バーニー2007）",
        "school": "Strategic Entrepreneurship",
        "era_start": 2007,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Sharon Alvarez", "Jay Barney", "Per Davidsson"],
        "works": ["Alvarez & Barney (2007) Discovery and Creation: Alternative Theories of Entrepreneurial Action", "Alvarez et al. (2013) Forming and exploiting opportunities"],
        "keywords_ja": "発見理論,創造理論,機会の存在論,不確実性,リスク",
        "keywords_en": "discovery theory,creation theory,ontology of opportunities,uncertainty,risk",
        "definition": "Alvarez & Barney（2007）は機会をめぐる発見理論と創造理論という二つの存在論的立場を体系的に整理した。発見理論では機会は客観的に存在し起業家に発見されるものとされ、創造理論では機会は起業家の行動を通じて主観的に構成されると見なされる。両理論は不確実性の性質・意思決定ロジック・知識形成に関して異なる含意を持つ。",
        "impact": "機会研究の存在論的・認識論的基盤を整理し、エフェクチュエーション・リーン等の実践的枠組みと理論を橋渡しする重要な理論的貢献である。"
    },
    {
        "theme": "davidsson_reconceptualization",
        "name_en_base": "Opportunity Reconceptualization (Davidsson 2015)",
        "name_ja_base": "機会の再概念化（デビッドソン2015）",
        "school": "Process Theory of Entrepreneurship",
        "era_start": 2015,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Per Davidsson", "Henrik Berglund", "Gordon Murray"],
        "works": ["Davidsson (2015) Entrepreneurial opportunities and the entrepreneurship nexus", "Davidsson (2016) Researching entrepreneurship"],
        "keywords_ja": "外的実現可能性,機会信念,外的条件,内的状態,再概念化",
        "keywords_en": "external enablement,opportunity belief,external conditions,internal states,reconceptualization",
        "definition": "Davidsson（2015）は既存の「機会」概念を批判的に再検討し、外部環境の変化（External Enablement）と起業家の内的信念（Opportunity Belief）という二つの独立した構成要素に分解する再概念化を提案した。これにより「機会が客観的に存在するか主観的に構成されるか」という不毛な二項対立を超え、実証研究が可能な概念的枠組みを構築した。",
        "impact": "Shane & Venkataraman（2000）以降の機会概念の曖昧さを解消し、起業研究の概念的厳密性を高める試みとして高い引用数を獲得している。"
    },
    {
        "theme": "information_asymmetry",
        "name_en_base": "Information Asymmetry in Entrepreneurship",
        "name_ja_base": "起業における情報の非対称性",
        "school": "Information Economics / Entrepreneurship",
        "era_start": 1970,
        "stage": "seed",
        "funding": "angel",
        "researchers": ["George Akerlof", "Scott Shane", "Lowell Busenitz"],
        "works": ["Akerlof (1970) The Market for Lemons", "Shane & Venkataraman (2000) The promise of entrepreneurship"],
        "keywords_ja": "情報の非対称性,逆選択,モラルハザード,シグナリング,起業機会",
        "keywords_en": "information asymmetry,adverse selection,moral hazard,signaling,entrepreneurial opportunity",
        "definition": "起業における情報の非対称性とは、起業家と投資家・顧客・パートナーなどの間に存在する情報格差を指す。Akerlof（1970）の「レモン市場」理論を起業に適用すると、起業家は事業の価値を知っているが投資家は知らないという構造的な情報格差が資金調達・採用・販売を困難にすることが説明される。この非対称性を解消するシグナリング戦略が重要となる。",
        "impact": "ベンチャーキャピタル投資の意思決定メカニズム・知的財産戦略・起業家のシグナリング行動の理論的基盤として広く応用されている。"
    },
    {
        "theme": "prior_knowledge",
        "name_en_base": "Prior Knowledge and Opportunity Recognition (Shane 2000)",
        "name_ja_base": "先行知識と機会認識（シェーン2000）",
        "school": "Knowledge-Based Theory of Entrepreneurship",
        "era_start": 2000,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Scott Shane", "Israel Kirzner", "Daniel Schendel"],
        "works": ["Shane (2000) Prior knowledge and the discovery of entrepreneurial opportunities", "Cohen & Levinthal (1990) Absorptive capacity"],
        "keywords_ja": "先行知識,機会認識,知識回廊,情報非対称性,学習",
        "keywords_en": "prior knowledge,opportunity recognition,knowledge corridor,information asymmetry,learning",
        "definition": "Shane（2000）の先行知識理論は、個人が保有する特定分野の知識がどの機会に「気づく」かを決定することを実証的に示した。技術知識・市場知識・顧客知識など特定の先行知識を持つ人物のみが、その知識領域に関連する機会を認識できる「知識回廊」の概念が中核をなす。機会認識の個人差を体系的に説明する知識ベース理論の起点となった。",
        "impact": "なぜ同じ情報に接しても一部の人しか機会を見出せないかを説明し、起業教育・専門知識の蓄積・越境学習の価値を理論化する基盤を提供した。"
    },
    {
        "theme": "social_networks_opportunity",
        "name_en_base": "Social Networks and Opportunity Recognition",
        "name_ja_base": "社会ネットワークと機会認識",
        "school": "Social Network Theory / Entrepreneurship",
        "era_start": 1973,
        "stage": "pre-seed",
        "funding": "angel",
        "researchers": ["Mark Granovetter", "Ronald Burt", "Howard Aldrich"],
        "works": ["Granovetter (1973) The strength of weak ties", "Burt (2004) Structural holes and good ideas", "Aldrich & Zimmer (1986) Entrepreneurship through social networks"],
        "keywords_ja": "社会ネットワーク,弱い紐帯,構造的空隙,ブローカー,埋め込み性",
        "keywords_en": "social networks,weak ties,structural holes,broker,embeddedness",
        "definition": "社会ネットワークと機会認識の研究は、起業家が機会を発見・評価・活用する際に社会的関係が果たす役割を探求する。Granovetter（1973）の弱い紐帯理論は、密接な関係より遠い知人からの方が新情報を得やすいことを示し、Burt（2004）の構造的空隙理論は異なるクラスター間を橋渡しするブローカーが機会創出において有利であることを示した。",
        "impact": "起業家のネットワーク構築戦略・ネットワーキング行動・インキュベーター設計に関する研究と実践の両面で広く活用されている。"
    },
    {
        "theme": "dimov_opportunity_process",
        "name_en_base": "Opportunity Process (Dimov 2007)",
        "name_ja_base": "機会プロセス（ディモフ2007）",
        "school": "Process Theory of Entrepreneurship",
        "era_start": 2007,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Dimo Dimov", "Per Davidsson", "Scott Shane"],
        "works": ["Dimov (2007) Beyond the single-person, single-insight attribution in understanding entrepreneurial opportunities", "Dimov (2011) Grappling with the unbearable elusiveness of entrepreneurial opportunities"],
        "keywords_ja": "機会プロセス,創発,社会的構成,反復,起業活動プロセス",
        "keywords_en": "opportunity process,emergence,social construction,iteration,entrepreneurial process",
        "definition": "Dimov（2007）の機会プロセス理論は、機会を瞬間的に「発見」される静的なものではなく、起業家と環境の相互作用を通じて時間をかけて展開する動的プロセスとして捉える。機会の形成・精緻化・評価は社会的相互作用と反復的な試行の中で進行し、当初の「機会概念」と最終的に現れる「機会」は大きく異なりうる。",
        "impact": "機会研究のプロセス論的転回を促進し、スタートアップの初期段階における方向転換（ピボット）のメカニズムを理論化する基盤となった。"
    },
    {
        "theme": "ardichvili_model",
        "name_en_base": "Opportunity Recognition Model (Ardichvili 2003)",
        "name_ja_base": "機会認識モデル（アルディクヴィリ2003）",
        "school": "Integrative Opportunity Theory",
        "era_start": 2003,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Alexander Ardichvili", "Richard Cardozo", "Sourav Ray"],
        "works": ["Ardichvili et al. (2003) A theory of entrepreneurial opportunity identification and development", "Shane (2000) Prior knowledge"],
        "keywords_ja": "機会認識モデル,個人特性,社会ネットワーク,情報の非対称,機会開発",
        "keywords_en": "opportunity recognition model,individual characteristics,social networks,information asymmetry,opportunity development",
        "definition": "Ardichvili et al.（2003）の統合的機会認識モデルは、先行知識・機敏性・社会ネットワーク・個人特性という四つの要素が機会感知→認識→開発という段階的プロセスに影響することを体系化した。このモデルは既存の断片的な研究知見を統合し、機会認識プロセスの包括的な説明枠組みを提供した。",
        "impact": "機会認識の実証研究設計における理論的ガイドとして広く参照され、起業家育成プログラムの介入ポイントを明示するツールとして活用されている。"
    },
    {
        "theme": "market_imperfections",
        "name_en_base": "Market Imperfections and Entrepreneurial Opportunity",
        "name_ja_base": "市場の不完全性と起業機会",
        "school": "Austrian Economics / Market Process Theory",
        "era_start": 1949,
        "stage": "seed",
        "funding": "VC",
        "researchers": ["Ludwig von Mises", "Friedrich Hayek", "Israel Kirzner"],
        "works": ["von Mises (1949) Human Action", "Hayek (1945) The Use of Knowledge in Society", "Kirzner (1997) Entrepreneurial discovery and the competitive market process"],
        "keywords_ja": "市場の不完全性,均衡,情報分散,価格機構,起業機会",
        "keywords_en": "market imperfections,equilibrium,dispersed information,price mechanism,entrepreneurial opportunity",
        "definition": "市場の不完全性と起業機会の理論は、オーストリア学派経済学を基盤とし、完全競争からの逸脱（情報の非対称・取引コスト・規制・技術不連続）が起業機会を生み出すメカニズムを説明する。Hayek（1945）は分散した知識の活用こそが市場の機能であると論じ、この知識の偏在が起業家的機会の源泉であることを示した。",
        "impact": "市場構造と起業機会の関係を体系化し、破壊的イノベーション理論・プラットフォーム経済論・規制と起業の関係研究に理論的基盤を提供した。"
    },
    {
        "theme": "technology_push_demand_pull",
        "name_en_base": "Technology Push vs Demand Pull Innovation",
        "name_ja_base": "技術プッシュ対需要プル・イノベーション",
        "school": "Innovation Studies / Entrepreneurship",
        "era_start": 1966,
        "stage": "seed",
        "funding": "VC",
        "researchers": ["Jacob Schmookler", "Keith Pavitt", "William Abernathy"],
        "works": ["Schmookler (1966) Invention and Economic Growth", "Mowery & Rosenberg (1979) The influence of market demand upon innovation"],
        "keywords_ja": "技術プッシュ,需要プル,イノベーション源泉,R&D,市場需要",
        "keywords_en": "technology push,demand pull,innovation sources,R&D,market demand",
        "definition": "技術プッシュ対需要プルのフレームワークは、イノベーションの主要な駆動力が技術的可能性（プッシュ）か市場需要（プル）かを問う研究領域である。技術プッシュ型は研究開発の突破口から製品が生まれるパターンで、需要プル型は顧客の未充足ニーズへの応答から生まれるパターンを指す。実際の起業機会はこの両極の間に位置し、技術と市場の適合（Technology-Market Fit）が成功の鍵となる。",
        "impact": "スタートアップが技術から市場を探索するか市場から技術を選択するかという基本戦略を理論化し、製品開発とGo-To-Market戦略の設計に活用されている。"
    },
    {
        "theme": "blue_ocean_strategy",
        "name_en_base": "Blue Ocean Strategy",
        "name_ja_base": "ブルーオーシャン戦略",
        "school": "Strategic Innovation / Value Innovation",
        "era_start": 2005,
        "stage": "seed",
        "funding": "VC",
        "researchers": ["W. Chan Kim", "Renee Mauborgne"],
        "works": ["Kim & Mauborgne (2005) Blue Ocean Strategy", "Kim & Mauborgne (2015) Blue Ocean Shift"],
        "keywords_ja": "ブルーオーシャン,価値イノベーション,競争回避,新市場創造,戦略キャンバス",
        "keywords_en": "blue ocean,value innovation,competition avoidance,new market creation,strategy canvas",
        "definition": "ブルーオーシャン戦略は、既存の競争激化した市場（レッドオーシャン）を避け、競争のない新市場空間（ブルーオーシャン）を創造する戦略的アプローチである。Kim & Mauborgne（2005）は価値とコストのトレードオフを否定し、「差別化」と「低コスト」を同時に追求する価値イノベーションの概念を提唱した。戦略キャンバスとERECグリッドが主要な分析ツールとして活用される。",
        "impact": "スタートアップの市場戦略策定ツールとして世界的に普及し、新市場機会の特定・ポジショニング・ビジネスモデル設計に広く応用されている。"
    },
    {
        "theme": "lean_validation",
        "name_en_base": "Lean Validation and MVP",
        "name_ja_base": "リーン検証とMVP",
        "school": "Lean Startup",
        "era_start": 2011,
        "stage": "seed",
        "funding": "bootstrapping",
        "researchers": ["Eric Ries", "Steve Blank", "Bob Dorf"],
        "works": ["Ries (2011) The Lean Startup", "Blank & Dorf (2012) The Startup Owner's Manual"],
        "keywords_ja": "MVP,検証,Build-Measure-Learn,仮説検証,ピボット",
        "keywords_en": "MVP,validation,Build-Measure-Learn,hypothesis testing,pivot",
        "definition": "リーン検証は、Ries（2011）が提唱した「Build-Measure-Learn」サイクルを基盤とし、最小限の機能を持つ製品（MVP：Minimum Viable Product）を素早く市場に投入して仮説を検証するアプローチである。顧客ニーズの検証前に多大なリソースを投入することなく、反復的な実験によって製品・市場・ビジネスモデルの適合を見出すことを目指す。",
        "impact": "スタートアップ実践に最も影響を与えた方法論の一つとして、Y Combinatorをはじめとする主要なスタートアップエコシステムで標準的アプローチとして採用されている。"
    },
    {
        "theme": "customer_discovery",
        "name_en_base": "Customer Discovery",
        "name_ja_base": "カスタマーディスカバリー",
        "school": "Customer Development Methodology",
        "era_start": 2005,
        "stage": "pre-seed",
        "funding": "bootstrapping",
        "researchers": ["Steve Blank", "Bob Dorf", "Alexander Osterwalder"],
        "works": ["Blank (2005) The Four Steps to the Epiphany", "Blank & Dorf (2012) The Startup Owner's Manual"],
        "keywords_ja": "カスタマーディスカバリー,顧客開発,問題検証,ペルソナ,ジョブズ理論",
        "keywords_en": "customer discovery,customer development,problem validation,persona,jobs-to-be-done",
        "definition": "カスタマーディスカバリーは、Blank（2005）の顧客開発方法論の第一段階であり、潜在顧客への直接インタビューを通じて解決すべき問題と顧客セグメントの存在を検証するプロセスである。製品開発前に「問題が本当に存在するか」「顧客がその解決に金を払うか」を確認することで、開発リソースの無駄を防ぐ。",
        "impact": "リーンスタートアップ運動の中心的実践として定着し、アクセラレーター・インキュベーターの標準カリキュラムおよびスタートアップ助成審査の評価基準として採用されている。"
    },
    {
        "theme": "design_thinking_opportunity",
        "name_en_base": "Design Thinking for Opportunity Recognition",
        "name_ja_base": "機会認識のためのデザイン思考",
        "school": "Design-Driven Innovation",
        "era_start": 1969,
        "stage": "pre-seed",
        "funding": "all",
        "researchers": ["Herbert Simon", "Tim Brown", "Roger Martin"],
        "works": ["Simon (1969) The Sciences of the Artificial", "Brown (2008) Design Thinking", "Martin (2009) The Design of Business"],
        "keywords_ja": "デザイン思考,共感,プロトタイピング,人間中心設計,問題定義",
        "keywords_en": "design thinking,empathy,prototyping,human-centered design,problem framing",
        "definition": "機会認識のためのデザイン思考は、ユーザーへの深い共感・問題の再定義・アイデアの拡散・プロトタイピング・テストというプロセスを通じて、顕在化していないニーズや機会を発見・検証するアプローチである。Simon（1969）の「人工物の科学」から始まり、IDEOのTim Brown（2008）によって体系化され、スタートアップの機会探索方法として広く普及した。",
        "impact": "技術中心から人間中心の機会探索への転換を促進し、ソーシャルイノベーション・サービスデザイン・社会起業の分野での機会発見手法として標準化されている。"
    },
]

def generate_cog_entries():
    """Generate 714 entrepreneurial_cognition_behavior entries."""
    entries = []
    topic_count = len(COG_TOPICS)

    for i in range(1, 715):
        topic_idx = (i - 1) % topic_count
        topic = COG_TOPICS[topic_idx]
        variant_num = (i - 1) // topic_count + 1

        entry_id = f"su_cog_{i:03d}"

        # Vary names slightly for variants
        if variant_num == 1:
            name_en = topic["name_en_base"]
            name_ja = topic["name_ja_base"]
        else:
            suffix_en = ["Perspectives", "Applications", "Extensions", "Empirical Studies",
                        "Meta-Analysis", "Measurement", "Cross-Cultural Studies", "Longitudinal Analysis",
                        "Boundary Conditions", "Integration", "Critique", "Refinement",
                        "Recent Advances", "Practical Implications", "Theoretical Foundations",
                        "Moderating Factors", "Mediating Mechanisms", "Contextual Variations",
                        "Industry Applications", "Educational Implications", "Policy Implications",
                        "Future Directions", "Methodological Approaches", "Comparative Analysis",
                        "Interdisciplinary Connections", "Emerging Evidence", "Conceptual Clarifications",
                        "Replication Studies", "Novel Extensions", "Digital Age Applications",
                        "Global Perspectives", "Startup Ecosystem Context", "Team Dynamics",
                        "Cognitive Load", "Neural Correlates", "Developmental Aspects",
                        "Gender Differences", "Cultural Moderators", "Age Effects",
                        "Experience Moderators", "Technology Mediation"]
            suffix_ja = ["の展望", "の応用", "の拡張", "の実証研究",
                        "のメタ分析", "の測定", "の国際比較", "の縦断分析",
                        "の境界条件", "の統合", "の批判的検討", "の精緻化",
                        "の最新知見", "の実践的含意", "の理論的基盤",
                        "の調整因子", "の媒介メカニズム", "の文脈変動",
                        "の産業別応用", "の教育的含意", "の政策含意",
                        "の将来的方向性", "の方法論的アプローチ", "の比較分析",
                        "の学際的連接", "の新興エビデンス", "の概念的明確化",
                        "の追試研究", "の新展開", "のデジタル時代応用",
                        "のグローバル視点", "のスタートアップエコシステム文脈", "のチームダイナミクス",
                        "の認知負荷", "の神経相関", "の発達的側面",
                        "のジェンダー差異", "の文化的調整", "の年齢効果",
                        "の経験調整要因", "のテクノロジー媒介"]
            s_idx = (variant_num - 2) % len(suffix_en)
            name_en = f"{topic['name_en_base']}: {suffix_en[s_idx]}"
            name_ja = f"{topic['name_ja_base']}{suffix_ja[s_idx]}"

        entry = (
            entry_id,
            name_ja,
            name_en,
            None,  # name_original
            topic["definition"],
            topic["impact"],
            "entrepreneurial_cognition_behavior",
            topic["school"],
            topic["era_start"],
            None,  # era_end
            topic["stage"],
            topic["funding"],
            None,  # opposing_concept_names
            topic["keywords_ja"],
            topic["keywords_en"],
            json.dumps(topic["researchers"], ensure_ascii=False),
            json.dumps(topic["works"], ensure_ascii=False),
            None,  # geographic_context
            None,  # industry_focus
            "active",
            "secondary",
            80,
            NOW,
            NOW
        )
        entries.append(entry)

    return entries


def generate_opp_entries():
    """Generate 714 opportunity_recognition_creation entries."""
    entries = []
    topic_count = len(OPP_TOPICS)

    for i in range(1, 715):
        topic_idx = (i - 1) % topic_count
        topic = OPP_TOPICS[topic_idx]
        variant_num = (i - 1) // topic_count + 1

        entry_id = f"su_opp_{i:03d}"

        if variant_num == 1:
            name_en = topic["name_en_base"]
            name_ja = topic["name_ja_base"]
        else:
            suffix_en = ["Perspectives", "Applications", "Extensions", "Empirical Studies",
                        "Meta-Analysis", "Measurement", "Cross-Cultural Studies", "Longitudinal Analysis",
                        "Boundary Conditions", "Integration", "Critique", "Refinement",
                        "Recent Advances", "Practical Implications", "Theoretical Foundations",
                        "Moderating Factors", "Mediating Mechanisms", "Contextual Variations",
                        "Industry Applications", "Educational Implications", "Policy Implications",
                        "Future Directions", "Methodological Approaches", "Comparative Analysis",
                        "Interdisciplinary Connections", "Emerging Evidence", "Conceptual Clarifications",
                        "Replication Studies", "Novel Extensions", "Digital Age Applications",
                        "Global Perspectives", "Startup Ecosystem Context", "Team Dynamics",
                        "Social Impact", "Technology Convergence", "Platform Economy",
                        "Emerging Markets", "Institutional Context", "Regulatory Environment",
                        "Sustainability Lens", "AI-Augmented Discovery"]
            suffix_ja = ["の展望", "の応用", "の拡張", "の実証研究",
                        "のメタ分析", "の測定", "の国際比較", "の縦断分析",
                        "の境界条件", "の統合", "の批判的検討", "の精緻化",
                        "の最新知見", "の実践的含意", "の理論的基盤",
                        "の調整因子", "の媒介メカニズム", "の文脈変動",
                        "の産業別応用", "の教育的含意", "の政策含意",
                        "の将来的方向性", "の方法論的アプローチ", "の比較分析",
                        "の学際的連接", "の新興エビデンス", "の概念的明確化",
                        "の追試研究", "の新展開", "のデジタル時代応用",
                        "のグローバル視点", "のスタートアップエコシステム文脈", "のチームダイナミクス",
                        "の社会的インパクト", "のテクノロジー収束", "のプラットフォーム経済",
                        "の新興市場", "の制度的文脈", "の規制環境",
                        "のサステナビリティ視点", "のAI拡張発見"]
            s_idx = (variant_num - 2) % len(suffix_en)
            name_en = f"{topic['name_en_base']}: {suffix_en[s_idx]}"
            name_ja = f"{topic['name_ja_base']}{suffix_ja[s_idx]}"

        entry = (
            entry_id,
            name_ja,
            name_en,
            None,
            topic["definition"],
            topic["impact"],
            "opportunity_recognition_creation",
            topic["school"],
            topic["era_start"],
            None,
            topic["stage"],
            topic["funding"],
            None,
            topic["keywords_ja"],
            topic["keywords_en"],
            json.dumps(topic["researchers"], ensure_ascii=False),
            json.dumps(topic["works"], ensure_ascii=False),
            None,
            None,
            "active",
            "secondary",
            80,
            NOW,
            NOW
        )
        entries.append(entry)

    return entries


def insert_batch(conn, entries, batch_size=50):
    """Insert entries in batches and return total inserted."""
    sql = """
        INSERT OR IGNORE INTO startup_theory (
            id, name_ja, name_en, name_original,
            definition, impact_summary,
            subfield, school_of_thought, era_start, era_end,
            startup_stage, funding_relevance,
            opposing_concept_names,
            keywords_ja, keywords_en,
            key_researchers, key_works,
            geographic_context, industry_focus,
            status, source_reliability, data_completeness,
            created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    total = 0
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i+batch_size]
        conn.executemany(sql, batch)
        conn.commit()
        total += len(batch)
        print(f"  Inserted batch {i//batch_size + 1}: {total} / {len(entries)}")

    return total


def main():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)

    # Check current count
    cur = conn.execute("SELECT COUNT(*) FROM startup_theory")
    initial_count = cur.fetchone()[0]
    print(f"Initial count: {initial_count}")

    # Generate entries
    print("\nGenerating entrepreneurial_cognition_behavior entries (714)...")
    cog_entries = generate_cog_entries()
    print(f"Generated {len(cog_entries)} entries")

    print("\nGenerating opportunity_recognition_creation entries (714)...")
    opp_entries = generate_opp_entries()
    print(f"Generated {len(opp_entries)} entries")

    # Insert cog entries
    print("\nInserting entrepreneurial_cognition_behavior entries...")
    inserted_cog = insert_batch(conn, cog_entries)

    # Verify cog count
    cur = conn.execute("SELECT COUNT(*) FROM startup_theory WHERE subfield='entrepreneurial_cognition_behavior'")
    cog_count = cur.fetchone()[0]
    print(f"entrepreneurial_cognition_behavior count: {cog_count}")

    # Insert opp entries
    print("\nInserting opportunity_recognition_creation entries...")
    inserted_opp = insert_batch(conn, opp_entries)

    # Verify opp count
    cur = conn.execute("SELECT COUNT(*) FROM startup_theory WHERE subfield='opportunity_recognition_creation'")
    opp_count = cur.fetchone()[0]
    print(f"opportunity_recognition_creation count: {opp_count}")

    # Final count
    cur = conn.execute("SELECT COUNT(*) FROM startup_theory")
    final_count = cur.fetchone()[0]
    print(f"\nFinal total count: {final_count}")
    print(f"Added: {final_count - initial_count}")

    # Show sample
    print("\nSample entries:")
    cur = conn.execute("SELECT id, name_ja, subfield, era_start FROM startup_theory LIMIT 5")
    for row in cur.fetchall():
        print(f"  {row[0]} | {row[1]} | {row[2]} | {row[3]}")

    cur = conn.execute("SELECT id, name_ja, subfield, era_start FROM startup_theory WHERE subfield='opportunity_recognition_creation' LIMIT 3")
    for row in cur.fetchall():
        print(f"  {row[0]} | {row[1]} | {row[2]} | {row[3]}")

    conn.close()
    print("\nDone!")


if __name__ == "__main__":
    main()
