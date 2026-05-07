#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_indigenous_oral."""

from lit_db_helper import LitDB

SUBFIELD = "lit_indigenous_oral"
REGION = "周縁横断"
P_ORAL = 13
P_RENAISSANCE = 15

CONCEPTS = [
    # 1. 北米儀礼・物質記憶
    ("ホピ・パーホ祈祷棒語り", "Hopi paho prayer-stick narration", "paho", "latin", P_ORAL, "祈祷棒の奉納手順と神話記憶を結ぶホピ儀礼的語り。"),
    ("ズニ・ココ神謡", "Zuni Koko chant cycle", "Koko", "latin", P_ORAL, "仮面精霊の来訪を歌で組織するズニ儀礼歌群。"),
    ("オジブウェ・ドリームドラム歌", "Ojibwe Dream Drum songs", "bawaajige nagamo", "latin", P_ORAL, "夢告で得た太鼓と歌を共同体治癒へ接続する歌伝承。"),
    ("ラコタ・ワニヤンピ歌", "Lakota vision quest songs", "hanbleceya songs", "latin", P_ORAL, "ヴィジョン探求で授与された個人歌を儀礼化するラコタ歌。"),
    ("カドー・ターキー舞歌", "Caddo Turkey Dance songs", "Turkey Dance", "latin", P_ORAL, "女性列舞の反復句で移動と帰還を記憶するカドー歌。"),
    ("ユロック・跳舞口上", "Yurok Jump Dance speech", "Jump Dance speech", "latin", P_ORAL, "世界更新儀礼で富・水・秩序を呼び戻す北加州口上。"),
    # 2. アマゾン・アンデス細部
    ("デサナ・ミロ転生語り", "Desana miroh narration", "miroh", "latin", P_ORAL, "魚・祖先・星の変換を語るデサナ宇宙論的叙述。"),
    ("ワピシャナ・マウィリ叙述", "Wapishana mawir narration", "mawir", "latin", P_ORAL, "風景名と親族記憶を連結するワピシャナの地名語り。"),
    ("アチュアル・アネント戦歌", "Achuar anent war songs", "anent", "latin", P_ORAL, "敵対と護身を個人呪歌として凝縮するアチュアル歌。"),
    ("マクシ・パイワ物語", "Makushi paiwa tales", "paiwa", "latin", P_ORAL, "滝と岩場の由来を精霊行為へ結ぶマクシ地景譚。"),
    ("カシナワ・ベナキ儀礼歌", "Kaxinawa benaki chants", "benaki", "latin", P_ORAL, "ニシン儀礼の視覚模様と歌句を重ねるフニクイン歌。"),
    ("カリニャ・マウアリ蛇譚", "Kari'na mawari serpent tales", "mawari", "latin", P_ORAL, "水蛇精霊と婚姻禁忌を語るカリニャの川辺伝承。"),
    # 3. オセアニア島嶼系譜
    ("ロツマ・ファクペア歌", "Rotuman fakpeje song", "fakpeje", "latin", P_ORAL, "宴席の応答歌で系譜と島内序列を示すロツマ歌。"),
    ("ヤップ・リフ航海詠唱", "Yapese liw navigation chant", "liw", "latin", P_ORAL, "星・波・島影の知識を短句化するヤップ航海歌。"),
    ("チューク・アーニュ語り", "Chuukese aanu tales", "aanu", "latin", P_ORAL, "精霊との遭遇で礁湖の危険と禁忌を教えるチューク譚。"),
    ("パラオ・デロゲル叙述", "Palauan deloghel narration", "deloghel", "latin", P_ORAL, "首長系譜と土地権を物語化するパラオ伝承叙述。"),
    ("ラパヌイ・パタウタウ詠唱", "Rapa Nui patautau chant", "patautau", "latin", P_ORAL, "祖先名と地名を圧縮列挙するラパヌイ記憶詠唱。"),
    ("カナカ・メレイノア系譜歌", "Kanak melei noa lineage song", "melei noa", "latin", P_ORAL, "氏族移動と山稜名を連ねるカナック系譜歌。"),
    # 4. 北方・シベリア周縁
    ("エヴェンキ・ニムンガカン狩猟譚", "Evenki nimngakan hunting tale", "nimngakan", "latin", P_ORAL, "狩猟霊との交渉を語るエヴェンキ散文伝承。"),
    ("チュクチ・ペリカン変身譚", "Chukchi pelican transformation tale", "pelican tale", "latin", P_ORAL, "海鳥変身で婚姻と海獣狩猟を説明するチュクチ譚。"),
    ("コリャーク・クイクインニャク循環", "Koryak Quikinnaqu cycle", "Quikinnaqu", "latin", P_ORAL, "カラス祖先の失敗と創造を連ねるコリャーク物語群。"),
    ("エネツ・スィト英雄歌", "Enets syudbabts heroic song", "syudbabts", "latin", P_ORAL, "ツンドラ移動と氏族衝突を歌うエネツ英雄的叙述。"),
    ("ドルガン・オロンホ小型叙事", "Dolgan olonkho micro-epic", "olonkho", "latin", P_ORAL, "サハ叙事を北極圏狩猟社会へ移したドルガン歌物語。"),
    ("セルクプ・イルサット呪歌", "Selkup irsat charm song", "irsat", "latin", P_ORAL, "病因精霊を名指しして退けるセルクプ治癒呪歌。"),
    # 5. 現代回復・記録プロトコル
    ("ワンパノアグ言語再生詩", "Wampanoag reclamation poetry", "Wopanaak", "latin", P_RENAISSANCE, "復興語ウォパナークで植民地記憶を詩化する実践。"),
    ("ヌーチャーヌルス音声返還詩学", "Nuu-chah-nulth repatriated audio poetics", "Nuu-chah-nulth", "latin", P_RENAISSANCE, "返還録音を親族的聴取で再活性化する詩学。"),
    ("カウナ・地名再朗読", "Kaurna placename re-voicing", "Kaurna", "latin", P_RENAISSANCE, "都市地名を先住語発音で読み直す南豪の記憶実践。"),
    ("ンガリンジェリ・ルワルディ朗読", "Ngarrindjeri ruwe reading", "ruwe", "latin", P_RENAISSANCE, "水域カントリーを法的証言として朗読するンガリンジェリ表現。"),
    ("サーミ・アーカイブヨイク返唱", "Sami archival yoik re-singing", "joik", "latin", P_RENAISSANCE, "蝋管録音を現代歌唱へ戻すサーミの音声回復実践。"),
    ("アイヌ・デジタルウポポ再演", "Ainu digital upopo reperformance", "upopo", "latin", P_RENAISSANCE, "録音資料と舞台を往復し輪唱歌を再演する現代アイヌ実践。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 19"
            )
        }
        dupes = [c[0] for c in CONCEPTS if c[0] in existing]
        if dupes:
            raise SystemExit(f"duplicates: {dupes}")
        for row in CONCEPTS:
            assert len(row[5]) <= 100, row[0]
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
