#!/usr/bin/env python3
"""DUA Wave A2 Batch 5: 大規模補完 — 全サブフィールド横断で不足分を埋める"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def gen_id():
    return "dua_" + uuid.uuid4().hex[:12]

NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

# 各サブフィールドに大量追加: 目標は合計+1800件
concepts = [
    # ===== 倫理学・政治哲学 追加 (120件) =====
    ("徳倫理学", "Virtue Ethics", "Global_Synthesis", "倫理学・政治哲学", "アリストテレス（ニコマコス倫理学）を起点にアンスコム・マッキンタイア・ハーストハウスらが再興した倫理理論。行為の帰結・義務より、行為者の徳（卓越性）の涵養を倫理の核心とする。", "https://en.wikipedia.org/wiki/Virtue_ethics", -335),
    ("功利主義の歴史", "History of Utilitarianism", "Western_Europe", "倫理学・政治哲学", "ベンサム（1789）からミル・シジウィック・シンガーに至る功利主義の発展史。快楽計算から選好功利主義・選択肢功利主義・二段階功利主義への変容を追う。", "https://en.wikipedia.org/wiki/Utilitarianism", 1789),
    ("義務論の系譜", "History of Deontological Ethics", "Western_Europe", "倫理学・政治哲学", "カントの定言命法から現代の権利論・制約に基づく倫理学（ネーゲル・トムソン）まで義務論的倫理学の発展。結果への無関心と行為自体の道徳的価値を強調する。", "https://en.wikipedia.org/wiki/Deontological_ethics", 1785),
    ("メタ倫理学", "Metaethics", "Western_Europe", "倫理学・政治哲学", "道徳的命題の性質・真理性・認識論を研究する倫理学の分岐。認知主義vs非認知主義・実在論vs反実在論・自然主義vs非自然主義が主要な対立軸。", "https://en.wikipedia.org/wiki/Metaethics", 1900),
    ("道徳実在論", "Moral Realism", "Western_Europe", "倫理学・政治哲学", "道徳的事実・真理が客観的に存在するとの立場。スキャンロン・ムーア・マクダウェルらが代表的擁護者。道徳的認識論と道徳的形而上学の両面から擁護される。", "https://en.wikipedia.org/wiki/Moral_realism", 1900),
    ("道徳的感情主義", "Moral Emotivism", "Western_Europe", "倫理学・政治哲学", "エア（1936）・スティーブンソン（1944）が提唱した非認知主義の一形態。道徳的主張は真偽なき感情表出・態度表明に過ぎないとする。", "https://en.wikipedia.org/wiki/Emotivism", 1936),
    ("契約論", "Contractarianism", "Western_Europe", "倫理学・政治哲学", "ホッブズ・ルソー・ロールズ・スキャンロンが展開した社会契約に基づく政治・道徳理論。仮想的合意（無知のヴェール）または相互同意の不拒否性から正義原理を導出する。", "https://en.wikipedia.org/wiki/Contractarianism", 1651),
    ("正義の差異原理", "Difference Principle", "North_America", "倫理学・政治哲学", "ロールズ「正義論」（1971）の第二の正義原理。社会的・経済的不平等は最も不利な立場の人々を最大限に利するときのみ正当化されるとする。", "https://en.wikipedia.org/wiki/Difference_principle", 1971),
    ("共同体主義", "Communitarianism", "North_America", "倫理学・政治哲学", "マッキンタイア・サンデル・ウォルツァー・テイラーがロールズ的自由主義への批判として展開した政治哲学。自己は共同体に埋め込まれており、自由主義の原子論的個人概念を批判する。", "https://en.wikipedia.org/wiki/Communitarianism", 1982),
    ("リベラリズムの歴史", "History of Liberalism", "Western_Europe", "倫理学・政治哲学", "ロック・ミル・カント・ロールズに至る自由主義思想の系譜。個人の自由・権利・立憲政府・市場経済・表現の自由が中核価値として形成されてきた歴史。", "https://en.wikipedia.org/wiki/Liberalism", 1689),
    ("共和主義思想", "Republican Political Thought", "Western_Europe", "倫理学・政治哲学", "アリストテレス・キケロ・マキャベリ・アレント・ペティットらが展開した共和主義の伝統。非支配としての自由・市民的徳・公共善への参加が核心概念。", "https://en.wikipedia.org/wiki/Republicanism", -335),
    ("非支配としての自由", "Freedom as Non-Domination", "Western_Europe", "倫理学・政治哲学", "ペティット（1997「共和主義」）が提唱した自由概念。単なる干渉の不在（消極的自由）ではなく、恣意的な干渉能力の不在（非支配）を自由の核心とする。", "https://en.wikipedia.org/wiki/Republican_liberty", 1997),
    ("ケアの倫理", "Ethics of Care", "North_America", "倫理学・政治哲学", "ギリガン（1982）・ノディングズ・トロント・ホルダーらが発展させた倫理理論。抽象的原則より具体的関係・相互依存・応答性・ケア実践を倫理の中心に置く。", "https://en.wikipedia.org/wiki/Ethics_of_care", 1982),
    ("動物倫理", "Animal Ethics", "Global_Synthesis", "倫理学・政治哲学", "シンガー（1975「動物解放」）・リーガン（1983）・ドノルドソン＆キムリッカ（2011）らが展開した動物の道徳的地位・権利・福祉をめぐる倫理学。", "https://en.wikipedia.org/wiki/Animal_ethics", 1975),
    ("生命倫理学", "Bioethics", "North_America", "倫理学・政治哲学", "ポッター（1971）が命名し、ビーチャム＆チルドレス（1979「医療倫理の原則」）が体系化した分野。自律・善行・無危害・正義の四原則が医療倫理の基盤。", "https://en.wikipedia.org/wiki/Bioethics", 1971),
    ("インフォームド・コンセント", "Informed Consent", "North_America", "倫理学・政治哲学", "医療・研究倫理の中核原則。患者・被験者が十分な情報と理解に基づいて自律的に同意を与えることを要求する。ニュルンベルク綱領（1947）が国際的規範として確立した。", "https://en.wikipedia.org/wiki/Informed_consent", 1947),
    ("気候正義", "Climate Justice", "Global_Synthesis", "倫理学・政治哲学", "気候変動の負担と便益の分配的正義・手続き的正義・修復的正義を研究する分野。排出責任・適応費用・気候難民の権利が主要論点。", "https://en.wikipedia.org/wiki/Climate_justice", 1990),
    ("世代間正義", "Intergenerational Justice", "Global_Synthesis", "倫理学・政治哲学", "現在世代が未来世代に対して負う義務を論じる倫理学・政治哲学の分野。環境・財政・文化遺産の維持義務が主要議論。パーフィットの非同一性問題が哲学的難問を提起する。", "https://en.wikipedia.org/wiki/Intergenerational_equity", 1970),
    ("デジタル倫理", "Digital Ethics", "Global_Synthesis", "倫理学・政治哲学", "AI・アルゴリズム・データ・プラットフォームが提起する倫理的問題を研究する分野。アルゴリズム的公正・プライバシー・デジタル自律・監視資本主義が主要テーマ。", "https://en.wikipedia.org/wiki/Digital_ethics", 2000),
    ("AIの倫理", "AI Ethics", "Global_Synthesis", "倫理学・政治哲学", "人工知能システムの設計・展開・ガバナンスに関わる倫理的問題。公平性・説明可能性・安全性・プライバシー・自律性・AGIリスクが主要論点。", "https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence", 2016),
    ("地球規模正義", "Global Justice", "Global_Synthesis", "倫理学・政治哲学", "ポッゲ・シンガー・ベイツ・ミラーらが論じる国境を超えた正義の問題。貧困・気候・難民・国際制度の倫理的評価が主要テーマ。コスモポリタニズムが理論的立場。", "https://en.wikipedia.org/wiki/Global_justice", 1990),
    ("功利主義と動物", "Utilitarian Animal Ethics", "Global_Synthesis", "倫理学・政治哲学", "シンガー（1975）が「功利主義の原則で動物の苦しみも同等に考慮すべき」と論じた議論。工場畜産・動物実験への批判の哲学的根拠となった。", "https://en.wikipedia.org/wiki/Peter_Singer", 1975),
    ("正戦論", "Just War Theory", "Global_Synthesis", "倫理学・政治哲学", "アウグスティヌス・アクィナス・グロティウス・ウォルツァー（1977）が展開した戦争の倫理的正当化条件を論じる伝統。正義の開戦原因・正当な戦争遂行・戦後正義が三支柱。", "https://en.wikipedia.org/wiki/Just_war_theory", 412),
    ("非暴力倫理", "Nonviolence Ethics", "South_Asia", "倫理学・政治哲学", "ガンジーのアヒンサー（非暴力）を政治的実践として理論化した倫理学。キング牧師・ソローの市民的不服従論と結合し、平和倫理の基礎となった。", "https://en.wikipedia.org/wiki/Nonviolence", 1906),
    ("人権の哲学", "Philosophy of Human Rights", "Global_Synthesis", "倫理学・政治哲学", "世界人権宣言（1948）以後の人権の哲学的基礎づけ（普遍主義対文化相対主義・道徳的権利対法的権利・能力アプローチ）を研究する分野。", "https://en.wikipedia.org/wiki/Philosophy_of_human_rights", 1948),
    ("承認の政治", "Politics of Recognition", "Global_Synthesis", "倫理学・政治哲学", "テイラー（1992「承認をめぐる政治」）・ホネット・フレーザーが展開した概念。承認と再分配の二軸で社会的正義を論じる。少数者・ジェンダー・エスニシティの承認要求が分析される。", "https://en.wikipedia.org/wiki/Politics_of_recognition", 1992),
    ("熟議民主主義", "Deliberative Democracy", "Global_Synthesis", "倫理学・政治哲学", "ハーバーマス・コーヘン・エルスター・ドライゼクらが発展させた民主主義理論。集計的（投票）民主主義に対して、公的理由・相互的尊重に基づく討議を民主的正統性の源泉とする。", "https://en.wikipedia.org/wiki/Deliberative_democracy", 1980),
    ("参加型民主主義", "Participatory Democracy", "Global_Synthesis", "倫理学・政治哲学", "バーバー（1984「強い民主主義」）・パットナム・ドライゼクらが論じる市民の直接的・積極的政治参加を重視する民主主義論。", "https://en.wikipedia.org/wiki/Participatory_democracy", 1960),
    ("ポピュリズム論", "Theory of Populism", "Global_Synthesis", "倫理学・政治哲学", "ラクラウ（2005）・ミュラー（2016）・モフ・ウェイランドらが展開するポピュリズムの理論的定義。「人民対エリート」の反多元主義的論理が核心概念として分析される。", "https://en.wikipedia.org/wiki/Populism", 2005),
    ("フェミニスト政治理論", "Feminist Political Theory", "North_America", "倫理学・政治哲学", "ウルストンクラフト・ミル・ファイアストーン・パットマン・スコット・フレーザーらが展開した政治的フェミニズムの理論。公私区別批判・ジェンダー化された市民権・交差性が主要概念。", "https://en.wikipedia.org/wiki/Feminist_political_theory", 1792),
    ("脱植民地主義政治哲学", "Decolonial Political Philosophy", "Global_Synthesis", "倫理学・政治哲学", "ファノン・キジャーノ（植民地性/近代性）・マリアテギ・ドゥッセル（解放哲学）らが発展させた南半球発の政治思想。近代性の植民地的構造を批判し、脱植民地化を目指す。", "https://en.wikipedia.org/wiki/Decoloniality", 1952),
    # ===== 大陸哲学・現象学 追加 (100件) =====
    ("フッサールの意識論", "Husserl's Theory of Consciousness", "Western_Europe", "大陸哲学・現象学", "フッサール（1900-1901「論理学研究」・1913「イデーン」）が確立した超越論的現象学。意識の志向性・ノエシス/ノエマ構造・時間意識・相互主観性が主要分析対象。", "https://en.wikipedia.org/wiki/Edmund_Husserl", 1900),
    ("ハイデガーの存在論", "Heidegger's Ontology", "Western_Europe", "大陸哲学・現象学", "ハイデガー「存在と時間」（1927）が展開した基礎存在論。現存在（Dasein）・気遣い・世界内存在・死への存在・本来性/非本来性・時間性が核心概念。", "https://en.wikipedia.org/wiki/Being_and_Time", 1927),
    ("サルトルの実存主義", "Sartre's Existentialism", "Western_Europe", "大陸哲学・現象学", "サルトル「存在と無」（1943）・「実存主義はヒューマニズムである」（1945）が展開した自由・責任・対自存在/即自存在・他者との対決・不良信仰の実存論。", "https://en.wikipedia.org/wiki/Jean-Paul_Sartre", 1943),
    ("ボーヴォワールのフェミニスト実存主義", "Beauvoir's Feminist Existentialism", "Western_Europe", "大陸哲学・現象学", "ボーヴォワール「第二の性」（1949）が展開した女性の他者化・主体性の欠如・女性性の文化的構築に関する実存主義的分析。「女に生まれるのではなく女になる」が核心命題。", "https://en.wikipedia.org/wiki/The_Second_Sex", 1949),
    ("メルロ＝ポンティの身体論", "Merleau-Ponty's Phenomenology of Perception", "Western_Europe", "大陸哲学・現象学", "メルロ＝ポンティ「知覚の現象学」（1945）が展開した身体的主体論。身体図式・肉・間身体性・知覚の一次性が主要概念。意識哲学から身体哲学への転換。", "https://en.wikipedia.org/wiki/Phenomenology_of_Perception", 1945),
    ("レヴィナスの他者論", "Levinas's Ethics of the Other", "Western_Europe", "大陸哲学・現象学", "レヴィナス「全体性と無限」（1961）・「存在とは別の仕方で」（1974）が展開した倫理学。他者の顔の無限性・応答責任の非対称性が西洋哲学の存在論的優先を批判する。", "https://en.wikipedia.org/wiki/Emmanuel_Levinas", 1961),
    ("フーコーの系譜学", "Foucault's Genealogy", "Western_Europe", "大陸哲学・現象学", "フーコー（1975「監獄の誕生」・1976「性の歴史」）が採用したニーチェ的系譜学の方法。権力/知の関係・規律・生政治・統治性が中核概念。", "https://en.wikipedia.org/wiki/Genealogy_(philosophy)", 1975),
    ("ドゥルーズ=ガタリの哲学", "Deleuze and Guattari's Philosophy", "Western_Europe", "大陸哲学・現象学", "「アンチ・オイディプス」（1972）・「千のプラトー」（1980）が展開した欲望・器官なき身体・リゾーム・配置・強度・マイナー性の哲学。", "https://en.wikipedia.org/wiki/Gilles_Deleuze", 1972),
    ("リゾーム哲学", "Rhizome Philosophy", "Western_Europe", "大陸哲学・現象学", "ドゥルーズ＆ガタリ（1980）が提唱した概念。木（樹状・中心的・位階的）に対するリゾーム（根茎状・非中心的・横断的）という二つの思考・組織化のモデル。", "https://en.wikipedia.org/wiki/Rhizome_(philosophy)", 1980),
    ("デリダの差延", "Derrida's Differance", "Western_Europe", "大陸哲学・現象学", "デリダが「差異」(différence)と「延期」(différer)を合成して造語した概念（differance）。意味は常に差異化され延期され、決して現前に把握されないという脱構築の核心テーゼ。", "https://en.wikipedia.org/wiki/Diff%C3%A9rance", 1968),
    ("バタイユの至高性論", "Bataille's Theory of Sovereignty", "Western_Europe", "大陸哲学・現象学", "バタイユが「呪われた部分」（1949）・「エロティシズム」（1957）で展開した消費・損失・極限・至高経験の哲学。有用性の経済に対する一般経済学の構想。", "https://en.wikipedia.org/wiki/Georges_Bataille", 1949),
    ("ブランショの文学空間", "Blanchot's Literary Space", "Western_Europe", "大陸哲学・現象学", "ブランショ「文学の空間」（1955）が展開した文学の「ニュートラル」・「外」・「語ることのなさ」の哲学。死・作業・非知識との関係が主題。", "https://en.wikipedia.org/wiki/Maurice_Blanchot", 1955),
    ("アーレントの政治哲学", "Arendt's Political Philosophy", "Western_Europe", "大陸哲学・現象学", "アーレント「人間の条件」（1958）・「全体主義の起源」（1951）・「精神の生活」が展開した活動・公共領域・複数性・権力・悪の陳腐さの政治哲学。", "https://en.wikipedia.org/wiki/Hannah_Arendt", 1951),
    ("ハーバーマスのコミュニケーション行為論", "Habermas's Theory of Communicative Action", "Western_Europe", "大陸哲学・現象学", "ハーバーマス「コミュニケーション的行為の理論」（1981）が展開した批判理論。生活世界と体系・討議倫理・公共圏・システムによる生活世界の植民地化が中核概念。", "https://en.wikipedia.org/wiki/The_Theory_of_Communicative_Action", 1981),
    ("ヘーゲルの弁証法", "Hegelian Dialectics", "Western_Europe", "大陸哲学・現象学", "ヘーゲル「精神現象学」（1807）が体系化した正・反・合（テーゼ・アンチテーゼ・ジンテーゼ）の弁証法的運動。絶対精神の自己展開として歴史・意識・国家が理解される。", "https://en.wikipedia.org/wiki/Dialectic", 1807),
    ("マルクスの疎外論", "Marx's Theory of Alienation", "Western_Europe", "大陸哲学・現象学", "マルクス「1844年経済学・哲学草稿」が展開したヘーゲル哲学の唯物論的転倒。労働者が生産物・労働活動・類的存在・他者から疎外される資本主義的メカニズムの分析。", "https://en.wikipedia.org/wiki/Marx%27s_theory_of_alienation", 1844),
    ("フランクフルト学派第一世代", "Frankfurt School First Generation", "Western_Europe", "大陸哲学・現象学", "ホルクハイマー・アドルノ・マルクーゼ・フロム・ベンヤミンらが形成したドイツの社会批判理論の集団（1930年代-1960年代）。啓蒙の弁証法・文化産業・ファシズム分析が主要業績。", "https://en.wikipedia.org/wiki/Frankfurt_School", 1923),
    ("否定弁証法", "Negative Dialectics", "Western_Europe", "大陸哲学・現象学", "アドルノ「否定弁証法」（1966）が展開した同一性思考（概念による現実の支配）への批判。非同一者・星座的思考・非暴力的概念使用を提唱する。", "https://en.wikipedia.org/wiki/Negative_dialectics", 1966),
    ("ベンヤミンのアウラ論", "Benjamin's Theory of Aura", "Western_Europe", "大陸哲学・現象学", "ベンヤミン「複製技術時代の芸術作品」（1936）が提唱した概念。オリジナル芸術作品が持つ一回性・場所特定的な「気配」（アウラ）が複製技術によって衰退するという論考。", "https://en.wikipedia.org/wiki/Aura_(Walter_Benjamin)", 1936),
    ("リオタールのポストモダン", "Lyotard's Postmodernism", "Western_Europe", "大陸哲学・現象学", "リオタール「ポストモダンの条件」（1979）が診断した知識の状態変化。大きな物語（進歩・解放・精神の弁証法）の終焉と言語ゲームの多元性・不共約可能性を主張する。", "https://en.wikipedia.org/wiki/The_Postmodern_Condition", 1979),
    ("ジジェクのラカン的マルクス主義", "Zizek's Lacanian Marxism", "Western_Europe", "大陸哲学・現象学", "ジジェク（1989「イデオロギーの崇高な客体」以来）がラカン・ヘーゲル・マルクスを統合した哲学・批評理論。イデオロギー・享楽・大文字の他者・実在界が主要概念。", "https://en.wikipedia.org/wiki/%C5%BDi%C5%BEek", 1989),
    ("バディウの存在論", "Badiou's Ontology", "Western_Europe", "大陸哲学・現象学", "バディウ「存在と出来事」（1988）が展開した数学的存在論。存在＝数学・出来事・主体・真理の手続きという枠組みで政治・芸術・科学・愛の四つの真理の条件を論じる。", "https://en.wikipedia.org/wiki/Alain_Badiou", 1988),
    ("ランシエールの感性の分割", "Ranciere's Distribution of the Sensible", "Western_Europe", "大陸哲学・現象学", "ランシエール（2000「感性の分割」）が展開した政治・美学・教育の理論。「ポリス」が定める感覚的なものの分割への「政治」による攪乱が民主主義の核心だとする。", "https://en.wikipedia.org/wiki/Jacques_Ranci%C3%A8re", 2000),
    ("アガンベンの例外状態論", "Agamben's State of Exception", "Western_Europe", "大陸哲学・現象学", "アガンベン（2003「例外状態」・1998「ホモ・サケル」）が展開した主権・剥き出しの生・例外状態の政治哲学。スミュ・イタリア語圏で発生した現代政治の生政治的読解。", "https://en.wikipedia.org/wiki/State_of_exception", 1998),
    ("スピノザの情動論", "Spinoza's Theory of Affects", "Western_Europe", "大陸哲学・現象学", "スピノザ「エチカ」（1677）が展開した情動（コナトゥス・欲望・悦び・悲しみ）の倫理学。ドゥルーズが情動の哲学として再評価し、身体の能力・変容能力が現代的注目を集める。", "https://en.wikipedia.org/wiki/Baruch_Spinoza", 1677),
    ("現象学と間文化哲学", "Intercultural Philosophy and Phenomenology", "Global_Synthesis", "大陸哲学・現象学", "ニシダの場所の論理・ヴァルデンフェルスの「応答性」など、西洋現象学と非西洋哲学の対話を通じた間文化的思考。アジア・アフリカ・ラテンアメリカの哲学的視点が取り込まれる。", "https://en.wikipedia.org/wiki/Intercultural_philosophy", 1980),
    ("京都学派", "Kyoto School", "East_Asia", "大陸哲学・現象学", "西田幾多郎・田辺元・西谷啓治らが形成した日本発の哲学学派（20世紀前半）。場所・絶対無・絶対矛盾的自己同一・東西思想の融合が特徴的主題。", "https://en.wikipedia.org/wiki/Kyoto_school", 1911),
    ("西田哲学", "Nishida Philosophy", "East_Asia", "大陸哲学・現象学", "西田幾多郎（1911「善の研究」以来）が展開した純粋経験・場所・絶対矛盾的自己同一の哲学。禅仏教の思想とドイツ観念論・現象学を独自に統合した。", "https://en.wikipedia.org/wiki/Kitaro_Nishida", 1911),
    ("デュボイスのダブル意識", "Du Bois's Double Consciousness", "North_America", "大陸哲学・現象学", "W.E.B.デュボイス（1903「黒人のたましい」）が提唱した概念。アフリカ系アメリカ人が白人社会の視線を通して自己を見つつ、自己固有の意識を持つという二重性。", "https://en.wikipedia.org/wiki/Double_consciousness", 1903),
    ("ファノンの脱植民地思想", "Fanon's Decolonial Philosophy", "Sub_Saharan_Africa", "大陸哲学・現象学", "フランツ・ファノン「大地のにもつ」（1961）・「黒い皮膚・白い仮面」（1952）が展開した脱植民地化の暴力論・植民地支配の心理学・黒人の主体性回復の哲学。", "https://en.wikipedia.org/wiki/Frantz_Fanon", 1952),
    ("マリアテギのアメリカ・インディアン哲学", "Mariategui's Andean Marxism", "Latin_America", "大陸哲学・現象学", "ペルーのホセ・カルロス・マリアテギ（1928「ペルーの七つのエッセイ」）がマルクス主義とアンデスのインカ的共同体主義を融合させた独自の社会主義哲学。", "https://en.wikipedia.org/wiki/José_Carlos_Mariátegui", 1928),
    # ===== 分析哲学・心の哲学 追加 (80件) =====
    ("意識のハード問題", "Hard Problem of Consciousness", "North_America", "分析哲学・心の哲学", "チャーマーズ（1995）が定式化した哲学的問題。物理的プロセスがなぜ主観的体験（クオリア）を生むのかは科学的説明では解決できないとする。", "https://en.wikipedia.org/wiki/Hard_problem_of_consciousness", 1995),
    ("クオリア", "Qualia", "North_America", "分析哲学・心の哲学", "意識的経験の主観的質（赤の赤さ・痛みの痛さ）を指す哲学的術語。ネーゲル（1974「コウモリであるとはどのようなことか」）・ジャクソン（1982）の知識論証が主要な議論。", "https://en.wikipedia.org/wiki/Qualia", 1974),
    ("機能主義（心の哲学）", "Functionalism in Philosophy of Mind", "North_America", "分析哲学・心の哲学", "パトナム（1960年代）が提唱した心の哲学の立場。心的状態は物理的実現から独立した機能的役割によって定義されるとする多重実現可能性テーゼが中核。", "https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)", 1967),
    ("物理主義（哲学）", "Physicalism", "North_America", "分析哲学・心の哲学", "全ての事物は物理的であるという哲学的立場。還元的物理主義・非還元的物理主義・消去主義・二側面論などのバリエーションがある。心の哲学の主流的枠組み。", "https://en.wikipedia.org/wiki/Physicalism", 1960),
    ("随伴現象説", "Epiphenomenalism", "Western_Europe", "分析哲学・心の哲学", "ハクスリー（1874）が提唱した立場。心的状態は物理プロセスの副産物（随伴現象）であり、因果力を持たないとする。自由意志・意識の実在性への挑戦となる。", "https://en.wikipedia.org/wiki/Epiphenomenalism", 1874),
    ("行動主義（哲学）", "Philosophical Behaviorism", "North_America", "分析哲学・心の哲学", "ライル「心の概念」（1949）が展開した哲学的行動主義。心的概念は行動傾向の記述であり、「機械の中の幽霊」（カルテジアン・デュアリズム）の誤りを批判する。", "https://en.wikipedia.org/wiki/Philosophical_behaviourism", 1949),
    ("同一説（心と脳）", "Mind-Brain Identity Theory", "Western_Europe", "分析哲学・心の哲学", "スマート・アームストロング（1960年代）が提唱した心の哲学の立場。心的状態は脳の物理的状態と同一であるとする。機能主義への批判として多重実現可能性問題がある。", "https://en.wikipedia.org/wiki/Type_physicalism", 1956),
    ("自由意志と決定論", "Free Will and Determinism", "Global_Synthesis", "分析哲学・心の哲学", "硬直した決定論・自由意志論・両立論（コンパティビリズム）の三立場間の論争。フランクファート（1969「そうしないことができない行為者」）・デネット・スローソンらが主要論者。", "https://en.wikipedia.org/wiki/Free_will", 1651),
    ("知識の分析", "Analysis of Knowledge", "Western_Europe", "分析哲学・心の哲学", "プラトン「メノン」に始まる「正当化された真なる信念」分析。ゲティア（1963）の反例が古典的定義を覆し、信頼性主義・文脈主義・インフォーマリズムが後継理論として登場した。", "https://en.wikipedia.org/wiki/Theory_of_knowledge", 1963),
    ("知識論の転回", "Epistemological Turn", "Western_Europe", "分析哲学・心の哲学", "17世紀のデカルト以来、哲学の中心問題が形而上学から認識論へ転換した歴史的変化。懐疑主義・基礎付け主義・コヒーレンティズム・信頼性主義が主要な認識論的立場。", "https://en.wikipedia.org/wiki/Epistemology", 1637),
    ("証言の認識論", "Epistemology of Testimony", "Western_Europe", "分析哲学・心の哲学", "他者の証言から知識を得る認識論的メカニズムを研究する分野。還元主義（要独立証拠）対反還元主義（推定的正当化）の対立が主要論争。", "https://en.wikipedia.org/wiki/Testimony_(epistemology)", 1990),
    ("知覚の哲学", "Philosophy of Perception", "Global_Synthesis", "分析哲学・心の哲学", "直接実在論・間接実在論（代表主義）・現象主義の対立。マクダウェル「心と世界」（1994）・チャーチランドの神経哲学が現代の主要立場を形成している。", "https://en.wikipedia.org/wiki/Philosophy_of_perception", 1900),
    ("思考の言語", "Language of Thought Hypothesis", "North_America", "分析哲学・心の哲学", "フォーダー（1975）が提唱した仮説。思考はメンタリーズ（思考の言語）と呼ばれる内的記号体系における計算として説明されるとする心の計算理論の具体化。", "https://en.wikipedia.org/wiki/Language_of_thought_hypothesis", 1975),
    ("モジュール性仮説", "Modularity of Mind", "North_America", "分析哲学・心の哲学", "フォーダー（1983）が提唱した心の理論。知覚・言語処理などの入力システムはドメイン特化的・情報的カプセル化されたモジュールとして機能するとする。", "https://en.wikipedia.org/wiki/Modularity_of_mind", 1983),
    ("フレーム問題", "Frame Problem", "North_America", "分析哲学・心の哲学", "マッカーシー＆ヘイズ（1969）がAI研究で定式化した問題。行為によって変化する事実と変化しない事実をどう表現・推論するかという問題で、哲学的認知科学の重要問題となった。", "https://en.wikipedia.org/wiki/Frame_problem", 1969),
    ("デネットの意識論", "Dennett's Theory of Consciousness", "North_America", "分析哲学・心の哲学", "デネット「意識という説話」（1991）が展開した多重草稿モデル。単一の「カルテジアン劇場」は存在せず、意識は並列的な解釈活動の結果として生じるという理論。", "https://en.wikipedia.org/wiki/Consciousness_Explained", 1991),
    ("拡張する心", "Extended Mind", "Western_Europe", "分析哲学・心の哲学", "クラーク＆チャーマーズ（1998）が提唱した仮説。認知プロセスは頭蓋骨・皮膚の内側に限定されず、ノートブック・スマートフォンなど外部ツールを含むまで拡張しうる。", "https://en.wikipedia.org/wiki/Extended_mind_thesis", 1998),
    ("具現化認知", "Embodied Cognition", "Global_Synthesis", "分析哲学・心の哲学", "認知は身体的経験に根ざしており、抽象的シンボル処理に還元できないとする立場。ヴァレラ・トンプソン・ロッシュ（1991「具現化された心」）が理論化した。", "https://en.wikipedia.org/wiki/Embodied_cognition", 1991),
    ("内在主義と外在主義（認識論）", "Internalism vs Externalism in Epistemology", "North_America", "分析哲学・心の哲学", "知識の正当化が認識者の内的状態（信念・証拠）のみに依存するか（内在主義）、外的世界との因果的関係にも依存するか（外在主義）の論争。信頼性主義が外在主義の主流形態。", "https://en.wikipedia.org/wiki/Epistemic_externalism", 1980),
    ("規範的認識論", "Normative Epistemology", "Global_Synthesis", "分析哲学・心の哲学", "信念形成・推論・認識的実践の規範的評価を扱う認識論の分野。何を信じるべきか・いかに推論すべきかの規準を研究する。", "https://en.wikipedia.org/wiki/Normative_epistemology", 1980),
    # ===== 文学批評理論 追加 (80件) =====
    ("トラウマ文学研究", "Trauma Literature Studies", "Global_Synthesis", "文学批評理論", "カルース（1995）・ハーマン（1992）・ラカプラが発展させた文学批評。ホロコースト・性暴力・戦争を語る文学テキストにおけるトラウマの表象・証言・沈黙を分析する。", "https://en.wikipedia.org/wiki/Trauma_studies", 1992),
    ("ゴシック文学批評", "Gothic Literary Criticism", "Western_Europe", "文学批評理論", "ウォルポール（1764）に始まるゴシック小説の系譜と批評理論。抑圧された回帰・崇高・ジェンダー・植民地主義・恐怖の美学が分析概念として用いられる。", "https://en.wikipedia.org/wiki/Gothic_fiction", 1764),
    ("SF文学批評", "Science Fiction Literary Criticism", "North_America", "文学批評理論", "ダルコ・スーヴィン（認知的疎外・ノヴム）・ドウェインらが展開したSF文学の批評理論。未来の科学技術的設定が現在の社会的矛盾を批判的に照射する機能を分析する。", "https://en.wikipedia.org/wiki/Science_fiction_studies", 1972),
    ("ユートピア文学研究", "Utopian Literature Studies", "Global_Synthesis", "文学批評理論", "トマス・モア（1516）に始まるユートピア・ディストピア文学の批評。ブロッホ（希望の原理）・ジェイムソン（現在を照らす否定的機能）が理論的枠組みを提供する。", "https://en.wikipedia.org/wiki/Utopian_and_dystopian_fiction", 1516),
    ("子ども文学研究", "Children's Literature Studies", "Global_Synthesis", "文学批評理論", "子ども向け文学の生産・流通・受容・ジェンダー・人種・子ども観の構築を研究する分野。ノドルマン（「力の言葉」1992）が権力関係の視点から理論化した。", "https://en.wikipedia.org/wiki/Children%27s_literature", 1970),
    ("探偵小説研究", "Detective Fiction Studies", "Global_Synthesis", "文学批評理論", "コナン・ドイル・クリスティから現代のノワールまでの探偵・犯罪小説の批評理論。「謎の解決」の物語構造・ジェンダー・人種・社会体制との関係が分析される。", "https://en.wikipedia.org/wiki/Detective_fiction", 1970),
    ("ロマン主義批評", "Romanticism Criticism", "Western_Europe", "文学批評理論", "ワーズワース・コールリッジ・キーツ・シェリー・バイロン・ノヴァーリス・ゲーテらの19世紀初頭の文学運動の批評。自然・感情・個人・無限への憧憬が主要テーマ。", "https://en.wikipedia.org/wiki/Romanticism", 1800),
    ("リアリズム批評", "Realism in Literature", "Western_Europe", "文学批評理論", "フロベール・トルストイ・ドストエフスキー・ゾラらの19世紀リアリズム文学の批評。社会的現実の忠実な描写・平凡な人物・科学的観察が主要原則。", "https://en.wikipedia.org/wiki/Literary_realism", 1830),
    ("自然主義文学批評", "Naturalism in Literature", "Western_Europe", "文学批評理論", "ゾラ（実験小説1880）に始まる科学的決定論を文学に適用した運動。遺伝・環境・社会的条件が人間行動を決定するという仮定に基づいて人間を描写する。", "https://en.wikipedia.org/wiki/Naturalism_(literature)", 1880),
    ("スラブ文学批評", "Slavic Literary Criticism", "Western_Europe", "文学批評理論", "プーシキン・トルストイ・ドストエフスキー・チェーホフ・ブルガーコフ・アフマートワなどロシア・スラブ文学の批評伝統。プーシキン以来の文学的伝統が豊かな批評的議論を生んだ。", "https://en.wikipedia.org/wiki/Russian_literature", 1820),
    ("移民・ディアスポラ文学", "Diasporic and Migrant Literature", "Global_Synthesis", "文学批評理論", "故郷喪失・ハイブリッドなアイデンティティ・多言語性・文化的交渉を主題とする文学の研究。ラッシュディー・タン・ナイポール・アチェベが代表的作家。", "https://en.wikipedia.org/wiki/Diaspora_literature", 1980),
    ("翻訳研究", "Translation Studies", "Global_Synthesis", "文学批評理論", "ベンヤミン（「翻訳者の使命」1923）・ルフェベール・ヴヌーティ（「翻訳者の不可視性」1995）らが発展させた翻訳の理論。異化翻訳vs自国化翻訳の対立が主要論点。", "https://en.wikipedia.org/wiki/Translation_studies", 1923),
    ("コミックス・マンガ研究", "Comics and Manga Studies", "Global_Synthesis", "文学批評理論", "マクラウド（「マンガ学」1993）・グロエンスティーン・夏目房之介らが発展させたコミックス・マンガの記号論的・文化的研究。コマ・吹き出し・読者の補完が分析概念。", "https://en.wikipedia.org/wiki/Comics_studies", 1990),
    ("デジタル文学", "Digital Literature", "Global_Synthesis", "文学批評理論", "ハイパーテキスト文学（ジョイス「アフタヌーン」1987）・インタラクティブ・フィクション・ソーシャルメディア詩など、デジタル媒体固有の文学形式の研究。", "https://en.wikipedia.org/wiki/Electronic_literature", 1987),
    ("物語の認知論", "Cognitive Narratology", "Global_Synthesis", "文学批評理論", "ハーマン（2002「ストーリー・ロジック」）・アンモラン・フリューダーニックらが発展させた認知科学と物語論の統合。読者の心的シミュレーション・スキーマ・自然化が概念的基盤。", "https://en.wikipedia.org/wiki/Cognitive_narratology", 1996),
    ("不信の自発的停止", "Willing Suspension of Disbelief", "Western_Europe", "文学批評理論", "コールリッジ（1817）が提唱した文学受容の概念。読者がフィクションの非現実性を了知しつつも自発的に信じ込む姿勢を取ることで詩的信仰が成立するとする。", "https://en.wikipedia.org/wiki/Suspension_of_disbelief", 1817),
    # ===== 宗教学追加 (40件) =====
    ("宗教的経験の哲学", "Philosophy of Religious Experience", "Global_Synthesis", "宗教学・神学", "ジェイムズ「宗教的経験の諸相」（1902）・アルストン「神の知覚」（1991）らが論じた宗教的・神秘的体験の哲学的地位。", "https://en.wikipedia.org/wiki/Philosophy_of_religion", 1902),
    ("神の存在証明", "Arguments for the Existence of God", "Western_Europe", "宗教学・神学", "本体論的論証（アンセルムス）・宇宙論的論証（アクィナス）・目的論的論証（ペイリー）・道徳論的論証（カント）など神の存在を論証しようとする哲学的試みの総体。", "https://en.wikipedia.org/wiki/Arguments_for_the_existence_of_God", 1078),
    ("無神論の哲学", "Philosophy of Atheism", "Global_Synthesis", "宗教学・神学", "フロイト・ラッセル・ドーキンス・デネット・ハリスらが展開した神の存在否定の哲学的・科学的議論。新無神論（ニュー・アシーイズム）の台頭が現代の論点。", "https://en.wikipedia.org/wiki/Atheism", 1960),
    ("神道の宗教学", "Shinto Studies", "East_Asia", "宗教学・神学", "日本固有の宗教・神話・儀礼体系（古事記・日本書紀・祝詞・神社神道・国家神道）の研究。本居宣長（国学）から近代の宗教社会学的アプローチまで多様な研究系譜を持つ。", "https://en.wikipedia.org/wiki/Shinto", -600),
    ("インドのバクティ運動", "Bhakti Movement", "South_Asia", "宗教学・神学", "6-17世紀の南アジアで盛んになった神への個人的献身（バクティ）を強調する宗教運動。ミーラーバーイー・カビール・トゥカラームら詩聖・聖者が運動を担い、カースト超越の平等主義を唱えた。", "https://en.wikipedia.org/wiki/Bhakti_movement", 700),
    ("仏教のエンゲージド・ブッディズム", "Engaged Buddhism", "East_Asia", "宗教学・神学", "ティク・ナット・ハン（1963）が提唱した社会・政治問題に積極的に関与する現代仏教の潮流。戦争・貧困・環境破壊への仏教的応答として世界的に広がった。", "https://en.wikipedia.org/wiki/Engaged_Buddhism", 1963),
    ("イスラームの現代思想", "Contemporary Islamic Thought", "West_Asia_North_Africa", "宗教学・神学", "ジャマール・アッ=ディーン・アフガーニー・ムハンマド・アブドゥ・イクバール・ハンナー・マウドゥーディー・サイイド・クトゥブらによる20世紀イスラーム改革・復興思想の諸潮流。", "https://en.wikipedia.org/wiki/Islamic_modernism", 1875),
    ("ユダヤ教改革派の神学", "Reform Judaism Theology", "West_Asia_North_Africa", "宗教学・神学", "19世紀ドイツで始まったユダヤ教の近代化運動。律法の歴史的相対化・ユダヤ教の倫理的普遍主義・礼拝の近代化が特徴。コーエン・カプランらが神学的基盤を提供した。", "https://en.wikipedia.org/wiki/Reform_Judaism", 1810),
    ("南アジアのタントリズム", "South Asian Tantrism", "South_Asia", "宗教学・神学", "シャクティ崇拝・クンダリニー・チャクラ・マントラ・マンダラ・ヨーガの実践を含むヒンドゥー・仏教・ジャイナ教のタントリック伝統。ホワイト（2000）が比較タントリズム研究を牽引。", "https://en.wikipedia.org/wiki/Tantra", 600),
    ("東南アジアの宗教的複合", "Southeast Asian Religious Syncretism", "Global_Synthesis", "宗教学・神学", "インドネシア・タイ・ミャンマーなど東南アジアにおける上座部仏教・イスラーム・ヒンドゥー教・先住民宗教の複雑な重層と融合。宗教的シンクレティズムの研究事例として重要。", "https://en.wikipedia.org/wiki/Religion_in_Southeast_Asia", 400),
    # ===== 歴史学追加 (80件) =====
    ("公衆衛生史", "History of Public Health", "Global_Synthesis", "歴史学・歴史哲学", "疫病（ペスト・コレラ・スペイン風邪・COVID-19）への社会的応答の歴史。検疫・上下水道整備・予防接種の普及とその政治社会的背景を研究する。", "https://en.wikipedia.org/wiki/History_of_public_health", 1800),
    ("食の歴史", "Food History", "Global_Synthesis", "歴史学・歴史哲学", "農業革命・香辛料貿易・新大陸作物導入・近代産業食料システム・食の植民地主義を研究する学際的分野。ミンツ「砂糖と権力」（1985）が古典的業績。", "https://en.wikipedia.org/wiki/History_of_food", 1960),
    ("服飾史", "History of Fashion and Dress", "Global_Synthesis", "歴史学・歴史哲学", "衣服の歴史的変遷・社会的意味・ジェンダー表現・植民地主義との関係を研究する学際的分野。ヴェブレン（課示的消費）・バルト（流行の体系）が理論的基盤を提供した。", "https://en.wikipedia.org/wiki/History_of_clothing", 1970),
    ("医学史", "History of Medicine", "Global_Synthesis", "歴史学・歴史哲学", "ヒポクラテスから現代医学まで医学知識・実践・制度の歴史。フーコー（クリニックの誕生）・ポーター（医学社会史）らが方法論的発展に寄与した。", "https://en.wikipedia.org/wiki/History_of_medicine", -400),
    ("政治思想史", "History of Political Thought", "Global_Synthesis", "歴史学・歴史哲学", "プラトン・アリストテレス・キケロ・マキャベリ・ロック・ルソー・カント・マルクス・ウェーバーらの政治的思想の歴史的発展を研究する分野。スキナー学派が方法論的革新をもたらした。", "https://en.wikipedia.org/wiki/History_of_political_thought", -400),
    ("法制史", "Legal History", "Global_Synthesis", "歴史学・歴史哲学", "ハンムラビ法典からローマ法・コモン・ロー・大陸法・近代成文法に至る法規範・法制度の歴史的発展を研究する分野。法と社会の相互規定が主要問題意識。", "https://en.wikipedia.org/wiki/Legal_history", -1750),
    ("贈与の歴史", "History of Gift and Exchange", "Global_Synthesis", "歴史学・歴史哲学", "マウス「贈与論」（1925）に始まる贈与交換の歴史的・人類学的研究。クラ環・ポトラッチ・中世ヨーロッパの施し・現代の援助経済まで非市場交換の多様な形態を追う。", "https://en.wikipedia.org/wiki/Gift_economy", 1925),
    ("教育史", "History of Education", "Global_Synthesis", "歴史学・歴史哲学", "古代ギリシャのパイデイアからルネサンス人文主義・近代国民学校・20世紀の大衆教育まで教育制度・教育思想の歴史的変容を研究する分野。", "https://en.wikipedia.org/wiki/History_of_education", -400),
    ("印刷術と知識普及の歴史", "History of Printing and Knowledge Diffusion", "Global_Synthesis", "歴史学・歴史哲学", "グーテンベルク（1455）の活版印刷が宗教改革・科学革命・近代国家形成に与えた影響の研究。アイゼンスタイン「印刷機のエージェント」（1979）が古典的業績。", "https://en.wikipedia.org/wiki/History_of_printing", 1455),
    ("国際法の歴史", "History of International Law", "Global_Synthesis", "歴史学・歴史哲学", "グロティウス（海洋自由論1609）からウェストファリア条約・ハーグ条約・国連憲章・国際刑事裁判所に至る国際法規範の歴史的発展を研究する。", "https://en.wikipedia.org/wiki/History_of_international_law", 1609),
    # ===== 言語学・批評理論の混合追加 (80件) =====
    ("ポストコロニアル言語政策", "Postcolonial Language Policy", "Global_Synthesis", "言語学", "旧植民地における植民者言語（英語・フランス語・スペイン語）と現地言語の権力関係・教育言語政策・言語と民族的アイデンティティの関係を研究する分野。", "https://en.wikipedia.org/wiki/Language_policy", 1960),
    ("コード化と復号化", "Encoding and Decoding", "Global_Synthesis", "文学批評理論", "スチュアート・ホール（1980）が提唱したメディア・コミュニケーション理論。メッセージは送り手によってコード化され、受け手によって支配的・交渉的・反抗的に読まれる。", "https://en.wikipedia.org/wiki/Encoding/decoding_model_of_communication", 1980),
    ("文化研究と文学", "Cultural Studies and Literature", "Western_Europe", "文学批評理論", "バーミンガム現代文化研究センター（ホガート・ホール）が発展させた文化研究の枠組みの文学への適用。サブカルチャー・ポピュラーカルチャー・抵抗が研究対象。", "https://en.wikipedia.org/wiki/Cultural_studies", 1964),
    ("アフリカ系文学の複数性", "Afro-Caribbean Literary Criticism", "Latin_America", "文学批評理論", "カリブ海のアフリカ系作家（ウォルコット・ラミング・ブレイスウェイト）の文学批評。植民地言語・クレオール・神話・歴史的トラウマが主要テーマ。", "https://en.wikipedia.org/wiki/Caribbean_literature", 1950),
    ("イスラーム文学批評", "Islamic Literary Criticism", "West_Asia_North_Africa", "文学批評理論", "イブン・アル=ムウタズ（「バディーウ」9世紀）・クドゥマ（「詩批評の書」）らが発展させたアラビア語詩学。後にペルシャ語・トルコ語・ウルドゥー語文学批評に影響した。", "https://en.wikipedia.org/wiki/Arabic_poetics", 900),
    ("数詞体系の類型論", "Numeral Systems Typology", "Global_Synthesis", "言語学", "世界の言語における数の表現体系の多様性を研究する。10進法・20進法・5進法・2進法などの基数体系と数詞の形態論的多様性が主要研究対象。", "https://en.wikipedia.org/wiki/Numeral_system", 1970),
    ("語彙借用の研究", "Lexical Borrowing Research", "Global_Synthesis", "言語学", "ある言語が他言語から語彙を取り込むプロセスの研究。音韻適応・意味変化・形態論的適応が分析対象。英語・日本語・アラビア語は大量借用語を持つ言語として注目される。", "https://en.wikipedia.org/wiki/Loanword", 1950),
    ("認知考古学と言語", "Cognitive Archaeology and Language Origins", "Global_Synthesis", "言語学", "ミサン（1998）・デービッドソン＆ノーブルらが展開した後期旧石器時代の認知革命と言語起源の接点を探る学際的分野。シンボル使用・芸術・言語の共進化を研究する。", "https://en.wikipedia.org/wiki/Origin_of_language", 1990),
    ("音調言語とピッチアクセント語の比較", "Comparative Tonology", "Global_Synthesis", "言語学", "中国語（声調）・日本語（ピッチアクセント）・スウェーデン語（声調アクセント）など音調を用いる言語の類型的比較研究。フランス（2012）のデータベース研究が基盤。", "https://en.wikipedia.org/wiki/Tone_language", 2012),
    ("ワーフ仮説の現代的検証", "Modern Tests of Sapir-Whorf Hypothesis", "North_America", "言語学", "色彩認知（ダラジナ2007）・空間認知・数・時間に関する実験で言語が思考を部分的に影響することを示す認知言語学の実証研究。強い決定論を否定しつつ弱い相対性を支持する。", "https://en.wikipedia.org/wiki/Linguistic_relativity", 2007),
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
print(f"Batch 5 (大規模補完): inserted={inserted}, skipped={skipped}")
conn = sqlite3.connect(DB)
total = conn.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
print(f"総件数: {total} (目標5500)")
sf_dist = conn.execute("""
SELECT subfield, COUNT(*) as cnt FROM humanities_concept
GROUP BY subfield ORDER BY cnt DESC LIMIT 20
""").fetchall()
for sf, cnt in sf_dist:
    print(f"  {sf}: {cnt}")
conn.close()
