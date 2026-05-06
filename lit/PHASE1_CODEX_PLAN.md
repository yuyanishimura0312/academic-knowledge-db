# LIT-DB Phase 1: Codex 20名 × サブフィールド対応 調査計画

**作成日**: 2026-05-07
**作成者**: academic-db-survey（Phase 1 担当）
**対象**: Phase 0 で確定した Codex 20名（C01-C20）の Phase 2 における30日間週次マイルストーン
**前提**: PROJECT_PLAN の 30日間 Phase 2、5週間構成、平均 concepts 73件/日（11,000 / 150 person-days）

---

## 0. 本書の位置づけ

Phase 0 で確定した 20名配置（PHASE0_SCOPE_REPORT.md 表5.1）を踏まえ、各員が Phase 2 の30日間で何をどの順序で行うかを週次マイルストーンとして定義する。第1週はキックオフと正典リスト作成、第2週は一次資料アクセス確立と最初の100概念収集、第3-4週は主要収集、第5週は関係性記述と cross_domain リンクという5フェーズ構成を全員共通とする。

各員には主担当サブフィールドのほか、副担当（隣接領域への補助）と検証協力（C20の補助）の3層タスクがある。本計画は主担当の進捗を中心に記述する。

---

## 1. Codex 20名 全体配置一覧

| # | Codex ID | 担当領域 | 主パターン | 副パターン | 目標concepts | 目標authors | 目標works | 目標movements |
|---|---|---|---|---|---:|---:|---:|---:|
| C01 | LIT-Classical-Antiquity | 古典古代文学 | パターン1 | パターン3 | 500 | 100 | 220 | 25 |
| C02 | LIT-EU-Medieval | 中世文学 | パターン1 | パターン2 | 400 | 80 | 200 | 25 |
| C03 | LIT-EU-EarlyModern | ルネサンス・近世文学 + 啓蒙ロマン主義 | パターン2 | パターン1 | 1,000 | 220 | 530 | 60 |
| C04 | LIT-EU-Modern | リアリズム・モダニズム・ポストモダン | パターン2 | パターン3 | 1,600 | 370 | 800 | 80 |
| C05 | LIT-CN-Classical | 中国古典文学 | パターン1 | パターン4 | 600 | 150 | 280 | 25 |
| C06 | LIT-CN-Modern | 中国近現代文学 | パターン2 | パターン4 | 400 | 100 | 180 | 20 |
| C07 | LIT-JP-Classical | 日本古典文学 | パターン1 | パターン2 | 500 | 120 | 250 | 25 |
| C08 | LIT-JP-Modern | 日本近現代文学 | パターン2 | パターン4 | 500 | 130 | 250 | 25 |
| C09 | LIT-India | インド文学 | パターン1+4 | パターン2 | 500 | 120 | 230 | 25 |
| C10 | LIT-Arab-Persian-Turkish | アラブ・ペルシア・トルコ | パターン1+4 | パターン2 | 700 | 160 | 330 | 35 |
| C11 | LIT-Africa | アフリカ文学 | パターン4 | パターン2 | 400 | 90 | 170 | 25 |
| C12 | LIT-LatinAmerica | ラテンアメリカ文学 | パターン4+2 | パターン1 | 500 | 110 | 220 | 25 |
| C13 | LIT-SEAsia-Korea | 東南アジア・韓国文学 | パターン4 | パターン2 | 300 | 80 | 150 | 20 |
| C14 | LIT-Russia-Slavic | ロシア・スラヴ文学 | パターン2 | パターン1 | 400 | 100 | 200 | 20 |
| C15 | LIT-Indigenous-Oral | 先住民・口承文学 | パターン4 | パターン1 | 400 | 80 | 150 | 30 |
| C16 | LIT-Diaspora | ディアスポラ・移民文学 | パターン4 | パターン2 | 400 | 100 | 170 | 20 |
| C17 | LIT-Genre | 児童・大衆・ジャンル文学 | パターン2 | パターン4 | 300 | 80 | 200 | 20 |
| C18 | LIT-Theory | 文学理論・批評 | パターン3 | パターン2 | 700 | 200 | 100 | 30 |
| C19 | LIT-WorldLit-DH | 比較文学・翻訳論 + DH/AI | パターン3+5 | パターン2 | 900 | 250 | 160 | 35 |
| C20 | LIT-Verifier | 全領域品質保証・cross_domain・横断検証 | （検証専従） | パターン5補助 | 検証 | 検証 | 検証 | 検証 |
| **計** | | | | | **11,000** | **2,640** | **4,810** | **610** |

注釈: C03 と C04 は西欧近世〜現代で負荷が大きく、Phase 2 中盤（15日目）の進捗判定で必要に応じてサブ分割（C03a/C03b, C04a/C04b）する。C19 は比較文学・翻訳論（500 concepts）と DH/AI（400 concepts）の合算で900 concepts、Phase 5 横断パターンは C19 が主担当・C20 が検証として分担する。

---

## 2. 共通5週間マイルストーン構成

全Codexは以下の5週間構成に従う。各週末にC20と西村への週次レポートを提出する。

### Week 1（Day 1-7）: キックオフ・正典リスト作成
- Day 1: 全員キックオフ（PHASE1_AXES_DEFINITION・PHASE1_REFERENCE_PATTERNS・PHASE1_CODEX_PLAN の読み込み、質疑）
- Day 2-3: 主担当領域の正典リスト作成（30-50件の起点作品/作家/運動/理論家）
- Day 4-5: 一次資料アクセス可否確認（24領域すべての契約・URL・API有効性）、不在資料は代替源を提案
- Day 6-7: 最初の20-30概念を試行投入し、入力フォーマット・source_tier 判定基準を C20 と擦り合わせ

### Week 2（Day 8-14）: 一次資料アクセス確立・最初の100概念
- Day 8-10: 主担当領域で concepts 50件、authors 10件、works 15件、movements 2件を目標
- Day 11-12: 担当領域の運動・主要作品ネットワークを概観し、Phase 2 収集の優先順位を確定
- Day 13-14: 累計100概念到達、C20 による初回監査受け入れ

### Week 3（Day 15-21）: 主要収集前半
- 各員 1日あたりの収集ペース目安（パターン別）に従って収集
- Day 15: 西村・オーケストレーターによる中間進捗レビュー、必要に応じて C03/C04 のサブ分割判断
- Day 16-21: concepts 累計を目標の50%に到達させる

### Week 4（Day 22-28）: 主要収集後半・関係性記述
- Day 22-25: concepts 残りの収集
- Day 26-28: relations / geneal_links の本格記述開始（収集と並行して関係性を記述する）

### Week 5（Day 29-30+α）: 関係性構築・cross_domain・第四変容タグ
- Day 29: 各員 relations 累計を目標数の70%に到達
- Day 30: cross_domain（PHIL/PT/AN/MG/Era-Talents への接続）と fourth_transform_tags の集中付与
- Day 30+α: C20 による全体監査、Phase 3（検証）への引き継ぎ

---

## 3. Codex 個別週次マイルストーン

### C01: 古典古代文学（500 concepts / 100 authors / 220 works / 25 movements）

**Week 1**: ホメロス・ギリシャ三大悲劇詩人・プラトン・アリストテレス・ウェルギリウス・ホラティウス・聖書文学を起点リストに。Perseus / TLG / Loeb / Sefaria のアクセス確認。

**Week 2**: 古典古代の概念100件（mimesis、catharsis、hubris、nomos、logos、ethos、pathos、kalokagathia、aretē、agonos等）を一次資料 Perseus 経由で投入。Loeb 批判校訂版を併用。

**Week 3-4**: 詩人・哲学者・歴史家・劇作家を100名まで。叙事詩・悲劇・喜劇・抒情詩・歴史叙述の代表作 220件。movements は古代の悲劇詩人グループ・ヘレニズム期アレクサンドリア学派等25件。

**Week 5**: relations は古典古代内（プラトン→アリストテレス→ヘレニズム哲学）を中心に、cross_domain は PHIL（ギリシャ哲学概念）・PT（古典詩学）に重点付与。第四変容タグは「物語」「正典」「翻訳」軸に重点。

### C02: 中世文学（400 concepts / 80 authors / 200 works / 25 movements）

**Week 1**: ベーオウルフ・神曲・カンタベリー物語・ニーベルンゲンの歌・アーサー王伝説・トリスタンとイズー・ローランの歌を起点に。MGH digital / TEAMS / Bibliotheca Augustana / Gallica のアクセス確認。

**Week 2**: 中世概念100件（騎士道 chivalry、宮廷愛 amour courtois、寓意 allegoria、四段階聖書解釈、imitatio Christi、auctoritas等）を MGH/TEAMS から取得。多言語（古英語・中英語・古フランス語・中高ドイツ語・古ノルド語・教会ラテン語）に対応した original_script 記録。

**Week 3-4**: 作家80名（オリジナルが多くは匿名のため author_name_text を活用）、作品200件、運動25件（騎士道物語・寓意文学・吟遊詩人・修道院文献・神秘主義文学）。

**Week 5**: 古典古代との連続性（geneal_links: Boethius → 中世スコラ）、ルネサンスへの橋渡し（geneal_links: Dante → ルネサンス）を記述。

### C03: ルネサンス・近世文学 + 啓蒙ロマン主義（1,000 concepts / 220 authors / 530 works / 60 movements）

**Week 1**: シェイクスピア・セルバンテス・ダンテ・ペトラルカ・ボッカチオ・ラブレー・モンテーニュ・ミルトン・ゲーテ・シラー・ワーズワース・コールリッジを起点に。Folger / EEBO / Gutenberg / DTA / ARTFL のアクセス確認。Day 15 のサブ分割判断に向けて進捗を可視化。

**Week 2-4**: 1日40-50 concepts 平均で集中収集。人文主義 / マニエリスム / バロック / 古典主義 / 啓蒙 / 前ロマン / 独・英・仏ロマン主義 / ゴシックの計60運動を体系的に。シェイクスピア研究は Folger Shakespeare Digital Texts を主源とする。

**Week 5**: 大規模な geneal_links 構築（古典回帰の系譜、シェイクスピア→ロマン主義の影響、ゲーテ→世界文学）。cross_domain は PHIL（人文主義哲学・啓蒙哲学・ロマン主義美学）に重点。第四変容タグは「作者性」「創造性」軸に重点（ルネサンス以降の個人作者の浮上、ロマン主義独創性の生成）。

### C04: リアリズム・モダニズム・ポストモダン（1,600 concepts / 370 authors / 800 works / 80 movements）

**Week 1**: バルザック・ディケンズ・ドストエフスキー・トルストイ・フローベール・ジョイス・プルースト・カフカ・ウルフ・ベケット・ボルヘス・ピンチョン・デリーロ等を起点に。Modernist Journals Project / JSTOR / Project MUSE のアクセス確認。

**Week 2-4**: 1日50-60 concepts ペースで収集。リアリズム / 自然主義 / 象徴主義 / モダニズム前期・ハイ・後期 / 戦後 / ポストモダン / メタフィクション / autofiction の計80運動。著作権下作品は二次文献ベース、source_tier は'tertiary'を多用。

**Week 5**: 20世紀文学の高密度な geneal_links（モダニズム継承、ポストモダンの自己言及性）、cross_domain は PHIL（実存主義・現象学・ポスト構造主義）と AI Development DB（戦後 SF からAI 時代への継承）。

### C05: 中国古典文学（600 concepts / 150 authors / 280 works / 25 movements）

**Week 1**: 詩経・楚辞・史記・三国志演義・水滸伝・西遊記・紅楼夢・李白・杜甫・蘇軾を起点に。CTEXT / 維基文庫 / Scripta Sinica / Kanripo のアクセス確認。

**Week 2**: 先秦から清末までの主要概念100件（詩、詞、文、賦、章回、興、比、賦、神韻、性靈、格律、言志、緣情等）を CTEXT から原文取得、original_script='kanji' を必須記録。

**Week 3-4**: 唐詩・宋詞・元曲・明清小説・四大奇書・章回小説の体系。movements は建安文学・古文運動（韓愈・柳宗元）・性靈派・桐城派等25件。

**Week 5**: 日本古典・韓国古典への波及を geneal_links で記録（漢字文化圏の系譜）。cross_domain は PHIL（儒教・道教・仏教思想）への接続。

### C06: 中国近現代文学（400 concepts / 100 authors / 180 works / 20 movements）

**Week 1**: 魯迅・茅盾・巴金・老舎・沈従文・莫言・余華・閻連科を起点に。CNKI（要契約確認）/ MCLC / 維基文庫のアクセス確認。

**Week 2-4**: 五四運動以降の運動20件（新文学運動・革命文学・京派・海派・尋根文学・先鋒文学・新写実主義等）、概念400件、作家100名、作品180件。

**Week 5**: 中国古典との断絶と継承（geneal_links: 古典→五四の批判的継承）、世界文学・翻訳論との接続（C19 と協働）。

### C07: 日本古典文学（500 concepts / 120 authors / 250 works / 25 movements）

**Week 1**: 万葉集・古今和歌集・源氏物語・枕草子・徒然草・能・狂言・西行・芭蕉・近松門左衛門・井原西鶴を起点に。NIJL 新日本古典籍総合データベース / NDL / J-STAGE / 青空文庫のアクセス確認。

**Week 2-4**: 上代・中古・中世・近世の体系的収集。概念（あはれ・幽玄・わび・さび・本歌取り・歌枕・縁語・枕詞・かけことば・まこと・うつろい等）500件、和歌・物語・随筆・能楽・俳諧・人形浄瑠璃の作品250件。movements は六歌仙・八代集編纂・蕉風俳諧・浮世草子・読本等25件。

**Week 5**: 中国古典との接触史（geneal_links: 漢詩→和歌、和漢混淆文）、cross_domain は PT（俳諧詩学）・AN（日本文化研究）。第四変容タグは「物語」「言語」軸に重点。

### C08: 日本近現代文学（500 concepts / 130 authors / 250 works / 25 movements）

**Week 1**: 二葉亭四迷・夏目漱石・森鷗外・芥川龍之介・志賀直哉・谷崎潤一郎・川端康成・三島由紀夫・大江健三郎・村上春樹を起点に。青空文庫 / NDL / CiNii / J-STAGEのアクセス確認。

**Week 2-4**: 明治・大正・昭和戦前・戦後・現代の体系。運動25件（写実主義・浪漫主義・自然主義・耽美派・白樺派・新感覚派・プロレタリア文学・第一次戦後派・内向の世代・J文学等）、私小説・心境小説・大衆文学・推理小説・SF等のジャンル発展を記録。

**Week 5**: 西欧モダニズムとの接触（geneal_links: 仏自然主義→日本自然主義）、戦後文学から現代の系譜、第四変容タグは「作者性」（私小説の作者-人物同一性問題）と「主体」軸に重点。

### C09: インド文学（500 concepts / 120 authors / 230 works / 25 movements）

**Week 1**: ヴェーダ・ラーマーヤナ・マハーバーラタ・カーリダーサ・バクティ詩人（カビール・トゥルシーダース・ミーラーバーイー）・タゴール・プレームチャンドを起点に。GRETIL / SARIT / Sanskrit Heritage / Murty Classical Library のアクセス確認。

**Week 2-3**: サンスクリット古典領域はパターン1で集中（Sanskrit Heritage Site の形態素解析を活用）、概念250件（rasa、dhvani、alamkara、bhava、abhinaya、kavya、shastra等）を原語表記必須で。

**Week 4**: バクティ運動以降のインド諸言語文学（ヒンディー・ベンガル・タミル・テルグ・マラヤラム等）はパターン4で。Murty Classical Library を経由した英訳併載で原語に遡及。

**Week 5**: 仏典との接続（geneal_links: サンスクリット仏典→中国仏典、漢訳）、cross_domain は PHIL（インド哲学）・PT（rasa 詩学、Poetics DB と密接）に重点。

### C10: アラブ・ペルシア・トルコ文学（700 concepts / 160 authors / 330 works / 35 movements）

**Week 1**: ジャーヒリーヤ詩・千夜一夜・アル＝ハリーリー・イブン＝アラビー・ナギーブ・マフフーズ・フェルドウスィー・ハーフェズ・ルーミー・サアディ・オスマン古典詩を起点に。Al-Maktaba al-Shamela / OpenITI / Ganjoor / Iranica / İslam Ansiklopedisi のアクセス確認。

**Week 2-3**: アラブ古典領域 400件（balagha、bayan、badi、qasida、ghazal、maqama、adab等）。OpenITI から原文取得、original_script='arabic' 必須。

**Week 4**: ペルシア古典 200件（Ganjoor.net 経由）、トルコ古典 100件（İslam Ansiklopedisi 経由）。ナフダ（19c）・現代アラブ小説の追加。

**Week 5**: イスラム文化圏内の伝播（アラビア語→ペルシア語→オスマン・トルコ語の系譜）を geneal_links で記録、cross_domain は PHIL（イスラム哲学）に重点。

### C11: アフリカ文学（400 concepts / 90 authors / 170 works / 25 movements）

**Week 1**: ネグリチュード（Senghor, Césaire）・Achebe・Soyinka・Ngũgĩ wa Thiong'o・Ben Okri・Adichie・口承伝統（Sundiata, Mwindo）を起点に。African Storybook / WOLP / AJOL のアクセス確認。

**Week 2-3**: パターン4（地域・言語クラスター）で集中。アフリカ言語（スワヒリ・ヨルバ・ハウサ・ズールー）と植民地言語（英・仏・葡）の二層で組織化。概念200件。

**Week 4**: 運動25件（Negritude、Onitsha Market Literature、African Renaissance、Pan-Africanism Literary Branch等）、作品170件。

**Week 5**: ヨーロッパ文学・ラテンアメリカ文学への影響（geneal_links: négritude → caribbean créolité）、cross_domain は AN（アフリカ研究、文化的所有権）に重点。第四変容タグは全9軸に高頻度付与（特に「正典」「真正性」「言語」）。

### C12: ラテンアメリカ文学（500 concepts / 110 authors / 220 works / 25 movements）

**Week 1**: ボルヘス・コルタサル・ガルシア＝マルケス・リョサ・フエンテス・ネルーダ・パス・ボラーニョ・先住民起源の伝承（ポポル・ブフ等）を起点に。Biblioteca Virtual Miguel de Cervantes / Memoria Chilena / JSTOR のアクセス確認。

**Week 2-3**: 植民地期（クロニカ・先住民伝承）・独立後ロマン主義・モデルニスモ・ブーム期・ポスト・ブームの体系。概念300件、運動25件。

**Week 4**: 先住民文学（ナワトル・ケチュア・グアラニ）はパターン4で別途、200件。

**Week 5**: スペイン文学・ヨーロッパモダニズムとの接続、世界文学への波及（魔術的リアリズムの世界的影響）を geneal_links で。第四変容タグは「主体」「真正性」軸に重点。

### C13: 東南アジア・韓国文学（300 concepts / 80 authors / 150 works / 20 movements）

**Week 1**: 韓国（鄭夢周・許筠・李光洙・李箱・現代詩）・ベトナム（チューノム文学・キエウ伝・現代）・インドネシア（プラムディヤ）・タイ（クムシン王朝古典）・フィリピン（リサール）を起点に。NLK / LTI Korea / Vietnamese Nôm Preservation Foundation / SEAlang のアクセス確認。

**Week 2-4**: 韓国古典（漢字文化圏）・植民地期・戦後・現代を体系。概念300件のうち韓国150・ベトナム80・インドネシア40・タイ20・フィリピン10程度の配分。

**Week 5**: 中国古典・日本古典との接続（漢字文化圏の系譜）、ヨーロッパ植民地言語との関係（geneal_links: 仏領印度支那→ベトナム近代文学）。

### C14: ロシア・スラヴ文学（400 concepts / 100 authors / 200 works / 20 movements）

**Week 1**: ドストエフスキー・トルストイ・チェーホフ・ゴーゴリ・プーシキン・銀の時代詩人（ブロック、アフマートヴァ等）・ナボコフ・ソルジェニーツィン・パステルナークを起点に。Russian Virtual Library / FEB / Gutenberg / TITUS のアクセス確認。

**Week 2-4**: 古ルーシ・18c古典主義・19c黄金時代・銀の時代・ソ連期・ソ連後の体系。概念400件、作家100名、運動20件（スラヴ派・西欧派・象徴主義・アクメイズム・社会主義リアリズム等）。

**Week 5**: バフチン理論・形式主義との接続（geneal_links: シクロフスキー異化→バフチン対話→西欧構造主義）、cross_domain は PT（理論）・PHIL に重点。

### C15: 先住民・口承文学（400 concepts / 80 authors / 150 works / 30 movements）

**Week 1**: ネイティブアメリカン（ナバホ、イヌイット、ホピ）・アボリジニ（ドリーミング物語）・アイヌ（カムイユカラ、ユカラ）・サーミ・マオリの口承伝統を起点に。WOLP / ELAR / PARADISEC / 国立アイヌ民族博物館 / Smithsonian NAA のアクセス確認。

**Week 2-3**: パターン4で集中。primary_source_type に 'oral_recording' / 'transcribed_oral' / 'collector_record' を厳密区別。アイヌ150件・北米200件・豪州100件・サーミ50件等の配分。

**Week 4**: 文化圏ごとの「口承の運動」（中継伝承者・口承詩人グループ）を movements として30件。

**Week 5**: cross_domain は AN（人類学）と高密度連携、Traditional Knowledge DB との接続も検討。第四変容タグは全9軸で高頻度（特に「正典」「真正性」「言語」「翻訳」軸）。

### C16: ディアスポラ・移民文学（400 concepts / 100 authors / 170 works / 20 movements）

**Week 1**: Naipaul・Rushdie・Lahiri・Nguyen Thanh Viet・Mo Yan の海外受容・在日朝鮮人文学（金石範、李恢成）・在米中国系・在英南アジア系等を起点に。JSTOR / Project MUSE / AAWW のアクセス確認。

**Week 2-4**: 戦前移民・ポストコロニアル・21世紀グローバルの3層で組織化。translingual writing、自己翻訳、第三空間（Bhabha）等の理論概念も含む。

**Week 5**: 出身地文学・受け入れ地文学との二重接続（geneal_links: 出身地→ディアスポラ作家、受け入れ地伝統→ディアスポラ作家）。cross_domain は AN（移動・境界・アイデンティティ）に重点。第四変容タグは「主体」「言語」「真正性」軸に重点。

### C17: 児童・大衆・ジャンル文学（300 concepts / 80 authors / 200 works / 20 movements）

**Week 1**: SF（Asimov, Le Guin, 伊藤計劃）・ファンタジー（Tolkien, Le Guin）・推理（Christie, 江戸川乱歩）・児童（Andersen, 宮沢賢治）・パルプ・コミックス（Tezuka）を起点に。ISFDB / Pulp Magazines Project / Baldwin Library / Comic Book Plus のアクセス確認。

**Week 2-4**: ジャンル別の体系化（SF/ファンタジー/推理/ホラー/児童/パルプ/コミックス）、19c起源・20c黄金期・戦後成熟・現代の時代区分で組織化。

**Week 5**: 大衆文学から正典文学への昇格事例（geneal_singularity links）、cross_domain は AI Development DB（SF とAI 概念の関係）。

### C18: 文学理論・批評（700 concepts / 200 authors / 100 works / 30 movements）

**Week 1**: ロシア・フォルマリズム・プラハ言語学派・新批評・神話批評・構造主義・ポスト構造主義・脱構築・読者反応批評・フェミニズム批評・ポストコロニアル批評・エコクリティシズムの系譜を起点に。SEP / PhilPapers / Cambridge Companions のアクセス確認。

**Week 2-3**: パターン3（理論家・批評家系譜）の中核実装。理論家200名（シクロフスキー、ヤコブソン、バフチン、バルト、デリダ、フーコー、クリステヴァ、ジュネット、Said、Spivak、Bhabha、Butler、Buell等）の概念を集中収集。

**Week 4**: 学派30件（Russian Formalism, Prague School, New Criticism, Structuralism, Yale School等）、理論的著作100件。

**Week 5**: 高密度な geneal_links（4世代以上の系譜を多数）、cross_domain は PHIL に重点（哲学と理論の境界が曖昧）。第四変容タグは全9軸でほぼ全件に付与（理論領域は再考の核）。

### C19: 比較文学・世界文学・翻訳論 + DH/AI（900 concepts / 250 authors / 160 works / 35 movements）

**Week 1**: ゲーテのWeltliteratur・Auerbach・Curtius・Casanova・Damrosch・Apter・Spivak『planetarity』・Moretti distant reading・Stanford Literary Lab・Electronic Literature Organization の系譜を起点に。BTSB / Index Translationum / ELO / arXiv（cs.CL）のアクセス確認。

**Week 2-3**: 比較文学・翻訳論の理論家250名・概念500件。翻訳研究は Benjamins Translation Studies Bibliography を主源。世界文学論は Casanova『La République mondiale des lettres』、Damrosch『What is World Literature?』等。

**Week 4**: DH/AI領域の400 concepts。電子文学（ELO Vol.1-3 の作品）、デジタル人文学手法、生成AI関連の批評論考（Critical AI 誌等）を集中収集。

**Week 5**: 第四変容軸（パターン5）の主担当として、全領域横断のタグ付与作業のリーダー役。C20と協働。cross_domain は AI Development DB と高密度連携。

### C20: 全領域品質保証・横断検証（検証専従）

**Week 1**: 全 Codex のキックオフ参加、入力フォーマットと判定基準の擦り合わせを主導。

**Week 2**: 各 Codex の最初の100概念について、source_tier 判定の妥当性・name_original 表記の正確性・引用の一次資料合致を抽出検査。

**Week 3-4**: 週次サンプリング監査（各員の概念から無作為に20件抽出して検証）、矛盾発見時の差し戻し。並行して cross_domain の妥当性検査（PHIL/PT/AN/MG/Era-Talents への接続が形式的でないか）。

**Week 5**: 全データの統合検査。重複検出、第四変容タグの軸間整合性、importance_score の偏り検査。Phase 3（検証・整理）への引き継ぎ準備。

---

## 4. リスクと対応

### 4.1 C03/C04 の負荷集中
西欧近世〜現代の負荷が突出する。Day 15 の中間レビューで進捗が当該日数比例の80%を切る場合、C03 を C03a（ルネサンス・近世）と C03b（啓蒙・ロマン）に、C04 を C04a（リアリズム・自然主義・象徴主義）と C04b（モダニズム・ポストモダン）に分割する。分割時の追加 Codex 2名は別予備プールから割り当てる前提とする。

### 4.2 アクセス困難領域（C13・C15）
東南アジア・韓国（C13）と先住民・口承（C15）は資料アクセスが最難関。Week 1 の段階で利用可能資料を確定し、目標未達リスクが高い場合は Phase 2 開始前に目標数の下方修正（300→200、400→300）を西村に提案する。

### 4.3 著作権下作品の収集
20-21世紀作品は PD原典が利用できないため、二次文献ベースで概念抽出を行う。`source_tier='tertiary'` を必須記録し、Phase 3 で再検査対象とする。Codex は二次文献の合致確認（最低3件）を Week 2 までに体制化する。

### 4.4 横断検証の遅延リスク
C20 単独で20名の検証を行うため、Week 3 以降に検証遅延が発生する可能性がある。週次レポートで C20 の検証残件数を可視化し、3週連続で残件が増加する場合、検証補助 Codex 1名（C04や別予備プール）を C20 に転用する。

---

## 5. Phase 1 完了確認

- 20名全員の主担当・副担当・目標数を確定
- 共通5週間マイルストーン構成を確立
- 各員の週次タスクを Week 1〜Week 5 にわたり記述
- リスク対応4項目を整理
- 本書を Phase 2 キックオフ資料として全員に配布

