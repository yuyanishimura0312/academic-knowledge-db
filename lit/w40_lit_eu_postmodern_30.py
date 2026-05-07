#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_eu_postmodern."""

from lit_db_helper import LitDB


SUBFIELD = "lit_eu_postmodern"
REGION = "西欧"


CONCEPTS = [
    # Cluster 1: minor-language postmodernisms
    {
        "name_ja": "フリジア語ポストモダン小説",
        "name_en": "Frisian postmodern novel",
        "name_original": "Fryske postmoderne roman",
        "definition": "フリジア語で自己言及や断片構成を試す少数語小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "ブレイス語実験散文",
        "name_en": "Breton experimental prose",
        "name_original": "komz-plaen arnod Brezhoneg",
        "definition": "ブルターニュ語復興と断片的語りが交差する実験散文",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "オック語ネオ前衛小説",
        "name_en": "Occitan neo-avant-garde fiction",
        "name_original": "roman neoavantgardista occitan",
        "definition": "オック語運動内で方言性と前衛形式を結ぶ小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "カタルーニャ語メタ探偵小説",
        "name_en": "Catalan meta-detective fiction",
        "name_original": "novella metadetectivesca catalana",
        "definition": "探偵形式で記憶政治と読解行為を反転するカタルーニャ小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "ガリシア語幽霊アーカイヴ",
        "name_en": "Galician ghost archive",
        "name_original": "arquivo fantasma galego",
        "definition": "ガリシア語散文で亡霊・文書・地域記憶を接合する形式",
        "period": "自伝的現代期",
    },
    {
        "name_ja": "サルデーニャ語偽民俗小説",
        "name_en": "Sardinian pseudo-folkloric novel",
        "name_original": "romanzu pseudofolcloricu sardu",
        "definition": "民俗資料を偽装し島嶼アイデンティティを揺らす小説",
        "period": "ポストモダン期",
    },
    # Cluster 2: forgotten or less-translated works/authors
    {
        "name_ja": "ロジェ・ラポルト『ビオグラフィー』",
        "name_en": "Roger Laporte Biography",
        "name_original": "Biographie",
        "definition": "自己記述の不可能性を断章化するフランスの忘れられた連作",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "ジャン・リカルドゥー『コンスタンチノープルの占領』",
        "name_en": "Jean Ricardou The Capture of Constantinople",
        "name_original": "La Prise de Constantinople",
        "definition": "物語生成規則そのものを主題化するヌーヴォー・ロマン系実験作",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "クリスティーヌ・ブルック＝ローズ『テクスト終了』",
        "name_en": "Christine Brooke-Rose Textermination",
        "name_original": "Textermination",
        "definition": "文学人物の会議を通じ正典存続を戯画化するメタ小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "アルノ・シュミット『ズェッテルの夢』",
        "name_en": "Arno Schmidt Bottom's Dream",
        "name_original": "Zettels Traum",
        "definition": "欄外・語源遊戯・引用を巨大ページに並走させる難解小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "ジョルジュ・ペレック『さまざまな空間』",
        "name_en": "Georges Perec Species of Spaces",
        "name_original": "Especes d'espaces",
        "definition": "部屋から宇宙までを分類し空間記述を文学実験化する散文",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "マリア・ガブリエラ・リャンソル断章小説",
        "name_en": "Maria Gabriela Llansol fragmentary fiction",
        "name_original": "ficcao fragmentaria de Llansol",
        "definition": "ポルトガル語圏で人物・神秘・日記を溶かす断章小説",
        "period": "自伝的現代期",
    },
    # Cluster 3: manuscript and archive microforms
    {
        "name_ja": "タイプ稿ヴァリアント小説",
        "name_en": "typescript variant novel",
        "name_original": "typescript variant novel",
        "definition": "タイプ稿差異や校正痕を物語構造へ組み込む小説形式",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "欄外注釈フィクション",
        "name_en": "marginalia fiction",
        "name_original": "fiction marginale",
        "definition": "本文より欄外書き込みが物語を駆動する注釈型小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "未刊草稿アーカイヴ小説",
        "name_en": "unpublished manuscript archive fiction",
        "name_original": "roman d'archives manuscrites",
        "definition": "未刊草稿の発見・編集・欠落を筋立てにするアーカイヴ小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "校訂者序文の虚構化",
        "name_en": "fictionalized editor's preface",
        "name_original": "preface editoriale fictive",
        "definition": "校訂者序文を虚構化し本文の信頼性を崩す装置",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "索引物語",
        "name_en": "index narrative",
        "name_original": "recit-index",
        "definition": "索引項目の配列だけで人物関係や事件を浮かべる形式",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "削除線叙述",
        "name_en": "strikethrough narration",
        "name_original": "narration biffee",
        "definition": "抹消された語句を読ませ訂正過程を物語化する技法",
        "period": "ポストモダン期",
    },
    # Cluster 4: sub-genre variants
    {
        "name_ja": "反ミステリ的地方犯罪小説",
        "name_en": "anti-detective regional crime fiction",
        "name_original": "regional anti-detective fiction",
        "definition": "地方犯罪小説の解決期待を崩し共同体記憶を前景化する形式",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "神学的サイバーパンク寓話",
        "name_en": "theological cyberpunk allegory",
        "name_original": "theological cyberpunk allegory",
        "definition": "ネットワーク表象に救済論や異端神学を重ねる欧州SF変種",
        "period": "ポスト・ポストモダン期",
    },
    {
        "name_ja": "ポスト産業牧歌",
        "name_en": "post-industrial pastoral",
        "name_original": "post-industrial pastoral",
        "definition": "廃工場や鉱山跡を牧歌形式で描き直す現代小説変種",
        "period": "ポスト・ポストモダン期",
    },
    {
        "name_ja": "博物館ゴシック",
        "name_en": "museum gothic",
        "name_original": "museum gothic",
        "definition": "展示室・収蔵庫・標本が怪奇と植民記憶を呼ぶ小説形式",
        "period": "自伝的現代期",
    },
    {
        "name_ja": "観光パンフレット小説",
        "name_en": "tourist-brochure novel",
        "name_original": "roman de brochure touristique",
        "definition": "観光案内の文体を模倣し地域表象の商品化を暴く小説",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "EU官僚制風刺小説",
        "name_en": "EU bureaucracy satire",
        "name_original": "EU bureaucracy satire",
        "definition": "EU機関の通訳・文書・規則を滑稽化する現代欧州小説",
        "period": "ポスト・ポストモダン期",
    },
    # Cluster 5: theoretical micro-debates
    {
        "name_ja": "小言語ポストモダン性論争",
        "name_en": "minor-language postmodernity debate",
        "name_original": "minor-language postmodernity debate",
        "definition": "少数語文学にポストモダン概念を適用できるかを問う論争",
        "period": "自伝的現代期",
    },
    {
        "name_ja": "制約文学と機械生成の境界",
        "name_en": "constraint writing versus machine generation",
        "name_original": "constraint writing versus machine generation",
        "definition": "ウリポ的制約とAI生成を連続か断絶かで見る微小論点",
        "period": "ポスト・ポストモダン期",
    },
    {
        "name_ja": "偽注釈の倫理",
        "name_en": "ethics of false annotation",
        "name_original": "ethics of false annotation",
        "definition": "虚偽の脚注や資料提示が読者信頼をどう扱うかの議論",
        "period": "ポストモダン期",
    },
    {
        "name_ja": "アーカイヴ疲労",
        "name_en": "archival fatigue",
        "name_original": "archival fatigue",
        "definition": "記憶資料の過剰提示が証言より疲弊を生むという批評概念",
        "period": "自伝的現代期",
    },
    {
        "name_ja": "翻訳不能性の商品化",
        "name_en": "commodification of untranslatability",
        "name_original": "commodification of untranslatability",
        "definition": "翻訳困難さ自体が市場価値や異国性として売られる現象",
        "period": "ポスト・ポストモダン期",
    },
    {
        "name_ja": "地方性のメタフィクション化",
        "name_en": "metafictionalization of locality",
        "name_original": "metafictionalization of locality",
        "definition": "地域性を透明な背景でなく語りの作為として示す方法",
        "period": "自伝的現代期",
    },
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB() as db:
        periods = {
            "ポストモダン期": db.get_or_create_period("ポストモダン期", REGION, 1960, 2000),
            "自伝的現代期": db.get_or_create_period("自伝的現代期", REGION, 1990, 2025),
            "ポスト・ポストモダン期": db.get_or_create_period("ポスト・ポストモダン期", REGION, 2000, 2025),
        }
        for entry in CONCEPTS:
            if len(entry["definition"]) > 100:
                raise ValueError(f"definition too long: {entry['name_ja']}")
            period_id = periods[entry.pop("period")]
            existed = db.find_concept(entry["name_ja"], REGION, period_id) is not None
            db.insert_concept(
                **entry,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if existed:
                skipped += 1
            else:
                inserted += 1
    print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
