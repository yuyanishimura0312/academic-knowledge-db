from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Insular manuscript micro-traditions
    ("『ヴェルチェリ書』説教詩群", "Vercelli Book homiletic poems", "Vercelli Book", 115, "古英語写本に残る説教的詩群"),
    ("『ブリックリング説教集』終末説教", "Blickling homilies on apocalypse", "Blickling Homilies", 115, "終末論を強調する古英語散文説教"),
    ("『ユニウス写本』創世記B断片", "Junius Genesis B fragment", "Genesis B", 115, "古英語創世記詩中の異系統断片"),
    ("『ヴェルチェリ書』聖アンドレアス詩", "Andreas in the Vercelli Book", "Andreas", 115, "使徒行伝を英雄詩化した古英語詩"),
    ("『エクセター書』デオール", "Deor in the Exeter Book", "Deor", 115, "宮廷歌人の失職を語る古英語短詩"),
    ("『エクセター書』妻の嘆き", "The Wife's Lament", "The Wife's Lament", 115, "女性声の離別を語る古英語悲歌"),
    # 2. Occitan and Catalan minor forms
    ("エンスニャメン（オック語教訓詩）", "ensenhamen", "ensenhamen", 214, "礼法や恋愛を説くオック語教訓詩"),
    ("サリュ・ダモール（恋文詩）", "salut d'amor", "salut d'amor", 214, "恋文形式で作るオック語叙情詩"),
    ("アルバ（夜明け別れ歌）異本群", "alba variants", "alba", 214, "夜明けの別離を歌うオック語小形式"),
    ("マラルティア・ダモール（恋の病詩）", "malautia d'amor", "malautia d'amor", 214, "恋の病を診断するオック語詩型"),
    ("カンソ・デ・クロワザーダ小枝群", "minor crusade canso", "canso de crozada", 214, "十字軍を扱う周縁的オック語歌"),
    ("ラモン・ヴィダル『アブリル・イシア』", "Ramon Vidal's Abril issia", "Abril issia", 214, "宮廷詩論を物語化したオック語作品"),
    # 3. Medieval Latin schoolroom and parody
    ("『ファセトゥス』礼法詩", "Facetus conduct poem", "Facetus", 219, "学校で読まれたラテン語礼法詩"),
    ("『ドクトリナーレ』韻文文法", "Doctrinale", "Doctrinale puerorum", 219, "中世学校用のラテン語韻文文法"),
    ("『グレキスムス』文法詩", "Graecismus", "Graecismus", 219, "語源と文法を扱うラテン語教科詩"),
    ("『バビオ』喜劇", "Babio", "Babio", 219, "聖職者家庭を諷刺するラテン喜劇"),
    ("『アルド』ラテン喜劇", "Alda", "Alda", 219, "古典喜劇を模す中世ラテン劇"),
    ("『モレトゥム』中世受容", "medieval Moretum reception", "Moretum", 219, "農民食詩の中世写本的受容"),
    # 4. Iberian peripheral manuscript traditions
    ("『リブラ・デ・トレス・レイス・ドリエン』", "Libre de tres reys d'Orient", "Libre de tres reys d'Orient", 215, "東方三博士を扱う短いカスティーリャ詩"),
    ("『聖マリア・エヒプシアカ伝』", "Vida de Santa Maria Egipciaca", "Vida de Santa Maria Egipciaca", 215, "悔悛聖女伝を語るイベリア詩"),
    ("『ラソン・デ・アモール』", "Razon de amor", "Razon de amor", 215, "愛と水の寓意をもつカスティーリャ短詩"),
    ("『ディスプタ・デル・アルマ・イ・エル・クエルポ』", "Disputa del alma y el cuerpo", "Disputa del alma y el cuerpo", 215, "魂と身体の論争を描くカスティーリャ詩"),
    ("『ロンスヴァリェス断片』", "Roncesvalles fragment", "Roncesvalles", 215, "ロラン伝承のカスティーリャ語断片"),
    ("『ユーセフの詩』アルハミアード版", "Poema de Yuçuf", "Poema de Yuçuf", 215, "アラビア文字カスティーリャ語のユースフ物語"),
    # 5. Germanic, Norse, and Slavic marginal texts
    ("『メーレンの王オルレンデル』", "King Orendel", "Orendel", 216, "聖衣伝承を含む中高ドイツ語物語"),
    ("『ザルマンとモロルフ』", "Salman und Morolf", "Salman und Morolf", 216, "ソロモン伝承の中高ドイツ語滑稽物語"),
    ("『リヴォニア韻文年代記』", "Livonian Rhymed Chronicle", "Livlandische Reimchronik", 216, "バルト十字軍を叙す中高ドイツ語年代記"),
    ("『テオドリクス・サガ』", "Thidrekssaga", "Thidrekssaga", 218, "ディートリヒ伝承を集成した古ノルド散文"),
    ("『聖オーラヴルの古サガ』", "Oldest Saga of Saint Olaf", "Elsta saga Olafs helga", 218, "聖王オーラヴル伝の最古層サガ"),
    ("『ザドンシチナ』", "Zadonshchina", "Zadonshchina", 220, "クリコヴォ戦勝を歌う中世ルーシ文学"),
]


def exists_in_subfield(db: LitDB, name_ja: str) -> bool:
    row = db.conn.execute(
        "SELECT 1 FROM concepts WHERE subfield_id = 2 AND name_ja = ? LIMIT 1",
        (name_ja,),
    ).fetchone()
    return row is not None


def main() -> None:
    with LitDB("lit.sqlite") as db:
        inserted = 0
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            if exists_in_subfield(db, name_ja):
                raise ValueError(f"already present in subfield 2: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code="lit_eu_medieval",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
        print(f"inserted {inserted} concepts")


if __name__ == "__main__":
    main()
