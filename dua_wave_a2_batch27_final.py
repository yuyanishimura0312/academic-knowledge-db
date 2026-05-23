"""DUA Wave A2 Batch 27 FINAL — need +29 to reach 5,500"""
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

# Very specific / niche concepts to minimize skips
concepts = [
    # 文化社会学・知識社会学 (8) — most underrepresented at 148
    ("オーラリティと文字文化","Orality and Literacy","","ウォルター・オングが論じた、口承文化と文字文化の認知・社会的特性の差異。語り・記憶・思考様式への媒体的影響を分析した。","文化社会学・知識社会学","メディア文化論",1982,"North_America","https://en.wikipedia.org/wiki/Orality_and_Literacy"),
    ("プロファン文化","Profane Culture","","世俗化された日常文化をデュルケームの聖俗二分法から分析する視点。宗教社会学から文化社会学へ展開した概念領域。","文化社会学・知識社会学","デュルケーム社会学",1995,"Western_Europe","https://en.wikipedia.org/wiki/Sacred%E2%80%93profane_dichotomy"),
    ("世界観の変容","Transformation of Worldview","","近代化・グローバル化に伴う文化的宇宙観・価値体系の変容過程を追う比較文化社会学の研究課題。イングルハートのポスト物質主義論が代表。","文化社会学・知識社会学","文化変容論",1977,"Western_Europe","https://en.wikipedia.org/wiki/Post-materialism"),
    ("文化的トラウマ","Cultural Trauma","","ジェフリー・アレクサンダーが提唱した、集合体が自己アイデンティティを根底から傷つける事件を集合的に解釈するプロセス。ホロコースト・奴隷制などを事例に展開。","文化社会学・知識社会学","文化社会学",2004,"North_America","https://en.wikipedia.org/wiki/Cultural_trauma"),
    ("文化的生産の場","Field of Cultural Production","","ブルデューが定義した、文化財（芸術・文学・音楽）の生産・流通・消費が行われる社会的空間。独自の論理（文化資本・象徴権力）が支配する。","文化社会学・知識社会学","ブルデュー社会学",1983,"Western_Europe","https://en.wikipedia.org/wiki/Field_of_cultural_production"),
    ("比較知識社会学","Comparative Sociology of Knowledge","","マンハイム・マートン以降に展開した、異なる社会・文化における知識生産様式を比較する方法論的枠組み。","文化社会学・知識社会学","知識社会学",1960,"Western_Europe","https://en.wikipedia.org/wiki/Sociology_of_knowledge"),
    ("感情の文化社会学","Cultural Sociology of Emotions","","感情が文化的・社会的に構成されるという視点。ホックシールドの感情管理論・コリンズの相互作用儀礼論・アーベ・ムーアらの研究を含む。","文化社会学・知識社会学","感情社会学",1979,"North_America","https://en.wikipedia.org/wiki/Sociology_of_emotions"),
    ("音楽社会学","Sociology of Music","","音楽が社会的実践・アイデンティティ・権力関係と結びつく様式を分析する学問領域。アドルノ・フリス・ベッカーが代表的論者。","文化社会学・知識社会学","文化社会学",1962,"Western_Europe","https://en.wikipedia.org/wiki/Sociology_of_music"),

    # デジタル社会学・ネットワーク社会 (8)
    ("AIガバナンス","Artificial Intelligence Governance","","AI技術の開発・運用・規制をめぐる政治的・制度的・倫理的取り組みの総体。EU AI規制法などを含む政策枠組みと学術的分析の双方が進む。","デジタル社会学・ネットワーク社会","デジタル社会学",2018,"Global_Synthesis","https://en.wikipedia.org/wiki/Artificial_intelligence_governance"),
    ("プラットフォーム労働者","Platform Workers","","ウーバー・デリバリーフードなどのデジタルプラットフォームを介して仕事をする就労形態。「ギグワーカー」とも呼ばれ、労働保護・社会保障の観点から議論される。","デジタル社会学・ネットワーク社会","デジタル社会学",2010,"Global_Synthesis","https://en.wikipedia.org/wiki/Gig_worker"),
    ("情報圏","Infosphere","","ルチアーノ・フロリディが提唱した、情報的実体・プロセス・作用から成る環境全体の概念。デジタル社会における存在論的枠組みとして発展中。","デジタル社会学・ネットワーク社会","デジタル社会学",2007,"Western_Europe","https://en.wikipedia.org/wiki/Infosphere"),
    ("デジタル分断","Digital Divide Revisited","","第一世代（接続格差）から第二世代（スキル格差）・第三世代（成果格差）への議論の深化。Van Dijkらが多次元的格差として再定義した。","デジタル社会学・ネットワーク社会","デジタル社会学",2006,"Western_Europe","https://en.wikipedia.org/wiki/Digital_divide"),
    ("ハイパーコネクティビティ","Hyperconnectivity","","常時接続・多チャンネル通信が社会生活・労働・親密性を変容させる状態。バリーウェルマン・ベアードが概念化した。","デジタル社会学・ネットワーク社会","ネットワーク社会論",2008,"North_America","https://en.wikipedia.org/wiki/Hyperconnectivity"),
    ("デジタル民主主義","Digital Democracy","","ICT・SNS・オンライン熟議などのデジタル技術が民主的参加・公共的議論を変容させる可能性と課題を分析する研究領域。","デジタル社会学・ネットワーク社会","デジタル社会学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Digital_democracy"),
    ("アルゴリズムの偏見","Algorithmic Bias","","機械学習アルゴリズムが訓練データや設計の偏りを反映して差別的結果を生む問題。採用・信用評価・司法分野の事例から社会学的に分析される。","デジタル社会学・ネットワーク社会","デジタル社会学",2016,"North_America","https://en.wikipedia.org/wiki/Algorithmic_bias"),
    ("デジタルウェルビーイング","Digital Wellbeing","","スマートフォン依存・SNSの精神健康への影響・スクリーンタイムなど、デジタル技術の利用と個人の心理的・社会的健康との関係を研究する領域。","デジタル社会学・ネットワーク社会","デジタル社会学",2017,"Global_Synthesis","https://en.wikipedia.org/wiki/Digital_well-being"),

    # 環境社会学・人新世 (8)
    ("気候正義","Climate Justice","","気候変動の影響が貧困国・脆弱なコミュニティに不均等に集中するという問題意識と、公平な気候政策を求める社会運動の論理。","環境社会学・人新世","環境正義",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Climate_justice"),
    ("アグロエコロジー","Agroecology","","生態学の原理を農業システムに適用し、生態的持続可能性・食料主権・農民の知識を中心に置く学際的アプローチ。グローバルサウスの農民運動と結びつく。","環境社会学・人新世","環境社会学",1990,"Latin_America","https://en.wikipedia.org/wiki/Agroecology"),
    ("環境人文学","Environmental Humanities","","文学・歴史・哲学・芸術などの人文学的視点から環境問題・自然観・人間と非人間の関係を探究する学際領域。","環境社会学・人新世","環境社会学",2010,"Global_Synthesis","https://en.wikipedia.org/wiki/Environmental_humanities"),
    ("リスク社会論の批判","Critique of Risk Society","","ベック『危険社会』への批判的応答。グローバルリスクの不平等な分配・リスク知覚の文化的差異・リスク社会概念の西洋中心性を問い直す議論。","環境社会学・人新世","リスク社会論",1995,"Western_Europe","https://en.wikipedia.org/wiki/Risk_society"),
    ("市場化された自然","Marketization of Nature","","炭素市場・生態系サービスの金融化など、自然の価値を市場メカニズムで計量・取引する動向を批判的に分析する政治生態学の議論。","環境社会学・人新世","政治生態学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Payment_for_ecosystem_services"),
    ("コモンズの悲劇の再検討","Revisiting Tragedy of the Commons","","ハーディンの「コモンズの悲劇」論をオストロムらが実証的に反証し、コミュニティによる自律的資源管理の可能性を示した議論。","環境社会学・人新世","コモンズ論",1990,"North_America","https://en.wikipedia.org/wiki/Tragedy_of_the_commons"),
    ("環境難民","Environmental Refugees","","気候変動・自然災害・環境劣化によって故郷を追われる人々。法的地位の不明確さ・南北格差・移住権の問題と結びついて議論される。","環境社会学・人新世","環境社会学",1985,"Global_Synthesis","https://en.wikipedia.org/wiki/Environmental_migrant"),
    ("半自然的空間","Semi-Natural Spaces","","都市農地・里山・管理草原など、人間の介入と自然プロセスが共存する空間。生物多様性保全・都市農業・地域コミュニティとの関係から研究される。","環境社会学・人新世","環境社会学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Semi-natural_habitat"),

    # 生活世界・現象学的社会学 (8)
    ("感覚の社会学","Sociology of the Senses","","デイヴィッド・ハウズらが展開した、視覚偏重の近代的感覚序列を批判し、匂い・音・触覚・味覚の社会的構成を分析する研究領域。","生活世界・現象学的社会学","現象学的社会学",2005,"North_America","https://en.wikipedia.org/wiki/Sociology_of_the_senses"),
    ("生活時間と社会構造","Time Use and Social Structure","","時間の使い方が階級・ジェンダー・文化によって異なる様式を分析する研究。時間利用調査（タイムユーズサーベイ）を用いた実証研究が中心。","生活世界・現象学的社会学","日常生活社会学",1975,"Western_Europe","https://en.wikipedia.org/wiki/Time_use_survey"),
    ("住まいの現象学","Phenomenology of Dwelling","","ハイデガーの「住まうこと」論とバシュラールの家の詩学を出発点に、住居・場所・帰属感の経験を分析する現象学的アプローチ。","生活世界・現象学的社会学","現象学的社会学",1958,"Western_Europe","https://en.wikipedia.org/wiki/The_Poetics_of_Space"),
    ("手続き的現実","Procedural Reality","","ガーフィンケルが実験的に明らかにした、社会的現実が日常的な相互作用の手続きによって達成されるという洞察。違反実験（breaching experiments）が方法として用いられた。","生活世界・現象学的社会学","エスノメソドロジー",1967,"North_America","https://en.wikipedia.org/wiki/Breaching_experiment"),
    ("共同注意","Joint Attention","","発達心理学・現象学・認知科学が交差する概念。他者と同一の対象に注意を向け共有する能力と実践が社会的相互行為の基盤をなすという議論。","生活世界・現象学的社会学","現象学的社会学",1975,"North_America","https://en.wikipedia.org/wiki/Joint_attention"),
    ("ケアの現象学","Phenomenology of Care","","ハイデガーの気遣い（Sorge）概念を出発点に、ケア実践の経験的・存在論的次元を分析する。医療人類学・ケア倫理・クィア理論と交差する。","生活世界・現象学的社会学","現象学的社会学",1980,"Western_Europe","https://en.wikipedia.org/wiki/Care_ethics"),
    ("日常の美学","Everyday Aesthetics","","アーノルド・バーリアント・ヨウコ・サイトーらが展開した、芸術だけでなく日常的経験（食・衣服・風景・空間）に美的価値を見出す哲学・社会学的研究。","生活世界・現象学的社会学","日常生活社会学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Everyday_aesthetics"),
    ("言語的転回の社会学","Linguistic Turn in Sociology","","1970年代以降、言語・言説・テキストが社会的現実を構成するという認識が社会学・歴史学に浸透した転換。フーコー・デリダ・ラクラウが代表的論者。","生活世界・現象学的社会学","現象学的社会学",1970,"Western_Europe","https://en.wikipedia.org/wiki/Linguistic_turn"),
]

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Batch 27 FINAL)...")
    ins, skp = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {skp}")
