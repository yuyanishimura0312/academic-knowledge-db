#!/usr/bin/env python3
"""Wave 38 C08: lit_eu_realism extra 30 niche concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_eu_realism"
REGION = "西欧"

# (name_ja, name_en, name_original, period_id, definition)
CONCEPTS = [
    # 1. French minor realism and documentary urban prose
    ("シャンフルーリ『モランシャールのブルジョワ』", "Champfleury, The Bourgeois of Molinchart", "Les Bourgeois de Molinchart", 120, "地方ブルジョワの日常的偽善を滑稽に観察するフランス小説。"),
    ("デュランティ『美男ギヨームの事件』", "Duranty, The Case of Handsome Guillaume", "La Cause du beau Guillaume", 120, "法廷調書風の語りで欲望と階級摩擦を描く実験的リアリズム。"),
    ("ミュルジェ『ボエーム生活の情景』", "Murger, Scenes of Bohemian Life", "Scènes de la vie de bohème", 120, "貧しい芸術家共同体を逸話連作で描く都市風俗リアリズム。"),
    ("エルクマン＝シャトリアン地方年代記", "Erckmann-Chatrian provincial chronicles", "récits provinciaux", 120, "アルザス農村と小市民の記憶を民衆語りで記録する連作群。"),
    ("ヴィクトール・シェルビュリエ社交小説", "Victor Cherbuliez society novel", "roman mondain", 120, "国際社交界の結婚市場と財産戦略を分析する中間的リアリズム。"),
    ("アンリ・セアール『ユヌ・ベル・ジュルネ』", "Henry Céard, A Fine Day", "Une belle journée", 122, "郊外の一日を反英雄的細部で解体するメダン派自然主義小説。"),
    # 2. British and Irish lesser-known realist forms
    ("オリファント『カーリングフォード年代記』", "Oliphant, Chronicles of Carlingford", "Chronicles of Carlingford", 121, "牧師館と地方町を通じて女性知性と教会政治を描く連作。"),
    ("ミセス・ヘンリー・ウッド『イースト・リン』", "Mrs Henry Wood, East Lynne", "East Lynne", 121, "家庭秘密と法的身分喪失を絡めるセンセーション小説。"),
    ("ジョージ・ムーア『エスター・ウォーターズ』", "George Moore, Esther Waters", "Esther Waters", 122, "女中の妊娠と競馬社会を自然主義的に描く英国小説。"),
    ("ギッシング『三文文士』", "Gissing, New Grub Street", "New Grub Street", 121, "文壇市場で消耗する作家労働を描く出版業リアリズム。"),
    ("ベサント『あらゆる境遇の人々』", "Besant, All Sorts and Conditions of Men", "All Sorts and Conditions of Men", 121, "イーストエンド改良と慈善の限界を小説化する社会派作品。"),
    ("サマヴィル＆ロス『アイルランドのRM』", "Somerville and Ross, Irish R.M.", "Some Experiences of an Irish R.M.", 121, "地主制末期の地方行政を滑稽な観察で描くアングロ・アイリッシュ連作。"),
    # 3. German, Austrian, and Swiss poetic realism margins
    ("シュピールハーゲン『問題的本性』", "Spielhagen, Problematic Natures", "Problematische Naturen", 173, "自由主義世代の政治的挫折を分析するドイツ問題小説。"),
    ("フライターク『借方と貸方』", "Freytag, Debit and Credit", "Soll und Haben", 173, "商業倫理と国民経済を教育小説化した市民リアリズム。"),
    ("アンツェングルーバー民衆劇", "Anzengruber folk drama", "Volksstück", 173, "村落共同体の迷信、貧困、宗教対立を舞台化するオーストリア劇。"),
    ("フェルディナント・フォン・ザール短編", "Ferdinand von Saar novellas", "Novellen", 173, "帝都周縁の没落貴族と官僚を抑制的に描く短編群。"),
    ("エーブナー＝エッシェンバッハ城館小説", "Ebner-Eschenbach estate fiction", "Schlossgeschichten", 173, "モラヴィア貴族社会の階級倫理を女性視点で描く散文。"),
    ("ペーター・ローゼッガー『森の故郷』", "Peter Rosegger, Forest Homeland", "Waldheimat", 173, "シュタイアーマルク農村の記憶を素朴語りで保存する散文群。"),
    # 4. Italian verismo and post-verismo niches
    ("マティルデ・セラーオ『ナポリの腹』", "Matilde Serao, The Belly of Naples", "Il ventre di Napoli", 171, "ナポリ貧民街を新聞調査と感傷で描く都市ルポ散文。"),
    ("デ・ロベルト『言語資料』", "De Roberto, Verbal Proceedings", "Processi verbali", 171, "証言録風の短編でシチリア社会の利害を露出するヴェリズモ。"),
    ("レナート・フチーニ『ネーリの夜話』", "Renato Fucini, Neri's Evening Tales", "Le veglie di Neri", 171, "トスカーナ農民の語り口で地方生活を記録する短編集。"),
    ("マリオ・プラテージ『遺産』", "Mario Pratesi, The Inheritance", "L'eredità", 171, "相続と家父長制の重圧を地方家庭に凝縮するイタリア小説。"),
    ("ネーラ『テレーザ』", "Neera, Teresa", "Teresa", 171, "北イタリア女性の結婚拘束と沈黙を内面から描く小説。"),
    ("ロヴェッタ『母なる悲しみ』", "Gerolamo Rovetta, Mater dolorosa", "Mater dolorosa", 171, "家庭メロドラマを社会的体面の批判へ転じる後期ヴェリズモ。"),
    # 5. Iberian, Portuguese, Nordic, and Dutch regional realism
    ("オリェール『黄金熱』", "Narcís Oller, Gold Fever", "La febre d'or", 172, "バルセロナ投機熱と新興ブルジョワを描くカタルーニャ小説。"),
    ("パラシオ・バルデス『マルタとマリア』", "Palacio Valdés, Marta y María", "Marta y María", 172, "信仰と結婚選択を地方家庭に置くスペイン写実小説。"),
    ("フィアルリョ・デ・アルメイダ『猫たち』", "Fialho de Almeida, The Cats", "Os Gatos", 172, "都市観察と毒舌風刺を混ぜるポルトガル散文スケッチ。"),
    ("トリンダーデ・コエーリョ『わが恋人たち』", "Trindade Coelho, My Loves", "Os meus amores", 172, "トラス・オス・モンテスの村落記憶を叙情的写実で描く短編集。"),
    ("アマリエ・スクラム『ヘレミュールの人々』", "Amalie Skram, People of Hellemyr", "Hellemyrsfolket", 121, "貧困と遺伝を家族サーガ化するノルウェー自然主義小説。"),
    ("クペールス『エリーネ・フェーレ』", "Couperus, Eline Vere", "Eline Vere", 121, "ハーグ上流社会の倦怠と神経症を描くオランダ自然主義。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: definition too long"
            before = db.find_concept(name_ja, REGION, period_id)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if before is None and cid:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=5"
        ).fetchone()[0]
    print(f"inserted={inserted} total={total}")


if __name__ == "__main__":
    main()
