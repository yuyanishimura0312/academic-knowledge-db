#!/usr/bin/env python3
"""Wave 44: add 30 ultra-niche lit_genre concepts."""

from lit_db_helper import LitDB


CONCEPTS = [
    # 1. 島嶼・水辺ミステリ
    ("サルデーニャ羊飼いノワール", "Sardinian shepherd noir", "Sardinian shepherd noir", "latin", "牧羊地帯の沈黙と血縁を犯罪劇にする島嶼ノワール。"),
    ("バレアレス洞窟ミステリ", "Balearic cave mystery", "Balearic cave mystery", "latin", "海蝕洞と観光利権を手掛かりにする地中海ミステリ。"),
    ("ヘリゴランド灯台探偵譚", "Heligoland lighthouse detective tale", "Heligoland lighthouse detective tale", "latin", "灯台勤務表と潮汐を謎解きに使う北海探偵譚。"),
    ("アラン島漁網ミステリ", "Aran net-fishing mystery", "Aran net-fishing mystery", "latin", "漁網の結び目と島内噂を証拠化する島嶼犯罪小説。"),
    ("ボーンホルム燻製小屋ノワール", "Bornholm smokehouse noir", "Bornholm smokehouse noir", "latin", "燻製小屋と港町密売を暗部化するバルト海ノワール。"),
    ("カナリア諸島火山探偵譚", "Canary volcanic detective tale", "Canary volcanic detective tale", "latin", "溶岩地形と観測所記録で事件を解く島嶼探偵譚。"),
    # 2. 鉄道・交通大衆小説
    ("寝台車相続ミステリ", "Sleeping-car inheritance mystery", "sleeping-car inheritance mystery", "latin", "寝台車の個室移動と遺言状を軸にする鉄道ミステリ。"),
    ("路面電車車掌ロマンス", "Tram-conductor romance", "tram-conductor romance", "latin", "停留所と乗換券の偶然を恋愛筋にする都市交通ロマンス。"),
    ("駅時計暗号スリラー", "Station-clock cipher thriller", "station-clock cipher thriller", "latin", "駅時計のずれを暗号通信に使う交通スリラー。"),
    ("山岳ケーブルカー遭難譚", "Mountain funicular disaster tale", "mountain funicular disaster tale", "latin", "索道停止と雪崩不安を閉鎖空間化する遭難小説。"),
    ("渡し船時刻表コージー", "Ferry-timetable cozy", "ferry-timetable cozy", "latin", "渡し船の便と港の常連客で謎を解く温和な地域ミステリ。"),
    ("地下鉄忘れ物探偵譚", "Subway lost-property detective tale", "subway lost-property detective tale", "latin", "忘れ物窓口の品物から都市事件をたどる探偵譚。"),
    # 3. 児童・少女雑誌細分
    ("少女養蚕クラブ物語", "Girls' sericulture club story", "girls' sericulture club story", "latin", "養蚕観察と共同作業を成長譚にする少女クラブ小説。"),
    ("少年測量隊リワードブック", "Boy surveyor reward book", "boy surveyor reward book", "latin", "測量実習と勤勉さを褒賞本形式で教える少年教訓譚。"),
    ("児童郵便貯金物語", "Juvenile postal-savings story", "juvenile postal-savings story", "latin", "貯金通帳と倹約を冒険の動機にする児童教育物語。"),
    ("少女顕微鏡クラブ譚", "Girls' microscope club tale", "girls' microscope club tale", "latin", "顕微鏡観察を友情と小事件発見へつなぐ少女雑誌小説。"),
    ("少年鳩時計修理譚", "Boy cuckoo-clock repair tale", "boy cuckoo-clock repair tale", "latin", "時計修理の技能習得を徳目化する少年職業物語。"),
    ("児童海図読み冒険譚", "Juvenile chart-reading adventure", "juvenile chart-reading adventure", "latin", "海図読解と沿岸探検を結びつける教育冒険小説。"),
    # 4. 産業・職業ロマンス
    ("製糖工場ロマンス", "Sugar-factory romance", "sugar-factory romance", "latin", "製糖工程と労務階層を恋愛葛藤に重ねる職業小説。"),
    ("缶詰工場女工出世譚", "Cannery-girl success tale", "cannery-girl success tale", "latin", "缶詰工場の季節労働から自立へ向かう女性出世物語。"),
    ("陶器絵付け職人求婚譚", "Ceramic-painter courtship tale", "ceramic-painter courtship tale", "latin", "絵付け工房の意匠競争を恋愛筋にする職人ロマンス。"),
    ("薬瓶ラベル校正ロマンス", "Medicine-label proofreader romance", "medicine-label proofreader romance", "latin", "薬瓶ラベルの校正ミスが陰謀と恋愛を呼ぶ職業ロマンス。"),
    ("港湾倉庫簿記メロドラマ", "Dock-warehouse ledger melodrama", "dock-warehouse ledger melodrama", "latin", "倉庫帳簿と横領疑惑を情愛劇にする港湾メロドラマ。"),
    ("電話帳編集者求婚譚", "Telephone-directory editor courtship", "telephone-directory editor courtship", "latin", "電話帳編集の名簿作業を出会いの装置にする都市ロマンス。"),
    # 5. 技術怪奇・微細SF
    ("蓄音機遺言怪談", "Phonograph-will ghost tale", "phonograph-will ghost tale", "latin", "蓄音機に残る遺言音声を怪異化する技術怪談。"),
    ("自動販売機ユートピアSF", "Vending-machine utopia SF", "vending-machine utopia SF", "latin", "自販機網が配給と欲望を統治する小規模ユートピアSF。"),
    ("信号塔幻視ホラー", "Signal-tower vision horror", "signal-tower vision horror", "latin", "鉄道信号塔の勤務孤独と幻視を恐怖化する産業ホラー。"),
    ("計算尺宇宙航法SF", "Slide-rule astrogation SF", "slide-rule astrogation SF", "latin", "計算尺による宇宙航法を問題解決の核にする古典SF細分。"),
    ("冷蔵倉庫吸血鬼譚", "Cold-storage vampire tale", "cold-storage vampire tale", "latin", "冷蔵倉庫の温度管理と吸血鬼伝承を結びつける怪奇譚。"),
    ("気球郵便終末譚", "Balloon-mail apocalypse tale", "balloon-mail apocalypse tale", "latin", "気球郵便だけが残る通信崩壊後の終末小説。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            cid = db.insert_concept(
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
            if cid:
                inserted += 1
            else:
                skipped += 1
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
