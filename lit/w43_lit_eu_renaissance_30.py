#!/usr/bin/env python3
"""Wave 43: 30 ultra-niche European Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian novella, comedy, and pastoral margins
    ("グラッツィーニ『夕食会』", "Grazzini, The Suppers", "Le cene", P_IT, "フィレンツェ市井の悪戯譚を重ねる晩餐枠物語。"),
    ("ビビエーナ『カランドリア』", "Bibbiena, Calandria", "La Calandria", P_IT, "双子取り違えを俗語散文喜劇へ移した宮廷劇。"),
    ("マキャヴェリ『マンドラーゴラ』", "Machiavelli, Mandragola", "La Mandragola", P_IT, "欲望と欺瞞を精密に組むフィレンツェ喜劇。"),
    ("ドルチェ『マリアンナ』", "Lodovico Dolce, Marianna", "Marianna", P_IT, "ヘロデ王家の嫉妬を扱うイタリア語悲劇。"),
    ("グアリーニ『忠実な牧人』", "Guarini, Il pastor fido", "Il pastor fido", P_IT, "悲喜劇論争を招いた宮廷牧歌劇の代表作。"),
    ("バンデッロ『ノヴェッレ』写本流通", "Bandello manuscript circulation", "Novelle", P_IT, "献辞付き短編が宮廷ネットワークで巡る受容形態。"),

    # French farce, pamphlet, and minor poetics
    ("グランゴール『愚者の王』", "Gringore, Prince of Fools", "Le Prince des Sots", P_FR, "愚者劇で教皇政治を諷すパリ祝祭演劇。"),
    ("ラリヴェ『幽霊』", "Larivey, Les Esprits", "Les Esprits", P_FR, "イタリア喜劇を仏語都市喜劇へ翻案した作。"),
    ("ベーズ『アブラハムの犠牲』", "Beza, Abraham sacrifiant", "Abraham sacrifiant", P_FR, "改革派信仰を仏語聖書悲劇にした作品。"),
    ("シャルル・フォンテーヌ『恋の矛盾』", "Charles Fontaine, Contr'amours", "Contr'amours", P_FR, "反ペトラルカ的機知で恋愛詩を反転する小詩集。"),
    ("マニー『ため息集』", "Olivier de Magny, Soupirs", "Les Soupirs", P_FR, "ローマ滞在経験を恋愛詩に織る宮廷詩集。"),
    ("ルイ・ル・カロン『対話篇』", "Louis Le Caron dialogues", "Dialogues", P_FR, "法服貴族の教養を示す仏語哲学対話集。"),

    # Iberian theatre, print, and devotional microgenres
    ("ロペ・デ・ルエダ『パソス』", "Lope de Rueda pasos", "Pasos", P_IB, "旅役者の短い幕間喜劇を集めた初期商業劇。"),
    ("アロンソ・デ・レデスマ『霊的コンセプトス』", "Ledesma, Spiritual Concepts", "Conceptos espirituales", P_IB, "機知表現を信仰詩へ転用する初期コンセプティスモ。"),
    ("ビルエス『モンセラーテ』", "Cristobal de Virues, Monserrate", "El Monserrate", P_IB, "聖山伝説を叙事詩化したスペイン宗教詩。"),
    ("コバルビアス『スペイン語宝庫』", "Covarrubias, Tesoro", "Tesoro de la lengua castellana", P_IB, "語源解釈を文学引用で支える初期西語辞書。"),
    ("エスピネル『マルコス・デ・オブレゴン』", "Espinel, Marcos de Obregon", "Marcos de Obregon", P_IB, "回想体で遍歴人生を語る後期ピカレスク小説。"),
    ("セルバンテス『パルナソ山への旅』", "Cervantes, Journey to Parnassus", "Viaje del Parnaso", P_IB, "同時代詩人を風刺的に評する韻文旅行記。"),

    # English rhetoric, pamphlet wars, and stage documents
    ("ウィルソン『修辞術』", "Thomas Wilson, Arte of Rhetorique", "The Arte of Rhetorique", P_EN, "英語散文で古典修辞を教える初期手引書。"),
    ("プットナム『英詩技法』", "Puttenham, Art of English Poesy", "The Arte of English Poesie", P_EN, "宮廷詩作の比喩・韻律・装飾を体系化した詩論。"),
    ("ガスコイン『詩作覚書』", "Gascoigne, Certayne Notes", "Certayne Notes of Instruction", P_EN, "英語詩作の実用規則を示す短い作詩論。"),
    ("ハーヴェイ＝ナッシュ筆戦", "Harvey-Nashe pamphlet quarrel", "Harvey-Nashe quarrel", P_EN, "大学才人の罵倒散文が競う一五九〇年代小冊子論争。"),
    ("マーティン・マープレレイト小冊子", "Marprelate tracts", "Martin Marprelate tracts", P_EN, "匿名の反主教風刺が地下印刷で流通したパンフレット群。"),
    ("ヘンスロー日記の上演記録", "Henslowe's Diary performance records", "Henslowe's Diary", P_EN, "ロンドン劇場の日銭と演目を残す興行台帳。"),

    # Northern humanist school drama and burgher prose
    ("マクロペディウス『ヘカストゥス』", "Macropedius, Hecastus", "Hecastus", P_NO, "万人劇を人文主義学校劇に改作したラテン戯曲。"),
    ("クロクス『ヨセフ』", "Cornelius Crocus, Joseph", "Joseph", P_NO, "ヨセフ物語を教室上演向けに整えたラテン劇。"),
    ("フィシャルト『幸運の船』", "Fischart, Das Gluckhafft Schiff", "Das Gluckhafft Schiff", P_NO, "市民祝祭を長詩化したシュトラスブルク航行詩。"),
    ("ヴィックラム『金の糸』", "Jorg Wickram, Goldthread", "Der Goldtfaden", P_NO, "都市読者向けに徳と結婚を語る初期ドイツ散文小説。"),
    ("リンゲルベルク『文学遊戯』", "Ringelbergius literary exercises", "Lucubrationes", P_NO, "知識分類と文体訓練を結ぶ北方人文主義小品。"),
    ("ムルネル『大ルター派愚者』", "Murner, Great Lutheran Fool", "Von dem grossen Lutherischen Narren", P_NO, "宗教改革論争を阿呆文学の形式で攻撃した諷刺。"),
]


def main() -> None:
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
