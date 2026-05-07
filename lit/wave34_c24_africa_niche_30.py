#!/usr/bin/env python3
"""Wave 34 C24: lit_africa niche 30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 15
REGION = "アフリカ"

# (name_ja, name_en, name_original, original_script, period_id, definition, importance, tier)
CONCEPTS = [
    # Cluster 1: 西アフリカ詳細
    ("マリアマ・バー『かくも長き手紙』", "Mariama Bâ 'Une si longue lettre'", "Une si longue lettre", "latin", 149, "セネガル女性作家による書簡体小説。一夫多妻制下の女性の声を描く西アフリカ・フェミニズム文学の古典。", 5, "tier1"),
    ("アミナタ・ソウ・ファル『乞食たちのストライキ』", "Aminata Sow Fall 'La Grève des Bàttu'", "La Grève des Bàttu", "latin", 149, "セネガル作家の風刺小説。乞食のストライキで都市の偽善を暴く。アフリカ女性作家の批評的散文。", 4, "tier1"),
    ("センベーヌ『ヴェイ＝チョザーヌ』", "Sembène Ousmane 'Vehi-Ciosane'", "Vehi-Ciosane", "latin", 64, "ウォロフ村落の近親相姦タブーを描く中編。植民地後の道徳危機を口承的語りで描出した。", 4, "tier1"),
    ("カリクスト・ベヤラ『日が私を焼いた』", "Calixthe Beyala 'C'est le soleil qui m'a brûlée'", "C'est le soleil qui m'a brûlée", "latin", 149, "カメルーン女性作家の処女作。都市スラムの少女の身体と性を生々しく描いたアフリフェミニズムの代表作。", 4, "tier1"),
    ("ウェレウェレ・リキング『碧玉の彼女』", "Werewere Liking 'Elle sera de jaspe et de corail'", "Elle sera de jaspe et de corail", "latin", 149, "カメルーン作家のシャン・ロマン（歌＝小説）。儀礼・詩・散文を融合した汎アフリカ的女性ユートピア。", 4, "tier2"),
    ("ベン・オクリ『満たされぬ道』", "Ben Okri 'The Famished Road'", "The Famished Road", "latin", 150, "ナイジェリア作家のブッカー賞受賞作。アビク（霊児）視点でマジックリアリズムとヨルバ宇宙観を融合。", 5, "tier1"),
    # Cluster 2: 東アフリカ
    ("ンギュギ『血の花弁』", "Ngugi wa Thiong'o 'Petals of Blood'", "Petals of Blood", "latin", 149, "ケニア独立後の腐敗と農民抑圧を四人の視点で描く政治小説。マルクス主義リアリズムの東アフリカ代表作。", 5, "tier1"),
    ("オコト・ビテック『ラウィノの歌』", "Okot p'Bitek 'Song of Lawino'", "Wer pa Lawino", "latin", 64, "ウガンダ詩人のアチョリ語長詩。西洋化した夫を批判する妻の声で、口承詩学と反植民地批評を融合。", 5, "tier1"),
    ("メジャ・ムワンギ『早く殺して』", "Meja Mwangi 'Kill Me Quick'", "Kill Me Quick", "latin", 149, "ナイロビのストリート青年を描くケニア都市小説。アフリカ社会派リアリズムと貧困表象の典型。", 3, "tier2"),
    ("M.G.ヴァサンジ『一等席にて』", "M.G. Vassanji 'In-Between World of Vikram Lall'", "In Place of First Class", "latin", 150, "東アフリカ・インド系ディアスポラ視点でケニア独立史を描く。アフリカン・アジアン文学の代表作。", 4, "tier2"),
    ("イヴォンヌ・オウオール『塵』", "Yvonne Owuor 'Dust'", "Dust", "latin", 150, "ケニア現代作家のデビュー作。トゥルカナ砂漠を舞台に独立後ケニアの暴力と記憶を抒情的に描く。", 4, "tier2"),
    ("ヌルディン・ファラー『マップス』", "Nuruddin Farah 'Maps'", "Maps", "latin", 149, "ソマリア作家三部作の第一作。オガデン戦争下の少年の身体・国家・地図の関係を二人称で問う。", 5, "tier1"),
    # Cluster 3: 中央+南アフリカ
    ("ペペテーラ『ヤカ』", "Pepetela 'Yaka'", "Yaka", "latin", 152, "アンゴラ作家による100年史小説。ベンゲラ植民史を一族五世代で描く葡語圏アフリカの叙事詩。", 4, "tier1"),
    ("ミア・コウト『夜に作られた声』", "Mia Couto 'Voices Made Night'", "Vozes Anoitecidas", "latin", 152, "モザンビーク作家の短編集。葡語にバントゥ語法を混淆した言語実験で内戦下の村落を描く。", 5, "tier1"),
    ("ベシー・ヘッド『雨雲が集まるとき』", "Bessie Head 'When Rain Clouds Gather'", "When Rain Clouds Gather", "latin", 64, "ボツワナに亡命した南ア作家の処女作。ジャーナル村の協同農業実験を描く脱植民地ユートピア小説。", 4, "tier1"),
    ("ゴーディマー『バーガーの娘』", "Nadine Gordimer 'Burger's Daughter'", "Burger's Daughter", "latin", 149, "南アフリカのアパルトヘイト下、共産党活動家の娘の政治的覚醒を描く。ノーベル賞作家の代表長編。", 5, "tier1"),
    ("ゾーイ・ウィカム『ユー・キャント・ゲット・ロスト』", "Zoë Wicomb 'You Can't Get Lost in Cape Town'", "You Can't Get Lost in Cape Town", "latin", 149, "南ア・カラード女性作家の連作短編。ケープタウンの混血アイデンティティと女性の身体を描く。", 4, "tier2"),
    ("ツィツィ・ダンガレンガ『ナーヴァス・コンディションズ』", "Tsitsi Dangarembga 'Nervous Conditions'", "Nervous Conditions", "latin", 149, "ジンバブエ女性作家のビルドゥングスロマン。植民地教育下の少女の二重意識を描く現代古典。", 5, "tier1"),
    # Cluster 4: 北アフリカ
    ("ドリス・シュライービ『単純な過去』", "Driss Chraïbi 'Le Passé Simple'", "Le Passé Simple", "latin", 64, "モロッコ作家の処女作。父権的伝統と西洋近代の間で引き裂かれる青年を描くマグレブ文学の出発点。", 5, "tier1"),
    ("タハール・ベン・ジェルーン『聖なる夜』", "Tahar Ben Jelloun 'La Nuit Sacrée'", "La Nuit Sacrée", "latin", 149, "モロッコ作家のゴンクール賞受賞作。男装で育てられた女性の解放譚。マグレブ仏語文学の代表作。", 5, "tier1"),
    ("アシア・ジェバール『アルジェの女たち』", "Assia Djebar 'Femmes d'Alger dans leur appartement'", "Femmes d'Alger dans leur appartement", "latin", 149, "アルジェリア女性作家の連作短編。ドラクロワ絵画を起点にアラブ女性の声と視線を回復する。", 5, "tier1"),
    ("ヤスミナ・カドラ『カブールの燕たち』", "Yasmina Khadra 'Les Hirondelles de Kaboul'", "Les Hirondelles de Kaboul", "latin", 150, "アルジェリア作家のタリバン下カブールを描く三部作の一作。マグレブ作家のグローバル・イスラーム表象。", 4, "tier2"),
    ("モハメッド・ショクリ『パンだけのために』", "Mohammed Choukri 'For Bread Alone'", "Al-khubz al-Hafi", "arabic", 149, "モロッコ作家の自伝的小説。タンジールのスラム少年の暴力と性をアラビア語で赤裸々に描く。", 4, "tier1"),
    ("ブアレム・サンサル『2084』", "Boualem Sansal '2084: La fin du monde'", "2084: La fin du monde", "latin", 150, "アルジェリア作家のディストピア。オーウェル『1984』を継承しイスラーム全体主義を風刺した寓話。", 4, "tier2"),
    # Cluster 5: ナイジェリア新世代
    ("ヘロン・ハビラ『天使を待ちながら』", "Helon Habila 'Waiting for an Angel'", "Waiting for an Angel", "latin", 150, "ナイジェリア作家のアバチャ独裁下ラゴスを描く連作。第三世代ナイジェリア小説の代表作。", 4, "tier2"),
    ("セフィ・アッタ『すべて良くなる』", "Sefi Atta 'Everything Good Will Come'", "Everything Good Will Come", "latin", 150, "ナイジェリア女性作家のビルドゥングスロマン。1970年代以降のラゴスで女性二人の友情と政治を描く。", 4, "tier2"),
    ("テジュ・コール『オープン・シティ』", "Teju Cole 'Open City'", "Open City", "latin", 150, "ナイジェリア系米国作家の遊歩者小説。NYと欧州を歩く精神科医の意識流でディアスポラと記憶を描く。", 5, "tier1"),
    ("チブンドゥ・オヌゾ『ようこそラゴスへ』", "Chibundu Onuzo 'Welcome to Lagos'", "Welcome to Lagos", "latin", 150, "ナイジェリア女性作家の都市群像劇。ニジェールデルタからラゴスへの五人の逃亡者を描く現代小説。", 3, "tier2"),
    ("アクワエケ・エメジ『フレッシュウォーター』", "Akwaeke Emezi 'Freshwater'", "Freshwater", "latin", 150, "ナイジェリア＝タミル系作家。イボのオグバンジェ霊概念で多重人格と性的アイデンティティを描く。", 4, "tier2"),
    ("ンネディ・オコラフォー『ビンティ』", "Nnedi Okorafor 'Binti'", "Binti", "latin", 150, "ナイジェリア系米国作家のヒューゴー＝ネビュラ賞SF三部作。ヒンバ族少女の宇宙旅行アフロフューチャリズム。", 4, "tier1"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for (nj, ne, no, ns, pid, dfn, imp, tier) in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nj, ne, no, ns, SUBFIELD_ID, REGION, pid, dfn, imp, tier, "yes" if tier == "tier1" else "no"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {nj}: {e}")
            skipped += 1
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"Total lit_africa concepts: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
