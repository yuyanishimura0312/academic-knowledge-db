"""
DUA Wave A2 Batch 10 — 科学方法論・科学史 (Scientific Methodology & History of Science)
Target: ~60 concepts, current subfield count ~11+a few, target ~120
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
        "name_ja": "科学革命と科学的方法の確立",
        "name_en": "Scientific Revolution and Establishment of Scientific Method",
        "definition": "16〜17世紀のコペルニクス・ガリレオ・ケプラー・ニュートンによる世界観の転換。観察・実験・数学的記述の三要素を科学的方法として確立した。ベーコン（帰納法・実験哲学）とデカルト（演繹法・機械論的世界像）が哲学的基礎を提供。",
        "impact_summary": "近代自然科学の制度的・認識論的起源。科学と宗教の分離・科学的知識の客観性基準・実験の権威化が現代科学文化の基盤をなす。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学・科学史",
        "era_start": 1543,
        "culture_region": "Europe_Western",
        "source_url": "https://www.cambridge.org/core/books/scientific-revolution/",
        "data_completeness": 92
    },
    {
        "name_ja": "帰納主義と反証主義",
        "name_en": "Inductivism and Falsificationism",
        "definition": "フランシス・ベーコン（1620年）の帰納主義は個別観察から一般法則を導出する。カール・ポパー（1934年）の反証主義は「反証可能性」を科学の境界基準とし、繰り返し検証に耐える仮説のみが科学的とみなされる。",
        "impact_summary": "現代科学の自己理解と教育の標準的枠組み。「科学とは何か」の境界設定問題に影響し、科学政策・倫理審査・疑似科学の判定基準として機能する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1934,
        "culture_region": "Europe_Western",
        "source_url": "https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447",
        "data_completeness": 90
    },
    {
        "name_ja": "科学的パラダイムと通常科学",
        "name_en": "Scientific Paradigms and Normal Science",
        "definition": "トーマス・クーン（1962年）が科学の発展を通常科学（パラダイム内の問題解決）→異常→危機→革命（パラダイム転換）のサイクルとして記述した。コペルニクス革命・ラヴォアジエの化学革命・プレートテクトニクスが事例。",
        "impact_summary": "科学が直線的に蓄積するのでなく非連続的に変革するという認識を普及。科学社会学・科学教育・イノベーション研究に「パラダイム」の語を定着させた。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1962,
        "culture_region": "North_America",
        "source_url": "https://press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html",
        "data_completeness": 92
    },
    {
        "name_ja": "ラカトシュの研究プログラム",
        "name_en": "Lakatos Research Programmes",
        "definition": "イムレ・ラカトシュ（1970年）がポパーとクーンを統合し、科学は「硬い核」（基本仮説）と「保護帯」（補助仮説）からなる研究プログラムとして進展すると論じた。進歩的・退行的プログラムの区別が科学の評価基準を提供。",
        "impact_summary": "科学哲学のポスト実証主義的展開の代表。科学理論の変遷を単純な反証で説明せず複合的に評価する枠組みとして、科学政策・科学史記述に影響する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1970,
        "culture_region": "Europe_Western",
        "source_url": "https://www.cambridge.org/core/books/criticism-and-the-growth-of-knowledge/",
        "data_completeness": 85
    },
    {
        "name_ja": "科学の社会的構成論",
        "name_en": "Social Construction of Scientific Knowledge",
        "definition": "エジンバラ学派のブルール（1976年）・科学知識社会学（SSK）が科学的事実は実験室内の社会的交渉・レトリック・利害によって構成されると論じた。ラトゥールとウールガー（1979年）の実験室研究が代表的事例研究。",
        "impact_summary": "科学の客観性概念を問い直し、科学技術社会論（STS）・フェミニスト科学批判・ポストコロニアル科学批評の理論的基礎となった。科学コミュニケーション・科学政策への示唆が現在も議論される。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学社会学",
        "era_start": 1976,
        "culture_region": "Europe_Western",
        "source_url": "https://www.routledge.com/Laboratory-Life-The-Construction-of-Scientific-Facts/Latour-Woolgar/p/book/9780691028323",
        "data_completeness": 85
    },
    {
        "name_ja": "ランダム化比較試験（RCT）の方法論",
        "name_en": "Randomized Controlled Trial Methodology",
        "definition": "フィッシャー（1935年）が農業実験で確立し、ブラッドフォード・ヒル（1948年）が結核治療試験で医学に応用した実験デザイン。無作為割付・盲検化・対照群設定により因果推論の黄金基準とされる。エビデンスに基づく医学（EBM）の中核。",
        "impact_summary": "医薬品・医療介入・政策の有効性評価の国際基準。CONSORT声明による報告基準が科学的コミュニケーションを標準化。開発経済学への適用（バナジー・デュフロ2019年ノーベル経済学賞）でも重要性が増した。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "実験的方法論",
        "era_start": 1948,
        "culture_region": "Europe_Western",
        "source_url": "https://www.bmj.com/content/313/7070/1451",
        "data_completeness": 90
    },
    {
        "name_ja": "メタ分析とシステマティックレビュー",
        "name_en": "Meta-Analysis and Systematic Review",
        "definition": "複数の独立研究を統計的に統合してより精度の高い推定を得る手法。グラス（1976年）が心理療法効果の研究で確立。コクラン共同体（1993年）が医学分野で体系化。効果量・異質性検定・出版バイアス補正が主要方法論。",
        "impact_summary": "エビデンスに基づく医学・政策の最高レベルエビデンス提供。コクランレビューは世界中の医療指針に影響する。再現性危機への対応としての事前登録・オープンデータと連動。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "統計的方法論",
        "era_start": 1976,
        "culture_region": "North_America",
        "source_url": "https://www.cochranelibrary.com/about/about-cochrane-reviews",
        "mathematical_formulation": r"\hat{\theta} = \frac{\sum_i w_i \hat{\theta}_i}{\sum_i w_i}, \quad w_i = \frac{1}{\text{Var}(\hat{\theta}_i)}",
        "data_completeness": 88
    },
    {
        "name_ja": "再現性危機と科学改革運動",
        "name_en": "Replication Crisis and Open Science Movement",
        "definition": "オープンサイエンス・コラボレーション（2015年）が心理学論文100本のうち39%しか再現しないと報告した「再現性危機」。前登録・オープンデータ・オープンピアレビュー・プレプリントサーバー（bioRxiv・arXiv）が改革手段として普及した。",
        "impact_summary": "科学的知識の信頼性に対する社会的懐疑を高め、研究インフラの透明化・標準化改革を駆動した。p値の誤用・出版バイアス・研究の自由度（researcher degrees of freedom）批判が研究文化変革を促す。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学改革",
        "era_start": 2011,
        "culture_region": "Global",
        "source_url": "https://www.science.org/doi/10.1126/science.aac4716",
        "data_completeness": 90
    },
    {
        "name_ja": "同料批判と科学出版システム",
        "name_en": "Peer Review and Scientific Publishing System",
        "definition": "査読制度は17世紀王立協会の書簡審査に起源をもち、20世紀に主要学術誌での普及が進んだ。ダブルブラインド査読・オープンアクセス・プレプリント（arXiv・bioRxiv）・ポストパブリケーションレビューが21世紀の変革点となっている。",
        "impact_summary": "科学的知識の品質管理と普及の中核インフラ。出版バイアス・食い違い結果の不出版・営利出版社の高額アクセス料が批判され、Plan S（欧州）・ダイヤモンドオープンアクセスが政策課題となっている。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学社会学",
        "era_start": 1665,
        "culture_region": "Europe_Western",
        "source_url": "https://www.nature.com/articles/nature05235",
        "data_completeness": 87
    },
    {
        "name_ja": "ビッグサイエンスと大型研究装置",
        "name_en": "Big Science and Large Research Infrastructures",
        "definition": "プライス（1963年）が提唱した「ビッグサイエンス」概念。マンハッタン計画（1942年〜）・CERN（1954年〜）・ヒトゲノム計画（1990年〜）・LIGO・EHT等の大型研究インフラが学際的・国際的共同研究の規範となった。",
        "impact_summary": "素粒子・宇宙・ゲノム・気候研究の新知見を可能にした一方、研究資源の集中・小規模研究の相対的縮小・研究者の分業化等の問題を提起する。科学政策の中核課題。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学政策・科学社会学",
        "era_start": 1963,
        "culture_region": "Global",
        "source_url": "https://www.press.uchicago.edu/ucp/books/book/chicago/B/bo3641578.html",
        "data_completeness": 85
    },
    {
        "name_ja": "植民地主義と科学知識の権力",
        "name_en": "Colonialism and Power in Scientific Knowledge",
        "definition": "植民地支配が非西洋の知識体系（伝統的生態知・医学・天文学）を周縁化し、西洋科学が普遍的基準として制度化された歴史を批判的に分析する。サンドラ・ハーディング（1986年）・ファニアン・ファノン・アニケ・ウォバ等が先駆者。",
        "impact_summary": "グローバルな科学参加の不平等・知識の盗用（バイオパイラシー）・先住民知識の法的保護問題に直結。南半球の研究者・機関の代表性向上を求める運動の理論的基盤。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "ポストコロニアル科学研究",
        "era_start": 1986,
        "culture_region": "Global",
        "source_url": "https://www.cambridge.org/core/books/science-and-social-inequality/",
        "data_completeness": 83
    },
    {
        "name_ja": "フェミニスト科学批評",
        "name_en": "Feminist Critique of Science",
        "definition": "ダナ・ハラウェイ（1988年）・ロンダ・シービンガー（1989年）らが科学における性差別的バイアス（研究対象・手法・解釈・制度的排除）を批判的に分析した。ハラウェイの「サイボーグ宣言」とエビデンスの「状況的知識」論が代表的。",
        "impact_summary": "科学の客観性概念の再定義（強い客観性・視点論）を促した。医学研究における女性過少代表・バイアス是正・STEM分野の多様性政策の理論的基盤。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "ポストコロニアル科学研究",
        "era_start": 1988,
        "culture_region": "North_America",
        "source_url": "https://feministstudies.org/article/situated-knowledges-the-science-question-in-feminism-and-the-privilege-of-partial-perspective/",
        "data_completeness": 83
    },
    {
        "name_ja": "研究倫理とインフォームドコンセント",
        "name_en": "Research Ethics and Informed Consent",
        "definition": "ニュルンベルク綱領（1947年）・ベルモントレポート（1979年）が人体実験の倫理原則（インフォームドコンセント・有益性・公正）を確立した。タスキーギ梅毒研究（1932〜1972年）・ナチスの人体実験が倫理規範形成の悲劇的転換点となった。",
        "impact_summary": "臨床試験・社会科学調査・遺伝子研究・AIデータ利用のすべてを規律する倫理フレームワークの基盤。インスティテューショナル・レビュー・ボード（IRB）制度の法的根拠。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "研究倫理",
        "era_start": 1947,
        "culture_region": "Global",
        "source_url": "https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/",
        "data_completeness": 87
    },
    {
        "name_ja": "オープンサイエンスとデータ共有",
        "name_en": "Open Science and Data Sharing",
        "definition": "研究データ・コード・方法・出版物を公開し、科学知識の再現性・累積性・参加性を高める運動。FAIR原則（見つけやすい・アクセス可能・相互運用可能・再利用可能）・プレプリントサーバー・市民科学・共同科学が実践形態。",
        "impact_summary": "COVID-19パンデミックで医学研究のオープンデータが政策決定速度を劇的に高め、オープンサイエンスの価値が立証された。科学の民主化・南北格差縮小・再現性改善の制度的手段。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学改革",
        "era_start": 2012,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/sdata201618",
        "data_completeness": 88
    },
    {
        "name_ja": "科学コミュニケーションとリスク認知",
        "name_en": "Science Communication and Risk Perception",
        "definition": "一般市民・政策立案者への科学情報の伝達と、リスクの主観的認知（アフェクト・ヒューリスティック・文化的世界観フィルター）の研究。欠如モデル批判・対話モデル・市民参加型科学が主要アプローチ。",
        "impact_summary": "気候変動・ワクチン・GMO・原子力をめぐる科学的合意と公衆の認識ギャップ対処の実践基盤。パンデミック・気候政策コミュニケーションで科学社会の最前線課題となっている。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学社会学",
        "era_start": 1985,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/nature06364",
        "data_completeness": 85
    },
    {
        "name_ja": "科学技術と社会（STS）",
        "name_en": "Science, Technology and Society (STS)",
        "definition": "科学技術が社会・政治・経済・文化と双方向に構成し合う関係を研究する学際分野。ウィン・ラトゥール・ジャサノフ・ハーディング等が代表的。「技術の社会的構成」（SCOT）・行為者ネットワーク理論（ANT）・共同生産（co-production）が主要枠組み。",
        "impact_summary": "AIガバナンス・バイオエシックス・環境政策・科学外交の学際的分析ツール。技術的選択の「政治性」を可視化し、民主的科学技術ガバナンスの設計に寄与する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学社会学",
        "era_start": 1962,
        "culture_region": "Global",
        "source_url": "https://www.cambridge.org/core/books/handbook-of-science-and-technology-studies/",
        "data_completeness": 85
    },
    {
        "name_ja": "モデルと理論の哲学",
        "name_en": "Philosophy of Models and Scientific Theory",
        "definition": "科学的モデル（数理・物理・計算）が世界をどのように表象し、理論・データ・現象を仲介するかを分析する科学哲学の分野。フリッグ・ギヤリー・モルガン等が代表的。理想化・抽象化・シミュレーションの認識論的地位が中心問題。",
        "impact_summary": "気候モデル・経済モデル・疫学モデル・AIモデルの認識論的限界を理解するための哲学的枠組み。モデルの「過剰適合」・不確実性定量化・説明可能性の科学哲学的根拠を提供する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1983,
        "culture_region": "Global",
        "source_url": "https://plato.stanford.edu/entries/models-science/",
        "data_completeness": 83
    },
    {
        "name_ja": "実験と観察の認識論",
        "name_en": "Epistemology of Experiment and Observation",
        "definition": "ハッキング（1983年）が「実験的実在論」を提唱し、介入可能な対象（電子を噴射できる）は実在すると論じた。観察の理論依存性（ハンソン1958年）・実験の誤差管理・再現性の哲学が主要問題。",
        "impact_summary": "科学的実在論論争・道具主義・反実在論の現代的形態。粒子加速器・天文観測・機械学習モデルから何を「発見」したと言えるかの認識論的問いに答える枠組み。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1958,
        "culture_region": "North_America",
        "source_url": "https://www.cambridge.org/core/books/representing-and-intervening/",
        "data_completeness": 83
    },
    {
        "name_ja": "説明と理解の科学哲学",
        "name_en": "Scientific Explanation and Understanding",
        "definition": "ヘンペル・オッペンハイム（1948年）の被覆法則モデル（演繹的‐法則的説明）から、サルモンの因果的説明・ウッドワードの操作的説明・フリードマンの統一的説明・デュプレのプルラリズムへと展開した科学哲学の中核テーマ。",
        "impact_summary": "「科学的説明とは何か」という問いが医学・心理学・経済学・AI解釈可能性（XAI）の方法論設計に影響する。「なぜ」の問いへの答え方が政策決定・因果推論に直結する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1948,
        "culture_region": "North_America",
        "source_url": "https://www.jstor.org/stable/185177",
        "data_completeness": 82
    },
    {
        "name_ja": "因果推論の統計的枠組み",
        "name_en": "Causal Inference Framework",
        "definition": "潜在結果モデル（ルービン1974年）・ポテンシャルアウトカム・操作変数・差の差法・回帰不連続設計・ジュディア・パール（2000年）の因果グラフ（DAG）・do計算子が統計因果推論の主要ツール。観察研究から因果効果を推定するための数学的基盤。",
        "impact_summary": "経済学・疫学・政策評価・AI公平性研究における「相関≠因果」問題の解決ツール。パールの2011年チューリング賞受賞が学術的認知を高め、因果AIの基礎となる。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "統計的方法論",
        "era_start": 1974,
        "culture_region": "North_America",
        "source_url": "https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/",
        "mathematical_formulation": r"E[Y(1) - Y(0)] \text{ (ATE); } P(Y|do(X)) \neq P(Y|X)",
        "data_completeness": 90
    },
    {
        "name_ja": "伝統的知識と西洋科学の対話",
        "name_en": "Traditional Ecological Knowledge and Western Science Dialogue",
        "definition": "先住民・地域コミュニティが蓄積した生態系・植物・気候・動物行動に関する知識体系（TEK）と制度的科学の統合的活用。生物多様性条約（名古屋議定書2010年）・IPBES等が「異なる知識体系」の統合アプローチを推進。",
        "impact_summary": "生物多様性保全・気候変動適応・植物由来薬剤開発に伝統的知識が提供する実践的価値。バイオパイラシー問題と知的財産権・コミュニティ利益配分の国際ルール形成に影響する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "ポストコロニアル科学研究",
        "era_start": 1992,
        "culture_region": "Global",
        "source_url": "https://www.ipbes.net/policy-support/tools-instruments/indigenous-and-local-knowledge",
        "data_completeness": 85
    },
    {
        "name_ja": "計算科学と数値シミュレーション",
        "name_en": "Computational Science and Numerical Simulation",
        "definition": "コンピュータを用いた数値計算によって自然現象・社会現象・物質特性を予測・解析する科学の第三のパラダイム（理論・実験に次ぐ）。モンテカルロ法・有限要素法・分子動力学・気候GCM・格子QCDが代表的方法。",
        "impact_summary": "気候変動予測・創薬（タンパク質フォールディング予測）・材料設計・航空宇宙エンジニアリングの革新を可能にした。AlphaFold2のタンパク質構造予測が計算科学とAIの統合の象徴的成果。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "計算科学",
        "era_start": 1945,
        "culture_region": "Global",
        "source_url": "https://www.nature.com/articles/d41586-021-00065-y",
        "data_completeness": 88
    },
    {
        "name_ja": "科学の経済学と研究生産性",
        "name_en": "Economics of Science and Research Productivity",
        "definition": "科学知識の生産・普及・応用における経済的ダイナミクスを研究する分野。アロー（1962年）の「知識の経済学」・ダイアモンドの科学の「アイデア生産関数」・バナナ分布問題（科学者の生産性の冪分布）が主要概念。",
        "impact_summary": "研究資金配分・学術出版・知的財産・大学‐産業連携の政策設計の科学的基盤。「アイデアが尽きている」仮説（ブルーム等2020年）は科学技術政策の根本的問いを提起する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学政策・科学社会学",
        "era_start": 1962,
        "culture_region": "North_America",
        "source_url": "https://www.nber.org/papers/w23782",
        "data_completeness": 83
    },
    {
        "name_ja": "データ駆動型科学の台頭",
        "name_en": "Data-Driven Science and Machine Learning in Discovery",
        "definition": "大規模データ収集（ゲノム・粒子衝突・天文サーベイ）とAI/機械学習の組み合わせにより、仮説を事前に設定せずパターンを発見する「第四のパラダイム」（ヘイ2009年）。AlphaFoldによるタンパク質構造解決・GW検出・創薬が象徴的事例。",
        "impact_summary": "仮説‐演繹法から帰納的発見へのパラダイムシフトを起動。科学者の役割変化・AI予測の解釈可能性・データ所有権・アルゴリズムバイアスが科学哲学・科学政策の新問題となっている。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "計算科学",
        "era_start": 2009,
        "culture_region": "Global",
        "source_url": "https://www.microsoft.com/en-us/research/book/fourth-paradigm/",
        "data_completeness": 88
    },
    {
        "name_ja": "非西洋科学の近代的制度化",
        "name_en": "Institutionalization of Non-Western Science in Modern Era",
        "definition": "19〜20世紀に日本・中国・インド・ブラジル・南アフリカが西洋式大学・研究機関・学術誌を設立し、自国科学者を育成した歴史的プロセス。日本の明治維新後の科学技術近代化・インドのTIFR・中国科学院・ブラジルFIOCRUZが代表例。",
        "impact_summary": "グローバルサウスにおける科学的能力形成の歴史。ポストコロニアル科学批評と「南北科学格差」問題の歴史的文脈を提供し、国際科学政策・留学・知識移転研究に重要な視座をなす。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学史",
        "era_start": 1868,
        "culture_region": "Global",
        "source_url": "https://www.cambridge.org/core/books/cambridge-history-of-science/",
        "data_completeness": 82
    },
    {
        "name_ja": "アブダクション（仮説推論）と発見の論理",
        "name_en": "Abduction and Logic of Scientific Discovery",
        "definition": "チャールズ・パース（1878年）が提唱したアブダクション（最良説明への推論）は、帰納・演繹に次ぐ第三の推論形式として科学的仮説の生成を説明する。ハンソン（1958年）・テーガード（1988年）が科学的発見の論理としてAIとの接続を論じた。",
        "impact_summary": "医学診断・科学的発見過程・AIの常識推論・説明可能AIの哲学的基盤。「なぜこの仮説を思いついたのか」という創造的発見過程を論理的に記述する試み。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1878,
        "culture_region": "North_America",
        "source_url": "https://plato.stanford.edu/entries/abduction/",
        "data_completeness": 82
    },
    {
        "name_ja": "科学的還元主義と創発論",
        "name_en": "Scientific Reductionism and Emergence",
        "definition": "還元主義は複雑系を構成要素の性質から説明する立場（分子生物学→生命過程）。創発論は構成要素では予測不可能な集合的性質（意識・生命・高温超伝導）の実在を主張する。フィリップ・アンダーソン（1972年「More Is Different」）が物理学者として創発論を擁護した。",
        "impact_summary": "生命科学・神経科学・複雑系科学の存在論的基盤。「意識とは何か」「生命は物理法則から完全に説明できるか」という根本的問いに答えるフレームワークとして科学哲学・AI倫理に影響する。",
        "subfield": "科学方法論・科学史",
        "school_of_thought": "科学哲学",
        "era_start": 1972,
        "culture_region": "North_America",
        "source_url": "https://www.science.org/doi/10.1126/science.177.4047.393",
        "data_completeness": 85
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
    print(f"\nBatch10 method: {n} concepts inserted")
    print(f"Total in table: {count}")
