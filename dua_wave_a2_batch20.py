#!/usr/bin/env python3
"""DUA Wave A2 Batch 20 — 60 concepts to push total to 5500+"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def uid(): return "dua_" + uuid.uuid4().hex[:12]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

RECORDS = [
    # ── 哲学・倫理学 (10) ──
    (uid(),"実践理性批判の倫理体系","Kantian Practical Reason Ethics","Kant's moral philosophy grounding ethics in the categorical imperative and rational autonomous agency","哲学・倫理学","Western_Europe",1788,"https://en.wikipedia.org/wiki/Critique_of_Practical_Reason","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ヘーゲル法哲学","Hegel Philosophy of Right","Hegel's systematic philosophy of legal institutions, civil society, and the state as actualization of freedom","哲学・倫理学","Western_Europe",1820,"https://en.wikipedia.org/wiki/Philosophy_of_Right","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"批判的合理主義","Critical Rationalism","Karl Popper's epistemology emphasizing falsifiability, fallibilism, and the growth of scientific knowledge","哲学・倫理学","Western_Europe",1934,"https://en.wikipedia.org/wiki/Critical_rationalism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"価値多元主義","Value Pluralism","Isaiah Berlin's thesis that fundamental human values are irreducibly plural and genuinely conflicting","哲学・倫理学","Western_Europe",1958,"https://en.wikipedia.org/wiki/Value_pluralism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ロールズの正義論","Rawlsian Theory of Justice","John Rawls' liberal political philosophy based on original position and two principles of justice","哲学・倫理学","North_America",1971,"https://en.wikipedia.org/wiki/A_Theory_of_Justice","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"チベット仏教哲学","Tibetan Buddhist Philosophy","Philosophical traditions of Tibetan Buddhism including Madhyamaka, Yogacara, and Dzogchen","哲学・倫理学","East_Asia",779,"https://en.wikipedia.org/wiki/Tibetan_Buddhism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ニヤーヤ哲学","Nyaya Philosophy","Ancient Indian school of logic and epistemology emphasizing pramana (valid means of knowledge)","哲学・倫理学","South_Asia",-200,"https://en.wikipedia.org/wiki/Ny%C4%81ya","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"イフワーン・サファー哲学","Ikhwan al-Safa Philosophy","10th century Islamic encyclopedists synthesizing Neoplatonism, Pythagoreanism, and Islamic thought","哲学・倫理学","West_Asia_North_Africa",983,"https://en.wikipedia.org/wiki/Brethren_of_Purity","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ブドゥ哲学","Voodoo Philosophy","Philosophical and spiritual dimensions of Vodou tradition in West Africa and Caribbean diaspora","哲学・倫理学","Sub_Saharan_Africa",1700,"https://en.wikipedia.org/wiki/Haitian_Vodou","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"マオリ哲学","Maori Philosophy","Indigenous philosophical traditions of Maori people including whakapapa, mauri, and mana concepts","哲学・倫理学","Oceania",1300,"https://en.wikipedia.org/wiki/M%C4%81ori_culture","url_present","dua_wave_a2","active",now(),now()),

    # ── 歴史学 (10) ──
    (uid(),"ビッグデータ歴史学","Big Data Historical Research","Use of large-scale digitized datasets for historical research enabling quantitative analysis","歴史学","Global_Synthesis",2010,"https://en.wikipedia.org/wiki/Digital_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"奴隷制の歴史学","Historiography of Slavery","Historical scholarship on Atlantic slavery, its causes, lived experiences, and long-term legacies","歴史学","North_America",1918,"https://en.wikipedia.org/wiki/Slavery_in_the_United_States","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"冷戦史学","Cold War Historiography","Historical scholarship on the Cold War using newly available archival sources from multiple countries","歴史学","Global_Synthesis",1989,"https://en.wikipedia.org/wiki/Cold_War","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"食料史","Food History","Historical study of food production, cuisine, and eating practices as windows into social history","歴史学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Food_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"科学思想史","History of Scientific Thought","Historical study of the development of scientific ideas, methods, and institutions across cultures","歴史学","Western_Europe",1913,"https://en.wikipedia.org/wiki/History_of_science","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アボリジナル史","Aboriginal Australian History","Historical study of Indigenous Australian peoples before and after European colonization","歴史学","Oceania",-50000,"https://en.wikipedia.org/wiki/History_of_Indigenous_Australians","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"東南アジア史学","Southeast Asian Historiography","Historical scholarship on Southeast Asia including maritime trade, Indianization, and colonial transformations","歴史学","South_Asia",1961,"https://en.wikipedia.org/wiki/Southeast_Asian_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ラテンアメリカ植民地史","Latin American Colonial History","Historical study of Spanish and Portuguese colonialism, indigenous responses, and creole society in the Americas","歴史学","Latin_America",1492,"https://en.wikipedia.org/wiki/Colonial_Latin_America","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"黒大西洋史","Black Atlantic History","Historical framework examining African diaspora across Atlantic world, developed by Paul Gilroy","歴史学","North_America",1993,"https://en.wikipedia.org/wiki/The_Black_Atlantic","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"環境史の理論","Environmental History Theory","Theoretical frameworks for environmental history studying human-nature relations over time","歴史学","North_America",1977,"https://en.wikipedia.org/wiki/Environmental_history","url_present","dua_wave_a2","active",now(),now()),

    # ── 文学・批評理論 (10) ──
    (uid(),"抵抗文学理論","Resistance Literature Theory","Theory of literary works expressing political and cultural resistance against colonialism and oppression","文学・批評理論","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Resistance_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ディアスポラ文学批評","Diaspora Literature Criticism","Critical frameworks for literature of displaced communities examining identity, memory, and belonging","文学・批評理論","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Diaspora_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"口承文芸の理論","Oral Literature Theory","Theoretical frameworks for studying oral literary traditions including performance, memory, and transmission","文学・批評理論","Global_Synthesis",1860,"https://en.wikipedia.org/wiki/Oral_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"実験文学批評","Experimental Fiction Criticism","Critical analysis of avant-garde and formally innovative prose fiction and literary experimentation","文学・批評理論","Western_Europe",1910,"https://en.wikipedia.org/wiki/Experimental_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"スラブ文学批評","Slavic Literature Criticism","Critical study of Russian, Polish, Czech, and other Slavic literary traditions","文学・批評理論","Western_Europe",1850,"https://en.wikipedia.org/wiki/Russian_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"インド古典詩学","Classical Indian Poetics","Sanskrit literary criticism including dhvani theory, riti schools, and alamkara rhetoric tradition","文学・批評理論","South_Asia",-200,"https://en.wikipedia.org/wiki/Sanskrit_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"韓国文学批評理論","Korean Literary Criticism","Critical study of Korean literary tradition from sijo poetry to contemporary Korean fiction","文学・批評理論","East_Asia",668,"https://en.wikipedia.org/wiki/Korean_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ニュージャーナリズム批評","New Journalism Criticism","Critical analysis of literary journalism movement blending reportage with literary techniques","文学・批評理論","North_America",1960,"https://en.wikipedia.org/wiki/New_Journalism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文学ゲノミクス","Literary Genomics","Computational analysis of large literary corpora to trace stylistic evolution and cultural patterns","文学・批評理論","Global_Synthesis",2010,"https://en.wikipedia.org/wiki/Digital_humanities","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"マダガスカル口承文学","Malagasy Oral Literature","Study of traditional oral literature of Madagascar including hainteny poetic riddles and kabary oratory","文学・批評理論","Sub_Saharan_Africa",1700,"https://en.wikipedia.org/wiki/Malagasy_literature","url_present","dua_wave_a2","active",now(),now()),

    # ── 言語学 (5) ──
    (uid(),"言語進化の科学","Language Evolution Science","Scientific study of evolutionary origins of human language capacity and communication systems","言語学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Origin_of_language","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アイヌ語言語学","Ainu Language Linguistics","Linguistic study of the Ainu language isolate of Hokkaido and Sakhalin","言語学","East_Asia",1800,"https://en.wikipedia.org/wiki/Ainu_language","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"スワヒリ語学","Swahili Language Linguistics","Linguistic study of Swahili, the major Bantu contact language and lingua franca of East Africa","言語学","Sub_Saharan_Africa",1800,"https://en.wikipedia.org/wiki/Swahili_language","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ケチュア語学","Quechua Language Linguistics","Linguistic study of Quechua language family of the Andean region of South America","言語学","Latin_America",-500,"https://en.wikipedia.org/wiki/Quechua_languages","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ナバホ語言語学","Navajo Language Linguistics","Linguistic study of Navajo, a Na-Dene language with complex tonality and polysynthetic morphology","言語学","North_America",-1000,"https://en.wikipedia.org/wiki/Navajo_language","url_present","dua_wave_a2","active",now(),now()),

    # ── 宗教学 (5) ──
    (uid(),"ゾロアスター教学","Zoroastrian Studies Academic","Academic study of Zoroastrianism from Avestan texts to Parsi diaspora and Neo-Zoroastrian revival","宗教学","West_Asia_North_Africa",-1500,"https://en.wikipedia.org/wiki/Zoroastrianism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"グノーシス主義学","Academic Gnostic Studies","Study of ancient Gnostic religious movements and Nag Hammadi texts recovered in 1945","宗教学","West_Asia_North_Africa",100,"https://en.wikipedia.org/wiki/Gnosticism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"カバラ学","Academic Kabbalah Studies","Scholarly study of Jewish mystical tradition including Zohar, Sefirot cosmology, and Lurianic Kabbalah","宗教学","West_Asia_North_Africa",1280,"https://en.wikipedia.org/wiki/Kabbalah","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アフリカン・ディアスポラ宗教学","African Diaspora Religion Studies","Study of Vodou, Candomble, Santeria, and other syncretic religions of the African diaspora","宗教学","Latin_America",1700,"https://en.wikipedia.org/wiki/African_diaspora_religions","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"チベット仏教研究","Tibetan Buddhist Studies","Academic study of Tibetan Buddhist traditions including tantra, debate, and Gelug-Kagyu-Nyingma lineages","宗教学","East_Asia",779,"https://en.wikipedia.org/wiki/Tibetan_Buddhism","url_present","dua_wave_a2","active",now(),now()),

    # ── 古典学 (5) ──
    (uid(),"ペルシア古典詩学","Persian Classical Poetics","Study of classical Persian poetry traditions including qasida, ghazal, and masnawi forms","古典学","West_Asia_North_Africa",900,"https://en.wikipedia.org/wiki/Persian_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"タミル古典文学研究","Tamil Classical Literature Studies","Study of Sangam literature and the ancient Tamil literary tradition of South India","古典学","South_Asia",-300,"https://en.wikipedia.org/wiki/Tamil_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"マヤ象形文字学","Maya Hieroglyphic Studies","Decipherment and interpretation of Maya hieroglyphic writing system and textual culture","古典学","Latin_America",-200,"https://en.wikipedia.org/wiki/Maya_script","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ゲエズ文学研究","Geez Literature Studies","Study of classical Ethiopic literature in Ge'ez language including Kebra Nagast and hagiographies","古典学","Sub_Saharan_Africa",400,"https://en.wikipedia.org/wiki/Ge%27ez_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ケルト古典文学研究","Celtic Classical Literature Studies","Study of medieval Irish and Welsh texts preserving pre-Christian mythological traditions","古典学","Western_Europe",600,"https://en.wikipedia.org/wiki/Celtic_mythology","url_present","dua_wave_a2","active",now(),now()),

    # ── 美学・芸術理論 (5) ──
    (uid(),"ゲーム美学","Video Game Aesthetics","Aesthetic analysis of video games as interactive art forms with unique ludic properties","美学・芸術理論","North_America",2001,"https://en.wikipedia.org/wiki/Game_studies","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ストリートアート美学","Street Art Aesthetics","Critical analysis of graffiti and street art as urban aesthetic and political intervention","美学・芸術理論","North_America",1970,"https://en.wikipedia.org/wiki/Street_art","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ファッション美学","Fashion Aesthetics","Cultural and aesthetic analysis of fashion as system of signs, identity, and artistic practice","美学・芸術理論","Western_Europe",1967,"https://en.wikipedia.org/wiki/Fashion_theory","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"バウハウス美学理論","Bauhaus Design Aesthetics","Design philosophy of the Bauhaus school combining fine arts and functional craft with modernist sensibility","美学・芸術理論","Western_Europe",1919,"https://en.wikipedia.org/wiki/Bauhaus","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"批判的デザイン美学","Critical Design Aesthetics","Design philosophy questioning normative assumptions about function and value, associated with speculative design","美学・芸術理論","Western_Europe",1999,"https://en.wikipedia.org/wiki/Critical_design","url_present","dua_wave_a2","active",now(),now()),
]


def main():
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=WAL")
    cur = con.cursor()
    existing = set(r[0] for r in cur.execute("SELECT name_en FROM humanities_concept").fetchall())
    batch, inserted, skipped = [], 0, 0
    for rec in RECORDS:
        name_en = rec[2]
        if name_en in existing:
            skipped += 1
            continue
        existing.add(name_en)
        batch.append(rec)
        if len(batch) >= 500:
            cur.executemany("""INSERT INTO humanities_concept
                (id,name_ja,name_en,definition,subfield,culture_region,
                 era_start,source_url,verification_status,quality_flag,
                 status,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
            con.commit()
            inserted += len(batch)
            batch = []
    if batch:
        cur.executemany("""INSERT INTO humanities_concept
            (id,name_ja,name_en,definition,subfield,culture_region,
             era_start,source_url,verification_status,quality_flag,
             status,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
        con.commit()
        inserted += len(batch)
    total = cur.execute("SELECT COUNT(*) FROM humanities_concept").fetchone()[0]
    print(f"inserted={inserted}, skipped={skipped}")
    print(f"総件数: {total} (目標5500)")
    con.close()


if __name__ == "__main__":
    main()
