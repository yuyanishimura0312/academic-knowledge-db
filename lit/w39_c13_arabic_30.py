from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_arabic", region="南西アジア")

CONCEPTS = [
    # 1. ジャーヒリーヤ・初期イスラーム周縁詩
    dict(**C, name_ja="シャンファラー『ラーミーヤト・アル＝アラブ』",
         name_en="al-Shanfara Lamiyyat al-Arab", name_original="لامية العرب",
         original_script="arabic", period_id=16,
         definition="追放者の誇りと砂漠倫理を凝縮したサアリーク詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="タアッバタ・シャッラン盗賊詩",
         name_en="Ta'abbata Sharran brigand poetry", name_original="تأبط شرا",
         original_script="arabic", period_id=16,
         definition="逃走・夜襲・孤独を誇るジャーヒリーヤ盗賊詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ウルワ・イブン・アル＝ワルド貧者詩",
         name_en="Urwa ibn al-Ward poor men's poetry", name_original="عروة بن الورد",
         original_script="arabic", period_id=16,
         definition="部族外の貧者連帯を歌うサアリーク詩人の詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ムハルヒル・イブン・ラビーア復讐詩",
         name_en="al-Muhalhil vengeance poetry", name_original="المهلهل بن ربيعة",
         original_script="arabic", period_id=16,
         definition="バスース戦争伝承に結びつく復讐と哀悼の詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="アルカマ・アル＝ファフル宮廷詩",
         name_en="Alqama al-Fahl court poetry", name_original="علقمة الفحل",
         original_script="arabic", period_id=16,
         definition="ヒーラ宮廷周辺で洗練された競詠型カスィーダ。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="アル＝フタイア諷刺短詩",
         name_en="al-Hutay'a satirical short poems", name_original="الحطيئة",
         original_script="arabic", period_id=17,
         definition="改宗期の社会的緊張を辛辣に刻む諷刺詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 2. アッバース朝アダブ細目
    dict(**C, name_ja="イブン・アブド・ラッビヒ『唯一の首飾り』",
         name_en="Ibn Abd Rabbih al-Iqd al-Farid", name_original="العقد الفريد",
         original_script="arabic", period_id=18,
         definition="アンダルスで編まれたアッバース的アダブ詞華集。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="タヌーヒー『座談の余話』",
         name_en="al-Tanukhi Nishwar al-Muhadara", name_original="نشوار المحاضرة",
         original_script="arabic", period_id=18,
         definition="裁判官世界の逸話を集めた十世紀アダブ散文。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="アブー・アリー・アル＝カーリー『アマーリー』",
         name_en="Abu Ali al-Qali al-Amali", name_original="الأمالي",
         original_script="arabic", period_id=18,
         definition="口述講義形式で伝える語彙・詩・逸話の集成。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ムバッラド『アル＝カーミル』",
         name_en="al-Mubarrad al-Kamil", name_original="الكامل",
         original_script="arabic", period_id=18,
         definition="文法家が詩文例で編んだ古典アダブ読本。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="スーリー『アブー・タンマーム伝』",
         name_en="al-Suli Akhbar Abi Tammam", name_original="أخبار أبي تمام",
         original_script="arabic", period_id=18,
         definition="詩人の逸話と受容を記す初期文学伝記。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イブン・アル＝ジャウズィー『愚者列伝』",
         name_en="Ibn al-Jawzi Akhbar al-Hamqa", name_original="أخبار الحمقى والمغفلين",
         original_script="arabic", period_id=18,
         definition="愚者逸話を倫理的笑いへ編成したアダブ小品集。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 3. アンダルス・マグレブ細部伝統
    dict(**C, name_ja="イブン・バッサーム『ダヒーラ』",
         name_en="Ibn Bassam al-Dhakhira", name_original="الذخيرة في محاسن أهل الجزيرة",
         original_script="arabic", period_id=139,
         definition="アンダルス諸詩人を地域別に収める大部の詞華集。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イブン・アブドゥーンのセビリア哀歌",
         name_en="Ibn Abdun elegy for Seville", name_original="قصيدة ابن عبدون",
         original_script="arabic", period_id=139,
         definition="アッバード朝没落を悼む政治的廃墟詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="アアマー・アッ＝トゥティーリー恋愛詩",
         name_en="al-Ama al-Tutili love poetry", name_original="الأعمى التطيلي",
         original_script="arabic", period_id=139,
         definition="トゥデラ盲目詩人の音楽性を帯びた恋愛詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ルサーフィー・アル＝バランスィー郷愁詩",
         name_en="al-Rusafi al-Balansi nostalgia poetry", name_original="الرصافي البلنسي",
         original_script="arabic", period_id=139,
         definition="バレンシア喪失を庭園記憶に重ねる郷愁詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イブン・ザムラク宮殿碑文詩",
         name_en="Ibn Zamrak palace inscription poetry", name_original="ابن زمرك",
         original_script="arabic", period_id=139,
         definition="アルハンブラ装飾に刻まれたナスル朝宮廷詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ティファーシー『心の悦楽』",
         name_en="al-Tifashi Nuzhat al-Albab", name_original="نزهة الألباب",
         original_script="arabic", period_id=140,
         definition="性愛逸話を分類する中世マグレブの艶笑散文。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 4. マムルーク・オスマン期マイナー散文
    dict(**C, name_ja="イブン・ダーニヤール影絵戯曲",
         name_en="Ibn Daniyal shadow plays", name_original="طيف الخيال",
         original_script="arabic", period_id=140,
         definition="カイロ庶民風俗を笑劇化した影絵劇三部作。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ブースィーリー『ブルダ』写本伝統",
         name_en="al-Busiri Burda manuscript tradition", name_original="البردة",
         original_script="arabic", period_id=140,
         definition="預言者称揚詩が写本・朗誦で増殖した伝統。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="カルカシャンディー『暁光』書記術",
         name_en="al-Qalqashandi Subh al-Asha", name_original="صبح الأعشى",
         original_script="arabic", period_id=140,
         definition="マムルーク官僚の文書作法を体系化した百科全書。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ヌワイリー『文学の究極目的』",
         name_en="al-Nuwayri Nihayat al-Arab", name_original="نهاية الأرب",
         original_script="arabic", period_id=140,
         definition="宇宙・歴史・文学を配列したマムルーク百科全書。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イブシーヒー『ムスタトラフ』",
         name_en="al-Ibshihi al-Mustatraf", name_original="المستطرف",
         original_script="arabic", period_id=140,
         definition="逸話・格言・詩を軽妙に配した後期アダブ集。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ナーブルスィー『真理への旅』",
         name_en="Abd al-Ghani al-Nabulsi al-Haqiqa", name_original="الحقيقة والمجاز",
         original_script="arabic", period_id=140,
         definition="シリア聖地巡礼を神秘主義的観察で綴る旅行記。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 5. 近現代地域小説・実験
    dict(**C, name_ja="エドワール・アル＝ハッラート『ラーマ』実験小説",
         name_en="Edwar al-Kharrat Rama experimental fiction", name_original="رامة والتنين",
         original_script="arabic", period_id=21,
         definition="アレクサンドリア記憶を断片化するエジプト実験小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ソンアッラー・イブラーヒーム『委員会』",
         name_en="Sonallah Ibrahim The Committee", name_original="اللجنة",
         original_script="arabic", period_id=21,
         definition="官僚制と監視を冷笑的に描くエジプト短長編。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="フアード・アル＝タカルリー『長い帰路』",
         name_en="Fuad al-Takarli The Long Way Back", name_original="الرجع البعيد",
         original_script="arabic", period_id=21,
         definition="バグダード家庭の崩壊に政治暴力を映す小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ジャブラ・イブラーヒーム・ジャブラ『船』",
         name_en="Jabra Ibrahim Jabra The Ship", name_original="السفينة",
         original_script="arabic", period_id=21,
         definition="船上空間で亡命知識人の記憶を交錯させる小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イブラーヒーム・アル＝クーニー砂漠神話小説",
         name_en="Ibrahim al-Koni desert myth fiction", name_original="إبراهيم الكوني",
         original_script="arabic", period_id=21,
         definition="トゥアレグ神話と砂漠倫理をアラビア語で小説化。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ライラー・アル＝ウスマーン湾岸女性小説",
         name_en="Laila al-Othman Gulf women's fiction", name_original="ليلى العثمان",
         original_script="arabic", period_id=21,
         definition="クウェート社会の性規範を女性視点で描く小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
]


def main() -> None:
    for entry in CONCEPTS:
        if len(entry["definition"]) > 100:
            raise ValueError(f"definition too long: {entry['name_ja']}")

    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 13"
            )
        }
        dupes = [entry["name_ja"] for entry in CONCEPTS if entry["name_ja"] in existing]
        if dupes:
            raise ValueError(f"duplicates already present: {dupes}")

        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 13"
        ).fetchone()[0]
        for entry in CONCEPTS:
            db.insert_concept(**entry)
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 13"
        ).fetchone()[0]

    print(f"inserted={after - before}")


if __name__ == "__main__":
    main()
