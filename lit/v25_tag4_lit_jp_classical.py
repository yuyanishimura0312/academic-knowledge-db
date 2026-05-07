#!/usr/bin/env python3
import os
import sqlite3


DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")

AXES = {"作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"}
STATUS = {"rethinking", "partial", "invariant"}

RULES = [
    ("翻訳", "partial", ("唐土", "漢文", "漢詩", "真名", "和漢", "訓字", "異文化", "遣唐")),
    ("正典", "partial", ("勅撰", "私家集", "歌集", "和歌集", "集", "部立", "正典", "三十六", "八代", "二十一代")),
    ("作者性", "rethinking", ("作者未詳", "作説", "編纂", "撰", "歌人", "世阿弥", "近松", "西鶴", "秋成", "定家", "俊成")),
    ("物語", "rethinking", ("物語", "軍記", "説話", "日記", "紀行", "心中", "恋愛", "悲恋", "輪廻", "事件", "章")),
    ("主体", "rethinking", ("女性", "皇女", "女帝", "女房", "御製", "辞世", "恋", "内面", "声", "和泉式部")),
    ("言語", "rethinking", ("歌風", "文体", "語", "詞", "訓字", "枕詞", "序詞", "和漢混淆", "漢文体")),
    ("受容", "partial", ("影響", "継承", "流派", "後続", "受容", "引用", "伝来", "体系化", "祖型")),
    ("真正性", "rethinking", ("論争", "記録", "史", "御製", "辞世", "事件", "自撰", "筆録", "公式")),
    ("創造性", "partial", ("連歌", "俳諧", "作劇", "発句", "作法", "演技", "狂言", "滑稽", "諧謔")),
]

RATIONALES = {
    "作者性": ("作者・編者の帰属や仮託がAI著者推定と生成代筆で揺らぐ", "著者推定"),
    "創造性": ("型と新作の境界がAI支援創作で再考される", "AI創作支援"),
    "物語": ("古典的な筋立てや再話構造が物語生成で再利用される", "物語生成"),
    "主体": ("詠み手や語り手の声がAIによる代弁生成で問い直される", "代弁生成"),
    "正典": ("選集・部立・伝来による価値づけがコーパス選別と接続する", "コーパス選別"),
    "受容": ("後代の読解・流派化・引用が推薦環境と生成再話で変質する", "推薦生成"),
    "翻訳": ("漢文・和漢混淆・越境表現が機械翻訳で平準化されうる", "機械翻訳"),
    "真正性": ("史料性や実作性の根拠が合成記録と生成補完で揺らぐ", "合成記録"),
    "言語": ("古典語彙・歌語・文体の微差が文体生成で再配置される", "文体生成"),
}


def choose_tags(name: str, definition: str) -> list[tuple[str, str]]:
    text = f"{name} {definition}"
    picked: list[tuple[str, str]] = []
    for axis, status, needles in RULES:
        if any(needle in text for needle in needles):
            picked.append((axis, status))
        if len(picked) == 2:
            break
    if not picked:
        picked.append(("受容", "partial"))
    return picked


def main() -> None:
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT c.id, c.name_ja, c.definition
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 10 AND ftt.id IS NULL
        LIMIT 100
        """
    )
    concepts = cur.fetchall()

    rows = []
    for concept_id, name, definition in concepts:
        for axis, status in choose_tags(name or "", definition or ""):
            if axis not in AXES or status not in STATUS:
                raise ValueError((concept_id, axis, status))
            rationale, phenomenon = RATIONALES[axis]
            rows.append((concept_id, axis, status, rationale, phenomenon))

    before = conn.total_changes
    cur.executemany(
        """
        INSERT OR IGNORE INTO fourth_transform_tags
            (concept_id, axis, status, rationale, related_ai_phenomenon)
        VALUES (?, ?, ?, ?, ?)
        """,
        rows,
    )
    conn.commit()
    inserted = conn.total_changes - before
    conn.close()
    print(f"concepts={len(concepts)} rows={len(rows)} inserted={inserted}")


if __name__ == "__main__":
    main()
