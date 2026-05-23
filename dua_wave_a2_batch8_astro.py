"""
DUA Wave A2 Batch 8 — 宇宙物理・天文学 (Astronomy & Astrophysics)
Target: ~60 concepts, current subfield count ~218, target ~368
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

BATCH1 = [
    {
        "name_ja": "ハーシェルの銀河構造モデル",
        "name_en": "Herschel's Model of the Milky Way",
        "definition": "ウィリアム・ハーシェル（1785年）が星数計測により天の川銀河の形状を初めて定量的に推定した。円盤状構造を示したが太陽を中心付近と誤推定した。ハーロー・シャプレー（1918年）が球状星団分布から太陽の周縁位置を修正。",
        "impact_summary": "銀河天文学の出発点。観測的方法論（星数計測→三次元構造推定）を確立し、後の星間消光補正・銀河回転曲線研究の端緒となった。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "観測天文学",
        "era_start": 1785,
        "culture_region": "Europe_Western",
        "source_url": "https://www.jstor.org/stable/25056",
        "data_completeness": 85
    },
    {
        "name_ja": "ケフェイド変光星と距離指標",
        "name_en": "Cepheid Variable Stars as Distance Indicators",
        "definition": "ヘンリエッタ・リービット（1912年）が小マゼラン雲のケフェイド変光星の周期と光度の比例関係（周期光度関係）を発見。ハッブルがアンドロメダ銀河のケフェイドを観測し（1924年）、宇宙の距離梯子の確立とM31の系外銀河性を証明した。",
        "impact_summary": "宇宙距離梯子の第一段。ハッブル定数測定・宇宙年齢・暗黒エネルギー研究の根幹データを提供し、現代宇宙論の観測的基盤をなす。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "観測天文学",
        "era_start": 1912,
        "culture_region": "North_America",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1083886/",
        "mathematical_formulation": r"M = \alpha \log P + \beta",
        "data_completeness": 90
    },
    {
        "name_ja": "銀河形態分類（ハッブルの音叉図）",
        "name_en": "Galaxy Morphological Classification",
        "definition": "エドウィン・ハッブル（1926年）が銀河を楕円銀河（E0〜E7）・レンズ状銀河（S0）・渦巻銀河（Sa〜Sc / SBa〜SBc）・不規則銀河に分類した形態系列。「音叉図」はその視覚的表現。形態は星形成史・環境・合体を反映する。",
        "impact_summary": "銀河天文学の基本語彙を確立。銀河形成理論・大規模構造・宇宙進化の観測的研究の出発点となり、今日も機械学習による自動分類に活用される。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "銀河天文学",
        "era_start": 1926,
        "culture_region": "North_America",
        "source_url": "https://ned.ipac.caltech.edu/level5/March01/Sandage/Sandage1.html",
        "data_completeness": 88
    },
    {
        "name_ja": "電波天文学の誕生",
        "name_en": "Origin of Radio Astronomy",
        "definition": "カール・ジャンスキー（1933年）が電波雑音の中に銀河中心からの電波を発見し、電波天文学を創始。グローテ・レーバーが最初の電波望遠鏡（1937年）を自作。戦後に大型アンテナが建設され、パルサー・クエーサー・CMBが発見された。",
        "impact_summary": "可視光以外の電磁波で宇宙を観測する多波長天文学の先駆け。中性水素21cm線・マサー・宇宙背景放射・超大質量ブラックホールのジェット観測の基盤。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "電波天文学",
        "era_start": 1933,
        "culture_region": "North_America",
        "source_url": "https://www.nrao.edu/history/",
        "data_completeness": 88
    },
    {
        "name_ja": "宇宙マイクロ波背景放射の発見と構造",
        "name_en": "CMB Anisotropy and Structure",
        "definition": "宇宙背景放射（CMB、2.725K）のわずかな温度ゆらぎ（10万分の1）はビッグバン後38万年の密度揺らぎを記録し、現在の宇宙大規模構造の種とされる。COBE（1989年）・WMAP（2001年）・Planck（2009年）が高精度測定。",
        "impact_summary": "宇宙論パラメータ（ハッブル定数・暗黒物質・暗黒エネルギー密度）の精密決定。インフレーション理論の観測的検証・宇宙の平坦性・バリオン音響振動（BAO）発見の基盤。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1965,
        "culture_region": "North_America",
        "source_url": "https://www.cosmos.esa.int/web/planck",
        "mathematical_formulation": r"C_\ell = \frac{1}{2\ell+1}\sum_m |a_{\ell m}|^2",
        "data_completeness": 93
    },
    {
        "name_ja": "重力波天文学（LIGO/Virgo）",
        "name_en": "Gravitational Wave Astronomy",
        "definition": "LIGO（2015年9月検出、公表2016年2月）がブラックホール連星合体からの重力波GW150914を初観測。その後中性子星連星（GW170817）の重力波・電磁波同時観測でマルチメッセンジャー天文学が確立した。",
        "impact_summary": "重力波という新しい観測窓の開拓。ブラックホール・中性子星の質量・自転・合体頻度を直接測定し、ハッブル定数の独立測定・核物質状態方程式制約に貢献。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "相対論的天体物理学",
        "era_start": 2015,
        "culture_region": "North_America",
        "source_url": "https://www.ligo.caltech.edu/detection",
        "mathematical_formulation": r"h = \frac{2G}{c^4 r}\ddot{I}_{ij}",
        "data_completeness": 95
    },
    {
        "name_ja": "ニュートリノ天文学",
        "name_en": "Neutrino Astronomy",
        "definition": "太陽・超新星・高エネルギー宇宙線からのニュートリノを検出する天文学分野。SN1987A超新星ニュートリノ（1987年）・太陽ニュートリノ（小柴昌俊・カミオカンデ）・IceCubeによる宇宙ニュートリノ（2013年）が主要成果。",
        "impact_summary": "超新星爆発内部・太陽核融合過程・高エネルギー宇宙線加速源の直接観測を実現。ニュートリノ振動発見（梶田隆章・2015年ノーベル物理学賞）は素粒子標準模型を超えた最初の観測的証拠。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "粒子天体物理学",
        "era_start": 1987,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/2002/koshiba/facts/",
        "data_completeness": 90
    },
    {
        "name_ja": "宇宙の大規模構造（フィラメント・ボイド）",
        "name_en": "Large Scale Structure of the Universe",
        "definition": "銀河は孤立せず、フィラメント・シート・ノード（銀河団）・ボイドからなる宇宙の巨大スポンジ状構造（コズミックウェブ）を形成する。CfAレッドシフト調査（1986年）・SDSSが全球的マップを提供した。",
        "impact_summary": "宇宙論的N体シミュレーション（IllustrisTNG・EAGLE）の検証標的。バリオン音響振動（BAO）スケールが暗黒エネルギー状態方程式の測定に使われる。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1986,
        "culture_region": "Global",
        "source_url": "https://www.sdss.org/science/",
        "mathematical_formulation": r"P(k) = A k^n T^2(k)",
        "data_completeness": 90
    },
    {
        "name_ja": "銀河の衝突・合体と銀河進化",
        "name_en": "Galaxy Mergers and Galaxy Evolution",
        "definition": "銀河が重力相互作用・合体を繰り返して成長し、形態・星形成史・中心BH質量が変化する過程。ハッブル宇宙望遠鏡とJWSTが高赤方偏移銀河の合体を直接観測。天の川銀河とアンドロメダ銀河は約45億年後に衝突合体予定。",
        "impact_summary": "現在の銀河形態・大質量楕円銀河形成・AGNフィードバックの説明に不可欠。宇宙年齢にわたる質量集積プロセスを観測・シミュレーション双方から検証する研究分野。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "銀河天文学",
        "era_start": 1972,
        "culture_region": "Global",
        "source_url": "https://hubblesite.org/contents/media/images/2012/09/2980-Image.html",
        "data_completeness": 87
    },
    {
        "name_ja": "太陽物理学・太陽風",
        "name_en": "Solar Physics and Solar Wind",
        "definition": "太陽コロナ（数百万K）からプラズマが超音速で流れ出す現象（太陽風）をユージン・パーカー（1958年）が予言。惑星磁気圏との相互作用・宇宙天気・地磁気嵐・オーロラを生む。SDO・SOHO・パーカー太陽探査機が観測する。",
        "impact_summary": "宇宙天気予報・人工衛星・GPS・電力網の障害リスク評価の科学的基盤。太陽活動の11年周期と地球気候変動の関係も研究される。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "太陽物理学",
        "era_start": 1958,
        "culture_region": "North_America",
        "source_url": "https://sdo.gsfc.nasa.gov/",
        "mathematical_formulation": r"n m_p \left(\vec{v}\cdot\nabla\right)\vec{v} = -\nabla p - \frac{GM_\odot}{r^2}\hat{r}",
        "data_completeness": 88
    },
    {
        "name_ja": "惑星形成論・原始惑星系円盤",
        "name_en": "Planet Formation and Protoplanetary Disks",
        "definition": "恒星形成時の残存ガス・ダストが回転する円盤（原始惑星系円盤）を形成し、微惑星集積→惑星形成が進む。ALMAが高解像度で円盤リングとギャップを直接観測（2018年HL Tau等）。ニース・モデルが太陽系の後期重爆撃期を説明する。",
        "impact_summary": "太陽系形成史・系外惑星多様性の理論的基盤。巨大惑星の移動（グランド・タック仮説）・地球の水起源・生命可能惑星形成条件の研究枠組み。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "惑星科学",
        "era_start": 1944,
        "culture_region": "Global",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-astro-081201-145423",
        "data_completeness": 88
    },
    {
        "name_ja": "パルサーと中性子星物理学",
        "name_en": "Pulsars and Neutron Star Physics",
        "definition": "ジョスリン・ベル（1967年）がパルサー（規則的電波パルスを放出する高速回転中性子星）を発見。ミリ秒パルサー・パルサー連星（ハルス・テイラー1974年、重力波放射の間接証拠）・マグネターが後に発見。核物質の高密度相を実験室で再現できない唯一の天然「実験場」。",
        "impact_summary": "核物質状態方程式・量子重力・パルサータイミングアレイ（PTAによる確率的重力波背景の検出2023年）の研究拠点。精密時計としてGPS補正・将来の宇宙航行にも応用。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "相対論的天体物理学",
        "era_start": 1967,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/physics/1974/hewish/facts/",
        "data_completeness": 90
    },
    {
        "name_ja": "超新星爆発のメカニズムと元素合成",
        "name_en": "Supernova Mechanism and Nucleosynthesis",
        "definition": "Ia型（白色矮星の熱核暴走）とII型（大質量星のコア崩壊）の2メカニズムがある。バーバリッジ・バーバリッジ・ファウラー・ホイル（B2FH, 1957年）の論文が恒星元素合成の理論的基礎を確立。鉄より重い元素はr過程（中性子星合体）で生成。",
        "impact_summary": "「私たちは星くずでできている」という概念の科学的根拠。Ia型超新星の標準光源としての利用が宇宙加速膨張（暗黒エネルギー）の発見に直結した。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "核天体物理学",
        "era_start": 1957,
        "culture_region": "Europe_Western",
        "source_url": "https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.29.547",
        "data_completeness": 92
    },
    {
        "name_ja": "活動銀河核とクエーサー",
        "name_en": "Active Galactic Nuclei and Quasars",
        "definition": "超大質量ブラックホール（SMBH）への物質降着が極めて高光度の電磁放射を生む天体クラス。クエーサー（1963年、シュミット）は高赤方偏移の超高光度AGN。電波銀河・セイファート銀河・BLラックと統一スキームで分類される。",
        "impact_summary": "銀河中心のSMBHと銀河進化の共進化（BH-バルジ関係）研究の出発点。銀河形成フィードバック機構・宇宙再電離過程の研究の核となる天体物理現象。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "銀河天文学",
        "era_start": 1963,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/197170a0",
        "data_completeness": 90
    },
    {
        "name_ja": "系外惑星の大気特性解析",
        "name_en": "Exoplanet Atmosphere Characterization",
        "definition": "系外惑星のトランジット中に恒星光をフィルターとして大気組成・温度・雲を分光分析する技術。JWSTによりCO2・水蒸気・メタンの検出精度が飛躍的向上。生命居住可能性の評価に直結する。",
        "impact_summary": "「第二の地球」探索の最前線技術。JWSTのTRAPPIST-1e/f/g大気観測がバイオシグネチャー探索を現実的な近未来課題とした。系外生命存在の観測的手がかりを初めて提供しうる技術。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "惑星科学",
        "era_start": 2001,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/nature09922",
        "data_completeness": 90
    },
    {
        "name_ja": "恒星の色・温度・スペクトル分類",
        "name_en": "Stellar Spectral Classification",
        "definition": "フラウンホーファー線（1814年）から恒星大気組成を推定する分光技術。ハーバード分類（O・B・A・F・G・K・M型、温度順）をアニー・ジャンプ・キャノンが体系化（1901〜1915年）。HR図はスペクトル型と絶対等級の関係を示す。",
        "impact_summary": "恒星物理学・恒星進化理論の観測的基盤。白色矮星・赤色巨星・主系列星の分類と進化経路理解、銀河の星形成史推定に不可欠なツール。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "恒星物理学",
        "era_start": 1901,
        "culture_region": "North_America",
        "source_url": "https://www.cfa.harvard.edu/about/history/henry-draper-catalogue",
        "data_completeness": 88
    },
    {
        "name_ja": "インドの古代天文学（アリヤバッタ）",
        "name_en": "Ancient Indian Astronomy (Aryabhata)",
        "definition": "アリヤバッタ（499年）は地球の自転・月の満ち欠けの科学的説明・惑星運動の数学的モデル（円に近い楕円軌道推定）・日食・月食の正確な予測を確立した。彼の著作『アーリャバティーヤ』は算数・代数・三角法・球面天文学を統合した。",
        "impact_summary": "イスラム天文学を経由してヨーロッパ天文学に影響を与えた非西洋知識体系の最重要事例。地動説的発想の先駆けとして科学史上の再評価が進んでいる。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "科学史",
        "era_start": 499,
        "culture_region": "South_Asia",
        "source_url": "https://www.cambridge.org/core/books/aryabhatiya-of-aryabhata/",
        "data_completeness": 83
    },
    {
        "name_ja": "イスラム黄金時代の天文学",
        "name_en": "Islamic Golden Age Astronomy",
        "definition": "9〜13世紀のバグダード・カイロ・コルドバのイスラム学者がプトレマイオス天文学を批判的に継承・改良した。イブン・アル＝ハイサム（光学的天文観測批判）・アル＝バッターニ（歳差精度改良）・ウルグ・ベク（サマルカンド天文台）が代表的人物。",
        "impact_summary": "コペルニクス・ティコ・ケプラーへの直接的知識継承路。星座名・アルゴリズムの語源がアラビア語に由来する事実が科学の多元的起源を示す。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "科学史",
        "era_start": 820,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.cambridge.org/core/books/islamic-astronomy/",
        "data_completeness": 83
    },
    {
        "name_ja": "マヤ天文学と暦体系",
        "name_en": "Maya Astronomy and Calendar Systems",
        "definition": "古典期マヤ（250〜900年）は金星・月・太陽の精密な観測に基づく260日（ツォルキン）・365日（ハアブ）・長期暦（Long Count）を統合。金星の584日会合周期を0.02日以内の精度で計算。ドレスデン絵文書が天文表を記録。",
        "impact_summary": "記数法（位取り記数法・ゼロの概念）・天文観測・暦法における中米先住民の独自的高度発達の証拠。科学知識の多元的・独立的発展の典型事例として科学史上重要。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "科学史",
        "era_start": 250,
        "culture_region": "Americas_Indigenous",
        "source_url": "https://www.cambridge.org/core/books/maya-astronomy/",
        "data_completeness": 80
    },
    {
        "name_ja": "中国古代天文学と星図",
        "name_en": "Ancient Chinese Astronomy and Star Catalogs",
        "definition": "周代以降、中国は赤道座標系に基づく星官（星座）体系を独自に発展させた。甘徳・石申（BC4世紀）の星表は現存最古級の星位記録。張衡（渾天儀）・郭守敬（授時暦・1280年）が代表的。日食・彗星・新星（超新星）記録は現代天文学に利用される。",
        "impact_summary": "東アジア独自の天文学体系。超新星SN1054（かに星雲の原星）の記録は中国文献のみが詳細を保存し、現代天体物理学の基礎データとなっている。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "科学史",
        "era_start": -350,
        "culture_region": "East_Asia",
        "source_url": "https://www.cambridge.org/core/books/history-of-chinese-astronomy/",
        "data_completeness": 82
    },
    {
        "name_ja": "暗黒物質の観測的証拠",
        "name_en": "Observational Evidence for Dark Matter",
        "definition": "フリッツ・ツビッキー（1933年）の銀河団速度分散・ヴェラ・ルービン（1970年代）の銀河回転曲線・重力レンズ・弾丸銀河団（2006年）がビリアル質量と光度質量の乖離を示し、見えない「暗黒物質」の存在を確立した。",
        "impact_summary": "宇宙全エネルギーの27%を占める暗黒物質の探索は現代素粒子物理学・宇宙論の最大問題。WIMPs・アクシオン・無菌ニュートリノ等が候補として研究されている。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1933,
        "culture_region": "Global",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.astro.12.1.391",
        "data_completeness": 92
    },
    {
        "name_ja": "バリオン音響振動（BAO）",
        "name_en": "Baryon Acoustic Oscillations",
        "definition": "ビッグバン後38万年の光子-バリオン流体が音速で振動し、解放後に宇宙の密度揺らぎに固有スケール（現在約500 Mpc）を刻印した現象。銀河の2点相関関数・パワースペクトルのピークとして観測される標準物差し。",
        "impact_summary": "宇宙膨張史・暗黒エネルギー状態方程式の精密測定に使用される宇宙論的測定ツール。SDSS・DESI・ユークリッド衛星が多色測光で測定を続ける。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 2005,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/nature03466",
        "mathematical_formulation": r"d_s = \frac{2c}{3H_0 \Omega_m^{1/2}} \left[\frac{1}{a_{eq}^{1/2}} + \left(1 + \frac{R_{eq}}{3}\right)^{1/2}\right]^{-1}",
        "data_completeness": 88
    },
    {
        "name_ja": "マルチメッセンジャー天文学",
        "name_en": "Multi-Messenger Astronomy",
        "definition": "重力波・電磁波（ガンマ線・X線・可視光・電波）・ニュートリノの複数「メッセンジャー」を同時に観測して天体現象を解読する手法。GW170817（中性子星合体2017年）がr過程元素合成の直接証拠を提供した最初の事例。",
        "impact_summary": "天文学の新フロンティア。重力波・電磁波・ニュートリノの同時観測が核物質状態方程式・宇宙化学・高エネルギー素粒子過程の同時解明を可能にした。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "粒子天体物理学",
        "era_start": 2017,
        "culture_region": "Global",
        "source_url": "https://www.science.org/doi/10.1126/science.aap9811",
        "data_completeness": 90
    },
    {
        "name_ja": "ガンマ線バースト",
        "name_en": "Gamma-Ray Bursts",
        "definition": "宇宙で最大のエネルギー放出事象。数秒〜数分で銀河全光度の1000倍以上を放射する。短時間GRBは中性子星合体、長時間GRBは大質量星コア崩壊（極超新星）が起源。コンプトンガンマ線観測衛星（1991年）・BATSEが全天分布を確立。",
        "impact_summary": "宇宙で最も激しい爆発現象。高赤方偏移宇宙の探針・重元素合成・宇宙線加速・大量絶滅との関連（オルドビス紀大量絶滅仮説）など多分野と接続する。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "高エネルギー天体物理学",
        "era_start": 1967,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/378389a0",
        "data_completeness": 88
    },
    {
        "name_ja": "恒星の主系列と核燃焼段階",
        "name_en": "Stellar Main Sequence and Nuclear Burning Stages",
        "definition": "ヘルツシュプルング＝ラッセル（HR）図の主系列は水素核融合中の恒星が占める対角線。質量に応じてH燃焼→He燃焼→C/Ne/O/Si燃焼と進み、Feコアの重力崩壊で終わる（大質量星）か、惑星状星雲→白色矮星で終わる（低質量星）かが分岐する。",
        "impact_summary": "恒星天体物理学の中核。銀河の星形成史・化学進化・核合成収量の計算基盤。太陽の将来（50億年後の赤色巨星→白色矮星）を定量的に予測する。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "恒星物理学",
        "era_start": 1911,
        "culture_region": "Europe_Western",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.aa.17.090179.001523",
        "mathematical_formulation": r"L \propto M^{3.5}",
        "data_completeness": 90
    },
    {
        "name_ja": "宇宙論的赤方偏移と距離-赤方偏移関係",
        "name_en": "Cosmological Redshift and Distance-Redshift Relation",
        "definition": "宇宙膨張による光の波長伸長（赤方偏移z）と距離の関係。ハッブル（1929年）がz∝d（線形則）を発見。高赤方偏移ではフリードマン方程式が適用され、Ia型超新星のz-d関係から暗黒エネルギーが発見された（1998年）。",
        "impact_summary": "宇宙の膨張・年齢・幾何の観測的測定の基本手法。JWSTがz>10の最初期銀河を観測し、宇宙論モデルの精密検証を行っている。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1929,
        "culture_region": "North_America",
        "source_url": "https://www.pnas.org/doi/10.1073/pnas.15.3.168",
        "mathematical_formulation": r"d_L = (1+z) \int_0^z \frac{c\,dz'}{H(z')}",
        "data_completeness": 92
    },
    {
        "name_ja": "アストロメトリーと精密測距（ガイア衛星）",
        "name_en": "Astrometry and Precision Measurements",
        "definition": "恒星の位置・固有運動・視差を精密測定する天文学の基本分野。ESAのガイア衛星（2013年〜）は20億個の恒星の3次元位置・速度を10μ秒角精度で測定し、銀河系のダイナミクス・暗黒物質分布・近傍恒星の進化を解明しつつある。",
        "impact_summary": "宇宙距離梯子の最下段の精密化。ケフェイド変光星・標準光源の較正を改善し、ハッブル張力（局所測定値とCMB値の食い違い）問題の解明に寄与する。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "観測天文学",
        "era_start": 2013,
        "culture_region": "Europe_Western",
        "source_url": "https://www.cosmos.esa.int/web/gaia",
        "data_completeness": 90
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)

    total = 0
    for i, batch in enumerate([BATCH1], 1):
        n = insert_batch(conn, batch)
        total += n
        print(f"  Batch {i}: {n} inserted (running total: {total})")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"\nBatch8 astro: {total} concepts inserted")
    print(f"Total in table: {count}")
