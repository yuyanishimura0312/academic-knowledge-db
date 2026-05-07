#!/usr/bin/env python3
"""Wave 37: lit_diaspora (subfield_id=20) — 30 niche concepts, 5 clusters x 6."""
import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SUBFIELD = 20
PERIOD = 274  # ポストコロニアル理論拡張期 (横断)
REGION = "横断"

CONCEPTS = [
    # 1: 黒人ディアスポラ
    ("トニ・モリスン『ビラヴド』詳論", "Toni Morrison: Beloved (detailed)",
     "1987年作。逃亡奴隷母セサが殺した娘の幽霊と再会する記憶と母性の小説。"),
    ("トニ・モリスン『ソロモンの歌』", "Toni Morrison: Song of Solomon",
     "1977年。黒人男性ミルクマンの飛翔伝承を辿る祖先探求の物語。"),
    ("エドウィージ・ダンティカ『クリック？クラック！』", "Edwidge Danticat: Krik? Krak!",
     "1995年短篇集。ハイチ女性たちの口承伝統と移民経験を交差させる。"),
    ("ジャマイカ・キンケイド『アニー・ジョン』詳論", "Jamaica Kincaid: Annie John",
     "1985年。アンティグアの少女の母娘葛藤と植民地教育からの離脱。"),
    ("カリル・フィリップス『川を渡る』詳論", "Caryl Phillips: Crossing the River",
     "1993年。アフリカ父祖の声で語る奴隷貿易250年の四つの物語。"),
    ("ポール・マーシャル『未亡人への賛歌』", "Paule Marshall: Praisesong for the Widow",
     "1983年。中年黒人女性がカリブ巡礼で祖先のアフリカ的記憶を回復する。"),
    # 2: アジア系米加
    ("マキシン・ホン・キングストン『女武者』詳論", "Maxine Hong Kingston: Woman Warrior",
     "1976年。中国系米国少女の記憶と神話を融合させた回想録的小説。"),
    ("エイミー・タン『ジョイ・ラック・クラブ』詳論", "Amy Tan: Joy Luck Club",
     "1989年。中国系移民母娘四組の麻雀会を通した世代間記憶の語り。"),
    ("ハ・ジン『待ち暮らし』", "Ha Jin: Waiting",
     "1999年。文革期中国の医師の18年に及ぶ離婚待機を描く全米図書賞作。"),
    ("チャンネ・リー『ネイティブ・スピーカー』詳論", "Chang-rae Lee: Native Speaker",
     "1995年。韓国系米国人スパイの言語と忠誠の二重性を扱う処女作。"),
    ("マデリン・ティエン『言わぬが花』", "Madeleine Thien: Do Not Say We Have Nothing",
     "2016年。文革と天安門を背景にカナダ華人三世代を描くブッカー候補作。"),
    ("タッシュ・アウ『五つ星億万長者』", "Tash Aw: Five Star Billionaire",
     "2013年。マレーシア華人五人の上海移住と新中国都市資本主義。"),
    # 3: ラテン系・先住民
    ("ジュノ・ディアス『オスカー・ワオの短く凄まじい人生』", "Junot Díaz: Brief Wondrous Life of Oscar Wao",
     "2007年ピューリッツァー賞。ドミニカ系米国人オタクとフクー呪いの家族史。"),
    ("サンドラ・シスネロス『マンゴー通り』詳論", "Sandra Cisneros: House on Mango Street",
     "1984年。シカゴのチカーナ少女エスペランサの44の散文詩的vignette。"),
    ("クリスティーナ・ガルシア『キューバ夢想』", "Cristina García: Dreaming in Cuban",
     "1992年。革命で離散したキューバ系三世代女性の記憶と政治。"),
    ("ルイーズ・アードリック『ラウンドハウス』", "Louise Erdrich: Round House",
     "2012年。オジブウェ保留地での母への暴行と少年の正義追求。"),
    ("トミー・オレンジ『ゼアゼア』", "Tommy Orange: There There",
     "2018年。オークランドの都市先住民12人の声が交錯するパウワウ襲撃。"),
    ("レスリー・マーモン・シルコ『死者の暦』", "Leslie Marmon Silko: Almanac of the Dead",
     "1991年。先住民予言と500年植民地暴力を描く763頁のラジカル叙事詩。"),
    # 4: 中東・南アジア系
    ("ヒシャム・マタール『男たちの国で』", "Hisham Matar: In the Country of Men",
     "2006年。カダフィ政権下リビアの少年スレイマンの父消失体験。"),
    ("ハラ・アライアン『塩の家』", "Hala Alyan: Salt Houses",
     "2017年。1967年戦争以降パレスチナ家族四世代の離散と家の記憶。"),
    ("ハーレド・ホッセイニ『君のためなら千回でも』", "Khaled Hosseini: Kite Runner",
     "2003年。アフガン少年アミールとハッサンの友情と戦後贖罪の旅。"),
    ("モハシン・ハミッド『出口の西へ』", "Mohsin Hamid: Exit West",
     "2017年。難民が魔法の扉で世界を移動する寓話的恋愛小説。"),
    ("カミラ・シャムジー『ホーム・ファイア』", "Kamila Shamsie: Home Fire",
     "2017年。アンティゴネ翻案。英国パキスタン系姉弟とISIS加入の悲劇。"),
    ("タミマ・アナム『骨たちの恵み』", "Tahmima Anam: Bones of Grace",
     "2016年。バングラデシュ三部作完結篇。古生物学者女性と離散の自己発見。"),
    # 5: 欧州ディアスポラ
    ("カリル・フィリップス『ケンブリッジ』", "Caryl Phillips: Cambridge",
     "1991年。19世紀奴隷男と英国女性の二重視点が交差する反転叙事。"),
    ("ハニフ・クレイシ『郊外の仏陀』詳論", "Hanif Kureishi: Buddha of Suburbia",
     "1990年。英国パキスタン系少年カリムの70年代郊外と性的覚醒。"),
    ("ザディー・スミス『ホワイト・ティース』詳論", "Zadie Smith: White Teeth",
     "2000年。ロンドンのジャマイカ系・ベンガル系・英国白人三家族のコメディ。"),
    ("モニカ・アリ『ブリック・レーン』", "Monica Ali: Brick Lane",
     "2003年。ロンドンのバングラデシュ系主婦ナズニーンの覚醒物語。"),
    ("モハシン・ハミッド『拒絶される根本主義者』詳論", "Mohsin Hamid: Reluctant Fundamentalist",
     "2007年。9.11後の米国でラホール出身青年が辿る信念の反転独白。"),
    ("ディナウ・メンゲストゥ『革命の子どもたち』", "Dinaw Mengestu: Children of the Revolution",
     "2007年（別題The Beautiful Things）。エチオピア難民のワシントン店主の孤独と歴史。"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for ja, en, defn in CONCEPTS:
        assert len(defn) <= 100, f"def too long: {len(defn)} {defn}"
        try:
            cur.execute(
                """INSERT INTO concepts (name_ja, name_en, subfield_id, region, period_id, definition, importance_score)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (ja, en, SUBFIELD, REGION, PERIOD, defn, 3),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP: {ja}: {e}")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
