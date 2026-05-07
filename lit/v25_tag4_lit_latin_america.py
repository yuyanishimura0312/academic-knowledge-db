import sqlite3

DB = "lit.sqlite"

R = {
    "canon": ("正典", "partial", "地域・国民文学の正典化がAI推薦で再配列され得る。", "AI推薦・教材生成"),
    "narr": ("物語", "rethinking", "多声性・断片化・記録性が生成AIの語りの組成と接続する。", "生成AIによる物語再構成"),
    "lang": ("言語", "rethinking", "口語・混淆語・詩的実験はAI翻訳や言語モデル化で再考される。", "機械翻訳・多言語LLM"),
    "auth": ("作者性", "partial", "証言・引用・編纂・自伝性がAI時代の作者境界を揺さぶる。", "AI共著・合成テキスト"),
    "subj": ("主体", "rethinking", "植民地・ジェンダー・人種・亡命の主体表象がAI分類で再編される。", "バイアス評価・表象生成"),
    "trans": ("翻訳", "partial", "多言語的流通と翻訳可能性がAI翻訳で変化する。", "ニューラル機械翻訳"),
    "real": ("真正性", "rethinking", "史実・証言・口承の真正性が合成生成物との比較で問われる。", "合成データ・真正性検証"),
    "cre": ("創造性", "rethinking", "形式実験やジャンル混淆が生成AIの創造性評価に関わる。", "生成AI・文体模倣"),
    "recv": ("受容", "partial", "国際的読まれ方や教材化がAI検索・推薦で変動する。", "AI検索・推薦"),
}

TAG_KEYS = {
    2519: ["canon", "subj"], 2521: ["canon", "recv"], 2523: ["lang", "narr"],
    2525: ["narr", "cre"], 2526: ["narr", "auth"], 2528: ["narr", "subj"],
    2529: ["narr", "lang"], 2530: ["real", "narr"], 2534: ["narr", "subj"],
    2535: ["lang", "cre"], 2536: ["lang", "narr"], 2537: ["lang", "cre"],
    2538: ["auth", "real"], 2540: ["lang", "recv"], 2541: ["real", "auth"],
    2542: ["canon", "recv"], 2543: ["narr", "real"], 2544: ["trans", "real"],
    2545: ["trans", "real"], 2546: ["lang", "trans"], 2547: ["narr", "subj"],
    2548: ["narr", "subj"], 2549: ["canon", "subj"], 3765: ["canon", "lang"],
    3766: ["narr", "real"], 3767: ["canon", "subj"], 3768: ["lang", "canon"],
    3769: ["subj", "canon"], 3770: ["auth", "canon"], 3771: ["lang", "recv"],
    3772: ["real", "subj"], 3773: ["auth", "recv"], 3774: ["auth", "narr"],
    3776: ["canon", "recv"], 3777: ["canon", "auth"], 3778: ["narr", "subj"],
    3782: ["canon", "narr"], 3783: ["subj", "real"], 3787: ["lang", "cre"],
    3790: ["lang", "auth"], 3791: ["narr", "subj"], 3793: ["narr", "auth"],
    3795: ["canon", "recv"], 3796: ["real", "narr"], 3799: ["auth", "narr"],
    3800: ["subj", "auth"], 3802: ["subj", "recv"], 3803: ["subj", "canon"],
    3804: ["narr", "canon"], 3805: ["subj", "narr"], 3812: ["recv", "canon"],
    3813: ["canon", "auth"], 3814: ["canon", "auth"], 3815: ["auth", "subj"],
    3816: ["lang", "canon"], 3817: ["canon", "auth"], 3818: ["subj", "canon"],
    3819: ["lang", "cre"], 3820: ["cre", "canon"], 4304: ["canon", "subj"],
    4305: ["subj", "canon"], 4306: ["canon", "recv"], 4307: ["subj", "recv"],
    4308: ["auth", "canon"], 4309: ["cre", "lang"], 4310: ["recv", "canon"],
    4314: ["lang", "canon"], 4316: ["lang", "cre"], 4317: ["canon", "recv"],
    4319: ["cre", "lang"], 4322: ["subj", "canon"], 4323: ["auth", "subj"],
    4325: ["canon", "recv"], 4326: ["lang", "canon"], 4328: ["lang", "canon"],
    4330: ["canon", "recv"], 4331: ["cre", "lang"], 4332: ["recv", "canon"],
    4333: ["cre", "lang"], 4336: ["recv", "canon"], 4337: ["lang", "cre"],
    4339: ["recv", "lang"], 4340: ["auth", "real"], 4343: ["lang", "canon"],
    4344: ["canon", "auth"], 4345: ["trans", "lang"], 4346: ["narr", "cre"],
    4349: ["real", "narr"], 4351: ["trans", "subj"], 4353: ["trans", "subj"],
    4354: ["real", "subj"], 4355: ["narr", "subj"], 4356: ["real", "subj"],
    4358: ["narr", "cre"], 4359: ["subj", "narr"], 4361: ["subj", "narr"],
    5289: ["canon", "subj"], 5290: ["canon", "recv"], 5291: ["subj", "recv"],
    5292: ["canon", "lang"],
}

rows = []
for concept_id, keys in TAG_KEYS.items():
    for key in keys:
        axis, status, rationale, phenomenon = R[key]
        rows.append((concept_id, axis, status, rationale, phenomenon))

with sqlite3.connect(DB) as conn:
    remaining = conn.execute(
        """
        SELECT c.id, c.name_ja, COALESCE(c.definition, '')
        FROM concepts c
        LEFT JOIN fourth_transform_tags ftt ON ftt.concept_id = c.id
        WHERE c.subfield_id = 16 AND ftt.id IS NULL
        GROUP BY c.id
        """
    ).fetchall()
    for concept_id, name, definition in remaining:
        text = f"{name} {definition}"
        keys = []
        if any(w in text for w in ("語", "詩", "口承", "二言語", "対訳", "方言", "口語", "翻訳")):
            keys.append("lang")
        if any(w in text for w in ("自伝", "日記", "証言", "記録", "報告", "編纂", "年代記", "エッセイ")):
            keys.append("auth")
        if any(w in text for w in ("歴史", "史実", "事件", "処刑", "征服", "革命", "軍政", "独裁", "失踪")):
            keys.append("real")
        if any(w in text for w in ("女性", "奴隷", "先住", "亡命", "混血", "ジェンダー", "人種", "植民地")):
            keys.append("subj")
        if any(w in text for w in ("多声", "断片", "視点", "小説", "物語", "短篇", "長編", "中編")):
            keys.append("narr")
        if any(w in text for w in ("前衛", "実験", "新造語", "パロディ", "シュルレアリスム", "幻想", "モデルニズモ")):
            keys.append("cre")
        if not keys:
            keys = ["canon", "recv"]
        elif len(keys) == 1:
            keys.append("recv" if keys[0] != "recv" else "canon")
        for key in keys[:2]:
            axis, status, rationale, phenomenon = R[key]
            rows.append((concept_id, axis, status, rationale, phenomenon))

    conn.executemany(
        """
        INSERT OR IGNORE INTO fourth_transform_tags
            (concept_id, axis, status, rationale, related_ai_phenomenon)
        VALUES (?, ?, ?, ?, ?)
        """,
        rows,
    )
    conn.commit()

print(f"inserted_or_existing={len(rows)}")
