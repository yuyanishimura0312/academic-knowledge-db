"""
DUA Wave A2 Batch 19: Chemistry 4 + Biology 2
Target: ~50 insertions → 化学 +30, 生命科学・生物学 +20
"""
import sqlite3, uuid
from datetime import datetime, timezone

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

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

CHEM_BATCH1 = [
    {
        "name_ja": "核磁気共鳴分光法（NMR）",
        "name_en": "Nuclear Magnetic Resonance Spectroscopy",
        "name_original": "NMR Spectroscopy",
        "definition": "原子核のスピン状態が磁場中で異なるエネルギー準位に分裂し、ラジオ波の吸収を利用して分子構造を解析する分光法。1H, 13C, 15N 等の核種で化学シフト・結合定数・NOE を測定し、タンパク質立体構造から天然物同定まで適用される。",
        "impact_summary": "医用MRI（磁気共鳴映像法）の基礎技術としても機能し、2002年ノーベル化学賞（Wüthrich、タンパク質NMR構造決定）など複数のノーベル賞に貢献。",
        "subfield": "化学",
        "school_of_thought": "分析化学",
        "era_start": 1945,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2002/press-release/",
        "mathematical_formulation": r"\nu = \frac{\gamma B_0}{2\pi}, \quad \delta = \frac{\nu_{sample} - \nu_{ref}}{\nu_{ref}} \times 10^6 \text{ (ppm)}",
        "data_completeness": 90
    },
    {
        "name_ja": "X線回折結晶学",
        "name_en": "X-ray Crystallography",
        "name_original": "X-ray Diffraction",
        "definition": "結晶にX線を照射して得られる回折パターンから、原子の三次元配置を決定する手法。ブラッグの法則（2d sinθ = nλ）に基づき、タンパク質・核酸・小分子の立体構造を原子分解能で解析する。DNAの二重らせん発見（Franklin/Watson/Crick）など構造生物学の基盤。",
        "impact_summary": "DNA・タンパク質・ウイルスの構造解明に不可欠で、28以上のノーベル賞に関連。2020年代のAlphaFold2による構造予測AIの訓練データの根拠となった。",
        "subfield": "化学",
        "school_of_thought": "構造化学",
        "era_start": 1912,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.iucr.org/education/pamphlets/2",
        "mathematical_formulation": r"2d\sin\theta = n\lambda, \quad F_{hkl} = \sum_j f_j \exp[2\pi i(hx_j + ky_j + lz_j)]",
        "data_completeness": 92
    },
    {
        "name_ja": "有機合成化学",
        "name_en": "Organic Synthesis",
        "name_original": "Organic Synthesis",
        "definition": "炭素骨格を構築・修飾して目的有機化合物を得る化学の一分野。逆合成解析（retrosynthetic analysis、Corey）を用いて複雑天然物を合成する全合成と、医薬品・機能性材料を効率製造するプロセス化学を含む。触媒的不斉合成・クロスカップリング・C-H活性化が現代の主要戦略。",
        "impact_summary": "医薬品（ペニシリン全合成、ビタミンB12全合成）から機能性材料まで現代化学産業の基盤。Corey（1990年ノーベル化学賞）がretrosynthesis理論を確立。",
        "subfield": "化学",
        "school_of_thought": "有機化学",
        "era_start": 1828,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1990/press-release/",
        "mathematical_formulation": r"\text{Retrosynthesis: } A \Rightarrow B + C, \quad \text{Step economy} = \frac{\text{Total steps}}{\text{Bonds formed}}",
        "data_completeness": 88
    },
    {
        "name_ja": "熱分析化学",
        "name_en": "Thermal Analysis Chemistry",
        "name_original": "Thermal Analysis",
        "definition": "物質の物理的・化学的性質を温度の関数として測定する分析手法群。示差走査熱量測定（DSC）、熱重量分析（TGA）、示差熱分析（DTA）により、相転移・分解・結晶化・ガラス転移温度を定量する。",
        "impact_summary": "ポリマー・医薬品・セラミクス・食品の品質管理と材料開発に不可欠。DSCはタンパク質の熱変性・リポソーム安定性・新薬の多形スクリーニングに応用される。",
        "subfield": "化学",
        "school_of_thought": "物理化学",
        "era_start": 1887,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.netzsch-thermal-analysis.com/en/landing-pages/thermal-analysis-explained/",
        "mathematical_formulation": r"\frac{dH}{dT} = C_p(T), \quad \Delta H = \int_{T_1}^{T_2} C_p\, dT",
        "data_completeness": 82
    },
    {
        "name_ja": "錯体触媒・均一系触媒",
        "name_en": "Homogeneous Catalysis",
        "name_original": "Homogeneous Catalysis",
        "definition": "触媒と基質が同一相（通常液相）に存在する触媒反応。遷移金属錯体触媒によるヒドロホルミル化・重合・クロスカップリングが代表例。Wilkinson触媒（RhCl(PPh3)3）による水素化、Ziegler-Natta重合などが工業プロセスに展開された。",
        "impact_summary": "不斉水素化（野依良治 2001年ノーベル化学賞）・Olefin metathesis（Grubbs, Schrock, Chauvin 2005年ノーベル化学賞）など多数のノーベル賞に関連した精密化学の中心。",
        "subfield": "化学",
        "school_of_thought": "触媒化学",
        "era_start": 1965,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2005/press-release/",
        "mathematical_formulation": r"r = k[\text{cat}][A]^m[B]^n, \quad k = A\exp\!\left(-\frac{E_a}{RT}\right)",
        "data_completeness": 88
    },
    {
        "name_ja": "分子認識・ホスト-ゲスト化学",
        "name_en": "Molecular Recognition and Host-Guest Chemistry",
        "name_original": "Host-Guest Chemistry",
        "definition": "非共有結合性相互作用（水素結合・静電力・疎水効果・π-π積層）により、受容体（ホスト）が特定の基質（ゲスト）を選択的に捕捉・認識する現象と設計原理。クラウンエーテル・シクロデキストリン・カリックスアレーン・metal-organic cage が主要なホスト分子系。",
        "impact_summary": "超分子化学の基礎（Pedersen, Cram, Lehn 1987年ノーベル化学賞）。薬物放出制御・センサー・分子輸送・触媒空間設計に応用される。",
        "subfield": "化学",
        "school_of_thought": "超分子化学",
        "era_start": 1967,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1987/press-release/",
        "mathematical_formulation": r"K_a = \frac{[\text{HG}]}{[\text{H}][\text{G}]}, \quad \Delta G^\circ = -RT\ln K_a",
        "data_completeness": 87
    },
    {
        "name_ja": "電気化学・電気分解",
        "name_en": "Electrochemistry and Electrolysis",
        "name_original": "Electrochemistry",
        "definition": "電気エネルギーと化学変化の相互変換を扱う分野。ファラデーの法則（m = MIt/nF）に基づき、電解めっき・アルミニウム製錬・塩素-苛性ソーダ製造が工業化。サイクリックボルタンメトリー・電気化学インピーダンス分光法（EIS）で電極過程を解析する。",
        "impact_summary": "バッテリー・燃料電池・電解水素製造・電気めっきなどエネルギー技術の中核。Faraday（1831–1834）の定量法則が電気化学の基礎を確立。",
        "subfield": "化学",
        "school_of_thought": "物理化学",
        "era_start": 1834,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.rsc.org/periodic-table/",
        "mathematical_formulation": r"m = \frac{MIt}{nF}, \quad E = E^\circ - \frac{RT}{nF}\ln Q \text{ (Nernst)}",
        "data_completeness": 88
    },
    {
        "name_ja": "光化学・光触媒",
        "name_en": "Photochemistry and Photocatalysis",
        "name_original": "Photochemistry",
        "definition": "光子の吸収による分子の励起状態から生じる化学反応を扱う。Grotthuss-Draper則・Einstein光量子則・Jablonski図により励起→蛍光/燐光/光反応経路を記述。二酸化チタン光触媒（Honda-Fujishima効果）は水分解・環境浄化に応用され、有機光レドックス触媒が現代有機合成の主流となった。",
        "impact_summary": "藤嶋昭（Fujishima, East_Asia）の光触媒発見（1972 Nature）が太陽光エネルギー変換研究を開拓。有機フォトレドックス触媒はプロセス化学を変革した。",
        "subfield": "化学",
        "school_of_thought": "光化学",
        "era_start": 1843,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nature.com/articles/238037a0",
        "mathematical_formulation": r"E = h\nu, \quad \Phi = \frac{\text{molecules reacted}}{\text{photons absorbed}}",
        "data_completeness": 87
    },
    {
        "name_ja": "アラビア錬金術から近代化学へ（ジャービル・イブン・ハイヤーン）",
        "name_en": "Arabic Alchemy: Jabir ibn Hayyan",
        "name_original": "جابر بن حيان",
        "definition": "ジャービル（ゲーバー、c.721–c.815）はアッバース朝期に活動したイスラーム圏の錬金術師・化学者。蒸留・昇華・結晶化・酸の製造（硝酸・塩酸・硫酸の原型）を体系化し、実験的アプローチによる化学知識の蓄積を推進した。中世ヨーロッパにラテン語訳で伝わりGeber名で知られる。",
        "impact_summary": "イスラーム科学の化学的遺産がヨーロッパ錬金術・近代化学の基礎を形成。王水（aqua regia）など多数の試薬発見の帰属元であり、実験化学の源流とみなされる。",
        "subfield": "化学",
        "school_of_thought": "イスラーム科学",
        "era_start": 776,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.britannica.com/biography/Jabir-ibn-Hayyan",
        "data_completeness": 85
    },
    {
        "name_ja": "高分子科学・高分子合成",
        "name_en": "Polymer Science and Synthesis",
        "name_original": "Polymer Science",
        "definition": "共有結合で連結されたモノマー単位からなるマクロ分子（高分子）の合成・構造・物性・応用を扱う分野。Staudinger（マクロ分子仮説 1920年）からNylonの発明（Carothers 1935年）・Ziegler-Natta重合（1950年代）・リビングラジカル重合（1990年代）まで進化。",
        "impact_summary": "プラスチック・合成繊維・ゴム・コーティング材料など現代文明の素材基盤。生分解性ポリマー・導電性ポリマー（Heeger, MacDiarmid, Shirakawa 2000年ノーベル化学賞）が次世代展開。",
        "subfield": "化学",
        "school_of_thought": "高分子化学",
        "era_start": 1920,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2000/press-release/",
        "mathematical_formulation": r"\bar{M}_n = \frac{\sum N_i M_i}{\sum N_i}, \quad \bar{M}_w = \frac{\sum N_i M_i^2}{\sum N_i M_i}",
        "data_completeness": 88
    },
    {
        "name_ja": "インド伝統化学・ラサシャーストラと水銀化学",
        "name_en": "Indian Traditional Chemistry: Rasashastra",
        "name_original": "रसशास्त्र",
        "definition": "ラサシャーストラはインドの伝統的水銀・金属化学体系（8–12世紀に体系化）。Nagarjuna（龍樹, c.2–3世紀）らが水銀精製・金属酸化物（バスマ）・硫化物の調製を記述し、Ayurveda医薬として内服・外用に用いた。現代から見れば水銀毒性の問題もあるが、金属変換・精製技術の先進事例。",
        "impact_summary": "インド亜大陸における冶金・薬学・化学の統合的発展の証拠。WHO/UNESCOも伝統知識として記録し、現代の薬用金属ナノ粒子研究との接続が議論されている。",
        "subfield": "化学",
        "school_of_thought": "インド伝統科学",
        "era_start": 800,
        "culture_region": "South_Asia",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3149399/",
        "data_completeness": 82
    },
    {
        "name_ja": "アフリカ伝統金属製錬・鉄冶金",
        "name_en": "African Iron Smelting and Traditional Metallurgy",
        "name_original": "African Iron Smelting",
        "definition": "サブサハラアフリカでは紀元前1000年頃から独自の鉄製錬技術が発達し（タンザニア・ハヤ族の炉は欧州の製法より500年先行との説）、高炭素鋼・大型炉設計など地域固有の冶金化学知識が蓄積された。Haaland（1980年代）らの発掘調査がこの独立発明を実証。",
        "impact_summary": "アフリカの冶金技術がユーラシアから独立して発展した歴史的証拠。草地の分析・炉温度管理・還元雰囲気制御など化学的洗練度の高さが評価される。",
        "subfield": "化学",
        "school_of_thought": "アフリカ科学史",
        "era_start": -1000,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.jstor.org/stable/524801",
        "data_completeness": 80
    },
    {
        "name_ja": "界面活性剤・コロイド科学",
        "name_en": "Surfactant and Colloid Science",
        "name_original": "Surfactant Science",
        "definition": "疎水性と親水性の両部位を持つ両親媒性分子（界面活性剤）が気液・液液・固液界面に吸着し、臨界ミセル濃度（CMC）以上でミセル・ベシクル・ラメラ相などの自己集合構造を形成する科学。石鹸・洗剤・エマルジョン・マイクロエマルジョン・医薬品リポソームが応用系。",
        "impact_summary": "食品・製薬・化粧品・化学工業の製品基盤。リポソーム（mRNAワクチン送達系）の開発はCOVID-19ワクチン（BioNTech/Moderna）の基礎科学として2021–22年に注目された。",
        "subfield": "化学",
        "school_of_thought": "物理化学",
        "era_start": 1913,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.rsc.org/journals-books-databases/find-an-article/journals-jrnl-det/?jrnlid=3",
        "mathematical_formulation": r"\gamma = \gamma_0 - \frac{RT}{\omega}\ln\!\left(1 + \frac{c}{a}\right) \text{ (Frumkin isotherm)}",
        "data_completeness": 85
    },
    {
        "name_ja": "生体直交反応・クリックケミストリー",
        "name_en": "Bioorthogonal Chemistry and Click Chemistry",
        "name_original": "Click Chemistry",
        "definition": "生体内条件（水・中性pH・低温・希薄濃度）で副反応なく特定の官能基同士が選択的に反応する「クリックケミストリー」。銅触媒アジド-アルキン環化付加（CuAAC）、SPAAC、逆電子需要Diels-Alder反応などが代表。Sharpless, Meldal, Bertozzi が2022年ノーベル化学賞受賞。",
        "impact_summary": "生体分子の蛍光標識・医薬品接合・材料修飾を生細胞・生体内で可能にした。抗体薬物複合体（ADC）や生体内画像化への応用が急拡大している（2022年ノーベル化学賞）。",
        "subfield": "化学",
        "school_of_thought": "有機化学",
        "era_start": 2001,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2022/press-release/",
        "mathematical_formulation": r"\text{CuAAC: } R-N_3 + R'-C\equiv CH \xrightarrow{Cu(I)} \text{1,2,3-triazole}",
        "data_completeness": 90
    },
    {
        "name_ja": "中国伝統本草学と化学物質の単離",
        "name_en": "Chinese Traditional Materia Medica: Phytochemical Isolation",
        "name_original": "本草学",
        "definition": "中国の本草学（神農本草経 c.200CE、李時珍『本草綱目』1596年）は植物・鉱物・動物由来の薬物約1800種を体系化。20世紀以降、アルテミシニン（Tu Youyou/屠呦呦、2015年ノーベル生理学・医学賞）など有効成分の化学的単離・構造決定・合成が進んだ。",
        "impact_summary": "屠呦呦によるアルテミシニン発見（マラリア治療）は本草学由来の近代化学の最高到達点として世界的に評価された（2015年ノーベル賞）。伝統知と現代化学の統合事例として研究継続。",
        "subfield": "化学",
        "school_of_thought": "東アジア科学",
        "era_start": 200,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2015/press-release/",
        "data_completeness": 88
    },
]

CHEM_BATCH2 = [
    {
        "name_ja": "量子化学・分子軌道法",
        "name_en": "Quantum Chemistry and Molecular Orbital Theory",
        "name_original": "Quantum Chemistry",
        "definition": "量子力学を分子の電子構造に適用する分野。Hartree-Fock法・密度汎関数理論（DFT）・MP2/CCSD(T)等のポストHF法により、化学結合エネルギー・反応経路・分子スペクトルを第一原理から計算する。Kohn-ShamのDFTが1998年ノーベル化学賞（Kohn, Pople）。",
        "impact_summary": "コンピュータ化学（computational chemistry）の理論基盤。医薬品設計・触媒設計・材料探索にDFT計算は必須ツール。AlphaFold2もDFTデータで訓練されたポテンシャル関数を使用。",
        "subfield": "化学",
        "school_of_thought": "理論化学",
        "era_start": 1926,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1998/press-release/",
        "mathematical_formulation": r"\hat{H}\Psi = E\Psi, \quad E_{DFT}[n] = T_s[n] + E_{ext}[n] + E_H[n] + E_{xc}[n]",
        "data_completeness": 92
    },
    {
        "name_ja": "カーボンナノチューブと炭素材料化学",
        "name_en": "Carbon Nanotube and Carbon Materials Chemistry",
        "name_original": "Carbon Nanotubes",
        "definition": "グラフェンシートを円筒状に巻いた単層（SWCNT）・多層（MWCNT）カーボンナノチューブ（飯島澄男 1991年）は、直径数nmで高い弾性率（~1 TPa）・電気伝導性・熱伝導性を示す。フラーレン（C60、Kroto, Curl, Smalley 1996年ノーベル化学賞）とともにnano-carbonファミリーを形成。",
        "impact_summary": "CNTは複合材料・電子素子・薬物送達・水処理膜への応用が研究中。飯島澄男（East_Asia）の発見は材料化学の新時代を拓き、現在のグラフェン研究（2010年ノーベル物理学賞）の先駆。",
        "subfield": "化学",
        "school_of_thought": "ナノ化学",
        "era_start": 1991,
        "culture_region": "East_Asia",
        "source_url": "https://www.nature.com/articles/354056a0",
        "mathematical_formulation": r"C_h = n\mathbf{a}_1 + m\mathbf{a}_2, \quad d = \frac{a\sqrt{n^2+nm+m^2}}{\pi}",
        "data_completeness": 88
    },
    {
        "name_ja": "生物無機化学・金属酵素",
        "name_en": "Bioinorganic Chemistry and Metalloenzymes",
        "name_original": "Bioinorganic Chemistry",
        "definition": "生体内での金属イオン（Fe, Cu, Zn, Mn, Mo, V等）の役割と金属含有生体分子を扱う。ヘモグロビン（Fe-O2結合）、ニトロゲナーゼ（N2固定、Fe-Mo-Sクラスター）、チトクロームP450（酸化触媒）、カルボニックアンヒドラーゼ（Zn酵素、CO2水和）が典型例。",
        "impact_summary": "金属による生命機能（酸素輸送・N2固定・光合成・DNA修復）の化学的理解。MRI造影剤・抗癌金属錯体（シスプラチン）・ソーラー燃料（人工光合成）の設計に直結。",
        "subfield": "化学",
        "school_of_thought": "生物化学",
        "era_start": 1960,
        "culture_region": "North_America_Europe",
        "source_url": "https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Bioinorganic_Chemistry",
        "mathematical_formulation": r"k_{cat}/K_M \leq k_{diff} \approx 10^8\text{--}10^9\ \text{M}^{-1}\text{s}^{-1}",
        "data_completeness": 85
    },
    {
        "name_ja": "中東アラビアの錬金術・蒸留技術（アル-ラーズィー）",
        "name_en": "Al-Razi and Arabic Distillation Techniques",
        "name_original": "أبو بكر الرازي",
        "definition": "アル-ラーズィー（Rhazes, 865–925）はペルシャ出身のイスラーム医師・化学者で、蒸留装置（alembic）・昇華・ろ過・結晶化など実験的化学操作を系統化した。著書「秘密の書（Kitab al-Asrar）」は化学物質を動物・植物・鉱物・誘導体・その他に分類した最初期の体系。",
        "impact_summary": "アル-ラーズィーの実験的方法論はヨーロッパ錬金術・化学に伝わり近代化学の先駆。エタノールの医療応用（傷口消毒）を初めて記述したとされる。",
        "subfield": "化学",
        "school_of_thought": "イスラーム科学",
        "era_start": 865,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.britannica.com/biography/al-Razi",
        "data_completeness": 80
    },
    {
        "name_ja": "有機金属化学・グリニャール反応",
        "name_en": "Organometallic Chemistry and Grignard Reaction",
        "name_original": "Grignard Reaction",
        "definition": "金属と炭素の直接結合を持つ有機金属化合物の合成・反応性を扱う分野。グリニャール試薬（RMgX、Grignard 1912年ノーベル化学賞）から金属カルベン・フェロセン（Wilkinson, Fischer 1973年ノーベル化学賞）・オレフィンメタセシス（2005年ノーベル化学賞）まで展開。",
        "impact_summary": "医薬品・農薬・ポリマー合成における炭素骨格構築の主要ツール。クロスカップリング（鈴木、根岸、Heck 2010年ノーベル化学賞）は製薬合成に革命をもたらした。",
        "subfield": "化学",
        "school_of_thought": "有機化学",
        "era_start": 1900,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2010/press-release/",
        "mathematical_formulation": r"R-X + Mg \rightarrow R-MgX, \quad R-MgX + R'-CHO \rightarrow R-CH(OH)-R'",
        "data_completeness": 88
    },
    {
        "name_ja": "天然物化学・二次代謝産物",
        "name_en": "Natural Products Chemistry",
        "name_original": "Natural Products Chemistry",
        "definition": "生物（植物・微生物・海洋生物）が産生する構造的に複雑な有機化合物（二次代謝産物）の単離・構造決定・生合成・全合成を扱う。ペニシリン・ストレプトマイシン・モルヒネ・タキソール・アルテミシニン・エリスロマイシンなどが代表。",
        "impact_summary": "現代医薬品の50%以上が天然物由来または誘導体。抗菌・抗癌・抗マラリア薬の多くが天然物化学に起源を持ち、生物多様性保護の経済的根拠にもなっている。",
        "subfield": "化学",
        "school_of_thought": "有機化学",
        "era_start": 1860,
        "culture_region": "North_America_Europe",
        "source_url": "https://pubs.acs.org/journal/jnprdf",
        "data_completeness": 87
    },
    {
        "name_ja": "原子・分子シミュレーション（分子動力学法）",
        "name_en": "Molecular Dynamics Simulation",
        "name_original": "Molecular Dynamics",
        "definition": "原子・分子の運動をNewton運動方程式を数値積分して追跡するシミュレーション手法。AMBER・CHARMM・NAMD・GROMACSなどのプログラムを用いてタンパク質折り畳み・膜動態・薬物-受容体相互作用を解析。Karplus, Levitt, Warshel が2013年ノーベル化学賞受賞。",
        "impact_summary": "MD法は実験では直接観察困難なナノ秒-マイクロ秒スケールの分子運動を可視化。COVID-19治療薬（ニルマトレルビル）の設計にも活用された（2013年ノーベル化学賞）。",
        "subfield": "化学",
        "school_of_thought": "計算化学",
        "era_start": 1957,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2013/press-release/",
        "mathematical_formulation": r"m_i\ddot{\mathbf{r}}_i = -\nabla_i U(\mathbf{r}_1,\ldots,\mathbf{r}_N), \quad U = \sum_{\text{bonds}} + \sum_{\text{angles}} + \sum_{ij}V_{ij}(r)",
        "data_completeness": 90
    },
    {
        "name_ja": "固体化学・無機固体合成",
        "name_en": "Solid-State Chemistry and Inorganic Synthesis",
        "name_original": "Solid-State Chemistry",
        "definition": "結晶・非晶質・セラミクス・ゼオライト・超伝導体など固体無機材料の合成・構造・性質の関係を扱う。高温固相反応・水熱合成・Sol-Gel法・化学気相蒸着（CVD）・共沈殿法が主要合成法。X線回折・中性子散乱・電子顕微鏡が構造解析手段。",
        "impact_summary": "セラミクス超伝導体（LaBaCuO系 Bednorz-Müller 1987年ノーベル物理学賞）・固体酸化物燃料電池・ゼオライト触媒・リチウムイオン電池材料（Goodenough, Whittingham, Yoshino 2019年ノーベル化学賞）が代表的成果。",
        "subfield": "化学",
        "school_of_thought": "無機化学",
        "era_start": 1850,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2019/press-release/",
        "data_completeness": 87
    },
    {
        "name_ja": "分離化学・クロマトグラフィー高度展開",
        "name_en": "Separation Science and Advanced Chromatography",
        "name_original": "Separation Science",
        "definition": "混合物から目的成分を純化する分離科学の発展形。高速液体クロマトグラフィー（HPLC）・超臨界流体クロマトグラフィー（SFC）・毛細管電気泳動（CE）・二次元LC・LC-MS/MSが主要技術。医薬品規格試験・環境分析・プロテオミクスに不可欠。",
        "impact_summary": "製薬・食品・環境・法医学分野の品質管理の根幹技術。LC-MS/MSはドーピング検査・残留農薬分析・タンパク質同定（プロテオミクス）で世界標準となっている。",
        "subfield": "化学",
        "school_of_thought": "分析化学",
        "era_start": 1906,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.chromatographyonline.com/",
        "data_completeness": 85
    },
    {
        "name_ja": "核化学・放射化学",
        "name_en": "Nuclear Chemistry and Radiochemistry",
        "name_original": "Nuclear Chemistry",
        "definition": "放射性核種の生成・崩壊・核反応・化学挙動を扱う。放射性炭素年代測定（14C）・中性子放射化分析・放射性医薬品（PET/SPECTトレーサー）・核燃料サイクル・放射性廃棄物処理が応用領域。Curie夫妻（1903、1911年ノーベル賞）・Hahn（核分裂発見 1944年ノーベル化学賞）が先駆者。",
        "impact_summary": "放射性医薬品（FDG-PET、99mTc-MDP）が癌・認知症の早期診断を可能に。加速器生産放射性同位体の医療・産業利用が拡大中。",
        "subfield": "化学",
        "school_of_thought": "核化学",
        "era_start": 1898,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.iaea.org/topics/radiochemistry",
        "mathematical_formulation": r"N(t) = N_0 e^{-\lambda t}, \quad t_{1/2} = \frac{\ln 2}{\lambda}",
        "data_completeness": 87
    },
]

BIO_BATCH = [
    {
        "name_ja": "CRISPR-Cas9ゲノム編集",
        "name_en": "CRISPR-Cas9 Genome Editing",
        "name_original": "CRISPR-Cas9",
        "definition": "細菌の免疫機構（CRISPR配列とCasヌクレアーゼ）を改変した、標的配列特異的なゲノム編集技術。Doudna・Charpentierが2020年ノーベル化学賞受賞。ガイドRNA（gRNA）がDNA標的を認識し、Cas9ヌクレアーゼが切断。HDR・NHEJ・塩基編集・プライム編集により遺伝子修正が可能。",
        "impact_summary": "農業（ゲノム編集作物）・医療（鎌状赤血球症・β-サラセミア遺伝子治療）・基礎研究（遺伝子機能解析）を一変させた革命的技術（2020年ノーベル化学賞）。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "分子生物学",
        "era_start": 2012,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2020/press-release/",
        "mathematical_formulation": r"\text{PAM: 5'-NGG-3', on-target score} = \prod_i w_i \delta_{s_i,g_i}",
        "data_completeness": 92
    },
    {
        "name_ja": "エピジェネティクス",
        "name_en": "Epigenetics",
        "name_original": "Epigenetics",
        "definition": "DNA配列を変えずに遺伝子発現を制御するメカニズムを扱う。DNAメチル化（5mC, 5hmC）・ヒストン修飾（アセチル化・メチル化・ユビキチン化）・クロマチンリモデリング・非コードRNA（miRNA, lncRNA）が主要機構。発生・分化・疾患・環境適応を制御。",
        "impact_summary": "癌（DNA高メチル化・ヒストン変異）・発達障害・老化のエピゲノム機構の解明。エピゲノム編集（dCas9-DNMT3A）・エピゲノム治療薬（HDAC阻害剤・BET阻害剤）が臨床応用へ展開。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "分子生物学",
        "era_start": 1942,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nature.com/subjects/epigenetics",
        "mathematical_formulation": r"m = \frac{\beta}{1-\beta}, \quad \beta = \frac{\text{mCpG}}{\text{mCpG} + \text{CpG}}",
        "data_completeness": 90
    },
    {
        "name_ja": "シングルセル解析（単一細胞オミクス）",
        "name_en": "Single-Cell Omics Analysis",
        "name_original": "Single-Cell RNA-seq",
        "definition": "個々の細胞のトランスクリプトーム（scRNA-seq）・エピゲノム（scATAC-seq）・ゲノム（scDNA-seq）・タンパク質（CITE-seq）を同時または個別に測定する技術群。Seurat・SCANPY等のツールでクラスタリング・軌跡解析・細胞型同定を行う。10x Genomics Chromiumが標準プラットフォーム。",
        "impact_summary": "Human Cell Atlas（HCA）は全身の細胞型カタログ化を目標に単一細胞解析を基盤とする。癌の腫瘍内不均一性・脳の細胞種多様性・免疫細胞動態の解明に革命的影響。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "ゲノム科学",
        "era_start": 2009,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.humancellatlas.org/",
        "data_completeness": 90
    },
    {
        "name_ja": "神経科学的記憶メカニズム・海馬LTP",
        "name_en": "Hippocampal Memory and Long-Term Potentiation",
        "name_original": "Long-Term Potentiation",
        "definition": "海馬の神経回路における長期増強（LTP）は、高頻度刺激後にシナプス伝達効率が持続的に増加する現象で（Bliss & Lømo 1973）、NMDA受容体のCa2+流入が引き金となりAMPA受容体の増加・構造的シナプス増大が起きる。手続き記憶・エピソード記憶・空間記憶の神経基盤。",
        "impact_summary": "O'Keefe（場所細胞発見）とMoser夫妻（格子細胞発見）が2014年ノーベル生理学・医学賞受賞。アルツハイマー病における海馬萎縮・LTP障害との関連から治療標的として研究が続く。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "神経科学",
        "era_start": 1973,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2014/press-release/",
        "mathematical_formulation": r"w_{ij}(t+1) = w_{ij}(t) + \eta \cdot x_i \cdot y_j \text{ (Hebbian rule)}",
        "data_completeness": 88
    },
    {
        "name_ja": "幹細胞生物学・ips細胞",
        "name_en": "Stem Cell Biology and iPSC",
        "name_original": "iPSC: induced Pluripotent Stem Cell",
        "definition": "山中伸弥（Yamanaka, 2006）が発見した人工多能性幹細胞（iPSC）は、体細胞にOct4・Sox2・Klf4・c-Mycの4転写因子（山中因子）を導入して胚性幹細胞（ES細胞）様の多能性を再獲得させた革新的技術。患者由来iPSCからの分化細胞は疾患モデルと再生医療に活用される。",
        "impact_summary": "山中伸弥（East_Asia）がGurdon（核移植）と共に2012年ノーベル生理学・医学賞受賞。倫理問題の少ない多能性幹細胞源として、網膜色素上皮・心筋細胞・ニューロンへの分化と移植研究が進む。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "発生生物学",
        "era_start": 2006,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2012/press-release/",
        "data_completeness": 92
    },
    {
        "name_ja": "合成生物学",
        "name_en": "Synthetic Biology",
        "name_original": "Synthetic Biology",
        "definition": "工学的アプローチで生物部品（プロモーター・リプレッサー・酵素）を設計・組み合わせて新機能を持つ生命システムを構築する分野。BioBrick標準部品・遺伝子回路（トグルスイッチ・振動回路）・代謝経路工学・最小ゲノム（JCVI-syn3.0）が代表的成果。",
        "impact_summary": "バイオ医薬品・バイオ燃料・生体センサー・環境修復微生物の設計基盤。Venter研究所による初の人工細菌ゲノム合成（2010年）が一里塚。抗マラリア薬アルテミシニンの酵母生産が工業化された。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "バイオテクノロジー",
        "era_start": 2000,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.synbiotools.org/",
        "mathematical_formulation": r"\frac{dx}{dt} = \beta\frac{K^n}{K^n + y^n} - \gamma x \text{ (genetic toggle)}",
        "data_completeness": 88
    },
    {
        "name_ja": "ウイルス学・ウイルス-宿主相互作用",
        "name_en": "Virology and Virus-Host Interactions",
        "name_original": "Virology",
        "definition": "ウイルスの構造・複製・進化・宿主との相互作用を扱う。DNAウイルス・RNAウイルス・レトロウイルス・バクテリオファージの複製サイクル・免疫逃避・病原性機構を解析。COVID-19（SARS-CoV-2）の出現でスパイクタンパク質・ACE2受容体相互作用・ウイルス進化動態が世界的注目を浴びた。",
        "impact_summary": "mRNAワクチン（BioNTech/Moderna）はウイルス学研究の直接的成果。B型・C型肝炎ウイルスの発見（2020年ノーベル生理学・医学賞：Alter, Houghton, Rice）は数億人の医療を変えた。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "微生物学",
        "era_start": 1898,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2020/press-release/",
        "data_completeness": 88
    },
    {
        "name_ja": "神経細胞回路形成・シナプス発生",
        "name_en": "Neural Circuit Formation and Synaptogenesis",
        "name_original": "Neural Circuit Development",
        "definition": "神経細胞の軸索伸長・ターゲット認識・シナプス形成・刈り込み（pruning）の分子機構を扱う。ネトリン・セマフォリン・エフリン等の軸索ガイダンス分子と受容体（DCC/UNC5・PlexinA/Neuropilin・EphB/ephrin）が回路形成を制御。Sperry（キメラ眼実験 1981年ノーベル賞）が基礎を確立。",
        "impact_summary": "自閉症スペクトラム障害・統合失調症のシナプス機能不全機構の解明につながり、神経発達障害治療薬開発の標的探索に貢献。脳オルガノイドを用いた回路形成研究が急進展。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "発生神経生物学",
        "era_start": 1950,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.cell.com/neuron/home",
        "data_completeness": 85
    },
    {
        "name_ja": "植物ホルモン・植物シグナル伝達",
        "name_en": "Plant Hormones and Signaling",
        "name_original": "Phytohormone Signaling",
        "definition": "植物の成長・分化・ストレス応答を制御するホルモン系を扱う。オーキシン（細胞伸長・根形成）・サイトカイニン（細胞分裂・葉緑体分化）・ジベレリン（茎伸長・種子発芽）・アブシジン酸（ABA、気孔閉鎖・種子休眠）・エチレン（果実成熟）・ブラシノステロイド・ストリゴラクトンが主要ホルモン。",
        "impact_summary": "農業における作物収量・ストレス耐性改善の基盤。矮性品種（Green Revolution品種）はジベレリン応答性変異に由来。ジャスモン酸（JA）シグナルによる病害虫抵抗性強化が農薬代替として研究中。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "植物生物学",
        "era_start": 1880,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.plantcell.org/",
        "mathematical_formulation": r"[ABA]_c = K_p \cdot [ABA]_v \cdot \exp\!\left(\frac{z_v - z_c}{RT/F}\right)",
        "data_completeness": 85
    },
    {
        "name_ja": "インド伝統医学・アーユルヴェーダの薬草学",
        "name_en": "Ayurveda Pharmacognosy and Ethnobotany",
        "name_original": "आयुर्वेद",
        "definition": "アーユルヴェーダ（生命の科学）はインド亜大陸の伝統医学体系で、Charaka Samhita（c.600BCE）・Sushruta Samhita に薬草700種以上の処方が記述されている。アシュワガンダ（Withania somnifera）・ニーム（Azadirachta indica）・ウコン（クルクミン）などの生薬が現代の天然物医薬品研究の起点となっている。",
        "impact_summary": "クルクミンの抗炎症・抗酸化活性研究、アシュワガンダのアダプトゲン効果研究が国際的に展開。WHO伝統医学戦略（2019-2034）でアーユルヴェーダが公式認定される。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "インド伝統科学",
        "era_start": -600,
        "culture_region": "South_Asia",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3611645/",
        "data_completeness": 82
    },
    {
        "name_ja": "マイクロバイオーム・腸内細菌叢",
        "name_en": "Microbiome and Gut Microbiota",
        "name_original": "Human Microbiome",
        "definition": "ヒト体内（腸管・皮膚・口腔・肺等）に共生する微生物群集（細菌・真菌・ウイルス・古細菌）の集合体。Human Microbiome Project（HMP 2007–）が16S rRNA/ショットガンシーケンシングで全身のマイクロバイオームを解析。腸-脳軸・免疫調節・代謝疾患との関連が解明中。",
        "impact_summary": "腸内細菌叢は肥満・糖尿病・うつ病・癌免疫療法の反応性に影響することが示された。糞便微生物移植（FMT）がClostridium difficile感染症の標準治療として承認。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "微生物学",
        "era_start": 2007,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.hmpdacc.org/",
        "data_completeness": 90
    },
    {
        "name_ja": "免疫チェックポイント療法",
        "name_en": "Immune Checkpoint Therapy",
        "name_original": "Checkpoint Immunotherapy",
        "definition": "免疫チェックポイント（CTLA-4, PD-1, PD-L1）を阻害する抗体薬（ipilimumab, nivolumab, pembrolizumab等）によりT細胞の活性化を回復させ癌を攻撃する治療法。James Allison（CTLA-4）と本庶佑（PD-1/東アジア）が2018年ノーベル生理学・医学賞受賞。",
        "impact_summary": "黒色腫・肺癌・尿路上皮癌・ホジキンリンパ腫など多種癌に対する劇的な奏効率改善をもたらし、癌治療のパラダイムシフト（2018年ノーベル賞）。複合免疫療法（PD-1+CTLA-4）の相乗効果が研究中。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "免疫学",
        "era_start": 1995,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/medicine/2018/press-release/",
        "data_completeness": 92
    },
    {
        "name_ja": "アフリカの生物多様性と固有種進化",
        "name_en": "African Biodiversity and Endemic Species Evolution",
        "name_original": "African Biodiversity",
        "definition": "アフリカ大陸（サブサハラ・マダガスカル・コンゴ盆地・東アフリカ地溝帯）は世界最高の生物多様性を擁し、チクリッド魚類（ヴィクトリア湖の急速適応放散）・ラタニア属植物・ゴリラ・ボノボなど固有の進化事例を持つ。マダガスカルは固有種率90%を超える進化の実験室。",
        "impact_summary": "ヴィクトリア湖チクリッドは15,000年未満での500種以上の適応放散として進化速度研究の標準事例。アフリカの熱帯雨林・サバンナ・乾燥帯の生態系サービスは地球炭素循環の要。",
        "subfield": "生命科学・生物学",
        "school_of_thought": "進化生物学",
        "era_start": 1858,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.iucnredlist.org/",
        "data_completeness": 82
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n1 = insert_batch(conn, CHEM_BATCH1)
    n2 = insert_batch(conn, CHEM_BATCH2)
    n3 = insert_batch(conn, BIO_BATCH)
    conn.close()
    total_inserted = n1 + n2 + n3
    cursor2 = sqlite3.connect(DB_PATH).cursor()
    cursor2.execute("SELECT COUNT(*) FROM natural_discovery WHERE status='active'")
    total = cursor2.fetchone()[0]
    print(f"Batch19 chem4+bio2: {total_inserted} inserted (chem1={n1}, chem2={n2}, bio={n3}). Total: {total}")
