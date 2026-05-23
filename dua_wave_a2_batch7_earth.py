"""
DUA Wave A2 Batch 7 — 地球科学・環境科学 (Earth Science & Environmental Science)
Target: ~60 concepts, current subfield count ~193, target ~393
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
        "name_ja": "地球の層構造",
        "name_en": "Internal Structure of the Earth",
        "definition": "地球は地殻・マントル・外核・内核の同心球状層構造をなす。地震波の速度変化から推定され、モホロビチッチ面（1909年）とグーテンベルク不連続面（1914年）が主要境界をなす。",
        "impact_summary": "固体地球物理学の基盤。地磁気発生メカニズム（外核の液体鉄対流）理解と資源探査に不可欠な知識体系。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "固体地球物理学",
        "era_start": 1909,
        "culture_region": "Europe_Western",
        "source_url": "https://www.usgs.gov/programs/earthquake-hazards/interior-earth",
        "mathematical_formulation": r"v_P = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \quad v_S = \sqrt{\frac{G}{\rho}}",
        "data_completeness": 90
    },
    {
        "name_ja": "マントル対流",
        "name_en": "Mantle Convection",
        "definition": "地球マントルは固体でありながら長期的には粘性流体として熱対流する。ホットスポット・沈み込み帯・中央海嶺の活動を駆動し、プレートテクトニクスのエンジンとなる。",
        "impact_summary": "プレート運動の熱力学的駆動力を説明。地球内部エネルギー散逸・大陸配置変化・深部物質循環の理解に不可欠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "固体地球物理学",
        "era_start": 1935,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/ngeo1078",
        "mathematical_formulation": r"Ra = \frac{\rho g \alpha \Delta T d^3}{\kappa \eta}",
        "data_completeness": 88
    },
    {
        "name_ja": "地震学・地震波伝播",
        "name_en": "Seismology and Seismic Wave Propagation",
        "definition": "地震は断層面のずれによって生じ、P波・S波・表面波を放射する。リヒタースケール（1935年）・モーメントマグニチュードが規模を定量化し、震源メカニズム解が断層活動を特定する。",
        "impact_summary": "地球内部構造の主要探査手段。地震災害軽減・核実験検知・天然資源探査に応用される広範な科学技術基盤。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "固体地球物理学",
        "era_start": 1897,
        "culture_region": "Global",
        "source_url": "https://earthquake.usgs.gov/learn/topics/seismology/",
        "mathematical_formulation": r"M_w = \frac{2}{3}\log_{10}(M_0) - 10.7",
        "data_completeness": 92
    },
    {
        "name_ja": "海洋底拡大説",
        "name_en": "Seafloor Spreading",
        "definition": "ハリー・ヘス（1962年）が提唱。中央海嶺から玄武岩質マグマが噴出し、新しい海洋底が対称的に形成されながら左右に移動する。バイン＝マシューズの磁気縞模様（1963年）が決定的証拠となった。",
        "impact_summary": "プレートテクトニクス革命の核心証拠。海洋底の年齢・厚さ・磁気異常パターンを統一的に説明し、固体地球科学を変革した。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "プレートテクトニクス",
        "era_start": 1962,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/199947a0",
        "data_completeness": 90
    },
    {
        "name_ja": "地球磁気逆転",
        "name_en": "Geomagnetic Reversal",
        "definition": "地球磁場の極性が数万〜数百万年周期で反転する現象。中央海嶺の磁気縞模様・岩石残留磁化に記録される。最後の逆転は約78万年前（松山‐ブリュンヌ境界）。",
        "impact_summary": "海洋底拡大と地球年代学の決定的証拠。磁気層序による地質年代較正と古環境復元に不可欠なツール。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古地磁気学",
        "era_start": 1906,
        "culture_region": "Europe_Western",
        "source_url": "https://www.usgs.gov/faqs/can-the-magnetic-north-pole-switch-places-south-magnetic-pole",
        "data_completeness": 87
    },
    {
        "name_ja": "氷河学・氷床コア",
        "name_en": "Glaciology and Ice Core Records",
        "definition": "南極・グリーンランドの氷床コアは過去80万年以上の気温・CO2・ダスト・火山噴火を年層として記録する。EPICA・VOSTOK・GRIP計画が主要データ源。",
        "impact_summary": "気候変動の長期記録提供。氷期‐間氷期サイクルとGHG濃度の相関を直接示し、現代気候変動研究の基礎データを提供する。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古気候学",
        "era_start": 1966,
        "culture_region": "Global",
        "source_url": "https://www.ncdc.noaa.gov/paleo-search/study/2515",
        "data_completeness": 90
    },
    {
        "name_ja": "ミランコビッチサイクル",
        "name_en": "Milankovitch Cycles",
        "definition": "セルビアの天文学者ミルティン・ミランコビッチ（1941年）が提唱。地球軌道の離心率（10万年）・自転軸傾斜（4.1万年）・歳差運動（2.3万年）の周期的変化が日射量を変化させ、氷期‐間氷期サイクルを駆動する。",
        "impact_summary": "氷期の天文学的原因を定量的に説明。古気候学・古海洋学の基準年代枠組みとなり、数万年スケールの気候変動予測に使用される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古気候学",
        "era_start": 1941,
        "culture_region": "Europe_Eastern",
        "source_url": "https://earthobservatory.nasa.gov/features/Milankovitch",
        "mathematical_formulation": r"Q_{summer} \propto \frac{S}{(1-e^2)^{1/2}} \left(1 + e \sin\omega\right)^2 \sin\phi",
        "data_completeness": 92
    },
    {
        "name_ja": "大気大循環・ハドレー循環",
        "name_en": "General Circulation of the Atmosphere",
        "definition": "熱帯の加熱によりハドレー循環（0‐30°）・フェレル循環（30‐60°）・極循環（60‐90°）の3セル構造が形成される。偏西風・貿易風・ジェット気流を生む地球規模の熱・運動量輸送機構。",
        "impact_summary": "気象学・気候学の理論的基盤。モンスーン・砂漠帯・極前線の位置を規定し、農業・航空・気候モデルの中核をなす。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気象力学",
        "era_start": 1735,
        "culture_region": "Europe_Western",
        "source_url": "https://www.metoffice.gov.uk/weather/learn-about/weather/atmosphere/global-circulation-patterns",
        "mathematical_formulation": r"\frac{\partial \vec{v}}{\partial t} + (\vec{v}\cdot\nabla)\vec{v} = -\frac{1}{\rho}\nabla p - 2\vec{\Omega}\times\vec{v} + g\hat{k} + \vec{F}",
        "data_completeness": 90
    },
    {
        "name_ja": "熱塩循環",
        "name_en": "Thermohaline Circulation",
        "definition": "海水の温度・塩分差による密度差が駆動する全球規模の海洋深層循環。大西洋経線逆転循環（AMOC）を中核とし、熱を極方向へ輸送して気候を調節する。「海洋コンベヤーベルト」とも称される。",
        "impact_summary": "北大西洋の温暖気候維持と全球の熱・塩・栄養塩輸送を担う。気候変動による崩壊リスクは西欧の急激な寒冷化として表れる可能性がある。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "物理海洋学",
        "era_start": 1961,
        "culture_region": "Global",
        "source_url": "https://oceanservice.noaa.gov/education/tutorial_currents/05conveyor1.html",
        "data_completeness": 88
    },
    {
        "name_ja": "炭素循環",
        "name_en": "Global Carbon Cycle",
        "definition": "炭素は大気・海洋・陸上生物圏・岩石圏の間を光合成・呼吸・溶解・風化・火山活動で循環する。工業化以降の化石燃料燃焼により大気CO2が280 ppmから420 ppm以上に増加した。",
        "impact_summary": "地球温暖化・海洋酸性化の物理化学的基盤。IPCC気候モデルにおける最重要素過程であり、排出権取引・カーボンニュートラル政策の科学的根拠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球システム科学",
        "era_start": 1957,
        "culture_region": "Global",
        "source_url": "https://www.ipcc.ch/report/ar6/wg1/",
        "mathematical_formulation": r"\frac{d[C_{atm}]}{dt} = F_{emission} - F_{ocean} - F_{land}",
        "data_completeness": 92
    },
    {
        "name_ja": "オゾン層と紫外線防護",
        "name_en": "Ozone Layer and UV Protection",
        "definition": "成層圏のオゾン（O3）層は太陽紫外線B・Cを吸収して地表生命を保護する。モリナとロウランド（1974年）がCFCによるオゾン破壊を予測し、1985年の南極オゾンホール発見が証明した。",
        "impact_summary": "モントリオール議定書（1987年）による国際的CFC規制へ直結。環境科学が国際政策へ結びついた最初の成功事例であり、気候変動外交の先例となった。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "大気化学",
        "era_start": 1974,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/249810a0",
        "mathematical_formulation": r"O_3 + Cl \rightarrow ClO + O_2; \quad ClO + O \rightarrow Cl + O_2",
        "data_completeness": 90
    },
    {
        "name_ja": "プレートテクトニクス",
        "name_en": "Plate Tectonics",
        "definition": "地球の岩石圏が十数枚の剛体プレートに分かれ、マントル対流に乗って移動する理論。1960年代に大陸移動説・海底拡大説・古地磁気データが統合されて確立。収束・発散・すれ違いの3境界型が地震・火山活動を生む。",
        "impact_summary": "20世紀地球科学の最大革命。地震・火山・山脈・海洋の形成を統一的に説明し、資源探査・自然災害軽減・進化生物地理学の基盤となった。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "プレートテクトニクス",
        "era_start": 1967,
        "culture_region": "Global",
        "source_url": "https://www.usgs.gov/science/science-explorer/natural-hazards/plate-tectonics",
        "data_completeness": 95
    },
    {
        "name_ja": "水文循環",
        "name_en": "Hydrological Cycle",
        "definition": "水が蒸発・降水・表面流出・地下浸透・蒸散を通じて大気・陸域・海洋を循環する系。全球淡水流量は約5万km3/年。気候変動は降水パターン・氷河融解・洪水・干ばつ頻度を変化させる。",
        "impact_summary": "農業・水資源管理・洪水予測・生態系維持の科学的基盤。IPCC報告書における水関連リスク評価の中核フレームワーク。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "水文学",
        "era_start": 1580,
        "culture_region": "Global",
        "source_url": "https://water.usgs.gov/edu/watercycle.html",
        "data_completeness": 88
    },
    {
        "name_ja": "土壌形成と風化作用",
        "name_en": "Pedogenesis and Chemical Weathering",
        "definition": "岩石が物理・化学・生物的風化を受けてレゴリス・土壌へと変化する過程。炭酸塩風化はCO2を固定し長期炭素循環を制御する。ウォーカーフィードバック（温度感受性風化）が地球の気候安定化に寄与する。",
        "impact_summary": "農業生産性・炭素隔離・元素循環の基盤。気候変動と土地利用変化が土壌劣化を加速させる問題を評価する科学的枠組み。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球化学",
        "era_start": 1883,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.fao.org/soils-portal/en/",
        "mathematical_formulation": r"CaSiO_3 + CO_2 \rightarrow CaCO_3 + SiO_2",
        "data_completeness": 85
    },
    {
        "name_ja": "同位体地球化学",
        "name_en": "Isotope Geochemistry",
        "definition": "放射性・安定同位体比を利用して岩石・水・生物の年代・起源・温度履歴を決定する。K-Ar・Rb-Sr・U-Pb・δ18O・δ13C等が古気候・地質年代・物質循環の解析に使われる。",
        "impact_summary": "地質年代学・古気候学・海洋化学の定量的基盤。生命起源・大量絶滅・マグマ分化・惑星形成史の解明に不可欠なツール。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球化学",
        "era_start": 1947,
        "culture_region": "North_America",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-earth-060614-105301",
        "mathematical_formulation": r"\delta^{18}O = \left(\frac{({}^{18}O/{}^{16}O)_{sample}}{({}^{18}O/{}^{16}O)_{SMOW}} - 1\right) \times 1000",
        "data_completeness": 90
    },
    {
        "name_ja": "生物地球化学的循環",
        "name_en": "Biogeochemical Cycling",
        "definition": "窒素・リン・硫黄・水・炭素が生物・土壌・水・大気を循環する過程。窒素固定（Rhizobium）・硝化・脱窒が生態系の一次生産を制限し、リン循環は地質時間スケールで進行する。",
        "impact_summary": "農業施肥・富栄養化・海洋酸素欠乏・温室効果ガスの科学的基盤。惑星的境界（窒素・リンサイクルの変化）評価の中核概念。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球システム科学",
        "era_start": 1926,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.nature.com/articles/461472a",
        "data_completeness": 88
    },
    {
        "name_ja": "地球温暖化・強化温室効果",
        "name_en": "Global Warming and Enhanced Greenhouse Effect",
        "definition": "人為起源CO2・CH4・N2O・フロンガスの大気増加が地球の放射強制力を高め、地表温度を上昇させる現象。IPCC第6次報告書（2021年）は産業革命前比+1.1℃の温暖化を確認。",
        "impact_summary": "現代最重要の環境・政策問題。パリ協定（2015年）の科学的根拠となり、脱炭素エネルギー転換・適応策の緊急性を示す。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1896,
        "culture_region": "Global",
        "source_url": "https://www.ipcc.ch/report/ar6/wg1/",
        "mathematical_formulation": r"\Delta F = 5.35 \ln\!\left(\frac{C}{C_0}\right) \text{ [W/m}^2\text{]}",
        "data_completeness": 95
    },
    {
        "name_ja": "海洋酸性化",
        "name_en": "Ocean Acidification",
        "definition": "大気CO2が海水に溶解して炭酸（H2CO3）を形成し、海洋pHを低下させる現象。工業化以降pHは8.2から8.1に低下（0.1単位＝水素イオン濃度26%増）。サンゴ・貝・翼足類のCaCO3殻形成を阻害する。",
        "impact_summary": "海洋生態系・漁業・珊瑚礁への壊滅的リスク。「もう一つのCO2問題」と呼ばれ、気候変動政策と生物多様性保全の交差点に位置する。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "海洋化学",
        "era_start": 2003,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/425365a",
        "mathematical_formulation": r"CO_2 + H_2O \rightleftharpoons H_2CO_3 \rightleftharpoons H^+ + HCO_3^-",
        "data_completeness": 90
    },
    {
        "name_ja": "生物多様性ホットスポット",
        "name_en": "Biodiversity Hotspots",
        "definition": "ノーマン・マイヤーズ（1988年）が提唱。固有種が特に豊富でありながら生息地の70%以上が失われた地球上の25地域（後に36地域）。地球全固有種の半数以上がこれら地域に集中する。",
        "impact_summary": "保全生物学・生物多様性政策の中核フレームワーク。限られた資源で最大の保全効果を得るための優先地域選定基準として国際的に採用。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "保全生態学",
        "era_start": 1988,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/35002501",
        "data_completeness": 87
    },
    {
        "name_ja": "惑星境界（地球限界）",
        "name_en": "Planetary Boundaries",
        "definition": "ヨハン・ロックストローム（2009年）が提唱。人類文明が安全に活動できる地球システムの9つの限界値。気候変動・生物多様性・土地利用・淡水・窒素・リン・海洋酸性化・大気エアロゾル・新規物質を評価枠組みとする。",
        "impact_summary": "持続可能性科学の中核フレームワーク。国連持続可能な開発目標（SDGs）・欧州グリーンディール・ドーナツ経済学等の政策立案の科学的根拠となる。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球システム科学",
        "era_start": 2009,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/461472a",
        "data_completeness": 92
    },
    {
        "name_ja": "古地理学・大陸配置変遷",
        "name_en": "Paleogeography and Continental Configuration",
        "definition": "地質時代を通じた大陸の位置・形状・海洋の分布を復元する学問。ロディニア（9億年前）・ゴンドワナ・ローラシア・パンゲア（2.5億年前）の超大陸を経て現在の配置に至る。",
        "impact_summary": "生物の分布・進化・海流変化・古気候を理解するための基本枠組み。化石分布・鉱物資源・海洋循環の歴史的理解に不可欠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "プレートテクトニクス",
        "era_start": 1912,
        "culture_region": "Europe_Western",
        "source_url": "https://www.usgs.gov/science/science-explorer/natural-hazards/historical-perspective",
        "data_completeness": 87
    },
    {
        "name_ja": "火山学・マグマ学",
        "name_en": "Volcanology and Magmatology",
        "definition": "マグマの生成（マントル融解）・上昇・噴火過程を研究する地球科学分野。盾状火山・成層火山・カルデラの形態差、ハワイ型・プリニー式噴火の様式、火山灰による気候影響（VEI指数）を扱う。",
        "impact_summary": "火山災害軽減・プレート境界プロセス・資源形成（熱水鉱床・地熱）の理解の基盤。超大陸崩壊・大量絶滅との関連（シベリアトラップ等）も研究される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "固体地球物理学",
        "era_start": 1815,
        "culture_region": "Global",
        "source_url": "https://www.usgs.gov/programs/VHP",
        "data_completeness": 87
    },
    {
        "name_ja": "津波の物理と予測",
        "name_en": "Tsunami Physics and Early Warning",
        "definition": "海底地震・海底火山・山体崩壊が引き金となる長波長波浪（津波）の生成・伝播・沿岸増幅の物理過程。浅水波として伝播し（速度√(gd)）、沿岸部で波高が激増する。2004年インド洋・2011年東日本大震災が転機となった。",
        "impact_summary": "太平洋津波警報センター（PTWC）・IOCの国際警報システム構築の科学的基盤。地震センサー・深海圧力計・衛星を組み合わせたリアルタイム予測システムに発展。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球物理学",
        "era_start": 1946,
        "culture_region": "Global",
        "source_url": "https://itic.ioc-unesco.org/",
        "mathematical_formulation": r"c = \sqrt{gd}, \quad \eta(x,t) = A\cos(kx - \omega t)",
        "data_completeness": 88
    },
    {
        "name_ja": "砂漠化と土地劣化",
        "name_en": "Desertification and Land Degradation",
        "definition": "乾燥・半乾燥地での土地生産性の不可逆的低下。過耕作・過放牧・森林伐採・気候変動の相乗効果で進行し、UNCCD推計では世界陸域の40%が影響を受け、31億人が脆弱。",
        "impact_summary": "食料安全保障・移民・地域紛争と直結するグローバル課題。「2030年土地劣化中立」目標の科学的根拠となり、砂漠緑化（中国三北防護林等）政策を後押し。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "環境科学",
        "era_start": 1977,
        "culture_region": "Global",
        "source_url": "https://www.unccd.int/land-and-life/desertification/overview",
        "data_completeness": 85
    },
    {
        "name_ja": "海面上昇の観測と予測",
        "name_en": "Sea Level Rise",
        "definition": "熱膨張・氷床融解・山岳氷河縮小により海面が上昇する現象。IPCC AR6は2100年時点で1.5℃目標でも0.3〜1.0m上昇を予測。超過した場合は低地都市・島嶼国への壊滅的影響が生じる。",
        "impact_summary": "バングラデシュ・ミクロネシア・ニューオーリンズ・東京等の沿岸低地都市の存続問題。適応策（堤防・移住）と気候緩和策の統合計画立案の科学的根拠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1993,
        "culture_region": "Global",
        "source_url": "https://sealevel.nasa.gov/",
        "data_completeness": 90
    },
    {
        "name_ja": "アフリカの気候学と季節風",
        "name_en": "African Climate and Monsoon Systems",
        "definition": "サハラ以南アフリカは熱帯収束帯（ITCZ）の季節移動が雨季・乾季を決定する。西アフリカモンスーン・インド洋ダイポールがサヘル・東アフリカの降水変動を支配し、農業・食料安全保障と直結する。",
        "impact_summary": "アフリカ54ヶ国・13億人の農業・水資源・疾病（マラリア・コレラ）パターンを規定。IGAD・AUSEにおける気候サービス構築の科学的基盤。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1960,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.wmo.int/pages/prog/wcp/agm/agm_home_en.html",
        "data_completeness": 83
    },
    {
        "name_ja": "インド洋ダイポールと南アジアモンスーン",
        "name_en": "Indian Ocean Dipole and South Asian Monsoon",
        "definition": "インド洋ダイポール（IOD）はインド洋東西の海面水温非対称を表す指標。正のIODは東アフリカ・インド降水増加・オーストラリア乾燥をもたらす。南アジアモンスーンはインド亜大陸の農業を支える季節風システム。",
        "impact_summary": "インド・スリランカ・東アフリカの農業・水文・食料安全保障と直結。ENSO・IODの相互作用理解が中期気候予測の精度向上に不可欠。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "海洋気候学",
        "era_start": 1999,
        "culture_region": "South_Asia",
        "source_url": "https://www.nature.com/articles/44373",
        "data_completeness": 85
    },
    {
        "name_ja": "黄土（ローム）堆積と風成層序",
        "name_en": "Loess Deposits and Aeolian Stratigraphy",
        "definition": "風によって堆積した細粒土（黄土/ローム）は古気候・古環境の高分解能記録を提供する。中国の黄土高原（世界最厚・最連続的黄土堆積）は過去250万年の東アジア夏季モンスーン変動を記録する。",
        "impact_summary": "東アジア気候史・土壌肥沃度・農業文明発展との関係解明。ミランコビッチサイクルと古モンスーン変動の相関を氷床コアとは独立に検証する重要記録媒体。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古気候学",
        "era_start": 1985,
        "culture_region": "East_Asia",
        "source_url": "https://www.nature.com/articles/325143a0",
        "data_completeness": 85
    },
    {
        "name_ja": "地球化学的フロンティア—金属循環",
        "name_en": "Geochemical Metal Cycling",
        "definition": "鉄・マンガン・銅・亜鉛等の金属元素が地殻・海洋・生物圏を循環する過程。熱水噴出孔・風化・大気沈着が海洋微量金属を補給し、海洋生物生産と連動する。",
        "impact_summary": "深海鉱物資源（マンガン団塊・熱水硫化物）の分布・形成を説明。微量金属制限下での海洋生産性・炭素固定量の変動が炭素循環モデルに組み込まれる。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球化学",
        "era_start": 1970,
        "culture_region": "Global",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-marine-010816-060526",
        "data_completeness": 83
    },
    {
        "name_ja": "古海洋学と深海堆積物",
        "name_en": "Paleoceanography and Deep Sea Sediments",
        "definition": "深海底の堆積物コア（有孔虫・珪藻・放散虫・炭酸塩）は海水温・塩分・栄養塩・海流を数百万年にわたり記録する。ODP・IODP計画が全球的データを提供。",
        "impact_summary": "新生代気候史・大量絶滅前後の海洋変化・海面変動の直接証拠を提供。ミランコビッチ理論の海洋側検証と古気候モデル較正の主要データ源。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古海洋学",
        "era_start": 1968,
        "culture_region": "Global",
        "source_url": "https://www.iodp.org/",
        "data_completeness": 87
    },
    {
        "name_ja": "エルニーニョ・南方振動（ENSO）",
        "name_en": "El Niño–Southern Oscillation",
        "definition": "熱帯太平洋の海面水温異常と大気圧差（南方振動）が2〜7年周期で変動するシステム。エルニーニョ期は東太平洋が温暖・ウォーカー循環が弱化し、世界各地に異常気象をもたらす。",
        "impact_summary": "全球気候予測の中核モード。農業・漁業・水資源・熱帯感染症・森林火災への影響を数ヶ月前から予測可能にし、食料安全保障政策に活用される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "海洋気候学",
        "era_start": 1923,
        "culture_region": "Global",
        "source_url": "https://www.climate.gov/enso",
        "mathematical_formulation": r"SST_{Nino3.4} = \overline{T}_{170W-120W, 5S-5N}",
        "data_completeness": 90
    },
    {
        "name_ja": "宇宙風化と惑星表面進化",
        "name_en": "Space Weathering and Planetary Surface Evolution",
        "definition": "太陽風・宇宙線・微小隕石衝突により、大気を持たない天体（月・小惑星）の表面鉱物が変質する過程。アモルファス層形成・ナノ鉄粒子生成・反射スペクトル変化をもたらし、リモートセンシングによる鉱物同定に影響する。",
        "impact_summary": "はやぶさ（JAXA）等の小惑星サンプル解析の解釈、月面資源開発・行星惑星地質年代の精密化に不可欠な概念。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "惑星科学",
        "era_start": 1975,
        "culture_region": "East_Asia",
        "source_url": "https://www.nature.com/articles/s41550-020-1206-7",
        "data_completeness": 82
    },
    {
        "name_ja": "古代インドの地球科学的知識",
        "name_en": "Ancient Indian Knowledge of Earth Sciences",
        "definition": "ヴェーダ時代（BC1500〜）から地層・鉱物・地震・天文を体系化した知識。アリヤバッタは地球の自転を認識し（499年）、ブラフマグプタは重力の概念を示唆した。スシュルタ・サンヒターは鉱物薬学（ラサシャーストラ）を記述した。",
        "impact_summary": "アラブ経由でヨーロッパ地球科学に影響した非西洋知識体系。植民地時代の「西洋発見」叙述を修正し、科学史の多元性を示す事例として重要。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "科学史",
        "era_start": -1500,
        "culture_region": "South_Asia",
        "source_url": "https://www.insa.nic.in/article/history-of-science-in-india",
        "data_completeness": 78
    },
    {
        "name_ja": "中国古代の地質・地震記録",
        "name_en": "Ancient Chinese Geological and Seismological Records",
        "definition": "張衡（132年）が世界最古の地震計（候風地動儀）を製作。沈括（1088年）は化石貝・竹の林の発見から地殻変動と古環境を推論した（夢渓筆談）。明代の農書・地志は洪水・地滑り・火山を詳細に記録した。",
        "impact_summary": "長期地震・地質・気候記録の保全と科学史研究における東アジア知識体系の評価。現代の古代地震研究（歴史地震学）に活用される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "科学史",
        "era_start": 132,
        "culture_region": "East_Asia",
        "source_url": "https://www.cambridge.org/core/books/history-of-chinese-science/",
        "data_completeness": 80
    },
    {
        "name_ja": "メソポタミアの天気記録と農耕気候学",
        "name_en": "Mesopotamian Weather Records and Agricultural Climatology",
        "definition": "バビロニア（BC800〜）の泥板文書には降水・洪水・干ばつの体系的記録が残り、農耕・灌漑管理に利用された。ムルアピン天文典（BC1000頃）は季節と農事を天文に対応させた。",
        "impact_summary": "人類最古の体系的気候記録の一つ。歴史気候学・農業文明起源研究の基礎データ。チグリス・ユーフラテス流域の水文変化史研究に応用される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "科学史",
        "era_start": -800,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.cambridge.org/core/journals/journal-of-the-economic-and-social-history-of-the-orient",
        "data_completeness": 75
    },
]

BATCH2 = [
    {
        "name_ja": "衛星リモートセンシングと地球観測",
        "name_en": "Satellite Remote Sensing and Earth Observation",
        "definition": "人工衛星から地表・海洋・大気を電磁波（可視・赤外・マイクロ波・SAR）で観測する技術。LANDSATシリーズ（1972年〜）・MODISが土地被覆変化・海面温度・植生指数（NDVI）の長期監視を実現した。",
        "impact_summary": "気候変動・森林消失・都市化・農業監視の不可欠インフラ。GAFAや国際機関が活用する開放データ（Copernicus・NASA Earthdata）の基盤技術。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "地球観測",
        "era_start": 1972,
        "culture_region": "Global",
        "source_url": "https://landsat.gsfc.nasa.gov/",
        "data_completeness": 90
    },
    {
        "name_ja": "地下水と帯水層",
        "name_en": "Groundwater and Aquifer Systems",
        "definition": "地下の砂礫・岩盤の間隙に貯留される淡水資源。confined/unconfined帯水層、涵養速度・採取量のバランスが持続可能性を決定。オガララ帯水層（米国）・インダス平野帯水層の過剰採取が世界的問題となっている。",
        "impact_summary": "世界の農業用水の43%・飲料水の50%を担う隠れた水資源。GRACE衛星による帯水層枯渇観測が政策立案のデータ提供に貢献している。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "水文地質学",
        "era_start": 1856,
        "culture_region": "Global",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/drinking-water",
        "mathematical_formulation": r"q = -K \frac{dh}{dl} \quad \text{(Darcy's Law)}",
        "data_completeness": 87
    },
    {
        "name_ja": "自然災害リスク評価",
        "name_en": "Natural Hazard Risk Assessment",
        "definition": "地震・火山・洪水・台風・土砂崩れ等の自然現象のハザード（頻度・規模）×露出（人口・資産）×脆弱性を定量化してリスクを評価する枠組み。仙台防災枠組（2015〜2030年）の科学的基盤。",
        "impact_summary": "死者ゼロを目指す防災政策の定量根拠。UNDRR・世界銀行・保険業界が活用するリスクモデルの科学的基礎であり、土地利用計画・建築基準に反映される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "環境科学",
        "era_start": 1990,
        "culture_region": "Global",
        "source_url": "https://www.undrr.org/sendai-framework",
        "mathematical_formulation": r"R = H \times E \times V",
        "data_completeness": 87
    },
    {
        "name_ja": "熱帯雨林生態学",
        "name_en": "Tropical Rainforest Ecology",
        "definition": "熱帯収束帯の高温多雨下で発達する多層構造（林冠・亜林冠・林床）の生態系。地球の種多様性の50〜80%を収容し、炭素貯蔵・水蒸気蒸散・雲形成を通じて地域・全球気候を制御する。",
        "impact_summary": "アマゾン・コンゴ・ボルネオの熱帯雨林は「地球の肺」。伐採・火入れによる炭素放出がIPCC排出シナリオに組み込まれ、REDD+制度の科学的根拠をなす。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "生態学",
        "era_start": 1898,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/nature14967",
        "data_completeness": 87
    },
    {
        "name_ja": "生態系サービス",
        "name_en": "Ecosystem Services",
        "definition": "自然生態系が人間社会に提供する財とサービスを4カテゴリ（供給・調整・文化・基盤）で分類する概念（ミレニアム生態系評価、2005年）。大気浄化・洪水緩衝・花粉媒介・水質浄化等が含まれる。",
        "impact_summary": "生物多様性条約の科学的基盤。自然資本の経済的価値評価（TEEB・IPBES）・緑の経済・ESG投資の科学的根拠として国際政策に広く採用。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "環境経済学・保全生態学",
        "era_start": 2001,
        "culture_region": "Global",
        "source_url": "https://www.millenniumassessment.org/",
        "data_completeness": 90
    },
    {
        "name_ja": "岩石磁気学・古地磁気学",
        "name_en": "Rock Magnetism and Paleomagnetism",
        "definition": "岩石中の磁性鉱物（磁鉄鉱・ヘマタイト）が冷却・堆積時に地磁気を記録する特性を利用し、過去の磁場方向と強度を復元する学問。地磁気逆転の年代表（地磁気年代スケール）と大陸移動速度の定量化に使われる。",
        "impact_summary": "プレートテクトニクス確立の決定的証拠を提供。海底磁気縞模様の解析・火山岩の定向磁化・堆積物の残留磁化が古地理復元の主ツール。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "古地磁気学",
        "era_start": 1954,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/175033a0",
        "data_completeness": 87
    },
    {
        "name_ja": "成層圏エアロゾルと火山強制力",
        "name_en": "Stratospheric Aerosols and Volcanic Forcing",
        "definition": "大規模火山噴火（タンボラ1815・ピナトゥボ1991）がSO2を成層圏に注入し、硫酸塩エアロゾルが太陽放射を散乱して地表を一時的に冷却する。「夏のない年」（1816年）はタンボラ噴火後の農業危機を引き起こした。",
        "impact_summary": "気候システムの自然強制力の定量化。太陽地球工学（成層圏エアロゾル注入）の科学的先例として、気候変動緩和代替策の議論に活用される。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "気候科学",
        "era_start": 1783,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/359142a0",
        "data_completeness": 87
    },
    {
        "name_ja": "地球の熱流量と地熱エネルギー",
        "name_en": "Earth's Heat Flow and Geothermal Energy",
        "definition": "地球内部（放射性崩壊＋原始熱）から表面への熱流量は平均47 TW。地熱勾配は平均25〜30°C/kmで、地熱発電（地熱フラッシュ・バイナリー・EGS）・直接熱利用に活用される。アイスランド・ケニア・フィリピン・日本が主要国。",
        "impact_summary": "再生可能エネルギーとして24時間安定発電が可能。アフリカ地溝帯（ケニア・エチオピア）の地熱開発は東アフリカのエネルギー貧困解消に貢献しうる。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "固体地球物理学",
        "era_start": 1904,
        "culture_region": "Global",
        "source_url": "https://www.irena.org/geothermal",
        "data_completeness": 85
    },
    {
        "name_ja": "生物礁と珊瑚礁生態学",
        "name_en": "Coral Reef Ecology and Biogenic Reefs",
        "definition": "造礁サンゴの炭酸カルシウム骨格が形成する複雑な三次元構造物。海洋面積の0.1%に過ぎないが25%の海洋種が依存する。白化現象（海水温上昇・酸性化による共生藻類の喪失）が地球規模で進行している。",
        "impact_summary": "水産・観光・沿岸保護に年間375億ドルの経済的価値。現状のCO2排出軌跡では2100年までに機能的消滅の可能性が高く、生物多様性条約・気候政策の最前線問題。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "海洋生態学",
        "era_start": 1842,
        "culture_region": "Global",
        "source_url": "https://www.coralreefwatch.noaa.gov/",
        "data_completeness": 87
    },
    {
        "name_ja": "大気汚染と粒子状物質",
        "name_en": "Air Pollution and Particulate Matter",
        "definition": "PM2.5（粒径2.5μm以下の微粒子）・NO2・O3・SO2等の大気汚染物質が人体・生態系に及ぼす影響を研究する分野。WHO推計では年間700万人が大気汚染関連疾患で死亡。中国・インドの急速工業化が主要な発生源となっている。",
        "impact_summary": "世界最大の環境リスク要因の一つ。アジア・アフリカの都市部健康被害・農業被害（オゾン）・気候変動（黒色炭素）との相互作用研究が進展。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "大気化学",
        "era_start": 1952,
        "culture_region": "Global",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health",
        "data_completeness": 87
    },
    {
        "name_ja": "地球外物質の地球科学的影響（隕石・小惑星衝突）",
        "name_en": "Extraterrestrial Impacts on Earth",
        "definition": "小惑星・彗星の衝突が地球の地質・生物進化に与えた影響を研究する衝突地質学。ユカタン半島のチクシュルーブクレーター（6600万年前、直径180km）が白亜紀-古第三紀大量絶滅の主因とされ、アルヴァレス仮説（1980年）が証明した。",
        "impact_summary": "生命進化の非連続性と突発的環境変動の理解。惑星防衛（NASAのDART計画2022年）の科学的根拠となり、将来の地球衝突リスク評価と偏向技術開発を駆動する。",
        "subfield": "地球科学・環境科学",
        "school_of_thought": "惑星科学",
        "era_start": 1980,
        "culture_region": "North_America",
        "source_url": "https://www.science.org/doi/10.1126/science.208.4448.1095",
        "data_completeness": 88
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)

    total = 0
    for i, batch in enumerate([BATCH1, BATCH2], 1):
        n = insert_batch(conn, batch)
        total += n
        print(f"  Batch {i}: {n} inserted (running total: {total})")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"\nBatch7 earth: {total} concepts inserted")
    print(f"Total in table: {count}")
