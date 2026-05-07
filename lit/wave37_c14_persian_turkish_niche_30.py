#!/usr/bin/env python3
"""Wave 37: Add 30 niche concepts to subfield 14 (lit_persian_turkish)."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SUBFIELD_ID = 14
REGION = "西アジア"

# period_id mapping (relevant southwest asia periods)
P_CLASSIC_EARLY = 46   # ペルシア古典初期（サーマーン朝）
P_CLASSIC_MID = 47     # ペルシア古典中期（セルジューク・ホラズム）
P_CLASSIC_LATE = 48    # ペルシア古典後期（イルハン・ティムール）
P_OSMAN = 49           # オスマン古典期（ディーワーン文学）
P_TANZIMAT = 50        # タンジマート期
P_MODERN = 51          # 近現代ペルシア・トルコ
P_OSMAN_FOLK = 251     # オスマン民俗・テッケ詩
P_HINDI = 142          # サブク・ヒンディー期

concepts = [
    # Cluster 1: 古典ペルシア詩細部
    ("ハーカーニー『二つのイラクの贈物』", "Khaqani Tuhfat al-Iraqayn", "تحفة العراقين", "arabic", P_CLASSIC_MID,
     "ハーカーニー12世紀の旅行詩。マッカ巡礼を題材にした韻文紀行。"),
    ("アンヴァリーのカスィーダ", "Anvari Qasida", "قصیده انوری", "arabic", P_CLASSIC_MID,
     "12世紀宮廷詩人アンヴァリーの讃歌詩。難解な修辞で知られる。"),
    ("マヌーチェフリーのムサンマト", "Manuchihri Musammat", "مسمط منوچهری", "arabic", P_CLASSIC_EARLY,
     "11世紀ガズナ朝詩人マヌーチェフリーの連節詩形。自然描写が特徴。"),
    ("アサディー・トゥースィー『ガルシャースプ・ナーマ』", "Asadi Tusi Garshasp-nama", "گرشاسپ‌نامه", "arabic", P_CLASSIC_EARLY,
     "11世紀の英雄叙事詩。シャー・ナーメ後の重要な英雄物語。"),
    ("ナーセル・ホスロウ『旅行記』詳論", "Nasir Khusraw Safarnama detailed", "سفرنامه ناصر خسرو", "arabic", P_CLASSIC_MID,
     "11世紀イスマーイール派詩人の散文紀行。7年の中東巡歴記録。"),
    ("サナーイー『真理の園』詳論", "Sanai Hadiqat al-haqiqa detailed", "حدیقة الحقیقه", "arabic", P_CLASSIC_MID,
     "12世紀スーフィー教訓詩集。マスナヴィー神秘主義詩の祖型。"),

    # Cluster 2: スーフィー詩・神秘主義
    ("アッタール『鳥の言葉』詳論", "Attar Mantiq al-Tayr detailed", "منطق الطیر", "arabic", P_CLASSIC_MID,
     "12世紀寓意詩。30羽の鳥がスィームルグを求める霊的旅。"),
    ("ルーミー『フィーヒ・マー・フィーヒ』", "Rumi Fihi ma fihi", "فیه ما فیه", "arabic", P_CLASSIC_LATE,
     "13世紀ルーミーの散文講話集。題は「中にあるものは中に」の意。"),
    ("ハーフェズ『サーキー・ナーマ』", "Hafez Saqi-nama", "ساقی‌نامه حافظ", "arabic", P_CLASSIC_LATE,
     "14世紀ハーフェズの酌人詩。ワインと神秘主義の融合詩形。"),
    ("ジャーミー『ユースフとズライハー』", "Jami Yusuf Zulaikha", "یوسف و زلیخا", "arabic", P_CLASSIC_LATE,
     "15世紀ジャーミーの神秘主義恋愛叙事詩。クルアーンの物語を翻案。"),
    ("ビーデル・インド様式", "Bidil Indian Style", "بیدل دهلوی", "arabic", P_HINDI,
     "17-18世紀ビーデル・デフラヴィーのサブク・ヒンディー様式詩。難解抽象。"),
    ("イラーキー『ラマアート』", "Iraqi Lama'at", "لمعات", "arabic", P_CLASSIC_LATE,
     "13世紀ファフロッディーン・イラーキーの神秘主義散文。光の閃き。"),

    # Cluster 3: 近代ペルシア
    ("ジャマールザーデ『昔々』", "Jamalzadeh Yeki Bud Yeki Nabud", "یکی بود یکی نبود", "arabic", P_MODERN,
     "1921年。近代ペルシア短編小説の先駆。口語文体革新。"),
    ("ヘダーヤト『盲目の梟』近代心理小説論", "Hedayat Buf-e Kur modernist analysis", "بوف کور تحلیل", "arabic", P_MODERN,
     "1936年サーデク・ヘダーヤトの心理小説。ペルシア・モダニズムの最高峰。"),
    ("フォルーグ『新たに生まれる』", "Forough Tavalludi Digar", "تولدی دیگر", "arabic", P_MODERN,
     "1964年フォルーグ・ファッロホザードの詩集。女性身体性の自由表現。"),
    ("セペフリー『八つの書』", "Sepehri Hasht Ketab", "هشت کتاب", "arabic", P_MODERN,
     "1977年ソフラブ・セペフリー全詩集。仏教的瞑想と東洋哲学の融合。"),
    ("シャムルー『アーイダ』詩篇", "Shamlu Ayda", "آیدا در آینه", "arabic", P_MODERN,
     "1964年アフマド・シャムルーの恋愛詩集。妻アーイダへの献辞詩。"),
    ("アフヴァーン・サーレス『冬』", "Akhavan Sales Zemestan", "زمستان", "arabic", P_MODERN,
     "1956年メフディー・アフヴァーンの詩集。クーデター後の絶望を象徴。"),

    # Cluster 4: オスマン古典
    ("フズーリー『レイラとメジュヌーン』詳細", "Fuzuli Leyla ve Mecnun detailed", "Leylâ vü Mecnûn", "latin", P_OSMAN,
     "16世紀フズーリーのトルコ語マスネヴィー。古典の最高傑作恋愛詩。"),
    ("バーキー『スレイマン哀悼詩』", "Baqi Mersiye-i Sultan Süleyman", "Mersiye-i Sultân Süleymân", "latin", P_OSMAN,
     "16世紀バーキーのスレイマン大帝への弔詩。オスマン哀悼詩の頂点。"),
    ("ネディーム チューリップ時代ガゼル", "Nedim Lale Devri ghazel", "Nedîm Gazelleri", "latin", P_OSMAN,
     "18世紀ネディームの享楽的ガゼル。チューリップ時代の都市文化を反映。"),
    ("シェイヒ・ガーリブ『美と愛』詳論", "Sheyh Galib Hüsn ü Aşk detailed", "Hüsn ü Aşk", "latin", P_OSMAN,
     "1782年メヴレヴィー教団詩人の寓意マスネヴィー。スーフィー象徴主義。"),
    ("ネフィー『風刺詩』", "Nef'i Hicv", "Sihâm-ı Kazâ", "latin", P_OSMAN,
     "17世紀ネフィーの辛辣な風刺詩集『運命の矢』。詩人は処刑された。"),
    ("ユヌス・エムレ テッケ詩", "Yunus Emre Tekke poetry", "Yunus Emre Tekke şiiri", "latin", P_OSMAN_FOLK,
     "13-14世紀ユヌス・エムレのスーフィー教団詩。素朴なトルコ語民衆詩。"),

    # Cluster 5: 近代トルコ
    ("テヴフィク・フィクレト『霧』", "Tevfik Fikret Sis", "Sis", "latin", P_TANZIMAT,
     "1902年フィクレットの政治詩。イスタンブルを抑圧の霧として描く。"),
    ("ヤフヤ・ケマル『静かな船』", "Yahya Kemal Sessiz Gemi", "Sessiz Gemi", "latin", P_MODERN,
     "1925年ヤフヤ・ケマルの死を主題にした名詩。新古典主義の代表作。"),
    ("ナーズム・ヒクメット『私の故郷からの人間風景』", "Nazim Hikmet Memleketimden İnsan Manzaraları", "Memleketimden İnsan Manzaraları", "latin", P_MODERN,
     "1941-50年ヒクメットの叙事詩。獄中で執筆したトルコ社会の壁画詩。"),
    ("オルハン・ヴェリ『奇妙な詩』", "Orhan Veli Garip", "Garip", "latin", P_MODERN,
     "1941年オルハン・ヴェリら『ガリプ運動』詩集。日常言語による革新。"),
    ("サイト・ファーイク『つまらぬ男』", "Sait Faik Lüzumsuz Adam", "Lüzumsuz Adam", "latin", P_MODERN,
     "1948年サイト・ファーイクの短編集。イスタンブル下町の市井人物像。"),
    ("パムク『黒い本』", "Pamuk Kara Kitap", "Kara Kitap", "latin", P_MODERN,
     "1990年オルハン・パムクの長編小説。イスタンブルの記号迷宮。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in concepts:
        try:
            cur.execute("""
                INSERT INTO concepts (
                    name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script,
                  SUBFIELD_ID, REGION, period_id, definition,
                  3, "tier2", "yes"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} ({e})")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
