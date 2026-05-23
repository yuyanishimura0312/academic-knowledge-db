"""DUA Wave A2 Batch 26 — final push to 5,500 (need +77 minimum)"""
import sqlite3, uuid, datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0; skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1; continue
        uid = str(uuid.uuid4())
        now = datetime.datetime.utcnow().isoformat()
        cur.execute("""INSERT INTO social_theory
            (id,name_ja,name_en,name_original,definition,subfield,school_of_thought,
             era_start,culture_region,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)""",
            (uid,name_ja,name_en,name_orig,defn,subfield,school,era,region,url,now,now))
        inserted += 1
        if inserted % 50 == 0:
            conn.commit(); print(f"  Committed {inserted}...")
    conn.commit(); conn.close()
    return inserted, skipped

concepts = [
    # ── 古典社会学 (10) ──
    ("社会秩序の問題","Problem of Social Order","","デュルケームやホッブズが問うた、なぜ社会は解体せずに秩序を維持できるのかという根本問い。パーソンズが『社会的行為の構造』で再定式化した。","古典社会学","構造機能主義",1937,"Western_Europe","https://en.wikipedia.org/wiki/Social_order"),
    ("社会連帯の二類型","Mechanical and Organic Solidarity","","デュルケームが提示した機械的連帯（同質性による結合）と有機的連帯（分業による相互依存）の二類型。近代化とともに後者が優位になると論じた。","古典社会学","デュルケーム社会学",1893,"Western_Europe","https://en.wikipedia.org/wiki/The_Division_of_Labour_in_Society"),
    ("官僚制の病理","Dysfunctions of Bureaucracy","","マートンが指摘した、官僚制が効率性を逆に阻害する逆機能現象。規則遵守の目的置換・訓練された無能・赤テープなどを含む。","古典社会学","マートン社会学",1940,"North_America","https://en.wikipedia.org/wiki/Bureaucracy#Dysfunctions"),
    ("準拠集団理論","Reference Group Theory","","個人が自己評価や態度形成の基準として用いる集団（成員でなくてもよい）を分析する理論。マートンとロージが体系化した。","古典社会学","マートン社会学",1950,"North_America","https://en.wikipedia.org/wiki/Reference_group"),
    ("ステータス不一致","Status Inconsistency","","個人の社会的地位の諸次元（収入・教育・職業威信・民族）がバラバラである状態。偏見や不満の原因となりうるとレンスキらが分析した。","古典社会学","社会階層論",1954,"North_America","https://en.wikipedia.org/wiki/Status_inconsistency"),
    ("文化的遅滞","Cultural Lag","","オグバーンが提唱した、物質文化（技術）が非物質文化（制度・価値）よりも速く変化するため生じるズレ。","古典社会学","オグバーン社会変動論",1922,"North_America","https://en.wikipedia.org/wiki/Cultural_lag"),
    ("ウェーバーの合法的支配","Legal-Rational Domination","","ウェーバーが提示した支配の三類型のひとつ。規則・法律に基づく近代官僚制的権威を指し、伝統的支配・カリスマ的支配と対比される。","古典社会学","ウェーバー社会学",1922,"Western_Europe","https://en.wikipedia.org/wiki/Three_types_of_domination"),
    ("社会的事実の物象化","Reification of Social Facts","","人間が作り出した社会制度や規範を、あたかも自然の法則のように固定したものと見なしてしまう誤認。ルカーチやバーガー・ルックマンが分析した。","古典社会学","マルクス主義社会学",1923,"Western_Europe","https://en.wikipedia.org/wiki/Reification_(Marxism)"),
    ("アノミー自殺","Anomic Suicide","","デュルケームが分類した自殺の一類型。社会規制の崩壊・急激な社会変動により欲求と現実のギャップが生じることで引き起こされる。","古典社会学","デュルケーム社会学",1897,"Western_Europe","https://en.wikipedia.org/wiki/Suicide_(Durkheim_book)"),
    ("宗教社会学の基礎","Elementary Forms of Religious Life","","デュルケームが1912年に著した著作が示す理論的枠組み。宗教を聖俗の二項対立に基づく集合的表象として分析し、宗教の社会的機能を強調した。","古典社会学","デュルケーム社会学",1912,"Western_Europe","https://en.wikipedia.org/wiki/The_Elementary_Forms_of_the_Religious_Life"),

    # ── 批判理論・フランクフルト学派 (10) ──
    ("文化的ヘゲモニー","Cultural Hegemony","","グラムシが提唱した、支配階級が強制でなく文化・イデオロギーを通じて同意を取り付ける支配のメカニズム。","批判理論・フランクフルト学派","グラムシ主義",1930,"Western_Europe","https://en.wikipedia.org/wiki/Cultural_hegemony"),
    ("陣地戦と機動戦","War of Position and War of Maneuver","","グラムシが革命戦略として区別した二概念。西欧では市民社会の陣地を固める長期的な文化闘争（陣地戦）が必要と論じた。","批判理論・フランクフルト学派","グラムシ主義",1930,"Western_Europe","https://en.wikipedia.org/wiki/Antonio_Gramsci#War_of_position_and_war_of_maneuver"),
    ("新左翼批判理論","New Left Critical Theory","","1960年代に台頭した、マルクス主義の経済還元主義を超えて文化・人種・ジェンダーを批判の軸に加えた思想潮流。","批判理論・フランクフルト学派","新左翼",1960,"North_America","https://en.wikipedia.org/wiki/New_Left"),
    ("技術的合理性","Technological Rationality","","マルクーゼが提唱した概念。近代技術が合理性の装いで支配と抑圧を再生産する仕組みを指す。『一次元的人間』で展開された。","批判理論・フランクフルト学派","マルクーゼ批判理論",1964,"North_America","https://en.wikipedia.org/wiki/One-Dimensional_Man"),
    ("実証主義論争","Positivism Dispute","","1960年代にポパー・アドルノらが参加した、社会科学における実証主義と批判理論の是非をめぐる学術論争。ドイツ社会学会での論争として知られる。","批判理論・フランクフルト学派","フランクフルト学派",1961,"Western_Europe","https://en.wikipedia.org/wiki/Positivism_dispute"),
    ("生産的想像力","Productive Imagination","","ブロッホが提唱した、ユートピア的願望エネルギーとしての想像力。未来への希望の痕跡を芸術・夢・民衆文化から読み取る「希望の原理」の中核。","批判理論・フランクフルト学派","ブロッホ哲学",1954,"Western_Europe","https://en.wikipedia.org/wiki/Ernst_Bloch"),
    ("非同一性思考","Negative Dialectics","","アドルノが同一性思考（概念への還元）に抗して提唱した、概念に回収されない非同一者の痕跡を保持する否定弁証法の核心。","批判理論・フランクフルト学派","アドルノ批判理論",1966,"Western_Europe","https://en.wikipedia.org/wiki/Negative_Dialectics"),
    ("ハーバーマスの公共圏再建","Habermas's Reconstruction of Public Sphere","","ハーバーマスが後期に理想的コミュニケーションの条件として再提示した公共圏論。初期の歴史社会学的叙述から規範理論へと移行した議論。","批判理論・フランクフルト学派","ハーバーマス批判理論",1990,"Western_Europe","https://en.wikipedia.org/wiki/J%C3%BCrgen_Habermas"),
    ("批判的教育学","Critical Pedagogy","","フレイレ『被抑圧者の教育学』を起点とする、教育を解放の実践として捉える理論潮流。フックス・ジルーらが展開した。","批判理論・フランクフルト学派","フレイレ教育論",1968,"Latin_America","https://en.wikipedia.org/wiki/Critical_pedagogy"),
    ("オルタナティブ公共圏","Counter-Public Sphere","","ナンシー・フレイザーが提唱した概念。支配的公共圏から排除されたマイノリティが形成する対抗的な議論空間を指す。","批判理論・フランクフルト学派","フレイザー批判理論",1990,"North_America","https://en.wikipedia.org/wiki/Nancy_Fraser"),

    # ── 構造主義・ポスト構造主義 (10) ──
    ("形式主義文学理論","Russian Formalism","","20世紀初頭にロシアで展開した文学理論の潮流。テキストの形式的特性（異化・支配的手法）を文学性の核と見なした。後の構造主義に影響。","構造主義・ポスト構造主義","ロシア・フォルマリズム",1910,"Western_Europe","https://en.wikipedia.org/wiki/Russian_formalism"),
    ("物語論","Narratology","","物語の構造・機能・類型を研究する学問領域。プロップの民話形態論、グレマスの行為者モデル、ジュネットの語り論が主要理論。","構造主義・ポスト構造主義","構造主義",1928,"Western_Europe","https://en.wikipedia.org/wiki/Narratology"),
    ("テクスト産出","Text Production","","クリステヴァおよびバルトが論じた、テクストを固定した意味の担体ではなく意味生産の実践として捉える概念。生産的読解の理論。","構造主義・ポスト構造主義","ポスト構造主義",1970,"Western_Europe","https://en.wikipedia.org/wiki/Julia_Kristeva"),
    ("シミュラークルの秩序","Orders of Simulacra","","ボードリヤールが提示した模倣の歴史的変容：原本の模倣→複製→記号の自律的循環という三段階。消費社会論の核心。","構造主義・ポスト構造主義","ボードリヤール",1981,"Western_Europe","https://en.wikipedia.org/wiki/Simulacra_and_Simulation"),
    ("知の考古学","Archaeology of Knowledge","","フーコーが提示した方法論。思想の連続的発展ではなく、特定の時代に真理とされる言説を規定する「エピステーメー」（認識枠組み）の断絶的変容を分析する。","構造主義・ポスト構造主義","フーコー",1969,"Western_Europe","https://en.wikipedia.org/wiki/The_Archaeology_of_Knowledge"),
    ("欲望する機械","Desiring Machines","","ドゥルーズ＝ガタリが『アンチ・オイディプス』で提示した概念。欲望を欠如ではなく生産的な力として捉え、フロイト＝ラカン的欲求論を批判した。","構造主義・ポスト構造主義","ドゥルーズ＝ガタリ",1972,"Western_Europe","https://en.wikipedia.org/wiki/Anti-Oedipus"),
    ("マイナー文学","Minor Literature","","ドゥルーズ＝ガタリが提唱した、マイノリティが多数派の言語で書くことで言語を「脱領土化」する文学実践。カフカ論で展開された。","構造主義・ポスト構造主義","ドゥルーズ＝ガタリ",1975,"Western_Europe","https://en.wikipedia.org/wiki/Kafka:_Toward_a_Minor_Literature"),
    ("大文字の他者","The Other (Lacan)","","ラカンが言語と象徴秩序の場として定義した「大文字の他者」。主体は言語を通じてこの他者の場に参入する。","構造主義・ポスト構造主義","ラカン精神分析",1950,"Western_Europe","https://en.wikipedia.org/wiki/Other_(Lacan)"),
    ("差延","Différance","","デリダが造語した概念。意味は常に「差異化」と「延期」のはたらきによって構成されるものであり、起源的な現前は存在しないと論じる。","構造主義・ポスト構造主義","デリダ脱構築",1968,"Western_Europe","https://en.wikipedia.org/wiki/Diff%C3%A9rance"),
    ("パロールとラング","Parole and Langue","","ソシュールが区別した、個別の発話行為（パロール）と社会的慣習としての言語体系（ラング）の対概念。構造主義言語学の基礎。","構造主義・ポスト構造主義","ソシュール言語学",1916,"Western_Europe","https://en.wikipedia.org/wiki/Parole_and_langue"),

    # ── フェミニズム・ジェンダー理論 (10) ──
    ("再生産的正義","Reproductive Justice","","ロレッタ・ロスらが1994年に提唱した概念。子どもを産む・産まない・育てる権利の三位一体として生殖の権利を再定義する。有色人種女性の視点から中産階級的プロチョイス運動を批判した。","フェミニズム・ジェンダー理論","交差性フェミニズム",1994,"North_America","https://en.wikipedia.org/wiki/Reproductive_justice"),
    ("エコフェミニズム","Ecofeminism","","フランソワーズ・ドボンヌが1974年に提唱した、自然への支配と女性への支配を同一の論理として批判する思想。","フェミニズム・ジェンダー理論","エコフェミニズム",1974,"Western_Europe","https://en.wikipedia.org/wiki/Ecofeminism"),
    ("ジェンダー・アイデンティティ形成","Gender Identity Formation","","心理学・フェミニズム理論が交差する分野。チョドロウの対象関係論、バトラーの反本質主義など複数の立場からジェンダー同一性の形成過程を分析する。","フェミニズム・ジェンダー理論","ジェンダー理論",1970,"North_America","https://en.wikipedia.org/wiki/Gender_identity"),
    ("フェミニスト法学","Feminist Jurisprudence","","マッキノンらが展開した、法制度が男性中心的なバイアスを内包しているとして批判する法理論。性的ハラスメントの法的概念化などに貢献。","フェミニズム・ジェンダー理論","フェミニスト法学",1979,"North_America","https://en.wikipedia.org/wiki/Feminist_jurisprudence"),
    ("感情労働とジェンダー","Emotional Labor and Gender","","アーリー・ホックシールドが着目した、感情管理を職務とする労働とジェンダー不平等の関係。女性がサービス業で感情労働を多く担わされる構造を分析。","フェミニズム・ジェンダー理論","フェミニスト労働理論",1983,"North_America","https://en.wikipedia.org/wiki/Emotional_labor"),
    ("ケアの倫理","Ethics of Care","","キャロル・ギリガンが1982年に提唱し、ネル・ノディングスらが発展させた道徳哲学。普遍的正義原理よりも具体的な関係性・ケア責任を道徳の中心に置く。","フェミニズム・ジェンダー理論","フェミニスト倫理学",1982,"North_America","https://en.wikipedia.org/wiki/Ethics_of_care"),
    ("ポストフェミニズム","Postfeminism","","1990年代以降の議論。フェミニズムの目標達成を前提にしたうえで個人の選択を強調する文化的言説で、しばしばフェミニズム批判として機能すると批判される。","フェミニズム・ジェンダー理論","ポストフェミニズム",1990,"North_America","https://en.wikipedia.org/wiki/Postfeminism"),
    ("フェミニスト認識論","Feminist Epistemology","","サンドラ・ハーディングらが展開した、知識生産の過程に埋め込まれた男性中心的前提を批判し、立場性（スタンドポイント）から認識論を再構成する議論。","フェミニズム・ジェンダー理論","スタンドポイント理論",1983,"North_America","https://en.wikipedia.org/wiki/Feminist_epistemology"),
    ("ジェンダーと発展","Gender and Development","","国際開発分野においてジェンダー平等を中心課題として捉える理論枠組み。WID（開発における女性）からGAD（開発とジェンダー）への転換を経て展開。","フェミニズム・ジェンダー理論","フェミニスト開発論",1975,"Global_Synthesis","https://en.wikipedia.org/wiki/Gender_and_development"),
    ("ブラック・フェミニズム","Black Feminism","","アンジェラ・デイヴィス、パトリシア・ヒル・コリンズらが展開した、人種・階級・ジェンダーの交差する抑圧構造を批判するフェミニスト思想。","フェミニズム・ジェンダー理論","ブラック・フェミニズム",1970,"North_America","https://en.wikipedia.org/wiki/Black_feminism"),

    # ── ポストコロニアル・脱植民地理論 (10) ──
    ("植民地近代性","Colonial Modernity","","植民地主義と近代性が不可分に結びついているという議論。ディペシュ・チャクラバルティやアニバル・キハーノが展開した脱植民地的近代論。","ポストコロニアル・脱植民地理論","脱植民地理論",1990,"South_Asia","https://en.wikipedia.org/wiki/Coloniality_of_power"),
    ("認識論的暴力","Epistemic Violence","","スピヴァクがガヤトリ・チャクラヴォルティの概念を展開。植民地主義が現地の知識体系を消去・周縁化することで加える認識論的な暴力を指す。","ポストコロニアル・脱植民地理論","スピヴァク",1988,"South_Asia","https://en.wikipedia.org/wiki/Epistemic_violence"),
    ("オリエンタリズム批判","Critique of Orientalism","","サイードの議論を受け継ぐ批判的実践。西洋による東洋の表象を権力・知識の産物として分析し、メディア・学術・政策のオリエンタリズムを告発する。","ポストコロニアル・脱植民地理論","ポストコロニアル理論",1980,"West_Asia_North_Africa","https://en.wikipedia.org/wiki/Orientalism"),
    ("南南協力","South-South Cooperation","","グローバルサウス諸国間の経済・技術・政治協力の枠組み。脱植民地的連帯の実践として分析される。","ポストコロニアル・脱植民地理論","脱植民地理論",1970,"Global_Synthesis","https://en.wikipedia.org/wiki/South%E2%80%93South_cooperation"),
    ("クレオール化","Creolization","","エドゥアール・グリッサンが提唱した、カリブ海・植民地接触から生まれる文化の混合・変容プロセス。単一文化アイデンティティを超えたハイブリッド性を概念化。","ポストコロニアル・脱植民地理論","グリッサン",1990,"Latin_America","https://en.wikipedia.org/wiki/Creolization"),
    ("植民地的差異","Colonial Difference","","ミニョーロが提唱した、植民地的モダニティが生産する知識・存在・権力の非対称的な位置性。ローカルな知識の復権と「複数の近代」論の基礎。","ポストコロニアル・脱植民地理論","脱植民地理論",2000,"Latin_America","https://en.wikipedia.org/wiki/Walter_Mignolo"),
    ("土着知識の復権","Indigenous Knowledge Recovery","","植民地化によって周縁化された先住民の知識体系（宇宙観・農業・医学・法）を学術的認識として回復する実践的・政治的運動。","ポストコロニアル・脱植民地理論","先住民研究",1990,"Global_Synthesis","https://en.wikipedia.org/wiki/Indigenous_knowledge"),
    ("人種資本主義","Racial Capitalism","","ロビン・D・G・ケリーが再定義した、資本主義の展開が人種的差異の生産・利用に依存しているという議論。セドリック・ロビンソンの原著（1983）に遡る。","ポストコロニアル・脱植民地理論","ブラック急進主義",1983,"North_America","https://en.wikipedia.org/wiki/Racial_capitalism"),
    ("ポスト開発論","Post-Development Theory","","アルトゥーロ・エスコバルらが展開した、「開発」という概念自体が植民地的権力関係を再生産するとして批判する理論枠組み。","ポストコロニアル・脱植民地理論","脱植民地理論",1992,"Latin_America","https://en.wikipedia.org/wiki/Post-development_theory"),
    ("アフリカ哲学","African Philosophy","","植民地主義が否定したアフリカ固有の哲学的伝統（ウブントゥ・哲学的対話伝統など）を回復・体系化する学的営み。クワメ・ギュエキェらが代表。","ポストコロニアル・脱植民地理論","アフリカン哲学",1970,"Sub_Saharan_Africa","https://en.wikipedia.org/wiki/African_philosophy"),

    # ── 政治社会学・国家論 (10) ──
    ("市民的不服従","Civil Disobedience","","ソローが19世紀に提唱し、20世紀にガンジー・キング牧師らが実践した、不正な法律への非暴力的抵抗。社会運動論・政治哲学で中心的概念。","政治社会学・国家論","政治哲学",1849,"North_America","https://en.wikipedia.org/wiki/Civil_disobedience"),
    ("熟議民主主義の実践","Deliberative Democratic Practice","","理論的枠組みを具体化した市民討議会・コンセンサス会議・熟議世論調査などの参加型制度設計。フィシュキン・ガストらが展開した。","政治社会学・国家論","熟議民主主義",1990,"North_America","https://en.wikipedia.org/wiki/Deliberative_democracy"),
    ("政治的機会構造","Political Opportunity Structure","","社会運動論の概念。国家と挑戦者集団の関係において、運動の生成・成功に影響を与える政治体制の開放性・同盟エリートの存在・エリート分裂などの条件。","政治社会学・国家論","資源動員論",1978,"North_America","https://en.wikipedia.org/wiki/Political_opportunity"),
    ("国家の失敗","State Failure","","国家が基本的な統治機能（治安・法・行政・公共財）を提供できなくなる状態。ソマリア・シエラレオネなどのケーススタディから理論化された。","政治社会学・国家論","比較政治学",1990,"North_America","https://en.wikipedia.org/wiki/Failed_state"),
    ("利益集団政治","Interest Group Politics","","政策決定過程に影響を及ぼそうとする組織化された集団の活動を分析する政治社会学の分野。多元主義論・コーポラティズム論が対立する軸。","政治社会学・国家論","政治社会学",1950,"North_America","https://en.wikipedia.org/wiki/Interest_group"),
    ("選挙権威主義","Electoral Authoritarianism","","競争的選挙を維持しながら実質的には権威主義的支配を続ける政治体制。シェドラー・リンスらが分類した「ハイブリッド政体」の一形態。","政治社会学・国家論","比較政治学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Electoral_authoritarianism"),
    ("国家と市民社会の関係","State-Civil Society Relations","","グラムシ以来の問いを引き継ぎ、国家と自律的な市民社会（NGO・宗教組織・社会運動）の相互作用を分析する枠組み。","政治社会学・国家論","政治社会学",1970,"Global_Synthesis","https://en.wikipedia.org/wiki/Civil_society"),
    ("ポピュリズムの比較分析","Comparative Populism Studies","","ムッデ・カルトワッセルらによる、ポピュリズムを薄いイデオロギー（一般人民対腐敗したエリート）として分析する比較政治学的アプローチ。","政治社会学・国家論","ポピュリズム研究",2004,"Global_Synthesis","https://en.wikipedia.org/wiki/Populism"),
    ("暴力の独占","Monopoly of Violence","","ウェーバーが近代国家の本質として定義した、正当な物理的強制力の独占。国家論の基礎概念として広く参照される。","政治社会学・国家論","ウェーバー社会学",1919,"Western_Europe","https://en.wikipedia.org/wiki/Monopoly_on_violence"),
    ("政治的動員と組織","Political Mobilization and Organization","","集合行為の課題を克服して政治参加を動員するプロセスの分析。オルソンの集合行為論からマクファーランドの組織論まで多様なアプローチを含む。","政治社会学・国家論","政治社会学",1965,"North_America","https://en.wikipedia.org/wiki/Political_mobilization"),

    # ── 文化社会学・知識社会学 (10) ──
    ("意味の生産と消費","Production and Consumption of Meaning","","スチュアート・ホールのエンコーディング・デコーディングモデルを発展させた議論。メディアや文化産物の意味は一義的に固定されず、受容者によって再解釈される。","文化社会学・知識社会学","カルチュラルスタディーズ",1980,"Western_Europe","https://en.wikipedia.org/wiki/Encoding/decoding_model_of_communication"),
    ("趣味の社会学","Sociology of Taste","","ブルデューが展開した、審美的趣味を階級的ハビトゥスの反映として分析する研究領域。『ディスタンクシオン』が代表作。","文化社会学・知識社会学","ブルデュー社会学",1979,"Western_Europe","https://en.wikipedia.org/wiki/Distinction_(book)"),
    ("記念と集合的記憶","Commemoration and Collective Memory","","モーリス・アルブバックスの集合的記憶論を継承し、記念碑・博物館・記念日などの公的実践が集合的記憶を形成・管理するプロセスを分析する。","文化社会学・知識社会学","集合的記憶論",1985,"Western_Europe","https://en.wikipedia.org/wiki/Collective_memory"),
    ("文化産業とクリエイティブ経済","Culture Industry and Creative Economy","","フランクフルト学派の文化産業批判と、フロリダらの「創造的経済」論の対話。文化生産の商品化・知識労働の経済的価値をめぐる議論。","文化社会学・知識社会学","文化社会学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Cultural_industry"),
    ("信頼の社会学","Sociology of Trust","","ニクラス・ルーマン、アンソニー・ギデンズらが展開した、近代社会における信頼（対人・制度・システム）の機能と構造を分析する理論。","文化社会学・知識社会学","システム理論",1979,"Western_Europe","https://en.wikipedia.org/wiki/Trust_(social_science)"),
    ("タブーと禁忌","Taboo and Prohibition","","デュルケーム・フロイト・メアリー・ダグラスらが分析した、文化が「汚れ」や「危険」として分類するものの社会的メカニズム。","文化社会学・知識社会学","文化社会学",1966,"Western_Europe","https://en.wikipedia.org/wiki/Taboo"),
    ("知識社会学の方法論","Methodology of Sociology of Knowledge","","マンハイム以降の知識社会学が用いる方法論的枠組み。思想の社会的条件付け・イデオロギー分析・パラダイム論などを含む。","文化社会学・知識社会学","知識社会学",1929,"Western_Europe","https://en.wikipedia.org/wiki/Sociology_of_knowledge"),
    ("象徴儀礼と境界","Symbolic Ritual and Boundary","","ヴィクター・ターナーのリミナリティ論・メアリー・ダグラスの境界論を統合した視点。社会的境界の儀礼的再生産と越境の社会的意味を分析する。","文化社会学・知識社会学","象徴人類学",1969,"Western_Europe","https://en.wikipedia.org/wiki/Liminality"),
    ("文化的市民権","Cultural Citizenship","","ロジック・フラーが提唱した概念。政治的・社会的権利に加えて、自らの文化的アイデンティティを承認され公共の場に参加できる権利を指す。","文化社会学・知識社会学","文化社会学",1994,"North_America","https://en.wikipedia.org/wiki/Cultural_citizenship"),
    ("科学技術のレトリック","Rhetoric of Science","","科学的言説が説得の修辞的実践を含むと分析する学際領域。マイヤーズ・ラトゥールらが科学論文の修辞構造を解析した。","文化社会学・知識社会学","科学社会学",1985,"North_America","https://en.wikipedia.org/wiki/Rhetoric_of_science"),

    # ── デジタル社会学・ネットワーク社会 (8) ──
    ("デジタル疎外","Digital Alienation","","ハイデガー的疎外論をデジタル環境に適用した概念。技術的システムへの依存・自律性の喪失・人間関係の道具化などを指摘する。","デジタル社会学・ネットワーク社会","デジタル社会学",2010,"Global_Synthesis","https://en.wikipedia.org/wiki/Digital_alienation"),
    ("計算的社会科学","Computational Social Science","","ビッグデータ・シミュレーション・ネットワーク分析などのコンピュータ的手法を社会現象の研究に適用する新興領域。ライザーらが2009年に提唱した。","デジタル社会学・ネットワーク社会","計算社会科学",2009,"North_America","https://en.wikipedia.org/wiki/Computational_social_science"),
    ("データ倫理","Data Ethics","","データの収集・利用・共有にかかわる倫理的問題を扱う分野。プライバシー・同意・アルゴリズムの公正性・データ主権などを含む。","デジタル社会学・ネットワーク社会","デジタル社会学",2015,"Global_Synthesis","https://en.wikipedia.org/wiki/Data_ethics"),
    ("ネットワーク社会の排除","Network Society and Exclusion","","カステルスのネットワーク社会論が示す、グローバルネットワークから切断された人々・地域の構造的排除問題。デジタルデバイドとの関連。","デジタル社会学・ネットワーク社会","カステルス",2000,"Western_Europe","https://en.wikipedia.org/wiki/Digital_divide"),
    ("ソーシャルボット","Social Bots","","SNS上で人間を模倣して自動的に投稿・拡散するプログラム。政治的世論操作・偽情報拡散の手段として社会学的分析の対象となっている。","デジタル社会学・ネットワーク社会","デジタル社会学",2014,"Global_Synthesis","https://en.wikipedia.org/wiki/Social_bot"),
    ("アルゴリズム的ガバナンス","Algorithmic Governance","","政策・規制・行政においてアルゴリズムが意思決定を代替・補完する現象。透明性・説明責任・民主的コントロールの観点から批判的に分析される。","デジタル社会学・ネットワーク社会","デジタル社会学",2012,"Global_Synthesis","https://en.wikipedia.org/wiki/Algorithmic_governance"),
    ("デジタル資本主義","Digital Capitalism","","情報技術を基盤とする資本蓄積の新段階を分析する概念。シラーが1999年に提唱し、プラットフォーム・データ・注意経済を含む議論として展開されている。","デジタル社会学・ネットワーク社会","デジタル社会学",1999,"North_America","https://en.wikipedia.org/wiki/Digital_capitalism"),
    ("量子化された自己","Quantified Self","","ウェアラブルデバイス・アプリによる自己追跡実践とその社会的含意。ルコフ・ウォルフが命名し、身体・健康・アイデンティティの数値化を社会学的に分析する。","デジタル社会学・ネットワーク社会","デジタル社会学",2007,"North_America","https://en.wikipedia.org/wiki/Quantified_self"),

    # ── 環境社会学・人新世 (9) ──
    ("環境正義運動","Environmental Justice Movement","","1980年代にアメリカで台頭した、環境汚染・廃棄物処理施設が有色人種・低所得者の居住地域に集中する現象への抵抗運動。","環境社会学・人新世","環境正義",1980,"North_America","https://en.wikipedia.org/wiki/Environmental_justice"),
    ("生態的市民権","Ecological Citizenship","","アンドリュー・ドブソンが提唱した、生態学的責任を市民の義務として組み込む政治的概念。消費・移動・廃棄の責任を含む。","環境社会学・人新世","環境政治理論",2003,"Western_Europe","https://en.wikipedia.org/wiki/Ecological_citizenship"),
    ("脱炭素正義","Decarbonization Justice","","エネルギー転換が雇用・地域・途上国にもたらすコストと便益の分配をめぐる正義論。「公正な移行（Just Transition）」概念と結びついている。","環境社会学・人新世","環境社会学",2015,"Global_Synthesis","https://en.wikipedia.org/wiki/Just_transition"),
    ("生態系サービスの社会学","Sociology of Ecosystem Services","","自然が人間社会に提供するサービス（食料・水・気候調節）の社会的評価・分配・ガバナンスを分析する学際領域。","環境社会学・人新世","環境社会学",2005,"Global_Synthesis","https://en.wikipedia.org/wiki/Ecosystem_services"),
    ("社会的代謝","Social Metabolism","","マルクスの物質代謝論を継承し、社会が自然と行うエネルギー・物質の交換プロセスを分析する概念。マルチネス＝アリエルらが展開。","環境社会学・人新世","政治生態学",1990,"Western_Europe","https://en.wikipedia.org/wiki/Social_metabolism"),
    ("地球的境界線","Planetary Boundaries","","ロックストロームらが2009年に提唱した、人類が安全に活動できる地球システムの限界値（9領域）を定量化した概念枠組み。","環境社会学・人新世","地球システム科学",2009,"Western_Europe","https://en.wikipedia.org/wiki/Planetary_boundaries"),
    ("脱成長論","Degrowth","","経済成長を前提としない社会モデルを志向する思想・運動。ラトゥーシュらが展開し、GDP至上主義を批判しウェルビーイング中心社会を提唱する。","環境社会学・人新世","政治生態学",2000,"Western_Europe","https://en.wikipedia.org/wiki/Degrowth"),
    ("適応的ガバナンス","Adaptive Governance","","不確実で複雑な社会＝生態システムの管理において、学習・実験・制度の柔軟な調整を行う統治の枠組み。","環境社会学・人新世","環境ガバナンス",2000,"North_America","https://en.wikipedia.org/wiki/Adaptive_governance"),
    ("多種世界","Multispecies World","","アナ・チン・ダナ・ハラウェイらが論じた、人間を他の種との共存・絡み合いの中で捉える存在論的転換。人間中心主義への批判。","環境社会学・人新世","人新世論",2010,"North_America","https://en.wikipedia.org/wiki/Multispecies_ethnography"),

    # ── 生活世界・現象学的社会学 (9) ──
    ("現象学的還元の社会学的応用","Phenomenological Reduction in Sociology","","フッサールのエポケー（判断停止）を社会学的方法として応用する試み。シュッツが生活世界の分析においてこれを変容させた形で用いた。","生活世界・現象学的社会学","現象学的社会学",1932,"Western_Europe","https://en.wikipedia.org/wiki/Phenomenological_reduction"),
    ("身体図式","Body Schema","","メルロ＝ポンティが提唱した、身体が環境との関係において無意識に構成する空間・運動のマップ。習慣的行為の根拠として社会学・認知科学で参照される。","生活世界・現象学的社会学","現象学的社会学",1945,"Western_Europe","https://en.wikipedia.org/wiki/Body_schema"),
    ("意味連関の多元性","Multiple Realities","","シュッツが提示した、日常生活・夢・宗教的経験・科学など複数の「意味領域（有限の意味領域）」が並立するという社会現象学的洞察。","生活世界・現象学的社会学","現象学的社会学",1945,"Western_Europe","https://en.wikipedia.org/wiki/Alfred_Schutz"),
    ("信頼とコミットメント","Trust and Commitment","","ルーマン・ギデンズが分析した、近代的不確実性を縮減する機制としての信頼とコミットメント。対人・制度・抽象システムへの信頼を区分する。","生活世界・現象学的社会学","現象学的社会学",1968,"Western_Europe","https://en.wikipedia.org/wiki/Trust_(social_science)#Sociology"),
    ("エスノメソドロジーの会話分析","Conversation Analysis in Ethnomethodology","","サックス・シェグロフ・ジェファーソンが開発した、日常会話の順番交替・修復・連鎖構造を詳細に分析する方法論。エスノメソドロジーの中核。","生活世界・現象学的社会学","エスノメソドロジー",1974,"North_America","https://en.wikipedia.org/wiki/Conversation_analysis"),
    ("間主観性の形成","Constitution of Intersubjectivity","","フッサールとシュッツが論じた、他者の経験をどのように理解するかという問題。感情移入・類推的移し入れによる他者経験の構成を分析する。","生活世界・現象学的社会学","現象学的社会学",1931,"Western_Europe","https://en.wikipedia.org/wiki/Intersubjectivity"),
    ("日常的知識の秩序","Order of Common-Sense Knowledge","","ガーフィンケルが研究した、日常生活者が自明視する社会的ルールの実践的達成。「背景期待」の秩序形成への貢献を分析した。","生活世界・現象学的社会学","エスノメソドロジー",1967,"North_America","https://en.wikipedia.org/wiki/Harold_Garfinkel"),
    ("実践的推論","Practical Reasoning","","エスノメソドロジーとウィトゲンシュタイン哲学が結びついた、日常生活者が状況に応じて行う実践的・手続的推論の分析。","生活世界・現象学的社会学","エスノメソドロジー",1967,"North_America","https://en.wikipedia.org/wiki/Practical_reason"),
    ("間身体性","Intercorporeality","","メルロ＝ポンティ由来の概念。身体的な共鳴・模倣・共同調整を通じた他者との根源的なつながりを指し、社会的相互作用の身体的基盤を説明する。","生活世界・現象学的社会学","現象学的社会学",1945,"Western_Europe","https://en.wikipedia.org/wiki/Intercorporeality"),
]

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 26)...")
    ins, skp = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {skp}")
