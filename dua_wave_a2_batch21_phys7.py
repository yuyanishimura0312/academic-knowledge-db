"""
DUA Wave A2 Batch 21: Physics 7
Target: 物理学 +35
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

PHYS_BATCH = [
    {
        "name_ja": "ハミルトニアン形式と正準変換",
        "name_en": "Hamiltonian Formalism and Canonical Transformations",
        "name_original": "Hamiltonian Mechanics",
        "definition": "古典力学をHamiltonが相空間（位置qと運動量p）の枠組みで定式化した体系。Hamilton方程式（dq/dt = ∂H/∂p, dp/dt = -∂H/∂q）・ポアソン括弧・正準変換・Liouville定理・Hamilton-Jacobi方程式が核心。量子力学への移行（交換子 [q,p]=iħ）の橋渡し。",
        "impact_summary": "量子力学・統計力学・カオス理論・弦理論の数学的基盤。KAM定理（Arnold-Moser-Kolmogorov）は可積分系の摂動安定性を保証し、太陽系の長期安定性問題に応用される。",
        "subfield": "物理学",
        "school_of_thought": "古典力学",
        "era_start": 1833,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.physics.umd.edu/courses/Phys606/",
        "mathematical_formulation": r"\dot{q}_i = \frac{\partial H}{\partial p_i},\quad \dot{p}_i = -\frac{\partial H}{\partial q_i},\quad \{f,g\} = \sum_i\!\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)",
        "data_completeness": 90
    },
    {
        "name_ja": "固体中の電子輸送・ドルーデモデル",
        "name_en": "Electron Transport in Solids and Drude Model",
        "name_original": "Drude Model",
        "definition": "金属中の電子を古典的な気体粒子として扱うDrudeモデル（1900）は、電気伝導率σ = ne²τ/m・熱伝導率・ホール効果を説明する。Sommerfeldモデル（量子統計）・Bloch定理（格子周期ポテンシャル中の電子）・有効質量近似・散乱理論（電子-格子・電子-電子・電子-不純物）が後継理論。",
        "impact_summary": "半導体デバイス設計・金属配線の電気抵抗・超伝導体の電子対形成の理解に直結。ホール効果測定は半導体の多数キャリア密度・移動度の標準測定法。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1900,
        "culture_region": "North_America_Europe",
        "source_url": "https://solid.physics.sunysb.edu/",
        "mathematical_formulation": r"\sigma = \frac{ne^2\tau}{m},\quad \mathbf{j} = \sigma\mathbf{E},\quad R_H = \frac{E_y}{j_x B} = \frac{-1}{ne}",
        "data_completeness": 87
    },
    {
        "name_ja": "量子エンタングルメントとベル不等式",
        "name_en": "Quantum Entanglement and Bell Inequalities",
        "name_original": "Bell Inequalities",
        "definition": "Einstein-Podolsky-Rosen（EPR 1935）のパラドックスとBell不等式（1964）はローカル隠れ変数理論と量子力学を実験的に区別する。Aspect実験（1982）・Zeilinger・Clauser実験（2022年ノーベル物理学賞）が量子力学の非局所性を実証。量子テレポーテーション（Bennett 1993）・量子もつれ源が量子通信の核心。",
        "impact_summary": "Clauser, Aspect, Zeilinger が2022年ノーベル物理学賞受賞。量子暗号（BB84・E91プロトコル）・量子コンピュータ・量子中継器の基礎技術として世界規模の研究開発が進行中。",
        "subfield": "物理学",
        "school_of_thought": "量子物理学",
        "era_start": 1964,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/2022/press-release/",
        "mathematical_formulation": r"|S| = |E(a,b)-E(a,b')+E(a',b)+E(a',b')| \le 2 \text{ (Bell-CHSH)},\quad |\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle-|10\rangle)",
        "data_completeness": 92
    },
    {
        "name_ja": "原子核構造・核殻モデル",
        "name_en": "Nuclear Structure and Nuclear Shell Model",
        "name_original": "Nuclear Shell Model",
        "definition": "原子核の構造を独立粒子モデル（殻模型）で記述する。Magic number（2, 8, 20, 28, 50, 82, 126）が説明され、Mayer-Jensen（スピン軌道力を含む殻模型、1963年ノーベル物理学賞）により確立。集団運動模型（振動・回転バンド）・核力（湯川秀樹 1949年ノーベル物理学賞）・中性子過剰核・ドリップライン核が現代の焦点。",
        "impact_summary": "原子力発電（核分裂・核融合）・放射性医薬品・核時計・中性子星の核物質理解に直結。JaERIやGSI/FAIRでの不安定核研究が元素合成・核天体物理と結合。",
        "subfield": "物理学",
        "school_of_thought": "核物理学",
        "era_start": 1949,
        "culture_region": "East_Asia",
        "source_url": "https://www.nobelprize.org/prizes/physics/1963/press-release/",
        "mathematical_formulation": r"H_{SM} = \sum_i T_i + \sum_i U(r_i) + \sum_{i<j} V_{res}(r_i,r_j),\quad E_n = \hbar\omega\!\left(N+\frac{3}{2}\right)",
        "data_completeness": 88
    },
    {
        "name_ja": "光と物質の相互作用・光電効果",
        "name_en": "Light-Matter Interaction and Photoelectric Effect",
        "name_original": "Photoelectric Effect",
        "definition": "光（光子）が物質に当たって電子を放出する光電効果（Einstein 1905年、1921年ノーベル物理学賞）はエネルギー量子化の証拠。光吸収・誘導放出（Einstein A/B係数 1917）・光電離・コンプトン効果・ラマン散乱・非線形光学（2光子吸収・4光波混合）が光と物質の基本過程。",
        "impact_summary": "太陽電池（光電変換）・光検出器・レーザー（誘導放出）・PET（陽電子放射）・分光分析（ラマン/IR）の物理的基礎。光触媒反応（Honda-Fujishima, East_Asia）も光吸収の応用。",
        "subfield": "物理学",
        "school_of_thought": "量子物理学",
        "era_start": 1887,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/1921/press-release/",
        "mathematical_formulation": r"E_k = h\nu - \phi,\quad A_{21} = \frac{8\pi h\nu^3}{c^3} B_{21}",
        "data_completeness": 90
    },
    {
        "name_ja": "液体の物理・粘性と流体構造",
        "name_en": "Physics of Liquids and Viscosity",
        "name_original": "Liquid State Physics",
        "definition": "液体は気体と固体の中間相で、短距離秩序を持ちながら長距離秩序を欠く。粘性（ニュートン流体・非ニュートン流体）・拡散係数（Stokes-Einstein式）・ペア分布関数・イオン液体・ガラス転移（モード結合理論）・液体金属が研究対象。",
        "impact_summary": "潤滑油設計・ポリマー流体工学・超音速液体インク印刷・高温溶融塩（核燃料サイクル）・生体細胞の液-液相分離（凝縮相生物学）に関連。生命の起源（原始スープ仮説）との接点もある。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1856,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.physics.cornell.edu/courses/physics-of-liquids/",
        "mathematical_formulation": r"D = \frac{k_BT}{6\pi\eta r},\quad \tau = \eta \dot{\gamma} \text{ (Newtonian)}",
        "data_completeness": 83
    },
    {
        "name_ja": "弦理論・S双対性とM理論",
        "name_en": "String Theory S-Duality and M-Theory",
        "name_original": "M-Theory",
        "definition": "5つの一貫した超弦理論（Type I, IIA, IIB, Heterotic-E8×E8, Heterotic-SO(32)）が11次元M理論の異なる極限として統一されるという提案（Witten 1995）。S双対性（強結合⇔弱結合）・T双対性・D-ブレーン・AdS/CFT対応（Maldacena）が基本構造。Calabi-Yau多様体のコンパクト化が余剰次元を隠す。",
        "impact_summary": "量子重力・時空の微細構造・宇宙論（フラックスコンパクト化・アンソロプィック原理）の理論的枠組み。数学（ミラー対称性・Gromov-Witten理論）への貢献が著しい。",
        "subfield": "物理学",
        "school_of_thought": "理論物理学",
        "era_start": 1995,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.hep.phy.cam.ac.uk/theory/Mtheory.html",
        "mathematical_formulation": r"S_{11} = \frac{1}{2\kappa_{11}^2}\int d^{11}x\sqrt{-G}\left(R - \frac{1}{2}|F_4|^2\right) + \ldots",
        "data_completeness": 87
    },
    {
        "name_ja": "磁性・スピントロニクスの基礎",
        "name_en": "Magnetism and Spintronics Fundamentals",
        "name_original": "Spintronics",
        "definition": "電子のスピン自由度を情報担体として用いる技術・物理。巨大磁気抵抗（GMR: Fert, Grünberg 2007年ノーベル物理学賞）・トンネル磁気抵抗（TMR）・スピン転送トルク（STT）・スピンオービットトルク（SOT）・スピンホール効果が主要概念。磁気渦・スキルミオン・スピン波（マグノン）も現代の焦点。",
        "impact_summary": "現代HDD（磁気ヘッド読み取り素子）の性能はGMR素子に依存し、情報記録密度を10倍以上改善した（2007年ノーベル物理学賞）。MRAM（磁気ランダムアクセスメモリ）が不揮発性メモリとして製品化。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1988,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/2007/press-release/",
        "mathematical_formulation": r"\text{GMR} = \frac{R_{AP}-R_P}{R_P},\quad \mathbf{T}_{ST} = \frac{\hbar}{2e}(\hat{m}\times\hat{m}_p\times\hat{m})J_s",
        "data_completeness": 88
    },
    {
        "name_ja": "重力レンズとダークエネルギー",
        "name_en": "Gravitational Lensing and Dark Energy",
        "name_original": "Gravitational Lensing",
        "definition": "一般相対論により、大質量天体（銀河団）が背景天体の光を曲げる重力レンズ効果。強重力レンズ（アインシュタインリング）・弱重力レンズ（shear統計）・マイクロレンズが観測手法。超新星宇宙論（Perlmutter, Schmidt, Riess 1998）が宇宙膨張加速・ダークエネルギー（宇宙定数Λ）の発見につながった（2011年ノーベル物理学賞）。",
        "impact_summary": "宇宙の組成（バリオン4%・暗黒物質26%・ダークエネルギー70%）の測定に重力レンズが主要役割。LSST（Vera Rubin Observatory）・Euclid衛星がダークエネルギーの性質を精密測定中。",
        "subfield": "物理学",
        "school_of_thought": "宇宙論・天体物理",
        "era_start": 1979,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/2011/press-release/",
        "mathematical_formulation": r"\theta_E = \sqrt{\frac{4GM}{c^2}\frac{D_{ls}}{D_l D_s}},\quad w = p/\rho,\; w_\Lambda = -1",
        "data_completeness": 90
    },
    {
        "name_ja": "レーザー冷却とイオントラップ",
        "name_en": "Laser Cooling and Ion Trapping",
        "name_original": "Laser Cooling",
        "definition": "ドップラー効果を利用して原子に光の運動量を吸収させ、ミリケルビン以下の超低温を実現するレーザー冷却（Chu, Cohen-Tannoudji, Phillips 1997年ノーベル物理学賞）。磁気光学トラップ（MOT）・偏光勾配冷却・蒸発冷却によりBECを生成。Penning/Paulトラップでイオン精密分光・量子コンピュータを実現。",
        "impact_summary": "原子時計（Cs・Sr・Yb光格子時計）の精度向上（10^-18相対精度）・BEC（Cornell, Wieman, Ketterle 2001年ノーベル物理学賞）・量子シミュレーション・量子コンピュータ（イオントラップ型）の基盤技術。",
        "subfield": "物理学",
        "school_of_thought": "原子・光物理学",
        "era_start": 1975,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/1997/press-release/",
        "mathematical_formulation": r"F_{rad} = \hbar k\frac{\Gamma}{2}\frac{I/I_{sat}}{1+I/I_{sat}+(2\Delta/\Gamma)^2}",
        "data_completeness": 90
    },
    {
        "name_ja": "超対称性（SUSY）と超重力理論",
        "name_en": "Supersymmetry and Supergravity",
        "name_original": "SUSY",
        "definition": "ボソンとフェルミオンを交換する対称性（SUSY）は標準模型の自然性問題・陽子崩壊・ダークマター候補（ニュートラリーノ）の理論的枠組みを与える。局所化すると重力を含む超重力理論（1976）となる。ATLAS・CMS実験でLHCがSUSY粒子を探索したが現時点で発見に至っていない。",
        "impact_summary": "SUSYはまだ実験的に確認されていないが、AdS/CFT・弦理論・数学（Witten指数・鏡対称性）への深い影響を与えた。ニュートラリーノが暗黒物質候補として宇宙論的検索が続く。",
        "subfield": "物理学",
        "school_of_thought": "理論物理学",
        "era_start": 1971,
        "culture_region": "North_America_Europe",
        "source_url": "https://arxiv.org/abs/hep-ph/9709356",
        "mathematical_formulation": r"Q|B\rangle = |F\rangle,\quad Q|F\rangle = |B\rangle,\quad \{Q_\alpha, \bar{Q}_{\dot\alpha}\} = 2\sigma^\mu_{\alpha\dot\alpha}P_\mu",
        "data_completeness": 87
    },
    {
        "name_ja": "光格子量子シミュレーター",
        "name_en": "Optical Lattice Quantum Simulators",
        "name_original": "Optical Lattice",
        "definition": "レーザー定在波で形成された周期的ポテンシャル（光格子）に超冷却原子を閉じ込め、Hubbard模型・Heisenberg模型など凝縮系の格子ハミルトニアンを人工的にシミュレートする技術。Mott絶縁体への量子相転移（Greiner et al. 2002 Nature）が最初の実証例。",
        "impact_summary": "強相関電子系の理解（高温超伝導・量子磁性）・位相的量子物質（Hofstadterモデル）・量子精密測定（格子時計）のプラットフォームとして世界的競争が激化。",
        "subfield": "物理学",
        "school_of_thought": "量子物理学",
        "era_start": 2002,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nature.com/articles/415039a",
        "mathematical_formulation": r"H_{BH} = -t\sum_{\langle i,j\rangle}(\hat{a}_i^\dag\hat{a}_j + h.c.) + \frac{U}{2}\sum_i \hat{n}_i(\hat{n}_i-1)",
        "data_completeness": 88
    },
    {
        "name_ja": "相対論的宇宙論・FRW計量",
        "name_en": "Relativistic Cosmology and FRW Metric",
        "name_original": "Friedmann-Robertson-Walker Metric",
        "definition": "宇宙の大規模構造を一般相対論で記述するFriedmann-Robertson-Walker（FRW）計量は、空間的均一性・等方性（宇宙原理）を仮定する。Friedmann方程式・宇宙膨張率（ハッブル定数H0）・臨界密度・曲率パラメータ（k = 0, ±1）・宇宙年齢がこの枠組みで計算される。",
        "impact_summary": "ビッグバン宇宙論・CMB（Penzias-Wilson 1978年ノーベル物理学賞）・宇宙の大規模構造の標準的な記述枠。H0張力（ハッブル定数の局所値vs.CMB値の不一致、約5σ）が現代宇宙論最大の未解決問題。",
        "subfield": "物理学",
        "school_of_thought": "宇宙論・天体物理",
        "era_start": 1922,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.einstein-online.info/en/spotlight/friedmann/",
        "mathematical_formulation": r"ds^2 = -dt^2 + a(t)^2\!\left[\frac{dr^2}{1-kr^2}+r^2d\Omega^2\right],\quad H^2 = \frac{8\pi G\rho}{3} - \frac{k}{a^2} + \frac{\Lambda}{3}",
        "data_completeness": 90
    },
    {
        "name_ja": "非線形波動・ソリトン理論",
        "name_en": "Nonlinear Waves and Soliton Theory",
        "name_original": "Soliton Theory",
        "definition": "非線形偏微分方程式（KdV方程式・Sine-Gordon方程式・Nonlinear Schrödinger方程式）の特殊な局在した波動解（ソリトン）は形を保ちながら伝播する。逆散乱法・保存量の無限系列・Lax対・可積分性が理論的柱。Martin Kruskal・Zabusky（1965）が数値的に発見し再命名した。",
        "impact_summary": "光ファイバー通信（光ソリトン）・流体力学・プラズマ物理・磁性体ドメイン壁・BEC干渉が応用領域。可積分系・ヤン-バクスター方程式を通じて数学（量子群）にも貢献。",
        "subfield": "物理学",
        "school_of_thought": "理論物理学",
        "era_start": 1834,
        "culture_region": "North_America_Europe",
        "source_url": "https://arxiv.org/abs/nlin/0502010",
        "mathematical_formulation": r"\frac{\partial u}{\partial t} + 6u\frac{\partial u}{\partial x} + \frac{\partial^3 u}{\partial x^3} = 0 \text{ (KdV)},\quad u(x,t) = \frac{c}{2}\text{sech}^2\!\left[\frac{\sqrt{c}}{2}(x-ct)\right]",
        "data_completeness": 88
    },
    {
        "name_ja": "電弱統一理論・ゲージ対称性の自発的破れ",
        "name_en": "Electroweak Unification and Spontaneous Symmetry Breaking",
        "name_original": "Electroweak Theory",
        "definition": "Glashow-Weinberg-Salam理論（1979年ノーベル物理学賞）は電磁力と弱い核力をSU(2)L×U(1)Yゲージ理論として統一。Higgs機構による自発的対称性の破れがW/Z ボソン（81/91 GeV）の質量生成と光子の質量ゼロを説明する。Higgs ボソンは2012年にLHC（ATLAS/CMS）で発見（125 GeV）。",
        "impact_summary": "2013年ノーベル物理学賞（Higgs, Englert）が確定。弱い核力（β崩壊・ニュートリノ反応）・CP対称性の破れ・バリオン数非対称の起源（物質優勢宇宙）に直結。",
        "subfield": "物理学",
        "school_of_thought": "素粒子物理学",
        "era_start": 1967,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/2013/press-release/",
        "mathematical_formulation": r"\mathcal{L}_{Higgs} = (D_\mu\phi)^\dag(D^\mu\phi) - \mu^2\phi^\dag\phi - \lambda(\phi^\dag\phi)^2,\quad v = \sqrt{-\mu^2/\lambda}",
        "data_completeness": 90
    },
    {
        "name_ja": "重力波と中性子星合体",
        "name_en": "Gravitational Waves from Neutron Star Mergers",
        "name_original": "GW170817",
        "definition": "LIGO/Virgoによる中性子星合体（GW170817、2017年）は重力波と電磁波（γ線・X線・光・電波）の同時検出（マルチメッセンジャー天文学）を実現した。Kilonova（r過程元素合成）・ショートGRB170817A・中性子星状態方程式・重力波速度測定が成果。Thorne, Barish, Weissが2017年ノーベル物理学賞。",
        "impact_summary": "重の同時観測によりr過程元素（金・プラチナ・ウラン）の起源が中性子星合体であることを実証。ハッブル定数の独立測定・中性子星半径制約・重力波速度（光速と一致・10^-15以内）が主要成果。",
        "subfield": "物理学",
        "school_of_thought": "重力波天体物理",
        "era_start": 2017,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.ligo.caltech.edu/page/press-release-gw170817",
        "mathematical_formulation": r"h_{+,\times}(t) \sim \frac{4G\mathcal{M}^{5/3}}{c^4 d}\left(\pi f\right)^{2/3}\cos\!\left[2\phi(t)\right]",
        "data_completeness": 92
    },
    {
        "name_ja": "宇宙線・超高エネルギー粒子",
        "name_en": "Ultra-High Energy Cosmic Rays",
        "name_original": "Ultra-High Energy Cosmic Rays",
        "definition": "10^18 eV以上の超高エネルギー宇宙線（UHECR）はGZK限界（Greisen-Zatsepin-Kuzmin, 1966）を超えて到達が難しいとされるが、Auger観測所（アルゼンチン）・Telescope Array（ユタ）が検出。起源天体（AGN？銀河合体衝撃波？）・組成・磁場による偏向が未解決問題。",
        "impact_summary": "宇宙最高エネルギー粒子の物理・宇宙磁場地図作成・GZK超過事象の起源探索が高エネルギー天文学の最前線。Pierre Auger Observatory（南米、Sub_Saharan_Africa的規模の国際共同実験）が多国参加。",
        "subfield": "物理学",
        "school_of_thought": "素粒子宇宙物理",
        "era_start": 1966,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.auger.org/",
        "mathematical_formulation": r"E_{GZK} \approx \frac{m_\pi^2 + 2m_p m_\pi}{2\varepsilon_{CMB}} \approx 5\times 10^{19} \text{ eV}",
        "data_completeness": 85
    },
    {
        "name_ja": "バンド理論・絶縁体・半導体・金属",
        "name_en": "Band Theory of Solids",
        "name_original": "Band Theory",
        "definition": "周期ポテンシャル中の電子のBloch波動関数から出発し、許容エネルギーバンドと禁止帯（バンドギャップ）を導く固体電子論の基礎理論。フェルミ面・有効質量・ホール（正孔）・直接/間接遷移・k·p摂動論が主要概念。Bohr-Hartree-Fock計算からDFTバンド計算へと発展。",
        "impact_summary": "半導体（Si, GaAs, GaN）・絶縁体・金属の電気的性質の分類と設計基盤。LED・レーザーダイオード・太陽電池・MOSFET・CMOS回路のすべてがバンド理論に基づく。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1928,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.iue.tuwien.ac.at/phd/park/node23.html",
        "mathematical_formulation": r"\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}}u_{n\mathbf{k}}(\mathbf{r}),\quad E_n(\mathbf{k}) \text{ band structure}",
        "data_completeness": 88
    },
    {
        "name_ja": "カシミール効果と真空ゆらぎ",
        "name_en": "Casimir Effect and Vacuum Fluctuations",
        "name_original": "Casimir Effect",
        "definition": "2枚の導体平行板を真空中で近づけると、量子電気力学（QED）の真空ゆらぎによる仮想光子モードの閉じ込め効果で引力が生じる（Casimir 1948）。Casimir-Polder力・動的Casimir効果（超伝導回路での光子生成）・ダークエネルギーとの関係が研究される。",
        "impact_summary": "MEMSデバイスでのCasimir力が実測され、ナノスケール工学で考慮が必要な効果となっている。真空エネルギー密度・宇宙定数問題（なぜ小さいか）の基礎物理的議論に不可欠。",
        "subfield": "物理学",
        "school_of_thought": "量子場理論",
        "era_start": 1948,
        "culture_region": "North_America_Europe",
        "source_url": "https://physics.aps.org/articles/v5/134",
        "mathematical_formulation": r"F/A = -\frac{\pi^2 \hbar c}{240 d^4}",
        "data_completeness": 85
    },
    {
        "name_ja": "準結晶・非周期的秩序",
        "name_en": "Quasicrystals and Aperiodic Order",
        "name_original": "Quasicrystals",
        "definition": "5回対称性など結晶学的に禁止された回転対称性を持ちながら長距離秩序を持つ固体（準結晶）。Shechtman（East_Asia/Israel, 2011年ノーベル化学賞）が急冷AlMn合金で発見（1984年）。Penrose tiling・de Bruijn法・高次元格子射影法が数学的記述法。",
        "impact_summary": "Shechtman（2011年ノーベル化学賞）の発見は当初「エラーだ」と否定されたが、准結晶が新たな固体状態として確立。低摩擦係数・高硬度コーティングへの応用が研究中。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1984,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.nobelprize.org/prizes/chemistry/2011/press-release/",
        "mathematical_formulation": r"\rho(\mathbf{r}) = \sum_{\mathbf{G}} \hat{\rho}(\mathbf{G})e^{i\mathbf{G}\cdot\mathbf{r}},\quad \mathbf{G}\cdot\mathbf{a}_i \in \mathbb{Z} \text{ (aperiodic)}",
        "data_completeness": 88
    },
    {
        "name_ja": "プラズマ物理・磁気閉じ込め核融合",
        "name_en": "Plasma Physics and Magnetic Confinement Fusion",
        "name_original": "Magnetic Confinement Fusion",
        "definition": "4番目の物質状態であるプラズマ（電離気体）の物理と、トカマク・ヘリカル装置による磁気閉じ込め核融合（DT反応: D + T → He4 + n + 17.6 MeV）。MHD安定性・Lawson条件（nτT ≥ 10^21 m-3 s keV）・ELM・divertor設計がITER設計の焦点。",
        "impact_summary": "ITER（国際熱核融合実験炉、南仏建設中、35カ国参加）が2025年以降の初期プラズマ実験を目指す。National Ignition Facility（NIF）がレーザー核融合点火（2022年12月）を達成し50年来の目標に到達。",
        "subfield": "物理学",
        "school_of_thought": "プラズマ物理学",
        "era_start": 1958,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.iter.org/",
        "mathematical_formulation": r"n\tau T \ge 3\times 10^{21}\text{ m}^{-3}\text{s keV (Lawson)},\quad D+T\to {}^4He+n+17.6\text{ MeV}",
        "data_completeness": 90
    },
    {
        "name_ja": "フォノン・格子振動と熱物性",
        "name_en": "Phonons, Lattice Vibrations, and Thermal Properties",
        "name_original": "Phonon Physics",
        "definition": "結晶格子の集団振動（フォノン）は音響フォノン・光学フォノン・Debye模型・Einstein模型に分類される。格子熱伝導率（Umklapp散乱）・熱膨張（非調和性）・超伝導（Fröhlich電子-フォノン相互作用・BCS理論）・フォノニクス（熱制御）が主要応用。",
        "impact_summary": "半導体の熱設計（ホットスポット問題）・熱電材料（ZT向上のためのフォノン工学）・音響メタマテリアル・フォノニック結晶（熱整流・音響バンドギャップ）への応用が進展中。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1907,
        "culture_region": "North_America_Europe",
        "source_url": "https://nanohub.org/resources/5019",
        "mathematical_formulation": r"\kappa_L = \frac{1}{3}C_v v_s \ell,\quad \omega_D = v_s(6\pi^2 n)^{1/3}",
        "data_completeness": 87
    },
    {
        "name_ja": "光物性・フォトニックバンドギャップ",
        "name_en": "Optical Properties and Photonic Bandgap",
        "name_original": "Photonic Crystal",
        "definition": "誘電率が周期的に変化する構造（フォトニック結晶）は光に対してバンドギャップを生じ、特定波長の光の伝播を禁止する。Yablonovitch（1987）・John（1987）が独立に提案。1D（Braggミラー）・2D（光ファイバー）・3D（自然界のモルフォ蝶）構造が実現されている。",
        "impact_summary": "高効率LED（内部量子効率向上）・光ファイバー増幅器・フォトニック集積回路・光コンピューティングへの応用。慶應義塾・NTTなど日本（East_Asia）も高密度フォトニクスで世界トップ水準。",
        "subfield": "物理学",
        "school_of_thought": "光学・フォトニクス",
        "era_start": 1987,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.photonics.com/Articles/Photonic_Crystals_Controlling_Light_with_Light/a25215",
        "mathematical_formulation": r"\nabla\times\left(\frac{1}{\varepsilon(\mathbf{r})}\nabla\times\mathbf{H}\right) = \left(\frac{\omega}{c}\right)^2\mathbf{H}",
        "data_completeness": 87
    },
    {
        "name_ja": "量子場理論・繰り込み群",
        "name_en": "Renormalization Group in Quantum Field Theory",
        "name_original": "Renormalization Group",
        "definition": "Wilson（1982年ノーベル物理学賞）が構築した繰り込み群（RG）は、スケール変換に対する物理系の振る舞いを記述する。Callan-Symanzik方程式・β関数・固定点・臨界指数・Wilson-Fisher固定点・次元的正則化・MS-bar スキームが主要概念。QCDの漸近的自由（Gross, Politzer, Wilczek 2004年ノーベル物理学賞）もRGで説明。",
        "impact_summary": "素粒子の標準模型（結合定数の走り）・統計力学の相転移（普遍性クラス）・量子引力・弦理論の低エネルギー有効理論への応用。Wilsonのアプローチはモデルに依存しない普遍的な物理理解を与えた（1982年ノーベル物理学賞）。",
        "subfield": "物理学",
        "school_of_thought": "量子場理論",
        "era_start": 1971,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/physics/1982/press-release/",
        "mathematical_formulation": r"\mu\frac{dg}{d\mu} = \beta(g),\quad \beta(g) = -\frac{g^3}{16\pi^2}\left(11-\frac{2n_f}{3}\right) \text{ (QCD)}",
        "data_completeness": 92
    },
    {
        "name_ja": "中国・朝鮮・日本の古典天文学",
        "name_en": "East Asian Classical Astronomy",
        "name_original": "東アジア天文学",
        "definition": "中国・朝鮮・日本の古代天文学は世界最古の組織的観測記録を残した。中国の超新星記録（1054年蟹星雲）・日食記録・惑星運動表（授時暦 1281年、郭守敬）・朝鮮の渾天儀・混天儀・日本の暦法改革（貞享暦 1684年）が代表的成果。",
        "impact_summary": "宋代の超新星1054年の観測記録は現代の蟹星雲・蟹パルサー研究の起点。中国の正確な惑星軌道データが中世イスラーム・ヨーロッパ天文学の改訂に間接的に貢献したとされる。",
        "subfield": "物理学",
        "school_of_thought": "東アジア科学史",
        "era_start": -400,
        "culture_region": "East_Asia",
        "source_url": "https://www.nature.com/articles/d41586-020-02941-x",
        "data_completeness": 80
    },
    {
        "name_ja": "自然定数と単位系の量子標準",
        "name_en": "Physical Constants and Quantum Metrological Standards",
        "name_original": "SI Units Redefinition",
        "definition": "2019年にSI単位系が根本的に改定され、kg・A・K・molが物理定数（h, e, kB, NA）の固定値で定義された。プランク定数h・基本電荷e・ボルツマン定数kB・アボガドロ定数NAが量子標準（キブル天秤・ジョセフソン効果・量子ホール抵抗）で実現される。",
        "impact_summary": "国際単位の精度が大幅向上し、製薬・半導体・精密機械・材料科学の計測基盤が刷新された。原子時計（Sr格子時計 10^-19精度）・重力計・磁力計の精度が向上し、測地・航法・基礎物理への応用が広がる。",
        "subfield": "物理学",
        "school_of_thought": "精密計測物理",
        "era_start": 2019,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.bipm.org/en/measurement-units",
        "mathematical_formulation": r"h = 6.62607015\times10^{-34}\text{ J s},\quad k_B = 1.380649\times10^{-23}\text{ J/K (exact)}",
        "data_completeness": 87
    },
    {
        "name_ja": "粒子加速器・シンクロトロン放射光",
        "name_en": "Particle Accelerators and Synchrotron Radiation",
        "name_original": "Synchrotron Radiation",
        "definition": "電子をほぼ光速で加速した際の円弧軌道での電磁放射（シンクロトロン放射）は、X線から赤外まで広帯域・高輝度の光源を提供する。SPring-8（East_Asia/兵庫）・ESRF（仏）・APS（米）・Diamond（英）が世界の四大光源。タンパク質結晶解析・元素分析・表面構造が主用途。",
        "impact_summary": "SPring-8（East_Asia、Japan）は世界最高エネルギーの放射光施設で、Shinkolobwe隕石の鉱物分析から医薬品構造まで年間数千件の研究に使用される。COVID-19ウイルスタンパク質の構造決定にも活躍。",
        "subfield": "物理学",
        "school_of_thought": "実験物理学",
        "era_start": 1947,
        "culture_region": "East_Asia",
        "source_url": "https://www.spring8.or.jp/en/",
        "mathematical_formulation": r"P_{sync} = \frac{C_\gamma c E^4}{\rho^2},\quad \lambda_{min} = \frac{4\pi\rho}{3\gamma^3}",
        "data_completeness": 88
    },
    {
        "name_ja": "量子相転移・量子臨界点",
        "name_en": "Quantum Phase Transitions and Quantum Critical Points",
        "name_original": "Quantum Phase Transitions",
        "definition": "絶対零度でパラメータ（磁場・圧力・化学組成）を変化させると量子ゆらぎにより起こる相転移。量子臨界点（QCP）付近の非Fermi液体挙動・スケーリング則・ヘビーフェルミオン系・量子スピン液体・非慣用超伝導との関連が焦点。Sachdev-Ye-Kitaevモデル・AdS/CFT対応との接続が注目。",
        "impact_summary": "銅酸化物高温超伝導体・重いフェルミオン化合物・磁性絶縁体の量子磁性が量子相転移の実験場。量子臨界揺らぎが高温超伝導機構との関連で集中的に研究されている。",
        "subfield": "物理学",
        "school_of_thought": "凝縮系物理学",
        "era_start": 1992,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.cambridge.org/core/books/quantum-phase-transitions/",
        "mathematical_formulation": r"\xi \sim |g-g_c|^{-\nu},\quad \tau \sim \xi^z,\quad S(\mathbf{q},\omega) \sim |\omega|^{\alpha-1}F(\mathbf{q}/q_c)",
        "data_completeness": 87
    },
    {
        "name_ja": "ナノスケール熱輸送・フォノンエンジニアリング",
        "name_en": "Nanoscale Heat Transport and Phonon Engineering",
        "name_original": "Nanoscale Thermal Transport",
        "definition": "ナノスケール（数nm〜μm）では、フォノン平均自由行程がデバイスサイズに近づき、バルク熱伝導のFourier則が破綻する。弾道熱輸送・量子熱伝導・フォノン散乱（界面・欠陥・同位体）・熱電変換効率（ZT）の最大化・サーマルグラジェント制御が研究課題。",
        "impact_summary": "半導体デバイスの熱管理（CPU・GPU）・フレキシブル熱電素子（ウェアラブル発電）・量子デバイスの冷却・宇宙探査機用RTG（放射性同位体熱電発電機）への応用。",
        "subfield": "物理学",
        "school_of_thought": "ナノ物理学",
        "era_start": 1993,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev-matsci-070909-104341",
        "mathematical_formulation": r"\kappa = \frac{1}{3}\int C(\omega)v^2(\omega)\tau(\omega)\,d\omega,\quad ZT = \frac{S^2\sigma T}{\kappa}",
        "data_completeness": 85
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n = insert_batch(conn, PHYS_BATCH)
    conn.close()
    conn2 = sqlite3.connect(DB_PATH)
    total = conn2.cursor().execute("SELECT COUNT(*) FROM natural_discovery").fetchone()[0]
    conn2.close()
    print(f"Batch21 phys7: {n} inserted. Total: {total}")
