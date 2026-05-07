#!/usr/bin/env python3
"""Phase 7 Codex dispatcher: axis-diversified prompts for 60 workers.

Different axes per bucket:
- Princeton Encyclopedia of Poetry & Poetics canon
- Routledge Handbook of Narrative
- Specific anthology focus
- Lesser-known but canonical authors
"""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT_DIR = Path("/tmp/poetics_texts_p7")
LOG_DIR = Path("/tmp/poetics_texts_p7_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

PER_WORKER = 60

# Each tuple: (worker_id, culture_region, era_period, language, axis_description)
WORKER_TASKS = [
    # Greek-Roman: 8 workers, different axes
    ("GR_perseus_lesser", "古代ギリシャ・ローマ", "Greek archaic-classical", "grc", "lesser-known canonical Greek poets cited in Perseus Digital Library: Bacchylides odes, Stesichorus, Ibycus, Anacreon longer fragments, Simonides epitaphs, Tyrtaeus, Mimnermus, Theognis sympotic elegies, Phocylides, Solon's elegies, Xenophanes, Empedocles philosophical fragments, Parmenides, Pratinas"),
    ("GR_hellenistic_deep", "古代ギリシャ・ローマ", "hellenistic", "grc", "Hellenistic poets beyond Theocritus: Herodas Mimes, Erinna, Anyte, Nossis, Moschus' Europa, Bion's Adonis, Lycophron's Alexandra, Aratus Phaenomena, Nicander Theriaca, Asclepiades epigrams, Posidippus, Leonidas of Tarentum, Antipater of Sidon"),
    ("GR_anthology_full", "古代ギリシャ・ローマ", "Hellenistic-Imperial", "grc", "Greek Anthology epigrams from books 5-12: love (Meleager, Asclepiades), funerary (Simonides, Antipater), votive, declamatory, satirical (Lucillius, Nicarchus), pederastic (Strato), Christian (Gregory of Nazianzus), 60 representative epigrams"),
    ("LAT_silver_age", "古代ギリシャ・ローマ", "Imperial Roman", "lat", "Silver Age Latin: Lucan Pharsalia all 10 books, Statius Thebaid+Achilleid+Silvae, Silius Italicus Punica, Valerius Flaccus Argonautica, Manilius Astronomica, Phaedrus Fables, Petronius Satyricon poems, Calpurnius Siculus eclogues"),
    ("LAT_christian_late", "古代ギリシャ・ローマ", "Late Antique", "lat", "Late Antique Christian Latin: Prudentius Cathemerinon+Peristephanon+Psychomachia, Sedulius Carmen Paschale, Juvencus, Paulinus of Nola, Commodian, Avitus, Dracontius, Boethius all 5 books Consolation meters, Venantius Fortunatus full hymns Pange/Vexilla"),
    ("LAT_neo_latin", "中世ヨーロッパ", "Carolingian-Medieval", "lat", "Carolingian and medieval Latin: Alcuin, Theodulf, Walafrid Strabo, Hrabanus Maurus, Notker Balbulus, Hroswitha, Gottschalk, Sedulius Scottus, Goliards, Archpoet Confession, Hugh Primas, Walter of Chatillon"),
    ("GR_orphic_hymn", "古代ギリシャ・ローマ", "Imperial Greek", "grc", "Orphic Hymns 87 poems plus Hermetic poems and Sibylline Oracles selections - mystical/oracular Greek poetry"),
    ("GR_tragedy_full", "古代ギリシャ・ローマ", "Classical Greek", "grc", "Greek tragedy choral odes deep dive: Aeschylus all 7 plays choruses (Persians, Seven Against Thebes, Suppliants, Agamemnon, Choephori, Eumenides, Prometheus), Sophocles all 7 (Ajax, Antigone, OT, Electra, Trachiniae, Philoctetes, OC), Euripides 18+ extant"),

    # Chinese: 7 workers
    ("CHN_quan_tang_1", "中国古典", "Tang", "lzh", "全唐詩 representative selections from minor Tang poets not in 唐詩三百首: 王勃 全集, 駱賓王, 楊炯, 盧照鄰, 沈佺期, 宋之問, 賀知章, 張若虛, 王翰, 王灣, 張九齡 minor works, 高適 marches, 岑参 frontiers"),
    ("CHN_quan_tang_2", "中国古典", "Mid-Tang", "lzh", "中唐詩人: 韓愈 全集 (Mountain rocks/Autumn meditations), 柳宗元 (Yongzhou exile poems), 孟郊 (Withered Trees suite), 賈島 (Lookout for Recluse), 李賀 鬼才 (Magic Strings), 元稹 (Gathering at Yueyang), 白居易 諷諭詩 (Old Charcoal Seller, Salt Merchant's Wife)"),
    ("CHN_late_tang", "中国古典", "Late Tang", "lzh", "晩唐: 李商隠 全106首 (Untitled poems sequence 1-7, Brocade Zither), 杜牧 (Red Cliff, Garden Stroll), 温庭筠 詞 (Bodhisattva Barbarian sequences), 韋荘, 皮日休, 陸亀蒙, 司空図 詩品24章 critical poetry, 羅隠"),
    ("CHN_song_ci_1", "中国古典", "Song Ci", "lzh", "宋詞: 晏殊 (Honglou waixi), 晏幾道 (Linjiangxian rememberer), 柳永 30 ci (Yulin ling, Ying tianchang), 蘇軾 ci 30 (Shuidiao gettou, Niannujiao chibi, Dingfengbo), 黃庭堅, 周邦彥 (Lan ling wang willow)"),
    ("CHN_song_ci_2", "中国古典", "Southern Song", "lzh", "南宋詞: 李清照 ci 30 (Drunk in Flower Shadow, Like a Dream remembering Xitting, As if dreaming Yuan Xi, Slow Slow song full), 辛棄疾 ci 30 (Yongyu yue, Pixiao Pu, Pojzenzi for Chen Tongfu), 陸游 (Hairpin Phoenix Shen Yuan), 姜夔 (Yangzhou slow), 史達祖, 呉文英, 王沂孫"),
    ("CHN_yuan_qu", "中国古典", "Yuan", "lzh", "元曲 散曲套曲 Yuan dynasty arias: 関漢卿 (Doue Yuan, Wang Jiangting, Mountain Slope sheep), 馬致遠 (Tianjing sha, Ye xing chuan autumn thoughts, Han gong qiu), 王実甫 (Xiaxiang ji excerpts), 白樸, 鄭光祖, 喬吉, 張可久, 貫雲石, 喬夢符"),
    ("CHN_ming_qing_classic", "中国古典", "Ming-Qing", "lzh", "明清詩詞: 高啓 (Plum Blossoms 9), 楊基, 唐寅 (Drunk in Floral Dream), 文徴明, 王士禎 神韻派, 朱彝尊 詞, 厲鶚, 納蘭性徳 全140首詞 deep dive, 王國維 人間詞 (Yiyu cai sang zi)"),

    # Japanese: 5 workers
    ("JP_manyoshu_deep", "日本古典", "上代", "ojp", "万葉集 全20巻 across all volumes: 巻一国見 to 巻二十防人歌, 各巻代表20首. 柿本人麻呂 traveler sequences, 大伴家持 春愁三首 senshu, 山上憶良 貧窮問答 full, 山部赤人 富士, 大伴旅人 thirteen sake songs, 高市黒人, 額田王, 笠郎女, 笠金村, 沙弥満誓, 防人歌, 東歌"),
    ("JP_kokin_chokusen", "日本古典", "平安", "ojp", "勅撰和歌集: 古今集 (cherry blossoms 春上下 100, autumn leaves 秋上下), 後撰集, 拾遺集, 後拾遺集, 金葉集, 詞花集, 千載集, 新勅撰集 — 各歌集から代表50-100首"),
    ("JP_chusei_renga_haikai", "日本古典", "中世-近世", "ojp/jpn", "中世連歌・俳諧: 二条良基 連歌新式, 宗祇 水無瀬三吟, 心敬 ささめごと, 宗鑑 犬筑波集, 荒木田守武 千句俳諧, 松永貞徳 御傘, 西山宗因 蚊柱百句; 江戸俳諧: 芭蕉 七部集 (Sarumino, Sumidawara, Tsumako misago, Hisago, Arano, Kohaikai, Aki-no-hi)"),
    ("JP_hyakunin", "日本古典", "中世", "ojp", "百人一首 全100首詳細 (天智天皇 to 順徳院), each with proper 5-line short, hyakunin secchu commentary"),
    ("JP_kindai_shi", "日本古典", "近代", "jpn", "近代詩・自由詩: 北原白秋 邪宗門+思ひ出+桐の花, 萩原朔太郎 月に吠える+青猫+純情小曲集, 高村光太郎 道程+智恵子抄+猛獣篇, 室生犀星 抒情小曲集, 中原中也 山羊の歌+在りし日の歌, 立原道造 萱草に寄す, 三好達治 測量船, 草野心平, 八木重吉, 安西冬衛, 福士幸次郎"),

    # Sanskrit / Buddhist: 4 workers
    ("SAN_kavya_deep", "サンスクリット", "古典サンスクリット", "san", "Sanskrit kavya: Magha Shishupalavadha 20 sargas with 1 verse each, Bharavi Kiratarjuniya 18 cantos, Sri Harsha Naishadhacarita 22 cantos, Bhavabhuti Uttararamacharita+Mahaviracharita verses, Padma's Vajjalagga, Rupa Goswami Haribhakti-rasamrita, Govardhana Aryasaptasati"),
    ("SAN_bhakti_dohra", "サンスクリット", "中世インド", "san/hi/bn", "Bhakti poetry: Kabir 100 dohas, Tulsidas Ramcharitmanas all 7 kands, Surdas Sursagar bal-leela, Mirabai bhajan 50, Chaitanya, Dadu, Raidas, Ramdas, Tukaram abhang, Eknath, Chandidas Vaishnav padavali, Vidyapati"),
    ("BUD_full_dhammapada", "仏典詩偈", "原始仏教", "pli", "Dhammapada all 423 verses (sample 50 representatives across 26 vaggas), Suttanipata Atthaka+Parayana vagga full, Theragatha selected 30 from 264 long-elder verses, Therigatha 30 from 73, Udana paticca-samuppada vatthu, Itivuttaka brahmana sutta verses"),
    ("BUD_mahayana", "仏典詩偈", "大乗仏教-禅", "lzh/jpn", "大乗・禅偈: 法華経偈頌 (序品/方便品/譬喻品/化城喻品/従地涌出品/如来寿量品/普門品), 華厳経入法界品 53善知識偈, 維摩経偈, 楞伽経偈, 永嘉玄覚 證道歌全, 寒山詩 50首, 道元 山水経・有時, 白隠 坐禅和讃全, 良寛漢詩 30, 一遍 一遍上人語録偈"),

    # Persian / Arabic: 4 workers
    ("PER_classical_complete", "アラビア・ペルシア", "Persian classical", "fas", "Persian classical: Ferdowsi Shahnameh 50 episodes from each section, Hafez 100 of 495 ghazals, Saadi Bustan 10 chapters + Gulistan 8 babs, Rumi Masnavi 6 books with 5 stories each + Diwan-e Shams 30 ghazals, Attar Mantiq al-Tayr 30 hikayat, Khayyam Rubaiyat 50, Nezami Khamsa each work, Jami Haft Awrang 7, Bidel"),
    ("ARA_classical_diwans", "アラビア・ペルシア", "Arabic classical", "ara", "Arabic diwans: Mu'allaqat 7 plus other Pre-Islamic, Antar+Imru' al-Qais full diwans, Abu Nuwas khamriyyat+ghazaliyyat, Abu Tammam Hamasa, al-Mutanabbi 100, al-Maarri Luzumiyyat, Andalusian (Ibn Zaydun, Ibn Hazm, al-Mu'tamid, Ibn al-Khatib), Sufi (Ibn al-Farid, Ibn Arabi, al-Hallaj, Rabi'a)"),
    ("PER_modern_PD", "アラビア・ペルシア", "近代ペルシア(PD)", "fas", "Modern Persian (PD before 1929): Iraj Mirza, Bahar Malek-osh-Sho'ara, Aref Qazvini, Dehkhoda, Forough Farrokhzad early, Sohrab Sepehri early — focus on PD-classical period works"),
    ("ARA_andalusian_focus", "アラビア・ペルシア", "Andalusian", "ara", "Al-Andalus poetry: Ibn Hazm Tawq al-Hamamah verses, Ibn Zaydun complete Nuniyya, al-Mu'tamid verses from prison, Ibn Sahl al-Andalusi muwashshahat, Wallada bint al-Mustakfi, Ibn al-Khatib, Ibn Hamdis, Ibn Khafaja, Ibn Quzman zajal"),

    # Modern European: 6 workers
    ("EU_german_full", "近代ヨーロッパ", "German Romantic-Modern", "de", "German poetry deep: Goethe 30 (West-östlicher Divan, Faust songs, Erlkönig, Mignon, Der Fischer, Der König in Thule), Schiller 20 (An die Freude, Götter Griechenlands, Lied von der Glocke, Walhall, Die Bürgschaft), Hölderlin 20 (Patmos, Mnemosyne, Brot und Wein, Andenken, Heimkunft), Heine 30 (Lyrisches Intermezzo, Romanzero, Lazarus), Mörike, Droste-Hülshoff, Storm, Rilke 20"),
    ("EU_french_full", "近代ヨーロッパ", "French", "fr", "French poetry: Hugo 30 (Demain dès l'aube, Booz endormi, Crépuscule, Tristesse Olympio, Lux), Lamartine 15 (Le Lac, L'Isolement, Le Vallon, Méditations), Baudelaire all sections, Rimbaud Illuminations 15+Saison 5, Verlaine Romances+Sagesse+Fêtes, Mallarmé 10, Apollinaire Alcools, Valéry, Heredia, Leconte de Lisle"),
    ("EU_italian_full", "近代ヨーロッパ", "Italian", "it", "Italian poetry: Leopardi Canti 30 (L'Infinito, A Silvia, Il sabato, La quiete, Canto notturno, Le Ricordanze, Aspasia), Carducci Odi barbare, Pascoli Myricae, D'Annunzio Alcyone (La pioggia nel pineto), Saba Canzoniere, Ungaretti Allegria+Sentimento, Montale Ossi"),
    ("EU_russian_silver", "近代ヨーロッパ", "Russian Silver Age", "ru", "Russian Silver Age (PD): Annensky, Sologub, Bryusov, Ivanov Vyach, Voloshin, Gippius, Khlebnikov, Mayakovsky early (PD), Pasternak early, Mandelstam early Tristia, Tsvetaeva early, Akhmatova early Vecher+Chetki, Yesenin, Klyuev, Esenin"),
    ("EU_polish_czech_hungarian", "近代ヨーロッパ", "中欧", "pl/cs/hu", "Polish-Czech-Hungarian: Słowacki, Norwid, Asnyk, Konopnicka; Mácha Máj, Erben Kytice, Vrchlický, Sova; Petőfi Apostle+Janos Vitez, Arany Toldi+ballads, Vörösmarty Csongor és Tünde, Madách Az ember tragédiája, Ady Endre"),
    ("EU_iberian_lusofone", "近代ヨーロッパ", "Iberian", "es/pt", "Iberian poetry: Garcilaso de la Vega 38 sonnets, San Juan de la Cruz 5 cantos, Quevedo 70+ sonnets, Góngora Polifemo+Soledades, Lope de Vega, Calderón, Bécquer Rimas 1-79, Espronceda; Camões Lusiadas 10 cantos, Sá de Miranda, Bocage, Almeida Garrett, Eça de Queiroz, Cesário Verde, Antero de Quental"),

    # 20-21c Global: 4 workers (focus on PD-OK 1929-)
    ("GLOBAL_latin_americana", "20-21世紀グローバル", "Latin America", "es", "Latin American (1929-1960 fair-use OK): Vallejo Trilce+España+Heraldos negros, Neruda Veinte poemas+Residencia+Canto General+Odas, Borges Fervor+Cuaderno San Martin, Mistral Desolacion+Tala+Lagar, Paz Piedra+Salamandra, Lezama Lima Muerte de Narciso, Huidobro Altazor"),
    ("GLOBAL_modern_arab", "20-21世紀グローバル", "Modern Arabic", "ara", "Modern Arabic: Ahmad Shawqi 'amir al-shuara, Hafiz Ibrahim, al-Manfaluti, al-Aqqad, Abu al-Qasim al-Shabi, Khalil Mutran, Jubran (Tears and Laughter, Twenty Drawings poems), al-Sayyab 'Anshudat al-Matar+Unshudat al-mukhtar, Nizar Qabbani early, Adonis, Mahmoud Darwish"),
    ("GLOBAL_african_modern", "アフリカ", "Modern African", "en/fr", "African modern: Senghor Hosties Noires+Ethiopiques, Aimé Césaire Cahier+Soleil cou coupé+Ferrements, David Diop Coups de Pilon, Birago Diop Leurres et Lueurs, Soyinka Idanre+Mandela's Earth, Okigbo Heavensgate+Limits+Path of Thunder, p'Bitek Song of Lawino+Song of Ocol, Brutus Letters to Martha"),
    ("GLOBAL_other_modern", "20-21世紀グローバル", "Diverse modern", "various", "Diverse modern (1929+ fair-use): Walcott Omeros+In a Green Night, Heaney Death of Naturalist+North+Field Work, Hughes Crow+Birthday Letters, Plath Ariel, Larkin Whitsun Weddings, Lowell Life Studies+For the Union Dead, Bishop Geography III, Ashbery Self-Portrait, Brodsky 24 elegies"),

    # East Asian (Korea/Vietnam): 4 workers
    ("KR_classical_modern", "東アジア", "Korean classical-modern", "kor", "Korean: 향가 14, 高麗歌謡 (動動, 青山別曲, 鄭瓜亭, 滿殿春, 西京別曲 fully), 時調 100 (Hwang Jini deep dive 30, Yi Hwang, Yi I, Jeong Cheol, Yun Seondo Sasi 40, Bak Inro), 歌辭 (Songgang Jeong Cheol Sa-Mi-In-Gok, Gwandong Byeolgok), 漢詩 (Choe Chiwon, Yi Saek, Heo Nanseolheon 50, Im Je), modern 韓龍雲, 金素月, 李陸史, 尹東柱"),
    ("VN_chu_nom_full", "東アジア", "Vietnamese", "vie", "Vietnamese chu nom and modern: Nguyễn Du Truyện Kiều 50 episodes, Nguyễn Trãi Quốc Âm Thi Tập 30 + Hán Việt 20, Nguyễn Bỉnh Khiêm Bạch Vân Quốc Ngữ Thi 30, Hồ Xuân Hương 50 chu nom poems, Bà Huyện Thanh Quan 10, Đoàn Thị Điểm Chinh Phụ Ngâm Khúc, Cao Bá Quát, Tản Đà 30, Nguyễn Khuyến 30, Trần Tế Xương 30"),
    ("KR_sijo_full", "東アジア", "朝鮮時調", "kor", "朝鮮時代時調: 高麗末忠節時調 (鄭夢周, 李芳遠, 李穡, 鄭道伝, 길재) 30, 朝鮮初士林時調 (孟思誠, 黃喜, 成三問六臣) 20, 中期 (李退渓, 李栗谷, 鄭澈, 尹善道) 50, 後期 (李冠命, 安玟英, 朴孝寛) 20, 妓生時調 (黃真伊, 桂娘, 梅窓, 紅粧, 洪娘) 30"),
    ("VN_sangam_other", "東アジア", "Other East Asian", "tam/various", "Tamil Sangam Akananuru+Purananuru+Kalittokai+Paripatal+Patirruppattu 50, Tirukkural 1330 representative 50; Khmer Reamker 5, Lao Sin Xay 5, Burmese Yatu+Eichin 10, Thai Sunthorn Phu 30, Indonesian Hikayat 5, Malay pantun 30"),

    # Medieval / additional: 5 workers
    ("MED_germanic", "中世ヨーロッパ", "Germanic Medieval", "ang/enm/gmh", "Germanic medieval: Beowulf all sections (Grendel, Mother, Dragon, Heorot scenes), Cædmon Hymn, Dream of the Rood, Wanderer, Seafarer, Battle of Maldon, Battle of Brunanburh, Riddles 30, Widsith, Deor; Middle English (Pearl, SGGK, Patience, Cleanness, Owl and Nightingale); Walther von der Vogelweide, Reinmar, Wolfram"),
    ("MED_romance", "中世ヨーロッパ", "Romance Medieval", "fro/oci/it", "Romance medieval: Chanson de Roland laisses 50, Chrétien (Erec, Cligès, Yvain, Lancelot, Perceval) 25, Marie de France 12 lais all, Tristan et Iseut Béroul+Thomas, Roman de la Rose Guillaume+Jean de Meun 50, Villon Testament+Lais full, Charles d'Orléans, Christine de Pizan; Trobadors (Bernart, Jaufre, Marcabru, Guillaume IX) 30"),
    ("MED_dante_petrarch", "中世ヨーロッパ", "Italian Trecento", "ita", "Italian Trecento: Dante Vita Nuova 31 sonnets+Convivio+all 100 Commedia cantos representative tercets, Petrarch Canzoniere 366 representative 80 (in vita+in morte), Boccaccio Filocolo+Filostrato+Teseida+Ninfale+Decameron poems, Cino da Pistoia, Cecco Angiolieri, Folgóre da San Gimignano"),
    ("MED_iberian_medieval", "中世ヨーロッパ", "Iberian medieval", "es/cat/gal", "Iberian medieval: Cantar de Mio Cid 3 cantares, Berceo Milagros, Juan Ruiz Libro de Buen Amor 50, Manrique Coplas, Marqués de Santillana sonetos+serranillas; Catalan: Llull Cant de Ramon, Ausiàs March 100 cants, Jordi de Sant Jordi; Galician-Portuguese cantigas de amigo+amor+escarnio 50"),
    ("MED_neo_byzantine", "中世ヨーロッパ", "Byzantine-Caroligian", "grc/lat", "Byzantine Greek hymns: Romanos Melodos kontakia 60, John of Damascus, Symeon the New Theologian Hymns of Divine Love, George of Pisidia; Caroligian Latin: Alcuin, Theodulf, Walafrid, Notker, Hrabanus Maurus")
]


def build_prompt(task) -> str:
    wid, region, era, lang, axis = task
    return f"""Output JSON with {PER_WORKER} canonical poetic texts focusing on:
{axis}

culture_region: "{region}"
era_period: "{era}"
language(s): {lang}

OUTPUT (only this JSON, no commentary):
{{"worker_id": "{wid}", "texts": [
  {{"id":"pt_text_<unique_snake>", "title_original":"<original-script>", "title_ja":"<日本語>", "title_en":"<English>", "author_name_display":"<著者>", "era_year":<int, BCE negative>, "era_period":"<period>", "culture_region":"{region}", "language_original":"<ISO 639-3>", "form_genre":"<form>", "meter_prosody":"<meter>", "length_lines":<int>, "full_text_or_excerpt":"<2-8 lines original text>", "excerpt_note":"<which part>", "public_domain_status":"PD-original", "source_url":"<archive URL>", "source_archive":"<archive>", "canonical_tier":<1, 2, or 3>}},
  ... ({PER_WORKER} entries)
]}}

Requirements:
- {PER_WORKER} entries, all with unique IDs starting "pt_text_"
- Use original-script characters (Greek, Latin, Chinese, Japanese, Sanskrit Devanagari, Arabic, Persian, Korean Hangul, Vietnamese chu nom etc.)
- 2-8 line excerpts of canonical opening or famous passages
- All authors must be PD (died before 1929 or pre-modern)
- source_url should be a real archive URL (Perseus/Gutenberg/Wikisource各言語/維基文庫/青空文庫/GRETIL/Ganjoor/Tipitaka)
- DIVERSITY: cover the breadth, not just the same 5 most-famous authors. Include lesser-known canonical works.
- Output JSON only, no commentary.
"""


def main():
    procs = []
    log_files = []
    for task in WORKER_TASKS:
        wid = task[0]
        out_file = OUTPUT_DIR / f"P7_{wid}.json"
        log_file = LOG_DIR / f"P7_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1500:
            print(f"Skip {out_file.name}")
            continue
        prompt = build_prompt(task)
        cmd = [
            "codex", "exec",
            "--skip-git-repo-check",
            "--sandbox", "read-only",
            "--output-last-message", str(out_file),
            prompt,
        ]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P7_{wid} (pid {p.pid})")

    print(f"\n{len(procs)} workers running...")
    for wid, p in procs:
        rc = p.wait()
        print(f"  P7_{wid}: exit {rc}")
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
