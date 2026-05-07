#!/usr/bin/env python3
"""Wave 37: lit_arabic (id=13) niche +30 concepts."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# (name_ja, name_en, name_original, original_script, period_id, definition)
# Periods: 16=Jahiliyya, 18=Abbasid, 19=Postmongol/Mamluk, 21=Modern, 139=Andalus, 140=Mamluk-Ottoman
ROWS = [
    # Cluster 1: 古典アラブ詩細部 (Mu'allaqat 6)
    ("イムルウル・カイス『ムアッラカ』詳細解読", "Imru' al-Qais Mu'allaqa close reading", "معلقة امرئ القيس", "arabic", 16,
     "懸詩冒頭の名作。廃墟前奏ナスィーブから恋愛・狩猟・嵐描写へ展開する古典詩の規範。"),
    ("ラビード『ムアッラカ』遊牧詠", "Labid Mu'allaqa nomadic ode", "معلقة لبيد", "arabic", 16,
     "廃墟描写と部族倫理を結ぶ詩。砂漠生活の循環と無常観を象徴的に表現する代表作。"),
    ("タラファ『ムアッラカ』ラクダ詩学", "Tarafa Mu'allaqa camel imagery", "معلقة طرفة", "arabic", 16,
     "ラクダ描写の長大な比喩で名高い懸詩。若き詩人の死生観と享楽哲学を併存させる。"),
    ("アンタラ『ムアッラカ』英雄叙事", "'Antara Mu'allaqa heroic ode", "معلقة عنترة", "arabic", 16,
     "黒人英雄詩人アンタラの自賛・恋愛・戦闘を統合した懸詩。後世の英雄譚の原型。"),
    ("ズハイル『ムアッラカ』倫理哲学詩", "Zuhayr Mu'allaqa ethical wisdom", "معلقة زهير", "arabic", 16,
     "和解と平和の倫理を説く格言的懸詩。アラブ詩における賢者の声の典型を示す。"),
    ("アムル・イブン・クルスーム『ムアッラカ』部族自賛", "'Amr ibn Kulthum Mu'allaqa fakhr", "معلقة عمرو", "arabic", 16,
     "タグリブ族の誇りを高唱する自賛詩。部族集団的アイデンティティの詩的結晶。"),

    # Cluster 2: アッバース朝詩 (6)
    ("アブー・ヌワース・ハムリーヤート酒詩集", "Abu Nuwas khamriyyat wine poems", "خمريات أبي نواس", "arabic", 18,
     "ジャーヒリーヤ詩規範を覆す酒讃歌群。都市的快楽と異教的洗練を結ぶアッバース朝詩革新。"),
    ("アブー・タンマーム『ハマーサ』詞華集", "Abu Tammam Hamasah anthology", "حماسة أبي تمام", "arabic", 18,
     "勇武・哀歌・賛美等10章編成の古典詩アンソロジー。後世詩学の規範教材となる。"),
    ("アル＝ブフトゥリー・カスィーダ集", "al-Buhturi qasida collection", "ديوان البحتري", "arabic", 18,
     "イーワーン・キスラー描写で名高いカスィーダ詩人。建築・自然詠の精緻な描写力。"),
    ("ムタナッビー・サイフィーヤート", "al-Mutanabbi Sayfiyyat panegyric", "سيفيات المتنبي", "arabic", 18,
     "サイフ・ダウラに捧げた賛歌群。アラブ詩史最高峰とされる修辞・思想の凝縮詩。"),
    ("マアッリー『サクト・アッ＝ザンド』初期詩集", "al-Ma'arri Saqt al-Zand", "سقط الزند", "arabic", 18,
     "マアッリー若年期の詩集。古典詩規範に従う形式美と懐疑的思索の萌芽を併せ持つ。"),
    ("イブン・アル＝ルーミー諷刺詩", "Ibn al-Rumi satirical poetry", "ديوان ابن الرومي", "arabic", 18,
     "心理描写と長大な比喩で知られる詩人。鋭利な諷刺と内省的悲嘆を併存させる作風。"),

    # Cluster 3: アンダルス・マグレブ (6)
    ("イブン・ハズム『鳩の頸飾り』恋愛論", "Ibn Hazm Tawq al-Hamama love treatise", "طوق الحمامة", "arabic", 139,
     "アンダルス散文の名作。恋愛の段階・症状・倫理を逸話で論じる人類学的恋愛論。"),
    ("イブン・クズマーン・ザジャル詩集", "Ibn Quzman zajal diwan", "ديوان ابن قزمان", "arabic", 139,
     "アンダルス俗語ザジャル詩の頂点。アラビア俗語と恋愛・酒・諷刺主題を融合させる。"),
    ("イブン・ザイドゥーン『ヌーニーヤ』", "Ibn Zaydun Nuniyya", "نونية ابن زيدون", "arabic", 139,
     "ワッラーダへ捧げた哀切な恋愛詩。アンダルス宮廷詩の代表的恋愛叙情詩。"),
    ("イブン・ハファージャ自然詩", "Ibn Khafaja nature poetry", "ديوان ابن خفاجة", "arabic", 139,
     "アンダルス庭園詩の達人。「庭園のシャイフ」と呼ばれた緑と河川の精細描写詩。"),
    ("ムウタミド・イブン・アッバード王詩", "al-Mu'tamid King of Seville poems", "ديوان المعتمد", "arabic", 139,
     "セビリャ王の詩集。栄華と幽閉後の悲嘆を主題とする運命の落差を詠じた王者詩。"),
    ("イブン・アラビー『タルジュマーン』恋愛詩", "Ibn 'Arabi Tarjuman al-Ashwaq", "ترجمان الأشواق", "arabic", 139,
     "スーフィー恋愛詩集。世俗的恋愛詩語彙で神秘的合一を寓意的に表現した名詩集。"),

    # Cluster 4: 散文古典 (6)
    ("ジャーヒズ『ブハラー』吝嗇者列伝", "Jahiz Bukhala stingy anecdotes", "كتاب البخلاء", "arabic", 18,
     "吝嗇者の逸話・対話・分析を集めた社会観察散文。アダブ文学の風刺的代表作。"),
    ("タウヒーディー『イムターウ』対話文学", "Tawhidi Imta' wa Mu'anasa", "الإمتاع والمؤانسة", "arabic", 18,
     "37夜にわたる宮廷夜話集。哲学・文芸・人物批評を縦横に語る対話散文の傑作。"),
    ("ハリーリー『マカーマート』詳細50篇", "Hariri Maqamat 50 sessions", "مقامات الحريري", "arabic", 18,
     "巧緻な押韻散文と語彙遊戯で50篇を構成。古典マカーマ文学の規範的頂点作。"),
    ("ハマザーニー『マカーマート』創始", "Hamadhani Maqamat foundational", "مقامات الهمذاني", "arabic", 18,
     "マカーマ形式の創始作。詐欺師主人公と語り手の枠物語による押韻散文の原型。"),
    ("イブン・トゥファイル『ハイイ・イブン・ヤクザーン』哲学小説", "Ibn Tufayl Hayy ibn Yaqzan", "حي بن يقظان", "arabic", 139,
     "孤島で独学する人間の認識発展を描く哲学物語。アラブ・ビルドゥングスロマン原型。"),
    ("ジュルジー・ザイダーン歴史小説群", "Jurji Zaydan historical novels", "روايات جرجي زيدان", "arabic", 20,
     "イスラーム史を題材とした22冊の歴史小説。近代アラブ歴史小説ジャンル創始作群。"),

    # Cluster 5: 近現代アラブ (6)
    ("マフフーズ『カイロ三部作』詳細", "Mahfouz Cairo Trilogy detailed", "الثلاثية", "arabic", 21,
     "20世紀前半カイロの一家族三世代を描く大河小説。アラブ近代リアリズムの金字塔。"),
    ("タイイブ・サーリフ『北方移住の季節』", "Tayeb Salih Season of Migration to the North", "موسم الهجرة إلى الشمال", "arabic", 21,
     "スーダン人の英国体験を描くポストコロニアル小説。植民地的欲望と暴力の解剖。"),
    ("カナファーニー『ハイファに戻って』", "Ghassan Kanafani Returning to Haifa", "عائد إلى حيفا", "arabic", 21,
     "1967年後パレスチナ人帰郷を描く中編。喪失・記憶・抵抗の倫理を凝縮する。"),
    ("ハナーン・アッ＝シャイフ『ザフラの物語』", "Hanan al-Shaykh Story of Zahra", "حكاية زهرة", "arabic", 21,
     "レバノン内戦下女性の身体・狂気・性を描くフェミニズム小説の里程標的作品。"),
    ("アドゥニース『アル＝キターブ』三巻", "Adunis al-Kitab three volumes", "الكتاب", "arabic", 21,
     "ムタナッビーを声として召喚するアラブ詩史の壮大な再書。三巻からなる長大詩。"),
    ("マフムード・ダルウィーシュ『壁画』", "Mahmoud Darwish Mural", "جدارية", "arabic", 21,
     "瀕死体験を経た詩人の長詩。死・生・パレスチナを宇宙的視野で詠じる晩年代表作。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_original, script, period_id, definition in ROWS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 13, '西アジア', ?, ?, 3, 'B', 'arab')
            """, (name_ja, name_en, name_original, script, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} ({e})", file=sys.stderr)
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=13")
    print(f"Total lit_arabic: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
