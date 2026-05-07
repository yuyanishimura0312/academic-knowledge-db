#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"

CONCEPTS = [
    # Cluster 1: premodern manuscript and religious relay
    ("コプト語外典のアラビア語説教訳", "Arabic homiletic translation of Coptic apocrypha", "Coptic apocrypha", "コプト外典がアラビア語説教へ組み替えられる写本翻訳。", "北アフリカ"),
    ("グルジア聖人伝のアルメニア語重訳", "Armenian relay of Georgian hagiography", "Georgian hagiography", "グルジア語聖人伝がアルメニア語で再流通する重訳層。", "コーカサス"),
    ("パフラヴィー知恵文学の新ペルシア語翻案", "New Persian adaptation of Pahlavi wisdom literature", "Pahlavi wisdom texts", "中世ペルシア知恵文学が新ペルシア語散文へ移る翻案。", "西アジア"),
    ("古教会スラヴ偽典のセルビア語写本訳", "Serbian manuscript translation of Slavonic apocrypha", "Slavonic apocrypha", "教会スラヴ語偽典をセルビア語写本圏が再語彙化する。", "バルカン"),
    ("ナワトル説教集の西語逐語対訳", "Spanish interlinear translation of Nahuatl sermons", "Nahuatl sermons", "ナワトル説教を西語逐語訳が植民地教学へ接続する。", "メソアメリカ"),
    ("チュルク語ユスフ物語のペルシア語逆訳", "Persian back-translation of Turkic Yusuf tales", "Yusuf tales", "チュルク語ユスフ物語がペルシア語へ戻る物語循環。", "中央アジア"),

    # Cluster 2: small-language mediation and bilingual publication
    ("マン島語民話の英語復興訳", "English revival translation of Manx folktales", "Manx folktales", "マン島語民話が英訳で言語復興教材へ変わる編集翻訳。", "西欧"),
    ("アストゥリアス語小説の西語窓口", "Spanish gateway translation of Asturian fiction", "Asturian fiction", "アストゥリアス語小説が西語版で国内出版網に入る経路。", "西欧"),
    ("ミランダ語詩の葡語併記出版", "Portuguese facing-text editions of Mirandese poetry", "Mirandese poetry", "ミランダ語詩を葡語併記が少数語文学として可視化する。", "西欧"),
    ("セトゥ語民謡のエストニア語編訳", "Estonian adaptation of Seto folksongs", "Seto folksongs", "セトゥ語民謡がエストニア語編訳で国民民俗へ入る。", "バルト"),
    ("マリ語叙事詩のロシア語学術訳", "Russian scholarly translation of Mari epic", "Mari epic", "マリ語叙事詩が露語注釈訳で民族誌資料化される。", "北東欧"),
    ("ロマンシュ語児童詩の独語橋渡し", "German mediation of Romansh children's verse", "Romansh children's verse", "ロマンシュ語児童詩が独語訳でスイス多言語市場へ渡る。", "西欧"),

    # Cluster 3: oral genre and performance translation
    ("ヨルバ語オリキの英語散文化", "English prose rendering of Yoruba oriki", "oriki", "称揚詩オリキの呼名連鎖を英語散文で説明化する。", "西アフリカ"),
    ("ネパール語ドホリ歌の英語字幕訳", "English subtitling of Nepali dohori songs", "dohori songs", "掛け合い歌ドホリの即興応答を字幕尺へ圧縮する訳。", "南アジア"),
    ("モンゴル英雄叙事詩の露語抄訳", "Russian abridgement of Mongolian heroic epics", "Mongolian epics", "モンゴル英雄叙事詩を露語抄訳が研究読本化する。", "中央アジア"),
    ("アラビア語ザジャルの仏語韻律訳", "French metrical translation of Arabic zajal", "zajal", "口語詩ザジャルの韻律と掛詞を仏語で補償する試み。", "西アジア"),
    ("ガリフナ歌謡の英語民族誌訳", "English ethnographic translation of Garifuna songs", "Garifuna songs", "ガリフナ歌謡が英語訳で儀礼説明と結びつく採録形式。", "カリブ"),
    ("サーミ・ヨイクの北欧語字幕訳", "Nordic subtitling of Sami joik", "joik", "ヨイクの反復声響を北欧語字幕が意味中心に縮約する。", "北欧"),

    # Cluster 4: censorship, exile, and activist circuits
    ("ウクライナ地下詩のポーランド語リレー訳", "Polish relay translation of Ukrainian underground poetry", "underground poetry", "地下詩がポーランド語を経て西欧支援圏へ届く回路。", "東欧"),
    ("ベラルーシ抗議詩の英語SNS訳", "English social-media translation of Belarusian protest poetry", "protest poetry", "抗議詩がSNS英訳で速報的連帯テキストになる現象。", "東欧"),
    ("シリア難民詩の独語朗読訳", "German performance translation of Syrian refugee poetry", "refugee poetry", "難民詩が独語朗読訳で証言イベントに組み込まれる。", "西アジア"),
    ("香港抗議詩の英語匿名訳", "Anonymous English translation of Hong Kong protest poems", "protest poems", "抗議詩の匿名英訳が身元保護と国際拡散を両立する。", "東アジア"),
    ("アルジェリア黒い十年小説の仏語自己訳", "French self-translation of Algerian Black Decade fiction", "Black Decade fiction", "内戦期小説が仏語自己訳で検閲と市場を横断する。", "北アフリカ"),
    ("ミャンマー獄中短歌の英語支援訳", "English solidarity translation of Myanmar prison tanka", "prison tanka", "獄中短歌が英語支援訳で人権運動の証言になる。", "東南アジア"),

    # Cluster 5: paratext, metrics, and AI-era microproblems
    ("訳者謝辞の不可視労働標識", "Translator acknowledgements as labor markers", "acknowledgements", "訳者謝辞が協力者と調査労働を可視化するパラテクスト。", "理論"),
    ("対訳脚注のページ滞留効果", "Page-dwell effect of bilingual footnotes", "bilingual footnotes", "対訳脚注が読者の視線滞留と解釈速度を変える効果。", "理論"),
    ("固有名索引の翻字統制", "Transliteration control in proper-name indexes", "name indexes", "索引で翻字揺れを統制し世界文学読書を支える技法。", "理論"),
    ("LLM訳の文体温度プロファイル", "Stylistic temperature profiling of LLM translation", "LLM temperature", "生成温度差が訳文文体と比喩密度を変える分析単位。", "デジタル"),
    ("プロンプト内参照訳の模倣汚染", "Reference imitation contamination in prompts", "reference imitation", "参照訳を含むプロンプトが訳文の独立性を損なう問題。", "デジタル"),
    ("多訳比較UIの評価バイアス", "Evaluation bias in multi-translation interfaces", "multi-translation UI", "複数訳提示UIの並び順が品質判断を偏らせる現象。", "デジタル"),
]


def main():
    with LitDB(DB) as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        existing = {row["name_ja"] for row in db.conn.execute("SELECT name_ja FROM concepts")}

        if len(CONCEPTS) != 30:
            raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")

        seen = set()
        for name_ja, _, _, definition, _ in CONCEPTS:
            if name_ja in seen:
                raise SystemExit(f"duplicate in script: {name_ja}")
            seen.add(name_ja)
            if name_ja in existing:
                raise SystemExit(f"duplicate in DB: {name_ja}")
            if len(definition) > 100:
                raise SystemExit(f"definition too long: {name_ja} ({len(definition)})")

        for name_ja, name_en, name_original, definition, region in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD,
                region=region,
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )

        db.conn.commit()
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        print(f"Inserted {after - before}; total {after}")


if __name__ == "__main__":
    main()
