#!/usr/bin/env python3
"""Wave 43: add 30 ultra-niche concepts to lit_cn_classical."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_cn_classical"
REGION = "東アジア"

P_PREQIN = 1
P_HAN = 2
P_WEIJIN = 3
P_TANG = 4
P_SONG = 52
P_MING = 54
P_QING = 55

CONCEPTS = [
    # 1. 詩経注疏・小学
    ("毛詩譜鄭氏地域説", "Zheng's regional Mao shi pu", "毛詩譜", P_HAN, "鄭玄が国風を地域秩序で読む譜説。詩経地理解釈の小系。"),
    ("孔疏風雅正変説", "Kong Yingda orthodox and variant airs", "風雅正變説", P_TANG, "毛詩正義に見える正風変風・正雅変雅の体系化。"),
    ("朱熹詩集伝淫詩説", "Zhu Xi licentious-poem reading", "淫詩説", P_SONG, "朱熹が一部国風を男女私情として読む小序批判の焦点。"),
    ("詩経叶韻説", "Shijing xieyun rhyme theory", "叶韻説", P_SONG, "古音差を読替で整える詩経押韻説。宋代音韻解釈の技法。"),
    ("姚際恒小序辨偽", "Yao Jiheng Xiaoxu critique", "小序辨偽", P_QING, "詩経小序の後出性を疑う清代辨偽。経学的読法を転換する。"),
    ("崔述詩経世本考", "Cui Shu Shijing chronology critique", "詩經世本考", P_QING, "崔述が詩篇の世次を再考する考証。毛序年代観を揺らす。"),
    # 2. 楚辞・漢賦の微細形式
    ("九歌東皇太一祭祀読法", "Donghuang Taiyi ritual reading", "東皇太一", P_PREQIN, "九歌首篇を楚地祭祀歌として読む解釈。神名と儀礼を結ぶ。"),
    ("招魂巫祝問答式", "Zhaohun shamanic dialogue form", "招魂問答式", P_PREQIN, "招魂に見える呼魂と応答の構成。楚辞の儀礼発話を示す。"),
    ("大招楚辞補篇", "Dazhao as Chuci supplement", "大招", P_HAN, "楚辞系統に収められた招魂類篇。饗宴描写で魂を誘う。"),
    ("枚乗「七発」問答賦", "Mei Sheng Qifa dialogue fu", "七發問答賦", P_HAN, "客主問答で病を覚ます七段構成の賦。七体形式の祖型。"),
    ("子虚上林虚構使者", "fictional envoys in Zixu Shanglin", "子虚烏有先生", P_HAN, "子虚・烏有先生らを置く賦の虚構対話装置。"),
    ("揚雄「甘泉賦」郊祀空間", "Yang Xiong Ganquan ritual space", "甘泉賦", P_HAN, "甘泉宮郊祀を宇宙的巡遊として描く揚雄賦の空間構成。"),
    # 3. 六朝文体・選本
    ("宮体詩艶情題詠", "palace-style erotic topical verse", "宮體艶情詩", P_WEIJIN, "梁陳宮廷で発達した女性身体・閨房題詠の詩風。"),
    ("竟陵王西邸唱和", "Prince Jingling Western Lodge exchange", "西邸唱和", P_WEIJIN, "竟陵王蕭子良の西邸文人圏で行われた唱和詩作。"),
    ("文選賦類三分法", "Wenxuan tripartite fu taxonomy", "文選賦類三分", P_WEIJIN, "文選が賦を京都・郊祀など細目に分ける選録分類法。"),
    ("玉台新詠閨閣選詩", "Yutai xinyong boudoir selection", "閨閣選詩", P_WEIJIN, "玉台新詠が女性・恋情題材を集中的に収める選詩方針。"),
    ("世説新語品藻語彙", "Shishuo evaluative vocabulary", "品藻語彙", P_WEIJIN, "人物評語で名士の才性を測る世説新語の批評語彙。"),
    ("劉勰隠秀篇含蓄論", "Liu Xie yin-xiu implicitness", "隱秀篇", P_WEIJIN, "文心雕龍隠秀篇の余意重視。言外の含蓄を論じる。"),
    # 4. 唐宋詩詞の制度・技法
    ("韓孟聯句体", "Han-Meng linked-verse style", "韓孟聯句", P_TANG, "韓愈・孟郊圏の連句実験。奇険語と合作性を兼ねる。"),
    ("元和新楽府小序", "Yuanhe new yuefu prefaces", "新樂府小序", P_TANG, "新楽府各篇に添えた諷諭目的の小序。詩題と政治性を明示する。"),
    ("花間集詞牌序列", "Huajian ji tune-title ordering", "花間集詞牌序列", P_TANG, "花間集で詞牌ごとに作品を配する配列。詞集編纂の早期形式。"),
    ("唐宋題壁詩慣行", "Tang-Song wall-inscribed poetry", "題壁詩", P_TANG, "寺壁・駅亭などに詩を書き残す実践。移動と公開読者を結ぶ。"),
    ("清真詞犯調運用", "Qingzhen ci fandiao technique", "犯調", P_SONG, "周邦彦詞に見える複数宮調を交差させる楽律技法。"),
    ("夢窗詞密麗用事", "Mengchuang dense allusive diction", "密麗用事", P_SONG, "呉文英詞の濃密な典故配置。晦渋で装飾的な詞風を作る。"),
    # 5. 明清出版・評点・文体
    ("八股文破題", "baguwen opening couplet", "破題", P_MING, "八股文冒頭で経義を二句に割り出す題解部。制義文の入口。"),
    ("時文評選本", "selected examination-essay criticism", "時文評選本", P_MING, "科挙時文を選び評語を付す刊本。受験文体の規範を流通させる。"),
    ("弋陽腔伝奇改編", "Yiyangqiang chuanqi adaptation", "弋陽腔改編", P_MING, "弋陽腔上演へ向け伝奇本文を改める地方劇化の実践。"),
    ("庚辰本脂硯斎重評", "Gengchen Zhi re-commentary", "庚辰本脂評", P_QING, "紅楼夢庚辰本に残る脂硯斎系重評。初期本文校勘の要点。"),
    ("但明倫聊斎評点", "Dan Minglun Liaozhai commentary", "但明倫評點", P_QING, "但明倫が聊斎志異に施した評点。志怪を古文技法で読む。"),
    ("評点眉批夾批形式", "marginal and interlinear pingdian", "眉批夾批", P_MING, "小説・戯曲評点で欄外批と行間批を併用する読書形式。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, (name_ja, len(definition))
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="kanji",
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
    print(f"inserted={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
