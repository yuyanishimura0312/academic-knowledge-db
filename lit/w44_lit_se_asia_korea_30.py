"""Wave 44: add 30 ultra-niche Korean literature concepts."""
from __future__ import annotations

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_se_asia_korea"
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
            # 1. 郷歌・口訣・漢文微形式
            dict(name_ja="郷歌『処容歌』疫神退散読解", name_en="Cheoyongga plague-expulsion reading", name_original="처용가", period_id=p_classic, definition="疫神との対面を呪術的和解で処理する郷歌読解。"),
            dict(name_ja="郷歌『兜率歌』弥勒請願構成", name_en="Dosolga Maitreya petition structure", name_original="도솔가", period_id=p_classic, definition="弥勒下生を願う儀礼歌として読む新羅郷歌。"),
            dict(name_ja="郷歌『献花歌』海岸献花場面", name_en="Heonhwaga flower-offering scene", name_original="헌화가", period_id=p_classic, definition="老人の献花行為で欲望と神異を結ぶ四句体郷歌。"),
            dict(name_ja="郷札『良』目的格標識", name_en="Hyangchal ryang object marker", name_original="향찰 良", period_id=p_classic, definition="郷歌本文で目的格機能を担う郷札字の用法。"),
            dict(name_ja="点吐口訣『乎』終結標識", name_en="Gugyeol ho sentence-final mark", name_original="구결 乎", period_id=p_classic, definition="漢文訓読で文末語気を示す口訣字の細部機能。"),
            dict(name_ja="高麗文人仮伝『孔方伝』", name_en="Gongbangjeon pseudo-biography", name_original="공방전", period_id=p_classic, definition="銭を人物化して利欲を諷刺する高麗仮伝文学。"),

            # 2. 朝鮮写本・女性読書圏
            dict(name_ja="諺解本『小學』内房読書", name_en="Eonhae Sohak women's reading", name_original="언해 소학", period_id=p_joseon, definition="女性教訓読書に用いられたハングル注解儒教書。"),
            dict(name_ja="『女四書諺解』訓育文体", name_en="Yeosaseo eonhae didactic style", name_original="여사서언해", period_id=p_joseon, definition="婦徳規範を翻訳文体で定着させた女性教訓書。"),
            dict(name_ja="『内訓』諺解女性規範", name_en="Naehun eonhae women's norms", name_original="내훈언해", period_id=p_joseon, definition="宮廷女性訓戒をハングル読本へ移した規範文。"),
            dict(name_ja="『癸丑日記』西宮幽閉叙述", name_en="Gyechuk ilgi palace confinement narrative", name_original="계축일기", period_id=p_joseon, definition="西宮幽閉事件を宮廷女性の視点で記す日記体叙事。"),
            dict(name_ja="『恨中録』世子死事件章", name_en="Hanjungnok crown-prince death chapter", name_original="한중록", period_id=p_joseon, definition="思悼世子事件を回想録内で再構成する核心章。"),
            dict(name_ja="『壬辰録』義兵英雄譚異本", name_en="Imjinrok righteous-army variants", name_original="임진록", period_id=p_joseon, definition="壬辰倭乱の義兵英雄を増殖させる古小説異本群。"),

            # 3. パンソリ・巫歌・地域唱
            dict(name_ja="パンソリ『内浦制』忠南唱法", name_en="Naepoje pansori style", name_original="내포제 판소리", period_id=p_joseon, definition="忠南内浦地域に伝わるパンソリ唱法の地域型。"),
            dict(name_ja="パンソリ『ジャジンモリ』急調部", name_en="Pansori jajinmori fast rhythm", name_original="자진모리", period_id=p_joseon, definition="場面転換や興奮を支える速いパンソリ長短。"),
            dict(name_ja="パンソリ『中モリ』叙情長短", name_en="Pansori jungmori lyric rhythm", name_original="중모리", period_id=p_joseon, definition="哀感や叙情場面を支える中速のパンソリ長短。"),
            dict(name_ja="巫歌『バリ公主』死霊済度譚", name_en="Princess Bari soul-guiding shaman song", name_original="바리공주", period_id=p_joseon, definition="捨て子女神が死者を導く巫俗叙事歌。"),
            dict(name_ja="済州巫歌『イコン本解』農耕神話", name_en="Jeju Igong bonpuri farming myth", name_original="이공본풀이", period_id=p_joseon, definition="花園管理神の由来を語る済州本解系巫歌。"),
            dict(name_ja="西道雑歌『排従歌』別離唱", name_en="Seodo japga Baejongga farewell song", name_original="배종가", period_id=p_joseon, definition="西道雑歌で旅立ちと別離を歌う長歌系レパートリー。"),

            # 4. 植民地期媒体・制度
            dict(name_ja="『開闢』文芸懸賞欄", name_en="Gaebyeok literary prize column", name_original="개벽 문예현상", period_id=p_modern, definition="新人作品を公募し近代文壇へ接続した雑誌制度。"),
            dict(name_ja="『新女性』恋愛相談文体", name_en="Sinyeoseong love-advice style", name_original="신여성 연애상담", period_id=p_modern, definition="恋愛相談を通じて新女性像を形成した雑誌文体。"),
            dict(name_ja="『東光』民族改造論文欄", name_en="Donggwang national-remaking essays", name_original="동광 민족개조론", period_id=p_modern, definition="啓蒙論説と文芸批評を結んだ民族改造論の欄。"),
            dict(name_ja="『朝鮮日報』新春文芸初期欄", name_en="Chosun Ilbo early spring literary contest", name_original="조선일보 신춘문예", period_id=p_modern, definition="新聞懸賞で新人小説・詩を選抜した登竜門欄。"),
            dict(name_ja="『東亜日報』連載農村小説", name_en="Dong-A Ilbo serialized rural fiction", name_original="동아일보 농촌소설", period_id=p_modern, definition="農村啓蒙と恋愛叙事を新聞連載で結んだ小説群。"),
            dict(name_ja="カップ映画小説欄", name_en="KAPF film-fiction column", name_original="카프 영화소설란", period_id=p_modern, definition="左翼文芸が映画筋書と小説形式を接続した欄。"),

            # 5. 分断後・移動・証言の小形式
            dict(name_ja="戦後避難民詩『板子村』表象", name_en="Postwar shantytown refugee poetry", name_original="판자촌 피난민 시", period_id=p_km, definition="避難民の板子村生活を都市貧困として詠む詩群。"),
            dict(name_ja="越南作家の北方方言挿入", name_en="Northern-refugee dialect insertion", name_original="월남작가 북방방언", period_id=p_km, definition="失郷感を北方方言の挿入で示す分断小説技法。"),
            dict(name_ja="在日朝鮮人『季刊三千里』文学欄", name_en="Kikan Sanzenri literary section", name_original="계간 삼천리 문학란", period_id=p_contemp, definition="在日知識人誌で詩・小説・評論を交差させた欄。"),
            dict(name_ja="光州聴聞会証言文学化", name_en="Gwangju hearing testimony literarization", name_original="광주청문회 증언문학", period_id=p_contemp, definition="公的証言を詩・小説の記憶形式へ転換する実践。"),
            dict(name_ja="セウォル号追悼詩アンソロジー", name_en="Sewol memorial poetry anthology", name_original="세월호 추모시집", period_id=p_contemp, definition="災害喪失と国家責任を追悼詩で記録する詩集群。"),
            dict(name_ja="脱北女性口述自伝叙事", name_en="North Korean women oral autobiography", name_original="탈북여성 구술자서전", period_id=p_contemp, definition="脱北女性の移動と暴力を口述自伝で語る叙事形式。"),
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

        for concept in concepts:
            db.insert_concept(
                **concept,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
        print(f"inserted={len(concepts)}")


if __name__ == "__main__":
    main()
