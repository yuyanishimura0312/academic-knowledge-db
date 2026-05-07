"""
LIT-DB Phase 2 Wave 7: C17 — 日本古典文学（中世〜近世）40概念投入スクリプト

主パターン: P1 (Canonical Primary Pursuit)
subfield_id=10 (lit_jp_classical), region='東アジア'

C16（上代・中古）と同subfield・同region。中世（鎌倉・室町）と近世（江戸）担当。
C16との重複ゼロ（事前確認済み）。

構成（5カテゴリ × 8件 = 40件）:
- A: 中世の主要ジャンル・主題（8件）
- B: 中世の詩学・批評（8件）
- C: 近世の主要ジャンル・形式（8件）
- D: 近世の主要作家・概念（8件）
- E: 主要詩学・批評概念（8件）

第四変容タグ: 不易流行・虚実皮膜論・幽玄（世阿弥）・浮世草子・国学のもののあはれ
再評価ほか12件以上付与。
PT・PHIL・AN との cross_domain を10件以上記録。

使用法:
    python3 wave7_c17_japan_classical_late.py
"""

from __future__ import annotations

from lit_db_helper import LitDB


# ----------------------------------------------------------------
# 期間（中世・近世）の用意
# ----------------------------------------------------------------

def setup_periods(db: LitDB) -> dict:
    """中世・近世（鎌倉〜江戸）の主要時代区分を get_or_create する。"""
    periods = {}
    periods["中世"] = db.get_or_create_period(
        name_ja="中世", name_en="Chūsei (Medieval / Kamakura-Muromachi)",
        region="東アジア", start_year=1185, end_year=1603,
        description=(
            "鎌倉時代〜室町時代末（戦国期含む）。武家文化と仏教の深化、"
            "新古今和歌集・軍記物語・連歌・能楽・五山文学が興隆した時代。"
        ),
    )
    periods["近世"] = db.get_or_create_period(
        name_ja="近世", name_en="Kinsei (Early Modern / Edo)",
        region="東アジア", start_year=1603, end_year=1868,
        description=(
            "江戸時代。町人文化の成立と出版文化の隆盛、"
            "俳諧・浮世草子・浄瑠璃・歌舞伎・読本・戯作が"
            "都市的読者市場を背景に発達した時代。"
        ),
    )
    return periods


# ----------------------------------------------------------------
# 40概念データ定義
# ----------------------------------------------------------------

def build_concept_records(periods: dict) -> list[dict]:
    """40概念のレコードリストを構築する。"""
    P_CHUSEI = periods["中世"]
    P_KINSEI = periods["近世"]

    records: list[dict] = []

    # ============================================================
    # A. 中世の主要ジャンル・主題（8件）
    # ============================================================
    records.append(dict(
        name_ja="軍記物語", name_en="gunki monogatari (war tales)",
        name_original="軍記物語", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "鎌倉〜室町期に成立した、武士の合戦と興亡を主題とする物語群の総称。"
            "『保元物語』『平治物語』『平家物語』『太平記』が代表で、"
            "歴史叙述と仏教的無常観・武士道倫理が融合する。琵琶法師の語り（平曲）"
            "という口承的伝承を伴い、書承と口承の交差点に位置する独自ジャンル。"
        ),
        background=(
            "源平争乱（1180-85）と承久の乱・南北朝動乱という大規模戦乱が、"
            "敗者と死者を語り継ぐ叙事的欲求を生んだ。"
        ),
        development=(
            "近世以降は浄瑠璃・歌舞伎・読本の素材源となり、"
            "近代以降も小説・映画・大河ドラマの参照体系として機能し続けている。"
        ),
        historical_context="武家政権成立期の戦乱と仏教的歴史観の融合。",
        primary_source_url="https://www.aozora.gr.jp/cards/000091/files/859_22020.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("物語", "partial",
                      "軍記物語は書承と口承の交差点で成立し、語り手（琵琶法師）と書記者の"
                      "二重作者性を持つ。AI生成物語における「複数声」の歴史的範例。",
                      "AIによる多声的物語生成、口承・書承融合")],
        cross=[("PT", None, "epic narrative", "parallel",
                "西欧叙事詩（ホメロス・武勲詩）との比較対象、ただし"
                "仏教的無常観を基底とする点で異なる")],
    ))

    records.append(dict(
        name_ja="無常観", name_en="mujōkan (sense of impermanence)",
        name_original="無常観", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "中世日本文学を貫く根本的な世界観。仏教の「諸行無常」を基礎に、"
            "万物の流転・栄枯盛衰・生死の儚さに対する鋭敏な感受性を含む。"
            "『方丈記』『徒然草』『平家物語』冒頭等に典型的に表現され、"
            "鴨長明・吉田兼好・西行らの隠者文学を通じて中世美学の中核となった。"
        ),
        background=(
            "源平争乱・承久の乱・末法思想・天変地異（養和の飢饉等）が"
            "現世の不安定性を実感させた中世初期の歴史的経験。"
        ),
        development=(
            "中世連歌論・能楽論（幽玄・冷えさび）・近世の枯淡美意識・"
            "近代の「もののあはれ」再評価へと連続的に継承された。"
        ),
        historical_context="鎌倉新仏教の浸透と隠者文学の成立。",
        primary_source_url="https://www.aozora.gr.jp/cards/000196/files/975_15935.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("PHIL", None, "Buddhist anitya / impermanence",
                "shared_concept",
                "仏教哲学の無常思想と日本中世美学の接続点"),
               ("AN", None, "ethnographic time and decay", "parallel",
                "人類学における時間・崩壊観の比較対象")],
    ))

    records.append(dict(
        name_ja="連歌", name_en="renga (linked verse)",
        name_original="連歌", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "複数人が交互に5・7・5（長句）と7・7（短句）を付け合って一連の"
            "詩を構成する集団詩形式。鎌倉末〜室町期に和歌から派生し独立した。"
            "短歌の上の句と下の句を別人が詠むという「付合」を反復し、"
            "百句連ねる「百韻」が標準形式となった。二条良基・心敬・宗祇らが大成。"
        ),
        background=(
            "院政期の鎖連歌（短い遊戯的応酬）が、武家社会・寺院社会で席の文芸として"
            "発展し、中世特有の集団的創作文化を形成した。"
        ),
        development=(
            "近世初期に俳諧連歌（俳諧）に分岐し、芭蕉らの蕉風俳諧、"
            "明治以後の俳句独立に至る系譜を形成した。"
        ),
        historical_context="中世武家・寺院社会における座の文芸の隆盛。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("作者性", "rethinking",
                      "連歌は単独作者性を解体し、複数人の付合の連鎖として成立する集団詩で、"
                      "近代的「個人作者」概念の解体的範例。AIと人間の協働創作（共著）の"
                      "歴史的先例として再評価しうる。",
                      "AI共著、人間-AI協働創作、集団的著作権")],
        cross=[("PT", None, "collaborative poetry / collective authorship",
                "shared_concept",
                "詩学DBの集団創作論との接続点")],
    ))

    records.append(dict(
        name_ja="発句（連歌）", name_en="hokku (opening verse of renga)",
        name_original="發句", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "連歌の一座の冒頭に置かれる5・7・5の長句。連歌全体の主題的・季節的"
            "枠組を提示する役割を担い、後句との独立性が高いことから、"
            "近世初期に独立した詩形（俳諧の発句、後の俳句）への分岐の母胎となった。"
            "二条良基『連理秘抄』『筑波問答』で発句作法が体系化された。"
        ),
        background="室町期の連歌儀礼における冒頭句の重要性の高まり。",
        development=(
            "松永貞徳・松尾芭蕉らの俳諧で発句単独鑑賞が定着し、"
            "正岡子規の俳句独立論に至る道を開いた。"
        ),
        historical_context="室町連歌の儀礼化と作法書文化。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="中世説話文学", name_en="medieval setsuwa literature",
        name_original="中世説話", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "中世（特に鎌倉期）に大量に編まれた仏教・世俗説話集。"
            "『宇治拾遺物語』『十訓抄』『古今著聞集』『沙石集』等が代表。"
            "今昔物語集の伝統を継ぎつつ、布教用・教訓用に再編成され、"
            "庶民の口承伝承と寺院の教説書記が交錯する場として機能した。"
        ),
        background=(
            "鎌倉新仏教の布教活動と、武家・庶民層への文学享受拡大に伴う"
            "口承・書承の混合的編纂の隆盛。"
        ),
        development=(
            "近世の浮世草子・落語・講談、近代の民俗学・口承文学研究へと"
            "素材的・方法的に継承された。"
        ),
        historical_context="鎌倉仏教の庶民教化と口承文化の書記化。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        cross=[("AN", None, "folk narrative collection", "shared_concept",
                "人類学的口承研究における説話集の位置")],
    ))

    records.append(dict(
        name_ja="御伽草子", name_en="otogizōshi (companion tales)",
        name_original="御伽草子", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "室町期〜江戸初期に流行した短編絵入り物語の総称。"
            "『一寸法師』『鉢かづき』『酒呑童子』『浦島太郎』等を含む約400編が"
            "知られる。貴族文学（物語）と庶民口承伝承の中間に位置し、"
            "挿絵を伴うビジュアル文学の最初の大量現象。"
        ),
        background="室町期の町衆文化と絵巻・絵入り本の制作技術発達。",
        development=(
            "近世の浮世草子・赤本・黒本・青本に直結し、"
            "現代の童話・絵本・アニメの祖型を形成した。"
        ),
        historical_context="室町期の町衆文化と絵入り出版の発達。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/2541380",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("受容", "partial",
                      "御伽草子は絵と文の融合を前提とする最初の大量視覚文学で、"
                      "現代マルチモーダルAI（絵+文の同時生成）の歴史的先例。",
                      "マルチモーダルAI、絵入り物語生成")],
    ))

    records.append(dict(
        name_ja="五山文学", name_en="Gozan literature (Zen monastic Sinitic)",
        name_original="五山文學", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "鎌倉末〜室町期、京都五山・鎌倉五山の禅僧らによる漢詩文の総称。"
            "義堂周信・絶海中津らが代表。宋元学・朱子学を取り込み、"
            "禅の悟境と中国詩文の伝統を融合させた。日本中世における漢学の中心として"
            "機能し、近世儒学・国学への基盤を提供した。"
        ),
        background=(
            "渡来僧（蘭渓道隆・無学祖元等）と入宋・入元僧の往来による"
            "禅文化と宋元文学の直接移入。"
        ),
        development=(
            "近世の藤原惺窩・林羅山ら朱子学者の素養基盤となり、"
            "儒学・漢詩文教養の制度化を準備した。"
        ),
        historical_context="日中禅僧交流と宋元学の輸入。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        cross=[("PHIL", None, "Zen and Neo-Confucian transmission",
                "shared_concept",
                "禅・朱子学の日本受容研究との接続点")],
    ))

    records.append(dict(
        name_ja="能（夢幻能）", name_en="nō (mugen-nō / dream-vision nō)",
        name_original="能（夢幻能）", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "観阿弥・世阿弥が大成した中世舞台芸術「能」の主要形式の一つ。"
            "ワキ（旅僧等）が宿る場所に過去の亡霊（シテ）が現れて昔語りをし、"
            "後場で本来の姿に戻って舞を披露する二場構成を取る。"
            "現実と異界、過去と現在、生者と死者の境界を主題化する独自の劇形式。"
        ),
        background=(
            "猿楽・田楽の芸能伝統と禅・浄土宗の死者鎮魂思想、"
            "和歌・連歌の余情美学が融合した室町期の舞台芸術革新。"
        ),
        development=(
            "観世流以下の流派分立を経て近世に幕府式楽として制度化され、"
            "現代まで生きた古典として継承されている。"
        ),
        historical_context="室町期の足利将軍家庇護下での能楽大成。",
        primary_source_url="https://www2.ntj.jac.go.jp/dglib/contents/learn/edc25/index.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("物語", "partial",
                      "夢幻能は「死者が語る」形式で、語り手と被語り手の境界を"
                      "舞台上で解体する。AI生成における「不在の声」の演出と構造的に並行。",
                      "AI生成における故人の声、死者の語り再現")],
        cross=[("PT", None, "dream-vision genre", "parallel",
                "西欧中世の夢幻文学（『薔薇物語』等）との比較対象")],
    ))

    # ============================================================
    # B. 中世の詩学・批評（8件）
    # ============================================================
    records.append(dict(
        name_ja="心敬ささめごと", name_en="Shinkei's Sasamegoto",
        name_original="ささめごと", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "連歌師心敬（1406-1475）が著した代表的連歌論書（1463-1464頃）。"
            "「冷え寂び」「ひえ枯る」を中心に、世俗的華美を排した枯淡幽玄の美意識を"
            "理論化した。和歌・連歌・仏道修行を一体として論じ、中世連歌論の最高峰と"
            "され、後の宗祇・芭蕉らに直接影響を与えた。"
        ),
        background=(
            "心敬の禅修行・天台宗素養と、応仁の乱前夜の戦乱不安が"
            "枯淡美への志向を生んだ。"
        ),
        development=(
            "宗祇『吾妻問答』、芭蕉の蕉風俳諧（さび・しおり）に直接系譜的に"
            "受け継がれた。"
        ),
        historical_context="室町後期連歌論の成熟期。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="二条良基連歌論", name_en="Nijō Yoshimoto's renga theory",
        name_original="二條良基連歌論", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "南北朝期の関白二条良基（1320-1388）が編んだ連歌論・式目の体系。"
            "『応安新式』（1372）で連歌の式目（去嫌・季節・配置の規則）を確立し、"
            "『筑波問答』『連理秘抄』で連歌の理論的基礎を提供した。"
            "中世連歌の制度的・理論的基盤を整えた最重要人物。"
        ),
        background=(
            "南北朝期の連歌の貴族・武家・僧侶を横断する場の文芸化と、"
            "規則体系化の必要性。"
        ),
        development=(
            "心敬・宗祇・宗長らの理論を経て、近世俳諧式目（貞門・談林・蕉風）に"
            "まで継承された。"
        ),
        historical_context="南北朝期の連歌制度化。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="世阿弥風姿花伝", name_en="Zeami's Fūshikaden",
        name_original="風姿花傳", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "観世流二世世阿弥（1363?-1443?）が著した能楽論書（1400-18年頃）。"
            "全7篇からなり、芸能修行論・演出論・批評論・「花」の美学論を体系化した。"
            "「秘すれば花」「時分の花」「真の花」など独自の美学概念を展開し、"
            "東アジア演劇論の最高峰、世界演劇論の古典の一つ。"
        ),
        background="観阿弥・世阿弥父子による能の芸術的完成と理論化の事業。",
        development=(
            "近世まで秘伝書として一族に継承され、明治期に発見・刊行されて"
            "近代演劇論・西洋演劇論との対話を生んだ。"
        ),
        historical_context="室町前期の能の大成期。",
        primary_source_url="https://www.aozora.gr.jp/cards/001443/files/56682_67076.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "世阿弥の「秘すれば花」は、創造の源泉を非顕示・隠蔽に置く独自の創造性論で、"
                      "AI生成の「全てを生成・全てを開示」傾向と対照をなす。"
                      "非開示・余白を伴う創造性の歴史的範例。",
                      "AI生成の透明性問題、創造の隠蔽性")],
        cross=[("PT", None, "performance theory / dramatic poetics",
                "shared_concept",
                "西欧演劇論（アリストテレス『詩学』等）との比較対象")],
    ))

    records.append(dict(
        name_ja="世阿弥幽玄", name_en="Zeami's yūgen",
        name_original="幽玄", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "世阿弥が能楽美学の中心に据えた美的理念。「奥深く幽かなる優美」を意味し、"
            "和歌・連歌の「幽玄」概念を能楽の身体表現・劇的構成に応用した。"
            "見えるものの奥に見えないものを感じさせる象徴的・暗示的美意識で、"
            "中世美学の最高概念の一つ。"
        ),
        background=(
            "藤原俊成・定家の和歌幽玄論、心敬の連歌論を世阿弥が能の身体性へ転用。"
        ),
        development=(
            "近世の俳諧論・茶道論（侘び寂び）、近代の岡倉天心『茶の本』、"
            "ハイデガー受容を通じた現代美学の比較対象まで継承された。"
        ),
        historical_context="室町期能楽美学の成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/001443/files/56682_67076.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "rethinking",
                      "幽玄は「言葉にしない・見せない」ことで生じる美で、"
                      "AI生成が「全てを言語化・視覚化する」傾向と根本的に対立する。"
                      "余白・暗示の美学の歴史的範例として再評価される。",
                      "AI生成の過剰説明性、暗示の不可能性"),
                     ("言語", "partial",
                      "幽玄は言語化を超える領域を志向する点で、"
                      "言語生成AIの能力境界を考える参照点となる。",
                      "LLMの言語化限界、暗黙知のAI処理")],
        cross=[("PHIL", None, "ineffable aesthetics", "shared_concept",
                "東西の言語化不能美学の比較研究")],
    ))

    records.append(dict(
        name_ja="世阿弥物まね", name_en="Zeami's monomane (mimesis)",
        name_original="物まね", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "世阿弥能楽論における演技の根本原理。対象（人物・草木・霊等）を"
            "そのまま模倣する「真の物まね」を基本とし、老体・女体・軍体等の"
            "「三体」分類による身体的演技体系を構築した。「似せる」ことを通じて"
            "「似せざる」境地（花）に至る逆説的演技論。"
        ),
        background="猿楽の写実的演技伝統と禅的「離見の見」の融合。",
        development=(
            "近世歌舞伎・人形浄瑠璃の演技論、近代演劇の写実主義論争、"
            "ブレヒト『中国演劇の異化効果』との比較対象となった。"
        ),
        historical_context="室町期能楽演技論の確立。",
        primary_source_url="https://www.aozora.gr.jp/cards/001443/files/56682_67076.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        cross=[("PT", None, "mimesis / imitation theory", "parallel",
                "アリストテレスのミメーシス論との比較対象")],
    ))

    records.append(dict(
        name_ja="連歌の付合論", name_en="renga tsukeai theory (linking aesthetics)",
        name_original="付合論", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "連歌で前句に次句を付ける際の連接美学を論じた理論。"
            "「物付」（語の連想）・「心付」（情趣の連想）・「響付」（音韻的連想）等の"
            "分類があり、近接性と意外性、調和と転換のバランスを論じる。"
            "二条良基『連理秘抄』、心敬『ささめごと』が体系化。"
        ),
        background="室町連歌の集団詩としての連接技法の理論化。",
        development=(
            "近世の俳諧式目（去嫌・配合）に継承され、明治以後の連歌・連句研究、"
            "詩的連想の比較研究の素材となった。"
        ),
        historical_context="室町連歌論の成熟。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("作者性", "partial",
                      "付合論は「先行句に応答する」形で詩を生成する原理で、"
                      "AIプロンプト連鎖（chain-of-thought, agentic loops）の歴史的先例。",
                      "プロンプトチェーン、エージェント連鎖型生成")],
    ))

    records.append(dict(
        name_ja="心敬の冷えさび", name_en="Shinkei's hie-sabi (cold austerity)",
        name_original="冷えさび", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "心敬が連歌の理想美として提示した美意識。「冷ゆ」「ひえさび」「ひえ枯る」"
            "等の語で表現され、世俗的華美・色彩・賑わいを排し、"
            "枯淡・寂寥・透徹を志向する。中世美学の極北の一つで、"
            "近世芭蕉の「さび」の直接的源流。"
        ),
        background="心敬の禅修行と応仁前夜の戦乱不安からの内向的美意識深化。",
        development=(
            "宗祇・宗長を経て松尾芭蕉の蕉風俳諧（さび・しおり）に結実し、"
            "茶道の侘び美学とも合流した。"
        ),
        historical_context="室町後期連歌論の禅的深化。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="京極派と二条派", name_en="Kyōgoku-ha vs Nijō-ha (medieval waka factions)",
        name_original="京極派・二條派", original_script="japanese",
        period_id=P_CHUSEI,
        definition=(
            "鎌倉後期〜南北朝期の和歌界を二分した流派対立。"
            "二条派（二条為世ら）が古今集以来の正統を守る保守派、"
            "京極派（京極為兼ら）が革新的写実・新表現を志向する革新派。"
            "『玉葉和歌集』『風雅和歌集』に京極派の独自性が結実した。"
        ),
        background="御子左家の分裂と冷泉家・京極家・二条家の血統的対立。",
        development=(
            "南北朝以後の和歌史は二条派が主流となるが、京極派の革新性は"
            "近世の伊藤梅宇・近代正岡子規の万葉再評価に再発見された。"
        ),
        historical_context="鎌倉後期の和歌流派対立と勅撰集編纂。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    # ============================================================
    # C. 近世の主要ジャンル・形式（8件）
    # ============================================================
    records.append(dict(
        name_ja="俳諧連歌", name_en="haikai-renga (comic linked verse)",
        name_original="俳諧連歌", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世初期に正統連歌から分岐した俳諧的（滑稽・俗語的）連歌。"
            "山崎宗鑑『新撰犬筑波集』（16世紀前半）に始まり、"
            "松永貞徳の貞門俳諧、西山宗因の談林俳諧を経て、"
            "松尾芭蕉の蕉風俳諧で芸術的完成を見た。"
        ),
        background="連歌の宮廷的・貴族的形式化に対する町人・地方文化の反発。",
        development=(
            "貞門（貞徳）→談林（宗因）→蕉風（芭蕉）→天明俳諧（蕪村）→"
            "明治の正岡子規俳句独立論まで連続的に発展した。"
        ),
        historical_context="近世初期の町人文化の形成と連歌の俗化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000020/files/57754_67144.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="俳句独立", name_en="independence of haiku (from haikai)",
        name_original="俳句獨立", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "俳諧連歌の発句が単独鑑賞・単独制作の対象として独立する歴史的過程。"
            "蕉風俳諧における発句の重要性増大に始まり、"
            "近世後期の月並俳諧での発句単独化を経て、"
            "明治の正岡子規『獺祭書屋俳話』『俳諧大要』（1893以降）で"
            "「俳句」概念として完成した。"
        ),
        background=(
            "連歌の集団的制作場の衰退と、近代的個人作者意識の浸透。"
        ),
        development=(
            "高浜虚子・河東碧梧桐らによる近代俳句運動を経て、"
            "現代俳句・国際的HAIKU運動へと展開した。"
        ),
        historical_context="近世後期〜明治の文学制度の近代化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000305/files/45617_24850.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("作者性", "partial",
                      "俳句独立は集団的連歌の中で生まれる発句が、"
                      "近代的個人作者の所有物に転換する過程で、"
                      "AI共著時代における「個人作者の歴史的構築性」を示す範例。",
                      "個人作者性の歴史的構築、AI共著における作者帰属")],
    ))

    records.append(dict(
        name_ja="浮世草子", name_en="ukiyo-zōshi (tales of the floating world)",
        name_original="浮世草子", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "井原西鶴『好色一代男』（1682）に始まる近世前期上方の風俗小説ジャンル。"
            "町人の恋愛・経済・職業生活を写実的かつ機知豊かに描き、"
            "好色物・町人物・武家物・気質物に分類される。"
            "西鶴・西沢一風・江島其磧らが代表作家で、近世大衆小説の起源。"
        ),
        background=(
            "元禄期の上方町人経済の隆盛と、出版業（版本）の商業的発展、"
            "御伽草子・仮名草子の文学伝統の蓄積。"
        ),
        development=(
            "宝暦期以降衰退するが、江戸の黄表紙・読本・人情本に"
            "町人文学の伝統を引き継いだ。"
        ),
        historical_context="元禄期上方町人文化の隆盛と出版革命。",
        primary_source_url="https://www.aozora.gr.jp/cards/000139/files/56533_57497.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "rethinking",
                      "浮世草子は出版・市場・読者層の成立を前提とする「大衆消費文学」の起源で、"
                      "AI生成コンテンツの大量供給時代における「読者の選別力」問題の歴史的先例。",
                      "AI生成大量コンテンツの消費、市場主導の文学生産")],
        cross=[("AN", None, "Edo townsfolk culture", "shared_concept",
                "江戸町人文化の人類学的研究との接続点")],
    ))

    records.append(dict(
        name_ja="黄表紙", name_en="kibyōshi (yellow-cover comics)",
        name_original="黄表紙", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "安永〜文政期（1775-1830頃）に江戸で流行した絵入り戯作本。"
            "黄色い表紙が名の由来。1ページに絵と書込文を配し、"
            "風刺・洒落・うがちを身上とする。恋川春町『金々先生栄花夢』（1775）を"
            "嚆矢とし、山東京伝・朋誠堂喜三二らが代表作家。"
        ),
        background=(
            "江戸の出版文化成熟と町人読者の知的遊戯欲求、"
            "上方浮世草子の影響と江戸独自の俗文化の発展。"
        ),
        development=(
            "寛政の改革で弾圧され衰退したが、合巻（柳亭種彦『偐紫田舎源氏』等）"
            "に変容して幕末まで継承された。現代漫画の祖型の一つ。"
        ),
        historical_context="安永・天明期江戸町人文化の絵入り出版隆盛。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="読本", name_en="yomihon (reading books)",
        name_original="讀本", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世後期の長編構築的小説ジャンル。絵を従とし読み応えを主とした"
            "ことから「読本」と呼ばれる。中国白話小説（『水滸伝』『三国志演義』）の"
            "翻案を含み、勧善懲悪・因果応報を主題とする。"
            "上田秋成『雨月物語』、滝沢馬琴『南総里見八犬伝』が代表作。"
        ),
        background=(
            "中国白話小説の輸入と翻訳、寛政期以降の戯作弾圧による"
            "より「真面目な」小説への需要増大。"
        ),
        development=(
            "幕末期に最高潮を迎え、近代小説（坪内逍遙・尾崎紅葉・幸田露伴）への"
            "前史的役割を果たした。"
        ),
        historical_context="近世後期の長編小説の確立期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000019/files/14066_28076.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="戯作", name_en="gesaku (playful fiction)",
        name_original="戲作", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世後期の通俗娯楽小説の総称。黄表紙・洒落本・滑稽本・人情本・"
            "合巻・読本を含む広義カテゴリで、職業作家（戯作者）が町人読者向けに"
            "書いた市場文学。「戯（たわむれ）の作」と自称する自己卑下の修辞を伴う。"
            "山東京伝・式亭三馬・十返舎一九・為永春水らが代表。"
        ),
        background="江戸出版業の成熟と町人読者市場の確立、職業作家の成立。",
        development=(
            "明治初年も継続するが、坪内逍遙『小説神髄』（1885）の戯作批判で"
            "「近代小説」に道を譲ったとされる。近年は再評価されている。"
        ),
        historical_context="近世後期の市場文学・職業作家成立。",
        primary_source_url="https://www.aozora.gr.jp/cards/000308/files/2364_22013.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="浄瑠璃", name_en="jōruri (puppet theater chanted narrative)",
        name_original="淨瑠璃", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "三味線伴奏の語り物芸能。近世初期に人形操りと結合し人形浄瑠璃（文楽）として大成。"
            "義太夫節（竹本義太夫）が18世紀以降の主流となり、"
            "近松門左衛門の世話物・時代物の名作を生んだ。"
            "歌舞伎と並ぶ近世舞台芸術の双璧。"
        ),
        background=(
            "中世末の浄瑠璃姫物語の語り物伝統、人形操り芸能の発達、"
            "近世初期の三味線輸入の融合。"
        ),
        development=(
            "義太夫節以降、豊竹座・竹本座の隆盛、近松没後の合作時代を経て、"
            "現代まで国立劇場を中心に伝承されている。"
        ),
        historical_context="近世初期〜中期の上方人形劇隆盛。",
        primary_source_url="https://www.aozora.gr.jp/cards/000064/files/362_22210.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="歌舞伎", name_en="kabuki",
        name_original="歌舞伎", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世初期に出雲阿国の「かぶき踊」（1603頃）に発し、"
            "野郎歌舞伎・元禄歌舞伎・化政歌舞伎へと発展した近世大衆舞台芸術。"
            "荒事（市川団十郎）と和事（坂田藤十郎）の演技様式、"
            "立役・女形・敵役の役柄分化、所作事・世話物・時代物の演目分類が特徴。"
        ),
        background="中世猿楽・能の伝統、近世初期の風俗芸能（かぶき）の隆盛。"
                   "浄瑠璃との相互影響。",
        development=(
            "浄瑠璃から多数の作品を移入（義経千本桜・仮名手本忠臣蔵等）、"
            "幕末の鶴屋南北・河竹黙阿弥で爛熟期を迎え、現代まで継承される。"
        ),
        historical_context="近世大衆都市文化の総合芸術。",
        primary_source_url="https://www2.ntj.jac.go.jp/dglib/",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("AN", None, "popular performance / urban folk theater",
                "shared_concept",
                "都市民俗芸能の人類学的研究との接続点")],
    ))

    # ============================================================
    # D. 近世の主要作家・概念（8件）
    # ============================================================
    records.append(dict(
        name_ja="松尾芭蕉不易流行", name_en="Bashō's fueki ryūkō",
        name_original="不易流行", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "松尾芭蕉（1644-1694）が晩年の蕉風俳諧で展開した中核理念。"
            "「不易」（永遠不変の真）と「流行」（時々の新しさ）の二極が"
            "根源において一であるという俳諧美学・創造論。"
            "弟子向井去来『去来抄』に詳述され、芭蕉俳論の最高概念とされる。"
        ),
        background=(
            "貞門・談林俳諧の語呂合わせ・滑稽性を超えた、"
            "芭蕉の「奥の細道」前後の精神的深化。"
        ),
        development=(
            "蕪村・一茶を経て近代の正岡子規・高浜虚子の俳句論、"
            "現代俳句論まで参照され続けている。"
        ),
        historical_context="元禄期蕉風俳諧の成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/000146/files/4885_8729.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "不易流行は「永遠の真と時代の新しさ」の弁証法で、"
                      "AI生成における「学習データ（不易）と新規生成（流行）」の関係を"
                      "考える歴史的範例。",
                      "AI生成における学習データと新規性の弁証法"),
                     ("真正性", "rethinking",
                      "「真の俳諧」を不変と変化の統合に求める姿勢は、"
                      "AI時代の「真正な創造」を不変要素と新規要素のどちらに置くかという"
                      "問いに直結する。",
                      "AI創造の真正性、本物らしさの構造")],
        cross=[("PHIL", None, "permanence and change", "shared_concept",
                "東洋哲学の不変・変化論との接続")],
    ))

    records.append(dict(
        name_ja="芭蕉軽み", name_en="Bashō's karumi (lightness)",
        name_original="輕み", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "芭蕉が晩年（元禄6-7年頃）に提唱した俳諧の最終理念。"
            "「重き」を脱した日常性・平明性を称揚する。「梅が香にのつと日の出る山路かな」"
            "等が範例。観念的な深刻さや凝った修辞を脱し、日常の何気ない瞬間に"
            "詩的真実を見出す芭蕉俳論の到達点とされる。"
        ),
        background="蕉風俳諧の「さび・しおり・細み」段階を経た更なる超越への志向。",
        development=(
            "一茶の生活感俳諧、近代正岡子規の写生主義、"
            "現代俳句の日常派系譜（飯田龍太・森澄雄等）まで継承された。"
        ),
        historical_context="芭蕉晩年の俳諧理念深化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000146/files/4885_8729.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="芭蕉さびしおり", name_en="Bashō's sabi and shiori",
        name_original="さび・しをり", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "芭蕉俳諧の中核美意識。「さび」は枯淡・寂寥の境地、"
            "「しおり」（撓り）は対象への深い同情・感情の余韻を意味する。"
            "心敬の冷えさび・幽玄を継承しつつ、俳諧の身体的瞬間性に応用した。"
            "『笈の小文』『去来抄』『三冊子』に理論化されている。"
        ),
        background="心敬連歌論・能楽幽玄論の中世美学伝統の継承。",
        development=(
            "蕉門俳諧の中核美学として継承され、近代日本美学（岡倉天心・"
            "西田幾多郎）を経て現代茶道・建築美学（侘び寂び）にまで展開した。"
        ),
        historical_context="元禄蕉風俳諧美学の確立。",
        primary_source_url="https://www.aozora.gr.jp/cards/000146/files/4885_8729.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("PT", None, "wabi-sabi aesthetics", "shared_concept",
                "詩学DBの東洋美学ノードとの接続")],
    ))

    records.append(dict(
        name_ja="井原西鶴浮世", name_en="Ihara Saikaku's ukiyo (floating world)",
        name_original="浮世", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "井原西鶴（1642-1693）の浮世草子に結晶した近世初期の世界観。"
            "「浮世」とは仏教的「憂き世」（厭うべき世）から、"
            "現世の快楽と経済を肯定する近世町人的「浮かれ世」への意味転換を遂げた語で、"
            "西鶴文学はこの転換を文学的に定着させた。"
        ),
        background=(
            "元禄期上方町人の経済的繁栄と、仏教的厭世観からの解放、"
            "現世享楽主義の台頭。"
        ),
        development=(
            "浮世絵（菱川師宣以降）・浮世風呂・浮世床等の町人文化全般に拡張し、"
            "近代の「世俗化」概念の日本的範型となった。"
        ),
        historical_context="元禄期上方町人文化の世界観転換。",
        primary_source_url="https://www.aozora.gr.jp/cards/000139/files/56533_57497.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        cross=[("AN", None, "secularization of worldview", "shared_concept",
                "世俗化の人類学的・歴史社会学的研究との接続")],
    ))

    records.append(dict(
        name_ja="近松門左衛門虚実皮膜論",
        name_en="Chikamatsu's kyojitsu hifukuron (theory of art between truth and falsehood)",
        name_original="虚實皮膜論", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近松門左衛門（1653-1725）の浄瑠璃・歌舞伎作劇論として穂積以貫"
            "『難波土産』（1738）に伝えられる芸術論。「芸といふものは実と虚との"
            "皮膜の間にあるもの也」とし、芸術は完全な現実模写でも完全な虚構でもなく、"
            "両者の薄皮一枚の境界に成立すると主張する。"
        ),
        background="近世前期の浄瑠璃作劇における写実と劇的構成の緊張。",
        development=(
            "近世演劇論の中核理論として継承され、"
            "近代の坪内逍遙『小説神髄』、現代演劇論・映画論にまで参照される。"
        ),
        historical_context="元禄〜享保期の浄瑠璃作劇論成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/000064/files/362_22210.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("真正性", "rethinking",
                      "虚実皮膜論は「現実そのもの」でも「完全な虚構」でもなく"
                      "両者の境界に芸術的真実があるとする。"
                      "AI生成（ディープフェイク・ハルシネーション含む）の時代に、"
                      "「真と偽の間」の芸術的価値を再考する直接の参照点。",
                      "ディープフェイク、AIハルシネーションの芸術的価値"),
                     ("物語", "rethinking",
                      "物語の真正性を「事実か虚構か」の二項ではなく"
                      "「皮膜の間」に置く東アジア的範型。",
                      "AI物語生成、虚実曖昧な合成物語")],
        cross=[("PHIL", None, "fiction-truth interpenetration",
                "shared_concept",
                "虚構論・芸術哲学との接続"),
               ("PT", None, "verisimilitude / mimesis revisited",
                "parallel",
                "西欧の真実らしさ論との比較")],
    ))

    records.append(dict(
        name_ja="上田秋成雨月物語", name_en="Ueda Akinari's Ugetsu Monogatari",
        name_original="雨月物語", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "上田秋成（1734-1809）が安永5年（1776）に刊行した怪異読本。"
            "中国白話小説（『剪燈新話』『古今奇観』等）と日本古典の翻案からなる"
            "9編の短篇集。「白峯」「菊花の約」「浅茅が宿」「夢応の鯉魚」等、"
            "幽玄と写実が融合した近世怪異文学の最高傑作とされる。"
        ),
        background=(
            "近世中期の漢学・国学の教養蓄積と、中国白話小説の翻案文化、"
            "秋成個人の医学・国学・俳諧の総合的素養。"
        ),
        development=(
            "近代の泉鏡花・芥川龍之介の怪異小説、"
            "現代の幻想文学（円城塔・京極夏彦等）への原型的影響。"
        ),
        historical_context="安永・天明期の読本確立期。",
        primary_source_url="https://www.aozora.gr.jp/cards/000074/files/421_19549.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="与謝蕪村", name_en="Yosa Buson",
        name_original="與謝蕪村", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "蕪村（1716-1784）は、芭蕉中興の祖と称される天明期俳諧の中心人物。"
            "画家としても南画（文人画）の大家。「離俗論」を唱え、"
            "詩中有画・画中有詩の理念で俳諧と絵画の融合を実現した。"
            "「春の海ひねもすのたりのたりかな」等、絵画的・空間的な俳句で知られる。"
        ),
        background=(
            "天明期（1781-1789）の漢詩文・南画文化の成熟と"
            "芭蕉再評価運動。"
        ),
        development=(
            "明治期の正岡子規が万葉集とともに蕪村を再発見・再評価し、"
            "近代俳句の写生論の源泉とした。"
        ),
        historical_context="天明俳諧と文人画の融合期。",
        primary_source_url="https://www.aozora.gr.jp/cards/001246/files/49215_38317.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    records.append(dict(
        name_ja="滝沢馬琴南総里見八犬伝",
        name_en="Takizawa Bakin's Nansō Satomi Hakkenden",
        name_original="南總里見八犬傳", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "滝沢（曲亭）馬琴（1767-1848）が文化11年（1814）から天保13年（1842）まで"
            "28年かけて執筆した全98巻106冊の長編読本。"
            "犬塚信乃ら八犬士の活躍を描く勧善懲悪物語で、"
            "中国白話小説『水滸伝』を範とする近世日本最大の長編小説。"
        ),
        background=(
            "馬琴の儒学・仏教教養、中国白話小説の影響、"
            "近世後期の長編読本の成熟。"
        ),
        development=(
            "明治以降の歴史小説（曲亭→紅葉・露伴）、"
            "現代の漫画・アニメ（『犬夜叉』『はっけん』等）への直接系譜。"
        ),
        historical_context="近世後期の読本最盛期。",
        primary_source_url="https://www.aozora.gr.jp/cards/001488/files/52410_47863.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
    ))

    # ============================================================
    # E. 主要詩学・批評概念（8件）
    # ============================================================
    records.append(dict(
        name_ja="本居宣長もののあはれ",
        name_en="Motoori Norinaga's mono no aware (revaluation)",
        name_original="もののあはれ", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "本居宣長（1730-1801）が源氏物語論『紫文要領』『源氏物語玉の小櫛』"
            "（1796）で展開した美意識論。儒仏的勧善懲悪説を排し、"
            "源氏物語の本意を「もののあはれを知る」という人間的共感の感受性に置いた。"
            "近世国学による平安美学の理論的再発見。"
        ),
        background=(
            "近世儒学的源氏物語批判への反論として、"
            "宣長の古事記研究と並行して進展した古典再評価事業。"
        ),
        development=(
            "近代日本美学（岡倉天心・九鬼周造）の基礎概念となり、"
            "戦後の小林秀雄『本居宣長』、丸山眞男の宣長論まで議論が継続している。"
        ),
        historical_context="寛政期国学の古典再評価。",
        primary_source_url="https://www.aozora.gr.jp/cards/001154/files/57195_67079.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("受容", "rethinking",
                      "宣長は儒仏的解釈枠を排して源氏物語を「再読」した。"
                      "これは古典の意味を時代ごとに再発見・再構築する歴史的範例で、"
                      "AI時代の古典再解釈（LLMによる新解釈生成）の先例。",
                      "AI古典再解釈、LLMによる新読解生成"),
                     ("正典", "rethinking",
                      "宣長は儒仏正典の権威を退け源氏物語を国学的正典に据え直した。"
                      "正典の組み替えがいかに可能かを示す範例で、"
                      "AI時代の「何を正典とするか」の問いに資する。",
                      "正典の歴史的可塑性、AI時代の新しい正典")],
        cross=[("PHIL", None, "hermeneutics of classics", "shared_concept",
                "古典解釈学との接続"),
               ("PT", None, "rediscovery of classics", "parallel",
                "近世における古典再評価の比較事例")],
    ))

    records.append(dict(
        name_ja="本居宣長物語論", name_en="Motoori Norinaga's theory of monogatari",
        name_original="物語論", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "本居宣長が『紫文要領』『源氏物語玉の小櫛』で展開した物語の本質論。"
            "物語は事実記述でも教訓書でもなく、人情の機微を描いて「もののあはれ」を"
            "知らせる独自の言語芸術であるとする。物語ジャンルを倫理・歴史から"
            "自立した美的領域として定義した日本初の体系的物語論。"
        ),
        background="儒仏的勧善懲悪解釈への反論と、平安物語の本来性回復への志向。",
        development=(
            "近代の坪内逍遙『小説神髄』、田山花袋『露骨なる描写』、"
            "近代日本の私小説論にまで間接的影響を与えた。"
        ),
        historical_context="寛政期国学の物語論確立。",
        primary_source_url="https://www.aozora.gr.jp/cards/001154/files/57195_67079.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        cross=[("PT", None, "theory of fiction", "shared_concept",
                "西欧フィクション論との比較対象")],
    ))

    records.append(dict(
        name_ja="国学", name_en="kokugaku (Native Studies)",
        name_original="國學", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世中後期に成立した日本古典・古道の学問運動。"
            "契沖（1640-1701）の万葉実証研究に始まり、"
            "荷田春満・賀茂真淵・本居宣長・平田篤胤の四大人を経て、"
            "古事記・万葉集・源氏物語等の古典を儒仏的解釈枠から解放し、"
            "「やまとごころ」（日本固有の心）の探究を志した。"
        ),
        background=(
            "近世儒学の体制化への反動と、契沖以来の文献実証主義の発達、"
            "庶民層への学問浸透。"
        ),
        development=(
            "明治維新の思想的基盤の一翼となり、近代日本の国文学・国語学・"
            "民俗学（柳田國男）の根本に継承された。"
        ),
        historical_context="近世中後期の知の自立化運動。",
        primary_source_url="https://www.aozora.gr.jp/cards/001154/files/57195_67079.html",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("正典", "partial",
                      "国学は「外来」（漢籍・仏典）を排し「自国固有」の正典を"
                      "再構築する事業で、AI時代の「学習データの自国性／グローバル性」"
                      "という問いの歴史的範例。",
                      "AI学習データのナショナリズム、自国コーパス重視論")],
        cross=[("PHIL", None, "philological nationalism", "shared_concept",
                "東アジア・西欧の文献学的ナショナリズム比較"),
               ("AN", None, "indigenous knowledge revival", "parallel",
                "先住民知識復興運動との比較対象")],
    ))

    records.append(dict(
        name_ja="蕪村離俗論", name_en="Buson's rizoku-ron (theory of departing from the vulgar)",
        name_original="離俗論", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "与謝蕪村が天明期俳諧で唱えた美学理念。「俗を離るる」ことを"
            "俳諧の根本に置き、漢詩・南画の文人精神を取り込んで"
            "日常的低俗を超えた芸術的高雅を追求した。"
            "貞門・談林の通俗性と芭蕉の禅的枯淡の中間に位置する独自の俳諧美学。"
        ),
        background="天明期の漢詩文・南画文化の隆盛と、芭蕉中興運動の精神化。",
        development=(
            "明治の正岡子規の蕪村再評価で近代俳論の主軸となり、"
            "現代俳句における芸術派系譜（飯田蛇笏・水原秋桜子等）の源流となった。"
        ),
        historical_context="天明俳諧の文人化。",
        primary_source_url="https://www.aozora.gr.jp/cards/001246/files/49215_38317.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="山東京伝うがち", name_en="Santō Kyōden's ugachi (penetration of social truths)",
        name_original="うがち", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "山東京伝（1761-1816）が黄表紙・洒落本で展開した戯作美学の中核概念。"
            "「うがつ」（穿つ）は表面に現れない人間心理・社会的真実を"
            "鋭く言い当てる機知で、江戸戯作の知的遊戯性の中心を成す。"
            "『江戸生艶気樺焼』『通言総籬』に典型的に表現される。"
        ),
        background="安永・天明期江戸町人の知的遊戯文化と機知文芸の発達。",
        development=(
            "寛政の改革による弾圧後も江戸戯作の根本美学として継承され、"
            "近代の落語・川柳・サラリーマン文学の機知系譜に流入した。"
        ),
        historical_context="安永・天明期江戸戯作の機知文化。",
        primary_source_url="https://www.aozora.gr.jp/cards/000308/files/2364_22013.html",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="黄表紙うがち", name_en="kibyōshi ugachi (satirical penetration in yellow-cover comics)",
        name_original="黄表紙うがち", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "黄表紙ジャンル全般における「うがち」の特化的展開。"
            "個別作家の創意を超えてジャンル全体の様式となった社会風刺・心理穿鑿の手法。"
            "幕府権力・武家階級・遊里慣習・流行風俗を、"
            "絵と文の遊戯的表現で批評する江戸独特の風刺文化。"
        ),
        background="江戸の出版規制との緊張下での寓意的批評の発達。",
        development=(
            "寛政の改革で衰退するが、合巻・人情本・落語に変容して継承され、"
            "現代の風刺漫画・パロディ文化の系譜となる。"
        ),
        historical_context="安永・天明期江戸の風刺文化。",
        primary_source_url="https://www.nijl.ac.jp/pages/database/",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="近世歌謡", name_en="kinsei kayō (early modern popular songs)",
        name_original="近世歌謠", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "近世初期〜中期に流行した俗謡・流行歌の総称。"
            "高三隆達の隆達節（16世紀末-17世紀初）、上方の小唄・端唄、"
            "江戸の端唄・都々逸等を含む。庶民の口頭歌謡が"
            "近世印刷文化と接続して文芸化された独自の領域。"
        ),
        background="近世初期の都市文化形成と俗謡の商業化。",
        development=(
            "近代の流行歌・新民謡運動・現代J-POPの口頭歌謡系譜の起源と位置づけられる。"
        ),
        historical_context="近世初〜中期の都市庶民歌謡。",
        primary_source_url="https://dl.ndl.go.jp/info:ndljp/pid/892906",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
    ))

    records.append(dict(
        name_ja="江戸戯作の自己言及性",
        name_en="self-referentiality in Edo gesaku",
        name_original="戲作自己言及性", original_script="japanese",
        period_id=P_KINSEI,
        definition=(
            "江戸戯作（特に黄表紙・滑稽本）に頻出するメタフィクション的"
            "自己言及性。作者・登場人物・読者の境界を意図的に攪乱し、"
            "「これは戯作である」と作中で明示する自己卑下・自己批評の修辞。"
            "山東京伝・式亭三馬・十返舎一九『東海道中膝栗毛』等に典型的。"
        ),
        background="戯作者の自己卑下修辞と読者との共犯的読書文化。",
        development=(
            "近代の夏目漱石『吾輩は猫である』の自己言及、"
            "戦後のメタフィクション（筒井康隆・後藤明生）に系譜的に継承された。"
        ),
        historical_context="近世後期戯作のメタ的成熟。",
        primary_source_url="https://www.aozora.gr.jp/cards/000308/files/2364_22013.html",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("作者性", "partial",
                      "江戸戯作の自己言及性は「これは作り物だ」と作中で宣言する"
                      "メタフィクションで、AI生成コンテンツが「自分はAI生成である」と"
                      "自己開示すべきかという問題の歴史的範例。",
                      "AIコンテンツの自己開示、メタAIフィクション")],
        cross=[("PT", None, "metafiction", "parallel",
                "西欧メタフィクション論との比較対象")],
    ))

    return records


# ----------------------------------------------------------------
# main
# ----------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("LIT-DB Phase 2 Wave 7 C17: 日本古典文学（中世〜近世）40概念")
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
                # 中世内系譜
                ("無常観", "軍記物語", "exemplifies",
                 "軍記物語は無常観を主題的に展開する代表ジャンル"),
                ("連歌", "発句（連歌）", "contains",
                 "連歌の最初の句が発句"),
                ("連歌", "連歌の付合論", "contains",
                 "付合論は連歌の核心理論"),
                ("二条良基連歌論", "連歌の付合論", "contains",
                 "良基連歌論が付合論の理論的基礎を提供"),
                ("二条良基連歌論", "心敬ささめごと", "precedes",
                 "良基の連歌論が心敬の連歌論の前提"),
                ("心敬ささめごと", "心敬の冷えさび", "contains",
                 "ささめごとは冷えさび美学を展開する書"),
                ("世阿弥風姿花伝", "世阿弥幽玄", "contains",
                 "風姿花伝は幽玄論の中核典拠"),
                ("世阿弥風姿花伝", "世阿弥物まね", "contains",
                 "風姿花伝は物まね論の中核典拠"),
                ("能（夢幻能）", "世阿弥風姿花伝", "exemplifies",
                 "夢幻能は風姿花伝の理論を体現する形式"),
                # 中世から近世への発展
                ("連歌", "俳諧連歌", "precedes",
                 "正統連歌から俳諧連歌が分岐"),
                ("発句（連歌）", "俳諧連歌", "precedes",
                 "発句が俳諧連歌の核を形成"),
                ("俳諧連歌", "俳句独立", "precedes",
                 "俳諧連歌の発句が後の俳句独立の母胎"),
                ("心敬の冷えさび", "芭蕉さびしおり", "precedes",
                 "心敬の冷えさび美学が芭蕉のさびしおりに直接系譜"),
                ("世阿弥幽玄", "芭蕉さびしおり", "precedes",
                 "幽玄美学が俳諧美学に継承"),
                # 近世内系譜
                ("俳諧連歌", "松尾芭蕉不易流行", "precedes",
                 "蕉風俳諧の中核理念として不易流行が成立"),
                ("松尾芭蕉不易流行", "芭蕉さびしおり", "contains",
                 "不易流行体系の中にさびしおり概念が位置"),
                ("松尾芭蕉不易流行", "芭蕉軽み", "extends",
                 "晩年の軽みは不易流行の到達点"),
                ("芭蕉さびしおり", "蕪村離俗論", "precedes",
                 "芭蕉のさびしおりが蕪村の離俗論に発展"),
                ("与謝蕪村", "蕪村離俗論", "exemplifies",
                 "蕪村の俳諧が離俗論を体現"),
                # 浮世草子系譜
                ("浮世草子", "井原西鶴浮世", "exemplifies",
                 "西鶴の浮世概念が浮世草子の世界観の核"),
                ("浮世草子", "黄表紙", "precedes",
                 "上方浮世草子から江戸黄表紙への展開"),
                ("黄表紙", "戯作", "contains",
                 "黄表紙は戯作の主要ジャンル"),
                ("黄表紙", "黄表紙うがち", "contains",
                 "黄表紙のうがちはジャンル全体の特徴"),
                ("山東京伝うがち", "黄表紙うがち", "exemplifies",
                 "京伝のうがちが黄表紙の特徴美学を体現"),
                ("黄表紙", "読本", "precedes",
                 "黄表紙弾圧後の真面目な小説への需要が読本を生む"),
                ("読本", "上田秋成雨月物語", "contains",
                 "雨月物語は前期読本の代表"),
                ("読本", "滝沢馬琴南総里見八犬伝", "contains",
                 "八犬伝は後期読本の代表"),
                # 演劇系譜
                ("浄瑠璃", "歌舞伎", "precedes",
                 "浄瑠璃の名作が歌舞伎に多数移入"),
                ("近松門左衛門虚実皮膜論", "浄瑠璃", "exemplifies",
                 "近松の虚実皮膜論が浄瑠璃作劇の核"),
                # 国学系譜
                ("国学", "本居宣長もののあはれ", "contains",
                 "宣長のもののあはれ論は国学の中核成果"),
                ("国学", "本居宣長物語論", "contains",
                 "宣長の物語論は国学の文学論部門"),
                ("本居宣長物語論", "本居宣長もののあはれ", "extends",
                 "物語論の核心としてもののあはれが据えられた"),
                # ジャンル発展
                ("中世説話文学", "御伽草子", "precedes",
                 "中世説話の伝統が御伽草子の母胎"),
                ("御伽草子", "浮世草子", "precedes",
                 "御伽草子の絵入り物語伝統が浮世草子に継承"),
                ("戯作", "江戸戯作の自己言及性", "contains",
                 "自己言及性は江戸戯作の特徴的美学"),
                # 漢学系譜
                ("五山文学", "国学", "precedes",
                 "五山文学の漢学伝統が近世儒学を経て国学反動を生む"),
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
                    source_evidence="日本古典文学史標準的記述（中世・近世）",
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
        print(f"importance_score distribution (subfield 10): "
              f"{[dict(r) for r in rows]}")

        # 第四変容タグ
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM fourth_transform_tags t "
            "JOIN concepts c ON t.concept_id=c.id WHERE c.subfield_id=10"
        ).fetchone()
        print(f"fourth_transform_tags (subfield 10): {row['c']}")

        # cross_domain
        row = db.conn.execute(
            "SELECT COUNT(*) AS c FROM cross_domain x "
            "JOIN concepts c ON x.lit_entity_id=c.id "
            "WHERE x.lit_entity_type='concept' AND c.subfield_id=10"
        ).fetchone()
        print(f"cross_domain links (subfield 10): {row['c']}")


if __name__ == "__main__":
    main()
