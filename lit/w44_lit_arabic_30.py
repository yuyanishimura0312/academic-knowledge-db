from lit_db_helper import LitDB


CONCEPTS = [
    # 1. 写本・注釈文化
    ("アンタル写本の馬名索引欄外", "Antar manuscript horse-name marginal index", "シーラ写本欄外に馬名を整理する読者索引慣行。", 140),
    ("マカーマ写本の語釈朱点網", "maqama manuscript red-dot gloss network", "難語語釈を朱点で連結するマカーマ写本注釈法。", 19),
    ("ブスィーリー讃詩のワクフ印周縁書込", "waqf-stamp marginalia on Busiri praise poems", "寄進印の周囲に讃詩句を増補する写本所有痕跡。", 140),
    ("ムワッシャハ写本のハルジャ脚韻照合表", "kharja rhyme concordance in muwashshah manuscripts", "ハルジャ異文の脚韻を対照する写本内整理表。", 139),
    ("サマーア証書の詩句略記符号", "poetic abbreviations in sama certificate notes", "聴講証書で引用詩句を省略記号化する伝達記録。", 18),
    ("紙背ファトワー余白の即興ラジャズ", "improvised rajaz on reused fatwa margins", "再利用文書の余白に残る即興ラジャズ詩句。", 140),
    # 2. 韻律・修辞の微細分類
    ("イクファー押韻欠陥の部族名分類", "tribal taxonomy of ikfa rhyme defects", "イクファーを部族名で細分する韻律批評語彙。", 18),
    ("タスリーウ冒頭句の半句均衡論", "hemistich balance in tasri opening", "冒頭二半句を同韻化するタスリーウの均衡論。", 18),
    ("タドウィール半句跨ぎの朗誦処理", "recitation handling of tadwir enjambment", "半句を跨ぐ構文を朗誦で処理する韻律技法。", 18),
    ("ルズーム・マー・ラー・ヤルザム二重束縛", "double constraint in luzum ma la yalzam", "不要韻字を重ねて自縛する過剰押韻技法。", 18),
    ("サジウ終止音の鼻音化効果論", "nasal cadence effects in saj prose", "サジウ散文の終止鼻音が響きを作る効果論。", 18),
    ("タウリヤ地名掛詞の巡礼詩用法", "toponymic tawriya in pilgrimage poems", "巡礼詩で地名を二重意味化する掛詞技法。", 18),
    # 3. 口承・民俗詩
    ("ヒジャーズ水汲み歌のマジュルール応答", "majrur response in Hijazi water-drawing songs", "水汲み労働歌に入るマジュルール型応答句。", 140),
    ("シリア砂漠シャッルーキ隊商歌", "Syrian desert sharruqi caravan song", "隊商移動で歌われるシャッルーキ系の短詩。", 140),
    ("デルタ農村マワーウィールの種蒔き反復", "sowing refrains in Delta mawawil", "種蒔き作業に合わせて反復されるマワーウィール。", 20),
    ("ジャウフ婚礼サムリー詩の拍手拍", "clap meter in Jawf samri wedding verse", "サムリー婚礼詩を支える手拍子拍節。", 140),
    ("モースル哀悼アブーザイヤの半音下降", "semitone descent in Mosul abu-dhiyya laments", "モースル哀悼歌で半音下降を伴うアブーザイヤ。", 21),
    ("ハドラマウト海民ダーンの返句競合", "answer-verse contests in Hadrami dan sea songs", "海民ダーン歌で返句の機知を競う掛合い。", 140),
    # 4. 近現代メディアと検閲
    ("ナフダ新聞フェイユトンの韻文署名", "verse signatures in Nahda newspaper feuilletons", "新聞連載欄で筆名を韻文化する署名慣行。", 20),
    ("カイロ初期映画字幕のサジウ調", "saj cadence in early Cairo film intertitles", "無声映画字幕に現れるサジウ風文体。", 20),
    ("バグダードラジオ劇の詩的ジングル", "poetic jingles in Baghdad radio drama", "ラジオ劇の場面転換を担う短詩ジングル。", 21),
    ("ベイルート小雑誌の切貼り散文詩", "collage prose poems in Beirut little magazines", "小雑誌で断片を切貼りする散文詩実験。", 21),
    ("検閲済み小説の黒塗り章題詩", "redacted chapter-title poems in censored novels", "黒塗り章題が詩句として読まれる検閲後効果。", 21),
    ("湾岸ブログ小説の方言タグ韻", "dialect-tag rhyme in Gulf blog novels", "ブログ小説で方言タグを脚韻化する文体。", 21),
    # 5. 越境・ディアスポラ表現
    ("マルセイユ・マグリブ朗読会の港湾記憶詩", "harbor-memory verse in Marseille Maghrebi readings", "移民朗読会で港湾記憶を詠むマグリブ詩。", 21),
    ("ベルリン亡命詩のアラビア語母音脱落", "vowel omission in Berlin exile Arabic poetry", "亡命詩で母音省略を断絶記号にする表記法。", 21),
    ("チリ・マハジャル紙の二重署名詩", "dual-signature poems in Chilean Mahjar papers", "移民紙でアラビア語名と西語名を併記する詩。", 20),
    ("スーダン難民WhatsApp哀歌連鎖", "Sudanese refugee WhatsApp elegy chains", "WhatsAppで転送連鎖する難民共同体の哀歌。", 21),
    ("パリ郊外ラップ詩のムワッシャハ引用", "muwashshah quotation in banlieue rap verse", "郊外ラップ詩に挿入されるムワッシャハ引用。", 21),
    ("オンライン・タフミースの共同半句補作", "collaborative hemistich completion in online takhmis", "オンライン上で半句を共同補作するタフミース実践。", 21),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, definition, period_id in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_arabic",
                region="南西アジア",
                definition=definition,
                period_id=period_id,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )
    print(f"inserted_or_skipped={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
