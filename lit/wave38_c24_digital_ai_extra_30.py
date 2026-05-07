#!/usr/bin/env python3
"""Wave 38: Add 30 deep-niche concepts to lit_digital_ai (subfield_id=24).
5 clusters x 6 concepts. Definition <= 100 chars, no background fields."""
import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SUBFIELD_ID = 24
REGION = "横断"
PERIOD_ID = 181  # デジタル・量的文学研究期（横断）

CONCEPTS = [
    # Cluster 1: AI判決・著作権
    ("Thaler対米著作権局訴訟", "Thaler v. Copyright Office", "Thaler v. U.S. Copyright Office",
     "AI生成画像「A Recent Entrance to Paradise」の著作権登録を否定した2023年判決。人間作者要件を確認。"),
    ("Naruto対Slater猿の自撮り訴訟", "Naruto v. Slater monkey selfie", "Naruto v. Slater",
     "猿が撮った自撮り写真の著作権を巡る2018年判決。非人間作者性の先例としてAI判例で参照される。"),
    ("Zarya of the Dawn AI漫画著作権事件", "Zarya of the Dawn AI comic copyright", "Zarya of the Dawn",
     "Midjourney生成画像漫画の登録を一部取消した2023年米著作権局決定。配置選択のみ著作権認定。"),
    ("Stable Diffusion集団訴訟", "Stable Diffusion class action", "Andersen v. Stability AI",
     "アーティスト3名が画像生成AIの訓練データに無断使用された絵画を巡って提起した2023年集団訴訟。"),
    ("サラ・アンダーセン作家訴訟", "Sarah Andersen artists' suit", "Sarah Andersen et al. v. Stability AI",
     "コミック作家サラ・アンダーセンが原告となったStable Diffusion訓練データ訴訟の主導的作家事件。"),
    ("Andersen対OpenAI訴訟", "Andersen v. OpenAI", "Andersen v. OpenAI",
     "作家アンダーセンらが提起したOpenAI訓練データ著作権侵害訴訟。LLM文学利用の核心的判例候補。"),

    # Cluster 2: AI翻訳と文学
    ("DeepL文学翻訳", "DeepL literary translation", "DeepL literary translation",
     "DeepLによる文学翻訳の品質と限界。詩や比喩表現での失敗パターンと文体保持の課題が議論される。"),
    ("Google翻訳詩学批判", "Google Translate poetry critique", "Google Translate poetry critique",
     "Google翻訳の詩翻訳における文字義性偏向と韻律喪失への批評。文学翻訳のNMT限界を示す。"),
    ("Tilde文学翻訳MTシステム", "Tilde literary translation MT", "Tilde literary MT",
     "ラトビアTilde社の文学翻訳特化型機械翻訳。少数言語と文学テクストへの適応研究を担う。"),
    ("Lluís Padróカタルーニャ語文学MT", "Lluís Padró Catalan literary MT", "Lluís Padró Catalan literary MT",
     "Padróらによるカタルーニャ語文学機械翻訳研究。少数言語文学のNMT適用の代表例。"),
    ("中英文学機械翻訳", "Chinese-English literary MT", "Chinese-English literary MT",
     "中国古典詩や現代小説の英語MT研究。文化固有語と詩的圧縮の処理が中心課題。"),
    ("日本語文学MTの課題", "Japanese literary MT challenges", "Japanese literary MT challenges",
     "敬語・主語省略・余白の機微が日本文学の機械翻訳を困難にする構造的問題群。"),

    # Cluster 3: テキスト分析手法
    ("Underwood単語ベクトル文学分析", "Ted Underwood word vectors literary", "Ted Underwood word vectors",
     "テッド・アンダーウッドが文学史分析に応用した単語埋め込み手法。ジャンル分類と文体変遷を測定。"),
    ("Piper枚挙分析", "Andrew Piper enumerations", "Andrew Piper Enumerations",
     "アンドリュー・パイパー著『Enumerations』。枚挙・反復の計量分析で小説の構造を解読する手法。"),
    ("Jockersマクロ分析", "Matthew Jockers Macroanalysis", "Matthew Jockers Macroanalysis",
     "マシュー・ジョッカーズ著『Macroanalysis』。19世紀英米小説4,000冊の主題・文体の量的解析。"),
    ("Morettiグラフ・地図・ツリー", "Franco Moretti Graphs Maps Trees", "Franco Moretti Graphs, Maps, Trees",
     "フランコ・モレッティの遠読方法論。グラフ・地図・進化樹で文学史を可視化する。"),
    ("Stanford Lit Lab Hofmannswaldau研究", "Stanford Lit Lab Hofmannswaldau", "Hofmannswaldau pamphlet",
     "スタンフォード・リテラリーラボのHofmannswaldau計量研究。バロック詩のスタイル分類実験。"),
    ("Reading Tea Leavesトピックモデル評価", "Reading Tea Leaves topic models", "Chang Reading Tea Leaves",
     "Changらの2009論文。トピックモデルの人間評価と一貫性測定の文学研究応用への影響。"),

    # Cluster 4: AI詩歌作家論
    ("Goodwin『1 the Road』", "Ross Goodwin 1 the Road", "1 the Road",
     "ロス・グッドウィンが車に搭載したRNNで生成した2018年AI小説。Kerouac的旅行記の機械版。"),
    ("Allado-McDowell『Pharmako-AI』", "K Allado-McDowell Pharmako-AI", "Pharmako-AI",
     "K・アラド＝マクダウェルがGPT-3と共著した2020年エッセイ集。共著者性とエコロジー思想を探る。"),
    ("Bertram『Travesty Generator』", "Lillian-Yvonne Bertram Travesty", "Travesty Generator",
     "リリアン＝イヴォン・バートラムによるアルゴリズム的詩集。コードと黒人詩学を統合。"),
    ("Jenny Lin AI詩", "Jenny Lin AI poetry", "Jenny Lin AI poetry",
     "ジェニー・リンによるAI生成詩実践。アジア系アメリカ詩学とLLM協働の交差点を探る。"),
    ("Derek BeaulieuのAI詩学", "Derek Beaulieu AI poetics", "Derek Beaulieu AI poetics",
     "デレク・ボーリューの概念詩学とAI詩生成実践。コンクリート詩の系譜にLLMを接続。"),
    ("Jhave Johnston『ReRites』", "Jhave Johnston ReRites", "ReRites",
     "デヴィッド・ジェイヴ・ジョンストンの2017-19年プロジェクト。RNN生成詩を毎月編集する大規模実践。"),

    # Cluster 5: ジェネラティブ作品
    ("Parrish『Articulations』", "Allison Parrish Articulations", "Articulations",
     "アリソン・パリッシュ2018年詩集。Project Gutenbergから音韻類似行を辿る生成詩学の名作。"),
    ("Parrish『Compasses』", "Allison Parrish Compasses", "Compasses",
     "パリッシュによる方位詩集。意味空間の幾何学的探索でテクスト座標を可視化する詩的実験。"),
    ("Montfort『Random Letters』", "Nick Montfort Random Letters", "Random Letters",
     "ニック・モントフォートの生成書簡集。乱数・制約から手紙形式の文学性を抽出する小品。"),
    ("Vladimir Tarakanov生成詩", "Vladimir Tarakanov generative poetry", "Vladimir Tarakanov",
     "ロシア出身の生成詩人タラカノフの実験。ニューラル詩生成の東欧的系譜を担う。"),
    ("Carrión『Membrana』", "Jorge Carrión Membrana", "Membrana",
     "ホルヘ・カリオン2021年小説。AI話者「美術館の声」が語る未来史小説で人間中心主義を解体。"),
    ("Stiles『Technelegy』", "Sasha Stiles Technelegy", "Technelegy",
     "サーシャ・スタイルズ2021年詩集。GPT-2と共作した「テクネレジー」(技術哀歌)というジャンル提唱。"),
]

assert len(CONCEPTS) == 30, f"Expected 30, got {len(CONCEPTS)}"

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, 0
    for name_ja, name_en, name_orig, definition in CONCEPTS:
        assert len(definition) <= 100, f"def too long: {name_ja} ({len(definition)})"
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, SUBFIELD_ID, REGION, PERIOD_ID, definition, 3))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP: {name_ja} -- {e}")
            skipped += 1
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
