#!/usr/bin/env python3
"""Wave37: subfield 16 (lit_latin_america) +30 niche concepts in 5 clusters."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"
SF = 16
REGION = "ラテンアメリカ"

# Period IDs (region='ラテンアメリカ')
P_POSTBOOM = 225      # ポスト・ブーム期
P_MCONDO = 226        # McOndo・Crack世代
P_WOMEN21 = 232       # 21世紀女性作家期
P_BRZMOD = 229        # ブラジル現代文学期
P_BRZNEAR = 259       # ブラジル深掘り期
P_POSTDIC = 260       # ポスト独裁期
P_ARG_BORG = 286      # アルゼンチン・ポスト・ボルヘス期
P_BOOM = 224          # ラテンアメリカ・ブーム期拡張
P_BOOMSUP = 258       # Boom補完期
P_INDIG = 223         # インディヘニスモ期
P_MEXPAZ = 285        # メキシコ・パス期

CONCEPTS = [
  # Cluster 1: ブームポスト世代（NICHE）
  ("ボラーニョ『2666』五部構造詳論", "Bolaño '2666' Five-Part Structure", "2666", "latin",
   P_MCONDO, "批評家・アマルフィターノ・フェイト・犯罪・アルチンボルディの五部からなる遺作巨篇の構造分析。", 4),
  ("ボラーニョ『野生の探偵たち』口承証言形式", "Bolaño 'Los detectives salvajes' Oral Testimony Form", "Los detectives salvajes", "latin",
   P_MCONDO, "53証言で構成される多声口承形式。インフラレアリスモ詩人世代の彷徨を再構築する手法。", 4),
  ("セサル・アイラ『エピソード ある看護婦の人生』", "César Aira 'Un episodio en la vida del pintor viajero'", "Un episodio", "latin",
   P_MCONDO, "ルゲンダスの被雷事件を起点にした即興的逸話小説。アイラの逃走前進(huida hacia adelante)技法。", 3),
  ("リカルド・ピグリア『燃える金』", "Ricardo Piglia 'Plata quemada'", "Plata quemada", "latin",
   P_ARG_BORG, "1965年実在の銀行強盗事件を題材にした犯罪ノワール。証言・新聞・尋問を多層モンタージュ。", 3),
  ("フアン・ビジョーロ『証人』", "Juan Villoro 'El testigo'", "El testigo", "latin",
   P_MCONDO, "亡命帰国者がメキシコPRI体制崩壊期を見届けるエルアラ賞受賞長篇。私的記憶と国家史の交差。", 3),
  ("アレハンドロ・サンブラ『盆栽』詳論", "Alejandro Zambra 'Bonsái' Detailed", "Bonsái", "latin",
   P_MCONDO, "ジュリオとエミリアの恋と読書の物語。極小ノヴェラ形式でチリ・ポスト独裁世代の感性を描く。", 4),

  # Cluster 2: 女性新世代（NICHE）
  ("サマンタ・シュウェブリン『救援距離』詳論", "Schweblin 'Distancia de rescate' Detailed", "Distancia de rescate", "latin",
   P_WOMEN21, "農薬汚染の村を舞台にする母娘の対話形式エコゴシック。Booker International候補。", 4),
  ("マリアナ・エンリケス『焚き火で失ったもの』短篇集詳論", "Mariana Enriquez 'Las cosas que perdimos en el fuego' Detailed", "Las cosas que perdimos en el fuego", "latin",
   P_WOMEN21, "アルゼンチン都市ゴシック短篇集。独裁の暴力記憶とフェミニスト身体政治を結ぶ。", 4),
  ("フェルナンダ・メルチョール『ハリケーンの季節』", "Fernanda Melchor 'Temporada de huracanes'", "Temporada de huracanes", "latin",
   P_WOMEN21, "メキシコ農村の魔女殺害を多視点長文で描く。麻薬暴力・性暴力・貧困を呪詛的文体で炙り出す。", 4),
  ("ポラ・オロイサラック『暗い星座』", "Pola Oloixarac 'Las constelaciones oscuras'", "Las constelaciones oscuras", "latin",
   P_WOMEN21, "植物学・生体認証・サイバー諜報を貫く三段構成。アルゼンチン理論派フェミニスト・サイファイ。", 3),
  ("セルバ・アルマダ『風が吹き荒ぶ』", "Selva Almada 'El viento que arrasa'", "El viento que arrasa", "latin",
   P_WOMEN21, "アルゼンチン北部の福音派牧師と整備工が嵐の一日を共に過ごす対話劇的長篇。乾いた地方文体。", 3),
  ("アリアナ・ハーウィッツ『死ね、愛しい人』", "Ariana Harwicz 'Matate, amor'", "Matate, amor", "latin",
   P_WOMEN21, "産後うつの母の独白で構成される過剰文体長篇。フランス田舎を舞台にしたディアスポラ女性文学。", 3),

  # Cluster 3: ブラジル細部（NICHE）
  ("リスペクトル『星の時』詳論", "Lispector 'A Hora da Estrela' Detailed", "A Hora da Estrela", "latin",
   P_BRZNEAR, "北東部出身マカベアと男性語り手ロドリゴ・SMの二重視点で書かれる遺作。階級・声・存在論。", 4),
  ("ギマランエス・ロサ『大いなる奥地：諸小道』", "Guimarães Rosa 'Grande Sertão: Veredas'", "Grande Sertão: Veredas", "latin",
   P_BRZNEAR, "ジャグンソ・リオバルドの一人語りで進む奥地叙事詩。造語と方言を融合した革新的散文。", 5),
  ("ジョアン・カブラル『セヴェリーノの死と生』", "João Cabral 'Morte e Vida Severina'", "Morte e Vida Severina", "latin",
   P_BRZMOD, "北東部移民セヴェリーノの旅を描くクリスマス劇詩。乾いた構成主義詩学の代表作。", 4),
  ("ヒルダ・イルスト『愛人への手紙』", "Hilda Hilst 'Cartas de um sedutor'", "Cartas de um sedutor", "latin",
   P_BRZNEAR, "猥褻三部作の一篇。書簡形式でエロス・宗教・狂気を融合させる前衛詩人散文。", 3),
  ("アデリア・プラード『荷物』", "Adélia Prado 'Bagagem'", "Bagagem", "latin",
   P_BRZMOD, "ミナス・ジェライス出身の主婦詩人デビュー詩集。日常神秘主義と女性身体の聖性を歌う。", 3),
  ("マルサル・アキーノ『殺すための頭』", "Marçal Aquino 'Cabeça a prêmio'", "Cabeça a prêmio", "latin",
   P_BRZNEAR, "麻薬密売・国境暴力を描くハードボイルド長篇。映画化もされたブラジル新ノワール代表。", 3),

  # Cluster 4: メキシコ・中米（NICHE）
  ("セルヒオ・ピトル『記憶の三部作』", "Sergio Pitol 'Trilogía de la memoria'", "Trilogía de la memoria", "latin",
   P_MEXPAZ, "『言葉の芸術』『旅』『魔術師の魔術』からなる自伝・旅行記・批評融合エッセイ。Cervantes賞2005。", 4),
  ("ルルフォ『ペドロ・パラモ』詳論", "Rulfo 'Pedro Páramo' Detailed", "Pedro Páramo", "latin",
   P_INDIG, "コマラの亡霊声群が織りなす断片構造。地主パラモを中心にメキシコ革命後の魂を弔う遺作。", 5),
  ("マルゴ・グランツ『家系図』", "Margo Glantz 'Las genealogías'", "Las genealogías", "latin",
   P_MEXPAZ, "ロシア系ユダヤ移民の両親をたどる自伝。ディアスポラ記憶とメキシコ文学を交錯させる傑作。", 3),
  ("バレリア・ルイセリ『失われた子どもたちのアーカイブ』", "Valeria Luiselli 'Lost Children Archive'", "Lost Children Archive", "latin",
   P_WOMEN21, "米墨国境を移動する家族と移民児童の声を重ねるドキュメンタリー長篇。英語執筆メキシコ作家。", 4),
  ("オラシオ・カステリャーノス・モヤ『嫌悪』", "Horacio Castellanos Moya 'El asco'", "El asco", "latin",
   P_POSTDIC, "サルバドル人主人公がベルンハルト風長文独白で祖国を罵倒する短篇。中米ポスト内戦文学の挑発作。", 3),
  ("リタ・インディアナ『ムカマス・デ・オムニクンレ』", "Rita Indiana 'La mucama de Omicunlé'", "La mucama de Omicunlé", "latin",
   P_WOMEN21, "ドミニカ未来都市を舞台にトランス主人公とサンテリア神霊が交差するクィア・カリブSF。", 3),

  # Cluster 5: アンデス・南錐（NICHE）
  ("アルゲダス『ヤワル・フィエスタ』", "Arguedas 'Yawar Fiesta'", "Yawar Fiesta", "latin",
   P_INDIG, "プキオ村のインディヘナ闘牛祭をめぐる多言語小説。スペイン語にケチュア統辞を埋め込む実験。", 4),
  ("バルガス・リョサ『緑の家』", "Vargas Llosa 'La casa verde'", "La casa verde", "latin",
   P_BOOM, "ピウラ砂漠とアマゾン奥地を交錯させる五系統並走長篇。Boom構造実験の代表作。", 4),
  ("ロベルト・アルト『七人の狂人』", "Roberto Arlt 'Los siete locos'", "Los siete locos", "latin",
   P_BOOMSUP, "ブエノスアイレス都市悪夢小説。エルドガインら陰謀結社の妄想で大恐慌期社会を描く。", 4),
  ("サラ・ガジャルド『エイセイハス』", "Sara Gallardo 'Eisejuaz'", "Eisejuaz", "latin",
   P_BOOMSUP, "アルゼンチン北部マタコ族の信仰を独特の口承文体で描く語り手小説。再評価が進む隠れた傑作。", 3),
  ("ディアメラ・エルティト『第四世界』", "Diamela Eltit 'El cuarto mundo'", "El cuarto mundo", "latin",
   P_POSTDIC, "双子の胎内意識から始まるピノチェト期実験小説。身体・国家・言語の暴力を破砕的文体で記述。", 4),
  ("ネストル・ペルロンゲール『屍体』", "Néstor Perlongher 'Cadáveres'", "Cadáveres", "latin",
   P_POSTDIC, "アルゼンチン軍政desaparecidosを呼び出すネオバロック詩。クィア南米詩学の到達点。", 4),
]

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    inserted, skipped = 0, []
    for name_ja, name_en, name_orig, script, period_id, definition, score in CONCEPTS:
        try:
            cur.execute("""
                INSERT INTO concepts
                  (name_ja, name_en, name_original, original_script,
                   subfield_id, region, period_id, definition,
                   importance_score, source_tier, canonical_in_region)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """, (name_ja, name_en, name_orig, script,
                  SF, REGION, period_id, definition,
                  score, "tier2", "yes"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped.append((name_ja, str(e)))
    con.commit()
    cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SF,))
    total = cur.fetchone()[0]
    con.close()
    print(f"Inserted: {inserted}/30 | Skipped: {len(skipped)} | Total subfield={SF}: {total}")
    for s in skipped:
        print("  -", s[0], "::", s[1])

if __name__ == "__main__":
    main()
