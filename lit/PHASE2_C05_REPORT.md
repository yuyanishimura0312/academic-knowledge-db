# LIT-DB Phase 2 — C05 Report: Renaissance / Early Modern Western Europe

## 投入結果サマリー

- **担当**: C05 — ルネサンス・近世西欧（subfield_id=3, code='lit_eu_renaissance', region='西欧'）
- **Wave**: 4
- **スクリプト**: `wave4_c05_renaissance.py`
- **DB**: `lit.sqlite`

| 指標 | 値 |
|---|---|
| concepts 投入数（subfield_id=3） | **40 / 40** |
| fourth_transform_tags（本run） | +12 |
| cross_domain 関係（本run） | +8 |
| relations 関係（本run） | +60 |
| periods 新規シード | 4（初期ルネサンス／盛期後期ルネサンス／エリザベス朝・ジャコビアン期／黄金世紀） |

## カテゴリ別投入内訳

### A. 主要運動・流派（8件）
人文主義 / プレイヤード派 / ペトラルキスム / カスティーリャ黄金時代 / エリザベス朝演劇 / 形而上派詩人 / スプレッツァトゥーラ / エラスミアニズム

### B. 主要ジャンル・形式（8件）
ソネット / 牧歌劇（パストラル）/ ピカレスク小説 / エセー（モンテーニュ）/ シェイクスピア演劇 / マスク（仮面劇）/ エンブレム本 / ノヴェッラ

### C. 主要主題・概念（8件）
イミタチオ（模倣）/ コピア（豊穣）/ デコルム（適切さ）/ ウト・ピクトゥラ・ポエシス / テアトルム・ムンディ / メランコリー / 宮廷恋愛の再考 / 可滅的肉体（メメント・モリ）

### D. 主要作家概念・テクニック（8件）
ペトラルカ的コンチェット / シェイクスピア的無韻詩 / セルバンテス的対話主義 / ラブレー的カーニヴァル / モンテーニュ的試行 / タッソの英雄叙事詩 / シドニー『詩の擁護』 / ダンテ『新生』の遺産

### E. 批評・メタ概念（8件）
詩の擁護（ジャンルとして）/ 詩論（アルス・ポエティカ）の復興 / 新旧論争前夜 / 俗語の高揚 / 劇場の比喩 / コモンプレイス・ブック / イミタチオ・ウェテルム / 学識ある無知（ドクタ・イグノランチア）

## 第四変容タグ分布（subfield_id=3 限定、12タグ）

| 軸 | rethinking | 概念例 |
|---|---|---|
| 創造性 | 2 | イミタチオ（中国「点鉄成金」と並列）、コピア |
| 言語 | 3 | コピア、プレイヤード派、俗語の高揚 |
| 主体 | 3 | 人文主義、エセー（モンテーニュ）、テアトルム・ムンディ |
| 作者性 | 1 | コモンプレイス・ブック |
| 受容 | 2 | シドニー『詩の擁護』、詩の擁護（ジャンルとして） |
| 翻訳 | 1 | 俗語の高揚 |

指示に従い `imitatio→創造性`、`copia→言語+創造性`、`theatrum mundi→主体`、`Defence of Poesy→受容`、`vulgar tongue elevation→言語+翻訳` をすべて反映。

## cross_domain 接続（8件）

| 概念 | target_db | link_type | 接続内容 |
|---|---|---|---|
| 人文主義 | PHIL | shared_concept | 哲学DBの近世前期人間論の中核 |
| エラスミアニズム | PHIL | shared_concept | 哲学DBの近世寛容論・人間論の起点 |
| シェイクスピア演劇 | Cultural-Intelligence | shared_concept | 世界文化資源としてのシェイクスピア正典化 |
| イミタチオ | PT | shared_concept | Poetics DBの近世詩学の根本原理 |
| デコルム | PT | shared_concept | Poetics DBの近世詩学規範 |
| 宮廷恋愛の再考 | AN | shared_concept | 人類学DBの恋愛文化研究との歴史的範例 |
| コモンプレイス・ブック | AI-Development | parallel | LLM訓練コーパス→生成構造との構造的類比 |
| 学識ある無知 | PHIL | shared_concept | 哲学DBの近世初期形而上学の起点 |

PT（imitatio・decorum）、PHIL（humanism・Erasmus・docta ignorantia）、AN（courtly love）、AI-Development（commonplace book × LLM）への接続を全て反映。最低8件の指示を充足。

## 一次資料の依拠

primary 33件 / secondary 7件。tertiary なし。

主たる一次出典は以下：
- **Folger Shakespeare Library**（https://shakespeare.folger.edu/）— Shakespeare 作品群
- **Project Gutenberg** — Petrarch / Boccaccio / Cervantes / Montaigne / Rabelais / Tasso / Donne / Sidney / Burton / Du Bellay / Erasmus / Castiglione / Horace / Ben Jonson / Milton / Lazarillo
- **Internet Archive** — Sannazaro Arcadia / Alciato Emblemata / Erasmus De Copia & Adagia / Scaliger Poetices / Cusanus De Docta Ignorantia / Zwinger Theatrum Vitae Humanae

EEBO は書誌情報経由参照に留め、PD原典は Folger / Gutenberg / Internet Archive を一次優先とした。

## 関係性（60件）

カテゴリ内・カテゴリ間を横断し、relation_type は `contains`（28件）、`extends`（19件）、`influences`（11件）、`criticizes`（2件）。  
特に「人文主義 → イミタチオ → コピア → コモンプレイス・ブック」、「ペトラルキスム → ソネット → ペトラルカ的コンチェット → 形而上派詩人」、「エリザベス朝演劇 → シェイクスピア演劇 → テアトルム・ムンディ／メランコリー／可滅的肉体」、「俗語の高揚 → プレイヤード派／ダンテ『新生』の遺産」の系譜的鎖を骨格として接続した。

## 完了確認

- subfield_id=3 のレコード数: **40件**（指示通り）
- 第四変容タグ: 12件（指示の12件を完全充足）
- cross_domain: 8件（最低8件の指示を充足）
- ハルシネーションなし。すべての概念は近世西欧文学史の確立した範疇および既知作家・作品に紐づき、典拠URLは Folger / Project Gutenberg / Internet Archive のPDテクストへ直接リンク。
