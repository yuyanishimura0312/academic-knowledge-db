#!/usr/bin/env python3
"""Wave 38: add 30 extra niche concepts to lit_russia_slavic."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

P_ROM = 201
P_REAL = 202
P_SILVER = 203
P_FORM = 204
P_BAKH = 205
P_SOV_MID = 206
P_SOV_LATE = 207
P_POST = 208
P_CZECH = 209
P_POLISH = 210
P_SOUTH = 211
P_GOLDEN = 291

CONCEPTS = [
    # Cluster 1: medieval and early Russian textuality
    ("イラリオン『律法と恩寵の言葉』", "Sermon on Law and Grace", None, "キエフ・ルーシの改宗史を救済史へ組み込む11世紀説教文学。"),
    ("ザドンシチナ写本伝承", "Zadonshchina manuscript tradition", None, "クリコヴォ戦勝を『イーゴリ遠征物語』風に語る軍記的写本群。"),
    ("『酔いどれ物語』転落寓話", "Tale of Woe-Misfortune", None, "放蕩青年の貧困化を擬人化された災厄が追う17世紀世俗物語。"),
    ("アヴァクーム自伝の古儀式派語り", "Avvakum Old Believer narration", None, "殉教体験を口語と聖書語で混ぜる古儀式派自伝の語り口。"),
    ("ドモストロイ家政規範", "Domostroi household code", None, "家父長制・信仰・家政を一体化するモスクワ国家期の訓戒文献。"),
    ("スコモローフ歌謡の禁圧記憶", "Skomorokh song repression", None, "道化芸能の歌と語りが教会禁圧後も民衆文学に残した痕跡。"),

    # Cluster 2: nineteenth-century subcurrents
    ("ラズノチーネツ語り", "Raznochinets narration", P_REAL, "身分混成知識人の不安定な自己形成を映す19世紀散文の語り型。"),
    ("ポチヴェンニチェストヴォ批評", "Pochvennichestvo criticism", P_REAL, "民衆の土壌への回帰を説き西欧化と急進主義を批判した思想文芸潮流。"),
    ("シベリア・オブラストニキ散文", "Siberian oblastniki prose", P_REAL, "辺境の自治意識と流刑地経験を結びつける19世紀シベリア地域主義文学。"),
    ("ネクラーソフ派市民詩", "Nekrasov civic verse school", P_REAL, "韻律の粗さと社会告発を武器にしたネクラーソフ周辺の市民詩系譜。"),
    ("メルニコフ＝ペチェルスキー旧教徒小説", "Melnikov-Pechersky Old Believer novels", P_REAL, "ヴォルガ旧教徒共同体を民俗誌的厚みで描く長編小説群。"),
    ("アポロン誌のネオ古典主義", "Apollon neoclassicism", P_SILVER, "象徴主義後期に明晰な形と古典的節度を掲げた雑誌『アポロン』の詩学。"),

    # Cluster 3: formalist and avant-garde micrologies
    ("トィニャーノフ『文学的事実』", "Tynianov literary fact", P_FORM, "作品・ジャンル・制度が歴史状況で文学になる条件を問うフォルマリズム概念。"),
    ("エイヘンバウム『文学的生活』", "Eikhenbaum literary life", P_FORM, "作家の生活制度と市場を文学史分析へ組み込む後期フォルマリズム概念。"),
    ("レフ誌のファクトグラフィア", "LEF factography", P_FORM, "記録・報告・写真を芸術制作へ転用する左翼前衛の反虚構プログラム。"),
    ("セラピオン兄弟の非党派性", "Serapion Brothers nonpartisanship", P_SOV_MID, "革命後文学に政治党派からの相対的自律を求めた若手作家集団の姿勢。"),
    ("オベリウ詩の不条理ミニアチュール", "OBERIU absurd miniature", P_SOV_MID, "論理崩壊と児童詩的軽さで日常を異化するレニングラード前衛の短詩法。"),
    ("バフチン『発話ジャンル』", "Bakhtin speech genres", P_BAKH, "日常発話から文学形式までを一次・二次ジャンルとして捉える言語論。"),

    # Cluster 4: late Soviet and post-Soviet unofficial poetics
    ("リアノゾヴォ派バラック詩", "Lianozovo barrack poetry", P_SOV_LATE, "郊外バラックの貧困語彙と視覚実験で公的叙情を外す非公式詩。"),
    ("SMOG詩人グループ", "SMOG poets", P_SOV_LATE, "1960年代モスクワで若手が検閲外朗読と自費冊子を行った短命詩集団。"),
    ("メタリアリズム詩", "Metarealism poetry", P_SOV_LATE, "現実の背後の多層的比喩空間を探る1980年代ロシア詩の潮流。"),
    ("クラブ81レニングラード非公式文学", "Club 81 unofficial literature", P_SOV_LATE, "当局公認枠を逆用し地下作家が発表空間を得たレニングラード文学クラブ。"),
    ("ミチキ文化テキスト", "Mitki cultural text", P_POST, "酔い・友情・反英雄をゆるい共同体美学へ変えたペテルブルク発の文化文体。"),
    ("ルネット文学初期", "Early Runet literature", P_POST, "ネット掲示板と個人サイトで流通した1990年代ロシア語電子文学の初期形。"),

    # Cluster 5: non-Russian Slavic niche movements
    ("スカマンデル派の日常詩", "Skamander everyday poetics", P_POLISH, "独立後ポーランドで都市の日常語と反予言者姿勢を掲げた詩人集団。"),
    ("ジャガリ派カタストロフィズム", "Zagary catastrophism", P_POLISH, "ヴィリニュスの若手詩人が破局予感を歴史哲学化した1930年代詩潮。"),
    ("チェコ・ポエティスム", "Czech Poetism", P_CZECH, "遊戯・映画・サーカス感覚を詩へ移すデヴィエトスィル周辺の前衛運動。"),
    ("チェコ構造主義の美的機能", "Czech structuralist aesthetic function", P_CZECH, "ムカジョフスキーが芸術を社会的機能の変動として捉えた詩学概念。"),
    ("セルビア・ゼニティズム", "Serbian Zenitism", P_SOUTH, "バルカン的野蛮のエネルギーで欧州前衛を更新しようとした雑誌運動。"),
    ("ブルガリア・ディアボリズム", "Bulgarian Diabolism", P_SOUTH, "悪魔的幻想と都市不安を結びつけた戦間期ブルガリア短編の暗黒潮流。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 18"
            )
        }
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            if name_ja in existing:
                skipped += 1
                print(f"[skip-name] {name_ja}")
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 18"
        ).fetchone()["c"]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Subfield 18 total: {total}")


if __name__ == "__main__":
    main()
