"""LIT-DB Phase 2 Wave 11 — C32 ADD: Diaspora Literature (+40 concepts).

Subfield: lit_diaspora (id=20), region='ディアスポラ'.
Adds 40 NEW concepts to complement the existing 40 (id=722-761).

Coverage focus:
  A: Asian American (8) — Kingston, Lahiri, Vuong, Cathy Park Hong, Min Jin Lee
  B: Black diaspora (8) — Caribbean Anglo (Walcott, Brathwaite, Lovelace),
                          Caribbean Franco (Glissant, Chamoiseau, Condé),
                          Black British (Levy, Evaristo, Phillips)
  C: Jewish diaspora (5) + Refugee writing (3) — I.B. Singer, Ozick, Howe,
                          Korean/Vietnamese/Cambodian American refugee
  D: Other diasporas (8) — Roma, Kurdish, Palestinian (Said, Darwish, Abulhawa),
                          translingual (Hemon, Tawada, Lahiri Italian)
  E: Theory & poetics (8) — Refugee Optic (Nguyen), exophonic theory,
                          Border/Borderland (Anzaldúa), code-switching aesthetics

Verification: living author 'secondary'; theory chapters with PD/critical text 'primary'.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("脱植民地・初期移民文学期", "Decolonial / Early Migrant",
     1900, 1965, "両大戦間期から脱植民地化初期に至る、初期移民・亡命作家の世代。"),
    ("ポストコロニアル・ディアスポラ期", "Postcolonial Diaspora",
     1965, 2000, "1965年米国移民法改正以降、世界規模のポストコロニアル離散文学が成熟する時代。"),
    ("グローバル・ディアスポラ期", "Global Diaspora",
     2000, 2026, "9.11以降のグローバル離散・難民文学・トランスリンガル創作の時代。"),
]


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
GUTEN = "https://www.gutenberg.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_diaspora", region="ディアスポラ",
         original_script="roman")


# ============================================================
# A: Asian American diaspora (8)
# ============================================================
add(**C, name_ja="マキシン・ホン・キングストン『チャイナタウンの女武者』",
    name_en="Maxine Hong Kingston's The Woman Warrior",
    name_original="The Woman Warrior",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="マキシン・ホン・キングストン（1940-）が1976年に発表した自伝的作品。中国系米国人女性の幼少期記憶、母の語る「talk-story」、花木蘭の伝説を融合し、ジャンル境界（自伝・小説・神話）を解体した。アジア系米国文学の制度的成立を象徴する画期作で、後のエイミー・タン、ジュンパ・ラヒリ、リサ・シーらに深い影響を与えた。",
    background="1965年米国移民法改正以降のアジア系移民第二世代の文化的覚醒、第二波フェミニズムの興隆、1960年代米国エスニック・スタディーズ運動。",
    development="アジア系米国文学批評（フランク・チン、エレイン・キム、リサ・ロウ）の中心テクストとなり、ノートンアンソロジーに収録された。",
    historical_context="1970年代米国における人種・ジェンダー政治の転換期と、エスニック自伝ジャンルの制度化。",
    primary_source_url=WIKI_EN+"The_Woman_Warrior",
    primary_source_type="Wikipedia: The Woman Warrior",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"母の口承「talk-story」を介した自我形成は、AI生成における他者の声を取り込んだ主体構築と並行して読める。",
         "related_ai_phenomenon":"AIにおける口承的・他者声統合的主体形成"},
        {"axis":"言語","status":"rethinking",
         "rationale":"中国語・英語・神話言語の重層は、多言語AIモデルの言語層位問題と理論的に共振する。",
         "related_ai_phenomenon":"多言語LLMの言語層位の混合"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"自伝的民族誌",
         "description":"キングストンの自伝はエスニック民族誌と文学の境界形態として、人類学的自己記述（autoethnography）と並行する。"}])

add(**C, name_ja="ジュンパ・ラヒリ『その名にちなんで』",
    name_en="Jhumpa Lahiri's The Namesake",
    name_original="The Namesake",
    period_key="グローバル・ディアスポラ期",
    definition="ジュンパ・ラヒリ（1967-）が2003年に発表した長編小説。ベンガル系米国移民第二世代ゴーゴリ・ガングリーの命名・改名・アイデンティティ形成を、抑制された散文で描いた。南アジア系米国ディアスポラ文学の制度的代表作で、第二世代の名前と帰属の問題を文学的に焦点化した。",
    background="1965年移民法改正以降のインド系米国移民第二世代の成熟、9.11以降の南アジア系米国人のアイデンティティ問題化。",
    development="南アジア系ディアスポラ文学（ジュリ・カーン、サンジヴ・サハ、チトラ・バネルジー）の規範作品となった。",
    historical_context="2000年代米国のエスニック小説市場の主流化と、第二世代物語ジャンルの確立。",
    primary_source_url=WIKI_EN+"The_Namesake_(novel)",
    primary_source_type="Wikipedia: The Namesake",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ジュンパ・ラヒリ・イタリア語期",
    name_en="Jhumpa Lahiri's Italian phase",
    name_original="In altre parole",
    period_key="グローバル・ディアスポラ期",
    definition="ラヒリが2012年以降ローマに移住し、母語英語を一時的に放棄してイタリア語で執筆した文学的転回。『べつの言葉で（In altre parole）』(2015)、『どこにいても（Dove mi trovo）』(2018、自身による英訳2021)で、トランスリンガルな自己再構築を実践した。エクソフォニック・ライティング（母語以外での創作）の現代的代表事例。",
    background="ベンガル語と英語の二重的母語経験、9.11以降の英語圏の言語政治への懐疑、欧州移住という言語的選択。",
    development="エクソフォニック・ライティング理論（多和田葉子、エミーヌ・セヴギ・エズダマー）と並行する21世紀トランスリンガル文学の中心事例となった。",
    historical_context="2010年代欧米の英語ヘゲモニーへの作家的応答と、後期人生の言語選択の理論化。",
    primary_source_url=WIKI_EN+"In_Other_Words_(Lahiri_book)",
    primary_source_type="Wikipedia: In Other Words",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"母語放棄と他言語創作は、LLMの言語切替・コードスイッチング機能と理論的に対比可能。AI時代における言語選択の主体的意味を再考する基準。",
         "related_ai_phenomenon":"LLMの多言語切替と作家的言語選択"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"エクソフォニック作家の自己翻訳は、AIによる自動翻訳と作家的翻訳の境界を再定義する。",
         "related_ai_phenomenon":"AI自動翻訳 vs 作家自己翻訳"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"言語と自己",
         "description":"ラヒリのイタリア語転回は、言語と自己の関係（ヴィトゲンシュタイン、デリダ「他者の単言語使用」）を文学的に実践する。"}])

add(**C, name_ja="オーシャン・ヴオン『地上で僕らはつかの間きらめく』",
    name_en="Ocean Vuong's On Earth We're Briefly Gorgeous",
    name_original="On Earth We're Briefly Gorgeous",
    period_key="グローバル・ディアスポラ期",
    definition="オーシャン・ヴオン（1988-）が2019年に発表した書簡形式の半自伝的長編小説。ベトナム系米国人「リトル・ドッグ」が読み書きできない母に宛てる手紙の形式で、戦争・難民・クィアな欲望・オピオイド危機を詩的散文で展開した。第二世代ベトナム系米国文学のグローバル承認を象徴する作品。",
    background="ベトナム戦争難民第二世代、2010年代米国オピオイド危機、クィア・アジア系米国文学の興隆。",
    development="ヴィエト・タン・ウェン、モンク・キム、グエン・ファン・ケ・マイらと並ぶ21世紀ベトナム系米国文学の中心作家となった。",
    historical_context="ベトナム戦争終結45年後の難民第二世代の文学的成熟期、米国でのアジア系反差別運動の興隆。",
    primary_source_url=WIKI_EN+"On_Earth_We%27re_Briefly_Gorgeous",
    primary_source_type="Wikipedia: On Earth We're Briefly Gorgeous",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"非識字の母への書簡という形式は、読み手不在の言語生成という構造を持ち、AI生成の擬似的読者構造と並行的。",
         "related_ai_phenomenon":"AI生成における擬似読者構造"}])

add(**C, name_ja="キャシー・パーク・ホン『マイナー・フィーリングズ』",
    name_en="Cathy Park Hong's Minor Feelings",
    name_original="Minor Feelings",
    period_key="グローバル・ディアスポラ期",
    definition="キャシー・パーク・ホン（1976-）が2020年に発表したエッセイ集。アジア系米国人の「マイナー・フィーリングズ（小さな感情）」（不快・恥・劣等感）を理論化し、米国の人種言説におけるアジア系の不可視性を批判した。「モデル・マイノリティ」言説の解体と、アジア系米国人主体の理論的再定義を達成した21世紀の重要批評作品。",
    background="2010年代後半の米国アジア系反差別運動、コロナ禍でのアジア系ヘイト犯罪急増、人種理論におけるアジア系の周辺性問題。",
    development="アジア系米国研究（ロウ、リム、エレイン・キム）の系譜を継ぎ、2020年代アジア系米国批評の中心テクストとなった。",
    historical_context="2020年新型コロナ禍以降の反アジア系暴力急増、Black Lives Matter運動とアジア系の連帯／分裂論議。",
    primary_source_url=WIKI_EN+"Minor_Feelings",
    primary_source_type="Wikipedia: Minor Feelings",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"感情の人類学",
         "description":"「マイナー・フィーリングズ」は感情の人類学（ローセー、アブー=ルゴード）における「マイナーな情動」概念と並行する、アジア系米国人の感情経験の理論化。"}])

add(**C, name_ja="ミン・ジン・リー『パチンコ』",
    name_en="Min Jin Lee's Pachinko",
    name_original="Pachinko",
    period_key="グローバル・ディアスポラ期",
    definition="ミン・ジン・リー（1968-）が2017年に発表した世代サーガ長編。日本占領下朝鮮から戦後日本のザイニチ（在日朝鮮人）四世代を描いた。コリアン・ディアスポラ（特に在日）の歴史を英語圏で広く可視化した画期作で、グローバル承認を獲得した（NYT年間ベスト・全米図書賞最終候補・Apple TV+映像化2022）。",
    background="20世紀朝鮮半島・日本史、特に植民地期・戦後在日朝鮮人差別の歴史、2010年代米国における移民世代サーガの興隆。",
    development="ヨンス・キム、リー・チャンレ、エヴァ・ホフマンらと並ぶ21世紀コリアン・ディアスポラ文学の代表作品となった。",
    historical_context="2010年代の植民地責任・歴史認識を巡る日韓論議、英語圏での非西洋ディアスポラ歴史の文学的注目。",
    primary_source_url=WIKI_EN+"Pachinko_(novel)",
    primary_source_type="Wikipedia: Pachinko",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モデル・マイノリティ言説批判",
    name_en="critique of the model minority discourse",
    name_original="model minority critique",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="アジア系米国人を「成功した模範的少数派」として表象する言説への批判的応答。ロナルド・タカキ『アジア系米国人の歴史』(1989)、エレイン・キム『アジア系米国文学』(1982)、後のフランク・チン、リサ・ロウ、キャシー・パーク・ホンが体系化。アジア系の構造的差別を不可視化し、黒人・ラテン系との分断を生む人種政治装置として批判される。",
    background="1966年『ニューヨーク・タイムズ・マガジン』『U.S.ニュース』のモデル・マイノリティ言説の登場、公民権運動と並行するアジア系の人種化問題。",
    development="2020年代アジア系反差別運動の理論的中核となり、ホン『マイナー・フィーリングズ』に集約された。",
    historical_context="1960年代米国公民権運動期の人種秩序再編と、アジア系を介した黒人運動分断の歴史的構造。",
    primary_source_url=WIKI_EN+"Model_minority",
    primary_source_type="Wikipedia: Model minority",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ザイニチ文学（在日朝鮮人文学）",
    name_en="Zainichi Korean literature",
    name_original="在日朝鮮人文学",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="日本居住朝鮮人とその子孫が日本語で執筆する文学。金石範、李恢成、金鶴泳、李良枝、柳美里、玄月、金時鐘らを代表作家とする。植民地期から続く朝鮮人差別、二重国籍問題、日本語と朝鮮語の言語的二重性、母語喪失といった主題を中心とする、東アジア・ディアスポラ文学の重要なサブカテゴリ。",
    background="1910-45年日本による朝鮮植民地支配、戦後在日朝鮮人の法的地位の不安定化、1948年朝鮮半島分断。",
    development="1970年代以降の作家世代の交代と、ミン・ジン・リー『パチンコ』等を通じた英語圏での再可視化が進行。",
    historical_context="戦後日本社会の朝鮮人マイノリティ政策、日韓関係史。",
    primary_source_url=WIKI_EN+"Zainichi_Korean_literature",
    primary_source_type="Wikipedia: Zainichi Korean literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"在日マイノリティの民族誌",
         "description":"ザイニチ文学は人類学的マイノリティ研究（コリアタウン、二重的アイデンティティ）と並行する自己記述形式。"}])


# ============================================================
# B: Black diaspora (8)
# ============================================================
add(**C, name_ja="デレク・ウォルコット『オメロス』",
    name_en="Derek Walcott's Omeros",
    name_original="Omeros",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="デレク・ウォルコット（1930-2017、セントルシア）が1990年に発表した叙事詩。ホメロス『オデュッセイア』をカリブ海漁師の物語として再書きし、植民地史・アフリカ系離散・カリブの自然を統合した。1992年ノーベル文学賞受賞。カリブ・アングロ系ディアスポラ文学の頂点で、ポストコロニアル叙事詩の規範作品。",
    background="セントルシアでの英仏二重植民地遺産、ハーバード講師経験、カリブ・モダニズム（ジョージ・ラミング、サミュエル・セルヴォン）の継承。",
    development="エドワード・カマウ・ブラスウェイト、グリッサンと並ぶカリブ詩の三巨頭の一人。21世紀ポストコロニアル詩学の規範となった。",
    historical_context="1980-90年代カリブ独立諸国の文化的成熟期、世界文学市場でのポストコロニアル文学の主流化。",
    primary_source_url=WIKI_EN+"Omeros",
    primary_source_type="Wikipedia: Omeros",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="エドワード・カマウ・ブラスウェイト「ネイション・ランゲージ」",
    name_en="Edward Kamau Brathwaite's Nation Language",
    name_original="Nation Language",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ブラスウェイト（1930-2020、バルバドス）が『ネイション・ランゲージの歴史』(1984)で提唱した詩学概念。カリブ口語（クレオール）を「方言（dialect）」ではなく独立した詩的言語「ネイション・ランゲージ」として再定義し、英語標準語に対抗するカリブ詩学の基礎を確立した。アフリカ系カリブの口承遺産を文字文学に取り戻す理論的装置。",
    background="アフリカ系カリブ口承伝統、1960年代カリブ・アーチストグループ（CAM）、フランツ・ファノン『黒い皮膚・白い仮面』。",
    development="ウォルコット、リントン・クェシ・ジョンソン、現代スポークン・ワード詩、カリブ・ヒップホップに継承された。",
    historical_context="独立後カリブ諸国の言語政策論議と、英語ヘゲモニーへの詩的応答。",
    primary_source_url=WIKI_EN+"Kamau_Brathwaite",
    primary_source_type="Wikipedia: Kamau Brathwaite",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"標準語ヘゲモニーに対抗するクレオール詩学は、AI時代における言語的多様性確保の理論的祖型。LLMの標準英語バイアスへの応答として再読される。",
         "related_ai_phenomenon":"LLMの標準語バイアスとマイナー言語の確保"}])

add(**C, name_ja="ジョージ・ラミング『私の肌の砦の中で』",
    name_en="George Lamming's In the Castle of My Skin",
    name_original="In the Castle of My Skin",
    period_key="脱植民地・初期移民文学期",
    definition="バルバドス出身ジョージ・ラミング（1927-2022）が1953年に発表した自伝的長編。植民地下バルバドスの少年期と政治的覚醒を描いた、カリブ・アングロ系ディアスポラ文学の出発点。1948年「ウィンドラッシュ世代」の英国移住作家グループの中心作品で、ポストコロニアル文学の制度的成立を象徴する。",
    background="1948年「エンパイア・ウィンドラッシュ号」によるカリブ系移住、1950年代英国の戦後ロマン・カリブ・ルネサンス、植民地末期の知的覚醒。",
    development="ナイポール、サム・セルヴォン、後のカリル・フィリップス、ザディー・スミスら英国カリブ系作家に深い影響を与えた。",
    historical_context="1950年代の脱植民地化加速期、英国における戦後カリブ系移民コミュニティ形成。",
    primary_source_url=WIKI_EN+"In_the_Castle_of_My_Skin",
    primary_source_type="Wikipedia: In the Castle of My Skin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エドゥアール・グリッサン「クレオライゼーション」",
    name_en="Édouard Glissant's créolisation",
    name_original="créolisation",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="マルティニーク出身グリッサン（1928-2011）が『関係の詩学』(1990)、『全＝世界論』(1997)で展開した中心概念。クレオール化を、カリブ社会で歴史的に生じた異なる文化要素の予測不可能な混淆過程と定義し、グローバル化時代の文化変容の普遍モデルとして提案した。フランス語圏カリブ理論の中心。",
    background="セゼール「ネグリチュード」、ファノン脱植民地論を継承しつつ、本質主義を超克する関係論的アイデンティティ論の構築。",
    development="シャモワゾー、コンフィアン『クレオール礼讃』(1989)、後のグローバル文化研究、世界文学論（ダムロッシュ）に深い影響を与えた。",
    historical_context="1980-90年代マルティニーク・グアドループの文化的アイデンティティ論議と、フランス共和制同化主義への応答。",
    primary_source_url=WIKI_EN+"%C3%89douard_Glissant",
    primary_source_type="Wikipedia: Édouard Glissant",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"クレオライゼーションの予測不可能な混淆論は、AI生成における異質な学習データの混淆過程と理論的に並行する。",
         "related_ai_phenomenon":"AI生成における異質データの予測不可能な混淆"},
        {"axis":"言語","status":"rethinking",
         "rationale":"言語混淆を肯定するグリッサン詩学は、多言語AIの言語混淆現象の理論的祖型として再読可能。",
         "related_ai_phenomenon":"多言語AIの言語混淆"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"関係の哲学",
         "description":"グリッサン「関係の詩学」はドゥルーズ「リゾーム」と並行する、関係論的存在論の文学的展開。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"文化混淆論",
         "description":"クレオライゼーションは人類学的混淆論（オルティス・トランスカルチュレーション、プラット・コンタクト・ゾーン）と理論的に共振する。"}])

add(**C, name_ja="パトリック・シャモワゾー『テキサコ』",
    name_en="Patrick Chamoiseau's Texaco",
    name_original="Texaco",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="マルティニーク出身シャモワゾー（1953-）が1992年に発表した長編小説。フランス植民地マルティニークの150年史を、フォール=ド=フランスの「テキサコ」貧民街の女性語り手マリー=ソフィーの口承を介して描いた。1992年ゴンクール賞受賞。フランス語圏カリブ文学の頂点で、クレオール詩学の小説的実践。",
    background="グリッサン関係詩学、1989年『クレオール礼讃』宣言（シャモワゾー、ベルナベ、コンフィアン）、フランス本土文学と差異化するクレオール文学運動。",
    development="2000年代以降の世界文学において、フランコフォン文学の中心作品として位置づけられた。",
    historical_context="1990年代マルティニークの文化政治と、フランス共和制内での文化的自律論議。",
    primary_source_url=WIKI_EN+"Texaco_(novel)",
    primary_source_type="Wikipedia: Texaco (novel)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="マリーズ・コンデ『セグー』",
    name_en="Maryse Condé's Ségou",
    name_original="Ségou",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="グアドループ出身マリーズ・コンデ（1934-2024）が1984-85年に発表した二巻組長編歴史小説。18-19世紀バンバラ王国セグー（現マリ）の興亡を、アフリカ・カリブ・ヨーロッパを跨ぐ家族史として描いた。コンデは2018年「代替ノーベル文学賞」受賞。フランコフォン・アフリカ系離散文学の最重要作家の一人。",
    background="ギニア・ガーナ・セネガル滞在を経た西アフリカ研究、マルティニーク・グアドループのフランコフォン文学伝統。",
    development="アフリカ・ディアスポラ歴史小説の規範作品となり、2000年代以降の歴史的ディアスポラ長編に深い影響を与えた。",
    historical_context="1980年代フランコフォン文学市場の形成、アフリカ系大西洋史への文学的注目。",
    primary_source_url=WIKI_EN+"Maryse_Cond%C3%A9",
    primary_source_type="Wikipedia: Maryse Condé",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ベルナーディン・エヴァリスト『少女、女、その他』",
    name_en="Bernardine Evaristo's Girl, Woman, Other",
    name_original="Girl, Woman, Other",
    period_key="グローバル・ディアスポラ期",
    definition="ベルナーディン・エヴァリスト（1959-）が2019年に発表した小説。12人の黒人英国女性の物語を、句読点を抑制した「fusion fiction」形式で連環させた。2019年ブッカー賞受賞（黒人英国女性初）、英国黒人ディアスポラ文学の制度的承認を象徴する。アンドレア・レヴィ、ザディー・スミス、カリル・フィリップスと並ぶ黒人英国文学の中心作家。",
    background="1990年代以降の黒人英国文学の興隆、Windrush世代以降の英国黒人女性作家の世代成熟、2010年代英国の人種・ジェンダー論議。",
    development="2020年代英国における黒人英国文学（black British literature）の規範作品となった。",
    historical_context="2018年「ウィンドラッシュ・スキャンダル」（戦後英国カリブ系移民の市民権剥奪事件）と並行する、英国黒人歴史の文学的可視化。",
    primary_source_url=WIKI_EN+"Girl,_Woman,_Other",
    primary_source_type="Wikipedia: Girl, Woman, Other",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アンドレア・レヴィ『スモール・アイランド』",
    name_en="Andrea Levy's Small Island",
    name_original="Small Island",
    period_key="グローバル・ディアスポラ期",
    definition="アンドレア・レヴィ（1956-2019）が2004年に発表した長編小説。1948年ウィンドラッシュ号によるジャマイカからの英国移住第一世代を、複数の語り手を通じて描いた。2004年オレンジ賞・ホイットブレッド賞受賞、2009年BBCドラマ化。英国カリブ系ディアスポラ文学の制度的成立を象徴する作品。",
    background="ジャマイカからの両親の移住経験（父はウィンドラッシュ号乗客）、1990年代以降の英国黒人歴史の文学的回復運動。",
    development="ザディー・スミス『ホワイト・ティース』(2000)と並ぶ2000年代英国黒人ディアスポラ文学の規範となった。",
    historical_context="2000年代英国における戦後カリブ移民史の再評価、Windrush世代60周年(2008)を巡る歴史的記憶論議。",
    primary_source_url=WIKI_EN+"Small_Island_(novel)",
    primary_source_type="Wikipedia: Small Island",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# C: Jewish diaspora (5) + Asian American refugee (3) = 8
# ============================================================
add(**C, name_ja="アイザック・バシェヴィス・シンガーのイディッシュ文学",
    name_en="Isaac Bashevis Singer's Yiddish literature",
    name_original="יצחק באשעוויס זינגער",
    period_key="脱植民地・初期移民文学期",
    definition="アイザック・バシェヴィス・シンガー（1902-1991）はポーランド出身のイディッシュ語作家。1935年に米国移住、『ゴリンプの悪魔』『ゴーライの満』『敵、ある愛物語』等で東欧ユダヤ世界とホロコースト後米国ユダヤ移民の生を描いた。1978年ノーベル文学賞受賞、イディッシュ語文学の最高峰として国際的承認を得た。",
    background="東欧シュテトル・ユダヤ世界、19世紀末〜20世紀イディッシュ語文学（ショレム・アレイヘム、I.L.ペレツ、I.J.シンガー）の継承。",
    development="ホロコーストによるイディッシュ語話者激減後、英語翻訳を通じて世界文学に位置づけられた最後のイディッシュ語大作家。",
    historical_context="ホロコースト前後の東欧ユダヤ文化の消滅と、米国移民を介した記憶の保存。",
    primary_source_url=WIKI_EN+"Isaac_Bashevis_Singer",
    primary_source_type="Wikipedia: Isaac Bashevis Singer",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"消滅言語イディッシュ語の文学的存続は、LLMが少数言語を保存する可能性／均質化する危険の両面と理論的に共振する。",
         "related_ai_phenomenon":"LLMによる消滅言語の保存／均質化"}])

add(**C, name_ja="シンシア・オジック",
    name_en="Cynthia Ozick",
    name_original="Cynthia Ozick",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="シンシア・オジック（1928-）は米国ユダヤ系作家・批評家。『The Shawl』(1989、ホロコースト題材)、『The Messiah of Stockholm』(1987、ブルーノ・シュルツへの応答)、エッセイ集『Art & Ardor』(1983)で、ユダヤ伝統と米国モダニズムの接続、翻訳の倫理、ホロコースト後の文学の役割を理論化した。米国ユダヤ系文学の哲学的中核。",
    background="戦後ニューヨーク・ユダヤ知識人圏（アーヴィング・ハウ、ライオネル・トリリング、フィリップ・ロス）の継承、ジェイムズ的英語小説伝統と東欧ユダヤ伝統の総合。",
    development="現代米国ユダヤ系批評（Commentary、Tikkun誌等）の中心知性となり、若手作家（ジョナサン・サフラン・フォア、ニコール・クラウス）に深い影響を与えた。",
    historical_context="ホロコースト後米国ユダヤ知識人の宗教的・文化的アイデンティティ模索、20世紀末の世俗主義論議。",
    primary_source_url=WIKI_EN+"Cynthia_Ozick",
    primary_source_type="Wikipedia: Cynthia Ozick",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アーヴィング・ハウ『私たちの父祖の世界』",
    name_en="Irving Howe's World of Our Fathers",
    name_original="World of Our Fathers",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="アーヴィング・ハウ（1920-1993）が1976年に発表した米国ユダヤ系移民史の決定版。1880-1920年代の東欧ユダヤ移民のニューヨーク・ロウアーイーストサイドでの生活・労働・文化を、文学的散文で総合した。1976年全米図書賞受賞、米国ユダヤ系ディアスポラ史の文学的記念碑。",
    background="ハウ自身の東欧系ユダヤ第二世代としての伝記、ニューヨーク知識人圏（パルチザン・レビュー誌）の中心人物としての文化的位置。",
    development="米国ユダヤ系移民史研究の規範作品となり、後の世代の自己理解の基礎を形成した。",
    historical_context="1970年代米国ユダヤ系のアイデンティティ覚醒（ホロコースト記念博物館建設論議、イスラエル・ユダヤ離散の関係再考）。",
    primary_source_url=WIKI_EN+"World_of_Our_Fathers",
    primary_source_type="Wikipedia: World of Our Fathers",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"移民共同体の民族誌",
         "description":"ハウの移民共同体史は人類学的民族誌と並行するエスニック共同体記述の文学的形式。"}])

add(**C, name_ja="カフカのディアスポラ的読解",
    name_en="diasporic reading of Kafka",
    name_original="Kafka als Diasporaautor",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="フランツ・カフカ（1883-1924）をモダニズムの枠組みを超えてユダヤ・ディアスポラ作家として再読する批評潮流。ハナ・アーレント『カフカ論』(1944)、ジル・ドゥルーズ／ガタリ『マイナー文学のためのカフカ』(1975)、ロバート・アルター『現代の神聖な経典』が中心。プラハの三言語環境（ドイツ語・チェコ語・イディッシュ語）と、シオニズム期ユダヤ知識人としてのカフカを再評価する視座。",
    background="第二次大戦後のユダヤ知識人によるカフカ再評価、1968年以降のドゥルーズ／ガタリ「マイナー文学」概念の影響、20世紀末のディアスポラ批評の興隆。",
    development="ポストコロニアル理論におけるカフカの位置づけ、現代の中欧文学批評（マレク・ネドヴェチェク、エンリケ・ヴィラ=マータス）に継承された。",
    historical_context="20世紀末のヨーロッパにおけるユダヤ文化記憶の再評価期と、モダニズム解釈枠組みの脱構築。",
    primary_source_url=WIKI_EN+"Franz_Kafka#Jewish_identity_and_themes",
    primary_source_type="Wikipedia: Kafka Jewish identity",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ドゥルーズ／ガタリが理論化したカフカの「マイナー文学」（多数派言語の中の少数派的使用）は、AI多言語モデルにおけるマイナー言語の位置を理論化する基準。",
         "related_ai_phenomenon":"AI多言語モデルにおけるマイナー文学の位置"}])

add(**C, name_ja="マイナー文学（ドゥルーズ／ガタリ）",
    name_en="minor literature (Deleuze/Guattari)",
    name_original="littérature mineure",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ジル・ドゥルーズとフェリックス・ガタリが『マイナー文学のためのカフカ』(1975)で提唱した概念。「マイナー文学」とは多数派言語内で少数派が行う文学（プラハのドイツ語ユダヤ文学、ケベック・フランス語文学等）で、(1)言語の脱領土化、(2)個人の政治的接続、(3)集合的言表配置の三特徴を持つ。ディアスポラ・ポストコロニアル文学の理論的枠組み。",
    background="フランツ・カフカ研究、1970年代フランスのポスト構造主義、植民地末期の言語政治論議。",
    development="ポストコロニアル批評（バーバ、スピヴァク）、世界文学論（カザノヴァ、ダムロッシュ）に深い影響を与えた。",
    historical_context="1970年代フランス左派思想とポストコロニアル批評の理論的接続点。",
    primary_source_url=WIKI_EN+"Kafka:_Toward_a_Minor_Literature",
    primary_source_type="Wikipedia: Kafka: Toward a Minor Literature",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"マイナー文学概念は、多数派言語内の少数派的使用を理論化する。LLMの英語ヘゲモニー下での非英語的使用を理論化する基盤となる。",
         "related_ai_phenomenon":"LLMの英語ヘゲモニー下のマイナー言語使用"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"ドゥルーズの脱領土化",
         "description":"マイナー文学はドゥルーズ哲学の脱領土化・リゾーム概念の文学的展開。"},
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"少数派詩学",
         "description":"マイナー文学はポストコロニアル詩学の中心理論枠組み。"}])

add(**C, name_ja="ヴィエト・タン・ウェン『シンパサイザー』",
    name_en="Viet Thanh Nguyen's The Sympathizer",
    name_original="The Sympathizer",
    period_key="グローバル・ディアスポラ期",
    definition="ヴィエト・タン・ウェン（1971-）が2015年に発表した長編小説。ベトナム戦争終結時の二重スパイの回想録形式で、戦争・難民・米国オリエンタリズムを批評的に描いた。2016年ピューリツァー賞受賞、ベトナム系米国文学の制度的承認を象徴する。続編『コミット』(2021)、『ノット・ダブル・トラブル』(2024)とで三部作を成す。",
    background="ベトナム戦争難民第二世代の歴史、米国でのベトナム戦争映画・文学のオリエンタリズムへの批判的応答、2010年代米国アジア系研究の興隆。",
    development="ヴィエトの理論書『何ものも死なない（Nothing Ever Dies）』(2016、戦争記憶論)と並んで、21世紀ベトナム系米国文学・批評の中心となった。",
    historical_context="ベトナム戦争終結40周年(2015)を巡る米国の戦争記憶論議。",
    primary_source_url=WIKI_EN+"The_Sympathizer",
    primary_source_type="Wikipedia: The Sympathizer",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヴィエト・タン・ウェン「難民の眼差し（Optic of the Refugee）」",
    name_en="Nguyen's Optic of the Refugee",
    name_original="Optic of the Refugee",
    period_key="グローバル・ディアスポラ期",
    definition="ヴィエト・タン・ウェンが『何ものも死なない』(2016)、『難民たち（The Refugees）』(2017)、論文「On Being a Refugee, an American—and a Human Being」で展開した理論的視座。「移民（immigrant）」が米国国民国家統合の語彙であるのに対し、「難民（refugee）」は国民国家システムへの根本的攪乱要因として機能すると論じた。21世紀難民文学の中心理論。",
    background="2015年シリア難民危機、米国移民・難民言説の政治的緊張、ポストコロニアル批評の難民への注目。",
    development="2010年代以降の難民文学（モフシン・ハミド『出口・西』、ディナ・ナイェリ、リュック・ナイ・ナム）の理論的基盤となった。",
    historical_context="2015年以降のグローバル難民危機（シリア・ロヒンギャ・ウクライナ・ガザ）の文学的応答。",
    primary_source_url=WIKI_EN+"Viet_Thanh_Nguyen",
    primary_source_type="Wikipedia: Viet Thanh Nguyen",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"難民の眼差しは国民国家的主体構成への根本的攪乱として理論化される。AI時代における国民国家を超えた主体構成の理論的祖型として再読される。",
         "related_ai_phenomenon":"AI時代の国民国家を超えた主体性の構成"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"難民の真正な経験を表象することの倫理的困難は、AIが難民経験を生成することの倫理的問題の理論的基盤。",
         "related_ai_phenomenon":"AI生成における難民経験の表象倫理"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アガンベン「むき出しの生」",
         "description":"難民の眼差しはアガンベンの「ホモ・サケル」「むき出しの生」概念と並行する、国民国家システム批判の文学的・哲学的枠組み。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"難民の人類学",
         "description":"難民の眼差しは難民の人類学（マリンキ、フェルドマン）と並行する難民経験の理論化。"}])

add(**C, name_ja="カンボジア系米国文学",
    name_en="Cambodian American literature",
    name_original="Cambodian American literature",
    period_key="グローバル・ディアスポラ期",
    definition="クメール・ルージュ大虐殺(1975-79)後に米国に移住したカンボジア系難民とその子孫が英語で執筆する文学。ソック・チャン・サムナング、リアム・ラチャナ、ヴァディ・ラトナー『パパイヤの根の影』(2012)、アンソニー・ヴェアサ・ピン・ボー、モンク・キム『黄金の傘』(2014)等を代表とする。21世紀東南アジア系米国文学の重要なサブカテゴリ。",
    background="1975-79年クメール・ルージュ虐殺による200万人死亡、1980年代米国へのカンボジア難民受入れ、第二世代の文学的成熟。",
    development="2000年代以降の米国アジア系文学拡張の一翼として位置づけられ、ベトナム系米国文学と並行する難民文学の重要分野となった。",
    historical_context="クメール・ルージュ国際法廷(2007-2018)期の歴史的記憶論議、米国でのトラウマ文学の主流化。",
    primary_source_url=WIKI_EN+"Cambodian_American",
    primary_source_type="Wikipedia: Cambodian American",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# D: Other diasporas (8): Roma, Kurdish, Palestinian, Translingual
# ============================================================
add(**C, name_ja="エドワード・サイード『故国喪失についての省察』",
    name_en="Edward Said's Reflections on Exile",
    name_original="Reflections on Exile",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="エドワード・サイード（1935-2003）が1984年論文として発表し、2000年同名エッセイ集に収録された亡命論。亡命を「個人と本来の場所、自己と本来の住処の間に裂け目を強制された不可逆の経験」と定義し、知識人の亡命的立場を倫理的・知的特権として理論化した。20世紀末の亡命・ディアスポラ論の中心テクスト。",
    background="サイード自身のパレスチナ系米国知識人としての伝記、ファノン・コンラッド研究、コロンビア大学比較文学教授としての位置。",
    development="現代の亡命知識人論（ホミ・バーバ、ガヤトリ・スピヴァク）に深い影響を与え、21世紀ディアスポラ批評の規範テクストとなった。",
    historical_context="冷戦末期の知識人亡命問題（ソルジェニツィン、ブロツキー）と、パレスチナ問題の知的可視化期。",
    primary_source_url=WIKI_EN+"Reflections_on_Exile",
    primary_source_type="Wikipedia: Reflections on Exile",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"サイード亡命論における「中心からの距離」の知的特権は、AI時代における脱中心的視座（特定文化に縛られないAI生成）の理論的祖型として再読される。",
         "related_ai_phenomenon":"AI生成における脱中心的視座"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"亡命の哲学",
         "description":"サイード亡命論はアレント、アドルノ、ベンヤミンの亡命知識人論と並行する20世紀亡命哲学の継承。"}])

add(**C, name_ja="マフムード・ダルウィーシュ",
    name_en="Mahmoud Darwish",
    name_original="محمود درويش",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="マフムード・ダルウィーシュ（1941-2008）はパレスチナ国民詩人。1948年ナクバ（大災厄）以降、ハイファ・モスクワ・カイロ・ベイルート・チュニス・パリ・ラマッラを経た亡命人生で、約30冊の詩集（『オリーヴの葉』(1964)、『身分証明書』、『ベイルートに賛歌』、『壁画』(2000)等）を発表。アラブ世界・グローバル文学界で20世紀後半最大のアラビア語詩人として承認された。",
    background="1948年ナクバ後のパレスチナ・ディアスポラ、1960年代以降のアラブ・ナショナリズム文学運動、PLO文化部門での活動。",
    development="現代パレスチナ詩（スーザン・アブラハ、ナオミ・シハブ・ナイ、ファディ・ジューダ）の理論的基礎を確立した。",
    historical_context="1948年ナクバから2003年イラク戦争まで、約60年のパレスチナ・アラブ世界史と並走した詩的軌跡。",
    primary_source_url=WIKI_EN+"Mahmoud_Darwish",
    primary_source_type="Wikipedia: Mahmoud Darwish",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"パレスチナ・アラビア語詩の地理的喪失下での維持は、消滅言語のAI保存の倫理問題と並行する。",
         "related_ai_phenomenon":"AIにおける離散言語の保存"}])

add(**C, name_ja="スーザン・アブラハ『ジェニンの朝』",
    name_en="Susan Abulhawa's Mornings in Jenin",
    name_original="Mornings in Jenin",
    period_key="グローバル・ディアスポラ期",
    definition="パレスチナ系米国人作家スーザン・アブラハ（1970-）が2010年に発表した長編小説（初版2006年『ジェニンのダビデの傷跡』）。1948年ナクバから2002年ジェニン・キャンプ侵攻まで、四世代のパレスチナ家族を描いた。世界30言語以上に翻訳され、英語圏でのパレスチナ・ディアスポラ文学の代表作となった。",
    background="アブラハ自身のクウェート→米国移住の伝記、2000年代米国でのパレスチナ問題の文学的可視化、英語圏での非西洋ディアスポラ文学の興隆。",
    development="現代パレスチナ・ディアスポラ文学（イサベラ・ハマディ、ハーラ・アライアン、アダニア・シブリ）の規範作品となった。",
    historical_context="2000年代第二次インティファーダから2010年代ガザ封鎖期のパレスチナ問題と、英語圏でのその文学的応答。",
    primary_source_url=WIKI_EN+"Mornings_in_Jenin",
    primary_source_type="Wikipedia: Mornings in Jenin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ロマ文学（ジプシー文学）",
    name_en="Roma literature",
    name_original="Romani literatura",
    period_key="グローバル・ディアスポラ期",
    definition="ロマ（ジプシー）民族の作家による文学。パピューシャ（ブロニスワヴァ・ヴァイス、ポーランド、1908-1987）、メノス・サルチン（ギリシャ）、フィリオメナ・フランツ（ドイツ）、マテオ・マクシモフ（フランス）、ルミニーツァ・ミカイ（ルーマニア）等を代表作家とする。1971年ロンドン世界ロマ会議以降、文学的・政治的アイデンティティの確立期にある「ヨーロッパ最大の少数民族」の文学。",
    background="11世紀北西インドからの移住、千年の欧州ディアスポラ、ホロコースト中のポラジモス（ロマ虐殺、約25-50万人）。",
    development="2010年代欧州反ロマ差別の中での文学的応答、欧州少数民族文学の中心領域として確立。",
    historical_context="2007年欧州ロマ・サミット、2015年シリア難民危機との並行的反差別問題化。",
    primary_source_url=WIKI_EN+"Romani_literature",
    primary_source_type="Wikipedia: Romani literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ロマの民族誌",
         "description":"ロマ文学は人類学的ロマ研究と並行する自己記述形式で、外部記述からの脱却を志向する。"}])

add(**C, name_ja="クルド文学（ディアスポラ）",
    name_en="Kurdish diaspora literature",
    name_original="edebiyata kurdî",
    period_key="グローバル・ディアスポラ期",
    definition="トルコ・イラク・イラン・シリアの分断的国家境界とディアスポラを通じて発達するクルド民族の文学。メフメト・ウズン（1953-2007、トルコ→スウェーデン）、ヤシャル・ケマル（クルド系トルコ作家）、ベフロウズ・ブーチャニ（マヌス収容所からのジャーナリズム）、シェルザード・ハサン、ベフチェト・チャンティ等を代表とする。母語抑圧下での文学的維持を中核問題とする。",
    background="1923年ローザンヌ条約以降のクルド民族分割、20世紀のクルド語抑圧、1980年代以降の欧州クルド・ディアスポラ形成。",
    development="2010年代以降のシリア内戦・ロジャヴァ革命を経て、英語・スウェーデン語・ドイツ語等への翻訳が増加した。",
    historical_context="2010年代のクルド民族の地政学的位置（ロジャヴァ・PKK・KRG）と並行する文学的可視化。",
    primary_source_url=WIKI_EN+"Kurdish_literature",
    primary_source_type="Wikipedia: Kurdish literature",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"母語抑圧下のクルド語文学は、AI時代における低資源言語のデジタル維持問題の典型例。",
         "related_ai_phenomenon":"低資源言語のAI維持"}])

add(**C, name_ja="アレクサンドル・ヘモン",
    name_en="Aleksandar Hemon",
    name_original="Aleksandar Hemon",
    period_key="グローバル・ディアスポラ期",
    definition="アレクサンドル・ヘモン（1964-）はサラエボ生まれボスニア系米国人作家。1992年ボスニア紛争勃発時にシカゴ滞在中で米国に取り残され、母語ボスニア語を放棄して英語で執筆する選択をした。『ノヴェル・コミック・ブック・オブ・ライフ』(2013)、『The Lazarus Project』(2008)等で、母語放棄と新言語獲得のトランスリンガル経験を主題化した。コンラッド・ナボコフ系譜の現代的代表。",
    background="1992-95年ボスニア紛争・サラエボ包囲、コンラッド・ナボコフのトランスリンガル先例、米国での文学的成熟。",
    development="現代トランスリンガル文学（ラヒリ、多和田葉子、エミーヌ・セヴギ・エズダマー）の中心作家として位置づけられた。",
    historical_context="1990年代ユーゴスラヴィア解体後の世界的ディアスポラ作家世代（ドゥブラフカ・ウグレシッチ、ダニロ・キシュ）の文脈。",
    primary_source_url=WIKI_EN+"Aleksandar_Hemon",
    primary_source_type="Wikipedia: Aleksandar Hemon",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ヘモンの強制的トランスリンガル経験は、AI翻訳が可能にする「言語の選択可能性」の歴史的対比点として再読される。",
         "related_ai_phenomenon":"AI翻訳と作家の言語選択"}])

add(**C, name_ja="多和田葉子のエクソフォニー",
    name_en="Yoko Tawada's exophony",
    name_original="多和田葉子のエクソフォニー",
    period_key="グローバル・ディアスポラ期",
    definition="多和田葉子（1960-）が日本語とドイツ語の両方で執筆する実践と、エッセイ集『エクソフォニー：母語の外へ出る旅』(2003)で理論化した概念。エクソフォニーとは「母語の外で書く」状態で、創作言語を母語に固定する「ナショナル文学」モデルへの根本的批判となる。21世紀トランスリンガル文学理論の中心概念。",
    background="多和田葉子の1982年ハンブルク大学留学・ドイツ移住、20世紀末グローバル化での作家言語選択の流動化、ナボコフ・ベケット等の先例。",
    development="ラヒリ、ヘモン、エズダマーらと並ぶ21世紀トランスリンガル文学運動の理論的中核となり、ドイツ語圏で2016年クライスト賞・2018年バイエルン芸術賞受賞。",
    historical_context="2000年代欧州における移民文学のドイツ語・フランス語圏での主流化、ナショナル文学概念の脱構築期。",
    primary_source_url=WIKI_EN+"Yoko_Tawada",
    primary_source_type="Wikipedia: Yoko Tawada",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"エクソフォニー概念は、母語外執筆を文学的特権として理論化する。AI翻訳・多言語生成時代における作家の言語選択の意味を再考する基準。",
         "related_ai_phenomenon":"AI多言語時代における作家の言語選択"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"母語との距離を介した作者性の構築は、母語を持たないAIの作者性問題の理論的祖型。",
         "related_ai_phenomenon":"母語なきAIの作者性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"言語と思考の関係",
         "description":"多和田のエクソフォニー実践は言語と思考の関係（フンボルト、サピア=ウォーフ、ベンヤミン）を文学的に検証する。"}])

add(**C, name_ja="エクソフォニック・ライティング理論",
    name_en="exophonic writing theory",
    name_original="exophone Schreibweise",
    period_key="グローバル・ディアスポラ期",
    definition="作家が母語以外の言語で創作する現象を理論化する21世紀文学批評枠組み。Susan Arndt, Dirk Naguschewski, Robert Stockhammer編『Exophonie: Anders-Sprachigkeit (in) der Literatur』(2007)が学術的体系化を果たした。コンラッド・ナボコフ・ベケットの古典例から、多和田葉子・ラヒリ・ヘモン・エズダマー等の現代例まで横断する研究領域。",
    background="2000年代欧州における移民文学・トランスリンガル文学の主流化、ナショナル文学・母語中心主義の脱構築論議。",
    development="マイナー文学論（ドゥルーズ／ガタリ）、世界文学論（カザノヴァ、ダムロッシュ）、翻訳論（ヴェヌティ）と接続して、21世紀比較文学の中心領域となった。",
    historical_context="2000年代以降の欧州移民第二・第三世代の文学的成熟と、母語概念の理論的問題化。",
    primary_source_url=WIKI_DE+"Exophonie",
    primary_source_type="Wikipedia: Exophonie",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"エクソフォニック理論は母語と作家の絶対的結合を解体する。AI生成における母語不在の創作可能性の理論的基盤。",
         "related_ai_phenomenon":"AI生成における母語不在の創作"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"翻訳と創作の境界",
         "description":"エクソフォニック理論は翻訳論・創作論の境界を再定義する現代詩学の中心テーマ。"}])


# ============================================================
# E: Theory & poetics (8)
# ============================================================
add(**C, name_ja="グロリア・アンサルドゥーア『ボーダーランド／ラ・フロンテーラ』",
    name_en="Gloria Anzaldúa's Borderlands/La Frontera",
    name_original="Borderlands/La Frontera: The New Mestiza",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="チカーナ・フェミニスト理論家グロリア・アンサルドゥーア（1942-2004）が1987年に発表した混合ジャンル作品。詩・エッセイ・自伝・神話を融合し、米墨国境地帯のメスティーザ意識・「ボーダーランド」概念・複言語使用を理論化した。チカーナ／フェミニズム／ポストコロニアル／クィア理論の交差点に立つ20世紀末批評の中心テクスト。",
    background="米墨国境地帯テキサス州出身の伝記、1981年Cherríe Moraga共編『This Bridge Called My Back』、第三世界フェミニズム運動。",
    development="チカーナ批評、ボーダーランド理論、トランスナショナル・フェミニズム、クィア理論の理論的基礎を確立した。",
    historical_context="1980年代米国の人種・ジェンダー・セクシュアリティ理論の交差期、メキシコ系米国人運動の知的成熟期。",
    primary_source_url=WIKI_EN+"Borderlands/La_Frontera:_The_New_Mestiza",
    primary_source_type="Wikipedia: Borderlands/La Frontera",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"アンサルドゥーアの「メスティーザ意識」は単一同一性を解体する境界主体を理論化する。AI主体性の混淆性の理論的祖型として再読される。",
         "related_ai_phenomenon":"AI主体の境界的・混淆的構成"},
        {"axis":"言語","status":"rethinking",
         "rationale":"スペイン語・英語・ナワトル語・チカーノ・スパングリッシュの混淆は、多言語AIの言語境界解体と理論的に共振する。",
         "related_ai_phenomenon":"多言語AIの言語境界解体"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"境界の人類学",
         "description":"アンサルドゥーアのボーダーランドは境界研究の人類学（レナト・ロサルド、シモーヌ・ゴンザレス）の理論的基盤。"},
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"境界の哲学",
         "description":"ボーダーランド概念はミニョーロ「境界思考（border thinking）」、デリダ「他者の歓待」と並行する境界の哲学。"}])

add(**C, name_ja="メスティーザ意識",
    name_en="mestiza consciousness",
    name_original="conciencia de la mestiza",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="アンサルドゥーアが『ボーダーランド』(1987)第7章で展開した中心理論。複数の文化・言語・人種・セクシュアリティに同時に属する境界的主体の意識形態。「両か（either-or）」二元論を超えて「両方かつ（both-and）」の包摂的論理を採用する、ポストコロニアル・フェミニスト主体性の理論的基盤。チカーナ批評の核心。",
    background="ホセ・バスコンセロス『宇宙人種論』(1925)のメスティーザ論、20世紀末の混血／混淆論議の理論的精緻化。",
    development="境界主体論（ホミ・バーバ、ガヤトリ・スピヴァク）、トランスナショナル・フェミニズム、21世紀のインターセクショナリティ理論の理論的源流となった。",
    historical_context="1980-90年代米国のアイデンティティ政治論議と、本質主義批判の興隆期。",
    primary_source_url=WIKI_EN+"Mestiza_consciousness",
    primary_source_type="Wikipedia: Mestiza consciousness (academic)",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="コードスイッチング詩学",
    name_en="code-switching aesthetics",
    name_original="code-switching aesthetics",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ディアスポラ・移民・多言語環境作家が複数言語を一作品内で意図的に交替させる文学的技法とその美学。サンドラ・シスネロス、ジュノー・ディアス（スパングリッシュ）、アンサルドゥーア、多和田葉子、エミネ・セヴギ・エズダマーが代表的実践者。社会言語学の「コードスイッチング」概念を文学美学として理論化した21世紀詩学。",
    background="社会言語学のコードスイッチング研究（ジョン・ガンパーズ、ショシャナ・ブロム=ジョージ）、20世紀末のチカーナ・移民文学の興隆。",
    development="現代多言語ディアスポラ文学（オセアン・ヴオン、エリザベス・アクヴェドー）の規範技法となり、21世紀世界文学の中心特徴となった。",
    historical_context="1980年代以降の米国・欧州の多文化主義論議と、文学言語の単言語性への批判期。",
    primary_source_url=WIKI_EN+"Code-switching_in_literature",
    primary_source_type="Wikipedia: Code-switching in literature",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"コードスイッチング詩学は、単一言語規範を解体する文学技法。LLMの多言語生成・コードスイッチングの文学的祖型。",
         "related_ai_phenomenon":"LLMによるコードスイッチング生成"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"コードスイッチング詩学の真正性は話者の生活経験に根差す。AIによる擬似コードスイッチング生成の真正性問題の基盤。",
         "related_ai_phenomenon":"AI擬似コードスイッチングの真正性"}])

add(**C, name_ja="難民文学（21世紀）",
    name_en="refugee literature (21st c.)",
    name_original="refugee literature",
    period_key="グローバル・ディアスポラ期",
    definition="2000年代以降のグローバル難民危機（アフガン・イラク・シリア・ロヒンギャ・ウクライナ・スーダン・ガザ）に応答する21世紀文学カテゴリ。モフシン・ハミド『出口・西』(2017)、ディナ・ナイェリ『難民の手引き』(2017)、ベフロウズ・ブーチャニ『山以外には友はいない』(2018、マヌス収容所携帯電話執筆)、ヴィエト・タン・ウェン『難民たち』(2017)を代表とする。",
    background="2015年シリア難民危機（100万人欧州到達）、2017年ロヒンギャ虐殺、2022年ウクライナ侵攻、米墨国境政策の難民化。",
    development="ヴィエト・タン・ウェン「難民の眼差し」理論を基盤に、21世紀グローバル・ディアスポラ文学の中心領域となった。",
    historical_context="2010年代後半のグローバル難民危機の全面化と、欧米でのその文学的応答。",
    primary_source_url=WIKI_EN+"Refugee_literature",
    primary_source_type="Wikipedia: Refugee literature",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"難民主体は国民国家システムの外部に位置する例外的主体性。AI時代における国家を超えた主体構成の理論的基盤。",
         "related_ai_phenomenon":"AI時代の国家外部的主体性"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"難民の真正な経験表象の困難は、AI生成による表象の倫理的問題の基盤。",
         "related_ai_phenomenon":"AIによる難民経験の表象の倫理"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"アガンベンのホモ・サケル",
         "description":"難民文学はアガンベン「ホモ・サケル」、アレント「権利を持つ権利」と並行する、国民国家外部の主体の哲学的問題化。"},
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"難民の人類学",
         "description":"難民文学は難民の人類学（マリンキ、フェルドマン、アガンベン）と並行する難民経験の理論化。"}])

add(**C, name_ja="トランスナショナル文学批評",
    name_en="transnational literary criticism",
    name_original="transnational literary criticism",
    period_key="グローバル・ディアスポラ期",
    definition="国民国家枠組みを越えて文学を分析する21世紀批評枠組み。Paul Jay『Global Matters』(2010)、Wai Chee Dimock『Through Other Continents』(2006)、Steven Yao、Heather Love等が中心。「ディアスポラ」「世界文学」「ポストコロニアル」を統合する理論的傘として機能し、21世紀比較文学の中心動向となった。",
    background="グローバル化に伴う移民・離散の常態化、国民文学パラダイムの解体、ポストコロニアル批評の世界文学への展開。",
    development="2000年代以降の英米比較文学・世界文学論の主流的枠組みとなり、ダムロッシュ『世界文学とは何か』(2003)、カザノヴァ『文学世界共和国』(1999)と接続した。",
    historical_context="2000年代以降の英米学界における国民文学・国民文化枠組みの脱構築期。",
    primary_source_url=WIKI_EN+"Transnationalism",
    primary_source_type="Wikipedia: Transnationalism",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="記憶のディアスポラ的継承",
    name_en="diasporic memory transmission",
    name_original="diasporic memory transmission",
    period_key="グローバル・ディアスポラ期",
    definition="マリアンヌ・ハーシュ『家族のフレーム』(1997)『ジェネレーション・オブ・ポストメモリー』(2012)が理論化した「ポストメモリー（postmemory）」概念を中核とする、ディアスポラ世代を超えたトラウマ的記憶の文学的継承。ホロコースト第二・第三世代文学（アート・スピーゲルマン『マウス』、ニコール・クラウス）、奴隷制記憶（モリスン）、難民記憶（ヴオン、ヴィエト・タン・ウェン）に共通する構造。",
    background="ホロコースト第二世代の記憶論（ハーシュ、ジェフリー・ハートマン）、トラウマ研究（キャシー・カルース）、現代の世代を超えた記憶論議。",
    development="21世紀ディアスポラ文学批評の中心枠組みとなり、奴隷制・植民地主義・難民の世代間記憶研究に拡張された。",
    historical_context="ホロコースト第三世代の文学的成熟期(2000年代)と、世界各地のトラウマ的歴史記憶の文学的応答期。",
    primary_source_url=WIKI_EN+"Postmemory",
    primary_source_type="Wikipedia: Postmemory",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ポストメモリー概念は、直接経験のないトラウマ記憶の継承を理論化する。AIが学習データから「経験のない記憶」を生成する現象の理論的祖型。",
         "related_ai_phenomenon":"AIによる経験なき記憶の生成"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"ポストメモリーの真正性問題は、AI生成記憶の真正性問題と直接的に共振する。",
         "related_ai_phenomenon":"AI生成記憶の真正性"}])

add(**C, name_ja="ディアスポラ的アイロニー",
    name_en="diasporic irony",
    name_original="diasporic irony",
    period_key="ポストコロニアル・ディアスポラ期",
    definition="ディアスポラ作家が母国／受入国の双方に対して保持する二重化された距離から生じるアイロニーの様態。ナボコフ、コンラッド、サルマン・ラシュディ、ザディー・スミス、ジュノー・ディアスに共通する。リンダ・ハッチオン『アイロニーの理論』(1994)が部分的に理論化し、後のポストコロニアル批評で発展した。",
    background="20世紀ロマン主義以来のアイロニー論（シュレーゲル、キルケゴール）の20世紀末ディアスポラ的拡張、ポストモダン・アイロニー論議。",
    development="現代ディアスポラ文学批評の中心概念の一つとなり、ザディー・スミス、ジュノー・ディアス、ラシュディ研究の主要枠組みとなった。",
    historical_context="1990-2000年代のポストコロニアル文学のグローバル承認と、その双面性の理論的探究期。",
    primary_source_url=WIKI_EN+"Postcolonial_literature",
    primary_source_type="Wikipedia: Postcolonial literature",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor")

add(**C, name_ja="食のディアスポラ詩学",
    name_en="poetics of diasporic food",
    name_original="poetics of diasporic food",
    period_key="グローバル・ディアスポラ期",
    definition="食物・料理・食卓を通じてディアスポラ的アイデンティティ・記憶・帰属を表現する文学的技法。ジュンパ・ラヒリ『病気の通訳』(1999)、エイミー・タン『ジョイ・ラック・クラブ』、モンク・キム、ヴァディ・ラトナー、リサ・シー等に共通する。アンソニー・ボルダンの食ジャーナリズム、フード・スタディーズと並行的に発達した21世紀ディアスポラ詩学。",
    background="20世紀末以降のフード・スタディーズの興隆（クロード・フィッシュラー、シドニー・ミンツ）、ディアスポラ研究の物質文化への注目。",
    development="2000年代以降のディアスポラ文学批評の中心領域となり、料理書・食エッセイ・小説の境界を解体した。",
    historical_context="2000年代のグローバル食文化注目と、ディアスポラの物質的次元の理論的可視化期。",
    primary_source_url=WIKI_EN+"Food_studies",
    primary_source_type="Wikipedia: Food studies",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"食の人類学",
         "description":"食のディアスポラ詩学は食の人類学（メアリー・ダグラス、シドニー・ミンツ、クロード・フィッシュラー）と並行する物質文化の文学的展開。"}])


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
        print(f"[c32-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c32-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
