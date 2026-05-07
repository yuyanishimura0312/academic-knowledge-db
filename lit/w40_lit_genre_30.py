#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche lit_genre concepts."""

from lit_db_helper import LitDB, LitDBError


CONCEPTS = [
    # 1. 超局地ミステリ
    ("マン島ティンワルド犯罪小説", "Manx Tynwald crime fiction", "Tynwald crime fiction", "latin", "マン島議会制度と島嶼法を謎解きに絡める犯罪小説細分。"),
    ("オークニー考古学ミステリ", "Orkney archaeology mystery", "Orkney archaeology mystery", "latin", "環状列石と島嶼発掘を殺人調査の軸にする北方ミステリ。"),
    ("ヘブリディーズ・クロフター・ノワール", "Hebridean crofter noir", "Hebridean crofter noir", "latin", "小作農地とゲール語共同体の閉塞を描く島嶼ノワール。"),
    ("ラディン語アルプス探偵譚", "Ladin Alpine detective tale", "Ladin Alpine detective tale", "latin", "ドロミーティの少数語共同体を舞台にする山岳探偵小説。"),
    ("カシューブ語湖沼ミステリ", "Kashubian lake mystery", "Kashubian lake mystery", "latin", "ポメラニア湖水地方の言語境界を謎に組み込む犯罪小説。"),
    ("コーンウォール密輸ノワール", "Cornish smuggling noir", "Cornish smuggling noir", "latin", "錫鉱山跡と密輸海岸を暗部化するケルト周縁犯罪小説。"),
    # 2. パルプ冒険の微細形式
    ("エアシップ海賊パルプ", "Airship pirate pulp", "airship pirate pulp", "latin", "飛行船と空賊を海洋冒険の語彙で描く初期パルプ変種。"),
    ("失われた都市女性探検譚", "Lost-city woman explorer tale", "lost-city woman explorer tale", "latin", "女性探検家を前面に出す秘境都市冒険小説の下位型。"),
    ("ラジウム発明少年譚", "Radium boy-inventor tale", "radium boy-inventor tale", "latin", "放射能幻想を少年発明家の活躍へ結びつける初期SF冒険。"),
    ("潜水艦復讐メロドラマ", "Submarine revenge melodrama", "submarine revenge melodrama", "latin", "私設潜水艦と復讐船長を軸にする海洋科学ロマンス。"),
    ("中空地球帝国ロマンス", "Hollow-earth empire romance", "hollow-earth empire romance", "latin", "地底世界の王朝と征服を描く冒険ロマンスの空想地理型。"),
    ("黒蘭ジャングル連載譚", "Black-orchid jungle serial", "black-orchid jungle serial", "latin", "希少植物探索を連載活劇化する熱帯冒険小説の細分。"),
    # 3. 児童出版の忘却ジャンル
    ("鉄道孤児連載物語", "Railway-orphan serial story", "railway-orphan serial story", "latin", "駅・車掌・拾い子を核にする児童雑誌の連載人情譚。"),
    ("寄宿学校暗号クラブ物語", "Boarding-school cipher club story", "boarding-school cipher club story", "latin", "寮内秘密結社と暗号解読を軸にする少年少女学校物語。"),
    ("布人形家庭道徳絵本", "Rag-doll domestic conduct book", "rag-doll conduct book", "latin", "布人形の行儀を通じ家庭徳目を教える幼児向け絵本型。"),
    ("小公女型没落令嬢物語", "Little-princess fallen-heiress tale", "fallen-heiress tale", "latin", "没落した少女の品位と回復を描く感傷的児童小説型。"),
    ("玩具兵隊戦争寓話", "Toy-soldier war fable", "toy-soldier war fable", "latin", "玩具兵隊を通じて戦争と忠誠を寓話化する児童短編。"),
    ("児童禁酒リワードブック", "Juvenile temperance reward book", "temperance reward book", "latin", "禁酒運動の教訓を褒賞本形式で流通させた児童出版ジャンル。"),
    # 4. SF・怪奇の極小サブジャンル
    ("宇宙灯台遭難SF", "Space-lighthouse disaster SF", "space-lighthouse SF", "latin", "宇宙航路の灯台勤務と孤立事故を描く短編SF細分。"),
    ("世代宇宙船法廷SF", "Generation-ship courtroom SF", "generation-ship courtroom SF", "latin", "閉鎖船内の継承法と裁判を扱う世代宇宙船小説型。"),
    ("反重力鉱山惑星ロマンス", "Anti-gravity mine planetary romance", "anti-gravity mine romance", "latin", "異星鉱山と反重力装置を活劇化する惑星ロマンス。"),
    ("月面温室カタストロフ", "Lunar greenhouse catastrophe", "lunar greenhouse catastrophe", "latin", "月面農業施設の崩壊を生態危機として描くSF災害譚。"),
    ("機械仕掛け降霊ホラー", "Clockwork seance horror", "clockwork seance horror", "latin", "自動人形と降霊会を結びつける機械怪奇小説の細分。"),
    ("寄生書物ホラー", "Parasitic book horror", "parasitic book horror", "latin", "読者や蔵書を侵す本そのものを怪物化する書物ホラー。"),
    # 5. ロマンス・家庭大衆小説の極細分類
    ("灯台守ロマンス", "Lighthouse-keeper romance", "lighthouse-keeper romance", "latin", "孤島灯台の監視労働と救難を恋愛の舞台にするロマンス。"),
    ("女性電話交換手ロマンス", "Telephone-operator romance", "telephone-operator romance", "latin", "交換台労働と声の親密性を恋愛定型へ組み込む職業小説。"),
    ("タイプライター娘出世譚", "Typewriter-girl success romance", "typewriter-girl romance", "latin", "事務職女性の技能と恋愛上昇を描く都市大衆ロマンス。"),
    ("戦時看護船ロマンス", "Hospital-ship wartime romance", "hospital-ship romance", "latin", "病院船の看護労働と戦時別離を絡める医療ロマンス。"),
    ("女性薬剤師職業ロマンス", "Woman pharmacist career romance", "pharmacist career romance", "latin", "薬局経営と専門職女性の自立を恋愛筋に重ねる職業ロマンス。"),
    ("村郵便局ハートウォーマー", "Village post-office heartwarmer", "post-office heartwarmer", "latin", "郵便局を縁結びと共同体再生の場にする温情大衆小説。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row[0]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 21"
            )
        }
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if name_ja in existing:
                skipped += 1
                print(f"[skip] exists: {name_ja}")
                continue
            try:
                db.insert_concept(
                    name_ja=name_ja,
                    name_en=name_en,
                    name_original=name_original,
                    original_script=script,
                    subfield_code="lit_genre",
                    region="周縁横断",
                    period_id=None,
                    definition=definition,
                    importance_score=2,
                    source_tier="secondary",
                    canonical_in_region="marginal",
                )
                inserted += 1
            except LitDBError as exc:
                skipped += 1
                print(f"[error] {name_ja}: {exc}")
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
