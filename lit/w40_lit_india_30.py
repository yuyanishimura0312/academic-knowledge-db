"""Wave 40: add 30 hyper-niche concepts to lit_india."""

from lit_db_helper import LitDB

SUBFIELD = "lit_india"
REGION = "南アジア"


CONCEPTS = [
    # Assamese, Manipuri, and northeastern manuscript cultures
    ("ブラジャーブリー・アンキヤ・ナート", "Brajavali Ankiya Naat", "Brajavali ankiya naat", "assamese", "アッサムの単幕宗教劇で用いられた混成文語。"),
    ("アッサム・ブランジ散文", "Assamese Buranji prose", "buranji", "assamese", "アホム王国年代記に発達したアッサム散文。"),
    ("メイテイ・プヤ写本", "Meitei Puya manuscripts", "puya", "meitei_mayek", "マニプルの宗教・王統知識を伝える写本群。"),
    ("『チェイタロル・クンババ』", "Cheitharol Kumbaba", "Cheitharol Kumbaba", "meitei_mayek", "マニプル王権の出来事を記すメイテイ年代記。"),
    ("カシ語キンティ伝承詩", "Khasi Kynti oral verse", "kynti", "roman", "カーシ丘陵で歌われる系譜的な口承詩。"),
    ("レプチャ語ナムタル", "Lepcha namthar", "namthar", "lepcha", "シッキム周辺の聖者伝を語るレプチャ文芸。"),
    # Jain, Prakrit, and Apabhramsha micro-traditions
    ("『サマライッチャカハー』", "Samarāiccakahā", "Samarāiccakahā", "prakrit", "ハリバドラ作のジャイナ説話的プラークリット物語。"),
    ("ジャイナ・パッターヴァリー", "Jain pattavali", "paṭṭāvalī", "devanagari", "僧統譜を記すジャイナ教団の系譜文献。"),
    ("グジャラート・チャリトラ写本", "Gujarati charitra manuscripts", "caritra", "gujarati", "商人・僧の伝記を記すグジャラート写本群。"),
    ("アパブランシャ・チャリウ", "Apabhramsha cariu", "cariu", "devanagari", "英雄や聖者の生涯を語るアパブランシャ詩。"),
    ("『ウパデーシャラーサーヤナラーサ』", "Upadeśarasāyana-rāsa", "Upadeśarasāyana-rāsa", "devanagari", "ジャイナ教訓をラーサ形式で説く中世詩。"),
    ("パームリーフ・ジャイナ目録詩", "Jain palm-leaf catalogue verse", "jaina granthasuci", "devanagari", "写本目録に添えられた短い韻文的記録。"),
    # Eastern vernacular cult genres
    ("ベンガル・マンガルカーヴィヤ小伝", "Minor Mangal-kavya", "maṅgal-kāvya", "bengali", "地方神を讃えるベンガル吉祥詩の小系譜。"),
    ("ダルママンガル異本群", "Dharmamangal recensions", "Dharmamaṅgal", "bengali", "ダルマ神物語の地域差を示す写本異本群。"),
    ("オリヤー・チャンパー歌曲", "Odia champu songs", "champu", "odia", "韻文と旋律を合わせたオリヤー語宮廷歌曲。"),
    ("サララ・マハーバーラタ", "Sarala Mahabharata", "Sāralā Mahābhārata", "odia", "サララ・ダーサによるオリヤー語叙事詩翻案。"),
    ("マイティリー・ヴィディヤーパティ歌曲", "Vidyapati Maithili songs", "Vidyapati pada", "maithili", "宮廷恋愛と信仰を交差させるマイティリー歌曲。"),
    ("チャリャーパダ写本断片", "Caryapada manuscript fragments", "Caryāpada", "bengali", "東インド初期俗語仏教詩の断片的写本。"),
    # Deccan, Marathi, and Kannada subgenres
    ("マハーヌバーヴ・リーラーチャリトラ", "Mahanubhava Lilacharitra", "Līḷācaritra", "marathi", "初期マラーティー散文で聖者行伝を記す作品。"),
    ("マラーティー・ポーワーダー", "Marathi powada", "powada", "devanagari", "戦功や反乱を歌うマラーティー英雄バラッド。"),
    ("ラーワニー印刷歌本", "Lavani chapbooks", "lāvaṇī", "devanagari", "民衆劇と結びついたマラーティー俗謡小冊子。"),
    ("カンナダ・ラガレ", "Kannada ragale", "ragaḷe", "kannada", "中世カンナダ詩で用いられた連続韻律形式。"),
    ("ハリハラ『ギリジャーカリャーナ』", "Harihara's Girijakalyana", "Girijākalyāṇa", "kannada", "ラガレ形式でシヴァ婚礼を語るカンナダ古典。"),
    ("テルグ・ドヴィパダ叙事詩", "Telugu dvipada epic", "dvipada", "telugu", "二行連鎖で物語を進めるテルグ語叙事詩型。"),
    # Poetic theory and manuscript micro-debates
    ("ラサーブハーサ論", "Rasabhasa debate", "rasābhāsa", "devanagari", "不完全なラサの成立をめぐる詩論上の争点。"),
    ("ドヴァニ対アヌミティ論争", "Dhvani-anumiti debate", "dhvani-anumiti", "devanagari", "詩的意味を暗示か推論かで説明する論争。"),
    ("アウチティヤ細目論", "Auchitya subcategory debate", "aucitya", "devanagari", "適切性を人物・時・場に細分する詩論。"),
    ("リーティ・グナ配置論", "Riti-guna taxonomy", "rīti-guṇa", "devanagari", "文体と詩質の対応関係を分類する微細論。"),
    ("ヴァクロークティ六層説", "Six levels of vakrokti", "vakrokti", "devanagari", "曲言性を音素から構成まで分けるクンタカ説。"),
    ("デーシー韻律目録", "Desi metre catalogues", "deśī chandas", "devanagari", "地域語詩の韻律を列挙する中世詩学文献。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id=12"
            ).fetchall()
        }
        dupes = [name for name, *_ in CONCEPTS if name in existing]
        if dupes:
            raise SystemExit(f"duplicates in lit_india: {dupes}")

        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=12"
        ).fetchone()[0]
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=12"
        ).fetchone()[0]
        print(f"before={before} after={after} added={after - before}")


if __name__ == "__main__":
    main()
