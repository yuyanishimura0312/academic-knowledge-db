#!/usr/bin/env python3
"""Wave 41: 30 hyper-niche European Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian minor prose and women writers
    ("ストラパローラ『愉しき夜』枠物語", "Straparola, Pleasant Nights frame", "Le piacevoli notti", P_IT, "民話素材を都市的ノヴェッラ枠へ収めた初期童話集。"),
    ("オルテンシオ・ランド『逆説集』", "Ortensio Lando, Paradossi", "Paradossi", P_IT, "通念を反転する短章で知的遊戯を行う逆説散文。"),
    ("アントン・フランチェスコ・ドーニ『世界』", "Anton Francesco Doni, I mondi", "I mondi", P_IT, "対話と夢想で奇態な社会像を並べる実験散文。"),
    ("ドメニキ『笑話集』", "Lodovico Domenichi, Facezie", "Facezie", P_IT, "宮廷機知と俗語逸話を編むルネサンス笑話集。"),
    ("トゥッリア・ダラゴーナ『愛の無限対話』", "Tullia d'Aragona, Dialogue on Love", "Dialogo dell'infinita d'amore", P_IT, "女性著者が愛の無限性を論じる新プラトン主義対話。"),
    ("ラウラ・バッティフェッリ『第一詩集』", "Laura Battiferri, First Book of Works", "Il primo libro delle opere toscane", P_IT, "ミケランジェロ圏の敬虔詩を硬質に編む女性詩集。"),

    # Iberian and Portuguese peripheral print
    ("ガルシア・デ・レゼンデ『総歌集』", "Garcia de Resende, Cancioneiro Geral", "Cancioneiro Geral", P_IB, "ポルトガル宮廷詩を集成した大部な印刷歌集。"),
    ("ベルナルディン・リベイロ『少女と娘』", "Bernardim Ribeiro, Menina e Moca", "Menina e Moca", P_IB, "サウダーデを散文牧歌へ沈めたポルトガル恋愛物語。"),
    ("フランシスコ・デ・モライス『パルメリン・デ・イングラテーラ』", "Francisco de Moraes, Palmeirim de Inglaterra", "Palmeirim de Inglaterra", P_IB, "ポルトガル語で展開した騎士道ロマンスの後期傍流。"),
    ("ジョルジェ・フェレイラ『エウフロジナ』", "Jorge Ferreira de Vasconcelos, Eufrosina", "Eufrosina", P_IB, "会話劇形式で宮廷恋愛と機知を競わせる散文喜劇。"),
    ("ティモネーダ『食卓話と慰め』", "Joan Timoneda, Sobremesa y alivio", "Sobremesa y alivio de caminantes", P_IB, "旅人向けの短い笑話を集めたバレンシア印刷本。"),
    ("フアン・デ・ラ・クエバ『詩法実例』", "Juan de la Cueva, Ejemplar poetico", "Ejemplar poetico", P_IB, "スペイン詩形の実践規範を韻文で説く詩論。"),

    # French provincial prose and poetics
    ("ノエル・デュ・ファイユ『田舎話』", "Noel du Fail, Rustic Talks", "Propos rustiques", P_FR, "ブルターニュ農村の語りを人文主義散文に移す小品集。"),
    ("タブロー『雑録集』", "Etienne Tabourot, Bigarrures", "Les Bigarrures", P_FR, "言葉遊びと奇文を蒐集するブルゴーニュ的雑録。"),
    ("ジャック・イヴェール『春』", "Jacques Yver, Le Printemps", "Le Printemps", P_FR, "戦乱後の語り場を設定する仏語ノヴェッラ集。"),
    ("ボエスチュオー『驚異譚集』", "Pierre Boaistuau, Histoires prodigieuses", "Histoires prodigieuses", P_FR, "怪異・奇形・天変を教訓化する驚異譚集。"),
    ("ギヨーム・デゾーテル『返答』", "Guillaume des Autels, Replique", "Replique", P_FR, "デュ・ベレー詩論へ地方詩人が返した反論書。"),
    ("クロード・ド・ポントゥー『理念』", "Claude de Pontoux, L'Idee", "L'Idee", P_FR, "リヨン派以後の抽象恋愛を細密化した詩集。"),

    # English minor print and devotional side channels
    ("イザベラ・ホイットニー『手紙の写し』", "Isabella Whitney, Copy of a Letter", "The Copy of a Letter", P_EN, "女性の都市的失恋を印刷詩で語る初期英詩集。"),
    ("ホイットニー『甘美な嗅ぎ袋』", "Isabella Whitney, Sweet Nosegay", "A Sweet Nosegay", P_EN, "教訓詩と遺言形式を混ぜる女性向け小冊子。"),
    ("ジョージ・ウェットストン『ヘプタメロン』", "George Whetstone, Heptameron", "An Heptameron of Civil Discourses", P_EN, "市民的談話を七日枠に置く英語散文物語集。"),
    ("バーナビー・グージ『牧歌集』", "Barnabe Googe, Eglogs", "Eglogs, Epytaphes, and Sonettes", P_EN, "改革派調の牧歌と墓碑詩を束ねた初期英詩集。"),
    ("トマス・チャーチヤード『小片集』", "Thomas Churchyard, Chippes", "Churchyardes Chippes", P_EN, "軍人詩人の雑多な回想詩文を集めた印刷本。"),
    ("ロバート・サウスウェル『聖ペテロの嘆き』", "Robert Southwell, Saint Peter's Complaint", "Saint Peter's Complaint", P_EN, "カトリック殉教圏の涙の瞑想詩。"),

    # Northern, Neo-Latin, and Reformation microcanons
    ("ロレンハーゲン『蛙鼠合戦』", "Georg Rollenhagen, Froschmeuseler", "Froschmeuseler", P_NO, "擬獣叙事で宗派対立と政治風刺を包む独語詩。"),
    ("ニコラウス・マヌエル『教皇と聖職者』", "Niklaus Manuel, Pope and Clergy", "Der Ablasskramer", P_NO, "宗教改革宣伝を謝肉祭劇にしたベルンの風刺劇。"),
    ("ブルシウス『ヨセフ劇』", "Cornelius Crocus, Joseph", "Joseph", P_NO, "アムステルダム人文主義学校劇の聖書悲劇。"),
    ("マカルスキー聖書劇写本", "Makarsky biblical play manuscripts", "Makarsky biblejske igre", P_NO, "クロアチア沿岸部に残る宗教劇写本群。"),
    ("レイ『カンデルのアヒル戦争』", "Johann Fischart, Das gluckhafft Schiff", "Das gluckhafft Schiff von Zurich", P_NO, "都市祝祭を韻文化したライン地方の機会詩。"),
    ("クラネック『ブルノ市書記詩』", "Renaissance Brno town-clerk verse", "Brnenske pisarske verse", P_NO, "都市書記がラテン語と俗語で残したモラヴィア詩文。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise ValueError("expected 30 concepts")
    inserted = 0
    with LitDB() as db:
        existing_names = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts")
        }
        dup_names = [row[0] for row in CONCEPTS if row[0] in existing_names]
        if dup_names:
            raise ValueError(f"already in DB: {dup_names}")
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
