from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_theory", region="理論", period_id=None)

CONCEPTS = [
    # 1. 微小ナラトロジー
    dict(**C, name_ja="ゼロ焦点化の揺戻し論",
         name_en="Zero focalization recoil theory",
         definition="全知語りが局所視点へ急縮する瞬間を読む微視物語論。"),
    dict(**C, name_ja="被物語者の沈黙応答論",
         name_en="Silent narratee response theory",
         definition="語りかけに返答しない被物語者を構造的欠落として読む。"),
    dict(**C, name_ja="遡及的プロレプシス密度論",
         name_en="Retrospective prolepsis density theory",
         definition="未来予告が後景から過去解釈を圧縮する度合いの分析。"),
    dict(**C, name_ja="場面境界の半句またぎ論",
         name_en="Hemistich scene-boundary enjambment",
         definition="半句単位の場面転換を叙述速度の微差として測る。"),
    dict(**C, name_ja="群像語りの代名詞漂流論",
         name_en="Pronoun drift in collective narration",
         definition="一人称複数の指示対象が滑る箇所を共同体語りで読む。"),
    dict(**C, name_ja="反復エピソードの薄差異論",
         name_en="Thin difference in repeated episodes",
         definition="反復場面の微細な差を物語進行の指標とみる方法。"),

    # 2. パラテクスト細部論
    dict(**C, name_ja="献辞の逆読者設定論",
         name_en="Counter-dedicatory reader theory",
         definition="献辞が実読者でなく拒まれた読者を作る機能を読む。"),
    dict(**C, name_ja="章題の遅延要約論",
         name_en="Delayed-summary chapter title theory",
         definition="章題が読後にだけ要約として働く逆行的効果を扱う。"),
    dict(**C, name_ja="索引項目の隠れ序列論",
         name_en="Hidden hierarchy of index entries",
         definition="索引の語順と細分化に潜む批評的順位づけを読む。"),
    dict(**C, name_ja="扉ページ余白の権威化論",
         name_en="Title-page whitespace authorization",
         definition="扉余白が著者名や題名の権威を演出する仕組み。"),
    dict(**C, name_ja="脚注番号の期待攪乱論",
         name_en="Footnote-number expectation disruption",
         definition="注番号の密度と欠番が読解リズムを乱す効果の分析。"),
    dict(**C, name_ja="奥付日付の読書時制論",
         name_en="Colophon date reading tense theory",
         definition="奥付の日付が作品時間と読書時間を接続する作用を読む。"),

    # 3. 翻訳批評の微技法
    dict(**C, name_ja="未訳語の局所異化論",
         name_en="Local foreignization by untranslated words",
         definition="訳文内の未訳語が一時的異化を作る箇所を読む。"),
    dict(**C, name_ja="訳注過剰の権威委譲論",
         name_en="Overannotation authority transfer",
         definition="過剰な訳注が本文の判断権を注へ移す現象を扱う。"),
    dict(**C, name_ja="固有名再音写の距離論",
         name_en="Retransliteration distance theory",
         definition="固有名の再音写が文化的距離を再設定する効果の分析。"),
    dict(**C, name_ja="韻律補償の局所損失論",
         name_en="Local loss in metrical compensation",
         definition="別箇所の韻律補償が近接行の意味損失を生む問題。"),
    dict(**C, name_ja="翻訳序文の責任分散論",
         name_en="Translator-preface responsibility dispersal",
         definition="訳者序文が誤読責任を作者・読者へ分散する働き。"),
    dict(**C, name_ja="二重訳語の揺れ幅管理論",
         name_en="Doublet term variance management",
         definition="同一語に二訳語を配し概念の揺れを管理する技法。"),

    # 4. 物質的テクスト微視論
    dict(**C, name_ja="紙質変化の章境界論",
         name_en="Paper-shift chapter boundary theory",
         definition="紙質の変化を章や挿入部の境界標識として読む。"),
    dict(**C, name_ja="活字摩耗の版差読解論",
         name_en="Type-wear edition-variant reading",
         definition="活字摩耗から刷次差と読者流通を推定する書誌論。"),
    dict(**C, name_ja="裁断余白の欠落証拠論",
         name_en="Trimmed-margin evidence theory",
         definition="裁断で失われた余白を注記欠落の証拠として扱う。"),
    dict(**C, name_ja="貼紙訂正の時間層論",
         name_en="Pasted-correction temporal layering",
         definition="貼紙訂正を刊行後介入の時間層として読む方法。"),
    dict(**C, name_ja="インク濃淡の筆写順序論",
         name_en="Ink-density copying order theory",
         definition="インク濃淡から筆写順序や中断を推定する写本分析。"),
    dict(**C, name_ja="折丁署名の迷路読解論",
         name_en="Signature-mark labyrinth reading",
         definition="折丁署名のずれを製本過程と読書順序の手掛かりにする。"),

    # 5. 読者・情動の局所論
    dict(**C, name_ja="退屈箇所の注意配分論",
         name_en="Attention allocation in boring passages",
         definition="退屈な箇所で読者注意が逸れる方向を批評対象にする。"),
    dict(**C, name_ja="羞恥の二次読解論",
         name_en="Secondary reading of shame",
         definition="登場人物の羞恥でなく読者の羞恥反応を読む方法。"),
    dict(**C, name_ja="誤読の保存価値論",
         name_en="Preservational value of misreading",
         definition="訂正不能な誤読を読書共同体の記録として評価する。"),
    dict(**C, name_ja="読書中断の感情句読論",
         name_en="Affective punctuation of reading pauses",
         definition="中断箇所を読者感情の句読点として分析する理論。"),
    dict(**C, name_ja="共感疲労の人物配置論",
         name_en="Character arrangement of empathy fatigue",
         definition="人物の連続苦難が共感疲労を生む配置を読む。"),
    dict(**C, name_ja="再読時の期待残響論",
         name_en="Expectation echo in rereading",
         definition="初読の期待が再読時にも残る残響効果を扱う読者論。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=22"
        ).fetchone()[0]
        inserted = 0
        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
            existing = db.find_concept(
                concept["name_ja"], concept["region"], concept["period_id"]
            )
            db.insert_concept(
                **concept,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="minor",
            )
            if existing is None:
                inserted += 1
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=22"
        ).fetchone()[0]
        print(f"inserted={inserted} before={before} after={after}")


if __name__ == "__main__":
    main()
