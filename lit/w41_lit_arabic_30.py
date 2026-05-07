from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_arabic", region="南西アジア", period_id=None)

CONCEPTS = [
    # 1. 地方少数口承
    dict(**C, name_ja="ハッサーニーヤのタブラア女性短詩",
         name_en="Hassaniyya tabraa women's quatrains",
         name_original="التبراع الحساني", definition="サハラ女性が匿名で恋情を詠むハッサーニーヤ短詩。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ティハーマ婚礼ザーミル",
         name_en="Tihama wedding zamil chants",
         name_original="زامل تهامي", definition="紅海沿岸イエメンの婚礼で応唱される短い部族詩。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ヌビア・アラビア語マワーウィール",
         name_en="Nubian Arabic mawwal songs",
         name_original="مواويل نوبية عربية", definition="ヌビア移住記憶を長母音旋律で語る口語歌謡。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="バーレーン真珠歌フィジュリ断章",
         name_en="Bahraini fijiri pearl-diving fragments",
         name_original="فجري بحريني", definition="真珠潜水労働の号令と哀歌が混じる湾岸歌謡断章。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ジャバル・アームル婚礼アターバ",
         name_en="Jabal Amil wedding ataba",
         name_original="عتابا جبل عامل", definition="南レバノン農村婚礼で歌われる四行口語詩型。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="マフラ沿岸の海難ナシード",
         name_en="Mahra coastal shipwreck nashid",
         name_original="نشيد مهري ساحلي", definition="南アラビア沿岸の遭難記憶を歌う半アラビア語詠唱。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),

    # 2. 忘却された作品・作家
    dict(**C, name_ja="イブン・シュハイド『従者と悪霊の書簡』",
         name_en="Ibn Shuhayd Risalat al-tawabi wa-l-zawabi",
         name_original="رسالة التوابع والزوابع", definition="霊界批評旅行として読まれるアンダルス奇想散文。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="フスリー・カイラワーニー『アダブの花』",
         name_en="al-Husri al-Qayrawani Zahr al-adab",
         name_original="زهر الآداب", definition="イフリーキヤで編まれた逸話・詩句の文苑集。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="イブン・ナキヤー『マカーマート』",
         name_en="Ibn Naqiya Maqamat",
         name_original="مقامات ابن ناقيا", definition="バグダード後期の皮肉と語彙遊戯を含むマカーマ集。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="イブン・アル＝ジャウズィー『愚者譚』",
         name_en="Ibn al-Jawzi Akhbar al-hamqa",
         name_original="أخبار الحمقى والمغفلين", definition="愚者逸話を教訓と笑いへ配列した説教師散文。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="イブン・アラビー『神聖伝承集』文学読解",
         name_en="literary readings of Ibn Arabi's Mishkat",
         name_original="مشكاة الأنوار", definition="聖伝承配列を神秘的散文構成として読む小論点。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="シャーブ・ザリーフのマムルーク小詩",
         name_en="Shabb al-Zarif Mamluk lyric miniatures",
         name_original="الشاب الظريف", definition="後期都市生活の機知と恋を縮約する小詩群。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 3. 写本・注釈伝承
    dict(**C, name_ja="サヌアー大モスク詩選写本断簡",
         name_en="Sanaa Great Mosque poetry anthology fragments",
         name_original="مختارات شعرية صنعانية", definition="イエメン写本庫に残る詩選断簡と異読の小伝統。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ダマスクス蔵ブスィーリー欄外讃詩",
         name_en="Damascus Busiri marginal praise poems",
         name_original="هوامش البوصيري", definition="ブルダ写本余白に増殖した追和・祈願詩の書写層。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ティンブクトゥ蔵マグリブ韻律手控え",
         name_en="Timbuktu Maghrebi prosody notebooks",
         name_original="كناشات عروضية مغربية", definition="西サハラ学習圏で用いられた韻律暗記用小写本。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="アレッポ詞華集の紙片再利用",
         name_en="Aleppo anthology palimpsest slips",
         name_original="رقاع مختارات حلبية", definition="詩選写本の補修紙に残る都市詩片の再利用例。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ムワッシャハ・ハルジャ異読表",
         name_en="kharja variant tables in muwashshah studies",
         name_original="اختلافات الخرجة", definition="終句ハルジャのロマンス語・口語異読を対照する伝承表。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="カイロ講釈本のアンタル欄外系図",
         name_en="Cairo Antara chapbook marginal genealogies",
         name_original="أنساب عنتر الهامشية", definition="民衆本余白に付されたアンタル一族系図の小系統。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),

    # 4. サブジャンル変種
    dict(**C, name_ja="マワーリヤー四行俗謡",
         name_en="mawaliya vernacular quatrain",
         name_original="المواليا", definition="職人・市場語りに広がった押韻四行の口語詩型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="カン・ワ・カン物語詩",
         name_en="kan wa-kan narrative verse",
         name_original="كان وكان", definition="マムルーク期に流行した物語性の強い俗語詩形式。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ドゥバイト・マシュリク化",
         name_en="Mashriqi adaptations of dubayt",
         name_original="دوبيت مشرقي", definition="ペルシア系四行詩が東アラブで変形した詩型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ムサンマト追和詩",
         name_en="musammat contrafacta",
         name_original="معارضات المسمط", definition="連詩型ムサンマトへ同韻同拍で応じる詩作慣行。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ラマダーニーヤート季節詩",
         name_en="ramadaniyyat seasonal poems",
         name_original="رمضانيات", definition="断食月の灯火・施し・夜遊びを詠む季節詩群。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="クンムトラー掛詞詩",
         name_en="qunmutra pun poems",
         name_original="قنمطرة", definition="語頭語尾を入れ替える難解な言語遊戯詩の一種。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),

    # 5. 理論的ミクロ論争
    dict(**C, name_ja="タドミーン引用の剽窃境界論",
         name_en="tadmin quotation and plagiarism boundary",
         name_original="حدود التضمين", definition="詩句引用が技巧か盗用かを分ける古典批評論点。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="イクワー押韻欠陥の許容論",
         name_en="iqwa rhyme fault tolerance debate",
         name_original="الإقواء", definition="格母音ずれを韻律破綻とみなす範囲をめぐる議論。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="イータ反復韻の欠陥分類",
         name_en="ita repeated rhyme fault taxonomy",
         name_original="الإيطاء", definition="同語韻の反復を詩的欠陥へ分類する韻律論。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="タジュニース過剰批判",
         name_en="critique of excessive tajnis",
         name_original="الإفراط في التجنيس", definition="同音異義技巧の過多が意味を損なうかを問う論点。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="サジウ散文の韻律近接論",
         name_en="saj prose proximity to meter debate",
         name_original="السجع والعروض", definition="押韻散文が詩の韻律へ近づきすぎる問題の議論。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="マトブーウ詩人評価基準",
         name_en="criteria for matbu natural poets",
         name_original="الشاعر المطبوع", definition="天性詩人を技巧派から区別する批評上の判定基準。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
]


def main() -> None:
    before = None
    with LitDB("lit.sqlite") as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
            db.insert_concept(**concept)
    with LitDB("lit.sqlite") as db:
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
    print(f"inserted={after - before}")


if __name__ == "__main__":
    main()
