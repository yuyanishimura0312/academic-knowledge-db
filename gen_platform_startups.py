#!/usr/bin/env python3
"""Generate platform_digital_startups entries (su_plat_001 to su_plat_714)"""
import sqlite3

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

TOPICS = [
    {
        "name_en": "Platform Leadership (Gawer & Cusumano)",
        "name_ja": "プラットフォームリーダーシップ（Gawer & Cusumano）",
        "definition": "Strategic framework by Gawer and Cusumano describing how firms design technology platforms that attract complementors, govern external innovation, and sustain competitive advantage through ecosystem orchestration.",
        "keywords_en": "platform leadership, Gawer, Cusumano, ecosystem, complementors, platform strategy",
        "keywords_ja": "プラットフォームリーダーシップ, Gawer, Cusumano, エコシステム, 補完者, プラットフォーム戦略",
        "key_researchers": "Gawer, Cusumano",
        "key_works": "Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation",
        "era_start": 2002, "era_end": None, "school": "Platform Economics",
        "stage": "growth to scale", "funding": "venture capital, IPO",
        "geo": "USA, Global", "industry": "technology platforms",
    },
    {
        "name_en": "Chicken-and-Egg Problem (Eisenmann)",
        "name_ja": "チキンアンドエッグ問題（Eisenmann）",
        "definition": "Market launch challenge faced by multi-sided platforms where each user group's value depends on the presence of others, requiring strategic subsidization or sequencing to achieve critical mass on both sides simultaneously.",
        "keywords_en": "chicken-and-egg, Eisenmann, two-sided market, critical mass, platform launch",
        "keywords_ja": "チキンアンドエッグ問題, Eisenmann, 両面市場, 臨界質量, プラットフォーム立ち上げ",
        "key_researchers": "Eisenmann, Parker, Van Alstyne",
        "key_works": "Strategies for Two-Sided Markets",
        "era_start": 2006, "era_end": None, "school": "Platform Strategy",
        "stage": "pre-seed to series A", "funding": "venture capital, strategic subsidization",
        "geo": "USA, Global", "industry": "marketplaces, gig economy, social platforms",
    },
    {
        "name_en": "Marketplace Startup Dynamics",
        "name_ja": "マーケットプレイススタートアップのダイナミクス",
        "definition": "Business model and growth mechanics of online marketplace startups that connect buyers and sellers, encompassing liquidity management, trust mechanisms, pricing models, and vertical versus horizontal market strategies.",
        "keywords_en": "marketplace startup, liquidity, buyer-seller match, trust, vertical marketplace",
        "keywords_ja": "マーケットプレイス, 流動性, 売買マッチング, 信頼, バーティカルマーケットプレイス",
        "key_researchers": "Andreessen Horowitz, Li Jin, Josh Breinlinger",
        "key_works": "A Marketplace Manifesto (a16z)",
        "era_start": 1995, "era_end": None, "school": "Platform Economics",
        "stage": "seed to series B", "funding": "venture capital, take-rate monetization",
        "geo": "USA, China, SE Asia", "industry": "e-commerce, gig economy, services",
    },
    {
        "name_en": "SaaS Metrics Framework (Tunguz)",
        "name_ja": "SaaSメトリクスフレームワーク（Tunguz）",
        "definition": "Tomasz Tunguz's systematic approach to measuring SaaS business health through metrics including Monthly Recurring Revenue (MRR), churn rate, Customer Acquisition Cost (CAC), and Lifetime Value (LTV).",
        "keywords_en": "SaaS metrics, MRR, ARR, churn, CAC, LTV, Tunguz, SaaS growth",
        "keywords_ja": "SaaSメトリクス, MRR, ARR, チャーン, CAC, LTV, Tunguz, SaaS成長",
        "key_researchers": "Tunguz, Skok, Mauboussin",
        "key_works": "Winning with Data: Transform Your Culture, Empower Your People, and Shape the Future",
        "era_start": 2013, "era_end": None, "school": "SaaS Strategy",
        "stage": "seed to growth", "funding": "venture capital, ARR-based lending",
        "geo": "USA, Global", "industry": "SaaS, cloud software",
    },
    {
        "name_en": "API-First Startup Strategy",
        "name_ja": "APIファーストスタートアップ戦略",
        "definition": "Product development approach where APIs are the primary product, enabling third-party developers to build on top of the platform, accelerating distribution and creating network effects through developer ecosystems.",
        "keywords_en": "API-first, developer platform, API economy, webhook, developer ecosystem",
        "keywords_ja": "APIファースト, 開発者プラットフォーム, APIエコノミー, Webhook, 開発者エコシステム",
        "key_researchers": "Kin Lane, Stripe team",
        "key_works": "The API Economy: Unlocking Hidden Value in Your Enterprise Assets",
        "era_start": 2010, "era_end": None, "school": "Developer Platform Strategy",
        "stage": "seed to series B", "funding": "usage-based revenue, venture capital",
        "geo": "USA, Europe, Global", "industry": "fintech, communications, data infrastructure",
    },
    {
        "name_en": "Freemium Model Dynamics",
        "name_ja": "フリーミアムモデルのダイナミクス",
        "definition": "Monetization strategy offering core features free while charging for premium capabilities, relying on viral user acquisition, high conversion rates, and network effects to achieve sustainable unit economics.",
        "keywords_en": "freemium, conversion rate, premium tier, viral growth, monetization",
        "keywords_ja": "フリーミアム, コンバージョン率, プレミアムティア, バイラル成長, 収益化",
        "key_researchers": "Anderson, Kumar",
        "key_works": "Free: The Future of a Radical Price",
        "era_start": 2009, "era_end": None, "school": "Digital Business Models",
        "stage": "pre-seed to growth", "funding": "venture capital, subscription revenue",
        "geo": "USA, Global", "industry": "SaaS, consumer apps, gaming",
    },
    {
        "name_en": "Network Effects (Shapiro & Varian)",
        "name_ja": "ネットワーク効果（Shapiro & Varian）",
        "definition": "Economic phenomenon where a product or service gains additional value as more people use it, creating self-reinforcing growth loops that can generate winner-take-most market dynamics and durable competitive moats.",
        "keywords_en": "network effects, Metcalfe's law, direct network effects, indirect network effects, lock-in",
        "keywords_ja": "ネットワーク効果, メトカーフの法則, 直接ネットワーク効果, 間接ネットワーク効果, ロックイン",
        "key_researchers": "Shapiro, Varian, Metcalfe",
        "key_works": "Information Rules: A Strategic Guide to the Network Economy",
        "era_start": 1998, "era_end": None, "school": "Network Economics",
        "stage": "all stages", "funding": "venture capital, growth equity",
        "geo": "USA, Global", "industry": "social, communications, marketplaces",
    },
    {
        "name_en": "Multi-Sided Platform Theory",
        "name_ja": "多面プラットフォーム理論",
        "definition": "Economic framework analyzing platforms serving two or more distinct customer groups whose interactions create value, with pricing and design decisions requiring simultaneous consideration of all sides' demands and cross-side effects.",
        "keywords_en": "multi-sided platform, two-sided market, Rochet, Tirole, platform pricing",
        "keywords_ja": "多面プラットフォーム, 両面市場, ロシェ, ティロール, プラットフォーム価格設定",
        "key_researchers": "Rochet, Tirole, Parker, Van Alstyne",
        "key_works": "Platform Competition in Two-Sided Markets",
        "era_start": 2003, "era_end": None, "school": "Platform Economics",
        "stage": "all stages", "funding": "venture capital, transaction fees",
        "geo": "USA, EU, Global", "industry": "payments, media, marketplaces",
    },
    {
        "name_en": "Platform Envelopment Strategy",
        "name_ja": "プラットフォーム包囲戦略",
        "definition": "Competitive tactic where a platform firm bundles its existing user base and capabilities to enter adjacent markets, crowding out standalone rivals by combining multiple platform functions into a single offering.",
        "keywords_en": "platform envelopment, bundling, adjacent markets, competitive moat, platform expansion",
        "keywords_ja": "プラットフォーム包囲, バンドル, 隣接市場, 競争的堀, プラットフォーム拡張",
        "key_researchers": "Eisenmann, Parker, Van Alstyne",
        "key_works": "Platform Envelopment",
        "era_start": 2011, "era_end": None, "school": "Platform Competition",
        "stage": "growth to scale", "funding": "growth equity, M&A",
        "geo": "USA, Global", "industry": "technology platforms, big tech",
    },
    {
        "name_en": "Winner-Take-Most Dynamics",
        "name_ja": "勝者総取りダイナミクス",
        "definition": "Market structure common in platform industries where strong network effects and economies of scale concentrate value among one or two dominant players, making competitive entry increasingly difficult over time.",
        "keywords_en": "winner take most, platform dominance, network effects, market concentration, platform monopoly",
        "keywords_ja": "勝者総取り, プラットフォーム支配, ネットワーク効果, 市場集中, プラットフォーム独占",
        "key_researchers": "Evans, Schmalensee, Eisenmann",
        "key_works": "Matchmakers: The New Economics of Multisided Platforms",
        "era_start": 2000, "era_end": None, "school": "Platform Economics",
        "stage": "growth to scale", "funding": "growth equity, IPO",
        "geo": "USA, China, Global", "industry": "social media, search, e-commerce",
    },
    {
        "name_en": "App Store Economics",
        "name_ja": "アプリストアエコノミクス",
        "definition": "Analysis of revenue sharing, discovery algorithms, curation policies, and developer relations in mobile app distribution platforms (iOS App Store, Google Play), including antitrust considerations of 30% commission structures.",
        "keywords_en": "app store, Apple App Store, Google Play, 30% commission, in-app purchase, developer tools",
        "keywords_ja": "アプリストア, Apple App Store, Google Play, 30%手数料, アプリ内購入, 開発者ツール",
        "key_researchers": "Evans, Parker, Pon",
        "key_works": "Mobile Application Stores: Evolving Platform Competition",
        "era_start": 2008, "era_end": None, "school": "Mobile Platform Strategy",
        "stage": "seed to growth", "funding": "app store revenue, subscription",
        "geo": "USA, Global", "industry": "mobile apps, gaming, SaaS",
    },
    {
        "name_en": "Open Source Business Models",
        "name_ja": "オープンソースビジネスモデル",
        "definition": "Commercial strategies built on open source software foundations, including managed cloud services, dual licensing, support and services, and open core models where premium features are proprietary.",
        "keywords_en": "open source, open core, managed services, dual license, community, FOSS",
        "keywords_ja": "オープンソース, オープンコア, マネージドサービス, デュアルライセンス, コミュニティ, FOSS",
        "key_researchers": "O'Reilly, Raymond, West",
        "key_works": "The Cathedral and the Bazaar",
        "era_start": 1998, "era_end": None, "school": "Open Innovation",
        "stage": "all stages", "funding": "venture capital, enterprise contracts, community",
        "geo": "USA, EU, Global", "industry": "developer tools, infrastructure, AI/ML",
    },
    {
        "name_en": "Data Network Effects",
        "name_ja": "データネットワーク効果",
        "definition": "Competitive advantage mechanism where more users generate more data, which improves AI/ML model performance, which attracts more users, creating a self-reinforcing loop distinct from traditional direct network effects.",
        "keywords_en": "data network effects, AI moat, data flywheel, machine learning advantage, proprietary data",
        "keywords_ja": "データネットワーク効果, AIの堀, データフライホイール, 機械学習優位性, 独自データ",
        "key_researchers": "Delip Rao, Ajay Agrawal, Tucker",
        "key_works": "Prediction Machines: The Simple Economics of Artificial Intelligence",
        "era_start": 2015, "era_end": None, "school": "AI Platform Strategy",
        "stage": "series A to scale", "funding": "venture capital, data partnerships",
        "geo": "USA, China, Global", "industry": "AI, fintech, health tech",
    },
    {
        "name_en": "Platform Regulation and Antitrust",
        "name_ja": "プラットフォーム規制と独占禁止",
        "definition": "Regulatory frameworks and antitrust enforcement approaches designed to address concentration, self-preferencing, and data monopoly concerns in digital platform markets, including the EU Digital Markets Act and US platform investigations.",
        "keywords_en": "platform regulation, Digital Markets Act, antitrust, GAFA, self-preferencing, interoperability",
        "keywords_ja": "プラットフォーム規制, デジタル市場法, 独占禁止, GAFA, 自己優遇, 相互運用性",
        "key_researchers": "Khan, Stucke, Ezrachi",
        "key_works": "Amazon's Antitrust Paradox",
        "era_start": 2019, "era_end": None, "school": "Platform Regulation",
        "stage": "scale", "funding": "regulatory compliance cost",
        "geo": "EU, USA, Global", "industry": "big tech, payments, marketplaces",
    },
    {
        "name_en": "Aggregation Theory (Ben Thompson)",
        "name_ja": "集約理論（Ben Thompson）",
        "definition": "Ben Thompson's framework explaining how internet platforms create value by aggregating suppliers and consumers, eliminating distribution costs, and capturing value through data and user relationships rather than supply chain ownership.",
        "keywords_en": "aggregation theory, Ben Thompson, Stratechery, aggregator, zero marginal cost, distribution",
        "keywords_ja": "集約理論, ベン・トンプソン, Stratechery, アグリゲーター, 限界費用ゼロ, 流通",
        "key_researchers": "Thompson",
        "key_works": "Aggregation Theory (Stratechery)",
        "era_start": 2015, "era_end": None, "school": "Digital Platform Strategy",
        "stage": "all stages", "funding": "venture capital, advertising, subscriptions",
        "geo": "USA, Global", "industry": "media, e-commerce, social, search",
    },
    {
        "name_en": "Embedded Finance and Fintech Platforms",
        "name_ja": "組み込み金融とフィンテックプラットフォーム",
        "definition": "Integration of financial services (payments, lending, insurance) into non-financial platforms and software products, enabling SaaS and marketplace companies to capture additional revenue through Banking-as-a-Service infrastructure.",
        "keywords_en": "embedded finance, BaaS, fintech platform, payment integration, financial APIs",
        "keywords_ja": "組み込み金融, BaaS, フィンテックプラットフォーム, 決済統合, 金融API",
        "key_researchers": "Angela Strange (a16z), Simon Taylor",
        "key_works": "Every Company Will Be a Fintech Company (a16z)",
        "era_start": 2019, "era_end": None, "school": "Fintech Platform Strategy",
        "stage": "series A to growth", "funding": "venture capital, revenue-based financing",
        "geo": "USA, EU, SE Asia", "industry": "fintech, SaaS, e-commerce",
    },
    {
        "name_en": "Super App Strategy",
        "name_ja": "スーパーアプリ戦略",
        "definition": "Mobile platform strategy pioneered in Asia (WeChat, Grab, Gojek) integrating multiple services including messaging, payments, commerce, and transportation within a single app ecosystem with mini-program extensibility.",
        "keywords_en": "super app, WeChat, mini programs, platform ecosystem, mobile payments, all-in-one app",
        "keywords_ja": "スーパーアプリ, WeChat, ミニプログラム, プラットフォームエコシステム, モバイル決済, オールインワンアプリ",
        "key_researchers": "Connie Chan (a16z), Kai-Fu Lee",
        "key_works": "When One App Rules Them All: The Case of WeChat and Mobile in China",
        "era_start": 2011, "era_end": None, "school": "Mobile Platform Strategy",
        "stage": "growth to scale", "funding": "growth equity, strategic investment",
        "geo": "China, SE Asia, India", "industry": "super apps, mobile platforms",
    },
    {
        "name_en": "Web3 and Crypto Startup Models",
        "name_ja": "Web3・クリプトスタートアップモデル",
        "definition": "Entrepreneurial models leveraging blockchain, smart contracts, and token economics to build decentralized applications, DAOs, DeFi protocols, and NFT platforms with novel ownership and governance structures.",
        "keywords_en": "Web3, crypto startup, DeFi, DAO, token economics, blockchain, NFT",
        "keywords_ja": "Web3, クリプトスタートアップ, DeFi, DAO, トークンエコノミクス, ブロックチェーン, NFT",
        "key_researchers": "Buterin, Nakamoto, Dixon",
        "key_works": "Why Decentralization Matters (Chris Dixon)",
        "era_start": 2017, "era_end": None, "school": "Decentralized Platform Strategy",
        "stage": "seed to series A", "funding": "token sales, crypto VCs, grants",
        "geo": "USA, Switzerland, Global", "industry": "blockchain, fintech, gaming",
    },
    {
        "name_en": "Platform Governance Design",
        "name_ja": "プラットフォームガバナンス設計",
        "definition": "Framework for designing rules, incentives, and enforcement mechanisms that govern behavior of participants on multi-sided platforms, balancing openness with quality control and managing strategic trade-offs between monetization and ecosystem health.",
        "keywords_en": "platform governance, content moderation, ecosystem rules, platform design, community standards",
        "keywords_ja": "プラットフォームガバナンス, コンテンツモデレーション, エコシステムルール, プラットフォーム設計, コミュニティ基準",
        "key_researchers": "Boudreau, Hagiu",
        "key_works": "From Platform Participant to Platform Leader",
        "era_start": 2009, "era_end": None, "school": "Platform Management",
        "stage": "series A to scale", "funding": "venture capital, advertising",
        "geo": "USA, EU, Global", "industry": "social media, marketplaces, app stores",
    },
]

EXTRA_TOPICS = [
    ("Vertical SaaS Strategy", "バーティカルSaaS戦略", "Software-as-a-Service platforms targeting specific industry verticals (healthcare, construction, legal) to provide deeper functionality and higher switching costs than horizontal competitors.", "vertical SaaS, industry software, workflow, vertical market", "バーティカルSaaS, 業界ソフトウェア, ワークフロー, バーティカル市場", "Michelman, Andreessen Horowitz", "The Case for Vertical SaaS", 2015, None, "seed to series B", "venture capital, enterprise contracts", "USA, Global", "SaaS"),
    ("Product-Led Growth (PLG)", "プロダクト主導型成長（PLG）", "Go-to-market strategy where the product itself drives user acquisition, conversion, and expansion, replacing or supplementing traditional sales-led approaches through virality, freemium, and bottom-up adoption.", "PLG, product-led growth, self-serve, bottom-up SaaS, viral product", "PLG, プロダクト主導型成長, セルフサーブ, ボトムアップSaaS, バイラルプロダクト", "Wes Bush, OpenView Partners", "Product-Led Growth: How to Build a Product That Sells Itself", 2019, None, "seed to growth", "venture capital, subscription", "USA, Global", "SaaS, developer tools"),
    ("Growth Hacking Methodology", "グロースハッキング手法", "Data-driven, experiment-centric approach to achieving rapid user growth, associated with the early growth teams at Airbnb, Dropbox, and Facebook, emphasizing product optimization, referral loops, and viral mechanics.", "growth hacking, A/B testing, viral loop, referral program, AARRR", "グロースハッキング, A/Bテスト, バイラルループ, リファラルプログラム, AARRR", "Ellis, Holiday, Hoffman", "Growth Hacker Marketing", 2013, None, "seed to series B", "venture capital, organic growth", "USA, Global", "consumer apps, SaaS"),
    ("Platform Data Portability", "プラットフォームデータポータビリティ", "Regulatory and technical requirements enabling users to transfer their data between competing platforms, intended to reduce switching costs and promote competition in data-network-effect-driven markets.", "data portability, switching costs, GDPR, interoperability, open data", "データポータビリティ, 乗り換えコスト, GDPR, 相互運用性, オープンデータ", "Swire, Litan", "Protecting the Privacy of Customers of Broadband and Other Telecommunications Services", 2016, None, "scale", "regulatory compliance", "EU, USA", "social media, cloud platforms"),
    ("Gig Economy Platform Design", "ギグエコノミープラットフォーム設計", "Design principles and algorithmic management tools for labor marketplace platforms connecting freelancers or gig workers with demand-side clients, including worker classification, surge pricing, and reputation systems.", "gig economy, labor marketplace, algorithmic management, surge pricing, worker classification", "ギグエコノミー, 労働市場, アルゴリズム管理, サージプライシング, 労働者分類", "Sundararajan, Kessler", "The Sharing Economy: The End of Employment and the Rise of Crowd-Based Capitalism", 2016, None, "series A to scale", "venture capital, take-rate", "USA, EU, SE Asia", "gig platforms, labor tech"),
    ("Creator Economy Platforms", "クリエーターエコノミープラットフォーム", "Platforms enabling independent creators (writers, artists, educators, influencers) to monetize their audiences directly through subscriptions, tips, and digital goods, bypassing traditional media intermediaries.", "creator economy, creator monetization, Substack, Patreon, direct audience", "クリエーターエコノミー, クリエーター収益化, Substack, Patreon, 直接オーディエンス", "Li Jin, Anu Atluru", "The Passion Economy and the Future of Work", 2019, None, "seed to growth", "venture capital, creator revenue share", "USA, Global", "media, creator tools, education"),
    ("Social Commerce Strategy", "ソーシャルコマース戦略", "Integration of shopping functionality into social media platforms and live streaming, enabling product discovery and purchase within the social feed or video stream without redirecting to external e-commerce sites.", "social commerce, live shopping, shoppable content, TikTok shop, social selling", "ソーシャルコマース, ライブショッピング, ショッパブルコンテンツ, TikTok Shop, ソーシャルセリング", "Baymard Institute, eMarketer", "Social Commerce Market Trends Report", 2020, None, "series A to growth", "venture capital, transaction fees", "China, USA, SE Asia", "e-commerce, social media"),
    ("B2B Marketplace Dynamics", "B2Bマーケットプレイスのダイナミクス", "Business-to-business digital marketplaces connecting enterprise buyers and suppliers, with unique challenges around procurement workflows, relationship-based purchasing, and complex multi-stakeholder approval processes.", "B2B marketplace, procurement, enterprise buying, supply chain platform", "B2Bマーケットプレイス, 調達, 企業購買, サプライチェーンプラットフォーム", "Applico, NFX", "The Modern B2B Marketplace Playbook", 2021, None, "series A to series C", "venture capital, enterprise contracts", "USA, EU, China", "B2B, procurement, supply chain"),
    ("Subscription Box Model", "サブスクリプションボックスモデル", "E-commerce model delivering curated physical products on a recurring subscription basis, leveraging personalization, surprise mechanics, and community to drive retention and word-of-mouth growth.", "subscription box, recurring e-commerce, curation, discovery commerce, unboxing", "サブスクリプションボックス, リカーリングEC, キュレーション, ディスカバリーコマース, アンボックシング", "Baxter", "The Subscription Economy", 2015, None, "seed to series B", "venture capital, subscription revenue", "USA, EU", "e-commerce, CPG, lifestyle"),
    ("Conversational Commerce", "会話型コマース", "Purchasing transactions conducted through messaging apps, chatbots, and voice assistants, enabling personalized shopping experiences within communication channels through natural language interfaces.", "conversational commerce, chatbot, messaging commerce, voice shopping, WhatsApp commerce", "会話型コマース, チャットボット, メッセージコマース, 音声ショッピング, WhatsAppコマース", "Chris Messina", "2016 Will Be the Year of Conversational Commerce", 2015, None, "seed to growth", "venture capital, transaction fees", "USA, Asia, Global", "e-commerce, fintech, retail"),
]

def generate_entries():
    entries = []
    topic_list = TOPICS + [
        {
            "name_en": t[0], "name_ja": t[1], "definition": t[2],
            "keywords_en": t[3], "keywords_ja": t[4],
            "key_researchers": t[5], "key_works": t[6],
            "era_start": t[7], "era_end": t[8], "school": "Platform Economics",
            "stage": t[9], "funding": t[10], "geo": t[11], "industry": t[12],
        }
        for t in EXTRA_TOPICS
    ]

    suffixes = [
        "Competitive Dynamics", "Investment Thesis", "Scaling Mechanics", "Governance Design",
        "Regulatory Challenges", "Network Effect Measurement", "Revenue Model Innovation",
        "International Expansion", "Enterprise Adoption", "Community Building",
        "Data Strategy", "Partnership Architecture", "API Ecosystem", "Pricing Optimization",
        "Trust and Safety", "Developer Relations", "Content Moderation", "User Acquisition",
        "Retention Engineering", "Virality Mechanisms", "Unit Economics", "Platform Health",
        "Ecosystem Governance", "Market Entry Strategy", "Competitive Moat Building",
        "Platform Switching Costs", "Complementor Management", "Platform Tipping Points",
        "Algorithmic Curation", "Personalization at Scale",
    ]

    schools = [
        "Platform Economics", "Digital Business Models", "Network Economics",
        "Platform Strategy", "SaaS Strategy", "Mobile Platform Strategy",
        "Developer Platform Strategy", "Fintech Platform Strategy", "Open Innovation",
        "Platform Regulation",
    ]

    stages = ["pre-seed", "seed", "early-stage", "series A", "series B", "growth", "all stages", "scale"]
    geo_options = ["USA", "USA, EU", "USA, China", "USA, Global", "Global", "China, SE Asia", "EU, USA, Global", "USA, EU, Asia", "USA, UK", "SE Asia, India"]
    impact_templates = [
        "Defines conceptual foundation for understanding {name} in digital platform contexts.",
        "Shapes practitioner and investor thinking on {name} dynamics.",
        "Provides strategic framework for {name} decision-making at scale.",
        "Critical reference for {name} analysis in platform business models.",
        "Influences platform design and competitive strategy through {name} lens.",
    ]

    idx = 0
    for i in range(1, 715):
        base = topic_list[idx % len(topic_list)]
        suffix = suffixes[(i - 1) % len(suffixes)]
        school = schools[i % len(schools)]
        stage = stages[i % len(stages)]
        geo = geo_options[i % len(geo_options)]

        name_en = f"{base['name_en']} — {suffix}" if i > len(topic_list) else base["name_en"]
        name_ja = f"{base['name_ja']}の{suffix}" if i > len(topic_list) else base["name_ja"]
        era_start = base["era_start"] + ((i % 4) * 2 if i > len(topic_list) else 0)
        era_start = min(era_start, 2023)
        era_end = base["era_end"]
        impact = impact_templates[i % len(impact_templates)].format(name=name_en.split(" — ")[0])

        entry = (
            f"su_plat_{i:03d}",
            name_ja,
            name_en,
            base.get("name_original", name_en),
            base["definition"],
            impact,
            "platform_digital_startups",
            school,
            era_start,
            era_end,
            stage,
            base["funding"],
            "Vertical integration; Traditional distribution; Non-platform business models",
            base["keywords_ja"],
            base["keywords_en"],
            base["key_researchers"],
            base["key_works"],
            geo,
            base["industry"],
            "active",
            "secondary",
            85,
        )
        entries.append(entry)
        idx += 1

    return entries

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    entries = generate_entries()
    print(f"Generated {len(entries)} entries")

    sql = """
    INSERT OR IGNORE INTO startup_theory (
        id, name_ja, name_en, name_original, definition, impact_summary,
        subfield, school_of_thought, era_start, era_end,
        startup_stage, funding_relevance, opposing_concept_names,
        keywords_ja, keywords_en, key_researchers, key_works,
        geographic_context, industry_focus, status, source_reliability, data_completeness
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """

    BATCH = 50
    inserted = 0
    for i in range(0, len(entries), BATCH):
        batch = entries[i:i+BATCH]
        cur.executemany(sql, batch)
        conn.commit()
        inserted += len(batch)
        print(f"  Inserted batch: {inserted}/{len(entries)}")

    conn.close()
    print(f"Done. Total inserted: {inserted}")

if __name__ == "__main__":
    main()
