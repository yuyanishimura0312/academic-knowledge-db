#!/usr/bin/env python3
"""Wave 44: add 30 ultra-niche concepts to lit_russia_slavic."""

from lit_db_helper import LitDB

SUBFIELD = "lit_russia_slavic"
REGION = "東欧・ロシア"

CONCEPTS = [
    # Cluster 1: East Slavic manuscript and sermon microforms
    ("『スヴャトスラフ選集1076年』教訓配列", "Sviatoslav Izbornik 1076 didactic ordering", "引用教訓を王侯倫理の読書順へ編むキエフ期選集構成。"),
    ("ノヴゴロド巡礼札文の短祈願", "Novgorod pilgrim-note brief prayers", "巡礼札や奉納文に残る短い祈願句の口語的信心表現。"),
    ("『ムーロムのコンスタンチン伝』改宗叙事", "Constantine of Murom conversion tale", "地方聖者伝で都市改宗を奇跡と王権の物語へ組む語り。"),
    ("『トヴェリのミハイル伝』殉教政治語り", "Mikhail of Tver political martyrdom", "公権力争いを受難聖者伝の語彙で正当化する中世叙述。"),
    ("プロローグ短伝の暦日圧縮", "Prologue short-life calendrical compression", "聖者伝を一日朗読用に縮約する暦書的ミニアチュール。"),
    ("『ステペンナヤ・クニーガ』系譜梯子", "Book of Degrees genealogical ladder", "王朝史を聖性の階梯として配列するモスクワ国家編纂。"),

    # Cluster 2: eighteenth-century print, theatre, and provincial genres
    ("スマロコフ悲劇の韻律規律", "Sumarokov tragedy metrical discipline", "仏古典劇法をロシア語六脚詩へ合わせる宮廷悲劇の規則。"),
    ("ノヴィコフ諷刺雑誌『トルテニ』", "Novikov Truten satirical journal", "怠惰な貴族像を寓話的対話で刺す啓蒙期の風刺誌面。"),
    ("フォンヴィージン喜劇の家庭教師風刺", "Fonvizin tutor satire", "家庭教育の仏語かぶれを笑劇化する貴族喜劇の批判装置。"),
    ("デルジャーヴィン頌詩の会話化", "Derzhavin conversational ode", "荘重な頌詩へ私的発話と官僚日常を混ぜる詩的転換。"),
    ("ヘラスコフ『ロシアーダ』帝国叙事", "Kheraskov Rossiada imperial epic", "カザン征服を古典叙事詩型で帝国起源譚へ整える長詩。"),
    ("クニャジニン共和悲劇の検閲痕", "Kniazhnin republican tragedy censorship", "共和主題の悲劇が発禁で政治的読解を帯びた劇作例。"),

    # Cluster 3: Russian emigre periodicals and Paris-Berlin niches
    ("『ソヴレメンヌィエ・ザピスキ』連載亡命圏", "Sovremennye zapiski serial emigre sphere", "パリ亡命誌が長編連載と政治論を同居させた編集空間。"),
    ("『チスラ』誌のパリ若手散文", "Chisla Paris young prose", "第一亡命世代の後続が断片心理と都市感覚を競った小雑誌。"),
    ("ベルリン『ナカヌネ』同伴者文学欄", "Berlin Nakanune fellow-traveler pages", "帰国志向の亡命新聞がソ連同伴者文学を紹介した欄。"),
    ("ゲオルギー・イワノフ亡命ニヒリズム", "Georgy Ivanov emigre nihilism", "亡命生活の空虚を冷笑的短詩へ凝縮するパリ詩壇の声。"),
    ("ガイト・ガズダーノフ夜間タクシー散文", "Gaito Gazdanov night-taxi prose", "運転手経験を夢幻的記憶小説へ転じる亡命都市散文。"),
    ("『ノーヴィ・ジュルナル』戦後継承", "Novyi zhurnal postwar continuity", "亡命ロシア文学の戦後発表媒体として世代を接続した雑誌。"),

    # Cluster 4: Soviet institutional and underground micro-scenes
    ("ラップ機関紙『ナ・リテラトゥルノム・ポストゥ』", "RAPP Na literaturnom postu", "党派批評で同伴者作家を攻撃したラップの主力誌面。"),
    ("リトフロント宣言の生産主義", "Litfront declaration productivism", "文学を工場的組織と社会的注文へ従わせる1930年前後の綱領。"),
    ("作家同盟第一回大会の模範作者像", "First Writers Congress model author", "社会主義リアリズムを作者倫理として制度化した大会言説。"),
    ("ズヴェズダ・レニングラード批判", "Zvezda Leningrad campaign", "アフマートヴァらを標的化した戦後文化統制の誌面批判。"),
    ("タルトゥ地下記号論セミナー", "Tartu underground semiotics seminar", "公式学術と非公式読解が交差した文化記号論の研究会圏。"),
    ("チェルヌホフ散文の汚れた日常", "Chernuha prose dirty everyday", "後期ソ連の暴力と貧困を露悪的現実感で描く散文傾向。"),

    # Cluster 5: West and South Slavic ultra-niche modernisms
    ("ポーランド『ズヴロトニツァ』未来派紙面", "Zwrotnica Futurist pages", "機械都市詩学を編集実験で広めたクラクフ前衛誌。"),
    ("ヴィトカツィ純粋形式劇", "Witkacy pure form drama", "心理写実を拒み異様な構成で形而上的不安を出す劇理論。"),
    ("チェコ『レド』誌ポエティスム舞台", "ReD Poetism stage", "デヴィエチル周辺が詩・映画・舞台を横断した前衛誌。"),
    ("セルビア『プテヴィ』誌表現主義圏", "Putevi Serbian expressionist circle", "戦後ベオグラードで表現主義と欧州前衛を媒介した小雑誌。"),
    ("ブルガリア『ヴェズニ』象徴派誌面", "Vezni Bulgarian Symbolist pages", "象徴派詩と翻訳を束ねたソフィアのモダニズム誌。"),
    ("クロアチア『ゼニット』バルバロゲニウス", "Zenit Barbarogenius", "バルカン的野性を欧州文明批判へ転じたゼニティズム概念。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    assert len(CONCEPTS) == 5 * 6
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute(
                "SELECT name_ja FROM concepts WHERE subfield_id = 18"
            )
        }
        for name_ja, name_en, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            if name_ja in existing:
                skipped += 1
                print(f"[skip-name] {name_ja}")
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=None,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            inserted += 1
    print(f"Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
