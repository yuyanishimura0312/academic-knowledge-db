#!/usr/bin/env python3
import sqlite3
import random

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

TOPICS = [
    {
        "name_en": "Blitzscaling",
        "name_ja": "ブリッツスケーリング",
        "school": "Hypergrowth Strategy School",
        "era": 2018,
        "keywords_en": "blitzscaling, hypergrowth, speed over efficiency, first-mover advantage, market capture",
        "keywords_ja": "ブリッツスケーリング, 超高速成長, 効率より速度, 先行者優位, 市場獲得",
        "researchers": "Reid Hoffman, Chris Yeh",
        "works": "Hoffman & Yeh (2018) Blitzscaling",
        "definition": "市場の不確実性にもかかわらず効率より速度を優先して急速にスケールする戦略。ネットワーク効果のある市場での先行者優位を獲得するため、意図的に非効率を受け入れる。",
        "impact": "Airbnb・LinkedIn・Uberなどのユニコーン企業の成長戦略を説明する理論的枠組みとなった",
        "stage": "early,growth,late",
        "funding": "series-a,series-b,series-c",
        "opposing": "段階的成長, 収益性重視経営, ゆっくりとした持続的成長",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,marketplace,SaaS,consumer"
    },
    {
        "name_en": "Scaling Up (Rockefeller Habits)",
        "name_ja": "スケーリングアップ（ロックフェラーの習慣）",
        "school": "Execution Excellence School",
        "era": 2014,
        "keywords_en": "scaling up, Rockefeller habits, OKR, execution rhythm, one-page strategic plan",
        "keywords_ja": "スケーリングアップ, ロックフェラーの習慣, OKR, 実行リズム, 1ページ戦略計画",
        "researchers": "Verne Harnish",
        "works": "Harnish (2014) Scaling Up; Harnish (2002) Mastering the Rockefeller Habits",
        "definition": "成長企業がスタートアップ段階から中堅企業へ移行する際の4つの決定（人材・戦略・実行・キャッシュ）を体系化したフレームワーク。",
        "impact": "世界40,000社以上が採用し、成長期スタートアップの経営体制整備に貢献した",
        "stage": "growth,late",
        "funding": "series-b,series-c",
        "opposing": "スタートアップ的混沌, 非組織的成長",
        "geo": "USA, Global",
        "industry": "technology,manufacturing,services"
    },
    {
        "name_en": "Network Effects Theory",
        "name_ja": "ネットワーク効果理論",
        "school": "Platform Economics School",
        "era": 1974,
        "keywords_en": "network effects, Metcalfe's law, direct network effects, indirect network effects, winner-take-all",
        "keywords_ja": "ネットワーク効果, メトカーフの法則, 直接ネットワーク効果, 間接ネットワーク効果, 勝者総取り",
        "researchers": "Robert Metcalfe, Geoffrey Parker, Marshall Van Alstyne, Sangeet Paul Choudary",
        "works": "Parker et al. (2016) Platform Revolution; Eisenmann et al. (2006) Strategies for Two-Sided Markets",
        "definition": "ユーザー数の増加が製品・サービスの価値を指数関数的に高める現象。直接ネットワーク効果（同一グループ内）と間接ネットワーク効果（異なるグループ間）が存在する。",
        "impact": "Facebook・WhatsApp・Uberなどのプラットフォーム企業の競争優位を説明する中核理論となった",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "製品差別化戦略, 単体製品競争",
        "geo": "USA, Global",
        "industry": "marketplace,social,technology,fintech"
    },
    {
        "name_en": "Winner-Take-All Markets",
        "name_ja": "勝者総取り市場",
        "school": "Platform Economics School",
        "era": 1981,
        "keywords_en": "winner-take-all, superstar economics, market concentration, platform dominance",
        "keywords_ja": "勝者総取り, スーパースター経済学, 市場集中, プラットフォーム支配",
        "researchers": "Sherwin Rosen, Robert Frank, Philip Cook",
        "works": "Rosen (1981) The Economics of Superstars; Frank & Cook (1995) The Winner-Take-All Society",
        "definition": "少数の最優秀プレーヤーが市場の大半を占有する経済構造。デジタル経済においてネットワーク効果と低限界コストにより一層強化される。",
        "impact": "テクノロジー産業の寡占化傾向を説明し、スタートアップの競争戦略に根本的影響を与えた",
        "stage": "growth,late",
        "funding": "series-b,series-c",
        "opposing": "完全競争市場, 多様性市場",
        "geo": "USA, Global",
        "industry": "technology,platform,media,software"
    },
    {
        "name_en": "S-Curve Technology Adoption",
        "name_ja": "S字曲線技術採用モデル",
        "school": "Diffusion of Innovation School",
        "era": 1962,
        "keywords_en": "S-curve, technology adoption, diffusion of innovation, early majority, late majority",
        "keywords_ja": "S字曲線, 技術採用, イノベーションの普及, アーリーマジョリティ, レイトマジョリティ",
        "researchers": "Everett Rogers, Richard Foster",
        "works": "Rogers (1962) Diffusion of Innovations; Foster (1986) Innovation: The Attacker's Advantage",
        "definition": "新技術・製品の市場浸透率が時間とともにS字型曲線を描く現象。イノベーター・アーリーアダプター・アーリーマジョリティ・レイトマジョリティ・ラガードの5段階で普及が進む。",
        "impact": "スタートアップのタイミング戦略と製品ロードマップ設計の理論基盤となった",
        "stage": "early,growth,late",
        "funding": "series-a,series-b,series-c",
        "opposing": "線形成長モデル, 段階的採用",
        "geo": "USA, Global",
        "industry": "technology,consumer,B2B"
    },
    {
        "name_en": "Viral Coefficient",
        "name_ja": "バイラル係数",
        "school": "Growth Hacking School",
        "era": 2008,
        "keywords_en": "viral coefficient, K-factor, viral loop, referral growth, word-of-mouth",
        "keywords_ja": "バイラル係数, K係数, バイラルループ, 紹介成長, 口コミ",
        "researchers": "David Skok, Andrew Chen",
        "works": "Skok (2009) Startup Metrics That Matter; Chen (2007) The Law of Shitty Clickthroughs",
        "definition": "既存ユーザー1人が平均して何人の新規ユーザーを招待するかを示す指標。K>1で指数関数的成長が発生し、K<1では外部マーケティングへの依存が続く。",
        "impact": "Dropbox・Hotmail・PayPalのバイラル成長戦略の理論的基盤となった",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "有料獲得成長, 営業主導成長",
        "geo": "Silicon Valley, USA, Global",
        "industry": "consumer,SaaS,marketplace,social"
    },
    {
        "name_en": "Growth Loops",
        "name_ja": "グロースループ",
        "school": "Growth Hacking School",
        "era": 2019,
        "keywords_en": "growth loops, compounding growth, flywheel, product-led growth, self-reinforcing growth",
        "keywords_ja": "グロースループ, 複利的成長, フライホイール, プロダクト主導成長, 自己強化成長",
        "researchers": "Brian Balfour, Andrew Chen, Casey Winters",
        "works": "Balfour (2019) Growth Loops are the New Funnels; Chen (2021) The Cold Start Problem",
        "definition": "ユーザー獲得から価値創造・共有・再獲得までが自己強化ループを形成する成長メカニズム。ファネル思考を超えた複利的成長を実現する。",
        "impact": "Notion・Figma・Slack等のPLG（プロダクト主導成長）企業の成長戦略に影響を与えた",
        "stage": "early,growth",
        "funding": "series-a,series-b",
        "opposing": "線形ファネル思考, 広告主導成長",
        "geo": "Silicon Valley, USA, Global",
        "industry": "SaaS,productivity,B2B,marketplace"
    },
    {
        "name_en": "Unit Economics",
        "name_ja": "ユニットエコノミクス",
        "school": "Financial Modeling School",
        "era": 2010,
        "keywords_en": "unit economics, CAC, LTV, LTV/CAC ratio, payback period, contribution margin",
        "keywords_ja": "ユニットエコノミクス, CAC, LTV, LTV/CAC比率, 投資回収期間, 貢献利益",
        "researchers": "Bill Gurley, David Skok",
        "works": "Gurley (2012) The Dangerous Seduction of the Lifetime Value Formula; Skok (2009) SaaS Metrics",
        "definition": "顧客1人あたりの獲得コスト（CAC）と生涯価値（LTV）の比率を核とするビジネス収益性分析フレームワーク。健全な成長のための基本的財務指標。",
        "impact": "VCの投資判断基準として普及し、持続可能な成長戦略立案の基盤となった",
        "stage": "seed,early,growth",
        "funding": "series-a,series-b,series-c",
        "opposing": "収益無視成長, グロスメトリクス重視",
        "geo": "USA, Global",
        "industry": "SaaS,e-commerce,marketplace,subscription"
    },
    {
        "name_en": "CAC/LTV Optimization",
        "name_ja": "CAC/LTV最適化",
        "school": "Financial Modeling School",
        "era": 2012,
        "keywords_en": "customer acquisition cost, lifetime value, retention, churn reduction, expansion revenue",
        "keywords_ja": "顧客獲得コスト, 顧客生涯価値, リテンション, チャーン削減, 拡張収益",
        "researchers": "Bill Gurley, Tomasz Tunguz",
        "works": "Gurley (2014) Burn Baby Burn; Tunguz (2015) Winning with Data",
        "definition": "顧客獲得コストを最小化しながら顧客生涯価値を最大化する戦略的枠組み。チャーン削減・アップセル・クロスセルの組み合わせで最適化を追求する。",
        "impact": "SaaS企業の財務管理手法を変革し、サブスクリプションビジネスの標準指標となった",
        "stage": "early,growth,late",
        "funding": "series-a,series-b,series-c",
        "opposing": "短期収益最大化, 顧客無視成長",
        "geo": "Silicon Valley, USA, Global",
        "industry": "SaaS,subscription,B2B,e-commerce"
    },
    {
        "name_en": "Venture Funding Stages",
        "name_ja": "ベンチャー資金調達ステージ",
        "school": "Venture Capital Theory",
        "era": 1970,
        "keywords_en": "seed funding, series A, series B, pre-IPO, venture capital, term sheet",
        "keywords_ja": "シード資金調達, シリーズA, シリーズB, IPO前, ベンチャーキャピタル, タームシート",
        "researchers": "Fred Wilson, Ben Horowitz, Marc Andreessen",
        "works": "Horowitz (2014) The Hard Thing About Hard Things; Kupor (2019) Secrets of Sand Hill Road",
        "definition": "スタートアップの成長段階に応じた資金調達の体系。シード（概念実証）・シリーズA（製品市場適合）・シリーズB（スケーリング）・シリーズC以降（拡張）の各段階で異なる投資家が参加する。",
        "impact": "シリコンバレーのベンチャーエコシステムの標準的資金調達プロセスを定義した",
        "stage": "pre-seed,seed,early,growth,late",
        "funding": "pre-seed,seed,series-a,series-b,series-c",
        "opposing": "自己資金経営, 銀行融資",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,all industries"
    },
    {
        "name_en": "Hypergrowth Management",
        "name_ja": "ハイパーグロース経営",
        "school": "Hypergrowth Strategy School",
        "era": 2016,
        "keywords_en": "hypergrowth, 40% rule, organizational scaling, talent acquisition, culture preservation",
        "keywords_ja": "ハイパーグロース, 40%ルール, 組織スケーリング, 人材獲得, 文化維持",
        "researchers": "Aaron Levie, Alex Osterwalder, Andrew McAfee",
        "works": "Hoffman (2018) Blitzscaling; Ellis & Brown (2017) Hacking Growth",
        "definition": "年成長率40%以上を維持しながら組織・プロセス・文化を同時にスケールさせる経営手法。採用速度・意思決定分権化・文化コードの明文化が鍵となる。",
        "impact": "Slack・Zoom・Stripeなどの急成長SaaS企業の経営手法を理論化した",
        "stage": "growth,late",
        "funding": "series-b,series-c",
        "opposing": "安定成長経営, 漸進的拡大",
        "geo": "Silicon Valley, USA, Global",
        "industry": "SaaS,technology,marketplace"
    },
    {
        "name_en": "Scaling Culture",
        "name_ja": "文化のスケーリング",
        "school": "Organizational Culture School",
        "era": 2014,
        "keywords_en": "culture scaling, values alignment, culture fit, Netflix culture, culture deck",
        "keywords_ja": "文化のスケーリング, 価値観整合, カルチャーフィット, Netflixカルチャー, カルチャーデッキ",
        "researchers": "Patty McCord, Reed Hastings, Ben Horowitz",
        "works": "McCord (2014) Powerful: Building a Culture of Freedom and Responsibility; Horowitz (2019) What You Do Is Who You Are",
        "definition": "急速な組織拡大の中で創業時の価値観・行動規範・意思決定原則を維持・伝播させるための組織文化管理理論。",
        "impact": "Netflix・AirbnbのカルチャーデッキがITスタートアップの人事・文化管理の標準となった",
        "stage": "early,growth,late",
        "funding": "series-b,series-c",
        "opposing": "個人主義文化, 非組織的カルチャー",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,all industries"
    },
    {
        "name_en": "Technical Debt Management",
        "name_ja": "技術的負債管理",
        "school": "Software Engineering School",
        "era": 1992,
        "keywords_en": "technical debt, refactoring, code quality, architecture debt, maintainability",
        "keywords_ja": "技術的負債, リファクタリング, コード品質, アーキテクチャ負債, 保守性",
        "researchers": "Ward Cunningham, Martin Fowler",
        "works": "Cunningham (1992) The WyCash Portfolio Management System; Fowler (2018) Refactoring",
        "definition": "短期的な開発速度のために将来の改修コストを積み上げる現象。スタートアップのスケーリング過程で蓄積される技術的負債を計画的に返済する管理手法。",
        "impact": "スタートアップの開発速度と長期保守性のトレードオフ管理の概念的基盤となった",
        "stage": "early,growth,late",
        "funding": "series-a,series-b,series-c",
        "opposing": "完璧主義的コード開発, 過度な初期設計",
        "geo": "USA, Global",
        "industry": "software,technology,SaaS"
    },
    {
        "name_en": "International Expansion Strategy",
        "name_ja": "国際展開戦略",
        "school": "International Business School",
        "era": 2010,
        "keywords_en": "international expansion, localization, market entry, glocalization, regulatory compliance",
        "keywords_ja": "国際展開, ローカライズ, 市場参入, グローカライズ, 規制対応",
        "researchers": "Pankaj Ghemawat, Jan Johanson",
        "works": "Ghemawat (2007) Redefining Global Strategy; Johanson & Vahlne (1977) Internationalization Process",
        "definition": "スタートアップが母国市場での成功を基盤に新規国際市場へ拡大する際の戦略フレームワーク。市場選択・参入モード・ローカライズ戦略を体系化する。",
        "impact": "Airbnb・Uber・Spotifyなどのグローバル展開を分析する学術的枠組みとなった",
        "stage": "growth,late",
        "funding": "series-b,series-c",
        "opposing": "国内市場集中戦略, 段階的海外展開",
        "geo": "Global",
        "industry": "marketplace,consumer,SaaS,fintech"
    },
    {
        "name_en": "Marketplace Liquidity",
        "name_ja": "マーケットプレイスの流動性",
        "school": "Platform Economics School",
        "era": 2011,
        "keywords_en": "marketplace liquidity, chicken-and-egg problem, supply-demand balance, critical mass",
        "keywords_ja": "マーケットプレイス流動性, 鶏と卵問題, 供給需要バランス, クリティカルマス",
        "researchers": "Andrei Hagiu, Julian Wright, Sangeet Paul Choudary",
        "works": "Hagiu & Wright (2015) Multi-Sided Platforms; Choudary (2015) Platform Scale",
        "definition": "二面市場における供給者と需要者の十分な参加によって取引が円滑に行われる状態。鶏と卵問題の解決がマーケットプレイス起業の最重要課題となる。",
        "impact": "Airbnb・Uber・UpworkなどのP2Pマーケットプレイスの戦略設計に貢献した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "単面市場, 中央集権型プラットフォーム",
        "geo": "USA, Global",
        "industry": "marketplace,platform,sharing economy"
    },
    {
        "name_en": "Monopoly Theory (Thiel)",
        "name_ja": "独占理論（ティール）",
        "school": "Contrarian Startup Strategy",
        "era": 2014,
        "keywords_en": "monopoly, competition, proprietary technology, network effects, economies of scale, branding",
        "keywords_ja": "独占, 競争, 独自技術, ネットワーク効果, 規模の経済, ブランディング",
        "researchers": "Peter Thiel, Blake Masters",
        "works": "Thiel (2014) Zero to One",
        "definition": "スタートアップは競争を避け独占的ポジションを目指すべきという逆張り理論。独自技術・ネットワーク効果・規模の経済・ブランドの4要素で独占を構築する。",
        "impact": "PayPal・Palantir創業者の思想として広まり、スタートアップ競争戦略に反競争的視点をもたらした",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed,series-a",
        "opposing": "完全競争市場参入, 模倣戦略",
        "geo": "Silicon Valley, USA",
        "industry": "technology,deep tech,B2B"
    },
    {
        "name_en": "Crossing the Chasm",
        "name_ja": "キャズムを越える",
        "school": "Diffusion of Innovation School",
        "era": 1991,
        "keywords_en": "crossing the chasm, early market, mainstream market, bowling alley strategy, whole product",
        "keywords_ja": "キャズム, 初期市場, メインストリーム市場, ボウリングレーン戦略, ホールプロダクト",
        "researchers": "Geoffrey Moore",
        "works": "Moore (1991) Crossing the Chasm; Moore (1995) Inside the Tornado",
        "definition": "テクノロジー製品がアーリーアダプターからアーリーマジョリティへ普及する際に存在するギャップ（キャズム）を越える戦略。ニッチ市場への集中攻略を推奨する。",
        "impact": "エンタープライズソフトウェアのGTM戦略に根本的影響を与え、B2Bスタートアップの必読理論となった",
        "stage": "early,growth",
        "funding": "series-a,series-b",
        "opposing": "マスマーケット一斉投入, バイラル拡散",
        "geo": "Silicon Valley, USA, Global",
        "industry": "enterprise software,B2B,technology"
    },
    {
        "name_en": "Organic vs Paid Growth",
        "name_ja": "オーガニック成長 vs 有料成長",
        "school": "Growth Marketing School",
        "era": 2012,
        "keywords_en": "organic growth, paid acquisition, SEO, content marketing, performance marketing",
        "keywords_ja": "オーガニック成長, 有料獲得, SEO, コンテンツマーケティング, パフォーマンスマーケティング",
        "researchers": "Rand Fishkin, Andrew Chen",
        "works": "Fishkin (2018) Lost and Founder; Chen (2021) The Cold Start Problem",
        "definition": "自然検索・コンテンツ・口コミによる有機的ユーザー獲得と、広告・プロモーション費用による有料獲得の戦略的バランス。長期的にはオーガニック成長の経済性が高い。",
        "impact": "スタートアップのマーケティングミックス最適化戦略に実証的基盤を提供した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "全額有料獲得, マーケティング無視",
        "geo": "USA, Global",
        "industry": "SaaS,e-commerce,consumer,B2B"
    },
    {
        "name_en": "Flywheel Effect",
        "name_ja": "フライホイール効果",
        "school": "Good to Great Strategy School",
        "era": 2001,
        "keywords_en": "flywheel, compounding growth, Amazon flywheel, self-reinforcing loop, momentum",
        "keywords_ja": "フライホイール, 複利的成長, Amazonフライホイール, 自己強化ループ, モメンタム",
        "researchers": "Jim Collins, Jeff Bezos",
        "works": "Collins (2001) Good to Great; Bezos (2001) Amazon Annual Letter",
        "definition": "複数の成長要素が相互強化的に作用し、一度回転し始めると加速度的に成長するビジネスダイナミクス。Amazonの低価格→顧客増加→セラー増加→品揃え増加のループが典型例。",
        "impact": "Amazonの事業戦略の理論的核心として知られ、プラットフォーム企業の成長分析に広く使用される",
        "stage": "early,growth,late",
        "funding": "series-a,series-b,series-c",
        "opposing": "線形成長モデル, 単一収益源",
        "geo": "USA, Global",
        "industry": "e-commerce,marketplace,platform,SaaS"
    },
]

VARIATION_TEMPLATES = [
    {
        "tmpl_en": "{base} in the Post-Pandemic Era",
        "tmpl_ja": "パンデミック後の{base_ja}",
        "def_tmpl": "コロナ禍後のデジタル加速・リモートワーク普及・サプライチェーン再構成という文脈で{base_ja}の適用方法がどのように変化したかを研究する。",
        "impact_tmpl": "パンデミック後のスタートアップエコシステム変容を理解する理論的枠組みを提供した",
        "era_offset": 9
    },
    {
        "tmpl_en": "{base}: Academic Literature Review",
        "tmpl_ja": "{base_ja}の学術文献レビュー",
        "def_tmpl": "{base_ja}に関する主要学術論文を体系的にレビューし、理論的発展・実証的知見・未解決課題を整理した包括的文献調査。",
        "impact_tmpl": "研究者と実践者の知識共有基盤を強化した",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base} and Emerging Market Adaptation",
        "tmpl_ja": "新興市場への{base_ja}適応",
        "def_tmpl": "インド・ブラジル・ナイジェリアなどの新興市場固有の課題（インフラ・制度・文化）に対して{base_ja}をどう適応させるかを研究する。",
        "impact_tmpl": "グローバルサウスの起業家エコシステム構築に知識基盤を提供した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and ESG Integration",
        "tmpl_ja": "{base_ja}とESG統合",
        "def_tmpl": "環境・社会・ガバナンス目標を{base_ja}の成長戦略に統合する方法論を研究する。財務リターンと社会的インパクトの同時最大化を目指す。",
        "impact_tmpl": "サステナブルスタートアップの経営モデル構築に貢献した",
        "era_offset": 8
    },
    {
        "tmpl_en": "{base}: Case Study Analysis",
        "tmpl_ja": "{base_ja}のケーススタディ分析",
        "def_tmpl": "実際の企業事例（成功・失敗含む）を通じて{base_ja}の適用パターンと成果を分析する定性的研究。実践的な教訓を体系化する。",
        "impact_tmpl": "ビジネススクールケース教材として広く採用された",
        "era_offset": 3
    },
    {
        "tmpl_en": "{base} and Founder Experience",
        "tmpl_ja": "{base_ja}と創業者経験",
        "def_tmpl": "創業者の過去経験・業界知識・ネットワークが{base_ja}の実施効果に与える影響を研究する。シリアル起業家と初回起業家の差異を特に分析する。",
        "impact_tmpl": "起業家キャリア発展とスタートアップ成功の関係性理解を深めた",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base} in B2B SaaS",
        "tmpl_ja": "B2B SaaSにおける{base_ja}",
        "def_tmpl": "エンタープライズ顧客向けSaaS事業における{base_ja}の特殊な適用方法を研究する。長い営業サイクル・複雑なオンボーディング・高い解約コストを考慮した戦略。",
        "impact_tmpl": "B2B SaaSスタートアップの戦略立案と投資判断に実践的指針を提供した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base}: Quantitative Evidence",
        "tmpl_ja": "{base_ja}の定量的エビデンス",
        "def_tmpl": "大規模データセット（CB Insights・Crunchbase・PitchBook）を用いて{base_ja}の有効性を統計的に検証した実証研究。",
        "impact_tmpl": "スタートアップ研究に計量経済学的手法を導入した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base} and Board Dynamics",
        "tmpl_ja": "{base_ja}と取締役会ダイナミクス",
        "def_tmpl": "投資家・創業者・独立取締役が参加する取締役会における{base_ja}の議論・意思決定・監督機能を研究する企業ガバナンス研究。",
        "impact_tmpl": "スタートアップのコーポレートガバナンス改善に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} in the Age of AI",
        "tmpl_ja": "AI時代における{base_ja}",
        "def_tmpl": "生成AI・機械学習ツールの普及が{base_ja}をどのように変革するかを探究する。AI支援の意思決定・自動化・予測分析との統合を研究する。",
        "impact_tmpl": "AIネイティブスタートアップの経営理論構築に先進的視点を提供した",
        "era_offset": 12
    },
    {
        "tmpl_en": "{base}: Failed Applications",
        "tmpl_ja": "{base_ja}の失敗適用事例",
        "def_tmpl": "{base_ja}を誤用・過剰適用・文脈無視で適用して失敗したスタートアップ事例を分析し、よくある過ちと回避策を体系化した研究。",
        "impact_tmpl": "同種の失敗パターンを防ぐ教訓として起業家教育に活用された",
        "era_offset": 6
    },
    {
        "tmpl_en": "Integrating {base} with OKRs",
        "tmpl_ja": "{base_ja}とOKR統合",
        "def_tmpl": "Objectives and Key Resultsフレームワークと{base_ja}を統合した組織目標管理手法を研究する。Google・Intelで普及したOKRとの相互補完関係を探究する。",
        "impact_tmpl": "成長期スタートアップの戦略実行力向上に寄与した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base} and Talent Density",
        "tmpl_ja": "{base_ja}と人材密度",
        "def_tmpl": "高密度の優秀人材が集まる組織における{base_ja}の有効性と、採用・評価・報酬設計との関係を研究する。Netflixモデルの理論的検討を含む。",
        "impact_tmpl": "スタートアップの人材戦略と組織成長の最適化に貢献した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base} and Capital Efficiency",
        "tmpl_ja": "{base_ja}と資本効率",
        "def_tmpl": "限られた資本でより大きな成長を実現するための{base_ja}の活用方法を研究する。ARR/資本調達比率・バーンマルチプルなどの資本効率指標との関係を分析する。",
        "impact_tmpl": "スタートアップの持続可能な成長戦略への転換に理論的根拠を提供した",
        "era_offset": 8
    },
    {
        "tmpl_en": "Predictive Modeling of {base}",
        "tmpl_ja": "{base_ja}の予測モデリング",
        "def_tmpl": "機械学習モデルを用いて{base_ja}の成果を予測する計量的研究。スタートアップデータベースから特徴量を抽出して成長・失敗を予測する。",
        "impact_tmpl": "VCの投資デューデリジェンスと意思決定の効率化に貢献した",
        "era_offset": 9
    },
    {
        "tmpl_en": "{base} in Fintech",
        "tmpl_ja": "フィンテックにおける{base_ja}",
        "def_tmpl": "金融規制・高セキュリティ要件・既存銀行との競争という独自課題を持つフィンテック業界における{base_ja}の特殊な適用を研究する。",
        "impact_tmpl": "フィンテックスタートアップの事業モデル構築と規制対応戦略に影響を与えた",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Founder-Market Fit",
        "tmpl_ja": "{base_ja}と創業者-市場適合",
        "def_tmpl": "創業者の個人的な経験・情熱・専門性が対象市場と高度に適合している状態（創業者-市場フィット）が{base_ja}の実施効果に与える影響を研究する。",
        "impact_tmpl": "VCの創業者評価基準の精緻化に貢献した",
        "era_offset": 4
    },
    {
        "tmpl_en": "{base}: European Perspective",
        "tmpl_ja": "欧州視点からの{base_ja}",
        "def_tmpl": "シリコンバレーモデルと異なる欧州の規制環境（GDPR）・資本市場・起業家文化の文脈における{base_ja}の適用と変容を研究する比較研究。",
        "impact_tmpl": "欧州スタートアップエコシステムの固有性理解と方法論的適応に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "Accelerator Programs and {base}",
        "tmpl_ja": "アクセラレータープログラムと{base_ja}",
        "def_tmpl": "Y Combinator・Techstars等のアクセラレータープログラムが{base_ja}の普及・標準化・実践支援にどのような役割を果たしてきたかを研究する。",
        "impact_tmpl": "グローバルアクセラレーターエコシステムの知識創造と伝播機能の理解を深めた",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Burnout Prevention",
        "tmpl_ja": "{base_ja}と燃え尽き症候群予防",
        "def_tmpl": "急成長過程でのリーダーシップ・チームマネジメント・個人的健康管理と{base_ja}の実施の両立方法を研究する。持続可能な高成長を目指す。",
        "impact_tmpl": "スタートアップのウェルビーイング文化形成と長期的競争力維持に貢献した",
        "era_offset": 8
    },
    {
        "tmpl_en": "Policy Implications of {base}",
        "tmpl_ja": "{base_ja}の政策的含意",
        "def_tmpl": "{base_ja}の普及がスタートアップ政策・産業政策・教育政策に与える示唆を研究する。政府・支援機関・大学への提言を含む政策研究。",
        "impact_tmpl": "スタートアップ政策立案者への実践的ガイダンスを提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base} and Corporate Venture Capital",
        "tmpl_ja": "{base_ja}とコーポレートベンチャーキャピタル",
        "def_tmpl": "大企業がCVCを通じてスタートアップに投資する際の{base_ja}の適用と、戦略的投資家関係の構築方法を研究する。",
        "impact_tmpl": "CVC運営と大企業のオープンイノベーション戦略に実践的知見を提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: Japanese Startup Context",
        "tmpl_ja": "日本のスタートアップ文脈における{base_ja}",
        "def_tmpl": "終身雇用・リスク回避文化・系列関係が残る日本のビジネス環境において{base_ja}をどのように適用するかを研究する地域特化研究。",
        "impact_tmpl": "日本のスタートアップエコシステム発展における方法論的適応の理解に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Exit Strategy",
        "tmpl_ja": "{base_ja}と出口戦略",
        "def_tmpl": "IPO・M&A・セカンダリーセールなどの出口戦略と{base_ja}の整合性を研究する。投資家の期待と創業者のビジョンの調整方法を扱う。",
        "impact_tmpl": "スタートアップの長期戦略設計と投資家関係管理に実践的知見を提供した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base}: Sector-Specific Analysis",
        "tmpl_ja": "セクター別{base_ja}分析",
        "def_tmpl": "ヘルスケア・教育・不動産・交通など特定産業セクターにおける{base_ja}の固有の適用条件と有効性を分析する産業別比較研究。",
        "impact_tmpl": "業界特化型スタートアップ支援プログラムの設計に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Revenue Model Innovation",
        "tmpl_ja": "{base_ja}と収益モデルイノベーション",
        "def_tmpl": "サブスクリプション・フリーミアム・マーケットプレイス手数料・広告など多様な収益モデルと{base_ja}の相互作用を研究する。",
        "impact_tmpl": "スタートアップの収益モデル設計と最適化に実践的フレームワークを提供した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: Longitudinal Cohort Study",
        "tmpl_ja": "{base_ja}の縦断コホート研究",
        "def_tmpl": "複数年にわたるスタートアップコホートを追跡して{base_ja}の長期的成果を分析する縦断研究。生存分析・成長パス・出口実績を定量評価する。",
        "impact_tmpl": "スタートアップ研究の方法論的厳密性向上に貢献した",
        "era_offset": 7
    },
    {
        "tmpl_en": "Teaching {base} at Business Schools",
        "tmpl_ja": "ビジネススクールでの{base_ja}教育",
        "def_tmpl": "MBAプログラム・起業家精神コースにおける{base_ja}教育の効果的設計と実施方法を研究する教育学的研究。Stanfordやハーバードの事例を含む。",
        "impact_tmpl": "次世代起業家教育の質向上に貢献した",
        "era_offset": 5
    },
    {
        "tmpl_en": "{base} and Competitive Moat",
        "tmpl_ja": "{base_ja}と競争優位の堀",
        "def_tmpl": "コスト優位・スイッチングコスト・規模の経済・ネットワーク効果などの「堀」（competitive moat）を構築するための{base_ja}の活用方法を研究する。",
        "impact_tmpl": "スタートアップの持続的競争優位構築戦略の理論的基盤を強化した",
        "era_offset": 6
    },
    {
        "tmpl_en": "{base}: First-Principles Thinking",
        "tmpl_ja": "第一原理思考による{base_ja}",
        "def_tmpl": "イーロン・マスクやアリストテレスが提唱する第一原理思考を{base_ja}に適用し、慣習に縛られない根本的なビジネスモデル革新を探究する。",
        "impact_tmpl": "Tesla・SpaceXなどの破壊的イノベーション理解の理論的枠組みを提供した",
        "era_offset": 7
    },
    {
        "tmpl_en": "{base} across Industry Verticals",
        "tmpl_ja": "産業縦断的{base_ja}研究",
        "def_tmpl": "複数の産業縦断（ヘルス・フィン・エド・クライメート・ロジスティクス）にわたって{base_ja}の適用パターンを比較分析した大規模研究。",
        "impact_tmpl": "産業横断的なスタートアップ知識移転と方法論的最適化に貢献した",
        "era_offset": 5
    },
]

STAGES = ["idea", "pre-seed", "seed", "early", "growth", "late"]
GEO_LIST = ["USA", "Europe", "Asia", "Global", "Silicon Valley", "Israel", "UK", "Germany", "Japan", "Southeast Asia"]
INDUSTRY_LIST = ["technology", "SaaS", "B2B", "B2C", "marketplace", "fintech", "healthtech", "edtech", "consumer", "deep tech"]

def generate_entries():
    entries = []
    topics_count = len(TOPICS)
    var_count = len(VARIATION_TEMPLATES)

    idx = 0
    while len(entries) < 714:
        topic = TOPICS[idx % topics_count]
        var = VARIATION_TEMPLATES[(idx // topics_count) % var_count]

        entry_num = len(entries) + 1
        entry_id = f"su_scale_{entry_num:03d}"

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
            "scaling_growth_strategy",
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

    cur.execute("SELECT COUNT(*) FROM startup_theory WHERE subfield='scaling_growth_strategy'")
    count = cur.fetchone()[0]
    print(f"Total scaling_growth_strategy rows: {count}")
    conn.close()

if __name__ == "__main__":
    main()
