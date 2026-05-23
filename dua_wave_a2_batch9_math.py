"""
DUA Wave A2 Batch 9 — 数学・統計学 (Mathematics & Statistics)
Target: ~80 concepts, current subfield count ~237, target ~387
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
        "name_ja": "位相幾何学（トポロジー）",
        "name_en": "Topology",
        "definition": "連続変換で不変な図形の性質（連結性・コンパクト性・ホモトピー類）を研究する数学分野。ポアンカレ（1895年）がホモロジー・基本群を導入。ケーニヒスベルクの橋問題（オイラー1736年）が端緒とされる。",
        "impact_summary": "現代数学の基盤言語。位相的量子コンピュータ・DNAの絡み合い解析・神経科学のデータ解析（TDA: 位相的データ解析）に応用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "現代数学",
        "era_start": 1895,
        "culture_region": "Europe_Western",
        "source_url": "https://www.ams.org/notices/199811/morse.pdf",
        "mathematical_formulation": r"\pi_1(S^1) \cong \mathbb{Z}",
        "data_completeness": 90
    },
    {
        "name_ja": "整数論と素数定理",
        "name_en": "Number Theory and Prime Number Theorem",
        "definition": "素数の分布則（素数定理: x以下の素数の個数π(x) ≈ x/ln x）をアダマール・ド・ラ・ヴァレ・プサン（1896年）が証明。リーマン予想（1859年）は未解決で、素数分布の精密化の中核問題。",
        "impact_summary": "RSA暗号（1977年）の数学的基盤。楕円曲線暗号・格子暗号・量子暗号との接続でデジタル通信セキュリティの根幹をなす。クレイ研究所のミレニアム問題の一つ。",
        "subfield": "数学・統計学",
        "school_of_thought": "現代数学",
        "era_start": 1896,
        "culture_region": "Europe_Western",
        "source_url": "https://www.ams.org/journals/bull/1996-33-01/S0273-0979-96-00654-4/",
        "mathematical_formulation": r"\pi(x) \sim \frac{x}{\ln x}",
        "data_completeness": 92
    },
    {
        "name_ja": "代数幾何学",
        "name_en": "Algebraic Geometry",
        "definition": "多項式方程式の零点集合（代数多様体）の幾何的性質を研究する数学分野。グロタンディーク（1960年代）のスキーム理論が近代的基盤を確立。ワイル予想の証明（ドリーニュ1974年）・フェルマーの最終定理証明（ワイルズ1995年）に活用。",
        "impact_summary": "数論・位相幾何学・複素解析を統合する現代数学の中核。エラー訂正符号（代数幾何符号）・暗号理論・弦理論に応用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "現代数学",
        "era_start": 1900,
        "culture_region": "Europe_Western",
        "source_url": "https://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf",
        "mathematical_formulation": r"V(f) = \{(x_1,\ldots,x_n) \in \mathbb{A}^n : f(x_1,\ldots,x_n) = 0\}",
        "data_completeness": 87
    },
    {
        "name_ja": "偏微分方程式論",
        "name_en": "Partial Differential Equations",
        "definition": "複数変数の未知関数とその偏微分を含む方程式の理論。波動方程式・熱方程式・ラプラス方程式・ナビエ＝ストークス方程式が古典的モデル。ゾボレフ空間・弱解・粘性解などの現代的概念が解の存在・一意性・正則性を保証する。",
        "impact_summary": "物理・工学・生物・金融の数理モデルの言語。量子力学・流体力学・弾性論・電磁気学・金融工学の解析的基盤。ナビエ＝ストークス方程式の解の滑らかさはミレニアム問題の一つ。",
        "subfield": "数学・統計学",
        "school_of_thought": "解析学",
        "era_start": 1747,
        "culture_region": "Europe_Western",
        "source_url": "https://www.claymath.org/millennium/navier-stokes-equation",
        "mathematical_formulation": r"\frac{\partial u}{\partial t} = \alpha \nabla^2 u",
        "data_completeness": 90
    },
    {
        "name_ja": "確率論と測度論的基礎",
        "name_en": "Probability Theory and Measure-Theoretic Foundations",
        "definition": "アンドレイ・コルモゴロフ（1933年）が測度論を基盤とした確率論の公理的体系を確立。確率空間（Ω, F, P）・可測関数（確率変数）・期待値・大数の法則・中心極限定理が基本定理。",
        "impact_summary": "統計学・金融数学・機械学習・情報理論・量子力学の数学的基盤。測度論的アプローチにより確率論が厳密な数学として確立され、無限次元確率過程の理論を可能にした。",
        "subfield": "数学・統計学",
        "school_of_thought": "解析学",
        "era_start": 1933,
        "culture_region": "Europe_Eastern",
        "source_url": "https://link.springer.com/book/9780387902623",
        "mathematical_formulation": r"P\!\left(\bigcup_n A_n\right) = \sum_n P(A_n), \quad A_i \cap A_j = \emptyset",
        "data_completeness": 92
    },
    {
        "name_ja": "フーリエ解析と調和解析",
        "name_en": "Fourier Analysis and Harmonic Analysis",
        "definition": "ジョセフ・フーリエ（1822年）が任意の周期関数を正弦・余弦波の重ね合わせで表現できることを示した。フーリエ変換・離散フーリエ変換（DFT）・高速フーリエ変換（FFT, クーリー＝チューキー1965年）が現代信号処理の基盤。",
        "impact_summary": "デジタル音声・画像・通信・MRI・地震波解析・量子計算の核心技術。FFTはコンピュータ科学史上最も重要なアルゴリズムの一つとされる。",
        "subfield": "数学・統計学",
        "school_of_thought": "解析学",
        "era_start": 1822,
        "culture_region": "Europe_Western",
        "source_url": "https://mathworld.wolfram.com/FourierTransform.html",
        "mathematical_formulation": r"\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx",
        "data_completeness": 92
    },
    {
        "name_ja": "群論と対称性",
        "name_en": "Group Theory and Symmetry",
        "definition": "エヴァリスト・ガロア（1832年）が5次方程式の根号解不可能性を証明する過程で群の概念を導入。群論は数学・物理学における対称性の数学的言語となり、リー群・表現論・結晶学・素粒子標準模型の基盤をなす。",
        "impact_summary": "素粒子標準模型（SU(3)×SU(2)×U(1)）のゲージ対称性記述・結晶構造分類・暗号理論（有限群）・量子コンピュータアルゴリズムに不可欠。",
        "subfield": "数学・統計学",
        "school_of_thought": "代数学",
        "era_start": 1832,
        "culture_region": "Europe_Western",
        "source_url": "https://www.ams.org/journals/bull/2006-43-03/S0273-0979-06-01126-8/",
        "mathematical_formulation": r"(G, \cdot): \forall a,b \in G,\; ab \in G;\; \exists e;\; \forall a, \exists a^{-1}",
        "data_completeness": 92
    },
    {
        "name_ja": "複素解析",
        "name_en": "Complex Analysis",
        "definition": "複素数を変数とする解析関数（正則関数）の理論。コーシー・リーマン方程式・留数定理・解析接続・リーマン写像定理が主定理。コーシー（1825年）・リーマン（1851年）・ワイエルシュトラスが基盤を確立した。",
        "impact_summary": "量子場の理論・流体力学・電磁気学・信号処理の解析ツール。複素数の零点分布がリーマン予想（ζ関数）と直結し、素数分布の最深部に関わる。",
        "subfield": "数学・統計学",
        "school_of_thought": "解析学",
        "era_start": 1825,
        "culture_region": "Europe_Western",
        "source_url": "https://link.springer.com/book/9780387985923",
        "mathematical_formulation": r"\oint_C f(z)\,dz = 2\pi i \sum_k \mathrm{Res}(f, a_k)",
        "data_completeness": 90
    },
    {
        "name_ja": "線形代数学",
        "name_en": "Linear Algebra",
        "definition": "ベクトル空間・線形写像・行列・固有値・固有ベクトルを扱う数学分野。ケーリー（1858年）が行列代数を体系化。特異値分解（SVD）・主成分分析（PCA）・フーリエ解析の離散版として機械学習の中核数学。",
        "impact_summary": "Google PageRankアルゴリズム・推薦システム・画像圧縮・量子コンピュータ（ユニタリ変換）・深層学習（重み行列）の数学的基盤。現代科学技術の最普遍的数学ツール。",
        "subfield": "数学・統計学",
        "school_of_thought": "代数学",
        "era_start": 1858,
        "culture_region": "Europe_Western",
        "source_url": "https://math.mit.edu/~gs/linearalgebra/",
        "mathematical_formulation": r"A\vec{v} = \lambda\vec{v}",
        "data_completeness": 93
    },
    {
        "name_ja": "グラフ理論",
        "name_en": "Graph Theory",
        "definition": "頂点（ノード）と辺（エッジ）からなる数学的構造を研究する分野。オイラーのケーニヒスベルク橋問題（1736年）が起源。4色定理（1976年、コンピュータ補助証明）・ラムゼー理論・ランダムグラフ（エルドシュ＝レーニイ）が代表的成果。",
        "impact_summary": "ソーシャルネットワーク分析・交通網最適化・インターネットルーティング・分子構造解析・パンデミックモデルの数学的言語。計算複雑性理論（P対NP問題）とも深く結合する。",
        "subfield": "数学・統計学",
        "school_of_thought": "離散数学",
        "era_start": 1736,
        "culture_region": "Europe_Western",
        "source_url": "https://www.springer.com/book/9783540261834",
        "data_completeness": 90
    },
    {
        "name_ja": "最適化理論",
        "name_en": "Optimization Theory",
        "definition": "制約条件下で目的関数を最小・最大化する問題の理論と計算手法。線形計画法（ダンツィグ1947年）・非線形計画法・凸最適化・整数計画法・動的計画法（ベルマン1957年）・確率的勾配降下法が主要体系。",
        "impact_summary": "オペレーションズリサーチ・機械学習・制御理論・経済学の基本ツール。ニューラルネットワーク学習（誤差逆伝播+SGD）の数学的基盤であり、AIブームの数学的エンジン。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1947,
        "culture_region": "North_America",
        "source_url": "https://web.stanford.edu/~boyd/cvxbook/",
        "mathematical_formulation": r"\min_x f(x) \text{ s.t. } g_i(x) \leq 0, \; h_j(x) = 0",
        "data_completeness": 90
    },
    {
        "name_ja": "情報理論",
        "name_en": "Information Theory",
        "definition": "クロード・シャノン（1948年）が情報量（エントロピー）・チャネル容量・符号化の数学的理論を確立。シャノンエントロピー H = -Σp log p、チャネル容量定理が基本。ハフマン符号・データ圧縮・誤り訂正符号の理論的基盤。",
        "impact_summary": "デジタル通信・データ圧縮（JPEG・MP3）・暗号化・機械学習（クロスエントロピー損失・KLダイバージェンス）の数学的基盤。人工知能の知識表現と情報処理の理論的枠組み。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1948,
        "culture_region": "North_America",
        "source_url": "https://math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf",
        "mathematical_formulation": r"H(X) = -\sum_{x \in \mathcal{X}} p(x) \log p(x)",
        "data_completeness": 95
    },
    {
        "name_ja": "カオス理論と非線形力学系",
        "name_en": "Chaos Theory and Nonlinear Dynamical Systems",
        "definition": "エドワード・ローレンツ（1963年）が大気対流モデルで初期値敏感依存性（バタフライ効果）を発見。リャプノフ指数・フラクタル次元・アトラクターが特性量。マンデルブロート集合（1979年）がフラクタル幾何の直観的象徴。",
        "impact_summary": "決定論的系における予測不可能性の発見。気象・生態系・株価・神経活動・乱流の理解に革命をもたらし、複雑系科学の基盤となった。",
        "subfield": "数学・統計学",
        "school_of_thought": "非線形科学",
        "era_start": 1963,
        "culture_region": "North_America",
        "source_url": "https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml",
        "mathematical_formulation": r"\lambda = \lim_{t\to\infty} \frac{1}{t}\ln\frac{|\delta Z(t)|}{|\delta Z(0)|}",
        "data_completeness": 90
    },
    {
        "name_ja": "フラクタル幾何学",
        "name_en": "Fractal Geometry",
        "definition": "ブノワ・マンデルブロート（1975年）がフラクタルの概念を体系化。自己相似性・非整数次元（ハウスドルフ次元）が特徴。コッホ曲線・カントール集合・シェルピンスキー三角形が古典例。自然界の海岸線・雲・雪の結晶・血管網がフラクタル構造を示す。",
        "impact_summary": "複雑な自然形態の数学的記述。画像圧縮（フラクタル圧縮）・アンテナ設計・腫瘍成長モデル・株価変動の数理モデルに応用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "非線形科学",
        "era_start": 1975,
        "culture_region": "North_America",
        "source_url": "https://www.cambridge.org/core/books/fractal-geometry/",
        "mathematical_formulation": r"d_H = \lim_{\epsilon\to 0} \frac{\log N(\epsilon)}{\log(1/\epsilon)}",
        "data_completeness": 87
    },
    {
        "name_ja": "数値解析と計算数学",
        "name_en": "Numerical Analysis and Scientific Computing",
        "definition": "数学的問題を有限精度の計算で近似解く理論と手法。有限差分法・有限要素法・モンテカルロ法・反復法・高速アルゴリズム設計が中心。丸め誤差・打ち切り誤差・数値安定性が重要概念。",
        "impact_summary": "工学・物理・生物・金融のすべての計算シミュレーションの数学的基盤。スパースソルバー・並列計算・GPU加速・量子コンピュータとの連携で計算科学に中核的役割を担う。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1946,
        "culture_region": "Global",
        "source_url": "https://www.siam.org/publications/books/numerical-analysis/",
        "data_completeness": 88
    },
    {
        "name_ja": "ゲーム理論（数学的基礎）",
        "name_en": "Game Theory (Mathematical Foundations)",
        "definition": "フォン・ノイマンとモルゲンシュテルン（1944年）が戦略的意思決定を数学的に定式化した理論。ナッシュ均衡（1950年）・ゼロサムゲーム・繰り返しゲーム・協力ゲームが主要概念。マクシミン定理・ミニマックス定理が基本定理。",
        "impact_summary": "経済学・政治科学・進化生物学・コンピュータ科学・軍事戦略の数学的基盤。オークション設計・電波帯域割当・AI強化学習のアルゴリズム設計に直接応用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1944,
        "culture_region": "Europe_Western",
        "source_url": "https://press.princeton.edu/books/paperback/9780691130613/theory-of-games-and-economic-behavior",
        "mathematical_formulation": r"\max_{x \in X} \min_{y \in Y} f(x, y) = \min_{y \in Y} \max_{x \in X} f(x, y)",
        "data_completeness": 90
    },
    {
        "name_ja": "ベイズ統計と事後分布推論",
        "name_en": "Bayesian Statistics and Posterior Inference",
        "definition": "事前確率・尤度・事後確率の関係（ベイズの定理）に基づき、データを観測するたびに信念を更新する統計的枠組み。マルコフ連鎖モンテカルロ（MCMC）・変分推論が計算手法。階層モデル・ガウス過程・ベイズニューラルネットが応用形態。",
        "impact_summary": "不確実性定量化・小標本統計・機械学習（確率的モデル）・医学研究・政策評価の主要パラダイム。頻度主義統計との二大学派として科学的推論の哲学的議論を提供する。",
        "subfield": "数学・統計学",
        "school_of_thought": "統計学",
        "era_start": 1763,
        "culture_region": "Europe_Western",
        "source_url": "https://www.stat.columbia.edu/~gelman/book/",
        "mathematical_formulation": r"p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)}",
        "data_completeness": 92
    },
    {
        "name_ja": "仮説検定と統計的有意性",
        "name_en": "Hypothesis Testing and Statistical Significance",
        "definition": "フィッシャー（1925年）・ネイマン＝ピアソン（1933年）が確立した帰無仮説検定の枠組み。p値・検定力・タイプI・IIエラー・信頼区間が基本概念。再現性危機（2010年代）を受けてベイズ的代替やデフォルト推定量への移行が進む。",
        "impact_summary": "科学的知識生産の標準的統計ツール。臨床試験・心理学・社会科学における統計的有意性基準p<0.05の批判的再評価が、科学的方法論の刷新を促している。",
        "subfield": "数学・統計学",
        "school_of_thought": "統計学",
        "era_start": 1925,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/d41586-019-00857-9",
        "mathematical_formulation": r"p = P(T \geq t_{obs} | H_0)",
        "data_completeness": 90
    },
    {
        "name_ja": "多変量解析",
        "name_en": "Multivariate Statistical Analysis",
        "definition": "複数の変量を同時に解析する統計的手法群。主成分分析（PCA）・因子分析・判別分析・クラスター分析・多変量回帰・偏最小二乗法が代表的。ピアソン（1901年）のPCAが端緒とされる。",
        "impact_summary": "遺伝学（GWAS）・神経科学（fMRI解析）・マーケティング・金融リスク管理の多変量データ理解ツール。機械学習の教師なし学習（次元削減・クラスタリング）の数学的基盤。",
        "subfield": "数学・統計学",
        "school_of_thought": "統計学",
        "era_start": 1901,
        "culture_region": "Europe_Western",
        "source_url": "https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316801",
        "data_completeness": 88
    },
    {
        "name_ja": "ランダム行列理論",
        "name_en": "Random Matrix Theory",
        "definition": "要素がランダムな大型行列の固有値分布を研究する数学分野。ウィグナー（1955年）が原子核の励起準位統計を説明するために導入。半円則・GUE（ガウスユニタリアンサンブル）・マルチェンコ・パスツール分布が基本定理。",
        "impact_summary": "量子カオス・リーマンζ関数の零点分布・高次元統計（covariance行列推定）・無線通信のMIMO技術の数学的基盤。機械学習の高次元統計解析への応用が急速に拡大。",
        "subfield": "数学・統計学",
        "school_of_thought": "現代数学",
        "era_start": 1955,
        "culture_region": "Europe_Western",
        "source_url": "https://www.annualreviews.org/doi/10.1146/annurev.statistics.011008.108103",
        "mathematical_formulation": r"\rho_{sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}, \; |x|\leq 2",
        "data_completeness": 85
    },
    {
        "name_ja": "インド数学の中世的発展（ケーララ学派続論）",
        "name_en": "Medieval Indian Mathematics: Extended Contributions",
        "definition": "マーダヴァ（1350〜1425年）はπの無限級数（マーダヴァ＝ライプニッツ級数）・正弦・余弦の冪級数をニュートン・ライプニッツより2世紀先に導出した。バースカラ2世（1150年）は微積分の先駆的概念を含む。ニーラカンタ（1500年頃）は地動説的惑星モデルを構築した。",
        "impact_summary": "西欧中心的科学史の修正に最も重要な非西洋数学の事例。微積分・無限級数・三角関数の独立発見が文化的多元性と知識移転の経路を問い直す。",
        "subfield": "数学・統計学",
        "school_of_thought": "科学史",
        "era_start": 1380,
        "culture_region": "South_Asia",
        "source_url": "https://www.cambridge.org/core/books/geometry-in-ancient-and-medieval-india/",
        "mathematical_formulation": r"\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots",
        "data_completeness": 85
    },
    {
        "name_ja": "アラビア代数学（フワーリズミー）",
        "name_en": "Arabic Algebra (Al-Khwarizmi)",
        "definition": "ムハンマド・イブン・ムーサー・アル＝フワーリズミー（820年代）が『アル＝キターブ・アル＝ムフタサル』で方程式の系統的解法を示し、代数学（algebra＜al-jabr）とアルゴリズム（algorithm＜al-Khwarizmi）の語源となった。",
        "impact_summary": "現代代数学の直系起源。バグダードの知恵の館での翻訳活動を経てヨーロッパに伝わり、中世数学を変革した。コンピュータ科学の「アルゴリズム」概念の語源としても科学史上決定的。",
        "subfield": "数学・統計学",
        "school_of_thought": "科学史",
        "era_start": 820,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.cambridge.org/core/books/mathematics-of-egypt-mesopotamia-china-india-and-islam/",
        "data_completeness": 85
    },
    {
        "name_ja": "中国の数学史（『九章算術』）",
        "name_en": "Chinese Mathematical Tradition (Nine Chapters)",
        "definition": "『九章算術』（前漢期に成立、AD前1世紀）は246の数学問題を体系化し、分数・連立一次方程式（行列消去法）・ピタゴラスの定理の応用・負数を扱った。劉徽（263年）の注釈が数学的証明を加え、祖冲之（480年頃）がπを3.1415926〜3.1415927と求めた。",
        "impact_summary": "東アジア数学の正典として千年以上使用された。行列消去法（現代のガウス消去法に対応）・負数・円周率精密化における中国数学の独立的高度発達の証拠。",
        "subfield": "数学・統計学",
        "school_of_thought": "科学史",
        "era_start": -100,
        "culture_region": "East_Asia",
        "source_url": "https://www.cambridge.org/core/books/mathematics-of-egypt-mesopotamia-china-india-and-islam/",
        "data_completeness": 83
    },
    {
        "name_ja": "バビロニア数学と60進法",
        "name_en": "Babylonian Mathematics and Sexagesimal System",
        "definition": "メソポタミアのバビロニア（BC2000〜500年）は60進位取り記数法を採用し、ピタゴラスの定理の応用・二次方程式の数値解法・天文計算を高精度で実施した。粘土板YBC 7289はπ（√2）を小数点以下6桁精度で記録する。",
        "impact_summary": "現代の60分・60秒・360度の起源。西洋数学に先行する体系的数学の最古事例の一つ。プトレマイオスの天文学を経由して近代天文学・数学に継承された。",
        "subfield": "数学・統計学",
        "school_of_thought": "科学史",
        "era_start": -2000,
        "culture_region": "West_Asia_North_Africa",
        "source_url": "https://www.cambridge.org/core/books/mathematics-of-egypt-mesopotamia-china-india-and-islam/",
        "data_completeness": 82
    },
    {
        "name_ja": "確率過程論（ブラウン運動・マルコフ連鎖）",
        "name_en": "Stochastic Processes (Brownian Motion, Markov Chains)",
        "definition": "時間とともに確率的に変動する現象の数学的モデル。ブラウン運動（ウィーナー過程）はアインシュタイン（1905年）・ウィーナー（1923年）が定式化。マルコフ連鎖は遷移確率行列で次状態が現在状態のみで決まる系。伊藤確率微分方程式が確率過程の微積分を提供。",
        "impact_summary": "金融数学（ブラック・ショールズ方程式）・量子力学・拡散過程・機械学習（MCMC・拡散モデル）の数学的基盤。拡散確率微分方程式が生成AIの画像生成モデルの核。",
        "subfield": "数学・統計学",
        "school_of_thought": "解析学",
        "era_start": 1905,
        "culture_region": "Europe_Western",
        "source_url": "https://link.springer.com/book/9783642140945",
        "mathematical_formulation": r"dX_t = \mu(X_t,t)dt + \sigma(X_t,t)dW_t",
        "data_completeness": 90
    },
    {
        "name_ja": "圏論（カテゴリー理論）",
        "name_en": "Category Theory",
        "definition": "アイレンバーグとマックレーン（1945年）が導入した、数学的構造とその間の射（関手）を抽象的に扱う理論。「数学の数学」とも呼ばれ、様々な数学的概念を統一する言語を提供する。モナド・随伴関手・トポス・高次圏が主要概念。",
        "impact_summary": "関数型プログラミング言語（Haskell・Scala）の設計・型理論・形式検証・量子計算プロトコルの数学的基盤。物理学のTQFT・弦理論のモジュラー圏にも応用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "現代数学",
        "era_start": 1945,
        "culture_region": "North_America",
        "source_url": "https://www.cambridge.org/core/books/category-theory/",
        "data_completeness": 85
    },
    {
        "name_ja": "機械学習の数学的基盤",
        "name_en": "Mathematical Foundations of Machine Learning",
        "definition": "機械学習は線形代数（重み行列）・確率論（ベイズ推定）・最適化（SGD・Adam）・情報理論（クロスエントロピー）・汎化理論（VC次元・PAC学習）を統合する。バプニック・チェルヴォネンキスの統計学習理論（1971年）が理論的基盤。",
        "impact_summary": "深層学習・強化学習・支持ベクトル機械の数学的理解の基盤。AIシステムの予測能力・汎化・過学習・説明可能性の理論的保証に不可欠。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1971,
        "culture_region": "Global",
        "source_url": "https://www.cambridge.org/core/books/understanding-machine-learning/",
        "mathematical_formulation": r"\mathcal{L}(\theta) = \frac{1}{n}\sum_{i=1}^n \ell(f_\theta(x_i), y_i) + \lambda\|\theta\|^2",
        "data_completeness": 90
    },
    {
        "name_ja": "数理生物学と個体群動態",
        "name_en": "Mathematical Biology and Population Dynamics",
        "definition": "ロトカ・ヴォルテラ方程式（1925年）が捕食者‐被食者の個体数振動を記述。SIRモデル（1927年）が感染症の流行を記述。フィッシャーの反応拡散方程式・チューリングのパターン形成（1952年）が生物形態形成の数理モデルを確立。",
        "impact_summary": "COVID-19パンデミック対策の数理的基盤（SIRモデル拡張）。生態系保全・農業害虫管理・創薬・発生生物学のシミュレーション設計に使用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1925,
        "culture_region": "Global",
        "source_url": "https://link.springer.com/book/9783662393673",
        "mathematical_formulation": r"\frac{dN}{dt} = rN\left(1-\frac{N}{K}\right)",
        "data_completeness": 88
    },
    {
        "name_ja": "ウェーブレット変換",
        "name_en": "Wavelet Transform",
        "definition": "モルレ・グロスマン（1984年）・ドービシー（1988年）が開発した時間‐周波数同時解析ツール。フーリエ変換と異なり局所的な時間変動を捉え、マルチスケール解析を可能にする。JPEG2000・LIGO重力波信号解析・地震波解析に応用。",
        "impact_summary": "信号処理・画像圧縮・医用画像（ECG・MRI）・地球物理データ解析の標準ツール。スパース表現と圧縮センシングの数学的基盤としてAI/統計学習にも活用される。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1984,
        "culture_region": "Europe_Western",
        "source_url": "https://www.cambridge.org/core/books/ten-lectures-on-wavelets/",
        "mathematical_formulation": r"W_f(a,b) = \frac{1}{\sqrt{a}}\int f(t)\,\overline{\psi\!\left(\frac{t-b}{a}\right)}dt",
        "data_completeness": 88
    },
    {
        "name_ja": "暗号理論（公開鍵暗号と格子暗号）",
        "name_en": "Cryptographic Theory: Public-Key and Lattice-Based",
        "definition": "RSA（リベスト・シャミール・エーデルマン1977年）は素因数分解の困難性を利用した公開鍵暗号。楕円曲線暗号（コブリッツ・ミラー1985年）が効率化。量子コンピュータ耐性の後量子暗号として格子問題（LWE・SIS）に基づく格子暗号がNIST標準化（2022年）された。",
        "impact_summary": "インターネット通信・電子商取引・ブロックチェーンのセキュリティ基盤。量子計算機の実用化を見越した後量子暗号への移行が国際的に進行中。",
        "subfield": "数学・統計学",
        "school_of_thought": "応用数学",
        "era_start": 1977,
        "culture_region": "North_America",
        "source_url": "https://csrc.nist.gov/projects/post-quantum-cryptography",
        "mathematical_formulation": r"C = M^e \bmod n, \quad M = C^d \bmod n",
        "data_completeness": 90
    },
    {
        "name_ja": "スペクトルグラフ理論",
        "name_en": "Spectral Graph Theory",
        "definition": "グラフの隣接行列・ラプラシアン行列の固有値・固有ベクトルを用いてグラフの構造的性質（連結性・直径・彩色数・展開性）を解析する理論。チーガー不等式・ラプラシアン固有値のギャップが重要量。",
        "impact_summary": "Google PageRank・グラフニューラルネットワーク（GNN）・コミュニティ検出・量子コンピュータの量子ウォーク・スペクトルクラスタリングの数学的基盤。",
        "subfield": "数学・統計学",
        "school_of_thought": "離散数学",
        "era_start": 1970,
        "culture_region": "Global",
        "source_url": "https://link.springer.com/book/9783319498836",
        "mathematical_formulation": r"L = D - A, \quad \lambda_2 > 0 \Leftrightarrow G \text{ is connected}",
        "data_completeness": 85
    },
    {
        "name_ja": "アフリカの数学的遺産（イシャンゴの骨）",
        "name_en": "African Mathematical Heritage (Ishango Bone)",
        "definition": "コンゴ民主共和国で発見されたイシャンゴの骨（約22,000年前）には素数列・乗算表と解釈される刻み目が施されており、人類最古の数学的活動の可能性がある。エジプト数学（パピルス・アフメス BC1650年頃）は分数・線形方程式を扱った。",
        "impact_summary": "数学的活動の起源をサブサハラアフリカに遡る可能性の証拠。アフリカ数学教育のルーツとして科学史の多元化に重要な事例。",
        "subfield": "数学・統計学",
        "school_of_thought": "科学史",
        "era_start": -22000,
        "culture_region": "Sub_Saharan_Africa",
        "source_url": "https://www.cambridge.org/core/books/mathematics-of-egypt-mesopotamia-china-india-and-islam/",
        "data_completeness": 78
    },
]

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)

    n = insert_batch(conn, CONCEPTS)
    print(f"  Inserted: {n}")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM natural_discovery")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"\nBatch9 math: {n} concepts inserted")
    print(f"Total in table: {count}")
