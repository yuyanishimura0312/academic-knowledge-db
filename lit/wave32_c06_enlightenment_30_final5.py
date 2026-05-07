#!/usr/bin/env python3
"""Wave 32 C06 final-5: top up to reach +30 net new concepts in subfield 4."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# Five extra concepts, one per cluster, distinct from existing names.
EXTRA = [
    # C1 French
    ("ヴォルテール『寛容論』", "Traité sur la tolérance", 183,
     "カラス事件を機に宗教寛容を訴えた啓蒙論争書（1763）。"),
    # C2 British
    ("リチャードソン『クラリッサ』語りの密度", "Narrative density in Clarissa", 184,
     "百万語規模の書簡で日常時間を細密に分節化する近代心理小説の極致（1748）。"),
    # C3 Gothic
    ("ルイス『マンク』神聖冒涜論争", "Blasphemy controversy of The Monk", 184,
     "出版直後の検閲・改稿論争、ゴシックと宗教的タブーの境界事例（1796-）。"),
    # C4 German
    ("シラー『群盗』反逆と兄弟相克", "Revolt and fratricide in Die Räuber", 185,
     "圧政への武力反抗と兄弟葛藤を結合したシュトゥルム劇のテーマ核（1781）。"),
    # C5 Romantic
    ("ブレイク『経験の歌』", "Songs of Experience", 186,
     "『無垢の歌』と対をなす詩集、抑圧と虎の象徴で経験の暗部を歌う（1794）。"),
]
SUBFIELD_ID = 4
REGION = "西欧"

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    existing = {r[0] for r in cur.fetchall()}
    inserted, skipped = 0, 0
    for name_ja, name_en, period_id, definition in EXTRA:
        if name_ja in existing:
            print(f"SKIP duplicate: {name_ja}")
            skipped += 1
            continue
        assert len(definition) <= 100, f"DEF too long ({len(definition)}): {name_ja}"
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (name_ja, name_en, SUBFIELD_ID, REGION, period_id, definition,
                 4, "tier1", "yes"),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"IntegrityError {name_ja}: {e}")
            skipped += 1
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted={inserted}, Skipped={skipped}, Total subfield4={total}")

if __name__ == "__main__":
    main()
