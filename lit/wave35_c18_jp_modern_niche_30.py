#!/usr/bin/env python3
"""Wave 35 C18: lit_jp_modern niche 30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 11
REGION = "東アジア"

# period mapping (region=東アジア)
P_TAISHO = 9        # 大正期
P_SHOWA_PRE = 10    # 昭和戦前期
P_POSTWAR = 11      # 戦後期
P_GENDAI = 12       # 現代

CONCEPTS = [
    # Cluster 1: 大正詩 (period=大正期)
    ("北原白秋『邪宗門』", "Kitahara Hakushu: Jashumon", "邪宗門", "kanji", P_TAISHO,
     "1909年詩集。南蛮趣味と異国情緒を象徴主義的に表現した白秋の代表作。"),
    ("萩原朔太郎『月に吠える』", "Hagiwara Sakutaro: Howling at the Moon", "月に吠える", "kanji", P_TAISHO,
     "1917年詩集。口語自由詩を確立し、近代日本詩の出発点となった病的感性の表現。"),
    ("高村光太郎『道程』", "Takamura Kotaro: Dotei", "道程", "kanji", P_TAISHO,
     "1914年詩集。理想主義と人道主義に貫かれた口語自由詩の先駆的達成。"),
    ("三好達治『測量船』", "Miyoshi Tatsuji: Sokuryosen", "測量船", "kanji", P_SHOWA_PRE,
     "1930年詩集。古典的抒情と近代詩の知性を融合した昭和叙情詩の金字塔。"),
    ("中原中也『山羊の歌』", "Nakahara Chuya: Yagi no Uta", "山羊の歌", "kanji", P_SHOWA_PRE,
     "1934年詩集。フランス象徴詩の影響下で歌謡的リズムと存在の哀しみを刻んだ生前唯一の詩集。"),
    ("西脇順三郎『AMBARVALIA』", "Nishiwaki Junzaburo: AMBARVALIA", "AMBARVALIA", "latin", P_SHOWA_PRE,
     "1933年詩集。モダニズムと古典の融合により日本シュルレアリスム詩を確立した先駆作。"),

    # Cluster 2: 昭和初期 (period=昭和戦前期)
    ("堀辰雄『菜穂子』", "Hori Tatsuo: Naoko", "菜穂子", "kanji", P_SHOWA_PRE,
     "1941年小説。フランス心理主義の影響下で女性の内面と病を繊細に描いた長編。"),
    ("横光利一『機械』", "Yokomitsu Riichi: Kikai", "機械", "kanji", P_SHOWA_PRE,
     "1930年小説。意識の流れと四人称的視点を試みた新感覚派から心理主義への転換作。"),
    ("川端康成『雪国』詳説", "Kawabata Yasunari: Snow Country (detailed)", "雪国", "kanji", P_SHOWA_PRE,
     "1937年小説。雪国の温泉芸者と都会人の交流を通して虚無と美の極致を描いた代表作。"),
    ("谷崎潤一郎『細雪』", "Tanizaki Junichiro: Sasameyuki", "細雪", "kanji", P_SHOWA_PRE,
     "1948年完結長編。船場の四姉妹を通して滅びゆく上方文化と古典的優美を描く。"),
    ("岡本かの子『老妓抄』", "Okamoto Kanoko: Roghisho", "老妓抄", "kanji", P_SHOWA_PRE,
     "1938年短編。老芸者と青年技師の交流を通して生命と芸の根源を描いた円熟期の代表作。"),
    ("林芙美子『放浪記』詳説", "Hayashi Fumiko: Horoki (detailed)", "放浪記", "kanji", P_SHOWA_PRE,
     "1930年自伝的小説。貧困と放浪を女性の視点から赤裸々に綴り女性労働文学の先駆となる。"),

    # Cluster 3: 戦後派詳細 (period=戦後期)
    ("野間宏『暗い絵』", "Noma Hiroshi: Kurai E", "暗い絵", "kanji", P_POSTWAR,
     "1946年小説。戦時下の青年の苦悩を全体小説の手法で描いた戦後派文学の出発点。"),
    ("武田泰淳『ひかりごけ』", "Takeda Taijun: Hikarigoke", "ひかりごけ", "kanji", P_POSTWAR,
     "1954年小説。難破船の人肉食事件を題材に人間存在の罪と倫理を問う問題作。"),
    ("椎名麟三『深夜の酒宴』", "Shiina Rinzo: Shinya no Shuen", "深夜の酒宴", "kanji", P_POSTWAR,
     "1947年小説。実存主義的視点から底辺労働者の生を描いたデビュー作で戦後派代表作。"),
    ("大岡昇平『野火』", "Ooka Shohei: Nobi", "野火", "kanji", P_POSTWAR,
     "1951年小説。フィリピン戦線敗走兵の極限体験を通して人間の倫理と神を問う代表作。"),
    ("中島敦『李陵』", "Nakajima Atsushi: Riryo", "李陵", "kanji", P_SHOWA_PRE,
     "1943年遺作中編。漢代の李陵・司馬遷・蘇武を通して運命と知識人の倫理を描く。"),
    ("福永武彦『死の島』", "Fukunaga Takehiko: Shi no Shima", "死の島", "kanji", P_POSTWAR,
     "1971年長編。広島原爆を背景に多視点構成で愛と死と芸術を描いたモダニズム的代表作。"),

    # Cluster 4: 第三の新人+1960s (period mix)
    ("吉行淳之介『驟雨』", "Yoshiyuki Junnosuke: Shuu", "驟雨", "kanji", P_POSTWAR,
     "1954年芥川賞作。娼婦と男の関係を通して都市の性と孤独を描く第三の新人代表作。"),
    ("庄野潤三『プールサイド小景』", "Shono Junzo: Poolside Shokei", "プールサイド小景", "kanji", P_POSTWAR,
     "1954年芥川賞作。中流家庭の崩壊の予兆を細やかな日常描写で捉えた第三の新人代表作。"),
    ("安岡章太郎『海辺の光景』", "Yasuoka Shotaro: Umibe no Kokei", "海辺の光景", "kanji", P_POSTWAR,
     "1959年小説。母の死をめぐる息子の意識を通して戦後家族の崩壊を描いた代表長編。"),
    ("小島信夫『アメリカン・スクール』", "Kojima Nobuo: American School", "アメリカン・スクール", "kanji", P_POSTWAR,
     "1954年芥川賞作。占領期の英語教師の屈折を通して戦後日本のアイデンティティを描く。"),
    ("大江健三郎『ピンチランナー調書』", "Oe Kenzaburo: Pinch Runner Memorandum", "ピンチランナー調書", "kanji", P_POSTWAR,
     "1976年長編。父子の入れ替わりという仕掛けを通して核時代の救済を描く実験的長編。"),
    ("開高健『輝ける闇』", "Kaiko Takeshi: Kagayakeru Yami", "輝ける闇", "kanji", P_POSTWAR,
     "1968年長編。ベトナム戦争従軍体験を基にしたルポルタージュ的小説で戦争文学新地平。"),

    # Cluster 5: 1980s+現代 (period=現代)
    ("中上健次『千年の愉楽』", "Nakagami Kenji: Sennen no Yuraku", "千年の愉楽", "kanji", P_GENDAI,
     "1982年連作短編。紀州の路地を舞台に被差別部落の血脈と神話的時間を描く代表作。"),
    ("古井由吉『杳子』", "Furui Yoshikichi: Yoko", "杳子", "kanji", P_POSTWAR,
     "1971年芥川賞作。山中で出会う精神病の女性との関係を通して内向の世代を代表する作品。"),
    ("後藤明生『挟み撃ち』", "Goto Meisei: Hasamiuchi", "挟み撃ち", "kanji", P_POSTWAR,
     "1973年長編。ゴーゴリ「外套」を引きつつ自己の起源を探索する内向の世代メタフィクション。"),
    ("阿部和重『シンセミア』", "Abe Kazushige: Sinsemilla", "シンセミア", "kanji", P_GENDAI,
     "2003年大長編。山形の地方都市を舞台に暴力と性の連鎖を多視点で描いた現代叙事詩。"),
    ("平野啓一郎『決壊』", "Hirano Keiichiro: Kekkai", "決壊", "kanji", P_GENDAI,
     "2008年長編。猟奇殺人事件を通して情報社会における悪と分人主義の問題を提起した作。"),
    ("古川日出男『ベルカ、吠えないのか?』", "Furukawa Hideo: Belka, Why Don't You Bark?", "ベルカ、吠えないのか?", "kanji", P_GENDAI,
     "2005年長編。20世紀の戦争を犬の視点から世界史的に描く現代日本文学のマジックリアリズム。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (name_ja, name_en, name_orig, script,
                 SUBFIELD_ID, REGION, period_id, definition,
                 3, "tier2", "yes"),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} ({e})")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
