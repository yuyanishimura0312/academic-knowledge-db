#!/usr/bin/env python3
"""Wave42: add 30 ultra-niche concepts to lit_latin_america."""

from lit_db_helper import LitDB

SUBFIELD = "lit_latin_america"
REGION = "ラテンアメリカ"

P_COLONIAL = 254
P_19C = 255
P_AFRO_CARIB = 227
P_POSTDICT = 260
P_21C = 288

ROWS = [
    # Cluster 1: colonial legal-visual microarchives
    ("メルセー訴願地図余白", "merced petition map margin", "margen de mapa de merced", P_COLONIAL, "土地授与訴願図の余白注記を読む植民地文書概念。"),
    ("レドゥクシオン村名簿声", "reduccion roster voice", "voz de padron reduccional", P_COLONIAL, "集住村名簿に残る改宗名と親族記憶の語り痕跡。"),
    ("異端審問通訳書記", "inquisition interpreter scribe", "escribano interprete inquisitorial", P_COLONIAL, "異端審問記録で通訳が証言文体を媒介する役割。"),
    ("ミタ免除嘆願定型", "mita exemption petition formula", "formula de exencion de mita", P_COLONIAL, "ミタ労役免除願に反復される病・貧困・忠誠の句法。"),
    ("聖体行列座席争い記録", "Corpus procession seating dispute", "pleito de asiento procesional", P_COLONIAL, "聖体行列の席次争いから身分序列を読む訴訟記録。"),
    ("教区婚姻調査恋文", "parish marriage inquiry love letter", "carta de amancebamiento", P_COLONIAL, "婚姻調査に添付された恋文を裁判文書として読む概念。"),

    # Cluster 2: 19th-century serial and print edges
    ("港湾税関フェリェトン", "customhouse folletin", "folletin aduanero", P_19C, "税関・密輸の噂を新聞連載小説へ変える港湾都市文体。"),
    ("電報戦争クロニカ", "telegraph war cronica", "cronica belica telegrafica", P_19C, "電報速報の断片性で内戦を報じる十九世紀クロニカ。"),
    ("亡命印刷所奥付政治", "exile press colophon politics", "politica de pie de imprenta", P_19C, "亡命地の印刷所奥付が政治的連帯を示す出版痕跡。"),
    ("婦人新聞仮名署名", "women's newspaper pseudonym signature", "seudonimo de prensa femenina", P_19C, "婦人紙の仮名署名が検閲と名誉規範をかわす実践。"),
    ("鉄道開通頌詩広告", "railway inauguration ode ad", "oda ferroviaria publicitaria", P_19C, "鉄道開通詩が広告文と国民進歩論を混ぜる形式。"),
    ("黄熱病死亡欄叙情", "yellow-fever obituary lyric", "lirica necrologica febril", P_19C, "黄熱病流行時の死亡欄に生じる都市的哀悼文体。"),

    # Cluster 3: Afro-Caribbean and creole mediations
    ("パレンケ逃亡告示詩学", "palenque runaway notice poetics", "poetica de cimarronaje", P_AFRO_CARIB, "逃亡奴隷告示の身体記述を抵抗の読解へ反転する概念。"),
    ("アフロ宗教供物目録", "Afro-religious offering inventory", "inventario de ofrendas afro", P_AFRO_CARIB, "供物目録から神霊・商品・植民地権力の接点を読む。"),
    ("クレオール子守唄翻字", "Creole lullaby transliteration", "transliteracion de nana criolla", P_AFRO_CARIB, "クレオール語子守唄を宗主国語表記へ移す媒介実践。"),
    ("砂糖工場鐘声記憶", "sugar-mill bell memory", "memoria de campana ingenio", P_AFRO_CARIB, "製糖工場の鐘声を労働時間と恐怖の記憶装置として読む。"),
    ("ラスタファリ書簡スペイン語化", "Rastafari letter Hispanization", "hispanizacion epistolar rastafari", P_AFRO_CARIB, "ラスタファリ書簡がスペイン語圏で再記号化される翻訳現象。"),
    ("コンパルサ仮装新聞評", "comparsa costume press review", "resena de comparsa", P_AFRO_CARIB, "カーニバル仮装評が人種風刺を紙面化する短評形式。"),

    # Cluster 4: post-dictatorship material traces
    ("押収タイプ原稿亡霊", "seized typescript ghost", "fantasma de mecanoscrito incautado", P_POSTDICT, "押収タイプ原稿の欠落と複写跡を記憶媒体として読む概念。"),
    ("地下出版ステンシル痕", "underground stencil trace", "rastro de mimeografo clandestino", P_POSTDICT, "地下出版物のステンシルずれを抵抗の物質痕跡として扱う。"),
    ("亡命葉書検閲黒塗り", "exile postcard redaction", "tachadura de postal exiliada", P_POSTDICT, "亡命葉書の黒塗りを親密圏と国家監視の接点として読む。"),
    ("真実委員会沈黙段落", "truth-commission silence paragraph", "parrafo de silencio", P_POSTDICT, "証言報告書の沈黙や中断を叙述単位として読む概念。"),
    ("スタジアム収容所落書き", "stadium camp graffiti", "grafiti de estadio-campo", P_POSTDICT, "競技場収容所の落書きを臨時監禁の文字記憶として読む。"),
    ("返還児童身元詩", "returned-child identity poem", "poema de identidad restituida", P_POSTDICT, "奪われた子どもの身元回復を詩の証明構造にする形式。"),

    # Cluster 5: 21st-century platform and extractive ecologies
    ("リチウム塩湖クロニカ", "lithium salar cronica", "cronica de salar litico", P_21C, "リチウム採掘と先住民領域を記録する塩湖クロニカ。"),
    ("麻薬潜水艇叙事断章", "narco-submarine epic fragment", "fragmento epico narcosubmarino", P_21C, "密輸潜水艇の噂を海洋叙事の断章へ変える語り。"),
    ("WhatsApp失踪者連鎖語り", "WhatsApp missing-person chain narration", "cadena de desaparecidos", P_21C, "失踪者捜索の転送文が共同体語りを形成する形式。"),
    ("森林火災煙日記", "wildfire smoke diary", "diario de humo incendiario", P_21C, "森林火災の煙と呼吸不全を日記形式で記録する環境文体。"),
    ("観光Airbnb廃墟詩", "Airbnb ruin poem", "poema de ruina turistica", P_21C, "観光民泊化で空洞化した街区を廃墟として詠む都市詩。"),
    ("配達アプリ労働クロニカ", "delivery-app labor cronica", "cronica de repartidor app", P_21C, "配達アプリ労働のGPS経路と危険を記録する都市クロニカ。"),
]


def main() -> None:
    if len(ROWS) != 30:
        raise SystemExit(f"expected 30 rows, got {len(ROWS)}")
    too_long = [(name, len(defn)) for name, *_rest, defn in ROWS if len(defn) > 100]
    if too_long:
        raise SystemExit(f"definitions too long: {too_long}")

    with LitDB() as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
        ids = []
        for name_ja, name_en, name_original, period_id, definition in ROWS:
            ids.append(db.insert_concept(
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
            ))
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=16"
        ).fetchone()[0]
    print(f"inserted={after - before} touched={len(ids)} total={after}")


if __name__ == "__main__":
    main()
