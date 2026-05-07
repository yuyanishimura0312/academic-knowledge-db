#!/usr/bin/env python3
"""Wave 37: 30 niche concepts for subfield 23 (lit_world_translation)."""
import sqlite3
import sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 23
PERIOD_ID = 58  # 世界文学・ポストコロニアル翻訳期 (理論)
REGION = "横断"

CONCEPTS = [
    # Cluster 1: 翻訳理論細部 (6)
    ("スコポス理論（フェルメーア精読）", "Skopos Theory (Vermeer)", "Skopostheorie",
     "翻訳の目的（スコポス）が方法を決定するとするフェルメーアの機能主義理論。"),
    ("ポリシステム理論（エヴェン=ゾーハー精読）", "Polysystem Theory (Even-Zohar)", "Polysystem Theory",
     "翻訳文学を受容文化の文学システム内の動的位置として捉えるイスラエル学派の理論。"),
    ("翻訳規範論（トゥーリ）", "Translation Norms (Toury)", "Translation Norms",
     "翻訳行動を規定する初期・操作・予備規範を記述するトゥーリの規範概念。"),
    ("操作学派（ヘルマンス）", "Manipulation School (Hermans)", "Manipulation School",
     "翻訳をテクスト操作として捉える低地国家系学派、ヘルマンス『文学操作』が起点。"),
    ("文化的転回（バスネット精読）", "Cultural Turn (Bassnett)", "Cultural Turn",
     "翻訳学を言語等価から文化交渉へ移したバスネット&ルフェーヴル1990年の転回。"),
    ("社会学的転回（ウォルフ）", "Sociological Turn (Wolf)", "Sociological Turn",
     "ブルデュー社会学を翻訳研究に導入し、行為者・場・資本を分析するウォルフの転回。"),

    # Cluster 2: 文芸翻訳実践 (6)
    ("ペヴェア=ヴォロホンスキー（ロシア文学）", "Pevear & Volokhonsky (Russian)", "Pevear-Volokhonsky",
     "ドストエフスキー・トルストイ等の英訳を刷新した夫婦共訳チーム、逐語性重視。"),
    ("イーディス・グロスマン（スペイン語圏）", "Edith Grossman (Spanish)", "Edith Grossman",
     "ガルシア=マルケス・セルバンテス『ドン・キホーテ』英訳で著名な米国翻訳家。"),
    ("アンシア・ベル（独仏児童文学）", "Anthea Bell (German/French)", "Anthea Bell",
     "ゼーバルト・カフカ・アステリックスを英訳した英国翻訳家、文化的脚色の名手。"),
    ("リディア・デイヴィス（プルースト英訳）", "Lydia Davis (Proust)", "Lydia Davis",
     "プルースト『スワン家の方へ』新訳・フローベール『ボヴァリー夫人』英訳の作家翻訳家。"),
    ("ドン・バートレット（クナウスゴール英訳）", "Don Bartlett (Knausgård)", "Don Bartlett",
     "クナウスゴール『わが闘争』全6巻を英訳したノルウェー文学英国翻訳家。"),
    ("ジェイ・ルービン（村上春樹英訳）", "Jay Rubin (Murakami)", "Jay Rubin",
     "村上春樹『ねじまき鳥クロニクル』『1Q84』英訳のハーバード日本文学者。"),

    # Cluster 3: 翻訳と政治 (6)
    ("検閲下の翻訳（独裁体制）", "Translation Under Censorship", "Translation Censorship",
     "ナチス・ソ連・フランコ等の体制下で翻訳が検閲・自己検閲される歴史的現象。"),
    ("擬似翻訳（トゥーリ）", "Pseudo-translation (Toury)", "Pseudo-translation",
     "翻訳と称する原作のないテクスト。トゥーリが規範回避戦略として理論化。"),
    ("自己翻訳（ベケット）", "Self-translation (Beckett)", "Self-translation: Beckett",
     "ベケットによる仏英自己翻訳の実践、原作と訳作の境界を脱構築する事例。"),
    ("自己翻訳（ナボコフ）", "Self-translation (Nabokov)", "Self-translation: Nabokov",
     "ナボコフが露英間で自作を翻訳し改作する実践、『絶望』『ロリータ』が代表例。"),
    ("間接翻訳・リレー翻訳", "Indirect Translation / Relay", "Indirect Translation",
     "中継言語を経由する翻訳、周縁言語文学の流通における政治経済的不均衡を露呈する。"),
    ("ディアスポラ翻訳者の主体性", "Diasporic Translator Agency", "Diasporic Translator Agency",
     "移民・亡命翻訳者が母語と受容語の間で発揮する文化的・政治的主体性概念。"),

    # Cluster 4: 機械翻訳・AI翻訳 (6)
    ("ニューラル機械翻訳（NMT）", "Neural Machine Translation (NMT)", "Neural Machine Translation",
     "Transformer等のニューラル網を用いた機械翻訳、2014年以降主流となった技術系譜。"),
    ("ポストエディット（PEMT）", "Post-editing (PEMT)", "Post-editing Machine Translation",
     "機械翻訳出力を人間が修正する作業、産業翻訳の標準ワークフロー。"),
    ("翻訳メモリ・CATツール", "Translation Memory / CAT", "Translation Memory",
     "Trados等のCATツールが用いる対訳セグメント蓄積技術、産業翻訳の基盤。"),
    ("AI文学翻訳論争", "AI Literary Translation Debate", "AI Literary Translation Debate",
     "GPT等が文学翻訳で人間を代替可能かを巡る2020年代の翻訳学・産業界論争。"),
    ("ChatGPTによる詩翻訳", "ChatGPT Poetry Translation", "ChatGPT Poetry Translation",
     "大規模言語モデルによる詩翻訳の実験と、リズム・暗示性の限界を巡る評価議論。"),
    ("Human-in-the-loop文学翻訳", "Human-in-the-loop Literary Translation", "Human-in-the-loop Literary",
     "AI出力に文学翻訳家が介入する協働モデル、創造性と効率の均衡を模索する手法。"),

    # Cluster 5: 世界文学循環 (6)
    ("ダムロッシュ『世界文学とは何か』精読", "Damrosch What is World Literature", "What Is World Literature?",
     "ダムロッシュが世界文学を「翻訳を通じた循環・読解様式」として再定義した2003年著作。"),
    ("カサノヴァ『文学の世界共和国』", "Casanova World Republic of Letters", "La République mondiale des Lettres",
     "ブルデュー社会学で世界文学場の不平等構造とパリ中心性を分析した1999年著作。"),
    ("モレッティ「遠読」", "Moretti Distant Reading", "Distant Reading",
     "個別精読を超え世界文学を量的・図表的に分析するモレッティの方法論的提言。"),
    ("アプター『翻訳不可能なもの』", "Apter Against World Literature", "Against World Literature",
     "アプターが翻訳不可能性を擁護し世界文学の流通主義を批判した2013年著作。"),
    ("バッタチャリヤ『翻訳不可能なものの受難』", "Bhattacharya Untranslatable", "Bhattacharya: Untranslatable",
     "バッタチャリヤが南アジア文脈から翻訳不可能性概念を再考した世界文学批判書。"),
    ("ウォルコウィッツ『生まれながら翻訳された』", "Walkowitz Born Translated", "Born Translated",
     "現代英語小説を「翻訳されることを前提に書かれた文学」として論じた2015年著作。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_original, definition in CONCEPTS:
        if len(definition) > 100:
            print(f"WARN definition too long ({len(definition)}): {name_ja}", file=sys.stderr)
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, subfield_id, region, period_id, definition, importance_score)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (name_ja, name_en, name_original, SUBFIELD_ID, REGION, PERIOD_ID, definition, 3),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}", file=sys.stderr)
    conn.commit()
    total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)).fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total in subfield {SUBFIELD_ID}: {total}")

if __name__ == "__main__":
    main()
