#!/usr/bin/env python3
"""Wave 33: lit_india niche 30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# Period IDs (region=南アジア)
P_BHAKTI = 132     # バクティ運動期（地域言語）
P_SUFI = 267       # 中世バクティ・スーフィー期
P_URDU = 240       # ウルドゥー近代詩・散文期
P_BENGAL = 134     # ベンガル・ルネサンス期
P_MARATHI = 241    # マラーティー近現代文学期
P_DALIT = 136      # ダリット・周縁文学期
P_LOCAL_NOVEL = 137  # 地域言語近現代小説期
P_KANNADA = 244    # カンナダ近現代文学期
P_MALAYALAM = 243  # マラヤーラム近現代文学期
P_TAMIL = 242      # タミル近現代文学期
P_HINDI_PROSE = 239  # ヒンディー散文成熟期

ROWS = [
    # Cluster 1: Bhakti詩派
    ("ミーラー・バーイー パダ集成", "Mirabai Padavali", "मीराबाई पदावली", "devanagari", P_BHAKTI,
     "ラージャスターン王妃の女性バクタによるクリシュナ恋慕パダ群、口承で広域伝播。"),
    ("スールダース『スールサーガル』", "Surdas Sursagar", "सूरसागर", "devanagari", P_BHAKTI,
     "ブラージ語による幼児クリシュナ叙情詩集成、ヴァッラバ派バクティの頂点。"),
    ("カビール『ビージャク』カビール派伝承", "Kabir Bijak", "बीजक", "devanagari", P_BHAKTI,
     "カビールパントが伝承する核心歌集、サブダ・サーキー・ラマイニーの三部構成。"),
    ("トゥカーラーム『アバンガ・ガーター』", "Tukaram Abhanga Gatha", "तुकारामगाथा", "devanagari", P_BHAKTI,
     "マラーティー・ヴァールカリー派の集成、約4,500アバンガを含むヴィッタル讃歌。"),
    ("ラヴィダース讃歌（グル・グラント収録）", "Ravidas Bani", "ਰਵਿਦਾਸ ਬਾਣੀ", "gurmukhi", P_BHAKTI,
     "ダリット出自の聖者ラヴィダースのバクティ詩、シク聖典に40篇収録。"),
    ("アーンダール『ティルッパーヴァイ』", "Andal Tiruppavai", "திருப்பாவை", "tamil", P_BHAKTI,
     "唯一の女性アルワール聖者による30詩節のヴィシュヌ恋慕誓願歌、タミル詩の至宝。"),

    # Cluster 2: Sufi+Urdu古典
    ("アミール・フスロウ カッワーリー詩", "Amir Khusrau Qawwali", "امیر خسرو قوّالی", "arabic", P_SUFI,
     "デリー・スルターン朝の詩人がペルシア・ヒンダヴィ混合で創始したスーフィー音楽詩。"),
    ("ワリー・ダカニー ディーワーン", "Wali Dakhani Diwan", "والی دکنی دیوان", "arabic", P_URDU,
     "デカン発のウルドゥー詩を北インド宮廷に持ち込み近代ガザル基礎を据えた詩集。"),
    ("ミール・タキー・ミール ディーワーン", "Mir Taqi Mir Diwan", "میر تقی میر دیوان", "arabic", P_URDU,
     "「ウルドゥーの神」と呼ばれる18世紀詩人の悲恋・離散を主題とする六巻ガザル集。"),
    ("ガーリブ ガザル全集", "Ghalib Ghazals", "دیوانِ غالب", "arabic", P_URDU,
     "形而上学的洞察と修辞的凝縮を極めた19世紀ウルドゥー・ペルシア詩の最高峰。"),
    ("イクバール『ザルベ・カリーム』", "Iqbal Zarb-e-Kalim", "ضربِ کلیم", "arabic", P_URDU,
     "1936年詩集、副題「現代に対する宣戦布告」、植民地近代と物質主義への批判詩。"),
    ("ファイズ・アフマド・ファイズ『ナクシェ・ファリヤディ』", "Faiz Naqsh-e-Faryadi", "نقشِ فریادی", "arabic", P_URDU,
     "進歩主義作家運動の旗手による1941年処女詩集、革命と恋愛を融合させた抒情。"),

    # Cluster 3: Bengali Renaissance
    ("バンキム・チャンドラ『アーナンドマト』詳論", "Bankim Anandamath", "আনন্দমঠ", "bengali", P_BENGAL,
     "1882年小説、サンニャースィー反乱を題材に「ヴァンデー・マータラム」を生んだ国民文学。"),
    ("タゴール『ゴーラ』詳論", "Tagore Gora", "গোরা", "bengali", P_BENGAL,
     "1910年大作、白人孤児の青年がヒンドゥー国族主義からブラフモ普遍主義へ転回する小説。"),
    ("タゴール『チャトゥランガ（四部）』", "Tagore Chaturanga", "চতুরঙ্গ", "bengali", P_BENGAL,
     "1916年中篇、四楽章構成で信仰・愛・知の葛藤を描いたタゴール実験的散文。"),
    ("シャラトチャンドラ『パリネーター』（道行く人）", "Sarat Chandra Pather Dabi", "পথের দাবী", "bengali", P_BENGAL,
     "1926年小説、ビルマと東南アジアを舞台に革命結社を描き英政庁が発禁とした作。"),
    ("ジボナナンド・ダース『バナラタ・セン』", "Jibanananda Banalata Sen", "বনলতা সেন", "bengali", P_BENGAL,
     "1942年詩集、千年の漂流者がベンガル女性の神秘的容貌に静寂を見出す近代詩。"),
    ("カジ・ナズルル『ヴィドローヒー（反逆者）』", "Kazi Nazrul Bidrohi", "বিদ্রোহী", "bengali", P_BENGAL,
     "1922年詩、植民地支配と抑圧への激烈な反逆を高揚した自己宣言として歌い上げた作。"),

    # Cluster 4: Marathi+Gujarati（マラーティー中心 周縁劇含む）
    ("トゥカーラーム デフー村伝承群", "Tukaram Dehu Tradition", "देहू तुकाराम परंपरा", "devanagari", P_MARATHI,
     "デフー村を起点とするヴァールカリー巡礼伝承、アバンガと聖者譚の地域基層。"),
    ("ジョーティバー・プーレー『ガラーミーギーリー（奴隷制）』", "Phule Gulamgiri", "गुलामगिरी", "devanagari", P_MARATHI,
     "1873年論説、カースト制を米国奴隷制と比較した反バラモニズム宣言文。"),
    ("テンドゥルカル『ガーシラーム・コトワール』詳論", "Tendulkar Ghashiram Kotwal", "घाशीराम कोतवाल", "devanagari", P_MARATHI,
     "1972年戯曲、18世紀プネーを舞台に権力と従属の悪循環を音楽劇形式で描く。"),
    ("マハーデーヴィー・ヴァルマー『ヤーマー（夜）』", "Mahadevi Verma Yama", "यामा", "devanagari", P_HINDI_PROSE,
     "1940年詩集、チャーヤーヴァード期の女性神秘詩を集成しジュナーンピート受賞契機。"),
    ("ニルマル・ヴェルマー『ラート・カー・リポーター』", "Nirmal Verma Raat ka Reporter", "रात का रिपोर्टर", "devanagari", P_HINDI_PROSE,
     "1989年小説、緊急事態下デリーの夜を彷徨う記者の実存的不安を描く新世代散文。"),
    ("ヴィジャイ・テンドゥルカル『サカーラーム・バインダル』詳論", "Tendulkar Sakharam Binder", "सखाराम बाइंडर", "devanagari", P_MARATHI,
     "1972年戯曲、カースト下層男性の暴力と性的支配を直視し検閲論争を惹起した作。"),

    # Cluster 5: 南インド・ダリット
    ("バーマー『カルッカ』詳論", "Bama Karukku", "கருக்கு", "tamil", P_DALIT,
     "1992年自伝、タミル・キリスト教ダリット女性の二重周縁化を口語タミルで証言。"),
    ("シヴァカミ『パリヤッカル』", "Sivakami Pazhaiyana Kazhithalum", "பழையன கழிதலும்", "tamil", P_DALIT,
     "1989年小説、タミルダリット女性作家による土地所有とジェンダー暴力の長篇。"),
    ("マハーシュウェター・デーヴィー『ハジャール・チョウラシール・マー』詳論", "Mahasweta Hajar Churashir Maa", "হাজার চুরাশির মা", "bengali", P_DALIT,
     "1974年小説、ナクサライト運動で殺された息子の母を通じ国家暴力と階級を告発。"),
    ("U・R・アナンタムールティ『サムスカーラ』詳論", "Ananthamurthy Samskara", "ಸಂಸ್ಕಾರ", "kannada", P_KANNADA,
     "1965年小説、バラモン村の死体処理儀礼を巡りカーストと近代化の亀裂を描く。"),
    ("O・V・ヴィジャヤン『カサーキンテ・イティハーサム』詳論", "Vijayan Khasakkinte Itihasam", "ഖസാക്കിന്റെ ഇതിഹാസം", "malayalam", P_MALAYALAM,
     "1969年小説、ケーララ僻村を舞台にマラヤーラム散文の文体革命を起こした実存譚。"),
    ("シヴァラーマ・カーラント『ムーカッジヤ・カナス』", "Karanth Mookajjiya Kanasu", "ಮೂಕಜ್ಜಿಯ ಕನಸುಗಳು", "kannada", P_KANNADA,
     "1968年小説、聾の老婆の夢を通じ人類進化と精神史を辿るカンナダ哲学的長篇。"),
]


def main() -> None:
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, defi in ROWS:
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (name_ja, name_en, name_orig, script,
                 12, "南アジア", period_id, defi,
                 4, "primary", "yes"),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
