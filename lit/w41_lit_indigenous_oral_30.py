#!/usr/bin/env python3
"""Wave 41: add 30 hyper-niche concepts to lit_indigenous_oral."""

from lit_db_helper import LitDB

SUBFIELD = "lit_indigenous_oral"
REGION = "周縁横断"
P_ORAL = 13
P_RECOVERY = 15

CONCEPTS = [
    # 1. 音声・韻律の微細技法
    ("ナバホ・グリッサンド祈祷句", "Navajo glissando prayer phrase", "glissando prayer", "latin", P_ORAL, "祝詞末尾の滑音で聖なる人物の接近を標示するディネ技法。"),
    ("ホピ・無声化終止式", "Hopi devoiced cadence", "devoiced cadence", "latin", P_ORAL, "儀礼朗唱の終句を息声化し秘匿知を示すホピ声法。"),
    ("ハイダ・声門閉鎖リフレイン", "Haida glottal-stop refrain", "glottal refrain", "latin", P_ORAL, "反復句の声門閉鎖で鴉の変身局面を切るハイダ口演法。"),
    ("ヌナブト・喉音返句", "Nunavut guttural antiphon", "katajjaq response", "latin", P_ORAL, "喉遊びの交替応答を物語導入へ転用するイヌイト技法。"),
    ("ヨルング・鼻音ドローン詞章", "Yolngu nasal drone verse", "nasal drone", "latin", P_ORAL, "マニカイ下声の鼻音持続で祖先軌跡を支える歌法。"),
    ("サーミ・微分音ヨイク輪郭", "Sami microtonal yoik contour", "yoik contour", "latin", P_ORAL, "対象名を避け旋律輪郭で人物や場所を喚起するヨイク技法。"),
    # 2. 地名・移動記憶
    ("ミクマク・石堤地名唱", "Mi'kmaq stone-weir placename chant", "weir chant", "latin", P_ORAL, "魚梁跡の地名列挙で季節移動を記憶するミクマク唱句。"),
    ("ワバナキ・霧港到着句", "Wabanaki fog-harbor arrival formula", "arrival formula", "latin", P_ORAL, "霧中の港名と親族訪問を結びつける到着定型句。"),
    ("トリンギット・潮汐境界口上", "Tlingit tidal-boundary speech", "tidal boundary", "latin", P_ORAL, "満干の境界を氏族領有の証言へ変える海岸口上。"),
    ("クワクワカワク・貝塚系譜列挙", "Kwakwaka'wakw midden genealogy list", "midden list", "latin", P_ORAL, "貝塚名の連鎖で婚姻と居住権を示す系譜列挙。"),
    ("グウィッチン・渡河名リタニー", "Gwich'in river-crossing litany", "crossing litany", "latin", P_ORAL, "渡河点名を順唱しカリブー狩猟道を保持するリタニー。"),
    ("ヤミ・飛魚礁名唱", "Tao flying-fish reef chant", "reef chant", "latin", P_ORAL, "飛魚季の礁名と禁忌を一続きに唱える蘭嶼タオの歌。"),
    # 3. 秘匿・権限・聴取
    ("アランダ・半公開チュリンガ詞章", "Arrernte semi-public churinga verse", "churinga verse", "latin", P_ORAL, "聴取権を段階化し聖物名を伏せる半公開詞章。"),
    ("ピチャンチャチャラ・夜間名伏せ歌", "Pitjantjatjara nocturnal name-avoidance song", "name-avoidance song", "latin", P_ORAL, "死者名回避の夜間発話を旋律で迂回する砂漠歌。"),
    ("ンガリニン・割礼後聴取句", "Ngarinyin post-initiation hearing formula", "hearing formula", "latin", P_ORAL, "通過儀礼後に初めて聞く地名神話の導入定型。"),
    ("マオリ・タプ解除カラキア", "Maori tapu-lifting karakia", "whakanoa karakia", "latin", P_ORAL, "朗唱で禁忌状態を解除し場を日常へ戻すカラキア。"),
    ("サモア・アヴァ杯順序口上", "Samoan ava-cup order speech", "ava order", "latin", P_ORAL, "アヴァ儀礼の杯順で称号序列を声にする口上。"),
    ("トンガ・カヴァ根献辞", "Tongan kava-root dedication", "kava dedication", "latin", P_ORAL, "カヴァ根の授受を王統記憶へ結ぶ短い献辞句。"),
    # 4. 物質媒体・身体記譜
    ("ワンピス紐結び記憶句", "Wampis knot-memory phrase", "knot phrase", "latin", P_ORAL, "結び目の順序を婚姻交渉の発話索引にする記憶句。"),
    ("エンベラ・籠目神話インデックス", "Embera basket-pattern myth index", "basket index", "latin", P_ORAL, "籠目模様を水界精霊譚の参照順にする索引実践。"),
    ("シピボ・ケネ旋律転写", "Shipibo kené melody transcription", "kené melody", "latin", P_ORAL, "幾何文様を治癒歌の旋律進行として読む転写実践。"),
    ("グナ・板絵治療唱導", "Guna board-painting healing prompt", "healing board", "latin", P_ORAL, "板絵の図像順で病因精霊への唱導を組み立てる技法。"),
    ("アイヌ・イクパスイ酒辞符号", "Ainu ikupasuy libation code", "ikupasuy code", "latin", P_ORAL, "捧酒箆の刻線をカムイへの酒辞順序へ結ぶ符号法。"),
    ("ニヴフ・熊檻呼びかけ句", "Nivkh bear-cage address formula", "bear address", "latin", P_ORAL, "熊檻前で客神の耳へ向ける定型呼びかけ句。"),
    # 5. 返還・再演プロトコル
    ("メノミニー蝋管歌返還", "Menominee wax-cylinder song return", "song return", "latin", P_RECOVERY, "蝋管歌を家族権限で聴き直し再歌唱へ戻す返還実践。"),
    ("ホーチャンク長老注釈録音", "Ho-Chunk elder-annotation recording", "elder annotation", "latin", P_RECOVERY, "古録音へ長老注釈を重ね口承文脈を復元する方法。"),
    ("モヒガン埋葬歌アクセス制限", "Mohegan burial-song access restriction", "access restriction", "latin", P_RECOVERY, "埋葬歌録音の聴取範囲を親族規約で限定する手続き。"),
    ("ワイラピリJukurrpaメタデータ", "Warlpiri Jukurrpa metadata", "Jukurrpa metadata", "latin", P_RECOVERY, "夢見物語の性別・場所制限を記録単位へ埋め込む実践。"),
    ("カナカ・カスタム権限タグ", "Kanak custom-authority tag", "custom authority", "latin", P_RECOVERY, "慣習首長の許可範囲をデジタル歌資料へ付すタグ。"),
    ("ユピック仮面写真再命名", "Yup'ik mask-photo renaming", "mask renaming", "latin", P_RECOVERY, "博物館写真の仮面名を共同体語彙で付け直す返還作業。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts WHERE subfield_id = 19")
        }
        dupes = [concept[0] for concept in CONCEPTS if concept[0] in existing]
        if dupes:
            raise SystemExit(f"duplicates: {dupes}")
        for concept in CONCEPTS:
            assert len(concept[5]) <= 100, concept[0]
        for name_ja, name_en, name_original, original_script, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=original_script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 19"
        ).fetchone()["c"]
        print(f"inserted=30 total={total}")


if __name__ == "__main__":
    main()
