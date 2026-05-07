#!/usr/bin/env python3
"""Wave 41: add 30 hyper-niche lit_eu_modernism concepts."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_eu_modernism"
REGION = "西欧"
PERIOD_ID = 22

CONCEPTS = [
    # Cluster 1: イベリア周縁モダニズム
    ("ペレス・デ・アヤラ『ベラルミーノとアポロニオ』", "Perez de Ayala, Belarmino y Apolonio", "Belarmino y Apolonio", "latin", "対話小説形式で哲学と地方俗語を衝突させるスペイン長篇。"),
    ("ガブリエル・ミロ『われらの父聖ダニエル』", "Gabriel Miro, Nuestro Padre San Daniel", "Nuestro Padre San Daniel", "latin", "感覚描写で地方信仰共同体の硬直を細密化する小説。"),
    ("ベンハミン・ハルネス『霧の街』", "Benjamin Jarnes, Locura y muerte de nadie", "Locura y muerte de nadie", "latin", "脱人格化された都市主体を描くスペイン前衛小説。"),
    ("カルネイロ『ルシオの告白』", "Sa-Carneiro, Lucio's Confession", "A Confissao de Lucio", "latin", "分身と芸術家幻想を交差させるポルトガル短篇小説。"),
    ("ジョゼ・レジオ『神と悪魔の詩』", "Jose Regio, Poems of God and the Devil", "Poemas de Deus e do Diabo", "latin", "信仰と肉体の緊張を劇化するプレゼンサ派詩集。"),
    ("ビセンテ・リスコ『豚足男』", "Vicente Risco, O porco de pe", "O porco de pe", "latin", "ガリシア都市俗物を怪物的寓話にした風刺小説。"),
    # Cluster 2: 北欧・バルト海小モダニズム
    ("エルメル・ディクトニウス『硬い歌』", "Elmer Diktonius, Hard Songs", "Harda sanger", "latin", "フィンランド瑞語で機械的リズムを刻む労働者前衛詩。"),
    ("ヘンリク・ティッカネン『ブロンディの家』", "Henry Parland, To Pieces", "Sonder", "latin", "広告・写真・断片で若者文化を組むフィンランド瑞語小説。"),
    ("ラグナル・ルードベリ『バラバ』", "Par Lagerkvist, Barabbas", "Barabbas", "latin", "救済の空白を冷たい寓話へ圧縮したスウェーデン小説。"),
    ("カリン・ボイェ『カロカイン』初期読解", "Karin Boye, Kallocain", "Kallocain", "latin", "監視国家を内面独白の恐怖として描く北欧ディストピア。"),
    ("シーグルズル・ノルダル『ヘルギの一生』", "Sigurdur Nordal, Hel", "Hel", "latin", "サガ語りを心理的断章へ変えるアイスランド小説。"),
    ("ヨハネス・ウル・ケートルム『自己の家』", "Johannes ur Kotlum, poetry", "Sjodandi dagar", "latin", "民衆詩の韻律を社会主義的都市感覚へずらす詩。"),
    # Cluster 3: アルプス・少数語圏
    ("シャルル＝フェルディナン・ラミュ『アダムとイヴ』", "C. F. Ramuz, Adam et Eve", "Adam et Eve", "latin", "農村聖書劇を断続的語りで再構成するスイス小説。"),
    ("ブレーズ・サンドラール『黒人選集』", "Cendrars, Anthologie negre", "Anthologie negre", "latin", "収集民話を前衛的声の素材に変えた問題的アンソロジー。"),
    ("オスカー・ペル『ラディン語自由詩』", "Oscar Peer, Romansh modernism", "poesia ladina", "latin", "ロマンシュ語抒情を近代的自由詩へ開いた周縁実験。"),
    ("クルト・マルティ『ベルン方言詩』", "Kurt Marti, Bernese dialect poetry", "Barndutsch", "latin", "方言の短句で標準語文学の権威をずらすスイス詩。"),
    ("グスタフ・レネ・ホッケのマニエリスム論", "G. R. Hocke, Mannerism debate", "Manierismus", "latin", "前衛を反古典的マニエリスムとして再系譜化する批評。"),
    ("アルプス雑誌『デア・ブレンナー』後期圏", "Der Brenner late circle", "Der Brenner", "latin", "インスブルック誌面で神秘主義と前衛詩を媒介した圏域。"),
    # Cluster 4: 小雑誌・出版形式
    ("『ヴァルーリ・メカニーチェ』誌", "Integral circle, Valori Plastici", "Valori Plastici", "latin", "形而上絵画と文学的古典回帰をつなぐイタリア小誌。"),
    ("『900』誌の仏伊二言語モダン", "Novecento magazine", "900", "latin", "ボンテンペッリ周辺の魔術的リアリズムを国際化した誌面。"),
    ("『レスプリ・ヌーヴォー』詩欄", "L'Esprit Nouveau poetry pages", "L'Esprit Nouveau", "latin", "建築合理主義と詩的近代を同居させた仏語誌面。"),
    ("『ラセルバ』誌の前衛ナショナリズム", "La Selva magazine", "La Selva", "latin", "イタリア地方誌で未来派以後の政治美学を編んだ媒体。"),
    ("『アウディション』ベルリン誌圏", "Die Aktion literary circle", "Die Aktion", "latin", "反戦表現主義の短詩と政治評論を結合したベルリン誌。"),
    ("『パン』誌末期の新即物性", "Pan magazine late phase", "Pan", "latin", "装飾的世紀末誌が機械時代の簡潔さへ移る境界。"),
    # Cluster 5: 校訂・理論ミクロ論争
    ("ジョイス『フィネガンズ・ウェイク』ワークブック", "Finnegans Wake notebooks", "Wake notebooks", "latin", "語彙採集帳が多言語地層を生成する草稿群。"),
    ("ウルフ『波』タイプ稿異同", "Woolf, The Waves typescript variants", "The Waves typescripts", "latin", "声の切替と間奏部の配分を示すタイプ稿差異。"),
    ("ベケット『マーフィー』検閲削除", "Beckett, Murphy censorship cuts", "Murphy cuts", "latin", "猥雑語句の削除が初期散文の身体性を変える校訂論点。"),
    ("リルケ『マルテ』ノート断片", "Rilke Malte notebooks", "Malte-Aufzeichnungen", "latin", "都市恐怖の断章が小説構造へ変わる生成資料。"),
    ("ヴァレリー『カイエ』索引化問題", "Valery Cahiers indexing debate", "Cahiers", "latin", "膨大な断章を主題索引で読むか年代順で読むかの論点。"),
    ("カフカ『城』章題付与論争", "Kafka, The Castle chapter titles", "Das Schloss", "latin", "無題章への編集題名が未完小説の読解方向を左右する。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise SystemExit(f"expected 30 concepts, got {len(CONCEPTS)}")
    too_long = [(name, len(definition)) for name, *_rest, definition in CONCEPTS if len(definition) > 100]
    if too_long:
        raise SystemExit(f"definitions over 100 chars: {too_long}")

    inserted = 0
    with LitDB() as db:
        names = [name for name, *_ in CONCEPTS]
        placeholders = ",".join("?" for _ in names)
        existing = db.conn.execute(
            f"SELECT name_ja FROM concepts WHERE name_ja IN ({placeholders})",
            names,
        ).fetchall()
        if existing:
            raise SystemExit(f"existing concept names: {[row['name_ja'] for row in existing]}")

        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"INSERTED={inserted}")


if __name__ == "__main__":
    main()
