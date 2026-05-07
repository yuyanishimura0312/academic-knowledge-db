#!/usr/bin/env python3
"""Wave 39 C02: add 30 ultra-niche medieval Europe concepts."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_medieval"
REGION = "西欧"

P_LATIN = 219
P_FR = 213
P_OCCITAN = 214
P_NORTH = 218
P_GERMAN = 216
P_IBERIA = 215

CONCEPTS = [
    # 1. 中世ラテン小叙事・学校文学
    ("『エクバシス・カプティヴィ』", "Ecbasis captivi", "Ecbasis captivi", "latin", P_LATIN, "子牛の逃亡譚を修道院風刺に仕立てた11世紀ラテン獣寓話詩。"),
    ("『ルオドリーブ』断片", "Ruodlieb fragments", "Ruodlieb", "latin", P_LATIN, "騎士の遍歴と宮廷処世を描く11世紀ラテン語ロマンス断片。"),
    ("『イーサングリムス』", "Ysengrimus", "Ysengrimus", "latin", P_LATIN, "狐レイナード系譚を狼僧批判へ展開したラテン風刺叙事詩。"),
    ("『パムフィルス』", "Pamphilus de amore", "Pamphilus de amore", "latin", P_LATIN, "恋愛誘惑を対話劇風に描く学校用ラテン喜劇的詩作品。"),
    ("マテオルス『哀歌』", "Matheolus Lamentations", "Lamentationes Matheoluli", "latin", P_LATIN, "結婚生活への怨嗟を韻文で述べる反女性的ラテン哀歌。"),
    ("『ゲッタ』ヴィタリス作", "Vitalis Geta", "Geta", "latin", P_LATIN, "アンフィトリュオ譚を学校喜劇へ翻案した12世紀ラテン戯曲。"),
    # 2. 古仏語小ロマンス
    ("『フロワールとブランシュフルール』", "Floire et Blancheflor", "Floire et Blancheflor", "latin", P_FR, "異教王子とキリスト教少女の恋を語る古仏語牧歌的ロマンス。"),
    ("『ギヨーム・ド・パレルヌ』", "Guillaume de Palerne", "Guillaume de Palerne", "latin", P_FR, "狼人間の援助で逃避行を進める古仏語冒険ロマンス。"),
    ("『アミとアミル』古仏語版", "Ami et Amile", "Ami et Amile", "latin", P_FR, "友情と犠牲を聖人伝的奇跡へ結ぶ古仏語友情ロマンス。"),
    ("『ピラミュスとティスベ』古仏語詩", "Piramus et Tisbe", "Piramus et Tisbe", "latin", P_FR, "オウィディウス恋愛悲劇を宮廷語法で翻案した古仏語短詩。"),
    ("ジャン・ルナール『ばら物語』", "Jean Renart Roman de la Rose", "Roman de la Rose ou de Guillaume de Dole", "latin", P_FR, "歌を散文筋へ挿入するジャン・ルナールの宮廷ロマンス。"),
    ("『シャテルラン・ド・クシー』", "Chatelain de Couci", "Roman du Chatelain de Couci", "latin", P_FR, "詩人騎士の恋と心臓食い伝説を結ぶ古仏語ロマンス。"),
    # 3. オック語・カタルーニャ周縁
    ("『フラメンカ』", "Flamenca", "Flamenca", "latin", P_OCCITAN, "嫉妬深い夫に監禁された女性の恋を描くオック語長編ロマンス。"),
    ("ギラウト・リキエルの晩期トロバール", "Guiraut Riquier lyric", "Guiraut Riquier", "latin", P_OCCITAN, "トルバドゥール終末期の自己注釈的で精密なオック語抒情。"),
    ("ペイレ・カルデナル諷刺詩", "Peire Cardenal sirventes", "Peire Cardenal", "latin", P_OCCITAN, "聖職者批判と政治諷刺を鋭く歌うオック語シルヴェンテス。"),
    ("ライモン・ヴィダル『トロバールの理』", "Raimon Vidal Razos de trobar", "Razos de trobar", "latin", P_OCCITAN, "オック語詩作の文法と用語を説く初期トルバドゥール詩学書。"),
    ("『アルビジョワ十字軍の歌』", "Canso de la Crozada", "Canso de la Crozada", "latin", P_OCCITAN, "南仏戦争を二声的視点で記すオック語・古仏語叙事詩。"),
    ("セルカモンのプラン", "Cercamon planh", "Cercamon", "latin", P_OCCITAN, "死者哀悼と封建的喪失を結ぶ初期トルバドゥール哀歌。"),
    # 4. 北方・ケルト周縁
    ("『エイルビッギャ・サガ』", "Eyrbyggja saga", "Eyrbyggja saga", "latin", P_NORTH, "スナイフェルスネスの家系争いと怪異を語るアイスランド・サガ。"),
    ("『ギスリのサガ』", "Gisla saga Surssonar", "Gisla saga Surssonar", "latin", P_NORTH, "追放者ギスリの夢と復讐を描くアイスランド家族サガ。"),
    ("『オルクニー人のサガ』", "Orkneyinga saga", "Orkneyinga saga", "latin", P_NORTH, "オークニー伯領の権力抗争を編む北大西洋サガ。"),
    ("『ファーグルスキンナ』", "Fagrskinna", "Fagrskinna", "latin", P_NORTH, "ノルウェー王たちの物語を簡潔に編年する王権サガ集。"),
    ("『ブランの航海』", "Immram Brain", "Immram Brain", "latin", P_NORTH, "異界島への航海を歌う古アイルランド語イムラム文学。"),
    ("『タリエシンの書』", "Book of Taliesin", "Llyfr Taliesin", "latin", P_NORTH, "伝説詩人タリエシン名義のウェールズ語詩を収める写本。"),
    # 5. イベリア・中高ドイツ小伝承
    ("『アポロニオの書』", "Libro de Apolonio", "Libro de Apolonio", "latin", P_IBERIA, "遍歴王アポロニオをクアデルナ・ビアで語るカスティーリャ詩。"),
    ("『アレクサンドレの書』", "Libro de Alexandre", "Libro de Alexandre", "latin", P_IBERIA, "アレクサンドロス伝を学僧詩法で拡張したカスティーリャ長詩。"),
    ("『フェルナン・ゴンサレスの詩』", "Poema de Fernan Gonzalez", "Poema de Fernan Gonzalez", "latin", P_IBERIA, "カスティーリャ伯の独立伝説を修道院的叙事詩にした作品。"),
    ("『モカダーデス・デ・ロドリーゴ』", "Mocedades de Rodrigo", "Mocedades de Rodrigo", "latin", P_IBERIA, "若きシッドの粗暴な武勇を語る後期カスティーリャ叙事詩。"),
    ("ハルトマン『貧しきハインリヒ』", "Der arme Heinrich", "Der arme Heinrich", "latin", P_GERMAN, "病む騎士と献身する少女をめぐる中高ドイツ語短編物語。"),
    ("シュトリッカー『司祭アーミス』", "Der Pfaffe Amis", "Der Pfaffe Amis", "latin", P_GERMAN, "詐術に長けた司祭を主人公にする中高ドイツ語滑稽譚集。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 2"
            )
        }
        dupes = [row[0] for row in CONCEPTS if row[0] in existing]
        if dupes:
            raise SystemExit(f"duplicates: {dupes}")
        for item in CONCEPTS:
            assert len(item[5]) <= 100, item[0]

        inserted = 0
        for name_ja, name_en, name_original, original_script, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=original_script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="primary",
                canonical_in_region="minor",
            )
            inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 2"
        ).fetchone()["c"]
        print(f"inserted={inserted} total={total}")


if __name__ == "__main__":
    main()
