#!/usr/bin/env python3
"""Wave 42: add 30 hyper-niche concepts to lit_persian_turkish."""

from lit_db_helper import LitDB


SUBFIELD = "lit_persian_turkish"
REGION = "南西アジア"

P_EARLY = 250
P_MID = 47
P_LATE = 48
P_OTTOMAN = 49
P_TEKKE = 251
P_MODERN = 51
P_PROSE = 141
P_CENTRAL = 143
P_MINOR = 252


CONCEPTS = [
    # 1. Persian manuscript paratexts
    ("ディーワーン写本ディーバーチェ自序", "Persian divan manuscript dibacha prefaces", P_LATE, "詩人像と編纂意図を短く示すディーワーン巻頭自序。"),
    ("ペルシア写本シャムセ扉詞", "Persian shamsa frontispiece texts", P_LATE, "金泥円章に献辞や所有者名を収める扉詞章。"),
    ("ハーフェズ写本ガザル番号異同", "Hafez manuscript ghazal numbering variants", P_MODERN, "占いや注釈で参照されるガザル番号の写本差。"),
    ("『ユースフとズライハー』挿絵詞書", "Yusuf u Zulaykha miniature captions", P_LATE, "細密画場面を短いペルシア語で標識する詞書。"),
    ("ムンシャアート署名祈願句", "Munshaat signature blessing formulae", P_PROSE, "書簡範例末尾に置かれる署名と祈願の定型句。"),
    ("サフィーナ折丁錯簡復元", "Safina quire misbinding reconstruction", P_LATE, "小型詩華写本の折丁乱れを詩順から復元する作業。"),

    # 2. Persian poetic microforms and riddling
    ("ペルシア・タルジーバンド連鎖句", "Persian tarji-band refrain chains", P_MID, "各節末の反復句で思想転換を結ぶ連作詩型。"),
    ("ペルシア・タルキーブバンド結句差替", "Persian tarkib-band changing couplets", P_MID, "節ごとに結句を替え意味を段階化する詩型。"),
    ("ムスタザード余剰半句", "Mustazad appended hemistichs", P_LATE, "各半句へ短い余剰句を添える拡張ガザル技法。"),
    ("ペルシア・ルガズ詩謎", "Persian lughz verse riddles", P_LATE, "物名を隠し比喩の連鎖で解かせる詩謎形式。"),
    ("ムアッマー名隠しペルシア詩", "Persian muamma name riddles", P_LATE, "文字計算や語分解で人名を隠す謎詩。"),
    ("サブク・ヒンディー新意狩り", "Sabk-i Hindi fresh-conceit hunting", P_LATE, "未聞の比喩を競うインド様式詩人の技巧意識。"),

    # 3. Ottoman performance and notebook niches
    ("オスマン・メジュムア歌詞雑録", "Ottoman mecmua song miscellanies", P_OTTOMAN, "歌曲・詩・祈祷を混載する私的雑録帳。"),
    ("アーシュク・ジョンク手帖", "Ashik conk notebooks", P_TEKKE, "吟遊詩人が歌詞や系譜を書き留めた縦長手帖。"),
    ("タリカト・ネフェス歌詞", "Tarikat nefes lyrics", P_TEKKE, "修道会儀礼で歌われる神秘主義的トルコ語歌詞。"),
    ("カフヴェハーネ・メッダー台本", "Coffeehouse meddah scripts", P_OTTOMAN, "語り手が町場で用いた一人語り芸の筋書き。"),
    ("オルタオユヌ導入歌", "Ortaoyunu opening songs", P_OTTOMAN, "即興喜劇の登場と場面設定を支える導入歌。"),
    ("カラギョズ・ムハーヴェレ写本", "Karagoz muhavere manuscripts", P_OTTOMAN, "影絵本編前の掛け合いを記す会話部写本。"),

    # 4. Chagatai and Central Asian textual microcultures
    ("チャガタイ・バヤーズ詩帖", "Chagatai bayaz poetry notebooks", P_CENTRAL, "中央アジア読者が抜粋詩を集めた私用詩帖。"),
    ("ナヴァーイー・ナズィーラ競作", "Navai nazira imitations", P_LATE, "ナヴァーイー詩へ同韻同題で応答する模倣詩。"),
    ("ホカンド宮廷女性タズキラ", "Kokand court women's tazkira notices", P_CENTRAL, "ホカンド詩壇で女性詩人を記録する小伝群。"),
    ("カシュガル東トルキ・マジュムア", "Kashgar Eastern Turki majmua", P_CENTRAL, "東トルキ語詩文を混載するカシュガル系雑録写本。"),
    ("ヤルカンド聖者マンキブ", "Yarkand saintly manaqib", P_CENTRAL, "ヤルカンド聖者の奇跡を語るトルキ語聖者伝。"),
    ("トルクメン・ゲログル写本異本", "Turkmen Gorogly manuscript variants", P_CENTRAL, "ゲログル叙事詩を写本ごとに変奏する異本群。"),

    # 5. Kurdish, Pashto, Balochi, and Sindhi microtraditions
    ("クルマンジー・ラウク恋歌", "Kurmanji lawik love songs", P_MINOR, "クルマンジー語で歌われる短い恋愛叙情歌。"),
    ("ムクリヤーニー印刷ソラニー詩", "Mukriyani printed Sorani poetry", P_MINOR, "初期ソラニー印刷文化を支えたムクリヤーニー系詩。"),
    ("パシュトー・タッパ女性応答歌", "Pashto tappa women's response songs", P_MINOR, "女性の即興応答で流通する二行パシュトー短歌。"),
    ("バローチ・シャイル戦歌", "Balochi shair war songs", P_MINOR, "部族抗争や英雄行動を短詩で伝える戦歌。"),
    ("スィンディー・カーフィー聖歌", "Sindhi kafi devotional songs", P_MINOR, "スーフィー聖者崇敬を歌うスィンディー抒情聖歌。"),
    ("ブラーフーイー叙事歌断片", "Brahui epic song fragments", P_MINOR, "ブラーフーイー語で断片的に伝わる英雄叙事歌。"),
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
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
