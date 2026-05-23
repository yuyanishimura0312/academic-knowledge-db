"""
DUA Wave A2 Batch 6 — 文学批評理論 +200, 古典学・古典文学 +175, 歴史学 +150, 言語学 +100
Target: ~625 attempts → ~500 net insertions
"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

CONCEPTS = []

# ── 文学批評理論 +200 ──────────────────────────────────────────────
lit_crit = [
    ("ナラトロジー", "Narratology", "物語の構造と機能を分析する学問分野。Genette、Bal、Rimmonde-Ladeらが体系化。", "文学批評理論", "Western_Europe", -1960, "https://en.wikipedia.org/wiki/Narratology"),
    ("焦点化", "Focalization", "物語内の視点と情報フィルタリングを指すナラトロジー概念。Genaetteが導入。", "文学批評理論", "Western_Europe", 1972, "https://en.wikipedia.org/wiki/Focalization"),
    ("信頼できない語り手", "Unreliable Narrator", "語り手の信頼性が疑わしい物語技法。Wayne Boothが概念化。", "文学批評理論", "North_America", 1961, "https://en.wikipedia.org/wiki/Unreliable_narrator"),
    ("自由間接話法", "Free Indirect Discourse", "語り手と人物の声が融合する文体技法。Flaubert以来の小説技法。", "文学批評理論", "Western_Europe", -1850, "https://en.wikipedia.org/wiki/Free_indirect_speech"),
    ("ミメーシスとディエゲーシス", "Mimesis and Diegesis", "アリストテレス以来の模倣と語りの二分法。プラトン、アリストテレスに遡る詩学概念。", "文学批評理論", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Mimesis"),
    ("叙事詩的劇場", "Epic Theatre", "ブレヒトの疎外効果を用いた演劇理論。観客の批判的意識を喚起する。", "文学批評理論", "Western_Europe", 1920, "https://en.wikipedia.org/wiki/Epic_theatre"),
    ("パロディとパスティーシュ", "Parody and Pastiche", "先行テクストを模倣・変形する文学技法。Genette、Jamesonが分析。", "文学批評理論", "Western_Europe", -1900, "https://en.wikipedia.org/wiki/Parody"),
    ("アレゴリー", "Allegory", "抽象的概念や道徳を具体的物語で表現する文学形式。中世・ルネサンスに隆盛。", "文学批評理論", "Western_Europe", -500, "https://en.wikipedia.org/wiki/Allegory"),
    ("風刺文学", "Satire", "社会・政治・人間の愚かさを嘲笑・批判する文学形式。古代ローマから連続する伝統。", "文学批評理論", "Western_Europe", -200, "https://en.wikipedia.org/wiki/Satire"),
    ("カルナヴァル文学論", "Carnivalesque", "バフチンの概念。民衆的笑いと転倒の文学的表現。ラブレー研究に基づく。", "文学批評理論", "Western_Europe", 1965, "https://en.wikipedia.org/wiki/Carnivalesque"),
    ("ダイアローグ性", "Dialogism", "バフチンの概念。テクスト内の複数の声と対話的関係。モノロジズムと対置。", "文学批評理論", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Dialogism"),
    ("ポリフォニー小説", "Polyphonic Novel", "バフチンがドストエフスキーに見た複数の独立した声が響き合う小説構造。", "文学批評理論", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Polyphony_(literature)"),
    ("クロノトポス", "Chronotope", "バフチンの時空間概念。文学テクストにおける時間と空間の内在的関連性。", "文学批評理論", "Western_Europe", 1937, "https://en.wikipedia.org/wiki/Chronotope"),
    ("ビルドゥングスロマン", "Bildungsroman", "主人公の精神的成長を描く教養小説のジャンル。ゲーテ「ウィルヘルム・マイスター」が典型。", "文学批評理論", "Western_Europe", 1795, "https://en.wikipedia.org/wiki/Bildungsroman"),
    ("ゴシック文学", "Gothic Literature", "恐怖・超自然・廃墟・道徳的腐敗を描く文学ジャンル。18世紀英国に起源。", "文学批評理論", "Western_Europe", 1764, "https://en.wikipedia.org/wiki/Gothic_fiction"),
    ("マジックリアリズム", "Magical Realism", "日常的現実に魔術的要素が融合する文学様式。ガルシア＝マルケスらラテンアメリカ文学と結びつく。", "文学批評理論", "Latin_America", 1950, "https://en.wikipedia.org/wiki/Magic_realism"),
    ("ポストコロニアル文学批評", "Postcolonial Literary Criticism", "植民地主義の文学的表象と抵抗の研究。バーバ、スピヴァク、サイードが中心。", "文学批評理論", "Global_Synthesis", 1978, "https://en.wikipedia.org/wiki/Postcolonial_literature"),
    ("世界文学", "World Literature", "国民文学を超えた比較文学の視座。ゲーテのWeltliteraturからダムロッシュの現代的再定義まで。", "文学批評理論", "Global_Synthesis", 1827, "https://en.wikipedia.org/wiki/World_literature"),
    ("口承文学研究", "Oral Literature Studies", "文字以前・文字外の口頭伝承・叙事詩の研究。パリー＝ロード理論が基礎。", "文学批評理論", "Global_Synthesis", 1928, "https://en.wikipedia.org/wiki/Oral_literature"),
    ("フォーミュラ理論", "Formula Theory", "パリーとロードによる口承詩のフォーミュラ的表現分析理論。ホメロス研究に革命。", "文学批評理論", "North_America", 1928, "https://en.wikipedia.org/wiki/Oral-formulaic_composition"),
    ("文学ジャンル論", "Genre Theory", "文学のジャンル分類と歴史的変容の研究。フライ、バフチン、トドロフが代表的理論家。", "文学批評理論", "North_America", -1900, "https://en.wikipedia.org/wiki/Literary_genre"),
    ("神話批評", "Myth Criticism", "文学テクストの神話的パターンを分析する批評手法。フライの元型批評が代表。", "文学批評理論", "North_America", 1957, "https://en.wikipedia.org/wiki/Myth_criticism"),
    ("精神分析批評", "Psychoanalytic Criticism", "フロイト・ラカン・クリステヴァの精神分析を文学に適用する批評。無意識と欲望の分析。", "文学批評理論", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Psychoanalytic_literary_criticism"),
    ("ラカン的文学批評", "Lacanian Literary Criticism", "ラカンの象徴界・想像界・現実界の三項構造を用いた文学分析。", "文学批評理論", "Western_Europe", 1953, "https://en.wikipedia.org/wiki/Jacques_Lacan"),
    ("クィア批評", "Queer Theory in Literature", "セクシュアリティと規範的ジェンダーへの抵抗を文学テクストで分析するアプローチ。", "文学批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Queer_theory"),
    ("フェミニスト文学批評", "Feminist Literary Criticism", "ジェンダー視点から文学テクストと文学史を再読する批評理論。ウォルフ、ショウォルターらが先駆。", "文学批評理論", "North_America", 1970, "https://en.wikipedia.org/wiki/Feminist_literary_criticism"),
    ("ジャイノクリティクス", "Gynocriticism", "ショウォルターが提唱した女性文学の固有伝統を研究する女性主義批評。", "文学批評理論", "North_America", 1979, "https://en.wikipedia.org/wiki/Gynocriticism"),
    ("エコクリティシズム", "Ecocriticism", "環境・自然と文学の関係を分析する生態学的批評。チェリュルとグロットフェルティが創始。", "文学批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Ecocriticism"),
    ("文化物質主義", "Cultural Materialism", "ドルシモアとシンフィールドが展開した英国版新歴史主義。権力と抵抗の物質的分析。", "文学批評理論", "Western_Europe", 1985, "https://en.wikipedia.org/wiki/Cultural_materialism_(literary_criticism)"),
    ("新歴史主義", "New Historicism", "グリーンブラットが創始。テクストと歴史的コンテクストの循環的関係を重視する批評。", "文学批評理論", "North_America", 1982, "https://en.wikipedia.org/wiki/New_Historicism"),
    ("テクスト生産論", "Textual Production Theory", "テクストの物質的生産過程・編集・出版を批評の対象とするアプローチ。McGannが代表。", "文学批評理論", "North_America", 1983, "https://en.wikipedia.org/wiki/Textual_criticism"),
    ("書誌学と校訂批評", "Bibliography and Textual Criticism", "写本・印刷テクストの伝承と校訂を研究する文献学的批評。", "文学批評理論", "Western_Europe", -1800, "https://en.wikipedia.org/wiki/Textual_criticism"),
    ("受容美学", "Reception Aesthetics", "ヤウスとイーザーが創始したコンスタンツ学派の読者反応理論。地平融合と読者の役割。", "文学批評理論", "Western_Europe", 1967, "https://en.wikipedia.org/wiki/Reception_theory"),
    ("読者反応批評", "Reader-Response Criticism", "テクストの意味が読者との相互作用で生成されるという批評理論。フィッシュ、ホランドが代表。", "文学批評理論", "North_America", 1970, "https://en.wikipedia.org/wiki/Reader-response_criticism"),
    ("詩学と修辞学", "Poetics and Rhetoric", "文学の技法と効果を体系的に分析する古代以来の学問。アリストテレスの詩学が基礎。", "文学批評理論", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Poetics_(Aristotle)"),
    ("プロットと物語構造", "Plot and Narrative Structure", "物語の時系列的展開と因果関係の分析。アリストテレスの始中終からフライタークのピラミッドまで。", "文学批評理論", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Plot_(narrative)"),
    ("トポス分析", "Topos Analysis", "クルティウスによる文学における繰り返し現れる定型的表現・場所の研究。", "文学批評理論", "Western_Europe", 1948, "https://en.wikipedia.org/wiki/Topos"),
    ("作者の意図論争", "Intentional Fallacy", "ウィムサットとビアズリーが提起した作者の意図を解釈基準とすることへの批判。", "文学批評理論", "North_America", 1946, "https://en.wikipedia.org/wiki/Intentional_fallacy"),
    ("文学的価値論", "Literary Value", "文学作品の芸術的・倫理的・社会的価値の基準をめぐる批評理論。", "文学批評理論", "Western_Europe", -1900, "https://en.wikipedia.org/wiki/Literary_criticism"),
    ("詩の音楽性", "Prosody", "詩のリズム・韻律・音響を分析する詩学の一分野。", "文学批評理論", "Western_Europe", -500, "https://en.wikipedia.org/wiki/Prosody_(linguistics)"),
    ("俳句と連歌の詩学", "Haiku and Renga Poetics", "日本の短詩形と連作詩の美学。切れ字・季語・間の概念を含む固有の詩学体系。", "文学批評理論", "East_Asia", 1600, "https://en.wikipedia.org/wiki/Haiku"),
    ("モノノアワレ", "Mono no Aware", "物事の無常さに対する日本的感受性。源氏物語研究を通じて本居宣長が体系化。", "文学批評理論", "East_Asia", 1796, "https://en.wikipedia.org/wiki/Mono_no_aware"),
    ("漢詩学", "Chinese Poetry Studies", "詩経から唐宋詩までの漢詩の形式・美学・批評を研究する学問。", "文学批評理論", "East_Asia", -600, "https://en.wikipedia.org/wiki/Chinese_poetry"),
    ("サンスクリット詩学", "Sanskrit Poetics", "ラサ論・ドヴァニ論など古代インドの詩学理論。バラタのナーティヤシャーストラが基礎。", "文学批評理論", "South_Asia", -200, "https://en.wikipedia.org/wiki/Sanskrit_literature"),
    ("ラサ論", "Rasa Theory", "バラタが体系化したインド古典芸術の感情・情緒の美学理論。シュリンガーラ等の九ラサ。", "文学批評理論", "South_Asia", -200, "https://en.wikipedia.org/wiki/Rasa_(aesthetics)"),
    ("アラビア詩学", "Arabic Poetics", "ムアッラカート・アッバース朝詩学・イブン・クタイバの批評を含む古典アラビア文学批評。", "文学批評理論", "West_Asia_North_Africa", 600, "https://en.wikipedia.org/wiki/Arabic_poetry"),
    ("アフリカ口承文学", "African Oral Literature", "グリオー伝統・スンジャータ叙事詩・民話を含むサブサハラアフリカの口承文学研究。", "文学批評理論", "Sub_Saharan_Africa", -1000, "https://en.wikipedia.org/wiki/African_oral_literature"),
    ("ネグリチュード文学", "Négritude Literature", "セゼール・サンゴールらによるアフリカ系文化の再肯定と植民地主義への抵抗の文学運動。", "文学批評理論", "Sub_Saharan_Africa", 1935, "https://en.wikipedia.org/wiki/N%C3%A9gritude"),
    ("ラテンアメリカ文学批評", "Latin American Literary Criticism", "ブーム文学・テスティモニオ・バロック文学を含むラテンアメリカ文学の批評的研究。", "文学批評理論", "Latin_America", 1960, "https://en.wikipedia.org/wiki/Latin_American_literature"),
    ("翻訳研究", "Translation Studies", "翻訳の理論・実践・文化的役割を研究する学際的分野。ヴェヌティ、ベンヤミン、ナイダが代表。", "文学批評理論", "Global_Synthesis", 1972, "https://en.wikipedia.org/wiki/Translation_studies"),
    ("異化と家内化翻訳", "Foreignization and Domestication", "ヴェヌティの翻訳戦略論。異文化性を保持する異化翻訳vs読者優先の家内化翻訳の対立。", "文学批評理論", "North_America", 1995, "https://en.wikipedia.org/wiki/Foreignization_and_domestication"),
    ("比較文学方法論", "Comparative Literature Methodology", "複数言語・文学伝統を横断的に比較研究する方法論。影響研究・類比研究・相互照射。", "文学批評理論", "Global_Synthesis", 1800, "https://en.wikipedia.org/wiki/Comparative_literature"),
    ("影響不安", "Anxiety of Influence", "ハロルド・ブルームの詩的影響論。後代詩人が先行詩人に対してとる誤読と克服の弁証法。", "文学批評理論", "North_America", 1973, "https://en.wikipedia.org/wiki/The_Anxiety_of_Influence"),
    ("正典形成論", "Canon Formation", "文学的正典の構築・維持・批判をめぐる議論。ブルーム対多文化主義批評の論争。", "文学批評理論", "North_America", 1980, "https://en.wikipedia.org/wiki/Western_canon"),
    ("文化研究と文学", "Cultural Studies and Literature", "バーミンガム学派の文化研究を文学分析に適用するアプローチ。大衆文化・サブカルチャー研究。", "文学批評理論", "Western_Europe", 1964, "https://en.wikipedia.org/wiki/Cultural_studies"),
    ("物語倫理学", "Narrative Ethics", "フェラン・ヌスバウム・ブースらが展開した物語の倫理的次元の研究。", "文学批評理論", "North_America", 1988, "https://en.wikipedia.org/wiki/Narrative_ethics"),
    ("認知詩学", "Cognitive Poetics", "認知科学と文学理論を統合したアプローチ。スティーンバーグ、ガブリエル、ツールが代表。", "文学批評理論", "Western_Europe", 1994, "https://en.wikipedia.org/wiki/Cognitive_poetics"),
    ("概念メタファー論と文学", "Conceptual Metaphor Theory in Literature", "レイコフとジョンソンの概念メタファー論を文学分析に応用する研究。", "文学批評理論", "North_America", 1980, "https://en.wikipedia.org/wiki/Conceptual_metaphor"),
    ("デジタル人文学と文学", "Digital Humanities and Literature", "遠読・コーパス分析・デジタル編集等の計算論的文学研究手法。モレッティが代表。", "文学批評理論", "Global_Synthesis", 2000, "https://en.wikipedia.org/wiki/Digital_humanities"),
    ("遠読", "Distant Reading", "モレッティが提唱した大規模コーパス分析による文学史研究。精読の対概念。", "文学批評理論", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/Distant_reading"),
    ("文学社会学", "Sociology of Literature", "文学の社会的生産・流通・受容を研究する社会学的アプローチ。ゴールドマン・エスカルピが代表。", "文学批評理論", "Western_Europe", 1958, "https://en.wikipedia.org/wiki/Sociology_of_literature"),
    ("文学場", "Literary Field", "ブルデューの文化場理論を文学に適用した概念。象徴資本・文学資本の競争空間。", "文学批評理論", "Western_Europe", 1983, "https://en.wikipedia.org/wiki/Field_theory_(sociology)"),
    ("マルクス主義文学批評", "Marxist Literary Criticism", "イデオロギー・土台と上部構造・階級意識を文学分析に適用する批評。ルカーチ・イーグルトンが代表。", "文学批評理論", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Marxist_literary_criticism"),
    ("反映論と自律論の論争", "Reflection Theory vs Autonomy", "文学が社会を反映するか自律した芸術かをめぐる批評理論の対立。", "文学批評理論", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Literary_criticism"),
    ("形式主義批評", "Formalist Criticism", "テクストの形式・構造・技法に焦点を当てる批評手法。ロシア・フォルマリズムと英米ニュークリティシズム。", "文学批評理論", "Western_Europe", 1910, "https://en.wikipedia.org/wiki/Formalism_(literature)"),
    ("シュクロフスキーの異化", "Defamiliarization (Ostranenie)", "シュクロフスキーが提唱した自動化された知覚を更新する芸術の機能概念。", "文学批評理論", "Western_Europe", 1917, "https://en.wikipedia.org/wiki/Defamiliarization"),
    ("プラハ学派詩学", "Prague School Poetics", "ムカジョフスキー・ヤコブソンらが展開した構造主義詩学。文学機能・優勢・前景化。", "文学批評理論", "Western_Europe", 1926, "https://en.wikipedia.org/wiki/Prague_linguistic_circle"),
    ("文学言語の詩的機能", "Poetic Function of Language", "ヤコブソンのコミュニケーション機能論における詩的機能。メッセージ自体への指向性。", "文学批評理論", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Jakobson's_functions_of_language"),
    ("テクストと作品の区別", "Text vs Work", "バルトの区別。固定した芸術作品としての「作品」対読者が生産する開かれた「テクスト」。", "文学批評理論", "Western_Europe", 1971, "https://en.wikipedia.org/wiki/The_Death_of_the_Author"),
    ("記号学的文学批評", "Semiotic Literary Criticism", "グレマス・ロトマン・エーコらが展開した文学テクストの記号論的分析。", "文学批評理論", "Western_Europe", 1966, "https://en.wikipedia.org/wiki/Semiotics"),
    ("物語文法", "Story Grammar", "ラメルハートとマンドラーが開発した物語構造の心理学的モデル。", "文学批評理論", "North_America", 1975, "https://en.wikipedia.org/wiki/Story_grammar"),
    ("プロップの昔話形態論", "Propp's Morphology of Folktales", "プロップが分析した民話の31の機能と7人の登場人物類型による物語構造論。", "文学批評理論", "Western_Europe", 1928, "https://en.wikipedia.org/wiki/Vladimir_Propp"),
    ("グレマスの行為素モデル", "Greimas Actantial Model", "グレマスが提案した6つの行為素（主体・客体・送り手・受け手・助力者・妨害者）による物語分析。", "文学批評理論", "Western_Europe", 1966, "https://en.wikipedia.org/wiki/Actant"),
    ("テクストの多義性", "Textual Polysemy", "テクストが複数の意味を同時に生成する特性。解釈の開放性とエーコの「開かれた作品」。", "文学批評理論", "Western_Europe", 1962, "https://en.wikipedia.org/wiki/Polysemy"),
    ("アイロニーと文学", "Irony in Literature", "テクストの表層的意味と深層的意味の乖離。口頭的・状況的・劇的アイロニーの区別。", "文学批評理論", "Western_Europe", -400, "https://en.wikipedia.org/wiki/Irony"),
    ("崇高の美学", "Aesthetic of the Sublime", "バーク・カントが分析した圧倒的な大きさや力による美的経験。ロマン主義文学の中心概念。", "文学批評理論", "Western_Europe", 1757, "https://en.wikipedia.org/wiki/Sublime_(aesthetics)"),
    ("テクスト間対話性", "Intertextuality", "クリステヴァが命名したテクスト相互の引用・変換・吸収の関係性概念。", "文学批評理論", "Western_Europe", 1969, "https://en.wikipedia.org/wiki/Intertextuality"),
    ("超テクスト性", "Hypertextuality", "ジュネットのトランステクスチュアリティ理論における後テクストと前テクストの変換的関係。", "文学批評理論", "Western_Europe", 1982, "https://en.wikipedia.org/wiki/G%C3%A9rard_Genette"),
    ("ロマン主義文学論", "Romantic Literary Theory", "シュレーゲル兄弟・ノヴァーリス・ワーズワースらのロマン主義文学理論。断片・無限・芸術の自律。", "文学批評理論", "Western_Europe", 1790, "https://en.wikipedia.org/wiki/Romanticism"),
    ("象徴主義詩学", "Symbolist Poetics", "マラルメ・ヴェルレーヌ・ランボーが実践した象徴・音楽性・暗示を重視する詩学。", "文学批評理論", "Western_Europe", 1880, "https://en.wikipedia.org/wiki/Symbolism_(arts)"),
    ("モダニズム文学論", "Modernist Literary Theory", "エリオット・パウンド・ウルフらが展開した伝統断絶と革新を旨とする文学理論。", "文学批評理論", "Western_Europe", 1910, "https://en.wikipedia.org/wiki/Modernism"),
    ("ポストモダン文学論", "Postmodern Literary Theory", "メタフィクション・断章・不確定性・パスティーシュを特徴とする文学理論と実践。", "文学批評理論", "North_America", 1960, "https://en.wikipedia.org/wiki/Postmodern_literature"),
    ("メタフィクション", "Metafiction", "フィクションであることを自己言及的に暴露する文学形式。ウォーとハッチオンが分析。", "文学批評理論", "North_America", 1970, "https://en.wikipedia.org/wiki/Metafiction"),
    ("オートフィクション", "Autofiction", "自伝的事実とフィクションが混交する文学形式。ドゥブロフスキーが命名。", "文学批評理論", "Western_Europe", 1977, "https://en.wikipedia.org/wiki/Autofiction"),
    ("ライフ・ライティング", "Life Writing", "自伝・回想録・日記・書簡などの生の経験を書く文学実践の総称。", "文学批評理論", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Life_writing"),
    ("身体と文学", "Body and Literature", "フェミニズム・クィア理論・障害学を通じた身体の文学的表象研究。", "文学批評理論", "North_America", 1985, "https://en.wikipedia.org/wiki/Body_in_literature"),
    ("トラウマ文学論", "Trauma Literature", "ホロコースト文学・戦争文学・証言文学の証言可能性と表象の倫理をめぐる理論。", "文学批評理論", "Global_Synthesis", 1992, "https://en.wikipedia.org/wiki/Trauma_literature"),
    ("ディアスポラ文学", "Diaspora Literature", "移民・難民・離散民族の経験を描く文学とその批評。ブレイスウェイト・ラシュディらが代表。", "文学批評理論", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Diaspora_literature"),
    ("民族文学", "Ethnic Literature", "特定民族集団の文化的アイデンティティと経験を表現する文学とその批評研究。", "文学批評理論", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Ethnic_literature"),
    ("先住民文学批評", "Indigenous Literary Criticism", "先住民の語りの伝統と欧米批評理論の接続・批判的再構築。ジョー・バストーら。", "文学批評理論", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Indigenous_literature"),
    ("環境文学", "Environmental Literature", "自然・環境・非人間的存在との関係を主題とする文学。エコクリティシズムと連動。", "文学批評理論", "North_America", 1970, "https://en.wikipedia.org/wiki/Environmental_literature"),
    ("ユートピア文学", "Utopian Literature", "理想社会・ディストピア・SFを含む社会的想像力の文学形式とその批評。", "文学批評理論", "Western_Europe", 1516, "https://en.wikipedia.org/wiki/Utopian_literature"),
    ("ファンタジー文学論", "Fantasy Literature Theory", "超自然・二次世界・ヘシタントの概念を含むファンタジー文学の定義と批評。トールキン・トドロフ。", "文学批評理論", "Western_Europe", 1954, "https://en.wikipedia.org/wiki/Fantasy_literature"),
    ("物語医学", "Narrative Medicine", "リタ・シャロンが確立した医療における物語能力の育成と応用。", "文学批評理論", "North_America", 2001, "https://en.wikipedia.org/wiki/Narrative_medicine"),
    ("文学ツーリズム", "Literary Tourism", "作家の生地・作品舞台の聖地巡礼を研究する文学地理学的アプローチ。", "文学批評理論", "Western_Europe", 1990, "https://en.wikipedia.org/wiki/Literary_tourism"),
    ("文学地理学", "Literary Geography", "文学テクストの空間・場所・地図的想像力を分析する地理批評。モレッティのアトラス。", "文学批評理論", "Western_Europe", 1998, "https://en.wikipedia.org/wiki/Literary_geography"),
    ("動物研究と文学", "Animal Studies and Literature", "非人間動物の文学的表象と人間中心主義批判を扱うアプローチ。", "文学批評理論", "North_America", 2000, "https://en.wikipedia.org/wiki/Animality"),
    ("物質文化と文学", "Material Culture and Literature", "物・モノ・商品の文学的機能と物質性を分析するアプローチ。", "文学批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Material_culture"),
    ("感情とアフェクト理論", "Affect Theory in Literature", "情動・感情の文学的機能と身体的次元を研究するアプローチ。マッスミ・セジウィック。", "文学批評理論", "North_America", 1995, "https://en.wikipedia.org/wiki/Affect_theory"),
    ("文学と記憶", "Literature and Memory", "個人・集合・文化的記憶の文学的構築と伝達を研究する批評的アプローチ。", "文学批評理論", "Global_Synthesis", 1992, "https://en.wikipedia.org/wiki/Memory_studies"),
    ("ゾンビ・アポカリプス文学", "Apocalyptic Literature", "終末・黙示録・破滅後世界を描く文学の伝統と現代的変容。宗教テクストから現代SF。", "文学批評理論", "Global_Synthesis", -200, "https://en.wikipedia.org/wiki/Apocalyptic_literature"),
    ("喜劇と悲劇の詩学", "Poetics of Comedy and Tragedy", "アリストテレス以来の二大ジャンルの定義・機能・系譜をめぐる詩学的議論。", "文学批評理論", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Tragedy"),
    ("カタルシス論", "Catharsis Theory", "アリストテレスが提唱した悲劇による感情の浄化・解放の効果概念。解釈の論争史。", "文学批評理論", "Western_Europe", -350, "https://en.wikipedia.org/wiki/Catharsis"),
    ("詩人追放論とその反論", "Defense of Poetry", "プラトンの詩人追放に対するシドニー・シェリーらの詩の擁護論。文学の認識論的価値。", "文学批評理論", "Western_Europe", -380, "https://en.wikipedia.org/wiki/A_Defence_of_Poetry"),
    ("文学的真実", "Literary Truth", "フィクションが虚偽にもかかわらず真実を語るという逆説。フッセン・ウォルトンが分析。", "文学批評理論", "North_America", 1990, "https://en.wikipedia.org/wiki/Fictionalism"),
    ("文学教育論", "Literary Pedagogy", "文学テクストを教育の場でどう教えるかをめぐる理論と実践。批判的リテラシー教育。", "文学批評理論", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Literary_education"),
    ("出版史と文学", "History of Publishing and Literature", "印刷・出版・書店・図書館が文学の生産と流通に果たした役割の歴史的研究。", "文学批評理論", "Western_Europe", 1440, "https://en.wikipedia.org/wiki/History_of_publishing"),
    ("スタイル論と文体研究", "Stylistics", "言語学的手法で文学テクストの文体を分析する学問。レヒとショートが代表的理論家。", "文学批評理論", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Stylistics"),
    ("文学とナショナリズム", "Literature and Nationalism", "国民文学の形成・国家的アイデンティティと文学の関係。アンダーソンの想像の共同体と連動。", "文学批評理論", "Global_Synthesis", 1800, "https://en.wikipedia.org/wiki/National_literature"),
    ("文学と映画研究", "Literature and Film Studies", "原作と映画化の関係・アダプテーション理論・中間メディア研究。", "文学批評理論", "Global_Synthesis", 1950, "https://en.wikipedia.org/wiki/Adaptation_studies"),
    ("詩の視覚性と図形詩", "Visual Poetry and Concrete Poetry", "文字の視覚的配置を詩的表現に用いるコンクリート・ポエトリーとその歴史。", "文学批評理論", "Global_Synthesis", 1950, "https://en.wikipedia.org/wiki/Concrete_poetry"),
    ("声とパフォーマンス詩学", "Voice and Performance Poetry", "詩の朗読・身体的演技を詩的実践の中心とする現代的詩学とスラム・ポエトリー。", "文学批評理論", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Slam_poetry"),
]
CONCEPTS.extend(lit_crit)

# ── 古典学・古典文学 +175 ──────────────────────────────────────────────
classics = [
    ("ホメロス問題", "Homeric Question", "イリアスとオデュッセイアの作者・成立過程・口承性をめぐる19世紀以来の学術論争。", "古典学・古典文学", "Western_Europe", 1795, "https://en.wikipedia.org/wiki/Homeric_question"),
    ("ヘシオドスの神統記", "Hesiod's Theogony", "ギリシア神々の系譜と宇宙生成を語るヘシオドスの叙事詩。神話・農事・労働の詩人。", "古典学・古典文学", "Western_Europe", -700, "https://en.wikipedia.org/wiki/Theogony"),
    ("ギリシア悲劇", "Greek Tragedy", "アイスキュロス・ソポクレス・エウリピデスによる5世紀アテナイの演劇形式。", "古典学・古典文学", "Western_Europe", -525, "https://en.wikipedia.org/wiki/Greek_tragedy"),
    ("アイスキュロス", "Aeschylus", "ギリシア悲劇の父。オレステイア三部作でコロスと二俳優を組み合わせた演劇形式を確立。", "古典学・古典文学", "Western_Europe", -525, "https://en.wikipedia.org/wiki/Aeschylus"),
    ("ソポクレス", "Sophocles", "オイディプス王・アンティゴネーを書いたギリシア悲劇詩人。運命・自由意志・知識を主題とする。", "古典学・古典文学", "Western_Europe", -497, "https://en.wikipedia.org/wiki/Sophocles"),
    ("エウリピデス", "Euripides", "メデイア・バッカイを書いたギリシア悲劇詩人。心理的深みと女性表象の革新で知られる。", "古典学・古典文学", "Western_Europe", -480, "https://en.wikipedia.org/wiki/Euripides"),
    ("アリストファネス", "Aristophanes", "古代ギリシア喜劇の代表的詩人。雲・蜂・鳥等でポリスの政治・社会を風刺。", "古典学・古典文学", "Western_Europe", -446, "https://en.wikipedia.org/wiki/Aristophanes"),
    ("ギリシア叙情詩", "Greek Lyric Poetry", "サッポー・アルカイオス・ピンダロス等による7-5世紀の個人的・祝典的詩歌。", "古典学・古典文学", "Western_Europe", -650, "https://en.wikipedia.org/wiki/Greek_lyric"),
    ("サッポー", "Sappho", "レスボス島の女性詩人。愛・欲望・神への祈りを詠んだ叙情詩で古代から珍重される。", "古典学・古典文学", "Western_Europe", -620, "https://en.wikipedia.org/wiki/Sappho"),
    ("ピンダロスの頌歌", "Pindar's Epinicia", "オリンピック等のゲームの勝利者を称える祝勝歌。合唱詩の最高峰とされる。", "古典学・古典文学", "Western_Europe", -518, "https://en.wikipedia.org/wiki/Pindar"),
    ("ヘロドトスの歴史", "Herodotus's Histories", "「歴史の父」ヘロドトスによるペルシア戦争の叙述。民族誌・地理・神話が融合した古代の傑作。", "古典学・古典文学", "Western_Europe", -440, "https://en.wikipedia.org/wiki/Histories_(Herodotus)"),
    ("トゥキュディデスの歴史", "Thucydides's History", "ペロポネソス戦争史。政治的分析・演説・方法論的厳密さで近代歴史学の先駆とされる。", "古典学・古典文学", "Western_Europe", -431, "https://en.wikipedia.org/wiki/History_of_the_Peloponnesian_War"),
    ("プラトンの対話篇", "Platonic Dialogues", "ソクラテスを主人公とした哲学的問答形式の著作群。イデア論・政治論・宇宙論を含む。", "古典学・古典文学", "Western_Europe", -399, "https://en.wikipedia.org/wiki/Platonic_dialogues"),
    ("アリストテレスの著作群", "Aristotelian Corpus", "論理学・生物学・詩学・政治学・形而上学を網羅したアリストテレスの著作体系。", "古典学・古典文学", "Western_Europe", -384, "https://en.wikipedia.org/wiki/Aristotle"),
    ("ソクラテス以前の哲学者", "Pre-Socratic Philosophers", "タレス・ヘラクレイトス・パルメニデス等のソクラテス以前の自然哲学者とその断片。", "古典学・古典文学", "Western_Europe", -624, "https://en.wikipedia.org/wiki/Pre-Socratic_philosophy"),
    ("ストア哲学の著作", "Stoic Writings", "エピクテトス・マルクス・アウレリウス・セネカによるローマ時代のストア思想の著述。", "古典学・古典文学", "Western_Europe", -300, "https://en.wikipedia.org/wiki/Stoicism"),
    ("エピクロス派の著作", "Epicurean Writings", "エピクロス・ルクレティウスによる快楽と平静さを主題とする哲学的著作。", "古典学・古典文学", "Western_Europe", -341, "https://en.wikipedia.org/wiki/Epicureanism"),
    ("ウェルギリウスのアエネイス", "Virgil's Aeneid", "ローマ建国神話を叙事詩で描いた作品。ホメロスへの応答とアウグストゥス帝国の正統化。", "古典学・古典文学", "Western_Europe", -29, "https://en.wikipedia.org/wiki/Aeneid"),
    ("ホラティウスの詩学", "Horace's Ars Poetica", "ローマの詩人ホラティウスによる詩の技法と目的を論じた書簡詩。古典詩学の規範的文書。", "古典学・古典文学", "Western_Europe", -18, "https://en.wikipedia.org/wiki/Ars_Poetica_(Horace)"),
    ("オウィディウスの変身物語", "Ovid's Metamorphoses", "神話の変身を主題とした15巻の叙事詩。後代の文学・芸術に広大な影響を与えた。", "古典学・古典文学", "Western_Europe", 8, "https://en.wikipedia.org/wiki/Metamorphoses"),
    ("カトゥルスの詩集", "Catullus's Poems", "共和政末期ローマの詩人カトゥルスによる愛詩・友情詩・風刺詩。ラテン叙情詩の代表。", "古典学・古典文学", "Western_Europe", -84, "https://en.wikipedia.org/wiki/Catullus"),
    ("キケロの雄弁術", "Cicero's Rhetoric", "ローマ最大の雄弁家キケロによる修辞学・哲学・政治論の著作群。ラテン語散文の規範。", "古典学・古典文学", "Western_Europe", -106, "https://en.wikipedia.org/wiki/Cicero"),
    ("タキトゥスの年代記", "Tacitus's Annals", "ローマ帝政初期を描いた歴史書。政治腐敗・権力・美徳の喪失を鋭く分析。", "古典学・古典文学", "Western_Europe", 117, "https://en.wikipedia.org/wiki/Annals_(Tacitus)"),
    ("リウィウスのローマ史", "Livy's History of Rome", "建国から1世紀までのローマの歴史を142巻で叙述した大著。現存は35巻。", "古典学・古典文学", "Western_Europe", -27, "https://en.wikipedia.org/wiki/Livy"),
    ("プルタルコスの対比列伝", "Plutarch's Parallel Lives", "ギリシア・ローマの偉人を対比的に描いた伝記。道徳的教訓と古代の生き方の記録。", "古典学・古典文学", "Western_Europe", 100, "https://en.wikipedia.org/wiki/Parallel_Lives"),
    ("ルキアノスの諸作品", "Lucian's Works", "2世紀のシリア系ギリシア語作家ルキアノスによる風刺的対話・旅行記・修辞的練習。", "古典学・古典文学", "Western_Europe", 125, "https://en.wikipedia.org/wiki/Lucian"),
    ("古代の書簡文学", "Ancient Epistolary Literature", "キケロ・セネカ・パウロらの書簡。古代の知的交流・修辞・倫理の窓口。", "古典学・古典文学", "Western_Europe", -100, "https://en.wikipedia.org/wiki/Epistolary_literature"),
    ("アプレイウスの黄金のロバ", "Apuleius's Golden Ass", "2世紀のラテン語小説。魔法で驢馬に変えられた男の冒険とイシス崇拝の宗教的回心。", "古典学・古典文学", "Western_Europe", 160, "https://en.wikipedia.org/wiki/The_Golden_Ass"),
    ("ペトロニウスのサテュリコン", "Petronius's Satyricon", "ネロ期ローマの放蕩物語。グロテスクな宴会「トリマルキオーの饗宴」を含む断片的小説。", "古典学・古典文学", "Western_Europe", 61, "https://en.wikipedia.org/wiki/Satyricon"),
    ("マルティアリスの警句", "Martial's Epigrams", "1世紀末ローマの詩人マルティアリスによるラテン語警句詩集。社会風刺と日常描写。", "古典学・古典文学", "Western_Europe", 86, "https://en.wikipedia.org/wiki/Martial"),
    ("ユウェナリスの諷刺詩", "Juvenal's Satires", "2世紀ローマの詩人による辛辣な社会風刺詩。panem et circensesの句で知られる。", "古典学・古典文学", "Western_Europe", 100, "https://en.wikipedia.org/wiki/Juvenal"),
    ("古代写本伝承学", "Manuscript Transmission", "古典文献が中世を通じてどのように写本で伝承されたかを研究する古典文献学の核心。", "古典学・古典文学", "Western_Europe", 400, "https://en.wikipedia.org/wiki/Manuscript_tradition"),
    ("パピルス学", "Papyrology", "エジプト等で発見されたパピルス文書を研究する学問。多くの古典文献を回復した。", "古典学・古典文学", "Western_Europe", 1788, "https://en.wikipedia.org/wiki/Papyrology"),
    ("碑文学", "Epigraphy", "石碑・建造物等に刻まれた古代の碑文を解読・分析する学問。", "古典学・古典文学", "Western_Europe", -1800, "https://en.wikipedia.org/wiki/Epigraphy"),
    ("古貨幣学", "Numismatics", "古代のコインを研究する学問。経済史・政治史・図像学の資料。", "古典学・古典文学", "Western_Europe", -1500, "https://en.wikipedia.org/wiki/Numismatics"),
    ("古代ギリシア語文法", "Ancient Greek Grammar", "古典ギリシア語の文法体系。格変化・動詞変化・構文の複雑な体系。", "古典学・古典文学", "Western_Europe", -300, "https://en.wikipedia.org/wiki/Ancient_Greek_grammar"),
    ("ラテン語文法", "Latin Grammar", "古典ラテン語の格変化・動詞活用・構文体系。プリスキアヌス・ドナートゥスの文法書。", "古典学・古典文学", "Western_Europe", -100, "https://en.wikipedia.org/wiki/Latin_grammar"),
    ("インド・ヨーロッパ語族と古典学", "Indo-European Studies in Classics", "ギリシア語・ラテン語のインド・ヨーロッパ語祖語との関係の比較言語学的研究。", "古典学・古典文学", "Western_Europe", 1786, "https://en.wikipedia.org/wiki/Indo-European_languages"),
    ("ダンテの神曲", "Dante's Divine Comedy", "中世イタリアの詩人ダンテによる地獄・煉獄・天国の旅を描いた叙事詩。西洋文学の頂点の一つ。", "古典学・古典文学", "Western_Europe", 1320, "https://en.wikipedia.org/wiki/Divine_Comedy"),
    ("ペトラルカとソネット", "Petrarch and Sonnet", "イタリアのペトラルカが完成させたソネット形式とラウラへの恋愛詩。叙情詩の革命。", "古典学・古典文学", "Western_Europe", 1304, "https://en.wikipedia.org/wiki/Petrarch"),
    ("ボッカッチョのデカメロン", "Boccaccio's Decameron", "黒死病から逃れた10人が語る100の物語。中世から近代への過渡期のイタリア散文の傑作。", "古典学・古典文学", "Western_Europe", 1353, "https://en.wikipedia.org/wiki/The_Decameron"),
    ("ラブレーのガルガンチュア", "Rabelais's Gargantua", "フランス・ルネサンスの巨人物語。笑い・肉体・学問の讃美とカトリックの権威への風刺。", "古典学・古典文学", "Western_Europe", 1534, "https://en.wikipedia.org/wiki/Gargantua_and_Pantagruel"),
    ("セルバンテスのドン・キホーテ", "Don Quixote", "近代小説の嚆矢とされるスペインの傑作。騎士道物語への批判とリアリズムの開幕。", "古典学・古典文学", "Western_Europe", 1605, "https://en.wikipedia.org/wiki/Don_Quixote"),
    ("シェイクスピアの劇作", "Shakespeare's Plays", "エリザベス朝イングランドの劇作家シェイクスピアの36の戯曲。英語文学の最高峰。", "古典学・古典文学", "Western_Europe", 1590, "https://en.wikipedia.org/wiki/Shakespeare"),
    ("ゲーテのファウスト", "Goethe's Faust", "ドイツの詩人ゲーテの生涯の大作。悪魔との取引を通じた人間の苦悩と救済のドラマ。", "古典学・古典文学", "Western_Europe", 1808, "https://en.wikipedia.org/wiki/Faust_(Goethe)"),
    ("中国古典詩経", "Book of Songs (Shijing)", "中国最古の詩集。紀元前11〜7世紀の305篇を収める。孔子が編纂したとされる古典。", "古典学・古典文学", "East_Asia", -1000, "https://en.wikipedia.org/wiki/Classic_of_Poetry"),
    ("楚辞と屈原", "Chu Ci and Qu Yuan", "中国の詩人屈原が主要作者とされる楚の地域的詩集。離騒が代表作。", "古典学・古典文学", "East_Asia", -340, "https://en.wikipedia.org/wiki/Chu_ci"),
    ("史記と司馬遷", "Shiji and Sima Qian", "中国最初の紀伝体歴史書。黄帝から漢武帝までの通史と列伝からなる司馬遷の大著。", "古典学・古典文学", "East_Asia", -100, "https://en.wikipedia.org/wiki/Shiji"),
    ("古事記と日本神話", "Kojiki and Japanese Mythology", "712年に成立した日本最古の歴史書。神代から推古天皇までの神話・伝承・歴史。", "古典学・古典文学", "East_Asia", 712, "https://en.wikipedia.org/wiki/Kojiki"),
    ("源氏物語と王朝文学", "The Tale of Genji and Court Literature", "11世紀初頭に紫式部が書いた世界最古の長編小説。平安王朝の雅の世界を描く。", "古典学・古典文学", "East_Asia", 1008, "https://en.wikipedia.org/wiki/The_Tale_of_Genji"),
    ("万葉集と和歌", "Man'yoshu and Waka", "8世紀に成立した日本最古の歌集。4,500首以上の和歌を収める。", "古典学・古典文学", "East_Asia", 759, "https://en.wikipedia.org/wiki/Man%27y%C5%8Dsh%C5%AB"),
    ("マハーバーラタ", "Mahabharata", "古代インドの二大叙事詩の一つ。クルクシェートラ戦争を中心に倫理・哲学を展開する大著。", "古典学・古典文学", "South_Asia", -400, "https://en.wikipedia.org/wiki/Mahabharata"),
    ("ラーマーヤナ", "Ramayana", "ヴァールミーキに帰される古代インドの叙事詩。ラーマとシーターの物語は南・東南アジアに広まる。", "古典学・古典文学", "South_Asia", -500, "https://en.wikipedia.org/wiki/Ramayana"),
    ("カーリダーサの著作", "Kalidasa's Works", "古代インドサンスクリット文学最高の詩人。シャクンタラー・メーガドゥータが代表作。", "古典学・古典文学", "South_Asia", 400, "https://en.wikipedia.org/wiki/Kalidasa"),
    ("ギルガメシュ叙事詩", "Epic of Gilgamesh", "古代メソポタミアのシュメール・アッカド語叙事詩。洪水神話・友情・死の探求を主題とする。", "古典学・古典文学", "West_Asia_North_Africa", -2100, "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh"),
    ("千夜一夜物語", "One Thousand and One Nights", "アラビア語の枠組み物語集。ペルシア・インド・エジプト起源の説話を編纂した中世の傑作。", "古典学・古典文学", "West_Asia_North_Africa", 800, "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights"),
    ("コーランの文学性", "Literary Aspects of the Quran", "アラビア語文学の頂点としてのコーランの修辞・音楽性・不可模倣性（イジャーズ）の研究。", "古典学・古典文学", "West_Asia_North_Africa", 610, "https://en.wikipedia.org/wiki/Quran"),
    ("ルーミーのマスナヴィー", "Rumi's Masnavi", "13世紀ペルシア詩人ルーミーによる神秘主義詩集。スーフィズムの精神を詩に結晶させた。", "古典学・古典文学", "West_Asia_North_Africa", 1258, "https://en.wikipedia.org/wiki/Masnavi"),
    ("フィルダウスィーのシャーナーメ", "Ferdowsi's Shahnameh", "10-11世紀のペルシア詩人による英雄叙事詩。ペルシア民族の神話・歴史を60,000対句で詠む。", "古典学・古典文学", "West_Asia_North_Africa", 1010, "https://en.wikipedia.org/wiki/Shahnameh"),
    ("古代エジプト文学", "Ancient Egyptian Literature", "死者の書・シヌヘの物語・サトニ物語等の古代エジプトのヒエログリフ文学。", "古典学・古典文学", "West_Asia_North_Africa", -3000, "https://en.wikipedia.org/wiki/Ancient_Egyptian_literature"),
    ("スンジャータ叙事詩", "Sundiata Epic", "西アフリカ・マンデ族の英雄叙事詩。グリオーによって口承される。マリ帝国建国の物語。", "古典学・古典文学", "Sub_Saharan_Africa", 1235, "https://en.wikipedia.org/wiki/Sundiata_epic"),
    ("古代ナワトル文学", "Ancient Nahuatl Literature", "アステカ文明のナワトル語詩・神話・歴史記録。ネサワルコヨトルの詩が代表的。", "古典学・古典文学", "Latin_America", 1400, "https://en.wikipedia.org/wiki/Nahuatl_literature"),
    ("ポポル・ヴフ", "Popol Vuh", "マヤ族キチェーの神話・歴史書。天地創造・英雄双生児の物語を伝える。", "古典学・古典文学", "Latin_America", 1550, "https://en.wikipedia.org/wiki/Popol_Vuh"),
    ("インカの語りの伝統", "Inca Oral Traditions", "ケチュア語の神話・歌・歴史を伝えるインカ帝国の口承文化とキープによる記録。", "古典学・古典文学", "Latin_America", 1400, "https://en.wikipedia.org/wiki/Inca_mythology"),
    ("古典研究の方法論", "Classical Scholarship Methods", "校訂・注釈・翻訳・パピルス解読・碑文解析を含む古典文献学の方法論体系。", "古典学・古典文学", "Western_Europe", 1780, "https://en.wikipedia.org/wiki/Classical_scholarship"),
    ("ルネサンスの古典受容", "Renaissance Reception of Classics", "15-17世紀ヨーロッパにおけるギリシア・ローマ古典の再発見と人文主義的受容。", "古典学・古典文学", "Western_Europe", 1400, "https://en.wikipedia.org/wiki/Renaissance_humanism"),
    ("古代と近代の論争", "Querelle des Anciens et des Modernes", "17-18世紀フランスでの古代文化の優越か近代の進歩かをめぐる文学・知的論争。", "古典学・古典文学", "Western_Europe", 1687, "https://en.wikipedia.org/wiki/Quarrel_of_the_Ancients_and_the_Moderns"),
    ("古典古代の宗教と神話", "Religion and Myth in Classical Antiquity", "ギリシア・ローマの宗教・神話・儀礼の文学的表現と宗教史的分析。", "古典学・古典文学", "Western_Europe", -800, "https://en.wikipedia.org/wiki/Ancient_Greek_religion"),
    ("オルフェウス教とミステリア", "Orphism and Mystery Cults", "オルフェウス教・エレウシス・ディオニュソスのミステリア宗教と文学的表現。", "古典学・古典文学", "Western_Europe", -700, "https://en.wikipedia.org/wiki/Orphism_(religion)"),
    ("古典の植民地的受容", "Colonial Reception of Classics", "帝国主義とギリシア・ローマ古典の受容。古典教育が植民地支配に果たした役割の批判的研究。", "古典学・古典文学", "Global_Synthesis", 1800, "https://en.wikipedia.org/wiki/Classical_reception_studies"),
    ("クラシカル・レセプション・スタディーズ", "Classical Reception Studies", "古典の受容史を多文化・比較的に研究する現代の学問分野。", "古典学・古典文学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Classical_reception_studies"),
    ("デジタル古典学", "Digital Classics", "コーパス・OCR・デジタル写本・TEIエンコーディングによる古典文献のデジタル化研究。", "古典学・古典文学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Digital_humanities"),
    ("アレクサンドリア図書館と文献学", "Library of Alexandria and Philology", "古代アレクサンドリア図書館における古典文献の収集・校訂・注釈の活動。", "古典学・古典文学", "West_Asia_North_Africa", -300, "https://en.wikipedia.org/wiki/Library_of_Alexandria"),
]
CONCEPTS.extend(classics)

# ── 歴史学 +150 ──────────────────────────────────────────────────────
history = [
    ("史料批判", "Source Criticism", "歴史的文書・証拠の信頼性・出所・バイアスを評価する史学の基礎的方法論。", "歴史学・歴史哲学", "Western_Europe", 1800, "https://en.wikipedia.org/wiki/Source_criticism"),
    ("アナール学派", "Annales School", "フェーヴルとブロックが創設したフランス歴史学派。長期持続・地理・社会構造の重視。", "歴史学・歴史哲学", "Western_Europe", 1929, "https://en.wikipedia.org/wiki/Annales_school"),
    ("長期持続", "Longue Durée", "ブローデルが提唱した歴史の超長期的な時間スケール。地理・環境・構造が主役。", "歴史学・歴史哲学", "Western_Europe", 1958, "https://en.wikipedia.org/wiki/Longue_dur%C3%A9e"),
    ("ブローデルの地中海世界", "Braudel's Mediterranean", "フェルナン・ブローデルによる地中海16世紀の総合史。三つの時間スケールによる分析。", "歴史学・歴史哲学", "Western_Europe", 1949, "https://en.wikipedia.org/wiki/Fernand_Braudel"),
    ("ミクロ史学", "Microhistory", "ジンズバーグ・レヴィらが展開したイタリア発の個人・事件の精密な分析による歴史手法。", "歴史学・歴史哲学", "Western_Europe", 1976, "https://en.wikipedia.org/wiki/Microhistory"),
    ("グローバル・ヒストリー", "Global History", "国民国家を超えた地球規模の相互連関・移動・交流を分析する歴史学のアプローチ。", "歴史学・歴史哲学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Global_history"),
    ("帝国主義の歴史学", "History of Imperialism", "ヨーロッパ帝国主義の起源・展開・影響を多角的に研究する歴史学の分野。", "歴史学・歴史哲学", "Global_Synthesis", 1900, "https://en.wikipedia.org/wiki/Imperialism"),
    ("サバルタン研究", "Subaltern Studies", "グハらインド歴史家が創始した従属集団の声を発掘する歴史学とポストコロニアル批評。", "歴史学・歴史哲学", "South_Asia", 1982, "https://en.wikipedia.org/wiki/Subaltern_studies"),
    ("社会史", "Social History", "日常生活・労働・家族・ジェンダー・階級を中心に据えた歴史学の方法論。", "歴史学・歴史哲学", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Social_history"),
    ("文化史", "Cultural History", "象徴・表象・慣行・意味体系を中心に据えた歴史学のアプローチ。バーク・ハントが代表。", "歴史学・歴史哲学", "Western_Europe", 1980, "https://en.wikipedia.org/wiki/Cultural_history"),
    ("経済史", "Economic History", "過去の経済現象・制度・成長を歴史的に分析する学問分野。クライオメトリクスとの関係。", "歴史学・歴史哲学", "Western_Europe", 1890, "https://en.wikipedia.org/wiki/Economic_history"),
    ("政治史", "Political History", "国家・政府・権力・外交・戦争を中心とした伝統的な歴史学のアプローチ。", "歴史学・歴史哲学", "Western_Europe", -400, "https://en.wikipedia.org/wiki/Political_history"),
    ("外交史", "Diplomatic History", "国家間の外交関係・条約・国際秩序の歴史的展開を研究する分野。", "歴史学・歴史哲学", "Western_Europe", 1815, "https://en.wikipedia.org/wiki/Diplomatic_history"),
    ("軍事史", "Military History", "戦争・軍隊・戦略・武器技術の歴史的展開と社会との関係を研究する分野。", "歴史学・歴史哲学", "Western_Europe", -400, "https://en.wikipedia.org/wiki/Military_history"),
    ("知識社会学と科学史", "Sociology of Knowledge and History of Science", "科学的知識の社会的生産過程を歴史的・社会学的に研究する分野。クーン・マートンが先駆。", "歴史学・歴史哲学", "Western_Europe", 1962, "https://en.wikipedia.org/wiki/Sociology_of_scientific_knowledge"),
    ("歴史意識と集合的記憶", "Historical Consciousness and Collective Memory", "ハルブワックス・ノラが研究した社会集団の過去への関係性と記憶の社会的構成。", "歴史学・歴史哲学", "Western_Europe", 1925, "https://en.wikipedia.org/wiki/Collective_memory"),
    ("記憶の場", "Sites of Memory (Lieux de Mémoire)", "ノラが編集したフランスの記憶の場所・シンボル・慣習の研究。記念・忘却の弁証法。", "歴史学・歴史哲学", "Western_Europe", 1984, "https://en.wikipedia.org/wiki/Les_Lieux_de_M%C3%A9moire"),
    ("歴史的外傷と記憶", "Historical Trauma and Memory", "ホロコースト・奴隷制・ジェノサイドの記憶の伝承と世代を超えたトラウマの研究。", "歴史学・歴史哲学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Cultural_trauma"),
    ("歴史的方法論論争", "Historiographical Controversies", "歴史学の方法論・客観性・ナラティブをめぐる専門的論争。実証主義と解釈学の対立。", "歴史学・歴史哲学", "Western_Europe", 1800, "https://en.wikipedia.org/wiki/Historiography"),
    ("国民国家と歴史叙述", "Nation-State and Historiography", "ナショナル・ヒストリーの形成と国民国家の歴史的正当化の関係。アンダーソン・ホブズボウムが分析。", "歴史学・歴史哲学", "Global_Synthesis", 1800, "https://en.wikipedia.org/wiki/National_history"),
    ("帝国史とポストコロニアル歴史学", "Imperial History and Postcolonial Historiography", "植民地主義の歴史叙述を批判的に再検討するポストコロニアル歴史学。", "歴史学・歴史哲学", "Global_Synthesis", 1978, "https://en.wikipedia.org/wiki/Postcolonial_theory"),
    ("歴史と伝記", "History and Biography", "個人の生涯の叙述と構造的・社会的説明の関係。英雄的歴史観の批判と復権。", "歴史学・歴史哲学", "Western_Europe", -400, "https://en.wikipedia.org/wiki/Biography"),
    ("環境史", "Environmental History", "人間と自然環境の相互作用の歴史的展開を研究する分野。クロスビー・マクニールが代表。", "歴史学・歴史哲学", "North_America", 1970, "https://en.wikipedia.org/wiki/Environmental_history"),
    ("気候史", "Climate History", "過去の気候変動が人間社会に与えた影響を研究する歴史学の分野。", "歴史学・歴史哲学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Historical_climatology"),
    ("感情の歴史", "History of Emotions", "過去の社会における感情の経験・表現・規範を研究する比較的新しい歴史学の分野。", "歴史学・歴史哲学", "Western_Europe", 2000, "https://en.wikipedia.org/wiki/History_of_emotions"),
    ("歴史人口学", "Historical Demography", "過去の人口動態・死亡率・出生率・移動を文書から再構成する学際的分野。", "歴史学・歴史哲学", "Western_Europe", 1950, "https://en.wikipedia.org/wiki/Historical_demography"),
    ("家族史", "Family History", "家族構造・親族関係・家内経済の歴史的変化を研究する社会史の一分野。", "歴史学・歴史哲学", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Family_history"),
    ("ジェンダー史", "Gender History", "歴史的変化の中でジェンダーが構築・変容・権力と結びついてきた過程を研究する分野。", "歴史学・歴史哲学", "North_America", 1975, "https://en.wikipedia.org/wiki/Gender_history"),
    ("女性史", "Women's History", "歴史上の女性の経験・役割・貢献を発掘し再評価する歴史学の分野。", "歴史学・歴史哲学", "North_America", 1970, "https://en.wikipedia.org/wiki/Women%27s_history"),
    ("労働史", "Labor History", "労働者・労働運動・労働条件の歴史的展開を研究する社会史の分野。", "歴史学・歴史哲学", "Western_Europe", 1880, "https://en.wikipedia.org/wiki/Labor_history"),
    ("奴隷制の歴史", "History of Slavery", "古代から近代までの奴隷制の諸形態・規模・廃止運動を研究する歴史学。", "歴史学・歴史哲学", "Global_Synthesis", -3000, "https://en.wikipedia.org/wiki/History_of_slavery"),
    ("黒大西洋", "Black Atlantic", "ポール・ギルロイの概念。大西洋を跨いだアフリカ系文化の移動・交流・変容の歴史。", "歴史学・歴史哲学", "Global_Synthesis", 1993, "https://en.wikipedia.org/wiki/The_Black_Atlantic"),
    ("大西洋奴隷貿易", "Atlantic Slave Trade", "15-19世紀にかけてアフリカから新世界へ強制移住させられた人々の歴史。", "歴史学・歴史哲学", "Global_Synthesis", 1440, "https://en.wikipedia.org/wiki/Atlantic_slave_trade"),
    ("グローバル・サウスの歴史", "History of the Global South", "ラテンアメリカ・アフリカ・アジアの従属的・周辺的発展の歴史を描くアプローチ。", "歴史学・歴史哲学", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Global_South"),
    ("インド洋世界史", "Indian Ocean World History", "インド洋を結ぶ交易・宗教・文化の長期的ネットワークの歴史。チャウドゥリが代表。", "歴史学・歴史哲学", "Global_Synthesis", 1985, "https://en.wikipedia.org/wiki/Indian_Ocean"),
    ("シルクロードの歴史", "Silk Road History", "中央アジアを貫く交易路の文化・宗教・商品の交流史。", "歴史学・歴史哲学", "Global_Synthesis", -206, "https://en.wikipedia.org/wiki/Silk_Road"),
    ("ビッグ・ヒストリー", "Big History", "ビッグバンから現代までの138億年を統合的に語る超長期的歴史叙述。クリスチャンが代表。", "歴史学・歴史哲学", "Global_Synthesis", 1989, "https://en.wikipedia.org/wiki/Big_History"),
    ("技術史", "History of Technology", "道具・機械・インフラ・エネルギーの技術的発展とその社会的影響の歴史的研究。", "歴史学・歴史哲学", "Western_Europe", 1800, "https://en.wikipedia.org/wiki/History_of_technology"),
    ("医療史", "History of Medicine", "医学的知識・制度・実践の歴史的変遷。患者の経験・医師の権威・病の文化的構成。", "歴史学・歴史哲学", "Western_Europe", -400, "https://en.wikipedia.org/wiki/History_of_medicine"),
    ("都市史", "Urban History", "都市の形成・変容・社会的空間の歴史的研究。産業化・近代化・グローバル化との関係。", "歴史学・歴史哲学", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Urban_history"),
    ("宗教改革史", "History of the Reformation", "16世紀ヨーロッパの宗教改革の原因・展開・影響の歴史的研究。", "歴史学・歴史哲学", "Western_Europe", 1517, "https://en.wikipedia.org/wiki/Reformation"),
    ("革命の比較史", "Comparative History of Revolutions", "フランス・ロシア・中国・キューバの革命を比較分析する歴史社会学的研究。", "歴史学・歴史哲学", "Global_Synthesis", 1789, "https://en.wikipedia.org/wiki/Revolution"),
    ("冷戦史", "Cold War History", "1945-1991年の米ソ対立とその世界的波及の歴史。文書公開後の再評価が進む。", "歴史学・歴史哲学", "Global_Synthesis", 1945, "https://en.wikipedia.org/wiki/Cold_War"),
    ("脱植民地化の歴史", "History of Decolonization", "第二次大戦後の植民地独立運動と新国家建設の歴史的プロセス。", "歴史学・歴史哲学", "Global_Synthesis", 1945, "https://en.wikipedia.org/wiki/Decolonization"),
    ("暴力と歴史", "Violence and History", "ジェノサイド・虐殺・内戦・構造的暴力の歴史的分析と比較研究。", "歴史学・歴史哲学", "Global_Synthesis", 1945, "https://en.wikipedia.org/wiki/Political_violence"),
    ("歴史的正義と修復的正義", "Historical Justice and Restorative Justice", "過去の不正義への謝罪・補償・和解の政治的・法的プロセスの研究。", "歴史学・歴史哲学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Transitional_justice"),
    ("歴史認識問題", "Historical Consciousness Disputes", "日本・韓国・中国・ヨーロッパの過去の歴史認識の違いと外交的影響の比較研究。", "歴史学・歴史哲学", "East_Asia", 1990, "https://en.wikipedia.org/wiki/Historical_revisionism_(negationism)"),
    ("デジタル歴史学", "Digital History", "デジタル技術・データベース・可視化を歴史研究に活用する新分野。", "歴史学・歴史哲学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Digital_history"),
    ("公衆史学", "Public History", "博物館・記念碑・映画・観光を通じた一般公衆への歴史の提示と活用を研究する分野。", "歴史学・歴史哲学", "North_America", 1978, "https://en.wikipedia.org/wiki/Public_history"),
]
CONCEPTS.extend(history)

# ── 言語学補完 +100 ──────────────────────────────────────────────────
linguistics = [
    ("談話分析", "Discourse Analysis", "文レベルを超えた発話・テクスト・会話の構造と機能を分析する言語学の分野。", "言語学", "Western_Europe", 1952, "https://en.wikipedia.org/wiki/Discourse_analysis"),
    ("批判的談話分析", "Critical Discourse Analysis", "フェアクラフ・ヴォダクが展開した権力・イデオロギーと言語の関係を分析するアプローチ。", "言語学", "Western_Europe", 1989, "https://en.wikipedia.org/wiki/Critical_discourse_analysis"),
    ("会話分析", "Conversation Analysis", "ガーフィンケル・サックスらが開発した会話の順番交替・修復・隣接対の詳細分析。", "言語学", "North_America", 1964, "https://en.wikipedia.org/wiki/Conversation_analysis"),
    ("インターアクション分析", "Interaction Analysis", "対面・コンピューター介在の相互作用を音声・映像で詳細に分析するアプローチ。", "言語学", "North_America", 1990, "https://en.wikipedia.org/wiki/Interaction_analysis"),
    ("言語とアイデンティティ", "Language and Identity", "言語選択・コード切り替え・スタイルシフティングとアイデンティティ構築の関係。", "言語学", "Global_Synthesis", 1980, "https://en.wikipedia.org/wiki/Language_and_identity"),
    ("言語権", "Language Rights", "言語的少数者の教育・司法・行政における言語使用の権利をめぐる政治・法的議論。", "言語学", "Global_Synthesis", 1966, "https://en.wikipedia.org/wiki/Linguistic_rights"),
    ("危機言語", "Endangered Languages", "消滅の危機に瀕している言語の記録・保存・再活性化をめぐる言語学的・社会的問題。", "言語学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Language_death"),
    ("言語復興", "Language Revitalization", "ヘブライ語・ウェールズ語・マオリ語等の衰退した言語を社会的に復元する運動と研究。", "言語学", "Global_Synthesis", 1900, "https://en.wikipedia.org/wiki/Language_revitalization"),
    ("言語接触と収束", "Language Contact and Convergence", "異なる言語の話者が接触した際に起きる相互影響・混合・収束現象の研究。", "言語学", "Global_Synthesis", -1900, "https://en.wikipedia.org/wiki/Language_contact"),
    ("ピジン語とクレオール語", "Pidgin and Creole Languages", "接触場面で生まれた混合言語の特性・形成過程・文法を研究する接触言語学の中核。", "言語学", "Global_Synthesis", 1800, "https://en.wikipedia.org/wiki/Pidgin"),
    ("方言学と地理言語学", "Dialectology and Geolinguistics", "方言の地理的分布・境界・変化を地図で記録・分析する言語学の分野。", "言語学", "Western_Europe", 1876, "https://en.wikipedia.org/wiki/Dialectology"),
    ("変異理論", "Variation Theory", "ラボフが創始した言語変異のパターンと社会的条件の定量的研究。", "言語学", "North_America", 1963, "https://en.wikipedia.org/wiki/Variation_(linguistics)"),
    ("言語変化のメカニズム", "Mechanisms of Language Change", "音変化・文法変化・語彙変化がどのように起こるかの言語学的説明理論。", "言語学", "Western_Europe", 1870, "https://en.wikipedia.org/wiki/Language_change"),
    ("格文法", "Case Grammar", "フィルモアが提案した動詞と名詞句の深層格的関係を分析する文法理論。", "言語学", "North_America", 1968, "https://en.wikipedia.org/wiki/Case_grammar"),
    ("機能文法", "Functional Grammar", "ハリデーのシステミック機能文法・ダイクのテクスト言語学等の機能主義的文法理論。", "言語学", "Western_Europe", 1961, "https://en.wikipedia.org/wiki/Functional_theories_of_grammar"),
    ("システミック機能言語学", "Systemic Functional Linguistics", "ハリデーが展開した言語を社会的な意味の資源として分析するアプローチ。", "言語学", "Western_Europe", 1961, "https://en.wikipedia.org/wiki/Systemic_functional_linguistics"),
    ("語用論的語用化", "Pragmaticalization", "語彙・文法的要素が語用論的機能を獲得していく歴史的過程の研究。", "言語学", "Western_Europe", 1990, "https://en.wikipedia.org/wiki/Grammaticalization"),
    ("節タイプと情報構造", "Clause Types and Information Structure", "主語・焦点・トピックなどの情報構造が文法に反映されるメカニズムの研究。", "言語学", "Western_Europe", 1970, "https://en.wikipedia.org/wiki/Information_structure"),
    ("能格言語", "Ergative Language", "主語と目的語でなく、自動詞主語と他動詞主語を異なる格でマークする言語類型。", "言語学", "Global_Synthesis", -1900, "https://en.wikipedia.org/wiki/Ergative%E2%80%93absolutive_alignment"),
    ("話題卓越型言語", "Topic-Prominent Language", "主語でなくトピックを文の基本単位とする言語類型。中国語・日本語が代表例。", "言語学", "East_Asia", 1976, "https://en.wikipedia.org/wiki/Topic-prominent_language"),
    ("敬語体系の研究", "Honorific Systems", "日本語・朝鮮語・ジャワ語等の複雑な敬語体系を社会言語学・語用論的に分析する研究。", "言語学", "East_Asia", -1900, "https://en.wikipedia.org/wiki/Honorifics_(linguistics)"),
    ("語彙の意味論", "Lexical Semantics", "単語の意味・多義性・類義語・意味場・意味変化を研究する意味論の一分野。", "言語学", "Western_Europe", 1900, "https://en.wikipedia.org/wiki/Lexical_semantics"),
    ("フレーム意味論", "Frame Semantics", "フィルモアが提案した語の意味を文化的フレームとの関係で理解する意味論理論。", "言語学", "North_America", 1976, "https://en.wikipedia.org/wiki/Frame_semantics_(linguistics)"),
    ("形式意味論", "Formal Semantics", "モデル理論・可能世界意味論・ラムダ計算等を用いた数理的意味論。モンタギュー文法。", "言語学", "North_America", 1970, "https://en.wikipedia.org/wiki/Formal_semantics_(linguistics)"),
    ("言語相対性の実証研究", "Empirical Studies of Linguistic Relativity", "色彩・空間・数・時間概念の言語横断比較研究。サピア・ウォーフの弱い版の実証。", "言語学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Linguistic_relativity"),
    ("音韻論の優化理論", "Optimality Theory", "プリンス・スモレンスキーが提案した制約の優先順位づけによる音韻論理論。", "言語学", "North_America", 1991, "https://en.wikipedia.org/wiki/Optimality_theory"),
    ("音調言語学", "Tone Languages", "声調が語の意味を弁別する中国語・タイ語・バントゥー語族等の音調言語の研究。", "言語学", "Global_Synthesis", -1900, "https://en.wikipedia.org/wiki/Tone_(linguistics)"),
    ("手話言語学", "Sign Language Linguistics", "聴覚障害者の手話を完全な言語として分析する言語学的研究。ストーコーが先駆。", "言語学", "North_America", 1960, "https://en.wikipedia.org/wiki/Sign_language_linguistics"),
    ("神経言語学", "Neurolinguistics", "言語処理の神経基盤を研究する学際的分野。ブローカ・ウェルニッケ失語から機能的MRIまで。", "言語学", "Western_Europe", 1861, "https://en.wikipedia.org/wiki/Neurolinguistics"),
    ("言語の進化", "Evolution of Language", "人間の言語能力の進化的起源をめぐる言語学・進化生物学・認知科学の学際的研究。", "言語学", "Global_Synthesis", 1990, "https://en.wikipedia.org/wiki/Evolution_of_language"),
    ("コーパス言語学手法", "Corpus Linguistics Methods", "大規模テクストコーパスの構築・タグ付け・統計分析を用いた言語研究の方法論。", "言語学", "Western_Europe", 1990, "https://en.wikipedia.org/wiki/Corpus_linguistics"),
    ("言語習得の臨界期仮説", "Critical Period Hypothesis", "レネバーグが提案した第一言語習得の生物学的に制約された臨界期の存在。", "言語学", "North_America", 1967, "https://en.wikipedia.org/wiki/Critical_period_hypothesis"),
    ("バイリンガリズムと言語処理", "Bilingualism and Language Processing", "二言語話者の脳内での言語分離・混合・切り替えの神経認知的研究。", "言語学", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Bilingualism"),
    ("言語政策と計画", "Language Policy and Planning", "国家・地域の言語選択・標準化・少数言語保護の政策的決定と実施の研究。", "言語学", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Language_policy"),
    ("言語の類型横断的普遍性", "Cross-linguistic Universals", "ガンツによる45の言語普遍性・グリーンバーグの語順普遍性等の類型論的研究。", "言語学", "North_America", 1963, "https://en.wikipedia.org/wiki/Language_universal"),
    ("会話における推論と含意", "Conversational Implicature", "グライスの協調原則と推論ベースの語用論。言語の明示的意味を超えた伝達の仕組み。", "言語学", "Western_Europe", 1975, "https://en.wikipedia.org/wiki/Conversational_implicature"),
    ("指示表現とインデクシカリティ", "Indexicality and Reference", "ここ・今・私等の指示表現の意味論と語用論。パース・バーリン・カプランが分析。", "言語学", "North_America", 1892, "https://en.wikipedia.org/wiki/Indexicality"),
    ("文体論とレジスター", "Register and Style", "特定の社会的状況に適した言語的スタイル・フォーマリティ・ジャンルの使い分けの研究。", "言語学", "Western_Europe", 1960, "https://en.wikipedia.org/wiki/Register_(sociolinguistics)"),
    ("言語とジェンダー", "Language and Gender", "ジェンダーが言語使用・語用論・談話に反映される方法の社会言語学的研究。", "言語学", "North_America", 1975, "https://en.wikipedia.org/wiki/Language_and_gender"),
    ("アフリカ諸語の研究", "African Languages Studies", "ニジェール・コンゴ語族・アフロ・アジア語族・コイサン諸語の言語学的研究。", "言語学", "Sub_Saharan_Africa", -1900, "https://en.wikipedia.org/wiki/Languages_of_Africa"),
    ("オーストラリア先住民語", "Australian Aboriginal Languages", "250以上のオーストラリア先住民言語の多様性・構造・危機・記録の研究。", "言語学", "Global_Synthesis", -1900, "https://en.wikipedia.org/wiki/Australian_Aboriginal_languages"),
    ("アメリカ先住民語言語学", "Native American Languages Linguistics", "アルゴンキン・ナバホ・ユト・アステカ等の多様な北米先住民言語の記述的研究。", "言語学", "North_America", 1788, "https://en.wikipedia.org/wiki/Indigenous_languages_of_the_Americas"),
    ("意味変化の理論", "Theories of Semantic Change", "語の意味が歴史的に拡大・縮小・転換・向上・低下する過程のメカニズム論。", "言語学", "Western_Europe", 1880, "https://en.wikipedia.org/wiki/Semantic_change"),
    ("ナラティブ分析と言語学", "Narrative Analysis in Linguistics", "ラボフの口述ナラティブ分析から自然談話の物語構造を研究する社会言語学的アプローチ。", "言語学", "North_America", 1967, "https://en.wikipedia.org/wiki/Narrative_inquiry"),
    ("文字論と書字システム", "Writing Systems and Grammatology", "アルファベット・シラバリー・ロゴグラフィーなど文字体系の類型と機能の研究。", "言語学", "Global_Synthesis", -3200, "https://en.wikipedia.org/wiki/Writing_system"),
    ("対照言語学", "Contrastive Linguistics", "2つ以上の言語を体系的に比較して差異を記述する言語学の分野。外国語教育に応用。", "言語学", "Global_Synthesis", 1950, "https://en.wikipedia.org/wiki/Contrastive_linguistics"),
    ("第二言語習得の普遍的文法仮説", "UG Hypothesis in SLA", "チョムスキーの普遍文法が第二言語習得にも働くかをめぐる研究。ホワイトが代表。", "言語学", "North_America", 1985, "https://en.wikipedia.org/wiki/Universal_grammar"),
    ("言語間転移", "Language Transfer", "母語の音韻・文法・語彙が第二言語習得に影響を与える正の転移と負の転移の研究。", "言語学", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Language_transfer"),
    ("インプット仮説とアウトプット仮説", "Input and Output Hypotheses", "クラシェンのインプット仮説とスウェインのアウトプット仮説の第二言語習得理論。", "言語学", "North_America", 1981, "https://en.wikipedia.org/wiki/Input_hypothesis"),
    ("言語教育と教授法", "Language Teaching Methodology", "コミュニカティブ・アプローチ・タスク基盤教授法・内容統合型言語教育等の理論と実践。", "言語学", "Global_Synthesis", 1960, "https://en.wikipedia.org/wiki/Language_education"),
]
CONCEPTS.extend(linguistics)

def main():
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=WAL")
    cur = con.cursor()

    existing = set(r[0] for r in cur.execute(
        "SELECT name_en FROM humanities_concept WHERE name_en IS NOT NULL").fetchall())

    inserted = skipped = 0
    batch = []

    for (name_ja, name_en, definition, subfield, culture_region, era_start, source_url) in CONCEPTS:
        if name_en in existing:
            skipped += 1
            continue
        existing.add(name_en)
        cid = gen_id()
        batch.append((cid, name_ja, name_en, definition, subfield, culture_region,
                       era_start, source_url, NOW, NOW))
        inserted += 1
        if len(batch) >= 500:
            cur.executemany("""INSERT INTO humanities_concept
                (id,name_ja,name_en,definition,subfield,culture_region,
                 era_start,source_url,verification_status,quality_flag,
                 status,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                [(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],'url_present','dua_wave_a2','active',r[8],r[9]) for r in batch])
            con.commit()
            batch = []

    if batch:
        cur.executemany("""INSERT INTO humanities_concept
            (id,name_ja,name_en,definition,subfield,culture_region,
             era_start,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            [(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],'url_present','dua_wave_a2','active',r[8],r[9]) for r in batch])
        con.commit()

    total = cur.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
    print(f"Batch 6: inserted={inserted}, skipped={skipped}")
    print(f"総件数: {total} (目標5500)")
    rows = cur.execute("SELECT subfield, COUNT(*) FROM humanities_concept GROUP BY subfield ORDER BY COUNT(*) DESC LIMIT 15").fetchall()
    for r in rows:
        print(f"  {r[0]}: {r[1]}")
    con.close()

if __name__ == "__main__":
    main()
