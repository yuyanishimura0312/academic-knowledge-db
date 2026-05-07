#!/usr/bin/env python3
"""Wave 37: 30 niche cutting-edge AI/digital literature concepts for subfield 24."""
import sqlite3
import sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 24
PERIOD_ID = 181  # デジタル・量的文学研究期 (横断)
REGION = "横断"

CONCEPTS = [
    # Cluster 1: 生成AI実作品 (6)
    ("Pharmako-AI（Allado-McDowell）", "Pharmako-AI", "Pharmako-AI", "K Allado-McDowellがGPT-3と共著した実験的書籍、機械的神秘主義の系譜を開く。"),
    ("1 the Road（Code Karadec）", "1 the Road", "1 the Road", "Ross Goodwin AI車載生成小説、ケルアック『路上』の機械版として2018年公刊。"),
    ("Death of the Marvell（GPT詩集）", "Death of the Marvell", "Death of the Marvell", "GPT系列生成詩集の代表作、17世紀詩人マーヴェルへの機械的応答実験。"),
    ("Sudowrite共著小説", "Sudowrite Co-authored Fiction", "Sudowrite", "Sudowrite利用作家による商業小説出版実例、人間-AI共著の現場実装を象徴。"),
    ("Janelle Shaneニューラル網ジョーク", "Janelle Shane Neural Net Jokes", "AI Weirdness", "Janelle Shaneがニューラル網に書かせた笑話・命名集、AI不条理文学の起点。"),
    ("Allison Parrish Articulations", "Allison Parrish Articulations", "Articulations", "Allison Parrish 2018年詩集、計算的音韻ベクトル空間からの自動生成詩。"),
    # Cluster 2: ジェネラティブ詩歌 (6)
    ("Bonjour Monde（JR Carpenter）", "Bonjour le Monde", "Bonjour le Monde", "JR Carpenterのフライトデータ駆動生成詩、気候批評と航空文学の交差。"),
    ("Code Poetry Rilke RNN", "Code Poetry Rilke RNN", "Rilke RNN", "Rilkeコーパス学習RNN詩生成プロジェクト、ニューラル抒情詩の初期実装例。"),
    ("RNN俳句ジェネレータ", "RNN Haiku Generator", "RNN Haiku", "RNNによる五七五学習・季語反映の俳句自動生成、定型詩計算化の代表。"),
    ("Nick Montfort Taroko Gorge", "Taroko Gorge", "Taroko Gorge", "Nick Montfort 2009年JavaScript生成詩、太魯閣峡谷描写の無限再生詩。"),
    ("McKenzie Wark生成理論テクスト", "McKenzie Wark Generative Theory", "Wark Generative", "McKenzie Warkの理論テクスト生成実験、批評的書記の機械化を試みる。"),
    ("Ryan Murphy生成詩", "Ryan Murphy Generative Poems", "Murphy Generative", "Ryan Murphy LLM活用詩集、プロンプト即興と編集再構成の往還詩学。"),
    # Cluster 3: ハイパーテクスト・電子文学細部 (6)
    ("Michael Joyce『Afternoon, a story』", "Afternoon, a story", "Afternoon, a story", "1987年Storyspace発表、ハイパーテクスト文学の正典・原型作品。"),
    ("Stuart Moulthrop『Victory Garden』", "Victory Garden", "Victory Garden", "1991年湾岸戦争を背景にしたハイパーテクスト小説、政治的網状叙述の代表。"),
    ("Shelley Jackson『Patchwork Girl』", "Patchwork Girl", "Patchwork Girl", "1995年Storyspaceフェミニズムハイパーテクスト、フランケンシュタイン女性版。"),
    ("Mark Bernstein Storyspace開発", "Mark Bernstein Storyspace", "Storyspace", "Mark Bernsteinが開発・販売したハイパーテクスト編集ソフト、電子文学基盤。"),
    ("Twineインタラクティブフィクション", "Twine Interactive Fiction", "Twine IF", "Twine利用の独立系インタラクティブ小説運動、ゲーム文学の民主化。"),
    ("Inkle Studiosナラティブデザイン", "Inkle Studios Narrative Design", "Inkle", "Inkle StudiosのInk言語と『80 Days』等、商業的物語型ゲーム文学の旗手。"),
    # Cluster 4: AIコラボ作家論争 (6)
    ("九段理江芥川賞AI共著発言", "Rie Kudan Akutagawa AI Prize", "九段理江AI", "九段理江2024年芥川賞受賞作にChatGPT利用を公表、AI共著の論争を引き起こす。"),
    ("Stephen Marche Death of Authorship 2.0", "Death of Authorship 2.0", "Marche 2.0", "Stephen Marche評論、AI時代におけるバルト「作者の死」再演を論じる。"),
    ("K Allado-McDowell共著者性論", "K Allado-McDowell Co-authorship", "Allado-McDowell", "K Allado-McDowellによる人間-AI共著者性の理論化、機械神秘主義として展開。"),
    ("AIゴーストライティング倫理", "AI Ghostwriting Ethics", "AI Ghostwriting Ethics", "AI代筆の開示義務・著作者表示・契約倫理に関する出版業界の論争領域。"),
    ("AIテクスト剽窃検出", "Plagiarism Detection AI Texts", "AI Plagiarism Detection", "GPTZero/Turnitin等AI生成検出技術と教育出版界の対応、検出限界も議論。"),
    ("AI支援詩批評論争", "AI-assisted Poetry Critique", "AI Poetry Critique", "LLMによる詩作批評・添削の是非論争、創作教育におけるAI役割を巡る議論。"),
    # Cluster 5: 計算文芸理論 (6)
    ("Andrew Piper Enumerations", "Andrew Piper Enumerations", "Enumerations", "Andrew Piper 2018年著作、計算的文学研究方法論を統合した代表的理論書。"),
    ("Ted Underwood Distant Horizons", "Distant Horizons", "Distant Horizons", "Ted Underwood 2019年著作、機械学習による200年文学史の遠読的分析。"),
    ("Stanford Literary Lab Pamphlet", "Stanford Literary Lab Pamphlet", "Stanford LitLab", "Moretti主導Stanford Literary Labのパンフレット連作、計算文学批評の系譜。"),
    ("Roopika Risam New Digital Worlds", "Roopika Risam New Digital Worlds", "New Digital Worlds", "Roopika Risam 2018年著作、ポストコロニアル・デジタル人文学を体系化。"),
    ("Lauren Klein Data Feminism文学応用", "Data Feminism Literary", "Data Feminism", "Lauren Klein/D'Ignazio『Data Feminism』の文学研究応用、批判的計算文学。"),
    ("Tara McPherson Reconstructing Textualities", "Tara McPherson Reconstructing", "Reconstructing", "Tara McPhersonの計算的テクスト性再構築論、人文学計算化の批判的枠組み。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_original, definition in CONCEPTS:
        if len(definition) > 100:
            print(f"WARN definition too long ({len(definition)}): {name_ja}", file=sys.stderr)
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, 3)
            """, (name_ja, name_en, name_original, SUBFIELD_ID, REGION, PERIOD_ID, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"Total in subfield {SUBFIELD_ID}: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
