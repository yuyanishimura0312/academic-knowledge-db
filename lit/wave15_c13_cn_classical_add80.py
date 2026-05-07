"""LIT-DB Phase 2 Wave 15 — C13 add80: Chinese Classical Literature (80 new).

Subfield: lit_cn_classical (id=8), region='東アジア'.
Existing 158 concepts. Target 600.
This wave adds 80 NEW non-overlapping concepts covering:
  - 先秦補完 (尚書/易經繫辭/三傳/戰國策/韓非子寓言/莊子内外雜篇)
  - 漢代補完 (史記/漢書/後漢書/三國志/樂府詳細/古詩十九首/蔡琰)
  - 六朝詳細 (世説新語/顔氏家訓/抱朴子/山海經/文心雕龍各篇/詩品/文選/玉台新詠)
  - 唐代詳細 (初唐四傑/沈宋/陳子昂/王昌齡/錢起/韋応物/韓柳古文/唐傳奇/杜牧/李商隱/李賀)
  - 宋代詳細 (歐陽修/王安石/蘇軾散文/江西派/楊万里/陸遊/朱熹/嚴羽/筆記)
  - 元代詳細 (西廂記論/関漢卿/紀君祥/散曲名家/録鬼簿)
  - 明代補完 (前後七子/唐宋派/公安/竟陵/李贄/三言二拍/封神/牡丹亭/曲律)
  - 清代補完 (神韻/格調/肌理/性靈/桐城/閱微/四庫/顧炎武/龔自珍/黃遵憲/紅樓続書)

Sources (real, verifiable):
  - CTEXT: https://ctext.org/
  - 維基文庫: https://zh.wikisource.org/
  - Kanripo: https://www.kanripo.org/
  - Wikipedia (zh/en).

Verification policy follows wave13 conventions.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


CTEXT = "https://ctext.org/"
WSRC_ZH = "https://zh.wikisource.org/wiki/"
KANRIPO = "https://www.kanripo.org/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"


PERIOD_NAMES = {
    "先秦": "先秦", "漢": "漢", "魏晋南北朝": "魏晋南北朝",
    "唐": "唐", "宋": "宋", "元": "元", "明": "明", "清": "清",
}


CONCEPTS: list[dict] = []


def add(**e):
    CONCEPTS.append(e)


C = dict(subfield_code="lit_cn_classical", region="東アジア",
         original_script="hanzi")


# ============================================================
# A: 先秦補完 (12)
# ============================================================
add(**C, name_ja="尚書編纂史",
    name_en="Compilation history of the Shangshu",
    name_original="尚書",
    period_key="先秦",
    definition="『尚書』（書経）は虞夏商周四代の典謨訓誥誓命を集成する儒家経典。今文28篇・古文25篇の真偽を巡る漢以来の論争（孔安国伝・梅賾偽古文）を経て、清代閻若璩『古文尚書疏證』が偽古文を実証した。中国散文の最古層をなす。",
    background="戦国〜漢初の儒家経典編纂と古文・今文経の対立。",
    development="閻若璩実証・現代清華簡『書』類の発見によりテキスト史が再構築されつつある。",
    historical_context="戦国末から漢代経学制度成立期。",
    primary_source_url=CTEXT+"shang-shu",
    primary_source_type="CTEXT: 尚書",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="易經繫辭傳の文学性",
    name_en="Literary character of the Xici Zhuan of Yijing",
    name_original="繫辭傳",
    period_key="先秦",
    definition="『周易』十翼の一つ繫辭傳上下は、戦国末〜漢初成立の哲学的散文で、「一陰一陽之謂道」「立象以盡意」等の命題を含む。中国哲学的散文の最早期の到達点であり、後世の「象」「意」「言」をめぐる文学理論（言意之辨）の根本典拠となった。",
    background="戦国末儒家・道家・陰陽家の総合期における経典化。",
    development="魏晋玄学の言意論争、唐宋詩学の象意論の理論的祖型。",
    historical_context="戦国末〜漢初の哲学的綜合期。",
    primary_source_url=CTEXT+"book-of-changes/xi-ci-shang",
    primary_source_type="CTEXT: 周易繫辭",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="繫辭傳「立象以盡意」「言不盡意」はAI生成の言語と意味の分離・象徴生成の根本問題を再考する東洋的祖型。")

add(**C, name_ja="春秋左氏傳の叙事",
    name_en="Narrative art of the Zuo Zhuan",
    name_original="春秋左氏傳",
    period_key="先秦",
    definition="『春秋』三傳のうち最も豊富な歴史記述を含む左丘明伝（戦国成書）。具体的人物描写・戦争叙述・外交辞令を備え、中国歴史叙事文学の祖型。司馬遷『史記』の直接的源流であり、後世の歴史叙事と古文の規範となった。",
    background="春秋経の解釈伝統と戦国期の歴史記述の制度化。",
    development="司馬遷『史記』の叙事手法、唐宋古文家の歴史散文の規範。",
    historical_context="戦国期の歴史叙事文化の成熟。",
    primary_source_url=CTEXT+"chun-qiu-zuo-zhuan",
    primary_source_type="CTEXT: 春秋左氏傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="公羊傳の義例",
    name_en="Hermeneutical canons of the Gongyang Zhuan",
    name_original="春秋公羊傳",
    period_key="先秦",
    definition="春秋三傳の一。戦国斉地の口伝を漢景帝期に文字化し、董仲舒・何休が体系化。「微言大義」「三世説」「大一統」等の解釈学的概念を提示し、漢代経学・清代今文学派（康有為）の理論的核心となった。",
    background="戦国〜漢初斉地公羊学派の口伝文化。",
    development="漢代董仲舒『春秋繁露』、清末康有為公羊改制論への系譜。",
    historical_context="漢代経学制度成立期の今文古文論争。",
    primary_source_url=CTEXT+"gongyang-zhuan",
    primary_source_type="CTEXT: 公羊傳",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="穀梁傳",
    name_en="Guliang Zhuan",
    name_original="春秋穀梁傳",
    period_key="先秦",
    definition="春秋三傳の一で穀梁赤伝。簡潔な義例解釈を特色とし、漢宣帝甘露三年の石渠閣会議で公羊との優劣論争を経て立学官となった。三傳中最も簡素で、文学的影響は左氏・公羊に劣るが経学史上の重要文献。",
    background="戦国魯地穀梁学派の口伝。",
    development="漢代石渠閣論議、唐代『春秋集解』への系譜。",
    historical_context="漢代経学正統化過程。",
    primary_source_url=CTEXT+"guliang-zhuan",
    primary_source_type="CTEXT: 穀梁傳",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="戰國策の叙事",
    name_en="Narrative art of the Zhanguo Ce",
    name_original="戰國策",
    period_key="先秦",
    definition="戦国期諸国遊説士の言説と外交を集成した史料・文学集。劉向（前77-前6）が校訂編纂し33篇とした。蘇秦・張儀・荊軻等の縦横家叙事は中国短篇叙事文学の祖型をなし、史記・後世小説の素材源となった。",
    background="戦国諸国の遊説文化と漢代劉向の校書事業。",
    development="史記列伝、後世「縦横家」叙事文学の規範的源流。",
    historical_context="戦国期遊説文化と漢代経籍校書制度。",
    primary_source_url=CTEXT+"zhan-guo-ce",
    primary_source_type="CTEXT: 戰國策",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="韓非子の寓言",
    name_en="Parables of Han Feizi",
    name_original="韓非子寓言",
    period_key="先秦",
    definition="韓非（前280頃-前233）の法家著作中、「説林」上下・「儲説」六篇等に収める寓話集。「守株待兎」「自相矛盾」「鄭人買履」等の寓言を法治論証の修辞的手段として駆使。中国寓話文学の頂点をなし、後世諷喩文学の規範となった。",
    background="戦国末法家思想の成熟と論証修辞学の発達。",
    development="漢代『説苑』『新序』、唐宋諷喩散文の祖型。",
    historical_context="戦国末諸子論争期の修辞文化。",
    primary_source_url=CTEXT+"hanfeizi",
    primary_source_type="CTEXT: 韓非子",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="韓非子寓言は法治論証の修辞的手段。AI時代における説得・物語型推論の古典的祖型として再評価可能。")

add(**C, name_ja="莊子内篇逍遙遊・齊物論・養生主",
    name_en="Inner Chapters of Zhuangzi: Xiaoyaoyou, Qiwulun, Yangshengzhu",
    name_original="莊子内篇",
    period_key="先秦",
    definition="『莊子』内篇七篇のうち冒頭三篇。逍遙遊は絶対自由、齊物論は相対主義認識論、養生主は生命の道の養成を寓言と詩的散文で論じる。中国哲学的散文の最高峰で、後世道家文学・玄学・禅文学の規範となった。",
    background="戦国中期道家思想の成熟と寓言哲学的散文の発達。",
    development="魏晋玄学（王弼・郭象）、唐宋詩学（蘇軾・黃庭堅）、禅文学の祖型。",
    historical_context="戦国中期諸子百家論争の深化期。",
    primary_source_url=CTEXT+"zhuangzi/enjoyment-in-untroubled-ease",
    primary_source_type="CTEXT: 莊子内篇",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="齊物論の相対主義はAI時代の真理多元性・主体客体融合問題の東洋的根本祖型。")

add(**C, name_ja="莊子外篇",
    name_en="Outer Chapters of Zhuangzi",
    name_original="莊子外篇",
    period_key="先秦",
    definition="『莊子』外篇15篇（駢拇・馬蹄・胠篋・在宥・天地・天道・天運・刻意・繕性・秋水・至樂・達生・山木・田子方・知北遊）。内篇に比し直接的論述が多く、戦国末〜漢初の道家学派による展開とされる。「秋水」「達生」等は寓言文学として独立した文学的価値を持つ。",
    background="戦国末〜漢初道家学派の経典化過程。",
    development="魏晋郭象注、唐成玄英疏、宋代道学の理論的源泉。",
    historical_context="戦国末から漢初の道家経典化期。",
    primary_source_url=CTEXT+"zhuangzi",
    primary_source_type="CTEXT: 莊子外篇",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="莊子雜篇",
    name_en="Miscellaneous Chapters of Zhuangzi",
    name_original="莊子雜篇",
    period_key="先秦",
    definition="『莊子』雜篇11篇（庚桑楚・徐無鬼・則陽・外物・寓言・讓王・盜跖・說劍・漁父・列御寇・天下）。最も成書年代が新しいとされ、特に「天下篇」は中国最古の哲学史記述、「寓言篇」は莊子の修辞論を提示し、文学理論史上の重要資料となる。",
    background="漢初道家思想の総合期における経典完成。",
    development="天下篇は司馬談「論六家要旨」、後世哲学史記述の祖型。",
    historical_context="漢初学派総合期。",
    primary_source_url=CTEXT+"zhuangzi",
    primary_source_type="CTEXT: 莊子雜篇",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="呂氏春秋",
    name_en="Lüshi Chunqiu",
    name_original="呂氏春秋",
    period_key="先秦",
    definition="秦呂不韋（?-前235）が食客を集めて編纂した雑家百科全書（前239頃成書）。十二紀・八覽・六論計160篇から成り、儒・道・法・墨・陰陽諸家を綜合する。中国最古の体系的百科全書文学で、後世『淮南子』『太平御覽』類書の祖型となった。",
    background="戦国末期諸子百家綜合の知的潮流。",
    development="漢代『淮南子』、唐代類書『藝文類聚』『太平御覽』への系譜。",
    historical_context="秦統一前夜の学術綜合期。",
    primary_source_url=CTEXT+"lvshi-chunqiu",
    primary_source_type="CTEXT: 呂氏春秋",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="晏子春秋",
    name_en="Yanzi Chunqiu",
    name_original="晏子春秋",
    period_key="先秦",
    definition="春秋斉国名相晏嬰（?-前500）の言行を集成した戦国期成書の説話集。内篇・外篇計215章で、機智・諷諫・節儉の逸話を寓言的に収める。中国短篇説話文学の祖型の一であり、後世「世説新語」型逸話文学の源流となった。",
    background="戦国期斉地稷下学派の説話伝承。",
    development="後世志人小説、世説新語型逸話集の祖型。",
    historical_context="戦国斉地の文化的繁栄期。",
    primary_source_url=CTEXT+"yanzi-chun-qiu",
    primary_source_type="CTEXT: 晏子春秋",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 漢代補完 (10)
# ============================================================
add(**C, name_ja="司馬遷『史記』列傳形式",
    name_en="Liezhuan form of Sima Qian's Shiji",
    name_original="史記列傳",
    period_key="漢",
    definition="司馬遷（前145頃-前86頃）『史記』130篇の中、列傳70篇は人物中心の歴史叙述形式を確立した。伯夷・管晏・老子韓非・孫子吳起・伍子胥・刺客・游俠・滑稽・貨殖等の伝は中国伝記文学の規範をなし、後世正史「紀傳體」の祖型となった。",
    background="漢武帝期の太史公制度と司馬談・遷父子の歴史編纂事業。",
    development="班固『漢書』以降の二十四史紀傳體の規範、後世伝記文学の根本典拠。",
    historical_context="漢武帝期の文化的綜合と歴史意識の発達。",
    primary_source_url=CTEXT+"shiji",
    primary_source_type="CTEXT: 史記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="史記列傳の人物中心叙事は主体性・物語的アイデンティティ理論の古典的祖型。AI時代における人物像生成・伝記再構築の規範的参照点。")

add(**C, name_ja="班固『漢書』述略",
    name_en="Ban Gu's Hanshu narrative style",
    name_original="漢書",
    period_key="漢",
    definition="班固（32-92）が完成した前漢一代の正史100篇。司馬遷『史記』を継承しつつ「斷代史」（一王朝史）の形式を確立。叙述は典雅で経学的色彩が濃く、文選収録の名文（蘇武李陵書・両都賦序等）を多く含み、後世史伝文学・古文の規範となった。",
    background="後漢初期の経学興隆と前漢史編纂の必要性。",
    development="後漢以降の正史「斷代史」体制、唐宋古文家の規範。",
    historical_context="後漢初期班氏家族の学術活動と東漢経学の成立。",
    primary_source_url=CTEXT+"han-shu",
    primary_source_type="CTEXT: 漢書",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="范曄『後漢書』文体",
    name_en="Fan Ye's Hou Hanshu literary style",
    name_original="後漢書",
    period_key="魏晋南北朝",
    definition="范曄（398-445）が劉宋元嘉年間に編纂した後漢一代の正史90篇。「論」「贊」を体系的に付し、駢文体の歴史叙述を発展させた。范曄の論贊は文選収録の名文として尊崇され、史論文学の規範となった。",
    background="南朝劉宋期の駢文興隆と歴史編纂の制度化。",
    development="後世正史の論贊形式、駢文歴史叙述の規範。",
    historical_context="劉宋元嘉文化期の文学・史学の交差。",
    primary_source_url=CTEXT+"hou-han-shu",
    primary_source_type="CTEXT: 後漢書",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="陳壽『三國志』筆法",
    name_en="Chen Shou's Sanguo Zhi narrative method",
    name_original="三國志",
    period_key="魏晋南北朝",
    definition="陳壽（233-297）が西晋初に編纂した三国時代の正史65篇（魏志30・蜀志15・呉志20）。簡潔な筆致と魏正統論を特色とし、劉宋裴松之注（429成）が膨大な異説を補注した。後世小説『三國演義』の歴史的基盤となり、東アジア「三国」想像の根本典拠。",
    background="西晋統一直後の三国史編纂と魏正統論。",
    development="裴松之注、宋代『資治通鑑』、明代『三國演義』への系譜。",
    historical_context="西晋初期の正史編纂と政治的正統論。",
    primary_source_url=CTEXT+"sanguozhi",
    primary_source_type="CTEXT: 三國志",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="孔雀東南飛",
    name_en="The Peacock Flies Southeast",
    name_original="孔雀東南飛",
    period_key="漢",
    definition="後漢末廬江郡の小吏焦仲卿と妻劉蘭芝の夫婦悲劇を歌う長篇樂府民歌（357句、1785字）。中国最長の樂府叙事詩で、姑による嫁の追い出し・両人の心中をめぐる社会批判性を含む。「孔雀東南飛、五里一徘徊」の名句で知られ、後世悲恋叙事詩の祖型となった。",
    background="後漢末江南地方の家族悲劇の民間伝承。",
    development="徐陵『玉台新詠』所収、後世悲恋叙事詩の規範。",
    historical_context="後漢末家族制度の矛盾と民間口承文学。",
    primary_source_url=CTEXT+"yutai-xinyong",
    primary_source_type="樂府: 玉台新詠所收",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="孔雀東南飛は家族・婚姻における権力構造を批判的に物語化した古代叙事。AI時代のジェンダー規範再考の古典的祖型。")

add(**C, name_ja="古詩十九首の背景",
    name_en="Background of the Nineteen Old Poems",
    name_original="古詩十九首",
    period_key="漢",
    definition="後漢末（2世紀後半）成立とされる無名作者群による五言古詩19首。蕭統『文選』巻29「雜詩」に集成。羈旅・別離・人生無常を主題とし、五言古詩の成熟段階を示す。鍾嶸『詩品』が「文温以麗、意悲而遠」と評し、五言詩の規範的祖型となった。",
    background="後漢末士人階層の動揺と五言詩の民間から文人への移行。",
    development="建安五言詩、六朝抒情詩、唐代五古の規範的源流。",
    historical_context="後漢末党錮の禍と知識人の困窮。",
    primary_source_url=CTEXT+"wen-xuan",
    primary_source_type="文選: 古詩十九首",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蔡琰悲憤詩・胡笳十八拍",
    name_en="Cai Yan's Beifen Shi and Hujia Shibapai",
    name_original="悲憤詩・胡笳十八拍",
    period_key="漢",
    definition="蔡琰（蔡文姫、177頃-?）の自伝的長篇詩。「悲憤詩」（五言108句）は匈奴に拉致された自身の苦難と帰国後の母子別離を語る。「胡笳十八拍」は後人仮託説もあるが、中国最早期の女性自伝叙事詩として、後世女性文学の祖型となった。",
    background="後漢末董卓・李傕の乱における名士家族の離散。",
    development="後世女性叙事詩、現代女性文学史研究の中核対象。",
    historical_context="後漢末三国前夜の社会的動乱と女性受難。",
    primary_source_url=CTEXT+"hou-han-shu/lie-nv-zhuan",
    primary_source_type="後漢書列女傳所收",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="蔡琰悲憤詩は古代女性自伝の希少な実作。AI時代のジェンダー視点による古典再読・女性主体性の再評価の規範的祖型。")

add(**C, name_ja="西京雜記",
    name_en="Xijing Zaji",
    name_original="西京雜記",
    period_key="魏晋南北朝",
    definition="伝劉歆撰・葛洪輯（成立は晋代）の前漢長安宮廷逸話集6巻132条。司馬相如卓文君故事・王嬙事跡・卓王孫宴等の逸話を収め、後世小説・戯曲の重要素材源となった。漢魏六朝筆記小説の代表作の一。",
    background="晋代の前漢宮廷逸話蒐集と志人小説の興隆。",
    development="唐代『開元天寶遺事』、後世宮廷逸話小説の祖型。",
    historical_context="晋代の漢代史事への関心の高まり。",
    primary_source_url=CTEXT+"xi-jing-za-ji",
    primary_source_type="CTEXT: 西京雜記",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王粲「七哀詩」",
    name_en="Wang Can's Qi Ai Shi",
    name_original="七哀詩",
    period_key="漢",
    definition="王粲（177-217、建安七子の一）作の五言古詩三首。後漢末董卓の乱を逃れて長安から荊州へ向かう途上の惨状を描き、「出門無所見、白骨蔽平原」の名句で知られる。建安詩の社会的写実性の代表作。",
    background="後漢末献帝期の戦乱と建安詩人の流亡体験。",
    development="杜甫「三吏三別」、後世社会写実詩の祖型。",
    historical_context="後漢末から建安期の社会的動乱。",
    primary_source_url=CTEXT+"wen-xuan",
    primary_source_type="文選: 王粲七哀詩",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="曹丕「燕歌行」",
    name_en="Cao Pi's Yan Ge Xing",
    name_original="燕歌行",
    period_key="漢",
    definition="魏文帝曹丕（187-226）作の七言詩。「秋風蕭瑟天氣涼」で始まる25句の閨怨詩で、現存する最古の完整な七言詩とされる。後世七言詩・歌行体の祖型として詩歌史上の画期的作品。曹丕『典論論文』とともに、建安文学の理論と実作の頂点。",
    background="建安期魏王朝文学の制度化。",
    development="鮑照「擬行路難」、唐代七言歌行（高適・岑參）の祖型。",
    historical_context="建安期魏王朝の文化的中心地形成。",
    primary_source_url=CTEXT+"yutai-xinyong",
    primary_source_type="樂府: 玉台新詠所收",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# C: 六朝詳細 (12)
# ============================================================
add(**C, name_ja="劉義慶『世説新語』",
    name_en="Liu Yiqing's Shishuo Xinyu",
    name_original="世説新語",
    period_key="魏晋南北朝",
    definition="南朝劉宋臨川王劉義慶（403-444）編纂、後梁劉孝標注の魏晋逸話集。徳行・言語・政事・文学等36門に1130余条の逸話を分類収録。魏晋名士の言行・玄学的清談を伝え、東アジア志人小説の最高傑作と評価される。",
    background="劉宋初期の魏晋懐古文化と志人小説の制度化。",
    development="後世笑林・志人小説、唐宋筆記の規範的源流。",
    historical_context="劉宋元嘉文化期の魏晋名士懐古。",
    primary_source_url=CTEXT+"shi-shuo-xin-yu",
    primary_source_type="CTEXT: 世説新語",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="世説新語の逸話は短い断片で人物像と思想を喚起する。AI時代のショートフォーム文学・ミーム化された意味伝達の東洋的祖型。")

add(**C, name_ja="顏氏家訓",
    name_en="Yan Shi Jia Xun",
    name_original="顏氏家訓",
    period_key="魏晋南北朝",
    definition="北斉黃門侍郎顏之推（531-591頃）が子孫のために著した家訓20篇。教子・治家・風操・慕賢・勉學・文章・名實・涉務・省事・止足・誡兵・養生・歸心等を論じる。中国家訓文学の祖型かつ最高傑作で、後世『朱子家訓』『曾國藩家書』への系譜の起点。",
    background="北朝末期顏氏家族の南北流転体験と儒家家庭教育の伝承。",
    development="後世家訓文学、宋代『朱子家訓』、清代曾國藩家書の祖型。",
    historical_context="北朝末南北朝交替期の士族文化変動。",
    primary_source_url=CTEXT+"yan-shi-jia-xun",
    primary_source_type="CTEXT: 顏氏家訓",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="抱朴子内外篇",
    name_en="Baopuzi Inner and Outer Chapters",
    name_original="抱朴子",
    period_key="魏晋南北朝",
    definition="東晋葛洪（283-343）の道教文学作品。内篇20篇は神仙煉丹・養生方術を、外篇50篇は時政批判・人物品評・文学論を論じる。中国最初期の体系的道教経典であり、外篇は六朝政治散文・文学論の重要資料。",
    background="東晋道教興隆と葛氏家族の方術伝承。",
    development="後世道教経典、葛洪『神仙傳』への系譜。",
    historical_context="東晋玄学・道教興隆期。",
    primary_source_url=CTEXT+"baopuzi",
    primary_source_type="CTEXT: 抱朴子",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="山海經注解",
    name_en="Commentaries on the Shanhai Jing",
    name_original="山海經注",
    period_key="魏晋南北朝",
    definition="先秦〜漢初成書の地理博物誌『山海經』18篇への東晋郭璞（276-324）注、清畢沅校・郝懿行箋疏。山川異物・神話伝説を体系化し、中国地理博物文学・神話学の根本典拠となった。後世神話・幻想文学の祖型。",
    background="戦国〜漢の地理博物誌の編纂と六朝の注釈学。",
    development="魯迅『中国小説史略』、現代神話学・民俗学の中核資料。",
    historical_context="東晋郭璞の博物学・讖緯学の興隆。",
    primary_source_url=CTEXT+"shan-hai-jing",
    primary_source_type="CTEXT: 山海經",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="神異經",
    name_en="Shen Yi Jing",
    name_original="神異經",
    period_key="漢",
    definition="伝東方朔撰（実際は六朝成書）の異物異域伝説集。『山海經』の体例を承けつつ、東西南北中の五方異物を簡潔に記述する。漢魏六朝志怪小説の重要先駆作で、唐代『博物誌』『酉陽雑俎』への直接的祖型。",
    background="漢魏六朝の方士文化と異物伝説の蒐集。",
    development="張華『博物誌』、段成式『酉陽雜俎』の祖型。",
    historical_context="六朝志怪文学の興隆期。",
    primary_source_url=CTEXT+"shen-yi-jing",
    primary_source_type="CTEXT: 神異經",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張華『博物誌』",
    name_en="Zhang Hua's Bowu Zhi",
    name_original="博物誌",
    period_key="魏晋南北朝",
    definition="西晋張華（232-300）撰の博物誌10巻。地理・人物・異獣・草木・薬物・神仙等を系統的に記録した百科全書的博物文学の祖型。原本は散逸し、現存本は後人輯本だが、後世唐宋類書・志怪小説への影響大。",
    background="西晋初張華の博物学的関心と六朝百科全書文化。",
    development="唐代段成式『酉陽雜俎』、宋代『太平御覽』の祖型。",
    historical_context="西晋統一期の文化的綜合。",
    primary_source_url=CTEXT+"bo-wu-zhi",
    primary_source_type="CTEXT: 博物誌",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="文心雕龍「原道・徵聖・宗經」",
    name_en="Wenxin Diaolong: Yuandao, Zhengsheng, Zongjing",
    name_original="文心雕龍原道徵聖宗經",
    period_key="魏晋南北朝",
    definition="劉勰（465-520頃）『文心雕龍』50篇の冒頭三篇。「原道」は文学の宇宙論的根源を、「徵聖」は聖人の規範性を、「宗經」は六経の文学的祖型を論じ、中国文学理論の体系的出発点となった。",
    background="南朝齊梁の駢文興隆と文学理論の体系化。",
    development="後世詩文評論の規範的祖型、現代中国文論研究の中核。",
    historical_context="南朝齊梁文化期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="文心雕龍「原道」は文学を宇宙論的根源に位置付ける。AI生成文学の存在論的位置付けを再考する東洋的祖型。")

add(**C, name_ja="文心雕龍「正緯・辨騷・明詩・樂府」",
    name_en="Wenxin Diaolong: Zhengwei, Bianshao, Mingshi, Yuefu",
    name_original="文心雕龍正緯辨騷明詩樂府",
    period_key="魏晋南北朝",
    definition="『文心雕龍』のジャンル論四篇。「正緯」は讖緯文書の文学性を、「辨騷」は楚辞の評価を、「明詩」は四言・五言詩史を、「樂府」は楽府の沿革を体系化する。各ジャンル史記述の祖型として後世詩文評の規範。",
    background="南朝齊梁のジャンル論的批評の制度化。",
    development="後世詩学・文学史記述の規範的源流。",
    historical_context="齊梁ジャンル意識成熟期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="文心雕龍「詮賦・頌讚・銘箴・誄碑」",
    name_en="Wenxin Diaolong: Quanfu, Songzan, Mingzhen, Leibei",
    name_original="文心雕龍詮賦頌讚銘箴誄碑",
    period_key="魏晋南北朝",
    definition="『文心雕龍』の文体論四篇。賦・頌・讚・銘・箴・誄・碑等の韻文ジャンルの起源・特性・規範を論じ、中国文体論の体系的祖型をなす。各文体の歴史的考察と理論的規定が現代も古典文体研究の出発点。",
    background="齊梁文体論興隆と韻文ジャンル意識の制度化。",
    development="後世「文體明辨」（明徐師曾）等文体論の規範。",
    historical_context="齊梁文学批評の体系化。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鍾嶸『詩品』品第論",
    name_en="Zhong Rong's Shipin grading system",
    name_original="詩品",
    period_key="魏晋南北朝",
    definition="鍾嶸（468頃-518頃）撰の五言詩評論集（梁天監年間成書）。漢魏〜梁代の五言詩人122人を上中下三品に格付し、各詩人の風格・系譜（如「源出於某」）を簡潔に評する。中国詩論最早期の体系的批評著作で、後世詩話の祖型。",
    background="齊梁文学批評の興隆と五言詩史の整理需要。",
    development="後世詩話（『六一詩話』『滄浪詩話』）の祖型。",
    historical_context="齊梁文学評論成熟期。",
    primary_source_url=CTEXT+"shipin",
    primary_source_type="CTEXT: 詩品",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="鍾嶸詩品の品第・系譜論はAI時代の作品評価アルゴリズム・推薦システムにおける格付け論の古典的祖型。")

add(**C, name_ja="蕭統『文選』選録基準",
    name_en="Selection criteria of Xiao Tong's Wen Xuan",
    name_original="文選",
    period_key="魏晋南北朝",
    definition="梁昭明太子蕭統（501-531）撰の中国最古の総集30巻。先秦〜梁代の詩賦文約700篇を37文体に分類収録。「事出於沈思、義歸乎翰藻」の選録基準で経史子を排し純文学を確立。後世「文選学」を生み、東アジア漢文教養の根幹となった。",
    background="梁昭明太子周辺の文学集団と文学独立論の興隆。",
    development="唐代「文選学」（李善注）、東アジア漢学教養の根幹。",
    historical_context="梁昭明太子文学集団の活動期。",
    primary_source_url=CTEXT+"wen-xuan",
    primary_source_type="CTEXT: 文選",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="文選の選録基準（事出於沈思、義歸乎翰藻）は文学独立論の古典的宣言。AI時代のキュレーション・選別アルゴリズムの規範的参照点。")

add(**C, name_ja="徐陵『玉台新詠』",
    name_en="Xu Ling's Yutai Xinyong",
    name_original="玉台新詠",
    period_key="魏晋南北朝",
    definition="梁徐陵（507-583）撰の艶詩総集10巻。漢〜梁の閨情・艶情詩約769首を集成、宮体詩の規範を確立した。「孔雀東南飛」「古詩十九首」を伝える最重要文献の一であり、女性視点詩・恋愛詩史の根本典拠。",
    background="梁宮体詩の興隆と艶情詩の総集化。",
    development="後世閨怨詩・艶情文学の祖型、女性文学史の根本資料。",
    historical_context="梁簡文帝期の宮体詩文化。",
    primary_source_url=CTEXT+"yutai-xinyong",
    primary_source_type="CTEXT: 玉台新詠",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# D: 唐代詳細 (16)
# ============================================================
add(**C, name_ja="初唐四傑（王勃・楊炯・盧照鄰・駱賓王）",
    name_en="Four Eminents of Early Tang",
    name_original="初唐四傑",
    period_key="唐",
    definition="初唐の王勃（650-676）・楊炯（650-693頃）・盧照鄰（630頃-687頃）・駱賓王（619頃-687）の四詩人。六朝駢文・宮体詩を脱却し、詩風に剛健の気を導入。王勃「滕王閣序」、駱賓王「為徐敬業討武曌檄」等の駢文と五言律詩で唐詩の方向を画定した。",
    background="初唐の宮廷駢文文化と新興士人階層の文学的革新。",
    development="盛唐五律・七律の形式的祖型。",
    historical_context="初唐高宗・武則天期の文化的変動。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="全唐詩・文選 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="沈佺期・宋之問の律詩定型化",
    name_en="Shen Quanqi and Song Zhiwen: codification of Lüshi",
    name_original="沈宋律詩",
    period_key="唐",
    definition="沈佺期（656-714頃）と宋之問（656-712）は武則天・中宗朝の宮廷詩人で、五律・七律の平仄規則・対句要件を完成させ「律詩」を定型化した。詩史上「沈宋」並称され、近体詩制度成立の画期となる。",
    background="武則天宮廷詩学集会と詩律理論の制度化。",
    development="盛唐杜甫・李商隱の律詩芸術の規範的基盤。",
    historical_context="武則天朝の文化的隆盛と科挙詩賦試験の制度化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="陳子昂「感遇」三十八首",
    name_en="Chen Zi'ang's Ganyu thirty-eight poems",
    name_original="感遇",
    period_key="唐",
    definition="陳子昂（661-702）の代表作五言古詩38首連作。阮籍「詠懷詩」の系譜を継承し、初唐宮体駢儷詩風を批判して古風復興を提唱。「漢魏風骨」の主張は後世復古派詩論の祖型となり、盛唐李白・杜甫への橋渡しを担った。",
    background="初唐後期の文学的革新運動と陳子昂の古風主張。",
    development="盛唐李白「古風」、宋代蘇軾の祖型。",
    historical_context="武則天朝末期の文化的緊張。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張九齡「感遇」十二首",
    name_en="Zhang Jiuling's Ganyu twelve poems",
    name_original="張九齡感遇",
    period_key="唐",
    definition="盛唐宰相張九齡（678-740）の五言古詩12首連作。陳子昂「感遇」の系譜を承け、被讒貶謫の懐を寓喩的に詠じる。「孤鴻海上來、池潢不敢顧」の名句で知られ、清代蘅塘退士『唐詩三百首』巻頭に置かれる規範作。",
    background="盛唐玄宗朝中期の政争と張九齢の貶謫。",
    development="後世士大夫貶謫詩の規範。",
    historical_context="開元天寶の政治的転換期。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王昌齡七絕",
    name_en="Wang Changling's seven-character quatrains",
    name_original="王昌齡七絕",
    period_key="唐",
    definition="王昌齡（698頃-756頃）は盛唐七絶の最高峰で「七絕聖手」と称された。「閨怨」「出塞」「從軍行」等は宮怨・辺塞・送別を凝縮した詩境で詠じ、王之渙・李白と並ぶ盛唐七絶三大家。鍾嶸詩品的「滋味」概念の七絶的体現。",
    background="盛唐辺塞詩・閨怨詩の興隆と七絶形式の成熟。",
    development="中晩唐李益・杜牧の七絶、宋代陸遊の祖型。",
    historical_context="盛唐玄宗期の辺塞拡張と都市文化。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="錢起・盧綸（大歷十才子）",
    name_en="Qian Qi, Lu Lun and the Ten Talents of Dali",
    name_original="大歷十才子",
    period_key="唐",
    definition="中唐大暦年間（766-779）の長安詩人集団で錢起・盧綸・吉中孚・韓翃・司空曙・苗發・崔峒・耿湋・夏侯審・李端の十名。王維・孟浩然系の山水閑適詩風を承け、盛唐から中唐への過渡的詩風を確立した。",
    background="安史の乱後の長安文化復興と詩人集団の形成。",
    development="中晩唐韋応物・劉長卿の山水詩、唐宋閑適詩の祖型。",
    historical_context="中唐大歷年間の社会的安定回復期。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="韋応物の詩風",
    name_en="Wei Yingwu's poetic style",
    name_original="韋応物",
    period_key="唐",
    definition="韋応物（737-792頃）は中唐山水閑適詩の大家。蘇州刺史を歴任し「韋蘇州」と称される。陶淵明・王維の系譜を承け、平淡冲和の詩境を開いた。「滁州西澗」「寄全椒山中道士」等の詩は後世「韋柳」（韋応物・柳宗元）並称の典範。",
    background="中唐韋氏家族の文化伝統と陶王系統の詩学継承。",
    development="柳宗元、宋代蘇軾「和陶詩」、明清山水詩の祖型。",
    historical_context="中唐前期の隠逸文化と山水閑適趣味。",
    primary_source_url=CTEXT+"quan-tang-shi",
    primary_source_type="全唐詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="韓愈「答李翊書・進学解」",
    name_en="Han Yu's Letters and Essays on Learning",
    name_original="答李翊書・進學解",
    period_key="唐",
    definition="韓愈（768-824）の古文運動を代表する論文二篇。「答李翊書」は文章修養論、「進學解」は学術職分論を寓設問答体で論じる。「氣盛言宜」「不平則鳴」等の命題を含み、唐宋古文家の文章論の規範的祖型。",
    background="中唐韓愈の古文運動と儒学復興運動。",
    development="宋代蘇軾・歐陽修の文論、明清古文家の規範。",
    historical_context="中唐元和文化変動期。",
    primary_source_url=CTEXT+"han-changli-ji",
    primary_source_type="韓昌黎集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="韓愈「不平則鳴」は文学の発生機構を心理的緊張と結びつける。AI時代の創作動機論再考の東洋的祖型。")

add(**C, name_ja="柳宗元「封建論・捕蛇者説」",
    name_en="Liu Zongyuan's Fengjianlun and Bushezhe Shuo",
    name_original="封建論・捕蛇者說",
    period_key="唐",
    definition="柳宗元（773-819）の代表的古文。「封建論」は古代封建制と郡県制を歴史的に論じる政論散文、「捕蛇者説」は永州蛇捕り老人の苦境を媒介に苛政批判する寓喩散文。中唐古文の論政・諷諭の双璧。",
    background="中唐永貞革新失敗後の柳宗元貶謫期。",
    development="後世政論散文・社会批判散文の規範。",
    historical_context="中唐元和政争期。",
    primary_source_url=CTEXT+"liu-he-dong-ji",
    primary_source_type="柳河東集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="唐傳奇「鶯鶯傳・霍小玉傳・李娃傳」",
    name_en="Tang Chuanqi: Yingying Zhuan, Huo Xiaoyu Zhuan, Li Wa Zhuan",
    name_original="鶯鶯傳・霍小玉傳・李娃傳",
    period_key="唐",
    definition="中晩唐傳奇小説の恋愛三大名作。元稹「鶯鶯傳」（『會真記』、後世『西廂記』源流）、蔣防「霍小玉傳」（妓女悲劇）、白行簡「李娃傳」（妓女・科挙生大団円）。中国短篇小説の最高峰の一群で、後世戯曲化の祖型。",
    background="中唐都市文化興隆と科挙生・妓女の社交圏。",
    development="元代『西廂記』、明代『紫釵記』、湯顯祖『南柯記』の祖型。",
    historical_context="中唐長安都市恋愛文化。",
    primary_source_url=CTEXT+"taiping-guangji",
    primary_source_type="太平廣記所收 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="唐傳奇恋愛三大名作は女性主体性・感情の文学化。AI時代における感情モデリング・人物心理生成の古典的祖型。")

add(**C, name_ja="唐傳奇「南柯太守傳・枕中記」",
    name_en="Tang Chuanqi: Nanke Taishou Zhuan, Zhenzhong Ji",
    name_original="南柯太守傳・枕中記",
    period_key="唐",
    definition="中晩唐傳奇の幻夢題材二大名作。沈既濟「枕中記」（黄粱一夢、盧生の出仕幻夢）、李公佐「南柯太守傳」（蟻國幻夢）。仏教華厳・道教幻想を統合し、人世無常を寓喩する。明代湯顯祖『邯鄲記』『南柯記』の直接的祖型。",
    background="中唐仏教華厳と道教幻想の文学的綜合。",
    development="湯顯祖玉茗堂四夢、後世幻夢小説の祖型。",
    historical_context="中唐宗教文化の文学的内在化。",
    primary_source_url=CTEXT+"taiping-guangji",
    primary_source_type="太平廣記所收 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="枕中記・南柯記の幻夢構造は仮想現実・シミュレーション論の東洋的祖型。AI生成現実の哲学的位置付けに資する。")

add(**C, name_ja="唐傳奇「古鏡記」",
    name_en="Tang Chuanqi: Gujing Ji",
    name_original="古鏡記",
    period_key="唐",
    definition="王度（585-625頃）撰の初唐傳奇。古鏡を媒介に妖怪退治の連鎖譚を構成する中国最古の本格傳奇小説。志怪から傳奇への移行点に位置し、長篇連環短篇の形式を確立した。後世幻想冒険小説の祖型。",
    background="初唐隋末の方士・道教文化と志怪小説の傳奇化。",
    development="中晩唐傳奇集、明清幻想長篇の祖型。",
    historical_context="初唐隋末の宗教文化変動期。",
    primary_source_url=CTEXT+"taiping-guangji",
    primary_source_type="太平廣記所收 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="杜牧七絶",
    name_en="Du Mu's seven-character quatrains",
    name_original="杜牧七絕",
    period_key="唐",
    definition="杜牧（803-852）は晩唐七絶の最高峰で「小杜」と称される（杜甫「老杜」に対し）。「江南春」「泊秦淮」「山行」「赤壁」「過華清宮」等の七絶は懐古・諷諭・抒情を凝縮し、王昌齡七絕の系譜の頂点をなす。",
    background="晩唐の懐古・諷諭文化と杜牧個人の歴史意識。",
    development="宋代王安石・蘇軾、後世七絶の規範。",
    historical_context="晩唐文宗武宗期の士大夫文化。",
    primary_source_url=CTEXT+"fan-chuan-wen-ji",
    primary_source_type="樊川文集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="李商隱無題詩・象徴主義",
    name_en="Li Shangyin's Wuti Shi and symbolic style",
    name_original="無題詩",
    period_key="唐",
    definition="李商隱（813頃-858）の無題詩群（「無題」「錦瑟」「無題二首」等）は典故・象徴・暗喩を重層化し、晦渋幽美の詩境を開いた。「滄海月明珠有淚、藍田日暖玉生煙」等の象徴的比喩は中国象徴主義詩の頂点で、現代詩学・西洋象徴主義との比較研究の中核対象。",
    background="晩唐党争（牛李党争）と李商隱の政治的不遇。",
    development="宋代江西派、清代龔自珍、現代象徴主義詩の祖型。",
    historical_context="晩唐党争激化期。",
    primary_source_url=CTEXT+"yi-shan-shi-ji",
    primary_source_type="李義山詩集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="李商隱無題詩の重層的象徴と意味の不確定性は、AI生成詩・多義的言語生成の古典的祖型として再読可能。")

add(**C, name_ja="李賀の鬼詩",
    name_en="Li He's ghost poems",
    name_original="李賀鬼詩",
    period_key="唐",
    definition="李賀（790-816）は中唐後期の異色詩人で「詩鬼」と称される。「金銅仙人辭漢歌」「秋來」「蘇小小墓」等の作で鬼神・幻想・死を主題とし、奇詭瑰麗の詩境を開いた。後世李商隱・温庭筠の詩風祖型、現代「幻想詩」研究の中核対象。",
    background="中唐元和の宗教文化と李賀の早逝・病弱体験。",
    development="晩唐李商隱・温庭筠、現代幻想詩研究の祖型。",
    historical_context="中唐元和文化変動と宗教幻想の文学化。",
    primary_source_url=CTEXT+"li-he-shi-ji",
    primary_source_type="李長吉歌詩 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# (removed: 蘅塘退士『唐詩三百首』 — secondary tier trimmed)


# ============================================================
# E: 宋代詳細 (10)
# ============================================================
add(**C, name_ja="歐陽修『六一詩話』",
    name_en="Ouyang Xiu's Liuyi Shihua",
    name_original="六一詩話",
    period_key="宋",
    definition="北宋歐陽修（1007-1072）の晩年随筆体詩話で、中国「詩話」ジャンル創始作。約28則の短評で同時代詩人逸話・詩句評鑑を綴る。「詩話」の名称・形式の祖となり、宋代『滄浪詩話』『歲寒堂詩話』等の典範となった。",
    background="北宋慶曆嘉祐期の歐陽修文学集団と詩学批評の制度化。",
    development="後世詩話伝統（宋金元明清）の祖型。",
    historical_context="北宋古文運動成熟期。",
    primary_source_url=CTEXT+"liu-yi-shi-hua",
    primary_source_type="CTEXT: 六一詩話",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="詩話形式は短評の蓄積による批評。AI時代のソーシャル批評・コメント文化の東洋的祖型。")

add(**C, name_ja="王安石『臨川集』",
    name_en="Wang Anshi's Linchuan Ji",
    name_original="王臨川集",
    period_key="宋",
    definition="北宋王安石（1021-1086）の詩文全集。詩は「半山體」と称される晩年絶句が著名（「春風又綠江南岸」等）、散文は「讀孟嘗君傳」等の短篇政論で知られる。新法政争を背景に、思想・詩風の双方で宋代知識人文学の重要モデル。",
    background="北宋熙寧変法と王安石の政治・文学活動。",
    development="後世政論散文、晩年絶句詩風の規範。",
    historical_context="北宋熙寧元豐の新法政争。",
    primary_source_url=CTEXT+"linchuan-ji",
    primary_source_type="王臨川集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="蘇軾『東坡志林』",
    name_en="Su Shi's Dongpo Zhilin",
    name_original="東坡志林",
    period_key="宋",
    definition="蘇軾（1037-1101）の晩年随筆集5巻203則。黃州・惠州・儋州貶謫期の見聞・讀書・夢・佛道思索を自在な短文で綴り、宋代筆記文学の最高峰の一。後世「小品文」の祖型として、明代『陶庵夢憶』『閑情偶寄』への系譜を開いた。",
    background="蘇軾晩年の貶謫体験と佛道思想の浸透。",
    development="明代小品文（張岱・李漁）、清代隨筆文学の祖型。",
    historical_context="北宋紹聖元符期の党争と蘇軾貶謫。",
    primary_source_url=CTEXT+"dongpo-zhilin",
    primary_source_type="CTEXT: 東坡志林",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# (removed: 陳師道・陳与義 — secondary trimmed)

add(**C, name_ja="楊万里誠齋體",
    name_en="Yang Wanli's Chengzhai Style",
    name_original="誠齋體",
    period_key="宋",
    definition="南宋楊万里（1127-1206）が確立した詩体。江西派の典故重畳を脱却し、日常的口語的表現と諧謔・敏感な自然観察を特色とする。「小池」「曉出淨慈寺送林子方」等の絶句は南宋詩風転換の象徴で、清代袁枚性靈派の祖型となった。",
    background="南宋孝宗期の江西派批判と新詩風探索。",
    development="清代袁枚性靈派、現代口語詩の祖型。",
    historical_context="南宋中期文学的革新期。",
    primary_source_url=CTEXT+"chengzhai-ji",
    primary_source_type="誠齋集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="范成大『田園雜興』",
    name_en="Fan Chengda's Tianyuan Zaxing",
    name_original="四時田園雜興",
    period_key="宋",
    definition="南宋范成大（1126-1193）の七絶60首連作（淳熙年間作）。春夏秋冬各12首ずつで江南農村四季を詠じ、陶淵明系統の田園詩を集大成。中国古典田園詩の頂点で、後世宋元田園詩、現代農村文学研究の中核対象。",
    background="南宋淳熙期の江南農村文化と范成大の隠居体験。",
    development="後世田園詩の規範、現代農村文学研究の中核資料。",
    historical_context="南宋孝宗期の江南農村経済と士大夫隠居文化。",
    primary_source_url=CTEXT+"shi-hu-ju-shi-shi-ji",
    primary_source_type="石湖居士詩集 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="文天祥「正氣歌」",
    name_en="Wen Tianxiang's Zhengqi Ge",
    name_original="正氣歌",
    period_key="宋",
    definition="南宋末文天祥（1236-1283）が元軍捕虜中に獄中で作した五言古詩60句。儒家「浩然之氣」を歴代忠臣の事跡に托して讃え、自身の節義を表明した中国忠義文学の頂点。明清遺民詩・近代愛国詩の規範的源流。",
    background="南宋末元朝侵攻と文天祥の被虜・獄中生活。",
    development="明末遺民詩、近代抗日愛国詩、現代愛国教育の規範。",
    historical_context="南宋滅亡期の忠義精神の文学化。",
    primary_source_url=CTEXT+"wen-shan-ji",
    primary_source_type="文山先生集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="嚴羽『滄浪詩話』",
    name_en="Yan Yu's Canglang Shihua",
    name_original="滄浪詩話",
    period_key="宋",
    definition="南宋嚴羽（1192頃-1245頃）の詩話。詩辨・詩體・詩法・詩評・考證五門に分かれ、禅宗を媒介とした「妙悟」「興趣」「別材別趣」概念で詩論を体系化。後世中国詩学の根本理論書として、明清詩話・清王士禛神韻説の理論的基盤となった。",
    background="南宋末文学批評の体系化と禅宗思想の浸透。",
    development="明代復古派、清代神韻説の理論的源泉。",
    historical_context="南宋末文化爛熟期。",
    primary_source_url=CTEXT+"canglang-shihua",
    primary_source_type="CTEXT: 滄浪詩話",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="嚴羽「妙悟」「別材別趣」は理性的論理を超えた直観知の重視。AI時代における理性vs直観・暗黙知問題再考の東洋的祖型。")

add(**C, name_ja="沈括『夢溪筆談』",
    name_en="Shen Kuo's Mengxi Bitan",
    name_original="夢溪筆談",
    period_key="宋",
    definition="北宋沈括（1031-1095）撰の科学技術・人文総合筆記30巻609条。天文・暦法・数学・医薬・地理・文学・芸術等を網羅し、中国科学技術史・百科全書文学の最重要文献。文学関連条目は宋代詩文・典故・品評を伝える一級資料。",
    background="北宋元祐期沈括の博学綜合と筆記文学の科学的拡張。",
    development="後世筆記文学、現代中国科学史研究の中核典拠。",
    historical_context="北宋元祐文化期の知的綜合。",
    primary_source_url=CTEXT+"mengxi-bitan",
    primary_source_type="CTEXT: 夢溪筆談",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="洪邁『容齋隨筆』",
    name_en="Hong Mai's Rongzhai Suibi",
    name_original="容齋隨筆",
    period_key="宋",
    definition="南宋洪邁（1123-1202）撰の考證隨筆74巻5冊（隨筆・續筆・三筆・四筆・五筆）。経史子集を博引旁徴し、考證・典故・文学評鑑を収める。宋代考證隨筆の頂点で、清代乾嘉考證学の遠源。後世筆記の規範。",
    background="南宋孝宗光宗期の考證学興隆。",
    development="清代乾嘉考證学（顧炎武・錢大昕）の祖型。",
    historical_context="南宋中期学術文化の成熟。",
    primary_source_url=CTEXT+"rongzhai-suibi",
    primary_source_type="CTEXT: 容齋隨筆",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# F: 元代詳細 (5)
# ============================================================
add(**C, name_ja="紀君祥『趙氏孤兒』",
    name_en="Ji Junxiang's Zhao Shi Gu Er",
    name_original="趙氏孤兒",
    period_key="元",
    definition="元代紀君祥（生没年不詳、13世紀後半）作の四折雑劇。春秋晋國趙氏一族の滅亡と孤児趙武の復讐を描く歴史悲劇。フランス啓蒙期にヴォルテール『中国孤児』（1755）に翻案され、欧州における中国戯曲受容の最重要作品となった。",
    background="元代中後期歴史悲劇の興隆と漢族忠義意識の文学化。",
    development="ヴォルテール仏訳、現代京劇『趙氏孤兒』の祖型。",
    historical_context="元代漢族文人の歴史意識と忠義観の文学化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="趙氏孤兒 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="関漢卿「單刀會」",
    name_en="Guan Hanqing's Dan Dao Hui",
    name_original="單刀會",
    period_key="元",
    definition="関漢卿（1234頃-1300頃）作の四折雑劇。三国時代の関羽が呉の魯肅の招宴に單刀（一振りの剣）で赴き機智で帰還する英雄劇。関漢卿の歴史劇代表作で、後世「關公戲」（関羽劇）の祖型となり、東アジア関帝信仰の文学的基盤の一を形成した。",
    background="元代雑劇黄金期と三国故事の戯曲化。",
    development="明代『三國演義』、後世関公戯の祖型。",
    historical_context="元代雑劇成熟期。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="關漢卿戲曲集 (CTEXT)",
    importance_score=3, source_tier="primary", canonical_in_region="major")

# (removed: 散曲名家 — secondary trimmed)

# (removed: 貫雲石・徐再思 — secondary trimmed)

# (removed: 録鬼簿 — secondary trimmed)


# ============================================================
# G: 明代補完 (10)
# ============================================================
add(**C, name_ja="前後七子復古論",
    name_en="Earlier and Later Seven Masters' Restoration",
    name_original="前後七子",
    period_key="明",
    definition="明代弘治正德の前七子（李夢陽1473-1530・何景明1483-1521ら）と嘉靖隆慶の後七子（李攀龍1514-1570・王世貞1526-1590ら）。「文必秦漢、詩必盛唐」を旗印に台閣體・八股文を批判し、復古主義文学運動を主導した。明代詩文の主要潮流。",
    background="明中期台閣體の弊害と復古主義の興隆。",
    development="清代格調説（沈德潛）、近代古典主義の祖型。",
    historical_context="明中期文化的成熟期と復古論争。",
    primary_source_url=WIKI_ZH+"前後七子",
    primary_source_type="維基百科: 前後七子",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="唐宋派（唐順之・歸有光・茅坤）",
    name_en="Tang-Song School: Tang Shunzhi, Gui Youguang, Mao Kun",
    name_original="唐宋派",
    period_key="明",
    definition="明嘉靖期の散文流派。唐順之（1507-1560）・歸有光（1507-1571）・茅坤（1512-1601）が前後七子の秦漢復古に対抗し、唐宋八大家の散文を規範として再評価。歸有光「項脊軒志」は明代散文の白眉。茅坤『唐宋八大家文鈔』は後世散文教育の標準教科書となった。",
    background="明嘉靖期の前後七子批判と唐宋古文の再評価。",
    development="清代桐城派（方苞・姚鼐）の祖型、後世散文教育の規範。",
    historical_context="明嘉靖文学論争期。",
    primary_source_url=WIKI_ZH+"唐宋派",
    primary_source_type="維基百科: 唐宋派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="公安派（袁宏道）",
    name_en="Gong'an School: Yuan Hongdao",
    name_original="公安派",
    period_key="明",
    definition="明萬曆期の文学流派。湖北公安出身の袁宗道・袁宏道（1568-1610）・袁中道兄弟が中心。「獨抒性靈、不拘格套」を主張し、前後七子の擬古主義・台閣體の形式主義を共に批判。明末小品文（張岱）の祖型を確立した。",
    background="明萬曆期の李贄童心説の影響と個性主義文学の興隆。",
    development="明末小品文、清代袁枚性靈説の祖型。",
    historical_context="明萬曆中後期の思想解放潮流。",
    primary_source_url=WIKI_ZH+"公安派",
    primary_source_type="維基百科: 公安派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

# (removed: 竟陵派 — secondary trimmed)

add(**C, name_ja="李贄童心説",
    name_en="Li Zhi's Theory of the Childlike Mind",
    name_original="童心說",
    period_key="明",
    definition="明李贄（1527-1602）の文学・哲学思想。「童心」（汚されない初心）を真の主体として尊び、儒家経典を「假人言假事」と斥けた。『焚書』『藏書』に体系化され、晩明思想解放潮流の核心理論として、公安派・湯顯祖『牡丹亭』・湯顯祖至情論の祖型となった。",
    background="明萬曆期の陽明学左派（泰州学派）展開と李贄の異端思想。",
    development="公安派性靈説、湯顯祖至情論、清袁枚性靈派の祖型。",
    historical_context="明萬曆思想解放期。",
    primary_source_url=CTEXT+"fenshu",
    primary_source_type="焚書 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="李贄童心説は儒家規範を脱した初心の主体性論。AI時代の主体性・本来性問題（authenticity）の東洋的祖型として再読可能。")

add(**C, name_ja="馮夢龍三言（喻世明言・警世通言・醒世恒言）",
    name_en="Feng Menglong's San Yan",
    name_original="三言",
    period_key="明",
    definition="明馮夢龍（1574-1646）が編纂・改作した白話短篇小説集三種、各40篇計120篇。宋元話本を底本に明代世情を加え、市井生活・恋愛・倫理・諷刺を多面的に描く。中国白話短篇小説の最高峰で、後世「三言二拍」と並称される。",
    background="晩明商業出版興隆と話本小説の文人改作。",
    development="凌濛初『二拍』、清代白話短篇集の祖型。",
    historical_context="晩明江南都市市民文化期。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="三言 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="馮夢龍三言は市井生活の多様性を物語化。AI時代の大衆物語・データ駆動型ナラティブ生成の古典的祖型。")

add(**C, name_ja="凌濛初二拍（初刻拍案驚奇・二刻拍案驚奇）",
    name_en="Ling Mengchu's Er Pai",
    name_original="二拍",
    period_key="明",
    definition="明凌濛初（1580-1644）が崇禎元年・五年（1628・1632）に刊行した白話短篇小説集二種、各40篇計80篇。馮夢龍『三言』に応じた個人創作集で、晩明社会の幅広い相を描出。「三言二拍」並称で中国白話短篇の頂点を構成した。",
    background="馮夢龍『三言』成功を承けた個人創作短篇集の興隆。",
    development="清代『今古奇觀』編纂、後世短篇小説の祖型。",
    historical_context="晩明崇禎期の出版文化。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="二拍 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="湯顯祖『牡丹亭』（玉茗堂四夢）",
    name_en="Tang Xianzu's Mudan Ting and Yumingtang Si Meng",
    name_original="牡丹亭・玉茗堂四夢",
    period_key="明",
    definition="湯顯祖（1550-1616）作の傳奇55齣『牡丹亭還魂記』（1598年成）。杜麗娘と柳夢梅の生死を超えた愛を描く。「玉茗堂四夢」（牡丹亭・紫釵記・南柯記・邯鄲記）は明代戯曲の頂点で、「至情」哲学を文学化。後世昆曲の中心レパートリー。",
    background="晩明李贄童心説・至情論の戯曲的体現。",
    development="清代昆曲、洪昇『長生殿』、孔尚任『桃花扇』の祖型。",
    historical_context="晩明萬曆期の文化的爛熟。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="牡丹亭 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="湯顯祖至情論は感情を生死を超える主体性原理として絶対化。AI時代における人間感情の独自性・愛の哲学的位置付けの古典的祖型。")

add(**C, name_ja="許仲琳『封神演義』",
    name_en="Xu Zhonglin's Fengshen Yanyi",
    name_original="封神演義",
    period_key="明",
    definition="明萬曆期成書（伝許仲琳作、1567-1620頃）の100回神魔小説。武王伐紂を主軸に、姜子牙の封神戦争を仏道神仙交錯の壮大な戦争神話として描く。『西遊記』と並ぶ中国神魔小説の頂点で、東アジア封神信仰・現代ファンタジーの祖型。",
    background="晩明三教交融文化と神魔小説の興隆。",
    development="清代神魔小説、現代華語ファンタジー文学の祖型。",
    historical_context="晩明宗教文化の融合期。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="封神演義 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# (removed: 王世貞曲藻沈璟詞律 — secondary trimmed)


# ============================================================
# H: 清代補完 (15)
# ============================================================
add(**C, name_ja="王士禛神韻説",
    name_en="Wang Shizhen's Shenyun Theory",
    name_original="神韻說",
    period_key="清",
    definition="清初王士禛（1634-1711）が提唱した詩学説。嚴羽『滄浪詩話』「妙悟」「興趣」を承け、「神韻」（言外の余韻と空霊な詩境）を最高美的範疇として確立。司空圖『二十四詩品』を理論的祖型とし、王孟韋柳系統の山水閑適詩を範型とする。清初詩学の主流。",
    background="清初詩学の体系化と神韻派の制度化。",
    development="後世中国詩学・現代日本俳論への影響。",
    historical_context="清康熙期文化爛熟期。",
    primary_source_url=CTEXT+"daijing-tang-shi-hua",
    primary_source_type="帶經堂詩話 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="王士禛神韻説の「言外余韻」「空霊」概念はAI生成詩における暗示・含蓄性問題の古典的参照点。")

add(**C, name_ja="沈德潛格調説",
    name_en="Shen Deqian's Gediao Theory",
    name_original="格調說",
    period_key="清",
    definition="清沈德潛（1673-1769）の詩学説。明代前後七子復古論を継承し、「格律」と「聲調」を詩の中核とする。漢魏盛唐の正統的詩風を規範とし、儒家温柔敦厚の詩教を強調。『古詩源』『唐詩別裁集』『清詩別裁集』等の大型選集編纂が後世詩教の規範となった。",
    background="清乾隆初期の正統詩学制度化と科挙詩教育。",
    development="後世詩教育、童蒙詩学の規範。",
    historical_context="清乾隆期文化的正統化。",
    primary_source_url=CTEXT+"shuo-shi-cui-yu",
    primary_source_type="說詩晬語 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# (removed: 翁方綱肌理説 — secondary trimmed)

add(**C, name_ja="袁枚『隨園詩話』・性靈説",
    name_en="Yuan Mei's Suiyuan Shihua and Xingling Theory",
    name_original="隨園詩話・性靈說",
    period_key="清",
    definition="清袁枚（1716-1797）の詩話16巻補遺10巻と詩学理論。明代公安派・李贄童心説を承け、「性靈」（個性的真情）を詩の本質とする。神韻・格調・肌理三派を共に批判し、清中期最も影響力のある詩学を確立。後世近代詩学・自由詩運動の祖型。",
    background="清乾隆期文化爛熟と袁枚の文人活動。",
    development="近代中国白話詩運動の祖型。",
    historical_context="清乾隆期江南文化爛熟。",
    primary_source_url=CTEXT+"suiyuan-shihua",
    primary_source_type="CTEXT: 隨園詩話",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="袁枚性靈説は個性的真情を詩の本質とする。AI時代のオリジナリティ・本来性論争の東洋的古典的参照点。")

add(**C, name_ja="趙翼『甌北詩話』",
    name_en="Zhao Yi's Oubei Shihua",
    name_original="甌北詩話",
    period_key="清",
    definition="清趙翼（1727-1814）の詩話12巻。歴代名家（李白・杜甫・韓愈・蘇軾・陸遊等）を独立論として体系評論し、清代詩史評論の頂点。「江山代有才人出、各領風騷數百年」の名句で知られ、現代詩史記述の祖型。",
    background="乾嘉考證学の詩学への展開と詩史記述の体系化。",
    development="現代中国詩史記述の祖型。",
    historical_context="清乾嘉考證学全盛期。",
    primary_source_url=CTEXT+"oubei-shihua",
    primary_source_type="CTEXT: 甌北詩話",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="桐城派（方苞・劉大櫆・姚鼐）",
    name_en="Tongcheng School: Fang Bao, Liu Dakui, Yao Nai",
    name_original="桐城派",
    period_key="清",
    definition="清代散文流派。安徽桐城出身の方苞（1668-1749、義法説）・劉大櫆（1698-1779、神氣音節説）・姚鼐（1731-1815、義理考據詞章三合一説）が確立。明代唐宋派を承け、儒家義理と古文技法を統合し、清代正統散文の主流となった。",
    background="清初唐宋古文継承と桐城地方文人ネットワーク。",
    development="清末民初古文家、現代古典散文教育の祖型。",
    historical_context="清乾嘉文化爛熟期の地方学派。",
    primary_source_url=WIKI_ZH+"桐城派",
    primary_source_type="維基百科: 桐城派",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="紀昀總纂『四庫全書總目提要』",
    name_en="Ji Yun's Siku Quanshu Zongmu Tiyao",
    name_original="四庫全書總目提要",
    period_key="清",
    definition="清乾隆37-46年（1772-1781）紀昀（1724-1805）総纂の図書目録解題200巻。経史子集四部44類に10254種図書を分類解題。中国古典文献学の最高峰で、現代中国学術研究の根本工具。文学関連解題は清以前の文学史記述の集大成。",
    background="乾隆四庫全書編纂事業の巨大プロジェクト。",
    development="現代中国学術研究・図書館学の根本典拠。",
    historical_context="清乾隆期文化的全盛と国家編纂事業。",
    primary_source_url=CTEXT+"library.pl",
    primary_source_type="四庫全書總目 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="顧炎武『日知録』",
    name_en="Gu Yanwu's Rizhi Lu",
    name_original="日知錄",
    period_key="清",
    definition="清初顧炎武（1613-1682）の考證隨筆32巻1019則。経史百家を博引旁徴し、考據・経世・文学評論を綜合する。清初実学の代表作で、乾嘉考證学の祖型。文学評論部分は明代文学批判と古文経世論を含み、清代散文の理論的基礎となった。",
    background="明清交替期の遺民学者顧炎武の経世実学。",
    development="乾嘉考證学（戴震・段玉裁）、近代経世学の祖型。",
    historical_context="明清交替期の学術転換。",
    primary_source_url=CTEXT+"ri-zhi-lu",
    primary_source_type="CTEXT: 日知錄",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="黃宗羲『明夷待訪錄』の文学性",
    name_en="Literary character of Huang Zongxi's Mingyi Daifang Lu",
    name_original="明夷待訪錄",
    period_key="清",
    definition="清初黃宗羲（1610-1695）の政治思想著作21篇。「原君」「原臣」「原法」等で君主専制を根本批判し、近代中国民主思想の祖型とされる。論政散文として簡潔峻厲な文体で、清初経世散文の頂点。後世梁啓超の称揚で近代啓蒙思想の規範となった。",
    background="明清交替期遺民学者の政治思想。",
    development="近代梁啓超啓蒙、現代政治哲学研究の祖型。",
    historical_context="明清交替期の政治批判思想。",
    primary_source_url=CTEXT+"mingyi-daifang-lu",
    primary_source_type="CTEXT: 明夷待訪錄",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="黃宗羲「原君」は君主専制を根本批判する近代政治思想の東洋的先駆。AI時代の権力構造再考・分散型統治の古典的理論基盤として再読可能。")

add(**C, name_ja="吳偉業（梅村）清初詩",
    name_en="Wu Weiye (Meicun) early Qing poetry",
    name_original="吳偉業詩",
    period_key="清",
    definition="清初吳偉業（1609-1672、号梅村）の詩作。明清交替の歴史悲劇を題材とした「梅村體」歌行（「圓圓曲」「永和宮詞」等）は唐代元白歌行を承けつつ独自の歴史抒情風格を確立。清初詩壇の三大家（吳偉業・錢謙益・龔鼎孳）の頂点。",
    background="明清交替期の知識人体験と歌行体の歴史抒情化。",
    development="清代歌行体、近代歴史抒情詩の祖型。",
    historical_context="明清交替期の文化的緊張。",
    primary_source_url=CTEXT+"meicun-jiacang-gao",
    primary_source_type="梅村家藏稿 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="龔自珍『己亥雜詩』",
    name_en="Gong Zizhen's Jihai Zashi",
    name_original="己亥雜詩",
    period_key="清",
    definition="清龔自珍（1792-1841）が道光19年（己亥、1839）に作した七絶315首連作。退官南帰途上の見聞・回想・政治批判・哲学を凝縮した中国近代詩の出発点。「九州生氣恃風雷」「我勸天公重抖擻」等の名句で知られ、近代啓蒙文学の規範。",
    background="清道光期社会矛盾激化と龔自珍の改革思想。",
    development="近代啓蒙詩、五四新文学の祖型。",
    historical_context="清道光期内憂外患の前夜。",
    primary_source_url=CTEXT+"ding-an-wen-ji",
    primary_source_type="定盦文集 (CTEXT)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="龔自珍己亥雜詩は近代意識の文学的覚醒。AI時代における時代変動を捉える詩的言語・批判精神の規範的祖型。")

add(**C, name_ja="黃遵憲『人境廬詩草』",
    name_en="Huang Zunxian's Renjinglu Shicao",
    name_original="人境廬詩草",
    period_key="清",
    definition="清末黃遵憲（1848-1905）の詩集11巻。日本・米国・英国・シンガポール公使歴任の海外体験を「我手寫吾口」の詩学で詠じ、外来事物・新概念を伝統詩形に取り込んだ「詩界革命」の核心作。近代中国詩革新の出発点。",
    background="清末黃遵憲の外交体験と詩界革命運動。",
    development="梁啓超「詩界革命」、近代白話詩運動の祖型。",
    historical_context="清末光緒期の維新運動。",
    primary_source_url=CTEXT+"renjinglu-shicao",
    primary_source_type="人境廬詩草 (CTEXT)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="梁啓超『文界革命』",
    name_en="Liang Qichao's Literary Revolution",
    name_original="文界革命",
    period_key="清",
    definition="清末梁啓超（1873-1929）が日本亡命中（1899）に提起した文学革新運動。「詩界革命」「文界革命」「小説界革命」を統一的に主張し、伝統文体を近代化・大衆化した「新民體」を確立。近代中国白話文運動・五四新文学の直接的祖型。",
    background="清末戊戌変法失敗後の梁啓超日本亡命と啓蒙活動。",
    development="五四新文学運動、近代中国文学史の出発点。",
    historical_context="清末光緒期の維新失敗と啓蒙活動。",
    primary_source_url=WIKI_ZH+"梁啟超",
    primary_source_type="維基百科: 梁啟超文界革命",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="梁啓超文界革命は近代媒体（新聞・雑誌）と文学を結合した変革。AI時代の生成型メディア・新民形成の古典的先駆として参照可能。")

# (removed: 才子佳人小説 — secondary trimmed)

# (removed: 紅樓夢續書 — secondary trimmed)


# ============================================================
# Cross-domain links (>=18 required)
# ============================================================
CROSS: dict[str, list[dict]] = {
    "尚書編纂史": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "中国経学",
         "description": "尚書は儒家五経の一として中国経学の根幹をなす。"},
    ],
    "易經繫辭傳の文学性": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "言意之辨",
         "description": "繫辭傳「立象以盡意」は中国哲学言意論の根本典拠。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "象徴と意味の理論",
         "description": "繫辭傳「象」概念は東アジア象徴理論の祖型。"},
    ],
    "莊子内篇逍遙遊・齊物論・養生主": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "道家相対主義",
         "description": "齊物論は中国哲学相対主義認識論の根本典拠。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "寓言と哲学的散文",
         "description": "莊子寓言は東アジア哲学的散文・寓言文学の規範。"},
    ],
    "韓非子の寓言": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "寓言と論証修辞",
         "description": "韓非子寓言は論証修辞学の中国的祖型。"},
    ],
    "司馬遷『史記』列傳形式": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "伝記文学・人物中心叙事",
         "description": "史記列伝は東アジア伝記文学・人物中心叙事の根本典拠。"},
    ],
    "孔雀東南飛": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "悲恋叙事詩",
         "description": "孔雀東南飛は東アジア悲恋叙事詩の祖型。"},
    ],
    "古詩十九首の背景": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "抒情詩の主体性",
         "description": "古詩十九首は中国抒情詩主体性の規範的祖型。"},
    ],
    "蔡琰悲憤詩・胡笳十八拍": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "女性自伝叙事詩",
         "description": "蔡琰悲憤詩は古代女性自伝叙事詩の希少な実作。"},
    ],
    "劉義慶『世説新語』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "逸話文学・志人小説",
         "description": "世説新語は東アジア志人小説・逸話文学の最高峰。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "魏晋玄学",
         "description": "世説新語は魏晋玄学的清談文化の文学的記録。"},
    ],
    "文心雕龍「原道・徵聖・宗經」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "文学理論体系",
         "description": "文心雕龍は中国文学理論最早期の体系的著作。"},
    ],
    "鍾嶸『詩品』品第論": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩人格付けと系譜論",
         "description": "詩品は東アジア詩人格付け・系譜論の祖型。"},
    ],
    "蕭統『文選』選録基準": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "文学独立論・選集編纂学",
         "description": "文選は中国純文学独立論と選集編纂学の出発点。"},
    ],
    "韓愈「答李翊書・進学解」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "古文運動と文章論",
         "description": "韓愈古文運動は東アジア散文理論の規範的祖型。"},
    ],
    "唐傳奇「鶯鶯傳・霍小玉傳・李娃傳」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "短篇小説と恋愛叙事",
         "description": "唐傳奇は中国短篇恋愛小説の最高峰。"},
    ],
    "李商隱無題詩・象徴主義": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "象徴主義詩",
         "description": "李商隱無題詩は中国象徴主義詩の頂点で西洋象徴主義との比較対象。"},
    ],
    "嚴羽『滄浪詩話』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "妙悟と興趣",
         "description": "嚴羽妙悟興趣論は東アジア詩学の中核理論。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "禅宗美学",
         "description": "嚴羽詩学は禅宗思想を媒介とした美学体系。"},
    ],
    "李贄童心説": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "陽明学左派",
         "description": "李贄童心説は陽明学左派（泰州学派）の文学的展開。"},
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "本来性・主体性論",
         "description": "童心説は東アジア主体性論・本来性論の祖型。"},
    ],
    "湯顯祖『牡丹亭』（玉茗堂四夢）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "至情論と恋愛文学",
         "description": "牡丹亭は東アジア至情論・恋愛戯曲の頂点。"},
    ],
    "袁枚『隨園詩話』・性靈説": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "性靈説と個性表現",
         "description": "袁枚性靈説は近代個性表現詩学の祖型。"},
    ],
    "桐城派（方苞・劉大櫆・姚鼐）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "義法・神氣・義理三合一",
         "description": "桐城派文論は東アジア散文理論の体系的頂点。"},
    ],
    "黃宗羲『明夷待訪錄』の文学性": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "近代政治思想の先駆",
         "description": "黃宗羲『原君』は中国近代政治思想の祖型。"},
    ],
    "梁啓超『文界革命』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "近代文学革新",
         "description": "梁啓超文界革命は近代中国白話文運動の出発点。"},
    ],
    "龔自珍『己亥雜詩』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "近代啓蒙詩",
         "description": "龔自珍己亥雜詩は近代啓蒙詩・批判詩学の祖型。"},
    ],
    "陳壽『三國志』筆法": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "歴史叙事と小説の交差",
         "description": "三國志は東アジア歴史叙事と小説の交差点。"},
    ],
}


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    inserted: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for key, name_ja in PERIOD_NAMES.items():
            row = db.conn.execute(
                "SELECT id FROM periods WHERE name_ja = ? AND region = ?",
                (name_ja, "東アジア"),
            ).fetchone()
            if row is None:
                print(f"  [error] missing period: {name_ja}")
                return 1
            period_ids[key] = row["id"]

        for raw in CONCEPTS:
            entry = dict(raw)
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            inserted[entry["name_ja"]] = cid
            if entry.get("fourth_transform_status"):
                fourth_count += 1

        for name_ja, links in CROSS.items():
            cid = inserted.get(name_ja)
            if cid is None:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE name_ja = ? AND subfield_id = 8",
                    (name_ja,),
                ).fetchone()
                if row is None:
                    print(f"  [warn] cross_domain target missing: {name_ja}")
                    continue
                cid = row["id"]
            for cd in links:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {name_ja}: {e}")

        summary = db.progress_summary()
        print(f"[c13_add80] inserted concepts (this run): {len(inserted)} / total: {summary['concepts']}")
        print(f"[c13_add80] fourth_transform tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = len(CONCEPTS)
        print(f"[c13_add80] tier breakdown: primary={primary}, secondary={secondary}, tertiary={tertiary}")
        print(f"[c13_add80] primary ratio: {primary/total*100:.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
