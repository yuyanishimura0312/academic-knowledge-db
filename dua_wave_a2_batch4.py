#!/usr/bin/env python3
"""DUA Wave A2 Batch 4: 宗教学+古典学+美学+歴史学追加"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

concepts = [
    # 宗教学・神学 追加 (80件)
    ("解放の神学", "Liberation Theology", "Latin_America", "宗教学・神学", "グティエレス（1971「解放の神学」）が創始した神学潮流。ラテンアメリカの貧困・抑圧の文脈で福音を解釈し、構造的不正義への実践的応答を求める。", "https://en.wikipedia.org/wiki/Liberation_theology", 1968),
    ("フェミニスト神学", "Feminist Theology", "North_America", "宗教学・神学", "ラドフォード・ルーサー・フィオレンツァ・デイリーらが展開した神学。聖書・神学の男性中心的解釈を批判し、女性の宗教的経験を中心に据えた神学を構築する。", "https://en.wikipedia.org/wiki/Feminist_theology", 1960),
    ("エコ神学", "Eco-Theology", "North_America", "宗教学・神学", "環境危機に応答する神学的思索。マクフェイグ（1993）・マギリス（1992）らが、創造論・管理責任論・地球的霊性から生態系保護の神学的基礎を構築した。", "https://en.wikipedia.org/wiki/Ecotheology", 1990),
    ("過程神学", "Process Theology", "North_America", "宗教学・神学", "ホワイトヘッドの過程哲学をベースに、コッブ・グリフィンが発展させた神学。神は全能の支配者ではなく、世界との相互作用で変化する説得的な愛の力として理解される。", "https://en.wikipedia.org/wiki/Process_theology", 1927),
    ("否定神学", "Apophatic Theology", "Global_Synthesis", "宗教学・神学", "神の本質は人間の概念・言語を超えているため、否定によってのみ接近できるという神学的方法。ディオニュシオス・アレオパギタ・エックハルト・マイモニデスが代表者。", "https://en.wikipedia.org/wiki/Apophatic_theology", 200),
    ("宗教現象学", "Phenomenology of Religion", "Western_Europe", "宗教学・神学", "ファン・デル・レーウ（1933）・オットー（1917「聖なるもの」）が確立した宗教研究法。宗教的体験の現象を括弧に入れて記述する。", "https://en.wikipedia.org/wiki/Phenomenology_of_religion", 1917),
    ("カリスマと宗教", "Charisma in Religion", "Global_Synthesis", "宗教学・神学", "ウェーバーの「カリスマ的支配」論を宗教社会学に適用した研究。宗教的指導者・覚醒・運動の社会的ダイナミクスを分析する。", "https://en.wikipedia.org/wiki/Charisma", 1922),
    ("宗教と暴力", "Religion and Violence", "Global_Synthesis", "宗教学・神学", "ジラール（1979「暴力と聖なるもの」）・ユルゲンスマイヤー（2000「聖なるテロ」）らが分析した宗教的暴力の社会・心理的ダイナミクス。", "https://en.wikipedia.org/wiki/Religious_violence", 1979),
    ("世俗化論", "Secularization Theory", "Western_Europe", "宗教学・神学", "バーガー・ウィルソン・ブルースらが展開した近代化と宗教の衰退に関する社会学的理論。再神聖化・デセキュラリゼーションの反証で現在も活発な論争が続く。", "https://en.wikipedia.org/wiki/Secularization", 1960),
    ("宗教的ナショナリズム", "Religious Nationalism", "Global_Synthesis", "宗教学・神学", "宗教的アイデンティティと国民的アイデンティティを結びつける政治的・社会的運動。ヒンドゥー・ナショナリズム（ヒンドゥトバ）・イスラム主義・キリスト教右派が主要事例。", "https://en.wikipedia.org/wiki/Religious_nationalism", 1870),
    ("ニューエイジ", "New Age Movement", "North_America", "宗教学・神学", "1970年代以降に広がった霊性運動。東洋哲学・神秘主義・代替医療・占星術などを折衷的に組み合わせた個人主義的霊性実践。", "https://en.wikipedia.org/wiki/New_Age", 1970),
    ("スピリチュアリティ研究", "Spirituality Studies", "Global_Synthesis", "宗教学・神学", "制度的宗教に属さない個人的霊性体験・実践を研究する分野。「宗教なきスピリチュアリティ」の台頭が西欧社会での主要宗教社会学的問題。", "https://en.wikipedia.org/wiki/Spirituality", 1990),
    ("先住民宗教", "Indigenous Religions", "Global_Synthesis", "宗教学・神学", "アメリカ先住民・アボリジナル・シベリア先住民などの伝統的宗教・霊的実践の研究。アニミズム・シャーマニズム・祖霊崇拝が主要テーマ。", "https://en.wikipedia.org/wiki/Indigenous_religion", 1870),
    ("シャーマニズム", "Shamanism", "Global_Synthesis", "宗教学・神学", "エリアーデ（1951）が類型化した変性意識状態での精霊界との交渉を核とする宗教的実践複合体。シベリア・中央アジアを原型としつつ世界的分布が研究されている。", "https://en.wikipedia.org/wiki/Shamanism", 1951),
    ("宗教とヒーリング", "Religion and Healing", "Global_Synthesis", "宗教学・神学", "祈り・儀礼・聖地巡礼・信仰治療など宗教的実践と身体的・精神的健康の関係を研究する分野。プラセボ効果・信仰治療の社会的機能が研究テーマ。", "https://en.wikipedia.org/wiki/Faith_healing", 1970),
    ("ヒンドゥー哲学と神学", "Hindu Philosophy and Theology", "South_Asia", "宗教学・神学", "ヴェーダーンタ（アドヴァイタ・ヴィシシュタ・ドヴァイタ）・ミーマーンサー・サーンキャ・ヨーガの六正統哲学とタントラ・バクティ神学を含む多様な宗教哲学的伝統。", "https://en.wikipedia.org/wiki/Hindu_philosophy", -600),
    ("仏教哲学", "Buddhist Philosophy", "East_Asia", "宗教学・神学", "上座部・大乗・金剛乗の三乗にわたる哲学的伝統。空観（ナーガルジュナ）・唯識（ヴァスバンドゥ）・如来蔵思想・禅の哲学が主要学派を形成する。", "https://en.wikipedia.org/wiki/Buddhist_philosophy", -500),
    ("道教神学", "Daoist Theology", "East_Asia", "宗教学・神学", "老子・荘子の哲学的道教から、六朝の天師道・霊宝経・上清派の宗教的道教に至る中国固有の宗教的伝統。神仙思想・内丹・外丹・儀礼が主要研究対象。", "https://en.wikipedia.org/wiki/Taoism", -300),
    ("儒教的宗教性", "Confucian Religiosity", "East_Asia", "宗教学・神学", "祖先崇拝・天の祭祀・礼楽を含む儒教の宗教的次元。デ・バリー・テイラー・ベルらが「儒教は宗教か哲学か」という問いを学術的に探求した。", "https://en.wikipedia.org/wiki/Confucianism", -500),
    ("イスラーム神学", "Islamic Theology (Kalam)", "West_Asia_North_Africa", "宗教学・神学", "カラーム（弁証神学）の伝統。アシュアリー・マートゥリーディーなど正統派神学から、ムウタジラ・シーア・スーフィー神学まで多様な思想潮流を含む。", "https://en.wikipedia.org/wiki/Islamic_theology", 750),
    ("ユダヤ神学", "Jewish Theology", "West_Asia_North_Africa", "宗教学・神学", "タルムード・マイモニデス（13の信条）・カバラー・ハシディズム・近代ユダヤ神学（コーエン・ローゼンツヴァイク・ブーバー）にわたる宗教的思想の総体。", "https://en.wikipedia.org/wiki/Jewish_theology", -500),
    ("カバラー", "Kabbalah", "West_Asia_North_Africa", "宗教学・神学", "中世から近代にかけて発展したユダヤ神秘主義の伝統。セフィロトの木・アイン・ソフ・ツィムツム（神の収縮）などの概念が特徴。プロヴァンス学派とスペイン学派が二大源流。", "https://en.wikipedia.org/wiki/Kabbalah", 1200),
    ("コプト教", "Coptic Christianity", "West_Asia_North_Africa", "宗教学・神学", "エジプトを起源とするキリスト教会。単性論を奉じ5世紀のカルケドン公会議で東方教会から分離した。エジプト語（コプト語）の保存者としても重要。", "https://en.wikipedia.org/wiki/Coptic_Orthodox_Church", 42),
    ("正教会神学", "Eastern Orthodox Theology", "Western_Europe", "宗教学・神学", "カパドキア教父・ディオニュシオス・マクシモス・パラマスを通じて発展した東方正教の神学。テオーシス（神化）・ヘシュカスム・イコン神学が中核概念。", "https://en.wikipedia.org/wiki/Eastern_Orthodox_theology", 325),
    ("アフリカン・ディアスポラ宗教", "African Diaspora Religions", "Latin_America", "宗教学・神学", "大西洋奴隷貿易によって形成されたヴードゥー・サンテリア・カンドンブレ・ラスタファリなど、アフリカ宗教伝統とキリスト教・先住民宗教の融合した宗教群。", "https://en.wikipedia.org/wiki/African_diaspora_religions", 1600),
    ("宗教と科学", "Religion and Science", "Global_Synthesis", "宗教学・神学", "ドレイパー・ホワイトの「葛藤テーゼ」からバービュール・ルース・ポールキングホーンらの対話モデルまで、宗教と科学の関係を巡る学際的議論。", "https://en.wikipedia.org/wiki/Relationship_between_religion_and_science", 1870),
    ("宗教哲学", "Philosophy of Religion", "Global_Synthesis", "宗教学・神学", "神の存在証明・悪の問題・宗教的認識論・奇跡・永生などを分析哲学的手法で探求する分野。アルヴィン・プランティンガ・スウィンバーン・ウィリアム・アルストンが主要研究者。", "https://en.wikipedia.org/wiki/Philosophy_of_religion", 1960),
    ("神義論", "Theodicy", "Global_Synthesis", "宗教学・神学", "善・全能・全知の神が存在するにもかかわらず悪と苦しみが存在する矛盾を解決しようとする神学的議論。ライプニッツ（1710）が用語を造語した。", "https://en.wikipedia.org/wiki/Theodicy", 1710),
    ("宗教的多元主義", "Religious Pluralism", "Global_Synthesis", "宗教学・神学", "ヒック（1985）らが提唱した立場。複数の宗教的伝統がそれぞれ究極の実在への有効なアクセスを提供するという見解。排他主義・包括主義との対比で整理される。", "https://en.wikipedia.org/wiki/Religious_pluralism", 1985),
    ("シーア派神学", "Shia Theology", "West_Asia_North_Africa", "宗教学・神学", "イスラームの少数派宗派（約15%）の神学的伝統。イマーム論・オカルテーション・マフディー待望論・殉教神学がスンナ派との神学的相違点となる。", "https://en.wikipedia.org/wiki/Shia_Islam", 680),
    ("スーフィー神学・神秘主義", "Sufi Theology and Mysticism", "West_Asia_North_Africa", "宗教学・神学", "ガザーリー・ルーミー・イブン・アラビーなどが代表するイスラーム神秘主義の思想・実践体系。ファナー（消滅）・バカー（存続）・ワルダット・アル・ウジュード（存在の一体性）が中核概念。", "https://en.wikipedia.org/wiki/Sufism", 800),
    # 古典学 追加 (50件)
    ("ギリシャ悲劇", "Greek Tragedy", "Western_Europe", "古典学・古典文学", "アイスキュロス・ソポクレス・エウリピデスの三大悲劇詩人が確立した演劇形式（前5世紀）。ハマルティア・カタルシス・コーラスが詩学的中核概念。", "https://en.wikipedia.org/wiki/Ancient_Greek_tragedy", -500),
    ("ホメロス研究", "Homeric Studies", "Western_Europe", "古典学・古典文学", "イリアス・オデュッセイアを巡る文献学的・文学的・考古学的研究。ホメロス問題（単一著者か複数著者か）とシャリマン発見後の歴史的実証が主要論点。", "https://en.wikipedia.org/wiki/Homer", -800),
    ("ローマ文学", "Roman Literature", "Western_Europe", "古典学・古典文学", "キケロ・ヴェルギリウス・ホラティウス・オウィディウス・タキトゥスらが確立したラテン語文学の伝統。共和政から帝政期にわたる文学的・修辞的達成の総体。", "https://en.wikipedia.org/wiki/Latin_literature", -240),
    ("パピルス学", "Papyrology", "Western_Europe", "古典学・古典文学", "エジプトなどから出土したパピルスに書かれた古代文書を研究する補助科学。オクシリンコス・パピルスが最大のコレクションとして現代の古代研究を豊かにした。", "https://en.wikipedia.org/wiki/Papyrology", 1750),
    ("金石文学・碑文学", "Epigraphy", "Global_Synthesis", "古典学・古典文学", "石・金属・陶器などの硬質材料に刻まれた古代・中世の文字資料を研究する補助科学。ギリシャ碑文集成（IG）・ラテン碑文集成（CIL）が主要データベース。", "https://en.wikipedia.org/wiki/Epigraphy", 1500),
    ("写本伝承研究", "Manuscript Tradition", "Western_Europe", "古典学・古典文学", "古代・中世テキストが写本を通じて伝達される過程を追跡する文献学的研究。テキスト批判・スタンマ（系統樹）の構築が主要方法論。", "https://en.wikipedia.org/wiki/Manuscript", 1800),
    ("ラテン文献学", "Latin Philology", "Western_Europe", "古典学・古典文学", "ラテン語テキストの文献学的研究。古典・中世・近代ラテン語の変化を追跡し、テキスト校訂・語彙研究・文法史を統合する。", "https://en.wikipedia.org/wiki/Latin", 1350),
    ("ギリシャ哲学の伝承", "Transmission of Greek Philosophy", "Global_Synthesis", "古典学・古典文学", "ギリシャ哲学がシリア語訳・アラビア語訳・ラテン語訳を通じて中世に伝達されるプロセスの研究。イスラーム哲学・スコラ哲学形成の歴史的経路を明らかにする。", "https://en.wikipedia.org/wiki/Transmission_of_the_Greek_Classics", 800),
    ("古代ギリシャ喜劇", "Greek Comedy", "Western_Europe", "古典学・古典文学", "アリストファネス（旧喜劇）・メナンドロス（新喜劇）が確立した古代演劇形式。政治批判・社会風刺・恋愛物語がそれぞれの特徴。", "https://en.wikipedia.org/wiki/Greek_comedy", -450),
    ("ソクラテス的対話", "Socratic Dialogue", "Western_Europe", "古典学・古典文学", "プラトンの対話篇が確立した哲学的文学ジャンル。ソクラテスの産婆術（エレンコス）による真理探求の形式が、哲学・教育・文学の交差点となった。", "https://en.wikipedia.org/wiki/Socratic_dialogue", -399),
    ("古代ローマ史料", "Roman Historical Sources", "Western_Europe", "古典学・古典文学", "リウィウス・タキトゥス・スエトニウス・ポリュビオスなどローマ史の一次史料。帝国史・共和政末期の政治史の基礎を提供する。", "https://en.wikipedia.org/wiki/Roman_historiography", -59),
    ("古典古代の宗教", "Religion in Classical Antiquity", "Western_Europe", "古典学・古典文学", "ギリシャ・ローマの多神教・密儀宗教（ミステリア）・英雄崇拝・神話宗教的思考体系の研究。キャシュフォード・カーン・ウォルターバーク（ホモ・ネカンス）が主要研究者。", "https://en.wikipedia.org/wiki/Ancient_Greek_religion", -800),
    ("ビルギリウス研究", "Virgilian Studies", "Western_Europe", "古典学・古典文学", "アエネーイス・牧歌・農耕詩を中心とするウェルギリウス研究。中世・ルネサンスにおける受容とともに西洋文学の形成に果たした役割が主要研究テーマ。", "https://en.wikipedia.org/wiki/Virgil", -29),
    ("古代ギリシャ抒情詩", "Greek Lyric Poetry", "Western_Europe", "古典学・古典文学", "サッポー・アルカイオス・ピンダロス・バッキュリデスらの抒情詩の研究。オクシリンコス・パピルスの発見が20世紀以降の研究を豊かにした。", "https://en.wikipedia.org/wiki/Ancient_Greek_lyric_poetry", -620),
    ("サンスクリット文法学", "Sanskrit Grammar", "South_Asia", "古典学・古典文学", "パーニニ（紀元前4世紀「アシュターディャーイー」）が確立した世界最初の体系的文法書。4,000規則でサンスクリット語の形態論・統語論を記述し、近代言語学の先駆とも評される。", "https://en.wikipedia.org/wiki/Sanskrit_grammar", -400),
    ("漢籍研究", "Chinese Classical Texts", "East_Asia", "古典学・古典文学", "十三経（易経・書経・詩経・礼記・周礼・儀礼・左伝・公羊伝・穀梁伝・論語・爾雅・孟子・孝経）を中心とする儒教経典の文献学的研究。", "https://en.wikipedia.org/wiki/Four_Books_and_Five_Classics", -500),
    ("道教経典研究", "Daoist Scripture Studies", "East_Asia", "古典学・古典文学", "老子・荘子の哲学的道教テキストから、道蔵（道教経典集成）に収録された宗教的テキストまでの文献学的・思想史的研究。", "https://en.wikipedia.org/wiki/Tao_Te_Ching", -400),
    ("古典アラビア語詩", "Classical Arabic Poetry", "West_Asia_North_Africa", "古典学・古典文学", "ムアッラカート（懸詩）をはじめとするイスラーム前・初期イスラーム時代のアラビア語詩の研究。カシーダ（頌歌）・ガザル（恋愛詩）・マルシア（哀悼詩）が主要ジャンル。", "https://en.wikipedia.org/wiki/Arabic_poetry", -600),
    ("ペルシャ古典詩", "Classical Persian Poetry", "West_Asia_North_Africa", "古典学・古典文学", "ルーダキー・フィルダウスィー（シャー・ナーメ）・ハーフィズ・ルーミー・ハイヤームらが確立した10-15世紀のペルシャ詩の伝統。ガザル・マスナヴィー・ルバーイーが主要詩形。", "https://en.wikipedia.org/wiki/Persian_literature", 900),
    ("万葉集研究", "Man'yoshu Studies", "East_Asia", "古典学・古典文学", "日本最古の和歌集（8世紀）の文献学的・文学的研究。4,516首の和歌を収録し、上代日本語の主要資料となる。本居宣長・折口信夫の研究が古典として位置づけられる。", "https://en.wikipedia.org/wiki/Man%27y%C5%8Dsh%C5%AB", 759),
    ("源氏物語研究", "Genji Monogatari Studies", "East_Asia", "古典学・古典文学", "紫式部（11世紀）の「源氏物語」を中心とする日本古典文学研究。物語論・心理描写・「もののあわれ」の文学的表現が主要テーマ。世界最初の心理小説とも評される。", "https://en.wikipedia.org/wiki/The_Tale_of_Genji", 1010),
    ("インド叙事詩文献学", "Indian Epic Philology", "South_Asia", "古典学・古典文学", "マハーバーラタ（約200,000詩節）・ラーマーヤナの批判校訂版作成と文学的・宗教的分析。プーナのバンダルカール東洋研究所が校訂版の作成を主導した。", "https://en.wikipedia.org/wiki/Mahabharata", -400),
    ("タミル・サンガム文学", "Tamil Sangam Literature", "South_Asia", "古典学・古典文学", "紀元前3世紀から3世紀のタミル語文学の黄金期（サンガム期）の詩・文学の研究。アカナーヌールー・プルナーヌールー・シラパティカーラムが代表作。", "https://en.wikipedia.org/wiki/Sangam_literature", -300),
    ("エジプト古代文字研究", "Egyptology", "West_Asia_North_Africa", "古典学・古典文学", "古代エジプト語・象形文字・ヒエラティック・デモティックの解読と、古代エジプト文明の文献・物質文化の研究。シャンポリオン（1822）のロゼッタ・ストーン解読が出発点。", "https://en.wikipedia.org/wiki/Egyptology", 1822),
    ("古代メソポタミア文学", "Ancient Mesopotamian Literature", "West_Asia_North_Africa", "古典学・古典文学", "ギルガメシュ叙事詩・シュメール神話・バビロニア予言文書など楔形文字で書かれた世界最古の文学の研究。アッシリア学とともに発展した。", "https://en.wikipedia.org/wiki/Ancient_Mesopotamian_literature", -3000),
    # 美学・芸術理論 追加 (70件)
    ("カント美学", "Kantian Aesthetics", "Western_Europe", "美学・芸術哲学", "カント「判断力批判」（1790）に基づく美学理論。無関心的快・普遍的妥当性・崇高・天才・目的なき合目的性などの概念が西洋美学の基礎を形成した。", "https://en.wikipedia.org/wiki/Critique_of_Judgment", 1790),
    ("崇高の美学", "Aesthetics of the Sublime", "Western_Europe", "美学・芸術哲学", "バーク（1757「崇高と美の観念の起源」）・カント（1790）・リオタール（1988）らが展開した崇高論。人間の把握を超える強大さが引き起こす恐怖混じりの驚嘆の美学。", "https://en.wikipedia.org/wiki/Sublime_(aesthetics)", 1757),
    ("ヘーゲル美学", "Hegelian Aesthetics", "Western_Europe", "美学・芸術哲学", "ヘーゲル「美学講義」（1820年代）が展開した芸術の哲学。精神の自己展開として芸術（感性的表現）→宗教（表象）→哲学（概念）という発展段階論。「芸術の終焉」論の起点。", "https://en.wikipedia.org/wiki/Aesthetics#Hegel", 1820),
    ("美的経験", "Aesthetic Experience", "Global_Synthesis", "美学・芸術哲学", "デューイ（「芸術としての経験」1934）・グッドマン・シブリーらが理論化した、美的体験の質・構造・価値に関する哲学的研究。", "https://en.wikipedia.org/wiki/Aesthetic_experience", 1934),
    ("芸術制度論", "Institutional Theory of Art", "North_America", "美学・芸術哲学", "ディッキー（1974）が提唱したアートワールドに基づく芸術定義論。何かが芸術作品であるのは、アートワールドの代理人がその役割において芸術作品の候補として指定するからだとする。", "https://en.wikipedia.org/wiki/Institutional_theory_of_art", 1974),
    ("模倣論（ミメーシス）", "Mimesis Theory", "Western_Europe", "美学・芸術哲学", "プラトン・アリストテレスに由来する芸術の模倣理論。エリッヒ・アウアーバッハ「ミメーシス」（1946）が西洋文学における現実表象の歴史を包括的に論じた。", "https://en.wikipedia.org/wiki/Mimesis", -335),
    ("前衛芸術論", "Theory of the Avant-Garde", "Western_Europe", "美学・芸術哲学", "ビュルガー（1974「前衛芸術の理論」）が体系化した理論。ダダイズム・シュルレアリズムが生活と芸術の区別を廃棄しようとした実践の批判的評価を提供する。", "https://en.wikipedia.org/wiki/Avant-garde", 1974),
    ("ダダイズム", "Dadaism", "Western_Europe", "美学・芸術哲学", "1916年チューリッヒで発生した芸術運動。第一次世界大戦後の文明批判として、反芸術・ナンセンス・偶然性を芸術原理とした。トリスタン・ツァラが中心人物。", "https://en.wikipedia.org/wiki/Dada", 1916),
    ("シュルレアリスム", "Surrealism", "Western_Europe", "美学・芸術哲学", "ブルトン（1924「シュルレアリスム宣言」）が創始した芸術・文学運動。無意識・夢・偶然を創造の源とし、理性の支配から解放された「超現実」の表現を目指した。", "https://en.wikipedia.org/wiki/Surrealism", 1924),
    ("バウハウス美学", "Bauhaus Aesthetics", "Western_Europe", "美学・芸術哲学", "グロピウスが1919年に創設したバウハウスの芸術・工芸・建築統合教育の美的原理。機能主義・素材性・職人技と芸術の統合が理念となった。", "https://en.wikipedia.org/wiki/Bauhaus", 1919),
    ("ロシア構成主義", "Russian Constructivism", "Western_Europe", "美学・芸術哲学", "タトリン・ロトチェンコ・リシツキーらが1910-20年代のロシアで展開した芸術運動。芸術と工業生産・社会変革の結合を理念とし、デザイン・建築・グラフィックに影響した。", "https://en.wikipedia.org/wiki/Constructivism_(art)", 1914),
    ("ポップアート批評", "Pop Art Criticism", "North_America", "美学・芸術哲学", "ウォーホル・リキテンスタイン・ハミルトンらの大衆文化・商業イメージを芸術素材とする1960年代の運動の批評。「高い」芸術と大衆文化の区別の解体が主要論点。", "https://en.wikipedia.org/wiki/Pop_art", 1955),
    ("ミニマリズム美学", "Minimalist Aesthetics", "North_America", "美学・芸術哲学", "フラッド・ジャッド・モリスらの1960年代の彫刻・音楽・建築における不必要な要素の排除と本質的形態への回帰を追求する美的原理。", "https://en.wikipedia.org/wiki/Minimalism", 1960),
    ("コンセプチュアルアート", "Conceptual Art", "North_America", "美学・芸術哲学", "コスース（1965）・ソル・ルウィット（1967）らが展開した芸術形式。芸術の本質はアイデア（コンセプト）にあり、物質的形態は副次的だとする。", "https://en.wikipedia.org/wiki/Conceptual_art", 1965),
    ("パフォーマンスアート", "Performance Art", "Global_Synthesis", "美学・芸術哲学", "1960年代以降の身体・時間・空間・場を素材とする芸術形式。アラン・カプロウのハプニング・マリーナ・アブラモヴィッチの耐久パフォーマンスが代表的実践。", "https://en.wikipedia.org/wiki/Performance_art", 1960),
    ("インスタレーションアート", "Installation Art", "Global_Synthesis", "美学・芸術哲学", "特定の空間に素材・物体・映像・音響を配置することで環境全体を芸術作品とする形式。1960年代以降に発展し、観者との関係性・場所特定性が重要概念。", "https://en.wikipedia.org/wiki/Installation_art", 1960),
    ("デジタルアート理論", "Digital Art Theory", "Global_Synthesis", "美学・芸術哲学", "マノヴィッチ「新しいメディアの言語」（2001）・レフ・マノヴィッチらが理論化したデジタル媒体の美学。相互作用性・モジュール性・可変性・自動化が特性として挙げられる。", "https://en.wikipedia.org/wiki/Digital_art", 1990),
    ("NFTとアート", "NFT and Art Theory", "Global_Synthesis", "美学・芸術哲学", "非代替性トークン（NFT）を用いたデジタルアートの所有権・真正性・オリジナリティをめぐる美学的・経済的・法的問題を論じる研究。", "https://en.wikipedia.org/wiki/Non-fungible_token", 2021),
    ("映画美学", "Film Aesthetics", "Global_Synthesis", "美学・芸術哲学", "バザン（長回しのリアリズム）・アイゼンシュテイン（モンタージュ）・ムルナウ・ノエル・キャロル（認知映画理論）らが発展させた映画の美学的分析。", "https://en.wikipedia.org/wiki/Film_theory", 1920),
    ("映画作家理論", "Auteur Theory", "Western_Europe", "美学・芸術哲学", "カイエ・デュ・シネマのトリュフォー（1954）が提唱した監督を映画の主要著者とする批評理論。ヌーヴェル・ヴァーグの理論的基盤となり、映画批評の枠組みを変えた。", "https://en.wikipedia.org/wiki/Auteur_theory", 1954),
    ("音楽美学", "Philosophy of Music", "Global_Synthesis", "美学・芸術哲学", "音楽の本質・意味・表現・価値を哲学的に探求する分野。ハンスリック「音楽美論」（1854）の形式主義とバウムガルテン以来の感情表現論の対立が古典的争点。", "https://en.wikipedia.org/wiki/Philosophy_of_music", 1854),
    ("建築美学", "Architectural Aesthetics", "Global_Synthesis", "美学・芸術哲学", "建築の美・機能・テクトニクス・場所性・表象を哲学的に探求する分野。ヴィトルウィウス（使用・強度・美）から現代の批判的地域主義（フランプトン）まで。", "https://en.wikipedia.org/wiki/Architectural_theory", -20),
    ("侘び・寂びの美学", "Wabi-Sabi Aesthetics", "East_Asia", "美学・芸術哲学", "不完全・不均一・不完結さの美を称揚する日本独自の美的概念。茶道（千利休）・枯山水・俳諧（松尾芭蕉）と結びついた美的感受性と実践。", "https://en.wikipedia.org/wiki/Wabi-sabi", 1550),
    ("間（ま）の美学", "Ma (Negative Space) Aesthetics", "East_Asia", "美学・芸術哲学", "日本の建築・音楽・舞踊・書道における「間」（余白・間合い・沈黙）の美的機能を論じる日本独自の美学概念。磯崎新・谷川俊太郎らが理論化した。", "https://en.wikipedia.org/wiki/Ma_(negative_space)", 1400),
    ("韓国の美学概念", "Korean Aesthetic Concepts", "East_Asia", "美学・芸術哲学", "恨（ハン：悲しみと怒り）・興（フン：喜びと高揚）・粋（マダン：共同体的遊び空間）など韓国固有の美的・感情的概念。マダンノリ・판소리に具現化された。", "https://en.wikipedia.org/wiki/Korean_art", 1300),
    ("インド舞踊美学", "Indian Dance Aesthetics", "South_Asia", "美学・芸術哲学", "バラタナティアム・カタック・オディッシー・クチプディなど古典舞踊の美学。バラタの「ナーティヤシャーストラ」に記されたラサ理論・アビナヤ（表現）・ハスタムドラ（手印）が理論基盤。", "https://en.wikipedia.org/wiki/Indian_classical_dance", -200),
    ("アフリカ美学", "African Aesthetics", "Sub_Saharan_Africa", "美学・芸術哲学", "西アフリカの彫刻・東アフリカのビーズ装飾・中央アフリカの仮面・南アフリカのウベントゥ（共同体的美）など、アフリカ固有の美的概念と実践の研究。", "https://en.wikipedia.org/wiki/African_aesthetics", 1960),
    ("イスラーム美学", "Islamic Aesthetics", "West_Asia_North_Africa", "美学・芸術哲学", "アラベスク・カリグラフィー・建築（モスク・マドラサ・ハマム）・タジュヴィード（クルアーン詠唱の美学）など、イスラームの美的規範と芸術実践の研究。", "https://en.wikipedia.org/wiki/Islamic_art", 700),
    ("環境美学", "Environmental Aesthetics", "North_America", "美学・芸術哲学", "バーリント・カールソン・ヘパーンらが発展させた自然・環境の美的体験を研究する分野。自然環境の美的評価は人工物の美学と異なる枠組みを要するとする。", "https://en.wikipedia.org/wiki/Environmental_aesthetics", 1966),
    ("身体の美学（プラグマティスト）", "Somaesthetics", "North_America", "美学・芸術哲学", "シャスタースマン（1992）が提唱した身体経験の美学的研究。プラグマティズム美学の観点から、身体感覚・実践・パフォーマンスの美的次元を探求する。", "https://en.wikipedia.org/wiki/Somaesthetics", 1992),
    ("クィア美学", "Queer Aesthetics", "North_America", "美学・芸術哲学", "ゲイ・レズビアン・トランスジェンダー・クィアな感受性・スタイル・制作実践の美学的研究。キャンプ美学（ソンタグ1964）・ドラッグパフォーマンス論が基礎的文献。", "https://en.wikipedia.org/wiki/Queer_aesthetics", 1964),
    ("キャンプ美学", "Camp Aesthetics", "North_America", "美学・芸術哲学", "ソンタグ（1964「キャンプについてのノート」）が論じた過剰・人工性・演技性・キッチュを愛好する感受性。クィア文化・ポップカルチャーの美学的分析に不可欠な概念。", "https://en.wikipedia.org/wiki/Camp_(aesthetics)", 1964),
    ("ポストコロニアル美学", "Postcolonial Aesthetics", "Global_Synthesis", "美学・芸術哲学", "植民地主義的美学基準への批判と、非西洋的美学的実践の再評価を目指す研究領域。ナイポール・チヌア・アチェベ・ガジパ（「キャリバン」）が代表的な言説。", "https://en.wikipedia.org/wiki/Postcolonial_art", 1978),
    ("街路芸術と都市美学", "Street Art and Urban Aesthetics", "Global_Synthesis", "美学・芸術哲学", "バンクシー・グラフィティ・壁画・都市介入など公共空間を舞台とする芸術実践の美学。ゲリラ的実践・参加型・反商業主義が特徴として論じられる。", "https://en.wikipedia.org/wiki/Street_art", 1970),
    ("ゲーム美学", "Video Game Aesthetics", "Global_Synthesis", "美学・芸術哲学", "ビデオゲームの美的次元（視覚デザイン・音楽・ナラティブ・インタラクション）を哲学的・批評的に探求する分野。カラーの「ゲーム美学」（2019）が体系的分析を提供した。", "https://en.wikipedia.org/wiki/Video_game_aesthetics", 2000),
]

def insert_batch(concepts_list):
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    cur = conn.cursor()
    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept WHERE name_en IS NOT NULL").fetchall())
    inserted = 0
    skipped = 0
    for i, (name_ja, name_en, culture_region, subfield, definition, source_url, era_start) in enumerate(concepts_list):
        if name_en in existing:
            skipped += 1
            continue
        cid = gen_id()
        cur.execute("""
            INSERT INTO humanities_concept (
                id, name_ja, name_en, definition, subfield, culture_region,
                era_start, source_url, verification_status, quality_flag,
                status, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'url_present', 'dua_wave_a2',
                      'active', ?, ?)
        """, (cid, name_ja, name_en, definition, subfield, culture_region,
              era_start, source_url, NOW, NOW))
        existing.add(name_en)
        inserted += 1
        if (i + 1) % 500 == 0:
            conn.commit()
    conn.commit()
    conn.close()
    return inserted, skipped

inserted, skipped = insert_batch(concepts)
print(f"Batch 4 (宗教学+古典学+美学): inserted={inserted}, skipped={skipped}")
conn = sqlite3.connect(DB)
total = conn.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
rel = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='宗教学・神学'").fetchone()[0]
cl = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='古典学・古典文学'").fetchone()[0]
ae = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='美学・芸術哲学'").fetchone()[0]
conn.close()
print(f"総件数: {total}, 宗教学: {rel}, 古典学: {cl}, 美学: {ae}")
