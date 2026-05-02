#!/usr/bin/env python3
"""Generate measurement_policy_governance entries batch 3 (inno_pol_553 to inno_pol_714)."""

import json
import os

entries = []
idx = 553

def add(name_en, name_ja, definition, impact, school, era_start, era_end, innov_type, cog_mech, researchers, works, opposing, kw_ja, kw_en):
    global idx
    entries.append({
        "id": f"inno_pol_{idx}",
        "name_en": name_en,
        "name_ja": name_ja,
        "definition": definition,
        "impact_summary": impact,
        "subfield": "measurement_policy_governance",
        "school_of_thought": school,
        "era_start": era_start,
        "era_end": era_end,
        "innovation_type": innov_type,
        "cognitive_mechanism": cog_mech,
        "key_researchers": json.dumps(researchers, ensure_ascii=False),
        "key_works": json.dumps(works, ensure_ascii=False),
        "opposing_concept_names": opposing,
        "keywords_ja": kw_ja,
        "keywords_en": kw_en,
        "schumpeter_layer": "macro",
        "status": "active",
        "source_reliability": "secondary",
        "data_completeness": 75,
    })
    idx += 1

# === ADVANCED MEASUREMENT METHODS (553-580) ===
add("Technological Diversification Index", "技術的多角化指数",
    "企業や国が活動する技術分野の広がりを定量化する指標。特許のIPC分類分布からエントロピー指数やハーフィンダール指数を算出し、技術ポートフォリオの多角化度とイノベーション戦略の方向性を評価する。",
    "技術ポートフォリオの多角化度の定量的評価。", "イノベーション計量学", 1990, None, "measurement", "learning",
    ["Pari Patel", "Keith Pavitt"], ["Patel & Pavitt (1997) The technological competencies of the world's largest firms"], "",
    "技術多角化,エントロピー指数,技術ポートフォリオ", "technological diversification, entropy index, technology portfolio")

add("Technology Life Cycle Analysis", "技術ライフサイクル分析",
    "特定技術の誕生から成熟・衰退までのライフサイクル段階を特許出願パターン、論文数変化、市場浸透率等のデータから推定する分析手法。S字曲線フィッティングと成長率分析が基本的アプローチ。",
    "技術の発展段階の定量的推定と戦略的意思決定支援。", "イノベーション計量学", 1985, None, "measurement", "learning",
    ["William Abernathy", "James Utterback"], ["Utterback & Abernathy (1975) A Dynamic Model of Process and Product Innovation"], "",
    "技術ライフサイクル,S字曲線,成長率分析", "technology life cycle, S-curve, growth rate analysis, maturity stage")

add("Innovation System Benchmarking", "イノベーションシステム・ベンチマーキング",
    "複数の国・地域のイノベーションシステムのパフォーマンスを多次元的に比較・評価するプロセス。ベストプラクティスの特定と政策学習を目的とし、EIS、GII等の合成指標とケーススタディを組み合わせる。",
    "イノベーションシステム間の体系的な比較学習プロセス。", "イノベーション計量学", 2000, None, "measurement,policy", "policy,learning",
    ["OECD", "European Commission"], ["OECD Reviews of Innovation Policy"], "",
    "ベンチマーキング,国際比較,ベストプラクティス", "benchmarking, international comparison, best practice, system performance")

add("Knowledge Spillover Measurement", "知識スピルオーバーの測定",
    "R&D活動から生じる知識の外部性（スピルオーバー）を特許引用、共同発明、生産性への間接効果等から定量的に測定する方法論。空間的減衰パターン、技術的近接性、制度的チャネルの分析を含む。",
    "知識の外部性の定量的測定と空間的パターン分析。", "イノベーション計量学", 1993, None, "measurement", "learning",
    ["Adam Jaffe", "Manuel Trajtenberg", "Maryann Feldman"], ["Jaffe et al. (1993) Geographic Localization of Knowledge Spillovers"], "",
    "知識スピルオーバー,外部性,空間的減衰", "knowledge spillover, externality, spatial decay, technology proximity")

add("Innovation Surveys in Developing Countries", "途上国のイノベーション調査",
    "CIS型イノベーション調査を途上国の文脈に適応させる方法論的課題と実践。ボゴタ・マニュアル（RICYT）がラテンアメリカ向けの適応指針を提供し、インフォーマル・セクターのイノベーション捕捉等の固有課題に対処する。",
    "途上国文脈に適応したイノベーション測定方法論。", "イノベーション計量学", 2000, None, "measurement", "policy,learning",
    ["RICYT", "UIS UNESCO"], ["Bogota Manual (RICYT, 2001)"], "",
    "途上国調査,ボゴタマニュアル,RICYT", "developing country survey, Bogota Manual, RICYT, adaptation")

add("Micro-Level Innovation Data Linking", "ミクロレベル・イノベーションデータ連結",
    "企業レベルのイノベーション調査データ、特許データ、財務データ、雇用データ等を企業識別子で連結し、包括的な企業イノベーション・プロファイルを構築する方法論。OECD MICRODATAプロジェクト等が推進。",
    "多ソースデータの企業レベル連結による包括的分析。", "イノベーション計量学", 2008, None, "measurement", "learning",
    ["OECD", "Eurostat"], ["OECD DynEmp/MultiProd Projects"], "",
    "データ連結,企業レベル分析,多ソースデータ", "data linking, firm-level analysis, multi-source data, microdata")

add("Real-Time Innovation Indicators", "リアルタイム・イノベーション指標",
    "Web、SNS、求人情報、特許出願、クラウドファンディング等のデジタルデータソースから、ほぼリアルタイムでイノベーション活動を追跡する指標群。従来の調査ベース指標の1-2年の遅延を克服する。",
    "リアルタイムでのイノベーション活動追跡。", "イノベーション計量学", 2015, None, "measurement", "learning",
    ["OECD", "Nesta"], ["Nesta Innovation Mapping Reports"], "",
    "リアルタイム指標,デジタルトレース,ビッグデータ", "real-time indicators, digital trace, big data, nowcasting")

add("Gender Equality in Innovation Indicators", "イノベーション指標におけるジェンダー平等",
    "特許発明者、研究者、起業家、CIS回答企業のリーダーシップ等におけるジェンダー別データの体系的収集と分析。ジェンダーギャップの定量化と、ジェンダー多様性がイノベーション・パフォーマンスに与える影響の実証。",
    "イノベーション活動のジェンダー格差の体系的測定。", "イノベーション計量学", 2010, None, "measurement,policy", "policy",
    ["European Commission", "OECD"], ["OECD STI Scoreboard Gender Chapter"], "",
    "ジェンダー指標,女性発明者,多様性効果", "gender indicators, women inventors, diversity effect, gender gap")

add("Eco-Patent Commons", "エコパテント・コモンズ",
    "環境技術特許を無償で公開し、環境イノベーションの普及を促進する自発的なイニシアチブ。IBM、Nokia等が参加し、特許の排他的権利を放棄して環境技術のオープンな利用を可能にする。",
    "環境技術特許の自発的な共有によるグリーンイノベーション促進。", "イノベーション政策", 2008, None, "institutional,policy", "policy",
    ["WBCSD", "IBM"], ["Eco-Patent Commons Initiative"], "",
    "エコパテント,環境技術共有,特許コモンズ", "eco-patent commons, environmental technology sharing, patent commons")

add("WIPO Technology Trends Report", "WIPO技術トレンドレポート",
    "WIPOが特許データの大規模分析に基づいて特定技術領域のグローバルなイノベーション・トレンドを報告するシリーズ。AI（2019年）、支援技術（2021年）等をテーマに、技術開発の地理的分布と時系列変化を分析。",
    "特許データに基づくグローバル技術トレンドの体系的分析。", "特許分析", 2019, None, "measurement", "learning",
    ["WIPO"], ["WIPO Technology Trends Reports"], "",
    "WIPO技術トレンド,グローバル分析,AI特許", "WIPO technology trends, global analysis, AI patents, patent data analytics")

add("Innovation Output Gap Analysis", "イノベーション・アウトプットギャップ分析",
    "イノベーション・インプット水準から期待されるアウトプット水準と実際のアウトプットの差（イノベーション・ギャップ）を推計し、イノベーション・システムの効率性を評価する分析手法。",
    "イノベーション・システムの効率性ギャップの診断。", "イノベーション計量学", 2007, None, "measurement", "policy,learning",
    ["WIPO", "European Commission"], ["GII Innovation Efficiency Analysis"], "",
    "アウトプットギャップ,効率性分析,システム診断", "output gap, efficiency analysis, system diagnosis, innovation gap")

add("Innovation Radar Approach to Technology Scouting", "テクノロジー・スカウティングのイノベーション・レーダーアプローチ",
    "企業や政府機関が外部の技術環境を体系的にスキャンし、潜在的に重要な技術やイノベーション機会を早期に発見する手法。特許マイニング、学術論文分析、スタートアップ・スカウティング等のツールを統合する。",
    "外部技術環境の体系的スキャンによる機会発見手法。", "技術フォーサイト", 2010, None, "measurement", "learning",
    ["Henry Chesbrough"], ["Chesbrough (2003) Open Innovation"], "",
    "テクノロジースカウティング,技術探索,機会発見", "technology scouting, technology exploration, opportunity discovery")

add("Innovation Procurement Metrics", "イノベーション調達指標",
    "公共調達のうちイノベーション促進要素を含む調達の割合、金額、手法分布を測定する指標体系。Pre-commercial procurement、イノベーション・パートナーシップ、機能要件仕様等のイノベーション調達手法の採用状況を追跡する。",
    "イノベーション調達の普及度と効果の定量的追跡。", "イノベーション計量学", 2015, None, "measurement,policy", "policy",
    ["European Commission"], ["EC Innovation Procurement Data"], "",
    "イノベーション調達指標,公共調達追跡", "innovation procurement metrics, public procurement tracking")

# === INNOVATION GOVERNANCE & INSTITUTIONAL DESIGN (567-600) ===
add("Innovation Agency Design Principles", "イノベーション機関設計原則",
    "国家レベルのイノベーション支援機関（Innovate UK、Vinnova、Tekes/Business Finland等）の組織設計・ガバナンスの最適化原則。ミッション定義、自律性、説明責任、評価メカニズム、政策整合等の設計変数を体系化する。",
    "イノベーション支援機関の効果的組織設計の原則。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["OECD"], ["OECD Reviews of Innovation Agencies"], "",
    "イノベーション機関,組織設計,ガバナンス", "innovation agency, organizational design, governance, institutional design")

add("Vinnova Model (Sweden)", "Vinnovaモデル（スウェーデン）",
    "スウェーデンのイノベーション庁Vinnovaの組織モデル。チャレンジ駆動型イノベーション・プログラム、戦略的イノベーション・プログラム（SIP）、需要サイド政策の統合を特徴とし、北欧型イノベーション政策の制度的実現。",
    "北欧型イノベーション政策の制度的実現モデル。", "イノベーション政策", 2001, None, "policy,institutional", "policy",
    ["Vinnova"], ["Vinnova Strategy Documents"], "",
    "Vinnova,スウェーデン,戦略的プログラム", "Vinnova, Sweden, strategic innovation program, challenge-driven")

add("Business Finland Model", "Business Finlandモデル",
    "フィンランドのイノベーション支援機関（旧Tekes + Finpro統合）のモデル。R&D助成と国際化支援を一体化し、小国のイノベーション企業のグローバル市場アクセスを包括的に支援する。",
    "R&D支援と国際化支援の統合による小国イノベーション促進。", "イノベーション政策", 2018, None, "policy,institutional", "policy",
    ["Business Finland"], ["Business Finland Annual Reports"], "",
    "Business Finland,フィンランド,国際化支援", "Business Finland, Finland, internationalization, innovation support")

add("DARPA-Style Program Management", "DARPA型プログラム管理",
    "DARPAのプログラム・マネージャー（PM）制度に基づく研究マネジメント手法。3-5年の任期制PM、トップダウンの課題設定、技術的リスクの積極的受容、迅速な資金配分・中止判断を特徴とする革新的な研究運営方式。",
    "ハイリスク・ハイリターン研究の効果的マネジメント手法。", "イノベーション政策", 1958, None, "institutional,policy", "policy",
    ["DARPA"], ["Fuchs (2010) Rethinking the Role of the State in Technology Development"], "",
    "DARPAプログラム管理,PM制度,ハイリスク研究", "DARPA program management, PM system, high-risk research")

add("National Research Council Model", "国立研究評議会モデル",
    "各国の研究システムの戦略的方向性を策定する最上位の諮問機関の組織設計。米国NRC、日本のCST、英国のUKRI等が代表的で、科学的助言と政策策定の接続メカニズムを制度化する。",
    "科学的助言と研究政策策定の制度的接続。", "イノベーション政策", 1916, None, "institutional,policy", "policy",
    ["US National Research Council"], ["NRC Advisory Reports"], "",
    "国立研究評議会,科学的助言,政策策定", "national research council, scientific advice, policy formulation")

add("Innovation Policy Advisory Council", "イノベーション政策諮問会議",
    "国家レベルでのイノベーション政策の戦略的方向性について政府に助言する上級諮問機関。科学者、企業人、市民社会代表で構成され、イノベーション・ガバナンスの最上位レベルの意思決定を支援する。",
    "国家イノベーション政策の戦略的方向付けを担う諮問機能。", "イノベーション政策", 2000, None, "institutional,policy", "policy",
    ["Various national governments"], ["OECD Innovation Policy Governance Reviews"], "",
    "政策諮問会議,戦略的助言,イノベーションガバナンス", "policy advisory council, strategic advice, innovation governance")

add("Place-Based Innovation Policy", "場所ベースのイノベーション政策",
    "地域の固有の文脈（資源、制度、文化、産業構造）に基づいてイノベーション政策を設計する空間的アプローチ。スマート専門化の理論的基盤であり、一律的な政策処方箋（one-size-fits-all）への批判から発展した。",
    "地域固有の文脈に基づくイノベーション政策設計。", "イノベーション政策", 2009, None, "policy,systemic", "policy,learning",
    ["Fabrizio Barca", "Philip McCann"], ["Barca (2009) An Agenda for a Reformed Cohesion Policy"], "",
    "場所ベース政策,地域文脈,スマート専門化", "place-based policy, regional context, smart specialisation, territorial")

add("Experimental Regulation for Innovation", "イノベーションのための実験的規制",
    "規制の効果を事前に厳密に評価するため、規制をパイロット的に限定適用し、その影響を実証的に検証してから本格導入するアプローチ。規制サンドボックスを超えた包括的な実験的規制設計の方法論。",
    "規制設計への実験的アプローチの体系化。", "イノベーション政策", 2018, None, "policy,institutional", "policy,learning",
    ["OECD", "European Commission"], ["OECD Regulatory Policy Outlook"], "",
    "実験的規制,パイロット規制,規制実験", "experimental regulation, pilot regulation, regulatory experiment")

add("Innovation Fund (EU ETS)", "イノベーション基金（EU ETS）",
    "EUの排出量取引制度（ETS）の排出枠オークション収入からイノベーティブなクリーンテクノロジーの実証プロジェクトを資金支援する仕組み。100億ユーロ規模で、CCS、再エネ、産業脱炭素等の大規模実証を支援。",
    "排出量取引収入によるクリーンテクノロジー実証支援。", "イノベーション政策", 2020, None, "policy", "policy",
    ["European Commission"], ["EU Innovation Fund Programme"], "",
    "イノベーション基金,EU ETS,クリーンテクノロジー", "Innovation Fund, EU ETS, clean technology, decarbonization")

add("Challenge-Based Innovation Programme", "チャレンジベース・イノベーション・プログラム",
    "社会的課題（気候変動、高齢化、都市化等）を出発点としてイノベーション活動を組織する資金配分手法。課題の定義にステークホルダーが参加し、学際的・セクター横断的なアプローチで解決策を追求する。",
    "社会的課題からイノベーション活動を組織する資金配分手法。", "イノベーション政策", 2010, None, "policy,systemic", "policy,learning",
    ["Vinnova", "European Commission"], ["Vinnova Challenge-Driven Innovation Reports"], "",
    "チャレンジベース,社会的課題,学際的アプローチ", "challenge-based, social challenges, interdisciplinary approach")

add("Innovation Policy Monitoring and Evaluation System", "イノベーション政策モニタリング・評価システム",
    "イノベーション政策の実施状況と成果を継続的にモニタリングし、定期的に包括的評価を行う制度的システム。ロジックモデル、Theory of Change、KPI設定、データ収集、インパクト評価の一連のプロセスを統合。",
    "イノベーション政策の継続的モニタリングと評価の制度化。", "イノベーション政策評価", 2005, None, "measurement,policy", "policy",
    ["OECD", "European Commission"], ["EC Better Regulation Guidelines"], "",
    "政策モニタリング,評価システム,ロジックモデル", "policy monitoring, evaluation system, logic model, KPI")

add("Innovation Policy and SDGs Alignment", "イノベーション政策とSDGsの整合",
    "イノベーション政策を国連持続可能な開発目標（SDGs）と体系的に整合させるフレームワーク。方向性のある（directed）イノベーション政策として、技術的・社会的イノベーションを持続可能性の目標に向けて誘導する。",
    "イノベーション政策と持続可能性目標の体系的整合。", "イノベーション政策", 2015, None, "policy,systemic", "policy",
    ["UNCTAD", "OECD"], ["UNCTAD Technology and Innovation Report"], "",
    "SDGs整合,持続可能性,方向性ある政策", "SDGs alignment, sustainability, directed policy, transformative innovation")

add("Systemic Innovation Policy Instruments", "システミック・イノベーション政策手段",
    "個別の市場の失敗への対処ではなく、イノベーション・システム全体の機能改善を目指す政策手段群。仲介機関の設立、ネットワーク形成支援、制度変革、能力構築等のシステミックな介入を含む。",
    "イノベーション・システム全体の機能改善を目指す政策手段。", "イノベーション政策", 2008, None, "policy,systemic", "policy,learning",
    ["Stefan Kuhlmann", "Arnold Smits"], ["Smits & Kuhlmann (2004) The Rise of Systemic Instruments"], "market failure instruments",
    "システミック政策,システム失敗,仲介機関", "systemic policy, system failure, intermediary organizations")

add("Innovation Policy Coherence", "イノベーション政策の一貫性",
    "研究政策、産業政策、教育政策、規制政策、貿易政策等の多様な政策領域間でイノベーション促進の観点から一貫性を確保するガバナンス課題。省庁間調整メカニズム、統合的戦略文書、横断的評価等の手段を活用。",
    "多政策領域間でのイノベーション促進の一貫性確保。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["OECD"], ["OECD Policy Coherence for Sustainable Development"], "",
    "政策一貫性,省庁間調整,統合戦略", "policy coherence, inter-ministerial coordination, integrated strategy")

# === SPECIFIC MEASUREMENT TOOLS AND DATABASES (581-610) ===
add("PATSTAT Patent Database", "PATSTATパテントデータベース",
    "EPOが提供する世界最大級の特許統計データベース。100以上の特許庁からの出願・登録データを統合的に収録し、大規模な特許分析研究の基盤データインフラとして広く利用される。",
    "世界規模の特許分析の基盤データインフラ。", "特許分析", 2006, None, "measurement", "learning",
    ["EPO"], ["PATSTAT User Documentation"], "",
    "PATSTAT,特許データベース,EPO", "PATSTAT, patent database, EPO, patent statistics")

add("Lens.org Patent and Scholarly Analysis", "Lens.org特許・学術分析",
    "特許データと学術論文データを統合的に検索・分析できるオープンアクセス・プラットフォーム。特許と論文の引用関係の追跡、技術-科学リンケージの分析等を無料で提供する。",
    "特許と学術論文の統合分析を無料で提供するプラットフォーム。", "特許分析", 2013, None, "measurement", "learning",
    ["Cambia", "Queensland University of Technology"], ["Lens.org Platform"], "",
    "Lens.org,統合分析,オープンアクセス", "Lens.org, integrated analysis, open access, patent-scholarly link")

add("Dimensions Database for Innovation Research", "イノベーション研究のためのDimensionsデータベース",
    "Digital Scienceが提供する学際的な研究情報プラットフォーム。論文、助成金、特許、臨床試験、政策文書をリンクし、研究のインプットからアウトプット・インパクトまでの全体像を把握するデータインフラ。",
    "研究活動の全ライフサイクルを統合するデータプラットフォーム。", "イノベーション計量学", 2018, None, "measurement", "learning",
    ["Digital Science"], ["Dimensions Platform Documentation"], "",
    "Dimensions,研究データベース,統合分析", "Dimensions, research database, integrated analysis, Digital Science")

add("OpenAlex Research Graph", "OpenAlex研究グラフ",
    "学術出版物、著者、機関、概念の大規模オープンデータセット。Microsoft Academic Graph（MAG）の後継として2022年に公開され、計量書誌学分析の無料オープンデータ基盤として急速に普及。",
    "大規模オープンな学術データ基盤として計量書誌学研究を民主化。", "計量書誌学", 2022, None, "measurement", "learning",
    ["OurResearch"], ["OpenAlex Documentation"], "",
    "OpenAlex,オープンデータ,研究グラフ", "OpenAlex, open data, research graph, bibliometric infrastructure")

add("Scopus and Web of Science Comparison", "ScopusとWeb of Scienceの比較",
    "二大学術論文索引データベース（Elsevier Scopus vs Clarivate Web of Science）のカバレッジ、品質、特徴の比較分析。データソース選択が計量書誌学的結果に与える影響を評価し、適切な使用ガイドラインを提供する。",
    "学術データベース選択の計量書誌学的影響の分析。", "計量書誌学", 2009, None, "measurement", "learning",
    ["Henk Moed", "Lutz Bornmann"], ["Mongeon & Paul-Hus (2016) The journal coverage of WoS and Scopus"], "",
    "Scopus,Web of Science,データベース比較", "Scopus, Web of Science, database comparison, coverage analysis")

add("Google Patents Analysis", "Google Patents分析",
    "Googleが提供する無料の特許検索・分析プラットフォーム。機械学習ベースの類似特許検索、先行技術調査支援等の機能を提供し、大規模特許データへのアクセスを民主化する。",
    "機械学習を活用した大規模特許データへの無料アクセス。", "特許分析", 2012, None, "measurement", "learning",
    ["Google"], ["Google Patents Platform"], "",
    "Google Patents,機械学習検索,無料特許分析", "Google Patents, ML-based search, free patent analysis")

add("CrunchBase Startup Database for Innovation", "イノベーションのためのCrunchBaseスタートアップデータベース",
    "スタートアップ、VC投資、M&A、IPO等のイノベーション・エコシステム・データを収録する大規模データベース。学術研究とスタートアップ・エコシステムの定量分析の主要データソースとして広く活用される。",
    "スタートアップ・エコシステム研究の主要データソース。", "イノベーション計量学", 2007, None, "measurement", "learning",
    ["Crunchbase"], ["Crunchbase Platform"], "",
    "CrunchBase,スタートアップデータ,VC投資", "CrunchBase, startup data, VC investment, ecosystem data")

add("OECD STIP Policy Database", "OECD STIP政策データベース",
    "OECDが運営するSTI（科学技術イノベーション）政策イニシアチブの国際データベース。各国のSTI政策措置を標準化された分類で収録し、政策比較と学習を支援する研究インフラ。",
    "STI政策の国際比較のための標準化されたデータ基盤。", "イノベーション政策評価", 2017, None, "measurement,policy", "policy,learning",
    ["OECD"], ["STIP Compass Database"], "",
    "STIP,政策データベース,国際比較", "STIP, policy database, international comparison, OECD")

add("VOSviewer Visualization Tool", "VOSviewer可視化ツール",
    "計量書誌学的マッピングとネットワーク可視化のための無料ソフトウェア。共著、共引用、キーワード共起等のネットワークを密度マップとオーバーレイ可視化で表現する。Leiden大学のvan Eck & Waltmanが開発。",
    "計量書誌学的ネットワークの直感的可視化ツール。", "計量書誌学", 2010, None, "measurement", "learning",
    ["Nees Jan van Eck", "Ludo Waltman"], ["van Eck & Waltman (2010) Software survey: VOSviewer"], "",
    "VOSviewer,ネットワーク可視化,計量書誌学ツール", "VOSviewer, network visualization, bibliometric tool, science mapping")

add("CiteSpace Visualization Platform", "CiteSpace可視化プラットフォーム",
    "科学文献のバースト検出、共引用クラスター分析、リサーチフロント可視化等の高度な計量書誌学分析機能を提供するソフトウェア。Chaomei Chenが開発し、萌芽領域の検出と知的構造の時系列変化の追跡に強み。",
    "萌芽領域検出と知的構造の動態分析に特化したツール。", "計量書誌学", 2006, None, "measurement", "learning",
    ["Chaomei Chen"], ["Chen (2006) CiteSpace II: Detecting and visualizing emerging trends"], "",
    "CiteSpace,バースト検出,リサーチフロント", "CiteSpace, burst detection, research front, trend visualization")

add("Bibliometrix R Package", "Bibliometrix Rパッケージ",
    "R言語で実装された包括的な計量書誌学分析ツール。Scopus/WoSデータの読み込み、記述統計、引用分析、共著分析、テーマ分析等の機能をワンストップで提供し、再現可能な計量書誌学分析を支援。",
    "R言語による包括的で再現可能な計量書誌学分析ツール。", "計量書誌学", 2017, None, "measurement", "learning",
    ["Massimo Aria", "Corrado Cuccurullo"], ["Aria & Cuccurullo (2017) Bibliometrix: An R-tool for comprehensive science mapping"], "",
    "Bibliometrix,Rパッケージ,再現可能分析", "Bibliometrix, R package, reproducible analysis, comprehensive tool")

# === EMERGING INNOVATION POLICY THEMES (592-620) ===
add("Generative AI Innovation Policy", "生成AIイノベーション政策",
    "大規模言語モデル等の生成AI技術の開発・利用に関する政策課題と対応。著作権問題、偽情報対策、労働市場影響、安全性評価等の規制課題とイノベーション促進の両立を図る政策設計。",
    "生成AI時代のイノベーション規制と促進の両立。", "イノベーション政策", 2023, None, "policy,institutional", "policy",
    ["OECD", "European Commission", "UK AISI"], ["EU AI Act", "UK AI Safety Institute Reports"], "",
    "生成AI政策,LLM,AI安全性", "generative AI policy, LLM, AI safety, copyright, innovation regulation")

add("Semiconductor Innovation Policy", "半導体イノベーション政策",
    "半導体（チップ）の設計・製造・パッケージングに関する国家イノベーション戦略。US CHIPS Act（2022年）、EU Chips Act（2023年）等の大規模産業政策が代表的で、サプライチェーンの地理的再配置と技術的自律性の確保を目指す。",
    "半導体サプライチェーンの戦略的再配置と技術自律性確保。", "イノベーション政策", 2022, None, "policy,institutional", "policy",
    ["US Congress", "European Commission"], ["US CHIPS and Science Act (2022)", "EU Chips Act (2023)"], "",
    "半導体政策,CHIPS Act,サプライチェーン", "semiconductor policy, CHIPS Act, supply chain, fab investment")

add("Carbon Removal Innovation Policy", "炭素除去イノベーション政策",
    "大気中のCO2を直接除去する技術（DAC、BECCS、Enhanced Weathering等）の研究開発・実証・普及を促進する政策。Frontier（Stripe等のAdvance Market Commitment）等の民間イニシアチブとUS DOE等の公的プログラムを含む。",
    "ネガティブエミッション技術のイノベーション促進。", "イノベーション政策", 2020, None, "policy", "policy",
    ["US DOE", "Frontier Climate"], ["US DOE Carbon Negative Shot"], "",
    "炭素除去,DAC,ネガティブエミッション", "carbon removal, DAC, negative emissions, BECCS, innovation policy")

add("Fusion Energy Innovation Policy", "核融合エネルギー・イノベーション政策",
    "核融合エネルギーの商業化を目指す公的・民間のイノベーション・プログラム。ITER（国際協力）に加えて、Commonwealth Fusion Systems等の民間企業への投資が急増し、政策パラダイムが変化。",
    "核融合エネルギー商業化に向けたイノベーション政策の転換。", "イノベーション政策", 2020, None, "policy", "policy",
    ["US DOE", "ITER Organization"], ["US Fusion Energy Sciences Programme"], "",
    "核融合政策,ITER,民間核融合", "fusion energy policy, ITER, private fusion, energy innovation")

add("Bioeconomy Innovation Strategy", "バイオエコノミー・イノベーション戦略",
    "バイオマス資源の持続的利用と生物学的プロセスを活用した経済活動（バイオエコノミー）のイノベーション促進戦略。EU Bioeconomy Strategy（2018年改訂）が代表的で、循環経済とバイオ技術の接合を図る。",
    "バイオマス活用経済のイノベーション促進の国家戦略。", "イノベーション政策", 2012, None, "policy,systemic", "policy",
    ["European Commission"], ["EU Bioeconomy Strategy (2018)"], "",
    "バイオエコノミー,バイオマス,循環経済", "bioeconomy, biomass, circular economy, bio-based innovation")

add("Deep Tech Innovation Policy", "ディープテック・イノベーション政策",
    "科学的発見に基づく深層技術（量子、AI、バイオ、先端材料、宇宙等）のスタートアップを支援する政策。長い開発期間、高い技術リスク、大規模資本需要等のディープテック固有の課題に対応した資金メカニズムと支援制度を設計する。",
    "科学基盤スタートアップの固有課題に対応した支援政策。", "イノベーション政策", 2019, None, "policy", "policy,learning",
    ["BCG", "Hello Tomorrow", "EIC"], ["BCG & Hello Tomorrow (2021) Deep Tech: The Great Wave"], "",
    "ディープテック,科学基盤スタートアップ,長期資金", "deep tech, science-based startup, patient capital, EIC")

add("Social Enterprise Innovation Policy", "ソーシャルエンタープライズ・イノベーション政策",
    "社会的企業（社会的課題の解決を主目的とする事業体）のイノベーション活動を促進する政策体系。法人形態の整備、社会的インパクト投資、インキュベーション、社会的インパクト測定等の制度的支援を含む。",
    "社会的企業のイノベーション活動への制度的支援。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["European Commission", "UK Government"], ["EU Social Enterprise Initiative"], "",
    "社会的企業,ソーシャルイノベーション政策", "social enterprise, social innovation policy, impact investment")

add("Technology Ethics Board", "テクノロジー倫理委員会",
    "新興技術の開発・展開における倫理的問題を審議・助言する制度的メカニズム。企業内（Google AI Ethics Board等）、国家レベル（英国AI Council等）、国際レベル（UNESCO AI Ethics）で設置される多層的なガバナンス制度。",
    "テクノロジーの倫理的ガバナンスの制度的メカニズム。", "イノベーション政策", 2015, None, "institutional,policy", "policy",
    ["UNESCO", "Various governments"], ["UNESCO Recommendation on AI Ethics (2021)"], "",
    "倫理委員会,テクノロジーガバナンス,AI倫理", "ethics board, technology governance, AI ethics, responsible innovation")

add("Innovation Policy for Circular Economy Transition", "循環経済移行のためのイノベーション政策",
    "製品設計、素材イノベーション、リサイクル技術、リマニュファクチャリング、サービス化（PaaS）等の循環経済イノベーションを促進する統合的政策枠組み。EPR（拡大生産者責任）、エコデザイン規制等の規制的手段とR&D支援を組み合わせる。",
    "循環経済移行のためのイノベーション促進の統合的政策。", "イノベーション政策", 2020, None, "policy,systemic", "policy",
    ["European Commission", "Ellen MacArthur Foundation"], ["EU New Circular Economy Action Plan (2020)"], "",
    "循環経済移行,エコデザイン,EPR", "circular economy transition, ecodesign, EPR, product-as-a-service")

add("Food System Innovation Policy", "食料システム・イノベーション政策",
    "持続可能な食料システムへの移行を促進するイノベーション政策。代替タンパク質、精密農業、食品ロス削減技術、フードテック・スタートアップ支援等を含む包括的なアプローチ。",
    "持続可能な食料システムへの移行を促進するイノベーション政策。", "イノベーション政策", 2019, None, "policy,systemic", "policy",
    ["FAO", "European Commission", "Good Food Institute"], ["EU Farm to Fork Strategy"], "",
    "食料システム,代替タンパク質,フードテック", "food system, alternative protein, food tech, sustainable agriculture")

add("Urban Innovation Policy", "都市イノベーション政策",
    "都市レベルでのイノベーション活動の促進を目的とする政策。スマートシティ技術の導入、都市リビングラボ、市民テック、イノベーション地区の形成等を通じて、都市のイノベーション・エコシステムを強化する。",
    "都市レベルのイノベーション・エコシステム強化政策。", "イノベーション政策", 2014, None, "policy,systemic", "policy,learning",
    ["Bloomberg Philanthropies", "Nesta"], ["Bloomberg Cities Initiative Reports"], "",
    "都市イノベーション,スマートシティ,市民テック", "urban innovation, smart city, civic tech, innovation district")

add("International Innovation Cooperation Framework", "国際イノベーション協力枠組み",
    "二国間・多国間のイノベーション政策協力、共同研究プログラム、標準化協力、人材交流等の制度的枠組み。EU-米国TTC（貿易技術評議会）、日EU STI協力等が代表的で、グローバルな課題への共同対応能力を強化する。",
    "国際的なイノベーション政策協力の制度化。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["European Commission", "OECD"], ["EU-US TTC Joint Statements"], "",
    "国際協力,二国間協力,共同研究", "international cooperation, bilateral cooperation, joint research, TTC")

add("Innovation Policy Sandbox", "イノベーション政策サンドボックス",
    "新しいイノベーション政策介入を小規模に実験的に導入し、効果を検証してからスケールアップする方法論。規制サンドボックスの概念をイノベーション政策全般に拡張し、政策自体のイノベーションを促進する。",
    "イノベーション政策自体の実験的テストと学習。", "イノベーション政策", 2018, None, "policy", "policy,learning",
    ["Nesta", "OECD"], ["OECD Innovation Policy Experimentation Studies"], "",
    "政策サンドボックス,政策実験,スケールアップ", "policy sandbox, policy experiment, scale-up, policy innovation")

add("Innovation Commons", "イノベーション・コモンズ",
    "オープンソース・ソフトウェア、Creative Commons、Open Hardware等の共有資源として管理されるイノベーション基盤。Ostromの共有資源管理理論をイノベーション領域に適用し、私的所有と公的所有の間の第三の選択肢を提供する。",
    "共有資源としてのイノベーション基盤の管理モデル。", "イノベーション政策", 2003, None, "institutional,policy", "policy,learning",
    ["Elinor Ostrom", "Yochai Benkler", "Lawrence Lessig"], ["Benkler (2006) The Wealth of Networks"], "proprietary innovation",
    "イノベーションコモンズ,共有資源,オープンソース", "innovation commons, shared resources, open source, Creative Commons")

add("OECD Inclusive Framework on Innovation", "OECDイノベーション包摂的枠組み",
    "先進国だけでなく新興国・途上国を含む幅広い国々がイノベーション政策の議論・設計に参加する多国間枠組み。イノベーション政策の国際的な知識共有と相互学習を制度的に促進する。",
    "グローバルなイノベーション政策対話の包摂的枠組み。", "イノベーション政策", 2015, None, "policy,institutional", "policy",
    ["OECD"], ["OECD Innovation Policy Reviews"], "",
    "包摂的枠組み,多国間協力,政策対話", "inclusive framework, multilateral cooperation, policy dialogue")

add("Anticipatory Innovation Governance", "予見的イノベーション・ガバナンス",
    "OECD OPSIが推進する、新興技術やトレンドの潜在的影響を事前に予見し、適応的なガバナンス体制を構築するアプローチ。フォーサイト、シナリオ分析、実験的手法を統合し、不確実性下での政策的機敏性を高める。",
    "不確実性下での適応的かつ予見的な政策ガバナンス。", "イノベーション政策", 2019, None, "policy,institutional", "policy,learning",
    ["OECD OPSI"], ["OECD OPSI Anticipatory Innovation Governance Reports"], "",
    "予見的ガバナンス,OPSI,適応的政策", "anticipatory governance, OPSI, adaptive policy, emerging technologies")

# === FINAL ENTRIES TO 714 (608-714) - expanded topics ===
add("Collaborative Innovation Networks (COINs)", "協調的イノベーション・ネットワーク",
    "共通のビジョンに基づいて自発的に形成される革新的な協働ネットワーク。Peter Gloorが概念化し、Webマイニングやソーシャルネットワーク分析を用いてCOINsの構造と創造性の関係を定量的に分析する方法論を確立。",
    "自発的協働ネットワークの創造性分析手法。", "イノベーション計量学", 2004, None, "measurement,systemic", "learning",
    ["Peter Gloor"], ["Gloor (2006) Swarm Creativity"], "",
    "COINs,協調ネットワーク,集合的創造性", "COINs, collaborative innovation network, swarm creativity")

add("Innovation Policy Theory of Change", "イノベーション政策のセオリー・オブ・チェンジ",
    "イノベーション政策介入がどのような因果メカニズムを通じて期待される成果に至るかを事前に明示するフレームワーク。政策設計の論理的一貫性を検証し、適切な評価指標の設定を支援するツール。",
    "政策介入の因果メカニズムの事前的明示と検証。", "イノベーション政策評価", 2010, None, "policy,measurement", "policy,learning",
    ["Carol Weiss", "European Commission"], ["EC Better Regulation Toolbox"], "",
    "セオリーオブチェンジ,政策ロジック,因果メカニズム", "theory of change, policy logic, causal mechanism, intervention design")

add("Innovation Policy Cost-Benefit Analysis", "イノベーション政策の費用便益分析",
    "イノベーション政策介入の社会的費用と便益を貨幣換算して比較する評価手法。R&Dの社会的収益率推計、スピルオーバー効果の定量化、動態的効率性への影響評価等を含む。",
    "イノベーション政策介入の社会的厚生効果の評価。", "イノベーション政策評価", 2000, None, "measurement,policy", "policy,learning",
    ["Bronwyn Hall", "Jacques Mairesse"], ["Hall, Mairesse & Mohnen (2010) Measuring the Returns to R&D"], "",
    "費用便益分析,社会的収益率,スピルオーバー", "cost-benefit analysis, social rate of return, spillover, welfare effect")

add("Innovation Diplomacy Networks", "イノベーション外交ネットワーク",
    "各国のイノベーション・アタッシェ、科学技術外交官、海外イノベーション拠点等のネットワークを通じた国際的なイノベーション・インテリジェンスの収集と二国間イノベーション協力の促進。",
    "イノベーション外交の制度的ネットワーク構築。", "イノベーション政策", 2015, None, "policy,institutional", "policy",
    ["Various national governments"], ["OECD Innovation Diplomacy Studies"], "",
    "イノベーション外交ネットワーク,科学アタッシェ", "innovation diplomacy network, science attaché, bilateral cooperation")

add("Innovation-Friendly Regulation", "イノベーション促進的規制",
    "規制がイノベーションを阻害するのではなく促進する方向で設計される規制アプローチ。パフォーマンスベースの規制、技術中立的な基準設定、定期的な規制レビュー、規制サンドボックス等の原則を体系化する。",
    "規制設計におけるイノベーション促進原則の体系化。", "イノベーション政策", 2015, None, "policy,institutional", "policy",
    ["OECD", "European Commission"], ["OECD Regulatory Policy and Innovation"], "",
    "イノベーション促進的規制,パフォーマンス規制", "innovation-friendly regulation, performance-based regulation, regulatory review")

add("Green Patent Classification", "グリーン特許分類",
    "環境関連技術の特許を体系的に識別・分類するためのタグ付けシステム。EPOのY02分類（気候変動緩和技術）やWIPOの IPC Green Inventoryが代表的で、環境イノベーションの定量的追跡を可能にする。",
    "環境技術特許の体系的識別と追跡。", "特許分析", 2010, None, "measurement", "learning",
    ["EPO", "WIPO"], ["EPO Y02 Classification", "WIPO IPC Green Inventory"], "",
    "グリーン特許,環境技術分類,Y02", "green patent, environmental technology classification, Y02, IPC Green")

add("Innovation Accounting Standards Board", "イノベーション会計基準",
    "無形資産（R&D、特許、ブランド、人的資本等）の会計処理に関する国際基準。IFRS/IASにおけるR&D支出の費用化vs資産化の基準が、企業のイノベーション投資のインセンティブと財務報告に影響する。",
    "無形資産会計がイノベーション投資に与える影響。", "イノベーション計量学", 1998, None, "measurement,institutional", "policy,learning",
    ["IASB", "FASB"], ["IAS 38 Intangible Assets", "IFRS Standards"], "",
    "無形資産会計,IAS 38,R&D会計", "intangible asset accounting, IAS 38, R&D accounting, IFRS")

add("Innovation Insurance and Risk Management", "イノベーション保険とリスク管理",
    "イノベーション・プロジェクトに固有のリスク（技術リスク、市場リスク、知財リスク等）を保険やリスク管理手法で軽減する制度的メカニズム。特許保険、R&Dプロジェクト保険等の金融商品を含む。",
    "イノベーション固有のリスクに対する金融的軽減メカニズム。", "イノベーション政策", 2010, None, "policy", "policy",
    ["Swiss Re", "Lloyd's"], ["IP Insurance Market Studies"], "",
    "イノベーション保険,リスク管理,知財保険", "innovation insurance, risk management, IP insurance, technology risk")

add("Innovation Metrics for Boards of Directors", "取締役会向けイノベーション指標",
    "企業の取締役会がイノベーション活動を監督・評価するために用いる指標体系。イノベーション・パイプライン指標、R&D効率指標、新製品収益比率、イノベーション文化指標等をダッシュボード形式で提供する。",
    "企業ガバナンスにおけるイノベーション監督のための指標体系。", "イノベーション計量学", 2015, None, "measurement", "learning",
    ["McKinsey", "BCG"], ["BCG Most Innovative Companies Report Methodology"], "",
    "取締役会指標,イノベーションダッシュボード,企業ガバナンス", "board metrics, innovation dashboard, corporate governance")

add("Innovation Policy Diffusion Across Countries", "イノベーション政策の国際的拡散",
    "特定のイノベーション政策手段（R&D税制、イノベーション・バウチャー、規制サンドボックス等）が国際的に拡散するパターン、メカニズム、条件の分析。政策移転、政策学習、模倣のダイナミクスを解明する。",
    "イノベーション政策手段の国際的拡散メカニズムの分析。", "イノベーション政策", 2010, None, "policy", "policy,learning",
    ["Fabrizio Gilardi", "OECD"], ["Gilardi (2010) Who Learns from What in Policy Diffusion Processes"], "",
    "政策拡散,政策移転,国際的模倣", "policy diffusion, policy transfer, international emulation")

add("Outcome-Based Innovation Procurement", "成果ベース・イノベーション調達",
    "調達仕様を技術的手段ではなく達成すべき成果（アウトカム）で定義するイノベーション調達手法。供給者の創造的な解決策提案を促し、イノベーティブなソリューションの調達可能性を高める。",
    "成果定義による調達のイノベーション促進効果。", "イノベーション政策", 2012, None, "policy", "policy",
    ["European Commission", "UK Government"], ["EC Guidance on Innovation Procurement"], "",
    "成果ベース調達,機能仕様,イノベーション調達", "outcome-based procurement, functional specification, innovation procurement")

add("Counterfactual Analysis for R&D Policy", "R&D政策の反事実分析",
    "R&D補助金の受給企業と類似の非受給企業を比較する傾向スコアマッチング、差の差分析等の手法でR&D政策の因果的効果を推定する計量分析方法論。追加性（additionality）とクラウディングアウトの識別が中心課題。",
    "R&D政策の因果的効果の厳密な推定方法論。", "イノベーション政策評価", 2005, None, "measurement,policy", "policy,learning",
    ["David Czarnitzki", "Cindy Lopes-Bento"], ["Czarnitzki & Lopes-Bento (2014) Innovation Subsidies"], "",
    "反事実分析,PSM,差の差,追加性", "counterfactual analysis, PSM, DID, additionality, R&D subsidy")

add("Innovation Radar for Social Innovation", "ソーシャルイノベーションのためのイノベーション・レーダー",
    "社会的イノベーションの動向を体系的にスキャン・分類・追跡するツール。新しい社会的実践、組織モデル、政策イノベーション等を多次元で把握し、社会変革のトレンドを可視化する。",
    "社会的イノベーションの体系的スキャンと追跡ツール。", "イノベーション計量学", 2015, None, "measurement,policy", "policy,learning",
    ["European Commission", "Nesta"], ["EU Social Innovation Monitor"], "",
    "ソーシャルイノベーションレーダー,社会変革トレンド", "social innovation radar, social change trends, innovation tracking")

add("Innovation Culture Index", "イノベーション文化指標",
    "組織や国のイノベーション文化（リスク許容度、失敗への寛容性、実験的精神、多様性の尊重等）を定量化する指標体系。CIS等のイノベーション調査の組織文化モジュールや独自の文化調査が方法論的基盤。",
    "イノベーションを育む文化的要素の定量化。", "イノベーション計量学", 2010, None, "measurement", "learning",
    ["INSEAD", "Global Entrepreneurship Monitor"], ["GEM Entrepreneurial Culture Indicators"], "",
    "イノベーション文化,リスク許容,起業家精神", "innovation culture, risk tolerance, entrepreneurial spirit, cultural index")

add("Innovation Talent Attraction Index", "イノベーション人材誘引指標",
    "国や都市が革新的人材（研究者、エンジニア、起業家等）を引きつける能力を測定する指標。研究環境、給与水準、生活品質、ビザ政策、起業環境等の多次元で人材誘引力を評価する。",
    "革新的人材の誘引能力の多次元的評価。", "イノベーション計量学", 2012, None, "measurement,policy", "policy,learning",
    ["OECD", "INSEAD"], ["INSEAD Global Talent Competitiveness Index"], "",
    "人材誘引,グローバル人材競争,ビザ政策", "talent attraction, global talent competition, visa policy, brain gain")

add("Innovation Space Utilization Metrics", "イノベーション空間利用指標",
    "コワーキングスペース、インキュベーター、アクセラレーター、メイカースペース、リビングラボ等のイノベーション支援空間の利用率、成果、ネットワーキング効果を測定する指標体系。",
    "イノベーション支援空間の利用と成果の定量的評価。", "イノベーション計量学", 2014, None, "measurement", "learning",
    ["NBIA", "GEN"], ["Global Accelerator Report"], "",
    "イノベーション空間,コワーキング,インキュベーター", "innovation space, coworking, incubator, accelerator, maker space")

add("Knowledge Economy Governance Index", "知識経済ガバナンス指標",
    "知識経済の効果的運営に必要なガバナンス制度（知財保護、研究資金配分、教育制度、データ政策、競争政策等）の質を総合的に評価する複合指標。制度的環境がイノベーション・パフォーマンスに与える影響を間接的に測定する。",
    "知識経済を支えるガバナンス制度の質の総合評価。", "イノベーション計量学", 2008, None, "measurement,policy", "policy",
    ["World Bank", "OECD"], ["World Bank Knowledge Economy Indicators"], "",
    "知識経済ガバナンス,制度の質,ガバナンス指標", "knowledge economy governance, institutional quality, governance index")

add("Open Innovation Ecosystem Metrics", "オープンイノベーション・エコシステム指標",
    "企業、大学、スタートアップ、政府機関等の多様なアクター間のオープンイノベーション活動の量、質、構造を測定する指標群。共同特許率、産学連携論文率、技術ライセンシング率、共同R&Dプロジェクト参加率等を含む。",
    "オープンイノベーション・エコシステムの多次元的測定。", "イノベーション計量学", 2010, None, "measurement,systemic", "learning",
    ["Henry Chesbrough", "Marcel Bogers"], ["Chesbrough & Bogers (2014) Explicating Open Innovation"], "",
    "オープンイノベーション指標,協業測定,エコシステム", "open innovation metrics, collaboration measurement, ecosystem")

add("Venture Studio Model", "ベンチャースタジオモデル",
    "スタートアップを連続的に創業するスタジオ型の起業プラットフォーム。共有リソース、体系化された検証プロセス、シリアルアントレプレナーのノウハウを組織化し、スタートアップの成功確率を高める組織モデル。",
    "スタートアップの連続的創業を組織化するモデル。", "イノベーション政策", 2015, None, "institutional", "learning",
    ["Idealab", "Rocket Internet"], ["GSSN Global Startup Studio Network Reports"], "",
    "ベンチャースタジオ,スタートアップファクトリー", "venture studio, startup factory, serial entrepreneurship, platform model")

add("Innovation Policy Intelligence Platform", "イノベーション政策インテリジェンス・プラットフォーム",
    "各国のイノベーション政策の動向、成果、ベストプラクティスを体系的に収集・分析・共有するデジタルプラットフォーム。AI・NLPを活用した政策文書の自動分析と構造化された比較分析を提供する。",
    "イノベーション政策の国際的な知識管理・共有基盤。", "イノベーション政策", 2020, None, "measurement,policy", "policy,learning",
    ["OECD", "European Commission"], ["OECD STIP Compass", "EU Policy Intelligence Tools"], "",
    "政策インテリジェンス,自動分析,知識共有", "policy intelligence, automated analysis, knowledge sharing, digital platform")

add("Innovation Pathway Analysis", "イノベーション経路分析",
    "特定のイノベーション成果に至るまでの技術的・制度的・市場的経路を体系的に追跡・分析する手法。ケーススタディ、パテントフロー分析、技術系譜分析を組み合わせ、イノベーションの因果構造を解明する。",
    "イノベーション成果に至る因果経路の体系的追跡。", "イノベーション計量学", 2010, None, "measurement", "learning",
    ["William Bonvillian"], ["Bonvillian (2018) Advanced Manufacturing"], "",
    "経路分析,技術系譜,因果構造", "pathway analysis, technology genealogy, causal structure")

add("Patent Assertion Entity (PAE) Analysis", "パテント・アサーション・エンティティ分析",
    "特許を実施せず他者への権利行使（訴訟・ライセンス要求）のみを行う主体（PAE/パテント・トロール）の活動パターン、経済的影響、政策的対応を分析する研究領域。特許制度のイノベーション阻害側面の実証。",
    "パテント・トロールのイノベーション阻害効果の分析。", "特許分析", 2010, None, "measurement,institutional", "policy,learning",
    ["James Bessen", "Michael Meurer"], ["Bessen & Meurer (2014) The Direct Costs from NPE Disputes"], "",
    "PAE,パテントトロール,特許訴訟", "PAE, patent troll, patent litigation, non-practicing entity")

add("Innovation Corridor Analysis", "イノベーション回廊分析",
    "都市間・地域間を結ぶイノベーション活動の空間的連結パターン（イノベーション回廊）を分析する手法。共同特許、共著論文、人材流動、VC投資フロー等のデータから回廊構造を可視化し、地域連携政策に活用する。",
    "地域間イノベーション連結の空間的パターン分析。", "イノベーション計量学", 2012, None, "measurement,systemic", "learning",
    ["Olav Sorenson", "Michael Storper"], ["Storper & Venables (2004) Buzz: Face-to-Face Contact"], "",
    "イノベーション回廊,地域間連結,空間的パターン", "innovation corridor, inter-regional linkage, spatial pattern, knowledge flow")

add("Future-Oriented Technology Analysis (FTA)", "将来志向型技術分析",
    "技術フォーサイト、技術評価、技術ロードマッピング等の将来志向型手法群を統合する包括的概念。Alan Porterが提唱し、テキストマイニング、特許分析、シナリオ手法等を組み合わせて技術の将来動向を分析する。",
    "将来志向型技術分析手法群の統合的概念。", "技術フォーサイト", 2004, None, "measurement,policy", "policy,learning",
    ["Alan Porter", "Jan Youtie"], ["Porter et al. (2004) Technology futures analysis"], "",
    "FTA,将来志向型分析,技術予測統合", "FTA, future-oriented technology analysis, tech mining, integrated foresight")

add("Emerging Technology Detection Methods", "新興技術検出手法",
    "萌芽段階にある新技術を早期に検出する定量的手法群。特許の急増パターン（バースト検出）、学術論文のクラスター形成、キーワード出現頻度の加速等の指標を用いて技術の創発を識別する。",
    "萌芽的技術の早期検出のための定量的手法群。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Jon Kleinberg", "Alan Porter"], ["Kleinberg (2003) Bursty and Hierarchical Structure in Streams"], "",
    "新興技術検出,バースト検出,早期警戒", "emerging technology detection, burst detection, early warning, weak signals")

add("Innovation Pipeline Metrics", "イノベーション・パイプライン指標",
    "企業のイノベーション・プロジェクトのポートフォリオを、アイデア段階から商業化までの各フェーズでの進捗・成功率・資源配分を追跡する指標群。ステージゲートプロセスの各段階のスループットと品質を定量化する。",
    "イノベーション・プロジェクト・ポートフォリオの進捗管理指標。", "イノベーション計量学", 2000, None, "measurement", "learning",
    ["Robert Cooper"], ["Cooper (2011) Winning at New Products"], "",
    "パイプライン指標,ステージゲート,ポートフォリオ管理", "pipeline metrics, stage-gate, portfolio management, throughput")

add("Competitive Intelligence for Innovation", "イノベーションのための競合インテリジェンス",
    "競合企業の技術戦略、特許活動、R&D投資、人材動向等を体系的にモニタリング・分析する手法。特許監視、論文分析、求人データ分析、製品リバースエンジニアリング等のツールを統合的に活用する。",
    "競合の技術・イノベーション活動の体系的モニタリング。", "イノベーション計量学", 1990, None, "measurement", "learning",
    ["Leonard Fuld", "Ben Gilad"], ["Fuld (2006) The Secret Language of Competitive Intelligence"], "",
    "競合インテリジェンス,技術監視,特許モニタリング", "competitive intelligence, technology monitoring, patent surveillance")

add("Innovation Capability Assessment Tool (ICAT)", "イノベーション能力評価ツール",
    "UNCTAD等が途上国向けに開発した、国レベルのイノベーション能力を評価するためのツール。STI政策の有効性、制度的枠組み、人材基盤、インフラ、企業能力等の次元でイノベーション能力の現状と改善方向を診断する。",
    "途上国向けのイノベーション能力の包括的診断ツール。", "イノベーション計量学", 2010, None, "measurement,policy", "policy,learning",
    ["UNCTAD"], ["UNCTAD Technology and Innovation Report"], "",
    "能力評価ツール,途上国,イノベーション診断", "capability assessment, developing countries, innovation diagnosis, UNCTAD")

add("Regional Innovation Strategy (RIS3) Monitoring", "地域イノベーション戦略（RIS3）モニタリング",
    "EUのスマート専門化戦略の実施状況をモニタリングするための指標体系とプロセス。EDP（起業家的発見プロセス）の活動度、戦略的優先分野への投資集中度、成果指標等を継続的に追跡する。",
    "スマート専門化戦略の実施モニタリング。", "イノベーション政策評価", 2014, None, "measurement,policy", "policy",
    ["European Commission", "JRC"], ["JRC S3 Platform Monitoring Reports"], "",
    "RIS3モニタリング,スマート専門化追跡", "RIS3 monitoring, smart specialisation tracking, EDP assessment")

# Save to JSON files
output_dir = os.path.dirname(os.path.abspath(__file__))
total = len(entries)
print(f"Total entries generated (batch 3): {total}")

for batch_idx in range(0, total, 50):
    batch = entries[batch_idx:batch_idx+50]
    batch_num = batch_idx // 50 + 7  # Continue from batch 7
    filepath = os.path.join(output_dir, f"pol_batch_{batch_num}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)
    print(f"Written {len(batch)} entries to {filepath} (IDs: {batch[0]['id']} - {batch[-1]['id']})")

print(f"\nAll pol entries: 146 + 106 + {total} = {146 + 106 + total} (need 414)")
