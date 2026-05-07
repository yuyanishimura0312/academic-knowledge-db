#!/usr/bin/env python3
"""Wave 37 cluster 07: postmodern niche - 30 concepts to subfield 7."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")

# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance)
CONCEPTS = [
    # 1: 米ポストモダン細部 (period 124)
    ("ピンチョン『メイスン&ディクスン』読解論", "Pynchon Mason & Dixon Readings", "Mason & Dixon Readings", "latin", "西欧", 124,
     "1997年作の擬古18世紀文体と境界=測量モチーフを脱構築的に読む批評群の総称。", 4),
    ("デリーロ『アンダーワールド』論", "DeLillo Underworld Studies", "Underworld Studies", "latin", "西欧", 124,
     "1997年作の冷戦廃物美学と全体小説性を分析する批評論考の系譜。", 4),
    ("ガス『トンネル』作品論", "William Gass The Tunnel", "The Tunnel", "latin", "西欧", 124,
     "1995年大著。ナチ史家が地下室で穴を掘る26年がかりのモノローグ的言語実験長編。", 4),
    ("ジョン・ホークス『ライム・ツィッグ』", "John Hawkes The Lime Twig", "The Lime Twig", "latin", "西欧", 124,
     "1961年作。戦後ロンドンの競馬詐欺を悪夢的散文で描く反リアリズム犯罪小説。", 4),
    ("クーヴァー『プリックソング集』論", "Coover Pricksongs Readings", "Pricksongs & Descants Readings", "latin", "西欧", 124,
     "1969年短編集の御伽噺解体と聖書再構成を分析するメタフィクション批評群。", 3),
    ("スタンリー・エルキン『マジック・キングダム』", "Stanley Elkin The Magic Kingdom", "The Magic Kingdom", "latin", "西欧", 124,
     "1985年長編。難病児を連れたディズニーランド巡礼を黒い喜劇文体で描く倫理的悲喜劇。", 4),

    # 2: 仏ヌーヴォーロマン以降 (period 124, some 131)
    ("ロブ=グリエ『嫉妬』", "Robbe-Grillet Jalousie", "La Jalousie", "latin", "西欧", 124,
     "1957年長編。ブラインド越しの幾何学的視線描写で物語を消去するヌーヴォーロマン典型作。", 5),
    ("サロート『トロピスム』", "Sarraute Tropismes", "Tropismes", "latin", "西欧", 124,
     "1939年初版・57年改訂の短篇集。会話下の微細心理運動を捉えるヌーヴォーロマン先駆。", 4),
    ("ビュトール『心変わり』", "Butor La Modification", "La Modification", "latin", "西欧", 124,
     "1957年長編。パリ-ローマ列車内の二人称現在形語りで主体決断を解体する形式小説。", 4),
    ("パンジェ『誰か』", "Pinget Quelqu'un", "Quelqu'un", "latin", "西欧", 124,
     "1965年長編。失踪した同居人を回想するモノローグの脱構築で記憶不確定性を提示する。", 3),
    ("クロード・シモン『フランドルへの道』", "Claude Simon La Route des Flandres", "La Route des Flandres", "latin", "西欧", 124,
     "1960年長編。1940年の敗走を断片化記憶で再構築するヌーヴォーロマン代表的歴史小説。", 4),
    ("ウエルベック『素粒子』作品論", "Houellebecq Particules élémentaires", "Les Particules élémentaires", "latin", "西欧", 131,
     "1998年長編。68年世代の解体と性的不能を生物学的決定論で描く論争的ポスト現代小説。", 4),

    # 3: 英国ポストモダン
    ("ラシュディ『悪魔の詩』", "Rushdie The Satanic Verses", "The Satanic Verses", "latin", "西欧", 124,
     "1988年長編。ムハンマド伝の脱構築的並行物語で文化越境とブラスフェミー問題を提起する。", 5),
    ("カーター『血染めの部屋』論", "Carter Bloody Chamber Studies", "Bloody Chamber Studies", "latin", "西欧", 124,
     "1979年作の青ひげ書換とフェミニスト・ゴシック手法を論じる批評研究の総体。", 4),
    ("アクロイド『ホークスムーア』作品論", "Ackroyd Hawksmoor", "Hawksmoor", "latin", "西欧", 124,
     "1985年長編。18世紀建築家と現代刑事の二重時間軸でロンドン暗黒史を交錯させる歴史小説。", 4),
    ("ウィル・セルフ『コック&ブル』", "Will Self Cock & Bull", "Cock & Bull", "latin", "西欧", 124,
     "1992年中編集。性別逆転と身体変容のグロテスクをサテリックに描く英ポストモダン短編。", 3),
    ("ウィル・セルフ『デッド・ライヴ』", "Will Self How the Dead Live", "How the Dead Live", "latin", "西欧", 124,
     "2000年長編。死後ロンドン郊外を彷徨う老女の語りで生死境界をブラックユーモア的に脱構築する。", 3),
    ("マンテル『ウルフ・ホール』", "Mantel Wolf Hall", "Wolf Hall", "latin", "西欧", 131,
     "2009年長編。クロムウェル視点でテューダー朝を現在形描写する新歴史小説三部作の第一作。", 5),

    # 4: 中欧南欧
    ("カルヴィーノ『冬の夜ひとりの旅人が』作品論", "Calvino If on a Winter's Night a Traveler", "Se una notte d'inverno un viaggiatore", "latin", "西欧", 124,
     "1979年長編。読者を二人称主人公とする10未完小説の入れ子で読書行為自体をメタ化する。", 5),
    ("エーコ『フーコーの振り子』作品論", "Eco Foucault's Pendulum", "Il pendolo di Foucault", "latin", "西欧", 124,
     "1988年長編。テンプル騎士団陰謀論を編集者三人が捏造し陰謀に呑まれるパロディック歴史哲学小説。", 4),
    ("クンデラ『冗談』", "Kundera The Joke", "Žert", "latin", "西欧", 124,
     "1967年長編。スターリン時代チェコの一葉書冗談が人生を決壊させる多声的政治小説。", 4),
    ("サラマーゴ『白の闇』作品論", "Saramago Blindness", "Ensaio sobre a cegueira", "latin", "西欧", 124,
     "1995年長編。原因不明の白い盲目流行で社会崩壊を句読点希薄な独自文体で描く寓話的小説。", 5),
    ("マグリス『ドナウ』", "Magris Danube", "Danubio", "latin", "西欧", 124,
     "1986年作。ドナウ川源流から黒海まで遡る紀行=エッセイ=歴史的瞑想を融合させた文学地理学。", 4),
    ("タブッキ『供述によるとペレイラは……』", "Tabucchi Pereira Maintains", "Sostiene Pereira", "latin", "西欧", 124,
     "1994年長編。サラザール独裁下リスボンで老編集者が政治覚醒する『供述』形式の語り。", 4),

    # 5: 独語圏・北欧
    ("ゼーバルト『アウステルリッツ』作品論", "Sebald Austerlitz", "Austerlitz", "latin", "西欧", 124,
     "2001年長編。写真挿入と長文体で東欧出自の建築史家がホロコースト記憶を再発見する作品。", 5),
    ("イェリネク『ピアニスト』", "Jelinek The Piano Teacher", "Die Klavierspielerin", "latin", "西欧", 124,
     "1983年長編。母娘共依存とサディズムを冷徹文体で暴く女性身体のオーストリア批判小説。", 4),
    ("ベルンハルト『ヴィトゲンシュタインの甥』", "Bernhard Wittgenstein's Nephew", "Wittgensteins Neffe", "latin", "西欧", 124,
     "1982年中編。哲学者従兄パウルとの友情を反復的長文で語る自伝的悲喜劇=独白文学。", 4),
    ("ハントケ『幸せではないが、もういい』", "Handke A Sorrow Beyond Dreams", "Wunschloses Unglück", "latin", "西欧", 124,
     "1972年中編。母自殺直後に書いた追悼伝記で女性史と母性を脱センチメンタルに記述する。", 4),
    ("クナウスゴール『我が闘争』作品論", "Knausgård My Struggle", "Min Kamp", "latin", "西欧", 131,
     "2009-11年全6巻。日常細部を執拗に書く北欧オートフィクションで自伝小説形式を再定義する作品。", 5),
    ("ペール・ペッターソン『馬を盗みに』", "Per Petterson Out Stealing Horses", "Ut og stjæle hester", "latin", "西欧", 131,
     "2003年長編。ノルウェー森の老人独居から少年期戦時記憶を遡る抒情的北欧自伝的小説。", 4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        name_ja, name_en, name_orig, script, region, pid, defn, imp = c
        assert len(defn) <= 100, f"definition too long ({len(defn)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, 7, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, region, pid, defn, imp))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {name_ja}: {e}")
            skipped += 1
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=7")
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted={inserted} Skipped={skipped} TotalSF7={total}")

if __name__ == "__main__":
    main()
