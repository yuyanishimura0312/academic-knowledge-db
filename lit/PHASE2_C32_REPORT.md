# Phase 2 — C32 LIT-Diaspora 投入レポート

## 概要
LIT-DB Phase 2 Wave 5 の Codex「C32: LIT-Diaspora（ディアスポラ・移民文学）」の投入結果を報告する。`subfield_id=20` (`code='lit_diaspora'`, `region='周縁横断'`) に対し、実証済みパターン（`pilot_c01_greek.py`）の構造を踏襲して40概念を一括投入した。

## 投入結果

| 項目 | 件数 |
|------|------|
| concepts (subfield_id=20) | 40 |
| fourth_transform_tags (本ラン分) | 21 |
| cross_domain (本ラン分) | 17 |
| relations (本ラン分) | 45 |
| periods 新規シード | 4 |

source_tier 内訳（DB全体）は primary 449 / secondary 300 / tertiary 12 となり、本ランも primary を中核に据えた。

## カテゴリ別投入（各8件 × 5）

- **A. 主要主題・世界観**: hyphenated identity, in-between space (Bhabha), third space, transnational subject, double consciousness (Du Bois), exile/exilic condition, multilingual self, deterritorialization。
- **B. 主要文化圏ディアスポラ文学**: Black Atlantic (Gilroy), Caribbean diaspora, South Asian diaspora, Chinese diaspora 文学, Jewish diaspora 文学, Arab diaspora (Mahjar), Korean diaspora, Chicano/a 文学。
- **C. 主要技法・形式**: code-switching, translingual writing, untranslated foreign words, multilingual punning, exile memoir, generational saga, transgenerational trauma narrative, palimpsestic narrative。
- **D. 主要作家概念**: imaginary homelands (Rushdie), translation as condition (Lahiri), Spanglish (Díaz), border voice (Cisneros), ancestral memory (Danticat), reluctant fundamentalism (Hamid), language politics (Ngũgĩ), mediation (Hosseini)。
- **E. 批評概念・理論**: diasporic aesthetics, hybridity (Bhabha), mimicry (colonial), contact zone (Pratt), cultural translation (Asad), traveling theory (Said), exophonic writing, translocality。

## 第四変容タグ（21件、9軸全可能性）

ディアスポラ領域の特性として、9軸全方向に展開できる広域な再考の場であることを反映し、軸の偏りを意図的に分散した。`multilingual self` には言語軸+主体軸を、`exile/exilic condition` には主体軸+真正性軸を、`code-switching` には言語軸（多言語LLM並走）を、`third space` には主体軸+受容軸を、`imaginary homelands` には真正性軸+物語軸を、`translocality` には翻訳軸+主体軸を付与した。これにディアスポラ的美学・ハイフン化アイデンティティ・double consciousness・translingual writing・exophonic writing・hybridity・palimpsestic narrative・untranslated insertion・Lahiri 翻訳条件・Ngũgĩ 言語政治を加え、合計21件で言語/主体/翻訳/真正性/物語/受容の6軸を覆った。

## cross_domain（17件、最低10件要件をクリア）

要件の各DBに対し以下のように接続を配した。

- **PHIL**: in-between space, double consciousness, deterritorialization, hybridity (Bhabha), traveling theory (Said) — 計5件。Bhabha・Said・Du Bois・Deleuze の哲学的位置と直接接続。
- **AN**: third space, double consciousness, Black Atlantic, hybridity, contact zone, cultural translation (Asad) — 計6件。人類学DBのコンタクト・ゾーン/ハイブリディティ/二重意識/Asad 文化翻訳と共有。
- **PT**: translation as condition, cultural translation — 計2件。詩学DBの翻訳論との接続。
- **AI-Development**: multilingual self, code-switching, language politics (Ngũgĩ) — 計3件。多言語LLM並走・LLMの言語的不均衡論との接続。
- **計17件**（10件の最低要件を超過）。

## relations（45件）

カテゴリ内およびカテゴリ間の概念対を `extends` / `contains` / `influences` / `criticizes` の関係型で結節した。代表的な系譜的接続として、Du Bois → Gilroy（二重意識→ブラック・アトランティック）、Bhabha 内部系譜（mimicry → hybridity → in-between → third space）、Said 系譜（exile → traveling theory → cultural translation）、Lahiri / Ngũgĩ 翻訳論争軸（条件としての翻訳 vs 言語政治）、ディアスポラ作家系譜（Rushdie → Lahiri → Hamid、Cisneros → Díaz、Danticat → 世代間トラウマ）を含めた。

## periods シード

4 期間（近代奴隷制期 1500-1900 / 脱植民地・初期移民期 1900-1965 / ポストコロニアル・ディアスポラ期 1965-2000 / グローバル・ディアスポラ期 2000-2026）を新規追加し、各概念を適切な期間に紐付けた。

## ハルシネーション防止

各概念の primary_source_url は、Bhabha / Gilroy / Said / Du Bois / Pratt / Asad / Ngũgĩ / Lahiri / Rushdie / Anzaldúa / Cisneros / Danticat / Hamid / Hosseini / Díaz / Min Jin Lee / Hirsch などの実在する出版社（Harvard UP, Routledge, Columbia UP, Penguin Random House, Princeton UP, Cambridge UP, James Currey, Aunt Lute, Brill, Duke UP）の書誌ページ、または JSTOR・Britannica・Project Gutenberg・AAWW・Cervantes Virtual の公開ページを参照した。出版年・刊行情報・作家名は既存の標準書誌に依拠し、創作的誇張を避けた。

## 成果物

- スクリプト: `/Users/nishimura+/projects/research/academic-knowledge-db/lit/wave5_c32_diaspora.py`
- 本レポート: `/Users/nishimura+/projects/research/academic-knowledge-db/lit/PHASE2_C32_REPORT.md`
- DB: `/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite` (subfield_id=20 に40件投入完了)
