#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_theory (subfield 22)."""

from lit_db_helper import LitDB

SUBFIELD = "lit_theory"
REGION = "横断"

# 5 thematic clusters x 6 concepts. period_id is NULL for cross-regional theory.
CONCEPTS = [
    # Cluster 1: regional minor theories
    ("アンダルス・ムワッシャハ理論", "Andalusian muwashshah poetics", "muwashshah", "latin",
     "アンダルス連詩の折返し・俗語句をめぐる詩学。"),
    ("グルジア賛歌イアムビコ論", "Georgian iambiko hymn poetics", "iambiko", "latin",
     "中世グルジア賛歌の音節型と典礼配置を読む詩学。"),
    ("アラカン宮廷ラザワン読解", "Arakanese razawan court reading", "razawan", "latin",
     "アラカン年代記を宮廷叙述の権威形式として読む方法。"),
    ("マラヤーラム・マニプラヴァーラム論", "Malayalam manipravalam poetics", "manipravalam", "latin",
     "サンスクリット・地域語混淆文体の詩学的規範。"),
    ("オック語トロバリッツ語り論", "trobairitz voice theory", "trobairitz", "latin",
     "女性トルバドゥール歌の声と帰属をめぐる微視的議論。"),
    ("コプト殉教物語レトリック", "Coptic martyr narrative rhetoric", "martyrium", "latin",
     "コプト殉教譚の証言配置と反帝国語りを分析する。"),

    # Cluster 2: manuscript and scribal micro-traditions
    ("パリンプセスト記憶詩学", "palimpsest memory poetics", "palimpsest", "latin",
     "消された下層本文を記憶と読解の痕跡として扱う。"),
    ("奥書コロフォン主体論", "colophon subjectivity", "colophon", "latin",
     "写字生奥書に現れる自己署名と読者宛てを分析する。"),
    ("欄外グロッサ共同読解論", "marginal gloss communal reading", "glossa", "latin",
     "欄外注を共同的読書の痕跡として読む写本研究。"),
    ("鎖状注解カテナ詩学", "catena commentary poetics", "catena", "latin",
     "引用連鎖型注解を断片編集の詩学として捉える。"),
    ("折丁ミスバインディング解釈", "quire misbinding hermeneutics", "quire", "latin",
     "錯簡や折丁誤綴を物語順序の生成要因として読む。"),
    ("赤字ルブリック読解論", "rubrication reading theory", "rubric", "latin",
     "朱書見出しが読者のジャンル認識を誘導する仕組み。"),

    # Cluster 3: forgotten works and less-translated authors
    ("アンドレアス・カペラヌス反宮廷恋愛論", "Andreas Capellanus anti-courtly love", "De amore", "latin",
     "宮廷恋愛規範を反語と教訓の揺れから読む論点。"),
    ("イブン・シュハイド精霊旅批評", "Ibn Shuhayd jinn journey criticism", "Risalat al-tawabi", "latin",
     "精霊随伴者の旅を文人権威の風刺装置として読む。"),
    ("ソル・フアナ沈黙弁証法", "Sor Juana silence dialectic", "Respuesta", "latin",
     "沈黙命令を知的自己弁護へ反転する修辞を読む。"),
    ("イェフダ・アルハリジ韻文散文論", "Yehuda al-Harizi maqama poetics", "Tahkemoni", "latin",
     "ヘブライ語マカーマの翻案と競作意識を扱う。"),
    ("アンナ・コムネナ自己史述論", "Anna Komnene self-historiography", "Alexiad", "latin",
     "皇女史家の自己正当化と古典引用を読む。"),
    ("バンデルロ物語枠批評", "Bandello novella frame criticism", "Novelle", "latin",
     "献辞・枠・事件報告が短篇権威を作る仕組み。"),

    # Cluster 4: sub-genre variants
    ("偽夢告白プロシメトルム論", "pseudo-dream prosimetrum", "prosimetrum", "latin",
     "夢告白と韻文挿入が混じる小ジャンルの形式論。"),
    ("都市奇聞アジャーイブ詩学", "urban ajaib poetics", "ajaib", "latin",
     "都市の驚異譚を地誌と逸話の交差形式として読む。"),
    ("聖者伝ミラクル目録論", "miracle catalogue hagiography", "miracula", "latin",
     "奇跡列挙が聖性と地域記憶を編む形式を分析。"),
    ("航海ロテイロ叙述論", "roteiro voyage narrative", "roteiro", "latin",
     "航路記録が文学的冒険譚へ変わる境界を読む。"),
    ("市井笑話ファセティエ分類論", "facetiae taxonomy", "facetiae", "latin",
     "ルネサンス笑話集の小話型と社会風刺を分類する。"),
    ("占夢書オネイロクリティカ読解", "oneirocritica reading", "oneirocritica", "latin",
     "夢占い書の記号表と物語的連想を分析する。"),

    # Cluster 5: theoretical micro-debates
    ("校訂本レクティオ・ディフィキリオル論争", "lectio difficilior debate", "lectio difficilior", "latin",
     "難読を原形とみなす校訂原則の限界を問う論争。"),
    ("寓意四義センス過剰論", "fourfold allegory overreading", "quadriga", "latin",
     "四義解釈が意味を過剰生産する危険をめぐる議論。"),
    ("偽書ピグラフィア作者性論", "pseudepigraphic authorship", "pseudepigrapha", "latin",
     "偽名著作の権威と作者性を分離して考える論点。"),
    ("翻案忠実性インフィデリティ論", "creative infidelity adaptation", "infidelity", "latin",
     "不忠実な翻案を創造的読解として評価する議論。"),
    ("韻律破格ライセンス論争", "metrical license debate", "licentia poetica", "latin",
     "韻律違反を誤りか詩的許可かで争う微細論点。"),
    ("口承筆録テクスト固定性論", "oral dictation textual fixation", "dictation", "latin",
     "口承を筆録した本文の固定性と変異を問う議論。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 22"
            )
        }
        inserted = 0
        skipped = 0
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            if name_ja in existing:
                skipped += 1
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=None,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
        print(f"inserted={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
