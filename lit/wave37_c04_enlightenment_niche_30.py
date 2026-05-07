#!/usr/bin/env python3
"""Wave 37: Add 30 niche concepts to subfield 4 (lit_eu_enlightenment)."""
import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SF = 4
REGION = "西欧"

# 5 clusters x 6 concepts. period_id mostly 100 (盛期啓蒙), 102 (後期/前ロマン)
ROWS = [
    # Cluster 1: 仏啓蒙細部
    ("マリヴォー『マリアンヌの生涯』詳論", "Marivaux La Vie de Marianne", "La Vie de Marianne", 100, "未完の心理小説。女性主人公の自己語りと社交界観察。", 4, "tier1", "canonical"),
    ("プレヴォ『マノン・レスコー』情熱論", "Prévost Manon Lescaut passion", "Histoire du chevalier Des Grieux et de Manon Lescaut", 100, "情熱と道徳の相克。回想体告白の感性主義の先駆。", 5, "tier1", "canonical"),
    ("クレビヨン・フィス『ソファ』東洋枠", "Crébillon fils Le Sopha oriental frame", "Le Sopha, conte moral", 100, "東洋枠物語形式のリベルタン小説。風刺と官能の織物。", 3, "tier2", "secondary"),
    ("レチフ・ド・ラ・ブルトンヌ『ムッシュー・ニコラ』", "Restif de la Bretonne Monsieur Nicolas", "Monsieur Nicolas", 102, "民衆出身者の巨大自伝。日常微細誌と性的告白の混合。", 3, "tier2", "secondary"),
    ("ベルナルダン・ド・サン＝ピエール『ポールとヴィルジニー』", "Bernardin de Saint-Pierre Paul et Virginie", "Paul et Virginie", 102, "熱帯島の牧歌的恋愛悲劇。ルソー的自然観の小説化。", 4, "tier1", "canonical"),
    ("サド『ジュスティーヌ』哲学的悪徳論", "Sade Justine philosophical vice", "Justine ou les Malheurs de la vertu", 102, "徳の不幸と悪の繁栄を描く反啓蒙的哲学小説。", 4, "tier1", "canonical"),

    # Cluster 2: 英散文・小説興隆
    ("デフォー『モル・フランダーズ』犯罪自伝", "Defoe Moll Flanders criminal autobiography", "The Fortunes and Misfortunes of the Famous Moll Flanders", 99, "女性犯罪者の一人称回想。経済的合理性と悔悛の語り。", 4, "tier1", "canonical"),
    ("リチャードソン『パメラ』徳の報い", "Richardson Pamela virtue rewarded", "Pamela; or, Virtue Rewarded", 100, "下女の貞操書簡体小説。中産階級道徳と感性の確立。", 5, "tier1", "canonical"),
    ("リチャードソン『クラリッサ』悲劇的書簡体", "Richardson Clarissa tragic epistolary", "Clarissa, or, the History of a Young Lady", 100, "1500ページの書簡体悲劇。誘惑・凌辱・聖化の心理劇。", 5, "tier1", "canonical"),
    ("フィールディング『ジョセフ・アンドルーズ』", "Fielding Joseph Andrews", "The History of the Adventures of Joseph Andrews", 100, "リチャードソン『パメラ』のパロディから出発した喜劇的叙事詩。", 4, "tier1", "canonical"),
    ("スモレット『ロデリック・ランダム』海洋ピカレスク", "Smollett Roderick Random naval picaresque", "The Adventures of Roderick Random", 100, "海軍経験を反映したスコットランド出身者のピカレスク小説。", 3, "tier1", "canonical"),
    ("スターン『センチメンタル・ジャーニー』", "Sterne A Sentimental Journey", "A Sentimental Journey Through France and Italy", 101, "感傷旅行記の創始。微細な感情の動きと自己観察。", 5, "tier1", "canonical"),

    # Cluster 3: 独啓蒙・疾風怒濤
    ("レッシング『エミーリア・ガロッティ』市民悲劇", "Lessing Emilia Galotti bourgeois tragedy", "Emilia Galotti", 100, "ヴィルギニア伝説の翻案。市民悲劇とドイツ啓蒙劇の頂点。", 4, "tier1", "canonical"),
    ("レッシング『賢者ナータン』寛容劇", "Lessing Nathan der Weise tolerance", "Nathan der Weise", 102, "三宗教の指輪のたとえ劇。啓蒙的寛容思想の演劇的表現。", 5, "tier1", "canonical"),
    ("クロップシュトック『メシアス』叙事詩", "Klopstock Der Messias epic", "Der Messias", 99, "ミルトンに倣った宗教叙事詩。ドイツ詩語の刷新。", 3, "tier1", "canonical"),
    ("ヴィーラント『オーベロン』ロマンス詩", "Wieland Oberon romance poem", "Oberon", 102, "騎士ロマンスと妖精譚の融合。シェイクスピア受容の結実。", 3, "tier1", "canonical"),
    ("レンツ『軍人たち』疾風怒濤劇", "Lenz Die Soldaten Sturm und Drang drama", "Die Soldaten", 102, "シェイクスピア型の市民劇。階級・性差別を告発する社会劇。", 3, "tier1", "canonical"),
    ("クリンガー『シュトゥルム・ウント・ドラング』", "Klinger Sturm und Drang", "Sturm und Drang", 102, "運動名の由来となった戯曲。情熱の暴発と若者の革命衝動。", 4, "tier1", "canonical"),

    # Cluster 4: 伊・西啓蒙
    ("ゴルドーニ『宿屋の女主人』喜劇改革", "Goldoni La Locandiera comedy reform", "La locandiera", 100, "コメディア・デラルテを脱した近代写実喜劇。市民風俗劇。", 4, "tier1", "canonical"),
    ("アルフィエーリ『サウル』新古典悲劇", "Alfieri Saul neoclassical tragedy", "Saul", 102, "イタリア新古典悲劇の頂点。専制への反逆と自由の精神。", 3, "tier1", "canonical"),
    ("パリーニ『一日』風刺詩", "Parini Il Giorno satire", "Il Giorno", 100, "貴族青年の一日を諷刺するブランクヴァース詩。啓蒙的市民批判。", 3, "tier1", "canonical"),
    ("フォスコロ『オルティスの最後の手紙』", "Foscolo Ultime lettere di Jacopo Ortis", "Ultime lettere di Jacopo Ortis", 102, "ナポレオン体制下イタリアの愛国的書簡体小説。ヴェルター型自殺。", 4, "tier1", "canonical"),
    ("フェイホー『普遍批評劇場』", "Feijoo Teatro crítico universal", "Teatro crítico universal", 99, "スペイン啓蒙の博物誌的百科。迷信批判と科学的合理性。", 3, "tier1", "canonical"),
    ("ホベリャーノス『パンと闘牛』改革論", "Jovellanos Pan y Toros reform pamphlet", "Pan y Toros", 102, "スペイン社会改革論のパンフレット。封建残滓と娯楽批判。", 3, "tier2", "secondary"),

    # Cluster 5: 露・北欧
    ("ロモノーソフ頌歌", "Lomonosov ode", "Ода", 99, "ロシア古典主義頌歌の創始。三スタイル説と詩語の規範化。", 3, "tier1", "canonical"),
    ("デルジャーヴィン『フェリーツァ』", "Derzhavin Felitsa", "Фелица", 100, "エカチェリーナ二世讃美の頌歌。古典主義の転位と個人語り。", 3, "tier1", "canonical"),
    ("カラムジン『哀れなリーザ』感傷小説", "Karamzin Poor Liza sentimental", "Бедная Лиза", 102, "ロシア感傷小説の代表作。階級差恋愛の悲劇と自然描写。", 4, "tier1", "canonical"),
    ("フォンヴィージン『未成年』風刺喜劇", "Fonvizin Nedorosl satirical comedy", "Недоросль", 100, "ロシア風刺喜劇の傑作。地方貴族の無教育と農奴制批判。", 4, "tier1", "canonical"),
    ("ホルベア『ニルス・クリムの地下旅行』", "Holberg Niels Klim subterranean", "Nicolai Klimii Iter Subterraneum", 100, "デンマーク啓蒙のラテン語空想旅行記。社会風刺と相対主義。", 3, "tier1", "canonical"),
    ("ベルマン『フレドマンの書簡』", "Bellman Fredmans epistlar", "Fredmans epistlar", 102, "スウェーデン酒場詩。バロック讃美歌のパロディと民衆生活。", 3, "tier2", "canonical"),
]

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    inserted = skipped = 0
    for name_ja, name_en, name_orig, period_id, definition, importance, tier, canon in ROWS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id,
                 region, period_id, definition, importance_score,
                 source_tier, canonical_in_region)
                VALUES (?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, SF, REGION, period_id, definition, importance, tier, canon))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    con.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SF,)).fetchone()[0]
    con.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total in subfield {SF}: {total}")

if __name__ == "__main__":
    main()
