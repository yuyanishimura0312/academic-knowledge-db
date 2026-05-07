#!/usr/bin/env python3
"""Wave 28 cluster 19: lit_india +30 concepts (5 thematic clusters x 6)."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 12
REGION = "南アジア"

# Period IDs (region='南アジア')
P_CLASSIC_DRAMA = 235   # 古典サンスクリット劇期
P_CLASSIC_KAVYA = 236   # 古典サンスクリット詩学期
P_TAMIL_MED = 237       # タミル中世文学期
P_BENGAL = 134          # ベンガル・ルネサンス期
P_HINDI_PROSE = 239     # ヒンディー散文成熟期
P_URDU = 240            # ウルドゥー近代詩・散文期
P_DALIT_FEM = 245       # インド・ダリット／女性文学期
P_INDOENG = 135         # 印英文学現代期
P_TAMIL_MOD = 242       # タミル近現代文学期
P_SANGAM = 133          # サンガム古典期

CONCEPTS = [
    # Cluster 1: Sanskrit drama (6)
    ("カーリダーサ『シャクンタラー』第四幕", "Kalidasa Shakuntala Act IV", "अभिज्ञानशाकुन्तलम्", "sanskrit", P_CLASSIC_DRAMA, "離別の章。カンヴァが養女シャクンタラーを送り出す場面、サンスクリット詩劇の頂点とされる。"),
    ("バーサ『プラティマー・ナータカ』", "Bhasa Pratima Nataka", "प्रतिमा नाटक", "sanskrit", P_CLASSIC_DRAMA, "ラーマーヤナ題材の彫像劇。バーサ十三戯曲群の代表で古層サンスクリット劇の様式を示す。"),
    ("シュードラカ『ムリッチャカティカー』第五幕", "Sudraka Mrcchakatika", "मृच्छकटिकम्", "sanskrit", P_CLASSIC_DRAMA, "土製小車の劇。遊女ヴァサンタセーナーと貧困バラモンの恋、市井のリアリズムを描く十幕劇。"),
    ("バヴァブーティ『ウッタララーマチャリタ』七幕", "Bhavabhuti Uttararamacharita 7 acts", "उत्तररामचरित", "sanskrit", P_CLASSIC_DRAMA, "ラーマ後伝。シーター追放と再会を描き、悲愴(karuna)ラサの極致と評される。"),
    ("ヴィシャーカダッタ『ムドラーラークシャサ』七幕", "Visakhadatta Mudraraksasa 7 acts", "मुद्राराक्षस", "sanskrit", P_CLASSIC_DRAMA, "印章のラークシャサ。チャーナキヤとラークシャサの政治劇、恋愛を排した稀有な政略劇。"),
    ("ハルシャ『ラトナーヴァリー』", "Harsha Ratnavali", "रत्नावली", "sanskrit", P_CLASSIC_DRAMA, "宝石の首飾り。王ハルシャ作とされる宮廷恋愛劇、ナーティカー型式の典型。"),
    # Cluster 2: Sanskrit kavya/poetics (6)
    ("バーラヴィ『キラータールジュニーヤ』", "Bharavi Kiratarjuniya", "किरातार्जुनीयम्", "sanskrit", P_CLASSIC_KAVYA, "アルジュナとシヴァの戦闘叙事詩。十八歌、五大マハーカーヴィヤの一つで重厚な文体を確立。"),
    ("マーガ『シシュパーラヴァダ』", "Magha Sisupalavadha", "शिशुपालवध", "sanskrit", P_CLASSIC_KAVYA, "シシュパーラ討伐譚。二十歌、技巧と語彙の壮麗さで「マーガに知らぬ語なし」と称される。"),
    ("シュリーハルシャ『ナイシャダチャリタ』", "Sriharsha Naisadhacarita", "नैषधचरितम्", "sanskrit", P_CLASSIC_KAVYA, "ナラ王譚。二十二歌、哲学的議論と難解な語法で後期マハーカーヴィヤの完成形。"),
    ("アーナンダヴァルダナ『ドヴァニャーローカ』", "Anandavardhana Dhvanyaloka", "ध्वन्यालोकः", "sanskrit", P_CLASSIC_KAVYA, "暗示の光。九世紀カシミール、詩の本質を暗示(dhvani)に置く理論で詩学を革新。"),
    ("マンマタ『カーヴィヤプラカーシャ』", "Mammata Kavyaprakasha", "काव्यप्रकाश", "sanskrit", P_CLASSIC_KAVYA, "詩の光。十一世紀の標準的詩学概論、十章構成でラサ・ドヴァニ・修辞を統合。"),
    ("ヴィシュヴァナータ『サーヒティヤダルパナ』", "Visvanatha Sahityadarpana", "साहित्यदर्पण", "sanskrit", P_CLASSIC_KAVYA, "文学の鏡。十四世紀、ラサを詩の魂と定め十章でジャンル論まで包括する詩学綱要。"),
    # Cluster 3: Tamil詳細 (6)
    ("シラッパディカーラム・カーンディ構成", "Cilappatikaram three cantos", "சிலப்பதிகாரம்", "tamil", P_TAMIL_MED, "プハール・マドゥライ・ヴァンチの三カーンディ構成、足輪を巡るカンナギ叙事詩の地理構造。"),
    ("マニメーガライ", "Manimekalai", "மணிமேகலை", "tamil", P_TAMIL_MED, "サッタナール作タミル仏教叙事詩。三十カーンディ、シラッパディカーラムの続編で改宗譚。"),
    ("ティルックラル・三部構成", "Tirukkural three sections", "திருக்குறள்", "tamil", P_SANGAM, "ティルヴァッルヴァル作。アラム(徳)・ポルル(財)・インバム(愛)三部、各クラル二行で1330句。"),
    ("ペリヤ・プラーナム", "Periya Puranam", "பெரிய புராணம்", "tamil", P_TAMIL_MED, "セーッキラール作。六十三ナーヤナール聖者列伝、シャイヴァ・シッダーンタ正典の十二典籍。"),
    ("テーヴァーラム", "Tevaram", "தேவாரம்", "tamil", P_TAMIL_MED, "サンバンダル・アッパル・スンダラル三聖者によるシヴァ讃歌集、シャイヴァ十二典籍冒頭七巻。"),
    ("マーニッカヴァーサガル『ティルヴァーサガム』", "Manikkavasagar Thiruvasagam", "திருவாசகம்", "tamil", P_TAMIL_MED, "聖なる言葉。九世紀シャイヴァ・バクティ詩、五十一篇でシヴァへの神秘的渇望を歌う。"),
    # Cluster 4: 近代 (6)
    ("タゴール『ギーターンジャリ』", "Tagore Gitanjali", "গীতাঞ্জলি", "bengali", P_BENGAL, "歌の捧物。1910年ベンガル語、英訳で1913年ノーベル文学賞、神秘主義的抒情詩集103篇。"),
    ("タゴール『ゴーラ』", "Tagore Gora", "গোরা", "bengali", P_BENGAL, "1910年。アイルランド系孤児ゴーラのアイデンティティを通じインド近代の宗教・国民論を描く長編。"),
    ("プレームチャンド『ゴーダーン』", "Premchand Godan", "गोदान", "hindi", P_HINDI_PROSE, "牛の布施。1936年ヒンディー語、農民ホーリーの悲劇を通じ植民地下農村社会を描く長編。"),
    ("イスマット・チュグタイ『リハーフ（毛布）』", "Ismat Chughtai Lihaaf", "لحاف", "urdu", P_URDU, "1942年ウルドゥー短編。女性同性愛を暗示し猥褻罪で起訴、進歩主義作家運動の象徴作。"),
    ("マントー『トーバー・テーク・スィン』", "Manto Toba Tek Singh", "ٹوبہ ٹیک سنگھ", "urdu", P_URDU, "1955年ウルドゥー短編。分離独立時の精神病院患者交換、狂気を通じ国境の不条理を告発。"),
    ("マハーシュウェター・デーヴィー『ハジャール・チョウラシール・マー』", "Mahasweta Devi Hazaar Chaurasi Ki Maa", "হাজার চুরাশির মা", "bengali", P_DALIT_FEM, "1974年ベンガル語。囚人番号1084の死体ナクサライト青年の母を通じ抑圧された声を描く。"),
    # Cluster 5: 現代 (6)
    ("ヴィクラム・セート『A Suitable Boy』", "Vikram Seth A Suitable Boy", "A Suitable Boy", "latin", P_INDOENG, "1993年英語。1950年代インド四家族の結婚を巡る1349頁の大河小説、英語小説史上最長級。"),
    ("サルマーン・ラシュディ『真夜中の子供たち』", "Salman Rushdie Midnights Children", "Midnight's Children", "latin", P_INDOENG, "1981年。独立瞬間生まれサリーム・シナイの自伝形式、マジックリアリズムでブッカー賞。"),
    ("アニタ・デサイ『澄んだ光の昼』", "Anita Desai Clear Light of Day", "Clear Light of Day", "latin", P_INDOENG, "1980年。デリー旧市街ダース家の四兄妹、分離独立後の時間と記憶をモダニズム手法で描く。"),
    ("キラン・デサイ『喪失の継承』", "Kiran Desai Inheritance of Loss", "The Inheritance of Loss", "latin", P_INDOENG, "2006年ブッカー賞。カリンポンの退職判事と移民料理人の息子、グローバリゼーションの陰影。"),
    ("アルンダティ・ロイ『小さきものたちの神』", "Arundhati Roy God of Small Things", "The God of Small Things", "latin", P_INDOENG, "1997年ブッカー賞。ケーララの双子アンムとラヘル、カースト越境の禁忌と家族崩壊を非線形に描く。"),
    ("ギーターンジャリ・シュリー『砂の墓』", "Geetanjali Shree Tomb of Sand", "रेत समाधि", "hindi", P_DALIT_FEM, "2018年ヒンディー語、英訳が2022年国際ブッカー賞。八十歳女性が分離独立の過去へ越境する。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
        assert len(definition) <= 100, f"def too long ({len(definition)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts
                  (name_ja, name_en, name_original, original_script,
                   subfield_id, region, period_id, definition,
                   importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 4, 'tier1', 'canonical')
            """, (name_ja, name_en, name_orig, script,
                  SUBFIELD_ID, REGION, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
    conn.commit()
    print(f"inserted={inserted} skipped={skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"lit_india total={cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
