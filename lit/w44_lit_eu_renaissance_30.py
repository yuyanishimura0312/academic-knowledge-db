#!/usr/bin/env python3
"""Wave 44: 30 ultra-niche European Renaissance concepts, 5 clusters x 6."""

from lit_db_helper import LitDB

SUBFIELD = "lit_eu_renaissance"
REGION = "西欧"

P_IT = 144
P_IB = 145
P_FR = 146
P_EN = 147
P_NO = 148

CONCEPTS = [
    # Italian academies, print, and minor stage forms
    ("アカデミア・デッラ・クルスカの『語彙集』", "Accademia della Crusca Vocabolario", "Vocabolario degli Accademici della Crusca", P_IT, "フィレンツェ語を権威化した初期イタリア語辞書。"),
    ("イントロナーティ学院の喜劇", "Intronati academy comedy", "commedie degli Intronati", P_IT, "シエナ学院文化で育った仮装と恋愛錯誤の俗語劇。"),
    ("イントロナーティ『欺かれた者たち』", "Gl'Ingannati", "Gl'Ingannati", P_IT, "女装と双子錯誤を組むシエナ学院喜劇。"),
    ("カルダーノ『自伝』", "Cardano, The Book of My Life", "De propria vita", P_IT, "占星術師が失敗と身体を記すラテン自己記述。"),
    ("ドーニ『地獄』", "Doni, The Hell", "I mondi inferni", P_IT, "夢幻旅行で同時代社会を風刺する奇想散文。"),
    ("パラヴィチーノ以前の書簡小説断章", "pre-Pallavicino epistolary fiction fragments", "frammenti epistolari narrativi", P_IT, "書簡の連鎖で恋愛事件を作る散文実験。"),

    # French salons-before-salons, polemic, and print miscellanies
    ("リヨン女性詩人のデヴィーズ詩", "Lyon women poets' devise verse", "devises lyonnaises", P_FR, "標語と図像を恋愛詩へ結ぶリヨン派小形式。"),
    ("セバスチャン・カステリオン聖書序文", "Castellio Bible prefaces", "prefaces bibliques", P_FR, "寛容論を翻訳序文に潜ませる改革派散文。"),
    ("エチエンヌ・ジョデル祝祭入場詩", "Jodelle entry festival verse", "vers d'entree", P_FR, "王侯入市式の寓意装飾を担う機会詩。"),
    ("タブロー『機知の大島』", "Tabourot, Bigarrures", "Les Bigarrures", P_FR, "駄洒落・判じ物・言葉遊びを集めた雑録。"),
    ("ビュデ『アッセとその部分』", "Bude, De asse", "De asse et partibus eius", P_FR, "貨幣注釈から古典学の精密読解を示す人文主義書。"),
    ("ラ・ヌー『政治軍事談義』", "La Noue, Political and Military Discourses", "Discours politiques et militaires", P_FR, "内戦経験を格言的散文で整理するユグノー回想。"),

    # Iberian chapbooks, border narratives, and stage microforms
    ("カルタス・デ・レラシオン文体", "cartas de relacion style", "cartas de relacion", P_IB, "征服報告を権威づける一人称行政散文。"),
    ("ゴンサロ・フェルナンデス・デ・オビエド叙述", "Oviedo colonial chronicle prose", "Historia general y natural", P_IB, "博物誌と体験談を混ぜる初期植民地年代記。"),
    ("フロリスタン型騎士道続編", "Floristan chivalric sequel type", "Floristan", P_IB, "既成騎士道物語を血統連鎖で延長する続編型。"),
    ("コロキオス・デ・パラティノとピンシアーノ", "Coloquios de Palatino y Pinciano", "Coloquios de Palatino y Pinciano", P_IB, "学生放浪を対話体で滑稽化する大学小説。"),
    ("ロマンセ・モリスコ小冊子", "Moorish romance chapbooks", "romances moriscos sueltos", P_IB, "グラナダ異国趣味を歌う廉価印刷ロマンセ。"),
    ("アウト・サクラメンタルのロア", "loa in autos sacramentales", "loa sacramental", P_IB, "聖体劇の前口上として観客を整える短詩劇。"),

    # English manuscript, pamphlet, and theatre micro-archives
    ("アルバム・アミコルム英詩記入", "English verse in alba amicorum", "album amicorum verse", P_EN, "友人帳に署名と短詩を残す旅行者の社交文学。"),
    ("チープサイド・ブロードサイド・バラッド", "Cheapside broadside ballads", "broadside ballads", P_EN, "街頭販売の一枚刷りで時事と恋歌を流通させた歌。"),
    ("セネカ風合唱幕間", "Senecan choric interlude", "Senecan chorus", P_EN, "復讐悲劇で道徳解釈を挟む合唱形式。"),
    ("レヴェルズ局検閲台帳", "Revels Office licensing records", "Revels Office books", P_EN, "宮廷上演と検閲の痕跡を残す劇務記録。"),
    ("大学才人のナイトピース散文", "University Wits night-piece prose", "night-piece prose", P_EN, "夜の都市を機知と悪徳で描く小冊子散文。"),
    ("タヴァーン・ジグの印刷歌詞", "printed tavern jig lyrics", "printed jigs", P_EN, "終演後の踊り歌が小冊子で残った劇場周辺歌謡。"),

    # Northern and central European humanist margins
    ("レーデライケルの王侯入市リフレイン", "Rederijker entry refrains", "intrede-refreinen", P_NO, "都市祝祭で提示された韻文標語と寓意詩。"),
    ("フリシュリン『ユリウス・レディヴィヴス』", "Frischlin, Julius Redivivus", "Julius Redivivus", P_NO, "古代作家を復活させ当世学芸を裁く学校劇。"),
    ("オピッツ以前のシレジア祝婚詩", "pre-Opitz Silesian wedding poetry", "epithalamia Silesiaca", P_NO, "ラテンと独語が交じる地方名士の婚礼詩。"),
    ("ゲオルク・ロレマン聖書エピグラム", "Georg Rollenhagen biblical epigrams", "biblische Epigramme", P_NO, "聖書教訓を短詩と寓意で圧縮する学校文学。"),
    ("アムステルダム商人の機会詩冊子", "Amsterdam merchant occasional verse", "gelegenheidsgedichten", P_NO, "商人家の婚礼・葬儀を飾る蘭語小冊子詩。"),
    ("ボヘミア兄弟団の賛歌序文", "Unity of Brethren hymnbook prefaces", "prefaces to hymnals", P_NO, "共同体の歌唱規律を示すチェコ・独語宗教散文。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            if db.find_concept(name_ja, REGION, period_id) is not None:
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="latin",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
