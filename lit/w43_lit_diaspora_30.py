#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche lit_diaspora concepts."""

from lit_db_helper import LitDB


SUBFIELD_CODE = "lit_diaspora"
REGION = "ディアスポラ"
PERIOD_ID = None

CONCEPTS = [
    # 1. Micro-press and pamphlet circuits
    ("シンガポール・シンド商人小冊子", "Singapore Sindhi merchant booklet", "シンド商人の移住網を広告と逸話で綴る英印系小冊子。"),
    ("香港パールシー慈善年報物語", "Hong Kong Parsi charity annual tale", "慈善年報の寄付者名簿から離散共同体を読む小叙述。"),
    ("マニラ・アルメニア商館書簡譚", "Manila Armenian counting-house letters", "商館書簡が港市間の親族と信用を物語化する形式。"),
    ("バタヴィア華僑公所碑文集", "Batavia Chinese kongsi epitaph anthology", "公所碑文を集め移住者の徳行と故郷を記す文献実践。"),
    ("ヨハネスブルグ・リトアニア語会報詩", "Johannesburg Lithuanian newsletter verse", "鉱山都市の移民会報に載るリトアニア語郷愁詩。"),
    ("メルボルン・マルタ移民劇ビラ", "Melbourne Maltese migrant playbill", "劇ビラの役名と広告で島嶼移民生活を読む資料。"),
    # 2. Ritual and mourning texts
    ("イスタンブル・セファルディ忌日冊子", "Istanbul Sephardi yahrzeit booklet", "忌日冊子が家族移動とラディーノ記憶を保存する形式。"),
    ("ザンジバル・ボーラ追悼マルスィヤ", "Zanzibar Bohra marsiya", "ボーラ共同体がインド洋移動を死者追悼に織る哀歌。"),
    ("ケープタウン・ハドラミー墓参詩", "Cape Town Hadhrami grave-visit poem", "墓参詩が祖地ハドラマウトと南部アフリカを結ぶ。"),
    ("ロンドン・キプロス追悼新聞欄", "London Cypriot memorial column", "移民新聞の追悼欄が村名と親族網を記録する場。"),
    ("マルセイユ・コモロ婚礼詠唱", "Marseille Comorian wedding chant", "婚礼詠唱が港市移住と島の系譜を結ぶ口承形式。"),
    ("デトロイト・カルデア葬儀小冊子", "Detroit Chaldean funeral booklet", "葬儀小冊子が故郷村と教会移住史を記す文献。"),
    # 3. Audio, radio, and cassette forms
    ("パリ・カビル亡命カセット詩", "Paris Kabyle exile cassette poetry", "カセット録音で村落喪失と労働移住を歌うカビル詩。"),
    ("ベルリン・アッシリア語ラジオ劇", "Berlin Assyrian radio drama", "亡命放送で家族分散と継承語を演じるラジオ劇。"),
    ("シカゴ・ポーランド移民電話詩", "Chicago Polish call-in verse", "電話投稿番組に寄せるポーランド語移民生活詩。"),
    ("シドニー・トンガ親族カセット書簡", "Sydney Tongan cassette letter", "声の手紙が送金と親族義務を媒介する物語形式。"),
    ("ブリュッセル・ルワンダ追悼ラジオ証言", "Brussels Rwandan memorial radio testimony", "追悼放送が亡命者の証言と共同体記憶を編む形式。"),
    ("テルアビブ・ブハラ民謡録音注釈", "Tel Aviv Bukharan song annotation", "移住後の民謡録音に付く注釈が失地を説明する。"),
    # 4. Bureaucratic and legal genres
    ("亡命公証翻訳余白", "asylum notarized-translation margin", "公証翻訳の余白に残る固有名と証言の揺れを読む概念。"),
    ("船員手帳ディアスポラ詩学", "seafarer booklet diaspora poetics", "船員手帳が港市労働と仮住まいを記録する詩学。"),
    ("ビザ更新領収書連作", "visa-renewal receipt sequence", "ビザ更新領収書を章立てに用い滞在不安を示す形式。"),
    ("出生地訂正申立ナラティブ", "birthplace-correction petition narrative", "出生地訂正申立が国籍と故郷表記をめぐる語りになる。"),
    ("難民家族再統合宣誓書", "refugee family-reunification affidavit", "再統合宣誓書が親族離散を法的物語へ圧縮する。"),
    ("港湾検疫票エピグラフ", "port quarantine-card epigraph", "検疫票を章頭に置き移動身体の管理を示す技法。"),
    # 5. Heritage-language scripts and scripts in transit
    ("キリル文字アルバニア移民詩", "Cyrillic Albanian migrant verse", "旧正書法のキリル表記で移住経験を記すアルバニア語詩。"),
    ("ローマ字ソマリ家族回覧", "Romanized Somali family circular", "ローマ字ソマリ語回覧が離散家族の近況を循環させる。"),
    ("ギリシア文字カラマンリ追悼文", "Greek-script Karamanli memorial text", "ギリシア文字トルコ語で移住死者を悼む小文。"),
    ("アラビア文字ベラルーシ・タタール手記", "Arabic-script Belarusian Tatar memoir", "アラビア文字スラヴ語手記がタタール移住記憶を残す。"),
    ("ヘブライ文字イディッシュSMS詩", "Hebrew-script Yiddish SMS poem", "SMS形式で継承語の短縮と離散親密圏を示す詩。"),
    ("ラテン文字アムハラ移民ブログ", "Latinized Amharic migrant blog", "ラテン転写アムハラ語で移民生活を綴るブログ散文。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"{name_ja}: definition too long")
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None and cid:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
