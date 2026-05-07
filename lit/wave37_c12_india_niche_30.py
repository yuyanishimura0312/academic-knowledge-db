#!/usr/bin/env python3
"""Wave37 c12 India niche 30 concepts."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# (name_ja, name_en, name_original, original_script, period_id, definition)
ROWS = [
    # 1. サンスクリット詩細部 (period 236 古典サンスクリット詩学期 / 235 古典サンスクリット劇期)
    ("マーガ『シシュパーラヴァダ』詳論", "Magha Shishupala-vadha detailed", "शिशुपालवध", "sanskrit", 236,
     "7世紀マーガ作・20歌のマハーカーヴィヤ。クリシュナのシシュパーラ討伐を技巧的二重表現で叙す。"),
    ("シュリーハルシャ『ナイシャダチャリタ』詳論", "Sri Harsha Naishadhiya detailed", "नैषधीयचरित", "sanskrit", 236,
     "12世紀シュリーハルシャ作・22歌のマハーカーヴィヤ。ナラ王とダマヤンティーの恋を哲学的修辞で展開。"),
    ("バッティ『バッティカーヴィヤ』", "Bhatti-kavya Ravanavadha", "भट्टिकाव्य", "sanskrit", 236,
     "7世紀バッティ作の文法例示型カーヴィヤ。ラーマ物語を題材にパーニニ文法規則を実例化する。"),
    ("バーラヴィ『キラータールジュニーヤ』詳論", "Bharavi Kiratarjuniya detailed", "किरातार्जुनीय", "sanskrit", 236,
     "6世紀バーラヴィ作・18歌。キラータ姿のシヴァとアルジュナの闘いを濃密な修辞で叙述する。"),
    ("バーナバッタ『カーダンバリー』詳論", "Bana Kadambari detailed", "कादम्बरी", "sanskrit", 236,
     "7世紀バーナバッタ作・サンスクリット散文ロマンスの最高峰。前世譚を重層化した複雑物語。"),
    ("ダンディン『ダシャクマーラチャリタ』詳論", "Dandin Dashakumaracarita detailed", "दशकुमारचरित", "sanskrit", 236,
     "7-8世紀ダンディン作。十王子の冒険譚を散文で描く社会描写豊かなアーキャーイカー作品。"),

    # 2. ドラマ古典 (period 235)
    ("バーサ『スヴァプナヴァーサヴァダッタ』", "Bhasa Svapnavasavadatta", "स्वप्नवासवदत्त", "sanskrit", 235,
     "バーサ作6幕劇。ウダヤナ王と王妃ヴァーサヴァダッターの再会を夢の場面で描く古劇傑作。"),
    ("バーサ『マディヤマヴィヤーヨーガ』", "Bhasa Madhyamavyayoga", "मध्यमव्यायोग", "sanskrit", 235,
     "バーサ作一幕ヴィヤーヨーガ劇。マハーバーラタを基にビーマと中の子ガトートカチャの邂逅を描く。"),
    ("シュードラカ『ムリッチャカティカー』詳論", "Sudraka Mrcchakatika detailed", "मृच्छकटिक", "sanskrit", 235,
     "5世紀頃シュードラカ作10幕プラカラナ。バラモンと遊女の恋を背景に庶民生活と政治陰謀を描く。"),
    ("ヴィシャーカダッタ『ムドラーラークシャサ』詳論", "Vishakhadatta Mudrarakshasa detailed", "मुद्राराक्षस", "sanskrit", 235,
     "ヴィシャーカダッタ作7幕劇。チャーナキヤとラークシャサの政治謀略を恋愛排しナータカで展開。"),
    ("バヴァブーティ『ウッタララーマチャリタ』詳論", "Bhavabhuti Uttararamacarita detailed", "उत्तररामचरित", "sanskrit", 235,
     "8世紀バヴァブーティ作7幕劇。シーター追放後を哀感のラサで描く感傷的後期サンスクリット劇。"),
    ("ラージャシェーカラ『カルプーラマンジャリー』", "Rajashekhara Karpuramanjari", "कर्पूरमञ्जरी", "sanskrit", 235,
     "10世紀ラージャシェーカラ作のサッタカ劇。プラークリットのみで上演される稀有な恋愛喜劇。"),

    # 3. バクティ運動 (period 132 / 267)
    ("トゥカーラーム『アバンガ・ガーター』詳論", "Tukaram Abhanga Gatha detailed", "अभंग गाथा", "sanskrit", 132,
     "17世紀マラーティー詩聖トゥカーラームの数千篇のアバンガ集。ヴィッタル神への帰依を口語で表現。"),
    ("エクナート『バーガヴァタ』", "Eknath Bhagavata", "एकनाथी भागवत", "sanskrit", 132,
     "16世紀エクナート作マラーティー語『バーガヴァタ・プラーナ』第11巻注釈。1万8千詩節の大作。"),
    ("スールダース『スールサーガル』詳論", "Surdas Sursagar detailed", "सूरसागर", "sanskrit", 132,
     "16世紀盲目詩人スールダース作のブラジ語讃歌集。クリシュナ幼児期描写ヴァーツァリヤ・バクティの極致。"),
    ("ミーラーバーイー バジャン集成", "Mirabai bhajan corpus", "मीरा भजन", "sanskrit", 132,
     "16世紀ラージプート王妃ミーラーのクリシュナ讃歌群。女性身体性と禁忌越境の恋愛バクティ詩。"),
    ("カビール『ドーハー』詳論", "Kabir doha detailed", "कबीर दोहा", "sanskrit", 267,
     "15世紀カビールの二行詩。ヒンドゥー・イスラーム両者を批判する逆説的・諷刺的霊的訓戒詩。"),
    ("トゥルシーダース『ラームチャリトマーナス』詳論", "Tulsidas Ramcharitmanas detailed", "रामचरितमानस", "sanskrit", 132,
     "16世紀トゥルシーダース作アワディー語ラーマ叙事詩。7カーンダ・北インド民衆ラーマ信仰の聖典。"),

    # 4. 近代インド多言語 (period 239 / 240 / 137 / 241)
    ("プレームチャンド『ゴーダーン』詳論", "Premchand Godan detailed", "गोदान", "sanskrit", 239,
     "1936年プレームチャンド作ヒンディー長編。農民ホーリーの牛布施願望を通じカースト・債務制を描く。"),
    ("マントー『トーバー・テーク・スィン』詳論", "Manto Toba Tek Singh detailed", "ٹوبہ ٹیک سنگھ", "arabic", 240,
     "1955年マントー作ウルドゥー短編。分離独立後の精神病院患者交換を通じ国境の不条理を寓話化。"),
    ("マハーシュウェター・デーヴィー『ハジャール・チョウラシーマー』詳論", "Mahasweta Devi Hazaar Chaurasi Ki Maa detailed", "হাজার চুরাশির মা", "other", 137,
     "1974年作ベンガル長編。ナクサライト運動で死んだ息子の母の追想を通じ国家暴力と階級を告発。"),
    ("クリシュナ・ソーバティー『ジンダギーナーマー』", "Krishna Sobti Zindaginama", "ज़िन्दगीनामा", "sanskrit", 239,
     "1979年作ヒンディー長編。20世紀初頭パンジャーブ村落を多声的散文で描く分離独立前夜の風土誌。"),
    ("テンドゥルカル『サカーラーム・バインダル』詳論", "Tendulkar Sakharam Binder detailed", "सखाराम बाइंडर", "sanskrit", 241,
     "1972年テンドゥルカル作マラーティー戯曲。家父長的暴力と女性の交換を露骨に描き上演禁止騒動。"),
    ("ガールシュ・カルナード『トゥグラク』詳論", "Girish Karnad Tughlaq detailed", "ತುಘಲಕ್", "other", 244,
     "1964年カルナード作カンナダ戯曲13場。理想主義的暴君ムハンマド・トゥグラクをネルー期へ重ね描く。"),

    # 5. 英語インド・ディアスポラ (period 135)
    ("ラシュディ『真夜中の子供たち』詳論", "Salman Rushdie Midnight's Children detailed", "Midnight's Children", "latin", 135,
     "1981年ラシュディ作。1947年深夜0時生サリームを語り手にマジックリアリズムでインド独立史を描く。"),
    ("ヴィクラム・セート『A Suitable Boy』詳論", "Vikram Seth A Suitable Boy detailed", "A Suitable Boy", "latin", 135,
     "1993年セート作1349頁長編。1950年代北インドで娘の婿探しを軸に四家族と新興国家を描く大河小説。"),
    ("アミタヴ・ゴーシュ『アイビス三部作』", "Amitav Ghosh Ibis Trilogy", "Ibis Trilogy", "latin", 135,
     "Sea of Poppies/River of Smoke/Flood of Fire三部作。アヘン戦争期インド洋世界を多言語で描く。"),
    ("アルンダティ・ロイ『至福の南』", "Arundhati Roy Ministry of Utmost Happiness", "The Ministry of Utmost Happiness", "latin", 135,
     "2017年ロイ作20年ぶり長編。ヒジュラとカシミール紛争を交差させ周縁者の連帯を描く政治小説。"),
    ("キラン・デサイ『喪失の継承』詳論", "Kiran Desai Inheritance of Loss detailed", "The Inheritance of Loss", "latin", 135,
     "2006年デサイ作ブッカー賞作。ダージリンのゴルカランド運動とニューヨーク移民労働を交錯させる。"),
    ("ジュンパ・ラーヒリ『低地』", "Jhumpa Lahiri The Lowland", "The Lowland", "latin", 135,
     "2013年ラーヒリ作長編。1960年代カルカッタのナクサライト運動と米国移民の兄弟を半世紀追う。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, pid, definition in ROWS:
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                                      subfield_id, region, period_id, definition,
                                      importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 12, '南アジア', ?, ?, 3, 'tier2', 'niche')
            """, (name_ja, name_en, name_orig, script, pid, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped}")

if __name__ == "__main__":
    main()
