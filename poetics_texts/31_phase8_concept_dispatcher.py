#!/usr/bin/env python3
"""Phase 8 concept expansion dispatcher.

40 specialized workers, each generating 30 detailed concepts in a niche
poetics sub-domain that the existing 1,494-concept DB has lightly covered.
"""
import subprocess
from pathlib import Path

OUTPUT_DIR = Path("/tmp/poetics_concepts_p8")
LOG_DIR = Path("/tmp/poetics_concepts_p8_logs")
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

PER_WORKER = 30

# 40 concept-expansion axes: each targets a specific poetics sub-domain
WORKER_AXES = [
    # Sanskrit Poetics (8 axes)
    ("SAN_rasa_nine", "古典詩学", "Sanskrit Rasa Theory - 9 rasas (shringara/hasya/karuna/raudra/vira/bhayanaka/bibhatsa/adbhuta/shanta) plus 33 sthayibhavas, 8 sattvikabhavas, 33 vyabhicaribhavas, with sanskrit names + Bharata Natyashastra references"),
    ("SAN_dhvani", "古典詩学", "Anandavardhana Dhvanyaloka concepts: dhvani (suggestion) types - vastu-dhvani, alamkara-dhvani, rasa-dhvani; vyanjana, lakshana, gunas, ritis, anumana, with sanskrit terms"),
    ("SAN_alamkara", "修辞学・弁論術", "Sanskrit Alamkaras: 50 figures of speech from Bhamaha, Dandin, Udbhata, Rudrata, Mammata - upama, rupaka, utpreksha, atisayokti, vyatireka, dipaka, samasokti, slesha, virodha, sandeha, etc. with original sanskrit definitions"),
    ("SAN_kavya_lakshana", "古典詩学", "Sanskrit Kavya theory: kavya-lakshana definitions from Bhamaha, Dandin Kavyadarsha, Vamana Kavyalankarasutra, Anandavardhana, Mammata Kavyaprakasha - prakaranas, gunas (madhurya/ojas/prasada), doshas"),
    ("SAN_riti_school", "古典詩学", "Vamana Riti school: vaidarbhi, gaudi, panchali styles, dasagunas (10 qualities), prasada, samadhi, kanti theory"),
    ("SAN_natyashastra_36_concepts", "古典詩学", "Bharata Natyashastra 36 lakshanas of dramatic composition + 5 kinds of vrtti (kaisiki/sattvati/arabhati/bharati) + 10 forms of rupaka + sandhis (5 junctures) + sandhyangas (64 elements)"),
    ("SAN_bhakti_alankara", "比較詩学", "Rupa Goswami Bhakti-rasamrita-sindhu concepts: madhurya-rasa, sakhya-rasa, vatsalya-rasa, dasya-rasa, shanta-rasa Bhakti specific applications, gauna-rasa, mukhya-rasa, sthayi-bhava in bhakti"),
    ("SAN_vakrokti", "修辞学・弁論術", "Kuntaka Vakrokti-jivita: vakrokti (oblique expression) 6 types - varna-vinyasa, pada-purvardha, vakya, prakarana, prabandha; vichitra-vakrokti vs other rasa systems"),

    # Chinese Poetics (5 axes)
    ("CHN_wenxin_50", "古典詩学", "劉勰『文心雕龍』50編の概念: 原道, 徵聖, 宗經, 正緯, 辨騷, 明詩, 樂府, 詮賦, 頌讚, 祝盟, 銘箴, 誄碑, 哀弔, 雜文, 諧讔, 史傳, 諸子, 論說, 詔策, 檄移, 封禪, 章表, 奏啟, 議對 etc - each as distinct theoretical concept with Chinese term"),
    ("CHN_sikongtu", "古典詩学", "司空図『二十四詩品』: 24品 - 雄渾, 沖澹, 纖穠, 沈著, 高古, 典雅, 洗鍊, 勁健, 綺麗, 自然, 含蓄, 豪放, 精神, 縝密, 疏野, 清奇, 委曲, 實境, 悲慨, 形容, 超詣, 飄逸, 曠達, 流動 - each as poetic mood concept"),
    ("CHN_yan_shenyun", "古典詩学", "王漁洋・神韻派詩学: 神韻 (sublime resonance), 興 (xing - evocative metaphor), 比 (bi - comparison), 賦 (fu - direct narration), 風 (feng - air/manner), 雅 (ya - elegance), 頌 (song - hymnic praise), 興趣 (interest), 妙悟 (subtle insight), 韻味 (lingering flavor) - Tang/Song/Qing school terms"),
    ("CHN_yixiang_jingjie", "古典詩学", "Chinese poetics: 意象 (yixiang - poetic image), 意境 (yijing - imagic realm), 境界 (jingjie - phenomenal境 from Wang Guowei), 神思 (creative imagination), 興象 (xingxiang - inspired image), 情景交融 (fusion of feeling and scene), 言志 (yan zhi - speaking the will), 言意 (saying-meaning) tensions - 王國維 人間詞話 concepts"),
    ("CHN_song_critics", "古典詩学", "宋代詩話 concepts: 嚴羽『滄浪詩話』妙悟・別材別趣・以禪喩詩, 司空圖韻味, 蘇軾枯淡, 黄庭堅換骨奪胎・点鉄成金, 陸游 詩外功夫, 楊万里 活法, 朱熹 興比賦三義 - each as critical concept"),

    # Japanese Poetics (5 axes)
    ("JP_karon_yugen", "比較詩学", "日本中世歌論: 幽玄 (Shunzei→Teika), 有心 (ushin), もののあはれ (mono no aware), あはれ (aware), 余情 (yojo - lingering feeling), 余韻 (yoin - lingering resonance), 妖艶 (yoen - ethereal beauty), 艶 (en - charm), をかし (okashi), さび (sabi), わび (wabi), 心 (kokoro), 詞 (kotoba), 姿 (sugata), 体 (tai - poetic style), 風骨 (fukotsu) - each with Mumyosho/Maigetsusho passages"),
    ("JP_haiku_terms", "比較詩学", "俳諧概念: 寂び (sabi - patina), 侘び (wabi - quiet poverty), しをり (shiori - tender pity), 細み (hosomi - slenderness), 軽み (karumi - lightness), 風雅 (fuga - poetic elegance), 不易流行 (ekirei - eternal-changing), 高悟帰俗 (kogo kizoku), 切字 (kireji - cutting word), 季語 (kigo - season word), 本意 (honi - essential nature) - Basho theory"),
    ("JP_renga_terms", "比較詩学", "連歌概念: 心敬 (Shinkei) ささめごと, 二条良基 連歌新式, 宗祇 連歌至宝抄, 宗鑑 - 寄合 (yoriai), 付合 (tsukeai), 詞遣 (kotoba-zukai), 物付 (monozuke), 心付 (kokorozuke), 匂付 (nioizuke), 余情, 心姿, 玄問黒 - linked verse compositional theory"),
    ("JP_zeami_noh", "比較詩学", "世阿弥能楽論: 風姿花伝 - 花 (hana), 幽玄 (yugen specific to Noh), もどき (modoki), 物まね (monomane), 序破急 (johakyu), 三体 (santai), 二曲三体 - aging theory, secret tradition - 風姿花伝・花鏡・至花道 quotations"),
    ("JP_motoori_kokugaku", "比較詩学", "国学派歌論: 賀茂真淵 ますらをぶり/たをやめぶり, 本居宣長 もののあはれ・古今集遠鏡, 物の真意, 漢意 (karagokoro) vs 大和心 (yamatogokoro), 直毘霊, 古道, 神道 詩学的展開, 香川景樹 桂園派 しらべ・ふしぎ - 国学アンティ-Confucian poetics"),

    # Persian / Arabic Poetics (4 axes)
    ("ARA_balagha", "修辞学・弁論術", "ʿIlm al-balāgha (Arabic rhetoric science): ʿIlm al-maʿānī (semantic), ʿIlm al-bayān (figurative - tashbīh, isti'āra, kināya, majāz), ʿIlm al-badīʿ (embellishment - jinās, ṭibāq, muqābala) - al-Jurjani Asrar al-balagha, Sakkaki Miftah al-ulum, Khatib al-Qazwini Talkhis al-Miftah - 30 concepts with Arabic terms"),
    ("PER_ghazal_form", "比較詩学", "Persian poetics specifics: maṭlaʿ, maqṭaʿ, takhalluṣ, radīf, qāfīya, wazn, maʿānī al-Qur'ān references, masnavi structure, qit'a, rubāʿī, ghazal organization - mukhammas, musaddas, tarji'-band, tarkib-band, 30 form concepts from Shams al-Din Razi al-Mu'jam"),
    ("ARA_maqama", "修辞学・弁論術", "Arabic prose-poetic: maqāma form (al-Hamadhani, al-Hariri), saj' (rhymed prose) types, badīʿiyyāt, qaṣīda structure (nasib, rahil, fakhr, hija, ritha), ḥikma, mathal - rhetorical-narrative compound concepts"),
    ("PER_irfan", "現象学的詩学", "Persian Sufi poetics: ʿishq (mystical love), shuhud (witnessing), fana (annihilation), baqa (subsistence), wahdat al-wujud, hal vs maqam, dhawq, mushahada - Ibn Arabi, Rumi, Hafez, Sanai, Attar mystical-poetic vocabulary - 30 concepts"),

    # Russian Formalism / Structuralism细目 (3 axes)
    ("RUS_formalism_deep", "ロシア・フォルマリズム", "Russian Formalism granular concepts: priem (device), ostranenie sub-types, automatization vs deautomatization, motivirovka, fabula vs syuzhet detailed, zaum (transrational), skaz (oral narration), dominant function, literary evolution Tynianov, polyphony Bakhtin, chronotope - 30 detailed Russian terms with Cyrillic"),
    ("STRUCT_genette", "構造主義詩学", "Genette narratology granular: focalization (zero/internal/external), récit/histoire/narration, analepsis/prolepsis, frequency (singulative/repetitive/iterative), narrative voice (extradiegetic/intradiegetic/metadiegetic), narratee, hypertextuality, paratext, architext, metalepsis - 30 narratological concepts with French terms"),
    ("STRUCT_jakobson_riffaterre", "構造主義詩学", "Jakobson + Riffaterre: 6 communicative functions (referential/emotive/conative/phatic/metalingual/poetic), poetic function projection, equivalence axis, hypogram, matrix, descriptive system, ungrammaticality, dual sign, semiotic mediation - 30 structural concepts"),

    # Reception / Reader-Response (2 axes)
    ("RECEPTION_jauss_iser", "受容理論", "Constance School: horizon of expectations (Erwartungshorizont), aesthetic distance, horizon change, indeterminacy, blanks (Iser), gap-filling, implied reader, transactional theory Rosenblatt, response statements, interpretive community Fish, validity Hirsch - 30 concepts"),
    ("RECEPTION_ingarden_layers", "現象学的詩学", "Ingarden literary work strata: 4 strata - sound stratum, meaning stratum, schematized aspects, represented objectivities; concretization, places of indeterminacy (Unbestimmtheitsstellen), aesthetic objects vs artistic objects, polyphonic harmony, opalescence, metaphysical qualities - 30 phenomenological terms"),

    # Cognitive Poetics (3 axes)
    ("COG_conceptual_blending", "認知詩学", "Conceptual blending (Fauconnier-Turner): mental spaces, generic space, blended space, integration networks, vital relations, compression, projection, elaboration, completion - + image schemas (path/container/balance/center-periphery), metaphor mappings (Lakoff-Johnson), prototype theory - 30 concepts"),
    ("COG_text_world", "認知詩学", "Text World Theory (Werth/Gavins): text-worlds, world-builders, function-advancers, modal worlds, deictic shift, world-switches, sub-worlds, focalizer, schema theory in poetics, attention/perspective, force dynamics, embodied simulation - 30 cognitive terms"),
    ("COG_narrative_poetics", "認知詩学", "Cognitive narratology Herman: storyworld, situation model, possibilities, narrative comprehension, prospection, intentional stance, theory of mind in narrative, qualia, naturalization, fictional minds Palmer, externalist/internalist - 30 concepts"),

    # Postmodern / Deconstruction (3 axes)
    ("POST_derrida", "ポスト構造主義詩学", "Derrida deconstruction: différance, trace, supplementarity, parergon, dissemination, hauntology, archive fever, gift, hospitality, pharmakon, hymen, undecidable, iterability, signature event context, mise en abyme - 30 deconstructive concepts"),
    ("POST_foucault_kristeva", "ポスト構造主義詩学", "Foucault: episteme, discourse formation, statement (énoncé), enunciative modality, governmentality, biopolitics, panopticon-as-poetic-trope; Kristeva: chora, semiotic vs symbolic, intertextuality 3 axes, abjection, jouissance, geno-text/pheno-text - 30 concepts"),
    ("POST_baudrillard_lyotard", "ポスト構造主義詩学", "Baudrillard: simulacrum (4 orders), hyperreality, fatal strategy, seduction, transparency of evil; Lyotard: petit récit, differend, postmodern condition, sublime, figural; de Man rhetoric/blindness/insight - 30 postmodern concepts"),

    # Digital / Electronic Poetics (2 axes)
    ("DIGITAL_combinatorial", "デジタル詩学", "Digital poetics: combinatorial generation, generative poetics, OuLiPo techniques (n+7, lipograms), aleatory composition, code poetry, electronic literature genres (hypertext/hyperpoetry/interactive fiction/CAVE poetry), kinetic poetry, sound poetry digital, distant reading - 30 concepts"),
    ("DIGITAL_machine", "デジタル詩学", "Computational poetics: Markov chain poetry, n-gram models in poetry, neural poetry generation, GPT poetry, bot poetry, transformer attention as poetic device, latent space exploration, prompt poetry, post-human authorship, machine reading, 30 ML-poetics concepts"),

    # African / Indigenous Poetics (2 axes)
    ("AFRICAN_oral", "比較詩学", "African oral poetics: griot epic conventions, izibongo/imbongi praise poetry conventions (Zulu/Xhosa), oriki structure (Yoruba), ifa divination poetry types (256 Odu), Ethiopian qene, Amharic gebre, dilemma tale verse, drum text, talking drum poetics, call-response, repetition-with-variation, oral formulaic theory Lord-Parry African application - 30 concepts"),
    ("INDIGENOUS_oceania", "比較詩学", "Indigenous oceanic poetics: Hawaiian mele kahiko classification (mele inoa/koihonua/ho'oipoipo), Maori waiata categories (waiata aroha/poi/karakia/moteatea), Songline structure (Australian), Inuit qarrtsiluni, Ainu yukar narrative conventions, nahuatl difrasismo, popol vuh parallelism, navajo blessingway formula - 30 cross-cultural oral concepts"),

    # Comparative / Translation Poetics (2 axes)
    ("COMP_translation", "比較詩学", "Translation poetics: foreignization vs domestication (Venuti), formal vs dynamic equivalence (Nida), skopos theory, polysystem theory (Even-Zohar), retranslation hypothesis, cultural turn, untranslatable, paratext as translation, indirect translation, pivot translation - 30 translation theory concepts"),
    ("COMP_world_lit", "比較詩学", "World literature theory: weltliteratur (Goethe), planetary (Spivak), worlded (Damrosch), translation zones (Apter), republic of letters (Casanova), national epic vs cosmopolitan, cosmopoetics, pan-Asian/pan-African comparative, gatherings (anthology theory), canon revision - 30 comparative concepts"),

    # Modern / 20c Movement (3 axes)
    ("MOD_imagism_principles", "近代美学・詩学", "Anglo-American modernism: imagism principles (Pound 'Few Don'ts'), vorticism, objective correlative (Eliot), tradition and individual talent, dissociation of sensibility, melopoeia/phanopoeia/logopoeia, ideogrammic method, Cathay translation theory, projective verse (Olson), composition by field - 30 modernist concepts"),
    ("MOD_new_criticism", "近代美学・詩学", "New Criticism: heresy of paraphrase (Brooks), intentional fallacy (Wimsatt-Beardsley), affective fallacy, ambiguity 7 types (Empson), tension (Tate), irony as principle (Brooks), close reading, organic unity, paradox (Brooks), well-wrought urn, dramatic monologue analysis, levels of meaning (Richards) - 30 concepts"),
    ("MOD_avant_garde", "ポスト構造主義詩学", "Avant-garde poetics: shock (Benjamin), montage (Eisenstein-poetics), epic theatre Brecht alienation, surrealist écriture automatique, dada cut-up Tzara, futurism words-in-freedom, expressionist scream, lettrisme, situationist détournement, language poetry, conceptual writing - 30 avant-garde concepts"),

    # Niche / specialized (4 axes)
    ("NICHE_meter_prosody", "古典詩学", "Cross-cultural prosody: dactylic hexameter, sapphic stanza, alcaic, hendecasyllable, alexandrine, heroic couplet, blank verse, terza rima, ottava rima, sonnet variants (Petrarchan/Shakespearean/Spenserian), villanelle, sestina, pantoum, ghazal radif-qafiya, ruba'i, tanka 5-7-5-7-7, haiku, sapphic - 30 metrical concepts"),
    ("NICHE_genre_taxonomy", "古典詩学", "Genre theory granular: pastoral conventions, elegy types (love elegy/funeral elegy/political elegy), epic conventions, ode types (Pindaric/Horatian/irregular), satire (Horatian/Juvenalian/Menippean), epigram conventions, ekphrasis, prosopopoeia, anatomy, encomium, blason, aubade, alba, planh - 30 classical genre concepts"),
    ("NICHE_eco_poetics", "近代美学・詩学", "Ecocriticism + ecopoetics: environmental imagination (Buell), ecocriticism waves, place attachment, deep ecology poetics, animal studies, multispecies, slow violence (Nixon), Anthropocene poetics, climate-change poetry, dwelling (Heideggerian), oikopoetics, georgics revival, nature writing - 30 concepts"),
    ("NICHE_disability_queer", "ポスト構造主義詩学", "Identity poetics: queer poetics (Sedgwick/Butler readings), feminist écriture féminine (Cixous), gynocriticism, lesbian continuum, disability poetics, crip time, narrative prosthesis, postcolonial poetics granular (mimicry/hybridity/third space Bhabha), creolization, négritude poetics - 30 concepts")
]


def build_prompt(wid, subfield, axis_desc):
    return f"""Generate {PER_WORKER} detailed poetics CONCEPTS in this niche sub-domain (NOT poetic texts - we want concepts/theoretical terms):

NICHE: {axis_desc}

Each concept must be a distinct theoretical term used in poetics scholarship.

OUTPUT (only this JSON, no commentary):
{{"worker_id": "{wid}", "concepts": [
  {{"id": "cp_<unique_snake>",
    "name_ja": "<日本語訳>",
    "name_en": "<English term>",
    "name_original": "<original-language term: Sanskrit IAST/Chinese/Arabic/Greek/etc>",
    "definition": "<200-400字 academic definition in Japanese>",
    "impact_summary": "<scholarly significance 100-200字>",
    "subfield": "{subfield}",
    "school_of_thought": "<school/tradition>",
    "era_start": <year, BCE negative>,
    "era_end": <year or null>,
    "methodology_level": "理論",
    "keywords_ja": "kw1,kw2,kw3",
    "keywords_en": "kw1, kw2, kw3",
    "originator_id": null,
    "year_proposed": <year>,
    "founding_work": "<work in which the concept was introduced>"
  }},
  ... ({PER_WORKER} concepts)
]}}

Requirements:
- {PER_WORKER} concepts
- IDs unique starting "cp_"
- Use original-language terms in name_original
- Subfield must be: {subfield}
- All authors PD (pre-1929)
- Output JSON only.
"""


def main():
    procs = []
    log_files = []
    for wid, sf, axis in WORKER_AXES:
        out_file = OUTPUT_DIR / f"P8C_{wid}.json"
        log_file = LOG_DIR / f"P8C_{wid}.log"
        if out_file.exists() and out_file.stat().st_size > 1500:
            print(f"Skip {out_file.name}")
            continue
        prompt = build_prompt(wid, sf, axis)
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(out_file), prompt]
        log = open(log_file, "w")
        p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        procs.append((wid, p))
        log_files.append(log)
        print(f"Launched P8C_{wid} (pid {p.pid})")

    print(f"\n{len(procs)} concept-expansion workers running...")
    for wid, p in procs:
        rc = p.wait()
        print(f"  P8C_{wid}: exit {rc}")
    for lf in log_files:
        lf.close()


if __name__ == "__main__":
    main()
