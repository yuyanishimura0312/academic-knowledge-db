"""LIT-DB Phase 2 Wave 21 — C18: Japanese Modern Literature ADD 80.

Subfield: lit_jp_modern (id=11), region='日本'.
Existing 222 → target 302 toward 500.
Sources: 青空文庫 (PD primary), NDL Digital, J-STAGE, academic Wikipedia.

Eight blocks of 10:
  A: 戦時文学・戦後直後の日記文学
  B: 戦後派詳細（野間・椎名・梅崎・武田・大岡・福永）
  C: 第三の新人・遠藤・阿部昭
  D: 戦後詩運動・列島・荒地・吉野弘・茨木のり子・石垣りん
  E: 1960s-70s 大江・開高・安部・三島
  F: 1960s-70s 女性作家・中上・水上・川端・井上・司馬
  G: 1980s-90s ポストモダン（高橋源・田中康・村上龍・山田詠美・古井・後藤・阿部和重・保坂）
  H: 1990s-2010s（平野・古川・川上弘美・多和田・江國・角田・桜庭・西加奈子・村田・又吉・朝井）
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("昭和戦前戦中期", "Early Shōwa & Wartime", 1926, 1945,
     "昭和改元から敗戦までの文学期。プロレタリア文学興隆と弾圧、モダニズム展開、戦時文学。"),
    ("戦後期", "Postwar", 1945, 1970,
     "戦後派・第三の新人・原爆文学を生んだ被占領と再出発の時代。"),
    ("現代", "Contemporary", 1970, 2025,
     "内向の世代から在日文学・ライトノベル・ウェブ小説まで多元化した時代。"),
]

AOZORA = "https://www.aozora.gr.jp/"
NDL = "https://dl.ndl.go.jp/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
JSTAGE = "https://www.jstage.jst.go.jp/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_jp_modern", region="日本", original_script="japanese")


# ============================================================
# A: 戦時文学・戦後直後の日記文学（10件）
# ============================================================
add(**C, name_ja="火野葦平『麦と兵隊』",
    name_en="Hino Ashihei's Mugi to Heitai",
    name_original="麦と兵隊",
    period_key="昭和戦前戦中期",
    definition="火野葦平（1907-1960）が1938年に発表した従軍記。徐州会戦への従軍体験を兵卒視点で描き、戦時下のベストセラーとなった、兵隊三部作の第一作。",
    background="日中戦争激化と兵隊作家の従軍報道文学需要。",
    development="続く『土と兵隊』『花と兵隊』とともに戦時下国民文学を代表した。",
    historical_context="昭和13年の徐州会戦と戦時文学の興隆期。",
    primary_source_url=AOZORA+"index_pages/person1101.html",
    primary_source_type="青空文庫: 火野葦平",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="火野葦平『土と兵隊』",
    name_en="Hino Ashihei's Tsuchi to Heitai",
    name_original="土と兵隊",
    period_key="昭和戦前戦中期",
    definition="火野葦平が1938年に発表した従軍記。杭州湾上陸作戦を書簡形式で描き、『麦と兵隊』に続く兵隊三部作の第二作として戦時下に広く読まれた。",
    background="日中戦争南方戦線と書簡形式従軍文学。",
    development="兵隊三部作の中核として、戦時下文学の規範を形成した。",
    historical_context="昭和12-13年の杭州湾上陸作戦期。",
    primary_source_url=WIKI_JA+"%E5%9C%9F%E3%81%A8%E5%85%B5%E9%9A%8A",
    primary_source_type="Wikipedia: 土と兵隊",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="火野葦平『花と兵隊』",
    name_en="Hino Ashihei's Hana to Heitai",
    name_original="花と兵隊",
    period_key="昭和戦前戦中期",
    definition="火野葦平が1939年に発表した従軍記。広東占領後の中国南部を描き、兵隊三部作を完結させ、戦時下の代表的国民文学となった。",
    background="日中戦争中国南方戦線と兵隊作家活動。",
    development="戦後は戦争責任問題で批判の対象となり、葦平自殺の遠因となった。",
    historical_context="昭和14年の広東占領と日中戦争長期化。",
    primary_source_url=WIKI_JA+"%E8%8A%B1%E3%81%A8%E5%85%B5%E9%9A%8A",
    primary_source_type="Wikipedia: 花と兵隊",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="石川達三『生きてゐる兵隊』",
    name_en="Ishikawa Tatsuzō's Ikiteiru Heitai",
    name_original="生きてゐる兵隊",
    period_key="昭和戦前戦中期",
    definition="石川達三（1905-1985）が1938年に発表した中編小説。南京戦への従軍体験から日本兵の蛮行を描き、新聞紙法違反で発禁・有罪となった、戦時下文学弾圧の象徴的事件。",
    background="南京事件後の従軍取材と戦争実態描写の試み。",
    development="戦後完全版が刊行され、戦争文学の良心として再評価された。",
    historical_context="昭和13年の戦時下言論統制最盛期。",
    primary_source_url=WIKI_JA+"%E7%94%9F%E3%81%8D%E3%81%A6%E3%82%90%E3%82%8B%E5%85%B5%E9%9A%8A",
    primary_source_type="Wikipedia: 生きてゐる兵隊",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"戦争実態描写の発禁事件は、AI生成における検閲・規制問題の歴史的参照点。",
         "related_ai_phenomenon":"AI生成と検閲・規制"}])

add(**C, name_ja="高見順『敗戦日記』",
    name_en="Takami Jun's Haisen Nikki",
    name_original="敗戦日記",
    period_key="戦後期",
    definition="高見順（1907-1965）が1945年に記録した日記。敗戦前後の日本社会・文壇の動揺を克明に記録し、戦後刊行されて昭和20年史の第一級資料となった、敗戦期日記文学の代表作。",
    background="戦時下からの転換期における作家の日記記録習慣。",
    development="戦後の高見作家活動と『昭和文学盛衰史』への基礎資料となった。",
    historical_context="昭和20年の敗戦と占領開始期。",
    primary_source_url=WIKI_JA+"%E9%AB%98%E8%A6%8B%E9%A0%86",
    primary_source_type="Wikipedia: 高見順",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="内田百閒『東京焼盡』",
    name_en="Uchida Hyakken's Tōkyō Shōjin",
    name_original="東京焼盡",
    period_key="戦後期",
    definition="内田百閒（1889-1971）が1944-45年の東京空襲体験を記録した日記。淡々とした筆致で戦災と日常の崩壊を描き、戦争記録文学の傑作となった、百閒晩年の代表作。",
    background="百閒の日記文学伝統と東京大空襲体験。",
    development="戦後の百閒随筆活動の中核資料となり、戦争記録の文学的規範を成した。",
    historical_context="昭和19-20年の東京空襲と戦時生活崩壊期。",
    primary_source_url=WIKI_JA+"%E5%86%85%E7%94%B0%E7%99%BE%E9%96%93",
    primary_source_type="Wikipedia: 内田百閒",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="中島敦『山月記』",
    name_en="Nakajima Atsushi's Sangetsuki",
    name_original="山月記",
    period_key="昭和戦前戦中期",
    definition="中島敦（1909-1942）が1942年に発表した短編小説。唐代伝奇『人虎伝』に基づき、虎に変身した詩人李徴の自意識と悔恨を漢文調で描いた、戦時下漢文学的小説の最高峰。",
    background="中島の漢学的素養と虚弱体質の自意識。",
    development="高校国語教科書定番作品として、戦後文学教育の中核を成した。",
    historical_context="昭和17年の戦時下文学と漢文化回帰。",
    primary_source_url=AOZORA+"cards/000119/card624.html",
    primary_source_type="青空文庫: 山月記",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"李徴の自意識と人格変容は、AI時代の主体性変質問題の歴史的参照点。",
         "related_ai_phenomenon":"AI時代の主体性変質"}])

add(**C, name_ja="中島敦『李陵』",
    name_en="Nakajima Atsushi's Riryō",
    name_original="李陵",
    period_key="昭和戦前戦中期",
    definition="中島敦が1943年に発表した中編小説（没後刊行）。漢の武将李陵の匈奴投降と司馬遷の宮刑を絡めて描き、運命と倫理の問題を漢文調で追究した、中島漢文学的小説の代表作。",
    background="中島の漢学素養と病床における歴史小説執筆。",
    development="『山月記』と並ぶ中島漢文学的小説の双璧として、戦後も繰り返し読み継がれた。",
    historical_context="昭和17-18年の戦時下歴史小説期。",
    primary_source_url=AOZORA+"cards/000119/card621.html",
    primary_source_type="青空文庫: 李陵",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="中島敦『弟子』",
    name_en="Nakajima Atsushi's Deshi",
    name_original="弟子",
    period_key="昭和戦前戦中期",
    definition="中島敦が1943年に発表した中編小説（没後刊行）。孔子の弟子子路の生涯を漢文調で描き、師弟関係と倫理的生の問題を追究した、中島歴史小説の代表作の一つ。",
    background="中島の漢学的素養と『論語』への傾倒。",
    development="『山月記』『李陵』と並ぶ中島歴史小説三部作を成した。",
    historical_context="昭和18年の戦時下漢学回帰文学期。",
    primary_source_url=AOZORA+"cards/000119/card625.html",
    primary_source_type="青空文庫: 弟子",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="中島敦『光と風と夢』",
    name_en="Nakajima Atsushi's Hikari to Kaze to Yume",
    name_original="光と風と夢",
    period_key="昭和戦前戦中期",
    definition="中島敦が1942年に発表した中編小説。サモア島でのスティーヴンソン晩年を日記形式で描き、芥川賞候補となった、中島の異国題材小説の代表作。",
    background="中島のパラオ南洋庁勤務体験とスティーヴンソン研究。",
    development="戦時下の異国題材文学として、独自の位置を占めた。",
    historical_context="昭和17年の南洋関心と戦時下異国題材小説期。",
    primary_source_url=AOZORA+"cards/000119/card622.html",
    primary_source_type="青空文庫: 光と風と夢",
    importance_score=3, source_tier="primary", canonical_in_region="major")


# ============================================================
# B: 戦後派詳細（10件）
# ============================================================
add(**C, name_ja="野間宏『暗い絵』",
    name_en="Noma Hiroshi's Kurai E",
    name_original="暗い絵",
    period_key="戦後期",
    definition="野間宏（1915-1991）が1946年に発表した中編小説。京都帝大時代の左翼運動挫折を全体小説的方法で描き、戦後派文学の出発点を画した、戦後文学第一作。",
    background="戦時下の野間左翼運動体験と戦後派全体小説論。",
    development="続く『真空地帯』『青年の環』への野間文学展開を準備した。",
    historical_context="昭和21年の戦後文学再出発期。",
    primary_source_url=WIKI_JA+"%E6%9A%97%E3%81%84%E7%B5%B5",
    primary_source_type="Wikipedia: 暗い絵",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="野間宏『真空地帯』",
    name_en="Noma Hiroshi's Shinkū Chitai",
    name_original="真空地帯",
    period_key="戦後期",
    definition="野間宏が1952年に発表した長編小説。陸軍内務班の暴力的軍隊組織を全体小説的に描き、戦後派文学の到達点を示した、戦後軍隊文学の代表作。",
    background="野間の陸軍兵卒体験と戦後派全体小説論の方法的徹底。",
    development="毎日出版文化賞受賞作として戦後文学の規範を成した。",
    historical_context="昭和27年の朝鮮戦争・再軍備問題期。",
    primary_source_url=WIKI_JA+"%E7%9C%9F%E7%A9%BA%E5%9C%B0%E5%B8%AF",
    primary_source_type="Wikipedia: 真空地帯",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"組織暴力と全体主義",
         "description":"内務班全体小説は経営学的組織暴力論の戦後文学的並行物。"}])

add(**C, name_ja="野間宏『青年の環』",
    name_en="Noma Hiroshi's Seinen no Wa",
    name_original="青年の環",
    period_key="戦後期",
    definition="野間宏が1947-71年にわたり執筆した長編小説。被差別部落問題を中心に戦時下大阪の青年群像を全体小説的に描き、谷崎潤一郎賞受賞、戦後派全体小説の頂点を成した、野間畢生の大作。",
    background="野間の長年にわたる被差別部落調査と全体小説完成への執念。",
    development="戦後派全体小説の到達点として、後の井上ひさし大長編小説に影響を残した。",
    historical_context="昭和22-46年の戦後民主主義文学長期展開期。",
    primary_source_url=WIKI_JA+"%E9%9D%92%E5%B9%B4%E3%81%AE%E7%92%B0",
    primary_source_type="Wikipedia: 青年の環",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="椎名麟三『深夜の酒宴』",
    name_en="Shiina Rinzō's Shin'ya no Shuen",
    name_original="深夜の酒宴",
    period_key="戦後期",
    definition="椎名麟三（1911-1973）が1947年に発表した中編小説。アパートに住む下層労働者の実存的虚無を描き、戦後派文学の代表作の一つとなった、椎名実存主義文学の出発点。",
    background="椎名の戦前左翼運動体験と戦後実存主義受容。",
    development="続く『重き流れの中に』『邂逅』への椎名文学展開を準備した。",
    historical_context="昭和22年の戦後実存主義文学興隆期。",
    primary_source_url=WIKI_JA+"%E6%A4%8E%E5%90%8D%E9%BA%9F%E4%B8%89",
    primary_source_type="Wikipedia: 椎名麟三",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="椎名麟三『重き流れの中に』",
    name_en="Shiina Rinzō's Omoki Nagare no Naka ni",
    name_original="重き流れの中に",
    period_key="戦後期",
    definition="椎名麟三が1947年に発表した長編小説。鉄道労働者から共産党員へ至る青年像を実存主義的に描き、椎名戦後派文学の代表作となった。",
    background="椎名の鉄道労働者・左翼運動体験の文学化。",
    development="戦後派実存主義文学の代表作として位置づけられた。",
    historical_context="昭和22年の戦後労働運動再生期。",
    primary_source_url=WIKI_JA+"%E6%A4%8E%E5%90%8D%E9%BA%9F%E4%B8%89",
    primary_source_type="Wikipedia: 椎名麟三",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="椎名麟三『邂逅』",
    name_en="Shiina Rinzō's Kaikō",
    name_original="邂逅",
    period_key="戦後期",
    definition="椎名麟三が1952年に発表した長編小説。キリスト教受洗後の椎名による信仰と実存の探究を描き、戦後派から宗教文学への椎名の転換を示した代表作。",
    background="椎名のキリスト教受洗（1950）と信仰文学への展開。",
    development="戦後日本キリスト教文学の重要作品として位置づけられた。",
    historical_context="昭和27年の戦後宗教文学興隆期。",
    primary_source_url=WIKI_JA+"%E6%A4%8E%E5%90%8D%E9%BA%9F%E4%B8%89",
    primary_source_type="Wikipedia: 椎名麟三",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="梅崎春生『桜島』",
    name_en="Umezaki Haruo's Sakurajima",
    name_original="桜島",
    period_key="戦後期",
    definition="梅崎春生（1915-1965）が1946年に発表した中編小説。海軍暗号兵として桜島基地で敗戦を迎えた体験を描き、戦後派文学の出発点的作品となった、戦後海軍文学の代表作。",
    background="梅崎の海軍暗号兵体験と戦後文学再生期の自伝的小説需要。",
    development="続く『日の果て』『ボロ家の春秋』への梅崎文学展開を準備した。",
    historical_context="昭和21年の戦後派文学第一陣登場期。",
    primary_source_url=AOZORA+"cards/000110/card4569.html",
    primary_source_type="青空文庫: 桜島",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="梅崎春生『日の果て』",
    name_en="Umezaki Haruo's Hi no Hate",
    name_original="日の果て",
    period_key="戦後期",
    definition="梅崎春生が1947年に発表した中編小説。南方戦線の壊滅的状況下の兵士心理を描き、『桜島』に続く戦争文学として戦後派文学の方向性を確立した。",
    background="梅崎の戦争体験と戦後派戦争文学の方法的展開。",
    development="戦後派戦争文学の代表作の一つとして位置づけられた。",
    historical_context="昭和22年の戦後戦争文学興隆期。",
    primary_source_url=WIKI_JA+"%E6%A2%85%E5%B4%8E%E6%98%A5%E7%94%9F",
    primary_source_type="Wikipedia: 梅崎春生",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="武田泰淳『司馬遷』",
    name_en="Takeda Taijun's Shibasen",
    name_original="司馬遷",
    period_key="昭和戦前戦中期",
    definition="武田泰淳（1912-1976）が1943年に刊行した評論。司馬遷『史記』を「世界史の中の人」として読み解き、戦時下の歴史思考を深めた、武田の代表的評論作。",
    background="武田の中国文学者としての素養と戦時下歴史思考。",
    development="戦後の武田文学の哲学的基盤を成し、『風媒花』『富士』へ展開した。",
    historical_context="昭和18年の戦時下中国学興隆期。",
    primary_source_url=WIKI_JA+"%E6%AD%A6%E7%94%B0%E6%B3%B0%E6%B7%B3",
    primary_source_type="Wikipedia: 武田泰淳",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"歴史哲学と東洋思想",
         "description":"司馬遷論は東洋歴史哲学の戦時下文学的展開の事例。"}])

add(**C, name_ja="武田泰淳『ひかりごけ』",
    name_en="Takeda Taijun's Hikarigoke",
    name_original="ひかりごけ",
    period_key="戦後期",
    definition="武田泰淳が1954年に発表した中編小説。北海道知床の難破船船長の食人事件を素材に、極限状況の倫理を裁判劇形式で追究した、戦後実存主義文学の代表作。",
    background="北海道知床事件と戦後実存倫理問題への武田の関心。",
    development="戦後派実存文学の代表作として戦後文学の規範を成した。",
    historical_context="昭和29年の戦後実存主義文学最盛期。",
    primary_source_url=WIKI_JA+"%E3%81%B2%E3%81%8B%E3%82%8A%E3%81%94%E3%81%91",
    primary_source_type="Wikipedia: ひかりごけ",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# C: 第三の新人・遠藤・阿部昭ほか（10件）
# ============================================================
add(**C, name_ja="大岡昇平『俘虜記』",
    name_en="Ōoka Shōhei's Furyoki",
    name_original="俘虜記",
    period_key="戦後期",
    definition="大岡昇平（1909-1988）が1948年に発表した中編小説。フィリピンでの米軍捕虜体験を冷徹な観察眼で描き、横光利一賞受賞、戦後派文学の代表作の一つとなった。",
    background="大岡のレイテ島従軍・米軍捕虜体験と戦後派的観察方法。",
    development="続く『野火』『レイテ戦記』への大岡戦争文学展開を準備した。",
    historical_context="昭和23年の戦後派戦争文学興隆期。",
    primary_source_url=WIKI_JA+"%E4%BF%98%E8%99%9C%E8%A8%98",
    primary_source_type="Wikipedia: 俘虜記",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="大岡昇平『野火』",
    name_en="Ōoka Shōhei's Nobi",
    name_original="野火",
    period_key="戦後期",
    definition="大岡昇平が1951年に発表した長編小説。フィリピン戦線敗走中の食人体験を扱い、極限状況の倫理を追究した、戦後派戦争文学の最高傑作の一つ。",
    background="大岡のレイテ島敗走体験と戦後実存倫理問題。",
    development="読売文学賞受賞作として戦後派文学の頂点を成した。",
    historical_context="昭和26年の戦後派戦争文学頂点期。",
    primary_source_url=WIKI_JA+"%E9%87%8E%E7%81%AB",
    primary_source_type="Wikipedia: 野火",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"倫理","status":"rethinking",
         "rationale":"極限状況の倫理探究は、AI時代の倫理判断問題の歴史的参照点。",
         "related_ai_phenomenon":"AI極限倫理判断"}])

add(**C, name_ja="大岡昇平『レイテ戦記』",
    name_en="Ōoka Shōhei's Reite Senki",
    name_original="レイテ戦記",
    period_key="現代",
    definition="大岡昇平が1967-69年にわたり発表した長編戦記。フィリピン・レイテ戦の全体像を史実調査と従軍体験で再構成し、戦後戦記文学の最高峰を成した、大岡畢生の大作。",
    background="大岡の長年にわたるレイテ戦調査と戦記文学への執念。",
    development="毎日芸術賞受賞作として戦後戦記文学の規範を成した。",
    historical_context="昭和42-44年の戦後再評価期。",
    primary_source_url=WIKI_JA+"%E3%83%AC%E3%82%A4%E3%83%86%E6%88%A6%E8%A8%98",
    primary_source_type="Wikipedia: レイテ戦記",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="福永武彦『死の島』",
    name_en="Fukunaga Takehiko's Shi no Shima",
    name_original="死の島",
    period_key="現代",
    definition="福永武彦（1918-1979）が1971年に発表した長編小説。広島の被爆女性の二重人格を多層的方法で描き、日本芸術院賞受賞、福永文学の頂点を成した、戦後原爆文学の代表作。",
    background="福永の戦後派文学方法と広島原爆問題への長年の関心。",
    development="戦後派モダニズム文学の到達点として位置づけられた。",
    historical_context="昭和46年の戦後派文学成熟期。",
    primary_source_url=WIKI_JA+"%E6%AD%BB%E3%81%AE%E5%B3%B6",
    primary_source_type="Wikipedia: 死の島",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="福永武彦『草の花』",
    name_en="Fukunaga Takehiko's Kusa no Hana",
    name_original="草の花",
    period_key="戦後期",
    definition="福永武彦が1954年に発表した長編小説。一高時代の同性愛的友情と療養所での死を描き、戦後派モダニズム文学の代表作となった、福永文学の出発点的作品。",
    background="福永の一高療養所体験と西欧モダニズム文学受容。",
    development="戦後派モダニズム文学の代表作として、後の福永文学の方向性を定めた。",
    historical_context="昭和29年の戦後派モダニズム文学期。",
    primary_source_url=WIKI_JA+"%E7%A6%8F%E6%B0%B8%E6%AD%A6%E5%BD%A6",
    primary_source_type="Wikipedia: 福永武彦",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="中村真一郎『死の影の下に』",
    name_en="Nakamura Shin'ichirō's Shi no Kage no Shita ni",
    name_original="死の影の下に",
    period_key="戦後期",
    definition="中村真一郎（1918-1997）が1947年に発表した長編連作小説。プルースト的時間意識を方法に戦時下青春の意識を描き、戦後派モダニズム文学の出発点となった、中村文学の代表作。",
    background="中村のプルースト『失われた時を求めて』翻訳と意識小説方法。",
    development="続く五部作として戦後派モダニズム文学の中核を成した。",
    historical_context="昭和22年の戦後派モダニズム文学黎明期。",
    primary_source_url=WIKI_JA+"%E4%B8%AD%E6%9D%91%E7%9C%9F%E4%B8%80%E9%83%8E",
    primary_source_type="Wikipedia: 中村真一郎",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="加藤周一『ある晴れた日に』",
    name_en="Katō Shūichi's Aru Hareta Hi ni",
    name_original="ある晴れた日に",
    period_key="戦後期",
    definition="加藤周一（1919-2008）が1949年に発表した長編小説。敗戦前後の医学生青年群像を知性的方法で描き、戦後派文学の代表作の一つとなった、加藤の数少ない小説作品。",
    background="加藤の医学生体験と戦後派知性主義文学への展開。",
    development="後の加藤評論活動への文学的基盤を成した。",
    historical_context="昭和24年の戦後派文学興隆期。",
    primary_source_url=WIKI_JA+"%E5%8A%A0%E8%97%A4%E5%91%A8%E4%B8%80",
    primary_source_type="Wikipedia: 加藤周一",
    importance_score=3, source_tier="secondary", canonical_in_region="marginal")

add(**C, name_ja="堀田善衛『広場の孤独』",
    name_en="Hotta Yoshie's Hiroba no Kodoku",
    name_original="広場の孤独",
    period_key="戦後期",
    definition="堀田善衛（1918-1998）が1951年に発表した長編小説。朝鮮戦争下の新聞記者の苦悩を描き、芥川賞受賞、戦後派文学の国際性を示した堀田の代表作。",
    background="堀田の上海体験と戦後アジア情勢への関心。",
    development="続く『インドで考えたこと』『方丈記私記』への堀田文学展開を準備した。",
    historical_context="昭和26年の朝鮮戦争・国際情勢緊迫期。",
    primary_source_url=WIKI_JA+"%E5%A0%80%E7%94%B0%E5%96%84%E8%A1%9B",
    primary_source_type="Wikipedia: 堀田善衛",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="安岡章太郎『海辺の光景』",
    name_en="Yasuoka Shōtarō's Umibe no Kōkei",
    name_original="海辺の光景",
    period_key="戦後期",
    definition="安岡章太郎（1920-2013）が1959年に発表した中編小説。母の死を契機に過去を回想する形式で家族崩壊を描き、野間文芸賞受賞、第三の新人文学の代表作となった。",
    background="安岡の母の死と私小説的告白方法の深化。",
    development="第三の新人文学の頂点的作品として位置づけられた。",
    historical_context="昭和34年の第三の新人文学成熟期。",
    primary_source_url=WIKI_JA+"%E5%AE%89%E5%B2%A1%E7%AB%A0%E5%A4%AA%E9%83%8E",
    primary_source_type="Wikipedia: 安岡章太郎",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="吉行淳之介『驟雨』",
    name_en="Yoshiyuki Junnosuke's Shūu",
    name_original="驟雨",
    period_key="戦後期",
    definition="吉行淳之介（1924-1994）が1954年に発表した短編小説。娼婦との関係を心理的に描き、芥川賞受賞、第三の新人文学の代表作となった吉行の出世作。",
    background="吉行の娼婦街取材と心理小説方法の確立。",
    development="続く『砂の上の植物群』『暗室』への吉行文学展開を準備した。",
    historical_context="昭和29年の第三の新人文学興隆期。",
    primary_source_url=WIKI_JA+"%E5%90%89%E8%A1%8C%E6%B7%B3%E4%B9%8B%E4%BB%8B",
    primary_source_type="Wikipedia: 吉行淳之介",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: 第三の新人後半・戦後詩・吉野・茨木・石垣（10件）
# ============================================================
add(**C, name_ja="庄野潤三『プールサイド小景』",
    name_en="Shōno Junzō's Poolside Shōkei",
    name_original="プールサイド小景",
    period_key="戦後期",
    definition="庄野潤三（1921-2009）が1954年に発表した短編小説。中産階級家庭の崩壊兆候をプールサイドの一場面で描き、芥川賞受賞、第三の新人文学の代表作となった。",
    background="庄野の中産階級的日常観察と心境小説方法の現代化。",
    development="後の『静物』『夕べの雲』への庄野家族小説展開を準備した。",
    historical_context="昭和29年の高度成長前夜の家族小説期。",
    primary_source_url=WIKI_JA+"%E5%BA%84%E9%87%8E%E6%BD%A4%E4%B8%89",
    primary_source_type="Wikipedia: 庄野潤三",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="小島信夫『アメリカン・スクール』",
    name_en="Kojima Nobuo's American School",
    name_original="アメリカン・スクール",
    period_key="戦後期",
    definition="小島信夫（1915-2006）が1954年に発表した短編小説。占領下の英語教師団の珍奇な見学体験を描き、芥川賞受賞、第三の新人文学の代表作となった、戦後占領文学の傑作。",
    background="小島の英語教師体験と占領下日本の文化的位相観察。",
    development="後の『抱擁家族』『別れる理由』への小島文学展開を準備した。",
    historical_context="昭和29年の占領下文学最終期。",
    primary_source_url=WIKI_JA+"%E5%B0%8F%E5%B3%B6%E4%BF%A1%E5%A4%AB",
    primary_source_type="Wikipedia: 小島信夫",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"占領下文化接触",
         "description":"占領下英語教師描写は人類学的文化接触の文学的事例。"}])

add(**C, name_ja="小島信夫『抱擁家族』",
    name_en="Kojima Nobuo's Hōyō Kazoku",
    name_original="抱擁家族",
    period_key="現代",
    definition="小島信夫が1965年に発表した長編小説。妻の不倫を契機とした中産階級家族崩壊を描き、谷崎潤一郎賞第一回受賞、戦後家族小説の代表作となった。",
    background="戦後民主主義家族の理想と現実の乖離問題。",
    development="戦後家族小説の規範を成し、後の家族崩壊小説に影響した。",
    historical_context="昭和40年の高度成長期家族論興隆期。",
    primary_source_url=WIKI_JA+"%E6%8A%B1%E6%93%81%E5%AE%B6%E6%97%8F",
    primary_source_type="Wikipedia: 抱擁家族",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="遠藤周作『白い人』",
    name_en="Endō Shūsaku's Shiroi Hito",
    name_original="白い人",
    period_key="戦後期",
    definition="遠藤周作（1923-1996）が1955年に発表した中編小説。第二次大戦下フランスの対独協力者を描き、芥川賞受賞、遠藤キリスト教文学の出発点となった作品。",
    background="遠藤のフランス留学体験とキリスト教文学への展開。",
    development="続く『黄色い人』『海と毒薬』『沈黙』への遠藤文学展開を準備した。",
    historical_context="昭和30年の戦後キリスト教文学興隆期。",
    primary_source_url=WIKI_JA+"%E9%81%A0%E8%97%A4%E5%91%A8%E4%BD%9C",
    primary_source_type="Wikipedia: 遠藤周作",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="遠藤周作『海と毒薬』",
    name_en="Endō Shūsaku's Umi to Dokuyaku",
    name_original="海と毒薬",
    period_key="戦後期",
    definition="遠藤周作が1957-58年に発表した長編小説。九州大学医学部での米軍捕虜生体解剖事件を素材に、日本人の倫理意識と神なき罪意識を追究した、遠藤キリスト教文学の代表作。",
    background="九大生体解剖事件と遠藤の神なき日本人論の深化。",
    development="新潮社文学賞受賞作として戦後キリスト教文学の規範を成した。",
    historical_context="昭和32-33年の戦後倫理問題追究期。",
    primary_source_url=WIKI_JA+"%E6%B5%B7%E3%81%A8%E6%AF%92%E8%96%AC",
    primary_source_type="Wikipedia: 海と毒薬",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="遠藤周作『侍』",
    name_en="Endō Shūsaku's Samurai",
    name_original="侍",
    period_key="現代",
    definition="遠藤周作が1980年に発表した長編小説。江戸初期の支倉常長遣欧使節を素材に、東西文化接触とキリスト教受容の問題を追究した、野間文芸賞受賞作。",
    background="遠藤の長年にわたるキリシタン研究と歴史小説への展開。",
    development="『沈黙』『深い河』とともに遠藤キリスト教歴史文学の三部作を成した。",
    historical_context="昭和55年の遠藤キリシタン文学頂点期。",
    primary_source_url=WIKI_JA+"%E4%BE%8D_(%E9%81%A0%E8%97%A4%E5%91%A8%E4%BD%9C)",
    primary_source_type="Wikipedia: 侍",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="遠藤周作『深い河』",
    name_en="Endō Shūsaku's Fukai Kawa",
    name_original="深い河",
    period_key="現代",
    definition="遠藤周作が1993年に発表した長編小説。インド・ガンジス河を舞台に各々の苦悩を抱えた日本人巡礼者を描き、毎日芸術賞受賞、遠藤キリスト教文学の最終到達点となった。",
    background="遠藤のインド体験と多元宗教論への晩年の展開。",
    development="遠藤畢生の代表作として、世界文学にも翻訳された。",
    historical_context="平成5年の遠藤晩年期。",
    primary_source_url=WIKI_JA+"%E6%B7%B1%E3%81%84%E6%B2%B3",
    primary_source_type="Wikipedia: 深い河",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"宗教多元主義",
         "description":"『深い河』の宗教多元主義は、宗教哲学の文学的展開事例。"}])

add(**C, name_ja="阿部昭『司令の休暇』",
    name_en="Abe Akira's Shirei no Kyūka",
    name_original="司令の休暇",
    period_key="現代",
    definition="阿部昭（1934-1989）が1970年に発表した中編小説。海軍司令官だった父との記憶を私小説的に描き、新潮新人賞受賞、内向の世代文学の代表作となった阿部の出世作。",
    background="阿部の海軍司令官父への記憶と内向の世代的方法。",
    development="続く『単純な生活』『無縁の生活』への阿部文学展開を準備した。",
    historical_context="昭和45年の内向の世代文学黎明期。",
    primary_source_url=WIKI_JA+"%E9%98%BF%E9%83%A8%E6%98%AD",
    primary_source_type="Wikipedia: 阿部昭",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="戦後詩運動",
    name_en="Postwar poetry movements",
    name_original="戦後詩運動",
    period_key="戦後期",
    definition="敗戦後に「荒地」「列島」「四季」などの詩誌を中心に展開した戦後詩運動。鮎川信夫・田村隆一らの『荒地』、関根弘らの『列島』が双璧を成し、戦後現代詩の方向性を決定づけた。",
    background="敗戦と戦争責任意識の中で再出発した詩人たちの結集。",
    development="50年代『櫂』、60年代以降の現代詩多様化への基盤となった。",
    historical_context="昭和20-30年代の戦後詩興隆期。",
    primary_source_url=WIKI_JA+"%E8%8D%92%E5%9C%B0_(%E8%A9%A9%E8%AA%8C)",
    primary_source_type="Wikipedia: 荒地",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="関根弘ら詩誌『列島』",
    name_en="Sekine Hiroshi et al. Rettō poetry magazine",
    name_original="列島",
    period_key="戦後期",
    definition="関根弘（1920-1994）・木島始らが1952年に創刊した戦後詩誌。社会主義リアリズムを基盤に労働者・大衆の現実を詩語化し、『荒地』とともに戦後詩の双璧を成した、戦後左翼詩運動の中核。",
    background="戦後労働運動と社会主義詩の国際的潮流。",
    development="60年代以降の社会派詩・現代詩の方向性に影響した。",
    historical_context="昭和27年の戦後社会派詩運動期。",
    primary_source_url=WIKI_JA+"%E5%88%97%E5%B3%B6_(%E8%A9%A9%E8%AA%8C)",
    primary_source_type="Wikipedia: 列島",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: 戦後詩補完・1960s-70s 大江・開高・安部・三島（10件）
# ============================================================
add(**C, name_ja="飯島耕一『ウイリアム・ブレイクを憶い出す詩』",
    name_en="Iijima Kōichi's Poem Recalling William Blake",
    name_original="ウイリアム・ブレイクを憶い出す詩",
    period_key="戦後期",
    definition="飯島耕一（1930-2013）が1956年に発表した詩集『他人の空』所収の代表詩。シュルレアリスム的方法でブレイク的幻視を現代化し、戦後シュルレアリスム詩運動の代表作となった。",
    background="飯島のシュルレアリスム研究と『鰐』詩誌活動。",
    development="戦後シュルレアリスム詩の代表作として位置づけられた。",
    historical_context="昭和31年の戦後前衛詩興隆期。",
    primary_source_url=WIKI_JA+"%E9%A3%AF%E5%B3%B6%E8%80%95%E4%B8%80",
    primary_source_type="Wikipedia: 飯島耕一",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="吉野弘『I was born』",
    name_en="Yoshino Hiroshi's I was born",
    name_original="I was born",
    period_key="戦後期",
    definition="吉野弘（1926-2014）が1957年に発表した代表詩。「生れる」を受身形で捉える英語表現に着想した、母の生命と引き換えの誕生という存在論的洞察を詩化した、戦後現代詩の名作。",
    background="吉野の労働者詩人としての出発と日常的詩語の追求。",
    development="教科書定番作品として戦後詩教育の中核を成した。",
    historical_context="昭和32年の戦後現代詩成熟期。",
    primary_source_url=WIKI_JA+"%E5%90%89%E9%87%8E%E5%BC%98_(%E8%A9%A9%E4%BA%BA)",
    primary_source_type="Wikipedia: 吉野弘",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="石垣りん『わたしの前にある鍋とお釜と燃える火と』",
    name_en="Ishigaki Rin's The Pot, The Rice Cooker and Burning Flames",
    name_original="わたしの前にある鍋とお釜と燃える火と",
    period_key="戦後期",
    definition="石垣りん（1920-2004）が1959年に発表した代表詩集の表題作。日常の台所労働を女性主体の存在論として詩化し、戦後女性詩の代表作となった石垣の出世作。",
    background="石垣の銀行勤務生活詩人としての出発と女性詩運動。",
    development="戦後女性詩の代表作として教科書定番化した。",
    historical_context="昭和34年の戦後女性詩興隆期。",
    primary_source_url=WIKI_JA+"%E7%9F%B3%E5%9E%A3%E3%82%8A%E3%82%93",
    primary_source_type="Wikipedia: 石垣りん",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"日常労働の女性主体詩は、AI時代の労働主体問題の歴史的参照点。",
         "related_ai_phenomenon":"AI時代の労働主体表現"}])

add(**C, name_ja="黒田喜夫『不安と遊撃』",
    name_en="Kuroda Kio's Fuan to Yūgeki",
    name_original="不安と遊撃",
    period_key="戦後期",
    definition="黒田喜夫（1926-1984）が1959年に刊行した第一詩集。戦後農村と都市労働の現実を社会派的方法で詩化し、H氏賞受賞、戦後社会派詩運動の代表作となった。",
    background="黒田の農村出身者・労働者詩人としての出発と『列島』派活動。",
    development="戦後社会派詩の代表作として位置づけられた。",
    historical_context="昭和34年の戦後社会派詩興隆期。",
    primary_source_url=WIKI_JA+"%E9%BB%92%E7%94%B0%E5%96%9C%E5%A4%AB",
    primary_source_type="Wikipedia: 黒田喜夫",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="新川和江『睡り椅子』",
    name_en="Shinkawa Kazue's Nemuri Isu",
    name_original="睡り椅子",
    period_key="戦後期",
    definition="新川和江（1929-2024）が1953年に刊行した第一詩集。女性的感性と宇宙的広がりを結ぶ抒情詩で、戦後女性詩の方向性を示した、新川詩業の出発点。",
    background="新川の戦後女性詩運動と『地球』詩誌活動。",
    development="後の『新川和江全詩集』への基盤を成した。",
    historical_context="昭和28年の戦後女性詩黎明期。",
    primary_source_url=WIKI_JA+"%E6%96%B0%E5%B7%9D%E5%92%8C%E6%B1%9F",
    primary_source_type="Wikipedia: 新川和江",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="大江健三郎『個人的な体験』",
    name_en="Ōe Kenzaburō's Kojinteki na Taiken",
    name_original="個人的な体験",
    period_key="現代",
    definition="大江健三郎（1935-2023）が1964年に発表した長編小説。障害をもつ息子の誕生を契機とした青年の苦悩と再生を描き、新潮社文学賞受賞、大江の作家的転換点を画した代表作。",
    background="大江の長男光誕生（1963）と作家的世界観の転換。",
    development="続く『万延元年のフットボール』への大江文学展開を準備した。",
    historical_context="昭和39年の60年安保後の大江文学転換期。",
    primary_source_url=WIKI_JA+"%E5%80%8B%E4%BA%BA%E7%9A%84%E3%81%AA%E4%BD%93%E9%A8%93",
    primary_source_type="Wikipedia: 個人的な体験",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="大江健三郎『同時代ゲーム』",
    name_en="Ōe Kenzaburō's Dōjidai Game",
    name_original="同時代ゲーム",
    period_key="現代",
    definition="大江健三郎が1979年に発表した長編小説。四国の村=国家=小宇宙の神話的歴史を双子兄妹の手紙形式で語り、大江神話的小説の頂点を成した、メタフィクション的大作。",
    background="大江の四国故郷神話への関心とラテンアメリカ文学受容。",
    development="後の『M/Tと森のフシギの物語』『懐かしい年への手紙』への大江神話小説展開を準備した。",
    historical_context="昭和54年の大江神話的小説期。",
    primary_source_url=WIKI_JA+"%E5%90%8C%E6%99%82%E4%BB%A3%E3%82%B2%E3%83%BC%E3%83%A0",
    primary_source_type="Wikipedia: 同時代ゲーム",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="開高健『裸の王様』",
    name_en="Kaikō Takeshi's Hadaka no Ōsama",
    name_original="裸の王様",
    period_key="戦後期",
    definition="開高健（1930-1989）が1957年に発表した中編小説。商社マンが見た児童画教室の権威的歪みを描き、芥川賞受賞、第三の新人後の世代の代表作となった開高の出世作。",
    background="開高の寿屋（現サントリー）勤務体験と現代社会観察。",
    development="続く『日本三文オペラ』『輝ける闇』への開高文学展開を準備した。",
    historical_context="昭和32年の戦後派後の世代文学興隆期。",
    primary_source_url=WIKI_JA+"%E9%96%8B%E9%AB%98%E5%81%A5",
    primary_source_type="Wikipedia: 開高健",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="開高健『輝ける闇』",
    name_en="Kaikō Takeshi's Kagayakeru Yami",
    name_original="輝ける闇",
    period_key="現代",
    definition="開高健が1968年に発表した長編小説。ベトナム戦争従軍取材体験を素材に、戦争の不条理を哲学的に描き、毎日出版文化賞受賞、戦後ベトナム戦争文学の代表作となった。",
    background="開高のベトナム戦争従軍取材（1964-65）と戦争文学への展開。",
    development="続く『夏の闇』への開高戦争文学展開を準備した。",
    historical_context="昭和43年のベトナム戦争激化期。",
    primary_source_url=WIKI_JA+"%E8%BC%9D%E3%81%91%E3%82%8B%E9%97%87",
    primary_source_type="Wikipedia: 輝ける闇",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="安部公房『箱男』",
    name_en="Abe Kōbō's Hako Otoko",
    name_original="箱男",
    period_key="現代",
    definition="安部公房（1924-1993）が1973年に発表した長編小説。段ボール箱を被った匿名男の都市彷徨を描き、現代都市の匿名性と監視を予言的に追究した、安部実験文学の代表作。",
    background="安部の都市論と現代社会の監視・匿名性問題への関心。",
    development="後の『密会』『方舟さくら丸』への安部実験文学展開を準備した。",
    historical_context="昭和48年の都市消費社会化期。",
    primary_source_url=WIKI_JA+"%E7%AE%B1%E7%94%B7",
    primary_source_type="Wikipedia: 箱男",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"匿名身体の都市彷徨は、AI時代の匿名性と監視問題の予言的参照点。",
         "related_ai_phenomenon":"AI監視社会と匿名性"}])


# ============================================================
# F: 三島・倉橋・円地・田辺・河野・大庭・石牟礼・中上・水上（10件）
# ============================================================
add(**C, name_ja="三島由紀夫『仮面の告白』",
    name_en="Mishima Yukio's Kamen no Kokuhaku",
    name_original="仮面の告白",
    period_key="戦後期",
    definition="三島由紀夫（1925-1970）が1949年に発表した長編小説。同性愛的傾向と仮面性を私小説的に告白し、三島の作家的出発を画した、戦後派文学の代表作の一つ。",
    background="三島の戦後文学的出発と告白文学方法の更新。",
    development="続く『愛の渇き』『禁色』への三島告白文学展開を準備した。",
    historical_context="昭和24年の戦後派文学興隆期。",
    primary_source_url=WIKI_JA+"%E4%BB%AE%E9%9D%A2%E3%81%AE%E5%91%8A%E7%99%BD",
    primary_source_type="Wikipedia: 仮面の告白",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="三島由紀夫『憂国』",
    name_en="Mishima Yukio's Yūkoku",
    name_original="憂国",
    period_key="現代",
    definition="三島由紀夫が1961年に発表した短編小説。二・二六事件下の青年将校夫妻の自決を耽美的に描き、三島の天皇主義文学への展開を画した、戦後右翼文学の代表作。",
    background="三島の天皇主義への政治的傾倒と耽美的死の美学化。",
    development="後の『豊饒の海』四部作と三島自決（1970）の精神的予兆となった。",
    historical_context="昭和36年の三島政治化期。",
    primary_source_url=WIKI_JA+"%E6%86%82%E5%9B%BD_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 憂国",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="倉橋由美子『パルタイ』",
    name_en="Kurahashi Yumiko's Partei",
    name_original="パルタイ",
    period_key="現代",
    definition="倉橋由美子（1935-2005）が1960年に発表した中編小説。学生運動下の党組織と恋愛の不条理を寓意的方法で描き、明治大学学長賞・女流文学者賞受賞、倉橋文学の出発点となった。",
    background="60年安保期の学生運動と倉橋の前衛的方法的意識。",
    development="続く『聖少女』『夢の浮橋』への倉橋実験文学展開を準備した。",
    historical_context="昭和35年の60年安保学生運動期。",
    primary_source_url=WIKI_JA+"%E5%80%89%E6%A9%8B%E7%94%B1%E7%BE%8E%E5%AD%90",
    primary_source_type="Wikipedia: 倉橋由美子",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="円地文子『女坂』",
    name_en="Enchi Fumiko's Onnazaka",
    name_original="女坂",
    period_key="戦後期",
    definition="円地文子（1905-1986）が1957年に発表した長編小説。明治期高級官吏家の妻が夫の妾たちを管理する苦悩を描き、野間文芸賞受賞、戦後女性文学の代表作となった。",
    background="円地の母方祖母をモデルとした明治家族小説の構築。",
    development="後の『朱を奪うもの』への円地文学展開を準備した。",
    historical_context="昭和32年の戦後女性文学興隆期。",
    primary_source_url=WIKI_JA+"%E5%9C%93%E5%9C%B0%E6%96%87%E5%AD%90",
    primary_source_type="Wikipedia: 円地文子",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="田辺聖子『感傷旅行』",
    name_en="Tanabe Seiko's Kanshō Ryokō",
    name_original="感傷旅行",
    period_key="現代",
    definition="田辺聖子（1928-2019）が1964年に発表した中編小説。船場商家娘と中年男性の関西を舞台にした恋愛を描き、芥川賞受賞、田辺文学の出発点となった代表作。",
    background="田辺の大阪船場体験と関西女性文学の展開。",
    development="続く『姥ざかり』『新源氏物語』への田辺文学展開を準備した。",
    historical_context="昭和39年の高度成長期女性文学期。",
    primary_source_url=WIKI_JA+"%E7%94%B0%E8%BE%BA%E8%81%96%E5%AD%90",
    primary_source_type="Wikipedia: 田辺聖子",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="河野多恵子『幼児狩り』",
    name_en="Kōno Taeko's Yōji Gari",
    name_original="幼児狩り",
    period_key="現代",
    definition="河野多恵子（1926-2015）が1961年に発表した短編小説。サディズム的女性の幼児への倒錯的関心を描き、新潮社同人雑誌賞受賞、河野文学の出発点となった戦後女性倒錯文学の代表作。",
    background="河野の谷崎潤一郎研究と女性倒錯文学の方法的展開。",
    development="続く『蟹』『みいら採り猟奇譚』への河野文学展開を準備した。",
    historical_context="昭和36年の戦後女性倒錯文学興隆期。",
    primary_source_url=WIKI_JA+"%E6%B2%B3%E9%87%8E%E5%A4%9A%E6%83%A0%E5%AD%90",
    primary_source_type="Wikipedia: 河野多恵子",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="大庭みな子『三匹の蟹』",
    name_en="Ōba Minako's Sanbiki no Kani",
    name_original="三匹の蟹",
    period_key="現代",
    definition="大庭みな子（1930-2007）が1968年に発表した短編小説。アラスカ在住日本人妻の倦怠と性的彷徨を描き、芥川賞・群像新人賞同時受賞、戦後越境女性文学の代表作となった。",
    background="大庭のアラスカ在住体験と女性越境文学の展開。",
    development="続く『寂兮寥兮』『浦島草』への大庭文学展開を準備した。",
    historical_context="昭和43年の女性越境文学黎明期。",
    primary_source_url=WIKI_JA+"%E5%A4%A7%E5%BA%AD%E3%81%BF%E3%81%AA%E5%AD%90",
    primary_source_type="Wikipedia: 大庭みな子",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"越境女性経験",
         "description":"アラスカ在住日本人妻描写は人類学的越境女性経験の文学的記録。"}])

add(**C, name_ja="石牟礼道子『苦海浄土』",
    name_en="Ishimure Michiko's Kugai Jōdo",
    name_original="苦海浄土",
    period_key="現代",
    definition="石牟礼道子（1927-2018）が1969年に発表した長編記録文学。水俣病患者の苦悩と尊厳を魂のことばで記録し、大宅壮一ノンフィクション賞辞退で知られる、戦後ドキュメンタリー文学の最高峰。",
    background="水俣病問題と石牟礼の長年にわたる患者交流。",
    development="続く『神々の村』『天の魚』とともに苦海浄土三部作を成した。",
    historical_context="昭和44年の公害問題顕在化期。",
    primary_source_url=WIKI_JA+"%E8%8B%A6%E6%B5%B7%E6%B5%84%E5%9C%9F",
    primary_source_type="Wikipedia: 苦海浄土",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"公害と地域共同体崩壊",
         "description":"水俣病記録は人類学的公害-地域共同体崩壊研究の文学的並行物。"}])

add(**C, name_ja="中上健次『岬』",
    name_en="Nakagami Kenji's Misaki",
    name_original="岬",
    period_key="現代",
    definition="中上健次（1946-1992）が1976年に発表した中編小説。紀州被差別部落「路地」を舞台に肉体労働者青年の血族的世界を描き、芥川賞受賞、中上紀州サーガの出発点となった。",
    background="中上の被差別部落出自と紀州サーガ文学の方法的確立。",
    development="続く『枯木灘』『千年の愉楽』への中上紀州サーガ展開を準備した。",
    historical_context="昭和51年の戦後被差別文学興隆期。",
    primary_source_url=WIKI_JA+"%E5%B2%AC_(%E4%B8%AD%E4%B8%8A%E5%81%A5%E6%AC%A1)",
    primary_source_type="Wikipedia: 岬",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="中上健次『千年の愉楽』",
    name_en="Nakagami Kenji's Sennen no Yuraku",
    name_original="千年の愉楽",
    period_key="現代",
    definition="中上健次が1982年に発表した長編連作小説。紀州路地の中本一統の若者たちの生と死を産婆オリュウノオバの語りで描き、中上紀州神話的サーガの頂点を成した。",
    background="中上の紀州路地神話化と語りの方法的成熟。",
    development="続く『奇跡』『天の歌』への中上紀州神話小説展開を準備した。",
    historical_context="昭和57年の中上紀州神話小説期。",
    primary_source_url=WIKI_JA+"%E5%8D%83%E5%B9%B4%E3%81%AE%E6%84%89%E6%A5%BD",
    primary_source_type="Wikipedia: 千年の愉楽",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# G: 水上勉・川端晩年・井上靖・司馬・1980s前半（10件）
# ============================================================
add(**C, name_ja="水上勉『雁の寺』",
    name_en="Minakami Tsutomu's Gan no Tera",
    name_original="雁の寺",
    period_key="現代",
    definition="水上勉（1919-2004）が1961年に発表した中編小説。京都禅寺の小僧が住職を殺害する事件を描き、直木賞受賞、戦後社会派推理文学の代表作となった水上の出世作。",
    background="水上の禅寺小僧体験と戦後社会派推理文学の展開。",
    development="続く『五番町夕霧楼』『飢餓海峡』への水上文学展開を準備した。",
    historical_context="昭和36年の戦後社会派推理文学興隆期。",
    primary_source_url=WIKI_JA+"%E6%B0%B4%E4%B8%8A%E5%8B%89",
    primary_source_type="Wikipedia: 水上勉",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="水上勉『飢餓海峡』",
    name_en="Minakami Tsutomu's Kiga Kaikyō",
    name_original="飢餓海峡",
    period_key="現代",
    definition="水上勉が1962年に発表した長編小説。洞爺丸事故下の犯罪事件を素材に、貧困と犯罪・贖罪の人間ドラマを描き、戦後社会派推理文学の頂点を成した水上の代表作。",
    background="洞爺丸事故（1954）と戦後社会派推理文学の方法的展開。",
    development="戦後社会派推理文学の規範を成し、後の松本清張系譜と並ぶ位置を占めた。",
    historical_context="昭和37年の戦後社会派推理文学最盛期。",
    primary_source_url=WIKI_JA+"%E9%A3%A2%E9%A4%93%E6%B5%B7%E5%B3%A1",
    primary_source_type="Wikipedia: 飢餓海峡",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="川端康成『眠れる美女』",
    name_en="Kawabata Yasunari's Nemureru Bijo",
    name_original="眠れる美女",
    period_key="現代",
    definition="川端康成が1960-61年に発表した中編小説。老人が眠らされた裸の美女の隣で過ごす秘密の宿を描き、川端晩年の倒錯的耽美文学の代表作となった、毎日出版文化賞受賞作。",
    background="川端晩年の老年と性をめぐる倒錯的美学の追求。",
    development="ノーベル文学賞受賞（1968）への川端晩年期の代表作。",
    historical_context="昭和35-36年の川端晩年文学期。",
    primary_source_url=WIKI_JA+"%E7%9C%A0%E3%82%8C%E3%82%8B%E7%BE%8E%E5%A5%B3",
    primary_source_type="Wikipedia: 眠れる美女",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="川端康成『古都』",
    name_en="Kawabata Yasunari's Koto",
    name_original="古都",
    period_key="現代",
    definition="川端康成が1961-62年に発表した長編小説。京都を舞台に生き別れた双子姉妹の再会を四季の風物とともに描き、ノーベル文学賞選考対象作の一つとなった川端晩年の代表作。",
    background="川端の京都体験と古都美学の集大成的執筆。",
    development="ノーベル文学賞受賞（1968）の選考根拠の一つとなった。",
    historical_context="昭和36-37年の川端古都美学期。",
    primary_source_url=WIKI_JA+"%E5%8F%A4%E9%83%BD_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 古都",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="井上靖『天平の甍』",
    name_en="Inoue Yasushi's Tenpyō no Iraka",
    name_original="天平の甍",
    period_key="戦後期",
    definition="井上靖（1907-1991）が1957年に発表した長編歴史小説。鑑真和上の渡日を支えた留学僧普照らの困難な使命を描き、芸術選奨文部大臣賞受賞、井上歴史小説の代表作となった。",
    background="井上の中国・西域への関心と歴史小説方法の展開。",
    development="続く『敦煌』『楼蘭』への井上西域歴史小説展開を準備した。",
    historical_context="昭和32年の戦後歴史小説興隆期。",
    primary_source_url=WIKI_JA+"%E5%A4%A9%E5%B9%B3%E3%81%AE%E7%94%8D",
    primary_source_type="Wikipedia: 天平の甍",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="井上靖『敦煌』",
    name_en="Inoue Yasushi's Tonkō",
    name_original="敦煌",
    period_key="現代",
    definition="井上靖が1959年に発表した長編歴史小説。敦煌莫高窟経典埋蔵の謎を11世紀宋人趙行徳の物語に仮構し、毎日芸術賞受賞、井上西域歴史小説の代表作となった。",
    background="井上の長年にわたる西域研究と歴史小説の集大成。",
    development="戦後西域ブームの起点となり、ロケ映画化もされた。",
    historical_context="昭和34年の戦後西域ブーム期。",
    primary_source_url=WIKI_JA+"%E6%95%A6%E7%85%8C_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 敦煌",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="司馬遼太郎『竜馬がゆく』",
    name_en="Shiba Ryōtarō's Ryōma ga Yuku",
    name_original="竜馬がゆく",
    period_key="現代",
    definition="司馬遼太郎（1923-1996）が1962-66年に新聞連載した長編歴史小説。坂本竜馬の生涯を司馬史観で描き、竜馬人気を国民的に確立した、司馬歴史小説の代表作。",
    background="司馬の幕末研究と国民的歴史小説への展開。",
    development="国民的ベストセラーとなり、後の司馬歴史小説の規範を成した。",
    historical_context="昭和37-41年の戦後歴史小説国民化期。",
    primary_source_url=WIKI_JA+"%E7%AB%9C%E9%A6%AC%E3%81%8C%E3%82%86%E3%81%8F",
    primary_source_type="Wikipedia: 竜馬がゆく",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="司馬遼太郎『坂の上の雲』",
    name_en="Shiba Ryōtarō's Saka no Ue no Kumo",
    name_original="坂の上の雲",
    period_key="現代",
    definition="司馬遼太郎が1968-72年に新聞連載した長編歴史小説。日露戦争を秋山兄弟・正岡子規の生涯で描き、明治国家像を国民的記憶として定着させた、司馬国民文学の頂点。",
    background="司馬の明治国家論と日露戦争研究の集大成。",
    development="国民的ベストセラーとなり、平成期のNHKドラマ化で再評価された。",
    historical_context="昭和43-47年の高度成長期国民文学期。",
    primary_source_url=WIKI_JA+"%E5%9D%82%E3%81%AE%E4%B8%8A%E3%81%AE%E9%9B%B2",
    primary_source_type="Wikipedia: 坂の上の雲",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"国民国家形成と歴史記憶",
         "description":"司馬国民文学は人類学的国民国家形成と集合記憶構築の文学的事例。"}])

add(**C, name_ja="高橋源一郎『さようなら、ギャングたち』",
    name_en="Takahashi Gen'ichirō's Sayōnara Gangs",
    name_original="さようなら、ギャングたち",
    period_key="現代",
    definition="高橋源一郎（1951-）が1981年に発表した長編小説。ポストモダン的引用と虚構性で詩人と娘の物語を描き、群像新人長編小説賞優秀作、80年代日本ポストモダン文学の出発点となった。",
    background="高橋の60年代学生運動挫折とポストモダン文学的展開。",
    development="80年代ポストモダン文学の代表作として位置づけられた。",
    historical_context="昭和56年の80年代ポストモダン文学黎明期。",
    primary_source_url=WIKI_JA+"%E3%81%95%E3%82%88%E3%81%86%E3%81%AA%E3%82%89%E3%80%81%E3%82%AE%E3%83%A3%E3%83%B3%E3%82%B0%E3%81%9F%E3%81%A1",
    primary_source_type="Wikipedia: さようなら、ギャングたち",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="田中康夫『なんとなく、クリスタル』",
    name_en="Tanaka Yasuo's Nantonaku Crystal",
    name_original="なんとなく、クリスタル",
    period_key="現代",
    definition="田中康夫（1956-）が1980年に発表した中編小説。ブランド名注釈付きで青山女子大生の消費生活を描き、文藝賞受賞、80年代消費社会文学の起点となった話題作。",
    background="80年代消費社会化と若者ブランド意識の文学的捕捉。",
    development="80年代消費社会文学の象徴的作品として位置づけられた。",
    historical_context="昭和55年の80年代消費社会文学黎明期。",
    primary_source_url=WIKI_JA+"%E3%81%AA%E3%82%93%E3%81%A8%E3%81%AA%E3%81%8F%E3%80%81%E3%82%AF%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%AB",
    primary_source_type="Wikipedia: なんとなく、クリスタル",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H: 1980s後半-2010s（10件）
# ============================================================
add(**C, name_ja="山田詠美『ベッドタイムアイズ』",
    name_en="Yamada Eimi's Bedtime Eyes",
    name_original="ベッドタイムアイズ",
    period_key="現代",
    definition="山田詠美（1959-）が1985年に発表した中編小説。日本人女性と黒人米兵の性愛を率直に描き、文藝賞受賞、80年代女性身体文学の代表作となった山田の出世作。",
    background="80年代女性主体性表現の興隆と山田の越境的方法。",
    development="続く『ジェシーの背骨』『放課後の音符』への山田文学展開を準備した。",
    historical_context="昭和60年の80年代女性文学興隆期。",
    primary_source_url=WIKI_JA+"%E5%B1%B1%E7%94%B0%E8%A9%A0%E7%BE%8E",
    primary_source_type="Wikipedia: 山田詠美",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="古井由吉『杳子』",
    name_en="Furui Yoshikichi's Yōko",
    name_original="杳子",
    period_key="現代",
    definition="古井由吉（1937-2020）が1971年に発表した中編小説。山中で出会った精神的危機の女性との関係を内的言語で描き、芥川賞受賞、内向の世代文学の代表作となった古井の出世作。",
    background="古井のドイツ文学者出自と内向的言語実験。",
    development="内向の世代文学の頂点を成し、後の古井文学の方向性を定めた。",
    historical_context="昭和46年の内向の世代文学頂点期。",
    primary_source_url=WIKI_JA+"%E5%8F%A4%E4%BA%95%E7%94%B1%E5%90%89",
    primary_source_type="Wikipedia: 古井由吉",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"内的言語の精緻な追求は、AI時代の言語精度問題の歴史的参照点。",
         "related_ai_phenomenon":"AI言語精度の歴史性"}])

add(**C, name_ja="後藤明生『挟み撃ち』",
    name_en="Gotō Meisei's Hasamiuchi",
    name_original="挟み撃ち",
    period_key="現代",
    definition="後藤明生（1932-1999）が1973年に発表した長編小説。ゴーゴリ『外套』を引用しつつ満州引揚げ記憶を反復的に語り、内向の世代文学の代表作となった後藤の代表作。",
    background="後藤の満州引揚げ体験とゴーゴリ研究的手法。",
    development="内向の世代文学の代表作として位置づけられた。",
    historical_context="昭和48年の内向の世代文学期。",
    primary_source_url=WIKI_JA+"%E5%BE%8C%E8%97%A4%E6%98%8E%E7%94%9F",
    primary_source_type="Wikipedia: 後藤明生",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="阿部和重『シンセミア』",
    name_en="Abe Kazushige's Sin Semillas",
    name_original="シンセミア",
    period_key="現代",
    definition="阿部和重（1968-）が2003年に発表した長編小説。山形県神町を舞台に、警察腐敗・盗撮・暴力を多視点的に描き、毎日出版文化賞受賞、阿部和重神町サーガの中核を成した大作。",
    background="阿部の山形神町出自と多視点的暴力描写の方法的展開。",
    development="続く『ピストルズ』とともに神町サーガを成した。",
    historical_context="平成15年のゼロ年代純文学期。",
    primary_source_url=WIKI_JA+"%E3%82%B7%E3%83%B3%E3%82%BB%E3%83%9F%E3%82%A2",
    primary_source_type="Wikipedia: シンセミア",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="保坂和志『プレーンソング』",
    name_en="Hosaka Kazushi's Plainsong",
    name_original="プレーンソング",
    period_key="現代",
    definition="保坂和志（1956-）が1990年に発表した長編小説。猫と若者たちの何でもない日常を反プロット的に描き、保坂日常美学文学の出発点となった、ゼロ年代日常系小説の祖型。",
    background="保坂の小説論的方法的意識と日常美学の追求。",
    development="続く『季節の記憶』『カンバセーション・ピース』への保坂文学展開を準備した。",
    historical_context="平成2年のポストモダン後の日常系文学黎明期。",
    primary_source_url=WIKI_JA+"%E4%BF%9D%E5%9D%82%E5%92%8C%E5%BF%97",
    primary_source_type="Wikipedia: 保坂和志",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="平野啓一郎『マチネの終わりに』",
    name_en="Hirano Keiichirō's Matinée no Owari ni",
    name_original="マチネの終わりに",
    period_key="現代",
    definition="平野啓一郎（1975-）が2016年に発表した長編小説。ギタリストとジャーナリスト女性の遠距離恋愛をクラシカルな筆致で描き、渡辺淳一文学賞受賞、平成末期ベストセラーとなった。",
    background="平野の分人主義論と恋愛小説的洗練。",
    development="平成末期純文学的恋愛小説の代表作として位置づけられた。",
    historical_context="平成28年の平成末期文学期。",
    primary_source_url=WIKI_JA+"%E3%83%9E%E3%83%81%E3%83%8D%E3%81%AE%E7%B5%82%E3%82%8F%E3%82%8A%E3%81%AB",
    primary_source_type="Wikipedia: マチネの終わりに",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="川上弘美『センセイの鞄』",
    name_en="Kawakami Hiromi's Sensei no Kaban",
    name_original="センセイの鞄",
    period_key="現代",
    definition="川上弘美（1958-）が2001年に発表した長編小説。中年女性ツキコと高校時代の国語教師との淡い恋を散文詩的に描き、谷崎潤一郎賞受賞、平成女性文学の代表作となった。",
    background="川上のミニマルな散文詩的方法と中高年恋愛文学の展開。",
    development="平成女性文学の代表作として位置づけられた。",
    historical_context="平成13年の平成女性文学成熟期。",
    primary_source_url=WIKI_JA+"%E3%82%BB%E3%83%B3%E3%82%BB%E3%82%A4%E3%81%AE%E9%9E%84",
    primary_source_type="Wikipedia: センセイの鞄",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="多和田葉子『犬婿入り』",
    name_en="Tawada Yōko's Inu Mukoiri",
    name_original="犬婿入り",
    period_key="現代",
    definition="多和田葉子（1960-）が1993年に発表した中編小説。多摩地区の塾教師と犬男との越境的婚姻を昔話的方法で描き、芥川賞受賞、多和田越境文学の出発点となった。",
    background="多和田のドイツ在住越境作家としての活動と昔話変容。",
    development="多和田越境文学の代表作として位置づけられた。",
    historical_context="平成5年の越境文学興隆期。",
    primary_source_url=WIKI_JA+"%E7%8A%AC%E5%A9%BF%E5%85%A5%E3%82%8A",
    primary_source_type="Wikipedia: 犬婿入り",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"越境的婚姻と人間-動物関係",
         "description":"犬男婚姻譚は人類学的人間-動物境界の文学的探究事例。"}])

add(**C, name_ja="多和田葉子『献灯使』",
    name_en="Tawada Yōko's Kentōshi",
    name_original="献灯使",
    period_key="現代",
    definition="多和田葉子が2014年に発表した長編小説。原発事故後の鎖国日本における老人と虚弱化した子の関係を寓意的に描き、全米図書賞受賞、ポスト3.11文学の代表作となった。",
    background="多和田のドイツ在住作家としての3.11後日本観察と寓意的方法。",
    development="ポスト3.11文学の代表作として国際的にも翻訳された。",
    historical_context="平成26年のポスト3.11文学期。",
    primary_source_url=WIKI_JA+"%E7%8C%AE%E7%81%AF%E4%BD%BF",
    primary_source_type="Wikipedia: 献灯使",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ポスト3.11寓意的身体描写は、AI時代の身体性問題の歴史的参照点。",
         "related_ai_phenomenon":"AI時代の身体性表現"}])

add(**C, name_ja="角田光代『八日目の蝉』",
    name_en="Kakuta Mitsuyo's Yōkame no Semi",
    name_original="八日目の蝉",
    period_key="現代",
    definition="角田光代（1967-）が2007年に発表した長編小説。略取した他人の子と暮らした女と、その子の成人後の物語を描き、中央公論文芸賞受賞、平成女性文学の代表作となった。",
    background="角田の女性人生模索小説の方法的成熟。",
    development="映画化・テレビドラマ化され、平成末期国民的小説となった。",
    historical_context="平成19年の平成女性文学頂点期。",
    primary_source_url=WIKI_JA+"%E5%85%AB%E6%97%A5%E7%9B%AE%E3%81%AE%E8%9D%89",
    primary_source_type="Wikipedia: 八日目の蝉",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Cross-domain bridges (additional, ensure >= 14)
# ============================================================
def attach_cross(name, target_db, link_type, target_name, desc):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("cross_domain", []).append(
                {"target_db": target_db, "link_type": link_type,
                 "target_entity_name": target_name, "description": desc})
            return

attach_cross("火野葦平『麦と兵隊』", "AN", "shared_concept",
             "戦時従軍報道と兵卒主体",
             "従軍兵卒視点の報道文学は人類学的戦時下兵士主体研究の文学的並行物。")
attach_cross("石川達三『生きてゐる兵隊』", "MG", "shared_concept",
             "報道規制と表現自由",
             "戦時下発禁事件は経営学的メディア組織と検閲経済の歴史的事例。")
attach_cross("高見順『敗戦日記』", "AN", "shared_concept",
             "敗戦期社会記録",
             "敗戦期日記は人類学的危機期社会記録の典型例。")
attach_cross("中島敦『山月記』", "PHIL", "shared_concept",
             "自意識と人格変容の哲学",
             "李徴自意識描写は哲学的人格同一性問題の文学的並行物。")
attach_cross("野間宏『青年の環』", "AN", "shared_concept",
             "被差別部落と社会構造",
             "被差別部落全体小説は人類学的社会階層研究の文学的並行物。")
attach_cross("大岡昇平『野火』", "PHIL", "shared_concept",
             "極限倫理と道徳哲学",
             "食人題材小説は道徳哲学的極限倫理問題の文学的探究事例。")
attach_cross("武田泰淳『ひかりごけ』", "PHIL", "shared_concept",
             "実存主義倫理",
             "極限状況裁判劇は実存主義倫理学の文学的並行物。")
attach_cross("遠藤周作『海と毒薬』", "PHIL", "shared_concept",
             "罪意識と神なき倫理",
             "生体解剖事件文学化は宗教哲学的罪概念の文学的探究事例。")
attach_cross("大江健三郎『個人的な体験』", "AN", "shared_concept",
             "障害と家族再生",
             "障害児誕生体験文学化は人類学的障害-家族研究の文学的並行物。")
attach_cross("安部公房『箱男』", "MG", "shared_concept",
             "都市監視と匿名身体",
             "段ボール箱男描写は都市経営学的監視-匿名性問題の文学的予言。")
attach_cross("中上健次『岬』", "AN", "shared_concept",
             "被差別部落と血族世界",
             "紀州路地サーガは人類学的被差別部落血族構造の文学的並行物。")
attach_cross("水上勉『飢餓海峡』", "MG", "shared_concept",
             "戦後社会階層と犯罪経済",
             "貧困犯罪小説は経営学的社会経済病理の文学的並行物。")
attach_cross("司馬遼太郎『竜馬がゆく』", "PHIL", "shared_concept",
             "歴史哲学と国民主体",
             "司馬国民歴史小説は歴史哲学的国民主体形成の文学的事例。")
attach_cross("田中康夫『なんとなく、クリスタル』", "MG", "shared_concept",
             "消費社会とブランド経済",
             "ブランド注釈小説は経営学的消費社会-ブランド戦略の文学的鏡像。")
attach_cross("山田詠美『ベッドタイムアイズ』", "AN", "shared_concept",
             "越境的身体と人種",
             "日米越境性愛描写は人類学的人種-身体研究の文学的並行物。")
attach_cross("阿部和重『シンセミア』", "AN", "shared_concept",
             "地方社会の暴力構造",
             "神町サーガは人類学的地方共同体暴力構造の文学的探究事例。")
attach_cross("角田光代『八日目の蝉』", "AN", "shared_concept",
             "母性の社会的構築",
             "略取育児小説は人類学的母性社会的構築論の文学的並行物。")


# ============================================================
# fourth_transform additional tags
# ============================================================
def attach_fourth(name, axis, status, rationale, ai_phen):
    for c in CONCEPTS:
        if c["name_ja"] == name:
            c.setdefault("fourth_axes", []).append(
                {"axis": axis, "status": status,
                 "rationale": rationale, "related_ai_phenomenon": ai_phen})
            return

attach_fourth("火野葦平『麦と兵隊』", "作者性", "rethinking",
              "戦時従軍作家の作者性は、AI生成プロパガンダ問題の歴史的参照点。",
              "AI生成プロパガンダの作者性")
attach_fourth("中島敦『李陵』", "言語", "rethinking",
              "漢文調歴史小説は、AI多文体生成の歴史的参照点。",
              "AI多言語多文体生成")
attach_fourth("内田百閒『東京焼盡』", "言語", "rethinking",
              "戦災記録の淡々とした筆致は、AI記録文体生成の歴史的参照点。",
              "AI戦災記録生成")
attach_fourth("野間宏『真空地帯』", "創造性", "rethinking",
              "全体小説方法は、AI長文生成の構造的参照点となる。",
              "AI全体小説生成")
attach_fourth("大岡昇平『レイテ戦記』", "作者性", "rethinking",
              "戦記文学の事実-虚構境界は、AI生成戦記の真正性問題の歴史的参照点。",
              "AI生成戦記の真正性")
attach_fourth("武田泰淳『司馬遷』", "作者性", "rethinking",
              "歴史思考の文学化は、AI歴史テクスト生成の主体性問題の歴史的源流。",
              "AI歴史テクスト生成")
attach_fourth("梅崎春生『桜島』", "主体", "rethinking",
              "暗号兵主体描写は、AI時代の専門職主体表象の歴史的参照点。",
              "AI専門職主体表象")
attach_fourth("椎名麟三『深夜の酒宴』", "主体", "rethinking",
              "戦後実存的虚無主体は、AI時代の虚無主体問題の歴史的参照点。",
              "AI虚無主体表現")
attach_fourth("吉行淳之介『驟雨』", "主体", "rethinking",
              "心理小説的女性表象は、AI時代の女性表象問題の歴史的参照点。",
              "AI時代の女性表象")
attach_fourth("遠藤周作『深い河』", "主体", "rethinking",
              "宗教多元主義的主体は、AI時代の信仰主体問題の歴史的参照点。",
              "AI時代の信仰多元性")
attach_fourth("吉野弘『I was born』", "言語", "rethinking",
              "受動形からの存在論的着想は、AI言語意識化の歴史的参照点。",
              "AI言語の存在論的反省")
attach_fourth("大江健三郎『同時代ゲーム』", "創造性", "rethinking",
              "神話的メタフィクションは、AI時代の物語生成の構造的参照点。",
              "AI神話的物語生成")
attach_fourth("三島由紀夫『仮面の告白』", "主体", "rethinking",
              "仮面性告白は、AI時代の主体仮面性問題の歴史的参照点。",
              "AI時代の主体仮面性")
attach_fourth("三島由紀夫『憂国』", "倫理", "rethinking",
              "耽美的死の美学化は、AI時代の死表象倫理の歴史的参照点。",
              "AI時代の死表象倫理")
attach_fourth("倉橋由美子『パルタイ』", "創造性", "rethinking",
              "学生運動寓意小説は、AI時代の政治寓意生成の歴史的参照点。",
              "AI政治寓意生成")
attach_fourth("円地文子『女坂』", "主体", "rethinking",
              "明治家族妻主体は、AI時代の歴史的女性主体表象の参照点。",
              "AI歴史的女性主体表象")
attach_fourth("河野多恵子『幼児狩り』", "倫理", "rethinking",
              "倒錯的女性主体描写は、AI時代の倒錯表象倫理の歴史的参照点。",
              "AI倒錯表象倫理")
attach_fourth("大庭みな子『三匹の蟹』", "主体", "rethinking",
              "越境女性主体は、AI時代の越境主体表象の歴史的参照点。",
              "AI越境主体表象")
attach_fourth("石牟礼道子『苦海浄土』", "言語", "rethinking",
              "魂のことば記録は、AI時代の声の記録倫理の歴史的参照点。",
              "AI声の記録倫理")
attach_fourth("中上健次『千年の愉楽』", "創造性", "rethinking",
              "紀州神話的サーガは、AI時代の地域神話生成の歴史的参照点。",
              "AI地域神話生成")
attach_fourth("川端康成『眠れる美女』", "倫理", "rethinking",
              "倒錯的耽美文学は、AI時代の倒錯表象倫理の歴史的参照点。",
              "AI倒錯耽美生成")
attach_fourth("司馬遼太郎『坂の上の雲』", "作者性", "rethinking",
              "国民的歴史小説の作者権威は、AI生成歴史叙述の権威問題の歴史的参照点。",
              "AI歴史叙述の権威性")
attach_fourth("高橋源一郎『さようなら、ギャングたち』", "創造性", "rethinking",
              "ポストモダン引用小説は、AI生成的引用問題の歴史的参照点。",
              "AI引用-創造性問題")
attach_fourth("古井由吉『杳子』", "主体", "rethinking",
              "精神的危機女性描写は、AI時代の精神病理表象問題の歴史的参照点。",
              "AI精神病理表象")
attach_fourth("阿部和重『シンセミア』", "創造性", "rethinking",
              "多視点暴力小説は、AI時代の暴力表象問題の歴史的参照点。",
              "AI暴力表象")
attach_fourth("平野啓一郎『マチネの終わりに』", "主体", "rethinking",
              "分人主義的主体描写は、AI時代の分散主体問題の歴史的参照点。",
              "AI時代の分散主体性")
attach_fourth("川上弘美『センセイの鞄』", "主体", "rethinking",
              "中年女性主体描写は、AI時代の中高年主体表象の歴史的参照点。",
              "AI中高年主体表象")
attach_fourth("多和田葉子『犬婿入り』", "言語", "rethinking",
              "越境作家の昔話変容は、AI多言語生成の歴史的参照点。",
              "AI多言語越境生成")


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="日本",
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
                    print(f"  [warn] fourth tag {entry['name_ja']}: {e}")
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
                    print(f"  [warn] cross_domain {entry['name_ja']}: {e}")

        summary = db.progress_summary()
        print(f"[wave21 c18 add80] inserted: {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave21 c18 add80] fourth +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
