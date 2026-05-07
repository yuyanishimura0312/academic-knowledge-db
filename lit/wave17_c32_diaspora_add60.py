"""LIT-DB Phase 2 Wave 17 — C32 ADD: Diaspora Literature (+60 concepts).

Subfield: lit_diaspora (id=20). Existing 80 concepts; this wave adds 60 NEW.
Coverage: Asian American detail, Caribbean Anglo/Franco補完, Black British,
Jewish diaspora, translingual, 21c women, theory補完.
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
# A: Asian American — Chinese American (8)
# ============================================================
add(**C, name_ja="マキシン・ホン・キングストン『チャイナ・メン』",
    name_en="Maxine Hong Kingston's China Men", name_original="China Men",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="キングストンが1980年に発表した男性側の中国系米国移民史。曾祖父・祖父・父・兄弟世代の労働史を神話と織り交ぜ、米国黒人/チカーノ運動と並行する華人男性史を文学化した。",
    background="1970年代米国エスニック・スタディーズと労働史見直し。",
    development="アジア系男性表象の批評的基盤となった。",
    historical_context="1970-80年代米国の人種・労働史再考期。",
    primary_source_url=WIKI_EN+"China_Men",
    primary_source_type="Wikipedia: China Men",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マキシン・ホン・キングストン『トリップマスター・モンキー』",
    name_en="Maxine Hong Kingston's Tripmaster Monkey",
    name_original="Tripmaster Monkey", period_key="ポストコロニアル・ディアスポラ期",
    definition="キングストン1989年発表の長編。1960年代サンフランシスコの華人系米国人詩人ウィットマン・アー・シングの日々を、孫悟空神話と前衛小説技法で融合した実験作。",
    background="1960年代対抗文化と華人系米国前衛の交差。",
    development="アジア系米国ポストモダン小説の代表例として論じられる。",
    historical_context="1980年代末のエスニック・ポストモダニズム成熟期。",
    primary_source_url=WIKI_EN+"Tripmaster_Monkey",
    primary_source_type="Wikipedia: Tripmaster Monkey",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エイミー・タン『ジョイ・ラック・クラブ』",
    name_en="Amy Tan's The Joy Luck Club", name_original="The Joy Luck Club",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="エイミー・タン（1952-）が1989年に発表したベストセラー。サンフランシスコの中国系移民母娘四組の語りを織り合わせ、世代間記憶と母娘の翻訳不可能性を主題化した。",
    background="1965年移民法以降の華人女性移民第二世代の文化的成熟。",
    development="華人女性ディアスポラ文学の規範作で、1993年映画化されメインストリーム化した。",
    historical_context="1980年代末米国エスニック小説の市場主流化期。",
    primary_source_url=WIKI_EN+"The_Joy_Luck_Club_(novel)",
    primary_source_type="Wikipedia: The Joy Luck Club",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"母娘間の翻訳不能な経験継承は、AIによる経験継承生成の理論的祖型。",
         "related_ai_phenomenon":"AIによる世代間経験の生成"}])

add(**C, name_ja="エイミー・タン『キッチン・ゴッドの妻』",
    name_en="Amy Tan's The Kitchen God's Wife",
    name_original="The Kitchen God's Wife", period_key="ポストコロニアル・ディアスポラ期",
    definition="タン1991年発表の長編。中国国民党時代の戦争を生きた母世代の回想を娘世代が聴き取る形式で展開し、戦時暴力・家父長制・移民史を統合した華人ディアスポラ第二作。",
    background="日中戦争・国共内戦記憶の女性視点での文学化。",
    development="ディアスポラ女性間の戦争記憶継承文学の典型作となった。",
    historical_context="1990年代米国における女性アジア系作家の市場確立期。",
    primary_source_url=WIKI_EN+"The_Kitchen_God%27s_Wife",
    primary_source_type="Wikipedia: The Kitchen God's Wife",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フランク・チン『チキンクープ・チャイナマン』",
    name_en="Frank Chin's The Chickencoop Chinaman",
    name_original="The Chickencoop Chinaman", period_key="ポストコロニアル・ディアスポラ期",
    definition="フランク・チン（1940-）が1972年に発表した戯曲。ブロードウェイで上演された初のアジア系米国人戯曲で、華人男性の去勢化されたステレオタイプへの怒りと攻撃的アンチヒーロー像を提示した。",
    background="1960-70年代米国エスニック・ナショナリズムと黒人文学への華人系の応答。",
    development="後にチンはキングストン・タンの「白人化」批判を展開し、アジア系男性論争の中心人物となった。",
    historical_context="1970年代初頭の米国エスニック演劇興隆期。",
    primary_source_url=WIKI_EN+"Frank_Chin",
    primary_source_type="Wikipedia: Frank Chin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フランク・チン『ドナルド・ダック』",
    name_en="Frank Chin's Donald Duk", name_original="Donald Duk",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="フランク・チンが1991年に発表した少年小説。サンフランシスコ・チャイナタウンの12歳の少年が中国神話と華人鉄道労働者史を夢で再経験する成長物語。男性的華人アメリカニズムの提唱。",
    background="チンの長年の華人男性表象闘争の小説的結晶。",
    development="アジア系米国YA文学の開拓的事例となった。",
    historical_context="1990年代米国YA文学のエスニック多様化期。",
    primary_source_url=WIKI_EN+"Frank_Chin",
    primary_source_type="Wikipedia: Frank Chin",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="ギッシュ・ジェン『典型的アメリカ人』",
    name_en="Gish Jen's Typical American", name_original="Typical American",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ギッシュ・ジェン（1955-）が1991年に発表した長編。1950年代に渡米した中国人三人組の同化・成功・失敗を皮肉な視点で描き、「典型的アメリカ人」という言葉の二重性を主題化した。",
    background="1990年代初頭の華人系米国移民史の成熟期。",
    development="続編『モナ・約束の地』でユダヤ系への改宗を描き、エスニック越境文学を確立した。",
    historical_context="1990年代米国の同化と多文化主義論議の最盛期。",
    primary_source_url=WIKI_EN+"Gish_Jen",
    primary_source_type="Wikipedia: Gish Jen",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チャールズ・ユー『インテリア・チャイナタウン』",
    name_en="Charles Yu's Interior Chinatown",
    name_original="Interior Chinatown", period_key="グローバル・ディアスポラ期",
    definition="チャールズ・ユー（1976-）が2020年に発表したテレビ脚本形式の実験小説。「ジェネリック・アジア人男性」を演じる俳優の視点で、米国メディア表象のステレオタイプを脱構築。全米図書賞受賞。",
    background="2010年代米国メディアのアジア系表象問題、#StarringJohnCho運動。",
    development="2024年Hulu連続ドラマ化され、メタフィクションのメインストリーム化を象徴。",
    historical_context="2020年米国コロナ禍でのアジア系差別激化期。",
    primary_source_url=WIKI_EN+"Interior_Chinatown",
    primary_source_type="Wikipedia: Interior Chinatown",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"脚本形式の小説は、テキスト生成の枠組み転換を演出する。AI生成テキストの形式横断と並行。",
         "related_ai_phenomenon":"AI生成のジャンル横断"}])


# ============================================================
# B: Asian American — Korean/Chinese American 続 (7)
# ============================================================
add(**C, name_ja="チャンネ・リー『ネイティブ・スピーカー』",
    name_en="Chang-rae Lee's Native Speaker", name_original="Native Speaker",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="チャンネ・リー（1965-）が1995年に発表したデビュー長編。韓国系米国人スパイの語りを通じ、「ネイティブ・スピーカー」性、移民の透明化と言語的所属の問題を探究した。",
    background="1990年代米国における韓国系米国人第二世代の文学的成熟期。",
    development="韓国系米国文学の制度的代表作となり、後のミン・ジン・リー、キャシー・パーク・ホンへ繋がる。",
    historical_context="1992年LA暴動以降の韓国系米国人の自己反省期。",
    primary_source_url=WIKI_EN+"Native_Speaker_(novel)",
    primary_source_type="Wikipedia: Native Speaker",
    importance_score=4, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"「ネイティブ・スピーカー」概念の脱構築は、LLMの言語規範問題と直接共振する。",
         "related_ai_phenomenon":"LLMにおける言語ネイティブ性"}])

add(**C, name_ja="チャンネ・リー『身ぶりの一生』",
    name_en="Chang-rae Lee's A Gesture Life", name_original="A Gesture Life",
    period_key="グローバル・ディアスポラ期",
    definition="チャンネ・リーが1999年に発表した長編。日本軍従軍慰安婦の医療補助官だった在日朝鮮人が戦後に米国で「日本人」として暮らす二重ディアスポラの物語。記憶と隠蔽の倫理を主題化した。",
    background="1990年代後半の従軍慰安婦問題の国際化、ザイニチ・ディアスポラ問題の文学的探究。",
    development="トランスナショナルなコリアン・ディアスポラ文学の代表作となった。",
    historical_context="1990年代末の戦争記憶政治化期。",
    primary_source_url=WIKI_EN+"A_Gesture_Life",
    primary_source_type="Wikipedia: A Gesture Life",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ミン・ジン・リー『億万長者の食卓』",
    name_en="Min Jin Lee's Free Food for Millionaires",
    name_original="Free Food for Millionaires", period_key="グローバル・ディアスポラ期",
    definition="ミン・ジン・リー（1968-）が2007年に発表したデビュー長編。マンハッタンの韓国系米国人キャシー・ハンを主人公に、移民第二世代の階級・宗教・労働を19世紀小説的射程で描いた。",
    background="2000年代米国における韓国系米国人専門職層の興隆。",
    development="リーの『パチンコ』の前駆作として、現代韓国系米国文学の基盤を築いた。",
    historical_context="2000年代米国コリアン社会の階級多様化期。",
    primary_source_url=WIKI_EN+"Min_Jin_Lee",
    primary_source_type="Wikipedia: Min Jin Lee",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="イーユン・リー『漂泊者』",
    name_en="Yiyun Li's The Vagrants", name_original="The Vagrants",
    period_key="グローバル・ディアスポラ期",
    definition="イーユン・リー（1972-）が2009年に発表したデビュー長編。1979年中国の地方都市で文化大革命後に処刑された若い女性の日に焦点を当てた、英語で執筆する華人作家の代表作。",
    background="2000年代に米国で英語で執筆する中国大陸出身作家の興隆（ハ・ジン、リー）。",
    development="ハ・ジンと並ぶ「翻訳されない中国」の英語文学を確立した。",
    historical_context="2000年代後半の英語ヘゲモニーと中国系作家の言語選択期。",
    primary_source_url=WIKI_EN+"Yiyun_Li",
    primary_source_type="Wikipedia: Yiyun Li",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"母語中国語放棄して英語のみで創作する作家性は、AI多言語生成と作家言語選択の論争点。",
         "related_ai_phenomenon":"作家の意図的言語放棄"}])

add(**C, name_ja="イーユン・リー『理由のない場所』",
    name_en="Yiyun Li's Where Reasons End", name_original="Where Reasons End",
    period_key="グローバル・ディアスポラ期",
    definition="リーが2019年に発表した実験的悲嘆小説。自死した16歳の息子との架空の対話で構成され、ディアスポラ作家の喪失と言語の関係を主題化した。",
    background="リー自身の息子の自死(2017)後の作家的応答。",
    development="現代ディアスポラ・グリーフ文学の代表作。",
    historical_context="2010年代後半の精神健康とアジア系米国コミュニティの問題化期。",
    primary_source_url=WIKI_EN+"Yiyun_Li",
    primary_source_type="Wikipedia: Yiyun Li",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モニク・トゥルオン『塩の書』",
    name_en="Monique Truong's The Book of Salt",
    name_original="The Book of Salt", period_key="グローバル・ディアスポラ期",
    definition="モニク・トゥルオン（1968-）が2003年に発表した長編。1930年代パリのガートルード・スタイン家でベトナム人料理人として働いた架空の主人公ビンを語り手とし、亡命・植民地・クィアの交差を食を通じ描いた。",
    background="2000年代米国におけるベトナム系米国文学とクィア文学の交差。",
    development="ベトナム系・クィア・ディアスポラ文学の交叉的代表作。",
    historical_context="2000年代初頭のクィア・ディアスポラ批評の興隆期。",
    primary_source_url=WIKI_EN+"The_Book_of_Salt",
    primary_source_type="Wikipedia: The Book of Salt",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ル・ティ・ジエム・トゥイ『私たちが探していたギャングスター』",
    name_en="Le Thi Diem Thuy's The Gangster We Are All Looking For",
    name_original="The Gangster We Are All Looking For",
    period_key="グローバル・ディアスポラ期",
    definition="ル・ティ・ジエム・トゥイが2003年に発表した詩的中編。サンディエゴに移住したベトナム難民家族の少女視点で、戦争記憶と新世界の喪失を断片的散文で描いた代表作。",
    background="1980年代ベトナム難民第二世代の文学的成熟。",
    development="ヴィエト・タン・ウェン以前のベトナム系米国詩的散文の規範作。",
    historical_context="2000年代初頭のベトナム系米国第二世代文学興隆期。",
    primary_source_url=WIKI_EN+"Le_Thi_Diem_Thuy",
    primary_source_type="Wikipedia: Le Thi Diem Thuy",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="スーザン・チョイ『信頼の演習』",
    name_en="Susan Choi's Trust Exercise", name_original="Trust Exercise",
    period_key="グローバル・ディアスポラ期",
    definition="スーザン・チョイ（1969-）が2019年に発表した全米図書賞受賞作。芸術高校を舞台にしたメタフィクション。韓国系米国人作家による語りの権威・性的合意・記憶の倫理の小説的探究。",
    background="2010年代後半の#MeToo運動と語りの権威の問題化。",
    development="韓国系米国文学のメタフィクション的展開を象徴。",
    historical_context="2019年#MeToo以降の米国文学の権威批判期。",
    primary_source_url=WIKI_EN+"Trust_Exercise",
    primary_source_type="Wikipedia: Trust Exercise",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# C: Caribbean Anglophone補完 (7)
# ============================================================
add(**C, name_ja="V・S・ナイポール『ミミック・メン』",
    name_en="V.S. Naipaul's The Mimic Men", name_original="The Mimic Men",
    period_key="脱植民地・初期移民文学期",
    definition="V・S・ナイポール（1932-2018）が1967年に発表した長編。架空のカリブ島出身政治家のロンドン亡命回想形式で、ポストコロニアル主体の「擬態」と無根性を主題化した。バーバ「擬態」論の文学的典型。",
    background="1960年代カリブ独立期の幻滅、ナイポール自身のトリニダード・インド系経験。",
    development="後のホミ・バーバ「コロニアル擬態」概念の文学的源流の一つとなった。",
    historical_context="1960年代後半カリブ独立後の幻滅期。",
    primary_source_url=WIKI_EN+"The_Mimic_Men",
    primary_source_type="Wikipedia: The Mimic Men",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"擬態と植民地主体",
         "description":"ナイポールの擬態描写はポストコロニアル人類学の擬態研究と並行する。"}])

add(**C, name_ja="V・S・ナイポール『川の湾曲』",
    name_en="V.S. Naipaul's A Bend in the River",
    name_original="A Bend in the River", period_key="ポストコロニアル・ディアスポラ期",
    definition="ナイポールが1979年に発表した代表的長編。脱植民地化アフリカ内陸の架空国を舞台に、東アフリカ・インド系商人の主体形成を描いた。コンラッド『闇の奥』のポストコロニアル書き換え。",
    background="1970年代のポストコロニアル・アフリカの政治混乱、ナイポールの世界旅行ジャーナリズム。",
    development="ポストコロニアル幻滅文学の代表作として論争を呼んだ。",
    historical_context="1970年代後半のポストコロニアル・アフリカ批判期。",
    primary_source_url=WIKI_EN+"A_Bend_in_the_River",
    primary_source_type="Wikipedia: A Bend in the River",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="サム・セルヴォン『孤独なロンドン人』",
    name_en="Sam Selvon's The Lonely Londoners",
    name_original="The Lonely Londoners", period_key="脱植民地・初期移民文学期",
    definition="サム・セルヴォン（1923-1994）が1956年に発表した長編。戦後ロンドンに移住したカリブ移民「ウィンドラッシュ世代」の経験を、トリニダード・クレオール英語で描いた英国カリブ・ディアスポラ文学の創成作。",
    background="1948年エンパイア・ウィンドラッシュ号到着以降のカリブ系英国移民の文学的成熟。",
    development="後のカリル・フィリップス、アンドレア・レヴィ、ザディー・スミスの黒人英国文学の基盤を築いた。",
    historical_context="1950年代英国の脱植民地化と移民流入期。",
    primary_source_url=WIKI_EN+"The_Lonely_Londoners",
    primary_source_type="Wikipedia: The Lonely Londoners",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"英語標準語へのクレオール介入は、LLMの方言・非標準言語表象問題の文学的祖型。",
         "related_ai_phenomenon":"LLMにおけるクレオール表象"}])

add(**C, name_ja="ジョージ・ラミング『亡命者の喜び』",
    name_en="George Lamming's The Pleasures of Exile",
    name_original="The Pleasures of Exile", period_key="脱植民地・初期移民文学期",
    definition="ジョージ・ラミング（1927-2022）が1960年に発表したエッセイ集。シェイクスピア『テンペスト』のキャリバン読み直しを中心に、カリブ知識人の英国亡命経験を理論化した。ポストコロニアル批評の先駆。",
    background="1950年代カリブ知識人のロンドン移住、植民地主体の自己理論化要求。",
    development="ファノン、サイードに先駆けるポストコロニアル理論の創成的テキストとなった。",
    historical_context="1960年カリブ独立期の知的覚醒期。",
    primary_source_url=WIKI_EN+"George_Lamming",
    primary_source_type="Wikipedia: George Lamming",
    importance_score=4, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"キャリバン的主体の言語的逆襲はAI時代の周縁主体の自己表象問題の祖型。",
         "related_ai_phenomenon":"AI時代の周縁主体表象"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"キャリバン哲学",
         "description":"ラミングのキャリバン読みはセゼール、レタマール、シルヴィア・ウィンターのキャリバン哲学と並行する。"}])

add(**C, name_ja="ジャマイカ・キンケイド『アニー・ジョン』",
    name_en="Jamaica Kincaid's Annie John", name_original="Annie John",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ジャマイカ・キンケイド（1949-）が1985年に発表したアンティグア出身少女の成長物語。母娘関係と植民地教育の重なりを、抑制された一人称で描いた女性カリブ・ディアスポラ文学の規範作。",
    background="1980年代米国における女性カリブ系作家の興隆。",
    development="続く『ルーシー』『母の自伝』とともにキンケイドの母娘三部作を構成。",
    historical_context="1980年代英米のフェミニスト文学興隆期。",
    primary_source_url=WIKI_EN+"Annie_John",
    primary_source_type="Wikipedia: Annie John",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ジャマイカ・キンケイド『母の自伝』",
    name_en="Jamaica Kincaid's The Autobiography of My Mother",
    name_original="The Autobiography of My Mother",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="キンケイドが1996年に発表した長編。ドミニカ島カリブ系女性シューラ・クローデットの一人称で、母を持たぬ娘の植民地的孤独を反母性的に描いた。フェミニスト・ポストコロニアル批評の中心テクスト。",
    background="1990年代のキンケイド母娘テーマの暗い極致化。",
    development="女性カリブ・ディアスポラ批評の中心テクストとなった。",
    historical_context="1990年代後半のポストコロニアル・フェミニズム成熟期。",
    primary_source_url=WIKI_EN+"The_Autobiography_of_My_Mother",
    primary_source_type="Wikipedia: The Autobiography of My Mother",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エドウィージ・ダンティカ『骨の収穫』",
    name_en="Edwidge Danticat's The Farming of Bones",
    name_original="The Farming of Bones", period_key="ポストコロニアル・ディアスポラ期",
    definition="エドウィージ・ダンティカ（1969-）が1998年に発表した長編。1937年トルヒーリョ政権下のドミニカ共和国「パセリ虐殺」を生き残るハイチ系女性労働者を描いた、ハイチ系米国ディアスポラ文学の重要作。",
    background="1990年代後半のハイチ系米国第二世代の文学的成熟。",
    development="ダンティカの『息、目、記憶』『クリック・クラック！』とともにハイチ系ディアスポラ文学の基盤を築いた。",
    historical_context="1990年代後半の米国エスニック文学の歴史的事件への注目期。",
    primary_source_url=WIKI_EN+"The_Farming_of_Bones",
    primary_source_type="Wikipedia: The Farming of Bones",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マーロン・ジェイムズ『七つの殺人の簡潔な歴史』",
    name_en="Marlon James's A Brief History of Seven Killings",
    name_original="A Brief History of Seven Killings",
    period_key="グローバル・ディアスポラ期",
    definition="マーロン・ジェイムズ（1970-）が2014年に発表した700頁を超える多声長編。1976年ボブ・マーリー暗殺未遂を中心に、ジャマイカ・ニューヨーク・マイアミの暴力と政治を76人の語り手で展開。2015年ブッカー賞。",
    background="2010年代ジャマイカ系米国文学の批評的成熟、グローバル・サウス文学の世界文学化。",
    development="2015年ブッカー賞でカリブ系作家初の同賞英国国籍外受賞となり、世界文学の地理的拡張を象徴した。",
    historical_context="2010年代世界文学の中心地理移動期。",
    primary_source_url=WIKI_EN+"A_Brief_History_of_Seven_Killings",
    primary_source_type="Wikipedia: A Brief History of Seven Killings",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"声","status":"rethinking",
         "rationale":"76の語り手による多声構成は、LLMによる多声生成の文学的祖型。",
         "related_ai_phenomenon":"LLM多声テキスト生成"}])


# ============================================================
# D: Caribbean Francophone補完 (6)
# ============================================================
add(**C, name_ja="マリーズ・コンデ『私、ティテュバ、サレムの黒い魔女』",
    name_en="Maryse Condé's I, Tituba", name_original="Moi, Tituba sorcière…",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="マリーズ・コンデ（1934-2024）が1986年に発表した長編。1692年セイラム魔女裁判の被告ティテュバを語り手とし、奴隷・女性・カリブの三重周縁を文学化したカリブ・フェミニスト歴史小説の代表作。",
    background="1980年代のフェミニスト歴史見直しと黒人女性史の文学化。",
    development="コンデの代表作の一つとなり、後のカリブ系・アフリカ系米国フェミニスト文学に深く影響した。",
    historical_context="1980年代後半フェミニスト歴史見直し期。",
    primary_source_url=WIKI_EN+"I,_Tituba,_Black_Witch_of_Salem",
    primary_source_type="Wikipedia: I, Tituba",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マリーズ・コンデ『マングローブの渡り』",
    name_en="Maryse Condé's Crossing the Mangrove",
    name_original="Traversée de la mangrove",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="コンデが1989年に発表したグアドループ村落小説。謎の死者を巡る20人の村人の語りで構成され、シャモワゾーらのクレオリテに対する女性的・ディアスポラ的応答。",
    background="1980年代カリブ・クレオリテ運動への女性側の応答要求。",
    development="シャモワゾー・コンフィアンの男性的クレオリテへの女性的批判として位置づけられた。",
    historical_context="1980年代末カリブ文学のジェンダー議論期。",
    primary_source_url=WIKI_EN+"Maryse_Cond%C3%A9",
    primary_source_type="Wikipedia: Maryse Condé",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パトリック・シャモワゾー『ソリボ・マニフィーク』",
    name_en="Patrick Chamoiseau's Solibo Magnifique",
    name_original="Solibo Magnifique", period_key="ポストコロニアル・ディアスポラ期",
    definition="パトリック・シャモワゾー（1953-）が1988年に発表した長編。フランス標準語で死亡したマルティニーク民話語りソリボの謎を、警察捜査と民俗誌が交差する形式で描いた。クレオール口承の書記化問題を主題化。",
    background="1980年代マルティニーク・クレオール文化喪失への危機感。",
    development="シャモワゾーのクレオリテ運動の文学的中核作品となった。",
    historical_context="1980年代後半のクレオリテ運動最盛期。",
    primary_source_url=WIKI_EN+"Patrick_Chamoiseau",
    primary_source_type="Wikipedia: Patrick Chamoiseau",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パトリック・シャモワゾー『古き奴隷と犬』",
    name_en="Patrick Chamoiseau's Slave Old Man",
    name_original="L'esclave vieil homme et le molosse",
    period_key="グローバル・ディアスポラ期",
    definition="シャモワゾーが1997年に発表した中編。マルティニーク奴隷時代に逃亡する老奴隷と追跡犬の対峙を、詩的散文とクレオール語の混淆で描いた奴隷制記憶の文学的記念碑。",
    background="1990年代後半カリブの奴隷制記憶の文学的再活性化。",
    development="現代カリブ・フランコフォン文学の典型作の一つとなった。",
    historical_context="1990年代末の奴隷制記憶政治化期。",
    primary_source_url=WIKI_EN+"Patrick_Chamoiseau",
    primary_source_type="Wikipedia: Patrick Chamoiseau",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エドゥアール・グリッサン『裂け目』",
    name_en="Édouard Glissant's La Lézarde", name_original="La Lézarde",
    period_key="脱植民地・初期移民文学期",
    definition="エドゥアール・グリッサン（1928-2011）が1958年に発表したデビュー長編（ルノードー賞受賞）。マルティニーク独立運動と若者集団の政治的覚醒を河流の象徴で描き、後のクレオライゼーション理論の文学的源泉。",
    background="1950年代マルティニーク独立運動とフランス共和国との緊張。",
    development="グリッサン後期理論（クレオライゼーション、関係の詩学）の文学的源流となった。",
    historical_context="1950年代後半マルティニーク政治覚醒期。",
    primary_source_url=WIKI_EN+"%C3%89douard_Glissant",
    primary_source_type="Wikipedia: Édouard Glissant",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シモーヌ・シュヴァルツ=バルト『風と雨のテリュメ・ミラクル』",
    name_en="Simone Schwarz-Bart's The Bridge of Beyond",
    name_original="Pluie et vent sur Télumée Miracle",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="シモーヌ・シュヴァルツ=バルト（1938-）が1972年に発表したグアドループの女性四世代物語。クレオール口承の女性版として、奴隷後カリブの女性の記憶と生活誌を詩的に展開した。",
    background="1970年代カリブ・フランコフォン文学への女性側の貢献。",
    development="フランコフォン・カリブ女性文学の規範作の一つとなった。",
    historical_context="1970年代仏領アンティルの女性作家興隆期。",
    primary_source_url=WIKI_EN+"Simone_Schwarz-Bart",
    primary_source_type="Wikipedia: Simone Schwarz-Bart",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: Black British (5)
# ============================================================
add(**C, name_ja="アンドレア・レヴィ『ロング・ソング』",
    name_en="Andrea Levy's The Long Song", name_original="The Long Song",
    period_key="グローバル・ディアスポラ期",
    definition="アンドレア・レヴィ（1956-2019）が2010年に発表したジャマイカ奴隷制末期を舞台にする歴史小説。元奴隷ジュリーの語りで、奴隷制から解放への転換期を脱英雄的に描いた黒人英国文学の代表作。",
    background="2000年代英国における奴隷貿易廃止200周年記念と歴史見直し。",
    development="レヴィの『スモール・アイランド』に並ぶ黒人英国歴史文学の中心作品となった。",
    historical_context="2007年大英帝国奴隷貿易廃止200周年期。",
    primary_source_url=WIKI_EN+"The_Long_Song",
    primary_source_type="Wikipedia: The Long Song",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ベルナーディン・エヴァリスト『ミスター・ラヴァーマン』",
    name_en="Bernardine Evaristo's Mr Loverman",
    name_original="Mr Loverman", period_key="グローバル・ディアスポラ期",
    definition="ベルナーディン・エヴァリスト（1959-）が2013年に発表した長編。74歳の同性愛アンティグア系英国人バリーを主人公とし、黒人クィア老年とディアスポラを陽気な散文で描いた。",
    background="2010年代英国の黒人クィア文学興隆。",
    development="エヴァリストの2019年ブッカー賞『少女、女、その他』へ繋がる代表作。",
    historical_context="2010年代英国LGBTQ文学のメインストリーム化期。",
    primary_source_url=WIKI_EN+"Bernardine_Evaristo",
    primary_source_type="Wikipedia: Bernardine Evaristo",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="カリル・フィリップス『川を渡る』",
    name_en="Caryl Phillips's Crossing the River",
    name_original="Crossing the River", period_key="ポストコロニアル・ディアスポラ期",
    definition="カリル・フィリップス（1958-）が1993年に発表した代表作。ブッカー賞最終候補。三世紀にわたる黒人ディアスポラの三人物語を父の声で繋ぎ、ブラック・アトランティックの文学的形象化を達成した。",
    background="1990年代初頭のポール・ギルロイ『ブラック・アトランティック』(1993)同時代の文学的応答。",
    development="フィリップスの『ケンブリッジ』とともに英国黒人ディアスポラ歴史文学の規範作となった。",
    historical_context="1990年代初頭のブラック・アトランティック理論興隆期。",
    primary_source_url=WIKI_EN+"Crossing_the_River",
    primary_source_type="Wikipedia: Crossing the River",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ブラック・アトランティック",
         "description":"フィリップスの三世紀構成はギルロイのブラック・アトランティック理論の文学的具体化。"}])

add(**C, name_ja="ハニフ・クレイシ『郊外の仏陀』",
    name_en="Hanif Kureishi's The Buddha of Suburbia",
    name_original="The Buddha of Suburbia", period_key="ポストコロニアル・ディアスポラ期",
    definition="ハニフ・クレイシ（1954-）が1990年に発表したデビュー長編（ホーソンデン賞）。インド系英国人カリムを主人公とする1970-80年代ロンドン郊外青春小説で、英国第二世代南アジア系文学を確立した。",
    background="1980-90年代英国南アジア系第二世代の文学的成熟。",
    development="後のザディー・スミス『ホワイト・ティース』、モニカ・アリ『ブリック・レーン』へ繋がる規範作。",
    historical_context="1990年代初頭の英国多文化主義論議期。",
    primary_source_url=WIKI_EN+"The_Buddha_of_Suburbia_(novel)",
    primary_source_type="Wikipedia: The Buddha of Suburbia",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ザディー・スミス『ホワイト・ティース』",
    name_en="Zadie Smith's White Teeth", name_original="White Teeth",
    period_key="グローバル・ディアスポラ期",
    definition="ザディー・スミス（1975-）が2000年に発表したデビュー長編。北ロンドンの英国・バングラデシュ系・ジャマイカ系の三家族の三世代物語で、現代英国多文化主義の文学的記念碑となった。",
    background="1990年代後半のロンドン多文化主義成熟期。",
    development="21世紀英国黒人・南アジア系ディアスポラ文学の中心作品となった。",
    historical_context="2000年ブレア政権下英国多文化主義黄金期。",
    primary_source_url=WIKI_EN+"White_Teeth",
    primary_source_type="Wikipedia: White Teeth",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"複数ディアスポラ家族の交錯は、AI時代の混合主体形成の文学的祖型。",
         "related_ai_phenomenon":"AI時代の混合主体形成"}])


# ============================================================
# F: Jewish Diaspora (8)
# ============================================================
add(**C, name_ja="ソール・ベロー『オーギー・マーチの冒険』",
    name_en="Saul Bellow's The Adventures of Augie March",
    name_original="The Adventures of Augie March",
    period_key="脱植民地・初期移民文学期",
    definition="ソール・ベロー（1915-2005）が1953年に発表した全米図書賞受賞長編。シカゴのユダヤ系米国人オーギー・マーチの自由放浪を描き、「私はアメリカ人、シカゴ生まれ」の冒頭でユダヤ系米国小説の主流化を象徴した。",
    background="1950年代米国ユダヤ系移民第二世代の文学的覚醒。",
    development="ベローの代表作の一つで、後のロス、マラマッドへの道を開いた。",
    historical_context="1950年代米国ユダヤ系文学の主流化期。",
    primary_source_url=WIKI_EN+"The_Adventures_of_Augie_March",
    primary_source_type="Wikipedia: The Adventures of Augie March",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ソール・ベロー『ハーツォグ』",
    name_en="Saul Bellow's Herzog", name_original="Herzog",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ベローが1964年に発表した全米図書賞受賞長編。中年ユダヤ系米国人モーゼス・ハーツォグの哲学的書簡形式の独白で、知的ユダヤ系米国人の中年危機と西洋思想史を融合した。",
    background="1960年代米国ユダヤ系知識人の最盛期。",
    development="ベロー1976年ノーベル文学賞受賞の中心作品。",
    historical_context="1960年代米国知的文化の最盛期。",
    primary_source_url=WIKI_EN+"Herzog_(novel)",
    primary_source_type="Wikipedia: Herzog",
    importance_score=4, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="バーナード・マラマッド『修理屋』",
    name_en="Bernard Malamud's The Fixer", name_original="The Fixer",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="バーナード・マラマッド（1914-1986）が1966年に発表したピューリッツァー賞・全米図書賞受賞長編。20世紀初頭ロシアの実在のメンデル・ベイリス血の中傷事件をもとに、東欧ユダヤ系の苦難と尊厳を描いた。",
    background="1960年代米国における東欧ユダヤ系記憶の文学的継承。",
    development="マラマッドの代表作で、ホロコースト前史の文学的記念碑となった。",
    historical_context="1960年代米国ユダヤ系文学のホロコースト前史化期。",
    primary_source_url=WIKI_EN+"The_Fixer_(Malamud_novel)",
    primary_source_type="Wikipedia: The Fixer",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フィリップ・ロス『ポートノイの不平不満』",
    name_en="Philip Roth's Portnoy's Complaint",
    name_original="Portnoy's Complaint", period_key="ポストコロニアル・ディアスポラ期",
    definition="フィリップ・ロス（1933-2018）が1969年に発表したベストセラー。精神分析の独白形式でユダヤ系米国人男性の性的・家族的神経症をスキャンダラスに展開した、ユダヤ系米国文学の転機作。",
    background="1960年代末米国の性革命と精神分析文化の交差。",
    development="ロスの数十年に及ぶ作家的挑発の起点となり、ユダヤ系コミュニティ内論争を呼んだ。",
    historical_context="1969年米国性革命期。",
    primary_source_url=WIKI_EN+"Portnoy%27s_Complaint",
    primary_source_type="Wikipedia: Portnoy's Complaint",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="フィリップ・ロス『アメリカン・パストラル』",
    name_en="Philip Roth's American Pastoral",
    name_original="American Pastoral", period_key="グローバル・ディアスポラ期",
    definition="ロスが1997年に発表したピューリッツァー賞受賞長編。ユダヤ系米国人「スウェード」レヴォブの理想的米国生活が娘のテロで崩壊する物語で、戦後米国の幻想と現実を主題化した。",
    background="1990年代後半米国の世紀末歴史見直し期。",
    development="ロスのアメリカン三部作の中核作で、戦後米国文学の到達点とされる。",
    historical_context="1990年代末米国歴史小説興隆期。",
    primary_source_url=WIKI_EN+"American_Pastoral",
    primary_source_type="Wikipedia: American Pastoral",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="シンシア・オジック『ショール』",
    name_en="Cynthia Ozick's The Shawl", name_original="The Shawl",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="シンシア・オジック（1928-）が1989年に発表した中編連作。ホロコースト収容所で乳児を失った女性ローザの記憶と亡命後の生を、抑制された詩的散文で描いた。米国ユダヤ系ホロコースト文学の規範作。",
    background="1980年代米国における第二世代ホロコースト文学の興隆。",
    development="オジックのホロコースト批評（『芸術と熱情』）と並行する文学的代表作。",
    historical_context="1980年代後半米国ホロコースト記憶政治化期。",
    primary_source_url=WIKI_EN+"The_Shawl_(short_story)",
    primary_source_type="Wikipedia: The Shawl",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ニコール・クラウス『愛の歴史』",
    name_en="Nicole Krauss's The History of Love",
    name_original="The History of Love", period_key="グローバル・ディアスポラ期",
    definition="ニコール・クラウス（1974-）が2005年に発表した長編。ホロコースト生存者レオ・ガースキーとブルックリン少女アルマの並行する物語で、第三世代ホロコースト・ポストメモリー文学を確立した。",
    background="2000年代米国第三世代ホロコースト文学の成熟。",
    development="クラウスの『偉大な家』と並ぶ第三世代ユダヤ系米国文学の中心作品。",
    historical_context="2000年代後半第三世代ホロコースト記憶の文学化期。",
    primary_source_url=WIKI_EN+"The_History_of_Love",
    primary_source_type="Wikipedia: The History of Love",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"第三世代の経験なき記憶継承は、AIの学習データに基づく経験生成と理論的に共振する。",
         "related_ai_phenomenon":"AIの第三者記憶生成"}])

add(**C, name_ja="マイケル・シェイボン『カヴァリエ＆クレイの驚くべき冒険』",
    name_en="Michael Chabon's The Amazing Adventures of Kavalier & Clay",
    name_original="The Amazing Adventures of Kavalier & Clay",
    period_key="グローバル・ディアスポラ期",
    definition="マイケル・シェイボン（1963-）が2000年に発表したピューリッツァー賞受賞長編。プラハからNYに逃れたユダヤ系移民とブルックリン従兄弟がコミック黄金時代を築く物語で、ユダヤ系大衆文化と歴史を融合した。",
    background="2000年米国ユダヤ系文学の歴史小説的転回。",
    development="シェイボンの『イディッシュ警察組合』と並ぶユダヤ系オルタナ歴史小説の代表作。",
    historical_context="2000年代米国ポップカルチャー的歴史小説興隆期。",
    primary_source_url=WIKI_EN+"The_Amazing_Adventures_of_Kavalier_%26_Clay",
    primary_source_type="Wikipedia: Kavalier & Clay",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# G: Translingual & 21c women (8)
# ============================================================
add(**C, name_ja="アレクサンドル・ヘモン『ブルーノの問題』",
    name_en="Aleksandar Hemon's The Question of Bruno",
    name_original="The Question of Bruno", period_key="グローバル・ディアスポラ期",
    definition="アレクサンドル・ヘモン（1964-）が2000年に発表したデビュー短編集。1992年シカゴ訪問中のサラエヴォ包囲で帰国不能となったボスニア系作家による、英語亡命創作の創成作。",
    background="1990年代ユーゴ戦争による作家の意図せぬ亡命と英語転換。",
    development="ヘモンの『ノーホエア・マン』『ラザロ計画』と並ぶ亡命英語文学の中核作。",
    historical_context="1990年代末バルカン戦争難民の文学的応答期。",
    primary_source_url=WIKI_EN+"Aleksandar_Hemon",
    primary_source_type="Wikipedia: Aleksandar Hemon",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"30歳での母語放棄と英語創作は、AI時代の言語選択と作家性の問題を再考する基準。",
         "related_ai_phenomenon":"成人後の言語転換とAI"}])

add(**C, name_ja="多和田葉子『雪の練習生』",
    name_en="Yoko Tawada's Memoirs of a Polar Bear",
    name_original="雪の練習生", period_key="グローバル・ディアスポラ期",
    definition="多和田葉子（1960-）が2011年に日本語で、2014年にドイツ語版『Etüden im Schnee』として発表した三世代の北極熊家族の物語。種を超えた語りで、エクソフォニックなディアスポラの理論的拡張を達成した。",
    background="2000年代多和田の日独二言語創作の成熟。",
    development="エクソフォニック文学の理論的代表作となり、英訳でも高く評価された。",
    historical_context="2010年代世界文学のポスト人間主義転回期。",
    primary_source_url=WIKI_EN+"Yoko_Tawada",
    primary_source_type="Wikipedia: Yoko Tawada",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"非人間主体（北極熊）の語りは、AI主体性の文学的祖型として読める。",
         "related_ai_phenomenon":"非人間主体の語り"}])

add(**C, name_ja="多和田葉子『献灯使』",
    name_en="Yoko Tawada's The Emissary", name_original="献灯使",
    period_key="グローバル・ディアスポラ期",
    definition="多和田葉子が2014年に発表した近未来日本ディストピア中編。鎖国した日本で老人が永遠に老いず若者が病弱に育つ世界を描き、英訳『The Emissary』(2018)で全米図書賞翻訳部門受賞。",
    background="2011年福島原発事故後のエクソフォニック作家による日本社会診断。",
    development="多和田の世界文学的承認の決定打となった。",
    historical_context="2010年代後半の日本ポスト原発文学興隆期。",
    primary_source_url=WIKI_EN+"The_Emissary_(Tawada)",
    primary_source_type="Wikipedia: The Emissary",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="テレサ・ハッキョン・チャ『ディクテ』",
    name_en="Theresa Hak Kyung Cha's Dictee", name_original="Dictee",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="テレサ・ハッキョン・チャ（1951-1982）が1982年に発表した実験テキスト。韓国系移民女性の言語的・歴史的記憶を多言語写真詩文の混淆形式で展開した、アジア系米国前衛フェミニズムの礎石。",
    background="1980年代初頭の韓国系米国フェミニスト前衛文学の創成。",
    development="後にカンディス・チュ、リサ・ロウ等のアジア系米国批評の中心テクストとなった。",
    historical_context="1980年代初頭米国の女性前衛文学興隆期。",
    primary_source_url=WIKI_EN+"Dictee",
    primary_source_type="Wikipedia: Dictee",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"多言語・多形式の混淆テキストは、AIマルチモーダル生成の文学的祖型。",
         "related_ai_phenomenon":"AIマルチモーダルテキスト生成"}])

add(**C, name_ja="ヤー・ジャシ『ホームゴーイング』",
    name_en="Yaa Gyasi's Homegoing", name_original="Homegoing",
    period_key="グローバル・ディアスポラ期",
    definition="ヤー・ジャシ（1989-）が2016年に発表したデビュー長編。18世紀ガーナの異母姉妹の家系を300年・14章で辿り、奴隷制とその後を大西洋の両岸で描いた。新世代アフリカ系ディアスポラ文学の代表作。",
    background="2010年代米国のアフリカ系第二世代「アフロポリタン」文学の興隆。",
    development="チママンダ・アディーチェ、テジュ・コール、イムボロ・ンブエらと並ぶアフロポリタン文学の中心作。",
    historical_context="2010年代後半の米国Black Lives Matter運動と歴史見直し期。",
    primary_source_url=WIKI_EN+"Homegoing_(Gyasi_novel)",
    primary_source_type="Wikipedia: Homegoing",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="アクウェケ・エメジ『フレッシュウォーター』",
    name_en="Akwaeke Emezi's Freshwater", name_original="Freshwater",
    period_key="グローバル・ディアスポラ期",
    definition="アクウェケ・エメジ（1987-）が2018年に発表したデビュー長編。イボ族のオグバンジェ精霊観念を生きるノンバイナリー主人公アダの物語で、アフリカ系ディアスポラ・クィア・霊的存在論の交差を達成した。",
    background="2010年代後半アフリカ系ディアスポラのクィア・トランス文学の興隆。",
    development="アフリカ哲学とクィア理論を架橋する21世紀ディアスポラ文学の典型作となった。",
    historical_context="2010年代末のアフリカ・トランス文学の世界文学化期。",
    primary_source_url=WIKI_EN+"Freshwater_(novel)",
    primary_source_type="Wikipedia: Freshwater",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"複数霊的主体性の同居は、AI主体性の多元化の文学的祖型。",
         "related_ai_phenomenon":"AI多元主体性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アフリカ存在論",
         "description":"エメジのオグバンジェ存在論はアフリカ哲学の存在論的多元性と並行する。"}])

add(**C, name_ja="マーザ・メンギステ『ライオンの足元で』",
    name_en="Maaza Mengiste's Beneath the Lion's Gaze",
    name_original="Beneath the Lion's Gaze", period_key="グローバル・ディアスポラ期",
    definition="マーザ・メンギステ（1971-）が2010年に発表したデビュー長編。1974年エチオピア革命下の医師家族を描き、エチオピア系米国ディアスポラ文学を確立した。",
    background="2010年代米国におけるエチオピア系・東アフリカ系第二世代の文学的成熟。",
    development="アフリカの非西アフリカ系ディアスポラ文学の重要作。",
    historical_context="2010年代米国アフロポリタン文学興隆期。",
    primary_source_url=WIKI_EN+"Maaza_Mengiste",
    primary_source_type="Wikipedia: Maaza Mengiste",
    importance_score=3, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="チネロ・オクパランタ『ウダラの木の下で』",
    name_en="Chinelo Okparanta's Under the Udala Trees",
    name_original="Under the Udala Trees", period_key="グローバル・ディアスポラ期",
    definition="チネロ・オクパランタ（1981-）が2015年に発表した長編。ビアフラ戦争期ナイジェリアのレズビアン少女の成長物語で、アフリカ・クィア・ディアスポラ文学の規範作となった。",
    background="2010年代アフリカLGBTQ文学のグローバル化、ナイジェリア反同性愛法批判。",
    development="チママンダ・アディーチェ以降のアフリカ系米国女性作家の代表作の一つ。",
    historical_context="2014年ナイジェリア反同性愛法後の文学応答期。",
    primary_source_url=WIKI_EN+"Under_the_Udala_Trees",
    primary_source_type="Wikipedia: Under the Udala Trees",
    importance_score=3, source_tier="secondary", canonical_in_region="major")


# ============================================================
# H: Diaspora theory補完 (10) - mostly primary
# ============================================================
add(**C, name_ja="アヴタール・ブラー『ディアスポラの地図』",
    name_en="Avtar Brah's Cartographies of Diaspora",
    name_original="Cartographies of Diaspora",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="アヴタール・ブラー（1944-）が1996年に発表した代表的理論書。「ディアスポラ空間（diaspora space）」概念を導入し、ジェンダー・人種・階級の交差点としてディアスポラを再定義した英国フェミニスト・ディアスポラ理論の礎石。",
    background="1990年代の英国南アジア系フェミニスト批評の興隆。",
    development="後のスチュアート・ホール、ポール・ギルロイのディアスポラ論と並ぶ英国カルチュラル・スタディーズの中心テクストとなった。",
    historical_context="1990年代後半の英国カルチュラル・スタディーズ最盛期。",
    primary_source_url=WIKI_EN+"Diaspora_studies",
    primary_source_type="Wikipedia: Diaspora studies",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ディアスポラ空間概念は、AI時代の境界横断的主体形成の理論的基盤。",
         "related_ai_phenomenon":"AI境界横断主体"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ディアスポラ空間",
         "description":"ブラーのディアスポラ空間論は人類学的トランスナショナリズム研究と並行する。"}])

add(**C, name_ja="ヴィジャイ・ミシュラ『ディアスポラ的想像力』",
    name_en="Vijay Mishra's The Literature of the Indian Diaspora",
    name_original="The Literature of the Indian Diaspora",
    period_key="グローバル・ディアスポラ期",
    definition="ヴィジャイ・ミシュラが2007年に発表した代表的理論書。「古いディアスポラ（年期奉公）」と「新しいディアスポラ（資本のディアスポラ）」の区分を確立し、インド系ディアスポラ文学批評の理論的基盤を提供した。",
    background="2000年代インド系ディアスポラ文学のグローバル化。",
    development="ナイポール、ラシュディ、ラヒリ、ミストリー研究の主要枠組みとなった。",
    historical_context="2000年代後半のインド系ディアスポラ批評の理論化期。",
    primary_source_url=WIKI_EN+"Vijay_Mishra",
    primary_source_type="Wikipedia: Vijay Mishra",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジェイムズ・クリフォード『ルーツ／ルート』",
    name_en="James Clifford's Routes", name_original="Routes",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ジェイムズ・クリフォード（1945-）が1997年に発表した代表的理論書。「ルーツ（roots）」から「ルート（routes）」への転換を提唱し、定住的アイデンティティを移動的アイデンティティで置換するディアスポラ理論の礎石。",
    background="1990年代後半人類学的アイデンティティ論の移動的転換。",
    development="後のアパデュライ、グルッパ、ハンナーズの「移動の人類学」の中心テクストとなった。",
    historical_context="1990年代末グローバリゼーション理論興隆期。",
    primary_source_url=WIKI_EN+"James_Clifford_(historian)",
    primary_source_type="Wikipedia: James Clifford",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ルーツとルート",
         "description":"クリフォードの転換は人類学全体のパラダイム移行を体現する。"}])

add(**C, name_ja="スチュアート・ホール「文化的アイデンティティとディアスポラ」",
    name_en="Stuart Hall's Cultural Identity and Diaspora",
    name_original="Cultural Identity and Diaspora",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="スチュアート・ホール（1932-2014）が1990年に発表した記念碑的論文。文化的アイデンティティを本質ではなく「位置取り（positioning）」として再定義し、カリブ・ディアスポラ理論の礎石となった。",
    background="1980年代英国カルチュラル・スタディーズ最盛期。",
    development="ホール最大の影響をもつ単独論文となり、ディアスポラ研究の理論的中核となった。",
    historical_context="1990年文化研究のディアスポラ的転回期。",
    primary_source_url=WIKI_EN+"Stuart_Hall_(cultural_theorist)",
    primary_source_type="Wikipedia: Stuart Hall",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"アイデンティティ＝位置取り論は、AI時代の主体性可塑性を理解する理論的基盤。",
         "related_ai_phenomenon":"AI時代の主体可塑性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"位置取りとしてのアイデンティティ",
         "description":"ホールの位置取り論はバトラーのパフォーマティヴィティ論と並行する。"}])

add(**C, name_ja="ポール・ギルロイ『ポストコロニアルなメランコリア』",
    name_en="Paul Gilroy's Postcolonial Melancholia",
    name_original="Postcolonial Melancholia",
    period_key="グローバル・ディアスポラ期",
    definition="ポール・ギルロイ（1956-）が2005年に発表した理論書。英国の帝国喪失後の「メランコリア」を診断し、9.11以降の人種主義復活への文化批判を展開した。ディアスポラ批評の現代的展開。",
    background="2000年代英国の帝国記憶政治と人種主義復活。",
    development="『ブラック・アトランティック』(1993)に続くギルロイの代表的批評書となった。",
    historical_context="2000年代後半英国の人種主義論議激化期。",
    primary_source_url=WIKI_EN+"Paul_Gilroy",
    primary_source_type="Wikipedia: Paul Gilroy",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"メランコリア政治",
         "description":"ギルロイのメランコリア論はフロイト・バトラーのメランコリア概念のポストコロニアル展開。"}])

add(**C, name_ja="エングセン・ホー『タリムの墓』",
    name_en="Engseng Ho's The Graves of Tarim",
    name_original="The Graves of Tarim", period_key="グローバル・ディアスポラ期",
    definition="エングセン・ホーが2006年に発表したインド洋ハドラミー・ディアスポラの民族誌的歴史書。500年にわたるイエメン系東南アジア・東アフリカ離散を追跡し、海洋ディアスポラ理論の代表作となった。",
    background="2000年代のインド洋世界研究の興隆。",
    development="アフロ・アジア・ディアスポラ理論の中心テクストとなった。",
    historical_context="2000年代海洋ディアスポラ研究興隆期。",
    primary_source_url=WIKI_EN+"Engseng_Ho",
    primary_source_type="Wikipedia: Engseng Ho",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"海洋ディアスポラ",
         "description":"ホーの海洋ディアスポラ論は人類学的トランスナショナリズム研究の中心。"}])

add(**C, name_ja="カンディス・チュ『他のものを想像する』",
    name_en="Kandice Chuh's Imagine Otherwise",
    name_original="Imagine Otherwise", period_key="グローバル・ディアスポラ期",
    definition="カンディス・チュが2003年に発表した理論書。アジア系米国研究を「主体なき批評（subjectless critique）」として再定義し、アジア系米国アイデンティティの本質化を脱構築した。",
    background="2000年代初頭アジア系米国研究の理論的成熟。",
    development="後のアジア系米国批評（リサ・ロウ、ヤマシタ）の主要参照点となった。",
    historical_context="2000年代初頭アジア系米国批評理論化期。",
    primary_source_url=WIKI_EN+"Asian_American_studies",
    primary_source_type="Wikipedia: Asian American studies",
    importance_score=3, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"主体なき批評論は、AIによるアイデンティティ生成の前提を問う基盤。",
         "related_ai_phenomenon":"AIアイデンティティ脱本質化"}])

add(**C, name_ja="リサ・ロウ『四大陸の親密性』",
    name_en="Lisa Lowe's The Intimacies of Four Continents",
    name_original="The Intimacies of Four Continents",
    period_key="グローバル・ディアスポラ期",
    definition="リサ・ロウが2015年に発表した理論書。アフリカ・アジア・ヨーロッパ・アメリカ大陸の植民地的親密性を文書館研究から追跡し、近代の地理的構造を脱中心化したディアスポラ理論の代表作。",
    background="2010年代の植民地文書館研究の興隆。",
    development="ロウの『移民法』(1996)に続くアジア系米国批評の中心テクストとなった。",
    historical_context="2010年代世界システム研究の文書館的転回期。",
    primary_source_url=WIKI_EN+"Lisa_Lowe",
    primary_source_type="Wikipedia: Lisa Lowe",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"植民地的親密性",
         "description":"ロウの親密性論は人類学的近代世界システム研究の重要な発展。"}])

add(**C, name_ja="リサ・ロウ『移民法』",
    name_en="Lisa Lowe's Immigrant Acts", name_original="Immigrant Acts",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="リサ・ロウが1996年に発表した理論書。アジア系米国移民を米国の文化的構成における「異質性・雑種性・多様性」の主体として理論化した、アジア系米国批評の礎石的著作。",
    background="1990年代アジア系米国批評の理論的成熟。",
    development="アジア系米国研究の中心理論書として20年以上影響力を保つ。",
    historical_context="1990年代米国移民法論議期。",
    primary_source_url=WIKI_EN+"Lisa_Lowe",
    primary_source_type="Wikipedia: Lisa Lowe",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"異質性・雑種性・多様性の三角理論は、AI時代の集合的主体性理解の基盤。",
         "related_ai_phenomenon":"AI時代の集合主体"}])

add(**C, name_ja="キャシー・パーク・ホン『マイナー詩学』",
    name_en="Cathy Park Hong's Engine Empire", name_original="Engine Empire",
    period_key="グローバル・ディアスポラ期",
    definition="キャシー・パーク・ホン（1976-）が2012年に発表した詩集。米国西部開拓時代・現代中国・近未来仮想空間の三部構成で、テクノロジー・帝国・人種を韓国系米国詩人視点で展開した。",
    background="2010年代キャシー・パーク・ホンのトリロジー詩学。",
    development="続く『マイナー・フィーリングズ』(2020)へ繋がるホンの代表詩集となった。",
    historical_context="2010年代米国アジア系詩のSF的転回期。",
    primary_source_url=WIKI_EN+"Cathy_Park_Hong",
    primary_source_type="Wikipedia: Cathy Park Hong",
    importance_score=3, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ホンの三言語層詩学は、LLM多言語生成の理論的祖型として読める。",
         "related_ai_phenomenon":"LLM多層言語生成"}])


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
        print(f"[wave17-c32-add60] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave17-c32-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
