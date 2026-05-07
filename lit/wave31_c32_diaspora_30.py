#!/usr/bin/env python3
"""Wave 31 C32 - Add 30 diaspora literature concepts to subfield 20."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SUBFIELD_ID = 20
PERIOD_ID = 168  # グローバル・ディアスポラ期 / ディアスポラ
REGION = "ディアスポラ"

# 5 clusters x 6 concepts = 30
CONCEPTS = [
    # Cluster 1: Asian American (Chinese American)
    ("マキシン・ホン・キングストン『女武者』", "Maxine Hong Kingston, The Woman Warrior",
     "中国系米女性の母系記憶と神話を交錯させた回想録、AA文学の画期作。"),
    ("エイミー・タン『ジョイ・ラック・クラブ』", "Amy Tan, The Joy Luck Club",
     "中国系米母娘四組の記憶と移民世代間トラウマを描く連作長篇。"),
    ("フランク・チン『ドナルド・ダック』", "Frank Chin, Donald Duk",
     "サンフランシスコ華人少年の自己同定をめぐる成長譚、関帝伝説を内包。"),
    ("チャンネ・リー『ネイティブ・スピーカー』", "Chang-rae Lee, Native Speaker",
     "韓国系米スパイ小説、言語と同化の二重性を探るAA文学転回作。"),
    ("イーユン・リー『漂泊者』", "Yiyun Li, The Vagrants",
     "毛沢東後中国地方都市を舞台に処刑と政治抑圧を描くディアスポラ的視座。"),
    ("チャールズ・ユー『インテリア・チャイナタウン』", "Charles Yu, Interior Chinatown",
     "脚本形式で華人俳優のステレオタイプ化を問うメタフィクション、全米図書賞。"),

    # Cluster 2: Korean + Vietnamese American
    ("ミン・ジン・リー『パチンコ』", "Min Jin Lee, Pachinko",
     "在日コリアン四世代を辿る大河小説、ザイニチ経験を英語圏に拓く。"),
    ("クリス・リー『漂う家』", "Krys Lee, Drifting House",
     "韓国・米国・脱北者を横断する短篇集、移動と離散の心象を凝縮。"),
    ("キャシー・パーク・ホン『マイナー・フィーリングズ』", "Cathy Park Hong, Minor Feelings",
     "アジア系米国人感情のマイナー性を理論化したエッセイ集、批評転回作。"),
    ("レ・ティ・ジエム・トゥイ『ギャングスター』", "Le Thi Diem Thuy, The Gangster We Are All Looking For",
     "ベトナム系米難民少女の家族と記憶を断片詩的に描く自伝的小説。"),
    ("オーシャン・ヴオン『地上で僕らは』", "Ocean Vuong, On Earth We're Briefly Gorgeous",
     "ベトナム系米詩人による母への手紙形式の小説、戦争と性の交点。"),
    ("ヴィエト・タン・ウェン『シンパサイザー』", "Viet Thanh Nguyen, The Sympathizer",
     "南ベトナム情報将校の二重スパイ的告白、ピューリッツァー賞。"),

    # Cluster 3: South Asian Diaspora
    ("サルマン・ラシュディ『真夜中の子供たち』", "Salman Rushdie, Midnight's Children",
     "印分離独立の夜に生まれた子ら、マジックリアリズム的国民寓話、ブッカー受賞。"),
    ("ジュンパ・ラヒリ『停電の夜に』", "Jhumpa Lahiri, Interpreter of Maladies",
     "印系米移民の日常を精緻に描く短篇集、ピューリッツァー賞。"),
    ("ヴィクラム・セット『相応しい少年』", "Vikram Seth, A Suitable Boy",
     "1950年代印で娘の縁談を軸に四家族を辿る大長篇、英語印度小説の代表。"),
    ("バーラティ・ムケルジー『ジャスミン』", "Bharati Mukherjee, Jasmine",
     "印女性が米国へ越境し自己改名する移民小説、変容の暴力を描く。"),
    ("アキル・シャルマ『家族の生活』", "Akhil Sharma, Family Life",
     "印系米家族と兄の事故後障害を扱う自伝的小説、ダブリン文学賞。"),
    ("モハシン・ハミッド『拒絶される根本主義者』", "Mohsin Hamid, The Reluctant Fundamentalist",
     "9/11後のパキスタン系男のモノローグ小説、対米感情のディアスポラ的反転。"),

    # Cluster 4: Caribbean + Black British
    ("V・S・ナイポール『川の湾曲』", "V. S. Naipaul, A Bend in the River",
     "脱植民地アフリカ町に住む印系商人の眼差し、ポストコロニアル黙示録。"),
    ("サム・セルヴォン『孤独なロンドン人』", "Sam Selvon, The Lonely Londoners",
     "ウィンドラッシュ世代カリブ移民の英都市生活をクレオール散文で描く。"),
    ("マーロン・ジェイムズ『七つの殺人の簡潔な歴史』", "Marlon James, A Brief History of Seven Killings",
     "ジャマイカ多声長篇、ボブ・マーリー暗殺未遂を中心に、ブッカー受賞。"),
    ("ベルナーディン・エヴァリスト『少女、女、その他』", "Bernardine Evaristo, Girl, Woman, Other",
     "黒英女性十二人の声を散文詩で結ぶ多声小説、ブッカー共同受賞。"),
    ("カリル・フィリップス『川を渡る』", "Caryl Phillips, Crossing the River",
     "奴隷貿易を父の独白で枠組み、四世紀のディアスポラ多声長篇。"),
    ("アンドレア・レヴィ『スモール・アイランド』", "Andrea Levy, Small Island",
     "戦後ロンドンのジャマイカ移民四人称多声、ウィンドラッシュ世代記憶化。"),

    # Cluster 5: Jewish + Translingual
    ("ソール・ベロー『オーギー・マーチ』", "Saul Bellow, The Adventures of Augie March",
     "シカゴ猶系青年の自由探求、米猶系小説の標準を打ち立てた成長譚。"),
    ("フィリップ・ロス『アメリカン・パストラル』", "Philip Roth, American Pastoral",
     "ニュージャージー猶系一家のアメリカ夢崩壊、ピューリッツァー賞。"),
    ("シンシア・オジック『ショール』", "Cynthia Ozick, The Shawl",
     "ホロコースト収容所と亡命後を結ぶ短篇二連作、沈黙と証言の文学。"),
    ("多和田葉子『雪の練習生』", "Yoko Tawada, Memoirs of a Polar Bear",
     "三世代北極熊を語り手にエクソフォニックに越境する独日語小説。"),
    ("アレクサンドル・ヘモン『ブルーノの問題』", "Aleksandar Hemon, The Question of Bruno",
     "サラエボ出身亡命者が英語で書く短篇集、戦争と翻訳の自己。"),
    ("テレサ・ハッキョン・チャ『ディクテ』", "Theresa Hak Kyung Cha, Dictee",
     "韓国系米作家による多言語多媒体テクスト、植民地・ジェンダー・言語批判の前衛作。"),
]

# Replacements for duplicates: 12 alternative works by same authors / same clusters
REPLACEMENTS = [
    # C1 replacements
    ("イーユン・リー『千年の祈り』", "Yiyun Li, A Thousand Years of Good Prayers",
     "中国系米作家の短篇集、改革開放後の中国と移民後の沈黙を描く。"),
    ("チャールズ・ユー『SF的宇宙で安全に生きる方法』", "Charles Yu, How to Live Safely in a Science Fictional Universe",
     "華系米作家のメタSF父子小説、時間機械修理工の自伝的探究。"),
    # C2 replacements
    ("ミン・ジン・リー『無料の食事』", "Min Jin Lee, Free Food for Millionaires",
     "韓国系米女性のニューヨーク経済社会を描く長篇、移民二世の階級越境。"),
    ("キャシー・パーク・ホン『翻訳された英語』", "Cathy Park Hong, Translating Mo'um",
     "韓国系米詩人の第一詩集、コードスイッチと身体の翻訳可能性を問う。"),
    ("ヴィエト・タン・ウェン『難民たち』", "Viet Thanh Nguyen, The Refugees",
     "ベトナム系米作家の短篇集、難民経験と亡命の倫理を多面的に描く。"),
    # C3 replacements
    ("アキル・シャルマ『従順な父』", "Akhil Sharma, An Obedient Father",
     "デリーの腐敗官僚を主人公とする処女長篇、家父長制の暴力を解剖。"),
    # C4 replacements
    ("マーロン・ジェイムズ『黒豹、赤狼』", "Marlon James, Black Leopard, Red Wolf",
     "アフリカ神話に基づくダーク・スター三部作の第一作、黒人ファンタジー再構築。"),
    ("ベルナーディン・エヴァリスト『マニフェスト』", "Bernardine Evaristo, Manifesto",
     "黒英女性作家の自伝的マニフェスト、黒英文学の40年を語る。"),
    ("アンドレア・レヴィ『ロング・ソング』", "Andrea Levy, The Long Song",
     "19世紀ジャマイカ奴隷制末期を女主人公の声で描く長篇、コスタ賞。"),
    # C5 replacements
    ("フィリップ・ロス『ヒューマン・ステイン』", "Philip Roth, The Human Stain",
     "黒人を隠して生きた猶系古典学者の暴露譚、米国三部作完結巻。"),
    ("多和田葉子『献灯使』", "Yoko Tawada, The Emissary",
     "災後鎖国した近未来日本で老曾祖父と虚弱曾孫を描く、全米図書賞翻訳部門。"),
    ("アレクサンドル・ヘモン『どこにもない人間』", "Aleksandar Hemon, Nowhere Man",
     "サラエボ出身ヨーゼフ・プローネクの分裂的伝記小説、亡命者の自我多重化。"),
]

CONCEPTS = CONCEPTS + REPLACEMENTS
# Now we have 42 candidates; aim is 30 net new. Script will skip dupes naturally.
assert len(CONCEPTS) == 42, len(CONCEPTS)
for _, _, d in CONCEPTS:
    assert len(d) <= 100, (len(d), d)



def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, definition in CONCEPTS:
        try:
            cur.execute(
                """
                INSERT INTO concepts (name_ja, name_en, subfield_id, region, period_id, definition, importance_score)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (name_ja, name_en, SUBFIELD_ID, REGION, PERIOD_ID, definition, 4),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"skip: {name_ja} ({e})")
    conn.commit()
    total = cur.execute(
        "SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SUBFIELD_ID,)
    ).fetchone()[0]
    conn.close()
    print(f"inserted={inserted} skipped={skipped} total_subfield20={total}")


if __name__ == "__main__":
    main()
