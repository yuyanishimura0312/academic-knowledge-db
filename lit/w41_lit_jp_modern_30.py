#!/usr/bin/env python3
"""Wave 41: lit_jp_modern (id=11) +30 hyper-niche concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_jp_modern"
REGION = "東アジア"

# period IDs: 8 明治期, 9 大正期, 10 昭和戦前期, 11 戦後期, 12 現代
CONCEPTS = [
    # 明治新聞・翻案の微細形式
    ("明治翻案小説の地名和訳", "Translated Place Names in Meiji Adaptations", 8, "西洋地名を日本地名へ置換する翻案技法。"),
    ("探偵実話の裁判速記体", "Court-Shorthand Detective True Tales", 8, "法廷速記の語りを借りた明治探偵実話文体。"),
    ("雑報欄挿入小説", "News-Column Insert Fiction", 8, "新聞雑報欄へ断片的に紛れ込む小説形式。"),
    ("政治小説の漢語総ルビ", "Full-Ruby Sino-Japanese Political Fiction", 8, "漢語政治語に総ルビを振る啓蒙的文体。"),
    ("講談本口絵キャプション", "Kodan Book Frontispiece Captions", 8, "口絵説明が読解順を誘導する講談本慣行。"),
    ("明治少年雑誌懸賞文", "Meiji Boys' Magazine Prize Prose", 8, "少年雑誌の懸賞欄で形成された模範作文。"),
    # 外地・辺境の小結社
    ("樺太日本語俳句会", "Karafuto Japanese Haiku Circles", 10, "樺太在住者の季語と植民地感覚を持つ俳句結社。"),
    ("南洋群島児童綴方", "South Seas Children Composition", 10, "委任統治領学校で書かれた日本語児童綴方。"),
    ("関東州日本語詩壇", "Kwantung Leased Territory Poetry Scene", 10, "大連・旅順周辺の日本語詩人ネットワーク。"),
    ("奄美復帰前短歌", "Pre-Reversion Amami Tanka", 11, "本土復帰前の境界意識を詠む奄美短歌。"),
    ("小笠原帰還者手記", "Ogasawara Returnee Memoirs", 11, "返還前後の帰島経験を記す島民手記。"),
    ("北海道炭鉱同人短歌", "Hokkaido Coalfield Coterie Tanka", 11, "炭鉱労働者同人誌に載る生活短歌。"),
    # 謄写版・回覧・学校文芸
    ("肉筆回覧詩誌", "Hand-Copied Circulating Poetry Magazines", 9, "同人間を肉筆で回覧した私的詩誌形態。"),
    ("謄写版句集奥付", "Mimeographed Haiku Colophon", 10, "謄写版句集の奥付に残る配布圏情報。"),
    ("青年訓練所文芸誌", "Youth Training School Literary Magazines", 10, "青年訓練所内で作られた半軍事的文芸誌。"),
    ("女学校校友会小説", "Girls' School Alumnae Fiction", 9, "校友会誌に載る女学生・卒業生の短編。"),
    ("工場寄宿舎壁新聞詩", "Factory Dormitory Wall-Newspaper Poetry", 11, "寄宿舎壁新聞に掲示された労働詩。"),
    ("療養所回覧童話", "Sanatorium Circulating Fairy Tales", 11, "療養所内で回覧された童話・短篇。"),
    # 忘却作家・稀覯作品
    ("水野仙子『神楽坂の半襟』", "Kagurazaka no Haneri (Mizuno Senko)", 9, "都市女性の労働と装いを描く短編。"),
    ("素木しづ『三十三の死』", "Thirty-Three Deaths (Shizuko Sogi)", 9, "病と夭折感覚を刻む大正期女性短編。"),
    ("尾崎翠『第七官界彷徨』", "Wandering in the Seventh Sense", 10, "感覚論を奇想化した鳥取出身作家の実験小説。"),
    ("佐多稲子『キャラメル工場から』", "From the Caramel Factory", 10, "女工経験を起点にした初期プロレタリア短編。"),
    ("真杉静枝『小魚の心』", "Heart of a Small Fish", 10, "植民地台湾体験を含む女性作家の短編世界。"),
    ("芝木好子『青果の市』", "Fruit and Vegetable Market", 11, "市場の労働と女性生活を描く戦後短編。"),
    # 理論・読解の小論点
    ("私小説の伏字索引問題", "I-Novel Redaction Index Problem", 11, "伏字人物を索引化する際の実名比定論点。"),
    ("方言ルビの内地標準語化", "Dialect Ruby Standardization", 10, "方言語彙を標準語ルビで馴致する表記問題。"),
    ("戦後雑誌座談会の匿名発言", "Anonymous Speech in Postwar Roundtables", 11, "座談会記録で発言主体が曖昧化する問題。"),
    ("少女小説の手紙体余白", "Epistolary Blank Space in Girls' Fiction", 10, "手紙体小説の余白が感情を演出する形式。"),
    ("連載末尾予告の焦点化", "Focalization in Serial Teasers", 8, "次号予告文が読者の視点を先取りする技法。"),
    ("全集月報の自己正典化", "Self-Canonization in Collected-Works Inserts", 12, "全集月報で作家像を再編集する受容装置。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")
    too_long = [(name, len(defn)) for name, _, _, defn in CONCEPTS if len(defn) > 100]
    if too_long:
        raise SystemExit(f"definition over 100 chars: {too_long}")

    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 11"
            )
        }
        dupes = [name for name, _, _, _ in CONCEPTS if name in existing]
        if dupes:
            raise SystemExit(f"duplicates in subfield 11: {dupes}")

        inserted = 0
        for name_ja, name_en, period_id, definition in CONCEPTS:
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

        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 11"
        ).fetchone()["c"]
        print(f"Inserted {inserted}; total subfield 11: {total}")


if __name__ == "__main__":
    main()
