#!/usr/bin/env python3
"""Wave 44: add 30 ultra-niche lit_world_translation concepts."""

from lit_db_helper import LitDB


SUBFIELD_CODE = "lit_world_translation"
REGION = "横断"
PERIOD_ID = None

CONCEPTS = [
    # 1. Manuscript and sacred-text translation routes
    ("コーカサス・アルバニア聖書断片のアルメニア語読解訳", "Caucasian Albanian Bible fragments via Armenian", "断片聖書をアルメニア語注解で読む翻訳媒介。"),
    ("サマリア五書アラビア語傍訳", "Samaritan Pentateuch Arabic side translation", "サマリア共同体内でヘブライ語本文に添えたアラビア語訳。"),
    ("中世ヌビア語奇跡譚のギリシア語重訳", "Medieval Nubian miracle tales via Greek", "ヌビア語聖者譚をギリシア語層から復元する重訳事例。"),
    ("クマン語典礼歌のラテン語注解訳", "Cuman liturgical song Latin gloss translation", "クマン語典礼歌をラテン語注で読ませる宣教翻訳形式。"),
    ("マラーティー・ポルトガル宣教対訳問答", "Marathi-Portuguese catechism dialogue", "宣教問答を二言語対話として組む初期近世の対訳形式。"),
    ("シンハラ仏伝のパーリ語逆注釈", "Sinhala Buddha-life Pali back-commentary", "シンハラ仏伝をパーリ権威へ戻す逆注釈的翻訳。"),
    # 2. Minority-language mediation and bridge editions
    ("アルザス語小説の仏独二重窓口", "Alsatian fiction French-German double gateway", "アルザス語小説が仏独二言語を窓口に流通する経路。"),
    ("ルシン語詩のウクライナ語橋渡し", "Rusyn poetry via Ukrainian bridge translation", "ルシン語詩をウクライナ語版経由で広域化する翻訳。"),
    ("カボベルデ・クレオール詩の葡語自己対訳", "Cape Verdean Creole Portuguese self-bilingual poem", "クレオール詩人が葡語対訳で世界流通を設計する形式。"),
    ("ブリヤート語叙事詩の露語学術抄訳", "Buryat epic Russian scholarly abridgment", "叙事詩を研究用ロシア語抄訳で固定する編集翻訳。"),
    ("ナワホ聖歌の英語民族誌訳", "Navajo chant ethnographic English translation", "儀礼聖歌を民族誌解説つき英訳へ変える翻訳実践。"),
    ("ツォツィル語証言文学の西語編集訳", "Tzotzil testimonial literature Spanish edited translation", "証言を西語編集訳で政治的読者へ届ける形式。"),
    # 3. Censorship, exile, and clandestine circulation
    ("サラザール期反体制小説の仏語抜粋訳", "Salazar-era dissident fiction French excerpt translation", "検閲を避け仏語抜粋で国外読者に届く反体制小説。"),
    ("ルーマニア共産期地下翻訳回覧", "Romanian communist-era underground translation circulation", "地下読書会で手稿翻訳を回覧した社会主義期の流通。"),
    ("ギリシア内戦亡命詩のチェコ語リレー", "Greek Civil War exile poetry Czech relay translation", "亡命詩が社会主義圏のチェコ語版で再媒介される経路。"),
    ("シリア検閲下小説のレバノン版翻案", "Syrian censored novel Lebanese adaptation", "検閲回避のためレバノン版で改題・改稿される翻訳。"),
    ("タイ不敬罪小説の英語匿名訳", "Thai lese-majeste fiction anonymous English translation", "匿名英訳で刑事リスクを分散する政治小説の翻訳。"),
    ("エチオピア赤色テロ証言の英語支援訳", "Ethiopian Red Terror testimony support translation", "証言を支援団体の英訳で国際人権言説へ接続する。"),
    # 4. Paratext, layout, and poetic-form translation
    ("縦中横数字の訳注処理", "tate-chu-yoko numeral annotation handling", "縦組み内数字表記を横組み訳注で説明する処理。"),
    ("声調脚韻の補償翻訳", "tonal rhyme compensatory translation", "声調と脚韻の同時損失を別位置で補う韻文翻訳。"),
    ("見開き対訳の改頁同期", "facing-page translation pagination sync", "原文と訳文の改頁を同期し引用単位を保つ組版技法。"),
    ("口絵キャプションの文化注釈訳", "frontispiece caption cultural gloss translation", "口絵説明を文化注つきで訳し読解枠を補正する処理。"),
    ("訳者索引の異名統制", "translator index alias control", "訳者名の異表記を索引で統制し受容史を追跡する方法。"),
    ("折句詩の頭字再構成訳", "acrostic initial-letter reconstruction translation", "折句の頭字構造を訳詩で再構成する制約翻訳。"),
    # 5. LLM and literary MT evaluation micro-methods
    ("LLM訳の訓練データ逆流検出", "LLM translation training-data backflow detection", "既存訳の記憶混入を訳文類似度から検出する方法。"),
    ("参照訳なし文学MTブラインド評価", "reference-free literary MT blind evaluation", "参照訳を見せず文学MTの文体と意味を評価する設計。"),
    ("低資源韻文の音韻埋め込み評価", "low-resource verse phonological embedding evaluation", "低資源詩訳の音響近似を埋め込みで測る評価法。"),
    ("プロンプト別訳調クラスタリング", "prompt-conditioned translation-tone clustering", "プロンプト差で生じる訳調をクラスタ化する比較法。"),
    ("LLM訳後編集の介入ログ分析", "LLM post-editing intervention log analysis", "後編集ログから人間の文体介入箇所を抽出する方法。"),
    ("多段LLMリレー翻訳劣化曲線", "multi-hop LLM relay translation degradation curve", "LLM重訳を段数ごとに比べ意味劣化を測る指標。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"{name_ja}: definition too long")
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None and cid:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
