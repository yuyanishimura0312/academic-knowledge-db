#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche concepts to lit_persian_turkish."""

from lit_db_helper import LitDB


SUBFIELD = "lit_persian_turkish"
REGION = "南西アジア"

P_EARLY = 250
P_MID = 47
P_LATE = 48
P_OTTOMAN = 49
P_TEKKE = 251
P_CENTRAL = 143
P_MINOR = 252


CONCEPTS = [
    # 1. Persian manuscript codicology
    ("ペルシア写本キターバト奥書", "Persian kitabah colophons", P_LATE, "書写者名・日付・場所を記すペルシア写本末尾の奥書。"),
    ("ワクフ印詩集伝来記", "Waqf-stamped divan provenance", P_LATE, "寄進印から詩集写本の所蔵移動を読む伝来記録。"),
    ("ペルシア写本ラクナ補写", "Persian manuscript lacuna repair", P_LATE, "欠落部を後代筆で補った詩文写本の補写痕。"),
    ("ムラッカア断簡貼込順序", "Muraqqa fragment mounting order", P_LATE, "詩画断簡の貼込順が鑑賞順序を作るアルバム構成。"),
    ("ナスタアリーク書写詩句見本", "Nastaliq copied verse specimens", P_LATE, "書家が筆法練習に用いた短詩句の見本書写。"),
    ("タズヒーブ余白花蔓詞", "Tazhib marginal vine captions", P_LATE, "装飾余白の花蔓に添えられる短い献辞や祈願句。"),

    # 2. Persian poetics and rhetoric
    ("ラディーフ二重反復ガザル", "Double-radif ghazals", P_MID, "同一ガザルで二つの反復語を連ねる押韻技巧。"),
    ("カーフィヤ異綴り押韻", "Qafiya orthographic rhyme variants", P_MID, "発音同一で綴りの揺れる語を脚韻に用いる作法。"),
    ("イハーム両義掛詞", "Iham double-meaning pun", P_LATE, "近い意味と遠い意味を同時に響かせる両義掛詞。"),
    ("タズミーン引用半句", "Tazmin quoted hemistichs", P_MID, "先行詩人の半句を自作詩へ組み込む引用技法。"),
    ("タルスィー均衡句法", "Tarsi balanced phrasing", P_LATE, "対応語を左右に配して句の音義を均衡させる修辞。"),
    ("ハブスィヤート嘆願結句", "Habsiyat petition endings", P_MID, "獄中詩の末尾に置く赦免嘆願の定型結句。"),

    # 3. Ottoman textual and performance niches
    ("オスマン・ルースナーメ暦詩", "Ottoman ruzname calendar verse", P_OTTOMAN, "暦注や日誌に添えられた短い吉凶詩句。"),
    ("メヴリド写本サラヴァト句", "Mevlid manuscript salawat lines", P_TEKKE, "預言者讃歌写本で章間に唱和される祝祷句。"),
    ("ディーワーン詩集フェフリスト", "Divan manuscript fihrist indexes", P_OTTOMAN, "巻頭に詩型や脚韻順を示すディーワーン索引。"),
    ("テズキレ死亡年クロノグラム", "Tazkira death-date chronograms", P_OTTOMAN, "詩人小伝で没年を文字数値詩に隠す記録法。"),
    ("オスマン・タフミス増補詩", "Ottoman tahmis expansions", P_OTTOMAN, "既存ガザル各句へ三句を足し五行連にする増補詩。"),
    ("ヘゼルフェン雑録詩欄", "Hezarfen miscellany verse columns", P_OTTOMAN, "博識家雑録に余白欄として収められる詩句群。"),

    # 4. Central Asian Turkic microcultures
    ("チャガタイ・ムハンマス応答詩", "Chagatai mukhammas replies", P_CENTRAL, "先行ガザルへ五行連形式で応答するチャガタイ詩。"),
    ("ホラズム語混交トルキ説話", "Khwarazmian-mixed Turkic tales", P_CENTRAL, "ホラズム語要素を残すトルキ語説話写本の混交層。"),
    ("ブハラ・マドラサ詩合", "Bukhara madrasa poetry contests", P_CENTRAL, "マドラサ学徒が同題同韻で競ったブハラ詩作慣行。"),
    ("コーカンド詩会ムシャーイラ", "Kokand mushaira gatherings", P_CENTRAL, "宮廷詩人が即興応答を競うコーカンド詩会。"),
    ("ウイグル木版キサス余白", "Uyghur woodblock qisas margins", P_CENTRAL, "預言者物語木版本の余白に残る読者注や祈願。"),
    ("テュルキ・アルーズ教本", "Turki aruz primers", P_CENTRAL, "トルキ語詩人向けに韻律型を整理したアルーズ入門。"),

    # 5. Kurdish, Pashto, Balochi, and Sindhi textual niches
    ("クルド・マスナヴィー恋愛序", "Kurdish masnavi love prologues", P_MINOR, "恋愛叙事詩冒頭で恋の権威を述べるクルド語序文。"),
    ("ソラニー新聞詩欄", "Sorani newspaper poetry columns", P_MINOR, "初期新聞に掲載され民族語意識を担ったソラニー詩欄。"),
    ("パシュトー・チャールベイタ脚韻", "Pashto charbeta rhyme schemes", P_MINOR, "四行歌謡チャールベイタを支える連鎖的脚韻型。"),
    ("バローチ・ハニ伝説変奏", "Balochi Hani legend variants", P_MINOR, "ハニ物語を部族歌謡ごとに変える叙事的変奏。"),
    ("スィンディー・スル叙情単位", "Sindhi sur lyric units", P_MINOR, "『リサーロ』各スルを構成する旋律別の叙情単位。"),
    ("ブラーフーイー婚礼即興歌", "Brahui wedding improvised songs", P_MINOR, "婚礼の場で掛け合い式に歌われるブラーフーイー即興歌。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts WHERE subfield_id = 14")
        }
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            if name_ja in existing:
                skipped += 1
                print(f"[skip-name] {name_ja}")
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
            )
            inserted += 1
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
