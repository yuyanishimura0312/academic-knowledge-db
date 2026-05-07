"""Wave 42: add 30 hyper-niche Korean literature concepts."""
from __future__ import annotations

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_se_asia_korea"
SUBFIELD_ID = 17
REGION = "グローバルサウス"


def pid(db: LitDB, name_ja: str) -> int:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region=?",
        (name_ja, REGION),
    ).fetchone()
    if not row:
        raise RuntimeError(f"period not found: {name_ja}")
    return row["id"]


def main() -> None:
    with LitDB() as db:
        p_classic = pid(db, "韓国古典文学期")
        p_joseon = pid(db, "朝鮮王朝期")
        p_modern = pid(db, "韓国近代期")
        p_contemp = pid(db, "韓国現代期")
        p_km = pid(db, "韓国近現代文学期")

        concepts = [
            # 1. 郷歌・口訣・高麗歌謡の微細単位
            dict(name_ja="郷歌『怨歌』讒言モチーフ", name_en="Hyangga Wonga slander motif", name_original="원가", period_id=p_classic, definition="讒言で退けられた忠臣の恨みを詠む八句体郷歌。"),
            dict(name_ja="郷歌『祭亡妹歌』十句体構成", name_en="Jemangmaega ten-line form", name_original="제망매가", period_id=p_classic, definition="亡妹追悼を十句体の仏教的転回で結ぶ郷歌。"),
            dict(name_ja="郷札『叱音』終声表記", name_en="Hyangchal sieus-eum coda notation", name_original="叱音", period_id=p_classic, definition="郷札で朝鮮語終声を借字で示す表記慣行。"),
            dict(name_ja="口訣点吐読法", name_en="Gugyeol point reading marks", name_original="구결점 토독법", period_id=p_classic, definition="漢文訓読の助詞・語順を点で補う高麗系読法。"),
            dict(name_ja="高麗歌謡『井邑詞』望夫歌", name_en="Jeongeupsa waiting-wife song", name_original="정읍사", period_id=p_classic, definition="夜道の夫の無事を月に祈る百済系伝承歌。"),
            dict(name_ja="高麗歌謡『青山別曲』余音句", name_en="Cheongsan byeolgok refrain", name_original="청산별곡 여음구", period_id=p_classic, definition="反復余音で流浪と退避願望を響かせる高麗歌謡。"),

            # 2. パンソリ・唱本・雑歌の局所形式
            dict(name_ja="東便制パンソリ羽調", name_en="Dongpyeonje ujo mode", name_original="동편제 우조", period_id=p_joseon, definition="力強い羽調を軸にする全羅東部系パンソリ唱法。"),
            dict(name_ja="西便制パンソリ界面調", name_en="Seopyeonje gyemyeonjo mode", name_original="서편제 계면조", period_id=p_joseon, definition="哀調の界面調を精緻化した全羅西部系唱法。"),
            dict(name_ja="中高制パンソリ忠清伝承", name_en="Junggoge pansori lineage", name_original="중고제", period_id=p_joseon, definition="忠清圏に伝わる古風で淡泊なパンソリ流派。"),
            dict(name_ja="申在孝版『兎別歌』唱本", name_en="Sin Jae-hyo Tobyeolga text", name_original="신재효본 토별가", period_id=p_joseon, definition="申在孝が整理した水宮歌系パンソリ唱本。"),
            dict(name_ja="パンソリ『変強釗歌』失伝唱", name_en="Lost Byeongangsoe pansori", name_original="변강쇠가", period_id=p_joseon, definition="放浪男女と禁忌破りを描く失伝系パンソリ一曲。"),
            dict(name_ja="丹歌『広大歌』芸能者自嘲", name_en="Gwangdaega short song", name_original="광대가", period_id=p_joseon, definition="広大の境遇を自嘲的に歌うパンソリ前唱短歌。"),

            # 3. 閨房・内房・家門小説の微ジャンル
            dict(name_ja="閨房歌辞『花煎歌』", name_en="Hwajeonga women's gasa", name_original="화전가", period_id=p_joseon, definition="春の花煎遊びを女性共同体の声で記す閨房歌辞。"),
            dict(name_ja="閨房歌辞『思親歌』", name_en="Sachinga women's gasa", name_original="사친가", period_id=p_joseon, definition="嫁入り後の実家恋慕を長歌化した女性歌辞。"),
            dict(name_ja="閨房歌辞『歎老歌』", name_en="Tannoga women's gasa", name_original="탄로가", period_id=p_joseon, definition="老いと家内労働の感覚を詠む内房系歌辞。"),
            dict(name_ja="『閨中七友争論記』針線寓話", name_en="Gyujung chil-u jaengnon-gi", name_original="규중칠우쟁론기", period_id=p_joseon, definition="裁縫道具七友の争いで女性労働を寓話化する小品。"),
            dict(name_ja="『玉楼夢』家門小説", name_en="Ongnumong family-lineage fiction", name_original="옥루몽", period_id=p_joseon, definition="才子佳人譚を大河化した朝鮮後期家門小説。"),
            dict(name_ja="『河陳両門録』両門婚姻叙事", name_en="Ha-Jin yangmunnok", name_original="하진양문록", period_id=p_joseon, definition="二家門の婚姻葛藤を連鎖させる長篇国文小説。"),

            # 4. 植民地期雑誌・同人場の局所媒体
            dict(name_ja="『朝鮮文壇』新人推薦欄", name_en="Joseon Mundan newcomer column", name_original="조선문단 추천란", period_id=p_modern, definition="植民地期作家登竜門となった文芸誌の推薦制度。"),
            dict(name_ja="『別乾坤』通俗文芸欄", name_en="Byeolgeongon popular literature pages", name_original="별건곤", period_id=p_modern, definition="都市読者向け逸話と通俗文芸を載せた総合雑誌欄。"),
            dict(name_ja="『三千里』女性読者欄", name_en="Samcheolli women readers column", name_original="삼천리 여성독자란", period_id=p_modern, definition="女性投稿と相談記事が交差した大衆雑誌の読者欄。"),
            dict(name_ja="『文章』推薦作家制度", name_en="Munjang recommendation system", name_original="문장 추천제", period_id=p_modern, definition="李泰俊らが新人を選抜した一九三九年創刊誌制度。"),
            dict(name_ja="『人文評論』転向批評欄", name_en="Inmun pyeongnon conversion criticism", name_original="인문평론", period_id=p_modern, definition="転向後知識人の文学論を載せた植民地末期評論場。"),
            dict(name_ja="『カトリック青年』詩壇", name_en="Catholic Youth poetry circle", name_original="가톨릭청년 시단", period_id=p_modern, definition="鄭芝溶周辺の宗教詩を支えたカトリック系誌面。"),

            # 5. 解放後・民衆・冷戦周縁の小領域
            dict(name_ja="四月革命詩アンソロジー", name_en="April Revolution poetry anthology", name_original="4월혁명시 선집", period_id=p_contemp, definition="一九六〇年蜂起の街頭経験を集成した詩歌群。"),
            dict(name_ja="釜馬抗争詩歌", name_en="Buma uprising poetry", name_original="부마항쟁 시가", period_id=p_contemp, definition="釜山・馬山抗争を地域記憶として詠む抵抗詩。"),
            dict(name_ja="朴労解『労働の夜明け』地下流通", name_en="Park Nohae underground circulation", name_original="노동의 새벽", period_id=p_contemp, definition="労働現場詩が非合法出版で読まれた八〇年代詩集。"),
            dict(name_ja="『実践文学』民衆文芸欄", name_en="Silcheon Munhak minjung pages", name_original="실천문학", period_id=p_contemp, definition="民衆文学の詩・ルポ・評論を結んだ文芸誌面。"),
            dict(name_ja="マダン劇『鳳山仮面劇』翻案台本", name_en="Bongsan mask play madanggeuk scripts", name_original="봉산탈춤 마당극 각색본", period_id=p_km, definition="仮面劇を運動圏の広場劇へ移した翻案台本群。"),
            dict(name_ja="離散家族手記『望郷』型", name_en="Separated-family manghyang memoir type", name_original="망향 수기", period_id=p_km, definition="分断で故郷喪失を語る離散家族の投稿手記類型。"),
        ]

        if len(concepts) != 30:
            raise RuntimeError(f"expected 30 concepts, got {len(concepts)}")
        too_long = [c["name_ja"] for c in concepts if len(c["definition"]) > 100]
        if too_long:
            raise RuntimeError(f"definition too long: {too_long}")

        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
            )
        }
        overlap = [c["name_ja"] for c in concepts if c["name_ja"] in existing]
        if overlap:
            raise RuntimeError(f"already present: {overlap}")

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
