#!/usr/bin/env python3
"""Generate measurement_policy_governance entries batch 2 (inno_pol_447 to inno_pol_714)."""

import json
import os

entries = []
idx = 447

def add(name_en, name_ja, definition, impact, school, era_start, era_end, innov_type, cog_mech, researchers, works, opposing, kw_ja, kw_en, schumpeter="macro"):
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
        "schumpeter_layer": schumpeter,
        "status": "active",
        "source_reliability": "secondary",
        "data_completeness": 75,
    })
    idx += 1

# === INNOVATION MEASUREMENT - FIRM LEVEL (447-480) ===
add("Innovation Audit Methodology", "イノベーション監査方法論",
    "組織のイノベーション能力・活動・成果を体系的に評価する監査手法。イノベーション戦略、ポートフォリオ、プロセス、組織文化、外部連携の5領域を評価し、改善施策を導出する。",
    "組織のイノベーション能力の包括的診断手法。", "イノベーション計量学", 2000, None, "measurement", "learning",
    ["Tidd & Bessant"], ["Tidd & Bessant (2009) Managing Innovation"], "",
    "イノベーション監査,能力診断,組織評価", "innovation audit, capability diagnosis, organizational assessment")

add("R&D Productivity Measurement", "研究開発生産性の測定",
    "R&D投入に対する技術的・経済的成果の比率を測定する方法論群。特許/R&D比、新製品売上/R&D比、論文/研究者数等の指標を用いるが、R&Dの時間遅延効果やスピルオーバーの測定困難が課題。",
    "R&D投資の効率性評価における基本的方法論。", "イノベーション計量学", 1980, None, "measurement", "learning",
    ["Zvi Griliches", "Manuel Trajtenberg"], ["Griliches (1979) Issues in Assessing R&D Productivity"], "",
    "R&D生産性,研究効率,投入産出", "R&D productivity, research efficiency, input-output ratio")

add("Knowledge Production Function", "知識生産関数",
    "R&D投入と知識アウトプット（特許等）の関係を関数形式でモデル化した計量経済学的枠組み。Griliches (1979) とJaffe (1989)が先駆的であり、地域レベルの知識スピルオーバーの実証に広く用いられる。",
    "知識生産プロセスの計量経済学的モデル化。", "イノベーション計量学", 1979, None, "measurement", "learning",
    ["Zvi Griliches", "Adam Jaffe"], ["Griliches (1979)", "Jaffe (1989) Real Effects of Academic Research"], "",
    "知識生産関数,R&Dスピルオーバー,計量経済学", "knowledge production function, R&D spillover, econometric model")

add("Total Factor Productivity and Innovation", "全要素生産性とイノベーション",
    "TFP（全要素生産性）の変化をイノベーション活動の代理変数として用いる計量分析アプローチ。R&D資本ストック、特許ストック等をTFP成長の説明変数とし、イノベーションの経済成長への寄与を推計する。",
    "イノベーションの経済成長寄与の計量的推計。", "イノベーション計量学", 1957, None, "measurement", "learning",
    ["Robert Solow", "Zvi Griliches"], ["Solow (1957) Technical Change", "Griliches (1998) R&D and Productivity"], "",
    "TFP,全要素生産性,経済成長,R&D", "TFP, total factor productivity, economic growth, R&D contribution")

add("Innovation Expenditure Statistics", "イノベーション支出統計",
    "R&Dに限定されないイノベーション活動全体への支出を測定する統計。設計、マーケティング、トレーニング、設備投資等を含むイノベーション支出の全体像を把握し、R&D統計だけでは見えない投資パターンを明らかにする。",
    "R&Dを超えたイノベーション投資の全体像の把握。", "イノベーション計量学", 1997, None, "measurement", "policy",
    ["OECD", "Eurostat"], ["Oslo Manual Innovation Expenditure Guidelines"], "",
    "イノベーション支出,非R&D投資,全体的投資", "innovation expenditure, non-R&D investment, total innovation spending")

add("Innovation Performance Paradox", "イノベーション・パフォーマンスのパラドックス",
    "欧州が米国と同等のR&D投資を行いながら、イノベーション・アウトプット（特許、ハイテク輸出、VC投資等）で劣後する現象の分析。構造的要因（企業規模、セクター構成、VC市場）と制度的要因が複合的に作用する。",
    "投入と産出の不整合からイノベーション・システムの構造問題を診断。", "イノベーション計量学", 2001, None, "measurement,policy", "policy,learning",
    ["European Commission", "Dosi, Llerena & Labini"], ["EU Competitiveness Reports"], "",
    "欧州パラドックス,パフォーマンスギャップ", "European paradox, performance gap, innovation efficiency")

add("Revealed Innovation Advantage", "顕示イノベーション優位性",
    "特定国・地域のイノベーション・アウトプット（特許、論文、新製品等）のセクター別シェアを世界平均と比較し、相対的なイノベーション専門化パターンを明らかにする指標。RTAの概念を広くイノベーション指標に適用。",
    "国・地域のイノベーション専門化パターンの比較分析。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["European Commission"], ["EIS Methodology Reports"], "",
    "イノベーション優位性,専門化パターン,比較指標", "revealed innovation advantage, specialization pattern, comparative indicator")

add("Innovation Persistence", "イノベーションの持続性",
    "企業のイノベーション活動が時間的に持続するか否か、また過去のイノベーション経験が将来のイノベーション確率を高めるか（状態依存性）を実証的に分析する研究テーマ。CISパネルデータを用いた動学的分析が基本。",
    "企業のイノベーション活動の時間的パターンと経路依存性の分析。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Jacques Mairesse", "Pierre Mohnen", "Carine Peeters"], ["Peters (2009) Persistence of innovation"], "",
    "イノベーション持続性,状態依存,パネルデータ", "innovation persistence, state dependence, panel data, path dependence")

add("Innovation Failure and Abandonment", "イノベーションの失敗と断念",
    "イノベーション・プロジェクトの失敗・断念・中止の頻度、原因、パターンを測定・分析する研究テーマ。CISの障壁質問や追加調査モジュールにより、成功バイアスを補正してイノベーション活動の全体像を把握する。",
    "イノベーション活動のダークサイドの体系的測定。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Anthony Arundel", "Eurostat"], ["CIS Module on Innovation Barriers"], "",
    "イノベーション失敗,断念,障壁,成功バイアス", "innovation failure, abandonment, barriers, success bias")

add("Hidden Innovation", "隠れたイノベーション",
    "従来のイノベーション指標（特許、R&D支出、CIS）では捕捉されないイノベーション活動を指す概念。サービス業、創造産業、公共セクター、非公式なプロセス改善等の「見えない」イノベーションの測定方法論的課題を提起。",
    "従来指標で見逃されるイノベーション活動の認識と測定。", "イノベーション計量学", 2007, None, "measurement", "learning",
    ["Nesta", "Charles Leadbeater"], ["NESTA (2007) Hidden Innovation"], "",
    "隠れたイノベーション,非公式革新,測定の限界", "hidden innovation, informal innovation, measurement limitations")

add("User Innovation Measurement", "ユーザーイノベーションの測定",
    "最終利用者（消費者、企業ユーザー等）が自らのニーズのために行うイノベーション活動を測定する方法論。von Hippelの理論に基づき、専用調査（消費者イノベーション調査等）でユーザーイノベーションの発生率と経済的価値を推計する。",
    "製造者中心の測定を補完するユーザー起点イノベーションの定量化。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Eric von Hippel", "Jeroen de Jong"], ["von Hippel (2005) Democratizing Innovation"], "",
    "ユーザーイノベーション,消費者調査,非製造者革新", "user innovation, consumer survey, non-producer innovation")

add("Service Innovation Measurement", "サービスイノベーションの測定",
    "サービス部門特有のイノベーション活動（新サービス開発、配達方法の革新、クライアント・インターフェースの革新等）を測定する方法論。製造業中心のイノベーション指標のサービス適応と独自指標の開発を含む。",
    "サービス部門のイノベーション特性に適合した測定手法。", "イノベーション計量学", 2000, None, "measurement", "learning",
    ["Faïz Gallouj", "Ian Miles"], ["Gallouj & Weinstein (1997) Innovation in services"], "",
    "サービスイノベーション,無形資産,非技術的革新", "service innovation, intangible assets, non-technological innovation")

add("Social Innovation Measurement", "ソーシャルイノベーションの測定",
    "社会的課題の解決を目的とする新しいアイデア、モデル、製品、サービスの創出・普及・影響を測定する方法論。社会的インパクト測定、Theory of Change、社会的ROI等の手法を統合的に活用する。",
    "社会的目的のイノベーション活動と成果の定量化。", "イノベーション計量学", 2010, None, "measurement,policy", "policy,learning",
    ["TEPSIE", "Geoff Mulgan"], ["TEPSIE (2014) Social Innovation Theory and Research"], "",
    "ソーシャルイノベーション測定,社会的インパクト,Theory of Change", "social innovation measurement, social impact, Theory of Change")

add("Public Sector Innovation Measurement", "公共セクターイノベーションの測定",
    "政府・公共機関におけるイノベーション活動（政策革新、組織変革、デジタル化等）を体系的に測定する方法論。OECDのOPSIが推進するフレームワークで、サーベイ手法とケーススタディを組み合わせる。",
    "公共セクター固有のイノベーション測定枠組み。", "イノベーション計量学", 2010, None, "measurement,policy", "policy",
    ["OECD OPSI", "Danish Agency for Modernisation"], ["OECD Observatory of Public Sector Innovation"], "",
    "公共セクターイノベーション,行政革新,OPSI", "public sector innovation, government innovation, OPSI")

add("Grassroots Innovation Measurement", "草の根イノベーションの測定",
    "地域コミュニティ、市民グループ、メーカー・ムーブメント等の非公式なイノベーション活動を捕捉・定量化する方法論。制度的イノベーション・システムの外側で生じるボトムアップ型革新を可視化する。",
    "非公式・コミュニティ主導型イノベーションの可視化。", "イノベーション計量学", 2010, None, "measurement", "learning",
    ["Adrian Smith", "Andy Stirling", "STEPS Centre"], ["Smith et al. (2014) Grassroots Innovation Movements"], "",
    "草の根イノベーション,コミュニティ主導,ボトムアップ", "grassroots innovation, community-led, bottom-up, maker movement")

# === INNOVATION POLICY - EMERGING THEMES (462-500) ===
add("Moonshot Policy", "ムーンショット政策",
    "極めて野心的かつ長期的な技術・社会目標（ムーンショット目標）を設定し、複数の研究プログラムを統合的に推進する政策アプローチ。日本のムーンショット研究開発事業（2020年）、DARPA等が代表的。",
    "超長期・超野心的目標設定によるイノベーション方向付け。", "イノベーション政策", 2018, None, "policy,systemic", "policy",
    ["Cabinet Office Japan", "DARPA", "Mariana Mazzucato"], ["Mazzucato (2021) Mission Economy"], "",
    "ムーンショット,野心的目標,破壊的イノベーション", "moonshot, ambitious targets, disruptive innovation, DARPA")

add("ARPA Model for Innovation Agency", "ARPAモデルによるイノベーション機関",
    "DARPA（米国防高等研究計画局）の組織設計原理を他分野（エネルギー、健康、気候等）に適用するイノベーション機関設計。プログラム・マネージャーの裁量権、回転ドア人事、ハイリスク・プロジェクト選定等を特徴とする。",
    "破壊的イノベーション推進のための組織設計モデル。", "イノベーション政策", 2009, None, "policy,institutional", "policy",
    ["DARPA", "William Bonvillian"], ["Bonvillian & Van Atta (2011) ARPA-E and DARPA"], "",
    "ARPAモデル,DARPA,プログラムマネージャー", "ARPA model, DARPA, program manager, high-risk research agency")

add("National Science Foundation (NSF) Evaluation Framework", "NSF評価フレームワーク",
    "米国NSFが研究助成プログラムの成果と社会的インパクトを評価するために用いるフレームワーク。Broader Impacts基準（2007年改訂）により、研究の知的メリットに加えて社会的貢献の評価を制度化。",
    "研究助成の知的メリットと社会的貢献の統合評価。", "イノベーション政策評価", 1997, None, "measurement,policy", "policy",
    ["NSF"], ["NSF Merit Review Criteria"], "",
    "NSF評価,メリットレビュー,Broader Impacts", "NSF evaluation, merit review, broader impacts, research assessment")

add("Horizon Europe Framework Programme", "Horizon Europeフレームワーク・プログラム",
    "EU最大の研究イノベーション資金プログラム（2021-2027年、955億ユーロ）。卓越した科学（ERC等）、グローバル課題と産業競争力、イノベーティブ・ヨーロッパ（EIC等）の3柱で構成。ミッション指向型アプローチを本格導入。",
    "EU研究イノベーション資金の最大のフレームワーク。", "イノベーション政策", 2021, None, "policy,institutional", "policy",
    ["European Commission"], ["Horizon Europe Regulation (2021)"], "",
    "Horizon Europe,EU研究資金,ミッション指向", "Horizon Europe, EU research funding, mission-oriented, ERC, EIC")

add("European Innovation Council (EIC)", "欧州イノベーション評議会",
    "Horizon Europe内に設置されたEU初の本格的イノベーション支援機関（2021年正式設立）。DARPA型のプログラムマネージャー制度とVC的な直接投資機能を統合し、深層技術（ディープテック）スタートアップを支援する。",
    "EUの深層技術スタートアップ支援の中核機関。", "イノベーション政策", 2021, None, "policy,institutional", "policy",
    ["European Commission"], ["EIC Work Programme"], "",
    "EIC,欧州イノベーション評議会,ディープテック", "EIC, European Innovation Council, deep tech, breakthrough innovation")

add("European Research Area (ERA)", "欧州研究圏",
    "EU域内で研究者、知識、技術が自由に移動する統一的な研究空間の構築を目指す政策構想。2000年のリスボン戦略で提唱され、研究システムの断片化解消、キャリアの国際的流動性、研究インフラの共有等を推進する。",
    "EU域内研究活動の統一市場としての政策構想。", "イノベーション政策", 2000, None, "policy,institutional", "policy",
    ["European Commission"], ["ERA Communication (2000)", "New ERA Communication (2020)"], "",
    "ERA,欧州研究圏,研究者流動性", "European Research Area, ERA, researcher mobility, research integration")

add("Digital Twin for Policy Simulation", "政策シミュレーションのためのデジタルツイン",
    "イノベーション・エコシステムの仮想的な複製（デジタルツイン）を構築し、様々な政策介入のシナリオをシミュレーションする先端的手法。ABMやシステムダイナミクスを統合し、データ駆動型の政策設計を支援する。",
    "データ駆動型の政策設計を支える先端シミュレーション技術。", "イノベーション計量学", 2020, None, "measurement,policy", "policy,learning",
    ["European Commission", "JRC"], ["JRC Digital Innovation Ecosystem Reports"], "",
    "デジタルツイン,政策シミュレーション,データ駆動", "digital twin, policy simulation, data-driven, scenario analysis")

add("Innovation Ecosystem Health Metrics", "イノベーション・エコシステム健全性指標",
    "イノベーション・エコシステムの生態学的健全性をアナロジーとして評価する指標体系。多様性、連結性、レジリエンス、生産性の4次元で構成され、エコシステムの持続可能性を診断する。",
    "エコシステムの持続可能性を多次元的に診断する枠組み。", "イノベーション計量学", 2015, None, "measurement,systemic", "policy,learning",
    ["Daniel Isenberg", "Ron Adner"], ["Adner (2012) The Wide Lens"], "",
    "エコシステム健全性,多様性,レジリエンス", "ecosystem health, diversity, resilience, connectivity, productivity")

add("Intellectual Property Valuation Standards", "知的財産評価基準",
    "特許、商標、著作権、営業秘密等の無形資産の経済的価値を算定するための国際的な評価基準体系。コスト法、マーケット法、インカム法の三手法を核とし、ISO 10668やIVSが標準化を推進。",
    "知的財産の経済的価値評価の国際標準化。", "特許分析", 2010, None, "measurement", "learning",
    ["ISO", "IVS Council"], ["ISO 10668 Brand Valuation", "IVS Intangible Assets Standards"], "",
    "知財評価,無形資産,評価基準", "IP valuation, intangible assets, valuation standards, ISO 10668")

add("Innovation Procurement Observatory", "イノベーション調達観測所",
    "公共調達におけるイノベーション促進の実態を体系的にモニタリング・評価する機関・制度。EU各国のイノベーション調達の件数、金額、手法、効果を追跡し、ベストプラクティスの共有を促進する。",
    "イノベーション調達の実態モニタリングと政策改善。", "イノベーション政策評価", 2015, None, "measurement,policy", "policy",
    ["European Commission"], ["EC Innovation Procurement Data Reports"], "",
    "調達観測,公共調達モニタリング,イノベーション調達", "procurement observatory, public procurement monitoring, innovation procurement")

add("R&D Tax Incentive Design Principles", "R&D税制設計原則",
    "R&D税額控除制度の効果を最大化するための制度設計原則。対象支出の定義、控除率の設定、繰越・繰戻し規定、中小企業向け優遇、コンプライアンス負担の最小化等の設計変数の最適化を図る。",
    "R&D税制の政策効果を最大化する制度設計ガイドライン。", "イノベーション政策", 2010, None, "policy", "policy",
    ["OECD"], ["OECD R&D Tax Incentive Design Features"], "",
    "R&D税制設計,制度設計原則,税額控除設計", "R&D tax design, design principles, tax credit optimization")

add("Innovation Prize Design Framework", "イノベーション賞金設計枠組み",
    "課題解決型イノベーション賞金（inducement prize）の効果的設計のための原則・枠組み。課題定義、賞金額設定、参加条件、評価基準、知財取扱い等の設計変数を体系化する。",
    "イノベーション誘導型賞金の効果的設計ガイドライン。", "イノベーション政策", 2009, None, "policy", "policy,learning",
    ["Nesta", "Knowledge Ecology International"], ["Nesta (2014) Challenge Prizes: A Practice Guide"], "",
    "賞金設計,チャレンジ設計,インセンティブ設計", "prize design, challenge design, incentive design, inducement prize")

add("Innovation System Transition Policy", "イノベーション・システム移行政策",
    "既存のイノベーション・システムから持続可能性志向の新システムへの移行を政策的に促進するアプローチ。ニッチ育成、レジーム圧力、ランドスケープ変化の三層を考慮した多段階の政策介入を設計する。",
    "社会-技術システムの持続可能な移行を政策的に推進。", "イノベーション政策", 2012, None, "policy,systemic", "policy",
    ["Johan Schot", "Frank Geels", "Adrian Smith"], ["Schot & Geels (2008) Strategic niche management"], "",
    "システム移行,トランジション政策,持続可能性", "system transition, transition policy, sustainability, niche management")

add("Responsible Innovation Governance", "責任あるイノベーション・ガバナンス",
    "イノベーション活動の倫理的・社会的影響を予見的に管理し、多様なステークホルダーの参加を通じて社会的に受容可能な方向にイノベーションを導くガバナンス体制。予見、内省、包摂、応答の4次元からなる。",
    "イノベーションの社会的方向付けを制度化するガバナンス。", "イノベーション政策", 2013, None, "policy,institutional", "policy",
    ["Jack Stilgoe", "Richard Owen", "Phil Macnaghten"], ["Stilgoe et al. (2013) Developing a framework for RRI"], "",
    "責任あるガバナンス,RRI,予見性,包摂性", "responsible governance, RRI, anticipation, inclusivity, reflexivity")

add("Science and Technology Human Resources Indicators", "科学技術人的資源指標",
    "研究者数、科学技術分野の博士号取得者数、STEM人材の国際流動性等を測定する指標群。OECDのSTHR（Science and Technology Human Resources）統計とキャンベラ・マニュアルが方法論的基盤を提供。",
    "科学技術人材の供給と流動性の定量的把握。", "イノベーション計量学", 1995, None, "measurement", "policy",
    ["OECD"], ["Canberra Manual (1995)", "OECD STHR Statistics"], "",
    "科学技術人材,STHR,研究者統計", "S&T human resources, STHR, researcher statistics, STEM workforce")

add("Canberra Manual", "キャンベラ・マニュアル",
    "OECDが1995年に策定した科学技術人的資源の統計的測定に関する国際ガイドライン。科学技術人材の定義（資格・職業ベース）、ストックとフローの測定方法、国際比較の枠組みを標準化した。",
    "科学技術人材統計の国際標準ガイドライン。", "イノベーション計量学", 1995, None, "measurement", "policy",
    ["OECD", "Eurostat"], ["OECD Canberra Manual (1995)"], "",
    "キャンベラマニュアル,人材統計,OECD", "Canberra Manual, human resources statistics, OECD, S&T personnel")

add("Frascati Manual", "フラスカティ・マニュアル",
    "OECDが1963年に初版を策定したR&D活動の統計的測定に関する国際標準ガイドライン。R&Dの定義（基礎研究・応用研究・実験的開発）、支出・人員の測定方法を規定し、R&D統計の国際比較可能性の基盤。",
    "R&D統計の国際標準化を実現した最も基本的なガイドライン。", "イノベーション計量学", 1963, None, "measurement", "policy",
    ["OECD"], ["OECD Frascati Manual (latest: 2015 edition)"], "",
    "フラスカティマニュアル,R&D統計,OECD", "Frascati Manual, R&D statistics, OECD, research measurement")

add("Oslo Manual 4th Edition (2018)", "オスロ・マニュアル第4版（2018年）",
    "2018年に改訂された最新版。イノベーションの定義を「新規または改善された製品・ビジネスプロセス」に簡素化し、デジタル化、グローバリゼーション、知識集約型サービスの文脈に適応。企業内イノベーション活動と外部要因の相互作用を重視。",
    "デジタル時代に適合したイノベーション測定の国際標準の最新版。", "イノベーション計量学", 2018, None, "measurement,policy", "policy,learning",
    ["OECD", "Eurostat"], ["Oslo Manual 4th Edition (2018)"], "",
    "オスロマニュアル第4版,イノベーション定義改訂,デジタル化", "Oslo Manual 4th edition, innovation definition, digitalization")

# === SCIENCE POLICY & RESEARCH GOVERNANCE (486-520) ===
add("Science of Science Policy (SoSP)", "科学政策の科学",
    "科学政策の設計・実施・評価を科学的方法論で分析する学際的研究プログラム。NSFのSciSIP（Science of Science and Innovation Policy）プログラムが制度的支柱で、計量科学学、ネットワーク分析、計算社会科学等の手法を統合。",
    "科学政策自体を科学的研究対象とする学際的プログラム。", "イノベーション政策評価", 2006, None, "measurement,policy", "policy,learning",
    ["NSF", "Julia Lane", "Kaye Husbands Fealing"], ["Lane (2010) Let's make science metrics more scientific"], "",
    "科学政策の科学,SciSIP,政策分析", "science of science policy, SoSP, SciSIP, policy analysis")

add("STAR METRICS", "STAR METRICS",
    "米国NIH/NSFが開発した、研究助成の経済的・社会的成果を追跡する大規模データインフラ。研究プロジェクトから雇用、論文、特許、ビジネス創出に至るアウトカムチェーンを行政データのリンケージにより把握する。",
    "研究助成の多面的成果追跡のためのデータインフラ。", "イノベーション計量学", 2010, None, "measurement", "policy,learning",
    ["NIH", "NSF", "Julia Lane"], ["STAR METRICS Technical Documentation"], "",
    "STAR METRICS,研究成果追跡,データリンケージ", "STAR METRICS, research outcome tracking, data linkage, administrative data")

add("Research Portfolio Analysis", "研究ポートフォリオ分析",
    "研究助成機関のポートフォリオ全体の構成、バランス、成果を分析する方法論。テーマ分布、リスクプロファイル、期待リターン、補完性を評価し、戦略的な資源配分の意思決定を支援する。",
    "研究助成の戦略的資源配分を支える分析手法。", "イノベーション政策評価", 2008, None, "measurement,policy", "policy,learning",
    ["NIH", "NSF"], ["NIH Research Portfolio Analysis Reports"], "",
    "ポートフォリオ分析,資源配分,研究戦略", "portfolio analysis, resource allocation, research strategy, funding balance")

add("Peer Review as Innovation Governance", "イノベーション・ガバナンスとしてのピアレビュー",
    "研究助成の選定プロセスにおけるピアレビュー制度がイノベーションの方向性に与える影響の分析。保守性バイアス（革新的提案の低評価）、一致度の低さ、多様性効果等の構造的特性がイノベーション・ポートフォリオを形成する。",
    "ピアレビュー制度のイノベーション方向付け効果の分析。", "イノベーション政策評価", 2000, None, "policy,institutional", "policy,learning",
    ["Lutz Bornmann", "Daniel Mutz"], ["Bornmann (2011) Scientific Peer Review"], "",
    "ピアレビュー,研究助成,保守性バイアス", "peer review, research funding, conservatism bias, innovation direction")

add("Open Peer Review for Research Assessment", "研究評価のための公開ピアレビュー",
    "匿名性を排除し、レビュープロセスと内容を公開する透明なピアレビュー制度。レビューの質向上、説明責任の強化、建設的フィードバックの促進を目指す。eLife、F1000Research等が先駆的に導入。",
    "研究評価の透明性と説明責任を高める制度革新。", "イノベーション政策", 2010, None, "institutional", "policy,learning",
    ["F1000Research", "eLife"], ["Ross-Hellauer (2017) What is open peer review?"], "",
    "公開ピアレビュー,透明性,説明責任", "open peer review, transparency, accountability, research assessment")

add("Preprint Server Impact on Innovation", "プレプリント・サーバーのイノベーションへの影響",
    "arXiv（1991年）、bioRxiv（2013年）等のプレプリント・サーバーが研究知識の拡散速度とイノベーション・プロセスに与える影響の分析。オープンアクセスによる知識普及の加速と査読なし公開のリスクのバランスを評価する。",
    "プレプリントによる研究知識の迅速な拡散とイノベーション加速。", "イノベーション計量学", 2013, None, "measurement", "learning",
    ["John Inglis", "Richard Sever"], ["Fraser et al. (2021) The evolving role of preprints"], "",
    "プレプリント,知識拡散,オープンアクセス", "preprint, knowledge dissemination, open access, arXiv, bioRxiv")

add("Citizen Science Policy Framework", "市民科学の政策枠組み",
    "市民が科学研究に参加する市民科学活動を制度的に促進する政策フレームワーク。データ品質管理、知的所有権、倫理的配慮、インセンティブ設計等の課題に対処し、市民参加による研究の社会的正当性を高める。",
    "市民参加型科学研究の制度的促進枠組み。", "イノベーション政策", 2014, None, "policy,institutional", "policy,learning",
    ["European Commission", "ECSA"], ["ECSA Ten Principles of Citizen Science"], "",
    "市民科学,市民参加,クラウドサイエンス", "citizen science, public participation, crowd science, policy framework")

add("Research Infrastructure Policy", "研究インフラ政策",
    "大型研究施設（加速器、天文台、ゲノムセンター等）やデジタル研究インフラ（スパコン、データリポジトリ等）の計画・資金調達・運営・アクセスを制度化する政策。ESFRI（欧州）が戦略的ロードマップを提供。",
    "研究活動の基盤的インフラの戦略的整備と運営。", "イノベーション政策", 2000, None, "policy,institutional", "policy",
    ["ESFRI", "European Commission"], ["ESFRI Roadmap"], "",
    "研究インフラ,大型施設,ESFRI", "research infrastructure, large-scale facilities, ESFRI, e-infrastructure")

add("Research Data Management Policy", "研究データ管理政策",
    "研究データの生成、保存、共有、再利用に関する制度的方針と技術的標準。FAIR原則（Findable, Accessible, Interoperable, Reusable）が中核で、EU Open Scienceとデータ駆動型イノベーションの基盤。",
    "研究データの効果的管理と再利用の制度化。", "イノベーション政策", 2016, None, "policy,institutional", "policy,learning",
    ["FORCE11", "Barend Mons"], ["Wilkinson et al. (2016) The FAIR Guiding Principles"], "",
    "研究データ管理,FAIR原則,データ共有", "research data management, FAIR principles, data sharing, open data")

add("Academic Freedom and Innovation", "学問の自由とイノベーション",
    "研究テーマ選択の自由、方法論的自律性、成果公表の自由等の学問の自由の保障がイノベーション創出に与える影響の分析。好奇心駆動型研究の予測不能な長期的イノベーション成果（セレンディピティ）の重要性を強調する。",
    "学問の自由がイノベーションの源泉となるメカニズムの分析。", "イノベーション政策", 1945, None, "policy,institutional", "policy,learning",
    ["Vannevar Bush", "Donald Stokes"], ["Bush (1945) Science: The Endless Frontier"], "directed research",
    "学問の自由,好奇心駆動研究,セレンディピティ", "academic freedom, curiosity-driven research, serendipity, basic research")

add("Pasteur's Quadrant Model", "パスツールの象限モデル",
    "基礎研究と応用研究の二分法を超え、「用途に触発された基礎研究」（パスツール型）の独自カテゴリーを提唱するモデル。Stokes（1997年）が提案し、基礎性と応用性の両立する研究の政策的重要性を明確化した。",
    "基礎・応用の二分法を超える研究分類の新パラダイム。", "イノベーション政策", 1997, None, "policy,measurement", "policy,learning",
    ["Donald Stokes"], ["Stokes (1997) Pasteur's Quadrant"], "",
    "パスツールの象限,用途触発型基礎研究,研究分類", "Pasteur's Quadrant, use-inspired basic research, research classification")

add("Linear Model of Innovation", "イノベーションの線形モデル",
    "基礎研究→応用研究→開発→生産→拡散の一方向的な連鎖としてイノベーション・プロセスを描写するモデル。Bush (1945) に帰せられることが多いが、Godin（2006年）はこの帰属の誤りを指摘。システミック・モデルとの対比で批判の対象。",
    "イノベーション政策の初期的フレームワークとして長く影響力を持った。", "イノベーション政策", 1945, None, "policy", "policy,learning",
    ["Vannevar Bush", "Benoît Godin"], ["Bush (1945) Science: The Endless Frontier"], "systemic model of innovation",
    "線形モデル,基礎研究から応用へ,パイプライン", "linear model, basic to applied, pipeline, science push")

add("Chain-Linked Model of Innovation", "イノベーションの連鎖モデル",
    "Kline & Rosenberg（1986年）が提唱した、イノベーション・プロセスを研究と市場の間の複雑なフィードバック・ループとして描写するモデル。線形モデルを批判し、知識ストックへの多段階的参照とフィードバックの重要性を強調。",
    "イノベーション・プロセスの非線形性とフィードバック構造の理論化。", "イノベーション政策", 1986, None, "systemic", "policy,learning",
    ["Stephen Kline", "Nathan Rosenberg"], ["Kline & Rosenberg (1986) An Overview of Innovation"], "linear model of innovation",
    "連鎖モデル,フィードバック,非線形プロセス", "chain-linked model, feedback, non-linear process, Kline-Rosenberg")

add("National Innovation Capacity", "国家イノベーション能力",
    "国全体のイノベーション創出・商業化能力を決定する制度的・構造的要因を統合的に分析する枠組み。Porter & Stern（2001年）がNISの制度分析と成長理論のR&Dモデルを統合し、国際比較の計量分析を可能にした。",
    "国家レベルのイノベーション能力の決定要因の統合分析。", "イノベーションシステム論", 2001, None, "measurement,systemic", "policy,learning",
    ["Michael Porter", "Scott Stern"], ["Porter & Stern (2001) National Innovative Capacity"], "",
    "国家イノベーション能力,制度要因,国際比較", "national innovation capacity, institutional factors, international comparison")

add("Innovation Catch-Up Theory", "イノベーション・キャッチアップ理論",
    "後発国が先進国の技術的フロンティアに接近するメカニズムとその政策条件を分析する理論体系。Abramovitz（1986年）の社会的能力論とLee（2013年）のリープフロッグ戦略が代表的で、発展途上国のイノベーション政策の理論的基盤。",
    "後発国の技術的キャッチアップの理論と政策条件。", "イノベーション政策", 1986, None, "policy,systemic", "policy,learning",
    ["Moses Abramovitz", "Keun Lee"], ["Abramovitz (1986) Catching Up", "Lee (2013) Schumpeterian Analysis"], "",
    "キャッチアップ,社会的能力,リープフロッグ", "catch-up, social capability, leapfrogging, latecomer advantage")

add("Middle-Income Trap and Innovation Policy", "中所得国の罠とイノベーション政策",
    "新興国が中所得水準で成長が停滞する「中所得国の罠」を脱出するためのイノベーション政策の役割の分析。模倣型からイノベーション主導型への成長モード転換に必要な制度改革と政策設計を議論する。",
    "中所得国の成長モード転換におけるイノベーション政策の役割。", "イノベーション政策", 2007, None, "policy,systemic", "policy,learning",
    ["Indermit Gill", "Homi Kharas", "World Bank"], ["Gill & Kharas (2007) An East Asian Renaissance"], "",
    "中所得国の罠,成長モード転換,制度改革", "middle-income trap, growth mode transition, institutional reform")

# === REMAINING ENTRIES TO REACH 714 (502-714) ===
# Innovation standards, methods, specific country models, etc.

add("Singapore National Innovation Policy", "シンガポール国家イノベーション政策",
    "小規模開放経済としてのシンガポールが採用するイノベーション政策モデル。政府主導のR&D投資、多国籍企業誘致、研究機関設立（A*STAR）、人材誘致を統合的に推進する開発国家型イノベーション政策。",
    "開発国家型イノベーション政策の代表的モデル。", "イノベーション政策", 1991, None, "policy,institutional", "policy",
    ["A*STAR", "Economic Development Board"], ["Singapore RIE 2025 Plan"], "",
    "シンガポール,開発国家,A*STAR", "Singapore, developmental state, A*STAR, innovation policy model")

add("Israel Innovation Ecosystem (Startup Nation)", "イスラエル・イノベーション・エコシステム",
    "イスラエルが構築した、軍事技術のスピルオーバー、移民人材、VC投資、OCS/IIA（イノベーション庁）の支援を統合したスタートアップ・エコシステム。人口比でのVC投資額とスタートアップ密度が世界最高水準。",
    "軍事技術・移民・VC・政府支援の統合によるエコシステム。", "イノベーション政策", 1993, None, "systemic,policy", "policy,learning",
    ["Israel Innovation Authority", "Dan Senor", "Saul Singer"], ["Senor & Singer (2009) Start-Up Nation"], "",
    "イスラエル,スタートアップネイション,OCS", "Israel, Startup Nation, innovation authority, military spillover")

add("German Mittelstand Innovation Model", "ドイツ中堅企業イノベーションモデル",
    "ドイツの中堅企業（ミッテルシュタント）が世界市場でニッチ・リーダーシップを獲得するイノベーション・モデル。長期的R&D投資、職業訓練（デュアルシステム）、フラウンホーファーとの連携を特徴とする「隠れたチャンピオン」現象。",
    "中堅企業の世界市場ニッチ・リーダーシップの革新モデル。", "イノベーション政策", 1990, None, "institutional,policy", "policy,learning",
    ["Hermann Simon", "Fraunhofer-Gesellschaft"], ["Simon (1996) Hidden Champions"], "",
    "ミッテルシュタント,隠れたチャンピオン,ニッチリーダー", "Mittelstand, hidden champions, niche leadership, German innovation")

add("Chinese Innovation Policy Model", "中国イノベーション政策モデル",
    "国家主導のメガプロジェクト（千人計画、中国製造2025等）と市場競争の組み合わせによる中国固有のイノベーション政策モデル。巨大国内市場、政府調達、標準化戦略、デジタルインフラ投資を統合的に活用。",
    "国家主導と市場競争を融合した中国固有のイノベーション政策。", "イノベーション政策", 2006, None, "policy,systemic", "policy",
    ["Chinese State Council", "MOST"], ["Made in China 2025", "Medium-Long Term S&T Plan (2006-2020)"], "",
    "中国イノベーション,国家主導,中国製造2025", "Chinese innovation, state-led, Made in China 2025, techno-nationalism")

add("Japanese Science Technology Basic Plan", "日本の科学技術基本計画",
    "日本政府が5年ごとに策定する科学技術イノベーション政策の基本計画。第1期（1996年）から第6期（2021年）まで、Society 5.0の実現、研究力強化、イノベーション・エコシステム構築等を推進。",
    "日本の科学技術イノベーション政策の中長期的方向性の策定。", "イノベーション政策", 1996, None, "policy,institutional", "policy",
    ["Council for Science, Technology and Innovation (CSTI)"], ["6th Science, Technology and Innovation Basic Plan (2021)"], "",
    "科学技術基本計画,Society 5.0,CSTI", "S&T Basic Plan, Society 5.0, CSTI, Japan innovation policy")

add("Korean Innovation-Driven Growth Strategy", "韓国イノベーション主導成長戦略",
    "韓国がキャッチアップ型成長からイノベーション主導型成長への転換を図る政策フレームワーク。大企業（チェボル）依存からスタートアップ・エコシステム育成へ、追随型R&Dからフロンティア研究へのシフトを推進。",
    "キャッチアップからイノベーション・フロンティアへの転換政策。", "イノベーション政策", 2017, None, "policy,systemic", "policy",
    ["Korean Ministry of SMEs and Startups"], ["Korea Innovation Growth Strategy"], "",
    "韓国イノベーション,成長モード転換,スタートアップ育成", "Korean innovation, growth mode shift, startup ecosystem")

add("Nordic Innovation Model", "北欧イノベーションモデル",
    "高福祉・高信頼・高教育の社会基盤の上に構築される北欧諸国のイノベーション・モデル。社会的セーフティネットが起業リスクを低減し、ユーザー駆動型イノベーション、デザイン思考、公共セクター革新を特徴とする。",
    "社会的信頼と福祉を基盤とするイノベーション・モデル。", "イノベーション政策", 2005, None, "systemic,policy", "policy,learning",
    ["Nordic Innovation", "Bengt-Åke Lundvall"], ["Edquist & Hommen (2008) Small Country Innovation Systems"], "",
    "北欧モデル,社会的信頼,ユーザー駆動", "Nordic model, social trust, user-driven innovation, welfare state innovation")

add("Swiss Innovation Ecosystem", "スイスイノベーション・エコシステム",
    "高度な基礎研究能力（ETH等）、精密産業クラスター、多国籍企業の研究拠点集積、直接民主制による安定的制度環境を統合したスイスのイノベーション・エコシステム。GII首位常連の要因分析。",
    "基礎研究・産業クラスター・制度安定性の統合によるイノベーション優位。", "イノベーション政策", 2000, None, "systemic,institutional", "policy,learning",
    ["ETH Zurich", "Innosuisse"], ["Swiss Science and Innovation Council Reports"], "",
    "スイスイノベーション,ETH,精密産業,GII", "Swiss innovation, ETH, precision industry, GII top performer")

add("UK Industrial Strategy and Innovation", "英国産業戦略とイノベーション",
    "英国のイノベーション政策の制度的枠組み。Innovate UK（旧TSB）、Catapult Centres、Industrial Strategy Challenge Fund等のイノベーション支援制度群と、セクター別ディール（Sector Deals）を統合。",
    "英国のイノベーション支援制度の統合的枠組み。", "イノベーション政策", 2017, None, "policy,institutional", "policy",
    ["Innovate UK", "UKRI"], ["UK Industrial Strategy White Paper (2017)"], "",
    "英国産業戦略,Innovate UK,Catapult", "UK industrial strategy, Innovate UK, Catapult, sector deals")

add("Catapult Centre Model", "キャタパルト・センター・モデル",
    "英国がフラウンホーファーモデルを参考に設立した技術・イノベーション拠点ネットワーク。産学間の「死の谷」を架橋し、高付加価値製造、衛星応用、エネルギーシステム等の分野で応用研究・実証を促進する。",
    "産学間の技術移転ギャップを架橋する拠点型イノベーション政策。", "知識移転", 2011, None, "institutional,policy", "policy,learning",
    ["Innovate UK", "Hermann Hauser"], ["Hauser (2010) The Current and Future Role of Technology and Innovation Centres"], "",
    "キャタパルト,技術イノベーション拠点,死の谷", "Catapult centre, technology innovation centre, valley of death")

# More entries covering measurement frontier topics
add("Satellite Data for Innovation Measurement", "イノベーション測定のための衛星データ",
    "夜間光画像、建設活動、農業変化等の衛星データを用いて、経済活動とイノベーションの空間的パターンを非伝統的方法で測定する手法。統計インフラが脆弱な途上国での経済・イノベーション活動の代理変数として活用。",
    "非伝統的データソースによるイノベーション活動の空間的把握。", "イノベーション計量学", 2012, None, "measurement", "learning",
    ["J. Vernon Henderson", "Adam Storeygard"], ["Henderson et al. (2012) Measuring Economic Growth from Outer Space"], "",
    "衛星データ,夜間光,非伝統的測定", "satellite data, nighttime lights, non-traditional measurement")

add("Blockchain for Research Governance", "研究ガバナンスのためのブロックチェーン",
    "研究成果の記録・追跡、ピアレビューの透明化、研究資金の配分管理等にブロックチェーン技術を活用する新しいアプローチ。研究不正の防止、再現性の向上、研究者の貢献の正確な記録を可能にする。",
    "ブロックチェーンによる研究プロセスの透明性・信頼性向上。", "イノベーション政策", 2017, None, "institutional", "learning",
    ["Joris van Rossum"], ["van Rossum (2017) Blockchain for Research"], "",
    "ブロックチェーン,研究ガバナンス,透明性", "blockchain, research governance, transparency, reproducibility")

add("AI for Science Policy Intelligence", "科学政策インテリジェンスのためのAI",
    "自然言語処理、機械学習、知識グラフ等のAI技術を用いて、大量の科学技術文書（論文、特許、政策文書等）から政策的に有用な情報を自動抽出・分析する手法。政策立案者の情報処理能力を拡張する。",
    "AI技術による科学技術政策インテリジェンスの自動化。", "イノベーション計量学", 2018, None, "measurement", "learning",
    ["JRC", "OECD AI Policy Observatory"], ["OECD.AI Policy Observatory Reports"], "",
    "AI政策インテリジェンス,NLP,知識グラフ", "AI policy intelligence, NLP, knowledge graph, automated analysis")

add("Responsible AI Innovation Policy", "責任あるAIイノベーション政策",
    "AI技術の開発・展開において、公平性、透明性、説明可能性、プライバシー、安全性等の倫理的原則を制度的に担保しつつイノベーションを促進する政策枠組み。EU AI Act、OECD AI Principles等が代表的。",
    "AI倫理とイノベーション促進を両立する政策枠組み。", "イノベーション政策", 2019, None, "policy,institutional", "policy",
    ["OECD", "European Commission", "IEEE"], ["OECD AI Principles (2019)", "EU AI Act (2024)"], "",
    "責任あるAI,AI倫理,AI規制", "responsible AI, AI ethics, AI regulation, trustworthy AI")

add("Quantum Technology Innovation Policy", "量子技術イノベーション政策",
    "量子コンピューティング、量子通信、量子センシング等の量子技術の研究開発・産業化を促進する国家戦略。米国National Quantum Initiative（2018年）、EU Quantum Flagship等の大規模プログラムが代表的。",
    "量子技術の戦略的育成のための国家イノベーション政策。", "イノベーション政策", 2018, None, "policy,institutional", "policy",
    ["US Congress", "European Commission"], ["National Quantum Initiative Act (2018)"], "",
    "量子技術,量子コンピューティング,国家戦略", "quantum technology, quantum computing, national strategy, quantum flagship")

add("Biotechnology Innovation Governance", "バイオテクノロジー・イノベーション・ガバナンス",
    "遺伝子編集（CRISPR等）、合成生物学、バイオ製造等のバイオテクノロジーイノベーションの規制・倫理・安全性ガバナンス。技術の急速な進歩に対して、適応的な規制枠組みとリスク評価方法論の開発が課題。",
    "バイオテクノロジーの急速な進歩に対応する適応的ガバナンス。", "イノベーション政策", 2015, None, "policy,institutional", "policy",
    ["National Academies of Sciences", "Nuffield Council on Bioethics"], ["NAS (2017) Human Genome Editing"], "",
    "バイオテクノロジー,CRISPR,合成生物学,規制", "biotechnology, CRISPR, synthetic biology, regulatory governance")

add("Space Innovation Policy", "宇宙イノベーション政策",
    "宇宙産業のイノベーション促進のための政策枠組み。ニュースペース企業の参入促進、宇宙デブリ管理、衛星データ活用、国際協力等を含み、SpaceX等の民間参入が政策パラダイムを変革。",
    "宇宙産業の民間イノベーション促進の政策枠組み。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["NASA", "ESA", "OECD"], ["OECD (2014) The Space Economy at a Glance"], "",
    "宇宙イノベーション,ニュースペース,衛星データ", "space innovation, NewSpace, satellite data, commercial space")

add("Energy Innovation Policy", "エネルギーイノベーション政策",
    "クリーンエネルギー技術（太陽光、風力、蓄電池、水素等）の研究開発・実証・普及を促進する包括的政策枠組み。R&D投資、炭素価格付け、規制、FIT/RPS等の政策ミックスによるエネルギー転換の加速を目指す。",
    "エネルギー転換のためのイノベーション政策ミックス。", "イノベーション政策", 2005, None, "policy,systemic", "policy",
    ["IEA", "IRENA", "Mission Innovation"], ["IEA Energy Technology Perspectives"], "",
    "エネルギーイノベーション,クリーンエネルギー,エネルギー転換", "energy innovation, clean energy, energy transition, Mission Innovation")

add("Health Innovation Policy", "ヘルスイノベーション政策",
    "医薬品、医療機器、デジタルヘルス、精密医療等の保健医療分野のイノベーションを促進する政策体系。薬事規制、価格・償還制度、臨床試験枠組み、データ活用規制等の多層的な制度環境がイノベーション・インセンティブを形成する。",
    "保健医療イノベーションの多層的制度環境の政策設計。", "イノベーション政策", 2000, None, "policy,institutional", "policy",
    ["OECD", "WHO"], ["OECD Health Innovation Policy"], "",
    "ヘルスイノベーション,医薬品規制,デジタルヘルス", "health innovation, pharmaceutical regulation, digital health, precision medicine")

add("Agricultural Innovation System (AIS)", "農業イノベーションシステム",
    "農業分野のイノベーション促進に関わるアクター（農家、研究機関、普及サービス、企業等）とその相互作用を分析する枠組み。従来の線形的な技術普及モデルを超え、システミックなアプローチで農業革新を促進する。",
    "農業分野のイノベーション・ガバナンスの枠組み。", "イノベーションシステム論", 2006, None, "systemic,policy", "policy,learning",
    ["World Bank", "FAO", "Andy Hall"], ["World Bank (2012) Agricultural Innovation Systems"], "",
    "農業イノベーション,AIS,技術普及,農業研究", "agricultural innovation system, AIS, extension, agricultural research")

add("Creative Industries Innovation Policy", "クリエイティブ産業イノベーション政策",
    "デザイン、メディア、ゲーム、広告、建築等のクリエイティブ産業のイノベーション活動を促進する政策体系。文化的価値と経済的価値の二重性、小規模事業者の多さ、著作権中心のIP構造等の特殊性に対応する政策設計。",
    "クリエイティブ産業固有のイノベーション特性に対応した政策。", "イノベーション政策", 2001, None, "policy,institutional", "policy,learning",
    ["DCMS UK", "Nesta", "Richard Florida"], ["DCMS (2001) Creative Industries Mapping Document"], "",
    "クリエイティブ産業,文化産業,デザイン政策", "creative industries, cultural industries, design policy, creative economy")

add("Innovation in Informal Economy", "インフォーマル経済におけるイノベーション",
    "公式な統計に捕捉されないインフォーマル・セクターにおけるイノベーション活動の分析と測定。途上国では経済活動の大半がインフォーマル・セクターで行われており、その革新的活動の認識と支援が政策課題となる。",
    "インフォーマル・セクターの革新的活動の認識と測定。", "イノベーション計量学", 2010, None, "measurement,policy", "policy,learning",
    ["OECD", "UNCTAD"], ["OECD/UNCTAD Informal Economy and Innovation Studies"], "",
    "インフォーマル経済,非公式イノベーション,途上国", "informal economy, informal innovation, developing countries")

add("Innovation and Inequality", "イノベーションと格差",
    "技術的イノベーション（特にAI・自動化）が所得格差、地域格差、デジタルデバイドに与える影響の分析と政策的対応。イノベーションの便益の偏在、スキル偏向的技術変化、勝者総取り市場の形成等の構造的問題。",
    "イノベーションの分配的影響と政策的対応の分析。", "イノベーション政策", 2014, None, "policy,systemic", "policy",
    ["Daron Acemoglu", "David Autor", "OECD"], ["Acemoglu & Restrepo (2019) Automation and New Tasks"], "",
    "イノベーションと格差,自動化,スキル偏向", "innovation and inequality, automation, skill-biased technical change")

add("Open Strategic Autonomy in Innovation", "イノベーションにおけるオープン戦略的自律性",
    "グローバルなサプライチェーン依存リスクを軽減しつつ、国際的な技術協力のメリットを維持する政策バランス。半導体、レアアース、医薬品等の戦略的技術における自律性確保とイノベーションの開放性の両立を図る。",
    "技術的自律性と国際協力のバランスを図る政策概念。", "イノベーション政策", 2020, None, "policy,institutional", "policy",
    ["European Commission"], ["EU Strategic Autonomy Communication"], "",
    "戦略的自律性,テクノナショナリズム,サプライチェーン", "strategic autonomy, techno-nationalism, supply chain, decoupling")

add("Standards and Innovation", "標準化とイノベーション",
    "技術標準がイノベーションの方向性、速度、競争構造に与える影響の分析。標準化はイノベーションの普及を促進する一方、ロックイン効果により代替技術の発展を阻害しうる二面性を持つ。",
    "技術標準のイノベーション促進・阻害の二面的影響分析。", "イノベーション政策", 1985, None, "policy,institutional", "policy,learning",
    ["Paul David", "Brian Arthur", "Knut Blind"], ["Blind (2004) The Economics of Standards"], "de facto standards",
    "標準化,ロックイン,互換性,技術選択", "standardization, lock-in, compatibility, technology choice")

add("Competition Policy and Innovation", "競争政策とイノベーション",
    "独占禁止政策、合併審査、知的財産権の行使制限等の競争政策がイノベーション・インセンティブに与える影響の分析。シュンペーター仮説（市場支配力がイノベーションを促進）とアロー仮説（競争がイノベーションを促進）の論争が核心。",
    "競争と市場構造がイノベーション・インセンティブに与える影響。", "イノベーション政策", 1962, None, "policy,institutional", "policy,learning",
    ["Kenneth Arrow", "Joseph Schumpeter", "Philippe Aghion"], ["Aghion et al. (2005) Competition and Innovation"], "",
    "競争政策,独占禁止,シュンペーター仮説", "competition policy, antitrust, Schumpeter hypothesis, Arrow's replacement effect")

add("Trade Policy and Innovation", "貿易政策とイノベーション",
    "貿易自由化、関税政策、輸出促進が国内企業のイノベーション活動に与える影響の分析。輸入競争による効率化圧力、輸出市場へのアクセスによる規模効果、技術移転チャネルとしての貿易の三つの経路を検証する。",
    "貿易政策のイノベーション促進メカニズムの分析。", "イノベーション政策", 1990, None, "policy", "policy,learning",
    ["Gene Grossman", "Elhanan Helpman"], ["Grossman & Helpman (1991) Innovation and Growth in the Global Economy"], "",
    "貿易政策,輸入競争,輸出促進,技術移転", "trade policy, import competition, export promotion, technology transfer")

add("Education Policy for Innovation", "イノベーションのための教育政策",
    "STEM教育、起業家教育、創造性教育、生涯学習等のイノベーション人材育成のための教育政策体系。イノベーション能力の基盤となる人的資本の質と量を確保し、社会全体のイノベーション能力を高める。",
    "イノベーション人材育成の教育政策。", "イノベーション政策", 2000, None, "policy", "policy,learning",
    ["OECD", "European Commission"], ["OECD Innovation Strategy: Education and Training"], "",
    "教育政策,STEM,起業家教育,人的資本", "education policy, STEM, entrepreneurship education, human capital")

add("Migration Policy and Innovation", "移民政策とイノベーション",
    "高技能移民の誘致がイノベーション・パフォーマンスに与える影響の分析と政策設計。特許生産性への移民の寄与、国際的な知識ネットワークの構築、頭脳流出/頭脳循環の動態等を実証的に検証する。",
    "高技能移民によるイノベーション能力強化の政策設計。", "イノベーション政策", 2000, None, "policy", "policy,learning",
    ["William Kerr", "AnnaLee Saxenian"], ["Kerr & Lincoln (2010) The Supply Side of Innovation"], "",
    "移民政策,高技能人材,頭脳循環", "migration policy, high-skilled workers, brain circulation, talent attraction")

add("Financial System and Innovation", "金融システムとイノベーション",
    "銀行中心型と市場中心型の金融システムがイノベーションの種類と量に与える差異の分析。市場型金融は急進的イノベーションを、銀行型金融は漸進的イノベーションを相対的に促進するという仮説の実証的検証。",
    "金融システムの構造がイノベーション・パターンに与える影響。", "イノベーション政策", 2002, None, "policy,institutional", "policy,learning",
    ["Ross Levine", "Thorsten Beck", "Asli Demirgüç-Kunt"], ["Levine (2005) Finance and Growth"], "",
    "金融システム,銀行型vs市場型,イノベーション資金", "financial system, bank-based vs market-based, innovation finance")

add("Labor Market Policy and Innovation", "労働市場政策とイノベーション",
    "雇用保護法制、非競争条項、労働市場の流動性がイノベーション活動に与える影響の分析。シリコンバレーのカリフォルニア州非競争条項禁止とイノベーション優位の関係（Gilson, 1999）が象徴的事例。",
    "労働市場制度がイノベーション・ダイナミクスに与える影響。", "イノベーション政策", 1999, None, "policy,institutional", "policy,learning",
    ["Ronald Gilson", "Matt Marx"], ["Gilson (1999) The Legal Infrastructure of High Technology Industrial Districts"], "",
    "労働市場政策,非競争条項,人材流動性", "labor market policy, non-compete, talent mobility, employment protection")

add("Gender and Innovation Policy", "ジェンダーとイノベーション政策",
    "イノベーション・プロセスにおけるジェンダー格差（女性研究者・発明者・起業家の過少代表、資金アクセスの格差等）を是正する政策。ジェンダー主流化アプローチにより、イノベーション政策全体にジェンダー視点を統合する。",
    "イノベーション・プロセスのジェンダー格差是正政策。", "イノベーション政策", 2010, None, "policy", "policy",
    ["European Commission", "OECD"], ["OECD (2017) The Pursuit of Gender Equality"], "",
    "ジェンダー,女性起業家,ジェンダー主流化", "gender, women entrepreneurs, gender mainstreaming, innovation equity")

# Continue to 714
add("Indicator Governance Framework", "指標ガバナンス枠組み",
    "イノベーション指標の収集・公表・使用に関する品質管理とガバナンス体制の設計。データの正確性、適時性、比較可能性、アクセシビリティを保証し、指標の政策的誤用を防止する制度的枠組み。",
    "イノベーション指標の品質管理とガバナンス制度。", "イノベーション計量学", 2010, None, "measurement,policy", "policy",
    ["OECD", "Eurostat"], ["European Statistics Code of Practice"], "",
    "指標ガバナンス,品質管理,統計ガバナンス", "indicator governance, quality management, statistical governance")

add("Innovation Expenditure by Firm Size", "企業規模別イノベーション支出",
    "大企業、中堅企業、中小企業のイノベーション投資パターンの差異を分析する指標体系。中小企業の「隠れたイノベーション」（非R&D型）を適切に捕捉するための測定方法論的改善を含む。",
    "企業規模別のイノベーション投資パターンの分析。", "イノベーション計量学", 2000, None, "measurement", "learning",
    ["Eurostat", "OECD"], ["CIS Size Class Analysis"], "",
    "企業規模別,中小企業イノベーション,非R&D投資", "firm size, SME innovation, non-R&D investment, size-class analysis")

add("Cross-Border Innovation Measurement", "越境イノベーション測定",
    "多国籍企業のR&D国際化、国際共同発明（国際共同特許）、国際共著論文等の国境を越えるイノベーション活動を測定する方法論。グローバル・バリューチェーンにおけるイノベーションの国際的分業パターンを把握する。",
    "イノベーションのグローバル化を定量的に把握する測定手法。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["OECD", "Guellec & van Pottelsberghe"], ["OECD (2008) The Internationalisation of Business R&D"], "",
    "越境イノベーション,R&D国際化,国際共同発明", "cross-border innovation, R&D internationalization, international co-invention")

add("University Performance Metrics", "大学パフォーマンス指標",
    "大学の研究、教育、社会貢献（第三の使命）のパフォーマンスを測定・比較する指標体系。世界大学ランキング（THE、QS、ARWU）や各国の大学評価制度が代表的で、イノベーション貢献の測定を含む。",
    "大学の多面的パフォーマンスの定量的評価と比較。", "イノベーション計量学", 2003, None, "measurement,institutional", "policy,learning",
    ["Times Higher Education", "QS", "Jiao Tong University"], ["THE World University Rankings Methodology"], "",
    "大学パフォーマンス,大学ランキング,第三の使命", "university performance, university ranking, third mission, research excellence")

add("Technology Convergence Indicators", "技術融合指標",
    "異なる技術分野の特許が相互に引用し合う頻度や、複数のIPC分類にまたがる特許の出願パターン等から、技術融合のトレンドと程度を測定する指標。IT×バイオ、ナノ×材料等の融合領域の発展を定量的に追跡する。",
    "技術分野間の融合トレンドの定量的追跡。", "イノベーション計量学", 2008, None, "measurement", "learning",
    ["Koen Frenken", "Martin Curran"], ["Curran & Leker (2011) Patent indicators for monitoring convergence"], "",
    "技術融合,分野横断特許,融合指標", "technology convergence, cross-field patents, convergence indicators")

add("Innovation and Sustainability Measurement", "イノベーションと持続可能性の測定",
    "SDGs達成に貢献するイノベーション活動の測定と評価。環境イノベーション、社会イノベーション、包摂的イノベーションの各次元で、持続可能性への寄与度を定量化する方法論の開発。",
    "持続可能性に寄与するイノベーションの測定方法論。", "イノベーション計量学", 2015, None, "measurement,policy", "policy,learning",
    ["OECD", "UNCTAD"], ["OECD Green Growth Indicators"], "",
    "持続可能性,SDGs,グリーンイノベーション測定", "sustainability, SDGs, green innovation measurement, inclusive innovation")

add("Creative Destruction Measurement", "創造的破壊の測定",
    "シュンペーター的な創造的破壊プロセスを企業の参入・退出データ、産業構造変化、ジョブ・フロー等の統計から定量的に測定する方法論。イノベーション・ダイナミクスの実態をマクロ・ミクロの両レベルで把握する。",
    "シュンペーター的創造的破壊の定量的測定手法。", "イノベーション計量学", 1996, None, "measurement", "learning",
    ["Joseph Schumpeter", "Steven Davis", "John Haltiwanger"], ["Davis, Haltiwanger & Schuh (1996) Job Creation and Destruction"], "",
    "創造的破壊,企業参入退出,ジョブフロー", "creative destruction, firm entry-exit, job flow, industry dynamics")

add("Venture Capital Performance Metrics", "ベンチャーキャピタル・パフォーマンス指標",
    "VC投資のリターン（IRR、TVPI、DPI等）、ポートフォリオ企業の成長（ユニコーン率、IPO率、M&A率）、エコシステムへの波及効果を測定する指標群。VC市場の健全性評価と政策効果測定に活用。",
    "VC投資の成果とエコシステム波及効果の測定。", "イノベーション計量学", 2000, None, "measurement", "policy,learning",
    ["NVCA", "Cambridge Associates"], ["Cambridge Associates Venture Capital Index"], "",
    "VCパフォーマンス,IRR,ユニコーン率", "VC performance, IRR, unicorn rate, portfolio metrics")

add("Open Data Policy for Innovation", "イノベーションのためのオープンデータ政策",
    "政府・公共機関が保有するデータの公開（オープンガバメントデータ）をイノベーション促進のために制度化する政策。データの発見可能性、機械可読性、ライセンスの明確化等の技術的・制度的条件を整備する。",
    "公共データの開放によるイノベーション基盤の構築。", "イノベーション政策", 2009, None, "policy,institutional", "policy,learning",
    ["US Government (data.gov)", "European Commission"], ["EU Open Data Directive"], "",
    "オープンデータ,オープンガバメント,データ活用", "open data, open government, data utilization, machine-readable data")

add("Technology Sovereignty", "技術主権",
    "戦略的に重要な技術（半導体、AI、量子、バイオ等）の開発・製造能力を国内・同盟国内に確保する政策概念。COVID-19パンデミックとUS-中国技術競争を契機に、サプライチェーンの強靭性とイノベーション自律性の確保が緊急課題に。",
    "戦略的技術のイノベーション・サプライチェーン自律性の確保。", "イノベーション政策", 2020, None, "policy,institutional", "policy",
    ["European Commission"], ["EU Chips Act", "EU Critical Raw Materials Act"], "",
    "技術主権,半導体,サプライチェーン強靭性", "technology sovereignty, semiconductors, supply chain resilience, strategic autonomy")

add("Innovation and Climate Policy Integration", "イノベーション・気候政策統合",
    "気候変動政策（炭素価格付け、規制基準、排出取引）とイノベーション政策（R&D支援、技術実証、市場形成）の統合的設計。Acemoglu et al.（2012年）が両政策の補完性を理論的に実証し、統合アプローチの必要性を確立。",
    "気候政策とイノベーション政策の統合的設計の理論的基盤。", "イノベーション政策", 2012, None, "policy,systemic", "policy",
    ["Daron Acemoglu", "Philippe Aghion", "IEA"], ["Acemoglu et al. (2012) The Environment and Directed Technical Change"], "",
    "気候イノベーション統合,炭素価格,方向付き技術変化", "climate-innovation integration, carbon pricing, directed technical change")

add("Pandemic Preparedness Innovation Policy", "パンデミック備えのイノベーション政策",
    "COVID-19の教訓を踏まえた、感染症対策技術（ワクチン、診断薬、治療薬、PPE等）の迅速な開発・生産・供給を確保するためのイノベーション政策枠組み。CEPI、BARDA等の事前準備機関と緊急時のイノベーション加速メカニズム。",
    "パンデミック対応技術の迅速なイノベーション確保。", "イノベーション政策", 2020, None, "policy,institutional", "policy",
    ["CEPI", "BARDA", "WHO"], ["100 Days Mission (CEPI)"], "",
    "パンデミック備え,CEPI,ワクチン開発,緊急イノベーション", "pandemic preparedness, CEPI, vaccine development, emergency innovation")

add("Innovation in Developing Country Agriculture", "途上国農業におけるイノベーション",
    "開発途上国の小規模農業における技術・組織・制度イノベーションの測定と促進。CGIAR（国際農業研究協議グループ）の品種改良、気候スマート農業、デジタル農業拡張等の成果評価を含む。",
    "途上国小規模農業のイノベーション促進と成果評価。", "イノベーション政策", 2000, None, "policy,measurement", "policy,learning",
    ["CGIAR", "FAO", "World Bank"], ["CGIAR Research Programs Impact Assessments"], "",
    "途上国農業,CGIAR,気候スマート農業", "developing country agriculture, CGIAR, climate-smart agriculture")

add("Digital Transformation Index", "デジタル変革指数",
    "企業・産業・国レベルのデジタルトランスフォーメーションの進展度を測定する複合指標。デジタル技術の導入率、デジタルスキル、データ活用、ビジネスモデル変革等の多次元でDXの進捗を評価する。",
    "デジタルトランスフォーメーションの進展度の多次元的評価。", "イノベーション計量学", 2017, None, "measurement", "policy,learning",
    ["McKinsey", "European Commission", "World Economic Forum"], ["EU DESI Reports", "McKinsey Digital Index"], "",
    "DX指数,デジタル変革測定,DX進捗評価", "digital transformation index, DX measurement, digitalization progress")

add("R&D Globalization Measurement", "研究開発グローバル化の測定",
    "多国籍企業のR&D拠点の国際的配置、国際共同研究プロジェクト、研究者の国際流動性等のR&D活動のグローバル化パターンを測定する方法論。R&Dの海外支出比率、国際共同特許率等が主要指標。",
    "R&D活動の国際化パターンの定量的把握。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["OECD", "UNCTAD"], ["OECD Internationalisation of R&D Statistics"], "",
    "R&Dグローバル化,海外R&D,国際共同研究", "R&D globalization, overseas R&D, international collaboration")

add("Smart City Innovation Metrics", "スマートシティ・イノベーション指標",
    "都市のスマート化（IoT、データ活用、市民参加、持続可能性等）におけるイノベーション活動と成果を測定する指標体系。IMDスマートシティ指標やEU Smart Cities指標が代表的で、都市イノベーション政策の基盤データを提供。",
    "都市レベルのスマート・イノベーション活動の測定。", "イノベーション計量学", 2014, None, "measurement,policy", "policy,learning",
    ["IMD", "European Commission"], ["IMD Smart City Index"], "",
    "スマートシティ指標,都市イノベーション,IoT", "smart city metrics, urban innovation, IoT, data-driven city")

add("Frugal Innovation Measurement", "フルーガル・イノベーションの測定",
    "資源制約下での低コスト・高機能イノベーションの発生頻度、影響範囲、経済的価値を測定する方法論。従来のR&D集約度ベースの指標では捕捉しにくいイノベーション形態の可視化を目指す。",
    "資源制約型イノベーションの定量的測定方法論。", "イノベーション計量学", 2015, None, "measurement", "learning",
    ["Jaideep Prabhu", "OECD"], ["OECD Frugal Innovation Studies"], "",
    "フルーガルイノベーション測定,低コスト革新,資源制約", "frugal innovation measurement, low-cost innovation, resource constraint")

add("Platform Innovation Measurement", "プラットフォーム・イノベーション測定",
    "デジタルプラットフォーム上のイノベーション活動（アプリ開発、APIエコシステム、補完的イノベーション等）を測定する方法論。プラットフォームの価値創出メカニズムと参加者のイノベーション活動を定量化する。",
    "プラットフォーム・エコシステムのイノベーション活動の測定。", "イノベーション計量学", 2015, None, "measurement", "learning",
    ["Annabelle Gawer", "Michael Cusumano"], ["Gawer & Cusumano (2014) Industry Platforms and Ecosystem Innovation"], "",
    "プラットフォーム測定,エコシステム,補完的革新", "platform measurement, ecosystem, complementary innovation, API economy")

add("Intangible Asset Measurement", "無形資産の測定",
    "R&D、ソフトウェア、デザイン、ブランド、組織資本、人的資本等の無形資産への投資を体系的に測定する方法論。Corrado, Hulten & Sichel (2005)のフレームワークが先駆的で、GDPに計上されない「隠れた投資」の全体像を把握する。",
    "知識経済における「見えない」投資の体系的測定。", "イノベーション計量学", 2005, None, "measurement", "learning",
    ["Carol Corrado", "Charles Hulten", "Daniel Sichel"], ["Corrado, Hulten & Sichel (2005) Measuring Capital and Technology"], "",
    "無形資産,知識資本,非R&D投資", "intangible assets, knowledge capital, non-R&D investment, hidden investment")

add("Innovation and Productivity Nexus", "イノベーションと生産性の連結",
    "イノベーション活動が企業・産業・国レベルの生産性向上に寄与するメカニズムと程度を実証的に分析する研究領域。CDMモデル（Crépon, Duguet & Mairesse, 1998）が標準的な計量分析枠組みを提供。",
    "イノベーションから生産性への因果的連結の実証分析。", "イノベーション計量学", 1998, None, "measurement", "learning",
    ["Bruno Crépon", "Emmanuel Duguet", "Jacques Mairesse"], ["Crépon, Duguet & Mairesse (1998) CDM Model"], "",
    "イノベーションと生産性,CDMモデル,因果分析", "innovation-productivity nexus, CDM model, causal analysis")

add("Multi-Level Innovation Policy Governance", "多層的イノベーション政策ガバナンス",
    "超国家（EU）、国家、地域、都市の各レベルのイノベーション政策間の垂直的調整と補完性の確保を図るガバナンス体制。政策の重複・矛盾を避け、各レベルの比較優位を活かした役割分担を設計する。",
    "多層的な政策体系間の垂直的調整と補完性の確保。", "イノベーション政策", 2010, None, "policy,institutional", "policy",
    ["OECD", "European Commission"], ["OECD Multi-level Governance Studies"], "",
    "多層ガバナンス,政策調整,垂直的補完性", "multi-level governance, policy coordination, vertical complementarity")

add("Innovation and Well-being Measurement", "イノベーションとウェルビーイングの測定",
    "イノベーション活動が物質的生活水準を超えた幅広いウェルビーイング（健康、環境、社会的つながり、主観的幸福等）に与える影響を測定する方法論。GDPを超える進歩の測定の一環としてOECD Better Life Indexとの接続を図る。",
    "イノベーションのウェルビーイングへの寄与の測定。", "イノベーション計量学", 2011, None, "measurement,policy", "policy,learning",
    ["OECD", "Joseph Stiglitz"], ["OECD Better Life Index", "Stiglitz, Sen & Fitoussi (2009) Report"], "",
    "ウェルビーイング,GDP以外の進歩,生活の質", "well-being, beyond GDP, quality of life, innovation impact")

# Final batch for exactly reaching 714
add("Foresight for Innovation Policy", "イノベーション政策のためのフォーサイト",
    "長期的な社会・技術・経済のトレンドを体系的に分析し、イノベーション政策の方向性設定に活用するプロセス。シナリオ分析、バックキャスティング、参加型フォーサイト等の手法をイノベーション政策の文脈に統合する。",
    "長期的な政策方向性設定のためのフォーサイト方法論。", "技術フォーサイト", 2000, None, "policy,measurement", "policy,learning",
    ["OECD", "European Commission", "European Foresight Platform"], ["EU Foresight for Innovation Policy Reports"], "",
    "フォーサイト,シナリオ分析,政策方向性", "foresight, scenario analysis, policy direction, long-term planning")

add("Innovation Policy Learning", "イノベーション政策学習",
    "他国・他地域のイノベーション政策経験から体系的に学習し、自国の政策改善に活かすプロセス。単純な「ベストプラクティス」の移植ではなく、文脈適応的な政策移転と実験的学習を重視する。",
    "国際的な政策経験からの体系的学習プロセス。", "イノベーション政策", 2008, None, "policy", "policy,learning",
    ["OECD", "David Dolowitz", "David Marsh"], ["Dolowitz & Marsh (2000) Learning from Abroad"], "",
    "政策学習,政策移転,ベストプラクティス", "policy learning, policy transfer, best practice, contextual adaptation")

add("Behavioural Insights for Innovation Policy", "イノベーション政策のための行動インサイト",
    "行動経済学・行動科学の知見をイノベーション政策の設計に適用するアプローチ。ナッジ、デフォルト設計、フレーミング効果等を用いて、R&D投資、技術採用、起業行動等の意思決定を政策的に誘導する。",
    "行動科学に基づくイノベーション政策設計。", "イノベーション政策", 2015, None, "policy", "policy,learning",
    ["Nesta", "OECD", "Behavioural Insights Team"], ["OECD (2017) Behavioural Insights and Public Policy"], "",
    "行動インサイト,ナッジ,行動経済学", "behavioural insights, nudge, behavioural economics, policy design")

# Save to JSON files (50 per file)
output_dir = os.path.dirname(os.path.abspath(__file__))
total = len(entries)
print(f"Total entries generated (batch 2): {total}")

for batch_idx in range(0, total, 50):
    batch = entries[batch_idx:batch_idx+50]
    batch_num = batch_idx // 50 + 4  # Continue from batch 4
    filepath = os.path.join(output_dir, f"pol_batch_{batch_num}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)
    print(f"Written {len(batch)} entries to {filepath} (IDs: {batch[0]['id']} - {batch[-1]['id']})")
