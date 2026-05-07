#!/usr/bin/env python3
"""Wave 37: Add 30 niche concepts to subfield 18 (lit_russia_slavic)."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")

# 5 thematic clusters x 6 concepts = 30
# period mapping
SILVER = 203   # ロシア銀の時代
SOVIET_MID = 206
SOVIET_LATE = 207
POST_SOV = 208
POLAND = 210
CZECH = 209
SOUTH_SLAV = 211

CONCEPTS = [
    # Cluster 1: 露銀の時代細部
    ("ベールイ『ペテルブルク』脳の遊戯細部", "Bely Petersburg cerebral play",
     SILVER, "ペテルブルクを父子の意識が交錯する脳内劇場として描いた象徴主義長編の細密構造。"),
    ("ソログーブ『小悪魔』ペレドノフ偏執細部", "Sologub Petty Demon Peredonov",
     SILVER, "教師ペレドノフの被害妄想と汚穢幻覚で田舎町の精神腐敗を描いた銀の時代の代表作。"),
    ("レーミゾフ『十字の姉妹』", "Remizov Sisters of the Cross",
     SILVER, "ペテルブルクの安アパートに棲む女たちの受難を口語語りで紡ぐレーミゾフの代表作。"),
    ("ギッピウス『悪魔の人形』", "Gippius Devil's Doll",
     SILVER, "革命前夜のロシア社会を悪魔的人形像で寓意化したギッピウスの宗教哲学的長編。"),
    ("ブリューソフ『火の天使』錬金術構造", "Briusov Fiery Angel alchemy",
     SILVER, "16世紀ドイツを舞台に魔女裁判と錬金術を絡めた歴史象徴主義長編の世界観構造。"),
    ("ベールイ・シンフォニア四作", "Bely four symphonies",
     SILVER, "音楽的構成を散文に持ち込んだベールイ初期の四つの「交響曲」連作実験。"),

    # Cluster 2: 露ソビエト
    ("バーベリ『騎兵隊』ユダヤ性と暴力", "Babel Red Cavalry Jewish violence",
     SOVIET_MID, "コサック部隊に従軍したユダヤ人作家が暴力と抒情の境界で書いた短篇連作の主題構造。"),
    ("プラトーノフ『土台穴』詳論", "Platonov Foundation Pit",
     SOVIET_MID, "全人民住宅の土台を掘り続ける労働者を通じてユートピア思想の不毛を描いた寓話。"),
    ("ブルガーコフ『白衛軍』", "Bulgakov White Guard",
     SOVIET_MID, "1918年キエフのトゥルビン家を中心に内戦下白系将校家族の崩壊を描いた長編。"),
    ("オレーシャ『羨望』カヴァレロフ像", "Olesha Envy Kavalerov",
     SOVIET_MID, "新時代の機能人間に嫉妬する旧世代詩人カヴァレロフを通じソ連的人間像を批評。"),
    ("ゾーシチェンコ風刺短編集", "Zoshchenko satirical stories",
     SOVIET_MID, "共同住宅の小市民を口語スカーズで描き官僚制と日常の歪みを笑ったソ連風刺の白眉。"),
    ("トリーフォノフ『川岸の家』", "Trifonov House on Embankment",
     SOVIET_LATE, "1930年代粛清期に高官子弟が住んだモスクワの邸宅を舞台にした記憶と裏切りの中編。"),

    # Cluster 3: 露反体制・亡命
    ("アフマートヴァ『レクイエム』粛清の母", "Akhmatova Requiem mothers",
     SOVIET_MID, "息子投獄を待つ母たちの列を哀歌に刻んだ粛清期20世紀ロシア詩連作の主題構造。"),
    ("マンデリシュタム『ヴォロネジ・ノート』流刑詩境", "Mandelstam Voronezh exile",
     SOVIET_MID, "流刑地ヴォロネジで書かれ収容所死前の極限詩境を凝縮した晩期詩集の構造。"),
    ("シャラーモフ『コルィマ物語』詳論", "Shalamov Kolyma Tales detailed",
     SOVIET_LATE, "極北収容所の17年経験を乾いた断章で記録した20世紀収容所文学の頂点。"),
    ("ブロツキー『ケープ・コッドの子守唄』", "Brodsky Lullaby of Cape Cod",
     SOVIET_LATE, "亡命後の米東海岸を舞台に帝国と漂泊を瞑想したブロツキー代表的長詩。"),
    ("アクショーノフ『火傷』五重主人公", "Aksyonov Burn five protagonists",
     SOVIET_LATE, "60年代世代の五重に分裂した主人公を多声的に描いた亡命前禁書長編の構造。"),
    ("ヴォイノヴィチ『チョンキン兵士』", "Voinovich Soldier Chonkin",
     SOVIET_LATE, "辺境に取り残された純朴兵チョンキンの冒険でソ連体制を笑い飛ばした長編風刺。"),

    # Cluster 4: ポーランド
    ("ミツキェヴィチ『パン・タデウシュ』13音節構造", "Mickiewicz Pan Tadeusz meter",
     POLAND, "1811年リトアニア貴族抗争を13音節句で詠ったポーランド国民叙事詩の韻律構造。"),
    ("スウォヴァツキ『ベニョフスキ』", "Słowacki Beniowski",
     POLAND, "歴史的冒険家ベニョフスキを題材にポーランド・ロマン派の自我詩学を展開した長詩。"),
    ("ノルヴィト『プロメティジオン』", "Norwid Promethidion",
     POLAND, "労働と美を結ぶ哲学対話詩でノルヴィトが芸術と社会の再統合を構想した代表作。"),
    ("センキェヴィチ『クォ・ヴァディス』詳論", "Sienkiewicz Quo Vadis",
     POLAND, "ネロ帝下のキリスト教徒迫害を歴史小説として再構成しノーベル賞をもたらした大作。"),
    ("イヴァシュキェヴィチ『デメテルの娘』", "Iwaszkiewicz Demeter",
     POLAND, "イヴァシュキェヴィチが古代神話を変奏し田園と喪失を抒情的に綴った中編。"),
    ("ミウォシュ『囚われの魂』四類型", "Miłosz Captive Mind four types",
     POLAND, "全体主義に屈した東欧知識人四類型ケトマンを分析した亡命詩人の道徳哲学的著作。"),

    # Cluster 5: チェコ・南スラブ
    ("フラバル『厳重に監視された列車』", "Hrabal Closely Watched Trains",
     CZECH, "ナチ占領下の田舎駅で青年見習が初体験と破壊工作に至る中編。チェコ新潮流原作。"),
    ("クンデラ『存在の耐えられない軽さ』軽重論", "Kundera Lightness ontology",
     CZECH, "プラハの春と亡命の四人の愛と政治を永劫回帰の軽重ニーチェ的に問う長編構造。"),
    ("ハシェク『シュヴェイク』愚直の風刺", "Hašek Švejk naive satire",
     CZECH, "大戦に駆り出された愚直シュヴェイクの徘徊でハプスブルク帝国を風刺した未完長編構造。"),
    ("アンドリッチ『ドリナの橋』400年構造", "Andrić Bridge Drina 400 years",
     SOUTH_SLAV, "オスマンが架けたヴィシェグラード橋の400年史で南スラヴの民族重層を貫く長編構造。"),
    ("クルレジャ『グレンバイ家』", "Krleža Glembays",
     SOUTH_SLAV, "ザグレブの大ブルジョワ一族グレンバイ家の腐敗を描く戯曲・短編の連作群。"),
    ("ペーキッチ『奇跡の時』", "Pekić Time of Miracles",
     SOUTH_SLAV, "新約聖書の奇跡譚を異端の視点から再記述したペーキッチの神学的歴史小説。"),
]

assert len(CONCEPTS) == 30

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, period_id, definition in CONCEPTS:
        assert len(definition) <= 100, f"def too long ({len(definition)}): {definition}"
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, subfield_id, region, period_id, definition, importance_score)
                   VALUES (?, ?, 18, '東欧・ロシア', ?, ?, 3)""",
                (name_ja, name_en, period_id, definition),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=18")
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Subfield 18 total: {total}")

if __name__ == "__main__":
    main()
