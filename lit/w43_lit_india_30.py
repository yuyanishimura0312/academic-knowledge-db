from lit_db_helper import LitDB


CONCEPTS = [
    # Vedic ritual paratexts
    ("シャウナカ派アヌクラマニー", "Shaunaka Anukramani", "リグ讃歌の配列情報を伝えるシャウナカ系索引", 261),
    ("ブリハッドデーヴァター", "Brihaddevata", "リグ讃歌の神格説話を集めるヴェーダ補助文献", 261),
    ("プラティシャーキヤ音韻規則", "Pratishakhya rules", "各ヴェーダ学派の発音・連声を規定する音韻書", 261),
    ("シクシャー音声学文献", "Shiksha texts", "ヴェーダ朗誦の音高・長短・調音を説く小文献", 261),
    ("シュラウタスートラ祭式章", "Shrautasutra ritual sections", "大祭式の手順を簡潔に列挙する祭式スートラ", 261),
    ("グリヒヤスートラ家庭儀礼章", "Grihyasutra domestic rites", "婚礼・命名など家内儀礼を記すスートラ章句", 261),

    # Prakrit and Apabhramsha micro-genres
    ("サットサイ恋愛詩型", "Sattasai love-verse mode", "短詩連作で恋情の瞬間を描くプラークリット詩型", 236),
    ("ドーハーコーシャ集成", "Dohakosha anthology", "アパブランシャ二行詩を集める教訓・宗教詩集", 265),
    ("チャリウ英雄伝記詩", "Chariu heroic biography", "ジャイナ聖者や英雄の生涯を歌うアパブランシャ詩", 265),
    ("ラーソー宮廷叙事詩", "Raso court epic", "ラージャスターン周辺の王侯武勲を語る初期叙事詩", 267),
    ("フォーク・バータ伝承", "Phad barta narration", "絵巻布を開きながら語るラージャスターン物語伝承", 138),
    ("チャリャーギーティ秘教歌", "Charyagiti esoteric songs", "サハジャヤーナ修行を隠語で歌う初期東印歌謡", 264),

    # Tamil and Dravidian manuscript forms
    ("ウラー巡幸詩", "Ula procession poem", "神や王の巡幸を都市視線で描くタミル宮廷詩", 237),
    ("ピッライタミル幼年讃歌", "Pillaittamil", "神や聖者を幼児として讃えるタミル詩形式", 237),
    ("アンターティ連鎖詩", "Antati linked verse", "前詩末語を次詩頭に継ぐタミル連鎖詩法", 237),
    ("コーヴァイ恋愛連作", "Kovai sequence", "定型場面を連ねる中世タミル恋愛連作詩", 237),
    ("カンナダ・ヴァチャナ集成写本", "Kannada vachana manuscripts", "リンガーヤタ詩人の短章を伝える写本群", 267),
    ("テルグ・ヤクシャガーナ詞章", "Telugu Yakshagana texts", "テルグ語歌舞劇で用いられる韻文台本群", 138),

    # Perso-Urdu and Indo-Muslim print niches
    ("サブキー・ヒンディー散文", "Sabki Hindi prose", "北インド教育印刷で普及した平易ヒンディー散文", 239),
    ("フォート・ウィリアム教科書文学", "Fort William textbooks", "植民地語学教育用に編まれた初期近代散文群", 268),
    ("ダースターン・エ・アミール・ハムザ版本", "Hamza dastan editions", "長大なウルドゥー英雄譚を印刷本化した版本群", 240),
    ("ナウタンキー歌本", "Nautanki songbooks", "北インド民衆劇の歌詞と台詞を載せた廉価本", 138),
    ("レーフティー女性語詩", "Rekhti women's speech poetry", "女性語りを模したラクナウ系ウルドゥー詩", 240),
    ("マルシヤー・アンジュマン朗誦", "Marsiya anjuman recitation", "シーア追悼詩を集会で朗誦する都市文芸慣行", 240),

    # Northeast and borderland literatures
    ("アッサム・サトラ演劇写本", "Assamese satra play manuscripts", "サトラ寺院劇の上演詞章を伝えるアッサム語写本", 267),
    ("ボド・カマイ歌謡", "Bodo Khamai songs", "ボド共同体儀礼で歌われる祈願・叙事歌謡", 138),
    ("ミゾ・ラルラム叙事歌", "Mizo Lalram epic songs", "ミゾ首長伝承を語る口承叙事歌の系統", 138),
    ("カシ・ラブン物語歌", "Khasi Labon narrative songs", "カシ語で祖先譚や地名由来を歌う物語歌", 138),
    ("メイテイ・ワリ・リバ朗読", "Meitei wari liba recitation", "マニプルの物語を朗読・語りで伝える実演形式", 138),
    ("レプチャ・ムン儀礼歌", "Lepcha mun ritual songs", "レプチャ巫者が神話と治癒を歌う儀礼歌", 138),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, definition, period_id in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_india",
                region="南アジア",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="minor",
            )


if __name__ == "__main__":
    main()
