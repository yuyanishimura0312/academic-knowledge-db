"""
LIT-DB Phase 2 Wave 4: C14 — 中国古典文学（宋元明清）40概念投入スクリプト

主パターン: P1 (Canonical Primary Pursuit)
subfield_id=8 (lit_cn_classical), region='東アジア'

C13（先秦〜唐50件）の続編。重複ゼロを保証しつつ宋〜清の40概念を投入する。

構成:
- A. 宋詩・宋詞（8件）
- B. 元明清の詩文（8件）
- C. 章回小説と四大奇書（8件）
- D. 詩学・批評（8件）
- E. 主題・メタ概念（8件）

使用法:
    python3 wave4_c14_chinese_classical_late.py
"""

from __future__ import annotations

from lit_db_helper import LitDB


# ----------------------------------------------------------------
# 期間（宋〜清）の用意
# ----------------------------------------------------------------

def setup_periods(db: LitDB) -> dict:
    """宋〜清の主要時代区分を get_or_create する。"""
    periods = {}
    periods["宋"] = db.get_or_create_period(
        name_ja="宋", name_en="Song",
        region="東アジア", start_year=960, end_year=1279,
        description="北宋・南宋。詩・詞・古文の盛期、江西詩派・婉約豪放詞派が並立。",
    )
    periods["元"] = db.get_or_create_period(
        name_ja="元", name_en="Yuan",
        region="東アジア", start_year=1271, end_year=1368,
        description="モンゴル支配下、雑劇（元曲）と通俗文学が興隆した時代。",
    )
    periods["明"] = db.get_or_create_period(
        name_ja="明", name_en="Ming",
        region="東アジア", start_year=1368, end_year=1644,
        description="章回小説・戯曲が完成し、公安派・性霊説が古文に挑戦した時代。",
    )
    periods["清"] = db.get_or_create_period(
        name_ja="清", name_en="Qing",
        region="東アジア", start_year=1644, end_year=1911,
        description="桐城派・神韻・格調・性霊・肌理の四詩派論争、紅楼夢の頂点。",
    )
    return periods


# ----------------------------------------------------------------
# 40概念データ定義
# ----------------------------------------------------------------

def build_concept_records(periods: dict) -> list[dict]:
    P_SONG = periods["宋"]
    P_YUAN = periods["元"]
    P_MING = periods["明"]
    P_QING = periods["清"]

    records: list[dict] = []

    # ============================================================
    # A. 宋詩・宋詞（8件）
    # ============================================================
    records.append(dict(
        name_ja="江西詩派", name_en="Jiangxi Poetry School",
        name_original="江西詩派", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "北宋末から南宋初にかけて黄庭堅を祖とし、陳師道・陳与義らを中堅とする"
            "宋代最大の詩派。呂本中『江西詩社宗派図』により25人が列名され体系化された。"
            "杜甫を「一祖」、黄庭堅を「宗主」とし、典故活用・拗体・点鉄成金・夺胎换骨"
            "を方法論的核心とする。学問詩・文人詩の典型として後世長く論争の対象となった。"
        ),
        background="北宋末の党争・文化沈滞期、唐詩との差別化を求める文人意識から成立。",
        development="南宋の楊万里・陸游らの批判を受けるも、明清に至るまで宋詩の代表派として再評価される。",
        historical_context="北宋末政治の混乱と文人士大夫の精神的亡命志向。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89436",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PHIL", None, "Song Neo-Confucianism", "parallel",
                "理学思潮と並走する詩派、学問と詩の融合志向")],
    ))

    records.append(dict(
        name_ja="蘇軾「以詩為文・以文為詩」総合", name_en="Su Shi's poetic-prose synthesis",
        name_original="蘇軾以詩為文以文為詩", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "蘇軾（東坡）が体現したジャンル横断的文章観。詩に文の議論性・散文性を導入し、"
            "文に詩の情感・比興を込める双方向的方法。宋代古文運動の集大成として、"
            "詩・文・賦・詞・尺牘・題跋を一貫した「文気」で統合した。"
            "韓愈以来の「以文為詩」を更に推進し、後の散文化詩風の理論的支柱となった。"
        ),
        background="北宋古文運動の歐陽脩を継承し、王安石新法を批判的に咀嚼した蘇軾独自の総合。",
        development="江西詩派・南宋詩への影響、明代公安派・清代桐城派の議論の出発点となる。",
        historical_context="北宋党争（新旧法党争）と文人の漂泊体験（黄州・恵州・儋州）。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=82253",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PHIL", None, "literary genre theory", "parallel",
                "散文と韻文の境界融解という文体論的問題")],
    ))

    records.append(dict(
        name_ja="黄庭堅 江西詩学体系", name_en="Huang Tingjian's poetics",
        name_original="黃庭堅江西詩學體系", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "黄庭堅（山谷）が提示した詩作理論の体系。点鉄成金・夺胎换骨を二大方法とし、"
            "杜甫を絶対の宗とし、典故・拗体・反俗・無一字無来処を強調する。"
            "「詩は意を以て主と為す」（意主論）と表現主体性を打ち出しつつ、"
            "古典再活用による「変化」を創造性の核心とした、東アジア初の体系的詩学方法論。"
        ),
        background="蘇軾門下にあって独立、北宋末の文化的爛熟期に古典再構築運動を主導。",
        development="陳師道・陳与義・呂本中らに継承され江西詩派の理論的中核となる。",
        historical_context="新旧法党争に巻き込まれた黄庭堅の流謫体験と仏教（禅）への傾倒。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=85636",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("創造性", "rethinking",
             "黄庭堅の「無一字無来処」「点鉄成金 夺胎换骨」は典故再構成による創造性論。"
             "AI時代の事前学習＋プロンプト工学による生成と構造的に酷似し、"
             "「ゼロからの創造」幻想を1000年前に既に解体していた。",
             "LLM事前学習・プロンプト工学・RAG・テキスト再構成型創造性")],
        cross=[("PT", None, "imitatio doctrine", "parallel",
                "西欧 imitatio・西修辞学の rewriting に対応する東アジア独自の方法論")],
    ))

    records.append(dict(
        name_ja="王安石新法詩", name_en="Wang Anshi's reformist poetry",
        name_original="王安石新法詩", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "北宋の宰相・王安石（1021-1086）が新法（青苗法・市易法等の経済改革）を"
            "推進する立場から書いた政治詩・社会詩の総称。儒教的経世思想と詩経「美刺」"
            "（風刺）伝統を結合し、政治的主張を詩で展開した。後に「拗体」風の独自詩風"
            "「半山体（半山絶句）」へと発展、宋詩の論理性・議論性の典型となる。"
        ),
        background="慶暦の改革挫折後、神宗朝の新法運動に詩を理論武装として動員。",
        development="蘇軾の旧法党詩との論争を経て、宋詩独自の「議論する詩」の伝統を形成。",
        historical_context="北宋中期の財政危機と新旧法党争。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89523",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("MG", None, "policy reform", "parallel",
                "経済政策と文学表現の連動、政策論争の文学的表出")],
    ))

    records.append(dict(
        name_ja="陸游愛国詩", name_en="Lu You's patriotic poetry",
        name_original="陸游愛國詩", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "南宋の陸游（1125-1210）による中原失陥への悲憤と北伐悲願を詠った詩群の総称。"
            "「王師北定中原日、家祭無忘告乃翁」（示児）に代表される、"
            "国家滅亡危機下の士大夫の心情を結晶化した愛国主義詩の典型。"
            "杜甫の「忠君愛国」伝統を直接継承し、後世の遺民詩・抗戦詩の祖型となる。"
        ),
        background="北宋滅亡（靖康の変、1127）と南宋朝廷の主和派優勢への抵抗。",
        development="文天祥『正気歌』、明末・清末の遺民詩、近代抗日詩へと連続する系譜の起点。",
        historical_context="南宋の対金・対モンゴル戦争と主戦・主和派の対立。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185655",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="楊万里誠斎体", name_en="Yang Wanli's Chengzhai style",
        name_original="楊萬里誠齋體", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "南宋の楊万里（1127-1206、号誠斎）が確立した活発な口語的・即興的詩風。"
            "江西詩派の典故重視を批判し、自然観察と日常感覚を「活法」「悟入」によって"
            "鮮やかに捉える。禅の「現量」観に通じ、平易明快な語彙で機智に富む詩境を開いた。"
            "南宋四大家（陸・楊・范・尤）の一として宋詩の新方向を示した。"
        ),
        background="紹興・乾道年間、江西詩派の硬直化に対する内部批判として誕生。",
        development="清代の袁枚「性霊説」へ間接的に継承、現代日本俳句的鑑賞にも影響。",
        historical_context="南宋中期の文化的安定と江西詩派の制度化への反動。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185657",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="李清照婉約詞", name_en="Li Qingzhao's wanyue ci",
        name_original="李清照婉約詞", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "北宋末・南宋初の女性詞人・李清照（1084-1155頃）に代表される婉約派詞風。"
            "繊細な感情・閨情・別離・喪失を口語的かつ平易な語彙で精緻に表現する。"
            "彼女の『詞論』は詞を「別是一家」（独自ジャンル）と主張し、詩との差異化を理論化。"
            "婉約 vs 豪放の二元論を生む発端となった。中国文学史上代表的女性作家。"
        ),
        background="北宋滅亡前後の動乱を体験した夫婦（趙明誠との金石学）の知的環境。",
        development="後の朱淑真等女流詞人、清代「随園女弟子」群へと女性文学の系譜を形成。",
        historical_context="北宋末の文化的爛熟と靖康の変による南渡体験。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185659",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("AN", None, "gender and literature", "parallel",
                "東アジア女性文学の自覚的ジャンル定義の最初期事例")],
    ))

    records.append(dict(
        name_ja="辛棄疾豪放詞", name_en="Xin Qiji's haofang ci",
        name_original="辛棄疾豪放詞", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "南宋の辛棄疾（1140-1207、号稼軒）が発展させた豪放派詞風。"
            "蘇軾の豪放詞を更に推進し、英雄的気概・愛国憤慨・歴史回顧・典故活用を"
            "豪壮なリズムで結晶化する。「以文為詞」（散文を詞に持ち込む）を実践し、"
            "詞というジャンルの限界を押し広げた。婉約派と並ぶ宋詞の双璧。"
        ),
        background="主戦派将軍として金軍と戦った経歴、政治的不遇による詞作集中。",
        development="清の陳維崧らに継承、現代の「愛国文学」概念の祖型ともなる。",
        historical_context="南宋の対金抗戦と主和派優位下での主戦派将官の鬱屈。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185658",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    # ============================================================
    # B. 元明清の詩文（8件）
    # ============================================================
    records.append(dict(
        name_ja="元曲（雑劇）", name_en="Yuan zaju drama",
        name_original="元曲（雜劇）", original_script="kanji",
        period_id=P_YUAN,
        definition=(
            "元代に大成した代表的戯曲ジャンル。一本四折＋楔子という定型構造を持ち、"
            "一人の主役（正末か正旦）が全曲歌唱する形式。"
            "北曲（北方音楽）に詞本（韻文）と賓白（科白）を組み合わせ、"
            "口語と典雅を融合した独自の文学言語を成立させた。"
            "関漢卿・王実甫・馬致遠・白樸を四大家とし、中国戯曲文学の頂点を形成した。"
        ),
        background="モンゴル支配下、科挙廃止により士人が市井の戯曲制作へ転じた社会背景。",
        development="明清の伝奇（南曲）に発展継承され、京劇等地方劇に影響、東アジア戯曲の母体となる。",
        historical_context="元朝の科挙中断・士人地位低下と都市商業文化の発達。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=85715",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PT", None, "drama theory", "parallel",
                "アリストテレス『詩学』の悲劇論に対比する東アジア戯曲ジャンル理論")],
    ))

    records.append(dict(
        name_ja="関漢卿『竇娥冤』", name_en="Guan Hanqing's Injustice to Dou E",
        name_original="關漢卿《竇娥冤》", original_script="kanji",
        period_id=P_YUAN,
        definition=(
            "関漢卿（1234頃-1300頃）作の元雑劇代表作。"
            "貞節寡婦・竇娥が冤罪で処刑され、死後三大誓い（血が白幡に飛ぶ・六月に雪が降る・"
            "三年大旱）で天を動かして冤を晴らす悲劇。"
            "民衆の社会正義渇望と元代司法の腐敗を激しく批判する社会派戯曲の典型。"
            "中国四大悲劇の一として後世長く演じ継がれた。"
        ),
        background="元朝官僚機構の腐敗と漢人民衆の沈黙的怨恨を背景に成立。",
        development="明清の小説・戯曲、現代京劇『六月雪』、白話小説への影響甚大。",
        historical_context="元朝の差別的民族統治政策と司法不公正。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=85716",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="王実甫『西廂記』", name_en="Wang Shifu's Romance of the Western Chamber",
        name_original="王實甫《西廂記》", original_script="kanji",
        period_id=P_YUAN,
        definition=(
            "王実甫（1260頃-1336頃）作の五本二十一折の長編元雑劇。"
            "唐代元稹『鶯鶯伝』を原型に、張生と崔鶯鶯の自由恋愛を「願天下有情人都成了眷属」"
            "（願わくは天下の有情人皆眷属となれ）と謳い、礼教批判の先駆となった。"
            "「花間美人」と称される典雅な詞章と「滴翠」の自然描写で元曲の最高傑作と評される。"
        ),
        background="唐代伝奇『鶯鶯伝』、董解元『西廂記諸宮調』を改作した最終形態。",
        development="明清の戯曲・小説、特に『紅楼夢』第二十三回の引用、中国恋愛文学の典型を確立。",
        historical_context="元代都市文化の自由恋愛志向と儒教的礼教との緊張。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=85717",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="公安派", name_en="Gongan School",
        name_original="公安派", original_script="kanji",
        period_id=P_MING,
        definition=(
            "明代万暦年間の袁宗道・袁宏道・袁中道（湖北公安出身の三兄弟）を中心とする"
            "詩文革新運動。「独抒性霊、不拘格套」（性霊を独自に表出し、格套に拘らない）を旗印に、"
            "前後七子の擬古主義（復古論）を激しく批判した。"
            "後の竟陵派・清代性霊説に直接系譜が繋がり、中国文学における近代的個性表現の起点。"
        ),
        background="明代中後期の李夢陽・李攀龍ら前後七子の擬古一辺倒に対する反動。",
        development="竟陵派（鍾惺・譚元春）、清代袁枚性霊説、五四新文学運動の白話詩へと連続。",
        historical_context="明末の商業文化発達と儒教的科挙文学価値観の動揺。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185660",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("主体", "rethinking",
             "公安派の「性霊」「真我」「童心」（李贄）は近代的個性概念の前駆。"
             "AIの非人間的「主体性」問題（生成主体は誰か）と接続する。",
             "AI生成コンテンツの作者性論争・LLMペルソナ・人格的真正性")],
        cross=[("PHIL", None, "Li Zhi's tongxin", "parallel",
                "李贄の童心説と並走する明末の主体性思想")],
    ))

    records.append(dict(
        name_ja="性霊説", name_en="xingling theory",
        name_original="性靈說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代袁枚（1716-1797、号随園）が体系化した詩学説。"
            "「詩を作るには性情を主と為すべし、その次は格律」と性情・天性の率直表出を中心に置く。"
            "明代公安派の性霊論を直接継承しつつ、女性詩人を多数門人化（随園女弟子）し、"
            "格調説・神韻説・肌理説と四詩派論争を展開した。中国近世における個性主義の頂点。"
        ),
        background="明代公安派の性霊論を承け、清初の格調・神韻論の硬直化に対する反動。",
        development="近代以降の個性表現論、五四新文学の自我主義へと継承される。",
        historical_context="清代乾隆年間の文化的繁栄と科挙文学の儀式化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89522",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("主体", "rethinking",
             "性霊説の「真我表出」は文学における主体の真正性原理。"
             "AI生成テキストでは「主体」が分散・不在となり、性霊概念の前提が問い直される。",
             "AI生成コンテンツの作者主体問題・人格的真正性")],
        cross=[("PT", None, "expressivism", "parallel",
                "西欧 expressivism（Romantic theory）と並走する東アジア表出主義")],
    ))

    records.append(dict(
        name_ja="桐城派", name_en="Tongcheng School",
        name_original="桐城派", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代の方苞・劉大櫆・姚鼐（安徽桐城出身）を中心とする古文派。"
            "「義法」（義＝内容、法＝法度）を主軸に、「神理気味」「格律声色」"
            "等の精緻な文章論を展開した。唐宋八大家文を範とし、"
            "桐城三祖から曽国藩らに至るまで200年にわたり清代古文の主流を占めた。"
            "東アジア最大の体系的散文流派。"
        ),
        background="明末清初の散文乱脈に対する規範化の要請から成立。",
        development="湘郷派（曽国藩）、清末民初の古文継承・批判を経て、現代散文教育の素地となる。",
        historical_context="清朝の漢学興隆と古文教学制度の整備。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185661",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="浙西詞派", name_en="Zhexi ci School",
        name_original="浙西詞派", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代康熙年間の朱彝尊・厲鶚らを中心とする詞派。"
            "南宋姜夔・張炎を範とし、「清空」「醇雅」を旨とする。"
            "明末以降衰退していた詞ジャンルを復興し、清代詞学の先駆となった。"
            "後の常州詞派（張惠言・周済）と対をなす清代詞二大派。"
        ),
        background="明代詞の俗化に対する反動、南宋雅詞の再評価運動。",
        development="常州詞派の比興寄託論への批判的継承を経て、晩清王国維の詞論へと連続。",
        historical_context="清初の文人結社隆盛と地方文化アイデンティティ。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185662",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="性靈派 vs 格調派", name_en="Xingling vs Gediao schools",
        name_original="性靈派對格調派", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代乾隆年間の二大詩学論争。袁枚の性霊派（個性・天性表出を主軸）と"
            "沈徳潜の格調派（漢魏盛唐を範とする格律重視）が対立した。"
            "性霊派は明代公安派の系譜を継承し、格調派は前後七子の擬古論を継承する。"
            "後に翁方綱の肌理説・王士禎の神韻説と合わせて清代四詩派と称される。"
        ),
        background="清代乾嘉学術と詩学批評の制度化。",
        development="近代以降「個性 vs 格律」の文学理論二元論へと抽象化される。",
        historical_context="清代盛世の文人サークル・詩壇政治。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185663",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("PT", None, "expressivism vs formalism", "parallel",
                "西欧 expressivism vs formalism 論争に対応する清代詩壇の二極対立")],
    ))

    # ============================================================
    # C. 章回小説と四大奇書（8件）
    # ============================================================
    records.append(dict(
        name_ja="章回小説", name_en="zhanghui xiaoshuo (chaptered novel)",
        name_original="章回小說", original_script="kanji",
        period_id=P_MING,
        definition=(
            "明代に成立した中国独自の長編小説形式。各回に二句対偶の回目（章タイトル）を持ち、"
            "「話説」「却説」で語り起こし「欲知後事如何、且聴下回分解」で締める"
            "講釈師（説話人）口演の文学化フォーマット。"
            "三国演義・水滸伝・西遊記・金瓶梅の四大奇書、"
            "後の儒林外史・紅楼夢に至るまで全て章回体で書かれた。"
        ),
        background="宋元の話本（講釈台本）が文人によって書面文学化された結果として成立。",
        development="明清の代表的小説形式となり、東アジア通俗文学の典型として日本・朝鮮・ベトナムへ伝播。",
        historical_context="明代都市商業文化と印刷出版業の発達。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=85718",
        primary_source_type="reference_work",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("物語", "partial",
             "章回小説は連続的・拡張可能・登場人物大量・並行プロット等、"
             "現代の連載・シリーズ・大規模ナラティブの先駆構造を持つ。"
             "AI生成長編ナラティブのプロット管理問題と接続する。",
             "LLM長編生成・並行プロット管理・ストーリー記憶・連載AI")],
        cross=[("Myth-Narratives", None, "long-form narrative", "parallel",
                "西欧 picaresque novel・Roman fleuve に対応する東アジア独自の長編形式")],
    ))

    records.append(dict(
        name_ja="三国演義", name_en="Romance of the Three Kingdoms",
        name_original="三國演義", original_script="kanji",
        period_id=P_MING,
        definition=(
            "羅貫中（14世紀）作とされる120回の歴史演義小説。"
            "後漢末から西晋統一までの群雄割拠を描き、「七実三虚」と称される史実と虚構の融合、"
            "曹操・劉備・諸葛亮・関羽等の人物造型で東アジア最大の集合的物語遺産を形成。"
            "中国四大奇書・四大名著の一として、現代に至るまでアジア大衆文化の核心源泉となる。"
        ),
        background="陳寿『三国志』、裴松之注、宋元の三国話本・雑劇を素材として集成。",
        development="毛宗崗評本（清初）が標準テキスト、日本の『三国志演義』訳・現代漫画ゲーム化等。",
        historical_context="元末明初の動乱と忠義イデオロギー再構築の時代。",
        primary_source_url="https://ctext.org/sanguo-yanyi",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="水滸伝", name_en="Water Margin",
        name_original="水滸傳", original_script="kanji",
        period_id=P_MING,
        definition=(
            "施耐庵（14世紀）に帰される章回小説。北宋末の宋江ら108人の梁山泊好漢の"
            "反乱と招安を描く。「逼上梁山」（追い詰められて反逆する）の成語を生み、"
            "民衆反逆叙事の原型となった。武松・林冲・魯智深らの個性的英雄群像と、"
            "白話文体の確立で明代白話小説の頂点を形成する。"
        ),
        background="宋江の乱（1119-1121）の史実、宋元の水滸話本・雑劇を素材とする。",
        development="金聖歎70回本（清初）が標準。明清の『金瓶梅』・現代の革命文学に影響。",
        historical_context="明代後期の社会矛盾激化と民衆反乱への文人共感。",
        primary_source_url="https://ctext.org/shui-hu-zhuan",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="西遊記", name_en="Journey to the West",
        name_original="西遊記", original_script="kanji",
        period_id=P_MING,
        definition=(
            "呉承恩（1500頃-1582頃）作とされる100回の神魔小説。"
            "玄奘三蔵が孫悟空・猪八戒・沙悟浄を従え天竺に経典を取りに行く旅を描く。"
            "「修心」（心の修養）を寓意的主題とし、儒仏道三教の習合的世界観を展開。"
            "孫悟空の72変化・如意金箍棒等の幻想的想像力で中国神魔小説の頂点を成す。"
        ),
        background="玄奘『大唐西域記』、宋元の取経話本『大唐三蔵取経詩話』、明代神魔民間信仰を結合。",
        development="清代の続書群、京劇、近現代の漫画・映画・アニメ（日本『ドラゴンボール』等）に。",
        historical_context="明代中後期の三教合一思潮と民間道教信仰。",
        primary_source_url="https://ctext.org/xiyouji",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("Myth-Narratives", None, "quest narrative", "parallel",
                "西欧 quest romance・Hero's Journey に対応する東アジア神魔取経物語")],
    ))

    records.append(dict(
        name_ja="金瓶梅", name_en="The Plum in the Golden Vase",
        name_original="金瓶梅", original_script="kanji",
        period_id=P_MING,
        definition=(
            "蘭陵笑笑生（仮名、16世紀後半）作とされる100回の世情小説。"
            "西門慶を主人公とし、潘金蓮・李瓶児・春梅（書名由来）の女性群像と"
            "明代後期都市市民の物質的生活・性・経済・人間関係を徹底的に描出する。"
            "中国初の文人個人作・市民写実小説として『紅楼夢』に直接影響を与え、"
            "東アジア小説リアリズムの起点となった。"
        ),
        background="水滸伝の武松・潘金蓮挿話を起点に、明末の都市文化を独自展開した文人作。",
        development="張竹坡評本（清初）、『紅楼夢』への直接影響、東アジア風俗小説の祖型。",
        historical_context="明末の商業資本主義発達と倫理崩壊への批判的観察。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185664",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="儒林外史", name_en="The Scholars",
        name_original="儒林外史", original_script="kanji",
        period_id=P_QING,
        definition=(
            "呉敬梓（1701-1754）作の56回の諷刺小説。"
            "明代を舞台に科挙制度に翻弄される儒者群像（范進中挙・厳監生臨終の二指等）を"
            "風刺的に描き、清代知識人社会の虚偽と功利を批判する。"
            "中国諷刺小説の頂点として確立し、近現代の魯迅『阿Q正伝』等の社会批判文学の祖型となる。"
        ),
        background="呉敬梓自身の科挙挫折・没落士人体験。",
        development="魯迅『中国小説史略』が「中国諷刺小説」ジャンルを確立、清末譴責小説の源流。",
        historical_context="清代雍正乾隆期の科挙制度の硬直化と士人精神の倦怠。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185665",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="紅楼夢「真事隠 假語存」", name_en="Hongloumeng's truth-fiction principle",
        name_original="紅樓夢「真事隱、假語存」", original_script="kanji",
        period_id=P_QING,
        definition=(
            "曹雪芹（1715頃-1763頃）『紅楼夢』第一回の自序的命題。"
            "「将真事隠去、用假語村言敷演出来」（真の事を隠し、仮の語・村言で敷衍する）。"
            "甄士隠（真事隠）と賈雨村（仮語存）の人名を含意とし、"
            "歴史的真実と虚構の関係を語る東アジア小説論最高の自己言及的命題。"
            "曹家家族史の「隠された真実」と虚構の二重構造を読者に示唆する。"
        ),
        background="曹雪芹自身の曹家凋落体験を「真事」として隠匿しつつ「仮語」で語り直した自伝性。",
        development="脂硯斎評語、近代紅学（胡適・周汝昌等）の自伝説考証へと展開。",
        historical_context="清代雍正期の曹家粛清と雪芹自身の没落体験。",
        primary_source_url="https://ctext.org/hongloumeng",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("真正性", "rethinking",
             "「真事隠 假語存」は虚構と真実の境界を意図的に曖昧化する自己言及命題。"
             "AI生成コンテンツでは「真」と「仮」の境界が制度的に消失し、"
             "曹雪芹の問題提起が新次元で再来する。",
             "AIフェイクとフィクション・ハルシネーション・自伝性の真正性論争"),
            ("物語", "rethinking",
             "メタ的な虚実論を物語内に埋め込む自己言及構造は、"
             "AI時代の物語生成における「これは小説か事実か」問題と直結する。",
             "AI生成自伝・パラフィクション・モックメンタリー")],
        cross=[("PHIL", None, "fact-fiction boundary", "parallel",
                "西洋認識論の真理 vs 虚構問題と並走する東アジア小説学的命題")],
    ))

    records.append(dict(
        name_ja="紅楼夢「夢」と現実", name_en="Hongloumeng's dream-reality structure",
        name_original="紅樓夢之「夢」與現實", original_script="kanji",
        period_id=P_QING,
        definition=(
            "『紅楼夢』全編を貫通する「太虚幻境」「金陵十二釵」「太虚警幻仙姑」"
            "等の夢中世界と賈府現実世界の二重構造。"
            "賈宝玉の夢遊太虚幻境（第五回）で運命が予示され、"
            "現実崩壊後に夢が真実だったと判明する反転構造。"
            "「假作真時真亦假、無為有処有還無」（仮を真とすれば真もまた仮、"
            "無為有処に有もまた無）の対聯が全編の認識論的核心命題。"
        ),
        background="仏教（華厳・唯識）と道教（『荘子』胡蝶夢）の夢思想を統合した認識論的小説構造。",
        development="現代紅学の哲学的解釈、東アジア「夢の文学」（漱石『夢十夜』等）への影響。",
        historical_context="清代乾隆期の三教合一的世界観と没落士人の存在論的不安。",
        primary_source_url="https://ctext.org/hongloumeng",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PHIL", None, "dream-reality philosophy", "parallel",
                "荘子胡蝶夢・仏教唯識・西洋デカルト懐疑等を統合する小説的展開")],
    ))

    # ============================================================
    # D. 詩学・批評（8件）
    # ============================================================
    records.append(dict(
        name_ja="滄浪詩話 厳羽「妙悟」", name_en="Yan Yu's miaowu (sublime enlightenment)",
        name_original="滄浪詩話嚴羽「妙悟」", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "南宋・厳羽（13世紀前半）『滄浪詩話』が打ち出した詩学中核概念。"
            "「禅道唯在妙悟、詩道亦在妙悟」（禅道は妙悟にあり、詩道もまた妙悟にあり）。"
            "禅の頓悟になぞらえ、詩の本質は概念分析でなく直観的体得にあるとし、"
            "盛唐詩を「第一義」と最高位に置いて宋代の議論詩・学問詩を批判した。"
            "東アジア詩学における直観主義の頂点で、王士禎神韻説の直接源流となる。"
        ),
        background="禅宗（特に臨済宗）の影響下、南宋の議論詩過剰への反動として成立。",
        development="明代復古派、清代王士禎の神韻説、日本の松尾芭蕉の「不易流行」論にまで影響。",
        historical_context="南宋の禅宗文化と詩学の精神論的深化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89438",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[
            ("受容", "rethinking",
             "妙悟は概念的分析を超える直観的詩理解を要請する。"
             "AIによる詩の意味解析（注釈・タグ付け）では捉えられない次元として、"
             "AI解釈の限界を予示している。",
             "LLM文学解釈の限界・AI批評の概念化問題"),
            ("創造性", "partial",
             "妙悟による創作論は、ルール・パターンを超える直観的把握を創造性の核心とする。"
             "AIの統計的パターン学習に対する東アジア的反論として再評価される。",
             "AI創造性論争・パターン学習を超えた創造性")],
        cross=[("PHIL", None, "Chan Buddhism epistemology", "parallel",
                "禅宗の頓悟と詩学の融合、東アジア独自の直観的認識論")],
    ))

    records.append(dict(
        name_ja="詩家三昧", name_en="poetic samadhi",
        name_original="詩家三昧", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "厳羽『滄浪詩話』中の概念。仏教三昧（深い精神集中状態）になぞらえ、"
            "詩人が詩境に入る最高度の精神的没入を指す。「読盛唐人詩」"
            "（盛唐人の詩を読む）こそ三昧の入門であるとし、模倣ではなく"
            "対象との一体化的理解を重視した。後の王士禎神韻説の精神論的源流。"
        ),
        background="厳羽の禅参・滄浪詩話の理論基盤。",
        development="明清の詩家が詩境理論として継承、現代の文学体験論にまで響く。",
        historical_context="南宋禅宗文化と詩境理論の精神論化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89438",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="神韻説", name_en="shenyun (spirit-resonance) theory",
        name_original="神韻說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清初の王士禎（1634-1711、号阮亭・漁洋山人）が体系化した詩学説。"
            "「神韻」とは詩の言外の韻味・余情・含蓄であり、王孟・韋柳の山水田園詩を"
            "範とし、禅の悟りと詩境を結合する。明代厳羽妙悟・司空図二十四詩品を直接継承し、"
            "格調説・性霊説・肌理説と並ぶ清代四詩派の一として詩壇を主導した。"
        ),
        background="厳羽『滄浪詩話』、司空図『二十四詩品』、明末の禅悦詩風を直接源流とする。",
        development="清中期に格調・性霊・肌理諸派と論争、近代の純粋詩論に影響。",
        historical_context="清初の文化的安定と禅宗的詩学の主流化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185666",
        primary_source_type="classical_text",
        importance_score=5, source_tier="primary", canonical_in_region="core",
        fourth_tags=[],
        cross=[("PT", None, "ineffability theory", "parallel",
                "西欧 ineffabilityや余白概念に対応する東アジア言外論")],
    ))

    records.append(dict(
        name_ja="格調説", name_en="gediao (form-tone) theory",
        name_original="格調說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代の沈徳潜（1673-1769）が体系化した詩学説。"
            "「格」（風格・体格）と「調」（音調・気調）を詩の本質と見なし、"
            "漢魏盛唐詩を最高範例とする復古的詩観。明代前後七子の擬古論を継承し、"
            "性霊派・神韻派と論争を展開した。『古詩源』『唐詩別裁集』等のアンソロジーで"
            "清代詩学教育の標準を形成した。"
        ),
        background="明代前後七子の復古論を清代に再構築、王士禎神韻説への反動。",
        development="清代科挙詩学の基準となり、近代以降の「古典派」概念の祖型。",
        historical_context="清代乾隆期の文化保守化と古典再規範化。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185667",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("PT", None, "neoclassicism", "parallel",
                "西欧新古典主義に対応する東アジア復古論")],
    ))

    records.append(dict(
        name_ja="性霊説（袁枚）", name_en="Yuan Mei's xingling theory",
        name_original="性靈說（袁枚）", original_script="kanji",
        period_id=P_QING,
        definition=(
            "袁枚（随園）の主著『随園詩話』に体系化された詩学説。"
            "「詩を作るには性情を主と為すべし、その次は格律」を中核とし、"
            "個人の率直な感情・天性表現を最高価値とする。"
            "明代公安派性霊論を継承しつつ、女性弟子（随園女弟子）を多数育てた点で"
            "中国詩学史上画期的、近代個人主義的文学観の先駆。"
            "（カテゴリBの「性霊説」と区別し、袁枚個人の詩論として独立項目化。）"
        ),
        background="清代乾隆期の文人趣味と袁枚自身の自由放任的人生観。",
        development="近代以降の個性表現論、五四新文学の自我主義的詩風に直結。",
        historical_context="清代盛世の文人サロン文化と科挙文学への倦怠。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89522",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="肌理説", name_en="jili (substance-pattern) theory",
        name_original="肌理說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清代の翁方綱（1733-1818）が打ち出した詩学説。"
            "「肌理」（皮膚の紋理）の比喩で「義理」（思想内容）と「文理」（文章組織）の"
            "緊密な織り合いを詩の本質と見なす。考証学の精緻な実証主義を詩学に持ち込み、"
            "神韻説の空疎・性霊説の率直に対する補完論として機能した。"
            "清代乾嘉学術と詩学の融合点となる。"
        ),
        background="清代乾嘉考証学の隆盛と翁方綱自身の金石碑学的素養。",
        development="清末の同光体詩風（学問詩復興）に影響、近代詩学批評の素地。",
        historical_context="清代考証学と詩学批評の制度的接続。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185668",
        primary_source_type="classical_text",
        importance_score=4, source_tier="primary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="比興六義 後代展開", name_en="bixing-liuyi later development",
        name_original="比興六義後代展開", original_script="kanji",
        period_id=P_QING,
        definition=(
            "詩経六義（風・雅・頌・賦・比・興）の宋元明清における理論的展開。"
            "宋代朱熹『詩集伝』が比興を「託物言志」（物に託して志を述べる）として再定義し、"
            "清代常州詞派の張惠言が詞批評に「比興寄託」論を移植、"
            "詞・小説・戯曲への寓意的解釈の根拠となった。"
            "東アジアにおける比喩・寓意・暗喩の理論的中核として連続発展した概念。"
        ),
        background="毛詩序の比興論を朱熹『詩集伝』が新儒教的に再構築。",
        development="清代常州詞派・桐城派古文論・近代修辞学にまで影響を継続的に与える。",
        historical_context="宋代理学興隆から清代考証学までの儒教詩学の連続。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185669",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="詩話の体系化", name_en="systematization of shihua (poetry talk)",
        name_original="詩話之體系化", original_script="kanji",
        period_id=P_QING,
        definition=(
            "宋代欧陽脩『六一詩話』に始まる「詩話」（詩に関する随筆的批評）が、"
            "宋元明清を通じて発展し、清代に何文煥『歴代詩話』、"
            "丁福保『歴代詩話続編』等の集成によりジャンルとして確立した過程。"
            "短評・逸話・考証・体系論が混淆する東アジア独自の批評形式で、"
            "西欧の体系的詩学（poetics）と並走しつつも全く異なる文体を発展させた。"
        ),
        background="宋代の文人筆記・随筆文化の発展と詩学批評の口承化。",
        development="清末民初の伝統詩話刊行ブームと近代文学史記述の素材化。",
        historical_context="宋以降の文人サークル・印刷出版業・批評共同体の発達。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=89436",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("PT", None, "criticism genre", "parallel",
                "西欧 poetics・aesthetics に対応する東アジア独自の批評ジャンル形式")],
    ))

    # ============================================================
    # E. 主題・メタ概念（8件）
    # ============================================================
    records.append(dict(
        name_ja="擬古 vs 創新", name_en="imitation vs innovation",
        name_original="擬古對創新", original_script="kanji",
        period_id=P_MING,
        definition=(
            "明清詩学を貫く根本的二項対立。明代前後七子（李夢陽・李攀龍ら）の"
            "「文必秦漢、詩必盛唐」（文は必ず秦漢、詩は必ず盛唐）の擬古論と、"
            "公安派・竟陵派・性霊派の「独抒性霊」創新論の対立として展開した。"
            "東アジア文学における伝統と革新の方法論的緊張を理論化した最大の論争軸。"
        ),
        background="明代中期の文学標準化要求と個人表現要求の対立。",
        development="清代の格調 vs 性霊派論争に継承、五四新文学運動「打倒孔家店」の遠因。",
        historical_context="明清の文人サロン・出版文化・科挙文学制度。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185670",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[
            ("創造性", "rethinking",
             "擬古は古典に基づく再構成、創新はゼロからの独創を理想とする。"
             "AIの事前学習＋プロンプトは構造的に擬古的方法論であり、"
             "「創新」概念そのものを根本から問い直す。",
             "LLM事前学習・プロンプト工学・AI創作の擬古的構造")],
        cross=[("PT", None, "imitation-innovation", "parallel",
                "西欧 imitatio vs originality に対応する東アジア最大の論争軸")],
    ))

    records.append(dict(
        name_ja="文人画と詩の融合", name_en="literati painting and poetry fusion",
        name_original="文人畫與詩之融合", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "宋元明清の文人画論で発展した「詩画一律」（詩と絵は同じ法則）の理念。"
            "蘇軾「詩中有画、画中有詩」（王維評）に端を発し、"
            "元代趙孟頫・倪瓚以降「題画詩」が文人画の不可欠要素となった。"
            "詩・書・画・印の四位一体的総合芸術として、東アジア独自の"
            "ジャンル横断的「文人」アイデンティティを成立させた中核理念。"
        ),
        background="蘇軾・米芾の宋代士大夫画論、元代南宗山水の隆盛。",
        development="明代呉派（沈周・文徴明）、清代四王・揚州八怪へと連続発展、日本の南画にも伝播。",
        historical_context="宋代以降の士大夫文化の総合芸術志向。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185671",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("AN", None, "literati identity", "parallel",
                "東アジア士大夫文化の総合芸術アイデンティティ")],
    ))

    records.append(dict(
        name_ja="隠逸 vs 経世", name_en="reclusion vs governance",
        name_original="隱逸對經世", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "宋元明清を貫く文人の根本的選択軸。「経世済民」（世を治め民を救う、"
            "范仲淹「先憂後楽」）と「隠逸退避」（山林に隠れる、陶淵明型）の対極的志向。"
            "明清転換期（明遺民）に最も先鋭化し、顧炎武・王夫之・黄宗羲ら清初思想家の"
            "選択（仕えるか隠れるか）として歴史的決断を迫られた。"
            "C13『出処』『隠逸』の宋以降展開として、より社会的・政治的次元に深化。"
        ),
        background="北宋范仲淹「以天下為己任」と陶淵明的隠逸の二大伝統の継続的緊張。",
        development="明清交替期の士人選択、近代以降の知識人の社会参加 vs 退避論争へ連続。",
        historical_context="王朝交代期の士人個人選択と倫理的責任。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185672",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("AN", None, "scholar-official identity", "parallel",
                "東アジア士大夫の二極アイデンティティ")],
    ))

    records.append(dict(
        name_ja="才子佳人小説", name_en="scholar-beauty romance",
        name_original="才子佳人小說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "清初に流行した文人と美人の恋愛・結婚を主題とする中編小説ジャンル。"
            "『玉嬌梨』『平山冷燕』『好逑伝』等が代表作。"
            "詩才を媒介とする恋愛、才学による試練、最終的な科挙合格と結婚という"
            "定型的プロットを持ち、明代金瓶梅以来の世情小説に対する理想化的反動として成立。"
            "後の『紅楼夢』が直接批判した同時代的小説ジャンル。"
        ),
        background="清初の都市文人生活と科挙挫折者の恋愛幻想。",
        development="日本江戸読本、朝鮮の漢文小説に翻案され、東アジア共通の恋愛小説型となる。",
        historical_context="清初の文化的安定と文人サロン化恋愛趣味。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185673",
        primary_source_type="reference_work",
        importance_score=3, source_tier="secondary", canonical_in_region="minor",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="諷刺小説", name_en="satirical novel",
        name_original="諷刺小說", original_script="kanji",
        period_id=P_QING,
        definition=(
            "明清に発展した社会批判的小説ジャンル。"
            "『儒林外史』を頂点として清末の譴責小説『官場現形記』『二十年目睹之怪現状』"
            "『老残遊記』『孽海花』に至る系譜を形成。"
            "魯迅『中国小説史略』により独立ジャンルとして概念化され、"
            "近現代中国の社会批判文学（魯迅・銭鍾書『囲城』等）の祖型となった。"
        ),
        background="明末清初の社会矛盾激化と章回小説の成熟。",
        development="清末譴責小説、五四新文学魯迅諷刺、現代華語社会派小説まで連続。",
        historical_context="明清の社会批判意識と科挙制度動揺。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185674",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[],
    ))

    records.append(dict(
        name_ja="志怪 vs 伝奇 後代", name_en="zhiguai vs chuanqi later development",
        name_original="志怪對傳奇後代", original_script="kanji",
        period_id=P_QING,
        definition=(
            "六朝志怪・唐代伝奇の二大短編伝統が、明清にどう継承・分化したかという系譜。"
            "明代瞿佑『剪灯新話』、清代蒲松齢『聊斎志異』が伝奇系の頂点を、"
            "紀昀『閲微草堂筆記』、袁枚『子不語』が志怪系の頂点を形成した。"
            "聊斎は伝奇の修辞美と志怪の超自然主題を融合し、東アジア怪異文学の最高峰となる。"
            "日本上田秋成『雨月物語』、現代怪談・ホラー文学にまで影響を波及させる。"
        ),
        background="六朝志怪・唐代伝奇の二大短編伝統の明清的継承と分化。",
        development="日本の怪奇小説（秋成・鏡花）、現代華語怪奇文学（莫言『蛙』等）への影響。",
        historical_context="明清の都市怪奇趣味・民間信仰興隆。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185675",
        primary_source_type="reference_work",
        importance_score=4, source_tier="secondary", canonical_in_region="major",
        fourth_tags=[],
        cross=[("Myth-Narratives", None, "supernatural narrative", "parallel",
                "東アジア独自の超自然短編伝統と現代怪奇文学への系譜")],
    ))

    records.append(dict(
        name_ja="集句詩", name_en="jiju shi (cento poetry)",
        name_original="集句詩", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "他者の既存詩句を組み合わせて新たな詩を構成する詩体。"
            "宋代王安石が体系化、文天祥『集杜詩』（杜甫詩のみで構成、200首）で頂点に達する。"
            "西欧の cento と独立に発達した東アジア独自の引用・モンタージュ詩法であり、"
            "完全に既存テキストの再配置のみで創造性を発揮するメタ文学的実験。"
        ),
        background="宋代の典故重視と詩学技巧化の極致として誕生。",
        development="明清に文人遊戯詩として継続、近代の詩学解体的実験詩への先駆性が再評価。",
        historical_context="宋代以降の知識集積化文化と典故活用詩風。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185676",
        primary_source_type="reference_work",
        importance_score=3, source_tier="secondary", canonical_in_region="minor",
        fourth_tags=[
            ("創造性", "rethinking",
             "集句詩は既存テキストの再配置のみで詩的価値を生む。"
             "AIの統計的次トークン予測も既存テキストの再構成と構造的に類似し、"
             "「再配置による創造性」のラディカルな先例を提供する。",
             "LLM生成の構造的本質・テキスト再配置・引用ベース創作")],
        cross=[("PT", None, "cento", "parallel",
                "西欧 cento poetry に対応する東アジア独自の集句伝統")],
    ))

    records.append(dict(
        name_ja="書院文学", name_en="academy literature",
        name_original="書院文學", original_script="kanji",
        period_id=P_SONG,
        definition=(
            "宋以降の書院（民間学術アカデミー、白鹿洞書院・嶽麓書院等）を場として"
            "成立した師生・友朋間の文学交流。朱熹・陸九淵らの講学、講会、師弟和韻、"
            "書院記等が含まれる。科挙的科挙詩文と異なる、共同体的・対話的・"
            "教学的文学のジャンル群を形成し、東アジアの「学問共同体としての文学」"
            "という独自伝統を成立させた。"
        ),
        background="北宋以降の書院興隆と理学共同体的学習文化。",
        development="明清の社・盟・詩社ネットワーク、近代以降の同人結社・大学文学グループへ連続。",
        historical_context="宋代以降の民間学術ネットワークと士大夫アイデンティティ。",
        primary_source_url="https://ctext.org/wiki.pl?if=gb&res=185677",
        primary_source_type="reference_work",
        importance_score=3, source_tier="secondary", canonical_in_region="minor",
        fourth_tags=[],
        cross=[("AN", None, "scholarly community", "parallel",
                "東アジア書院・学派文化と西欧 academy 文化の比較対象")],
    ))

    return records


# ----------------------------------------------------------------
# 投入処理
# ----------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("LIT-DB Phase 2 Wave 4 C14: 中国古典文学（宋元明清）40概念")
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
            def cid_of(name: str) -> int:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE name_ja=? AND region='東アジア'",
                    (name,),
                ).fetchone()
                if not row:
                    raise RuntimeError(f"concept not found: {name}")
                return row["id"]

            relations_data = [
                # 江西詩派系譜
                ("点鉄成金", "江西詩派", "extends",
                 "黄庭堅の点鉄成金論が江西詩派の方法論的中核"),
                ("夺胎换骨", "江西詩派", "extends",
                 "黄庭堅の夺胎换骨論も江西詩派の方法論的中核"),
                ("黄庭堅 江西詩学体系", "江西詩派", "introduced_by",
                 "黄庭堅の詩学体系が江西詩派の理論的基礎"),
                # 宋詩内系譜
                ("以詩為文", "蘇軾「以詩為文・以文為詩」総合", "extends",
                 "蘇軾の双方向的文体実践は『以詩為文』の発展形"),
                ("以文為詩", "蘇軾「以詩為文・以文為詩」総合", "extends",
                 "蘇軾の双方向的文体実践は『以文為詩』の発展形"),
                ("江西詩派", "楊万里誠斎体", "criticizes",
                 "誠斎体は江西詩派の典故重視に対する内部批判"),
                # 詞二派
                ("李清照婉約詞", "辛棄疾豪放詞", "criticizes",
                 "婉約 vs 豪放は宋詞の二大対立で並列的批評関係"),
                # 元曲系譜
                ("元曲（雑劇）", "関漢卿『竇娥冤』", "exemplifies",
                 "竇娥冤は元雑劇の代表作"),
                ("元曲（雑劇）", "王実甫『西廂記』", "exemplifies",
                 "西廂記は元雑劇の最高傑作"),
                # 章回小説系譜
                ("章回小説", "三国演義", "exemplifies",
                 "三国演義は章回小説四大奇書の一"),
                ("章回小説", "水滸伝", "exemplifies",
                 "水滸伝は章回小説四大奇書の一"),
                ("章回小説", "西遊記", "exemplifies",
                 "西遊記は章回小説四大奇書の一"),
                ("章回小説", "金瓶梅", "exemplifies",
                 "金瓶梅は章回小説四大奇書の一"),
                ("章回小説", "儒林外史", "exemplifies",
                 "儒林外史は清代章回小説の頂点の一"),
                ("金瓶梅", "紅楼夢「真事隠 假語存」", "precedes",
                 "金瓶梅の市民写実が紅楼夢のリアリズムに直接影響"),
                ("紅楼夢「真事隠 假語存」", "紅楼夢「夢」と現実", "extends",
                 "真事仮語の二項対立が夢現実構造として全編に展開"),
                ("儒林外史", "諷刺小説", "introduced_by",
                 "儒林外史が諷刺小説ジャンル成立の起点"),
                # 詩学派論争
                ("滄浪詩話 厳羽「妙悟」", "詩家三昧", "contains",
                 "詩家三昧は滄浪詩話中の核心概念"),
                ("滄浪詩話 厳羽「妙悟」", "神韻説", "precedes",
                 "厳羽妙悟が王士禎神韻説の直接源流"),
                ("公安派", "性霊説", "precedes",
                 "公安派性霊論が清代袁枚性霊説の直接源流"),
                ("公安派", "性霊説（袁枚）", "precedes",
                 "公安派が袁枚性霊説の直接的祖型"),
                ("性霊説", "性霊説（袁枚）", "extends",
                 "袁枚性霊説はカテゴリBの性霊説（清代総体）の核心個別事例"),
                ("神韻説", "格調説", "criticizes",
                 "格調説は神韻説の空疎を批判して成立"),
                ("格調説", "性霊説", "criticizes",
                 "性靈派 vs 格調派は清代詩壇最大の対立"),
                ("性靈派 vs 格調派", "性霊説", "contains",
                 "性霊説が性靈派 vs 格調派論争の一極"),
                ("性靈派 vs 格調派", "格調説", "contains",
                 "格調説が性靈派 vs 格調派論争の一極"),
                ("肌理説", "神韻説", "criticizes",
                 "肌理説は神韻説の空疎・性霊説の率直に対する補完論として成立"),
                # 主題系譜
                ("隠逸", "隠逸 vs 経世", "extends",
                 "隠逸概念の宋以降社会的展開"),
                ("出処", "隠逸 vs 経世", "extends",
                 "出処論の宋以降政治化展開"),
                # 諷刺小説と才子佳人
                ("才子佳人小説", "紅楼夢「真事隠 假語存」", "criticizes",
                 "紅楼夢序が才子佳人小説の定型を批判して書かれた"),
                # 比興六義の連続
                ("比", "比興六義 後代展開", "extends",
                 "C13比概念の宋元明清的継続展開"),
                ("興", "比興六義 後代展開", "extends",
                 "C13興概念の宋元明清的継続展開"),
                # 擬古 vs 創新
                ("公安派", "擬古 vs 創新", "exemplifies",
                 "公安派は明代創新派の最重要事例"),
                ("桐城派", "擬古 vs 創新", "exemplifies",
                 "桐城派は古文擬古派の頂点事例"),
                # 集句詩
                ("点鉄成金", "集句詩", "extends",
                 "点鉄成金的方法を完全に既存テキストのみで実現したのが集句詩"),
                # 詩話
                ("滄浪詩話 厳羽「妙悟」", "詩話の体系化", "exemplifies",
                 "滄浪詩話は詩話ジャンルの代表事例"),
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
            print(f"  {r['axis']:8s} | {r['status']:11s} | {r['c']}")


if __name__ == "__main__":
    main()
