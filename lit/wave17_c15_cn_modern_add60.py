"""LIT-DB Phase 2 Wave 17 — C15 Chinese modern literature ADD 60.

Subfield: lit_cn_modern (id=9), region='東アジア'.
Sources: 維基文庫 (zh.wikisource.org), CTEXT, 維基百科, 中国国家図書館,
Project Gutenberg (PD pre-1957), academic Wikipedia.

60 NEW non-overlapping concepts covering 五四 details, 文研会・新月派,
1930s小説, 戦時抗戦, 中華人民共和国期, 文革後・新時期, 21c.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("清", "Qing dynasty", 1644, 1911,
     "清朝期。1840年アヘン戦争以降は晩清として近代化と文学変革の時期。"),
    ("五四新文学期", "May Fourth era", 1915, 1927,
     "新青年創刊から国民革命まで、白話文学運動と新文学諸団体形成期。"),
    ("国民革命〜抗戦期", "National Revolution / Anti-Japanese War",
     1927, 1949,
     "国民政府期から日中戦争・国共内戦に至る民国期文学拡張期。"),
    ("毛沢東期", "Mao era", 1949, 1976,
     "中華人民共和国成立から文化大革命終結まで。延安文芸講話路線の制度化期。"),
    ("改革開放期", "Reform-and-Opening era", 1976, 1989,
     "毛沢東後の文学解放期。傷痕・尋根・先鋒・新写実が連続出現。"),
    ("現代", "Contemporary China", 1990, 2025,
     "1990年代市場化以降の華語圏全体の現代文学。"),
]


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_ZH = "https://zh.wikipedia.org/wiki/"
WSRC_ZH = "https://zh.wikisource.org/wiki/"
GUTEN = "https://www.gutenberg.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_cn_modern", region="東アジア",
         original_script="hanzi")


# ============================================================
# A: 五四詳細（10）
# ============================================================
add(**C, name_ja="魯迅『野草』",
    name_en="Lu Xun's Wild Grass",
    name_original="野草",
    period_key="五四新文学期",
    definition="魯迅(1881-1936)が1924-26年『語絲』に連載した散文詩集23篇。象徴主義・夢幻・寓話を駆使し近代中国知識人の絶望と抵抗を凝縮した。中国近代散文詩の頂点。",
    background="北京段祺瑞政府期の政治弾圧と魯迅個人の精神的危機。",
    development="戦後魯迅研究で散文詩の規範作品として正典化。",
    historical_context="1924-26年の北京政治混乱と知識人の苦境。",
    primary_source_url=WSRC_ZH+"野草",
    primary_source_type="維基文庫: 野草",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"夢と象徴の連鎖はAI生成の幻想テキスト構造の歴史的祖型。",
         "related_ai_phenomenon":"AI幻想テキスト生成"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"散文詩理論",
         "description":"魯迅『野草』はボードレール散文詩の中国的展開として比較詩学の中心事例。"}])

add(**C, name_ja="魯迅『故事新編』",
    name_en="Lu Xun's Old Tales Retold",
    name_original="故事新編",
    period_key="国民革命〜抗戦期",
    definition="魯迅が1922-35年に書き継ぎ1936年刊行した歴史小説集8篇。女媧・伯夷・荘子等の古典神話歴史人物を諷刺的に再話し、中国近代歴史小説の方法を確立した。",
    background="魯迅晩年の左翼論争期と古典再読衝動。",
    development="後の歴史小説（郭沫若劇、王小波等）に方法論を継承。",
    historical_context="1930年代上海左翼文化期の歴史的省察。",
    primary_source_url=WSRC_ZH+"故事新編",
    primary_source_type="維基文庫: 故事新編",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"正典","status":"rethinking",
         "rationale":"古典再話方法は正典テキストの再生成として、AI古典模倣テキスト生成の歴史的祖型。",
         "related_ai_phenomenon":"AI古典再話生成"}],
    cross_domain=[
        {"target_db":"Myth-Narratives","link_type":"shared_concept",
         "target_entity_name":"中国神話再話",
         "description":"魯迅『故事新編』は女媧・伯夷等の神話人物を諷刺的再話した中国神話現代化の典型。"}])

add(**C, name_ja="魯迅『朝花夕拾』",
    name_en="Lu Xun's Dawn Blossoms Plucked at Dusk",
    name_original="朝花夕拾",
    period_key="五四新文学期",
    definition="魯迅が1926年に書いた回想散文10篇。幼少期紹興・南京・仙台留学体験を回顧し、近代中国回想散文の規範を確立。藤野先生・百草園等の名篇を含む。",
    background="厦門大学・広州中山大学転任期の精神的危機と回想衝動。",
    development="中等教育教材定番として中国現代散文の代表作と化した。",
    historical_context="1926年北京三一八事件後の魯迅の南方流浪。",
    primary_source_url=WSRC_ZH+"朝花夕拾",
    primary_source_type="維基文庫: 朝花夕拾",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="周作人『自己的園地』",
    name_en="Zhou Zuoren's My Own Garden",
    name_original="自己的園地",
    period_key="五四新文学期",
    definition="周作人(1885-1967)が1923年に編んだ散文評論集。「自分の畑」概念で個人主義的文学論を提起し、五四「人的文学」観を発展させ閑適散文の系譜を開いた。",
    background="新潮社解散後の周作人の個人主義的転回。",
    development="林語堂・梁実秋らの閑適散文派の理論的源流となった。",
    historical_context="1920年代北京知識人社会の個人主義的潮流。",
    primary_source_url=WSRC_ZH+"自己的園地",
    primary_source_type="維基文庫: 自己的園地",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="周作人『雨天的書』",
    name_en="Zhou Zuoren's Book of Rainy Days",
    name_original="雨天的書",
    period_key="五四新文学期",
    definition="周作人が1925年に北新書局より刊行した散文集。日常瑣事と読書随想を「閑適筆致」で綴り、中国近代小品文の規範を確立した代表作。",
    background="1920年代北京苦雨齋の周作人の閑適生活。",
    development="現代散文「美文」概念の典型として正典化。",
    historical_context="北洋政府期北京の知識人文化サロン。",
    primary_source_url=WSRC_ZH+"雨天的書",
    primary_source_type="維基文庫: 雨天的書",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="胡適『嘗試集』",
    name_en="Hu Shih's Experiments",
    name_original="嘗試集",
    period_key="五四新文学期",
    definition="胡適(1891-1962)が1920年に刊行した中国近代最初の白話新詩集。古典詩形式から自由詩への過渡的試作を含み、中国近代新詩運動の始点となった画期的詩集。",
    background="留米時代のイマジズム受容と『新青年』白話詩論争。",
    development="郭沫若『女神』『新青年』詩派の新詩運動全体の出発点。",
    historical_context="1917-19年文学革命論争期の白話実験。",
    primary_source_url=WSRC_ZH+"嘗試集",
    primary_source_type="維基文庫: 嘗試集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"形式実験としての胡適嘗試はAI生成詩の形式探索の祖型。",
         "related_ai_phenomenon":"AI詩形式実験"},
        {"axis":"言語","status":"rethinking",
         "rationale":"白話文と古典文の境界実験はAI多言語スタイル切替の歴史的参照点。",
         "related_ai_phenomenon":"AIスタイル切替生成"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"プラグマティズム",
         "description":"胡適のプラグマティズム文学方法論はデューイ哲学の中国的応用。"}])

add(**C, name_ja="胡適『中国哲学史大綱』",
    name_en="Hu Shih's Outline of Chinese Philosophy",
    name_original="中國哲學史大綱",
    period_key="五四新文学期",
    definition="胡適が1919年に商務印書館から刊行した中国哲学史。プラグマティズム方法論で先秦諸子を再構成し、中国近代学術の方法的転回を宣言した記念碑的著作。",
    background="コロンビア大学デューイ門下の博士論文を基礎とする。",
    development="顧頡剛『古史辨』運動・近代国学方法論の母胎。",
    historical_context="五四期の科学的方法論受容と国故整理運動。",
    primary_source_url=WSRC_ZH+"中國哲學史大綱",
    primary_source_type="維基文庫: 中國哲學史大綱",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="陳独秀『新青年』論争",
    name_en="Chen Duxiu's New Youth debates",
    name_original="新青年論爭",
    period_key="五四新文学期",
    definition="陳独秀(1879-1942)主編『新青年』(1915-26)誌上で展開された文学革命・科学民主・反孔諸論争。文学革命論(1917)・易卜生号・馬克思主義紹介を通じ五四新文化運動の制度的中核を成した。",
    background="日本留学経験と上海亡命期の啓蒙活動。",
    development="中国共産党創設(1921)・現代中国思想史の出発点。",
    historical_context="1915-26年の中国知識人思想転換期。",
    primary_source_url=WSRC_ZH+"新青年",
    primary_source_type="維基文庫: 新青年",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"『新青年』論争は西洋近代思想の中国受容の制度的中核で、AI時代の異文化思想受容の歴史的参照点。",
         "related_ai_phenomenon":"AIによる異文化思想受容"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中国近代啓蒙思想",
         "description":"陳独秀『新青年』論争は中国近代啓蒙哲学の制度的中核。"}])

add(**C, name_ja="郭沫若『女神』",
    name_en="Guo Moruo's Goddesses",
    name_original="女神",
    period_key="五四新文学期",
    definition="郭沫若(1892-1978)が1921年に刊行した中国近代浪漫主義新詩集。ホイットマン・ゲーテ・タゴール影響下に「鳳凰涅槃」「天狗」等を含む狂熱的自我膨張詩を展開し、創造社の旗印となった。",
    background="九州帝国大学医学部留学期のホイットマン受容。",
    development="創造社浪漫主義の中核作品として中国近代詩史を画す。",
    historical_context="1919-21年の留日中国知識青年の自我形成期。",
    primary_source_url=WSRC_ZH+"女神",
    primary_source_type="維基文庫: 女神",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"郭沫若『女神』の自我膨張詩は近代中国主体形成の典型でAI時代主体問題の対比軸。",
         "related_ai_phenomenon":"AI時代主体形成"}])

add(**C, name_ja="郭沫若『屈原』",
    name_en="Guo Moruo's Qu Yuan",
    name_original="屈原_(劇本)",
    period_key="国民革命〜抗戦期",
    definition="郭沫若が1942年重慶で発表した5幕歴史劇。戦国楚詩人屈原の悲劇を通じ抗日民族精神を喚起し、抗戦期歴史劇の代表作として大成功を収めた。",
    background="重慶国民政府期の歴史劇による民族動員需要。",
    development="抗戦期歴史劇運動・社会主義中国歴史劇の祖型を成した。",
    historical_context="1942年皖南事変後の重慶政治状況。",
    primary_source_url=WIKI_ZH+"屈原_(劇本)",
    primary_source_type="維基百科: 屈原 (劇本)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

# ============================================================
# B: 文学研究会・新月派・創造社（10）
# ============================================================
add(**C, name_ja="田漢『獲虎之夜』",
    name_en="Tian Han's Night the Tiger was Caught",
    name_original="獲虎之夜",
    period_key="五四新文学期",
    definition="田漢(1898-1968)が1924年に発表した一幕劇。湖南山村の若者と娘の悲恋を新ロマン主義筆致で描き、創造社系話劇運動の初期代表作となった。",
    background="日本留学期の小山内薫・坪内逍遙劇運動受容。",
    development="南国社運動を経て中国近代話劇の制度的成立に寄与。",
    historical_context="1920年代上海近代演劇運動興隆期。",
    primary_source_url=WIKI_ZH+"獲虎之夜",
    primary_source_type="維基百科: 獲虎之夜",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="文学研究会・創造社論争",
    name_en="Literary Research Association vs Creation Society debate",
    name_original="文研會與創造社論爭",
    period_key="五四新文学期",
    definition="1922-25年に展開された五四二大文学団体間の論争。文学研究会の「人生のための文学」リアリズム路線と、創造社の「芸術のための芸術」浪漫主義が対立し、後の左翼文学路線形成に影響した。",
    background="1921年の両団体創立と機関誌『小説月報』『創造』の対立。",
    development="左聯成立(1930)による論争の止揚。",
    historical_context="1920年代中国新文学団体形成期。",
    primary_source_url=WIKI_ZH+"創造社",
    primary_source_type="維基百科: 創造社",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="徐志摩『再別康橋』",
    name_en="Xu Zhimo's Saying Goodbye to Cambridge Again",
    name_original="再別康橋",
    period_key="五四新文学期",
    definition="徐志摩(1897-1931)が1928年に発表した抒情詩。ケンブリッジ大学留学体験を回想し新月派音節美の極致を示した中国近代最も愛唱される詩篇。",
    background="ケンブリッジ留学体験と新月派格律詩運動。",
    development="新月派音節三美(音楽美・絵画美・建築美)の規範作品。",
    historical_context="1920年代後期新月派活動最盛期。",
    primary_source_url=WIKI_ZH+"再別康橋",
    primary_source_type="維基百科: 再別康橋",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"格律詩三美",
         "description":"徐志摩『再別康橋』は新月派音節美の到達点で詩学理論研究の中心事例。"}])

add(**C, name_ja="林徽因",
    name_en="Lin Huiyin",
    name_original="林徽因",
    period_key="国民革命〜抗戦期",
    definition="林徽因(1904-1955)は新月派詩人・建築学者。代表詩「你是人間的四月天」(1934)で中国近代女性詩の規範を確立、夫梁思成と中国古建築調査でも先駆的業績を残した。",
    background="ペンシルヴァニア大学建築留学・新月派サロン参加。",
    development="新月派音節美と知性詩の融合。中国近代女性知識人の象徴。",
    historical_context="1930-40年代北京新月派サロン文化。",
    primary_source_url=WIKI_ZH+"林徽因",
    primary_source_type="維基百科: 林徽因",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="聞一多『紅燭』",
    name_en="Wen Yiduo's Red Candle",
    name_original="紅燭",
    period_key="五四新文学期",
    definition="聞一多(1899-1946)が1923年に刊行した詩集。シカゴ大学留学期のキーツ受容と古典格律意識を融合し新月派理論的中核となった。聞一多は格律詩三美を提唱した。",
    background="清華学校・シカゴ大学留学期の英米浪漫派受容。",
    development="新月派『詩鐫』運動と『死水』へ展開。",
    historical_context="1920年代米国留学中国知識青年の文化的位置。",
    primary_source_url=WSRC_ZH+"紅燭",
    primary_source_type="維基文庫: 紅燭",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="聞一多『死水』",
    name_en="Wen Yiduo's Dead Water",
    name_original="死水",
    period_key="五四新文学期",
    definition="聞一多が1928年に刊行した詩集。表題詩は格律美の極致と社会批判の融合で、中国近代格律詩の到達点を示した。新月派音節三美の規範作品となる。",
    background="新月派『詩鐫』運動と格律詩実験成熟期。",
    development="後の格律新詩運動全般の規範。",
    historical_context="1928年北伐完了期の知識人苦悩。",
    primary_source_url=WSRC_ZH+"死水",
    primary_source_type="維基文庫: 死水",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="朱湘",
    name_en="Zhu Xiang",
    name_original="朱湘",
    period_key="五四新文学期",
    definition="朱湘(1904-1933)は新月派四詩人の一人。代表作『草莽集』(1927)で叙事詩・格律詩を実験し、29歳で長江入水自殺した悲劇的詩人。中国近代詩のソネット導入で先駆的業績。",
    background="清華学校教育・米国オハイオ大学留学体験。",
    development="新月派叙事詩・格律詩実験の重要担い手。",
    historical_context="1920-30年代新月派サロン文化。",
    primary_source_url=WIKI_ZH+"朱湘",
    primary_source_type="維基百科: 朱湘",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="陳夢家",
    name_en="Chen Mengjia",
    name_original="陳夢家",
    period_key="国民革命〜抗戦期",
    definition="陳夢家(1911-1966)は新月派後期詩人・甲骨学者。詩集『夢家詩集』(1931)・編著『新月詩選』(1931)で新月派総括を行い、後に殷代甲骨研究の世界的権威となった。",
    background="国立中央大学法学院・燕京大学宗教学院。",
    development="新月派総括者・甲骨学への転回が中国知識人軌跡の典型。",
    historical_context="1930年代新月派最終期と国学転回。",
    primary_source_url=WIKI_ZH+"陳夢家",
    primary_source_type="維基百科: 陳夢家",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="沈尹默『新潮』",
    name_en="Shen Yinmo and New Tide journal",
    name_original="新潮雜誌",
    period_key="五四新文学期",
    definition="沈尹默(1883-1971)・傅斯年・羅家倫が1919年北京大学新潮社で創刊した五四学生雑誌。『新青年』と並び五四新文化運動の二大誌で、新文学創作と西洋思想紹介を行った。",
    background="北京大学学生運動と『新青年』影響下の創刊。",
    development="顧頡剛『古史辨』・新文学創作の制度的母胎。",
    historical_context="1919年五四運動前後の北大学生文化。",
    primary_source_url=WIKI_ZH+"新潮社",
    primary_source_type="維基百科: 新潮社",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="新月派格律詩運動",
    name_en="Crescent Moon School metrical poetry movement",
    name_original="新月派格律詩運動",
    period_key="五四新文学期",
    definition="徐志摩・聞一多・朱湘らが1926年『晨報詩鐫』を中心に展開した格律新詩運動。音楽美・絵画美・建築美の三美原則で自由詩への反動として古典韻律を現代化、中国近代詩の重要潮流を成した。",
    background="自由詩過剰拡散への反動と英米格律詩規範の受容。",
    development="戴望舒・卞之琳・何其芳ら現代派詩人への影響。",
    historical_context="1926-31年新月派最盛期。",
    primary_source_url=WIKI_ZH+"新月派",
    primary_source_type="維基百科: 新月派",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

# ============================================================
# C: 1930s小説（10）
# ============================================================
add(**C, name_ja="茅盾『蝕』三部",
    name_en="Mao Dun's Eclipse Trilogy",
    name_original="蝕三部曲",
    period_key="国民革命〜抗戦期",
    definition="茅盾(1896-1981)が1927-28年に発表した『幻滅』『動揺』『追求』の三部作。北伐失敗後の革命知識青年の幻滅・動揺・追求を心理リアリズムで描いた中国近代心理小説の先駆。",
    background="国共分裂(1927)後の作者の上海亡命期の創作。",
    development="後の『子夜』(1933)『腐蝕』(1941)へ展開する茅盾社会派長編の起点。",
    historical_context="1927年蒋介石四・一二政変直後の知識人危機。",
    primary_source_url=WIKI_ZH+"蝕_(小說)",
    primary_source_type="維基百科: 蝕 (三部曲)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="沈従文『辺城』",
    name_en="Shen Congwen's Border Town",
    name_original="邊城",
    period_key="国民革命〜抗戦期",
    definition="沈従文(1902-1988)が1934年に発表した中編小説。湘西茶峒の少女翠翠を中心に湘西土地の純朴と悲哀を抒情的に描き、京派文学の頂点として現代田園小説の規範を確立した。",
    background="作者の湘西出身経験と京派抒情文学運動。",
    development="夏志清『中国現代小説史』で再評価され世界的中国近代文学正典化。",
    historical_context="1930年代北京京派サロン文化。",
    primary_source_url=WIKI_ZH+"邊城",
    primary_source_type="維基百科: 邊城",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"沈従文の湘西土地書写は失われた地方真正性を文学化する方法でAI時代土着性問題の参照。",
         "related_ai_phenomenon":"AI地方文化生成と真正性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"湘西民族誌",
         "description":"沈従文の湘西書写は中国西南部少数民族民族誌の文学的並行物。"}])

add(**C, name_ja="沈従文『湘行散記』",
    name_en="Shen Congwen's Recollections of West Hunan",
    name_original="湘行散記",
    period_key="国民革命〜抗戦期",
    definition="沈従文が1934年に湘西帰省途上の沅水紀行を綴った散文集。湘西の風土・船人・水夫を民族誌的観察と抒情的筆致で描き、中国近代散文の傑作とされる。",
    background="1934年母病報を受けた湘西帰省体験。",
    development="湘西世界三部作(『辺城』『長河』)の方法的基盤。",
    historical_context="1930年代中国地方民族誌文学興隆期。",
    primary_source_url=WIKI_ZH+"湘行散記",
    primary_source_type="維基百科: 湘行散記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="老舎『二馬』",
    name_en="Lao She's Mr. Ma and Son",
    name_original="二馬",
    period_key="国民革命〜抗戦期",
    definition="老舎が1929年ロンドン東洋学院教員時代に発表した長編小説。在英中国父子の異文化体験を諷刺的筆致で描き、作者初期諷刺長編三部作の最高傑作とされる。",
    background="ロンドン東洋学院教員期(1924-29)の在英中国人観察。",
    development="老舎『離婚』(1933)・『駱駝祥子』(1936)へ展開。",
    historical_context="1920年代英国中国人社会と異文化遭遇。",
    primary_source_url=WIKI_ZH+"二馬",
    primary_source_type="維基百科: 二馬",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="老舎『四世同堂』",
    name_en="Lao She's Four Generations Under One Roof",
    name_original="四世同堂",
    period_key="国民革命〜抗戦期",
    definition="老舎が1944-50年に書いた百万字長編小説三部作。日中戦争下北京小羊圏胡同の祁家四世代を中心に北京市民社会全景を描いた抗戦文学の最大の達成。",
    background="重慶抗戦期と戦後米国客員作家期の創作。",
    development="戦後社会主義中国における民族抗戦記憶の規範作品。",
    historical_context="1937-45年北京日本占領期の市民生活。",
    primary_source_url=WIKI_ZH+"四世同堂",
    primary_source_type="維基百科: 四世同堂",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"老舎の北京口語文学は地域口語の文学化でAI時代の方言生成問題の歴史的祖型。",
         "related_ai_phenomenon":"AI方言生成"}],
    cross_domain=[
        {"target_db":"Cultural-Intelligence","link_type":"shared_concept",
         "target_entity_name":"北京胡同文化",
         "description":"老舎『四世同堂』は北京胡同社会の文学的記録。"}])

add(**C, name_ja="蕭軍『八月的鄉村』",
    name_en="Xiao Jun's Village in August",
    name_original="八月的鄉村",
    period_key="国民革命〜抗戦期",
    definition="蕭軍(1907-1988)が1935年に上海で発表した中編小説。満洲国下の遊撃隊抗日闘争を描き、魯迅の支援で出版され東北作家群の代表作となった抗日文学先駆作品。",
    background="作者の東北満州体験と1934年上海亡命。",
    development="東北作家群(蕭紅・端木蕻良・駱賓基)抗戦文学の起点。",
    historical_context="満洲事変(1931)後の東北抗日闘争。",
    primary_source_url=WIKI_ZH+"八月的鄉村",
    primary_source_type="維基百科: 八月的鄉村",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="蕭紅『生死場』",
    name_en="Xiao Hong's Field of Life and Death",
    name_original="生死場",
    period_key="国民革命〜抗戦期",
    definition="蕭紅(1911-1942)が1935年に魯迅序文付きで発表した長編小説。東北農村女性の生殖・労働・抗日を独特の抒情的散文体で描き、中国近代女性文学の傑作とされる。",
    background="東北黒竜江出身体験と1934年上海亡命魯迅サロン参加。",
    development="夏志清・葛浩文評価で世界的中国近代女性文学正典化。",
    historical_context="満洲事変後の東北農村社会瓦解。",
    primary_source_url=WIKI_ZH+"生死場",
    primary_source_type="維基百科: 生死場",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"蕭紅の身体性散文体はAI時代における身体的経験のテキスト化問題への参照点。",
         "related_ai_phenomenon":"AI身体経験テキスト化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"女性身体の民族誌",
         "description":"蕭紅の女性身体描写は東北農村女性の民族誌的記録。"}])

add(**C, name_ja="蕭紅『呼蘭河伝』",
    name_en="Xiao Hong's Tales of Hulan River",
    name_original="呼蘭河傳",
    period_key="国民革命〜抗戦期",
    definition="蕭紅が1940年香港で完成した自伝的長編小説。故郷呼蘭河の童年回想を散文詩的・断片的構造で展開し、中国近代女性自伝小説の規範を確立。",
    background="作者の香港亡命期(1940-42)の故郷回想衝動。",
    development="後の自伝的女性文学(王安憶・林白)に影響。",
    historical_context="抗戦期香港の中国人亡命作家コミュニティ。",
    primary_source_url=WIKI_ZH+"呼蘭河傳",
    primary_source_type="維基百科: 呼蘭河傳",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="端木蕻良",
    name_en="Duanmu Hongliang",
    name_original="端木蕻良",
    period_key="国民革命〜抗戦期",
    definition="端木蕻良(1912-1996)は東北作家群代表。代表作『鴜鷺湖的憂鬱』(1936)・『科爾沁旗草原』(1939)で東北モンゴル草原社会を抒情的長編で描き、抗戦東北文学の重要担い手となった。",
    background="作者の東北遼寧出身と1934年上海亡命体験。",
    development="蕭紅と結婚し東北作家群中核を成した。",
    historical_context="東北作家群の上海・武漢・桂林転戦。",
    primary_source_url=WIKI_ZH+"端木蕻良",
    primary_source_type="維基百科: 端木蕻良",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="駱賓基",
    name_en="Luo Binji",
    name_original="駱賓基",
    period_key="国民革命〜抗戦期",
    definition="駱賓基(1917-1994)は東北作家群末期作家。『北望園的春天』(1944)『姜歩畏家史』等で東北抗日と地方社会を描き、戦後は古文字学者に転じた。蕭紅臨終看取り者として知られる。",
    background="東北吉林出身と1937年上海亡命。",
    development="東北作家群末期と社会主義中国古文字学への転回。",
    historical_context="抗戦末期重慶・桂林文人社会。",
    primary_source_url=WIKI_ZH+"駱賓基",
    primary_source_type="維基百科: 駱賓基",
    importance_score=2, source_tier="secondary", canonical_in_region="minor")

# ============================================================
# D: 戦時抗戦・人民共和国期（10）
# ============================================================
add(**C, name_ja="姚雪垠『差半車麦秸』",
    name_en="Yao Xueyin's Half a Cart of Wheat Straw",
    name_original="差半車麥秸",
    period_key="国民革命〜抗戦期",
    definition="姚雪垠(1910-1999)が1938年に発表した抗戦短編。河南農民出身ゲリラ兵の人物造形で抗戦初期文学の代表作となり、後に大長編歴史小説『李自成』(1963-99)で社会主義歴史小説の規範を作った。",
    background="抗戦初期作者の河南北方戦線体験。",
    development="戦後『李自成』五巻本で社会主義歴史小説の頂点に達した。",
    historical_context="1937-38年抗日戦争初期の華北農村抗戦。",
    primary_source_url=WIKI_ZH+"姚雪垠",
    primary_source_type="維基百科: 姚雪垠",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="丘東平",
    name_en="Qiu Dongping",
    name_original="丘東平",
    period_key="国民革命〜抗戦期",
    definition="丘東平(1910-1941)は左聯系抗戦作家。代表作『沈鬱的梅冷城』(1938)『第七連』(1939)で新四軍部隊の苦戦を硬質リアリズムで描き、塩城戦闘で30歳戦死した。",
    background="左聯参加と1938年新四軍政治部宣伝従事。",
    development="抗戦軍隊文学の規範を確立し戦死で伝説化した。",
    historical_context="1938-41年新四軍華中抗戦時期。",
    primary_source_url=WIKI_ZH+"丘東平",
    primary_source_type="維基百科: 丘東平",
    importance_score=2, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="趙樹理『李有才板話』",
    name_en="Zhao Shuli's Rhymes of Li Youcai",
    name_original="李有才板話",
    period_key="国民革命〜抗戦期",
    definition="趙樹理(1906-1970)が1943年に発表した中編小説。山西農村の階級闘争を山西梆子板話形式で描き、延安文芸講話路線に最も忠実な「工農兵文芸」規範作品となった。",
    background="作者の山西沁水農村出身と1937年延安移住。",
    development="山薬蛋派(西戎・馬烽・束為等)の規範を確立。",
    historical_context="1942年延安文芸座談会講話以降の文芸路線実践。",
    primary_source_url=WIKI_ZH+"李有才板話",
    primary_source_type="維基百科: 李有才板話",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="趙樹理『小二黒結婚』",
    name_en="Zhao Shuli's Marriage of Xiao Erhei",
    name_original="小二黑結婚",
    period_key="国民革命〜抗戦期",
    definition="趙樹理が1943年に発表した短編。解放区山西農村の自由恋愛と封建習俗の対立を民間説話風口語で描き、解放区文芸の最も成功した普及作品となった。",
    background="延安文芸講話以降の作者の解放区文芸実践。",
    development="解放区映画化(1950)を経て社会主義中国大衆文化規範に。",
    historical_context="1943年華北抗日解放区婦女解放運動。",
    primary_source_url=WIKI_ZH+"小二黑結婚",
    primary_source_type="維基百科: 小二黑結婚",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="柳青『創業史』",
    name_en="Liu Qing's Builders of a New Life",
    name_original="創業史",
    period_key="毛沢東期",
    definition="柳青(1916-1978)が1959年に発表した社会主義建設長編小説。陝西渭河平原の合作社化運動を梁生宝の人物造形で描き、社会主義リアリズム長編の規範作品となった。",
    background="作者の陝西長安皇甫村14年滞在体験。",
    development="社会主義リアリズム『創業史』『暴風驟雨』『紅旗譜』三大柱の一。",
    historical_context="1953-58年農業集団化運動。",
    primary_source_url=WIKI_ZH+"創業史",
    primary_source_type="維基百科: 創業史",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="楊沫『青春之歌』",
    name_en="Yang Mo's Song of Youth",
    name_original="青春之歌",
    period_key="毛沢東期",
    definition="楊沫(1914-1995)が1958年に発表した社会主義リアリズム長編小説。1930年代女性知識人林道静の革命的成長を描き、文革前最も人気を得た「成長小説」(教養小説)規範作品となった。",
    background="作者の北平女学生体験と1936年共産党入党。",
    development="社会主義中国「革命的成長小説」の最も影響力ある作品。",
    historical_context="1958年大躍進前夜の社会主義文芸高揚期。",
    primary_source_url=WIKI_ZH+"青春之歌",
    primary_source_type="維基百科: 青春之歌",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="梁斌『紅旗譜』",
    name_en="Liang Bin's Red Flag Saga",
    name_original="紅旗譜",
    period_key="毛沢東期",
    definition="梁斌(1914-1996)が1957年に発表した社会主義リアリズム長編小説。冀中農村三世代の階級闘争史を描き、毛沢東期紅色経典三大長編の一として「革命歴史小説」の規範を成した。",
    background="作者の河北蠡県農村出身と1930年代党活動体験。",
    development="文革後も社会主義中国紅色経典として読み継がれた。",
    historical_context="1957年反右派闘争前夜の社会主義文芸出版。",
    primary_source_url=WIKI_ZH+"紅旗譜",
    primary_source_type="維基百科: 紅旗譜",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="浩然『艷陽天』",
    name_en="Hao Ran's Bright Sunny Days",
    name_original="豔陽天",
    period_key="毛沢東期",
    definition="浩然(1932-2008)が1964-66年に発表した三巻本社会主義リアリズム長編。北京郊外農村合作社闘争を描き、文革期に唯一公認された農村小説作家として絶大な部数を記録した。",
    background="作者の河北農村出身と1956年党農村工作経験。",
    development="文革期『金光大道』(1972-76)で「八個樣板戯一個作家」と称された。",
    historical_context="1964-66年文革直前の社会主義文芸路線。",
    primary_source_url=WIKI_ZH+"艷陽天",
    primary_source_type="維基百科: 豔陽天",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="浩然『金光大道』",
    name_en="Hao Ran's Golden Road",
    name_original="金光大道",
    period_key="毛沢東期",
    definition="浩然が1972-76年に発表した文革期長編小説。河北農村の集団化路線を描いた文革期唯一の大型農村長編で、毛沢東農業政策の文学的祝祭として位置づけられた。",
    background="文革期工農兵作家路線下の唯一の専業小説家活動。",
    development="文革後批判対象とされたが90年代以降文学史的再評価。",
    historical_context="1972-76年文革末期の社会主義文芸状況。",
    primary_source_url=WIKI_ZH+"金光大道",
    primary_source_type="維基百科: 金光大道",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="樣板戲八大",
    name_en="eight model operas",
    name_original="八大樣板戲",
    period_key="毛沢東期",
    definition="文革期(1966-76)江青指導下に唯一公認された8大革命模範劇。京劇『紅燈記』『沙家浜』『智取威虎山』『海港』『奇襲白虎団』、革命バレエ『紅色娘子軍』『白毛女』、交響楽『沙家浜』を含み、文革期文芸の独占的中核を成した。",
    background="1966年江青「部隊文芸工作座談会紀要」以降の文芸独占。",
    development="文革後否定されたが2000年代以降「文革文化研究」対象として再評価。",
    historical_context="1966-76年文革期文芸極左路線。",
    primary_source_url=WIKI_ZH+"樣板戲",
    primary_source_type="維基百科: 樣板戲",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

# ============================================================
# E: 文革後・新時期作家（10）
# ============================================================
add(**C, name_ja="劉心武『班主任』",
    name_en="Liu Xinwu's Class Counsellor",
    name_original="班主任",
    period_key="改革開放期",
    definition="劉心武(1942-)が1977年『人民文学』に発表した短編小説。文革被害を受けた中学生を題材に「傷痕文学」第一作と位置づけられ、新時期文学開闢の象徴的作品となった。",
    background="文革直後の教育崩壊観察と1977年新時期文芸開放。",
    development="盧新華『傷痕』(1978)とともに傷痕文学を本格化させた。",
    historical_context="1977年文革直後の社会的精神的廃墟。",
    primary_source_url=WIKI_ZH+"班主任_(短篇小說)",
    primary_source_type="維基百科: 班主任",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="盧新華『傷痕』",
    name_en="Lu Xinhua's The Wounded",
    name_original="傷痕",
    period_key="改革開放期",
    definition="盧新華(1954-)が1978年8月『文匯報』に発表した短編小説。文革で親と引き裂かれた女性を描き「傷痕文学」運動の命名作品となり、新時期文芸の方向性を決定づけた。",
    background="復旦大学中文学生時代の文革体験形象化。",
    development="傷痕文学・反思文学・尋根文学への新時期文学三連動の起点。",
    historical_context="1978年改革開放始動期。",
    primary_source_url=WIKI_ZH+"傷痕_(小說)",
    primary_source_type="維基百科: 傷痕",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王蒙『布禮』",
    name_en="Wang Meng's Bolshevik Salute",
    name_original="布禮",
    period_key="改革開放期",
    definition="王蒙(1934-)が1979年に発表した中編小説。反右派闘争で迫害された幹部の20年を意識流技法で描き、反思文学の代表作となった。後の文化部長(1986-89)。",
    background="作者の1957年「組織部新来的青年人」事件と20年の新疆流浪。",
    development="王蒙『活動変人形』(1986)とともに反思文学規範作品。",
    historical_context="1979年反右派派事件名誉回復期。",
    primary_source_url=WIKI_ZH+"布禮",
    primary_source_type="維基百科: 布禮",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="韓少功『爸爸爸』",
    name_en="Han Shaogong's Pa Pa Pa",
    name_original="爸爸爸",
    period_key="改革開放期",
    definition="韓少功(1953-)が1985年に発表した中編小説。湖南山村の知能障害児丙仔を中心に楚文化深層と非合理性を描き、尋根文学の代表作・規範作品となった。",
    background="作者の湖南汨羅知青下放体験と楚文化研究。",
    development="後の『馬橋詞典』(1996)に至る尋根文学方法を確立。",
    historical_context="1985年「文化熱」期の文学的根源探索。",
    primary_source_url=WIKI_ZH+"爸爸爸",
    primary_source_type="維基百科: 爸爸爸",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="阿城『棋王』",
    name_en="A Cheng's The Chess Master",
    name_original="棋王",
    period_key="改革開放期",
    definition="阿城(鍾阿城、1949-)が1984年『上海文学』に発表した中編小説。雲南知青の象棋名人王一生を中心に道家伝統と知青体験を融合し、尋根文学・知青文学の頂点とされる傑作。",
    background="作者の雲南知青下放体験(1968-79)と古典文化教養。",
    development="『樹王』(1985)『孩子王』(1985)三部作で尋根文学規範化。",
    historical_context="1984-85年「文化熱」と知青文学第二波。",
    primary_source_url=WIKI_ZH+"棋王",
    primary_source_type="維基百科: 棋王",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"阿城『棋王』の道家的主体観は西洋近代主体への対抗でAI時代非自我的主体の参照点。",
         "related_ai_phenomenon":"AI時代非西洋主体観"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"道家美学",
         "description":"阿城『棋王』は道家美学の現代文学的展開。"}])

add(**C, name_ja="莫言『紅高粱家族』",
    name_en="Mo Yan's Red Sorghum",
    name_original="紅高粱家族",
    period_key="改革開放期",
    definition="莫言(管謨業、1955-)が1986年に発表した中編小説連作。山東高密農村の抗日と家族史を魔幻リアリズム筆致で描き、第五世代映画化(1987張芸謀)で世界的可視化、2012年ノーベル文学賞受賞の代表作。",
    background="作者の山東高密農村出身と解放軍芸術学院文学系修学。",
    development="魔幻リアリズム中国版の頂点として世界文学受容。",
    historical_context="1986年改革開放第二期文学最盛期。",
    primary_source_url=WIKI_ZH+"紅高粱家族",
    primary_source_type="維基百科: 紅高粱家族",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"魔幻リアリズム中国版の身体性・呪術性はAI時代の異種テキスト生成・幻想世界構築の歴史的祖型。",
         "related_ai_phenomenon":"AI幻想世界生成"},
        {"axis":"正典","status":"rethinking",
         "rationale":"ノーベル文学賞受賞による中国文学世界正典化はAI翻訳時代の正典化機制と接続する。",
         "related_ai_phenomenon":"AI時代の世界文学正典化"}],
    cross_domain=[
        {"target_db":"Cultural-Intelligence","link_type":"shared_concept",
         "target_entity_name":"高密農村文化",
         "description":"莫言の高密文化記録は山東農村文化の文学的民族誌。"}])

add(**C, name_ja="莫言『生死疲労』",
    name_en="Mo Yan's Life and Death are Wearing Me Out",
    name_original="生死疲勞",
    period_key="現代",
    definition="莫言が2006年に発表した長編小説。地主西門鬧の六道輪廻転生を通じ1950-2000年代中国農村史を描き、章回小説形式と魔幻リアリズムを融合した莫言中期最大の達成。",
    background="作者の山東高密農村四世代観察と章回伝統復興意識。",
    development="2012年ノーベル賞授賞演説でも言及された代表作。",
    historical_context="2006年莫言世界的可視化期。",
    primary_source_url=WIKI_ZH+"生死疲勞",
    primary_source_type="維基百科: 生死疲勞",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="余華『活着』",
    name_en="Yu Hua's To Live",
    name_original="活著",
    period_key="改革開放期",
    definition="余華(1960-)が1992年に発表した長編小説。地主の子福貴の60年苦難を「活着」一語に凝縮した抑制的散文で描き、張芸謀映画(1994)で世界化、20世紀末中国文学最高傑作の声を得た。",
    background="先鋒小説期から市井リアリズム転換期の作品。",
    development="『許三観売血記』(1995)とともに余華中期傑作の双璧。",
    historical_context="1992年南巡講話・市場経済転換期。",
    primary_source_url=WIKI_ZH+"活著_(小說)",
    primary_source_type="維基百科: 活著",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"余華『活着』の極限受苦物語は人間生存物語の最小化形式でAI物語生成と人間物語の境界問題の参照。",
         "related_ai_phenomenon":"AI物語生成と受苦物語"}])

add(**C, name_ja="余華『兄弟』",
    name_en="Yu Hua's Brothers",
    name_original="兄弟_(小說)",
    period_key="現代",
    definition="余華が2005-06年に発表した長編小説。文革期から改革開放期までの兄弟二人の運命を諷刺的・誇張的筆致で描き、当代中国の野蛮な現実を寓話化した余華後期代表作。",
    background="2000年代中国市場経済の野蛮的拡張観察。",
    development="後の『第七天』(2013)に至る余華当代中国諷刺の起点。",
    historical_context="2005年中国経済急成長期の社会矛盾。",
    primary_source_url=WIKI_ZH+"兄弟_(小說)",
    primary_source_type="維基百科: 兄弟 (小說)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="王安憶『長恨歌』",
    name_en="Wang Anyi's Song of Everlasting Sorrow",
    name_original="長恨歌_(王安憶)",
    period_key="現代",
    definition="王安憶(1954-)が1995年に発表した長編小説。1940年代上海ミス上海王琦瑤の40年を上海都市の女性史として描き、20世紀末上海書写の規範作品・茅盾文学賞受賞作。",
    background="上海作家王安憶の都市記憶探索と作家家系の文化的位置。",
    development="後の『天香』(2011)『紀実與虚構』(1993)に至る上海書写の中核。",
    historical_context="1990年代上海ノスタルジー文化興隆。",
    primary_source_url=WIKI_ZH+"長恨歌_(王安憶)",
    primary_source_type="維基百科: 長恨歌 (王安憶)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"王安憶『長恨歌』の女性主体40年史はAI時代女性主体物語生成の参照点。",
         "related_ai_phenomenon":"AI女性主体物語生成"}],
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"上海女性史",
         "description":"王安憶『長恨歌』は20世紀上海女性史の文学的形象。"}])

# ============================================================
# F: 90s-21c（10）
# ============================================================
add(**C, name_ja="賈平凹『廃都』",
    name_en="Jia Pingwa's Ruined City",
    name_original="廢都",
    period_key="現代",
    definition="賈平凹(1952-)が1993年に発表した長編小説。西安知識人の頽廃を『金瓶梅』風筆致で描き発禁となった問題作。後の『秦腔』(2005)『古爐』(2011)『山本』(2018)に至る賈平凹当代陝西書写の起点。",
    background="作者の西安在住知識人観察と古典『金瓶梅』方法受容。",
    development="2009年解禁後フランスFemina文学賞外国小説賞受賞。",
    historical_context="1993年市場化転換期知識人危機。",
    primary_source_url=WIKI_ZH+"廢都",
    primary_source_type="維基百科: 廢都",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="阿来『塵埃落定』",
    name_en="Alai's Red Poppies",
    name_original="塵埃落定",
    period_key="現代",
    definition="阿来(1959-)が1998年に発表した長編小説。チベット族土司の没落をチベット族「傻子」の視点で描き第5回茅盾文学賞最年少受賞、チベット族当代中国文学の頂点となった。",
    background="作者のチベット族出身体験と四川マルカム土司歴史調査。",
    development="後の『空山』(2005-09)に至る阿来チベット書写の規範。",
    historical_context="1998年中国少数民族文学興隆期。",
    primary_source_url=WIKI_ZH+"塵埃落定",
    primary_source_type="維基百科: 塵埃落定",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="閻連科『丁庄夢』",
    name_en="Yan Lianke's Dream of Ding Village",
    name_original="丁莊夢",
    period_key="現代",
    definition="閻連科(1958-)が2006年に発表した長編小説。河南売血エイズ村の悲劇を「神実主義」筆致で描き、政治的に問題視され大陸では削除版のみ刊行されたが世界翻訳で高評価を得た。",
    background="1990年代河南農村血液買売エイズ蔓延の社会調査。",
    development="後の『四書』(2010)『日熄』(2015)に至る閻連科神実主義の代表作。",
    historical_context="2000年代中国農村医療危機と検閲問題。",
    primary_source_url=WIKI_ZH+"丁莊夢",
    primary_source_type="維基百科: 丁莊夢",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"閻連科神実主義は超リアル現実をテキスト化する方法でAI時代の現実生成テキストの参照点。",
         "related_ai_phenomenon":"AI超リアル生成"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"村落エイズ社会",
         "description":"閻連科の河南売血エイズ村書写は当代中国農村医療民族誌。"}])

add(**C, name_ja="劉震雲『一句頂一萬句』",
    name_en="Liu Zhenyun's Someone to Talk To",
    name_original="一句頂一萬句",
    period_key="現代",
    definition="劉震雲(1958-)が2009年に発表した長編小説。河南農村三世代の「話の通じる相手」探求を独特の循環反復筆致で描き、第8回茅盾文学賞受賞・中国当代孤独表象の代表作となった。",
    background="作者の河南農村出身と当代孤独現象観察。",
    development="後の『一日三秋』(2021)に至る劉震雲循環文体の規範。",
    historical_context="2009年中国都市化加速期孤独現象。",
    primary_source_url=WIKI_ZH+"一句頂一萬句",
    primary_source_type="維基百科: 一句頂一萬句",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="畢飛宇『推拿』",
    name_en="Bi Feiyu's Massage",
    name_original="推拿_(小說)",
    period_key="現代",
    definition="畢飛宇(1964-)が2008年に発表した長編小説。盲人マッサージ師たちの集団生活と恋愛を細密心理リアリズムで描き、第8回茅盾文学賞受賞・婁燁映画化(2014)で世界的可視化。",
    background="作者の南京盲人按摩院取材体験。",
    development="後の畢飛宇都市底辺小説の代表作。",
    historical_context="2008年北京五輪期都市底辺問題顕在化。",
    primary_source_url=WIKI_ZH+"推拿_(小說)",
    primary_source_type="維基百科: 推拿 (小說)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="麦家『暗算』",
    name_en="Mai Jia's Plot Against",
    name_original="暗算",
    period_key="現代",
    definition="麦家(蔣本滸、1964-)が2003年に発表した長編小説。中国スパイ機関701局を描いた中国当代スパイ小説興隆の起点。後の『風声』(2007)『解密』(2002)とともに中国スパイ文学規範化。",
    background="作者の解放軍情報部隊勤務体験。",
    development="ドラマ化(2005)で大衆文化化、2014年英訳『Decoded』で世界化。",
    historical_context="2000年代中国大衆文学諜報サブジャンル興隆。",
    primary_source_url=WIKI_ZH+"暗算",
    primary_source_type="維基百科: 暗算",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="韓松",
    name_en="Han Song",
    name_original="韓松",
    period_key="現代",
    definition="韓松(1965-)は中国SF第三世代代表作家。『紅色海洋』(2004)『地鉄』(2010)『驅魔』(2017)等で中国の暗黒未来をディストピア的筆致で描き、劉慈欣と並ぶ中国SF双璧と評された。",
    background="作者の新華社記者経歴と中国社会観察。",
    development="2010年代中国SFニューウェーブの中核作家。",
    historical_context="2000年代中国SF再生期。",
    primary_source_url=WIKI_ZH+"韓松",
    primary_source_type="維基百科: 韓松",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"韓松ディストピアSFは中国未来テキスト生成の歴史的祖型としてAI時代に再読される。",
         "related_ai_phenomenon":"AIディストピア生成"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AIディストピア物語",
         "description":"韓松SFはAI時代社会想像の文学的予兆。"}])

add(**C, name_ja="郝景芳『北京折叠』",
    name_en="Hao Jingfang's Folding Beijing",
    name_original="北京摺疊",
    period_key="現代",
    definition="郝景芳(1984-)が2014年に発表した中編SF。三層折畳北京の階級分化を描き2016年第74回ヒューゴー賞中編部門受賞、劉慈欣後の中国SF国際的可視化を代表する作品となった。",
    background="作者の清華大学物理博士・経済学者経歴。",
    development="中国第四世代SFの国際的台頭の象徴的作品。",
    historical_context="2010年代中国都市階級分化深化期。",
    primary_source_url=WIKI_ZH+"北京摺疊",
    primary_source_type="維基百科: 北京摺疊",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"郝景芳の階級分割空間SFはAI時代における労働階層分化の文学的予言として読みうる。",
         "related_ai_phenomenon":"AI時代労働階層分化"}],
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"AI労働分断",
         "description":"郝景芳『北京折叠』はAIによる労働階層三分割の予兆的物語。"}])

add(**C, name_ja="双雪涛『平原上的摩西』",
    name_en="Shuang Xuetao's Moses on the Plain",
    name_original="平原上的摩西",
    period_key="現代",
    definition="双雪涛(1983-)が2015年に発表した中編小説。1990年代国営工場リストラ期の瀋陽鉄西区殺人事件をミステリ形式で描き、班宇・鄭執と並ぶ「東北文芸復興」三本柱の代表作となった。",
    background="作者の瀋陽鉄西区出身と1990年代国企業崩壊観察。",
    development="後の『飛行員』(2017)とともに中国ニューウェーブ短編規範。",
    historical_context="2010年代中国「東北文芸復興」現象。",
    primary_source_url=WIKI_ZH+"平原上的摩西",
    primary_source_type="維基百科: 雙雪濤",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="残雪",
    name_en="Can Xue",
    name_original="殘雪",
    period_key="改革開放期",
    definition="残雪(鄧小華、1953-)は中国実験文学最先鋒作家。『五香街』(2002)『黄泥街』(1986)『屈光不正』(2018)等で夢幻的・カフカ的・カオス的世界を描き、ノーベル文学賞候補としてアジア女性作家最有力候補の一人と目される。",
    background="湖南長沙裁縫家族出身・正規教育3年のみの異色経歴。",
    development="2010年代以降欧米で中国実験文学最高峰として高評価。",
    historical_context="1980年代先鋒文学の最も極端な実験的位置。",
    primary_source_url=WIKI_ZH+"殘雪",
    primary_source_type="維基百科: 殘雪",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"残雪のカオス的・夢幻的テキストはAI生成幻想テキストの最も近い文学的祖型。",
         "related_ai_phenomenon":"AIカオス生成"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"残雪の独学・夢日記方法は人間作者性の極限を示しAI作者性比較の参照点。",
         "related_ai_phenomenon":"AI作者性"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"カフカ的アレゴリー",
         "description":"残雪はカフカ的アレゴリー文学の中国的展開として比較文学正典化。"}])


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
        print(f"[c15-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c15-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
