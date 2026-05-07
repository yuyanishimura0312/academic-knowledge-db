"""LIT-DB Phase 2 Wave 20 — C16: Japanese Classical Literature ADD 80.

Subfield: lit_jp_classical (id=10), region='東アジア'.
Existing periods (reused): 上代/中古/中世/近世.
Adds 80 NEW concepts NON-overlapping with the 223 existing entries.

Coverage focuses on:
  A: 万葉集深掘り (10) — 大伴旅人讃酒歌, 山上憶良貧窮問答歌詳細解読,
                         有間皇子辞世二首詳細, 元正天皇御製, 持統天皇御製,
                         弓削皇子御製, 軽皇子御製, 中臣宅守-狭野茅上娘子贈答,
                         大伴坂上郎女歌群, 大伴池主家持書簡歌
  B: 古今集分類詳細 (12) — 古今集春上下/夏/秋上下/冬, 賀歌, 離別歌, 羈旅歌,
                            物名, 哀傷, 雑下, 雑体, 大歌所御歌
  C: 古今集制度・論争 (5) — 真名序仮名序対照論, 紀貫之古今集編纂論争,
                              六歌仙評価, 屏風歌制度, 歌合制度の正典化
  D: 私家集追補 (4) — 古今和歌六帖, 凡河内躬恒集, 紀友則集, 壬生忠岑集
  E: 平安和歌歌人 (8) — 伊勢, 中務, 小大君, 赤染衛門, 伊勢大輔, 相模,
                         源頼政歌集, 紀友則歌風
  F: 伊勢物語段別 (5) — 伊勢物語1段「初冠」, 9段「東下り」, 23段「筒井筒」,
                          69段「狩の使」, 82段「渚の院」
  G: 中古散文詳細 (4) — 大和物語段別, 平中物語細目, 多武峰少将物語, 篁物語
  H: 源氏物語帖選抜 (8) — 桐壺巻, 若紫巻, 葵巻, 須磨巻, 明石巻, 玉鬘十帖,
                            若菜上下, 宇治十帖橋姫巻
  I: 中世詩歌歌人 (8) — 後鳥羽院, 式子内親王, 藤原家隆, 九条良経, 寂蓮,
                          京極為兼, 伏見院, 永福門院
  J: 中世論評・連歌 (6) — 慈円愚管抄, 一条兼良花鳥余情, 正徹物語,
                            心敬老葉, 心敬老のすさみ, 二条良基応安新式
  K: 中世物語・説話 (4) — 源平盛衰記補, 今昔物語集天竺震旦, 沙石集無住道暁,
                            十二類絵巻
  L: 軍記諸本 (3) — 太平記古態本西源院本, 義経記諸本, 曾我物語真名仮名
  M: 近世補完 (3) — 芭蕉野ざらし紀行, 芭蕉笈の小文, 蕪村七部集
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


NIJL = "https://kokusho.nijl.ac.jp/"
NDL = "https://dl.ndl.go.jp/"
AOZORA = "https://www.aozora.gr.jp/"
JSTAGE = "https://www.jstage.jst.go.jp/"
JTI = "https://jti.lib.virginia.edu/"
WASEDA = "https://www.wul.waseda.ac.jp/kotenseki/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


C = dict(subfield_code="lit_jp_classical", region="東アジア",
         original_script="kanji_kana")


# ============================================================
# A: 万葉集深掘り (10) — period: 上代
# ============================================================
add(**C, name_ja="大伴旅人讃酒歌十三首",
    name_en="Otomo no Tabito: Thirteen Poems Praising Sake",
    name_original="讃酒歌十三首",
    period_key="上代",
    definition="大伴旅人(665-731)が大宰帥時代に詠んだ巻三338-350の十三首連作。「験なき物を思はずは一坏の濁れる酒を飲むべくあるらし」等、酒讃美を通じ老荘的隠逸思想と憂愁を表現。万葉集における中国文学受容と知識人的諧謔の頂点を成す。",
    background="天平初期大宰府文学圏での老荘思想受容。",
    development="近世以降、漢文学受容と日本的諧謔の融合事例として再評価された。",
    historical_context="天平2-3年(730-731)の大宰府筑紫歌壇期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三338-350",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"旅人讃酒歌は漢籍引用と個人的憂愁が融合した知識人主体の表明で、AI時代の他文化テキスト引用と作者性の問題を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI時代の引用と作者性"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"老荘的隠逸思想",
         "description":"旅人讃酒歌は東アジア老荘思想を日本的詩歌形式に翻訳した古代事例として哲学史と文学史を架橋する。"}])

add(**C, name_ja="山上憶良「貧窮問答歌」精読",
    name_en="Yamanoue no Okura: Detailed Reading of Hinkyu Mondoka",
    name_original="貧窮問答歌精読",
    period_key="上代",
    definition="山上憶良(660頃-733頃)の長歌「風雑り雨降る夜の…」(巻五892-893)とその反歌の精読。問答体形式で貧者と更貧者の対話を構成し、律令制下農民窮乏を批判的に描く。万葉集における社会批評詩の極致で、儒教的民生思想と仏教的悲哀観を融合した特異作。",
    background="天平4年(732)頃筑前守時代の社会観察と漢籍儒仏混淆。",
    development="近代以降、社会派文学・プロレタリア文学の祖型として再評価された。",
    historical_context="天平初期の律令制疲弊期農民実態。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻五892-893",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"invariant",
         "rationale":"貧窮問答歌の問答体貧者主体化は周縁的声の文学化の古代事例で、AI時代の声なき主体の代弁倫理を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における周縁的主体の代弁"}])

add(**C, name_ja="有間皇子辞世二首",
    name_en="Prince Arima: Two Death Verses",
    name_original="有間皇子辞世二首",
    period_key="上代",
    definition="有間皇子(640-658)が斉明4年(658)11月謀反の罪で藤白坂で絞殺される直前に詠んだ巻二141-142の二首「磐代の浜松が枝を引き結びま幸くあらばまた帰り見む」「家にあれば笥に盛る飯を草枕旅にしあれば椎の葉に盛る」。日本辞世文学の最古層を成し、大津皇子辞世歌と並ぶ皇族辞世詩の祖型。",
    background="斉明朝の蘇我赤兄謀略による有間皇子排斥。",
    development="近世以降、辞世和歌の祖型として武家辞世文学に継承された。",
    historical_context="斉明4年(658)の宮廷政争。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻二141-142",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"invariant",
         "rationale":"有間皇子辞世二首は処刑直前の死者主体の声を文学化した最古例で、AI時代の生成主体と死をめぐる声の問題を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI生成における死者主体表現"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"日本辞世詩の死生観",
         "description":"有間辞世二首は日本辞世文学の最古層を成し、武家辞世への系譜的起点として哲学史と文学史を架橋する。"}])

add(**C, name_ja="元正天皇御製",
    name_en="Empress Gensho's Imperial Verses",
    name_original="元正天皇御製",
    period_key="上代",
    definition="元正天皇(680-748、在位715-724)の万葉集所収御製群。巻八1637等の四季雑歌や応制歌を残す。女帝として持統・元明に続く皇統儀礼歌の継承者で、奈良前期女性天皇による文学的活動の証左。律令期女帝歌の典型として位置づけられる。",
    background="奈良前期女帝政の文化的活動。",
    development="近現代女性天皇研究の文学的資料として再注目された。",
    historical_context="養老期(717-724)の女帝政。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻八1637他",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="持統天皇御製",
    name_en="Empress Jito's Imperial Verses",
    name_original="持統天皇御製",
    period_key="上代",
    definition="持統天皇(645-703、在位690-697)の万葉集所収御製群。「春過ぎて夏来たるらし白栲の衣干したり天の香具山」(巻一28)が著名。藤原京遷都期の女帝として宮廷儀礼歌の中心に位置し、人麻呂讃歌の対象でもある。萬葉集巻一巻二編年配列の中核となる女帝歌。",
    background="天武皇統継承期の女帝政と宮廷儀礼整備。",
    development="百人一首入撰により近世以降日本人最も知られる古代和歌の一つとなった。",
    historical_context="持統朝(690-697)藤原京遷都期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻一28他",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"invariant",
         "rationale":"持統天皇御製は女帝による国家儀礼歌作者性の確立で、AI時代の権威的主体による生成テキストの作者性論を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における権威主体の作者性"}],
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"古代女性権力者と文学",
         "description":"持統天皇御製は古代女性最高権力者の文学活動の祖型として、女性権力者と文芸活動の系譜研究の中核を占める。"}])

add(**C, name_ja="弓削皇子御製",
    name_en="Prince Yuge's Imperial Verses",
    name_original="弓削皇子御製",
    period_key="上代",
    definition="弓削皇子(?-699)の万葉集所収歌。天武天皇皇子で長皇子の弟。巻二111-112で額田王と贈答し、巻三242-243等で繊細な抒情を残す。「夕されば潮満ち来なむ住吉の浅鹿の浦に玉藻刈りてな」等、皇族歌人の知的洗練を示す。但馬皇女・湯原王と並ぶ天武皇統皇族歌人の一。",
    background="天武皇統皇族歌人の文化的活動。",
    development="近代以降、繊細な抒情表現の祖として再評価された。",
    historical_context="持統朝後期の皇族文化圏。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻二111-112他",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="軽皇子御製(文武天皇)",
    name_en="Prince Karu (Emperor Monmu) Imperial Verses",
    name_original="軽皇子御製",
    period_key="上代",
    definition="軽皇子（後の文武天皇、683-707）が皇太子時代に詠んだ巻一46-49の安騎野遊猟歌前後の御製と、人麻呂が随行して詠んだ長歌反歌を含む歌群。亡父草壁皇子追慕の情と王権継承の儀礼性を兼ね備え、人麻呂職業歌人の活動と皇族主体の重層構造を示す。",
    background="持統朝後期の皇太子制度確立と狩猟儀礼。",
    development="人麻呂宮廷歌人活動と皇族主体の関係を示す中核資料。",
    historical_context="持統6年(692)頃の安騎野遊猟。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻一46-49",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"軽皇子御製と人麻呂随行歌の重層は皇族主体と職業歌人代作の関係を示し、AI時代の代作・代理生成の作者性問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI代作と作者性の重層構造"}])

add(**C, name_ja="中臣宅守・狭野茅上娘子贈答",
    name_en="Nakatomi no Yakamori and Sano no Chigami exchange",
    name_original="中臣宅守・狭野茅上娘子贈答歌",
    period_key="上代",
    definition="中臣宅守と狭野茅上娘子の流配恋歌63首(巻十五3723-3785)。天平10年(738)頃宅守の越前流配時に交わされた贈答歌群で、女性側娘子の作が40首と男性側を上回る点で異例。流配と引き離しの悲哀を率直に詠む万葉相聞歌の精華で、女性主体の長期贈答歌として独自の地位を占める。",
    background="天平期律令制下流刑制度と恋愛分断。",
    development="近代以降、女性主体的恋愛詩として再評価された。",
    historical_context="天平10年(738)頃の越前流配期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十五3723-3785",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"狭野茅上娘子の長期贈答歌は女性主体の能動的恋愛表現の古代事例で、AI時代の女性主体声の文学的構築を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の女性主体表現"}])

add(**C, name_ja="大伴坂上郎女歌群",
    name_en="Otomo no Sakanoue no Iratsume: Poetic Corpus",
    name_original="大伴坂上郎女歌群",
    period_key="上代",
    definition="大伴坂上郎女(700頃-750頃)の万葉集所収約84首。大伴旅人妹で家持叔母。巻三・四・六・八・十七・十八等に長歌6首・短歌約78首を残す。万葉女性歌人として笠女郎と並ぶ多作家で、長歌作者として唯一無二の女性歌人。家族歌・宴席歌・相聞歌等多彩な詠歌領域を持つ。",
    background="奈良前期大伴氏族文学圏での女性歌人活動。",
    development="近現代万葉女性歌人研究の中核として重視された。",
    historical_context="天平初期から中期の大伴氏族文化圏。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻三-巻十八",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"古代氏族内女性的役割",
         "description":"坂上郎女は氏族内女性歌人としての役割を制度化した古代日本の事例で、人類学的氏族研究の比較対象となる。"}])

add(**C, name_ja="大伴池主・家持書簡歌",
    name_en="Otomo no Ikenushi and Yakamochi: Epistolary Verses",
    name_original="大伴池主・家持書簡歌",
    period_key="上代",
    definition="大伴池主と大伴家持が天平19-20年(747-748)越中で交わした書簡形式長歌・反歌群(巻十七3962以降)。漢文書簡と和歌を組合せた特異な形式で、和漢混淆の書簡文学の祖型を成す。万葉集における和文書簡文学・漢詩交流文化の融合例として重要。",
    background="天平期越中における大伴氏族文学交流。",
    development="後の和漢混淆書簡文学（平安以降）の祖型として位置づけられた。",
    historical_context="天平19年(747)家持越中守期の交流。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 萬葉集巻十七3962以降",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# B: 古今集分類詳細 (12) — period: 中古
# ============================================================
add(**C, name_ja="古今集春歌上下",
    name_en="Kokin Wakashu: Spring Volumes 1-2",
    name_original="古今和歌集春歌上・春歌下",
    period_key="中古",
    definition="古今集巻一春歌上・巻二春歌下の二巻134首は、立春から晩春・落花までの季節推移を詠歌で構成する。日本和歌史における四季部立の正典的起点で、後続勅撰集すべての春歌部立の祖型を成す。紀貫之・凡河内躬恒・紀友則の主導により季節進行の物語化が達成された。",
    background="延喜5年(905)頃の四季部立確立過程。",
    development="後続勅撰集二十一代集の春歌部立の祖型となった。",
    historical_context="醍醐朝期の和歌正典化期。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻一・二",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"invariant",
         "rationale":"古今集春歌部立の正典化は日本和歌における季節性正典化の起点で、AI時代の文化的時間性の継承構造を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における文化的季節性"}])

add(**C, name_ja="古今集夏歌",
    name_en="Kokin Wakashu: Summer Volume",
    name_original="古今和歌集夏歌",
    period_key="中古",
    definition="古今集巻三夏歌34首は四季部立の中で最少の巻で、初夏・五月雨・郭公・夏夜・蝉等の季節事物を主題化する。郭公（時鳥）詠歌が中核を占め、後続勅撰集における時鳥詠の正典化の起点を成す。夏部立の数的劣位は日本和歌史における四季感受の偏在を示す。",
    background="中古日本人四季感受の和歌的正典化期。",
    development="夏歌時鳥中心構成は後続勅撰集すべてに継承された。",
    historical_context="醍醐朝期の四季部立確立期。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻三",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集秋歌上下",
    name_en="Kokin Wakashu: Autumn Volumes 1-2",
    name_original="古今和歌集秋歌上・秋歌下",
    period_key="中古",
    definition="古今集巻四秋歌上・巻五秋歌下の二巻145首は四季部立中最多巻。立秋から晩秋紅葉までの季節進行を歌題化し、月・萩・女郎花・紅葉等の秋事物を体系的に配する。日本和歌における秋季偏愛の正典化の起点となり、後の二十一代集すべてに秋歌偏多が継承された。",
    background="日本人秋季偏愛感受の和歌的正典化。",
    development="二十一代集すべてに秋偏多構成が継承された。",
    historical_context="醍醐朝期の四季感受の制度化。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻四・五",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"正典","status":"invariant",
         "rationale":"古今集秋歌偏多は日本和歌の正典的構造を決定し、AI時代の和歌生成における季節偏在の文化的継承を再考する参照点となる。",
         "related_ai_phenomenon":"AI和歌生成における文化的偏在"}])

add(**C, name_ja="古今集冬歌",
    name_en="Kokin Wakashu: Winter Volume",
    name_original="古今和歌集冬歌",
    period_key="中古",
    definition="古今集巻六冬歌29首は四季部立中最少。初冬の時雨・霜・雪・歳末の年内立春までの冬季事物を歌題化する。雪詠歌が中核で、四季部立の最終位として春への循環的回帰（年内立春）で締められる構成は、和歌における時間循環の正典化を示す。",
    background="日本人冬季感受の和歌的体系化期。",
    development="冬-春循環構造は後続勅撰集に継承された。",
    historical_context="醍醐朝期四季部立確立期。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻六",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集賀歌",
    name_en="Kokin Wakashu: Volume of Felicitations",
    name_original="古今和歌集賀歌",
    period_key="中古",
    definition="古今集巻七賀歌22首は祝賀・長寿・千代万代の慶祝歌を集める。「君が代は千代に八千代に」の祖となる「わが君は千代に八千代に細石の巌となりて苔の生すまで」(343)等を含み、宮廷儀礼歌として後続勅撰集賀歌部立の祖型を成す。賀歌部の正典的祖型として機能した。",
    background="醍醐朝賀儀礼の文学的体系化。",
    development="後の祝賀和歌・国歌「君が代」原型を提供。",
    historical_context="醍醐朝賀儀礼制度。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻七",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集離別歌",
    name_en="Kokin Wakashu: Volume of Partings",
    name_original="古今和歌集離別歌",
    period_key="中古",
    definition="古今集巻八離別歌41首は別れの場の和歌を集める。地方赴任・任期終了・出家等の人事的別離を主題化し、後の勅撰集離別歌部の祖型となる。「立ち別れいなばの山の峰に生ふる松としきかば今帰り来む」(在原行平365)等が典型。日本離別文学の正典的起源。",
    background="平安宮廷人事制度と離別儀礼。",
    development="後の勅撰集離別歌部の祖型として継承された。",
    historical_context="醍醐朝の宮廷人事文化。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻八",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集羈旅歌",
    name_en="Kokin Wakashu: Volume of Travel",
    name_original="古今和歌集羈旅歌",
    period_key="中古",
    definition="古今集巻九羈旅歌16首は旅の歌を集める最少巻の一。「天の原ふりさけみれば春日なる三笠の山にいでし月かも」(阿倍仲麻呂406)等を含み、紀貫之『土佐日記』への影響をはじめ後の旅文学の祖型を成す。少数ながら日本旅文学の正典的起源として重要な部立。",
    background="平安初期人事赴任旅文化と漢詩旅情詩受容。",
    development="土佐日記等仮名旅日記の祖型を提供。",
    historical_context="醍醐朝の地方赴任制度。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻九",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集物名",
    name_en="Kokin Wakashu: Volume of Hidden Names",
    name_original="古今和歌集物名",
    period_key="中古",
    definition="古今集巻十物名47首は事物名を歌中に隠し詠み込む言語遊戯歌の集合。掛詞・折句技法を駆使し、和歌の知的言語遊戯性を制度化した部立。後の勅撰集物名・離合体・俳諧的遊戯歌の祖型となり、日本和歌における言語遊戯性正典化の起点を成す。",
    background="平安初期宮廷知的遊戯文化。",
    development="後の俳諧・川柳的言語遊戯の祖型を提供。",
    historical_context="醍醐朝宮廷遊戯文化。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻十",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"物名歌は事物名を音韻的に隠し詠む高度な言語遊戯の正典化で、AI時代の言語遊戯生成と隠喩生成を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における言語遊戯"}])

add(**C, name_ja="古今集哀傷歌",
    name_en="Kokin Wakashu: Volume of Lamentations",
    name_original="古今和歌集哀傷歌",
    period_key="中古",
    definition="古今集巻十六哀傷歌34首は死別・追悼の和歌を集める。「思ひきや別れし秋にあひ見むと心の枝も結ばざりしを」(835)等を含み、万葉挽歌から平安哀傷歌への文学的転換を象徴する部立。仏教的無常観と平安宮廷的死別感の融合により、後の哀傷和歌・追悼文学の正典化を達成した。",
    background="平安仏教的無常観と万葉挽歌伝統の融合。",
    development="後の勅撰集哀傷歌部の祖型として機能した。",
    historical_context="醍醐朝期仏教的無常観の文学化。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻十六",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集雑下",
    name_en="Kokin Wakashu: Miscellaneous Volume 2",
    name_original="古今和歌集雑下",
    period_key="中古",
    definition="古今集巻十八雑下68首は他の部立に収めきれない多様な歌を集める。在原業平・小野小町等晩年詠を含み、無常観・人生回顧的詠歌が中心。「世の中にたえて桜のなかりせば春の心はのどけからまし」(在原業平53)等が著名。古今集の事実上の総集として、雑歌雑体の正典化を行う。",
    background="醍醐朝期晩年詠文学の制度化。",
    development="後続勅撰集雑歌部の祖型として継承された。",
    historical_context="醍醐朝期人事多様性の和歌的反映。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻十八",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集雑体",
    name_en="Kokin Wakashu: Variant Forms Volume",
    name_original="古今和歌集雑体",
    period_key="中古",
    definition="古今集巻十九雑体68首は短歌以外の歌体（長歌・旋頭歌・誹諧歌）を集める。中でも誹諧歌58首は古今集中の諧謔的歌群で、滑稽・諷刺・知的遊戯の側面を持ち、後の俳諧連歌・俳句の祖型として極めて重要。短歌正典化の中での非短歌的多様性の保存装置となる。",
    background="醍醐朝期非短歌的歌体の保存装置化。",
    development="誹諧歌は近世俳諧文学の祖型として位置づけられた。",
    historical_context="醍醐朝期歌体多様性の制度的保存。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻十九",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="古今集大歌所御歌",
    name_en="Kokin Wakashu: Imperial Bureau Songs",
    name_original="古今和歌集大歌所御歌",
    period_key="中古",
    definition="古今集巻二十大歌所御歌32首は宮廷儀礼用神楽歌・東遊歌・大歌所所管歌を集める最終巻。神事芸能歌の正典化として、和歌と神事歌謡の制度的統合を実現する。神楽歌・催馬楽・風俗歌等の宮廷音楽芸能との接点を保存し、和歌の儀礼的基盤を示す重要な部立。",
    background="平安初期神祇芸能制度と和歌の統合。",
    development="後の儀礼歌・神楽歌研究の正典的資料となった。",
    historical_context="醍醐朝期神祇芸能制度。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集巻二十",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"宮廷儀礼歌謡",
         "description":"大歌所御歌は宮廷儀礼歌謡の制度的保存事例として、人類学的儀礼研究の比較対象となる。"}])


# ============================================================
# C: 古今集制度・論争 (5) — period: 中古
# ============================================================
add(**C, name_ja="古今集真名序仮名序対照論",
    name_en="Comparative Study of Kokinshu's Mana and Kana Prefaces",
    name_original="古今集真名序仮名序対照論",
    period_key="中古",
    definition="古今集に冠する紀淑望真名序（漢文）と紀貫之仮名序（仮名）の構造的対照論。両序とも六歌仙評価・六義論を共有しつつ、漢文真名序が公式性、仮名序が文学性を担う二重序文構造を確立。和漢混淆的勅撰集体制の祖型を成し、後の勅撰集序文制度の基礎を提供した。",
    background="醍醐朝期和漢二重表記体制の文学的定立。",
    development="後の勅撰集序文の和漢二重構造の祖型を提供した。",
    historical_context="延喜5年(905)古今集成立期。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集真名序・仮名序",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"真名仮名二重序は日本における二言語並列体制の祖型で、AI時代の多言語並列生成・翻訳的等価性を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI多言語並列生成"}])

add(**C, name_ja="紀貫之古今集編纂論争",
    name_en="Debate on Ki no Tsurayuki and Kokinshu Compilation",
    name_original="紀貫之古今集編纂論争",
    period_key="中古",
    definition="古今集編纂における紀貫之の主導性をめぐる近現代国文学の論争。貫之主編説（窪田空穂・佐伯梅友）に対し、紀友則・凡河内躬恒・壬生忠岑の四人共編説、貫之最終編集説等が並立。古今集の文体的均質性と作者偏在をどう説明するかに関わる中核論題。",
    background="20世紀国文学の古今集本文批判の深化。",
    development="現代古今集研究の中核論争として継続中。",
    historical_context="近現代国文学による撰集論的批判。",
    primary_source_url=JSTAGE+"article/jjcl/",
    primary_source_type="J-STAGE: 古今集編纂論",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="古今集六歌仙評価論",
    name_en="Critical Evaluation of the Six Poetic Sages in Kokinshu",
    name_original="六歌仙評価論",
    period_key="中古",
    definition="古今集仮名序が在原業平・小野小町・喜撰法師・大伴黒主・文屋康秀・僧正遍昭の六歌仙を評価する論評部分の精読。各歌人の作風と限界を批評的に提示する貫之の批評は、日本最古の体系的歌人論として後の歌論史の祖型を成す。批評対象として選ばれた六人の選定基準も論争的。",
    background="醍醐朝期歌人批評文化の制度化。",
    development="後の歌論・歌人列伝の批評的祖型を提供した。",
    historical_context="平安初期の和歌正典化期。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集仮名序六歌仙評",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"受容","status":"rethinking",
         "rationale":"六歌仙評価論は批評家貫之による先行歌人の受容的評価の祖型で、AI時代の批評的選別と作品評価の問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における批評的評価"}],
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"知識評価の制度化",
         "description":"六歌仙評価は知識権威による先行知識評価の制度化の古典事例として、知識経営論的選別研究の比較対象となる。"}])

add(**C, name_ja="屏風歌制度",
    name_en="Byobu-uta: Screen Painting Poetry Institution",
    name_original="屏風歌制度",
    period_key="中古",
    definition="平安宮廷で屏風絵に和歌を書き付ける文化制度。延喜・天暦期に紀貫之・伊勢らが多数の屏風歌を詠み、貫之集・伊勢集等の私家集の中核を成す。屏風絵の主題（四季・名所・物語場面）に応じた和歌制作という応用型詠歌の制度化により、和歌の絵画依存性と独立性の関係が問い直された。",
    background="醍醐・村上朝期屏風絵文化の興隆。",
    development="後の歌絵・絵歌・絵巻物文学の祖型を提供した。",
    historical_context="平安中期宮廷屏風文化期。",
    primary_source_url=NDL+"info:ndljp/pid/2543356",
    primary_source_type="NDL: 古今和歌集・貫之集",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"絵画詩文芸合一",
         "description":"屏風歌は絵画と詩文の複合的儀礼を制度化した平安事例で、人類学的物質文化研究の比較対象となる。"}])

add(**C, name_ja="歌合制度の正典化",
    name_en="Canonization of Utaawase Poetry Contest",
    name_original="歌合制度の正典化",
    period_key="中古",
    definition="天徳4年(960)内裏歌合を画期とする歌合制度の正典化過程。左右に分かれて各題で和歌を競い、判者が判詞で勝負を決定する儀礼制度。天徳歌合は壬生忠見「恋すてふ我が名はまだき立ちにけり…」と平兼盛の競詠が伝説化し、後の勅撰集和歌正典化の基盤的舞台となった。",
    background="村上朝期宮廷歌合文化の頂点。",
    development="後の歌合・百人一首競詠の祖型として継承された。",
    historical_context="天徳4年(960)内裏歌合。",
    primary_source_url=NDL+"info:ndljp/pid/2543359",
    primary_source_type="NDL: 天徳内裏歌合",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"歌合制度は競争的詠歌による創造性の制度化で、AI時代の競争的創作生成と評価機構を再考する参照点となる。",
         "related_ai_phenomenon":"AI競争的生成と評価"}],
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"競争的評価制度",
         "description":"歌合は知識競争評価の制度化の古典事例として、組織内競争評価論の比較対象となる。"}])


# ============================================================
# D: 私家集追補 (4) — period: 中古
# ============================================================
add(**C, name_ja="古今和歌六帖",
    name_en="Kokin Waka Rokujo: Six Volumes of Ancient and Modern Verses",
    name_original="古今和歌六帖",
    period_key="中古",
    definition="天徳元年(957)頃成立とされる類題和歌集。万葉集・古今集・後撰集等から約4500首を25部立25項516題に分類配列する平安最大規模の類題集。題詠歌制作の参考資料として広く流布し、後の歌道家における題詠基盤となった。私撰集として最大規模を誇り、平安和歌の類題的基盤を提供。",
    background="平安中期類題和歌集化の興隆。",
    development="後の題詠歌・歌道教育の基盤資料となった。",
    historical_context="天徳期類題集成期。",
    primary_source_url=NDL+"info:ndljp/pid/2543361",
    primary_source_type="NDL: 古今和歌六帖",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="凡河内躬恒集",
    name_en="Oshikochi no Mitsune Shu",
    name_original="凡河内躬恒集",
    period_key="中古",
    definition="古今集撰者凡河内躬恒(859?-925?)の私家集。古今集195首入撰の貫之に次ぐ第二位歌人で、屏風歌・歌合歌を中核とする私家集を残す。「心あてに折らばや折らむ初霜の置きまどはせる白菊の花」(古今277)等の繊細な観察的詠歌で著名。古今集第二位歌人の私家集として古今集編纂研究の中核資料。",
    background="醍醐朝古今集撰者集団の文学活動。",
    development="後の古今集第二位歌人研究の基盤資料となった。",
    historical_context="延喜期古今集編纂期。",
    primary_source_url=NDL+"info:ndljp/pid/2543362",
    primary_source_type="NDL: 凡河内躬恒集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="紀友則集",
    name_en="Ki no Tomonori Shu",
    name_original="紀友則集",
    period_key="中古",
    definition="古今集撰者紀友則(?-905?)の私家集。古今集編纂中に没したとされ、貫之と並ぶ撰者四人の中核。「久方の光のどけき春の日にしづ心なく花の散るらむ」(古今84)等百人一首入撰歌で知られる。古今集編纂期最初期の死去により撰者活動の不完全性が論争点となる。",
    background="古今集撰者集団の世代交代期。",
    development="貫之に先立つ撰者として古今集編纂史の中核位置を占める。",
    historical_context="延喜初期撰集編纂期。",
    primary_source_url=NDL+"info:ndljp/pid/2543363",
    primary_source_type="NDL: 紀友則集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="壬生忠岑集",
    name_en="Mibu no Tadamine Shu",
    name_original="壬生忠岑集",
    period_key="中古",
    definition="古今集撰者壬生忠岑(860?-920?)の私家集。古今集撰者四人中の最後の一人で、『和歌体十種』(945年頃)の作者として最初の体系的歌論書を著した。「有明のつれなく見えし別れより暁ばかり憂きものはなし」(古今625)等百人一首入撰歌で知られ、歌論書著作により古今集撰者中最初の理論的歌人。",
    background="醍醐朝撰者集団の歌論的活動。",
    development="日本最初の歌論書『和歌体十種』により後の歌論史の祖となる。",
    historical_context="延喜期歌論成立期。",
    primary_source_url=NDL+"info:ndljp/pid/2543364",
    primary_source_type="NDL: 壬生忠岑集・和歌体十種",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# E: 平安和歌歌人 (8) — period: 中古
# ============================================================
add(**C, name_ja="伊勢(歌人)",
    name_en="Lady Ise (poet)",
    name_original="伊勢",
    period_key="中古",
    definition="平安初期女性歌人伊勢(872?-938?)。宇多天皇中宮温子女房で宇多天皇皇子敦慶親王と結ばれる。古今集22首入撰、平安初期女性歌人の代表で『伊勢集』を残す。「難波潟みじかき芦のふしの間も逢はでこの世を過ぐしてよとや」(新古今1049)等が著名。屏風歌の名手として平安宮廷女性歌人の地位確立に貢献した。",
    background="宇多朝女房文学の興隆期。",
    development="後の女性歌人系譜（小町-伊勢-紫式部-和泉式部）の中核位置を占める。",
    historical_context="宇多朝期宮廷女房文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543365",
    primary_source_type="NDL: 伊勢集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"invariant",
         "rationale":"伊勢は宮廷女性歌人の地位確立を示す古代事例で、AI時代の女性主体声の文学的構築と歴史的継承を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の女性歌人主体"}],
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"平安女性知的活動",
         "description":"伊勢の女性歌人活動は平安宮廷女性知的活動の祖型として、女性才能発揮の歴史的系譜の中核を占める。"}])

add(**C, name_ja="中務(歌人)",
    name_en="Lady Nakatsukasa (poet)",
    name_original="中務",
    period_key="中古",
    definition="平安中期女性歌人中務(912?-991?)。伊勢と敦慶親王の娘で、母の歌才を継承した宮廷女性歌人。三十六歌仙の一人。後撰集・拾遺集等に多数入撰し、『中務集』を残す。村上朝期女性歌人の中核として、母伊勢から娘へ継承された歌道家系の祖型を成す。",
    background="村上朝期女性歌人系譜の継承。",
    development="女性歌人世襲継承の祖型を成した。",
    historical_context="村上朝期宮廷女性歌人活動期。",
    primary_source_url=NDL+"info:ndljp/pid/2543366",
    primary_source_type="NDL: 中務集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="小大君",
    name_en="Lady Kodaimon",
    name_original="小大君",
    period_key="中古",
    definition="平安中期女性歌人小大君(生没年未詳、円融朝-一条朝)。三条天皇皇后娀子内親王女房で三十六歌仙の一人。「岩橋の夜の契りも絶えぬべし明くる侘しき葛城の神」(拾遺1201)等が著名。一条朝期女房文学の主要担い手の一として、紫式部・清少納言・和泉式部らに先立つ女性歌人系譜の重要環。",
    background="円融-一条朝期女房文学の隆盛。",
    development="紫式部・清少納言らの女房文学への系譜的橋渡しを行った。",
    historical_context="円融-一条朝期女性歌人活動。",
    primary_source_url=NDL+"info:ndljp/pid/2543367",
    primary_source_type="NDL: 小大君集",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="赤染衛門",
    name_en="Akazome Emon",
    name_original="赤染衛門",
    period_key="中古",
    definition="平安中期女性歌人赤染衛門(956?-1041?)。藤原道長正室源倫子女房、夫は大江匡衡。『栄花物語』正編の作者と伝承される。「やすらはで寝なまし物を小夜更けてかたぶくまでの月を見しかな」(後拾遺680)百人一首入撰歌で著名。和泉式部と並ぶ一条朝期女性歌人で歴史物語作者としての地位も確立。",
    background="一条朝期女房文学黄金期。",
    development="女性による歴史物語編纂の祖型を成した。",
    historical_context="一条朝期道長文化圏の女性活動。",
    primary_source_url=NDL+"info:ndljp/pid/2543368",
    primary_source_type="NDL: 赤染衛門集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"平安女性知識人",
         "description":"赤染衛門は歴史物語編纂と女性歌人としての複合的活動の祖型で、女性知識人系譜の中核を占める。"}])

add(**C, name_ja="伊勢大輔",
    name_en="Ise no Taifu",
    name_original="伊勢大輔",
    period_key="中古",
    definition="平安中期女性歌人伊勢大輔(989?-1060?)。藤原彰子女房で『紫式部日記』にも登場。「いにしへの奈良の都の八重桜けふ九重に匂ひぬるかな」(詞花29)百人一首入撰歌で著名。一条朝-後一条朝の女房歌人で紫式部・和泉式部らと同時代に活躍し、平安女房文学黄金期の中核を担った。",
    background="一条朝-後一条朝期女房文学。",
    development="女房歌人系譜の中核として後世に継承された。",
    historical_context="後一条朝期彰子サロン文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543369",
    primary_source_type="NDL: 伊勢大輔集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="相模",
    name_en="Sagami (poet)",
    name_original="相模",
    period_key="中古",
    definition="平安中期女性歌人相模(998?-1061?)。脩子内親王女房で大江公資妻。後拾遺集に40首と最多入撰、『相模集』を残す。「うらみわびほさぬ袖だにあるものを恋に朽ちなむ名こそをしけれ」(後拾遺815)百人一首入撰歌で著名。後拾遺集女性筆頭歌人として平安後期女性和歌の中核位置を占める。",
    background="後一条-後冷泉朝期女性歌人活動。",
    development="後拾遺集女性筆頭として平安後期和歌史を画した。",
    historical_context="後冷泉朝期宮廷女性文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543370",
    primary_source_type="NDL: 相模集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="源頼政歌集",
    name_en="Minamoto no Yorimasa Poetry Collection",
    name_original="源頼政集",
    period_key="中古",
    definition="平安末期歌人源頼政(1104-1180)の私家集『源三位頼政集』。源平争乱期に以仁王とともに平氏打倒を企てて宇治で自刃した武将でありながら平安和歌の伝統を継承した稀有な武将歌人。千載集14首入撰。「埋もれ木の花咲くこともなかりしに身のなる果てぞ悲しかりける」辞世が著名。",
    background="平安末期源平争乱期と武将和歌伝統。",
    development="後の武将和歌（実朝以降）の祖型を提供した。",
    historical_context="治承4年(1180)宇治平等院での自刃。",
    primary_source_url=NDL+"info:ndljp/pid/2543371",
    primary_source_type="NDL: 源三位頼政集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="紀友則歌風",
    name_en="Poetic Style of Ki no Tomonori",
    name_original="紀友則歌風",
    period_key="中古",
    definition="古今集撰者紀友則(?-905?)の歌風的特質論。古今集46首入撰で撰者四人中第三位。「久方の光のどけき春の日にしづ心なく花の散るらむ」百人一首歌に代表される明朗端正な詠風で、貫之の知的洗練・躬恒の繊細・忠岑の重厚に対し友則の明朗を位置づけ、撰者四人風の体系化に貢献した。",
    background="古今集撰者四人風論の歴史的展開。",
    development="撰者四人風の比較研究は近現代国文学の中核課題となった。",
    historical_context="延喜期撰者集団内的差異論。",
    primary_source_url=JTI+"japanese/kokinshu/",
    primary_source_type="JTI: 古今和歌集紀友則歌",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# F: 伊勢物語段別 (5) — period: 中古
# ============================================================
add(**C, name_ja="伊勢物語1段「初冠」",
    name_en="Ise Monogatari Section 1: First Cap",
    name_original="伊勢物語第一段",
    period_key="中古",
    definition="伊勢物語冒頭第1段「むかし、男、初冠して…」。元服直後の男（在原業平の隠喩）が春日野で姉妹を垣間見て、「春日野の若紫のすり衣しのぶの乱れ限り知られず」を信夫摺の狩衣の裾を切り取り贈る歌物語的祖型。物語冒頭としての元服-恋情-歌贈という伊勢物語の基本構造を確立した。",
    background="平安初期歌物語形式の確立期。",
    development="後の和歌物語・恋物語冒頭の祖型を提供した。",
    historical_context="9世紀後半業平活躍期の事跡。",
    primary_source_url=JTI+"japanese/ise/",
    primary_source_type="JTI: 伊勢物語第一段",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"invariant",
         "rationale":"伊勢物語1段は元服-恋情-歌贈の物語的祖型を確立し、AI時代の物語的祖型の継承構造を再考する参照点となる。",
         "related_ai_phenomenon":"AI物語生成における祖型継承"}])

add(**C, name_ja="伊勢物語9段「東下り」",
    name_en="Ise Monogatari Section 9: Journey to the East",
    name_original="伊勢物語第九段",
    period_key="中古",
    definition="伊勢物語第9段「東下り」。男（業平）が都を捨て東国へ下る旅段。三河八橋での「かきつばた」折句歌、駿河宇津山での蔦の細道、富士山雪、武蔵野隅田川での「都鳥」歌「名にし負はばいざ言問はむ都鳥わが思ふ人はありやなしやと」を含む。日本旅文学・東国文学の正典的祖型。",
    background="9世紀後半業平東下伝承の文学化。",
    development="後の旅文学・隅田川文学・東国文学の祖型を提供した。",
    historical_context="9世紀後半業平東国行伝承。",
    primary_source_url=JTI+"japanese/ise/",
    primary_source_type="JTI: 伊勢物語第九段",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"古代日本の地理的他者性",
         "description":"伊勢物語9段東下りは都-東国の文化的他者性の文学化事例として、人類学的中心-周縁論の比較対象となる。"}])

add(**C, name_ja="伊勢物語23段「筒井筒」",
    name_en="Ise Monogatari Section 23: The Well-Curb",
    name_original="伊勢物語第二十三段",
    period_key="中古",
    definition="伊勢物語第23段「筒井筒」。幼馴染の男女が成長して結婚し、男が高安の女に通うが妻の変わらぬ愛で連れ戻される話。「筒井つの井筒にかけしまろがたけ過ぎにけらしな妹見ざる間に」「くらべこし振り分け髪も肩過ぎぬ君ならずして誰かあぐべき」の幼児期相聞歌が物語核。後の能『井筒』の典拠。",
    background="平安初期幼馴染恋愛物語の祖型化。",
    development="後の能『井筒』への翻案により謡曲化された。",
    historical_context="9世紀後半業平庶民的恋愛伝承。",
    primary_source_url=JTI+"japanese/ise/",
    primary_source_type="JTI: 伊勢物語第二十三段",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"invariant",
         "rationale":"筒井筒は幼馴染恋愛物語の祖型として日本物語史を貫き、AI時代の物語アーキタイプ継承を再考する参照点となる。",
         "related_ai_phenomenon":"AI物語生成における関係性アーキタイプ"}])

add(**C, name_ja="伊勢物語69段「狩の使」",
    name_en="Ise Monogatari Section 69: The Hunting Envoy",
    name_original="伊勢物語第六十九段",
    period_key="中古",
    definition="伊勢物語第69段「狩の使」。男が伊勢国狩使として下向し伊勢斎宮（恬子内親王）と密通する逸話。「君や来し我や行きけむおもほえず夢かうつつか寝てか覚めてか」の朝の歌が物語核。神聖な斎宮との禁忌的恋という伊勢物語の物語題名の起源で、平安宮廷恋愛の極北を示す。",
    background="平安初期斎宮制度と禁忌的恋愛伝承。",
    development="伊勢物語題名の起源として物語全体の象徴的中核となった。",
    historical_context="9世紀後半業平斎宮密通伝承。",
    primary_source_url=JTI+"japanese/ise/",
    primary_source_type="JTI: 伊勢物語第六十九段",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"狩の使段は神聖性と恋情の境界を侵犯する主体の古典事例で、AI時代の境界侵犯的物語生成と禁忌再現を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における禁忌的主題"}])

add(**C, name_ja="伊勢物語82段「渚の院」",
    name_en="Ise Monogatari Section 82: The Pavilion by the Shore",
    name_original="伊勢物語第八十二段",
    period_key="中古",
    definition="伊勢物語第82段「渚の院」。惟喬親王が交野で遊宴し業平・在原行平らと桜を詠む段。「世の中にたえて桜のなかりせば春の心はのどけからまし」(53)が中核歌。皇族と廷臣の遊宴と桜詠の正典的祖型を提供し、平安貴族遊宴文化と桜文学の結合点として後世和歌史に深く影響した。",
    background="平安初期惟喬親王文化サロンと業平交流。",
    development="桜詠の祖型として後世和歌・絵画・能楽に深く継承された。",
    historical_context="9世紀後半惟喬親王遊宴文化。",
    primary_source_url=JTI+"japanese/ise/",
    primary_source_type="JTI: 伊勢物語第八十二段",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# G: 中古散文詳細 (4)
# ============================================================
add(**C, name_ja="大和物語段別構成",
    name_en="Yamato Monogatari: Sectional Structure",
    name_original="大和物語段別",
    period_key="中古",
    definition="天暦5年(951)頃成立『大和物語』173段の段別構成研究。前半（1-140段）は宇多朝-村上朝期の宮廷人歌物語、後半（141-173段）は伝説的歌物語（蘆刈・姨捨等）を集める二部構成。伊勢物語と並ぶ歌物語の双璧で、複数主人公の宮廷説話的展開を特徴とし、後の説話文学の祖型を提供した。",
    background="天暦期歌物語の集大成期。",
    development="後の歌物語・宮廷説話文学の祖型を提供した。",
    historical_context="天暦5年(951)頃の宮廷歌物語編纂期。",
    primary_source_url=JTI+"japanese/yamato/",
    primary_source_type="JTI: 大和物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="平中物語細目",
    name_en="Heichu Monogatari: Detailed Structure",
    name_original="平中物語細目",
    period_key="中古",
    definition="天徳-応和期(959-963)頃成立とされる歌物語『平中物語』。平定文（平中、872?-923?）を主人公とする39段の歌物語で、ほぼ全段が定文と諸女性との贈答歌からなる。伊勢物語が一人の男（業平）を主人公とする祖型を継承し、定文を業平的人物として恋愛遍歴を物語化する歌物語第二の中核作品。",
    background="天徳期歌物語第二世代の確立。",
    development="伊勢物語に次ぐ歌物語の正典として位置づけられた。",
    historical_context="平定文活躍期(9世紀後半-10世紀初)の追想的物語化。",
    primary_source_url=NDL+"info:ndljp/pid/2543372",
    primary_source_type="NDL: 平中物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="多武峰少将物語",
    name_en="Tonomine Shosho Monogatari",
    name_original="多武峰少将物語",
    period_key="中古",
    definition="天禄年間(970-973)成立の歌物語『多武峰少将物語』。藤原高光（多武峰少将、939?-994?）の出家を中心物語化する。藤原道長の祖父藤原師輔の三男高光が天暦元年(961)若くして出家し多武峰に入った経緯を女房的視点で描く。出家を物語主題とする歌物語の独特な作品。",
    background="天禄期出家物語の興隆。",
    development="後の出家文学・遁世物語の祖型を提供した。",
    historical_context="天暦元年(961)藤原高光出家事件の物語化。",
    primary_source_url=NDL+"info:ndljp/pid/2543373",
    primary_source_type="NDL: 多武峰少将物語",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="篁物語",
    name_en="Takamura Monogatari",
    name_original="篁物語",
    period_key="中古",
    definition="平安中期成立とされる歌物語『篁物語』(別名『小野篁集』)。小野篁(802-853)を主人公とし、篁と異母妹との禁忌的恋愛を中心に物語化する。篁の漢詩文才能と異母妹との悲恋という和漢混淆的物語構造を持ち、平安歌物語における禁忌的恋愛主題の深化例として独自の位置を占める。",
    background="平安中期禁忌的恋愛物語の文学化。",
    development="後の禁忌的恋愛文学・近親恋愛物語の祖型を提供した。",
    historical_context="平安中期小野篁伝承の物語化。",
    primary_source_url=NDL+"info:ndljp/pid/2543374",
    primary_source_type="NDL: 篁物語",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# H: 源氏物語帖選抜 (8) — period: 中古
# ============================================================
add(**C, name_ja="源氏物語桐壺巻",
    name_en="Tale of Genji: Kiritsubo Chapter",
    name_original="源氏物語桐壺巻",
    period_key="中古",
    definition="紫式部『源氏物語』第一巻「桐壺」。光源氏出生から12歳元服までを描く物語冒頭巻。「いづれの御時にか…」の冒頭は日本古典文学最高度の名文とされる。源氏の母桐壺更衣の死、藤壺入内、源氏元服までの源氏物語全体の発端を提示し、物語全54巻の祖型構造を確立した。",
    background="一条朝期紫式部執筆開始期。",
    development="日本古典文学冒頭の最高峰として後世評価された。",
    historical_context="寛弘期(1004-1008)頃執筆開始。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語桐壺巻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"invariant",
         "rationale":"桐壺巻冒頭は日本長編物語冒頭の祖型として、AI時代の物語生成における冒頭定型問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI物語生成における冒頭定型"}],
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"平安女性作家",
         "description":"桐壺巻は紫式部による世界最古長編小説の冒頭で、女性作家による長編創作の祖型として位置づけられる。"}])

add(**C, name_ja="源氏物語若紫巻",
    name_en="Tale of Genji: Wakamurasaki Chapter",
    name_original="源氏物語若紫巻",
    period_key="中古",
    definition="源氏物語第五巻「若紫」。源氏18歳、北山で十歳の少女紫上を見初めて引き取り、藤壺との禁忌的密通の懐妊を描く中核巻。源氏物語の主要人物紫上登場と藤壺密通という物語全体を貫く二大主題を確立する画期的巻。「手に取りていつしかも見む紫の根に通ひける野辺の若草」が紫上命名の歌。",
    background="一条朝期紫式部執筆中盤期。",
    development="源氏物語前半の中核巻として後世評価された。",
    historical_context="寛弘期紫式部執筆中盤。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語若紫巻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"若紫巻の少女引取は成人男性による少女育成という主体性問題の古典事例で、AI時代の関係性倫理の歴史的参照点として再考される。",
         "related_ai_phenomenon":"AI時代の関係性倫理"}])

add(**C, name_ja="源氏物語葵巻",
    name_en="Tale of Genji: Aoi Chapter",
    name_original="源氏物語葵巻",
    period_key="中古",
    definition="源氏物語第九巻「葵」。源氏22-23歳、葵上の出産直後の死、六条御息所生霊事件を中核とする源氏物語前半最大の悲劇巻。賀茂祭車争いと六条御息所生霊化、葵上死、その後の紫上裳着・新枕までを描く。生霊・物の怪表現が日本古典文学における超自然的描写の頂点を成す。",
    background="一条朝期紫式部執筆中盤期。",
    development="生霊・物の怪文学の祖型として後世深く影響した。",
    historical_context="寛弘期執筆中盤期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語葵巻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"生霊・物の怪信仰",
         "description":"葵巻の生霊事件は平安貴族社会の超自然信仰の文学化事例として、人類学的精霊信仰研究の比較対象となる。"}])

add(**C, name_ja="源氏物語須磨巻",
    name_en="Tale of Genji: Suma Chapter",
    name_original="源氏物語須磨巻",
    period_key="中古",
    definition="源氏物語第十二巻「須磨」。源氏26-27歳、朧月夜事件発覚により須磨へ自主流謫する転機巻。父桐壺院の夢告、明石入道との縁起、源氏自身の哀傷詠歌「みやこ出でし春の嘆きにおとらめや年経る浦を別れぬる秋」等。流謫文学の祖型として後の流謫物語・流人文学に深く影響した。",
    background="一条朝期紫式部執筆中盤期。",
    development="日本流謫文学の祖型として後世深く継承された。",
    historical_context="寛弘期執筆中盤期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語須磨巻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"須磨巻自主流謫は権力主体の自主的隔離による主体再構築の物語化で、AI時代の主体的退避と再構築を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の自主隔離と主体再構築"}])

add(**C, name_ja="源氏物語明石巻",
    name_en="Tale of Genji: Akashi Chapter",
    name_original="源氏物語明石巻",
    period_key="中古",
    definition="源氏物語第十三巻「明石」。源氏27-28歳、須磨から明石へ移り明石入道に迎えられ明石上と結ばれる転機巻。明石上懐妊・源氏帰京までを描く。明石上出産児（後の明石中宮）が源氏一族の最高栄達を導く物語的伏線として機能し、源氏物語前半最大の運命転換点を成す。",
    background="一条朝期紫式部執筆中盤期。",
    development="源氏物語三大女性（紫上・藤壺・明石上）の最後を確立した。",
    historical_context="寛弘期執筆中盤期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語明石巻",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="源氏物語玉鬘十帖",
    name_en="Tale of Genji: Tamakazura Decade",
    name_original="源氏物語玉鬘十帖",
    period_key="中古",
    definition="源氏物語第二十二巻「玉鬘」から第三十一巻「真木柱」までの十巻。夕顔遺児玉鬘の流転・源氏邸引取・髭黒との結婚までを描く独立的物語群。源氏物語前半終盤の付加的物語として、本筋の紫上-源氏軸とは別の女性主人公中心物語の試みを示し、源氏物語の物語構造の重層性を示す。",
    background="一条朝期紫式部執筆後半期。",
    development="女性主人公中心物語の祖型として位置づけられた。",
    historical_context="寛弘期執筆後半期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語玉鬘十帖",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="源氏物語若菜上下巻",
    name_en="Tale of Genji: Wakana Chapters",
    name_original="源氏物語若菜上・若菜下巻",
    period_key="中古",
    definition="源氏物語第三十四・三十五巻「若菜上下」。源氏40-47歳、女三宮降嫁・柏木密通・薫出生までを描く源氏物語後半最大の転回巻。紫上の苦悩・出家・発病、女三宮密通、薫の出生という後半物語の全展開の起点を成す画期的巻。源氏物語第三部（以降）の物語構造を決定的に変容させた。",
    background="一条朝期紫式部執筆後半期。",
    development="源氏物語第三部の物語構造変容を決定づけた。",
    historical_context="寛弘期執筆後半期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語若菜上下巻",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"物語","status":"rethinking",
         "rationale":"若菜上下の物語転回は長編物語における主題的転換の古典事例で、AI時代の長編物語生成における転回問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI長編生成における物語転回"}])

add(**C, name_ja="源氏物語橋姫巻",
    name_en="Tale of Genji: Hashihime Chapter",
    name_original="源氏物語橋姫巻",
    period_key="中古",
    definition="源氏物語第四十五巻「橋姫」。宇治十帖の冒頭巻で、源氏死後の物語。宇治八宮の二姫君（大君・中君）と源氏の異母弟（実は柏木の子）薫の関係を描く。源氏物語第三部の独立物語性を確立し、後の宇治十帖全体の祖型を成す。「橋姫の心を汲みて高瀬さす…」の歌が宇治十帖の象徴的歌。",
    background="一条朝期紫式部執筆最終期。",
    development="宇治十帖独立物語の祖として後世評価された。",
    historical_context="寛弘期執筆最終期。",
    primary_source_url=JTI+"japanese/genji/",
    primary_source_type="JTI: 源氏物語橋姫巻",
    importance_score=5, source_tier="primary", canonical_in_region="core")


# ============================================================
# I: 中世詩歌歌人 (8) — period: 中世
# ============================================================
add(**C, name_ja="後鳥羽院",
    name_en="Retired Emperor Go-Toba",
    name_original="後鳥羽院",
    period_key="中世",
    definition="後鳥羽院(1180-1239)。新古今集勅撰の主導者であり自身も新古今集第一位歌人(34首入撰)。承久の乱(1221)敗北後は隠岐に流配され『後鳥羽院御口伝』『時代不同歌合』等を残す。「奥山のおどろが下も踏み分けて道ある世ぞと人に知らせむ」の御製で為政者意識を表明した中世和歌の最高権威。",
    background="後鳥羽院政期の和歌再興運動。",
    development="新古今集編纂主導により中世和歌の頂点を画した。",
    historical_context="承久の乱(1221)前後の隠岐流配期。",
    primary_source_url=NDL+"info:ndljp/pid/2543375",
    primary_source_type="NDL: 後鳥羽院御口伝・時代不同歌合",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"後鳥羽院は政治的最高権威と文学的最高権威の合一事例で、AI時代の権威の集中と作者性問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の権威集中と作者性"}],
    cross_domain=[
        {"target_db":"Era-Talents","link_type":"shared_concept",
         "target_entity_name":"中世皇族文化人",
         "description":"後鳥羽院は政治家と文学者の最高水準合一事例として、歴史的偉人比較の中核を占める。"}])

add(**C, name_ja="式子内親王",
    name_en="Princess Shikishi",
    name_original="式子内親王",
    period_key="中世",
    definition="式子内親王(1149-1201)。後白河天皇皇女、賀茂斎院。新古今集49首入撰の女性筆頭歌人。「玉の緒よ絶えなば絶えねながらへば忍ぶることの弱りもぞする」百人一首歌で著名。藤原定家との恋愛伝説が後世能『定家』の典拠となる。中世女性歌人の最高峰として新古今集女流和歌の中核を成した。",
    background="後白河院期女流和歌伝統の継承。",
    development="新古今期女流和歌の最高峰として後世評価された。",
    historical_context="後白河-後鳥羽院期女性皇族文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543376",
    primary_source_type="NDL: 式子内親王集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"主体","status":"invariant",
         "rationale":"式子内親王の内省的閉塞的歌風は中世女性主体の自閉的内面化の極致で、AI時代の内的主体表現の問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の内省的主体表現"}])

add(**C, name_ja="藤原家隆",
    name_en="Fujiwara no Ietaka",
    name_original="藤原家隆",
    period_key="中世",
    definition="藤原家隆(1158-1237)。新古今集43首入撰、新古今集撰者の一人で藤原定家と並び称される新古今期最高歌人の双璧。『壬二集』を残す。「風そよぐならの小川の夕暮はみそぎぞ夏のしるしなりける」百人一首歌で著名。定家の幽玄に対し家隆は明朗端正な歌風で、新古今美学の二大潮流を体現した。",
    background="後鳥羽院期新古今集撰者活動。",
    development="新古今期定家との双璧として中世和歌史を画した。",
    historical_context="新古今集撰集期(1201-1205)。",
    primary_source_url=NDL+"info:ndljp/pid/2543377",
    primary_source_type="NDL: 壬二集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="九条良経",
    name_en="Kujo Yoshitsune",
    name_original="九条良経",
    period_key="中世",
    definition="九条良経(1169-1206)。摂政関白藤原兼実の子で新古今集仮名序の作者。新古今集79首入撰（俊成・西行に次ぎ第三位）、自身も摂政太政大臣を務めた最高権力者かつ歌人。「きりぎりすなくや霜夜のさむしろに衣かたしき独りかも寝む」百人一首歌で著名。新古今期最高権威歌人の一。",
    background="後鳥羽院期新古今集編纂中心人物。",
    development="新古今集仮名序作者として中世和歌正典化を画した。",
    historical_context="後鳥羽院期摂関政治と和歌再興。",
    primary_source_url=NDL+"info:ndljp/pid/2543378",
    primary_source_type="NDL: 秋篠月清集",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="寂蓮",
    name_en="Jakuren",
    name_original="寂蓮",
    period_key="中世",
    definition="寂蓮(1139?-1202)。藤原俊成兄俊海の子で俊成養子（後に出家）。新古今集35首入撰、新古今集撰者の一人。「むらさめの露もまだひぬまきの葉に霧立ちのぼる秋の夕暮」三夕の歌の一として百人一首入撰。三夕は西行・寂蓮・定家の秋夕暮詠で新古今美学の中核を成し、寂蓮はその一翼を担った。",
    background="後鳥羽院期新古今集撰者活動。",
    development="三夕の歌の一として中世幽玄美学の中核を成した。",
    historical_context="新古今集撰集期(1201-1202)。",
    primary_source_url=NDL+"info:ndljp/pid/2543379",
    primary_source_type="NDL: 寂蓮法師集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="京極為兼",
    name_en="Kyogoku Tamekane",
    name_original="京極為兼",
    period_key="中世",
    definition="京極為兼(1254-1332)。京極派始祖で『玉葉和歌集』(1313)撰者。藤原定家曽孫の冷泉為相系から分岐した京極派は、二条派の保守的伝統に対し新古今期定家の幽玄を再生し、繊細な実景描写と内省的詠歌を主張した。鎌倉後期の歌壇分裂（二条派・京極派・冷泉派）の中核存在として中世和歌史を画した。",
    background="鎌倉後期歌壇分裂期の革新派。",
    development="京極派は伏見院・永福門院・京極為子へと継承された。",
    historical_context="鎌倉後期(13世紀末-14世紀初)歌壇分裂期。",
    primary_source_url=NDL+"info:ndljp/pid/2543380",
    primary_source_type="NDL: 為兼卿和歌抄・玉葉集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"京極為兼の革新派和歌は伝統内革新の事例で、AI時代の伝統内革新と古典遵守のバランス問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における伝統内革新"}])

add(**C, name_ja="伏見院",
    name_en="Retired Emperor Fushimi",
    name_original="伏見院",
    period_key="中世",
    definition="伏見院(1265-1317、在位1287-1298)。京極為兼に和歌を学んだ京極派の中心人物で、自身も極めて優れた歌人。『伏見院御集』を残し、玉葉集・風雅集に多数入撰。京極派の繊細な実景観察と内省的歌風を皇族として体現し、二条派が支配する勅撰集体制に対抗する革新派の中核を成した。",
    background="鎌倉後期京極派の皇族中心化。",
    development="京極派の皇族的後援者として歌壇分裂を画した。",
    historical_context="鎌倉後期皇族-京極派同盟期。",
    primary_source_url=NDL+"info:ndljp/pid/2543381",
    primary_source_type="NDL: 伏見院御集",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="永福門院",
    name_en="Eifukumon-in",
    name_original="永福門院",
    period_key="中世",
    definition="永福門院(1271-1342)。伏見院中宮で京極派最重要女性歌人。『永福門院百番自歌合』を残し、玉葉集・風雅集に49首入撰。京極派の繊細な観察的歌風を女性として深化し、新古今期女性歌人式子内親王に次ぐ中世女性歌人の頂点を成す。皇室文化と京極派和歌の融合の中核を担った。",
    background="鎌倉後期京極派皇室文化の女性的展開。",
    development="中世女性歌人として式子内親王に次ぐ地位を確立した。",
    historical_context="鎌倉後期皇室京極派文化期。",
    primary_source_url=NDL+"info:ndljp/pid/2543382",
    primary_source_type="NDL: 永福門院百番自歌合",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"invariant",
         "rationale":"永福門院の繊細な観察的歌風は女性主体の独自視点による中世和歌革新の事例で、AI時代の主体的視点生成を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の女性視点生成"}])


# ============================================================
# J: 中世論評・連歌 (6) — period: 中世
# ============================================================
add(**C, name_ja="慈円『愚管抄』",
    name_en="Jien, Gukansho",
    name_original="愚管抄",
    period_key="中世",
    definition="天台座主慈円(1155-1225)が承久2年(1220)頃著した日本初の体系的歴史哲学書『愚管抄』七巻。神武から順徳まで歴史を「道理」概念で体系化し、末法思想・本地垂迹説を背景に独自の歴史循環論を提示する。漢文ではなく仮名書きの稀有な歴史哲学書で、後の北畠親房『神皇正統記』に深く影響した。",
    background="承久の乱前夜の歴史哲学的思索。",
    development="日本歴史哲学の祖型として後の歴史思想史に深く影響した。",
    historical_context="承久2年(1220)承久乱前夜執筆。",
    primary_source_url=NDL+"info:ndljp/pid/2543383",
    primary_source_type="NDL: 愚管抄",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中世日本歴史哲学",
         "description":"愚管抄は中世日本における体系的歴史哲学の祖型で、東アジア哲学史における歴史思想の比較対象となる。"}])

add(**C, name_ja="一条兼良『花鳥余情』",
    name_en="Ichijo Kaneyoshi, Kacho Yojo",
    name_original="花鳥余情",
    period_key="中世",
    definition="関白一条兼良(1402-1481)が文明4年(1472)頃著した『源氏物語』注釈書『花鳥余情』。河海抄に次ぐ中世源氏物語注釈の頂点で、四辻善成『河海抄』を批判的に継承し、語句注釈・典拠注解の精緻化を達成した。室町期源氏研究の最高峰として近世契沖『源注拾遺』まで標準的注釈となった。",
    background="室町期源氏物語注釈学の発展期。",
    development="中世源氏物語注釈の最高峰として近世まで標準的地位を保った。",
    historical_context="文明4年(1472)応仁乱中の執筆。",
    primary_source_url=NDL+"info:ndljp/pid/2543384",
    primary_source_type="NDL: 花鳥余情",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"受容","status":"invariant",
         "rationale":"花鳥余情は注釈学による古典受容の極致で、AI時代の古典テキスト解釈と注釈生成を再考する参照点となる。",
         "related_ai_phenomenon":"AI時代の古典注釈生成"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中世注釈学",
         "description":"花鳥余情は中世日本注釈学の頂点として、東アジア注釈学伝統との比較研究の中核となる。"}])

add(**C, name_ja="正徹物語",
    name_en="Shotetsu Monogatari",
    name_original="正徹物語",
    period_key="中世",
    definition="室町中期歌人正徹(1381-1459)が永享期(1429-1441)頃著した歌論書『正徹物語』。藤原定家を絶対的師と仰ぎ「定家を難ずる輩は和歌の罪人」と断じる定家絶対主義を表明する。室町期和歌の定家追慕傾向を象徴する歌論書として、二条派・冷泉派対立の中で定家系統の正統性を確立した。",
    background="室町中期定家追慕主義の興隆。",
    development="室町期定家絶対主義の中核論として後世継承された。",
    historical_context="永享期(1429-1441)歌論執筆期。",
    primary_source_url=NDL+"info:ndljp/pid/2543385",
    primary_source_type="NDL: 正徹物語",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="心敬『老葉』",
    name_en="Shinkei, Oiba",
    name_original="老葉",
    period_key="中世",
    definition="連歌師心敬(1406-1475)が著した晩年の発句集『老葉』。心敬は『ささめごと』『老のすさみ』とともに連歌論三部作を成し、『老葉』は実作の発句集として連歌実作と理論の対応を示す重要作。「冷えさび」美学の実践的表現として、宗祇等後の連歌実作に深く影響した。",
    background="室町後期連歌実作の理論化。",
    development="心敬冷えさび実践の実作的展開として後世継承された。",
    historical_context="文明期(1469-1487)心敬晩年期。",
    primary_source_url=NDL+"info:ndljp/pid/2543386",
    primary_source_type="NDL: 老葉",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="心敬『老のすさみ』",
    name_en="Shinkei, Oi no Susami",
    name_original="老のすさみ",
    period_key="中世",
    definition="連歌師心敬(1406-1475)が文明3年(1471)頃著した連歌論『老のすさみ』。『ささめごと』に続く晩年の連歌論で、冷えさび美学の哲学的深化を示す。連歌の付合の本質を「心の詞」として精神性に還元し、実作と理論の融合を目指す。室町後期連歌論の最深層を提示し、宗祇連歌の理論的基盤となった。",
    background="室町後期連歌論の哲学的深化期。",
    development="宗祇等次世代連歌師の理論的基盤となった。",
    historical_context="文明3年(1471)心敬最晩年期。",
    primary_source_url=NDL+"info:ndljp/pid/2543387",
    primary_source_type="NDL: 老のすさみ",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="二条良基『応安新式』",
    name_en="Nijo Yoshimoto, Oan Shinshiki",
    name_original="応安新式",
    period_key="中世",
    definition="関白二条良基(1320-1388)が応安5年(1372)に救済(きゅうせい)と協力して定めた連歌式目『応安新式』。連歌進行の規則（去り嫌い・付合・式目）を体系化した連歌史上最重要式目で、後の連歌・俳諧の式目体系の祖型を成す。二条良基『菟玖波集』編纂とともに連歌正典化の双璧を成した。",
    background="室町初期連歌正典化の制度的確立期。",
    development="後の連歌・俳諧式目すべての祖型を提供した。",
    historical_context="応安5年(1372)連歌制度化期。",
    primary_source_url=NDL+"info:ndljp/pid/2543388",
    primary_source_type="NDL: 応安新式",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"invariant",
         "rationale":"応安新式は連歌制度的規範の制定で、AI時代の生成的創造性と規範統制のバランス問題を再考する参照点となる。",
         "related_ai_phenomenon":"AI生成における規範と創造性"}],
    cross_domain=[
        {"target_db":"MG","link_type":"shared_concept",
         "target_entity_name":"創造活動の制度化",
         "description":"応安新式は集合的創作活動の規範制度化の古典事例として、組織的創造性管理研究の比較対象となる。"}])


# ============================================================
# K: 中世物語・説話 (4)
# ============================================================
add(**C, name_ja="源平盛衰記諸本",
    name_en="Genpei Seisuiki: Manuscript Lineages",
    name_original="源平盛衰記諸本",
    period_key="中世",
    definition="軍記物語『源平盛衰記』48巻の諸本研究。平家物語の異本扱いされる場合と独立軍記扱いされる場合があり、覚一本『平家物語』の流布本系に属しつつ大幅な増補・改作を含む。読み本系として講演用ではなく書写流布された軍記の代表で、『平家物語』本文研究の比較資料として重要。",
    background="中世軍記物語の本文異流多様化期。",
    development="平家物語本文研究の比較資料として位置づけられた。",
    historical_context="鎌倉-室町期軍記物語多様化期。",
    primary_source_url=NDL+"info:ndljp/pid/2543389",
    primary_source_type="NDL: 源平盛衰記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="今昔物語集天竺・震旦部",
    name_en="Konjaku Monogatari Shu: India and China Sections",
    name_original="今昔物語集天竺震旦部",
    period_key="中世",
    definition="平安後期成立『今昔物語集』31巻のうち天竺(インド)部(巻1-5)・震旦(中国)部(巻6-10)。仏伝・釈尊本生譚・中国仏教説話を集める前半10巻で、本朝部(巻11-31)に対する三国伝来仏教説話の体系を成す。三国(印・中・日)を統合する仏教説話世界観を文学化した中世説話文学の中核資料。",
    background="平安後期三国仏教世界観の文学的体系化。",
    development="後の三国伝記等三国説話伝統の祖型を提供した。",
    historical_context="平安後期(12世紀前半)成立期。",
    primary_source_url=NDL+"info:ndljp/pid/2543390",
    primary_source_type="NDL: 今昔物語集天竺震旦部",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"三国仏教世界観",
         "description":"今昔天竺震旦部は印中日三国を統合する仏教世界観の文学的体系化で、東アジア仏教哲学史の比較対象となる。"}])

add(**C, name_ja="無住道暁『沙石集』",
    name_en="Muju Dogyo, Shasekishu",
    name_original="無住道暁・沙石集",
    period_key="中世",
    definition="臨済僧無住道暁(1227-1312)が弘安6年(1283)成立、永仁3年(1295)頃改訂した仏教説話集『沙石集』10巻。仏教教化説話に和漢混淆・諧謔的滑稽を交えた独特な仏教説話で、本地垂迹・神仏融合思想を体系化する。日本中世における和漢混淆説話文学の頂点を成し、後の説話文学に深く影響した。",
    background="鎌倉後期臨済禅と説話文学の融合期。",
    development="日本中世説話文学の頂点として後世評価された。",
    historical_context="弘安6年(1283)鎌倉後期執筆期。",
    primary_source_url=NDL+"info:ndljp/pid/2543391",
    primary_source_type="NDL: 沙石集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"中世仏教説話思想",
         "description":"沙石集は中世禅と説話の融合事例として、東アジア仏教哲学と物語の関係研究の中核を占める。"}])

add(**C, name_ja="十二類絵巻",
    name_en="Junirui Emaki: The Twelve Animals Scroll",
    name_original="十二類絵巻",
    period_key="中世",
    definition="室町期絵巻物『十二類絵巻』(15世紀頃)。十二支の動物達が歌合を開く擬人化動物絵巻で、御伽草子的物語と絵画の融合作品。動物を擬人化して人間社会を諧謔的に描く動物文学の中世的祖型を成し、付喪神絵巻等とともに中世擬人化文学の系譜を形成する。",
    background="室町期擬人化文学・絵巻物の興隆。",
    development="近世以降の動物文学・擬人化文学の祖型を提供した。",
    historical_context="室町期(15世紀)擬人化絵巻物文化。",
    primary_source_url=NDL+"info:ndljp/pid/2543392",
    primary_source_type="NDL: 十二類絵巻",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


# ============================================================
# L: 軍記諸本 (3)
# ============================================================
add(**C, name_ja="太平記諸本(古態本・西源院本)",
    name_en="Taiheiki: Old Form and Saigen-in Manuscripts",
    name_original="太平記古態本・西源院本",
    period_key="中世",
    definition="『太平記』40巻の諸本研究。古態本系統(神田本等)と流布本系統(西源院本等)が並存し、本文異同が大規模で複雑。古態本は南北朝動乱期(1318-1368)成立の原型に近いとされ、西源院本は後世流布本の代表。本文系統研究は太平記成立論・本文批判の中核課題で、軍記諸本研究の典型例。",
    background="南北朝期太平記本文形成と後世流布変遷。",
    development="軍記本文系統研究の典型例として中世文学研究の中核となった。",
    historical_context="南北朝期(14世紀)太平記本文形成期。",
    primary_source_url=NDL+"info:ndljp/pid/2543393",
    primary_source_type="NDL: 太平記古態本・西源院本",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="義経記諸本",
    name_en="Gikeiki: Manuscript Lineages",
    name_original="義経記諸本",
    period_key="中世",
    definition="『義経記』8巻の諸本研究。室町前期(15世紀前半)成立の源義経伝記軍記で、平家物語・吾妻鏡を補完する義経主人公の英雄譚的軍記。流布本・古活字本・写本系統等の諸本があり、義経の鞍馬時代から最期までを描く。後の能・浄瑠璃・歌舞伎義経物のすべての祖型を成す。",
    background="室町前期英雄譚的軍記の発達。",
    development="後の能・浄瑠璃・歌舞伎義経物の祖型を提供した。",
    historical_context="室町前期(15世紀)英雄軍記成立期。",
    primary_source_url=NDL+"info:ndljp/pid/2543394",
    primary_source_type="NDL: 義経記",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="曾我物語(真名本・仮名本)",
    name_en="Soga Monogatari: Mana and Kana Versions",
    name_original="曾我物語真名本・仮名本",
    period_key="中世",
    definition="『曾我物語』12巻の諸本研究。真名本(漢字漢文体)と仮名本(仮名交り文)の二系統が並存し、真名本が古態とされる。建久4年(1193)富士裾野巻狩での曾我兄弟仇討事件を物語化した英雄譚軍記で、義経記と並ぶ室町期英雄譚の双璧。後の能・浄瑠璃・歌舞伎の曾我物すべての祖型。",
    background="建久4年(1193)曾我兄弟仇討事件の英雄譚化。",
    development="後の能・浄瑠璃・歌舞伎曾我物の祖型を提供した。",
    historical_context="室町期英雄譚軍記成立期。",
    primary_source_url=NDL+"info:ndljp/pid/2543395",
    primary_source_type="NDL: 曾我物語真名本・仮名本",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# M: 近世補完 (3)
# ============================================================
add(**C, name_ja="松尾芭蕉『野ざらし紀行』",
    name_en="Matsuo Basho, Nozarashi Kiko",
    name_original="野ざらし紀行",
    period_key="近世",
    definition="松尾芭蕉(1644-1694)が貞享元年(1684)8月から翌年4月の旅を記した俳諧紀行『野ざらし紀行』(別名『甲子吟行』)。江戸から伊賀帰省・京・名古屋・木曽路を経て江戸帰着の旅。「野ざらしを心に風のしむ身かな」が冒頭句。芭蕉俳諧紀行5部作の最初の作品で、後の『おくのほそ道』への祖型となる紀行文学の発端。",
    background="貞享期芭蕉俳諧紀行文学の発端。",
    development="芭蕉俳諧紀行5部作の最初として『おくのほそ道』に至る祖型を提供した。",
    historical_context="貞享元-2年(1684-1685)芭蕉初期紀行期。",
    primary_source_url=AOZORA+"cards/000146/files/2533_19994.html",
    primary_source_type="青空文庫: 野ざらし紀行",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="松尾芭蕉『笈の小文』",
    name_en="Matsuo Basho, Oi no Kobumi",
    name_original="笈の小文",
    period_key="近世",
    definition="松尾芭蕉が貞享4年-元禄元年(1687-1688)の旅を記した俳諧紀行『笈の小文』(没後刊行)。江戸から伊勢・吉野・須磨・明石を経て大坂に至る旅で、「造化にしたがひ造化にかへれ」「風雅における誠」等の芭蕉俳諧理論の中核命題が表明される。芭蕉俳諧理論的中核を含む紀行として『おくのほそ道』に次ぐ重要作。",
    background="貞享期芭蕉俳諧理論成立期。",
    development="芭蕉風雅論の中核を提示し後の俳論史に深く影響した。",
    historical_context="貞享4-元禄1年(1687-1688)芭蕉理論形成期。",
    primary_source_url=AOZORA+"cards/000146/files/2534_19995.html",
    primary_source_type="青空文庫: 笈の小文",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"笈の小文の「造化にしたがひ造化にかへれ」は自然と創造的主体の合一論で、AI時代の創造性論を再考する古典的参照点となる。",
         "related_ai_phenomenon":"AI時代の自然と創造性"}])

add(**C, name_ja="与謝蕪村七部集",
    name_en="Yosa Buson Shichibushu",
    name_original="蕪村七部集",
    period_key="近世",
    definition="与謝蕪村(1716-1784)門下の俳諧七部集の総称。『其雪影』『明烏』『花鳥編』『あけ烏』『夜半叟句集』『新花つみ』等を含む蕪村派俳諧の集成。蕪村の絵画的・知的洗練の俳諧美学を体系化した蕪村派の集大成で、芭蕉七部集に対応する天明俳諧の正典的集成として後世評価された。",
    background="天明期蕪村派俳諧の集成期。",
    development="芭蕉七部集に並ぶ近世俳諧正典として位置づけられた。",
    historical_context="天明期(1781-1789)蕪村派活動期。",
    primary_source_url=AOZORA+"cards/000232/files/4473_30712.html",
    primary_source_type="青空文庫: 蕪村七部集",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"創造性","status":"rethinking",
         "rationale":"蕪村七部集の絵画的俳諧は視覚と言語の融合創造の事例で、AI時代のマルチモーダル生成創造性を再考する参照点となる。",
         "related_ai_phenomenon":"AIマルチモーダル生成"}],
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"近世絵画詩文化",
         "description":"蕪村俳画は絵画と詩文の文化的融合事例として、人類学的物質文化研究の比較対象となる。"}])


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj in ["上代", "中古", "中世", "近世"]:
            row = db.conn.execute(
                "SELECT id FROM periods WHERE name_ja=? AND region='東アジア' LIMIT 1",
                (nj,)).fetchone()
            if row is None:
                print(f"  [error] period not found: {nj}")
                return 1
            period_ids[nj] = row[0]

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
        print(f"[c16-w20] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c16-w20] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
