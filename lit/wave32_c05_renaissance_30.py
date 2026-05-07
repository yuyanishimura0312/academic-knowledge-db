#!/usr/bin/env python3
"""Wave 32 Cluster 05: Renaissance/Early Modern Western Europe (30 concepts)"""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 3
REGION = "西欧"

# Cluster 1: Italian Renaissance | Cluster 2: French | Cluster 3: Spanish Golden Age
# Cluster 4: English Tudor/Jacobean | Cluster 5: Northern Renaissance
CONCEPTS = [
    # 1. Italian Renaissance
    ("ペトラルカ『カンツォニエーレ』ラウラ詩篇", "Petrarch Canzoniere Laura sequence", "Rerum vulgarium fragmenta", "latin", 43,
     "ラウラへの愛をソネットで紡ぐ俗語抒情詩集、ペトラルキスムの源泉。", 5),
    ("ポリツィアーノ『スタンツェ』詩学", "Poliziano Stanze poetics", "Stanze per la giostra", "latin", 42,
     "メディチ家のために綴られた未完の俗語叙事詩、神話と恋愛の融合。", 4),
    ("サンナザーロ『アルカディア』牧歌散文", "Sannazaro Arcadia pastoral prose", "Arcadia", "latin", 43,
     "韻文と散文を交えた牧歌小説、近世パストラル小説の祖型。", 5),
    ("ボイアルド『恋するオルランド』騎士道叙事", "Boiardo Orlando Innamorato chivalric epic", "Orlando innamorato", "latin", 42,
     "シャルルマーニュ伝説と恋愛物語を融合した俗語騎士道叙事詩。", 4),
    ("アレティーノ『対話篇（ラジョナメンティ）』風刺", "Aretino Ragionamenti satire", "Ragionamenti", "latin", 43,
     "娼婦の対話形式で社会を風刺した俗語散文、近世エロティカの先駆。", 4),
    ("ヴァザーリ『芸術家列伝』批評詩学", "Vasari Vite critical poetics", "Le Vite", "latin", 43,
     "美術家伝記を通じた様式史叙述、芸術批評文学の基礎を築く。", 5),

    # 2. French Renaissance
    ("マロ『青年詩集』短詩形", "Marot Adolescence Clémentine short forms", "L'Adolescence clémentine", "latin", 146,
     "ロンドー・バラードを刷新した俗語短詩集、フランス近世詩の幕開け。", 5),
    ("ロンサール『カッサンドルへの愛』詩編", "Ronsard Amours de Cassandre", "Les Amours de Cassandre", "latin", 146,
     "プレイヤード派の代表的ペトラルカ風ソネット連作。", 5),
    ("デュ・ベレー『ローマの古蹟』詩集", "Du Bellay Antiquités de Rome", "Les Antiquités de Rome", "latin", 146,
     "古代ローマ廃墟を瞑想する俗語ソネット集、廃墟美学の先駆。", 5),
    ("マルグリット・ド・ナヴァール『エプタメロン』物語", "Marguerite Heptaméron tales", "L'Heptaméron", "latin", 146,
     "ボッカッチョ枠物語に倣う仏語ノヴェッラ集、宗教改革期の女性視点。", 5),
    ("ラブレー『パンタグリュエル』巨人物語", "Rabelais Pantagruel giant narrative", "Pantagruel", "latin", 146,
     "巨人王の冒険を通じた人文主義と諷刺の融合、カーニヴァル文学の精華。", 5),
    ("モンテーニュ『エセー』第三巻自己探究", "Montaigne Essais Book III self-inquiry", "Les Essais Livre III", "latin", 146,
     "成熟期の長編エセーで自己観察と懐疑を深化させた近世散文の頂点。", 5),

    # 3. Spanish Golden Age
    ("セルバンテス『ドン・キホーテ』第二部メタ虚構", "Cervantes Don Quixote Part II metafiction", "Don Quijote II", "latin", 43,
     "第一部の存在を作中で扱う先駆的メタ虚構小説、近代小説の原型。", 5),
    ("ロペ・デ・ベガ『フエンテオベフナ』集団主人公劇", "Lope Fuenteovejuna collective protagonist", "Fuenteovejuna", "latin", 43,
     "村全体を主人公とする民衆劇、コメディア・ヌエバの政治的頂点。", 5),
    ("カルデロン『人生は夢』哲学劇", "Calderón La vida es sueño philosophical drama", "La vida es sueño", "latin", 43,
     "幻想と現実の境界を問うバロック哲学劇、自由意志の考察。", 5),
    ("ティルソ・デ・モリーナ『セビーリャの色事師』ドン・ファン創出", "Tirso Burlador de Sevilla Don Juan origin", "El burlador de Sevilla", "latin", 43,
     "ドン・ファン伝説を演劇化した原典、誘惑者アーキタイプの誕生。", 5),
    ("ケベード『ブスコン』ピカレスク完成形", "Quevedo Buscón picaresque culmination", "El Buscón", "latin", 43,
     "コンセプティスモ文体で綴られた最も洗練されたピカレスク小説。", 5),
    ("ゴンゴラ『ソレダーデス』クルテラニスモ詩学", "Góngora Soledades culteranismo", "Soledades", "latin", 43,
     "難解なラテン語法と隠喩を駆使した俗語牧歌詩、バロック詩の極致。", 5),

    # 4. English Tudor/Jacobean
    ("シドニー『アストロフェルとステラ』英語ソネット連作", "Sidney Astrophil and Stella sonnet sequence", "Astrophil and Stella", "latin", 43,
     "英語最初の本格的ペトラルカ風ソネット連作、エリザベス朝詩学の規範。", 5),
    ("スペンサー『妖精の女王』第一巻聖性の騎士", "Spenser Faerie Queene Book I Holiness", "The Faerie Queene Book I", "latin", 43,
     "聖性を擬人化した騎士の遍歴を描くアレゴリー叙事詩、英国ルネサンス頂点。", 5),
    ("マーロウ『フォースタス博士』ファウスト劇", "Marlowe Doctor Faustus", "The Tragical History of Doctor Faustus", "latin", 43,
     "悪魔と契約する学者を描くブランクヴァース悲劇、知識への欲望の悲劇。", 5),
    ("ダン『歌とソネット』形而上派詩学", "Donne Songs and Sonnets metaphysical poetics", "Songs and Sonnets", "latin", 43,
     "知性的奇想（コンチェット）と感覚的肉体性を融合した形而上派詩の核。", 5),
    ("ベン・ジョンソン『ヴォルポーネ』風刺喜劇", "Jonson Volpone satirical comedy", "Volpone, or The Fox", "latin", 43,
     "貪欲な狐ヴォルポーネを軸とする体液論的風刺喜劇、ジャコビアン喜劇の代表。", 5),
    ("ウェブスター『マルフィ公爵夫人』復讐悲劇", "Webster The Duchess of Malfi revenge tragedy", "The Duchess of Malfi", "latin", 43,
     "未亡人公爵夫人の悲劇を描くジャコビアン暗黒悲劇、宮廷の腐敗を凝視する。", 5),

    # 5. Northern Renaissance
    ("エラスムス『痴愚神礼賛』風刺", "Erasmus Praise of Folly satire", "Stultitiae Laus", "latin", 148,
     "痴愚女神に教会と社会を語らせる人文主義的諷刺、北方ルネサンスの代表作。", 5),
    ("ルター『卓上語録』口承文学", "Luther Tischreden table talk", "Tischreden", "latin", 148,
     "弟子が記録したルターの食卓談話集、口承宗教文学の独自ジャンル。", 4),
    ("ブラント『阿呆船』教訓詩", "Brant Narrenschiff didactic verse", "Das Narrenschiff", "latin", 148,
     "百一種の阿呆を船に乗せ風刺する独語教訓詩、阿呆文学の元祖。", 5),
    ("トマス・モア『ユートピア』理想郷文学", "Thomas More Utopia ideal commonwealth", "De optimo rei publicae statu deque nova insula Utopia", "latin", 148,
     "ラテン語で書かれた架空島の社会批評、ユートピア文学ジャンルの起点。", 5),
    ("フォンデル『ルシファー』天使悲劇", "Vondel Lucifer angelic tragedy", "Lucifer", "latin", 148,
     "堕天使ルシファーの反逆を描く蘭語古典悲劇、ミルトンへの影響源。", 4),
    ("カルヴァン『キリスト教綱要』文学性", "Calvin Institutes literary qualities", "Institutio Christianae Religionis", "latin", 148,
     "神学体系書でありながら仏語散文の規範を示した宗教改革文学。", 4),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for nj, ne, no, script, pid, defi, imp in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, original_script, subfield_id, region, period_id,
                 definition, importance_score, source_tier, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nj, ne, no, script, SUBFIELD_ID, REGION, pid, defi, imp, "tier1", "yes"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {nj}: {e}")
    conn.commit()
    conn.close()
    print(f"INSERTED={inserted} SKIPPED={skipped} TOTAL={len(CONCEPTS)}")

if __name__ == "__main__":
    main()
