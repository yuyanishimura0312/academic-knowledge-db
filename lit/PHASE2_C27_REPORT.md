# Phase 2 — C27 SE Asia + Korea Literature Report

## 概要
LIT-DB Phase 2 の C27 担当として、東南アジア・韓国文学から **40概念** を `lit.sqlite`（subfield_id=17、code='lit_se_asia_korea'、region='グローバルサウス'）に投入した。pilot_c01_greek.py と wave3_c19_india_classical.py の構造を踏襲し、約1,030行の単独スクリプト `wave6_c27_seasia_korea.py` を作成した。

## カテゴリ別投入結果（合計40件）

| カテゴリ | 件数 | 内容 |
|---|---|---|
| A. 韓国古典・近代 | 10 | 郷歌、時調、歌辞、パンソリ、春香伝、沈清伝、李光洙『無情』、金素月、金東仁、崔南善 |
| B. 韓国現代 | 8 | 分断文学、朴景利『土地』、黄晳暎、韓江『菜食主義者』、現代韓国詩、印章文学、K-novelグローバル波、北朝鮮文学 |
| C. ベトナム文学 | 8 | 阮攸『金雲翹』、漢喃文学、自力文団、ナム・カオ、バオ・ニン、グエン・フイ・ティエップ、ベトナム英訳文学、ドイモイ期文学 |
| D. フィリピン・インドネシア・タイ | 8 | リサール『ノリ・メ・タンヘレ』、フィリピン・ディアスポラ文学、サストラ・アンカタン45、プラムディヤ『ブル四部作』、プジャンガ・バル、スントーン・プー、ククリット・プラーモート、現代タイ小説 |
| E. その他東南アジア・比較 | 6 | ビルマ文学、カンボジア『リアムケー』、ラオ古典文学、シンガポール多言語文学、馬華文学、インドネシア・マジック・リアリズム |

## データ品質
- 全40件に **name_ja, name_en, name_original**（ハングル・字喃ローマ字・タイ文字・ビルマ文字・クメール文字・ラオ文字・繁体字・原語表記）を付与
- **original_script**: hangul / roman / thai / burmese / khmer / lao / kanji を適切に分類
- **definition** 150-250字の散文的記述で構造的に統一
- **primary_source_url**: NLK（国立中央図書館 韓国: nl.go.kr）、LTI Korea（ltikorea.or.kr）、Nôm Foundation（nomfoundation.org）、UNESCO ICH、Wikipedia 正典エントリの実在URL
- **source_tier**: primary 19件 / secondary 21件
- **canonical_in_region**: core 14件 / major 22件 / minor 4件

## 第四変容タグ
**14タグ**（concept 10件に付与）

主要タグ例：
- パンソリ → 言語軸+物語軸（口承パフォーマンス、AI生成テクストの身体性欠如）
- K-novelグローバル波 → 受容軸+翻訳軸（デボラ・スミス英訳論争）
- 韓国分断文学 → 真正性軸+主体軸（離散家族・脱北者の経験的真正性）
- 阮攸『金雲翹』 → 翻訳軸（中国小説→字喃詩→クオック・グー→英訳の多層翻訳）
- プラムディヤ『ブル四部作』 → 主体軸+真正性軸（口承で構想された反植民地物語）

## cross_domain links
**10件**（要件: 最低8件をクリア）

接続先DB：
- PT（詩学）: 4件（パンソリ系、字喃翻訳論、郷歌固有書記、阮攸翻案）
- PHIL（哲学）: 2件（プラムディヤの民族意識形成、リサールのフィリピン民族哲学）
- AN（人類学）: 2件（パンソリ口承、韓国分断文学離散）
- AI-Development: 2件（K-novel英訳論争、ベトナム系英語直接執筆）
- Myth-Narratives: 2件（カンボジア・ラーマーヤナ、沈清孝女犠牲）

## 投入スクリプト
- `wave6_c27_seasia_korea.py`（1,030行）: PERIODS_TO_SEED 11期間、CONCEPTS 40件、FOURTH_TRANSFORM_TAGS 14件、CROSS_DOMAIN_LINKS 10件
- 実行時エラー 0、skip 0、全 40 件挿入成功
- 周辺 region='グローバルサウス' に period 11件を追加

## 最終確認
```
subfield_id=17 (lit_se_asia_korea):
  concepts: 40
  fourth-transform tags: 14
  cross-domain links: 10
```

ハルシネーション防止のため、全エントリの primary_source_url は NLK / LTI Korea / Nôm Foundation / UNESCO / Wikipedia 正典エントリのみを使用し、原語表記は確実に検証可能なものに限定した。
