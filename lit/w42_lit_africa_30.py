from lit_db_helper import LitDB


REGION = "グローバルサウス"

P = {
    "oral": 61,
    "colonial": 62,
    "anti": 63,
    "post": 149,
    "contemporary": 150,
    "maghreb": 151,
    "lusophone": 152,
    "egypt_sudan": 248,
}

CONCEPTS = [
    # サヘル女性歌謡と儀礼詩
    ("ザルマ語ホレイ精霊歌", "Zarma holey spirit songs", "ニジェールの精霊憑依儀礼で歌われるザルマ語詩歌。", P["oral"]),
    ("ウォロフ語ンドゥップ治癒歌", "Wolof ndëpp healing songs", "レブー女性儀礼に伴う治癒と召喚の歌詞形式。", P["oral"]),
    ("ソンガイ語ホロ奴隷記憶歌", "Songhay horo memory songs", "身分記憶を暗示するソンガイ語の儀礼歌謡。", P["oral"]),
    ("バンバラ語ボリ供犠讃歌", "Bambara boli sacrificial praise", "ボリ祭祀で唱えられる供犠対象への短い讃歌。", P["oral"]),
    ("フルベ語ヤーラル牧畜詩", "Fulfulde yaaral pastoral verse", "牧畜移動と美牛を称えるフルベ語祝祭詩。", P["oral"]),
    ("ハウサ語ボリ精霊劇歌", "Hausa bori spirit drama songs", "ボリ憑依劇の役柄を標識するハウサ語歌詞。", P["oral"]),
    # 東アフリカ海岸・インド洋小文芸
    ("パテ島スワヒリ語ウテンジ断簡", "Pate Swahili utenzi fragments", "パテ島写本に残るスワヒリ語叙事詩断片。", P["oral"]),
    ("モンバサ・マウリディ歌詞冊子", "Mombasa maulidi lyric booklets", "預言者生誕祭で配られたスワヒリ語讃歌冊子。", P["colonial"]),
    ("ザンジバル女性ターラブ返信詩", "Zanzibar women's taarab reply verse", "女性歌手が恋愛歌へ応答したターラブ詞章。", P["colonial"]),
    ("マダガスカル・カバリ演説詩", "Malagasy kabary oratorical verse", "儀礼演説カバリに挿入される諺的詩句。", P["oral"]),
    ("コモロ・シンゲ婚礼掛詞", "Comorian shinge wedding wordplay", "婚礼歌で交わされるコモロ語の掛詞的短句。", P["oral"]),
    ("シェラザード写本スワヒリ翻案", "Swahili Scheherazade manuscript adaptations", "千夜一夜系物語の沿岸スワヒリ語写本翻案。", P["colonial"]),
    # 南部アフリカ労働・新聞・劇
    ("ソト語ファモ歌詞新聞化", "Sesotho famo lyrics in print", "ファモ歌詞が新聞欄で政治風刺化する現象。", P["post"]),
    ("ズールー語イシカタミヤ歌詞詩学", "Zulu isicathamiya lyric poetics", "男声合唱歌詞の移民労働と夢表象の詩学。", P["post"]),
    ("ナマ語ヘンドリック・ヴィットボーイ書簡", "Nama Hendrik Witbooi letters", "ナマ語・蘭語書簡に現れる抵抗の修辞。", P["colonial"]),
    ("ツォンガ語鉱山帰還物語", "Tsonga mine-return narratives", "鉱山出稼ぎ帰還者を描くツォンガ語短編群。", P["post"]),
    ("ヘレロ語追悼讃歌オクヒュパ", "Herero okuhupa lament praise", "虐殺記憶を担うヘレロ語追悼讃歌。", P["colonial"]),
    ("アフリカーンス黒人新聞詩", "Black Afrikaans newspaper verse", "有色人種紙面に載った抵抗的アフリカーンス詩。", P["anti"]),
    # マグレブ・サハラ周縁写本
    ("タシュリヒート語アマルグ恋歌", "Tashelhit amarg love songs", "スース地方のベルベル語恋愛・離別歌。", P["maghreb"]),
    ("モザブ・イバード派説教詩", "Mzab Ibadi sermon verse", "モザブ共同体で読まれた教訓的アラビア語詩。", P["maghreb"]),
    ("トゥアレグ・テフィナグ恋文詩", "Tuareg Tifinagh love letters", "テフィナグ文字で刻まれた短い恋文詩。", P["oral"]),
    ("リーフ語移民カセット詩", "Riffian migrant cassette poetry", "欧州移民経験を歌うリーフ語カセット詩。", P["contemporary"]),
    ("サハラウィ・ハウル抵抗詩", "Sahrawi haul resistance poetry", "亡命キャンプで歌われるハッサーニーヤ抵抗詩。", P["contemporary"]),
    ("ジュデオ・アラビア語マグレブ哀歌", "Maghrebi Judeo-Arabic elegies", "北アフリカ・ユダヤ共同体の葬送哀歌。", P["maghreb"]),
    # デジタル返還・アーカイブ倫理
    ("アジャミ母音補記タグ論争", "Ajami vowel-tagging debate", "OCR後に母音補記を標準化するかの編集論争。", P["contemporary"]),
    ("口承採録GPS秘匿問題", "oral archive GPS concealment", "儀礼地保護のため採録位置を伏せる保存倫理。", P["contemporary"]),
    ("写本家系アクセス権プロトコル", "manuscript lineage access protocols", "家系単位で写本閲覧権を調整する手続き。", P["contemporary"]),
    ("ディアスポラ朗読逆輸入現象", "diaspora recitation reimportation", "海外朗読版が地域口承へ再流入する現象。", P["contemporary"]),
    ("少数語字幕正典化", "minor-language subtitle canonization", "映像字幕訳が文学テキストとして読まれる過程。", P["contemporary"]),
    ("AI復元写本異読監査", "AI-restored manuscript variant audit", "AI補完した欠損写本の異読を検証する手続き。", P["contemporary"]),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        before = db.conn.total_changes
        for name_ja, name_en, definition, period_id in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_africa",
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
        print(f"inserted={db.conn.total_changes - before}")


if __name__ == "__main__":
    main()
