#!/usr/bin/env python3
"""Wave 40: lit_jp_modern (id=11) +30 hyper-niche concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_jp_modern"
REGION = "東アジア"

CONCEPTS = [
    # 明治の印刷・新聞小説装置
    ("新聞小説前号梗概", "newspaper serial recap", 8, "連載読者の記憶を補助する前回要約欄。"),
    ("明治口絵の人物先取り", "Meiji kuchie foreshadowing", 8, "挿絵が人物像を本文より先に規定する読書効果。"),
    ("硯友社的句読点過多", "Kenyusha dense punctuation", 8, "美文調の息遣いを細かい句読点で刻む文体癖。"),
    ("投書欄連動小説", "reader-column linked fiction", 8, "新聞投書欄の反応を連載展開へ取り込む形式。"),
    ("講談速記由来の地の文", "kodan shorthand narration", 8, "講談速記の調子を小説の説明文に残す語り。"),
    ("活版ルビの心理強調", "typographic ruby emphasis", 8, "ルビで語の情緒や心理的読みを過剰指定する技法。"),
    # 大正同人誌・文壇小装置
    ("同人誌合評会メモ", "coterie review minutes", 9, "同人内批評を作品形成の記録として残す慣行。"),
    ("私小説実名伏字", "I-novel masked real names", 9, "実名性を保ちつつ伏字で醜聞性を高める表記。"),
    ("文壇ゴシップ引用文体", "bundan gossip citation style", 9, "噂話を批評や小説の証拠風に組み込む文体。"),
    ("同人費自弁出版", "self-funded coterie printing", 9, "会員負担で小部数雑誌を維持する出版方式。"),
    ("校正刷回覧批評", "galley-circulated critique", 9, "校正刷を回して同人が相互に批評する慣習。"),
    ("文芸時評の新人命名", "critic-made newcomer labels", 9, "時評が新人群を命名し文壇配置を作る作用。"),
    # 外地日本語文学の媒体回路
    ("外地文芸欄の内地転載", "metropole reprint of colony pages", 10, "外地新聞の文芸欄が内地誌面へ再流通する回路。"),
    ("台湾日本語短歌結社", "Taiwan Japanese tanka circles", 10, "台湾で日本語短歌を結社的に制作した場。"),
    ("満洲開拓文学懸賞", "Manchurian settler fiction prizes", 10, "満洲開拓を題材に募集された文学懸賞制度。"),
    ("南方徴用作家手記", "southern conscript writer notes", 10, "南方占領地へ派遣された作家の現地記録文。"),
    ("外地方言ルビ", "colonial dialect ruby gloss", 10, "外地語彙や方言をルビで異 exotic 化する表記。"),
    ("帝国地図口絵", "imperial map frontispiece", 10, "外地物語の冒頭で版図感覚を示す地図挿絵。"),
    # 戦時検閲・用紙統制の文学形態
    ("用紙割当短篇化", "paper-rationed short fiction", 10, "用紙統制で短篇や圧縮文体が促された現象。"),
    ("検閲削除空白", "censorship blank space", 10, "伏字や空白で削除痕を読ませる戦時表記。"),
    ("国策文学座談会", "policy-literature roundtable", 10, "座談会形式で国策文学の規範を調整する媒体。"),
    ("慰問袋掲載詩", "comfort-package poems", 10, "兵士慰問袋に同封・掲載された短詩形式。"),
    ("従軍ペン部隊報告", "war-writer corps reports", 10, "従軍作家団が戦場体験を報告文学化した文書。"),
    ("銃後少女雑誌小説", "home-front girls' magazine fiction", 10, "少女雑誌で銃後奉仕を物語化した小説形式。"),
    # 戦後・現代の小媒体実験
    ("ガリ版詩誌ネットワーク", "mimeograph poetry networks", 11, "ガリ版小詩誌が地域横断的に交換された回路。"),
    ("占領期翻訳欄", "Occupation-era translation columns", 11, "占領期雑誌で米英文学翻訳を連載した欄。"),
    ("貸本劇画小説混淆", "rental manga-fiction hybrid", 11, "貸本文化で劇画的構成と小説語りが混じる形式。"),
    ("ミニコミ女性詩", "minikomi women's poetry", 12, "小流通誌で女性の身体感覚を詩化した実践。"),
    ("ワープロ同人誌文体", "word-processor coterie style", 12, "ワープロ組版が同人誌の改行や余白を変えた文体。"),
    ("震災後掌篇連鎖", "post-disaster flash-fiction chains", 12, "震災後に短い掌篇が連鎖的に共有された形式。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")
    too_long = [(name, len(defn)) for name, _, _, defn in CONCEPTS if len(defn) > 100]
    if too_long:
        raise SystemExit(f"definition over 100 chars: {too_long}")

    with LitDB() as db:
        existing = {
            r["name_ja"]
            for r in db.conn.execute("SELECT name_ja FROM concepts WHERE subfield_id = 11")
        }
        dupes = [name for name, _, _, _ in CONCEPTS if name in existing]
        if dupes:
            raise SystemExit(f"duplicates in subfield 11: {dupes}")

        inserted = 0
        for name_ja, name_en, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_ja,
                original_script="kanji",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1

        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 11"
        ).fetchone()["c"]
        print(f"Inserted {inserted}; total subfield 11: {total}")


if __name__ == "__main__":
    main()
