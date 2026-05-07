#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_eu_enlightenment."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_enlightenment"
REGION = "西欧"

CONCEPTS = [
    # Cluster 1: clandestine manuscripts and radical pamphlet afterlives
    {
        "name_ja": "『三詐欺師論』地下写本",
        "name_en": "Traite des trois imposteurs clandestine manuscript",
        "name_original": "Traite des trois imposteurs",
        "definition": "宗教批判写本。預言者像を政治的詐術として読む。",
    },
    {
        "name_ja": "『軍人哲学者』地下唯物論",
        "name_en": "Le Militaire philosophe",
        "name_original": "Le Militaire philosophe",
        "definition": "匿名地下文書。軍人語りで自然宗教と唯物論を結ぶ。",
    },
    {
        "name_ja": "ジャン・メリエ『遺書』抜粋流通",
        "name_en": "Jean Meslier Testament excerpts",
        "name_original": "Memoire des pensees et sentiments",
        "definition": "司祭の無神論的遺稿。抜粋版で急進啓蒙へ浸透。",
    },
    {
        "name_ja": "『スピノザ精神』写本読書圏",
        "name_en": "L'Esprit de Spinoza manuscript circulation",
        "name_original": "L'Esprit de Spinoza",
        "definition": "スピノザ主義を簡約する地下文書。反聖職者読書に媒介。",
    },
    {
        "name_ja": "『良識』匿名無神論パンフ",
        "name_en": "Le Bon Sens anonymous atheist pamphlet",
        "name_original": "Le Bon Sens",
        "definition": "簡潔な無神論パンフ。民衆向け論証で信仰を攻撃。",
    },
    {
        "name_ja": "『テレマコス』政治鍵読み",
        "name_en": "Telemaque political key reading",
        "name_original": "Les Aventures de Telemaque",
        "definition": "教訓叙事を宮廷批判の暗号として読む受容慣行。",
    },

    # Cluster 2: periodicals, miscellanies, and para-literary publics
    {
        "name_ja": "マリヴォー『フランス傍観者』",
        "name_en": "Marivaux Le Spectateur francais",
        "name_original": "Le Spectateur francais",
        "definition": "一人称観察の定期文。都市風俗と内面分析を細密化。",
    },
    {
        "name_ja": "プレヴォ『賛否両論』",
        "name_en": "Prevost Le Pour et contre",
        "name_original": "Le Pour et contre",
        "definition": "英仏文芸情報誌。翻訳紹介と批評判断を連載化。",
    },
    {
        "name_ja": "ヘイウッド『女性傍観者』",
        "name_en": "Eliza Haywood The Female Spectator",
        "name_original": "The Female Spectator",
        "definition": "女性向け定期文。恋愛訓戒と社交批評を結び直す。",
    },
    {
        "name_ja": "ジョンソン『ランブラー』紙",
        "name_en": "Samuel Johnson The Rambler",
        "name_original": "The Rambler",
        "definition": "道徳週刊文。抽象的反省を短い散文形式に凝縮。",
    },
    {
        "name_ja": "メルシエ『パリ情景』断章都市誌",
        "name_en": "Mercier Tableau de Paris urban fragments",
        "name_original": "Tableau de Paris",
        "definition": "断章都市誌。街路観察を社会批評の細胞にする。",
    },
    {
        "name_ja": "メーザー『愛国幻想』地方随筆",
        "name_en": "Justus Moser Patriotische Phantasien",
        "name_original": "Patriotische Phantasien",
        "definition": "オスナブリュック発の随筆。地方慣習を啓蒙改革に対置。",
    },

    # Cluster 3: Swiss-German pastoral, poetics, and minor prose
    {
        "name_ja": "ハラー『アルプス』山岳記述詩",
        "name_en": "Albrecht von Haller Die Alpen",
        "name_original": "Die Alpen",
        "definition": "山岳記述詩。自然科学的観察と徳の地理を結ぶ。",
    },
    {
        "name_ja": "ゲスナー『牧歌』ロココ田園",
        "name_en": "Salomon Gessner Idyllen",
        "name_original": "Idyllen",
        "definition": "小型田園散文詩。ロココ的感性で古典牧歌を縮約。",
    },
    {
        "name_ja": "クライスト『春』自然描写詩",
        "name_en": "Ewald von Kleist Der Fruhling",
        "name_original": "Der Fruhling",
        "definition": "季節詩。自然神学と感覚描写を穏健に接続する。",
    },
    {
        "name_ja": "ラーベナー風刺的性格素描",
        "name_en": "Gottlieb Wilhelm Rabener satirical sketches",
        "name_original": "Satiren",
        "definition": "小市民的悪徳を性格素描で刺すドイツ啓蒙風刺。",
    },
    {
        "name_ja": "ツィンツェンドルフ賛美歌圏",
        "name_en": "Zinzendorf Moravian hymn culture",
        "name_original": "Herrnhuter Lieder",
        "definition": "ヘルンフート派の賛美歌圏。信愛の語彙を詩化。",
    },
    {
        "name_ja": "ラファーター観相学断章",
        "name_en": "Lavater physiognomic fragments",
        "name_original": "Physiognomische Fragmente",
        "definition": "顔貌読解の断章集。身体記号を性格批評へ転用。",
    },

    # Cluster 4: women's epistolary and educational micro-traditions
    {
        "name_ja": "グラフィニー『ペルー女の手紙』",
        "name_en": "Graffigny Lettres d'une Peruvienne",
        "name_original": "Lettres d'une Peruvienne",
        "definition": "異邦女性書簡体。征服批判と感情教育を交差させる。",
    },
    {
        "name_ja": "シャリエール『ヌーシャテル書簡』",
        "name_en": "Isabelle de Charriere Lettres neuchateloises",
        "name_original": "Lettres neuchateloises",
        "definition": "地方都市の書簡体小説。結婚市場と階層感覚を測る。",
    },
    {
        "name_ja": "リッコボーニ『ファニ・バトラー書簡』",
        "name_en": "Riccoboni Lettres de Fanni Butler",
        "name_original": "Lettres de Mistriss Fanni Butlerd",
        "definition": "女性一人称書簡体。恋愛依存と語りの自己防衛を描く。",
    },
    {
        "name_ja": "ジャンリス教育劇",
        "name_en": "Madame de Genlis educational theater",
        "name_original": "Theatre a l'usage des jeunes personnes",
        "definition": "少女教育用の家庭劇。徳目を上演訓練へ組み込む。",
    },
    {
        "name_ja": "エッジワース『実地教育』物語教材",
        "name_en": "Edgeworth Practical Education narrative pedagogy",
        "name_original": "Practical Education",
        "definition": "児童教育論の物語例示。観察と実験を家庭教材化。",
    },
    {
        "name_ja": "バーボールド賛美歌的児童散文",
        "name_en": "Anna Laetitia Barbauld hymnic children's prose",
        "name_original": "Hymns in Prose for Children",
        "definition": "児童向け散文賛歌。自然観察を敬虔な感性へ導く。",
    },

    # Cluster 5: Italian, Iberian, and border-zone micro-debates
    {
        "name_ja": "ルサン『詩学』新古典論争",
        "name_en": "Luzan Poetica neoclassical debate",
        "name_original": "La Poetica",
        "definition": "スペイン新古典詩学。規則と趣味をめぐる論争の核。",
    },
    {
        "name_ja": "モンティ『バッスヴィル讃歌』",
        "name_en": "Vincenzo Monti Bassvilliana",
        "name_original": "In morte di Ugo Bassville",
        "definition": "反革命的幻視詩。ダンテ調で政治暴力を寓意化。",
    },
    {
        "name_ja": "バレッティ『文学鞭』",
        "name_en": "Giuseppe Baretti La Frusta letteraria",
        "name_original": "La Frusta letteraria",
        "definition": "攻撃的文芸定期刊行物。趣味判断を個人罵倒に近づける。",
    },
    {
        "name_ja": "ベッカリーア『リチェルケ』文体論",
        "name_en": "Beccaria Ricerche intorno alla natura dello stile",
        "name_original": "Ricerche intorno alla natura dello stile",
        "definition": "文体の快苦を論じる小論。感覚論を修辞学に適用。",
    },
    {
        "name_ja": "クリスティアン・フェリックス・ヴァイセ児童劇",
        "name_en": "Christian Felix Weisse children's drama",
        "name_original": "Kinderfreund",
        "definition": "児童雑誌と劇作の交点。啓蒙的しつけを対話化。",
    },
    {
        "name_ja": "フォルネル『学者のカフェ』風刺",
        "name_en": "Juan Pablo Forner cafe satire",
        "name_original": "El cafe",
        "definition": "スペイン文人風刺。社交空間を知的虚栄の舞台にする。",
    },
]


def main() -> None:
    inserted = skipped = 0
    with LitDB("lit.sqlite") as db:
        for entry in CONCEPTS:
            cid_before = db.find_concept(entry["name_ja"], REGION, None)
            db.insert_concept(
                **entry,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=None,
                original_script="latin",
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if cid_before:
                skipped += 1
            else:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id = 4"
        ).fetchone()[0]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total: {total}")


if __name__ == "__main__":
    main()
