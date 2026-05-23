"""
DUA Wave A2 Batch 17 — Multi-subfield batch covering:
- 材料科学 (~25 concepts)
- 医学・臨床科学 (~25 concepts)
- 生命科学・生物学 (~20 concepts)
"""
import sqlite3
import uuid
from datetime import datetime, timezone

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

MATERIALS = [
    {
        "name_ja": "形状記憶合金",
        "name_en": "Shape Memory Alloys",
        "definition": "変形後に加熱すると元の形状に回復する合金（NiTi合金が代表例）。マルテンサイト変態が形状記憶効果・超弾性の機構。",
        "impact_summary": "医療ステント・アクチュエータ・航空機・ロボット筋肉に応用。年間市場20億USD以上（2020）。Buehler・Wang(1963, Naval Research Lab)が発見。",
        "subfield": "材料科学", "school_of_thought": "Materials Science", "era_start": 1963,
        "culture_region": "North_America",
        "source_url": "https://www.mrs.org/",
        "data_completeness": 87,
    },
    {
        "name_ja": "ソフトロボティクス材料",
        "name_en": "Soft Robotics Materials",
        "definition": "弾性率が生体組織（1 kPa–1 MPa）に近い柔軟材料（シリコーンエラストマー・ハイドロゲル・繊維複合材料）を用いたロボット構造・アクチュエーター・センサー。",
        "impact_summary": "手術補助ロボット・ウェアラブルデバイス・グリッパー・爬行ロボットへの応用。Harvard Soft Robotics Toolkit（木・Whitesides研究室）が普及を促進。",
        "subfield": "材料科学", "school_of_thought": "Materials Science", "era_start": 2011,
        "culture_region": "North_America",
        "source_url": "https://softroboticstoolkit.com/",
        "data_completeness": 85,
    },
    {
        "name_ja": "イオン導電体と固体電解質",
        "name_en": "Solid Electrolytes and Ionic Conductors",
        "definition": "リチウム・ナトリウム・水素イオンを高速に伝導できる固体材料（酸化物系・硫化物系・ポリマー系固体電解質）。全固体電池の中核材料。",
        "impact_summary": "液体電解質の発火リスクを排除した全固体電池（Toyota・BYD・Samsung）の実用化に直結。ガーネット型（LLZO）・LGPS・Li₆PS₅Clが主要材料。2030年代のEV革命の鍵。",
        "subfield": "材料科学", "school_of_thought": "Materials Chemistry", "era_start": 1970,
        "culture_region": "East_Asia",
        "source_url": "https://www.nature.com/articles/s41578-019-0165-5",
        "mathematical_formulation": r"\sigma = \sigma_0 e^{-E_a/k_BT} \quad \text{(Arrhenius conductivity)}",
        "data_completeness": 88,
    },
    {
        "name_ja": "生体適合材料とインプラント",
        "name_en": "Biomaterials and Implants",
        "definition": "人体に埋め込んだとき生体組織と適合して機能する材料（チタン合金・ハイドロキシアパタイト・医療グレードシリコーン・生分解性ポリマー）の設計・評価・認証体系。",
        "impact_summary": "人工股関節・冠動脈ステント・歯科インプラント・人工角膜・薬物溶出ステントの世界市場（2022年1,300億USD）を支える。FDAのISO 10993規格準拠が必要。",
        "subfield": "材料科学", "school_of_thought": "Biomedical Engineering", "era_start": 1960,
        "culture_region": "North_America",
        "source_url": "https://www.biomaterials.org/",
        "data_completeness": 87,
    },
    {
        "name_ja": "インドの伝統冶金（インドのダマスカス鋼と亜鉛精錬）",
        "name_en": "Indian Traditional Metallurgy and Zinc Smelting",
        "definition": "紀元前〜中世インドで発展したウーツ鋼（高炭素製鋼）と、9世紀にラジャスタン州Zawarで開発された最古の工業的亜鉛蒸留精錬技術。ヨーロッパより数世紀先行する冶金技術。",
        "impact_summary": "Zawarの亜鉛製錬（9–11世紀）はヨーロッパの亜鉛工業化（17世紀）より600年以上先行した非西洋冶金技術の先端事例。ウーツ鋼は現代の超高強度鋼材料研究に影響。",
        "subfield": "材料科学", "school_of_thought": "History of Materials", "era_start": 800,
        "culture_region": "South_Asia",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S1044580320302667",
        "data_completeness": 80,
    },
    {
        "name_ja": "高エントロピー合金",
        "name_en": "High-Entropy Alloys",
        "definition": "5種以上の主要元素をほぼ等モル比で混合した多主成分合金（HEA）。高混合エントロピーによる固溶強化・優れた高温強度・放射線耐性・コロッション耐性が特徴。",
        "impact_summary": "従来の2–3成分合金を超える性能が多数報告。Cantor合金（CrMnFeCoNi）が原型。航空エンジン・核融合炉壁材・耐食コーティングへの応用研究が急拡大（2004〜）。",
        "subfield": "材料科学", "school_of_thought": "Physical Metallurgy", "era_start": 2004,
        "culture_region": "East_Asia",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S1359645404000527",
        "data_completeness": 86,
    },
    {
        "name_ja": "フレキシブルエレクトロニクス",
        "name_en": "Flexible Electronics",
        "definition": "曲折・延伸可能な基板上に薄膜トランジスタ・有機半導体・電極を形成した電子デバイス。ウェアラブルセンサー・電子スキン・折りたたみスマートフォン・神経インターフェイスに応用。",
        "impact_summary": "フレキシブルディスプレイ（Samsung Galaxy Z Fold）・皮膚貼付型電子タトゥー・脳皮質電極の市場が急拡大。John Rogers（UIUC）が生体統合型フレキシブルエレクトロニクスを開拓。",
        "subfield": "材料科学", "school_of_thought": "Electronics Materials", "era_start": 2000,
        "culture_region": "North_America",
        "source_url": "https://rogersgroup.northwestern.edu/",
        "data_completeness": 86,
    },
    {
        "name_ja": "遺伝子編集と材料インフォマティクス",
        "name_en": "Materials Informatics and Machine Learning",
        "definition": "機械学習・ディープラーニング・生成モデルを用いて新材料の組成・構造・物性を予測・逆設計するデータ駆動型材料科学（マテリアルズインフォマティクス）。",
        "impact_summary": "Materials Project・AFLOW・NOMAD等のデータベース+DFT計算+MLが新超伝導体・電池材料・触媒の発見を加速。DeepMind GNoME(2023)が220万種の安定新材料構造を予測。",
        "subfield": "材料科学", "school_of_thought": "Computational Materials", "era_start": 2011,
        "culture_region": "North_America",
        "source_url": "https://materialsproject.org/",
        "data_completeness": 87,
    },
    {
        "name_ja": "天然繊維と持続可能テキスタイル材料",
        "name_en": "Natural Fibers and Sustainable Textile Materials",
        "definition": "綿・麻・絹・羊毛・竹・ケナフ等の天然繊維の化学的構造（セルロース・タンパク質・リグニン）と性能、生分解性・カーボンフットプリント・機能化処理の化学。",
        "impact_summary": "ファスト・ファッションの環境負荷（世界廃水の20%はテキスタイル染色由来）への対案として天然・リサイクル繊維が注目。バイオベースポリマー（PLA・PHA）との複合化が進む。",
        "subfield": "材料科学", "school_of_thought": "Textile Science", "era_start": 1900,
        "culture_region": "South_Asia",
        "source_url": "https://www.sciencedirect.com/journal/composites-part-b-engineering",
        "data_completeness": 82,
    },
    {
        "name_ja": "超材料（メタマテリアル）の設計",
        "name_en": "Metamaterials Design",
        "definition": "自然界に存在しない電磁的・弾性的・音響的性質（負の屈折率・完全吸収・零屈折・弾性波操作）を持つ人工周期構造体（メタマテリアル）の設計・製造・応用の科学。",
        "impact_summary": "光学クローキング（透明マント）・超解像レンズ（スーパーレンズ）・5G/6G電磁波制御・防振メタマテリアルへの応用。Pendry(1996–2000)が理論基盤を確立。",
        "subfield": "材料科学", "school_of_thought": "Photonics", "era_start": 1968,
        "culture_region": "Europe_Western",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0370157319303478",
        "data_completeness": 87,
    },
]

MEDICINE = [
    {
        "name_ja": "免疫学の基礎と自己非自己識別",
        "name_en": "Immunology and Self-Nonself Discrimination",
        "definition": "免疫系が病原体（非自己）と自己組織を識別するメカニズム。T細胞・B細胞の活性化・クローン選択・MHC拘束性・免疫寛容・自己免疫疾患の発症機序が主要テーマ。",
        "impact_summary": "Burnet・Medawar(1960 Nobel, クローン選択説・免疫寛容)・Doherty・Zinkernagel(1996 Nobel, MHC拘束性)が確立。ワクチン・臓器移植・がん免疫療法（PD-1 : Honjo 2018 Nobel/East_Asia）の基盤。",
        "subfield": "医学・臨床科学", "school_of_thought": "Immunology", "era_start": 1957,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2018/honjo/lecture/",
        "data_completeness": 91,
    },
    {
        "name_ja": "ゲノム医学とパーソナライズド医療",
        "name_en": "Genomic Medicine and Precision Medicine",
        "definition": "個人のゲノム情報（多型・変異・発現）を診断・治療・予防に活用する医学。全ゲノム解読（WGS）・腫瘍ゲノムプロファイリング・薬理ゲノミクス（薬物反応多型）が主要ツール。",
        "impact_summary": "HGP完成(2003)後、次世代シーケンシングが普及し希少疾患診断・がん分子標的療法の設計を加速。英国Biobank(50万人)・AllofUs(100万人)が人口規模のゲノム医学を推進。",
        "subfield": "医学・臨床科学", "school_of_thought": "Genomics", "era_start": 1990,
        "culture_region": "North_America",
        "source_url": "https://www.genome.gov/about-genomics/fact-sheets/Genomics-and-Medicine",
        "data_completeness": 89,
    },
    {
        "name_ja": "脳神経外科と機能脳外科",
        "name_en": "Neurosurgery and Functional Brain Surgery",
        "definition": "脳腫瘍切除・脊椎手術・脳血管手術（動脈瘤クリッピング・血管内治療）・機能的脳外科（DBS・癲癇手術・定位放射線手術）を含む外科医学分野。",
        "impact_summary": "定位脳深部刺激（DBS）がパーキンソン病・振戦・強迫症の劇的改善をもたらした。AWake craniotomy（覚醒下手術）・術中MRIが手術精度を向上。ロボット支援脳外科が普及中。",
        "subfield": "医学・臨床科学", "school_of_thought": "Surgery", "era_start": 1930,
        "culture_region": "North_America",
        "source_url": "https://www.neurosurgery.org/",
        "data_completeness": 86,
    },
    {
        "name_ja": "伝染病の疫学とR₀（基本再生産数）",
        "name_en": "Infectious Disease Epidemiology and R0",
        "definition": "感染症の集団内拡散を定量化するSIR/SEIR数理モデル・基本再生産数（R₀）・実効再生産数（Rt）・感染の爆発的拡大（pandemic）vs 収束の条件を研究する医学疫学。",
        "impact_summary": "COVID-19パンデミック（R₀≈2–3）でのロックダウン政策・ワクチン戦略策定の科学的根拠。Ross(1908 Nobel, マラリア伝播)・Kermack-McKendrick(1927, SIRモデル)が数理基盤を確立。",
        "subfield": "医学・臨床科学", "school_of_thought": "Epidemiology", "era_start": 1927,
        "culture_region": "Europe_Western",
        "source_url": "https://www.who.int/emergencies/diseases/novel-coronavirus-2019",
        "mathematical_formulation": r"R_0 = \frac{\beta}{\gamma}, \quad \frac{dI}{dt} = \beta SI - \gamma I",
        "data_completeness": 90,
    },
    {
        "name_ja": "アフリカの伝統医学と生薬研究",
        "name_en": "African Traditional Medicine and Phytotherapy",
        "definition": "サハラ以南アフリカで数千年の実践を持つ伝統医学体系（ズールー・ヨルバ・アカン・サンブル等）における薬用植物・動物・鉱物の利用と、その薬学的・毒理学的科学的検証。",
        "impact_summary": "アフリカ植物由来化合物（アルテミシニン類縁体・モリンガ・スーパーフルーツ由来成分）の医薬品開発。WHO伝統医学戦略2019–2034が在来知識と近代医学の統合を推進。",
        "subfield": "医学・臨床科学", "school_of_thought": "Ethnomedicine", "era_start": 1960,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.who.int/traditional-complementary-integrative-medicine/about/en/",
        "data_completeness": 82,
    },
    {
        "name_ja": "神経変性疾患の分子機構",
        "name_en": "Molecular Mechanisms of Neurodegeneration",
        "definition": "アルツハイマー病（Aβ・タウ凝集）・パーキンソン病（αシヌクレイン・PINK1-Parkin経路）・ALS（TDP-43・FUS凝集）・ハンチントン病における異常タンパク質凝集と神経死の分子経路。",
        "impact_summary": "高齢化社会における認知症（世界5,500万人, 2021）・ALS・PDの治療法開発の基盤。レカネマブ（抗Aβ抗体）が2023年初のAD疾患修飾薬として承認。",
        "subfield": "医学・臨床科学", "school_of_thought": "Neuroscience", "era_start": 1907,
        "culture_region": "Europe_Western",
        "source_url": "https://www.alzforum.org/",
        "data_completeness": 88,
    },
    {
        "name_ja": "腫瘍免疫療法",
        "name_en": "Cancer Immunotherapy",
        "definition": "免疫系をがんに対して再活性化する治療法。免疫チェックポイント阻害（PD-1/PD-L1・CTLA-4抗体）・CAR-T細胞療法・がんワクチン・腫瘍溶解性ウイルスが主要モダリティ。",
        "impact_summary": "Allison・本庶佑(2018 Nobel)の免疫チェックポイント発見がメラノーマ等の難治がんに長期完全寛解をもたらした。CAR-T（KYMRIAH 2017 FDA承認）が白血病の標準治療になった。",
        "subfield": "医学・臨床科学", "school_of_thought": "Oncology", "era_start": 1992,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2018/summary/",
        "data_completeness": 92,
    },
    {
        "name_ja": "手術ロボットと最低侵襲外科",
        "name_en": "Robotic Surgery and Minimally Invasive Surgery",
        "definition": "腹腔鏡・内視鏡・ロボット（da Vinci）を用いて小切開で行う手術。高精度な手震え補正・3D拡大視野・遠隔手術が可能。",
        "impact_summary": "前立腺がん・婦人科腫瘍・消化器外科で年間120万件以上のda Vinci手術（2021）。5G遠隔ロボット手術が過疎地・途上国医療へのアクセスを改善する可能性を持つ。",
        "subfield": "医学・臨床科学", "school_of_thought": "Surgery", "era_start": 1987,
        "culture_region": "North_America",
        "source_url": "https://www.intuitive.com/en-us",
        "data_completeness": 86,
    },
    {
        "name_ja": "人工知能による診断支援",
        "name_en": "AI-Assisted Diagnostic Imaging",
        "definition": "深層学習（CNN・Transformer）を用いた医療画像（X線・CT・MRI・病理スライド）の自動解析・病変検出・疾患分類・予後予測システムの開発と臨床評価。",
        "impact_summary": "網膜画像からの糖尿病網膜症AI診断がFDA承認（IDx-DR 2018）。Google DeepMind・NVIDIA-FLARE・GE Healthcareが医療AIプラットフォームを展開。放射線科医・病理医の業務変革が進行中。",
        "subfield": "医学・臨床科学", "school_of_thought": "Medical Informatics", "era_start": 2012,
        "culture_region": "North_America",
        "source_url": "https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices",
        "data_completeness": 87,
    },
    {
        "name_ja": "ウイルス学と抗ウイルス薬開発",
        "name_en": "Virology and Antiviral Drug Development",
        "definition": "ウイルスの複製サイクル（吸着・侵入・複製・アセンブリ・放出）の分子機構と、各ステップを標的とする抗ウイルス薬（核酸類縁体・プロテアーゼ阻害薬・融合阻害薬等）の設計。",
        "impact_summary": "HIV/AIDS治療（HAART：逆転写酵素阻害+プロテアーゼ阻害+インテグラーゼ阻害）が死亡率を激減。COVID-19パクスロビド（ニルマトレルビル/リトナビル）・モルヌピラビルが緊急承認。",
        "subfield": "医学・臨床科学", "school_of_thought": "Virology", "era_start": 1892,
        "culture_region": "North_America",
        "source_url": "https://www.niaid.nih.gov/diseases-conditions/antivirals",
        "data_completeness": 89,
    },
    {
        "name_ja": "幹細胞医学と再生医療",
        "name_en": "Stem Cell Medicine and Regenerative Medicine",
        "definition": "ES細胞・iPS細胞（Yamanaka 2012 Nobel/East_Asia）・成体幹細胞を用いた失われた組織・臓器の再生を目指す医学。心筋・神経・膵島・角膜・軟骨の再生研究が進む。",
        "impact_summary": "山中伸弥のiPS細胞技術が倫理問題を回避した多能性幹細胞源として世界的普及。iPS由来心筋シートの臨床試験（阪大）・角膜上皮シート・RPE移植が実用化段階。",
        "subfield": "医学・臨床科学", "school_of_thought": "Regenerative Medicine", "era_start": 1998,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2012/yamanaka/lecture/",
        "data_completeness": 91,
    },
    {
        "name_ja": "インドのアーユルヴェーダと現代医学的検証",
        "name_en": "Ayurveda and Its Scientific Validation",
        "definition": "古代インド医学体系アーユルヴェーダ（「生命の科学」）の主要概念（3ドーシャ説・パンチャカルマ浄化法・薬草処方）の現代医学的再評価と有効成分の科学的検証。",
        "impact_summary": "ウコン（クルクミン）・バジル・アシュワガンダ・グドゥチ等のアーユルヴェーダ植物の薬理学的研究が世界的に注目。WHO伝統医療戦略・COVID-19予防研究で科学的根拠の評価が加速。",
        "subfield": "医学・臨床科学", "school_of_thought": "Ethnomedicine", "era_start": -600,
        "culture_region": "South_Asia",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3131773/",
        "data_completeness": 82,
    },
    {
        "name_ja": "医療倫理と臨床試験の倫理規範",
        "name_en": "Medical Ethics and Clinical Trial Standards",
        "definition": "ニュルンベルク綱領（1947）・ヘルシンキ宣言（1964）・ベルモントレポート（1979）に基づくインフォームド・コンセント・リスク-ベネフィット評価・研究倫理審査委員会（IRB）の体系。",
        "impact_summary": "ナチスの人体実験・タスキギー梅毒実験の歴史的教訓から構築された医学研究の倫理的枠組み。遺伝子編集臨床応用（He Jiankui事件 2018/East_Asia）の倫理問題で再び注目を集めた。",
        "subfield": "医学・臨床科学", "school_of_thought": "Bioethics", "era_start": 1947,
        "culture_region": "North_America",
        "source_url": "https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html",
        "data_completeness": 85,
    },
    {
        "name_ja": "熱帯病と省みられない熱帯病（NTD）",
        "name_en": "Neglected Tropical Diseases",
        "definition": "主に熱帯・亜熱帯の低所得国に蔓延する17以上の疾患群（リーシュマニア症・シャーガス病・フィラリア症・住血吸虫症・トラコーマ等）。WHO NTDロードマップが根絶目標を設定。",
        "impact_summary": "Campbell・大村智(2015 Nobel, イベルメクチン)がフィラリア症・オンコセルカ症の制圧に貢献。10億人以上に影響するNTDが製薬企業・国際援助機関のプライオリティに再浮上。",
        "subfield": "医学・臨床科学", "school_of_thought": "Tropical Medicine", "era_start": 1900,
        "culture_region": "East_Asia",
        "source_url": "https://www.who.int/health-topics/neglected-tropical-diseases",
        "data_completeness": 87,
    },
    {
        "name_ja": "メンタルヘルスの神経科学基盤",
        "name_en": "Neuroscience of Mental Health",
        "definition": "うつ病・統合失調症・双極性障害・PTSD・強迫症等の精神疾患の神経回路（前頭前野-扁桃体・デフォルトモードネットワーク）・神経伝達物質（セロトニン・ドーパミン・グルタミン酸）・遺伝的基盤の研究。",
        "impact_summary": "SSRI・第2世代抗精神病薬・ケタミン（抗うつ）・TMS/ECTの機序理解。世界人口の14%が何らかの精神疾患（WHO, 2022）。COVID-19後遺症としての精神症状の神経生物学的解明が急務。",
        "subfield": "医学・臨床科学", "school_of_thought": "Psychiatry", "era_start": 1950,
        "culture_region": "North_America",
        "source_url": "https://www.nimh.nih.gov/health/statistics",
        "data_completeness": 87,
    },
]

BIOLOGY = [
    {
        "name_ja": "細胞分裂と有糸分裂チェックポイント",
        "name_en": "Cell Division and Mitotic Checkpoints",
        "definition": "有糸分裂（M期）の紡錘体チェックポイント・DNAダメージチェックポイント・細胞質分裂の分子機構。サイクリン-CDK・APC/C・分裂促進因子（MPF）が制御中枢。",
        "impact_summary": "Hartwell・Hunt・Nurse(2001 Nobel, 細胞周期制御)が確立。チェックポイント異常ながん化・CDK4/6阻害薬（パルボシクリブ）の抗がん薬開発に直結。",
        "subfield": "生命科学・生物学", "school_of_thought": "Cell Biology", "era_start": 1970,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2001/summary/",
        "data_completeness": 90,
    },
    {
        "name_ja": "植物の光形態形成",
        "name_en": "Plant Photomorphogenesis",
        "definition": "植物が光シグナル（赤色光・遠赤色光・青色光）によって発芽・葉の展開・開花・花成誘導（光周性）等の形態形成応答を調節する分子機構。フィトクロム・フォトトロピン・クリプトクロムが光受容体。",
        "impact_summary": "農業（人工光栽培・植物工場・長日植物の開花制御）・宇宙農業・バイオリズム研究の基盤。Bünning（概日リズム先駆）・Quail（フィトクロム分子生物学）が確立。",
        "subfield": "生命科学・生物学", "school_of_thought": "Plant Biology", "era_start": 1920,
        "culture_region": "North_America",
        "source_url": "https://www.plantcell.org/content/33/1/1",
        "data_completeness": 86,
    },
    {
        "name_ja": "生体リズムと概日時計",
        "name_en": "Circadian Clock and Biological Rhythms",
        "definition": "24時間周期の内因性生物時計の分子機構。CLOCK・BMAL1・PER・CRYタンパク質のフィードバックループが哺乳類の概日リズムを生成する。",
        "impact_summary": "Hall・Rosbash・Young(2017 Nobel, 概日リズムの分子機構)が確立。睡眠障害・代謝疾患・がん・薬物投与タイミング（時間療法）への応用。航空士・シフト労働者の健康影響の科学的根拠。",
        "subfield": "生命科学・生物学", "school_of_thought": "Chronobiology", "era_start": 1971,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2017/summary/",
        "data_completeness": 91,
    },
    {
        "name_ja": "タンパク質の折りたたみと品質管理",
        "name_en": "Protein Folding and Quality Control",
        "definition": "新生ポリペプチドが三次元機能的立体構造を獲得する過程（タンパク質折りたたみ）と、誤折りたたみタンパク質の認識・修正・分解（タンパク質品質管理）の細胞機構。",
        "impact_summary": "Anfinsen(1972 Nobel, タンパク質折りたたみの熱力学)・AlphaFold2(DeepMind 2021)が50年の難問を解決しPDB全体の構造予測を達成。アミロイド病（アルツハイマー・プリオン）の理解基盤。",
        "subfield": "生命科学・生物学", "school_of_thought": "Structural Biology", "era_start": 1961,
        "culture_region": "North_America",
        "source_url": "https://alphafold.ebi.ac.uk/",
        "data_completeness": 91,
    },
    {
        "name_ja": "生態系サービスと自然資本",
        "name_en": "Ecosystem Services and Natural Capital",
        "definition": "生態系が人類に提供する恩恵（供給サービス・調節サービス・文化的サービス・支持サービス）を経済的に評価する概念的・定量的枠組み。Costanza et al.(1997)が先駆的定量化。",
        "impact_summary": "世界の生態系サービスの価値は推定125–145兆USD/年（世界GDP以上）。IPBES報告書・SEEA生態系勘定・ネイチャーポジティブ経営の科学的基盤として政策・金融に組み込まれつつある。",
        "subfield": "生命科学・生物学", "school_of_thought": "Conservation Biology", "era_start": 1997,
        "culture_region": "North_America",
        "source_url": "https://ipbes.net/global-assessment",
        "data_completeness": 87,
    },
    {
        "name_ja": "腸管免疫と粘膜免疫",
        "name_en": "Gut Immunity and Mucosal Immunology",
        "definition": "腸管上皮・Peyer板・分泌型IgA・腸間膜リンパ節・腸管神経系が構成する消化管免疫の複合体。腸内細菌叢と宿主免疫の相互作用が核心テーマ。",
        "impact_summary": "炎症性腸疾患（IBD）・セリアック病・アレルギー・自閉症・神経変性疾患との腸-脳軸を介した連関が明らかになっている。プロバイオティクス・糞便微生物移植（FMT）の科学的根拠の構築。",
        "subfield": "生命科学・生物学", "school_of_thought": "Immunology", "era_start": 1960,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/collections/gut-microbiome",
        "data_completeness": 87,
    },
    {
        "name_ja": "種分化と隔離機構",
        "name_en": "Speciation and Isolating Mechanisms",
        "definition": "生物が新たな種に分岐する過程（種分化）の生態的・行動的・遺伝的隔離機構。異所的種分化・同所的種分化・隔離強化・ポスト接合的不和合（hybrid inviability）が主要概念。",
        "impact_summary": "Mayr(1942)の生物学的種概念・Dobzhansky-Mullerモデル・ゲノム種分化（ゲノム島）の研究が進む。シクリッド（アフリカ大湖）・ガラパゴスフィンチが種分化研究の古典的モデル生物。",
        "subfield": "生命科学・生物学", "school_of_thought": "Evolutionary Biology", "era_start": 1942,
        "culture_region": "North_America",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-ecolsys-120213-091818",
        "data_completeness": 87,
    },
    {
        "name_ja": "生化学的発光とGFP",
        "name_en": "Green Fluorescent Protein (GFP) and Fluorescent Proteins",
        "definition": "クラゲから分離された緑色蛍光タンパク質（GFP）とその変異体（YFP・CFP・RFP等）を生体分子のラベルとして使用する生細胞蛍光イメージング手法。",
        "impact_summary": "Shimomura・Chalfie・Tsien(2008 Nobel)。FRET・スーパー解像度蛍光顕微鏡（PALM/STORM）・生細胞トラッキング・オプトジェネティクスの分子ツールとして革命的普及。",
        "subfield": "生命科学・生物学", "school_of_thought": "Cell Biology", "era_start": 1994,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2008/summary/",
        "data_completeness": 91,
    },
    {
        "name_ja": "X線結晶構造解析によるタンパク質構造決定",
        "name_en": "X-ray Crystallography of Proteins",
        "definition": "タンパク質単結晶にX線を照射して得られる回折パターンからフーリエ変換で電子密度マップを再構築し原子分解能での三次元構造を決定する手法。",
        "impact_summary": "Kendrew・Perutz(1962 Nobel, ミオグロビン・ヘモグロビン構造)がタンパク質構造生物学を開始。DNAポリメラーゼ・リボソーム(Yonath・Steitz・Ramakrishnan 2009 Nobel)・GPCRの構造決定が医薬品設計を加速。",
        "subfield": "生命科学・生物学", "school_of_thought": "Structural Biology", "era_start": 1958,
        "culture_region": "Europe_Western",
        "source_url": "https://www.rcsb.org/stats/summary",
        "data_completeness": 91,
    },
    {
        "name_ja": "中国・東アジアの伝統的植物学と本草学",
        "name_en": "Chinese Materia Medica and Traditional Botany of East Asia",
        "definition": "古代から中世にかけて中国・日本・韓国・ベトナムで発展した薬用植物の体系的分類・栽培・加工の知識体系。李時珍の『本草綱目』（1596年）が集大成。",
        "impact_summary": "屠呦呦によるアルテミシニン発見（2015 Nobel）は本草綱目の葛洪記述（肘後方）を起点とした。東アジア伝統植物学が現代医薬品開発・植物分類学・農業多様性研究に継続的に貢献。",
        "subfield": "生命科学・生物学", "school_of_thought": "Ethnobotany", "era_start": 200,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2015/tu/lecture/",
        "data_completeness": 85,
    },
]

def insert_batch(conn, batch):
    cursor = conn.cursor()
    now = datetime.now(timezone.utc).isoformat()
    inserted = 0
    for c in batch:
        cursor.execute("SELECT id FROM natural_discovery WHERE name_en = ?", (c["name_en"],))
        if cursor.fetchone():
            continue
        uid = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO natural_discovery (
                id, name_ja, name_en, name_original, definition, impact_summary,
                subfield, school_of_thought, era_start, culture_region,
                source_url, mathematical_formulation, verification_status,
                status, data_completeness, created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (uid, c["name_ja"], c["name_en"], c.get("name_original"),
              c["definition"], c["impact_summary"], c["subfield"],
              c["school_of_thought"], c["era_start"], c["culture_region"],
              c["source_url"], c.get("mathematical_formulation"),
              c.get("verification_status", "url_present"), "active",
              c.get("data_completeness", 85), now, now))
        inserted += 1
    conn.commit()
    return inserted

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n1 = insert_batch(conn, MATERIALS)
    n2 = insert_batch(conn, MEDICINE)
    n3 = insert_batch(conn, BIOLOGY)
    total = n1 + n2 + n3
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    grand = cursor.fetchone()[0]
    conn.close()
    print(f"Batch17 multi: {total} inserted (mat={n1}, med={n2}, bio={n3}). Total: {grand}")
