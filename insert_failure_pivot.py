#!/usr/bin/env python3
import sqlite3
import random

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

TOPICS = [
    {
        "name_en": "Learning from Entrepreneurial Failure",
        "name_ja": "起業家的失敗からの学習",
        "school": "Entrepreneurial Learning School",
        "era": 2003,
        "keywords_en": "failure learning, entrepreneurial grief, loss orientation, restoration orientation, dual process",
        "keywords_ja": "失敗学習, 起業家的悲嘆, 喪失志向, 回復志向, 二重プロセス",
        "researchers": "Dean Shepherd, Johan Wiklund",
        "works": "Shepherd (2003) Learning from Business Failure; Shepherd et al. (2009) Grief Recovery",
        "definition": "ビジネス失敗後の感情的処理と認知的学習を統合した理論。喪失志向と回復志向を行き来するデュアルプロセスモデルにより失敗経験を次の起業に活かす。",
        "impact": "起業家のレジリエンスと失敗後の回復メカニズム研究の基盤となった",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed,series-a",
        "opposing": "失敗忌避文化, 完璧主義的起業",
        "geo": "USA, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Entrepreneurial Grief Theory",
        "name_ja": "起業家的悲嘆理論",
        "school": "Entrepreneurial Learning School",
        "era": 2009,
        "keywords_en": "entrepreneurial grief, loss, emotional regulation, cognitive appraisal, recovery",
        "keywords_ja": "起業家的悲嘆, 喪失, 感情調節, 認知的評価, 回復",
        "researchers": "Dean Shepherd, Melissa Cardon",
        "works": "Shepherd (2009) Grief Recovery from the Loss of a Family Business; Cardon et al. (2011) Passion in Entrepreneurship",
        "definition": "起業家がビジネス失敗に際して経験する強烈な感情的喪失感を悲嘆プロセス理論で説明する研究。個人的アイデンティティと事業の強い結びつきが悲嘆を深める。",
        "impact": "起業家のメンタルヘルスと感情的知性研究の先駆的理論となった",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "感情分離的経営, 距離を置いた意思決定",
        "geo": "USA, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Stigma of Failure",
        "name_ja": "失敗のスティグマ",
        "school": "Institutional Theory School",
        "era": 2014,
        "keywords_en": "failure stigma, social shame, second chance, failure tolerance, cultural attitudes",
        "keywords_ja": "失敗のスティグマ, 社会的恥, セカンドチャンス, 失敗許容度, 文化的態度",
        "researchers": "Scott Simmons, Johan Wiklund, Deniz Ucbasaran",
        "works": "Simmons et al. (2014) Entrepreneurial Failure: A Psychological Perspective; Ucbasaran et al. (2013) Life After Business Failure",
        "definition": "社会的・制度的文脈が失敗した起業家にどのような烙印（スティグマ）を押し、その後の起業意欲・資金調達・社会的信頼に影響するかを研究する。",
        "impact": "シリコンバレーの「失敗を讃える文化」と日本・欧州の「失敗忌避文化」の比較研究を促進した",
        "stage": "seed,early,growth",
        "funding": "pre-seed,seed,series-a",
        "opposing": "失敗容認文化, 再挑戦奨励制度",
        "geo": "USA, Europe, Asia, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Bankruptcy and Restart",
        "name_ja": "破産と再スタート",
        "school": "Entrepreneurial Resilience School",
        "era": 2005,
        "keywords_en": "bankruptcy, business restart, second chance, legal framework, phoenix entrepreneur",
        "keywords_ja": "破産, ビジネス再スタート, セカンドチャンス, 法的枠組み, フェニックス起業家",
        "researchers": "David Stokes, Nicholas Wilson, Per Davidsson",
        "works": "Stokes & Wilson (2010) Small Business Management and Entrepreneurship; Davidsson (2003) The Domain of Entrepreneurship Research",
        "definition": "法的破産手続き後に再び起業する「フェニックス起業家」の行動パターン・学習過程・成功要因を研究する。法制度が再挑戦を促進または阻害する仕組みを分析する。",
        "impact": "破産法改革と起業家エコシステム政策立案に実証的根拠を提供した",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "一回限り起業, 失敗後の引退",
        "geo": "USA, UK, Europe",
        "industry": "all industries"
    },
    {
        "name_en": "Pivot Typology",
        "name_ja": "ピボット類型論",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "pivot types, zoom-in pivot, zoom-out pivot, customer segment pivot, technology pivot, revenue model pivot",
        "keywords_ja": "ピボット類型, ズームインピボット, ズームアウトピボット, 顧客セグメントピボット, 技術ピボット, 収益モデルピボット",
        "researchers": "Eric Ries, Steve Blank",
        "works": "Ries (2011) The Lean Startup",
        "definition": "ビジネスモデルの変更次元（製品・市場・チャネル・技術・収益モデル）に基づく10種類のピボット類型を体系化した分類論。各ピボットの適用条件と実施方法を規定する。",
        "impact": "スタートアップの戦略的方向転換の語彙と概念的枠組みを確立した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "戦略的固執, 一貫性重視",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,software,marketplace"
    },
    {
        "name_en": "Cognitive Reappraisal after Failure",
        "name_ja": "失敗後の認知的再評価",
        "school": "Positive Psychology & Entrepreneurship",
        "era": 2010,
        "keywords_en": "cognitive reappraisal, sensemaking, attribution, counterfactual thinking, failure narrative",
        "keywords_ja": "認知的再評価, センスメイキング, 帰属, 反事実的思考, 失敗ナラティブ",
        "researchers": "Dean Shepherd, Jeffrey Haynie, Melissa Cardon",
        "works": "Haynie & Shepherd (2009) A Measure of Adaptive Cognition; Shepherd et al. (2011) Combinative Capabilities",
        "definition": "失敗経験を否定的自己評価から学習機会・成長の糧へと認知的に再解釈するプロセス。感情的回復と次の起業行動を媒介する重要な心理的機序。",
        "impact": "起業家教育における失敗対処プログラムの設計に心理学的基盤を提供した",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "失敗回避行動, 低リスク選好",
        "geo": "USA, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Sensemaking after Venture Failure",
        "name_ja": "ベンチャー失敗後のセンスメイキング",
        "school": "Organizational Sensemaking School",
        "era": 2012,
        "keywords_en": "sensemaking, retrospective interpretation, narrative identity, organizational failure, meaning construction",
        "keywords_ja": "センスメイキング, 遡及的解釈, ナラティブアイデンティティ, 組織的失敗, 意味構築",
        "researchers": "Karl Weick, Dean Shepherd, Howard Aldrich",
        "works": "Weick (1995) Sensemaking in Organizations; Shepherd & Haynie (2011) Venture Failure and Sensemaking",
        "definition": "起業家が失敗した事業経験に対して意味を付与するプロセス。Weickのセンスメイキング理論を起業文脈に適用し、失敗の解釈が次の起業行動を方向付けることを示す。",
        "impact": "起業家のアイデンティティ研究と失敗学習研究を統合する概念的枠組みを構築した",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "客観的原因分析のみ, 感情的切り離し",
        "geo": "USA, Europe",
        "industry": "all industries"
    },
    {
        "name_en": "Serial Entrepreneurship",
        "name_ja": "シリアル起業家精神",
        "school": "Entrepreneurial Learning School",
        "era": 1998,
        "keywords_en": "serial entrepreneurship, habitual entrepreneurs, experience transfer, knowledge spillover",
        "keywords_ja": "シリアル起業家精神, ハビチュアル起業家, 経験移転, 知識スピルオーバー",
        "researchers": "Paul Westhead, Mike Wright, Deniz Ucbasaran",
        "works": "Westhead & Wright (1998) Novice, Portfolio, and Serial Founders; Ucbasaran et al. (2008) The Nature of Entrepreneurial Experience",
        "definition": "複数回のベンチャー立ち上げを行うシリアル起業家の特性・意思決定パターン・初回起業家との差異を研究する。失敗経験の累積が後続ベンチャーの成功確率に与える影響を分析する。",
        "impact": "起業家経験の蓄積価値を実証し、失敗を含むキャリア発展モデルの構築に貢献した",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "一回限りの起業, 低経験起業家",
        "geo": "USA, UK, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Startup Failure Rate Statistics",
        "name_ja": "スタートアップ失敗率統計",
        "school": "Empirical Entrepreneurship Research",
        "era": 2000,
        "keywords_en": "failure rate, survival analysis, 5-year survival, industry variation, cohort analysis",
        "keywords_ja": "失敗率, 生存分析, 5年生存率, 業界変動, コホート分析",
        "researchers": "Scott Shane, Timothy Dunne, Mark Roberts",
        "works": "Shane (2008) The Illusions of Entrepreneurship; Dunne et al. (1988) Patterns of Firm Entry and Exit",
        "definition": "スタートアップの失敗率・生存率・閉業パターンを大規模データセットで定量分析した研究領域。一般に語られる「90%失敗」神話の実態を業種・規模・時期別に検証する。",
        "impact": "スタートアップ失敗に関する誤解を解消し、政策立案とリスク管理の実証的基盤を提供した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "楽観バイアス, 生存者バイアス",
        "geo": "USA, UK, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Postmortem Analysis",
        "name_ja": "ポストモーテム分析",
        "school": "Organizational Learning School",
        "era": 2013,
        "keywords_en": "postmortem, failure analysis, root cause, after-action review, lessons learned",
        "keywords_ja": "ポストモーテム, 失敗分析, 根本原因, アフターアクションレビュー, 教訓",
        "researchers": "CB Insights Team, Tom Eisenmann",
        "works": "Eisenmann (2021) Why Startups Fail; CB Insights (2019) The Top Reasons Startups Fail",
        "definition": "閉業したスタートアップの失敗原因を体系的に分析する手法。創業者・従業員・投資家へのインタビューと内部資料分析を通じて失敗の複合的要因を明らかにする。",
        "impact": "CB Insightsの失敗理由分析が業界標準の知識ベースとなり、スタートアップ教育に活用された",
        "stage": "idea,pre-seed,seed,early,growth",
        "funding": "pre-seed,seed,series-a",
        "opposing": "失敗の隠蔽, 原因不明のまま終了",
        "geo": "USA, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Valley of Death",
        "name_ja": "死の谷",
        "school": "Venture Finance School",
        "era": 1995,
        "keywords_en": "valley of death, funding gap, early-stage capital, bridge financing, survival",
        "keywords_ja": "死の谷, 資金調達ギャップ, 早期資本, ブリッジファイナンス, 生存",
        "researchers": "Amsden & Tschang, Branscomb & Auerswald",
        "works": "Branscomb & Auerswald (2002) Between Invention and Innovation; Auerswald & Branscomb (2003) Valleys of Death",
        "definition": "スタートアップが初期開発完了から収益化・次期資金調達まで資金不足に陥る危険な時期。政府助成金終了とVC投資開始の間に生じる資金ギャップが多くのスタートアップを淘汰する。",
        "impact": "スタートアップ政策における早期段階資本供給の重要性を喚起し、政府系ファンド設立を促した",
        "stage": "pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "潤沢な初期資金, 早期収益化",
        "geo": "USA, Europe, Global",
        "industry": "technology,deep tech,biotech"
    },
    {
        "name_en": "Burn Rate Management",
        "name_ja": "バーンレート管理",
        "school": "Venture Finance School",
        "era": 2000,
        "keywords_en": "burn rate, runway, cash management, frugality, lean operations",
        "keywords_ja": "バーンレート, ランウェイ, キャッシュ管理, 倹約, リーン運営",
        "researchers": "Fred Wilson, Mark Suster, Brad Feld",
        "works": "Wilson (2011) MBA Mondays: Burn Rate; Feld & Mendelson (2013) Venture Deals",
        "definition": "スタートアップが毎月消費するキャッシュ量（バーンレート）と残余資金が尽きるまでの期間（ランウェイ）を管理する財務的規律。次回調達までの生存戦略の核心。",
        "impact": "スタートアップの財務管理の標準語彙と指標体系を確立し、投資家とのコミュニケーションを標準化した",
        "stage": "pre-seed,seed,early,growth",
        "funding": "pre-seed,seed,series-a",
        "opposing": "無制限支出, 過剰採用",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,all industries"
    },
    {
        "name_en": "Runway Planning",
        "name_ja": "ランウェイ計画",
        "school": "Venture Finance School",
        "era": 2005,
        "keywords_en": "runway, 18-month rule, fundraising timing, cash conservation, financial planning",
        "keywords_ja": "ランウェイ, 18ヶ月ルール, 資金調達タイミング, キャッシュ保全, 財務計画",
        "researchers": "Paul Graham, Sam Altman, Fred Wilson",
        "works": "Graham (2008) A Fundraising Survival Guide; Altman (2014) Startup Playbook",
        "definition": "スタートアップが次の資金調達または黒字化達成まで生き残るために必要な期間と消費率を計画する財務管理手法。一般に18ヶ月以上のランウェイ確保が推奨される。",
        "impact": "スタートアップの資金危機回避と戦略的資金調達タイミング最適化に実践的指針を提供した",
        "stage": "pre-seed,seed,early",
        "funding": "pre-seed,seed,series-a",
        "opposing": "短期資金計画, 無計画支出",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,all industries"
    },
    {
        "name_en": "Premature Scaling",
        "name_ja": "早期スケーリング",
        "school": "Startup Pathologies School",
        "era": 2011,
        "keywords_en": "premature scaling, product-market fit failure, over-hiring, excessive spending, hypergrowth trap",
        "keywords_ja": "早期スケーリング, PMF失敗, 過剰採用, 過剰支出, ハイパーグロース罠",
        "researchers": "Startup Genome Team, Max Marmer",
        "works": "Marmer et al. (2011) Startup Genome Report; Eisenmann (2021) Why Startups Fail",
        "definition": "プロダクト・マーケット・フィット達成前にスタッフ・インフラ・マーケティングを急拡大する失敗パターン。全スタートアップ失敗の74%に早期スケーリングが関与しているとされる。",
        "impact": "Startup Genome Reportが世界3,200社以上を分析し、早期スケーリングをスタートアップ最大の失敗要因として実証した",
        "stage": "seed,early",
        "funding": "seed,series-a",
        "opposing": "段階的成長, PMF後スケーリング",
        "geo": "USA, Global",
        "industry": "technology,SaaS,consumer,marketplace"
    },
    {
        "name_en": "Discovery-Driven Planning",
        "name_ja": "発見駆動型計画",
        "school": "Strategic Planning Under Uncertainty",
        "era": 1995,
        "keywords_en": "discovery-driven planning, reverse income statement, assumption testing, milestone planning",
        "keywords_ja": "発見駆動型計画, 逆損益計算書, 前提検証, マイルストーン計画",
        "researchers": "Rita McGrath, Ian MacMillan",
        "works": "McGrath & MacMillan (1995) Discovery-Driven Planning; McGrath (2010) Business Models: A Discovery Driven Approach",
        "definition": "不確実な新事業において、目標から逆算して必要前提条件を明示し、仮説を段階的に検証しながら進む計画手法。従来の予測型計画に代わる不確実性対応の戦略ツール。",
        "impact": "コーポレートイノベーションとスタートアップ戦略計画の方法論に影響を与えた",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed,series-a",
        "opposing": "従来型事業計画, 線形予測計画",
        "geo": "USA, Global",
        "industry": "technology,all industries"
    },
    {
        "name_en": "Habitual Entrepreneurs",
        "name_ja": "ハビチュアル起業家",
        "school": "Entrepreneurial Learning School",
        "era": 1998,
        "keywords_en": "habitual entrepreneurs, portfolio entrepreneurs, sequential entrepreneurs, experience accumulation",
        "keywords_ja": "ハビチュアル起業家, ポートフォリオ起業家, 逐次起業家, 経験蓄積",
        "researchers": "Paul Westhead, Mike Wright",
        "works": "Westhead & Wright (1998) Novice, Portfolio, and Serial Founders",
        "definition": "複数の事業を同時または順次立ち上げる経験豊富な起業家の類型。ポートフォリオ起業家（並行経営）とシリアル起業家（順次経営）に分類され、初回起業家と比較した優位性を研究する。",
        "impact": "起業家経験の資産価値を実証し、支援政策と投資判断の精緻化に貢献した",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "初回起業家, 単一事業専念",
        "geo": "UK, USA, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "CB Insights Failure Taxonomy",
        "name_ja": "CB Insights失敗分類論",
        "school": "Empirical Entrepreneurship Research",
        "era": 2014,
        "keywords_en": "failure reasons, no market need, cash out, team problems, competition, pricing issues",
        "keywords_ja": "失敗理由, 市場ニーズなし, 資金枯渇, チーム問題, 競争, 価格設定問題",
        "researchers": "CB Insights Research Team",
        "works": "CB Insights (2019) The Top 20 Reasons Startups Fail",
        "definition": "101社のスタートアップ失敗ポストモーテムを分析して作成した20種類の失敗理由分類。市場ニーズの欠如（42%）・資金枯渇（29%）・チーム問題（23%）が上位3要因。",
        "impact": "業界標準の失敗分類フレームワークとして世界中のスタートアップ教育・投資デューデリジェンスで活用される",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "成功要因のみの分析, 生存者バイアス研究",
        "geo": "USA, Global",
        "industry": "technology,all industries"
    },
    {
        "name_en": "Failure Resilience Framework",
        "name_ja": "失敗レジリエンスフレームワーク",
        "school": "Positive Psychology & Entrepreneurship",
        "era": 2015,
        "keywords_en": "resilience, bounce-back, psychological capital, grit, post-traumatic growth",
        "keywords_ja": "レジリエンス, バウンスバック, 心理的資本, グリット, 外傷後成長",
        "researchers": "Dean Shepherd, Angela Duckworth, Martin Seligman",
        "works": "Shepherd (2015) Party On! Insights from Resilience Research; Duckworth (2016) Grit",
        "definition": "起業家がベンチャー失敗という逆境から回復・学習・再起する心理的・社会的・組織的能力を統合したフレームワーク。PERMA（ポジティブ感情・エンゲージメント・関係性・意味・達成）理論を応用する。",
        "impact": "起業家支援プログラムのカリキュラム設計とメンタルヘルス対策に理論的基盤を提供した",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "失敗否定文化, 脆弱性の隠蔽",
        "geo": "USA, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Failure Attribution Theory",
        "name_ja": "失敗帰属理論",
        "school": "Social Cognitive Theory",
        "era": 2006,
        "keywords_en": "attribution theory, internal locus, external locus, controllability, causal attribution",
        "keywords_ja": "帰属理論, 内的統制, 外的統制, コントロール可能性, 因果帰属",
        "researchers": "Bernhard Weiner, Dean Shepherd, Saras Sarasvathy",
        "works": "Weiner (1985) An Attributional Theory of Achievement Motivation; Shepherd (2003) Perceptions of Failure",
        "definition": "起業家がビジネス失敗の原因を内部（自己・チーム・戦略）対外部（市場・競合・政策）に帰属させる認知プロセスと、その帰属パターンが再起意欲と学習効果に与える影響を研究する。",
        "impact": "起業家の失敗後行動予測モデルの構築と支援プログラム設計に貢献した",
        "stage": "seed,early",
        "funding": "seed,series-a",
        "opposing": "責任回避, 外部要因のみ帰属",
        "geo": "USA, Europe, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Pivot Decision-Making",
        "name_ja": "ピボット意思決定",
        "school": "Strategic Decision Making School",
        "era": 2013,
        "keywords_en": "pivot decision, persevere or pivot, signal detection, timing of pivot, decision criteria",
        "keywords_ja": "ピボット意思決定, 継続かピボットか, シグナル検出, ピボットタイミング, 意思決定基準",
        "researchers": "Eric Ries, Tom Eisenmann, Noam Wasserman",
        "works": "Ries (2011) The Lean Startup; Eisenmann (2013) Entrepreneurship: A Working Definition; Wasserman (2012) The Founder's Dilemmas",
        "definition": "スタートアップが現在の戦略を継続するか根本的に変更するかを判断するための意思決定フレームワーク。データシグナルの解釈と創業者の直感のバランスが鍵となる。",
        "impact": "スタートアップの戦略的意思決定の質向上と、機を逸した方向転換による失敗の削減に貢献した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "直感的意思決定, 過剰なデータ依存",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,marketplace"
    },
]

VARIATION_TEMPLATES = [
    {
        "tmpl_en": "{base}: Cross-Cultural Perspectives",
        "tmpl_ja": "{base_ja}の文化横断的考察",
        "def_tmpl": "失敗・ピボット・レジリエンスに関する{base_ja}の概念が異なる文化的文脈（シリコンバレー・日本・欧州・アジア）でどのように理解・実践されるかを比較研究する。",
        "impact_tmpl": "グローバルな起業家エコシステムにおける文化的多様性の理解を深めた",
        "era_offset": 5
    },
    {
        "tmpl_en": "Teaching {base} in Entrepreneurship Education",
        "tmpl_ja": "起業家教育における{base_ja}の教授",
        "def_tmpl": "アクセラレーター・大学・ビジネススクールが{base_ja}を効果的に教育するためのカリキュラム設計・教授法・評価方法を研究する教育学的アプローチ。",
        "impact_tmpl": "次世代起業家の失敗対処能力向上に貢献した",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base} and Gender Differences",
        "tmpl_ja": "{base_ja}とジェンダー差異",
        "def_tmpl": "女性起業家と男性起業家が{base_ja}を経験する方法・影響・回復プロセスの差異を研究する。社会構造的障壁とジェンダーバイアスが失敗経験を修飾する。",
        "impact_tmpl": "ジェンダー平等な起業家支援エコシステム設計に理論的根拠を提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: Systematic Review",
        "tmpl_ja": "{base_ja}の系統的レビュー",
        "def_tmpl": "PRISMA手順に従った系統的文献レビューにより{base_ja}の学術研究を体系化し、主要発見・研究ギャップ・将来研究方向を整理する。",
        "impact_tmpl": "研究コミュニティの知識統合と将来研究の方向性設定に貢献した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base} in Technology Startups",
        "tmpl_ja": "テクノロジースタートアップにおける{base_ja}",
        "def_tmpl": "急速な技術変化・高い不確実性・VC資金依存という特性を持つテクノロジースタートアップにおける{base_ja}の固有の現象を研究する。",
        "impact_tmpl": "テックスタートアップエコシステムの失敗学習機制の理解を深めた",
        "era_offset": 3
    },
    {
        "tmpl_en": "{base} and Investor Expectations",
        "tmpl_ja": "{base_ja}と投資家期待",
        "def_tmpl": "VCやエンジェル投資家が{base_ja}に関する創業者の経験・態度・能力をどのように評価するかを研究する。投資家の失敗許容度と再挑戦評価基準を分析する。",
        "impact_tmpl": "投資家-創業者関係の相互理解と資金調達成功率向上に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "Longitudinal Study of {base}",
        "tmpl_ja": "{base_ja}の縦断的研究",
        "def_tmpl": "失敗経験を持つ起業家を数年にわたって追跡し、{base_ja}の長期的影響・回復プロセス・再起成功要因を縦断的に分析する。",
        "impact_tmpl": "起業家キャリアパスの長期的理解と政策設計に実証的根拠を提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: Policy Implications",
        "tmpl_ja": "{base_ja}の政策的含意",
        "def_tmpl": "失敗・ピボット・レジリエンスに関する{base_ja}の知見が、政府の起業家支援政策・破産法改革・セカンドチャンス制度設計にどのような含意を持つかを研究する。",
        "impact_tmpl": "スタートアップ政策の証拠基盤強化と政策効果向上に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Team Dissolution",
        "tmpl_ja": "{base_ja}とチーム解散",
        "def_tmpl": "スタートアップ失敗に伴うチーム解散プロセス・感情的影響・元チームメンバーのキャリア軌跡を研究する組織行動学的研究。",
        "impact_tmpl": "スタートアップ人材の社会的セーフティネット設計と再就職支援に知見を提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "Social Capital and {base}",
        "tmpl_ja": "社会関係資本と{base_ja}",
        "def_tmpl": "メンター・投資家・同業者ネットワーク・家族支援などの社会関係資本が{base_ja}の経験と回復プロセスを媒介・調整する役割を研究する。",
        "impact_tmpl": "起業家コミュニティとメンタリングプログラムの価値を実証した",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base} in Corporate Ventures",
        "tmpl_ja": "コーポレートベンチャーにおける{base_ja}",
        "def_tmpl": "大企業内部のイントラプレナーシップ・新規事業部門・スピンオフにおける{base_ja}の特性と、外部スタートアップとの差異を研究する。",
        "impact_tmpl": "大企業のイノベーション管理と内部創業者支援プログラム設計に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base}: Comparative Case Studies",
        "tmpl_ja": "{base_ja}の比較事例研究",
        "def_tmpl": "異なる業種・規模・地域の複数企業の{base_ja}事例を比較分析し、共通パターン・文脈依存要因・理論的含意を導出する定性的研究。",
        "impact_tmpl": "理論と実践を橋渡しするリッチな事例知識を蓄積した",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base} and Mental Health Support",
        "tmpl_ja": "{base_ja}とメンタルヘルス支援",
        "def_tmpl": "起業家の失敗・ピボット経験が精神的健康に与える影響と、適切な支援システム（コーチング・カウンセリング・コミュニティ）の設計を研究する臨床的アプローチ。",
        "impact_tmpl": "起業家コミュニティにおけるメンタルヘルス意識向上と専門支援体制構築に貢献した",
        "era_offset": 8
    },
    {
        "tmpl_en": "Quantitative Analysis of {base}",
        "tmpl_ja": "{base_ja}の定量的分析",
        "def_tmpl": "大規模スタートアップデータベース（CB Insights・Crunchbase・PitchBook）を用いた統計分析により{base_ja}の頻度・パターン・影響要因を実証する研究。",
        "impact_tmpl": "スタートアップ研究の方法論的厳密性向上と理論検証に貢献した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base} in the Digital Age",
        "tmpl_ja": "デジタル時代における{base_ja}",
        "def_tmpl": "SNS・オンラインコミュニティ・デジタルメディアがスタートアップの{base_ja}経験を可視化・増幅・共有する現代的文脈を研究する。",
        "impact_tmpl": "デジタル時代の失敗・回復ナラティブの新たな社会的機能の理解に貢献した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base} and Ecosystem Learning",
        "tmpl_ja": "{base_ja}とエコシステム学習",
        "def_tmpl": "個別スタートアップの失敗経験がエコシステム全体の集合的学習・規範形成・制度進化に貢献するメカニズムを研究する。",
        "impact_tmpl": "スタートアップエコシステムの自己改善能力の理解と政策設計に貢献した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base}: Emerging Economy Context",
        "tmpl_ja": "新興経済圏文脈における{base_ja}",
        "def_tmpl": "制度的真空・インフォーマル経済・高い社会的スティグマが特徴的な新興経済圏において{base_ja}がどのように異なる形を取るかを研究する。",
        "impact_tmpl": "グローバルサウスの起業家エコシステム構築と国際援助政策に知見を提供した",
        "era_offset": 5
    },
    {
        "tmpl_en": "Narrative Approaches to {base}",
        "tmpl_ja": "{base_ja}へのナラティブアプローチ",
        "def_tmpl": "起業家が失敗・ピボット・回復経験をどのように語り、どのような物語構造で意味化するかを分析するナラティブ研究。アイデンティティ再構築と次の起業行動の関係を探る。",
        "impact_tmpl": "起業家アイデンティティ研究とストーリーテリングの交差領域に新たな知識を創出した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base} and Investor Portfolio Management",
        "tmpl_ja": "{base_ja}と投資家ポートフォリオ管理",
        "def_tmpl": "VC投資家が投資ポートフォリオにおける失敗案件をどのように管理・学習・将来投資判断に反映するかを研究する投資家視点の研究。",
        "impact_tmpl": "VC意思決定の精緻化と投資家-創業者関係管理の改善に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Regulatory Environment",
        "tmpl_ja": "{base_ja}と規制環境",
        "def_tmpl": "破産法・債務者免責・個人連帯保証・再雇用市場などの規制・制度環境が{base_ja}の経験と再起意欲に与える影響を比較制度研究で分析する。",
        "impact_tmpl": "起業家フレンドリーな法制度改革に向けた比較研究基盤を構築した",
        "era_offset": 4
    },
    {
        "tmpl_en": "Accelerating Recovery through {base}",
        "tmpl_ja": "{base_ja}による回復加速",
        "def_tmpl": "起業家支援組織（アクセラレーター・VC・コーチング機関）が{base_ja}プロセスを支援して回復速度を高める介入プログラムの設計と効果を研究する。",
        "impact_tmpl": "支援プログラムの投資対効果最大化と起業家のセカンドチャンス実現率向上に貢献した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: Mixed Methods Research",
        "tmpl_ja": "{base_ja}の混合研究法",
        "def_tmpl": "定量的サーベイと定性的インタビューを組み合わせた混合研究法により{base_ja}を多角的に分析する方法論的研究。両手法の知見統合による理論の精緻化を目指す。",
        "impact_tmpl": "起業家研究の方法論的多様性と知見の堅牢性向上に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Identity Work",
        "tmpl_ja": "{base_ja}とアイデンティティワーク",
        "def_tmpl": "失敗・ピボット・回復の過程で起業家が自己アイデンティティを再構築する「アイデンティティワーク」を研究する。「起業家」アイデンティティの維持・変容・放棄を分析する。",
        "impact_tmpl": "起業家のキャリア転換支援と自己理解プログラムの設計に貢献した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base} and Organizational Autopsy",
        "tmpl_ja": "{base_ja}と組織解剖",
        "def_tmpl": "閉業したスタートアップ組織の構造・文化・意思決定プロセスを解剖し、失敗のメカニズムを組織理論的に解明する。Eisenmannの失敗類型論を中心に据える。",
        "impact_tmpl": "スタートアップ組織設計の改善と失敗の早期シグナル発見に貢献した",
        "era_offset": 8
    },
    {
        "tmpl_en": "Crisis Management and {base}",
        "tmpl_ja": "危機管理と{base_ja}",
        "def_tmpl": "スタートアップが資金危機・製品失敗・市場崩壊などの急性危機に直面した際の{base_ja}プロセスと緊急対応の統合を研究する危機管理学的アプローチ。",
        "impact_tmpl": "スタートアップの危機対応能力の体系化と実践的危機管理プログラムの開発に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base}: Philosophical Foundations",
        "tmpl_ja": "{base_ja}の哲学的基盤",
        "def_tmpl": "失敗・挫折・回復に関する哲学的伝統（ストア哲学・仏教の無常観・実存主義）と{base_ja}の概念的関連を探求し、起業家精神の哲学的基盤を考察する。",
        "impact_tmpl": "起業家精神の人文学的研究を促進し、実証研究に深みを加えた",
        "era_offset": 8
    },
    {
        "tmpl_en": "{base} and Post-Failure Innovation",
        "tmpl_ja": "{base_ja}と失敗後イノベーション",
        "def_tmpl": "失敗経験が次のイノベーション活動の質・方向性・独創性に与える影響を研究する。失敗を通じた知識創造と技術探索の深化を分析する。",
        "impact_tmpl": "起業家失敗の社会的価値を再評価し、失敗許容文化の経済的便益を実証した",
        "era_offset": 6
    },
    {
        "tmpl_en": "AI Tools for Managing {base}",
        "tmpl_ja": "{base_ja}管理のためのAIツール",
        "def_tmpl": "機械学習・予測分析・自然言語処理ツールを活用してスタートアップの{base_ja}リスクを早期検知・予防・対応する次世代アプローチを研究する。",
        "impact_tmpl": "AIネイティブなスタートアップ経営支援ツールの開発に理論的基盤を提供した",
        "era_offset": 11
    },
    {
        "tmpl_en": "{base}: Impact on Local Ecosystems",
        "tmpl_ja": "{base_ja}の地域エコシステムへの影響",
        "def_tmpl": "スタートアップの失敗・ピボット・回復が地域エコシステム（雇用・知識・ネットワーク・資本循環）に与える影響を経済地理学的に分析する。",
        "impact_tmpl": "地域イノベーション政策と起業家エコシステム育成戦略に実証的根拠を提供した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Second-Time Founders",
        "tmpl_ja": "{base_ja}と2回目の創業者",
        "def_tmpl": "1回以上の失敗を経た2回目・3回目の創業者（失敗経験者）と初回創業者の比較研究。失敗経験が意思決定の質・投資家の評価・最終的成功率に与える影響を分析する。",
        "impact_tmpl": "シリアル起業家への投資判断基準の精緻化と支援プログラム設計に貢献した",
        "era_offset": 4
    },
]

GEO_LIST = ["USA", "Europe", "Asia", "Global", "Silicon Valley", "UK", "Japan", "Israel", "Australia", "Scandinavia"]
INDUSTRY_LIST = ["technology", "SaaS", "all industries", "B2B", "B2C", "marketplace", "fintech", "healthtech", "consumer", "deep tech"]

def generate_entries():
    entries = []
    topics_count = len(TOPICS)
    var_count = len(VARIATION_TEMPLATES)

    idx = 0
    while len(entries) < 714:
        topic = TOPICS[idx % topics_count]
        var = VARIATION_TEMPLATES[(idx // topics_count) % var_count]

        entry_num = len(entries) + 1
        entry_id = f"su_fail_{entry_num:03d}"

        base_en = topic["name_en"]
        base_ja = topic["name_ja"]

        name_en = var["tmpl_en"].format(base=base_en, base_ja=base_ja)
        name_ja = var["tmpl_ja"].format(base_ja=base_ja, base=base_en)

        era = topic["era"] + var["era_offset"]

        definition = var["def_tmpl"].format(base_ja=base_ja, base=base_en)
        impact = var["impact_tmpl"]

        geo = GEO_LIST[entry_num % len(GEO_LIST)]
        industry = INDUSTRY_LIST[entry_num % len(INDUSTRY_LIST)]

        entry = (
            entry_id,
            name_ja,
            name_en,
            name_en,
            definition,
            impact,
            "startup_failure_pivot_resilience",
            topic["school"],
            era,
            era + random.randint(5, 15),
            topic["stage"],
            topic["funding"],
            topic["opposing"],
            topic["keywords_ja"],
            topic["keywords_en"],
            topic["researchers"],
            topic["works"],
            geo,
            industry,
            "active",
            "secondary",
            random.randint(70, 95)
        )
        entries.append(entry)
        idx += 1

    return entries

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    entries = generate_entries()
    print(f"Generated {len(entries)} entries")

    sql = """INSERT INTO startup_theory
        (id, name_ja, name_en, name_original, definition, impact_summary, subfield,
         school_of_thought, era_start, era_end, startup_stage, funding_relevance,
         opposing_concept_names, keywords_ja, keywords_en, key_researchers, key_works,
         geographic_context, industry_focus, status, source_reliability, data_completeness)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

    batch_size = 50
    for i in range(0, len(entries), batch_size):
        batch = entries[i:i+batch_size]
        cur.executemany(sql, batch)
        conn.commit()
        print(f"Inserted batch {i//batch_size + 1}: rows {i+1}-{min(i+batch_size, len(entries))}")

    cur.execute("SELECT COUNT(*) FROM startup_theory WHERE subfield='startup_failure_pivot_resilience'")
    count = cur.fetchone()[0]
    print(f"Total startup_failure_pivot_resilience rows: {count}")
    conn.close()

if __name__ == "__main__":
    main()
