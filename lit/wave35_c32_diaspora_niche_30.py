"""Wave 35 C32: lit_diaspora niche 30 concepts (5 clusters x 6)."""
import sqlite3, os
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")

SUBFIELD_ID = 20
PERIOD_ID = 168  # グローバル・ディアスポラ期

CONCEPTS = [
    # Cluster 1: Caribbean Francophone (6)
    ("マリーズ・コンデ『エレマコノン』", "Maryse Condé, Heremakhonon", "Heremakhonon", "latin", "ラテンアメリカ",
     "グアドループ女性のアフリカ帰還を描く幻滅の自伝的小説、汎アフリカ主義の神話を解体する。"),
    ("パトリック・シャモワゾー『テキサコ』詳論", "Patrick Chamoiseau, Texaco (analysis)", "Texaco", "latin", "ラテンアメリカ",
     "マルティニーク貧民街の三世代史をクレオール語で語り、口承記憶と都市性を結ぶゴンクール賞作。"),
    ("エドゥアール・グリッサン『裂け目の河』", "Édouard Glissant, La Lézarde", "La Lézarde", "latin", "ラテンアメリカ",
     "1958年マルティニーク独立運動を背景に、河と土地の声で集団的主体形成を描く処女長編。"),
    ("シュザンヌ・セゼール『トロピック』論考", "Suzanne Césaire, Tropiques essays", "Tropiques", "latin", "ラテンアメリカ",
     "シュルレアリスムとカリブ的感性を結合し、植民地的従属を超える「カリブ的人間」を構想した戦中誌。"),
    ("シモーヌ・シュヴァルツ=バルト『風と雨のテリュメ』", "Simone Schwarz-Bart, Pluie et vent sur Télumée Miracle", "Pluie et vent", "latin", "ラテンアメリカ",
     "グアドループ農村の四世代女性史を口承的文体で描き、奴隷後社会の女性の強靱さを称揚する。"),
    ("ダニエル・マクシマン『噴火口たち』", "Daniel Maximin, L'Isolé soleil", "L'Isolé soleil", "latin", "ラテンアメリカ",
     "グアドループ史を断片と書簡で再構築し、火山島の地層的記憶とディアスポラ意識を交錯させる。"),

    # Cluster 2: Black British detail (6)
    ("ベルナーディン・エヴァリスト『ララ』", "Bernardine Evaristo, Lara", "Lara", "latin", "西欧",
     "黒人アイルランド系英国女性の系譜を韻文小説で辿り、四大陸の祖先を結ぶ自伝的叙事詩。"),
    ("カリル・フィリップス『最終航路』詳論", "Caryl Phillips, The Final Passage (analysis)", "The Final Passage", "latin", "西欧",
     "ウィンドラッシュ世代カリブ女性の英国移住と幻滅を内省的視点で描いた処女長編。"),
    ("ヘレン・オエイェミ『ホワイト・イズ・フォー・ウィッチング』", "Helen Oyeyemi, White Is for Witching", "White Is for Witching", "latin", "西欧",
     "ナイジェリア系英国の家系を取り憑く幽霊屋敷を四声で語り、人種・摂食障害・地霊を交錯させる。"),
    ("ハニフ・クレイシ『郊外の仏陀』詳論", "Hanif Kureishi, The Buddha of Suburbia (analysis)", "The Buddha of Suburbia", "latin", "西欧",
     "1970年代ロンドン郊外のパキスタン系英国少年の成長を諧謔的に描き、ハイブリッド英国性を問う。"),
    ("ダイアナ・エヴァンス『26a』詳論", "Diana Evans, 26a (analysis)", "26a", "latin", "西欧",
     "ナイジェリア系英国双子姉妹の屋根裏部屋世界を描き、移民第二世代の二重性と離別を寓話化する。"),
    ("ジェイ・バーナード『サージ』", "Jay Bernard, Surge", "Surge", "latin", "西欧",
     "1981年ニュー・クロス火災事件アーカイブを再訪する詩集、黒人英国の集合的喪と亡霊性を編む。"),

    # Cluster 3: Translingual (6)
    ("アレクサンドル・ヘモン『ラザロ計画』", "Aleksandar Hemon, The Lazarus Project", "The Lazarus Project", "latin", "横断",
     "1908年シカゴで射殺されたユダヤ移民事件と現代ボスニア人作家の旅を交錯させる二重物語。"),
    ("多和田葉子『雪の練習生』詳論", "Yoko Tawada, Memoirs of a Polar Bear (analysis)", "雪の練習生", "kanji", "横断",
     "三世代の北極熊が語る亡命と書くことの寓話、ドイツ語で書かれた越境動物自伝。"),
    ("テレサ・ハッキョン・チャ『ディクテ』詳論", "Theresa Hak Kyung Cha, Dictée (analysis)", "Dictée", "latin", "横断",
     "韓国系米国女性の九つのミューズによる多言語実験テクスト、植民地史と母語喪失を断章で編む。"),
    ("ジュンパ・ラヒリ『どこにいるのか』", "Jhumpa Lahiri, Whereabouts", "Dove mi trovo", "latin", "横断",
     "イタリア語で書かれ自ら英訳した断章小説、無名のローマの女性の場所と孤独を四十六章で記す。"),
    ("カプカ・カサボヴァ『ボーダー』", "Kapka Kassabova, Border", "Border", "latin", "横断",
     "ブルガリア生まれ作家がブルガリア・ギリシャ・トルコ三国境を歩く越境ノンフィクション紀行。"),
    ("オルガ・トカルチュク『逃亡派』", "Olga Tokarczuk, Flights", "Bieguni", "latin", "西欧",
     "断片的旅と人体保存の挿話を百以上織る星座的小説、移動を主体性の様態として理論化する。"),

    # Cluster 4: Latinx US (6)
    ("サンドラ・シスネロス『キャラメル色の肌』", "Sandra Cisneros, Caramelo", "Caramelo", "latin", "横断",
     "メキシコ系米国一家のシカゴ・メキシコシティ往復史を娘の語りで紡ぐ三世代多言語家族叙事詩。"),
    ("ジュノ・ディアス『こうしてお前は彼女を失う』", "Junot Díaz, This Is How You Lose Her", "This Is How You Lose Her", "latin", "横断",
     "ドミニカ系米国男性ユニオールの愛と裏切りの連作短編、マチスモとSpanglishの詩学。"),
    ("クリスティーナ・ガルシア『キューバン・ドリーム』", "Cristina García, Dreaming in Cuban", "Dreaming in Cuban", "latin", "横断",
     "革命キューバと米国に分かれたデルピノ家三世代の女性を多視点で描く亡命と神霊の家族小説。"),
    ("アチー・オベハス『記憶のマンボ』", "Achy Obejas, Memory Mambo", "Memory Mambo", "latin", "横断",
     "キューバ系レズビアン女性の家族秘密と記憶の捏造を扱う、ディアスポラとクィアを交差させる小説。"),
    ("ダニエル・アラルコン『失われた都市の電波』", "Daniel Alarcón, Lost City Radio", "Lost City Radio", "latin", "横断",
     "ペルー系米国作家による架空南米国家の内戦後行方不明者ラジオ番組を描く政治寓話。"),
    ("フリア・アルバレス『蝶々の時代』", "Julia Alvarez, In the Time of the Butterflies", "In the Time of the Butterflies", "latin", "横断",
     "ドミニカ独裁下で殺害されたミラバル四姉妹を多声で蘇らせる歴史小説、亡命作家の故国記憶。"),

    # Cluster 5: Middle East + African Diaspora (6)
    ("エドウィージ・ダンティカ『兄よ、私は死にゆく』", "Edwidge Danticat, Brother, I'm Dying", "Brother, I'm Dying", "latin", "横断",
     "ハイチ系米国作家による父と叔父の死を綴る回想録、移民拘留制度下の家族喪失を証言する。"),
    ("マーロン・ジェイムズ『黒豹、赤狼』", "Marlon James, Black Leopard, Red Wolf", "Black Leopard, Red Wolf", "latin", "アフリカ",
     "ジャマイカ系作家によるアフリカ神話的ファンタジー三部作第一作、口承的多視点で英雄譚を解体。"),
    ("ヤー・ジャシ『ホームゴーイング』詳論", "Yaa Gyasi, Homegoing (analysis)", "Homegoing", "latin", "アフリカ",
     "ガーナ系米国作家がアサンテ姉妹から七世代の奴隷貿易と米国黒人史を交互章で辿る系譜小説。"),
    ("インボロ・ンブエ『見よ、夢みる者たちを』", "Imbolo Mbue, Behold the Dreamers", "Behold the Dreamers", "latin", "アフリカ",
     "カメルーン系移民夫婦とリーマンショック期マンハッタン富裕層を交錯させる移民小説。"),
    ("アクウェケ・エメジ『ペット』", "Akwaeke Emezi, Pet", "Pet", "latin", "アフリカ",
     "ナイジェリア系作家のYA小説、絵から現れる存在ペットと黒人少女の正義を巡る寓話。"),
    ("マーザ・メンギステ『シャドウ・キング』", "Maaza Mengiste, The Shadow King", "The Shadow King", "latin", "アフリカ",
     "1935年イタリア=エチオピア戦争を女性兵士の視点から描く、エチオピア系米国作家の歴史小説。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for (nj, ne, no, scr, region, defn) in CONCEPTS:
        try:
            cur.execute("""INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 3, 'A', 'yes')""",
                (nj, ne, no, scr, SUBFIELD_ID, region, PERIOD_ID, defn))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {nj} -> {e}")
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"Total in subfield 20: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
