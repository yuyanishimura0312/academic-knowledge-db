"""Wave 43: add 30 ultra-niche Korean literature concepts."""
from __future__ import annotations

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_se_asia_korea"
SUBFIELD_ID = 17
REGION = "グローバルサウス"


def period_id(db: LitDB, name_ja: str) -> int:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region=?",
        (name_ja, REGION),
    ).fetchone()
    if not row:
        raise RuntimeError(f"period not found: {name_ja}")
    return row["id"]


def main() -> None:
    with LitDB() as db:
        p_classic = period_id(db, "韓国古典文学期")
        p_joseon = period_id(db, "朝鮮王朝期")
        p_modern = period_id(db, "韓国近代期")
        p_contemp = period_id(db, "韓国現代期")
        p_km = period_id(db, "韓国近現代文学期")

        concepts = [
            # 1. 表記・注釈・仏教歌謡
            dict(name_ja="郷札『只』格助詞表記", name_en="Hyangchal -ji case marker", name_original="향찰 只", period_id=p_classic, definition="郷歌解読で格機能を担う郷札字の細部用法。"),
            dict(name_ja="郷歌『安民歌』政治讃歌構成", name_en="Anminga political hymn structure", name_original="안민가", period_id=p_classic, definition="君臣民の秩序を仏教的勧戒で詠む十句体郷歌。"),
            dict(name_ja="郷歌『慕竹旨郎歌』追慕叙情", name_en="Mojukjirangga elegiac lyric", name_original="모죽지랑가", period_id=p_classic, definition="花郎追慕を老いの感覚で組み立てる新羅郷歌。"),
            dict(name_ja="釈読口訣逆読符号", name_en="Seokdok gugyeol reverse-reading marks", name_original="석독구결 역독점", period_id=p_classic, definition="漢文を朝鮮語順に読むための口訣点の反転指示。"),
            dict(name_ja="『均如伝』郷歌注釈層", name_en="Gyunyeojeon hyangga gloss layer", name_original="균여전 향가 주석", period_id=p_classic, definition="均如郷歌を伝える伝記内の語釈・教義注記。"),
            dict(name_ja="高麗仏教偈頌漢詩", name_en="Goryeo Buddhist gatha poetry", name_original="고려 불교 게송", period_id=p_classic, definition="禅問答と修行境地を短い漢詩偈で示す高麗詩。"),

            # 2. 朝鮮後期写本・俗文学
            dict(name_ja="『沈清伝』貰冊本異本群", name_en="Segaekbon Simcheongjeon variants", name_original="세책본 심청전", period_id=p_joseon, definition="貸本流通で増補された沈清伝の写本・版本系統。"),
            dict(name_ja="『九雲夢』漢文・諺文本併存", name_en="Guunmong dual-script circulation", name_original="구운몽 한문본 언문본", period_id=p_joseon, definition="漢文原本とハングル読本が並行流通した受容形態。"),
            dict(name_ja="『淑香伝』女性読本圏", name_en="Sukhyangjeon women's reading sphere", name_original="숙향전", period_id=p_joseon, definition="女性読者の筆写・貸借で広がった才子佳人型古小説。"),
            dict(name_ja="『薔花紅蓮伝』公案小説性", name_en="Janghwa Hongryeonjeon legal-case fiction", name_original="장화홍련전", period_id=p_joseon, definition="継母迫害譚を訟獄解決へ結ぶ朝鮮公案小説。"),
            dict(name_ja="『謝氏南征記』家門諷諫読解", name_en="Sassi namjeonggi admonitory reading", name_original="사씨남정기", period_id=p_joseon, definition="家門小説形式で宮廷政治を諷諫する読解枠。"),
            dict(name_ja="『彰善感義録』善悪報応叙事", name_en="Changseon gamuirok karmic plot", name_original="창선감의록", period_id=p_joseon, definition="善悪報応を長篇家門秩序へ展開する古小説。"),

            # 3. パンソリ・民謡の微形式
            dict(name_ja="パンソリ『短歌』開場機能", name_en="Pansori danga opening function", name_original="판소리 단가", period_id=p_joseon, definition="長篇唱に先立ち声調と聴衆を整える短い歌。"),
            dict(name_ja="パンソリ『アニリ』叙述部", name_en="Pansori aniri narration", name_original="판소리 아니리", period_id=p_joseon, definition="唱の間を散文語りで接続するパンソリ叙述技法。"),
            dict(name_ja="パンソリ『ノルムセ』身体演技", name_en="Pansori neoreumsae gesture", name_original="판소리 너름새", period_id=p_joseon, definition="扇子・身振りで場面を可視化する唱者の演技。"),
            dict(name_ja="パンソリ『チュイムセ』聴衆応答", name_en="Pansori chuimsae audience calls", name_original="판소리 추임새", period_id=p_joseon, definition="鼓手や聴衆が挟む掛け声による共演的応答。"),
            dict(name_ja="京畿雑歌『十二雑歌』", name_en="Gyeonggi twelve japga", name_original="경기 십이잡가", period_id=p_joseon, definition="京畿名唱圏で整えられた長歌系俗謡レパートリー。"),
            dict(name_ja="民謡『アリラン』本調系譜", name_en="Arirang bonjo lineage", name_original="아리랑 본조", period_id=p_km, definition="地域変奏の基準とされるアリラン基本旋律系。"),

            # 4. 植民地期メディア・文芸制度
            dict(name_ja="『朝光』総合雑誌文芸欄", name_en="Chogwang literary section", name_original="조광 문예란", period_id=p_modern, definition="大衆総合誌で小説・随筆を編成した植民地期欄。"),
            dict(name_ja="『女性』誌新女性随筆", name_en="Yeoseong magazine New Woman essays", name_original="여성 신여성 수필", period_id=p_modern, definition="新女性の生活感覚を商品文化と結ぶ雑誌随筆。"),
            dict(name_ja="京城放送局ラジオドラマ", name_en="Gyeongseong radio drama", name_original="경성방송국 라디오드라마", period_id=p_modern, definition="植民地期放送で脚本化された朝鮮語劇文学。"),
            dict(name_ja="『毎日申報』連載通俗小説", name_en="Maeil Sinbo serial popular fiction", name_original="매일신보 연재소설", period_id=p_modern, definition="新聞連載で消費された恋愛・家庭通俗小説。"),
            dict(name_ja="プロレタリア児童文学欄", name_en="Proletarian children's literature column", name_original="프로 아동문학란", period_id=p_modern, definition="階級意識を童話・童謡へ移した左翼文芸欄。"),
            dict(name_ja="満洲朝鮮人移民小説", name_en="Manchurian Korean migrant fiction", name_original="만주 조선인 이민소설", period_id=p_modern, definition="満洲移住地の貧困と民族境界を描く植民地小説。"),

            # 5. 分断・移動・記憶文学
            dict(name_ja="捕虜収容所手記文学", name_en="POW camp memoir literature", name_original="포로수용소 수기문학", period_id=p_km, definition="朝鮮戦争捕虜体験を証言体で記す記憶文学。"),
            dict(name_ja="離北作家の失郷小説", name_en="Northern refugee lost-home fiction", name_original="이북 출신 작가 실향소설", period_id=p_km, definition="越南作家が故郷喪失を反復する分断小説。"),
            dict(name_ja="光州抗争獄中詩", name_en="Gwangju prison protest poetry", name_original="광주항쟁 옥중시", period_id=p_contemp, definition="拘禁経験から光州の暴力を記録する抵抗詩。"),
            dict(name_ja="労働者手記『全泰壱』系譜", name_en="Jeon Tae-il worker memoir lineage", name_original="전태일 노동자 수기", period_id=p_contemp, definition="労働現場の自己記録を運動記憶へ接続する手記群。"),
            dict(name_ja="脱北者証言小説", name_en="North Korean defector testimony fiction", name_original="탈북자 증언소설", period_id=p_contemp, definition="脱北経験を証言と小説技法の間で語る現代叙事。"),
            dict(name_ja="コリョサラム強制移住詩", name_en="Koryo-saram deportation poetry", name_original="고려사람 강제이주 시", period_id=p_km, definition="中央アジア移住の記憶を朝鮮語・ロシア語で詠む詩。"),
        ]

        existing_all = {
            row["name_ja"] for row in db.conn.execute("SELECT name_ja FROM concepts")
        }
        overlap = [c["name_ja"] for c in concepts if c["name_ja"] in existing_all]
        if overlap:
            raise RuntimeError(f"already present: {overlap}")
        if len(concepts) != 30:
            raise RuntimeError(f"expected 30 concepts, got {len(concepts)}")
        too_long = [c["name_ja"] for c in concepts if len(c["definition"]) > 100]
        if too_long:
            raise RuntimeError(f"definition too long: {too_long}")

        inserted = 0
        for concept in concepts:
            db.insert_concept(
                **concept,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
        print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
