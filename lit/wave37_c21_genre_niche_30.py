#!/usr/bin/env python3
"""Wave 37 Cluster 21: Genre niche - 30 concepts across 5 thematic clusters."""
import sqlite3
import sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"

# 5 clusters x 6 concepts = 30
CONCEPTS = [
    # Cluster 1: 探偵推理ジャンル
    ("ロックト・ルーム・ミステリ", "Locked-room mystery", "locked-room mystery", "latin",
     "密室殺人を論理で解明するミステリ下位ジャンル。Carrを代表に不可能犯罪の趣向を競う形式", 150, "世界"),
    ("ノワール／ハードボイルド", "Noir/Hardboiled", "noir", "latin",
     "都市の暗部と幻滅した一人称探偵を描くハードボイルド系統。Hammett・Chandler・Cain派生", 150, "世界"),
    ("コージー・ミステリ", "Cozy mystery", "cozy mystery", "latin",
     "小規模共同体・素人探偵・暴力描写抑制のミステリ。Christie系譜のサブジャンル", 150, "世界"),
    ("警察小説（ポリス・プロシージャル）", "Police procedural", "police procedural", "latin",
     "警察組織の捜査手続きを写実的に描くミステリ。McBain・Sjöwall&Wahlöö等を代表", 150, "世界"),
    ("倒叙ミステリ（インヴァーテッド）", "Inverted detective", "inverted detective", "latin",
     "犯人を冒頭で開示し追及過程を描くミステリ形式。Crofts・Freeman起源、刑事コロンボ等", 150, "世界"),
    ("ハウキャッチェム", "Howcatchem", "howcatchem", "latin",
     "犯人既知でいかに捕えるかを焦点化する倒叙派生形式。Columbo型構造を指す批評語", 150, "世界"),

    # Cluster 2: SFサブジャンル
    ("サイバーパンク", "Cyberpunk", "cyberpunk", "latin",
     "ハイテク低生活・身体改造・電脳空間を描くSF。Gibson・Sterling・Shirleyが旗手", 150, "世界"),
    ("ソーラーパンク", "Solarpunk", "solarpunk", "latin",
     "再生可能エネルギーと共生社会を描く希望志向SF。2010年代台頭、気候危機への応答", 150, "世界"),
    ("クライ・フィ（気候フィクション）", "Climate fiction", "cli-fi", "latin",
     "気候変動を主題化する文学ジャンル。Robinson・Atwood・Ghoshが理論化と実作を牽引", 150, "世界"),
    ("マンデーンSF", "Mundane SF", "mundane SF", "latin",
     "FTL等の不可能設定を排し近未来現実に基づくSF運動。2004年Ryman宣言が起点", 150, "世界"),
    ("ハードSFとソフトSFの対比", "Hard SF vs Soft SF", "hard SF / soft SF", "latin",
     "自然科学厳密性志向と人文社会志向の対立軸。Campbell系/New Wave系の分岐を概念化", 150, "世界"),
    ("アフロフューチャリズム文学", "Afrofuturism (literary)", "Afrofuturism", "latin",
     "アフリカ系の未来想像力を中心に据える文学運動。Butler・Delany・Okoraforが代表", 150, "世界"),

    # Cluster 3: ファンタジー細分
    ("ソード・アンド・ソーサリー", "Sword and sorcery", "sword and sorcery", "latin",
     "個人英雄の冒険と魔術を主軸とするファンタジー下位形式。Howard・Leiberが定式化", 150, "世界"),
    ("ハイ・ファンタジー", "High fantasy", "high fantasy", "latin",
     "二次世界舞台と善悪叙事詩を特徴とするファンタジー形式。Tolkien・Lewisが確立", 150, "世界"),
    ("アーバン・ファンタジー", "Urban fantasy", "urban fantasy", "latin",
     "現代都市と魔術的存在の混淆を描くファンタジー。de Lint・Gaiman・Butcherが代表", 150, "世界"),
    ("マジックリアリズムとファンタジーの境界", "Magic realism vs fantasy", "magic realism / fantasy", "latin",
     "幻想を日常に内在化させるラ米マジックリアリズムと西洋ファンタジーの理論的分節", 150, "世界"),
    ("グリムダーク", "Grimdark", "grimdark", "latin",
     "道徳的曖昧と暴力的世界観を強調するファンタジー潮流。Abercrombie・Martinが代表", 150, "世界"),
    ("ホープパンク", "Hopepunk", "hopepunk", "latin",
     "シニシズムに抗し連帯と希望を志向するジャンル運動。2017年Rowland命名、SF/F横断", 150, "世界"),

    # Cluster 4: ロマンス・YA
    ("ロマンス小説（ジャンル理論）", "Romance subgenre theory", "romance genre", "latin",
     "HEA/HFN規約・サブジャンル分化を持つ商業ジャンル。Regis・Ramsdell等が理論化", 150, "世界"),
    ("ボディスリッパー", "Bodice ripper", "bodice ripper", "latin",
     "1970年代から流行した官能歴史ロマンスの俗称。Woodiwiss『炎と花』が嚆矢", 150, "世界"),
    ("チック・リット", "Chick lit", "chick lit", "latin",
     "都市独身女性の生活と恋愛を一人称で描く商業文学。Fielding『ブリジット・ジョーンズ』が起点", 150, "世界"),
    ("YA教養小説（Bildungsroman YA）", "Bildungsroman YA", "YA Bildungsroman", "latin",
     "ヤングアダルト世代の自己形成を主題化した教養小説の現代変奏。Green・Chbosky等", 150, "世界"),
    ("ニューアダルト", "New Adult", "New Adult", "latin",
     "18-25歳主人公層を対象とする2009年台頭の出版カテゴリ。YAと一般文芸の橋渡し", 150, "世界"),
    ("LGBTQ+ロマンス", "LGBTQ+ romance", "LGBTQ+ romance", "latin",
     "クィア当事者の恋愛を中心化するロマンス系統。M/M・F/F・トランス等の細分化進展", 150, "世界"),

    # Cluster 5: 戦争小説・歴史小説
    ("戦争小説", "War novel", "war novel", "latin",
     "戦闘・前線・戦争体験を主題とする小説ジャンル。Tolstoy・Remarque・Mailerを系譜とする", 150, "世界"),
    ("反戦文学", "Anti-war literature", "anti-war literature", "latin",
     "戦争批判を中心化する文学潮流。Remarque・Heller・Vonnegutが20世紀の軸を成す", 150, "世界"),
    ("歴史小説", "Historical fiction", "historical fiction", "latin",
     "実在の過去を舞台に虚構を織り込むジャンル。Scott起源、20世紀以降に多様化", 150, "世界"),
    ("オルタネート・ヒストリー", "Alternate history", "alternate history", "latin",
     "歴史改変を前提に別の現代を構築する形式。Dick『高い城の男』Roth『プロット』等", 150, "世界"),
    ("歴史叙述メタフィクション", "Historiographic metafiction", "historiographic metafiction", "latin",
     "歴史叙述の構成性を自己言及的に問う後期近代小説形式。Hutcheonが理論化", 150, "世界"),
    ("サーガ小説", "Saga novel", "saga novel", "latin",
     "複数世代・家系を追う長大な叙事的小説形式。Mann・Galsworthy・Mahfouzが代表", 150, "世界"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Find period for late 20c/21c, region '世界'
    cur.execute("SELECT id FROM periods WHERE region='世界' AND (name_ja LIKE '%20世紀後半%' OR name_ja LIKE '%21世紀%') ORDER BY id LIMIT 1")
    row = cur.fetchone()
    if not row:
        # Fallback: any period_id with region '世界'
        cur.execute("SELECT id FROM periods WHERE region='世界' ORDER BY id LIMIT 1")
        row = cur.fetchone()
    period_id = row[0] if row else None
    print(f"period_id = {period_id}")

    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, defn, importance, region in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                                      subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, 21, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, region, period_id, defn[:100], importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)

    conn.commit()
    print(f"INSERTED={inserted} SKIPPED={skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=21")
    print(f"TOTAL subfield_id=21: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
