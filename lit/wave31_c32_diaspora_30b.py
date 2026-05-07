#!/usr/bin/env python3
"""Wave 31 C32b - Add 14 more diaspora concepts to reach 30 net new."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 20
PERIOD_ID = 168
REGION = "ディアスポラ"

EXTRA = [
    # C1 Asian American (Chinese)
    ("マキシン・ホン・キングストン『中国人の男たち』", "Maxine Hong Kingston, China Men",
     "華系米男系移民労働史を物語化した連作、女武者の対をなす作品。"),
    ("エイミー・タン『キッチン・ゴッドの妻』", "Amy Tan, The Kitchen God's Wife",
     "戦中中国を生き延びた母の告白を娘が聞く構造の長篇、世代間沈黙の解凍。"),
    # C2 Korean / Vietnamese
    ("クリス・リー『君が去ったら』", "Krys Lee, How I Became a North Korean",
     "脱北者と韓国系米青年の中朝国境物語、難民倫理を交錯させる長篇。"),
    ("オーシャン・ヴオン『傷ついた夜空』", "Ocean Vuong, Night Sky with Exit Wounds",
     "ヴェトナム系米詩人の処女詩集、戦争・性・父をめぐるエレジー連作。"),
    ("レ・ティ・ジエム・トゥイ『水と土の声』", "Le Thi Diem Thuy, Voices from Water and Earth",
     "ベトナム系米作家の朗読パフォーマンス由来テクスト、難民身体性を演じる。"),
    # C3 South Asian
    ("ジュンパ・ラヒリ『その名にちなんで』再考", "Jhumpa Lahiri, The Namesake (re-reading)",
     "印系米二世のゴーゴリ命名の重荷、移民世代の名と帰属の小説、改訂評価。"),
    ("ヴィクラム・セット『等しい音楽』", "Vikram Seth, An Equal Music",
     "ロンドン弦楽四重奏のヴァイオリニストを語り手とする音楽小説、印系英文学の例外作。"),
    ("モハシン・ハミッド『出口の西』", "Mohsin Hamid, Exit West",
     "難民魔術扉モチーフの寓話的長篇、グローバル移動の倫理と愛。"),
    # C4 Caribbean / Black British
    ("V・S・ナイポール『半生』", "V. S. Naipaul, Half a Life",
     "印系青年の英・アフリカ・ロンドン放浪を描く晩年作、ノーベル受賞前夜。"),
    ("サム・セルヴォン『モーゼ・アセンディング』", "Sam Selvon, Moses Ascending",
     "孤独なロンドン人続篇、トリニダード移民モーゼのロンドン家主転身譚。"),
    ("カリル・フィリップス『最終航路』", "Caryl Phillips, The Final Passage",
     "1950年代カリブ女性のウィンドラッシュ移民を描く処女長篇、希望と失望の年代記。"),
    # C5 Jewish / Translingual
    ("ソール・ベロー『フンボルトの贈り物』", "Saul Bellow, Humboldt's Gift",
     "詩人フンボルトの霊と作家チャーリーを巡る自伝的長篇、ピューリッツァー賞。"),
    ("シンシア・オジック『プトメッサーの諸論集』", "Cynthia Ozick, The Puttermesser Papers",
     "ニューヨーク市職員プトメッサー連作、猶系女性のゴーレム創造譚。"),
    ("テレサ・ハッキョン・チャ『見える者の機械』", "Theresa Hak Kyung Cha, Apparatus",
     "編著の前衛理論アンソロジー、映画装置と視覚の植民地性を批判。"),
]

assert len(EXTRA) == 14
for _, _, d in EXTRA:
    assert len(d) <= 100, (len(d), d)


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, definition in EXTRA:
        try:
            cur.execute(
                """
                INSERT INTO concepts (name_ja, name_en, subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name_ja, name_en, SUBFIELD_ID, REGION, PERIOD_ID, definition, 4),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"skip: {name_ja} ({e})")
    conn.commit()
    total = cur.execute(
        "SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    ).fetchone()[0]
    conn.close()
    print(f"inserted={inserted} skipped={skipped} total_subfield20={total}")


if __name__ == "__main__":
    main()
