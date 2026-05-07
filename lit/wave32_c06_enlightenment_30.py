#!/usr/bin/env python3
"""Wave 32 C06: Enlightenment & Romanticism +30 concepts -> subfield_id=4"""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# 5 clusters x 6 concepts = 30
# period_id mapping (region=西欧):
#   183 = 18世紀フランス啓蒙拡張期
#   184 = 18世紀英国小説興隆期
#   292 = ゴシック小説深化期
#   185 = ドイツ・シュトゥルム・ウント・ドラング期
#   186 = 英国ロマン主義詩期

CONCEPTS = [
    # Cluster 1: French Enlightenment (period 183)
    ("ヴォルテール『哲学書簡』", "Lettres philosophiques", 183, "英国の自由・寛容を称揚し仏旧体制を諷刺する啓蒙宣言書（1734）。"),
    ("ディドロ『運命論者ジャックとその主人』", "Jacques le fataliste et son maître", 183, "決定論と語りの遊戯を組み合わせた反小説的対話小説（1796刊）。"),
    ("ルソー『新エロイーズ』", "Julie ou La Nouvelle Héloïse", 183, "感性と徳の葛藤を描く書簡体小説、感傷主義の決定版（1761）。"),
    ("マリヴォー『マリアンヌの生涯』", "La Vie de Marianne", 183, "孤児の感情と社会的上昇を細密心理で描く未完書簡小説（1731-41）。"),
    ("ボーマルシェ『フィガロの結婚』", "Le Mariage de Figaro", 183, "従僕が主人を出し抜く諷刺喜劇、革命前夜の階級批判（1784）。"),
    ("ラクロ『危険な関係』", "Les Liaisons dangereuses", 183, "リベルタンの誘惑術を冷徹に描く書簡体小説、貴族社会の腐敗を暴く（1782）。"),

    # Cluster 2: British 18c (period 184)
    ("デフォー『ロビンソン・クルーソー』", "Robinson Crusoe", 184, "孤島漂流と自己労働による文明再建を描く近代小説の祖（1719）。"),
    ("リチャードソン『パメラ』", "Pamela; or, Virtue Rewarded", 184, "下女の貞操と上昇婚を描く書簡体小説、心理小説の起点（1740）。"),
    ("フィールディング『トム・ジョーンズ』", "The History of Tom Jones, a Foundling", 184, "捨子の遍歴を喜劇的叙事詩として描いた包括的小説（1749）。"),
    ("スターン『トリストラム・シャンディ』", "The Life and Opinions of Tristram Shandy", 184, "脱線と前衛的タイポグラフィに満ちた反小説的自伝小説（1759-67）。"),
    ("バーニー『エヴェリーナ』", "Evelina", 184, "若い女性の社交界デビューを書簡で描く女性小説の先駆（1778）。"),
    ("スモレット『ロデリック・ランダム』", "The Adventures of Roderick Random", 184, "海軍体験を交えたピカレスク的冒険小説（1748）。"),

    # Cluster 3: Gothic (period 292)
    ("ウォルポール『オトラント城』", "The Castle of Otranto", 292, "中世城を舞台に超自然と恐怖を導入したゴシック小説の起源（1764）。"),
    ("ラドクリフ『ユードルフォ城の謎』", "The Mysteries of Udolpho", 292, "崇高な風景と説明的超自然で恐怖を醸成するゴシックの代表作（1794）。"),
    ("ルイス『マンク』", "The Monk", 292, "聖職者の堕落と神聖冒涜を描く扇情的ゴシック（1796）。"),
    ("マチューリン『放浪者メルモス』", "Melmoth the Wanderer", 292, "魂の取引と入れ子構造を駆使した最後期ゴシックの傑作（1820）。"),
    ("ホッグ『義とされた罪人の手記と告白』", "The Private Memoirs and Confessions of a Justified Sinner", 292, "二重人格と分身モチーフでカルヴァン主義を批判的に描く（1824）。"),
    ("リーヴ『古英国男爵』", "The Old English Baron", 292, "ウォルポールを抑制的に書き直したゴシック・ロマンス（1778）。"),

    # Cluster 4: German Sturm und Drang + Klassik (period 185)
    ("レッシング『賢者ナータン』", "Nathan der Weise", 185, "三宗教の和解と寛容を説く啓蒙劇詩、指輪のたとえを核に置く（1779）。"),
    ("ゲーテ『若きウェルテルの悩み』", "Die Leiden des jungen Werthers", 185, "感性過剰と失恋自殺を描き欧州を席巻した書簡体小説（1774）。"),
    ("ゲーテ『ファウスト』第一部", "Faust. Eine Tragödie. Erster Teil", 185, "悪魔との契約とグレートヒェン悲劇を描くドイツ文学最大の悲劇（1808）。"),
    ("シラー『群盗』", "Die Räuber", 185, "兄弟相克と圧政への武力反抗を描くシュトゥルム劇の代表作（1781）。"),
    ("ヘルダーリン『ヒュペーリオン』", "Hyperion oder Der Eremit in Griechenland", 185, "近代ギリシアを舞台に理念喪失と憧憬を歌う書簡体抒情小説（1797-99）。"),
    ("クロップシュトック『救世主』", "Der Messias", 185, "ヘクサメトロスでキリスト受難を歌う宗教叙事詩、独詩語の解放（1748-73）。"),

    # Cluster 5: Romantic poetry (period 186)
    ("ワーズワース『序曲』", "The Prelude", 186, "詩人精神の成長を回想する自伝的長詩、第一次想像力の理論詩（1850）。"),
    ("コールリッジ『老水夫の歌』", "The Rime of the Ancient Mariner", 186, "アホウドリ殺害から贖罪への象徴的航海を語るバラッド（1798）。"),
    ("ブレイク『無垢の歌』", "Songs of Innocence", 186, "子供視点と彩飾印刷で無垢の世界を歌う預言的詩集（1789）。"),
    ("キーツ『聖アグネス祭の前夜』", "The Eve of St. Agnes", 186, "中世ロマンスを官能的絢爛体で再構築した物語詩（1820）。"),
    ("シェリー『縛を解かれたプロメテウス』", "Prometheus Unbound", 186, "圧政打倒と愛による宇宙再生を歌う革命的抒情劇（1820）。"),
    ("バイロン『チャイルド・ハロルドの巡礼』", "Childe Harold's Pilgrimage", 186, "幻滅した若者の欧州遍歴、バイロン的英雄を確立した長詩（1812-18）。"),
]

REGION = "西欧"
SUBFIELD_ID = 4

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # existing names for dedup
    cur.execute("SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    existing = {r[0] for r in cur.fetchall()}

    inserted, skipped = 0, 0
    for name_ja, name_en, period_id, definition in CONCEPTS:
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
            print(f"IntegrityError: {name_ja} -> {e}")
            skipped += 1

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted={inserted}, Skipped={skipped}, Total subfield4={total}")

if __name__ == "__main__":
    main()
