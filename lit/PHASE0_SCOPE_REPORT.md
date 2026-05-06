# 文学学術知識DB（LIT-DB）Phase 0 スコーピング・レポート

**作成日**: 2026-05-06
**作成者**: academic-db-scope（Phase 0 担当）
**対象**: LIT-DB 24サブフィールド・11,000概念・全方法論的基盤
**ステータス**: 西村承認待ち（Phase 1 起動前ゲート）
**前提**: PROJECT_PLAN.md v0.1（規模・配分・スキーマは承認済み）

---

## 0. 要約

本レポートは、文学学術知識DB（LIT-DB）の24サブフィールド・11,000概念規模の構築に向けた一次資料源マッピング、収集目標マトリクス、第四変容タグ優先度、および収集難所への対応策を提示する。哲学DB構築で確立した「PD原典からの一次取得」原則を文学領域に拡張し、西欧中心主義の解体を構造に内在化させる配分（非西欧68.2%）を維持したまま、各領域に最低5つの実在する一次資料・学術DBを紐づけた。本レポートはPhase 1（調査設計）の起点として機能する。

LIT-DBは Poetics DB（PT, 1,121概念）の上位包含層として作品・作家・運動・地域伝統を扱い、詩学理論はPT側にリンクのみ残して二重化を防ぐ。第四変容期（AI社会）における「作者性」「創造性」「物語」「主体」「正典」「受容」「翻訳」「真正性」「言語」の9軸再考タグを全概念に付与することで、生成AI時代における文学概念の再構造化を可視化する。

---

## 1. 24サブフィールドごとの一次資料源マッピング

各サブフィールドに対して、信頼できる一次資料・PDテキストアーカイブ・主要学術DBを最低5つ列挙する。実在を確認できないものは「要確認」と明記し、Phase 1で精査する。各エントリには言語・カバー範囲・利用条件を併記した。本節の本文は、各領域における収集設計の前提を散文で説明する形式とする。

### 1.1 西欧文学系譜

#### (1) 古典古代文学（lit_eu_classical）

ギリシャ・ローマの古典は学術的整備が最も進んだ領域であり、PDテキストの一次入手と批判校訂版（Loeb等）の併用が標準パイプラインとなる。Perseus Digital Library（米Tufts大）はギリシャ語・ラテン語原典に英訳・形態素タグを併載しオープンアクセスで公開、TLG（Thesaurus Linguae Graecae）はホメロスから後期ビザンツまでのギリシャ語コーパスをカバーするが利用には機関契約が必要である。Loeb Classical Library digital（Harvard）は会員制だがほぼ全古典を批判校訂で網羅、Project Gutenbergは英訳PD版を補完する。聖書文学はBibleHub・Sefaria（ヘブライ語/ギリシャ語）が一次資料として有用。

主要源: Perseus Digital Library / TLG（Thesaurus Linguae Graecae）/ Loeb Classical Library Online / Project Gutenberg / Sefaria / BibleHub。
言語: 古典ギリシャ語・ラテン語・ヘブライ語・コイネー。利用条件: Perseus・Sefaria・BibleHub・Gutenbergはオープン、TLG・Loebは契約必要。

#### (2) 中世文学（lit_eu_medieval）

中世はラテン語・古フランス語・中高ドイツ語・古英語・古ノルド語など多言語が交錯し、修道院文献・騎士道物語・寓意文学・吟遊詩人作品が並列する。Monumenta Germaniae Historica（MGH）digitalがゲルマン圏のラテン語史料の標準、TEAMS Middle English Texts（Rochester大）は中英語作品の批判校訂版PDアクセス、Bibliotheca Augustanaは独語圏の古典・中世PDコーパスを提供する。Bibliothèque nationale de France のGallicaは古フランス語写本デジタル画像、Internet Medieval Sourcebook（Fordham）は史料英訳のオープンアーカイブとして補完的役割を持つ。

主要源: MGH digital / TEAMS Middle English Texts / Bibliotheca Augustana / Gallica（BnF）/ Internet Medieval Sourcebook / DMBS（Digital Medieval Manuscripts at Houghton, 要確認: 名称揺れあり）。

#### (3) ルネサンス・近世文学（lit_eu_renaissance）

シェイクスピアは Folger Shakespeare Library と Open Source Shakespeare の二大公開源があり、注釈・原典の両方がオープン提供される。EEBO（Early English Books Online）は1473-1700年の英書をほぼ全冊スキャン、機関契約だが研究標準。Internet Archive と HathiTrust は近世英・仏・伊・西語のPD版を網羅、Italian Petrarch Archive・Project Gutenbergはペトラルカ・ボッカチオ・セルバンテスのPD原典を補完する。

主要源: Folger Shakespeare Digital Texts / Open Source Shakespeare / EEBO（Early English Books Online）/ HathiTrust / Project Gutenberg / Internet Archive。

#### (4) 啓蒙・ロマン主義（lit_eu_enlightenment）

18-19世紀英米独仏の文学はProject Gutenberg・HathiTrust・Internet Archiveの3大PDアーカイブが主軸となる。ARTFL Project（シカゴ大）は仏語コーパス（百科全書・啓蒙文学等）を提供、Deutsches Textarchiv（DTA）は独語1600-1900年のコーパス、Wikisource（多言語）は校訂PDテキストの補完源として有用。

主要源: Project Gutenberg / HathiTrust / Internet Archive / ARTFL Project / Deutsches Textarchiv（DTA）/ Wikisource（多言語版）。

#### (5) リアリズム・自然主義・象徴主義（lit_eu_realism）

19世紀小説と象徴詩は同じく上記PDアーカイブで大半をカバー可能。フランス象徴派は Gallica（BnF）とWikisource仏語版、ロシア・北欧・南欧の19世紀作品はWikisource各言語版とProject Gutenbergの組合せで網羅する。MLA International Bibliographyは二次文献参照の標準（機関契約）。

主要源: Project Gutenberg / Gallica（BnF）/ Wikisource多言語 / HathiTrust / MLA International Bibliography / JSTOR。

#### (6) モダニズム（lit_eu_modernism）

20世紀前半は著作権が現役で残る作品が多く、PD化はBerne条約により国・年代で異なる。Modernist Journals Project（Brown大）は1890-1922年の英米モダニズム雑誌をオープン公開、Modernist Versions Projectはジョイス等のテキスト比較版を提供する。James Joyce Online Notes・Kafka Project（San Diego State）は作家固有の学術ポータル。日本語訳の同時代受容は青空文庫（PD化された訳業）で部分的に追跡可能。

主要源: Modernist Journals Project / Modernist Versions Project / Project Gutenberg Australia（カナダPD準拠）/ HathiTrust / Kafka Project（要確認: 公式運営状況）/ JSTOR。

#### (7) ポストモダン・現代（lit_eu_postmodern）

戦後以降は著作権の関係でPD原典は限定的、二次文献ベースでの収集が中心となる。MLA International Bibliography・JSTOR・Project MUSE が主要学術DB、Electronic Literature Collection（ELO）はデジタル文学の一次源、Internet ArchiveはOpen Libraryによる読み取り提供（コントロール付き貸出）が補助的に機能する。

主要源: MLA International Bibliography / JSTOR / Project MUSE / Electronic Literature Collection（ELO Vol.1-3）/ Internet Archive Open Library / Wikipedia学術版（Wikidata連携）。

### 1.2 東アジア文学系譜

#### (8) 中国古典文学（lit_cn_classical）

CTEXT（Chinese Text Project, https://ctext.org/）は事実上の標準で、先秦から清末までの古典文献を原文＋英訳併記で公開、APIアクセス可能。維基文庫（Wikisource中文版）はPD版のテキストを校訂継続中、四庫全書電子版（迪志文化版）は機関契約だが網羅性は最大。Scripta Sinica（中央研究院、台湾）は史書・文集の検索コーパス、Hanchi.ihp.sinica.edu.twは台湾アカデミアシニカの漢籍電子文献。Kanripo（漢リポ）は校訂本付きのGitHubベース漢籍リポジトリ。

主要源: CTEXT（Chinese Text Project）/ 維基文庫（中文Wikisource）/ Scripta Sinica（漢籍電子文獻資料庫, 中央研究院）/ Kanripo（漢リポ）/ 四庫全書電子版（要機関契約）/ Database of Chinese Buddhist Texts CBETA（仏教文献補完）。

#### (9) 中国近現代文学（lit_cn_modern）

20世紀の中国文学は著作権制約が強く、CNKI（中国知網）が主要二次文献DBとなる（機関契約）。魯迅・茅盾等の主要作家の初期作品は中国大陸でPD化されており、維基文庫・読秀（中国の電子書籍プラットフォーム、要機関契約）で部分入手可能。MCLC Resource Center（Modern Chinese Literature and Culture, Ohio State）は学術ポータル、Chinese Literature Today誌（Oklahoma大）は英訳と論考の主要源。

主要源: CNKI（中国知網, 要契約）/ 維基文庫 / MCLC Resource Center（Ohio State）/ Chinese Literature Today / Paper Republic（中国現代文学英訳プロジェクト）/ JSTOR。

#### (10) 日本古典文学（lit_jp_classical）

国文学研究資料館（NIJL）の日本古典籍総合目録データベース・新日本古典籍総合データベースは画像・書誌の標準源で、3万点超の写本・版本がオープン公開。国立国会図書館デジタルコレクション（NDL）はPD版の和書をAPI提供、ジャパンナレッジは『日本古典文学全集』『新編日本古典文学全集』等の校訂版を機関契約で提供する。J-STAGEは日本国文学関連の論文オープンアクセス、青空文庫はPD化された古典・近代訳業を網羅する。

主要源: 国文学研究資料館 新日本古典籍総合データベース / NDL（国立国会図書館デジタルコレクション）/ J-STAGE / ジャパンナレッジ（要機関契約）/ 青空文庫 / 国際日本文化研究センター（日文研）データベース群。

#### (11) 日本近現代文学（lit_jp_modern）

明治期から戦前までの作品は青空文庫が事実上の標準（PD化済み）、戦後以降は著作権下のためジャパンナレッジ・CiNii Articles・J-STAGE が二次文献の主要源となる。日本近代文学館は専門資料館として書誌情報・原稿画像を提供。NDLデジタルコレクションは1968年以前の図書をログイン送信で広く利用可能。

主要源: 青空文庫 / NDLデジタルコレクション / CiNii Research（CiNii Articles + Books統合）/ J-STAGE / 日本近代文学館 / ジャパンナレッジ（要機関契約）。

### 1.3 南アジア・西アジア文学

#### (12) インド文学（lit_india）

サンスクリット古典は GRETIL（Göttingen Register of Electronic Texts in Indian Languages）が国際標準、SARIT（Search and Retrieval of Indic Texts）は批判校訂テキストのTEI準拠リポジトリ、Sanskrit Heritage Site（Gérard Huet, INRIA）は形態素解析と辞書機能を持つ。Digital Library of India・Internet ArchiveはPD版の近代インド諸言語文学（ヒンディー・ベンガル・タミル等）を提供、Murty Classical Library of India（Harvard）は古典の現代英訳を併載した近年の批判校訂事業。

主要源: GRETIL（Göttingen）/ SARIT / Sanskrit Heritage Site（INRIA）/ Digital Library of India / Internet Archive / Murty Classical Library of India（一次源は機関契約）。

#### (13) アラブ文学（lit_arabic）

Al-Maktaba al-Shamela（المكتبة الشاملة）は古典アラビア語文献の最大級コーパスで7,000以上のテキストを収録、無料配布。OpenITI（Open Islamicate Texts Initiative）はAl-Shamelaを基礎に学術的整備したコーパス、Bibliotheca Alexandrina の Memory of the Arab Worldはエジプト・近東のデジタルアーカイブ。Arabic Collections Online（NYU）は前近代から近代までのPDアラビア語書籍をオープン公開、Brill Online Reference（Encyclopaedia of Islam等）は二次文献の標準（機関契約）。

主要源: Al-Maktaba al-Shamela / OpenITI / Arabic Collections Online（NYU）/ Bibliotheca Alexandrina デジタルアーカイブ / Brill Encyclopaedia of Islam（要契約）/ AlKindi（Dominican Institute for Oriental Studies）。

#### (14) ペルシア・トルコ文学（lit_persian_turkish）

Ganjoor.net はペルシア古典詩の最大級アーカイブで、フェルドウスィー・ハーフェズ・ルーミー・サアディ等を網羅、無料公開。Roshan Cultural Heritage Institute やPersian Literature in Translationは英訳補完。トルコ語はTürkiye Diyanet Vakfı İslam Ansiklopedisi（オスマン古典の主要典拠）、Ottoman Text Archive Project、Istanbul Üniversitesi Nadir Eserler Kütüphanesi（写本デジタル化）が一次源。Encyclopaedia Iranica（Columbia大主導、IranicaOnline）は学術的二次文献の標準。

主要源: Ganjoor.net / Encyclopaedia Iranica（Columbia）/ İslam Ansiklopedisi（Diyanet Vakfı）/ Ottoman Text Archive Project（要確認: 運営状況）/ HathiTrust（オスマン古印刷本）/ Roshan Cultural Heritage Institute（要確認: 公開状況）。

### 1.4 グローバル・サウス文学

#### (15) アフリカ文学（lit_africa）

口承文学のため学術整備は領域横断で偏在する。African Storybook Project（南ア・Saide）はオープンライセンスで多言語の口承・現代文学を提供、ALUKA（JSTOR Global Plants/African Cultural Heritageプロジェクトの一部）はサブサハラ史資料、World Oral Literature Project（Cambridge）は口承文学の音声・転記アーカイブ。African Journals Online（AJOL）は学術論文オープンアクセス、Chinua Achebe・Wole Soyinka等の現代作家は機関契約のJSTOR・Project MUSEで補完される。

主要源: African Storybook Project / World Oral Literature Project（Cambridge）/ African Journals Online（AJOL）/ JSTOR / Project MUSE / UNESCO Memory of the World（口承文化分も一部含む）。

#### (16) ラテンアメリカ文学（lit_latin_america）

Biblioteca Virtual Miguel de Cervantes はスペイン語圏文学の最大級PDアーカイブで、ラテンアメリカ植民地期から20世紀前半をカバー。Latin American Network Information Center（LANIC, Texas大）は地域横断ポータル（要確認: 2010年代後半以降の更新状況）、Hemispheric Institute Digital Video Library（NYU）はパフォーマンス文化の一次源。Project Gutenbergのスペイン語・ポルトガル語版もボルヘス以前のPDを多数収録、JSTOR・MLA Bibliographyは二次文献補完。

主要源: Biblioteca Virtual Miguel de Cervantes / LANIC（Texas大、要確認）/ Hemispheric Institute Digital Video Library（NYU）/ Project Gutenberg西語・葡語 / JSTOR / Memoria Chilena（チリ国立図書館デジタルアーカイブ）。

#### (17) 東南アジア・韓国文学（lit_se_asia_korea）

韓国は KRpia（韓国学中央研究院運営、要機関契約）と Korean Literature Now（LTI Korea運営、英訳と紹介）が学術源、National Library of Korea デジタルライブラリーはPD版書籍を公開。ベトナムは Vietnamese Nôm Preservation Foundation（チューノム・古典漢文写本デジタル化）、インドネシア・マレーはSEAlangプロジェクトが標準的言語コーパス、Library of Congress の Southeast Asia Collection はオンライン書誌の主要源。

主要源: National Library of Korea デジタルライブラリー / Korean Literature Now（LTI Korea）/ Vietnamese Nôm Preservation Foundation / SEAlang Library / KRpia（要契約）/ DBpia（韓国学術DB、要契約）。

### 1.5 周縁・横断的領域

#### (18) ロシア・スラヴ文学（lit_russia_slavic）

Russian Virtual Library（rvb.ru）とFundamental Electronic Library of Russian Literature（feb-web.ru）はロシア古典・19世紀作品の批判校訂版を公開する標準源。Project Gutenberg と Wikisource ロシア語版は補完。RUCONT（Russian Online Library, 要機関契約）と eLIBRARY.RU は二次文献。スラヴ諸語はTITUS（Frankfurt大、Indo-European/Caucasian Languages Texts）が比較文献学レベルで参照される。

主要源: Russian Virtual Library（rvb.ru）/ Fundamental Electronic Library of Russian Literature（FEB, feb-web.ru）/ Project Gutenberg / Wikisource ロシア語版 / TITUS（Frankfurt大）/ eLIBRARY.RU（要契約）。

#### (19) 先住民・口承文学（lit_indigenous_oral）

文字化された一次資料が限定的なため、フィールド録音アーカイブと先住民コミュニティ主導のデジタル化事業が中核となる。World Oral Literature Project（Cambridge）、Endangered Languages Archive（ELAR, SOAS）、Pacific and Regional Archive for Digital Sources in Endangered Cultures（PARADISEC, Sydney大）が国際標準。アイヌは北海道立アイヌ民族文化研究センター・国立アイヌ民族博物館がデジタル化進行、ネイティブアメリカンはSmithsonian Institution の National Anthropological Archives と American Indian Studies Research Institute（Indiana大）が主要源。

主要源: World Oral Literature Project / Endangered Languages Archive（ELAR, SOAS）/ PARADISEC / 国立アイヌ民族博物館（ウポポイ）デジタルアーカイブ / Smithsonian National Anthropological Archives / UNESCO Intangible Cultural Heritage（無形文化遺産DB）。

#### (20) ディアスポラ・移民文学（lit_diaspora）

地域横断のため固有DBは少ないが、領域別アーカイブの組合せで対処する。Postcolonial Web（旧VictorianWeb系列、Brown大）は理論と作家ポータル（要確認: 現状の更新状況）、Asian American Writers' Workshop の Open Country Mag、Caribbean Literature Online（要確認）、Goethe-Institutの世界文学プログラム関連資料、JSTOR・Project MUSE・MLA Bibliography が研究側の標準。原典は各作家の出身地・滞在地のPDアーカイブと現代作家の出版社サイトを使い分ける。

主要源: JSTOR / Project MUSE / MLA International Bibliography / Asian American Writers' Workshop / Postcolonial Studies @ Emory / The Margins（AAWW誌）。

#### (21) 児童・大衆・ジャンル文学（lit_genre）

Internet Speculative Fiction Database（ISFDB）はSF・ファンタジーの書誌標準、Pulp Magazines Project（Bowling Green State）と Galactic Central はPD化されたパルプ雑誌の網羅源。International Children's Digital Library（IBBY系列、ICDL）は児童文学多言語デジタル化、Baldwin Library of Historical Children's Literature（Florida大）は19-20世紀児童書のPDコレクション、Comic Book Plus はPDコミックスの保存サイト。

主要源: ISFDB（Internet Speculative Fiction Database）/ Pulp Magazines Project / International Children's Digital Library（ICDL, 要確認: 現状運営）/ Baldwin Library of Historical Children's Literature（Florida大）/ Comic Book Plus / Project Gutenberg。

### 1.6 理論・横断概念

#### (22) 文学理論・批評（lit_theory）

二次文献領域のため、JSTOR・Project MUSE・MLA International Bibliographyの三大学術DBが基礎。Stanford Encyclopedia of Philosophyは理論家伝記・概念解説の信頼源（哲学DBと共有）、PhilPapers は理論論文の書誌コーパス、Critical Inquiry誌・New Literary History誌・Diacritics誌のオンラインアーカイブが個別アクセス源。Routledge Encyclopedia of Philosophy・Cambridge Companions（要契約）も主要参照。

主要源: JSTOR / Project MUSE / MLA International Bibliography / Stanford Encyclopedia of Philosophy / PhilPapers / Cambridge Companions Online（要契約）。

#### (23) 比較文学・世界文学・翻訳論（lit_world_translation）

比較文学はACLA（American Comparative Literature Association）刊行物、世界文学はDavid Damrosch主導の Institute for World Literature 関連資料、翻訳論はBenjamins Translation Studies Bibliography（BTSB, 要契約）が標準書誌。UNESCO Index Translationum は世界の翻訳書誌DB（運営状況要確認）、Routledge Translation Studies（要契約）も基幹。

主要源: JSTOR / Project MUSE / Benjamins Translation Studies Bibliography（BTSB, 要契約）/ UNESCO Index Translationum（要確認）/ MLA International Bibliography / Institute for World Literature（Harvard）。

#### (24) デジタル人文学・AI時代の文学（lit_digital_ai）

Electronic Literature Organization（ELO）の Electronic Literature Collection Vol.1-3 は電子文学の一次源、Electronic Literature Knowledge Base はメタデータDB。ADHO（Alliance of Digital Humanities Organizations）と DHCommons はDH全般のポータル、Stanford Literary Lab・Modern Language Association Commons は計算文学批評の主要拠点。生成AI関連は arXiv（cs.CL）と ACL Anthology が技術論文側、JSTOR・Project MUSEが文学側からの応答論考を提供する。

主要源: Electronic Literature Collection（ELO Vol.1-3）/ Electronic Literature Knowledge Base / Stanford Literary Lab / ACL Anthology / arXiv（cs.CL）/ MLA Commons。

---

## 2. 収集目標マトリクス（concepts/authors/works/movements の4軸）

各サブフィールドについて、概念・作家・作品・運動・時代区分の目標数を提示する。`works`テーブル独立は西村承認済み・スキーマ実装済みのため、本マトリクスは作品単位の収集計画を含む。`works`はサブフィールドあたりの主要作品（importance_score 4-5に相当する正典級）と中間層（重要だが非正典）の合計目標であり、全体5,000件目標から各領域の知的生産密度を勘案して配分した。

| # | サブフィールド | concepts | authors | works | movements | 主要period分割 |
|---|---|---:|---:|---:|---:|---|
| 1 | 古典古代文学 | 500 | 100 | 220 | 25 | 古代ギリシャ（前8c〜前4c）/ ヘレニズム / ローマ（共和政・帝政）/ 後期古代 |
| 2 | 中世文学 | 400 | 80 | 200 | 25 | 初期中世（5-10c）/ 盛期中世（11-13c）/ 後期中世（14-15c） |
| 3 | ルネサンス・近世文学 | 500 | 100 | 250 | 30 | 伊ルネサンス / 北方ルネサンス / バロック（17c）/ 古典主義 |
| 4 | 啓蒙・ロマン主義 | 500 | 120 | 280 | 30 | 啓蒙（18c前〜中）/ 前ロマン / ロマン主義（独・英・仏）/ ゴシック |
| 5 | リアリズム・自然主義・象徴主義 | 600 | 130 | 320 | 30 | リアリズム（1830-70）/ 自然主義（1870-1900）/ 象徴主義（1880-1910） |
| 6 | モダニズム | 500 | 110 | 250 | 25 | 前期モダニズム（1900-1918）/ ハイモダニズム（1918-1939）/ 後期 |
| 7 | ポストモダン・現代 | 500 | 130 | 230 | 25 | 戦後（1945-1970）/ ポストモダン（1970-2000）/ 21世紀 |
| 8 | 中国古典文学 | 600 | 150 | 280 | 25 | 先秦 / 漢魏六朝 / 唐 / 宋 / 元明 / 清 |
| 9 | 中国近現代文学 | 400 | 100 | 180 | 20 | 五四（1917-）/ 抗日 / 建国後 / 改革開放後 |
| 10 | 日本古典文学 | 500 | 120 | 250 | 25 | 上代 / 中古 / 中世 / 近世 |
| 11 | 日本近現代文学 | 500 | 130 | 250 | 25 | 明治 / 大正 / 昭和戦前 / 戦後 / 現代 |
| 12 | インド文学 | 500 | 120 | 230 | 25 | ヴェーダ / 古典サンスクリット / バクティ運動 / 近代諸言語 / 独立後 |
| 13 | アラブ文学 | 400 | 90 | 180 | 20 | ジャーヒリーヤ / アッバース朝古典 / アンダルス / ナフダ（19c）/ 現代 |
| 14 | ペルシア・トルコ文学 | 300 | 70 | 150 | 15 | サーマーン朝〜サファヴィー朝古典詩 / オスマン古典 / 近代 |
| 15 | アフリカ文学 | 400 | 90 | 170 | 25 | 口承伝統 / 植民地期 / 独立期 / ポストコロニアル / 現代 |
| 16 | ラテンアメリカ文学 | 500 | 110 | 220 | 25 | 植民地期 / 独立後ロマン主義 / モデルニスモ / ブーム期 / ポスト・ブーム |
| 17 | 東南アジア・韓国文学 | 300 | 80 | 150 | 20 | 古典（漢字文化圏）/ 植民地期 / 戦後 / 現代 |
| 18 | ロシア・スラヴ文学 | 400 | 100 | 200 | 20 | 古ルーシ / 18c古典主義 / 19c黄金時代 / 銀の時代 / ソ連期 / ソ連後 |
| 19 | 先住民・口承文学 | 400 | 80 | 150 | 30 | 文化圏別（北米・豪・アイヌ・サーミ等）の地域時代区分 |
| 20 | ディアスポラ・移民文学 | 400 | 100 | 170 | 20 | 戦前移民 / ポストコロニアル / 21世紀グローバル |
| 21 | 児童・大衆・ジャンル文学 | 300 | 80 | 200 | 20 | 19c起源 / 20c黄金期 / 戦後ジャンル成熟 / 現代 |
| 22 | 文学理論・批評 | 700 | 200 | 100 | 30 | 古典批評 / 19c批評 / 20c前半（形式主義・新批評）/ 構造主義以後 |
| 23 | 比較文学・世界文学・翻訳論 | 500 | 150 | 80 | 20 | 19c比較文学起源 / 戦後比較文学 / 世界文学論（2000-） |
| 24 | デジタル人文学・AI時代 | 400 | 100 | 80 | 15 | 電子文学（1990-）/ デジタル人文学（2000-）/ 生成AI期（2020-） |
| **合計** | | **11,000** | **2,560** | **4,810** | **570** | |

注釈: authors合計2,560はPROJECT_PLANの3,000目標に対して内部配分の現実値、worksは4,810で5,000目標枠内、movementsは570で500目標を若干超過するが正典化途上の運動を含めるため許容範囲とする。Phase 1で各サブフィールドからの再申告を受けて±5%調整可能とする。

各時代区分（period）は地域別に独立して定義されるため、同一年代でも地域が異なれば別レコードとなる。例えば1900年は西欧では「世紀末・モダニズム黎明」だが、中国では「清末・新文化運動前夜」、日本では「明治後期」と区分される。これにより西欧時代区分の他地域への押し付けを構造的に回避する。

---

## 3. 第四変容タグ9軸 × サブフィールド優先度マトリクス

第四変容期（AI社会）における再考軸9つを、各サブフィールドへの関連強度（高=H/中=M/低=L）で評価した。値が「H」の場合、当該サブフィールドの収集ではこの軸の概念をfourth_transform_tags の必須付与対象として扱う。マトリクスは Phase 2 収集時の優先順位付けに直接反映される。

| サブフィールド \ 軸 | 作者性 | 創造性 | 物語 | 主体 | 正典 | 受容 | 翻訳 | 真正性 | 言語 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 古典古代文学 | M | M | H | M | H | M | H | M | H |
| 中世文学 | H | M | H | L | H | M | H | M | H |
| ルネサンス・近世文学 | H | H | M | H | H | M | H | H | M |
| 啓蒙・ロマン主義 | H | H | H | H | M | M | M | H | M |
| リアリズム・自然主義・象徴主義 | M | H | H | H | M | H | M | H | H |
| モダニズム | H | H | H | H | M | H | H | H | H |
| ポストモダン・現代 | H | H | H | H | H | H | H | H | M |
| 中国古典文学 | M | L | M | L | H | M | H | M | H |
| 中国近現代文学 | M | M | M | H | H | H | H | M | H |
| 日本古典文学 | M | M | H | M | H | M | M | M | H |
| 日本近現代文学 | H | M | H | H | M | M | M | H | M |
| インド文学 | L | M | H | M | H | M | H | M | H |
| アラブ文学 | M | M | H | M | H | M | H | M | H |
| ペルシア・トルコ文学 | M | M | H | M | H | M | H | M | M |
| アフリカ文学 | M | M | H | H | H | H | H | H | H |
| ラテンアメリカ文学 | M | M | H | H | H | M | H | H | H |
| 東南アジア・韓国文学 | M | M | M | H | H | M | H | M | H |
| ロシア・スラヴ文学 | M | M | H | H | M | M | M | H | M |
| 先住民・口承文学 | H | H | H | H | H | H | H | H | H |
| ディアスポラ・移民文学 | M | M | H | H | H | H | H | H | H |
| 児童・大衆・ジャンル文学 | H | H | H | M | M | H | M | M | M |
| 文学理論・批評 | H | H | H | H | H | H | H | H | H |
| 比較文学・世界文学・翻訳論 | M | M | M | M | H | H | H | H | H |
| デジタル人文学・AI時代 | H | H | H | H | H | H | H | H | H |

ハイライト: 「先住民・口承文学」「文学理論・批評」「デジタル人文学・AI時代」の3領域は全9軸でHの最重要再考領域となる。これらは生成AIによる「作者性」「真正性」「言語の所有」の問題が最も鋭く立ち上がる接続面である。逆に古典古代と中国古典は伝統側に据え置かれる軸（創造性のロマン主義的概念は近代以降の構築であり古典側はimitatio中心）が多い。

---

## 4. 想定される収集難所と対応策

### 4.1 一次資料が不足する領域

**口承文学・先住民文学**: 文字化された一次資料が限定的なため、World Oral Literature Project・ELAR・PARADISECといったフィールド録音アーカイブを一次源として位置づける。テキスト化が部分的でも、二次的な民俗学的記録（19-20世紀の収集者による転記・翻訳）を「中継資料」として明示的にprimary_source_typeフィールドに記録し、原資料との隔たりを可視化する。アイヌは知里幸恵『アイヌ神謡集』、ネイティブアメリカンはBoas学派の記録、アボリジニはStrehlow Research Centre等を主要中継源とする。

**東南アジア・韓国近世以前**: 韓国は漢文文献が中心でCTEXTで部分的にカバー可能、ベトナムはチューノム文献が Vietnamese Nôm Preservation Foundation でデジタル化進行中。マレー・インドネシア・タイの古典は欧州オリエンタリスト記述に依存する場合が多く、ヨーロッパ図書館（KITLV、SOAS等）のコレクションを並用する。

**著作権下の20-21世紀作品**: PD原典が利用できない場合、二次文献ベース（学術DB論文・批判校訂版の書誌情報）で概念抽出を行い、primary_source_url を空欄にせずsecondary_source_url として明記する仕様にする。Phase 1のスキーマ拡張で `source_tier` カラム（`primary`/`secondary`/`tertiary`）の追加を提案する。

### 4.2 翻訳バイアスへの対応

LIT-DB は原語表記（name_original / original_script）を必須項目とすることで、翻訳経由でのみ知られた概念（西欧経由のサンスクリット語rasa→「美的情趣」等）について原語への遡及を強制する。具体運用として、(1) 翻訳語のみで定義される概念は importance_score を1段下げる、(2) 同一概念の異言語表記をrelationsテーブルで `equivalent_in_translation` リンクし学術的整合性を保つ、(3) 西欧理論の概念を非西欧領域へ適用する場合は cross_domain テーブルにて明示的に「borrowed_from」として記録、の3つの規律を導入する。

### 4.3 西欧中心主義の再生産を避ける配分検証

PROJECT_PLAN にて西欧31.8%（3,500/11,000）、非西欧68.2%（7,500/11,000）の配分が承認されており、本Phase 0 マトリクスもこの比率を維持する。検証メカニズムは以下:

1. **相互参照の双方向性**: 西欧→非西欧の影響リンクと、非西欧→西欧の影響リンクの数を比較し、後者が前者の50%以上となることを目標とする（cross_domain テーブルでの定量検証）。
2. **正典定義の地域依存性**: `canonical_in_region` カラムの追加をPhase 1で提案。「ある地域では正典、他地域では未知」を構造化。
3. **理論領域の脱中心化**: 文学理論700概念のうち、非西欧理論（中国詩話、インド rasa 理論、アラブ balagha 等）を最低200（28.6%）配置。これは Phase 1 で個別カウントを実施する。

### 4.4 ハルシネーション防止

哲学DBで確立した「PD原典からの一次取得」原則を踏襲し、以下の3層チェックを Phase 2-3 で実行する:

- **Tier 1（PD原典直接取得）**: name_original・代表引用・成立年が原典から直接抽出可能な概念。importance_score 4-5の概念は原則ここに属するべき。
- **Tier 2（批判校訂版経由）**: PD原典がない、または部分的な場合、確立された批判校訂版（Loeb・Murty・新編日本古典文学全集等）を通じて取得。
- **Tier 3（二次文献経由）**: 上記2層が利用不可の場合、複数の独立した学術二次文献（最低3件）の合致をもって採録。Codex 横断検証2名がレビュー必須。

各 concept レコードに `source_tier` を必須記録することで、後段の検証・整理（Phase 3）でTier 3 のみの概念を抽出し再検査するワークフローが組める。

---

## 5. Phase 1（調査設計）への引き継ぎ事項

### 5.1 Codex 20名の役割分担確定案

PROJECT_PLAN の20名配置を踏まえつつ、本Phase 0で明らかになった一次資料源の分布に応じて、各員の主要利用DB群を確定する。

| # | Codex | 担当領域 | 主要利用DB | 予定concepts数 |
|---|---|---|---|---:|
| C01 | 古典古代担当 | 古典古代文学 | Perseus / TLG / Loeb / Sefaria | 500 |
| C02 | 西欧中世担当 | 中世文学 | MGH / TEAMS / Bibliotheca Augustana / Gallica | 400 |
| C03 | 西欧近世担当 | ルネサンス・啓蒙・ロマン | Folger / EEBO / Gutenberg / DTA / ARTFL | 1,000 |
| C04 | 西欧近現代担当 | リアリズム・モダニズム・ポストモダン | Modernist Journals / JSTOR / Project MUSE | 1,600 |
| C05 | 中国古典担当 | 中国古典文学 | CTEXT / 維基文庫 / Scripta Sinica / Kanripo | 600 |
| C06 | 中国近現代担当 | 中国近現代文学 | CNKI / MCLC / Paper Republic / 維基文庫 | 400 |
| C07 | 日本古典担当 | 日本古典文学 | NIJL / NDL / J-STAGE / 青空文庫 | 500 |
| C08 | 日本近現代担当 | 日本近現代文学 | 青空文庫 / NDL / CiNii / J-STAGE | 500 |
| C09 | インド担当 | インド文学 | GRETIL / SARIT / Sanskrit Heritage / Murty | 500 |
| C10 | アラブ・ペルシア担当 | アラブ・ペルシア・トルコ | Al-Shamela / OpenITI / Ganjoor / Iranica | 700 |
| C11 | アフリカ担当 | アフリカ文学 | African Storybook / WOLP / AJOL / JSTOR | 400 |
| C12 | ラテンアメリカ担当 | ラテンアメリカ文学 | Cervantes Virtual / Memoria Chilena / JSTOR | 500 |
| C13 | 東南アジア・韓国担当 | 東南アジア・韓国文学 | NLK / LTI Korea / Nôm Foundation / SEAlang | 300 |
| C14 | ロシア・スラヴ担当 | ロシア・スラヴ文学 | rvb.ru / FEB / Gutenberg / TITUS | 400 |
| C15 | 先住民・口承担当 | 先住民・口承文学 | WOLP / ELAR / PARADISEC / Smithsonian NAA | 400 |
| C16 | ディアスポラ担当 | ディアスポラ・移民文学 | JSTOR / Project MUSE / AAWW / 各地域DB | 400 |
| C17 | ジャンル担当 | 児童・大衆・ジャンル文学 | ISFDB / Pulp Magazines / ICDL / Baldwin | 300 |
| C18 | 理論・批評担当（主） | 文学理論・批評 | JSTOR / SEP / PhilPapers / Project MUSE | 700 |
| C19 | 比較文学・翻訳論担当 | 比較文学・世界文学・翻訳論 + DH/AI | BTSB / Index Translationum / ELO / arXiv | 900 |
| C20 | 横断検証担当 | 全領域品質保証・ハルシネーション検出・cross_domain | 全DB横断 | 検証専従 |

注意: C03/C04 は西欧近世〜現代で1,000〜1,600 concepts と負荷が大きいため、Phase 2 中盤で必要に応じてサブ分割（C03a/C03b等）する余地を残す。C19 はDH/AI領域もカバーするためdigital_aiの400 conceptsを兼任。C20 は専属検証で、収集自体は他19名が担う。

### 5.2 5参照パターンの定義

哲学DB・経営学DB構築で確立された5参照パターンを文学領域に適応させる。

**パターン1: 正典型一次資料追跡（Canonical Primary Pursuit）**
- 適用領域: 古典古代・中国古典・日本古典・インド古典・アラブ古典
- 手順: 既知の正典作品リスト（学術通史で言及される代表作）を起点に、PD原典/批判校訂版から概念・登場人物・主題・修辞・後代影響を抽出
- 主要利用: Perseus / CTEXT / NIJL / GRETIL / Al-Shamela
- 規模目安: 1サブフィールドあたり250-400 concepts、authors 70-150、works 150-280

**パターン2: 文学運動・流派起点（Movement-Driven Aggregation）**
- 適用領域: ルネサンス〜現代の西欧、中国近現代、日本近現代、ラテンアメリカ・ブーム期、モダニズム、ポストモダン、各種主義
- 手順: 文学運動（ロマン主義、自然主義、シュルレアリスム、ブーム期等）を起点とし、その所属作家・代表作・宣言・批判者・継承者をネットワーク的に展開
- 主要利用: 各時代の二次文献通史（Routledge Companion / Cambridge Companion等）+ JSTOR
- 規模目安: 1サブフィールドあたり400-600 concepts

**パターン3: 理論家・批評家系譜（Theorist-Genealogy Pattern）**
- 適用領域: 文学理論・批評、比較文学・翻訳論、デジタル人文学
- 手順: 主要理論家（Bakhtin → Kristeva → Genette 等）の系譜を構築し、各理論家の主要概念・批判対象・継承者をgeneal_links に登録。哲学DBとのcross_domain強化
- 主要利用: SEP / PhilPapers / JSTOR / Cambridge Companions
- 規模目安: 1サブフィールドあたり500-700 concepts、theory単独で200近い理論家

**パターン4: 地域・言語クラスター展開（Regional Cluster Expansion）**
- 適用領域: アフリカ・ラテンアメリカ・東南アジア・韓国・ディアスポラ・先住民
- 手順: 言語または地域クラスター（スワヒリ語圏、アンデス先住民、韓国近代等）ごとに、(1) その地域の代表的アンソロジー、(2) 国家文学史叙述、(3) 領域研究学会誌の3層から概念・作家を抽出
- 主要利用: 各地域学会誌 + UNESCO ICH + 各国国立図書館DB
- 規模目安: 1サブフィールドあたり300-500 concepts

**パターン5: 第四変容軸クロスカット収集（Fourth-Transformation Cross-Cut）**
- 適用領域: 全24サブフィールドの横断付与
- 手順: 9軸（作者性〜言語）ごとに「AI時代に再考対象となる代表概念」を全領域から抽出し、fourth_transform_tagsに記録。生成AIによる作者性解体・正典再編・翻訳の自動化等の現象との対応関係を rationale に記述
- 主要利用: arXiv（cs.CL）/ ACL Anthology / Critical AI誌 / electronicbookreview
- 規模目安: 9軸 × 平均30概念 = 270の重点タグ。全概念にいずれかの軸タグが付くことを目標

### 5.3 Phase 1 が必要とする追加判断事項

Phase 1 起動前に、以下を西村と確認する:

- `source_tier` カラム追加（primary/secondary/tertiary）— ハルシネーション防止のため Phase 1 で schema.sql に追加することを提案
- `canonical_in_region` カラム追加 — 地域別正典定義のため
- C03/C04 の負荷分割を Phase 2 中盤に判断する基準（例: 進捗60%時点でレート割れの場合分割）
- 第四変容タグ9軸の定義文（各axisの操作的定義）を Phase 1 で確定

---

## 6. Phase 0 完了確認

- 24サブフィールドごとの一次資料源マッピング完了（実在DB基準で5以上を列挙、不確実なものは「要確認」明示）
- 収集目標マトリクス4軸（concepts/authors/works/movements）完了、合計11,000 concepts に整合
- 第四変容タグ9軸 × 24サブフィールド優先度マトリクス完了
- 想定難所と対応策（4カテゴリ）整理完了
- Phase 1 引き継ぎ事項（Codex 20名割当・5参照パターン・追加判断項目）完了

本レポートをもって Phase 0 を完了とし、西村レビュー後に academic-db-survey による Phase 1（調査設計、5日）を起動する。
