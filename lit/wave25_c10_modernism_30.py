#!/usr/bin/env python3
"""Wave 25 - Cluster 10: 30 modernism concepts for lit_eu_modernism (subfield_id=6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 6
PERIOD_ID = 22  # モダニズム期 西欧
REGION = "西欧"

CONCEPTS = [
    # Cluster 1: Joyce Ulysses episodes
    ("ジョイス『ユリシーズ』アイオロス挿話", "Ulysses: Aeolus Episode", "Aeolus", "latin",
     "新聞社を舞台に修辞技法を多用したジョイス『ユリシーズ』第7挿話。"),
    ("ジョイス『ユリシーズ』さまよえる岩々挿話", "Ulysses: Wandering Rocks", "Wandering Rocks", "latin",
     "ダブリン市街19断片を同時並行で描く第10挿話。都市モンタージュの極致。"),
    ("ジョイス『ユリシーズ』ナウシカア挿話", "Ulysses: Nausicaa", "Nausicaa", "latin",
     "海岸の少女ガーティを大衆ロマンス文体で描く第13挿話。視点交替と性。"),
    ("ジョイス『ユリシーズ』太陽神の牛挿話", "Ulysses: Oxen of the Sun", "Oxen of the Sun", "latin",
     "英語文体史をパスティーシュで再現する産科病院場面の第14挿話。"),
    ("ジョイス『ユリシーズ』キルケ挿話", "Ulysses: Circe", "Circe", "latin",
     "夜の街の幻想を演劇形式で展開する第15挿話。無意識の劇化。"),
    ("ジョイス『ユリシーズ』エウマイオス挿話", "Ulysses: Eumaeus", "Eumaeus", "latin",
     "倦怠と陳腐な文体で深夜の御者宿を描く第16挿話。疲労の文体実験。"),

    # Cluster 2: Eliot Pound 補完
    ("エリオット『スウィーニー・アゴニステス』", "Sweeney Agonistes", "Sweeney Agonistes", "latin",
     "ジャズ・リズムを取り入れたエリオットの未完劇詩断片。現代の聖性探求。"),
    ("エリオット『キリスト教社会の理念』", "The Idea of a Christian Society", "The Idea of a Christian Society", "latin",
     "1939年エリオットの社会論。世俗化批判とキリスト教共同体の構想。"),
    ("エリオット『批評の機能』", "The Function of Criticism", "The Function of Criticism", "latin",
     "1923年論文。批評の役割を伝統と秩序の維持として定義した宣言。"),
    ("パウンド『ドラフト・断章』", "Drafts and Fragments", "Drafts and Fragments", "latin",
     "『キャントーズ』最終巻。沈黙と未完を主題とした晩年の断章群。"),
    ("パウンド『読書の手引き』", "ABC of Reading", "ABC of Reading", "latin",
     "1934年。文学読解の基礎を平易に説いたパウンドの教育的批評書。"),
    ("パウンド『ロマンスの精神』", "The Spirit of Romance", "The Spirit of Romance", "latin",
     "1910年。プロヴァンス・伊仏中世詩を論じたパウンド初期比較文学論。"),

    # Cluster 3: Stein Williams Stevens
    ("スタイン『アメリカ人の形成』", "The Making of Americans", "The Making of Americans", "latin",
     "1925年。家族史を反復文体で書き換えるスタインの巨大な散文実験。"),
    ("スタイン『書く方法』", "How to Write", "How to Write", "latin",
     "1931年。文法・センテンス・段落を脱構築するスタインの詩学的論考集。"),
    ("ウィリアムズ『地獄のコラ』", "Kora in Hell", "Kora in Hell: Improvisations", "latin",
     "1920年。即興散文詩の連作。米国モダニズム散文詩の起点的作品。"),
    ("スティーヴンズ『秩序の観念』", "Ideas of Order", "Ideas of Order", "latin",
     "1936年詩集。混沌と秩序の関係を瞑想する後期スティーヴンズへの転換点。"),
    ("スティーヴンズ『青いギターの男』", "The Man with the Blue Guitar", "The Man with the Blue Guitar", "latin",
     "1937年詩集。芸術と現実の関係を変奏する33連の長詩を中心に据えた。"),
    ("スティーヴンズ『必要な天使』", "The Necessary Angel", "The Necessary Angel", "latin",
     "1951年。詩と想像力に関する論集。最高の虚構の理論的基盤書。"),

    # Cluster 4: HD Crane Frost Moore
    ("H.D.『三部作』", "Trilogy", "Trilogy", "latin",
     "1944-46年。戦時ロンドンを舞台とした神話的長詩三部作。女性モダニズム叙事詩。"),
    ("H.D.『エジプトのヘレン』", "Helen in Egypt", "Helen in Egypt", "latin",
     "1961年長詩。ステシコロス系神話を女性視点で再構築したH.D.最後の主著。"),
    ("クレイン『白い建物』", "White Buildings", "White Buildings", "latin",
     "1926年詩集。象徴主義と機械文明を融合させたハート・クレイン第一詩集。"),
    ("フロスト『山あいの間』", "Mountain Interval", "Mountain Interval", "latin",
     "1916年詩集。「選ばれざる道」を含むフロスト中期の代表詩集。"),
    ("フロスト『証人の樹』", "A Witness Tree", "A Witness Tree", "latin",
     "1942年詩集。ピュリッツァー賞受賞。戦時下の自然瞑想と倫理の詩篇。"),
    ("マリアン・ムーア『観察集』", "Observations", "Observations", "latin",
     "1924年詩集。引用と精密観察を組み合わせるムーアの方法を確立した詩集。"),

    # Cluster 5: Continental 補完
    ("アポリネール『カリグラム』", "Calligrammes", "Calligrammes", "latin",
     "1918年詩集。文字配列で図像を作る視覚詩。タイポグラフィ革新の極点。"),
    ("ジッド『田園交響楽』", "La Symphonie pastorale", "La Symphonie pastorale", "latin",
     "1919年中編。盲目の少女と牧師の物語。叙述の偽善を解剖するジッド作品。"),
    ("マン『ヴェニスに死す』", "Death in Venice", "Der Tod in Venedig", "latin",
     "1912年中編。芸術家の崩壊を疫病都市ヴェニスで描く美と頽廃の象徴作。"),
    ("マン『マリオと魔術師』", "Mario and the Magician", "Mario und der Zauberer", "latin",
     "1930年中編。催眠術師を通してファシズム的支配の心理を寓意化した作品。"),
    ("アフマートヴァ『北の哀歌』", "Northern Elegies", "Северные элегии", "cyrillic",
     "1940-64年連作。スターリン時代の生を瞑想する晩年アフマートヴァの哀歌群。"),
    ("マンデリシュターム『ヴォロネジ・ノート』", "Voronezh Notebooks", "Воронежские тетради", "cyrillic",
     "1935-37年流刑地で書かれた最後期詩篇群。死を前にした言語の極限。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for name_ja, name_en, name_orig, script, definition in CONCEPTS:
        assert len(definition) <= 100, f"definition too long ({len(definition)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition,
                 importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 3, 'tier1', 'yes')
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, PERIOD_ID, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
