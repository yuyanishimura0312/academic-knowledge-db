"""LIT-DB Phase 2 Wave 20 — C13 add80: Chinese Classical Literature (80 new).

Subfield: lit_cn_classical (id=8), region='東アジア'.
Existing 247 concepts. Target 600.
This wave adds 80 NEW non-overlapping concepts covering:
  - 詩經注疏伝統 (毛詩故訓伝/鄭玄箋/孔穎達正義/朱熹集伝/姚際恒/段玉裁/馬瑞辰/陳奐)
  - 楚辞注疏 (王逸章句/洪興祖補注/朱熹集注/王夫之通釈/姜亮夫通故)
  - 漢代散文補完 (史記五体例/漢書十志/後漢書類伝/裴松之注/賈誼/鼂錯/劉向/王充/桓寛/仲長統/應劭)
  - 文体論古典 (摯虞/文心雕龍各篇/詩品三品/文選体例/任昉/皎然)
  - 唐代散文革新 (韓愈各篇/柳宗元各篇/古文運動論争/劉知幾)
  - 唐代詩学 (杜甫六絶句/王昌齢詩格/皎然内意外意/二十四詩品)
  - 唐傳奇詳細 (枕中記/任氏伝/柳毅伝/霍小玉伝/離魂記/玄怪録/酉陽雑俎/虬髯客)
  - 宋代詩文補完 (歐陽修/蘇軾/王安石/蘇洵/蘇轍/范仲淹/朱熹/楊万里/嚴羽詩辨)
  - 宋詞論争 (蘇門詞派/婉約豪放/周邦彥律呂/姜夔詩説/夢窓晦渋/碧山詠物/張炎詞源)
  - 元曲深掘り (録鬼簿/太和正音譜/西廂諸本/秋思/趙氏孤児/紀君祥)
  - 明代戲曲 (玉茗堂四夢/湯沈論争/曲律/閒情偶寄/南詞叙録)
  - 清代詩学 (帯經堂詩話/説詩晬語/石洲詩話/續詩品/甌北詩話/閱微/揅經室/文史通義)
  - 桐城派 (方苞/劉大櫆/姚鼐/曾國藩/林紓)
  - 清末文界革命 (黄遵憲/梁啓超/嚴復/譚嗣同/章太炎/王國維)

Sources (real, verifiable):
  - CTEXT: https://ctext.org/
  - 維基文庫: https://zh.wikisource.org/
  - Kanripo: https://www.kanripo.org/
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


CTEXT = "https://ctext.org/"
WSRC_ZH = "https://zh.wikisource.org/wiki/"
KANRIPO = "https://www.kanripo.org/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"


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
# A: 詩經注疏伝統 (8)
# ============================================================
add(**C, name_ja="毛詩故訓伝", name_en="Mao's Commentary on the Shijing",
    name_original="毛詩故訓傳", period_key="漢",
    definition="西漢魯人毛亨・趙人毛萇に伝えられた詩経の最古完備な注釈。古文学派の正典として後世詩経解釈の基礎となり、序（毛詩序）と訓詁を備える。",
    background="漢代経学の今古文論争中、古文系毛詩のみが完整に伝承された。",
    development="鄭玄箋・孔穎達正義に継承され、唐宋以降の経学正統。",
    historical_context="西漢経学制度化期。",
    primary_source_url=CTEXT+"book-of-poetry",
    primary_source_type="CTEXT: 毛詩",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="鄭玄毛詩箋", name_en="Zheng Xuan's Annotations on Mao Shi",
    name_original="毛詩鄭箋", period_key="漢",
    definition="後漢鄭玄（127-200）が毛伝を補訂し三家詩説を取り入れた箋注。「箋」は識記の意で、毛伝の不足を補い異説を提示。経学綜合の規範となった。",
    background="後漢経学綜合期、鄭玄の経籍総注事業。",
    development="孔穎達『毛詩正義』が毛伝鄭箋を底本とし唐代官学化。",
    historical_context="後漢末経学綜合期。",
    primary_source_url=CTEXT+"book-of-poetry",
    primary_source_type="CTEXT: 毛詩鄭箋",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="孔穎達『毛詩正義』", name_en="Kong Yingda's Mao Shi Zhengyi",
    name_original="毛詩正義", period_key="唐",
    definition="唐孔穎達（574-648）勅撰『五経正義』の一。毛伝鄭箋を疏解し、経義を統一。科挙経義の規範となり、宋代に至るまで詩経解釈の正統を担った。",
    background="唐初太宗による経学統一事業（貞観中）。",
    development="宋代朱熹『詩集傳』登場までの経学正統。",
    historical_context="唐初経学制度化期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=82",
    primary_source_type="CTEXT: 毛詩正義",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="朱熹『詩集傳』", name_en="Zhu Xi's Shi Jizhuan",
    name_original="詩集傳", period_key="宋",
    definition="南宋朱熹（1130-1200）の詩経注釈。毛伝鄭箋の桎梏を脱し、本義に基づく解釈を試み、淫詩説（鄭衛之風）等の革新を含む。元明清科挙の正典となった。",
    background="南宋道学の経学再編成と本義主義。",
    development="元延祐科挙以降、清代官学に至るまで詩経解釈の正統。",
    historical_context="南宋朱子学興隆期。",
    primary_source_url=WSRC_ZH+"詩集傳",
    primary_source_type="維基文庫: 詩集傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="姚際恒『詩經通論』", name_en="Yao Jiheng's Shijing Tonglun",
    name_original="詩經通論", period_key="清",
    definition="清初姚際恒（1647-1715頃）の詩経批判的解釈。毛伝・朱熹双方を批判し独自の文学的読解を提示。考証学興起期の文学的詩経学の代表作。",
    background="清初考証学興起と経学独立思考の発達。",
    development="清代独立学派の祖型、現代文学的詩経研究の先駆。",
    historical_context="清初考証学勃興期。",
    primary_source_url=WIKI_ZH+"詩經通論",
    primary_source_type="維基百科: 詩經通論",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

# ============================================================
# B: 楚辞注疏 (5)
# ============================================================
add(**C, name_ja="王逸『楚辞章句』",
    name_en="Wang Yi's Chuci Zhangju",
    name_original="楚辞章句", period_key="漢",
    definition="後漢王逸（89-158頃）が東漢順帝期に編んだ現存最古完備な楚辞注釈17巻。屈原作品の章句訓詁を逐句に施し、後世楚辞学の基礎をなす。",
    background="後漢経学的楚辞理解と屈原顕彰。",
    development="洪興祖補注、朱熹集注の基盤となる根本典拠。",
    historical_context="後漢経学制度成立期。",
    primary_source_url=CTEXT+"chu-ci",
    primary_source_type="CTEXT: 楚辞章句",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="洪興祖『楚辞補注』",
    name_en="Hong Xingzu's Chuci Buzhu",
    name_original="楚辞補注", period_key="宋",
    definition="南宋洪興祖（1090-1155）が王逸章句を補訂した楚辞注釈17巻。語義訓詁を精細化し、王逸の不備を補完。宋代楚辞学の代表作で清代まで標準テキスト。",
    background="北宋末南宋初の楚辞研究の興隆。",
    development="朱熹『楚辞集注』に影響、清代王夫之・蔣驥に継承。",
    historical_context="南宋初学術復興期。",
    primary_source_url=WSRC_ZH+"楚辭補注",
    primary_source_type="維基文庫: 楚辭補注",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="朱熹『楚辞集注』",
    name_en="Zhu Xi's Chuci Jizhu",
    name_original="楚辭集注", period_key="宋",
    definition="南宋朱熹（1130-1200）の楚辞注釈8巻。王逸注を簡素化し朱子学的解釈を加え、屈原の忠君愛国を強調。元明科挙官学化により後世規範となった。",
    background="南宋朱子学による経典再解釈事業。",
    development="元明清楚辞学の正統テキスト。",
    historical_context="南宋朱子学完成期。",
    primary_source_url=WSRC_ZH+"楚辭集注",
    primary_source_type="維基文庫: 楚辭集注",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="王夫之『楚辞通釋』",
    name_en="Wang Fuzhi's Chuci Tongshi",
    name_original="楚辭通釋", period_key="清",
    definition="明遺民王夫之（1619-1692）の楚辞注釈14巻。亡国の遺民として屈原に己を投影し、独自の歴史的政治的解釈を展開。清初遺民文学の重要文献。",
    background="明清交替期遺民の屈原追慕。",
    development="近代蔣驥『山帯閣注楚辭』に影響。",
    historical_context="明清交替期遺民学者の活動。",
    primary_source_url=WIKI_ZH+"王夫之",
    primary_source_type="維基百科: 王夫之",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="王夫之楚辞通釈は遺民の自己投影を介した古典解釈の典型。AI時代の主体的読解と歴史的アイデンティティ再構築の祖型。")

# ============================================================
# C: 漢代散文補完 (10)
# ============================================================
add(**C, name_ja="史記五体例（本紀・表・書・世家・列傳）",
    name_en="Five forms of Sima Qian's Shiji",
    name_original="史記五體", period_key="漢",
    definition="司馬遷『史記』130篇の独創的編纂体系。本紀12（帝王）・表10（年表）・書8（制度）・世家30（諸侯）・列傳70（人物）から成り、「紀傳體」の祖型として後世正史24史の規範となった。",
    background="先秦編年体（春秋）から司馬遷による紀傳体への革新。",
    development="班固『漢書』以降の二十四史紀傳体の規範。",
    historical_context="漢武帝期太史公制度の成熟。",
    primary_source_url=CTEXT+"shiji",
    primary_source_type="CTEXT: 史記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="漢書十志・八表",
    name_en="Ten Treatises and Eight Tables of Hanshu",
    name_original="漢書志表", period_key="漢",
    definition="班固『漢書』の制度史叙述部分。十志（律暦・禮樂・刑法・食貨・郊祀・天文・五行・地理・溝洫・藝文）と八表は漢一代の制度を体系化し、特に藝文志は中国最古の図書分類学。",
    background="後漢初期班固・班昭による前漢一代の制度史編纂。",
    development="後世正史十志体・図書分類学（隋書経籍志・四庫提要）の祖型。",
    historical_context="後漢初経学興隆期。",
    primary_source_url=CTEXT+"han-shu",
    primary_source_type="CTEXT: 漢書",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="裴松之『三國志注』",
    name_en="Pei Songzhi's Sanguo Zhi Annotations",
    name_original="三國志注", period_key="魏晋南北朝",
    definition="劉宋裴松之（372-451）が429年に完成した三國志注。陳寿原文の三倍に及ぶ200余種の異書を引用し、「補闕・備異・懲妄・論辨」の四原則で異説を保存。中国注釈学の最高峰。",
    background="劉宋元嘉期の史学興隆と古史料保存意識。",
    development="後世「裴注」型注釈学（資治通鑑考異等）の祖型。",
    historical_context="南朝劉宋初期史学制度化。",
    primary_source_url=CTEXT+"sanguozhi",
    primary_source_type="CTEXT: 三國志注",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="賈誼「陳政事疏」「過秦論」",
    name_en="Jia Yi's Chen Zhengshi Shu and Guo Qin Lun",
    name_original="陳政事疏・過秦論", period_key="漢",
    definition="前漢賈誼（前200-前168）の政論散文。「過秦論」は秦失天下の理由を雄渾な筆致で論じ、「陳政事疏」（治安策）は漢初の諸侯王問題を論じた。漢初政論散文の白眉。",
    background="漢初文景之治の政治改革議論。",
    development="後世政論散文（董仲舒・韓愈・蘇洵）の祖型。",
    historical_context="漢文帝期の政治制度整備。",
    primary_source_url=CTEXT+"xinshu",
    primary_source_type="CTEXT: 賈誼新書",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="劉向『七略』『別録』",
    name_en="Liu Xiang's Qilüe and Bielu",
    name_original="七略・別錄", period_key="漢",
    definition="前漢劉向（前77-前6）・歆父子による中国最古の系統的書籍分類目録。劉向『別録』が個別解題、劉歆『七略』が六分法（六藝・諸子・詩賦・兵書・術数・方技・輯略）を確立。班固藝文志の母体。",
    background="漢成哀期の宮中典籍校書事業。",
    development="班固藝文志、隋書経籍志四部分類への祖型。",
    historical_context="前漢末校書制度の成熟。",
    primary_source_url=WIKI_ZH+"七略",
    primary_source_type="維基百科: 七略",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="王充『論衡』",
    name_en="Wang Chong's Lunheng",
    name_original="論衡", period_key="漢",
    definition="後漢王充（27-97頃）の哲学散文85篇。「疾虚妄」を旨とし当時の讖緯迷信を批判。理性主義的批判精神と簡潔な散文体を備え、中国古代論説散文の白眉として後世自由思想の源流となった。",
    background="後漢経学讖緯化への批判的反動。",
    development="魏晋自由思想・宋代理性主義散文の祖型。",
    historical_context="後漢章帝期讖緯神秘主義の隆盛。",
    primary_source_url=CTEXT+"lunheng",
    primary_source_type="CTEXT: 論衡",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="王充論衡の批判的合理主義はAI時代における誤情報批判・科学的思考の古典的祖型。")

# ============================================================
# D: 文体論古典 (8)
# ============================================================
add(**C, name_ja="摯虞『文章流別論』",
    name_en="Zhi Yu's Wenzhang Liubie Lun",
    name_original="文章流別論", period_key="魏晋南北朝",
    definition="西晋摯虞（?-311）の文体論。詩・賦・頌・銘等の各文体の起源と変遷を体系的に論じた中国最早の文体論専著。原書佚失、佚文のみ現存。劉勰文心雕龍の先駆。",
    background="西晋初学術綜合期の文体意識の成熟。",
    development="文心雕龍体性篇・通変篇の理論的源泉。",
    historical_context="西晋初年文学独立意識の興隆。",
    primary_source_url=WIKI_ZH+"摯虞",
    primary_source_type="維基百科: 摯虞",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="文心雕龍「神思・體性」",
    name_en="Wenxin Diaolong: Shensi and Tixing",
    name_original="文心雕龍神思體性", period_key="魏晋南北朝",
    definition="劉勰『文心雕龍』創作論篇。「神思」は構思の精神過程・想像力論、「體性」は文体と作家個性の対応論。中国創作心理学・作家論の理論的根本典拠。",
    background="南朝齊梁期の文学創作意識の理論化。",
    development="唐宋詩学創作論・作家風格論の祖型。",
    historical_context="南朝齊梁文学理論の成熟期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="神思論は古代創作心理学。AI時代の創造性・生成プロセス論の東洋的祖型として再評価される。")

add(**C, name_ja="文心雕龍「風骨・通變・定勢」",
    name_en="Wenxin Diaolong: Fenggu, Tongbian, Dingshi",
    name_original="文心雕龍風骨通變定勢", period_key="魏晋南北朝",
    definition="劉勰『文心雕龍』風格論三篇。「風骨」は剛健な文学的生命力、「通變」は伝統と革新の弁証、「定勢」は文体に応じた表現勢の確定を論ず。中国風格論の体系的祖型。",
    background="南朝齊梁文体多様化への理論的応答。",
    development="唐宋以降の風格論・通変論の根本典拠。",
    historical_context="齊梁駢文興隆期の風骨論争。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="文心雕龍「情采・熔裁・聲律・麗辭」",
    name_en="Wenxin Diaolong: Qingcai, Rongcai, Shenglü, Lici",
    name_original="文心雕龍情采熔裁聲律麗辭", period_key="魏晋南北朝",
    definition="劉勰『文心雕龍』表現技法論。「情采」（情と文飾）「熔裁」（推敲）「聲律」（音律）「麗辭」（対偶）の各篇は駢文時代の修辞技法を体系化。中国修辞学の理論的頂点。",
    background="齊梁駢文盛行期の修辞技法論の成熟。",
    development="唐宋律詩律賦理論・近世修辞学の祖型。",
    historical_context="齊梁駢文最盛期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="文心雕龍「比興・夸飾・事類・練字・隱秀」",
    name_en="Wenxin Diaolong: Bixing, Kuashi, Shilei, Lianzi, Yinxiu",
    name_original="文心雕龍比興夸飾事類練字隱秀", period_key="魏晋南北朝",
    definition="劉勰『文心雕龍』修辞論。「比興」は譬喩・暗喩、「夸飾」は誇張、「事類」は典故、「練字」は字句精選、「隱秀」は含蓄と精彩を論ず。中国修辞批評の体系的祖型。",
    background="齊梁駢文修辞精緻化の理論化。",
    development="唐宋詩学比興論・典故論・含蓄論の根本典拠。",
    historical_context="齊梁文学批評の成熟期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="文心雕龍「指瑕・養氣・附會・總術」",
    name_en="Wenxin Diaolong: Zhixia, Yangqi, Fuhui, Zongshu",
    name_original="文心雕龍指瑕養氣附會總術", period_key="魏晋南北朝",
    definition="劉勰『文心雕龍』創作技法論末四篇。「指瑕」（誤謬指摘）「養氣」（精神涵養）「附會」（構成統一）「總術」（総合技法論）から成り、創作実践の方法論を綜括する。",
    background="齊梁文学批評の方法論的成熟。",
    development="後世創作技法論・批評理論の祖型。",
    historical_context="齊梁文学批評体系化期。",
    primary_source_url=CTEXT+"wenxin-diaolong",
    primary_source_type="CTEXT: 文心雕龍",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鍾嶸『詩品』上中下三品評",
    name_en="Zhong Rong's Shipin three-grade evaluation",
    name_original="詩品上中下", period_key="魏晋南北朝",
    definition="梁鍾嶸（?-518頃）『詩品』が漢魏六朝122五言詩人を上品11・中品39・下品72に格付けし、各人の風格・系譜・優劣を評論。中国詩人格付論の祖型で、後世詩話批評の規範。",
    background="齊梁文学批評の格付け意識の成熟。",
    development="唐宋詩話・詩格・詩品の祖型、清代神韻格調論の遠源。",
    historical_context="齊梁文学批評最盛期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=4658",
    primary_source_type="CTEXT: 詩品",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============================================================
# E: 唐代散文革新 (9)
# ============================================================
add(**C, name_ja="韓愈「原道・原性・原毀」",
    name_en="Han Yu's Yuan Dao, Yuan Xing, Yuan Hui",
    name_original="韓愈五原", period_key="唐",
    definition="韓愈（768-824）の論説散文「五原」のうち「原道」（儒家道統論）「原性」（性三品論）「原毀」（毀謗論）。儒家道統復興と仏老批判を旨とし、宋代道学の理論的源流となった。",
    background="中唐古文運動と儒家復興の高揚。",
    development="北宋道学（周敦頤・張載・二程・朱熹）の道統論的祖型。",
    historical_context="中唐元和期の儒学復興運動。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86303",
    primary_source_type="CTEXT: 韓昌黎集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="韓愈「送孟東野序・送窮文」",
    name_en="Han Yu's Song Meng Dongye Xu and Song Qiong Wen",
    name_original="送孟東野序・送窮文", period_key="唐",
    definition="韓愈の名文。「送孟東野序」は「不平則鳴」の文学発生論を提示、「送窮文」は寓意的擬古文。両篇とも古文運動の代表作で、後世散文の規範となった。",
    background="中唐古文運動の文学理論的展開。",
    development="宋代蘇軾散文・明清古文家の規範的源流。",
    historical_context="中唐文学革新期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86303",
    primary_source_type="CTEXT: 韓昌黎集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="韓愈「張中丞傳後敘・伯夷頌・平淮西碑」",
    name_en="Han Yu's Zhang Zhongcheng Zhuan Houxu, Boyi Song, Ping Huaixi Bei",
    name_original="韓愈史伝散文", period_key="唐",
    definition="韓愈の史伝・頌賛・碑文の代表作。「張中丞傳後敘」は安史の乱の英雄張巡を顕彰、「伯夷頌」は気節を称揚、「平淮西碑」は元和中興の戦勝記念。古文体史伝の規範。",
    background="中唐元和中興期の文学的記念事業。",
    development="後世史伝散文・碑文体の規範的祖型。",
    historical_context="中唐元和期の政治文化。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86303",
    primary_source_type="CTEXT: 韓昌黎集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="柳宗元「捕蛇者説・三戒」",
    name_en="Liu Zongyuan's Bushe Zhe Shuo and San Jie",
    name_original="捕蛇者説・三戒", period_key="唐",
    definition="柳宗元（773-819）の諷喩散文。「捕蛇者説」は永州の毒蛇捕獲者の苦難を通じ苛政を批判、「三戒」（臨江之麋・黔之驢・永某氏之鼠）は寓言形式の社会批判。中国諷喩散文の頂点。",
    background="柳宗元永州貶謫期の社会観察。",
    development="宋代諷喩散文（王安石・蘇軾）の祖型。",
    historical_context="中唐永貞革新失敗後の貶謫文学。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86304",
    primary_source_type="CTEXT: 柳河東集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="柳宗元「段太尉逸事狀・愚溪詩序」",
    name_en="Liu Zongyuan's Duan Taiwei Yishi Zhuang and Yuxi Shi Xu",
    name_original="段太尉逸事狀・愚溪詩序", period_key="唐",
    definition="柳宗元の伝記散文と詩序。「段太尉逸事狀」は段秀実の節義を顕彰、「愚溪詩序」は永州愚溪の命名由縁を述べ自己の境遇を寄託。柳宗元散文の精髄。",
    background="柳宗元永州永貞革新失敗後の散文活動。",
    development="後世伝記散文・地誌散文の規範。",
    historical_context="中唐元和初期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86304",
    primary_source_type="CTEXT: 柳河東集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="柳宗元「答韋中立論師道書」",
    name_en="Liu Zongyuan's Da Wei Zhongli Lun Shidao Shu",
    name_original="答韋中立論師道書", period_key="唐",
    definition="柳宗元が韋中立に答えた書簡で、為文の方法論を説く。「文以明道」「養吾根」を主張し、古文運動の創作理論を体系化。後世散文創作論の規範的源泉。",
    background="中唐古文運動の理論的成熟。",
    development="宋代欧陽修・蘇軾散文論、明清桐城派文論の祖型。",
    historical_context="中唐元和期の文学理論論争。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86304",
    primary_source_type="CTEXT: 柳河東集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古文運動論争（韓柳 vs 駢文）",
    name_en="Guwen Movement vs. Pianwen debate",
    name_original="古文運動論爭", period_key="唐",
    definition="中唐韓愈・柳宗元主導の古文運動と、当時主流の駢文との文体論争。古文派は先秦両漢散文の質朴を範に「文以載道」を主張、駢文派は形式美を擁護。中国散文史の決定的転換点。",
    background="中唐儒学復興と六朝駢文への批判。",
    development="北宋欧陽修古文運動による完全勝利、明前後七子・公安派論争への系譜。",
    historical_context="中唐元和期の文学イデオロギー論争。",
    primary_source_url=WIKI_ZH+"古文運動",
    primary_source_type="維基百科: 古文運動",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="劉知幾『史通』",
    name_en="Liu Zhiji's Shitong",
    name_original="史通", period_key="唐",
    definition="唐劉知幾（661-721）の史学理論専著。内篇36・外篇13、史書体例・編纂方法・史家修養を体系化。中国最早の史学概論書で、後世章學誠『文史通義』の祖型。",
    background="盛唐史官制度と史学批評意識の成熟。",
    development="清代章學誠『文史通義』の理論的源流。",
    historical_context="盛唐開元期の学術制度化。",
    primary_source_url=CTEXT+"shitong",
    primary_source_type="CTEXT: 史通",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============================================================
# F: 唐代詩学 (5)
# ============================================================
add(**C, name_ja="杜甫「戯為六絶句」",
    name_en="Du Fu's Six Quatrains in Jest",
    name_original="戲為六絕句", period_key="唐",
    definition="杜甫（712-770）が前代詩人（庾信・四傑等）を絶句6首で批評論定した中国最古の論詩絶句。「未及前賢更勿疑」「不薄今人愛古人」等の名句で文学批評の絶句体を創始した。",
    background="盛唐詩学反省の成熟期。",
    development="元好問「論詩三十首」、清王士禛「論詩絶句」の祖型。",
    historical_context="盛唐文学批評の発達期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=87164",
    primary_source_type="CTEXT: 杜詩詳註",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="王昌齢『詩格』",
    name_en="Wang Changling's Shige",
    name_original="詩格", period_key="唐",
    definition="盛唐王昌齢（698頃-756頃）に仮託される詩学理論書（日本伝存）。「三境」（物境・情境・意境）等の概念を提示し、中国「意境」論の最早の理論的祖型として重要。",
    background="盛唐詩学理論化の発達。",
    development="皎然『詩式』・司空圖『二十四詩品』・王國維意境論の遠源。",
    historical_context="盛唐詩学理論成熟期。",
    primary_source_url=WIKI_ZH+"王昌齡",
    primary_source_type="維基百科: 王昌齡",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="皎然『詩式』内意外意論",
    name_en="Jiaoran's Shishi: theory of inner and outer meaning",
    name_original="詩式內意外意", period_key="唐",
    definition="中唐僧皎然（720-803頃）『詩式』5巻の中核理論。「両重意以上、皆文外之旨」と説き、内意（言外の真意）と外意（表層の言）を区別。禅宗的詩学の祖型で嚴羽妙悟論の遠源。",
    background="中唐禅詩学の興隆と意境論の成熟。",
    development="司空圖含蓄論・嚴羽妙悟論・王國維境界論の理論的源流。",
    historical_context="中唐禅宗思想と詩学の融合期。",
    primary_source_url=WIKI_ZH+"詩式",
    primary_source_type="維基百科: 詩式",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="皎然内意外意論は言語表層と意味深層の弁別。AI生成テキストの意味階層論の東洋的祖型。")

add(**C, name_ja="司空圖『二十四詩品』",
    name_en="Sikong Tu's Twenty-four Poetic Modes",
    name_original="二十四詩品", period_key="唐",
    definition="晩唐司空圖（837-908）の詩学理論。雄渾・沖淡・纖穠・沈著・高古・典雅・洗鍊・勁健・綺麗・自然・含蓄・豪放・精神・縝密・疏野・清奇・委曲・實境・悲慨・形容・超詣・飄逸・曠達・流動の24品で詩境を分類。中国詩学風格論の頂点。",
    background="晩唐詩学の風格論的成熟。",
    development="清代王士禛神韻説の根本典拠、現代中国美学の重要資源。",
    historical_context="晩唐五代詩学の極致。",
    primary_source_url=WSRC_ZH+"二十四詩品",
    primary_source_type="維基文庫: 二十四詩品",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="劉禹錫「陋室銘」",
    name_en="Liu Yuxi's Loushi Ming",
    name_original="陋室銘", period_key="唐",
    definition="劉禹錫（772-842）の銘文短文。81字で陋室（粗末な居）に住む文人の精神的高貴を歌い、「斯是陋室、惟吾德馨」「孔子云：何陋之有」で結ぶ。中国短文銘の白眉。",
    background="中唐文人の隠逸志向と銘文形式の発達。",
    development="後世銘文・短文格言の規範。",
    historical_context="中唐元和期の文人文化。",
    primary_source_url=WSRC_ZH+"陋室銘",
    primary_source_type="維基文庫: 陋室銘",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# G: 唐傳奇詳細 (8)
# ============================================================
add(**C, name_ja="沈既濟『枕中記』",
    name_en="Shen Jiji's Zhenzhong Ji",
    name_original="枕中記", period_key="唐",
    definition="中唐沈既濟（750頃-800頃）の伝奇短篇。盧生が呂翁の枕で一夢に栄華富貴を体験し覚めれば黍未だ熟さずという「黄粱一夢」「邯鄲之夢」の原型。中国夢幻文学の祖型。",
    background="中唐道教思想と夢文学の融合。",
    development="元馬致遠『邯鄲記』、明湯顕祖『邯鄲夢』、日本能『邯鄲』の祖型。",
    historical_context="中唐徳宗期の文学。",
    primary_source_url=WSRC_ZH+"枕中記",
    primary_source_type="維基文庫: 枕中記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="枕中記は夢と現実の境界を問う古典。VR/シミュレーション仮説と現実認識を再考する東洋的祖型。")

add(**C, name_ja="沈既濟『任氏傳』",
    name_en="Shen Jiji's Renshi Zhuan",
    name_original="任氏傳", period_key="唐",
    definition="沈既濟の狐女譚伝奇。狐精任氏が貧士鄭六に嫁ぎ夫を富裕にするも、馬上にて猟犬に殺される悲劇。狐精と人間の真実な愛情を描く中国狐女文学の祖型。",
    background="中唐動物精霊伝承の文学化。",
    development="清代蒲松齢『聊齋誌異』狐女譚の祖型。",
    historical_context="中唐徳宗期の文学。",
    primary_source_url=WSRC_ZH+"任氏傳",
    primary_source_type="維基文庫: 任氏傳",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="李朝威『柳毅傳』",
    name_en="Li Chaowei's Liu Yi Zhuan",
    name_original="柳毅傳", period_key="唐",
    definition="中唐李朝威（生没年不詳）の伝奇。書生柳毅が涇河で龍女に出会い洞庭龍宮へ書信を伝え、最終的に龍女と結ばれる物語。中国龍女・人神戀愛伝説の規範的祖型。",
    background="中唐道教神仙伝承の文学化。",
    development="元尚仲賢『柳毅傳書』、明李好古『張生煮海』等の祖型。",
    historical_context="中唐徳宗貞元期の文学。",
    primary_source_url=WSRC_ZH+"柳毅傳",
    primary_source_type="維基文庫: 柳毅傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蔣防『霍小玉傳』",
    name_en="Jiang Fang's Huo Xiaoyu Zhuan",
    name_original="霍小玉傳", period_key="唐",
    definition="中唐蔣防（792頃-835頃）の伝奇。妓女霍小玉が李益と契りを結ぶも捨てられ恨んで死ぬ悲劇。中国悲恋伝奇の代表作で、湯顕祖『紫釵記』の原型。",
    background="中唐元和期の妓女文学伝統。",
    development="明湯顕祖『紫釵記』『紫簫記』の原型。",
    historical_context="中唐元和期の文学。",
    primary_source_url=WSRC_ZH+"霍小玉傳",
    primary_source_type="維基文庫: 霍小玉傳",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="霍小玉傳は妓女視点の悲劇。AI時代のジェンダー視点による古典再読の重要対象。")

add(**C, name_ja="陳玄祐『離魂記』",
    name_en="Chen Xuanyou's Li Hun Ji",
    name_original="離魂記", period_key="唐",
    definition="中唐陳玄祐の伝奇短篇（779頃成）。倩娘の魂が肉体を離れて愛人王宙と出奔し、5年後帰郷時に魂と肉体が再合一する物語。中国「離魂」モチーフの祖型。",
    background="中唐魂魄分離信仰の文学化。",
    development="元鄭光祖『倩女離魂』、明湯顕祖『牡丹亭』の理論的源流。",
    historical_context="中唐貞元期の文学。",
    primary_source_url=WSRC_ZH+"離魂記",
    primary_source_type="維基文庫: 離魂記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="牛僧孺『玄怪録』",
    name_en="Niu Sengru's Xuanguai Lu",
    name_original="玄怪錄", period_key="唐",
    definition="中唐牛僧孺（779-848）の志怪伝奇集10巻。天人・神怪・妖物の説話を集め、伝奇文学の体系化を進めた。「李湯」「岑文本」等の名篇を含み、後世志怪集の規範。",
    background="中唐元和長慶期の志怪文学興隆。",
    development="李復言『續玄怪錄』、宋『太平廣記』の素材源。",
    historical_context="中唐宰相牛僧孺の文学活動。",
    primary_source_url=WIKI_ZH+"玄怪錄",
    primary_source_type="維基百科: 玄怪錄",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="段成式『酉陽雜俎』",
    name_en="Duan Chengshi's Youyang Zazu",
    name_original="酉陽雜俎", period_key="唐",
    definition="晩唐段成式（803-863）の志怪博物雜記30巻。仙鬼・神怪・動植物・域外風俗・各国伝聞を百科全書的に集成。世界文学史上最早期の博物文学集の一。",
    background="晩唐文人の博物学的好奇心と海外交流。",
    development="宋『太平廣記』『太平御覽』の素材源、東アジア博物文学の祖型。",
    historical_context="晩唐文宗武宗期の文化国際化。",
    primary_source_url=CTEXT+"library.pl?if=en&res=82876",
    primary_source_type="CTEXT: 酉陽雜俎",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="杜光庭『虬髯客傳』",
    name_en="Du Guangting's Qiu Ranke Zhuan",
    name_original="虬髯客傳", period_key="唐",
    definition="晩唐五代杜光庭（850-933）の伝奇短篇。隋末乱世に虬髯客（赤鬚客）・李靖・紅拂女の「風塵三俠」が天命を語り別れる物語。中国武俠伝奇の祖型として重要。",
    background="唐末五代道士杜光庭の文学活動。",
    development="後世武俠小説（金庸等）の祖型、明清侠義伝統の根源。",
    historical_context="唐末五代乱世期の文学。",
    primary_source_url=WSRC_ZH+"虬髯客傳",
    primary_source_type="維基文庫: 虬髯客傳",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# H: 宋代詩文補完 (9)
# ============================================================
add(**C, name_ja="歐陽修「秋聲賦・醉翁亭記」",
    name_en="Ouyang Xiu's Qiusheng Fu and Zuiweng Tingji",
    name_original="秋聲賦・醉翁亭記", period_key="宋",
    definition="北宋歐陽修（1007-1072）の散文双璧。「秋聲賦」は秋の音を借りて人生哲学を散文賦体で詠じ、「醉翁亭記」は滁州太守時の名亭を「醉翁之意不在酒」と歌う。宋代古文の頂点。",
    background="北宋慶暦古文運動の成熟。",
    development="後世古文家・文賦体の規範的祖型。",
    historical_context="北宋慶暦至嘉祐期の文学黄金期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=88389",
    primary_source_type="CTEXT: 歐陽修集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蘇軾「前後赤壁賦」",
    name_en="Su Shi's Former and Latter Red Cliff Rhapsodies",
    name_original="前後赤壁賦", period_key="宋",
    definition="北宋蘇軾（1037-1101）が黄州貶謫期（1082）に長江赤壁を遊覧した際の散文賦双篇。「前赤壁賦」は哲学的問答、「後赤壁賦」は神秘的体験を描く。中国散文賦の頂点。",
    background="蘇軾烏台詩案後の黄州貶謫期文学。",
    development="後世散文賦・遊記文学の規範。",
    historical_context="北宋元豊期の党争と文学。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86346",
    primary_source_type="CTEXT: 蘇東坡集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="蘇軾「留侯論・教戰守策」",
    name_en="Su Shi's Liuhou Lun and Jiao Zhanshou Ce",
    name_original="留侯論・教戰守策", period_key="宋",
    definition="蘇軾の論策文。「留侯論」は張良の「能忍」を分析した史論、「教戰守策」は北宋軍事弱化を批判した政論。蘇軾の論策文として後世散文の規範となった。",
    background="北宋嘉祐治平期の科挙策論文化。",
    development="明清制義文・桐城派論策文の祖型。",
    historical_context="北宋嘉祐至熙寧期の政論。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86346",
    primary_source_type="CTEXT: 蘇東坡集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王安石「遊褒禪山記・讀孟嘗君傳」",
    name_en="Wang Anshi's You Baochan Shan Ji and Du Mengchangjun Zhuan",
    name_original="遊褒禪山記・讀孟嘗君傳", period_key="宋",
    definition="王安石（1021-1086）の散文双篇。「遊褒禪山記」は遊記に「世之奇偉瑰怪非常之觀常在險遠」の哲理、「讀孟嘗君傳」は史記伝記の批判的読解。簡潔峻切な王安石散文の精髄。",
    background="北宋熙寧変法主導者王安石の散文活動。",
    development="後世簡潔散文・讀史隨筆の規範。",
    historical_context="北宋熙寧変法期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=88378",
    primary_source_type="CTEXT: 臨川集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="蘇洵「六國論」",
    name_en="Su Xun's Liu Guo Lun",
    name_original="六國論", period_key="宋",
    definition="北宋蘇洵（1009-1066）の史論。「六國破滅、非兵不利、戦不善、弊在賂秦」と論じ戦国六国滅亡を北宋遼夏外交への寓意とした。中国史論散文の規範。",
    background="北宋慶暦期の対遼夏外交問題。",
    development="後世史論・諷諫散文の規範的祖型。",
    historical_context="北宋慶暦至嘉祐期。",
    primary_source_url=CTEXT+"library.pl?if=en&res=86345",
    primary_source_type="CTEXT: 嘉祐集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="蘇轍「黃州快哉亭記」",
    name_en="Su Zhe's Huangzhou Kuaizai Ting Ji",
    name_original="黃州快哉亭記", period_key="宋",
    definition="蘇轍（1039-1112）が兄蘇軾の黃州貶謫地で張夢得が建てた「快哉亭」のために作った記文。「士生於世、使其中不自得、將何往而非病」と人生哲理を説く宋代記文の佳作。",
    background="蘇軾黃州貶謫期の家族文学活動。",
    development="後世記文・遊記散文の規範。",
    historical_context="北宋元豊期の党争と文学。",
    primary_source_url=CTEXT+"library.pl?if=en&res=88445",
    primary_source_type="CTEXT: 欒城集",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="周敦頤「愛蓮説」",
    name_en="Zhou Dunyi's Ai Lian Shuo",
    name_original="愛蓮說", period_key="宋",
    definition="北宋周敦頤（1017-1073）の短文哲理散文。「予獨愛蓮之出淤泥而不染」と蓮花を君子の象徴とし、菊（隠逸）牡丹（富貴）と対比。中国象徴散文の規範。",
    background="北宋道学興隆期と象徴的散文の発達。",
    development="後世「四君子」象徴体系・哲理散文の祖型。",
    historical_context="北宋熙寧元豊期の道学初期。",
    primary_source_url=WSRC_ZH+"愛蓮說",
    primary_source_type="維基文庫: 愛蓮說",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="范仲淹「岳陽樓記」",
    name_en="Fan Zhongyan's Yueyang Lou Ji",
    name_original="岳陽樓記", period_key="宋",
    definition="北宋范仲淹（989-1052）の記文。慶暦六年（1046）岳州知州滕子京の依頼で作。「先天下之憂而憂、後天下之樂而樂」の名句で知られ、士大夫精神の理想型を示した古文の名篇。",
    background="北宋慶暦新政期の士大夫精神。",
    development="後世士大夫精神論・記文体の規範。",
    historical_context="北宋慶暦六年（1046）。",
    primary_source_url=WSRC_ZH+"岳陽樓記",
    primary_source_type="維基文庫: 岳陽樓記",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="嚴羽『滄浪詩話』詩辨・詩體・詩法",
    name_en="Yan Yu's Canglang Shihua: Shibian, Shiti, Shifa",
    name_original="滄浪詩話五門", period_key="宋",
    definition="南宋嚴羽『滄浪詩話』の体系構成。詩辨（理論）・詩體（文体）・詩法（技法）・詩評（批評）・詩證（考証）の五部から成り、「以禪喩詩」「妙悟」「興趣」を核心とする中国詩学の頂点。",
    background="南宋江西派詩学への批判的反動。",
    development="明前後七子・清王士禛神韻説の根本典拠。",
    historical_context="南宋理宗期文学批評の成熟。",
    primary_source_url=WSRC_ZH+"滄浪詩話",
    primary_source_type="維基文庫: 滄浪詩話",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# I: 宋詞論争 (5)
# ============================================================
add(**C, name_ja="婉約豪放二派区分論争",
    name_en="Debate on Wanyue vs Haofang schools of Ci",
    name_original="婉約豪放論爭", period_key="明",
    definition="明張綖『詩餘圖譜』が宋詞を婉約（柳永・周邦彥・李清照）と豪放（蘇軾・辛棄疾）に二分して以来の詞学論争。後世詞学の根本的二項対立として清代浙西派・常州派論争に繋がる。",
    background="明代後期詞学批評の体系化。",
    development="清代浙西詞派（朱彝尊）・常州詞派（張惠言）論争。",
    historical_context="明嘉靖隆慶期の詞学批評。",
    primary_source_url=WIKI_ZH+"婉約派",
    primary_source_type="維基百科: 婉約派と豪放派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="周邦彥『清真詞』律呂法度",
    name_en="Zhou Bangyan's Qingzhen Ci: tonal rules",
    name_original="清真詞律呂", period_key="宋",
    definition="北宋末周邦彥（1056-1121）の詞集『清真詞』が確立した詞律の精密体系。大晟楽府提挙としての制度的地位を背景に、平仄四声の精緻な配置を体系化し、南宋姜夔・吳文英の詞学的祖型となった。",
    background="北宋末徽宗期大晟府音楽制度。",
    development="姜夔・吳文英・張炎南宋格律詞派の祖型。",
    historical_context="北宋末徽宗大晟府の文化政策。",
    primary_source_url=WIKI_ZH+"周邦彥",
    primary_source_type="維基百科: 周邦彥",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="姜夔『白石道人詩說』",
    name_en="Jiang Kui's Baishi Daoren Shishuo",
    name_original="白石道人詩說", period_key="宋",
    definition="南宋姜夔（1155-1221）の詩学論。「文以文而工、不以文而妙」「詩有四種高妙：理高妙・意高妙・想高妙・自然高妙」等を提唱。南宋格律派詞人による独自の詩学。",
    background="南宋格律派詞人による詩学的反省。",
    development="嚴羽『滄浪詩話』との対話、後世格律派詩学の祖型。",
    historical_context="南宋慶元嘉泰期文学批評。",
    primary_source_url=WIKI_ZH+"白石道人詩說",
    primary_source_type="維基百科: 白石道人詩說",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="張炎『詞源』",
    name_en="Zhang Yan's Ciyuan",
    name_original="詞源", period_key="宋",
    definition="宋末元初張炎（1248-1320）の詞論専書2巻。上巻は楽律論、下巻は詞作技法論で「清空」「騷雅」を尊び呉文英の「質実」を批判。中国最早期の体系的詞論で清代浙西派の祖型。",
    background="宋末元初遺民詞人の理論的反省。",
    development="清代浙西詞派朱彝尊の理論的根源。",
    historical_context="宋元交替期遺民文学。",
    primary_source_url=WIKI_ZH+"詞源_(張炎)",
    primary_source_type="維基百科: 詞源",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="沈義父『樂府指迷』",
    name_en="Shen Yifu's Yuefu Zhimi",
    name_original="樂府指迷", period_key="宋",
    definition="南宋末沈義父（1230頃-1280頃）の詞論短篇。呉文英の詞学を継承し「字面以蘊藉為佳」「下字運意皆有法度」等を説く。南宋末格律派詞論の代表的著作。",
    background="南宋末呉文英学派の理論化。",
    development="張炎『詞源』への影響、清代格律派詞学の遠源。",
    historical_context="南宋末元初詞学。",
    primary_source_url=WIKI_ZH+"沈義父",
    primary_source_type="維基百科: 沈義父",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# J: 元曲深掘り (5)
# ============================================================
add(**C, name_ja="鍾嗣成『録鬼簿』",
    name_en="Zhong Sicheng's Lugui Bu",
    name_original="錄鬼簿", period_key="元",
    definition="元末鍾嗣成（1279頃-1360頃）が1330頃編纂した元雑劇作家152人と作品約450種を記録した雑劇史書。中国最早の戯曲作家伝記資料で、関漢卿等の生平・作品を伝える唯一資料の多くを含む。",
    background="元末雑劇黄金期の歴史的記録意識。",
    development="明代朱權『太和正音譜』、明賈仲明『録鬼簿續編』への祖型。",
    historical_context="元末至順至正期戯曲文化。",
    primary_source_url=WIKI_ZH+"錄鬼簿",
    primary_source_type="維基百科: 錄鬼簿",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="朱權『太和正音譜』十二科分類",
    name_en="Zhu Quan's Taihe Zhengyin Pu: twelve categories",
    name_original="太和正音譜", period_key="明",
    definition="明寧獻王朱權（1378-1448）が1398頃編纂した元明雑劇曲律譜。雑劇を「神仙道化・隠居樂道・披袍秉笏・忠臣烈士・孝義廉節・叱奸罵讒・逐臣孤子・鈸刀趕棒・風花雪月・悲歡離合・煙花粉黛・神頭鬼面」の十二科に分類。中国戯曲分類学の祖型。",
    background="明初宗室文人による雑劇理論化。",
    development="後世戯曲分類・曲律学の祖型。",
    historical_context="明洪武建文期。",
    primary_source_url=WIKI_ZH+"太和正音譜",
    primary_source_type="維基百科: 太和正音譜",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王實甫『西廂記』諸本系譜",
    name_en="Genealogy of editions of Wang Shifu's Xixiang Ji",
    name_original="西廂記諸本", period_key="元",
    definition="王實甫『西廂記』の版本系譜。元刊本は失伝、明弘治岳氏刊本（1498）、明万暦凌濛初刊本、清金聖嘆批點『第六才子書西廂記』（1656）等の主要版本。版本学的価値が高く中国戯曲版本学の中核対象。",
    background="明清出版文化と戯曲評点伝統。",
    development="金聖嘆批本は『西廂記』解釈の規範、清以降の戯曲版本学。",
    historical_context="明清出版・評点文化。",
    primary_source_url=WIKI_ZH+"西廂記",
    primary_source_type="維基百科: 西廂記諸本",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="馬致遠「天淨沙・秋思」",
    name_en="Ma Zhiyuan's Tianjingsha: Qiusi",
    name_original="天淨沙·秋思", period_key="元",
    definition="元馬致遠（1250頃-1321頃）の散曲小令。「枯藤老樹昏鴉、小橋流水人家、古道西風瘦馬、夕陽西下、斷腸人在天涯」の28字で羈旅愁思を凝縮し、中国散曲小令の絶頂とされる。",
    background="元代散曲小令文化の極致。",
    development="後世小令・短歌的抒情詩の規範。",
    historical_context="元代大徳延祐期の文学。",
    primary_source_url=WSRC_ZH+"天淨沙·秋思",
    primary_source_type="維基文庫: 天淨沙秋思",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="楊顯之・鄭德輝（元雑劇作家）",
    name_en="Yang Xianzhi and Zheng Dehui",
    name_original="楊顯之・鄭德輝", period_key="元",
    definition="元前期雑劇作家。楊顯之『瀟湘雨』（夫婦再会劇）と鄭德輝（光祖）『倩女離魂』『㑇梅香』等は関漢卿・王實甫に次ぐ元雑劇の重要遺産。鄭德輝は「元曲四大家」の一に数えられる。",
    background="元前期大都雑劇黄金期。",
    development="明清雑劇・伝奇への素材源。",
    historical_context="元世祖至元至成宗大徳期。",
    primary_source_url=WIKI_ZH+"鄭光祖",
    primary_source_type="維基百科: 鄭光祖",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# K: 明代戲曲 (5)
# ============================================================
add(**C, name_ja="湯顯祖玉茗堂四夢",
    name_en="Tang Xianzu's Four Dreams of Yuming Tang",
    name_original="玉茗堂四夢", period_key="明",
    definition="湯顯祖（1550-1616）の代表作四伝奇「牡丹亭」「南柯記」「邯鄲記」「紫釵記」の総称。夢を共通モチーフとし「至情」「夢幻」「人生哲理」を展開、中国戯曲の哲学的頂点を成す。",
    background="明万暦期江西臨川派の戯曲活動。",
    development="清代崑曲全盛期の主要演目、現代戯曲研究の中核。",
    historical_context="明万暦中期文化。",
    primary_source_url=WIKI_ZH+"玉茗堂四夢",
    primary_source_type="維基百科: 玉茗堂四夢",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="湯沈論争（湯顯祖vs沈璟）",
    name_en="Tang-Shen debate on Ci vs Li",
    name_original="湯沈論爭", period_key="明",
    definition="明万暦期戯曲論争。湯顯祖の臨川派が「意趣神色」を尊び詞采（情感性）を重視、沈璟（1553-1610）の呉江派が「合律依腔」を尊び曲律を重視。中国戯曲史の根本的対立。",
    background="明万暦期戯曲創作と曲律の緊張。",
    development="清代戯曲論争・崑曲格律学の祖型。",
    historical_context="明万暦中後期。",
    primary_source_url=WIKI_ZH+"湯沈之爭",
    primary_source_type="維基百科: 湯沈之爭",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="王驥德『曲律』",
    name_en="Wang Jide's Qulü",
    name_original="曲律", period_key="明",
    definition="明王驥德（?-1623頃）の戯曲理論専著4巻40節。論調・論韻・論平仄・論句法・論套数・論引子・論過搭・論曲禁等を体系化。中国最完備な戯曲理論書として明末清初戯曲論の頂点。",
    background="明万暦末戯曲理論の総合化。",
    development="李漁『閒情偶寄』詞曲部の祖型。",
    historical_context="明万暦末期戯曲学。",
    primary_source_url=WIKI_ZH+"曲律",
    primary_source_type="維基百科: 曲律",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="李漁『閒情偶寄』詞曲論部",
    name_en="Li Yu's Xianqing Ouji: Ciqu Lun section",
    name_original="閒情偶寄詞曲論", period_key="清",
    definition="清初李漁（1611-1680）『閒情偶寄』16巻のうち詞曲部・演習部。結構・詞采・音律・賓白・科諢・格局を論じ、世界戯曲論最早期の体系的著作。中国劇作術の理論的頂点。",
    background="清初戯曲創作実践と理論の結合。",
    development="後世戯曲学・現代演劇理論の祖型。",
    historical_context="清順治康熙期戯曲文化。",
    primary_source_url=WIKI_ZH+"閒情偶寄",
    primary_source_type="維基百科: 閒情偶寄",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="徐渭『南詞敘錄』",
    name_en="Xu Wei's Nanci Xulu",
    name_original="南詞敘錄", period_key="明",
    definition="明徐渭（1521-1593）の南戯研究専著。中国最早の南戯歴史・声腔・体例・劇目を記録した著作。永楽大典戯文三種を補完する南戯研究の根本資料。",
    background="明嘉靖期江南南戯文化の興隆。",
    development="清代戯曲史研究・現代南戯学の祖型。",
    historical_context="明嘉靖隆慶期文化。",
    primary_source_url=WIKI_ZH+"南詞敘錄",
    primary_source_type="維基百科: 南詞敘錄",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# L: 清代詩学 (8)
# ============================================================
add(**C, name_ja="王士禛『帶經堂詩話』",
    name_en="Wang Shizhen's Daijing Tang Shihua",
    name_original="帶經堂詩話", period_key="清",
    definition="清王士禛（1634-1711）の詩話集成（張宗柟編、30巻）。神韻説の理論的源泉として、唐人詩境・王孟韋柳の風格・「不著一字、盡得風流」の美学を体系化。清代詩学の頂点。",
    background="清初康熙期王士禛による詩学指導。",
    development="清代神韻派の根本典拠。",
    historical_context="清初康熙期文学批評。",
    primary_source_url=WIKI_ZH+"王士禛",
    primary_source_type="維基百科: 王士禛詩話",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="沈德潛『說詩晬語』『古詩源』",
    name_en="Shen Deqian's Shuoshi Cuiyu and Gushi Yuan",
    name_original="說詩晬語・古詩源", period_key="清",
    definition="清沈德潛（1673-1769）の格調説詩論と詩選。『說詩晬語』2巻は格調説の理論書、『古詩源』14巻は先秦至隋古詩選で「温柔敦厚」の詩教を尊ぶ。清代格調派の理論的核心。",
    background="清乾隆期格調派の理論化。",
    development="清代官学詩教・科挙試帖詩の祖型。",
    historical_context="清乾隆期詩学。",
    primary_source_url=WIKI_ZH+"沈德潛",
    primary_source_type="維基百科: 沈德潛",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="翁方綱『石洲詩話』",
    name_en="Weng Fanggang's Shizhou Shihua",
    name_original="石洲詩話", period_key="清",
    definition="清翁方綱（1733-1818）の詩話8巻。肌理説の理論書として「義理」と「文理」の統合を主張、神韻派・格調派双方を批判。考証学を詩学に応用した清代詩学の独自展開。",
    background="清乾嘉考証学の詩学への応用。",
    development="清代乾嘉派詩学の理論的核心。",
    historical_context="清乾嘉期文学。",
    primary_source_url=WIKI_ZH+"翁方綱",
    primary_source_type="維基百科: 翁方綱",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="袁枚『續詩品』",
    name_en="Yuan Mei's Xu Shipin",
    name_original="續詩品", period_key="清",
    definition="清袁枚（1716-1797）が司空圖『二十四詩品』を継承し作った『續詩品』32首。崇意・精思・博習・相題・選材・用筆・理氣・布格・擇韻等の創作論を韻文形式で展開。性靈説の理論的補完。",
    background="清乾隆期性靈派の創作論的展開。",
    development="現代詩学創作論の参照点。",
    historical_context="清乾隆期性靈派活動。",
    primary_source_url=WSRC_ZH+"續詩品",
    primary_source_type="維基文庫: 續詩品",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="趙翼『甌北詩話』『陔餘叢考』",
    name_en="Zhao Yi's Oubei Shihua and Gaiyu Congkao",
    name_original="甌北詩話・陔餘叢考", period_key="清",
    definition="清趙翼（1727-1814）の詩話と考証随筆。『甌北詩話』12巻は唐宋元明清主要詩人を批評、『陔餘叢考』は文史考証随筆43巻。「江山代有才人出、各領風騷數百年」の名句で知られる進化的詩観。",
    background="清乾嘉期歴史文学批評の融合。",
    development="近代文学進化論の祖型。",
    historical_context="清乾嘉期文学。",
    primary_source_url=WIKI_ZH+"趙翼",
    primary_source_type="維基百科: 趙翼",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="紀昀『閱微草堂筆記』分類体系",
    name_en="Ji Yun's Yuewei Caotang Biji classification",
    name_original="閱微草堂筆記分類", period_key="清",
    definition="清紀昀（1724-1805）『閱微草堂筆記』24巻の構成。灤陽消夏錄6巻・如是我聞4巻・槐西雜志4巻・姑妄聽之4巻・灤陽續錄6巻の五部から成り、各部毎の体裁・主題的特色が考察対象となる。",
    background="清乾嘉期紀昀の長期執筆事業（1789-1798）。",
    development="清末民国筆記文学の規範。",
    historical_context="清乾嘉期文人筆記。",
    primary_source_url=CTEXT+"library.pl?if=en&res=78030",
    primary_source_type="CTEXT: 閱微草堂筆記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="阮元『揅經室集』",
    name_en="Ruan Yuan's Yanjingshi Ji",
    name_original="揅經室集", period_key="清",
    definition="清阮元（1764-1849）の文集。経学・史学・金石学・文学等を綜合する乾嘉学派の総帥的著作。『十三經注疏校勘記』『經籍纂詁』等の事業も含み、清代学術の頂点を示す。",
    background="清乾嘉期阮元による学術組織化事業。",
    development="清末民国学術の制度的基盤。",
    historical_context="清乾隆嘉慶道光期学術。",
    primary_source_url=WIKI_ZH+"阮元",
    primary_source_type="維基百科: 阮元",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="章學誠『文史通義』",
    name_en="Zhang Xuecheng's Wenshi Tongyi",
    name_original="文史通義", period_key="清",
    definition="清章學誠（1738-1801）の史学・文学理論書8巻。「六經皆史」「即器明道」を主張、文学と歴史を統合する独創的理論を展開。中国伝統学術の最高総合の一として近代学術観の先駆。",
    background="清乾嘉期歴史哲学・文学哲学の総合。",
    development="近代中国史学・文学理論の祖型。",
    historical_context="清乾隆嘉慶期。",
    primary_source_url=CTEXT+"wenshi-tongyi",
    primary_source_type="CTEXT: 文史通義",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# M: 桐城派詳細 (5)
# ============================================================
add(**C, name_ja="方苞「義法」論",
    name_en="Fang Bao's theory of Yifa",
    name_original="方苞義法", period_key="清",
    definition="清桐城派祖方苞（1668-1749）の散文理論「義法」。「義」（言之有物）と「法」（言之有序）の統一を主張し、史記等先秦両漢散文を範とする。桐城派文論の核心。",
    background="清初桐城派散文運動の理論化。",
    development="劉大櫆・姚鼐への発展、桐城派文論の祖型。",
    historical_context="清康熙乾隆期。",
    primary_source_url=WIKI_ZH+"方苞",
    primary_source_type="維基百科: 方苞",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="劉大櫆『論文偶記』",
    name_en="Liu Dakui's Lunwen Ouji",
    name_original="論文偶記", period_key="清",
    definition="清桐城派劉大櫆（1698-1779）の散文理論短篇。「神氣」「音節」「字句」の三段階を提唱し、方苞「義法」論を発展させ姚鼐への橋渡しをなす桐城派中期の核心理論書。",
    background="清乾隆期桐城派理論の中期発展。",
    development="姚鼐桐城三合一論の祖型。",
    historical_context="清乾隆期桐城派活動。",
    primary_source_url=WIKI_ZH+"劉大櫆",
    primary_source_type="維基百科: 劉大櫆",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="姚鼐『古文辭類纂』",
    name_en="Yao Nai's Guwen Cilei Zuan",
    name_original="古文辭類纂", period_key="清",
    definition="清桐城派姚鼐（1731-1815）が編纂した古文選集75巻。先秦至清初の古文を論辨・序跋・奏議・書説・贈序・詔令・伝状・碑誌・雜記・箴銘・頌賛・辭賦・哀祭の13類に分類。桐城派古文の規範的選本。",
    background="清乾嘉期桐城派による古文教育の制度化。",
    development="清末民国古文教育の標準教材。",
    historical_context="清乾嘉期。",
    primary_source_url=WIKI_ZH+"古文辭類纂",
    primary_source_type="維基百科: 古文辭類纂",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="曾國藩『經史百家雜鈔』",
    name_en="Zeng Guofan's Jingshi Baijia Zachao",
    name_original="經史百家雜鈔", period_key="清",
    definition="清湘郷派曾國藩（1811-1872）が姚鼐『古文辭類纂』を継承拡張した古文選集26巻。論著・詞賦・序跋・詔令・奏議・書牘・哀祭・伝志・敘記・典志・雜記の11類に分類。経史と古文を統合した桐城派の発展形。",
    background="清咸豊同治期湘郷派による桐城派継承拡張。",
    development="清末古文選集・国民教育の祖型。",
    historical_context="清咸同期文学。",
    primary_source_url=WIKI_ZH+"經史百家雜鈔",
    primary_source_type="維基百科: 經史百家雜鈔",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="林紓『古文研究法』",
    name_en="Lin Shu's Guwen Yanjiu Fa",
    name_original="古文研究法", period_key="清",
    definition="清末民初林紓（1852-1924）が桐城派古文を体系化した教本。古文の修辞・章法・気勢を分析し近代古文教育の規範を確立。林紓は同時に翻訳家として近代翻訳文学の祖でもあり、近代文学転換期の重要人物。",
    background="清末民初白話文運動への対抗としての伝統古文擁護。",
    development="近代古文教育の規範、五四新文学運動への対立軸。",
    historical_context="清末民初新旧文学交替期。",
    primary_source_url=WIKI_ZH+"林紓",
    primary_source_type="維基百科: 林紓",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_transform_status="rethinking",
    fourth_transform_note="林紓古文研究法と翻訳活動は伝統と近代の交差。AI時代の翻訳・伝統継承問題の古典的祖型。")


# ============================================================
# N: 清末文界革命 (5)
# ============================================================
add(**C, name_ja="黃遵憲「我手寫我口」",
    name_en="Huang Zunxian's 'My hand writes what my mouth says'",
    name_original="我手寫我口", period_key="清",
    definition="清末黃遵憲（1848-1905）が『人境廬詩草自序』『雜感』等で示した詩学革新主張。「我手寫我口、古豈能拘牽」と古典束縛からの解放を宣言、詩界革命の先駆として近代白話詩への移行を準備。",
    background="清末甲午戦後の維新派文学革新。",
    development="梁啓超詩界革命の祖型、五四白話新詩への遠源。",
    historical_context="清末光緒戊戌期。",
    primary_source_url=WIKI_ZH+"黃遵憲",
    primary_source_type="維基百科: 黃遵憲",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="黃遵憲口語詩主張は近代主体性・自然言語表現の祖型。AI時代の言語表現自由化との接続点。")

add(**C, name_ja="嚴復『天演論』譯序",
    name_en="Yan Fu's preface to Tianyan Lun",
    name_original="天演論譯序", period_key="清",
    definition="清末嚴復（1854-1921）が1898年Huxley『進化と倫理』を訳した『天演論』の自序。「信達雅」翻訳三原則を提唱、中国近代翻訳論の祖型。社会進化論の中国紹介で近代思想の転換点。",
    background="清末甲午戦後の維新派啓蒙活動。",
    development="近代中国翻訳学・社会進化論受容の祖型。",
    historical_context="清末光緒戊戌期。",
    primary_source_url=WIKI_ZH+"嚴復",
    primary_source_type="維基百科: 嚴復天演論",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="譚嗣同『仁學』",
    name_en="Tan Sitong's Renxue",
    name_original="仁學", period_key="清",
    definition="清末譚嗣同（1865-1898）の哲学書2巻。儒・仏・耶・近代科学を綜合し、「仁」を「以太」（エーテル）と同一視する独創的形而上学を展開。戊戌変法殉教者の遺著で近代中国哲学の出発点。",
    background="清末戊戌変法期維新派の哲学的綜合。",
    development="近代中国哲学・五四思想への直接的影響。",
    historical_context="戊戌変法期（1898）。",
    primary_source_url=WIKI_ZH+"仁學",
    primary_source_type="維基百科: 仁學",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="譚嗣同仁学は東洋哲学・西洋科学融合の試み。AI時代の知識統合の古典的祖型。")

add(**C, name_ja="章太炎『國故論衡』",
    name_en="Zhang Taiyan's Guogu Lunheng",
    name_original="國故論衡", period_key="清",
    definition="清末民初章太炎（1869-1936）の学術論集3巻（1910刊）。小学・文学・諸子学を綜合し、伝統学術の近代的再構築を企図。「国故」概念を提唱、五四「整理国故」運動の理論的祖型。",
    background="清末民初の学術近代化と国学運動の出発。",
    development="五四「整理国故」運動・現代国学の祖型。",
    historical_context="清末宣統民国初期。",
    primary_source_url=WIKI_ZH+"國故論衡",
    primary_source_type="維基百科: 國故論衡",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="王國維『紅樓夢評論』『宋元戲曲考』",
    name_en="Wang Guowei's Honglou Meng Pinglun and Songyuan Xiqu Kao",
    name_original="紅樓夢評論・宋元戲曲考", period_key="清",
    definition="王國維（1877-1927）の近代文学研究双璧。『紅樓夢評論』（1904）はショーペンハウアー悲劇美学で紅楼夢を分析、『宋元戲曲考』（1913）は中国戯曲史の近代的科学的研究の出発点。",
    background="清末民初王國維による西洋美学と中国文学の融合。",
    development="現代中国文学研究・戯曲史学の祖型。",
    historical_context="清末民初学術近代化。",
    primary_source_url=WIKI_ZH+"王國維",
    primary_source_type="維基百科: 王國維",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_transform_status="rethinking",
    fourth_transform_note="王國維西洋美学による紅楼夢解釈は東西比較文学の祖型。AI時代の異文化解釈の古典的範型。")


# ============================================================
# Cross-domain links (>=18 required)
# ============================================================
CROSS: dict[str, list[dict]] = {
    "毛詩故訓伝": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "今古文経学",
         "description": "毛詩は古文経学の代表的経注で、漢代経学制度の中核。"},
    ],
    "鄭玄毛詩箋": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "鄭学",
         "description": "鄭玄毛詩箋は鄭学（鄭玄経学綜合）の代表的成果。"},
    ],
    "朱熹『詩集傳』": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "朱子学経学",
         "description": "朱熹詩集傳は朱子学経学の重要構成要素。"},
    ],
    "王逸『楚辞章句』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "注釈学伝統",
         "description": "王逸楚辞章句は中国注釈学最古の完備例。"},
    ],
    "朱熹『楚辞集注』": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "朱子学忠君論",
         "description": "朱熹楚辞集注は朱子学的忠君愛国論の文学的表現。"},
    ],
    "史記五体例（本紀・表・書・世家・列傳）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "歴史叙事形式",
         "description": "史記五体例は東アジア歴史叙事の根本形式。"},
    ],
    "漢書十志・八表": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "図書分類学",
         "description": "漢書藝文志は中国図書分類学の祖型。"},
    ],
    "裴松之『三國志注』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "注釈学・異説保存",
         "description": "裴松之注は古史料保存型注釈の規範。"},
    ],
    "王充『論衡』": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "批判的合理主義",
         "description": "王充論衡は中国古代批判的合理主義の代表。"},
    ],
    "劉向『七略』『別録』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "目録学",
         "description": "七略別録は中国目録学の出発点。"},
    ],
    "文心雕龍「神思・體性」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "創作心理学",
         "description": "神思論は東アジア創作心理学の祖型。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "想像力論",
         "description": "神思は中国想像力論の哲学的展開。"},
    ],
    "鍾嶸『詩品』上中下三品評": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "詩人格付論・系譜批評",
         "description": "詩品三品評は東アジア詩人格付論の祖型。"},
    ],
    "韓愈「原道・原性・原毀」": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "道統論",
         "description": "韓愈原道は宋代道学道統論の起源。"},
    ],
    "古文運動論争（韓柳 vs 駢文）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "文体論争",
         "description": "古文運動は中国散文史最大の文体論争。"},
    ],
    "劉知幾『史通』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "史学批評",
         "description": "史通は中国史学理論の祖型。"},
    ],
    "司空圖『二十四詩品』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "風格論・美学類型",
         "description": "二十四詩品は東アジア美学類型論の頂点。"},
    ],
    "皎然『詩式』内意外意論": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "禅宗詩学",
         "description": "皎然詩式は禅宗思想と詩学の融合の祖。"},
    ],
    "沈既濟『枕中記』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "夢幻文学",
         "description": "枕中記は東アジア夢幻文学の祖型。"},
    ],
    "嚴羽『滄浪詩話』詩辨・詩體・詩法": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "禅と詩の融合",
         "description": "嚴羽滄浪詩話は禅宗美学と詩学の体系的融合。"},
    ],
    "湯顯祖玉茗堂四夢": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "至情論・夢幻戯曲",
         "description": "玉茗堂四夢は東アジア至情論戯曲の頂点。"},
    ],
    "湯沈論争（湯顯祖vs沈璟）": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "戯曲詞采vs曲律論争",
         "description": "湯沈論争は中国戯曲論争の根本構造。"},
    ],
    "李漁『閒情偶寄』詞曲論部": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "戯曲創作理論",
         "description": "閒情偶寄は世界戯曲論最早期の体系的著作。"},
    ],
    "鍾嗣成『録鬼簿』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "戯曲作家史",
         "description": "録鬼簿は中国最早の戯曲作家伝。"},
    ],
    "章學誠『文史通義』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "六經皆史",
         "description": "文史通義は中国伝統学術の総合的頂点。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "歴史哲学",
         "description": "章學誠は中国歴史哲学の頂点。"},
    ],
    "姚鼐『古文辭類纂』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "古文選集体系",
         "description": "古文辭類纂は東アジア古文選集の規範。"},
    ],
    "黃遵憲「我手寫我口」": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "近代詩革新",
         "description": "黄遵憲口語詩主張は近代詩革新の出発点。"},
    ],
    "嚴復『天演論』譯序": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "翻訳理論",
         "description": "信達雅は中国近代翻訳論の祖型。"},
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "社会進化論受容",
         "description": "天演論は中国近代思想転換の鍵。"},
    ],
    "譚嗣同『仁學』": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "東西哲学綜合",
         "description": "仁學は中国近代東西哲学綜合の代表。"},
    ],
    "章太炎『國故論衡』": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "国学",
         "description": "国故論衡は中国近代国学の祖型。"},
    ],
    "王國維『紅樓夢評論』『宋元戲曲考』": [
        {"target_db": "PT", "link_type": "shared_concept",
         "target_entity_name": "近代比較文学",
         "description": "王國維紅楼夢評論は近代比較文学の祖。"},
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
        print(f"[wave20_c13_add80] inserted concepts (this run): {len(inserted)} / total: {summary['concepts']}")
        print(f"[wave20_c13_add80] fourth_transform tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = len(CONCEPTS)
        print(f"[wave20_c13_add80] tier breakdown: primary={primary}, secondary={secondary}, tertiary={tertiary}")
        print(f"[wave20_c13_add80] primary ratio: {primary/total*100:.1f}%")
        print(f"[wave20_c13_add80] CONCEPTS count: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
