#!/usr/bin/env python3
"""Wave 38: subfield 22 (lit_theory) +30 deep niche concepts.
5 thematic clusters x 6 concepts."""
import sqlite3, sys, os

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# Period IDs
P_THEORY_CLASSICAL = 169   # 古典・前近代翻訳伝統期 (理論)
P_ROMANTIC = 253           # ロマン主義・近代翻訳論期 (理論)
P_WORLD_LIT = 58           # 世界文学・ポストコロニアル翻訳期 (理論)
P_WORLD_LIT2 = 273         # 世界文学・遠読期 (横断)
P_AFFECT = 180             # 情動・認知・ポスト批評期 (横断)
P_AFFECT2 = 276            # 情動批評深化期 (横断)
P_BOOK_HIST = 179          # 書物史・受容史期 (横断)
P_NARRATOLOGY = 178        # 古典・古典後ナラトロジー期 (横断)

CONCEPTS = [
    # ===== Cluster 1: 古典理論伝統再読 =====
    ("アリストテレス『詩学』カタルシス再読", "Aristotle Poetics Catharsis Revisited", "Περὶ ποιητικῆς", "greek",
     "西欧", P_THEORY_CLASSICAL,
     "現代解釈学が読み直す悲劇の浄化作用、認知・情動両面の機能再評価。"),
    ("ロンギノス『崇高論』現代受容", "Longinus On the Sublime Contemporary Reception", "Περὶ ὕψους", "greek",
     "西欧", P_THEORY_CLASSICAL,
     "古代修辞学の崇高概念がカント・ハイデガー以降の美学批評で再活性化される系譜。"),
    ("ホラティウス『詩論』delight and instruct", "Horace Ars Poetica utile dulci", "Ars Poetica", "latin",
     "西欧", P_THEORY_CLASSICAL,
     "効用と快楽の二重目的論が近世詩学・教訓文学・大衆文化研究で再検討される枠組み。"),
    ("ボワロー『詩法』新古典主義規範", "Boileau Art Poétique Neoclassical Norm", "L'Art poétique", "french",
     "西欧", P_THEORY_CLASSICAL,
     "17世紀仏新古典主義規範の現代再評価、規則と自由の弁証法を再考する。"),
    ("シドニー『詩の擁護』詳細精読", "Sidney Defence of Poesy Close Reading", "An Apology for Poetry", "english",
     "西欧", P_THEORY_CLASSICAL,
     "プラトン詩人追放論への16世紀英国側応答、想像力擁護の修辞構造を精読する。"),
    ("シュレーゲル断章『アテネーウム』", "Schlegel Athenaeum Fragments", "Athenäums-Fragmente", "german",
     "西欧", P_ROMANTIC,
     "初期ロマン派の断章形式が現代理論の非全体性・反システム志向に与えた影響。"),

    # ===== Cluster 2: 翻訳・世界文学理論 =====
    ("ダムロッシュ『今日の比較文学』", "Damrosch Comparative Literature Today", "Comparative Literature in an Age of Globalization", "english",
     "横断", P_WORLD_LIT,
     "21世紀比較文学の方法論再定義、楕円的読解と流通モデルを統合した世界文学論。"),
    ("カサノヴァ『世界文学共和国』", "Casanova World Republic of Letters", "La République mondiale des Lettres", "french",
     "西欧", P_WORLD_LIT,
     "ブルデュー社会学を世界文学に適用、文学資本の中心-周縁構造を分析した枠組み。"),
    ("アプター『翻訳ゾーン』", "Apter Translation Zone", "The Translation Zone", "english",
     "横断", P_WORLD_LIT,
     "翻訳不可能性を世界文学批評の核心に据え、言語間の摩擦を理論化した政治的翻訳論。"),
    ("ステーリングス translatio論", "Stallings translatio Theory", "translatio studii", "latin",
     "横断", P_WORLD_LIT,
     "中世のtranslatio studii概念を現代世界文学・知識移転論として再定義する試み。"),
    ("酒井直樹『翻訳と主体』", "Naoki Sakai Translation and Subjectivity", "翻訳と主体", "kanji",
     "東アジア", P_WORLD_LIT,
     "翻訳行為が国民言語と主体を構築する過程を批判、同質的言語共同体の幻想を解体する。"),
    ("リディア・リウ translingual practice", "Lydia Liu Translingual Practice", "Translingual Practice", "english",
     "東アジア", P_WORLD_LIT,
     "近代中国における新語生成と西洋概念翻訳の権力関係を分析する翻訳実践論。"),

    # ===== Cluster 3: アフェクトターン =====
    ("セジウィック偏執的読解批判", "Sedgwick Paranoid Reading Critique", "Paranoid Reading and Reparative Reading", "english",
     "横断", P_AFFECT,
     "批評が暴露・告発志向に偏ることへの批判、修復的読解への転換を提唱した宣言。"),
    ("バーラント『親密な公共性』", "Berlant Intimate Publics", "The Female Complaint", "english",
     "横断", P_AFFECT,
     "女性向け大衆文化に形成される情動的共同性を分析、公私の境界を再定義する。"),
    ("アーメッド『情動の文化政治学』", "Ahmed Cultural Politics of Emotion", "The Cultural Politics of Emotion", "english",
     "横断", P_AFFECT,
     "情動が他者を構築し対象化する政治的機能を分析、感情の表面的循環を批判する。"),
    ("マッスミ『寓話論』", "Massumi Parables for the Virtual", "Parables for the Virtual", "english",
     "横断", P_AFFECT,
     "ドゥルーズ的情動論を運動・身体・潜在性の理論として展開、認知主義を超える試み。"),
    ("ンガイ stuplimity概念", "Ngai stuplimity Concept", "stuplimity", "english",
     "横断", P_AFFECT,
     "崇高と退屈の混合的情動を新造語で理論化、現代の倦怠美学を批評する独創概念。"),
    ("フランク・セジウィック共著情動論", "Frank-Sedgwick Affect Reader", "Shame and its Sisters", "english",
     "横断", P_AFFECT2,
     "トムキンスのシステム理論をクィア批評に接続、恥の情動論を文学批評に導入。"),

    # ===== Cluster 4: 物質性・本のメディア =====
    ("シャルチエ『書物の秩序』", "Chartier Order of Books", "L'Ordre des livres", "french",
     "西欧", P_BOOK_HIST,
     "読書実践と書物形式の歴史的変容を分析、テクストの物質的条件を理論化する。"),
    ("マッケンジー『テクスト社会学』", "McKenzie Sociology of Texts", "Bibliography and the Sociology of Texts", "english",
     "西欧", P_BOOK_HIST,
     "書誌学を物理書物のみならず社会的伝達過程として再定義、書物史の方法論を刷新。"),
    ("マガン『テクストの条件』", "McGann Textual Condition", "The Textual Condition", "english",
     "西欧", P_BOOK_HIST,
     "テクストの物質性・社会性が意味形成を規定すると主張、編集理論の方法論的転換。"),
    ("ヘイルズ『書く機械』", "Hayles Writing Machines", "Writing Machines", "english",
     "横断", P_BOOK_HIST,
     "メディア特性を意識した文学解釈の必要を提唱、デジタル時代の物質批評を開く。"),
    ("ギトルマン『紙の知識』", "Gitelman Paper Knowledge", "Paper Knowledge", "english",
     "横断", P_BOOK_HIST,
     "ドキュメントというメディア形式の歴史を辿り、知識生産における紙の文化を分析。"),
    ("キルシェンバウム『機構』", "Kirschenbaum Mechanisms", "Mechanisms", "english",
     "横断", P_BOOK_HIST,
     "デジタル文学の物質性を磁気記録・ストレージ層から分析、電子テクストの考古学。"),

    # ===== Cluster 5: ナラトロジー新世代 =====
    ("ライアン『可能世界・人工知能・物語論』", "Ryan Possible Worlds AI Narrative", "Possible Worlds, Artificial Intelligence, and Narrative Theory", "english",
     "横断", P_NARRATOLOGY,
     "可能世界論理学を物語論に応用、フィクション世界の再中心化原理を体系化する。"),
    ("フルダーニク『自然のナラトロジー』", "Fludernik Towards a Natural Narratology", "Towards a Natural Narratology", "english",
     "西欧", P_NARRATOLOGY,
     "経験性を物語性の核心に据え、認知言語学的物語論を構築する第二世代理論。"),
    ("ハーマン『ストーリー・ロジック』", "Herman Story Logic", "Story Logic", "english",
     "横断", P_NARRATOLOGY,
     "認知科学・言語学を統合した物語論、心的シミュレーションとしての物語を理論化。"),
    ("アルバー『不自然な物語』", "Alber Unnatural Narrative", "Unnatural Narrative", "english",
     "西欧", P_NARRATOLOGY,
     "現実物理法則を逸脱する物語を体系的に分析、自然化を超える読解戦略を提唱する。"),
    ("リチャードソン『不自然な声』", "Richardson Unnatural Voices", "Unnatural Voices", "english",
     "横断", P_NARRATOLOGY,
     "一人称・二人称・複数語り等の異例な語りを分析、ジュネット枠組みの拡張を試みる。"),
    ("メレトーヤ『物語論的解釈学』", "Meretoja Narrative Hermeneutics", "The Ethics of Storytelling", "english",
     "西欧", P_NARRATOLOGY,
     "物語が経験と倫理を媒介する解釈学的機能を理論化、語ることの倫理的次元を探究。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, region, period_id, definition in CONCEPTS:
        if len(definition) > 100:
            print(f"[ERR] definition too long ({len(definition)} chars): {name_ja}", file=sys.stderr)
            continue
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score, source_tier)
                VALUES (?, ?, ?, ?, 22, ?, ?, ?, 3, 'tier1')
            """, (name_ja, name_en, name_orig, script, region, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"[SKIP] {name_ja}: {e}", file=sys.stderr)
            skipped += 1
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
