#!/usr/bin/env python3
"""Wave 42: add 30 ultra-niche concepts to lit_russia_slavic."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

P_ROM = 201
P_REAL = 202
P_SILVER = 203
P_FORM = 204
P_SOV_MID = 206
P_SOV_LATE = 207
P_CZECH = 209
P_POLISH = 210
P_SOUTH = 211
P_MED = 220

CONCEPTS = [
    # Cluster 1: East Slavic manuscript and church miscellany
    ("イズボルニク1073年選文構成", "Izbornik 1073 compilation structure", P_MED, "ビザンツ教父抜粋を公国教養へ編むキエフ期選集の配列法。"),
    ("ムスチスラフ福音書装飾書記", "Mstislav Gospel ornamented scribal style", P_MED, "福音書写本で金泥頭文字と南スラヴ系装飾を結ぶ書記実践。"),
    ("ノヴゴロド白樺文書恋文語り", "Novgorod birchbark love-letter voice", P_MED, "白樺文書の私的恋文に残る口語的呼びかけと感情表現。"),
    ("『キエフ洞窟修道院聖者伝』修道逸話", "Kievan Caves Patericon monastic anecdotes", P_MED, "奇跡・誘惑・従順を短い逸話で連ねるルーシ修道院文学。"),
    ("ヨシフ・ヴォロツキー論争文体", "Joseph Volotsky polemical style", P_MED, "異端論駁と修道院財産擁護を聖句引用で固める15世紀論争散文。"),
    ("ニコン年代記帝権編纂", "Nikon Chronicle imperial compilation", P_MED, "モスクワ大公権を聖史へ接続する16世紀巨大年代記の編集原理。"),

    # Cluster 2: obscure nineteenth-century Russian print and prose
    ("『北の花』年鑑抒情圏", "Northern Flowers almanac lyric milieu", P_ROM, "デルヴィーク周辺がロマン派詩と社交的年鑑文化を結んだ誌面。"),
    ("ポレヴォイ『モスクワ電信』商業批評", "Polevoy Moscow Telegraph commercial criticism", P_ROM, "読者市場と百科全書的記事で貴族文学圏を揺さぶった雑誌批評。"),
    ("クコリニク劇場愛国メロドラマ", "Kukolnik patriotic melodrama", P_ROM, "宮廷劇場向けに帝国忠誠と感傷的効果を結ぶニコライ期戯曲。"),
    ("グリゴローヴィチ農奴村落スケッチ", "Grigorovich serf-village sketches", P_REAL, "農奴制下の村落貧困を感傷と観察で描く自然派初期散文。"),
    ("ポミャロフスキー神学校半自伝", "Pomyalovsky seminary semi-autobiography", P_REAL, "神学校の暴力的教育を俗語と諷刺で暴く1860年代リアリズム散文。"),
    ("ウスペンスキー民衆経済スケッチ", "Gleb Uspensky folk-economy sketches", P_REAL, "村落の土地・労働・貨幣感覚を観察するナロードニキ系小品。"),

    # Cluster 3: Silver Age journals, coteries, and occult poetics
    ("『黄金の羊毛』誌面コスモポリタン", "Golden Fleece cosmopolitan magazine", P_SILVER, "仏露象徴主義と美術複製を並置した豪華雑誌の国際趣味。"),
    ("『アポロン』小劇場批評", "Apollon little-theatre criticism", P_SILVER, "詩・舞踊・小劇場をネオ古典主義的趣味で評価した銀の時代批評。"),
    ("アルゴナウタイ神秘サークル", "Argonauts mystical circle", P_SILVER, "ベールイ周辺がソフィア論と日記的共同体意識を育てた若象徴派集団。"),
    ("スクリャービン受容の詩的色聴", "Scriabin reception poetic synesthesia", P_SILVER, "音・色・恍惚を詩語へ移す神秘主義的共感覚の批評語彙。"),
    ("ロザノフ断章家庭神学", "Rozanov fragmentary domestic theology", P_SILVER, "家族・性・信仰を短章の逆説で結ぶ宗教思想的散文。"),
    ("『犬小屋』カバレット詩壇", "Stray Dog cabaret poetry scene", P_SILVER, "ペテルブルク地下酒場で朗読・即興・前衛社交が交差した詩壇。"),

    # Cluster 4: formalist, Soviet, and late-Soviet microforms
    ("レフ誌トレチャコフ事実文学", "LEF Tretyakov literature of fact", P_FORM, "旅行記・報告・記録を芸術化し作家機能を再定義する前衛論。"),
    ("リディア・ギンズブルグ心理散文論", "Lidiya Ginzburg psychological prose theory", P_FORM, "日記・回想・小説の境界から人格表現を分析するレニングラード批評。"),
    ("ムラドファクトゥーラ児童前衛", "Muradfaktura children's avant-garde", P_SOV_MID, "マルシャーク周辺の児童誌面で遊戯語と構成主義を接続した実験。"),
    ("ドブロラヴィエ村落ユートピア散文", "Dobrolavie village-utopia prose", P_SOV_MID, "集団農場を道徳共同体として描く1930年代周辺の牧歌的生産散文。"),
    ("アルマナフ『メトロポリ』非公式編集", "Metropol almanac unofficial editing", P_SOV_LATE, "検閲外原稿を作家共同で束ねた1979年モスクワ非公式年鑑。"),
    ("ヴェネディクト・エロフェーエフ酩酊巡礼", "Venedikt Erofeev drunken pilgrimage", P_SOV_LATE, "酒・引用・鉄道移動でソ連日常を聖俗混交化する地下散文技法。"),

    # Cluster 5: West and South Slavic ultra-niches
    ("ポーランド・メシアニズム講壇講義", "Polish messianist lecture poetics", P_POLISH, "亡命講義で民族受難を普遍救済史へ読み替えるロマン主義語り。"),
    ("『ヒメラ』誌ワルシャワ象徴派", "Chimera Warsaw symbolist magazine", P_POLISH, "美術複製と退廃詩を結ぶ若きポーランド期の高踏的雑誌文化。"),
    ("チェコ・デヴィエチル集団詩学", "Devetsil collective poetics", P_CZECH, "都市娯楽・写真・タイポグラフィを詩へ入れたチェコ前衛グループ。"),
    ("ヤン・ムカジョフスキー前景化論", "Jan Mukarovsky foregrounding theory", P_CZECH, "標準言語からの逸脱を美的機能として捉えるプラハ学派詩学。"),
    ("クロアチア・クルグ文学誌", "Croatian Krugovi magazine generation", P_SOUTH, "戦後ザグレブで実存主義と都市感覚を掲げた若手文学誌圏。"),
    ("セルビア・シュルレアリスム宣言", "Serbian surrealist manifesto", P_SOUTH, "ベオグラード前衛が夢・自動記述・政治的反抗を結んだ綱領文。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            before = db.find_concept(name_ja, REGION, period_id)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += int(before is None and cid is not None)
            skipped += int(before is not None)
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
