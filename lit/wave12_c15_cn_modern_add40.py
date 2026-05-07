"""LIT-DB Phase 2 Wave 12 — C15 Chinese modern literature ADD 40.

Subfield: lit_cn_modern (id=9), region='東アジア'.
Sources: 維基文庫 Chinese Wikisource (zh.wikisource.org), CTEXT modern,
Scripta Sinica (Academia Sinica), Zhejiang University CN modern lit DB,
Project Gutenberg (PD pre-1957 translations), academic Wikipedia.

Verification policy mirrors wave9_c08_realism.py.

40 NEW concepts (no overlap with existing 40 May Fourth core):
  A: 晩清過渡期 — 8
  B: 民国期拡張（張愛玲・老舎・曹禺等補完） — 8
  C: 延安/社会主義/文革地下 — 8
  D: 改革開放後（先鋒/新写実/神実主義/SF） — 8
  E: 1990s+市場・華語圏・网络文学 — 8
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("清", "Qing dynasty", 1644, 1911,
     "清朝期。1840年アヘン戦争以降は晩清として近代化と文学変革の時期。"),
    ("国民革命〜抗戦期", "National Revolution / Anti-Japanese War",
     1927, 1949,
     "国民政府期から日中戦争・国共内戦に至る民国期文学拡張期。"),
    ("毛沢東期", "Mao era", 1949, 1976,
     "中華人民共和国成立から文化大革命終結まで。延安文芸講話路線の制度化期。"),
    ("改革開放期", "Reform-and-Opening era", 1976, 1989,
     "毛沢東後の文学解放期。傷痕・尋根・先鋒・新写実が連続出現。"),
    ("現代", "Contemporary China", 1970, 2025,
     "1990年代市場化以降の華語圏全体（大陸・台湾・香港・東南アジア華人・北米）の現代文学。"),
]


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"
WSRC_ZH = "https://zh.wikisource.org/wiki/"
CTEXT = "https://ctext.org/"
GUTEN = "https://www.gutenberg.org/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_cn_modern", region="東アジア",
         original_script="hanzi")


# ============================================================
# A: 晩清過渡期（8）
# ============================================================
add(**C, name_ja="李宝嘉『官場現形記』",
    name_en="Li Boyuan's Officialdom Unmasked",
    name_original="官場現形記",
    period_key="清",
    definition="李宝嘉（李伯元、1867-1906）が1903-05年に上海『世界繁華報』に連載した晩清譴責小説の代表作。清末官界の腐敗・賄賂・無能を60章にわたり連作短編形式で暴露した。魯迅『中国小説史略』が「譴責小説」概念を立てた際の中心作品で、五四白話小説に至る過渡期の社会批判文学の典型を成す。",
    background="義和団事件後の清末政治腐敗と、上海近代出版業の興隆。",
    development="呉趼人『二十年目睹之怪現状』、劉鶚『老残遊記』とともに晩清四大譴責小説を構成し、五四リアリズムへの橋渡しとなった。",
    historical_context="光緒新政期(1901-)の制度改革と、それに伴う官僚体制の瓦解。",
    primary_source_url=WSRC_ZH+"官場現形記",
    primary_source_type="維基文庫: 官場現形記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="劉鶚『老残遊記』",
    name_en="Liu E's The Travels of Lao Can",
    name_original="老殘遊記",
    period_key="清",
    definition="劉鶚（劉鉄雲、1857-1909）が1903-07年に発表した長編小説。江湖医「老残」の漫遊を借りて、晩清の山東地方を中心に「清官」の害を描いた。胡適が中国近代小説の傑作として高く評価し、王国維風景描写論との関連でも論じられる。譴責小説中、文学的完成度の最高峰とされる。",
    background="義和団事件後の地方官治と、洋務派知識人の社会観察。",
    development="魯迅『中国小説史略』および胡適の評価を経て、近代中国小説の正典に組み込まれた。",
    historical_context="光緒末年の山東省政治腐敗と、列強進出下の中国社会。",
    primary_source_url=WSRC_ZH+"老殘遊記",
    primary_source_type="維基文庫: 老殘遊記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"清官批判と社会記述",
         "description":"劉鶚の「清官の害」批判は、晩清官僚社会への民族誌的観察として、19世紀社会観察言説の中国的形式を成す。"}])

add(**C, name_ja="呉趼人『二十年目睹之怪現状』",
    name_en="Wu Jianren's Strange Events of the Last Twenty Years",
    name_original="二十年目睹之怪現狀",
    period_key="清",
    definition="呉趼人（呉沃尭、1866-1910）が1903-10年に『新小説』『月月小説』に連載した晩清長編小説。「九死一生」と号する語り手が20年間に目撃した社会の怪現象1080編を一人称回顧形式で展開。一人称視点の本格的導入で、晩清小説の方法的革新を達成した。",
    background="日清戦争後の社会瓦解と、梁啓超主導の「小説界革命」綱領下の新小説雑誌興隆。",
    development="一人称回顧形式は五四以降の現代中国短編小説の祖型となった。",
    historical_context="光緒末年から宣統期の社会瓦解と、梁啓超「論小説与群治之関係」(1902)以降の小説制度的興隆。",
    primary_source_url=WSRC_ZH+"二十年目睹之怪現狀",
    primary_source_type="維基文庫: 二十年目睹之怪現狀",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="曾樸『孽海花』",
    name_en="Zeng Pu's Flower in a Sea of Sin",
    name_original="孽海花",
    period_key="清",
    definition="曾樸（1872-1935）が1905-30年代まで断続的に発表した晩清歴史小説。状元洪鈞と妓女傅彩雲（賽金花）の生涯を軸に、同治・光緒期の30年間の中国知識人社会と国際情勢を描く。フランス文学に通じた曾樸の方法は、晩清譴責小説と五四歴史小説をつなぐ橋となった。",
    background="洋務運動から戊戌変法に至る知識人社会、フランス・ロマン主義文学の作者による翻訳実践。",
    development="魯迅『中国小説史略』が四大譴責小説の一とし、後の歴史小説（茅盾、姚雪垠）に影響した。",
    historical_context="同治・光緒期の中国対外関係と、上海開港後のコスモポリタン文化。",
    primary_source_url=WSRC_ZH+"孽海花",
    primary_source_type="維基文庫: 孽海花",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="梁啓超「小説界革命」",
    name_en="Liang Qichao's Revolution in the Realm of Fiction",
    name_original="小說界革命",
    period_key="清",
    definition="梁啓超（1873-1929）が1902年『新小説』創刊号「論小説与群治之関係」で提唱した文学改革綱領。「欲新一国之民、不可不先新一国之小説」と説き、小説を社会改革・国民教化の手段として位置づけた。晩清譴責小説、政治小説、五四白話小説運動の理論的源流となった。",
    background="戊戌変法挫折後の梁啓超亡命期日本における日本政治小説受容、明治啓蒙文学経由の社会改革論。",
    development="陳独秀・胡適の白話文運動、五四新文学運動の社会改革指向の直接的前提となった。",
    historical_context="戊戌政変(1898)後の改革派知識人の文学的転回と、日本明治啓蒙文学の中介。",
    primary_source_url=WSRC_ZH+"論小說與群治之關係",
    primary_source_type="維基文庫: 論小說與群治之關係",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"小説を国民教化・社会改革手段とする梁啓超の綱領は、AI生成テキストを政策的・教化的目的で大規模配備しうる現代状況の歴史的祖型として再読される。",
         "related_ai_phenomenon":"AIによる大規模社会教化テキスト配信"}])

add(**C, name_ja="林紓翻訳",
    name_en="Lin Shu's translations",
    name_original="林譯小說",
    period_key="清",
    definition="林紓（1852-1924）が1899-1924年に発表した180余編の西洋小説の文言文翻訳。デュマ『椿姫』『黒奴籲天録』『塊肉余生述（デヴィッド・コパーフィールド）』等を文言文の優美な散文で漢訳した。外国語不能の林紓が口述翻訳者と協働した独特の翻訳方法は、晩清の西洋文学受容の制度的起点となった。",
    background="戊戌変法前後の西洋知識輸入需要と、上海商務印書館の翻訳出版事業。",
    development="魯迅・周作人兄弟、郭沫若、銭鍾書ら五四世代の西洋文学受容の入口となった。",
    historical_context="光緒末年から民国初期の翻訳文学制度形成期。",
    primary_source_url=WSRC_ZH+"巴黎茶花女遺事",
    primary_source_type="維基文庫: 巴黎茶花女遺事 (林紓訳)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="晩清「新小説」雑誌",
    name_en="late-Qing 'New Fiction' magazines",
    name_original="新小說",
    period_key="清",
    definition="梁啓超『新小説』(1902-06、横浜・上海)、呉趼人主編『月月小説』(1906-08)、商務印書館『小説月報』(1910-31)等、晩清から民国初期に隆盛した小説雑誌群。原稿料制度・連載形式・翻訳並置を確立し、中国近代小説制度の物質的基盤を成した。",
    background="清末日本亡命知識人の出版活動、上海近代印刷出版業の成立、租界経済による出版自由空間の形成。",
    development="『小説月報』は1921年茅盾主編下で文学研究会機関誌に変貌し、五四リアリズムの中心媒体となった。",
    historical_context="光緒新政期(1901-)の出版制度自由化と、原稿料制度による職業作家層の形成。",
    primary_source_url=WIKI_ZH+"新小說",
    primary_source_type="維基百科: 新小說",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="晩清譴責小説",
    name_en="late-Qing exposé novel",
    name_original="譴責小說",
    period_key="清",
    definition="魯迅『中国小説史略』(1923)が立てたジャンル概念。1900-1910年代の李宝嘉・呉趼人・劉鶚・曾樸の長編小説を中核に、清末社会の腐敗・無能を暴露的に描く小説群を指す。明清世情小説と五四リアリズムをつなぐ過渡期形式として、近代中国小説史の枢要な位置を占める。",
    background="魯迅『中国小説史略』のジャンル整理と、五四以降の晩清文学再評価。",
    development="後の社会派長編（茅盾『子夜』、呉趼人系の都市小説）の祖型となった。",
    historical_context="義和団事件後の清末政治社会の瓦解と、それを文学化する制度的需要。",
    primary_source_url=WSRC_ZH+"中國小說史略",
    primary_source_type="維基文庫: 中國小說史略 (魯迅)",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 民国期拡張（8）
# ============================================================
add(**C, name_ja="巴金『激流三部曲』",
    name_en="Ba Jin's Turbulent Stream Trilogy",
    name_original="激流三部曲",
    period_key="国民革命〜抗戦期",
    definition="巴金（1904-2005）の長編三部作『家』(1933)、『春』(1938)、『秋』(1940)。四川成都の旧家「高家」三世代の解体を、新青年世代の自由・恋愛・革命への離脱を軸に描く。五四個人解放思想の長編形式での結晶として、民国期最広範な読者層を獲得し、中国家族小説の規範を確立した。",
    background="作者の四川大家族での体験、五四個人主義思想の長編化。",
    development="社会主義リアリズム成立後も民国期家族小説の規範として読み継がれ、文革後の作者『随想録』(1978-86)再評価で再び注目された。",
    historical_context="1920-30年代中国の旧家族制度解体と、新青年世代の社会的自立。",
    primary_source_url=WIKI_ZH+"激流三部曲",
    primary_source_type="維基百科: 激流三部曲",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"巴金の旧家解体物語は、家族集団主義から個人主体への移行を物語化する五四思想の典型。AI時代における主体形成・個人化議論の歴史的参照点として再読される。",
         "related_ai_phenomenon":"AI時代の個人主体形成と集団的アイデンティティの再編"}])

add(**C, name_ja="老舎『駱駝祥子』",
    name_en="Lao She's Camel Xiangzi (Rickshaw Boy)",
    name_original="駱駝祥子",
    period_key="国民革命〜抗戦期",
    definition="老舎（舒慶春、1899-1966）が1936-37年に『宇宙風』に連載した長編小説。北京の人力車夫祥子の三度の挫折と精神的崩壊を、北京口語と社会観察を統合して描いた。1945年の英訳『Rickshaw Boy』が米国ベストセラーとなり、中国近代文学の世界的代表作として位置づけられた。",
    background="老舎の北京下層社会観察と、ロンドン留学期に得たディケンズ的都市リアリズム手法。",
    development="老舎『四世同堂』(1944-50)、戦後の都市下層リアリズムに継承された。",
    historical_context="日中戦争前夜の北京社会と、軍閥支配下の都市下層民の生活。",
    primary_source_url=WIKI_ZH+"駱駝祥子",
    primary_source_type="維基百科: 駱駝祥子",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"老舎の北京口語文学は地域口語を文学言語に転化する方法論で、AI時代の方言・少数言語のテキスト生成における言語多様性問題の歴史的祖型。",
         "related_ai_phenomenon":"AIによる方言・地域口語生成と言語多様性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"都市下層の民族誌",
         "description":"老舎の人力車夫描写は北京下層民族誌として、20世紀中国都市人類学の文学的並行物を成す。"}])

add(**C, name_ja="老舎『茶館』",
    name_en="Lao She's Teahouse",
    name_original="茶館",
    period_key="毛沢東期",
    definition="老舎が1957年に発表した三幕劇。北京の茶館「裕泰」を舞台に、戊戌変法（1898）・軍閥期（1918）・国共内戦末期（1948）の50年間の北京社会の変遷を、70余の人物を通じて凝縮した。中国近代演劇の頂点と評され、北京人民芸術劇院の代表的レパートリーとなった。",
    background="老舎の北京口語感覚と、社会主義新中国における歴史回顧的劇作の制度的需要。",
    development="文革期に老舎が迫害自殺した後も、1979年再演を機に正典化された。20世紀中国演劇の代表作として国外にも翻訳上演された。",
    historical_context="百花斉放期(1956-57)の創作自由と、その直後の反右派闘争(1957)の歴史的緊張。",
    primary_source_url=WIKI_ZH+"茶館",
    primary_source_type="維基百科: 茶館",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"群像劇と凝縮構造",
         "description":"老舎『茶館』の50年圧縮三幕構造は、19世紀リアリズム劇の凝縮形式と並ぶ群像劇詩学の中心事例。"}])

add(**C, name_ja="曹禺『雷雨』",
    name_en="Cao Yu's Thunderstorm",
    name_original="雷雨",
    period_key="国民革命〜抗戦期",
    definition="曹禺（萬家寶、1910-1996）が1934年に発表した四幕劇。鉱山主周家を舞台に、近親相姦・労資対立・運命悲劇を24時間に圧縮した古典悲劇構造で展開。中国近代話劇の制度的成立を象徴する作品で、イプセン・ギリシャ悲劇・チェーホフを中国化した規範作品となった。",
    background="清華大学西洋文学科で受けたイプセン・ギリシャ悲劇・オニール教育、1930年代上海話劇運動の興隆。",
    development="『日出』(1936)、『原野』(1937)、『北京人』(1941)とともに中国近代演劇の正典を構成した。",
    historical_context="1930年代南京政府期の都市資本主義拡大と、左翼文化運動下の社会派演劇隆盛。",
    primary_source_url=WIKI_ZH+"雷雨_(話劇)",
    primary_source_type="維基百科: 雷雨 (話劇)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="曹禺『日出』",
    name_en="Cao Yu's Sunrise",
    name_original="日出",
    period_key="国民革命〜抗戦期",
    definition="曹禺が1936年に発表した四幕劇。1930年代天津の高級ホテルを舞台に、社交婦・銀行家・小市民・娼婦らが交差する「横断面」構造で資本主義都市の腐敗を描く。『雷雨』の閉鎖空間悲劇から、より社会的横断面のリアリズムへ移行した代表作。",
    background="天津・上海の租界都市資本主義観察、1930年代左翼文化運動の社会観察思想。",
    development="戦後社会主義リアリズム劇への橋渡しとなり、改革開放後にも繰り返し上演された。",
    historical_context="1930年代中国都市資本主義の急速な発展と、それに伴う社会問題の文学化。",
    primary_source_url=WIKI_ZH+"日出_(劇本)",
    primary_source_type="維基百科: 日出 (話劇)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="張愛玲『傾城之恋』",
    name_en="Eileen Chang's Love in a Fallen City",
    name_original="傾城之戀",
    period_key="国民革命〜抗戦期",
    definition="張愛玲（1920-1995）が1943年に発表した中編小説。上海の没落上層家族の白流蘇と、香港帰りの華僑富豪范柳原の恋愛を、香港陥落（1941年12月）の戦時を背景に描く。古典的「才子佳人」物語と西洋心理小説を融合した方法は、海派文学の頂点として戦後再発見された。",
    background="作者の上海貴族家系出身と没落体験、英国植民地香港大学での西洋文学修養。",
    development="夏志清『中国現代小説史』(1961)による再評価以降、台湾・香港・大陸の張愛玲現象を生み、現代華語文学の中心作家として正典化された。",
    historical_context="1941年12月日本軍香港占領と、上海・香港間の華人エリート移動の歴史。",
    primary_source_url=WIKI_ZH+"傾城之戀",
    primary_source_type="維基百科: 傾城之戀",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"張愛玲は古典「才子佳人」物語と西洋心理小説の融合を達成した。AI時代における異文化テキスト融合・スタイル転移生成の歴史的祖型として再読される。",
         "related_ai_phenomenon":"AIによる異文化スタイル融合・転移生成"}])

add(**C, name_ja="張愛玲『金鎖記』",
    name_en="Eileen Chang's The Golden Cangue",
    name_original="金鎖記",
    period_key="国民革命〜抗戦期",
    definition="張愛玲が1943年に発表した中編小説。麻油屋出身の女性曹七巧が大家族姜家に嫁ぎ、金銭欲と性的抑圧によって精神的怪物に変貌する30年を描く。夏志清が「中国近代文学最高傑作」と評価し、フロイト・ユング深層心理小説と中国家族小説を融合した張愛玲文学の方法的頂点とされる。",
    background="作者の家族体験、上海租界文化の心理的退廃観察。",
    development="夏志清評価以降、中国心理小説の規範として正典化され、英語圏中国研究の中心テクストとなった。",
    historical_context="1940年代占領下上海の海派文学興隆、租界文化終焉期の精神的退廃。",
    primary_source_url=WIKI_ZH+"金鎖記",
    primary_source_type="維基百科: 金鎖記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"心理小説と物語論",
         "description":"張愛玲の心理小説は中国近代文学における自由間接話法と心理リアリズムの代表的応用例として、ナラトロジー研究の対象となる。"}])

add(**C, name_ja="銭鍾書『囲城』",
    name_en="Qian Zhongshu's Fortress Besieged",
    name_original="圍城",
    period_key="国民革命〜抗戦期",
    definition="銭鍾書（1910-1998）が1947年に発表した長編小説。フランス留学帰りの方鴻漸が婚姻と職業生活で連続的に挫折する姿を、博覧的諷刺と西洋古典引用を駆使した独自の文体で描く。中国近代諷刺小説の頂点として、夏志清『中国現代小説史』が高く評価し、改革開放後の再発見を経て正典化された。",
    background="作者のオックスフォード・パリ留学体験、博覧家としての東西文学知識。",
    development="改革開放後の1980年代に再評価され、TVドラマ化(1990)で全国的人気を獲得した。",
    historical_context="抗戦末期から国共内戦初期の中国知識人社会と、海外帰国知識人の社会的位置の不安定。",
    primary_source_url=WIKI_ZH+"圍城",
    primary_source_type="維基百科: 圍城",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"諷刺小説の詩学",
         "description":"銭鍾書『囲城』の博覧的諷刺は20世紀中国諷刺小説の頂点で、英国18世紀諷刺伝統と並ぶ詩学的事例。"}])


# ============================================================
# C: 延安・社会主義・文革地下（8）
# ============================================================
add(**C, name_ja="趙樹理「山薬蛋派」",
    name_en="Zhao Shuli and the 'Potato School'",
    name_original="山藥蛋派",
    period_key="毛沢東期",
    definition="趙樹理（1906-1970）と山西省作家群（馬烽、西戎、束為、孫謙、胡正）が形成した、延安文芸講話路線下の農民文学流派。山西方言・民間文芸（説書・板話）・農村題材を統合し、毛沢東「工農兵文芸」の最も成功した実践とされた。趙樹理『小二黒結婚』(1943)、『李有才板話』(1943)が代表作。",
    background="毛沢東「延安文芸座談会講話」(1942)の制度的展開と、山西解放区における農民読者層の形成。",
    development="文革期に趙樹理は迫害死したが、改革開放後に再評価され、社会主義リアリズムの民衆性側面の代表として位置づけ直された。",
    historical_context="抗日戦争期の解放区文化政策と、農民読者層を視野に入れた文学制度の形成。",
    primary_source_url=WIKI_ZH+"山藥蛋派",
    primary_source_type="維基百科: 山藥蛋派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="周立波『暴風驟雨』",
    name_en="Zhou Libo's The Hurricane",
    name_original="暴風驟雨",
    period_key="毛沢東期",
    definition="周立波（1908-1979）が1948-49年に発表した長編小説。1946-47年の東北土地改革を、東北元宝鎮の村民・工作隊員の視点から描く。社会主義リアリズム中国版の最初期代表作で、丁玲『太陽は桑乾河を照らす』(1948)と並び、1951年スターリン文学賞を受賞した。",
    background="作者の東北土地改革参加体験、ソ連社会主義リアリズム理論の延安での受容。",
    development="1950年代の社会主義リアリズム長編小説（柳青『創業史』、梁斌『紅旗譜』等）の祖型となった。",
    historical_context="1946-49年の中国共産党土地改革政策と、それを文学化する制度的需要。",
    primary_source_url=WIKI_ZH+"暴風驟雨",
    primary_source_type="維基百科: 暴風驟雨",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="孫犁「荷花淀派」",
    name_en="Sun Li and the 'Lotus Lake School'",
    name_original="荷花淀派",
    period_key="毛沢東期",
    definition="孫犁（1913-2002）と河北白洋淀地域作家群（劉紹棠、従維熙、韓映山）が形成した、抒情的リアリズムの流派。代表作『荷花淀』(1945)に象徴されるように、戦争・革命題材を抒情的・詩的に描く。山薬蛋派の素朴農民写実と対照的な、社会主義リアリズム内部の抒情的潮流を代表する。",
    background="作者の冀中根拠地体験と、五四以降の抒情的散文伝統の社会主義文学への継承。",
    development="改革開放後に孫犁は「老作家」として再評価され、汪曾祺ら1980年代抒情派作家の精神的源流となった。",
    historical_context="抗日戦争期の冀中解放区文化と、戦後社会主義文学制度の多様性。",
    primary_source_url=WIKI_ZH+"荷花淀派",
    primary_source_type="維基百科: 荷花淀派",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="革命様板戯",
    name_en="revolutionary model operas",
    name_original="革命樣板戲",
    period_key="毛沢東期",
    definition="文化大革命期(1966-76)に江青を中心に制定された8本（後に増補）の革命題材様板劇。京劇『紅灯記』『智取威虎山』『沙家浜』『海港』『奇襲白虎団』、芭蕾劇『紅色娘子軍』『白毛女』、交響曲『沙家浜』。文革10年間中国全土で唯一の上演舞台芸術となり、毛沢東文芸路線の制度的頂点を成した。",
    background="江青の文芸介入(1962-)、社会主義リアリズム中国化の極限的展開。",
    development="文革後に「文化的暴政」として批判されたが、2000年代以降、メディア研究・文化史研究で再検討対象となった。",
    historical_context="文化大革命期の「破四旧」運動と、伝統演劇・五四新劇・西洋劇の全面禁止。",
    primary_source_url=WIKI_ZH+"樣板戲",
    primary_source_type="維基百科: 樣板戲",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"流通","status":"rethinking",
         "rationale":"様板戯は文革10年間中国全土で唯一の上演舞台芸術となった。AI時代における単一テンプレートの大規模配信・コンテンツ独占状況を考察する歴史的参照点。",
         "related_ai_phenomenon":"AI生成コンテンツの単一モデル独占とテンプレート均質化"}])

add(**C, name_ja="文革地下文学",
    name_en="Cultural Revolution underground literature",
    name_original="文革地下文學",
    period_key="毛沢東期",
    definition="文革期(1966-76)に公式出版回路の外で書かれ、手抄本（手写し）形式で流通した文学作品群。趙振開（北島）の「告訴你、当我懂得了人類！」、靳凡『公開的情書』、張揚『第二次握手』、礼平『晩霞消失的時候』が代表的。文革後に発表され、朦朧詩・傷痕文学の地下源流として位置づけられる。",
    background="文革期の公式文学制度の崩壊と、知識青年下放下での秘密読書サークル形成。",
    development="改革開放後に発表され、1970年代末-80年代の朦朧詩・傷痕文学・反思文学の精神的源流となった。",
    historical_context="文革「黄皮書」「灰皮書」（内部参考読物）の流通と、知識青年世代の自発的読書共同体形成。",
    primary_source_url=WIKI_ZH+"地下文學",
    primary_source_type="維基百科: 地下文學",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"流通","status":"rethinking",
         "rationale":"手抄本流通は公式回路を迂回した文学伝達の歴史的事例であり、AI時代における分散型コンテンツ流通・脱プラットフォーム文学の祖型として再読される。",
         "related_ai_phenomenon":"分散型・脱プラットフォーム的AI生成テキスト流通"}])

add(**C, name_ja="黄皮書・灰皮書",
    name_en="Yellow Books / Grey Books (Cultural Revolution era)",
    name_original="黃皮書／灰皮書",
    period_key="毛沢東期",
    definition="1960-70年代に「内部参考」として限定発行された外国文学・社会科学翻訳書。文学系（黄皮書）はサルトル『嘔吐』、サリンジャー『ライ麦畑でつかまえて』、ケルアック『路上』等。社会科学系（灰皮書）はトロツキー、ベルジャエフ等。文革期知識青年の地下読書サークルの中核教材となり、朦朧詩・先鋒文学の精神的養分となった。",
    background="中ソ対立下の「修正主義批判」目的の翻訳事業が、結果として外国現代思想を中国に密輸する経路となった。",
    development="改革開放後の翻訳文学興隆、北島・芒克ら朦朧詩人、馬原・余華ら先鋒作家の精神形成に決定的影響を与えた。",
    historical_context="1960年代中ソ対立期の党内部批判教材としての翻訳事業の制度的逆機能。",
    primary_source_url=WIKI_ZH+"黃皮書",
    primary_source_type="維基百科: 黃皮書",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="食指（郭路生）",
    name_en="Shi Zhi (Guo Lusheng)",
    name_original="食指（郭路生）",
    period_key="毛沢東期",
    definition="食指（郭路生、1948-）は文革期地下詩の代表的詩人。1968年「相信未来」「这是四点零八分的北京」が知識青年下放世代の間で手抄本流通し、後の朦朧詩運動の最初の歴史的接点となった。北島は食指を「朦朧詩の父」と呼んだ。1970年代に精神疾患を発症し、文革終結後の1990年代に再発見・正典化された。",
    background="文革期北京知識青年（クッキー世代）の地下文化、ソ連翻訳詩・西洋現代詩の手抄本受容。",
    development="北島・芒克・舒婷ら朦朧詩人の精神的源流として、1990年代以降に正典化された。",
    historical_context="1968年「上山下郷運動」開始期の知識青年下放と、その精神的衝撃の文学化。",
    primary_source_url=WIKI_ZH+"食指_(詩人)",
    primary_source_type="維基百科: 食指",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="白洋淀詩群",
    name_en="Baiyangdian poetry group",
    name_original="白洋淀詩群",
    period_key="毛沢東期",
    definition="文革期(1969-76)に河北省白洋淀地域に下放された北京知識青年（芒克、根子、多多、林莽等）が形成した地下詩人サークル。手抄本・口承で詩を交換し、朦朧詩の歴史的前段階を成した。1978年北京で芒克・北島が雑誌『今天』を創刊し、白洋淀詩群と朦朧詩の正式接続が成立した。",
    background="1969年北京知識青年の白洋淀下放、黄皮書・灰皮書の地下流通。",
    development="1978年『今天』創刊以降、朦朧詩運動の母体となり、現代中国詩の精神的源流として位置づけられた。",
    historical_context="1968-76年「上山下郷運動」下の知識青年世代の文化的潜流。",
    primary_source_url=WIKI_ZH+"白洋淀詩群",
    primary_source_type="維基百科: 白洋淀詩群",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: 改革開放後（先鋒・新写実・神実主義・SF）（8）
# ============================================================
add(**C, name_ja="馬原「叙述の罠」",
    name_en="Ma Yuan's narrative traps",
    name_original="敘述的圈套",
    period_key="改革開放期",
    definition="馬原（1953-）が1984-87年の中短編『岡底斯的誘惑』『虚構』『拉薩河女神』等で展開した中国先鋒小説の方法論的核。チベット題材を素材に、語り手・物語・読者の三者関係を意図的に解体し、「私（馬原）」を物語に登場させてリアリズム約束を破壊する。中国先鋒小説の出発点となり、後の余華・格非・蘇童に影響した。",
    background="作者のチベット8年間勤務体験、ボルヘス・ロブ=グリエ・カルヴィーノ等の翻訳受容。",
    development="格非『迷舟』、余華『現実一種』、蘇童『妻妾成群』ら1980年代後半先鋒小説の方法的祖型となった。",
    historical_context="1980年代中国の翻訳文学全盛期と、改革開放下の創作自由の急速な拡大。",
    primary_source_url=WIKI_ZH+"馬原_(作家)",
    primary_source_type="維基百科: 馬原 (作家)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="格非『褐色鳥群』",
    name_en="Ge Fei's Brown Birds",
    name_original="褐色鳥群",
    period_key="改革開放期",
    definition="格非（劉勇、1964-）が1988年に発表した中篇小説。記憶・夢・現実の境界の曖昧化、循環的時間構造、メタフィクション的語り手介入を駆使し、ボルヘス的迷宮構造を中国語小説に持ち込んだ。中国先鋒小説の方法的精緻化を象徴する作品で、清華大学教授としての格非の理論的基盤ともなった。",
    background="作者のボルヘス・カルヴィーノ熱中、馬原以降の中国先鋒小説実験。",
    development="2000年代以降、格非『江南三部曲』(2004-11)で歴史リアリズムへの転回を見せ、第9回茅盾文学賞(2015)を受賞した。",
    historical_context="1980年代後半中国文学の翻訳全盛期と、若年世代作家の方法的実験。",
    primary_source_url=WIKI_ZH+"格非",
    primary_source_type="維基百科: 格非",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="蘇童『妻妾成群』",
    name_en="Su Tong's Wives and Concubines",
    name_original="妻妾成群",
    period_key="改革開放期",
    definition="蘇童（童中貴、1963-）が1989年に発表した中篇小説。1920年代江南の旧家陳家に四夫人として入る頌蓮の堕落と狂気を、抒情的散文と象徴主義的構造で描く。1991年張芸謀監督が『紅夢』として映画化し、ヴェネツィア国際映画祭銀獅子賞・米アカデミー外国語映画賞ノミネートを獲得し、中国文学の世界的可視化を象徴する作品となった。",
    background="作者の江南文化的記憶、先鋒小説の歴史題材への転回。",
    development="蘇童『罌粟之家』『紅粉』『我的帝王生涯』等の歴史小説連作を派生し、現代中国文学の歴史想像力の代表作家となった。",
    historical_context="1989年前後の中国文化的・政治的転換期と、文学の歴史題材への退避。",
    primary_source_url=WIKI_ZH+"妻妾成群",
    primary_source_type="維基百科: 妻妾成群",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="余華『活着』",
    name_en="Yu Hua's To Live",
    name_original="活著",
    period_key="改革開放期",
    definition="余華（1960-）が1992-93年に発表した長編小説。地主の息子・福貴が国共内戦・大躍進・文革・改革開放を生き抜き、家族7人を全て失っていく姿を、一人称回顧形式で淡々と描く。1994年張芸謀映画化（カンヌ審査員大賞）。先鋒小説出身の余華が「ゼロ度の語り」へ転回した代表作で、現代中国文学の世界的代表作の一つ。",
    background="作者の浙江海塩農村医療体験、先鋒文学から人間史詩への方法的転回。",
    development="余華『許三観売血記』(1995)、『兄弟』(2005-06)、『第七天』(2013)に至る系列の出発点となった。",
    historical_context="1990年代初頭中国の市場化転換と、20世紀中国農村史の文学的総括の需要。",
    primary_source_url=WIKI_ZH+"活著",
    primary_source_type="維基百科: 活著",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"余華『活著』の「ゼロ度の語り」は、感情的判断を排した一人称語りで、AI生成テキストの感情的中立性主張と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における感情的中立的語りの構造"}])

add(**C, name_ja="新写実主義",
    name_en="neo-realism (Chinese)",
    name_original="新寫實主義",
    period_key="改革開放期",
    definition="1987年雑誌『鍾山』が提唱した中国小説流派。劉震雲『一地鶏毛』、池莉『煩悩人生』、方方『風景』、劉恒『伏羲伏羲』を代表作家とする。先鋒文学の言語実験と社会主義リアリズムの理念性をともに退け、都市・農村の日常生活の零度の写実を志向した。改革開放期中国文学の方法的多様化を象徴する潮流。",
    background="改革開放下の都市生活変容、先鋒文学疲労、市場化以前の知識人写実需要。",
    development="1990年代中国都市小説、王安憶『長恨歌』、衛慧『上海宝貝』ら都市派の祖型となった。",
    historical_context="1980年代末中国の都市化加速と、知識人の生活感覚の市民化。",
    primary_source_url=WIKI_ZH+"新寫實主義",
    primary_source_type="維基百科: 新寫實主義",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="閻連科「神実主義」",
    name_en="Yan Lianke's mythorealism",
    name_original="神實主義",
    period_key="現代",
    definition="閻連科（1958-）が『発現小説』(2011)で提唱した小説論。表層的事実描写を超えて、現実の隠された「神性的真実」「内在的真実」を寓話的・神話的方法で開示する文学方法を指す。代表作『日光流年』(1998)、『受活』(2004)、『四書』(2010)、『日熄』(2015)で実践された。閻連科は2014年フランツ・カフカ賞を中国人初受賞。",
    background="河南省農村体験、ガルシア・マルケス・カフカ・ルカーチの方法的吸収、中国大躍進・文革の歴史記憶。",
    development="2010年代中国大陸文学の最前衛として、フランツ・カフカ賞・国際ブッカー賞ノミネート等で世界文学的承認を獲得した。",
    historical_context="2010年代中国の検閲強化期における、寓話的・神話的方法による批判文学の戦略。",
    primary_source_url=WIKI_ZH+"閻連科",
    primary_source_type="維基百科: 閻連科",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"神実主義は表層的事実を超えた「内在的真実」を寓話で開示する方法論で、AI生成が増殖させる表層的「事実っぽさ」と対照的な、深層的真正性概念の現代的提唱として再読される。",
         "related_ai_phenomenon":"AI生成の表層的事実性 vs 深層的真正性"}])

add(**C, name_ja="劉慈欣『三体』",
    name_en="Liu Cixin's The Three-Body Problem",
    name_original="三體",
    period_key="現代",
    definition="劉慈欣（1963-）が2006-10年に発表した長編SF三部作『三体』『黒暗森林』『死神永生』。文革を起点に銀河規模の文明衝突を描き、中国SFの世界文学的地位を決定的に確立した。2015年第73回ヒューゴー賞長編部門受賞は中国人およびアジア人初。バラク・オバマ等が公的に推奨し、中国大衆文学の世界的影響力を象徴する作品。",
    background="作者の山西省娘子関発電所工程師としての科学的背景、アシモフ・クラーク等英米黄金期SFの吸収。",
    development="ネットフリックス映像化(2024)、中国国内外での中国SF（チェン・チウファン、ハオ・ジンファン）の興隆を主導した。",
    historical_context="2010年代中国の科学技術台頭と、それに伴う中国SFの世界文学的可視化。",
    primary_source_url=WIKI_ZH+"三體",
    primary_source_type="維基百科: 三體",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"宇宙観","status":"rethinking",
         "rationale":"『三体』の「黒暗森林」宇宙観・宇宙社会学は、AI時代の知性間競争・存在論的脅威モデルとして広く参照され、AGIリスク論議の文学的祖型として機能している。",
         "related_ai_phenomenon":"AGI存在論的脅威・知性間競争モデル"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AGIリスク・宇宙社会学",
         "description":"『三体』黒暗森林理論はAGIリスク論議・スーパーインテリジェンス論の文学的参照点として機能している。"}])

add(**C, name_ja="王朔「痞子文学」",
    name_en="Wang Shuo's hooligan literature",
    name_original="王朔／痞子文學",
    period_key="改革開放期",
    definition="王朔（1958-）が1980年代後半-90年代に確立した北京口語の都市青年小説。『頑主』(1987)、『一半是火焔、一半是海水』(1986)、『動物凶猛』(1991)で、北京下層青年・遊民・元知識青年の口語を文学化し、社会主義知識人エリート文学に対する反逆を象徴した。「痞子（チンピラ）文学」と呼ばれた。",
    background="作者の北京軍人家庭出身、1980年代北京下層青年文化、改革開放期都市青年の社会的位置の変化。",
    development="1990年代の馮小剛映画、王朔的都市口語は中国大衆文学の規範形式となり、後の都市青年小説（韓寒、郭敬明）の祖型となった。",
    historical_context="1980年代後半中国都市青年世代の社会的位置の流動化と、口語的反エリート文学の制度的需要。",
    primary_source_url=WIKI_ZH+"王朔",
    primary_source_type="維基百科: 王朔",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: 1990s+ 市場・華語圏・网络文学（8）
# ============================================================
add(**C, name_ja="王安憶『長恨歌』",
    name_en="Wang Anyi's The Song of Everlasting Sorrow",
    name_original="長恨歌",
    period_key="現代",
    definition="王安憶（1954-）が1995年に発表した長編小説。1940年代上海「上海小姐」の王琦瑶の半生を、上海弄堂（路地）の物質文化と精緻な日常描写を通じて描く。第5回茅盾文学賞受賞(2000)。張愛玲海派伝統の現代的継承として、1990年代上海ノスタルジア文学の頂点を成し、現代中国都市小説の正典となった。",
    background="作者の上海生育・知識青年下放体験、1990年代上海の急速な都市再開発と歴史的上海への文学的回帰。",
    development="2005年映画化（関錦鵬監督）、TVドラマ化、米国Penguin Classics翻訳出版(2008)で世界的可視化を獲得した。",
    historical_context="1990年代上海浦東開発・都市再開発と、それに伴う旧上海の歴史的喪失感。",
    primary_source_url=WIKI_ZH+"長恨歌_(小說)",
    primary_source_type="維基百科: 長恨歌 (小說)",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="厳歌苓",
    name_en="Yan Geling",
    name_original="嚴歌苓",
    period_key="現代",
    definition="厳歌苓（1958-）は北米華人代表的女性作家。文革期文工団体験を経て1989年渡米、コロンビア大学MFA。『扶桑』(1996)、『陸犯焉識』(2011、張芸謀映画化『帰来』)、『金陵十三釵』(2007、張芸謀映画化)、『芳華』(2017、馮小剛映画化)で、海外華人視点と中国現代史を融合した方法を確立し、中国大陸・北米・台湾を横断する華語圏文学の代表作家となった。",
    background="作者の文工団体験、コロンビア大学創作教育、北米華人女性作家としての位置。",
    development="2000年代以降、中国大陸映画化の最大の原作供給源となり、華語圏文学の世界的可視化を牽引した。",
    historical_context="1990年代以降の華人作家の越境的活動と、中国大陸映画産業の文学原作需要。",
    primary_source_url=WIKI_ZH+"嚴歌苓",
    primary_source_type="維基百科: 嚴歌苓",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="白先勇『臺北人』",
    name_en="Bai Xianyong's Taipei People",
    name_original="臺北人",
    period_key="現代",
    definition="白先勇（1937-）が1965-71年に『現代文学』『文学季刊』に発表した短編小説連作（1971年単行本化）。1949年大陸から台北に移住した「外省人」の戦後の没落・郷愁・喪失を、張愛玲海派伝統と現代主義技法を融合して描く。中国現代文学百年百強の上位作品で、台湾文学・華語圏文学の正典となった。",
    background="作者の桂系将軍白崇禧の子としての出自、アイオワ大学創作講座（聂華苓主催）での修養、1960年代台湾現代主義文学運動。",
    development="台湾現代主義文学から1980年代以降の華語圏文学全体への影響、英訳・複数言語翻訳で世界文学化された。",
    historical_context="1949年国民党敗退後の台湾外省人社会の集団的喪失と、それを文学化する世代的需要。",
    primary_source_url=WIKI_ZH+"臺北人",
    primary_source_type="維基百科: 臺北人",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="西西",
    name_en="Xi Xi",
    name_original="西西",
    period_key="現代",
    definition="西西（張彦、1937-2022）は香港代表的女性作家。代表作『我城』(1975)、『候鳥』(1991)、『飛氈』(1996)、『哀悼乳房』(1992、自身の乳癌体験を文学化)。香港都市感性と実験的形式（メタフィクション・コラージュ・グラフィック）を融合し、香港文学のアイデンティティ確立に決定的役割を果たした。2019年スウェーデン・チカダ賞受賞。",
    background="香港教育科学校卒、1970年代以降の香港文学雑誌『大拇指』『素葉文学』活動。",
    development="2000年代以降、香港文学の世界的代表として台湾・大陸・北米華語圏で再評価され、英訳出版を経て世界文学に組み込まれた。",
    historical_context="1970年代以降の香港文学アイデンティティ形成期と、英国植民地末期の都市文学興隆。",
    primary_source_url=WIKI_ZH+"西西_(作家)",
    primary_source_type="維基百科: 西西 (作家)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="馬華文学",
    name_en="Mahua literature (Malaysian Chinese)",
    name_original="馬華文學",
    period_key="現代",
    definition="マレーシア華人による華語文学。1920-30年代の南洋華人移民文学を起源に、独立後（1957）の馬華文学独立論、1990年代以降の張貴興『群象』『猴杯』、黄錦樹『雨』、李永平『大河尽頭』等の世界的代表作家輩出により、華語圏文学の重要な拠点となった。台湾出版・大陸受容を通じて華語圏文学の地理的拡張を象徴する。",
    background="20世紀初頭以降の南洋華人移民、マレーシア独立後の華人文化政治的位置の問題化。",
    development="2000年代以降、王徳威『華夷風起』(2015)等の華語語系（Sinophone）理論の台頭とともに、馬華文学は華語圏文学の中心的事例として理論化された。",
    historical_context="マレーシア独立後の華人文化政策の制限と、台湾出版を経由した文学的活動の維持。",
    primary_source_url=WIKI_ZH+"馬華文學",
    primary_source_type="維基百科: 馬華文學",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ディアスポラ華人と華語圏",
         "description":"馬華文学は華人ディアスポラと華語圏（Sinophone）の文学的事例として、人類学的ディアスポラ研究と接続する。"}])

add(**C, name_ja="网络文学",
    name_en="Chinese internet literature",
    name_original="網絡文學",
    period_key="現代",
    definition="1998年「榕樹下」サイト創設以降、中国インターネット上で発展した連載小説形式。起点中文網（2002創設）、晋江文学城（2003、女性向け）、紅袖添香等のプラットフォームを基盤に、有料連載・打賞（投げ銭）モデルが確立。2020年代には登録作家数1000万人超、読者数4億人超に達し、世界最大規模のネット文学市場となった。",
    background="1990年代末中国インターネット普及、創世中文網以降の有料連載モデル、印刷出版審査回避ニッチ。",
    development="玄幻・仙侠・都市・歴史・科幻・耽美など多ジャンルが派生し、影視化（ドラマ・映画化）を通じて中国大衆文化全体の中核コンテンツ供給源となった。",
    historical_context="2000年代以降の中国デジタル経済急成長と、伝統出版業審査体制を迂回する文学経済の成立。",
    primary_source_url=WIKI_ZH+"網絡文學",
    primary_source_type="維基百科: 網絡文學",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"流通","status":"rethinking",
         "rationale":"中国网络文学はAI時代以前から大規模・連載・有料・読者反応反映型のテキスト経済を確立した。AI生成テキストの大規模配信モデルの直接的祖型。",
         "related_ai_phenomenon":"AI生成テキストの大規模・有料・連載配信モデル"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"日々数千字を1000万人作家が量産する网络文学経済は、AIによるテキスト大量生成時代の到来以前から「人間版量産」を実現しており、AI生成と人間生成の境界の曖昧化を考察する歴史的参照点。",
         "related_ai_phenomenon":"人間量産文学とAI量産文学の境界"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"大規模生成テキスト経済",
         "description":"中国网络文学の連載・打賞経済は、AI生成テキストの将来的経済モデルの最も近い歴史的祖型を提供する。"}])

add(**C, name_ja="仙侠・玄幻",
    name_en="xianxia / xuanhuan",
    name_original="仙俠／玄幻",
    period_key="現代",
    definition="网络文学の主要ジャンル。仙侠は道教神話・武侠伝統を融合した修仙小説で、忘語『凡人修仙伝』(2007-)、耳根『仙逆』、辰東『遮天』等を代表作とする。玄幻は西洋ファンタジー要素を取り込んだ世界観構築型ジャンルで、唐家三少『斗羅大陸』、天蚕土豆『斗破蒼穹』等が代表的。両者あわせて中国网络文学の最大シェアを占める。",
    background="伝統武侠小説（金庸・古龍）の伝統、1990年代日本ライトノベル・MMORPGの影響、网络文学プラットフォームの長編連載モデル。",
    development="2010年代以降、英訳サイト『Wuxiaworld』(2014創設)を通じて世界各国の翻訳ファンダムを獲得し、中国大衆文学の世界輸出の中核となった。",
    historical_context="2000年代中国インターネット普及期と、伝統武侠の連載長編形式への現代的継承。",
    primary_source_url=WIKI_ZH+"仙俠小說",
    primary_source_type="維基百科: 仙俠小說",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="耽美・系統小説",
    name_en="danmei / system novels",
    name_original="耽美／系統小說",
    period_key="現代",
    definition="耽美は男性同性愛BL小説の中国網絡文学ジャンル。晋江文学城を主要拠点とし、墨香銅臭『魔道祖師』『天官賜福』、Priest『鎮魂』等が代表作で、影視化で全アジア的人気を獲得した。系統小説は主人公がゲーム的「システム」と契約してミッションを遂行する自己再帰的サブジャンル。両者あわせて2010年代以降の网络文学の中心潮流を成す。",
    background="日本BL文化・ゲーム文化のオンライン受容、晋江文学城（女性読者中心）の制度的成立。",
    development="2018-19年の影視化ブーム（『陳情令』『山河令』等）で全アジア的可視化を獲得し、中国大衆文学の世界輸出の重要分野となった。",
    historical_context="2010年代中国女性読者層の文学経済的台頭と、ジェンダー越境的物語消費の制度化。",
    primary_source_url=WIKI_ZH+"耽美",
    primary_source_type="維基百科: 耽美",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"系統小説は主人公が「システム」と契約しミッション処理する物語構造で、AIエージェント・人間とAIシステムの協働関係の文学的祖型として読みうる。",
         "related_ai_phenomenon":"AIエージェントと人間の協働関係の物語化"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="東アジア",
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
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth tag failed for {entry['name_ja']}: {e}")
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
        print(f"[c15-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c15-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
