#!/usr/bin/env python3
"""Wave37: lit_jp_modern (subfield_id=11) niche 30 concepts."""
import sqlite3
import os

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# (name_ja, name_en, name_original, definition, period_id, importance, tier, canonical)
# period_ids: 195=戦後, 289=戦後期, 290=現代, 196=現代文学期
ROWS = [
    # Cluster 1: 戦後派詳細 (period_id=195/289)
    ("真空地帯（野間宏）", "Vacuum Zone (Noma)", "真空地帯", "野間宏1952年作。軍隊内部の非人間性を描いた戦後派代表長編。", 195, 4),
    ("永遠序章（椎名麟三）", "Eternal Prologue (Shiina)", "永遠なる序章", "椎名麟三1948年作。実存主義的不安と再生希求を描く戦後文学。", 195, 3),
    ("風媒花（武田泰淳）", "Wind-pollinated Flower (Takeda)", "風媒花", "武田泰淳1952年作。中国体験と戦後知識人の倫理を描く長編。", 195, 3),
    ("桜島（梅崎春生）", "Sakurajima (Umezaki)", "桜島", "梅崎春生1946年作。敗戦間際の海軍基地を舞台にした不条理小説。", 195, 4),
    ("死の影の下に（中村真一郎）", "Beneath the Shadow of Death", "死の影の下に", "中村真一郎1947年作。プルースト的内省手法による戦後五部作冒頭。", 195, 3),
    ("草の花（福永武彦）", "Flower of Grass (Fukunaga)", "草の花", "福永武彦1954年作。同性愛的友情と病死を主題とする抒情長編。", 195, 3),
    # Cluster 2: 第三の新人 (period_id=289)
    ("海辺の光景（安岡章太郎）", "A View by the Sea", "海辺の光景", "安岡章太郎1959年作。母の死と病院を描く第三の新人代表作。", 289, 4),
    ("砂の上の植物群（吉行淳之介）", "Plants on the Sand", "砂の上の植物群", "吉行淳之介1964年作。性と日常の不毛を描く都市心理小説。", 289, 3),
    ("静物（庄野潤三）", "Still Life (Shono)", "静物", "庄野潤三1960年作。家族日常を精緻に描く第三の新人作品。", 289, 3),
    ("抱擁家族（小島信夫）", "Embracing Family", "抱擁家族", "小島信夫1965年作。郊外住宅と妻の不倫を描く戦後家族崩壊小説。", 289, 4),
    ("黒いハンカチ（小沼丹）", "Black Handkerchief (Onuma)", "黒いハンカチ", "小沼丹1958年作。女性教師を語り手とする連作短編集。", 289, 3),
    ("山本五十六（阿川弘之）", "Yamamoto Isoroku (Agawa)", "山本五十六", "阿川弘之1965年作。連合艦隊司令長官を描く伝記小説。", 289, 3),
    # Cluster 3: 内向の世代以降 (period_id=290)
    ("杳子（古井由吉）", "Yoko (Furui)", "杳子", "古井由吉1971年作。山中で出会う神経症の女との関係を描く芥川賞作。", 290, 4),
    ("時間（黒井千次）", "Time (Kuroi)", "時間", "黒井千次1969年作。サラリーマン日常の倦怠と意識の流れを描く。", 290, 3),
    ("挾み撃ち（後藤明生）", "Pincer Movement (Goto)", "挟み撃ち", "後藤明生1973年作。ゴーゴリ的脱線文体による存在論的長編。", 290, 3),
    ("司令の休暇（阿部昭）", "Commander's Leave", "司令の休暇", "阿部昭1970年作。海軍士官の父を描く私小説的短編。", 290, 3),
    ("北の河（高井有一）", "Northern River (Takai)", "北の河", "高井有一1965年作。母の自殺を背景とする芥川賞抒情作。", 290, 3),
    ("髪の祭（田久保英夫）", "Festival of Hair", "髪の祭", "田久保英夫1971年作。性と土俗を融合する芥川賞短編集。", 290, 3),
    # Cluster 4: 80年代以降女性作家 (period_id=290/196)
    ("火の山-山猿記（津島佑子）", "Mountain of Fire", "火の山―山猿記", "津島佑子1996-98年作。三世代の女系家族史を描く大河小説。", 196, 4),
    ("波うつ土地（富岡多恵子）", "Undulating Land", "波うつ土地", "富岡多恵子1983年作。郊外の主婦を主人公とする長編。", 290, 3),
    ("蟹（河野多恵子）", "Crab (Kono)", "蟹", "河野多恵子1962/63年作。サディスティックな性愛を描く短編。", 290, 3),
    ("透光の樹（高樹のぶ子）", "Translucent Tree", "透光の樹", "高樹のぶ子1999年作。中年男女の官能と死を描く谷崎賞作。", 196, 3),
    ("二百回忌（笙野頼子）", "Two-hundredth Memorial", "二百回忌", "笙野頼子1994年作。死者と生者が交錯する幻想的家族譚。", 290, 3),
    ("ナチュラル・ウーマン（松浦理英子）", "Natural Woman", "ナチュラル・ウーマン", "松浦理英子1987年作。レズビアン関係を主題とする連作小説。", 290, 4),
    # Cluster 5: 現代詩・俳句細部 (period_id=290/196)
    ("サフラン摘み（吉岡実）", "Saffron Picking (Yoshioka)", "サフラン摘み", "吉岡実1976年作。視覚的イメージ過剰の前衛詩集。", 290, 3),
    ("季節・夏（入沢康夫）", "Season - Summer (Irisawa)", "季節 / 夏", "入沢康夫1962-65年作。物語詩実験と神話的循環の連作。", 290, 3),
    ("鏡のなかの男（多田智満子）", "Man in the Mirror", "鏡のなかの男", "多田智満子1968年作。古典的修辞による知的女性詩篇集。", 290, 3),
    ("会社の人事（中桐雅夫）", "Company Personnel", "会社の人事", "中桐雅夫1979年作。サラリーマン詩を確立した晩年の代表詩集。", 290, 4),
    ("他人の空（飯島耕一）", "Stranger's Sky", "他人の空", "飯島耕一1953年作。シュルレアリスム影響下の戦後詩集名篇。", 195, 3),
    ("透視図法（大岡信）", "Perspective (Ooka)", "透視図法", "大岡信1972年作。連歌的方法を試みた中期詩集。", 290, 3),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, defn, period_id, imp in ROWS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
                 definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, 'kanji', 11, '東アジア', ?, ?, ?, 'A', 'JP')
            """, (name_ja, name_en, name_orig, period_id, defn, imp))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} -- {e}")
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=11").fetchone()[0]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield 11: {total}")
    conn.close()

if __name__ == "__main__":
    main()
