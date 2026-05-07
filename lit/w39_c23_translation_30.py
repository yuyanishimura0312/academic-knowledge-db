#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"
REGION = "理論"
PERIOD_ID = 58

CONCEPTS = [
    # Cluster 1: 前近代・宗教翻訳の細部
    ("ボハイラ派聖書アラビア語訳", "Bohairic-Arabic Bible Translation", "Bohairic-Arabic",
     "コプト典礼本文がアラビア語へ移る中世エジプトの聖書翻訳。"),
    ("サアディア・ガオン聖書アラビア語訳", "Saadia Gaon Arabic Bible", "Tafsir Saadia",
     "ユダヤ共同体向けにヘブライ聖書をユダヤ・アラビア語化した訳業。"),
    ("ウイグル仏典の重訳層", "Old Uyghur Buddhist Relay Translation", "Old Uyghur Buddhist",
     "漢訳・トカラ語訳を介した古ウイグル仏典の多層的重訳。"),
    ("アルバニア語メシャリ翻訳", "Albanian Meshari Translation", "Meshari",
     "ブズクの典礼書がラテン典礼を初期アルバニア語へ移した訳例。"),
    ("ワラーム聖書訳の方言混淆", "Warao Bible Dialect Mediation", "Warao Bible",
     "宣教翻訳で複数方言を折衷し標準的聖書語を作る過程。"),
    ("満洲語仏典翻訳の欽定語彙", "Manchu Buddhist Translation Lexicon", "Manchu canon",
     "清朝宮廷で仏教用語を満洲語へ制度的に定着させた語彙体系。"),

    # Cluster 2: 周縁文学のリレー経路
    ("フェロー語文学のデンマーク語仲介", "Faroese-Danish Literary Relay", "Faroese relay",
     "フェロー語作品がデンマーク語版を介し国際流通する経路。"),
    ("ソルブ語文学のドイツ語窓口", "Sorbian-German Literary Mediation", "Sorbian mediation",
     "ソルブ語作品がドイツ語紹介で可視化される少数語文学の回路。"),
    ("コミ語詩のロシア語自己翻訳", "Komi-Russian Poetic Self-Translation", "Komi self-translation",
     "コミ語詩人がロシア語版で韻律と民族語感を再設計する実践。"),
    ("ガリシア語小説のカスティーリャ語先行訳", "Galician-Castilian Pretranslation", "Galician relay",
     "ガリシア語作品がスペイン語版を先行させる国内外向け媒介。"),
    ("アディゲ文学のロシア語ピボット", "Adyghe-Russian Pivot Translation", "Adyghe pivot",
     "北コーカサス文学がロシア語を足場に他言語化される構造。"),
    ("マプチェ詩の二言語版パラテクスト", "Mapuche Bilingual Poetic Paratext", "Mapuche paratext",
     "マプドゥングン詩の対訳版で注釈が民族性を枠づける仕組み。"),

    # Cluster 3: 検閲・亡命・地下出版
    ("サミズダート翻訳の手稿流通", "Samizdat Translation Manuscript Circulation", "samizdat translation",
     "禁止文学の翻訳が手稿複写で読者共同体を作る地下流通。"),
    ("タミズダート翻訳の国外戻し", "Tamizdat Translation Reimport", "tamizdat translation",
     "国外刊行訳が原圏へ逆流し検閲下の読書を支える現象。"),
    ("チリ軍政期の偽装翻訳", "Chilean Dictatorship Pseudotranslation", "pseudotranslation",
     "検閲回避のため外国作家訳として提示された創作テクスト。"),
    ("フランコ期カタルーニャ語翻訳検閲", "Francoist Catalan Translation Censorship", "Catalan censorship",
     "カタルーニャ語翻訳出版が許可制度と自己検閲に縛られた状況。"),
    ("南ア反アパルトヘイト翻訳パンフ", "Anti-Apartheid Translation Pamphlets", "anti-apartheid pamphlets",
     "声明・詩・証言の翻訳小冊子が国際連帯を組織した実践。"),
    ("イラン地下翻訳PDF流通", "Iranian Underground Translation PDFs", "underground PDFs",
     "未許可訳がPDFで流れ検閲外の文学受容を作るデジタル回路。"),

    # Cluster 4: 翻訳者・小出版・叢書
    ("バニパル誌アラブ文学英訳回路", "Banipal Arabic-English Translation Circuit", "Banipal",
     "雑誌掲載訳がアラブ現代文学の英語圏受容を下支えする場。"),
    ("ダルキー・アーカイヴ翻訳叢書", "Dalkey Archive Translation Series", "Dalkey Archive",
     "実験文学の翻訳刊行で周縁的モダニズムを英語圏に広げた叢書。"),
    ("オープン・レター翻訳選書", "Open Letter Translation List", "Open Letter Books",
     "大学系小出版が未紹介文学を英訳で継続紹介する制度。"),
    ("セアガル翻訳選書", "Seagull Books Translation List", "Seagull Books",
     "欧亜の戯曲・思想・小説を英訳で束ねるコルカタ発の叢書。"),
    ("アーキペラゴ叢書の再翻訳戦略", "Archipelago Books Retranslation Strategy", "Archipelago",
     "古典と近現代作を新訳で再配置する米国小出版の編集方針。"),
    ("アンド・アザー・ストーリーズ共同選書", "And Other Stories Translation Selection", "And Other Stories",
     "読者サークルが翻訳候補を発掘する共同型小出版モデル。"),

    # Cluster 5: マイクロ技法・デジタル実践
    ("傍点の翻訳補償", "Bouten Emphasis Compensation", "bouten",
     "日本語傍点の強調や皮肉を斜体・反復・語順で補う訳法。"),
    ("敬称スタッキング翻訳", "Honorific Stacking Translation", "honorific stacking",
     "複数敬称が示す距離や序列を訳語と説明で再構成する技法。"),
    ("ルビ多義性の訳注化", "Ruby Polysemy Annotation", "ruby annotation",
     "ルビが作る二重意味を本文訳と注で分担させる処理。"),
    ("縦書き改行の横組み再配置", "Vertical Linebreak Reflow", "vertical reflow",
     "縦書き詩行の視覚的切れを横組み訳で再設計する問題。"),
    ("字幕折返しによる詩行変形", "Subtitle Line-Wrap Poetic Deformation", "subtitle line wrap",
     "字幕の字数制限が詩的改行や反復を変形させる翻訳現象。"),
    ("LLM訳文の温度差分比較", "LLM Translation Temperature Diffing", "temperature diffing",
     "生成温度別の訳文差分から文体揺れと創造性を測る手法。"),
]


def main():
    with LitDB(DB) as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        existing = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts")
        }

        if len(CONCEPTS) != 30:
            raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")

        for name_ja, _, _, definition in CONCEPTS:
            if name_ja in existing:
                raise SystemExit(f"duplicate in DB: {name_ja}")
            if len(definition) > 100:
                raise SystemExit(f"definition too long: {name_ja}")

        for name_ja, name_en, name_original, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=3,
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
