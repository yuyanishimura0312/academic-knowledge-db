#!/usr/bin/env python3
"""Wave 25 C11: Add 30 postmodern concepts to lit_eu_postmodern (subfield_id=7)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 7
PERIOD_ID = 124  # ポストモダン期 (西欧)
REGION = "西欧"

# (name_ja, name_en, name_original, original_script, definition, importance, source_tier)
CONCEPTS = [
    # 1. Theoretical (6)
    ("リオタール『ポストモダンの条件』論", "Lyotard, La condition postmoderne", "La condition postmoderne", "latin",
     "大きな物語への不信を時代精神とし、知の正統性を多様な小さな語りに分散させる理論枠組。", 5, "secondary"),
    ("ボードリヤール『シミュラークルとシミュレーション』論", "Baudrillard, Simulacres et simulation", "Simulacres et simulation", "latin",
     "現実とコピーの区別が崩壊し、模像が先行するハイパーリアリティを記述する文化論。", 5, "secondary"),
    ("ジェイムソン『ポストモダニズム』論", "Jameson, Postmodernism", "Postmodernism, or, the Cultural Logic of Late Capitalism", "latin",
     "後期資本主義の文化論理としてポストモダンを捉え、空間性・パスティーシュ・歴史感覚喪失を分析する。", 5, "secondary"),
    ("ハッチオン『ポストモダニズムの詩学』再考", "Hutcheon, A Poetics of Postmodernism (revisited)", "A Poetics of Postmodernism", "latin",
     "歴史記述的メタフィクションを核に、参照と批判を両立させるポストモダンの詩学を体系化する。", 4, "secondary"),
    ("マクヘイル『ポストモダニスト・フィクション』再考", "McHale, Postmodernist Fiction (revisited)", "Postmodernist Fiction", "latin",
     "存在論的優位への移行を診断軸に、ポストモダン小説の世界構築を体系化する研究。", 4, "secondary"),
    ("ハッサン『ポストモダン的転回』", "Hassan, The Postmodern Turn", "The Postmodern Turn", "latin",
     "モダンとポストモダンの対比表を提示し、不確定性・内在性を文化的兆候として概念化した試論。", 4, "secondary"),

    # 2. American (6)
    ("デリーロ『アンダーワールド』再読", "DeLillo, Underworld (reread)", "Underworld", "latin",
     "冷戦期アメリカの廃棄物・記憶・メディアを長編横断的に編み上げる歴史記述的メタフィクション。", 4, "secondary"),
    ("ピンチョン『メイスン&ディクスン』再読", "Pynchon, Mason & Dixon (reread)", "Mason & Dixon", "latin",
     "18世紀英語擬古文体で米国境界線測量を語り、近代性の暴力と魔術的余剰を露呈させる長編。", 4, "secondary"),
    ("ウォレス『ペイル・キング』再読", "Wallace, The Pale King (reread)", "The Pale King", "latin",
     "国税庁を舞台に退屈と注意の倫理を探求し、ポスト・アイロニーの誠実を志向する未完小説。", 4, "secondary"),
    ("クーヴァー『公開焚刑』再読", "Coover, The Public Burning (reread)", "The Public Burning", "latin",
     "ローゼンバーグ夫妻処刑をニクソンの語りで脱構築し、米国神話を爆破するメタ歴史小説。", 4, "secondary"),
    ("バース『驚き屋敷で道に迷って』再読", "Barth, Lost in the Funhouse (reread)", "Lost in the Funhouse", "latin",
     "語りの自己言及と枠物語連鎖でメタフィクションの可能性を提示した連作短編。", 4, "secondary"),
    ("ヴォネガット『スローターハウス5』再読", "Vonnegut, Slaughterhouse-Five (reread)", "Slaughterhouse-Five", "latin",
     "ドレスデン爆撃の記憶をSF的時間跳躍と反語で語り、戦争と歴史を脱中心化した古典。", 4, "secondary"),

    # 3. British (6)
    ("カーター『血染めの部屋』再読", "Carter, The Bloody Chamber (reread)", "The Bloody Chamber", "latin",
     "童話の暴力と性差を再書きし、フェミニズム的ゴシックとしてジャンル境界を脱臼させる短編集。", 4, "secondary"),
    ("アクロイド『ホークスムーア』再読", "Ackroyd, Hawksmoor (reread)", "Hawksmoor", "latin",
     "18世紀建築家と現代刑事の二重時間を交錯させ、ロンドン都市記憶を心霊化した小説。", 4, "secondary"),
    ("マキューアン『贖罪』再読", "McEwan, Atonement (reread)", "Atonement", "latin",
     "誤認証言と作家化された語りを枠ごと暴き、フィクションの倫理を主題化する歴史記述的メタ小説。", 4, "secondary"),
    ("イシグロ『クララとお日さま』", "Ishiguro, Klara and the Sun", "Klara and the Sun", "latin",
     "AF（人工友人）クララの語りで人格・愛・代替不可能性を問うポスト・ヒューマン的寓話。", 4, "secondary"),
    ("スミス『ホワイト・ティース』再読", "Smith, White Teeth (reread)", "White Teeth", "latin",
     "戦後ロンドンの多文化家族三世代を多声的に描き、ポスト植民地英国小説を更新した長編。", 4, "secondary"),
    ("ミッチェル『クラウド・アトラス』再読", "Mitchell, Cloud Atlas (reread)", "Cloud Atlas", "latin",
     "六つの時代のジャンル小説を入れ子状に連結し、輪廻と権力の連鎖を描く構造小説。", 4, "secondary"),

    # 4. European (6)
    ("エーコ『フーコーの振り子』再読", "Eco, Il pendolo di Foucault (reread)", "Il pendolo di Foucault", "latin",
     "陰謀論の構築と読みの暴走を描き、過剰解釈と記号過剰の現代を風刺する百科全書的小説。", 4, "secondary"),
    ("カルヴィーノ『見えない都市』再読", "Calvino, Le città invisibili (reread)", "Le città invisibili", "latin",
     "マルコ・ポーロが語る寓話的都市群でカタログ的形式と都市論を融合させた連作。", 4, "secondary"),
    ("ゼーバルト『アウステルリッツ』再読", "Sebald, Austerlitz (reread)", "Austerlitz", "latin",
     "写真と長文一段落で記憶喪失とホロコースト痕跡を辿る、ドキュ・フィクションの代表作。", 4, "secondary"),
    ("クンデラ『存在の耐えられない軽さ』", "Kundera, The Unbearable Lightness of Being", "Nesnesitelná lehkost bytí", "latin",
     "プラハの春前後の四人を題材に、軽さ/重さ・反復・キッチュを哲学的随筆と編む小説。", 4, "secondary"),
    ("ウエルベック『服従』", "Houellebecq, Soumission", "Soumission", "latin",
     "近未来仏のイスラーム政権成立を冷ややかな視点で描き、世俗近代の自滅を描出する政治小説。", 4, "secondary"),
    ("サラマーゴ『白の闇』再読", "Saramago, Blindness (reread)", "Ensaio sobre a cegueira", "latin",
     "突如失明する都市崩壊を句読点を解体した語りで描き、文明の脆さを寓意化する長編再読。", 4, "secondary"),

    # 5. Slavic + misc (6)
    ("クラスナホルカイ『サタンタンゴ』再読", "Krasznahorkai, Sátántangó (reread)", "Sátántangó", "latin",
     "崩壊する集団農場を長文連続体で描き、終末感と循環構造を提示するハンガリー長編。", 4, "secondary"),
    ("ペレーヴィン『エンパイアV』", "Pelevin, Empire V", "Ампир В", "cyrillic",
     "吸血鬼の隠れ支配神話を消費社会風刺に翻案し、ポストソ連ロシアの記号操作を描く小説。", 4, "secondary"),
    ("トカルチュク『ヤコブの書物』", "Tokarczuk, The Books of Jacob", "Księgi Jakubowe", "latin",
     "18世紀フランク派救世主運動を多声的に再構成し、東欧多文化史を神話化する大長編。", 4, "secondary"),
    ("アトウッド『侍女の物語』再読", "Atwood, The Handmaid's Tale (reread)", "The Handmaid's Tale", "latin",
     "神権主義的近未来でのオブフレッドの語りを枠学術註で挟み、ジェンダーと権力を脱構築する。", 4, "secondary"),
    ("ミッチェル『ナンバー9ドリーム』", "Mitchell, Number9Dream", "Number9Dream", "latin",
     "東京を舞台に夢と現実、サイバーと神話を多層化した日英クロスオーバーのポストモダン小説。", 3, "secondary"),
    ("ボラーニョ『2666』", "Bolaño, 2666", "2666", "latin",
     "シウダー・フアレスの女性連続殺人を中心に五部を編み、暴力と20世紀の闇を巨視する遺作。", 4, "secondary"),
]


def main() -> None:
    conn = sqlite3.connect(str(DB))
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for name_ja, name_en, name_orig, script, definition, importance, tier in CONCEPTS:
        assert len(definition) <= 100, f"def too long ({len(definition)}): {name_ja}"
        try:
            cur.execute(
                """
                INSERT INTO concepts
                  (name_ja, name_en, name_original, original_script,
                   subfield_id, region, period_id,
                   definition, importance_score, source_tier)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (name_ja, name_en, name_orig, script,
                 SUBFIELD_ID, REGION, PERIOD_ID,
                 definition, importance, tier),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield 7: {total}")


if __name__ == "__main__":
    main()
