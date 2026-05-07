#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_world_translation"
REGION = "理論"
PERIOD_ID = 58

CONCEPTS = [
    # Cluster 1: 翻訳史ミクロ制度
    ("アルメニア聖書翻訳黄金期", "Armenian Bible Translation Golden Age", "Ոսկեդար",
     "メスロプ文字創成後の聖書翻訳が文語規範を固めた5世紀運動。"),
    ("シリア語ペシッタ翻訳圏", "Syriac Peshitta Translation Zone", "Peshitta",
     "シリア語聖書訳が東方キリスト教の注釈と再翻訳を媒介した圏域。"),
    ("アルフォンソ10世翻訳工房", "Alfonso X Translation Workshop", "Alfonsine workshop",
     "王権主導でアラビア語知をカスティーリャ語化した多言語翻訳工房。"),
    ("近世イエズス会適応翻訳", "Jesuit Accommodation Translation", "accommodatio",
     "布教語彙を現地概念へ寄せるイエズス会の適応的翻訳実践。"),
    ("ドラーグマン外交翻訳", "Dragoman Diplomatic Translation", "dragoman",
     "オスマン外交で通訳官が条約・書簡の意味を交渉した制度。"),
    ("ロシア聖務会翻訳検閲", "Russian Synod Translation Censorship", "Synod censorship",
     "聖務会が宗教書翻訳の語彙と流通を統制した帝政期の検閲制度。"),

    # Cluster 2: 周縁言語の媒介連鎖
    ("イディッシュ文学の英語仲介", "Yiddish Literature via English", "Yiddish relay",
     "イディッシュ作品が英訳を経て世界文学市場へ入る媒介構造。"),
    ("ハイチ・クレオール自己翻訳", "Haitian Creole Self-Translation", "Kreyol self-translation",
     "仏語とクレオール語の間で作者が階層差を操作する自己翻訳実践。"),
    ("バスク語文学のスペイン語リレー", "Basque-Spanish Relay Translation", "Basque relay",
     "バスク語作品がスペイン語版を足場に国際翻訳される流通経路。"),
    ("サーミ文学の北欧語仲介", "Sami Literature Nordic Mediation", "Sami mediation",
     "サーミ語作品がノルウェー語等を介して世界市場へ届く翻訳回路。"),
    ("グアラニー語二重書記翻訳", "Guarani Bilingual Script Translation", "Guarani bilingualism",
     "口承・スペイン語・グアラニー語表記が交差する二重翻訳実践。"),
    ("チベット仏典逆翻訳", "Tibetan Buddhist Back-Translation", "back-translation",
     "失われた梵本をチベット訳から復元する仏典文献学の翻訳手法。"),

    # Cluster 3: 詩学・形式の翻訳問題
    ("押韻補償翻訳", "Rhyme Compensation Translation", "rhyme compensation",
     "失われた脚韻効果を別箇所の音型や反復で補う詩翻訳技法。"),
    ("異質韻律の移植", "Transplanting Foreign Prosody", "prosodic transfer",
     "原詩の拍・脚・行分けを受容語の韻律へずらして移す方法。"),
    ("句読点翻訳の詩学", "Poetics of Punctuation Translation", "punctuation translation",
     "句読点や改行の変更が声・間・解釈を作る翻訳上の微細操作。"),
    ("多声性の標識翻訳", "Translating Polyphonic Markers", "polyphonic markers",
     "方言・引用符・語調で多声性を読ませる標識を訳す問題系。"),
    ("オノマトペ密度の翻訳", "Onomatopoeic Density Translation", "onomatopoeic density",
     "擬音語の頻度差を意味・音感・幼児性の配分として処理する技法。"),
    ("人称代名詞ゼロ翻訳", "Zero Pronoun Translation", "zero pronoun translation",
     "主語省略言語から人称必須言語へ訳す際の視点固定化問題。"),

    # Cluster 4: 産業・パラテクスト
    ("翻訳者あとがきの権威化", "Translator Afterword Authority", "translator afterword",
     "訳者あとがきが作品解釈と翻訳者の専門性を制度化する現象。"),
    ("翻訳版カバーデザイン介入", "Translated Cover Design Intervention", "translated cover design",
     "受容国の表紙がジャンル・国籍・読者像を再符号化する過程。"),
    ("サンプル翻訳ゲートキーピング", "Sample Translation Gatekeeping", "sample translation",
     "助成・版権売買で抜粋訳が翻訳可否を決める選別装置となる。"),
    ("翻訳権エージェント回路", "Translation Rights Agent Circuit", "rights agents",
     "版権エージェントが言語間流通と文学的価値付けを調整する回路。"),
    ("文学翻訳助成制度", "Literary Translation Subsidy", "translation subsidy",
     "国家・財団助成が周縁言語作品の翻訳採算を補正する制度。"),
    ("翻訳賞の市場効果", "Market Effect of Translation Prizes", "translation prize effect",
     "翻訳賞が訳者名・出版社・原作者の可視性と売上を押し上げる効果。"),

    # Cluster 5: デジタル・評価ニッチ
    ("低資源文学翻訳NMT", "Low-Resource Literary NMT", "low-resource NMT",
     "訓練データ不足言語の文学翻訳でNMTが比喩と文体を崩す問題。"),
    ("合成対訳コーパス翻訳", "Synthetic Parallel Corpus Translation", "synthetic parallel corpus",
     "逆翻訳で作った対訳データを文学翻訳モデル訓練に使う手法。"),
    ("固有名照応のMT誤り", "Named-Entity Coreference MT Error", "NE coreference error",
     "人物名・敬称・代名詞連鎖を機械翻訳が崩す文学読解上の誤り。"),
    ("文体距離メトリクス", "Stylistic Distance Metrics", "style distance metrics",
     "原文と訳文の文体差を頻度・構文・埋め込みで測る評価指標群。"),
    ("訳文アライメント可視化", "Translation Alignment Visualization", "alignment visualization",
     "原文訳文の対応箇所を可視化し省略・増補・移動を分析する方法。"),
    ("文学MT評価の参照依存性", "Reference Dependence in Literary MT", "reference dependence",
     "単一参照訳への近さが創造的良訳を低く評価する指標上の偏り。"),
]


def main():
    with LitDB(DB) as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        existing = {
            r["name_ja"]
            for r in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id=23"
            )
        }
        for name_ja, _, _, definition in CONCEPTS:
            if name_ja in existing:
                raise SystemExit(f"duplicate in subfield: {name_ja}")
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

        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=23"
        ).fetchone()[0]
        print(f"Inserted {after - before}; total {after}")


if __name__ == "__main__":
    main()
