#!/usr/bin/env python3
"""Wave 29 cluster 21: Arabic literature 30 concepts (subfield_id=13)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# region uses '西アジア' per CHECK on concepts.region
REGION = "南西アジア"
SUBFIELD = 13

# (name_ja, name_en, name_original, period_id, definition, importance, fourth_status)
ROWS = [
    # 1. ジャーヒリーヤ (period 16)
    ("イムルウル・カイス『ムアッラカ』詩学分析", "Imru' al-Qais Mu'allaqa Poetics", "معلقة امرئ القيس",
     16, "前イスラーム期キンダ族の長編カスィーダ。ナスィーブと砂漠描写で懸詩の規範を確立。", 5, "invariant"),
    ("タラファ『ムアッラカ』ラクダ描写", "Tarafa Mu'allaqa Camel Ode", "معلقة طرفة",
     16, "若年詩人タラファによる懸詩。ラクダ描写と人生哲学的瞑想で名高い。", 4, "invariant"),
    ("ズハイル『ムアッラカ』倫理詩学", "Zuhayr Mu'allaqa Ethical Verse", "معلقة زهير",
     16, "倫理的格言と平和称揚を特徴とする懸詩。ヒクマ詩の源流。", 4, "invariant"),
    ("ラビード『ムアッラカ』廃墟詩", "Labid Mu'allaqa Atlal", "معلقة لبيد",
     16, "アトラール（廃墟）モチーフを精緻化した懸詩。無常観の表現で後世に影響。", 4, "invariant"),
    ("アンタラ『ムアッラカ』英雄詩学", "Antara Mu'allaqa Heroic", "معلقة عنترة",
     16, "黒人騎士アンタラによる懸詩。ファフル（自賛）と恋慕アブラを織り合わせる。", 4, "invariant"),
    ("ハッサーン・イブン・サービト預言者称揚詩", "Hassan ibn Thabit Prophetic Praise", "حسان بن ثابت",
     16, "預言者ムハンマド付きの詩人。マディーフをイスラーム的価値に転用した。", 4, "partial"),

    # 2. アッバース朝 (period 18)
    ("アブー・ヌワース・ハムリーヤート", "Abu Nuwas Khamriyyat", "خمريات أبي نواس",
     18, "アッバース朝の酒詩ジャンル。バッカナリアと反規範美学を融合した代表作群。", 5, "rethinking"),
    ("バッシャール・イブン・ブルド・ムフダス革新", "Bashshar Muhdath Innovation", "بشار بن برد",
     18, "盲目のペルシア系詩人。ムフダス（新派）詩学の先駆者で修辞革新を担った。", 4, "partial"),
    ("アブー・アル＝アターヒヤ・ズフド詩", "Abu al-Atahiya Zuhdiyyat", "أبو العتاهية",
     18, "禁欲詩（ズフディーヤ）の創始者。死と無常の主題を平易な言葉で歌った。", 4, "invariant"),
    ("アル＝ブフトゥリー・カスィーダ建築描写", "al-Buhturi Iwan Kisra Ode", "البحتري",
     18, "アッバース朝詩人。サーサーン宮殿イーワーン詩で歴史的廃墟詩学を完成。", 4, "invariant"),
    ("シャリーフ・アル＝ラディー・恋愛詩", "Sharif al-Radi Ghazal", "الشريف الرضي",
     18, "シーア派貴族詩人・『ナフジュ・バラーガ』編者。優雅なガザルで知られる。", 4, "invariant"),
    ("ミフヤール・アッ＝ダイラミー詩", "Mihyar al-Daylami Diwan", "مهيار الديلمي",
     18, "アル＝ラディー門下のペルシア系詩人。古典的ファサーハの継承で高評価。", 3, "invariant"),

    # 3. 散文古典 (period 18)
    ("イブン・アル＝ムカッファ翻訳文体", "Ibn al-Muqaffa Translation Style", "ابن المقفع",
     18, "『カリーラとディムナ』翻訳でアラビア散文文体を樹立した翻訳家。", 5, "invariant"),
    ("ジャーヒズ『ブハラー』吝嗇文学", "al-Jahiz Bukhala Anecdotes", "البخلاء للجاحظ",
     18, "吝嗇者の逸話集。アダブ散文と社会観察を融合した古典。", 5, "invariant"),
    ("イブン・クタイバ『アダブ・アル＝カーティブ』書記教養", "Ibn Qutayba Adab al-Katib", "أدب الكاتب",
     18, "書記官のための言語・修辞教本。アダブ（教養文学）の規範書。", 4, "invariant"),
    ("サアーリビー『ヤティーマト・アッ＝ダフル』詩人列伝", "Tha'alibi Yatimat al-Dahr", "يتيمة الدهر",
     18, "10-11世紀の同時代詩人辞典。アンソロジー兼批評の古典資料。", 4, "invariant"),
    ("マスウーディー『黄金の牧場』歴史地理", "al-Mas'udi Muruj al-Dhahab", "مروج الذهب",
     18, "『黄金の牧場と宝石の鉱山』。アダブ的歴史書としてイスラーム世界誌の規範。", 5, "invariant"),
    ("タウヒーディー『イムターウ』対話文学", "Tawhidi al-Imta wal-Mu'anasa", "الإمتاع والمؤانسة",
     18, "宮廷夜話集。哲学・文学・宗教を対話形式で論じた散文の傑作。", 4, "invariant"),

    # 4. アンダルス・マグレブ (period 139)
    ("イブン・クズマーン・ザジャル俗語詩", "Ibn Quzman Zajal", "ابن قزمان",
     139, "アンダルス俗語詩ザジャルの大家。アラビア俗語＋ロマンス語要素の混淆詩。", 5, "rethinking"),
    ("イブン・ハズム『鳩の頸飾り』恋愛論", "Ibn Hazm Tawq al-Hamama", "طوق الحمامة",
     139, "アンダルスの宮廷恋愛論。心理分析的散文で恋愛のフェーズを類型化した。", 5, "invariant"),
    ("イブン・トゥファイル『ハイイ・イブン・ヤクザーン』哲学小説", "Ibn Tufail Hayy ibn Yaqzan", "حي بن يقظان",
     139, "孤島で独力で真理に達する哲学小説。後の啓蒙思想にも影響を与えた。", 5, "rethinking"),
    ("イブン・ハファージャ・自然詩", "Ibn Khafaja Nature Poetry", "ابن خفاجة",
     139, "アンダルス自然詩の代表者。庭園・川・山を官能的に描いた詩風で知られる。", 4, "invariant"),
    ("イブン・ザイドゥーン＝ワッラーダ恋愛往還", "Ibn Zaydun-Wallada Affair", "ابن زيدون وولادة",
     139, "コルドバ詩人イブン・ザイドゥーンと王女ワッラーダの恋愛と書簡詩の交換。", 4, "invariant"),
    ("リサーン・アッディーン・イブン・アル＝ハティーブ歴史散文", "Lisan al-Din al-Khatib", "لسان الدين بن الخطيب",
     139, "ナスル朝グラナダの宰相・歴史家・詩人。アンダルス末期の総合的文人。", 4, "invariant"),

    # 5. 現代詩・小説 (period 21)
    ("サイヤーブ『雨の歌』自由詩", "Sayyab Anshudat al-Matar", "أنشودة المطر",
     21, "イラク詩人による自由詩革命の代表作。神話的イメージと社会的悲嘆を融合。", 5, "rethinking"),
    ("アドゥニース『ミフヤールの歌』詩学革新", "Adunis Aghani Mihyar al-Dimashqi", "أغاني مهيار الدمشقي",
     21, "アラブ近代詩のモダニズム宣言書。神秘主義と前衛詩学を統合した詩集。", 5, "rethinking"),
    ("マフフーズ『カイロ三部作』近代小説", "Mahfouz Cairo Trilogy", "الثلاثية",
     21, "20世紀カイロ家族三世代を描く写実小説。ノーベル賞アラブ近代小説の金字塔。", 5, "rethinking"),
    ("タイイブ・サーリフ『北方移住の季節』ポストコロニアル", "Tayyib Salih Mawsim al-Hijra", "موسم الهجرة إلى الشمال",
     21, "スーダン人作家のポストコロニアル小説。コンラッドへの応答として読まれる。", 5, "rethinking"),
    ("エリアス・フーリー『太陽の門』パレスチナ記憶", "Khoury Bab al-Shams", "باب الشمس",
     21, "レバノン作家によるパレスチナ難民の口承史を編み込んだ大河小説。", 5, "rethinking"),
    ("サアダーウィー『女ゼロ地点』フェミニズム", "Saadawi Woman at Point Zero", "امرأة عند نقطة الصفر",
     21, "エジプト・フェミニズム作家の獄中ヒロイン小説。家父長制告発の古典。", 5, "rethinking"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for (name_ja, name_en, name_original, period_id, definition, importance, fourth_status) in ROWS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
                 definition, importance_score, fourth_transform_status, source_tier, canonical_in_region)
                VALUES (?, ?, ?, 'arabic', ?, ?, ?, ?, ?, ?, 'tier1', 'canonical')
            """, (name_ja, name_en, name_original, SUBFIELD, REGION, period_id,
                  definition, importance, fourth_status))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP {name_ja}: {e}")
            skipped += 1
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD,)).fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield13: {total}")

if __name__ == "__main__":
    main()
