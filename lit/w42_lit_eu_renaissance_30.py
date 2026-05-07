#!/usr/bin/env python3
"""Wave 42: 30 hyper-niche European Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian comic, dialect, and marginal print
    ("ルザンテ『ビロラ』", "Ruzante, Bilora", "Bilora", P_IT, "パドヴァ方言で農民の嫉妬と暴力を描く短喜劇。"),
    ("ルザンテ『帰還兵』", "Ruzante, The Veteran", "Il reduce", P_IT, "戦争帰りの農民声を方言で響かせる反牧歌劇。"),
    ("カルロ・ゴッツィ以前の即興ラッツィ", "pre-Gozzi commedia lazzi", "lazzi", P_IT, "定型仮面役が挟む即興身振りと小滑稽場面。"),
    ("カランドリア型俗語喜劇", "Calandria-type vernacular comedy", "commedia erudita", P_IT, "ビッビエーナ以後の学識喜劇が用いた取違え筋。"),
    ("ニッコロ・フランコ『ピストレ』", "Niccolo Franco, Pistole vulgari", "Pistole vulgari", P_IT, "毒舌書簡を俗語出版で演じる反アレティーノ散文。"),
    ("リングア・ペデスカ詩", "lingua pedesca verse", "lingua pedesca", P_IT, "ドイツ兵風の混成俗語で笑いを作る北伊詩。"),

    # Iberian chapbooks, pliegos, and theater edges
    ("プリーゴ・スエルト詩歌", "pliego suelto verse", "pliego suelto", P_IB, "一枚刷り小冊子で流通した俗謡・時事詩。"),
    ("ロマンセ・デ・シエゴ", "blind-bard romance sheets", "romance de ciego", P_IB, "盲人歌手が売った事件物語系ロマンセ刷物。"),
    ("ハカラの犯罪語り", "jacara criminal narration", "jacara", P_IB, "盗賊・牢獄語を歌謡化する黄金世紀の小ジャンル。"),
    ("モハランガ笑劇", "mojiganga farce", "mojiganga", P_IB, "仮装行列と滑稽踊りを混ぜる短い祝祭劇。"),
    ("エントレメスのサカリストン型", "sacristan type in entremes", "sacristan", P_IB, "小間劇で好色聖具係を笑う定番人物型。"),
    ("フェリシアーノ・デ・シルバ騎士道文体", "Feliciano de Silva chivalric style", "estilo silvesco", P_IB, "迂遠な恋愛修辞で騎士道本を過飾する文体。"),

    # French print miscellanies and courtly microforms
    ("カナール・サングラン", "sanglant canard", "canard sanglant", P_FR, "殺人・怪異を煽情的に報じる仏語小冊子。"),
    ("ノエル・ヌーヴォー集", "Noels nouveaux", "noels nouveaux", P_FR, "流行旋律に聖誕詞を載せる仏語宗教歌本。"),
    ("ブリュスクの宮廷滑稽", "Bruscambille court farce", "Bruscambille", P_FR, "前口上と下品な機知で劇場を温める笑芸散文。"),
    ("パレ・ド・ジュスティスのファルス", "Palais de Justice farce", "farce du Palais", P_FR, "法曹街の口論と訴訟語を笑うパリ小喜劇。"),
    ("リヨン派デヴィーズ詩", "Lyonnais devise poetry", "devise", P_FR, "標語・図像・短詩を組ませるリヨン周辺の宮廷詩。"),
    ("ブロドリー詩型", "broderie verse form", "broderie poetique", P_FR, "刺繍模様の反復に似せた恋愛短詩の装飾型。"),

    # English pamphlet, stage, and manuscript niches
    ("ステーションナーズ登録簿詩", "Stationers' Register verse", "Stationers' Register", P_EN, "出版登録簿に痕跡だけ残る英詩・小冊子群。"),
    ("ポールズ・クロス説教パンフレット", "Paul's Cross sermon pamphlets", "Paul's Cross sermons", P_EN, "野外説教を時事的印刷物へ変えた宗教散文。"),
    ("コンニーキャッチング小冊子", "coney-catching pamphlets", "coney-catching", P_EN, "都市詐欺の手口を暴露風に語るロンドン小冊子。"),
    ("ジグ終幕歌", "stage jig afterpiece", "jig", P_EN, "芝居後に歌と踊りで演じた卑俗な短い余興劇。"),
    ("子役劇団のブラックフライアーズ風刺", "Blackfriars boys' satire", "Blackfriars boys", P_EN, "少年劇団が上演した鋭い都市風刺喜劇。"),
    ("ミセラニー写本詩サークル", "manuscript miscellany coterie verse", "miscellany verse", P_EN, "私的写本で回覧された宮廷・地方の短詩群。"),

    # Northern, Neo-Latin, and Reformation print niches
    ("フルフトブレッター事件詩", "Flugblatt event verse", "Flugblatt", P_NO, "一枚刷りで災害・怪異・戦争を韻文化する独語詩。"),
    ("パスキル風宗教改革風刺", "Reformation pasquil satire", "Pasquill", P_NO, "匿名札文の形式で教皇派を攻撃する風刺印刷物。"),
    ("シュヴァンクブーフ小話", "Schwankbuch tales", "Schwankbuch", P_NO, "市民的機知と愚行を集める独語笑話本。"),
    ("ラテン学校プログラム劇", "Latin school program drama", "Schuldrama", P_NO, "学校行事用に印刷・上演された新ラテン語劇。"),
    ("レーデライケル室内リフレイン", "Rederijker refrain", "refrein", P_NO, "蘭語詩社が競作した脚韻反復の格言詩。"),
    ("グダニスク婚礼カルメン", "Danzig wedding carmen", "carmen nuptiale", P_NO, "都市人文主義者が婚礼に捧げたラテン機会詩。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise ValueError("expected 30 concepts")
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            before = db.find_concept(name_ja, REGION, period_id)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
