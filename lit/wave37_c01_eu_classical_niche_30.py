#!/usr/bin/env python3
"""Wave 37 cluster 1: lit_eu_classical NICHE 30 concepts."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# (name_ja, name_en, name_original, original_script, period_id, definition)
ROWS = [
    # 1: 希悲劇細部
    ("『ペルシア人』アイスキュロス", "Persae (Aeschylus)", "Πέρσαι", "greek", 6, "現存最古のギリシア悲劇。サラミス海戦を敗者ペルシア視点から描く哀歌劇。"),
    ("『テバイ攻めの七将』アイスキュロス", "Septem contra Thebas", "Ἑπτὰ ἐπὶ Θήβας", "greek", 6, "オイディプス家の呪いとエテオクレス・ポリュネイケスの兄弟相剋を描く。"),
    ("『トラキスの女たち』ソフォクレス", "Trachiniae", "Τραχίνιαι", "greek", 6, "デイアネイラの嫉妬とヘラクレスの死を描く家庭内悲劇の典型。"),
    ("『ヘカベ』エウリピデス", "Hecuba", "Ἑκάβη", "greek", 6, "トロイア陥落後のヘカベの復讐。母の悲嘆と人間性喪失を描く。"),
    ("『ヘレネ』エウリピデス", "Helena", "Ἑλένη", "greek", 6, "幻のヘレネー神話に基づくロマンス的悲劇。エイドロン主題の典拠。"),
    ("『リュシストラテ』アリストパネス", "Lysistrata", "Λυσιστράτη", "greek", 6, "性ストライキで戦争停止を実現する女性連帯喜劇。政治風刺の極北。"),
    # 2: 希詩・抒情
    ("バッキュリデス勝利歌", "Bacchylides Epinicia", "Ἐπίνικοι", "greek", 6, "ピンダロスと並ぶエピニキオン詩人。神話挿話と勝者称揚を結合。"),
    ("ステシコロス『ヘレネ』とパリノディア", "Stesichorus Helene", "Ἑλένη / Παλινῳδία", "greek", 5, "ヘレネー誹謗を撤回したパリノディアで知られる合唱抒情詩断片。"),
    ("イビュコス愛の断片", "Ibycus on Aphrodite", "Ἴβυκος", "greek", 5, "情念を稲妻・嵐に喩える官能的抒情詩断片群。サモス宮廷詩人。"),
    ("アナクレオン饗宴詩", "Anacreon symposion", "Ἀνακρέων", "greek", 5, "酒・愛・若さを軽やかに歌う饗宴詩。後世アナクレオンティカの源流。"),
    ("サッポー『アナクトリアへ』", "Sappho fr.16 Anactoria", "πρὸς Ἀνακτορίαν", "greek", 5, "「最も美しいのは愛する者」と説く相対主義的恋愛詩の極致。"),
    ("ピンダロス『ピューティア祝勝歌』", "Pindar Pythian Odes", "Πυθιόνικοι", "greek", 6, "デルポイ祝勝歌12篇。神話と教訓の三段構造で勝者を不滅化。"),
    # 3: 羅詩
    ("カトゥッルス第64歌", "Catullus Carmen 64", "Carmen 64", "latin", 73, "ペレウスとテティスの婚礼を描くエピュリオン。エクフラシスの傑作。"),
    ("ルクレティウス『事物の本性について』第3巻", "Lucretius DRN Book 3", "De Rerum Natura III", "latin", 73, "魂の死すべき本性を説き死の恐怖を解く哲学詩の核心巻。"),
    ("ホラティウス『談話集（諷刺詩）』", "Horace Sermones", "Sermones / Saturae", "latin", 74, "会話体六歩格による倫理的諷刺詩集。穏健諷刺(satura)の規範化。"),
    ("プロペルティウス『キュンティア』詩集", "Propertius Cynthia", "Cynthia (Monobiblos)", "latin", 74, "恋人キュンティアへの恋愛悲歌集。執着と挫折のエレゲイア。"),
    ("ティブッルス『デリア』詩集", "Tibullus Delia", "Delia", "latin", 74, "田園的牧歌調と恋人デリアへの愛を結合した穏和な恋愛悲歌集。"),
    ("オウィディウス『悲しみの歌』", "Ovid Tristia", "Tristia", "latin", 74, "黒海トミス追放中の哀歌5巻。流謫文学・自伝的悲歌の祖。"),
    # 4: 羅散文
    ("サッルスティウス『カティリーナ陰謀』", "Sallust Bellum Catilinae", "De Coniuratione Catilinae", "latin", 73, "共和政末期の道徳的退廃を診断する歴史モノグラフ。簡潔体の典型。"),
    ("タキトゥス『ゲルマニア』", "Tacitus Germania", "De origine et situ Germanorum", "latin", 75, "ゲルマン民族誌。ローマと対比した「高貴な野蛮人」像の原型。"),
    ("スエトニウス『ネロ伝』", "Suetonius Vita Neronis", "Vita Neronis", "latin", 75, "暴君ネロの伝記。逸話列挙型皇帝伝の代表で後世王伝の規範。"),
    ("プリニウス（小）書簡集", "Pliny the Younger Epistulae", "Epistulae", "latin", 75, "公私10巻書簡。ウェスウィウス噴火・キリスト教徒対応など一次資料。"),
    ("アプレイウス『黄金の驢馬』", "Apuleius Metamorphoses", "Metamorphoses", "latin", 75, "現存唯一の完全ラテン小説。クピド・プシュケ挿話を含む変身譚。"),
    ("ペトロニウス『トリマルキオの饗宴』", "Petronius Cena Trimalchionis", "Cena Trimalchionis", "latin", 75, "『サテュリコン』中の自由民富豪饗宴場面。俗ラテン口語の宝庫。"),
    # 5: 後期古代
    ("ルキアノス『本当の話』", "Lucian True History", "Ἀληθῆ Διηγήματα", "greek", 75, "月旅行を含む空想譚。SF・冒険小説の遠祖、誇張パロディの古典。"),
    ("ヘリオドロス『エチオピア物語』", "Heliodorus Aethiopica", "Αἰθιοπικά", "greek", 198, "テアゲネスとカリクレイアの恋愛冒険譚。古代恋愛小説の最高峰。"),
    ("ロンゴス『ダフニスとクロエ』", "Longus Daphnis and Chloe", "Δάφνις καὶ Χλόη", "greek", 198, "牧歌的舞台で展開する純朴な恋愛小説。田園恋愛小説の祖型。"),
    ("マクロビウス『サートゥルナーリア』", "Macrobius Saturnalia", "Saturnalia", "latin", 198, "祭礼の場で繰り広げる学識対話。古代知識の百科全書的継承。"),
    ("ボエティウス『哲学の慰め』運命の輪", "Boethius Wheel of Fortune", "Rota Fortunae", "latin", 198, "『慰め』第2巻の運命の輪論。中世フォルトゥーナ表象の源泉。"),
    ("クラウディアヌス『プロセルピナ強奪』", "Claudian De Raptu Proserpinae", "De Raptu Proserpinae", "latin", 198, "未完の神話叙事詩。ペルセフォネ誘拐譚。後期ラテン詩の最高峰。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for nj, ne, no, sc, pid, df in ROWS:
        if len(df) > 100:
            print(f"DEF TOO LONG ({len(df)}): {nj}", file=sys.stderr)
            sys.exit(1)
        try:
            cur.execute("""
                INSERT INTO concepts(name_ja, name_en, name_original, original_script,
                                     subfield_id, region, period_id, definition,
                                     importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, 1, '西欧', ?, ?, 3, 'A', 'yes')
            """, (nj, ne, no, sc, pid, df))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP (dup): {nj} -- {e}", file=sys.stderr)
            skipped += 1
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=1")
    print(f"Total in subfield 1: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
