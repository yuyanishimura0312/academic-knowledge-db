from lit_db_helper import LitDB


SUBFIELD = "lit_eu_modernism"
REGION = "西欧"
PERIOD_ID = 22


CONCEPTS = [
    # manuscript genetics
    ("プルースト割付紙片の層位", "Proust paperole stratigraphy", "貼紙増補の順序から長篇生成を読む分析単位。"),
    ("ジョイス赤鉛筆校正記号", "Joyce red-pencil proofs", "校正刷上の色鉛筆指示を改稿工程として読む論点。"),
    ("ウルフ削除段落の余白配置", "Woolf deleted paragraph spacing", "タイプ稿余白の削除跡から語りの沈黙を読む単位。"),
    ("カフカ四つ折りノート束", "Kafka folded-quarto bundles", "小型束ノートの物理配列で断章連鎖を読む方法。"),
    ("ムージル番号札カード索引", "Musil numbered card index", "章案カード番号で未完長篇の構成可能性を追う論点。"),
    ("ベケット英文草稿の仏語挿入", "Beckett French insertions in English drafts", "英文草稿内の仏語挿入を自己翻訳以前の異化として読む。"),
    # little magazines and print networks
    ("『S4N』前衛誌の誌面実験", "S4N magazine page experiments", "英仏前衛誌の版面処理を国際モダンの接点として読む。"),
    ("『クラルテ』文学欄モダン", "Clarte literary-column modernism", "左派誌文学欄に現れる前衛形式と政治語彙の接合。"),
    ("『ラ・ルヴュ・ユーロペエンヌ』翻訳網", "La Revue Europeenne translation network", "仏語誌の翻訳掲載を欧州小雑誌網として読む論点。"),
    ("『クエルシュニット』新即物欄", "Querschnitt Neue Sachlichkeit column", "ベルリン誌の軽妙な新即物性と国際趣味の交差。"),
    ("『ディスコンティニュイテ』短命誌", "Discontinuite short-lived review", "一号誌的断絶をシュルレアリスム周縁の戦術として読む。"),
    ("『メック』機械美学誌面", "Mecano mechanomorphic pages", "機械形態の版面を詩的構成として使うオランダ前衛。"),
    # peripheral and minority modernisms
    ("フェロー語初期モダン詩", "early Faroese modernist poetry", "島嶼語詩で都市的断片性を移植する周縁モダン。"),
    ("ロマンシュ語前衛小散文", "Romansh avant-garde short prose", "少数語散文が欧州前衛語法を圧縮移入する現象。"),
    ("サルデーニャ語モダン叙情", "Sardinian modernist lyric", "地方語叙情が象徴主義以後の断片形式を担う事例。"),
    ("ブルトン語都市詩", "Breton urban poetry", "地域語詩が都市騒音と交通感覚を取り込む局面。"),
    ("ラディン語山岳モダン詩", "Ladin Alpine modernist poetry", "山岳少数語で速度感覚と断片的抒情を結ぶ詩法。"),
    ("カシューブ語前衛抒情", "Kashubian avant-garde lyric", "バルト周縁の少数語詩が前衛形式を受容する論点。"),
    # micro-forms and page techniques
    ("時刻表型叙述", "timetable narration", "列車時刻表の配列を物語時間の骨格にする技法。"),
    ("領収書コラージュ詩", "receipt-collage poetry", "商業伝票の断片を詩行へ転用する頁面実験。"),
    ("電話帳式人物列挙", "telephone-directory character listing", "電話帳の列挙形式で都市匿名性を示す叙述。"),
    ("誤植保存版面", "preserved-misprint page", "誤植を訂正せず意味生成の痕跡として残す実験。"),
    ("電報改行リズム", "telegram line-break rhythm", "電文の短句と改行を詩的テンポへ変換する形式。"),
    ("欄外広告侵入", "marginal advertisement intrusion", "広告文が本文欄へ侵入し語りを攪乱する版面技法。"),
    # multilingual and translation poetics
    ("仏独混成カフェ対話", "Franco-German cafe dialogue", "カフェ会話で仏独語が切替わる多言語モダン技法。"),
    ("伊英自己翻訳草稿", "Italian-English self-translation drafts", "伊英間の自訳草稿差異を作家像の揺れとして読む。"),
    ("亡命者仮名署名", "exilic pseudonymous signatures", "亡命小雑誌で仮名署名が国籍と作者性をずらす現象。"),
    ("脚注内原語残存", "source-language residue in footnotes", "翻訳脚注に原語片を残し異文化性を可視化する方法。"),
    ("三言語朗読プログラム", "trilingual reading programme", "朗読会番組で三言語併置が前衛共同体を作る形式。"),
    ("通訳遅延の劇作法", "interpreter-delay dramaturgy", "通訳の遅れを舞台上の時間差として使う劇作技法。"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
    print(f"inserted_or_existing={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
