from lit_db_helper import LitDB


CONCEPTS = [
    # Vedic recitation and exegetical micro-forms
    ("パダパータ読誦", "Padapatha recitation", "語を分解して唱えるヴェーダ本文保持法", 261),
    ("クラマパータ読誦", "Kramapatha recitation", "隣接語を連鎖させるヴェーダ暗誦形式", 261),
    ("ガナパータ読誦", "Ghanapatha recitation", "語順反復で本文を保護する高度な暗誦法", 261),
    ("ニガントゥ語彙集", "Nighantu lexicon", "ヴェーダ語の難語を分類した古層語彙集", 261),
    ("ニルクタ語源注釈", "Nirukta etymology", "ヤースカ系のヴェーダ語源解釈技法", 261),
    ("アヌクラマニー目録", "Anukramani index", "讃歌の作者・神格・韻律を列挙する索引", 261),

    # Sanskrit poetics and figure taxonomies
    ("アビダー語義機能", "Abhidha", "語が第一義を示す詩学上の意味作用", 236),
    ("ラクシャナー転義機能", "Lakshana", "文脈で第一義を離れる転義的意味作用", 236),
    ("ヴィヤンジャナー暗示機能", "Vyanjana", "字義を超え詩的含意を発生させる作用", 236),
    ("アヌプラーサ音韻修辞", "Anuprasa", "頭韻や反復音で効果を作る音修辞", 236),
    ("ウトプレークシャ想像修辞", "Utpreksha", "対象を仮想的に見立てる比喩的修辞", 236),
    ("ルーパカ隠喩修辞", "Rupaka", "喩える物と喩えられる物を同一化する修辞", 236),

    # Jaina and Prakrit textual niches
    ("シュラーヴァカーチャーラ文学", "Shravakachara literature", "在家ジャイナ信徒の行法を説く教訓文献", 265),
    ("プラバンダ・チンターマニ", "Prabandha Chintamani", "ジャイナ伝承の人物逸話を集めた説話集", 265),
    ("カルパスートラ朗誦本", "Kalpasutra recitation book", "祭礼で朗誦されるジャイナ聖者伝写本", 265),
    ("プラークリット・チャルチャー詩", "Prakrit charcha verse", "問答調で教義を整理するプラークリット詩", 265),
    ("ジャイナ・ラース叙事詩", "Jain ras epic", "西インドで発達したジャイナ系物語詩", 265),
    ("アーヴァシュヤカ・カター", "Avashyaka katha", "日課儀礼注釈に付随する教訓説話群", 265),

    # Regional oral and performance literatures
    ("ヴィッルパットゥ弓歌", "Villupattu", "弓を打楽器に用いるタミル語物語歌", 138),
    ("ヤクシャガーナ台本", "Yakshagana prasanga", "カンナダ語歌舞劇の韻文上演台本", 138),
    ("ブーター・コーラ歌謡", "Bhuta Kola songs", "トゥル語精霊祭祀で歌われる叙事歌", 138),
    ("テルグ・ブッラカター", "Telugu Burrakatha", "語り手三人で演じるテルグ語物語芸能", 138),
    ("パンディラヴァーニー歌謡", "Pandavani", "チャッティースガルのパーンダヴァ物語歌", 138),
    ("オッタン・トゥッラル詞章", "Ottan Thullal text", "風刺を含むマラヤーラム語独演舞踊詞章", 138),

    # Modern language movements and marginal print cultures
    ("フングリー世代宣言", "Hungry Generation manifesto", "1960年代ベンガル前衛詩運動の宣言文", 137),
    ("ナイ・カハーニー短編", "Nayi Kahani", "独立後ヒンディー語の都市的心理短編潮流", 239),
    ("ナヴヤ・カンナダ小説", "Navya Kannada novel", "実存意識を前景化したカンナダ近代小説", 244),
    ("ナイー・シェーリー詩", "Nai Sheri poetry", "都市感覚を押し出す近代ウルドゥー詩潮流", 240),
    ("ダリット・パンサー詩", "Dalit Panther poetry", "1970年代マラーティー急進ダリット詩", 245),
    ("ストリーヴァーディー短編", "Strivadi short fiction", "女性主体を掲げるインド諸語フェミ短編", 245),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, definition, period_id in CONCEPTS:
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
