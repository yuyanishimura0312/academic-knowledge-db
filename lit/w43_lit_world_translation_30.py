#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"

CONCEPTS = [
    # Cluster 1: manuscript relay and sacred-literary drift
    ("エチオピア王書のアムハラ語抄訳", "Amharic epitome of Ethiopian royal books", "Kebra-style royal books", "ゲエズ系王書をアムハラ語抄訳が宮廷読本化する過程。", "東アフリカ"),
    ("シリア語バルラーム物語のアラビア語重訳", "Arabic relay of Syriac Barlaam tales", "Barlaam tales", "シリア語物語がアラビア語重訳で東方説話圏を渡る層。", "西アジア"),
    ("ラダック語仏伝のチベット語逆訳", "Tibetan back-translation of Ladakhi Buddha lives", "Buddha lives", "ラダック語仏伝がチベット語へ戻る地域的逆翻訳。", "ヒマラヤ"),
    ("マンダ語祈祷文のアラビア語傍訳", "Arabic marginal translation of Mandaic prayers", "Mandaic prayers", "マンダ語祈祷文にアラビア語傍訳が併走する写本慣行。", "メソポタミア"),
    ("グラゴル文字説教のラテン語抄訳", "Latin epitome of Glagolitic sermons", "Glagolitic sermons", "グラゴル文字説教をラテン語抄訳が教会管理へ接続する。", "バルカン"),
    ("ソグド語商人書簡の漢語読解訳", "Chinese reading translation of Sogdian merchant letters", "Sogdian letters", "商人書簡が漢語読解訳で交易文学資料に変わる形式。", "中央アジア"),

    # Cluster 2: small-language gateway editions
    ("ウェールズ語エングリンの英語韻律訳", "English metrical translation of Welsh englyn", "englyn", "定型詩エングリンを英語韻律で再構成する翻訳実験。", "西欧"),
    ("スコットランド・ゲール語哀歌の英語対訳", "Facing English translation of Gaelic laments", "Gaelic laments", "ゲール語哀歌が英語対訳で民俗叢書へ入る編集形態。", "西欧"),
    ("イングリア語民謡のフィンランド語採録訳", "Finnish collection translation of Ingrian songs", "Ingrian songs", "イングリア語民謡がフィンランド語採録訳で保存される回路。", "北欧"),
    ("モクシャ語詩のロシア語アンソロジー訳", "Russian anthology translation of Moksha poetry", "Moksha poetry", "モクシャ語詩が露語アンソロジーで少数文学化される。", "ヴォルガ"),
    ("ウドムルト語童話のロシア語教育訳", "Russian pedagogic translation of Udmurt tales", "Udmurt tales", "ウドムルト語童話が露語教育訳で学校読本へ移る。", "ヴォルガ"),
    ("フェロー語バラッドのデンマーク語児童訳", "Danish children's translation of Faroese ballads", "Faroese ballads", "フェロー語バラッドをデンマーク語児童版が再物語化する。", "北欧"),

    # Cluster 3: performance and sound-bound genres
    ("トゥバ喉歌詞のロシア語字幕訳", "Russian subtitling of Tuvan throat-song lyrics", "Tuvan songs", "喉歌詞の反復音声をロシア語字幕が意味単位へ圧縮する。", "中央アジア"),
    ("マオリ・カランガの英語儀礼訳", "English ritual translation of Maori karanga", "karanga", "呼びかけ儀礼カランガを英語が説明的に再配置する訳。", "オセアニア"),
    ("ベルベル語アヘリル歌謡の仏語採録訳", "French transcription-translation of Berber ahellil", "ahellil", "アヘリル歌謡が仏語採録訳で儀礼詩として読まれる。", "北アフリカ"),
    ("タミル語ヴィルパットゥの英語舞台訳", "English stage translation of Tamil villu pattu", "villu pattu", "弓歌語りの掛け合いを英語舞台台本へ移す翻訳。", "南アジア"),
    ("セルビア叙事歌グスレの英語散文訳", "English prose translation of Serbian gusle epics", "gusle epics", "グスレ伴奏叙事歌が英語散文で物語資料化される。", "バルカン"),
    ("アイヌ叙事詩ユーカラの日本語改作訳", "Japanese adaptive translation of Ainu yukar", "yukar", "ユーカラの口承反復を日本語改作が物語化する過程。", "東アジア"),

    # Cluster 4: censorship, exile, and covert paratexts
    ("ソ連期ユダヤ地下詩のヘブライ語リレー訳", "Hebrew relay of Soviet Jewish underground poetry", "underground poetry", "地下詩がヘブライ語リレーで亡命出版へ渡る経路。", "東欧"),
    ("チェコ正常化期サミズダート翻訳序文", "Samizdat translation prefaces under Czech Normalization", "samizdat prefaces", "翻訳序文が検閲下で読解共同体の合図になる形式。", "中欧"),
    ("東独検閲下SF翻訳の偽装奥付", "Disguised colophons in East German SF translation", "SF colophons", "SF翻訳の奥付偽装が原典と検閲痕跡を隠す手法。", "中欧"),
    ("ピノチェト期詩集の仏語亡命訳", "French exile translation of Pinochet-era poetry", "exile poetry", "軍政期詩集が仏語亡命訳で国際抗議圏へ流れる。", "ラテンアメリカ"),
    ("アパルトヘイト獄中詩の蘭語支援訳", "Dutch solidarity translation of apartheid prison poetry", "prison poetry", "獄中詩が蘭語支援訳で反アパルトヘイト運動に入る。", "南部アフリカ"),
    ("クメール・ルージュ証言文学の仏語抄訳", "French abridged translation of Khmer Rouge testimony", "testimony literature", "証言文学の仏語抄訳が裁判資料と読書市場を結ぶ。", "東南アジア"),

    # Cluster 5: microfeatures, platforms, and AI evaluation
    ("訳者略歴のジェンダー化フレーミング", "Gendered framing in translator bios", "translator bios", "訳者略歴の語彙が権威や感情労働を性別化する現象。", "理論"),
    ("対訳版ノンブルずれの引用問題", "Citation problems from bilingual pagination drift", "pagination drift", "対訳版の頁ずれが研究引用と授業読解を乱す問題。", "理論"),
    ("逐語グロスの詩的誤読誘発", "Poetic misreading caused by interlinear glosses", "interlinear glosses", "逐語グロスが詩の語順を過剰に原文化して読ませる効果。", "理論"),
    ("LLM訳の固有名正規化過剰", "Over-normalization of proper names in LLM translation", "name normalization", "LLM訳が異綴り固有名を過度に標準化する誤り。", "デジタル"),
    ("多言語OCR後翻訳の行分割汚染", "Line-break contamination after multilingual OCR translation", "OCR line breaks", "OCR由来の行分割が後続翻訳の詩行と文体を歪める。", "デジタル"),
    ("訳文ランキングUIの中央配置効果", "Center-position effect in translation ranking interfaces", "ranking UI", "訳文比較UIの中央配置が品質順位判断を偏らせる効果。", "デジタル"),
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
