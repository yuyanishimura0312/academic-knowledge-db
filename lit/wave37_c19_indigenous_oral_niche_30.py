#!/usr/bin/env python3
"""Wave 37: subfield 19 (lit_indigenous_oral) — 30 niche concepts across 5 clusters."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")

# 5 clusters x 6 concepts = 30
# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance, tier)
CONCEPTS = [
    # Cluster 1: 太平洋オセアニア (period_id=13 先住民口承伝統期 周縁横断)
    ("イヒマエラ『ホエール・ライダー』詳細論", "Witi Ihimaera Whale Rider analysis", "The Whale Rider", "latin", "周縁横断", 13,
     "マオリ女性継承を描くイヒマエラの代表作。鯨乗り神話と現代女性主権を接合した先住民再話。", 4, "tier1"),
    ("グレイス『ポティキ』土地闘争小説", "Patricia Grace Potiki land struggle", "Potiki", "latin", "周縁横断", 13,
     "マオリ共同体の土地開発抵抗を描くグレイス1986年作。語り手交代と神話的時間の融合。", 4, "tier1"),
    ("ハルメ『骨の人々』神話再構築", "Keri Hulme Bone People myth", "the bone people", "latin", "周縁横断", 13,
     "マオリ・パケハ混血の三人を巡るハルメ1984年ブッカー賞作。神話再構築と沈黙の詩学。", 4, "tier1"),
    ("ウェンド『バニヤンの葉』サモア叙事", "Albert Wendt Leaves of the Banyan Tree", "Leaves of the Banyan Tree", "latin", "周縁横断", 13,
     "ウェンドのサモア三世代叙事詩小説。植民地化と伝統の衝突を家族史で描く太平洋文学基礎。", 4, "tier1"),
    ("フィギエル『私たちがかつて居た場所』詳論", "Sia Figiel Where We Once Belonged", "Where We Once Belonged", "latin", "周縁横断", 13,
     "サモア少女視点の集合的語り。ファガオゴ口承形式を小説化し女性身体と村落規範を問う。", 4, "tier1"),
    ("ハウオファ『ティコンの語り』風刺集", "Epeli Hau'ofa Tales of the Tikongs", "Tales of the Tikongs", "latin", "周縁横断", 13,
     "トンガのハウオファ短篇集。援助と開発を風刺し『島々の海』の汎太平洋アイデンティティを準備。", 4, "tier1"),

    # Cluster 2: 北米先住民詩 (period_id=15 先住民文芸復興期 周縁横断)
    ("ハージョ『彼女は何頭かの馬を持っていた』詩集", "Joy Harjo She Had Some Horses", "She Had Some Horses", "latin", "周縁横断", 15,
     "マスコギー族ハージョ1983年詩集。馬の連祷で女性魂と先住民再生を呼び起こす儀礼詩。", 4, "tier1"),
    ("オルティス『雨が来る』詩集", "Simon Ortiz Going for the Rain", "Going for the Rain", "latin", "周縁横断", 15,
     "アコマ・プエブロ詩人オルティス1976年詩集。旅と雨乞い儀礼で先住民連続性を歌う。", 4, "tier1"),
    ("ホーガン『ソーラー・ストームズ』環境小説", "Linda Hogan Solar Storms", "Solar Storms", "latin", "周縁横断", 15,
     "チカソー族ホーガン1995年作。ダム建設に抗する先住民女性世代の癒しと土地神聖性。", 4, "tier1"),
    ("アレクシー『ローン・レンジャーとトント』短篇", "Sherman Alexie Lone Ranger and Tonto", "Lone Ranger and Tonto Fistfight", "latin", "周縁横断", 15,
     "スポケーン・コーダレーン族アレクシー1993年短篇集。保留地生活の絶望と諧謔を描く。", 4, "tier1"),
    ("アードリック『疫病の鳩』裁判小説", "Louise Erdrich Plague of Doves", "The Plague of Doves", "latin", "周縁横断", 15,
     "オジブウェ族アードリック2008年作。先住民冤罪と入植者の罪責の世代連鎖を多声で描く。", 4, "tier1"),
    ("ウェルチ『フールズ・クロウ』詳細論", "James Welch Fools Crow", "Fools Crow", "latin", "周縁横断", 15,
     "ブラックフット族ウェルチ1986年作。1860年代の若者の眼でブラックフット世界を内側から再構築。", 4, "tier1"),

    # Cluster 3: 中南米先住民 (period_id=231 先住民口承・現代インディヘナ ラテンアメリカ)
    ("ポポル・ヴフ詳細論", "Popol Vuh detailed", "Popol Wuj", "latin", "ラテンアメリカ", 231,
     "キチェ・マヤ創世神話。双子英雄フンアフプー兄弟の冥界下降と人類創成を語る基礎テクスト。", 5, "tier1"),
    ("カンタレス・メヒカノス", "Cantares Mexicanos", "Cantares Mexicanos", "latin", "ラテンアメリカ", 231,
     "16世紀ナワトル詩集。テスココのネサワルコヨトル王ら華の歌(xochicuicatl)を保存する基礎史料。", 5, "tier1"),
    ("チワイラフ『青い夢』マプチェ詩", "Elicura Chihuailaf Sueño Azul", "Sueño Azul", "latin", "ラテンアメリカ", 231,
     "マプチェ詩人チワイラフのバイリンガル詩。ウィノル(青い夢)の祖母伝承を現代詩に翻案。", 4, "tier1"),
    ("ワロチリ写本", "Huarochirí Manuscript", "Runa yndio ñiscap machoncuna", "latin", "ラテンアメリカ", 231,
     "16世紀末ケチュア語ワカ神話集。アンデス山岳神々の起源譚を植民地期に書記化した唯一の文書。", 5, "tier1"),
    ("ニャンデ・レコ", "Ñande Reko", "Ñande Reko", "latin", "ラテンアメリカ", 231,
     "グアラニー族の存在様式概念。土地・親族・善き生(teko porã)を一体化した口承倫理体系。", 4, "tier1"),
    ("シマンカ『恥の手紙』ワユー", "Estercilia Simanca Manifiesta", "Manifiesta no saber firmar", "latin", "ラテンアメリカ", 231,
     "コロンビア・ワユー族シマンカの代表作。先住民投票偽装を告発する短篇で口承詩学を散文化。", 4, "tier1"),

    # Cluster 4: アイヌ・ウィルタ・東北亜先住民 (period_id=13 先住民口承伝統期)
    ("ユーカラ詳細論", "Yukar epic detailed", "ユカㇻ", "kana", "周縁横断", 13,
     "アイヌ叙事詩。サケヘ反復句で英雄神(ヤイレスポ)の自伝を一人称で謡う長編口承文芸。", 5, "tier1"),
    ("カムイユカㇻ詳細", "Kamuy Yukar detailed", "カムイユカㇻ", "kana", "周縁横断", 13,
     "アイヌ神謡。動植物カムイ自身が語る短い反復歌で、知里幸恵『アイヌ神謡集』に集成された。", 5, "tier1"),
    ("ウィルタ・ヌプリ語り", "Uilta Nupuri narrative", "Нупури", "cyrillic", "周縁横断", 13,
     "サハリン・ウィルタ(オロッコ)族の山(ヌプリ)を中心とする口承譚。トナカイ遊牧民の世界観伝承。", 3, "tier2"),
    ("サハ・オロンホ叙事詩", "Sakha Olonkho", "Олоҥхо", "cyrillic", "周縁横断", 13,
     "ヤクート族の長大英雄叙事詩。ニュルグン・ボートゥル等の上界英雄を歌うUNESCO無形遺産。", 4, "tier1"),
    ("ナナイ・ニムガカン", "Nanai Nimngakan", "Нимӈакан", "cyrillic", "周縁横断", 13,
     "アムール川流域ナナイ族の散文神話。シャマンの宇宙旅行と動物変身譚を伝える口承伝統。", 3, "tier2"),
    ("ニヴフ氏族系譜詠唱", "Nivkh clan genealogy", "тылгур", "cyrillic", "周縁横断", 13,
     "サハリン・ニヴフ(ギリヤーク)族の氏族系譜詠唱(tylgur)。熊送りに連動する起源神話。", 3, "tier2"),

    # Cluster 5: 口承詩学・パフォーマンス研究 (period_id=15 先住民文芸復興期 周縁横断)
    ("ロード『歌の歌い手』詳細論", "Albert Lord Singer of Tales", "The Singer of Tales", "latin", "周縁横断", 15,
     "ロード1960年著。パリーのフィールドからユーゴ歌手の口頭定型作詩理論を体系化した古典。", 5, "tier1"),
    ("パリー口頭定型句理論", "Milman Parry oral-formulaic", "oral-formulaic theory", "latin", "周縁横断", 15,
     "パリー1928-35年。ホメロス叙事詩の定型句がスラヴ口承歌手と同型の即興技術であると論証。", 5, "tier1"),
    ("フィネガン『口承詩』比較研究", "Ruth Finnegan Oral Poetry", "Oral Poetry", "latin", "周縁横断", 15,
     "フィネガン1977年著。アフリカ・太平洋・北極の口承詩を横断比較し書記/口承二分法を解体。", 4, "tier1"),
    ("ハイムズ・エスノポエティクス詳細", "Dell Hymes ethnopoetics detailed", "ethnopoetics", "latin", "周縁横断", 15,
     "ハイムズの先住民語りを詩行・連で再分節する手法。散文化された記録の韻律構造を回復。", 5, "tier1"),
    ("テッドロック翻訳詩学", "Dennis Tedlock translation poetics", "Finding the Center", "latin", "周縁横断", 15,
     "テッドロック『中心を見出す』。ズニ語りを息と声量で再翻訳しパフォーマンス次元を可視化。", 4, "tier1"),
    ("バウマン上演理論", "Richard Bauman performance theory", "Verbal Art as Performance", "latin", "周縁横断", 15,
     "バウマン1977年著。口承を上演キーイングの枠組みで分析し民俗学に演者責任の概念を導入。", 5, "tier1"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        name_ja, name_en, name_orig, script, region, pid, defn, imp, tier = c
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
                 definition, importance_score, source_tier)
                VALUES (?, ?, ?, ?, 19, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, region, pid, defn, imp, tier))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} -> {e}")
    conn.commit()
    print(f"Wave 37 c19 niche: inserted={inserted}, skipped={skipped}, total={len(CONCEPTS)}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=19")
    print(f"subfield_id=19 total now: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
