"""
DUA Wave A2 Batch 11 — 物理学 追加 (Physics supplement)
Target: ~80 concepts
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

CONCEPTS = [
    {
        "name_ja": "ヴァン・デル・ワールス力と分子間力",
        "name_en": "Van der Waals Forces and Intermolecular Interactions",
        "definition": "分子間に働く非共有結合性引力（ロンドン分散力・双極子-双極子力・誘起双極子力）の総称。ヨハネス・ディデリク・ファン・デル・ワールス（1873年）の実在気体方程式が出発点。生物分子認識・気体液化・薄膜接着に基本的役割を果たす。",
        "impact_summary": "ゲッコーの足の粘着・自己組織化単分子膜・MOF多孔性材料・タンパク質フォールディングの理解に必須。超高精度の原子間力顕微鏡測定で単分子レベルの力が直接計測される。",
        "subfield": "物理学",
        "school_of_thought": "統計力学・物性物理学",
        "era_start": 1873,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/nnano.2013.196",
        "mathematical_formulation": r"U_{vdW}(r) = -\frac{C_6}{r^6}",
        "data_completeness": 87
    },
    {
        "name_ja": "非平衡統計力学と揺動散逸定理",
        "name_en": "Non-Equilibrium Statistical Mechanics and Fluctuation-Dissipation Theorem",
        "definition": "平衡近傍の非平衡系において、外乱への線形応答係数（散逸）が系の熱揺らぎ（相関関数）と等しいとする定理（カレン・ウェルトン1951年）。オンサーガーの相反定理・久保公式が体系的に非平衡現象を記述する。",
        "impact_summary": "ブラウン運動の精密解析・電気雑音測定・生物モーター効率測定・分子機械設計の理論的基盤。レプリカ理論・ジャルジンスキー等式等の現代非平衡統計力学への架け橋。",
        "subfield": "物理学",
        "school_of_thought": "統計力学",
        "era_start": 1951,
        "culture_region": "Japan",
        "source_url": "https://journals.aps.org/pr/abstract/10.1103/PhysRev.83.34",
        "mathematical_formulation": r"S_{xx}(\omega) = \frac{2k_BT}{\omega}\mathrm{Im}[\chi(\omega)]",
        "data_completeness": 87
    },
    {
        "name_ja": "量子場理論とファインマン経路積分",
        "name_en": "Quantum Field Theory and Feynman Path Integral",
        "definition": "場を量子化し素粒子を場の励起として記述する理論。ファインマン（1948年）の経路積分法は量子振幅を全経路の重ね合わせとして定式化し、摂動計算・ファインマン図表・規格化の体系を確立した。QED・QCD・標準模型の数学的基盤。",
        "impact_summary": "素粒子標準模型の計算ツール。QEDの電子異常磁気モーメント計算（精度10^{-12}）は物理学史上最精密の予測。経路積分は量子重力・弦理論・量子コンピュータのアルゴリズム設計にも応用される。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1948,
        "culture_region": "North_America",
        "source_url": "https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.20.367",
        "mathematical_formulation": r"Z = \int \mathcal{D}\phi \, e^{iS[\phi]/\hbar}",
        "data_completeness": 92
    },
    {
        "name_ja": "スピン液体と量子スピン系",
        "name_en": "Quantum Spin Liquids",
        "definition": "磁性スピンが絶対零度でも長距離秩序を形成せず、量子揺らぎにより液体的状態を保つ磁性相。アンダーソン（1973年）が共鳴原子価結合（RVB）として提唱。フラクショナルエクシタトン・マヨラナフェルミオン的準粒子を持ち、フォールトトレラント量子コンピュータの候補。",
        "impact_summary": "トポロジカル量子コンピュータの物理的基盤の候補。銅酸化物高温超伝導の近接相として研究され、強相関電子系・幾何学的フラストレーション・非アーベル統計の実験場。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1973,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/nphys4477",
        "data_completeness": 85
    },
    {
        "name_ja": "冷却原子と光格子",
        "name_en": "Ultracold Atoms and Optical Lattices",
        "definition": "レーザー冷却・蒸発冷却で数十nKまで冷却した原子を、定在光波（光格子）に閉じ込め、強相関格子系をシミュレートする量子シミュレーション技術。ヤコーシュとブロッホ（2002年）がモット絶縁体‐超流動相転移を実証した。",
        "impact_summary": "強相関電子系・高温超伝導・量子磁性の「量子シミュレータ」として機能する。量子コンピュータの中性原子プラットフォームの物理的基盤であり、量子誤り訂正符号の実験実現を目指す。",
        "subfield": "物理学",
        "school_of_thought": "原子分子光学物理学",
        "era_start": 2002,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/415039a",
        "data_completeness": 88
    },
    {
        "name_ja": "量子デコヒーレンスと量子-古典境界",
        "name_en": "Quantum Decoherence and Quantum-Classical Boundary",
        "definition": "量子系が環境と相互作用することで量子重ね合わせが急速に失われる（デコヒーレンス）現象。ツーレク（1981年）・ヨース＝ツェー（1985年）が理論化。マクロな物体が古典的に見える理由を説明し、測定問題・量子コンピュータの誤りの主因となる。",
        "impact_summary": "量子コンピュータの量子誤り訂正の根本的動機。測定問題・多世界解釈・コペンハーゲン解釈の区別に関わる。マクロ量子重ね合わせの上限（猫の問題の科学的解答）を規定する。",
        "subfield": "物理学",
        "school_of_thought": "量子力学基礎論",
        "era_start": 1981,
        "culture_region": "North_America",
        "source_url": "https://www.nature.com/articles/nature10377",
        "data_completeness": 87
    },
    {
        "name_ja": "超対称性理論（SUSY）",
        "name_en": "Supersymmetry Theory (SUSY)",
        "definition": "ボソンとフェルミオンを結びつける対称性（超対称変換）を仮定する素粒子理論。ワインバーグ・グルフィン等（1974年）が定式化。標準模型の階層性問題・暗黒物質候補（中立要素中和子）・大統一理論への足がかりを提供するが、LHC実験で実験的証拠が得られていない。",
        "impact_summary": "超弦理論の数学的基盤。LHCでSUSY粒子が未検出であることが素粒子物理学の「砂漠問題」を深刻化させ、自然性原理の再考・景観問題との関連で現代物理学の最前線課題となる。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1974,
        "culture_region": "North_America",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.nucl.53.041002.110401",
        "data_completeness": 85
    },
    {
        "name_ja": "弦理論とM理論",
        "name_en": "String Theory and M-Theory",
        "definition": "素粒子を0次元の点でなく1次元の振動する弦（文字列）として記述する理論。南部陽一郎・ニールセン・サスキンド（1970年）が先駆け。5種の超弦理論が11次元M理論で統一される（ウィッテン1995年）。余剰次元・コンパクト化・AdS/CFT対応を含む。",
        "impact_summary": "重力と量子場理論の統合（量子重力）の最有力候補。ブラックホールのエントロピー計算（ストロミンジャー・ヴァファ1996年）・AdS/CFT対応による強結合QCDの解析に貢献した。実験的検証可能性が根本的課題。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1970,
        "culture_region": "East_Asia",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.nucl.55.090103.134232",
        "data_completeness": 85
    },
    {
        "name_ja": "AdS/CFT対応（ホログラフィー原理）",
        "name_en": "AdS/CFT Correspondence and Holographic Principle",
        "definition": "マルダセナ（1997年）が提唱。（d+1）次元の反ドジッター空間上の重力理論がd次元境界の共形場理論と等価である双対性。「ホログラフィー原理」の具体的実現。強相関系・クォーク・グルーオンプラズマ・黒穴情報問題の研究ツール。",
        "impact_summary": "弦理論から凝縮系物理・重イオン衝突・量子情報に橋をかけた。ブラックホール情報パラドックスへの新たなアプローチを提供し、「情報は保存されるか」という根本問題に迫る。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1997,
        "culture_region": "South_America",
        "source_url": "https://arxiv.org/abs/hep-th/9711200",
        "mathematical_formulation": r"Z_{grav}[AdS_{d+1}] = Z_{CFT}[\partial AdS]",
        "data_completeness": 88
    },
    {
        "name_ja": "ニュートリノ質量と振動",
        "name_en": "Neutrino Mass and Oscillations",
        "definition": "ニュートリノが飛行中に3フレーバー間で確率的に変換する現象（ニュートリノ振動）。ポンテコルヴォ（1957年）が予言し、スーパーカミオカンデ（1998年、梶田隆章）・SNO（2001年）が確立した。標準模型の修正を要する最初の実験的証拠。",
        "impact_summary": "ノーベル物理学賞2015年（梶田・マクドナルド）。標準模型を超えた新物理の最初の確立した証拠。ニュートリノの絶対質量・マヨラナ性・CP対称性の破れが次の探索課題で、宇宙の物質優勢の解明に関わる。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1998,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/2015/kajita/facts/",
        "mathematical_formulation": r"P(\nu_\alpha \to \nu_\beta) = \sum_{i,j} U_{\alpha i}^* U_{\beta i} U_{\alpha j} U_{\beta j}^* e^{-i\Delta m^2_{ij} L/2E}",
        "data_completeness": 90
    },
    {
        "name_ja": "プラズマ物理学と核融合",
        "name_en": "Plasma Physics and Nuclear Fusion",
        "definition": "高温電離気体（プラズマ）の電磁流体力学的振る舞いを研究する分野。核融合炉（トカマク・ITER）は重水素・三重水素プラズマを1億K以上に加熱し、D+T→He+n反応を利用する。磁気閉じ込め（トカマク・ステラレータ）・慣性閉じ込め（NIF）が主要方式。",
        "impact_summary": "炭素排出のない無限エネルギー源としての核融合発電の実現を目指す。NIF（2022年）が燃料投入エネルギーを超えるレーザー核融合を初実証。ITER完成が2025年代を目標とし、商用核融合炉の建設競争が開始された。",
        "subfield": "物理学",
        "school_of_thought": "プラズマ物理学",
        "era_start": 1950,
        "culture_region": "Global",
        "source_url": "https://www.iter.org/",
        "mathematical_formulation": r"Q = \frac{P_{fusion}}{P_{input}} > 1",
        "data_completeness": 90
    },
    {
        "name_ja": "量子光学と光子縺れ実験",
        "name_en": "Quantum Optics and Photon Entanglement Experiments",
        "definition": "光と物質の量子的相互作用を研究する分野。アスペ実験（1982年）がベルの不等式の破れを確認し、量子もつれの実在性を証明した。クラウサー・アスペ・ツァイリンガー（2022年ノーベル物理学賞）が代表的人物。単一光子源・光子検出・量子テレポーテーション・QKD（量子鍵配送）が主要応用。",
        "impact_summary": "量子情報科学の実験的基盤。量子通信・量子暗号・量子コンピュータの光子ベースプラットフォームの物理的基礎。ベルの不等式実験は哲学的・物理学的意味で20世紀最重要実験の一つ。",
        "subfield": "物理学",
        "school_of_thought": "量子力学基礎論",
        "era_start": 1982,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/physics/2022/press-release/",
        "data_completeness": 90
    },
    {
        "name_ja": "半導体物理と電子バンド理論",
        "name_en": "Semiconductor Physics and Electronic Band Theory",
        "definition": "固体の電子状態をバンド構造（許容帯・禁止帯）で記述する理論。ブロッホの定理（1928年）・ウィルソン（1931年）・ブラタン・バーディン・ショックレーのトランジスタ発明（1947年）が転換点。p-n接合・MOSFET・ヘテロ接合が電子デバイスの物理的基盤。",
        "impact_summary": "現代の情報化社会の物質的基盤。ムーアの法則（1965年）に従ったトランジスタの微細化により現代コンピュータ・スマートフォン・太陽電池・LED・レーザーが実現した。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1928,
        "culture_region": "Global",
        "source_url": "https://www.nobelprize.org/prizes/physics/1956/press-release/",
        "mathematical_formulation": r"\psi_{nk}(r) = e^{ikr} u_{nk}(r), \quad E_n(k)",
        "data_completeness": 92
    },
    {
        "name_ja": "光-物質相互作用と分光法の歴史",
        "name_en": "Light-Matter Interaction and History of Spectroscopy",
        "definition": "フラウンホーファー（1814年）の暗線発見・キルヒホッフ＝ブンゼン（1859年）の発光分析・バルマー（1885年）の水素線系列が原子スペクトルの発見史を形成した。ボーア原子モデル（1913年）・シュレーディンガー方程式が量子論的説明を与えた。",
        "impact_summary": "原子・分子構造解明の出発点。天体の化学組成分析・核磁気共鳴（NMR）・レーザー分光・LIDAR等への展開が現代科学技術の中心を担う。",
        "subfield": "物理学",
        "school_of_thought": "原子分子物理学",
        "era_start": 1814,
        "culture_region": "Europe_Western",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.anchem.1.031207.113216",
        "data_completeness": 88
    },
    {
        "name_ja": "磁気共鳴（NMR・MRI）",
        "name_en": "Nuclear Magnetic Resonance and MRI",
        "definition": "核スピンが外部磁場中で共鳴する現象（ラビ1938年・ブロッホ・パーセル1946年）。パルスNMR（エルンスト1966年）が高分解能化学分析を実現し、ラウターバー・マンスフィールド（1973年）がMRI装置に発展させた。",
        "impact_summary": "化学構造決定の最強ツール（NMR）と医療画像の標準（MRI）。ノーベル賞2003年（ラウターバー・マンスフィールド）。タンパク質三次元構造・拡散強調MRI・機能的MRI（fMRI）への発展。",
        "subfield": "物理学",
        "school_of_thought": "原子分子物理学",
        "era_start": 1946,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/physics/1952/press-release/",
        "mathematical_formulation": r"\omega_0 = \gamma B_0",
        "data_completeness": 90
    },
    {
        "name_ja": "2次元材料と「グラフェン革命」",
        "name_en": "Two-Dimensional Materials and the Graphene Revolution",
        "definition": "ガイム＝ノボセロフ（2004年）がスコッチテープ法で単原子層のグラフェンを単離し（ノーベル物理学賞2010年）、二次元材料の新領域を開拓した。六方晶窒化ホウ素・遷移金属ダイカルコゲナイド（MoS2等）・ツイストバイレイヤーグラフェン（魔角グラフェン）が続く。",
        "impact_summary": "電子移動度・熱伝導率・強度が桁違いの新材料。半導体の次世代材料・柔軟電子デバイス・バリア膜・エネルギー貯蔵への応用を目指す。ツイストバイレイヤーグラフェンの超伝導発見（2018年、曹原）が凝縮系物理に衝撃を与えた。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 2004,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/physics/2010/press-release/",
        "mathematical_formulation": r"E(k) = \pm v_F \hbar |k|, \quad v_F \approx 10^6 \text{ m/s}",
        "data_completeness": 90
    },
    {
        "name_ja": "宇宙線研究と粒子加速器の歴史",
        "name_en": "Cosmic Ray Research and Particle Accelerator History",
        "definition": "ヘス（1912年）の宇宙線発見から始まり、陽電子（アンダーソン1932年）・ミュオン・パイ中間子・奇妙粒子が宇宙線実験で発見された。コッククロフト＝ウォルトン型→バンデグラーフ→サイクロトロン（ローレンス1930年）→シンクロトロンと加速器技術が進化し、現在はLHCが最高エネルギーを実現。",
        "impact_summary": "素粒子物理学・核物理学の実験的基盤の発展史。医療（放射線治療・PET）・材料改質（イオン注入）・中性子ビーム（物質構造解析）への応用が産業・医療に広く浸透。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1912,
        "culture_region": "Global",
        "source_url": "https://home.cern/science/accelerators/history",
        "data_completeness": 88
    },
    {
        "name_ja": "非線形光学と光の高調波発生",
        "name_en": "Nonlinear Optics and Harmonic Generation",
        "definition": "強力なレーザー光と媒質の非線形相互作用で倍波（SHG）・三倍波・光パラメトリック過程が生じる現象。フランケン（1961年）が最初に確認。ブロンベルゲン・ブロッホの非線形光学理論（1962年）が体系化。フェムト秒レーザー・アト秒光パルス生成の基盤。",
        "impact_summary": "波長変換デバイス・超高速分光・二光子顕微鏡・レーザー通信・量子情報（もつれ光子対生成）の技術的基盤。アト秒科学（ノーベル物理学賞2023年）の中核技術。",
        "subfield": "物理学",
        "school_of_thought": "光学・レーザー物理学",
        "era_start": 1961,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/physics/1981/press-release/",
        "mathematical_formulation": r"P^{(n)}(t) = \epsilon_0 \chi^{(n)} E^n(t)",
        "data_completeness": 87
    },
    {
        "name_ja": "スピントロニクス",
        "name_en": "Spintronics",
        "definition": "電子のスピン角運動量を情報担体として利用する電子工学分野。巨大磁気抵抗（GMR）効果をフェールとグリュンベルク（1988年）が発見（ノーベル物理学賞2007年）。GMRヘッドによるハードディスクの記録密度革命・MRAM・スピン軌道トルク素子が代表的成果。",
        "impact_summary": "現代HDD（全出荷のGMRヘッド）・MRAM（不揮発性高速メモリ）の技術的基盤。量子コンピュータのスピン量子ビット・スキルミオンメモリ・テラヘルツスピントロニクスが次の展開。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1988,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/physics/2007/press-release/",
        "data_completeness": 87
    },
    {
        "name_ja": "量子熱力学",
        "name_en": "Quantum Thermodynamics",
        "definition": "熱力学の法則を量子系・量子情報理論の枠組みで再定式化する分野。量子カルノーサイクル・量子熱機関の効率限界・ランダウアーの原理（情報消去と熱）・量子ゆらぎ定理が主要概念。情報と熱力学の関係の量子的拡張。",
        "impact_summary": "量子コンピュータの熱散逸問題・量子電池・ナノスケール熱機関の設計に直接関わる。マクスウェルの悪魔問題の量子的解決・情報の物理学への貢献が哲学的にも重要。",
        "subfield": "物理学",
        "school_of_thought": "統計力学",
        "era_start": 2000,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/nphys3169",
        "data_completeness": 82
    },
    {
        "name_ja": "流体力学・乱流",
        "name_en": "Fluid Dynamics and Turbulence",
        "definition": "レイノルズ数Re>4000で流れが乱流に遷移する（1883年）。コルモゴロフ（1941年）のK41理論がエネルギーカスケード・5/3乗スペクトル則を予測。直接数値シミュレーション（DNS）・大渦シミュレーション（LES）・RANS方程式が工学的手法。",
        "impact_summary": "航空機・船舶・風力発電・血流・大気海洋循環設計の中核物理。ナビエ＝ストークス方程式の滑らかさはミレニアム問題であり、乱流の完全理解は未解決のまま現代物理の最前線問題の一つ。",
        "subfield": "物理学",
        "school_of_thought": "流体物理学",
        "era_start": 1883,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-fluid-010816-060322",
        "mathematical_formulation": r"E(k) \propto k^{-5/3}",
        "data_completeness": 88
    },
    {
        "name_ja": "アインシュタインの奇跡の年（1905年）",
        "name_en": "Einstein's Annus Mirabilis 1905",
        "definition": "1905年にアルベルト・アインシュタインが5本の独立した革命的論文を発表した年。光電効果（光量子仮説→光子概念→量子論の転換点）・ブラウン運動（原子論の確立）・特殊相対性理論・質量エネルギー等価（E=mc²）が含まれ、いずれも物理学を根底から変えた。",
        "impact_summary": "20世紀物理学の出発点。光電効果論文でノーベル賞（1921年）。相対性理論とE=mc²はGPS補正・核エネルギー・宇宙論の数学的基盤。史上最も生産的な単年論文群として科学史上の転換点。",
        "subfield": "物理学",
        "school_of_thought": "科学史",
        "era_start": 1905,
        "culture_region": "Europe_Western",
        "source_url": "https://www.aip.org/history-programs/niels-bohr-library/oral-histories",
        "mathematical_formulation": r"E = mc^2",
        "data_completeness": 92
    },
    {
        "name_ja": "強磁場物理学とランダウ準位",
        "name_en": "High-Magnetic-Field Physics and Landau Levels",
        "definition": "強磁場下の二次元電子ガスはランダウ準位（離散化されたエネルギー準位）に量子化される。量子ホール効果（クリッツィング1980年）・分数量子ホール効果（ツイ・ストーマー・ゴサード1982年）・アハロノフ＝ボーム効果が代表的現象。",
        "impact_summary": "電気抵抗の精密標準（フォン・クリッツィング定数RK）としてSI単位系に組み込まれた。分数量子ホール効果の複合フェルミオン理論・アニオン統計・位相量子コンピュータの候補エンタングルメント源。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1980,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nobelprize.org/prizes/physics/1985/klitzing/facts/",
        "mathematical_formulation": r"E_n = \hbar\omega_c\left(n + \frac{1}{2}\right), \quad \omega_c = \frac{eB}{m^*}",
        "data_completeness": 88
    },
    {
        "name_ja": "インド・パキスタン核物理学と開発途上国の物理学",
        "name_en": "Nuclear Physics in South Asia: Salam, Bhabha, and Development",
        "definition": "アブドゥス・サラム（パキスタン）は電弱統一理論でノーベル賞（1979年）を受賞した初のイスラム教徒科学者。ホミ・バーバ（インド）はTIFR（タタ基礎科学研究所）を設立しインド核科学プログラムを創設。南アジアの物理学制度化の先駆者。",
        "impact_summary": "途上国からの素粒子物理学への貢献の最高事例。ICTPの設立（サラム1964年）は途上国の科学者教育の国際的拠点となり、科学の南北協力モデルとして現在も機能する。",
        "subfield": "物理学",
        "school_of_thought": "科学史",
        "era_start": 1956,
        "culture_region": "South_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/1979/salam/facts/",
        "data_completeness": 83
    },
    {
        "name_ja": "中国の現代物理学と杨振宁",
        "name_en": "Chinese Modern Physics: Yang-Mills and CNS",
        "definition": "楊振寧（チェンニン・ヤン）とリー・ミルズ（1954年）は非アーベルゲージ場理論（ヤン＝ミルズ理論）を確立し、標準模型の数学的基盤を与えた。楊と李政道は弱い相互作用でのパリティ対称性の破れを予言（1956年、ノーベル賞1957年）した。",
        "impact_summary": "ヤン＝ミルズ理論はQCD・電弱統一理論・大統一理論の数学的言語となった。中国系科学者による素粒子物理学への決定的貢献として、現代物理学の多文化的起源を示す。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1954,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/1957/press-release/",
        "mathematical_formulation": r"F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c",
        "data_completeness": 87
    },
    {
        "name_ja": "光子エンジン・レーザートラップと光ピンセット",
        "name_en": "Laser Trapping and Optical Tweezers",
        "definition": "アーサー・アシュキン（1986年）が集光レーザーで誘電体粒子・生きた細菌を光だけで把持・操作できる光ピンセットを実現（ノーベル物理学賞2018年）。熱揺らぎとの闘いでフェムトニュートン級の力を測定し、分子モーター・DNA・タンパク質の一分子物理学が解明された。",
        "impact_summary": "生物物理学における一分子実験の革命。筋肉ミオシン・RNA polymerase・DNA伸長の力-変位曲線が直接測定され、細胞機械の仕組みが原子レベルで解明された。",
        "subfield": "物理学",
        "school_of_thought": "生物物理学",
        "era_start": 1986,
        "culture_region": "North_America",
        "source_url": "https://www.nobelprize.org/prizes/physics/2018/ashkin/facts/",
        "data_completeness": 88
    },
    {
        "name_ja": "熱電効果とエネルギー変換",
        "name_en": "Thermoelectric Effect and Energy Conversion",
        "definition": "ゼーベック効果（温度差→電圧, 1821年）・ペルティエ効果（電流→冷却, 1834年）・トムソン効果が熱電効果の三形態。性能指数ZT = S²σT/κが熱電材料の効率指標。Bi₂Te₃が商用材料の標準。廃熱回収・半導体冷却素子に利用。",
        "impact_summary": "廃熱の電力変換（自動車排熱・宇宙探査機RTG・ウェアラブルデバイス）の物理的基盤。ZT>3の高効率熱電材料探索が材料科学の活発な研究分野。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1821,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/nmat2090",
        "mathematical_formulation": r"ZT = \frac{S^2 \sigma T}{\kappa}",
        "data_completeness": 85
    },
    {
        "name_ja": "核磁気と電子スピン共鳴（ESR）",
        "name_en": "Electron Spin Resonance (ESR) Spectroscopy",
        "definition": "不対電子をもつ常磁性種（ラジカル・遷移金属錯体）が外部磁場中で電磁波と共鳴する現象を利用した分光法。ザボイスキー（1944年）が発見。活性酸素種・光合成中間体・触媒活性点の検出に用いられる。",
        "impact_summary": "生物フリーラジカルの生体内検出・電池劣化機構解析・磁性材料評価の不可欠ツール。NMR・ESRの組み合わせが有機・無機化学の構造決定に革命的情報を提供した。",
        "subfield": "物理学",
        "school_of_thought": "原子分子物理学",
        "era_start": 1944,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.rsc.org/publishing/journals/pccp/",
        "mathematical_formulation": r"h\nu = g\mu_B B",
        "data_completeness": 83
    },
    {
        "name_ja": "電弱相転移と宇宙バリオン数生成",
        "name_en": "Electroweak Phase Transition and Baryogenesis",
        "definition": "ビッグバン後10^-12秒頃、電弱対称性が自発的に破れ（ヒッグス機構）、W±・Zボソンが質量を獲得した。サハロフの条件（バリオン数非保存・C/CP対称性の破れ・非平衡過程）を満たせば物質‐反物質非対称性が生まれる。",
        "impact_summary": "宇宙が反物質でなく物質優勢である理由の説明候補。ヒッグス粒子発見（2012年LHC）後も標準模型のCP破れは観測宇宙バリオン数を説明するには不十分で、新物理の存在を示唆する。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1967,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.nature.com/articles/nphys2397",
        "data_completeness": 83
    },
    {
        "name_ja": "強相関電子系と重フェルミオン",
        "name_en": "Strongly Correlated Electron Systems and Heavy Fermions",
        "definition": "電子間クーロン斥力がバンド幅を超える固体（モット絶縁体・重フェルミオン金属・高温超伝導体）では電子相関が支配的で、独立電子描像が破綻する。局在f電子・近藤効果・量子臨界点・奇異金属相が特徴的現象。",
        "impact_summary": "高温超伝導・近藤絶縁体・量子スピン液体・重い電子系の理論的理解に不可欠。量子コンピュータ用トポロジカル超伝導体の探索と結びつく現代物性物理学の最前線。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1964,
        "culture_region": "Global",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-conmatphys-031119-050558",
        "data_completeness": 82
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n = insert_batch(conn, CONCEPTS)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"Batch11 physics3: {n} inserted. Total: {count}")
