#!/usr/bin/env python3
"""Wave 30 C30 — Indigenous oral lit subfield_id=19, +30 concepts (5 clusters x 6)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 19
REGION = "周縁横断"
PERIOD_ID = 15  # 先住民文芸復興期

CONCEPTS = [
    # Cluster 1: ネイティブ・アメリカン
    ("モマデイ『夜明けに作られた家』詳論", "House Made of Dawn detailed", "House Made of Dawn", "latin",
     "1968年ピュリツァー賞受賞作。ネイティブ・アメリカン・ルネッサンスの起点となった小説。", 5),
    ("シルコ『儀式』詳論", "Ceremony detailed", "Ceremony", "latin",
     "ラグナ・プエブロ伝承を骨格に、戦争PTSDからの治癒物語を編む代表作。", 5),
    ("アードリック『ラブ・メディスン』詳論", "Love Medicine detailed", "Love Medicine", "latin",
     "オジブウェ家族の連作短編。多視点語りでネイティブの近現代生活を描く。", 5),
    ("アレクシー『ローン・レンジャーとトント』", "Lone Ranger and Tonto Fistfight", "The Lone Ranger and Tonto Fistfight in Heaven", "latin",
     "スポケーン保留地の現代生活をユーモアと痛みで描く短編連作。", 4),
    ("ハージョ『彼女は何頭かの馬を持っていた』詳論", "She Had Some Horses detailed", "She Had Some Horses", "latin",
     "マスコギー詩人ハージョの代表詩集。儀礼的反復と祈りの詩学。", 4),
    ("オレンジ『ゼア・ゼア』詳論", "There There detailed", "There There", "latin",
     "都市インディアンの12人をオークランドのパウワウに収斂させる多声小説。", 5),

    # Cluster 2: カナダ・豪先住民
    ("ハイウェイ『リズ姉妹』詳論", "The Rez Sisters detailed", "The Rez Sisters", "latin",
     "クリー語族劇作家による7女性のビンゴ巡礼劇。先住民演劇の里程標。", 4),
    ("トーマス・キング『緑の草、流れる水』詳論", "Green Grass Running Water detailed", "Green Grass, Running Water", "latin",
     "ブラックフット創世神話と西洋古典を交錯させるメタ小説。", 5),
    ("ライト『カーペンタリア』詳論", "Carpentaria detailed", "Carpentaria", "latin",
     "ワーニ族出身ライトのマイルズ・フランクリン賞作。湾岸地帯の長大叙事。", 5),
    ("キム・スコット『ベナング』", "Benang", "Benang: From the Heart", "latin",
     "ヌンガ系作家による同化政策犠牲者の系譜回復小説。", 4),
    ("ウィンチ『収穫』詳論", "The Yield detailed", "The Yield", "latin",
     "ウィラジュリ語辞書を編む祖父の遺稿を軸に、言語と土地の回復を描く。", 4),
    ("マリア・キャンベル『ハーフブリード』詳論", "Halfbreed detailed", "Halfbreed", "latin",
     "メティス女性の自伝。カナダ先住民女性文学の出発点となった証言。", 4),

    # Cluster 3: 太平洋諸島
    ("イヒマエラ『ホエール・ライダー』詳論", "Whale Rider detailed", "The Whale Rider", "latin",
     "マオリ系作家によるカフィア部族の女性後継者譚。映画化で世界的反響。", 5),
    ("グレイス『ポティキ』詳論", "Potiki detailed", "Potiki", "latin",
     "マオリ共同体への観光開発を巡るパトリシア・グレイスの代表作。", 4),
    ("ハルメ『骨の人々』詳論", "The Bone People detailed", "The Bone People", "latin",
     "1985年ブッカー賞受賞。マオリ・ケルト混淆の三人を描く実験的小説。", 5),
    ("ウェンド『帰郷の息子たち』詳論", "Sons for the Return Home detailed", "Sons for the Return Home", "latin",
     "サモア系アルバート・ウェンドのポリネシア・ディアスポラ初期長編。", 4),
    ("フィギエル『私たちがかつて居た場所』詳論", "Where We Once Belonged detailed", "Where We Once Belonged", "latin",
     "サモア女性初の長編小説。村落少女の声を集合的語り口で描く。", 4),
    ("サリヴァン『スター・ワカ』詳論", "Star Waka detailed", "Star Waka", "latin",
     "マオリ詩人ロバート・サリヴァンによる2000行のカヌー・船航海連詩。", 4),

    # Cluster 4: アイヌ詳細
    ("知里幸恵『アイヌ神謡集』詳論", "Ainu Shinyoshu detailed", "アイヌ神謡集", "kanji",
     "1923年刊。19歳の知里幸恵がカムイユカラ13編をローマ字+和訳で集成。", 5),
    ("バチェラー『アイヌ詞曲集』", "Bachelor Ainu Songs", "アイヌ詞曲集", "kanji",
     "宣教師ジョン・バチェラーがアイヌ口承を採録・英訳した先駆資料。", 3),
    ("萱野茂『カムイユカラ』詳論", "Kayano Kamuy Yukar detailed", "カムイユカラ", "kanji",
     "二風谷の語り部萱野茂が録音採録したカムイユカラ集。研究基礎資料。", 4),
    ("ノック・ウッド口承法", "Knock Wood storytelling", "クナルアシ", "kanji",
     "アイヌ女性語り手による炉縁を木で打ち拍子をとる口承スタイル。", 3),
    ("砂澤クラ語り", "Sumiya Sakata orality", "砂澤クラ", "kanji",
     "アイヌ女性語り手砂澤クラのウエペケレ採録。家庭口承の貴重記録。", 3),
    ("アイヌ資源回復文学", "Ainu resource recovery lit", "アイヌ資源回復", "kanji",
     "21世紀アイヌが言語・神謡・物語を主体的に取り戻す現代運動の文芸。", 4),

    # Cluster 5: 先住民理論
    ("ジャスティス『なぜ先住民文学が重要か』詳論", "Why Indigenous Literatures Matter detailed", "Why Indigenous Literatures Matter", "latin",
     "チェロキー研究者ダニエル・ジャスティスによる先住民文学論の現代的綱領。", 5),
    ("ウォマック『レッド・オン・レッド』", "Red on Red", "Red on Red: Native American Literary Separatism", "latin",
     "クレイグ・ウォマックによる先住民文学的分離主義の宣言的批評書。", 5),
    ("ヴァイザナー・サヴァイヴァンス論", "Vizenor survivance theory", "Survivance", "latin",
     "ジェラルド・ヴァイザナーによる生存と抵抗の融合概念。先住民批評の鍵。", 5),
    ("クルサード『赤い肌、白い仮面』詳論", "Red Skin White Masks detailed", "Red Skin, White Masks", "latin",
     "ヤロウク・デネ哲学者クルサードによる承認の政治批判と再起化理論。", 5),
    ("ルイス先住民未来想像論", "Lewis future imaginary", "Indigenous Futurisms", "latin",
     "ジェイソン・ルイスらによる先住民AI主権・未来想像の理論枠組み。", 4),
    ("GIDA先住民データ主権原則", "GIDA Indigenous data principles", "CARE Principles", "latin",
     "Global Indigenous Data Allianceが定めたCARE原則。データ主権の規範。", 4),
]

def main():
    assert len(CONCEPTS) == 30, f"Expected 30 concepts, got {len(CONCEPTS)}"
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, definition, importance in CONCEPTS:
        assert len(definition) <= 100, f"Definition too long ({len(definition)}): {name_ja}"
        try:
            cur.execute("""
                INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name_ja, name_en, name_orig, script, SUBFIELD_ID, REGION, PERIOD_ID,
                  definition, importance))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,))
    total = cur.fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total subfield 19: {total}")

if __name__ == "__main__":
    main()
