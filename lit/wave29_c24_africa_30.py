#!/usr/bin/env python3
"""Wave 29 cluster 24: lit_africa subfield_id=15 — add 30 concepts (5 clusters x 6)."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")

# subfield_id=15 lit_africa, region='アフリカ'
# Period IDs: 80=植民地後期・独立直前, 81=独立期, 64=独立後初期, 149=独立後中期,
#             152=葡語圏アフリカ独立後, 21=現代アラブ文学期, 248=エジプト・スーダン近現代

ROWS = [
    # --- Cluster 1: Anglophone (avoid duplicates with existing) ---
    ("アチェベ『もはや安らぎはない』", "Achebe: No Longer at Ease", "No Longer at Ease", "latin", 64,
     "アチェベ三部作第二作。植民地末期ナイジェリアのオビ・オコンクォの帰国と腐敗を描く。"),
    ("アチェベ『神矢』再読", "Re-reading Arrow of God", "Arrow of God", "latin", 80,
     "イボ祭司エズールと植民地行政の衝突。アチェベ三部作完結篇の批評的再評価。"),
    ("ンギュギ『十字架上の悪魔』", "Ngugi: Devil on the Cross", "Caitaani Mutharaba-ini", "latin", 149,
     "ギクユ語で獄中執筆。資本と新植民地主義を寓話化したンギュギ転換期の代表作。"),
    ("ソインカ『解釈者たち』", "Soyinka: The Interpreters", "The Interpreters", "latin", 64,
     "独立直後ナイジェリアの知識人五人の幻滅を描いた多声的モダニズム小説。"),
    ("チュツオーラ『ヤシ酒飲み』", "Tutuola: Palm-Wine Drinkard", "The Palm-Wine Drinkard", "latin", 80,
     "ヨルバ口承を英語で再話した最初期作品。ピジン的英語と神話的旅路。"),
    ("アディーチェ『アメリカーナ』", "Adichie: Americanah", "Americanah", "latin", 149,
     "ナイジェリア・米国・英国を往還する移民女性イフェメルの愛と人種の物語。"),

    # --- Cluster 2: Francophone ---
    ("センベーヌ『神の森の木片』", "Sembène: Les Bouts de bois de Dieu", "Les Bouts de bois de Dieu", "latin", 80,
     "1947年ダカール=ニジェール鉄道スト史実に基づく仏語圏アフリカ社会主義リアリズムの古典。"),
    ("シェイク・ハミドゥ・カン『曖昧な冒険』再読", "Re-reading L'Aventure ambiguë", "L'Aventure ambiguë", "latin", 80,
     "セネガル少年サンバ・ジャロのコーラン学と西洋教育の引き裂き。実存と霊性の小説。"),
    ("クルマ『ビロアと呼ばれた男』", "Kourouma: Monnè, outrages et défis", "Monnè, outrages et défis", "latin", 149,
     "コートジボワール植民史を口承マンディング語法で描く。クルマ後期作。"),
    ("センゴール『黒い犠牲・連禱』", "Senghor: Hosties noires", "Hosties noires", "latin", 80,
     "第二次大戦に従軍したセネガル兵への鎮魂。ネグリチュード詩の中核作。"),
    ("ビラゴ・ジョップ『新アマドゥ・クンバ物語』", "B. Diop: Nouveaux contes d'Amadou Koumba", "Nouveaux contes", "latin", 80,
     "ウォロフ口承伝統をフランス語に翻訳した寓話集の続篇。動物寓話と祖先知。"),
    ("モンゴ・ベティ『残酷な町』", "Mongo Beti: Ville cruelle", "Ville cruelle", "latin", 80,
     "1954年エザ・ボト名義初作。仏領カメルーン青年バンダの植民地都市体験。"),

    # --- Cluster 3: South African ---
    ("クッツェー『鉄の時代』", "Coetzee: Age of Iron", "Age of Iron", "latin", 149,
     "末期癌の白人女性カレンが息子に書く手紙体小説。アパルトヘイト末期の倫理。"),
    ("ゴーディマー『保護主義者』", "Gordimer: The Conservationist", "The Conservationist", "latin", 149,
     "1974年ブッカー賞。白人実業家メリングと黒人土地霊の幻視。意識の流れ手法。"),
    ("ザケス・ムダ『赤の心』再読", "Re-reading Mda: Heart of Redness", "The Heart of Redness", "latin", 149,
     "1856年コーサ家畜屠殺予言と現代開発を二重化した歴史メタフィクション。"),
    ("ソル・プラーチェ『先住民の生活』", "Plaatje: Native Life in South Africa", "Native Life", "latin", 80,
     "1913年原住民土地法の実態ルポ。プラーチェの政治散文。"),
    ("ブリンク『乾季白い季節』", "Brink: A Dry White Season", "'n Droë wit seisoen", "latin", 149,
     "1979年。アパルトヘイト下白人教師ベンの覚醒と殉教。検閲下アフリカーンス文学。"),
    ("アソル・フガード『ボエスマンとレナ』", "Fugard: Boesman and Lena", "Boesman and Lena", "latin", 64,
     "強制立退き後のカラード夫婦二人芝居。南ア演劇のラディカルな身体性。"),

    # --- Cluster 4: Lusophone ---
    ("ミア・コウト『眠る大地の家系』", "Mia Couto: A Confissão da Leoa", "A Confissão da Leoa", "latin", 152,
     "モザンビーク北部での女性襲撃ライオン伝承を多声で書く。コウト後期作。"),
    ("ペペテーラ『マヨンベ』再読", "Re-reading Pepetela: Mayombe", "Mayombe", "latin", 152,
     "アンゴラ独立戦争MPLAゲリラ部隊。革命と部族アイデンティティの葛藤。"),
    ("アグアルーザ『一般忘却理論』", "Agualusa: Teoria Geral do Esquecimento", "Teoria Geral do Esquecimento", "latin", 152,
     "アンゴラ独立期にアパートに自閉した白人女性ルドの28年。記憶と国家の寓話。"),
    ("チジアネ『ニケッチ：一夫多妻物語』", "Chiziane: Niketche", "Niketche: Uma História de Poligamia", "latin", 152,
     "南北モザンビークの一夫多妻文化と女性解放を描いたフェミニズム小説。"),
    ("ホンワナ『私たちは犬を殺した』再読", "Re-reading Honwana: Nós matámos o Cão-Tinhoso", "Nós matámos o Cão-Tinhoso", "latin", 80,
     "モザンビーク植民地末期の少年視点短篇集。葡語圏アフリカ短篇の規範作。"),
    ("クラヴェイリーニャ『カリンガナ・ウア・カリンガナ』", "Craveirinha: Karingana ua Karingana", "Karingana ua Karingana", "latin", 64,
     "モザンビーク詩。ロンガ語語り起こし定型を葡語詩に移植したアフリカニズモ。"),

    # --- Cluster 5: Maghreb + Egypt ---
    ("マフフーズ『ハーン・ハリーリー』", "Mahfouz: Khan al-Khalili", "خان الخليلي", "arabic", 248,
     "1945年作。第二次大戦下カイロの中流家庭兄弟の挫折。マフフーズ初期写実主義。"),
    ("タハール・ベン・ジェルーン『砂の子』", "Ben Jelloun: L'Enfant de sable", "L'Enfant de sable", "latin", 149,
     "モロッコの八番目娘を息子として育てる父。語り手交替のポストモダン小説。"),
    ("ハティビ『刺青の記憶』", "Khatibi: La Mémoire tatouée", "La Mémoire tatouée", "latin", 149,
     "モロッコ自伝小説。アラビア語と仏語の二言語性を「他者の思考」として理論化。"),
    ("ジェバール『アルジェの女たちの部屋にて』再読", "Re-reading Djebar: Femmes d'Alger", "Femmes d'Alger", "latin", 149,
     "ドラクロワ絵画への返答。植民地視線下のアルジェリア女性身体の解放。"),
    ("メンゲステ『獅子の足元に』", "Mengiste: Beneath the Lion's Gaze", "Beneath the Lion's Gaze", "latin", 149,
     "1974年エチオピア革命とデルグ独裁を医師家族から描く。歴史小説の傑作。"),
    ("ハビラ『旅する者たち』", "Habila: Travelers", "Travelers", "latin", 149,
     "ナイジェリア出身作家がベルリン他で出会うアフリカ移民六話。21世紀移民文学。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in ROWS:
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, original_script, subfield_id, region,
                    period_id, definition, importance_score, source_tier, canonical_in_region)
                   VALUES (?, ?, ?, ?, 15, 'アフリカ', ?, ?, 4, 'A', 'yes')""",
                (name_ja, name_en, name_orig, script, period_id, definition),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"  SKIP: {name_ja} -- {e}")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
