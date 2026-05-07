#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"

CONCEPTS = [
    # Cluster 1: overlooked sacred/manuscript translation chains
    ("ゲエズ聖人伝アラビア語重訳", "Arabic Relay of Ge'ez Hagiography", "Ge'ez hagiography", "エチオピア聖人伝がアラビア語経由で再流通する重訳層。", "エチオピア"),
    ("スラヴ語外典のルーマニア語写本訳", "Romanian Manuscript Translations of Slavonic Apocrypha", "Slavonic apocrypha", "教会スラヴ語外典がルーマニア語写本で俗語化する系譜。", "東欧"),
    ("シリア語アレクサンドロス伝の東方訳", "Eastern Translations of the Syriac Alexander Romance", "Syriac Alexander Romance", "シリア語物語がアルメニア語・ペルシア語へ枝分かれする翻訳圏。", "西アジア"),
    ("カロシュティー断片仏典のガンダーラ訳語", "Gandhari Buddhist Translation Lexicon", "Gandhari fragments", "ガンダーラ写本断片に残る仏教語彙の初期翻訳実験。", "中央アジア"),
    ("古ヌビア語聖書断片訳", "Old Nubian Biblical Fragment Translation", "Old Nubian Bible", "ナイル中流の断片写本に残るギリシア語聖書の地域語訳。", "アフリカ"),
    ("マラヤーラム古聖歌のシリア語翻案", "Malayalam-Syriac Hymn Adaptation", "Syriac-Malayalam hymns", "トマス派典礼歌がシリア語句法を地域詩形へ移す翻案。", "南アジア"),

    # Cluster 2: minor-language relay and self-translation circuits
    ("ブルトン語詩のフランス語自己抄訳", "Breton-French Poetic Self-Abridgement", "Breton poetry", "ブルトン語詩人が仏訳で民謡性を圧縮する自己翻訳慣行。", "西欧"),
    ("フリジア語児童文学のオランダ語窓口", "Frisian-Dutch Children's Literature Relay", "Frisian children's books", "フリジア語児童書が蘭訳を足場に国外紹介される回路。", "西欧"),
    ("カシューブ語小説のポーランド語橋渡し", "Kashubian-Polish Novel Mediation", "Kashubian prose", "カシューブ語散文がポーランド語版で少数語文学として読まれる経路。", "東欧"),
    ("メグレル語民話のグルジア語編訳", "Mingrelian-Georgian Folktale Adaptation", "Mingrelian tales", "メグレル語口承がグルジア語編集で国家文学内に置かれる実践。", "コーカサス"),
    ("ラディン語詩のイタリア語対訳出版", "Ladin-Italian Bilingual Poetry Editions", "Ladin poetry", "ラディン語詩が伊語対訳で山岳少数語の可視性を得る形式。", "西欧"),
    ("カレリア語叙事詩のフィンランド語再編", "Karelian-Finnish Epic Recomposition", "Karelian epic", "カレリア語歌謡素材がフィンランド語叙事詩へ再構成される翻訳問題。", "北欧"),

    # Cluster 3: forgotten works and local genres in translation
    ("アムハラ語タリク小説の伊語植民地訳", "Italian Colonial Translations of Amharic Tarik Fiction", "tarik fiction", "アムハラ語歴史物語が植民地期イタリア語で再枠づけられた例。", "アフリカ"),
    ("オック語フェリブリージュ詩の仏語注釈訳", "Occitan Felibrige Annotated French Translation", "Felibrige poetry", "オック語復興詩が仏語注釈で地方色を説明化する翻訳形式。", "西欧"),
    ("タガログ語コリードのスペイン語逆訳", "Spanish Back-Translations of Tagalog Corrido", "Tagalog corrido", "タガログ韻文物語が植民地語へ戻されるジャンル横断訳。", "東南アジア"),
    ("マラーティー語パワーダー英訳", "English Translation of Marathi Powada", "powada", "武勇歌パワーダーの反復・掛け声を英訳で処理する課題。", "南アジア"),
    ("ジャワ語ババッド蘭訳抄本", "Dutch Abridgements of Javanese Babad", "babad", "ジャワ年代記が蘭訳抄本で史料化される翻訳編集。", "東南アジア"),
    ("ケチュア語ワイノ歌詞の西語散文化", "Spanish Prose Rendering of Quechua Huayno Lyrics", "huayno lyrics", "ワイノ歌詞の反復と音韻性を西語散文が削る翻訳現象。", "アンデス"),

    # Cluster 4: censorship, exile, and para-translation
    ("ポルトガル新国家期の検閲済み翻訳小説", "Estado Novo Censored Translated Fiction", "Estado Novo translations", "独裁期ポルトガルで訳小説が削除・改題された検閲事例群。", "西欧"),
    ("ギリシア軍政期の暗号化翻訳序文", "Greek Junta Coded Translation Prefaces", "coded prefaces", "翻訳書序文が検閲下で政治的合図を忍ばせるパラテクスト。", "南欧"),
    ("ビルマ亡命詩の英語ニュースレター訳", "Burmese Exile Poetry Newsletter Translation", "exile newsletters", "亡命者ニュースレターがビルマ語詩を英訳で運動化する回路。", "東南アジア"),
    ("ポーランド地下SF翻訳同人誌", "Polish Underground SF Translation Fanzines", "SF fanzines", "社会主義期同人誌が英米SF訳を非公式に流通させた場。", "東欧"),
    ("チュニジア仏語検閲下アラビア語自己訳", "Tunisian Arabic Self-Translation under Francophone Censorship", "Tunisian self-translation", "仏語発表後にアラビア語自己訳で政治的含意をずらす実践。", "北アフリカ"),
    ("朝鮮戦争捕虜詩の通訳筆記", "Interpreter Transcription of Korean War POW Poetry", "POW poetry", "捕虜詩が通訳筆記を介し証言資料化する翻訳過程。", "東アジア"),

    # Cluster 5: micro-debates in technique and evaluation
    ("双数代名詞の翻訳損失", "Dual Pronoun Translation Loss", "dual pronoun loss", "双数を持つ言語の親密性や数感が訳文で消える問題。", "理論"),
    ("語根反復の語族外翻訳", "Root-Repetition Translation across Language Families", "root repetition", "セム語などの語根反復を非語根型言語へ移す補償論点。", "理論"),
    ("押韻脚注の可読性論争", "Readability Debate on Rhyme Footnotes", "rhyme footnotes", "韻の説明脚注が詩的読解を助けるか妨げるかの小論争。", "理論"),
    ("対訳ページの視線誘導効果", "Eye-Tracking Effects of Facing-Page Translation", "facing-page translation", "対訳配置が原文参照と訳文没入の比率を変える現象。", "理論"),
    ("訛り表記の社会階層翻訳", "Class Translation of Dialect Orthography", "dialect orthography", "方言綴りを階層・地域・人種標識としてどう移すかの問題。", "理論"),
    ("LLM訳の幻の典拠生成", "Phantom Source Generation in LLM Translation", "phantom sources", "LLMが訳注や出典らしき根拠を生成してしまう評価課題。", "デジタル"),
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
                canonical_in_region="minor",
            )

        db.conn.commit()
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        print(f"Inserted {after - before}; total {after}")


if __name__ == "__main__":
    main()
