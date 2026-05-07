"""Wave 30 Cluster 22: Persian/Turkish 30 concepts (subfield_id=14)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 14
REGION = "西アジア"

# period mapping
P_CLASSIC_EARLY = 250  # ペルシア古典初期（サーマーン・ガズナ）
P_CLASSIC_MID = 47     # ペルシア古典中期（セルジューク・ホラズム）
P_CLASSIC_LATE = 48    # ペルシア古典後期（イルハン・ティムール）
P_SABK_HINDI = 142     # サブク・ヒンディー期
P_OTTOMAN = 49         # オスマン古典期
P_MODERN = 51          # 近現代ペルシア・トルコ

CONCEPTS = [
    # Cluster 1: ペルシア古典 (6)
    ("ルーダキー『ディーワーン詩集』", "Rudaki Divan", "دیوان رودکی", "arabic", P_CLASSIC_EARLY,
     "ペルシア詩の父ルーダキーの抒情詩集。サーマーン朝宮廷詩の規範を確立した。"),
    ("ダキーキー『シャー・ナーメ断片』", "Daqiqi Shahnameh Fragments", "شاهنامه دقیقی", "arabic", P_CLASSIC_EARLY,
     "フェルドウスィーに先立つダキーキーによる王書断片1000節。ゾロアスター教改宗譚を含む。"),
    ("シャー・ナーメ『ビージャンとマニージェ』", "Bizhan and Manijeh", "بیژن و منیژه", "arabic", P_CLASSIC_EARLY,
     "フェルドウスィー王書中の恋愛悲劇譚。捕囚されたビージャンとトゥラン王女の愛の物語。"),
    ("シャー・ナーメ『ロスタムとソフラーブ』詳論", "Rostam and Sohrab Detailed", "رستم و سهراب", "arabic", P_CLASSIC_EARLY,
     "父子対決の悲劇。父が知らずして実子を殺す王書最大の英雄譚で運命と認知の主題を展開。"),
    ("シャー・ナーメ『スィヤーヴァシュ』詳論", "Siavash Detailed", "سیاوش", "arabic", P_CLASSIC_EARLY,
     "純潔の王子スィヤーヴァシュの受難と殉死譚。火試練と政治的犠牲を描く悲劇連作。"),
    ("シャー・ナーメ『エスファンディヤール』詳論", "Esfandiyar Detailed", "اسفندیار", "arabic", P_CLASSIC_EARLY,
     "不死身の王子エスファンディヤールとロスタムの宿命的対決。七難業と目への矢の物語。"),

    # Cluster 2: ペルシアSufi (6)
    ("サナーイー『真理の園（ハディーカト）』", "Hadiqat al-Haqiqa", "حدیقة الحقیقة", "arabic", P_CLASSIC_MID,
     "ペルシア神秘主義教訓詩の祖型。マスナヴィー形式でスーフィー道の教義を体系化した。"),
    ("アッタール『聖者列伝（タズキラト）』", "Tazkirat al-Awliya", "تذکرة الأولیاء", "arabic", P_CLASSIC_MID,
     "アッタールの散文集。72人のスーフィー聖者伝を逸話と教説で構成、神秘主義伝記の規範。"),
    ("ルーミー『マスナヴィー第一巻』詳論", "Masnavi Book One", "مثنوی دفتر اول", "arabic", P_CLASSIC_MID,
     "葦笛の歌で開く全6巻の冒頭。分離と帰還の主題を約4000節で展開する神秘哲学詩の核。"),
    ("ルーミー『ディーワーン・シャムス』詳論", "Diwan-e Shams", "دیوان شمس", "arabic", P_CLASSIC_MID,
     "ルーミーがシャムスへの愛で歌った40000節超のガザル集。恍惚と消滅の詩学。"),
    ("サアディー『ブースターン』教訓構造詳論", "Bustan", "بوستان", "arabic", P_CLASSIC_MID,
     "果樹園の意。10章のマスナヴィー教訓詩で正義・慈悲・知足を逸話で説く倫理学体系。"),
    ("ハーフェズ『ディーワーン』ガザル集", "Hafez Divan Ghazals", "دیوان حافظ", "arabic", P_CLASSIC_LATE,
     "シーラーズの詩聖ハーフェズの約500篇ガザル。多義性と神秘恋愛の最高峰として愛唱される。"),

    # Cluster 3: Sabk-e Hindi (6)
    ("ビーデル・デフラヴィー", "Bidel Dehlavi", "بیدل دهلوی", "arabic", P_SABK_HINDI,
     "ムガル朝の哲学詩人。難解な比喩と思弁性でサブク・ヒンディー最高峰、中央アジアで信奉。"),
    ("サーイブ・タブリーズィー", "Sa'eb Tabrizi", "صائب تبریزی", "arabic", P_SABK_HINDI,
     "イスファハーン派の指導的詩人。新奇な比喩（マズムーン）でサブク・ヒンディー期を代表。"),
    ("カリーム・カーシャーニー", "Kalim Kashani", "کلیم کاشانی", "arabic", P_SABK_HINDI,
     "シャー・ジャハーン宮廷詩人。社会批評的ガザルで知られインド・ペルシア詩流の重鎮。"),
    ("ナズィーリー・ニーシャープーリー", "Naziri Nishaburi", "نظیری نیشابوری", "arabic", P_SABK_HINDI,
     "ムガル朝アクバル・ジャハーンギール期の詩人。深遠な思弁ガザルでサブク・ヒンディー形成。"),
    ("ガザーリー・マシュハディー", "Ghazali Mashhadi", "غزالی مشهدی", "arabic", P_SABK_HINDI,
     "アクバル朝最初の桂冠詩人。神秘主義と新奇比喩を融合しサブク・ヒンディー初期を導いた。"),
    ("ターヘル・ヴァヒード", "Tahir Vahid", "طاهر وحید", "arabic", P_SABK_HINDI,
     "サファヴィー朝後期の宰相詩人。ガザル12万節超を伝え新派ペルシア詩の集大成者。"),

    # Cluster 4: Ottoman classical (6)
    ("ユヌス・エムレ『ディーワーン』", "Yunus Emre Divan", "Yunus Emre Divanı", "latin", P_OTTOMAN,
     "アナトリア・テッケ詩の父。素朴なトルコ語による神秘主義抒情詩で民衆スーフィズムの礎。"),
    ("フズーリー『レイラとメジュヌーン』詳論", "Leyla vu Mecnun", "Leylâ ve Mecnûn", "latin", P_OTTOMAN,
     "アゼリ・トルコ語マスナヴィー恋愛叙事詩。ニザーミーを継承しオスマン古典の頂点を成す。"),
    ("アフメディー『イスケンデルナーメ』詳論", "Iskendername", "İskendernâme", "latin", P_OTTOMAN,
     "アレクサンドロス王譚の8000節トルコ語マスナヴィー。最古期オスマン文学の代表作。"),
    ("シェイヒ・ガーリブ『フスン・ヴ・アシュク』詳論", "Hüsn ü Aşk", "Hüsn ü Aşk", "latin", P_OTTOMAN,
     "メウレヴィー教団詩人ガーリブの寓意マスナヴィー。美と愛の神秘的旅路を象徴詩で描く。"),
    ("ネディーム『ガザル集』", "Nedim Ghazals", "Nedim Gazelleri", "latin", P_OTTOMAN,
     "チューリップ時代の宮廷詩人。世俗的享楽とイスタンブール風物を歌うガザルで一新を遂げた。"),
    ("バーキー『カスィーデ集』", "Baki Kasideler", "Bâkî Kasideleri", "latin", P_OTTOMAN,
     "スレイマン1世の桂冠詩人。荘重なカスィーデで君主賛美の規範を確立、詩王と称された。"),

    # Cluster 5: Modern (6)
    ("ヘダーヤト『盲目の梟』詳論", "Buf-e Kur Detailed", "بوف کور", "arabic", P_MODERN,
     "1937年刊。意識流と幻想で現代イラン人の疎外を描く近代ペルシア小説の金字塔。"),
    ("フォルーグ『新たに誕生する』", "Tavalludi Digar", "تولدی دیگر", "arabic", P_MODERN,
     "1964年刊フォルーグ・ファッロホザード詩集。女性主体で身体・愛・解放を歌う革新的作品。"),
    ("シャムルー『鏡の中のアーイダ』", "Ayda dar Ayene", "آیدا در آینه", "arabic", P_MODERN,
     "1964年シャムルー詩集。妻アーイダを主題に自由詩（シェル・スピード）の到達点を示す。"),
    ("パムク『私の名は紅』", "My Name Is Red", "Benim Adım Kırmızı", "latin", P_MODERN,
     "1998年作。16世紀オスマン細密画工の殺人事件を多声で描くノーベル賞作家の代表長編。"),
    ("タンプナル『時間調整研究所』", "Saatleri Ayarlama Enstitüsü", "Saatleri Ayarlama Enstitüsü", "latin", P_MODERN,
     "1962年刊。トルコ近代化の不条理を時計修理協会の風刺で描く20世紀文学の傑作。"),
    ("ヒクメット『私の故郷からの人間風景』", "Memleketimden İnsan Manzaraları", "Memleketimden İnsan Manzaraları", "latin", P_MODERN,
     "ナーズム・ヒクメットの大叙事詩。獄中執筆、近代トルコ社会を多視点で描く全5巻の代表作。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for (name_ja, name_en, name_orig, script, period_id, definition) in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, period_id, definition, 4, "primary", "yes"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP: {name_ja} ({e})")
            skipped += 1
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)).fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield 14: {total}")

if __name__ == "__main__":
    main()
