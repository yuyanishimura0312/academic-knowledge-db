#!/usr/bin/env python3
"""Wave 38 / Cluster 05: lit_eu_renaissance に30概念を追加（細部ニッチ）"""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 3  # lit_eu_renaissance

# 期間ID（西欧）
P_ELIZ = 44   # エリザベス朝・ジャコビアン期（英）
P_FR_R = 146  # フランス・ルネサンス期
P_IT_R = 144  # イタリア・ルネサンス期
P_GOLD = 45   # 黄金世紀（西）
P_NORTH = 148 # 北方ルネサンス期

CONCEPTS = [
    # Cluster 1: 英演劇細部以外の作家
    ("キッド『スペインの悲劇』", "Kyd Spanish Tragedy", "The Spanish Tragedy", "latin", "西欧", P_ELIZ,
     "復讐悲劇の祖型を確立したトマス・キッドの代表作。劇中劇構造を導入。"),
    ("マーロウ『フォースタス博士』詩学", "Marlowe Doctor Faustus poetics", "The Tragical History of Doctor Faustus", "latin", "西欧", P_ELIZ,
     "ファウスト伝説をブランクヴァースで悲劇化したマーロウの代表作。野心と知識への欲望を描く。"),
    ("マーロウ『タンバレイン大王』", "Marlowe Tamburlaine the Great", "Tamburlaine the Great", "latin", "西欧", P_ELIZ,
     "ティムール征服譚を題材にした二部構成の英雄悲劇。雄渾な無韻詩で英語悲劇を一新。"),
    ("ウェブスター『マルフィ公爵夫人』詩学", "Webster Duchess of Malfi poetics", "The Duchess of Malfi", "latin", "西欧", P_ELIZ,
     "ジョン・ウェブスターによる暗黒悲劇。死と狂気のイメジャリーで形而上的恐怖を表現。"),
    ("ミドルトン『チェンジリング』", "Middleton The Changeling", "The Changeling", "latin", "西欧", P_ELIZ,
     "トマス・ミドルトン共作の心理悲劇。欲望の倫理的変質を二重筋構造で展開。"),
    ("ジョン・フォード『あわれ彼女は娼婦』", "Ford Tis Pity She's a Whore", "'Tis Pity She's a Whore", "latin", "西欧", P_ELIZ,
     "近親相姦愛を主題化したフォードの問題悲劇。後期ジャコビアン演劇の極北。"),

    # Cluster 2: 仏宮廷詩・詩劇
    ("ロンサール『エレーヌへのソネット集』", "Ronsard Sonnets pour Hélène", "Sonnets pour Hélène", "latin", "西欧", P_FR_R,
     "プレイヤード派の領袖ロンサールが晩年の宮廷恋愛を歌った晩年の傑作ソネット連作。"),
    ("デュ・ベレー『オリーヴ』", "Du Bellay L'Olive", "L'Olive", "latin", "西欧", P_FR_R,
     "フランス語初の本格的ソネット連作。ペトラルカ受容のフランス的展開。"),
    ("ロベール・ガルニエ『ブラダマンテ』", "Garnier Bradamante", "Bradamante", "latin", "西欧", P_FR_R,
     "アリオストの題材を仏古典悲劇形式で翻案。トラジコメディの先駆的作品。"),
    ("ジョデル『捕えられたクレオパトラ』詩学", "Jodelle Cléopâtre captive poetics", "Cléopâtre captive", "latin", "西欧", P_FR_R,
     "フランス語初の人文主義悲劇。プレイヤード派による古代悲劇形式の移植。"),
    ("バイフ『ミーム集』", "Baïf Mimes", "Mimes, enseignements et proverbes", "latin", "西欧", P_FR_R,
     "アントワーヌ・ド・バイフによる教訓詩集。古典詩律実験と俗諺を融合。"),
    ("ペルネット・デュ・ギエ『詩集』", "Pernette du Guillet Rymes", "Rymes", "latin", "西欧", P_FR_R,
     "リヨン派の女性詩人による新プラトン主義的恋愛詩集。ルイーズ・ラベに先行。"),

    # Cluster 3: 伊新プラトン主義・詩集
    ("フィチーノ『プラトン神学』", "Ficino Platonic Theology", "Theologia Platonica", "latin", "西欧", P_IT_R,
     "マルシリオ・フィチーノが魂の不滅を論じた新プラトン主義神学の集大成。"),
    ("ピコ・デラ・ミランドラ『人間の尊厳について』", "Pico Oration on the Dignity of Man", "Oratio de hominis dignitate", "latin", "西欧", P_IT_R,
     "人間の自由意志と無限の可能性を宣言したルネサンス人文主義の宣言文。"),
    ("ベンボ『アゾラーニ』恋愛論", "Bembo Gli Asolani", "Gli Asolani", "latin", "西欧", P_IT_R,
     "ピエトロ・ベンボの三日間にわたる恋愛対話篇。新プラトン主義的恋愛観を提示。"),
    ("ヴィットリア・コロンナ『霊の詩集』", "Vittoria Colonna Rime spirituali", "Rime spirituali", "latin", "西欧", P_IT_R,
     "ペスカーラ侯爵夫人による宗教詩集。ミケランジェロにも影響した霊性詩。"),
    ("ガスパラ・スタンパ『詩集』", "Gaspara Stampa Rime", "Rime", "latin", "西欧", P_IT_R,
     "16世紀ヴェネツィアの女性詩人による情熱的恋愛ソネット集。死後出版。"),
    ("ヴェロニカ・フランコ『テルツェ・リーメ』", "Veronica Franco Terze rime", "Terze rime", "latin", "西欧", P_IT_R,
     "ヴェネツィアの高級娼婦詩人による三韻句詩集。女性の自立的声を表明。"),

    # Cluster 4: 西宗教詩・牧歌
    ("聖テレサ・デ・アビラ『生涯の書』", "Santa Teresa de Ávila Vida", "Libro de la vida", "latin", "西欧", P_GOLD,
     "カルメル会改革者テレサによる神秘体験を綴った霊性自伝。スペイン散文の傑作。"),
    ("聖フアン・デ・ラ・クルス『霊の讃歌』", "San Juan de la Cruz Cántico Espiritual", "Cántico Espiritual", "latin", "西欧", P_GOLD,
     "カルメル会神秘家の詩。雅歌に基づく魂と神の婚姻を歌うバロック神秘詩の頂点。"),
    ("モンテマヨール『ディアナ』", "Montemayor Diana", "Los siete libros de la Diana", "latin", "西欧", P_GOLD,
     "イベリア初の本格牧歌小説。サンナザーロを継承し欧州牧歌ロマンスの典型確立。"),
    ("ガルシラーソ『第三牧歌』", "Garcilaso Eclogue III", "Égloga III", "latin", "西欧", P_GOLD,
     "ガルシラーソ・デ・ラ・ベガによる神話的牧歌。タホ川のニンフ刺繍を描く名篇。"),
    ("フライ・ルイス・デ・レオン『隠棲の生活』", "Fray Luis de León Vida retirada", "Vida retirada", "latin", "西欧", P_GOLD,
     "アウグスティノ会神学者による隠棲頌歌。ホラティウス受容と霊性の融合。"),
    ("ロペ・デ・ベガ『ラ・ドロテア』", "Lope de Vega La Dorotea", "La Dorotea", "latin", "西欧", P_GOLD,
     "ロペ晩年の対話小説。自伝的恋愛体験を『セレスティーナ』形式で描く。"),

    # Cluster 5: 北部欧州人文主義
    ("エラスムス『痴愚神礼賛』詩学", "Erasmus Praise of Folly poetics", "Moriae Encomium", "latin", "西欧", P_NORTH,
     "エラスムスによる風刺的賛辞。痴愚女神の自己賛美を通じ社会全般を批判。"),
    ("トマス・モア『ユートピア』詩学", "More Utopia poetics", "Utopia", "latin", "西欧", P_NORTH,
     "理想郷の枠組と対話篇形式で社会批判を展開。ジャンルとしてのユートピア確立。"),
    ("メランヒトン『詩学』", "Melanchthon poetics", "Elementa rhetorices", "latin", "西欧", P_NORTH,
     "ルター派人文主義者による修辞・詩学書。ドイツ・プロテスタント教育を規定。"),
    ("コンラート・ツェルティス『恋愛詩集』", "Conrad Celtis Amores", "Quattuor libri amorum", "latin", "西欧", P_NORTH,
     "ドイツ桂冠詩人によるラテン語恋愛詩集。四つのドイツ地方を象徴する女性を歌う。"),
    ("ブラント『阿呆船』詩学", "Brant Ship of Fools poetics", "Das Narrenschiff", "latin", "西欧", P_NORTH,
     "教訓的諷刺詩集。112種の愚者像を木版画と韻文で批判する大衆教訓文学の起源。"),
    ("ハンス・ザックス『阿呆を歌う職匠』", "Hans Sachs Singer of Fools", "Meistergesang", "latin", "西欧", P_NORTH,
     "ニュルンベルクの靴職人マイスタージンガーによる風刺・教訓的職匠歌。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, region, period_id, definition in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id,
                 region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID,
                  region, period_id, definition, 3, 'A', '西欧'))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {name_ja} ({e})")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
