from lit_db_helper import LitDB


CONCEPTS = [
    # Occitan and Catalan lyric microforms
    ("ドンプナトゲ（女性支配語法）", "dompna-oriented rhetoric", None, 214, "オック語恋愛詩で貴婦人への封臣的服従を示す語法"),
    ("メゾナドゥーラ（中庸トロバール）", "trobar mesurat", None, 214, "難解詩風と平明詩風の中間を志向するオック語詩法"),
    ("グロサ（トロバドゥール評釈）", "troubadour gloss", None, 214, "歌詞や詩人伝に付されるオック語・ラテン語の解釈注"),
    ("コブラ・カプフィニーダ", "cobla capfinida", None, 214, "前連末語を次連冒頭へ接続するトロバドゥール連構成"),
    ("デスコルト多言語型", "multilingual descort", None, 214, "複数言語を交替させ恋の不和を形式化するデスコルト"),
    ("ゲイ・サベールの花章規定", "Floral Games rules", None, 214, "トゥールーズ詩会で詩型と賞を制度化した規則群"),
    # Old French romance, song, and drama niches
    ("ロトルアンジュ", "rotrouenge", None, 213, "古仏語抒情詩の一形式で、反復句を伴う騎士的歌"),
    ("コンジェ・ダラス", "Arras congé", None, 213, "アラス詩人が都市共同体へ別れを告げる叙情ジャンル"),
    ("ジュ・パルティ・ダラス", "Arras jeu-parti", None, 213, "アラスの詩人団体で交わされた二者択一の恋愛論争歌"),
    ("ロマン・ディドー写本群", "Didot-Perceval cluster", None, 213, "散文聖杯物語を伝えるディドー系写本群"),
    ("ミラクル・ド・ノートルダム", "Miracles de Nostre Dame", None, 114, "聖母の介入を劇化する古仏語奇蹟劇群"),
    ("アリストテレスのレー", "Lai d'Aristote", None, 213, "賢者の失墜を滑稽化する古仏語短詩物語"),
    # Insular manuscript and devotional microtraditions
    ("ソウルズ・アドレス写本伝承", "Soul's Address tradition", None, 116, "魂と身体の対話を英語写本で反復する説教詩伝承"),
    ("ハーレー2253恋愛歌群", "Harley 2253 love lyrics", None, 217, "ハーレー写本2253に収められた多言語恋愛抒情詩群"),
    ("キルデア詩群", "Kildare Poems", None, 116, "14世紀アイルランド英語で書かれた風刺・宗教詩群"),
    ("サウス・イングリッシュ・レジェンダリー異本", "SEL variants", None, 116, "南英語聖人伝集の地域写本差を示す異本群"),
    ("アンカライト規則三部作", "ancrene trilogy", None, 116, "隠修女向け規範書と関連説教・瞑想文の一群"),
    ("ヨーク水売り劇", "York Waterleaders play", None, 217, "ヨーク聖史劇で水売り同職組合が担ったノア劇"),
    # Germanic and Norse minor forms
    ("シュプルーフディヒトゥング細分類", "Sangspruch subgenres", None, 118, "中高ドイツ語格言歌の政治・道徳・宗教的下位型"),
    ("ロイヒのミンネザング", "Leich Minnesang", None, 216, "旋律と節型を変化させる長大な中高ドイツ語恋愛歌"),
    ("メーレ形式", "Maere", None, 118, "中高ドイツ語の短い韻文物語・教訓笑話形式"),
    ("ビスプルーディヒトゥング", "Bispel poetry", None, 118, "例話を韻文化して教訓化する中高ドイツ語詩"),
    ("ラウスヴィーサ", "lausavisa", None, 117, "サガ内で即興的に挿入される単独スカルド詩節"),
    ("セーンナ（罵倒問答）", "senna", None, 117, "古ノルド文学で名誉を争う罵倒・応酬の場面型"),
    # Latin, Iberian, and Slavic learned niches
    ("ノトゥラエ・アウクトーリス", "notulae auctoris", None, 219, "中世ラテン写本で作者情報を短く示す欄外注"),
    ("フロリレギウム配列術", "florilegium ordering", None, 219, "引用摘録集で権威文句を主題順に配置する編集技法"),
    ("リズムス・デ・サンクティス", "rhythmus de sanctis", None, 219, "聖人讃歌を俗ラテン韻律で歌う短詩形式"),
    ("アルス・プレディカンディ序論型", "ars praedicandi accessus", None, 219, "説教術書で主題・分割・適用を導入する定型構成"),
    ("カンティガ・デ・マルディゼール", "cantiga de maldizer", None, 215, "露骨な名指しで相手を攻撃するガリシア語風刺歌"),
    ("プロストラノエ・ジチエ型", "expanded vita", None, 220, "スラヴ聖人伝で奇蹟と説教を増補する長篇伝記型"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, (name_ja, len(definition))
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code="lit_eu_medieval",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
