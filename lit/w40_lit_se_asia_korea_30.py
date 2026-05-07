"""Wave 40: add 30 hyper-niche Korean concepts to lit_se_asia_korea."""
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
        p_joseon = period_id(db, "朝鮮王朝期")
        p_modern = period_id(db, "韓国近代期")
        p_contemp = period_id(db, "韓国現代期")
        p_km = period_id(db, "韓国近現代文学期")

        concepts = [
            # 1. 地方巫歌・口承叙事
            dict(name_ja="済州巫歌『チョゴン本解』", name_en="Chogong bonpuri", name_original="초공본풀이", period_id=p_joseon, definition="済州巫俗の神職起源を語る本解系叙事巫歌。"),
            dict(name_ja="済州巫歌『三公本解』", name_en="Samgong bonpuri", name_original="삼공본풀이", period_id=p_joseon, definition="運命神の由来を語る済州本解系の口承叙事。"),
            dict(name_ja="済州巫歌『セギョン本解』", name_en="Segyeong bonpuri", name_original="세경본풀이", period_id=p_joseon, definition="農耕神セギョンの来歴を唱える済州巫歌。"),
            dict(name_ja="東海岸別神クッ巫歌", name_en="East Coast Byeolsin-gut songs", name_original="동해안별신굿 무가", period_id=p_km, definition="漁村祭儀で世襲巫が唱える東海岸系叙事歌。"),
            dict(name_ja="西道雑歌『愁心歌』", name_en="Suseimga", name_original="수심가", period_id=p_joseon, definition="平安・黄海道系の哀調をもつ西道雑歌の定番曲。"),
            dict(name_ja="南道雑歌『興打令』", name_en="Heung taryeong", name_original="흥타령", period_id=p_joseon, definition="全羅系の掛け声と反復をもつ南道雑歌。"),

            # 2. 写本・流通・古小説の微形態
            dict(name_ja="閨房歌辞内房筆写本", name_en="Gyubang gasa manuscript copies", name_original="규방가사 내방필사본", period_id=p_joseon, definition="女性読者が内房で筆写した歌辞写本群。"),
            dict(name_ja="貰冊本小説", name_en="Segaekbon fiction", name_original="세책본 소설", period_id=p_joseon, definition="貸本屋を通じ流通した朝鮮後期のハングル小説本。"),
            dict(name_ja="坊刻本古小説", name_en="Banggangbon old fiction", name_original="방각본 고소설", period_id=p_joseon, definition="民間板元が刊行した商業木版本の古小説。"),
            dict(name_ja="完板本『烈女春香守節歌』", name_en="Wanpan edition of Yeolnyeo Chunhyang sujeolga", name_original="완판본 열녀춘향수절가", period_id=p_joseon, definition="全州刊本に属する春香伝系の長篇異本。"),
            dict(name_ja="京板本『洪吉童伝』", name_en="Gyeongpan Hong Gildongjeon", name_original="경판본 홍길동전", period_id=p_joseon, definition="漢城坊刻本に残る洪吉童伝の短縮流通形。"),
            dict(name_ja="夢遊録小説", name_en="Mongyurok dream-journey fiction", name_original="몽유록", period_id=p_joseon, definition="夢の旅で歴史批評を行う朝鮮漢文小説類型。"),

            # 3. 女性著述・周縁文人
            dict(name_ja="金三宜堂の漢詩", name_en="Kim Samuidang poetry", name_original="김삼의당 한시", period_id=p_joseon, definition="夫婦唱和と地方女性の教養を示す漢詩作品群。"),
            dict(name_ja="姜静一堂『静一堂遺稿』", name_en="Gang Jeongildang, Jeongildang yugo", name_original="정일당유고", period_id=p_joseon, definition="性理学修養を女性の声で記す朝鮮後期文集。"),
            dict(name_ja="任允摯堂『允摯堂遺稿』", name_en="Im Yunjidang, Yunjidang yugo", name_original="윤지당유고", period_id=p_joseon, definition="女性儒学者の理気論と詩文を収めた遺稿。"),
            dict(name_ja="李師朱堂『胎教新記』", name_en="Yi Sajudang, Taegyo singi", name_original="태교신기", period_id=p_joseon, definition="胎教を女性知として体系化した朝鮮後期教訓書。"),
            dict(name_ja="羅蕙錫『瓊姫』", name_en="Na Hye-seok, Gyeonghui", name_original="경희", period_id=p_modern, definition="新女性の自我葛藤を描く植民地期短編。"),
            dict(name_ja="金明淳『疑心の少女』", name_en="Kim Myeong-sun, The Suspicious Girl", name_original="의심의 소녀", period_id=p_modern, definition="女性作家の告白体を開いた初期近代短編。"),

            # 4. 植民地期小同人・批評微論争
            dict(name_ja="九人会同人", name_en="Guinhoe circle", name_original="구인회", period_id=p_modern, definition="京城モダニズムを支えた一九三〇年代の九人同人。"),
            dict(name_ja="『白潮』同人誌", name_en="Baekjo magazine", name_original="백조", period_id=p_modern, definition="浪漫主義詩と感傷的散文を掲げた初期同人誌。"),
            dict(name_ja="『詩文学』同人誌", name_en="Simunhak magazine", name_original="시문학", period_id=p_modern, definition="純粋詩論を提示した一九三〇年代詩専門誌。"),
            dict(name_ja="朝鮮農民小説論争", name_en="Korean peasant fiction debate", name_original="농민소설 논쟁", period_id=p_modern, definition="農村現実の表象方法をめぐる植民地期批評論争。"),
            dict(name_ja="カップ解散期転向小説", name_en="KAPF dissolution conversion fiction", name_original="카프 해산기 전향소설", period_id=p_modern, definition="左翼文学者の転向心理を物語化した一九三〇年代小説。"),
            dict(name_ja="京城考現学的散文", name_en="Gyeongseong modernological prose", name_original="경성 고현학 산문", period_id=p_modern, definition="都市観察を断片化して書く植民地京城の散文実験。"),

            # 5. 北朝鮮・在日・冷戦周縁
            dict(name_ja="主体文学の種子論", name_en="Seed theory in Juche literature", name_original="종자론", period_id=p_contemp, definition="作品の核心思想を種子と呼ぶ北朝鮮文芸理論。"),
            dict(name_ja="首領形象文学", name_en="Suryong image literature", name_original="수령형상문학", period_id=p_contemp, definition="指導者像の造形を中心に据える北朝鮮文学様式。"),
            dict(name_ja="革命歌劇台本文学", name_en="Revolutionary opera libretti", name_original="혁명가극 대본문학", period_id=p_contemp, definition="北朝鮮革命歌劇の唱詞と台本を文学化する領域。"),
            dict(name_ja="総聯系朝鮮語児童文学", name_en="Chongryon Korean-language children's literature", name_original="총련계 조선어 아동문학", period_id=p_km, definition="在日朝鮮学校圏で読まれた朝鮮語児童文学。"),
            dict(name_ja="済州四・三詩歌", name_en="Jeju 4.3 poetry", name_original="제주4·3 시가", period_id=p_km, definition="済州四・三事件の記憶を歌う地域詩歌群。"),
            dict(name_ja="サハリン韓人回想記", name_en="Sakhalin Korean memoir writing", name_original="사할린 한인 회상기", period_id=p_km, definition="強制移住と帰還未遂を記すサハリン韓人の回想文。"),
        ]

        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
            )
        }
        overlap = [c["name_ja"] for c in concepts if c["name_ja"] in existing]
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
