"""
DUA Wave A2 Batch 22: Earth Science 3 + Astronomy 3
Target: 地球科学 +25, 宇宙物理 +20 = ~45 insertions
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

EARTH_BATCH = [
    {
        "name_ja": "地球内部構造・地震波トモグラフィー",
        "name_en": "Earth Interior and Seismic Tomography",
        "name_original": "Seismic Tomography",
        "definition": "地震波（P波・S波・表面波）の走時・振幅・位相を地球全域の観測データから三次元的に逆問題解析し、地球内部（地殻・マントル・コア）の温度・組成・構造を映像化する技術。Dziewonski・Anderson（PREM地球モデル 1981）・Van der Hilst・Montelli によりスーパープルームの直接証拠が得られた。",
        "impact_summary": "マントル対流・プレートテクトニクスの駆動力・ホットスポット（ハワイ・アイスランド）の根源・地球コアの成長史を解明。IRIS・F-net（日本）の高密度地震観測網が解像度を向上させ続けている。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球物理学",
        "era_start": 1977,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.iris.edu/hq/programs/education_and_outreach/seismic_tomography",
        "mathematical_formulation": r"d_i = \int_{\text{ray}} s(\mathbf{r})\,dl + \varepsilon_i,\quad \mathbf{d} = \mathbf{A}\mathbf{m} + \boldsymbol{\varepsilon}",
        "data_completeness": 88
    },
    {
        "name_ja": "地球温暖化・温室効果の物理",
        "name_en": "Global Warming and Greenhouse Effect Physics",
        "name_original": "Greenhouse Effect",
        "definition": "CO2・CH4・N2O・H2O等の温室効果ガスが赤外放射を吸収して再放射し、地球表面を温暖化するメカニズム。Arrhenius（1896）が定量化し、Keeling曲線（1958年以降のCO2連続測定）が人為的増加を実証。気候感度・フィードバック（雲・氷アルベド・水蒸気）・海洋熱吸収が気候モデルの核心。",
        "impact_summary": "Manabe（真鍋淑郎, East_Asia）とHasselmannが2021年ノーベル物理学賞受賞（気候変動の物理的モデリング）。IPCC AR6（2021–2022年）は工業化前比+1.1°C確認・2°C以内に抑える政策的含意を示した。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1896,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/2021/press-release/",
        "mathematical_formulation": r"\Delta F = 5.35\ln(C/C_0) \text{ [W m}^{-2}],\quad \Delta T = \lambda \Delta F",
        "data_completeness": 92
    },
    {
        "name_ja": "海洋化学・炭素循環",
        "name_en": "Ocean Chemistry and Carbon Cycle",
        "name_original": "Ocean Carbon Chemistry",
        "definition": "海洋は大気CO2の約25-30%を吸収する炭素の巨大リザーバー。CO2の海水溶解・炭酸系（H2CO3/HCO3-/CO3²-）の平衡・海洋酸性化（pH低下）・溶存無機炭素（DIC）・生物ポンプ（植物プランクトン光合成→有機炭素沈降）・熱塩循環による炭素輸送が主要過程。",
        "impact_summary": "海洋酸性化による珊瑚礁・貝類・翼足類の骨格溶解が生態系危機として認識。ARGO浮標・Biogeochemical Argo・Ocean Acidification International Coordination Centerが全球監視を実施。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "海洋科学",
        "era_start": 1950,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification",
        "mathematical_formulation": r"CO_2 + H_2O \rightleftharpoons H_2CO_3 \rightleftharpoons H^+ + HCO_3^- \rightleftharpoons 2H^+ + CO_3^{2-}",
        "data_completeness": 88
    },
    {
        "name_ja": "地球磁場・地磁気逆転",
        "name_en": "Geomagnetic Field and Polarity Reversals",
        "name_original": "Geomagnetic Reversals",
        "definition": "地球内核・外核の液体鉄の対流により駆動されるダイナモ理論が地磁気を生成する。地磁気の方向が不規則に反転（百万年に数回の頻度）し、岩石に磁気縞として記録される。海底拡大説（Vine-Matthews-Morley 1963）・古地磁気学・磁気年代尺（GPTS）・地磁気双極子モーメントの変動が研究対象。",
        "impact_summary": "古地磁気縞模様はプレートテクトニクス理論の決定的証拠となった。次の地磁気逆転予兆（南大西洋アノマリー・極移動速度増大）は人工衛星・電力グリッドへのリスクとして監視されている。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球物理学",
        "era_start": 1600,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.usgs.gov/programs/geomagnetism",
        "mathematical_formulation": r"\frac{\partial \mathbf{B}}{\partial t} = \nabla\times(\mathbf{u}\times\mathbf{B}) + \eta\nabla^2\mathbf{B}",
        "data_completeness": 87
    },
    {
        "name_ja": "土壌学・土壌炭素と農業生産性",
        "name_en": "Soil Science: Carbon Storage and Agricultural Productivity",
        "name_original": "Soil Carbon",
        "definition": "土壌は陸域最大の炭素貯蔵庫（約2,000 GtC、大気の約2.5倍）で、土壌有機炭素（SOC）の蓄積・分解・安定化機構が気候変動・食糧安全保障に直結する。土壌微生物群集・腐植形成・岩石風化（シリケート炭素吸収）・土壌侵食・Dokuchaev（ロシア土壌学の父）の土壌分類が基礎。",
        "impact_summary": "「4 per 1000」イニシアティブ（フランス提唱、COP21）は世界の土壌SOCを年0.4%増やすだけで大気CO2増加分を相殺できると主張。インドの伝統的農法（ゼロ耕起・バイオチャー）が土壌炭素固定に有効との研究が進む。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "土壌科学",
        "era_start": 1883,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.fao.org/soils-portal/soil-management/soil-carbon-sequestration/en/",
        "mathematical_formulation": r"\frac{dC_{soil}}{dt} = NPP_{below} - k\cdot C_{soil} \cdot f(T,W)",
        "data_completeness": 85
    },
    {
        "name_ja": "洪水・土砂災害・斜面崩壊の地形力学",
        "name_en": "Flood Hazard and Landslide Geomorphology",
        "name_original": "Landslide Dynamics",
        "definition": "降雨・地震・火山噴火により引き起こされる斜面崩壊・土砂流・岩石なだれ・鉄砲水の発生機構・移動・堆積を解析する地形力学分野。Bishop安定解析・Mohr-Coulomb破壊基準・Bingham流体モデル・数値シミュレーション（DAN3D, RAMMS）が主要ツール。",
        "impact_summary": "インドネシア・日本・中国・インドなど急峻な地形を持つアジア諸国で毎年多数の犠牲者が出る。地形・地質・雨量の組み合わせリスクマップと早期警戒システム（ALOS衛星・SAR干渉測位）が防災基盤。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地形学",
        "era_start": 1920,
        "culture_region": "North_America_Europe",
        "source_url": "https://nhess.copernicus.org/",
        "mathematical_formulation": r"FS = \frac{c' + (\sigma-u)\tan\phi'}{c'+\sigma\tan\phi'}, \quad FS \ge 1 \text{ (stable)}",
        "data_completeness": 83
    },
    {
        "name_ja": "鉱床学・レアアース鉱床",
        "name_en": "Economic Geology and Rare Earth Deposits",
        "name_original": "Rare Earth Element Deposits",
        "definition": "希土類元素（REE: La〜Lu + Y + Sc）は炭酸岩・イオン吸着型粘土鉱床・アルカリ岩に濃集する。中国（East_Asia）が世界産出量の60%超を占め（バヤンオボ・モンゴル産炭酸岩鉱床）、EVモーター・風力タービン磁石・LED蛍光体の原材料として戦略的重要性を持つ。マグマ分化・熱水変質・堆積後成岩が主要濃集機構。",
        "impact_summary": "グリーンエネルギー転換に不可欠なREEの供給制約（中国依存）が世界的課題。深海底のレアアース泥床（東京大学加藤泰浩、East_Asia）が次世代鉱床として注目される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "鉱床地質学",
        "era_start": 1950,
        "culture_region": "East_Asia",
        "source_url": "https://www.usgs.gov/centers/national-minerals-information-center/rare-earths",
        "data_completeness": 85
    },
    {
        "name_ja": "古気候学・氷床コアと気候プロキシ",
        "name_en": "Paleoclimatology and Ice Core Records",
        "name_original": "Ice Core Paleoclimatology",
        "definition": "南極・グリーンランドの氷床コアに閉じ込められた古代空気バブルの分析により、過去80万年の大気CO2濃度・気温（d18O・dD同位体）・火山灰・エアロゾルが復元される。Vostok・EPICA Dome C・WAIS Divideコアが代表的記録。ミランコビッチサイクル（軌道強制）との対応が解明された。",
        "impact_summary": "EPICA Dome C（南極、欧州）の80万年記録は過去の間氷期が現在より温暖でなかったことを示し、現在の温暖化が人為起源であることの古気候的証拠。IPCC AR6の結論の主要根拠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1969,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.epica.awi.de/",
        "mathematical_formulation": r"\delta^{18}O = \left(\frac{R_{sample}}{R_{standard}} - 1\right)\times 1000 \text{ (‰)},\quad \Delta T \approx 1.5\times\delta D",
        "data_completeness": 88
    },
    {
        "name_ja": "大気化学・オゾン・エアロゾル",
        "name_en": "Atmospheric Chemistry: Ozone and Aerosols",
        "name_original": "Atmospheric Chemistry",
        "definition": "成層圏オゾン（Dobson単位）・オゾンホール（Molina, Rowland, Crutzen 1995年ノーベル化学賞）・対流圏光化学スモッグ・エアロゾル（硫酸塩・有機物・黒色炭素）の形成・輸送・除去反応を扱う。OH ラジカルが大気の「洗浄剤」として機能し、CH4・CO・VOCを分解する。",
        "impact_summary": "モントリオール議定書（1987年）によるCFC規制成功でオゾン層は回復軌道に。一方、大気エアロゾルは放射強制力の最大不確実性要因として気候モデルの精度向上のカギ。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "大気科学",
        "era_start": 1930,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/1995/press-release/",
        "mathematical_formulation": r"O_3 + h\nu \to O(^1D) + O_2,\quad \text{Cl} + O_3 \to ClO + O_2 \text{ (catalytic cycle)}",
        "data_completeness": 88
    },
    {
        "name_ja": "地下水・水文地質学",
        "name_en": "Hydrogeology and Groundwater",
        "name_original": "Hydrogeology",
        "definition": "地下水の分布・流動・水質変化・揚水と涵養の均衡を扱う水文地質学。Darcy法則（Q = KAi）・透水係数・帯水層（被圧・不圧）・地下水位低下・地盤沈下・硝酸塩汚染・ヒ素汚染（バングラデシュ、South_Asia）が主要問題。気候変動による降水パターン変化が帯水層涵養を脅かす。",
        "impact_summary": "世界人口の約40%が地下水を主要飲料水源とする。バングラデシュ・インド（South_Asia）の地下水ヒ素汚染は数千万人規模の健康問題。気候変動下のサウジアラビア・インド半島・米国オガララ帯水層の枯渇が食糧安全保障リスク。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "水文学",
        "era_start": 1856,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.usgs.gov/mission-areas/water-resources/science/groundwater",
        "mathematical_formulation": r"Q = KA\frac{dh}{dl} \text{ (Darcy)},\quad S\frac{\partial h}{\partial t} = \nabla(K\nabla h) + W",
        "data_completeness": 85
    },
    {
        "name_ja": "地震断層・地震サイクルと地震予知",
        "name_en": "Fault Mechanics and Earthquake Cycle",
        "name_original": "Earthquake Cycle",
        "definition": "地震断層の固着・スリップ・余効変動のサイクルをプレート境界の弾性変形と非弾性すべりから記述する。速度-状態依存摩擦則（Rate-and-State friction）・断層帯流体・すべり欠如・固着域マッピング（geodetic inversions・SAR干渉法）・前震・本震・余震シーケンスが研究対象。",
        "impact_summary": "東北地方太平洋沖地震（2011年、Mw 9.0）は固着域の大きさと前震の見落としを再認識させた。GNSS・InSAR・海底地殻変動観測網（S-net, DONET）が南海トラフ地震の準リアルタイム監視に使用中。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地震学",
        "era_start": 1965,
        "culture_region": "East_Asia",
        "source_url": "https://www.bosai.go.jp/",
        "mathematical_formulation": r"\mu = \mu_0 + a\ln\frac{V}{V_0} + b\ln\frac{V_0\theta}{D_c} \text{ (R-S friction)}",
        "data_completeness": 88
    },
    {
        "name_ja": "火山噴火・火山灰と気候影響",
        "name_en": "Volcanic Eruptions and Climatic Impact",
        "name_original": "Volcanic Climate Forcing",
        "definition": "大規模噴火（VEI ≥5）が成層圏に注入した硫酸塩エアロゾル（H2SO4液滴）は太陽放射を散乱・吸収して数年間の気候冷却（火山冬）を引き起こす。Tambora1815（夏なし年1816）・Pinatubo1991（約-0.5°C/2年）・インドネシア島弧火山・アイスランドの間欠泉・スーパー噴火（Toba）が研究事例。",
        "impact_summary": "火山灰の農業破壊・航空路閉鎖（Eyjafjallajökull 2010年）・気候工学（成層圏エアロゾル注入SAIへの安全性知見）。日本（East_Asia）の火山観測体制（気象庁）が高度で世界の防災モデル。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "火山学",
        "era_start": 1815,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.volcanodiscovery.com/volcanology.html",
        "mathematical_formulation": r"\text{RF} = -\frac{S_0}{4}(1-\alpha_p)\left(\frac{\delta\tau_{aer}}{\delta SO_2}\right)\Delta m_{SO_2}",
        "data_completeness": 85
    },
    {
        "name_ja": "アフリカ地質・クラトンと太古代地殻",
        "name_en": "African Geology: Cratons and Archean Crust",
        "name_original": "African Cratons",
        "definition": "アフリカは世界最古の大陸地殻（クラトン）の大部分を占め、カーパンヴァール・ジンバブウェ・タンザニア・サハラクラトンが38-36億年前の太古代地殻を保存する。西アフリカ・カラハリ・コンゴクラトンが現在の大陸安定域を形成。GreatRift Valley（東アフリカ地溝帯）は現在進行中の大陸分裂を示す。",
        "impact_summary": "アフリカの鉱床（カッパーベルト・金鉱・白金族元素）の多くがクラトン縁辺の変成帯に集中。太古代の生命痕跡（西オーストラリア・南アフリカのストロマトライト）が初期生命進化の研究場。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地質学",
        "era_start": -3800,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.geological-digressions.com/african-geology-overview/",
        "data_completeness": 80
    },
    {
        "name_ja": "気象学・台風・サイクロン力学",
        "name_en": "Meteorology: Tropical Cyclone Dynamics",
        "name_original": "Tropical Cyclones",
        "definition": "熱帯低気圧（台風・ハリケーン・サイクロン）はCoriolis力と海面蒸発熱（湿潤断熱プロセス）によって組織化される巨大熱機関。CAPE（対流有効位置エネルギー）・最大強度理論（Emanuel 1987）・眼・眼壁・スパイラルバンド・急発達（RI: Rapid Intensification）が主要概念。",
        "impact_summary": "スーパー台風・カテゴリー5ハリケーン（Katrina, Harvey, Hagibis）による洪水・高潮被害は年間数千億ドル規模。全球温暖化による最大強度台風の増加（Knutson et al.）が予測されており、アジア（East_Asia）・南アジア（インド洋サイクロン）の防災が急務。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気象学",
        "era_start": 1950,
        "culture_region": "East_Asia",
        "source_url": "https://www.jma.go.jp/jma/en/News/typhoon.html",
        "mathematical_formulation": r"V_{max} = \sqrt{\frac{C_k}{C_d}\frac{T_s-T_o}{T_o}k_0^*} \text{ (Emanuel MPI)}",
        "data_completeness": 85
    },
    {
        "name_ja": "インド洋・モンスーン気候システム",
        "name_en": "Indian Ocean and Monsoon Climate System",
        "name_original": "South Asian Monsoon",
        "definition": "南アジアのモンスーン（季節風）はインド洋の海面水温・チベット高原加熱・ITCZ移動によって制御される大規模気候現象。IOD（インド洋ダイポール）・ENSO遠隔相関・アラビア海アップウェリングが変動要因。中国（東アジア）の梅雨前線・東アジアモンスーンも関連する。",
        "impact_summary": "南アジア12億人以上の農業水資源をモンスーン降水が支える。IODの正相時にオーストラリア干ばつ・東アフリカ洪水が生じ（2019年）、気候変動によるモンスーン変動が多大な社会経済影響を持つ。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1686,
        "culture_region": "South_Asia",
        "source_url": "https://www.imd.gov.in/pages/monsoon_main.php",
        "mathematical_formulation": r"\text{IOD index} = \text{SSTA}(50^\circ E\text{-}70^\circ E, 10^\circ S\text{-}10^\circ N) - \text{SSTA}(90^\circ E\text{-}110^\circ E, 10^\circ S\text{-}0^\circ)",
        "data_completeness": 85
    },
]

ASTRO_BATCH = [
    {
        "name_ja": "系外惑星の直接撮像",
        "name_en": "Direct Imaging of Exoplanets",
        "name_original": "Exoplanet Direct Imaging",
        "definition": "恒星の光を冠カメラ（コロナグラフ）で遮蔽し系外惑星を直接撮像する技術。Gemini惑星搭載器（GPI）・SPHERE（VLT）・ジェームズ・ウェッブ宇宙望遠鏡（JWST）の中間赤外線観測が代表的手法。HR 8799系（4惑星直接撮像）・Beta Pictoris b（詳細な軌道測定）・AF Leporis bが成果例。",
        "impact_summary": "JWST（2022年運用開始）は系外惑星大気（CO2・水・メタン）の透過分光と直接撮像を可能にし、生命の化学的痕跡探索に直結。将来の宇宙望遠鏡（HabEx・LUVOIR）設計の指針となる。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "観測天文学",
        "era_start": 2008,
        "culture_region": "North_America_Europe",
        "source_url": "https://webbtelescope.org/contents/news-releases/2022/news-2022-046",
        "data_completeness": 90
    },
    {
        "name_ja": "活動銀河核・ブラックホール質量測定",
        "name_en": "Active Galactic Nuclei and Black Hole Mass Measurement",
        "name_original": "Active Galactic Nuclei (AGN)",
        "definition": "活動銀河核（AGN）は銀河中心の超大質量ブラックホール（SMBH）への降着円盤から放射する。Seyfert銀河・クエーサー（QSO）・BL Lac天体・電波銀河・マイクロクエーサーが分類。Mσ関係（バルジ速度分散とSMBH質量の相関）・Eddington光度・相対論的ジェットが主要概念。",
        "impact_summary": "Event Horizon Telescope（EHT）によるM87ブラックホール（2019年）・銀河中心SgrA*（2022年、Genzel, Ghez 2020年ノーベル物理学賞）の直接撮像が金字塔。ブラックホール-銀河共進化（AGNフィードバック）が銀河形成の鍵機構。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "高エネルギー天文学",
        "era_start": 1943,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/2020/press-release/",
        "mathematical_formulation": r"L_{Edd} = \frac{4\pi G M_{BH} m_p c}{\sigma_T},\quad M_{BH} \sim 10^8 M_\odot\left(\frac{\sigma}{200\text{ km/s}}\right)^5",
        "data_completeness": 92
    },
    {
        "name_ja": "恒星進化・赤色超巨星と超新星",
        "name_en": "Stellar Evolution: Red Supergiants and Supernovae",
        "name_original": "Stellar Evolution",
        "definition": "大質量星（>8 M☉）の主系列→赤色超巨星→コア崩壊型超新星（SN Ib/c, SN II）の進化を扱う。鉄コアが電子縮退圧を超えた崩壊（~0.25秒）でニュートリノが放出され、衝撃波が外層を吹き飛ばす。r過程元素合成（中性子星合体と超新星の寄与）・超新星の光度曲線・残骸（中性子星・ブラックホール）が研究対象。",
        "impact_summary": "SN 1987A（大マゼラン雲）は初のニュートリノ同時検出（小柴昌俊 2002年ノーベル物理学賞、East_Asia）超新星として理論検証。超新星サーベイ（Vera Rubin Observatory）がType Ia標準光源で宇宙論的距離測定を担う。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "恒星天体物理",
        "era_start": 1939,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/2002/press-release/",
        "mathematical_formulation": r"L = 4\pi R^2 \sigma T_{eff}^4,\quad \frac{dM}{dt} = -\dot{M}_{wind} \text{ (mass loss)}",
        "data_completeness": 90
    },
    {
        "name_ja": "銀河の形成・合体・フィードバック",
        "name_en": "Galaxy Formation, Mergers and AGN Feedback",
        "name_original": "Galaxy Formation",
        "definition": "宇宙論的シミュレーション（IllustrisTNG, EAGLE, Simba）が暗黒物質ハロー形成・バリオン物理・星形成・超新星フィードバック・AGNジェット（電波モードフィードバック）を組み合わせて銀河形成の自己矛盾のない描像を構築する。銀河の形態（楕円/渦巻）・ダウンサイジング・クエンチング・環境効果（ラム圧ストリッピング）が主要テーマ。",
        "impact_summary": "JWSTが宇宙最初の10億年内の銀河（高赤方偏移源）を大量発見し、Λ-CDM標準模型の予測と比較して議論が続く。銀河中心ブラックホールと宿主銀河の共進化がAGNフィードバックを通じて説明される。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論・観測天文学",
        "era_start": 1978,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.tng-project.org/",
        "data_completeness": 88
    },
    {
        "name_ja": "宇宙マイクロ波背景放射・初期宇宙観測",
        "name_en": "Cosmic Microwave Background and Early Universe",
        "name_original": "CMB",
        "definition": "ビッグバン後38万年の宇宙再結合期に放出された光（CMB）は現在2.725 Kの黒体放射として全天に広がる。COBE（Smoot, Mather 2006年ノーベル物理学賞）・WMAP・Planck衛星が温度異方性（ΔT/T〜10^-5）を精密測定し、宇宙論パラメータ（H0, Ωb, Ωm, ΩΛ, ns）を確定した。",
        "impact_summary": "Planck2018のデータからΛ-CDM標準宇宙論モデルが確立。宇宙論パラメータ（H0=67.4 km/s/Mpc, Ωm=0.315）がBAO・超新星測定と比較されH0張力が浮上。BICEP/Keck Array・CMB-S4が原始重力波（インフレーション証拠）を探索中。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1965,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.esa.int/Science_Exploration/Space_Science/Planck",
        "mathematical_formulation": r"C_l = \frac{2}{\pi}\int k^2 P(k) |\Delta_l(k)|^2 dk,\quad T_0 = 2.7255\pm0.0006 \text{ K}",
        "data_completeness": 92
    },
    {
        "name_ja": "マヤ・インカの天文知識",
        "name_en": "Maya and Inca Astronomical Knowledge",
        "name_original": "Maya Astronomy",
        "definition": "マヤ文明は金星・太陽・月の精密な観測に基づく暦体系（ハアブ暦・ツォルキン暦・長期暦）と天文表（ドレスデン絵文書の金星表・月食表）を構築した。インカは星の暗黒星座（夕暗の帯の形で星座を設定）と天空の川（銀河）を農業・宗教に結びつけ、太陽の頂天通過を石柱（ゴルセカ）で計測した。",
        "impact_summary": "マヤの金星周期（584日）はグレゴリオ暦より精確との説がある。南米先住民の暗黒星座（黒い雲）はウランバラ（ラマ・蛙・ヘビ）として記述され、天文学的宇宙観の多様性を示す。チチェン・イッツァのエルカスティジョは春分・秋分の蛇の影で太陽年を表示する精密建造物。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "先住民科学史",
        "era_start": 200,
        "culture_region": "Americas_Indigenous",
        "source_url": "https://www.archaeology.org/news/8200-200103-maya-venus-table",
        "data_completeness": 78
    },
    {
        "name_ja": "中世イスラームの天文学・アルマゲスト批判",
        "name_en": "Islamic Astronomy and Critique of Almagest",
        "name_original": "التراث الفلكي الإسلامي",
        "definition": "イスラーム黄金時代（9–15世紀）の天文学者たちはプトレマイオス『アルマゲスト』を翻訳・改良し、コペルニクス・ティコ・ブラーエに先行する批判的改革を行った。Ibn al-Haytham（「惑星運動の疑問」）・Nasir al-Din al-Tusi（トゥーシのカップル、均衡機構への代替）・Ibn al-Shatir（地心・非周転円軌道）・al-Biruni（地球自転仮説）が代表的人物。",
        "impact_summary": "コペルニクスの数学的構造がIbn al-Shatirのモデルと等価であるとの研究が、イスラーム天文学のヨーロッパ科学革命への貢献を示す（Roberts 1957, Saliba）。ギリシャ知識の保存・改良・伝達の中継点としてのイスラーム科学の役割が評価されている。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "イスラーム科学",
        "era_start": 830,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.islamicmoon.com/",
        "data_completeness": 82
    },
    {
        "name_ja": "連星系・食連星・コンパクト天体",
        "name_en": "Binary Stars, Eclipsing Binaries and Compact Objects",
        "name_original": "Binary Stars",
        "definition": "2つの恒星が相互の重力で公転する連星系は恒星質量・半径・光度の直接測定手段。食連星（光度曲線）・分光連星（ドップラー速度曲線）・視覚連星・X線連星（コンパクト天体への降着）・中性子星合体（GW）が主要種別。Chandrasekhar限界（1.44 M☉、1983年ノーベル物理学賞）は白色矮星の最大質量。",
        "impact_summary": "連星系はType Ia超新星の起源（単一縮退・二重縮退機構）・短周期GRBの前駆体・X線連星（ブラックホール・中性子星）の研究場。Hulse-Taylor連星パルサー（1993年ノーベル物理学賞）が一般相対論の間接的重力波証拠を提供。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "恒星天体物理",
        "era_start": 1783,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/1993/press-release/",
        "mathematical_formulation": r"P^2 = \frac{4\pi^2 a^3}{G(M_1+M_2)},\quad M_{Ch} = \frac{5.87}{\mu_e^2}M_\odot \approx 1.44M_\odot",
        "data_completeness": 88
    },
    {
        "name_ja": "太陽物理学・磁気嵐と宇宙天気",
        "name_en": "Solar Physics and Space Weather",
        "name_original": "Solar Physics",
        "definition": "太陽は可視光（光球）・彩層・コロナ・フレア・コロナ質量放出（CME）・太陽風を放出する恒星プラズマ。太陽磁気サイクル（11年・22年）・黒点・活動領域・磁気リコネクション（フレア加熱）・ハイド-クレシェフォードモデル・Parker太陽風モデルが基礎理論。",
        "impact_summary": "磁気嵐（地磁気インデックスKp）が人工衛星・GPS・電力グリッド・航空通信に障害を与えた事例（1989年ケベック停電、2003年ハロウィン嵐）。Parker Solar Probe（NASA）・Solar Orbiter（ESA）が太陽コロナ加熱機構を解明しつつある。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "太陽天体物理",
        "era_start": 1859,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nasa.gov/missions/parker-solar-probe/",
        "mathematical_formulation": r"\frac{1}{r^2}\frac{d}{dr}(r^2 v\rho) = 0,\quad \rho v\frac{dv}{dr} = -\frac{dp}{dr} - \frac{GM_\odot\rho}{r^2} \text{ (Parker wind)}",
        "data_completeness": 88
    },
    {
        "name_ja": "バリオン音響振動・大規模構造",
        "name_en": "Baryon Acoustic Oscillations and Large-Scale Structure",
        "name_original": "Baryon Acoustic Oscillations",
        "definition": "初期宇宙のバリオン-光子流体中の音波が再結合期に凍結した痕跡（BAO）が銀河の空間分布に約150 Mpc（500 Mly）のスケールで観測される。SDSS・2dF銀河サーベイ・BOSS（Eisenstein et al. 2005）が検出。宇宙膨張の「標準定規」としてH(z)とDA(z)を測定し、ダークエネルギー方程式のパラメータを制約する。",
        "impact_summary": "DESI（Dark Energy Spectroscopic Instrument）が5年間で3,600万銀河のBAO測定を進め、ダークエネルギーの時間変化（w0wa CDM）の可能性を2024–2025年に示唆した結果が注目されている。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1970,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.desi.lbl.gov/",
        "mathematical_formulation": r"r_s = \int_0^{z_*} \frac{c_s\,dz}{H(z)},\quad c_s = \frac{c}{\sqrt{3(1+R)}},\; R = \frac{3\rho_b}{4\rho_\gamma}",
        "data_completeness": 90
    },
    {
        "name_ja": "恒星の内部核合成・元素起源",
        "name_en": "Stellar Nucleosynthesis: Origin of Elements",
        "name_original": "Nucleosynthesis",
        "definition": "Burbidge-Burbidge-Fowler-Hoyle（B2FH 1957）論文が恒星核融合による元素合成の包括的理論を提示。主系列（pp連鎖・CNOサイクル）・赤色巨星（Heシェル燃焼・s過程）・超新星（r過程・p過程・explosive burning）・コンパクト天体合体（r過程）が元素合成の場。",
        "impact_summary": "Fowler（1983年ノーベル物理学賞）が実験核物理データでB2FH理論を補強。GW170817による中性子星合体のキロノバがr過程元素（金・プラチナ等）の主要生成場であることを実証した。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "核天体物理",
        "era_start": 1957,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/1983/press-release/",
        "mathematical_formulation": r"\frac{dY_i}{dt} = \sum_j \lambda_j Y_j + \sum_{j,k} \rho N_A \langle\sigma v\rangle_{jk} Y_j Y_k",
        "data_completeness": 90
    },
    {
        "name_ja": "インドの古典天文学・アーリヤバタ",
        "name_en": "Indian Classical Astronomy: Aryabhata",
        "name_original": "आर्यभट",
        "definition": "アーリヤバタ（476–550 CE）はグプタ朝期インドの数学者・天文学者で、『アーリヤバティーヤ』に地球の自転・惑星運動・月食・太陽食の幾何学的説明・三角関数の概念（半弦jya）・円周率π≈3.1416を記述した。Brahmagupta（628 CE）がさらにゼロの演算・不定方程式を完成させた。",
        "impact_summary": "インドの三角法・天文計算（エフェメリス）がイスラーム世界（アル-バタニ）を経てヨーロッパへ伝わり、コペルニクス前の天文学の精度向上に寄与。π=62832/20000=3.1416はヨーロッパの数世紀先を行く精度。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "インド天文学",
        "era_start": 499,
        "culture_region": "South_Asia",
        "source_url": "https://www.britannica.com/biography/Aryabhata-I",
        "data_completeness": 83
    },
    {
        "name_ja": "宇宙論的シミュレーション・N体計算",
        "name_en": "Cosmological N-body Simulations",
        "name_original": "N-body Cosmological Simulations",
        "definition": "ダークマターハロー・バリオン物理・宇宙論的膨張を数百億〜数兆個の粒子シミュレーションで追跡する。Millenium（Springel, Virgo Consortium 2005）・IllustrisTNG・Bolshoi・Simbaが代表的シミュレーション。TreePM法・AMR（適応的メッシュ精緻化）・GPU高速化が計算技術革新。",
        "impact_summary": "Ω_mとσ8のパラメータ制約・銀河群と銀河団の大規模構造比較・弱重力レンズとの整合性検証。JWSTによる初期銀河の豊かさがΛ-CDM予測と合わない可能性を示唆し、シミュレーションと観測の照合が急務。",
        "subfield": "宇宙物理・天文学",
        "school_of_thought": "宇宙論",
        "era_start": 1985,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.tng-project.org/",
        "mathematical_formulation": r"\ddot{\mathbf{r}}_i = -G\sum_{j\ne i}\frac{m_j(\mathbf{r}_i-\mathbf{r}_j)}{(|\mathbf{r}_i-\mathbf{r}_j|^2+\epsilon^2)^{3/2}}",
        "data_completeness": 88
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n1 = insert_batch(conn, EARTH_BATCH)
    n2 = insert_batch(conn, ASTRO_BATCH)
    conn.close()
    conn2 = sqlite3.connect(DB_PATH)
    total = conn2.cursor().execute("SELECT COUNT(*) FROM natural_discovery").fetchone()[0]
    conn2.close()
    print(f"Batch22 earth+astro: {n1+n2} inserted (earth={n1}, astro={n2}). Total: {total}")
