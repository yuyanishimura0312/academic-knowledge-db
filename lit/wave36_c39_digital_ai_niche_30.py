#!/usr/bin/env python3
"""Wave 36 C39: lit_digital_ai niche 30 concepts (5 clusters x 6)."""
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 24
PERIOD_ID = 290  # 現代
TIER = "secondary"

CONCEPTS = [
    # Cluster 1: AI著作権訴訟2024-2025
    ("Concord Music対Anthropic歌詞訴訟", "Concord Music v Anthropic lyrics", "西欧",
     "2023年提訴の音楽出版社連合による歌詞無断学習訴訟。2025年和解で訓練倫理に影響。"),
    ("Suno/Udio RIAA訴訟2024", "RIAA v Suno Udio 2024", "西欧",
     "2024年大手レコード3社が音楽生成AI Suno/Udioを著作権侵害で提訴した画期的訴訟。"),
    ("Authors Equityポリシー", "Authors Equity AI policy", "西欧",
     "2024年Madeline McIntosh設立の出版社、AI訓練利用に作家同意必須を明文化。"),
    ("Adobe Firefly訓練データ論争", "Adobe Firefly training data", "西欧",
     "「倫理的AI」と謳ったFireflyが実はMidjourney画像も学習していた2024年発覚事件。"),
    ("Disney対Midjourney訴訟", "Disney v Midjourney 2025", "西欧",
     "2025年Disney/Universalが提訴したキャラクター無断生成に対する大手スタジオ初訴訟。"),
    ("OpenAI Connections訴訟", "OpenAI Connections lawsuit", "西欧",
     "NYT Connectionsパズル等の著作権侵害でOpenAI/Microsoftが追訴された2024-25年訴訟群。"),
    # Cluster 2: AI日本文学
    ("AI俳句一茶くん", "AI haiku Issa-kun", "東アジア",
     "北海道大学川村秀憲研究室開発の俳句生成AI。LSTMベース、季語と五七五を自動生成。"),
    ("ELYZA日本語LLM", "ELYZA Japanese LLM", "東アジア",
     "東大松尾研発ELYZA社の日本語特化LLM。Llama2/3ベースで日本文学生成・要約に特化。"),
    ("青空文庫AI訓練利用問題", "Aozora Bunko AI training", "東アジア",
     "PD日本古典16,000作品の青空文庫がLLM訓練に大量利用される倫理問題が2024年顕在化。"),
    ("NHK朝ドラAI制作論争", "NHK morning drama AI", "東アジア",
     "2024年NHKがAI脚本支援を朝ドラ制作で試行、脚本家協会が懸念表明した事例。"),
    ("AI源氏物語英訳", "AI Genji Monogatari translation", "東アジア",
     "GPT-4/Claude等による源氏物語英訳実験。Tyler/Seidensticker訳との文体比較研究進展。"),
    ("Sakana AI日本語進化的LLM", "Sakana AI evolutionary LLM", "東アジア",
     "David Ha/Llion Jones設立Sakana AIの進化的モデル統合手法。日本語LLM EvoLLM-JP公開。"),
    # Cluster 3: AI×非西欧
    ("AI4Bharat IndicLLM群", "AI4Bharat IndicLLM suite", "南アジア",
     "IIT Madras主導の22インド公用語対応LLM群。IndicTrans2/IndicBERTで南アジア文学AI基盤。"),
    ("Aya Cohere多言語LLM", "Aya Cohere multilingual", "横断",
     "Cohere For AIの101言語対応モデルAya。低資源言語の文学生成・翻訳を民主化する試み。"),
    ("Jais Falcon Arabic LLM", "Jais Falcon Arabic LLM", "西アジア",
     "G42/MBZUAI開発Jaisと TII開発FalconのアラビアLLM。アラブ文学AI生成の主要基盤。"),
    ("HyperCLOVA韓国語LLM", "HyperCLOVA Korean LLM", "東アジア",
     "Naver開発の韓国語特化大規模LLM。HyperCLOVA Xで文学創作・翻訳支援機能を展開。"),
    ("Wenxin/Qwen中国語LLM", "Wenxin Qwen Chinese LLM", "東アジア",
     "百度文心一言・阿里Qwenによる中国語特化LLM。中国古典文学生成・現代文学創作の基盤。"),
    ("Baichuan中国語LLM", "Baichuan Chinese LLM", "東アジア",
     "王小川設立百川智能の中国語LLM。中国文学・詩詞生成と長文小説執筆支援に展開。"),
    # Cluster 4: 倫理深掘り
    ("Buolamwini Gender Shades監査", "Buolamwini Gender Shades", "横断",
     "2018年Joy Buolamwini顔認識バイアス監査研究。AI文学批評の身体表象分析の起点。"),
    ("Gebru確率的オウム論", "Gebru Stochastic Parrots", "横断",
     "2021年Bender/Gebru/McMillan-Major/Mitchell論文。LLMを統計的反復装置と批判する基盤論。"),
    ("Benjamin Race After Tech", "Benjamin Race After Technology", "横канд",
     "2019年Ruha Benjamin著。新ジムクロウ的テクノロジーの差別構造を分析する文学批評の基盤。"),
    ("Noble Algorithms Oppression", "Noble Algorithms of Oppression", "横断",
     "2018年Safiya Umoja Noble著。検索アルゴリズムの黒人女性蔑視を暴く文化批評古典。"),
    ("Eubanks Automating Inequality", "Eubanks Automating Inequality", "横断",
     "2018年Virginia Eubanks著。自動化システムが貧困層を罰する構造を分析する社会記述。"),
    ("Crawford Atlas of AI", "Crawford Atlas of AI", "横断",
     "2021年Kate Crawford著。AIの物質的・労働的・環境的基盤を批判する政治地理学的文学論。"),
    # Cluster 5: 新形式
    ("Twineナラティブ実践詳細", "Twine narrative practice", "西欧",
     "Chris Klimas開発のオープンソース対話型物語ツール。Porpentine等インディー作家の主要基盤。"),
    ("Inkle Heaven's Vault", "Inkle Heaven's Vault", "西欧",
     "Inkle Studios2019年作品。古代言語解読を核としたゲーム文学、考古学的読解の新形式。"),
    ("Florenceゲーム文学", "Florence game-as-literature", "西欧",
     "Mountains開発2018年作品。台詞なしジェスチャー操作で恋愛を語るゲーム形式の短編文学。"),
    ("Disco Elysium文学性", "Disco Elysium literary", "東欧",
     "ZA/UM 2019年作品。100万語超のテクスト量と内的独白を備えるRPG形式の哲学小説。"),
    ("Citizen Sleeper", "Citizen Sleeper", "西欧",
     "Jump Over the Age 2022年作品。サイコロとTRPGメカニクスで労働・連帯を描くSF文学。"),
    ("Hidden Door個別化物語", "Hidden Door personalized", "西欧",
     "Hilary Mason創業Hidden Doorの2024年LLMベース個別化物語生成プラットフォーム。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, region, definition in CONCEPTS:
        if len(definition) > 100:
            print(f"SKIP (def too long {len(definition)}): {name_ja}", file=sys.stderr)
            skipped += 1
            continue
        try:
            cur.execute(
                """INSERT INTO concepts
                (name_ja, name_en, subfield_id, region, period_id, definition, source_tier, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (name_ja, name_en, SUBFIELD_ID, region, PERIOD_ID, definition, TIER, 3),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"SKIP (dup): {name_ja} -- {e}", file=sys.stderr)
            skipped += 1
    conn.commit()
    conn.close()
    print(f"INSERTED={inserted} SKIPPED={skipped}")


if __name__ == "__main__":
    main()
