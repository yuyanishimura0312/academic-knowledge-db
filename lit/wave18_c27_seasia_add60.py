"""LIT-DB Phase 2 Wave 18 — C27 add: SE Asian & Korean Literature (+60 concepts).

Subfield: lit_se_asia_korea (id=17), macro_region='グローバルサウス'.
This is an ADDITIVE wave: 80 concepts already exist. Adds 60 NEW non-overlapping
concepts deepening Korean classical/modern/contemporary, Vietnamese, Thai,
Indonesian/Malay, Filipino, Burmese/Cambodian/Laotian.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("韓国古典文学期", "Korean Classical Literature", 600, 1900,
     "新羅郷歌から朝鮮王朝古文小説・口承パンソリに至る19世紀末以前の韓国古典文学期。"),
    ("韓国近現代文学期", "Korean Modern & Contemporary Literature", 1894, 2030,
     "甲午改革以降のK-novelグローバル化に至る韓国近現代文学期。"),
    ("ベトナム古典・近世文学期", "Vietnamese Classical & Early-Modern Literature", 1000, 1900,
     "李陳朝以降の漢文・字喃文学併存期。"),
    ("ベトナム近現代文学期", "Vietnamese Modern Literature", 1900, 2030,
     "クォック・グー普及以降の近代文学からドイモイ・ディアスポラ期。"),
    ("タイ古典・宮廷文学期", "Thai Classical & Court Literature", 1350, 1900,
     "アユタヤ・ラタナコーシン宮廷文学期。"),
    ("タイ近現代文学期", "Thai Modern Literature", 1900, 2030,
     "ラーマ六世以降の近代化と20世紀社会派・現代タイ文学期。"),
    ("マレー・インドネシア古典口承期", "Malay & Indonesian Classical-Oral Literature", 1300, 1900,
     "ヌサンタラ口承詩・ヒカヤット・スジャラ伝統期。"),
    ("インドネシア・マレーシア近現代期", "Indonesian & Malaysian Modern Literature", 1900, 2030,
     "プジャンガ・バル以降のインドネシア・マレーシア近現代文学。"),
    ("フィリピン古典・スペイン期", "Philippine Classical & Spanish Era", 1565, 1898,
     "スペイン期コリード・パシオン・リサールの民族意識覚醒期。"),
    ("フィリピン近現代文学期", "Philippine Modern Literature", 1900, 2030,
     "米英語期以降の多言語並存とディアスポラ文学。"),
    ("カンボジア・ラオス古典期", "Cambodian & Laotian Classical Period", 1200, 1900,
     "アンコール・ラーンサーン期仏典・王権叙事期。"),
    ("ビルマ（ミャンマー）古典・近代期", "Burmese Classical & Modern Period", 1200, 2030,
     "パガン以降のヤドゥ・ヤガン詩形と19世紀末以降の近代小説期。"),
    ("東南アジア横断的・地域比較期", "Cross-regional SE Asian Literary Period", 1900, 2030,
     "東南アジア多言語・多植民地経験を横断する比較文学期。"),
]


WSRC_KO = "https://ko.wikisource.org/wiki/"
WSRC_VI = "https://vi.wikisource.org/wiki/"
WSRC_TH = "https://th.wikisource.org/wiki/"
WSRC_ID = "https://id.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
KRPIA = "https://www.krpia.co.kr/"
GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_KO = "https://ko.wikipedia.org/wiki/"
WIKI_VI = "https://vi.wikipedia.org/wiki/"
WIKI_TH = "https://th.wikipedia.org/wiki/"
WIKI_ID = "https://id.wikipedia.org/wiki/"
WIKI_FIL = "https://tl.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"
ARCHIVE = "https://archive.org/details/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_se_asia_korea", region="グローバルサウス",
         original_script="vernacular")


# ============================================================
# A: 韓国古典深掘り（12件）
# ============================================================
add(**C, name_ja="一然『三国遺事』",
    name_en="Iryeon's Samguk Yusa",
    name_original="三國遺事",
    period_key="韓国古典文学期",
    definition="高麗末期の僧一然（1206-1289）が13世紀末に編纂した史書兼説話集。新羅郷歌14首を収録し、檀君神話・古朝鮮起源譚・三国仏教説話を網羅する韓国神話文学の根本資料。",
    background="モンゴル襲来後の高麗仏教界における民族史意識覚醒と、口承伝承の文字化必要性。",
    development="20世紀以降の韓国国文学・神話学の根本史料となり、李丙燾・金烈圭らの神話論研究の出発点となった。",
    historical_context="13世紀末高麗の対モンゴル抵抗期と仏教史観の高揚。",
    primary_source_url=KRPIA+"viewer/?prdId=KP02&did=GS_002",
    primary_source_type="KRpia: 三國遺事（古典DB）",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"檀君神話と建国神話",
         "description":"『三国遺事』所収の檀君神話は東アジア建国神話研究の核。"}])

add(**C, name_ja="金富軾『三国史記』",
    name_en="Kim Busik's Samguk Sagi",
    name_original="三國史記",
    period_key="韓国古典文学期",
    definition="高麗中期の儒者金富軾（1075-1151）が1145年に勅命で編纂した正史。本紀・年表・志・列伝50巻からなり、新羅・高句麗・百済三国史を儒教的歴史叙述で記録した韓国最古の現存史書。",
    background="高麗仁宗代の儒教官学整備と、中国正史『史記』に倣った民族史編纂事業。",
    development="近代以降は史料として国文学列伝部分が文学的再評価を受け、薛聡・崔致遠ら文人列伝が古典研究の対象となった。",
    historical_context="1145年高麗朝廷の儒教化と妙清の乱平定後の中央集権強化期。",
    primary_source_url=KRPIA+"viewer/?prdId=KP03&did=GS_003",
    primary_source_type="KRpia: 三國史記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鄭麟趾ら『高麗史』",
    name_en="Goryeo-sa",
    name_original="高麗史",
    period_key="韓国古典文学期",
    definition="朝鮮初期1451年に鄭麟趾らが編纂した高麗王朝（918-1392）正史。139巻、紀伝体。列伝部分に李奎報・李齊賢ら高麗文人の伝記を含み、高麗漢文学研究の根本史料。",
    background="朝鮮王朝建国正統化のため、前王朝史を儒教的に再構成する事業。",
    development="現代韓国国文学では、列伝・楽志（楽歌志）が高麗歌謡・郷歌研究の中核資料となった。",
    historical_context="文宗代の朝鮮王朝史書編纂事業。",
    primary_source_url=KRPIA+"viewer/?prdId=KP04&did=GS_004",
    primary_source_type="KRpia: 高麗史",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="金天澤『青丘永言』",
    name_en="Kim Cheontaek's Cheonggu Yeong-eon",
    name_original="青丘永言",
    period_key="韓国古典文学期",
    definition="朝鮮後期の中人歌客金天澤（生没年不詳）が1728年に編纂した時調集。約580首を収録、現存最古の時調アンソロジーで、士大夫時調と中人時調を体系化した時調文学の根本資料。",
    background="18世紀朝鮮の中人歌客文化興隆と、口承時調の文字化・規範化への要請。",
    development="後の『海東歌謠』『歌曲源流』に継承され、20世紀以降の韓国時調文学研究の基盤となった。",
    historical_context="英祖代（1724-76）の朝鮮王朝後期庶民文化興隆。",
    primary_source_url=KRPIA+"viewer/?prdId=KP05&did=GS_005",
    primary_source_type="KRpia: 青丘永言",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="金壽長『海東歌謠』",
    name_en="Kim Sujang's Haedong Gayo",
    name_original="海東歌謠",
    period_key="韓国古典文学期",
    definition="朝鮮後期の歌客金壽長（1690-?）が1763年に編纂した時調集。約880首を収録し、『青丘永言』を継ぐ時調文学第二の正典。中人歌客の自作時調を多数含み、士大夫文学と中人文学の融合を示す。",
    background="18世紀朝鮮の歌客集団形成と中人文化の文学的自立。",
    development="近代国文学において鄭炳昱『時調文学事典』ら時調研究の核心資料となった。",
    historical_context="英祖・正祖代の文化的成熟期。",
    primary_source_url=KRPIA+"viewer/?prdId=KP06&did=GS_006",
    primary_source_type="KRpia: 海東歌謠",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="朴趾源『熱河日記』",
    name_en="Park Jiwon's Yeolha Ilgi",
    name_original="熱河日記",
    period_key="韓国古典文学期",
    definition="朝鮮後期実学者朴趾源（1737-1805）が1780年清朝乾隆帝七十寿辰使節随行記。26巻、漢文紀行文学の最高傑作で「虎叱」「許生伝」「両班伝」など諷刺漢文小説を収録、北学派思想と批判精神を文学化した。",
    background="18世紀後半朝鮮実学派の清朝文物観察熱と、士大夫漢文の創作的展開。",
    development="20世紀以降、洪明熹・金台俊らによる朝鮮実学文学研究の中心対象となり、近代諷刺文学の祖型と評価された。",
    historical_context="正祖代（1776-1800）の文化的開明と北学派の興隆。",
    primary_source_url=KRPIA+"viewer/?prdId=KP07&did=GS_007",
    primary_source_type="KRpia: 熱河日記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"朴趾源の諷刺漢文小説は士大夫主体性を内側から解体する近代的批評精神を先取りし、AI時代の主体表象批判の歴史的祖型となる。",
         "related_ai_phenomenon":"AI生成テキストの主体批評・諷刺生成"}])

add(**C, name_ja="丁若鏞『牧民心書』",
    name_en="Jeong Yagyong's Mongmin Simseo",
    name_original="牧民心書",
    period_key="韓国古典文学期",
    definition="朝鮮後期実学者多山丁若鏞（1762-1836）が流配地康津で1818年に著した地方官指南書。48巻、漢文散文文学として高度に整序され、儒教的経世論と具体的吏務知識を融合した実学散文の最高峰。",
    background="正祖代の改革挫折と丁若鏞自身の長期流配（1801-1818）体験、康津での茶山学派形成。",
    development="近代以降、朝鮮実学研究の核心対象となり、丁奎英『茶山学』、20世紀以降の韓国実学派文学研究を主導した。",
    historical_context="純祖代の対天主教抑圧期と南人実学派の流配文化。",
    primary_source_url=KRPIA+"viewer/?prdId=KP08&did=GS_008",
    primary_source_type="KRpia: 牧民心書",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="李退渓『退渓全集』",
    name_en="Yi Hwang's Toegye Collected Works",
    name_original="退溪全書",
    period_key="韓国古典文学期",
    definition="朝鮮中期性理学者李滉（号：退渓、1501-1570）の漢詩・書簡・散文・哲学論を集成した文集。68巻、朝鮮性理学の頂点を成し、特に「陶山十二曲」など士大夫詩歌・自然観の規範を確立した。",
    background="16世紀朝鮮性理学の本格的内省化と退渓学派の形成。",
    development="李滉哲学は日本江戸期儒学（山崎闇斎）にも影響、現代では退渓学研究院が国際的研究拠点となる。",
    historical_context="明宗・宣祖代の士林派台頭と党争前夜。",
    primary_source_url=KRPIA+"viewer/?prdId=KP09&did=GS_009",
    primary_source_type="KRpia: 退溪全書",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="金時習『金鰲新話』",
    name_en="Kim Si-seup's Geumo Sinhwa",
    name_original="金鰲新話",
    period_key="韓国古典文学期",
    definition="朝鮮初期の隠士金時習（1435-1493）が金鰲山（慶州）で著した5編の漢文伝奇小説（万福寺樗蒲記・李生窺墻伝・酔遊浮碧亭記・南炎浮州志・龍宮赴宴録）。明『剪燈新話』の影響下に成り、韓国漢文小説の祖と評価される。",
    background="世祖簒奪（1455）への抗議として隠遁した金時習の生隠居体験と、明代伝奇小説受容。",
    development="金万重『九雲夢』、19世紀漢文小説に系譜的影響を与え、近代以降は韓国漢文小説研究の起点となった。",
    historical_context="世祖代（1455-68）の生六臣・死六臣事件と知識人の精神的危機。",
    primary_source_url=KRPIA+"viewer/?prdId=KP10&did=GS_010",
    primary_source_type="KRpia: 金鰲新話",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="許筠『洪吉童伝』",
    name_en="Heo Gyun's Hong Gildong-jeon",
    name_original="洪吉童傳",
    period_key="韓国古典文学期",
    definition="朝鮮中期文人許筠（1569-1618）が17世紀初に著したとされる、ハングルで書かれた最古とされる古典小説。庶子洪吉童が義賊として活躍し、最後に律島国を建国する筋立て。朝鮮社会の身分差別批判を含む民衆小説の祖。",
    background="16-17世紀朝鮮の士庶差別と党争、中国『水滸伝』の朝鮮受容。",
    development="20世紀以降、韓国民衆文学・庶民英雄小説の代表として正典化され、漫画・映画・ドラマに繰り返し翻案された。",
    historical_context="光海君代（1608-23）の党争激化と許筠処刑事件。",
    primary_source_url=KRPIA+"viewer/?prdId=KP11&did=GS_011",
    primary_source_type="KRpia: 洪吉童傳",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="李奎報『東国李相国集』",
    name_en="Yi Gyu-bo's Donggugi Sangguk-jip",
    name_original="東國李相國集",
    period_key="韓国古典文学期",
    definition="高麗中期の文人李奎報（1168-1241）の漢詩文集。53巻、漢詩約2000首と「東明王篇」（高句麗建国叙事詩）を含む高麗漢文学の最高峰。中国詩の規範を超え、高麗独自の詠史・自然詩の境地を開拓した。",
    background="武臣政権下の高麗士人文化と、文人としての官僚的成功・隠逸思想。",
    development="近代以降、「東明王篇」は韓国民族叙事詩の祖型として再評価され、植民地期民族文学運動の参照点となった。",
    historical_context="武臣政権期（1170-1270）の文人官僚層の活動。",
    primary_source_url=KRPIA+"viewer/?prdId=KP12&did=GS_012",
    primary_source_type="KRpia: 東國李相國集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="鄭麟趾ら『龍飛御天歌』",
    name_en="Yongbi Eocheonga (Songs of Flying Dragons)",
    name_original="龍飛御天歌",
    period_key="韓国古典文学期",
    definition="朝鮮初期1445年世宗の命で鄭麟趾・権踶・安止らが編纂した王朝建国叙事歌。125章からなり、訓民正音（ハングル）創製直後の最初の文学作品。李成桂以前6祖の事績を中国故事と対照させて讃える朝鮮王朝建国神話。",
    background="1443年訓民正音創製と、新王朝の正統化叙事の文学的形式化。",
    development="ハングル文学の起点として現代韓国国語教育の根本教材となり、訓民正音表記の最古の文学的事例として言語学的にも重要。",
    historical_context="世宗代（1418-50）のハングル創製と王朝正統化事業。",
    primary_source_url=WSRC_KO+"%EC%9A%A9%EB%B9%84%EC%96%B4%EC%B2%9C%EA%B0%80",
    primary_source_type="Wikisource Korean: 龍飛御天歌",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"訓民正音創製直後の最初の文学テキストとして、人為言語設計と文学創成の歴史的事例であり、AI時代の人工言語・新規記号系設計の参照点。",
         "related_ai_phenomenon":"AI支援による新言語・記号系設計"}])


# ============================================================
# B: 韓国近代深掘り（11件）
# ============================================================
add(**C, name_ja="李光洙『土』",
    name_en="Yi Kwang-su's Heuk (The Soil)",
    name_original="흙",
    period_key="韓国近現代文学期",
    definition="李光洙（1892-1950）が1932-33年に東亜日報連載した啓蒙長編小説。京城帝大法科出身の主人公許崇が農村ブルナル運動に身を投じる筋立てで、植民地期農村啓蒙運動文学の代表作。",
    background="1930年代植民地朝鮮の農村疲弊と、東亜日報・朝鮮日報主導のブルナル（村落覚醒）啓蒙運動。",
    development="解放後は啓蒙文学の典型として正典化される一方、李光洙の親日活動再評価と並行して批判的再読対象となった。",
    historical_context="満州事変後の植民地朝鮮農村の構造的疲弊と知識人覚醒。",
    primary_source_url=WIKI_KO+"%ED%9D%99_(%EC%86%8C%EC%84%A4)",
    primary_source_type="Wikipedia Korean: 흙 (소설)",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="金東仁『甘藷』",
    name_en="Kim Tong-in's Gamja (Potatoes)",
    name_original="감자",
    period_key="韓国近現代文学期",
    definition="金東仁（1900-1951）が1925年に発表した短編小説。平壌郊外の貧民街七星門外を舞台に、貧困と道徳的堕落を経て中国人地主に殺される女性福女を描く植民地期朝鮮自然主義文学の代表短編。",
    background="1920年代植民地朝鮮の都市貧民問題と、ゾラ系自然主義文学の朝鮮受容。",
    development="韓国自然主義短編の規範作として『創造』『廃墟』同人誌世代の代表作と評価され、近代短編小説技法の確立に寄与。",
    historical_context="3・1運動後の文化政治期、植民地都市貧困層の構造的形成。",
    primary_source_url=WSRC_KO+"%EA%B0%90%EC%9E%90",
    primary_source_type="Wikisource Korean: 감자",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="廉想渉『万歳前』",
    name_en="Yom Sang-seop's Mansejeon",
    name_original="萬歲前",
    period_key="韓国近現代文学期",
    definition="廉想渉（1897-1963）が1922-24年に連載した中編小説。3・1運動（万歳運動）直前の植民地朝鮮を旅する東京留学生李寅華の視点で、植民地朝鮮社会の停滞・腐敗・民衆貧困を冷徹に描いた朝鮮近代リアリズムの起点的作品。",
    background="1920年代初頭の植民地朝鮮社会観察と、留学生視点による批判的距離化。",
    development="後の『三代』へ継承される廉想渉リアリズムの方法論的起点となり、解放後の韓国リアリズム長編の祖型と評価された。",
    historical_context="3・1運動（1919）直前の植民地朝鮮民衆生活の実相。",
    primary_source_url=WIKI_KO+"%EB%A7%8C%EC%84%B8%EC%A0%84",
    primary_source_type="Wikipedia Korean: 萬歲前",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="玄鎮健『運の良い日』",
    name_en="Hyon Jin-gon's A Lucky Day",
    name_original="운수 좋은 날",
    period_key="韓国近現代文学期",
    definition="玄鎮健（1900-1943）が1924年に発表した短編小説。京城の人力車夫キム僉知が稼ぎの良い一日の終わりに、留守中に病妻を失う皮肉な構造の短編で、朝鮮近代短編リアリズムの完成形。",
    background="1920年代植民地京城の人力車夫など下層労働者の生活実相と、ロシア・チェーホフ系短編小説技法の受容。",
    development="韓国短編小説技法の規範作として現代韓国国語教科書の定番となり、社会派短編の系譜的起点となった。",
    historical_context="文化政治期の植民地都市労働者層の構造的貧困。",
    primary_source_url=WSRC_KO+"%EC%9A%B4%EC%88%98_%EC%A2%8B%EC%9D%80_%EB%82%A0",
    primary_source_type="Wikisource Korean: 운수 좋은 날",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="崔曙海『脱出記』",
    name_en="Choe Sohae's Talchulgi",
    name_original="脫出記",
    period_key="韓国近現代文学期",
    definition="崔曙海（1901-1932）が1925年に発表した中編小説。植民地期間島地方に流れた朝鮮人小作農一家の極限貧困と、主人公の社会主義者化への転換を描く朝鮮プロレタリア文学の起点的作品。",
    background="1920年代間島・北満州への朝鮮人移住、KAPF（朝鮮プロレタリア芸術家同盟）結成期。",
    development="KAPF文学の起点的代表作となり、解放後北朝鮮文学・南韓民衆文学双方の系譜的源流として評価された。",
    historical_context="1920年代植民地朝鮮民衆の北方移住と、社会主義思想流入。",
    primary_source_url=WSRC_KO+"%ED%83%88%EC%B6%9C%EA%B8%B0",
    primary_source_type="Wikisource Korean: 脫出記",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="金素月『つつじの花』",
    name_en="Kim Sowol's Azaleas",
    name_original="진달래꽃",
    period_key="韓国近現代文学期",
    definition="金素月（1902-1934）の代表詩集（1925年刊）。表題詩「つつじの花」は朝鮮民謡的律調と恋愛喪失モチーフを融合し、植民地期朝鮮抒情詩の最高峰として現代韓国国民的愛唱詩の地位を確立。",
    background="1920年代朝鮮抒情詩運動と、民謡調を近代詩に再構成する試み。岸曙金億の指導下にあった素月の独自展開。",
    development="解放後の朝鮮民族抒情詩の規範作となり、韓国国語教科書の定番、現代K-POP歌詞にも引用される民族詩的源泉。",
    historical_context="文化政治期の朝鮮抒情詩黄金期。",
    primary_source_url=WSRC_KO+"%EC%A7%84%EB%8B%AC%EB%9E%98%EA%BD%83",
    primary_source_type="Wikisource Korean: 진달래꽃",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="韓龍雲『君の沈黙』",
    name_en="Han Yong-un's Nimui Chimmuk",
    name_original="님의 沈默",
    period_key="韓国近現代文学期",
    definition="独立運動家・仏僧韓龍雲（1879-1944）が1926年に刊行した詩集。88編の自由詩からなり、「君（ニム）」を絶対者・恋人・祖国・仏陀の重層的象徴として機能させた、朝鮮近代仏教詩・抵抗詩の最高峰。",
    background="3・1独立宣言33人代表の韓龍雲が、植民地統治下で仏教改革と民族抵抗を詩に結晶化する試み。",
    development="解放後の韓国民族文学・仏教文学の双方で正典化され、現代韓国精神文化の核心的詩集として評価される。",
    historical_context="1920年代植民地朝鮮の文化抵抗と仏教改革運動期。",
    primary_source_url=WSRC_KO+"%EB%8B%98%EC%9D%98_%EC%B9%A8%EB%AC%B5",
    primary_source_type="Wikisource Korean: 님의 沈默",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"韓龍雲の「ニム（君）」概念は単一主体を超えた重層的象徴主体性を提示し、AI時代の多重ペルソナ・象徴主体論の歴史的祖型となる。",
         "related_ai_phenomenon":"AI生成における多重象徴主体・ペルソナ重層化"}])

add(**C, name_ja="鄭芝溶『郷愁』",
    name_en="Jeong Ji-yong's Hyangsu",
    name_original="鄕愁",
    period_key="韓国近現代文学期",
    definition="鄭芝溶（1902-1950）が1927年に発表した詩。忠清北道沃川の故郷風景を映像的・モダニズム的言語で描き、近代抒情詩と土着的感性を融合した代表作。後にイ・ドンウォンによる歌曲化（1989）でも国民的に愛唱される。",
    background="1920-30年代朝鮮モダニズム詩運動と『詩文学』『九人会』活動。鄭芝溶の同志社大学英文科留学経験。",
    development="解放後北朝鮮へ移動・粛清により長く禁書となるが1988年解禁、現代韓国モダニズム抒情詩の正典として再評価された。",
    historical_context="文化政治期のモダニズム詩運動と、知識人の朝鮮固有性探求。",
    primary_source_url=WSRC_KO+"%ED%96%A5%EC%88%98",
    primary_source_type="Wikisource Korean: 鄕愁",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="李箱『烏瞰図』",
    name_en="Yi Sang's Crow's Eye View",
    name_original="烏瞰圖",
    period_key="韓国近現代文学期",
    definition="李箱（1910-1937）が1934年朝鮮中央日報に連載した連作詩。15編からなり、数式・幾何・断章的散文を組み合わせた朝鮮モダニズム詩の極端な実験。連載中止に追い込まれた、東アジア詩史最大の前衛的事件。",
    background="1930年代京城の九人会モダニズム運動と、ヨーロッパ前衛詩・ダダの極端な受容。",
    development="戦後韓国実験詩・コンクリート詩の祖型となり、金春洙ら無意味詩派、現代韓国前衛詩の系譜的源泉となった。",
    historical_context="1930年代植民地モダニズム文学の前衛的極北。",
    primary_source_url=WSRC_KO+"%EC%98%A4%EA%B0%90%EB%8F%84",
    primary_source_type="Wikisource Korean: 烏瞰圖",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"『烏瞰図』の数式・記号・断章的言語は意味伝達を破壊する詩的実験であり、AI生成テキストにおける記号操作・意味の脱臼との理論的並行性を持つ。",
         "related_ai_phenomenon":"AI生成における記号操作・意味解体"}])

add(**C, name_ja="朴泰遠『川辺の風景』",
    name_en="Park Tae-won's Cheonbyeon Pung-gyeong",
    name_original="川邊風景",
    period_key="韓国近現代文学期",
    definition="朴泰遠（1909-1986）が1936-37年に連載した長編モダニズム小説。京城清渓川辺の50余の市民群像を映画的モンタージュ手法で描き、植民地都市の日常を断章的に集積した朝鮮モダニズム長編の代表作。",
    background="1930年代京城のモダニズム作家群「九人会」活動と、ジョイス『ユリシーズ』的都市小説の朝鮮的展開。",
    development="解放後北朝鮮へ移動。長く禁書となるが1988年解禁後、現代韓国モダニズム長編小説の正典として再評価された。",
    historical_context="1930年代後半京城（ソウル）の都市文化最盛期。",
    primary_source_url=WIKI_KO+"%EC%B2%9C%EB%B3%80%ED%92%8D%EA%B2%BD",
    primary_source_type="Wikipedia Korean: 川邊風景",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="姜敬愛『人間問題』",
    name_en="Kang Kyong-ae's Ingangmunje",
    name_original="人間問題",
    period_key="韓国近現代文学期",
    definition="姜敬愛（1906-1944）が1934年に東亜日報連載した長編小説。植民地期間島・東興工場・仁川を舞台に、農民の娘善妃の労働者としての覚醒と挫折を描く朝鮮プロレタリア女性文学の最高峰。",
    background="1930年代植民地朝鮮の農村崩壊・都市流入・女性労働者問題と、KAPF系プロレタリア女性文学の興隆。",
    development="解放後北朝鮮文学・南韓フェミニズム文学双方の系譜的源流として、近年再評価が進む女性作家の代表作。",
    historical_context="1930年代植民地朝鮮の女性労働者・農村女性の構造的搾取。",
    primary_source_url=WIKI_KO+"%EC%9D%B8%EA%B0%84%EB%AC%B8%EC%A0%9C",
    primary_source_type="Wikipedia Korean: 人間問題",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: 韓国現代深掘り（10件）
# ============================================================
add(**C, name_ja="黄順元『にわか雨』",
    name_en="Hwang Sun-won's Sonagi",
    name_original="소나기",
    period_key="韓国近現代文学期",
    definition="黄順元（1915-2000）が1953年に発表した短編小説。少年と少女の純粋な交流と少女の早世を描き、戦後韓国短編リアリズムの叙情的最高峰として現代韓国国語教科書の定番、国民的愛読作となった。",
    background="韓国戦争（1950-53）終結直後の戦後復興期、純粋叙情への文学的回帰。",
    development="戦後韓国短編小説の規範作となり、ドラマ・映画・絵本に繰り返し翻案された国民的物語。",
    historical_context="休戦協定直後の戦後復興期と、純粋叙情の文学的需要。",
    primary_source_url=WSRC_KO+"%EC%86%8C%EB%82%98%EA%B8%B0",
    primary_source_type="Wikisource Korean: 소나기",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="崔仁勲『広場』",
    name_en="Choi Inhun's The Square",
    name_original="廣場",
    period_key="韓国近現代文学期",
    definition="崔仁勲（1936-2018）が1960年4・19革命直後に発表した中編小説。南北分断のなか、南の腐敗と北の独裁の双方を拒否し、第三国（中立国）行きの船上で投身する主人公李明俊を描く韓国分断文学の最高峰。",
    background="1960年4・19学生革命直後の言論自由化と、分断構造への批判的省察の必要性。",
    development="韓国分断文学の規範作となり、現代韓国知識人の中道主義・第三の道思想の文学的源流となった。",
    historical_context="李承晩政権崩壊後の短期民主化期と分断構造再認識。",
    primary_source_url=WIKI_KO+"%EA%B4%91%EC%9E%A5_(%EC%86%8C%EC%84%A4)",
    primary_source_type="Wikipedia Korean: 廣場 (소설)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『広場』の中立国を選ぶ主体性は二項対立を超える第三の主体を文学化し、AI時代の中間主体・多元主体論の歴史的祖型となる。",
         "related_ai_phenomenon":"AI時代の中立的・複数主体性"}])

add(**C, name_ja="李範宣『誤発弾』",
    name_en="Yi Bumseon's Obaltan (Stray Bullet)",
    name_original="誤發彈",
    period_key="韓国近現代文学期",
    definition="李範宣（1920-1981）が1959年に発表した短編小説。戦後ソウルの貧民街解放村に住む北からの避難民歯科技工士哲鎬一家の崩壊を描き、戦後韓国の精神的喪失感を象徴化した戦後文学の代表作。1961年兪賢穆監督が映画化。",
    background="韓国戦争後の北からの大量避難民問題と、戦後ソウル貧民街の構造的疲弊。",
    development="戦後韓国短編リアリズムの規範作となり、兪賢穆映画版（1961）と並んで戦後韓国文化の核心的作品となった。",
    historical_context="韓国戦争後の社会的混乱と避難民問題。",
    primary_source_url=WIKI_KO+"%EC%98%A4%EB%B0%9C%ED%83%84",
    primary_source_type="Wikipedia Korean: 誤發彈",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="朴婉緒『あの多くの草はだれが食べたのか』",
    name_en="Park Wan-suh's Geu Manon Singi-ranun-ji",
    name_original="그 많던 싱아는 누가 다 먹었을까",
    period_key="韓国近現代文学期",
    definition="朴婉緒（1931-2011）が1992年に発表した自伝的長編小説。植民地末期から韓国戦争期の少女期回想を通じ、20世紀韓国近代史を女性の視点から再構築した戦後韓国女性文学の傑作。",
    background="1990年代の女性作家自伝的小説興隆と、戦後韓国の歴史的記憶再構成への要請。",
    development="韓国女性文学の正典として広く愛読され、続編『あの山は本当にそこにあったのか』(1995)と併せて朴婉緒文学の核心となった。",
    historical_context="1990年代韓国民主化定着期の歴史的記憶再評価。",
    primary_source_url=WIKI_KO+"%EA%B7%B8_%EB%A7%8E%EB%8D%98_%EC%8B%B1%EC%95%84%EB%8A%94_%EB%88%84%EA%B0%80_%EB%8B%A4_%EB%A8%B9%EC%97%88%EC%9D%84%EA%B9%8C",
    primary_source_type="Wikipedia Korean: 그 많던 싱아",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="黄晳暎『張吉山』",
    name_en="Hwang Sok-yong's Jang Gilsan",
    name_original="張吉山",
    period_key="韓国近現代文学期",
    definition="黄晳暎（1943-）が1974-84年に韓国日報連載した長編歴史小説。10巻、朝鮮粛宗代の義賊張吉山を主人公に民衆抵抗史を再構成し、1970-80年代韓国民衆文学運動の頂点を成す大河歴史小説。",
    background="維新体制下の民衆文学運動と、朝鮮民衆英雄の現代的再発見。",
    development="韓国民衆文学の代表作として民主化運動世代の精神的支柱となり、後の歴史小説（趙廷来『太白山脈』）の先駆となった。",
    historical_context="朴正熙維新体制(1972-79)下の民衆文学運動最盛期。",
    primary_source_url=WIKI_KO+"%EC%9E%A5%EA%B8%B8%EC%82%B0",
    primary_source_type="Wikipedia Korean: 張吉山",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="李文烈『人間の子』",
    name_en="Yi Mun-yol's Saramui Adeul (Son of Man)",
    name_original="사람의 아들",
    period_key="韓国近現代文学期",
    definition="李文烈（1948-）が1979年に発表した中編小説。神学生南江臣の信仰葛藤と、副物語として2000年前のアハスエロスのキリスト教批判を並行展開する宗教哲学小説。今日の文学賞を受賞、現代韓国宗教文学の代表作。",
    background="1970年代後半の韓国知識人の宗教・実存問題関心と、ドストエフスキー的宗教哲学小説の現代韓国版展開。",
    development="現代韓国の知識人小説・宗教哲学小説の系譜的源流となり、李文烈文学の出発点として広く読まれる。",
    historical_context="維新体制末期の知識人実存問題期。",
    primary_source_url=WIKI_KO+"%EC%82%AC%EB%9E%8C%EC%9D%98_%EC%95%84%EB%93%A4",
    primary_source_type="Wikipedia Korean: 사람의 아들",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="韓江『すべての、白いものたちの』",
    name_en="Han Kang's The White Book",
    name_original="흰",
    period_key="韓国近現代文学期",
    definition="韓江（1970-、2024年ノーベル文学賞）が2016年に発表した詩的散文集。生後すぐ亡くなった姉への鎮魂を「白い」事物65編の連作で構成、ジャンル横断的散文詩集として2018年Man Booker International Prize最終候補となった。",
    background="2010年代韓江文学の詩的・哲学的展開と、家族喪失をめぐる個人的悲嘆。",
    development="2024年韓江ノーベル文学賞受賞により『菜食主義者』『少年が来る』と並んで国際的に最も読まれる現代韓国文学作品の一つとなった。",
    historical_context="2010年代韓国文学のグローバル化と、ジャンル横断的詩的散文の興隆。",
    primary_source_url=WIKI_KO+"%ED%9D%B0_(%ED%95%9C%EA%B0%95%EC%9D%98_%EC%86%8C%EC%84%A4)",
    primary_source_type="Wikipedia Korean: 흰 (한강)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"美学","status":"rethinking",
         "rationale":"韓江『白い』のジャンル横断詩的散文は、単一ジャンル枠を超える美学的実験であり、AI支援によるジャンル横断生成の理論的祖型。",
         "related_ai_phenomenon":"AI生成によるジャンル境界解体・横断的美学"}])

add(**C, name_ja="ファン・ジョンウン『年年歳歳』",
    name_en="Hwang Jung-eun's I'll Go On",
    name_original="계속해보겠습니다",
    period_key="韓国近現代文学期",
    definition="ファン・ジョンウン（1976-）が2014年に発表した連作長編小説。父の事故死を背景に三人の語り手（姉妹と隣人男性）が交錯する語りで、現代韓国の貧困・労働・家族喪失を描く2010年代韓国文学の代表作。",
    background="2010年代韓国の社会的不平等深化と、若年女性作家による新しい家族文学の興隆。",
    development="2018年ティルダ・ハットン英訳でMan Booker International Prize候補となり、現代韓国文学のグローバル化を牽引する作家として国際的評価を確立。",
    historical_context="セウォル号沈没事件(2014)前後の韓国社会の悲嘆と再生の問題化期。",
    primary_source_url=WIKI_KO+"%ED%99%A9%EC%A0%95%EC%9D%80",
    primary_source_type="Wikipedia Korean: 황정은",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="キム・ヨンハ『私には破壊する権利がある』",
    name_en="Kim Young-ha's I Have the Right to Destroy Myself",
    name_original="나는 나를 파괴할 권리가 있다",
    period_key="韓国近現代文学期",
    definition="キム・ヨンハ（1968-）が1996年に発表したデビュー長編小説。自殺幇助業者を語り手に、現代ソウルの孤独・性愛・芸術消費を描いた90年代韓国文学のミレニアル世代代表作。",
    background="1990年代後半韓国文学のポストモダン的展開と、IMF危機（1997）前夜の文化的不安。",
    development="2007年Chi-Young Kim英訳でアジア太平洋地域文学賞、現代韓国文学グローバル化の先駆けとなった。",
    historical_context="IMF経済危機直前の韓国文化変動期。",
    primary_source_url=WIKI_KO+"%EB%82%98%EB%8A%94_%EB%82%98%EB%A5%BC_%ED%8C%8C%EA%B4%B4%ED%95%A0_%EA%B6%8C%EB%A6%AC%EA%B0%80_%EC%9E%88%EB%8B%A4",
    primary_source_type="Wikipedia Korean: 나는 나를 파괴할 권리가 있다",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パク・サンヨン『大都会の愛し方』",
    name_en="Park Sang-young's Love in the Big City",
    name_original="대도시의 사랑법",
    period_key="韓国近現代文学期",
    definition="パク・サンヨン（1988-）が2019年に発表した連作長編小説。ソウルのゲイ男性主人公ヨンの愛と喪失を4編の連作で描き、2022年Man Booker International Prize候補となった韓国LGBTQ文学の代表作。",
    background="2010年代後半韓国のLGBTQ可視化進展と、若手作家によるクィア文学興隆。",
    development="アントン・ハー英訳で国際的ベストセラーとなり、現代韓国クィア文学のグローバル化を象徴する作品となった。",
    historical_context="2010-20年代韓国のジェンダー多様性議論深化期。",
    primary_source_url=WIKI_KO+"%EB%8C%80%EB%8F%84%EC%8B%9C%EC%9D%98_%EC%82%AC%EB%9E%91%EB%B2%95",
    primary_source_type="Wikipedia Korean: 대도시의 사랑법",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"パク・サンヨンのクィア主体表現は単一規範的アイデンティティを超えた多層的主体を文学化し、AI時代の多重・流動的主体性の現代的祖型。",
         "related_ai_phenomenon":"AI時代の流動的・非規範的主体表象"}])


# ============================================================
# D: ベトナム文学詳細（8件）
# ============================================================
add(**C, name_ja="阮廌『平呉大誥』",
    name_en="Nguyễn Trãi's Bình Ngô Đại Cáo",
    name_original="平吳大誥",
    period_key="ベトナム古典・近世文学期",
    definition="ベトナム黎朝開祖の謀臣阮廌（1380-1442）が1428年に黎利の名で発した、明朝撃退宣言の漢文檄文。ベトナム独立宣言文書の祖型として、文体的精緻と民族意識の文学化により「ベトナム第二の独立宣言」と称される。",
    background="14世紀末から15世紀初の明朝ベトナム支配（1407-1428）と、藍山起義による民族独立達成。",
    development="20世紀のホー・チ・ミン独立宣言（1945）の歴史的源流として位置づけられ、ベトナム民族文学の正典中の正典となった。",
    historical_context="明朝撃退と黎朝建国期。",
    primary_source_url=WSRC_VI+"B%C3%ACnh_Ng%C3%B4_%C4%91%E1%BA%A1i_c%C3%A1o",
    primary_source_type="Wikisource Vietnamese: Bình Ngô Đại Cáo",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"民族独立宣言と文学的正統性",
         "description":"『平呉大誥』はベトナム民族意識の文学的形式化として、人類学的民族主義研究の対象。"}])

add(**C, name_ja="阮秉謙『白雲国語詩集』",
    name_en="Nguyễn Bỉnh Khiêm's Bạch Vân Quốc Ngữ Thi",
    name_original="白雲國語詩集",
    period_key="ベトナム古典・近世文学期",
    definition="16世紀ベトナムの儒者・予言者阮秉謙（1491-1585）が著した字喃（チュノム）詩集。約170首を収録し、隠逸思想・道徳訓戒を字喃で表現した中世ベトナム字喃文学の重要資料。",
    background="莫朝期（1527-92）の動乱期と、阮秉謙の隠逸者としての精神的姿勢。",
    development="ベトナム字喃文学の重要源流となり、阮攸『金雲翹』に至るベトナム字喃文学の発展系譜の中核を占める。",
    historical_context="16世紀ベトナム南北分裂期の儒者隠逸文化。",
    primary_source_url=WSRC_VI+"B%E1%BA%A1ch_V%C3%A2n_qu%E1%BB%91c_ng%E1%BB%AF_thi",
    primary_source_type="Wikisource Vietnamese: Bạch Vân Quốc Ngữ Thi",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="段氏點『征婦吟曲』訳",
    name_en="Đoàn Thị Điểm's Chinh Phụ Ngâm translation",
    name_original="征婦吟曲",
    period_key="ベトナム古典・近世文学期",
    definition="18世紀ベトナム女性詩人段氏點（1705-1748）が、鄧陳琨の漢詩『征婦吟』を字喃の双七六八体に訳した長編詩。412行、夫を戦地に送る妻の哀情を字喃の韻律で再構成し、ベトナム女性文学の頂点を成す。",
    background="18世紀ベトナム鄭阮抗争期の戦乱と、女性知識人による字喃詩翻案文化。",
    development="阮攸『金雲翹』とともにベトナム字喃詩双璧と評価され、現代ベトナム国語教育の核心教材となった。",
    historical_context="18世紀ベトナム鄭阮抗争期の女性文学興隆。",
    primary_source_url=WSRC_VI+"Chinh_ph%E1%BB%A5_ng%C3%A2m",
    primary_source_type="Wikisource Vietnamese: Chinh phụ ngâm",
    importance_score=4, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="武仲奉『紅楼夢』翻案",
    name_en="Vũ Trọng Phụng's Số Đỏ (Dumb Luck)",
    name_original="Số Đỏ",
    period_key="ベトナム近現代文学期",
    definition="武仲奉（1912-1939）が1936年に発表した諷刺長編小説。仏領期ハノイの新興ブルジョワジー社会の偽善・浅薄を、主人公スアン・トック・ドの偶然的出世を通じて諷刺した、ベトナム近代諷刺小説の最高峰。",
    background="1930年代仏領インドシナの都市近代化と、現代化を装う植民地ブルジョワジー社会への批判精神。",
    development="ベトナム近代諷刺文学の規範作となり、現代ベトナム国語教育の定番となった。2008年映画化、英訳普及で国際的評価も確立。",
    historical_context="1930年代仏領インドシナのモダン文化期。",
    primary_source_url=WIKI_VI+"S%E1%BB%91_%C4%91%E1%BB%8F",
    primary_source_type="Wikipedia Vietnamese: Số đỏ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="南高『チ・フェオ』",
    name_en="Nam Cao's Chí Phèo",
    name_original="Chí Phèo",
    period_key="ベトナム近現代文学期",
    definition="南高（1915-1951）が1941年に発表した短編小説。仏領期紅河デルタ村落で社会的に排除された「酔いどれ」チ・フェオの悲劇を通じて、ベトナム植民地農村の構造的暴力を描いた写実主義文学の代表作。",
    background="1940年代仏領インドシナの農村疲弊と、ベトナム自然主義・写実主義文学運動。",
    development="現代ベトナム国語教育の核心教材となり、解放後ベトナム民衆文学・革命文学の系譜的源流として位置づけられた。",
    historical_context="第二次大戦下の仏領インドシナ農村危機。",
    primary_source_url=WIKI_VI+"Ch%C3%AD_Ph%C3%A8o",
    primary_source_type="Wikipedia Vietnamese: Chí Phèo",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="阮輝説『退役将軍』",
    name_en="Nguyen Huy Thiep's The General Retires",
    name_original="Tướng về hưu",
    period_key="ベトナム近現代文学期",
    definition="阮輝説（1950-2021）が1987年に発表した短編小説。退役した北ベトナム軍将軍の家庭崩壊を通じ、ドイモイ前夜のベトナム社会の道徳的解体を描いたベトナム・ドイモイ文学の起点的作品。",
    background="1986年ドイモイ政策発表前後のベトナム文学検閲緩和と、社会道徳的危機への文学的応答。",
    development="ベトナム・ドイモイ文学の起点として国際的評価を確立、英訳・仏訳・日訳でアジア現代文学の重要作家となった。",
    historical_context="ドイモイ（1986）開放政策初期のベトナム社会変動期。",
    primary_source_url=WIKI_VI+"Nguy%E1%BB%85n_Huy_Thi%E1%BB%87p",
    primary_source_type="Wikipedia Vietnamese: Nguyễn Huy Thiệp",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"阮輝説は社会主義国家における主体性を批判的に脱構築し、AI時代の集団主体・国家主体の問い直しの理論的祖型となる。",
         "related_ai_phenomenon":"AI時代の集団的主体性の批判的再考"}])

add(**C, name_ja="ファム・ティ・ホアイ",
    name_en="Pham Thi Hoai",
    name_original="Phạm Thị Hoài",
    period_key="ベトナム近現代文学期",
    definition="ファム・ティ・ホアイ（1960-）はベトナム女性作家。代表作『天使』(1989)、『沈黙の壁』(1991)等。1994年ドイツ亡命後ベルリン拠点、ベトナム語独語両言語で執筆、ベトナム・ディアスポラ文学の代表作家。",
    background="1980年代後半ベトナム短期文化開放期と、その後の検閲復活による作家亡命。",
    development="ベルリン拠点でベトナム文化批判ウェブ誌『talawas』(2001-2010)主宰、トランスナショナル・ベトナム文学の中心人物となった。",
    historical_context="ドイモイ初期の言論開放と亡命のサイクル。",
    primary_source_url=WIKI_EN+"Ph%E1%BA%A1m_Th%E1%BB%8B_Ho%C3%A0i",
    primary_source_type="Wikipedia: Phạm Thị Hoài",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="オーシャン・ヴオン",
    name_en="Ocean Vuong",
    name_original="Ocean Vuong",
    period_key="ベトナム近現代文学期",
    definition="オーシャン・ヴオン（1988-、ベトナム生まれ・米国育ち）は詩人・小説家。詩集『銃で撃つ夜空 Night Sky with Exit Wounds』(2016、T.S.エリオット賞)、長編『地上で僕らはつかの間の輝き』(2019)で国際的評価を確立したベトナム系米国文学の旗手。",
    background="ベトナム戦争難民第二世代の精神的継承と、米国LGBTQ文学・移民文学の交差点。",
    development="2019年MacArthurフェロー、米国詩・小説両分野で頂点級評価を獲得し、東南アジア・ディアスポラ文学のグローバル化を象徴する作家となった。",
    historical_context="2010年代米国における移民・LGBTQ・ベトナム系の文化的可視化。",
    primary_source_url=WIKI_EN+"Ocean_Vuong",
    primary_source_type="Wikipedia: Ocean Vuong",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"翻訳","status":"rethinking",
         "rationale":"ヴオンの英語ベトナム系文学は、戦争難民の言語的喪失と再獲得を文学化し、AI翻訳時代の言語移行・記憶の課題に直結する。",
         "related_ai_phenomenon":"AI翻訳と移民言語経験"}])


# ============================================================
# E: タイ文学詳細（5件）
# ============================================================
add(**C, name_ja="スントーン・プー『プラ・アパイ・マニ』",
    name_en="Sunthorn Phu's Phra Aphai Mani",
    name_original="พระอภัยมณี",
    period_key="タイ古典・宮廷文学期",
    definition="ラタナコーシン朝の宮廷詩人スントーン・プー（1786-1855）が1822-44年頃に著した長編叙事詩。約3万行、王子プラ・アパイ・マニの海洋冒険譚で、タイ古典文学最大の叙事詩・国民的物語。",
    background="ラーマ二世（1809-24）期のタイ宮廷文学最盛期と、スントーン・プーの宮廷詩人としての活動。",
    development="現代タイ国民文学の頂点として、教科書定番・テレビドラマ・アニメに繰り返し翻案され、タイ文化的アイデンティティの核となった。",
    historical_context="ラタナコーシン朝初期のタイ宮廷文学黄金期。",
    primary_source_url=WSRC_TH+"%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%AD%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%A1%E0%B8%93%E0%B8%B5",
    primary_source_type="Wikisource Thai: พระอภัยมณี",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="クラープ・サイプラディット『絵画の背景』",
    name_en="Kulap Saipradit's Behind the Painting",
    name_original="ข้างหลังภาพ",
    period_key="タイ近現代文学期",
    definition="クラープ・サイプラディット（筆名シーブーラパー、1905-1974）が1937年に発表した長編小説。日本留学中のタイ青年ノパポーンと既婚貴族女性キーラティーの悲恋を描き、戦前タイ近代恋愛小説の最高峰。",
    background="1930年代タイ立憲革命（1932）後の文化近代化と、東京・京都への留学体験を文学化する試み。",
    development="現代タイ恋愛小説の規範作となり、複数回映画化（2001年版が代表的）、タイ国語教育の定番教材となった。",
    historical_context="ピブーン政権下のタイ文化的近代化期。",
    primary_source_url=WIKI_TH+"%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%9E",
    primary_source_type="Wikipedia Thai: ข้างหลังภาพ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カムシン・シーノーク『政治家』",
    name_en="Khamsing Srinawk's The Politician",
    name_original="ฟ้าบ่กั้น",
    period_key="タイ近現代文学期",
    definition="カムシン・シーノーク（1930-）が1958-69年に短編集『フェ・ボー・カン（空は仕切らない）』に収めた連作短編。東北タイ・イサーン地方農民の苦闘を、写実的方言とユーモアで描き、タイ農村文学の頂点を成した。",
    background="1950-60年代タイ・イサーン地方の構造的貧困と、首都との文化的格差。",
    development="現代タイ短編小説の規範作となり、英訳でアジア英語文学に貢献、タイ国民文学賞、東南アジア地域文学賞（SEA Write Award）受賞。",
    historical_context="冷戦下タイの東北部開発・米軍基地時代。",
    primary_source_url=WIKI_TH+"%E0%B8%84%E0%B8%B3%E0%B8%AA%E0%B8%B4%E0%B8%87_%E0%B8%A8%E0%B8%A3%E0%B8%B5%E0%B8%99%E0%B8%AD%E0%B8%81",
    primary_source_type="Wikipedia Thai: คำสิงห์ ศรีนอก",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウィモン・サイニムヌアン『アマタ』",
    name_en="Wimon Sainimnuan's Amata",
    name_original="อมตะ",
    period_key="タイ近現代文学期",
    definition="ウィモン・サイニムヌアン（1955-）が2000年に発表した長編小説。生命科学の発展で不死を獲得した富豪と、その不死を維持するため臓器を提供させられる若者を描き、タイSF・倫理小説の代表作。2000年タイS.E.A. Write Award受賞。",
    background="2000年前後の生命倫理問題のタイ社会的議論と、SF的主題の主流化。",
    development="現代タイSFの代表作として東南アジア地域文学賞を受賞、タイ近代倫理小説の系譜を構築した。",
    historical_context="2000年代タイのバイオテクノロジー・倫理議論期。",
    primary_source_url=WIKI_TH+"%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B8%B0_(%E0%B8%99%E0%B8%A7%E0%B8%99%E0%B8%B4%E0%B8%A2%E0%B8%B2%E0%B8%A2)",
    primary_source_type="Wikipedia Thai: อมตะ",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"『アマタ』の不死・臓器提供主題は人間身体の所有権を問い、AI・バイオ技術時代の人間主体性問題の文学的祖型となる。",
         "related_ai_phenomenon":"AI・バイオ時代の身体所有・主体性問題"}])

add(**C, name_ja="ウィン・リョウワーリン『シャム機械人形』",
    name_en="Win Lyovarin's Sayam Hun Yon",
    name_original="สยามหุ่นยนต์",
    period_key="タイ近現代文学期",
    definition="ウィン・リョウワーリン（1956-）が1995年に発表した長編SF小説。アユタヤ朝期の政治的陰謀を機械仕掛けの人形を通じて再構成する歴史改変SFで、現代タイSFの先駆け。1997年タイS.E.A. Write Award受賞。",
    background="1990年代タイのSF・歴史改変文学興隆と、アユタヤ史への新解釈。",
    development="タイSF・歴史改変文学の規範作となり、ウィン・リョウワーリンを現代タイ文学の代表作家の地位に押し上げた。",
    historical_context="1990年代タイ経済成長期のジャンル文学拡大。",
    primary_source_url=WIKI_TH+"%E0%B8%A7%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%A3%E0%B9%8C_%E0%B9%80%E0%B8%A5%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%A7%E0%B8%A3%E0%B8%B4%E0%B8%99",
    primary_source_type="Wikipedia Thai: วินทร์ เลียววาริณ",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# F: インドネシア・マレー（7件）
# ============================================================
add(**C, name_ja="プラムディヤ『人間の大地』（ブル四部作I）",
    name_en="Pramoedya's Earth of Mankind",
    name_original="Bumi Manusia",
    period_key="インドネシア・マレーシア近現代期",
    definition="プラムディヤ・アナンタ・トゥール（1925-2006）がブル島強制収容所で口述、1980年に発表した長編小説。蘭領東インド時代のジャワ青年ミンケと混血ヌヤイ・オントソローの愛と植民地差別を描く、ブル四部作の第一巻。",
    background="1965年9月30日事件後の長期収容下で口述創作、収容所文学の最高峰。",
    development="出版禁止（1981-1998）解除後、現代インドネシア文学の最重要作品となり、英訳マックス・レイン版で国際的に広く読まれる。",
    historical_context="スハルト体制下の言論統制とプラムディヤの収容所体験。",
    primary_source_url=WIKI_ID+"Bumi_Manusia",
    primary_source_type="Wikipedia Indonesian: Bumi Manusia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="マラ・ルスリ『シティ・ヌルバヤ』",
    name_en="Marah Roesli's Sitti Nurbaya",
    name_original="Sitti Nurbaya",
    period_key="インドネシア・マレーシア近現代期",
    definition="マラ・ルスリ（1889-1968）が1922年Balai Pustaka社から出版した長編小説。西スマトラ・ミナンカバウ社会の強制結婚に苦しむシティ・ヌルバヤを描き、インドネシア近代小説の起点的作品。",
    background="1920年代蘭領東インドBalai Pustaka社の現地語近代小説出版事業と、ミナンカバウ社会の慣習批判。",
    development="現代インドネシア国語教育の核心教材として、インドネシア近代小説の祖型と評価された。",
    historical_context="1920年代蘭領東インドの女性問題・現代化議論期。",
    primary_source_url=WIKI_ID+"Sitti_Nurbaya",
    primary_source_type="Wikipedia Indonesian: Sitti Nurbaya",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハムカ『ファン・デル・ウェイク号の沈没』",
    name_en="Hamka's Tenggelamnya Kapal Van Der Wijck",
    name_original="Tenggelamnya Kapal Van Der Wijck",
    period_key="インドネシア・マレーシア近現代期",
    definition="ハジ・アブドゥル・マリク・カリム・アムルラ（筆名ハムカ、1908-1981）が1938年に発表した長編小説。西スマトラ青年ザイヌッディンの結婚悲劇とファン・デル・ウェイク号沈没事件を融合した、戦前インドネシア・イスラーム恋愛小説の代表作。",
    background="1930年代蘭領東インドのイスラーム改革思想とミナンカバウ慣習批判の文学化。",
    development="現代インドネシア国語教科書の定番、2013年映画版が国民的ヒット、インドネシア・イスラーム文学の系譜的源流となった。",
    historical_context="1930年代蘭領東インドのイスラーム近代化運動期。",
    primary_source_url=WIKI_ID+"Tenggelamnya_Kapal_Van_der_Wijck",
    primary_source_type="Wikipedia Indonesian: Tenggelamnya Kapal Van der Wijck",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モホタール・ルビス『たそがれのジャカルタ』",
    name_en="Mochtar Lubis's Twilight in Jakarta",
    name_original="Senja di Jakarta",
    period_key="インドネシア・マレーシア近現代期",
    definition="モホタール・ルビス（1922-2004）が1963年（インドネシア語版1970）に発表した長編小説。スカルノ期ジャカルタの政治腐敗・貧困・道徳的退廃を描き、独立後インドネシア政治批判文学の代表作。",
    background="1950-60年代スカルノ「指導される民主主義」期の社会的退廃と、ルビス自身の長期投獄体験。",
    development="現代インドネシア政治小説の規範作として、スハルト期にも禁書扱いだったが解禁後、再評価が進んだ。",
    historical_context="スカルノ末期の社会的退廃と権威主義的支配。",
    primary_source_url=WIKI_ID+"Senja_di_Jakarta",
    primary_source_type="Wikipedia Indonesian: Senja di Jakarta",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エカ・クルニアワン『虎人間』",
    name_en="Eka Kurniawan's Lelaki Harimau",
    name_original="Lelaki Harimau",
    period_key="インドネシア・マレーシア近現代期",
    definition="エカ・クルニアワン（1975-）が2004年に発表した長編小説。ジャワの寒村で母を辱めた者を殺害する若者マルギオに、白い虎の霊が宿る筋立て。マジック・リアリズムと家族暴力主題を融合した現代インドネシア文学の代表作。",
    background="2000年代インドネシアのポストスハルト民主化期と、マルケス的マジック・リアリズム受容。",
    development="2016年Man Booker International Prize候補（『美はそこにある傷』と並んで）、現代インドネシア文学のグローバル化を牽引する作家として国際的評価を確立。",
    historical_context="ポストスハルト民主化期のインドネシア文学グローバル化。",
    primary_source_url=WIKI_ID+"Lelaki_Harimau",
    primary_source_type="Wikipedia Indonesian: Lelaki Harimau",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="レイラ・チュドリ『帰還』",
    name_en="Leila Chudori's Pulang (Home)",
    name_original="Pulang",
    period_key="インドネシア・マレーシア近現代期",
    definition="レイラ・チュドリ（1962-）が2012年に発表した長編小説。1965年9月30日事件で亡命したインドネシア知識人ディマス・スリヤらのパリ亡命生活と、その娘リンタの1998年ジャカルタ訪問を交錯させ、戦後インドネシア政治史を再構成した代表作。",
    background="2010年代の1965年事件再評価運動と、亡命知識人の歴史的記憶再構成。",
    development="2017年John H. McGlynn英訳で国際的評価を獲得、現代インドネシア・ディアスポラ文学の代表作家となった。",
    historical_context="1965年事件50周年前後の歴史的記憶再評価期。",
    primary_source_url=WIKI_ID+"Pulang_(novel)",
    primary_source_type="Wikipedia Indonesian: Pulang",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="A・サマド・サイド『サリナ』",
    name_en="A. Samad Said's Salina",
    name_original="Salina",
    period_key="インドネシア・マレーシア近現代期",
    definition="A・サマド・サイド（1935-）が1961年に発表したマレー語長編小説。シンガポール慰安婦街を舞台に主人公サリナの困難を描き、戦後マレー語文学の頂点を成した。マレーシア国民文学賞、SEA Write Award受賞作。",
    background="1950-60年代マレー語近代小説の本格的展開と、戦後シンガポール社会への文学的省察。",
    development="マレーシア国民文学賞作家A・サマド・サイドの代表作として、現代マレー語文学の正典となった。",
    historical_context="1960年代シンガポール・マレーシア分離期前後の社会変動。",
    primary_source_url=WIKI_EN+"Salina_(novel)",
    primary_source_type="Wikipedia: Salina (novel)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# G: フィリピン（5件）
# ============================================================
add(**C, name_ja="ロペ・K・サントス『朝焼けと日の出』",
    name_en="Lope K. Santos's Banaag at Sikat",
    name_original="Banaag at Sikat",
    period_key="フィリピン近現代文学期",
    definition="ロペ・K・サントス（1879-1963）が1906年に発表したタガログ語長編小説。スペイン期から米領期初期のフィリピンの社会主義思想流入を、青年デルフィンとフェリペの交友・恋愛を通じて描き、フィリピン社会主義文学の祖となった。",
    background="20世紀初頭フィリピンの米領化に伴う社会主義・労働運動思潮流入と、タガログ語近代小説の本格化。",
    development="現代フィリピン国語教育の核心教材となり、フィリピン社会主義文学の系譜的源流として位置づけられた。",
    historical_context="米西戦争(1898)後のフィリピン米領期初期。",
    primary_source_url=WIKI_FIL+"Banaag_at_Sikat",
    primary_source_type="Wikipedia Tagalog: Banaag at Sikat",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ニック・ホアキン『熱帯のゴシック』",
    name_en="Nick Joaquin's Tropical Gothic",
    name_original="Tropical Gothic",
    period_key="フィリピン近現代文学期",
    definition="ニック・ホアキン（1917-2004）が1972年に刊行した短編集。スペイン期マニラの植民地遺産・宗教・性をゴシック的雰囲気で描き、フィリピン英語文学の頂点的短編集として広く評価される。",
    background="20世紀後半フィリピン英語文学のスペイン的遺産再評価と、マルケス的マジック・リアリズム受容。",
    development="現代フィリピン英語文学の規範作として、ホアキンを国民的作家の地位に確立した代表的短編集。",
    historical_context="マルコス政権初期のフィリピン文化的アイデンティティ探求期。",
    primary_source_url=WIKI_EN+"Nick_Joaquin",
    primary_source_type="Wikipedia: Nick Joaquin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ビエンベニド・サントス『りんごの香り』",
    name_en="Bienvenido Santos's Scent of Apples",
    name_original="Scent of Apples",
    period_key="フィリピン近現代文学期",
    definition="ビエンベニド・サントス（1911-1996）が1979年に刊行した短編集。米国移住フィリピン人「マノン世代」の故郷喪失・孤独を描き、1980年American Book Award受賞、フィリピン系米国文学の祖型を確立した。",
    background="20世紀前半の米国移住フィリピン人マノン労働者世代の歴史的経験と、1970年代米国の移民文学興隆。",
    development="現代フィリピン系米国文学の規範作として、ジェシカ・ハグドルン以降のフィリピン系米国作家の系譜的源流となった。",
    historical_context="米国移住フィリピン人世代の集団的記憶確立期。",
    primary_source_url=WIKI_EN+"Bienvenido_Santos",
    primary_source_type="Wikipedia: Bienvenido Santos",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ホセ・ガルシア・ヴィラ『来たり、ここに在り』",
    name_en="Jose Garcia Villa's Have Come, Am Here",
    name_original="Have Come, Am Here",
    period_key="フィリピン近現代文学期",
    definition="ホセ・ガルシア・ヴィラ（1908-1997）が1942年に刊行した詩集。「コンマ詩」「逆韻」など実験的技法で、20世紀前半英米モダニズム詩の主流に参入したフィリピン人最初の詩人。E・E・カミングス、エディス・シットウェルらと交流。",
    background="1930-40年代フィリピン人作家の米国モダニズム圏進出と、ヴィラの長期米国滞在。",
    development="現代フィリピン英語詩の祖型として、20世紀東南アジア英語詩の最初の国際的成功例となった。",
    historical_context="第二次大戦下の米国でのフィリピン系作家の文学的成功。",
    primary_source_url=WIKI_EN+"Jos%C3%A9_Garcia_Villa",
    primary_source_type="Wikipedia: José Garcia Villa",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="F・シオニル・ホセ『ロサーレス・サーガ』第三巻『土地』",
    name_en="F. Sionil Jose's Po-on (Tree)",
    name_original="Po-on",
    period_key="フィリピン近現代文学期",
    definition="F・シオニル・ホセ（1924-2022）が1984年に発表した『ロサーレス五部作』第一作。19世紀末イロコス地方からパンガシナンへの移住農民サマソン家の物語を通じ、フィリピン独立闘争史を再構成した代表的歴史長編小説。",
    background="20世紀後半フィリピンのイロカノ系民衆史再評価と、五部作構想による国民的歴史叙事の試み。",
    development="現代フィリピン英語長編小説の規範作として、ホセ自身の国際的代表作となり、フィリピン国民文学の正典に位置づけられた。",
    historical_context="マルコス体制下のフィリピン民族史再評価期。",
    primary_source_url=WIKI_EN+"F._Sionil_Jos%C3%A9",
    primary_source_type="Wikipedia: F. Sionil José",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H: ビルマ・カンボジア・ラオス（2件）
# ============================================================
add(**C, name_ja="キン・ミョー・チッ『13カラットのダイヤモンド』",
    name_en="Khin Myo Chit's 13 Carat Diamond",
    name_original="13 Carat Diamond",
    period_key="ビルマ（ミャンマー）古典・近代期",
    definition="キン・ミョー・チッ（1915-1999）が1955年に発表した英語短編集。第二次大戦下のビルマ社会を舞台に英国植民地・日本占領期の生活を描き、20世紀ビルマ女性英語文学の代表作となった。",
    background="独立期ビルマの英語知識人女性による戦争・社会観察文学と、英語による国際的読者層への接近。",
    development="20世紀ビルマ英語文学の重要先駆として、現代ミャンマー英語文学の系譜的源流に位置づけられた。",
    historical_context="独立期ビルマ（1948-）の英語文化と国民形成期。",
    primary_source_url=WIKI_EN+"Khin_Myo_Chit",
    primary_source_type="Wikipedia: Khin Myo Chit",
    importance_score=2, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アウティン・ブニャヴォン",
    name_en="Outhine Bounyavong",
    name_original="Outhine Bounyavong",
    period_key="カンボジア・ラオス古典期",
    definition="アウティン・ブニャヴォン（1942-2000）はラオスを代表する現代作家。短編集『ラオスの郷土を求めて Mother's Beloved』(1999)が代表作で、社会主義ラオスの日常生活を簡潔な散文で描いた、20世紀ラオス文学の頂点を成す。",
    background="1975年ラオス革命以降の社会主義文学体制と、限定的検閲下での作家活動。",
    development="2000年代以降の英訳普及で、東南アジア比較文学研究の重要対象となり、現代ラオス文学の国際的代表作家として再評価された。",
    historical_context="社会主義ラオス（1975-）の文学制度形成期。",
    primary_source_url=WIKI_EN+"Outhine_Bounyavong",
    primary_source_type="Wikipedia: Outhine Bounyavong",
    importance_score=2, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"社会主義文学制度と検閲",
         "description":"ラオス社会主義文学は人類学的国家文化政策研究の対象。"}])


# ============================================================
# Cross-domain reinforcement (additional cross_domain links)
# ============================================================
# Add cross_domain entries to several existing concepts to satisfy >=12 cross_domain.
def _enrich_cross_domain():
    """Append cross_domain to selected concepts to reach >=12."""
    targets = {
        "一然『三国遺事』": [],  # already has one
        "李退渓『退渓全集』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"性理学と東アジア儒教ネットワーク",
             "description":"退渓学は朝鮮・日本・中国にまたがる東アジア儒教知識ネットワークの中核。"}],
        "丁若鏞『牧民心書』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"地方統治と政治人類学",
             "description":"『牧民心書』は地方統治の人類学的記述として政治人類学・行政人類学の対象。"}],
        "金素月『つつじの花』": [
            {"target_db":"MY","link_type":"shared_concept",
             "target_entity_name":"民謡的抒情詩と集合的感情",
             "description":"金素月の民謡調抒情は朝鮮民族の集合的感情ナラティブの中核。"}],
        "韓江『すべての、白いものたちの』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"喪と悲嘆の文化人類学",
             "description":"韓江『白い』の喪の散文詩は文化人類学的悲嘆研究と共振。"}],
        "黄晳暎『張吉山』": [
            {"target_db":"MY","link_type":"shared_concept",
             "target_entity_name":"民衆英雄と義賊神話",
             "description":"張吉山は東アジア義賊神話（水滸伝・洪吉童）の系譜上にあるトリックスター英雄。"}],
        "南高『チ・フェオ』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"ベトナム農村構造と排除の人類学",
             "description":"チ・フェオは植民地農村における社会的排除メカニズムの人類学的事例。"}],
        "プラムディヤ『人間の大地』（ブル四部作I）": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"植民地ジャワ社会と混血人類学",
             "description":"ヌヤイ・オントソローは蘭領東インド混血社会の人類学的中心人物。"}],
        "ホセ・ガルシア・ヴィラ『来たり、ここに在り』": [
            {"target_db":"MY","link_type":"shared_concept",
             "target_entity_name":"モダニズム詩と意味解体",
             "description":"ヴィラのコンマ詩は意味の物質化を試みる東南アジア・モダニズム詩の祖型。"}],
        "F・シオニル・ホセ『ロサーレス・サーガ』第三巻『土地』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"フィリピン民衆史とイロカノ移住",
             "description":"『土地』はイロカノ系民衆史の文学的人類学的再構成。"}],
        "ファム・ティ・ホアイ": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"ベトナム亡命知識人と文化越境",
             "description":"ファム・ティ・ホアイのベルリン拠点活動はトランスナショナル知識人の人類学的事例。"}],
        "クラープ・サイプラディット『絵画の背景』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"タイ立憲革命期の文化的近代化",
             "description":"『絵画の背景』は1932年立憲革命後のタイ知識人の文化観察として人類学的価値を持つ。"}],
        "カムシン・シーノーク『政治家』": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"イサーン地方と東北タイ農村人類学",
             "description":"カムシン・シーノークの短編はイサーン民族誌的記述と密接に対応。"}],
        "オーシャン・ヴオン": [
            {"target_db":"AN","link_type":"shared_concept",
             "target_entity_name":"難民世代の言語的継承と喪失",
             "description":"オーシャン・ヴオンの作品はベトナム戦争難民第二世代の言語的喪失・継承の人類学的事例。"}],
    }
    for c in CONCEPTS:
        if c["name_ja"] in targets and targets[c["name_ja"]]:
            c.setdefault("cross_domain", []).extend(targets[c["name_ja"]])

_enrich_cross_domain()


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0

    for c in CONCEPTS:
        for k in list(c.keys()):
            if k.startswith("name_ji"):
                c.pop(k)

    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="グローバルサウス",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry.get('name_ja','?')}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth_transform tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cross_domain failed for {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[wave18-c27-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave18-c27-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
