"""LIT-DB Phase 2 Wave 22 — C32 ADD: Diaspora Literature (+80 concepts).

Subfield: lit_diaspora (id=20). Existing 141 concepts; this wave adds 80 NEW.
Coverage: Asian American expanded (Chinese/Korean/Vietnamese), Indian diaspora deep,
Caribbean expanded, Black British detailed, Jewish Diaspora deeper.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("脱植民地・初期移民文学期", "Decolonial / Early Migrant",
     1900, 1965, "両大戦間期から脱植民地化初期に至る世代。"),
    ("ポストコロニアル・ディアスポラ期", "Postcolonial Diaspora",
     1965, 2000, "1965年米移民法改正以降のポストコロニアル離散文学成熟期。"),
    ("グローバル・ディアスポラ期", "Global Diaspora",
     2000, 2026, "9.11以降のグローバル離散・難民・トランスリンガル創作の時代。"),
]

WIKI_EN = "https://en.wikipedia.org/wiki/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_diaspora", region="ディアスポラ",
         original_script="roman")


# ============================================================
# A: Asian American Chinese expanded (16)
# ============================================================
add(**C, name_ja="マキシン・ホン・キングストン『第五の平和の書』",
    name_en="Maxine Hong Kingston's The Fifth Book of Peace",
    name_original="The Fifth Book of Peace", period_key="グローバル・ディアスポラ期",
    definition="キングストンが2003年に発表したジャンル混成作。1991年オークランド火災で焼失した原稿の喪失と再構築を巡る瞑想・小説・回想で、アジア系米国老成期文学を体現する。",
    background="2000年代アジア系米国第一世代作家の老成期創作。",
    development="キングストンの晩年代表作として批評的評価を受けた。",
    historical_context="2000年代初頭9.11後の平和文学興隆期。",
    primary_source_url=WIKI_EN+"Maxine_Hong_Kingston",
    primary_source_type="Wikipedia: Maxine Hong Kingston",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エイミー・タン『100の秘密の感覚』",
    name_en="Amy Tan's The Hundred Secret Senses",
    name_original="The Hundred Secret Senses", period_key="ポストコロニアル・ディアスポラ期",
    definition="タンが1995年に発表した長編。半分中国系の主人公が異母姉と訪れる中国農村で前世記憶と霊的世界に触れる物語で、華人ディアスポラ文学にエスニック霊性を導入した。",
    background="1990年代中盤ニューエイジ的霊性と華人文学の交差。",
    development="タンの霊的・神秘主義的傾向の代表作となった。",
    historical_context="1990年代米国中産階級スピリチュアル文学興隆期。",
    primary_source_url=WIKI_EN+"Amy_Tan",
    primary_source_type="Wikipedia: Amy Tan",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エイミー・タン『溺れる魚を救う』",
    name_en="Amy Tan's Saving Fish from Drowning",
    name_original="Saving Fish from Drowning", period_key="グローバル・ディアスポラ期",
    definition="タンが2005年に発表した長編。ビルマで失踪した米国人観光客集団を死者の語り手が観察する変則的構成で、グローバル観光・ディアスポラ・東南アジア政治を結び付けた。",
    background="2000年代ビルマ軍政下の人権問題と米国観光業の批判。",
    development="タンの最も実験的構成作として注目された。",
    historical_context="2000年代半ばのビルマ国際批判期。",
    primary_source_url=WIKI_EN+"Saving_Fish_from_Drowning",
    primary_source_type="Wikipedia: Saving Fish from Drowning",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エイミー・タン『驚異の谷』",
    name_en="Amy Tan's The Valley of Amazement",
    name_original="The Valley of Amazement", period_key="グローバル・ディアスポラ期",
    definition="タンが2013年に発表した長編。20世紀初頭上海の高級遊郭を舞台に、半分中国系の遊女と母娘三世代の物語を描き、華人女性史と性労働の文学化を達成した。",
    background="2010年代タンの中国近代史への関心深化。",
    development="タン晩期の代表作として評価された。",
    historical_context="2010年代米国華人歴史小説のジェンダー化期。",
    primary_source_url=WIKI_EN+"The_Valley_of_Amazement",
    primary_source_type="Wikipedia: The Valley of Amazement",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ギッシュ・ジェン『約束の地のモナ』",
    name_en="Gish Jen's Mona in the Promised Land",
    name_original="Mona in the Promised Land", period_key="ポストコロニアル・ディアスポラ期",
    definition="ジェンが1996年に発表した長編。華人系少女モナがユダヤ教に改宗する物語で、ニューヨーク郊外の多文化コンタクトゾーンを描いたエスニック越境文学の代表作。",
    background="1990年代米国多文化主義論議の最盛期。",
    development="エスニック・ハイブリディティ研究の主要参照テクストとなった。",
    historical_context="1990年代後半米国アイデンティティ政治期。",
    primary_source_url=WIKI_EN+"Gish_Jen",
    primary_source_type="Wikipedia: Gish Jen",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"エスニック改宗による主体形成は、AI時代の選択的アイデンティティ構築の祖型。",
         "related_ai_phenomenon":"AI時代の選択的アイデンティティ"}])

add(**C, name_ja="ギッシュ・ジェン『世界と町』",
    name_en="Gish Jen's World and Town",
    name_original="World and Town", period_key="グローバル・ディアスポラ期",
    definition="ジェンが2010年に発表した長編。ニューイングランド小村に60代の華人系米国未亡人と新参カンボジア難民家族が共生する物語で、9.11以降の小コミュニティのディアスポラを描いた。",
    background="2000年代後半米国地方の難民受け入れ問題。",
    development="ジェンの中期代表作として評価された。",
    historical_context="2010年代初頭米国地方共同体のディアスポラ化期。",
    primary_source_url=WIKI_EN+"Gish_Jen",
    primary_source_type="Wikipedia: Gish Jen",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ギッシュ・ジェン『抵抗者たち』",
    name_en="Gish Jen's The Resisters",
    name_original="The Resisters", period_key="グローバル・ディアスポラ期",
    definition="ジェンが2020年に発表したディストピア長編。AI監視社会の近未来米国で華人系野球選手の少女が抵抗する物語で、アジア系米国SF文学の重要例となった。",
    background="2020年代AI監視社会への文学的応答とアジア系SFの興隆。",
    development="アジア系米国スペキュラティブ・フィクションの代表作。",
    historical_context="2020年代AIガバナンス論議期。",
    primary_source_url=WIKI_EN+"Gish_Jen",
    primary_source_type="Wikipedia: Gish Jen",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"AI監視下のエスニック抵抗は、AI時代のディアスポラ主体性の文学的探求。",
         "related_ai_phenomenon":"AI監視とエスニック主体"}])

add(**C, name_ja="チャンネ・リー『漂う高みに』",
    name_en="Chang-rae Lee's Aloft",
    name_original="Aloft", period_key="グローバル・ディアスポラ期",
    definition="チャンネ・リーが2004年に発表した長編。イタリア系米国男性主人公の語りで韓国系米国家族との関係を逆方向から描き、エスニック越境視点の倫理を探究した。",
    background="2000年代初頭米国エスニック小説の白人視点反転実験。",
    development="リーの最も実験的アイデンティティ越境作となった。",
    historical_context="2000年代米国エスニック・アイデンティティ論議期。",
    primary_source_url=WIKI_EN+"Chang-rae_Lee",
    primary_source_type="Wikipedia: Chang-rae Lee",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="チャンネ・リー『降伏した者』",
    name_en="Chang-rae Lee's The Surrendered",
    name_original="The Surrendered", period_key="グローバル・ディアスポラ期",
    definition="リーが2010年に発表した長編。朝鮮戦争孤児院から始まる三人の人生をニュージャージー・イタリア・満州に展開させ、戦争トラウマと戦後ディアスポラを描いた史詩。",
    background="2010年朝鮮戦争60年と韓国系米国第二世代の歴史回帰。",
    development="リーの最も野心的歴史小説として全米図書批評家賞最終候補となった。",
    historical_context="2010年代韓国系米国歴史小説興隆期。",
    primary_source_url=WIKI_EN+"The_Surrendered",
    primary_source_type="Wikipedia: The Surrendered",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チャンネ・リー『満ち足りた海で』",
    name_en="Chang-rae Lee's On Such a Full Sea",
    name_original="On Such a Full Sea", period_key="グローバル・ディアスポラ期",
    definition="リーが2014年に発表したディストピア長編。中国系移民労働者集合体B-Mor（旧ボルチモア）から失踪した少女ファンの物語で、アジア系米国ディストピアSFを確立した。",
    background="2010年代米国SF文学のエスニック化、気候危機・階級分断の文学的探究。",
    development="リーの最もスペキュラティブな実験作となった。",
    historical_context="2010年代半ばアメリカ・ディストピア文学興隆期。",
    primary_source_url=WIKI_EN+"On_Such_a_Full_Sea",
    primary_source_type="Wikipedia: On Such a Full Sea",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"集合体B-Morの集合的主体性は、AI時代の集合主体性の文学的祖型。",
         "related_ai_phenomenon":"集合的AI主体"}])

add(**C, name_ja="ラン・サマンサ・チャン『相続』",
    name_en="Lan Samantha Chang's Inheritance",
    name_original="Inheritance", period_key="グローバル・ディアスポラ期",
    definition="ラン・サマンサ・チャン（1965-）が2004年に発表したデビュー長編。日中戦争から米国移民までの華人姉妹三世代を描き、戦争記憶と継承を主題化した華人女性ディアスポラ作。",
    background="2000年代米国アジア系第二世代女性作家の歴史回帰。",
    development="チャンの主要作として評価された。",
    historical_context="2000年代米国華人女性歴史小説興隆期。",
    primary_source_url=WIKI_EN+"Lan_Samantha_Chang",
    primary_source_type="Wikipedia: Lan Samantha Chang",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ラン・サマンサ・チャン『飢餓』",
    name_en="Lan Samantha Chang's Hunger",
    name_original="Hunger", period_key="ポストコロニアル・ディアスポラ期",
    definition="チャンが1998年に発表した中編集。ニューヨークの華人系移民音楽家家族の崩壊を描いた表題作で華人ディアスポラ文学に新たな心理的精緻さを導入した。",
    background="1990年代末華人ディアスポラ第二世代の心理小説興隆。",
    development="アイオワ作家ワークショップ後継者世代の代表作となった。",
    historical_context="1990年代末華人女性短編文学興隆期。",
    primary_source_url=WIKI_EN+"Lan_Samantha_Chang",
    primary_source_type="Wikipedia: Lan Samantha Chang",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="イーユン・リー『ありえない理由のための場所』",
    name_en="Yiyun Li's Where Reasons End",
    name_original="Where Reasons End", period_key="グローバル・ディアスポラ期",
    definition="イーユン・リー（1972-）が2019年に発表した長編。自殺で失った息子と亡霊として対話する母親の物語で、トランスリンガル英語創作とトラウマ表象の極限を達成した。",
    background="2010年代後半リーの個人的喪失体験の文学化。",
    development="批評的最高評価を獲得し、リーの代表作となった。",
    historical_context="2010年代末トラウマ文学の精神医学的成熟期。",
    primary_source_url=WIKI_EN+"Where_Reasons_End",
    primary_source_type="Wikipedia: Where Reasons End",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"母語放棄者による喪失と言語の関係探究は、AI時代の言語と感情の問題に通じる。",
         "related_ai_phenomenon":"AI生成と感情真正性"}])

add(**C, name_ja="イーユン・リー『私の人生から愛しい友よ』",
    name_en="Yiyun Li's Dear Friend, from My Life I Write to You in Your Life",
    name_original="Dear Friend, from My Life I Write to You in Your Life",
    period_key="グローバル・ディアスポラ期",
    definition="リーが2017年に発表したエッセイ集。中国語放棄と英語選択、自殺未遂、文学との関係を綴り、トランスリンガル作家の極限的自己分析を達成した。",
    background="2010年代半ば作家の個人的危機の文学化。",
    development="リーのトランスリンガル理論の中核テクストとなった。",
    historical_context="2010年代後半作家自殺問題の文学化期。",
    primary_source_url=WIKI_EN+"Yiyun_Li",
    primary_source_type="Wikipedia: Yiyun Li",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"母語拒絶と外国語選択の意識的論理は、AI時代の言語選択論議の文学的基盤。",
         "related_ai_phenomenon":"言語選択とアイデンティティ"}])

add(**C, name_ja="イーユン・リー『ガチョウの書』",
    name_en="Yiyun Li's The Book of Goose",
    name_original="The Book of Goose", period_key="グローバル・ディアスポラ期",
    definition="リーが2022年に発表した長編。戦後フランス農村の少女二人の創作と支配の関係を描き、リー後期の最高傑作と評価された。",
    background="2020年代リーの英語創作成熟期。",
    development="PEN/フォークナー賞最終候補となった。",
    historical_context="2020年代世界文学のトランスリンガル成熟期。",
    primary_source_url=WIKI_EN+"The_Book_of_Goose",
    primary_source_type="Wikipedia: The Book of Goose",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ルース・オゼキ『時を生むものの物語』",
    name_en="Ruth Ozeki's A Tale for the Time Being",
    name_original="A Tale for the Time Being", period_key="グローバル・ディアスポラ期",
    definition="ルース・オゼキ（1956-）が2013年に発表した長編。日系カナダ人作家がBC海岸で発見した日本少女の日記を読む二重構造で、3.11・量子物理・禅・ディアスポラを統合した。",
    background="2011年東日本大震災と量子論的世界文学の興隆。",
    development="ブッカー賞最終候補となり、女性版図書賞受賞した。",
    historical_context="2010年代日系ディアスポラ文学のトランス太平洋化期。",
    primary_source_url=WIKI_EN+"A_Tale_for_the_Time_Being",
    primary_source_type="Wikipedia: A Tale for the Time Being",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"作中作家と読者の量子的相互作用は、AI生成と読者の関係を予示する。",
         "related_ai_phenomenon":"AIと読者の相互生成"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"量子的観測者性",
         "description":"オゼキの量子文学は科学哲学の観測者問題と並行する。"}])


# ============================================================
# B: Asian American — Ozeki/Park/Ko/Hua/Ma/etc (12)
# ============================================================
add(**C, name_ja="ルース・オゼキ『すべての創造の上に』",
    name_en="Ruth Ozeki's All Over Creation",
    name_original="All Over Creation", period_key="ポストコロニアル・ディアスポラ期",
    definition="オゼキが2003年に発表した長編。アイダホのジャガイモ農家を舞台に遺伝子組換え作物・先住民権・日系ディアスポラを統合した、エコクリティカルなディアスポラ文学の代表作。",
    background="2000年代初頭の遺伝子組換え論争と日系第三世代の環境意識。",
    development="日系ディアスポラ・エコ文学の確立的作品となった。",
    historical_context="2000年代初頭米国GMO論議激化期。",
    primary_source_url=WIKI_EN+"Ruth_Ozeki",
    primary_source_type="Wikipedia: Ruth Ozeki",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"環境とエスニシティ",
         "description":"オゼキのGMO批判は環境人類学のエスニック資源論と並行する。"}])

add(**C, name_ja="ルース・オゼキ『マイ・イヤー・オブ・ミーツ』",
    name_en="Ruth Ozeki's My Year of Meats",
    name_original="My Year of Meats", period_key="ポストコロニアル・ディアスポラ期",
    definition="オゼキが1998年に発表したデビュー長編。日米両国を行き来する日系米国TV番組制作者を主人公に、米国畜産業のホルモン問題と日本主婦の生を交差させた。",
    background="1990年代末グローバル食品産業批判の興隆。",
    development="日系ディアスポラ食文学の創成作となった。",
    historical_context="1990年代末トランス太平洋メディア批判期。",
    primary_source_url=WIKI_EN+"My_Year_of_Meats",
    primary_source_type="Wikipedia: My Year of Meats",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ルース・オゼキ『形と空の書』",
    name_en="Ruth Ozeki's The Book of Form and Emptiness",
    name_original="The Book of Form and Emptiness", period_key="グローバル・ディアスポラ期",
    definition="オゼキが2021年に発表した長編。声を聴く少年と本そのものが語り手となる仏教的メタフィクションで、女性版図書賞受賞しオゼキ後期の代表作となった。",
    background="2010年代後半オゼキの禅僧侶としての成熟と書物哲学。",
    development="2022年女性版図書賞を受賞しオゼキの世界文学的承認を確立した。",
    historical_context="2020年代世界文学の禅・スピリチュアル傾向期。",
    primary_source_url=WIKI_EN+"The_Book_of_Form_and_Emptiness",
    primary_source_type="Wikipedia: The Book of Form and Emptiness",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"本それ自体が語り手となる存在論は、AI著者性の文学的祖型。",
         "related_ai_phenomenon":"AI著者性とテクスト主体"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"色即是空",
         "description":"オゼキの仏教存在論は仏教哲学の色空論を文学化した。"}])

add(**C, name_ja="エド・パーク『個人的日々』",
    name_en="Ed Park's Personal Days",
    name_original="Personal Days", period_key="グローバル・ディアスポラ期",
    definition="エド・パーク（1970-）が2008年に発表したデビュー長編。NYオフィスで不安に苛まれる華人系従業員を含む集団を実験的人称・形式で描き、アジア系米国オフィス文学を確立した。",
    background="2000年代後半グローバル金融危機前夜のオフィス文学興隆。",
    development="韓国系米国実験文学の重要作となった。",
    historical_context="2008年金融危機直前期。",
    primary_source_url=WIKI_EN+"Ed_Park_(writer)",
    primary_source_type="Wikipedia: Ed Park",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エド・パーク『同床異夢』",
    name_en="Ed Park's Same Bed Different Dreams",
    name_original="Same Bed Different Dreams", period_key="グローバル・ディアスポラ期",
    definition="パークが2023年に発表した長編。20世紀韓国独立運動の架空組織KPGをテーマに陰謀論的歴史メタフィクションを展開し、韓国系米国実験文学の頂点に達した。",
    background="2020年代韓国系米国第二世代作家の歴史回帰と実験性。",
    development="全米図書批評家賞最終候補となった。",
    historical_context="2020年代韓国独立運動100年期。",
    primary_source_url=WIKI_EN+"Same_Bed_Different_Dreams",
    primary_source_type="Wikipedia: Same Bed Different Dreams",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="リサ・コ『去る者たち』",
    name_en="Lisa Ko's The Leavers",
    name_original="The Leavers", period_key="グローバル・ディアスポラ期",
    definition="リサ・コ（1979-）が2017年に発表したデビュー長編。突然消えた中国系移民母と養子に出された息子の物語で、不法移民・拘留・分離家族の問題を描いた。",
    background="2010年代中頃の米国移民拘留・親子分離政策批判。",
    development="PEN/ベリンゲン賞受賞しアジア系移民拘留文学の代表作となった。",
    historical_context="2010年代後半トランプ移民政策批判期。",
    primary_source_url=WIKI_EN+"The_Leavers",
    primary_source_type="Wikipedia: The Leavers",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴァネッサ・フア『紫禁城』",
    name_en="Vanessa Hua's Forbidden City",
    name_original="Forbidden City", period_key="グローバル・ディアスポラ期",
    definition="ヴァネッサ・フア（1973-）が2022年に発表した長編。文化大革命期に毛沢東の専属ダンサーとなる農村少女を描き、華人ディアスポラ作家による中国近代史の文学化を達成した。",
    background="2020年代華人系米国第二世代作家による中国近現代史回帰。",
    development="フアの代表的歴史小説となった。",
    historical_context="2020年代米中緊張下の華人歴史小説興隆期。",
    primary_source_url=WIKI_EN+"Vanessa_Hua",
    primary_source_type="Wikipedia: Vanessa Hua",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ヴァネッサ・フア『欺瞞とその他の可能性』",
    name_en="Vanessa Hua's Deceit and Other Possibilities",
    name_original="Deceit and Other Possibilities", period_key="グローバル・ディアスポラ期",
    definition="フアが2016年に発表した短編集。シリコンバレー華人系移民・韓国系教会・カリブ系等の多様な太平洋系米国移民の生を描き、シリコンバレー・ディアスポラ文学を確立した。",
    background="2010年代半ばシリコンバレーのテクノ・ディアスポラ文学興隆。",
    development="シリコンバレー・アジア系米国短編の代表作となった。",
    historical_context="2010年代半ばテック・ブーム下のディアスポラ期。",
    primary_source_url=WIKI_EN+"Vanessa_Hua",
    primary_source_type="Wikipedia: Vanessa Hua",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="リン・マ『セヴェランス』",
    name_en="Ling Ma's Severance",
    name_original="Severance", period_key="グローバル・ディアスポラ期",
    definition="リン・マ（1983-）が2018年に発表したデビュー長編。中国系米国出版社員が「シェン熱」パンデミック後のニューヨークを彷徨う物語で、移民・労働・終末の融合を達成した。",
    background="2010年代後半パンデミック予感的SFと華人移民労働文学の交差。",
    development="2020年代パンデミック文学の予言作と再評価された。",
    historical_context="2018年パンデミック直前期。",
    primary_source_url=WIKI_EN+"Severance_(Ma_novel)",
    primary_source_type="Wikipedia: Severance",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"パンデミック下のルーティン継続主体は、AI自動化労働の文学的予示。",
         "related_ai_phenomenon":"AI労働自動化と主体"}])

add(**C, name_ja="リン・マ『至福の山』",
    name_en="Ling Ma's Bliss Montage",
    name_original="Bliss Montage", period_key="グローバル・ディアスポラ期",
    definition="リン・マが2022年に発表した短編集。スペキュラティブな超現実的設定で華人系米国女性の経験を再構成し、エスニック・スペキュラティブ・フィクションの代表作となった。",
    background="2020年代エスニック・スペキュラティブ短編の興隆。",
    development="リン・マの実験的方向性を確立する第二作となった。",
    historical_context="2020年代米国スペキュラティブ短編興隆期。",
    primary_source_url=WIKI_EN+"Bliss_Montage",
    primary_source_type="Wikipedia: Bliss Montage",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チャールズ・ユー『安全に生きる科学小説的宇宙のための方法』",
    name_en="Charles Yu's How to Live Safely in a Science Fictional Universe",
    name_original="How to Live Safely in a Science Fictional Universe",
    period_key="グローバル・ディアスポラ期",
    definition="ユーが2010年に発表したデビュー長編。タイムマシン修理工の華人系息子が父を探す物語で、SFメタフィクションとアジア系米国父子関係を融合した。",
    background="2010年代初頭アジア系米国SFの興隆。",
    development="ユーの『インテリア・チャイナタウン』への道を開いた重要先行作。",
    historical_context="2010年代米国エスニックSF興隆期。",
    primary_source_url=WIKI_EN+"How_to_Live_Safely_in_a_Science_Fictional_Universe",
    primary_source_type="Wikipedia: How to Live Safely",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"SFメタ言語によるエスニック表象は、AI生成エスニック・テキストの祖型。",
         "related_ai_phenomenon":"AI生成エスニック表象"}])

add(**C, name_ja="クリスタル・ハナ・キム『君が去ったら』",
    name_en="Crystal Hana Kim's If You Leave Me",
    name_original="If You Leave Me", period_key="グローバル・ディアスポラ期",
    definition="クリスタル・ハナ・キムが2018年に発表したデビュー長編。朝鮮戦争期の少女ハネと三人の男性の関係を描き、韓国系米国第二世代女性作家による戦争史復興作。",
    background="2010年代末韓国系米国女性作家による朝鮮戦争歴史回帰。",
    development="現代韓国系米国歴史小説の重要新人作となった。",
    historical_context="2010年代末韓国戦争史小説興隆期。",
    primary_source_url=WIKI_EN+"Crystal_Hana_Kim",
    primary_source_type="Wikipedia: Crystal Hana Kim",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: Korean American expanded (10)
# ============================================================
add(**C, name_ja="ミン・ジン・リー『無料の食事』",
    name_en="Min Jin Lee's Free Food for Millionaires",
    name_original="Free Food for Millionaires", period_key="グローバル・ディアスポラ期",
    definition="ミン・ジン・リーが2007年に発表したデビュー長編。プリンストン卒の韓国系米国女性ケイシーがNY金融界で奮闘する物語で、韓国系米国女性労働階級・移民第二世代を主題化した。",
    background="2000年代後半韓国系米国第二世代女性の労働文学興隆。",
    development="リーの『パチンコ』への礎石作となった。",
    historical_context="2000年代後半NY金融界の多様化期。",
    primary_source_url=WIKI_EN+"Min_Jin_Lee",
    primary_source_type="Wikipedia: Min Jin Lee",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ステフ・チャ『君の家は支払う』",
    name_en="Steph Cha's Your House Will Pay",
    name_original="Your House Will Pay", period_key="グローバル・ディアスポラ期",
    definition="ステフ・チャ（1986-）が2019年に発表した長編。1991年LA韓国人女性店主による黒人少女射殺事件と現代の余波を描き、韓国系・アフリカ系米国の人種関係を文学化した。",
    background="2019年LA暴動30年と韓黒関係の歴史見直し。",
    development="ロサンゼルス・タイムズ図書賞受賞しエスニック間関係文学の代表作となった。",
    historical_context="2010年代末黒人生命運動下の韓国系米国文学。",
    primary_source_url=WIKI_EN+"Your_House_Will_Pay",
    primary_source_type="Wikipedia: Your House Will Pay",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"エスニック間暴力",
         "description":"チャの韓黒関係描写は人種関係人類学と並行する。"}])

add(**C, name_ja="ステフ・チャ『家へ追え』",
    name_en="Steph Cha's Follow Her Home",
    name_original="Follow Her Home", period_key="グローバル・ディアスポラ期",
    definition="チャが2013年に発表したデビュー長編。レイモンド・チャンドラー的探偵フィクションを韓国系米国女性主人公で書き換え、エスニック・ノワールを確立したシリーズ第一作。",
    background="2010年代米国エスニック・ノワール興隆。",
    development="エスニック探偵フィクションの新世代代表作となった。",
    historical_context="2010年代米国ジャンル文学のエスニック化期。",
    primary_source_url=WIKI_EN+"Steph_Cha",
    primary_source_type="Wikipedia: Steph Cha",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="パティ・ユミ・コトレル『平和を乱して悪い』",
    name_en="Patty Yumi Cottrell's Sorry to Disrupt the Peace",
    name_original="Sorry to Disrupt the Peace", period_key="グローバル・ディアスポラ期",
    definition="パティ・ユミ・コトレルが2017年に発表したデビュー長編。養子の弟の自殺後にミルウォーキーへ戻る韓国系養子の三十代女性を描き、養子ディアスポラ文学を新たな心理的水準に押し上げた。",
    background="2010年代後半韓国系米国養子経験の文学化。",
    development="ホワイティング賞受賞しトランスナショナル養子文学の代表作となった。",
    historical_context="2010年代末韓国系養子文学興隆期。",
    primary_source_url=WIKI_EN+"Patty_Yumi_Cottrell",
    primary_source_type="Wikipedia: Patty Yumi Cottrell",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クリス・リー『漂泊する家』",
    name_en="Krys Lee's Drifting House",
    name_original="Drifting House", period_key="グローバル・ディアスポラ期",
    definition="クリス・リー（1973-）が2012年に発表したデビュー短編集。LA韓国系・北朝鮮脱北者・韓国系米国教会等を題材に、グローバル韓国ディアスポラの多様性を描いた。",
    background="2010年代初頭韓国系米国短編集の地理的拡大。",
    development="現代韓国ディアスポラ短編の代表作となった。",
    historical_context="2010年代北朝鮮脱北者問題の文学化期。",
    primary_source_url=WIKI_EN+"Krys_Lee",
    primary_source_type="Wikipedia: Krys Lee",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クリス・リー『私が北朝鮮人になった方法』",
    name_en="Krys Lee's How I Became a North Korean",
    name_original="How I Became a North Korean", period_key="グローバル・ディアスポラ期",
    definition="リーが2016年に発表したデビュー長編。中朝国境地帯の脱北者・キリスト教ブローカー・北朝鮮系米国少年を描き、北朝鮮ディアスポラ文学の英語化を達成した。",
    background="2010年代半ば北朝鮮脱北者問題の世界的注目。",
    development="北朝鮮ディアスポラ英語小説の代表作となった。",
    historical_context="2010年代半ば北朝鮮人権運動高揚期。",
    primary_source_url=WIKI_EN+"How_I_Became_a_North_Korean",
    primary_source_type="Wikipedia: How I Became a North Korean",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジャニス・Y・K・リー『ピアノ教師』",
    name_en="Janice Y. K. Lee's The Piano Teacher",
    name_original="The Piano Teacher", period_key="グローバル・ディアスポラ期",
    definition="ジャニス・Y・K・リーが2009年に発表したデビュー長編。1940年代日本占領下香港のピアノ教師と1950年代英人駐在員夫人を交差させ、香港ディアスポラ文学を米国市場で確立した。",
    background="2000年代末香港ディアスポラ作家の英語小説興隆。",
    development="NY Times ベストセラーとなり香港歴史小説の代表作となった。",
    historical_context="2000年代末香港返還後10年の文学的回顧期。",
    primary_source_url=WIKI_EN+"The_Piano_Teacher_(Lee_novel)",
    primary_source_type="Wikipedia: The Piano Teacher",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アレクサンダー・チー『エディンバラ』",
    name_en="Alexander Chee's Edinburgh",
    name_original="Edinburgh", period_key="ポストコロニアル・ディアスポラ期",
    definition="アレクサンダー・チー（1967-）が2001年に発表したデビュー長編。韓国系米国少年の合唱団指導者性虐待トラウマを描き、韓国系米国クィア文学とトラウマ文学を融合した。",
    background="2000年代初頭韓国系米国クィア作家の創作興隆。",
    development="米国クィア・ディアスポラ文学の重要新人作となった。",
    historical_context="2000年代初頭米国クィア・エスニック文学興隆期。",
    primary_source_url=WIKI_EN+"Alexander_Chee",
    primary_source_type="Wikipedia: Alexander Chee",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アレクサンダー・チー『夜の女王』",
    name_en="Alexander Chee's The Queen of the Night",
    name_original="The Queen of the Night", period_key="グローバル・ディアスポラ期",
    definition="チーが2016年に発表した長編。19世紀パリの歌手リリエの歴史小説で、韓国系米国クィア作家による西洋オペラ史の文学化を達成した。",
    background="2010年代半ば韓国系米国クィア作家の歴史小説への展開。",
    development="チーの最も野心的な歴史小説となった。",
    historical_context="2010年代半ばクィア歴史小説興隆期。",
    primary_source_url=WIKI_EN+"The_Queen_of_the_Night",
    primary_source_type="Wikipedia: The Queen of the Night",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ドン・ミ・チェ『DMZコロニー』",
    name_en="Don Mee Choi's DMZ Colony",
    name_original="DMZ Colony", period_key="グローバル・ディアスポラ期",
    definition="ドン・ミ・チェ（1962-）が2020年に発表した詩集。韓国DMZ・米軍基地・植民地記憶を多言語・多形式で展開し、全米図書賞詩部門を受賞した。",
    background="2020年代韓国系米国実験詩興隆。",
    development="アジア系米国実験詩の頂点となり、テレサ・チャ『ディクテ』の継承を確立した。",
    historical_context="2020年代米軍基地問題と韓国詩学の交差期。",
    primary_source_url=WIKI_EN+"Don_Mee_Choi",
    primary_source_type="Wikipedia: Don Mee Choi",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"多言語・多形式詩学は、AI多言語生成詩の理論的祖型。",
         "related_ai_phenomenon":"AI多言語詩生成"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"植民地詩学",
         "description":"チェの詩学は詩学理論の植民地・帝国研究と並行する。"}])


# ============================================================
# D: Indian diaspora deep — Rushdie/Seth/Desai/Ghosh (16)
# ============================================================
add(**C, name_ja="サルマン・ラシュディ『真夜中の子供たち』",
    name_en="Salman Rushdie's Midnight's Children",
    name_original="Midnight's Children", period_key="ポストコロニアル・ディアスポラ期",
    definition="サルマン・ラシュディ（1947-）が1981年に発表した長編。1947年8月15日のインド独立瞬間に生まれた1001人の子供たちのテレパシー連帯を描き、ブッカー賞受賞・「ブッカー・オブ・ブッカーズ」も獲得したポストコロニアル文学の最高峰。",
    background="1970年代末ラシュディのインド独立史への文学的応答。",
    development="ポストコロニアル文学の規範となり、世代を超えて影響力を保つ。",
    historical_context="1980年代初頭インド・ディアスポラ作家の世界文学化期。",
    primary_source_url=WIKI_EN+"Midnight%27s_Children",
    primary_source_type="Wikipedia: Midnight's Children",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"テレパシー連帯主体は、AI集合知の文学的祖型として読める。",
         "related_ai_phenomenon":"AI集合知主体"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"集合的意識",
         "description":"ラシュディの集合主体はインド哲学アートマンと近代主体の融合。"}])

add(**C, name_ja="サルマン・ラシュディ『悪魔の詩』",
    name_en="Salman Rushdie's The Satanic Verses",
    name_original="The Satanic Verses", period_key="ポストコロニアル・ディアスポラ期",
    definition="ラシュディが1988年に発表した長編。インド系英国移民の二人の物語と並行的なイスラム史想像を融合させ、1989年ホメイニ師のファトワーを引き起こしポストコロニアル文学最大の論争作となった。",
    background="1980年代末英国インド系ディアスポラと宗教論争の交差。",
    development="ファトワー事件はラシュディを10年以上の隠遁に追いやり、世界文学と宗教の関係を根本的に変えた。",
    historical_context="1989年ベルリン壁崩壊と並ぶ文化史転換点。",
    primary_source_url=WIKI_EN+"The_Satanic_Verses",
    primary_source_type="Wikipedia: The Satanic Verses",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="サルマン・ラシュディ『恥』",
    name_en="Salman Rushdie's Shame",
    name_original="Shame", period_key="ポストコロニアル・ディアスポラ期",
    definition="ラシュディが1983年に発表した長編。パキスタン政治史を架空国家「Q」の物語として展開し、ベナジル・ブットとジア・ウル・ハクの暗示的肖像で南アジア政治批判を達成した。",
    background="1980年代初頭パキスタン軍政期のラシュディの政治批判。",
    development="ラシュディの三大初期長編（『真夜中』『恥』『悪魔の詩』）の中核作。",
    historical_context="1980年代初頭パキスタン軍政批判期。",
    primary_source_url=WIKI_EN+"Shame_(Rushdie_novel)",
    primary_source_type="Wikipedia: Shame",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サルマン・ラシュディ『フィレンツェの女妖術師』",
    name_en="Salman Rushdie's The Enchantress of Florence",
    name_original="The Enchantress of Florence", period_key="グローバル・ディアスポラ期",
    definition="ラシュディが2008年に発表した長編。ムガル帝国アクバル帝の宮廷とメディチ家フィレンツェを物語と歴史で結ぶ実験作で、グローバルなインド・西洋接触史を文学化した。",
    background="2000年代末ラシュディの歴史小説への展開。",
    development="ブッカー賞最終候補となった。",
    historical_context="2000年代末グローバル歴史小説興隆期。",
    primary_source_url=WIKI_EN+"The_Enchantress_of_Florence",
    primary_source_type="Wikipedia: The Enchantress of Florence",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サルマン・ラシュディ『勝利の都』",
    name_en="Salman Rushdie's Victory City",
    name_original="Victory City", period_key="グローバル・ディアスポラ期",
    definition="ラシュディが2023年に発表した長編。14世紀南インド・ヴィジャヤナガル帝国を女性詩人が予言する叙事詩で、襲撃直前に完成した晩期代表作。",
    background="2020年代ラシュディの南インド歴史回帰。",
    development="2022年襲撃事件直前の完成作として注目された。",
    historical_context="2020年代インド歴史回顧文学期。",
    primary_source_url=WIKI_EN+"Victory_City",
    primary_source_type="Wikipedia: Victory City",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サルマン・ラシュディ『ナイフ』",
    name_en="Salman Rushdie's Knife",
    name_original="Knife", period_key="グローバル・ディアスポラ期",
    definition="ラシュディが2024年に発表した回想録。2022年8月のニューヨーク州での襲撃事件と回復過程を綴り、35年間のファトワー後の文学者の覚悟を提示した。",
    background="2022年襲撃事件の文学的応答。",
    development="ラシュディ晩年の重要自伝として批評的注目を集めた。",
    historical_context="2024年襲撃事件後の文学検閲論議期。",
    primary_source_url=WIKI_EN+"Knife_(Rushdie_book)",
    primary_source_type="Wikipedia: Knife",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴィクラム・セット『相応しい少年』",
    name_en="Vikram Seth's A Suitable Boy",
    name_original="A Suitable Boy", period_key="ポストコロニアル・ディアスポラ期",
    definition="ヴィクラム・セット（1952-）が1993年に発表した1349頁の超長編。1951-52年独立直後インドの結婚相手探しを4家族で描き、英語小説史上最長級のインド・ディアスポラ叙事詩。",
    background="1990年代初頭インド系ディアスポラ作家の長編大作興隆。",
    development="2020年BBC連続ドラマ化されインド英語小説の規範となった。",
    historical_context="1990年代初頭インド経済自由化下の歴史小説興隆期。",
    primary_source_url=WIKI_EN+"A_Suitable_Boy",
    primary_source_type="Wikipedia: A Suitable Boy",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ヴィクラム・セット『等しい音楽』",
    name_en="Vikram Seth's An Equal Music",
    name_original="An Equal Music", period_key="ポストコロニアル・ディアスポラ期",
    definition="セットが1999年に発表した長編。ロンドンのバイオリニストとピアニストの再会と別離を描き、ディアスポラ作家による西洋クラシック音楽世界の文学化を達成した。",
    background="1990年代末セットの英国移住と音楽愛の文学化。",
    development="セットの音楽小説の代表作となった。",
    historical_context="1990年代末英国インド系作家の越境期。",
    primary_source_url=WIKI_EN+"An_Equal_Music",
    primary_source_type="Wikipedia: An Equal Music",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アニタ・デサイ『清き朝の光』",
    name_en="Anita Desai's Clear Light of Day",
    name_original="Clear Light of Day", period_key="ポストコロニアル・ディアスポラ期",
    definition="アニタ・デサイ（1937-）が1980年に発表した長編。1947年印パ分離期のオールド・デリーで成長した姉妹の再会を描き、英語インド女性ディアスポラ文学の礎石となった。",
    background="1980年代初頭インド系ディアスポラ女性作家の創成期。",
    development="ブッカー賞最終候補となりインド英語女性文学の規範作となった。",
    historical_context="1980年代初頭インド・ディアスポラ女性文学興隆期。",
    primary_source_url=WIKI_EN+"Clear_Light_of_Day",
    primary_source_type="Wikipedia: Clear Light of Day",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アニタ・デサイ『山の火』",
    name_en="Anita Desai's Fire on the Mountain",
    name_original="Fire on the Mountain", period_key="ポストコロニアル・ディアスポラ期",
    definition="デサイが1977年に発表した長編。引退した老女が訪れる曾孫の話を中心に、女性の孤独と暴力を描いたインド英語女性心理小説の代表作。",
    background="1970年代末インド英語女性心理小説興隆。",
    development="サヒティヤ・アカデミ賞受賞しデサイの代表作となった。",
    historical_context="1970年代末インド女性文学の心理化期。",
    primary_source_url=WIKI_EN+"Fire_on_the_Mountain_(novel)",
    primary_source_type="Wikipedia: Fire on the Mountain",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="キラン・デサイ『損失の継承』",
    name_en="Kiran Desai's The Inheritance of Loss",
    name_original="The Inheritance of Loss", period_key="グローバル・ディアスポラ期",
    definition="キラン・デサイ（1971-）が2006年に発表した長編。北東インド・ヒマラヤ麓のグルカ独立運動を背景に、退職判事・孫娘・NY不法移民の物語を交差させ、ブッカー賞を受賞した。",
    background="2000年代半ばインド系ディアスポラ女性作家の世界文学化。",
    development="2006年ブッカー賞でアニタ・デサイの娘として最年少受賞者となった。",
    historical_context="2000年代半ばグローバル不法移民問題期。",
    primary_source_url=WIKI_EN+"The_Inheritance_of_Loss",
    primary_source_type="Wikipedia: The Inheritance of Loss",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ロヒントン・ミストリー『精妙な均衡』",
    name_en="Rohinton Mistry's A Fine Balance",
    name_original="A Fine Balance", period_key="ポストコロニアル・ディアスポラ期",
    definition="ロヒントン・ミストリー（1952-）が1995年に発表した長編。1975年インディラ・ガンディーの非常事態下のボンベイで四人が共生する物語で、パールシー系ディアスポラ作家による現代インド史の最高峰小説。",
    background="1990年代半ばカナダ・インド系パールシー作家の歴史小説興隆。",
    development="ブッカー賞最終候補となり世界文学的に評価された。",
    historical_context="1990年代半ば非常事態時代の歴史回顧期。",
    primary_source_url=WIKI_EN+"A_Fine_Balance",
    primary_source_type="Wikipedia: A Fine Balance",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="アミタヴ・ゴーシュ『ガラスの宮殿』",
    name_en="Amitav Ghosh's The Glass Palace",
    name_original="The Glass Palace", period_key="ポストコロニアル・ディアスポラ期",
    definition="アミタヴ・ゴーシュ（1956-）が2000年に発表した長編。1885年英ビルマ王国併合から第二次大戦までのビルマ・インド・マレー三世代家族史を描き、東南アジア・ディアスポラ史の文学的礎石となった。",
    background="2000年ゴーシュの東南アジア史への展開。",
    development="ゴーシュの『海の罌粟三部作』への礎石作となった。",
    historical_context="2000年東南アジア歴史小説興隆期。",
    primary_source_url=WIKI_EN+"The_Glass_Palace",
    primary_source_type="Wikipedia: The Glass Palace",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"インド洋世界",
         "description":"ゴーシュのインド洋ネットワーク描写は人類学的世界システム研究と並行する。"}])

add(**C, name_ja="アミタヴ・ゴーシュ『海の罌粟』",
    name_en="Amitav Ghosh's Sea of Poppies",
    name_original="Sea of Poppies", period_key="グローバル・ディアスポラ期",
    definition="ゴーシュが2008年に発表した『罌粟海三部作』第一部。1838年阿片戦争前夜のガンガー河とインド洋を舞台に、年期奉公労働者・女性・水夫の交差を描いたインド洋ディアスポラ叙事詩。",
    background="2000年代末ゴーシュの大西洋に対するインド洋世界の文学化。",
    development="三部作（『海の罌粟』『罌粟河』『罌粟洪水』）の大規模インド洋史プロジェクトとなった。",
    historical_context="2000年代末グローバル海洋史興隆期。",
    primary_source_url=WIKI_EN+"Sea_of_Poppies",
    primary_source_type="Wikipedia: Sea of Poppies",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ピジン・ラスカリ・諸言語混淆は、AI多言語生成の文学的祖型。",
         "related_ai_phenomenon":"AI多言語混淆生成"}])

add(**C, name_ja="アミタヴ・ゴーシュ『銃の島』",
    name_en="Amitav Ghosh's Gun Island",
    name_original="Gun Island", period_key="グローバル・ディアスポラ期",
    definition="ゴーシュが2019年に発表した長編。ベンガル神話の蛇女神とイタリア難民危機を交差させ、気候危機・移民・神話を統合したエコクライメート・ディアスポラ小説。",
    background="2010年代末気候危機文学とエコクリティシズムの興隆。",
    development="ゴーシュの気候フィクションとしての代表作となった。",
    historical_context="2010年代末グローバル気候危機文学興隆期。",
    primary_source_url=WIKI_EN+"Gun_Island",
    primary_source_type="Wikipedia: Gun Island",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"気候とディアスポラ",
         "description":"ゴーシュの気候難民論は環境人類学のディアスポラ研究と並行する。"}])

add(**C, name_ja="アミタヴ・ゴーシュ『ナツメグの呪い』",
    name_en="Amitav Ghosh's The Nutmeg's Curse",
    name_original="The Nutmeg's Curse", period_key="グローバル・ディアスポラ期",
    definition="ゴーシュが2021年に発表した理論書。17世紀バンダ諸島ナツメグ大量虐殺から始めて、植民地主義・気候危機・地球の運命を結合したディアスポラ批評の代表作。",
    background="2020年代植民地・気候危機批評の融合期。",
    development="気候危機論議の重要文献となった。",
    historical_context="2020年代脱植民地・気候批評融合期。",
    primary_source_url=WIKI_EN+"Amitav_Ghosh",
    primary_source_type="Wikipedia: Amitav Ghosh",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"地球倫理",
         "description":"ゴーシュの地球倫理論はチャクラバルティらの惑星哲学と並行する。"}])


# ============================================================
# E: Indian diaspora — Mukherjee/Sharma/James/etc (8)
# ============================================================
add(**C, name_ja="バーラティ・ムケルジー『ジャスミン』",
    name_en="Bharati Mukherjee's Jasmine",
    name_original="Jasmine", period_key="ポストコロニアル・ディアスポラ期",
    definition="バーラティ・ムケルジー（1940-2017）が1989年に発表した長編。パンジャブ村娘ジョーティが米国アイオワ農村を経て西海岸へ向かう物語で、米国南アジア系移民女性文学の礎石となった。",
    background="1980年代末米国南アジア系移民女性文学興隆。",
    description=None,
    development="米国インド系ディアスポラ女性文学の規範作となった。",
    historical_context="1980年代末米国インド系移民増加期。",
    primary_source_url=WIKI_EN+"Jasmine_(novel)",
    primary_source_type="Wikipedia: Jasmine",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アキル・シャルマ『家族の生活』",
    name_en="Akhil Sharma's Family Life",
    name_original="Family Life", period_key="グローバル・ディアスポラ期",
    definition="アキル・シャルマ（1971-）が2014年に発表した自伝的長編。8歳で米国移住したインド少年と兄の事故による永久障害後の家族崩壊を描き、フォリオ賞を受賞した。",
    background="2010年代米国インド系第二世代男性作家のトラウマ文学興隆。",
    development="2014年フォリオ賞受賞しインド系米国文学の頂点に達した。",
    historical_context="2010年代米国インド系トラウマ文学興隆期。",
    primary_source_url=WIKI_EN+"Family_Life_(Sharma_novel)",
    primary_source_type="Wikipedia: Family Life",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アキル・シャルマ『従順な父』",
    name_en="Akhil Sharma's An Obedient Father",
    name_original="An Obedient Father", period_key="ポストコロニアル・ディアスポラ期",
    definition="シャルマが2000年に発表したデビュー長編。デリーの汚職役人と娘の関係を娘への性虐待を含む形で容赦なく描き、PEN/ヘミングウェイ賞受賞しインド系米国文学に新たな倫理的水準を導入した。",
    background="2000年代初頭インド系米国男性作家の倫理的硬骨さ。",
    development="2001年PEN/ヘミングウェイ賞受賞した。",
    historical_context="2000年代初頭インド英語ノワール興隆期。",
    primary_source_url=WIKI_EN+"An_Obedient_Father",
    primary_source_type="Wikipedia: An Obedient Father",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ターニャ・ジェイムズ『傷つけた牙』",
    name_en="Tania James's The Tusk That Did the Damage",
    name_original="The Tusk That Did the Damage", period_key="グローバル・ディアスポラ期",
    definition="ターニャ・ジェイムズが2015年に発表した長編。南インドの密猟されたゾウの視点・ドキュメンタリー作家・密猟者の三声で展開し、インド系米国エコフィクションを確立した。",
    background="2010年代半ばインド系米国エコフィクション興隆。",
    development="米国インド系ディアスポラ動物文学の代表作となった。",
    historical_context="2010年代半ばインド野生動物保護論議期。",
    primary_source_url=WIKI_EN+"Tania_James",
    primary_source_type="Wikipedia: Tania James",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ターニャ・ジェイムズ『戦利品』",
    name_en="Tania James's Loot",
    name_original="Loot", period_key="グローバル・ディアスポラ期",
    definition="ジェイムズが2023年に発表した長編。18世紀ティプー・スルタン宮廷の機械工アッバスを主人公に、インド─フランス─英国の旅と植民地略奪を描いた。",
    background="2020年代インド系米国歴史小説興隆。",
    development="ジェイムズの代表的歴史小説となった。",
    historical_context="2020年代植民地略奪返還論議期。",
    primary_source_url=WIKI_EN+"Tania_James",
    primary_source_type="Wikipedia: Tania James",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カラン・マハジャン『小爆弾の協会』",
    name_en="Karan Mahajan's The Association of Small Bombs",
    name_original="The Association of Small Bombs", period_key="グローバル・ディアスポラ期",
    definition="カラン・マハジャン（1984-）が2016年に発表した長編。1996年デリー市場での小規模テロ爆発の被害者・加害者・遺族を多視点で描き、ポストコロニアル・テロ文学を確立した。",
    background="2010年代半ばインド系米国テロ文学興隆。",
    development="全米図書批評家賞最終候補となった。",
    historical_context="2010年代半ばインド・テロ問題の文学化期。",
    primary_source_url=WIKI_EN+"The_Association_of_Small_Bombs",
    primary_source_type="Wikipedia: The Association of Small Bombs",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# F: Caribbean expanded (10)
# ============================================================
add(**C, name_ja="V・S・ナイポール『世界の道』",
    name_en="V. S. Naipaul's A Way in the World",
    name_original="A Way in the World", period_key="ポストコロニアル・ディアスポラ期",
    definition="V・S・ナイポール（1932-2018）が1994年に発表した小説兼自伝。トリニダード・英国・南米を巡る9つの物語でカリブ・ディアスポラ作家の旅を綴り、晩期ナイポールの形式実験を体現した。",
    background="1990年代半ばナイポールの自伝的旅行文学への展開。",
    development="ナイポール晩期の代表作となった。",
    historical_context="1990年代半ばカリブ・ディアスポラ作家の自伝化期。",
    primary_source_url=WIKI_EN+"A_Way_in_the_World",
    primary_source_type="Wikipedia: A Way in the World",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="V・S・ナイポール『半生』",
    name_en="V. S. Naipaul's Half a Life",
    name_original="Half a Life", period_key="グローバル・ディアスポラ期",
    definition="ナイポールが2001年に発表した長編。インド人ヒンドゥー教徒の青年がロンドン・ポルトガル領東アフリカを彷徨う半生を描き、ノーベル賞受賞年の代表作となった。",
    background="2001年ナイポールのノーベル賞受賞期の作品。",
    development="続編『マジック・シーズ』(2004)を生み出した。",
    historical_context="2001年ノーベル文学賞受賞期。",
    primary_source_url=WIKI_EN+"Half_a_Life_(novel)",
    primary_source_type="Wikipedia: Half a Life",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="サム・セルヴォン『モーゼ・アセンディング』",
    name_en="Sam Selvon's Moses Ascending",
    name_original="Moses Ascending", period_key="ポストコロニアル・ディアスポラ期",
    definition="サム・セルヴォン（1923-1994）が1975年に発表した長編。『孤独なロンドン人』のモーゼが地主となる続編で、カリブ・ディアスポラの階級昇進と幻滅を描いた。",
    background="1970年代英国カリブ系第一世代の階級変動。",
    development="セルヴォンのモーゼ三部作の中核作となった。",
    historical_context="1970年代英国カリブ・ディアスポラ階級論議期。",
    primary_source_url=WIKI_EN+"Sam_Selvon",
    primary_source_type="Wikipedia: Sam Selvon",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フレッド・ダグィアール『最も長い記憶』",
    name_en="Fred D'Aguiar's The Longest Memory",
    name_original="The Longest Memory", period_key="ポストコロニアル・ディアスポラ期",
    definition="フレッド・ダグィアール（1960-）が1994年に発表したデビュー長編。1810年ヴァージニアの逃亡奴隷少年と老父の物語を多視点で描き、デイビッド・ハイアム賞・ホワイトブレッド初作賞を受賞した。",
    background="1990年代半ば英国カリブ系作家の奴隷制歴史小説興隆。",
    development="英国カリブ・ディアスポラ歴史小説の代表作となった。",
    historical_context="1990年代半ば奴隷制200年記憶論議期。",
    primary_source_url=WIKI_EN+"Fred_D%27Aguiar",
    primary_source_type="Wikipedia: Fred D'Aguiar",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カリル・フィリップス『最終航路』",
    name_en="Caryl Phillips's The Final Passage",
    name_original="The Final Passage", period_key="ポストコロニアル・ディアスポラ期",
    definition="カリル・フィリップス（1958-）が1985年に発表したデビュー長編。1958年カリブ女性レイラの英国渡航と幻滅を描き、Windrush世代英国カリブ・ディアスポラ文学を確立した。",
    background="1980年代半ば英国カリブ系第二世代の歴史小説興隆。",
    development="英国カリブ・ディアスポラ女性文学の創成作となった。",
    historical_context="1980年代半ばWindrush世代回顧期。",
    primary_source_url=WIKI_EN+"Caryl_Phillips",
    primary_source_type="Wikipedia: Caryl Phillips",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カリル・フィリップス『血の本質』",
    name_en="Caryl Phillips's The Nature of Blood",
    name_original="The Nature of Blood", period_key="ポストコロニアル・ディアスポラ期",
    definition="フィリップスが1997年に発表した長編。15世紀ヴェネツィアのオセロ・ホロコースト・現代カリブ系を結合した複合的歴史小説で、カリブとユダヤ・ディアスポラを並行させた。",
    background="1990年代末カリブ・ユダヤ並行ディアスポラ批評の興隆。",
    development="フィリップスの最も野心的構造作となった。",
    historical_context="1990年代末ホロコースト記憶論議期。",
    primary_source_url=WIKI_EN+"The_Nature_of_Blood",
    primary_source_type="Wikipedia: The Nature of Blood",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マーロン・ジェイムズ『夜の女たちの書』",
    name_en="Marlon James's The Book of Night Women",
    name_original="The Book of Night Women", period_key="グローバル・ディアスポラ期",
    definition="マーロン・ジェイムズ（1970-）が2009年に発表した長編。19世紀初頭ジャマイカ砂糖プランテーションの女奴隷ライラスの物語を奴隷英語で描き、奴隷制女性史を文学化した。",
    background="2000年代末ジャマイカ系作家による奴隷制女性史回帰。",
    development="ダゲン・ローレンス賞受賞しジェイムズの最初の世界的成功作となった。",
    historical_context="2000年代末ジャマイカ系作家世界文学化期。",
    primary_source_url=WIKI_EN+"The_Book_of_Night_Women",
    primary_source_type="Wikipedia: The Book of Night Women",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マーロン・ジェイムズ『黒豹、赤狼』",
    name_en="Marlon James's Black Leopard, Red Wolf",
    name_original="Black Leopard, Red Wolf", period_key="グローバル・ディアスポラ期",
    definition="ジェイムズが2019年に発表した『暗き星三部作』第一部。アフリカ神話を基盤にした幻想叙事詩で、ジャマイカ系作家によるアフリカ文学伝統への回帰を達成した。",
    background="2010年代末ディアスポラ作家のアフリカ幻想叙事詩興隆。",
    development="アフリカ系ディアスポラのファンタジー小説の頂点と評価された。",
    historical_context="2010年代末アフリカ系ファンタジー文学興隆期。",
    primary_source_url=WIKI_EN+"Black_Leopard,_Red_Wolf",
    primary_source_type="Wikipedia: Black Leopard, Red Wolf",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ケイ・ミラー『シオンへの道を地図にしようとする地図学者』",
    name_en="Kei Miller's The Cartographer Tries to Map a Way to Zion",
    name_original="The Cartographer Tries to Map a Way to Zion",
    period_key="グローバル・ディアスポラ期",
    definition="ケイ・ミラー（1978-）が2014年に発表した詩集。植民地測量と現地ラスタファリ宇宙論の対話形式で、ジャマイカ系英国詩人による植民地批判詩学を確立した。",
    background="2010年代半ばジャマイカ系英国詩人の植民地批判詩学興隆。",
    development="フォワード賞受賞しカリブ詩学の代表作となった。",
    historical_context="2010年代半ばジャマイカ独立50年期。",
    primary_source_url=WIKI_EN+"Kei_Miller",
    primary_source_type="Wikipedia: Kei Miller",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"植民地測量批判",
         "description":"ミラーの植民地測量批判は詩学理論の脱植民地論と並行する。"}])


# ============================================================
# G: Black British detailed (8)
# ============================================================
add(**C, name_ja="ベルナーディン・エヴァリスト『ローラ』",
    name_en="Bernardine Evaristo's Lara",
    name_original="Lara", period_key="ポストコロニアル・ディアスポラ期",
    definition="ベルナーディン・エヴァリスト（1959-）が1997年に発表した自伝的詩小説。ナイジェリア人父・英国人母の混血少女ローラの自己発見を韻文で描き、英国黒人女性ディアスポラ詩小説を確立した。",
    background="1990年代末英国黒人女性作家の韻文長編興隆。",
    development="エヴァリストの『ガール、ウーマン、アザー』への礎石作となった。",
    historical_context="1990年代末英国黒人女性詩学興隆期。",
    primary_source_url=WIKI_EN+"Bernardine_Evaristo",
    primary_source_type="Wikipedia: Bernardine Evaristo",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ベルナーディン・エヴァリスト『金髪のルーツ』",
    name_en="Bernardine Evaristo's Blonde Roots",
    name_original="Blonde Roots", period_key="グローバル・ディアスポラ期",
    definition="エヴァリストが2008年に発表した代替歴史長編。アフリカ人がヨーロッパ人を奴隷にする逆転世界を描き、奴隷制歴史小説に皮肉な批評を導入した。",
    background="2000年代末英国黒人女性作家の代替歴史実験。",
    development="奴隷制風刺文学の代表作となった。",
    historical_context="2000年代末奴隷制歴史記憶論議期。",
    primary_source_url=WIKI_EN+"Blonde_Roots",
    primary_source_type="Wikipedia: Blonde Roots",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ベルナーディン・エヴァリスト『マニフェスト』",
    name_en="Bernardine Evaristo's Manifesto",
    name_original="Manifesto", period_key="グローバル・ディアスポラ期",
    definition="エヴァリストが2021年に発表した回想録兼マニフェスト。40年の作家活動と英国黒人女性文学運動の証言で、ブッカー賞共同受賞作家による文化批評を展開した。",
    background="2019年エヴァリストの『ガール、ウーマン、アザー』ブッカー賞共同受賞後の回想。",
    development="英国黒人女性文学史の重要文献となった。",
    historical_context="2020年代英国黒人女性作家の世界文学化期。",
    primary_source_url=WIKI_EN+"Manifesto_(book)",
    primary_source_type="Wikipedia: Manifesto",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ハニフ・クレイシ『黒のアルバム』",
    name_en="Hanif Kureishi's The Black Album",
    name_original="The Black Album", period_key="ポストコロニアル・ディアスポラ期",
    definition="ハニフ・クレイシ（1954-）が1995年に発表した長編。1989年ラシュディ事件下のロンドン大学での南アジア系青年とイスラム原理主義者の関係を描き、英国南アジア系世代論争を主題化した。",
    background="1990年代半ば英国ムスリム南アジア系青年の宗教化と世俗化対立。",
    development="ラシュディ事件後の英国ムスリム文学の代表作となった。",
    historical_context="1990年代半ば英国ラシュディ事件後遺症期。",
    primary_source_url=WIKI_EN+"The_Black_Album_(novel)",
    primary_source_type="Wikipedia: The Black Album",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ハニフ・クレイシ『親密』",
    name_en="Hanif Kureishi's Intimacy",
    name_original="Intimacy", period_key="ポストコロニアル・ディアスポラ期",
    definition="クレイシが1998年に発表した中編。家族を捨てる夜を語る男の独白で、英国南アジア系男性の中年危機と倫理を主題化した実験的告白小説。",
    background="1990年代末英国南アジア系男性中年文学興隆。",
    development="クレイシの最も個人的な実験作となった。",
    historical_context="1990年代末英国男性告白文学興隆期。",
    primary_source_url=WIKI_EN+"Intimacy_(novella)",
    primary_source_type="Wikipedia: Intimacy",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ダイアナ・エヴァンス『26a』",
    name_en="Diana Evans's 26a",
    name_original="26a", period_key="グローバル・ディアスポラ期",
    definition="ダイアナ・エヴァンス（1972-）が2005年に発表したデビュー長編。ナイジェリア英国混血の双子姉妹を描き、英国黒人女性新世代ディアスポラ文学を確立した。",
    background="2000年代半ば英国黒人女性新世代作家の興隆。",
    development="ベイリーズ女性小説賞受賞しエヴァンス代表作となった。",
    historical_context="2000年代半ば英国黒人女性新世代文学興隆期。",
    primary_source_url=WIKI_EN+"Diana_Evans",
    primary_source_type="Wikipedia: Diana Evans",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ダイアナ・エヴァンス『普通の人々』",
    name_en="Diana Evans's Ordinary People",
    name_original="Ordinary People", period_key="グローバル・ディアスポラ期",
    definition="エヴァンスが2018年に発表した長編。2008年オバマ当選後のロンドン中産階級黒人カップル二組の関係を描き、英国黒人ミドルクラス文学を確立した。",
    background="2010年代末英国黒人ミドルクラス文学興隆。",
    development="フェミニズム賞・コスタ小説賞最終候補となった。",
    historical_context="2010年代末英国黒人中産階級文学興隆期。",
    primary_source_url=WIKI_EN+"Diana_Evans",
    primary_source_type="Wikipedia: Diana Evans",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヘレン・オエイェミ『白は魔女のために』",
    name_en="Helen Oyeyemi's White Is for Witching",
    name_original="White Is for Witching", period_key="グローバル・ディアスポラ期",
    definition="ヘレン・オエイェミ（1984-）が2009年に発表した長編。ナイジェリア系英国少女の家屋を語り手にしたゴシック幻想で、英国黒人女性ゴシック・ディアスポラ文学を確立した。",
    background="2000年代末英国黒人女性ゴシック小説興隆。",
    development="サマセット・モーム賞受賞しオエイェミの最重要作の一つとなった。",
    historical_context="2000年代末英国黒人女性ゴシック小説興隆期。",
    primary_source_url=WIKI_EN+"White_Is_for_Witching",
    primary_source_type="Wikipedia: White Is for Witching",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"家屋を語り手とする物語論は、AI環境主体の文学的祖型。",
         "related_ai_phenomenon":"AI環境主体性"}])


# ============================================================
# H: Jewish Diaspora deeper — Bellow/Malamud/Roth (12)
# ============================================================
add(**C, name_ja="ソール・ベロー『オーギー・マーチの冒険』",
    name_en="Saul Bellow's The Adventures of Augie March",
    name_original="The Adventures of Augie March", period_key="脱植民地・初期移民文学期",
    definition="ソール・ベロー（1915-2005）が1953年に発表した長編。シカゴのユダヤ系少年オーギーのピカレスク的成長物語で、米国ユダヤ系小説を主流文学に押し上げ全米図書賞を受賞した。",
    background="1950年代米国ユダヤ系作家の主流化。",
    development="米国ユダヤ系小説の規範となり後にノーベル賞へ繋がった。",
    historical_context="1950年代戦後米国ユダヤ系黄金期。",
    primary_source_url=WIKI_EN+"The_Adventures_of_Augie_March",
    primary_source_type="Wikipedia: The Adventures of Augie March",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ソール・ベロー『雨の王ヘンダソン』",
    name_en="Saul Bellow's Henderson the Rain King",
    name_original="Henderson the Rain King", period_key="脱植民地・初期移民文学期",
    definition="ベローが1959年に発表した長編。中年米国WASP男性が架空アフリカで精神的覚醒を求める物語で、ベローによる白人主人公実験作・米国ユダヤ作家のアフリカ想像の記念碑作。",
    background="1950年代末ユダヤ作家による白人主人公実験。",
    development="ベロー中期の代表作となった。",
    historical_context="1950年代末アフリカ独立運動期。",
    primary_source_url=WIKI_EN+"Henderson_the_Rain_King",
    primary_source_type="Wikipedia: Henderson the Rain King",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ソール・ベロー『フンボルトの贈り物』",
    name_en="Saul Bellow's Humboldt's Gift",
    name_original="Humboldt's Gift", period_key="ポストコロニアル・ディアスポラ期",
    definition="ベローが1975年に発表した長編。詩人デルモア・シュワルツをモデルにした友人フンボルトの追悼を含む小説家チャーリーの物語で、ピューリッツァー賞受賞・1976年ノーベル賞受賞へ繋がった。",
    background="1970年代米国ユダヤ作家の友情・芸術小説興隆。",
    development="1976年ノーベル文学賞受賞の決定打となった。",
    historical_context="1970年代後半米国ユダヤ系作家世界文学化期。",
    primary_source_url=WIKI_EN+"Humboldt%27s_Gift",
    primary_source_type="Wikipedia: Humboldt's Gift",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ソール・ベロー『ラヴェルスタイン』",
    name_en="Saul Bellow's Ravelstein",
    name_original="Ravelstein", period_key="グローバル・ディアスポラ期",
    definition="ベローが2000年に発表した最後の長編。哲学者アラン・ブルームをモデルにした表題人物の追悼で、シカゴ大学のユダヤ系知識人世界を描いた晩期傑作。",
    background="2000年ベローの最晩年作。",
    development="ベロー晩期の代表作として広く評価された。",
    historical_context="2000年代米国ユダヤ系知識人世代終末期。",
    primary_source_url=WIKI_EN+"Ravelstein",
    primary_source_type="Wikipedia: Ravelstein",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バーナード・マラマッド『魔法の樽』",
    name_en="Bernard Malamud's The Magic Barrel",
    name_original="The Magic Barrel", period_key="脱植民地・初期移民文学期",
    definition="バーナード・マラマッド（1914-1986）が1958年に発表した短編集。ユダヤ系移民の魔術的リアリズム的短編で、表題作含む全米図書賞受賞作。米国ユダヤ系短編の規範となった。",
    background="1950年代米国ユダヤ系移民第二世代の短編興隆。",
    development="米国ユダヤ系短編の規範となった。",
    historical_context="1950年代末米国ユダヤ系短編黄金期。",
    primary_source_url=WIKI_EN+"The_Magic_Barrel",
    primary_source_type="Wikipedia: The Magic Barrel",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="バーナード・マラマッド『ナチュラル』",
    name_en="Bernard Malamud's The Natural",
    name_original="The Natural", period_key="脱植民地・初期移民文学期",
    definition="マラマッドが1952年に発表したデビュー長編。野球選手ロイ・ホブズの物語を聖杯神話的に展開し、米国ユダヤ系作家による国民スポーツの神話的扱いを達成した。",
    background="1950年代米国ユダヤ系作家の国民神話への参入。",
    development="米国スポーツ小説の規範となった。",
    historical_context="1950年代米国ユダヤ系作家国民化期。",
    primary_source_url=WIKI_EN+"The_Natural",
    primary_source_type="Wikipedia: The Natural",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バーナード・マラマッド『テナント』",
    name_en="Bernard Malamud's The Tenants",
    name_original="The Tenants", period_key="ポストコロニアル・ディアスポラ期",
    definition="マラマッドが1971年に発表した長編。閉鎖直前のアパートメントでユダヤ作家とアフリカ系作家が対立する物語で、米国ユダヤ系・アフリカ系関係の緊張を主題化した。",
    background="1970年代米国ユダヤ系・アフリカ系作家関係論議。",
    development="エスニック間文学関係の代表作となった。",
    historical_context="1970年代米国エスニック間関係論議期。",
    primary_source_url=WIKI_EN+"The_Tenants",
    primary_source_type="Wikipedia: The Tenants",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フィリップ・ロス『ヒューマン・ステイン』",
    name_en="Philip Roth's The Human Stain",
    name_original="The Human Stain", period_key="グローバル・ディアスポラ期",
    definition="フィリップ・ロス（1933-2018）が2000年に発表した長編。古典学教授コールマン・シルクが実は混血黒人を隠して生きた物語で、ロス『アメリカ三部作』の頂点。",
    background="2000年代初頭米国人種・アイデンティティ政治の文学化。",
    development="ロスの21世紀代表作となった。",
    historical_context="1990年代末米国大統領弾劾問題期。",
    primary_source_url=WIKI_EN+"The_Human_Stain",
    primary_source_type="Wikipedia: The Human Stain",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"パッシング主体の構造は、AI生成アイデンティティの偽装可能性の祖型。",
         "related_ai_phenomenon":"AI生成アイデンティティ偽装"}])

add(**C, name_ja="フィリップ・ロス『反米陰謀』",
    name_en="Philip Roth's The Plot Against America",
    name_original="The Plot Against America", period_key="グローバル・ディアスポラ期",
    definition="ロスが2004年に発表した代替歴史長編。リンドバーグが1940年大統領選で勝利した米国でユダヤ系一家を迫害する架空史を描き、米国ファシズムの可能性を提示した。",
    background="2000年代半ばブッシュ政権下の代替歴史小説興隆。",
    development="2020年HBOミニシリーズ化されトランプ時代の警句として再評価された。",
    historical_context="2000年代半ば米国愛国法論議期。",
    primary_source_url=WIKI_EN+"The_Plot_Against_America",
    primary_source_type="Wikipedia: The Plot Against America",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="フィリップ・ロス『カウンターライフ』",
    name_en="Philip Roth's The Counterlife",
    name_original="The Counterlife", period_key="ポストコロニアル・ディアスポラ期",
    definition="ロスが1986年に発表した長編。ザッカーマン四部作の頂点で、ザッカーマン兄弟の対立と変奏を多重物語で展開し、全米図書批評家賞を受賞したロス中期傑作。",
    background="1980年代後半ロスの形式実験成熟。",
    development="ザッカーマン四部作の頂点となった。",
    historical_context="1980年代後半米国ユダヤ系作家形式実験期。",
    primary_source_url=WIKI_EN+"The_Counterlife",
    primary_source_type="Wikipedia: The Counterlife",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フィリップ・ロス『オペレーション・シャイロック』",
    name_en="Philip Roth's Operation Shylock",
    name_original="Operation Shylock", period_key="ポストコロニアル・ディアスポラ期",
    definition="ロスが1993年に発表した長編。「フィリップ・ロス」を名乗る男にエルサレムで会う「フィリップ・ロス」の物語で、ユダヤ・ディアスポラとアイデンティティの極限的探究を達成した。",
    background="1990年代初頭ロスのメタフィクション成熟。",
    development="ペン/フォークナー賞受賞しロスの最も実験的作の一つとなった。",
    historical_context="1990年代初頭イスラエル和平論議期。",
    primary_source_url=WIKI_EN+"Operation_Shylock",
    primary_source_type="Wikipedia: Operation Shylock",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"自己と分身の同居は、AI生成自己の問題の文学的祖型。",
         "related_ai_phenomenon":"AI生成自己と分身"}])


# ============================================================
# I: Krauss/Foer/Cohen/Chabon/Ozick (8)
# ============================================================
add(**C, name_ja="ニコール・クラウス『偉大なる家』",
    name_en="Nicole Krauss's Great House",
    name_original="Great House", period_key="グローバル・ディアスポラ期",
    definition="ニコール・クラウス（1974-）が2010年に発表した長編。チリ詩人の机を巡る四つの物語でユダヤ・ディアスポラの記憶と物の継承を描き、全米図書賞最終候補となった。",
    background="2010年代米国ユダヤ女性作家の物語実験。",
    development="クラウスの最も野心的構造作となった。",
    historical_context="2010年代初頭ユダヤ・ディアスポラ女性文学興隆期。",
    primary_source_url=WIKI_EN+"Great_House_(novel)",
    primary_source_type="Wikipedia: Great House",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ニコール・クラウス『暗い森』",
    name_en="Nicole Krauss's Forest Dark",
    name_original="Forest Dark", period_key="グローバル・ディアスポラ期",
    definition="クラウスが2017年に発表した長編。テルアビブで失踪する米国ユダヤ系男性とブルックリンの作家ニコールを並行させ、ユダヤ・ディアスポラ・カフカ・自己物語を融合した。",
    background="2010年代後半米国ユダヤ系女性作家の自伝的実験。",
    development="クラウス代表作の一つとして評価された。",
    historical_context="2010年代後半米国ユダヤ系自伝的小説興隆期。",
    primary_source_url=WIKI_EN+"Forest_Dark",
    primary_source_type="Wikipedia: Forest Dark",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジョナサン・サフラン・フォア『何もかも明るく照らされる』",
    name_en="Jonathan Safran Foer's Everything Is Illuminated",
    name_original="Everything Is Illuminated", period_key="グローバル・ディアスポラ期",
    definition="ジョナサン・サフラン・フォア（1977-）が2002年に発表したデビュー長編。米国の青年がウクライナで祖父をナチから救った女性を探す物語で、米国ユダヤ系第三世代のホロコースト記憶文学を刷新した。",
    background="2000年代初頭ホロコースト第三世代文学の興隆。",
    development="ガーディアン処女作賞受賞しフォアの世界的成功作となった。",
    historical_context="2000年代初頭米国ユダヤ系第三世代ホロコースト文学興隆期。",
    primary_source_url=WIKI_EN+"Everything_Is_Illuminated",
    primary_source_type="Wikipedia: Everything Is Illuminated",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"非母語話者の英語を語り手にする実験は、AI多言語生成の祖型。",
         "related_ai_phenomenon":"AI非母語生成"}])

add(**C, name_ja="ジョナサン・サフラン・フォア『私はここにいる』",
    name_en="Jonathan Safran Foer's Here I Am",
    name_original="Here I Am", period_key="グローバル・ディアスポラ期",
    definition="フォアが2016年に発表した長編。ワシントンDCのユダヤ系一家の崩壊と中東地震・イスラエル危機を交差させ、米国ユダヤ・ディアスポラとイスラエルの関係を主題化した。",
    background="2010年代半ば米国ユダヤ系・イスラエル関係の文学化。",
    development="フォアの中期代表作となった。",
    historical_context="2010年代半ば米国ユダヤ系・イスラエル関係論議期。",
    primary_source_url=WIKI_EN+"Here_I_Am_(novel)",
    primary_source_type="Wikipedia: Here I Am",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジョシュア・コーエン『ネタニヤフ家』",
    name_en="Joshua Cohen's The Netanyahus",
    name_original="The Netanyahus", period_key="グローバル・ディアスポラ期",
    definition="ジョシュア・コーエン（1980-）が2021年に発表した長編。1959年米国学院に来訪したベンジオン・ネタニヤフ（首相の父）一家を描き、2022年ピューリッツァー賞を受賞した。",
    background="2020年代米国ユダヤ系作家の歴史小説興隆。",
    development="2022年ピューリッツァー賞受賞しコーエンの世界的成功作となった。",
    historical_context="2020年代米国・イスラエル関係再考期。",
    primary_source_url=WIKI_EN+"The_Netanyahus",
    primary_source_type="Wikipedia: The Netanyahus",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="マイケル・シェイボン『ピッツバーグの謎』",
    name_en="Michael Chabon's The Mysteries of Pittsburgh",
    name_original="The Mysteries of Pittsburgh", period_key="ポストコロニアル・ディアスポラ期",
    definition="マイケル・シェイボン（1963-）が1988年に発表したデビュー長編。ピッツバーグ大学の若いユダヤ系男性主人公の物語で、米国ユダヤ系第三世代成長小説の代表作となった。",
    background="1980年代末米国ユダヤ系第三世代成長小説の興隆。",
    development="シェイボンの世界的成功への礎石作となった。",
    historical_context="1980年代末米国ユダヤ系青年文学興隆期。",
    primary_source_url=WIKI_EN+"The_Mysteries_of_Pittsburgh",
    primary_source_type="Wikipedia: The Mysteries of Pittsburgh",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マイケル・シェイボン『ユダヤ人警察組合』",
    name_en="Michael Chabon's The Yiddish Policemen's Union",
    name_original="The Yiddish Policemen's Union", period_key="グローバル・ディアスポラ期",
    definition="シェイボンが2007年に発表した代替歴史長編。1948年イスラエル建国失敗後、アラスカに60年期限のユダヤ自治区が成立した世界の探偵小説で、ヒューゴー賞・ネビュラ賞を受賞した。",
    background="2000年代後半米国ユダヤ系SF代替歴史興隆。",
    development="米国ユダヤ系SF・代替歴史の代表作となった。",
    historical_context="2000年代後半米国ユダヤ系想像力新興期。",
    primary_source_url=WIKI_EN+"The_Yiddish_Policemen%27s_Union",
    primary_source_type="Wikipedia: The Yiddish Policemen's Union",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"イディッシュ世界という代替言語空間は、AI生成代替言語の文学的祖型。",
         "related_ai_phenomenon":"AI代替言語空間生成"}])

add(**C, name_ja="マイケル・シェイボン『ムーングロウ』",
    name_en="Michael Chabon's Moonglow",
    name_original="Moonglow", period_key="グローバル・ディアスポラ期",
    definition="シェイボンが2016年に発表した長編。死の床の祖父の証言を再構成する自伝的フィクションで、米国ユダヤ系男性世代を月面宇宙開発・ホロコースト記憶と結合した。",
    background="2010年代半ば米国ユダヤ系作家の自伝的歴史化。",
    development="米国ユダヤ系・宇宙史小説の代表作となった。",
    historical_context="2010年代半ば米国宇宙開発回顧期。",
    primary_source_url=WIKI_EN+"Moonglow_(novel)",
    primary_source_type="Wikipedia: Moonglow",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="ディアスポラ",
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
            entry.pop("description", None)
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
        print(f"[wave22-c32-add80] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave22-c32-add80] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
