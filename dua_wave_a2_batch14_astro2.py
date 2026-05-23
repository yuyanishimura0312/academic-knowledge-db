"""
DUA Wave A2 Batch 14 — Astronomy/Earth Science supplement
~60 concepts across '宇宙物理・天文学' and '地球科学・環境科学'
"""
import sqlite3
import uuid
from datetime import datetime, timezone

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

# Astronomy/Astrophysics concepts
ASTRO_BATCH = [
    {
        "name_ja": "電波天文学",
        "name_en": "Radio Astronomy",
        "definition": "宇宙から届く電波（波長1mm〜10m）を観測する天文学の分野。宇宙背景放射・パルサー・中性水素21cm線・クェーサー・電波銀河の観測が主要テーマ。",
        "impact_summary": "Jansky(1932)が宇宙電波を発見。ジョドレルバンク・VLA・ALMA・SKAなどの電波望遠鏡が宇宙の精密地図を作成。宇宙背景放射の精密観測が標準宇宙論を確立。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Observational Astronomy",
        "era_start": 1932,
        "culture_region": "North_America",
        "source_url": "https://public.nrao.edu/radio-astronomy/what-is-radio-astronomy/",
        "data_completeness": 88,
    },
    {
        "name_ja": "X線天文学",
        "name_en": "X-ray Astronomy",
        "definition": "宇宙から到達するX線（0.1–100 keV）を観測する天文学。中性子星・白色矮星降着円盤・ブラックホールX線連星・銀河団の高温ガス（ICM）が主要天体。",
        "impact_summary": "Giacconi(2002 Nobel)がX線源（Sco X-1）を発見（1962）。ROSAT・XMM-Newton・Chandra・NuSTAR・eROSITAが全天X線サーベイ。銀河団質量・活動銀河核の物理解明に不可欠。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "High Energy Astrophysics",
        "era_start": 1962,
        "culture_region": "North_America",
        "source_url": "https://chandra.harvard.edu/xray_astro/what_is_xray_astro.html",
        "data_completeness": 88,
    },
    {
        "name_ja": "重力波天文学",
        "name_en": "Gravitational Wave Astronomy",
        "definition": "時空の歪みとして伝播する重力波を検出し宇宙天体（連星ブラックホール・中性子星合体等）の物理を解明する天文学の新領域。LIGOとVirgoが主要観測機関。",
        "impact_summary": "GW150914（2015）で史上初の連星BH合体を検出（Barish・Thorne・Weiss 2017 Nobel）。GW170817（中性子星合体）が電磁波マルチメッセンジャー天文学を開拓し重元素起源を解明。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Gravitational Wave Physics",
        "era_start": 2015,
        "culture_region": "North_America",
        "source_url": "https://www.ligo.caltech.edu/",
        "mathematical_formulation": r"h_{+,\times} \sim \frac{G}{c^4 r}\ddot{I}_{ij}, \quad h \sim 10^{-21}",
        "data_completeness": 91,
    },
    {
        "name_ja": "ガンマ線バースト",
        "name_en": "Gamma-Ray Bursts",
        "definition": "宇宙で最も明るい爆発現象。持続時間でショート型（中性子星合体起源）とロング型（大質量星の重力崩壊起源）に分類。赤方偏移z>8の最遠方天体も検出されている。",
        "impact_summary": "Swift・Fermi衛星が観測。GRBの残光で高赤方偏移宇宙の化学進化・再電離史を探索。ショート型GRBは中性子星合体の電磁波対応天体（キロノバ）として重元素合成の現場。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "High Energy Astrophysics",
        "era_start": 1967,
        "culture_region": "North_America",
        "source_url": "https://fermi.gsfc.nasa.gov/science/eteu/grbs/",
        "mathematical_formulation": r"E_{\text{iso}} \sim 10^{51}-10^{54}\,\text{erg}, \quad L \sim 10^{51}\,\text{erg/s}",
        "data_completeness": 87,
    },
    {
        "name_ja": "系外惑星の大気分光",
        "name_en": "Exoplanet Atmospheric Spectroscopy",
        "definition": "トランジット中の透過スペクトルや二次食の熱放射スペクトルから系外惑星大気成分（H₂O・CO₂・メタン・酸素等）を検出する観測手法。JWSTが高精度化を実現。",
        "impact_summary": "JWST(2022)がTRAPPIST-1e・TOI-700dなどハビタブルゾーン惑星の大気探索を開始。生命の化学的サインを宇宙規模で探す「宇宙生命天文学」の最前線。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Planetary Science",
        "era_start": 2002,
        "culture_region": "North_America",
        "source_url": "https://www.stsci.edu/jwst/science-execution/approved-programs",
        "data_completeness": 88,
    },
    {
        "name_ja": "パルサーとパルサータイミングアレイ",
        "name_en": "Pulsars and Pulsar Timing Arrays",
        "definition": "高速回転する中性子星（パルサー）が放射する規則正しいパルス電波。パルサータイミングアレイ（PTA）は複数のパルサーを使ってナノヘルツ帯の重力波背景を検出する手法。",
        "impact_summary": "Hewish・Bell Burnell(1974 Nobel)が発見。二重パルサーが重力波の間接的証拠（Hulse・Taylor 1993 Nobel）を提供。2023年NANOGrav等PTA連合が重力波背景の証拠を報告。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "High Energy Astrophysics",
        "era_start": 1967,
        "culture_region": "Europe_Western",
        "source_url": "https://nanograv.org/",
        "mathematical_formulation": r"P\dot{P} = \frac{4\pi^2 I}{c^3}\left(\frac{dE}{dt}\right)^{-1}\dot{E}",
        "data_completeness": 88,
    },
    {
        "name_ja": "銀河の形成と進化",
        "name_en": "Galaxy Formation and Evolution",
        "definition": "宇宙初期の密度揺らぎから現在の多様な銀河形態（楕円・渦巻・不規則）が形成される過程のシミュレーションと観測的研究。階層的構造形成・フィードバック・再電離期が核心テーマ。",
        "impact_summary": "ハッブル宇宙望遠鏡・JWSTが高赤方偏移銀河を直接観測。IllustrisTNG・EAGLE等の宇宙流体シミュレーションが銀河形成の物理を再現。超大質量BHと銀河の共進化が注目課題。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Cosmology",
        "era_start": 1975,
        "culture_region": "North_America",
        "source_url": "https://www.illustris-project.org/",
        "data_completeness": 88,
    },
    {
        "name_ja": "恒星の核融合と元素合成",
        "name_en": "Stellar Nucleosynthesis",
        "definition": "恒星内部の核融合反応によって水素・ヘリウムから重元素が生成される過程。主系列・赤色巨星・超新星爆発・中性子星合体（rプロセス）が各元素生成の場。",
        "impact_summary": "Burbidge・Fowler・Hoyle(1957, B²FH論文)が恒星核合成の体系を確立。Chandrasekhar(1983 Nobel)・Fowler(1983 Nobel)が理論発展。重元素（金・ウラン）は中性子星合体で生成される（GW170817で実証）。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Nuclear Astrophysics",
        "era_start": 1957,
        "culture_region": "Europe_Western",
        "source_url": "https://www.astro.yale.edu/astro130/lecturenotes/lectures/nucleosynthesis.html",
        "mathematical_formulation": r"{}^1H + {}^1H \rightarrow {}^2H + e^+ + \nu_e, \quad Q = 1.44\,\text{MeV}",
        "data_completeness": 90,
    },
    {
        "name_ja": "ハッブル定数の緊張（H₀テンション）",
        "name_en": "Hubble Tension",
        "definition": "宇宙マイクロ波背景放射（CMB）から導出されるH₀（67.4 km/s/Mpc）と局所宇宙のセファイド変光星・Ia型超新星から得られるH₀（73.0 km/s/Mpc）の5σ不一致。",
        "impact_summary": "標準宇宙論（ΛCDM）の重大な亀裂を示す可能性。新しい物理（初期暗黒エネルギー・暗黒輻射・修正重力理論）を要求するか、系統誤差かが論争中。2020年代宇宙論の最重要未解決問題。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "Cosmology",
        "era_start": 2019,
        "culture_region": "North_America",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-astro-091924-093949",
        "mathematical_formulation": r"H_0^{\text{CMB}} = 67.4 \pm 0.5, \quad H_0^{\text{local}} = 73.0 \pm 1.0 \; [\text{km/s/Mpc}]",
        "data_completeness": 87,
    },
    {
        "name_ja": "オリエント・バビロニアの天文学",
        "name_en": "Babylonian Astronomy and Mathematical Prediction",
        "definition": "紀元前7–1世紀のバビロニアで発展した精密な天体観測記録と数理的予測体系。月・惑星の位置をZiqpu表・MUL.APIN文書・惑星表に記録し周期則で月食・惑星位置を予測した。",
        "impact_summary": "現代天文学の計算的伝統の直接的先駆け。バビロニア起源の数学（60進法・角度度数）が現代天文計算に残る。Saros周期（6585日の月食サイクル）の発見は精密天文観測の到達点。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "History of Astronomy",
        "era_start": -700,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.britannica.com/science/Babylonian-astronomy",
        "data_completeness": 85,
    },
]

# Earth Science concepts
EARTH_BATCH = [
    {
        "name_ja": "地震波と地球内部構造",
        "name_en": "Seismic Waves and Earth's Interior",
        "definition": "地震や人工爆発で発生する弾性波（P波・S波・表面波）が地球内部を伝播する速度・振幅変化から地球内部（地殻・マントル・外核・内核）の構造を推定する地球物理手法。",
        "impact_summary": "Andrija Mohorovičić(1909)がモホ面を発見。Lehmann(1936)が固体内核を証明。現在の全球地震トモグラフィーがマントル対流パターン・ホットスポット起源を可視化。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Geophysics",
        "era_start": 1906,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.iris.edu/hq/inclass/animation/seismicwaves",
        "mathematical_formulation": r"v_P = \sqrt{\frac{K+4\mu/3}{\rho}}, \quad v_S = \sqrt{\frac{\mu}{\rho}}",
        "data_completeness": 90,
    },
    {
        "name_ja": "海洋循環と熱塩循環",
        "name_en": "Ocean Circulation and Thermohaline Conveyor",
        "definition": "海水の温度・塩分濃度差が駆動する深層海流（熱塩循環）と風が駆動する表層海流の全球循環系。大西洋子午面循環（AMOC）が北大西洋の気候に決定的な役割を果たす。",
        "impact_summary": "「地球温暖化によるAMOC弱化→ヨーロッパ寒冷化」が気候変動の主要リスク。Stommel(1961)が理論化。アルゴフロート・RAPID監視アレイによる実測が2000年代以降進展。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Oceanography",
        "era_start": 1751,
        "culture_region": "North_America",
        "source_url": "https://www.rapid.ac.uk/",
        "data_completeness": 88,
    },
    {
        "name_ja": "土壌科学と農業地理",
        "name_en": "Soil Science and Pedology",
        "definition": "土壌の生成・分類・物理化学的性質・生態系機能・農業生産性を研究する地球科学分野。土壌層位・有機物・粘土鉱物・微生物群集・CEC（陽イオン交換容量）が主要概念。",
        "impact_summary": "世界の食料生産の95%が土壌に依存（FAO）。土壌有機炭素は大気CO₂の3倍の炭素を貯留。土壌劣化（侵食・塩害・砂漠化）が世界農地の33%に影響（IPBES 2018）。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Earth System Science",
        "era_start": 1883,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.fao.org/soils-portal/en/",
        "data_completeness": 87,
    },
    {
        "name_ja": "氷床・氷河の動態",
        "name_en": "Ice Sheet and Glacier Dynamics",
        "definition": "グリーンランド・南極大陸の氷床および山岳氷河の流動・融解・崩壊・質量収支の動態。海面上昇・淡水収支・アルベド変化への影響が気候研究の中核テーマ。",
        "impact_summary": "GRACE衛星で計測したグリーンランド氷床の年間損失は約2,800億トン（2002–2019平均）。南極西部氷床の不安定性（海洋性氷床不安定性）が21世紀末に6m以上の海面上昇を引き起こす可能性がある。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Glaciology",
        "era_start": 1840,
        "culture_region": "Europe_Western",
        "source_url": "https://nsidc.org/cryosphere/glaciers",
        "data_completeness": 88,
    },
    {
        "name_ja": "成層圏オゾン層と大気化学",
        "name_en": "Stratospheric Ozone and Atmospheric Chemistry",
        "definition": "高度15–35 kmの成層圏に存在するオゾン層が太陽紫外線（UV-B）を吸収する機能と、CFC・ハロンによるオゾン破壊カタリシス（ClOx・BrOx反応サイクル）。",
        "impact_summary": "Molina・Rowland・Crutzen(1995 Nobel)がオゾン破壊メカニズムを解明。モントリオール議定書（1987）がCFCを廃止し、南極オゾンホールは2075年頃に回復と予測。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Atmospheric Science",
        "era_start": 1974,
        "culture_region": "North_America",
        "source_url": "https://www.noaa.gov/education/resource-collections/climate/ozone",
        "mathematical_formulation": r"Cl + O_3 \rightarrow ClO + O_2, \quad ClO + O \rightarrow Cl + O_2",
        "data_completeness": 90,
    },
    {
        "name_ja": "地下水学と水循環",
        "name_en": "Hydrogeology and Water Cycle",
        "definition": "地下の帯水層における地下水の賦存・流動・揚水・涵養を研究する地球科学分野。地下水流動方程式（ダルシー則）・水文学的サイクル・地下水と気候変動の関係が主要テーマ。",
        "impact_summary": "世界人口の50%が飲料水・農業用水を地下水に依存。地下水枯渇（インド・米国中部・中東）が農業危機・地盤沈下・沿岸帯水層塩水化を引き起こす。GRACE衛星が地下水変動を監視。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Hydrology",
        "era_start": 1856,
        "culture_region": "Europe_Western",
        "source_url": "https://www.iah.org/",
        "mathematical_formulation": r"\mathbf{q} = -K\nabla h \quad \text{(Darcy's Law)}, \quad \frac{\partial h}{\partial t} = \frac{K}{S_s}\nabla^2 h",
        "data_completeness": 87,
    },
    {
        "name_ja": "堆積岩と堆積環境",
        "name_en": "Sedimentary Rocks and Depositional Environments",
        "definition": "砕屑性・化学的・生物的起源の堆積物が圧密・固結して形成される岩石とその形成環境。層序学・堆積相解析・シーケンス層序学が主要手法。",
        "impact_summary": "石油・天然ガスの80%以上が堆積盆地に賦存（炭化水素の探鉱に直結）。化石記録・古気候復元・地下水帯水層・石灰岩の炭素隔離評価に必須。地球史46億年の記録庫。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Sedimentology",
        "era_start": 1760,
        "culture_region": "Europe_Western",
        "source_url": "https://www.sepm.org/",
        "data_completeness": 87,
    },
    {
        "name_ja": "火山物質流動と火砕流",
        "name_en": "Volcanic Mass Flows and Pyroclastic Density Currents",
        "definition": "火山爆発で生じる溶岩流・火砕流（高温ガス・火山灰・岩塊の高速流）・火山泥流（ラハール）・火山性津波の流体力学と堆積物を研究する火山学分野。",
        "impact_summary": "1980年セント・ヘレンズ噴火・1991年ピナトゥボ（成層圏エアロゾル0.5℃寒冷化）・2022年トンガ噴火の記録が防災科学に活用。AI・ドローン監視が火山リアルタイム観測を変革中。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Volcanology",
        "era_start": 1815,
        "culture_region": "Europe_Western",
        "source_url": "https://www.iavcei.org/",
        "data_completeness": 86,
    },
    {
        "name_ja": "インド洋ダイポールと南アジア気候",
        "name_en": "Indian Ocean Dipole and South Asian Climate",
        "definition": "インド洋の熱帯域で西部の温暖・東部の冷却（正のIOD）または逆（負のIOD）が生じる気候変動モード。インドのモンスーン・オーストラリアの干ばつ・アフリカの洪水と連動する。",
        "impact_summary": "Saji et al.(1999, Nature 401)が発見。正のIODはインド夏季モンスーン強化・東アフリカ洪水と相関。気候変動下でIOD強度・頻度が増大しアジア・アフリカの農業に深刻影響。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Climate Science",
        "era_start": 1999,
        "culture_region": "South_Asia",
        "source_url": "https://www.nature.com/articles/23544",
        "data_completeness": 87,
    },
    {
        "name_ja": "アフリカの大地溝帯と地殻変動",
        "name_en": "African Rift Valley and Tectonic Dynamics",
        "definition": "東アフリカ大地溝帯（Great Rift Valley）はエチオピア〜モザンビークを縦断する地溝帯。プレート分裂が進行中で将来的にアフリカ東部が分裂・新たな海洋が形成される可能性がある。",
        "impact_summary": "人類の揺籃地（アウストラロピテクス・ホモ・エレクトスの化石産地）としての考古学的価値。地熱エネルギー資源（エチオピアの地熱発電）・地震リスク・火山活動の継続的監視が必要。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Tectonics",
        "era_start": 1890,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.britannica.com/place/Great-Rift-Valley",
        "data_completeness": 85,
    },
    {
        "name_ja": "古生物学と化石の解析",
        "name_en": "Paleontology and Fossil Analysis",
        "definition": "過去の生物が残した化石（骨・歯・殻・花粉・足跡・生痕）を研究し生命の進化史・古環境・大量絶滅イベントを復元する地球科学分野。",
        "impact_summary": "カンブリア爆発・ペルム紀末大量絶滅・恐竜絶滅（K-Pg境界）・エディアカラ生物群の解析が地球史の理解に革命をもたらした。ラガーシュテッテン（澄江・バージェス頁岩・ホルツマーデン）が主要産地。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Earth History",
        "era_start": 1820,
        "culture_region": "Europe_Western",
        "source_url": "https://www.paleo.amnh.org/",
        "data_completeness": 88,
    },
    {
        "name_ja": "地球磁場とその反転",
        "name_en": "Geomagnetic Field and Polarity Reversals",
        "definition": "外核液体鉄の対流で生成される地球磁場（双極子成分主体）の強度・方向の時間変化と過去数億年の磁極逆転（地磁気逆転）の記録および反転機構の研究。",
        "impact_summary": "海底溶岩の磁気縞模様が大陸移動説の決定的証拠（Vine-Matthews, 1963）。古地磁気年代測定・古気候復元・コア-マントル境界ダイナミクスの解明に活用。宇宙線シールドとしての機能も重要。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "Geophysics",
        "era_start": 1600,
        "culture_region": "Europe_Western",
        "source_url": "https://www.ngdc.noaa.gov/geomag/",
        "data_completeness": 88,
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
    n1 = insert_batch(conn, ASTRO_BATCH)
    n2 = insert_batch(conn, EARTH_BATCH)
    total = n1 + n2
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    grand = cursor.fetchone()[0]
    conn.close()
    print(f"Batch14 astro+earth: {total} inserted (astro={n1}, earth={n2}). Total: {grand}")
