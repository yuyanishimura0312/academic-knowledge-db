from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_arabic", region="南西アジア")

CONCEPTS = [
    # 1. アンダルス女性詩
    dict(**C, name_ja="ワッラーダ・ビント・アル＝ムスタクフィー宮廷詩",
         name_en="Wallada bint al-Mustakfi court poetry", name_original="ولادة بنت المستكفي",
         period_id=139, definition="コルドバ王女詩人の恋愛・機知・自己顕示をめぐる短詩群。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ハフサ・ラクーニーヤ恋愛応酬詩",
         name_en="Hafsa Rakuniyya amatory exchange poetry", name_original="حفصة الركونية",
         period_id=139, definition="グラナダの女性詩人が書簡的応酬で展開した恋愛詩。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ムフジャ・アル＝クルトゥビーヤ諷刺詩",
         name_en="Muhja al-Qurtubiyya satirical poetry", name_original="مهجة القرطبية",
         period_id=139, definition="ワッラーダ周辺で知られるコルドバ女性詩人の鋭い諷刺短詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ナズフーン・アル＝クラシーヤ機知詩",
         name_en="Nazhun al-Qulai'iyya witty poetry", name_original="نزهون القلعية",
         period_id=139, definition="グラナダ女性詩人の即興性と応酬力を示す機知詩群。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="アーイシャ・アル＝クルトゥビーヤ学芸詩",
         name_en="Aisha al-Qurtubiyya learned poetry", name_original="عائشة القرطبية",
         period_id=139, definition="書記・学者として名高いアンダルス女性の詩文伝承。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="イティマード・アル＝ルマイキーヤ王妃詩",
         name_en="Itimad al-Rumaikiyya queenly poetry", name_original="اعتماد الرميكية",
         period_id=139, definition="セビリア王妃となった女性詩人の恋愛と宮廷記憶の詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 2. スーフィー女性
    dict(**C, name_ja="ラービア・アル＝アダウィーヤ祈祷詩",
         name_en="Rabia al-Adawiyya prayers", name_original="رابعة العدوية",
         period_id=18, definition="神への無償の愛を凝縮したバスラ女性聖者の祈祷句。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="アーイシャ・アル＝バーウーニーヤ神秘詩",
         name_en="Aisha al-Bauniyya mystical poetry", name_original="عائشة الباعونية",
         period_id=140, definition="マムルーク期女性スーフィーによる預言者称揚と神秘詩。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ムニーサ・ハートゥーン修道詩伝承",
         name_en="Munisa Khatun Sufi verse tradition", name_original="منيسة خاتون",
         period_id=251, definition="テッケ文化圏で語られる女性聖者の修道詩的伝承。",
         importance_score=3, source_tier="tertiary", canonical_in_region="major"),
    dict(**C, name_ja="ラーレーシュワリー・ヴァーク詩",
         name_en="Lalleshwari vakhs", name_original="لال دد",
         period_id=30, definition="カシミール女性神秘家の短詩ヴァークに見る脱制度的霊性。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ハヤーティ・ハートゥーン預言者称揚詩",
         name_en="Hayati Hatun devotional poetry", name_original="حياتي خاتون",
         period_id=251, definition="オスマン女性詩人による預言者称揚とディーワーン詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ダマスカスのラービア禁欲逸話",
         name_en="Rabia of Damascus ascetic anecdotes", name_original="رابعة الدمشقية",
         period_id=18, definition="シリア女性聖者として伝わる禁欲と祈りの逸話群。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 3. マムルーク・オスマン散文
    dict(**C, name_ja="イブン・イヤース年代記『バダーイウ』",
         name_en="Ibn Iyas Bada'i al-zuhur", name_original="بدائع الزهور",
         period_id=140, definition="マムルーク末期エジプトの政治崩壊を記録した年代記。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="マクリーズィー『ヒタト』都市誌",
         name_en="al-Maqrizi Khitat", name_original="المواعظ والاعتبار",
         period_id=140, definition="カイロの地誌・制度・記憶を集成したマムルーク都市誌。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="イブン・ハッリカーン『ワファヤート』列伝",
         name_en="Ibn Khallikan Wafayat al-ayan", name_original="وفيات الأعيان",
         period_id=140, definition="学者・詩人の没年と逸話を整理したアラブ列伝文学。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ナーイマー『ターリフ・イ・ナーイマー』",
         name_en="Naima Tarih-i Naima", name_original="تاريخ نعيما",
         period_id=140, definition="オスマン帝国の政治叙述を代表する宮廷年代記。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="エヴリヤ・チェレビー『セヤハトナーメ』",
         name_en="Evliya Celebi Seyahatname", name_original="سياحتنامه",
         period_id=140, definition="広域旅行を逸話・地誌・観察で綴るオスマン旅行記。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="キャーティブ・チェレビー『ミーザーン・アル＝ハック』",
         name_en="Katib Celebi Mizan al-Haqq", name_original="ميزان الحق",
         period_id=140, definition="宗教論争を均衡的判断で論じたオスマン知識人散文。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 4. 現代アラブ詩
    dict(**C, name_ja="サアディー・ユースフのイラク亡命詩",
         name_en="Saadi Yousef Iraqi exile poetry", name_original="سعدي يوسف",
         period_id=21, definition="政治亡命と日常語を交差させたイラク現代詩。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ムハンマド・アル＝マグート散文詩",
         name_en="Mohammad al-Maghout prose poetry", name_original="محمد الماغوط",
         period_id=21, definition="シリアの抑圧感覚を口語的散文詩で刻む現代詩。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="サリーム・バラカート越境詩",
         name_en="Salim Barakat Kurdish-Arabic poetry", name_original="سليم بركات",
         period_id=21, definition="クルド語的想像力をアラビア語詩に移植する越境詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="サルゴン・ブルス自由詩",
         name_en="Sargon Boulus free verse", name_original="سركون بولص",
         period_id=21, definition="イラク離散経験と都市感覚を結ぶ自由詩。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="ファドワー・トゥーカーン抵抗詩",
         name_en="Fadwa Tuqan Palestinian resistance poetry", name_original="فدوى طوقان",
         period_id=21, definition="女性の私的声とパレスチナ抵抗を結んだ詩作。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="エテル・アドナン多言語詩",
         name_en="Etel Adnan multilingual poetry", name_original="إيتيل عدنان",
         period_id=21, definition="レバノン離散と多言語感覚を横断する詩と散文。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),

    # 5. アラブ女性現代
    dict(**C, name_ja="フダー・バラカート『耕す水』",
         name_en="Hoda Barakat The Tiller of Waters", name_original="حارث المياه",
         period_id=21, definition="ベイルート内戦後の廃墟を織物記憶で読む小説。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="リアナ・バドル『鏡の眼』",
         name_en="Liana Badr Eye of the Mirror", name_original="عين المرآة",
         period_id=21, definition="テル・ザアタル虐殺を女性の証言で描くパレスチナ小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
    dict(**C, name_ja="サハル・ハリーファ『野生の棘』",
         name_en="Sahar Khalifeh Wild Thorns", name_original="الصبار",
         period_id=21, definition="占領下ナーブルスの抵抗と労働を描くパレスチナ小説。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ラティーファ・ザイヤート『開かれた扉』",
         name_en="Latifa al-Zayyat The Open Door", name_original="الباب المفتوح",
         period_id=21, definition="女性解放とエジプト民族運動を重ねる成長小説。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="ラドワー・アーシュール『グラナダ三部作』",
         name_en="Radwa Ashour Granada Trilogy", name_original="ثلاثية غرناطة",
         period_id=21, definition="アンダルス喪失を現代アラブ記憶へ接続する歴史小説。",
         importance_score=4, source_tier="secondary", canonical_in_region="core"),
    dict(**C, name_ja="アハダーフ・スウェイフ『愛の地図』歴史記憶",
         name_en="Ahdaf Soueif The Map of Love", name_original="خارطة الحب",
         period_id=21, definition="植民地期エジプトと現代を往還する英語圏アラブ小説。",
         importance_score=3, source_tier="secondary", canonical_in_region="major"),
]


def main() -> None:
    before = None
    with LitDB("lit.sqlite") as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
        for entry in CONCEPTS:
            db.insert_concept(**entry)
    with LitDB("lit.sqlite") as db:
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
    print(f"inserted={after - before}")


if __name__ == "__main__":
    main()
