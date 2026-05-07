#!/usr/bin/env python3
"""Wave37 C05: Renaissance niche 30 concepts for subfield_id=3 (lit_eu_renaissance)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 3

# (name_ja, name_en, name_original, original_script, region, period_id, definition, importance)
CONCEPTS = [
    # 1: 仏ルネサンス（フランス・ルネサンス期 146、盛期・後期ルネサンス期 43）
    ("マロ『青年詩集』短詩形式", "Marot Adolescence clémentine", "L'Adolescence clémentine", "latin", "西欧", 146, "クレマン・マロの初期詩集。短詩形・口語性で仏ルネサンス詩の出発点。", 4),
    ("スポンド『愛と死のソネット』", "Sponde Sonnets on Love and Death", "Sonnets sur l'amour et sur la mort", "latin", "西欧", 146, "ジャン・ド・スポンドのバロック前夜の宗教的ソネット連作。", 3),
    ("ドービニェ『悲愴詩集』七巻", "Aubigné Les Tragiques", "Les Tragiques", "latin", "西欧", 146, "アグリッパ・ドービニェの宗教戦争叙事詩。プロテスタント的予言詩。", 4),
    ("デュ・バルタス『七日聖週間』", "Du Bartas La Sepmaine", "La Sepmaine ou Création du monde", "latin", "西欧", 146, "ギヨーム・デュ・バルタスの天地創造叙事詩。欧州バロック宗教詩に影響。", 3),
    ("パスキエ『フランス研究』", "Pasquier Recherches de la France", "Les Recherches de la France", "latin", "西欧", 146, "エチエンヌ・パスキエの仏文化史的散文。俗語擁護と国民文学意識の確立。", 3),
    ("エチエンヌ『ヘロドトス弁護』", "Estienne Apologie pour Hérodote", "Apologie pour Hérodote", "latin", "西欧", 146, "アンリ・エチエンヌの諷刺的歴史書。古典学識と宗教論争を結合。", 3),

    # 2: 伊宮廷詩（イタリア・ルネサンス期 144、盛期・後期 43、バロック後期 249）
    ("ベンボ『アゾラーニ』恋愛対話", "Bembo Asolani", "Gli Asolani", "latin", "西欧", 144, "ピエトロ・ベンボの宮廷恋愛対話篇。プラトニスムと俗語規範の結合。", 4),
    ("カスティリオーネ『宮廷人』対話", "Castiglione Il Cortegiano", "Il libro del Cortegiano", "latin", "西欧", 144, "理想宮廷人像の対話篇。スプレッツァトゥーラ概念の典拠。", 5),
    ("ベルニ滑稽詩 rime burlesche", "Berni rime burlesche", "Rime burlesche", "latin", "西欧", 144, "フランチェスコ・ベルニの低俗模写諷刺詩。反ペトラルキスム派の中核。", 3),
    ("プルチ『大モルガンテ』騎士道", "Pulci Morgante", "Il Morgante", "latin", "西欧", 144, "ルイジ・プルチの諧謔的騎士道叙事。フィレンツェ宮廷の口承文化。", 3),
    ("ボイアルド『恋するオルランド』", "Boiardo Orlando Innamorato", "Orlando Innamorato", "latin", "西欧", 144, "マッテーオ・ボイアルドの未完騎士道叙事。アリオストの直接的源泉。", 4),
    ("マリーノ『アドーネ』バロック叙事", "Marino L'Adone", "L'Adone", "latin", "西欧", 249, "ジャンバッティスタ・マリーノの感覚的長編叙事。マリニスム源泉。", 4),

    # 3: 西黄金世紀（黄金世紀 45、スペイン黄金時代 145）
    ("ガルシラーソ『第一牧歌』", "Garcilaso Égloga primera", "Égloga primera", "latin", "西欧", 145, "ガルシラーソ・デ・ラ・ベガの牧歌詩。伊風詩形を西語へ移植。", 4),
    ("フライ・ルイス『澄んだ夜』", "Fray Luis Noche serena", "Noche serena", "latin", "西欧", 145, "フライ・ルイス・デ・レオンの神秘的頌歌。新プラトニスム的天空観想。", 3),
    ("ケベード『夢』連作諷刺", "Quevedo Sueños", "Los Sueños", "latin", "西欧", 45, "フランシスコ・デ・ケベードの寓意的諷刺散文。コンセプティスモの実践。", 4),
    ("ゴンゴラ『孤独』詩学", "Góngora Soledades", "Soledades", "latin", "西欧", 45, "ルイス・デ・ゴンゴラの未完長詩。クルテラニスモの極致。", 5),
    ("ロペ『新作劇法』詩論", "Lope Arte nuevo", "Arte nuevo de hacer comedias", "latin", "西欧", 45, "ロペ・デ・ベガの俗衆向け新喜劇詩論。三一致解体の宣言。", 4),
    ("カルデロン『人生は夢』哲学劇", "Calderón La vida es sueño", "La vida es sueño", "latin", "西欧", 45, "カルデロンの自由意志と運命を巡る形而上的バロック劇。", 5),

    # 4: 英ルネサンス散文（テューダー・ジャコビアン期 147、エリザベス朝 44）
    ("シドニー『アルカディア』牧歌散文", "Sidney Arcadia", "The Countess of Pembroke's Arcadia", "latin", "西欧", 147, "フィリップ・シドニーの牧歌的散文ロマンス。英散文虚構の起点。", 4),
    ("リリー『ユーフィーズ』修辞", "Lyly Euphues", "Euphues: The Anatomy of Wit", "latin", "西欧", 147, "ジョン・リリーの装飾過多な散文。ユーフィーイズム文体を生む。", 3),
    ("グリーン『パンドストー』ロマンス", "Greene Pandosto", "Pandosto: The Triumph of Time", "latin", "西欧", 147, "ロバート・グリーンの牧歌ロマンス。『冬物語』の典拠。", 3),
    ("ナッシュ『不運な旅人』", "Nashe Unfortunate Traveller", "The Unfortunate Traveller", "latin", "西欧", 147, "トマス・ナッシュのピカレスク的英散文。元祖英国小説と称される。", 3),
    ("ロッジ『ロザリンド』牧歌", "Lodge Rosalynde", "Rosalynde: Euphues' Golden Legacy", "latin", "西欧", 147, "トマス・ロッジの牧歌散文ロマンス。『お気に召すまま』の典拠。", 3),
    ("アスカム『教師』教育論", "Ascham The Schoolmaster", "The Scholemaster", "latin", "西欧", 147, "ロジャー・アスカムのチューダー期教育論。古典模倣論と俗語擁護。", 3),

    # 5: 独・北欧（北方ルネサンス期 148、中世末期ゲルマン圏 119）
    ("ザックス謝肉祭劇 Fastnachtspiel", "Hans Sachs Shrovetide play", "Fastnachtspiel", "latin", "西欧", 148, "ハンス・ザックスの市民謝肉祭劇。ドイツ俗語短劇の規範形式。", 3),
    ("ブラント『阿呆船』ラテン版翻案", "Locher Stultifera Navis", "Stultifera Navis", "latin", "西欧", 148, "ヤーコプ・ローハーによるブラントのラテン語翻案。汎欧州伝播の媒介。", 3),
    ("ゼバスティアン・フランク年代記", "Sebastian Franck Chronica", "Chronica, Zeitbuch und Geschichtbibel", "latin", "西欧", 148, "急進宗教改革者の歴史散文。霊主義と俗語史学の融合。", 3),
    ("フィッシャルト『ガルガンチュア』訳", "Fischart Geschichtklitterung", "Geschichtklitterung", "latin", "西欧", 148, "ヨハン・フィッシャルトのラブレー独訳的翻案。言語的奔放さの極致。", 3),
    ("ペッテル・ダス『ノルランの喇叭』", "Petter Dass Nordlands Trompet", "Nordlands Trompet", "latin", "西欧", 249, "ノルウェー牧師詩人ダスの北方地誌詩。北欧バロック地方詩の到達点。", 3),
    ("ボーディング バロック抒情", "Anders Bording Den Danske Mercurius", "Den Danske Mercurius", "latin", "西欧", 249, "デンマーク詩人ボーディングの韻文新聞。北欧バロック俗語詩の試み。", 3),
]


def main() -> None:
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for c in CONCEPTS:
        (name_ja, name_en, name_original, original_script, region, period_id, definition, importance) = c
        assert len(definition) <= 100, f"def too long ({len(definition)}): {name_ja}"
        try:
            cur.execute(
                """
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id, definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'tier2', 'niche')
                """,
                (name_ja, name_en, name_original, original_script, SUBFIELD_ID, region, period_id, definition, importance),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    print(f"Inserted={inserted} Skipped={skipped} Total={len(CONCEPTS)}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    print(f"Subfield {SUBFIELD_ID} total now: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
