#!/usr/bin/env python3
"""Wave 26 / C34: lit_theory subfield expansion +30 concepts.
5 thematic clusters x 6 concepts each, complementing existing entries.
"""
import sqlite3, os, sys

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SUBFIELD_ID = 22  # lit_theory

# 30 concepts: 5 clusters x 6
# Each: (name_ja, name_en, name_original, original_script, region, period_id, definition<=100, importance, fourth_status, fourth_note, source_tier, canonical_in_region)
CONCEPTS = [
    # Cluster 1: Genre theory (avoid duplicates of existing Genette/Derrida/Todorov/Booth/Bakhtin/Frye core entries)
    ("フライ『批評の解剖』モード論", "Frye Anatomy of Criticism Modes", "Anatomy of Criticism", "latin", "西欧", 125,
     "フライが主人公の力に応じて文学を5モード（神話・ロマンス・高位模倣・低位模倣・皮肉）に区分する理論。", 4, "partial",
     "AI生成物のモード判定とジャンル系譜の自動分類に再応用される。", "primary", "西欧"),
    ("ジュネット『アルシテクスト序説』ジャンル理論", "Genette Architext Genre Theory", "Introduction à l'architexte", "latin", "西欧", 125,
     "ジュネットがアリストテレス以来のジャンル分類の歴史的誤読を批判し、テクスト性の階層を再構築した試み。", 4, "partial",
     "デジタル時代のジャンル混淆とトランステクスチュアリテに継承される。", "primary", "西欧"),
    ("デリダ「ジャンルの法」原理", "Derrida The Law of Genre Principle", "La loi du genre", "latin", "西欧", 125,
     "デリダがジャンルは参加せずに帰属させると述べ、純粋ジャンルの不可能性と境界侵犯の必然性を論証した法則。", 5, "rethinking",
     "AI生成物の境界侵犯とジャンル汚染を考える理論的基盤として再評価。", "primary", "西欧"),
    ("トドロフ幻想ジャンルの3条件", "Todorov Fantastic Three Conditions", "Introduction à la littérature fantastique", "latin", "西欧", 125,
     "トドロフが幻想文学を超自然と自然の解釈の躊躇によって定義し、奇怪・驚異との3区分を立てたジャンル理論。", 4, "invariant",
     "ホラー・SF・スペキュレイティブ・フィクション分析の核心枠組み。", "primary", "西欧"),
    ("ブース『小説の修辞学』内包作者論", "Booth Rhetoric of Fiction Implied Author", "The Rhetoric of Fiction", "latin", "西欧", 125,
     "ブースが小説のジャンル的修辞性を分析し、内包作者・信頼できない語り手の概念を確立した修辞理論。", 5, "invariant",
     "AI生成テクストの「内包作者」をどう想定するかという新たな問いを生む。", "primary", "西欧"),
    ("バフチン・ジャンル記憶論", "Bakhtin Genre Memory", "Память жанра", "cyrillic", "東欧・ロシア", 210,
     "バフチンがジャンルは過去の発話形式の沈殿物として記憶を持ち、新作品にも古層が活きるとする理論。", 4, "invariant",
     "AI学習データに沈殿するジャンル記憶の解析に応用可能。", "primary", "東欧・ロシア"),

    # Cluster 2: New Historicism (complementing existing Greenblatt/Montrose/Gallagher/Orgel)
    ("グリーンブラット自己成型論詳説", "Greenblatt Self-Fashioning Detailed", "Renaissance Self-Fashioning", "latin", "西欧", 125,
     "ルネサンス期の自己はテクスト的・社会的力場の交渉の産物であるとする新歴史主義の中核論。", 5, "rethinking",
     "デジタル自我の構築とAIアバターの自己成型に拡張的に応用される。", "primary", "西欧"),
    ("グリーンブラット社会的エネルギー循環論", "Greenblatt Circulation of Social Energy", "Shakespearean Negotiations", "latin", "西欧", 125,
     "シェイクスピア劇を通じた社会的エネルギーの集合的交渉と循環を分析する新歴史主義の方法論。", 5, "partial",
     "プラットフォーム経済の文化的循環の分析にも応用される。", "primary", "西欧"),
    ("モントローズ「文化の詩学／詩学の政治学」", "Montrose Poetics of Culture", "Professing the Renaissance", "latin", "西欧", 125,
     "モントローズが文学テクストの歴史性と歴史のテクスト性を双方向に読み解く新歴史主義のスローガン的定式。", 5, "invariant",
     "歴史と表象の相互構成という視点はAI時代の歴史叙述にも有効。", "primary", "西欧"),
    ("ギャラガー＝グリーンブラット『新歴史主義の実践』方法論", "Gallagher Greenblatt Practicing New Historicism Method", "Practicing New Historicism", "latin", "西欧", 125,
     "新歴史主義のアネクドートから出発し文化全体を再構成する解釈技法を体系化した方法論書。", 5, "primary",
     "デジタルアーカイブ時代の微細歴史記述に直結する。", "primary", "西欧"),
    ("オーゲル『幻影の力』権力演劇論", "Orgel Illusion of Power Theatre", "The Illusion of Power", "latin", "西欧", 125,
     "オーゲルがスチュアート朝のマスク劇を通じて宮廷儀礼と権力の演出的構造を分析した新歴史主義古典。", 4, "invariant",
     "メディアスペクタクル分析の系譜に位置づけられる。", "primary", "西欧"),
    ("ドラン『危険な親密』家庭悲劇論", "Dolan Dangerous Familiars", "Dangerous Familiars", "latin", "西欧", 125,
     "ドランが近世イングランドの家庭悲劇と魔女裁判記録から家父長制と家政の暴力を読む新歴史主義論。", 4, "rethinking",
     "ジェンダー暴力と家庭空間の言説分析の基礎参照。", "primary", "西欧"),

    # Cluster 3: Cultural materialism (complementing existing Williams/Eagleton/Hoggart/Hall)
    ("ウィリアムズ『田舎と都会』対照論", "Williams Country and City", "The Country and the City", "latin", "西欧", 125,
     "ウィリアムズが英文学における田舎／都会の表象を歴史唯物論的に読み解いた文化唯物論の代表作。", 5, "primary",
     "都市化・気候変動と農村ノスタルジアの再考に直結。", "primary", "西欧"),
    ("ウィリアムズ『マルクス主義と文学』感情の構造", "Williams Marxism and Literature Structures of Feeling", "Marxism and Literature", "latin", "西欧", 125,
     "ウィリアムズがヘゲモニー・残余・新興・感情の構造を統合した文化唯物論の理論的体系書。", 5, "primary",
     "AI時代の集合的感情構造分析の理論基盤。", "primary", "西欧"),
    ("ウィリアムズ『キーワード』語彙史アプローチ", "Williams Keywords Lexical History", "Keywords", "latin", "西欧", 125,
     "ウィリアムズが文化的に重要な語の意味史を辿り、社会変化と概念変動の連動を示した辞典型批評。", 5, "primary",
     "デジタル人文学の概念史マイニングの源流。", "primary", "西欧"),
    ("イーグルトン『批評の機能』公共圏論", "Eagleton Function of Criticism Public Sphere", "The Function of Criticism", "latin", "西欧", 125,
     "イーグルトンが18世紀以降の批評の公共的機能の歴史的衰退と再生可能性を論じた文化唯物論的批評史。", 4, "primary",
     "SNS時代の批評の公共性回復論として再読される。", "primary", "西欧"),
    ("ホガート『読み書き能力の効用』労働者文化論", "Hoggart The Uses of Literacy Working-Class", "The Uses of Literacy", "latin", "西欧", 125,
     "ホガートが英国労働者階級の生活文化と大衆メディアによる文化変容を観察した文化研究の創始的著作。", 5, "primary",
     "プラットフォーム時代の生活文化変容研究の原点。", "primary", "西欧"),
    ("ホール「エンコーディング／デコーディング」モデル", "Hall Encoding Decoding", "Encoding/Decoding", "latin", "西欧", 125,
     "ホールがメディアメッセージの生産・流通・消費の意味交渉を支配的・交渉的・対抗的の3読解で分析する枠組み。", 5, "rethinking",
     "アルゴリズム媒介下の意味生成の再記述に応用される。", "primary", "西欧"),

    # Cluster 4: Stylistics + cognitive (avoid duplicates)
    ("ハリデー＝ハッサン結束性理論", "Halliday Hasan Cohesion Theory", "Cohesion in English", "latin", "西欧", 125,
     "ハリデーらがテクストの結束性を指示・代用・省略・接続・語彙結束の5装置で分析する体系機能言語学。", 5, "secondary",
     "AI生成テクストの結束性評価の基礎指標。", "primary", "西欧"),
    ("リーチ＝ショート『小説の文体』分析法", "Leech Short Style in Fiction", "Style in Fiction", "latin", "西欧", 125,
     "リーチとショートが小説の文体特徴を語彙・文法・比喩・結束性の4水準で網羅的に分析するスタイリスティクス。", 5, "secondary",
     "計算文体論と機械学習文体検出の参照モデル。", "primary", "西欧"),
    ("レイコフ＝ジョンソン概念メタファー理論", "Lakoff Johnson Conceptual Metaphor", "Metaphors We Live By", "latin", "西欧", 125,
     "レイコフとジョンソンが日常言語のメタファーが思考の身体的基盤を露呈するとする認知言語学の中核理論。", 5, "rethinking",
     "AIの推論におけるメタファー的構造の研究に拡張される。", "primary", "西欧"),
    ("ストックウェル『認知詩学入門』", "Stockwell Cognitive Poetics Introduction", "Cognitive Poetics", "latin", "西欧", 125,
     "ストックウェルが認知言語学とスキーマ理論を文学読解に体系適用した認知詩学の標準教科書。", 4, "secondary",
     "AI読解と人間読解の差を測る基準を提供する。", "primary", "西欧"),
    ("ザンシャイン『なぜ我々はフィクションを読むか』心の理論", "Zunshine Why We Read Fiction Theory of Mind", "Why We Read Fiction", "latin", "西欧", 125,
     "ザンシャインが小説読解を心の理論の認知トレーニングとして説明する認知文芸批評の代表作。", 5, "rethinking",
     "AI登場人物への心的帰属に関する新たな問いを開く。", "primary", "西欧"),
    ("ホーガン『情動的物語論』", "Hogan Affective Narratology", "Affective Narratology", "latin", "西欧", 125,
     "ホーガンが情動システムを物語生成の動因とし、ジャンルを情動的プロトタイプとして再記述する理論。", 4, "rethinking",
     "AI物語生成の情動的整合性評価の理論基盤。", "primary", "西欧"),

    # Cluster 5: World-systems + postcolonial (avoid duplicates)
    ("カザノヴァ『文学の世界共和国』中心-周縁論", "Casanova World Republic of Letters Center Periphery", "La République mondiale des Lettres", "latin", "西欧", 125,
     "カザノヴァが世界文学を文学資本の不均等分配と中心-周縁の構造的不平等として記述する世界システム文学論。", 5, "primary",
     "AI翻訳時代の文学資本流通の再考に直結。", "primary", "西欧"),
    ("モレッティ遠読・量的形式主義", "Moretti Distant Reading Quantitative Formalism", "Distant Reading", "latin", "西欧", 125,
     "モレッティが大量の作品をデータとして俯瞰し、ジャンル進化や形式分布を統計的に追う遠読の方法論。", 5, "rethinking",
     "計算文学批評と機械学習文体分析の理論的母胎。", "primary", "西欧"),
    ("ダムロッシュ『世界文学とは何か』楕円的読解", "Damrosch What is World Literature Elliptical", "What is World Literature?", "latin", "西欧", 125,
     "ダムロッシュが世界文学を母文化と受容文化の楕円焦点による翻訳的存在として再定義する世界文学論。", 5, "primary",
     "翻訳機械時代の世界文学循環の理論枠組み。", "primary", "西欧"),
    ("スピヴァク『学問分野の死』惑星性", "Spivak Death of a Discipline Planetarity", "Death of a Discipline", "latin", "横断", 125,
     "スピヴァクが比較文学の死から惑星性へと向かう倫理的読解を提唱したポストコロニアル世界文学論。", 5, "rethinking",
     "気候・AI危機下の人文学の倫理的再構築の参照点。", "primary", "横断"),
    ("バーバ「ディセミネーション」国民物語論", "Bhabha DissemiNation Nation Narrative", "DissemiNation", "latin", "横断", 125,
     "バーバが国民の語りを教育的時間と遂行的時間の分裂として読み解くポストコロニアル国民論。", 5, "primary",
     "AI時代の国民共同体の再形成と文化アイデンティティ分析に有効。", "primary", "横断"),
    ("ムベンベ『ポストコロニーについて』権力論", "Mbembe On the Postcolony Power", "On the Postcolony", "latin", "横断", 150,
     "ムベンベがアフリカ・ポストコロニアル国家における権力の劇場性・身体性・暴力を分析した政治批評。", 5, "rethinking",
     "デジタル監視時代のネクロポリティクス分析の理論的基盤。", "primary", "横断"),
]

assert len(CONCEPTS) == 30, f"expected 30, got {len(CONCEPTS)}"

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        (name_ja, name_en, name_original, script, region, pid, definition,
         importance, fourth_status, fourth_note, tier, canonical) = c
        # avoid duplicates by (name_ja, region, period_id)
        cur.execute("SELECT id FROM concepts WHERE name_ja=? AND region=? AND period_id=?",
                    (name_ja, region, pid))
        if cur.fetchone():
            skipped += 1
            continue
        try:
            cur.execute("""INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id,
                 region, period_id, definition, importance_score,
                 fourth_transform_status, fourth_transform_note,
                 source_tier, canonical_in_region)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (name_ja, name_en, name_original, script, SUBFIELD_ID,
                 region, pid, definition, importance,
                 fourth_status, fourth_note, tier, canonical))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
            skipped += 1
    conn.commit()
    # report
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"inserted={inserted} skipped={skipped} subfield22_total={total}")

if __name__ == "__main__":
    main()
