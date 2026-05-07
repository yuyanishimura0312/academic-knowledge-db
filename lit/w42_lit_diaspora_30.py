#!/usr/bin/env python3
"""Wave 42: add 30 ultra-niche lit_diaspora concepts."""

from lit_db_helper import LitDB


SUBFIELD_CODE = "lit_diaspora"
REGION = "ディアスポラ"
PERIOD_ID = None

CONCEPTS = [
    # 1. Indian Ocean labor liturgies
    ("ナタール・タミル契約詩", "Natal Tamil indenture verse", "ナタール契約移民が労働と帰郷不能を歌うタミル語詩。"),
    ("フィジー・ギルミティヤ・ビルハ", "Fiji girmitiya birha", "フィジー契約移民の別離を歌うボージュプリー系ビルハ。"),
    ("スリナム・サルナミ移民チャウタール", "Sarnami migrant chautal", "スリナムのサルナミ語歌謡に残る契約移民の季節記憶。"),
    ("グアドループ・タミル誓願歌", "Guadeloupe Tamil vow song", "グアドループ印僑儀礼で移住祖先を呼ぶタミル系誓願歌。"),
    ("ナタール・グジャラート商人帳物語", "Natal Gujarati ledger tale", "商人台帳の余白から離散家族を読むグジャラート語小譚。"),
    ("セイシェル・クレオール追放歌", "Seychellois Creole exile song", "島嶼流刑と労働移動を歌うセイシェル・クレオール小歌。"),
    # 2. Jewish micro-diasporic print
    ("ジュデオ・タジク新聞小説", "Judeo-Tajik newspaper fiction", "ブハラ系移民紙に載るジュデオ・タジク語連載小説。"),
    ("バグダーディ・ユダヤ英語回章", "Baghdadi Jewish English circular", "港市ユダヤ商人が英語回章で家族網を物語化する形式。"),
    ("ジュデオ・マラーティー追悼歌", "Judeo-Marathi elegiac song", "ベネ・イスラエル移民が共同体死者を歌うマラーティー哀歌。"),
    ("ジュデオ・マラヤーラム家系譚", "Judeo-Malayalam lineage tale", "コーチン系離散家族の系譜を語るマラヤーラム小伝承。"),
    ("テッサロニキ・ラディーノ船歌", "Salonican Ladino ship song", "港湾労働と亡命航路を歌うテッサロニキ系ラディーノ歌。"),
    ("カイロ・カライム追放メモワール", "Cairo Karaite expulsion memoir", "カイロ系カライム共同体の退去経験を記す小回想録。"),
    # 3. Afro-Atlantic enclaves
    ("ブルーフィールズ・クレオール帰還譚", "Bluefields Creole return tale", "ニカラグア英語系共同体が帰還と再移住を語る説話。"),
    ("プエルトリモン英語バラッド", "Puerto Limon English ballad", "カリブ系鉄道移民の労働記憶を歌うコスタリカ英語バラッド。"),
    ("バルバドス・パナマ運河書簡詩", "Barbados Canal letter verse", "パナマ運河労働者の手紙を詩化するバルバドス系表現。"),
    ("コロン・クレオール港湾小話", "Colon Creole port tale", "パナマ港市の黒人英語共同体が移動を笑話化する形式。"),
    ("ブルックリン・ガイアナ葬儀冊子", "Brooklyn Guyanese funeral booklet", "移民葬儀冊子が故郷と教会網を記録する文献実践。"),
    ("トロント・カリブ追悼ダブ詩", "Toronto Caribbean memorial dub", "移民二世が銃死と故郷記憶を重ねる追悼ダブ詩。"),
    # 4. Caucasus and steppe displacements
    ("ノガイ追放叙事歌", "Nogai deportation epic song", "草原離散と強制移住を語り継ぐノガイ語叙事歌。"),
    ("カラチャイ・バルカル帰還詩", "Karachay-Balkar return poem", "追放後の帰還を山岳地名で刻むカラチャイ・バルカル詩。"),
    ("アブハズ・ムハージル家譜譚", "Abkhaz muhajir genealogy tale", "オスマン移住家系を語るアブハズ系ムハージル伝承。"),
    ("アディゲ語亡命新聞詩", "Adyghe exile newspaper verse", "亡命紙面で祖地喪失を詠むアディゲ語共同体詩。"),
    ("メスヘティア・トルコ語追放回想", "Meskhetian Turkish exile memoir", "再移住を重ねたメスヘティア系家族の追放回想録。"),
    ("カルムイク離散仏教説話", "Kalmyk diaspora Buddhist tale", "移住先寺院で伝わるカルムイク語仏教説話の離散形。"),
    # 5. Tiny media and bureaucratic traces
    ("移民通帳余白詩", "migrant passbook marginalia", "通帳余白の覚書を送金と自己記録の詩として読む概念。"),
    ("国際電話カード物語", "calling-card narrative", "国際電話カードが親密圏と距離を媒介する移民小説装置。"),
    ("帰化証明書コラージュ", "naturalization-certificate collage", "帰化文書の断片を貼り合わせ身分変化を語る表現形式。"),
    ("領事館待合室独白", "consular waiting-room monologue", "領事館待合室で査証不安を独白化する越境文学の場面。"),
    ("送金領収書エピグラフ", "remittance-receipt epigraph", "章頭の送金領収書で家族責務を示す小説技法。"),
    ("墓地GPS巡礼譚", "cemetery-GPS pilgrimage tale", "墓地位置情報を頼りに離散家族史をたどる巡礼譚。"),
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
