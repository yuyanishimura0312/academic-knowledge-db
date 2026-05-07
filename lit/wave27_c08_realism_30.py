#!/usr/bin/env python3
"""Wave 27 / Cluster 08: Add 30 realism concepts to subfield 5 (lit_eu_realism)."""
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parent / "lit.sqlite"
SUBFIELD_ID = 5

# 5 clusters x 6 concepts. (name_ja, name_en, name_original, original_script, region, period_id, definition, importance, fourth_status, fourth_note, source_tier, canonical)
CONCEPTS = [
    # Cluster 1: French realism expansion
    ("ジョルジュ・サンド『プチット・ファデット』", "Sand: La Petite Fadette", "La Petite Fadette", "latin", "西欧", 120, "サンド田園小説三部作の一篇。ベリー地方を舞台に少女ファデットの成長と愛を描く。", 4, "partial", "農村共同体描写の現代再評価", "tier1", "yes"),
    ("ジョルジュ・サンド『コンスエロ』別系列", "Sand: Consuelo extended", "Consuelo", "latin", "西欧", 120, "歌姫コンスエロの遍歴を通じ芸術と神秘主義を描く長編。女性芸術家像の先駆的形象。", 4, "rethinking", "ジェンダー芸術論の再焦点化", "tier1", "yes"),
    ("ジョルジュ・サンド『レリア』", "Sand: Lélia", "Lélia", "latin", "西欧", 120, "1833年刊の哲学的小説。女性の懐疑と宗教的求道を語る、サンド初期の問題作。", 4, "rethinking", "女性の主体性とセクシュアリティ再考", "tier1", "partial"),
    ("ヴィニー『軍隊の服従と偉大』別系列", "Vigny: Servitude et grandeur militaires extended", "Servitude et grandeur militaires", "latin", "西欧", 120, "1835年発表。三話構成の軍人哲学小説。義務と尊厳を主題化する近代的軍隊倫理。", 3, "partial", "義務倫理の現代再読", "tier1", "partial"),
    ("ヴィニー『ステロ』", "Vigny: Stello", "Stello", "latin", "西欧", 120, "1832年発表。詩人と社会の緊張を三人の詩人例（ジルベール、チャタートン、シェニエ）で描く対話小説。", 3, "partial", "芸術家社会論の系譜", "tier1", "partial"),
    ("ピエール・ロティ『お菊さん』別系列", "Loti: Pêcheur d'Islande extended", "Pêcheur d'Islande", "latin", "西欧", 174, "ブルターニュ漁師の海と家族の悲劇。1886年作、海洋リアリズムの代表的長編。", 4, "partial", "辺境ローカリティの再評価", "tier1", "yes"),

    # Cluster 2: English realism expansion
    ("エリオット『フロス河の水車場』別系列", "Eliot: Mill on the Floss extended", "The Mill on the Floss", "latin", "西欧", 121, "1860年発表。マギー・タリヴァーの内的成長と兄弟愛、社会的束縛を描く半自伝的長編。", 5, "rethinking", "ジェンダーと家族倫理の再考", "tier1", "yes"),
    ("エリオット『ダニエル・デロンダ』別系列", "Eliot: Daniel Deronda extended", "Daniel Deronda", "latin", "西欧", 121, "1876年作。ユダヤ系アイデンティティと英国社会を交錯させる、エリオット最晩年の大作。", 5, "rethinking", "ディアスポラ・国民性の再焦点化", "tier1", "yes"),
    ("ハーディ『青い目の二人』別系列", "Hardy: A Pair of Blue Eyes extended", "A Pair of Blue Eyes", "latin", "西欧", 121, "1873年作。コーンウォールを舞台にした三角関係恋愛小説。ハーディ初期の重要作。", 4, "partial", "悲劇的リアリズム原型", "tier1", "partial"),
    ("トロロップ『今を生きる』別系列", "Trollope: The Way We Live Now extended", "The Way We Live Now", "latin", "西欧", 121, "1875年発表。金融詐欺と社会腐敗を描いた風刺的大長編。ヴィクトリア朝後期社会批評の到達点。", 4, "rethinking", "金融資本主義批評の現代再読", "tier1", "yes"),
    ("コンラッド『闇の奥』別系列", "Conrad: Heart of Darkness extended", "Heart of Darkness", "latin", "西欧", 174, "1899年作。コンゴ植民地を舞台に帝国主義の闇とアイデンティティ崩壊を描く中編傑作。", 5, "rethinking", "ポストコロニアル再読の中心テクスト", "tier1", "yes"),
    ("ウェルズ『トノ・バンゲイ』別系列", "Wells: Tono-Bungay extended", "Tono-Bungay", "latin", "西欧", 174, "1909年作。広告と虚業の経済を風刺するエドワード朝社会小説。商業主義リアリズム。", 3, "rethinking", "消費社会前夜の批評的再評価", "tier1", "partial"),

    # Cluster 3: German + Italian realism
    ("シュトルム『白馬の騎手』別系列", "Storm: Der Schimmelreiter extended", "Der Schimmelreiter", "latin", "西欧", 173, "1888年作。北ドイツ堤防地帯を舞台にした技術者と幽霊の悲劇的ノヴェレ。シュトルム最終傑作。", 4, "partial", "技術と自然の関係再考", "tier1", "yes"),
    ("ケラー『七つの伝説』別系列", "Keller: Sieben Legenden extended", "Sieben Legenden", "latin", "西欧", 173, "1872年作。中世聖人伝説を世俗化・人間化した連作。スイス詩的リアリズムの宝石的小品集。", 3, "partial", "宗教的物語の世俗化分析", "tier1", "partial"),
    ("ヴェルガ『はしばみ姫の物語』", "Verga: Storia di una capinera", "Storia di una capinera", "latin", "西欧", 171, "1871年作。修道院に閉ざされた少女の悲劇を書簡体で描く、ヴェリズモ前夜の感傷小説。", 3, "rethinking", "女性監禁ナラティヴの再評価", "tier1", "partial"),
    ("カプアーナ『ロッカヴェルディーナ侯爵』別系列", "Capuana: Il marchese di Roccaverdina extended", "Il marchese di Roccaverdina", "latin", "西欧", 171, "1901年作。シチリア貴族の罪と狂気を心理的精緻さで描いたヴェリズモ後期の傑作長編。", 4, "rethinking", "罪悪感心理の現代再読", "tier1", "yes"),
    ("ピランデッロ『故マッティーア・パスカル』別系列", "Pirandello: Il fu Mattia Pascal extended", "Il fu Mattia Pascal", "latin", "西欧", 171, "1904年作。死亡偽装者の自己同一性危機を描く、近代アイデンティティ崩壊の先駆的長編。", 5, "rethinking", "アイデンティティ流動性の最古典", "tier1", "yes"),
    ("デレッダ『灰』", "Deledda: Cenere", "Cenere", "latin", "西欧", 171, "1904年作。サルデーニャを舞台にした母子愛と贖罪の物語。映画化（1916）でも知られる。", 4, "partial", "辺境女性ナラティヴの再評価", "tier1", "yes"),

    # Cluster 4: Spanish + Portuguese realism
    ("ガルドス『トリスターナ』別系列", "Galdós: Tristana extended", "Tristana", "latin", "西欧", 172, "1892年作。後見人に支配される若い女性の解放闘争を描く、近代スペイン女性主義小説の里程標。", 4, "rethinking", "女性自立論の再焦点化", "tier1", "yes"),
    ("ガルドス『ミゼリコルディア』別系列", "Galdós: Misericordia extended", "Misericordia", "latin", "西欧", 172, "1897年作。マドリードの貧者と慈悲を描く社会的福音小説。スピリチュアリスト・リアリズムの到達。", 4, "partial", "貧困と霊性の現代再読", "tier1", "yes"),
    ("パルド・バサン『ラ・トリブナ』別系列", "Pardo Bazán: La Tribuna extended", "La Tribuna", "latin", "西欧", 172, "1883年作。タバコ工場女工アマパーロを主人公にした、スペイン初期女性労働者リアリズム。", 4, "rethinking", "労働とジェンダーの先駆的記述", "tier1", "partial"),
    ("クラリン『下り坂』", "Clarín: Cuesta abajo", "Cuesta abajo", "latin", "西欧", 172, "アラスの未完小説（1890-91）。スペイン・リアリズムの心理深化と没落主題を扱う。", 3, "partial", "未完テクスト再評価", "tier2", "partial"),
    ("ペレダ『ソティレサ』別系列", "Pereda: Sotileza extended", "Sotileza", "latin", "西欧", 172, "1885年作。サンタンデール漁村を舞台にした地方主義（コスツンブリスモ）リアリズムの代表作。", 3, "partial", "地方主義リアリズム再評価", "tier1", "partial"),
    ("エサ・デ・ケイロス『アマロ神父の罪』別系列", "Eça: O Crime do Padre Amaro extended", "O Crime do Padre Amaro", "latin", "西欧", 172, "1875年作。ポルトガルの聖職者の罪を解剖した、イベリア・リアリズムの記念碑的反教権長編。", 5, "rethinking", "宗教制度批評の古典再読", "tier1", "yes"),

    # Cluster 5: Russian + American realism
    ("ドストエフスキー『虐げられた人びと』別系列", "Dostoevsky: The Insulted and Injured extended", "Униженные и оскорблённые", "cyrillic", "西欧", 170, "1861年作。ペテルブルクの貧者と虐げられた人々を描く、本格期前夜のフェユトン的長編。", 4, "partial", "苦悩と慰めの現代再読", "tier1", "yes"),
    ("トルストイ『ハジ・ムラート』別系列", "Tolstoy: Hadji Murad extended", "Хаджи-Мурат", "cyrillic", "西欧", 170, "1912年没後刊行。チェチェン指導者の悲劇を通じ帝国の暴力を抉る最晩年の中編傑作。", 5, "rethinking", "植民地暴力批判の先駆", "tier1", "yes"),
    ("ツルゲーネフ『煙』別系列", "Turgenev: Smoke extended", "Дым", "cyrillic", "西欧", 170, "1867年作。バーデン=バーデンを舞台にロシア知識人の幻滅を描く、政治的論争を呼んだ長編。", 4, "partial", "亡命知識人論の現代再読", "tier1", "yes"),
    ("ゴンチャロフ『平凡物語』別系列", "Goncharov: An Ordinary Story extended", "Обыкновенная история", "cyrillic", "西欧", 170, "1847年作。地方青年の理想主義崩壊と都会的順応を描いた、ロシア・リアリズム初期の代表作。", 4, "partial", "若者の理想主義喪失再評価", "tier1", "yes"),
    ("ノリス『マクティーグ』別系列", "Norris: McTeague extended", "McTeague", "latin", "西欧", 122, "1899年作。サンフランシスコ歯科助手の堕落を描く、米国自然主義の決定的長編。", 5, "rethinking", "自然主義的決定論の現代再読", "tier1", "yes"),
    ("ウォートン『無垢の時代』別系列", "Wharton: The Age of Innocence extended", "The Age of Innocence", "latin", "西欧", 122, "1920年作。19世紀末ニューヨーク上流社会の慣習と個人の葛藤を描いたピューリッツァ受賞長編。", 5, "rethinking", "上流社会慣習の批評的再読", "tier1", "yes"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        (name_ja, name_en, name_orig, script, region, period_id,
         definition, importance, fstatus, fnote, tier, canonical) = c
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script,
                 subfield_id, region, period_id, definition,
                 importance_score, fourth_transform_status, fourth_transform_note,
                 source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script,
                  SUBFIELD_ID, region, period_id, definition,
                  importance, fstatus, fnote, tier, canonical))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
    conn.commit()
    conn.close()
    print(f"inserted={inserted} skipped={skipped}")

if __name__ == "__main__":
    main()
