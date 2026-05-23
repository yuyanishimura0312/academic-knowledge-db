"""DUA Wave A2 Patch — need exactly 7 more inserts to hit 5,500"""
import sqlite3, uuid, datetime

DB_PATH = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def insert_batch(concepts):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0; skipped = 0
    for c in concepts:
        name_ja, name_en, name_orig, defn, subfield, school, era, region, url = c
        cur.execute("SELECT COUNT(*) FROM social_theory WHERE name_en=?", (name_en,))
        if cur.fetchone()[0] > 0:
            skipped += 1; continue
        uid = str(uuid.uuid4())
        now = datetime.datetime.utcnow().isoformat()
        cur.execute("""INSERT INTO social_theory
            (id,name_ja,name_en,name_original,definition,subfield,school_of_thought,
             era_start,culture_region,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,'url_present','B','active',?,?)""",
            (uid,name_ja,name_en,name_orig,defn,subfield,school,era,region,url,now,now))
        inserted += 1
    conn.commit(); conn.close()
    return inserted, skipped

concepts = [
    ("文化的混合主義","Cultural Syncretism","","異なる文化体系の要素が接触・融合して新たな文化形態を生み出すプロセス。宗教・音楽・料理など多領域で観察される。","文化社会学・知識社会学","文化変容論",1935,"Global_Synthesis","https://en.wikipedia.org/wiki/Syncretism"),
    ("モラル・パニック","Moral Panic","","スタンリー・コーエンが1972年に定式化した概念。社会の一部が特定の集団や行動を脅威として急激に反応・道徳化するプロセス。","文化社会学・知識社会学","逸脱社会学",1972,"Western_Europe","https://en.wikipedia.org/wiki/Moral_panic"),
    ("コモンセンスの政治学","Politics of Common Sense","","スチュアート・ホールらが論じた、イデオロギーが「当然のこと」として自然化される過程。サッチャリズム分析で展開された。","批判理論・フランクフルト学派","カルチュラルスタディーズ",1988,"Western_Europe","https://en.wikipedia.org/wiki/Stuart_Hall_(cultural_theorist)"),
    ("ポスト世俗主義","Post-Secularism","","ハーバーマス・テイラーらが議論した、宗教が近代公共圏に再登場する現象。世俗化テーゼの再検討として注目される。","政治社会学・国家論","政治社会学",2001,"Western_Europe","https://en.wikipedia.org/wiki/Post-secular_society"),
    ("アフリカ的社会主義","African Socialism","","ニエレレ（タンザニア）・セングール（セネガル）らが唱えた、アフリカ固有の共同体的価値観に基づく社会主義。脱植民地化と開発の文脈で提唱された。","ポストコロニアル・脱植民地理論","アフリカ社会主義",1960,"Sub_Saharan_Africa","https://en.wikipedia.org/wiki/African_socialism"),
    ("ランドスケープ生態学の社会学的応用","Social Dimensions of Landscape Ecology","","土地利用・景観変化が社会関係・文化的アイデンティティ・権力と結びつく様式を分析する、環境社会学と景観生態学の交差領域。","環境社会学・人新世","環境社会学",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Landscape_ecology"),
    ("デジタル記憶とアーカイブ","Digital Memory and Archives","","デジタル技術が集合的記憶・歴史叙述・文化遺産の保存と忘却をどのように変容させるかを分析する研究領域。","デジタル社会学・ネットワーク社会","デジタル社会学",2010,"Global_Synthesis","https://en.wikipedia.org/wiki/Digital_preservation"),
    ("認知的正義","Cognitive Justice","","ボアベントゥラ・デ・ソウザ・サントスが提唱した、知識の多元性と異なる認識の仕方への権利。南半球の知識を周縁化するグローバルな知識秩序への抵抗概念。","ポストコロニアル・脱植民地理論","脱植民地理論",2000,"Global_Synthesis","https://en.wikipedia.org/wiki/Cognitive_justice"),
    ("フォーマル組織とインフォーマル組織","Formal and Informal Organization","","チェスター・バーナードらが分析した、公式的組織構造と非公式なネットワーク・規範・慣行との相互作用。組織社会学の基礎概念。","古典社会学","組織社会学",1938,"North_America","https://en.wikipedia.org/wiki/Informal_organization"),
    ("性の政治経済学","Political Economy of Sexuality","","ゲイル・ルービン・ジュディス・バトラーらが展開した、セクシュアリティが経済・政治的構造と結びつく様式を分析する枠組み。","フェミニズム・ジェンダー理論","クィア理論",1984,"North_America","https://en.wikipedia.org/wiki/Political_economy_of_sex"),
]

if __name__ == "__main__":
    print(f"Inserting {len(concepts)} concepts (Patch Final)...")
    ins, skp = insert_batch(concepts)
    print(f"Done. Inserted: {ins}, Skipped: {skp}")
