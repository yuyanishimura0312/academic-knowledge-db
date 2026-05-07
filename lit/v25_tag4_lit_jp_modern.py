#!/usr/bin/env python3
import os
import sqlite3


DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
VALID_AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}
VALID_STATUS = {"rethinking", "partial", "invariant"}


RATIONALES = {
    "作者性": ("rethinking", "作者経験と作品声の結合がAI代筆で揺らぐ", "AI代筆"),
    "創造性": ("rethinking", "独創的発想や造形が生成支援で再配分される", "生成支援創作"),
    "物語": ("partial", "物語構造や類型が自動生成で再利用される", "物語生成"),
    "主体": ("rethinking", "近代的内面や倫理的主体が擬似主体生成で問い直される", "擬似主体生成"),
    "正典": ("partial", "文学史的評価が推薦アルゴリズムや教材化で再編される", "推薦アルゴリズム"),
    "受容": ("partial", "読者共同体や流通制度が生成配信環境で変質する", "生成配信"),
    "翻訳": ("rethinking", "翻訳・翻案の創造的媒介性が機械翻訳で再考される", "機械翻訳"),
    "真正性": ("rethinking", "記録や体験の真実性が合成証言で揺らぐ", "合成証言"),
    "言語": ("rethinking", "文体・詩語・口語表現が大規模言語生成で模倣される", "文体生成"),
}


def add_axis(axes, axis):
    if axis in VALID_AXES and axis not in axes:
        axes.append(axis)


def classify(name, definition):
    text = f"{name} {definition}"
    axes = []

    if any(k in text for k in ("訳", "翻訳", "翻案", "西欧", "異国", "多言語", "英文")):
        add_axis(axes, "翻訳")
    if any(k in text for k in ("日記", "自伝", "従軍記", "記録", "証言", "被爆", "敗戦", "捕虜", "体験")):
        add_axis(axes, "真正性")
    if any(k in text for k in ("詩", "歌集", "短歌", "文体", "口語", "雅文", "漢文", "言文一致", "象徴", "比喩")):
        add_axis(axes, "言語")
    if any(k in text for k in ("評論", "論争", "思想書", "文学理論", "史論", "幸福論", "日本語論")):
        add_axis(axes, "受容")
    if any(k in text for k in ("最高傑作", "代表作", "規範", "古典", "教科書", "文学史", "到達点", "受賞", "ベストセラー")):
        add_axis(axes, "正典")
    if any(k in text for k in ("私小説", "作者", "一葉", "晶子", "女性作家", "代筆", "告白")):
        add_axis(axes, "作者性")
    if any(k in text for k in ("主体", "自我", "内面", "青年", "女性", "倫理", "実存", "孤独", "虚無")):
        add_axis(axes, "主体")
    if any(k in text for k in ("シュルレアリスム", "前衛", "幻想", "独自", "革新", "創造", "想像力")):
        add_axis(axes, "創造性")
    if any(k in text for k in ("小説", "童話", "戯曲", "物語", "シリーズ", "長編", "中編", "短編", "会話劇")):
        add_axis(axes, "物語")

    if not axes:
        add_axis(axes, "受容")
    return axes[:2]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 11 AND ftt.id IS NULL
        ORDER BY c.id
        LIMIT 100
        """
    ).fetchall()

    inserts = []
    for concept_id, name, definition in rows:
        for axis in classify(name or "", definition or ""):
            status, rationale, phenomenon = RATIONALES[axis]
            if axis not in VALID_AXES or status not in VALID_STATUS:
                raise ValueError((concept_id, axis, status))
            inserts.append((concept_id, axis, status, rationale, phenomenon))

    before = conn.total_changes
    cur.executemany(
        """
        INSERT OR IGNORE INTO fourth_transform_tags
            (concept_id, axis, status, rationale, related_ai_phenomenon)
        VALUES (?, ?, ?, ?, ?)
        """,
        inserts,
    )
    conn.commit()
    inserted = conn.total_changes - before
    remaining = cur.execute(
        """
        SELECT COUNT(*)
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 11 AND ftt.id IS NULL
        """
    ).fetchone()[0]
    conn.close()
    print(f"concepts={len(rows)} attempted_tags={len(inserts)} inserted={inserted} remaining_untagged={remaining}")


if __name__ == "__main__":
    main()
