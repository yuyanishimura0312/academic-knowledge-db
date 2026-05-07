#!/usr/bin/env python3
"""Wave 25 C03: Add 30 medieval EU concepts to subfield_id=2 (lit_eu_medieval).
Avoids existing entries via dedicated new concepts list.
"""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

conn = sqlite3.connect(str(DB))
cur = conn.cursor()


def pid(name):
    row = cur.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region='西欧'",
        (name,),
    ).fetchone()
    return row[0] if row else None


# Period mapping
P_IT_HIGH = pid("中世盛期イタリア") or pid("中世盛期後期（13世紀）")
P_IT_LATE = pid("トレチェント（14世紀イタリア）")
P_FR_CLASS = pid("中世フランス古典期")
P_FR_HIGH = pid("中世盛期（ロマネスク・初期ゴシック）")
P_FR_LATE = pid("中世晩期（14-15世紀）")
P_OC = pid("オック語抒情詩期")
P_IB = pid("イベリア中世")
P_DE_HIGH = pid("中高ドイツ期") or pid("中高ドイツ語期")
P_DE_LATE = pid("中世末期ゲルマン圏")
P_EN_LATE = pid("中英語盛期")

# 30 concepts: 5 clusters × 6
concepts = [
    # ===== Cluster 1: Italian medieval (6) =====
    ("ブルネット・ラティーニ『書の宝（Li Livres dou Tresor）』", "Li Livres dou Tresor", "Li Livres dou Tresor",
     "latin", P_IT_HIGH, "ブルネットがフランス語で著した百科全書的散文。倫理・修辞学を含む。", 4, "rethinking",
     "https://www.gutenberg.org/", "online_text"),
    ("チーノ・ダ・ピストイア『カンツォニエーレ』", "Cino da Pistoia Canzoniere", "Cino da Pistoia Canzoniere",
     "latin", P_IT_HIGH, "ペトラルカに影響を与えたドルチェ・スティル・ノーヴォ後期の抒情詩集。", 4, "invariant",
     None, None),
    ("カヴァルカンティ『私は見た（Vedete ch'i' son un）』", "Cavalcanti Vedete ch'i' son un", "Vedete ch'i' son un",
     "latin", P_IT_HIGH, "カヴァルカンティの自己省察的ソネット。愛による魂の動揺を描く代表作。", 3, "invariant",
     None, None),
    ("ラポ・ジャンニ『恋の優雅（Amor, eo chero mia donna）』", "Lapo Gianni Amor eo chero", "Amor, eo chero mia donna in salute",
     "latin", P_IT_HIGH, "スティルノヴィスティ第一世代ラポによる宮廷愛バラータ。優雅な様式の典型。", 3, "invariant",
     None, None),
    ("ヤコポーネ・ダ・トーディ『スタバト・マーテル』", "Stabat Mater", "Stabat Mater Dolorosa",
     "latin", P_IT_HIGH, "聖母の悲嘆を歌うラテン語ラウダ。中世末期から現代まで歌い継がれる宗教詩。", 5, "invariant",
     "https://www.gutenberg.org/", "online_text"),
    ("シチリア派ソネット形式の確立", "Sicilian Sonnet form establishment", "sonetto siciliano",
     "latin", P_IT_HIGH, "ジャコモ・ダ・レンティーニが創出した14行詩型。後の欧州ソネット史の起点。", 5, "invariant",
     None, None),

    # ===== Cluster 2: Old French (6) =====
    ("ヴァース『聖ニコラの生涯』", "Wace Vie de Saint Nicolas", "La Vie de Saint Nicolas",
     "latin", P_FR_HIGH, "ノルマン詩人ヴァースによる聖人伝。アングロ・ノルマン語聖人伝の先駆。", 3, "invariant",
     None, None),
    ("マリー・ド・フランス『レー集（十二のレー）』", "Marie de France Lais", "Les Lais de Marie de France",
     "latin", P_FR_HIGH, "12世紀後半に編まれた12篇のブルトン・レー詩集。宮廷愛と妖精譚を融合。", 5, "invariant",
     "https://www.gutenberg.org/ebooks/22387", "online_text"),
    ("マリー・ド・フランス『寓話集（イゾペ）』", "Marie de France Fables", "Ysopet",
     "latin", P_FR_HIGH, "イソップ寓話を古フランス語で再話した102篇の韻文寓話集。中世寓話の白眉。", 4, "invariant",
     None, None),
    ("『オーカッサンとニコレット』のシャントファブル形式", "Aucassin chantefable form", "chantefable",
     "latin", P_FR_HIGH, "散文と韻文を交互に置く独自の物語ジャンル形式。13世紀の唯一現存例。", 4, "rethinking",
     None, None),
    ("『ルナール物語』第1枝（Branche I）", "Roman de Renart Branche I", "Roman de Renart, Branche I",
     "latin", P_FR_HIGH, "獣寓話叙事詩の核心枝。狐ルナールと狼イザングランの法廷争いを描く。", 4, "invariant",
     "https://www.gutenberg.org/", "online_text"),
    ("クリスティーヌ・ド・ピザン『女性たちの都』", "Christine de Pizan Cité des Dames", "Le Livre de la Cité des Dames",
     "latin", P_FR_LATE, "1405年成立。歴史上の女性を集めた寓意都市。中世フェミニズムの古典。", 5, "rethinking",
     None, None),

    # ===== Cluster 3: Provençal (6) =====
    ("ベルナール・ド・ヴァンタドゥール『ひばりの歌（Can vei la lauzeta）』", "Can vei la lauzeta", "Can vei la lauzeta mover",
     "latin", P_OC, "失恋の絶望を歌う代表的カンソ。トルバドゥール抒情詩の頂点とされる。", 5, "invariant",
     None, None),
    ("ベルトラン・ド・ボルン『シルヴェンテス（戦讃歌）』", "Bertran de Born sirventes", "Be·m platz lo gais temps",
     "latin", P_OC, "戦闘讃美のシルヴェンテス。ダンテが地獄篇で言及した戦闘詩人の代表作。", 4, "rethinking",
     None, None),
    ("マルカブリュ『パストレラ』", "Marcabru pastorela", "L'autrier jost'una sebissa",
     "latin", P_OC, "騎士と羊飼い娘の対話詩。パストレラ（牧歌）ジャンルの始祖。", 4, "invariant",
     None, None),
    ("アルノー・ダニエルのセスティーナ", "Arnaut Daniel sestina", "Lo ferm voler qu'el cor m'intra",
     "latin", P_OC, "アルノーが発明した6行6連+トルナーダの韻型。ダンテ・ペトラルカが継承。", 5, "invariant",
     None, None),
    ("ベアトリス・ド・ディア『つらい歌（A chantar m'er）』", "Beatriz de Dia A chantar", "A chantar m'er de so qu'eu no volria",
     "latin", P_OC, "女性トルバドゥール（トロバイリッツ）唯一の旋律付き完詩。女性の声の自立。", 5, "rethinking",
     None, None),
    ("トロバール・クルス（閉じた詩風）", "trobar clus", "trobar clus",
     "latin", P_OC, "難解で閉ざされた詩風。マルカブリュ・アルノーらが追求した秘教的修辞美学。", 4, "invariant",
     None, None),

    # ===== Cluster 4: Iberian (6) =====
    ("『わがシッドの歌』の客観的写実主義", "Cantar de mio Cid realism", "Cantar de mio Cid",
     "latin", P_IB, "1207年写本。スペイン国民叙事詩。誇張を排した史実的写実が特徴。", 5, "invariant",
     "https://www.gutenberg.org/ebooks/14977", "online_text"),
    ("ゴンサロ・デ・ベルセオ『聖ドミニコ伝』", "Berceo Vida de Santo Domingo", "Vida de Santo Domingo de Silos",
     "latin", P_IB, "メステル・デ・クレレシーアの代表作。教養僧侶詩の規範を示す聖人伝。", 3, "invariant",
     None, None),
    ("メステル・デ・クレレシーア（教養僧侶詩派）", "mester de clerecía", "mester de clerecía",
     "latin", P_IB, "13-14世紀イベリア半島の教養詩運動。クアデルナ・ヴィーア（4行14音節）を用いる。", 4, "invariant",
     None, None),
    ("フアン・ルイス『良き愛の書』のパロディ性", "Buen Amor parody dimension", "Libro de buen amor",
     "latin", P_IB, "1330/43年。聖俗・宗教愛・肉欲愛を多層的に交錯させたパロディ百科。", 5, "rethinking",
     None, None),
    ("ホルヘ・マンリケ『コプラス』のウビ・スント主題", "Coplas ubi sunt motif", "ubi sunt qui ante nos",
     "latin", P_IB, "1476年。父の死を悼む哀歌。中世ウビ・スント詩想の頂点を示す代表作。", 4, "invariant",
     None, None),
    ("『セレスティーナ』の対話小説形式", "Celestina dialogue novel form", "comedia humanística",
     "latin", P_IB, "1499年。21幕の対話劇。喜劇・小説の境界を越えた人文主義劇の傑作。", 5, "rethinking",
     None, None),

    # ===== Cluster 5: German + English (6) =====
    ("ヴァルター・フォン・デア・フォーゲルヴァイデ『菩提樹の下で』", "Walther Under der linden", "Under der linden",
     "latin", P_DE_HIGH, "ミンネザング代表作。庶民女性の恋愛体験を一人称で歌う革新的抒情。", 5, "invariant",
     None, None),
    ("ヴォルフラム『パルチヴァール』の聖杯神学", "Parzival grail theology", "Parzival",
     "latin", P_DE_HIGH, "1210頃。聖杯探求と内面的成長を統合したアーサー王ロマンスの最高峰。", 5, "invariant",
     "https://www.gutenberg.org/", "online_text"),
    ("ヒルデガルト・フォン・ビンゲン『道を知れ（Scivias）』", "Hildegard Scivias", "Scivias - Scito vias Domini",
     "latin", P_DE_HIGH, "12世紀ベネディクト会修道女ヒルデガルトの幻視神学書。図像と詩文を融合。", 5, "rethinking",
     None, None),
    ("メヒティルト・フォン・マクデブルク『神性の流れる光』神秘主義", "Mechthild mysticism", "Das fließende Licht der Gottheit",
     "latin", P_DE_HIGH, "13世紀女性神秘家の俗語散文神秘主義。低地ドイツ語による愛の神秘体験記述。", 5, "rethinking",
     None, None),
    ("パール詩人『清浄（Cleanness）』", "Pearl Poet Cleanness", "Cleanness (Purity)",
     "latin", P_EN_LATE, "ガウェイン詩人写本収録の頭韻詩。聖書例話で清浄の徳を説く道徳詩。", 4, "invariant",
     None, None),
    ("マージェリー・ケンプ『マージェリー・ケンプの書』の自伝形式", "Margery Kempe autobiography form", "The Book of Margery Kempe",
     "latin", P_EN_LATE, "1438頃口述完成。英語最古の自伝。女性の宗教体験と巡礼を口述記録。", 5, "rethinking",
     None, None),
]

inserted = 0
skipped = 0
errors = []

for row in concepts:
    name_ja, name_en, name_orig, script, p_id, definition, importance, fourth, src_url, src_type = row
    if len(definition) > 100:
        errors.append(f"DEF_OVER: {name_ja} ({len(definition)} chars)")
        continue
    try:
        cur.execute(
            """
            INSERT INTO concepts(
                name_ja, name_en, name_original, original_script,
                subfield_id, region, period_id, definition,
                importance_score, fourth_transform_status,
                primary_source_url, primary_source_type,
                source_tier, canonical_in_region
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                name_ja, name_en, name_orig, script,
                2, "西欧", p_id, definition,
                importance, fourth,
                src_url, src_type,
                "tier1", "yes",
            ),
        )
        inserted += 1
    except sqlite3.IntegrityError as e:
        skipped += 1
        errors.append(f"SKIP: {name_ja} :: {e}")

conn.commit()

# Final counts
total_sub2 = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=2").fetchone()[0]
print(f"INSERTED: {inserted}")
print(f"SKIPPED: {skipped}")
print(f"TOTAL subfield_id=2: {total_sub2}")
if errors:
    print("--- notes ---")
    for e in errors[:20]:
        print(e)

conn.close()
