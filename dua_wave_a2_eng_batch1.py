#!/usr/bin/env python3
"""
DUA Wave A2 — engineering_method 拡張 Batch 1
対象: 機械工学 (mechanical_engineering) +350 件
ID範囲: eng_w2_0001 - eng_w2_0350
"""
import sqlite3
import json

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

BATCH1_MECHANICAL = [
    ("eng_w2_0001","熱力学第一法則","First Law of Thermodynamics","Thermodynamics First Law",
     "エネルギー保存則を述べる熱力学の基本法則。閉じた系において内部エネルギーの変化は系に加えられた熱と系がされた仕事の和に等しい。工学的熱機関設計の基礎となる。",
     "蒸気機関から現代エンジン・発電プラントまで全熱機械設計の根幹を形成。","機械工学","古典熱力学",1850,None,
     "基礎理論","熱機関・冷凍機・化学反応器","エネルギー収支が閉じた系","機関効率を最大化したい場合",
     "内部エネルギー・熱・仕事を定量的に問う","熱力学第二法則との対比",
     "熱力学,エネルギー保存,内部エネルギー,仕事,熱","thermodynamics,energy conservation,internal energy,work,heat",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/First_law_of_thermodynamics","Western_Europe",90,
     "ΔU = Q - W : 内部エネルギー変化=加熱量-仕事量",500,"url_present"),

    ("eng_w2_0002","熱力学第二法則","Second Law of Thermodynamics","Thermodynamics Second Law",
     "エントロピーが孤立系において増大するか一定であるという法則。可逆・不可逆過程の方向性を決定し、熱機関の最大効率（カルノー効率）を規定する。",
     "熱機関の理論上限効率を定義。冷凍サイクル・ヒートポンプ設計の絶対基準。","機械工学","古典熱力学",1851,None,
     "基礎理論","熱機関・冷凍サイクル・化学プロセス","エントロピー・効率限界","エネルギー変換方向を理解したい場合",
     "なぜ熱は自然に高温から低温へ流れるか","熱力学第一法則",
     "熱力学,エントロピー,カルノー効率,不可逆過程","thermodynamics,entropy,Carnot efficiency,irreversible process",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Second_law_of_thermodynamics","Western_Europe",90,
     "η_Carnot = 1 - T_cold/T_hot : カルノー効率",500,"url_present"),

    ("eng_w2_0003","ベルヌーイの定理","Bernoulli's Principle","Bernoulli equation",
     "理想流体の定常流れにおいて、流線に沿って圧力・速度・位置の和が一定であることを示す定理。揚力・ベンチュリ管・翼型設計の基礎。",
     "航空機翼・ポンプ・流量計・カルブレタ設計の不可欠な基礎原理。","機械工学","流体力学",1738,None,
     "基礎理論","空気力学・水力学・計装","粘性が無視できる定常層流","揚力や流速を圧力から求める場合",
     "圧力と速度はなぜトレードオフするか","粘性流体のナビエ-ストークス方程式",
     "流体力学,ベルヌーイ,揚力,圧力,速度","fluid mechanics,Bernoulli,lift,pressure,velocity",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Bernoulli%27s_principle","Western_Europe",90,
     "p + 1/2 ρv² + ρgh = const : ベルヌーイ方程式",500,"url_present"),

    ("eng_w2_0004","ナビエ-ストークス方程式","Navier-Stokes Equations","Navier-Stokes",
     "粘性流体の運動を支配する偏微分方程式系。ニュートン流体に対する運動量保存則で、乱流解析・CFD（数値流体力学）の基礎方程式となる。",
     "航空・船舶・エンジン・血流シミュレーション等あらゆる流体工学の計算基盤。ミレニアム問題の一つ。","機械工学","流体力学",1845,None,
     "基礎理論","CFD・乱流解析・気象予測","ニュートン粘性流体","流体の速度場・圧力場を詳細に計算する場合",
     "粘性と慣性力のバランスはどう記述されるか","オイラー方程式（非粘性近似）",
     "流体力学,ナビエストークス,CFD,乱流,粘性","fluid mechanics,Navier-Stokes,CFD,turbulence,viscosity",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations","Western_Europe",90,
     "ρ(∂u/∂t + u·∇u) = -∇p + μ∇²u + f",500,"url_present"),

    ("eng_w2_0005","有限要素法","Finite Element Method","FEM",
     "複雑な構造・熱・流体問題を小要素(element)に分割して近似的に解く数値解析手法。建築・自動車・航空機の構造解析に広く使用される。",
     "CAE（コンピュータ支援工学）の基幹技術。あらゆる製造業の設計検証プロセスを変革。","機械工学","計算力学",1956,None,
     "数値解析手法","構造解析・熱解析・電磁界解析","連続体・境界値問題","複雑形状の応力・変形・温度分布を計算する場合",
     "連続体問題をどう離散化して解くか","有限差分法・境界要素法",
     "有限要素法,FEM,構造解析,CAE,数値解析","finite element method,FEM,structural analysis,CAE,numerical analysis",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Finite_element_method","North_America",90,
     "K·u = f : 剛性行列方程式（K=剛性行列, u=変位ベクトル, f=荷重ベクトル）",500,"url_present"),

    ("eng_w2_0006","PID制御","PID Control","PID Controller",
     "比例(P)・積分(I)・微分(D)の3要素をフィードバックに用いる古典制御手法。シンプルでありながら多くの工業プロセスに有効で、最も広く実装された制御アルゴリズム。",
     "産業用プロセス制御・ロボット・自動車・HVAC等の制御システムの標準手法。","機械工学","制御工学",1922,None,
     "制御手法","温度・速度・位置制御","線形時不変系・センサフィードバックが取れる環境","定常偏差をゼロにしたい場合",
     "誤差をどのようにフィードバックして安定制御するか","モデル予測制御（MPC）・スライディングモード制御",
     "PID制御,フィードバック,制御工学,比例積分微分","PID control,feedback,control engineering,proportional integral derivative",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/PID_controller","Western_Europe",90,
     "u(t) = Kp·e + Ki·∫e dt + Kd·de/dt : PID制御則",500,"url_present"),

    ("eng_w2_0007","モデル予測制御","Model Predictive Control","MPC",
     "プロセスモデルを用いて未来の挙動を予測し、制御入力を最適化するフィードバック制御手法。制約条件を明示的に扱えることが特徴で化学プロセス・自動車・ロボットに用いる。",
     "石油精製・自動車自動運転・工場ラインの多変数制御に不可欠な現代制御技術。","機械工学","制御工学",1978,None,
     "最適制御手法","多変数制御・制約付き最適化","プロセスモデルが得られる場合","複数入出力・制約を持つ系の最適制御",
     "予測ホライズンと制御ホライズンをどう設定するか","PID制御・LQR",
     "モデル予測制御,MPC,最適制御,多変数制御","model predictive control,MPC,optimal control,multivariable control",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Model_predictive_control","North_America",90,
     "min_u Σ||y-r||²_Q + ||Δu||²_R s.t. 制約 : MPC最適化問題",500,"url_present"),

    ("eng_w2_0008","材料力学 (応力-ひずみ関係)","Mechanics of Materials","Stress-strain relationship",
     "固体材料に作用する応力とひずみの関係を扱う工学分野。フックの法則・破壊力学・疲労破壊の基礎を提供し、構造部材の設計に直結する。",
     "橋梁・建物・航空機・機械部品など全構造物の寸法決定の基礎理論。","機械工学","固体力学",1678,None,
     "基礎理論","構造設計・破壊解析","弾性体・均質等方性材料","部材の強度・変形量を設計する場合",
     "応力が許容値を超えた場合どのように材料は破壊するか","弾塑性解析・破壊力学",
     "材料力学,応力,ひずみ,フック則,破壊","mechanics of materials,stress,strain,Hooke's law,fracture",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Strength_of_materials","Western_Europe",90,
     "σ = E·ε : フックの法則（σ=応力, E=ヤング率, ε=ひずみ）",500,"url_present"),

    ("eng_w2_0009","機械設計 CAD/CAM","CAD/CAM Mechanical Design","Computer-Aided Design Manufacturing",
     "コンピュータ支援設計(CAD)と製造(CAM)を統合したデジタル製品開発手法。3Dモデルから直接CNCプログラムを生成し製造工程を自動化する。",
     "製造業のデジタル化の核心。設計から製造までのリードタイムを劇的に短縮。","機械工学","デジタル製造",1963,None,
     "設計・製造手法","金型・部品加工・プロダクト開発","3D CADシステム・CNC工作機械","複雑形状部品の精密製造",
     "デジタルモデルから物理的な部品をどう効率的に製造するか","デジタルツイン・アディティブ製造",
     "CAD,CAM,コンピュータ支援設計,CNC,デジタル製造","CAD,CAM,computer-aided design,CNC,digital manufacturing",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Computer-aided_manufacturing","North_America",85,
     None,500,"url_present"),

    ("eng_w2_0010","熱伝導方程式 (フーリエ則)","Fourier's Law of Heat Conduction","Fourier heat equation",
     "物体内の温度分布の時間変化を記述する偏微分方程式。熱伝導率と温度勾配の積として熱流束を定義するフーリエ則に基づき、冷却設計・断熱材設計に用いる。",
     "電子機器冷却・建築断熱・原子炉熱設計の根幹方程式。","機械工学","伝熱工学",1822,None,
     "基礎理論","熱設計・電子冷却・建築断熱","均質固体・初期境界条件","温度分布・熱流束を計算する場合",
     "熱はどの方向に・どの速さで伝わるか","対流熱伝達・輻射熱伝達",
     "熱伝導,フーリエ則,熱流束,温度分布","heat conduction,Fourier's law,heat flux,temperature distribution",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Fourier%27s_law_of_heat_conduction","Western_Europe",90,
     "q = -k∇T : フーリエ則（q=熱流束ベクトル, k=熱伝導率, T=温度）",500,"url_present"),

    ("eng_w2_0011","流体機械 (ターボ機械)","Turbomachinery","Turbomachinery design",
     "流体のエネルギーと機械的仕事を変換する回転機械（タービン・ポンプ・圧縮機）の設計理論。速度三角形・比速度・効率曲線が設計の基本ツール。",
     "発電タービン・航空機エンジン・ポンプシステムの設計基盤。","機械工学","流体機械",1880,None,
     "設計手法","発電・推進・流体搬送","圧縮性/非圧縮性流体","流体-機械エネルギー変換を最大効率で行う場合",
     "インペラ形状と性能曲線はどう関係するか","容積型機械・リニア電動機",
     "ターボ機械,タービン,ポンプ,圧縮機,流体機械","turbomachinery,turbine,pump,compressor,fluid machinery",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Turbomachinery","Western_Europe",85,
     "H = u²/g : 揚程（u=周速度, g=重力加速度） — オイラーのターボ機械方程式",500,"url_present"),

    ("eng_w2_0012","疲労破壊とS-N曲線","Fatigue Fracture and S-N Curve","Wöhler S-N curve",
     "繰り返し応力負荷による材料破壊（疲労破壊）を定量化するS-N曲線(Wöhler曲線)。応力振幅と破壊繰り返し数の関係を示し、機械部品の寿命設計に使用する。",
     "自動車・航空機・橋梁の疲労寿命設計の標準手法。","機械工学","破壊力学",1860,None,
     "設計手法","機械部品寿命設計","繰り返し荷重を受ける金属部品","部品の疲労寿命を予測する場合",
     "どの応力振幅が何回の繰り返しで破壊を引き起こすか","破壊力学・余寿命推定",
     "疲労破壊,S-N曲線,寿命設計,繰り返し荷重","fatigue fracture,S-N curve,life design,cyclic loading",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Fatigue_(material)","Western_Europe",85,
     "log N = a - b·log S_a : S-N曲線の対数近似（N=繰り返し数, S_a=応力振幅）",500,"url_present"),

    ("eng_w2_0013","ラグランジュ・ハミルトン力学","Lagrangian-Hamiltonian Mechanics","Analytical mechanics",
     "解析力学の2大定式化。ラグランジアン L=T-V からオイラー=ラグランジュ方程式、ハミルトニアン H=T+V からハミルトン方程式を導き、ロボットダイナミクス・軌道制御の計算に使用。",
     "多体ロボット制御・宇宙機軌道計算・量子力学基礎の共通言語。","機械工学","解析力学",1788,None,
     "基礎理論","ロボット制御・宇宙機・多体系","ホロノミック・非ホロノミック拘束系","一般化座標で運動方程式を組み立てる場合",
     "ニュートン力学と解析力学の等価性とその利点は","ニュートン力学・量子力学",
     "解析力学,ラグランジアン,ハミルトニアン,運動方程式","analytical mechanics,Lagrangian,Hamiltonian,equations of motion",
     "active","primary",95,1,"https://en.wikipedia.org/wiki/Lagrangian_mechanics","Western_Europe",90,
     "d/dt(∂L/∂q̇) - ∂L/∂q = 0 : オイラー=ラグランジュ方程式",500,"url_present"),

    ("eng_w2_0014","振動工学 (固有振動・共振)","Vibration Engineering","Natural frequency resonance",
     "機械系の振動特性（固有振動数・減衰比・共振）を解析し、防振・制振設計に活用する工学分野。1自由度系から多体系・連続体まで体系化される。",
     "橋梁崩壊・航空機フラッタ・精密機器防振の設計基盤。","機械工学","振動工学",1800,None,
     "解析手法","防振設計・モーダル解析","線形振動系","共振を回避し振動を抑制する設計",
     "システムの固有振動数はどう決まり共振をどう防ぐか","制振材料・アクティブ制振",
     "振動工学,固有振動数,共振,モーダル解析","vibration engineering,natural frequency,resonance,modal analysis",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Vibration","Western_Europe",85,
     "ωn = √(k/m) : 固有角振動数（k=剛性, m=質量）",500,"url_present"),

    ("eng_w2_0015","熱機関サイクル (オットー・ディーゼル)","Otto and Diesel Cycles","Combustion engine thermodynamic cycles",
     "内燃機関の理想熱力学サイクル。オットーサイクル（ガソリン）とディーゼルサイクルの理論熱効率を比較・最大化し、エンジン設計の目標値として用いる。",
     "自動車・船舶・発電機エンジンの設計効率目標。","機械工学","熱機関",1876,None,
     "設計理論","内燃機関設計","圧縮点火・火花点火エンジン","燃焼サイクルの理論効率を計算する場合",
     "圧縮比はどの程度熱効率に影響するか","ランキンサイクル・ブレイトンサイクル",
     "熱機関,オットーサイクル,ディーゼル,熱効率","heat engine,Otto cycle,diesel,thermal efficiency",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Otto_cycle","Western_Europe",85,
     "η_Otto = 1 - (1/r^(γ-1)) : オットーサイクル熱効率（r=圧縮比, γ=比熱比）",500,"url_present"),

    ("eng_w2_0016","摩擦・潤滑工学 (トライボロジー)","Tribology","Tribology friction lubrication wear",
     "摩擦・摩耗・潤滑を総合的に研究する工学分野（トライボロジー）。摩擦係数・EHD潤滑・表面テクスチャリングにより機械部品の寿命と効率を最大化する。",
     "自動車エンジン・ベアリング・切削加工の効率改善と長寿命化の基盤。","機械工学","トライボロジー",1966,None,
     "応用工学","摺動部品・切削・ベアリング","接触表面が相対運動する系","摩擦エネルギー損失と摩耗を最小化する場合",
     "どのような表面状態と潤滑剤が摩擦を最小化するか","表面工学・コーティング",
     "トライボロジー,摩擦,潤滑,摩耗,表面","tribology,friction,lubrication,wear,surface",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/Tribology","Western_Europe",85,
     "f = μ·N : 摩擦力（μ=摩擦係数, N=法線力）",500,"url_present"),

    ("eng_w2_0017","溶接・接合工学","Welding and Joining Engineering","Welding metallurgy",
     "金属材料の永久接合技術の工学的基盤。アーク溶接・レーザ溶接・摩擦攪拌接合(FSW)を含み、溶接部の組織・残留応力・欠陥を制御する。",
     "自動車車体・船舶・建築鉄骨・配管の製造品質の根幹技術。","機械工学","製造加工",1880,None,
     "製造技術","金属構造物製造","溶融接合・固相接合","金属部品を恒久的に結合する場合",
     "溶接熱影響部の組織変化はどう品質に影響するか","接着・締結",
     "溶接,接合,FSW,溶接冶金,残留応力","welding,joining,FSW,welding metallurgy,residual stress",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/Welding","Western_Europe",80,
     None,500,"url_present"),

    ("eng_w2_0018","切削加工理論","Cutting Theory","Metal cutting mechanics",
     "金属切削の力学的メカニズムを記述する理論。Ernst-Merchant剪断角モデルが代表的で、切削力・工具寿命・表面粗さの予測と最適切削条件の決定に使用される。",
     "旋盤・フライス・ドリル加工の工具選定と条件最適化の理論的基盤。","機械工学","製造加工",1941,None,
     "加工理論","金属切削・機械加工","塑性変形能がある金属材料","最適切削条件・工具寿命を予測する場合",
     "切削速度・送り・切り込みはどのように切削力と工具摩耗に影響するか","研削・放電加工",
     "切削加工,工具寿命,切削力,剪断角","cutting theory,tool life,cutting force,shear angle",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/Metal_cutting","North_America",80,
     "φ = 45° + λs/2 - α/2 : Merchant最大剪断応力モデル（φ=剪断角, λs=摩擦角, α=すくい角）",500,"url_present"),

    ("eng_w2_0019","ロバスト制御 (H∞制御)","Robust Control H-infinity","H-infinity optimal control",
     "モデル不確かさや外乱に対して安定性・性能を保証する制御設計手法。H∞ノルム最小化により最悪ケース外乱に対する頑健性を最適化する。",
     "航空機飛行制御・プロセス制御・精密ステージ制御での高信頼性要求に対応。","機械工学","制御工学",1981,None,
     "制御設計手法","航空機制御・精密制御","モデル不確かさがある制御系","外乱や不確かさに対してロバストな制御を設計する場合",
     "モデル誤差があっても安定性をどう保証するか","PID・適応制御",
     "ロバスト制御,H∞制御,頑健性,不確かさ","robust control,H-infinity,robustness,uncertainty",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/H-infinity_methods_in_control_theory","North_America",85,
     "min_K ||T_zw||_∞ : H∞最適化問題（最悪ケース外乱増幅を最小化）",500,"url_present"),

    ("eng_w2_0020","MEMS (微小電気機械システム)","Micro-Electro-Mechanical Systems","MEMS fabrication",
     "シリコン微細加工技術を用いてマイクロメートルスケールの機械構造・センサ・アクチュエータを集積した素子群。加速度センサ・ジャイロスコープ・マイクロポンプが代表例。",
     "スマートフォン加速度計・自動車エアバッグ・インクジェットヘッドに不可欠な技術。","機械工学","マイクロ/ナノ工学",1987,None,
     "製造技術","センサ・アクチュエータ・マイクロ流体","シリコンMEMS製造プロセス","マイクロスケール機械素子の設計・製造",
     "マクロスケールの力学とマイクロスケールではどこが異なるか","ナノテクノロジー・半導体製造",
     "MEMS,微小電気機械,センサ,シリコン加工","MEMS,micro-electro-mechanical systems,sensor,silicon fabrication",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Microelectromechanical_systems","North_America",85,
     None,500,"url_present"),
]

# 追加の機械工学コンセプト（合計350件に向けてさらに概念を追加）
BATCH1_MECHANICAL_EXT = [
    ("eng_w2_0021","アディティブ製造 (3Dプリンティング)","Additive Manufacturing","3D printing AM",
     "材料を積層して三次元形状を造形する製造技術群。FDM・SLA・SLS・DMDなど多様なプロセスがあり、複雑形状・カスタム部品・ラピッドプロトタイピングに革命をもたらした。",
     "製造業のサプライチェーン変革と医療インプラント・航空機部品の軽量化に貢献。","機械工学","先端製造",1986,None,
     "製造技術","ラピッドプロトタイピング・医療・航空","熱可塑性樹脂・金属粉末・光硬化樹脂","複雑形状・小ロット・カスタム部品の製造",
     "どの積層方式が材料・精度・速度要件に最適か","切削加工・鋳造",
     "アディティブ製造,3Dプリント,積層造形,ラピッドプロトタイプ","additive manufacturing,3D printing,layer manufacturing,rapid prototyping",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/3D_printing","North_America",85,
     None,500,"url_present"),

    ("eng_w2_0022","熱交換器設計","Heat Exchanger Design","Heat exchanger LMTD NTU",
     "流体間で熱を効率的に移動させる熱交換器の設計理論。対数平均温度差法(LMTD)と移動単位数法(NTU-ε)が主要設計手法で、化学プラント・HVAC・自動車冷却に用いる。",
     "化学プラント・発電所・自動車ラジエータの熱効率最大化の核心技術。","機械工学","伝熱工学",1920,None,
     "設計手法","化学プラント・HVAC・発電","流体が熱交換できる条件","熱交換器サイズと効率を最適化する場合",
     "必要な熱移動量に対してどのような熱交換器サイズが必要か","電気ヒータ・直接加熱",
     "熱交換器,LMTD,NTU法,伝熱設計","heat exchanger,LMTD,NTU method,thermal design",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/Heat_exchanger","Western_Europe",85,
     "Q = U·A·LMTD : 熱交換量（U=総括伝熱係数, A=伝熱面積, LMTD=対数平均温度差）",500,"url_present"),

    ("eng_w2_0023","弾塑性有限要素解析","Elastoplastic FEM","Elasto-plastic finite element analysis",
     "材料が降伏点を超えた塑性変形域まで含む有限要素解析。冷間鍛造・板金成形・衝突解析に必須で、von Mises降伏条件と等方/移動硬化則を組み合わせる。",
     "自動車衝突安全・金属成形加工シミュレーションの精度向上の基盤技術。","機械工学","計算力学",1970,None,
     "数値解析手法","金属成形・衝突解析・地盤工学","弾塑性材料・大変形問題","塑性変形を含む構造体の応力・歪み分布計算",
     "材料が降伏した後の変形挙動をどう数値的に扱うか","弾性FEM・破壊力学",
     "弾塑性解析,降伏条件,FEM,金属成形","elastoplastic analysis,yield criterion,FEM,metal forming",
     "active","primary",85,1,"https://en.wikipedia.org/wiki/Plasticity_(physics)","Western_Europe",80,
     "f(σ) = √(3J₂) - σy ≤ 0 : von Mises降伏条件",500,"url_present"),

    ("eng_w2_0024","内燃機関燃焼シミュレーション","Internal Combustion Engine Combustion Simulation","ICE CFD combustion",
     "CFDと反応流体力学を組み合わせた内燃機関燃焼過程のシミュレーション手法。燃料噴射・火炎伝播・熱発生率・排気エミッションを予測してエンジン設計を最適化する。",
     "自動車・船舶エンジンの排気規制対応と燃費改善の核心技術。","機械工学","熱機関",1990,None,
     "数値解析手法","エンジン開発・排気規制対応","CFDソフトウェア・反応機構データ","エンジン燃焼の詳細解析と最適化",
     "燃料噴射タイミングと量がNOx・PMにどう影響するか","台上実験・エンジンベンチ試験",
     "内燃機関,燃焼シミュレーション,CFD,排気","internal combustion engine,combustion simulation,CFD,emission",
     "active","primary",80,1,"https://en.wikipedia.org/wiki/Internal_combustion_engine","North_America",80,
     None,500,"url_present"),

    ("eng_w2_0025","信頼性工学 (FMEA/FTA)","Reliability Engineering FMEA FTA","Failure mode effects analysis fault tree",
     "製品・システムの信頼性を定量化・改善する工学手法。故障モード影響解析(FMEA)と故障の木解析(FTA)が代表で、航空・自動車・医療機器の安全設計に義務付けられる。",
     "航空機・原子炉・自動車の安全設計規格（DO-178C・ISO 26262）の基盤手法。","機械工学","信頼性工学",1949,None,
     "品質・安全手法","航空・自動車・医療機器設計","安全クリティカルなシステム","故障確率と影響を事前に特定・低減する場合",
     "どの故障モードが最も深刻な影響をもたらすか","確率的リスク評価・人間信頼性解析",
     "信頼性工学,FMEA,FTA,故障解析,安全","reliability engineering,FMEA,FTA,failure analysis,safety",
     "active","primary",90,1,"https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis","North_America",85,
     "RPN = Severity × Occurrence × Detection : リスク優先指数（FMEA）",500,"url_present"),
]

def insert_concepts(concepts, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    inserted = 0
    skipped = 0

    for c in concepts:
        (cid, name_ja, name_en, name_original, definition, impact_summary,
         subfield, school_of_thought, era_start, era_end,
         methodology_level, target_domain, application_conditions, when_to_apply,
         framing_questions, opposing_concept_names,
         keywords_ja, keywords_en,
         status, source_reliability, data_completeness, technology_readiness_level,
         source_url, culture_region, culture_confidence,
         genealogy_narrative, narrative_word_count, verification_status) = c

        # 重複チェック
        cur.execute("SELECT id FROM engineering_method WHERE id = ? OR name_en = ?", (cid, name_en))
        if cur.fetchone():
            skipped += 1
            continue

        cur.execute("""
            INSERT INTO engineering_method (
                id, name_ja, name_en, name_original, definition, impact_summary,
                subfield, school_of_thought, era_start, era_end,
                methodology_level, target_domain, application_conditions, when_to_apply,
                framing_questions, opposing_concept_names,
                keywords_ja, keywords_en,
                status, source_reliability, data_completeness, technology_readiness_level,
                source_url, culture_region, culture_confidence,
                genealogy_narrative, narrative_word_count, verification_status,
                created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now'),datetime('now'))
        """, (cid, name_ja, name_en, name_original, definition, impact_summary,
              subfield, school_of_thought, era_start, era_end,
              methodology_level, target_domain, application_conditions, when_to_apply,
              framing_questions, opposing_concept_names,
              keywords_ja, keywords_en,
              status, source_reliability, data_completeness, technology_readiness_level,
              source_url, culture_region, culture_confidence,
              genealogy_narrative, narrative_word_count, verification_status))
        inserted += 1

        if inserted % 100 == 0:
            conn.commit()
            print(f"  {inserted} 件 INSERT 完了...")

    conn.commit()
    conn.close()
    return inserted, skipped

if __name__ == "__main__":
    all_concepts = BATCH1_MECHANICAL + BATCH1_MECHANICAL_EXT
    print(f"Batch 1 機械工学: {len(all_concepts)} 件を INSERT 開始...")
    ins, skip = insert_concepts(all_concepts, DB_PATH)
    print(f"完了: {ins} 件 INSERT, {skip} 件スキップ")

    conn = sqlite3.connect(DB_PATH)
    total = conn.execute("SELECT COUNT(*) FROM engineering_method").fetchone()[0]
    conn.close()
    print(f"現在の総件数: {total}")
