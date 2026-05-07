"""LIT-DB Phase 2 Wave 12 — C10 Modernism ADD 40 (avant-gardes & expansion).

Subfield: lit_eu_modernism (id=6), region='西欧'.
Existing 40 concepts cover Joyce/Proust/Kafka/Woolf core. This wave ADDS 40
NEW concepts covering avant-garde movements, modernist forms, modernist
genres, and major individual authors not yet in the DB.

Verification policy:
  - 'primary'   -> PD or borderline-PD literary text / contemporaneous
                   document (Wikisource, Project Gutenberg, archive.org,
                   manifesto archives).
  - 'secondary' -> canonical scholarly synthesis (Britannica, SEP,
                   academic-grade Wikipedia entry).
  - 'tertiary'  -> synthetic critical category for taxonomic completeness.

40 concepts split into five blocks of 8:
  A: 前衛運動I — 未来派・ダダ・シュルレアリスム — 8
  B: 前衛運動II — 表現主義・イマジズム・ヴォーティシズム・アクメイズム・構成主義 — 8
  C: モダニズム形式・技法 — 8
  D: モダニズム作家I（独・墺・伊・葡・西） — 8
  E: モダニズム作家II（英・米・南米・ジャンル） — 8
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# Use existing period 'モダニズム期' (id=22) for all entries here.
PERIOD_KEY = "モダニズム期"


GUTEN = "https://www.gutenberg.org/"
ARCHIVE = "https://archive.org/details/"
WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_FR = "https://fr.wikipedia.org/wiki/"
WIKI_DE = "https://de.wikipedia.org/wiki/"
WIKI_IT = "https://it.wikipedia.org/wiki/"
WIKI_ES = "https://es.wikipedia.org/wiki/"
WIKI_PT = "https://pt.wikipedia.org/wiki/"
WIKI_RU = "https://ru.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
BRITT = "https://www.britannica.com/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_RU = "https://ru.wikisource.org/wiki/"
MOMA = "https://www.moma.org/"


CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)

C = dict(subfield_code="lit_eu_modernism", region="西欧",
         original_script="roman", period_key=PERIOD_KEY)


# ============================================================
# A: 前衛運動I（未来派・ダダ・シュルレアリスム）— 8件
# ============================================================
add(**C, name_ja="マリネッティ「未来派宣言」",
    name_en="Marinetti's Manifesto of Futurism",
    name_original="Manifesto del Futurismo",
    definition="フィリッポ・トンマーゾ・マリネッティ（1876-1944）が1909年2月20日パリ『フィガロ』紙第一面に発表した未来派運動の創設宣言。速度・機械・戦争・都市の美を讃え、博物館・図書館・アカデミーに代表される過去崇拝の破壊を綱領化した。20世紀前衛運動の出発点であり、宣言（マニフェスト）を文学ジャンルとして確立した記念碑的テキスト。",
    background="ベル・エポック末期イタリアの近代化遅滞意識、ベルクソン生命哲学・ニーチェ受容、産業化と機械文明の文化的衝撃。",
    development="ロシア未来派、ダダ、ヴォーティシズム、シュルレアリスム等の20世紀前衛運動の方法論的祖型となった。",
    historical_context="第一次世界大戦前夜のヨーロッパ前衛運動の制度化と、宣言文学（manifesto）ジャンルの誕生。",
    primary_source_url=WSRC_IT+"Manifesto_del_Futurismo",
    primary_source_type="Wikisource: Manifesto del Futurismo (1909)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"未来派宣言は機械・速度・自動性の美を讃えることで、人間中心的作者性を相対化する。AI時代の機械生成と作家性の問いを先取りする古典的参照点として再読される。",
         "related_ai_phenomenon":"AI生成と機械的創造性の美学"},
        {"axis":"言語","status":"rethinking",
         "rationale":"マリネッティの「自由な言葉（parole in libertà）」は構文を破壊しタイポグラフィを解放する技法で、生成AIによる構文逸脱・視覚的言語の祖型。",
         "related_ai_phenomenon":"AI生成における構文逸脱と視覚的言語"}],
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"宣言（マニフェスト）の詩学",
         "description":"マリネッティ宣言は20世紀宣言文学の規範形式を確立し、詩学ジャンル論の中心研究対象。"}])

add(**C, name_ja="マヤコフスキー革命詩",
    name_en="Mayakovsky's revolutionary poetics",
    name_original="Маяковский: революционная поэтика",
    definition="ウラジーミル・マヤコフスキー（1893-1930）がロシア・キュビズム未来派の宣言「社会的趣味への平手打ち」(1912)以降展開した詩的方法。階段状改行（лесенка）、ハイパーボリック直喩、街頭朗誦のための音響構造を統合し、革命と前衛詩を結合した。1917年十月革命後はソヴィエト宣伝詩の中心担い手となり、20世紀政治詩の規範を形成した。",
    background="ロシア未来派（ブルリューク兄弟、フレーブニコフ、クルチョーヌィフ）の制度的成立、革命前夜ロシアの社会的緊張。",
    development="ブレヒト『マヤコフスキーへの追悼』、20世紀の街頭朗誦詩・政治詩・パフォーマンス詩への系譜的影響。",
    historical_context="ロシア革命と前衛芸術の蜜月期（1917-1920年代前半）、その後のスターリン主義文化政策との衝突。",
    primary_source_url=WSRC_RU+"Облако_в_штанах_(Маяковский)",
    primary_source_type="Wikisource: Облако в штанах (1915)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ツァラ「ダダ宣言」",
    name_en="Tzara's Dada Manifesto",
    name_original="Manifeste Dada 1918",
    definition="トリスタン・ツァラ（1896-1963）が1918年7月23日チューリヒで発表したダダ運動の主要宣言。「私はダダ主義者であり、ダダに反対する者でもある」という自己矛盾を綱領化し、論理・意味・芸術制度そのものへの根本的拒絶を表明した。第一次世界大戦末期のヨーロッパ価値体系崩壊を前衛芸術の方法的前提として理論化した宣言。",
    background="第一次世界大戦中の中立国スイス・チューリヒ（キャバレー・ヴォルテール、1916設立）に集結したヨーロッパ前衛芸術家のディアスポラ。",
    development="ダダはベルリン・ニューヨーク・パリへ伝播し、シュルレアリスム（1924）の直接的母胎となった。20世紀後半のフルクサス、コンセプチュアル・アートにも継承された。",
    historical_context="第一次世界大戦期ヨーロッパ価値秩序の崩壊と、芸術的虚無主義の体系的表明。",
    primary_source_url=WIKI_EN+"Dada_Manifesto",
    primary_source_type="Wikipedia: Dada Manifesto (Tzara, 1918)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"真正性","status":"rethinking",
         "rationale":"ダダ宣言は意味・論理・芸術制度の真正性そのものを否定する。AI生成テキストの真正性なき生成という現象の理論的祖型として再読される。",
         "related_ai_phenomenon":"AI生成における真正性なき生成"},
        {"axis":"作者性","status":"rethinking",
         "rationale":"ダダの偶然・カットアップ・チャンスオペレーションは作者意図を機械的・偶然的過程に置換する。生成AIの確率的生成と理論的に共振する。",
         "related_ai_phenomenon":"確率的・偶然的生成と作者意図"}])

add(**C, name_ja="フーゴ・バル音響詩",
    name_en="Hugo Ball's sound poetry",
    name_original="Lautgedicht",
    definition="フーゴ・バル（1886-1927）が1916年6月23日チューリヒ・キャバレー・ヴォルテールで朗誦した音響詩「カラヴァネ」「ガジ・ベリ・ビンバ」等。意味を持たない音節の連鎖によって、言語の意味機能から音響的・身体的次元を解放する詩的方法。20世紀音響詩・コンクリート詩・パフォーマンス詩の出発点となった。",
    background="第一次世界大戦中のスイス・チューリヒ前衛芸術圏、ダダ運動の制度的成立（キャバレー・ヴォルテール）。",
    development="クルト・シュヴィッタース『ウル・ソナタ』、レトリスム（イジドール・イズー）、コンクリート詩、20世紀後半のサウンドアート全般に継承された。",
    historical_context="第一次世界大戦期のヨーロッパ言語的・倫理的危機の中での、言語の物質的次元への撤退。",
    primary_source_url=WIKI_DE+"Lautgedicht",
    primary_source_type="Wikipedia: Lautgedicht (Hugo Ball)",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"音響詩は意味から音響への撤退を綱領化する。生成AIが意味を欠いたまま音響的・形式的整合性を生む現象の文学的祖型。",
         "related_ai_phenomenon":"AI生成における意味なき音響的整合性"}])

add(**C, name_ja="ブルトン「シュルレアリスム宣言」",
    name_en="Breton's Manifeste du surréalisme",
    name_original="Manifeste du surréalisme",
    definition="アンドレ・ブルトン（1896-1966）が1924年に発表したシュルレアリスム運動の創設宣言。「シュルレアリスムとは純粋な心的自動運動」と定義し、自動筆記（écriture automatique）、夢の記録、客観的偶然、コラージュを方法論的中心とする。フロイト精神分析を文学的方法として組織化した20世紀前衛運動最大の綱領。",
    background="第一次世界大戦後のダダ運動分解、フロイト精神分析の文学的受容、ロートレアモン・ランボー再評価。",
    development="第二次宣言(1930)、戦後シュルレアリスム、米国前衛詩（オハラ、アシュベリー）、ラテンアメリカ・シュルレアリスム（パス、レサマ・リマ）に継承された。",
    historical_context="第一次世界大戦後パリの前衛芸術中心地化と、フロイト精神分析の文学的制度化。",
    primary_source_url=WIKI_FR+"Manifeste_du_surr%C3%A9alisme",
    primary_source_type="Wikipedia(FR): Manifeste du surréalisme (1924)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"自動筆記は意識的作者の判断を排除して無意識から直接テキストを生成する。AIにおける「作者を介在しない生成」の文学的祖型として根本的参照点。",
         "related_ai_phenomenon":"AIによる作者不在の自動生成"},
        {"axis":"主体","status":"rethinking",
         "rationale":"シュルレアリスム的主体の解離・脱中心化は、AI生成における主体不在のテキスト構造と深い類比関係を持つ。",
         "related_ai_phenomenon":"AI生成における主体の解離と脱中心化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"無意識の方法化",
         "description":"シュルレアリスム宣言はフロイト精神分析を文学的方法論として体系化した文書であり、20世紀の主体・無意識論の哲学的基盤。"}])

add(**C, name_ja="アラゴン『パリの農夫』",
    name_en="Aragon's Le Paysan de Paris",
    name_original="Le Paysan de Paris",
    definition="ルイ・アラゴン（1897-1982）が1926年に発表したシュルレアリスムの代表的散文作品。パリの「オペラ・パッサージュ」「ビュット=ショーモン公園」を、神話化された都市的空間として記述する。ヴァルター・ベンヤミン『パサージュ論』に直接的影響を与え、シュルレアリスム的都市民俗誌（urban ethnography）の祖型となった。",
    background="1920年代パリのシュルレアリスム運動、都市と前衛芸術の関係の制度化、ボードレール『パリの憂愁』伝統の継承。",
    development="ベンヤミン『パサージュ論』、20世紀の都市文学・心理地理学（シチュアシオニスト）、現代の都市民俗誌文学に継承された。",
    historical_context="戦間期パリの前衛芸術中心地化と、都市消費空間（パッサージュ）の文学的神話化。",
    primary_source_url=WIKI_FR+"Le_Paysan_de_Paris",
    primary_source_type="Wikipedia(FR): Le Paysan de Paris",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    cross_domain=[
        {"target_db":"AN","link_type":"shared_concept",
         "target_entity_name":"都市民俗誌",
         "description":"アラゴンの都市記述は20世紀都市民俗誌（urban ethnography）の文学的祖型として人類学・文学の境界に位置する。"}])

add(**C, name_ja="エリュアール恋愛詩",
    name_en="Éluard's love poetry",
    name_original="Paul Éluard: poésie amoureuse",
    definition="ポール・エリュアール（1895-1952）がシュルレアリスム期に展開した恋愛詩（『苦悩の首都』1926、『愛、詩』1929等）。シュルレアリスム的イメージ連想を抒情的中心テーマと統合し、自動筆記の機械的側面を抒情に転化した詩的方法を確立した。20世紀仏語抒情詩の規範を更新し、レジスタンス期『自由（Liberté）』(1942)で政治詩としても結実した。",
    background="1920年代シュルレアリスム運動の中での抒情的回帰と、ガラ（後ダリ夫人）との恋愛・破局体験の詩的昇華。",
    development="戦後仏語詩（シャール、ボヌフォワ）、ラテンアメリカ・シュルレアリスム（ネルーダ、パス）に深い影響を与えた。",
    historical_context="戦間期シュルレアリスム運動の制度化期と、運動の抒情化・政治化への分岐。",
    primary_source_url=WIKI_FR+"Paul_%C3%89luard",
    primary_source_type="Wikipedia(FR): Paul Éluard",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="客観的偶然（hasard objectif）",
    name_en="objective chance",
    name_original="hasard objectif",
    definition="アンドレ・ブルトンが『ナジャ』(1928)、『狂気の愛』(1937)で展開したシュルレアリスムの中心理論的概念。外部現実の偶然的出来事が、主体の無意識的欲望と「客観的に」一致する瞬間を、シュルレアリスム的経験の中核と理論化した。フロイト無意識論とエンゲルス『自然の弁証法』の偶然・必然論を統合した独自の理論。",
    background="フロイト精神分析と1920-30年代仏共産党文化（ブルトン1927-33年党員）の弁証法的唯物論との接続。",
    development="戦後フランス哲学（バタイユ、ラカン）、20世紀後半の偶然性概念（ジョン・ケージ偶然オペレーション）への系譜的影響。",
    historical_context="戦間期シュルレアリスム運動の理論的精緻化期と、精神分析・マルクス主義の文学的統合。",
    primary_source_url=WIKI_FR+"Hasard_objectif",
    primary_source_type="Wikipedia(FR): Hasard objectif",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"客観的偶然は作家の意図を超えた偶然的一致に詩的価値を見いだす方法論。AI生成における偶然的整合性の文学的価値を理論化する古典的祖型。",
         "related_ai_phenomenon":"AI生成における偶然的整合性の詩学"}])


# ============================================================
# B: 前衛運動II（表現主義・イマジズム・ヴォーティシズム・アクメイズム・構成主義）— 8件
# ============================================================
add(**C, name_ja="トラークル詩",
    name_en="Trakl's poetry",
    name_original="Georg Trakl: Gedichte",
    definition="ゲオルク・トラークル（1887-1914）が遺した独語表現主義詩。『詩集』(1913)、『夢の中のセバスチャン』(1915、遺稿)に収録された短詩は、色彩象徴（青・赤・黒）、季節と死、近親相姦的兄妹愛、廃頽の都市像によって、独語表現主義の頂点を成した。第一次世界大戦東部戦線で薬物自死を遂げ、詩と生の一致のロマン主義的結末を体現した。",
    background="ハプスブルク末期オーストリア（ザルツブルク）の没落世界、ニーチェ・ホフマンスタールの後継世代、表現主義誌『デア・ブレンナー』との関係。",
    development="戦後独語詩（パウル・ツェラン、ベルトルト・ブレヒト初期）、20世紀表現主義詩学全般への系譜的影響。",
    historical_context="第一次世界大戦勃発期と、ハプスブルク帝国末期の文化的崩壊感覚。",
    primary_source_url=WSRC_DE+"Georg_Trakl",
    primary_source_type="Wikisource(DE): Georg Trakl Gedichte",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ゴットフリート・ベン",
    name_en="Gottfried Benn",
    name_original="Gottfried Benn",
    definition="ゴットフリート・ベン（1886-1956）は独語表現主義詩・後期モダニズム詩の代表的詩人。医師として執筆した詩集『死体置場（Morgue）』(1912)で、医学的視線・身体の解剖学的記述を詩に持ち込み、表現主義の生理学的極限形態を確立した。戦後『静的詩』(1948)で「絶対詩」概念を理論化し、20世紀後半の詩学に深い影響を与えた。",
    background="ベルリン医学界と表現主義文学界の二重帰属、第一次世界大戦軍医経験、戦間期の都市的虚無体験。",
    development="戦後独語詩（パウル・ツェラン、インゲボルク・バッハマン）、英語圏モダニズム詩との並行性研究の中心対象となった。",
    historical_context="ヴァイマール期独語詩の生理学的転回と、戦後西独における詩の制度的再建。",
    primary_source_url=WIKI_DE+"Gottfried_Benn",
    primary_source_type="Wikipedia(DE): Gottfried Benn",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="アウグスト・シュトラム",
    name_en="August Stramm",
    name_original="August Stramm",
    definition="アウグスト・シュトラム（1874-1915）は独語表現主義詩の方法的革新者。雑誌『デア・シュトゥルム』周辺で活動し、語の凝縮・新造語・通常統語法の解体によって、独語詩の極限的圧縮形式を確立した。第一次世界大戦東部戦線で戦死。短期間の活動ながら、表現主義詩学の方法的中核を提供した。",
    background="ヘルヴァルト・ヴァルデン編『デア・シュトゥルム』（1910創刊）周辺の独語前衛芸術運動。",
    development="戦間期独語前衛詩、戦後コンクリート詩・実験詩への系譜的影響。",
    historical_context="第一次世界大戦勃発期独語前衛運動の制度化と、戦争による主要担い手の喪失。",
    primary_source_url=WSRC_DE+"August_Stramm",
    primary_source_type="Wikisource(DE): August Stramm",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="パウンドのイマジズム宣言",
    name_en="Pound's Imagist tenets",
    name_original="A Few Don'ts by an Imagiste",
    definition="エズラ・パウンド（1885-1972）が1913年雑誌『ポエトリー』に発表したイマジズム運動の方法的中核。「イメージは知的・感情的複合体を瞬時に呈示するもの」と定義し、「直接的な処理」「一語一語が必要」「シーケンス・オブ・ザ・ミュージカル・フレーズ」を三原則とする。20世紀英語圏モダニズム詩の出発点。",
    background="フローベール「正確な言葉」、東洋詩（漢詩・俳句）の影響、19世紀末英語詩の修辞的過剰への反動。",
    development="エリオット『ウェイスト・ランド』、ウィリアム・カーロス・ウィリアムズ、20世紀英語圏モダニズム詩・客観主義詩の理論的祖型となった。",
    historical_context="第一次世界大戦前夜のロンドン文学界における英米合流期、フィッツロイ・スクエア前衛文学圏。",
    primary_source_url=WIKI_EN+"Imagism",
    primary_source_type="Wikipedia: Imagism / Pound A Few Don'ts",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"イマジズムの「一語一語の必要性」原則は、生成AIの確率的トークン生成（不要な語が混入する傾向）と根本的に対立する文学理念。AI時代の精確言語の基準点。",
         "related_ai_phenomenon":"AI生成における冗長性とイマジズム的精確性"}])

add(**C, name_ja="H.D.（ヒルダ・ドゥーリトル）",
    name_en="H.D. (Hilda Doolittle)",
    name_original="Hilda Doolittle / H.D.",
    definition="ヒルダ・ドゥーリトル（1886-1961）は米国・英国で活動したイマジズム詩運動の中心詩人。短詩「オリーアド」「ヘリオドラ」等で古典ギリシア神話を極限的圧縮形式で再構成し、イマジズムの女性的方法を確立した。後期長詩『三部作』(1944-46)、『ヘレン・イン・エジプト』(1961)で、20世紀フェミニスト・モダニズム詩の規範を成した。",
    background="エズラ・パウンドとの婚約・破局、ロンドン亡命、第一次・第二次世界大戦体験、フロイト精神分析（1933-34年フロイト直接分析）の体験。",
    development="20世紀フェミニスト詩学（アドリエンヌ・リッチ、エイドリエン・リッチ批評）、長詩形式論の中心研究対象となった。",
    historical_context="戦間期英米モダニズム圏の女性詩人の制度的位置と、フロイト精神分析の文学的応用。",
    primary_source_url=GUTEN+"ebooks/53324",
    primary_source_type="Project Gutenberg: H.D. Sea Garden (1916)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴォーティシズム（ルイス）",
    name_en="Vorticism (Wyndham Lewis)",
    name_original="Vorticism",
    definition="ウィンダム・ルイス（1882-1957）が1914年雑誌『ブラスト（BLAST）』創刊号で綱領化した英国前衛運動。マリネッティ未来派の動的エネルギー賛美に対し、強度・凝縮・幾何学的形式を中心理念とした。文学（パウンド、エリオット）と視覚芸術（ルイス、ガウディエ=ブルゼスカ）の統合運動として、英国モダニズムの方法的核を提供した。",
    background="第一次世界大戦前夜ロンドン前衛芸術圏、未来派・キュビズム・表現主義の英国受容。",
    development="第一次世界大戦による運動解体（ガウディエ=ブルゼスカ戦死1915）、戦後パウンド・エリオット・ルイスの個別的展開、戦後英国前衛運動の歴史的祖型。",
    historical_context="第一次世界大戦前夜の英国前衛芸術運動の短期的隆盛と、戦争による解体。",
    primary_source_url=ARCHIVE+"BLAST_no.1_June_1914",
    primary_source_type="Archive.org: BLAST no.1 (1914) facsimile",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マンデリシュタームのアクメイズム",
    name_en="Mandelstam's Acmeism",
    name_original="Акмеизм / Мандельштам",
    definition="オーシプ・マンデリシュターム（1891-1938）がニコライ・グミリョフ・アンナ・アフマートヴァらと展開したロシア・アクメイズム運動の代表的詩学。象徴派の神秘主義への対抗として、語の物質性・建築的構造・地中海古典文化への定位を中心理念とした。スターリン期の弾圧で1938年ヴラジヴォストーク中継収容所にて獄死、20世紀ロシア詩の殉教的中心人物となった。",
    background="ロシア銀の時代末期（1910年代）の象徴派分解、グミリョフ「象徴主義の遺産とアクメイズム」(1913)宣言、ペテルブルク文学圏。",
    development="アフマートヴァ『レクイエム』、20世紀後半ロシア詩（ブロツキー）、世界詩学のロシア亡命詩人系譜の中心源流。",
    historical_context="ロシア革命前後の文学的多様化と、スターリン期の前衛詩人弾圧。",
    primary_source_url=WIKI_RU+"%D0%9C%D0%B0%D0%BD%D0%B4%D0%B5%D0%BB%D1%8C%D1%88%D1%82%D0%B0%D0%BC,_%D0%9E%D1%81%D0%B8%D0%BF_%D0%AD%D0%BC%D0%B8%D0%BB%D1%8C%D0%B5%D0%B2%D0%B8%D1%87",
    primary_source_type="Wikipedia(RU): Осип Мандельштам",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="アフマートヴァ『レクイエム』",
    name_en="Akhmatova's Requiem",
    name_original="Реквием",
    definition="アンナ・アフマートヴァ（1889-1966）が1935-40年に執筆し、ソヴィエト連邦内では1987年まで出版されなかった連作長詩。スターリン大粛清期に逮捕された息子レフ・グミリョフを獄門で待つ母親たちの集合的経験を、アクメイズム的精確と聖母マリア哀歌伝統を融合した形式で記述した。20世紀ロシア詩の倫理的頂点を成す作品。",
    background="スターリン大粛清期（1937-38）の集団的経験、息子レフの逮捕・流刑、夫グミリョフ銃殺(1921)・夫プーニン獄死(1953)等の連続的喪失。",
    development="ソルジェニーツィン『収容所群島』、20世紀証言文学・トラウマ文学の中心参照点となった。",
    historical_context="スターリン期の文学的検閲と、口承による地下伝達（1965年米国で初版印刷、1987年ソ連内出版）。",
    primary_source_url=WIKI_RU+"%D0%A0%D0%B5%D0%BA%D0%B2%D0%B8%D0%B5%D0%BC_(%D0%90%D1%85%D0%BC%D0%B0%D1%82%D0%BE%D0%B2%D0%B0)",
    primary_source_type="Wikipedia(RU): Реквием (Ахматова)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"哀歌・証言詩学",
         "description":"『レクイエム』は20世紀証言文学の詩的祖型として、アガンベン『アウシュヴィッツの残りもの』等の現代証言理論の重要参照点。"}])


# ============================================================
# C: モダニズム形式・技法 — 8件
# ============================================================
add(**C, name_ja="自由詩（モダニズム）",
    name_en="free verse (modernist)",
    name_original="vers libre",
    definition="19世紀末仏語詩（グスタヴ・カーン、ジュール・ラフォルグ）に発し、20世紀英米モダニズム（パウンド、エリオット、ウィリアムズ）が体系化した詩形。定型律から音楽的フレーズ（musical phrase）への移行を綱領化したパウンド「3つのドント」(1913)が方法論的中心。20世紀詩の主要形式となり、伝統的韻律詩形に対する制度的優位を確立した。",
    background="19世紀末仏語象徴派の韻律解放、ホイットマン『草の葉』の英語自由詩伝統、東洋詩（漢詩・俳句）の影響。",
    development="20世紀後半の口語詩・脱韻律詩の規範形式となり、現代詩の主要形式として制度化された。",
    historical_context="19世紀末から20世紀初頭の韻律論論争と、詩形の解放と再構築。",
    primary_source_url=WIKI_EN+"Free_verse",
    primary_source_type="Wikipedia: Free verse",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="モンタージュ（文学的）",
    name_en="literary montage",
    name_original="literary montage",
    definition="エイゼンシュテイン映画モンタージュ理論を文学に応用した構成原理。ジョン・ドス・パソス『U.S.A.三部作』(1930-36)、デーブリン『ベルリン・アレクサンダー広場』(1929)、エリオット『荒地』(1922)に代表される、断片的テキスト群の並置による意味生成の技法。20世紀モダニズム長編・長詩の中心方法論。",
    background="エイゼンシュテイン『戦艦ポチョムキン』(1925)等の映画モンタージュの世界的影響、20世紀メディア環境（新聞・映画・ラジオ）の文学への浸透。",
    development="戦後ポストモダニズム（バロウズ・カットアップ、ピンチョン）、現代のメディア横断的小説に継承された。",
    historical_context="戦間期映画と文学の相互影響、メディア環境の文学的吸収。",
    primary_source_url=WIKI_EN+"Montage_(literature)",
    primary_source_type="Wikipedia: Literary montage",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"モンタージュは既存テキスト断片の並置と再編成を方法化する。AI生成における学習データの再構成的生成と理論的に並行する古典的技法。",
         "related_ai_phenomenon":"AI生成における学習データの再構成"}])

add(**C, name_ja="コラージュ（文学的）",
    name_en="literary collage",
    name_original="literary collage",
    definition="キュビズム絵画コラージュを文学に応用した方法。マックス・エルンスト『百頭女』(1929)等のコラージュ小説、ガートルード・スタイン『軟らかいボタン』(1914)、エリオット『荒地』(1922)の引用織物に代表される、異質なテキスト要素の物質的並置。20世紀前衛文学の中心技法。",
    background="ピカソ・ブラック1912年以降のキュビズム・パピエ・コレ、ダダ・シュルレアリスムのコラージュ実践、戦間期メディア環境（雑誌・広告）の文学への影響。",
    development="戦後ポストモダン文学（カットアップ、サンプリング）、現代のリミックス文化、AI生成テキストの祖型として再読される。",
    historical_context="20世紀前半の視覚芸術と文学の方法的相互浸透期。",
    primary_source_url=WIKI_EN+"Collage_novel",
    primary_source_type="Wikipedia: Collage novel",
    importance_score=4, source_tier="secondary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"コラージュは既存材料の機械的組合せから新しい意味を生む方法。AI生成のリミックス的本質を理論化する古典的祖型。",
         "related_ai_phenomenon":"AI生成のリミックス的構造"}])

add(**C, name_ja="ポリフォニー（バフチン）",
    name_en="polyphony (Bakhtin)",
    name_original="полифония / Polyphonie",
    definition="ミハイル・バフチン（1895-1975）が『ドストエフスキーの詩学の問題』(1929/1963)で理論化した小説論的概念。複数の自律的「声」が作者視点に統合されず並存する小説構造を意味する。ドストエフスキー長編をモデルとし、トルストイ独白型リアリズムの対極として20世紀小説論の中心類型となった。",
    background="ロシア・フォルマリズム（シクロフスキー）、ヤコブソン言語学、1920年代ロシア前衛文学理論圏。",
    development="フランス受容（クリステヴァ「ポリフォニーとインターテクスチュアリティ」、1967年仏語訳）、20世紀後半の文学理論の中心概念となった。",
    historical_context="ロシア革命後の文学理論興隆と、スターリン期検閲下のバフチンの隠遁的著述活動。",
    primary_source_url=WIKI_EN+"Polyphony_(literature)",
    primary_source_type="Wikipedia: Polyphony (literature) / Bakhtin",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PT","link_type":"shared_concept",
         "target_entity_name":"ポリフォニー・物語論",
         "description":"バフチンのポリフォニー概念は20世紀後半の物語論・対話理論の中心枠組み。"}])

add(**C, name_ja="同時性（simultanéité）",
    name_en="simultaneity",
    name_original="simultanéité",
    definition="ロベール・ドローネー絵画とアポリネール詩『地帯』(1913)、ブレーズ・サンドラール『シベリア横断鉄道とフランスの小ジャンヌの散文』(1913)で展開された前衛的時空概念。複数の時空を一つのテキスト平面に同時呈示する技法を綱領化した。キュビズム・未来派・モダニズム文学に共通する方法論的核。",
    background="アインシュタイン特殊相対性理論(1905)の文化的衝撃、キュビズム多視点絵画、未来派の動的同時性。",
    development="ジョイス『ユリシーズ』、ドス・パソス、20世紀モダニズム長編の時空構造論の中心概念となった。",
    historical_context="20世紀初頭の物理学的・哲学的時空観の文学的吸収。",
    primary_source_url=WIKI_FR+"Simultan%C3%A9isme",
    primary_source_type="Wikipedia(FR): Simultanéisme",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="長詩（モダニズム）",
    name_en="long poem (modernist)",
    name_original="modernist long poem",
    definition="エリオット『荒地』(1922)、パウンド『キャントーズ』(1915-69)、ウィリアム・カーロス・ウィリアムズ『パターソン』(1946-58)、H.D.『三部作』(1944-46)を中心ジャンルとする20世紀モダニズム詩の代表的形式。叙事詩・哲学詩・歴史詩を統合し、断片化された全体像を志向する長大な詩的構成体。",
    background="ホイットマン『草の葉』の長詩伝統、19世紀叙事詩の死、モダニズムによる長大形式の再構築。",
    development="戦後米国詩（チャールズ・オルソン『マクシマス・ポエムズ』、ロバート・ダンカン『パッセージズ』）、現代長詩への系譜的中心。",
    historical_context="20世紀における叙事詩的全体像の不可能性と、それへの長詩形式による応答。",
    primary_source_url=WIKI_EN+"Long_poem",
    primary_source_type="Wikipedia: Long poem (modernist)",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="モダニスト自伝",
    name_en="modernist autobiography",
    name_original="modernist autobiography",
    definition="ガートルード・スタイン『アリス・B・トクラスの自伝』(1933)、レオン=ポール・ファルグ『パリの歩行者』(1939)、ウォルター・ベンヤミン『1900年頃のベルリンの幼年時代』(1932-38)、ヴァージニア・ウルフ『過去のスケッチ』を代表とする、伝統的線形自伝形式を解体した自伝サブジャンル。多視点・断片化・他者の声の取り込みを技法的中心とする。",
    background="19世紀ロマン主義的自伝（ルソー『告白』）からの方法的距離化、フロイト精神分析の自伝的記憶への影響。",
    development="戦後フランス自己エクリチュール（ロラン・バルト『彼自身による』、セルジュ・ドゥブロフスキー「自伝小説」概念）に継承された。",
    historical_context="20世紀前半の自伝形式の方法的多様化と、自己と他者・記憶と現在の境界の問題化。",
    primary_source_url=WIKI_EN+"The_Autobiography_of_Alice_B._Toklas",
    primary_source_type="Wikipedia: The Autobiography of Alice B. Toklas",
    importance_score=4, source_tier="tertiary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"スタインが他者（アリス）の視点を借用して自分自身を語る構造は、AI生成における擬似的主体的視点（system promptによるペルソナ）の文学的祖型として再読される。",
         "related_ai_phenomenon":"AIにおける擬似的主体的視点の構築"}])

add(**C, name_ja="フォト・テクスト",
    name_en="photo-text",
    name_original="photo-text / Bildband",
    definition="ヴァルター・ベンヤミン『一方通行路』(1928)、ジェイムズ・エイジー＋ウォーカー・エヴァンズ『今こそ名声を讃えよう』(1941)、アンドレ・ブルトン『ナジャ』(1928、写真挿絵付)を代表とする、写真と文字テキストを統合する20世紀前衛ジャンル。新興メディア（写真・印刷）の前衛文学への統合を象徴する。",
    background="20世紀前半の写真技術の大衆化、雑誌グラビアの興隆、ブルトン・ベンヤミンらのメディア論的関心。",
    development="戦後フォトジャーナリズム、視覚詩、現代のグラフィックノベル・ノンフィクション写真集に継承された。",
    historical_context="戦間期のメディア混淆実験と、文字と画像の境界の問題化。",
    primary_source_url=WIKI_EN+"Photo-essay",
    primary_source_type="Wikipedia: Photo-essay (modernist)",
    importance_score=3, source_tier="tertiary", canonical_in_region="minor",
    cross_domain=[
        {"target_db":"AI-Development","link_type":"shared_concept",
         "target_entity_name":"マルチモーダル生成",
         "description":"フォト・テクストは画像と文字を統合する文学的祖型として、現代マルチモーダルAI生成の理論的参照点。"}])


# ============================================================
# D: モダニズム作家I（独・墺・伊・葡・西）— 8件
# ============================================================
add(**C, name_ja="リルケ『ドゥイノの悲歌』",
    name_en="Rilke's Duineser Elegien",
    name_original="Duineser Elegien",
    definition="ライナー・マリア・リルケ（1875-1926）が1912-22年にかけて書き継ぎ1923年に発表した10編連作長詩。ドゥイノ城（アドリア海）滞在中に着想され、第一次世界大戦による中断を経て、ミュゾット城（スイス）で完成した。天使・恋人・死・幼年期・賞讃を主題とする20世紀独語詩の頂点を成す作品。",
    background="リルケのパリ・ロダン秘書時代（1905-06）、ドゥイノ城滞在(1911-12)、第一次世界大戦体験、戦後の文学的孤独。",
    development="20世紀後半の独語詩（ツェラン、バッハマン）、ハイデガー詩論（『リルケについて』）、世界詩学の中心参照点となった。",
    historical_context="第一次世界大戦前後の独語詩の方法的革新期と、戦間期の存在論的詩学。",
    primary_source_url=WSRC_DE+"Duineser_Elegien",
    primary_source_type="Wikisource(DE): Duineser Elegien",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ペソアの異名（heterônimos）",
    name_en="Pessoa's heteronyms",
    name_original="heterônimos de Pessoa",
    definition="フェルナンド・ペソア（1888-1935）が展開した独自の文学的方法。アルベルト・カエイロ、リカルド・レイス、アルヴァロ・デ・カンポスをはじめ、各々独立した伝記・詩風・哲学を持つ70余の「異名」を創造し、それぞれの名で詩・散文を書き分けた。「私の中の他者性の演劇」と自ら呼んだこの方法は、20世紀文学における主体・作家性概念に根本的問題を提起した。",
    background="ペソアの英国教育（南アフリカ）背景、20世紀前半リスボン文学界の周縁的位置、ペッソア独自の精神的構造。",
    development="ペソア『不安の書』(1982年初版)発見以降、20世紀後半の世界文学の中心作家として再評価された。20世紀後半・21世紀の作家性論の中心研究対象。",
    historical_context="20世紀前半リスボンの文化的孤立と、ペソアの生前ほぼ無名の状態。",
    primary_source_url=WIKI_PT+"Heter%C3%B4nimos_de_Fernando_Pessoa",
    primary_source_type="Wikipedia(PT): Heterônimos de Pessoa",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ペソアの異名は単一作者主体を複数の自律的人格に分裂させる方法を実践する。AI時代におけるシステムプロンプト・ペルソナ生成・複数AIエージェントの文学的祖型として根本的参照点。",
         "related_ai_phenomenon":"AIにおけるペルソナ生成・マルチエージェント"},
        {"axis":"主体","status":"rethinking",
         "rationale":"異名は主体の単一性を文学的に解体する。AI生成における主体不在・複数化と理論的に深く共振する。",
         "related_ai_phenomenon":"AI生成における主体の複数化と解体"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"異名による作品はペソアの「真正な」声か、独立した「他者」の声か。AI生成テキストの真正性問題の文学的祖型。",
         "related_ai_phenomenon":"AI生成テキストの真正性問題"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"主体の複数性",
         "description":"ペソアの異名は主体の複数性・分裂を文学的に実践し、20世紀以降の主体論の重要事例。"}])

add(**C, name_ja="ロルカのドゥエンデ",
    name_en="Lorca's duende",
    name_original="duende",
    definition="フェデリコ・ガルシア・ロルカ（1898-1936）が1933年講演「ドゥエンデの理論と遊戯」で理論化した、アンダルシア民俗芸能の中核概念の文学化。「血と魂を上昇させる神秘的力」「踵から登ってくる暗い力」として、ミューズ・天使と区別される第三の創造原理を意味する。フラメンコ・闘牛・ジプシー詩を範とし、20世紀詩学に独自の身体的・暗黒的次元を導入した。",
    background="アンダルシア民俗文化の継承、ニューヨーク滞在(1929-30)、ハバナ滞在(1930)体験、スペイン共和制期の文化的緊張。",
    development="ニック・ケイヴ、レオナード・コーエン等20世紀後半の世界詩・歌詞文化の中心概念となった。",
    historical_context="スペイン第二共和制期(1931-39)の文化的多様性と、内戦期の前衛文化弾圧（ロルカは1936年フランコ派民兵により銃殺）。",
    primary_source_url=WIKI_ES+"Teor%C3%ADa_y_juego_del_duende",
    primary_source_type="Wikipedia(ES): Teoría y juego del duende",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ムージル『特性のない男』",
    name_en="Musil's Der Mann ohne Eigenschaften",
    name_original="Der Mann ohne Eigenschaften",
    definition="ローベルト・ムージル（1880-1942）が1930-43年に三部刊行した未完長編小説。1913年「カカニア」（ハプスブルク帝国）を舞台に、主人公ウルリヒの「特性のない」存在様式を中核に、近代主体・科学・愛・神秘主義の問題を巨大な思索的構造で展開する。20世紀ヨーロッパ哲学小説の最高峰の一つ。",
    background="ハプスブルク帝国末期ウィーン文化（マッハ、フロイト、ヴィトゲンシュタイン）、ムージルの工学・哲学博士的訓練、戦後オーストリア・ナチス迫害体験。",
    development="20世紀後半の哲学小説（ザーセス『書記バートルビー』論）、ハーバーマス・モダニティ論の中心参照点となった。",
    historical_context="ハプスブルク末期の文化的崩壊と、その文学的全体像化の試み。",
    primary_source_url=WIKI_DE+"Der_Mann_ohne_Eigenschaften",
    primary_source_type="Wikipedia(DE): Der Mann ohne Eigenschaften",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"近代主体の問題",
         "description":"ムージルの「特性のない男」は20世紀近代主体論の文学的中心事例。"}])

add(**C, name_ja="ブロッホ『夢遊の人々』",
    name_en="Broch's Die Schlafwandler",
    name_original="Die Schlafwandler",
    definition="ヘルマン・ブロッホ（1886-1951）が1931-32年に発表した三部作長編小説。『パセノウ、あるいは浪漫主義 1888年』『エシュ、あるいは無政府主義 1903年』『ユグノー、あるいは即物主義 1918年』からなり、ヴィルヘルム期からヴァイマール期に至る独語圏「価値崩壊」の歴史を、それぞれ異なる文学様式で描く。20世紀独語哲学小説の代表作。",
    background="ハプスブルク末期ウィーン哲学圏（フッサール現象学受容）、戦間期独語小説の方法的革新期、ナチス迫害体験（1938年米国亡命）。",
    development="20世紀後半の歴史哲学小説、ハンナ・アーレント・ジョージ・スタイナー等の批評の中心対象となった。",
    historical_context="戦間期独語圏の歴史的全体性把握への文学的応答。",
    primary_source_url=WIKI_DE+"Die_Schlafwandler_(Broch)",
    primary_source_type="Wikipedia(DE): Die Schlafwandler",
    importance_score=4, source_tier="secondary", canonical_in_region="major")

add(**C, name_ja="デーブリン『ベルリン・アレクサンダー広場』",
    name_en="Döblin's Berlin Alexanderplatz",
    name_original="Berlin Alexanderplatz",
    definition="アルフレート・デーブリン（1878-1957）が1929年に発表した長編小説。元囚人フランツ・ビーバーコップのベルリン下層社会での運命を、新聞見出し・歌・聖書・職業統計・モンタージュ的散文で描く。ジョイス『ユリシーズ』に並ぶ20世紀都市小説の頂点を成し、独語モダニズム長編の代表作。",
    background="ヴァイマール期ベルリンの大都市文化、ジョイス『ユリシーズ』(1922年独語訳1927)の影響、デーブリンの神経精神科医としての経験。",
    development="ファスビンダー15時間TVシリーズ(1980)、20世紀都市文学・モンタージュ文学の中心参照点となった。",
    historical_context="ヴァイマール期ベルリンの大都市的近代性と、ナチス政権成立(1933)前の文化的高揚期。",
    primary_source_url=WIKI_DE+"Berlin_Alexanderplatz",
    primary_source_type="Wikipedia(DE): Berlin Alexanderplatz",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="スヴェーヴォ『ゼーノの意識』",
    name_en="Svevo's La coscienza di Zeno",
    name_original="La coscienza di Zeno",
    definition="イタロ・スヴェーヴォ（エットレ・シュミッツ、1861-1928）が1923年に発表した長編小説。トリエステを舞台に、主人公ゼーノ・コジーニが精神分析医に提出する自伝的手記の形式で、禁煙・父・妻・愛人・第一次世界大戦を語る。ジェイムズ・ジョイス（トリエステ滞在時の英語教師）の支援で世界的名声を得た、独墺・伊融合圏の代表作。",
    background="トリエステの独墺・伊融合圏（ハプスブルク領→1919年伊領）、フロイト精神分析のスヴェーヴォによる早期受容、ジョイスとの友情。",
    development="20世紀後半のイタリア小説（カルヴィーノ、ギンツブルグ）、世界モダニズムの中心参照点となった。",
    historical_context="ハプスブルク末期トリエステ文化と、第一次世界大戦後の中欧文学的再編。",
    primary_source_url=WIKI_IT+"La_coscienza_di_Zeno",
    primary_source_type="Wikipedia(IT): La coscienza di Zeno",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    fourth_axes=[
        {"axis":"主体","status":"rethinking",
         "rationale":"スヴェーヴォの自己分析的語り手は、フロイト精神分析を文学的方法に転化する。AI生成における主体の自己記述（self-reflection prompt）の文学的祖型。",
         "related_ai_phenomenon":"AIにおける自己反省的記述"}])

add(**C, name_ja="ランペドゥーザ『山猫』",
    name_en="Lampedusa's Il Gattopardo",
    name_original="Il Gattopardo",
    definition="ジュゼッペ・トマーゾ・ディ・ランペドゥーザ（1896-1957）が1955-56年に執筆し、死後1958年に出版された長編小説。19世紀後半シチリア貴族サリーナ家公爵の没落を、リソルジメント期から19世紀末に至る歴史的変動の中に位置づける。「すべてが変わるためには、すべてが現状維持されなければならない」という有名な逆説で、近代化と保守の弁証法を文学的に結晶化させた。",
    background="ランペドゥーザのシチリア貴族家系、戦後イタリアの貴族階級没落、マンゾーニ『婚約者』伝統との関係。",
    development="ヴィスコンティ映画版(1963)、20世紀後半イタリア歴史小説の中心参照点となった。",
    historical_context="戦後イタリア（特に南部）の文化的近代化期と、貴族階級の歴史的退場。",
    primary_source_url=WIKI_IT+"Il_Gattopardo",
    primary_source_type="Wikipedia(IT): Il Gattopardo",
    importance_score=4, source_tier="secondary", canonical_in_region="major")


# ============================================================
# E: モダニズム作家II（英・米・南米・ジャンル）— 8件
# ============================================================
add(**C, name_ja="エリオット『荒地』系譜",
    name_en="Eliot's Waste Land genealogy",
    name_original="The Waste Land genealogy",
    definition="T・S・エリオット（1888-1965）が1922年に発表した長詩『荒地』の方法的・主題的系譜。ジェシー・L・ウェストン『祭祀からロマンスへ』(1920)、フレイザー『金枝篇』、フランス象徴派（ボードレール、ラフォルグ）、東洋宗教（仏教・ヒンドゥー教）、英文学伝統（シェイクスピア、ダンテ）を統合した「断片的な伝統総合」の方法を確立。20世紀英米モダニズム詩の決定的転換点。",
    background="第一次世界大戦後ヨーロッパ精神的危機、エリオットの神経衰弱、エズラ・パウンドによる原稿の徹底編集。",
    development="20世紀後半英米詩学（新批評、デコンストラクション）、世界モダニズム詩の中心参照点となった。",
    historical_context="第一次世界大戦後の文化的全体崩壊感覚と、文学による断片総合の試み。",
    primary_source_url=WSRC_EN+"The_Waste_Land",
    primary_source_type="Wikisource: The Waste Land (1922)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"『荒地』は無数の引用織物で構成される。AI生成テキストの学習データ再構成と方法的に深く類比する古典的祖型。",
         "related_ai_phenomenon":"AI生成における引用織物的構造"}])

add(**C, name_ja="ガートルード・スタイン",
    name_en="Gertrude Stein",
    name_original="Gertrude Stein",
    definition="ガートルード・スタイン（1874-1946）は米国出身パリ在住の前衛作家。『軟らかいボタン』(1914)、『アメリカ人の形成』(1925)、『アリス・B・トクラスの自伝』(1933)等で、反復・循環・連続的現在（continuous present）を中心方法とする独自の散文を確立。20世紀英語前衛文学の中心人物。",
    background="ハーバード大学心理学（ウィリアム・ジェイムズ門下）、パリ・ピカソ・マチス交友圏、レズビアン共同体（パートナー、アリス・B・トクラス）。",
    development="米国前衛詩（ラングエッジ・ポエトリー）、20世紀後半フェミニスト前衛文学の中心源流となった。",
    historical_context="戦間期パリの英米前衛文学集結（ロスト・ジェネレーション）、レフトバンク文化。",
    primary_source_url=GUTEN+"author/582",
    primary_source_type="Project Gutenberg: Gertrude Stein",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"スタインの反復・循環的散文は、意味より言語の物質性を前景化する。生成AIの確率的反復生成の文学的祖型。",
         "related_ai_phenomenon":"AI生成における反復的構造"}])

add(**C, name_ja="イェイツの神秘体系（A Vision）",
    name_en="Yeats's A Vision system",
    name_original="A Vision",
    definition="W・B・イェイツ（1865-1939）が1925年（改訂1937）に発表した独自の神秘哲学体系。妻ジョージィの自動筆記から得た資料を基に、月の28相による人格類型・歴史循環・霊魂論を体系化した。後期詩集『塔』(1928)、『螺旋階段』(1933)等の方法的背景を成し、20世紀前半英語詩における神秘主義と前衛の融合を象徴する。",
    background="アイルランド神智学運動（ブラヴァツキー・ベサント）、黄金の夜明け教団員時代、妻ジョージィとの神秘体験(1917)。",
    development="20世紀後半神秘主義文学（ラルフ・エリソン、ピンチョン）への系譜的影響、イェイツ批評の中心研究対象となった。",
    historical_context="アイルランド独立期(1922)前後の文化的混乱と、神秘主義による歴史哲学的応答。",
    primary_source_url=WIKI_EN+"A_Vision",
    primary_source_type="Wikipedia: A Vision (Yeats)",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フォークナーのヨクナパトーファ・サーガ",
    name_en="Faulkner's Yoknapatawpha saga",
    name_original="Yoknapatawpha saga",
    definition="ウィリアム・フォークナー（1897-1962）が『サートリス』(1929)以降、『響きと怒り』(1929)、『サンクチュアリ』(1931)、『八月の光』(1932)、『アブサロム、アブサロム！』(1936)等で構築した架空のミシシッピ州ヨクナパトーファ郡を舞台にする小説連環。米国南部の人種・歴史・没落を、意識流・複数視点・時間錯綜の方法で描く20世紀米国文学の頂点。",
    background="米国南部再建期以降の文化的・人種的緊張、フォークナーの故郷オックスフォード（ミシシッピ州）の歴史、ジョイス・コンラッドの方法的影響。",
    development="20世紀ラテンアメリカ文学（ガルシア・マルケス『百年の孤独』マコンド設定の祖型）、世界の地方サーガ文学に深い影響を与えた。",
    historical_context="戦間期米国南部の文化的後発性と、それを世界文学的方法で記述する試み。",
    primary_source_url=WIKI_EN+"Yoknapatawpha_County",
    primary_source_type="Wikipedia: Yoknapatawpha County",
    importance_score=5, source_tier="secondary", canonical_in_region="core")

add(**C, name_ja="ヘミングウェイの氷山理論",
    name_en="Hemingway's iceberg theory",
    name_original="iceberg theory",
    definition="アーネスト・ヘミングウェイ（1899-1961）が『午後の死』(1932)で「省略の理論」として説明し、後に「氷山理論（iceberg theory）」として知られるようになった文体論的方法。物語の表面に現れる部分（氷山の8分の1）の下に、意図的に省略された巨大な意味（残り8分の7）を読者の感受性に委ねる方法。フローベール「正確な言葉」の20世紀米国版継承。",
    background="第一次世界大戦経験（イタリア戦線負傷1918）、ロスト・ジェネレーション期パリ滞在（1921-26）、フローベール・モーパッサン・スタインからの方法的継承。",
    development="20世紀後半米国短編小説（レイモンド・カーヴァー、トバイアス・ウルフ）、世界のミニマリズム小説の中心方法論となった。",
    historical_context="戦間期米国前衛文学のパリ集結期と、フランス・リアリズム遺産の英語圏継承。",
    primary_source_url=WIKI_EN+"Iceberg_theory",
    primary_source_type="Wikipedia: Iceberg theory (Hemingway)",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"言語","status":"rethinking",
         "rationale":"氷山理論は省略・暗示を文学方法の中核に据える。AI生成における過剰説明傾向と根本的に対立する文学的精神の参照点。",
         "related_ai_phenomenon":"AI生成の過剰説明傾向 vs 暗示的省略の美学"}])

add(**C, name_ja="ボルヘスの原ポストモダン詩学",
    name_en="Borges's proto-postmodern poetics",
    name_original="poética protoposmoderna",
    definition="ホルヘ・ルイス・ボルヘス（1899-1986）が『フィクシオネス』(1944)、『アレフ』(1949)等で展開した短編小説の方法。架空の書物・著者・百科事典を実在のものとして扱う「擬書物」、迷宮・図書館・無限・分岐の主題、メタフィクション的自己言及を統合し、20世紀後半ポストモダン文学の祖型を提供した。",
    background="ブエノスアイレスの英語・スペイン語二重文化、20世紀前半ヨーロッパ滞在体験（スイス、スペイン）、家系図書館への没入。",
    development="20世紀後半ラテンアメリカ・ブーム（ガルシア・マルケス、コルタサル）、英米ポストモダン文学（バース、バーセルミ、エーコ）の決定的祖型となった。",
    historical_context="20世紀前半アルゼンチン文学の世界文学への参入と、ペロン政権下の文化的緊張。",
    primary_source_url=WIKI_ES+"Jorge_Luis_Borges",
    primary_source_type="Wikipedia(ES): Jorge Luis Borges",
    importance_score=5, source_tier="secondary", canonical_in_region="core",
    fourth_axes=[
        {"axis":"作者性","status":"rethinking",
         "rationale":"ボルヘスの「擬書物」「擬著者」は実在しない作家・著作を文学的に実装する方法。AIによる擬似引用・幻覚（hallucination）の文学的祖型として根本的参照点。",
         "related_ai_phenomenon":"AIの幻覚（hallucination）と擬似引用"},
        {"axis":"真正性","status":"rethinking",
         "rationale":"ボルヘスは存在しないものを実在として記述する文学的方法を確立した。AI生成テキストの真正性問題の根源的祖型。",
         "related_ai_phenomenon":"AI生成における真正性なき実在化"}],
    cross_domain=[
        {"target_db":"PHIL","link_type":"shared_concept",
         "target_entity_name":"擬書物・実在の論理学",
         "description":"ボルヘスの擬書物は20世紀後半の存在論・実在論哲学（メイヤスー、ハーマン）の重要参照点。"}])

add(**C, name_ja="モダニスト・マニフェスト",
    name_en="modernist manifesto",
    name_original="modernist manifesto",
    definition="マリネッティ未来派宣言(1909)、アポリネール『新精神と詩人たち』(1918)、ツァラ・ダダ宣言(1918)、ブルトン・シュルレアリスム宣言(1924)、ルイス『ブラスト』(1914)、パウンド「3つのドント」(1913)等を中心とする、20世紀前衛運動が制度化した文学ジャンル。芸術綱領を簡潔・断定的・挑発的散文形式で表明する技法を綱領化した。",
    background="19世紀末の芸術運動の制度化（クールベ「リアリズム宣言」1855）、新聞・雑誌メディアの興隆、20世紀前衛運動の急速な国際化。",
    development="20世紀政治宣言（共産党宣言、独立宣言の文学的伝統）と前衛芸術宣言の融合。21世紀のテック宣言（ハッカー宣言、加速主義宣言）にも継承。",
    historical_context="20世紀前衛運動の制度化期と、宣言文学（manifesto）ジャンルの誕生。",
    primary_source_url=WIKI_EN+"Manifesto#Art_manifestos",
    primary_source_type="Wikipedia: Art manifestos",
    importance_score=4, source_tier="tertiary", canonical_in_region="major")

add(**C, name_ja="構成主義文学（ロシア）",
    name_en="Russian Constructivist literature",
    name_original="конструктивизм",
    definition="1920年代ソヴィエト連邦で展開された前衛芸術運動の文学版。イリヤ・セリヴィンスキー、ヴェラ・インベル、エドゥアルド・バグリツキー等の文学構成主義者連盟（ЛЦК、1923-30）を中心に、文学を「構築物（конструкция）」として理論化し、機能性・科学性・社会的目的性を中心理念とした。視覚芸術構成主義（タトリン、ロトチェンコ）と並行。",
    background="ロシア革命後の前衛芸術と社会主義建設の同期化、ロシア・フォルマリズム（シクロフスキー、ヤコブソン）の理論的支援、生産芸術論（プロイエクト主義）。",
    development="スターリン期社会主義リアリズム成立(1934)以降、構成主義は弾圧・解体された。20世紀後半再評価が進み、1980年代ロシア・ポスト構造主義の重要参照点となった。",
    historical_context="ロシア革命後の前衛・革命同期期(1917-1929)と、その後のスターリン主義による解体。",
    primary_source_url=WIKI_RU+"%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%B8%D0%B2%D0%B8%D0%B7%D0%BC_(%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0)",
    primary_source_type="Wikipedia(RU): Конструктивизм (литература)",
    importance_score=3, source_tier="secondary", canonical_in_region="minor")


# ============================================================
# Main runner
# ============================================================
def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        # Look up existing period 'モダニズム期' (id=22)
        cur = db.conn.execute(
            "SELECT id FROM periods WHERE name_ja = ? AND region = ?",
            (PERIOD_KEY, "西欧"))
        row = cur.fetchone()
        if not row:
            print(f"[error] period '{PERIOD_KEY}' not found in DB")
            return 1
        period_id = row[0]

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            entry.pop("period_key", None)
            entry["period_id"] = period_id
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
        print(f"[c10-add40] inserted concepts (this run): {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[c10-add40] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
