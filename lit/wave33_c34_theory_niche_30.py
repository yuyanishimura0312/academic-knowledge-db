#!/usr/bin/env python3
"""Wave 33 C34: lit_theory niche 30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 22
PERIOD_ID = 12  # 現代

CONCEPTS = [
    # Cluster 1: Trauma + memory studies
    ("カルース『取り戻されざる経験』", "Caruth: Unclaimed Experience", "横断", "トラウマは遅延と反復で証言される、表象の不可能性をめぐる文学批評の枠組み。"),
    ("フェルマン『証言』", "Felman: Testimony", "横断", "ホロコースト後の証言理論、教える＝聴くことの倫理を文学批評と精神分析で統合。"),
    ("ハーシュ『ポストメモリ世代』", "Hirsch: The Generation of Postmemory", "西欧", "第二世代が継承する間接的トラウマ記憶を写真と物語から論じるポストメモリ概念。"),
    ("ラカプラ『歴史を書く、トラウマを書く』", "LaCapra: Writing History, Writing Trauma", "西欧", "歴史記述におけるアクティングアウトとワーキングスルーの区別、トラウマ史学方法論。"),
    ("ロスバーグ『多方向的記憶』", "Rothberg: Multidirectional Memory", "横断", "ホロコーストと脱植民地化記憶を競合ではなく相互参照する多方向的記憶モデル。"),
    ("コナトン『近代社会はいかに忘却するか』", "Connerton: How Modernity Forgets", "西欧", "近代の場所喪失と速度が集合的忘却を生む過程を社会的記憶論として理論化。"),

    # Cluster 2: Ecocriticism deeper
    ("ビュエル『環境批評の未来』", "Buell: The Future of Environmental Criticism", "西欧", "第一波・第二波エコクリティシズムの統合と環境的想像力の再定義を提示する綱領的著作。"),
    ("ハイザ『絶滅を想像する』", "Heise: Imagining Extinction", "西欧", "種絶滅の物語と多種文化記述を通じて生物多様性ナラティブを批評する文化分析。"),
    ("ガラード『エコクリティシズム』", "Garrard: Ecocriticism", "西欧", "汚染・荒野・終末論等の主題群でエコクリティシズム史を体系化した入門理論書。"),
    ("イオヴィーノ『物質的エコクリティシズム』", "Iovino: Material Ecocriticism", "西欧", "物質の語りと身体性を中心に据える物質的エコクリティシズムの理論枠組。"),
    ("プラムウッド『環境文化』", "Plumwood: Environmental Culture", "横断", "理性／自然の二元論を批判し合理主義の生態学的危機を文化哲学として論じる。"),
    ("モートン『ハイパーオブジェクト』", "Morton: Hyperobjects", "西欧", "気候変動など時空を超えた巨大対象＝ハイパーオブジェクトの美学と倫理を提案。"),

    # Cluster 3: Queer theory deeper
    ("ハルバースタム『女性的男性性』", "Halberstam: Female Masculinity", "西欧", "男性性を男性身体から切り離し女性的男性性として理論化したクィア批評の鍵著作。"),
    ("ムニョス『クルージング・ユートピア』", "Muñoz: Cruising Utopia", "西欧", "クィアな未来性と希望を反未来主義に対抗して論じる遂行的ユートピア論。"),
    ("エーデルマン『ノー・フューチャー』", "Edelman: No Future", "西欧", "再生産的未来主義と子供のシンボルを批判し死動因に立つ反社会的クィア理論。"),
    ("プアール『テロリスト・アサンブラージュ』", "Puar: Terrorist Assemblages", "横断", "ホモナショナリズムとアサンブラージュ概念で人種・性・テロ言説を分析。"),
    ("ファーガソン『逸脱の黒人性』", "Ferguson: Aberrations in Black", "西欧", "クィア・オブ・カラー批評を制度化し正典社会学のセクシュアリティ前提を解体。"),
    ("リード=ファール『黒人ゲイ男性』", "Reid-Pharr: Black Gay Man", "西欧", "黒人男性同性愛主体を文学・批評・自伝で交錯させ人種とクィアを再接続。"),

    # Cluster 4: Black studies
    ("ハートマン『気ままな生』", "Hartman: Wayward Lives", "西欧", "二〇世紀初頭の黒人女性の日常を批評的虚構で再構成する思弁的アーカイヴ実践。"),
    ("シャープ『航跡の中で』", "Sharpe: In the Wake", "西欧", "中間航路の余波を生きる黒人生の状況を「ウェイク」概念で理論化する黒人研究。"),
    ("モテン『盗まれた生』", "Moten: Stolen Life", "西欧", "黒人逃走と下生（アンダーコモンズ）を音と詩学で論じる黒人ラディカル伝統の理論。"),
    ("スピラーズ「ママのベビー、パパのたぶん」", "Spillers: Mama's Baby, Papa's Maybe", "西欧", "肉と身体の区別から奴隷制下のジェンダー文法を論じる黒人フェミニズム古典論文。"),
    ("ウィルダーソン『赤・白・黒』", "Wilderson: Red, White & Black", "西欧", "アフロペシミズムを映画・批評で展開、黒人性を社会的死として位置づける枠組。"),
    ("ウォーレン『存在論的恐怖』", "Warren: Ontological Terror", "西欧", "黒人を非存在として位置づける形而上学的反黒人性をハイデガー読解で批判。"),

    # Cluster 5: Posthuman + digital theory
    ("ブライドッティ『ポストヒューマン的知』", "Braidotti: Posthuman Knowledge", "西欧", "批判的ポストヒューマニズムを学知の再編とノマド的主体性として体系化した近著。"),
    ("ヘイルズ『ポストヒューマンの誕生』", "Hayles: How We Became Posthuman", "西欧", "情報・身体・サイバネティクスから人間概念の解体を辿るポストヒューマン文学批評。"),
    ("ウルフ『法の前で』", "Wolfe: Before the Law", "西欧", "種境界とバイオポリティクスを動物・障害・法で交差させるポストヒューマン理論。"),
    ("ガロウェイ『エクスコミュニケーション』", "Galloway: Excommunication", "西欧", "媒介の三位（ヘルメス・イリス・ファロス）でメディア理論を再編する三人共著。"),
    ("チョン『更新は同じまま留まる』", "Chun: Updating to Remain the Same", "横断", "ニューメディアの習慣性と更新性を批判するソフトウェア文化論。"),
    ("ブライドル『ニュー・ダーク・エイジ』", "Bridle: New Dark Age", "西欧", "計算的思考の不透明性が知の闇を増殖させる過程を批評するデジタル文化論。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, region, definition in CONCEPTS:
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, subfield_id, region, period_id, definition,
                    importance_score, source_tier)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (name_ja, name_en, SUBFIELD_ID, region, PERIOD_ID, definition, 4, "core"),
            )
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped} total={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
