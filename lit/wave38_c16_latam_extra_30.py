#!/usr/bin/env python3
"""Wave 38: lit_latin_america (subfield_id=16) +30 deep niche concepts."""
import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), "lit.sqlite")
SF = 16
REGION = "ラテンアメリカ"

# period mapping (region=ラテンアメリカ)
P_BR_POESIA = 281      # ブラジル20世紀詩補完期
P_CARIBE = 227         # カリブ・スペイン語文学期 (使う: アンティル仏語も近接)
P_W21 = 288            # 21世紀ラテンアメリカ女性期
P_W21_2 = 232          # 21世紀女性作家期
P_VAN_DETAIL = 284     # Vanguardismo詳細期
P_MX_PAZ = 285         # メキシコ・パス期
P_BOOM_EXT = 224       # ラテンアメリカ・ブーム期拡張
P_INDIGE = 223         # インディヘニスモ期
P_19TH = 255           # 19世紀補完期

rows = [
    # Cluster 1: ブラジル詩細部 (P_BR_POESIA)
    ("ドラモンド『世界の感情』詳論", "Sentimento do Mundo", "Sentimento do Mundo", "latin", P_BR_POESIA,
     "1940年詩集。戦争前夜の集団的不安と詩人の連帯を平易な口語で描く。"),
    ("マヌエル・バンデイラ『ベロ・ベロ』", "Belo Belo", "Belo Belo", "latin", P_BR_POESIA,
     "1948年詩集。日常語と抒情の融合、生と死を軽みで歌う晩年バンデイラの結晶。"),
    ("セシーリア・メイレレス『絶対の海』", "Mar Absoluto", "Mar Absoluto", "latin", P_BR_POESIA,
     "1945年詩集。海と魂の象徴主義的瞑想、ポルトガル詩伝統と東洋的静謐を融合。"),
    ("ムリーロ・メンデス『時と永遠』詳論", "Tempo e Eternidade", "Tempo e Eternidade", "latin", P_BR_POESIA,
     "1935年Jorge de Lima共著。カトリック超現実主義、聖性と現代性の同時性を探究。"),
    ("パウロ・レミンスキー『カプリーチョス・イ・リラショス』", "Caprichos e Relaxos", "Caprichos e Relaxos", "latin", P_BR_POESIA,
     "1983年詩集。俳句・コンクレチズモ・ロックを混淆するクリチバ派代表作。"),
    ("アナ・クリスチナ・セザール『未刊詩集』", "Inéditos e Dispersos", "Inéditos e Dispersos", "latin", P_BR_POESIA,
     "1985年遺稿集。Geração Mimeógrafoの女性声、自伝・翻訳・断章の境界を撹乱する。"),

    # Cluster 2: アンティル諸島文学 (P_CARIBE)
    ("セゼール『故郷帰還ノート』", "Cahier d'un retour au pays natal", "Cahier d'un retour au pays natal", "latin", P_CARIBE,
     "1939年長詩。ネグリチュード宣言、マルティニーク回帰と植民地批判の叙事的告白。"),
    ("グリッサン『全=世界』", "Tout-Monde", "Tout-Monde", "latin", P_CARIBE,
     "1993年小説。クレオリザシオン哲学を物語化、関係性の詩学を多声小説で実装。"),
    ("シャモワゾー『テキサコ』", "Texaco", "Texaco", "latin", P_CARIBE,
     "1992年Goncourt賞。フォール=ド=フランス貧民街の口承クレオール語小説。"),
    ("マリーズ・コンデ『セグー』", "Ségou", "Ségou", "latin", P_CARIBE,
     "1984-85年大河小説。バンバラ王国崩壊と離散黒人の三大陸サーガ。"),
    ("シュワルツ=バル『テリュメ・ミラクル』", "Pluie et vent sur Télumée Miracle", "Pluie et vent sur Télumée Miracle", "latin", P_CARIBE,
     "1972年小説。グアドループ女性四世代の口承的語り、奴隷制記憶と精神的尊厳。"),
    ("ジャック・ルーマン『露の主』", "Gouverneurs de la rosée", "Gouverneurs de la rosée", "latin", P_CARIBE,
     "1944年ハイチ小説。農村共同労働コンビット、社会主義的人民詩学の古典。"),

    # Cluster 3: 現代女性詩・回想 (P_W21 / P_W21_2)
    ("ペリ・ロッシ『亡命の状態』", "Estado de exilio", "Estado de exilio", "latin", P_W21,
     "2003年詩集。ウルグアイ亡命40年の総決算、政治と身体の二重亡命を凝視。"),
    ("イデア・ビラリーニョ『ペヌルティモ詩』", "Poemas de amor / Anteúltimos", "Poemas anteúltimos", "latin", P_W21_2,
     "1962-1980年詩。ミニマルな愛の言語、ウルグアイ45年世代女性の最深部。"),
    ("ブランカ・バレラ『動物のコンシエルト』", "Concierto animal", "Concierto animal", "latin", P_W21_2,
     "1999年詩集。ペルー女性詩の頂点、肉体と動物性の暗い祝祭を低声で響かせる。"),
    ("オルガ・オロスコ『ベレニーチェの歌』", "Cantos a Berenice", "Cantos a Berenice", "latin", P_W21_2,
     "1977年詩集。死んだ猫への挽歌連作、グノーシス的悼みの儀礼詩。"),
    ("マロサ・ディ・ジョルジオ『野菜の記憶』", "La liebre de marzo / Memoria hortelana", "Memoria hortelana", "latin", P_W21_2,
     "ウルグアイ農園を舞台にしたエロティック散文詩、植物的官能の幻視譚。"),
    ("タマラ・カメンスサイン『エロス・フルティーリャ』", "Eros, frutilla", "Eros, frutilla", "latin", P_W21,
     "アルゼンチン詩人による日常エロスの詩、ネオ・オブヘティビスモの女性版。"),

    # Cluster 4: メキシコ詩・実験 (P_MX_PAZ)
    ("パス『ブランコ』", "Blanco", "Blanco", "latin", P_MX_PAZ,
     "1967年長詩。マラルメ＋密教、巻物形式で空白と複数読みを構造化した実験詩。"),
    ("コラル・ブラチョ『さまよう大地』", "El ser que va a morir / Tierra de entraña ardiente", "Tierra donde vagamos", "latin", P_MX_PAZ,
     "メキシコ女性詩、官能的物質性と流動するイメージで言語の触覚を再定義。"),
    ("ダビ・ウエルタ『不治』", "Incurable", "Incurable", "latin", P_MX_PAZ,
     "1987年長詩。389頁の散文詩巨編、メキシコ80年代の存在論的崩壊を全包囲。"),
    ("パチェコ『私に聞かないで時間がどう流れるか』", "No me preguntes cómo pasa el tiempo", "No me preguntes cómo pasa el tiempo", "latin", P_MX_PAZ,
     "1969年詩集。歴史と日常の崩壊感覚、Tlatelolco以後の倫理的詩学。"),
    ("ベロニカ・ボルコフ『海岸とインク』", "Litoral de tinta", "Litoral de tinta", "latin", P_MX_PAZ,
     "メキシコ女性詩。書字と海の境界を探る瞑想、Trotsky曾孫としての歴史継承。"),
    ("テディ・ロペス・ミルス『註解と断章』", "Glosas / Fragmentos", "Glosas y Fragmentos", "latin", P_MX_PAZ,
     "メキシコ現代女性詩。哲学的散文詩、Wittgenstein/Stein系統の断章構成。"),

    # Cluster 5: ガウーチョ・伝統 (P_19TH / P_INDIGE / P_BOOM_EXT)
    ("エルナンデス『マルティン・フィエロ』詳細", "Martín Fierro", "Martín Fierro", "latin", P_19TH,
     "1872/1879年。ガウチェスコ叙事詩の頂点、Vuelta含む二部構成と国民神話化。"),
    ("グイラルデス『ドン・セグンド・ソンブラ』詳細", "Don Segundo Sombra", "Don Segundo Sombra", "latin", P_INDIGE,
     "1926年小説。消えゆくガウチョを少年視点で詩化、近代化前夜の挽歌。"),
    ("オネッティ『造船所』詳論", "El astillero", "El astillero", "latin", P_BOOM_EXT,
     "1961年小説。サンタ・マリア物語群の核、廃墟造船所を舞台にした実存的虚構。"),
    ("ドノソ『卑猥な夜の鳥』詳論", "El obsceno pájaro de la noche", "El obsceno pájaro de la noche", "latin", P_BOOM_EXT,
     "1970年小説。チリ・バロック狂気、imbunche(縫合)とミューテーションの大伽藍。"),
    ("ロア・バストス『人の子』", "Hijo de hombre", "Hijo de hombre", "latin", P_BOOM_EXT,
     "1960年小説。パラグアイ受難史、グアラニ語層と聖書的犠牲のクレオール叙事詩。"),
    ("アストゥリアス『トウモロコシの人々』", "Hombres de maíz", "Hombres de maíz", "latin", P_INDIGE,
     "1949年小説。Popol Vuh神話を基層、グアテマラ先住民魔術的リアリズムの源泉。"),
]

assert len(rows) == 30, len(rows)

con = sqlite3.connect(DB)
cur = con.cursor()
inserted = 0
skipped = 0
for name_ja, name_en, name_orig, script, period_id, definition in rows:
    assert len(definition) <= 100, (len(definition), definition)
    try:
        cur.execute("""
            INSERT INTO concepts (name_ja, name_en, name_original, original_script,
                                  subfield_id, region, period_id, definition, importance_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 3)
        """, (name_ja, name_en, name_orig, script, SF, REGION, period_id, definition))
        inserted += 1
    except sqlite3.IntegrityError as e:
        skipped += 1
        print(f"SKIP {name_ja}: {e}")
con.commit()
total = cur.execute("SELECT COUNT(*) FROM concepts WHERE subfield_id=?", (SF,)).fetchone()[0]
con.close()
print(f"Wave38 c16 latam_extra: inserted={inserted} skipped={skipped} total_subfield={total}")
