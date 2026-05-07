#!/usr/bin/env python3
"""Wave 31 C38: Add 30 concepts to lit_world_translation (subfield_id=23).
5 thematic clusters x 6 concepts each.
"""
import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lit.sqlite")

SUBFIELD_ID = 23
PERIOD_ID = 273  # 世界文学・遠読期 (横断)
REGION = "横断"

# 5 clusters x 6 concepts = 30
CONCEPTS = [
    # Cluster 1: 翻訳論深化
    ("ベルマン『他者の試練』詳説", "L'épreuve de l'étranger", "L'épreuve de l'étranger", "latin",
     "ベルマンが翻訳を他者性の経験と捉え、自言語に異物を呼び込む倫理を提示した1984年論考。"),
    ("メショニック『翻訳の詩学』", "Poétique du traduire", "Poétique du traduire", "latin",
     "メショニックが翻訳を意味伝達でなくリズム再生と定義し、詩学的翻訳論を体系化した1999年著作。"),
    ("スタイナー『バベル以後』詳説", "After Babel", "After Babel", "latin",
     "スタイナーが解釈学的四段階モデル（信頼・侵入・受容・補償）で翻訳を理論化した1975年大著。"),
    ("エーコ『鼠か蝿か』", "Mouse or Rat?", "Mouse or Rat?", "latin",
     "エーコが翻訳を「ほぼ同じこと」を言う交渉と捉え、文化的等価性を実例で論じた2003年著。"),
    ("オクタビオ・パス翻訳論", "Traducción: literatura y literalidad", "Traducción", "latin",
     "パスが翻訳と創作の連続性を主張し、字義性と文学性の弁証法を論じた1971年エッセイ。"),
    ("カサン『翻訳不可能なもの辞典』", "Dictionary of Untranslatables", "Vocabulaire européen des philosophies", "latin",
     "カサン編の哲学概念翻訳不可能性辞典。各言語固有の概念を比較分析した2004年プロジェクト。"),

    # Cluster 2: 機械翻訳
    ("Vaswani『Attention is All You Need』", "Attention Is All You Need", "Attention Is All You Need", "latin",
     "Transformerアーキテクチャを提唱しNMTを刷新したVaswaniら2017年論文。現代翻訳AIの基礎。"),
    ("Bahdanau注意機構2014", "Neural Machine Translation by Jointly Learning to Align and Translate", "Bahdanau attention", "latin",
     "Bahdanauらが導入した注意機構によりエンコーダ・デコーダ翻訳の長文対応を解決した2014年論文。"),
    ("BLEU評価指標", "BLEU: a Method for Automatic Evaluation of Machine Translation", "BLEU", "latin",
     "Papineniら2002年提唱の機械翻訳自動評価指標。n-gram一致率で翻訳品質を定量化する標準。"),
    ("COMET評価指標", "COMET: A Neural Framework for MT Evaluation", "COMET", "latin",
     "Reiら2020年のニューラル翻訳評価指標。多言語事前学習モデルを用い人間評価と高相関を示す。"),
    ("MQM評価フレームワーク", "Multidimensional Quality Metrics", "MQM", "latin",
     "Lommel主導の翻訳品質多次元評価フレーム。エラー類型を体系化し業界標準的に普及した。"),
    ("NLLB-200多言語翻訳", "No Language Left Behind", "NLLB-200", "latin",
     "Meta AIが2022年に発表した200言語対応大規模NMTモデル。低資源言語の包摂を目的とする。"),

    # Cluster 3: 翻訳実践
    ("グロスマン『なぜ翻訳が重要か』詳説", "Why Translation Matters", "Why Translation Matters", "latin",
     "グロスマンがガルシア=マルケス英訳経験から翻訳の文学的・倫理的意義を論じた2010年エッセイ。"),
    ("ティム・パークス『翻訳のスタイル』", "Translating Style", "Translating Style", "latin",
     "パークスが英伊翻訳実践から文体翻訳の困難と方法論を論じた1997/2007年実践批評書。"),
    ("ベルノフスキー『外国語』エッセイ", "Foreign Words", "Foreign Words", "latin",
     "ベルノフスキーがヴァルザー独訳経験から翻訳における異質性保持を論じた実践エッセイ。"),
    ("ジェニファー・クロフト『階級』", "Class", "Class", "latin",
     "ポーランド語翻訳家クロフトが翻訳者の労働・階級・可視性を論じたエッセイ・小説作品。"),
    ("アントン・ホー韓国文学翻訳", "Anton Hur Korean translator", "Anton Hur", "latin",
     "韓国文学英訳者ホーが国際ブッカー候補ボラ・チョン等を訳出、現代韓国文学世界化を担う。"),
    ("ドン・ミー・チョイ『DMZコロニー』", "DMZ Colony", "DMZ Colony", "latin",
     "韓国系米国詩人チョイが翻訳・移民・植民地性を交差させた2020年全米図書賞詩集。"),

    # Cluster 4: 比較・世界文学
    ("ダムロッシュ『世界文学の読み方』", "How to Read World Literature", "How to Read World Literature", "latin",
     "ダムロッシュが世界文学を読む実践的方法論を提示した2009年入門書。流通と受容を重視。"),
    ("アプター『翻訳不可能性』", "Against World Literature: On the Politics of Untranslatability", "Against World Literature", "latin",
     "アプターが世界文学概念を翻訳不可能性の観点から批判した2013年著作。カサンを応用展開。"),
    ("ウォルコウィッツ『翻訳のために生まれた』", "Born Translated", "Born Translated", "latin",
     "ウォルコウィッツが翻訳前提で書かれる現代小説（born-translated）を理論化した2015年著。"),
    ("カサノヴァ『文学のグリニッジ子午線』", "The World Republic of Letters", "La République mondiale des Lettres", "latin",
     "カサノヴァが文学世界の中心-周縁構造とパリの象徴的子午線を論じた1999年世界文学社会学。"),
    ("ムフティ『英語を忘れよ』", "Forget English!", "Forget English!", "latin",
     "ムフティが英語による世界文学覇権を批判しオリエンタリズム再考を促した2016年著。"),
    ("チア『世界文学とは何か』", "What Is a World?", "What Is a World?", "latin",
     "チアが世界文学を世界化（worlding）の現象学として再定義した2016年ポストコロニアル理論書。"),

    # Cluster 5: 翻訳と権力
    ("ニランジャーナ『場の取り戻し』詳説", "Siting Translation", "Siting Translation", "latin",
     "ニランジャーナが英印翻訳における植民地権力を批判的に分析した1992年ポストコロニアル名著。"),
    ("酒井直樹『翻訳と主体』", "Translation and Subjectivity", "Translation and Subjectivity", "latin",
     "酒井が翻訳を国民主体形成の装置と捉え、均質的言語共同体を批判した1997年理論書。"),
    ("ティモシュコ『翻訳学の拡張』", "Enlarging Translation, Empowering Translators", "Enlarging Translation", "latin",
     "ティモシュコが西欧中心翻訳学を脱構築し非西欧伝統を含む拡張学を提唱した2007年著。"),
    ("アサド『文化翻訳の概念』", "The Concept of Cultural Translation", "Cultural Translation", "latin",
     "アサドが英国社会人類学の文化翻訳概念を権力・非対称性の観点から批判した1986年論考。"),
    ("スピヴァク『翻訳の政治学』", "The Politics of Translation", "The Politics of Translation", "latin",
     "スピヴァクが第三世界女性テクスト翻訳の政治性・倫理を論じた1993年フェミニスト翻訳論。"),
    ("ラファエル『植民地の契約』", "Contracting Colonialism", "Contracting Colonialism", "latin",
     "ラファエルがスペイン植民地下タガログ語翻訳の権力構造を分析した1988年歴史人類学書。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Existing names check
    cur.execute("SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    existing = {row[0] for row in cur.fetchall()}

    inserted = 0
    skipped = 0
    for name_ja, name_en, name_original, original_script, definition in CONCEPTS:
        if name_ja in existing:
            skipped += 1
            continue
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_original, original_script,
                  SUBFIELD_ID, REGION, PERIOD_ID, definition, 4))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP (integrity): {name_ja} - {e}")
            skipped += 1

    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

    # Final counts
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    print(f"Total in subfield {SUBFIELD_ID}: {total}")
    conn.close()


if __name__ == "__main__":
    main()
