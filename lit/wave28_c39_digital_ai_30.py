#!/usr/bin/env python3
"""Wave28 C39: Add 30 concepts to lit_digital_ai (subfield_id=24).
5 thematic clusters x 6 concepts. Period 290 (現代). source_tier='secondary'."""

import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD = 24
PERIOD = 290
TIER = "secondary"

CONCEPTS = [
    # Cluster 1: AI訴訟2024-2025
    ("Concord Music対Anthropic訴訟", "Concord Music v Anthropic", "music publishers", "西欧",
     "2023年提訴の音楽出版社による歌詞無断学習訴訟。2025年3月部分和解、AI訓練データ著作権の試金石。"),
    ("Suno/Udio対RIAA訴訟2024", "Suno Udio RIAA Lawsuit 2024", "RIAA v Suno Udio", "西欧",
     "2024年6月RIAAが音楽生成AIを音源無断学習で提訴。AI音楽生成の合法性を問う代表訴訟。"),
    ("Authors Equity AIポリシー", "Authors Equity AI Policy", "Authors Equity", "西欧",
     "新興出版社Authors Equityが2024年策定したAI利用方針、人間作家保護と透明性開示を義務化。"),
    ("NYT Connections対Fox誹謗訴訟", "NYT Connections Fox Defamation", "Connections lawsuit", "西欧",
     "2024年AI生成コンテンツによる名誉毀損疑義訴訟、生成AIの誹謗責任所在を巡る判例形成。"),
    ("伊Garante GDPR ChatGPTブロック", "Italian Garante GDPR ChatGPT Ban", "Garante Privacy", "西欧",
     "2023年伊データ保護当局がChatGPTを一時遮断、GDPR準拠を要求した世界初のLLM規制執行事例。"),
    ("EU AI法文学詳細条項", "EU AI Act Literary Provisions", "EU AI Act", "西欧",
     "2024年成立EU AI法の文学・創作関連条項。透明性義務・訓練データ開示・著作権遵守を明文化。"),

    # Cluster 2: Generation tools
    ("Sudowrite Story Engine", "Sudowrite Story Engine", "Sudowrite", "横断",
     "2024年公開の長編小説生成支援機能。プロット・キャラ・章立てを構造化、AI共著実践の代表ツール。"),
    ("NovelAI Aetherroom", "NovelAI Aetherroom", "Aetherroom", "横断",
     "NovelAIのストーリー協創環境。世界観・キャラ管理機能でAI駆動長編小説を実現する執筆基盤。"),
    ("Hidden Door個別物語生成", "Hidden Door Personalized Narratives", "Hidden Door", "西欧",
     "既存IP（既刊小説等）からAI生成個別物語を提供。読者参加型ナラティブの新形式を提示。"),
    ("Replika文学的親密性", "Replika Literary Intimacy", "Replika", "西欧",
     "AIコンパニオンアプリRepilikaにおける文学的会話・小説的親密性、人間-AI関係の物語化。"),
    ("Inworld AIキャラクター", "Inworld AI Characters", "Inworld", "西欧",
     "ゲーム・物語向けAIキャラクター生成基盤。性格・記憶・声を統合した動的ナラティブ駆動エンジン。"),
    ("Character.AIファンフィク", "Character.AI Fanfiction", "Character.AI", "横断",
     "Character.AIで爆発したキャラ会話型ファンフィクション、二次創作の新モード形成。"),

    # Cluster 3: Multimodal
    ("Sora物語含意", "Sora Narrative Implications", "Sora OpenAI", "西欧",
     "2024年OpenAI Sora公開、テキストから映像物語生成。文学とシネマトグラフィの境界を再定義。"),
    ("Runway Gen-3物語", "Runway Gen-3 Alpha", "Runway Gen-3", "西欧",
     "2024年公開Runway Gen-3 Alpha、長尺一貫映像生成で文学-映像ブリッジを実現。"),
    ("ElevenLabs声クローン", "ElevenLabs Voice Cloning", "ElevenLabs", "西欧",
     "高精度音声クローン技術、亡き作家の朗読再現や多言語オーディオブック生成を可能にした。"),
    ("Apple Intelligenceナレーション", "Apple Intelligence Narration", "Apple Intelligence", "西欧",
     "2024年Apple Intelligence搭載、デバイス内ナレーション・要約機能で文学消費体験を変容。"),
    ("NotebookLM Audio Overview", "NotebookLM Audio Overview", "NotebookLM", "西欧",
     "2024年Google NotebookLMのテキスト→ポッドキャスト変換、文学批評の音声化を一般化。"),
    ("拡散モデル詩", "Diffusion Poetry", "Diffusion Poetry", "横断",
     "拡散モデルによるテキスト生成詩、視覚芸術技法の言語転用で新たな詩学を開拓。"),

    # Cluster 4: HCI×文学
    ("Twine SugarCube", "Twine SugarCube", "Twine SugarCube", "西欧",
     "Twineの主要ストーリーフォーマットSugarCube。複雑な分岐・状態管理で電子文学制作を支える。"),
    ("Inkle Heaven's Vault", "Inkle Heaven's Vault", "Heaven's Vault", "西欧",
     "Inkle製2019年作。古代言語解読を中核に据えた言語考古学ナラティブゲーム、文学性高評価。"),
    ("Florenceゲーム文学", "Florence Game as Literature", "Florence game", "西欧",
     "2018年Mountains制作、無音グラフィック・ノベルとしての恋愛物語ゲーム、文学的構造を持つ。"),
    ("Citizen Sleeper", "Citizen Sleeper", "Citizen Sleeper", "西欧",
     "2022年Jump Over the Age作TRPG型SF文学ゲーム、選択駆動の労働・身体性を巡る現代文学。"),
    ("Disco Elysium文学", "Disco Elysium as Literature", "Disco Elysium", "西欧",
     "2019年ZA/UM作、100万語超のテキスト量で文学的ロールプレイの頂点を示した代表作。"),
    ("80 Daysナラティブ", "80 Days Narrative", "80 Days inkle", "西欧",
     "2014年inkle作、ヴェルヌ翻案分岐物語。ポストコロニアル再読を内包した代表的IF文学。"),

    # Cluster 5: AI×非西欧
    ("AI4Bharat IndicLLM", "AI4Bharat IndicLLM", "AI4Bharat", "南アジア",
     "インド工科大学発の22インド言語対応LLMプロジェクト、南アジア多言語文学のAI基盤。"),
    ("Aya Cohere多言語", "Aya Cohere Multilingual", "Aya Cohere", "横断",
     "2024年Cohere for AI公開101言語対応LLM、低リソース言語文学のAI処理を可能化。"),
    ("Jais Falcon Arabic", "Jais Falcon Arabic LLM", "Jais Falcon", "西アジア",
     "UAE Inception開発のアラビア語特化LLM、アラブ文学・古典詩のAI処理基盤を構築。"),
    ("HyperCLOVA韓国語", "HyperCLOVA Korean LLM", "HyperCLOVA NAVER", "東アジア",
     "NAVER開発の韓国語特化LLM、韓国現代文学・K-コンテンツ生成の中核技術基盤。"),
    ("Wenxin Qwen中国語LLM", "Wenxin Qwen Chinese LLM", "Wenxin Qwen", "東アジア",
     "百度Wenxin・阿里Qwenの中国語特化LLM、中国古典文学・現代網絡文学の処理基盤。"),
    ("Sakana AI日本語進化", "Sakana AI Japanese Evolution", "Sakana AI", "東アジア",
     "Sakana AIによる日本語進化的モデル統合、日本文学固有のスタイル・俳句生成に特化した基盤。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, region, definition in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                (name_ja, name_en, name_original, subfield_id, region, period_id,
                 definition, importance_score, source_tier)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, SUBFIELD, region, PERIOD,
                  definition, 3, TIER))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD,))
    print(f"Total in subfield {SUBFIELD}: {cur.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    main()
