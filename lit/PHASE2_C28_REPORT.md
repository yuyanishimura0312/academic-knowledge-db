# PHASE 2 — C28 LIT-Russia-19c 報告書

## 投入概要

LIT-DB Phase 2 Wave 4 の Codex C28 として、ロシア・スラヴ19世紀黄金時代に関する学術概念40件を `lit.sqlite` の `concepts` テーブルに subfield_id=18 (`lit_russia_slavic`)、region='周縁横断' で投入した。スクリプトは `wave4_c28_russia_19c.py` で、パイロット `pilot_c01_greek.py` および Wave 3 `wave3_c10_modernism.py` の構造を踏襲している。

## 投入内訳

| 区分 | 件数 |
|---|---|
| concepts (この実行) | 40 |
| fourth_transform_tags 追加 | 11 |
| cross_domain 追加 | 16 |
| 総 concepts (DB全体) | 481 |

カテゴリ別8件×5＝40件のバランスを保持。各概念は name_ja / name_en / name_original (キリル文字) / definition (150-250字相当) / primary_source_url / source_tier / canonical_in_region を備え、ハルシネーション防止のためキリル原語表記が確実な項目のみ original_script='cyrillic' を付与した。

## カテゴリ構成

A. 主要主義・運動（8件）: ロシア・センチメンタリズム／ロシア・ロマンチズム／自然派／スラヴ派 vs 西欧派／ナロードニチェストヴォ文学／ニヒリズム文学／ロシア象徴主義／ロシア・リアリズム。

B. 主要作家概念（8件）: プーシキン「余計な人」／ゴーゴリ「外套」の小人／レールモントフ『現代の英雄』／トゥルゲーネフ『父と子』世代対立／ドストエフスキー「ポリフォニー」（バフチン解釈）／ドストエフスキー『悪霊』／トルストイの歴史哲学／チェーホフの「中身のない人物」。

C. 主要主題/世界観（8件）: ロシア魂／受苦／ユロージヴィ（聖愚者）／リシニー・チェロヴェク（余計な人）／アヴォシ／トスカ／ザイカ／бытие vs быт。

D. 主要詩学・批評（8件）: ベリンスキー「現実批評」／チェルヌィシェフスキー「美と現実」／ピーサレフ・ニヒリスト批評／アポロン・グリゴーリエフ有機的批評／バフチン「ポリフォニー」／バフチン「カーニバル」／バフチン「対話的想像力」／ヤコブソン「文学性」前史。

E. メタ・形式概念（8件）: スカーズ／ロシア小説の長編性／雑誌文学（厚い雑誌）／検閲との交渉／ポエマ／ポーヴェスチ／リテラトゥールヌィ・ブィト／散文の詩化。

## 第四変容タグ（fourth_transform_tags = 11件）

主体軸を中心に、物語軸・受容軸・正典軸・言語軸・真正性軸・翻訳軸の7軸にまたがる。代表例:

- バフチン「ポリフォニー」（バフチン解釈版）→ 主体軸 rethinking + 物語軸 rethinking
- バフチン「ポリフォニー」（独立項）→ 主体軸 + 物語軸 (LLM共著の多声性祖型)
- バフチン「カーニバル」→ 受容軸 + 正典軸（高/低・正典/非正典の解体）
- スカーズ → 言語軸 rethinking（LLMの声色生成）
- リシニー・チェロヴェク → 主体軸 rethinking（AI時代の知識労働者主体性）
- チェーホフ的中身のない人物 → 主体軸 rethinking
- 受苦 → 真正性軸 invariant（模倣困難な真正経験）
- トスカ → 翻訳軸 invariant（翻訳不能性）

「rethinking」と「invariant」両方を含むことで、AI時代に再考される軸と不変として機能する軸の両側面を確保した。

## クロスドメイン接続（cross_domain = 16件）

PHIL 7件、PT 5件、AN 4件の合計16件で要件「最低10件、PT・PHIL・AN多数」を満たす。代表的接続:

- PT × バフチン詩学群 (ポリフォニー・対話的想像力・スカーズ・文学性)
- PHIL × ロシア宗教哲学・対話の哲学 (ベルジャーエフ・シェストフ・ブーバー・レヴィナス・アーレント全体主義論・トルストイ歴史哲学)
- AN × ナロードニチェストヴォの民衆共同体研究／ユロージヴィの宗教人類学／カーニバルとリミナリティ／文学的日常の文学社会学

## ソース構成と検証可能性

source_tier 分布は primary 7件 / secondary 32件 / tertiary 1件。一次資料 URL は以下の検証可能なPD/学術リポジトリに限定した:

- rvb.ru — Russian Virtual Library (プーシキン、ゴーゴリ、レールモントフ、トゥルゲーネフ底本)
- feb-web.ru — Fundamental Electronic Library of Russian Literature (チェルヌィシェフスキー)
- gutenberg.org — Project Gutenberg (英訳『戦争と平和』『悪霊』)
- en/ja/ru.wikipedia.org の academic-grade 項目 (二次的概観)
- plato.stanford.edu (哲学的概念の参照)

tertiary は「ザイカ」1件のみで、これは19世紀ロシア文学の批評的横断テーマとして体系的合成度が高いため tertiary とした。

## 期間設定 (periods)

3期を新規作成:

- ロシア文学黄金時代 (1820-1900)
- ロシア・センチメンタリズム期 (1790-1820)
- ロシア銀の時代前夜 (1890-1900)

すべて region='周縁横断' で統一し、後続Codex（C29 ロシア20世紀／C30 周縁等）と接続可能な構造にした。

## 制約遵守

- ハルシネーション禁止: キリル原語表記は学術的に確認可能なものに限定。不確実なものは name_original 欄を西欧転写に留めた。
- 40件投入を最優先: 全件 [skip] なく新規挿入完了。
- 構造踏襲: パイロットの dict CONCEPTS + main() ループ構造を厳密に踏襲、ループ内 fourth_axes / cross_domain 取り出しも同パターン。

## 完了確認

```
[c28] inserted concepts (this run): 40 / total: 481
[c28] fourth_transform_tags +11; cross_domain +16
```

subfield_id=18 の concepts COUNT(*) = 40 を SQLite で直接確認済み。
