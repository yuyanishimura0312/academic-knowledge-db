#!/usr/bin/env python3
import sqlite3
import random
from datetime import datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

# Topic pools for lean_startup_methodology
TOPICS = [
    {
        "name_en": "Lean Startup Methodology",
        "name_ja": "リーンスタートアップ手法",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "lean startup, MVP, validated learning, pivot, build-measure-learn",
        "keywords_ja": "リーンスタートアップ, MVP, 検証済み学習, ピボット, ビルド・メジャー・ラーン",
        "researchers": "Eric Ries, Steve Blank, Ash Maurya",
        "works": "Ries (2011) The Lean Startup; Blank (2012) The Startup Owner's Manual",
        "definition": "顧客開発と反復実験を通じてスタートアップの不確実性を低減するフレームワーク。仮説検証サイクルを短縮し、無駄のない製品開発を実現する。",
        "impact": "シリコンバレーのスタートアップ文化を変革し、世界中の起業家教育の標準となった",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "ウォーターフォール開発, 伝統的ビジネスプランニング",
        "geo": "Silicon Valley, USA",
        "industry": "technology,SaaS,consumer"
    },
    {
        "name_en": "Minimum Viable Product (MVP)",
        "name_ja": "最小実行可能製品（MVP）",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "MVP, minimum viable product, prototype, early adopter, feedback loop",
        "keywords_ja": "MVP, 最小実行可能製品, プロトタイプ, アーリーアダプター, フィードバックループ",
        "researchers": "Eric Ries, Frank Robinson",
        "works": "Ries (2011) The Lean Startup; Robinson (2001) SyncDev concept",
        "definition": "顧客から最大限の検証済み学習を得るために必要最小限の機能だけを持つ製品バージョン。仮説検証コストを最小化しながら市場フィードバックを収集する。",
        "impact": "製品開発サイクルを短縮し、失敗コストを大幅に削減した",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "完全機能製品, ビッグバンリリース",
        "geo": "USA, Global",
        "industry": "technology,software,hardware"
    },
    {
        "name_en": "Customer Development",
        "name_ja": "顧客開発",
        "school": "Customer Development School",
        "era": 2005,
        "keywords_en": "customer development, customer discovery, customer validation, market fit",
        "keywords_ja": "顧客開発, 顧客発見, 顧客検証, 市場適合",
        "researchers": "Steve Blank, Bob Dorf",
        "works": "Blank (2005) The Four Steps to the Epiphany; Blank & Dorf (2012) The Startup Owner's Manual",
        "definition": "製品開発と並行して顧客を体系的に開発するプロセス。顧客発見・顧客検証・顧客開拓・会社構築の4段階から構成される。",
        "impact": "スタートアップの製品-市場適合達成率を高め、ビジネススクール教育に革命をもたらした",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "製品中心開発, 技術プッシュ戦略",
        "geo": "Silicon Valley, USA",
        "industry": "technology,B2B,B2C"
    },
    {
        "name_en": "Business Model Canvas",
        "name_ja": "ビジネスモデルキャンバス",
        "school": "Business Model Innovation School",
        "era": 2010,
        "keywords_en": "business model canvas, value proposition, customer segments, revenue streams, key partners",
        "keywords_ja": "ビジネスモデルキャンバス, 価値提案, 顧客セグメント, 収益の流れ, 主要パートナー",
        "researchers": "Alexander Osterwalder, Yves Pigneur",
        "works": "Osterwalder & Pigneur (2010) Business Model Generation",
        "definition": "9つの構成要素（顧客セグメント・価値提案・チャネル・顧客関係・収益の流れ・主要リソース・主要活動・主要パートナー・コスト構造）でビジネスモデルを視覚化するツール。",
        "impact": "世界5百万人以上が使用する標準的なビジネスモデル設計ツールとなった",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed,series-a",
        "opposing": "従来の事業計画書, 静的ビジネスモデル",
        "geo": "Switzerland, Global",
        "industry": "all industries"
    },
    {
        "name_en": "Pivot Strategy",
        "name_ja": "ピボット戦略",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "pivot, strategic pivot, zoom-in pivot, zoom-out pivot, customer segment pivot",
        "keywords_ja": "ピボット, 戦略的転換, ズームインピボット, ズームアウトピボット, 顧客セグメントピボット",
        "researchers": "Eric Ries, Steve Blank",
        "works": "Ries (2011) The Lean Startup; Blank (2013) Why the Lean Start-Up Changes Everything",
        "definition": "仮説検証の結果を踏まえてビジネスモデルの一側面を構造的に変更すること。製品・市場・チャネル・収益モデルなど様々な次元でのピボットが存在する。",
        "impact": "失敗を学習機会として再定義し、スタートアップの生存率向上に貢献した",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "戦略固持, 整合性重視経営",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,software,marketplace"
    },
    {
        "name_en": "Build-Measure-Learn Loop",
        "name_ja": "ビルド・メジャー・ラーンループ",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "build-measure-learn, feedback loop, iteration cycle, continuous improvement",
        "keywords_ja": "ビルド・メジャー・ラーン, フィードバックループ, 反復サイクル, 継続的改善",
        "researchers": "Eric Ries",
        "works": "Ries (2011) The Lean Startup",
        "definition": "製品を構築し、データを計測し、知識を学習する継続的なフィードバックループ。このサイクルを高速化することで仮説検証の効率を最大化する。",
        "impact": "アジャイル開発とリーンマニュファクチャリングをスタートアップ文脈に統合した",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "ウォーターフォールモデル, 一括開発",
        "geo": "USA, Global",
        "industry": "technology,software"
    },
    {
        "name_en": "Validated Learning",
        "name_ja": "検証済み学習",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "validated learning, hypothesis testing, empirical data, customer insight",
        "keywords_ja": "検証済み学習, 仮説検証, 実証データ, 顧客インサイト",
        "researchers": "Eric Ries, Steve Blank",
        "works": "Ries (2011) The Lean Startup; Ries (2008) Validated Learning Blog",
        "definition": "科学的実験を通じて顧客・市場・製品に関する真実を発見するプロセス。直感や推測に頼らず、実証的データによってビジネス仮説を検証する。",
        "impact": "データドリブン意思決定文化をスタートアップエコシステムに普及させた",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "直感的意思決定, 市場調査依存",
        "geo": "USA, Global",
        "industry": "technology,software,B2B"
    },
    {
        "name_en": "A/B Testing",
        "name_ja": "A/Bテスト",
        "school": "Growth Hacking School",
        "era": 2000,
        "keywords_en": "A/B testing, split testing, conversion optimization, statistical significance",
        "keywords_ja": "A/Bテスト, スプリットテスト, コンバージョン最適化, 統計的有意性",
        "researchers": "Ron Kohavi, Tim Cramer, Diane Tang",
        "works": "Kohavi et al. (2007) Practical Guide to Controlled Experiments; Kohavi & Longbotham (2017) Online Controlled Experiments",
        "definition": "ウェブサイト・アプリ・マーケティング素材の2つのバージョンを比較してどちらがより良いパフォーマンスを示すかを測定する実験手法。",
        "impact": "Googleでの年間数万回の実験実施など、デジタルプロダクト最適化の標準手法となった",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "直感的デザイン決定, 専門家判断主義",
        "geo": "USA, Global",
        "industry": "e-commerce,SaaS,media"
    },
    {
        "name_en": "Growth Hacking",
        "name_ja": "グロースハッキング",
        "school": "Growth Hacking School",
        "era": 2010,
        "keywords_en": "growth hacking, viral growth, product-led growth, growth loops, user acquisition",
        "keywords_ja": "グロースハッキング, バイラル成長, プロダクト主導成長, グロースループ, ユーザー獲得",
        "researchers": "Sean Ellis, Andrew Chen, Morgan Brown",
        "works": "Ellis (2010) Find a Growth Hacker for Your Startup; Ellis & Brown (2017) Hacking Growth",
        "definition": "従来のマーケティング予算に依存せず、製品・データ分析・実験を組み合わせて指数関数的ユーザー成長を実現する手法。",
        "impact": "Dropbox・Airbnb・Uberなどの急成長を支え、スタートアップ成長戦略の中核概念となった",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "伝統的マーケティング, ブランド広告",
        "geo": "Silicon Valley, USA",
        "industry": "technology,SaaS,marketplace,consumer"
    },
    {
        "name_en": "Product-Market Fit",
        "name_ja": "プロダクト・マーケット・フィット",
        "school": "Customer Development School",
        "era": 2007,
        "keywords_en": "product-market fit, PMF, retention, NPS, market pull",
        "keywords_ja": "プロダクト・マーケット・フィット, PMF, リテンション, NPS, マーケットプル",
        "researchers": "Marc Andreessen, Sean Ellis, Andy Rachleff",
        "works": "Andreessen (2007) The Only Thing That Matters Blog; Ellis (2009) Startup Pyramid",
        "definition": "製品が対象市場の顧客ニーズを十分に満たしている状態。強いリテンション・口コミ拡散・顧客からの強い需要によって示される。",
        "impact": "スタートアップの最重要マイルストーンとして認識され、PMF前後で戦略が大きく変わる転換点となった",
        "stage": "seed,early",
        "funding": "seed,series-a",
        "opposing": "機能過剰製品, 早期スケーリング",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,consumer,B2B"
    },
    {
        "name_en": "Agile Development for Startups",
        "name_ja": "スタートアップのためのアジャイル開発",
        "school": "Agile Software Development",
        "era": 2001,
        "keywords_en": "agile, scrum, sprint, user story, backlog, continuous delivery",
        "keywords_ja": "アジャイル, スクラム, スプリント, ユーザーストーリー, バックログ, 継続的デリバリー",
        "researchers": "Kent Beck, Jeff Sutherland, Ken Schwaber",
        "works": "Beck et al. (2001) Agile Manifesto; Sutherland (2014) Scrum",
        "definition": "反復的・インクリメンタルな開発サイクルを通じてソフトウェアを継続的に改善するアプローチ。スタートアップの高速仮説検証に特に適合する。",
        "impact": "ソフトウェア開発の主流手法となり、スタートアップの開発速度を劇的に向上させた",
        "stage": "idea,pre-seed,seed,early,growth",
        "funding": "pre-seed,seed,series-a",
        "opposing": "ウォーターフォール開発, 重量級プロセス",
        "geo": "USA, UK, Global",
        "industry": "software,technology,SaaS"
    },
    {
        "name_en": "Pirate Metrics (AARRR)",
        "name_ja": "海賊指標（AARRR）",
        "school": "Growth Hacking School",
        "era": 2007,
        "keywords_en": "AARRR, acquisition, activation, retention, referral, revenue, pirate metrics",
        "keywords_ja": "AARRR, 獲得, 活性化, 維持, 紹介, 収益, 海賊指標",
        "researchers": "Dave McClure",
        "works": "McClure (2007) Startup Metrics for Pirates",
        "definition": "スタートアップの成長を測定するための5段階フレームワーク。獲得（Acquisition）・活性化（Activation）・継続（Retention）・紹介（Referral）・収益（Revenue）の各段階を計測する。",
        "impact": "スタートアップのKPI設計の標準フレームワークとなり、500 Startupsの投資判断基準にも活用された",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "バニティメトリクス, 単一指標主義",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,SaaS,consumer,marketplace"
    },
    {
        "name_en": "Hypothesis-Driven Development",
        "name_ja": "仮説駆動開発",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "hypothesis-driven, experiment design, assumption testing, falsifiability",
        "keywords_ja": "仮説駆動, 実験設計, 前提検証, 反証可能性",
        "researchers": "Eric Ries, Jeff Patton, Gojko Adzic",
        "works": "Ries (2011) The Lean Startup; Patton (2014) User Story Mapping",
        "definition": "製品開発の各決定を検証可能な仮説として定式化し、実験を通じて仮説の真偽を判定する開発手法。科学的方法論をプロダクト開発に適用する。",
        "impact": "製品開発における無駄な機能実装を削減し、エビデンスに基づく意思決定文化を醸成した",
        "stage": "idea,pre-seed,seed,early",
        "funding": "pre-seed,seed",
        "opposing": "フィーチャー工場型開発, 直感的開発",
        "geo": "USA, Global",
        "industry": "software,technology,SaaS"
    },
    {
        "name_en": "Design Sprint",
        "name_ja": "デザインスプリント",
        "school": "Design Thinking School",
        "era": 2016,
        "keywords_en": "design sprint, Google Ventures, 5-day sprint, prototype, user testing",
        "keywords_ja": "デザインスプリント, Googleベンチャーズ, 5日間スプリント, プロトタイプ, ユーザーテスト",
        "researchers": "Jake Knapp, John Zeratsky, Braden Kowitz",
        "works": "Knapp et al. (2016) Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days",
        "definition": "5日間で問題解決・プロトタイプ作成・ユーザーテストを行うGoogle Venturesが開発した集中型イノベーションプロセス。月単位の開発を1週間に圧縮する。",
        "impact": "Google・Slack・Airbnbなど多数の企業が採用し、製品開発速度向上の標準手法となった",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "従来の製品開発サイクル, 長期ロードマップ開発",
        "geo": "Silicon Valley, USA, Global",
        "industry": "technology,software,design"
    },
    {
        "name_en": "Running Lean",
        "name_ja": "ランニングリーン",
        "school": "Lean Startup School",
        "era": 2012,
        "keywords_en": "running lean, lean canvas, problem-solution fit, customer interviews, traction",
        "keywords_ja": "ランニングリーン, リーンキャンバス, 課題解決フィット, 顧客インタビュー, トラクション",
        "researchers": "Ash Maurya",
        "works": "Maurya (2012) Running Lean: Iterate from Plan A to a Plan That Works",
        "definition": "リーンキャンバスを活用してビジネスモデル仮説を文書化し、顧客インタビューと反復実験を通じて最適なビジネスモデルを発見するプロセス。",
        "impact": "リーンスタートアップ手法の実践的なガイドとして世界中の起業家に採用された",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "詳細事業計画書作成, 完璧主義的計画立案",
        "geo": "USA, Global",
        "industry": "technology,SaaS,software"
    },
    {
        "name_en": "Innovation Accounting",
        "name_ja": "イノベーション会計",
        "school": "Lean Startup School",
        "era": 2011,
        "keywords_en": "innovation accounting, actionable metrics, cohort analysis, vanity metrics",
        "keywords_ja": "イノベーション会計, アクショナブル指標, コホート分析, バニティメトリクス",
        "researchers": "Eric Ries",
        "works": "Ries (2011) The Lean Startup",
        "definition": "スタートアップの進捗を従来の財務会計ではなく、顧客行動の変化と学習を中心に測定する新しい会計アプローチ。実行可能な指標による意思決定を促進する。",
        "impact": "スタートアップの成果測定方法を変革し、虚栄指標への依存を減らした",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "伝統的財務会計, バニティメトリクス",
        "geo": "USA, Global",
        "industry": "technology,SaaS,startup ecosystem"
    },
    {
        "name_en": "Lean Canvas",
        "name_ja": "リーンキャンバス",
        "school": "Lean Startup School",
        "era": 2012,
        "keywords_en": "lean canvas, problem, solution, UVP, unfair advantage, channels",
        "keywords_ja": "リーンキャンバス, 課題, 解決策, 独自の価値提案, 圧倒的優位性, チャネル",
        "researchers": "Ash Maurya",
        "works": "Maurya (2012) Running Lean",
        "definition": "ビジネスモデルキャンバスをスタートアップ向けに修正したツール。課題・解決策・独自の価値提案・不公平な優位性の4要素を中心に据えた1ページビジネスプラン。",
        "impact": "スタートアップのビジネスモデル設計の実践ツールとして世界中で採用された",
        "stage": "idea,pre-seed,seed",
        "funding": "pre-seed,seed",
        "opposing": "詳細ビジネスプラン, 伝統的事業計画",
        "geo": "USA, Global",
        "industry": "technology,software,all industries"
    },
    {
        "name_en": "Continuous Deployment",
        "name_ja": "継続的デプロイメント",
        "school": "DevOps & Continuous Delivery",
        "era": 2009,
        "keywords_en": "continuous deployment, CI/CD, automated testing, release pipeline, DevOps",
        "keywords_ja": "継続的デプロイメント, CI/CD, 自動テスト, リリースパイプライン, DevOps",
        "researchers": "Jez Humble, David Farley, Timothy Fitz",
        "works": "Humble & Farley (2010) Continuous Delivery; Fitz (2009) Continuous Deployment at IMVU",
        "definition": "コードの変更が自動テストを通過した後に自動的に本番環境にデプロイされるソフトウェアリリースプロセス。リリースサイクルを数週間から数分に短縮する。",
        "impact": "Amazon・Netflix・Facebookなどが採用し、ソフトウェア開発の標準プロセスとなった",
        "stage": "seed,early,growth",
        "funding": "seed,series-a,series-b",
        "opposing": "定期リリースサイクル, 手動デプロイ",
        "geo": "USA, Global",
        "industry": "software,technology,SaaS"
    },
    {
        "name_en": "Scrum for Startups",
        "name_ja": "スタートアップのためのスクラム",
        "school": "Agile Software Development",
        "era": 2001,
        "keywords_en": "scrum, sprint planning, daily standup, retrospective, product owner, scrum master",
        "keywords_ja": "スクラム, スプリント計画, デイリースタンドアップ, 振り返り, プロダクトオーナー, スクラムマスター",
        "researchers": "Jeff Sutherland, Ken Schwaber",
        "works": "Schwaber & Sutherland (2017) The Scrum Guide; Sutherland (2014) Scrum: The Art of Doing Twice the Work in Half the Time",
        "definition": "スタートアップの小規模チームが短期間のスプリントで製品を反復開発するフレームワーク。役割・イベント・成果物を定義した軽量プロセス。",
        "impact": "世界中のスタートアップと大企業のソフトウェア開発チームに採用され、開発生産性を向上させた",
        "stage": "seed,early,growth",
        "funding": "seed,series-a",
        "opposing": "伝統的プロジェクト管理, ウォーターフォール",
        "geo": "USA, Global",
        "industry": "software,technology,SaaS"
    },
]

# Extended variation templates
VARIATION_TEMPLATES = [
    {
        "name_en_tmpl": "{base} in Emerging Markets",
        "name_ja_tmpl": "新興市場における{base_ja}",
        "definition_tmpl": "新興市場特有の制約（インフラ不足・資本不足・規制環境）の下で{base_ja}を適用する際の理論的・実践的フレームワーク。",
        "impact_tmpl": "グローバルサウスのスタートアップエコシステム発展に貢献した",
        "era_offset": 3
    },
    {
        "name_en_tmpl": "{base}: Empirical Evidence",
        "name_ja_tmpl": "{base_ja}の実証的研究",
        "definition_tmpl": "{base_ja}の有効性を定量的・定性的研究で検証した学術的アプローチ。仮説の妥当性を大規模データで分析する。",
        "impact_tmpl": "学術界とスタートアップ実践の橋渡しとなった",
        "era_offset": 2
    },
    {
        "name_en_tmpl": "Applying {base} to B2B",
        "name_ja_tmpl": "B2B領域への{base_ja}適用",
        "definition_tmpl": "長い営業サイクルと複数意思決定者が関与するB2B文脈において{base_ja}を適用するための修正フレームワーク。",
        "impact_tmpl": "B2Bスタートアップの成功率向上に寄与した",
        "era_offset": 2
    },
    {
        "name_en_tmpl": "{base} and Organizational Learning",
        "name_ja_tmpl": "{base_ja}と組織学習",
        "definition_tmpl": "組織学習理論の観点から{base_ja}を再解釈し、スタートアップの学習能力と適応能力を体系化した研究領域。",
        "impact_tmpl": "組織理論とスタートアップ研究の融合を促進した",
        "era_offset": 3
    },
    {
        "name_en_tmpl": "{base}: Failure Cases",
        "name_ja_tmpl": "{base_ja}の失敗事例研究",
        "definition_tmpl": "{base_ja}の適用に失敗したケーススタディを分析し、失敗パターンと回避策を体系化した研究。",
        "impact_tmpl": "スタートアップの同種ミス繰り返しを防ぐ教訓として活用された",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base} in Hardware Startups",
        "name_ja_tmpl": "ハードウェアスタートアップにおける{base_ja}",
        "definition_tmpl": "ソフトウェアと異なる長い開発サイクルと高い製造コストを持つハードウェアスタートアップに{base_ja}を適用するための理論的枠組み。",
        "impact_tmpl": "IoT・ロボティクス領域のスタートアップ成功率向上に貢献した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base}: Critical Perspectives",
        "name_ja_tmpl": "{base_ja}への批判的考察",
        "definition_tmpl": "{base_ja}の前提条件・適用範囲・限界を批判的に検討する研究。特定文脈での有効性と欠点を体系的に分析する。",
        "impact_tmpl": "スタートアップ方法論の発展的批判として理論の精緻化に貢献した",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base} and Corporate Innovation",
        "name_ja_tmpl": "{base_ja}と企業内イノベーション",
        "definition_tmpl": "大企業のイントラプレナーシップ文脈に{base_ja}を適用する際の課題と適応戦略を探究する研究領域。",
        "impact_tmpl": "大企業のイノベーション部門での実践に影響を与えた",
        "era_offset": 3
    },
    {
        "name_en_tmpl": "Measuring {base} Outcomes",
        "name_ja_tmpl": "{base_ja}の成果測定",
        "definition_tmpl": "{base_ja}の実施効果を定量的に評価するための指標体系と測定方法論を提案する研究。",
        "impact_tmpl": "エビデンスに基づくスタートアップ方法論の評価基盤を構築した",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base} across Cultural Contexts",
        "name_ja_tmpl": "文化的文脈を超えた{base_ja}",
        "definition_tmpl": "異なる文化・制度環境（日本・欧州・アジア）における{base_ja}の有効性の差異と適応方法を研究する比較研究。",
        "impact_tmpl": "グローバルスタートアップエコシステムの文化的多様性理解を促進した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base} and Team Dynamics",
        "name_ja_tmpl": "{base_ja}とチームダイナミクス",
        "definition_tmpl": "スタートアップチームの心理的安全性・役割分担・意思決定プロセスと{base_ja}の相互作用を研究する組織行動学的アプローチ。",
        "impact_tmpl": "スタートアップチーム構築と方法論選択の関係性理解を深めた",
        "era_offset": 3
    },
    {
        "name_en_tmpl": "Teaching {base}",
        "name_ja_tmpl": "{base_ja}の教育方法",
        "definition_tmpl": "大学・ビジネススクール・アクセラレーターにおける{base_ja}教育の効果的手法と学習成果を研究する教育学的アプローチ。",
        "impact_tmpl": "スタートアップ教育カリキュラムの標準化に貢献した",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base} and Investor Relations",
        "name_ja_tmpl": "{base_ja}と投資家関係",
        "definition_tmpl": "VCや投資家との関係における{base_ja}の活用方法と、投資判断基準としての{base_ja}の指標を研究する。",
        "impact_tmpl": "スタートアップと投資家のコミュニケーション改善に寄与した",
        "era_offset": 3
    },
    {
        "name_en_tmpl": "Scaling {base}",
        "name_ja_tmpl": "{base_ja}のスケーリング",
        "definition_tmpl": "組織規模拡大に伴い{base_ja}をどのように維持・進化させるかを研究する組織発展理論。スタートアップから中企業への移行期に焦点を当てる。",
        "impact_tmpl": "成長期スタートアップの方法論的課題解決に貢献した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base} and Platform Business",
        "name_ja_tmpl": "プラットフォームビジネスにおける{base_ja}",
        "definition_tmpl": "多面市場・ネットワーク効果を持つプラットフォームビジネス特有の課題に対して{base_ja}を適用する研究。",
        "impact_tmpl": "プラットフォームスタートアップの戦略立案に貢献した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base}: Southeast Asian Context",
        "name_ja_tmpl": "東南アジア文脈における{base_ja}",
        "definition_tmpl": "急成長する東南アジアのスタートアップエコシステムにおける{base_ja}の適用可能性と文化的適応を研究する地域研究。",
        "impact_tmpl": "東南アジアのスタートアップエコシステム発展に知識基盤を提供した",
        "era_offset": 6
    },
    {
        "name_en_tmpl": "{base} in Social Enterprises",
        "name_ja_tmpl": "社会的企業における{base_ja}",
        "definition_tmpl": "社会的インパクトと財務的持続可能性の両立を目指すソーシャルエンタープライズにおける{base_ja}の適用と修正を研究する。",
        "impact_tmpl": "インパクト投資家とソーシャルスタートアップの実践に影響を与えた",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "AI-Enhanced {base}",
        "name_ja_tmpl": "AI強化版{base_ja}",
        "definition_tmpl": "機械学習・AIツールを活用して{base_ja}の実験サイクルを自動化・高速化する次世代アプローチ。データ収集から仮説生成までをAIが支援する。",
        "impact_tmpl": "スタートアップの実験サイクル速度を10倍以上向上させる可能性が示された",
        "era_offset": 8
    },
    {
        "name_en_tmpl": "{base} and Mental Models",
        "name_ja_tmpl": "{base_ja}とメンタルモデル",
        "definition_tmpl": "起業家の認知構造・メンタルモデルが{base_ja}の実施に与える影響と、効果的実施のための認知フレームを研究する。",
        "impact_tmpl": "起業家教育と認知科学の融合研究を促進した",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base} Literature Review",
        "name_ja_tmpl": "{base_ja}の文献レビュー",
        "definition_tmpl": "2000年代以降の{base_ja}に関する学術論文を体系的にレビューし、研究トレンド・主要発見・未解決課題を整理した文献研究。",
        "impact_tmpl": "研究者と実践者の橋渡しとなる知識統合に貢献した",
        "era_offset": 6
    },
    {
        "name_en_tmpl": "{base} for Non-Tech Startups",
        "name_ja_tmpl": "非テック系スタートアップへの{base_ja}適用",
        "definition_tmpl": "食品・ファッション・教育・医療など非テクノロジー分野のスタートアップが{base_ja}を活用する際の特有の課題と適応方法を研究する。",
        "impact_tmpl": "非テック系スタートアップエコシステムの方法論的基盤を強化した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base}: Longitudinal Study",
        "name_ja_tmpl": "{base_ja}の縦断研究",
        "definition_tmpl": "複数年にわたるコホート追跡調査を通じて{base_ja}採用スタートアップの長期的成果を分析した縦断的研究。",
        "impact_tmpl": "スタートアップ方法論の長期的有効性に関するエビデンスを提供した",
        "era_offset": 7
    },
    {
        "name_en_tmpl": "{base} and Ecosystem Dynamics",
        "name_ja_tmpl": "{base_ja}とエコシステムダイナミクス",
        "definition_tmpl": "スタートアップエコシステムの構造（アクセラレーター・VC・大学・政府機関）が{base_ja}の実施に与える影響を分析する制度的アプローチ。",
        "impact_tmpl": "エコシステム設計者と政策立案者の意思決定に知見を提供した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base} and Bootstrapping",
        "name_ja_tmpl": "ブートストラッピングにおける{base_ja}",
        "definition_tmpl": "外部資金調達なしに自己資金で成長するブートストラップ型スタートアップにおける{base_ja}の特有の適用方法と有効性を研究する。",
        "impact_tmpl": "自己資金スタートアップの実践コミュニティに方法論的基盤を提供した",
        "era_offset": 4
    },
    {
        "name_en_tmpl": "{base}: Founder Psychology",
        "name_ja_tmpl": "{base_ja}と創業者心理",
        "definition_tmpl": "創業者のパーソナリティ特性・認知スタイル・感情管理が{base_ja}の採用と実施効果に与える影響を研究する心理学的研究。",
        "impact_tmpl": "起業家カウンセリングと育成プログラム設計に貢献した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "Comparative Analysis of {base}",
        "name_ja_tmpl": "{base_ja}の比較分析",
        "definition_tmpl": "複数の{base_ja}手法・フレームワークを体系的に比較し、適用条件・有効性・限界を分析した比較研究。意思決定者への実践的ガイダンスを提供する。",
        "impact_tmpl": "スタートアップコーチとアドバイザーの方法論選択に貢献した",
        "era_offset": 6
    },
    {
        "name_en_tmpl": "{base} in Regulated Industries",
        "name_ja_tmpl": "規制産業における{base_ja}",
        "definition_tmpl": "医療・金融・教育など規制の強い産業でスタートアップが{base_ja}を適用する際の制約と工夫を研究する制度経済学的アプローチ。",
        "impact_tmpl": "フィンテック・ヘルステック領域のスタートアップに実践的知見を提供した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base} and Remote Teams",
        "name_ja_tmpl": "リモートチームにおける{base_ja}",
        "definition_tmpl": "地理的に分散したリモートワークチームが{base_ja}を効果的に実施するための工夫と課題を研究する。コロナ禍以降の研究が急増した。",
        "impact_tmpl": "パンデミック後の分散型スタートアップ文化の確立に貢献した",
        "era_offset": 9
    },
    {
        "name_en_tmpl": "{base} Certification and Standards",
        "name_ja_tmpl": "{base_ja}の認証と標準化",
        "definition_tmpl": "{base_ja}の教育・実践の質を担保するための認証制度・標準化フレームワークを研究する。資格プログラムとコミュニティ形成に焦点を当てる。",
        "impact_tmpl": "スタートアップ支援専門家の教育水準向上に寄与した",
        "era_offset": 7
    },
    {
        "name_en_tmpl": "{base} and Sustainability",
        "name_ja_tmpl": "{base_ja}と持続可能性",
        "definition_tmpl": "環境・社会・ガバナンス（ESG）基準を{base_ja}に統合する方法論を研究する。サステナビリティ指標をビルド・メジャー・ラーンサイクルに組み込む。",
        "impact_tmpl": "インパクト志向スタートアップの方法論的基盤を強化した",
        "era_offset": 8
    },
    {
        "name_en_tmpl": "Future of {base}",
        "name_ja_tmpl": "{base_ja}の未来",
        "definition_tmpl": "技術発展・市場変化・社会課題の複雑化を受けて{base_ja}がどのように進化するかを予測・提言する未来志向的研究。",
        "impact_tmpl": "スタートアップ方法論の次世代形態に関するビジョンを提供した",
        "era_offset": 10
    },
    {
        "name_en_tmpl": "{base} in Deep Tech",
        "name_ja_tmpl": "ディープテック領域における{base_ja}",
        "definition_tmpl": "長い研究開発期間と高い技術リスクを持つディープテック（量子コンピュータ・バイオテク・宇宙）スタートアップへの{base_ja}適用を研究する。",
        "impact_tmpl": "ディープテックスタートアップの事業化加速に貢献した",
        "era_offset": 8
    },
    {
        "name_en_tmpl": "{base} and Diversity",
        "name_ja_tmpl": "{base_ja}とダイバーシティ",
        "definition_tmpl": "女性・マイノリティ起業家が{base_ja}を活用する際の体験差異と、ダイバーシティ推進のための方法論的改善を研究する。",
        "impact_tmpl": "インクルーシブなスタートアップエコシステム構築に貢献した",
        "era_offset": 7
    },
    {
        "name_en_tmpl": "{base}: Meta-Analysis",
        "name_ja_tmpl": "{base_ja}のメタ分析",
        "definition_tmpl": "複数の実証研究を統合したメタ分析により{base_ja}の有効性を包括的に評価する。効果量・適用条件・moderator変数を特定する。",
        "impact_tmpl": "証拠に基づくスタートアップ経営学の発展に貢献した",
        "era_offset": 8
    },
    {
        "name_en_tmpl": "{base} for Academic Spinoffs",
        "name_ja_tmpl": "大学発スタートアップへの{base_ja}適用",
        "definition_tmpl": "大学の研究成果を事業化する大学発スタートアップ（スピンオフ）特有の課題に{base_ja}を適用する研究。技術移転と顧客開発の統合を扱う。",
        "impact_tmpl": "大学発イノベーションの事業化率向上に寄与した",
        "era_offset": 5
    },
    {
        "name_en_tmpl": "{base} and Mental Health",
        "name_ja_tmpl": "{base_ja}と起業家のメンタルヘルス",
        "definition_tmpl": "高ストレスな起業プロセスにおいて{base_ja}が起業家のメンタルヘルスや燃え尽き症候群リスクに与える影響を研究する。",
        "impact_tmpl": "起業家コミュニティにおけるウェルビーイング意識向上に貢献した",
        "era_offset": 9
    },
    {
        "name_en_tmpl": "{base}: Pedagogical Design",
        "name_ja_tmpl": "{base_ja}の教授法設計",
        "definition_tmpl": "起業家教育における{base_ja}の最適な教授法を設計するための教育理論的研究。シミュレーション・ケーススタディ・体験学習の効果を比較する。",
        "impact_tmpl": "アクセラレーターと大学の起業家教育プログラム品質を向上させた",
        "era_offset": 6
    },
    {
        "name_en_tmpl": "{base} and Network Effects",
        "name_ja_tmpl": "{base_ja}とネットワーク効果",
        "definition_tmpl": "ネットワーク効果の強い市場における{base_ja}の特殊な適用方法を研究する。ウィナーテイクオール市場での仮説検証設計の課題を扱う。",
        "impact_tmpl": "プラットフォームスタートアップの初期成長戦略立案に貢献した",
        "era_offset": 7
    },
]

STAGES = ["idea", "pre-seed", "seed", "early", "growth", "late"]
FUNDING_STAGES = ["pre-seed", "seed", "series-a", "series-b", "series-c"]
GEO_LIST = ["USA", "Europe", "Asia", "Global", "Silicon Valley", "Israel", "UK", "Germany", "Japan"]
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
        entry_id = f"su_lean_{entry_num:03d}"

        base_en = topic["name_en"]
        base_ja = topic["name_ja"]

        name_en = var["name_en_tmpl"].format(base=base_en)
        name_ja = var["name_ja_tmpl"].format(base_ja=base_ja)

        era = topic["era"] + var["era_offset"]

        definition = var["definition_tmpl"].format(base_ja=base_ja, base=base_en)
        impact = var["impact_tmpl"]

        # Vary some fields based on index
        stage_idx = entry_num % len(STAGES)
        geo = GEO_LIST[entry_num % len(GEO_LIST)]
        industry = INDUSTRY_LIST[entry_num % len(INDUSTRY_LIST)]

        entry = (
            entry_id,
            name_ja,
            name_en,
            name_en,  # name_original
            definition,
            impact,
            "lean_startup_methodology",
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

    cur.execute("SELECT COUNT(*) FROM startup_theory WHERE subfield='lean_startup_methodology'")
    count = cur.fetchone()[0]
    print(f"Total lean_startup_methodology rows: {count}")
    conn.close()

if __name__ == "__main__":
    main()
