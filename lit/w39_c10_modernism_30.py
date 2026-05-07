#!/usr/bin/env python3
"""Wave 39 cluster 10: add 30 ultra-niche lit_eu_modernism concepts."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_eu_modernism"
REGION = "西欧"
PERIOD_ID = 22

CONCEPTS = [
    # Cluster 1: 英語圏小雑誌・周縁作家
    ("ホープ・ミリーズ『パリ』", "Hope Mirrlees, Paris", "Paris", "latin", "一日都市を神話化する、注釈的断片で組まれた実験長詩。"),
    ("ドロシー・リチャードソン『巡礼』窓意識", "Dorothy Richardson, Pilgrimage", "Pilgrimage", "latin", "女性の日常知覚を連続内面で追う長篇連作の意識技法。"),
    ("ブライア『発展』", "Bryher, Development", "Development", "latin", "映画的記憶と少女期の感覚を接続する英語モダニズム小説。"),
    ("ジョン・ロドカー『アドリフト』", "John Rodker, Adolphe 1920", "Adolphe 1920", "latin", "ロンドン小出版社圏の断片的自我小説。"),
    ("ローラ・ライディング『十四A』", "Laura Riding, Fourteen A", "Fourteen A", "latin", "抽象語法で主体と詩の論理を詰める実験詩集。"),
    ("ユージン・ジョラス『遷移』誌", "Eugene Jolas, transition", "transition", "latin", "多言語実験と夢の言語を掲げたパリ発英語前衛誌。"),
    # Cluster 2: 仏語前衛の小運動
    ("フィリップ・スーポー『水族館』", "Philippe Soupault, Aquarium", "Aquarium", "latin", "自動記述以前の都市速度と比喩を集めた初期詩集。"),
    ("アルベール＝ビロー『SIC』誌", "Pierre Albert-Birot, SIC", "SIC", "latin", "詩・絵画・演劇を横断した仏前衛小雑誌。"),
    ("ポール・デルメ『ノール＝シュッド』", "Paul Dermée, Nord-Sud", "Nord-Sud", "latin", "キュビスム詩人を結集した短命のパリ前衛誌。"),
    ("リブモン＝デセーニュ『駝鳥』", "Ribemont-Dessaignes, L'Autruche", "L'Autruche", "latin", "ダダ的論理破壊を舞台化する不条理喜劇。"),
    ("イヴァン・ゴル『メトゥザレム』", "Yvan Goll, Methusalem", "Methusalem", "latin", "表現主義と仏前衛を混交する機械時代の戯曲。"),
    ("ロジェ・ヴィトラック『ヴィクトール』", "Roger Vitrac, Victor", "Victor ou les enfants au pouvoir", "latin", "家族劇を倒錯させる初期シュルレアリスム演劇。"),
    # Cluster 3: 独墺周縁モダニズム
    ("カール・アインシュタイン『ベビュカン』", "Carl Einstein, Bebuquin", "Bebuquin", "latin", "キュビスム的知覚で叙述を崩す独語実験小説。"),
    ("ミノナ『灰色の魔術』", "Mynona, Graue Magie", "Graue Magie", "latin", "哲学的奇想と風刺を混ぜるベルリン前衛短篇。"),
    ("アルフレート・デーブリン『王倫の三跳躍』", "Döblin, The Three Leaps of Wang Lun", "Die drei Sprünge des Wang-lun", "latin", "集団運動を多声的叙述で描く初期デーブリン長篇。"),
    ("エルゼ・ラスカー＝シューラー『ヘブライのバラード』", "Else Lasker-Schüler, Hebrew Ballads", "Hebräische Balladen", "latin", "仮面と聖書的声を交差させる表現主義詩集。"),
    ("アルフレート・クビン『裏面』", "Alfred Kubin, The Other Side", "Die andere Seite", "latin", "夢幻都市ペルレを舞台にする不安と崩壊の幻想小説。"),
    ("フランツ・ブライ『大動物寓話集』", "Franz Blei, Bestiarium literaricum", "Das große Bestiarium", "latin", "同時代作家を動物寓意で諷刺するウィーン文壇小品。"),
    # Cluster 4: 伊・イベリア前衛
    ("パラッツェスキ『ペレラの暗号』", "Palazzeschi, The Code of Perelà", "Il codice di Perelà", "latin", "煙の男をめぐる反英雄的未来派小説。"),
    ("アルデンゴ・ソッフィチ『BIF&ZF+18』", "Ardengo Soffici, BIF&ZF+18", "BIF&ZF+18", "latin", "活字実験と断片詩で構成された伊未来派詩集。"),
    ("アルベルト・サヴィニオ『両性具有者』", "Alberto Savinio, Hermaphrodito", "Hermaphrodito", "latin", "神話・自伝・戦争記憶を混ぜる形而上派散文。"),
    ("ラモン・ゴメス・デ・ラ・セルナのグレゲリーア", "Ramón Gómez de la Serna, greguería", "greguería", "latin", "隠喩と機知を極小散文へ圧縮するスペイン前衛形式。"),
    ("ギリェルモ・デ・トーレ『螺旋』", "Guillermo de Torre, Hélices", "Hélices", "latin", "ウルトライスモの機械美と活字感覚を示す詩集。"),
    ("マリオ・デ・サ＝カルネイロ『空の炎』", "Mário de Sá-Carneiro, Céu em fogo", "Céu em fogo", "latin", "分裂自我と人工美を濃縮するポルトガル短篇集。"),
    # Cluster 5: 北欧・中東欧の小系譜
    ("エディット・セーデルグラン『九月の竪琴』", "Edith Södergran, Septemberlyran", "Septemberlyran", "latin", "フィンランド・スウェーデン語圏の予言的自由詩集。"),
    ("ペール・ラーゲルクヴィスト『不安』", "Pär Lagerkvist, Ångest", "Ångest", "latin", "戦時の恐怖を硬質な自由詩にした北欧表現主義詩集。"),
    ("カレル・タイゲのポエティスム", "Karel Teige, Poetism", "poetismus", "latin", "生活遊戯と映画的感覚を掲げたチェコ前衛理論。"),
    ("ヴィーチェスラフ・ネズヴァル『エジソン』", "Vítězslav Nezval, Edison", "Edison", "latin", "発明家像を都市的電気神話へ変えるチェコ長詩。"),
    ("ヴィトカツィ『靴屋たち』", "Witkacy, The Shoemakers", "Szewcy", "latin", "革命と消費社会を怪物化するポーランド前衛戯曲。"),
    ("デボラ・フォーゲルのフォトモンタージュ散文", "Debora Vogel, photomontage prose", "akacje kwitną", "latin", "イディッシュ・ポーランド前衛の都市断片散文。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, definition in CONCEPTS:
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            after = db.find_concept(name_ja, REGION, PERIOD_ID)
            if before is None and after is not None:
                inserted += 1
    print(f"INSERTED={inserted}")


if __name__ == "__main__":
    main()
