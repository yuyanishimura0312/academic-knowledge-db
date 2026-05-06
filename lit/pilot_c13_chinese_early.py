"""
LIT-DB Phase 2 Pilot: C13 — 中国古典文学（先秦〜唐）50概念投入スクリプト

主パターン: P1 (Canonical Primary Pursuit)
subfield_id=8 (lit_cn_classical), region='東アジア'

構成:
- 詩歌ジャンル/形式: 10件
- 詩論概念: 10件
- 主題/世界観: 10件
- 主要詩派/集団 (movements): 10件
- メタ文学/批評概念: 10件

第四変容タグは詩論・批評概念を中心に付与する。
西欧概念との対比は cross_domain (target_db='PT') で記録する。

使用法:
    python3 pilot_c13_chinese_early.py
"""

from __future__ import annotations

from lit_db_helper import LitDB


# ----------------------------------------------------------------
# 期間（先秦〜唐）の用意
# ----------------------------------------------------------------

def setup_periods(db: LitDB) -> dict:
    """先秦〜唐の主要時代区分を get_or_create する。"""
    periods = {}
    periods["先秦"] = db.get_or_create_period(
        name_ja="先秦", name_en="Pre-Qin",
        region="東アジア", start_year=-1100, end_year=-221,
        description="周代から戦国末期まで。詩経・楚辞の成立期。",
    )
    periods["漢"] = db.get_or_create_period(
        name_ja="漢", name_en="Han",
        region="東アジア", start_year=-206, end_year=220,
        description="前漢・後漢。楽府・古詩・賦の発展期。",
    )
    periods["魏晋南北朝"] = db.get_or_create_period(
        name_ja="魏晋南北朝", name_en="Wei-Jin-Northern-Southern",
        region="東アジア", start_year=220, end_year=589,
        description="建安文学・玄学・山水詩・声律論の成立期。",
    )
    periods["唐"] = db.get_or_create_period(
        name_ja="唐", name_en="Tang",
        region="東アジア", start_year=618, end_year=907,
        description="近体詩成立、李杜王孟韓白等が活躍した中国詩の最盛期。",
    )
    return periods


# ----------------------------------------------------------------
# 50概念データ定義
# ----------------------------------------------------------------

def build_concept_records(periods: dict) -> list[dict]:
    """50概念のレコードリストを構築する。
    各レコードは insert_concept のkwargs相当。
    'fourth_tags' は別キーで保持し、後段で tag_fourth_transform を呼ぶ。
    'cross' は cross_domain 用。
    """
    P_QIN = periods["先秦"]
    P_HAN = periods["漢"]
    P_WJ = periods["魏晋南北朝"]
    P_TANG = periods["唐"]

    records: list[dict] = []

    # ============================================================
    # A. 詩歌ジャンル/形式（10件）
    # ============================================================
    records.append(dict(
        name_ja="風雅頌", name_en="feng ya song (Airs, Odes, Hymns)",
        name_original="風雅頌", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "『詩経』を構成する三大区分。「風」は十五国風（地方民謡）、"
            "「雅」は大雅・小雅（朝廷の宴会・政教の歌）、「頌」は周頌・魯頌・商頌"
            "（祖先・神霊への祭祀歌）を指す。詩を社会階層と機能で類別する最古の体系として、"
            "後世の詩論（賦比興と並ぶ「六義」の前三義）の基礎となった。"
        ),
        background="周代の宮廷および諸侯国で歌われた歌謡を孔子が編纂したと伝えられる。",
        development="毛詩序により儒教的詩教論と結合し、東アジア詩学の正典的枠組みとなった。",
        historical_context="周王朝の祭祀・宴会・採詩制度に由来する古代歌謡の分類。",
        primary_source_url="https://ctext.org/book-of-poetry",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="楚辞体", name_en="chuci style (Songs of Chu)",
        name_original="楚辭體", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "戦国末期の楚国で屈原・宋玉らによって創出された南方系の詩体。"
            "句末の「兮（けい）」を特徴とする長句のリズム、シャーマニズム的想像力、"
            "個人的悲憤の表出を持ち、北方『詩経』の四言体と対をなす。"
            "後の漢賦の母体となり、屈原『離騒』が代表作。"
        ),
        background="楚地方の祭祀歌・巫覡文化を背景に、屈原の政治的失脚と結びついて文学化した。",
        development="漢代の賦体に直接継承され、後世「騒体」「楚騒」として詩史の二大源流の一翼を担う。",
        historical_context="戦国末期、楚の懐王・頃襄王の時代の政治抗争と亡命体験。",
        primary_source_url="https://ctext.org/chu-ci",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="楽府", name_en="yuefu (Music Bureau poetry)",
        name_original="樂府", original_script="kanji",
        period_id=P_HAN,
        definition=(
            "漢の武帝が設立した音楽官署「楽府」で採集・制作された歌曲、"
            "およびその歌辞形式を踏襲した後世の詩。民間歌謡・宮廷雅楽・"
            "外来音楽を含み、五言詩成立の母胎となった。後世「新楽府」（白居易ら）"
            "として社会批評の媒体となる。"
        ),
        background="武帝の音楽行政改革と民間採詩の伝統が結合して成立。",
        development="魏晋の文人楽府・南朝民歌・唐の新楽府運動へ展開した。",
        historical_context="前漢中期の中央集権体制下における音楽・祭祀の整備。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=748277",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="古詩十九首", name_en="Nineteen Old Poems",
        name_original="古詩十九首", original_script="kanji",
        period_id=P_HAN,
        definition=(
            "『文選』巻二十九に収録される作者不詳の五言古詩十九篇。"
            "後漢末の文人によると推定され、人生無常・離別・思婦の主題を"
            "簡潔で深遠な五言で歌う。五言詩の成立を示す画期的作品群とされ、"
            "鍾嶸『詩品』は「驚心動魄、一字千金」と絶賛した。"
        ),
        background="楽府民歌から文人五言詩への移行期に位置する匿名作品群。",
        development="建安詩人・陶淵明・唐詩の五言古詩の規範となった。",
        historical_context="後漢末の社会動揺と文人の個人的内省の深化。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("作者性", "rethinking",
                      "古詩十九首は作者不詳のまま千年以上正典として享受された。"
                      "個別作者の同定なしに「驚心動魄」と評価された事実は、"
                      "近代以降のロマン主義的作者性概念とも、AI時代の生成テキストとも対比的に再考できる。",
                      "AI生成テキストの匿名性・作者性帰属問題、米国著作権局のAI作品判断")],
    ))

    records.append(dict(
        name_ja="近体詩", name_en="jintishi (regulated verse)",
        name_original="近體詩", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "唐代に完成した平仄・対句・押韻の規則に基づく定型詩の総称。"
            "古体詩に対する語で、絶句（四句）・律詩（八句）・排律を含む。"
            "沈佺期・宋之問らによって確立、王維・李白・杜甫らによって"
            "美学的極致に達した。"
        ),
        background="斉梁の声律論（永明体）が唐初に整備され、科挙制度と結びついて規範化。",
        development="宋以降、近体は士大夫の必須教養となり、東アジア漢字文化圏全体の詩の規範となる。",
        historical_context="初唐期の科挙詩賦試の制度化と宮廷詩文化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="絶句", name_en="jueju (quatrain)",
        name_original="絕句", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "近体詩の一形式で、五言または七言・四句からなる短詩。"
            "起承転結の構造と平仄・押韻の規則を持つ。短小ながら意境を"
            "凝縮させる詩体として、王維・李白・王昌齢らに名作が多い。"
        ),
        background="南朝楽府民歌や六朝の小詩から発展し、唐代に定型化。",
        development="宋詞・元曲を経て日本の漢詩・俳句の凝縮美にも影響を与えた。",
        historical_context="唐代の宴席・送別・即興吟詠の文化的需要。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="律詩", name_en="lüshi (regulated octave)",
        name_original="律詩", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "近体詩の中心形式。五言または七言・八句からなり、第三・四句"
            "（頷聯）と第五・六句（頸聯）が対句となる。平仄・押韻・粘対の"
            "厳格な規則を持つ。杜甫が完成度の高峰とされる。"
        ),
        background="斉梁の声律論を承け、初唐に沈佺期・宋之問らが定型化。",
        development="科挙の試詩として千年以上規範性を保ち、東アジアの漢詩文化の中心となった。",
        historical_context="科挙制度における詩賦試の標準体裁。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="歌行体", name_en="gexing (song-style verse)",
        name_original="歌行體", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "古体詩の一種で、楽府由来の自由な句長と韻の転換を許す長篇詩体。"
            "「歌」「行」「吟」「引」等を題に冠することが多い。叙事的・抒情的"
            "情感を奔放に展開できる体裁として、白居易『長恨歌』『琵琶行』、"
            "李白『将進酒』が代表作。"
        ),
        background="漢魏の楽府古辞から発展し、初唐に文人詩体として確立。",
        development="宋元の歌行・明清の長篇叙事詩へと継承された。",
        historical_context="唐代社会の物語的需要と楽府民歌の文人化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=748277",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="賦", name_en="fu (rhapsody / rhyme-prose)",
        name_original="賦", original_script="kanji",
        period_id=P_HAN,
        definition=(
            "韻文と散文の中間に位置する文学形式。司馬相如・揚雄らによって漢代に"
            "大成された大賦は宮廷の壮麗を讃える長篇叙事的修辞、後の小賦・抒情賦"
            "は個人感情を歌う。「鋪陳其事而直言之（事を鋪陳して直に言う）」と"
            "『詩経』の賦比興にも通じる修辞概念でもある。"
        ),
        background="楚辞の長句修辞と戦国諸子の対問体が結合して成立。",
        development="魏晋の抒情小賦、唐宋の律賦・文賦へと変容しつつ千余年継続。",
        historical_context="漢帝国の宮廷文化と修辞の制度化。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="駢文", name_en="pianwen (parallel prose)",
        name_original="駢文", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "対句・四六調・典故を多用する華麗な散文文体。「駢儷文」「四六文」"
            "とも呼ばれる。六朝期に大成され、唐初の四傑（王勃・楊炯ら）が極致を"
            "示した。中唐の韓愈・柳宗元による「古文運動」の批判対象となる。"
        ),
        background="魏晋の声律論と修辞主義が散文に及び、対偶を絶対化した文体。",
        development="唐宋の古文運動により位置を低下させたが、四六文として実用文に残存。",
        historical_context="六朝貴族社会の修辞主義と科挙制成立期の試文化。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    # ============================================================
    # B. 詩論概念（10件）
    # ============================================================
    records.append(dict(
        name_ja="風骨", name_en="fenggu (wind and bone / vigorous spirit)",
        name_original="風骨", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "劉勰『文心雕龍』風骨篇および鍾嶸『詩品』に現れる中核的詩論概念。"
            "「風」は感化力ある気韻、「骨」は文辞の骨格・力強さを指し、"
            "両者を兼備した剛健な美質を理想とする。建安文学の力強い気概を範とし、"
            "後の唐代盛唐詩の雄渾な美意識に継承された。"
        ),
        background="魏晋玄学の気の思想と建安七子の力強い詩風から抽出された美的範疇。",
        development="陳子昂の「漢魏風骨」呼号、盛唐詩の雄渾美の規範となった。",
        historical_context="六朝後期の柔靡な文風への反省として理論化された。",
        primary_source_url="https://ctext.org/wenxin-diaolong/feng-gu",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "partial",
                      "風骨は気の流動性に基づく作家の人格的・身体的なエネルギーが文辞に貫通する概念で、"
                      "AI生成テキストには「骨」は模倣可能でも「風」（生きた気の感化力）は原理的に欠落するという"
                      "対比構造が成立する。中国古典美学の身体性と機械的生成の差異を浮かび上がらせる。",
                      "LLMによる文体模倣と「身体的気韻」の不在、AI作詩の評価基準論争")],
        cross=[("PT", None, "fenggu", "shared_concept",
                "Poetics DBの作家のエネルギー・力動的美学概念と並行する東アジア美学範疇")],
    ))

    records.append(dict(
        name_ja="気韻", name_en="qiyun (resonance of vital breath)",
        name_original="氣韻", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "「気」（生命的エネルギー）と「韻」（余韻・響き）の結合。"
            "もとは謝赫『古画品録』の「気韻生動」（六法の第一）として絵画論で"
            "提唱されたが、詩文論にも援用され、作品全体に通底する生気と余韻を"
            "指す。技巧の巧拙を超えた精神性の美を表現する。"
        ),
        background="魏晋玄学の気の思想と人物批評の風韻概念が美術理論に結晶した。",
        development="唐宋の詩画論で中心概念となり、日本の幽玄・風雅にも影響した。",
        historical_context="六朝の人物品藻と絵画批評の交叉。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=80596",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "気韻は作品に流れる生命的エネルギーであり、作家の身体・呼吸・生命と不可分とされる。"
                      "AIには気がないという中国古典美学の前提が、AI生成作品の本質的限界を問う観点を提供する。",
                      "LLM出力における「死んだ言葉」批判、生成AIと身体性の哲学")],
        cross=[("PT", None, "qiyun", "shared_concept", "詩文・絵画に通底する東アジア美学概念")],
    ))

    records.append(dict(
        name_ja="興", name_en="xing (evocation / stirring)",
        name_original="興", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "『詩経』の修辞法「賦比興」の一つ。先に他の事物（自然・景物）を"
            "引いて読者の情感を呼び起こし、本題を導入する技法。「先言他物以引起所詠之詞」"
            "（朱熹）と定義される。象徴・連想・比喩を含み、漢字文化圏の詩学の中核技法。"
        ),
        background="毛詩注釈学において賦・比と並ぶ第三の修辞法として理論化。",
        development="漢代の鄭玄、宋代の朱熹が定義を精緻化。日本の和歌の序詞・枕詞にも対応。",
        historical_context="周代の歌謡における自然と人事の連想的結合の伝統。",
        primary_source_url="https://ctext.org/book-of-poetry",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PT", None, "xing", "shared_concept",
                "Poetics DBのevocation/figura/imageと並行する東アジア固有の連想的修辞")],
    ))

    records.append(dict(
        name_ja="比", name_en="bi (analogy / comparison)",
        name_original="比", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "賦比興の第二。「以彼物比此物（彼の物を以て此の物に比す）」（朱熹）"
            "と定義される直接的比喩・寓意の技法。興がさりげない連想を伴うのに対し、"
            "比は明示的な対応関係を提示する。後世の寓言・比興詩の基礎となる。"
        ),
        background="毛詩鄭箋以来の伝統的解釈学的範疇。",
        development="後世の比興詩・寓言詩・諷喩詩の理論的支柱。",
        historical_context="周代歌謡の比喩的表現の体系化。",
        primary_source_url="https://ctext.org/book-of-poetry",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("PT", None, "bi", "shared_concept",
                "Poetics DBのsimile/analogyに対応する東アジア修辞範疇")],
    ))

    records.append(dict(
        name_ja="賦（修辞法）", name_en="fu (direct exposition as figure)",
        name_original="賦", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "賦比興の第一。「敷陳其事而直言之者也（其の事を敷陳し直に之を言う者なり）」"
            "（朱熹）。事物を直接的に列挙・描写する修辞法で、興・比に対し直接表現を指す。"
            "後の文学ジャンル「賦」の語源でもあり、詩経の修辞法と漢代の文学体裁が"
            "同名で結ばれる稀有な例。"
        ),
        background="毛詩注釈の三義として理論化された伝統的修辞範疇。",
        development="漢賦の長篇叙事修辞へと展開し、ジャンル名に転じた。",
        historical_context="周代詩経の直接描写の伝統。",
        primary_source_url="https://ctext.org/book-of-poetry",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="神思", name_en="shensi (spiritual / divine thought)",
        name_original="神思", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "劉勰『文心雕龍』神思篇に展開される創作心理論の中核概念。"
            "創作時に作家の精神（神）が時空を超えて自由に飛翔し、万象と感応する状態を指す。"
            "「文之思也、其神遠矣。故寂然凝慮、思接千載；悄焉動容、視通萬里」と説かれる。"
        ),
        background="魏晋玄学の「無」「虚静」の思想と修辞論が結合して成立。",
        development="後の唐宋詩論における「興会」「霊感」「妙悟」概念の源流となった。",
        historical_context="六朝後期の創作論・芸術論の理論的成熟。",
        primary_source_url="https://ctext.org/wenxin-diaolong/shen-si",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "神思は創作主体の精神が万象と感応し時空を超えて飛翔する「天人合一」的創造性概念であり、"
                      "個別主体の独創性に立脚する西欧ロマン主義とも、訓練データの統計的再構成であるLLMとも"
                      "本質的に異なる第三の創造性モデルを提示する。AI時代の創造性論争に新たな比較軸を与える。",
                      "LLMの「創造性」をめぐる哲学的論争、東アジア美学からのAI批評"),
                     ("主体", "rethinking",
                      "神思の主体は個我ではなく、虚静によって万象と感応する開かれた精神である。"
                      "デカルト的cogitoとも、AIの「主体なき発話」とも異なるモデルとして再考対象となる。",
                      "AIエージェントの主体性論争、ポストヒューマン主体論")],
        cross=[("PHIL", None, "shensi", "shared_concept",
                "創作心理・精神現象学の東アジア概念")],
    ))

    records.append(dict(
        name_ja="滋味", name_en="ziwei (savor / aesthetic flavor)",
        name_original="滋味", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "鍾嶸『詩品』序に提示される詩の美的評価概念。「五言居文詞之要、是衆作之有滋味者也」"
            "として、五言詩は「滋味」（噛みしめるほどに出てくる美的快感）を持つ点で他形式より"
            "優れるとした。後の唐宋詩論の「味外之味」「韻外之致」（司空図）に継承される。"
        ),
        background="味覚を芸術評価に転用する六朝美学の特徴的修辞。",
        development="司空図『二十四詩品』の「韻外之致、味外之旨」に直接継承される。",
        historical_context="六朝の品藻文化と美学的精緻化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("PT", None, "ziwei", "shared_concept",
                "Poetics DBのaesthetic flavor/savor概念に対応")],
    ))

    records.append(dict(
        name_ja="含蓄", name_en="hanxu (suggestiveness / implicit reserve)",
        name_original="含蓄", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "言外に深意を蓄え、明言せずに余情を残す美学。司空図『二十四詩品』含蓄品で"
            "「不著一字、尽得風流（一字をも著けずして、風流を尽く得たり）」と表現された。"
            "唐代以降の中国詩学の中核的審美規範となり、日本の「言わぬが花」にも通じる。"
        ),
        background="老荘の「大音希声」「言不尽意」の思想を美学に転用。",
        development="宋代厳羽『滄浪詩話』、清代王士禛の「神韻説」に継承された。",
        historical_context="中唐期の詩美学における言語と意の関係への深化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=752088",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("言語", "rethinking",
                      "含蓄は意を言葉の外に置く東アジア美学の核心であり、"
                      "言葉の明示性・冗長性を志向する生成AIテキストとは原理的に対立する。"
                      "「言わない」ことの美学はAI時代の言語哲学を再考する重要な参照点となる。",
                      "LLM出力の冗長性問題、明示性vs余白の言語観")],
        cross=[("PT", None, "hanxu", "shared_concept",
                "Poetics DBのsuggestiveness/implicit meaning概念に対応")],
    ))

    records.append(dict(
        name_ja="意境", name_en="yijing (poetic realm / artistic conception)",
        name_original="意境", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "「意」（情感・思想）と「境」（情景・環境）が融合した詩的世界を指す美学概念。"
            "唐代の王昌齡『詩格』に「物境・情境・意境」の三境説が提示され、後に詩学の中心範疇となる。"
            "情景交融・虚実相生を要件とし、東アジア詩学の独自概念として知られる。"
        ),
        background="仏教の「境」（境界）概念と中国詩学の「情景」論が結合。",
        development="王国維『人間詞話』により近代美学範疇として再定式化された。",
        historical_context="唐代詩格類における詩学の理論化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("創造性", "rethinking",
                      "意境は作家・作品・読者・自然が融合する開かれた詩的場であり、"
                      "個別作品の所有的創造性とも、AI生成の閉じた出力とも異なる関係的創造性モデルを示す。",
                      "AI時代の関係的・場所的創造性論")],
        cross=[("PT", None, "yijing", "shared_concept",
                "Poetics DBのpoetic world/artistic conceptionに対応する東アジア固有概念")],
    ))

    records.append(dict(
        name_ja="境界（王国維）", name_en="jingjie (state / poetic state)",
        name_original="境界", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "唐代詩学に発し、近代王国維『人間詞話』で結晶した美学範疇。"
            "「有境界則自成高格、自有名句」とされ、作品が独自の詩的世界を立ち上げているか"
            "を問う基準。本DBでは唐代由来の詩境概念として採録する。「有我之境」「無我之境」"
            "の区別が後代に展開された。"
        ),
        background="意境論および仏教境界概念の美学的洗練。",
        development="王国維により近代中国美学の中心概念に昇格、現代中国文学批評にも継承。",
        historical_context="唐から清末にいたる詩境論の蓄積。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    # ============================================================
    # C. 主題/世界観（10件）
    # ============================================================
    records.append(dict(
        name_ja="隠逸", name_en="yinyi (reclusion / hermitism)",
        name_original="隱逸", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "世俗・官界を離れ山林に身を隠す生き方、およびそれを主題とする文学。"
            "陶淵明『帰去来兮辞』『飲酒』連作が代表で、儒家の出処進退論と道家の自然志向が結合した"
            "東アジア独自の文学的世界観。後世の山水田園詩・閑適文学の母胎となる。"
        ),
        background="老荘思想・玄学・乱世における政治回避の実践が結合。",
        development="王維・孟浩然の山水詩、宋代の隠逸文人画、日本の隠者文学に継承された。",
        historical_context="魏晋南北朝の政治的混乱と玄学・仏教の流行。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89568",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="出処", name_en="chuchu (advance and withdrawal)",
        name_original="出處", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "「出（仕官）」と「処（隠退）」の選択に関わる士人の根本的倫理問題。"
            "孔子『論語』に「邦有道則仕、邦無道則可巻而懐之」と説かれ、"
            "孟子・荀子で展開された後、文学の中心主題となる。陶淵明・杜甫・"
            "蘇軾の作品の核心にこの主題がある。"
        ),
        background="儒家倫理学の士人論として体系化。",
        development="後世の士大夫文学全体を貫く倫理的・実存的主題となった。",
        historical_context="春秋戦国期の士人の役割定立。",
        primary_source_url="https://ctext.org/analects",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="志道", name_en="zhidao (commitment to the Way)",
        name_original="志道", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "孔子『論語』里仁篇「士志於道」に発する士人の精神的志向。"
            "詩は志を言うものであるとする「詩言志」（『書経』堯典）と結合し、"
            "詩を倫理的・政治的志向の表現とする中国詩学の根本姿勢を形成した。"
        ),
        background="儒家倫理学の根本命題として『論語』『書経』に明示。",
        development="毛詩序の「在心為志、発言為詩」を経て、唐宋古文運動の「文以載道」に展開。",
        historical_context="春秋戦国期の士人理念の形成。",
        primary_source_url="https://ctext.org/analects",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="遊仙", name_en="youxian (wandering immortals)",
        name_original="遊仙", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "仙界を遊歴し神仙と交わる幻想的詩境を主題とする詩のジャンル。"
            "曹植『遊仙詩』、郭璞『遊仙詩』が代表的で、楚辞『遠遊』を遠源とする。"
            "現実逃避・道教信仰・哲学的思索が交錯する六朝独自の幻想文学。"
        ),
        background="楚辞の巫覡的飛翔、道教の神仙思想、玄学の超越志向が結合。",
        development="李白の遊仙詩、唐代道教詩、明清の幻想小説に継承された。",
        historical_context="魏晋南北朝の政治的混乱と道教の流行。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="山水", name_en="shanshui (mountains-and-rivers / landscape)",
        name_original="山水", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "自然景観そのものを主題とする詩風。謝霊運を祖、王維・孟浩然を高峰とする。"
            "玄学的自然観・仏教の境地観・隠逸思想が結合し、「澄懐観道」（宗炳）の理念のもとに"
            "純粋に景観を描く文学的伝統を確立した。"
        ),
        background="六朝の老荘・玄学・仏教の自然観が文学化した。",
        development="盛唐の王孟詩派が様式美を完成し、宋代の山水詩・山水画と一体化した。",
        historical_context="東晋南朝の貴族文化と江南の山水景観。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="田園", name_en="tianyuan (fields-and-gardens / pastoral)",
        name_original="田園", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "農村・田畑・庭園での自得的生活を主題とする詩風。陶淵明を祖とし、"
            "王維・孟浩然・儲光羲ら盛唐の田園山水詩派に継承された。山水詩が壮大な自然を"
            "対象とするのに対し、田園詩は人事と接した日常的自然を対象とする。"
        ),
        background="陶淵明の隠逸生活実践と詩作が原型を確立。",
        development="盛唐田園山水詩、宋代范成大の田園雑興、日本の田園詩へ展開。",
        historical_context="東晋末の士人の隠退と農的生活の理想化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89568",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="閨怨", name_en="guiyuan (boudoir lament)",
        name_original="閨怨", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "夫や恋人と離別した女性の閨房での孤独と恨みを歌う詩のジャンル。"
            "六朝楽府民歌に源流があり、唐代に王昌齢『閨怨』をはじめ盛行した。"
            "男性詩人による女性視点の代弁という擬作形式が特徴で、後世の代言体・閨秀詩学の基礎となる。"
        ),
        background="楚辞『怨歌行』類、漢魏古詩の思婦詩を承けて成立。",
        development="宋詞の婉約派、明清の閨秀詩人の自作閨怨詩へと変容しつつ継承。",
        historical_context="唐代の征戍・宦遊文化と女性の社会的位置。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("主体", "partial",
                      "閨怨は男性詩人による女性主体の代弁という擬作構造を持ち、"
                      "「我」と「他者の声」の境界が制度化されている。"
                      "AIによる人格代弁・キャラクター生成と歴史的な代言体伝統の比較対象となる。",
                      "AI生成のキャラクター発話、代弁・憑依の主体論")],
    ))

    records.append(dict(
        name_ja="送別", name_en="songbie (farewell / parting)",
        name_original="送別", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "友人・同僚との別離を主題とする詩のジャンル。王勃『送杜少府之任蜀州』、"
            "王維『送元二使安西』、李白『送孟浩然之広陵』が代表。盛唐に名作が集中し、"
            "唐代士人の宦遊・科挙赴任文化と結びついた中国詩特有のジャンルとなる。"
        ),
        background="春秋戦国の餞別歌、漢魏の別離詩を経て唐代に独立ジャンル化。",
        development="宋詞・元曲・日本漢詩の送別詩へ継承された。",
        historical_context="唐代の科挙・任官・宦遊による地方異動の常態化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="懐古", name_en="huaigu (meditations on the past)",
        name_original="懷古", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "歴史的遺跡や過去の偉人を訪い、興亡の感慨を詠む詩のジャンル。"
            "陳子昂『登幽州台歌』、劉禹錫『金陵五題』、杜牧『赤壁』が代表。"
            "歴史哲学・無常観・詩人の自己投影が結合し、唐代に独立ジャンル化した。"
        ),
        background="楚辞『離騒』、賈誼『弔屈原賦』に源流を持つ歴史的感懐の伝統。",
        development="宋元明清を通じて懐古詠史詩は士大夫文学の中核ジャンルとなった。",
        historical_context="唐代の歴史意識・興亡観の高まり。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="忠君愛国", name_en="zhongjun aiguo (loyalty and patriotism)",
        name_original="忠君愛國", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "君主への忠と国家への愛を表現する文学的主題。屈原『離騒』を遠源、"
            "杜甫『春望』『北征』、陸游を典型とする。詩経・楚辞以来の「美刺」（褒める・諷刺する）"
            "の伝統と結合し、中国詩学の倫理的中軸を形成した。"
        ),
        background="儒家倫理と屈原の楚辞的悲憤が結合した伝統的詩主題。",
        development="宋代愛国詩・明末遺民詩・近代救国詩へ千年以上継承された。",
        historical_context="士人の政治的責任意識と詩教論の結合。",
        primary_source_url="https://ctext.org/chu-ci",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    # ============================================================
    # D. 詩派/集団 (movementsとして登録するが、概念としても機能するためconceptsに格納)
    # ============================================================
    records.append(dict(
        name_ja="建安七子", name_en="Seven Masters of Jian'an",
        name_original="建安七子", original_script="kanji",
        period_id=P_HAN,
        definition=(
            "後漢末建安年間（196-220）に活躍した文人集団。孔融・陳琳・王粲・徐幹・"
            "阮瑀・応瑒・劉楨を指す。曹氏父子（曹操・曹丕・曹植）を中心に集まり、"
            "「慷慨悲涼」の力強い気概（建安風骨）で五言詩の地位を確立した。"
        ),
        background="後漢末の戦乱と曹操の業を中心とする文人庇護政策により集団形成。",
        development="後の風骨論の理論的範例となり、唐代陳子昂が「漢魏風骨」を呼号した。",
        historical_context="後漢末三国時代の動乱と曹氏政権の文化政策。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="竹林七賢", name_en="Seven Sages of the Bamboo Grove",
        name_original="竹林七賢", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "魏晋転換期に河内山陽の竹林に集った文人グループ。阮籍・嵇康・山濤・"
            "向秀・劉伶・王戎・阮咸を指す。玄学的清談・酒・音楽・詩を交わし、"
            "礼法を超越した精神を実践した。乱世における精神的退避と独自の美学を確立。"
        ),
        background="魏晋禅代期の政治的緊張と玄学の隆盛。",
        development="後世の士人の自由・狷介な生き方の典型となり、芸術・文学に深い影響を与えた。",
        historical_context="3世紀中葉の魏晋政権交代期の思想的危機。",
        primary_source_url="https://ctext.org/shi-shuo-xin-yu",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="陶謝", name_en="Tao-Xie (Tao Yuanming and Xie Lingyun)",
        name_original="陶謝", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "東晋・南朝宋の詩人陶淵明と謝霊運の併称。陶は田園詩、謝は山水詩の祖とされ、"
            "両者をもって六朝詩の双璧とする批評慣習が唐代以降確立した。"
            "後世の隠逸・山水・田園詩学の根本範例となる。"
        ),
        background="東晋末-南朝宋の貴族文化と隠逸思想の結合。",
        development="王孟・李白・蘇軾・日本の漢詩文学等に決定的影響を残した。",
        historical_context="4-5世紀の南朝貴族社会と山水文化の発達。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89568",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="初唐四傑", name_en="Four Eminences of the Early Tang",
        name_original="初唐四傑", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "初唐期に活躍した王勃・楊炯・盧照鄰・駱賓王の四詩人の併称。"
            "六朝以来の宮廷詩風を脱し、雄渾で気骨ある新風を打ち出した。"
            "近体詩の定型化と七言歌行体の発展に大きく寄与した。"
        ),
        background="初唐宮廷詩の華靡な弊風への反発として登場。",
        development="陳子昂の漢魏風骨呼号と相まって盛唐詩の道を開いた。",
        historical_context="7世紀後半の唐帝国確立期と科挙制度整備。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="王孟", name_en="Wang-Meng (Wang Wei and Meng Haoran)",
        name_original="王孟", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "盛唐の山水田園詩派の代表詩人、王維と孟浩然の併称。"
            "陶謝の伝統を承け、自然と禅的境地を融合させた清澄な詩風で盛唐の一流派を形成した。"
            "王維は仏教的・絵画的、孟浩然は隠逸的気風を持つ。"
        ),
        background="盛唐の隠逸文化と仏教（特に禅）の流行。",
        development="後世の山水田園詩の規範、日本の漢詩・俳句美学にも影響を与えた。",
        historical_context="8世紀盛唐の安定期と仏教文化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="高岑", name_en="Gao-Cen (Gao Shi and Cen Shen) / frontier poets",
        name_original="高岑", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "盛唐の辺塞詩派の代表詩人、高適と岑参の併称。"
            "辺境の戦闘・遠征・異域風物を雄渾に歌う「辺塞詩」のジャンルを確立した。"
            "盛唐詩を王孟（山水）・李杜（雄渾抒情）と並ぶ三大潮流として彩る。"
        ),
        background="唐玄宗期の辺境拡張政策と文人の従軍経験。",
        development="後世の辺塞詩・愛国詩の源流となった。",
        historical_context="8世紀唐の対外戦争と辺境統治。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="李杜", name_en="Li-Du (Li Bai and Du Fu)",
        name_original="李杜", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "盛唐の二大詩人李白（詩仙）と杜甫（詩聖）の併称。"
            "李白は道家的奔放と歌行体の名人、杜甫は儒家的憂国と律詩の高峰として、"
            "中国詩史上最高峰を二分する。両者の併称は中唐韓愈以降の批評慣習に定着した。"
        ),
        background="盛唐期の文化的爛熟と安史の乱の動乱が両者を輩出。",
        development="千年以上にわたり中国詩の最高範例とされ、李杜優劣論争が継続した。",
        historical_context="8世紀盛唐の極盛期と安史の乱（755-763）。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="韓孟詩派", name_en="Han-Meng poetic school",
        name_original="韓孟詩派", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "中唐期に韓愈・孟郊を中心に形成された詩派。「以文為詩」（文を以て詩と為す）"
            "の方法、奇崛険怪な造語、苦吟の作法を特徴とし、平易なるを尚ぶ元白詩派と対立的に位置づけられる。"
            "李賀・賈島も近接する。"
        ),
        background="安史の乱後の中唐期、平易な詩風への対抗として奇崛な美を追求。",
        development="宋代江西詩派の「点鉄成金」「夺胎换骨」（黄庭堅）に直接的影響を与えた。",
        historical_context="9世紀初頭の中唐文化の多様化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="元白詩派", name_en="Yuan-Bai poetic school",
        name_original="元白詩派", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "中唐の元稹と白居易を中心とする詩派。「老嫗能解」（老婆も理解できる）と"
            "言われるほどの平易な言語で社会批評を行う「新楽府運動」を推進し、"
            "文学の社会的機能を重視した。韓孟詩派と双璧を成す中唐詩の二大潮流。"
        ),
        background="安史の乱後の社会矛盾を背景に、詩の社会機能を再活性化する運動。",
        development="日本の平安朝文学（『白氏文集』への深い愛好）、朝鮮漢詩へ広く影響した。",
        historical_context="9世紀初頭中唐の社会批評文学の興隆。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="苦吟派", name_en="kuyin (painstaking poets)",
        name_original="苦吟派", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "中晚唐期、賈島・姚合らを中心とする詩風で、一字一句を苦悩の末に練り上げる"
            "「苦吟」（つらい吟詠）を特徴とする。「二句三年得、一吟雙涙流（賈島）」が"
            "象徴的句。後の宋詩の精緻化や、詩作を職人的訓練と見なす伝統の源流。"
        ),
        background="中唐後の詩境拡張困難の中で、極限的言語精緻化を追求。",
        development="晚唐五律の細密美、宋代江西詩派の彫琢主義に継承された。",
        historical_context="9世紀後半中晚唐の文化的成熟と内向。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=3, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[("創造性", "rethinking",
                      "苦吟は一字一句に長年の生命を投じる手作業的創造性のモデルであり、"
                      "瞬時に大量生成するLLMとは時間性・身体性の点で対極にある。"
                      "AI時代における「苦吟」の意義の再評価が可能。",
                      "LLMによる即時大量生成、AI時代の手仕事的創造性論")],
    ))

    # ============================================================
    # E. メタ文学/批評概念（10件）
    # ============================================================
    records.append(dict(
        name_ja="言志", name_en="yanzhi (poetry expresses intent)",
        name_original="言志", original_script="kanji",
        period_id=P_QIN,
        definition=(
            "『書経』堯典「詩言志、歌永言（詩は志を言い、歌は言を永くす）」に由来する"
            "中国詩学最古の根本命題。詩を作家の「志」（思想・志向・倫理的目標）の表現と"
            "規定する伝統で、毛詩序「在心為志、発言為詩」によって体系化された。"
        ),
        background="周代以来の詩教論として『書経』『毛詩序』に明示的に立てられた。",
        development="陸機の「縁情」論との対立を通じて中国詩学の基軸論争を形成、唐宋古文運動の文以載道に展開。",
        historical_context="周代から漢代にかけての儒家詩教論の体系化。",
        primary_source_url="https://ctext.org/shang-shu/canon-of-yao",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("主体", "rethinking",
                      "言志は詩を「私の志」の表現と規定し、明確な作家主体の存在を前提とする。"
                      "『私』の倫理的志向の言語化という構造は、AIの「主体なき発話」と対比すれば"
                      "近代的な作家主体論より遙かに先鋭な形で「主体の問題」を提起する。",
                      "AI生成テキストの「志」不在問題、生成AIと意図性の哲学"),
                     ("作者性", "partial",
                      "言志論は詩と作者の倫理的同一性を要請する点で、強い作者性概念を持つ。"
                      "AIに「志」はあるかという根源的問いに繋がる。",
                      "AI著作権・AI作者性をめぐる論争")],
        cross=[("PHIL", None, "yanzhi", "shared_concept",
                "東アジア倫理学の意図・志の概念と詩学の交差点")],
    ))

    records.append(dict(
        name_ja="縁情", name_en="yuanqing (poetry traces emotion)",
        name_original="緣情", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "陸機『文賦』の「詩縁情而綺靡（詩は情に縁って綺靡たり）」に由来する詩論。"
            "言志論が政教倫理的志を強調するのに対し、詩を個人的感情に発するものとし、"
            "美的洗練を重視する。六朝以降の唯美主義・抒情主義の理論的支柱となった。"
        ),
        background="魏晋玄学の個人意識と六朝美意識の隆盛が背景。",
        development="言志vs縁情論争は中国詩学最大の理論的二分法として千年以上続いた。",
        historical_context="3世紀末西晋の文学的個人主義。",
        primary_source_url="https://ctext.org/wen-xuan",
        primary_source_type="anthology",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="物感", name_en="wugan (stirred by things)",
        name_original="物感", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "外界の事物に触発されて感情・創作が発動するという中国詩学の発生論。"
            "鍾嶸『詩品』序「気之動物、物之感人、故揺蕩性情、形諸舞詠」に明示される。"
            "西欧のミューズ的霊感とは異なり、自然事物との感応に詩の発生を求める。"
        ),
        background="六朝玄学・気の哲学・美学が結合して理論化された。",
        development="後世の「興」「観物」「感物」論の基礎、宋明理学の格物致知にも繋がる。",
        historical_context="魏晋南北朝の自然観・感応思想。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[("創造性", "rethinking",
                      "物感は外界事物との感応を創作の起点とする点で、"
                      "個別主体の内的霊感に立脚する西欧ロマン主義的創造性とは異なるモデルを提示。"
                      "また、世界との実体的感応はAIの確率的言語生成とも本質的に異なる。",
                      "AI時代の創造性発生論、生成AIと「世界経験」の不在")],
    ))

    records.append(dict(
        name_ja="遺民意識", name_en="yimin yishi (loyalist consciousness)",
        name_original="遺民意識", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "前王朝に忠を尽くし新王朝に仕えない「遺民」の精神的姿勢を文学化した主題。"
            "陶淵明の東晋への忠（「義熙」紀年使用説）が古典的範例とされ、後世の宋遺民・"
            "明遺民詩文の母型となった。亡国の悲しみと節操の固持を結合する。"
        ),
        background="王朝交代期における士人の倫理選択の文学化。",
        development="南宋遺民・明末清初遺民・近代清遺民へ千年以上継承された。",
        historical_context="政治変動期における士人の節操論。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89568",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="以詩為文", name_en="yi shi wei wen (prose written like poetry)",
        name_original="以詩為文", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "詩のような修辞・対句・凝縮を散文に持ち込む文体的方法。"
            "六朝の駢文に典型的に見られる文体観で、唐宋古文運動（韓愈・柳宗元）が"
            "批判する対象となった概念。後の「以文為詩」（宋代）と対をなす。"
        ),
        background="六朝の修辞主義散文（駢文）の特質を批評的に概念化したもの。",
        development="唐宋古文運動による批判を通じて散文の独立性が確立された。",
        historical_context="六朝-唐の散文文体史。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=752088",
        primary_source_type="classical_text",
        importance_score=3, source_tier="secondary", canonical_in_region="minor",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="以文為詩", name_en="yi wen wei shi (poetry written like prose)",
        name_original="以文為詩", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "散文的な議論・叙事・説明を詩中に持ち込む方法。中唐の韓愈詩に典型的に表れ、"
            "宋詩（特に黄庭堅・蘇軾）に継承された。詩の音楽性・抒情性を犠牲にしても"
            "知的・議論的内容を詩化する方向で、宋詩の議論調の起源となる。"
        ),
        background="中唐韓愈の詩実践と古文運動の散文志向が結合。",
        development="宋詩全体の議論的・知的傾向の理論的支柱となった。",
        historical_context="9世紀韓孟詩派と古文運動の文学革新。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="声律論", name_en="shenglü lun (theory of tonal prosody)",
        name_original="聲律論", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "南斉の沈約・周顒らが提唱した中国語の四声（平上去入）に基づく詩の音律理論。"
            "「永明体」と呼ばれる新詩体を生み、唐代近体詩の平仄規則の直接的基礎となった。"
            "中国語の声調が詩の形式に組み込まれた画期的理論。"
        ),
        background="梵語の韻律理論と中国語の四声発見が結合して成立。",
        development="初唐沈宋（沈佺期・宋之問）による近体詩の規則化に直結した。",
        historical_context="5-6世紀南斉梁の音韻学発展と仏教の音声論流入。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[("言語", "partial",
                      "声律論は中国語の音韻特質を詩形式に決定的に組み込んだ言語特殊主義的理論。"
                      "中国語の音響的特質に依存するため、機械翻訳・LLMによる多言語的標準化と"
                      "本質的に対立する側面を持ち、AI時代の言語多様性論への参照点となる。",
                      "LLM多言語処理における音韻特性の損失、AI翻訳と詩学")],
    ))

    records.append(dict(
        name_ja="四声八病", name_en="sisheng babing (four tones, eight defects)",
        name_original="四聲八病", original_script="kanji",
        period_id=P_WJ,
        definition=(
            "沈約による永明体の具体的規則。中国語の四声（平上去入）を基に、"
            "詩中で避けるべき八種の音律的欠陥（平頭・上尾・蜂腰・鶴膝・大韻・小韻・"
            "傍紐・正紐）を体系化した。極めて精緻な音律規定だが煩瑣との批判もあった。"
        ),
        background="梵語音韻学と中国語四声の発見の応用。",
        development="近体詩平仄規則に簡略化・継承された。",
        historical_context="6世紀斉梁の音韻論隆盛。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=3, source_tier="primary", canonical_in_region="minor",
        fourth_tags=[],
    ))

    records.append(dict(
        name_ja="点鉄成金", name_en="diantie chengjin (turning iron into gold)",
        name_original="點鐵成金", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "古人の語句を取り入れ新たな意味に転化する詩作方法。"
            "宋代黄庭堅が古典詩作の方法として提唱した概念だが、その源流は中唐韓愈・"
            "李賀以来の典故活用にあり、本DBでは唐代までの典故活用方法として採録する。"
            "鉄を金に変えるように、既存の語句を新たな価値に変換する技法を意味する。"
        ),
        background="中唐韓愈・李賀の博奥な典故活用が原型。",
        development="宋代江西詩派により方法論として体系化、後世の典故詩学の中核となる。",
        historical_context="中晚唐から宋代にかけての文学的精緻化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[("創造性", "partial",
                      "点鉄成金は既存テクストの再構成によって新たな価値を生み出す方法であり、"
                      "ロマン主義的独創性とは異なるimitatio型創造性の東アジア版である。"
                      "AI時代のプロンプト工学・既存データ再構成による創造と直接的対比が可能。",
                      "LLM出力の本質（訓練データ再構成）、AIプロンプト工学と典故活用の比較"),
                     ("作者性", "partial",
                      "他者の語句を自作に取り込むことで作者性が分散する点で、"
                      "ロマン主義的単一作者観とAI時代の協働的執筆観の中間に位置する伝統である。",
                      "AI協働執筆の作者帰属問題")],
        cross=[("PT", None, "diantie chengjin", "parallel",
                "Poetics DBのimitatio・intertextuality概念に対応する東アジア独自の方法論")],
    ))

    records.append(dict(
        name_ja="夺胎换骨", name_en="duotai huangu (taking embryo, exchanging bones)",
        name_original="奪胎換骨", original_script="kanji",
        period_id=P_TANG,
        definition=(
            "古人の意を取って語を変え（奪胎）、語を取って意を変える（換骨）詩作方法。"
            "宋代黄庭堅・呂本中らによって理論化されたが、唐代韓孟詩派の典故革新方法に"
            "源流がある。点鉄成金と並び江西詩派の二大方法として知られる。"
            "本DBでは唐代の方法論的源流として採録する。"
        ),
        background="中唐韓愈・李賀の典故再利用法が原型を提供。",
        development="宋代江西詩派により方法論として体系化、明清の詩論にも継承。",
        historical_context="中唐-宋初の詩学の方法論的精緻化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=148291",
        primary_source_type="classical_text",
        importance_score=3, source_tier="secondary", canonical_in_region="minor",
        fourth_tags=[("創造性", "partial",
                      "古典の身体（胎・骨）を借りて新たな生命を吹き込む方法は、"
                      "AI時代のファインチューニング・プロンプトエンジニアリングと"
                      "創造的な「再利用」の系譜として比較可能である。",
                      "LLMファインチューニング、プロンプトによるテキスト変換")],
        cross=[("PT", None, "duotai huangu", "parallel",
                "imitatio・rewriting・transformation概念に対応する東アジア独自の方法論")],
    ))

    return records


# ----------------------------------------------------------------
# 投入処理
# ----------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("LIT-DB Phase 2 Pilot C13: 中国古典文学（先秦〜唐）50概念")
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
        assert len(records) == 50, f"expected 50 records, got {len(records)}"

        # Step 3: 概念投入
        with db.transaction():
            for rec in records:
                fourth_tags = rec.pop("fourth_tags", [])
                cross = rec.pop("cross", [])

                cid = db.insert_concept(
                    subfield_code="lit_cn_classical",
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
            # name_ja でidを取得するヘルパー
            def cid_of(name: str) -> int:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE name_ja=? AND region='東アジア'",
                    (name,),
                ).fetchone()
                if not row:
                    raise RuntimeError(f"concept not found: {name}")
                return row["id"]

            relations_data = [
                # 詩経三大区分 -> 楚辞体（南北詩源流）
                ("風雅頌", "楚辞体", "precedes",
                 "北方詩経と南方楚辞は中国詩史の二大源流として対をなす"),
                # 楚辞体 -> 賦（直接継承）
                ("楚辞体", "賦", "extends",
                 "楚辞の長句修辞は漢賦に直接継承された"),
                # 楽府 -> 古詩十九首
                ("楽府", "古詩十九首", "precedes",
                 "楽府民歌から文人五言詩への移行を示す画期的作品"),
                # 古詩十九首 -> 近体詩
                ("古詩十九首", "近体詩", "precedes",
                 "五言詩の成立から近体詩への定型化"),
                # 声律論 -> 近体詩
                ("声律論", "近体詩", "introduced_by",
                 "永明体の声律論が近体詩の平仄規則の直接的基礎"),
                ("四声八病", "声律論", "extends",
                 "四声八病は声律論を具体化した規則"),
                ("近体詩", "律詩", "contains",
                 "律詩は近体詩の中心形式"),
                ("近体詩", "絶句", "contains",
                 "絶句は近体詩の短詩形式"),
                # 賦比興（修辞） -> 賦（ジャンル）
                ("賦（修辞法）", "賦", "extends",
                 "詩経の修辞法「賦」がジャンル名「賦」の語源となった"),
                # 言志 vs 縁情 の二元論
                ("言志", "縁情", "criticizes",
                 "言志（倫理的志）と縁情（個人感情）は中国詩学最大の理論的二分"),
                # 物感 -> 興
                ("物感", "興", "extends",
                 "物感の発生論は興の修辞論として詩経注釈に既に体現"),
                # 神思 -> 含蓄/意境
                ("神思", "意境", "precedes",
                 "神思の創作主体論が意境論の前提を提供"),
                ("含蓄", "意境", "extends",
                 "言外の含蓄が意境の核心要件"),
                # 滋味 -> 含蓄
                ("滋味", "含蓄", "extends",
                 "滋味論は含蓄論の前駆"),
                # 風骨 -> 気韻
                ("風骨", "気韻", "extends",
                 "風骨と気韻は六朝美学の双璧"),
                # 隠逸 -> 山水/田園
                ("隠逸", "山水", "extends",
                 "隠逸思想が山水詩の世界観的基礎"),
                ("隠逸", "田園", "extends",
                 "隠逸思想が田園詩の生活的基礎"),
                # 出処 -> 隠逸
                ("出処", "隠逸", "precedes",
                 "出処論が隠逸選択の倫理的枠組み"),
                # 志道 -> 言志
                ("志道", "言志", "precedes",
                 "士人の志道理念が詩言志論の倫理的基礎"),
                # 詩派系譜
                ("建安七子", "竹林七賢", "precedes",
                 "建安文学から竹林七賢へ、魏晋転換期の文人集団系譜"),
                ("陶謝", "王孟", "precedes",
                 "陶謝の山水田園が王孟詩派の直接的祖型"),
                ("初唐四傑", "李杜", "precedes",
                 "初唐四傑の改革が盛唐李杜の出現を準備"),
                ("李杜", "韓孟詩派", "precedes",
                 "盛唐李杜の後、中唐に韓孟詩派が登場"),
                ("韓孟詩派", "元白詩派", "criticizes",
                 "中唐の二大詩派は奇崛 vs 平易で対立的"),
                ("韓孟詩派", "苦吟派", "extends",
                 "韓孟の彫琢主義が晚唐苦吟派に継承"),
                # 以詩為文 vs 以文為詩
                ("以詩為文", "以文為詩", "criticizes",
                 "六朝の駢文化に対する中唐古文運動の反動として以文為詩が成立"),
                # 韓孟詩派 -> 点鉄成金/夺胎换骨
                ("韓孟詩派", "点鉄成金", "precedes",
                 "韓孟の典故活用が宋代点鉄成金論の源流"),
                ("点鉄成金", "夺胎换骨", "extends",
                 "二法は江西詩派の双璧として対をなす"),
                # 以文為詩 -> 韓孟詩派
                ("韓孟詩派", "以文為詩", "exemplifies",
                 "韓愈詩こそ以文為詩の典型実例"),
                # 元白詩派 -> 楽府（新楽府）
                ("楽府", "元白詩派", "extends",
                 "新楽府運動が元白詩派の中核活動"),
                # 主題的関係
                ("忠君愛国", "遺民意識", "extends",
                 "忠君愛国の倫理が王朝交代期に遺民意識として結晶"),
                ("懐古", "遺民意識", "extends",
                 "懐古主題が王朝交代期に遺民意識と深く結合"),
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
                    source_evidence="中国古典文学史標準的記述",
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
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id=8"
        ).fetchone()
        print(f"subfield_id=8 total concepts: {row['c']}")

        # Tier別
        rows = db.conn.execute(
            "SELECT source_tier, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=8 GROUP BY source_tier"
        ).fetchall()
        print(f"source_tier distribution (subfield 8): {[dict(r) for r in rows]}")

        # importance別
        rows = db.conn.execute(
            "SELECT importance_score, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=8 GROUP BY importance_score ORDER BY importance_score DESC"
        ).fetchall()
        print(f"importance_score distribution: {[dict(r) for r in rows]}")

        # canonical別
        rows = db.conn.execute(
            "SELECT canonical_in_region, COUNT(*) AS c FROM concepts "
            "WHERE subfield_id=8 GROUP BY canonical_in_region"
        ).fetchall()
        print(f"canonical_in_region distribution: {[dict(r) for r in rows]}")

        # 第四変容タグ分布
        rows = db.conn.execute(
            """SELECT t.axis, t.status, COUNT(*) AS c
               FROM fourth_transform_tags t
               JOIN concepts c ON c.id = t.concept_id
               WHERE c.subfield_id = 8
               GROUP BY t.axis, t.status
               ORDER BY t.axis, t.status"""
        ).fetchall()
        print(f"fourth_transform_tags distribution (subfield 8):")
        for r in rows:
            print(f"  {r['axis']:6s} | {r['status']:11s} | {r['c']}")


if __name__ == "__main__":
    main()
