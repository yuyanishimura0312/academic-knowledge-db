"""Wave 38: add 30 deep niche Indian literature concepts to lit_india."""

from lit_db_helper import LitDB

SUBFIELD = "lit_india"
REGION = "南アジア"


def period_id(db: LitDB, name_ja: str) -> int | None:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region=?",
        (name_ja, REGION),
    ).fetchone()
    return row["id"] if row else None


def main() -> None:
    with LitDB("lit.sqlite") as db:
        p = {
            "jaina": period_id(db, "ジャイナ文学期"),
            "poetics": period_id(db, "古典サンスクリット詩学期"),
            "bhakti": period_id(db, "中世バクティ・スーフィー期"),
            "urdu": period_id(db, "ウルドゥー近代詩・散文期"),
            "marginal": period_id(db, "インド・ダリット／女性文学期"),
        }
        concepts = [
            # Prakrit, Apabhramsha, Jaina narrative
            ("ガーハーサッタサイ", "Gaha Sattasai", "Gāhā Sattasaī", "prakrit", p["jaina"], "マハーラーシュトリー俗語の恋愛短詩集。", 3, "minor"),
            ("セトゥバンダ", "Setubandha", "Setubandha", "prakrit", p["jaina"], "プラヴァラセーナ作とされるプラークリット叙事詩。", 3, "minor"),
            ("パウマチャリヤ", "Paumacariya", "Paumacariya", "prakrit", p["jaina"], "ラーマ物語をジャイナ教的に再構成した叙事詩。", 3, "minor"),
            ("クヴァラヤマーラー", "Kuvalayamala", "Kuvalayamālā", "prakrit", p["jaina"], "俗語混交で都市生活を描くジャイナ物語集。", 2, "marginal"),
            ("アパブランシャ・ドーハー", "Apabhramsha doha", "Apabhraṃśa dohā", "devanagari", p["jaina"], "後期中期インド語の二行詩形式。", 3, "minor"),
            ("ラーサ文学", "Rasa literature", "Rāsa", "devanagari", p["jaina"], "グジャラート周辺のジャイナ物語詩ジャンル。", 2, "marginal"),
            # Sanskrit poetics and formal devices
            ("アヌマーナ派詩論", "Anumana school of poetics", "anumāna", "devanagari", p["poetics"], "詩的意味を推論作用から説明する詩論系譜。", 2, "marginal"),
            ("スフォータ詩学", "Sphota poetics", "sphoṭa", "devanagari", p["poetics"], "語の全体的発現を詩的意味に結びつける考え。", 3, "minor"),
            ("チトラカーヴィヤ", "Citra-kavya", "citrakāvya", "devanagari", p["poetics"], "文字配置や視覚技巧を重んじる装飾詩。", 3, "minor"),
            ("ヤマカ", "Yamaka", "yamaka", "devanagari", p["poetics"], "同音反復で多重の意味や響きを作る修辞。", 3, "minor"),
            ("シレーシャ", "Shlesha", "śleṣa", "devanagari", p["poetics"], "一語句に複数の意味を重ねる掛詞的技法。", 3, "minor"),
            ("プラバンダ・カーヴィヤ", "Prabandha kavya", "prabandha-kāvya", "devanagari", p["poetics"], "章立てされた物語性の強いサンスクリット詩。", 3, "minor"),
            # South Indian devotional and mixed-language forms
            ("カライッカール・アンマイヤール詩", "Karaikkal Ammaiyar poetry", "Kāraikkāl Ammaiyār", "tamil", p["bhakti"], "初期タミル・シヴァ派女性聖者の幻視詩。", 3, "minor"),
            ("シッダル詩", "Tamil Siddhar poetry", "cittar pāṭal", "tamil", p["bhakti"], "身体・錬金術・反制度性を歌うタミル神秘詩。", 3, "minor"),
            ("ヴィーラシャイヴァ・ヴァチャナ", "Virashaiva vachana", "vacana", "kannada", p["bhakti"], "カンナダ語の短い散文詩的シヴァ信仰表現。", 3, "minor"),
            ("アッカ・マハーデーヴィー・ヴァチャナ", "Akka Mahadevi vachana", "Akka Mahadevi vacana", "kannada", p["bhakti"], "女性聖者による身体放棄と神愛のヴァチャナ。", 3, "minor"),
            ("カンナダ・シャンパー", "Kannada champu", "campu", "kannada", p["bhakti"], "韻文と散文を交える古カンナダ宮廷文体。", 2, "marginal"),
            ("マニプラヴァーラム", "Manipravalam", "maṇipravāḷam", "malayalam", p["bhakti"], "サンスクリットと地域語を混用する南インド文体。", 3, "minor"),
            # Urdu, Deccani, and Persianate genres
            ("ダカニー文学", "Dakhani literature", "Dakhani", "arabic", p["urdu"], "デカン地方で発達した初期ウルドゥー文学。", 3, "minor"),
            ("サブ・ラス", "Sab Ras", "Sab Ras", "arabic", p["urdu"], "ダカニー散文ロマンスの代表的初期作品。", 2, "marginal"),
            ("レーフティー", "Rekhti", "rekhtī", "arabic", p["urdu"], "女性語りを模したウルドゥー詩の特異なジャンル。", 3, "minor"),
            ("シャフル・アーショーブ", "Shahr-ashob", "shahr-āshob", "arabic", p["urdu"], "都市の衰退や職人社会を嘆くペルシア系詩型。", 3, "minor"),
            ("マルシヤー", "Marsiya", "mars̱iyah", "arabic", p["urdu"], "カルバラー追悼を中心とするウルドゥー哀歌。", 3, "minor"),
            ("キッサ・ダースターン印刷本", "Qissa-Dastan chapbooks", "qiṣṣa-dāstān", "arabic", p["urdu"], "北インドで流通した安価な物語印刷本。", 2, "marginal"),
            # Northeastern, Adivasi, and small-language modernities
            ("ミゾ口承詩", "Mizo oral poetry", "Mizo hla", "roman", p["marginal"], "ミゾ社会の歌謡・戦士伝承に根ざす口承詩。", 2, "marginal"),
            ("ボド語バトウ文学", "Bodo Bathou literature", "Bathou", "devanagari", p["marginal"], "ボドのバトウ信仰を背景にした詩と物語。", 2, "marginal"),
            ("サンタル語オル・チキ文学", "Santali Ol Chiki literature", "Ol Chiki", "ol_chiki", p["marginal"], "オル・チキ文字で展開したサンタル語近代文学。", 3, "minor"),
            ("コクボロク現代詩", "Kokborok modern poetry", "Kokborok", "roman", p["marginal"], "トリプラのコクボロク語による現代詩運動。", 2, "marginal"),
            ("ナガ英語詩", "Naga English poetry", "Naga English poetry", "roman", p["marginal"], "ナガランドの記憶と紛争を英語で書く詩群。", 2, "marginal"),
            ("マラヤーラム小雑誌運動", "Malayalam little magazine movement", "little magazine", "malayalam", p["marginal"], "ケーララで実験詩と批評を支えた小雑誌文化。", 2, "marginal"),
        ]

        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=12"
        ).fetchone()[0]
        inserted = 0
        for name_ja, name_en, name_original, script, pid, definition, importance, canonical in concepts:
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=pid,
                definition=definition,
                importance_score=importance,
                source_tier="secondary",
                canonical_in_region=canonical,
            )
            inserted += 1 if cid else 0
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=12"
        ).fetchone()[0]
        print(f"inserted_attempted={inserted} before={before} after={after} added={after-before}")


if __name__ == "__main__":
    main()
