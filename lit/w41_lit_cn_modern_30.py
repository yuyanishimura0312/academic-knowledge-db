from lit_db_helper import LitDB


CLUSTERS = {
    "晩清・民初小誌": [
        ("『遊戯雑誌』礼拝六余波", "民初娯楽小誌に残る短篇・笑話混成の余脈。"),
        ("『半月』南社小品欄", "南社系文人の旧体詩と小品文が交錯した欄。"),
        ("『越鐸日報』文芸副刊", "浙江地方紙で新旧文学が併存した副刊面。"),
        ("『民権素』女性投書欄", "民初女性読者の投書・短文が集まった小欄。"),
        ("『小說大觀』短札体", "短い書簡形式で都市風聞を連ねる民初小説様式。"),
        ("『紅雑誌』海上艶情欄", "上海小誌の恋愛逸話・劇評混成欄。"),
    ],
    "地域・方言微伝統": [
        ("無錫滑稽小説", "無錫方言の掛け合いで商家生活を諷刺する小説群。"),
        ("潮汕僑批叙事", "僑批書簡を素材に移民家族を描く潮汕系叙事。"),
        ("桂林抗戦木刻詩", "桂林疎開期の木刻版画と短詩の結合形式。"),
        ("青島徳租界散文", "青島租界の街路感覚を描く短い都市散文。"),
        ("滇西抗戦辺地小説", "雲南西部戦線の補給路と少数民族村落を描く小説。"),
        ("川東茶館評書体小説", "茶館語りの節回しを小説文体へ移した川東叙事。"),
    ],
    "少数民族・辺境近代": [
        ("達斡爾漢語新詩", "達斡爾族知識人による漢語自由詩の小系譜。"),
        ("赫哲族漁歌改写文学", "赫哲族漁歌を現代散文・児童文学へ改写した実践。"),
        ("撒拉族漢語回想録", "撒拉族生活を漢語で記した回想録的散文群。"),
        ("佤族口承転写小説", "佤族口承譚を漢語小説へ移した辺境叙事。"),
        ("東郷族女性散文", "東郷族女性の婚姻・教育経験を綴る漢語散文。"),
        ("鄂温克狩猟叙事改編", "鄂温克狩猟口承を現代物語に再編した作品群。"),
    ],
    "地下・手稿・流通": [
        ("油印詩刊『啓明星』", "油印で回覧された地方青年詩刊。"),
        ("北京知青手抄劇本", "知青集団内で筆写共有された短い劇本。"),
        ("蘭州地下抒情詩稿", "蘭州青年詩人の私的回覧詩稿群。"),
        ("工廠黒板詩", "工場黒板に掲示され短期で消えた労働詩。"),
        ("民間評書手抄本小説", "評書語りを筆録し貸本化した手抄小説。"),
        ("知青日記小説化", "知青日記を後年小説へ再構成する叙述型。"),
    ],
    "形式・理論微論争": [
        ("新詩標点論争", "新詩で句読点の有無が韻律を変えるかの小論争。"),
        ("報告文学細節真偽論", "報告文学の細部虚構化をめぐる真偽論争。"),
        ("方言詞注釈過多問題", "方言小説で注釈が読書を妨げるかの編集論点。"),
        ("小説結尾空白論", "開放的結末の余白をめぐる先鋒小説批評語。"),
        ("朦朧詩主語隠去論", "朦朧詩の一人称省略を政治的身振りと読む議論。"),
        ("網文断更倫理", "連載停止が読者契約を破るかをめぐる網文内論争。"),
    ],
}


def main() -> None:
    rows = [
        {"name_ja": name, "definition": definition}
        for concepts in CLUSTERS.values()
        for name, definition in concepts
    ]
    if len(rows) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(rows)}")
    too_long = [r["name_ja"] for r in rows if len(r["definition"]) > 100]
    if too_long:
        raise SystemExit(f"definitions too long: {too_long}")

    with LitDB("lit.sqlite") as db:
        existing = {
            r["name_ja"]
            for r in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 9"
            )
        }
        duplicates = [r["name_ja"] for r in rows if r["name_ja"] in existing]
        if duplicates:
            raise SystemExit(f"already present: {duplicates}")

        for row in rows:
            db.insert_concept(
                name_ja=row["name_ja"],
                subfield_code="lit_cn_modern",
                region="東アジア",
                period_id=None,
                definition=row["definition"],
                importance_score=1,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )

    print("inserted 30 lit_cn_modern concepts")


if __name__ == "__main__":
    main()
