from lit_db_helper import LitDB


CLUSTERS = {
    "晩清・五四小メディア": [
        ("『申報』自由談短評小説", "時評欄の短評が小説的断片へ転じた欄文体。", 55),
        ("『小説時報』旅行小品欄", "旅行記を短い都市観察小品として載せた欄。", 55),
        ("『礼拝六』偵探翻案欄", "探偵翻訳を上海通俗短篇へ改作した欄。", 55),
        ("『婦女雑誌』問題小説欄", "婚姻・教育問題を短篇で論じた女性誌欄。", 24),
        ("『新青年』通信欄白話実験", "読者通信で試された初期白話散文の場。", 24),
        ("『每周評論』随感録小品", "政治随感を掌篇散文へ圧縮した五四欄。", 24),
    ],
    "上海モダン都市文体": [
        ("亭子間作家群小説", "上海屋根裏生活を貧窮知識人視点で描く小説。", 25),
        ("小報続書連載小説", "小報で人気作の続篇を継ぎ足した連載形式。", 25),
        ("新感覚派電影院叙事", "映画館の視覚刺激で都市感覚を組む叙事。", 25),
        ("『良友』画報写真小説", "写真ページに短い恋愛・都市物語を添えた形式。", 25),
        ("舞女生活速写小説", "上海舞女の日常を速写風に描く都市小説。", 25),
        ("左聯街頭詩伝単", "左聯系詩を街頭配布物として流通させた形式。", 25),
    ],
    "戦時・孤島・根拠地": [
        ("上海孤島副刊小説", "租界孤島期の副刊に載った抗戦暗喩小説。", 25),
        ("重慶霧季小品文", "霧の陪都生活を短い随筆で描く戦時文体。", 25),
        ("香港抗戦通俗劇本", "香港舞台で上演された抗日通俗劇の台本。", 25),
        ("延安牆報叙事詩", "牆報に貼られた短い英雄叙事詩。", 26),
        ("晋察冀通訊報告文学", "根拠地通信を報告文学へ整えた文体。", 25),
        ("皖南事変追悼詩抄", "皖南事変犠牲者を悼む手写・油印詩群。", 25),
    ],
    "毛沢東期非正規文芸": [
        ("批林批孔寓言詩", "政治批判を寓言詩の形式で処理した文革詩。", 26),
        ("樣板戲唱詞改写本", "様板戯唱詞を職場宣伝用に改作した小冊子。", 26),
        ("知青農場家書小説", "知青の家書を小説的連作に仕立てた文章群。", 26),
        ("地下恋愛手抄本小説", "私的筆写で回覧された恋愛叙事の手抄本。", 26),
        ("紅衛兵詩詞伝単", "紅衛兵組織が配った詩詞形式の宣伝紙。", 26),
        ("文革口号詩章法", "口号反復を詩行構成へ転用した文革文体。", 26),
    ],
    "改革以後・デジタル細分": [
        ("大案紀実文学叙事", "重大事件報道を長篇紀実文学に組む叙事。", 27),
        ("単位解体小説", "国有単位の崩れを日常倫理から描く小説群。", 12),
        ("下崗女工口述文学", "下崗女性労働者の語りを編集した文学形式。", 12),
        ("博客連載官場小説", "ブログで章回的に発表された官場風刺小説。", 12),
        ("微信公衆号非虚構", "公衆号で流通する調査報道風の非虚構文。", 12),
        ("網文打賞章末話", "打賞を促す章末作者語りの網文慣行。", 12),
    ],
}


def main() -> None:
    rows = [
        {"name_ja": name, "definition": definition, "period_id": period_id}
        for concepts in CLUSTERS.values()
        for name, definition, period_id in concepts
    ]
    if len(CLUSTERS) != 5 or any(len(v) != 6 for v in CLUSTERS.values()):
        raise SystemExit("expected 5 clusters x 6 concepts")
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
                period_id=row["period_id"],
                definition=row["definition"],
                importance_score=1,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )

    print("inserted 30 lit_cn_modern concepts")


if __name__ == "__main__":
    main()
