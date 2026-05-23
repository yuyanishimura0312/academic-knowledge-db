"""
DUA Wave A2 Batch 16 — Chemistry batch 3 (~50 concepts, subfield '化学')
"""
import sqlite3
import uuid
from datetime import datetime, timezone

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

CONCEPTS = [
    {
        "name_ja": "立体化学と光学活性",
        "name_en": "Stereochemistry and Optical Activity",
        "definition": "分子の三次元配置（エナンチオマー・ジアステレオマー・コンフォメーション）とその化学的・生物学的性質の差異を研究する化学分野。旋光性・キラリティーが核心概念。",
        "impact_summary": "サリドマイド惨事（一方のエナンチオマーのみ催奇性）が不斉合成の重要性を証明。不斉触媒（野依・Noyori, 2001 Nobel）が医薬品の100%エナンチオ選択的合成を実現。",
        "subfield": "化学", "school_of_thought": "Organic Chemistry", "era_start": 1848,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2001/noyori/lecture/",
        "mathematical_formulation": r"[\alpha]_D^{25} = \frac{\alpha}{l \cdot c}",
        "data_completeness": 91,
    },
    {
        "name_ja": "有機金属化学",
        "name_en": "Organometallic Chemistry",
        "definition": "炭素-金属結合を含む化合物の合成・反応・触媒機能を扱う化学分野。フェロセン・グリニャール試薬・有機リチウム・π錯体・カルベン錯体が主要クラス。",
        "impact_summary": "Fischer・Wilkinson(1973 Nobel, サンドイッチ錯体)。有機合成の汎用ツール（有機銅試薬・有機亜鉛試薬）。遷移金属触媒反応（Pd・Rh・Ru触媒）の分子レベルの理解基盤。",
        "subfield": "化学", "school_of_thought": "Inorganic Chemistry", "era_start": 1900,
        "culture_region": "Europe_Western",
        "source_url": "https://www.rsc.org/journals-books-databases/find-an-article/organometallics/",
        "data_completeness": 89,
    },
    {
        "name_ja": "生体内金属酵素",
        "name_en": "Metalloenzymes and Bioinorganic Chemistry",
        "definition": "鉄・銅・亜鉛・マンガン・モリブデン等の金属イオンを活性中心に持つ酵素の触媒機構・構造・生物機能を研究する分野。ヘモグロビン・チトクロームP450・ニトロゲナーゼが代表例。",
        "impact_summary": "ニトロゲナーゼ（窒素固定・FeMoコファクター）の機構解明が人工窒素固定触媒設計の指針を提供。シスプラチン（白金錯体抗がん剤）はバイオ無機化学の臨床応用の典型。",
        "subfield": "化学", "school_of_thought": "Biochemistry", "era_start": 1960,
        "culture_region": "North_America",
        "source_url": "https://pubs.acs.org/journal/acbcct",
        "data_completeness": 88,
    },
    {
        "name_ja": "ナノ化学と自己組織化",
        "name_en": "Nanochemistry and Self-Assembly",
        "definition": "ナノスケール（1–100 nm）の材料合成と分子間非共有結合力による自発的な高次構造（ナノ粒子・ナノチューブ・単分子膜・ベシクル）の形成を研究する化学分野。",
        "impact_summary": "金ナノ粒子（光熱療法・バイオセンシング）・リポソーム薬物デリバリー・チオール自己組織化単分子膜（SAM）・DNA折り紙（DNAオリガミ）等が医療・電子材料・触媒に展開。",
        "subfield": "化学", "school_of_thought": "Materials Chemistry", "era_start": 1990,
        "culture_region": "North_America",
        "source_url": "https://www.rsc.org/journals-books-databases/find-an-article/nanoscale/",
        "data_completeness": 88,
    },
    {
        "name_ja": "有機π共役系と有機半導体",
        "name_en": "Conjugated Systems and Organic Semiconductors",
        "definition": "交互する単結合-二重結合（π共役）を持つ有機分子（ポリアセチレン・ペンタセン・フラーレン誘導体・ペリレン等）が示す電気的・光学的半導体特性。",
        "impact_summary": "白川英樹・MacDiarmid・Heeger(2000 Nobel, 導電性ポリマー/East_Asia)。有機EL（OLED）・有機太陽電池・有機FET（電子ペーパー）・フレキシブルエレクトロニクスの基盤。",
        "subfield": "化学", "school_of_thought": "Materials Chemistry", "era_start": 1977,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2000/shirakawa/lecture/",
        "mathematical_formulation": r"E_g = E_{\text{LUMO}} - E_{\text{HOMO}}, \quad \mu_{FET} = \frac{L}{WC_{ox}V_{ds}}\frac{dI_{ds}}{dV_{gs}}",
        "data_completeness": 91,
    },
    {
        "name_ja": "結晶化と多形",
        "name_en": "Crystallization and Polymorphism",
        "definition": "溶液・融液・気相からの結晶核生成・成長の熱力学・動力学、および同じ化学組成で異なる結晶構造（多形・多型）を持つことの化学・薬学的意義。",
        "impact_summary": "医薬品多形（シメチジン・リトナビルのAbbvie多形問題）が薬物動態・特許に決定的影響。Oswald熟成・核生成理論（Classical Nucleation Theory）が工業結晶化プロセス設計の基盤。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1780,
        "culture_region": "Europe_Western",
        "source_url": "https://goldbook.iupac.org/terms/view/P04840",
        "mathematical_formulation": r"\Delta G_{\text{nucleus}} = \frac{4}{3}\pi r^3\Delta G_v + 4\pi r^2\gamma",
        "data_completeness": 87,
    },
    {
        "name_ja": "表面科学と不均一触媒の分子論",
        "name_en": "Surface Science and Heterogeneous Catalysis",
        "definition": "固体触媒表面における気体分子の吸着・解離・反応・脱着の分子論的機構を研究する物理化学・材料科学の分野。UHV-STM・XPS・LEED・反応速度論が主要ツール。",
        "impact_summary": "Ertl(2007 Nobel, ハーバー-ボッシュ反応の表面機構解明)。自動車排気触媒（三元触媒・Pt-Pd-Rh）・燃料電池電極触媒設計・光触媒（TiO₂/水分解）の原子論的基礎。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1960,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2007/ertl/lecture/",
        "mathematical_formulation": r"\theta_A = \frac{K_A p_A}{1 + K_A p_A + K_B p_B} \quad \text{(Langmuir adsorption)}",
        "data_completeness": 90,
    },
    {
        "name_ja": "重合禁止剤とラジカル安定化",
        "name_en": "Radical Chemistry and Stabilization",
        "definition": "不対電子を持つラジカル種の生成・反応・安定化・クエンチの化学。共役系・立体保護・窒素酸化物（NIT等）・キャプチャー試薬によるラジカルトラッピングが主要テーマ。",
        "impact_summary": "重合反応制御（ATRP・RAFT等のリビングラジカル重合）・抗酸化剤（ビタミンE・フェノール系）の機構・ESR測定によるラジカル検出・タンパク質ラジカルの生物学的意義。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1900,
        "culture_region": "North_America",
        "source_url": "https://goldbook.iupac.org/terms/view/R05066",
        "data_completeness": 85,
    },
    {
        "name_ja": "化学発光と生物発光",
        "name_en": "Chemiluminescence and Bioluminescence",
        "definition": "化学反応（またはルシフェラーゼ酵素反応）によって励起状態が生成され発光する現象。ルシフェリン-ルシフェラーゼ系・ルミノール反応・ホタル・深海生物発光が代表例。",
        "impact_summary": "GFP（Green Fluorescent Protein）関連研究（Shimomura・Chalfie・Tsien, 2008 Nobel）と合わせ、生体イメージング・細胞追跡・がん検出・法医学（ルミノール）に広く応用。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1928,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2008/shimomura/lecture/",
        "data_completeness": 88,
    },
    {
        "name_ja": "分子マシン",
        "name_en": "Molecular Machines",
        "definition": "化学エネルギーや光エネルギーによって機械的仕事を行う合成分子装置。ロタキサン・カテナン・分子モーター・分子スイッチが主要構成要素。",
        "impact_summary": "Sauvage・Stoddart・Feringa(2016 Nobel)が合成分子マシンを確立。ATP合成酵素（天然の分子モーター）との比較・ドラッグデリバリー制御・ナノロボティクスへの展開が期待される。",
        "subfield": "化学", "school_of_thought": "Organic Chemistry", "era_start": 1983,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2016/summary/",
        "data_completeness": 90,
    },
    {
        "name_ja": "同位体標識と代謝フラックス解析",
        "name_en": "Isotope Labeling and Metabolic Flux Analysis",
        "definition": "安定同位体（¹³C・¹⁵N・²H）または放射性同位体（¹⁴C・³H）で標識した化合物をトレーサーとして代謝経路・フラックスを定量的に解析する手法。",
        "impact_summary": "Calvin-Benson回路の解明（Calvinの¹⁴C実験, 1961 Nobel）・がん代謝（ワールブルク効果）の¹³C代謝フラックス解析・腸内細菌の代謝産物追跡に活用。",
        "subfield": "化学", "school_of_thought": "Biochemistry", "era_start": 1940,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1961/calvin/lecture/",
        "mathematical_formulation": r"\dot{x} = Nv, \quad \text{(Sv = 0 at steady state)}",
        "data_completeness": 88,
    },
    {
        "name_ja": "水の化学的性質と水素結合ネットワーク",
        "name_en": "Chemistry of Water and Hydrogen Bond Network",
        "definition": "水分子の特異な物性（高比熱・高表面張力・4℃最大密度・強い溶媒能）の起源となる三次元水素結合ネットワークの構造・ダイナミクス・揺らぎ。",
        "impact_summary": "生命の溶媒としての水の役割・タンパク質疎水性折りたたみ・電解質水溶液の熱力学・二酸化炭素水和（海洋酸性化）の基礎。1フェムト秒レーザーで水の超高速ダイナミクスを追跡可能に。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1933,
        "culture_region": "North_America",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0959440X19301381",
        "mathematical_formulation": r"g(r) = \frac{\rho(r)}{\rho_0}, \quad \xi(t) = \langle\delta O(0)\delta O(t)\rangle",
        "data_completeness": 88,
    },
    {
        "name_ja": "金属有機構造体（MOF）",
        "name_en": "Metal-Organic Frameworks (MOFs)",
        "definition": "金属イオン（または金属クラスター）と有機配位子を組み合わせた多孔性結晶性材料（MOF）。比表面積10,000 m²/g超を達成し細孔サイズ・機能を精密設計できる。",
        "impact_summary": "CO₂回収・水素貯蔵・薬物送達・触媒・化学センサーへの応用。Yaghi(カリフォルニア大)・Kitagawa(東京大/East_Asia)・Férey(仏)が独立に確立。商業化が進む次世代多孔性材料。",
        "subfield": "化学", "school_of_thought": "Materials Chemistry", "era_start": 1995,
        "culture_region": "East_Asia",
        "source_url": "https://pubs.acs.org/journal/aaemcq",
        "mathematical_formulation": r"S_{\text{BET}} = \frac{v_m N_A \sigma}{\text{mass}}, \quad \text{BET adsorption}",
        "data_completeness": 88,
    },
    {
        "name_ja": "電気化学的窒素固定",
        "name_en": "Electrochemical Nitrogen Fixation",
        "definition": "電力を用いて常温常圧でN₂をNH₃に還元する電気化学的窒素固定反応（e-NRR）。ハーバー-ボッシュ法の脱炭素代替として注目されるが、選択性（NH₃/HER競合）が主要課題。",
        "impact_summary": "再生可能エネルギー由来電力でのグリーンアンモニア合成を実現できればカーボンニュートラル農業・水素エネルギーキャリアへの貢献が大きい。2020年代に研究が急加速。",
        "subfield": "化学", "school_of_thought": "Electrochemistry", "era_start": 2015,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/s41929-019-0249-y",
        "mathematical_formulation": r"N_2 + 6H^+ + 6e^- \rightarrow 2NH_3, \quad E^\circ = -0.57\,\text{V vs SHE}",
        "data_completeness": 85,
    },
    {
        "name_ja": "メカノケミストリー（力化学）",
        "name_en": "Mechanochemistry",
        "definition": "機械的力（粉砕・押出・剪断）によって化学反応を誘起する化学。固相反応・ポリマー力化学・タンパク質力学伸長・分子力センサーが主要テーマ。溶媒不要の緑色合成法として注目。",
        "impact_summary": "医薬品共結晶合成・ポリマー架橋制御・コプレシピテーション法の代替。力で発色するポリマー（メカノクロミズム）が損傷センサーに応用。Lehn・Fréchetらが理論的に整備。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1893,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/s41557-021-00825-3",
        "data_completeness": 85,
    },
    {
        "name_ja": "ボロン化学と有機ホウ素化合物",
        "name_en": "Boron Chemistry and Organoboron Compounds",
        "definition": "ホウ素化合物（ボロン酸・ボレート・カルボランなど）の合成・反応性・応用を扱う化学分野。鈴木-宮浦カップリング（C-Cクロスカップリング）の試薬として不可欠。",
        "impact_summary": "鈴木-宮浦カップリング(Suzuki・Miyaura/East_Asia, 2010 Nobel)がボロン酸エステルを医薬品合成の標準試薬として確立。ボロン中性子捕捉療法（BNCT）がん治療への応用が進む。",
        "subfield": "化学", "school_of_thought": "Organic Chemistry", "era_start": 1979,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2010/suzuki/lecture/",
        "data_completeness": 89,
    },
    {
        "name_ja": "錬金術から化学への移行（ヨーロッパ近代）",
        "name_en": "Alchemy to Chemistry Transition in Europe",
        "definition": "16–18世紀にかけて、金属変換・哲学者の石追求を目指す錬金術から実験的・定量的化学（Lavoisierの化学革命）へと転換した科学史的プロセス。Boyle・Stahl・Lavoisierが主要人物。",
        "impact_summary": "化学の科学的方法論（定量測定・元素概念・名称体系化）を確立した歴史的転換点。近代科学全体の規範形成にも影響。パラケルスス・ヘルモント等の医化学派も含む複合的変革。",
        "subfield": "化学", "school_of_thought": "History of Chemistry", "era_start": 1620,
        "culture_region": "Europe_Western",
        "source_url": "https://www.sciencehistory.org/learn/science-matters/history-of-chemistry",
        "data_completeness": 85,
    },
    {
        "name_ja": "アフリカの植物薬学と天然物化学",
        "name_en": "African Ethnopharmacology and Natural Products Chemistry",
        "definition": "アフリカ在来知識体系（伝統医学）から発掘された薬用植物の化学成分（アルカロイド・テルペノイド・フラボノイド）を科学的に解明する研究分野。",
        "impact_summary": "ヨヒンビン（インポテンス治療）・レセルピン（降圧薬）・ビンブラスチン（抗がん薬, キョウチクトウ科）・アルテミシニン関連化合物がアフリカ伝統知から開発された。WHO伝統医学戦略の科学的裏付け。",
        "subfield": "化学", "school_of_thought": "Ethnochemistry", "era_start": 1800,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0031942216302552",
        "data_completeness": 82,
    },
    {
        "name_ja": "フローケミストリーと連続製造",
        "name_en": "Continuous Manufacturing in Chemistry",
        "definition": "医薬品・化学品を連続的に製造するプロセス化学の変革。バッチ生産からフロー合成・連続結晶化・インライン分析・フィードバック制御へのシフト。FDA・EMAが推奨。",
        "impact_summary": "バッチ生産比でコスト30–50%削減・リードタイム短縮・廃棄物削減を実証。ジョンソン&ジョンソン・Eli Lily等が医薬品連続製造を実用化。COVID-19ワクチン製造のスケールアップに貢献。",
        "subfield": "化学", "school_of_thought": "Process Chemistry", "era_start": 2010,
        "culture_region": "North_America",
        "source_url": "https://www.fda.gov/science-research/advances-regulatory-science/continuous-manufacturing-pharmaceutical-solid-dosage-forms",
        "data_completeness": 86,
    },
    {
        "name_ja": "環境有機汚染物質と生体蓄積",
        "name_en": "Persistent Organic Pollutants and Bioaccumulation",
        "definition": "脂溶性が高く環境中で分解されにくい有機化合物（PCB・ダイオキシン・PFAS・DDT等）が食物連鎖を通じて生物濃縮（バイオマグニフィケーション）する現象と化学的性質。",
        "impact_summary": "ストックホルム条約（2001）がPOPs12種の生産・使用・排出を規制。PFAS（永遠の化学物質）問題が現在進行中で飲料水汚染・甲状腺機能・がんリスクとの関連が社会問題化。",
        "subfield": "化学", "school_of_thought": "Environmental Chemistry", "era_start": 1962,
        "culture_region": "North_America",
        "source_url": "https://chm.pops.int/",
        "mathematical_formulation": r"\log K_{ow} > 5 \Rightarrow \text{bioaccumulation potential}",
        "data_completeness": 87,
    },
    {
        "name_ja": "化学反応ダイナミクスと遷移状態",
        "name_en": "Reaction Dynamics and Transition State Theory",
        "definition": "化学反応における反応座標・遷移状態（活性化錯体）・ポテンシャルエネルギー面の概念と、率定数の温度依存性を記述するEyring（遷移状態）理論。",
        "impact_summary": "Eyring(TST, 1935)・Arrhenius(活性化エネルギー)・Marcus(電子移動速度, 1992 Nobel)が体系化。酵素反応・大気化学・爆発反応の速度論的制御の理論基盤。",
        "subfield": "化学", "school_of_thought": "Physical Chemistry", "era_start": 1889,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1992/marcus/lecture/",
        "mathematical_formulation": r"k = \frac{k_BT}{h}e^{-\Delta G^\ddagger/RT} = Ae^{-E_a/RT}",
        "data_completeness": 91,
    },
    {
        "name_ja": "核磁気共鳴によるタンパク質構造決定",
        "name_en": "NMR-based Protein Structure Determination",
        "definition": "多次元NMR（COSY・NOESY・HSQC・HNCO等）スペクトルから核Overhauser効果（NOE）距離制約・J結合角を抽出しタンパク質の三次元溶液構造を決定する手法。",
        "impact_summary": "Wüthrich(2002 Nobel)がNMR構造決定法を確立。結晶化が困難な膜タンパク・IDPに特に有効。溶液中の動的挙動・化学シフト摂動による相互作用解析が薬物-受容体研究に不可欠。",
        "subfield": "化学", "school_of_thought": "Biochemistry", "era_start": 1986,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2002/wuthrich/lecture/",
        "data_completeness": 90,
    },
    {
        "name_ja": "生体高分子の相分離（液-液相分離）",
        "name_en": "Biomolecular Condensates and Liquid-Liquid Phase Separation",
        "definition": "細胞内でタンパク質・核酸が液-液相分離によって形成される非膜結合性オルガネラ様凝縮体（P顆粒・ストレス顆粒・スプライシングスポット）の物理化学。",
        "impact_summary": "転写制御・RNAプロセシング・シグナル伝達・神経変性疾患（ALS・FTD）との関連。Brangwynne・Hyman(2009, MBL)が発見した新概念で2010年代後半から急速に研究が拡大。",
        "subfield": "化学", "school_of_thought": "Biochemistry", "era_start": 2009,
        "culture_region": "North_America",
        "source_url": "https://www.science.org/doi/10.1126/science.1172046",
        "data_completeness": 88,
    },
    {
        "name_ja": "単分子分光と力学的特性計測",
        "name_en": "Single-Molecule Spectroscopy and Force Spectroscopy",
        "definition": "個々の分子を光学的（FRET・TIRF・STED）または力学的（AFM・光ピンセット・磁気ピンセット）に観察・操作し統計平均では隠れた分子内ダイナミクスを解明する手法。",
        "impact_summary": "DNA複製・タンパク質折りたたみ・分子モーターの力学サイクル・RNAポリメラーゼの転写の一分子リアルタイム観察が生化学に革命をもたらした。超解像蛍光顕微鏡（2014 Nobel）と連携。",
        "subfield": "化学", "school_of_thought": "Analytical Chemistry", "era_start": 1990,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2014/summary/",
        "data_completeness": 89,
    },
    {
        "name_ja": "フォトレドックス触媒と可視光有機合成",
        "name_en": "Photoredox Catalysis in Organic Synthesis",
        "definition": "可視光を吸収する光増感剤（ルテニウム・イリジウム錯体・有機色素）を触媒として、一電子移動経路で従来困難だった結合形成（C-C・C-N・C-O）を行う手法。",
        "impact_summary": "MacMillan・Yoon・Stephenson(2008–2011)が現代的光触媒有機合成を確立。医薬品合成ステップ数削減・複雑分子の直接官能基化・フロー光化学反応として実用化が進む。",
        "subfield": "化学", "school_of_thought": "Organic Chemistry", "era_start": 2008,
        "culture_region": "North_America",
        "source_url": "https://pubs.acs.org/doi/10.1021/ja8019975",
        "data_completeness": 87,
    },
    {
        "name_ja": "中国の磁器と釉薬化学",
        "name_en": "Chinese Porcelain and Glaze Chemistry",
        "definition": "宋〜清代に発達した景徳鎮磁器の釉薬（石灰・長石・カオリン配合）の高温焼成化学。青花（コバルト着色）・汝窯（鉄含有青磁）・粉彩（ホウ砂釉薬）の化学的成分。",
        "impact_summary": "東洋の磁器製造技術が17–18世紀ヨーロッパに輸出され、マイセン磁器等の開発を促進。文化財保存・考古化学・セラミックス材料史において非西洋化学史の重要事例。",
        "subfield": "化学", "school_of_thought": "History of Chemistry", "era_start": 960,
        "culture_region": "East_Asia",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S2352409X18300373",
        "data_completeness": 82,
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
    n = insert_batch(conn, CONCEPTS)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    grand = cursor.fetchone()[0]
    conn.close()
    print(f"Batch16 chemistry3: {n} inserted. Total: {grand}")
