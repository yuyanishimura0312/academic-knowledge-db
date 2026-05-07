"""Wave 38: lit_se_asia_korea (id=17) +30 compact niche concepts."""
from __future__ import annotations

from lit_db_helper import LitDB, LitDBError

SUBFIELD_CODE = "lit_se_asia_korea"
REGION = "グローバルサウス"


def pid(db: LitDB, name_ja: str) -> int:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region='グローバルサウス'",
        (name_ja,),
    ).fetchone()
    if not row:
        raise RuntimeError(f"period not found: {name_ja}")
    return row["id"]


def main() -> None:
    with LitDB() as db:
        p_kr = pid(db, "韓国現代期")
        p_kr_mod = pid(db, "韓国近現代文学期")
        p_vn = pid(db, "ベトナム現代期")
        p_th = pid(db, "タイ近現代文学期")
        p_sea = pid(db, "東南アジア現代期")
        p_ph = pid(db, "フィリピン近現代文学期")
        p_im = pid(db, "インドネシア・マレーシア近現代期")

        concepts = [
            # 1: 韓国現代女性
            dict(name_ja="韓江『菜食主義者』暴力読解", name_en="Han Kang, The Vegetarian", name_original="채식주의자", period_id=p_kr, definition="身体拒否を通じ家父長制暴力と非人間化を描く韓国現代小説。"),
            dict(name_ja="韓江『少年が来る』光州記憶", name_en="Han Kang, Human Acts", name_original="소년이 온다", period_id=p_kr, definition="光州事件の死者と生者の声を連ねる証言的ポリフォニー小説。"),
            dict(name_ja="ペ・スア『朗読する女たち』", name_en="Bae Suah, Recitation", name_original="철수", period_id=p_kr, definition="翻訳・旅・声のずれで語りの主体を揺らす実験的散文。"),
            dict(name_ja="ファン・ジョンウン『百の影』", name_en="Hwang Jung-eun, One Hundred Shadows", name_original="백의 그림자", period_id=p_kr, definition="再開発地区の労働者と影をめぐる静かな寓話的都市小説。"),
            dict(name_ja="趙南柱『82年生まれ、キム・ジヨン』フェミニズム", name_en="Cho Nam-joo, Kim Jiyoung, Born 1982", name_original="82년생 김지영", period_id=p_kr, definition="統計的語りで日常的性差別を可視化した韓国フェミニズム小説。"),
            dict(name_ja="金惠順『死の自伝』", name_en="Kim Hyesoon, Autobiography of Death", name_original="죽음의 자서전", period_id=p_kr_mod, definition="死者の声と女性身体を重ねる断章的フェミニズム詩集。"),

            # 2: 韓国詩・現代詩
            dict(name_ja="金洙暎『草』", name_en="Kim Soo-young, Pul", name_original="풀", period_id=p_kr_mod, definition="草の揺れに民衆的抵抗と自由の感覚を託す現代韓国詩。"),
            dict(name_ja="金春洙『花』", name_en="Kim Chun-su, Flower", name_original="꽃", period_id=p_kr_mod, definition="名づけと存在の関係を凝縮した韓国存在論的抒情詩。"),
            dict(name_ja="徐廷柱『驢馬』", name_en="Suh Jung-ju, Donkey", name_original="나귀", period_id=p_kr_mod, definition="土俗的イメージと官能的言語で生命力をうたう詩。"),
            dict(name_ja="朴在森『古い歌』", name_en="Park Jaesam, Old Song", name_original="오래된 노래", period_id=p_kr_mod, definition="南海の情景と民謡的リズムで喪失を歌う叙情詩。"),
            dict(name_ja="高銀『萬人譜』", name_en="Ko Un, Maninbo", name_original="만인보", period_id=p_kr_mod, definition="無数の人物像で韓国近現代史を編む大規模連作詩。"),
            dict(name_ja="黄東奎『風葬』", name_en="Hwang Tong-gyu, Wind Burial", name_original="풍장", period_id=p_kr_mod, definition="死と風のイメージで存在の流動性を探る現代詩連作。"),

            # 3: ベトナム現代
            dict(name_ja="ズオン・トゥー・フオン『盲目の楽園』家族政治", name_en="Duong Thu Huong, Paradise of the Blind", name_original="Những thiên đường mù", period_id=p_vn, definition="革命後社会の家族倫理と党派的抑圧を女性視点で描く長編。"),
            dict(name_ja="マー・ヴァン・カン『遠い豊かな土地』", name_en="Ma Van Khang, A Bountiful Distant Land", period_id=p_vn, definition="山岳辺境の開発と民族関係を描くドイモイ期ベトナム小説。"),
            dict(name_ja="レ・ミン・クエ『独身男のいない町』", name_en="Le Minh Khue, The Town with No Bachelors", period_id=p_vn, definition="戦後の地方社会と女性の日常を皮肉に描く短編小説。"),
            dict(name_ja="ファム・ティ・ホアイ『水晶の使者』", name_en="Pham Thi Hoai, The Crystal Messenger", name_original="Thiên sứ", period_id=p_vn, definition="寓話的語りで社会主義的規範と家族制度を風刺する小説。"),
            dict(name_ja="グエン・クアン・ティエウ『不眠』", name_en="Nguyen Quang Thieu, Insomnia", period_id=p_vn, definition="農村記憶と戦後不安を夢幻的イメージで編む現代詩。"),
            dict(name_ja="ファン・ニエン・ハオの亡命詩", name_en="Phan Nhien Hao, poetry", period_id=p_vn, definition="亡命経験と都市的孤独を切断的イメージで書くベトナム系詩。"),

            # 4: タイ・ラオス現代
            dict(name_ja="ピーラ・スダム『モンスーンの国』", name_en="Pira Sudham, Monsoon Country", period_id=p_th, definition="イサーン農村と移民経験を英語で描くタイ現代小説。"),
            dict(name_ja="サネー・サオワポン『毒』", name_en="Saneh Sangsuk, Venom", period_id=p_th, definition="少年と蛇の対峙に暴力と生存本能を凝縮した短編小説。"),
            dict(name_ja="ウィーラポーン『川面の記憶』", name_en="Veeraporn Nitiprapha, River Reflections", period_id=p_th, definition="家族史と川の記憶を重ねるタイ現代叙事小説。"),
            dict(name_ja="アウティン・ブニャヴォン『母の最愛のもの』", name_en="Outhine Bounyavong, Mother's Beloved", period_id=p_sea, definition="家族と村落倫理を簡潔な語りで描くラオス近現代短編。"),
            dict(name_ja="ブライアン・タオ・ウォーラのラオ系米国詩", name_en="Bryan Thao Worra, Lao American poetry", period_id=p_sea, definition="難民記憶と怪奇的想像力を混交するラオ系アメリカ詩。"),
            dict(name_ja="カム・ウアン・ラッサパイの現代ラオス文学", name_en="Kham Ouane Ratsapay", period_id=p_sea, definition="社会変動期ラオスの生活感覚を描く現代散文の一系譜。"),

            # 5: 比・尼・馬来現代
            dict(name_ja="ルアルハティ・バウティスタ『デカダ70』", name_en="Lualhati Bautista, Dekada '70", period_id=p_ph, definition="戒厳令下フィリピンの家族と女性の政治的覚醒を描く長編。"),
            dict(name_ja="エリック・ガマリンダ『記憶の帝国』", name_en="Eric Gamalinda, Empire of Memory", period_id=p_ph, definition="独裁後の記憶と歴史改作をめぐるフィリピン英語小説。"),
            dict(name_ja="アユ・ウタミ『サマン』ジェンダー読解", name_en="Ayu Utami, Saman", period_id=p_im, definition="性・宗教・政治を交差させたポスト・スハルト期小説。"),
            dict(name_ja="エカ・クルニアワン『美は傷』暴力史", name_en="Eka Kurniawan, Beauty Is a Wound", name_original="Cantik Itu Luka", period_id=p_im, definition="幽霊的語りで植民地以後の暴力史を描くインドネシア長編。"),
            dict(name_ja="タシュ・オー『ハーモニー・シルク工場』", name_en="Tash Aw, The Harmony Silk Factory", period_id=p_im, definition="複数証言で植民地期マラヤの商人像を再構成する小説。"),
            dict(name_ja="タン・トゥアンエン『夕霧花園』", name_en="Tan Twan Eng, The Garden of Evening Mists", period_id=p_im, definition="戦争記憶と庭園美学を絡めるマレーシア英語小説。"),
        ]

        inserted = 0
        for entry in concepts:
            entry = dict(entry)
            entry["subfield_code"] = SUBFIELD_CODE
            entry["region"] = REGION
            try:
                db.insert_concept(**entry)
                inserted += 1
            except LitDBError as exc:
                print(f"[error] {entry['name_ja']}: {exc}")
        print(f"inserted_or_existing={inserted}")


if __name__ == "__main__":
    main()
