#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("lit.sqlite")

AXES = {
    "作者性", "創造性", "物語", "主体", "正典", "受容", "翻訳", "真正性", "言語"
}

RULES = [
    ("言語", "partial", ("言語", "文体", "韻", "ナンセンス", "俗語", "語り", "名前", "コード", "記号", "翻訳不能")),
    ("翻訳", "partial", ("翻訳", "世界", "国際", "比較", "欧米", "日本", "英米", "フランス", "亡命")),
    ("作者性", "rethinking", ("自伝", "著者", "作者", "作家", "共著", "ゴーストライター", "シンジケート", "筆名", "脚本", "作画")),
    ("創造性", "rethinking", ("技法", "様式", "形式", "造本", "コラージュ", "グリッド", "メディア", "実験", "融合", "発明", "独自")),
    ("主体", "rethinking", ("主人公", "少年", "少女", "探偵", "刑事", "女性", "子供", "青年", "反英雄", "怪物", "ロボット")),
    ("真正性", "partial", ("リアリズム", "歴史", "記録", "証言", "体験", "ホロコースト", "階級", "植民", "私小説", "メモワール")),
    ("受容", "partial", ("読者", "市場", "ファン", "共同体", "ジャンル", "大衆", "制度", "学術", "文化", "運動")),
    ("正典", "invariant", ("古典", "規範", "正典", "起源", "祖型", "代表作", "確立", "黄金時代", "シリーズ", "連作")),
    ("物語", "partial", ("物語", "小説", "長篇", "短篇", "寓話", "神話", "ミステリ", "SF", "ファンタジー", "ホラー", "ロマンス")),
]

RATIONALES = {
    "作者性": "生成AIとの共作や名義管理により、作者の責任と帰属が再考される。",
    "創造性": "生成AIが様式模倣や形式生成を行うため、創造性の所在が再検討される。",
    "物語": "AIによる筋生成やジャンル混成で、物語形式の安定性が部分的に変わる。",
    "主体": "AIキャラクターや合成語り手により、主体表象の条件が再考される。",
    "正典": "正典化された作品・ジャンルは参照基準として残るが、再編の対象にもなる。",
    "受容": "推薦・ファン生成・読書ログ解析により、受容共同体が部分的に変容する。",
    "翻訳": "機械翻訳と多言語生成により、越境流通と翻訳の役割が再検討される。",
    "真正性": "合成テキスト時代に、体験・記録・証言の真正性が問われる。",
    "言語": "LLMが文体・語彙・韻律を生成するため、言語的特徴の評価が変わる。",
}

PHENOMENA = {
    "作者性": "AI共著・著者帰属",
    "創造性": "様式模倣・生成AI創作",
    "物語": "プロット生成・ジャンル混成",
    "主体": "AIキャラクター・合成語り手",
    "正典": "学習データ化・正典再編",
    "受容": "推薦アルゴリズム・ファン生成",
    "翻訳": "機械翻訳・多言語生成",
    "真正性": "合成テキスト検出・出典確認",
    "言語": "文体変換・LLM言語生成",
}

PREFERRED = {
    "童話": ["物語", "正典"], "絵本": ["創造性", "受容"], "児童": ["主体", "受容"],
    "YA": ["主体", "受容"], "ミステリ": ["物語", "正典"], "探偵": ["主体", "物語"],
    "ノワール": ["物語", "真正性"], "SF": ["物語", "創造性"], "ファンタジー": ["物語", "創造性"],
    "ホラー": ["物語", "受容"], "ロマンス": ["受容", "物語"], "マンガ": ["創造性", "受容"],
    "コミック": ["創造性", "受容"], "グラフィック": ["創造性", "作者性"], "自伝": ["作者性", "真正性"],
    "理論": ["受容", "言語"], "正典": ["正典", "受容"], "翻訳": ["翻訳", "言語"],
}


def choose_axes(name: str, definition: str) -> list[str]:
    text = f"{name} {definition}"
    scores = {axis: 0 for axis in AXES}
    for key, axes in PREFERRED.items():
        if key in text:
            for axis in axes:
                scores[axis] += 6
    for axis, _status, words in RULES:
        scores[axis] += sum(1 for word in words if word in text)
    ranked = [axis for axis, score in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])) if score > 0]
    if not ranked:
        ranked = ["物語", "受容"]
    if len(ranked) == 1:
        ranked.append("正典" if ranked[0] != "正典" else "受容")
    return ranked[:2]


def status_for(axis: str) -> str:
    for rule_axis, status, _words in RULES:
        if rule_axis == axis:
            return status
    return "partial"


def main() -> None:
    con = sqlite3.connect(DB)
    rows = con.execute(
        """
        SELECT c.id, c.name_ja, COALESCE(c.definition, '')
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 21 AND ftt.id IS NULL
        ORDER BY c.id
        """
    ).fetchall()

    inserts = []
    for concept_id, name, definition in rows:
        for axis in choose_axes(name or "", definition or ""):
            inserts.append((concept_id, axis, status_for(axis), RATIONALES[axis], PHENOMENA[axis]))

    con.executemany(
        """
        INSERT OR IGNORE INTO fourth_transform_tags
            (concept_id, axis, status, rationale, related_ai_phenomenon)
        VALUES (?, ?, ?, ?, ?)
        """,
        inserts,
    )
    con.commit()
    print(f"concepts={len(rows)} inserted={con.total_changes}")
    con.close()


if __name__ == "__main__":
    main()
