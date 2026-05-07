"""
LIT-DB Phase 2 Wave 5: C16 — 日本古典文学（上代〜中古）40概念投入スクリプト

主パターン: P1 (Canonical Primary Pursuit)
subfield_id=10 (lit_jp_classical), region='東アジア'

構成（5カテゴリ × 8件 = 40件）:
- A: 上代の主要作品・形式（8件）
- B: 上代の主要詩学概念（8件）
- C: 中古の主要ジャンル（8件）
- D: 中古の詩学・批評（8件）
- E: 主要作品概念（8件）

第四変容タグは「もののあはれ」「本歌取」「仮名 vs 真名」「物語/虚構の起源」
「女流文学」を中心に12件以上付与。
PT・PHIL・AN・Myth-Narrativesとの cross_domain を10件以上記録。

使用法:
    python3 wave5_c16_japan_classical_early.py
"""

from __future__ import annotations

from lit_db_helper import LitDB


# ----------------------------------------------------------------
# 期間（上代・中古）の用意
# ----------------------------------------------------------------

def setup_periods(db: LitDB) -> dict:
    """上代・中古（奈良・平安）の主要時代区分を get_or_create する。"""
    periods = {}
    periods["上代"] = db.get_or_create_period(
        name_ja="上代", name_en="Jōdai (Archaic / Nara)",
        region="東アジア", start_year=600, end_year=794,
        description=(
            "推古朝〜奈良時代末。記紀・風土記・万葉集・懐風藻が成立し、"
            "口承文学の文字化と漢文学受容の最初期にあたる時代。"
        ),
    )
    periods["中古"] = db.get_or_create_period(
        name_ja="中古", name_en="Chūko (Heian / Classical)",
        region="東アジア", start_year=794, end_year=1185,
        description=(
            "平安時代。仮名文字の発達と国風文化の成熟期。"
            "古今集・源氏物語・枕草子等の和歌・物語・日記文学の黄金時代。"
        ),
    )
    return periods


# ----------------------------------------------------------------
# 40概念データ定義
# ----------------------------------------------------------------

def build_concept_records(periods: dict) -> list[dict]:
    """40概念のレコードリストを構築する。"""
    P_JODAI = periods["上代"]
    P_CHUKO = periods["中古"]

    records: list[dict] = []

    # ============================================================
    # A. 上代の主要作品・形式（8件）
    # ============================================================
    records.append(dict(
        name_ja="記紀", name_en="Kiki (Kojiki and Nihon Shoki)",
        name_original="記紀", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "『古事記』（712年・太安万侶撰）と『日本書紀』（720年・舎人親王ら撰）の併称。"
            "天皇家の系譜と神話・伝承を載せる現存最古の歴史書で、日本における"
            "神話・歴史・文学の不可分の三位一体を体現する。古事記は和語的表記、"
            "日本書紀は漢文正史体という対照的な書記戦略を取る。"
        ),
        background=(
            "天武朝の国史編纂事業に発し、記憶術士稗田阿礼の誦習を太安万侶が筆録した古事記、"
            "中国正史に倣い舎人親王らが編んだ日本書紀という二系統で結実した。"
        ),
        development=(
            "中世以降、本居宣長『古事記伝』により国学の聖典として再発見され、"
            "近代日本文学・神話学の根本資料となった。"
        ),
        historical_context="律令国家確立期における国家アイデンティティの文字化事業。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991094",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("物語", "rethinking",
                      "記紀は神話・伝承を「歴史」として権威化する装置であり、"
                      "事実と虚構の境界を成立させる以前の「神話的歴史」の様態を保存する。"
                      "AIが生成する「もっともらしい歴史」と、神話的真実性の構造的類似と差異が問題化する。",
                      "AI生成の擬似歴史記述、ディープフェイク歴史、神話的真実性")],
        cross=[("Myth-Narratives", None, "Japanese creation myth (Kojiki)",
                "shared_concept",
                "古事記の天地開闢・国生み神話は世界神話DBの主要参照点")],
    ))

    records.append(dict(
        name_ja="風土記", name_en="Fudoki (provincial gazetteers)",
        name_original="風土記", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "713年の元明天皇詔に基づき各国に編纂を命じた地誌。地名由来・産物・"
            "古老の伝承を記録する。出雲・常陸・播磨・豊後・肥前の五風土記が"
            "現存（出雲のみほぼ完本）。地方伝承・地名起源説話の最古層を保存し、"
            "土地と物語の結合を示す根本資料。"
        ),
        background="律令国家の地方統治のための地理情報整備事業として始まった。",
        development=(
            "後世の地誌・国学的地名研究・民俗学（柳田國男）の根本資料となり、"
            "「地名の物語化」という日本文学の特質の起源として再評価された。"
        ),
        historical_context="奈良時代の地方統治と地誌編纂事業。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991095",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="万葉集", name_en="Man'yōshū",
        name_original="萬葉集", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "8世紀後半に編纂された現存最古の和歌集。約4,500首を20巻に収め、"
            "雑歌・相聞・挽歌の三大部立による分類、長歌・短歌・旋頭歌等の多様な形式、"
            "天皇から防人・東国農民まで多層な作者層を持つ。万葉仮名（漢字音訓借用）で"
            "表記され、和歌史の出発点。"
        ),
        background="大伴家持の最終編纂と推定される複数編者・複数巻の累層的成立。",
        development=(
            "平安期は古今集に押されたが、賀茂真淵『万葉考』により近世国学で再発見され、"
            "近代『アララギ』派の写実主義の聖典となった。"
        ),
        historical_context="律令国家成立期の多元的歌唱文化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("作者性", "partial",
                      "万葉集は天皇から名もなき防人まで多層な作者層を保存する点で、"
                      "後の宮廷和歌の閉鎖的作者圏とは対照的な「広範な歌い手」のモデルを提供する。"
                      "AIが生成する大量テキスト時代における「誰の声か」の再考に資する。",
                      "AI生成テキストの作者帰属、声の多層性")],
        cross=[("PT", None, "Man'yōshū", "shared_concept",
                "詩学DBの古代抒情詩集の比較対象")],
    ))

    records.append(dict(
        name_ja="懐風藻", name_en="Kaifūsō",
        name_original="懷風藻", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "751年成立、現存最古の日本人漢詩集。64名120首を収録。大友皇子・"
            "大津皇子・長屋王ら皇族貴族の漢詩を中心とする。万葉集と同時代に"
            "並立し、和歌（やまとうた）と漢詩（からうた）という日本文学の"
            "二言語的双軸の確立を象徴する。"
        ),
        background="奈良朝の唐文化受容と貴族の漢詩教養の高度化。",
        development=(
            "平安朝の『凌雲集』『文華秀麗集』『経国集』の勅撰三集に直接連なり、"
            "和漢比較の基盤を形成した。"
        ),
        historical_context="8世紀の遣唐使と唐風文化受容。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991096",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("言語", "partial",
                      "懐風藻と万葉集の並立は日本文学の和漢二言語的構造の起源を示す。"
                      "AI多言語処理が言語間の境界を曖昧化する時代に、"
                      "二言語並行創作の歴史的範例として再評価しうる。",
                      "LLM多言語生成、コードスイッチング、二言語文学")],
    ))

    records.append(dict(
        name_ja="枕詞", name_en="makura-kotoba (pillow word)",
        name_original="枕詞", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "和歌で特定の語を導く慣用的な修飾語。通常5音節で、被修飾語との結合が"
            "歌語的伝統で固定化される（例:「あしひきの」→山、「ひさかたの」→光・天）。"
            "万葉集に既に成立し、古今集以降も継承された。意味的合理性を超え、"
            "音響的・呪術的・伝統的な連想機能で和歌に定型的厚みを与える。"
        ),
        background="古代呪詞・神事歌謡における音韻的反復に源流を持つと推定される。",
        development=(
            "万葉から古今へと厳格な伝統として継承され、後世の連歌・俳諧でも"
            "「歌語」として残存した。"
        ),
        historical_context="古代日本の呪術的言語観と歌唱文化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="序詞", name_en="jo-kotoba (preface phrase)",
        name_original="序詞", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "和歌で本旨に入る前に置かれる、ある語句や句を導き出す前置きの修辞。"
            "枕詞より長く（数句〜数十音）、自由度が高い。比喩的・音韻的に"
            "本旨と接続する。万葉集の長歌・短歌に頻出し、抒情的厚みの源泉となった。"
        ),
        background="古代歌謡の反復・対句構造に起源を持つ。",
        development="平安以降は短歌の凝縮化により規模が縮小したが、修辞理論として継承。",
        historical_context="万葉長歌の修辞学。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="掛詞", name_en="kake-kotoba (pivot word / wordplay)",
        name_original="掛詞", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "和歌で同音異義の語を用い一語で二つの意味を同時に喚起する修辞技法。"
            "「松（まつ）」と「待つ」、「ふる」（降る・古る・経る・振る）等が典型。"
            "万葉に萌芽が見え、古今集以降の和歌で中核技法となった。"
            "日本語の音韻構造（同音異義語の豊富さ）を最大限に活用した独自の修辞。"
        ),
        background="日本語のCV型音節構造による同音異義語の豊富さを基盤とする。",
        development=(
            "新古今集の余情美学、後世の連歌・浄瑠璃・歌舞伎の言語遊戯まで継承された。"
        ),
        historical_context="平安朝和歌の凝縮的修辞文化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("言語", "rethinking",
                      "掛詞は日本語音韻特質に依存する修辞であり、翻訳に最も抵抗する詩的要素。"
                      "AI翻訳が掛詞をどう扱うかは、文学翻訳における「言語特殊性」の根本問題となる。",
                      "AI翻訳の不可能性、言語特殊修辞のLLM処理")],
        cross=[("PT", None, "pun / paronomasia", "parallel",
                "西欧詩学の punning との対比対象、ただし日本語音韻に固有の構造")],
    ))

    records.append(dict(
        name_ja="旋頭歌", name_en="sedōka",
        name_original="旋頭歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "和歌の古典的形式の一つ。5・7・7・5・7・7の6句38音で構成され、"
            "上の句と下の句が対句的・問答的構造を持つ。万葉集に約60首収録。"
            "短歌・長歌に対する第三の形式として上代に成立したが、平安以降は衰退し、"
            "古今集には僅かな例を残すのみとなった。"
        ),
        background="古代歌謡の問答・対唱形式に源流を持つ。",
        development=(
            "平安以降衰退し、古典的「失われた形式」として後世の歌人が時に復興を試みた。"
        ),
        historical_context="万葉時代の多様な歌唱形式の一つ。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=2, source_tier="primary", canonical_in_region="minor",
    ))

    # ============================================================
    # B. 上代の主要詩学概念（8件）
    # ============================================================
    records.append(dict(
        name_ja="真名と仮名", name_en="mana and kana (true script and provisional script)",
        name_original="真名／假名", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "日本書記体系の二極を表す概念。「真名」は漢字（公的・男性的・漢文）、"
            "「仮名」は漢字を音節文字化した万葉仮名・平仮名・片仮名（私的・女性的・"
            "和文）を指す。9-10世紀に公式（漢文）／私的（仮名）、男性／女性、"
            "国家／個人という二項対立が文学的書記の基盤として機能した。"
        ),
        background="漢字一辺倒の8世紀から、9世紀の万葉仮名草書化を経て平仮名・片仮名が分化。",
        development=(
            "土佐日記（紀貫之、男性が女性に仮託して仮名で書いた日記）に象徴的に現れ、"
            "源氏物語等の女流文学を生む書記基盤となった。"
        ),
        historical_context="9-10世紀の国風文化形成期における書記体系の二極化。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/2611715",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("言語", "rethinking",
                      "真名／仮名は日本における書記言語の選択が、ジェンダー・公私・国家／個人を"
                      "同時に決定する「言語政治」の原型である。"
                      "AI時代の言語選択（プロンプト言語、モデル言語）と人格・公私の関係を考える参照点。",
                      "AIプロンプトにおける言語選択、コードスイッチング"),
                     ("作者性", "partial",
                      "土佐日記の「男もすなる日記といふもの」は男性著者が女性仮託で仮名を選ぶという"
                      "二重の書記操作で、作者性と書記体系の関係を最初に問題化した。"
                      "AI時代の作者偽装・人格生成の歴史的先例。",
                      "AIによる人格偽装、女性語LLMチャットボット")],
        cross=[("PHIL", None, "writing system as politics", "shared_concept",
                "デリダのエクリチュール論と書記体系の政治性議論との接続点"),
               ("AN", None, "gendered writing", "shared_concept",
                "人類学のジェンダー化された言語実践研究との接続")],
    ))

    records.append(dict(
        name_ja="漢詩文受容", name_en="reception of Sinitic literature",
        name_original="漢詩文受容", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "上代から中古にかけての中国詩文（特に六朝〜唐の詩文）の受容過程。"
            "懐風藻に始まり、勅撰三集（凌雲集・文華秀麗集・経国集、9世紀前半）で頂点に達し、"
            "白居易『白氏文集』が和歌と物語に深く浸透した。和漢併存・和漢比較が"
            "日本文学の構造的特質となる。"
        ),
        background="遣隋使・遣唐使による文物移入と貴族教養の体系化。",
        development=(
            "和漢朗詠集（藤原公任、1018頃）で和漢の対称的読書が制度化され、"
            "源氏物語の漢籍引用に結実した。"
        ),
        historical_context="7-11世紀の東アジア漢字文化圏内での日本の位置取り。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991100",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "partial",
                      "漢詩文受容は「外来高文化を翻訳・適応・内在化する」千年以上の事業の起源で、"
                      "現代のAI技術受容（米中由来の汎用モデルの日本語適応）と構造的に並行する。",
                      "AI技術の文化的受容、翻訳的適応、ローカライゼーション")],
        cross=[("PT", None, "imitatio", "parallel",
                "西欧の古典模倣論と東アジア漢詩文受容の比較対象")],
    ))

    records.append(dict(
        name_ja="古事記の神話的物語", name_en="mythic narrative in Kojiki",
        name_original="古事記神話", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "古事記上巻の神々の物語を中心とする神話群。天地開闢・国生み・"
            "天照大神の岩戸隠れ・須佐之男命の八岐大蛇退治・大国主の国譲り・"
            "天孫降臨等を含む。世界の起源と王権の正統性を結ぶ神話的物語の典型で、"
            "日本における物語生成の原始的モデル。"
        ),
        background="各氏族の伝承を天皇家中心に再編した8世紀の体系化。",
        development=(
            "中世神話学・本居宣長『古事記伝』・近代日本神話学・現代の比較神話学"
            "（吉田敦彦・大林太良）まで継続的に研究の対象となる。"
        ),
        historical_context="律令国家の正統性を神話で基礎づける8世紀の事業。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991094",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("Myth-Narratives", None, "Amaterasu cave myth, Yamata no Orochi",
                "shared_concept",
                "世界神話DBの主要日本神話エントリーへの参照"),
               ("AN", None, "myth-history continuum", "shared_concept",
                "人類学的神話研究における歴史と神話の連続性の事例")],
    ))

    records.append(dict(
        name_ja="国讃め歌", name_en="kuni-bome (land-praising poetry)",
        name_original="國讚め歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "土地・国土を讃える呪術的・儀礼的な歌謡。万葉集巻頭の舒明天皇御製"
            "「香具山の歌」が典型。山の上から国見をして土地の豊穣を言祝ぐ"
            "「国見歌」と密接に結びつき、王権による国土支配の言語的儀礼として"
            "古代和歌の根源的機能を体現する。"
        ),
        background="古代王権の国見儀礼と土地呪術の文学化。",
        development=(
            "後世にも国見的視点の歌は残るが、儀礼性は次第に薄れて純粋な"
            "風景叙述・抒情へと変化した。"
        ),
        historical_context="古代天皇制の儀礼的国土観。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="相聞歌", name_en="sōmonka (mutual exchange / love poems)",
        name_original="相聞歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "万葉集の三大部立の一つ。男女・親子・友人間の交わされる歌で、"
            "中心は恋歌。「相聞」とは互いに音信を交わすこと。万葉集中で最大量を占める。"
            "個人的感情の歌唱という和歌の中核機能を体現し、後の平安朝恋歌・"
            "贈答歌の伝統の起源となった。"
        ),
        background="古代歌垣・問答歌の伝統の文学的体系化。",
        development=(
            "古今集以降「恋」部として再分類されつつ、贈答という対話的形式を"
            "中世まで保ち続けた。"
        ),
        historical_context="万葉時代の歌唱共同体と恋愛文化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="挽歌", name_en="banka (elegy / death poems)",
        name_original="挽歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "万葉集の三大部立の一つ。死者を悼む哀傷の歌。中国の挽歌（葬送歌）に"
            "ならった部立名。柿本人麻呂の長歌が代表的で、皇族の崩御や近親者の死を"
            "公的・私的に哀悼する。挽歌は古代日本における死生観・呪鎮の言語化として"
            "和歌の儀礼的根源を示す。"
        ),
        background="中国の挽歌と日本の殯（もがり）儀礼の文学的結合。",
        development=(
            "古今集以降は「哀傷」部として継承され、辞世の和歌の伝統を貫流する。"
        ),
        historical_context="古代葬送儀礼と歌唱の結合。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        cross=[("PT", None, "elegy", "parallel",
                "西欧詩学のエレジー概念と東アジア挽歌の比較対象")],
    ))

    records.append(dict(
        name_ja="雑歌", name_en="zōka (miscellaneous poems)",
        name_original="雜歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "万葉集の三大部立の一つ。相聞・挽歌に分類されない歌全般を指す。"
            "公的儀礼歌・行幸歌・羈旅歌・四季歌・雑詠を含み、最も雑多な部立。"
            "後の古今集における「春・夏・秋・冬・賀・離別・羈旅」等の細分化された"
            "部立体系の母型となった。"
        ),
        background="万葉編纂時の素朴な三分類体系の必然的残余カテゴリ。",
        development=(
            "古今集ではこの「雑歌」の内実が四季・賀・離別・羈旅・物名・恋・哀傷等に"
            "細分化された。"
        ),
        historical_context="万葉編纂の分類学。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="東歌", name_en="azuma-uta (Eastern Provinces poems)",
        name_original="東歌", original_script="japanese",
        period_id=P_JODAI,
        definition=(
            "万葉集巻14の関東以東諸国の民謡的歌。約230首。方言・地方語彙・"
            "庶民的素材を含み、宮廷歌人による精緻な歌とは対照的に素朴で力強い。"
            "防人歌（巻20）と並び、万葉集の階層的多様性を象徴する重要部分。"
        ),
        background="奈良朝の地方制度と国府を通じた地方歌謡採集。",
        development=(
            "中世以降は国学者により民俗・方言研究の根本資料となった。"
            "近代には柳田國男・折口信夫が民俗学的に再評価。"
        ),
        historical_context="律令国家の地方統治と歌唱文化採集。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4946_22618.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("主体", "partial",
                      "東歌は宮廷外・名もなき地方民の声を文学正典に組み込んだ稀有な事例で、"
                      "「誰が歌う権利を持つか」という主体問題の早期事例である。"
                      "AI時代のマイノリティ表象・声の可視化と比較される対象。",
                      "AIによる多声的生成、マイノリティ表象")],
        cross=[("AN", None, "folk poetry collection", "parallel",
                "民俗学・人類学における民謡採集事業の先駆け")],
    ))

    # ============================================================
    # C. 中古の主要ジャンル（8件）
    # ============================================================
    records.append(dict(
        name_ja="物語", name_en="monogatari (tale / narrative fiction)",
        name_original="物語", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "平安時代に成立した散文虚構文学の総称。「物語る」という語の名詞化。"
            "竹取物語（9世紀末-10世紀初）、伊勢物語、宇津保物語、落窪物語、"
            "そして源氏物語（11世紀初）まで多様な系列を含む。仮名書きで、"
            "和歌を散文中に挿入する独自の混合文体を持つ世界文学史上稀有な散文虚構の伝統を確立した。"
        ),
        background="仮名文字の確立と女流作者層の成立を基盤に発展。",
        development=(
            "源氏物語が頂点を極め、後の擬古物語・歴史物語・軍記物語・読本まで"
            "「monogatari」の系譜は近世まで継続した。"
        ),
        historical_context="9-11世紀の国風文化と女房文化の発達。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/2611715",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("物語", "rethinking",
                      "物語は世界文学史的に見て早期の本格的散文虚構の確立例で、"
                      "「事実とは別の真実」としての虚構を肯定する文学観の起源（紫式部の「物語論」）を含む。"
                      "AI生成テキストにおける「虚構の真実性」の根源的問いに直接接続する。",
                      "AI生成虚構の真実性、物語の存在論"),
                     ("真正性", "rethinking",
                      "源氏物語『蛍』巻の「物語論」は、嘘を含むからこそ深い真実を伝えるという"
                      "虚構の真正性論を世界に先駆けて提示した。AI生成物の真正性議論の歴史的先例。",
                      "AI生成物の真正性、虚構の認識論")],
        cross=[("PT", None, "prose fiction origins", "shared_concept",
                "西欧近代小説起源論との比較対象（源氏物語の世界小説起源説）")],
    ))

    records.append(dict(
        name_ja="日記文学", name_en="nikki bungaku (diary literature)",
        name_original="日記文學", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "平安時代に発達した、自伝的・内省的散文の一群。土佐日記（935頃）に始まり、"
            "蜻蛉日記（10世紀後半）、和泉式部日記、紫式部日記、更級日記（11世紀）等。"
            "私的経験の文学化、時間の流れの内的記録、女性著者による自己表現という"
            "西欧の自伝文学に匹敵する独自の伝統を平安期に確立した。"
        ),
        background=(
            "漢文公式日記の伝統に対する、仮名による私的内的記録の発生。"
            "土佐日記が男性著者の女性仮託という形で口火を切った。"
        ),
        development=(
            "中世の女流日記（とはずがたり等）、近世の俳諧紀行（奥の細道）、"
            "近代の私小説まで日本文学の自伝的伝統を貫流する。"
        ),
        historical_context="10-11世紀の女流文学開花期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000091/files/41254_18920.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("主体", "rethinking",
                      "日記文学は中世以降の自伝的文学を準備した、世界文学史的にも早期の"
                      "「内面を持つ書く主体」の確立例で、AIが生成する「日記風テキスト」の"
                      "主体性問題を考える歴史的座標となる。",
                      "AI生成の自伝的テキスト、書く主体の問題")],
        cross=[("AN", None, "women's writing", "shared_concept",
                "ジェンダーと書く実践の人類学的研究との接続")],
    ))

    records.append(dict(
        name_ja="随筆", name_en="zuihitsu (essay / miscellany)",
        name_original="隨筆", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "「筆に随う」と書き、思いつくままに記す散文ジャンル。枕草子（清少納言、"
            "11世紀初）に始まり、徒然草（吉田兼好、14世紀）、方丈記（鴨長明、13世紀）"
            "を三大随筆とする。固定された主題や形式を持たず、観察・断章・章段の"
            "緩やかな連鎖で構成される、東アジアでも独自の散文形式。"
        ),
        background="物語・日記・歌集とは別系統の、断章的散文の必要性に応えて成立。",
        development=(
            "中世・近世を通じて知識人の主要な散文形式となり、"
            "近代の随想・エッセイの直接的祖型となった。"
        ),
        historical_context="平安朝後期の宮廷女房文化の知的・批評的成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/001102/files/49236_42624.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="勅撰和歌集", name_en="chokusen wakashū (imperial waka anthologies)",
        name_original="敕撰和歌集", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "天皇の勅命により編纂された和歌集。905年の古今和歌集（醍醐天皇勅）に始まり、"
            "後撰・拾遺・後拾遺・金葉・詞花・千載・新古今（1205）までの八代集、"
            "さらに新勅撰以下を含めて二十一代集に及ぶ。和歌の正典化・国家事業化・"
            "歌人の社会的地位確立という点で、東アジアでも独自の文学制度を構築した。"
        ),
        background="国風文化の成熟と漢詩勅撰三集の伝統を和歌に転用したもの。",
        development=(
            "古今集仮名序による和歌史観と歌論を基盤に、新古今集まで六部立体系を保ち、"
            "中世の堂上歌道・近世の歌学を制度的に支えた。"
        ),
        historical_context="平安朝の天皇権威と和歌文化の結合。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4944_22606.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="歌物語", name_en="uta-monogatari (poem-tale)",
        name_original="歌物語", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "和歌を中核に、その制作の事情を散文で添える短編集成型の物語ジャンル。"
            "伊勢物語（10世紀前半）、大和物語、平中物語が代表。和歌の社会的・"
            "対話的機能を物語化し、和歌を中心とする貴族生活の詩的記録となる。"
            "後の物語文学・連歌・俳諧紀行にも影響した独自の混合形式。"
        ),
        background="和歌の詞書（ことばがき）の独立的展開。",
        development=(
            "源氏物語等の長編物語に吸収・統合され、「歌物語」というジャンル自体は"
            "中古以後衰退したが、和歌＋散文の混合形式は連歌・紀行に継承。"
        ),
        historical_context="9-10世紀の宮廷和歌共同体の物語化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4945_22612.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="説話", name_en="setsuwa (anecdotal tale)",
        name_original="說話", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "短い口承的・教訓的・奇譚的な物語の集成。日本霊異記（9世紀初、"
            "現存最古の仏教説話集）に始まり、今昔物語集（12世紀、千余話）、"
            "宇治拾遺物語等に展開する。仏教説話・世俗説話を含み、雑多な"
            "庶民的素材と短小性を特徴とする、物語とは別系統の散文伝統。"
        ),
        background="中国の志怪小説・仏教経典の譬喩と日本固有の口承伝承の融合。",
        development=(
            "中世の沙石集・古今著聞集、近世の御伽草子・仮名草子・落語の"
            "源流の一つとなり、近代の芥川龍之介の素材源としても重要。"
        ),
        historical_context="平安末期の仏教普及と庶民物語需要の高まり。",
        primary_source_url="https://www.aozora.gr.jp/cards/001147/files/49984_43221.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="伝奇物語", name_en="denki-monogatari (fantastic / romantic tale)",
        name_original="傳奇物語", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "竹取物語・宇津保物語・落窪物語等、超自然的要素・異郷訪問・"
            "ロマンス・継子いじめなど類型的物語要素を中心とする初期物語の系列。"
            "中国唐代の伝奇小説の影響を受けつつ、日本独自に展開した物語類型。"
            "後の源氏物語の前史となる物語形式の実験段階。"
        ),
        background="中国伝奇小説の受容と日本固有の口承物語素材の結合。",
        development=(
            "源氏物語に統合・乗り越えられたが、物語類型としては中世の御伽草子、"
            "近世の浮世草子・読本まで継承された。"
        ),
        historical_context="9-10世紀の物語形成期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000329/files/18253_12244.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="軍記物語前史",
        name_en="precursors of war tales",
        name_original="軍記物語前史", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "保元物語・平治物語に先立つ、戦乱・軍事を扱った散文の萌芽。"
            "将門記（10世紀、平将門の乱を漢文体で記す）、陸奥話記（11世紀、"
            "前九年の役を記す）が代表。漢文体記録から仮名軍記への移行期に位置し、"
            "平家物語に至る軍記物語の前史を構成する。"
        ),
        background="武士台頭以前の地方軍事衝突の記録化。",
        development=(
            "12世紀末の保元物語・平治物語、13世紀の平家物語へと結実し、"
            "中世軍記物語の主流を形成した。"
        ),
        historical_context="平安中後期の地方武士団台頭と軍事衝突の文学化。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991110",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    # ============================================================
    # D. 中古の詩学・批評（8件）
    # ============================================================
    records.append(dict(
        name_ja="古今集仮名序", name_en="Kokinshū Kana Preface (by Ki no Tsurayuki)",
        name_original="古今集假名序", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "905年成立の古今和歌集に紀貫之が付した仮名による序文。日本最初の"
            "本格的歌論で、「やまとうたは人の心を種として万の言の葉とぞなれりける」"
            "に始まる和歌生成論、六歌仙批評、和歌史観を含む。日本詩学史の出発点であり、"
            "日本における体系的文学論の嚆矢となる。"
        ),
        background=(
            "毛詩大序を意識しつつ仮名で和歌論を構築するという紀貫之の独創的試み。"
        ),
        development=(
            "後の歌論（俊頼髄脳・無名抄・古来風躰抄・近代秀歌等）の理論的基礎となり、"
            "日本詩学史を貫流する根源テクストとなった。"
        ),
        historical_context="10世紀初頭の国風文化と和歌正典化の事業。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4944_22606.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("作者性", "partial",
                      "仮名序の「人の心を種」という和歌発生論は、作者の心を詩の根源と置く"
                      "強い作家主体論を提示する。AIによる「心なき生成」が和歌たりうるかという"
                      "根本問いの歴史的座標。",
                      "AI生成詩の心の不在、生成主体の問題")],
        cross=[("PT", None, "Kokinshū preface", "shared_concept",
                "詩学DBの世界詩論史における日本詩学の起点として参照")],
    ))

    records.append(dict(
        name_ja="もののあはれ", name_en="mono no aware",
        name_original="もののあはれ", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "事物に触れて心が動く、ある種の哀感・情趣・しみじみとした感慨を意味する"
            "美的概念。本居宣長が源氏物語論（『紫文要領』『源氏物語玉の小櫛』、18世紀）で"
            "源氏物語の本質として概念化し、平安朝美意識を代表する語として確立した。"
            "事物の儚さ・人生の無常への深い共感を含む独特の情緒。"
        ),
        background=(
            "「あはれ」は元々感嘆詞で、物語・和歌で多義的に用いられていた。"
            "本居宣長が18世紀にこれを源氏物語の核心概念として体系化した。"
        ),
        development=(
            "近代の日本美学（九鬼周造『「いき」の構造』、和辻哲郎の風土論等）、"
            "現代の日本文化論まで、日本的情趣の代表概念として継続的に再解釈されている。"
        ),
        historical_context="平安朝貴族の情趣文化と18世紀国学の出会い。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4949_22631.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "rethinking",
                      "もののあはれは、外部世界（物）と内的情緒（心）の感応関係を核とする"
                      "受容論的美学であり、一方的に作品を制作・消費するのではなく"
                      "「触れて感じる」関係性を重視する。"
                      "AI時代の作品体験・生成物との情緒的関係を考える参照点。",
                      "AI生成物への情緒的応答、作品との関係性"),
                     ("真正性", "rethinking",
                      "もののあはれは「本物の感動」の判定基準として機能した美学概念で、"
                      "AI生成物が「あはれ」を引き起こしうるかという問いは、"
                      "作品の真正性と情緒の本物性を直接問う。",
                      "AI作品の情緒喚起、生成物の真正性")],
        cross=[("PT", None, "mono no aware", "shared_concept",
                "詩学DBに既存のmono no aware概念への直接的参照"),
               ("PHIL", None, "Buddhist impermanence (mujō)", "shared_concept",
                "仏教的無常観と日本美学の交差点"),
               ("AN", None, "emotional aesthetics", "parallel",
                "情動の人類学・美的経験の文化研究との接続")],
    ))

    records.append(dict(
        name_ja="余情", name_en="yojō (lingering resonance)",
        name_original="餘情", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "和歌・連歌で、表現された言葉の外に残る情趣・余韻。藤原公任『新撰髄脳』"
            "（11世紀初）が「心深く姿清げに、心におかしき所あるを優れたるとすべし」と"
            "述べる以来、平安末から中世にかけて中心的詩論概念となった。中国詩学の"
            "「言外之意」と相通じつつ、日本独自に展開された。"
        ),
        background="中国詩論の含蓄・象外之象・滋味論の受容と日本和歌への適用。",
        development=(
            "藤原俊成・藤原定家により幽玄論と結合され、新古今和歌集の美意識として結実、"
            "後の連歌論・能楽論・俳論に深く影響した。"
        ),
        historical_context="11-12世紀の和歌・連歌理論の精緻化。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991115",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "partial",
                      "余情は読者の側で展開・補完される意味の残響に詩の本質を見るため、"
                      "完結したテキストの「正確な解釈」を求めるAI読解とは構造的に異なる。"
                      "受容者の余地を残す詩学のAI時代における意義の再考に資する。",
                      "AI読解の確定性志向、解釈の余地と受容美学")],
        cross=[("PT", None, "yojō", "shared_concept",
                "詩学DBに既存のyojō概念への直接的参照"),
               ("PT", None, "han-xu (含蓄)", "parallel",
                "中国詩学の含蓄論との対比対象")],
    ))

    records.append(dict(
        name_ja="幽玄前史", name_en="precursors of yūgen",
        name_original="幽玄前史", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "後に世阿弥能楽論で大成される「幽玄」概念の平安〜鎌倉初期の前史。"
            "藤原俊成『古来風躰抄』に幽玄が和歌美の中心理念として登場し、"
            "藤原定家の有心体論に繋がる。元来は道家・仏教用語（深遠で計り知れない）"
            "だったものが、平安末に和歌美学に転用され、新古今美学の核心となった。"
        ),
        background="老荘思想・仏教の幽玄概念の受容と和歌美学への適用。",
        development=(
            "新古今和歌集の主要美意識となり、中世連歌（心敬）・能楽論（世阿弥）"
            "へと深化していく。"
        ),
        historical_context="12世紀末の和歌美学転換期。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991116",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="縁語", name_en="engo (associated words)",
        name_original="緣語", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "和歌の修辞技法で、ある語と意味的・連想的に関連する語群を歌中に意図的に"
            "配置することで表現に厚みを加える方法。例えば「うらみ」（恨・浦見）から"
            "「波」「磯」「沖」を連想させて配置する等。掛詞と並ぶ平安中期以降の"
            "和歌の精緻化を支える主要修辞となった。"
        ),
        background="和歌における音韻と意味の重層的活用への要求から発達。",
        development=(
            "新古今集で頂点に達し、中世連歌の付合論にも継承された。"
        ),
        historical_context="平安中後期の和歌修辞の凝縮化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4944_22606.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="本歌取", name_en="honkadori (allusive variation)",
        name_original="本歌取", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "古歌（本歌）の語句や着想を意図的に取り入れて新しい和歌を詠む技法。"
            "藤原定家『近代秀歌』（13世紀初）が方法論として体系化した。"
            "古歌の世界を背景として召喚しつつ新たな景を重ねるという、"
            "高度に間テクスト的な創作方法で、新古今和歌集で頂点を極めた。"
        ),
        background="平安和歌の本説取・古歌摂取の伝統が方法論として理論化されたもの。",
        development=(
            "新古今集の主要創作技法となり、後の連歌・俳諧の付合・典故・"
            "伝統美学の中核として機能した。中国の点鉄成金・夺胎换骨と並行する"
            "東アジア的「典故活用創造性」の代表的範例。"
        ),
        historical_context="新古今時代の歌道の制度化・技法化。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991117",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "本歌取は古典への参照を本質とする間テクスト的創造性のモデルで、"
                      "ロマン主義的独創性とは根本的に異なる。"
                      "中国の点鉄成金と並び、AIが既存テキストを再構成する創造の歴史的範例として、"
                      "AI生成物の「創造性」を再定義する直接的参照点となる。",
                      "LLMのテキスト再構成、AI創造性の伝統的先行モデル"),
                     ("作者性", "partial",
                      "本歌取は他者の語句を自作に統合する点で、ロマン主義的単一作者観と"
                      "AI協働執筆の中間的位置を示す歴史的範例。",
                      "AI協働執筆の作者帰属")],
        cross=[("PT", None, "honkadori", "shared_concept",
                "詩学DBに既存のhonkadori概念への直接的参照"),
               ("PT", None, "diantie chengjin (点鉄成金)", "parallel",
                "中国宋代の点鉄成金論と並行する東アジア的間テクスト技法")],
    ))

    records.append(dict(
        name_ja="歌合", name_en="utaawase (poetry contest)",
        name_original="歌合", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "二組の歌人が題に従って和歌を詠み、判者が優劣を判定する公的な催し。"
            "天徳四年内裏歌合（960年）が古典的範例とされ、判詞・歌論・歌人の社会的"
            "地位形成に決定的役割を果たした。和歌を社会的・批評的実践として制度化し、"
            "中世和歌の主要場面となった。"
        ),
        background="平安朝の宮廷文化における詩文の公的儀礼化。",
        development=(
            "判詞の蓄積が歌論・歌学の発展を促し、後鳥羽院の建仁元年・建仁二年・"
            "千五百番歌合等で頂点を極めた。"
        ),
        historical_context="10-13世紀の宮廷文化と和歌の制度化。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991118",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="六歌仙", name_en="rokkasen (six poetic immortals)",
        name_original="六歌仙", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "古今集仮名序が万葉と古今の間を代表する歌人として挙げる六人:"
            "在原業平・小野小町・僧正遍昭・喜撰法師・文屋康秀・大伴黒主。"
            "紀貫之による批評的選定で、それぞれに具体的歌風評（「在原業平はその心余りて"
            "言葉足らず」等）が付けられ、日本最初の体系的歌人批評を構成する。"
        ),
        background="古今集編纂時の歌人系譜化と批評的整理の必要性。",
        development=(
            "中世以降は和歌史の正典的歌人として地位が固定し、後の三十六歌仙・"
            "百人一首等の歌人選定基準の原型となった。"
        ),
        historical_context="10世紀初頭の和歌史認識の体系化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4944_22606.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    # ============================================================
    # E. 主要作品概念（8件）
    # ============================================================
    records.append(dict(
        name_ja="源氏物語ともののあはれ",
        name_en="Genji Monogatari and mono no aware",
        name_original="源氏物語ともののあはれ", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "紫式部『源氏物語』（11世紀初）54帖の主題的核心としての「もののあはれ」。"
            "本居宣長が『紫文要領』『源氏物語玉の小櫛』で源氏物語論として構築した解釈で、"
            "勧善懲悪の儒教的読解に対し、人生・恋愛・運命に対するしみじみとした"
            "感受性こそが源氏物語の本質と位置づけた、日本文学批評史上画期的な解釈。"
        ),
        background="中世以来の儒仏的源氏物語解釈に対する18世紀国学者本居宣長の革新的読解。",
        development=(
            "近代日本文学観の根本的枠組みとなり、和辻哲郎・小林秀雄等の批評家、"
            "ドナルド・キーン等の海外日本学にも継承された。"
        ),
        historical_context="平安朝文学の核心 × 18世紀国学的解釈の結合。",
        primary_source_url="https://www.aozora.gr.jp/cards/000052/files/5016_15265.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("正典", "rethinking",
                      "源氏物語は世界文学史上最初期の本格長編散文虚構であり、"
                      "正典化の過程で「日本文学の代表」となった。"
                      "AI時代の正典再考（誰の声が文学正典に入るか、生成テキストは正典化されうるか）"
                      "の歴史的座標として機能する。",
                      "AI時代の文学正典、生成テキストの正典化問題")],
        cross=[("Myth-Narratives", None, "Genji long narrative", "shared_concept",
                "世界長編物語DBの参照点")],
    ))

    records.append(dict(
        name_ja="伊勢物語とみやび", name_en="Ise Monogatari and miyabi (courtly elegance)",
        name_original="伊勢物語と雅び", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "歌物語の代表作『伊勢物語』（10世紀前半）の中核美学である「みやび」"
            "（雅び・宮び）。在原業平の伝とされる125段の章段で、洗練された宮廷的"
            "感受性・恋愛美学・粋（雅）の典型を提示する。日本における「みやび」"
            "（都らしさ・洗練）の文学的範例を確立した。"
        ),
        background="9世紀後半の業平的宮廷恋愛文化と歌物語形式の成立。",
        development=(
            "中世連歌・近世俳諧の美意識（俳諧における「みやび／ひなび」対立）、"
            "近代の和辻哲郎『日本精神史研究』等に継承された。"
        ),
        historical_context="9-10世紀の宮廷恋愛文化と物語化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000922/files/4945_22612.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="枕草子とをかし", name_en="Makura no Sōshi and okashi",
        name_original="枕草子と「をかし」", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "清少納言『枕草子』（11世紀初）の中核美学「をかし」。「あはれ」が深い"
            "感慨であるのに対し、「をかし」は明朗・知的・機知的な美感を指す。"
            "本居宣長以来「あはれ／をかし」を平安美学の二大対比軸として論じる伝統が"
            "あり、枕草子はをかし美学の代表的作品とされる。"
        ),
        background="清少納言の鋭利な観察眼と宮廷批評精神を背景に成立。",
        development=(
            "近代以降の日本美学論で「あはれ」と並ぶ重要美意識として位置づけられ、"
            "近代散文・批評の精神的祖型ともされる。"
        ),
        historical_context="11世紀初頭の宮廷女房文化の知的成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/001102/files/49236_42624.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="竹取物語と起源譚",
        name_en="Taketori Monogatari as origin tale",
        name_original="竹取物語と起源譚", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "『竹取物語』（9世紀末-10世紀初）は「物語の出で来はじめの祖（おや）」"
            "（源氏物語『絵合』巻）と称される、現存最古の作り物語。竹中の少女が"
            "成長して月へ帰る幻想譚で、起源譚（origin tale）・異郷訪問譚・天人女房譚"
            "等の世界的物語型を含む、日本散文虚構の原点的作品。"
        ),
        background="伝承的物語素材と新しい仮名散文形式の最初期の出会い。",
        development=(
            "源氏物語以降の物語の祖型と認識され続け、近代以降は児童文学の"
            "古典的素材として継承。柳田國男・折口信夫の民俗学的研究対象。"
        ),
        historical_context="9-10世紀の散文虚構文学の生誕期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000329/files/18253_12244.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("Myth-Narratives", None, "moon-princess origin myth",
                "shared_concept",
                "世界神話DBの起源譚・天降り型物語の事例")],
    ))

    records.append(dict(
        name_ja="蜻蛉日記と自伝的書字",
        name_en="Kagerō Nikki and autobiographical writing",
        name_original="蜻蛉日記と自伝的書字", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "藤原道綱母『蜻蛉日記』（10世紀後半、974年頃成立）は女性自身による"
            "現存最古の自伝的散文。藤原兼家との結婚生活・愛憎・宗教的内省を21年に"
            "渡り記録し、世界文学史上最も早期の本格自伝文学の一つとされる。"
            "「日記文学」というジャンルの実質的起点。"
        ),
        background="土佐日記の女性仮託に対する、女性自身の本物の自伝的書字の登場。",
        development=(
            "後の和泉式部日記・紫式部日記・更級日記の母型となり、"
            "日本における女流自伝文学の伝統を確立した。"
        ),
        historical_context="10世紀後半の女流文学開花期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000091/files/41254_18920.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("主体", "rethinking",
                      "蜻蛉日記は女性自身による自伝的「私」の確立として世界文学史的に画期的で、"
                      "「書く女性主体」の早期事例として、AIが生成する「自伝風テキスト」の"
                      "主体性問題と直接対比される。",
                      "AI生成の自伝、女性主体のAI模倣")],
        cross=[("AN", None, "women's autobiography", "shared_concept",
                "ジェンダー化された書字実践の人類学的研究との接続")],
    ))

    records.append(dict(
        name_ja="土佐日記と仮名日記",
        name_en="Tosa Nikki and kana diary",
        name_original="土佐日記と仮名日記", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "紀貫之『土佐日記』（935年頃）は土佐から京への55日の帰京記。"
            "「男もすなる日記といふものを、女もしてみむとてするなり」と冒頭に置き、"
            "男性著者が女性語り手に仮託して仮名で日記を書くという二重の書記操作で、"
            "日本における「日記文学」というジャンルの実質的開幕を告げる。"
        ),
        background="漢文公式日記の伝統に対する仮名による私的日記の対抗的創出。",
        development=(
            "蜻蛉日記以下の女流日記文学を直接準備し、日本独自の自伝的散文伝統の起点。"
        ),
        historical_context="10世紀前半の仮名表記の浸透と書記体系の二極化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000091/files/41254_18920.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("作者性", "rethinking",
                      "土佐日記は男性著者が女性語り手を演じるという作者性の二重化を"
                      "日本文学の起点に据えた。AIによるペルソナ生成・人格偽装の"
                      "千年以上前の歴史的先例として、作者性の操作可能性を提起する。",
                      "AIペルソナ、人格偽装LLM、女性語チャットボット")],
        cross=[("PHIL", None, "performative authorship", "shared_concept",
                "パフォーマティヴな作者性論との接続")],
    ))

    records.append(dict(
        name_ja="大鏡と歴史物語",
        name_en="Ōkagami and rekishi monogatari (historical tales)",
        name_original="大鏡と歷史物語", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "『大鏡』（11世紀末-12世紀初）は藤原道長の栄華を中心に14代176年の歴史を"
            "二老人の対話形式で語る歴史物語。「鏡もの」（大鏡・今鏡・水鏡・増鏡）の祖。"
            "歴史を物語化し、虚構的形式に歴史評価を盛る独自のジャンルで、"
            "正史（六国史）と虚構物語の中間に位置する。"
        ),
        background=(
            "六国史終焉後の歴史記述需要と物語形式の発達の結合。"
        ),
        development=(
            "今鏡・水鏡・増鏡の続編を生み、また栄花物語と対をなして"
            "歴史物語というジャンルを確立した。"
        ),
        historical_context="11世紀末の歴史認識と物語形式の融合。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/991120",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="今昔物語と仏教説話",
        name_en="Konjaku Monogatari and Buddhist setsuwa",
        name_original="今昔物語と佛教說話", original_script="japanese",
        period_id=P_CHUKO,
        definition=(
            "『今昔物語集』（12世紀前半）は天竺（インド）・震旦（中国）・本朝（日本）"
            "の三部構成で約千余話を収める世界最大級の説話集。仏教説話を骨格としつつ"
            "世俗説話も多数含み、「今は昔」の定型句で全話が始まる。"
            "中世説話文学の規範となり、近代以降は芥川龍之介の素材源として再発見された。"
        ),
        background=(
            "平安末期の仏教普及（末法思想・浄土信仰）と説話需要の拡大。"
            "中国・インド説話の翻案的受容。"
        ),
        development=(
            "中世の沙石集・古今著聞集等に直接影響、近代では芥川龍之介『羅生門』"
            "『鼻』等の素材源として再生された。"
        ),
        historical_context="平安末-院政期の仏教文化と説話文学の成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/001147/files/49984_43221.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("PHIL", None, "Buddhist narrative ethics", "shared_concept",
                "仏教説話倫理学との接続"),
               ("Myth-Narratives", None, "Konjaku tales", "shared_concept",
                "世界説話DBの主要参照点")],
    ))

    return records


# ----------------------------------------------------------------
# 投入処理
# ----------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("LIT-DB Phase 2 Wave 5 C16: 日本古典文学（上代〜中古）40概念")
    print("=" * 60)

    inserted_ids: list[int] = []
    fourth_tag_count = 0
    cross_domain_count = 0
    relation_count = 0

    with LitDB() as db:
        # Step 1: 期間の準備
        periods = setup_periods(db)
        print(f"[periods] prepared: {list(periods.keys())}")

        # Step 2: 概念レコードリスト構築
        records = build_concept_records(periods)
        print(f"[records] built {len(records)} concept records")
        assert len(records) == 40, f"expected 40 records, got {len(records)}"

        # Step 3: 概念投入
        with db.transaction():
            for rec in records:
                fourth_tags = rec.pop("fourth_tags", [])
                cross = rec.pop("cross", [])

                cid = db.insert_concept(
                    subfield_code="lit_jp_classical",
                    region="東アジア",
                    **rec,
                )
                inserted_ids.append(cid)

                # Step 4: 第四変容タグ付与
                for tag in fourth_tags:
                    axis, status, rationale, ai_phenom = tag
                    db.tag_fourth_transform(
                        cid, axis=axis, status=status,
                        rationale=rationale,
                        related_ai_phenomenon=ai_phenom,
                    )
                    fourth_tag_count += 1

                # Step 5: cross_domain 登録
                for c in cross:
                    target_db, target_id, target_name, link_type, desc = c
                    db.insert_cross_domain(
                        lit_entity_type="concept",
                        lit_entity_id=cid,
                        target_db=target_db,
                        target_entity_id=target_id,
                        target_entity_name=target_name,
                        link_type=link_type,
                        description=desc,
                    )
                    cross_domain_count += 1

            # Step 6: 主要な系譜的relations投入
            def cid_of(name: str) -> int:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE name_ja=? AND region='東アジア' "
                    "AND subfield_id=10",
                    (name,),
                ).fetchone()
                if not row:
                    raise RuntimeError(f"concept not found: {name}")
                return row["id"]

            relations_data = [
                # 上代 → 中古の発展
                ("万葉集", "勅撰和歌集", "precedes",
                 "万葉集の編纂が後の勅撰和歌集（古今集以下）の祖型となった"),
                ("懐風藻", "漢詩文受容", "exemplifies",
                 "懐風藻は奈良朝漢詩文受容の最初期の結晶"),
                ("記紀", "古事記の神話的物語", "contains",
                 "記紀の上巻が神話的物語を構成する"),
                ("記紀", "風土記", "precedes",
                 "記紀の編纂事業の延長として風土記の編纂が命じられた"),
                # 修辞技法の系譜
                ("枕詞", "序詞", "precedes",
                 "短い枕詞から自由度の高い序詞へと修辞が拡張"),
                ("掛詞", "縁語", "precedes",
                 "掛詞の同音多義活用が縁語の連想配置に発展"),
                ("掛詞", "本歌取", "precedes",
                 "掛詞の修辞が本歌取の間テクスト性に統合"),
                # 部立体系
                ("雑歌", "勅撰和歌集", "precedes",
                 "万葉の雑歌が古今集以下の細分化された部立体系の母型"),
                ("相聞歌", "勅撰和歌集", "precedes",
                 "万葉相聞歌が後の「恋」部の起源"),
                ("挽歌", "勅撰和歌集", "precedes",
                 "万葉挽歌が後の「哀傷」部の起源"),
                # 詩学理論の系譜
                ("古今集仮名序", "余情", "precedes",
                 "仮名序の歌論が後の余情論の理論的基礎を提供"),
                ("古今集仮名序", "幽玄前史", "precedes",
                 "仮名序の和歌美意識の体系化が幽玄論を準備"),
                ("余情", "幽玄前史", "extends",
                 "余情論が幽玄論に発展統合された"),
                ("古今集仮名序", "六歌仙", "contains",
                 "仮名序が六歌仙批評を含む"),
                # ジャンル系譜
                ("物語", "歌物語", "contains",
                 "歌物語は物語の一系統"),
                ("物語", "伝奇物語", "contains",
                 "伝奇物語は物語の一系統"),
                ("物語", "源氏物語ともののあはれ", "extends",
                 "源氏物語は物語ジャンルの完成形"),
                ("竹取物語と起源譚", "物語", "precedes",
                 "竹取物語は「物語の出で来はじめの祖」"),
                ("伝奇物語", "竹取物語と起源譚", "contains",
                 "竹取物語は伝奇物語の代表作"),
                ("歌物語", "伊勢物語とみやび", "contains",
                 "伊勢物語は歌物語の代表作"),
                # 日記文学系譜
                ("土佐日記と仮名日記", "日記文学", "precedes",
                 "土佐日記が日記文学ジャンルの実質的起点"),
                ("日記文学", "蜻蛉日記と自伝的書字", "contains",
                 "蜻蛉日記は日記文学の代表作"),
                ("真名と仮名", "土佐日記と仮名日記", "exemplifies",
                 "土佐日記は仮名日記成立の典型例"),
                # 美学概念の関係
                ("もののあはれ", "源氏物語ともののあはれ", "exemplifies",
                 "源氏物語はもののあはれの典型的作品"),
                ("枕草子とをかし", "随筆", "exemplifies",
                 "枕草子は随筆の代表作"),
                ("もののあはれ", "枕草子とをかし", "criticizes",
                 "「あはれ」と「をかし」は平安美学の二大対比軸"),
                # 説話系譜
                ("説話", "今昔物語と仏教説話", "extends",
                 "今昔物語集は説話文学の集大成"),
                # 歴史物語
                ("大鏡と歴史物語", "軍記物語前史", "precedes",
                 "歴史物語の発達と並行して軍記物語の前史が形成"),
                # 漢詩文受容との関係
                ("漢詩文受容", "懐風藻", "precedes",
                 "懐風藻が漢詩文受容の最初の文学的結晶"),
                ("漢詩文受容", "物語", "precedes",
                 "漢詩文受容（白氏文集等）が源氏物語等の物語に深く浸透"),
                # 書記体系の影響
                ("真名と仮名", "物語", "precedes",
                 "仮名の確立が仮名物語文学を可能にした"),
                ("真名と仮名", "日記文学", "precedes",
                 "仮名の確立が仮名日記文学を可能にした"),
                # 修辞と本歌取
                ("本歌取", "勅撰和歌集", "exemplifies",
                 "本歌取は新古今和歌集の主要技法"),
                # 国讃め歌系譜
                ("国讃め歌", "雑歌", "extends",
                 "国讃め歌は雑歌部立に分類される"),
                # 歌合と勅撰
                ("歌合", "勅撰和歌集", "precedes",
                 "歌合の判詞蓄積が勅撰集の歌論的基盤"),
            ]
            for src, tgt, rtype, desc in relations_data:
                db.insert_relation(
                    source_type="concept",
                    source_id=cid_of(src),
                    target_type="concept",
                    target_id=cid_of(tgt),
                    relation_type=rtype,
                    description=desc,
                    confidence=4,
                    source_evidence="日本古典文学史標準的記述（上代・中古）",
                )
                relation_count += 1

        # Step 7: 検証
        print()
        print("=" * 60)
        print("投入結果サマリー")
        print("=" * 60)
        print(f"concepts inserted: {len(inserted_ids)}")
        print(f"fourth_transform_tags: {fourth_tag_count}")
        print(f"cross_domain links: {cross_domain_count}")
        print(f"relations: {relation_count}")
        print()

        # サブフィールド別カウント
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id=10"
        ).fetchone()
        print(f"subfield_id=10 total concepts: {row['c']}")

        # Tier別
        rows = db.conn.execute(
            "SELECT source_tier, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=10 GROUP BY source_tier"
        ).fetchall()
        print(f"source_tier distribution (subfield 10): {[dict(r) for r in rows]}")

        # importance別
        rows = db.conn.execute(
            "SELECT importance_score, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=10 GROUP BY importance_score ORDER BY importance_score DESC"
        ).fetchall()
        print(f"importance_score distribution: {[dict(r) for r in rows]}")

        # canonical別
        rows = db.conn.execute(
            "SELECT canonical_in_region, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=10 GROUP BY canonical_in_region"
        ).fetchall()
        print(f"canonical_in_region distribution: {[dict(r) for r in rows]}")

        # 第四変容タグ分布
        rows = db.conn.execute(
            """SELECT t.axis, t.status, COUNT(*) AS c
               FROM fourth_transform_tags t
               JOIN concepts c ON t.concept_id = c.id
               WHERE c.subfield_id = 10
               GROUP BY t.axis, t.status
               ORDER BY t.axis, t.status"""
        ).fetchall()
        print(f"fourth_transform distribution (subfield 10):")
        for r in rows:
            print(f"  {dict(r)}")

        # cross_domain分布
        rows = db.conn.execute(
            """SELECT cd.target_db, COUNT(*) AS c
               FROM cross_domain cd
               JOIN concepts c ON cd.lit_entity_id = c.id AND cd.lit_entity_type='concept'
               WHERE c.subfield_id = 10
               GROUP BY cd.target_db"""
        ).fetchall()
        print(f"cross_domain distribution (subfield 10): {[dict(r) for r in rows]}")

    print()
    print("[done] C16 投入完了")


if __name__ == "__main__":
    main()
