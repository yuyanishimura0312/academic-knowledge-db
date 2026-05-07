#!/usr/bin/env python3
"""Wave 37: lit_africa subfield (id=15) niche concepts +30. 5 thematic clusters x 6 concepts."""
import sqlite3
import sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# period mapping
P_INDEP_EARLY = 64    # 独立後初期 1960-1980
P_INDEP_MID = 149     # 独立後中期 1980-2000
P_21C = 150           # 21世紀アフリカ文学 2000-2030
P_LUSO = 152          # 葡語圏アフリカ独立後 1975-2025
P_MAGHREB = 151       # マグレブ近代 1950-2010
P_LATE_COLONIAL = 247 # 植民地末期 1930-1960

REGION = "グローバルサウス"
SUBFIELD = 15

CONCEPTS = [
    # Cluster 1: 西アフリカ細部
    ("ソインカ『死と王の馬丁』", "Death and the King's Horseman", "Death and the King's Horseman", "english",
     P_INDEP_MID, "ヨルバ的世界観と植民地遭遇を儀礼劇に凝縮したソインカ1975年の代表悲劇。"),
    ("アチェベ『神の矢』詳論", "Arrow of God (close reading)", "Arrow of God", "english",
     P_LATE_COLONIAL, "イボ祭司エゼウルと植民地行政の衝突を描くアチェベ1964年の三部作中核を精読。"),
    ("マリアマ・バー『かくも長き手紙』詳論", "So Long a Letter (close reading)", "Une si longue lettre", "french",
     P_INDEP_EARLY, "セネガルの一夫多妻と寡婦の喪を書簡体で描く西アフリカ女性文学起点作の精読。"),
    ("センベーヌ『神の森の木片』", "God's Bits of Wood", "Les Bouts de bois de Dieu", "french",
     P_INDEP_EARLY, "1947年ダカール=ニジェール鉄道スト題材の集合的主人公型労働叙事小説。"),
    ("クルマ『アラーは義務ではない』詳論", "Allah n'est pas obligé (close reading)", "Allah n'est pas obligé", "french",
     P_21C, "西アフリカ少年兵を口語マリンケ語混合で語るクルマ2000年作の声と暴力の詩学。"),
    ("ベン・オクリ『飢えた道』詳論", "The Famished Road (close reading)", "The Famished Road", "english",
     P_INDEP_MID, "アビク（再生児）視点でナイジェリア政治とヨルバ霊性を融合した魔術的写実精読。"),

    # Cluster 2: 東アフリカ
    ("ンギュギ『血の花弁』詳論", "Petals of Blood (close reading)", "Petals of Blood", "english",
     P_INDEP_EARLY, "独立後ケニアの新植民地主義と農村崩壊を四人連環視点で描く1977年作の精読。"),
    ("ンギュギ『精神の脱植民地化』理論", "Decolonising the Mind (theory)", "Decolonising the Mind", "english",
     P_INDEP_MID, "英語放棄とギクユ語回帰を宣言した1986年エッセイの言語政治理論。"),
    ("ヌルディン・ファラー『マップス』詳論", "Maps (close reading)", "Maps", "english",
     P_INDEP_MID, "オガデン戦争を背景にソマリア孤児アスカルのアイデンティティを二人称で問う1986年作。"),
    ("イヴォンヌ・ヴェラ『石の処女』", "The Stone Virgins", "The Stone Virgins", "english",
     P_21C, "ジンバブエ・グクラフンディ虐殺を女性身体の詩的散文で記録する2002年作。"),
    ("ダンガレンガ『ナーヴァス・コンディションズ』詳論", "Nervous Conditions (close reading)", "Nervous Conditions", "english",
     P_INDEP_MID, "ローデシア少女タンブーの教育と摂食障害を通じ植民地内面化を描く1988年作精読。"),
    ("オコト・ビテック『ラウィノの歌』", "Song of Lawino", "Wer pa Lawino", "acholi",
     P_INDEP_EARLY, "西洋化夫オコルへのアチョリ妻の口承詩的反論。1966年の英語経由アチョリ詩学。"),

    # Cluster 3: 南部アフリカ
    ("ベシー・ヘッド『力の問題』", "A Question of Power", "A Question of Power", "english",
     P_INDEP_EARLY, "ボツワナ亡命作家の精神崩壊と人種混淆アイデンティティを描く1973年自伝的作。"),
    ("エズキア・ムファレレ『下の二番街』", "Down Second Avenue", "Down Second Avenue", "english",
     P_LATE_COLONIAL, "ソフィアタウン少年期からアパルトヘイト亡命までを語る1959年自伝の古典。"),
    ("アレックス・ラ・グマ『夜歩く』", "A Walk in the Night", "A Walk in the Night", "english",
     P_LATE_COLONIAL, "ケープタウン第六区の一夜の暴力と疎外を圧縮するラ・グマ1962年中篇。"),
    ("ゴーディマー『七月の人々』詳論", "July's People (close reading)", "July's People", "english",
     P_INDEP_MID, "革命後南アで白人家族が黒人召使ジュリーの村に逃れる1981年逆転物語の精読。"),
    ("クッツェー『恥辱』詳論", "Disgrace (close reading)", "Disgrace", "english",
     P_21C, "ポストアパルトヘイト南アの教授ルリーの転落を通じ罪と贖いを問う1999年作精読。"),
    ("ザケス・ムダ『赤の心』詳論", "The Heart of Redness (close reading)", "The Heart of Redness", "english",
     P_21C, "コーサ牛殺し1856年と現代開発を二重時間で交錯させるムダ2000年作精読。"),

    # Cluster 4: マグレブ・アラブアフリカ
    ("タハール・ベン・ジェルーン『砂の子』", "The Sand Child", "L'Enfant de sable", "french",
     P_MAGHREB, "モロッコで男として育てられた女アフメドを多声語りで描くベン・ジェルーン1985年作。"),
    ("アシア・ジェバール『アルジェリア白書』", "Algerian White", "Le Blanc de l'Algérie", "french",
     P_21C, "1990年代アルジェリア内戦で殺された友人作家への鎮魂エッセイ1995年作。"),
    ("ドリス・シュライービ『単純な過去』", "The Simple Past", "Le Passé simple", "french",
     P_LATE_COLONIAL, "モロッコ父権社会への息子の反抗を激越なフランス語で書いた1954年デビュー作。"),
    ("カテブ・ヤシン『ネジマ』", "Nedjma", "Nedjma", "french",
     P_LATE_COLONIAL, "アルジェリア独立闘争を四人男性が同名女性ネジマを通じ語る1956年モダニズム小説。"),
    ("ナワル・サアダーウィー『零度の女』", "Woman at Point Zero", "إمرأة عند نقطة الصفر", "arabic",
     P_INDEP_EARLY, "死刑囚売春婦フィルダウスの一人称告白で家父長暴力を糾弾する1975年作。"),
    ("レイラ・スリマニ『ヌヌ（ねむれない子守唄）』", "Lullaby (Chanson douce)", "Chanson douce", "french",
     P_21C, "パリの白人中産家庭で起きた乳母による幼児殺害を遡及するスリマニ2016年作。"),

    # Cluster 5: ルソフォン・新世代
    ("ミア・コウト『夢遊する大地』詳論", "Sleepwalking Land (close reading)", "Terra Sonâmbula", "portuguese",
     P_LUSO, "モザンビーク内戦の難民老人と少年の旅と日記内日記を交錯させる1992年作精読。"),
    ("ペペテーラ『マヨンベ』詳論", "Mayombe (close reading)", "Mayombe", "portuguese",
     P_LUSO, "アンゴラ解放戦争の森ゲリラ部隊の民族間緊張を多視点で描く1980年作精読。"),
    ("ホセ・ルアンディーノ・ヴィエイラ", "José Luandino Vieira", "José Luandino Vieira", "portuguese",
     P_LUSO, "ルアンダのムセケ（スラム）方言キンブンドゥ混成で書く葡語圏アフリカ文学の刷新者。"),
    ("アディーチェ『半分のぼった黄色い太陽』詳論", "Half of a Yellow Sun (close reading)", "Half of a Yellow Sun", "english",
     P_21C, "ビアフラ戦争1967-70を三人称三視点で再構成するアディーチェ2006年作精読。"),
    ("テジュ・コール『オープン・シティ』詳論", "Open City (close reading)", "Open City", "english",
     P_21C, "ナイジェリア系米国人医ジュリウスのNY散歩録から記憶と暴力を編む2011年作精読。"),
    ("ノヴァイオレット・ブラワヨ『新しい名前は要らない』詳論", "We Need New Names (close reading)", "We Need New Names", "english",
     P_21C, "ジンバブエ少女ダーリンの貧民街と米国移住を二部構成で描く2013年作精読。"),
]

assert len(CONCEPTS) == 30, f"Expected 30, got {len(CONCEPTS)}"

con = sqlite3.connect(DB)
cur = con.cursor()

inserted = 0
skipped = 0
for name_ja, name_en, name_orig, script, period_id, definition in CONCEPTS:
    assert len(definition) <= 100, f"Definition too long ({len(definition)}): {definition}"
    try:
        cur.execute(
            """INSERT INTO concepts
               (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (name_ja, name_en, name_orig, script, SUBFIELD, REGION, period_id, definition, 3, "secondary", "africa"),
        )
        inserted += 1
    except sqlite3.IntegrityError as e:
        skipped += 1
        print(f"SKIP (dup): {name_ja} -> {e}", file=sys.stderr)

con.commit()
print(f"inserted={inserted} skipped={skipped}")
total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=15").fetchone()[0]
print(f"subfield_id=15 total={total}")
con.close()
