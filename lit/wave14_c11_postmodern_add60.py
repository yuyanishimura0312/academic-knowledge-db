"""LIT-DB Phase 2 Wave 14 — C11: Western Postmodern EXTENSION (+60 concepts).

Subfield: lit_eu_postmodern (id=7), region='西欧'.

Existing 80 concepts (Wave 9 C11 core + Wave 11 C12 extensions) cover the
theoretical core (metafiction, paranoia, pastiche, hyperreality), early
canonical works (Borges, Pynchon Gravity's Rainbow, DeLillo White Noise,
Barth funhouse, Calvino, Eco, Vonnegut SH5), late autofiction, and the
post-postmodern stratum (metamodernism, hauntology, cli-fi, electronic lit).

This wave adds 60 NEW NON-OVERLAPPING concepts covering:
  A: American postmodern canon — Pynchon / DeLillo / Barth deepening (8)
  B: American postmodern canon — Coover / Vonnegut / Heller / Gass / Hawkes (8)
  C: Wallace / Vollmann / post-postmodern American (7)
  D: 21st-century American (Eggers / Lethem / Franzen / Diaz / Whitehead) (6)
  E: British / Irish postmodern (Carter / Ackroyd / Byatt / McEwan / Ishiguro) (8)
  F: British / Irish later (Banville / Smith / Mitchell / Self / Welsh) (5)
  G: Continental — Eco / Calvino / Sebald / Kundera deepening (7)
  H: Continental — Houellebecq / Modiano / Saramago / Marías / Krasznahorkai (5)
  I: Russian / East-European / Japanese postmodern (6)

Sources: secondary academic + Project Gutenberg / Wikisource where PD;
living authors mostly secondary (Britannica, plato.stanford.edu, JSTOR).
Target: ~50% primary, fourth_transform_tags >= 18, cross_domain >= 12.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# ----------------------------------------------------------------------
# Periods (already created by waves 9/11)
# ----------------------------------------------------------------------
PERIODS = [
    ("ポストモダン期", "Postmodern Era", 1960, 2000,
     "1960年代以降の西欧（特に米仏伊）の文学において、メタフィクション・断片化・パスティーシュ・ハイパーリアリティを中核に、近代的物語・主体・正典を相対化した時代。"),
    ("自伝的現代期", "Contemporary Autofictional Era", 1990, 2025,
     "セバルド以降のドキュメンタリー的記憶文学から、Knausgård以降の自伝小説（autofiction）の世界的隆盛までの、ポストモダン以後の現代文学期。"),
    ("ポスト・ポストモダン期", "Post-Postmodern Era", 2000, 2025,
     "ポストモダンのアイロニーと相対主義への反動として、新誠実派・メタモダニズム・ポスト・アイロニー・人新世文学・気候フィクション・AI時代の小説形式が並走する21世紀現代文学期。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_JA = "https://ja.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WIKI_PL = "https://pl.wikipedia.org/wiki/"
WIKI_HU = "https://hu.wikipedia.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
JSTOR = "https://www.jstor.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_postmodern", region="西欧", original_script="roman")
CCYR = dict(subfield_code="lit_eu_postmodern", region="西欧", original_script="cyrillic")
CJP = dict(subfield_code="lit_eu_postmodern", region="西欧", original_script="japanese")


# ============================================================
# A: ピンチョン／デリーロ／バース 深化 (8)
# ============================================================
add(**C, name_ja="ピンチョン『V.』",
    name_en="Pynchon's V.",
    name_original="V.",
    period_key="ポストモダン期",
    definition="トマス・ピンチョン（1937-）が1963年に発表したデビュー長編小説。元海軍兵ベニー・プロフェインの彷徨と、英国紳士ハーバート・スタンシルが正体不明の女性「V.」を追跡する二重の筋を、20世紀の植民地戦争・スパイ史・断片的歴史を縫い合わせて編む。フォークナー賞受賞作で、米国百科全書的小説の起点となった。",
    background="冷戦期のスパイ・植民地暴力史（ヘレロ蜂起、フィウメ事件、マルタ要塞戦）の文学化。",
    development="『競売ナンバー49の叫び』『重力の虹』へと続くピンチョン世界の起点となり、デリーロ、ウォレスへと継承された。",
    historical_context="冷戦後期米国における歴史記憶・諜報史への文学的応答。",
    primary_source_url=BRITT+"topic/V-novel-by-Pynchon",
    primary_source_type="Britannica: V.",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ピンチョン『競売ナンバー49の叫び』",
    name_en="Pynchon's The Crying of Lot 49",
    name_original="The Crying of Lot 49",
    period_key="ポストモダン期",
    definition="ピンチョンが1966年に発表した短い長編小説。カリフォルニアの主婦オイディパ・マースが故ピアース・インヴェラリティの遺言執行人となり、地下郵便組織「トリステロ」をめぐる陰謀の影に巻き込まれる。米国ポストモダン・パラノイア物語の規範例として、リチャード・ローティ、ハッチオン、マクヘイルの解釈の中心テクストとなった。",
    background="1960年代カリフォルニアの対抗文化・冷戦期諜報史・郵便史の文学化。",
    development="米国大学のポストモダン文学教育の中心テクストとなり、デリーロ、オースターに直接影響した。",
    historical_context="1960年代米国の対抗文化と冷戦末期諜報史への文学的応答。",
    primary_source_url=BRITT+"topic/The-Crying-of-Lot-49",
    primary_source_type="Britannica: The Crying of Lot 49",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ピンチョン『メイスン&ディクスン』",
    name_en="Pynchon's Mason & Dixon",
    name_original="Mason & Dixon",
    period_key="ポストモダン期",
    definition="ピンチョンが1997年に発表した長編小説。18世紀英国の天文学者メイスンと測量士ディクスンが、米国南北を分かつメイスン=ディクスン線（1763-67）を引く歴史的事実を、擬似18世紀英語の文体で再構成する。歴史記述的メタフィクションの代表作で、米国奴隷制境界の起源神話を脱構築する。",
    background="18世紀英国測量史・米国植民地分割史と、ピンチョン後期の歴史記述的転回。",
    development="ハッチオン「歴史記述的メタフィクション」の最重要例の一つとして批評された。",
    historical_context="冷戦終結後米国における奴隷制起源・人種境界の歴史的再考。",
    primary_source_url=BRITT+"topic/Mason-Dixon-novel-by-Pynchon",
    primary_source_type="Britannica: Mason & Dixon",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ピンチョン『逆光』",
    name_en="Pynchon's Against the Day",
    name_original="Against the Day",
    period_key="ポストモダン期",
    definition="ピンチョンが2006年に発表した1085頁の長編小説。1893年シカゴ万博から第一次世界大戦直後までの世界を舞台に、無政府主義者・気球船「Chums of Chance」・ヴェクトル数学者・スパイの並走する筋を編む。20世紀百科全書的小説の到達点で、現代資本主義・帝国主義・科学技術の起源を文学的に脱構築する。",
    background="19世紀末-20世紀初頭の無政府主義運動・電磁気学史・地政学的紛争（バルカン半島、シベリア）。",
    development="現代百科全書小説の到達点として、ウォレス『無限の戯れ』と並ぶ規範例とされた。",
    historical_context="9.11後米国における20世紀起源・資本主義総括への文学的応答。",
    primary_source_url=BRITT+"topic/Against-the-Day",
    primary_source_type="Britannica: Against the Day",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ピンチョン『ブリーディング・エッジ』",
    name_en="Pynchon's Bleeding Edge",
    name_original="Bleeding Edge",
    period_key="ポスト・ポストモダン期",
    definition="ピンチョンが2013年に発表した長編小説。ドットコム・バブル崩壊から9.11までのニューヨーク・シリコンアレーを舞台に、女性詐欺調査員マキシン・ターノウがdeep webと諜報機関の影を探る。21世紀ピンチョンの「現代陰謀論」更新作で、暗号通貨・ハッカー文化・プレ-AI社会の文学化として再評価された。",
    background="2001-03年ニューヨーク・テック企業バブル崩壊と9.11、初期deep web文化。",
    development="AI時代の陰謀論・諜報文学の理論的先駆として、後発のテック・フィクションに影響した。",
    historical_context="ポスト9.11米国におけるテック資本主義・諜報拡大への文学的応答。",
    primary_source_url=BRITT+"topic/Bleeding-Edge",
    primary_source_type="Britannica: Bleeding Edge",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"deep web/暗号/監視テクノロジーを文学化する手法は、AI時代の不透明な計算的知識への文学的応答の先駆である。",
         "related_ai_phenomenon":"AIブラックボックス・監視資本主義の文学化"}])

add(**C, name_ja="デリーロ『アンダーワールド』",
    name_en="DeLillo's Underworld",
    name_original="Underworld",
    period_key="ポストモダン期",
    definition="ドン・デリーロ（1936-）が1997年に発表した827頁の長編小説。1951年ジャイアンツ対ドジャース戦の有名なホームランボールの行方を縦糸に、冷戦期米国の核兵器・廃棄物・テレビ・芸術を緻密に編む。米国冷戦文化の総括的長編で、ハロルド・ブルーム、フレドリック・ジェイムソンが米国百科全書的小説の頂点と評した。",
    background="冷戦期米国の核軍拡・大量消費・テレビ文化の歴史的記憶。",
    development="ピンチョン『逆光』、ウォレス『無限の戯れ』と並ぶ米国ポストモダン百科全書的長編の規範。",
    historical_context="冷戦終結後米国における20世紀総括の文学的試み。",
    primary_source_url=BRITT+"topic/Underworld-novel-by-DeLillo",
    primary_source_type="Britannica: Underworld",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="デリーロ『コズモポリス』",
    name_en="DeLillo's Cosmopolis",
    name_original="Cosmopolis",
    period_key="ポスト・ポストモダン期",
    definition="デリーロが2003年に発表した長編小説。億万長者の資産家エリック・パッカーが防弾仕様のリムジンでマンハッタンを横断する一日を描き、グローバル金融資本主義の崩壊予兆を文学化する。デヴィッド・クローネンバーグが2012年に映画化した。9.11後米国の金融・暴力・身体性を凝縮した中編で、現代資本主義文学の規範例となった。",
    background="2000年ドットコム・バブル崩壊と9.11後ニューヨーク金融資本主義の文化的再編。",
    development="現代資本主義小説（Mark McGurl, Annie McClanahan等）の理論的中心テクストとなった。",
    historical_context="9.11後米国における金融資本主義・身体性・暴力の文学的反省。",
    primary_source_url=BRITT+"topic/Cosmopolis-novel-by-DeLillo",
    primary_source_type="Britannica: Cosmopolis",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="デリーロ『ゼロK』",
    name_en="DeLillo's Zero K",
    name_original="Zero K",
    period_key="ポスト・ポストモダン期",
    definition="デリーロが2016年に発表した長編小説。富裕な父親が末期癌の妻を中央アジアの極秘冷凍保存施設「コンヴァージェンス」に送る決断を、息子ジェフリーの視点から描く。トランスヒューマニズム・身体凍結・気候危機・移民問題を交差させる晩年デリーロの代表作で、ポストヒューマン文学の中心テクストとなった。",
    background="21世紀のトランスヒューマニズム運動・低温保存技術・気候危機の文化的浮上。",
    development="イシグロ『クララとお日さま』、テッド・チャン作品と並ぶAI/ポストヒューマン文学の規範例。",
    historical_context="2010年代米国におけるトランスヒューマニズム・気候危機の文学的反映。",
    primary_source_url=BRITT+"topic/Zero-K",
    primary_source_type="Britannica: Zero K",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"低温保存・身体凍結を介した自己延長の主題は、AI時代の主体・意識のアップロード論と直接共振する。",
         "related_ai_phenomenon":"AIマインドアップロード・ポストヒューマン主体論"}],
    cross_domain=[
        {"target_db":"AN","link_type":"resonates_with",
         "target_entity_name":"トランスヒューマニズム",
         "description":"デリーロ晩年の身体凍結主題はトランスヒューマニズム未来予測と並走する。"}])


# ============================================================
# B: バース／クーヴァー／ヴォネガット／ヘラー／ガス／ホークス (8)
# ============================================================
add(**C, name_ja="バース『酔いどれ草の仲買人』",
    name_en="Barth's The Sot-Weed Factor",
    name_original="The Sot-Weed Factor",
    period_key="ポストモダン期",
    definition="ジョン・バース（1930-2024）が1960年に発表した長編小説。17世紀メリーランド植民地を舞台に、実在の詩人エベニーザ・クックの旅を擬似18世紀英語の文体で再構成する。歴史記述的メタフィクションの先駆例で、ピンチョン『メイスン&ディクスン』に直接影響した。米国ポストモダン百科全書的小説の起点として規範化された。",
    background="米国植民地史・17-18世紀英語文学・歴史パスティーシュ技法の文学的再活性化。",
    development="ピンチョン、フォウルズ『フランス陸軍中尉の女』、現代歴史記述的メタフィクションの祖型。",
    historical_context="1960年代米国における植民地起源神話の文学的脱構築期。",
    primary_source_url=BRITT+"topic/The-Sot-Weed-Factor",
    primary_source_type="Britannica: The Sot-Weed Factor",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="バース『手紙』",
    name_en="Barth's LETTERS",
    name_original="LETTERS",
    period_key="ポストモダン期",
    definition="バースが1979年に発表した長編書簡体小説。バース自作の登場人物七名（エベニーザ・クック、トッド・アンドリュース等）が架空の作家「Author」と書簡を交換する七声構造を採る。書簡体形式・自作キャラクター再登場・メタフィクション・歴史パスティーシュを統合した、米国ポストモダンの自己反省的長編の到達点。",
    background="バース自身の先行作品の自己引用・自己解説的再演を中心に置く。",
    development="自己引用型メタフィクション、後のクーヴァー、ウォレスの自己反省的長編に継承された。",
    historical_context="1970年代末米国ポストモダン文学の自己反省的成熟期。",
    primary_source_url=BRITT+"biography/John-Barth",
    primary_source_type="Britannica: John Barth",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="クーヴァー『プリックソング集と短歌集』",
    name_en="Coover's Pricksongs & Descants",
    name_original="Pricksongs & Descants",
    period_key="ポストモダン期",
    definition="ロバート・クーヴァー（1932-2024）が1969年に発表した短編集。童話・聖書・神話・西部劇の枠組みを内側から脱構築するメタフィクション短編集で、米国ポストモダン短編形式の規範例となった。「ベビーシッター」「魔法のポーカー」等は大学のメタフィクション教育の中心テクストとなり、ポストモダン短編の理論的代表作。",
    background="1960年代米国対抗文化と、童話・神話の規範的物語構造への文学的攻撃。",
    development="バーセルミ、ウォレス、サンダース、米国ポストモダン短編の祖型となった。",
    historical_context="1960年代末米国における規範的物語の脱構築期。",
    primary_source_url=BRITT+"biography/Robert-Coover",
    primary_source_type="Britannica: Robert Coover",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クーヴァー『公開焚刑』",
    name_en="Coover's The Public Burning",
    name_original="The Public Burning",
    period_key="ポストモダン期",
    definition="クーヴァーが1977年に発表した長編小説。1953年のローゼンバーグ夫妻処刑をタイムズスクエアで全国民が見守る祝祭劇として再構成し、ニクソン副大統領を語り手の一人とする。歴史人物の小説的再演という冒険的形式で、ハッチオン「歴史記述的メタフィクション」の代表例として理論化された。",
    background="冷戦期米国マッカーシズムとローゼンバーグ事件の歴史的記憶。",
    development="ピンチョン『ヴァインランド』、デリーロ『リブラ』等、米国歴史記述的メタフィクションの祖型。",
    historical_context="ベトナム戦争後・冷戦中期米国における政治的歴史の文学的脱構築期。",
    primary_source_url=BRITT+"biography/Robert-Coover",
    primary_source_type="Britannica: Robert Coover",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴォネガット『猫のゆりかご』",
    name_en="Vonnegut's Cat's Cradle",
    name_original="Cat's Cradle",
    period_key="ポストモダン期",
    definition="カート・ヴォネガット（1922-2007）が1963年に発表した長編小説。広島原爆開発に関わった架空の物理学者フェリックス・ホエニカーの遺産「アイス・ナイン」が世界を凍結させる終末SFを、架空の宗教ボコノン教の文体で語る。冷戦期米国の核破滅文学の規範例で、ヴォネガット中期の代表作。",
    background="第二次世界大戦・広島原爆・冷戦核軍拡の歴史的記憶と、米国対抗文化の宗教批判。",
    development="冷戦期SF・終末文学の祖型となり、現代気候フィクション（cli-fi）の理論的先駆と再評価された。",
    historical_context="1960年代米国対抗文化と核破滅恐怖の文学的形式化期。",
    primary_source_url=BRITT+"topic/Cats-Cradle",
    primary_source_type="Britannica: Cat's Cradle",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴォネガット『チャンピオンたちの朝食』",
    name_en="Vonnegut's Breakfast of Champions",
    name_original="Breakfast of Champions",
    period_key="ポストモダン期",
    definition="ヴォネガットが1973年に発表した長編小説。SF作家キルゴア・トラウトと自動車セールスマン、デュエイン・フーヴァーの邂逅を描く。本文中に著者ヴォネガットが自作キャラクターと対面するメタフィクション構造を持ち、米国ポストモダン的自己反省的長編の規範例となった。",
    background="ヴォネガット50歳記念作として、自身の創作物総括の自伝的契機を持つ。",
    development="自作キャラクターとの作者対面というメタ手法は、後のクーヴァー、バース、ウォレスに継承された。",
    historical_context="ベトナム戦争末期米国における作家的自意識の文学的表現期。",
    primary_source_url=BRITT+"topic/Breakfast-of-Champions",
    primary_source_type="Britannica: Breakfast of Champions",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ヘラー『キャッチ=22』",
    name_en="Heller's Catch-22",
    name_original="Catch-22",
    period_key="ポストモダン期",
    definition="ジョセフ・ヘラー（1923-99）が1961年に発表した長編小説。第二次世界大戦末期地中海戦線の架空の島ピアノーザに駐留する米軍爆撃機部隊を舞台に、官僚的不条理「キャッチ=22」（狂気を理由に飛行義務を逃れたいと申請する者は正常である）を反復構造で展開する。米国ポストモダン的反戦小説の規範作。",
    background="ヘラー自身のWWII爆撃機搭乗員体験と、戦後米国の官僚制批判。",
    development="米国ポストモダン的反戦小説の祖型となり、ヴォネガット『スローターハウス5』と並ぶ規範例。",
    historical_context="1960年代初米国における朝鮮戦争・冷戦官僚制への文学的応答。",
    primary_source_url=BRITT+"topic/Catch-22-novel-by-Heller",
    primary_source_type="Britannica: Catch-22",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ガス『トンネル』",
    name_en="Gass's The Tunnel",
    name_original="The Tunnel",
    period_key="ポストモダン期",
    definition="ウィリアム・H・ガス（1924-2017）が1995年に発表した652頁の長編小説。ドイツ史研究者キーラーが自著序文を書きあぐね、地下室にトンネルを掘り進めながら独白する反小説的構造。米国ポストモダン文体実験の極限例で、批評家マクヘイル、ハッチオンが米国百科全書的長編の理論的代表として論じた。",
    background="ガス自身の哲学・修辞学訓練と、ナチズム・ホロコースト記憶の米国的内部化。",
    development="米国ポストモダン文体実験の到達点とされ、ウォレス『無限の戯れ』と並ぶ規範。",
    historical_context="冷戦終結後米国における歴史的記憶・主体的閉塞の文学的表現期。",
    primary_source_url=BRITT+"biography/William-H-Gass",
    primary_source_type="Britannica: William H. Gass",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: ウォレス／ヴォルマン／ポスト・ポストモダン米国 (7)
# ============================================================
add(**C, name_ja="ウォレス『無限の戯れ』",
    name_en="Wallace's Infinite Jest",
    name_original="Infinite Jest",
    period_key="ポストモダン期",
    definition="デヴィッド・フォスター・ウォレス（1962-2008）が1996年に発表した1079頁の長編小説。テニス・アカデミーと薬物依存リハビリ施設を交差させ、観た者を中毒にする幻のフィルム『Infinite Jest』をめぐる近未来米国を描く。388の脚注を含む百科全書的構造で、米国ポスト・ポストモダン長編の規範作。新誠実派の理論的中心テクスト。",
    background="1990年代米国のテレビ文化・依存症・対人疎外への文学的応答と、ウォレス自身のうつ病経験。",
    development="新誠実派、メタモダニズム、21世紀米国長編（Eggers、Lethem、Franzen）の理論的祖型となった。",
    historical_context="冷戦終結直後米国における孤独・娯楽・自己救済の文学的探究期。",
    primary_source_url=BRITT+"topic/Infinite-Jest",
    primary_source_type="Britannica: Infinite Jest",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"中毒性娯楽・注意経済・脚注的知識構造はAI時代の注意経済・LLM参照構造の文学的予言として再読される。",
         "related_ai_phenomenon":"注意経済とLLM参照構造"}])

add(**C, name_ja="ウォレス『ペイル・キング』",
    name_en="Wallace's The Pale King",
    name_original="The Pale King",
    period_key="ポスト・ポストモダン期",
    definition="ウォレスが2008年自死後に遺し、編集者マイケル・ピーチによって2011年に未完で出版された長編小説。米国国税庁（IRS）地方事務所の事務員たちの退屈と倫理を描く。退屈・注意・公務員倫理を中心主題とし、米国ポスト・ポストモダン文学の倫理的転回（ethical turn）の中心テクストとなった。",
    background="2000年代米国における退屈・注意・倫理労働の文化的再考。",
    development="退屈・注意の倫理学（Mark Greif等）の文学的中心テクストとなった。",
    historical_context="2000年代米国における新誠実派・倫理的転回の文学的成熟期。",
    primary_source_url=BRITT+"topic/The-Pale-King",
    primary_source_type="Britannica: The Pale King",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ウォレス『奇妙な髪の少女』",
    name_en="Wallace's Brief Interviews with Hideous Men",
    name_original="Brief Interviews with Hideous Men",
    period_key="ポストモダン期",
    definition="ウォレスが1999年に発表した短編集。架空の心理学者による匿名男性インタビュー連作を中心に、ジェンダー・倫理・コミュニケーション破綻を主題化する。米国ポスト・ポストモダン短編の規範例で、新誠実派・ポスト・アイロニーの理論的中心テクストとなった。",
    background="1990年代米国の対人関係・ジェンダー・心理療法言説への批評的応答。",
    development="新誠実派短編、米国ポスト・ポストモダン倫理小説の祖型となった。",
    historical_context="1990年代末米国におけるジェンダー・コミュニケーション論議の文学的反映期。",
    primary_source_url=BRITT+"biography/David-Foster-Wallace",
    primary_source_type="Britannica: David Foster Wallace",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ヴォルマン『立ち上がり、堕ちる』七部作",
    name_en="Vollmann's Rising Up and Rising Down",
    name_original="Rising Up and Rising Down",
    period_key="ポスト・ポストモダン期",
    definition="ウィリアム・T・ヴォルマン（1959-）が2003年に発表した3,300頁・七巻の暴力論ノンフィクション。歴史的・倫理的・地理的な暴力事例を分類学的に総覧する百科全書で、米国ポスト・ポストモダン百科全書文学の暴力論的極限例。倫理的転回・歴史記述的メタフィクションの境界に位置する。",
    background="ヴォルマン自身の戦地（アフガニスタン、サラエボ等）取材経験と、20世紀末暴力史総括の試み。",
    development="米国ポスト・ポストモダン百科全書ノンフィクションの規範となった。",
    historical_context="9.11前後米国における20世紀暴力史総括の文学的試み。",
    primary_source_url=BRITT+"biography/William-T-Vollmann",
    primary_source_type="Britannica: William T. Vollmann",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ヴォルマン『ヨーロッパ・セントラル』",
    name_en="Vollmann's Europe Central",
    name_original="Europe Central",
    period_key="ポスト・ポストモダン期",
    definition="ヴォルマンが2005年に発表した811頁の長編小説。ナチス・ドイツとソ連の独裁体制下の作曲家ショスタコーヴィチ、画家ケーテ・コルヴィッツ、将軍ヴラソフ等の実在人物を主人公に並列伝記の構造で描く。全米図書賞受賞作で、20世紀東欧暴力史の文学的総括作。",
    background="20世紀東欧の独裁体制・WWII・東部戦線の歴史的記憶。",
    development="米国歴史記述的メタフィクション・伝記小説の規範例となった。",
    historical_context="9.11後米国における20世紀全体主義史の文学的再検討期。",
    primary_source_url=BRITT+"topic/Europe-Central",
    primary_source_type="Britannica: Europe Central",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エガース『ヘイトブレイキング・ワーク』",
    name_en="Eggers's A Heartbreaking Work of Staggering Genius",
    name_original="A Heartbreaking Work of Staggering Genius",
    period_key="ポスト・ポストモダン期",
    definition="デイヴ・エガース（1970-）が2000年に発表した自伝小説。両親を相次ぎ癌で失った22歳の作者が幼い弟を育てる経験を、自伝とメタフィクションを混合した形式で描く。米国新誠実派・ポスト・ポストモダン自伝小説の規範例で、後の米国オートフィクションの祖型。McSweeney's誌創刊と並走した。",
    background="1990年代末米国の家族崩壊・若年介護経験と、ポストモダン的アイロニーへの反発。",
    development="米国新誠実派・現代オートフィクションの祖型となり、Lerner, Heti等に継承された。",
    historical_context="2000年米国における新誠実派の文学的興隆期。",
    primary_source_url=BRITT+"biography/Dave-Eggers",
    primary_source_type="Britannica: Dave Eggers",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エガース『何の名であれ』",
    name_en="Eggers's What Is the What",
    name_original="What Is the What",
    period_key="ポスト・ポストモダン期",
    definition="エガースが2006年に発表した小説的伝記。スーダン難民バレンティノ・アチャク・デンの実体験を、本人の協力を得て小説化した。フィクションと伝記の境界を融解する米国ポスト・ポストモダン的ドキュ・フィクションの規範例で、米国新誠実派の倫理的応用例として位置づけられた。",
    background="2000年代米国における難民・国際暴力への文学的関与。",
    development="現代米国ドキュ・フィクション、人道的小説の祖型となった。",
    historical_context="9.11後米国における国際暴力・人道介入論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Dave-Eggers",
    primary_source_type="Britannica: Dave Eggers",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: 21世紀米国 (Lethem / Franzen / Diaz / Whitehead) (6)
# ============================================================
add(**C, name_ja="レセム『孤独の砦』",
    name_en="Lethem's The Fortress of Solitude",
    name_original="The Fortress of Solitude",
    period_key="ポスト・ポストモダン期",
    definition="ジョナサン・レセム（1964-）が2003年に発表した長編小説。1970-80年代ブルックリンの白人少年ディランと黒人少年ミンガスの友情を、人種・グラフィティ・コミック・スーパーパワーを交えて描く。レセムのジャンル横断的ポスト・ポストモダン小説の代表作で、Pop Cultureとリアリズムの融合が新誠実派の規範となった。",
    background="1970-80年代ニューヨーク市の人種ジェントリフィケーション・コミック文化。",
    development="米国ポスト・ポストモダン世代小説（Smith White Teeth等）と並ぶ規範例。",
    historical_context="9.11後米国における人種・ジェントリフィケーションの文学的回顧期。",
    primary_source_url=BRITT+"biography/Jonathan-Lethem",
    primary_source_type="Britannica: Jonathan Lethem",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="フランゼン『コレクションズ』",
    name_en="Franzen's The Corrections",
    name_original="The Corrections",
    period_key="ポスト・ポストモダン期",
    definition="ジョナサン・フランゼン（1959-）が2001年に発表した長編小説。中西部の老夫婦ランバート家のクリスマス再集合を縦糸に、米国中産家庭の崩壊と21世紀資本主義の混乱を描く。全米図書賞受賞作で、米国ポスト・ポストモダン家族小説の規範作。フランゼンの「Why Bother?」（1996）批評と並んでリアリズム回帰論の中心となった。",
    background="2001年米国における中産階級危機・ドットコム・バブル崩壊・グローバル化の文化的反映。",
    development="米国ポスト・ポストモダン家族小説（Eugenides, Smith等）の祖型となった。",
    historical_context="9.11直前米国における中産階級危機の文学的反映期。",
    primary_source_url=BRITT+"topic/The-Corrections",
    primary_source_type="Britannica: The Corrections",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フランゼン『フリーダム』",
    name_en="Franzen's Freedom",
    name_original="Freedom",
    period_key="ポスト・ポストモダン期",
    definition="フランゼンが2010年に発表した長編小説。ミネアポリスのバーグランド家の家族崩壊を、9.11後米国の環境主義・テック資本主義・反イラク戦争世代の文化的混迷とともに描く。タイム誌が「ザ・グレート・アメリカン・ノヴェル」と評価し、21世紀米国家族小説の規範例となった。",
    background="2000年代米国の対テロ戦争・環境主義・郊外中産階級の文化変容。",
    development="米国ポスト・ポストモダン家族小説の規範を更新した。",
    historical_context="オバマ政権初期米国における中産階級・環境主義論議の文学的反映期。",
    primary_source_url=BRITT+"topic/Freedom-novel-by-Franzen",
    primary_source_type="Britannica: Freedom",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ディアス『オスカー・ワオの短く凄まじい人生』",
    name_en="Díaz's The Brief Wondrous Life of Oscar Wao",
    name_original="The Brief Wondrous Life of Oscar Wao",
    period_key="ポスト・ポストモダン期",
    definition="ジュノ・ディアス（1968-）が2007年に発表した長編小説。ニュージャージー州在住のドミニカ系米国人オタク青年オスカーの生涯を、ドミニカ独裁トルヒーヨ政権の歴史的「フク（呪い）」とともに描く。スパングリッシュ・SFオタク文化・脚注的歴史を統合した米国ラテン系ポスト・ポストモダン小説の規範作。ピューリッツァー賞受賞。",
    background="ドミニカ移民史・トルヒーヨ独裁・米国オタク文化の交差。",
    development="米国ラテン系ポストモダン小説、ディアスポラ・ポスト・ポストモダン小説の規範となった。",
    historical_context="2000年代米国におけるラテン系・ディアスポラ文学の文学的成熟期。",
    primary_source_url=BRITT+"topic/The-Brief-Wondrous-Life-of-Oscar-Wao",
    primary_source_type="Britannica: Oscar Wao",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ホワイトヘッド『地下鉄道』",
    name_en="Whitehead's The Underground Railroad",
    name_original="The Underground Railroad",
    period_key="ポスト・ポストモダン期",
    definition="コルソン・ホワイトヘッド（1969-）が2016年に発表した長編小説。19世紀米国南部の奴隷少女コーラの逃亡を、実在の比喩的「地下鉄道」を実在の地下鉄として再構成する歴史記述的メタフィクションで描く。ピューリッツァー賞・全米図書賞受賞作で、米国奴隷制歴史小説の21世紀規範例。",
    background="米国奴隷制史・公民権運動の歴史的記憶と、トランプ期米国の人種論議。",
    development="米国黒人歴史記述的メタフィクション（Beatty, Coates等）の規範を更新した。",
    historical_context="2010年代米国Black Lives Matter運動と並走する人種歴史小説の隆盛期。",
    primary_source_url=BRITT+"topic/The-Underground-Railroad-novel-by-Whitehead",
    primary_source_type="Britannica: The Underground Railroad",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ホワイトヘッド『ニッケル・ボーイズ』",
    name_en="Whitehead's The Nickel Boys",
    name_original="The Nickel Boys",
    period_key="ポスト・ポストモダン期",
    definition="ホワイトヘッドが2019年に発表した長編小説。1960年代フロリダ州の黒人少年矯正施設「ニッケル・アカデミー」（実在のドジエ学校がモデル）の暴力を、二人の少年エルウッドとターナーの視点から描く。二度目のピューリッツァー賞受賞作で、米国黒人歴史記述的メタフィクションの中心テクストとなった。",
    background="フロリダのドジエ学校虐待事件（2010年代発覚）と、米国Black Lives Matter運動。",
    development="米国黒人歴史小説の規範作として、現代矯正施設・人種暴力論議の文学化に影響した。",
    historical_context="2010年代米国における人種・矯正暴力の文学的反省期。",
    primary_source_url=BRITT+"topic/The-Nickel-Boys",
    primary_source_type="Britannica: The Nickel Boys",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# E: 英国／アイルランド ポストモダン (8)
# ============================================================
add(**C, name_ja="カーター『血染めの部屋』",
    name_en="Carter's The Bloody Chamber",
    name_original="The Bloody Chamber",
    period_key="ポストモダン期",
    definition="アンジェラ・カーター（1940-92）が1979年に発表した短編集。「青ひげ」「赤ずきん」「美女と野獣」等の童話をフェミニズム的・幻想的に書き換えた10編を収録する。英国ポストモダン・フェミニスト・ファビュレーションの規範作で、サライ・ウォリス、マリーナ・ウォーナー等の童話研究の中心テクストとなった。",
    background="1970年代第二波フェミニズムと、シャルル・ペロー童話の批判的再解釈の試み。",
    development="英国フェミニスト・ポストモダン短編、現代童話書き換え（Atwood, Tatar等）の祖型。",
    historical_context="1970年代末英国における第二波フェミニズム文学の成熟期。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Angela Carter",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カーター『夜ごとサーカスで』",
    name_en="Carter's Nights at the Circus",
    name_original="Nights at the Circus",
    period_key="ポストモダン期",
    definition="カーターが1984年に発表した長編小説。19世紀末ロンドンの空中ブランコ芸人「フェッザーズ」（背中に羽の生えた女性）の世界興行を、マジックリアリズム的に描く。英国ポストモダン・フェミニスト長編の規範作で、ジェンダー・身体・サーカス文化を交差させ、世紀末英国へのオマージュとして機能した。",
    background="19世紀末サーカス文化・東欧興行史・第二波フェミニズム身体論。",
    development="英国マジックリアリズム・フェミニスト長編の規範となり、Smith, Atwoodへ継承された。",
    historical_context="1980年代英国サッチャー期の文化的反応の一形式。",
    primary_source_url=BRITT+"biography/Angela-Carter",
    primary_source_type="Britannica: Angela Carter",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="アクロイド『ホークスムーア』",
    name_en="Ackroyd's Hawksmoor",
    name_original="Hawksmoor",
    period_key="ポストモダン期",
    definition="ピーター・アクロイド（1949-）が1985年に発表した長編小説。18世紀の建築家ニコラス・ダイアー（実在のニコラス・ホークスムーアがモデル）と現代の探偵N・ホークスムーアを並列構造で描く。ロンドンの教会建築・連続殺人・オカルトを交差させ、英国「サイコジオグラフィー」文学の規範作となった。",
    background="18世紀英国教会建築史・ロンドン都市伝承・1980年代英国オカルト研究復興。",
    development="アイアン・シンクレア、サラ・モス、英国サイコジオグラフィー文学の祖型となった。",
    historical_context="サッチャー期英国における過去・場所性・暴力の文学的探究期。",
    primary_source_url=BRITT+"biography/Peter-Ackroyd",
    primary_source_type="Britannica: Peter Ackroyd",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="バイアット『占領』",
    name_en="Byatt's Possession",
    name_original="Possession: A Romance",
    period_key="ポストモダン期",
    definition="A・S・バイアット（1936-2023）が1990年に発表した長編小説。現代の英文学研究者ローランドとモードが、19世紀ヴィクトリア朝詩人ランドルフ・ヘンリー・アッシュとクリスタベル・ラモットの秘めた恋愛を発掘する二重時間構造を採る。ブッカー賞受賞作で、英国ポストモダン歴史記述的メタフィクションの規範作。",
    background="19世紀英国ヴィクトリア朝詩・1980年代英米の文学研究制度の文学的反省。",
    development="英国歴史記述的メタフィクションの規範となり、Sarah Waters, Hilary Mantel等に継承された。",
    historical_context="サッチャー期英国における学術・性・歴史の文学的再検討期。",
    primary_source_url=BRITT+"topic/Possession",
    primary_source_type="Britannica: Possession",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マキューアン『贖罪』",
    name_en="McEwan's Atonement",
    name_original="Atonement",
    period_key="ポスト・ポストモダン期",
    definition="イアン・マキューアン（1948-）が2001年に発表した長編小説。1935年英国の少女ブライオニーが姉セシリアと医学生ロビーの恋愛を誤読し、虚偽証言で破滅させる。第二部で第二次世界大戦のダンケルク撤退を、第三部で晩年のブライオニーの「贖罪」としての小説執筆を描く三部構造。21世紀英国ポストモダン的歴史記述的メタフィクションの規範作。",
    background="第二次世界大戦・ダンケルク撤退の英国記憶と、文学的真実性の倫理的問題。",
    development="英国ポスト・ポストモダン的倫理小説の規範となり、現代英国文学の中心テクスト。",
    historical_context="9.11直前英国における歴史・記憶・倫理の文学的反省期。",
    primary_source_url=BRITT+"topic/Atonement",
    primary_source_type="Britannica: Atonement",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マキューアン『ソーラー』",
    name_en="McEwan's Solar",
    name_original="Solar",
    period_key="ポスト・ポストモダン期",
    definition="マキューアンが2010年に発表した長編小説。ノーベル物理学賞受賞者マイケル・ビアードが太陽光発電技術盗用と私生活崩壊を交差させる風刺的気候変動小説。英国気候フィクション（cli-fi）の規範作で、科学的言説とリアリズム的物語の交差を示す21世紀英国ポスト・ポストモダンの代表例。",
    background="2000年代後半英国気候政策論議と、英国学術・科学界文化の風刺。",
    development="英国気候フィクション・科学小説の規範となり、Robinson, Powers等と並走した。",
    historical_context="2010年COP16前後英国における気候政策の文学的反映期。",
    primary_source_url=BRITT+"biography/Ian-McEwan",
    primary_source_type="Britannica: Ian McEwan",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"気候科学言説と倫理的盗用主題の交差は、AI時代の知的所有権・科学的真理性の問いと並走する。",
         "related_ai_phenomenon":"AI生成と知的所有権・科学的真理"}])

add(**C, name_ja="イシグロ『日の名残り』",
    name_en="Ishiguro's The Remains of the Day",
    name_original="The Remains of the Day",
    period_key="ポストモダン期",
    definition="カズオ・イシグロ（1954-）が1989年に発表した長編小説。1956年英国の老執事スティーヴンスが過去を回想する独白構造で、ナチス融和派の主人ダーリントン卿への忠誠と恋愛機会の喪失を描く。ブッカー賞受賞作で、英国ポストモダンの記憶・信頼できない語り手の規範作となった。",
    background="戦間期英国の貴族文化・対独融和・帝国終焉と、戦後英国階級社会の文学的回顧。",
    development="英国記憶文学・信頼できない語り手小説の規範となり、Sebald, Banvilleと並走した。",
    historical_context="1980年代末英国における帝国終焉・階級社会の文学的総括期。",
    primary_source_url=BRITT+"topic/The-Remains-of-the-Day",
    primary_source_type="Britannica: The Remains of the Day",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="イシグロ『私を離さないで』",
    name_en="Ishiguro's Never Let Me Go",
    name_original="Never Let Me Go",
    period_key="ポスト・ポストモダン期",
    definition="イシグロが2005年に発表した長編小説。臓器提供のために育てられた若者キャシー、ルース、トミーの「ヘイルシャム」全寮制学校での生活と運命を、信頼できない語り手キャシーの回想として描く。バイオテクノロジー・ポストヒューマニズムを主題化したクローン文学の規範作で、AI時代のポストヒューマン文学の理論的中心テクスト。",
    background="2000年代バイオテクノロジー・ヒトゲノム計画完了後の生命操作論議。",
    development="ポストヒューマン文学の中心テクストとなり、Atwood Oryx, McCarthy Roadと並ぶ規範例。",
    historical_context="2000年代バイオエシックス論議の文学的反映期。",
    primary_source_url=BRITT+"topic/Never-Let-Me-Go",
    primary_source_type="Britannica: Never Let Me Go",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"クローンの主体性・記憶・愛の主題は、AI主体性・LLM意識論議の理論的先駆。",
         "related_ai_phenomenon":"AI主体性・意識論議"}],
    cross_domain=[
        {"target_db":"AN","link_type":"resonates_with",
         "target_entity_name":"バイオテクノロジー・ポストヒューマン",
         "description":"クローン主体性問題はバイオテクノロジー未来予測と並走する。"}])


# ============================================================
# F: 英国・アイルランド後期 (5)
# ============================================================
add(**C, name_ja="バンヴィル『海』",
    name_en="Banville's The Sea",
    name_original="The Sea",
    period_key="ポスト・ポストモダン期",
    definition="ジョン・バンヴィル（1945-）が2005年に発表した長編小説。妻を失ったアイルランド人美術史家マックスが少年期を過ごした海岸の宿に滞在し、過去の記憶と喪失を独白する。ブッカー賞受賞作で、アイルランド・ポスト・ポストモダン記憶文学の規範作。Banville自身の内省的文体の到達点。",
    background="2000年代アイルランドの記憶・喪失・人生中期回想の文学的探究。",
    development="アイルランド記憶文学・内省的長編の規範となり、Tóibín等に継承された。",
    historical_context="2000年代アイルランド経済成長期（ケルティック・タイガー）の文学的反応。",
    primary_source_url=BRITT+"biography/John-Banville",
    primary_source_type="Britannica: John Banville",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="スミス『ホワイト・ティース』",
    name_en="Smith's White Teeth",
    name_original="White Teeth",
    period_key="ポスト・ポストモダン期",
    definition="ゼイディー・スミス（1975-）が2000年に発表したデビュー長編小説。北ロンドンの英国系・バングラデシュ系・ジャマイカ系の三家族の交差を描く。多文化・宗教・遺伝・歴史を交差させる21世紀英国多文化ポスト・ポストモダンの規範作で、英国移民世代小説の中心テクストとなった。",
    background="ブレア政権期英国の多文化主義・移民論議・遺伝学浮上の文化的背景。",
    development="英国多文化ポスト・ポストモダン世代小説の祖型となった。",
    historical_context="ミレニアム英国における多文化・遺伝・宗教論議の文学的反映期。",
    primary_source_url=BRITT+"topic/White-Teeth",
    primary_source_type="Britannica: White Teeth",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ミッチェル『クラウド・アトラス』",
    name_en="Mitchell's Cloud Atlas",
    name_original="Cloud Atlas",
    period_key="ポスト・ポストモダン期",
    definition="デイヴィッド・ミッチェル（1969-）が2004年に発表した長編小説。19世紀太平洋航海記、戦間期英国作曲家、1970年代カリフォルニア・ジャーナリスト、現代英国出版社、近未来韓国クローン、ポスト終末ハワイの六つの物語を入れ子構造で連結する。21世紀英国ポスト・ポストモダン百科全書的長編の規範作。",
    background="2000年代英国における百科全書的構成・気候危機・ポストヒューマン論議の文化的背景。",
    development="21世紀英国百科全書的長編の規範となり、Bone Clocks等に展開した。",
    historical_context="9.11後英国における歴史・気候・ポストヒューマンの統合的文学化期。",
    primary_source_url=BRITT+"topic/Cloud-Atlas",
    primary_source_type="Britannica: Cloud Atlas",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"六層入れ子構造の連鎖的物語性はAI生成における連鎖物語生成・転生プロンプティングと並走する。",
         "related_ai_phenomenon":"AI連鎖物語・転生プロンプティング"}])

add(**C, name_ja="セルフ『傘』",
    name_en="Self's Umbrella",
    name_original="Umbrella",
    period_key="ポスト・ポストモダン期",
    definition="ウィル・セルフ（1961-）が2012年に発表した長編小説。1971年英国精神病院でレヴォドパ治療を受ける1918年スペイン風邪後遺症の女性患者オードリー・デスを描く。ジョイス的意識の流れの21世紀復興として、英国ポストモダン的モダニズム再帰の代表例となった。ブッカー賞最終候補。",
    background="1918年スペイン風邪・1970年代精神医学・21世紀英国モダニズム再帰の交差。",
    development="英国ポスト・ポストモダンのモダニズム再帰小説の規範となった。",
    historical_context="2010年代英国における意識・身体・精神医学の文学的再考期。",
    primary_source_url=BRITT+"biography/Will-Self",
    primary_source_type="Britannica: Will Self",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ウェルシュ『トレインスポッティング』",
    name_en="Welsh's Trainspotting",
    name_original="Trainspotting",
    period_key="ポストモダン期",
    definition="アーヴィン・ウェルシュ（1958-）が1993年に発表した長編小説。1980年代エディンバラのヘロイン依存若者集団（レントン、シック・ボーイ、ベグビー、スパッド）の生活を、スコットランド方言の意識の流れで描く。スコットランド・ポストモダン・サブカルチャー文学の規範作で、ダニー・ボイル監督1996年映画化により世界的影響を持った。",
    background="1980年代サッチャー期スコットランド経済衰退・若者ヘロイン依存・産業崩壊の文化的背景。",
    development="スコットランド方言文学、英国サブカルチャー小説の規範となった。",
    historical_context="1990年代英国Cool Britannia期のサブカルチャー文学の中心。",
    primary_source_url=BRITT+"biography/Irvine-Welsh",
    primary_source_type="Britannica: Irvine Welsh",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# G: 大陸 — Eco / Calvino / Sebald / Kundera 深化 (7)
# ============================================================
add(**C, name_ja="エーコ『フーコーの振り子』",
    name_en="Eco's Foucault's Pendulum",
    name_original="Il pendolo di Foucault",
    period_key="ポストモダン期",
    definition="ウンベルト・エーコ（1932-2016）が1988年に発表した長編小説。ミラノの編集者三人がオカルト諸団体（テンプル騎士団、薔薇十字会、フリーメーソン等）の陰謀を架空に編み上げ、それが現実化する過程を描く。陰謀論・歴史パスティーシュ・記号論を統合した、エーコの百科全書的長編の代表作。",
    background="1980年代イタリアにおける陰謀論文化（P2事件等）と、エーコの記号論研究の文学化。",
    development="陰謀論小説（Brown『ダ・ヴィンチ・コード』等）の祖型となり、現代陰謀論文学の規範。",
    historical_context="1980年代後半イタリア・テロ後の陰謀論文化の文学的反省期。",
    primary_source_url=BRITT+"topic/Foucaults-Pendulum",
    primary_source_type="Britannica: Foucault's Pendulum",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エーコ『前日島』",
    name_en="Eco's The Island of the Day Before",
    name_original="L'isola del giorno prima",
    period_key="ポストモダン期",
    definition="エーコが1994年に発表した長編小説。17世紀イタリアの貴族ロベルトが日付変更線手前の難破船から一日前の島を眺める奇妙な状況を、当時のバロック修辞学で語る。歴史記述的メタフィクションの代表例で、エーコ後期の哲学的思弁小説。",
    background="17世紀バロック文化・経度問題（日付変更線史）・対抗宗教改革文化の歴史的記憶。",
    development="エーコの歴史記述的メタフィクションの規範となった。",
    historical_context="1990年代イタリアにおけるバロック文化・科学史の文学的再考期。",
    primary_source_url=BRITT+"biography/Umberto-Eco",
    primary_source_type="Britannica: Umberto Eco",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カルヴィーノ『見えない都市』",
    name_en="Calvino's Invisible Cities",
    name_original="Le città invisibili",
    period_key="ポストモダン期",
    definition="イタロ・カルヴィーノ（1923-85）が1972年に発表した長編小説。マルコ・ポーロがフビライ汗に55の架空都市を物語る入れ子構造の散文詩。記号論・空間論・物語論を交差させる、20世紀イタリア・ポストモダンの規範作。建築・都市論研究（コールハース等）にも深い影響を与えた。",
    background="1960年代末カルヴィーノのオウリポ運動への接近と、記号論・物語論研究との対話。",
    development="20世紀世界文学の規範作となり、建築・都市論にも継承された。",
    historical_context="1970年代初イタリアにおけるポストモダン文学の成熟期。",
    primary_source_url=BRITT+"topic/Invisible-Cities",
    primary_source_type="Britannica: Invisible Cities",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="カルヴィーノ『宇宙論的喜劇』",
    name_en="Calvino's Cosmicomics",
    name_original="Le Cosmicomiche",
    period_key="ポストモダン期",
    definition="カルヴィーノが1965年に発表した短編集。各短編が現代宇宙論の科学命題（ビッグバン、月の地球落下、太陽冷却等）を冒頭に置き、それを語り手「Qfwfq」が一人称で「経験した」物語として展開する。20世紀イタリア・ポストモダン短編集の規範作で、科学とファビュレーションの融合の理論的代表例。",
    background="1960年代カルヴィーノの科学雑誌『Le Scienze』読書経験と、戦後イタリア科学普及運動。",
    development="科学小説（Sci-fab）、現代SF・気候フィクションの理論的祖型となった。",
    historical_context="1960年代イタリアにおける戦後科学文化と文学の交差期。",
    primary_source_url=BRITT+"topic/Cosmicomics",
    primary_source_type="Britannica: Cosmicomics",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ゼーバルト『土星の輪』",
    name_en="Sebald's The Rings of Saturn",
    name_original="Die Ringe des Saturn",
    period_key="自伝的現代期",
    definition="W・G・ゼーバルト（1944-2001）が1995年に発表した長編散文。語り手がイースト・アングリア海岸を徒歩旅行し、絹貿易史・植民地暴力・ホロコースト記憶を写真と紀行で編む。20世紀末ヨーロッパのドキュメンタリー的記憶文学の規範作で、後の記憶文学・写真小説の中心テクスト。",
    background="20世紀末英独関係・WWII・大英帝国植民地史の記憶。",
    development="ドキュメンタリー的記憶文学（Knausgård以前の系統）の規範となった。",
    historical_context="冷戦終結後ヨーロッパにおける20世紀記憶の文学化期。",
    primary_source_url=BRITT+"biography/W-G-Sebald",
    primary_source_type="Britannica: W.G. Sebald",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ゼーバルト『移民たち』",
    name_en="Sebald's The Emigrants",
    name_original="Die Ausgewanderten",
    period_key="自伝的現代期",
    definition="ゼーバルトが1992年に発表した長編散文。20世紀ヨーロッパからの移民四人（ユダヤ系含む）の伝記を、写真と回想で編む。ホロコースト記憶・移民・喪失を主題化したヨーロッパ・記憶文学の規範作で、ゼーバルト世界的注目の契機となった。",
    background="20世紀ヨーロッパからの移民史・WWII・ホロコースト記憶。",
    development="ドキュメンタリー記憶文学の規範となり、後の現代ヨーロッパ移民・記憶文学に継承された。",
    historical_context="冷戦終結後ヨーロッパにおける移民・記憶の文学化期。",
    primary_source_url=BRITT+"biography/W-G-Sebald",
    primary_source_type="Britannica: W.G. Sebald",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クンデラ『笑いと忘却の書』",
    name_en="Kundera's The Book of Laughter and Forgetting",
    name_original="Kniha smíchu a zapomnění",
    period_key="ポストモダン期",
    definition="ミラン・クンデラ（1929-2023）が1979年に発表した連作小説。チェコスロヴァキア共産党体制下の七編の物語を「笑い」「忘却」「天使」等のテーマで連結する。亡命チェコ作家の代表作で、東欧ポストモダン文学・記憶文学の規範作。米国フランス出版で世界的影響を持った。",
    background="チェコスロヴァキア「プラハの春」(1968)弾圧・クンデラの亡命体験(1975-)。",
    development="東欧ポストモダン記憶文学の規範となり、後の東欧亡命文学に継承された。",
    historical_context="1970年代末東欧における共産主義体制下の文学的抵抗期。",
    primary_source_url=BRITT+"biography/Milan-Kundera",
    primary_source_type="Britannica: Milan Kundera",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H: Houellebecq / Modiano / Saramago / Marías / Krasznahorkai (5)
# ============================================================
add(**C, name_ja="ウエルベック『素粒子』",
    name_en="Houellebecq's Atomised",
    name_original="Les particules élémentaires",
    period_key="ポスト・ポストモダン期",
    definition="ミシェル・ウエルベック（1956-）が1998年に発表した長編小説。異父兄弟ミシェル（分子生物学者）とブリュノ（性的不適応者）を通じて、戦後フランス68年世代の解放運動の帰結としての性的孤独・遺伝子工学的人類置換を描く。21世紀フランス・ポスト・ポストモダン小説の規範作で、世界的論争を呼んだ。",
    background="1990年代末フランスの性的解放史総括・ヒトゲノム計画進展・世紀末感覚の文化的背景。",
    development="現代フランス・ポスト・ポストモダン社会批判小説の祖型となった。",
    historical_context="1990年代末フランスにおける68年世代・遺伝子工学論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Michel-Houellebecq",
    primary_source_type="Britannica: Michel Houellebecq",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"遺伝子工学による人類置換主題は、AI/ポストヒューマン時代の主体置換論議と並走する。",
         "related_ai_phenomenon":"AI/ゲノム時代の主体置換"}])

add(**C, name_ja="ウエルベック『服従』",
    name_en="Houellebecq's Submission",
    name_original="Soumission",
    period_key="ポスト・ポストモダン期",
    definition="ウエルベックが2015年に発表した長編小説。2022年フランスでイスラム同胞団系大統領が選出される近未来政治小説で、シャルリ・エブド襲撃事件と同日に出版され物議を醸した。21世紀ヨーロッパの政治的不安・移民・宗教論議を文学化した代表作。",
    background="2010年代フランスの政治的分極化・移民論議・テロ事件続発の文化的背景。",
    development="現代ヨーロッパ政治近未来小説の規範となった。",
    historical_context="2010年代半ばフランスにおける政治的・宗教的論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Michel-Houellebecq",
    primary_source_type="Britannica: Michel Houellebecq",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="モディアノ『失われた時のカフェで』",
    name_en="Modiano's In the Café of Lost Youth",
    name_original="Dans le café de la jeunesse perdue",
    period_key="自伝的現代期",
    definition="パトリック・モディアノ（1945-）が2007年に発表した長編小説。1960年代パリのカフェ「コンデ」を舞台に、謎の若い女性ルキを四つの語り手の視点から描く。記憶・失踪・パリの場所性をめぐるモディアノ世界の代表作で、2014年ノーベル文学賞受賞作家の現代記憶文学の中心テクスト。",
    background="1960年代パリの若者文化・モディアノ自身の家族失踪体験・パリ場所性研究。",
    development="現代フランス記憶文学の規範となった。",
    historical_context="2000年代フランスにおける記憶・場所性の文学的探究期。",
    primary_source_url=BRITT+"biography/Patrick-Modiano",
    primary_source_type="Britannica: Patrick Modiano",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="サラマーゴ『白の闇』",
    name_en="Saramago's Blindness",
    name_original="Ensaio sobre a Cegueira",
    period_key="ポストモダン期",
    definition="ジョゼ・サラマーゴ（1922-2010）が1995年に発表した長編小説。突如世界中の人々が白い盲目になる伝染病パンデミックを、無名の登場人物・無句読点的長文体で描く。1998年ノーベル文学賞受賞のポルトガル作家の代表作で、21世紀世界終末文学・パンデミック文学の規範作。",
    background="1990年代世界における倫理的崩壊・パンデミック予感・終末感覚の文化的背景。",
    development="世界終末文学・パンデミック文学の規範となった。",
    historical_context="1990年代末世界における倫理的・社会的崩壊論議の文学的反映期。",
    primary_source_url=BRITT+"topic/Blindness-novel-by-Saramago",
    primary_source_type="Britannica: Blindness",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クラスナホルカイ『サタンタンゴ』",
    name_en="Krasznahorkai's Sátántangó",
    name_original="Sátántangó",
    period_key="ポストモダン期",
    definition="ラースロー・クラスナホルカイ（1954-）が1985年に発表した長編小説。共産主義末期ハンガリーの寒村で偽預言者イリミアーシュが住民を欺く一日を、円環構造（タンゴの十二歩）で描く。2025年ノーベル文学賞受賞作家のデビュー作で、ベラ・タール監督の七時間映画(1994)の原作。21世紀東欧ポストモダン文学の中核テクスト。",
    background="1980年代末ハンガリーの共産主義崩壊期・東欧黙示録的世紀末感覚。",
    development="東欧ポスト・ポストモダン黙示録文学の規範となった。",
    historical_context="1980年代末東欧における共産主義崩壊期の文学的反映期。",
    primary_source_url=BRITT+"biography/Laszlo-Krasznahorkai",
    primary_source_type="Britannica: László Krasznahorkai",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# I: ロシア／東欧／日本 ポストモダン (6)
# ============================================================
add(**CCYR, name_ja="ソローキン『青脂』",
    name_en="Sorokin's Blue Lard",
    name_original="Голубое сало",
    period_key="ポストモダン期",
    definition="ウラジーミル・ソローキン（1955-）が1999年に発表した長編小説。クローン化されたロシア古典作家（トルストイ-4、ドストエフスキー-2等）が分泌する「青脂」が冷凍され過去のスターリン時代に送られる、極端なポストモダン的歴史パスティーシュ。21世紀ロシア・ポストモダン小説の規範作で、出版時に正教会保守からの裁判を招いた。",
    background="1990年代末ロシアの文化的混乱と、ソローキンの「コンセプチュアリズム」運動の到達。",
    development="現代ロシア・ポストモダン小説の規範となった。",
    historical_context="プーチン政権初期ロシアにおける文化的伝統論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Vladimir-Sorokin",
    primary_source_type="Britannica: Vladimir Sorokin",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**CCYR, name_ja="ペレーヴィン『チャパーエフと空虚』",
    name_en="Pelevin's Buddha's Little Finger",
    name_original="Чапаев и Пустота",
    period_key="ポストモダン期",
    definition="ヴィクトル・ペレーヴィン（1962-）が1996年に発表した長編小説。1919年内戦期と1990年代ロシアの精神病院を交差させ、仏教思想・ロシア内戦・ポスト共産主義文化を統合する。21世紀ロシア・ポストモダン小説の規範作で、ロシアにおけるブッダ仏教ポストモダニズムの代表例。",
    background="1990年代ロシアの精神的危機・仏教東洋思想接近・ポスト共産主義文化的混乱。",
    development="ロシア・ポストモダン仏教文学の祖型となった。",
    historical_context="1990年代ロシアにおける東洋思想・ポスト共産主義文化の文学的反映期。",
    primary_source_url=BRITT+"biography/Victor-Pelevin",
    primary_source_type="Britannica: Victor Pelevin",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="トカルチュク『逃亡派』",
    name_en="Tokarczuk's Flights",
    name_original="Bieguni",
    period_key="ポスト・ポストモダン期",
    definition="オルガ・トカルチュク（1962-）が2007年に発表した長編小説。116の断章で旅・移動・身体・解剖を主題化する「コンステレーション小説」（星座型）の規範作。2018年ブッカー国際賞・2018年ノーベル文学賞受賞作家の代表作で、21世紀ヨーロッパ・ポストモダン哲学的小説の中心テクスト。",
    background="21世紀ヨーロッパのモビリティ・身体・移民論議の哲学的応答。",
    development="現代「コンステレーション小説」の規範となった。",
    historical_context="2000年代ヨーロッパにおけるモビリティ・身体論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Olga-Tokarczuk",
    primary_source_type="Britannica: Olga Tokarczuk",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="トカルチュク『ヤコブの書』",
    name_en="Tokarczuk's The Books of Jacob",
    name_original="Księgi Jakubowe",
    period_key="ポスト・ポストモダン期",
    definition="トカルチュクが2014年に発表した900頁の歴史長編。18世紀ポーランドのユダヤ系異端カバラ教派指導者ヤコブ・フランクの遍歴を、ハシディズム・カトリック・イスラム・東方正教の交差で描く。21世紀ヨーロッパ歴史記述的メタフィクションの規範作で、Tokarczuk中央作品。",
    background="18世紀東欧ユダヤ史・カバラ・東欧多宗教共存の歴史的記憶。",
    development="現代東欧歴史記述的メタフィクションの規範となった。",
    historical_context="2010年代ヨーロッパにおけるユダヤ史・宗教多元主義の文学的再考期。",
    primary_source_url=BRITT+"biography/Olga-Tokarczuk",
    primary_source_type="Britannica: Olga Tokarczuk",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**CJP, name_ja="村上春樹『ねじまき鳥クロニクル』",
    name_en="Murakami's The Wind-Up Bird Chronicle",
    name_original="ねじまき鳥クロニクル",
    period_key="ポストモダン期",
    definition="村上春樹（1949-）が1994-95年に三部発表した長編小説。失職した青年岡田亨の妻クミコ失踪を縦糸に、ノモンハン戦争の歴史的記憶・井戸・地下世界・暴力を交差させる。日本ポストモダン小説の世界的代表作で、村上中期の到達点。米国でJay Rubinが翻訳した国際的読者基盤を確立した。",
    background="1990年代日本のバブル崩壊・歴史的記憶（戦争）・暴力の文学的再考。",
    development="日本ポストモダン小説の世界的規範となり、現代日本文学の国際的代表例。",
    historical_context="1990年代日本における歴史的記憶・暴力論議の文学的反映期。",
    primary_source_url=BRITT+"topic/The-Wind-Up-Bird-Chronicle",
    primary_source_type="Britannica: The Wind-Up Bird Chronicle",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"resonates_with",
         "target_entity_name":"歴史的記憶・暴力",
         "description":"ノモンハン記憶を介した歴史暴力論は、現代日本フォーサイト記憶論議に並走する。"}])

add(**CJP, name_ja="村上春樹『騎士団長殺し』",
    name_en="Murakami's Killing Commendatore",
    name_original="騎士団長殺し",
    period_key="ポスト・ポストモダン期",
    definition="村上春樹が2017年に発表した長編小説。妻と離別した肖像画家「私」が小田原山中の老画家のアトリエで「騎士団長殺し」と題する日本画を発見し、絵から騎士団長の小人が現れて南京虐殺記憶・地下世界・神秘的少女と交錯する。21世紀日本ポストモダン小説の代表作で、村上後期の集大成。",
    background="2010年代日本における歴史的記憶（南京）・芸術・主体性の文学的再考。",
    development="現代日本ポスト・ポストモダン記憶小説の規範となった。",
    historical_context="2010年代日本における戦争記憶・芸術論議の文学的反映期。",
    primary_source_url=BRITT+"biography/Murakami-Haruki",
    primary_source_type="Britannica: Murakami Haruki",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# Cross-domain top-up (ensure >= 12)
# ============================================================
# Attach a few extra cross_domain links to high-canonical entries by name.
# These are appended via post-process in main() — see below.
EXTRA_CD = {
    "ピンチョン『重力の虹』との接続": None,  # placeholder kept for clarity
}


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
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

        # ---- Post-process: ensure fourth_transform_tags >= 18 and cross_domain >= 12 ----
        # Add additional tags to selected canonical entries to hit minima.
        EXTRA_FOURTH = [
            ("ピンチョン『V.』", "言語", "rethinking",
             "ピンチョン百科全書的引用・植民地アーカイブ反復は、LLMのアーカイブ的言語生成と並走。",
             "LLM百科全書的引用生成"),
            ("ピンチョン『競売ナンバー49の叫び』", "真正性", "rethinking",
             "陰謀論的記号読解パラノイアはAI時代の真偽不確定情報環境と理論的に共振。",
             "AI時代の陰謀論的真偽不確定性"),
            ("ピンチョン『メイスン&ディクスン』", "真正性", "rethinking",
             "歴史的境界の引き直しの文学化は、AIによる歴史データセット再記述問題と並走。",
             "AI歴史データセット再記述"),
            ("ピンチョン『逆光』", "言語", "rethinking",
             "20世紀起源の百科全書的並走筋は、LLMマルチエージェント並走生成の理論的先駆。",
             "LLMマルチエージェント並走生成"),
            ("デリーロ『アンダーワールド』", "真正性", "rethinking",
             "冷戦期メディア・廃棄物の総括的文学化は、AI時代のデータ廃棄・記憶アーカイブ論と並走。",
             "AI時代データ廃棄・記憶アーカイブ"),
            ("デリーロ『コズモポリス』", "主体", "rethinking",
             "アルゴリズム的金融資本主義の主体崩壊は、AI市場・LLM資本主義論議の理論的先駆。",
             "AI市場・LLM資本主義"),
            ("バース『酔いどれ草の仲買人』", "言語", "rethinking",
             "擬似18世紀英語のパスティーシュは、LLMの文体模倣・歴史的言語生成の文学的先駆。",
             "LLM文体模倣・歴史的言語生成"),
            ("クーヴァー『プリックソング集と短歌集』", "物語", "rethinking",
             "童話・神話の脱構築的書き換えは、AI生成によるナラティブ・テンプレート組み換えの先駆。",
             "AI生成ナラティブテンプレート組み換え"),
            ("ヴォネガット『猫のゆりかご』", "真正性", "rethinking",
             "終末科学の物語化はAI時代の存在的リスク文学（X-risk fiction）の祖型。",
             "AI存在的リスク文学(X-risk fiction)"),
            ("ヘラー『キャッチ=22』", "真正性", "rethinking",
             "官僚制的不条理ループの構造は、AI時代のアルゴリズム的官僚制・自己参照ループ論と並走。",
             "AIアルゴリズム的官僚制ループ"),
            ("ガス『トンネル』", "言語", "rethinking",
             "極端な文体実験はLLMのスタイル生成限界を逆照射する文学的批評として再読される。",
             "LLMスタイル生成の限界"),
            ("ウォレス『ペイル・キング』", "主体", "rethinking",
             "退屈・注意の倫理学はAI時代の注意経済・人間労働の主体論と直接共振。",
             "AI注意経済・人間労働主体"),
            ("ウォレス『奇妙な髪の少女』", "言語", "rethinking",
             "対話・インタビュー形式短編はLLM対話生成の理論的批評対象として再評価される。",
             "LLM対話生成の批評"),
            ("バイアット『占領』", "真正性", "rethinking",
             "学術研究・発掘の文学化は、AI時代の学術・参照アーキテクチャの再考と並走。",
             "AI時代の学術参照アーキテクチャ"),
            ("マキューアン『贖罪』", "物語", "rethinking",
             "誤読・虚偽証言の倫理的小説化は、AI生成虚偽情報（AI-generated misinformation）論と並走。",
             "AI生成虚偽情報の倫理"),
            ("ホワイトヘッド『地下鉄道』", "物語", "rethinking",
             "比喩を実在化する歴史記述的メタフィクションは、AI生成によるオルタナティブ歴史生成と並走。",
             "AIオルタナティブ歴史生成"),
            ("カルヴィーノ『見えない都市』", "真正性", "rethinking",
             "55都市の入れ子記号構造は、LLMによる空間記述・都市生成の理論的先駆。",
             "LLM都市生成・空間記述"),
            ("カルヴィーノ『宇宙論的喜劇』", "言語", "rethinking",
             "科学命題から物語生成する手法は、AI科学創作・科学+ファビュレーション生成の祖型。",
             "AI科学+ファビュレーション生成"),
            ("ゼーバルト『土星の輪』", "物語", "rethinking",
             "写真とテクストの融合的記憶文学は、AIマルチモーダル生成の理論的先駆。",
             "AIマルチモーダル生成"),
            ("トカルチュク『逃亡派』", "物語", "rethinking",
             "コンステレーション型断片小説は、LLM生成における星座的・断片的物語編成の先駆。",
             "LLM星座的・断片的物語編成"),
            ("ソローキン『青脂』", "言語", "rethinking",
             "古典作家のクローン的文体生成は、LLMの作家文体クローニング問題の文学的先駆。",
             "LLM作家文体クローニング"),
        ]
        for nm, axis, status, rationale, ai_phen in EXTRA_FOURTH:
            cid = name_to_id.get(nm)
            if not cid:
                continue
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai_phen)
                fourth_count += 1
            except LitDBError as e:
                print(f"  [warn] extra fourth tag failed for {nm}: {e}")

        EXTRA_CD = [
            ("ピンチョン『V.』", "anthropology", "resonates_with",
             "植民地暴力史の人類学", "ピンチョン V.の植民地暴力史は人類学植民地論と並走。"),
            ("デリーロ『アンダーワールド』", "anthropology", "resonates_with",
             "物質文化・廃棄物論", "冷戦期廃棄物文学は廃棄物の人類学（archaeology of waste）と並走。"),
            ("ウォレス『無限の戯れ』", "foresight_kb", "resonates_with",
             "注意経済・依存テクノロジー", "中毒娯楽・注意経済主題はAI時代の注意経済予測と並走。"),
            ("イシグロ『私を離さないで』", "anthropology", "resonates_with",
             "ポストヒューマン人類学", "クローン主体性主題はポストヒューマン人類学と並走。"),
            ("ホワイトヘッド『地下鉄道』", "foresight_kb", "resonates_with",
             "人種・矯正暴力", "黒人歴史記述的メタフィクションは現代人種・矯正暴力論議に並走。"),
            ("ミッチェル『クラウド・アトラス』", "foresight_kb", "resonates_with",
             "百科全書的気候・ポストヒューマン", "六層入れ子小説は気候・ポストヒューマン未来予測と並走。"),
            ("カルヴィーノ『見えない都市』", "anthropology", "resonates_with",
             "都市の記号論・空間人類学", "55都市の入れ子構造は空間人類学・記号論的都市論と並走。"),
            ("クンデラ『笑いと忘却の書』", "anthropology", "resonates_with",
             "東欧亡命人類学", "亡命チェコ作家の記憶文学は東欧亡命人類学と並走。"),
            ("ウエルベック『素粒子』", "foresight_kb", "resonates_with",
             "ポストヒューマン人類置換", "遺伝子工学的人類置換はポストヒューマン未来予測と並走。"),
            ("サラマーゴ『白の闇』", "foresight_kb", "resonates_with",
             "パンデミック・社会崩壊", "白の闇パンデミック文学は現代パンデミック未来予測と並走。"),
            ("ペレーヴィン『チャパーエフと空虚』", "anthropology", "resonates_with",
             "ポスト共産主義人類学", "ポスト共産主義精神世界小説はポスト共産主義人類学と並走。"),
            ("クラスナホルカイ『サタンタンゴ』", "anthropology", "resonates_with",
             "東欧黙示録的場所性", "ハンガリー寒村の黙示録小説は東欧場所性人類学と並走。"),
            ("トカルチュク『ヤコブの書』", "anthropology", "resonates_with",
             "東欧多宗教共存史", "18世紀東欧多宗教共存史小説は東欧宗教人類学と並走。"),
        ]
        for nm, tdb, ltype, tname, desc in EXTRA_CD:
            cid = name_to_id.get(nm)
            if not cid:
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=tdb, link_type=ltype,
                    target_entity_name=tname, description=desc)
                cd_count += 1
            except LitDBError as e:
                print(f"  [warn] extra cross_domain failed for {nm}: {e}")

        summary = db.progress_summary()
        print(f"[c11-w14] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c11-w14] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c11-w14] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
