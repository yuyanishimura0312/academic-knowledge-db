#!/usr/bin/env python3
"""Wave 28 C28: lit_russia_slavic +30 concepts (5 clusters x 6)."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 18

# period IDs (verified from periods table)
P_GOLDEN = 291      # 19世紀ロシア黄金時代 1820-1860
P_REALISM = 202     # 19世紀後期ロシア・リアリズム成熟期 1860-1910
P_SILVER = 203      # ロシア銀の時代 1890-1925
P_SOVIET_MID = 206  # ソヴィエト中期 1925-1965
P_CZECH = 209       # チェコ近現代文学期 1880-2025
P_POLAND = 210      # ポーランド・ロマン主義および近現代期 1820-2025

R_RUS = "東欧・ロシア"

# Each tuple: (name_ja, name_en, name_original, original_script, period_id, region, definition, importance, fourth_status, source_tier, canonical)
concepts = [
    # Cluster 1: Russian詳細 (6)
    ("カラムジン『哀れなリーザ』詳論", "Karamzin Bednaya Liza in detail", "Бедная Лиза", "cyrillic", P_GOLDEN, R_RUS,
     "1792年の感傷小説。農民娘の悲恋を通じてロシア感傷主義を確立した代表作。", 4, "invariant", "tier1", "yes"),
    ("レールモントフ『デーモン』長編詩", "Lermontov Demon long poem", "Демон", "cyrillic", P_GOLDEN, R_RUS,
     "堕天使の愛と悲劇を描く長編叙事詩。コーカサスを舞台にロマン主義的反抗を象徴。", 4, "invariant", "tier1", "yes"),
    ("ゴーゴリ・ペテルブルク物語群", "Gogol Petersburg Tales", "Петербургские повести", "cyrillic", P_GOLDEN, R_RUS,
     "『鼻』『外套』『涅瓦大通り』等を含む短編群。都市の幻想と小役人の悲哀を描く。", 5, "invariant", "tier1", "yes"),
    ("チュッチェフ『沈黙！』Silentium", "Tyutchev Silentium", "Silentium!", "cyrillic", P_GOLDEN, R_RUS,
     "1830年の詩。「言葉にされた思いは虚偽」と説き、内面の沈黙を讃える形而上抒情詩。", 4, "invariant", "tier1", "yes"),
    ("フェート夕べの灯火詩篇", "Fet evening lights cycle", "Вечерние огни", "cyrillic", P_REALISM, R_RUS,
     "晩年の四詩集。瞬間の感覚と自然の微光を捉える純粋抒情の到達点。", 3, "invariant", "tier2", None),
    ("アポロン・マイコフ古典主義抒情", "Apollon Maykov classical lyric", "Аполлон Майков", "cyrillic", P_GOLDEN, R_RUS,
     "古代ギリシア・ローマ題材の彫琢された抒情詩で知られる19世紀詩人。", 3, "invariant", "tier2", None),

    # Cluster 2: Symbolism (6)
    ("ブリューソフ『火の天使』詳論", "Bryusov Fiery Angel detailed", "Огненный ангел", "cyrillic", P_SILVER, R_RUS,
     "1908年の歴史小説。16世紀ドイツを舞台に魔術と恋情を描く象徴主義代表作。", 4, "invariant", "tier1", "yes"),
    ("ソログーブ『小悪魔』詳論", "Sologub Petty Demon", "Мелкий бес", "cyrillic", P_SILVER, R_RUS,
     "1907年の小説。ペレドノフ像を通じ俗悪と狂気を描いた象徴主義散文の到達点。", 4, "invariant", "tier1", "yes"),
    ("ベールイ『ペテルブルク』構造", "Bely Petersburg structure", "Петербург", "cyrillic", P_SILVER, R_RUS,
     "1913年小説のリズム的散文・幾何学的都市像・父子テーマがモダニズムを先取り。", 5, "rethinking", "tier1", "yes"),
    ("アンネンスキー『糸杉の小箱』詳論", "Annensky Cypress Casket detailed", "Кипарисовый ларец", "cyrillic", P_SILVER, R_RUS,
     "1910年遺作詩集。透明な憂愁と細密な感覚で銀の時代詩学を結晶化した。", 4, "invariant", "tier1", "yes"),
    ("ヴャチェスラフ・イワノフ『コル・アルデンス』詳論", "Vyacheslav Ivanov Cor Ardens detailed", "Cor Ardens", "latin", P_SILVER, R_RUS,
     "1911年の二部構成詩集。神秘主義と古典神話を織り合わせた象徴主義の理論的中核。", 4, "invariant", "tier1", "yes"),
    ("メレジコフスキー『キリストと反キリスト』三部作詳論", "Merezhkovsky Christ and Antichrist detailed", "Христос и Антихрист", "cyrillic", P_SILVER, R_RUS,
     "1895-1905年の歴史小説三部作。神権と肉欲の対立を歴史哲学として展開。", 3, "invariant", "tier2", None),

    # Cluster 3: Acmeism+ (6)
    ("アフマートヴァ『Anno Domini』", "Akhmatova Anno Domini", "Anno Domini MCMXXI", "latin", P_SILVER, R_RUS,
     "1922年詩集。革命後の喪失と祈りを古典的造形で歌うアクメイズム成熟期の作。", 4, "invariant", "tier1", "yes"),
    ("アフマートヴァ『レクイエム』詳論", "Akhmatova Requiem", "Реквием", "cyrillic", P_SOVIET_MID, R_RUS,
     "1935-1961年の連作詩。大粛清下の母たちの悲嘆を記念碑的に証言した代表作。", 5, "invariant", "tier1", "yes"),
    ("マンデリシュタム『石』詳論", "Mandelstam Stone detailed", "Камень", "cyrillic", P_SILVER, R_RUS,
     "1913/1916年の処女詩集。建築の堅固さを詩語に求めるアクメイズム宣言の実践。", 5, "invariant", "tier1", "yes"),
    ("マンデリシュタム『トリスティア』詳論", "Mandelstam Tristia", "Tristia", "latin", P_SILVER, R_RUS,
     "1922年詩集。古代と亡命の主題を重ね、ヘレニズム的世界文学観を提示。", 4, "invariant", "tier1", "yes"),
    ("グミリョフ『火の柱』詳論", "Gumilyov Pillar of Fire detailed", "Огненный столп", "cyrillic", P_SILVER, R_RUS,
     "1921年遺作詩集。アフリカ・神秘・運命を主題とするアクメイズム最終達成。", 4, "invariant", "tier1", "yes"),
    ("ホダセーヴィチ『ヨーロッパの夜』", "Khodasevich European Night", "Европейская ночь", "cyrillic", P_SOVIET_MID, R_RUS,
     "1927年亡命詩集。パリの夜と精神の漂泊を端正な古典詩形で刻んだ。", 4, "invariant", "tier1", "yes"),

    # Cluster 4: Soviet (6)
    ("エセーニン『黒い男』詳論", "Esenin Black Man", "Чёрный человек", "cyrillic", P_SOVIET_MID, R_RUS,
     "1925年の長詩。詩人の分身としての黒い男との対話で自己崩壊を描く遺作。", 4, "invariant", "tier1", "yes"),
    ("パステルナーク『わが妹なる人生』詳論", "Pasternak My Sister Life", "Сестра моя — жизнь", "cyrillic", P_SILVER, R_RUS,
     "1922年詩集。1917年夏の体験を生命と自然の輝きで描き、新世代詩学を確立。", 5, "invariant", "tier1", "yes"),
    ("ツヴェターエワ『ヴェールスティ』", "Tsvetaeva Versts", "Вёрсты", "cyrillic", P_SILVER, R_RUS,
     "1921/1922年詩集。革命期モスクワを激情的リズムで歌い独自の声を確立。", 4, "invariant", "tier1", "yes"),
    ("バーベリ『騎兵隊』詳論", "Babel Red Cavalry", "Конармия", "cyrillic", P_SOVIET_MID, R_RUS,
     "1926年短編集。ポーランド戦争に従軍したユダヤ知識人の暴力と美の証言。", 5, "invariant", "tier1", "yes"),
    ("オレーシャ『羨望』詳論", "Olesha Envy", "Зависть", "cyrillic", P_SOVIET_MID, R_RUS,
     "1927年の中編。新旧ソ連社会の対立を詩的散文で描いた1920年代代表作。", 4, "invariant", "tier1", "yes"),
    ("ブルガーコフ『犬の心臓』詳論", "Bulgakov Heart of a Dog", "Собачье сердце", "cyrillic", P_SOVIET_MID, R_RUS,
     "1925年の風刺中編。犬から人への移植実験で新ソ連人を諷した寓意作。", 4, "invariant", "tier1", "yes"),

    # Cluster 5: Slavic (6)
    ("ハシェク『勇敢な兵士シュヴェイク』詳論", "Hašek The Good Soldier Schweik", "Osudy dobrého vojáka Švejka", "latin", P_CZECH, R_RUS,
     "1921-1923年のチェコ風刺長編。愚直な兵士を通じハプスブルク軍を笑い飛ばす。", 5, "invariant", "tier1", "yes"),
    ("ミツキェヴィチ『パン・タデウシュ』詳論", "Mickiewicz Pan Tadeusz detailed", "Pan Tadeusz", "latin", P_POLAND, R_RUS,
     "1834年のポーランド民族叙事詩。リトアニア貴族社会の郷愁を描いた国民的古典。", 5, "invariant", "tier1", "yes"),
    ("シュルツ『シナモン書房』詳論", "Schulz Cinnamon Shops detailed", "Sklepy cynamonowe", "latin", P_POLAND, R_RUS,
     "1934年短編集。父と少年の幻想的小宇宙を神話的散文で描くポーランド・モダニズム。", 5, "invariant", "tier1", "yes"),
    ("ゴンブローヴィチ『フェルディドゥルケ』詳論", "Gombrowicz Ferdydurke", "Ferdydurke", "latin", P_POLAND, R_RUS,
     "1937年のポーランド前衛小説。形式と未熟さの問題を諧謔と歪みで解体。", 5, "invariant", "tier1", "yes"),
    ("トカルチュク『フライト/逃亡派』", "Tokarczuk Flights", "Bieguni", "latin", P_POLAND, R_RUS,
     "2007年のポーランド断章小説。旅と身体の断片群でノーベル賞作家の代表作となった。", 4, "invariant", "tier1", "yes"),
    ("クラスナホルカイ『サタンタンゴ』詳論", "Krasznahorkai Satantango", "Sátántangó", "latin", P_CZECH, R_RUS,
     "1985年のハンガリー長編。寒村の終末と疑似救済者を長文体で描く東欧暗黒小説。", 4, "invariant", "tier1", "yes"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in concepts:
        (name_ja, name_en, name_orig, script, pid, region, definition, imp, ftrans, tier, canonical) = c
        if len(definition) > 100:
            print(f"WARN definition too long ({len(definition)}): {name_ja}", file=sys.stderr)
        # check duplicate by (name_ja, region, period_id)
        cur.execute("SELECT id FROM concepts WHERE name_ja=? AND region=? AND IFNULL(period_id,-1)=IFNULL(?,-1)",
                    (name_ja, region, pid))
        if cur.fetchone():
            skipped += 1
            continue
        cur.execute("""
            INSERT INTO concepts
              (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
               definition, importance_score, fourth_transform_status, source_tier, canonical_in_region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, region, pid,
              definition, imp, ftrans, tier, canonical))
        inserted += 1
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"inserted={inserted} skipped={skipped} subfield18_total={total}")

if __name__ == "__main__":
    main()
