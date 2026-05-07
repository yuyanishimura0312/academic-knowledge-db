from lit_db_helper import LitDB


REGION = "グローバルサウス"

P = {
    "oral": 61,
    "colonial": 62,
    "anti": 63,
    "post": 149,
    "contemporary": 150,
    "maghreb": 151,
    "lusophone": 152,
    "egypt_sudan": 248,
}

CONCEPTS = [
    # 口承・写本の局地形式
    ("アジャミ・フルフルデ書簡詩", "Ajami Fulfulde epistolary verse", "西アフリカのフルフルデ語アラビア文字詩文。", P["oral"]),
    ("ソマリ・ガベイ即興論争", "Somali gabay poetic duel", "ソマリ長詩ガベイの即興応酬と批評慣行。", P["oral"]),
    ("タマシェク・テソワイ恋愛歌", "Tamasheq tesawit love song", "トゥアレグ女性歌唱に残る恋愛短詩形式。", P["oral"]),
    ("ワガドゥ叙事詩断片", "Wagadu epic fragments", "ソニンケ語圏に伝わるガーナ王国滅亡叙事断片。", P["oral"]),
    ("マダガスカル・ハインテニ", "Malagasy hain-teny", "メリナ宮廷由来の謎掛け的恋愛詩話。", P["oral"]),
    ("マンデ狩猟歌ドンソンコ", "Mande donsonkoni hunters' song", "狩猟結社の系譜・呪力を語るマンデ歌謡。", P["oral"]),
    # 地域小出版・新聞圏
    ("ルバ語カタンガ鉱山歌", "Luba Katanga mine songs", "カタンガ鉱山労働を歌うルバ語圏の都市口承。", P["colonial"]),
    ("コサ語インボンギ新聞詩", "Xhosa imbongi newspaper verse", "初期コサ語新聞に載った賛歌詩の書記化。", P["colonial"]),
    ("キクユ語ムウィガニャ印刷詩", "Kikuyu Muigwithania verse", "ムウィガニャ紙周辺のキクユ語短詩・政治詩。", P["colonial"]),
    ("エウェ語会衆劇台本", "Ewe congregational drama", "宣教学校と教会で演じられたエウェ語宗教劇。", P["colonial"]),
    ("リンガラ・植民地兵士歌", "Lingala colonial soldier songs", "フォルス・ピュブリック周辺の兵士歌謡。", P["colonial"]),
    ("ザンジバル・ターラブ歌詞帳", "Zanzibar taarab lyric booklets", "スワヒリ語ターラブの小冊子化された歌詞文化。", P["colonial"]),
    # 忘れられた作品・作家
    ("カジ・ナズルルのアビシニア詩", "Nazrul Abyssinia poems", "エチオピア戦争を扱うベンガル語反帝国詩。", P["anti"]),
    ("ラビ・ベン・スーサン写本", "Rabbi Ben Soussan manuscripts", "モロッコ・ユダヤ系アラビア語詩写本の伝承。", P["maghreb"]),
    ("ファジル・ゲビの宮廷年代記", "Fasil Ghebbi court chronicles", "ゴンダール宮廷周辺で編まれたゲエズ語年代記群。", P["oral"]),
    ("エフライム・アマのエウェ小説", "Ephraim Amu Ewe prose", "エウェ語文化復興期の散文実験と教育文学。", P["colonial"]),
    ("ムベラ・ソネ・ディプコ『悲しみの数』", "Mbella Sonne Dipoko's A Few Nights and Days", "英語圏カメルーン初期小説の忘却された一作。", P["post"]),
    ("ユスフ・ファデル初期演劇", "Youssef Fadel early theatre", "モロッコ独立後の投獄経験を映す初期戯曲群。", P["maghreb"]),
    # サブジャンル変種
    ("アカン語アンサ物語変種", "Akan Ananse variant cycles", "アナンセ譚のアカン語地域別モチーフ連鎖。", P["oral"]),
    ("ウォロフ語タージャーブーン風刺歌", "Wolof taajaboon satire songs", "セネガル都市祭礼の子ども風刺歌謡。", P["oral"]),
    ("シンディカリスト鉱山小説", "Southern African syndicalist mine fiction", "南部アフリカ労働運動系の鉱山短編小説。", P["post"]),
    ("ナイル・ヌビア追悼歌", "Nile Nubian lament songs", "水没・移住記憶を担うヌビア語追悼歌。", P["egypt_sudan"]),
    ("ハラリ語ワズィーマ詩", "Harari wazima verse", "ハラール旧市街の女性儀礼に伴う短詩形式。", P["oral"]),
    ("クレオール語サントメ小説", "Santome Creole fiction", "フォロ語・アンゴラール語を絡める島嶼散文。", P["lusophone"]),
    # 理論的ミクロ論争
    ("アジャミ翻字不能性論争", "Ajami untranslatability debate", "アジャミ文学の音価・聖性をめぐる翻訳論争。", P["contemporary"]),
    ("オラル・テキスト境界論", "oral-text boundary debate", "口承採録物を作品と資料のどちらに置くかの小論争。", P["contemporary"]),
    ("グリオ著作権帰属問題", "griot copyright attribution", "演者・採録者・家系の権利帰属をめぐる議論。", P["contemporary"]),
    ("少数語自費出版正典化", "minor-language self-publishing canonization", "少数語小出版を地域正典に含めるかの議論。", P["contemporary"]),
    ("植民地民族誌の詩化問題", "poeticization of colonial ethnography", "民族誌採録歌を文学化して読む方法上の問題。", P["contemporary"]),
    ("アフリカ写本デジタル帰還", "African manuscript digital return", "海外所蔵写本のデジタル返還と読解権をめぐる論点。", P["contemporary"]),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        before = db.conn.total_changes
        for name_ja, name_en, definition, period_id in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_africa",
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
        print(f"inserted={db.conn.total_changes - before}")


if __name__ == "__main__":
    main()
