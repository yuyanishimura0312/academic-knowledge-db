#!/usr/bin/env python3
"""Wave 34 C28: Russian/Slavic niche concepts +30."""
import sqlite3, sys, os

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance)
CONCEPTS = [
    # Cluster 1: Russian詳細 (6)
    ("プーシキン『エヴゲーニイ・オネーギン』第一章", "Pushkin Eugene Onegin Chapter I", "Евгений Онегин Глава 1", "cyrillic", "ロシア・スラヴ", 291,
     "ペテルブルク社交界の貴族青年像。オネーギン・スタンザ4+4+2+2+2押韻形式で叙事と抒情を融合。", 4),
    ("レールモントフ『現代の英雄』ペチョーリン心理", "Lermontov Hero of Our Time Pechorin", "Герой нашего времени", "cyrillic", "ロシア・スラヴ", 291,
     "コーカサスを舞台にした余計な人ペチョーリンの心理小説。5部構成で時系列を解体する近代手法。", 4),
    ("ゴーゴリ『死せる魂』第一巻構造", "Gogol Dead Souls Vol I structure", "Мёртвые души Том I", "cyrillic", "ロシア・スラヴ", 202,
     "チチコフ巡歴で地主類型を提示する叙事的ポエマ。第二巻焼却によりダンテ風三部作未完。", 5),
    ("ゴンチャロフ『オブローモフ』のオブローモフシチナ", "Goncharov Oblomov Oblomovshchina", "Обломов", "cyrillic", "ロシア・スラヴ", 202,
     "貴族の無為怠惰を象徴する文化批評概念。ドブロリューボフが「オブローモフ主義」と命名。", 5),
    ("サルトィコフ＝シチェドリン『ゴロヴリョフ家の人々』", "Saltykov-Shchedrin Golovlyov Family", "Господа Головлёвы", "cyrillic", "ロシア・スラヴ", 202,
     "三代家族の崩壊と偽善ユドゥーシカ像を描く陰惨な貴族没落小説。風刺リアリズムの極北。", 4),
    ("レスコフ『大聖堂の人々』", "Leskov Cathedral Folk", "Соборяне", "cyrillic", "ロシア・スラヴ", 202,
     "地方聖職者の年代記体長編。スカーズ語法で正教文化と民衆精神を描く保守派の代表作。", 4),

    # Cluster 2: Russian Symbolism (6)
    ("ソログーブ『小悪魔』ペレドノフ偏執", "Sologub Petty Demon Peredonov paranoia", "Мелкий бес", "cyrillic", "ロシア・スラヴ", 203,
     "地方教師の被害妄想と偏執を描く象徴主義小説。「ネドティコムカ」幻像で悪の遍在を可視化。", 4),
    ("ベールイ『ペテルブルク』脳遊戯構造", "Bely Petersburg cerebral play", "Петербург", "cyrillic", "ロシア・スラヴ", 203,
     "1905年革命前夜の父子テロル劇。ジョイス以前の意識流とリズム散文で都市黙示録を構築。", 5),
    ("アンネンスキー『糸杉の小箱』詩学", "Annensky Cypress Casket poetics", "Кипарисовый ларец", "cyrillic", "ロシア・スラヴ", 203,
     "死後刊行の絶筆詩集。三連詩集として構成、印象主義的繊細さがアクメイズム母胎となる。", 4),
    ("ヴォローシン詩学とコクテベリ", "Voloshin poetics and Koktebel", "Максимилиан Волошин", "cyrillic", "ロシア・スラヴ", 203,
     "クリミアのコクテベリで芸術家コロニーを主宰。風景詩と歴史詩で内戦期ロシアの悲劇を象徴化。", 3),
    ("ヴャチェスラフ・イワノフ『コル・アルデンス』", "Vyacheslav Ivanov Cor Ardens", "Cor Ardens", "latin", "ロシア・スラヴ", 203,
     "「燃ゆる心」題の二巻詩集。ディオニュソス的合一とソボールノスチを詩化した第二世代象徴主義の頂点。", 4),
    ("ブーニン『暗い並木道』", "Ivan Bunin Dark Avenues", "Тёмные аллеи", "cyrillic", "ロシア・スラヴ", 207,
     "亡命期の38連作短編集。失われた愛と記憶を簡潔な散文で結晶化。ノーベル賞作家円熟の到達点。", 4),

    # Cluster 3: Soviet (6)
    ("バーベリ『騎兵隊』ナラティブ", "Babel Red Cavalry narrative", "Конармия", "cyrillic", "ロシア・スラヴ", 206,
     "ポーランド戦線のコサック従軍記36編。ユダヤ人知識人の語り手と暴力美学が緊張関係を生む。", 4),
    ("オレーシャ『羨望』", "Olesha Envy", "Зависть", "cyrillic", "ロシア・スラヴ", 206,
     "新旧世代対立を風変わりな文体で描く中編。古い感情を持つ知識人カヴァレロフの苦悩を象徴的に呈示。", 4),
    ("プラトーノフ『土台穴』", "Platonov Foundation Pit", "Котлован", "cyrillic", "ロシア・スラヴ", 206,
     "全人類の家のための穴掘り工事を寓話化したディストピア中編。集団化期の言語的逸脱が哲学的深淵となる。", 5),
    ("ブルガーコフ『巨匠とマルガリータ』", "Bulgakov Master and Margarita", "Мастер и Маргарита", "cyrillic", "ロシア・スラヴ", 206,
     "悪魔ヴォランドのモスクワ来訪+ピラト福音+巨匠の小説の三層構造ファンタスマゴリア。タミズダート伝説の頂点。", 5),
    ("ショーロホフ『静かなドン』", "Sholokhov Quiet Don", "Тихий Дон", "cyrillic", "ロシア・スラヴ", 206,
     "コサック村グリゴリーの内戦遍歴を四巻で描くソヴィエト叙事詩。ノーベル賞、著者問題で議論。", 5),
    ("アクショーノフ『クリミア島』", "Aksyonov Island of Crimea", "Остров Крым", "cyrillic", "ロシア・スラヴ", 207,
     "クリミアが島で白衛軍が生き延びた架空史小説。70年代亡命前の異論派代表作で言語遊戯と政治寓話。", 4),

    # Cluster 4: 反体制 (6)
    ("ソルジェニーツィン『収容所群島』三部構成", "Solzhenitsyn Gulag Archipelago", "Архипелаг ГУЛАГ", "cyrillic", "ロシア・スラヴ", 207,
     "227人の証言と自己体験を編んだ「文学的調査」三巻。ソ連強制収容所体制の総体的告発の金字塔。", 5),
    ("シャラーモフ『コルィマ物語』", "Shalamov Kolyma Tales", "Колымские рассказы", "cyrillic", "ロシア・スラヴ", 207,
     "極北ラーゲリの17年体験から書く147短編連作。「新散文」概念で文学化拒絶のドキュメント詩学を提示。", 5),
    ("シニャフスキー『プーシキンとの散歩』", "Sinyavsky Strolls with Pushkin", "Прогулки с Пушкиным", "cyrillic", "ロシア・スラヴ", 207,
     "獄中執筆の脱聖化エッセイ。ロシア国民詩人を軽妙に挑発し、亡命知識人界に大論争を巻き起こした。", 4),
    ("ダニエル＋マルチェンコ『私の証言』", "Daniel Marchenko My Testimony", "Мои показания", "cyrillic", "ロシア・スラヴ", 207,
     "ポスト・スターリン期収容所のサミズダート証言録。ダニエル裁判から続く異論派ドキュメント文学の起点。", 4),
    ("ブロツキー『ヴェニス覚書』", "Brodsky Watermark", "Набережная неисцелимых", "cyrillic", "ロシア・スラヴ", 208,
     "亡命詩人によるヴェニス散文詩。記憶と水と石を巡る瞑想で、ノーベル賞詩人の英語散文の到達点。", 4),
    ("ペトルシェフスカヤ『夜の時間』", "Petrushevskaya Time Night", "Время ночь", "cyrillic", "ロシア・スラヴ", 208,
     "三世代女性の苦難を語る独白中編。ペレストロイカ後リアリズムの女性語りの代表作。", 4),

    # Cluster 5: Slavic (6)
    ("ハシェク『勇敢な兵士シュヴェイク』反戦笑劇", "Hasek Good Soldier Schweik", "Osudy dobrého vojáka Švejka", "latin", "中欧", 209,
     "WWIオーストリア=ハンガリー軍を諷刺する未完4巻長編。愚直シュヴェイクの言語遊戯で権力を解体。", 5),
    ("フラバル『私はイギリス王に給仕した』", "Hrabal I Served King of England", "Obsluhoval jsem anglického krále", "latin", "中欧", 209,
     "20世紀チェコ激動史を給仕ヤン・ジーチェの一人称で語る饒舌長編。ババル「パラベル」語法の傑作。", 4),
    ("センキェヴィチ『クォ・ヴァディス』", "Sienkiewicz Quo Vadis", "Quo vadis", "latin", "中欧", 210,
     "ネロ帝下のキリスト教徒迫害を描く歴史大河。1905年ノーベル賞受賞、世界的ベストセラーとなる。", 5),
    ("シェフチェンコ『コブザール』", "Shevchenko Kobzar", "Кобзар", "cyrillic", "ロシア・スラヴ", 201,
     "ウクライナ詩人画家の詩集。コサック叙事と農民抒情でウクライナ国民文学の礎を築く。", 5),
    ("ヴァーゾフ『軛のもとに』", "Vazov Under the Yoke", "Под игото", "cyrillic", "ロシア・スラヴ", 211,
     "1876年四月蜂起を背景に描くブルガリア初の本格長編小説。国民文学の出発点となる歴史リアリズム。", 4),
    ("アンドリッチ『ドリナの橋』", "Andric Bridge on Drina", "На Дрини ћуприја", "cyrillic", "ロシア・スラヴ", 211,
     "ヴィシェグラード橋を巡る400年のボスニア年代記。1961年ノーベル賞、南スラヴ歴史叙事の頂点。", 5),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for (nj, ne, no, os_, region, pid, defi, imp) in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                                       subfield_id, region, period_id, definition,
                                       importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 18, ?, ?, ?, ?, 'tier1', 'canonical')
            """, (nj, ne, no, os_, region, pid, defi, imp))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {nj} ({e})", file=sys.stderr)
    conn.commit()
    conn.close()
    print(f"INSERTED={inserted} SKIPPED={skipped}")

if __name__ == "__main__":
    main()
