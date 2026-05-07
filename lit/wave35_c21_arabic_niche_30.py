#!/usr/bin/env python3
"""Wave 35 C21 - Arabic literature niche 30 concepts."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 13
REGION = "南西アジア"

# (name_ja, name_en, name_original, original_script, period_id, definition, importance, fourth, tier, canonical)
CONCEPTS = [
    # Cluster 1: アンダルス補完 (period 139)
    ("イブン・ハズム『鳩の頸飾り』恋愛論詳細", "Ibn Hazm Tawq al-hamama detailed", "طوق الحمامة", "arabic", 139, "11世紀アンダルスの恋愛心理論考、散文と挿入詩で恋の諸相を分析。", 4, "invariant", "primary", "yes"),
    ("イブン・トゥファイル『ハイイ・イブン・ヤクザーン』哲学小説詳細", "Ibn Tufail Hayy ibn Yaqzan detailed", "حي بن يقظان", "arabic", 139, "12世紀アンダルスの哲学的寓話小説、孤島の独学者の理性探究を描く。", 4, "invariant", "primary", "yes"),
    ("イブン・サフル・アル＝アンダルスィー詩集", "Ibn Sahl al-Andalusi diwan", "ابن سهل الأندلسي", "arabic", 139, "13世紀セビーリャのユダヤ系改宗詩人、ムワッシャハ恋愛詩で著名。", 3, "invariant", "primary", "partial"),
    ("イブン・ハムディース・シチリア詩", "Ibn Hamdis Sicilian poetry", "ابن حمديس الصقلي", "arabic", 139, "11-12世紀シチリア出身詩人、ノルマン征服後の故郷喪失と回想を歌う。", 3, "invariant", "primary", "partial"),
    ("ムワッシャハ詩形構造論", "Muwashshah strophic form theory", "موشح", "arabic", 139, "アンダルス発祥の連節詩形、ハルジャ（俗語結句）を含む多言語混成構造。", 4, "invariant", "primary", "yes"),
    ("イブン・クズマーン・ザジャル詩集", "Ibn Quzman zajal corpus", "ديوان ابن قزمان", "arabic", 139, "12世紀コルドバ詩人、アンダルス俗語アラビア語によるザジャル詩の集成。", 4, "invariant", "primary", "yes"),

    # Cluster 2: ナフダ詳細 (period 20)
    ("ヤーズィジー『マジュマウ・アル＝バフライン』", "Yaziji Majma' al-bahrayn", "مجمع البحرين", "arabic", 20, "ナースィーフ・ヤーズィジーのマカーマ集、古典文体復興の代表作。", 3, "rethinking", "primary", "partial"),
    ("ブスターニー『ダーイラト・アル＝マアーリフ』", "Bustani Da'irat al-Ma'arif", "دائرة المعارف", "arabic", 20, "ブトルス・ブスターニー編纂の近代アラブ初の百科事典、ナフダ知の集約。", 4, "rethinking", "primary", "yes"),
    ("シドヤーク『脚の上の脚』詳細", "Shidyaq Saq 'ala al-saq detailed", "الساق على الساق", "arabic", 20, "1855年刊の自伝的散文小説、言語実験と社会風刺で近代アラブ散文を開拓。", 4, "rethinking", "primary", "yes"),
    ("マフムード・サーミー・アル＝バールーディー", "Mahmoud Sami al-Barudi", "محمود سامي البارودي", "arabic", 20, "19世紀末エジプト詩人、新古典主義（ネオクラシシズム）詩運動の指導者。", 4, "rethinking", "primary", "yes"),
    ("アフマド・シャウキー・マハジャル交流", "Ahmad Shawqi mahjar exchanges", "أحمد شوقي والمهجر", "arabic", 20, "詩人の王シャウキーとマハジャル（移民）詩人ジブラーン等との交流圏。", 3, "rethinking", "secondary", "partial"),
    ("ハリール・ムトラーン詩学革新", "Khalil Mutran poetic innovation", "خليل مطران", "arabic", 20, "シリア出身エジプト活動詩人、フランス象徴主義導入とロマン主義への橋渡し。", 4, "rethinking", "primary", "yes"),

    # Cluster 3: 現代詩 (period 21)
    ("アドゥニース『ミフヤール・アッ＝ダマシュキーの歌』", "Adunis Aghani Mihyar al-Dimashqi", "أغاني مهيار الدمشقي", "arabic", 21, "1961年刊、神話的人物ミフヤールを通じ近代性とアラブ伝統を再編する詩集。", 5, "rethinking", "primary", "yes"),
    ("サイヤーブ『雨の歌』詳細", "Sayyab Anshudat al-matar detailed", "أنشودة المطر", "arabic", 21, "1960年刊、自由詩形（シウル・フッル）の金字塔、イラク農村と再生神話を融合。", 5, "rethinking", "primary", "yes"),
    ("バヤーティー『貧困の書』", "Bayati Sifr al-faqr wa al-thawra", "سفر الفقر والثورة", "arabic", 21, "1965年刊詩集、亡命と革命のテーマでアラブ自由詩運動を深化させる。", 4, "rethinking", "primary", "partial"),
    ("マフムード・ダルウィーシュ『記憶のための忘却』", "Mahmoud Darwish Memory for Forgetfulness", "ذاكرة للنسيان", "arabic", 21, "1982年ベイルート包囲戦の散文詩的回想録、パレスチナ集合的記憶の再構築。", 5, "rethinking", "primary", "yes"),
    ("ニザール・カッバーニー『お前は私のもの』", "Nizar Qabbani Hubla", "حبلى", "arabic", 21, "女性身体と政治的怒りを融合した代表的恋愛・政治詩、アラブ口語性を導入。", 4, "rethinking", "primary", "partial"),
    ("ハリール・ハーウィー『脱穀場と飢餓』", "Khalil Hawi Bayadir al-Ju", "بيادر الجوع", "arabic", 21, "1965年刊詩集、アラブ近代の精神的不毛と再生願望をエリオット的に表現。", 4, "rethinking", "primary", "partial"),

    # Cluster 4: 現代小説 (period 21)
    ("マフフーズ『カルナック・カフェ』", "Mahfouz Karnak Cafe", "الكرنك", "arabic", 21, "1974年刊小説、ナーセル時代の抑圧体制を市民の視点から告発する政治小説。", 4, "rethinking", "primary", "yes"),
    ("マフフーズ『ゲベラウィの子供たち』詳細", "Mahfouz Awlad Haratina detailed", "أولاد حارتنا", "arabic", 21, "1959年連載アレゴリー小説、宗教史を路地物語に翻案、長期発禁となる。", 5, "rethinking", "primary", "yes"),
    ("ユースフ・イドリース『我らが街区の息子たち』", "Idris Sons of Our Quarter", "أبناء حارتنا", "arabic", 21, "短編集、エジプト農村と都市下層の声を口語混成体で描き短編形式を革新。", 3, "rethinking", "primary", "partial"),
    ("エリアス・フーリー『ヤーロー』", "Khoury Yalo", "يالو", "arabic", 21, "2002年刊小説、レバノン内戦下の暴力と証言の不可能性を多声法で描く。", 4, "rethinking", "primary", "yes"),
    ("タイイブ・サーリフ『ザインの結婚』", "Salih Wedding of Zein", "عرس الزين", "arabic", 21, "1966年刊スーダン中編、村落共同体の祝祭と聖愚者像を民俗的に描く。", 4, "rethinking", "primary", "yes"),
    ("ムニーフ『塩の都市』五部作", "Munif Cities of Salt pentalogy", "مدن الملح", "arabic", 21, "1984-89年刊、湾岸石油発見と部族社会の解体を叙事詩的に描く大河小説。", 5, "rethinking", "primary", "yes"),

    # Cluster 5: 女性+マグレブ (period 21)
    ("ライラー・バアラバッキー『私は生きる』", "Layla Ba'albakki Ana Ahya", "أنا أحيا", "arabic", 21, "1958年刊レバノン小説、女性一人称による性と自由の語りでアラブ社会に衝撃。", 4, "rethinking", "primary", "yes"),
    ("ハナーン・アッ＝シャイフ『ザフラの物語』", "Hanan al-Shaykh Hikayat Zahra", "حكاية زهراء", "arabic", 21, "1980年刊、レバノン内戦下の女性精神の崩壊を女性身体の視点から描く。", 4, "rethinking", "primary", "yes"),
    ("アハダーフ・スウェイフ『愛の地図』", "Ahdaf Soueif Map of Love", "خريطة الحب", "arabic", 21, "1999年英語刊、英エジプト二世代の恋愛と植民地主義を交錯させる小説。", 4, "rethinking", "primary", "partial"),
    ("サアダーウィー『二人の女が一人になる』", "Saadawi Two Women in One", "امرأتان في امرأة", "arabic", 21, "1968年刊、医学生女性の二重意識と家父長制への反逆を描くフェミニズム小説。", 4, "rethinking", "primary", "yes"),
    ("ターハル・ワッタール『地震』他", "Tahar Ouettar al-Lazz/al-Zilzal", "الزلزال", "arabic", 21, "1974年刊アルジェリア小説、土地改革下の旧封建層意識を内的独白で描く。", 3, "rethinking", "primary", "partial"),
    ("ムハンマド・シュクリ『過ちの時間』", "Mohammed Choukri Time of Errors", "زمن الأخطاء", "arabic", 21, "1992年刊自伝第二部、タンジェ青年期の彷徨と教育覚醒を赤裸々に描く。", 4, "rethinking", "primary", "yes"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for c in CONCEPTS:
        (name_ja, name_en, name_orig, script, period_id, defn, imp, fourth, tier, canonical) = c
        # check existence
        cur.execute(
            "SELECT id FROM concepts WHERE name_ja=? AND region=? AND period_id=?",
            (name_ja, REGION, period_id),
        )
        if cur.fetchone():
            skipped += 1
            continue
        cur.execute(
            """INSERT INTO concepts
            (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
             definition, importance_score, fourth_transform_status, source_tier, canonical_in_region)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, period_id,
             defn, imp, fourth, tier, canonical),
        )
        inserted += 1
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"inserted={inserted} skipped={skipped} total_arabic={total}")


if __name__ == "__main__":
    main()
