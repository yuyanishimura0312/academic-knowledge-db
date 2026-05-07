from lit_db_helper import LitDB


SUBFIELD = "lit_eu_medieval"
REGION = "西欧"


CONCEPTS = [
    # 1. Occitan and Catalan stanza microtechniques
    ("コブラ・エスパルサ", "cobla esparsa", 214, "単独連だけで完結するオック語トロバドゥール短詩"),
    ("コブラス・ウニソナンス", "coblas unissonans", 214, "全連で同じ脚韻音を保つトロバドゥール連構成"),
    ("コブラス・ドブラス", "coblas doblas", 214, "二連ごとに脚韻組を替えるオック語詩の連結法"),
    ("コブラス・シングラルス", "coblas singulars", 214, "各連ごとに新しい脚韻組を用いるトロバドゥール詩法"),
    ("リムス・ディソルツ", "rims dissoluts", 214, "各行が別個の脚韻系列を持つ高度なオック語技巧"),
    ("エストランプ詩法", "estramp", 214, "脚韻を置かず同一韻律で押し通すカタルーニャ詩法"),
    # 2. Insular manuscript and scribal niches
    ("トレムルス・ハンド注記", "Tremulous Hand glosses", 116, "ウースター写本に古英語語句を震える筆跡で注す慣行"),
    ("ラヤモン『ブルート』二写本差", "Layamon Brut manuscript variants", 116, "『ブルート』二主要写本に現れる語形・韻律差"),
    ("オルムルム正書法", "Ormulum orthography", 116, "短母音後の子音重写で発音を示す中英語表記法"),
    ("アクリン・ウィスAB言語", "Ancrene Wisse AB language", 116, "西ミッドランド系写本に見られる標準化した中英語書記語"),
    ("カリグラA.ix動物寓話群", "Caligula A.ix beast texts", 116, "同写本に集められた鳥獣対話・寓話的中英語作品群"),
    ("ヴェルチェリ書ルーン署名", "Vercelli runic signatures", 115, "キュネウルフ名をルーンで埋め込む古英語宗教詩の署名法"),
    # 3. Medieval Latin scholastic and compilation forms
    ("アクセススの六項目型", "six-part accessus", 219, "作者・題名・意図など六項で古典を導入する注釈定型"),
    ("プロエミウム主題提示", "proemial thema", 219, "説教や論書の冒頭で聖句主題を掲げるラテン序法"),
    ("ディヴィシオ・テマティス", "divisio thematis", 219, "説教主題の語を分割し論点配列へ変換する技法"),
    ("クラウスラ韻律散文", "cursus clausulae", 219, "文末リズムを整え権威を示す中世ラテン散文技法"),
    ("コンピラティオ序文", "compilatio prologue", 219, "抜粋編集物で素材の権威と配列意図を説明する序文型"),
    ("アウクトリタス索引", "auctoritas index", 219, "権威引用を検索可能に並べる説教・学術写本の索引"),
    # 4. Germanic and Norse textual minutiae
    ("ヒルデブラント歌頭韻欠損", "Hildebrandslied alliterative gaps", 118, "古高ドイツ語断片に残る頭韻対応の破れと補読問題"),
    ("ニーベルンゲン詩節異形", "Nibelungenstrophe variants", 216, "写本間で音節数やカエスラが揺れる英雄叙事詩節"),
    ("ミンネレーデ短篇型", "short Minnerede", 119, "恋愛議論を小規模な韻文独白にまとめる中世末期形式"),
    ("シュヴァンクメールライン", "Schwankmaere", 119, "笑話的逸話を韻文化した中世末期ドイツ語短篇"),
    ("トリストラム韻文断片", "Tristrams saga verse insertions", 117, "北欧トリストラム伝承に挿入される韻文断片"),
    ("フォルナルダルサガ韻文挿入", "fornaldarsaga verse insertions", 117, "伝説サガの物語進行を区切る古詩風の挿入詩節"),
    # 5. Iberian and Slavic border forms
    ("モサラベ語ハルチャ女性声", "female-voice kharja", 215, "ハルチャ末尾で恋する女性の声を俗語で響かせる型"),
    ("ムワッシャハ末尾接合", "muwashshah-kharja junction", 215, "アラビア語・ヘブライ語詩体から俗語末尾へ移る接合部"),
    ("クアデルナ・ビア脚韻例外", "cuaderna via rhyme exceptions", 215, "四行同韻詩形で写本伝承に現れる脚韻逸脱"),
    ("アルハミアード表記詩", "Aljamiado verse script", 215, "ロマンス語詩をアラビア文字で記すイベリア写本慣行"),
    ("カンティガ写本割付", "cantiga manuscript layout", 215, "歌詞・記譜・挿絵を連動配置するカンティガ写本設計"),
    ("ズボルニク説教配列", "zbornik homily ordering", 220, "スラヴ雑纂写本で説教や聖人伝を暦順に並べる配列法"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB() as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, (name_ja, len(definition))
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
