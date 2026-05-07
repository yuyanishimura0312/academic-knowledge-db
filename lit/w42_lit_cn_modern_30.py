from lit_db_helper import LitDB


CLUSTERS = {
    "晩清・民初小刊": [
        ("『月月小説』科学滑稽欄", "晩清小誌で科学語を笑話化した短文欄。", 55),
        ("『時報』図画副刊小説", "図像欄に添えた都市小説的キャプション群。", 55),
        ("『大共和日報』文芸小品", "共和初期の日刊紙に載る短い政治小品。", 55),
        ("『女子世界』閨秀小説欄", "女性投稿者の家庭・学堂小説を集めた欄。", 55),
        ("『神州日報』滑稽余談", "時事諷刺を笑話と短篇で処理した余談欄。", 55),
        ("『民呼日報』白話筆記", "白話運動前夜の短い社会観察筆記。", 55),
    ],
    "上海都市微ジャンル": [
        ("新舞台劇評小説化", "劇評文が筋書き小説へ接近する上海文体。", 25),
        ("月份牌広告叙事", "広告画の女性像を短篇的物語へ読む叙事型。", 25),
        ("跑馬庁観覧散文", "競馬場観覧を都市感覚で描く小散文。", 25),
        ("弄堂口伝聞小説", "路地口の噂を断片連鎖で組む上海小説。", 25),
        ("電車車廂速写", "市電車内の身振りを素描する都市短文。", 25),
        ("映画本事翻案短篇", "映画梗概を通俗短篇へ改作する翻案形式。", 25),
    ],
    "抗戦辺地メディア": [
        ("桂林壁報詩", "桂林疎開地の壁新聞に貼られた短詩群。", 25),
        ("昆明茶館朗誦稿", "茶館朗読用に作られた抗戦詩・散文稿。", 25),
        ("重慶防空洞日記文", "空襲避難壕の体験を日記体で綴る散文。", 25),
        ("晋察冀木刻連環詩", "木刻連環画に短詩を添えた宣伝形式。", 25),
        ("延安秧歌劇台本端本", "秧歌劇の短い上演端本として残る脚本。", 26),
        ("西南聯大校刊小品", "西南聯大学生刊行物の随筆・小説小品。", 25),
    ],
    "毛沢東期非公式流通": [
        ("右派労改詩手抄本", "労改経験を私的筆写で残した詩稿群。", 26),
        ("北大荒知青油印詩", "北大荒知青が油印で回覧した抒情詩。", 26),
        ("工宣隊批判劇小本", "工宣隊活動で使われた短い批判劇冊子。", 26),
        ("内参小説抄読圏", "内部資料小説を限られた読者が抄読した圏。", 26),
        ("農場壁新聞連載小説", "国営農場の壁新聞に連載された短篇叙事。", 26),
        ("革委会快板詞文学", "革委会宣伝の快板詞を文学資料化したもの。", 26),
    ],
    "改革開放以後の微実践": [
        ("『星星』民刊詩附録", "地方民刊に挟まれた詩人同人の附録冊子。", 27),
        ("海南房地産小説", "海南開発熱を投機風俗として描く小説群。", 27),
        ("深圳打工妹手記", "出稼ぎ女性労働者の手記風散文。", 27),
        ("BBS接龍小説", "掲示板参加者が継ぎ足す連鎖小説形式。", 12),
        ("豆瓣日記体微小説", "豆瓣日記欄で流通した短い私小説風叙事。", 12),
        ("晋江榜単文案美学", "晋江ランキング文案に特有の惹句様式。", 12),
    ],
}


def main() -> None:
    rows = [
        {"name_ja": name, "definition": definition, "period_id": period_id}
        for concepts in CLUSTERS.values()
        for name, definition, period_id in concepts
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
                period_id=row["period_id"],
                definition=row["definition"],
                importance_score=1,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )

    print("inserted 30 lit_cn_modern concepts")


if __name__ == "__main__":
    main()
