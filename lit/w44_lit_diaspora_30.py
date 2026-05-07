#!/usr/bin/env python3
"""Wave 44: add 30 ultra-niche lit_diaspora concepts."""

from lit_db_helper import LitDB


SUBFIELD_CODE = "lit_diaspora"
REGION = "ディアスポラ"
PERIOD_ID = None

CONCEPTS = [
    # 1. Port micro-archives
    ("マカオ・マカエンセ弔辞小冊子", "Macanese funeral booklet", "マカエンセ共同体の姓と港市移動を弔辞に残す小冊子。"),
    ("ボンベイ・バグダーディ会堂掲示詩", "Bombay Baghdadi synagogue notice verse", "会堂掲示の韻文が商人離散と寄進を記す形式。"),
    ("スラバヤ華僑墓誌拓本譚", "Surabaya Chinese epitaph rubbing tale", "墓誌拓本を通じて客家・福建移民の系譜を読む小叙述。"),
    ("アデン・ソマリ船員歌冊子", "Aden Somali seafarer song booklet", "船員歌冊子が紅海移動と賃労働の声を保存する。"),
    ("カルカッタ・アルメニア訃報欄", "Calcutta Armenian obituary column", "訃報欄が商館家族の移動先と教会記憶を列挙する。"),
    ("セイロン・マレー連隊回想詩", "Ceylon Malay regiment memoir verse", "連隊移住の記憶をマレー語混交韻文で語る形式。"),
    # 2. Ritual booklets and domestic rites
    ("クラクフ・ロマ追悼カード物語", "Krakow Romani memorial card tale", "追悼カードが移動親族と収容記憶を短く物語化する。"),
    ("イズミル・ラディーノ割礼歌本", "Izmir Ladino circumcision songbook", "割礼歌本が家族儀礼と地中海離散を結びつける。"),
    ("カイロ・ギリシア人婚礼新聞詩", "Cairo Greek wedding newspaper verse", "婚礼新聞詩が商家同盟と帰郷不能を祝祭内に記す。"),
    ("サイゴン・タミル寺院誓願札詩", "Saigon Tamil temple vow slip verse", "寺院の誓願札が移住労働者の願いを韻文化する。"),
    ("ハバナ華人清明祭文", "Havana Chinese Qingming ritual text", "清明祭文が墓地巡礼と広東系移民記憶を接続する。"),
    ("ベイルート・アルメニア洗礼名簿譚", "Beirut Armenian baptism-register tale", "洗礼名簿が難民家族の再定住と命名を語る資料になる。"),
    # 3. Sound and broadcast fragments
    ("モントリオール・ハイチ葬送ラジオ詩", "Montreal Haitian funeral radio verse", "葬送番組の詩がクレオール追悼と移民聴衆を結ぶ。"),
    ("ロッテルダム・カーボベルデ船歌録音", "Rotterdam Cape Verdean sea-song recording", "港湾録音の船歌が島嶼離散と労働記憶を響かせる。"),
    ("大阪ブラジル日系FM短歌", "Osaka Nikkei Brazilian FM tanka", "FM投稿短歌がポルトガル語圏日系移民の日常を刻む。"),
    ("マドリード赤道ギニア亡命朗読", "Madrid Equatoguinean exile recitation", "亡命朗読会がスペイン語圏アフリカ記憶を再配置する。"),
    ("ストックホルム・チリ亡命カセット劇", "Stockholm Chilean exile cassette drama", "カセット劇が軍政亡命者の家庭内記憶を演じる形式。"),
    ("トロント・パンジャーブ留守電ガザル", "Toronto Punjabi voicemail ghazal", "留守電の声をガザル化し遠隔親密性を示す移民詩。"),
    # 4. Bureaucratic edge texts
    ("帰化面接逐語録小説", "naturalization interview transcript novel", "帰化面接の逐語録形式で発音と忠誠の圧力を描く小説。"),
    ("国外退去命令脚注詩", "deportation-order footnote poem", "退去命令書の脚注が家族史と法的暴力を示す詩形。"),
    ("難民番号バーコード叙述", "refugee-number barcode narrative", "難民番号とバーコードを章題化し匿名化を語る技法。"),
    ("領事館出生届余白譚", "consular birth-registration margin tale", "出生届の余白が二重国籍と継承名の揺れを記録する。"),
    ("再入国許可証エピグラフ", "re-entry permit epigraph", "再入国許可証を章頭に置き滞在の暫定性を示す技法。"),
    ("通訳者署名の証言詩学", "interpreter-signature testimony poetics", "通訳者署名が証言の媒介性と不信を可視化する概念。"),
    # 5. Script-switching and small media
    ("ラテン文字ティグリニャ亡命短信", "Latinized Tigrinya exile text message", "ラテン転写ティグリニャ語短信が亡命親族圏を維持する。"),
    ("アラビア文字シンド語商用SMS", "Arabic-script Sindhi merchant SMS", "アラビア文字シンド語SMSが商取引と親族連絡を重ねる。"),
    ("キリル文字モルドバ移民ブログ", "Cyrillic Moldovan migrant blog", "キリル表記のブログが労働移住と正書法政治を映す。"),
    ("ヘブライ文字ジュデオ・スペイン語絵葉書", "Hebrew-script Judeo-Spanish postcard", "ヘブライ文字絵葉書が地中海離散の私信を保存する。"),
    ("ローマ字ネパール語介護日誌", "Romanized Nepali care-work diary", "ローマ字ネパール語日誌が介護労働と送金生活を綴る。"),
    ("混字アルメニア語チャット詩", "mixed-script Armenian chat poem", "アルメニア文字とラテン字の混用で離散会話を詩化する。"),
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
