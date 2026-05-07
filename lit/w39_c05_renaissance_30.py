#!/usr/bin/env python3
"""Wave 39 C05: 30 ultra-niche Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian microgenres and forgotten works
    ("ジュリオ・カミッロ『記憶劇場』", "Giulio Camillo Theatre of Memory", "L'Idea del Theatro", P_IT, "記憶術を劇場模型で体系化した秘教的人文主義書。"),
    ("テオフィロ・フォレンゴ『バルドゥス』", "Teofilo Folengo Baldus", "Baldus", P_IT, "俗語とラテン語を混ぜる滑稽叙事詩。"),
    ("フォレンゴ風マッケロニ詩", "Folengan macaronic verse", "poesia maccheronica", P_IT, "ラテン語形態に俗語語彙を混ぜる諧謔詩法。"),
    ("アンニーバレ・カーロ『アエネーイス』訳", "Annibale Caro Aeneid translation", "Eneide", P_IT, "無韻十一音節詩で古典叙事詩を俗語化した訳業。"),
    ("ルイジ・グロート『ハドリアーナ』", "Luigi Groto Hadriana", "Hadriana", P_IT, "盲目詩人グロートによるヴェネツィア悲劇。"),
    ("イザベラ・アンドレイニ『ミルティッラ』", "Isabella Andreini Mirtilla", "Mirtilla", P_IT, "女性役者が書いた牧歌劇の稀少例。"),

    # French minor court and religious forms
    ("セビエ『マルグリット・ポエティック』", "Sceve Marguerite Poetique", "Marguerite Poetique", P_FR, "リヨン派周辺の女性的寓意詩集。"),
    ("ラ・セペード『神聖定理』", "La Ceppede Sacred Theorems", "Theoremes spirituels", P_FR, "受難を瞑想する膨大な宗教ソネット連作。"),
    ("フィリップ・デポルト宮廷詩", "Philippe Desportes court lyric", "poesies", P_FR, "アンリ三世宮廷で流行した洗練恋愛詩。"),
    ("パスラ『モノフィル』", "Pasquier Monophile", "Le Monophile", P_FR, "法曹人文主義者による恋愛対話の小品。"),
    ("タユロー『ラ・トレカレ』", "Taillemont La Tricarite", "La Tricarite", P_FR, "女性三美神をめぐるリヨン派的対話篇。"),
    ("ヴォークラン『フランス詩法』", "Vauquelin Art poetique francais", "Art poetique francais", P_FR, "地方貴族が編んだ後期ルネサンス詩法書。"),

    # Iberian and Portuguese marginal Renaissance
    ("ヒル・ビセンテ『イネス・ペレイラ』", "Gil Vicente Ines Pereira", "Farsa de Ines Pereira", P_IB, "ポルトガル民衆喜劇の機知ある結婚風刺。"),
    ("サー・デ・ミランダ『書簡』", "Sa de Miranda Epistles", "Cartas", P_IB, "イタリア詩形をポルトガル語に移した書簡詩。"),
    ("カスティリェホ反イタリア詩", "Castillejo anti-Italian verse", "Contra los que dejan", P_IB, "伝統カスティーリャ詩形を擁護する論争詩。"),
    ("トレス・ナアロ『プロパラディア』", "Torres Naharro Propalladia", "Propalladia", P_IB, "スペイン初期演劇理論を含む劇作集。"),
    ("エルシーリャ『アラウカーナ』", "Ercilla La Araucana", "La Araucana", P_IB, "チリ征服戦争を八行詩で叙事化した作品。"),
    ("バラオナ・デ・ソト『アンヘリカの涙』", "Barahona de Soto Tears of Angelica", "Las lagrimas de Angelica", P_IB, "アリオスト後日譚をスペイン語叙事詩化した作。"),

    # English and Scottish overlooked print culture
    ("ジョージ・ガスコイン『鋼の鏡』", "Gascoigne Steel Glass", "The Steele Glas", P_EN, "英語初期の無韻詩風刺長詩。"),
    ("バーナビー・リッチ『軍務告別』", "Barnabe Rich Farewell", "Farewell to Military Profession", P_EN, "シェイクスピア材源を含む軍人ロマンス集。"),
    ("メアリ・ロウス『ウラニア』", "Mary Wroth Urania", "Urania", P_EN, "女性作者による散文ロマンスの大作。"),
    ("サミュエル・ダニエル『デリア』", "Samuel Daniel Delia", "Delia", P_EN, "シドニー後の端正な英語ソネット連作。"),
    ("マイケル・ドレイトン『ポリオルビオン』", "Drayton Poly-Olbion", "Poly-Olbion", P_EN, "英国地誌を擬人化して歌う長大詩。"),
    ("ウィリアム・ドラモンド『サイプレスの森』", "Drummond Cypress Grove", "A Cypresse Grove", P_EN, "スコットランド詩人の死と霊魂をめぐる散文瞑想。"),

    # Northern and Low Countries niche humanism
    ("ゲオルク・ロレンハーゲン『ラテン寸劇』", "Georg Rollenhagen Latin school drama", "Acolastus", P_NO, "学校劇として読まれた放蕩息子劇の変種。"),
    ("ニコデムス・フリシュリン『レベッカ』", "Nicodemus Frischlin Rebecca", "Rebecca", P_NO, "聖書題材を学校演劇化したラテン劇。"),
    ("ヨハネス・セクンドゥス『接吻詩』", "Johannes Secundus Basia", "Basia", P_NO, "ネオラテン恋愛詩の接吻主題連作。"),
    ("ヘンドリック・ラウレンスゾーン・スピーゲル『心鏡』", "Spieghel Hertspiegel", "Hertspiegel", P_NO, "オランダ語で徳倫理を詩化した教訓詩。"),
    ("ヤン・ファン・デル・ノート『劇場』", "Jan van der Noot Theatre", "Het Theatre", P_NO, "黙示録的図像と詩を結ぶネーデルラント作品。"),
    ("ユストゥス・リプシウス『恒心論』", "Justus Lipsius On Constancy", "De constantia", P_NO, "ストア派倫理を戦乱期人文主義へ再編した対話篇。"),
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
