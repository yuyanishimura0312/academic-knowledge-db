"""DUA Wave A2 Batch 10 — 古典学・宗教学・文学批評・美学・歴史学 補強 (~280 entries)"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def uid(): return "dua_" + uuid.uuid4().hex[:12]

RECORDS = [
# ── 古典学・古典文学 補強 (~80 entries) ──
(uid(),"ヒポクラテス全集","Hippocratic Corpus","古代ギリシアの医学文献集。古代医学の根本資料。","古典学・古典文学","Western_Europe",-400,"https://en.wikipedia.org/wiki/Hippocratic_Corpus",now,now),
(uid(),"ガレノス医学","Galenic medicine","古代ローマの医師ガレノスの医学体系。中世まで権威を持った。","古典学・古典文学","Western_Europe",129,"https://en.wikipedia.org/wiki/Galen",now,now),
(uid(),"プルタルコス列伝","Parallel Lives","古代の英雄・政治家の伝記集。道徳的人物像を描く。","古典学・古典文学","Western_Europe",100,"https://en.wikipedia.org/wiki/Parallel_Lives",now,now),
(uid(),"アエネーイス","Aeneid","ウェルギリウスによるローマ建国叙事詩。ホメロスに倣う。","古典学・古典文学","Western_Europe",-29,"https://en.wikipedia.org/wiki/Aeneid",now,now),
(uid(),"変身物語","Metamorphoses (Ovid)","オウィディウスによる神話変身譚集。西洋文学に多大な影響。","古典学・古典文学","Western_Europe",8,"https://en.wikipedia.org/wiki/Metamorphoses_(Ovid)",now,now),
(uid(),"リウィウス歴史","Ab Urbe Condita","ローマ史家リウィウスによるローマ建国史。全142巻。","古典学・古典文学","Western_Europe",-27,"https://en.wikipedia.org/wiki/Ab_Urbe_Condita_Libri",now,now),
(uid(),"タキトゥス年代記","Annals (Tacitus)","ローマ帝政期を記録したタキトゥスの歴史書。","古典学・古典文学","Western_Europe",117,"https://en.wikipedia.org/wiki/Annals_(Tacitus)",now,now),
(uid(),"スエトニウス皇帝伝","Lives of the Twelve Caesars","ローマ皇帝の伝記集。スキャンダラスな記述で知られる。","古典学・古典文学","Western_Europe",121,"https://en.wikipedia.org/wiki/The_Twelve_Caesars",now,now),
(uid(),"キケロ修辞学","Cicero's rhetorical works","古代ローマの政治家キケロによる修辞学・哲学著作群。","古典学・古典文学","Western_Europe",-55,"https://en.wikipedia.org/wiki/Cicero",now,now),
(uid(),"セネカ悲劇","Senecan tragedy","ストア哲学者セネカによるラテン語悲劇。復讐と運命を主題とする。","古典学・古典文学","Western_Europe",54,"https://en.wikipedia.org/wiki/Senecan_tragedy",now,now),
(uid(),"マルクス・アウレリウス自省録","Meditations (Marcus Aurelius)","ストア哲学の実践を記したローマ皇帝の個人日誌。","古典学・古典文学","Western_Europe",161,"https://en.wikipedia.org/wiki/Meditations",now,now),
(uid(),"プロティノスのエネアデス","Enneads","新プラトン主義哲学者プロティノスの著作集。","古典学・古典文学","Western_Europe",270,"https://en.wikipedia.org/wiki/Enneads",now,now),
(uid(),"ユスティニアヌス法典","Corpus Juris Civilis","東ローマ皇帝が編纂した古代ローマ法の集大成。","古典学・古典文学","Western_Europe",529,"https://en.wikipedia.org/wiki/Corpus_Juris_Civilis",now,now),
(uid(),"ベーオウルフ","Beowulf","古英語の叙事詩。北欧神話的世界観を描く中世英文学の礎。","古典学・古典文学","Western_Europe",700,"https://en.wikipedia.org/wiki/Beowulf",now,now),
(uid(),"ニーベルンゲンの歌","Nibelungenlied","中高ドイツ語の英雄叙事詩。ジークフリート伝説を中心とする。","古典学・古典文学","Western_Europe",1200,"https://en.wikipedia.org/wiki/Nibelungenlied",now,now),
(uid(),"ロランの歌","Song of Roland","フランス中世最古の武勲詩。シャルルマーニュ軍の勇士を讃える。","古典学・古典文学","Western_Europe",1040,"https://en.wikipedia.org/wiki/The_Song_of_Roland",now,now),
(uid(),"エッダ詩","Poetic Edda","北欧神話・英雄伝説を記した古ノルド語詩集。","古典学・古典文学","Western_Europe",1220,"https://en.wikipedia.org/wiki/Poetic_Edda",now,now),
(uid(),"スカルド詩","Skaldic poetry","ヴァイキング時代の宮廷詩人が詠んだ複雑韻律の詩。","古典学・古典文学","Western_Europe",850,"https://en.wikipedia.org/wiki/Skaldic_poetry",now,now),
(uid(),"パリ写本文化","Paris manuscript culture","中世パリの写字室文化。神学・哲学著作の保存と流通の拠点。","古典学・古典文学","Western_Europe",1100,"https://en.wikipedia.org/wiki/Medieval_manuscript",now,now),
(uid(),"ビザンツ文学","Byzantine literature","東ローマ帝国時代のギリシア語文学。古典の保存と宗教文学。","古典学・古典文学","Western_Europe",330,"https://en.wikipedia.org/wiki/Byzantine_literature",now,now),
(uid(),"バガヴァッド・ギーター","Bhagavad Gita","マハーバーラタの一部をなすヒンドゥー哲学詩。クリシュナとアルジュナの対話。","古典学・古典文学","South_Asia",-400,"https://en.wikipedia.org/wiki/Bhagavad_Gita",now,now),
(uid(),"マハーバーラタ","Mahabharata","古代インドのサンスクリット叙事詩。世界最長の叙事詩のひとつ。","古典学・古典文学","South_Asia",-400,"https://en.wikipedia.org/wiki/Mahabharata",now,now),
(uid(),"ラーマーヤナ","Ramayana","ヴァールミーキによるサンスクリット叙事詩。ラーマ王子の物語。","古典学・古典文学","South_Asia",-500,"https://en.wikipedia.org/wiki/Ramayana",now,now),
(uid(),"カーリダーサ詩学","Kalidasa","古代インドの詩人劇作家。シャクンタラーなど古典サンスクリット文学の頂点。","古典学・古典文学","South_Asia",400,"https://en.wikipedia.org/wiki/Kalidasa",now,now),
(uid(),"パーリ語三蔵","Pali Canon","上座部仏教の聖典。パーリ語で記された最古の仏典集成。","古典学・古典文学","South_Asia",-250,"https://en.wikipedia.org/wiki/P%C4%81li_Canon",now,now),
(uid(),"詩経","Classic of Poetry","中国最古の詩集。305篇の詩を収録し儒教五経の一つ。","古典学・古典文学","East_Asia",-1000,"https://en.wikipedia.org/wiki/Classic_of_Poetry",now,now),
(uid(),"楚辞","Songs of Chu","中国古代南方の詩集。屈原作離騒など幻想的詩風。","古典学・古典文学","East_Asia",-300,"https://en.wikipedia.org/wiki/Chuci",now,now),
(uid(),"漢賦","Han fu","漢代の宮廷文学様式。華麗な修辞で宮殿・狩猟を詠む。","古典学・古典文学","East_Asia",-200,"https://en.wikipedia.org/wiki/Fu_(literature)",now,now),
(uid(),"唐詩","Tang poetry","中国唐代の詩文化。李白・杜甫・王維ら大詩人を輩出した。","古典学・古典文学","East_Asia",618,"https://en.wikipedia.org/wiki/Tang_poetry",now,now),
(uid(),"宋詞","Song ci","宋代の歌詞文学。音楽と連動した新しい詩型として発達した。","古典学・古典文学","East_Asia",960,"https://en.wikipedia.org/wiki/Ci_(poetry)",now,now),
(uid(),"古事記","Kojiki","日本最古の歴史書。神話・歌謡・系譜を含む。","古典学・古典文学","East_Asia",712,"https://en.wikipedia.org/wiki/Kojiki",now,now),
(uid(),"土左日記","Tosa Diary","紀貫之による日本最初の仮名日記文学。女性に仮託した旅日記。","古典学・古典文学","East_Asia",935,"https://en.wikipedia.org/wiki/Tosa_Diary",now,now),
(uid(),"大和物語","Yamato Monogatari","平安時代の歌物語集。和歌と散文が融合した短篇集。","古典学・古典文学","East_Asia",951,"https://en.wikipedia.org/wiki/Yamato_Monogatari",now,now),
(uid(),"和漢朗詠集","Wakan Roeishu","藤原公任編の和漢詩文集。日本と中国の詩句を集成した。","古典学・古典文学","East_Asia",1013,"https://en.wikipedia.org/wiki/Wakan_r%C5%8Dei_sh%C5%AB",now,now),
(uid(),"エピック・オブ・ギルガメシュ","Epic of Gilgamesh","メソポタミアの古代叙事詩。世界最古の文学作品のひとつ。","古典学・古典文学","West_Asia_North_Africa",-2100,"https://en.wikipedia.org/wiki/Epic_of_Gilgamesh",now,now),
(uid(),"アラビアンナイト","One Thousand and One Nights","アラビア語の民話集。世界各地の説話を集めた文学的集積。","古典学・古典文学","West_Asia_North_Africa",800,"https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights",now,now),
(uid(),"ルバイヤート","Rubaiyat of Omar Khayyam","ペルシア詩人ハイヤームの四行詩集。快楽主義と無常感を歌う。","古典学・古典文学","West_Asia_North_Africa",1048,"https://en.wikipedia.org/wiki/Rubaiyat_of_Omar_Khayyam",now,now),
(uid(),"シャーナーメ","Shahnameh","フェルドウスィーによるペルシア叙事詩。イラン民族の英雄伝説。","古典学・古典文学","West_Asia_North_Africa",1010,"https://en.wikipedia.org/wiki/Shahnameh",now,now),
(uid(),"タルムード","Talmud","ユダヤ法・倫理の集大成。ミシュナとゲマラから成る聖典。","古典学・古典文学","West_Asia_North_Africa",500,"https://en.wikipedia.org/wiki/Talmud",now,now),
(uid(),"グリオ伝統","Griot tradition","西アフリカの口承詩人・音楽家。歴史・系譜・物語を担う。","古典学・古典文学","Sub_Saharan_Africa",700,"https://en.wikipedia.org/wiki/Griot",now,now),
(uid(),"オリキ詩","Oriki","ヨルバ族の讃美詩・系譜詩。個人・家族・神格を讃える口承詩。","古典学・古典文学","Sub_Saharan_Africa",800,"https://en.wikipedia.org/wiki/Oriki",now,now),
(uid(),"ポポル・ヴフ","Popol Vuh","マヤ・キチェー族の創世神話書。マヤ文明の宇宙観を記す。","古典学・古典文学","Latin_America",-300,"https://en.wikipedia.org/wiki/Popol_Vuh",now,now),
(uid(),"ケチュア詩","Quechua poetry","インカ帝国および現代の詩歌。アンデスの口承と書記文化。","古典学・古典文学","Latin_America",1400,"https://en.wikipedia.org/wiki/Quechua_literature",now,now),
# 古典学追加
(uid(),"ラテン語文法","Latin grammar","古典ラテン語の文法体系。ドナトゥスとプリスキアヌスが基礎を確立した。","古典学・古典文学","Western_Europe",400,"https://en.wikipedia.org/wiki/Latin_grammar",now,now),
(uid(),"スコラ哲学ラテン語","Scholastic Latin","中世スコラ哲学で使われた学術ラテン語。神学・哲学議論の媒体。","古典学・古典文学","Western_Europe",1100,"https://en.wikipedia.org/wiki/Scholasticism",now,now),
(uid(),"ペトラルカのソネット","Petrarchan sonnet","ペトラルカが完成した14行詩形式。ヨーロッパ恋愛詩の原型となった。","古典学・古典文学","Western_Europe",1340,"https://en.wikipedia.org/wiki/Petrarchan_sonnet",now,now),
(uid(),"ダンテ神曲","Divine Comedy","ダンテ・アリギエーリのイタリア語叙事詩。地獄・煉獄・天国の旅を描く。","古典学・古典文学","Western_Europe",1320,"https://en.wikipedia.org/wiki/Divine_Comedy",now,now),
(uid(),"ボッカチオデカメロン","Decameron","ボッカチオによる100話の短篇集。ペスト禍を逃れた若者の物語。","古典学・古典文学","Western_Europe",1353,"https://en.wikipedia.org/wiki/The_Decameron",now,now),
(uid(),"イリアスの注釈伝統","Homeric commentary tradition","古代から続くホメロス解釈の伝統。アレクサンドリア図書館での校訂が起点。","古典学・古典文学","Western_Europe",-200,"https://en.wikipedia.org/wiki/Homeric_scholarship",now,now),
(uid(),"ピンダロス頌歌","Pindaric ode","古代ギリシアのピンダロスが作った勝利を讃える合唱詩。ダクテュル六歩格と異なる。","古典学・古典文学","Western_Europe",-470,"https://en.wikipedia.org/wiki/Pindar",now,now),
(uid(),"サッポー詩","Sappho's poetry","古代ギリシアの女性詩人サッポーによる個人的感情・愛を歌う抒情詩。","古典学・古典文学","Western_Europe",-600,"https://en.wikipedia.org/wiki/Sappho",now,now),
(uid(),"アリストファネス喜劇","Aristophanic comedy","古代アテネの喜劇作家アリストファネスによる政治風刺・社会批評の喜劇。","古典学・古典文学","Western_Europe",-425,"https://en.wikipedia.org/wiki/Aristophanes",now,now),
(uid(),"メナンドロス新喜劇","New Comedy (Menander)","ヘレニズム期の喜劇作家メナンドロスによる市民生活・恋愛を描く喜劇。","古典学・古典文学","Western_Europe",-316,"https://en.wikipedia.org/wiki/Menander",now,now),
(uid(),"スタン詩","Stanzaic poetry of China","中国の律詩・絶句・詞など定型詩の体系。声調と押韻の規則が厳密。","古典学・古典文学","East_Asia",618,"https://en.wikipedia.org/wiki/Regulated_verse",now,now),
(uid(),"漢字文化圏文学","Sinosphere literature","中国・日本・韓国・ベトナムにわたる漢字を共通媒体とした文学的伝統。","古典学・古典文学","East_Asia",-100,"https://en.wikipedia.org/wiki/Sinosphere",now,now),
(uid(),"ティルックラル","Tirukkural","古代タミル語の格言詩集。倫理・政治・愛を扱う南アジアの古典。","古典学・古典文学","South_Asia",-300,"https://en.wikipedia.org/wiki/Tirukkural",now,now),
(uid(),"サンガム文学","Sangam literature","古代タミル語の詩歌群。愛と戦争をテーマとする南インド最古の文学。","古典学・古典文学","South_Asia",-300,"https://en.wikipedia.org/wiki/Sangam_literature",now,now),
(uid(),"スワヒリ古典文学","Classical Swahili literature","アラビア語の影響を受けたスワヒリ語の詩・叙事詩の伝統。","古典学・古典文学","Sub_Saharan_Africa",1700,"https://en.wikipedia.org/wiki/Swahili_literature",now,now),

# ── 宗教学・神学 補強 (~70 entries) ──
(uid(),"神義論","Theodicy","神の全善・全能と悪の存在を調和させようとする神学的議論。","宗教学・神学","Western_Europe",1710,"https://en.wikipedia.org/wiki/Theodicy",now,now),
(uid(),"否定神学","Apophatic theology","神は人間の概念を超えると主張する神学方法。神について否定の形で語る。","宗教学・神学","Western_Europe",500,"https://en.wikipedia.org/wiki/Apophatic_theology",now,now),
(uid(),"プロセス神学","Process theology","ホワイトヘッドの過程哲学を基礎とする神学。神の変化可能性を主張。","宗教学・神学","North_America",1929,"https://en.wikipedia.org/wiki/Process_theology",now,now),
(uid(),"解放神学","Liberation theology","ラテンアメリカで発展した貧困者解放を中心に据えたキリスト教神学。","宗教学・神学","Latin_America",1968,"https://en.wikipedia.org/wiki/Liberation_theology",now,now),
(uid(),"フェミニスト神学","Feminist theology","女性の視点から聖典・神学・典礼を批判的に再解釈する神学。","宗教学・神学","North_America",1960,"https://en.wikipedia.org/wiki/Feminist_theology",now,now),
(uid(),"比較宗教学","Comparative religion","複数の宗教を比較研究する学問分野。マックス・ミュラーに始まる。","宗教学・神学","Western_Europe",1873,"https://en.wikipedia.org/wiki/Comparative_religion",now,now),
(uid(),"聖なるもの","The Sacred","デュルケームが宗教の本質と定義した概念。世俗と区別される神聖な領域。","宗教学・神学","Western_Europe",1912,"https://en.wikipedia.org/wiki/The_Sacred_and_the_Profane",now,now),
(uid(),"宗教現象学","Phenomenology of religion","宗教体験をフッサール現象学の方法で分析する学問。ファン・デル・レーウが代表。","宗教学・神学","Western_Europe",1933,"https://en.wikipedia.org/wiki/Phenomenology_of_religion",now,now),
(uid(),"宗教社会学","Sociology of religion","宗教を社会的現象として研究する。ウェーバー・デュルケームが基礎を築く。","宗教学・神学","Western_Europe",1897,"https://en.wikipedia.org/wiki/Sociology_of_religion",now,now),
(uid(),"宗教心理学","Psychology of religion","宗教体験・信仰・改宗を心理学的に研究する。ウィリアム・ジェームズが開拓。","宗教学・神学","North_America",1902,"https://en.wikipedia.org/wiki/Psychology_of_religion",now,now),
(uid(),"世俗化論","Secularization thesis","近代化とともに宗教の影響力が低下するという理論。ベルガーらが提唱。","宗教学・神学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Secularization",now,now),
(uid(),"宗教復興","Religious revival","宗教的熱心さが高まる歴史的・社会的現象。大覚醒など。","宗教学・神学","North_America",1730,"https://en.wikipedia.org/wiki/Religious_revival",now,now),
(uid(),"新宗教運動","New religious movement","既成宗教から分岐・独立した新興宗教団体の総称。","宗教学・神学","Global_Synthesis",1800,"https://en.wikipedia.org/wiki/New_religious_movement",now,now),
(uid(),"スピリチュアリティ研究","Spirituality studies","制度宗教に縛られない個人の精神的探求・体験の学術的研究。","宗教学・神学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Spirituality",now,now),
(uid(),"神話学","Mythology studies","神話を体系的に研究する学問。レヴィ＝ストロース・エリアーデら。","宗教学・神学","Global_Synthesis",1800,"https://en.wikipedia.org/wiki/Mythology",now,now),
(uid(),"神話の構造分析","Structural analysis of myth","レヴィ＝ストロースによる二項対立を用いた神話の構造分析法。","宗教学・神学","Western_Europe",1958,"https://en.wikipedia.org/wiki/Claude_L%C3%A9vi-Strauss",now,now),
(uid(),"古代エジプト宗教","Ancient Egyptian religion","ファラオ神性・来世信仰・多神教から成るエジプト文明の宗教体系。","宗教学・神学","West_Asia_North_Africa",-3000,"https://en.wikipedia.org/wiki/Ancient_Egyptian_religion",now,now),
(uid(),"メソポタミア宗教","Mesopotamian religion","シュメール・アッカド・バビロニアの多神教体系。","宗教学・神学","West_Asia_North_Africa",-3500,"https://en.wikipedia.org/wiki/Mesopotamian_religion",now,now),
(uid(),"グノーシス主義","Gnosticism","物質を悪とし精神的知識による救済を主張する古代宗教運動。","宗教学・神学","West_Asia_North_Africa",100,"https://en.wikipedia.org/wiki/Gnosticism",now,now),
(uid(),"マニ教","Manichaeism","3世紀にマニが創始した二元論宗教。善悪・光明と闇の対立を中核とする。","宗教学・神学","West_Asia_North_Africa",240,"https://en.wikipedia.org/wiki/Manichaeism",now,now),
(uid(),"バハーイー教","Bahai Faith","19世紀イランに起源を持つ一神教。全宗教の統一と人類の一体性を説く。","宗教学・神学","West_Asia_North_Africa",1844,"https://en.wikipedia.org/wiki/Bah%C3%A1%27%C3%AD_Faith",now,now),
(uid(),"ヴォードゥー","Haitian Vodou","ベナン起源のアフリカ系宗教。ハイチに移植され独自発展した。","宗教学・神学","Sub_Saharan_Africa",1600,"https://en.wikipedia.org/wiki/Haitian_Vodou",now,now),
(uid(),"サンテリア","Santeria","キューバのアフロ・キューバ系宗教。ヨルバの神格をカトリックの聖人と融合。","宗教学・神学","Latin_America",1800,"https://en.wikipedia.org/wiki/Santer%C3%ADa",now,now),
(uid(),"カンドンブレ","Candomble","ブラジルのアフリカ起源宗教。ヨルバ・ダオメ系の神格を祀る。","宗教学・神学","Latin_America",1800,"https://en.wikipedia.org/wiki/Candombl%C3%A9",now,now),
(uid(),"シャーマニズム","Shamanism","宗教的専門家が憑依・脱魂によって霊界と交信する宗教現象の総称。","宗教学・神学","Global_Synthesis",-10000,"https://en.wikipedia.org/wiki/Shamanism",now,now),
(uid(),"アボリジナル宗教","Australian Aboriginal religion","ドリームタイムを中核概念とするオーストラリア先住民の宗教。","宗教学・神学","Oceania",-50000,"https://en.wikipedia.org/wiki/Australian_Aboriginal_religion",now,now),
(uid(),"マオリ宗教","Maori religion","タプー・マナ・マウイ神話を含むニュージーランド先住民の宗教体系。","宗教学・神学","Oceania",-1000,"https://en.wikipedia.org/wiki/M%C4%81ori_religion",now,now),
(uid(),"儒教礼楽思想","Confucian ritual and music","礼と楽を社会秩序・道徳涵養の基本とする儒教の思想体系。","宗教学・神学","East_Asia",-500,"https://en.wikipedia.org/wiki/Confucian_ritual",now,now),
(uid(),"道教内丹術","Inner alchemy neidan","道教の瞑想・気功・錬金術的修行法。不老不死を目指す内的変容。","宗教学・神学","East_Asia",300,"https://en.wikipedia.org/wiki/Neidan",now,now),
(uid(),"天台宗","Tiantai Buddhism","智顗が創始した中国仏教宗派。法華経を最高位に置く総合的教学体系。","宗教学・神学","East_Asia",575,"https://en.wikipedia.org/wiki/Tiantai",now,now),
(uid(),"法相宗","Yogacara school","唯識思想を中核とする仏教宗派。玄奘がインドから将来した。","宗教学・神学","East_Asia",600,"https://en.wikipedia.org/wiki/Yogachara",now,now),
(uid(),"真言宗","Shingon Buddhism","空海が請来した密教。曼荼羅・加持祈祷を重視する。","宗教学・神学","East_Asia",806,"https://en.wikipedia.org/wiki/Shingon_Buddhism",now,now),
(uid(),"修験道","Shugendo","山岳での修行を通じて霊力を得る日本独自の山岳信仰。仏教・神道が融合。","宗教学・神学","East_Asia",700,"https://en.wikipedia.org/wiki/Shugendo",now,now),
(uid(),"スンナ派神学","Sunni theology","イスラームの主流神学。アシュアリー派・マートゥリーディー派などを含む。","宗教学・神学","West_Asia_North_Africa",900,"https://en.wikipedia.org/wiki/Sunni_Islam",now,now),
(uid(),"イスラーム哲学","Islamic philosophy","イブン・スィーナー・イブン・ルシュドらによるギリシア哲学とイスラームの融合。","宗教学・神学","West_Asia_North_Africa",800,"https://en.wikipedia.org/wiki/Islamic_philosophy",now,now),
(uid(),"カバラー","Kabbalah","中世ユダヤ教の神秘主義。セフィロトの木・エン・ソフを中核概念とする。","宗教学・神学","West_Asia_North_Africa",1150,"https://en.wikipedia.org/wiki/Kabbalah",now,now),
(uid(),"ハシディズム","Hasidism","18世紀ポーランドで生まれたユダヤ教敬虔主義運動。カリスマ的指導者を中心とする。","宗教学・神学","Western_Europe",1730,"https://en.wikipedia.org/wiki/Hasidism",now,now),
(uid(),"宗教改革","Protestant Reformation","16世紀ルターに始まるカトリック教会への抗議運動。西洋宗教地図を変革した。","宗教学・神学","Western_Europe",1517,"https://en.wikipedia.org/wiki/Reformation",now,now),
(uid(),"対抗宗教改革","Counter-Reformation","カトリック教会の内部改革・プロテスタントへの対抗運動。イエズス会が中心。","宗教学・神学","Western_Europe",1545,"https://en.wikipedia.org/wiki/Counter-Reformation",now,now),
(uid(),"敬虔主義","Pietism","ドイツで生まれたルター派の信仰刷新運動。個人の回心体験を重視する。","宗教学・神学","Western_Europe",1675,"https://en.wikipedia.org/wiki/Pietism",now,now),
(uid(),"メソジスト運動","Methodist movement","18世紀ウェスレー兄弟が起こした英国国教会内の信仰覚醒運動。","宗教学・神学","Western_Europe",1738,"https://en.wikipedia.org/wiki/Methodism",now,now),
(uid(),"ヨガ哲学","Yoga philosophy","パタンジャリのヨーガ・スートラを基礎とするインド六派哲学のひとつ。","宗教学・神学","South_Asia",-200,"https://en.wikipedia.org/wiki/Yoga_Sutras_of_Patanjali",now,now),
(uid(),"ウパニシャッド哲学","Upanishadic philosophy","ヴェーダの締めくくりをなすインド哲学の根本聖典群。ブラフマン・アートマン論。","宗教学・神学","South_Asia",-800,"https://en.wikipedia.org/wiki/Upanishads",now,now),
(uid(),"バクティ運動","Bhakti movement","中世インドの宗教的献身・愛神運動。カースト制を超えた平等を説いた。","宗教学・神学","South_Asia",800,"https://en.wikipedia.org/wiki/Bhakti_movement",now,now),
(uid(),"チベット密教","Tibetan Buddhism","インド仏教とボン教が融合したチベット独自の仏教形態。ダライ・ラマ制度を含む。","宗教学・神学","East_Asia",641,"https://en.wikipedia.org/wiki/Tibetan_Buddhism",now,now),
(uid(),"上座部仏教","Theravada Buddhism","パーリ語三蔵に基づく東南アジア・スリランカの仏教伝統。比丘制度を重視。","宗教学・神学","South_Asia",-250,"https://en.wikipedia.org/wiki/Theravada",now,now),
(uid(),"原始キリスト教","Early Christianity","1世紀から4世紀のキリスト教の形成期。異端論争・聖書正典化・教会形成が進む。","宗教学・神学","West_Asia_North_Africa",30,"https://en.wikipedia.org/wiki/Early_Christianity",now,now),
(uid(),"東方正教神秘主義","Eastern Orthodox mysticism","ヘシュカズム（静寂主義）・神化（テオーシス）を中核とする正教会の神秘的伝統。","宗教学・神学","Western_Europe",300,"https://en.wikipedia.org/wiki/Hesychasm",now,now),
(uid(),"近代宗教批判","Critique of religion","啓蒙主義・マルクス・フォイエルバッハによる宗教の人間的・社会的起源の暴露。","宗教学・神学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Criticism_of_religion",now,now),

# ── 文学批評理論 補強 (~60 entries) ──
(uid(),"オリエンタリズム批判","Orientalism Said","エドワード・サイードによる西洋の東洋表象が植民地権力を構成するという批判理論。","文学批評理論","Global_Synthesis",1978,"https://en.wikipedia.org/wiki/Orientalism_(Said_book)",now,now),
(uid(),"フェミニスト文学批評","Feminist literary criticism","女性経験・ジェンダー・家父長制を視点に文学を読み直す批評方法。","文学批評理論","North_America",1970,"https://en.wikipedia.org/wiki/Feminist_literary_criticism",now,now),
(uid(),"クィア理論","Queer theory","異性愛規範・性別二元論を解体する文化批評。バトラーのジェンダー・パフォーマティヴィティが基盤。","文学批評理論","North_America",1990,"https://en.wikipedia.org/wiki/Queer_theory",now,now),
(uid(),"脱構築批評","Deconstructive criticism","デリダの脱構築をテキスト読解に応用する批評実践。テキストの意味の不安定性を示す。","文学批評理論","Western_Europe",1966,"https://en.wikipedia.org/wiki/Deconstructive_criticism",now,now),
(uid(),"イデオロギー批評","Ideological criticism","マルクス主義的視点から文学テキストに潜むイデオロギーを暴露する批評。","文学批評理論","Western_Europe",1970,"https://en.wikipedia.org/wiki/Marxist_literary_criticism",now,now),
(uid(),"精神分析批評","Psychoanalytic criticism","フロイト・ラカンの精神分析理論を文学解釈に応用する批評方法。","文学批評理論","Western_Europe",1900,"https://en.wikipedia.org/wiki/Psychoanalytic_literary_criticism",now,now),
(uid(),"アーキタイプ批評","Archetypal criticism","ユング的元型・神話的パターンを文学テキストに見出すフライの批評理論。","文学批評理論","North_America",1957,"https://en.wikipedia.org/wiki/Archetypal_literary_criticism",now,now),
(uid(),"受容美学","Reception aesthetics","ヤウスとイーザーが発展させた読者の読書体験・地平融合を重視する文学理論。","文学批評理論","Western_Europe",1967,"https://en.wikipedia.org/wiki/Reception_theory",now,now),
(uid(),"物語論","Narratology","物語の構造・語り手・視点・時制を分析する学問。ジュネット・リモン＝ケナンが代表。","文学批評理論","Western_Europe",1966,"https://en.wikipedia.org/wiki/Narratology",now,now),
(uid(),"モダニズム文学","Modernist literature","20世紀初頭の形式実験・内面意識探求・伝統批判を特徴とする文学運動。","文学批評理論","Western_Europe",1890,"https://en.wikipedia.org/wiki/Modernist_literature",now,now),
(uid(),"ポストモダン文学","Postmodern literature","メタフィクション・パスティーシュ・脱中心化を特徴とする文学。","文学批評理論","North_America",1960,"https://en.wikipedia.org/wiki/Postmodern_literature",now,now),
(uid(),"マジックリアリズム","Magical realism","日常現実に魔術的要素が自然に組み込まれる文学スタイル。ガルシア＝マルケスが代表。","文学批評理論","Latin_America",1940,"https://en.wikipedia.org/wiki/Magic_realism",now,now),
(uid(),"ポストコロニアル文学","Postcolonial literature","植民地体験・独立後の文化的アイデンティティを描く文学。","文学批評理論","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Postcolonial_literature",now,now),
(uid(),"ディアスポラ文学","Diaspora literature","故郷からの離散と異郷での生をテーマとする文学。移民・亡命者の声を記録する。","文学批評理論","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Diaspora_literature",now,now),
(uid(),"世界文学論","World literature","ゲーテが提唱し現代のモレッティらが発展させた文学の地球規模的流通・比較研究。","文学批評理論","Global_Synthesis",1827,"https://en.wikipedia.org/wiki/World_literature",now,now),
(uid(),"間テクスト性","Intertextuality","テクストが他のテクストを引用・変形・対話することで意味を生成する概念。","文学批評理論","Western_Europe",1966,"https://en.wikipedia.org/wiki/Intertextuality",now,now),
(uid(),"バフチンのポリフォニー","Polyphony Bakhtin","バフチンがドストエフスキー小説に見出した複数の独立した声が並存する文学形式。","文学批評理論","Western_Europe",1929,"https://en.wikipedia.org/wiki/Dialogic",now,now),
(uid(),"カーニヴァル理論","Carnivalesque Bakhtin","バフチンが提唱した文学における笑い・転覆・民衆的逸脱の理論。","文学批評理論","Western_Europe",1965,"https://en.wikipedia.org/wiki/Carnivalesque",now,now),
(uid(),"崇高論","Sublime aesthetics","バーク・カントが理論化した圧倒的な自然や芸術に触れた時の畏怖と快感が混在する体験。","文学批評理論","Western_Europe",1757,"https://en.wikipedia.org/wiki/Sublime_(philosophy)",now,now),
(uid(),"エコクリティシズム","Ecocriticism","文学と自然環境の関係を研究する文学批評。環境問題との関連を探る。","文学批評理論","North_America",1978,"https://en.wikipedia.org/wiki/Ecocriticism",now,now),
(uid(),"アフリカ文学批評","African literary criticism","アフリカ文学の独自性・脱植民地化・伝統の口承性を論じる批評理論。","文学批評理論","Sub_Saharan_Africa",1960,"https://en.wikipedia.org/wiki/African_literature",now,now),
(uid(),"サバルタン研究","Subaltern studies","グラムシの概念を使いインド植民地史を書き直したチャクラバルティらの研究集団。","文学批評理論","South_Asia",1982,"https://en.wikipedia.org/wiki/Subaltern_Studies",now,now),
(uid(),"ゴシック文学","Gothic fiction","ホラー・神秘・中世的雰囲気を特徴とする文学ジャンル。ウォルポールに始まる。","文学批評理論","Western_Europe",1764,"https://en.wikipedia.org/wiki/Gothic_fiction",now,now),
(uid(),"ロマン主義文学","Romantic literature","理性より感情・想像力・自然を重視する19世紀初頭の文学運動。","文学批評理論","Western_Europe",1798,"https://en.wikipedia.org/wiki/Romantic_literature",now,now),
(uid(),"自然主義文学","Naturalism literature","科学的決定論を文学に適用し遺伝・環境による人間行動を描くゾラに始まる運動。","文学批評理論","Western_Europe",1870,"https://en.wikipedia.org/wiki/Naturalism_(literature)",now,now),
(uid(),"象徴主義詩","Symbolist poetry","直接的表現を避け象徴・音楽性で内面を表現するフランス19世紀末の詩運動。","文学批評理論","Western_Europe",1880,"https://en.wikipedia.org/wiki/Symbolism_(arts)",now,now),
(uid(),"超現実主義文学","Surrealist literature","無意識・夢・自動筆記を文学に導入するブルトンに始まる運動。","文学批評理論","Western_Europe",1924,"https://en.wikipedia.org/wiki/Surrealist_literature",now,now),
(uid(),"ニグリチュード運動","Negritude","セゼール・サンゴールらによるアフリカ人の文化的アイデンティティ回復の文学運動。","文学批評理論","Sub_Saharan_Africa",1930,"https://en.wikipedia.org/wiki/N%C3%A9gritude",now,now),
(uid(),"ラテンアメリカのBoom","Latin American Boom","1960年代のラテンアメリカ文学の国際的台頭。マルケス・バルガスリョサら。","文学批評理論","Latin_America",1960,"https://en.wikipedia.org/wiki/Latin_American_Boom",now,now),
(uid(),"デトロワジームバリズム","Dakwah literature","イスラーム的価値観に基づくマレーシア・インドネシアの現代文学運動。","文学批評理論","South_Asia",1970,"https://en.wikipedia.org/wiki/Malay_literature",now,now),

# ── 美学・芸術哲学 補強 (~50 entries) ──
(uid(),"カントの判断力批判","Critique of Judgment Kant","カントの第三批判書。美的判断の普遍性・目的論的自然観を論じる。","美学・芸術哲学","Western_Europe",1790,"https://en.wikipedia.org/wiki/Critique_of_Judgment",now,now),
(uid(),"ヘーゲル美学","Hegel aesthetics","絶対精神の自己展開として芸術を位置づけるヘーゲルの体系的美学。","美学・芸術哲学","Western_Europe",1835,"https://en.wikipedia.org/wiki/Introductory_Lectures_on_Aesthetics",now,now),
(uid(),"ニーチェ芸術哲学","Nietzsche philosophy of art","アポロン的・ディオニュソス的の二原理から芸術の本質を論じる。","美学・芸術哲学","Western_Europe",1872,"https://en.wikipedia.org/wiki/The_Birth_of_Tragedy",now,now),
(uid(),"デューイの経験としての芸術","Art as Experience Dewey","デューイがプラグマティズムの立場から芸術を日常経験の完結形として論じた美学。","美学・芸術哲学","North_America",1934,"https://en.wikipedia.org/wiki/Art_as_Experience",now,now),
(uid(),"制度的芸術定義","Institutional theory of art","ダントーとディッキーによる芸術界が芸術を定義するという理論。","美学・芸術哲学","North_America",1964,"https://en.wikipedia.org/wiki/Institutional_theory_of_art",now,now),
(uid(),"芸術定義論争","Definition of art debate","芸術とは何かをめぐる哲学的議論。本質主義・反本質主義・制度論が対立する。","美学・芸術哲学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Art",now,now),
(uid(),"映画の美学","Aesthetics of film","映画を芸術として分析する美学的研究。モンタージュ・映画言語・リアリズム論。","美学・芸術哲学","Western_Europe",1920,"https://en.wikipedia.org/wiki/Film_theory",now,now),
(uid(),"音楽の哲学","Philosophy of music","音楽の本質・表現・美的経験を論じる哲学。絶対音楽vs標題音楽論争が代表。","美学・芸術哲学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Philosophy_of_music",now,now),
(uid(),"建築の美学","Aesthetics of architecture","建築物の美的価値・機能との関係・都市との関係を論じる美学。","美学・芸術哲学","Western_Europe",1750,"https://en.wikipedia.org/wiki/Aesthetics_of_architecture",now,now),
(uid(),"応用美学","Applied aesthetics","日常的対象・デザイン・大衆文化に美学的分析を適用する分野。","美学・芸術哲学","North_America",1960,"https://en.wikipedia.org/wiki/Applied_aesthetics",now,now),
(uid(),"環境美学","Environmental aesthetics","自然環境・人工環境の美的経験を研究する比較的新しい美学分野。","美学・芸術哲学","North_America",1970,"https://en.wikipedia.org/wiki/Environmental_aesthetics",now,now),
(uid(),"インド美学","Indian aesthetics","ラサ理論・ドヴァニ理論など古代インド独自の美的理論体系。","美学・芸術哲学","South_Asia",-200,"https://en.wikipedia.org/wiki/Indian_aesthetics",now,now),
(uid(),"中国美術史論","Chinese art theory","筆墨・気韻生動・六法など中国独自の絵画・書道理論。","美学・芸術哲学","East_Asia",400,"https://en.wikipedia.org/wiki/Chinese_art",now,now),
(uid(),"侘び・寂び","Wabi-sabi","不完全・無常・質素を美の本質とする日本固有の美的理念。茶道と結びつく。","美学・芸術哲学","East_Asia",1300,"https://en.wikipedia.org/wiki/Wabi-sabi",now,now),
(uid(),"もののあわれ","Mono no aware","事物の移ろいやすさへの感受性と哀愁を表す日本の美的概念。本居宣長が理論化。","美学・芸術哲学","East_Asia",1796,"https://en.wikipedia.org/wiki/Mono_no_aware",now,now),
(uid(),"アフリカ美学","African aesthetics","アフリカ伝統芸術の機能的・共同体的・精神的側面を論じる美学。","美学・芸術哲学","Sub_Saharan_Africa",1960,"https://en.wikipedia.org/wiki/African_aesthetics",now,now),
(uid(),"大衆文化の美学","Popular aesthetics","高尚芸術と大衆文化の境界を問い直す美学。カルチュラルスタディーズと連動。","美学・芸術哲学","North_America",1970,"https://en.wikipedia.org/wiki/Popular_culture",now,now),
(uid(),"デジタル美学","Digital aesthetics","コンピュータ・デジタル技術が生み出す新しい芸術形式と美的経験の研究。","美学・芸術哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Digital_art",now,now),
(uid(),"身体パフォーマンス美学","Performance aesthetics","身体・ライブ性・参加を重視するパフォーマンスアートの美的理論。","美学・芸術哲学","North_America",1960,"https://en.wikipedia.org/wiki/Performance_art",now,now),
(uid(),"写真の美学","Aesthetics of photography","写真が芸術として認められるための理論的議論。バルト・ソンタグが代表。","美学・芸術哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Photography_and_the_aesthetics_of_photography",now,now),

# ── 歴史学 補強 (~40 entries) ──
(uid(),"マイクロヒストリー","Microhistory","個人・村落・出来事など微小なスケールから歴史の深層を照らすジンズブルグらの方法論。","歴史学・歴史哲学","Western_Europe",1976,"https://en.wikipedia.org/wiki/Microhistory",now,now),
(uid(),"グローバルヒストリー","Global history","特定国家・文明圏の枠を超えて地球規模の連関を論じる歴史学。","歴史学・歴史哲学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Global_history",now,now),
(uid(),"デジタルヒストリー","Digital history","デジタル技術・ビッグデータを用いる歴史研究の新分野。","歴史学・歴史哲学","North_America",2000,"https://en.wikipedia.org/wiki/Digital_history",now,now),
(uid(),"ビッグヒストリー","Big History","宇宙の誕生から現代まで138億年を統合的に論じる学際的歴史観。","歴史学・歴史哲学","Global_Synthesis",1989,"https://en.wikipedia.org/wiki/Big_History",now,now),
(uid(),"環境史","Environmental history","人間社会と自然環境の相互作用を研究する歴史学分野。","歴史学・歴史哲学","North_America",1970,"https://en.wikipedia.org/wiki/Environmental_history",now,now),
(uid(),"ジェンダー史","Gender history","歴史においてジェンダーが社会関係を構成する役割を研究する分野。","歴史学・歴史哲学","North_America",1980,"https://en.wikipedia.org/wiki/Gender_history",now,now),
(uid(),"記憶研究","Memory studies","集合的記憶・記念・忘却を研究する学際的分野。ノラ・アスマンが代表。","歴史学・歴史哲学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Memory_studies",now,now),
(uid(),"植民地史","Colonial history","植民地支配の形成・維持・崩壊と被支配者の経験を研究する分野。","歴史学・歴史哲学","Global_Synthesis",1880,"https://en.wikipedia.org/wiki/Colonialism",now,now),
(uid(),"アフリカ歴史学","African historiography","口承伝統・考古学・文字資料を組み合わせてアフリカ史を再構成する方法論。","歴史学・歴史哲学","Sub_Saharan_Africa",1960,"https://en.wikipedia.org/wiki/African_historiography",now,now),
(uid(),"ラテンアメリカ歴史学","Latin American historiography","征服以前の文明・植民地期・独立後の歴史的変化を研究する分野。","歴史学・歴史哲学","Latin_America",1800,"https://en.wikipedia.org/wiki/Latin_American_history",now,now),
(uid(),"中国史学","Chinese historiography","正史体制・実録・通史など中国固有の歴史叙述の伝統と方法論。","歴史学・歴史哲学","East_Asia",-100,"https://en.wikipedia.org/wiki/Chinese_historiography",now,now),
(uid(),"イスラーム歴史学","Islamic historiography","アラビア語・ペルシア語での歴史叙述の伝統。イブン・ハルドゥーンが代表。","歴史学・歴史哲学","West_Asia_North_Africa",700,"https://en.wikipedia.org/wiki/Islamic_historiography",now,now),
(uid(),"史料批判","Source criticism","歴史資料の真正性・信頼性・偏向を批判的に検討する歴史学の基本方法。","歴史学・歴史哲学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Source_criticism",now,now),
(uid(),"口承史","Oral history","目撃者・参加者の証言を記録・保存・分析して歴史を再構成する方法論。","歴史学・歴史哲学","Global_Synthesis",1940,"https://en.wikipedia.org/wiki/Oral_history",now,now),
(uid(),"ランケ実証主義","Rankean historicism","あったがままを示すというランケの実証主義的歴史学方法論。近代史学の基礎。","歴史学・歴史哲学","Western_Europe",1824,"https://en.wikipedia.org/wiki/Leopold_von_Ranke",now,now),
(uid(),"反実仮想史","Counterfactual history","もしという思考実験で歴史の因果を検討する方法論。","歴史学・歴史哲学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Counterfactual_history",now,now),
(uid(),"社会史","Social history","上層エリートでなく一般民衆の生活・家族・共同体の歴史を研究する方法論。","歴史学・歴史哲学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Social_history",now,now),
(uid(),"文化史","Cultural history","象徴・儀礼・表象・メンタリティを研究対象とする歴史学。ブルクハルトに始まる。","歴史学・歴史哲学","Western_Europe",1860,"https://en.wikipedia.org/wiki/Cultural_history",now,now),
(uid(),"科学史","History of science","科学的知識・方法・制度の歴史的発展を研究する分野。クーンが代表。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/History_of_science",now,now),
(uid(),"技術史","History of technology","技術的革新とその社会的影響の歴史的変化を研究する分野。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/History_of_technology",now,now),
(uid(),"宗教史","History of religion","世界各地の宗教の起源・発展・相互影響を研究する分野。エリアーデが代表。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/History_of_religion",now,now),
(uid(),"医療史","History of medicine","医学知識・医療実践・病気認識の歴史的変化を研究する分野。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/History_of_medicine",now,now),
(uid(),"プロソポグラフィー","Prosopography","集団的伝記研究。エリート層・集団の社会的背景・ネットワークを分析する方法論。","歴史学・歴史哲学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Prosopography",now,now),
(uid(),"日本史学","Japanese historiography","国史・正史体制から近代実証史学への変遷と戦後史学の展開。","歴史学・歴史哲学","East_Asia",720,"https://en.wikipedia.org/wiki/History_of_Japan",now,now),
]

con = sqlite3.connect(DB)
con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM humanities_concept WHERE status='active'")
print(f"既存件数: {cur.fetchone()[0]}")

existing = set(r[0] for r in con.execute("SELECT name_en FROM humanities_concept"))
batch = []
inserted = skipped = 0

for r in RECORDS:
    if r[2] in existing:
        skipped += 1
        continue
    existing.add(r[2])
    batch.append((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],'url_present','dua_wave_a2','active',r[8],r[9]))
    if len(batch) >= 500:
        cur.executemany("""INSERT INTO humanities_concept
            (id,name_ja,name_en,definition,subfield,culture_region,
             era_start,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
        con.commit()
        inserted += len(batch)
        batch = []

if batch:
    cur.executemany("""INSERT INTO humanities_concept
        (id,name_ja,name_en,definition,subfield,culture_region,
         era_start,source_url,verification_status,quality_flag,
         status,created_at,updated_at)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
    con.commit()
    inserted += len(batch)

cur.execute("SELECT COUNT(*) FROM humanities_concept WHERE status='active'")
total = cur.fetchone()[0]
con.close()
print(f"inserted={inserted}, skipped={skipped}")
print(f"総件数: {total} (目標5500)")
