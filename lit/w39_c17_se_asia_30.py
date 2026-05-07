"""Wave 39: add 30 ultra-niche Korean concepts to lit_se_asia_korea."""
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
        p_goryeo = period_id(db, "高麗期")
        p_joseon = period_id(db, "朝鮮王朝期")
        p_modern = period_id(db, "韓国近代期")
        p_km = period_id(db, "韓国近現代文学期")

        concepts = [
            # 1. 新羅・高麗の稀少漢文散文
            dict(name_ja="慧超『往五天竺国伝』", name_en="Hyecho, Memoir of the Pilgrimage to the Five Kingdoms of India", name_original="往五天竺國傳", period_id=p_goryeo, definition="新羅僧慧超のインド巡礼を記す断簡旅行記。"),
            dict(name_ja="崔致遠『桂苑筆耕集』", name_en="Choe Chiwon, Gyewon pilgyeong", name_original="桂苑筆耕集", period_id=p_goryeo, definition="唐滞在期の表奏文を集めた新羅末期漢文集。"),
            dict(name_ja="李仁老『破閑集』", name_en="Yi In-ro, Pahanjip", name_original="破閑集", period_id=p_goryeo, definition="高麗文人の詩話と逸話を集めた閑談集。"),
            dict(name_ja="林椿『麹醇伝』", name_en="Im Chun, Guk Sun jeon", name_original="麴醇傳", period_id=p_goryeo, definition="酒を擬人化し官僚社会を諷す高麗仮伝体。"),
            dict(name_ja="李奎報『麹先生伝』", name_en="Yi Gyubo, Master Guk", name_original="麴先生傳", period_id=p_goryeo, definition="麹先生を主人公にした酒徳風刺の仮伝体短編。"),
            dict(name_ja="高麗歌謡『動動』", name_en="Dongdong", name_original="動動", period_id=p_goryeo, definition="月令形式で恋慕を歌う高麗俗謡の代表的断章。"),

            # 2. 朝鮮野談・笑話・異本
            dict(name_ja="柳夢寅『於于野談』", name_en="Yu Mong-in, Eou yadam", name_original="於于野談", period_id=p_joseon, definition="士大夫社会の奇聞逸話を集めた朝鮮野談集。"),
            dict(name_ja="任埅『天倪録』", name_en="Im Bang, Cheon-ye rok", name_original="天倪錄", period_id=p_joseon, definition="怪異と因果譚を記録した朝鮮後期野談集。"),
            dict(name_ja="李鈺『鳳城文餘』", name_en="Yi Ok, Bongseong munyeo", name_original="鳳城文餘", period_id=p_joseon, definition="小品文と市井観察を収める朝鮮後期文集。"),
            dict(name_ja="朴趾源『許生伝』", name_en="Pak Jiwon, Heo Saeng jeon", name_original="許生傳", period_id=p_joseon, definition="商業と北学思想を寓話化した燕岩の漢文短編。"),
            dict(name_ja="『裵裨将伝』", name_en="Bae Bijang jeon", name_original="裵裨將傳", period_id=p_joseon, definition="済州を舞台に好色官吏を笑う朝鮮後期滑稽小説。"),
            dict(name_ja="『雍固執伝』", name_en="Ong Gojip jeon", name_original="雍固執傳", period_id=p_joseon, definition="頑固な富民像を通じ吝嗇と欲望を諷刺する古小説。"),

            # 3. 女性漢詩・宮中文学の細部
            dict(name_ja="許蘭雪軒『蘭雪軒集』", name_en="Heo Nanseolheon, Nanseolheon jip", name_original="蘭雪軒集", period_id=p_joseon, definition="薄命意識と仙界幻想を詠む朝鮮女性漢詩集。"),
            dict(name_ja="黄真伊の時調", name_en="Hwang Jini sijo", name_original="黃眞伊時調", period_id=p_joseon, definition="妓生詩人黄真伊に帰される恋愛と機知の時調群。"),
            dict(name_ja="李玉峰の漢詩", name_en="Yi Ok-bong poetry", name_original="李玉峰漢詩", period_id=p_joseon, definition="離別と女性主体の声で知られる朝鮮女性漢詩。"),
            dict(name_ja="『恨中録』", name_en="Hanjungnok", name_original="閑中錄", period_id=p_joseon, definition="思悼世子事件を記す恵慶宮洪氏の宮廷回想録。"),
            dict(name_ja="『癸丑日記』", name_en="Gyechuk ilgi", name_original="癸丑日記", period_id=p_joseon, definition="光海君期の宮廷政争を内側から描くハングル日記。"),
            dict(name_ja="『仁顕王后伝』", name_en="Queen Inhyeon jeon", name_original="仁顯王后傳", period_id=p_joseon, definition="廃妃と復位を描く宮廷系ハングル伝記小説。"),

            # 4. 植民地期モダニズム周縁
            dict(name_ja="『創造』同人誌", name_en="Changjo magazine", name_original="創造", period_id=p_modern, definition="金東仁らが始めた植民地期初期の近代文学同人誌。"),
            dict(name_ja="『廃墟』同人誌", name_en="Pyeheo magazine", name_original="廢墟", period_id=p_modern, definition="退廃的感性を掲げた一九二〇年代朝鮮文学同人誌。"),
            dict(name_ja="朴泰遠『小説家仇甫氏の一日』", name_en="Pak Taewon, A Day in the Life of Kubo the Novelist", name_original="小說家仇甫氏의 一日", period_id=p_modern, definition="京城散歩を意識流で追う一九三〇年代モダニズム小説。"),
            dict(name_ja="李孝石『蕎麦の花咲く頃』", name_en="Yi Hyoseok, When Buckwheat Flowers Bloom", name_original="메밀꽃 필 무렵", period_id=p_modern, definition="市と旅芸人をめぐる抒情的地方短編。"),
            dict(name_ja="李無影『第一課第一章』", name_en="Yi Muyeong, First Lesson, First Chapter", name_original="제1과 제1장", period_id=p_modern, definition="帰農と農村現実を描く植民地期農民小説。"),
            dict(name_ja="金裕貞『椿の花』", name_en="Kim Yujeong, Camellias", name_original="동백꽃", period_id=p_modern, definition="方言と滑稽で農村恋愛を描く植民地期短編。"),

            # 5. 北朝鮮・越境・在日周縁
            dict(name_ja="趙基天『白頭山』", name_en="Cho Ki-chon, Mount Paektu", name_original="백두산", period_id=p_km, definition="抗日神話を叙事詩化した北朝鮮建国期の長詩。"),
            dict(name_ja="韓雪野『大同江』", name_en="Han Sorya, Taedong River", name_original="대동강", period_id=p_km, definition="解放後北朝鮮の新社会像を描くプロレタリア長編。"),
            dict(name_ja="李箕永『故郷』", name_en="Yi Kiyong, Hometown", name_original="고향", period_id=p_modern, definition="小作農運動を描く植民地期プロレタリア長編。"),
            dict(name_ja="洪命熹『林巨正』", name_en="Hong Myong-hui, Im Kkeokjeong", name_original="林巨正", period_id=p_modern, definition="盗賊義賊を軸に民衆史を描く植民地期歴史長編。"),
            dict(name_ja="在日朝鮮人誌『ヂンダレ』", name_en="Jindalle magazine", name_original="ヂンダレ", period_id=p_km, definition="在日朝鮮人詩人の戦後同人誌と抒情詩運動。"),
            dict(name_ja="金石範『火山島』", name_en="Kim Sok-pom, The Volcano Island", name_original="火山島", period_id=p_km, definition="済州四・三事件を日本語で描く在日朝鮮人長編。"),
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
