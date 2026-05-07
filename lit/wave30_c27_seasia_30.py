#!/usr/bin/env python3
"""Wave 30 - Add 30 concepts to subfield 17 (lit_se_asia_korea)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# Period IDs: 韓国古典 → 98(近世), 韓国近代 → 8(明治期相当)/9(大正期), 韓国現代 → 12(現代)
# Vietnam/Thai classical → 98(近世), modern → 12(現代)
# Indonesia/Philippines → 12(現代), Balagtas → 98(近世)

CONCEPTS = [
    # Cluster 1: 韓国古典 (6)
    ("一然『三国遺事』新羅伽倻仏教説話", "Samguk Yusa", "三國遺事", "kanji", 98, "東アジア",
     "新羅・高麗の仏教説話と建国神話を集成した13世紀の歴史説話集。"),
    ("金富軾『三国史記』正史", "Samguk Sagi", "三國史記", "kanji", 97, "東アジア",
     "高麗時代1145年成立の三国時代正史で漢文紀伝体の朝鮮最古の正史。"),
    ("鄭麟趾ら『高麗史』官撰史書", "Goryeosa", "高麗史", "kanji", 54, "東アジア",
     "朝鮮王朝が編纂した高麗王朝の官撰史書で1451年成立の139巻紀伝体。"),
    ("燕岩朴趾源『虎叱』風刺漢文短編", "Hojil by Park Jiwon", "虎叱", "kanji", 98, "東アジア",
     "両班の偽善を虎の口を借りて批判する朴趾源の漢文風刺短編小説。"),
    ("茶山丁若鏞『牧民心書』地方官指南", "Mongminsimseo", "牧民心書", "kanji", 98, "東アジア",
     "丁若鏞が地方官の倫理と実務を説いた実学派代表書で1818年成立。"),
    ("金時習『金鰲新話』漢文伝奇集", "Geumo Sinhwa", "金鰲新話", "kanji", 54, "東アジア",
     "朝鮮初期の漢文伝奇小説集で『剪燈新話』影響下の幻想短編五編を収録。"),

    # Cluster 2: 韓国近代 (6)
    ("李光洙『無情』近代長編小説", "Mujeong by Yi Kwang-su", "無情", "kanji", 8, "東アジア",
     "1917年連載の朝鮮初の近代長編小説で啓蒙主義と新女性像を描く。"),
    ("金東仁『甘藷』自然主義短編", "Gamja by Kim Tongin", "감자", "hangul", 9, "東アジア",
     "1925年発表の貧困と道徳崩壊を描く自然主義的短編小説の代表作。"),
    ("廉想渉『万歳前』植民地小説", "Mansejeon by Yom Sang-seop", "萬歲前", "kanji", 9, "東アジア",
     "三一運動前夜の朝鮮社会をリアリズムで描く廉想渉の中編小説。"),
    ("金素月『つつじの花』民謡風叙情詩", "Chindallaekkot", "진달래꽃", "hangul", 9, "東アジア",
     "1925年の民謡的リズムで離別の情を歌う朝鮮近代詩の白眉。"),
    ("韓龍雲『君の沈黙』象徴詩集", "Nimui Chimmuk", "님의 침묵", "hangul", 9, "東アジア",
     "1926年の仏教的形而上学と民族意識を象徴する韓龍雲の詩集。"),
    ("李箱『烏瞰図』モダニズム連作詩", "Ogamdo by Yi Sang", "烏瞰圖", "kanji", 10, "東アジア",
     "1934年連載のシュルレアリスム的言語実験による前衛詩連作。"),

    # Cluster 3: 韓国現代 (6)
    ("朴婉緖『あの多くの草はだれが食べたのか』", "Geu Manon Singi", "그 많던 싱아는 누가 다 먹었을까", "hangul", 12, "東アジア",
     "1992年の朴婉緒による植民地・分断期の少女時代を回想する自伝小説。"),
    ("黄晳暎『林巨正』歴史長編", "Im by Hwang Sok-yong", "林巨正", "kanji", 12, "東アジア",
     "16世紀朝鮮の盗賊林巨正を主人公とする壮大な民衆史観歴史小説。"),
    ("李文烈『人間の子』神学小説", "Saramui Adeul", "사람의 아들", "hangul", 12, "東アジア",
     "1979年の李文烈による聖書再解釈と存在論的問いを扱う神学小説。"),
    ("申京淑『母をお願い』家族小説", "Eomma by Sin Kyong-suk", "엄마를 부탁해", "hangul", 12, "東アジア",
     "2008年の失踪した母を家族視点で語り直すベストセラー長編小説。"),
    ("韓江『菜食主義者』身体小説", "The Vegetarian", "채식주의자", "hangul", 12, "東アジア",
     "2007年の韓江による暴力拒絶と身体変容を描くブッカー国際賞受賞作。"),
    ("朴玟奎『ピンポン』前衛長編", "Pingpong by Park Min-gyu", "핑퐁", "hangul", 12, "東アジア",
     "2006年の朴玟奎によるいじめられた少年と地球の運命を交差させる長編。"),

    # Cluster 4: ベトナム+タイ (6)
    ("阮廌『平呉大誥』民族独立宣言", "Binh Ngo Dai Cao", "平吳大誥", "kanji", 98, "東南アジア",
     "1428年の明軍駆逐を宣する阮廌の漢文檄文でベトナム独立精神の古典。"),
    ("阮攸『金雲翹』字喃叙事詩", "Truyen Kieu", "傳翹", "nom", 98, "東南アジア",
     "19世紀初頭の阮攸による3,254行の字喃六八体叙事詩で国民文学。"),
    ("胡春香の字喃艶詩", "Ho Xuan Huong nom poems", "胡春香喃詩", "nom", 98, "東南アジア",
     "18-19世紀女性詩人胡春香の二重意味と性的諷刺を込めた字喃詩群。"),
    ("スントーン・プー『プラ・アパイ・マニ』", "Phra Aphai Mani", "พระอภัยมณี", "thai", 98, "東南アジア",
     "19世紀初頭スントーン・プーの王子の冒険を描くタイ古典長編詩。"),
    ("クラープ・サイプラディット『絵画の背景』", "Lae Phai", "ข้างหลังภาพ", "thai", 11, "東南アジア",
     "1937年シーブーラパーの叶わぬ恋を描くタイ近代ロマン主義小説。"),
    ("チャート・コープチッティ『判決』", "Khamphi Phipraksa", "คำพิพากษา", "thai", 12, "東南アジア",
     "1981年の村社会の偏見が無実の男を破滅させるタイ現代社会派長編。"),

    # Cluster 5: インドネシア+フィリピン (6)
    ("プラムディヤ『ブル四部作』植民地大河", "Buru Tetralogy", "Tetralogi Buru", "latin", 12, "東南アジア",
     "1980-88年プラムディヤがブル島流刑中に口述した四部作植民地史叙事。"),
    ("エカ・クルニアワン『美は傷』マジックリアリズム", "Cantik Itu Luka", "Cantik Itu Luka", "latin", 12, "東南アジア",
     "2002年エカ・クルニアワンが20世紀インドネシア史を幻想的に描く長編。"),
    ("アユ・ウタミ『サマン』ポスト・スハルト小説", "Saman by Ayu Utami", "Saman", "latin", 12, "東南アジア",
     "1998年改革期に女性4人の性と政治を描き話題となった革新的長編。"),
    ("リンダ・クリスタンティ短編集", "Linda Christanty short stories", "Kuda Terbang Maria Pinto", "latin", 12, "東南アジア",
     "アチェ紛争と政治暴力を女性視点で描くインドネシア現代短編作家。"),
    ("バラグタス『フロランテとラウラ』", "Florante at Laura", "Florante at Laura", "latin", 98, "東南アジア",
     "1838年バラグタスのタガログ語アウィット長詩でフィリピン民族文学の礎。"),
    ("ニック・ホアキン『熱帯のゴシック』短編集", "Tropical Gothic", "Tropical Gothic", "latin", 12, "東南アジア",
     "1972年ホアキンがマニラの植民地遺産と幻想を描く英語短編集の傑作。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for (name_ja, name_en, name_orig, script, period_id, region, definition) in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 17, ?, ?, ?, 4, 'tier1', 'yes')
            """, (name_ja, name_en, name_orig, script, region, period_id, definition))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=17")
    print(f"Total in subfield 17: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
