#!/usr/bin/env python3
"""Wave 37: 30 niche concepts for subfield_id=22 (lit_theory)."""
import sqlite3
import sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# 5 thematic clusters x 6 concepts = 30
# Each: (name_ja, name_en, name_original, original_script, region, period_id, definition, importance)
CONCEPTS = [
    # Cluster 1: 21世紀理論細部 (period 180/182, region=横断)
    ("レヴィン『フォームズ』", "Caroline Levine 'Forms'", "Forms: Whole, Rhythm, Hierarchy, Network", "latin", "横断", 182,
     "形式を全体・リズム・階層・ネットワーク4類型で再定義し美学と政治を架橋", 4),
    ("フェルスキ『批評の限界』", "Rita Felski 'The Limits of Critique'", "The Limits of Critique", "latin", "横断", 180,
     "懐疑批評の限界を指摘しポスト批評・愛着的読解への転換を提唱", 4),
    ("モイ『普通の言葉の革命』", "Toril Moi 'Revolution of the Ordinary'", "Revolution of the Ordinary", "latin", "横断", 180,
     "ウィトゲンシュタイン後期言語観で文学批評の常識を組み替える日常言語批評", 3),
    ("ンガイ『不快な感情』", "Sianne Ngai 'Ugly Feelings'", "Ugly Feelings", "latin", "横断", 180,
     "嫉妬・苛立ち等の弱い負の情動が後期資本主義美学を構成すると論じる", 4),
    ("バーラント残酷な楽観主義", "Berlant cruel optimism", "Cruel Optimism", "latin", "横断", 180,
     "幸福を約束する対象が逆に幸福を阻害する執着構造を分析する情動理論", 4),
    ("フィッシャー資本主義リアリズム", "Mark Fisher capitalist realism", "Capitalist Realism", "latin", "横断", 182,
     "資本主義以外を想像できない文化状況を批評する21世紀左派文化理論", 4),

    # Cluster 2: ポスト批評・ポスト理論 (period 180/181)
    ("ベスト＝マーカス表層読解", "Best & Marcus surface reading", "Surface Reading", "latin", "横断", 180,
     "症候読解への対抗として表層に注意を払う記述的読解実践", 4),
    ("ポスト批評・修復的読解", "Postcritique reparative reading", "Postcritique / Reparative Reading", "latin", "横断", 180,
     "懐疑解釈学を脱し愛着・修復・記述を重視する21世紀批評運動", 4),
    ("セジウィック偏執／修復的読解", "Sedgwick paranoid/reparative", "Paranoid/Reparative Reading", "latin", "横断", 180,
     "偏執的暴露読解と修復的読解の対比により批評倫理を再構築", 4),
    ("モレッティ遠読・精読対比", "Moretti distant vs close reading", "Distant Reading", "latin", "横断", 181,
     "個別精読を超え数千冊規模の量的パターン抽出を可能にする読解法", 4),
    ("マノヴィッチ文化分析学", "Manovich cultural analytics", "Cultural Analytics", "latin", "横断", 181,
     "大規模デジタル文化データを統計可視化で分析する計算文化研究", 3),
    ("計算文学研究", "Computational Literary Studies", "Computational Literary Studies", "latin", "横断", 181,
     "機械学習・NLPを用いて文学コーパスから様式・主題変遷を抽出する潮流", 4),

    # Cluster 3: エコクリティシズム細部 (period 182, 横断)
    ("ラトゥール地球的存在論", "Latour earthbound", "Down to Earth / Terrestrial", "latin", "横断", 182,
     "近代の自然/社会二分を脱し地球と結ばれた地球生物として政治を再構想", 4),
    ("ハラウェイ・クトゥルー新世", "Haraway Chthulucene", "Chthulucene", "latin", "横断", 182,
     "人新世を超え多種共生・触手的時代としての新地質時代概念", 4),
    ("ツィン『マツタケ』", "Anna Tsing 'Mushroom at the End'", "The Mushroom at the End of the World", "latin", "横断", 182,
     "資本主義廃墟で生きる多種協働を松茸交易から描くマルチスピーシーズ民族誌", 4),
    ("ゴーシュ『大いなる錯乱』", "Ghosh 'The Great Derangement'", "The Great Derangement", "latin", "横断", 182,
     "近代小説形式が気候危機を表象し損なう構造的失敗を批判するエコ批評", 4),
    ("ニクソン緩慢な暴力", "Rob Nixon slow violence", "Slow Violence", "latin", "横断", 182,
     "可視化されにくい長期環境破壊を貧者の暴力として概念化", 4),
    ("アライモ・トランスコーポリアリティ", "Stacy Alaimo trans-corporeality", "Trans-corporeality", "latin", "横断", 182,
     "人間身体と環境物質の連続的相互浸透を物質的フェミニズムから論じる", 3),

    # Cluster 4: ポストヒューマン・AI理論 (period 182)
    ("ヘイルズ『未思考』", "Hayles 'Unthought'", "Unthought: Power of Nonconscious", "latin", "横断", 182,
     "非意識認知が人間と技術系を貫く認知アセンブリを構成すると論じる理論", 4),
    ("ブライドッティ・ポストヒューマン", "Braidotti posthuman", "The Posthuman", "latin", "横断", 182,
     "人間中心主義を脱し生命物質の連続性に立つノマド的批判理論", 4),
    ("バラッド・エージェンシャル・リアリズム", "Barad agential realism", "Agential Realism", "latin", "横断", 182,
     "物質と意味が内的作用で同時生成すると論じる量子的フェミニズム存在論", 4),
    ("スティグレール象徴的悲惨", "Stiegler Symbolic Misery", "Misère symbolique", "latin", "横断", 182,
     "産業的記号生産が個体化と感性を破壊する後期資本主義の象徴危機論", 3),
    ("AI著者性論争", "AI authorship debate", "AI Authorship Debate", "latin", "横断", 182,
     "生成AI時代における著者・創造性・原作性の再定義をめぐる文学理論論争", 4),
    ("ストリファス・アルゴリズム文化", "Striphas algorithmic culture", "Algorithmic Culture", "latin", "横断", 182,
     "アルゴリズムが文化選別と読書実践を媒介する新たな文化形態の分析枠組", 3),

    # Cluster 5: ディスアビリティ・クィア・新唯物論 (period 275, 横断)
    ("マクルアー・クリップ理論", "McRuer crip theory", "Crip Theory", "latin", "横断", 275,
     "強制的健常性を批判しクィア理論と障害学を接合する批判理論", 4),
    ("シーバーズ障害美学", "Siebers disability aesthetics", "Disability Aesthetics", "latin", "横断", 275,
     "障害身体が現代美学を再構成すると論じる美学理論", 3),
    ("ムニョス『クルージング・ユートピア』", "Muñoz 'Cruising Utopia'", "Cruising Utopia", "latin", "横断", 182,
     "クィア未来性を此岸に未到来のユートピア地平として再起動する理論", 4),
    ("エーデルマン・ノー・フューチャー", "Edelman 'No Future'", "No Future", "latin", "横断", 182,
     "再生産的未来主義を拒絶しクィア反社会的否定性を擁護する理論", 4),
    ("バラッド宇宙の途上で出会う", "Barad 'Meeting Universe Halfway'", "Meeting the Universe Halfway", "latin", "横断", 182,
     "観測と現象の内的作用を量子力学から導く新唯物論的存在論の主著", 4),
    ("ベネット活気ある物質", "Bennett vibrant matter", "Vibrant Matter", "latin", "横断", 182,
     "物が政治的アクターとして作用すると論じる新唯物論的政治生態学", 4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        name_ja, name_en, name_orig, script, region, period_id, definition, importance = c
        if len(definition) > 100:
            print(f"DEFINITION TOO LONG ({len(definition)}): {name_ja}")
            sys.exit(1)
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier)
                VALUES (?, ?, ?, ?, 22, ?, ?, ?, ?, 'tier2')
            """, (name_ja, name_en, name_orig, script, region, period_id, definition, importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=22").fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield 22: {total}")

if __name__ == "__main__":
    main()
