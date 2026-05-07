#!/usr/bin/env python3
"""Wave 42: add 30 ultra-niche concepts to lit_indigenous_oral."""

from lit_db_helper import LitDB

SUBFIELD = "lit_indigenous_oral"
REGION = "周縁横断"
P_ORAL = 13
P_RECOVERY = 15

CONCEPTS = [
    # 1. 音声・韻律の極小技法
    ("ミウォク・息継ぎ熊歌句", "Miwok breath-marked bear-song phrase", "bear-song breath phrase", "latin", P_ORAL, "熊歌の息継ぎ位置で変身局面を示すミウォク唱法。"),
    ("ユロック・歯擦音跳舞句", "Yurok sibilant jump-dance phrase", "jump-dance sibilant", "latin", P_ORAL, "跳舞口上の歯擦音反復で霊的緊張を高める句法。"),
    ("チマクム・落声名指し句", "Chemakum falling-tone naming phrase", "falling-tone name phrase", "latin", P_ORAL, "末尾下降調で故人名の近接をぼかす名指し回避句。"),
    ("カリブー・イヌイト鼻息拍", "Caribou Inuit breath-pulse beat", "breath pulse", "latin", P_ORAL, "狩猟歌の鼻息拍で橇移動と獲物接近を刻む声法。"),
    ("カユーガ・弱拍弔歌リフレイン", "Cayuga offbeat condolence refrain", "offbeat refrain", "latin", P_ORAL, "弔慰儀礼の弱拍反復で喪失と再統合を標示する句。"),
    ("セリ・潮声母音延長", "Seri tide-voice vowel lengthening", "tide vowel", "latin", P_ORAL, "潮待ち歌で母音を伸ばし海況判断を声に残す技法。"),
    # 2. 地名・道筋・季節記憶
    ("クリー・ムース湿地名唱", "Cree moose-marsh placename chant", "moose-marsh chant", "latin", P_ORAL, "湿地名の連唱でヘラジカ猟期の移動路を記憶する歌。"),
    ("クテナイ・峠越え到着句", "Ktunaxa pass-crossing arrival formula", "pass formula", "latin", P_ORAL, "峠名と婚姻訪問を結びつけるクテナイ到着定型。"),
    ("オオダム・サワロ水場リタニー", "O'odham saguaro-water litany", "saguaro litany", "latin", P_ORAL, "サワロ果と水場名を雨乞い暦へ接続する列挙句。"),
    ("ララムリ・崖道走行歌", "Raramuri canyon-run song", "canyon-run song", "latin", P_ORAL, "崖道の曲がり名を長距離走の拍へ刻む地名歌。"),
    ("セネカ・泉名感謝口上", "Seneca spring-name thanksgiving speech", "spring-name speech", "latin", P_ORAL, "泉名を感謝祭の供物順へ組み込む短い口上。"),
    ("チュマシュ・島渡り星名句", "Chumash island-crossing star phrase", "star-crossing phrase", "latin", P_ORAL, "星名と島影を対応させ海上移動を導く記憶句。"),
    # 3. 秘匿・資格・儀礼権限
    ("カドー・火床名伏せ口上", "Caddo hearth-name avoidance speech", "hearth avoidance", "latin", P_ORAL, "儀礼火床の名を親族称号で迂回する秘匿口上。"),
    ("ズニ・雨司祭聴取順", "Zuni rain-priest hearing order", "hearing order", "latin", P_ORAL, "雨司祭だけが段階的に聞く神謡配列の規則。"),
    ("メスカレロ・成人名迂回歌", "Mescalero puberty-name avoidance song", "puberty avoidance song", "latin", P_ORAL, "成人儀礼中の名呼びを旋律語で避けるアパッチ歌。"),
    ("タナナ・狩場沈黙句", "Tanana hunting-ground silence formula", "silence formula", "latin", P_ORAL, "狩場境界で発話を止める合図を含む短い定型句。"),
    ("ワラオ・精霊笛禁名句", "Warao spirit-flute taboo-name phrase", "flute taboo phrase", "latin", P_ORAL, "精霊笛の名を水路比喩で置換する禁名句。"),
    ("ヤグア・夜猟耳打ち神話", "Yagua night-hunt whispered myth", "whispered myth", "latin", P_ORAL, "夜猟中だけ小声で語る獲物精霊への短い神話。"),
    # 4. 物質媒体・図像索引
    ("ホピ・綿紐暦歌索引", "Hopi cotton-string calendar song index", "cotton-string index", "latin", P_ORAL, "綿紐の結び順を儀礼暦歌の記憶索引にする方法。"),
    ("マカ・銛線系譜唱", "Makah harpoon-line genealogy chant", "harpoon genealogy", "latin", P_ORAL, "銛線の巻き順で捕鯨家系を唱える系譜記憶法。"),
    ("パイユート・籠縁星図歌", "Paiute basket-rim star-map song", "basket star song", "latin", P_ORAL, "籠縁模様を季節星座の歌順へ対応させる実践。"),
    ("ティクナ・仮面彩色名簿", "Tikuna mask-paint name register", "mask-paint register", "latin", P_ORAL, "仮面彩色の順で氏族名と精霊名を呼び出す索引。"),
    ("エセエハ・羽冠鳥名唱", "Ese Eja feather-crown bird-name chant", "bird-name chant", "latin", P_ORAL, "羽冠の羽列を森の鳥名唱へ変換する記憶技法。"),
    ("カリナ・櫂刻み航路句", "Kalina paddle-notch route phrase", "paddle-notch route", "latin", P_ORAL, "櫂の刻み目を河川航路の短句順へ結ぶ方法。"),
    # 5. 録音返還・再演プロトコル
    ("タギシュ蝋管笑話返唱", "Tagish wax-cylinder joke retelling", "joke retelling", "latin", P_RECOVERY, "蝋管笑話を家族語彙で聞き直し再話する返還実践。"),
    ("トゥスカローラ賛歌譜再口承化", "Tuscarora hymn-sheet reoralization", "hymn reoralization", "latin", P_RECOVERY, "賛歌譜面を長老発音で歌へ戻す再口承化作業。"),
    ("オナイダ蝋盤弔辞アクセス票", "Oneida wax-disc condolence access tag", "access tag", "latin", P_RECOVERY, "弔辞録音の聴取資格を親族票で管理するタグ。"),
    ("イヌヴィアルイト狩猟歌字幕監修", "Inuvialuit hunting-song subtitle review", "subtitle review", "latin", P_RECOVERY, "狩猟歌映像の字幕語彙を共同体が監修する手続き。"),
    ("ヤキ語ミサ歌再命名", "Yaqui mission-song renaming", "song renaming", "latin", P_RECOVERY, "ミサ歌録音をヤキ語の儀礼名で付け直す返還作業。"),
    ("マプチェ・ピフィルカ録音権限札", "Mapuche pifilka recording authority tag", "authority tag", "latin", P_RECOVERY, "ピフィルカ録音に再演許可範囲を付す権限タグ。"),
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
