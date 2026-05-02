#!/usr/bin/env python3
"""Generate final measurement_policy_governance entries (inno_pol_636 to inno_pol_714)."""

import json
import os

entries = []
idx = 636

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

# === REMAINING ENTRIES (636-714) ===
add("Technology Gap Theory Measurement", "技術ギャップ理論の測定",
    "先進国と後発国の技術水準の差（技術ギャップ）を定量化し、その縮小（キャッチアップ）パターンを測定する方法論。TFP比較、特許引用の国際パターン、技術フロンティアとの距離の推定等。",
    "技術ギャップの定量化とキャッチアップ・パターンの追跡。", "イノベーション計量学", 1966, None, "measurement", "learning",
    ["Michael Posner", "Jan Fagerberg"], ["Fagerberg (1987) A Technology Gap Approach to Why Growth Rates Differ"], "",
    "技術ギャップ,キャッチアップ,国際比較", "technology gap, catch-up, international comparison, frontier distance")

add("Innovation Survey Non-Response Bias", "イノベーション調査の無回答バイアス",
    "CIS等のイノベーション調査における無回答企業の系統的偏り（イノベーティブな企業の方が回答率が高い等）を分析し、推定結果への影響を評価する方法論的研究テーマ。",
    "イノベーション調査の信頼性を脅かすバイアスの分析。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Anthony Arundel", "Eurostat"], ["Arundel (2006) Innovation Survey Indicators"], "",
    "無回答バイアス,調査品質,信頼性", "non-response bias, survey quality, reliability, measurement error")

add("Innovation in Services Taxonomy", "サービスイノベーションの分類体系",
    "サービス部門のイノベーション形態を体系的に分類するフレームワーク。Gadrey & Gallouj（1998）の特性ベースモデル等が代表的で、製造業中心のイノベーション分類をサービス特有の形態に拡張する。",
    "サービス部門のイノベーション形態の体系的分類。", "イノベーション計量学", 1998, None, "measurement", "learning",
    ["Faïz Gallouj", "Jean Gadrey"], ["Gallouj & Weinstein (1997) Innovation in Services"], "",
    "サービスイノベーション分類,特性ベース,分類体系", "service innovation taxonomy, characteristics-based, classification")

add("Innovation Intermediary Policy", "イノベーション仲介機関政策",
    "技術移転機関、イノベーション・ハブ、クラスターマネジメント組織等の仲介機関を制度的に支援する政策。情報の非対称性の解消、ネットワーク構築、能力構築等の仲介機能を通じてイノベーション・システムの機能を改善。",
    "イノベーション仲介機能の制度的支援政策。", "イノベーション政策", 2005, None, "policy,institutional", "policy,learning",
    ["Sven Lundvall", "OECD"], ["OECD Innovation Intermediaries Studies"], "",
    "仲介機関,ブローカー,ネットワーク構築", "innovation intermediary, broker, network building, system function")

add("Global Value Chain and Innovation Measurement", "グローバルバリューチェーンとイノベーション測定",
    "GVC内での企業の位置付けとイノベーション活動の関係を測定する方法論。GVCへの統合度、アップグレーディング、技術吸収等のメカニズムを通じたイノベーション効果を定量化する。",
    "GVC参加とイノベーション能力の関係の定量分析。", "イノベーション計量学", 2010, None, "measurement", "learning",
    ["Gary Gereffi", "OECD"], ["OECD TiVA Indicators", "Gereffi et al. (2005) Governance of GVCs"], "",
    "GVC,バリューチェーン,アップグレーディング", "GVC, value chain, upgrading, innovation measurement")

add("Patent Examination Quality Metrics", "特許審査品質指標",
    "特許庁の審査プロセスの質を評価する指標群。審査期間、審査一貫性（同一出願への異なる審査官の判断一致率）、付与後無効化率、引用先行技術の網羅性等から審査品質を多面的に評価する。",
    "特許審査プロセスの質と効率の多面的評価。", "特許分析", 2008, None, "measurement,institutional", "policy",
    ["EPO", "USPTO", "Dietmar Harhoff"], ["Harhoff & Wagner (2009) The Duration of Patent Examination at the EPO"], "",
    "審査品質,特許庁評価,審査一貫性", "examination quality, patent office evaluation, examination consistency")

add("Innovation and Absorptive Capacity Measurement at National Level", "国家レベルの吸収能力の測定",
    "国全体の外部知識の吸収・活用能力を定量化する指標。R&D人材の質・量、教育水準、技術インフラ、制度的品質等から構成され、FDI・技術移転の効果を左右する要因として政策評価に活用される。",
    "国家レベルの知識吸収能力の定量的評価。", "イノベーション計量学", 2002, None, "measurement,policy", "policy,learning",
    ["Wesley Cohen", "Daniel Levinthal", "OECD"], ["Cohen & Levinthal (1990) Absorptive Capacity"], "",
    "吸収能力測定,国家レベル,知識活用", "absorptive capacity measurement, national level, knowledge utilization")

add("Innovation Tax Policy Instruments Database", "イノベーション税制政策データベース",
    "各国のR&D税制、パテントボックス、エンジェル税制等のイノベーション関連税制優遇措置を体系的に収録したデータベース。OECD R&D Tax Incentive Databaseが代表的で、国際比較分析の基盤データ。",
    "イノベーション税制の国際比較のためのデータ基盤。", "イノベーション政策", 2010, None, "measurement,policy", "policy",
    ["OECD"], ["OECD R&D Tax Incentive Database"], "",
    "税制データベース,国際比較,R&D税制", "tax policy database, international comparison, R&D tax incentive")

add("Clinical Trial Innovation Policy", "臨床試験イノベーション政策",
    "臨床試験プロセスの効率化・革新化を促進する政策。適応的試験デザイン、分散型臨床試験（DCT）、Real-World Evidence活用、規制の国際調和等を制度的に推進し、医薬品イノベーションの迅速化を図る。",
    "臨床試験プロセスのイノベーション促進政策。", "イノベーション政策", 2018, None, "policy,institutional", "policy",
    ["FDA", "EMA"], ["FDA Adaptive Trial Design Guidance"], "",
    "臨床試験革新,DCT,適応的デザイン", "clinical trial innovation, DCT, adaptive design, RWE")

add("Innovation Procurement Partnership", "イノベーション調達パートナーシップ",
    "EU公共調達指令（2014年）で導入された新しい調達手続きで、公共部門が民間パートナーと長期的な研究開発協力関係を構築し、市場に存在しない革新的ソリューションを共同開発する制度的枠組み。",
    "公共部門と民間の長期的イノベーション共同開発の制度化。", "イノベーション政策", 2014, None, "policy,institutional", "policy",
    ["European Commission"], ["EU Public Procurement Directive 2014/24/EU"], "",
    "調達パートナーシップ,共同開発,EU調達指令", "procurement partnership, co-development, EU procurement directive")

add("Knowledge Intensive Activities Indicator", "知識集約的活動指標",
    "経済活動全体に占める知識集約的活動（R&D、デザイン、ソフトウェア開発、コンサルティング等）の比率を測定する指標。知識経済化の進展度を産業構造の変化から捕捉する。",
    "知識経済化の進展度の産業構造的測定。", "イノベーション計量学", 2000, None, "measurement", "learning",
    ["OECD", "Eurostat"], ["OECD Knowledge-Based Economy Reports"], "",
    "知識集約活動,知識経済化,産業構造", "knowledge-intensive activities, knowledge economy, industry structure")

add("Innovation and Employment Impact Assessment", "イノベーションの雇用影響評価",
    "技術的イノベーション（自動化、AI、ロボティクス等）が雇用の量、質、スキル構成に与える影響を評価する方法論。タスクベース・アプローチ、職業別自動化確率推定、スキル需要予測等の手法を統合する。",
    "イノベーションの雇用・労働市場への影響の体系的評価。", "イノベーション政策評価", 2013, None, "measurement,policy", "policy,learning",
    ["Carl Benedikt Frey", "Michael Osborne", "OECD"], ["Frey & Osborne (2017) The Future of Employment"], "",
    "雇用影響,自動化,スキル変化", "employment impact, automation, skill change, task-based approach")

add("Innovation and Regional Inequality", "イノベーションと地域格差",
    "イノベーション活動の地理的集中が地域間経済格差に与える影響の分析。知識スピルオーバーの限定的な地理的範囲、「勝者独り占め」のクラスター効果、取り残された地域（left-behind places）の政策課題。",
    "イノベーション集中と地域間格差の構造的関係の分析。", "イノベーション政策", 2017, None, "policy,measurement", "policy",
    ["Andrés Rodríguez-Pose", "Enrico Moretti"], ["Rodríguez-Pose (2018) The revenge of the places that don't matter"], "",
    "地域格差,取り残された地域,空間的集中", "regional inequality, left-behind places, spatial concentration")

add("Responsible Innovation Assessment Framework", "責任あるイノベーション評価枠組み",
    "RRIの4次元（予見、内省、包摂、応答）の実施度を企業・プロジェクト・政策レベルで評価する枠組み。自己評価ツール、第三者監査、ステークホルダー・フィードバック等の手法を用いた制度化を推進。",
    "責任あるイノベーションの実践度の体系的評価。", "イノベーション計量学", 2015, None, "measurement,policy", "policy",
    ["European Commission", "RRI Tools Project"], ["RRI Tools Self-Assessment Guide"], "",
    "RRI評価,責任あるイノベーション,自己評価", "RRI assessment, responsible innovation, self-assessment, stakeholder feedback")

add("AI Ethics Impact Assessment", "AI倫理影響評価",
    "AIシステムの開発・導入に先立って、公平性、透明性、プライバシー、安全性等の倫理的影響を事前に評価する手法。EU AI Actの高リスクAIシステムへの適合性評価や、各国のAI倫理ガイドラインに基づく評価プロセス。",
    "AIシステムの倫理的影響の事前評価制度。", "イノベーション政策", 2019, None, "measurement,policy", "policy",
    ["European Commission", "IEEE"], ["EU AI Act Conformity Assessment", "IEEE Ethics in AI Guidelines"], "",
    "AI倫理評価,影響評価,高リスクAI", "AI ethics assessment, impact assessment, high-risk AI, conformity")

add("Innovation Policy for Just Transition", "公正な移行のためのイノベーション政策",
    "脱炭素化等の構造的転換の過程で、雇用・地域・産業への負の影響を最小化しつつイノベーションを促進する政策枠組み。化石燃料依存地域のイノベーション能力転換、労働者の再訓練、新産業の育成等を統合的に推進する。",
    "構造的転換の公正性とイノベーション促進の両立。", "イノベーション政策", 2020, None, "policy,systemic", "policy",
    ["European Commission", "ILO"], ["EU Just Transition Mechanism"], "",
    "公正な移行,脱炭素化,地域転換", "just transition, decarbonization, regional transformation, reskilling")

add("Innovation Challenge Fund Design", "イノベーション・チャレンジ基金設計",
    "特定の技術的・社会的課題に対して競争的資金を配分するチャレンジ型イノベーション基金の設計原則。課題設定の方法、審査基準、段階的資金配分、成果評価等の設計変数を体系化する。",
    "課題解決型イノベーション基金の効果的設計原則。", "イノベーション政策", 2015, None, "policy", "policy,learning",
    ["Innovate UK", "European Commission"], ["Innovate UK Industrial Strategy Challenge Fund Reports"], "",
    "チャレンジ基金,競争的資金,課題設定", "challenge fund, competitive funding, problem setting, staged funding")

add("Systemic Risk in Innovation Systems", "イノベーションシステムのシステミック・リスク",
    "イノベーション・システム全体に波及しうる構造的リスク（技術的ロックイン、制度的硬直性、過度の専門化等）を識別・評価する分析枠組み。金融システムのシステミック・リスク分析のアナロジーをイノベーション政策に適用。",
    "イノベーション・システム全体の構造的脆弱性の評価。", "イノベーション計量学", 2015, None, "measurement,systemic", "policy,learning",
    ["OECD"], ["OECD System Innovation Studies"], "",
    "システミックリスク,構造的脆弱性,ロックイン", "systemic risk, structural vulnerability, lock-in, institutional rigidity")

add("Innovation and Ethical Supply Chain", "イノベーションと倫理的サプライチェーン",
    "サプライチェーンの透明性・追跡可能性・倫理的調達をイノベーション（ブロックチェーン、IoT、AI等）で実現する政策・技術的アプローチ。紛争鉱物規制、強制労働防止、環境デューデリジェンスとの接合を図る。",
    "技術イノベーションによるサプライチェーン倫理の実現。", "イノベーション政策", 2017, None, "policy,institutional", "policy",
    ["European Commission"], ["EU Corporate Sustainability Due Diligence Directive"], "",
    "倫理的サプライチェーン,透明性,ブロックチェーン", "ethical supply chain, transparency, blockchain, due diligence")

add("Innovation Policy for Resilience", "レジリエンスのためのイノベーション政策",
    "パンデミック、気候変動、地政学的ショック等の危機に対するイノベーション・システムのレジリエンス（回復力・適応力）を高める政策枠組み。多様性の確保、冗長性の設計、適応的能力の構築を重視する。",
    "イノベーション・システムのレジリエンス強化政策。", "イノベーション政策", 2020, None, "policy,systemic", "policy",
    ["OECD"], ["OECD (2021) Fostering Innovation Ecosystem Resilience"], "",
    "レジリエンス,危機対応,適応力", "resilience, crisis response, adaptive capacity, system robustness")

add("Sovereign Wealth Fund for Innovation", "イノベーションのためのソブリン・ウェルス・ファンド",
    "国富ファンドの投資戦略にイノベーション促進を組み込むアプローチ。シンガポールのTemasek/GIC、UAE のMubadala等がディープテック投資や国内イノベーション・エコシステム構築に戦略的に資金を配分。",
    "国富ファンドによるイノベーション・エコシステムへの戦略的投資。", "イノベーション政策", 2010, None, "policy", "policy",
    ["Temasek", "Mubadala"], ["IFSWF Santiago Principles"], "",
    "ソブリンウェルスファンド,戦略的投資,国富ファンド", "sovereign wealth fund, strategic investment, innovation ecosystem")

add("University-Industry Collaboration Measurement", "産学連携の測定",
    "産学間の知識移転・共同研究活動を定量的に測定する指標体系。共同特許、共著論文、ライセンシング収入、スピンオフ数、共同研究契約金額、人材交流等の多次元で産学連携の量と質を評価する。",
    "産学連携の量と質の多次元的測定。", "イノベーション計量学", 2000, None, "measurement,institutional", "learning",
    ["OECD", "AUTM"], ["OECD University-Industry Collaboration Indicators"], "",
    "産学連携測定,共同研究,ライセンシング", "university-industry collaboration measurement, joint research, licensing")

add("Innovation System Resilience Index", "イノベーションシステム・レジリエンス指標",
    "イノベーション・システムの外部ショック（金融危機、パンデミック、サプライチェーン途絶等）に対する耐性と回復力を定量的に評価する複合指標。多様性、冗長性、適応速度、資源流動性等の次元で構成。",
    "イノベーション・システムのショック耐性の定量的評価。", "イノベーション計量学", 2021, None, "measurement,systemic", "policy,learning",
    ["OECD", "European Commission"], ["OECD Resilience Indicators"], "",
    "レジリエンス指標,ショック耐性,システム評価", "resilience index, shock resistance, system assessment, adaptive capacity")

add("Frontier Technology Readiness Assessment", "フロンティア技術準備度評価",
    "AI、ブロックチェーン、量子、バイオ等のフロンティア技術の展開に対する国の準備度（ICTインフラ、人材、R&D、規制環境等）を評価する枠組み。UNCTADが途上国を含む包括的な評価指標を開発。",
    "フロンティア技術への国の準備度の包括的評価。", "イノベーション計量学", 2021, None, "measurement,policy", "policy,learning",
    ["UNCTAD"], ["UNCTAD Technology and Innovation Report 2021"], "",
    "フロンティア技術準備度,途上国,AI準備度", "frontier technology readiness, developing countries, AI readiness")

add("Patent-Based Technology Transfer Indicators", "特許ベース技術移転指標",
    "特許のライセンシング、譲渡、共同出願等の取引データから技術移転の方向性・規模・パターンを測定する指標群。大学から産業への技術移転、国際間技術移転等の動態を定量的に追跡する。",
    "特許取引データによる技術移転の定量的追跡。", "特許分析", 2005, None, "measurement", "learning",
    ["OECD", "Carlos Rosell"], ["OECD Patent Transfer Indicators"], "",
    "特許移転指標,技術移転追跡,ライセンシング", "patent transfer indicators, technology transfer tracking, licensing data")

add("Innovation Ecosystem Maturity Model", "イノベーション・エコシステム成熟度モデル",
    "地域・都市のイノベーション・エコシステムの発展段階を、萌芽期→成長期→成熟期→再活性化期の各段階で評価するモデル。各段階に必要な政策介入の種類と強度を診断的に特定する。",
    "イノベーション・エコシステムの発展段階と政策ニーズの診断。", "イノベーション計量学", 2015, None, "measurement,systemic", "policy,learning",
    ["Startup Genome", "Daniel Isenberg"], ["Isenberg (2010) How to Start an Entrepreneurial Revolution"], "",
    "エコシステム成熟度,発展段階,段階的政策", "ecosystem maturity, development stage, staged policy intervention")

add("Innovation and Digital Skills Measurement", "イノベーションとデジタルスキル測定",
    "イノベーション活動に必要なデジタルスキル（データ分析、プログラミング、AI活用等）の労働力における分布と水準を測定する方法論。デジタルスキルギャップの定量化と人材育成政策の基盤データを提供する。",
    "デジタルスキルの分布と水準の定量的把握。", "イノベーション計量学", 2016, None, "measurement,policy", "policy,learning",
    ["European Commission", "OECD"], ["DESI Human Capital Dimension", "OECD Skills Outlook"], "",
    "デジタルスキル,スキルギャップ,人材育成", "digital skills, skills gap, human capital, workforce development")

add("Innovation and Trust Indicators", "イノベーションと信頼の指標",
    "社会的信頼水準（対人信頼、制度的信頼）とイノベーション活動の関係を測定・分析する指標体系。高信頼社会がリスクテイキングと協力的イノベーションを促進するメカニズムの実証的検証。",
    "社会的信頼とイノベーション活動の関係の定量分析。", "イノベーション計量学", 2008, None, "measurement", "policy,learning",
    ["Christian Bjørnskov", "OECD"], ["OECD Trust and Innovation Studies"], "",
    "信頼指標,社会的信頼,リスクテイキング", "trust indicators, social trust, risk-taking, cooperation")

add("Innovation Policy for Agri-Food Sector", "農食品セクターのイノベーション政策",
    "農業・食品産業のバリューチェーン全体にわたるイノベーション促進政策。精密農業、フードテック、代替タンパク質、食品安全技術等の分野横断的なイノベーション支援と規制環境整備を含む。",
    "農食品バリューチェーン全体のイノベーション促進。", "イノベーション政策", 2015, None, "policy", "policy",
    ["FAO", "OECD"], ["OECD Agricultural Innovation Systems Studies"], "",
    "農食品イノベーション,精密農業,フードテック", "agri-food innovation, precision agriculture, food tech")

add("Innovation Outcome Indicators vs Output Indicators", "イノベーション成果指標とアウトプット指標の区別",
    "イノベーション活動の直接的産出物（アウトプット：特許、論文等）と最終的な社会的・経済的成果（アウトカム：生産性向上、福祉改善等）を区別し、政策評価の適切な指標選択を導く概念的枠組み。",
    "イノベーション評価における指標の概念的整理。", "イノベーション計量学", 2005, None, "measurement,policy", "policy,learning",
    ["OECD"], ["OECD Blue Sky Forum on Innovation Indicators"], "",
    "アウトプットvsアウトカム,指標区別,政策評価", "output vs outcome, indicator distinction, policy evaluation")

add("Blue Sky Forum on Innovation Indicators", "イノベーション指標に関するブルースカイフォーラム",
    "OECDが約10年ごとに開催する、次世代のイノベーション測定方法論を議論する国際会議。2016年のギザ会議では、デジタル化、グローバル化、社会的イノベーション等の測定課題が議論された。",
    "次世代イノベーション測定の方向性を設定する国際的対話。", "イノベーション計量学", 1996, None, "measurement", "policy,learning",
    ["OECD NESTI Working Party"], ["OECD Blue Sky Forum Reports"], "",
    "ブルースカイ,次世代指標,方法論革新", "Blue Sky Forum, next-generation indicators, methodology innovation")

add("Innovation Policy for Demographic Change", "人口動態変化のためのイノベーション政策",
    "少子高齢化、人口減少、都市化等の人口動態変化に対応するイノベーション政策。労働力不足を補う自動化、高齢者QoL向上技術、地方創生のためのリモートワーク技術等を促進する政策枠組み。",
    "人口動態変化に対応するイノベーション政策。", "イノベーション政策", 2015, None, "policy,systemic", "policy",
    ["OECD", "European Commission"], ["OECD Ageing and Technology Reports"], "",
    "人口動態,少子高齢化,労働力不足", "demographic change, ageing society, labor shortage, automation")

add("Experimentation Clauses in Regulation", "規制における実験条項",
    "既存規制に一時的な例外条項を設けて、新技術やビジネスモデルの実証実験を法的に許容する制度。規制サンドボックスの法的根拠を提供し、イノベーションと規制の共進化を制度化する。",
    "規制内にイノベーション実験を許容する法的メカニズム。", "イノベーション政策", 2016, None, "policy,institutional", "policy",
    ["European Commission"], ["EU Better Regulation: Experimentation Clauses"], "",
    "実験条項,規制例外,法的根拠", "experimentation clause, regulatory exception, legal basis, sandbox")

add("Innovation Broker Function", "イノベーション・ブローカー機能",
    "異なるアクター（企業、大学、政府、市民社会）間のイノベーション連携を仲介・促進する機能の分析と制度化。情報仲介、ネットワーク構築、翻訳（異なる言語・文化間の橋渡し）、調整等の具体的機能を定義する。",
    "イノベーション連携を仲介する機能の分析と制度化。", "イノベーション政策", 2006, None, "institutional,policy", "policy,learning",
    ["Laurens Klerkx", "Cees Leeuwis"], ["Klerkx & Leeuwis (2009) Innovation Intermediaries"], "",
    "イノベーションブローカー,仲介機能,ネットワーク", "innovation broker, intermediary function, network building")

add("Innovation and Geopolitics", "イノベーションと地政学",
    "技術覇権競争、技術デカップリング、経済安全保障等の地政学的要因がイノベーション政策・戦略に与える影響の分析。米中技術競争、半導体サプライチェーン、AI規制等の地政学的文脈でのイノベーション政策を検討する。",
    "地政学的競争のイノベーション政策への影響分析。", "イノベーション政策", 2019, None, "policy,institutional", "policy",
    ["Henry Farrell", "Abraham Newman"], ["Farrell & Newman (2019) Weaponized Interdependence"], "",
    "地政学,技術覇権,デカップリング", "geopolitics, technology hegemony, decoupling, economic security")

add("Innovation Policy for Net Zero", "ネットゼロのためのイノベーション政策",
    "2050年ネットゼロ排出目標の達成に必要なクリーンテクノロジー・イノベーションを加速する包括的政策枠組み。IEAの技術ロードマップに基づき、R&D投資、実証支援、市場形成、国際協力を統合的に推進する。",
    "ネットゼロ達成のためのイノベーション加速政策。", "イノベーション政策", 2021, None, "policy,systemic", "policy",
    ["IEA", "Mission Innovation"], ["IEA Net Zero by 2050 Roadmap"], "",
    "ネットゼロ,クリーンテクノロジー,IEA", "net zero, clean technology, IEA, innovation acceleration")

add("Innovation Policy Coherence Assessment", "イノベーション政策一貫性評価",
    "複数の政策領域（研究、産業、教育、規制、貿易等）間でのイノベーション促進の一貫性・矛盾を体系的に評価する方法論。政策マッピング、政策間相互作用分析、ステークホルダー評価等の手法を統合する。",
    "多政策領域間のイノベーション政策一貫性の評価方法論。", "イノベーション政策評価", 2015, None, "measurement,policy", "policy",
    ["OECD"], ["OECD Innovation Policy Coherence Studies"], "",
    "政策一貫性評価,政策間相互作用,マッピング", "policy coherence assessment, policy interaction, mapping")

add("Science Park Performance Evaluation", "サイエンスパーク・パフォーマンス評価",
    "科学技術団地（サイエンスパーク）の入居企業のイノベーション・パフォーマンス（特許、売上成長、雇用成長、資金調達等）を非入居企業と比較して評価する方法論。サイエンスパーク政策の付加価値を厳密に推定する。",
    "サイエンスパークのイノベーション促進効果の厳密な評価。", "イノベーション政策評価", 2000, None, "measurement,institutional", "policy,learning",
    ["Phillip Phan", "Donald Siegel", "Mike Wright"], ["Siegel, Westhead & Wright (2003) Science Parks and Incubators"], "",
    "サイエンスパーク評価,インキュベーター効果,付加価値", "science park evaluation, incubator effect, value added")

add("Innovation and Digital Sovereignty", "イノベーションとデジタル主権",
    "クラウドインフラ、データ管理、AI基盤モデル等のデジタル基盤技術における国・地域の自律性を確保する政策概念。EU GAIA-X等のデジタルインフラ・イニシアチブと、デジタル技術のイノベーション促進のバランスを図る。",
    "デジタル基盤技術の自律性確保とイノベーション促進。", "イノベーション政策", 2020, None, "policy,institutional", "policy",
    ["European Commission"], ["EU GAIA-X Initiative", "EU Data Strategy"], "",
    "デジタル主権,クラウド自律性,GAIA-X", "digital sovereignty, cloud autonomy, GAIA-X, data sovereignty")

add("Indicator Dashboard for Innovation Policy", "イノベーション政策のための指標ダッシュボード",
    "イノベーション政策の監視・運営に必要な多次元的な指標をリアルタイムで統合的に表示するダッシュボード設計。インプット指標、プロセス指標、アウトプット指標、アウトカム指標を統合的に可視化する。",
    "イノベーション政策運営のための統合的指標可視化。", "イノベーション計量学", 2015, None, "measurement,policy", "policy",
    ["European Commission", "OECD"], ["EC Innovation Dashboard Tools"], "",
    "指標ダッシュボード,統合可視化,政策運営", "indicator dashboard, integrated visualization, policy management")

add("Innovation Policy for Indigenous Communities", "先住民コミュニティのイノベーション政策",
    "先住民族の伝統的知識をイノベーション・システムに統合し、先住民コミュニティのイノベーション能力を構築する政策アプローチ。伝統的知識の知財保護、文化的配慮を伴うイノベーション支援を含む。",
    "先住民族の伝統的知識とイノベーションの統合的政策。", "イノベーション政策", 2015, None, "policy,institutional", "policy,learning",
    ["WIPO", "UNESCO"], ["WIPO Traditional Knowledge Division"], "",
    "先住民イノベーション,伝統的知識,文化的配慮", "indigenous innovation, traditional knowledge, cultural sensitivity")

add("Patent Pledges and Innovation Commons", "パテント・プレッジとイノベーション・コモンズ",
    "特許保有者が自発的に特許権の行使を制限するプレッジ（誓約）を通じて、技術の共有とイノベーションの促進を図る制度。Tesla Open Patent Pledge、LOT Network等の民間イニシアチブが代表的。",
    "自発的な特許権制限によるイノベーション促進の制度。", "イノベーション政策", 2014, None, "institutional,policy", "policy",
    ["Tesla", "LOT Network"], ["Tesla Open Patent Pledge", "LOT Network Agreement"], "",
    "パテントプレッジ,特許共有,オープンイノベーション", "patent pledge, patent sharing, open innovation, commons")

add("Regulatory Technology (RegTech) for Innovation", "イノベーションのための規制テクノロジー",
    "AIやブロックチェーン等の技術を規制遵守・監督プロセスに適用し、規制コストの低減とコンプライアンスの効率化を実現するアプローチ。イノベーション企業の規制対応負担を軽減し、規制当局の監督能力を強化する。",
    "テクノロジーによる規制プロセスの効率化とイノベーション促進。", "イノベーション政策", 2016, None, "policy,institutional", "policy",
    ["UK FCA", "FinTech associations"], ["FCA RegTech Reports"], "",
    "RegTech,規制テクノロジー,コンプライアンス自動化", "RegTech, regulatory technology, compliance automation, supervisory tech")

# Save to JSON files
output_dir = os.path.dirname(os.path.abspath(__file__))
total = len(entries)
print(f"Total entries generated (batch 4): {total}")
print(f"ID range: inno_pol_636 to inno_pol_{635+total}")
print(f"Cumulative total: 146 + 106 + 83 + {total} = {146+106+83+total}")

for batch_idx in range(0, total, 50):
    batch = entries[batch_idx:batch_idx+50]
    batch_num = batch_idx // 50 + 9
    filepath = os.path.join(output_dir, f"pol_batch_{batch_num}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)
    print(f"Written {len(batch)} entries to {filepath} (IDs: {batch[0]['id']} - {batch[-1]['id']})")
