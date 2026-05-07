"""LIT-DB Phase 2 Wave 23 — C10: European Modernism (+80).

Subfield: lit_eu_modernism (id=6).
Adds 80 NEW non-overlapping concepts targeting:
  A: Anglo-American Modernism deeper (Pound, Eliot, Stein, Williams, Stevens, Frost, HD, Moore, Crane) — 25
  B: French Modernism (Valéry, Apollinaire, Gide, Claudel, Mallarmé, Perse, Reverdy, Eluard) — 14
  C: German Modernism (Hofmannsthal, Rilke deeper, Hesse, Kraus, Broch detail) — 11
  D: Italian/Spanish (Pirandello, Saba, Montale, Ungaretti, Lorca) — 9
  E: Russian Acmeism/Futurism deeper (Akhmatova, Mandelstam, Esenin, Khlebnikov, Mayakovsky) — 9
  F: Peripheral (Pessoa heteronyms, Cavafy, Yeats, Beckett) — 7
  G: Avant-garde deeper (Dada, Surrealism, Vorticism, Imagism) — 5
fourth_transform_tags >= 24, cross_domain >= 18, primary >= 50%.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("モダニズム期", "Modernism", 1890, 1945,
     "ジョイス、プルースト、マン、カフカ、ウルフらヨーロッパ高地モダニズム期。"),
    ("後期モダニズム期", "Late Modernism", 1945, 1965,
     "戦後モダニズム後期。"),
]


GUTEN = "https://www.gutenberg.org/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_PT = "https://pt.wikisource.org/wiki/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_eu_modernism", region="西欧", original_script="roman")
CR = dict(subfield_code="lit_eu_modernism", region="ロシア", original_script="cyrillic")
CP = dict(subfield_code="lit_eu_modernism", region="南欧", original_script="roman")


# ============================================================
# A: Anglo-American Modernism deeper (25)
# ============================================================
add(**C, name_ja="パウンド『キャントーズ』全体構造",
    name_en="Pound's The Cantos overall structure",
    name_original="The Cantos",
    period_key="モダニズム期",
    definition="エズラ・パウンド(1885-1972)が約50年(1917-1969)にわたり書き継いだ全120篇の長詩。ホメロス・オウィディウス・孔子・ダンテ・ジェファソンらを並列するイデオグラム的編集史詩で、20世紀モダニズム長詩の頂点。",
    background="第一次大戦後パウンドの欧州亡命、東洋古典・近代経済学への関心の総合化。",
    development="20世紀世界の長詩・編集詩学の規範研究対象となった。",
    historical_context="戦間期から戦後欧米の歴史的危機期。",
    primary_source_url=WIKI_EN+"The_Cantos",
    primary_source_type="Wikipedia: The Cantos",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"異文化テクストのイデオグラム的編集構造は、AI生成における引用ベース・コラージュ的著作の祖型。",
         "related_ai_phenomenon":"AI生成における引用・コラージュ的著作"}])

add(**C, name_ja="パウンド『ピサ詩篇』",
    name_en="Pound's The Pisan Cantos",
    name_original="The Pisan Cantos",
    period_key="後期モダニズム期",
    definition="パウンドが1948年に発表した『キャントーズ』第74-84篇。第二次大戦後ピサの米軍収容所で精神崩壊しつつ書かれた抒情的章で、ボリンゲン賞を受賞しつつ授賞論争を巻き起こした。20世紀政治詩・収容所文学の中心。",
    background="第二次大戦後パウンドの反逆罪訴追、ピサ収容所体験。",
    development="20世紀政治詩・収容所文学の規範作品となった。",
    historical_context="戦後欧米の政治的・文化的清算期。",
    primary_source_url=WIKI_EN+"The_Pisan_Cantos",
    primary_source_type="Wikipedia: The Pisan Cantos",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="パウンド『マウバリー』",
    name_en="Pound's Hugh Selwyn Mauberley",
    name_original="Hugh Selwyn Mauberley",
    period_key="モダニズム期",
    definition="パウンドが1920年に発表した連作詩。第一次大戦後ロンドン文学界からの離別を、二人の詩人ペルソナを介して諷刺的に描く。エリオット『荒地』(1922)に直結する20世紀モダニズム詩の重要過渡作。",
    background="第一次大戦後ロンドン詩壇の停滞、パウンドの欧州大陸移住決意期。",
    development="20世紀モダニズム連作詩の規範作品となった。",
    historical_context="第一次大戦後英国文学界の文化的疲弊期。",
    primary_source_url=GUTEN+"ebooks/49856",
    primary_source_type="Project Gutenberg: Mauberley",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="パウンド『キャセイ』",
    name_en="Pound's Cathay",
    name_original="Cathay",
    period_key="モダニズム期",
    definition="パウンドが1915年に発表した李白等中国古典詩の英訳集。フェノロサの遺稿から作られた翻訳で、中国詩のイデオグラム的明晰さの英語詩への移植を試み、20世紀英語詩の感覚を根本的に変えたエリオットらに影響した記念碑作品。",
    background="フェノロサ遺稿の継承、第一次大戦初期パウンドの東洋詩学的転回。",
    development="20世紀英語詩の感覚的革新点として中国詩学受容史の中心。",
    historical_context="第一次大戦期英米文化の東洋的転回期。",
    primary_source_url=GUTEN+"ebooks/55247",
    primary_source_type="Project Gutenberg: Cathay",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"異言語詩学の翻訳的移植は、AI機械翻訳における詩的明晰性の生成可能性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI機械翻訳における詩的言語の生成"}])

add(**C, name_ja="パウンド『新しくせよ』",
    name_en="Pound's Make It New",
    name_original="Make It New",
    period_key="モダニズム期",
    definition="パウンドが1934年に編んだ批評集。表題はアジア儒教の「日新」に由来し、20世紀モダニズムの中核標語となった。トルバドール詩・カヴァルカンティ・中国詩学・ジェイムズ批評を統合する20世紀モダニスト批評の規範文献。",
    background="戦間期パウンドの東洋・中世受容、米国ブルジョワ批評との対決。",
    development="20世紀モダニスト批評の中心スローガン・規範文献となった。",
    historical_context="戦間期英米モダニズム批評期。",
    primary_source_url=WIKI_EN+"Make_It_New_(book)",
    primary_source_type="Wikipedia: Make It New",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エリオット『プルーフロックの恋歌』",
    name_en="Eliot's The Love Song of J. Alfred Prufrock",
    name_original="The Love Song of J. Alfred Prufrock",
    period_key="モダニズム期",
    definition="T.S.エリオット(1888-1965)が1915年に発表した最初期の傑作詩。中年男プルーフロックの内的独白で、近代都市における主体の優柔不断・性的疎外を究極的に文学化した。20世紀英語詩の出発点。",
    background="エリオットのハーバード留学からロンドン移住期、ベルクソン・ブラッドリー受容。",
    development="20世紀英語詩・モダニズム独白詩の規範作品となった。",
    historical_context="第一次大戦初期欧米の主体危機文化。",
    primary_source_url=WSRC_EN+"The_Love_Song_of_J._Alfred_Prufrock",
    primary_source_type="Wikisource: Prufrock",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="エリオット『荒地』",
    name_en="Eliot's The Waste Land",
    name_original="The Waste Land",
    period_key="モダニズム期",
    definition="エリオットが1922年に発表した連作詩。第一次大戦後ヨーロッパの精神的荒廃を、聖杯伝説・上座仏教・サンスクリット語などを縫合した434行のイデオグラム的構造で描く。20世紀世界モダニズム詩の最重要古典。",
    background="第一次大戦後エリオットの精神的危機、ジェシー・ウェストン『祭儀から騎士物語へ』受容。",
    development="20世紀世界詩・モダニズム長詩の最重要規範作品となった。",
    historical_context="第一次大戦後ヨーロッパ精神的荒廃期。",
    primary_source_url=GUTEN+"ebooks/1321",
    primary_source_type="Project Gutenberg: The Waste Land",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"多言語・多テクスト引用の縫合構造は、AI生成のコラージュ的・引用ベース著作の文学的祖型。",
         "related_ai_phenomenon":"AI生成における多言語コラージュ"}])

add(**C, name_ja="エリオット『四つの四重奏』",
    name_en="Eliot's Four Quartets",
    name_original="Four Quartets",
    period_key="後期モダニズム期",
    definition="エリオットが1936-42年に発表した4篇連作長詩(Burnt Norton, East Coker, The Dry Salvages, Little Gidding)。時間と永遠の関係を音楽的構造で究極的に詩化した、20世紀晩年エリオットの最高傑作で、ノーベル文学賞授賞理由。",
    background="第二次大戦期英国の精神的危機、エリオットのキリスト教瞑想詩学。",
    development="20世紀英語瞑想詩・宗教詩の最重要規範作品となった。",
    historical_context="第二次大戦期英国精神文化期。",
    primary_source_url=WIKI_EN+"Four_Quartets",
    primary_source_type="Wikipedia: Four Quartets",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="エリオット『大聖堂の殺人』",
    name_en="Eliot's Murder in the Cathedral",
    name_original="Murder in the Cathedral",
    period_key="モダニズム期",
    definition="エリオットが1935年に発表した詩劇。1170年カンタベリー大主教トマス・ベケットの殉教を、4人の誘惑者と4人の刺客の象徴主義的構造で詩化した。20世紀英語詩劇復興運動の中心作品。",
    background="戦間期英国の宗教詩劇復興運動、エリオットの英国国教会改宗。",
    development="20世紀英語詩劇・宗教劇の規範作品となった。",
    historical_context="戦間期英国国教会文化復興期。",
    primary_source_url=WIKI_EN+"Murder_in_the_Cathedral",
    primary_source_type="Wikipedia: Murder in the Cathedral",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="エリオット『伝統と個人の才能』",
    name_en="Eliot's Tradition and the Individual Talent",
    name_original="Tradition and the Individual Talent",
    period_key="モダニズム期",
    definition="エリオットが1919年に発表した批評論文。詩人の感情を「客観的相関物」で表現する非個性化論と、過去全体が現在によって変容する「同時的秩序」概念を提示し、20世紀モダニズム批評・新批評の祖型を作った。",
    background="第一次大戦後ロンドン文学界、ブラッドリー新ヘーゲル主義哲学受容。",
    development="20世紀新批評・モダニズム批評の最重要規範文献となった。",
    historical_context="第一次大戦後英米批評期。",
    primary_source_url=WIKI_EN+"Tradition_and_the_Individual_Talent",
    primary_source_type="Wikipedia: Tradition and the Individual Talent",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者の非個性化論は、AI時代の非人間的・非個性的著作生成の祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI時代の非個性的・非人間的著作"}])

add(**C, name_ja="エリオット『聖なる森』",
    name_en="Eliot's The Sacred Wood",
    name_original="The Sacred Wood",
    period_key="モダニズム期",
    definition="エリオットが1920年に発表した最初期批評集。「ハムレットとその問題」「客観的相関物」「伝統と個人の才能」等を収め、20世紀英米モダニズム批評の最重要起点となった批評書。",
    background="第一次大戦後ロンドン文学界、フランス象徴主義批評受容。",
    development="20世紀英米モダニズム批評の最重要起点。",
    historical_context="第一次大戦後英国批評期。",
    primary_source_url=GUTEN+"ebooks/30844",
    primary_source_type="Project Gutenberg: The Sacred Wood",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エリオット『文化の定義のためのノート』",
    name_en="Eliot's Notes towards the Definition of Culture",
    name_original="Notes towards the Definition of Culture",
    period_key="後期モダニズム期",
    definition="エリオットが1948年に発表した文化論。文化を「ある人民の生活様式の総体」と定義し、階級・地域・宗教の相互依存性を論じた。戦後英米文化保守主義の最重要起点で、レイモンド・ウィリアムズ等の応答対象となった。",
    background="戦後英国の文化政策論議、エリオット晩年の社会哲学。",
    development="戦後英米文化研究・文化保守主義の中心テクスト。",
    historical_context="戦後英国文化政策期。",
    primary_source_url=WIKI_EN+"Notes_Towards_the_Definition_of_Culture",
    primary_source_type="Wikipedia: Notes Definition Culture",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ウルフ『オーランドー』",
    name_en="Woolf's Orlando",
    name_original="Orlando: A Biography",
    period_key="モダニズム期",
    definition="ヴァージニア・ウルフが1928年に発表した実験的長編小説。エリザベス朝の貴族青年オーランドーが400年生き、途中で女性に変身する伝記形式の幻想譚。ヴィタ・サクヴィル＝ウェストへの賛歌として20世紀ジェンダー研究・クィア批評の中心テクスト。",
    background="ウルフのヴィタ・サクヴィル＝ウェストとの愛、戦間期英国ジェンダー文化批判。",
    development="20世紀ジェンダー研究・クィア批評の中心テクストとなった。",
    historical_context="戦間期英国ジェンダー文化期。",
    primary_source_url=WIKI_EN+"Orlando:_A_Biography",
    primary_source_type="Wikipedia: Orlando",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"性別・時代を超えた主体の連続性は、AI環境におけるアイデンティティの可塑性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における主体の可塑性・性別越境性"}])

add(**C, name_ja="ウルフ『三ギニー』",
    name_en="Woolf's Three Guineas",
    name_original="Three Guineas",
    period_key="モダニズム期",
    definition="ウルフが1938年に発表した長文評論。戦争防止・女性教育・職業の3つの要請を3ギニーで応答する書簡形式で、戦争・家父長制・教育の相互連関をフェミニスト視点から解析する。20世紀フェミニスト平和論の最重要規範文献。",
    background="第二次大戦前夜英国の戦争危機、戦間期女性権利運動の蓄積。",
    development="20世紀フェミニスト平和論・反戦論の中心起点。",
    historical_context="戦間期末期英国の戦争危機。",
    primary_source_url=WIKI_EN+"Three_Guineas",
    primary_source_type="Wikipedia: Three Guineas",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="スタイン『三人の女』",
    name_en="Stein's Three Lives",
    name_original="Three Lives",
    period_key="モダニズム期",
    definition="ガートルード・スタイン(1874-1946)が1909年に発表した最初期作品。3人の労働階級女性(Good Anna, Melanctha, Gentle Lena)の生活を反復的・連続的現在の散文で描く。20世紀英語モダニズム散文の最初期実験作。",
    background="20世紀初頭パリ・スタインのアメリカ合衆国移住期、セザンヌ受容期。",
    development="20世紀英語モダニズム散文の最初期規範作品となった。",
    historical_context="20世紀初頭米国労働階級・人種文化期。",
    primary_source_url=GUTEN+"ebooks/15408",
    primary_source_type="Project Gutenberg: Three Lives",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="スタイン『優しいボタン』",
    name_en="Stein's Tender Buttons",
    name_original="Tender Buttons",
    period_key="モダニズム期",
    definition="スタインが1914年に発表した散文詩集。3部(Objects, Food, Rooms)に分かれ、ピカソ・ブラックのキュビスム手法を文学に翻訳する反指示的言語実験。20世紀英語モダニズム言語実験の最も急進的な作品。",
    background="20世紀初頭パリ・キュビスム運動、スタインのピカソ・ブラックとの友情。",
    development="20世紀英語モダニズム言語実験・実験詩学の規範作品。",
    historical_context="20世紀初頭パリ・キュビスム文化期。",
    primary_source_url=GUTEN+"ebooks/15396",
    primary_source_type="Project Gutenberg: Tender Buttons",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"反指示的言語実験は、AI生成における言語の指示性解離・自己生成的言語と理論的に共振する。",
         "related_ai_phenomenon":"AI生成における反指示的・自律的言語"}])

add(**C, name_ja="スタイン『アリス・トクラスの自伝』",
    name_en="Stein's The Autobiography of Alice B. Toklas",
    name_original="The Autobiography of Alice B. Toklas",
    period_key="モダニズム期",
    definition="スタインが1933年に発表した実験的自伝。パートナーのアリス・トクラスを語り手にして、スタイン自身のパリ生活・芸術家友人(ピカソ、マティス、ヘミングウェイ)を描く。20世紀実験的伝記・他者越権語りの規範作品。",
    background="戦間期パリのアメリカ人芸術家コミュニティ、スタイン・トクラス同性愛パートナーシップ。",
    development="20世紀実験的伝記・他者語り研究の中心テクスト。",
    historical_context="戦間期パリのアメリカ人芸術家文化。",
    primary_source_url=WIKI_EN+"The_Autobiography_of_Alice_B._Toklas",
    primary_source_type="Wikipedia: Autobiography Alice Toklas",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウィリアムズ『春とすべて』",
    name_en="Williams's Spring and All",
    name_original="Spring and All",
    period_key="モダニズム期",
    definition="ウィリアム・カーロス・ウィリアムズ(1883-1963)が1923年に発表した詩集。詩と散文宣言が交互に置かれる構造で、有名な「赤い手押し車」(The Red Wheelbarrow)を含む。20世紀米国モダニズム詩・客観主義詩学の規範作品。",
    background="第一次大戦後米国モダニズム詩、ニュージャージー州ラザーフォード医師・詩人体験。",
    development="20世紀米国モダニズム詩・客観主義詩学の規範作品。",
    historical_context="第一次大戦後米国モダニズム詩文化。",
    primary_source_url=WIKI_EN+"Spring_and_All",
    primary_source_type="Wikipedia: Spring and All",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ウィリアムズ『パターソン』",
    name_en="Williams's Paterson",
    name_original="Paterson",
    period_key="後期モダニズム期",
    definition="ウィリアムズが1946-58年に発表した5巻長詩。ニュージャージー州パターソン市と巨人男・女の象徴的同一視を通じて、米国地域経験のモダニスト的記述を試みた。20世紀米国地誌的長詩の規範作品。",
    background="戦後米国モダニズム詩・地域文化記述の文学化、ウィリアムズの医師経験。",
    development="20世紀米国地誌的長詩の規範作品。",
    historical_context="戦後米国地域文化期。",
    primary_source_url=WIKI_EN+"Paterson_(poem)",
    primary_source_type="Wikipedia: Paterson",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ウィリアムズ『アメリカン・グレイン』",
    name_en="Williams's In the American Grain",
    name_original="In the American Grain",
    period_key="モダニズム期",
    definition="ウィリアムズが1925年に発表した実験的歴史エッセイ集。コロンブス、コルテス、ピューリタン、フランクリン、リンカーン等の米国史人物を、原資料引用とモダニスト散文で再構築する。20世紀米国モダニスト歴史叙述の規範作品。",
    background="戦間期米国モダニズム歴史認識、ウィリアムズの米国土着主義。",
    development="20世紀米国モダニスト歴史叙述の規範作品。",
    historical_context="戦間期米国土着主義文化期。",
    primary_source_url=WIKI_EN+"In_the_American_Grain",
    primary_source_type="Wikipedia: In the American Grain",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="スティーヴンズ『ハーモニアム』",
    name_en="Stevens's Harmonium",
    name_original="Harmonium",
    period_key="モダニズム期",
    definition="ウォレス・スティーヴンズ(1879-1955)が1923年に発表した最初の詩集。「黒鳥を見る13の方法」「日曜日の朝」「アイスクリーム皇帝」等の傑作を含み、20世紀米国モダニズム詩の最も豊穣な処女詩集の一つ。",
    background="第一次大戦後米国モダニズム詩、コネチカット州保険会社副社長・詩人体験。",
    development="20世紀米国モダニズム詩の最重要詩集の一つとなった。",
    historical_context="第一次大戦後米国モダニズム詩文化。",
    primary_source_url=WIKI_EN+"Harmonium_(poetry_collection)",
    primary_source_type="Wikipedia: Harmonium",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="スティーヴンズ『最高の虚構へのノート』",
    name_en="Stevens's Notes toward a Supreme Fiction",
    name_original="Notes toward a Supreme Fiction",
    period_key="後期モダニズム期",
    definition="スティーヴンズが1942年に発表した長詩。「抽象的でなければならぬ」「変化しなければならぬ」「快楽でなければならぬ」の3部構造で、近代における「最高の虚構」(Supreme Fiction)の必要性を究極的に詩化する。20世紀米国モダニズム哲学詩の頂点。",
    background="第二次大戦期スティーヴンズの哲学詩学、ヴァレリー・ベルクソン受容。",
    development="20世紀米国モダニズム哲学詩の最重要規範作品。",
    historical_context="第二次大戦期米国精神文化期。",
    primary_source_url=WIKI_EN+"Notes_toward_a_Supreme_Fiction",
    primary_source_type="Wikipedia: Notes toward Supreme Fiction",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"近代における虚構の必要性論は、AI生成虚構の存在論的必要性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI生成虚構と近代主体性"}])

add(**C, name_ja="フロスト『ボストンの北』",
    name_en="Frost's North of Boston",
    name_original="North of Boston",
    period_key="モダニズム期",
    definition="ロバート・フロスト(1874-1963)が1914年に発表した第二詩集。「壁の修繕」「死刑執行人」「家の男」等の劇的独白詩を含み、ニューイングランドの口語と古典詩形式を統合した。20世紀米国詩の規範詩集の一つ。",
    background="20世紀初頭米国ニューイングランド農村文化、フロストの英国滞在期。",
    development="20世紀米国詩・劇的独白詩の規範作品となった。",
    historical_context="20世紀初頭米国ニューイングランド文化期。",
    primary_source_url=GUTEN+"ebooks/3026",
    primary_source_type="Project Gutenberg: North of Boston",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="HD『シー・ガーデン』",
    name_en="HD's Sea Garden",
    name_original="Sea Garden",
    period_key="モダニズム期",
    definition="H.D.(ヒルダ・ドゥーリトル、1886-1961)が1916年に発表した最初の詩集。古代ギリシャ詩学の英語イマジズム的再話を試みる海洋・植物詩集で、20世紀英語イマジズム詩の規範詩集。女性モダニスト詩人の起点。",
    background="第一次大戦初期ロンドン・イマジズム運動、H.D.の古代ギリシャ詩学受容。",
    development="20世紀英語イマジズム・女性モダニズム詩の規範詩集となった。",
    historical_context="第一次大戦期英国モダニズム詩文化。",
    primary_source_url=GUTEN+"ebooks/22898",
    primary_source_type="Project Gutenberg: Sea Garden",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="クレイン『橋』",
    name_en="Crane's The Bridge",
    name_original="The Bridge",
    period_key="モダニズム期",
    definition="ハート・クレイン(1899-1932)が1930年に発表した長詩。ブルックリン橋を象徴に、コロンブス・ポカホンタス・ホイットマン等を縫合する米国神話的長詩。エリオット『荒地』への抒情的応答として20世紀米国モダニズム長詩の頂点の一つ。",
    background="戦間期米国モダニズム詩、クレインの精神的危機・自殺前最大作品。",
    development="20世紀米国モダニズム長詩・神話的詩の規範作品。",
    historical_context="戦間期米国モダニズム詩文化。",
    primary_source_url=WIKI_EN+"The_Bridge_(poem)",
    primary_source_type="Wikipedia: The Bridge",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# B: French Modernism (14)
# ============================================================
add(**C, name_ja="ヴァレリー『若きパルク』",
    name_en="Valéry's La Jeune Parque",
    name_original="La Jeune Parque",
    period_key="モダニズム期",
    definition="ポール・ヴァレリー(1871-1945)が1917年に発表した長詩。古代神話のパルク(運命女神)の若い姿を語り手に、自意識の覚醒・身体性・思考の関係を512行で究極的に詩化する。20世紀フランスモダニズム詩の頂点の一つ。",
    background="第一次大戦期ヴァレリーの23年の沈黙からの復帰、マラルメ象徴主義の継承と発展。",
    development="20世紀フランスモダニズム詩・哲学詩の規範作品。",
    historical_context="第一次大戦期フランス精神文化期。",
    primary_source_url=WSRC_FR+"La_Jeune_Parque",
    primary_source_type="Wikisource: La Jeune Parque",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァレリー『魅惑』",
    name_en="Valéry's Charmes",
    name_original="Charmes",
    period_key="モダニズム期",
    definition="ヴァレリーが1922年に発表した詩集。「海辺の墓地」「失われた美酒」「足音」等を含み、純粋詩学の極限を示す20世紀フランス詩の最重要規範詩集の一つ。マラルメ象徴主義の継承と数学的精度の統合。",
    background="第一次大戦後フランス詩文化、ヴァレリー純粋詩学の確立期。",
    development="20世紀フランス詩・純粋詩学の最重要規範詩集。",
    historical_context="第一次大戦後フランス精神文化期。",
    primary_source_url=WSRC_FR+"Charmes",
    primary_source_type="Wikisource: Charmes",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ヴァレリー『カイエ』",
    name_en="Valéry's Cahiers",
    name_original="Cahiers",
    period_key="モダニズム期",
    definition="ヴァレリーが約50年(1894-1945)の毎朝書き続けた哲学的・科学的・詩学的私的ノート全261冊・約26,000ページ。20世紀フランス思想・モダニズム詩学の最大の私的コーパスとして、戦後CNRS版で出版が進む。",
    background="ヴァレリーの毎朝の知的訓練、20世紀フランス自意識思想の最大私的コーパス化。",
    development="20世紀フランス思想・モダニズム詩学の重要私的記録。",
    historical_context="20世紀フランス精神文化長期記録期。",
    primary_source_url=WIKI_FR+"Cahiers_(Paul_Valéry)",
    primary_source_type="Wikipedia: Cahiers",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アポリネール『アルコール』",
    name_en="Apollinaire's Alcools",
    name_original="Alcools",
    period_key="モダニズム期",
    definition="ギヨーム・アポリネール(1880-1918)が1913年に発表した詩集。「ゾーン」「ミラボー橋」「マリー」等を含み、句読点を全廃した革新的形式と都市・愛の主題を統合した。20世紀フランスモダニズム詩の最重要詩集。",
    background="20世紀初頭パリ・キュビスム文化、アポリネールのキュビスト詩学確立期。",
    development="20世紀フランスモダニズム詩の最重要規範詩集。",
    historical_context="20世紀初頭パリ・キュビスム文化期。",
    primary_source_url=GUTEN+"ebooks/55306",
    primary_source_type="Project Gutenberg: Alcools",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アポリネール『ティレジアスの乳房』",
    name_en="Apollinaire's Les Mamelles de Tirésias",
    name_original="Les Mamelles de Tirésias",
    period_key="モダニズム期",
    definition="アポリネールが1917年に上演した戯曲。表題「シュルレアリスム的劇」副題でこの語の最初の使用例となった、性転換・出生主義の不条理喜劇。1947年プーランクのオペラ化を経て20世紀シュルレアリスム劇の起点となった。",
    background="第一次大戦末期パリ前衛劇、アポリネールの「シュルレアリスム」造語期。",
    development="20世紀シュルレアリスム・前衛劇の起点的作品。",
    historical_context="第一次大戦末期パリ前衛文化期。",
    primary_source_url=WSRC_FR+"Les_Mamelles_de_Tirésias",
    primary_source_type="Wikisource: Les Mamelles de Tirésias",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジッド『贋金つくり』",
    name_en="Gide's Les Faux-monnayeurs",
    name_original="Les Faux-monnayeurs",
    period_key="モダニズム期",
    definition="アンドレ・ジッド(1869-1951)が1925年に発表した長編小説。作家エドゥアールが「贋金つくり」という小説を書く過程を含む入れ子構造の自己言及的小説で、ジッドはこれを「私の最初の小説」と呼んだ。20世紀フランス自己言及小説の規範作品。",
    background="戦間期パリ文学界、ジッドの自己言及小説実験期。",
    development="20世紀フランス自己言及小説・メタフィクションの規範作品。",
    historical_context="戦間期フランス文学界期。",
    primary_source_url=WIKI_FR+"Les_Faux-monnayeurs",
    primary_source_type="Wikipedia: Les Faux-monnayeurs",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"小説内小説の入れ子的自己言及構造は、AI生成における自己参照的・再帰的著作の祖型。",
         "related_ai_phenomenon":"AI生成における自己参照的・再帰的著作"}])

add(**C, name_ja="ジッド『背徳者』",
    name_en="Gide's L'Immoraliste",
    name_original="L'Immoraliste",
    period_key="モダニズム期",
    definition="ジッドが1902年に発表した中編小説。学者ミシェルが結核療養中に北アフリカで欲望と肉体に目覚め、妻を失う物語。ニーチェ受容と同性愛の文学化を統合し、20世紀フランス内省的小説の規範作品。",
    background="20世紀初頭ジッドのアルジェリア体験、ニーチェ受容期。",
    development="20世紀フランス内省的小説・同性愛文学の規範作品。",
    historical_context="20世紀初頭フランス植民地・性的覚醒文化期。",
    primary_source_url=GUTEN+"ebooks/35794",
    primary_source_type="Project Gutenberg: L'Immoraliste",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジッド『狭き門』",
    name_en="Gide's La Porte étroite",
    name_original="La Porte étroite",
    period_key="モダニズム期",
    definition="ジッドが1909年に発表した中編小説。ジェロームと従姉妹アリサの精神的愛と、アリサの宗教的禁欲による拒絶を日記形式で描く。プロテスタント禁欲主義の文学的批判として20世紀フランス心理小説の規範作品。",
    background="20世紀初頭フランス・プロテスタント禁欲主義の文学的批判期。",
    development="20世紀フランス心理小説・宗教批判小説の規範作品。",
    historical_context="20世紀初頭フランス・プロテスタント文化期。",
    primary_source_url=GUTEN+"ebooks/13735",
    primary_source_type="Project Gutenberg: La Porte étroite",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="クローデル『繻子の靴』",
    name_en="Claudel's Le Soulier de satin",
    name_original="Le Soulier de satin",
    period_key="モダニズム期",
    definition="ポール・クローデル(1868-1955)が1929年に発表した詩劇。16世紀大航海時代のプロエーズとロドリーグの愛と精神的探求を、4日構造の壮大な詩劇形式で描く。20世紀フランスカトリック詩劇の頂点。",
    background="戦間期クローデルの外交官生活、カトリック詩劇の文学化。",
    development="20世紀フランスカトリック詩劇の最重要規範作品。",
    historical_context="戦間期フランスカトリック文化期。",
    primary_source_url=WIKI_FR+"Le_Soulier_de_satin",
    primary_source_type="Wikipedia: Le Soulier de satin",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クローデル『マリアへのお告げ』",
    name_en="Claudel's L'Annonce faite à Marie",
    name_original="L'Annonce faite à Marie",
    period_key="モダニズム期",
    definition="クローデルが1912年に上演した詩劇。中世フランスを舞台に、ヴィオレーヌの癩病・聖性・蘇生を中心に、姉妹の愛と犠牲を描く。20世紀カトリック詩劇の代表作の一つで、クローデル詩劇の最初期傑作。",
    background="20世紀初頭フランスカトリック復興期、クローデル中世主義。",
    development="20世紀フランスカトリック詩劇の規範作品。",
    historical_context="20世紀初頭フランスカトリック復興期。",
    primary_source_url=GUTEN+"ebooks/14866",
    primary_source_type="Project Gutenberg: L'Annonce faite à Marie",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マラルメ『骰子一擲』",
    name_en="Mallarmé's Un coup de dés",
    name_original="Un coup de dés jamais n'abolira le hasard",
    period_key="モダニズム期",
    definition="ステファヌ・マラルメ(1842-1898)が1897年に発表した革新的長詩。文字の大きさ・配置・空白を意味化する活字的革命で、20世紀視覚詩・コンクリート詩・ハイパーテクスト詩学の最重要起点となった。",
    background="19世紀末マラルメ象徴主義の極限、活字技術の文学的活用期。",
    development="20世紀視覚詩・コンクリート詩・ハイパーテクスト詩学の最重要起点。",
    historical_context="19世紀末フランス象徴主義文化期。",
    primary_source_url=WSRC_FR+"Un_coup_de_dés_jamais_n’abolira_le_hasard",
    primary_source_type="Wikisource: Un coup de dés",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"活字配置の意味化は、AI環境におけるテキスト視覚的構造の生成・配置可能性と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における視覚的テキスト生成"}])

add(**C, name_ja="サン＝ジョン・ペルス『アナバーズ』",
    name_en="Saint-John Perse's Anabase",
    name_original="Anabase",
    period_key="モダニズム期",
    definition="サン＝ジョン・ペルス(1887-1975)が1924年に発表した長詩。古代アジア大陸の遊牧民の遠征を象徴的舞台に、人類の長期的彷徨と征服を巨大な散文詩形式で詩化する。エリオットの英訳(1930)で世界文学化した20世紀フランス長詩の傑作。",
    background="戦間期ペルスの中国外交官時代、古代神話的長詩実験期。",
    development="20世紀世界文学・長詩の重要作品となった。",
    historical_context="戦間期フランス中国外交期。",
    primary_source_url=WIKI_FR+"Anabase",
    primary_source_type="Wikipedia: Anabase",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ルヴェルディ『屋根のスレート』",
    name_en="Reverdy's Les Ardoises du toit",
    name_original="Les Ardoises du toit",
    period_key="モダニズム期",
    definition="ピエール・ルヴェルディ(1889-1960)が1918年に発表した詩集。キュビスム的視覚的配置と「異質的現実の比較」(rapprochement)による独自のキュビスト詩学を確立し、ブルトンらシュルレアリストに直接影響した20世紀フランス前衛詩の中心。",
    background="第一次大戦期パリ・キュビスム運動、ルヴェルディの『北南』(Nord-Sud)雑誌主宰期。",
    development="20世紀フランスキュビスト詩・シュルレアリスム詩の重要起点。",
    historical_context="第一次大戦期パリ前衛文化期。",
    primary_source_url=WIKI_FR+"Pierre_Reverdy",
    primary_source_type="Wikipedia: Reverdy",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="エリュアール『苦悩の首都』",
    name_en="Eluard's Capitale de la douleur",
    name_original="Capitale de la douleur",
    period_key="モダニズム期",
    definition="ポール・エリュアール(1895-1952)が1926年に発表した詩集。シュルレアリスム運動初期の代表詩集で、「エルザ恋愛詩」「無償の選択」等を含む。20世紀フランスシュルレアリスム抒情詩の規範詩集の一つ。",
    background="戦間期パリ・シュルレアリスム運動の最初期、エリュアール・ガラ夫婦パートナーシップ。",
    development="20世紀フランスシュルレアリスム抒情詩の規範詩集。",
    historical_context="戦間期パリ・シュルレアリスム期。",
    primary_source_url=WIKI_FR+"Capitale_de_la_douleur",
    primary_source_type="Wikipedia: Capitale de la douleur",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# C: German Modernism (11)
# ============================================================
add(**C, name_ja="ホフマンスタール『チャンドス卿の手紙』",
    name_en="Hofmannsthal's Ein Brief (Chandos Letter)",
    name_original="Ein Brief",
    period_key="モダニズム期",
    definition="フーゴ・フォン・ホフマンスタール(1874-1929)が1902年に発表した架空書簡形式の散文。フランシス・ベーコン宛のチャンドス卿の言語的危機・沈黙の告白を通じて、20世紀言語懐疑主義(Sprachskepsis)の最重要起点となった。",
    background="世紀転換期ウィーンの言語批判文化、マウトナー言語批判受容期。",
    development="20世紀言語懐疑主義・モダニズム言語論の最重要起点。",
    historical_context="世紀転換期ウィーン言語文化期。",
    primary_source_url=WSRC_DE+"Ein_Brief",
    primary_source_type="Wikisource: Ein Brief",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"言語の指示性・表現可能性への根本的懐疑は、AI生成における言語の意味機能性問題の祖型。",
         "related_ai_phenomenon":"AI生成における言語の意味機能性懐疑"}])

add(**C, name_ja="ホフマンスタール『エレクトラ』",
    name_en="Hofmannsthal's Elektra",
    name_original="Elektra",
    period_key="モダニズム期",
    definition="ホフマンスタールが1903年に上演した戯曲（リヒャルト・シュトラウス1909年オペラ化）。古代ギリシャ悲劇のエレクトラを世紀転換期心理学・フロイト的視点で再解釈し、20世紀ウィーンモダニズム劇の規範作品。",
    background="世紀転換期ウィーン心理学・フロイト精神分析受容期。",
    development="20世紀ウィーンモダニズム劇・オペラの規範作品。",
    historical_context="世紀転換期ウィーン心理文化期。",
    primary_source_url=WIKI_DE+"Elektra_(Hofmannsthal)",
    primary_source_type="Wikipedia: Elektra",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="リルケ『マルテの手記』",
    name_en="Rilke's Die Aufzeichnungen des Malte Laurids Brigge",
    name_original="Die Aufzeichnungen des Malte Laurids Brigge",
    period_key="モダニズム期",
    definition="ライナー・マリア・リルケ(1875-1926)が1910年に発表した実験的小説。デンマーク貴族マルテのパリ滞在を断片的手記形式で描く近代主体危機の文学化。20世紀ドイツ語モダニズム散文の最重要規範作品。",
    background="20世紀初頭リルケのパリ滞在、ロダン秘書経験。",
    development="20世紀ドイツ語モダニズム散文の最重要規範作品。",
    historical_context="20世紀初頭パリ・近代主体危機期。",
    primary_source_url=GUTEN+"ebooks/13099",
    primary_source_type="Project Gutenberg: Malte Laurids Brigge",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="リルケ『時祷詩集』",
    name_en="Rilke's Das Stunden-Buch",
    name_original="Das Stunden-Buch",
    period_key="モダニズム期",
    definition="リルケが1905年に発表した3部構成詩集（修道生活・巡礼・貧困と死）。ロシア旅行体験から生まれた神への祈りの詩集で、20世紀ドイツ語抒情詩・宗教詩の規範詩集。リルケ詩学の出発点。",
    background="20世紀初頭リルケのロシア旅行・ルー・サロメとの友情期。",
    development="20世紀ドイツ語抒情詩・宗教詩の規範詩集。",
    historical_context="20世紀初頭ドイツ語圏宗教文化期。",
    primary_source_url=WSRC_DE+"Das_Stunden-Buch",
    primary_source_type="Wikisource: Das Stunden-Buch",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リルケ『若き詩人への手紙』",
    name_en="Rilke's Briefe an einen jungen Dichter",
    name_original="Briefe an einen jungen Dichter",
    period_key="モダニズム期",
    definition="リルケが1903-08年に書き、1929年に出版された10通の手紙。若き士官候補生フランツ・カプスへの詩学的・人生哲学的助言で、20世紀世界の詩学書簡の規範作品となった。",
    background="20世紀初頭リルケのパリ滞在期、若き詩人カプス指導。",
    development="20世紀世界の詩学書簡・人生哲学書の規範作品。",
    historical_context="20世紀初頭ドイツ語圏詩学文化期。",
    primary_source_url=GUTEN+"ebooks/45683",
    primary_source_type="Project Gutenberg: Briefe an einen jungen Dichter",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="リルケ『オルフォイスへのソネット』",
    name_en="Rilke's Sonette an Orpheus",
    name_original="Sonette an Orpheus",
    period_key="モダニズム期",
    definition="リルケが1922年に発表したソネット集（55篇）。早世した友人の娘ヴェーラへの追悼を契機に、オルフォイス神話を中心に芸術・死・変容を究極的に詩化する。『ドゥイノの悲歌』と同時期の最高傑作の一つ。",
    background="戦間期リルケのスイス・ミュゾット城執筆期、ヴェーラ・クノープ追悼。",
    development="20世紀ドイツ語ソネット・神話詩の最重要規範作品。",
    historical_context="戦間期スイス・ドイツ語圏精神文化期。",
    primary_source_url=WIKI_DE+"Sonette_an_Orpheus",
    primary_source_type="Wikipedia: Sonette an Orpheus",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"オルフォイス神話による死と変容の詩化は、AI環境における主体の変容・死後性問題と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における主体の変容・死後的継続"}])

add(**C, name_ja="ヘッセ『荒野の狼』",
    name_en="Hesse's Der Steppenwolf",
    name_original="Der Steppenwolf",
    period_key="モダニズム期",
    definition="ヘルマン・ヘッセ(1877-1962)が1927年に発表した長編小説。50歳の知識人ハリー・ハラーの精神的危機を、人間と狼の二重性、そして「魔術劇場」での人格分裂体験で描く。20世紀ドイツ語精神分析的小説の規範作品。",
    background="戦間期ヘッセのスイス亡命・ユング受容期、知識人危機の文学化。",
    development="20世紀ドイツ語精神分析的小説・カウンターカルチャー文学の規範作品。",
    historical_context="戦間期スイス・ドイツ語圏精神文化期。",
    primary_source_url=WIKI_DE+"Der_Steppenwolf",
    primary_source_type="Wikipedia: Der Steppenwolf",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヘッセ『シッダールタ』",
    name_en="Hesse's Siddhartha",
    name_original="Siddhartha",
    period_key="モダニズム期",
    definition="ヘッセが1922年に発表した中編小説。古代インドのバラモン青年シッダールタの精神的探求を描く東洋思想的成長小説で、20世紀ドイツ語東洋思想受容文学の規範作品。戦後米国カウンターカルチャーで広く読まれた。",
    background="戦間期ヘッセの東洋思想受容期、第一次大戦後ヨーロッパ精神危機。",
    development="20世紀ドイツ語東洋思想受容文学・成長小説の規範作品。",
    historical_context="戦間期ドイツ語圏東洋思想受容期。",
    primary_source_url=WIKI_DE+"Siddhartha_(Roman)",
    primary_source_type="Wikipedia: Siddhartha",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ヘッセ『ガラス玉演戯』",
    name_en="Hesse's Das Glasperlenspiel",
    name_original="Das Glasperlenspiel",
    period_key="後期モダニズム期",
    definition="ヘッセが1943年に発表した長編小説。23世紀の架空学術共同体カスターリエンと「ガラス玉演戯」の創始者ヨーゼフ・クネヒトの伝記形式で、近代知識生産・教育論を究極的に文学化した。1946年ヘッセノーベル賞受賞理由。",
    background="第二次大戦期ヘッセのスイス亡命創作集中、近代知識生産批判。",
    development="20世紀ドイツ語ユートピア小説・知識批判小説の規範作品。",
    historical_context="第二次大戦期スイス・ドイツ語圏精神文化期。",
    primary_source_url=WIKI_DE+"Das_Glasperlenspiel",
    primary_source_type="Wikipedia: Das Glasperlenspiel",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"知識・象徴の演戯的・組合せ的生産は、AI生成における組合せ的・自動化された知識生産の祖型。",
         "related_ai_phenomenon":"AI生成における組合せ的・自動化知識生産"}])

add(**C, name_ja="クラウス『人類最後の日々』",
    name_en="Kraus's Die letzten Tage der Menschheit",
    name_original="Die letzten Tage der Menschheit",
    period_key="モダニズム期",
    definition="カール・クラウス(1874-1936)が1922年に発表した巨大悲劇。第一次大戦中ウィーン社会の言語的・道徳的崩壊を、約700頁・220場面の引用コラージュ的劇形式で記録する。20世紀ドキュメンタリー劇・引用劇の最重要規範作品。",
    background="第一次大戦期ウィーンのジャーナリズム的言語崩壊、クラウス『炬火』(Die Fackel)雑誌主宰期。",
    development="20世紀ドキュメンタリー劇・引用劇の最重要規範作品。",
    historical_context="第一次大戦期ウィーン言語文化危機期。",
    primary_source_url=WIKI_DE+"Die_letzten_Tage_der_Menschheit",
    primary_source_type="Wikipedia: Die letzten Tage der Menschheit",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ジャーナリズム言語の引用コラージュ的批判は、AI生成における引用ベース・メディア言語問題の祖型。",
         "related_ai_phenomenon":"AI生成におけるメディア言語の引用的構築"}])

add(**C, name_ja="ブロッホ『ウェルギリウスの死』",
    name_en="Broch's Der Tod des Vergil",
    name_original="Der Tod des Vergil",
    period_key="後期モダニズム期",
    definition="ヘルマン・ブロッホ(1886-1951)が1945年に発表した長編小説。臨終のローマ詩人ウェルギリウスの18時間を、4部の意識の流れで描く。20世紀ドイツ語意識の流れ小説の最も実験的な作品の一つ。",
    background="第二次大戦期ブロッホの米国亡命創作、古代古典の現代再話。",
    development="20世紀ドイツ語意識の流れ小説・歴史的伝記小説の規範作品。",
    historical_context="第二次大戦期亡命知識人文化期。",
    primary_source_url=WIKI_DE+"Der_Tod_des_Vergil",
    primary_source_type="Wikipedia: Der Tod des Vergil",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# D: Italian/Spanish (9)
# ============================================================
add(**CP, name_ja="ピランデッロ『作者を探す六人の登場人物』",
    name_en="Pirandello's Sei personaggi in cerca d'autore",
    name_original="Sei personaggi in cerca d'autore",
    period_key="モダニズム期",
    definition="ルイジ・ピランデッロ(1867-1936)が1921年に上演した戯曲。リハーサル中の劇場に、未完の戯曲から脱出した6人の登場人物が現れて作者を求める「劇中劇」構造で、20世紀メタ演劇・不条理演劇の最重要起点となった。1934年ノーベル賞授賞理由。",
    background="戦間期イタリア前衛演劇、ピランデッロのメタ演劇実験期。",
    development="20世紀メタ演劇・不条理演劇の最重要起点。",
    historical_context="戦間期イタリア前衛演劇期。",
    primary_source_url=WSRC_IT+"Sei_personaggi_in_cerca_d%27autore",
    primary_source_type="Wikisource: Sei personaggi",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"作者と登場人物の境界の解体は、AI生成における作者・キャラクター関係の問題の祖型。",
         "related_ai_phenomenon":"AI生成における作者と人物の境界解体"}])

add(**CP, name_ja="ピランデッロ『故マッティア・パスカル』",
    name_en="Pirandello's Il fu Mattia Pascal",
    name_original="Il fu Mattia Pascal",
    period_key="モダニズム期",
    definition="ピランデッロが1904年に発表した長編小説。死亡公告された男マッティア・パスカルが新しいアイデンティティで生きようとして失敗する物語。20世紀イタリアモダニズム小説・アイデンティティ危機文学の規範作品。",
    background="20世紀初頭イタリアモダニズム文学、ピランデッロのアイデンティティ哲学確立期。",
    development="20世紀イタリアモダニズム小説・アイデンティティ危機文学の規範作品。",
    historical_context="20世紀初頭イタリアモダニズム文化期。",
    primary_source_url=WSRC_IT+"Il_fu_Mattia_Pascal",
    primary_source_type="Wikisource: Il fu Mattia Pascal",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**CP, name_ja="サバ『カンツォニエーレ』",
    name_en="Saba's Il Canzoniere",
    name_original="Il Canzoniere",
    period_key="モダニズム期",
    definition="ウンベルト・サバ(1883-1957)が1900-57年に書き続けた生涯詩集。トリエステの日常生活・家族・自意識を、ペトラルカ的伝統と心理学的近代性を統合した抒情詩形式で記録した。20世紀イタリア抒情詩の最重要規範詩集。",
    background="20世紀イタリア・トリエステ多文化都市文化、サバ精神分析受容期。",
    development="20世紀イタリア抒情詩の最重要規範詩集。",
    historical_context="20世紀イタリア・トリエステ多文化文化期。",
    primary_source_url=WIKI_IT+"Canzoniere_(Saba)",
    primary_source_type="Wikipedia: Il Canzoniere",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CP, name_ja="モンターレ『イカの骨』",
    name_en="Montale's Ossi di seppia",
    name_original="Ossi di seppia",
    period_key="モダニズム期",
    definition="エウジェーニオ・モンターレ(1896-1981)が1925年に発表した最初の詩集。リグーリア地方の海岸風景を象徴的舞台に、20世紀近代主体の精神的危機を結晶化する。1975年ノーベル賞授賞理由となった、20世紀イタリアエルメティスモ詩の規範詩集。",
    background="戦間期イタリアエルメティスモ運動、モンターレのリグーリア海岸景観の象徴化。",
    development="20世紀イタリアエルメティスモ詩・モダニズム詩の最重要規範詩集。",
    historical_context="戦間期イタリアエルメティスモ詩文化期。",
    primary_source_url=WIKI_IT+"Ossi_di_seppia",
    primary_source_type="Wikipedia: Ossi di seppia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CP, name_ja="モンターレ『機会』",
    name_en="Montale's Le occasioni",
    name_original="Le occasioni",
    period_key="モダニズム期",
    definition="モンターレが1939年に発表した第二詩集。「モテット」連作を含み、エルメティスモ詩学の頂点を示す。エリオット象徴詩学の継承と独自の「機会」詩学の確立で、20世紀イタリア詩の規範詩集の一つ。",
    background="戦間期イタリアエルメティスモ運動、モンターレのフィレンツェ図書館長期。",
    development="20世紀イタリアエルメティスモ詩の規範詩集。",
    historical_context="戦間期イタリア・ファシズム期文化。",
    primary_source_url=WIKI_IT+"Le_occasioni",
    primary_source_type="Wikipedia: Le occasioni",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CP, name_ja="ウンガレッティ『喜び』",
    name_en="Ungaretti's L'allegria",
    name_original="L'allegria",
    period_key="モダニズム期",
    definition="ジュゼッペ・ウンガレッティ(1888-1970)が1931年に確定版を出した詩集（最初版1916『埋もれた港』）。第一次大戦の塹壕で書かれた極限的に短い詩で、20世紀イタリアエルメティスモ詩の起点となった。",
    background="第一次大戦期ウンガレッティのカルソ塹壕戦体験、極限的詩学誕生期。",
    development="20世紀イタリアエルメティスモ詩の最重要起点。",
    historical_context="第一次大戦期イタリア戦争文化。",
    primary_source_url=WIKI_IT+"L%27allegria",
    primary_source_type="Wikipedia: L'allegria",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CP, name_ja="ロルカ『ジプシー歌集』",
    name_en="Lorca's Romancero gitano",
    name_original="Romancero gitano",
    period_key="モダニズム期",
    definition="フェデリコ・ガルシア・ロルカ(1898-1936)が1928年に発表した詩集。アンダルシアのジプシー文化を、伝統民謡形式と前衛的象徴主義を統合した18の物語詩で詩化する。20世紀スペイン語詩の最重要規範詩集の一つ。",
    background="戦間期スペイン・アンダルシア民俗文化、ロルカ「世代27」運動。",
    development="20世紀スペイン語詩・民俗詩学の最重要規範詩集。",
    historical_context="戦間期スペイン・アンダルシア文化期。",
    primary_source_url=WIKI_ES+"Romancero_gitano",
    primary_source_type="Wikipedia: Romancero gitano",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CP, name_ja="ロルカ『ニューヨークの詩人』",
    name_en="Lorca's Poeta en Nueva York",
    name_original="Poeta en Nueva York",
    period_key="モダニズム期",
    definition="ロルカが1929-30年のニューヨーク滞在から書き、1940年死後出版された詩集。大恐慌期ニューヨークの非人間化された都市文化を、シュルレアリスム的詩学で究極的に批判した、20世紀スペイン語シュルレアリスム詩の最重要規範詩集。",
    background="大恐慌期ニューヨーク、ロルカのコロンビア大学留学体験。",
    development="20世紀スペイン語シュルレアリスム詩の最重要規範詩集。",
    historical_context="大恐慌期米国都市文化期。",
    primary_source_url=WIKI_ES+"Poeta_en_Nueva_York",
    primary_source_type="Wikipedia: Poeta en Nueva York",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"大都市の非人間化的批判は、AI環境における都市・テクノロジーの非人間化問題の祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI環境における都市の非人間化"}])

add(**CP, name_ja="ロルカ『ベルナルダ・アルバの家』",
    name_en="Lorca's La casa de Bernarda Alba",
    name_original="La casa de Bernarda Alba",
    period_key="モダニズム期",
    definition="ロルカが1936年に書き上げた最後の戯曲（死後初演1945）。スペイン田舎町の未亡人ベルナルダ・アルバと5人の娘の家父長制的閉塞を描く悲劇で、20世紀スペイン語演劇の最重要規範作品の一つ。",
    background="戦間期スペイン田舎町家父長制文化、ロルカ「田舎三部作」最終作。",
    development="20世紀スペイン語演劇・フェミニスト演劇の規範作品。",
    historical_context="スペイン内戦前夜文化期。",
    primary_source_url=WIKI_ES+"La_casa_de_Bernarda_Alba",
    primary_source_type="Wikipedia: La casa de Bernarda Alba",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: Russian Acmeism/Futurism deeper (9)
# ============================================================
add(**CR, name_ja="アフマートヴァ『主人なき空』",
    name_en="Akhmatova's Anno Domini MCMXXI",
    name_original="Anno Domini MCMXXI",
    period_key="モダニズム期",
    definition="アンナ・アフマートヴァ(1889-1966)が1922年に発表した詩集。ロシア革命後の精神的危機を、アクメイズム的明晰さと密度の高い象徴で詩化する。20世紀ロシア・アクメイズム詩の中心詩集の一つ。",
    background="ロシア革命直後のソヴィエト初期、アフマートヴァの社会的孤立期。",
    development="20世紀ロシア・アクメイズム詩・革命後抒情詩の規範詩集。",
    historical_context="ロシア革命直後文化期。",
    primary_source_url=WIKI_RU+"Anno_Domini_MCMXXI",
    primary_source_type="Wikipedia: Anno Domini MCMXXI",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CR, name_ja="アフマートヴァ『主人公のいない叙事詩』",
    name_en="Akhmatova's Poema bez geroya",
    name_original="Поэма без героя",
    period_key="後期モダニズム期",
    definition="アフマートヴァが1940-65年の25年間書き続けた長詩。1913年ペテルブルクの記憶を、3部構造の重層的回想形式で詩化する。20世紀ロシア詩の最も複雑な長詩で、アフマートヴァ晩年の最高傑作。",
    background="戦間期から戦後ソヴィエト・アフマートヴァの長期創作集中、銀の時代記憶。",
    development="20世紀ロシア詩の最重要長詩の一つ。",
    historical_context="戦後ソヴィエト・アフマートヴァ晩年文化期。",
    primary_source_url=WIKI_RU+"Поэма_без_героя",
    primary_source_type="Wikipedia: Poema bez geroya",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"主人公不在の長詩構造は、AI生成における中心化されない・分散的主体性の祖型として理論的に共振する。",
         "related_ai_phenomenon":"AI生成における分散的・非中心主体性"}])

add(**CR, name_ja="マンデリシュターム『石』",
    name_en="Mandelstam's Kamen",
    name_original="Камень",
    period_key="モダニズム期",
    definition="オシップ・マンデリシューターム(1891-1938)が1913年に発表した最初の詩集。アクメイズム運動の中心詩集として、ペテルブルクの古典建築・古代地中海文化を象徴する明晰で建築的な詩を集める。20世紀ロシア・アクメイズム詩の起点。",
    background="20世紀初頭ロシア銀の時代・アクメイズム運動、ペテルブルク古典文化。",
    development="20世紀ロシア・アクメイズム詩の最重要起点詩集。",
    historical_context="20世紀初頭ロシア銀の時代文化期。",
    primary_source_url=WIKI_RU+"Камень_(сборник_Мандельштама)",
    primary_source_type="Wikipedia: Kamen",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CR, name_ja="マンデリシューターム『トリスティア』",
    name_en="Mandelstam's Tristia",
    name_original="Tristia",
    period_key="モダニズム期",
    definition="マンデリシュタームが1922年に発表した第二詩集。表題はオウィディウスの追放詩集に由来し、ロシア革命後のヨーロッパ文化喪失と古典追慕を結晶化する。20世紀ロシア革命後抒情詩の最重要規範詩集の一つ。",
    background="ロシア革命直後マンデリシュタームのモスクワ・クリミア滞在、古典喪失意識。",
    development="20世紀ロシア革命後抒情詩・追放詩学の最重要規範詩集。",
    historical_context="ロシア革命直後文化期。",
    primary_source_url=WIKI_RU+"Tristia_(сборник)",
    primary_source_type="Wikipedia: Tristia",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**CR, name_ja="マンデリシュターム『ヴォロネジ・ノート』",
    name_en="Mandelstam's Voronezhskie tetradi",
    name_original="Воронежские тетради",
    period_key="モダニズム期",
    definition="マンデリシュタームが1934-37年の追放地ヴォロネジで書いた90余篇の詩。スターリン時代の極限状況下で書かれた最後の詩で、密度・複雑性の極限を示す。20世紀ロシア最も悲劇的な詩集の一つ。",
    background="スターリン恐怖時代マンデリシュタームの追放地ヴォロネジ滞在、最後創作期。",
    development="20世紀ロシア政治詩・追放詩の最重要規範作品。",
    historical_context="スターリン恐怖時代文化期。",
    primary_source_url=WIKI_RU+"Воронежские_тетради",
    primary_source_type="Wikipedia: Voronezhskie tetradi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"政治的弾圧下の詩的記録は、AI監視環境下の表現可能性問題の歴史的祖型として理論的に再読される。",
         "related_ai_phenomenon":"AI監視環境下の表現可能性"}])

add(**CR, name_ja="マンデリシューターム『ダンテをめぐる対話』",
    name_en="Mandelstam's Razgovor o Dante",
    name_original="Разговор о Данте",
    period_key="モダニズム期",
    definition="マンデリシュタームが1933年に書いたダンテ論。『神曲』の音響学・転位的詩学を分析し、20世紀ロシア・モダニズム批評の最重要規範文献となった。1967年に死後初出版された。",
    background="戦間期マンデリシュタームのダンテ集中研究、近代ロシアダンテ受容期。",
    development="20世紀ロシア・モダニズム批評・ダンテ批評の最重要規範文献。",
    historical_context="戦間期ロシア・ダンテ受容文化期。",
    primary_source_url=WIKI_RU+"Разговор_о_Данте",
    primary_source_type="Wikipedia: Razgovor o Dante",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**CR, name_ja="エセーニン『ペルシャ・モチーフ』",
    name_en="Esenin's Persidskie motivy",
    name_original="Персидские мотивы",
    period_key="モダニズム期",
    definition="セルゲイ・エセーニン(1895-1925)が1924-25年のバクー滞在から書いた連作詩。架空のペルシャを舞台に、ハーフェズ・サアディ系の東方抒情詩を露語に翻訳する。エセーニン晩年の傑作の一つで、20世紀ロシア・東方抒情詩の規範。",
    background="1920年代ロシア・東方文化の文学的受容、エセーニンのバクー滞在。",
    development="20世紀ロシア・東方抒情詩・新農民詩の規範作品。",
    historical_context="1920年代ロシア・東方文化期。",
    primary_source_url=WIKI_RU+"Персидские_мотивы",
    primary_source_type="Wikipedia: Persidskie motivy",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**CR, name_ja="フレーブニコフ『ザンゲジ』",
    name_en="Khlebnikov's Zangezi",
    name_original="Зангези",
    period_key="モダニズム期",
    definition="ヴェリミール・フレーブニコフ(1885-1922)が1922年に書いた長編詩劇。架空の予言者ザンゲジが20の「平面」(plokost)で語る言語実験的詩劇で、ザーウム言語(超意識的言語)の頂点を示す。20世紀ロシア未来派詩の最も実験的な作品。",
    background="ロシア未来派運動の頂点、フレーブニコフのザーウム言語実験。",
    development="20世紀ロシア未来派・実験詩の最重要規範作品。",
    historical_context="ロシア革命期未来派文化。",
    primary_source_url=WIKI_RU+"Зангези",
    primary_source_type="Wikipedia: Zangezi",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"超意識的・抽象的ザーウム言語実験は、AI生成における超人間的・自律的言語生成の祖型。",
         "related_ai_phenomenon":"AI生成における超人間的・自律的言語"}])

add(**CR, name_ja="マヤコフスキー『ズボンをはいた雲』",
    name_en="Mayakovsky's Oblako v shtanakh",
    name_original="Облако в штанах",
    period_key="モダニズム期",
    definition="ウラジーミル・マヤコフスキー(1893-1930)が1915年に発表した長詩。第一次大戦期の若き詩人の愛・芸術・社会・宗教の4つのテーマでの叫びを、巨大化された主体性と未来派形式で詩化する。20世紀ロシア未来派詩の頂点。",
    background="第一次大戦期マヤコフスキー20代、ロシア未来派運動最盛期。",
    development="20世紀ロシア未来派詩の最重要規範作品。",
    historical_context="第一次大戦期ロシア未来派文化期。",
    primary_source_url=WIKI_RU+"Облако_в_штанах",
    primary_source_type="Wikipedia: Oblako v shtanakh",
    importance_score=5, source_tier="secondary", canonical_in_region="core")


# ============================================================
# F: Peripheral (Pessoa, Cavafy, Yeats, Beckett) (7)
# ============================================================
add(**C, name_ja="ペソア『不安の書』",
    name_en="Pessoa's Livro do Desassossego",
    name_original="Livro do Desassossego",
    period_key="モダニズム期",
    definition="フェルナンド・ペソア(1888-1935)が約20年(1913-1934)書き続けた断片散文集。半異名ベルナルド・ソアレスを語り手に、リスボンの会計事務員の日常的形而上学的省察を記録する。20世紀ポルトガル・モダニズム散文の最重要規範作品。",
    background="20世紀ポルトガル・モダニズム文学、ペソアの異名創作期。",
    development="20世紀ポルトガル・モダニズム散文の最重要規範作品。",
    historical_context="20世紀ポルトガル・モダニズム文化期。",
    primary_source_url=WIKI_EN+"The_Book_of_Disquiet",
    primary_source_type="Wikipedia: Livro do Desassossego",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"半異名語り手による断片散文は、AI生成における擬似的・非自伝的語り手の祖型として理論的に共振する。",
         "related_ai_phenomenon":"AI生成における擬似語り手・複数主体著作"}])

add(**C, name_ja="ペソア異名アルベルト・カエイロ",
    name_en="Pessoa's heteronym Alberto Caeiro",
    name_original="Alberto Caeiro",
    period_key="モダニズム期",
    definition="ペソアの主要4異名の一人で、自然詩人・哲学的単純性の唱道者。「群れの番人」(O Guardador de Rebanhos, 1914)等を著し、ペソア他異名(レイス、カンポス)の精神的師として描かれる。20世紀ポルトガル詩異名創作の中核。",
    background="20世紀ポルトガル・モダニズム文学、ペソア異名体系の中核。",
    development="20世紀ポルトガル詩・異名創作研究の中心。",
    historical_context="20世紀ポルトガル・モダニズム文化期。",
    primary_source_url=WSRC_PT+"Autor:Alberto_Caeiro",
    primary_source_type="Wikisource PT: Caeiro",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ペソア異名アルヴァロ・デ・カンポス",
    name_en="Pessoa's heteronym Álvaro de Campos",
    name_original="Álvaro de Campos",
    period_key="モダニズム期",
    definition="ペソアの主要4異名の一人で、未来派エンジニア詩人。「勝利のオード」(Ode triunfal, 1914)、「タバコ屋」(Tabacaria, 1933)等を著し、20世紀ポルトガル未来派詩の中心。マリネッティ未来派受容と独自性を融合した。",
    background="20世紀ポルトガル・モダニズム文学、ペソア未来派受容期。",
    development="20世紀ポルトガル未来派詩・モダニズム詩の規範。",
    historical_context="20世紀ポルトガル・モダニズム文化期。",
    primary_source_url=WSRC_PT+"Autor:Álvaro_de_Campos",
    primary_source_type="Wikisource PT: Campos",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カヴァフィス選集",
    name_en="Cavafy's Selected Poems",
    name_original="Καβάφης",
    period_key="モダニズム期",
    definition="コンスタンディノス・カヴァフィス(1863-1933)がアレクサンドリアで書いた約154篇の確定詩。古代ヘレニズム期歴史を背景にした歴史詩と、同性愛抒情詩の二極で構成され、20世紀ギリシャ語モダニズム詩の最重要規範詩。",
    background="エジプト・アレクサンドリアのギリシャ語ディアスポラ文化、カヴァフィスの図書館員生活。",
    development="20世紀ギリシャ語モダニズム詩の最重要規範。",
    historical_context="20世紀初頭アレクサンドリア多文化文化期。",
    primary_source_url=WIKI_EN+"Constantine_P._Cavafy",
    primary_source_type="Wikipedia: Cavafy",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="イェイツ『塔』",
    name_en="Yeats's The Tower",
    name_original="The Tower",
    period_key="モダニズム期",
    definition="ウィリアム・バトラー・イェイツ(1865-1939)が1928年に発表した詩集。「ビザンティウムへの航海」「レダと白鳥」「内戦に際しての省察」等を含み、晩年イェイツの最高傑作詩集の一つ。20世紀英語モダニズム詩の規範詩集。",
    background="戦間期アイルランド独立戦争・内戦後、イェイツのバリリー塔購入時代。",
    development="20世紀英語モダニズム詩・晩年イェイツ研究の中心詩集。",
    historical_context="戦間期アイルランド独立後文化期。",
    primary_source_url=WIKI_EN+"The_Tower_(poetry_collection)",
    primary_source_type="Wikipedia: The Tower",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ベケット『ゴドーを待ちながら』",
    name_en="Beckett's En attendant Godot",
    name_original="En attendant Godot",
    period_key="後期モダニズム期",
    definition="サミュエル・ベケット(1906-1989)が1953年に上演した戯曲。エストラゴンとウラジミルの2人がゴドーを待ち続ける2幕の不条理劇で、20世紀世界の不条理演劇の最重要規範作品となった。1969年ノーベル賞授賞理由。",
    background="戦後パリ・ベケット仏語創作期、不条理演劇運動の中核。",
    development="20世紀世界の不条理演劇の最重要規範作品。",
    historical_context="戦後パリ前衛演劇期。",
    primary_source_url=WIKI_FR+"En_attendant_Godot",
    primary_source_type="Wikipedia: En attendant Godot",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"不在の他者を待ち続ける主体構造は、AI環境における不在的他者・対話相手の生成問題と理論的に共振する。",
         "related_ai_phenomenon":"AI環境における不在的他者・対話相手"}])

add(**C, name_ja="ベケット三部作（モロイ・マロウン・名づけえぬ）",
    name_en="Beckett's Trilogy (Molloy, Malone Dies, The Unnamable)",
    name_original="Molloy, Malone meurt, L'Innommable",
    period_key="後期モダニズム期",
    definition="ベケットが1951-53年に発表した仏語三部作小説。語り手の自我が次第に解体・縮減し、最終巻『名づけえぬもの』では声のみの存在に至る。20世紀小説の主体解体実験の極限点で、ベケット小説の頂点。",
    background="戦後パリ・ベケット仏語創作期、極限的主体解体実験。",
    development="20世紀小説・主体解体実験の最重要規範作品。",
    historical_context="戦後パリ前衛文学期。",
    primary_source_url=WIKI_EN+"The_Trilogy_(Beckett)",
    primary_source_type="Wikipedia: Beckett Trilogy",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"主体の段階的解体・声のみへの縮減は、AI生成における非身体的・声のみ主体性の祖型として理論的に共振する。",
         "related_ai_phenomenon":"AI生成における非身体的・声のみ主体"}])


# ============================================================
# G: Avant-garde deeper (5)
# ============================================================
add(**C, name_ja="シュヴィッタース『アンナ・ブルーメに』",
    name_en="Schwitters's An Anna Blume",
    name_original="An Anna Blume",
    period_key="モダニズム期",
    definition="クルト・シュヴィッタース(1887-1948)が1919年に発表したダダ詩。「アンナ・ブルーメ」へのナンセンス的恋歌で、ダダの言語遊戯・字面遊びの代表作。20世紀ドイツ語ダダ詩の最重要規範作品。",
    background="第一次大戦後ハノーファー・メルツ運動、シュヴィッタース総合芸術期。",
    development="20世紀ドイツ語ダダ詩の最重要規範作品。",
    historical_context="第一次大戦後ドイツダダ文化期。",
    primary_source_url=WIKI_DE+"An_Anna_Blume",
    primary_source_type="Wikipedia: An Anna Blume",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="シュヴィッタース『原ソナタ』",
    name_en="Schwitters's Ursonate",
    name_original="Ursonate",
    period_key="モダニズム期",
    definition="シュヴィッタースが1922-32年に作曲した音響詩。ソナタ形式で構成された純粋音響(無意味音節)による詩で、20世紀音響詩・パフォーマンス詩学の最重要規範作品となった。",
    background="戦間期ドイツダダ・メルツ運動、シュヴィッタースの音響詩学確立期。",
    development="20世紀音響詩・パフォーマンス詩学の最重要規範作品。",
    historical_context="戦間期ドイツ前衛文化期。",
    primary_source_url=WIKI_DE+"Ursonate",
    primary_source_type="Wikipedia: Ursonate",
    importance_score=3, source_tier="secondary", canonical_in_region="minor",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"純粋音響による意味解離詩学は、AI音声合成・音響生成における意味機能性問題の祖型。",
         "related_ai_phenomenon":"AI音声合成における意味解離・音響生成"}])

add(**C, name_ja="ルイス『ブラスト』",
    name_en="Lewis's BLAST",
    name_original="BLAST",
    period_key="モダニズム期",
    definition="ウィンダム・ルイス(1882-1957)が1914-15年に主宰した雑誌。タイポグラフィカルに革新的な「ヴォーティシズム」運動の機関誌で、パウンド、エリオット、フォードらを掲載した。20世紀英国前衛運動の最重要規範雑誌。",
    background="第一次大戦初期ロンドン・ヴォーティシズム運動、未来派・キュビスム英国受容期。",
    development="20世紀英国前衛運動・タイポグラフィ実験の最重要規範雑誌。",
    historical_context="第一次大戦初期英国前衛文化期。",
    primary_source_url=WIKI_EN+"BLAST_(magazine)",
    primary_source_type="Wikipedia: BLAST",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ルイス『ターパ』",
    name_en="Lewis's Tarr",
    name_original="Tarr",
    period_key="モダニズム期",
    definition="ウィンダム・ルイスが1918年に発表した長編小説。第一次大戦前パリの英国人芸術家ターパとドイツ人芸術家クライスラーの対立を描く。ヴォーティシズム小説美学の頂点で、20世紀英国前衛小説の規範作品。",
    background="第一次大戦期ルイスのヴォーティシズム小説実験、近代芸術家対立の文学化。",
    development="20世紀英国前衛小説・ヴォーティシズム小説の規範作品。",
    historical_context="第一次大戦期英国前衛文化期。",
    primary_source_url=GUTEN+"ebooks/22566",
    primary_source_type="Project Gutenberg: Tarr",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ブルトン『ナジャ』",
    name_en="Breton's Nadja",
    name_original="Nadja",
    period_key="モダニズム期",
    definition="アンドレ・ブルトン(1896-1966)が1928年に発表した小説。語り手「私」とパリの神秘的女性ナジャの邂逅を、写真・「客観的偶然」・夢の記述で構成する。20世紀シュルレアリスム小説の最重要規範作品。",
    background="戦間期パリ・シュルレアリスム運動の頂点、ブルトン文学実験期。",
    development="20世紀シュルレアリスム小説・写真テクストの最重要規範作品。",
    historical_context="戦間期パリ・シュルレアリスム文化期。",
    primary_source_url=WIKI_FR+"Nadja_(roman)",
    primary_source_type="Wikipedia: Nadja",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"写真・偶然・夢を統合する小説形式は、AI生成における多モーダル・確率的著作の祖型。",
         "related_ai_phenomenon":"AI生成における多モーダル・確率的著作"}])


# ============================================================
# Cross-domain attachments (>= 18)
# ============================================================
def _attach_cross(name: str, cd_list: list[dict]) -> None:
    for c in CONCEPTS:
        if c["name_ja"] == name:
            existing = c.get("cross_domain", [])
            c["cross_domain"] = existing + cd_list
            return


_attach_cross("パウンド『キャントーズ』全体構造", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"イデオグラム的編集詩学",
     "description":"異文化テクスト並列のイデオグラム的編集は、20世紀モダニスト編集詩学の規範例。"}])

_attach_cross("パウンド『キャセイ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"翻訳詩学",
     "description":"異言語詩学の英語移植は、20世紀比較詩学・翻訳詩学の規範例。"}])

_attach_cross("エリオット『荒地』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"イデオグラム的長詩構造",
     "description":"多言語・多テクスト縫合の長詩構造は、20世紀モダニズム長詩詩学の最重要規範例。"}])

_attach_cross("エリオット『伝統と個人の才能』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"非個性詩学",
     "description":"作者の非個性化論は、20世紀新批評・モダニズム批評の最重要起点。"}])

_attach_cross("ウルフ『オーランドー』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"ジェンダー越境性の人類学",
     "description":"性別越境主体の文学化は、20世紀ジェンダー人類学・クィア研究の中心テクスト。"}])

_attach_cross("ウルフ『三ギニー』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"フェミニスト平和論",
     "description":"戦争・家父長制連関論は、20世紀フェミニスト平和論・反戦論の最重要起点。"}])

_attach_cross("スタイン『優しいボタン』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"反指示的言語実験",
     "description":"キュビスト的反指示言語実験は、20世紀英語実験詩学の最も急進的範型。"}])

_attach_cross("マラルメ『骰子一擲』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"視覚的活字詩学",
     "description":"活字配置の意味化は、20世紀視覚詩・コンクリート詩学の最重要起点。"}])

_attach_cross("ジッド『贋金つくり』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"メタフィクション詩学",
     "description":"小説内小説の入れ子構造は、20世紀メタフィクション詩学の規範例。"}])

_attach_cross("ホフマンスタール『チャンドス卿の手紙』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"言語懐疑主義",
     "description":"言語の指示性懐疑は、20世紀言語批判哲学・モダニズム言語論の最重要起点。"}])

_attach_cross("リルケ『マルテの手記』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"近代主体危機論",
     "description":"近代主体の断片的危機の文学化は、20世紀近代主体危機論の最重要規範例。"}])

_attach_cross("ヘッセ『ガラス玉演戯』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"知識生産の組合せ論",
     "description":"知識・象徴の演戯的・組合せ的生産論は、20世紀知識生産論・記号論の規範例。"}])

_attach_cross("クラウス『人類最後の日々』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"言語批判の文化人類学",
     "description":"ジャーナリズム言語崩壊の引用コラージュ的批判は、20世紀メディア人類学の祖型。"}])

_attach_cross("ピランデッロ『作者を探す六人の登場人物』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"メタ演劇詩学",
     "description":"作者・登場人物境界の解体は、20世紀メタ演劇・不条理演劇の最重要起点。"}])

_attach_cross("ロルカ『ニューヨークの詩人』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"近代都市の人類学",
     "description":"大都市の非人間化批判は、20世紀都市人類学・モダニズム批評の中心テクスト。"}])

_attach_cross("マンデリシュターム『ヴォロネジ・ノート』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"政治的弾圧下の表現論",
     "description":"政治的弾圧下の詩的記録は、20世紀全体主義論・表現倫理の規範例。"}])

_attach_cross("フレーブニコフ『ザンゲジ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"超意識的言語(ザーウム)",
     "description":"ザーウム言語実験は、20世紀ロシア未来派・実験詩学の最重要規範例。"}])

_attach_cross("ペソア『不安の書』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"異名・複数主体性論",
     "description":"半異名語り手による断片散文は、20世紀複数主体性論・異名論の最重要規範例。"}])

_attach_cross("ベケット『ゴドーを待ちながら』", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"不条理主体論",
     "description":"不在の他者を待つ主体構造は、20世紀不条理主体論・実存主義文学の最重要規範例。"}])

_attach_cross("ベケット三部作（モロイ・マロウン・名づけえぬ）", [
    {"target_db":"PHIL","link_type":"shared_concept",
     "target_entity_name":"主体解体論",
     "description":"主体の段階的解体・声のみへの縮減は、20世紀主体解体論・脱構築の文学的規範例。"}])

_attach_cross("ブルトン『ナジャ』", [
    {"target_db":"AN","link_type":"shared_concept",
     "target_entity_name":"客観的偶然の人類学",
     "description":"写真・偶然・夢を統合する小説形式は、20世紀シュルレアリスム人類学の規範例。"}])

_attach_cross("シュヴィッタース『原ソナタ』", [
    {"target_db":"PT","link_type":"shared_concept",
     "target_entity_name":"音響詩学",
     "description":"純粋音響による意味解離詩学は、20世紀音響詩・パフォーマンス詩学の最重要規範例。"}])


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
                    print(f"  [warn] fourth_transform failed for {entry['name_ja']}: {e}")
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
        print(f"[c10-w23] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c10-w23] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        primary = sum(1 for c in CONCEPTS if c.get("source_tier") == "primary")
        secondary = sum(1 for c in CONCEPTS if c.get("source_tier") == "secondary")
        tertiary = sum(1 for c in CONCEPTS if c.get("source_tier") == "tertiary")
        total = primary + secondary + tertiary
        print(f"[c10-w23] tiers: primary={primary} secondary={secondary} tertiary={tertiary} total={total} (primary%={100*primary/total:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
