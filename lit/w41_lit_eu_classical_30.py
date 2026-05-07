#!/usr/bin/env python3
"""Wave 41: add 30 hyper-niche concepts to lit_eu_classical."""

from lit_db_helper import LitDB


ROWS = [
    # 1: Minor Greek lyric and local traditions
    ("アルカイオス政治断片", "Alcaeus political fragments", "Ἀλκαίου πολιτικά", "greek", 6, "レスボス内紛を歌う、党派的スタシス詩の断片群。"),
    ("テルパンドロス・ノモス伝承", "Terpander nomos tradition", "Τέρπανδρος νόμοι", "greek", 6, "レスボス系キタラ歌の創始をめぐる、音楽詩伝承。"),
    ("コリンナ『オレステス』断片", "Corinna Orestes fragments", "Κόριννα Ὀρέστης", "greek", 6, "ボイオティア神話を方言詩で語った女性詩人の断片。"),
    ("プラクシラのスコリオン", "Praxilla skolia", "Πράξιλλα σκόλια", "greek", 6, "宴席歌に神話的機知を折り込む、シキュオン詩人の断片。"),
    ("テレスティス賛歌断片", "Telestes hymn fragments", "Τελέστης ὕμνοι", "greek", 6, "新音楽期の技巧を伝える、ディテュランボス詩人の断片。"),
    ("プラティナスのサテュロス劇改革", "Pratinas satyr-play reform", "Πρατίνας σατυρικόν", "greek", 6, "合唱と笛伴奏の比重を争った、初期劇詩の小論点。"),
    # 2: Hellenistic microgenres and scholarly poetics
    ("ソータデス風イオニア詩", "Sotadean Ionic verse", "Σωτάδεια", "greek", 7, "猥雑なイオニア方言と逆走韻律で知られる小詩型。"),
    ("フェニックス『コロフォンの乞食』", "Phoenix Beggar of Colophon", "Πτωχός", "greek", 7, "キナイディック韻律で貧窮人物を描くヘレニズム小品。"),
    ("アレクサンドロス・アイトロス哀歌", "Alexander Aetolus elegies", "Ἀλέξανδρος Αἰτωλός", "greek", 7, "悲劇校訂者でもあった詩人の、学匠的エレゲイア断片。"),
    ("ヘルメシアナクス『レオンティオン』", "Hermesianax Leontion", "Λεόντιον", "greek", 7, "詩人たちの恋を列挙する、博識的恋愛エレゲイア。"),
    ("ディオニュシオス『鳥類誌』", "Dionysius Ixeutica", "Ἰξευτικά", "greek", 7, "鳥捕り知識を詩文化へ編む、希少な教訓詩断片。"),
    ("フィロステファノス島誌断片", "Philostephanus island fragments", "Περὶ νήσων", "greek", 7, "島々の神話由来を集める、地誌的アイティア散文。"),
    # 3: Roman minor and fragmentary works
    ("ネウィウス『ポエニ戦争』断片", "Naevius Bellum Punicum", "Bellum Punicum", "latin", 73, "ローマ史と神話起源を混ぜる、初期ラテン叙事詩断片。"),
    ("エンニウス悲劇『メデア』断片", "Ennius Medea fragments", "Medea exul", "latin", 73, "ギリシア悲劇を古ラテン語で移植した共和政劇断片。"),
    ("アッキウス『アトレウス』断片", "Accius Atreus fragments", "Atreus", "latin", 73, "暴君表象を濃縮する、共和政末期悲劇の断片。"),
    ("パクウィウス『アンティオペ』断片", "Pacuvius Antiope fragments", "Antiopa", "latin", 73, "哲学的語彙で知られる、古ラテン悲劇の断片作品。"),
    ("ルキリウス諷刺断片", "Lucilius satire fragments", "Lucilii Saturae", "latin", 73, "個人攻撃と会話体でラテン諷刺を固めた断片群。"),
    ("フリウス・ビバクルス『アイトナ』論争", "Furius Bibaculus Aetna debate", "Aetna", "latin", 73, "火山詩作者比定をめぐる、小叙事詩帰属論争。"),
    # 4: Late antique Greek prose, rhetoric, and chronicles
    ("リバニオス『エートポイイア』", "Libanius ethopoeiae", "Ἠθοποιίαι", "greek", 198, "神話人物の声を練習する、後期修辞学校の小課題集。"),
    ("コリキオス『エクフラシス』", "Choricius ekphraseis", "Ἐκφράσεις", "greek", 198, "ガザ修辞学校で磨かれた、絵画・建築描写の演習。"),
    ("ヒメリオス学校演説", "Himerius school orations", "Λόγοι", "greek", 198, "アテナイ修辞教育の祝辞・送辞を伝える演説群。"),
    ("テミスティオス皇帝演説", "Themistius imperial orations", "Βασιλικοὶ λόγοι", "greek", 198, "哲人弁論家が皇帝徳を調停する、政治演説群。"),
    ("エウナピオス『哲学者列伝』", "Eunapius Lives of Philosophers", "Βίοι φιλοσόφων", "greek", 198, "新プラトン派知識人を異教的視点で記す列伝。"),
    ("デキッポス『スキュティカ』断片", "Dexippus Scythica fragments", "Σκυθικά", "greek", 198, "ゴート侵入を古典語法で記録した三世紀史断片。"),
    # 5: Manuscript traditions and micro-debates
    ("ヴェネトゥスA『イリアス』ショリア", "Venetus A Iliad scholia", "Scholia Veneta A", "greek", None, "ホメロス本文批判を伝える、十世紀写本注釈層。"),
    ("D写本ホメロス神話注", "D-scholia mythographic notes", "Scholia D", "greek", None, "学校用に神話梗概を添えた、ホメロス注釈伝承。"),
    ("ウェルギリウス・ロマヌス写本", "Vergilius Romanus", "Codex Vaticanus lat. 3867", "latin", None, "挿絵付き古写本が伝える、ウェルギリウス受容資料。"),
    ("アンブロシアヌス・プラウトゥス写本", "Ambrosian Plautus palimpsest", "Ambrosianus G 82 sup.", "latin", None, "パリンプセストで残る、プラウトゥス本文の主要証人。"),
    ("オルフェウス金板文", "Orphic gold tablets", "χρύσεα ἐλάσματα", "greek", None, "死者への冥界指示を刻む、秘儀詩的短文伝承。"),
    ("キケロ『国家論』パリンプセスト", "Cicero Republic palimpsest", "De re publica palimpsestus", "latin", None, "失われた政治哲学書を再発見させた重写本。"),
]


def main() -> None:
    if len(ROWS) != 30:
        raise ValueError("expected 30 rows")

    with LitDB() as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts WHERE subfield_id = 1")
        }
        overlap = [row[0] for row in ROWS if row[0] in existing]
        if overlap:
            raise ValueError(f"already present: {overlap}")

        for name_ja, name_en, name_original, script, period_id, definition in ROWS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code="lit_eu_classical",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="primary",
                canonical_in_region="minor",
            )
    print("Inserted 30 lit_eu_classical concepts")


if __name__ == "__main__":
    main()
