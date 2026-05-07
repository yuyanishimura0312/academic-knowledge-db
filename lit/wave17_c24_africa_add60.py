"""LIT-DB Phase 2 Wave 17 — C24: Africa ADD 60.

Subfield: lit_africa (id=15). Existing 80. Target 400.
This wave adds 60 NEW non-overlapping covering Anglophone classics
detail, Francophone補完, South African深掘り, Lusophone, Maghreb,
Egypt-Sudan, women's writing, 21c novel, poetry, drama, criticism.

Targets: fourth_transform_tags >= 18, cross_domain >= 14.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


PERIODS = [
    ("独立後初期", "Early Post-Independence", 1960, 1980,
     "アフリカ諸国の独立直後の文学的高揚期。"),
    ("独立後中期", "Mid Post-Independence", 1980, 2000,
     "アパルトヘイト終結期文学。ジェンダー・国民国家の幻滅・移動の主題化。"),
    ("21世紀アフリカ文学", "21st Century African Literature", 2000, 2030,
     "アフリカ系ディアスポラ作家の世界文学的台頭期。"),
    ("マグレブ近代", "Maghreb Modern", 1950, 2010,
     "アルジェリア独立戦争前後から21世紀初頭までのマグレブ文学。"),
    ("葡語圏アフリカ独立後", "Lusophone Africa Post-Independence", 1975, 2025,
     "アンゴラ・モザンビーク・カーボヴェルデ独立以降の葡語圏アフリカ文学。"),
    ("植民地末期", "Late Colonial Africa", 1930, 1960,
     "ネグリチュード・初期反植民地文学・アフリカ独立直前期。"),
    ("エジプト・スーダン近現代", "Egypt-Sudan Modern", 1900, 2025,
     "アラビア語近代エジプト・スーダン文学（マフフーズ世代以降）。"),
]

REGION = "グローバルサウス"
SUBFIELD = "lit_africa"

WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
WIKI_AR = "https://ar.wikipedia.org/wiki/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code=SUBFIELD, region=REGION, original_script="roman")
CAR = dict(subfield_code=SUBFIELD, region=REGION, original_script="arabic")


# A. Anglophone classics 補完 (Achebe/Ngugi/Soyinka/Head/Tutuola) (12)
add(**C, name_ja="アチェベ『崩れゆく絆』",
    name_en="Achebe's Things Fall Apart",
    name_original="Things Fall Apart",
    period_key="植民地末期",
    definition="チヌア・アチェベ（1930-2013）が1958年に発表した長編小説。イボ族のオコンクォを主人公に植民地接触期の文化崩壊を描く。アフリカ近代文学の出発点。",
    background="ジョイス・ケイリー『ミスター・ジョンソン』への応答、英国植民地教育下のイボ族出身作家による反植民地的応答。",
    development="アチェベ三部作の起点となり、Heinemann African Writers Series創立の中核。世界55言語に翻訳された。",
    historical_context="1950年代末ナイジェリア独立(1960)直前期。",
    primary_source_url=WIKI_EN+"Things_Fall_Apart",
    primary_source_type="Wikipedia: Things Fall Apart",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"アチェベは英語による土着文化の文学的再構築を実践した。AI時代の多言語生成における文化的等価性の祖型。",
         "related_ai_phenomenon":"AI多言語生成における文化的等価性"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"イボ族文化人類学",
         "description":"『崩れゆく絆』は人類学的イボ族研究と並行する文学的民族誌的作品。"}])

add(**C, name_ja="アチェベ『神の矢』",
    name_en="Achebe's Arrow of God",
    name_original="Arrow of God",
    period_key="植民地末期",
    definition="アチェベが1964年に発表した第三長編小説。1920年代植民地ナイジェリアのイボ族司祭エズールを主人公に、伝統宗教権威と植民地行政・キリスト教宣教の三重衝突を描いた。",
    background="間接統治下のイボ族司祭職と植民地行政の構造的対立。",
    development="アチェベ三部作の頂点とされ、後の脱植民地化文学の規範作。",
    historical_context="1920年代英領ナイジェリアの間接統治期。",
    primary_source_url=WIKI_EN+"Arrow_of_God",
    primary_source_type="Wikipedia: Arrow of God",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"権威","status":"rethinking",
         "rationale":"アチェベ『神の矢』は伝統的宗教権威と植民地行政の三重衝突を主題化する。AI時代の権威の多重化への祖型。",
         "related_ai_phenomenon":"AI時代の権威の多重化"}])

add(**C, name_ja="アチェベ『民衆の人』",
    name_en="Achebe's A Man of the People",
    name_original="A Man of the People",
    period_key="独立後初期",
    definition="アチェベが1966年に発表した長編。独立後ナイジェリアの政治腐敗を諷刺し、ビアフラ戦争・軍事クーデターを予言した政治小説として読まれた。",
    background="独立後ナイジェリアの第一共和制（1963-66）の政治的腐敗。",
    development="ナイジェリア独立後文学の政治的諷刺潮流の起点。",
    historical_context="1966年ナイジェリア軍事クーデター直前期。",
    primary_source_url=WIKI_EN+"A_Man_of_the_People",
    primary_source_type="Wikipedia: A Man of the People",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"独立後アフリカの政治哲学",
         "description":"アチェベの政治諷刺はファノン的脱植民地化政治哲学と並行する。"}])

add(**C, name_ja="アチェベ『サバンナの蟻塚』",
    name_en="Achebe's Anthills of the Savannah",
    name_original="Anthills of the Savannah",
    period_key="独立後中期",
    definition="アチェベが1987年に発表した長編。架空のアフリカ国カンガンを舞台に独裁・知識人・女性の役割を描き、1987年ブッカー賞最終候補。",
    background="20年の長編創作中断の後の復帰作、1980年代アフリカ独裁体制への応答。",
    development="ポストコロニアル・アフリカ政治小説の規範作の一つ。",
    historical_context="1980年代ナイジェリア軍政期。",
    primary_source_url=WIKI_EN+"Anthills_of_the_Savannah",
    primary_source_type="Wikipedia: Anthills of the Savannah",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"アチェベの多声的語りは、AI時代の集合的・多視点的作者性の祖型。",
         "related_ai_phenomenon":"AIによる多視点的物語生成"}])

add(**C, name_ja="ンギュギ『泣くな、わが子よ』",
    name_en="Ngugi's Weep Not, Child",
    name_original="Weep Not, Child",
    period_key="独立後初期",
    definition="ンギュギ・ワ・ティオンゴ（1938-）が1964年に発表した長編。マウマウ蜂起期のキクユ族少年ンジョロゲを主人公とする、東アフリカ初の英語長編小説。",
    background="マウマウ蜂起(1952-60)とケニア独立(1963)直後期。",
    development="ンギュギ初期三部作の起点となり、東アフリカ近代英語文学の出発点。",
    historical_context="ケニア独立直後の歴史的記憶政治。",
    primary_source_url=WIKI_EN+"Weep_Not,_Child",
    primary_source_type="Wikipedia: Weep Not, Child",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"マウマウ蜂起人類学",
         "description":"ンギュギ初期長編はキクユ族マウマウ蜂起の文化人類学（ジョモ・ケニヤッタ等）と並行する。"}])

add(**C, name_ja="ンギュギ『一粒の麦』",
    name_en="Ngugi's A Grain of Wheat",
    name_original="A Grain of Wheat",
    period_key="独立後初期",
    definition="ンギュギが1967年に発表した長編。ケニア独立直前を舞台に、マウマウ蜂起の裏切り・記憶・贖罪を多視点で描いた、ンギュギ初期文学の頂点。",
    background="マウマウ蜂起の歴史的記憶と、ファノン的脱植民地化思想のンギュギによる吸収。",
    development="アフリカ現代文学の正典作の一つ。後の『血の花弁』へ繋がる転換点。",
    historical_context="1960年代ケニアの独立記憶構築期。",
    primary_source_url=WIKI_EN+"A_Grain_of_Wheat",
    primary_source_type="Wikipedia: A Grain of Wheat",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ンギュギ『血の花弁』",
    name_en="Ngugi's Petals of Blood",
    name_original="Petals of Blood",
    period_key="独立後初期",
    definition="ンギュギが1977年に発表した長編。独立後ケニアの新植民地的資本主義を批判し、4人の容疑者の視点で連続殺人を描いた政治的長編。執筆後ンギュギは投獄された。",
    background="独立後ケニア政府の腐敗と、マルクス主義的脱植民地化への急進化。",
    development="ンギュギの投獄(1977-78)を招き、後にギクユ語創作への転換点となった。",
    historical_context="ケニヤッタ政権末期の政治的緊張。",
    primary_source_url=WIKI_EN+"Petals_of_Blood",
    primary_source_type="Wikipedia: Petals of Blood",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ンギュギ『精神の脱植民地化』",
    name_en="Ngugi's Decolonising the Mind",
    name_original="Decolonising the Mind",
    period_key="独立後中期",
    definition="ンギュギが1986年に発表したエッセイ集。アフリカ作家がアフリカ語で書くべきとする言語論争を理論化し、英語による創作からギクユ語創作への転換を宣言した。",
    background="1962年マケレレ会議以降の言語論争と、ンギュギ自身のギクユ語転換実践。",
    development="アフリカ言語論争の中核文献。21世紀の世界文学言語政治の中心参照点。",
    historical_context="1980年代アフリカ文学の言語選択期。",
    primary_source_url=WIKI_EN+"Decolonising_the_Mind",
    primary_source_type="Wikipedia: Decolonising the Mind",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"ンギュギの言語脱植民地化論は、AI時代における言語覇権・低資源言語の権力分析の理論的祖型。",
         "related_ai_phenomenon":"AIにおける言語覇権・低資源言語"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"言語の脱植民地化",
         "description":"ンギュギは脱植民地化哲学とアフリカ言語政治学の交差点。"}])

add(**C, name_ja="ソインカ『死と王の馬丁』",
    name_en="Soyinka's Death and the King's Horseman",
    name_original="Death and the King's Horseman",
    period_key="独立後初期",
    definition="ウォーレ・ソインカ（1934-）が1975年に発表した戯曲。1946年オヨ王国の王の馬丁エレシン・オバの儀礼的自死を植民地行政が中断する事件を、ヨルバ宗教哲学的悲劇として上演した。",
    background="1946年オヨ王葬儀事件の史実、ヨルバ宗教の儀礼的自死観念。",
    development="ソインカ・ノーベル文学賞(1986)の中心作の一つ。世界戯曲史の正典化。",
    historical_context="1970年代ナイジェリア・ヨルバ伝統の文学的再構築期。",
    primary_source_url=WIKI_EN+"Death_and_the_King%27s_Horseman",
    primary_source_type="Wikipedia: Death and the King's Horseman",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"ヨルバ宗教",
         "description":"ソインカ戯曲はヨルバ宗教人類学（ピーター・モートン＝ウィリアムズ等）と並行する。"}])

add(**C, name_ja="ソインカ『獅子と宝石』",
    name_en="Soyinka's The Lion and the Jewel",
    name_original="The Lion and the Jewel",
    period_key="植民地末期",
    definition="ソインカが1959年に執筆した喜劇。ヨルバ村落の長老バロカと教師ラクンレの娘シディをめぐる婚姻の競争を、伝統と近代の風刺的対比で描いた初期代表作。",
    background="1950年代末ナイジェリアの近代化と伝統の緊張。",
    development="ソインカ初期戯曲の代表作。アフリカ大学演劇の古典化。",
    historical_context="ナイジェリア独立直前(1959)期。",
    primary_source_url=WIKI_EN+"The_Lion_and_the_Jewel",
    primary_source_type="Wikipedia: The Lion and the Jewel",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ソインカ『アケ：幼年時代』",
    name_en="Soyinka's Aké: The Years of Childhood",
    name_original="Aké: The Years of Childhood",
    period_key="独立後中期",
    definition="ソインカが1981年に発表した自伝。ヨルバ族の町アケでの幼年期(1934-)を描き、世界自伝文学の正典化。",
    background="ヨルバ族司祭家系の家族環境とキリスト教宣教学校の幼年期。",
    development="ソインカ自伝四部作の起点となり、世界自伝文学の正典の一つ。",
    historical_context="1930-40年代英領ナイジェリアの植民地末期。",
    primary_source_url=WIKI_EN+"Ak%C3%A9:_The_Years_of_Childhood",
    primary_source_type="Wikipedia: Aké",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ベシー・ヘッド『マル』",
    name_en="Bessie Head's Maru",
    name_original="Maru",
    period_key="独立後初期",
    definition="ベシー・ヘッド（1937-1986）が1971年に発表した長編。ボツワナ村落を舞台に、サン人（マサルワ）女性教師マルガレットへの差別・愛・解放を描いた。",
    background="ヘッドのアパルトヘイト南アから亡命後のボツワナ生活、サン人差別の現実。",
    development="アフリカ女性文学の先駆作。サン人の文学的代表作。",
    historical_context="1960-70年代ボツワナ独立後期。",
    primary_source_url=WIKI_EN+"Maru_(novel)",
    primary_source_type="Wikipedia: Maru",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# B. Francophone補完 (Sembene/Kourouma/Senghor/Diop/Beti/Oyono/Kane) (10)
add(**C, name_ja="センベーヌ『神の森』",
    name_en="Sembène's Les Bouts de bois de Dieu",
    name_original="Les Bouts de bois de Dieu",
    period_key="植民地末期",
    definition="ウスマン・センベーヌ（1923-2007）が1960年に発表した長編。1947-48年ダカール=ニジェール鉄道ストライキを多視点で描き、仏語圏アフリカ文学の社会的リアリズムの代表作。",
    background="センベーヌ自身が労働者として参加したダカール=ニジェール鉄道スト史実。",
    development="アフリカ社会的リアリズムの正典化。後にセンベーヌは映画監督に転身。",
    historical_context="1940年代仏領西アフリカの労働運動期。",
    primary_source_url=WIKI_FR+"Les_Bouts_de_bois_de_Dieu",
    primary_source_type="Wikipedia FR: Les Bouts de bois de Dieu",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="センベーヌ『ハラ』",
    name_en="Sembène's Xala",
    name_original="Xala",
    period_key="独立後初期",
    definition="センベーヌが1973年に発表した中編小説（後に同タイトルで映画化）。独立後セネガルの新興ブルジョワ実業家を主人公に、性的不能（ハラ）を諷刺的隠喩として独立後の経済的従属を描いた。",
    background="独立後セネガルの新植民地的経済構造への風刺。",
    development="センベーヌ映画『ハラ』(1975)を経て、世界アフリカ映画・文学の正典。",
    historical_context="1970年代セネガル新植民地経済期。",
    primary_source_url=WIKI_FR+"Xala_(roman)",
    primary_source_type="Wikipedia FR: Xala",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="シェイク・ハミドゥ・カン『曖昧な冒険』",
    name_en="Cheikh Hamidou Kane's L'Aventure ambiguë",
    name_original="L'Aventure ambiguë",
    period_key="植民地末期",
    definition="シェイク・ハミドゥ・カン（1928-）が1961年に発表した長編。セネガル・フラニ族のサンバ・ジャロを主人公に、イスラーム教育と西欧近代教育の哲学的緊張を描いた仏語圏アフリカ哲学小説の代表作。",
    background="セネガル・スーフィー教育（ティジャーニーヤ教団）と仏植民地学校の二重教育体験。",
    development="アフリカ哲学小説の正典化。21世紀イスラーム・アフリカ思想の前提条件。",
    historical_context="セネガル独立(1960)直後の教育文化の二重性。",
    primary_source_url=WIKI_FR+"L%27Aventure_ambigu%C3%AB",
    primary_source_type="Wikipedia FR: L'Aventure ambiguë",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"イスラーム哲学とアフリカ近代",
         "description":"カンはイスラーム哲学とアフリカ近代教育の哲学的対話を文学化した。"}])

add(**C, name_ja="クルマ『独立の太陽』",
    name_en="Kourouma's Les Soleils des indépendances",
    name_original="Les Soleils des indépendances",
    period_key="独立後初期",
    definition="アマドゥ・クルマ（1927-2003）が1968年に発表した長編。マリンケ語的フランス語で独立後コートジボワールの没落王族ファマを描いた、仏語圏アフリカ文学の言語革新の起点。",
    background="マリンケ語話者クルマによるフランス語の脱植民地的変形。",
    development="アフリカ仏語文学の言語的脱植民地化の正典作。",
    historical_context="1960年代独立後西アフリカの社会変動期。",
    primary_source_url=WIKI_FR+"Les_Soleils_des_ind%C3%A9pendances",
    primary_source_type="Wikipedia FR: Les Soleils des indépendances",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"クルマのマリンケ語的フランス語は、AI時代の多言語混淆生成の歴史的祖型。",
         "related_ai_phenomenon":"AI多言語混淆生成"}])

add(**C, name_ja="クルマ『アラーは義務ではない』",
    name_en="Kourouma's Allah n'est pas obligé",
    name_original="Allah n'est pas obligé",
    period_key="21世紀アフリカ文学",
    definition="クルマが2000年に発表した長編。リベリア・シエラレオネ内戦の少年兵ビラヒマを語り手に、子供の戦争体験をピジン仏語で描いた。2000年ルノドー賞・ゴンクール高校生賞受賞。",
    background="1990年代西アフリカ内戦（リベリア・シエラレオネ）と少年兵問題。",
    development="アフリカ少年兵文学の正典作。世界文学賞受賞による国際化。",
    historical_context="2000年代西アフリカ内戦終結期。",
    primary_source_url=WIKI_FR+"Allah_n%27est_pas_oblig%C3%A9",
    primary_source_type="Wikipedia FR: Allah n'est pas obligé",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="サンゴール『影の歌』",
    name_en="Senghor's Chants d'ombre",
    name_original="Chants d'ombre",
    period_key="植民地末期",
    definition="レオポール・セダール・サンゴール（1906-2001）が1945年に発表した処女詩集。ネグリチュード詩運動の出発点で、アフリカ的リズム・祖国記憶・パリでの追放を主題化した。",
    background="サンゴール・パリ留学(1928-)期のネグリチュード運動形成。",
    development="ネグリチュード詩運動の起点。サンゴール詩集全体の出発点。",
    historical_context="第二次大戦末期パリの黒人知識人運動。",
    primary_source_url=WIKI_FR+"Chants_d%27ombre",
    primary_source_type="Wikipedia FR: Chants d'ombre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サンゴール『黒い犠牲』",
    name_en="Senghor's Hosties noires",
    name_original="Hosties noires",
    period_key="植民地末期",
    definition="サンゴールが1948年に発表した詩集。第二次大戦の黒人兵士を「黒い聖体（hosties noires）」として描き、戦争・植民地化・救済を統合した戦後ネグリチュード詩の代表作。",
    background="サンゴール自身の独軍捕虜体験(1940-42)とフランス黒人連隊の戦死記憶。",
    development="ネグリチュード詩の戦後展開の中核作。",
    historical_context="第二次大戦終結直後の仏領アフリカ植民地兵士の記憶政治。",
    primary_source_url=WIKI_FR+"Hosties_noires",
    primary_source_type="Wikipedia FR: Hosties noires",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ビラゴ・ジョップ『アマドゥ・クンバ物語』",
    name_en="Birago Diop's Contes d'Amadou Koumba",
    name_original="Les Contes d'Amadou Koumba",
    period_key="植民地末期",
    definition="ビラゴ・ジョップ（1906-1989）が1947年に発表した民話集。セネガル・ウォロフ族のグリオ、アマドゥ・クンバから採集した口承物語をフランス語で文学化した、口承文学の文学化の先駆作。",
    background="ビラゴの父系グリオ系統とパリでの民俗学的出版機運。",
    development="アフリカ口承文学の文学化の正典化。後の口承文学集成の祖型。",
    historical_context="1940年代仏領セネガルの民俗学的回帰期。",
    primary_source_url=WIKI_FR+"Les_Contes_d%27Amadou_Koumba",
    primary_source_type="Wikipedia FR: Contes d'Amadou Koumba",
    importance_score=3, source_tier="primary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"グリオ口承伝統",
         "description":"ビラゴ・ジョップの民話集はセネガル民俗学（グリオ研究）と並行する。"}])

add(**C, name_ja="モンゴ・ベティ『憐れなキリスト・ボンバ』",
    name_en="Mongo Beti's Le Pauvre Christ de Bomba",
    name_original="Le Pauvre Christ de Bomba",
    period_key="植民地末期",
    definition="モンゴ・ベティ（1932-2001）が1956年に発表した長編。カメルーン宣教師ドリュモンを通じて植民地キリスト教宣教の偽善を諷刺した、仏語圏アフリカ反植民地小説の代表作。",
    background="ベティ自身のカメルーン宣教学校体験と仏領カメルーン独立闘争(UPC)の文脈。",
    development="仏語圏アフリカ反植民地文学の正典化。",
    historical_context="1950年代カメルーン独立闘争期。",
    primary_source_url=WIKI_FR+"Le_Pauvre_Christ_de_Bomba",
    primary_source_type="Wikipedia FR: Le Pauvre Christ de Bomba",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="フェルディナン・オヨノ『ボーイの一生』",
    name_en="Ferdinand Oyono's Une vie de boy",
    name_original="Une vie de boy",
    period_key="植民地末期",
    definition="フェルディナン・オヨノ（1929-2010）が1956年に発表した長編。カメルーン人ボーイのトゥンディの植民地体験を日記形式で描き、植民地暴力の文学化の正典作となった。",
    background="仏領カメルーンの植民地下のボーイ労働制度。",
    development="仏語圏アフリカ反植民地小説の正典作。後にオヨノは外交官に転身。",
    historical_context="1950年代仏領カメルーン独立直前期。",
    primary_source_url=WIKI_FR+"Une_vie_de_boy",
    primary_source_type="Wikipedia FR: Une vie de boy",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# C. South African 深掘り (Coetzee/Gordimer/Brink/Fugard/Plaatje) (10)
add(**C, name_ja="クッツェー『恥辱』",
    name_en="Coetzee's Disgrace",
    name_original="Disgrace",
    period_key="21世紀アフリカ文学",
    definition="J・M・クッツェー（1940-）が1999年に発表した長編。ポストアパルトヘイト南アフリカの大学教授デヴィッド・ラウリーの転落を描き、1999年ブッカー賞受賞。クッツェー・ノーベル賞(2003)の中心作。",
    background="アパルトヘイト終結(1994)後の南アフリカの新しい暴力・人種関係の現実。",
    development="クッツェー後期の倫理的小説の頂点作。",
    historical_context="1990年代末ポストアパルトヘイト南アフリカ社会の緊張。",
    primary_source_url=WIKI_EN+"Disgrace",
    primary_source_type="Wikipedia: Disgrace",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"クッツェー『恥辱』は脱主体化・脆弱性の倫理を扱う。AI時代の主体・倫理関係の哲学的祖型。",
         "related_ai_phenomenon":"AI時代の主体・脆弱性の倫理"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"脆弱性の倫理",
         "description":"クッツェーはバトラー・ヌスバウム的脆弱性の倫理と並行する文学的探求。"}])

add(**C, name_ja="クッツェー『野蛮人を待ちながら』",
    name_en="Coetzee's Waiting for the Barbarians",
    name_original="Waiting for the Barbarians",
    period_key="独立後初期",
    definition="クッツェーが1980年に発表した長編。架空の帝国の辺境で「野蛮人」への暴力行使を目撃する治安判事を主人公に、植民地暴力の構造を寓話化した。",
    background="アパルトヘイト南アフリカの暴力・拷問の現実、カヴァフィス詩への応答。",
    development="クッツェー初期の代表作。世界寓話文学の正典化。",
    historical_context="1980年代アパルトヘイト南アフリカの政治危機期。",
    primary_source_url=WIKI_EN+"Waiting_for_the_Barbarians",
    primary_source_type="Wikipedia: Waiting for the Barbarians",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="クッツェー『マイケル・Kの生涯と時代』",
    name_en="Coetzee's Life & Times of Michael K",
    name_original="Life & Times of Michael K",
    period_key="独立後中期",
    definition="クッツェーが1983年に発表した長編。架空の内戦下南アフリカの口蓋裂男マイケル・Kの放浪を描き、1983年ブッカー賞受賞。",
    background="1980年代アパルトヘイト南アフリカの内戦的緊張。",
    development="クッツェー初期長編三部作の頂点。",
    historical_context="1980年代南アフリカの非常事態期。",
    primary_source_url=WIKI_EN+"Life_%26_Times_of_Michael_K",
    primary_source_type="Wikipedia: Life & Times of Michael K",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="クッツェー『敵あるいはフォー』",
    name_en="Coetzee's Foe",
    name_original="Foe",
    period_key="独立後中期",
    definition="クッツェーが1986年に発表した長編。デフォー『ロビンソン・クルーソー』を女性語り手スーザン・バートンの視点で書き直し、植民地物語の正典化を脱構築した。",
    background="ポストコロニアル理論の文学的応用、デフォー古典のメタフィクション化。",
    development="ポストコロニアル小説の正典化作の一つ。",
    historical_context="1980年代世界文学のポストコロニアル転換期。",
    primary_source_url=WIKI_EN+"Foe_(novel)",
    primary_source_type="Wikipedia: Foe",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ゴーディマー『七月の人々』",
    name_en="Gordimer's July's People",
    name_original="July's People",
    period_key="独立後中期",
    definition="ナディン・ゴーディマー（1923-2014）が1981年に発表した長編。架空の南ア革命下、白人スマレス家がボーイ・ジュライの村に避難する状況を描き、人種関係の反転を主題化した。",
    background="アパルトヘイト末期南アフリカの政治危機の文学的予言。",
    development="ゴーディマー・ノーベル賞(1991)の中心作の一つ。",
    historical_context="1980年代アパルトヘイト南アフリカの非常事態期。",
    primary_source_url=WIKI_EN+"July%27s_People",
    primary_source_type="Wikipedia: July's People",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ゴーディマー『バーガーの娘』",
    name_en="Gordimer's Burger's Daughter",
    name_original="Burger's Daughter",
    period_key="独立後中期",
    definition="ゴーディマーが1979年に発表した長編。共産党活動家の娘ロザ・バーガーを通じて、白人反アパルトヘイト運動の倫理的緊張を描いた。発表後南ア政府により発禁処分。",
    background="1970年代南アフリカ共産党・ANC地下運動の現実。",
    development="ゴーディマー中期長編の頂点作。",
    historical_context="1970年代末アパルトヘイト南アフリカの抑圧期。",
    primary_source_url=WIKI_EN+"Burger%27s_Daughter",
    primary_source_type="Wikipedia: Burger's Daughter",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アンドレ・ブリンク『乾季白い季節』",
    name_en="André Brink's A Dry White Season",
    name_original="A Dry White Season",
    period_key="独立後中期",
    definition="アンドレ・ブリンク（1935-2015）が1979年に発表した長編。アパルトヘイト南アで黒人少年の死を追求する白人教師ベンを描き、ブッカー賞最終候補・南ア政府発禁処分・1989年映画化。",
    background="1976年ソウェト蜂起と白人アフリカーナーの良心的応答。",
    development="アパルトヘイト批判文学の正典作の一つ。",
    historical_context="1970年代後半南アフリカの抑圧期。",
    primary_source_url=WIKI_EN+"A_Dry_White_Season",
    primary_source_type="Wikipedia: A Dry White Season",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アソル・フガード『マスター・ハロルド…とボーイたち』",
    name_en="Athol Fugard's Master Harold...and the Boys",
    name_original="Master Harold...and the Boys",
    period_key="独立後中期",
    definition="アソル・フガード（1932-2025）が1982年に発表した戯曲。ポートエリザベスの茶店で白人少年ハリーと黒人ボーイ二人の人種的関係転換を描いた、アパルトヘイト戯曲の代表作。",
    background="フガード自身の幼少期実体験、ポートエリザベスの人種隔離茶店文化。",
    development="アパルトヘイト世界戯曲の正典化。フガード代表作の一つ。",
    historical_context="1980年代アパルトヘイト南アフリカの戯曲運動期。",
    primary_source_url=WIKI_EN+"Master_Harold...and_the_Boys",
    primary_source_type="Wikipedia: Master Harold...and the Boys",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ソル・プラーチェ『ムフディ』",
    name_en="Sol Plaatje's Mhudi",
    name_original="Mhudi",
    period_key="植民地末期",
    definition="ソル・プラーチェ（1876-1932）が1930年に発表した長編。19世紀ムジリカジ王によるバロロン族征服を、女性ムフディを語り手に描いた、南アフリカ初の英語長編小説。",
    background="プラーチェのANC（南アフリカ・ナショナル・コングレス）創立(1912)の活動と歴史小説的応答。",
    development="南アフリカ黒人英語文学の出発点。",
    historical_context="1920年代南アフリカの黒人土地法・人種立法期。",
    primary_source_url=WIKI_EN+"Mhudi",
    primary_source_type="Wikipedia: Mhudi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ソル・プラーチェ『先住民の生活』",
    name_en="Plaatje's Native Life in South Africa",
    name_original="Native Life in South Africa",
    period_key="植民地末期",
    definition="プラーチェが1916年に発表したルポルタージュ。1913年南アフリカ黒人土地法による強制移住の実態を記録し、20世紀初頭南アフリカ黒人ジャーナリズムの正典化。",
    background="1913年南アフリカ黒人土地法の強制移住の現実。",
    development="20世紀南アフリカ黒人歴史記述の正典化作。",
    historical_context="1910年代南アフリカ連邦成立期の黒人立法。",
    primary_source_url=WIKI_EN+"Native_Life_in_South_Africa",
    primary_source_type="Wikipedia: Native Life",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"南アフリカ強制移住",
         "description":"プラーチェのルポルタージュは南アフリカ社会人類学（モニカ・ウィルソン等）と並行する。"}])


# D. Lusophone (Mia Couto/Pepetela/Agualusa/Honwana/Khosa) (5)
add(**C, name_ja="ミア・コウト『夢遊する大地』",
    name_en="Mia Couto's Terra Sonâmbula",
    name_original="Terra Sonâmbula",
    period_key="葡語圏アフリカ独立後",
    definition="ミア・コウト（1955-）が1992年に発表した長編。モザンビーク内戦下、少年ムイディンガと老人トゥアハイルの放浪を、ポルトガル語の創造的変形で描いた葡語圏アフリカ・マジック・リアリズムの代表作。",
    background="モザンビーク内戦(1977-92)の文学的応答とコウトの言語的変形実践。",
    development="葡語圏アフリカ文学の世界文学化の中心作。コウト・カモンイス賞(2013)の代表作。",
    historical_context="モザンビーク内戦終結直後期。",
    primary_source_url=WIKI_PT+"Terra_Son%C3%A2mbula",
    primary_source_type="Wikipedia PT: Terra Sonâmbula",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"コウトのポルトガル語の創造的変形は、AI時代の言語生成における創造的逸脱の祖型。",
         "related_ai_phenomenon":"AI言語生成における創造的逸脱"}])

add(**C, name_ja="ペペテーラ『ヤカ』",
    name_en="Pepetela's Yaka",
    name_original="Yaka",
    period_key="葡語圏アフリカ独立後",
    definition="ペペテーラ（1941-）が1984年に発表した長編。アンゴラ南部ベンゲラ家系を1890年代から1975年独立まで4世代にわたって描き、葡語圏アフリカ歴史小説の代表作。",
    background="アンゴラ独立(1975)後の歴史的記憶政治と、ペペテーラのMPLA系列活動。",
    development="ペペテーラ・カモンイス賞(1997)の中心作の一つ。",
    historical_context="1980年代アンゴラ独立後の歴史的構築期。",
    primary_source_url=WIKI_PT+"Pepetela",
    primary_source_type="Wikipedia PT: Pepetela",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アグアルーザ『過去の売人』",
    name_en="Agualusa's O Vendedor de Passados",
    name_original="O Vendedor de Passados",
    period_key="21世紀アフリカ文学",
    definition="ジョゼ・エドゥアルド・アグアルーザ（1960-）が2004年に発表した長編。アンゴラの過去の売人ヴェントゥラを、ペットのヤモリの視点で語る独自の語りを展開した。2007年Independent Foreign Fiction Prize受賞。",
    background="アンゴラ内戦終結(2002)後の歴史的記憶構築の問題化。",
    development="アグアルーザ世界文学的躍進の中心作。",
    historical_context="2000年代アンゴラ内戦後復興期。",
    primary_source_url=WIKI_PT+"O_Vendedor_de_Passados",
    primary_source_type="Wikipedia PT: O Vendedor de Passados",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ホンワナ『私たちは犬を殺した』",
    name_en="Honwana's Nós Matámos o Cão-Tinhoso",
    name_original="Nós Matámos o Cão-Tinhoso",
    period_key="植民地末期",
    definition="ルイス・ベルナルド・ホンワナ（1942-2017）が1964年に発表した短編集。植民地モザンビークの少年たちの体験を通じて植民地暴力を描いた、葡語圏アフリカ短編文学の正典化作。",
    background="ホンワナ自身のFRELIMO政治活動と、葡領モザンビーク独立闘争期。",
    development="葡語圏アフリカ短編文学の正典化。",
    historical_context="1960年代葡領モザンビーク独立闘争期。",
    primary_source_url=WIKI_PT+"Lu%C3%ADs_Bernardo_Honwana",
    primary_source_type="Wikipedia PT: Honwana",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ウンガラニ・バ・カ・コーサ『ウアラピ』",
    name_en="Ungulani Ba Ka Khosa's Ualalapi",
    name_original="Ualalapi",
    period_key="葡語圏アフリカ独立後",
    definition="ウンガラニ・バ・カ・コーサ（1957-）が1987年に発表した長編。19世紀末ガザ帝国の最後の王ンゴングニャネを多視点的物語形式で描き、モザンビーク歴史小説の正典化。",
    background="独立後モザンビーク（FRELIMO政府下）の歴史的記憶政治。",
    development="モザンビーク現代文学の正典化作の一つ。",
    historical_context="1980年代モザンビーク内戦下の歴史小説的応答。",
    primary_source_url=WIKI_PT+"Ungulani_Ba_Ka_Khosa",
    primary_source_type="Wikipedia PT: Ungulani Ba Ka Khosa",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# E. Maghreb (Chraibi/Khair-Eddine/Djaout/Khadra/Dib) (5)
add(**C, name_ja="ドリス・シュライービ『単純な過去』",
    name_en="Driss Chraibi's Le Passé simple",
    name_original="Le Passé simple",
    period_key="マグレブ近代",
    definition="ドリス・シュライービ（1926-2007）が1954年に発表した長編。モロッコ・カサブランカの少年ドリスを語り手に、父権・植民地・宗教の三重圧迫を描いた、マグレブ仏語文学の出発点。",
    background="仏領モロッコの父権制とカサブランカ近代化の緊張。",
    development="マグレブ仏語小説の正典化の起点。",
    historical_context="1950年代モロッコ独立直前期。",
    primary_source_url=WIKI_FR+"Le_Pass%C3%A9_simple",
    primary_source_type="Wikipedia FR: Le Passé simple",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="ターハル・ジャウト『骨の探索者たち』",
    name_en="Tahar Djaout's Les Chercheurs d'os",
    name_original="Les Chercheurs d'os",
    period_key="マグレブ近代",
    definition="ターハル・ジャウト（1954-1993）が1984年に発表した長編。アルジェリア独立戦争で死亡した兄の骨を探す少年の旅を描き、マグレブ独立後文学の代表作。1993年ジャウトはイスラーム原理主義者により暗殺。",
    background="アルジェリア独立戦争(1954-62)の記憶と独立後アルジェリアの記憶政治。",
    development="ジャウト暗殺(1993)はマグレブ知識人の文学的殉教の象徴となった。",
    historical_context="1980年代アルジェリアの独立後記憶構築期。",
    primary_source_url=WIKI_FR+"Tahar_Djaout",
    primary_source_type="Wikipedia FR: Tahar Djaout",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ヤスミナ・カドラ『カブールの燕たち』",
    name_en="Yasmina Khadra's Les Hirondelles de Kaboul",
    name_original="Les Hirondelles de Kaboul",
    period_key="21世紀アフリカ文学",
    definition="ヤスミナ・カドラ（モハメッド・ムレッセウル、1955-）が2002年に発表した長編。タリバーン支配下カブールの2組の夫婦の運命を描き、マグレブ・中東連環文学の代表作。",
    background="アルジェリア出身軍人作家カドラの中東イスラーム圏への文学的拡張。",
    development="カドラ「中東三部作」の起点となり、世界文学的躍進。",
    historical_context="2001年アフガニスタン戦争前後期。",
    primary_source_url=WIKI_FR+"Les_Hirondelles_de_Kaboul",
    primary_source_type="Wikipedia FR: Les Hirondelles de Kaboul",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="モハメッド・ディブ『アルジェ大邸宅三部作』",
    name_en="Mohammed Dib's Algeria Trilogy",
    name_original="La Grande Maison / L'Incendie / Le Métier à tisser",
    period_key="マグレブ近代",
    definition="モハメッド・ディブ（1920-2003）が1952-57年に発表した三部作『大邸宅』『火事』『機織り』。植民地アルジェリアのトレムセン少年オマールを通じて植民地下マグレブ社会を描いた、マグレブ仏語文学の正典化作。",
    background="仏領アルジェリアのトレムセン市の植民地社会的現実。",
    development="ディブはマグレブ仏語文学の最重要作家の一人として国際的に評価された。",
    historical_context="1950年代仏領アルジェリア末期。",
    primary_source_url=WIKI_FR+"Mohammed_Dib",
    primary_source_type="Wikipedia FR: Mohammed Dib",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アルベール・メミ『塩の像』",
    name_en="Albert Memmi's La Statue de sel",
    name_original="La Statue de sel",
    period_key="植民地末期",
    definition="アルベール・メミ（1920-2020）が1953年に発表した自伝的長編。チュニジアのユダヤ系少年アレクサンドル・モルデカイ・ベニルーシュを通じて、植民地下マグレブ・ユダヤ人の三重周縁性を描いた。",
    background="メミ自身のチュニジア・ユダヤ系の家族環境。",
    development="メミ後の理論書『被植民者の肖像』(1957)へ発展。",
    historical_context="1950年代仏領チュニジアのユダヤ人共同体期。",
    primary_source_url=WIKI_FR+"La_Statue_de_sel",
    primary_source_type="Wikipedia FR: La Statue de sel",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# F. Egypt-Sudan (Mahfouz further/Idris/Salih/Bahaa Taher) (5)
add(**CAR, name_ja="マフフーズ『ゲベラーウィの子供たち』",
    name_en="Mahfouz's Children of Gebelawi",
    name_original="أولاد حارتنا",
    period_key="エジプト・スーダン近現代",
    definition="ナギーブ・マフフーズ（1911-2006）が1959年に新聞連載した長編。カイロの架空ハーラ（地区）を舞台に、アダム・モーセ・キリスト・ムハンマドを寓喩化した宗教史寓話で、長らくエジプトで発禁となった。",
    background="マフフーズの宗教的アレゴリーへの転換期、1959年新聞連載。",
    development="マフフーズへの暗殺未遂(1994)の直接的契機となった作品。",
    historical_context="1950年代末ナセル期エジプトの宗教・政治緊張。",
    primary_source_url=WIKI_AR+"%D8%A3%D9%88%D9%84%D8%A7%D8%AF_%D8%AD%D8%A7%D8%B1%D8%AA%D9%86%D8%A7",
    primary_source_type="Wikipedia AR: Awlad Haritna",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"イスラーム宗教寓喩",
         "description":"マフフーズの宗教史寓話は20世紀イスラーム思想の文学的応答の中心作。"}])

add(**CAR, name_ja="マフフーズ『泥棒と犬』",
    name_en="Mahfouz's The Thief and the Dogs",
    name_original="اللص والكلاب",
    period_key="エジプト・スーダン近現代",
    definition="マフフーズが1961年に発表した長編。ナセル期エジプトの元囚人サイード・マハランの復讐を、独白技法で描いた、マフフーズ・モダニズム転換期の代表作。",
    background="ナセル期エジプトの政治的幻滅と、マフフーズのジョイス的内的独白技法の導入。",
    development="マフフーズ第二期の起点となり、現代アラビア語小説の正典化。",
    historical_context="1960年代ナセル期エジプトの政治社会的緊張。",
    primary_source_url=WIKI_AR+"%D8%A7%D9%84%D9%84%D8%B5_%D9%88%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8",
    primary_source_type="Wikipedia AR: Al-Liss wa al-Kilab",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CAR, name_ja="ユースフ・イドリース『最も安価な夜』",
    name_en="Yusuf Idris's The Cheapest Nights",
    name_original="أرخص ليالي",
    period_key="エジプト・スーダン近現代",
    definition="ユースフ・イドリース（1927-1991）が1954年に発表した処女短編集。エジプト農村・都市下層民の日常を口語アラビア語混入の散文で描き、現代アラビア語短編文学の正典化作。",
    background="イドリース医師としての農村医療経験と、エジプト共産党系の政治的傾倒。",
    development="現代エジプト短編文学・口語的散文の正典化。",
    historical_context="ナセル革命直後のエジプト農村変動期。",
    primary_source_url=WIKI_AR+"%D9%8A%D9%88%D8%B3%D9%81_%D8%A5%D8%AF%D8%B1%D9%8A%D8%B3",
    primary_source_type="Wikipedia AR: Yusuf Idris",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CAR, name_ja="タイイブ・サーリフ『ザインの結婚』",
    name_en="Tayeb Salih's The Wedding of Zein",
    name_original="عرس الزين",
    period_key="独立後初期",
    definition="タイイブ・サーリフ（1929-2009）が1969年に発表した中編。スーダン・北部ナイル流域の村でユーモラスな道化ザインの結婚を描いた、現代アラビア語スーダン文学の正典化作。",
    background="独立後スーダン北部の村落社会変動期と、サーリフのBBCアラビア語放送経験。",
    development="サーリフは『北の地への移住の季節』(1966)と並ぶ二大作品の一つ。",
    historical_context="1960年代独立後スーダン北部の村落変動期。",
    primary_source_url=WIKI_AR+"%D8%A7%D9%84%D8%B7%D9%8A%D8%A8_%D8%B5%D8%A7%D9%84%D8%AD",
    primary_source_type="Wikipedia AR: Tayeb Salih",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**CAR, name_ja="バハー・ターヒル『日没のオアシス』",
    name_en="Bahaa Taher's Sunset Oasis",
    name_original="واحة الغروب",
    period_key="21世紀アフリカ文学",
    definition="バハー・ターヒル（1935-2022）が2007年に発表した長編。19世紀末英国植民地下シーワオアシス警官マフムードを通じて植民地と古代記憶の交差を描き、2008年アラビック・ブッカー賞受賞。",
    background="エジプト古代史と19世紀英国植民地遭遇の歴史小説的探求。",
    development="ターヒル晩年の代表作。アラブ世界文学の世界文学化の象徴作。",
    historical_context="2000年代エジプトのオリエンタリズム的記憶政治。",
    primary_source_url=WIKI_AR+"%D8%A8%D9%87%D8%A7%D8%A1_%D8%B7%D8%A7%D9%87%D8%B1",
    primary_source_type="Wikipedia AR: Bahaa Taher",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# G. Women's writing 補完 (Sow Fall/Beyala/Dangarembga/Bulawayo/Adichie) (5)
add(**C, name_ja="アミナタ・ソウ・ファル『乞食のストライキ』",
    name_en="Aminata Sow Fall's La Grève des Bàttu",
    name_original="La Grève des Bàttu",
    period_key="独立後初期",
    definition="アミナタ・ソウ・ファル（1941-）が1979年に発表した長編。ダカールの乞食たちが街から追放される事態に対するストライキを描き、新興仏語圏アフリカ女性作家の代表作。",
    background="1970年代セネガル都市政策と乞食差別の現実。",
    development="ソウ・ファルは仏語圏アフリカ女性作家の先駆者として国際的に評価された。",
    historical_context="1970年代セネガル都市変動期。",
    primary_source_url=WIKI_FR+"Aminata_Sow_Fall",
    primary_source_type="Wikipedia FR: Aminata Sow Fall",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="カリクスト・ベヤラ『太陽が私を焼いた』",
    name_en="Calixthe Beyala's C'est le soleil qui m'a brûlée",
    name_original="C'est le soleil qui m'a brûlée",
    period_key="独立後中期",
    definition="カリクスト・ベヤラ（1961-）が1987年に発表した処女作。カメルーン都市スラム女性の身体と性を率直に描き、仏語圏アフリカ女性文学のフェミニズム的転換を示した。",
    background="ベヤラ自身のドゥアラ・パリ間の二重生活と、第三世代仏語圏アフリカ女性作家の出発点。",
    development="ベヤラ後の長編連作の起点。",
    historical_context="1980年代仏語圏アフリカ女性作家運動期。",
    primary_source_url=WIKI_FR+"Calixthe_Beyala",
    primary_source_type="Wikipedia FR: Calixthe Beyala",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ダンガレンガ『恐怖の状態』",
    name_en="Dangarembga's Nervous Conditions",
    name_original="Nervous Conditions",
    period_key="独立後中期",
    definition="ツィツィ・ダンガレンガ（1959-）が1988年に発表した長編。植民地末期ローデシアのショナ族少女タンブを語り手に、教育・植民地・ジェンダーの交差を描いた、ジンバブエ女性文学の出発点。",
    background="ファノン『地に呪われたる者』への直接的応答（題名はファノンから）。",
    development="ダンガレンガ三部作（『The Book of Not』『This Mournable Body』）の起点。",
    historical_context="1980年代独立後ジンバブエの記憶政治。",
    primary_source_url=WIKI_EN+"Nervous_Conditions",
    primary_source_type="Wikipedia: Nervous Conditions",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"ダンガレンガの「神経症的条件」は脱植民地化主体形成の祖型。AI時代の主体形成と並行。",
         "related_ai_phenomenon":"AI時代の主体形成の脆弱性"}])

add(**C, name_ja="ノヴァイオレット・ブラワヨ『新しい名前は要らない』",
    name_en="NoViolet Bulawayo's We Need New Names",
    name_original="We Need New Names",
    period_key="21世紀アフリカ文学",
    definition="ノヴァイオレット・ブラワヨ（1981-）が2013年に発表した処女作。ジンバブエ少女ダーリングを語り手に、ジンバブエ・米国移住経験を描き、2013年ブッカー賞最終候補。",
    background="2000年代ジンバブエ経済危機(ハイパーインフレ)とブラワヨ自身の米国移住。",
    development="新世代アフリカ・ディアスポラ女性作家の代表作。",
    historical_context="2010年代アフリカ・ディアスポラ文学の世界文学化。",
    primary_source_url=WIKI_EN+"We_Need_New_Names",
    primary_source_type="Wikipedia: We Need New Names",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アディーチェ『半分のぼった黄色い太陽』",
    name_en="Adichie's Half of a Yellow Sun",
    name_original="Half of a Yellow Sun",
    period_key="21世紀アフリカ文学",
    definition="チママンダ・ンゴズィ・アディーチェ（1977-）が2006年に発表した長編。ビアフラ戦争(1967-70)を3人の視点で描き、2007年オレンジ賞受賞、世界アフリカ文学の世界文学化の象徴作。",
    background="アディーチェ祖父母のビアフラ戦争体験と、ナイジェリア戦争記憶の文学化。",
    development="アディーチェ世界文学的躍進の中心作。",
    historical_context="2000年代ナイジェリア・ビアフラ戦争記憶政治期。",
    primary_source_url=WIKI_EN+"Half_of_a_Yellow_Sun",
    primary_source_type="Wikipedia: Half of a Yellow Sun",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"アディーチェのSingle Story批判は、AI生成における代表性・多様性の理論的祖型。",
         "related_ai_phenomenon":"AI生成における代表性バイアス"}])


# H. 21世紀小説 (Mengiste/Habila/Cole/Selasi/Mengestu/Sarr) (4)
add(**C, name_ja="メンゲステ『影の王』",
    name_en="Maaza Mengiste's The Shadow King",
    name_original="The Shadow King",
    period_key="21世紀アフリカ文学",
    definition="マーザ・メンゲステ（1971-）が2019年に発表した長編。1935年伊エチオピア戦争で戦った女性兵士ヒルートを主人公に、エチオピア女性史を再構築し、2020年ブッカー賞最終候補。",
    background="エチオピア女性兵士の歴史的不可視化への文学的応答。",
    development="2010年代アフリカ・ディアスポラ歴史小説の代表作。",
    historical_context="2010年代エチオピア戦争記憶政治期。",
    primary_source_url=WIKI_EN+"The_Shadow_King",
    primary_source_type="Wikipedia: The Shadow King",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="テジュ・コール『オープン・シティ』",
    name_en="Teju Cole's Open City",
    name_original="Open City",
    period_key="21世紀アフリカ文学",
    definition="テジュ・コール（1975-）が2011年に発表した長編。マンハッタンを徘徊するナイジェリア系米国人精神科医ジュリウスを語り手に、世界都市の脱植民地的記憶を描き、PEN/ヘミングウェイ賞受賞。",
    background="2010年代アフリカ・ディアスポラ作家の世界都市文学化。",
    development="ゼーバルト的散歩・記憶散文をアフリカ・ディアスポラ的に応用した代表作。",
    historical_context="2010年代世界都市文学のポストコロニアル転換期。",
    primary_source_url=WIKI_EN+"Open_City_(novel)",
    primary_source_type="Wikipedia: Open City",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="セラシ『ガーナは行かねばならない』",
    name_en="Taiye Selasi's Ghana Must Go",
    name_original="Ghana Must Go",
    period_key="21世紀アフリカ文学",
    definition="タイイェ・セラシ（1979-）が2013年に発表した処女作。ガーナ・ナイジェリア系米国人医師家族の崩壊を描き、セラシ「アフロポリタン」概念の文学的具体化として国際的に注目された。",
    background="セラシ自身の「アフロポリタン」エッセイ(2005)とアフリカ・ディアスポラの世代交代。",
    development="新世代アフリカ・ディアスポラ文学の代表作。",
    historical_context="2010年代アフロポリタン文化現象期。",
    primary_source_url=WIKI_EN+"Taiye_Selasi",
    primary_source_type="Wikipedia: Taiye Selasi",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ムブガル・サール『最も秘密の人類記憶』",
    name_en="Mbougar Sarr's La Plus Secrète Mémoire des hommes",
    name_original="La Plus Secrète Mémoire des hommes",
    period_key="21世紀アフリカ文学",
    definition="モハメド・ムブガル・サール（1990-）が2021年に発表した長編。架空のセネガル人作家エリマンの謎を追う若手作家を語り手に、世界文学の植民地的構造を脱構築し、2021年ゴンクール賞受賞（サブサハラ初）。",
    background="ヤンボ・ウオロゲム『暴力の義務』(1968)スキャンダルへの文学的応答。",
    development="サブサハラ仏語圏作家初のゴンクール賞受賞。世界文学制度の脱植民地化の象徴作。",
    historical_context="2020年代世界文学賞制度の脱植民地化期。",
    primary_source_url=WIKI_FR+"La_Plus_Secr%C3%A8te_M%C3%A9moire_des_hommes",
    primary_source_type="Wikipedia FR: Mbougar Sarr",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"サールのメタ文学的な「失われた作家」探求は、AI時代の作者性・記憶構造への祖型。",
         "related_ai_phenomenon":"AI時代の作者性・テクスト記憶"}])


# I. 詩・批評 (Awoonor/Brutus/Serote/Mbembe/Mudimbe/Quayson) (4)
add(**C, name_ja="アウォーノル『海と時間』",
    name_en="Kofi Awoonor's Until the Morning After",
    name_original="Until the Morning After",
    period_key="独立後中期",
    definition="コフィ・アウォーノル（1935-2013）の詩集（1987）。エウェ族口承詩「ハロ」を英語詩に変形し、ガーナ・アフリカ詩の正典化に決定的役割を果たした。2013年ナイロビ・ウェストゲート襲撃で死亡。",
    background="アウォーノルのエウェ族グリオ伝統との生涯にわたる対話。",
    development="アフリカ英語詩の正典化作の一つ。",
    historical_context="1980年代ガーナ詩運動期。",
    primary_source_url=WIKI_EN+"Kofi_Awoonor",
    primary_source_type="Wikipedia: Kofi Awoonor",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")

add(**C, name_ja="ブルートゥス『マーサへの手紙』",
    name_en="Dennis Brutus's Letters to Martha",
    name_original="Letters to Martha",
    period_key="独立後初期",
    definition="デニス・ブルートゥス（1924-2009）が1968年に発表した詩集。ロベン島刑務所からの「手紙」形式の詩で、アパルトヘイト囚人体験を国際的に文学化した。",
    background="ブルートゥス自身のロベン島収監体験(1963-65)と国際スポーツ・ボイコット運動。",
    development="アパルトヘイト国際抗議文学の中心作。",
    historical_context="1960年代アパルトヘイト南アの抑圧期。",
    primary_source_url=WIKI_EN+"Dennis_Brutus",
    primary_source_type="Wikipedia: Dennis Brutus",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="モンガネ・セローテ『ヤカルインコモ』",
    name_en="Mongane Wally Serote's Yakhal'inkomo",
    name_original="Yakhal'inkomo",
    period_key="独立後初期",
    definition="モンガネ・ワリー・セローテ（1944-）が1972年に発表した詩集。タウンシップ詩運動「ブラック・コンシャスネス」期の代表作で、ズールー語題（「牛が泣く」）にアパルトヘイト下黒人の声を結晶化した。",
    background="ブラック・コンシャスネス運動(1968-77)の文学的中核。",
    development="セローテ後の長編・詩集の起点。",
    historical_context="1970年代アパルトヘイト南ア・ブラック・コンシャスネス期。",
    primary_source_url=WIKI_EN+"Mongane_Wally_Serote",
    primary_source_type="Wikipedia: Mongane Wally Serote",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ムベンベ『黒人理性批判』",
    name_en="Mbembe's Critique of Black Reason",
    name_original="Critique de la raison nègre",
    period_key="21世紀アフリカ文学",
    definition="アシール・ムベンベが2013年に発表した著作。「黒人」概念がいかに資本主義近代の構築物として歴史的に作られたかを分析し、ファノン以後最大規模の脱植民地化哲学書として国際評価を得た。",
    background="2010年代世界資本主義におけるレイシャル・キャピタリズムの理論的問題化。",
    development="ムベンベ『野蛮主義』(2020)へ展開し、世界脱植民地化思想の中心源流。",
    historical_context="2010年代Black Lives Matter運動期。",
    primary_source_url=WIKI_FR+"Achille_Mbembe",
    primary_source_type="Wikipedia FR: Mbembe",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ムベンベの黒人理性批判は、AI時代の人種化された主体・知識生産への根本批判の祖型。",
         "related_ai_phenomenon":"AI生成における人種的バイアス"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"レイシャル・キャピタリズム",
         "description":"ムベンベはセドリック・ロビンソン以降のレイシャル・キャピタリズム理論の中心源流。"}])


# Main runner
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region=REGION,
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            entry.setdefault("original_script", "roman")
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
        print(f"[wave17_c24] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave17_c24] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
        print(f"[wave17_c24] CONCEPTS defined in this script: {len(CONCEPTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
