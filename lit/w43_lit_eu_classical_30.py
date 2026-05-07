#!/usr/bin/env python3
"""Wave 43: 30 ultra-niche lit_eu_classical concepts."""

from lit_db_helper import LitDB


ROWS = [
    # 1: Homeric scholia and textual signs
    ("エクテシス欄外突出記法", "Ekthesis marginal projection", "ἔκθεσις", "greek", 199, "行頭を欄外に出し注目箇所を示す写本配置法"),
    ("コロメトリー行分割", "Colometry", "κωλομετρία", "greek", 198, "散文や詩を意味単位ごとに短行化する古代配置"),
    ("シグマ注記の同義反復標示", "Sigma scholion marker", "σίγμα", "greek", 199, "同義反復や重複行を示すホメロス注釈記号"),
    ("アンティシグマ校訂符号", "Antisigma critical sign", "ἀντίσιγμα", "greek", 199, "行順転倒や重複疑義を示すアレクサンドリア符号"),
    ("ケライオン句読符", "Keraion punctuation", "κεραία", "greek", 199, "写本で句切りや略号を示す小角状の記号"),
    ("ペリグラフェー抹消標示", "Perigraphe deletion mark", "περιγραφή", "greek", 199, "不要本文を囲って削除候補にする校訂操作"),
    # 2: Greek lyric meter microforms
    ("グリュコネイオン基底律", "Glyconic base", "γλυκώνειον", "greek", 5, "アイオリス抒情詩で多用される短い歌唱韻律"),
    ("ファライケイオン十一音節", "Phalaecian hendecasyllable", "hendecasyllabus", "latin", 5, "ギリシア小詩からカトゥッルスへ渡る十一音節律"),
    ("ヒッポナクテイオン跛行律", "Hipponactean choliamb", "χωλίαμβος", "greek", 5, "終脚を重くして罵倒詩に滑稽な跛行感を出す律"),
    ("レキュティオン喜劇韻脚", "Lecythion comic cadence", "ληκύθιον", "greek", 6, "悲劇詩句を茶化す喜劇的な短い韻律断片"),
    ("ドクミオス動揺律", "Dochmiac meter", "δόχμιος", "greek", 6, "悲劇の恐怖や混乱場面に用いる不安定な抒情律"),
    ("イオニコス・アポ・メイゾノス", "Ionic a maiore", "ἰωνικὸς ἀπὸ μείζονος", "greek", 5, "長長短短を基礎にした饗宴歌向きの韻律型"),
    # 3: Hellenistic book and epigram practices
    ("ピナケス的書誌分類", "Pinakes bibliographic taxonomy", "Πίνακες", "greek", 7, "アレクサンドリア図書館で著者とジャンルを分類する目録法"),
    ("シッリュボス巻物札", "Sillybos scroll tag", "σίλλυβος", "greek", 7, "巻物外側に題名や著者名を吊す識別札"),
    ("コロフォン書写末尾記", "Colophon subscription", "κολοφών", "greek", 7, "巻末に写本情報や題名を記す書誌的末尾文"),
    ("アナグノーシス朗読慣行", "Anagnosis reading practice", "ἀνάγνωσις", "greek", 7, "学芸サークルで詩文を声に出して披露する慣行"),
    ("スフラギス署名詩句", "Sphragis signature passage", "σφραγίς", "greek", 7, "詩人が作品末尾などに自己名を封印する句"),
    ("イソプセフィア数値エピグラム", "Isopsephic epigram", "ἰσοψηφία", "greek", 7, "文字数価の合計を趣向にするギリシア短詩"),
    # 4: Roman book culture and performance
    ("レキタティオ私的朗読会", "Recitatio", "recitatio", "latin", 75, "新作詩文を招待客の前で読む帝政期の文芸慣行"),
    ("リベルルス小冊子詩集", "Libellus poetry booklet", "libellus", "latin", 74, "短詩を小冊子単位で流通させるローマ詩集形態"),
    ("ティトゥルス巻物題札", "Titulus scroll label", "titulus", "latin", 75, "巻物端に付ける題名表示や所有標識"),
    ("ウンビリクス巻物軸端", "Umbilicus scroll boss", "umbilicus", "latin", 75, "巻物の軸端を飾り保護する突起部"),
    ("メンブラーナ冊子本移行", "Membrana codex shift", "membrana", "latin", 75, "羊皮紙冊子が巻物文化に割り込む初期の媒体転換"),
    ("パリンプセスト再利用写本", "Palimpsest reuse", "palimpsestus", "latin", 198, "旧本文を削り新本文を書いた再利用写本"),
    # 5: Late antique Christian and Byzantine microforms
    ("コンタキオン・エフュムニオン", "Kontakion ephymnion", "ἐφύμνιον", "greek", 199, "各連末で反復されるコンタキオンの折返し句"),
    ("カノン頌歌イルモス", "Canon heirmos", "εἱρμός", "greek", 199, "ビザンツ聖歌カノン各頌の旋律と韻律を導く冒頭詩節"),
    ("スティケロン単連聖歌", "Sticheron", "στιχηρόν", "greek", 199, "詩篇句に挿入される単連型のビザンツ典礼詩"),
    ("シナクサリオン短伝", "Synaxarion notice", "συναξάριον", "greek", 199, "祝日に読む聖人や出来事の短い典礼伝記"),
    ("メノロギオン月別聖人伝", "Menologion", "μηνολόγιον", "greek", 199, "月日順に聖人伝を配列するビザンツ読物集"),
    ("アクロスティック・テオトキオン", "Acrostic theotokion", "θεοτοκίον", "greek", 199, "聖母賛歌に頭字技巧を組み込む典礼詩形"),
]


def main() -> None:
    with LitDB() as db:
        inserted = 0
        for name_ja, name_en, name_original, script, period_id, definition in ROWS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code="lit_eu_classical",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"Inserted {inserted} concepts")


if __name__ == "__main__":
    main()
