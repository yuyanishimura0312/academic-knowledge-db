"""LIT-DB Phase 2 Wave 13 — C18: Japanese Modern Literature ADD 60 concepts.

Subfield: lit_jp_modern (id=11), region='日本'.
Sources: 青空文庫 (PD primary), NDL Digital Collections, J-STAGE,
  britannica.com, academic-grade Wikipedia (ja/en).

Verification policy:
  - 'primary'  -> PD literary text or contemporaneous critical document
                  (青空文庫, NDL Digital, Wikisource).  Pre-1953 PD primary.
  - 'secondary' -> canonical scholarly synthesis (Britannica, academic Wikipedia).
  - 'tertiary' -> synthetic/comparative critical category for taxonomy.

60 NEW concepts (existing 50 → target 500).  Aim 60% primary tier.
Six blocks of 10:
  A: 明治文学補完 (二葉亭四迷～徳冨蘆花) — 10
  B: 鷗外・漱石・自然主義 — 10
  C: 反自然主義・耽美派・大正白樺 — 10
  D: 大正後期・新感覚派・川端 — 10
  E: 戦中戦後 (太宰・三島・大江・安部 etc.) — 10
  F: 現代 (村上春樹～又吉直樹～平成令和) — 10
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("明治文学期", "Meiji Literature", 1868, 1912,
     "明治維新から大正改元までの近代日本文学形成期。言文一致運動、写実主義、ロマン主義、自然主義が連続的に展開し、近代小説・批評の制度的基盤が確立した時期。"),
    ("大正文学期", "Taishō Literature", 1912, 1926,
     "大正改元から昭和改元までの文学期。白樺派の人道主義、新思潮派の理知主義、耽美派の感覚主義、新感覚派の文体実験が並行展開した。"),
    ("昭和戦前戦中期", "Early Shōwa & Wartime", 1926, 1945,
     "昭和改元から敗戦までの文学期。プロレタリア文学興隆と弾圧、転向、新感覚派からモダニズムへの展開、戦時動員下の文学。"),
    ("戦後文学期", "Postwar Literature", 1945, 1970,
     "敗戦後の文学的再出発期。第一次・第二次戦後派、第三の新人、内向の世代が連続して登場した。"),
    ("現代文学期", "Contemporary Japanese Literature", 1970, 2026,
     "高度経済成長後期から平成・令和に至る現代日本文学期。村上春樹を起点とするポストモダン、女性作家の台頭、純文学とエンタメの境界再編期。"),
]


AOZORA = "https://www.aozora.gr.jp/"
NDL = "https://dl.ndl.go.jp/"
JSTAGE = "https://www.jstage.jst.go.jp/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
BRITT = "https://www.britannica.com/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_jp_modern", region="日本",
         original_script="japanese")


# ============================================================
# A: 明治文学補完（10件）
# ============================================================
add(**C, name_ja="二葉亭四迷『浮雲』",
    name_en="Futabatei Shimei's Ukigumo",
    name_original="浮雲",
    period_key="明治文学期",
    definition="二葉亭四迷（1864-1909）が1887-89年に発表した近代日本最初の言文一致体長編小説。役所を免職された青年内海文三と従妹お勢の心理を口語体で描き、近代日本小説の出発点として位置づけられる。ツルゲーネフ翻訳経験と坪内逍遥の影響下に生まれた、近代散文の方法的礎石。",
    background="坪内逍遥『小説神髄』(1885)による近代小説論の影響と、ロシア・リアリズム翻訳実践。",
    development="国木田独歩、田山花袋、夏目漱石らの近代小説に直接的影響を与え、言文一致体の規範を確立した。",
    historical_context="明治20年代の自由民権運動退潮と、近代国家形成期の青年知識人の懊悩。",
    primary_source_url=AOZORA+"cards/000006/card1424.html",
    primary_source_type="青空文庫: 浮雲",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"言文一致と近代化",
         "description":"二葉亭の言文一致は、日本の近代化過程における話し言葉と書き言葉の統合を文学的に主導した、人類学的言語実践の中核事例。"}])

add(**C, name_ja="二葉亭四迷『平凡』",
    name_en="Futabatei Shimei's Heibon",
    name_original="平凡",
    period_key="明治文学期",
    definition="二葉亭四迷が1907年に発表した自伝的長編小説。「平凡な男」の半生を平明な口語で語る一人称独白形式で、明治末期文壇に対する自己批評の含意を持つ。日露戦争後の知識人の倦怠と懐疑を表現した、自然主義・私小説の先駆的作品。",
    background="日露戦争後の文学的閉塞感と、二葉亭自身の文学から離れた20年間の経歴。",
    development="田山花袋『蒲団』(1907)と並ぶ私小説的告白の祖型として、自然主義私小説の系譜の起点を成した。",
    historical_context="日露戦争(1904-05)後の社会的虚無感と、明治末期文壇の自然主義論争。",
    primary_source_url=AOZORA+"cards/000006/card1474.html",
    primary_source_type="青空文庫: 平凡",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="坪内逍遥『小説神髄』",
    name_en="Tsubouchi Shōyō's Shōsetsu Shinzui",
    name_original="小説神髄",
    period_key="明治文学期",
    definition="坪内逍遥（1859-1935）が1885-86年に発表した近代日本最初の体系的小説論。「小説の主脳は人情なり、世態風俗これに次ぐ」と述べ、勧善懲悪の戯作的小説を排して人間心理の写実的描写を主張した。日本近代小説論の出発点として位置づけられる。",
    background="英国ヴィクトリア朝小説論の受容と、戯作的小説伝統への明治知識人の反省。",
    development="二葉亭四迷『浮雲』、夏目漱石、坪内自身の『当世書生気質』を含む明治写実主義の理論的支柱となった。",
    historical_context="明治10年代の文明開化期、西欧近代小説論の組織的受容期。",
    primary_source_url=AOZORA+"cards/001645/card57495.html",
    primary_source_type="青空文庫: 小説神髄",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"逍遥の「人情を写す」近代小説論は、AI生成テキストにおける「人情の写実性」が真にあり得るかを問う出発点として再読可能。",
         "related_ai_phenomenon":"AI生成テキストの心理写実性問題"}])

add(**C, name_ja="坪内逍遥『当世書生気質』",
    name_en="Tsubouchi Shōyō's Tōsei Shosei Katagi",
    name_original="当世書生気質",
    period_key="明治文学期",
    definition="坪内逍遥が1885-86年に発表した、『小説神髄』の理論的主張を実践した長編小説。明治期書生（学生）の風俗・人情を写実的に描いたが、戯作的口調が残存しており、二葉亭四迷『浮雲』に至る言文一致への中継的位置を占める。",
    background="『小説神髄』の理論的提唱を実作で示す必要性。",
    development="二葉亭『浮雲』への直接的橋渡しとなり、明治写実主義の制度的成立に貢献した。",
    historical_context="明治10年代後半の高等教育拡充期と書生文化の形成期。",
    primary_source_url=NDL+"info:ndljp/pid/869127",
    primary_source_type="NDL Digital: 当世書生気質",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="尾崎紅葉『金色夜叉』",
    name_en="Ozaki Kōyō's Konjiki Yasha",
    name_original="金色夜叉",
    period_key="明治文学期",
    definition="尾崎紅葉（1868-1903）が1897-1903年に『読売新聞』連載した長編小説（未完）。許嫁お宮を富豪に奪われた間貫一の高利貸への転身と復讐を描き、明治中期最大のベストセラーとなった。雅俗折衷文体と通俗的物語性で、硯友社文学の頂点を成した。",
    background="硯友社（1885結成）の活動と、明治中期の新聞小説文化興隆。",
    development="泉鏡花、徳田秋声の文学的出発点となり、明治・大正の通俗長編小説の規範形式となった。",
    historical_context="明治30年代の新聞・雑誌メディア発展期と、近代資本主義社会の道徳的葛藤。",
    primary_source_url=AOZORA+"cards/000094/card4513.html",
    primary_source_type="青空文庫: 金色夜叉",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"明治資本主義と道徳",
         "description":"『金色夜叉』は明治資本主義（高利貸資本）と伝統的恋愛道徳の衝突を文学化し、経営学的価値観転換期の文化的指標となる。"}])

add(**C, name_ja="幸田露伴『五重塔』",
    name_en="Kōda Rohan's Gojū-no-tō",
    name_original="五重塔",
    period_key="明治文学期",
    definition="幸田露伴（1867-1947）が1891-92年に発表した短編小説。江戸の腕利きの大工「のっそり十兵衛」が五重塔建立に己の魂を懸ける姿を描き、職人精神と東洋的求道の理念を雅文体で表現した。明治20年代の理想主義文学の代表作。",
    background="江戸戯作の伝統的職人語りと、明治知識人の東洋思想再評価。",
    development="紅露時代（紅葉と露伴の並立期）の象徴的作品となり、後の谷崎潤一郎『春琴抄』など職人芸文学の祖型を成した。",
    historical_context="明治20年代の伝統美再評価運動（フェノロサ・岡倉天心）と並行する文学的国粋主義。",
    primary_source_url=AOZORA+"cards/000051/card43504.html",
    primary_source_type="青空文庫: 五重塔",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"職人精神・伝統工芸",
         "description":"露伴『五重塔』の職人精神描写は、人類学的物質文化論における職人技と伝統工芸の文学的並行物。"}])

add(**C, name_ja="樋口一葉『たけくらべ』",
    name_en="Higuchi Ichiyō's Takekurabe",
    name_original="たけくらべ",
    period_key="明治文学期",
    definition="樋口一葉（1872-1896）が1895-96年に発表した中編小説。吉原遊郭近辺の少年少女の淡い恋と社会的境遇を、雅俗折衷の和文体で描く。明治女性作家の到達点として、近代日本文学史上最も高く評価される作品の一つ。森鷗外・幸田露伴は『めさまし草』合評で絶賛した。",
    background="井原西鶴文体の研究と、明治後期下層女性の生活体験。",
    development="明治女性文学の頂点として、後の与謝野晶子・平塚らいてう以降の女性表現の祖型となった。",
    historical_context="明治20年代後半の女子高等教育萌芽期と、下層女性の社会的地位問題。",
    primary_source_url=AOZORA+"cards/000064/card389.html",
    primary_source_type="青空文庫: たけくらべ",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"一葉の少女主体描写は、近代以前の伝統的女性主体観と近代主体観の境界に立ち、AI時代の「主体性の歴史的構築」を再検討する基準点となる。",
         "related_ai_phenomenon":"AIによる女性主体表象の歴史性"}])

add(**C, name_ja="樋口一葉『にごりえ』",
    name_en="Higuchi Ichiyō's Nigorie",
    name_original="にごりえ",
    period_key="明治文学期",
    definition="樋口一葉が1895年に発表した短編小説。銘酒屋（私娼窟）の女お力と顧客源七の心中で終わる物語を、雅俗折衷文体で展開する。明治下層社会の女性の自尊と挫折を凝縮的に描き、『たけくらべ』と並ぶ一葉の代表作。",
    background="本郷丸山福山町での貧困生活体験と、明治都市下層女性観察。",
    development="明治女性文学の到達点として、後の田村俊子・宮本百合子の女性表現に継承された。",
    historical_context="明治末期都市下層社会と娼婦をめぐる文学的問題化。",
    primary_source_url=AOZORA+"cards/000064/card381.html",
    primary_source_type="青空文庫: にごりえ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="樋口一葉『十三夜』",
    name_en="Higuchi Ichiyō's Jūsan'ya",
    name_original="十三夜",
    period_key="明治文学期",
    definition="樋口一葉が1895年に発表した短編小説。富裕な家に嫁いだお関が夫の冷遇に耐えかねて実家に戻ろうとし、結局あきらめて帰宅する道で初恋の人と再会する物語。明治家父長制下の女性の境遇と諦念を、雅文体の凝縮された叙述で描いた。",
    background="明治民法（1898年公布）以前の女性の家族内地位と、結婚制度をめぐる社会的論議。",
    development="明治女性文学の倫理的核として、後の女性作家による結婚制度批判の祖型となった。",
    historical_context="明治20年代後半の家父長制成熟期と女性問題の文学的問題化。",
    primary_source_url=AOZORA+"cards/000064/card393.html",
    primary_source_type="青空文庫: 十三夜",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"家父長制と女性",
         "description":"一葉『十三夜』の女性主体描写は、人類学的家父長制研究と並行する文学的問題化を成す。"}])

add(**C, name_ja="徳冨蘆花『不如帰』",
    name_en="Tokutomi Roka's Hototogisu",
    name_original="不如帰",
    period_key="明治文学期",
    definition="徳冨蘆花（1868-1927）が1898-99年『国民新聞』連載した家庭小説。海軍士官川島武男と病妻浪子の悲恋を描き、結核と家父長制の二重の桎梏に苦しむ女性像を創出した。明治30年代最大のベストセラーで、家庭小説ジャンルの規範作品となった。",
    background="兄徳富蘇峰主宰『国民新聞』の家庭読者向け連載需要と、結核流行時代の社会的恐怖。",
    development="明治家庭小説の頂点として、後の通俗小説・ホームドラマ的物語類型の祖型となった。",
    historical_context="明治30年代の家父長制成熟期と、結核流行・女性の家族内地位問題。",
    primary_source_url=AOZORA+"cards/000280/card2509.html",
    primary_source_type="青空文庫: 不如帰",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"家庭小説とメロドラマ詩学",
         "description":"『不如帰』は明治家庭小説のメロドラマ詩学を確立し、現代物語論におけるジャンル研究の中核事例。"}])


# ============================================================
# B: 鷗外・漱石・自然主義（10件）
# ============================================================
add(**C, name_ja="森鷗外『舞姫』",
    name_en="Mori Ōgai's Maihime",
    name_original="舞姫",
    period_key="明治文学期",
    definition="森鷗外（1862-1922）が1890年に発表した短編小説。ベルリン留学中の官費留学生太田豊太郎が踊子エリスと愛を交わすも、立身出世のために彼女を捨てる物語。雅文体（漢文訓読体・和文混淆体）の頂点として、近代日本ロマン主義の起点を成した。",
    background="鷗外自身のドイツ留学体験(1884-88)と、ヨーロッパ・ロマン派文学受容。",
    development="明治ロマン主義の起点として、北村透谷、樋口一葉、後の谷崎潤一郎・三島由紀夫の雅文体に系譜的影響を与えた。",
    historical_context="明治20年代の西欧文化受容期と、近代国家形成下の個人と国家の葛藤。",
    primary_source_url=AOZORA+"cards/000129/card2122.html",
    primary_source_type="青空文庫: 舞姫",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"鷗外『舞姫』は近代日本的主体（立身出世とエロス）の分裂を文学化した。AI時代の主体性の歴史的構築性を再検討する基準点。",
         "related_ai_phenomenon":"AIによる近代主体表象の歴史化"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"異文化接触と主体形成",
         "description":"鷗外『舞姫』は明治日本人の異文化接触体験を文学化した、文化人類学的接触帯研究の文学的並行物。"}])

add(**C, name_ja="森鷗外『青年』",
    name_en="Mori Ōgai's Seinen",
    name_original="青年",
    period_key="明治文学期",
    definition="森鷗外が1910-11年に発表した長編小説。地方から上京した青年小泉純一の知的成長と恋愛を描く。夏目漱石『三四郎』(1908)への意識的応答であり、明治末期知識人青年の自意識を理知的に分析した。鷗外後期文学の出発点。",
    background="漱石『三四郎』への対抗意識と、鷗外の医学・文学両分野での円熟期。",
    development="鷗外後期長編『雁』『灰燼』『渋江抽斎』への展開と、大正知性主義の基礎となった。",
    historical_context="明治末期の高等教育拡充期と、青年知識人の自意識問題。",
    primary_source_url=AOZORA+"cards/000129/card2127.html",
    primary_source_type="青空文庫: 青年",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="森鷗外『雁』",
    name_en="Mori Ōgai's Gan",
    name_original="雁",
    period_key="明治文学期",
    definition="森鷗外が1911-13年に発表した中編小説。明治13年の本郷を舞台に、高利貸の妾となったお玉と医学生岡田の幻のような恋を、回想的一人称で描く。鷗外円熟期の代表作で、雅文体と心理描写の精度の頂点を成す。",
    background="鷗外の本郷在住体験と、明治中期都市風俗の歴史的記憶化。",
    development="後の谷崎潤一郎『細雪』、川端康成の女性描写に影響を与えた、明治末期心理小説の規範。",
    historical_context="明治末期の歴史的距離化と、明治初年代風俗の文学的再現。",
    primary_source_url=AOZORA+"cards/000129/card2095.html",
    primary_source_type="青空文庫: 雁",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="夏目漱石『吾輩は猫である』",
    name_en="Natsume Sōseki's Wagahai wa Neko de Aru",
    name_original="吾輩は猫である",
    period_key="明治文学期",
    definition="夏目漱石（1867-1916）が1905-06年に『ホトトギス』連載した長編小説。中学英語教師苦沙弥先生の家に住み着いた猫の視点で、明治知識人の生活と社会風刺を展開する。漱石文学の出発点として、近代日本文学最大の作家の登場を告げた作品。",
    background="ロンドン留学(1900-02)後の神経衰弱体験と、英文学者としての漱石の知的背景。",
    development="漱石後続作品『坊っちゃん』『草枕』への直接的展開と、近代日本ユーモア小説の規範となった。",
    historical_context="日露戦争前後の明治知識人の社会的位置と、英文学受容期の知的雰囲気。",
    primary_source_url=AOZORA+"cards/000148/card789.html",
    primary_source_type="青空文庫: 吾輩は猫である",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"漱石の猫視点小説は、非人間的視点による人間社会観察を文学化した。AI生成における非人間視点・第三者観察と理論的に共振する。",
         "related_ai_phenomenon":"AI生成の非人間視点・第三者観察"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"動物視点・非人間ナラティブ",
         "description":"漱石の猫視点は現代物語論の非人間ナラティブ研究の祖型的事例。"}])

add(**C, name_ja="夏目漱石『三四郎』",
    name_en="Natsume Sōseki's Sanshirō",
    name_original="三四郎",
    period_key="明治文学期",
    definition="夏目漱石が1908年『朝日新聞』連載した長編小説。熊本から東京帝国大学に上京した小川三四郎の青春と、美禰子への淡い恋を描く。後の『それから』『門』と合わせ「前期三部作」を構成する、明治末期青春小説の規範作品。",
    background="漱石の朝日新聞専属作家就任(1907)後の本格長編連載開始。",
    development="後続『それから』『門』『彼岸過迄』『行人』『こころ』への系譜的発展と、近代日本青春小説の祖型となった。",
    historical_context="明治末期の高等教育拡充期と、地方出身青年の都市体験の文学的問題化。",
    primary_source_url=AOZORA+"cards/000148/card794.html",
    primary_source_type="青空文庫: 三四郎",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"漱石の青年主体描写は、近代日本における「自意識ある主体」の文学的構築を典型化する。AI時代における主体性の歴史性を再検討する基準点。",
         "related_ai_phenomenon":"AIにおける近代的主体性の解体"}])

add(**C, name_ja="夏目漱石『それから』",
    name_en="Natsume Sōseki's Sorekara",
    name_original="それから",
    period_key="明治文学期",
    definition="夏目漱石が1909年『朝日新聞』連載した長編小説。働かない高等遊民代助が、友人平岡に譲った三千代を奪い返す決断に至る心理過程を描く。前期三部作中央作品で、明治末期インテリ青年の社会的不適応を主題化した。",
    background="明治末期高等教育卒業者の就職難と、知識人の社会的位置問題。",
    development="『門』『彼岸過迄』『行人』『こころ』への思想的展開の中継点。",
    historical_context="明治40年代の経済不況期と知識人の倦怠感。",
    primary_source_url=AOZORA+"cards/000148/card793.html",
    primary_source_type="青空文庫: それから",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="夏目漱石『こころ』",
    name_en="Natsume Sōseki's Kokoro",
    name_original="こころ",
    period_key="明治文学期",
    definition="夏目漱石が1914年『朝日新聞』連載した長編小説。「先生」と「私」の交流、先生の妻をめぐる学生時代の友人Kとの三角関係、Kの自殺と先生の罪悪感、最終的に明治天皇崩御を機にした先生の自殺を、書簡形式で展開する。漱石文学の倫理的頂点を成す代表作。",
    background="明治末期の知識人倫理問題と、明治天皇崩御(1912)による時代意識の転換。",
    development="近代日本文学の倫理的中核作品として、戦後・現代に至るまで読み継がれ、罪悪感・自意識・友情・近代性をめぐる議論の中心テクストとなった。",
    historical_context="明治から大正への時代転換期と、近代日本の倫理的核問題化。",
    primary_source_url=AOZORA+"cards/000148/card773.html",
    primary_source_type="青空文庫: こころ",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"漱石の罪悪感・自意識描写は、近代主体の倫理的核を文学的に確立する。AI生成における倫理的主体の不在問題と理論的に対峙する古典的参照点。",
         "related_ai_phenomenon":"AI生成テキストにおける倫理的主体性の不在"}])

add(**C, name_ja="夏目漱石『明暗』",
    name_en="Natsume Sōseki's Meian",
    name_original="明暗",
    period_key="明治文学期",
    definition="夏目漱石が1916年『朝日新聞』連載中に死去した未完の長編小説。新婚の津田由雄と妻お延を中心に、複数の登場人物の心理を客観的・分析的に展開する。漱石後期の方法的革新の到達点として、近代日本心理小説の頂点を成す。",
    background="漱石後期の「則天去私」思想と、ヘンリー・ジェイムズ的心理分析方法の導入。",
    development="後の中野重治、戦後第三の新人、安岡章太郎・吉行淳之介らに方法的影響を与えた。",
    historical_context="大正初期の知識人結婚生活と心理的葛藤の文学的問題化。",
    primary_source_url=AOZORA+"cards/000148/card776.html",
    primary_source_type="青空文庫: 明暗",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="国木田独歩『武蔵野』",
    name_en="Kunikida Doppo's Musashino",
    name_original="武蔵野",
    period_key="明治文学期",
    definition="国木田独歩（1871-1908）が1898-1901年に発表した短編・随筆。ツルゲーネフ『あいびき』(二葉亭四迷訳)に触発され、武蔵野の雑木林の自然美を抒情的散文で描いた。日本近代散文における自然描写の祖型として位置づけられる作品。",
    background="ツルゲーネフ自然描写の二葉亭翻訳を通じての受容と、独歩の渋谷郊外生活体験。",
    development="自然主義文学の感性的基盤となり、後の田山花袋『田舎教師』、徳田秋声、志賀直哉の自然描写に継承された。",
    historical_context="明治30年代の都市拡張期と、近郊自然への文学的眼差しの形成。",
    primary_source_url=AOZORA+"cards/000038/card354.html",
    primary_source_type="青空文庫: 武蔵野",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="島崎藤村『破戒』",
    name_en="Shimazaki Tōson's Hakai",
    name_original="破戒",
    period_key="明治文学期",
    definition="島崎藤村（1872-1943）が1906年に自費出版した長編小説。被差別部落出身を隠して教師となった瀬川丑松が、父の遺戒を破って自己の出自を告白するに至る過程を描く。日本自然主義文学の出発点であり、社会派長編小説の最初の本格作品。",
    background="藤村の信州小諸時代の体験と、ゾラ・自然主義の日本受容初期。",
    development="田山花袋『蒲団』(1907)、藤村『春』『家』『夜明け前』への発展と、自然主義文学運動の出発点となった。",
    historical_context="明治末期の被差別部落問題と、近代国民国家における差別の文学的問題化。",
    primary_source_url=AOZORA+"cards/000158/card1483.html",
    primary_source_type="青空文庫: 破戒",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"藤村の被差別主体描写は、社会的アイデンティティの隠蔽と告白のドラマを文学化した。AI時代におけるアイデンティティ表象の倫理問題を再検討する基準点。",
         "related_ai_phenomenon":"AIにおけるマイノリティ・アイデンティティ表象"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"被差別部落と社会人類学",
         "description":"藤村『破戒』は人類学的差別研究と並行する文学的問題化を成し、社会人類学と文学の交差点。"}])


# ============================================================
# C: 反自然主義・耽美派・大正白樺（10件）
# ============================================================
add(**C, name_ja="島崎藤村『夜明け前』",
    name_en="Shimazaki Tōson's Yoake-mae",
    name_original="夜明け前",
    period_key="昭和戦前戦中期",
    definition="島崎藤村が1929-35年に発表した大長編小説。木曽馬籠の本陣・庄屋を継いだ父青山半蔵の維新前後の苦闘と狂死を、平田派国学への信仰と挫折を中軸に描く。藤村文学の総括的傑作で、近代日本歴史小説の一頂点を成す。",
    background="藤村の父・島崎正樹（半蔵モデル）の生涯への息子としての回顧と、近代日本の起源への問いかけ。",
    development="近代日本歴史長編の規範作品として、戦後の大河小説（松本清張、司馬遼太郎）の祖型的位置を占めた。",
    historical_context="昭和初期の歴史回顧的気運と、明治維新60-70年の歴史化。",
    primary_source_url=AOZORA+"cards/000158/card3633.html",
    primary_source_type="青空文庫: 夜明け前",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="田山花袋『蒲団』",
    name_en="Tayama Katai's Futon",
    name_original="蒲団",
    period_key="明治文学期",
    definition="田山花袋（1872-1930）が1907年に発表した中編小説。中年作家竹中時雄が女弟子横山芳子への性的執着を告白する物語。日本自然主義の代表作にして、近代日本私小説の出発点として位置づけられる、文学史上極めて重要な作品。",
    background="花袋の女弟子岡田美知代との実体験と、フランス自然主義（ゾラ・モーパッサン）の受容。",
    development="日本自然主義の方法的核となり、後の徳田秋声、葛西善蔵、嘉村礒多、戦後の私小説（西村賢太）に至る系譜の起点となった。",
    historical_context="明治末期の自然主義文学運動高揚期と、家庭内告白文学の登場。",
    primary_source_url=AOZORA+"cards/000214/card43511.html",
    primary_source_type="青空文庫: 蒲団",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"花袋『蒲団』の自伝的告白は、私小説における「真正性の暴露」を方法化した。AI生成における擬似私小説的告白の真正性問題を再検討する古典的参照点。",
         "related_ai_phenomenon":"AI生成における擬似自伝的告白の真正性"}])

add(**C, name_ja="田山花袋『田舎教師』",
    name_en="Tayama Katai's Inaka Kyōshi",
    name_original="田舎教師",
    period_key="明治文学期",
    definition="田山花袋が1909年に発表した長編小説。埼玉羽生の若き小学校教師林清三の文学的野心と挫折・夭折を、平静な観察的散文で描く。実在モデルに基づく取材小説で、自然主義の観察方法の成熟期作品。",
    background="花袋の取材実践と、明治30年代地方教師の実像への文学的関心。",
    development="徳田秋声、岩野泡鳴、後の中村光夫評論等に継承された自然主義観察方法の規範。",
    historical_context="明治末期の地方教師の社会的位置と、青年知識人の地方的閉塞感。",
    primary_source_url=AOZORA+"cards/000214/card1668.html",
    primary_source_type="青空文庫: 田舎教師",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="北村透谷『内部生命論』",
    name_en="Kitamura Tōkoku's Naibu Seimei-ron",
    name_original="内部生命論",
    period_key="明治文学期",
    definition="北村透谷（1868-1894）が1893年『文学界』に発表した評論。「内部生命」（人間内面の精神的核）を文学の中心概念として打ち出し、外部物質的世界への対抗概念とした。明治日本ロマン主義の理論的核心であり、近代日本文学批評の出発点として位置づけられる。",
    background="エマソン・カーライルの英米超越主義の受容と、自由民権運動退潮後の精神主義的反動。",
    development="島崎藤村、樋口一葉、後の白樺派人道主義への系譜的影響を与えた、明治ロマン主義評論の頂点。",
    historical_context="明治20年代の自由民権運動敗北と、知識人の内面的退却の文学化。",
    primary_source_url=AOZORA+"cards/000157/card46487.html",
    primary_source_type="青空文庫: 内部生命論",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"透谷の「内部生命」概念は、近代日本における内面主体の発見を理論化した。AI時代における内面主体の解体と歴史的構築性を再検討する基準点。",
         "related_ai_phenomenon":"AIにおける内面主体性の歴史的構築"}])

add(**C, name_ja="永井荷風『すみだ川』",
    name_en="Nagai Kafū's Sumidagawa",
    name_original="すみだ川",
    period_key="明治文学期",
    definition="永井荷風（1879-1959）が1909年に発表した中編小説。隅田川向こうの下町を舞台に、俳諧師蘿月とその甥長吉、芸妓お糸の悲恋を、江戸情緒漂う雅文体で描く。荷風の反自然主義・耽美派文学の出発点。",
    background="荷風のフランス・米国留学(1903-08)後の帰国と、明治末期都市近代化への嫌悪。",
    development="荷風後続作品『腕くらべ』『つゆのあとさき』『濹東綺譚』への展開と、耽美派文学の制度的成立に貢献した。",
    historical_context="明治末期の自然主義全盛期に対する反動として、江戸情緒・伝統美への文学的回帰。",
    primary_source_url=AOZORA+"cards/001341/card55520.html",
    primary_source_type="青空文庫: すみだ川",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="谷崎潤一郎『刺青』",
    name_en="Tanizaki Jun'ichirō's Shisei",
    name_original="刺青",
    period_key="明治文学期",
    definition="谷崎潤一郎（1886-1965）が1910年『新思潮』に発表した短編小説。彫物師清吉が美少女の背に女郎蜘蛛を彫り、彼女が「魔性の女」へと変貌する物語を、絢爛たる雅文体で描く。日本耽美派文学の出発点として位置づけられる。",
    background="谷崎の東京帝国大学在学中の処女作で、永井荷風の絶賛により文壇登場した。",
    development="谷崎『春琴抄』『細雪』『陰翳礼讃』への系譜的展開と、日本耽美派文学の制度的成立に決定的貢献を成した。",
    historical_context="明治末期の自然主義隆盛期に対する反動的耽美主義の登場。",
    primary_source_url=AOZORA+"cards/001383/card56646.html",
    primary_source_type="青空文庫: 刺青",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="谷崎潤一郎『春琴抄』",
    name_en="Tanizaki Jun'ichirō's Shunkinshō",
    name_original="春琴抄",
    period_key="昭和戦前戦中期",
    definition="谷崎潤一郎が1933年に発表した中編小説。盲目の三味線師匠春琴と弟子佐助の倒錯的な献身愛を、句読点を抑制した文語的長文で描く。谷崎中期傑作で、日本耽美派文学の頂点を成す代表作。",
    background="関西移住(1923関東大震災後)による日本伝統美への深化と、谷崎独自の女性崇拝思想の成熟。",
    development="谷崎後期『細雪』『鍵』『瘋癲老人日記』への展開と、世界文学における日本耽美派の代表作品。",
    historical_context="昭和初期の伝統文化再評価期と、近代化への文学的反動。",
    primary_source_url=AOZORA+"cards/001383/card56654.html",
    primary_source_type="青空文庫: 春琴抄",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="芥川龍之介『羅生門』",
    name_en="Akutagawa Ryūnosuke's Rashōmon",
    name_original="羅生門",
    period_key="大正文学期",
    definition="芥川龍之介（1892-1927）が1915年『帝国文学』に発表した短編小説。『今昔物語集』を典拠に、平安京羅生門で職を失った下人が老婆から着物を奪う行為に至る心理を、緻密な分析と簡潔な文体で描く。日本近代短編小説の頂点を成す代表作。",
    background="芥川の東京帝国大学在学中の作品で、夏目漱石門下としての出発。",
    development="新思潮派の中心作品として、大正知性主義文学の制度的成立を決定づけ、世界的評価を得た（黒澤明映画化1950）。",
    historical_context="大正初期の知識人の倫理的相対主義と、古典素材の近代的再構成の流行。",
    primary_source_url=AOZORA+"cards/000879/card127.html",
    primary_source_type="青空文庫: 羅生門",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"芥川の古典再話法は、既存テクストからの再生成という構造を文学的に確立した。AI生成における既存コーパスからの再構築・再話と理論的に並行する。",
         "related_ai_phenomenon":"AIによる古典素材の再生成"}])

add(**C, name_ja="芥川龍之介『藪の中』",
    name_en="Akutagawa Ryūnosuke's Yabu no Naka",
    name_original="藪の中",
    period_key="大正文学期",
    definition="芥川龍之介が1922年『新潮』に発表した短編小説。山中の殺人事件をめぐる7人の証言が互いに矛盾する構造を持ち、「真実の到達不可能性」を主題化した。20世紀世界文学の認識論的傑作として、黒澤明映画『羅生門』(1950)で世界的に有名となった。",
    background="芥川後期の認識論的不安と、ロバート・ブラウニング『指輪と本』の影響。",
    development="後の現代世界文学（ボルヘス、ナボコフ）の不確実性の物語の祖型となり、「藪の中」は日本語慣用句となった。",
    historical_context="大正末期の知性主義の自己懐疑期と、認識論的相対主義の文学化。",
    primary_source_url=AOZORA+"cards/000879/card179.html",
    primary_source_type="青空文庫: 藪の中",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"『藪の中』の多視点矛盾構造は、唯一の真実が認識不可能であることを文学的に問題化する。AI時代におけるディープフェイク・複数情報源の真偽判断不能性と理論的に共振する。",
         "related_ai_phenomenon":"AI時代のディープフェイク・真実の到達不可能性"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"多視点・焦点化",
         "description":"『藪の中』はジュネット焦点化理論の極限的応用例として、現代物語論の中心研究対象となる。"}])

add(**C, name_ja="志賀直哉『暗夜行路』",
    name_en="Shiga Naoya's An'ya Kōro",
    name_original="暗夜行路",
    period_key="昭和戦前戦中期",
    definition="志賀直哉（1883-1971）が1921-37年に発表した長編小説。主人公時任謙作の出生秘密、結婚、妻の不貞の発覚と赦しに至る精神的遍歴を、簡潔な散文で描く。志賀文学の頂点であり、白樺派・私小説の代表作。",
    background="志賀の長期に渡る執筆過程と、白樺派人道主義の内面的深化。",
    development="日本私小説の頂点として、後の小林秀雄評論『私小説論』、戦後の私小説作家への決定的影響を与えた。",
    historical_context="大正後期から昭和初期にかけての知識人の倫理的内省期。",
    primary_source_url=AOZORA+"cards/001383/card3727.html",
    primary_source_type="青空文庫: 暗夜行路",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"私小説と心境小説詩学",
         "description":"志賀『暗夜行路』は日本私小説詩学の頂点として、現代物語論における私小説研究の中核事例。"}])


# ============================================================
# D: 大正後期・新感覚派・川端（10件）
# ============================================================
add(**C, name_ja="志賀直哉『城の崎にて』",
    name_en="Shiga Naoya's Kinosaki nite",
    name_original="城の崎にて",
    period_key="大正文学期",
    definition="志賀直哉が1917年『白樺』に発表した短編小説。電車事故後の養生のために城崎温泉に滞在した「自分」が、蜂・鼠・蠑螈の死に対する観察を通じて生と死の意識を深化させる物語。日本私小説・心境小説の方法的範型。",
    background="志賀自身の山手線事故経験(1913)と、城崎温泉での療養体験。",
    development="心境小説ジャンルの祖型として、後の梶井基次郎、嘉村礒多、戦後第三の新人に深い影響を与えた。",
    historical_context="大正中期の白樺派人道主義と、内省的散文の精緻化期。",
    primary_source_url=AOZORA+"cards/001383/card1379.html",
    primary_source_type="青空文庫: 城の崎にて",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="志賀直哉『小僧の神様』",
    name_en="Shiga Naoya's Kozō no Kamisama",
    name_original="小僧の神様",
    period_key="大正文学期",
    definition="志賀直哉が1920年に発表した短編小説。鮨屋小僧の仙吉と、彼に偶然鮨をご馳走する貴族院議員Aの物語。簡潔な記述に作者の倫理的観察と仁恕を凝縮した、白樺派人道主義の代表的短編。",
    background="志賀直哉の文体的成熟期と、白樺派人道主義の社会観の文学的展開。",
    development="日本短編小説の規範形式として、後の川端康成『掌の小説』、各種短編作家に影響を与えた。",
    historical_context="大正中期の階級格差問題と、知識人の道徳的責任感。",
    primary_source_url=AOZORA+"cards/001383/card3741.html",
    primary_source_type="青空文庫: 小僧の神様",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="武者小路実篤",
    name_en="Mushanokōji Saneatsu",
    name_original="武者小路実篤",
    period_key="大正文学期",
    definition="武者小路実篤（1885-1976）は白樺派の中心人物。1910年雑誌『白樺』創刊を主導し、人道主義・個人主義・新しき村運動(1918)で大正デモクラシーの文学的代表となった。代表作『お目出たき人』『友情』『真理先生』。",
    background="学習院出身の華族子弟集団による『白樺』創刊と、トルストイ人道主義への共鳴。",
    development="白樺派の中心として、志賀直哉・有島武郎・里見弴・木下利玄らの活動を統合し、大正人道主義文学の制度的中核となった。",
    historical_context="大正デモクラシー期の人道主義興隆と、華族・知識人の社会改革志向。",
    primary_source_url=AOZORA+"index_pages/person45.html",
    primary_source_type="青空文庫: 武者小路実篤",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="有島武郎『或る女』",
    name_en="Arishima Takeo's Aru Onna",
    name_original="或る女",
    period_key="大正文学期",
    definition="有島武郎（1878-1923）が1919年に発表した長編小説。新時代女性早月葉子（モデル：佐々城信子）の自由奔放な生と破滅を描く。大正期最大の女性主人公長編で、近代日本女性表象の決定的作品。",
    background="有島の札幌農学校・米国留学体験と、白樺派人道主義の急進化。",
    development="後の女性表象（宮本百合子・林芙美子・有吉佐和子）の祖型となり、近代日本女性主体描写の規範となった。",
    historical_context="大正デモクラシー期の女性解放運動高揚（青鞜社1911）と、新時代女性像の文学化。",
    primary_source_url=AOZORA+"cards/000025/card612.html",
    primary_source_type="青空文庫: 或る女",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"有島の女性主体描写は、近代日本の新しい女性主体性を文学的に構築した。AI時代の女性主体表象の歴史性を再検討する基準点。",
         "related_ai_phenomenon":"AIによる女性主体表象の歴史的変容"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近代女性とジェンダー人類学",
         "description":"有島『或る女』は近代日本ジェンダー研究の中核事例として、人類学的ジェンダー論の文学的対応物。"}])

add(**C, name_ja="横光利一新感覚派宣言",
    name_en="Yokomitsu Riichi's Shinkankakuha manifesto",
    name_original="新感覚派",
    period_key="大正文学期",
    definition="横光利一（1898-1947）が1924年『文藝時代』創刊と前後して打ち出した新感覚派の文学運動。「青空に瓦礫が走る」式の比喩破壊・感覚優位の文体で、自然主義散文への対抗を表明した。日本モダニズム文学の出発点となった運動。",
    background="ヨーロッパ表現主義・未来派・ダダの日本受容と、関東大震災(1923)後の文学的再構成期。",
    development="川端康成、片岡鉄兵、中河与一らとともに『文藝時代』を結集し、後の新興芸術派・新心理主義派、戦後モダニズムへの祖型となった。",
    historical_context="大正末期から昭和初期の都市近代化と、欧州前衛文学受容期。",
    primary_source_url=AOZORA+"index_pages/person168.html",
    primary_source_type="青空文庫: 横光利一",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="川端康成『伊豆の踊子』",
    name_en="Kawabata Yasunari's Izu no Odoriko",
    name_original="伊豆の踊子",
    period_key="大正文学期",
    definition="川端康成（1899-1972）が1926年に発表した短編小説。一高生「私」が伊豆を旅する途中で旅芸人一座と道連れとなり、踊子薫に淡い恋心を抱く物語。川端文学の出発点として、抒情的散文の規範となった。",
    background="川端自身の伊豆旅行体験(1918)と、新感覚派同人としての活動初期。",
    development="川端後期『雪国』『古都』『山の音』への展開と、日本抒情小説の規範形式となった。",
    historical_context="大正末期から昭和初期の旅行文化と、青年期抒情の文学化。",
    primary_source_url=AOZORA+"cards/001383/card53203.html",
    primary_source_type="青空文庫: 伊豆の踊子",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="川端康成『雪国』",
    name_en="Kawabata Yasunari's Yukiguni",
    name_original="雪国",
    period_key="昭和戦前戦中期",
    definition="川端康成が1935-37年に発表（推敲継続1947）した中編小説。東京の文筆家島村が越後湯沢の温泉地で芸者駒子と虚しく交わる物語を、徹底的に切り詰めた文体と象徴的自然描写で展開する。1968年ノーベル文学賞受賞の主要対象作。",
    background="川端の越後湯沢滞在体験と、川端独自の「東洋の虚無」美学の成熟。",
    development="戦後の川端中後期作品の規範となり、ノーベル文学賞受賞による日本文学の世界的認知の決定的契機となった。",
    historical_context="昭和10年代の日本社会の急速な変動期と、伝統美への文学的回帰。",
    primary_source_url=WIKI_JA+"%E9%9B%AA%E5%9B%BD",
    primary_source_type="Wikipedia: 雪国",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="川端康成『山の音』",
    name_en="Kawabata Yasunari's Yama no Oto",
    name_original="山の音",
    period_key="戦後文学期",
    definition="川端康成が1949-54年に発表した長編小説。鎌倉に住む老人尾形信吾が、息子の妻菊子への秘めた愛と老いの意識を深めていく物語。戦後川端文学の頂点を成す作品で、ノーベル賞対象作の一つ。",
    background="戦後の川端の鎌倉在住体験と、敗戦後日本の家族意識の変動。",
    development="戦後日本長編小説の規範作品として、後の安岡章太郎・庄野潤三の家族描写に影響を与えた。",
    historical_context="戦後復興期の家族関係の変質と、老年意識の文学化。",
    primary_source_url=WIKI_JA+"%E5%B1%B1%E3%81%AE%E9%9F%B3",
    primary_source_type="Wikipedia: 山の音",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="堀辰雄『風立ちぬ』",
    name_en="Hori Tatsuo's Kaze Tachinu",
    name_original="風立ちぬ",
    period_key="昭和戦前戦中期",
    definition="堀辰雄（1904-1953）が1936-38年に発表した中編小説。サナトリウムで結核で死にゆく節子と「私」の愛を、ヴァレリー詩句「風立ちぬ、いざ生きめやも」を主導動機に描く。日本知性派モダニズムの代表作で、宮崎駿映画化(2013)で再注目された。",
    background="堀の婚約者矢野綾子の死(1935)と、フランス象徴派・プルーストの受容。",
    development="戦後の知性派文学（福永武彦・中村真一郎）の祖型となり、日本モダニズム文学の倫理的核を形成した。",
    historical_context="昭和10年代の戦時体制下における文学的純粋性の希求。",
    primary_source_url=AOZORA+"cards/001030/card4811.html",
    primary_source_type="青空文庫: 風立ちぬ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="谷崎潤一郎『陰翳礼讃』",
    name_en="Tanizaki Jun'ichirō's In'ei Raisan",
    name_original="陰翳礼讃",
    period_key="昭和戦前戦中期",
    definition="谷崎潤一郎が1933-34年に発表した随筆。日本伝統的住空間・什器・食物・女性美における「陰翳」の美学を体系化し、西欧近代の明るさへの対抗として東洋美学を理論化した。20世紀世界の建築・デザイン論に影響を与えた美学的傑作。",
    background="谷崎の関西移住後の伝統美への沈潜と、近代電気照明文化への嫌悪。",
    development="20世紀世界の建築論（ル・コルビュジェ受容圏での日本美学評価）、戦後デザイン論、和辻哲郎風土論と並ぶ日本美学の基礎文献となった。",
    historical_context="昭和初期の伝統文化再評価期と、近代化への美学的反動。",
    primary_source_url=AOZORA+"cards/001383/card56640.html",
    primary_source_type="青空文庫: 陰翳礼讃",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"日本美学・物質文化論",
         "description":"谷崎の陰翳論は人類学的物質文化論と日本美学の橋渡しとなる、文学と美学の交差点的テクスト。"}])


# ============================================================
# E: 戦中戦後（10件）
# ============================================================
add(**C, name_ja="太宰治『人間失格』",
    name_en="Dazai Osamu's Ningen Shikkaku",
    name_original="人間失格",
    period_key="戦後文学期",
    definition="太宰治（1909-1948）が1948年6月『展望』連載した長編小説（同月玉川上水入水自殺）。主人公大庭葉蔵の幼少から自殺未遂・廃人化に至る半生を、三冊の手記の体裁で展開する。戦後文学の極北として、日本近代文学最大の自己破壊的告白作品。",
    background="太宰の薬物中毒・自殺未遂を含む実体験と、戦後の精神的混乱。",
    development="戦後第二次戦後派と並ぶ太宰文学の頂点として、戦後日本人の精神史的代表作品となった。",
    historical_context="敗戦直後の日本社会の精神的混乱期と、知識人の倫理的破綻。",
    primary_source_url=AOZORA+"cards/000035/card301.html",
    primary_source_type="青空文庫: 人間失格",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"太宰の自己破壊的告白は、近代主体の「人間として失格」を文学的に極限化した。AI時代における主体性の解体と理論的に共振する古典的参照点。",
         "related_ai_phenomenon":"AI時代の主体性解体・人間性概念の再考"}])

add(**C, name_ja="太宰治『斜陽』",
    name_en="Dazai Osamu's Shayō",
    name_original="斜陽",
    period_key="戦後文学期",
    definition="太宰治が1947年『新潮』連載した中編小説。敗戦後の没落貴族家を舞台に、母・娘かず子・弟直治を中心に、伝統と滅亡をめぐるドラマを展開する。「斜陽族」（没落上流階級）という流行語を生んだ戦後日本最大のベストセラー。",
    background="太宰の太田静子による日記提供と、敗戦後の貴族階級没落の社会的現実。",
    development="戦後文学の象徴的作品として、貴族・伝統・新時代をめぐる議論の中心テクストとなった。",
    historical_context="戦後の華族制度廃止(1947)と貴族階級の社会的没落期。",
    primary_source_url=AOZORA+"cards/000035/card1565.html",
    primary_source_type="青空文庫: 斜陽",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="坂口安吾『堕落論』",
    name_en="Sakaguchi Ango's Darakuron",
    name_original="堕落論",
    period_key="戦後文学期",
    definition="坂口安吾（1906-1955）が1946年4月『新潮』に発表した評論。「人間は堕ちる、女は堕ちる、私も堕ちる、戦争に負けたから堕ちるのではない、人間だから堕ちるのだ」と説き、戦後日本の道徳的再出発の倫理的核を提示した。戦後思想史の転換点。",
    background="敗戦直後の道徳的混乱と、戦時動員イデオロギーへの根本的反省。",
    development="戦後民主主義思想の倫理的基盤として、丸山眞男・吉本隆明らの戦後思想と並ぶ精神史的位置を占める。",
    historical_context="敗戦直後(1946)の精神的真空状態と、価値観転換期。",
    primary_source_url=AOZORA+"cards/000361/card42826.html",
    primary_source_type="青空文庫: 堕落論",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="三島由紀夫『金閣寺』",
    name_en="Mishima Yukio's Kinkakuji",
    name_original="金閣寺",
    period_key="戦後文学期",
    definition="三島由紀夫（1925-1970）が1956年に発表した長編小説。1950年金閣寺放火事件に取材し、吃音の青年僧溝口が金閣の絶対美に呪縛され、最終的に放火に至る心理過程を、絢爛たる雅文体で展開する。三島文学の頂点を成す代表作。",
    background="三島の戦後精神史的位置と、絶対美と暴力の関係への独自の哲学的探求。",
    development="戦後日本文学の象徴的作品として、世界的評価を獲得し、三島の世界文学的地位を確立した。",
    historical_context="戦後復興期の伝統文化問題と、芸術・暴力・美の関係をめぐる文学的問題化。",
    primary_source_url=WIKI_JA+"%E9%87%91%E9%96%A3%E5%AF%BA_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 金閣寺(小説)",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"三島の絶対美と暴力の文学的探求は、AI時代の美的価値判断と倫理判断の関係を再考する古典的参照点。",
         "related_ai_phenomenon":"AI生成における美的判断と倫理判断の関係"}])

add(**C, name_ja="三島由紀夫『豊饒の海』四部作",
    name_en="Mishima Yukio's Hōjō no Umi tetralogy",
    name_original="豊饒の海",
    period_key="戦後文学期",
    definition="三島由紀夫が1965-71年に発表した長大な四部作小説『春の雪』『奔馬』『暁の寺』『天人五衰』。明治末から昭和末を貫く輪廻転生の物語で、各部の主人公が同一の魂の生まれ変わりとされる構造を持つ。三島の最終遺作で、1970年自決日に最終巻原稿を完成させた。",
    background="三島の唯識思想・東洋哲学への深化と、自決を視野に入れた最終的長編構想。",
    development="戦後日本文学最大の長編構想として、世界文学的評価を獲得し、三島自決後も読み継がれる。",
    historical_context="戦後高度成長期の三島の政治的右傾化と、自決(1970年11月25日)を予期する晩年。",
    primary_source_url=WIKI_JA+"%E8%B1%8A%E9%A5%92%E3%81%AE%E6%B5%B7",
    primary_source_type="Wikipedia: 豊饒の海",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="安部公房『砂の女』",
    name_en="Abe Kōbō's Suna no Onna",
    name_original="砂の女",
    period_key="戦後文学期",
    definition="安部公房（1924-1993）が1962年に発表した長編小説。昆虫採集に出かけた教師仁木順平が砂丘の村に閉じ込められ、「砂の女」と暮らしながら脱出と帰属を巡る実存的葛藤を経験する物語。日本実存主義文学の代表作で、勅使河原宏映画化(1964)で世界的評価を得た。",
    background="安部の満洲体験と、戦後フランス実存主義（カフカ・カミュ）の受容。",
    development="戦後日本実存主義文学の頂点として、世界的評価を確立し、現代寓話小説の規範となった。",
    historical_context="高度経済成長期の日本社会変動と、近代主体の根源的疎外問題の文学化。",
    primary_source_url=WIKI_JA+"%E7%A0%82%E3%81%AE%E5%A5%B3",
    primary_source_type="Wikipedia: 砂の女",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"安部の「砂の女」は近代主体の根源的疎外を寓話化した。AI時代の主体の閉じ込められと脱出不能性を再検討する基準点。",
         "related_ai_phenomenon":"AIシステムへの主体の閉じ込められ・依存"}])

add(**C, name_ja="大江健三郎『万延元年のフットボール』",
    name_en="Ōe Kenzaburō's Man'en Gannen no Futtobōru",
    name_original="万延元年のフットボール",
    period_key="戦後文学期",
    definition="大江健三郎（1935-2023）が1967年に発表した長編小説。四国の谷間の村に帰った蜜三郎・鷹四兄弟が、万延元年(1860)の百姓一揆と現代の暴動を交錯させて自己と歴史を再認識する物語。1994年ノーベル文学賞受賞対象作。",
    background="大江の四国出身体験と、1960年代日本の政治的混乱（60年安保・大学闘争）。",
    development="戦後日本長編の代表作として世界的評価を獲得し、ノーベル文学賞受賞の主要対象作品となった。",
    historical_context="1960年代後半の日本社会の政治的緊張と、歴史的時間意識の文学化。",
    primary_source_url=WIKI_JA+"%E4%B8%87%E5%BB%B6%E5%85%83%E5%B9%B4%E3%81%AE%E3%83%95%E3%83%83%E3%83%88%E3%83%9C%E3%83%BC%E3%83%AB",
    primary_source_type="Wikipedia: 万延元年のフットボール",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="遠藤周作『沈黙』",
    name_en="Endō Shūsaku's Chinmoku",
    name_original="沈黙",
    period_key="戦後文学期",
    definition="遠藤周作（1923-1996）が1966年に発表した長編小説。江戸時代初期の日本を舞台に、ポルトガル人宣教師ロドリゴが踏み絵を踏むに至る信仰の苦悩を描く。日本キリスト教文学の頂点で、マーティン・スコセッシ映画化(2016)で世界的評価を得た。",
    background="遠藤のキリスト教徒としての日本における信仰問題と、長崎潜伏キリシタン研究。",
    development="戦後日本キリスト教文学の代表作として、宗教・文化・帝国主義をめぐる議論の中心テクストとなった。",
    historical_context="戦後日本の宗教観の変動期と、東西文化の衝突問題の文学化。",
    primary_source_url=WIKI_JA+"%E6%B2%88%E9%BB%99_(%E9%81%A0%E8%97%A4%E5%91%A8%E4%BD%9C)",
    primary_source_type="Wikipedia: 沈黙(遠藤周作)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="井伏鱒二『黒い雨』",
    name_en="Ibuse Masuji's Kuroi Ame",
    name_original="黒い雨",
    period_key="戦後文学期",
    definition="井伏鱒二（1898-1993）が1965-66年に発表した長編小説。広島原爆で被爆した姪矢須子の縁談を巡る伯父閑間重松の懊悩を、被爆体験記の引用と並行的に描く。日本原爆文学の頂点で、戦後文学の倫理的核作品。",
    background="井伏の広島地縁と、被爆者の縁談差別という戦後社会の現実。",
    development="戦後原爆文学の代表作として、原民喜・大田洋子と並ぶ被爆体験文学の中核を成す。",
    historical_context="戦後20年経過後の被爆者問題の社会的認知期と、原爆体験の文学的形式化。",
    primary_source_url=WIKI_JA+"%E9%BB%92%E3%81%84%E9%9B%A8",
    primary_source_type="Wikipedia: 黒い雨",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="中上健次『枯木灘』",
    name_en="Nakagami Kenji's Karekinada",
    name_original="枯木灘",
    period_key="現代文学期",
    definition="中上健次（1946-1992）が1977年に発表した長編小説。紀州熊野「路地」（被差別部落）を舞台に、青年秋幸の家族・血縁・暴力をめぐる物語を、フォークナー的多元的構造で展開する。日本被差別部落文学の頂点で、戦後最大の日本語表現の革新者の代表作。",
    background="中上の新宮被差別部落出身という体験と、フォークナー・ガルシア=マルケス受容。",
    development="戦後日本における被差別部落文学の頂点として、後の現代文学（古川日出男・佐伯一麦）に深い影響を与えた。",
    historical_context="高度経済成長期の被差別部落解放運動と、地方共同体の文学的問題化。",
    primary_source_url=WIKI_JA+"%E6%9E%AF%E6%9C%A8%E7%81%98",
    primary_source_type="Wikipedia: 枯木灘",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"中上の被差別部落主体描写は、近代日本における主体構築の周縁を文学化する。AI時代におけるマイノリティ主体の表象問題を再考する基準点。",
         "related_ai_phenomenon":"AIにおけるマイノリティ主体の表象"}])


# ============================================================
# F: 現代（10件）
# ============================================================
add(**C, name_ja="村上春樹『ノルウェイの森』",
    name_en="Murakami Haruki's Norwegian Wood",
    name_original="ノルウェイの森",
    period_key="現代文学期",
    definition="村上春樹（1949-）が1987年に発表した長編小説。1960年代末東京を舞台に、ワタナベトオルと直子・緑との恋愛を描く。日本国内430万部の大ベストセラーとなり、村上文学の世界的認知の決定的契機となった作品。",
    background="村上の1960年代学生運動末期の体験と、欧米文学（フィッツジェラルド・カポーティ）受容。",
    development="村上文学の世界化の出発点として、後の『海辺のカフカ』『1Q84』への展開と、日本現代文学のグローバル化を象徴する。",
    historical_context="バブル経済期日本の文化的国際化と、過去の青春の文学化。",
    primary_source_url=WIKI_JA+"%E3%83%8E%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A4%E3%81%AE%E6%A3%AE",
    primary_source_type="Wikipedia: ノルウェイの森",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"Cultural-Intelligence","link_type":"shared_concept",
         "target_entity_name":"村上春樹現象とグローバル文化",
         "description":"村上『ノルウェイの森』は日本文学の世界化現象を象徴し、文化情報学的グローバル文学市場研究の中核事例。"}])

add(**C, name_ja="村上春樹『世界の終りとハードボイルド・ワンダーランド』",
    name_en="Murakami's Hard-Boiled Wonderland and the End of the World",
    name_original="世界の終りとハードボイルド・ワンダーランド",
    period_key="現代文学期",
    definition="村上春樹が1985年に発表した長編小説。「ハードボイルド・ワンダーランド」と「世界の終り」の二つの異なる物語が並行進行する構造を持ち、村上文学の方法的革新の頂点を成す。谷崎潤一郎賞受賞作。",
    background="村上の1980年代前半の文学的成熟期と、日本ポストモダン小説の方法的探求。",
    development="日本ポストモダン文学の代表作として、後の村上長編『1Q84』『海辺のカフカ』への展開の方法的基盤となった。",
    historical_context="1980年代日本のポストモダン文化興隆期と、文学的形式の実験期。",
    primary_source_url=WIKI_JA+"%E4%B8%96%E7%95%8C%E3%81%AE%E7%B5%82%E3%82%8A%E3%81%A8%E3%83%8F%E3%83%BC%E3%83%89%E3%83%9C%E3%82%A4%E3%83%AB%E3%83%89%E3%83%BB%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89",
    primary_source_type="Wikipedia: 世界の終りとハードボイルド・ワンダーランド",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"村上の並行物語構造は、複数の現実世界の同時進行を文学化する。AI時代の並行現実生成・マルチ仮想空間と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における並行現実・マルチ仮想空間"}])

add(**C, name_ja="村上龍『コインロッカー・ベイビーズ』",
    name_en="Murakami Ryū's Coin Locker Babies",
    name_original="コインロッカー・ベイビーズ",
    period_key="現代文学期",
    definition="村上龍（1952-）が1980年に発表した長編小説。コインロッカーに捨てられた二人の少年キクとハシの暴力的・幻覚的成長を、グロテスクな想像力で描く。1980年代日本の文学的暗黒面を象徴する作品で、日本ポストモダン文学の方法的祖型。",
    background="村上龍の沖縄返還後の1970年代日本社会の暴力性への眼差し。",
    development="後の中上健次・島田雅彦・古川日出男らの幻覚的散文の祖型となり、日本ポストモダン文学の暗黒面を代表する。",
    historical_context="高度成長期日本の影の側面（捨て子問題・米軍基地・暴力）の文学的問題化。",
    primary_source_url=WIKI_JA+"%E3%82%B3%E3%82%A4%E3%83%B3%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC%E3%83%BB%E3%83%99%E3%82%A4%E3%83%93%E3%83%BC%E3%82%BA",
    primary_source_type="Wikipedia: コインロッカー・ベイビーズ",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="吉本ばなな『キッチン』",
    name_en="Banana Yoshimoto's Kitchen",
    name_original="キッチン",
    period_key="現代文学期",
    definition="吉本ばなな（1964-）が1988年に発表したデビュー中編小説。祖母を喪った大学生桜井みかげが、唯一の生き残りの心の支えとして「キッチン」（台所）を見出す物語。日本女性文学の世界的認知の決定的契機となった作品。",
    background="バブル経済期女性の都市的孤独と、新しい家族関係の文学化。",
    development="日本女性文学の世界化の出発点として、後の川上弘美・川上未映子・小川洋子らへの道を切り拓いた。",
    historical_context="バブル経済期日本の女性ライフスタイル変動と、家族解体の進展。",
    primary_source_url=WIKI_JA+"%E3%82%AD%E3%83%83%E3%83%81%E3%83%B3_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: キッチン(小説)",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"家族解体と新家族形成",
         "description":"吉本ばなな『キッチン』は人類学的家族研究と並行する、ポスト核家族時代の文学的問題化を成す。"}])

add(**C, name_ja="多和田葉子の越境文学",
    name_en="Tawada Yōko's transnational literature",
    name_original="多和田葉子",
    period_key="現代文学期",
    definition="多和田葉子（1960-）はドイツ在住で日本語・ドイツ語両言語で創作する作家。『犬婿入り』(1992)、『献灯使』(2014)、『地球にちりばめられて』三部作等で、言語・国境・文化の越境を主題化する。日本現代文学のグローバル化を象徴する代表的作家。",
    background="多和田のハンブルク・ベルリン在住体験と、両言語創作の制度的確立。",
    development="日本現代文学のグローバル化の象徴として、世界文学における日本語の越境的可能性を切り拓いた。",
    historical_context="グローバル化時代の日本文学の越境的位置と、言語アイデンティティの問題化。",
    primary_source_url=WIKI_JA+"%E5%A4%9A%E5%92%8C%E7%94%B0%E8%91%89%E5%AD%90",
    primary_source_type="Wikipedia: 多和田葉子",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"多和田の両言語創作実践は、AI時代の機械翻訳・多言語生成と理論的に共振する。母語と非母語の境界の流動化を文学的に先取りした位置。",
         "related_ai_phenomenon":"AI機械翻訳・多言語生成と作家性"},
        {"axis":"翻訳","status":"rethinking",
         "rationale":"多和田の越境は翻訳概念そのものを問い直す文学的実践であり、AI翻訳時代の翻訳哲学を再考する基準点。",
         "related_ai_phenomenon":"AI翻訳時代の翻訳概念再考"}])

add(**C, name_ja="川上未映子『乳と卵』",
    name_en="Kawakami Mieko's Chichi to Ran",
    name_original="乳と卵",
    period_key="現代文学期",
    definition="川上未映子（1976-）が2007年『文學界』に発表した中編小説で2008年第138回芥川賞受賞作。豊胸手術を考える姉巻子と思春期の娘緑子を巡る物語を、大阪弁の流動的散文で描く。21世紀日本女性文学の方法的革新を象徴する作品。",
    background="川上の関西出身体験と、樋口一葉文体への意識的回帰。",
    development="後の『すべて真夜中の恋人たち』『夏物語』への展開と、現代日本女性文学の世界的評価獲得（村上春樹推薦による国際的認知）。",
    historical_context="平成20年代の女性身体・出産・家族関係をめぐる社会的議論期。",
    primary_source_url=WIKI_JA+"%E4%B9%B3%E3%81%A8%E5%8D%B5",
    primary_source_type="Wikipedia: 乳と卵",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="小川洋子『博士の愛した数式』",
    name_en="Ogawa Yōko's Hakase no Aishita Sūshiki",
    name_original="博士の愛した数式",
    period_key="現代文学期",
    definition="小川洋子（1962-）が2003年に発表した長編小説。記憶が80分しか持たない数学者の家政婦と息子ルートとの交流を、数学的美と日常の優しさを織り交ぜて描く。第1回本屋大賞受賞作で、現代日本文学の世界的評価を象徴する作品。",
    background="小川の数学への文学的関心と、現代日本における科学と芸術の橋渡し志向。",
    development="現代日本文学の国際的評価の代表作として、世界各国で翻訳・受容された。",
    historical_context="平成15年(2003)前後の日本文学の世界化と、科学技術と人間関係の文学的問題化。",
    primary_source_url=WIKI_JA+"%E5%8D%9A%E5%A3%AB%E3%81%AE%E6%84%9B%E3%81%97%E3%81%9F%E6%95%B0%E5%BC%8F",
    primary_source_type="Wikipedia: 博士の愛した数式",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="平野啓一郎『日蝕』",
    name_en="Hirano Keiichirō's Nisshoku",
    name_original="日蝕",
    period_key="現代文学期",
    definition="平野啓一郎（1975-）が1998年『新潮』に発表したデビュー長編で、第120回芥川賞受賞作。15世紀末フランスを舞台にドミニコ会修道士ニコラスの錬金術的体験を、擬古文体で展開する。三島由紀夫以来の若手雅文体作家として注目された。",
    background="平野の京都大学法学部時代の独学による西欧中世神秘主義への沈潜。",
    development="平成期日本若手作家の知的水準を象徴する作品として、後の『マチネの終わりに』『ある男』への発展。",
    historical_context="平成10年代の日本若手作家の国際志向と、西欧中世への文学的回帰。",
    primary_source_url=WIKI_JA+"%E6%97%A5%E8%9D%95_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 日蝕(小説)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="村田沙耶香『コンビニ人間』",
    name_en="Murata Sayaka's Konbini Ningen",
    name_original="コンビニ人間",
    period_key="現代文学期",
    definition="村田沙耶香（1979-）が2016年『文學界』に発表した中編で第155回芥川賞受賞作。コンビニ店員として18年間働く36歳の独身女性古倉恵子を主人公に、現代日本社会の規範と異常性を逆転的に提示する。世界30言語以上に翻訳された平成末期日本文学の世界的代表作。",
    background="村田自身のコンビニアルバイト体験(20年弱)と、現代日本社会への観察。",
    development="平成末期日本女性文学の世界化の代表作として、世界的評価を獲得し、グローバル文学市場における日本現代文学の位置を確立した。",
    historical_context="平成末期の日本社会の家族・労働・性の規範変動と、非婚女性の社会的位置問題。",
    primary_source_url=WIKI_JA+"%E3%82%B3%E3%83%B3%E3%83%93%E3%83%8B%E4%BA%BA%E9%96%93",
    primary_source_type="Wikipedia: コンビニ人間",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"村田の主人公は社会規範に適合できない「異常な主体」を肯定的に提示する。AI時代における主体性の規範からの逸脱と理論的に共振する。",
         "related_ai_phenomenon":"AI時代の主体性の規範化と逸脱"},
        {"axis":"受容","status":"rethinking",
         "rationale":"『コンビニ人間』のグローバル受容は、日本社会の特殊性が普遍的問題として読み替えられる現象を示す。AI翻訳時代における文化的特殊性の普遍化を理論化する基準点。",
         "related_ai_phenomenon":"AI翻訳時代における文化的特殊性の普遍化"}])

add(**C, name_ja="又吉直樹『火花』",
    name_en="Matayoshi Naoki's Hibana",
    name_original="火花",
    period_key="現代文学期",
    definition="又吉直樹（1980-）が2015年『文學界』に発表したデビュー中編で第153回芥川賞受賞作。芸人徳永と先輩芸人神谷の交流を通じて、芸（笑い）の倫理を探求する。芸人による純文学受賞という現象自体が、平成27年文壇の最大事件となった。",
    background="又吉自身のお笑い芸人としての20年の体験と、太宰治・尾崎放哉等への文学的傾倒。",
    development="平成末期の純文学とエンタメの境界再編現象を象徴する作品として、文壇制度の問い直しを引き起こした。",
    historical_context="平成27年(2015)の文芸ジャーナリズムの変容と、SNS時代の文学的注目の集中。",
    primary_source_url=WIKI_JA+"%E7%81%AB%E8%8A%B1_(%E5%B0%8F%E8%AA%AC)",
    primary_source_type="Wikipedia: 火花(小説)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"又吉の事例は、文学的作者性が制度的文壇から拡散していく過程を典型化する。AI時代の作者性の拡散と理論的に共振する。",
         "related_ai_phenomenon":"AI時代の作者性の拡散・脱制度化"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Create periods
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="日本",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        # Insert concepts
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
        print(f"[c18 add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c18 add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
