#!/usr/bin/env python3
"""Wave 37 C08: lit_eu_realism niche concepts (30 items, 5 clusters x 6).

Adds detail-level concepts to subfield 5 (lit_eu_realism). Avoids duplicates
already present in DB by selecting alternative niche works/aspects from the
same authors when canonical titles already exist.
"""
import sqlite3
from pathlib import Path

DB = Path("/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite")
SUBFIELD_ID = 5
REGION = "西欧"
P_REALISM = 123       # リアリズム理論成熟期
P_NATURALISM = 122    # 自然主義期
P_FR = 120            # 19世紀フランス・リアリズム期
P_EN = 121            # 19世紀英米・北欧リアリズム期
P_RU = 170            # ロシア・リアリズム期
P_DE = 173            # ドイツ詩的リアリズム期
P_IT = 171            # イタリア・ヴェリズモ期
P_ES = 172            # イベリア・リアリズム期

# (name_ja, name_en, name_original, original_script, period_id, definition, importance, canonical, fourth)
ROWS = [
    # ===== Cluster 1: 仏小説詳細 (6) =====
    ("バルザック『ゴリオ爺さん』詳論", "Balzac, Père Goriot (close reading)", "Le Père Goriot", "latin", P_FR,
     "父性と社会上昇野心の交錯を描く『人間喜劇』の中核小説に対する人物配置と語りの分析。", 4, "high", "partial"),
    ("バルザック『ウジェニー・グランデ』守銭奴像", "Balzac, Eugénie Grandet (miser figure)", "Eugénie Grandet", "latin", P_FR,
     "守銭奴グランデと娘ウジェニーの対比により貨幣・愛・宗教の交差を典型化した人物造形。", 4, "high", "partial"),
    ("バルザック『従妹ベット』復讐譚", "Balzac, La Cousine Bette (revenge plot)", "La Cousine Bette", "latin", P_FR,
     "嫉妬と復讐を駆動因に第二帝政期パリの腐敗を解剖する後期『人間喜劇』の代表作。", 4, "high", "partial"),
    ("スタンダール『赤と黒』野心と仮面", "Stendhal, Le Rouge et le Noir (ambition)", "Le Rouge et le Noir", "latin", P_FR,
     "ジュリアン・ソレルの上昇野心と内面独白を通じ王政復古期社会を描く心理リアリズムの古典。", 5, "high", "partial"),
    ("フローベール『ボヴァリー夫人』倦怠の詩学", "Flaubert, Madame Bovary (poetics of ennui)", "Madame Bovary", "latin", P_FR,
     "地方ブルジョワ妻の幻想と倦怠を非個人的文体で描き近代小説の出発点とされる作品。", 5, "high", "rethinking"),
    ("フローベール『感情教育』失敗の小説", "Flaubert, L'Éducation sentimentale", "L'Éducation sentimentale", "latin", P_FR,
     "1848年革命を背景にフレデリックの恋と志の挫折を描く反成長小説的な世代史小説。", 5, "high", "partial"),

    # ===== Cluster 2: 英ヴィクトリア (6) =====
    ("ディケンズ『大いなる遺産』成長譚", "Dickens, Great Expectations", "Great Expectations", "latin", P_EN,
     "孤児ピップの紳士願望と幻滅を一人称で語る、階級と良心を主題とする後期代表作。", 5, "high", "invariant"),
    ("ディケンズ『荒涼館』裁判批判", "Dickens, Bleak House (Chancery)", "Bleak House", "latin", P_EN,
     "ジャンディス訴訟を通じ衡平法裁判所の官僚的腐敗と都市の霧を批判する社会小説。", 5, "high", "partial"),
    ("エリオット『ミドルマーチ』地方社会研究", "Eliot, Middlemarch (provincial study)", "Middlemarch", "latin", P_EN,
     "1830年代地方都市を舞台に複数主人公の倫理的選択を緻密に追う多声的全体小説。", 5, "high", "rethinking"),
    ("ハーディ『テス』犠牲のヒロイン", "Hardy, Tess of the d'Urbervilles", "Tess of the d'Urbervilles", "latin", P_NATURALISM,
     "純朴な農民娘テスを社会道徳と運命が破滅へ導く悲劇的自然主義小説。", 5, "high", "rethinking"),
    ("ハーディ『日陰者ジュード』結婚批判", "Hardy, Jude the Obscure", "Jude the Obscure", "latin", P_NATURALISM,
     "学問と結婚の双方で挫折するジュードを通じ階級制度と婚姻制度を批判する晩期作品。", 4, "high", "rethinking"),
    ("トロロップ『バーチェスターの塔』教会小説", "Trollope, Barchester Towers", "Barchester Towers", "latin", P_EN,
     "架空の聖堂都市バーチェスターを舞台とする教会派閥抗争を諷刺的に描く連作の第二作。", 4, "high", "invariant"),

    # ===== Cluster 3: 露小説 (6) =====
    ("ドストエフスキー『罪と罰』良心の劇", "Dostoevsky, Crime and Punishment", "Преступление и наказание", "cyrillic", P_RU,
     "ラスコーリニコフの殺人と贖罪を通じ非凡人理論と良心を問うポリフォニー小説の起点。", 5, "high", "rethinking"),
    ("ドストエフスキー『カラマーゾフの兄弟』神義論", "Dostoevsky, The Brothers Karamazov", "Братья Карамазовы", "cyrillic", P_RU,
     "父殺しを軸に三兄弟の信仰・理性・情念を対峙させる宗教的・哲学的最終長編。", 5, "high", "rethinking"),
    ("トルストイ『アンナ・カレーニナ』姦通悲劇", "Tolstoy, Anna Karenina", "Анна Каренина", "cyrillic", P_RU,
     "アンナの不倫破滅とリョーヴィンの農村模索を並行させる二重プロット構造の長編。", 5, "high", "rethinking"),
    ("トルストイ『戦争と平和』歴史哲学小説", "Tolstoy, War and Peace", "Война и мир", "cyrillic", P_RU,
     "ナポレオン戦争を背景に貴族五家族と歴史哲学的考察を融合した叙事詩的全体小説。", 5, "high", "invariant"),
    ("ツルゲーネフ『父と子』ニヒリズム像", "Turgenev, Fathers and Sons", "Отцы и дети", "cyrillic", P_RU,
     "バザーロフを通じ1860年代ロシアのニヒリズムと世代対立を提示した同時代社会小説。", 5, "high", "partial"),
    ("チェーホフ『桜の園』喪失の喜劇", "Chekhov, The Cherry Orchard", "Вишнёвый сад", "cyrillic", P_RU,
     "没落貴族家の桜の園売却を四幕で描き旧体制終焉と新興階層を象徴する晩期戯曲。", 5, "high", "partial"),

    # ===== Cluster 4: 米英自然主義 (6) =====
    ("ハウエルズ『サイラス・ラパムの立身』", "Howells, The Rise of Silas Lapham", "The Rise of Silas Lapham", "latin", P_EN,
     "新興実業家サイラスの社会的上昇と倫理的試練を描く米国リアリズムの代表的長編。", 4, "high", "partial"),
    ("クレイン『赤い武勲章』戦場心理", "Crane, The Red Badge of Courage", "The Red Badge of Courage", "latin", P_NATURALISM,
     "南北戦争一兵卒の恐怖と勇気を断片的印象主義で描く心理的自然主義の試金石。", 4, "high", "partial"),
    ("ノリス『マクティーグ』退化の物語", "Norris, McTeague", "McTeague", "latin", P_NATURALISM,
     "サンフランシスコ歯科医の没落をゾラ的決定論で描いた米国自然主義の典型。", 4, "high", "partial"),
    ("ドライサー『シスター・キャリー』都市移動", "Dreiser, Sister Carrie", "Sister Carrie", "latin", P_NATURALISM,
     "農村娘キャリーのシカゴ・NYでの欲望と社会上昇を非道徳的視点で描く都市自然主義。", 4, "high", "partial"),
    ("ウォートン『歓楽の家』社交界悲劇", "Wharton, The House of Mirth", "The House of Mirth", "latin", P_NATURALISM,
     "NY上流社会のリリー・バートの転落を通じ女性の経済的脆さを批判する自然主義小説。", 4, "high", "rethinking"),
    ("ジェイムズ『ある婦人の肖像』選択の自由", "James, The Portrait of a Lady", "The Portrait of a Lady", "latin", P_EN,
     "イザベル・アーチャーの結婚選択を通じ意識の劇場を構築した心理リアリズムの里程標。", 5, "high", "rethinking"),

    # ===== Cluster 5: 独伊西 (6) =====
    ("フォンターネ『エフィ・ブリースト』姦通小説", "Fontane, Effi Briest", "Effi Briest", "latin", P_DE,
     "プロイセン貴族妻エフィの不倫と社会的処罰を抑制的文体で描く独詩的リアリズム代表作。", 5, "high", "partial"),
    ("ヴェルガ『マラヴォリア家の人々』ヴェリズモ", "Verga, I Malavoglia", "I Malavoglia", "latin", P_IT,
     "シチリア漁村一家の没落を方言的自由間接話法で描く伊ヴェリズモ運動の旗艦作。", 5, "high", "partial"),
    ("ガルドス『フォルトゥナータとハシンタ』", "Galdós, Fortunata y Jacinta", "Fortunata y Jacinta", "latin", P_ES,
     "マドリードの愛人と妻という二女性の対比から復古王政期社会を描く西リアリズム長編。", 5, "high", "partial"),
    ("パルド・バサン『ウリョアの館』地方頽廃", "Pardo Bazán, Los Pazos de Ulloa", "Los Pazos de Ulloa", "latin", P_ES,
     "ガリシアの没落貴族館を舞台に地方の野生と頽廃を描く西自然主義代表作。", 4, "high", "partial"),
    ("エサ・デ・ケイロス『マイア家の人々』", "Eça de Queirós, Os Maias", "Os Maias", "latin", P_ES,
     "リスボン上流家系の頽廃を世代的に追い葡国社会を批判するポルトガル・リアリズム長編。", 5, "high", "partial"),
    ("シュトルム『白馬の騎手』堤防の伝説", "Storm, Der Schimmelreiter", "Der Schimmelreiter", "latin", P_DE,
     "北フリースラントを舞台に堤防監督官ハウケの悲劇を語る独詩的リアリズム晩年ノヴェレ。", 5, "high", "invariant"),
]

assert len(ROWS) == 30, len(ROWS)

INSERT = """
INSERT OR IGNORE INTO concepts
  (name_ja, name_en, name_original, original_script, subfield_id, region,
   period_id, definition, importance_score, source_tier, canonical_in_region,
   fourth_transform_status)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
"""

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    inserted = 0
    skipped = 0
    for r in ROWS:
        (nja, nen, norig, scr, pid, dfn, imp, canon, four) = r
        assert len(dfn) <= 100, f"def too long ({len(dfn)}): {nja}"
        cur.execute(INSERT, (nja, nen, norig, scr, SUBFIELD_ID, REGION, pid, dfn, imp, "tier1", canon, four))
        if cur.rowcount == 1:
            inserted += 1
        else:
            skipped += 1
    con.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)).fetchone()[0]
    con.close()
    print(f"inserted={inserted} skipped={skipped} subfield_total={total}")

if __name__ == "__main__":
    main()
