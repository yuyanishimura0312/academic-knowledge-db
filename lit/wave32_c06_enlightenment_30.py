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
    # Cluster 1: French Enlightenment (period 183) — replacements use distinct works
    ("ヴォルテール『寛容論』", "Traité sur la tolérance", 183, "カラス事件を機に宗教寛容を訴えた啓蒙論争書（1763）。"),
    ("ディドロ『運命論者ジャックとその主人』", "Jacques le fataliste et son maître", 183, "決定論と語りの遊戯を組み合わせた反小説的対話小説（1796刊）。"),
    ("ルソー『社会契約論』", "Du contrat social", 183, "一般意志と人民主権を説き近代政治思想を画した啓蒙古典（1762）。"),
    ("マリヴォー『マリアンヌの生涯』", "La Vie de Marianne", 183, "孤児の感情と社会的上昇を細密心理で描く未完書簡小説（1731-41）。"),
    ("ボーマルシェ『セビリアの理髪師』続編論争", "Querelle du Mariage de Figaro", 183, "『フィガロの結婚』上演をめぐる検閲論争、表現の自由の試金石（1784）。"),
    ("ラクロ『危険な関係』書簡技法", "Technique épistolaire de Laclos", 183, "多重視点書簡の交錯で誘惑と欺瞞を可視化する小説技法（1782）。"),

    # Cluster 2: British 18c (period 184)
    ("デフォー『ロビンソン・クルーソー』植民地読解", "Colonial reading of Crusoe", 184, "孤島労働と他者支配を植民地主義の寓話として読む批評枠組（1719/20c）。"),
    ("リチャードソン『クラリッサ』", "Clarissa, or the History of a Young Lady", 184, "誘拐と陵辱の悲劇を百万語の書簡で描く長大書簡体小説（1748）。"),
    ("フィールディング『ジョセフ・アンドルーズ』", "Joseph Andrews", 184, "リチャードソン『パメラ』をパロディ化したコミック・エピック（1742）。"),
    ("スターン『センチメンタル・ジャーニー』", "A Sentimental Journey Through France and Italy", 184, "感受性の旅日誌で感傷主義を結晶化したスターン晩年作（1768）。"),
    ("バーニー『セシリア』", "Cecilia, or Memoirs of an Heiress", 184, "相続条件と婚姻の葛藤を描き『高慢と偏見』の語句源となる小説（1782）。"),
    ("スモレット『ハンフリー・クリンカー』", "The Expedition of Humphry Clinker", 184, "多視点書簡で英スコットランド旅を描いた書簡体ピカレスク（1771）。"),

    # Cluster 3: Gothic (period 292)
    ("ウォルポール『オトラント城』第二版序文", "Preface to The Castle of Otranto 2nd ed.", 292, "古代と近代ロマンスの融合を宣言したゴシック・ジャンル定義文（1765）。"),
    ("ラドクリフ『ユードルフォの謎』", "The Mysteries of Udolpho", 292, "崇高な風景と説明的超自然で恐怖を醸成するゴシックの代表作（1794）。"),
    ("ルイス『マンク』", "The Monk", 292, "聖職者の堕落と神聖冒涜を描く扇情的ゴシック（1796）。"),
    ("マチューリン『放浪者メルモス』入れ子構造", "Frame narrative in Melmoth", 292, "複数の手稿が連鎖する入れ子物語で時空を貫く誘惑譚を構築（1820）。"),
    ("ホッグ『義とされた罪人の手記と告白』", "Confessions of a Justified Sinner", 292, "二重人格と分身モチーフでカルヴァン主義を批判的に描く（1824）。"),
    ("リーヴ『英国老男爵』ゴシック穏健化", "Domestication of Gothic in The Old English Baron", 292, "超自然を抑制し家庭ロマンスへ穏健化したゴシック改作戦略（1778）。"),

    # Cluster 4: German Sturm und Drang + Klassik (period 185)
    ("レッシング『賢者ナータン』指輪のたとえ", "Ringparabel in Nathan der Weise", 185, "三宗教の真理競争を退け実践による証立てを説く寛容寓話（1779）。"),
    ("ゲーテ『ウェルテル』模倣自殺現象", "Werther-Fieber / copycat suicide", 185, "出版直後に流行した模倣自殺、文学の社会的伝染力の事例（1774-）。"),
    ("ゲーテ『ファウスト』第二部", "Faust. Der Tragödie zweiter Teil", 185, "ヘレナ章と救済を含むゲーテ畢生の象徴劇、近代の総合（1832）。"),
    ("シラー『群盗』", "Die Räuber", 185, "兄弟相克と圧政への武力反抗を描くシュトゥルム劇の代表作（1781）。"),
    ("ヘルダーリン『ヒュペーリオンの運命の歌』", "Hyperions Schicksalslied", 185, "神々と人間の運命を対比した自由韻律の頌歌、内挿詩の頂点（1799）。"),
    ("クロップシュトック『救世主』", "Der Messias", 185, "ヘクサメトロスでキリスト受難を歌う宗教叙事詩、独詩語の解放（1748-73）。"),

    # Cluster 5: Romantic poetry (period 186)
    ("ワーズワース『序曲』", "The Prelude", 186, "詩人精神の成長を回想する自伝的長詩、第一次想像力の理論詩（1850）。"),
    ("コールリッジ『老水夫の歌』象徴解釈", "Symbolic readings of Ancient Mariner", 186, "アホウドリと贖罪をエコロジー・原罪・植民地など多層に読む批評（1798/）。"),
    ("ブレイク『無垢の歌』", "Songs of Innocence", 186, "子供視点と彩飾印刷で無垢の世界を歌う預言的詩集（1789）。"),
    ("キーツ『聖アグネス祭の前夜』", "The Eve of St. Agnes", 186, "中世ロマンスを官能的絢爛体で再構築した物語詩（1820）。"),
    ("シェリー『縛を解かれたプロメテウス』第四幕", "Act IV of Prometheus Unbound", 186, "解放後の宇宙合唱を描く形而上学的詩劇のクライマックス（1820）。"),
    ("バイロン『チャイルド・ハロルドの巡礼』第三歌", "Childe Harold's Pilgrimage Canto III", 186, "ワーテルロー後の自然賛美と歴史省察、バイロン的英雄の深化（1816）。"),
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
