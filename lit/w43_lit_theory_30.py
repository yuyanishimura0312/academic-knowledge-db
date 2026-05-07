#!/usr/bin/env python3
from lit_db_helper import LitDB

DB = "lit.sqlite"
SUBFIELD = "lit_theory"
REGION = "理論"

PERIODS = {
    "narratology": "構造主義・ポスト構造主義期",
    "paratext": "ポスト構造主義以後の批評期",
    "affect": "環境・脱植民地・ポストヒューマン期",
    "postcolonial": "世界文学・ポストコロニアル翻訳期",
    "digital": "デジタル人文学・AI時代",
}

CONCEPTS = [
    # Cluster 1: micro-narratology
    ("接続詞残響ナラトロジー", "Conjunctive Echo Narratology", "conjunctive echo", "段落冒頭接続詞が前場面の余韻を保つ語りの微細効果。", "narratology"),
    ("無標引用符の声源錯乱論", "Unmarked Quotation Voice Drift", "unmarked quotation", "引用符なき発話が語り手と人物の声源を曖昧化する現象。", "narratology"),
    ("代名詞遅延同定の焦点化論", "Delayed Pronoun Identification", "delayed pronoun ID", "代名詞の指示対象を遅らせて視点情報を制御する技法。", "narratology"),
    ("反復副詞の時間粘度論", "Temporal Viscosity of Repeated Adverbs", "repeated adverbs", "同一副詞の反復が出来事時間を粘らせる叙述効果。", "narratology"),
    ("省略ダッシュの語り沈黙論", "Narrative Silence of Elliptic Dashes", "elliptic dashes", "ダッシュ省略が発話不能や検閲を局所的に示す読解点。", "narratology"),
    ("群像章の視点余剰論", "Focal Surplus in Ensemble Chapters", "focal surplus", "群像章で視点情報が人物数を超えて漏れ出す構成問題。", "narratology"),

    # Cluster 2: paratext and textual materiality
    ("折込図版の読解遅延論", "Foldout Plate Reading Delay", "foldout plates", "折込図版が本文読解の順序と中断を作る物質的効果。", "paratext"),
    ("献辞空欄の名宛て不在論", "Blank Dedication Addressee Absence", "blank dedication", "献辞欄の空白が受取人不在を読む余地を作るパラテクスト。", "paratext"),
    ("版元広告の逆正典化論", "Publisher Advertisements and Counter-Canon", "publisher ads", "巻末広告が同時代の別正典を可視化する読書史論点。", "paratext"),
    ("誤植表の権威回復論", "Errata List Authority Repair", "errata list", "誤植表が本文の信頼性を回復しつつ欠陥を記録する機能。", "paratext"),
    ("紙葉透けの両面読解論", "Show-Through Bifacial Reading", "show-through", "薄紙の裏写りが表裏二面の同時読解を誘う物質性。", "paratext"),
    ("装幀背文字の棚読解論", "Spine Lettering Shelf Reading", "spine lettering", "背文字が棚上で作品同士の隣接関係を作る読解条件。", "paratext"),

    # Cluster 3: affective and readerly microstates
    ("羞恥回避の斜め読み論", "Shame-Avoidant Skimming", "shame skimming", "羞恥を誘う場面で読者が速度と注視を変える反応。", "affect"),
    ("未完結文の不安保持論", "Anxiety Retention in Unfinished Sentences", "unfinished sentences", "未完結文が不安の解消を先送りする情動的仕掛け。", "affect"),
    ("反感人物への注意固着論", "Attention Fixation on Disliked Characters", "disliked characters", "嫌悪対象の人物ほど読者注意を固定する逆説的効果。", "affect"),
    ("退屈の局所倫理論", "Local Ethics of Boredom", "local boredom", "退屈な箇所を飛ばすか耐えるかをめぐる読者倫理。", "affect"),
    ("再読羞恥の記憶更新論", "Memory Updating in Rereading Shame", "rereading shame", "再読時の羞恥が初読記憶を上書きする情動過程。", "affect"),
    ("共感拒否の批評的効用論", "Critical Use of Empathy Refusal", "empathy refusal", "共感しない読解が作品理解を深める場合を扱う論点。", "affect"),

    # Cluster 4: minor postcolonial and world-literary methods
    ("港湾訛りの帝国語読解論", "Imperial Reading of Port Accents", "port accents", "港湾混成語を帝国語秩序の揺らぎとして読む方法。", "postcolonial"),
    ("領事報告の文学場攪乱論", "Consular Reports and Literary Field Distortion", "consular reports", "領事報告が周縁文学の分類と価値を歪める作用。", "postcolonial"),
    ("植民地書店目録の世界文学論", "Colonial Bookshop Catalog World Literature", "bookshop catalogs", "植民地書店目録から世界文学流通を読む資料論。", "postcolonial"),
    ("非同盟会議詩学", "Non-Aligned Conference Poetics", "non-aligned poetics", "非同盟会議の語彙が詩と声明文に渡る形式を読む視角。", "postcolonial"),
    ("越境脚注の主権攪乱論", "Border-Crossing Footnote Sovereignty", "border footnotes", "国境説明の脚注が主権的地図認識を揺さぶる働き。", "postcolonial"),
    ("密輸本パラテクスト論", "Smuggled Book Paratexts", "smuggled books", "密輸本の印章や隠し表紙を読解対象にする方法。", "postcolonial"),

    # Cluster 5: digital and AI literary theory
    ("OCR誤読の批評的偶然論", "Critical Contingency of OCR Misreading", "OCR misreading", "OCR誤読をノイズでなく解釈の偶然性として扱う視角。", "digital"),
    ("埋め込み空間のジャンル滲出論", "Genre Bleed in Embedding Space", "embedding genre bleed", "埋め込み空間でジャンル境界が連続的に滲む現象。", "digital"),
    ("プロンプト注釈の作者性論", "Authorship of Prompt Annotation", "prompt annotation", "生成AIへの注釈指示を共同作者性として読む論点。", "digital"),
    ("幻典拠の引用倫理論", "Citation Ethics of Phantom Sources", "phantom sources", "生成AIが作る架空典拠を批評実践の倫理問題として扱う。", "digital"),
    ("トークン境界の詩行切断論", "Token Boundary Lineation", "token lineation", "トークン分割が詩行や語感の単位をずらす問題。", "digital"),
    ("合成読者モデルの受容美学", "Reception Aesthetics of Synthetic Readers", "synthetic readers", "AI読者モデルを受容美学の仮想読者として検討する視角。", "digital"),
]


def period_id(db, key):
    name = PERIODS[key]
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja = ? AND region = ?",
        (name, REGION),
    ).fetchone()
    if not row:
        raise SystemExit(f"missing theory period: {name}")
    return row["id"]


def main():
    with LitDB(DB) as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 22"
        ).fetchone()[0]
        existing = {r["name_ja"] for r in db.conn.execute("SELECT name_ja FROM concepts")}

        if len(CONCEPTS) != 30:
            raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")

        seen = set()
        pids = {key: period_id(db, key) for key in PERIODS}
        for name_ja, _, _, definition, key in CONCEPTS:
            if name_ja in seen:
                raise SystemExit(f"duplicate in script: {name_ja}")
            if name_ja in existing:
                raise SystemExit(f"duplicate in DB: {name_ja}")
            if len(definition) > 100:
                raise SystemExit(f"definition too long: {name_ja} ({len(definition)})")
            seen.add(name_ja)
            if key not in pids:
                raise SystemExit(f"unknown cluster key: {key}")

        for name_ja, name_en, name_original, definition, key in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=pids[key],
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="minor",
            )

        db.conn.commit()
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 22"
        ).fetchone()[0]
        print(f"Inserted {after - before}; total {after}")


if __name__ == "__main__":
    main()
