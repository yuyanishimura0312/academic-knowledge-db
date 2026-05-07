# PHASE2 C23 Report — LIT-Africa-Early

## 概要

Wave 5 の C23 として、アフリカ文学の口承伝統と植民地期に関する **40 概念** を `lit.sqlite` の `subfield_id=15`（`lit_africa`、地域 `グローバルサウス`）に投入した。AJOL・UNESCO ICH・Présence Africaine・African Storybook・Wikipedia 等の公開アーカイブを一次／二次ソースとして用い、ハルシネーションを避けつつ、口承伝統からネグリチュード・脱植民地化批評までを網羅した。

実行スクリプト: `wave5_c23_africa_early.py`

## 投入結果

| 項目 | 件数 |
|---|---|
| concepts (subfield_id=15) | **40** |
| fourth_transform_tags | 21 |
| cross_domain | 21 |
| periods 新規追加 | 4（アフリカ口承伝統期 / 植民地期 / ネグリチュード・反植民地期 / 独立後初期） |

エラー・スキップ・失敗は 0 件。

## カテゴリ別投入

- **A. 口承伝統 (8)** — グリオ、ムヴェット、イファ卜占詩、賛歌詩、民話、アナンセ物語、イジボンゴ、オリキ
- **B. 主要主題・世界観 (8)** — ウブントゥ、ネグリチュード、アフリカン・パーソナリティ、民族哲学、祖先記憶、トーテミズム、共同体的自己と個人的自己、口承＝書記の分割
- **C. 植民地期文学 (8)** — ミッションスクール文学、仏／英／葡語圏初期小説、オニチャ市場文学、南ア初期黒人文学、ハウサ語カノ印刷、スワヒリ語初期近代
- **D. ネグリチュード・反植民地運動 (8)** — Présence Africaine、ネグリチュード対タイガリチュード、反植民地詩、セゼール『帰郷ノート』、サンゴールのリズム、David Diop、Birago Diop『Contes』、Camara Laye『L'Enfant noir』
- **E. 主要批評概念 (8)** — 口承ジャンル分類、ピジン化、言語選択論争、精神の脱植民地化、アフリカ文学美学、ujamaa文学、対話的祖先形式、oraliture

## 品質指標

- **canonical_in_region**: core 10 / major 24 / minor 6
- **source_tier**: primary 7 / secondary 33（tertiary なし）
- **第四変容タグ分布（軸別）**: 言語 8、受容 4、主体 3、物語 2、翻訳 2、作者性 1、創造性 1（合計 21、12 概念に最低 1 軸）
- **cross_domain 分布**: AN 9、PHIL 6、PT 4、Myth-Narratives 2（合計 21）

人類学（AN）接点が深いという指示通り、ウブントゥ・グリオ・共同体的自己・祖先記憶・親族／トーテム・口承＝書記の分割等が AN にリンクしている。哲学（PHIL）には ubuntu・ネグリチュード・ethnophilosophy・decolonizing the mind 等が、詩学（PT）には grio／praise poetry／oríkì／ジャンル理論が接続。

## 第四変容タグ（指示12件以上を確保）

指示に挙げられた優先タグはすべて投入済み：

- griot → 作者性 + 物語
- ネグリチュード → 主体 + 言語
- decolonizing the mind → 言語 + 受容
- 共同体的自己と個人的自己 → 主体
- 口承＝書記の分割 → 言語 + 翻訳

加えてイファ卜占詩、ムヴェット、サンゴールのリズム、ピジン化、言語選択論争、oraliture 等にも軸を付与した。

## ソース運用

- **primary**: UNESCO ICH（イファ卜占）、Présence Africaine（ネグリチュード関連）、AIATSIS／African Storybook 等の機関アーカイブ、Birago Diop（Présence版）など
- **secondary**: Wikipedia、AJOL 学術誌（Research in African Literatures、SA Journal of Philosophy 等）

地域言語名は `name_original` にローマ字で保存し、`original_script='roman'` で統一（指示準拠）。

## 留意点

- アフリカ独立直後の `独立後初期 (1960-1980)` を期間として新設し、批評概念群と ujamaa 文学を時期付けした。
- ヨルバ語（イファ・oríkì）、マンデ語（griot/jeli）、バントゥ語（ubuntu/kamuy 系ではなくイジボンゴ）、ハウサ語（カノ）、スワヒリ語（ujamaa）の語彙を `name_original` に併記。
- ピジン化と言語選択論争を独立概念として分離し、母語優位論争と書記言語選択論争の両軸を確保。

## 投入数

**40 / 40 件投入完了**。
