"""
LIT-DB Wave 31 — C33 Genre +30 (compact, no background)
========================================================
Adds 30 new concepts to subfield 'lit_genre' (id=21).
5 thematic clusters x 6 concepts each.
period_id=269 (横断 ジャンル理論期), region='周縁横断'.
Definitions kept <=100 chars. Mostly secondary tier.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

SUBFIELD_CODE = "lit_genre"
REGION = "周縁横断"
PERIOD_ID = 269  # ジャンル理論期 (横断)

CONCEPTS: list[dict] = [
    # === Cluster 1: SF (alternatives, not duplicating existing) ===
    {"name_ja": "アシモフ『鋼鉄都市』",
     "name_en": "Isaac Asimov: The Caves of Steel",
     "name_original": "The Caves of Steel",
     "definition": "アシモフ1954年作。ロボットR.ダニールと刑事ベイリの未来都市SFミステリ融合古典。"},
    {"name_ja": "クラーク『幼年期の終り』",
     "name_en": "Arthur C. Clarke: Childhood's End",
     "name_original": "Childhood's End",
     "definition": "クラーク1953年作。人類の進化的超越を描く形而上的SFの代表作。"},
    {"name_ja": "ハインライン『月は無慈悲な夜の女王』",
     "name_en": "Robert A. Heinlein: The Moon Is a Harsh Mistress",
     "name_original": "The Moon Is a Harsh Mistress",
     "definition": "ハインライン1966年作。月植民地の独立革命を描くリバタリアン的政治SFの古典。"},
    {"name_ja": "ル=グウィン『ゲド戦記』",
     "name_en": "Ursula K. Le Guin: A Wizard of Earthsea",
     "name_original": "A Wizard of Earthsea",
     "definition": "ル=グウィン1968年開始の異世界ファンタジー連作。真の名と影の哲学的探究を描く。"},
    {"name_ja": "ディック『高い城の男』",
     "name_en": "Philip K. Dick: The Man in the High Castle",
     "name_original": "The Man in the High Castle",
     "definition": "ディック1962年作。枢軸国勝利の歴史改変SFで、現実認識の不確かさを問う。"},
    {"name_ja": "ギブスン『カウント・ゼロ』",
     "name_en": "William Gibson: Count Zero",
     "name_original": "Count Zero",
     "definition": "ギブスン1986年作。『ニューロマンサー』に続くスプロール三部作第二作、サイバーパンク拡張。"},

    # === Cluster 2: Fantasy ===
    {"name_ja": "トールキン『指輪物語』",
     "name_en": "J.R.R. Tolkien: The Lord of the Rings",
     "name_original": "The Lord of the Rings",
     "definition": "トールキン1954-55年作。中つ国を舞台とする現代ハイ・ファンタジーの規範を確立した三部作。"},
    {"name_ja": "ルイス『ライオンと魔女』",
     "name_en": "C.S. Lewis: The Lion, the Witch and the Wardrobe",
     "name_original": "The Lion, the Witch and the Wardrobe",
     "definition": "ルイス1950年作。ナルニア年代記第一作で、児童ファンタジーにキリスト教寓意を導入した。"},
    {"name_ja": "ル=グウィン『影との戦い』",
     "name_en": "Ursula K. Le Guin: A Wizard of Earthsea (vol.1)",
     "name_original": "A Wizard of Earthsea",
     "definition": "ゲド戦記第一巻。若き魔法使いゲドが自身の影と対峙する成長譚で、心理的ファンタジーの古典。"},
    {"name_ja": "プルマン『黄金の羅針盤』",
     "name_en": "Philip Pullman: Northern Lights / The Golden Compass",
     "name_original": "Northern Lights",
     "definition": "プルマン1995年作。『ライラの冒険』第一巻で、神学批判的ファンタジーの代表作。"},
    {"name_ja": "ローリング『賢者の石』",
     "name_en": "J.K. Rowling: Harry Potter and the Philosopher's Stone",
     "name_original": "Harry Potter and the Philosopher's Stone",
     "definition": "ローリング1997年作。ハリー・ポッター連作の出発点で、現代児童ファンタジーの世界的現象を起動。"},
    {"name_ja": "マーティン『七王国の玉座』",
     "name_en": "George R.R. Martin: A Game of Thrones",
     "name_original": "A Game of Thrones",
     "definition": "マーティン1996年作。『氷と炎の歌』第一巻で、グリムダーク・ファンタジーの規範を確立。"},

    # === Cluster 3: Mystery ===
    {"name_ja": "クリスティ『そして誰もいなくなった』",
     "name_en": "Agatha Christie: And Then There Were None",
     "name_original": "And Then There Were None",
     "definition": "クリスティ1939年作。孤島連続殺人の極限的密室変奏で、史上最も売れたミステリの一つ。"},
    {"name_ja": "セイヤーズ『ナイン・テイラーズ』",
     "name_en": "Dorothy L. Sayers: The Nine Tailors",
     "name_original": "The Nine Tailors",
     "definition": "セイヤーズ1934年作。ピーター卿ものの代表作で、英国村落と教会鐘文化を背景にした文学的ミステリ。"},
    {"name_ja": "ハメット『血の収穫』",
     "name_en": "Dashiell Hammett: Red Harvest",
     "name_original": "Red Harvest",
     "definition": "ハメット1929年作。コンチネンタル・オプ物の代表作で、ハードボイルド派の出発点。"},
    {"name_ja": "チャンドラー『大いなる眠り』",
     "name_en": "Raymond Chandler: The Big Sleep",
     "name_original": "The Big Sleep",
     "definition": "チャンドラー1939年作。マーロウ初登場の長編で、ハードボイルド文体の規範を確立した。"},
    {"name_ja": "ハイスミス『太陽がいっぱい』",
     "name_en": "Patricia Highsmith: The Talented Mr. Ripley",
     "name_original": "The Talented Mr. Ripley",
     "definition": "ハイスミス1955年作。リプリー連作第一作で、犯罪心理サスペンスの傑作。"},
    {"name_ja": "ル・カレ『寒い国から帰ってきたスパイ』",
     "name_en": "John le Carré: The Spy Who Came in from the Cold",
     "name_original": "The Spy Who Came in from the Cold",
     "definition": "ル・カレ1963年作。冷戦リアリズム・スパイ小説の規範を確立した文学的諜報小説。"},

    # === Cluster 4: Horror ===
    {"name_ja": "ラヴクラフト『クトゥルフの呼び声』",
     "name_en": "H.P. Lovecraft: The Call of Cthulhu",
     "name_original": "The Call of Cthulhu",
     "definition": "ラヴクラフト1928年発表の中編。クトゥルフ神話体系の中核テクストで、コズミック・ホラーの起点。"},
    {"name_ja": "ジャクスン『丘の屋敷』",
     "name_en": "Shirley Jackson: The Haunting of Hill House",
     "name_original": "The Haunting of Hill House",
     "definition": "ジャクスン1959年作。心理ゴシック・ホラーの古典で、現代幽霊屋敷小説の規範作。"},
    {"name_ja": "キング『キャリー』",
     "name_en": "Stephen King: Carrie",
     "name_original": "Carrie",
     "definition": "キング1974年デビュー作。超能力少女ホラーで、現代大衆ホラー文学市場の幕開けを画した。"},
    {"name_ja": "バーカー『血の本』",
     "name_en": "Clive Barker: Books of Blood",
     "name_original": "Books of Blood",
     "definition": "バーカー1984-85年連作短編集。スプラッターパンク・ホラーの起点で、身体性と聖性の融合を探究。"},
    {"name_ja": "ストラウブ『ゴースト・ストーリー』",
     "name_en": "Peter Straub: Ghost Story",
     "name_original": "Ghost Story",
     "definition": "ストラウブ1979年作。米国小都市の幽霊譚で、現代文学的ホラーの代表作。"},
    {"name_ja": "オーツ『かれら』",
     "name_en": "Joyce Carol Oates: them",
     "name_original": "them",
     "definition": "オーツ1969年作。デトロイト下層家族の暴力的歴史を描き、ゴシック的リアリズムでNBA受賞。"},

    # === Cluster 5: Graphic novel + Children's ===
    {"name_ja": "シュピーゲルマン『マウスII』",
     "name_en": "Art Spiegelman: Maus II",
     "name_original": "Maus: A Survivor's Tale, Part II",
     "definition": "シュピーゲルマン1991年作。ホロコースト体験の続編で、グラフィックノベル文学化の決定的画期。"},
    {"name_ja": "サトラピ『ペルセポリス2』",
     "name_en": "Marjane Satrapi: Persepolis 2",
     "name_original": "Persepolis 2: The Story of a Return",
     "definition": "サトラピ2004年作。革命後イラン・欧州亡命の自伝的グラフィック・メモワール続編。"},
    {"name_ja": "ベクデル『ファン・ホーム』のメタ的手法",
     "name_en": "Bechdel Fun Home: metafictional technique",
     "name_original": "Fun Home: A Family Tragicomic",
     "definition": "ベクデル2006年作の文学引用織込み手法。家族史と読書経験を重層化したクイア自伝の方法論。"},
    {"name_ja": "ムーア『ウォッチメン』",
     "name_en": "Alan Moore: Watchmen",
     "name_original": "Watchmen",
     "definition": "ムーア／ギボンズ1986-87年作。スーパーヒーロー脱構築でグラフィックノベル文学化を画した。"},
    {"name_ja": "センダック『まよなかのだいどころ』",
     "name_en": "Maurice Sendak: In the Night Kitchen",
     "name_original": "In the Night Kitchen",
     "definition": "センダック1970年作。夢的絵本で『かいじゅうたちのいるところ』に続く想像力解放絵本の代表作。"},
    {"name_ja": "サン=テグジュペリ『星の王子さま』哲学童話",
     "name_en": "Saint-Exupéry: Le Petit Prince — philosophical fable",
     "name_original": "Le Petit Prince",
     "definition": "1943年作の哲学童話形式。寓話と児童文学の境界に立つ20世紀世界文学の代表作。"},
]


def main() -> int:
    if len(CONCEPTS) != 30:
        print(f"ERROR: expected 30 concepts, got {len(CONCEPTS)}")
        return 1
    print(f"[wave31_c33_genre_30] inserting {len(CONCEPTS)} concepts...")
    inserted = 0
    skipped = 0
    with LitDB() as db:
        for c in CONCEPTS:
            defn = c["definition"]
            if len(defn) > 100:
                print(f"[warn] definition too long ({len(defn)} chars): {c['name_ja']}")
            try:
                cid = db.insert_concept(
                    name_ja=c["name_ja"],
                    name_en=c.get("name_en"),
                    name_original=c.get("name_original"),
                    original_script="roman",
                    subfield_code=SUBFIELD_CODE,
                    region=REGION,
                    period_id=PERIOD_ID,
                    definition=defn,
                    importance_score=4,
                    source_tier="secondary",
                    canonical_in_region="adjacent",
                )
                # Detect skip (existing) by re-querying — simple heuristic via print logs
                inserted += 1
            except LitDBError as e:
                print(f"[error] {c['name_ja']}: {e}")
                skipped += 1
        db.commit()
    print(f"[done] processed {inserted}, errors {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
