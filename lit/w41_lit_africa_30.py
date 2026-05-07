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
    # サヘル・アジャミ写本の微細伝統
    ("ウォロフ語アジャミ・カスィーダ", "Wolof Ajami qasida", "ムリッド教団圏で筆写されたウォロフ語讃歌詩。", P["oral"]),
    ("ハウサ語タワッスル詩", "Hausa tawassul verse", "聖者仲介を求めるハウサ語アジャミ祈願詩。", P["oral"]),
    ("カヌリ語マラブー写本詩", "Kanuri marabout manuscript verse", "ボルヌ周辺の学僧家系に伝わるカヌリ語宗教詩。", P["oral"]),
    ("ソニンケ語アジャミ商人書簡", "Soninke Ajami merchant letters", "交易家族が残したソニンケ語アラビア文字書簡。", P["colonial"]),
    ("マンデ語ワリ占い注釈詩", "Mande wali divination gloss verse", "護符占い文献に付くマンデ語の短い注釈詩。", P["oral"]),
    ("フータ・ジャロン説教詩断簡", "Futa Jallon sermon verse fragments", "フルベ学僧圏に残る説教調アジャミ詩断簡。", P["oral"]),
    # 島嶼・沿岸の小ジャンル
    ("シェラ語ラム詩謡", "Shela Lamu verse songs", "ラム島シェラ地区のスワヒリ語婚礼詩謡。", P["oral"]),
    ("コモロ語シンドゥジ詩", "Comorian shindzuzi verse", "コモロ諸島の式典で唱和される短詩形式。", P["oral"]),
    ("レユニオン・マロヤ歌詞冊子", "Reunion maloya lyric booklets", "島嶼クレオール抵抗歌の小冊子化された歌詞。", P["contemporary"]),
    ("カーボベルデ・モルナ筆写歌集", "Cape Verde morna manuscript songbooks", "モルナ歌詞を家族単位で写した手稿歌集。", P["lusophone"]),
    ("ギニアビサウ・クレオール劇台本", "Guinea-Bissau Creole play scripts", "独立後のクレオール語民衆劇の台本群。", P["lusophone"]),
    ("マヨット・シマオレ婚礼歌", "Maore wedding songs", "マヨットのシマオレ語で歌われる婚礼掛け合い歌。", P["oral"]),
    # 少数語印刷・新聞文化
    ("ツワナ語モリミ新聞詩", "Tswana Morimi newspaper verse", "初期ツワナ語紙に載った教訓詩と時事詩。", P["colonial"]),
    ("ガ語アクラ市場小説", "Ga Accra market fiction", "アクラ露店印刷で流通したガ語短編小説。", P["post"]),
    ("イドマ語教会劇冊子", "Idoma church drama pamphlets", "中部ナイジェリア宣教圏のイドマ語宗教劇冊子。", P["colonial"]),
    ("セペディ語労働者自伝", "Sepedi worker autobiographies", "鉱山移住者がセペディ語で綴った生活記録。", P["post"]),
    ("ルガンダ語エビカ新聞風刺", "Luganda Ebika newspaper satire", "氏族紙面に現れるルガンダ語の短い政治風刺。", P["colonial"]),
    ("ショナ語ムウェジ小説欄", "Shona Mwedzi fiction columns", "月刊誌の連載欄で育ったショナ語大衆小説。", P["post"]),
    # 忘却作家・未翻訳作品
    ("セク・トゥレ期スス語詩", "Susu poetry under Sekou Toure", "ギニア文化政策下で作られたスス語政治詩。", P["anti"]),
    ("ベルナール・ダディエ初期童話", "Bernard Dadie early tales", "植民地期雑誌に散在した初期フランス語童話。", P["colonial"]),
    ("エベネザー・オベイ歌曲詞", "Ebenezer Obey song lyrics", "ヨルバ・ジュジュ音楽における教訓的歌詞群。", P["contemporary"]),
    ("ジャン・プリヤ『夜の女』", "Jean Pliya, La secretaire particuliere", "ベナン演劇の官僚制風刺を担う仏語戯曲。", P["post"]),
    ("アルファ・マンデ・ジャロ詩", "Alpha Mande Diallo poetry", "ギニア移民経験を綴る未翻訳フランス語詩。", P["contemporary"]),
    ("モハメド・ハイル＝エディン断章詩", "Mohammed Khaïr-Eddine fragment poems", "モロッコ前衛の破片的仏語詩作群。", P["maghreb"]),
    # 理論的ミクロ論争
    ("アフリカ口承採録者署名問題", "African oral collector signature problem", "採録者名を著者欄に置く慣行への批判論点。", P["contemporary"]),
    ("アジャミOCR正規化論争", "Ajami OCR normalization debate", "アジャミ文字認識で発音差を消すかの論争。", P["contemporary"]),
    ("少数語文学賞資格論争", "minor-language prize eligibility debate", "翻訳経由作品を文学賞対象に含めるかの議論。", P["contemporary"]),
    ("歌詞文学の正典化問題", "song-lyric canonization problem", "大衆音楽歌詞を文学正典へ入れる可否の論点。", P["contemporary"]),
    ("写本返還メタデータ所有権", "manuscript return metadata ownership", "返還データの記述権を誰が持つかの論争。", P["contemporary"]),
    ("口承AI合成声の真正性", "AI synthetic voice authenticity in orature", "故人の声で口承を再現する際の真正性問題。", P["contemporary"]),
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
