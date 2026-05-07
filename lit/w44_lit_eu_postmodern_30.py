#!/usr/bin/env python3
"""Wave 44: add 30 ultra-niche concepts to lit_eu_postmodern."""

from lit_db_helper import LitDB


SUBFIELD = "lit_eu_postmodern"
REGION = "西欧"


CONCEPTS = [
    # Cluster 1: paratextual machinery
    {"name_ja": "ブックマーク跡叙述", "name_en": "bookmark trace narration", "name_original": "bookmark trace narration", "definition": "挟み跡や栞位置を読解順序の証拠にする叙述", "period": "ポストモダン期"},
    {"name_ja": "重版帯コピー小説", "name_en": "reprint obi-copy fiction", "name_original": "reprint blurb fiction", "definition": "帯文や販促文句が筋と評価を侵食する小説形式", "period": "ポストモダン期"},
    {"name_ja": "貸出票プロット", "name_en": "borrowing-slip plot", "name_original": "borrowing-slip plot", "definition": "図書館貸出票の履歴から失われた読者を復元する筋", "period": "ポストモダン期"},
    {"name_ja": "折込図版錯誤", "name_en": "foldout-plate error", "name_original": "foldout-plate error", "definition": "誤配置された折込図版が語りの時系列をずらす装置", "period": "ポストモダン期"},
    {"name_ja": "読者カード返信小説", "name_en": "reader-card reply fiction", "name_original": "reader-card reply fiction", "definition": "読者カードや返信欄を作中対話へ変える小説", "period": "ポストモダン期"},
    {"name_ja": "製本ミス時間論", "name_en": "binding-error temporality", "name_original": "binding-error temporality", "definition": "乱丁や落丁を偶然でなく時間構造として読む概念", "period": "ポストモダン期"},
    # Cluster 2: archive microforms
    {"name_ja": "マイクロフィルム亡霊", "name_en": "microfilm ghosting", "name_original": "microfilm ghosting", "definition": "縮写資料の滲みや重影を記憶の幽霊化に使う技法", "period": "ポストモダン期"},
    {"name_ja": "閲覧制限メタ小説", "name_en": "restricted-access metafiction", "name_original": "restricted-access metafiction", "definition": "閲覧不可の文書を中心に知の欠落を語る小説", "period": "ポストモダン期"},
    {"name_ja": "保存温度叙述", "name_en": "storage-temperature narration", "name_original": "storage-temperature narration", "definition": "保存条件の記録を感情や証言の冷却比喩へ変える叙述", "period": "自伝的現代期"},
    {"name_ja": "褪色インク証言", "name_en": "faded-ink testimony", "name_original": "faded-ink testimony", "definition": "薄れた筆跡を証言の強度と不確かさに結びつける方法", "period": "自伝的現代期"},
    {"name_ja": "箱番号迷宮", "name_en": "box-number labyrinth", "name_original": "box-number labyrinth", "definition": "保存箱番号の連鎖で探索の迷宮性を作る構成", "period": "ポストモダン期"},
    {"name_ja": "閲覧机私小説", "name_en": "reading-desk autofiction", "name_original": "reading-desk autofiction", "definition": "閲覧室の机上作業だけで自己史を組み立てる私小説", "period": "自伝的現代期"},
    # Cluster 3: translation residue
    {"name_ja": "訳者保留符号", "name_en": "translator's hold mark", "name_original": "translator's hold mark", "definition": "未決訳語の印が語りの躊躇として残る翻訳小説技法", "period": "ポストモダン期"},
    {"name_ja": "二重訳者前書き", "name_en": "double translator preface", "name_original": "double translator preface", "definition": "架空訳者と実在訳者の前書きが権威を食い合う装置", "period": "ポストモダン期"},
    {"name_ja": "訳抜けプロット", "name_en": "omitted-translation plot", "name_original": "omitted-translation plot", "definition": "訳出されない語句が事件や記憶の鍵になる構成", "period": "ポストモダン期"},
    {"name_ja": "逆輸入原文小説", "name_en": "reimported-original fiction", "name_original": "reimported-original fiction", "definition": "翻訳から失われた原文を後から捏造する小説形式", "period": "ポストモダン期"},
    {"name_ja": "機械訳誤読叙述", "name_en": "machine-translation misreading", "name_original": "machine-translation misreading", "definition": "機械訳の誤りを人物理解や筋のずれに転用する叙述", "period": "ポスト・ポストモダン期"},
    {"name_ja": "字幕同期ずれ詩学", "name_en": "subtitle lag poetics", "name_original": "subtitle lag poetics", "definition": "字幕の遅延や先行を多言語的時間差として扱う詩学", "period": "ポスト・ポストモダン期"},
    # Cluster 4: platform traces
    {"name_ja": "編集履歴自伝", "name_en": "revision-history autobiography", "name_original": "revision-history autobiography", "definition": "編集履歴の差分から自己像を組み立てる自伝形式", "period": "ポスト・ポストモダン期"},
    {"name_ja": "共有権限プロット", "name_en": "sharing-permission plot", "name_original": "sharing-permission plot", "definition": "閲覧権限の付与や剥奪が関係性を動かす筋", "period": "ポスト・ポストモダン期"},
    {"name_ja": "タイムスタンプ合唱", "name_en": "timestamp chorus", "name_original": "timestamp chorus", "definition": "複数の時刻印が声の重なりを作るデジタル多声法", "period": "ポスト・ポストモダン期"},
    {"name_ja": "共同編集幽霊", "name_en": "collaborative-editing ghost", "name_original": "collaborative-editing ghost", "definition": "共同編集画面の匿名カーソルを幽霊的存在にする技法", "period": "ポスト・ポストモダン期"},
    {"name_ja": "既読取消叙述", "name_en": "unread-reversal narration", "name_original": "unread-reversal narration", "definition": "既読表示の取消不能性を後悔や責任の記号にする叙述", "period": "ポスト・ポストモダン期"},
    {"name_ja": "通知設定人物造形", "name_en": "notification-setting characterization", "name_original": "notification-setting characterization", "definition": "通知の許可や沈黙設定で人物関係を示す造形法", "period": "ポスト・ポストモダン期"},
    # Cluster 5: institutional forms
    {"name_ja": "倫理審査小説", "name_en": "ethics-review fiction", "name_original": "ethics-review fiction", "definition": "倫理審査書類の語彙で調査と語りの権力を問う小説", "period": "ポスト・ポストモダン期"},
    {"name_ja": "同意書メタ物語", "name_en": "consent-form metanarrative", "name_original": "consent-form metanarrative", "definition": "同意書の署名や拒否を語りへの参加条件にする装置", "period": "ポスト・ポストモダン期"},
    {"name_ja": "匿名化黒塗り文体", "name_en": "anonymized-redaction style", "name_original": "anonymized-redaction style", "definition": "匿名化の黒塗りが人物像と責任の空白を作る文体", "period": "ポスト・ポストモダン期"},
    {"name_ja": "研究助成報告小説", "name_en": "grant-report fiction", "name_original": "grant-report fiction", "definition": "助成報告書の成果語彙で創作の失敗を語る小説", "period": "ポスト・ポストモダン期"},
    {"name_ja": "データ管理計画叙述", "name_en": "data-management-plan narration", "name_original": "data-management-plan narration", "definition": "データ保存計画を記憶と忘却の設計図にする叙述", "period": "ポスト・ポストモダン期"},
    {"name_ja": "査読コメント劇", "name_en": "peer-review comment drama", "name_original": "peer-review comment drama", "definition": "査読コメントの応酬だけで作品の欠落を浮かべる劇形式", "period": "ポスト・ポストモダン期"},
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB() as db:
        periods = {
            "ポストモダン期": db.get_or_create_period("ポストモダン期", REGION, 1960, 2000),
            "自伝的現代期": db.get_or_create_period("自伝的現代期", REGION, 1990, 2025),
            "ポスト・ポストモダン期": db.get_or_create_period("ポスト・ポストモダン期", REGION, 2000, 2025),
        }
        for entry in CONCEPTS:
            if len(entry["definition"]) > 100:
                raise ValueError(f"definition too long: {entry['name_ja']}")
            concept = dict(entry)
            period_id = periods[concept.pop("period")]
            existed = db.find_concept(concept["name_ja"], REGION, period_id) is not None
            db.insert_concept(
                **concept,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 0 if existed else 1
            skipped += 1 if existed else 0
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
