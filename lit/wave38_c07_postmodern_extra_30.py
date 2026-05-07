#!/usr/bin/env python3
"""Wave 38: lit_eu_postmodern (id=7) extra 30 niche concepts."""

from lit_db_helper import LitDB


SUBFIELD = "lit_eu_postmodern"
REGION = "西欧"


CONCEPTS = [
    # Cluster 1: 欧州メタフィクション細部
    ("アラズラキ・新幻想", "Alazraki neo-fantastic", "lo neofantastico", "latin", "ポストモダン期", "恐怖より知覚裂け目を重視する戦後幻想小説論", 3),
    ("ウリポ的潜在文学", "Oulipian potential literature", "litterature potentielle", "latin", "ポストモダン期", "制約から未在の形式を生成する実験文学の方法", 4),
    ("プレテクスト小説", "pretextual novel", "pre-textual fiction", "latin", "ポストモダン期", "注釈・草稿・索引など準本文が物語本体を侵食する形式", 3),
    ("偽学術装置", "pseudo-scholarly apparatus", "pseudo-scholarly apparatus", "latin", "ポストモダン期", "脚注や索引を虚構化し知の権威を攪乱する技法", 4),
    ("偽翻訳小説", "pseudotranslation fiction", "pseudotraduction", "latin", "ポストモダン期", "翻訳書を装い原作性と文化帰属を曖昧化する小説形式", 4),
    ("消失章構成", "missing-chapter structure", "missing chapter", "latin", "ポストモダン期", "欠落した章や断片を読者の推理で補わせる構成技法", 3),

    # Cluster 2: 記憶・アーカイヴ
    ("アーカイヴ的自伝", "archival autobiography", "archival autobiography", "latin", "自伝的現代期", "私的記憶を写真・公文書・目録で検証する自伝形式", 4),
    ("文書フェティシズム", "document fetishism", "fetichisme documentaire", "latin", "自伝的現代期", "証拠文書への過剰依存が真実性を逆に不安定化する効果", 3),
    ("記憶の空白地図", "cartography of memory gaps", "cartographie des lacunes", "latin", "自伝的現代期", "失われた場所や証言の欠落を地図化する記憶叙述", 3),
    ("写真テクスト複合", "photo-text composite", "photo-text", "latin", "自伝的現代期", "写真と散文が互いの証拠性を補強・失効させる形式", 4),
    ("証言の二次性", "secondary witnessing", "secondary witnessing", "latin", "自伝的現代期", "直接経験なき世代が媒介資料で証言を継承する叙述", 4),
    ("遺品カタログ叙述", "relic catalogue narration", "catalogue des reliques", "latin", "自伝的現代期", "遺品一覧が人物像と喪失を断片的に構成する語り", 3),

    # Cluster 3: 後期社会主義・移行期
    ("検閲後寓話", "post-censorship allegory", "post-censorship allegory", "latin", "ポストモダン期", "検閲崩壊後も残る暗号化習慣を使う政治寓話", 4),
    ("サミズダート残響", "samizdat afterecho", "samizdat afterecho", "latin", "ポストモダン期", "地下出版の形式記憶が市場化後の文体に残る現象", 4),
    ("移行期ブラックユーモア", "transition black humour", "transition black humour", "latin", "ポストモダン期", "体制転換の不条理を暴力的笑いで描く東欧的語法", 3),
    ("官僚的グロテスク", "bureaucratic grotesque", "bureaucratic grotesque", "latin", "ポストモダン期", "書類・規則・窓口が怪物化する後期社会主義的表象", 4),
    ("ポスト全体主義キッチュ", "post-totalitarian kitsch", "post-totalitarian kitsch", "latin", "ポストモダン期", "旧体制記号が商品化され空虚な懐旧へ転じる美学", 3),
    ("地下出版パロディ", "samizdat parody", "samizdat parody", "latin", "ポストモダン期", "秘密流通形式そのものを模倣し笑いに変える実験", 3),

    # Cluster 4: 欧州オートフィクション細部
    ("非人称自伝", "impersonal autobiography", "autobiographie impersonnelle", "latin", "自伝的現代期", "一人称を薄め社会的型として自己を記述する自伝形式", 4),
    ("社会学的私小説", "sociological autofiction", "autofiction sociologique", "latin", "自伝的現代期", "階級移動や制度経験を自己物語の核に据える小説", 4),
    ("母語喪失自伝", "mother-tongue loss memoir", "perte de la langue maternelle", "latin", "自伝的現代期", "移住や同化で失われた母語を自己形成の傷として語る形式", 3),
    ("最小自伝断片", "minimal autobiographical fragment", "fragment autobiographique minimal", "latin", "自伝的現代期", "極短断章で自己像を累積させる自伝的散文形式", 3),
    ("親密圏の記録小説", "documentary intimacy novel", "roman documentaire intime", "latin", "自伝的現代期", "家族・恋愛・ケアの記録を資料的に編成する小説", 3),
    ("自己消去語り手", "self-effacing narrator", "self-effacing narrator", "latin", "自伝的現代期", "語り手が他者の声の媒介へ退き自己を間接化する技法", 4),

    # Cluster 5: ポストデジタル欧州小説
    ("プラットフォーム・リアリズム", "platform realism", "platform realism", "latin", "ポスト・ポストモダン期", "SNSや配信基盤が生活世界の現実感を形作る小説語法", 4),
    ("通知散文", "notification prose", "notification prose", "latin", "ポスト・ポストモダン期", "通知・ログ・短文断片で意識の分断を表す散文形式", 3),
    ("検索履歴叙述", "search-history narration", "search-history narration", "latin", "ポスト・ポストモダン期", "検索語列が欲望・記憶・不安を間接的に物語る形式", 3),
    ("データ化された親密性", "datafied intimacy", "datafied intimacy", "latin", "ポスト・ポストモダン期", "恋愛や友情が数値・履歴・推薦で媒介される表象", 4),
    ("ポストデジタル倦怠", "post-digital fatigue", "post-digital fatigue", "latin", "ポスト・ポストモダン期", "接続過多後の疲弊と低強度の疎外を描く現代小説感覚", 3),
    ("アルゴリズム的偶然", "algorithmic serendipity", "algorithmic serendipity", "latin", "ポスト・ポストモダン期", "推薦や検索が偶然の出会いを擬似生成する物語装置", 3),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB() as db:
        periods = {
            "ポストモダン期": db.get_or_create_period("ポストモダン期", REGION, 1960, 2000),
            "自伝的現代期": db.get_or_create_period("自伝的現代期", REGION, 1990, 2025),
            "ポスト・ポストモダン期": db.get_or_create_period("ポスト・ポストモダン期", REGION, 2000, 2025),
        }
        for name_ja, name_en, name_original, script, period_key, definition, score in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja} {len(definition)}")
            period_id = periods[period_key]
            existed = db.find_concept(name_ja, REGION, period_id) is not None
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=score,
                source_tier="secondary",
                canonical_in_region="minor",
                skip_duplicates=True,
            )
            if existed:
                skipped += 1
            else:
                inserted += 1
        total = db.conn.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=7").fetchone()[0]
    print(f"inserted={inserted} skipped={skipped} total={total}")


if __name__ == "__main__":
    main()
