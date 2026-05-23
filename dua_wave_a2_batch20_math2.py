"""
DUA Wave A2 Batch 20: Mathematics 2 + Statistics/Computation
Target: 数学 +25, 統計学・計算科学 +20 = ~45 insertions
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

MATH_BATCH1 = [
    {
        "name_ja": "代数幾何学",
        "name_en": "Algebraic Geometry",
        "name_original": "Algebraic Geometry",
        "definition": "多項式方程式の解集合（代数多様体）の幾何学的性質を研究する数学の一分野。Zariski位相・スキーム理論（Grothendieck）・層理論・コホモロジー（エタールコホモロジー）・モジュライ空間が主要概念。Weil予想（Deligne証明 1974年フィールズ賞）・Fermat最終定理（Wiles、楕円曲線・モジュラー曲線を使用）と深く関わる。",
        "impact_summary": "数論・表現論・弦理論・暗号理論の基礎。MirrorSymmetry（数理物理）・Monstrous Moonshine（Borcherds 1998年フィールズ賞）など学際的発展。",
        "subfield": "数学",
        "school_of_thought": "代数学",
        "era_start": 1900,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.math.columbia.edu/~chaoli/docs/AlgebraicGeometry.html",
        "mathematical_formulation": r"\text{Proj}(R), \quad H^i(X, \mathcal{F}), \quad \chi(X) = \sum_i (-1)^i \dim H^i(X, \mathcal{O}_X)",
        "data_completeness": 88
    },
    {
        "name_ja": "微分方程式の解析学",
        "name_en": "Analysis of Differential Equations",
        "name_original": "Differential Equations Analysis",
        "definition": "常微分方程式（ODE）と偏微分方程式（PDE）の解の存在・一意性・安定性・漸近挙動を扱う解析学の一分野。Cauchy-Kovalevskaya定理（解析的解の存在）・Sobolev空間・弱解・変分法・Lax-Milgram定理が基本ツール。Navier-Stokes方程式のClay Millennium問題、Ricci流（Perelman球面定理証明）が代表的難問。",
        "impact_summary": "流体力学・電磁気学・量子力学・熱伝導・弾性体理論の数学的基礎。Hamilton-Jacobiおよびオイラー-ラグランジュ方程式は制御理論・経路最適化の基盤。",
        "subfield": "数学",
        "school_of_thought": "解析学",
        "era_start": 1736,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.claymath.org/millennium-problems/navier-stokes-equation",
        "mathematical_formulation": r"\frac{\partial u}{\partial t} + (u\cdot\nabla)u = -\nabla p + \nu\Delta u,\quad \nabla\cdot u = 0",
        "data_completeness": 90
    },
    {
        "name_ja": "組合せ論",
        "name_en": "Combinatorics",
        "name_original": "Combinatorics",
        "definition": "有限または可算の離散構造（順列・組合せ・グラフ・ポリトープ・格子）の列挙・構造・最適化を扱う数学分野。Ramsey理論・Erdős問題・超グラフ彩色・Tutte多項式・生成関数・包除原理が主要トピック。Paul Erdős（ハンガリー出身）が20世紀最多の共著者として組合せ論を牽引。",
        "impact_summary": "暗号理論・アルゴリズム設計・コーディング理論・統計物理（Ising模型）の数学基盤。Zarankiewicz問題などが計算機科学の複雑性理論と深く連携。",
        "subfield": "数学",
        "school_of_thought": "離散数学",
        "era_start": 1202,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.mat.univie.ac.at/~slc/",
        "mathematical_formulation": r"\binom{n}{k} = \frac{n!}{k!(n-k)!}, \quad \sum_{k=0}^n \binom{n}{k}x^k = (1+x)^n",
        "data_completeness": 87
    },
    {
        "name_ja": "表現論",
        "name_en": "Representation Theory",
        "name_original": "Representation Theory",
        "definition": "抽象的な代数的構造（群・環・Lie代数）を線形写像として行列・ベクトル空間上で実現する理論。Frobenius指標理論・Schur-Weyl双対性・Langlands対応・量子群が主要発展。物理では素粒子の対称性（SU(2), SU(3), SU(5) GUT）・スペクトル理論との結合が深い。",
        "impact_summary": "粒子物理（標準模型のゲージ群）・量子力学（スピン表現）・数論（保型形式・Langlandsプログラム）を統合する中枢理論。Langlandsプログラムに関連し複数のフィールズ賞が授与されている。",
        "subfield": "数学",
        "school_of_thought": "代数学",
        "era_start": 1896,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.math.ias.edu/langlands",
        "mathematical_formulation": r"\rho: G \to GL(V),\quad \chi_\rho(g) = \text{tr}(\rho(g)),\quad \langle\chi_\rho,\chi_\sigma\rangle = \delta_{\rho\sigma}",
        "data_completeness": 88
    },
    {
        "name_ja": "数値解析・有限要素法",
        "name_en": "Numerical Analysis and Finite Element Method",
        "name_original": "Finite Element Method",
        "definition": "連続問題を離散化して計算機で解く数値解析の中核手法。有限要素法（FEM）は偏微分方程式を弱形式に変換しメッシュ要素で近似する。有限差分法・有限体積法・境界要素法・分光要素法も主要手法。誤差解析（Lax等価定理・Cea補題）・条件数・前処理法が理論基盤。",
        "impact_summary": "航空機設計・自動車衝突解析・建築構造・医療インプラント・地震解析・CFD（計算流体力学）に不可欠。ANSYS・ABAQUS・OpenFOAMが代表的商用・オープンソースパッケージ。",
        "subfield": "数学",
        "school_of_thought": "応用数学",
        "era_start": 1943,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.dealii.org/",
        "mathematical_formulation": r"a(u,v) = L(v) \;\forall v\in V,\quad u_h = \sum_j U_j \phi_j,\quad \mathbf{K}\mathbf{U} = \mathbf{F}",
        "data_completeness": 88
    },
    {
        "name_ja": "測度論・ルベーグ積分",
        "name_en": "Measure Theory and Lebesgue Integration",
        "name_original": "Lebesgue Integration",
        "definition": "Lebesgue（1902年）が構築した測度論的積分理論。Riemann積分で扱えない関数クラス（単調点列の極限等）も積分可能にし、L^p空間・確率論・フーリエ解析の厳密な基礎を与える。Borel集合族・σ-加法族・Radon-Nikodym定理・Fubini-Tonelli定理が核心定理。",
        "impact_summary": "現代確率論（Kolmogorov公理化）・統計力学・量子力学のHilbert空間論・信号処理のフーリエ解析すべてがLebesgue測度論上に構築されている。",
        "subfield": "数学",
        "school_of_thought": "解析学",
        "era_start": 1902,
        "culture_region": "North_America_Europe",
        "source_url": "https://mathworld.wolfram.com/LebesgueIntegral.html",
        "mathematical_formulation": r"\int f\,d\mu = \sup\left\{\int s\,d\mu : 0 \le s \le f,\, s \text{ simple}\right\}",
        "data_completeness": 88
    },
    {
        "name_ja": "整数論・解析的数論",
        "name_en": "Analytic Number Theory",
        "name_original": "Analytic Number Theory",
        "definition": "解析的手法（複素関数論・フーリエ解析）を用いて整数の性質を研究する数論の分野。Riemann ζ関数とリーマン予想・素数定理（π(x)〜x/ln x）・ディリクレL関数・円法・指数和・篩法（小野の篩等）が主要ツール。ゴールドバッハ予想・ twin prime予想も関連。",
        "impact_summary": "RSA暗号（大きな素数の乗積分解困難性）の数論的基礎。Ramanujan（South_Asia）のモック・シータ関数・分割数公式が現代数論に大きな影響を与えた。",
        "subfield": "数学",
        "school_of_thought": "数論",
        "era_start": 1859,
        "culture_region": "South_Asia",
        "source_url": "https://www.claymath.org/millennium-problems/riemann-hypothesis",
        "mathematical_formulation": r"\zeta(s) = \sum_{n=1}^\infty n^{-s} = \prod_p (1-p^{-s})^{-1},\quad \pi(x) \sim \frac{x}{\ln x}",
        "data_completeness": 90
    },
    {
        "name_ja": "確率過程・マルコフ連鎖",
        "name_en": "Stochastic Processes and Markov Chains",
        "name_original": "Markov Chains",
        "definition": "時間とともに確率的に変化する状態遷移を記述する数学的枠組み。マルコフ性（未来は現在のみに依存）を持つ離散・連続時間マルコフ連鎖・ポアソン過程・Brown運動（Wiener過程）・Itô確率積分・マルチンゲール理論が主要概念。",
        "impact_summary": "金融数学（オプション価格Black-Scholes・Itô公式）・統計物理（ボルツマン分布）・機械学習（マルコフ連鎖モンテカルロ: MCMC）・待ち行列理論・強化学習（Q-learning）の基盤理論。",
        "subfield": "数学",
        "school_of_thought": "確率論",
        "era_start": 1906,
        "culture_region": "Europe_Eastern",
        "source_url": "https://www.math.ucdavis.edu/~gravner/MAT135B/",
        "mathematical_formulation": r"P(X_{n+1}=j\mid X_n=i) = p_{ij},\quad \pi P = \pi,\quad dX_t = \mu\,dt + \sigma\,dW_t",
        "data_completeness": 90
    },
    {
        "name_ja": "関数解析・ヒルベルト空間",
        "name_en": "Functional Analysis and Hilbert Spaces",
        "name_original": "Functional Analysis",
        "definition": "無限次元ベクトル空間（バナッハ空間・ヒルベルト空間）上の線形作用素を扱う解析学。スペクトル定理・コンパクト作用素・ハーン-バナッハ定理・開写像定理・一様有界性原理（バナッハ-スタインハウス定理）が中心定理。量子力学の数学的基礎として von Neumann が整備。",
        "impact_summary": "量子力学（可観測量=自己共役作用素）・偏微分方程式（Sobolev空間）・信号処理（ウェーブレット）・統計的学習理論（RKHS・サポートベクターマシン）の理論的骨格。",
        "subfield": "数学",
        "school_of_thought": "解析学",
        "era_start": 1907,
        "culture_region": "North_America_Europe",
        "source_url": "https://mathworld.wolfram.com/HilbertSpace.html",
        "mathematical_formulation": r"\langle f,g\rangle = \int f\bar{g}\,d\mu,\quad \|f\|^2 = \langle f,f\rangle,\quad T^* = \text{adjoint}",
        "data_completeness": 90
    },
    {
        "name_ja": "インド数学・ラマヌジャンの無限級数",
        "name_en": "Indian Mathematics: Ramanujan's Series and Identities",
        "name_original": "श्रीनिवास रामानुजन",
        "definition": "Srinivasa Ramanujan（1887–1920）はインド独学の数学者で、タミル・ナードゥ州出身。mock theta函数・Ramanujan sum・Rogers-Ramanujan恒等式・タウ関数・高次合成数・円周率の急収束無限級数（後のChudnovskyアルゴリズムの起源）など数千の公式を発見した。Hardy-Ramanujan数（1729）も有名。",
        "impact_summary": "Ramanujanの直観的公式は20世紀以降に厳密証明が次々進み、保型形式・数論・組合せ論を革新した。1987年Chudnovsky公式（π計算の世界記録に使用）はRamanujanの公式の精緻化。",
        "subfield": "数学",
        "school_of_thought": "数論",
        "era_start": 1900,
        "culture_region": "South_Asia",
        "source_url": "https://www.math.rutgers.edu/~zeilberg/ramanujan.html",
        "mathematical_formulation": r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^\infty \frac{(4k)!(1103+26390k)}{(k!)^4 396^{4k}}",
        "data_completeness": 90
    },
    {
        "name_ja": "位相幾何学・ホモロジー理論",
        "name_en": "Topology and Homology Theory",
        "name_original": "Algebraic Topology",
        "definition": "連続変形（位相同型）で不変な空間の性質（位相不変量）を研究する数学分野。基本群・ホモロジー群・コホモロジー・ホモトピー群・ファイバー束・コボルディズムが主要概念。Perelman によるポアンカレ予想の証明（Ricci流手術、2006年フィールズ賞辞退）が21世紀最大成果。",
        "impact_summary": "弦理論（カラビ-ヤウ多様体）・凝縮系物理（位相絶縁体・不変量）・データ解析（パーシステントホモロジー）・ロボティクス（構成空間）への応用が広がる。",
        "subfield": "数学",
        "school_of_thought": "位相幾何学",
        "era_start": 1895,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.claymath.org/millennium-problems/poincar%C3%A9-conjecture",
        "mathematical_formulation": r"H_n(X;\mathbb{Z}) = \ker\partial_n / \text{im}\,\partial_{n+1},\quad \chi(X) = \sum_n (-1)^n \text{rank}\, H_n",
        "data_completeness": 90
    },
    {
        "name_ja": "離散数学・ブール代数",
        "name_en": "Discrete Mathematics and Boolean Algebra",
        "name_original": "Boolean Algebra",
        "definition": "有限または可算の離散的構造（グラフ・論理式・集合・格子）を扱う数学分野の中核。Boole（1854）が論理演算を代数化したブール代数は、Shannonの情報理論・論理回路設計の基礎。命題論理・述語論理・充足可能性問題（SAT）・グラフ理論・コーディング理論と密接。",
        "impact_summary": "コンピュータ回路設計（AND/OR/NOT ゲート）・SAT solver（現代の検証ツール）・人工知能（知識表現）・Internetルーティングアルゴリズムのすべてがブール代数と離散数学上に構築されている。",
        "subfield": "数学",
        "school_of_thought": "離散数学",
        "era_start": 1854,
        "culture_region": "North_America_Europe",
        "source_url": "https://plato.stanford.edu/entries/boolean-algebras-propositional-logic/",
        "mathematical_formulation": r"A \wedge (B \vee C) = (A\wedge B)\vee(A\wedge C),\quad \overline{A\vee B} = \bar{A}\wedge\bar{B}",
        "data_completeness": 87
    },
    {
        "name_ja": "ゲーム理論の数学的基礎",
        "name_en": "Mathematical Game Theory",
        "name_original": "Game Theory",
        "definition": "合理的意思決定主体間の戦略的相互作用を数学的に分析する理論。Nash均衡（Nash 1994年ノーベル経済学賞）・ミニマックス定理（von Neumann）・協力ゲーム・繰り返しゲーム・進化ゲーム理論・メカニズム設計（Hurwicz, Maskin, Myerson 2007年ノーベル経済学賞）が主要トピック。",
        "impact_summary": "経済学・生物学（ESS: Evolutionary Stable Strategy）・政治学・オークション設計・インターネットプロトコル設計（BGP、TCP輻輳制御）に適用される。",
        "subfield": "数学",
        "school_of_thought": "応用数学",
        "era_start": 1944,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nobelprize.org/prizes/economic-sciences/1994/press-release/",
        "mathematical_formulation": r"\max_{x_1}\min_{x_2} u_1(x_1,x_2),\quad \text{Nash: } u_i(s_i^*,s_{-i}^*) \ge u_i(s_i,s_{-i}^*)\;\forall s_i",
        "data_completeness": 88
    },
    {
        "name_ja": "中国数学の古典・天元術と方程式解法",
        "name_en": "Chinese Classical Mathematics: Tian Yuan Shu",
        "name_original": "天元術",
        "definition": "天元術（天元代数）は宋・金・元代（12–14世紀）の中国数学で、数学者朱世傑（Zhu Shijie）らが多元高次方程式の数値解法と四元術（4変数連立方程式）を構築。算盤（そろばん）との連携による数値計算の精度向上と、増乗開方法（Horner法の原型）が特徴的。",
        "impact_summary": "東アジア独自の代数体系が西洋数学と独立に発展した事例。Pascal三角形（楊輝三角、1303年）がヨーロッパの200年前に中国で記述されていたことを示す。",
        "subfield": "数学",
        "school_of_thought": "東アジア数学史",
        "era_start": 1200,
        "culture_region": "East_Asia",
        "source_url": "https://www.britannica.com/science/Chinese-mathematics",
        "data_completeness": 80
    },
    {
        "name_ja": "複素解析・リーマン面",
        "name_en": "Complex Analysis and Riemann Surfaces",
        "name_original": "Complex Analysis",
        "definition": "複素数体上の関数（正則関数・有理型関数）の微積分を扱う数学。Cauchy積分定理・留数定理・コーシー-リーマン方程式・解析接続・リーマン面・モノドロミー・等角写像（Riemann写像定理）が中心。物理ではポテンシャル流・量子場の散乱振幅（complexified空間）に応用。",
        "impact_summary": "フーリエ変換・ラプラス変換の理論的基礎。リーマン ζ 関数・楕円関数・保型形式を通じて数論と深く結合。電気工学のインピーダンス解析・制御系のNyquist安定判別にも用いられる。",
        "subfield": "数学",
        "school_of_thought": "解析学",
        "era_start": 1851,
        "culture_region": "North_America_Europe",
        "source_url": "https://mathworld.wolfram.com/ComplexAnalysis.html",
        "mathematical_formulation": r"\oint_C f(z)\,dz = 2\pi i\sum_k \text{Res}(f,z_k),\quad \frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\; \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}",
        "data_completeness": 90
    },
]

STAT_COMP_BATCH = [
    {
        "name_ja": "ベイズ統計学",
        "name_en": "Bayesian Statistics",
        "name_original": "Bayesian Statistics",
        "definition": "事前確率と尤度関数をベイズの定理で結合して事後分布を推定する統計的パラダイム。MCMC（マルコフ連鎖モンテカルロ）・変分ベイズ・Stan/BUGS等の計算ツール・ベイズ情報量基準（BIC）・ベイズモデル選択・階層ベイズモデルが主要概念。頻度論と対比して主観確率・事前知識の利用を認める。",
        "impact_summary": "機械学習（ナイーブベイズ・ガウス過程・変分オートエンコーダ）・疫学（COVID-19感染者数推定）・天文学（重力波探索）・自然言語処理（LDA）の標準ツール。臨床試験の適応的設計にも採用拡大。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "統計学",
        "era_start": 1763,
        "culture_region": "North_America_Europe",
        "source_url": "https://mc-stan.org/",
        "mathematical_formulation": r"P(\theta|X) = \frac{P(X|\theta)P(\theta)}{P(X)} \propto P(X|\theta)P(\theta)",
        "data_completeness": 92
    },
    {
        "name_ja": "機械学習の統計理論",
        "name_en": "Statistical Learning Theory",
        "name_original": "Statistical Learning Theory",
        "definition": "機械学習アルゴリズムの汎化誤差・サンプル複雑性・計算複雑性を数学的に解析する理論。VC次元・Rademacher複雑性・PAC学習（Valiant 1984年）・バイアス-バリアンス分解・正則化理論（Tikhonov, Lasso, Ridge）・カーネル法（Mercer定理）が主要概念。",
        "impact_summary": "ディープラーニングの理解（過学習・二重降下・ニューラルタンジェントカーネル）・Transformerの汎化能力の理論的説明に向けた研究が活発。医療AIの認証・公平性評価に理論的根拠を提供。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "機械学習理論",
        "era_start": 1984,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.math.ias.edu/files/math/Bernstein.pdf",
        "mathematical_formulation": r"R(h) \le \hat{R}(h) + \mathcal{R}_n(\mathcal{H}) + \sqrt{\frac{\ln(1/\delta)}{2n}}",
        "data_completeness": 90
    },
    {
        "name_ja": "信号処理・ウェーブレット変換",
        "name_en": "Signal Processing and Wavelet Transform",
        "name_original": "Wavelet Transform",
        "definition": "信号を時間-周波数の両領域で解析する数学的ツール。Morlet wavelet（1984）・Daubechies wavelet（1988）・離散ウェーブレット変換（DWT）・マルチレゾリューション解析がGrossman, Morlet, Daubechiesにより整備。JPEG2000・音声圧縮・重力波（LIGOのwhitening）・医療画像（MRI再構成）に応用。",
        "impact_summary": "フーリエ変換が苦手な非定常信号解析（脳波・地震波・金融時系列）に強力。Daubechies（ベルギー、後に米国）は初の女性フィールズ賞受賞（2010年）。LIGOの重力波検出にはウェーブレット解析が活用された。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "応用数学",
        "era_start": 1984,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.wavelet.org/",
        "mathematical_formulation": r"W_f(a,b) = \frac{1}{\sqrt{|a|}}\int f(t)\,\overline{\psi\!\left(\frac{t-b}{a}\right)}\,dt",
        "data_completeness": 88
    },
    {
        "name_ja": "深層学習・バックプロパゲーション",
        "name_en": "Deep Learning and Backpropagation",
        "name_original": "Deep Learning",
        "definition": "多層人工ニューラルネットワーク（DNN）の表現学習と誤差逆伝播（backpropagation）アルゴリズムを用いた大規模パラメータ最適化。Rumelhart-Hinton-Williams（1986）が逆伝播を普及させ、LeCunの畳み込みニューラルネット（CNN）・Hochreiter-SchmidhuberのLSTM・Vaswaniらのトランスフォーマー（2017）が主要アーキテクチャ。",
        "impact_summary": "Hinton, LeCun, Bengio が2018年チューリング賞受賞。画像認識（ImageNet）・自然言語処理（GPT-4）・タンパク質構造予測（AlphaFold2）・音声認識（Whisper）での人間超え性能を達成。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "機械学習",
        "era_start": 1986,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.deeplearning.ai/",
        "mathematical_formulation": r"\mathbf{h}^{(l)} = \sigma(W^{(l)}\mathbf{h}^{(l-1)} + b^{(l)}),\quad \frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial \mathbf{h}^{(l)}}\cdot(\mathbf{h}^{(l-1)})^\top",
        "data_completeness": 92
    },
    {
        "name_ja": "計算複雑性理論・P対NP問題",
        "name_en": "Computational Complexity: P vs NP",
        "name_original": "P vs NP",
        "definition": "アルゴリズムの計算資源（時間・空間）要求量を分類する理論。P（多項式時間解ける問題）・NP（多項式時間検証可能な問題）・NP完全（Cook-Levin定理 1971）・co-NP・PSPACE・PHの多項式階層が主要クラス。P=NP?がClay Millennium Problemsの1つ。",
        "impact_summary": "暗号理論（RSA・楕円曲線暗号の安全性はP≠NP仮定に依存）・最適化・AIの根幹問題。Razborov-Rudich自然証明・算術回路下界がP vs NP証明の主要障壁として研究される。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "計算理論",
        "era_start": 1971,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.claymath.org/millennium-problems/p-vs-np-problem",
        "mathematical_formulation": r"P \subseteq NP,\quad \text{NP-hard}: \forall L'\in NP,\; L'\le_p L",
        "data_completeness": 90
    },
    {
        "name_ja": "情報理論・エントロピーとチャネル容量",
        "name_en": "Information Theory: Entropy and Channel Capacity",
        "name_original": "Information Theory",
        "definition": "Shannon（1948）が創始した情報の定量化・符号化・伝送の理論。Shannon entropy（H = -Σ p log p）・相互情報量・通信路容量（Shannon-Hartley定理）・情報源符号化定理・通信路符号化定理（誤り訂正の限界）・Slepian-Wolfのネットワーク情報理論が核心。",
        "impact_summary": "インターネット・携帯電話（LTE/5G）・圧縮（MP3/JPEG/H.264）・LDPC/Turbo符号（Shannon限界達成）・量子情報理論（量子エントロピー）の数学的基礎。Shannonは「情報革命の父」と称される。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "情報理論",
        "era_start": 1948,
        "culture_region": "North_America_Europe",
        "source_url": "https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf",
        "mathematical_formulation": r"H(X) = -\sum_x p(x)\log p(x),\quad C = B\log_2\!\left(1+\frac{S}{N}\right)",
        "data_completeness": 92
    },
    {
        "name_ja": "量子計算・量子アルゴリズム",
        "name_en": "Quantum Computing and Quantum Algorithms",
        "name_original": "Quantum Computing",
        "definition": "量子力学の重ね合わせ・エンタングルメント・干渉を利用して古典コンピュータを凌駕する計算パラダイム。Grover探索アルゴリズム（√N検索）・Shor因数分解アルゴリズム（素因数分解を多項式時間に）・量子誤り訂正（Shor符号・表面符号）・変分量子固有値ソルバー（VQE）が主要成果。",
        "impact_summary": "ShorアルゴリズムはRSA暗号を理論的に破る可能性があり、耐量子暗号（NIST標準化 2022年）への移行を促進。Googleの量子超越性実証（2019年）・IBMの1000量子ビット以上のチップが研究の最前線。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "量子情報科学",
        "era_start": 1994,
        "culture_region": "North_America_Europe",
        "source_url": "https://quantum.country/qcvc",
        "mathematical_formulation": r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle,\quad |\alpha|^2+|\beta|^2=1,\quad U_f|x\rangle|y\rangle = |x\rangle|y\oplus f(x)\rangle",
        "data_completeness": 92
    },
    {
        "name_ja": "統計的検定・仮説検定の理論",
        "name_en": "Statistical Hypothesis Testing",
        "name_original": "Hypothesis Testing",
        "definition": "Fisher（p値・有意水準）・Neyman-Pearson（第I種・第II種誤り・検出力）の枠組みによる統計的仮説検定の体系。t検定・χ2検定・ANOVA・Wilcoxon検定・尤度比検定・多重比較補正（Bonferroni・Benjamini-Hochberg FDR法）が主要手法。",
        "impact_summary": "医学・薬学（RCT）・心理学・生物学の実験科学の標準推論枠組み。再現性危機（p値ハッキング・選択的報告）を受けてEffect Size報告・事前登録・Bayesian代替の採用が進む。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "統計学",
        "era_start": 1925,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.nature.com/articles/d41586-019-00857-9",
        "mathematical_formulation": r"p\text{-value} = P(T \ge t_{\text{obs}} | H_0),\quad \text{power} = P(\text{reject } H_0 | H_1)",
        "data_completeness": 88
    },
    {
        "name_ja": "最適化理論・凸最適化",
        "name_en": "Optimization Theory and Convex Optimization",
        "name_original": "Convex Optimization",
        "definition": "目的関数の最小化・最大化を扱う数学の一分野。線形計画法（Dantzig 1947）・凸最適化（Boyd & Vandenberghe 2004）・半正定値計画（SDP）・確率的勾配降下法（SGD）・Adam・自動微分（autodiff）・変分不等式が主要概念。制約なし・制約つき最適化のKKT条件が中心定理。",
        "impact_summary": "機械学習のニューラルネット学習（確率的勾配降下法）・サプライチェーン最適化・電力網・金融ポートフォリオ・構造設計に不可欠。CVXPy・JAX・PyTorch等の自動微分ライブラリが研究・産業を変革。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "応用数学",
        "era_start": 1947,
        "culture_region": "North_America_Europe",
        "source_url": "https://web.stanford.edu/~boyd/cvxbook/",
        "mathematical_formulation": r"\min_x f(x) \text{ s.t. } g_i(x)\le 0,\quad \nabla L = 0 \Leftrightarrow \nabla f + \sum \lambda_i \nabla g_i = 0",
        "data_completeness": 90
    },
    {
        "name_ja": "ネットワーク科学・スケールフリーネットワーク",
        "name_en": "Network Science and Scale-Free Networks",
        "name_original": "Network Science",
        "definition": "実社会・生物・技術ネットワークのトポロジーと動態を複雑系科学の手法で研究する分野。Barabási-Albert（スケールフリー・優先的結合 1999）・Watts-Strogatz（スモールワールド 1998）・コミュニティ検出・パーコレーション・情報伝播・ネットワーク回復力が主要概念。",
        "impact_summary": "インターネット・SNS・疾患感染拡大・生態系・金融システム・脳神経接続（コネクトーム）の構造理解に広く適用。COVID-19感染ネットワーク解析・予防接種戦略最適化に応用された。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "複雑系科学",
        "era_start": 1998,
        "culture_region": "North_America_Europe",
        "source_url": "https://barabasi.com/book/network-science",
        "mathematical_formulation": r"P(k) \sim k^{-\gamma},\quad \langle d\rangle \sim \frac{\ln N}{\ln\ln N} \text{ (SF network)}",
        "data_completeness": 90
    },
    {
        "name_ja": "イスラーム数学・代数の起源（アル-フワーリズミー）",
        "name_en": "Islamic Mathematics: Al-Khwarizmi and the Origins of Algebra",
        "name_original": "محمد بن موسى الخوارزمي",
        "definition": "アル-フワーリズミー（c.780–c.850）は「代数（al-jabr）」という言葉の起源となった著書「Kitāb al-mukhtaṣar fī ḥisāb al-jabr waʾl-muqābala」（代数学要論、c.820）を著し、線形・二次方程式の体系的解法を記述した。「algorithm（アルゴリズム）」の語源でもある。インドのゼロ・十進数表記をアラビアに紹介した。",
        "impact_summary": "ヨーロッパ中世にラテン語訳されて伝わり、近代代数学の直接の源流となった。アルゴリズムの概念が現代計算機科学に繋がり、ゼロの概念普及は欧州数学・科学の発展を촉進した。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "イスラーム科学",
        "era_start": 820,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.britannica.com/biography/al-Khwarizmi",
        "mathematical_formulation": r"ax^2 + bx + c = 0 \Rightarrow x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
        "data_completeness": 85
    },
    {
        "name_ja": "時系列解析・ARIMAとスペクトル推定",
        "name_en": "Time Series Analysis: ARIMA and Spectral Estimation",
        "name_original": "ARIMA",
        "definition": "時間順に観測された数値列（時系列）の構造を統計的に解析・予測する手法体系。Box-Jenkins ARIMA（自己回帰和分移動平均）・SARIMA・VARモデル・状態空間モデル（カルマンフィルタ）・スペクトル推定（ピリオドグラム・Welch法）・GARCH（ボラティリティモデル）が主要手法。",
        "impact_summary": "気象予測・株価・GDP・疫病流行・電力需要・交通流の予測に標準的ツール。NeuralProphet・Prophet（Facebook）・Transformerベース（PatchTST）が機械学習との融合を進める。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "統計学",
        "era_start": 1970,
        "culture_region": "North_America_Europe",
        "source_url": "https://otexts.com/fpp3/",
        "mathematical_formulation": r"\phi(B)(1-B)^d X_t = \theta(B)\varepsilon_t,\quad \text{AIC} = -2\ln L + 2k",
        "data_completeness": 88
    },
    {
        "name_ja": "分散・並列計算・MapReduce",
        "name_en": "Distributed Computing and MapReduce",
        "name_original": "MapReduce",
        "definition": "大規模データを複数ノードに分散して並列処理するパラダイム。Lamport（分散システムの時計理論 1978）・GoogleのMapReduce（Dean & Ghemawat 2004）・Hadoop・Spark・分散ストレージ（HDFS, GFS）・CAP定理（Brewer 2000）・Paxos/Raftコンセンサスアルゴリズムが主要概念。",
        "impact_summary": "Google・Amazon・Facebook・Alibaba（East_Asia）等のクラウドサービス基盤。ビッグデータ分析・分散機械学習（Parameter Server・AllReduce）・ブロックチェーン（Nakamotoコンセンサス）の基礎技術。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "計算科学",
        "era_start": 1978,
        "culture_region": "North_America_Europe",
        "source_url": "https://static.googleusercontent.com/media/research.google.com/ja//archive/mapreduce-osdi04.pdf",
        "data_completeness": 88
    },
    {
        "name_ja": "グラフ理論・スペクトルグラフ理論",
        "name_en": "Graph Theory and Spectral Graph Theory",
        "name_original": "Graph Theory",
        "definition": "点（頂点）と辺（エッジ）からなる構造（グラフ）の組合せ的・代数的・幾何的性質を研究する数学。オイラーの一筆書き問題（1736）・四色定理（Appel-Haken 1976）・マッチング・フロー・スペクトルグラフ理論（グラフラプラシアン・チーガー不等式）・Ramsey理論が代表的トピック。",
        "impact_summary": "インターネットルーティング・ソーシャルネットワーク分析・化学分子グラフ（SMILES）・タンパク質相互作用ネットワーク・GNN（グラフニューラルネット）の数学基盤。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "離散数学",
        "era_start": 1736,
        "culture_region": "North_America_Europe",
        "source_url": "https://www.math.ucsd.edu/~fan/research/revised.html",
        "mathematical_formulation": r"\lambda_2 \ge \frac{h(G)^2}{2},\quad h(G) = \min_{S} \frac{|E(S,\bar{S})|}{\min(|S|,|\bar{S}|)}",
        "data_completeness": 88
    },
    {
        "name_ja": "強化学習・マルコフ決定過程",
        "name_en": "Reinforcement Learning and Markov Decision Processes",
        "name_original": "Reinforcement Learning",
        "definition": "エージェントが環境との相互作用（状態・行動・報酬）を通じて最適方策を学習するパラダイム。Bellman方程式・Q学習・方策勾配法・Actor-Critic・モデルベース強化学習・AlphaGo（Monte Carlo Tree Search + DNN）・PPO・SAC が主要手法。",
        "impact_summary": "囲碁（AlphaGo/AlphaZero、East_Asia/中国基地のDeepMind）・ロボット制御・材料探索・タンパク質デザイン・LLMの人間フィードバック強化学習（RLHF）の基盤技術。",
        "subfield": "統計学・計算科学",
        "school_of_thought": "機械学習",
        "era_start": 1989,
        "culture_region": "North_America_Europe",
        "source_url": "https://incompleteideas.net/book/the-book.html",
        "mathematical_formulation": r"Q^*(s,a) = \mathbb{E}\!\left[r + \gamma\max_{a'}Q^*(s',a')\right],\quad \pi^*(s) = \arg\max_a Q^*(s,a)",
        "data_completeness": 92
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    n1 = insert_batch(conn, MATH_BATCH1)
    n2 = insert_batch(conn, STAT_COMP_BATCH)
    conn.close()
    total_inserted = n1 + n2
    conn2 = sqlite3.connect(DB_PATH)
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT COUNT(*) FROM natural_discovery")
    total = cursor2.fetchone()[0]
    conn2.close()
    print(f"Batch20 math2+stat: {total_inserted} inserted (math={n1}, stat={n2}). Total: {total}")
