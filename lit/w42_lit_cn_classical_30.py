#!/usr/bin/env python3
"""Wave 42: add 30 ultra-niche concepts to lit_cn_classical."""

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
    # 1. 詩経・経学の微細伝承
    ("魯詩申培授受", "Shen Pei transmission of Lu Poetry", "魯詩申培授受", P_HAN, "申培を祖とする魯詩の師承系譜。今文詩学の伝授単位。"),
    ("齊詩轅固生傳", "Yuan Gusheng Qi Poetry line", "齊詩轅固生傳", P_HAN, "轅固生に帰される斉詩伝承。漢初詩説の政治的読法を示す。"),
    ("韓詩外傳詩義", "Han shi waizhuan poem exegesis", "韓詩外傳詩義", P_HAN, "韓詩外伝で詩句を説話に結ぶ解釈法。経義の物語化。"),
    ("毛詩鄭箋箋體", "Zheng Xuan jian gloss form", "毛詩鄭箋箋體", P_HAN, "鄭玄箋に特有の補注形式。伝文を押し広げる注釈文体。"),
    ("陸德明『毛詩音義』", "Lu Deming Maoshi yinyi", "毛詩音義", P_TANG, "経典釈文所収の毛詩音注。詩経読音と異文を保存する。"),
    ("詩緯含神霧", "Shiwei Hanshenwu", "詩緯含神霧", P_HAN, "詩経を讖緯的に読む緯書。詩義と瑞祥思想を結びつける。"),
    # 2. 楚辞・漢賦の細部
    ("東方朔「七諫」", "Dongfang Shuo Qijian", "七諫", P_HAN, "楚辞遠遊系の諷諫連作。屈原像を漢代に再演する。"),
    ("劉向「九歎」", "Liu Xiang Jiutan", "九歎", P_HAN, "劉向の楚辞補作。屈原哀怨の語彙を漢代宮廷で継ぐ。"),
    ("王褒「九懷」", "Wang Bao Jiuhuai", "九懷", P_HAN, "王褒による楚辞系連章。招隠と憂世の語りを重ねる。"),
    ("揚雄「反離騷」", "Yang Xiong Fan Lisao", "反離騷", P_HAN, "離騒を反転批評する揚雄の辞賦。屈原評価を揺さぶる。"),
    ("班婕妤「自悼賦」", "Ban Jieyu Zidao fu", "自悼賦", P_HAN, "班婕妤の失寵哀悼賦。宮怨文学の早期女性声を示す。"),
    ("張衡「思玄賦」", "Zhang Heng Sixuan fu", "思玄賦", P_HAN, "宇宙遊行で玄理を探る大賦。天文想像と自省を結ぶ。"),
    # 3. 六朝文体・声律・注釈
    ("永明声律沈約説", "Shen Yue Yongming prosody", "永明聲律沈約説", P_WEIJIN, "沈約に帰される四声調整論。近体詩成立前夜の声律意識。"),
    ("王融竟陵八友詩", "Wang Rong Jingling poems", "王融竟陵八友詩", P_WEIJIN, "竟陵八友圏の王融詩。斉梁新体詩の社交的実作層。"),
    ("謝朓新体詩律化", "Xie Tiao regulated new style", "謝朓新體詩律化", P_WEIJIN, "謝朓詩に見る対偶と声律の精密化。唐律詩への前段階。"),
    ("丘遲「與陳伯之書」", "Qiu Chi letter to Chen Bozhi", "與陳伯之書", P_WEIJIN, "帰順勧告を抒情化した駢文書簡。六朝文の説得技法を示す。"),
    ("任昉表奏筆體", "Ren Fang memorial prose style", "任昉表奏筆體", P_WEIJIN, "任昉の表奏文に見える典故密度と四六調。梁代公文美文の型。"),
    ("劉孝標『世説新語注』", "Liu Xiaobiao Shishuo notes", "世説新語注", P_WEIJIN, "世説新語の人名・逸話を増補する注。清談世界の資料庫。"),
    # 4. 唐宋の制度文芸・詞楽
    ("唐代試帖詩", "Tang examination regulated poem", "試帖詩", P_TANG, "科挙課題として作る定型詩。官僚選抜と詩律訓練を結ぶ。"),
    ("唐人送窮文系譜", "Tang send-poverty prose lineage", "送窮文", P_TANG, "貧窮を擬人化して送る戯文。韓愈以後の寓意散文の小系。"),
    ("敦煌願文定型", "Dunhuang vow text formulae", "願文", P_TANG, "敦煌写本に多い願文の定型句。祈願儀礼と文章作法の接点。"),
    ("宋代四六啓", "Song parallel qi letters", "四六啓", P_SONG, "宋代に発達した四六調の啓文。社交書簡を美文化する文体。"),
    ("南宋江湖集刻本", "Southern Song Jianghu ji editions", "江湖集刻本", P_SONG, "江湖詩人を収めた刊本群。書坊出版と詩派形成を示す。"),
    ("宋詞自度曲", "self-composed Song ci tunes", "自度曲", P_SONG, "詞人が新たに作る曲調名。詞楽創作と個人様式を示す。"),
    # 5. 明清小説版本・評点
    ("崇禎本『金瓶梅』", "Chongzhen Jin Ping Mei edition", "崇禎本金瓶梅", P_MING, "繍像評点を備えた金瓶梅版本。詞話本と並ぶ本文系統。"),
    ("詞話本『金瓶梅』", "Cihua Jin Ping Mei edition", "詞話本金瓶梅", P_MING, "金瓶梅最古層の詞話系版本。講唱的章回語りを残す。"),
    ("李卓吾評『忠義水滸全書』", "Li Zhuowu Shuihu ping edition", "李卓吾評忠義水滸全書", P_MING, "李卓吾名義の水滸評本。百回本流通と評点読法を結ぶ。"),
    ("秦可卿淫喪脂評", "Zhi comment on Qin Keqing funeral", "秦可卿淫喪脂評", P_QING, "紅楼夢十三回をめぐる脂評。削除本文と倫理批評の焦点。"),
    ("程甲本『紅樓夢』", "Chengjia Hongloumeng edition", "程甲本紅樓夢", P_QING, "1791年刊の百二十回紅楼夢。活字刊本流通の起点。"),
    ("程乙本『紅樓夢』", "Chengyi Hongloumeng edition", "程乙本紅樓夢", P_QING, "1792年刊の改訂紅楼夢。程甲本との差異が校勘対象となる。"),
]


def main() -> None:
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, (name_ja, len(definition))
            cid = db.insert_concept(
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
            if cid:
                inserted += 1
            else:
                skipped += 1
    print(f"inserted_or_existing={inserted} skipped={skipped}")


if __name__ == "__main__":
    main()
