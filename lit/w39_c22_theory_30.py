#!/usr/bin/env python3
"""Wave 39: add 30 ultra-niche concepts to lit_theory (subfield 22)."""

from lit_db_helper import LitDB

REGION = "横断"
SUBFIELD = "lit_theory"

# 5 thematic clusters x 6 concepts. period_id intentionally NULL for cross-regional theory.
CONCEPTS = [
    # Cluster 1: minor narratology / unnatural narrative
    ("アルバー認知的再枠づけ", "Alber cognitive reframing", "Unnatural Narrative", "latin",
     "不自然な物語を読者が現実枠から再解釈する認知的処理。"),
    ("リチャードソン二人称語り論", "Brian Richardson second-person narrative", "Unnatural Voices", "latin",
     "二人称語りを通常の人称体系から逸脱する物語声として分析。"),
    ("パヴェル虚構世界の存在論", "Thomas Pavel fictional worlds", "Fictional Worlds", "latin",
     "虚構世界を独自の存在論的領域として扱う物語意味論。"),
    ("ドールツェル異世界意味論", "Lubomir Dolezel heterocosmica", "Heterocosmica", "latin",
     "文学作品を可能世界の構築物として記述する虚構意味論。"),
    ("ウォー実験的メタフィクション論", "Patricia Waugh metafiction", "Metafiction", "latin",
     "自己言及的小説を現実表象の危機を示す実験形式として読む。"),
    ("マクヘイル存在論的ドミナント", "McHale ontological dominant", "Postmodernist Fiction", "latin",
     "ポストモダン小説の焦点を認識論から存在論へ移す概念。"),

    # Cluster 2: postclassical rhetoric / lyric theory
    ("カヴァナー叙情詩の陳述論", "Jonathan Culler lyric address", "Theory of the Lyric", "latin",
     "叙情詩を発話状況より儀礼的陳述として読む理論。"),
    ("プリンス被物語者論", "Gerald Prince narratee", "narratee", "latin",
     "語りの内部で語り手が想定する受け手を区別する物語論概念。"),
    ("フェラン不安定性の進行", "James Phelan progression instability", "progression", "latin",
     "物語の不均衡と解決過程を読者判断の連鎖として捉える。"),
    ("ラビノヴィッツ読解規則論", "Peter Rabinowitz rules of reading", "Before Reading", "latin",
     "読者がジャンル慣習から作品理解を組織する規則群の理論。"),
    ("コーン精神透明性論", "Dorrit Cohn transparency", "Transparent Minds", "latin",
     "小説が他者意識を直接提示する技法を分類する物語論。"),
    ("ケイト・ハンバーガー叙述論", "Kate Hamburger logic of literature", "Die Logik der Dichtung", "german",
     "文学発話を実在発話と異なる論理で捉えるドイツ語圏理論。"),

    # Cluster 3: book history / bibliography micro-traditions
    ("マクガン社会化テクスト論", "Jerome McGann socialized text", "A Critique of Modern Textual Criticism", "latin",
     "作品本文を作者意図でなく出版・編集の社会過程から捉える。"),
    ("ブライアント流動テクスト論", "John Bryant fluid text", "The Fluid Text", "latin",
     "改稿・版差・翻案を作品の変異過程として扱う編集理論。"),
    ("シャイリングスバーグ文書証拠論", "Shillingsburg documentary evidence", "Scholarly Editing", "latin",
     "校訂で物理資料の証拠性を優先する英米書誌学の方法。"),
    ("ティアンズ応答する書誌学", "Marta Tians responsive bibliography", "Book Use, Book Theory", "latin",
     "読者の使用痕跡を本文解釈に組み込む物質的書物研究。"),
    ("マッケンジー意味形成の形式論", "D. F. McKenzie forms effect meaning", "Sociology of Texts", "latin",
     "活字・紙面・流通形式が意味を作るとする書誌学命題。"),
    ("ガーベイ再利用紙片文化論", "Ellen Gruber Garvey scrap culture", "Writing with Scissors", "latin",
     "切抜き帳文化を読者参加型の再編集実践として分析する。"),

    # Cluster 4: decolonial / minor postcolonial theory
    ("グリッサン不透明性の権利", "Glissant right to opacity", "droit a l'opacite", "french",
     "他者を透明に理解し尽くす欲望を拒むカリブ海思想の概念。"),
    ("ブランスコム沈黙の翻訳論", "Kamau Brathwaite nation language", "History of the Voice", "latin",
     "植民地英語に抗する声・リズム・島嶼言語性の詩学。"),
    ("チャンドラ・モハンティ第三世界女性批判", "Chandra Mohanty Third World woman", "Under Western Eyes", "latin",
     "西洋フェミニズムが単一化する第三世界女性像を批判。"),
    ("ガンディポストコロニアル倫理", "Leela Gandhi postcolonial ethics", "Postcolonial Theory", "latin",
     "反植民地主義を友情・禁欲・倫理的関係から読み替える理論。"),
    ("チェン・クワンシン脱帝国方法", "Kuan-Hsing Chen Asia as Method", "Asia as Method", "latin",
     "アジア内部の参照軸で冷戦・帝国知を相対化する方法論。"),
    ("ニルマル・プワール空間侵入者論", "Nirmal Puwar space invaders", "Space Invaders", "latin",
     "制度空間に入る人種化・性別化身体の違和を分析する概念。"),

    # Cluster 5: affect, reception, and ordinary reading
    ("スチュアート日常の雰囲気論", "Kathleen Stewart ordinary affects", "Ordinary Affects", "latin",
     "日常の微細な感触や気配を情動の生成場として記述する。"),
    ("フラットリー情動地図論", "Jonathan Flatley affective mapping", "Affective Mapping", "latin",
     "憂鬱を歴史的連帯へ接続する読解地図として理論化する。"),
    ("ラブ記述的読解論", "Heather Love descriptive reading", "description", "latin",
     "解釈の深さより観察と記述を重視するポスト批評的方法。"),
    ("ドナルドソン認知的脚本論", "Elizabeth Donaldson cognitive script", "cognitive disability studies", "latin",
     "障害表象を読者の認知的脚本の変容から分析する方法。"),
    ("ライリー失読症的読解論", "Denise Riley dysfluency", "The Words of Selves", "latin",
     "自己語りの途切れや言いよどみを主体形成の問題として読む。"),
    ("マッカーシー普通読者の制度論", "Mary McCarthy ordinary reader", "ordinary reader", "latin",
     "専門批評外の読書判断を文学制度との緊張で捉える読者論。"),
]


def main() -> None:
    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 22"
            )
        }
        inserted = 0
        skipped = 0
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            if name_ja in existing:
                skipped += 1
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=None,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 1
        print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
