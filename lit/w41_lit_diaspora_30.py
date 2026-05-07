from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Indian Ocean and island print micro-traditions
    ("バタヴィア・マルディカー哀歌", "Batavian Mardijker elegy", "植民地バタヴィアの混血解放民に伝わる喪失歌。"),
    ("マレー・ジャウィ移民パンフレット", "Malay Jawi migrant pamphlet", "ジャウィ表記で港市移民に配られた廉価説話冊子。"),
    ("ケープ・マレー・キターブ詩", "Cape Malay kitab verse", "ケープのマレー系共同体がキターブ余白に残した詩。"),
    ("ペナン・タミル雑誌短編", "Penang Tamil magazine story", "ペナン Tamil 雑誌に載る港湾労働者の短編小説。"),
    ("モーリシャス・ボージュプリー歌謡小説", "Mauritian Bhojpuri song novel", "移民歌と散文が混じるモーリシャス系ボージュプリー物語。"),
    ("レユニオン・マラバール祈願歌", "Reunion Malbar vow song", "レユニオン島タミル系儀礼の誓願歌と移住記憶。"),
    # 2. Judeo-language and Sephardi fringe archives
    ("ハケットィア結婚コプラ", "Haketia wedding copla", "モロッコ系セファルディ婚礼で歌われるハケットィア連詩。"),
    ("テトゥアン・ラディーノ新聞小説", "Tetouan Ladino newspaper serial", "テトゥアンのラディーノ紙に載った移民連載小説。"),
    ("ジュデオ・ベルベル女性哀歌", "Judeo-Berber women's lament", "北アフリカのユダヤ女性が歌うベルベル語系離散哀歌。"),
    ("ロマニオット・メギラー翻案", "Romaniote megillah adaptation", "ギリシア系ユダヤ共同体のメギラー俗語翻案。"),
    ("クリムチャク語追放歌", "Krymchak deportation song", "クリミア系ユダヤ人の強制移住を歌うクリムチャク語歌。"),
    ("ユダヤ・グルジア語巡礼譚", "Judeo-Georgian pilgrimage tale", "グルジア系ユダヤ移民の巡礼と帰郷を語る小伝承。"),
    # 3. Black Atlantic and creole minor forms
    ("フェルナンディーノ新聞詩", "Fernandino newspaper verse", "ビオコ島フェルナンディーノ紙に載るクレオール詩。"),
    ("サントメ・フォロ語契約労働歌", "Forro contract-labor song", "サントメのフォロ語で契約労働移動を歌う小歌謡。"),
    ("トリニダード・ホセイ叙事歌", "Trinidad Hosay epic song", "ホセイ祭の記憶を移民叙事として歌うトリニダード歌。"),
    ("ベリーズ・クレオール移民笑話", "Belize Kriol migrant joke tale", "移住先とのずれを笑いにするベリーズ・クレオール小話。"),
    ("ロアタン黒人英語海難譚", "Roatan Black English shipwreck tale", "ロアタン島英語系共同体に残る海難と移動の説話。"),
    ("リベリア帰還民説教物語", "Liberian settler sermon tale", "帰還黒人入植者の説教に混じる米国記憶の物語。"),
    # 4. Balkan, Caucasus, and borderland diasporas
    ("カラマンリッド移民小冊子", "Karamanlidika migrant booklet", "ギリシア文字トルコ語で移民向けに刷られた小冊子。"),
    ("ガガウズ語出稼ぎ劇", "Gagauz labor-migrant drama", "ガガウズ語で出稼ぎと村落分裂を描く小演劇。"),
    ("メグレル語離散追悼詩", "Megrelian diaspora memorial verse", "メグレル語で亡命者を追悼する共同体詩。"),
    ("ラズ語亡命ラジオ詩", "Laz exile radio poem", "亡命放送で読まれたラズ語詩の記録文化。"),
    ("アルメニア・キプチャク書簡詩", "Armeno-Kipchak epistolary verse", "アルメニア文字キプチャク語書簡に混じる移住詩。"),
    ("チェルケス・ムハージル叙事歌", "Circassian muhajir epic song", "オスマン移住を語り継ぐチェルケス系叙事歌。"),
    # 5. Manuscript afterlives and theoretical micro-debates
    ("祖語フォント置換論争", "ancestral-font substitution debate", "継承文字を代替フォントで示す是非をめぐる小論争。"),
    ("亡命脚注の自己検閲", "exilic footnote self-censorship", "亡命作家が脚注で政治名を伏せる読解上の問題。"),
    ("継承語OCR誤読詩学", "heritage OCR misreading poetics", "継承語資料のOCR誤読を離散的ノイズとして読む視点。"),
    ("パスポート名カタログ詩", "passport-name catalogue poem", "旅券名の揺れを列挙して移民主体を描く詩型。"),
    ("ディアスポラ小型出版社奥付", "diaspora small-press colophon", "移民小出版社の奥付から流通網を読む文献概念。"),
    ("移民墓碑転写文学", "migrant gravestone transcription literature", "墓碑銘の転写で失われた移動史を再構成する実践。"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_diaspora",
                region="ディアスポラ",
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
