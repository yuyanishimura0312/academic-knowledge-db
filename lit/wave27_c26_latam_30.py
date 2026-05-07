#!/usr/bin/env python3
"""Wave 27 - Latin America 30 concepts (5 clusters x 6)."""
import sqlite3, sys

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/lit/lit.sqlite"
SUBFIELD_ID = 16
REGION = "ラテンアメリカ"

# period mapping (use existing periods)
P_BR_19 = 280   # ブラジル19世紀補完期
P_BR_POETRY = 281  # ブラジル20世紀詩補完期
P_LATAM_19_F = 282  # 19世紀ラテンアメリカ女性期
P_MOD = 283     # モデルニスモ詳細期
P_20F = 256     # 20世紀前半期
P_POSTDIC = 260 # ポスト独裁期
P_MCONDO = 226  # McOndo・Crack世代
P_BOOM = 224    # Boom拡張
P_BOOMSUP = 258 # Boom補完期
P_F21 = 232     # 21世紀女性作家期
P_PB = 286      # アルゼンチン・ポスト・ボルヘス期

# (name_ja, name_en, name_original, period_id, definition<=100, importance, source_tier, fourth_status)
CONCEPTS = [
  # Cluster 1: Brazilian詳細
  ("アレンカール『イラセマ』詳論", "Alencar 'Iracema' detailed", "Iracema", P_BR_19,
   "1865年ブラジル先住民派ロマン主義小説。詩的散文で先住民女性の悲恋を描く国民文学起源作。", 5, "tier1", "rethinking"),
  ("マセード『モレニーニャ』詳論", "Macedo 'A Moreninha' detailed", "A Moreninha", P_BR_19,
   "1844年ブラジル都市ロマン主義小説の出発点。リオの中産階級風俗を軽妙に描く。", 4, "tier1", "invariant"),
  ("カストロ・アルヴェス『泡沫』", "Castro Alves 'Espumas Flutuantes'", "Espumas Flutuantes", P_BR_19,
   "1870年詩集。条件付奴隷解放運動を担った社会派ロマン派詩人の代表作。", 4, "tier1", "rethinking"),
  ("ビラック『午後』", "Bilac 'Tarde'", "Tarde", P_BR_19,
   "1919年詩集。ブラジル・パルナシスム代表詩人による完成期作品、形式美と抒情の融合。", 3, "tier1", "invariant"),
  ("クルス・イ・ソウザ『灯台』", "Cruz e Sousa 'Faróis'", "Faróis", P_BR_19,
   "1900年ブラジル象徴主義詩集。アフリカ系詩人による神秘主義的・音楽的詩学の最高峰。", 4, "tier1", "rethinking"),
  ("アウグスト・ドス・アンジョス『私』詳論", "Augusto dos Anjos 'Eu' detailed", "Eu", P_BR_POETRY,
   "1912年詩集。科学用語と退廃美学を融合、ブラジル詩史上最も独異な唯一の詩集。", 4, "tier1", "rethinking"),

  # Cluster 2: 19c女性
  ("アベリャネーダ『サブ』詳論", "Avellaneda 'Sab' detailed", "Sab", P_LATAM_19_F,
   "1841年キューバ反奴隷制小説。女性作家による先駆的人種・ジェンダー批判ロマン主義作。", 5, "tier1", "rethinking"),
  ("ゴリッティ『夢と現実』詳論", "Gorriti 'Sueños y realidades' detailed", "Sueños y realidades", P_LATAM_19_F,
   "1865年アルゼンチン女性作家短編集。亡命・先住民・女性経験を幻想的に交錯させる。", 4, "tier1", "rethinking"),
  ("マットー・デ・トゥルネル『巣のない鳥』詳論", "Matto 'Aves sin nido' detailed", "Aves sin nido", P_LATAM_19_F,
   "1889年ペルー女性作家による先駆的インディヘニスモ小説、聖職者批判と先住民擁護。", 5, "tier1", "rethinking"),
  ("ロサリオ・カステリャーノス『バルン・カナン』詳論", "Castellanos 'Balún Canán' detailed", "Balún Canán", P_20F,
   "1957年メキシコ先住民地主社会を女児視点から描く。ジェンダーと植民性の交差。", 5, "tier1", "rethinking"),
  ("ロサリオ・カステリャーノス『他者の文化としての女性』", "Castellanos 'Mujer que sabe latín'", "Mujer que sabe latín", P_20F,
   "1973年メキシコ・フェミニズム批評エッセイ。女性を文化的他者として位置づけた先駆的論考。", 4, "tier1", "rethinking"),
  ("ロサリオ・フェレ『甘き呪い』", "Ferré 'Maldito amor'", "Maldito amor", P_F21,
   "1986年プエルトリコ女性作家による家族・人種・植民地史を多声的に語る中編集。", 4, "tier1", "rethinking"),

  # Cluster 3: Modernismo
  ("シルバ『食卓の後で』詳論", "Silva 'De sobremesa' detailed", "De sobremesa", P_MOD,
   "1925年（執筆1896）コロンビア・モデルニスモ唯一長編。デカダンス耽美と都市疎外の日記体小説。", 4, "tier1", "rethinking"),
  ("ゴンサレス・プラダ『自由のページ』詳論", "González Prada 'Páginas libres' detailed", "Páginas libres", P_MOD,
   "1894年ペルー無政府主義的批評エッセイ集。先住民解放と教会批判を先駆的に展開。", 5, "tier1", "rethinking"),
  ("グティエレス・ナヘラ『色とりどりの物語』", "Gutiérrez Nájera 'Cuentos color de humo'", "Cuentos color de humo", P_MOD,
   "1894年メキシコ・モデルニスモ短編集。フランス象徴主義の影響下、都市の感受性を彫琢。", 3, "tier1", "invariant"),
  ("カサル『風の葉』", "Casal 'Hojas al viento'", "Hojas al viento", P_MOD,
   "1890年キューバ・モデルニスモ初期詩集。デカダンス的耽美と東洋趣味を融合。", 3, "tier1", "invariant"),
  ("ダリオ『青...』詳論", "Darío 'Azul...' detailed", "Azul...", P_MOD,
   "1888年ニカラグア発、イスパノアメリカ・モデルニスモの誕生を画した詩・散文集。", 5, "tier1", "rethinking"),
  ("ルゴーネス『感傷的月暦』詳論", "Lugones 'Lunario sentimental' detailed", "Lunario sentimental", P_MOD,
   "1909年アルゼンチン・モデルニスモ詩集。月モチーフで形式実験と前衛詩への橋渡し。", 4, "tier1", "rethinking"),

  # Cluster 4: 20c一般
  ("アストゥリアス『トウモロコシの人々』詳論", "Asturias 'Hombres de maíz' detailed", "Hombres de maíz", P_BOOM,
   "1949年グアテマラ。マヤ神話と土地収奪を魔術的リアリズムで結ぶ大地小説の到達点。", 5, "tier1", "rethinking"),
  ("ロア・バストス『至高の私』詳論", "Roa Bastos 'Yo el Supremo' detailed", "Yo el Supremo", P_BOOMSUP,
   "1974年パラグアイ独裁者小説の最高峰。フランシア博士の独白と多声で歴史言説を脱構築。", 5, "tier1", "rethinking"),
  ("カルペンティエル『この世の王国』詳論", "Carpentier 'El reino de este mundo' detailed", "El reino de este mundo", P_BOOM,
   "1949年ハイチ革命を素材に「驚異的現実」概念を提唱。ラテンアメリカ的歴史小説の起点。", 5, "tier1", "rethinking"),
  ("レサマ・リマ『パラディーソ』詳論", "Lezama Lima 'Paradiso' detailed", "Paradiso", P_BOOM,
   "1966年キューバ。バロック密度の隠喩で性・芸術・幼年期を融合した詩的全体小説。", 5, "tier1", "rethinking"),
  ("カブレラ・インファンテ『三匹の悲しき虎』詳論", "Cabrera Infante 'Tres tristes tigres' detailed", "Tres tristes tigres", P_BOOM,
   "1967年キューバ。ハバナ夜文化と言語遊戯で構成された反小説、口語的爆発の傑作。", 5, "tier1", "rethinking"),
  ("サルドゥイ『どこから来た歌い手たちか』詳論", "Sarduy 'De donde son los cantantes' detailed", "De donde son los cantantes", P_BOOMSUP,
   "1967年キューバ・ネオバロック小説。三人種同一性をパフォーマンス的に脱構築。", 4, "tier1", "rethinking"),

  # Cluster 5: 現代
  ("サエール『傷痕』詳論", "Saer 'Cicatrices' detailed", "Cicatrices", P_PB,
   "1969年アルゼンチン。サンタフェの殺人事件を四つの視点から多声的に再構成する小説。", 4, "tier1", "rethinking"),
  ("ピグリア『人工呼吸』詳論", "Piglia 'Respiración artificial' detailed", "Respiración artificial", P_POSTDIC,
   "1980年アルゼンチン軍政期に書かれた政治・文学批評を織り込んだ知的探偵小説。", 5, "tier1", "rethinking"),
  ("アイラ『エピソード』", "Aira 'Un episodio en la vida del pintor viajero'", "Un episodio en la vida del pintor viajero", P_PB,
   "2000年。画家ルガンダスのパンパ旅を描く中編、アイラの「逃走前進」詩学の代表作。", 4, "tier1", "rethinking"),
  ("エルティト『ルンペリカ』詳論", "Eltit 'Lumpérica' detailed", "Lumpérica", P_POSTDIC,
   "1983年チリ。ピノチェト独裁下、女性身体と広場を実験的散文で政治化したネオ前衛作。", 5, "tier1", "rethinking"),
  ("ボラーニョ『遠い星』詳論", "Bolaño 'Estrella distante' detailed", "Estrella distante", P_POSTDIC,
   "1996年チリ。詩人＝空軍パイロット殺人鬼を追う、独裁の美学と犯罪を結ぶ中編。", 5, "tier1", "rethinking"),
  ("バスケス『物の音』", "Vásquez 'El ruido de las cosas al caer'", "El ruido de las cosas al caer", P_MCONDO,
   "2011年コロンビア。麻薬戦争世代の記憶と暴力を内省的に再構成した現代小説。", 5, "tier1", "rethinking"),
]

def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted, skipped = 0, []
    for (nj, ne, no, pid, defn, imp, tier, fts) in CONCEPTS:
        try:
            cur.execute("""INSERT INTO concepts
                (name_ja, name_en, name_original, subfield_id, region, period_id, definition,
                 importance_score, source_tier, fourth_transform_status, canonical_in_region)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (nj, ne, no, SUBFIELD_ID, REGION, pid, defn, imp, tier, fts, "yes" if imp >= 5 else "no"))
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped.append((nj, str(e)))
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted}, Skipped: {len(skipped)}")
    for s in skipped:
        print("  SKIP:", s[0], "-", s[1])

if __name__ == "__main__":
    main()
