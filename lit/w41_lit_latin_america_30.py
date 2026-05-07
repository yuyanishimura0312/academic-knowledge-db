#!/usr/bin/env python3
"""Wave41: add 30 hyper-niche concepts to lit_latin_america."""

from lit_db_helper import LitDB

SUBFIELD = "lit_latin_america"
REGION = "ラテンアメリカ"

P_COLONIAL = 254
P_VANG = 284
P_POSTDICT = 260
P_INDIG = 231
P_WOMEN = 288

ROWS = [
    # Cluster 1: colonial Indigenous manuscript/legal microforms
    ("テステリアーノ絵文字教理問答", "Testerian pictographic catechism", "catecismo testeriano", P_COLONIAL, "絵文字で教理を記憶させる植民地メソアメリカ布教冊子。"),
    ("ナワトル遺言状定型句", "Nahuatl testament formula", "formula testamentaria nahuatl", P_COLONIAL, "ナワトル語遺言状に反復される相続・信仰の文書定型。"),
    ("ティトゥロ・プリモルディアル偽古文書", "titulo primordial pseudo-archive", "titulo primordial", P_COLONIAL, "共同体土地権を古文書風に主張する植民地先住民文書。"),
    ("カシケ系譜訴訟絵図", "cacique genealogical lawsuit map", "mapa genealogico de cacique", P_COLONIAL, "首長家系と土地権を一枚絵で訴える法廷用図像文書。"),
    ("チラム・バラム暦注断章", "Chilam Balam calendrical gloss", "glosa calendrica chilam balam", P_COLONIAL, "ユカタン・マヤ写本で暦注と預言が混じる短い注記形式。"),
    ("アンデス訪問記録の通訳声", "Andean visita interpreter voice", "voz de interprete en visita", P_COLONIAL, "植民地巡察記録に残る通訳媒介の間接発話層。"),

    # Cluster 2: regional minor oral-print traditions
    ("パヤーダ・デ・コントラプント", "payada de contrapunto", "payada de contrapunto", P_VANG, "二人の歌い手が即興で論争する南米草原詩の競技形式。"),
    ("コルデル表紙木版詩学", "cordel woodcut-cover poetics", "xilogravura de cordel", P_VANG, "ブラジル民衆冊子の木版表紙が読解を誘導する視覚詩学。"),
    ("デシマ・ハイバロ即興", "jibaro decima improvisation", "decima jibara", P_VANG, "プエルトリコ農民歌で十行詩を即興応答させる形式。"),
    ("トローバ・パイサ頓智問答", "trova paisa repartee", "trova paisa", P_VANG, "コロンビア山地の即興四行詩が機知で競う口承芸。"),
    ("ベラクルス・ソン詩脚", "Veracruz son verse-foot", "versada jarocha", P_VANG, "ソン・ハローチョ歌唱で即興連を支える押韻単位。"),
    ("チリ・リラ・ポプラール事件歌", "Chilean lira popular crime song", "lira popular de sucesos", P_VANG, "安価な一枚刷りが犯罪や災害を詩で速報する民衆媒体。"),

    # Cluster 3: forgotten authors and work-specific micro debates
    ("テラサス英雄詩断片", "Terrazas epic fragment", "fragmento epico de Terrazas", P_COLONIAL, "新スペイン初期詩人テラサスの未完英雄詩断片をめぐる概念。"),
    ("カビエデス医学風刺詩", "Caviedes medical satire", "satira medica de Caviedes", P_COLONIAL, "リマの医師文化を毒舌で攻撃する植民地バロック風刺。"),
    ("シグエンサ彗星パンフレット論争", "Siguenza comet pamphlet debate", "debate cometario de Siguenza", P_COLONIAL, "彗星解釈をめぐる新スペインの学知・信仰パンフレット論争。"),
    ("メルセデス・カベージョ自然主義論争", "Mercedes Cabello naturalism debate", "debate naturalista de Cabello", P_WOMEN, "ペルー女性作家の自然主義受容をめぐる道徳批評論争。"),
    ("アウタ・デ・ソウザ霊媒叙情", "Auta de Souza mediumistic lyric", "lirica mediumnica de Auta", P_WOMEN, "ブラジル象徴派女性詩を心霊主義読書へ接続する受容系。"),
    ("ホセフィーナ・プラ陶芸詩学", "Josefina Pla ceramic poetics", "poetica ceramica de Pla", P_WOMEN, "詩・陶芸・亡命感覚を交差させるパラグアイ前衛の小概念。"),

    # Cluster 4: subgenre variants of extractive and provincial modernity
    ("ゴム景気小説", "rubber-boom novel", "novela del caucho", P_VANG, "アマゾンのゴム採取暴力を描く辺境搾取小説の型。"),
    ("硝石鉱山クロニカ", "nitrate-mining cronica", "cronica salitrera", P_VANG, "チリ硝石鉱山の労働・事故・抗議を記録するクロニカ。"),
    ("カカオ農園メロドラマ", "cacao plantation melodrama", "melodrama cacaotero", P_VANG, "カカオ農園の相続・恋愛・労働を絡める地方小説類型。"),
    ("バナナ会社社史小説", "banana-company corporate novel", "novela bananera empresarial", P_POSTDICT, "バナナ企業の資料体裁で虐殺と労働支配を語る小説形式。"),
    ("エスタンシア衰退譚", "estancia decline tale", "relato de decadencia estanciera", P_VANG, "大農園家族の没落で地主制の終焉を語る地方叙事。"),
    ("河川汽船クロニカ", "river-steamer cronica", "cronica de vapor fluvial", P_VANG, "内陸河川汽船の移動空間を近代化の舞台にする記録文。"),

    # Cluster 5: theoretical micro-debates and translation edge cases
    ("インディアス・バロック命名論争", "Baroque of the Indies naming debate", "barroco de Indias", P_COLONIAL, "植民地バロックを欧州派生か現地変形かで争う命名問題。"),
    ("証言の編集者所有権論争", "testimonio editor ownership debate", "debate editorial del testimonio", P_POSTDICT, "証言文学で聞き手編集者の権利と改変範囲を問う論争。"),
    ("ボセオ翻訳不能性", "untranslatable voseo", "intraducibilidad del voseo", P_POSTDICT, "voseoの親密さ・階層差を他語へ移せない問題。"),
    ("ポルトニョール正書法詩", "Portunhol orthographic poetry", "poesia portunhol", P_POSTDICT, "国境混成語を揺れる綴字のまま詩化する実践。"),
    ("グアラニー二重言語詩学", "Guarani diglossic poetics", "poetica diglosica guarani", P_INDIG, "グアラニー語とスペイン語の権力差を形式化する詩学。"),
    ("ネオインディヘニスモ媒介性論", "neo-indigenismo mediation debate", "mediacion neoindigenista", P_INDIG, "非先住民作家が先住民声を媒介する資格を問う小論争。"),
]


def main() -> None:
    if len(ROWS) != 30:
        raise SystemExit(f"expected 30 rows, got {len(ROWS)}")
    too_long = [(name, len(defn)) for name, *_rest, defn in ROWS if len(defn) > 100]
    if too_long:
        raise SystemExit(f"definitions too long: {too_long}")
    with LitDB() as db:
        names = [row[0] for row in ROWS]
        placeholders = ",".join("?" for _ in names)
        existing = db.conn.execute(
            f"SELECT name_ja FROM concepts WHERE subfield_id = 16 AND name_ja IN ({placeholders})",
            names,
        ).fetchall()
        if existing:
            raise SystemExit(f"existing names: {[row[0] for row in existing]}")
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
        for name_ja, name_en, name_original, period_id, definition in ROWS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
    print(f"inserted={after - before} total={after}")


if __name__ == "__main__":
    main()
