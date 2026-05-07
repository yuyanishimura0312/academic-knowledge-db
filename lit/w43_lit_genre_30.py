#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche lit_genre concepts."""

from lit_db_helper import LitDB


CONCEPTS = [
    # 1. 島嶼・辺境犯罪小説
    ("アゾレス捕鯨ミステリ", "Azorean whaling mystery", "Azorean whaling mystery", "latin", "捕鯨港と移民記憶を捜査線に絡める大西洋島嶼ミステリ。"),
    ("マデイラ崖道ノワール", "Madeira levada noir", "Madeira levada noir", "latin", "灌漑水路と崖道集落の閉塞を犯罪劇にする島嶼ノワール。"),
    ("フェロー郵便船探偵譚", "Faroese mail-boat detective tale", "Faroese mail-boat detective tale", "latin", "離島郵便船の時刻表と乗客網を謎解きに使う探偵譚。"),
    ("ゴットランド石碑ミステリ", "Gotland rune-stone mystery", "Gotland rune-stone mystery", "latin", "ルーン石碑と交易遺跡を手掛かりにするバルト島ミステリ。"),
    ("キクラデス修道院ノワール", "Cycladic monastery noir", "Cycladic monastery noir", "latin", "修道院文書と観光島の利権を暗部化する地中海犯罪小説。"),
    ("済州海女コージー", "Jeju haenyeo cozy mystery", "Jeju haenyeo cozy mystery", "latin", "海女共同体と海産物市場を舞台にする温和な地域ミステリ。"),
    # 2. 印刷・都市職業ロマンス
    ("植字工場ロマンス", "Composing-room romance", "composing-room romance", "latin", "活字組版工場の技能と階級上昇を恋愛筋に重ねる職業小説。"),
    ("貸本屋若旦那メロドラマ", "Rental-library heir melodrama", "rental-library heir melodrama", "latin", "貸本屋後継者と読者共同体を軸にする都市人情メロドラマ。"),
    ("新聞校正係求婚譚", "Proofreader courtship tale", "proofreader courtship tale", "latin", "新聞校正の誤植発見を恋愛の媒介にする職業ロマンス。"),
    ("製本女工出世物語", "Bookbinder-girl success tale", "bookbinder-girl success tale", "latin", "製本工場の女性労働と自立を描く都市大衆小説型。"),
    ("速記者暗号ロマンス", "Stenographer cipher romance", "stenographer cipher romance", "latin", "速記符号と秘書労働を恋愛陰謀に結びつける職業ロマンス。"),
    ("夜間電報配達恋愛譚", "Night-telegram courier romance", "night-telegram courier romance", "latin", "夜間電報配達の偶然と都市不安を恋愛劇化する短編型。"),
    # 3. 児童クラブ・教育小説
    ("少年鉱物採集クラブ譚", "Boy mineral-club story", "boy mineral-club story", "latin", "鉱物採集と地域探検を教育冒険化する少年クラブ物語。"),
    ("少女無線劇団物語", "Girl radio-drama club story", "girl radio-drama club story", "latin", "校内ラジオ劇制作を成長譚にする少女クラブ小説。"),
    ("児童気象日誌物語", "Juvenile weather-diary story", "juvenile weather-diary story", "latin", "毎日の観測記録を事件発見へつなぐ教育的児童物語。"),
    ("模型鉄道探偵クラブ譚", "Model-railway detective club tale", "model-railway detective club tale", "latin", "模型鉄道の配線と時刻表で謎を解く児童探偵クラブ譚。"),
    ("少女手芸通信クラブ譚", "Girls' needlework correspondence club", "needlework correspondence club", "latin", "手芸投稿と文通網を友情形成に使う少女雑誌小説型。"),
    ("少年消防隊リワードブック", "Boy fire-brigade reward book", "boy fire-brigade reward book", "latin", "防火訓練と勇敢さを褒賞本形式で教える児童教訓譚。"),
    # 4. 微細SF・怪奇
    ("気象制御保険SF", "Weather-insurance SF", "weather-insurance SF", "latin", "気象制御事故と保険査定を組み合わせる制度派SF細分。"),
    ("軌道エレベーター労災SF", "Orbital-elevator workplace SF", "orbital-elevator workplace SF", "latin", "軌道エレベーター保守労働と事故責任を描く近未来SF。"),
    ("深海電信ケーブル怪談", "Submarine-cable ghost tale", "submarine-cable ghost tale", "latin", "海底電信線の断線と声の怪異を結びつける技術怪談。"),
    ("菌類図鑑呪物ホラー", "Fungal field-guide cursed-object horror", "fungal guide horror", "latin", "菌類図鑑を呪物化し分類行為を恐怖に変える書物ホラー。"),
    ("自動ピアノ降霊譚", "Player-piano seance tale", "player-piano seance tale", "latin", "自動ピアノの穴紙と霊媒現象を絡める機械怪奇譚。"),
    ("真空列車遭難SF", "Vacuum-train disaster SF", "vacuum-train disaster SF", "latin", "真空チューブ列車の停止事故を閉鎖空間SF化する災害譚。"),
    # 5. 民衆小冊子・露店文芸
    ("縁日見世物小冊子", "Fairground sideshow chapbook", "sideshow chapbook", "latin", "見世物興行の奇譚を安価な小冊子で売る露店文芸型。"),
    ("港町船占いチャップブック", "Harbor fortune chapbook", "harbor fortune chapbook", "latin", "船乗りの航海占いと恋愛予言を売る港町チャップブック。"),
    ("鉱山事故バラッド小冊子", "Mining-disaster ballad pamphlet", "mining-disaster ballad pamphlet", "latin", "鉱山事故を歌謡化し即売した追悼バラッド小冊子。"),
    ("巡礼橋奇跡譚小冊子", "Pilgrim-bridge miracle pamphlet", "pilgrim-bridge miracle pamphlet", "latin", "橋や渡河の奇跡を巡礼土産化する宗教小冊子。"),
    ("市場料理暦物語", "Market-cookery almanac tale", "market-cookery almanac tale", "latin", "料理暦と短い人情話を合わせた市場向け暦物語。"),
    ("行商針売り証言譚", "Peddler needle-seller testimony tale", "needle-seller testimony tale", "latin", "針売り行商の目撃談を怪談や教訓に仕立てる民衆小冊子。"),
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
                continue
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
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
