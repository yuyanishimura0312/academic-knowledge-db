#!/usr/bin/env python3
"""Wave 38: Add 30 deep-niche concepts to subfield 19 (lit_indigenous_oral)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 19

# 5 clusters x 6 concepts. period: 15 = 先住民文芸復興期 (modern), 13 = 先住民口承伝統期 (oral)
CONCEPTS = [
    # Cluster 1: 北極圏イヌイット (period 15)
    ("ミティアルジュク・サナアク『サナアク』", "Mitiarjuk Nappaaluk, Sanaaq", "ᓴᓈᖅ", "Inuktitut", "世界", 15,
     "イヌクティトゥット語による初の本格的イヌイット小説、女性視点で日常生活を描く"),
    ("マーコーシー・パツァウク『銛打ちの狩人』", "Markoosie Patsauq, Harpoon of the Hunter", "ᓴᓇᔪᖅ", "Inuktitut", "世界", 15,
     "1969年発表、初英訳イヌイット小説。少年の北極狩猟譚に文化変容を織り込む"),
    ("トムソン・ハイウェイ『毛皮の女王のキス』", "Tomson Highway, Kiss of the Fur Queen", None, None, "世界", 15,
     "クリー族兄弟の寄宿学校体験を描く自伝的小説、トリックスター神話を構造に用いる"),
    ("ジョシュア・ホワイトヘッド『ジョニー・アップルシード』", "Joshua Whitehead, Jonny Appleseed", None, None, "世界", 15,
     "オジ・クリー族トゥースピリット主人公の都市先住民クィア小説、ランブラー文体採用"),
    ("ノルマ・ダニング『アニー・ムクトゥク』", "Norma Dunning, Annie Muktuk and Other Stories", None, None, "世界", 15,
     "イヌイット女性の生を描く短篇集、定住化と生存の狭間を口承的リズムで語る"),
    ("ダフネ・マーラット『スティーヴストン』", "Daphne Marlatt, Steveston", None, None, "世界", 15,
     "コースト・サリッシュ漁村の場所性詩、日系・先住民・白人の重層的記憶を地誌詩で再構築"),

    # Cluster 2: アボリジニ・トレス諸島 (period 15)
    ("ウジェルー・ヌーヌッカル『私たちは去る』", "Oodgeroo Noonuccal, We Are Going", None, None, "世界", 15,
     "アボリジニ初の英語詩集（1964）、植民地暴力と文化喪失を抗議する政治詩"),
    ("キム・スコット『ベナング』", "Kim Scott, Benang: From the Heart", None, None, "世界", 15,
     "ヌーンガル族の同化政策史を断章形式で告発、ハーモニー失調世代の傷を描く"),
    ("アレクシス・ライト『カーペンタリア』", "Alexis Wright, Carpentaria", None, None, "世界", 15,
     "ワーニ族の神話的時間軸でカーペンタリア湾紛争を描く、マジックリアリズム的長篇"),
    ("タラ・ジューン・ウィンチ『収穫』", "Tara June Winch, The Yield", None, None, "世界", 15,
     "ウィラジュリ語辞書を構造に用い言語復興と先祖の声を編む小説、マイルズ・フランクリン賞"),
    ("メリッサ・ルカショーンコ『あまりの口』", "Melissa Lucashenko, Too Much Lip", None, None, "世界", 15,
     "ブンジャラング族家族のブラック・コメディ、女性主権と土地返還闘争を描く"),
    ("キム・スコット『あの死人の踊り』", "Kim Scott, That Deadman Dance", None, None, "世界", 15,
     "ヌーンガル族と入植者の友好的接触から離反への転換を描く歴史小説、コモンウェルス賞"),

    # Cluster 3: マオリ詩・劇 (period 15)
    ("ホネ・トゥファレ『普通でない太陽』", "Hone Tuwhare, No Ordinary Sun", None, None, "世界", 15,
     "1964年マオリ初英語詩集、核実験への抗議と土地への愛を口承リズムで歌う"),
    ("アピラナ・テイラー『柔らかな葉が銀に落ちる』", "Apirana Taylor, Soft Leaf Falls of Silver", None, None, "世界", 15,
     "テ・アティアワ詩人による短詩集、ハカ・ファカパパ・カラキアの音調を現代詩へ翻案"),
    ("バブ・ブリッジャー『ザクロ』", "Bub Bridger, Pomegranate", None, None, "世界", 15,
     "ンガーティ・カフングヌ女性詩人による生活詩集、家族とフェミニンな身体性を描く"),
    ("ロバート・サリヴァン『キャプテン・クック』", "Robert Sullivan, Captain Cook in the Underworld", None, None, "世界", 15,
     "クック航海をマオリ視点で書き換える長詩、海洋叙事詩と植民地批判の結節"),
    ("ブライアン・ヴィンセント・ウォルポール詩", "Bryan Vincent Walpole poetry", None, None, "世界", 15,
     "テ・アラワ詩人、温泉地ロトルアと祖先の声を素材にした詠唱的英語詩"),
    ("ホネ・ヒパンゴ詩劇", "Hone Hipango verse drama", None, None, "世界", 15,
     "ファンガヌイ部族の劇詩家、マラエ儀礼の語り口を現代演劇に移植"),

    # Cluster 4: 北米先住民散文 (period 15)
    ("モマデイ『夜明けに作られた家』初版論", "N. Scott Momaday, House Made of Dawn", None, None, "世界", 15,
     "1969ピューリッツァー受賞、ジマソン帰還の儀礼的構造でナバホ・キオワ精神性を描く"),
    ("シルコ『儀式』儀礼治療論", "Leslie Marmon Silko, Ceremony", None, None, "世界", 15,
     "ラグーナ・プエブロ復員兵の治癒物語、ケレス語儀礼歌の詩節を散文に編み込む"),
    ("ヴァイザナー『ベアハート』", "Gerald Vizenor, Bearheart: The Heirship Chronicles", None, None, "世界", 15,
     "アニシナーベ・ピカレスク小説、トリックスターを核にポストモダン先住民批評を実装"),
    ("トーマス・キング『緑の草、流れる水』詳細", "Thomas King, Green Grass Running Water", None, None, "世界", 15,
     "チェロキー系作家による多声小説、聖書・西部劇・先住民創世神話を交差させる構造"),
    ("デイヴィッド・トルーアー『ハイアワサ』", "David Treuer, The Hiawatha", None, None, "世界", 15,
     "オジブウェ作家によるミネアポリス都市先住民小説、Termination政策後の労働と暴力を描く"),
    ("ダイアン・グランシー『プッシング・ベア』", "Diane Glancy, Pushing the Bear", None, None, "世界", 15,
     "チェロキー涙の道を多声で再現する歴史小説、強制移住の暴力をオーラル断章で構成"),

    # Cluster 5: アンデス・アマゾン口承 (period 13)
    ("ケチュア・ワカ物語群", "Quechua wak'a stories", "wak'a willakuy", "Quechua", "世界", 13,
     "アンデス聖地ワカに宿る祖霊の語り、地形と神格化された山岳精霊を結ぶ口承伝承群"),
    ("アイマラ・アチャチラ物語", "Aymara achachila narratives", "achachila", "Aymara", "世界", 13,
     "祖父山岳神アチャチラの守護と懲罰を語る伝承、ティティカカ周辺で儀礼酒供物と結合"),
    ("ヤノマミ・シャーマン詠唱", "Yanomami shamanic chants (xapiri)", "xapiri pë", "Yanomami", "世界", 13,
     "シャピリ精霊を呼び出す詠唱、エペナ吸入と多声で森林宇宙を組成する儀礼ボイス"),
    ("アシャニンカ・ソング・サイクル", "Ashaninka song cycle", None, "Asháninka", "世界", 13,
     "ペルー・アマゾン民の儀礼歌循環、マサト酒宴で連歌的に演唱される世代継承詠唱"),
    ("シュアル・ツァンツァ語り", "Shuar tsantsa narrative", None, "Shuar", "世界", 13,
     "首狩り儀礼に伴う語り、敵霊ムイサクを縛り力を反転させる口承詩学"),
    ("カヤポー神話循環", "Kayapó myth cycle", None, "Mẽbêngôkre", "世界", 13,
     "メベンゴクレ族の創世・ジャガー火・天体神話を結ぶ循環、男性会堂で連夜語り継がれる"),
]

assert len(CONCEPTS) == 30, f"Expected 30 got {len(CONCEPTS)}"


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Get existing names to skip dupes
    existing = {r[0] for r in cur.execute(
        "SELECT name_ja FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    )}

    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, region, period_id, definition in CONCEPTS:
        if name_ja in existing:
            skipped += 1
            print(f"SKIP dup: {name_ja}")
            continue
        assert len(definition) <= 100, f"Definition too long ({len(definition)}): {name_ja}"
        cur.execute(
            """
            INSERT INTO concepts
              (name_ja, name_en, name_original, original_script,
               subfield_id, region, period_id, definition,
               importance_score, source_tier)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (name_ja, name_en, name_orig, script,
             SUBFIELD_ID, region, period_id, definition, 3, "secondary"),
        )
        inserted += 1
    conn.commit()

    total = cur.execute(
        "SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    ).fetchone()[0]
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {skipped}, Total in subfield {SUBFIELD_ID}: {total}")


if __name__ == "__main__":
    main()
