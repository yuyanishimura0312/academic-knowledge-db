"""DUA Wave A2 Batch 18 — 残り218件 目標5500総件数到達用"""
import sqlite3, uuid, datetime

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"

def uid(): return "dua_" + uuid.uuid4().hex[:12]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

RECORDS = [
    # ===== 哲学・倫理学 固有概念 新規 (~40) =====
    (uid(),"スコラ哲学の普遍論争","Scholastic Universals Debate","Medieval debate between realists and nominalists about the existence of universals","哲学・倫理学","Western_Europe",1050,"https://en.wikipedia.org/wiki/Problem_of_universals","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"オッカムの剃刀","Occam's Razor","William of Ockham's principle that entities should not be multiplied beyond necessity","哲学・倫理学","Western_Europe",1320,"https://en.wikipedia.org/wiki/Occam%27s_razor","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アンセルムスの神の存在論的証明","Anselmian Ontological Argument","Anselm's a priori argument for God's existence from the concept of the greatest being","哲学・倫理学","Western_Europe",1077,"https://en.wikipedia.org/wiki/Ontological_argument","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アクィナスの五道","Aquinas Five Ways","Thomas Aquinas's five a posteriori arguments for the existence of God","哲学・倫理学","Western_Europe",1265,"https://en.wikipedia.org/wiki/Five_Ways_(Aquinas)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"神正論","Theodicy","Philosophical justification of God's goodness in the face of evil and suffering","哲学・倫理学","Western_Europe",1710,"https://en.wikipedia.org/wiki/Theodicy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"宗教哲学の認識論","Epistemology of Religious Belief","Plantinga's reformed epistemology and proper basicality of theistic belief","哲学・倫理学","North_America",1981,"https://en.wikipedia.org/wiki/Reformed_epistemology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"行為理論","Action Theory","Philosophical analysis of intentional action, reasons, and agency","哲学・倫理学","North_America",1963,"https://en.wikipedia.org/wiki/Action_theory_(philosophy)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"社会的存在論","Social Ontology","Study of the nature of social entities: institutions, corporations, and collective intentionality","哲学・倫理学","North_America",1990,"https://en.wikipedia.org/wiki/Social_ontology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"形而上学の新アリストテレス主義","Neo-Aristotelian Metaphysics","Contemporary revival of Aristotelian categories: substance, essence, powers, and grounding","哲学・倫理学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Aristotelian_metaphysics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"グラウンディング理論","Metaphysical Grounding","Study of the asymmetric dependence relation between less fundamental and more fundamental entities","哲学・倫理学","Western_Europe",2009,"https://en.wikipedia.org/wiki/Grounding_(metaphysics)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"自由意志と決定論","Free Will and Determinism","The philosophical debate about whether determinism is compatible with moral responsibility","哲学・倫理学","Western_Europe",1650,"https://en.wikipedia.org/wiki/Free_will","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"個人同一性の持続問題","Problem of Personal Identity Over Time","How persons persist through change: psychological continuity vs. biological approaches","哲学・倫理学","Western_Europe",1690,"https://en.wikipedia.org/wiki/Personal_identity","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"知識とゲティア問題","Gettier Problem","Edmund Gettier's 1963 counterexamples to the justified true belief account of knowledge","哲学・倫理学","North_America",1963,"https://en.wikipedia.org/wiki/Gettier_problem","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"証言の認識論","Epistemology of Testimony","Whether knowledge acquired from others requires independent verification","哲学・倫理学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Testimony_(philosophy)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"認識的徳論","Virtue Epistemology","Extension of virtue ethics to epistemology: intellectual character traits and their role in knowledge","哲学・倫理学","North_America",1980,"https://en.wikipedia.org/wiki/Virtue_epistemology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"社会認識論","Social Epistemology","Study of how social practices and institutions affect knowledge production","哲学・倫理学","North_America",1987,"https://en.wikipedia.org/wiki/Social_epistemology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"動物の権利倫理学","Animal Rights Ethics","Peter Singer and Tom Regan's arguments for the moral status of non-human animals","哲学・倫理学","North_America",1975,"https://en.wikipedia.org/wiki/Animal_rights","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"気候変動の倫理学","Climate Ethics","Moral dimensions of climate change: intergenerational justice and responsibility","哲学・倫理学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Climate_ethics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"AI倫理学","AI Ethics","Ethical analysis of artificial intelligence: bias, transparency, and value alignment","哲学・倫理学","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"バイオエシックスの原理","Principles of Bioethics","Beauchamp and Childress's four principles: autonomy, beneficence, non-maleficence, justice","哲学・倫理学","North_America",1979,"https://en.wikipedia.org/wiki/Bioethics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"意識の神経哲学","Neurophilosophy of Consciousness","Patricia Churchland's program to solve consciousness using neuroscience","哲学・倫理学","North_America",1986,"https://en.wikipedia.org/wiki/Neurophilosophy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"4E認知科学","4E Cognition","Embodied, embedded, enacted, extended approaches to cognitive science","哲学・倫理学","Global_Synthesis",1991,"https://en.wikipedia.org/wiki/Embodied_cognition","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"延長した心","Extended Mind","Clark and Chalmers's thesis that cognition extends beyond the brain into the environment","哲学・倫理学","Western_Europe",1998,"https://en.wikipedia.org/wiki/Extended_mind_thesis","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"過去の偶発性","Contingency of the Past","Philosophical analysis of whether the past could have been otherwise given causal determinism","哲学・倫理学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Determinism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"相対主義と普遍主義","Relativism vs. Universalism","Metaethical debate over whether moral truths vary across cultures or are universal","哲学・倫理学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Moral_relativism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"政治哲学と国家の正当性","Legitimacy of the State","Philosophical justifications for state authority: consent, fair play, and natural duty","哲学・倫理学","Western_Europe",1651,"https://en.wikipedia.org/wiki/Legitimacy_(political)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"民主主義の哲学","Philosophy of Democracy","Deliberative, epistemic, and aggregative theories of democratic legitimacy","哲学・倫理学","Western_Europe",1840,"https://en.wikipedia.org/wiki/Democracy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"正義の哲学","Philosophy of Justice","Theories of distributive justice from Aristotle to Rawls and beyond","哲学・倫理学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Justice_(virtue)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"グローバル正義","Global Justice","Thomas Pogge and Charles Beitz on justice beyond the state in global institutions","哲学・倫理学","Global_Synthesis",1979,"https://en.wikipedia.org/wiki/Global_justice","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"世代間正義","Intergenerational Justice","Obligations to future generations: sustainability, climate policy, and institutional design","哲学・倫理学","Global_Synthesis",1971,"https://en.wikipedia.org/wiki/Intergenerational_equity","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"認識的不正義","Epistemic Injustice","Miranda Fricker's analysis of testimonial and hermeneutical injustice","哲学・倫理学","Western_Europe",2007,"https://en.wikipedia.org/wiki/Epistemic_injustice","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"障害の哲学","Philosophy of Disability","Critical disability studies and the social model vs. medical model debate","哲学・倫理学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/Disability_studies","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"食の倫理学","Food Ethics","Ethical dimensions of food production, consumption, and food justice","哲学・倫理学","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Food_ethics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"テクノロジーの哲学","Philosophy of Technology","Ellul, Heidegger, and Winner on the essence and politics of technology","哲学・倫理学","Western_Europe",1954,"https://en.wikipedia.org/wiki/Philosophy_of_technology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"マインドフルネスの哲学","Philosophy of Mindfulness","Philosophical analysis of mindfulness practices drawing on Buddhist and phenomenological traditions","哲学・倫理学","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Mindfulness","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"オントロジカル・ターン","Ontological Turn in Philosophy","Post-Analytic move to take metaphysics seriously: neo-Aristotelian ontology renaissance","哲学・倫理学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Ontology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"スピノザの汎神論","Spinoza's Pantheism","Spinoza's monism: God and Nature as one infinite substance with infinite attributes","哲学・倫理学","Western_Europe",1677,"https://en.wikipedia.org/wiki/Baruch_Spinoza","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"批判的実在論","Critical Realism","Roy Bhaskar's philosophy of science distinguishing the real, actual, and empirical","哲学・倫理学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Critical_realism_(philosophy_of_the_social_sciences)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"科学哲学の実在論","Scientific Realism","Debate over whether successful scientific theories describe a mind-independent reality","哲学・倫理学","Western_Europe",1960,"https://en.wikipedia.org/wiki/Scientific_realism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"インド哲学の知覚論","Indian Theory of Perception","Nyaya and Buddhist theories of valid perception as a source of knowledge","哲学・倫理学","South_Asia",-400,"https://en.wikipedia.org/wiki/Pramana","url_present","dua_wave_a2","active",now(),now()),
    # ===== 歴史学 固有概念 新規 (~30) =====
    (uid(),"マイクロヒストリー","Microhistory","Intensive historical analysis of small-scale events and individuals: Ginzburg's cheese and worms","歴史学","Western_Europe",1976,"https://en.wikipedia.org/wiki/Microhistory","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"グローバルヒストリー","Global History","Writing history from a global perspective, transcending national and regional boundaries","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Global_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ビッグヒストリー","Big History","Interdisciplinary study of history from the Big Bang to the present","歴史学","Global_Synthesis",1989,"https://en.wikipedia.org/wiki/Big_History","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"遺産と歴史","Heritage and History","Study of how the past is selected, preserved, and presented for contemporary audiences","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Cultural_heritage","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"フランス・アナール学派","Annales School","French historiographical movement emphasizing social structures, mentalites, and longue duree","歴史学","Western_Europe",1929,"https://en.wikipedia.org/wiki/Annales_school","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ドイツ歴史主義","German Historicism","Nineteenth-century German approach emphasizing historical particularity and Verstehen","歴史学","Western_Europe",1820,"https://en.wikipedia.org/wiki/Historicism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"サバルタン・スタディーズ","Subaltern Studies","South Asian historiographical collective recovering voices of the colonized","歴史学","South_Asia",1982,"https://en.wikipedia.org/wiki/Subaltern_Studies","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ポストコロニアル歴史学","Postcolonial Historiography","Dipesh Chakrabarty's provincializing Europe and writing histories from the margins","歴史学","Global_Synthesis",1992,"https://en.wikipedia.org/wiki/Postcolonial_theory","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"感情の歴史","History of Emotions","Study of how emotions are culturally constructed and experienced in past societies","歴史学","Western_Europe",2000,"https://en.wikipedia.org/wiki/History_of_emotions","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"物質文化史","Material Culture History","Study of objects and material goods as evidence for historical understanding","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Material_culture","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"フード・ヒストリー","Food History","Historical study of what people ate, food production, and foodways","歴史学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/History_of_food","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"身体の歴史","History of the Body","Historical study of how bodies are experienced, disciplined, and represented","歴史学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Body_studies","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"動物の歴史","Animal History","Historical study of human-animal relationships and the agency of non-human animals","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Animal_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"印刷革命の歴史","History of the Printing Revolution","Elizabeth Eisenstein's analysis of print culture and its social transformations","歴史学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Printing_press","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"大西洋史","Atlantic History","Study of the interconnected histories of Europe, Africa, and the Americas since 1500","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Atlantic_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"太平洋史","Pacific History","Study of the Pacific Ocean region, island peoples, and Pacific-rim connections","歴史学","Oceania",1960,"https://en.wikipedia.org/wiki/Pacific_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"宗教史の世俗主義的アプローチ","Secular Approaches to Religious History","Study of religion as a human phenomenon without theological assumptions","歴史学","Global_Synthesis",1870,"https://en.wikipedia.org/wiki/Secular_humanism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"近代ヨーロッパ史","Early Modern European History","History of Europe from 1450 to 1800: reformations, scientific revolution, absolutism","歴史学","Western_Europe",1450,"https://en.wikipedia.org/wiki/Early_modern_period","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"戦争の歴史","History of War","Military history and the study of warfare's political, social, and cultural dimensions","歴史学","Global_Synthesis",-3000,"https://en.wikipedia.org/wiki/Military_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"外交史","Diplomatic History","Traditional history of international relations and statecraft through archival sources","歴史学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Diplomatic_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"知識人の歴史","Intellectual History","History of ideas and the social context in which they were produced","歴史学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Intellectual_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"概念史","History of Concepts","Koselleck's Begriffsgeschichte: history of fundamental political and social concepts","歴史学","Western_Europe",1972,"https://en.wikipedia.org/wiki/Conceptual_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ブックヒストリー","History of Books","Study of the production, distribution, and reception of books across cultures","歴史学","Global_Synthesis",1980,"https://en.wikipedia.org/wiki/History_of_the_book","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"共同体の歴史","Community History","Local and regional historical studies emphasizing community agency","歴史学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Community_history","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"コロニアル・エンカウンターの歴史","History of Colonial Encounters","Study of the contact zones between colonizers and indigenous peoples","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Contact_zone","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"市場の歴史","History of Markets","Study of the development of commercial exchange from ancient markets to capitalism","歴史学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Market_(economics)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"金融の歴史","Financial History","Study of the development of money, credit, banking, and financial crises","歴史学","Western_Europe",1600,"https://en.wikipedia.org/wiki/Financial_history_of_the_Dutch_Republic","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"疫病の歴史","History of Epidemics","Study of how diseases shaped human populations and historical trajectories","歴史学","Global_Synthesis",-3000,"https://en.wikipedia.org/wiki/History_of_plague","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"移民の歴史","Migration History","Study of human migration patterns and their social, economic, and cultural consequences","歴史学","Global_Synthesis",1850,"https://en.wikipedia.org/wiki/History_of_immigration","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"帝国比較史","Comparative Empire History","Cross-cultural comparison of imperial formations and their structures","歴史学","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Comparative_history","url_present","dua_wave_a2","active",now(),now()),
    # ===== 文学・批評理論 固有概念 新規 (~30) =====
    (uid(),"現代詩の理論","Theory of Modern Poetry","Modernist poetics from Pound's Imagism to Eliot's impersonality and Olson's projectivist verse","文学・批評理論","North_America",1912,"https://en.wikipedia.org/wiki/Modernist_poetry","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"韻文と散文の差異","Verse vs. Prose Distinction","Philosophical analysis of what distinguishes verse from prose and poetry from fiction","文学・批評理論","Western_Europe",1790,"https://en.wikipedia.org/wiki/Verse_(poetry)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文学と道徳","Literature and Morality","Debate over whether literature has moral obligations or can be purely aesthetic","文学・批評理論","Western_Europe",1880,"https://en.wikipedia.org/wiki/Literary_ethics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文学の心理学","Psychology of Literature","Study of how literature represents mental states and creates empathic engagement","文学・批評理論","Western_Europe",1900,"https://en.wikipedia.org/wiki/Psychology_of_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"認知詩学","Cognitive Poetics","Application of cognitive linguistics and psychology to literary analysis","文学・批評理論","Western_Europe",1990,"https://en.wikipedia.org/wiki/Cognitive_poetics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"テクスト言語学","Textlinguistics","Study of texts as coherent wholes: cohesion, coherence, and textual properties","文学・批評理論","Western_Europe",1970,"https://en.wikipedia.org/wiki/Text_linguistics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"作者の意図","Authorial Intention","Debate over whether the author's intention is relevant to textual interpretation","文学・批評理論","North_America",1946,"https://en.wikipedia.org/wiki/Intentionalism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"キャラクター理論","Character Theory","Philosophical analysis of fictional characters as entities in possible worlds","文学・批評理論","Western_Europe",1980,"https://en.wikipedia.org/wiki/Character_(arts)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"フィクションのパラドックス","Paradox of Fiction","Why do we feel emotions about fictional characters we know do not exist?","文学・批評理論","Western_Europe",1975,"https://en.wikipedia.org/wiki/Paradox_of_fiction","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"崇高の文学批評","Sublime in Literary Criticism","Analysis of the aesthetics of the sublime in literary texts from Longinus to Burke to Kant","文学・批評理論","Western_Europe",100,"https://en.wikipedia.org/wiki/Sublime_in_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文学的典型","Literary Archetype","Jungian and Northrop Frye's use of archetypes in literary criticism","文学・批評理論","North_America",1957,"https://en.wikipedia.org/wiki/Archetype","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"メタフィクション","Metafiction","Fiction that calls attention to its own fictional status: self-referential narrative","文学・批評理論","North_America",1970,"https://en.wikipedia.org/wiki/Metafiction","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"自動作成詩","Computational Poetry","Poetry generated by algorithms and rule-based systems","文学・批評理論","Global_Synthesis",1960,"https://en.wikipedia.org/wiki/Computer_poetry","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"脱構築批評","Deconstructive Criticism","Application of Derridean deconstruction to literary texts: aporia and undecidability","文学・批評理論","Western_Europe",1967,"https://en.wikipedia.org/wiki/Deconstruction","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文化唯物論","Cultural Materialism","Raymond Williams and Jonathan Dollimore's materialist criticism of cultural texts","文学・批評理論","Western_Europe",1977,"https://en.wikipedia.org/wiki/Cultural_materialism_(literature)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"新歴史主義","New Historicism","Stephen Greenblatt's approach embedding literary texts in their historical contexts","文学・批評理論","North_America",1982,"https://en.wikipedia.org/wiki/New_Historicism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"帝国のテクスト","Empire and the Text","Analysis of how canonical literary texts encode colonial ideology","文学・批評理論","Global_Synthesis",1978,"https://en.wikipedia.org/wiki/Postcolonial_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"韓国文学","Korean Literature","Literary traditions of Korea from Sijo and Gasa to contemporary Korean fiction","文学・批評理論","East_Asia",900,"https://en.wikipedia.org/wiki/Korean_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ベトナム文学","Vietnamese Literature","Literary traditions of Vietnam including Nom literature and modern Vietnamese fiction","文学・批評理論","East_Asia",1000,"https://en.wikipedia.org/wiki/Vietnamese_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"スワヒリ語文学","Swahili Literature","Literary traditions of the Swahili coast of East Africa in Arabic script and Swahili","文学・批評理論","Sub_Saharan_Africa",1500,"https://en.wikipedia.org/wiki/Swahili_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"トルコ文学","Turkish Literature","Literary traditions from Ottoman divan poetry to modern Turkish Republican literature","文学・批評理論","West_Asia_North_Africa",1200,"https://en.wikipedia.org/wiki/Turkish_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ポーランド文学","Polish Literature","Literary traditions of Poland including Romanticism, Nobel laureates Szymborska and Milosz","文学・批評理論","Western_Europe",1100,"https://en.wikipedia.org/wiki/Polish_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"スカンジナビア文学","Scandinavian Literature","Literary traditions of Scandinavia: sagas, Strindberg, Ibsen, Hamsun, Lagerlof","文学・批評理論","Western_Europe",1000,"https://en.wikipedia.org/wiki/Scandinavian_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"オーストラリア文学","Australian Literature","Literary traditions of Australia including Aboriginal oral tradition and settler literature","文学・批評理論","Oceania",1788,"https://en.wikipedia.org/wiki/Australian_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"カナダ文学","Canadian Literature","Literary traditions of Canada in English and French, including First Nations literature","文学・批評理論","North_America",1600,"https://en.wikipedia.org/wiki/Canadian_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"南アフリカ文学","South African Literature","Literary traditions of South Africa: Coetzee, Gordimer, and post-apartheid writing","文学・批評理論","Sub_Saharan_Africa",1800,"https://en.wikipedia.org/wiki/South_African_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ポルトガル語文学","Portuguese Literature","Literary traditions of Portugal and Brazil including Pessoa, Saramago, and Guimaraes Rosa","文学・批評理論","Western_Europe",1100,"https://en.wikipedia.org/wiki/Portuguese_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ギリシア現代文学","Modern Greek Literature","Literary traditions of modern Greece from Solomos and Cavafy to Seferis","文学・批評理論","Western_Europe",1821,"https://en.wikipedia.org/wiki/Modern_Greek_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"フィリピン文学","Philippine Literature","Literary traditions of the Philippines in Tagalog, Spanish, English, and regional languages","文学・批評理論","East_Asia",1300,"https://en.wikipedia.org/wiki/Philippine_literature","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"カリブ海文学","Caribbean Literature","Postcolonial literary traditions of the Caribbean: Walcott, Lamming, Glissant","文学・批評理論","Latin_America",1900,"https://en.wikipedia.org/wiki/Caribbean_literature","url_present","dua_wave_a2","active",now(),now()),
    # ===== 言語学 固有概念 新規 (~20) =====
    (uid(),"変形生成文法のミニマリスト","Minimalist Program","Chomsky's 1995 framework reducing syntax to Merge and formal features","言語学","North_America",1995,"https://en.wikipedia.org/wiki/Minimalist_program","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"語彙意味論","Lexical Semantics","Study of word meaning, semantic relations, and lexical organization","言語学","Western_Europe",1970,"https://en.wikipedia.org/wiki/Lexical_semantics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"メタファー理論","Conceptual Metaphor Theory","Lakoff and Johnson's view that abstract thought is structured by conceptual metaphors","言語学","North_America",1980,"https://en.wikipedia.org/wiki/Conceptual_metaphor","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"空間と言語","Language and Space","How languages encode spatial relations: frames of reference, path, and ground","言語学","Global_Synthesis",1985,"https://en.wikipedia.org/wiki/Spatial_language","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"修辞学の伝統","Rhetorical Tradition","Study of classical and modern rhetoric: Aristotle's pisteis and Ciceronian oratory","言語学","Western_Europe",-350,"https://en.wikipedia.org/wiki/Rhetoric","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"言語と思考の関係","Language-Thought Relationship","Debates about whether language shapes thought, thought shapes language, or they are independent","言語学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Linguistic_relativity","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"語声学","Speech Perception","Study of how listeners recognize and categorize speech sounds in real time","言語学","Western_Europe",1950,"https://en.wikipedia.org/wiki/Speech_perception","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"コミュニケーション障害学","Communication Disorders","Study of aphasia, dysarthria, stuttering, and other language impairments","言語学","Global_Synthesis",1861,"https://en.wikipedia.org/wiki/Communication_disorder","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"テキスト統語論","Text Syntax","Study of grammatical structures above the sentence level in connected discourse","言語学","Western_Europe",1975,"https://en.wikipedia.org/wiki/Syntax","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"インタラクショナル言語学","Interactional Linguistics","Study of grammar in interaction using conversation analysis methods","言語学","Western_Europe",1990,"https://en.wikipedia.org/wiki/Interactional_linguistics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"文字と書記体系","Writing Systems","Typology and history of orthographic and writing systems across languages","言語学","Global_Synthesis",-3200,"https://en.wikipedia.org/wiki/Writing_system","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"語源学","Etymology","Study of the historical development and origin of words","言語学","Western_Europe",-400,"https://en.wikipedia.org/wiki/Etymology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"借用語の研究","Loanword Studies","Study of words borrowed from one language into another and their phonological adaptation","言語学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Loanword","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"プロソディーと意味","Prosody and Meaning","Study of how intonation and stress patterns contribute to propositional and pragmatic meaning","言語学","Western_Europe",1980,"https://en.wikipedia.org/wiki/Prosody_(linguistics)","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"マルチモーダル言語学","Multimodal Linguistics","Study of meaning-making through combinations of language, gesture, and visual modes","言語学","Western_Europe",2000,"https://en.wikipedia.org/wiki/Multimodality","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"音声記号論","Phonological Sign","Study of the phonological component of linguistic signs and its internal structure","言語学","Western_Europe",1916,"https://en.wikipedia.org/wiki/Phoneme","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"語用論の認知的アプローチ","Cognitive Approach to Pragmatics","Relevance theory (Sperber and Wilson) and its account of utterance interpretation","言語学","Western_Europe",1986,"https://en.wikipedia.org/wiki/Relevance_theory","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"手話言語学","Sign Language Linguistics","Study of the grammar and phonology of natural sign languages","言語学","North_America",1960,"https://en.wikipedia.org/wiki/Sign_language","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"言語政策","Language Policy","Study of government and institutional decisions about language use and status","言語学","Global_Synthesis",1960,"https://en.wikipedia.org/wiki/Language_policy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"言語教育学","Language Pedagogy","Study of methods for teaching foreign and second languages","言語学","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Language_education","url_present","dua_wave_a2","active",now(),now()),
    # ===== 宗教学 固有概念 新規 (~20) =====
    (uid(),"メソジズムの歴史","History of Methodism","Study of John Wesley's Methodist movement and evangelical Christianity","宗教学","Western_Europe",1739,"https://en.wikipedia.org/wiki/Methodism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"カルヴァン主義","Calvinism","Reformed Protestant theology of John Calvin: predestination, total depravity, irresistible grace","宗教学","Western_Europe",1536,"https://en.wikipedia.org/wiki/Calvinism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"東方正教会の神学","Eastern Orthodox Theology","Theology of the Eastern Church: theosis, apophatic theology, and hesychasm","宗教学","Western_Europe",1054,"https://en.wikipedia.org/wiki/Eastern_Orthodox_theology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"リベラル神学","Liberal Theology","Nineteenth-century Protestant accommodation of Christianity to modern science and culture","宗教学","Western_Europe",1800,"https://en.wikipedia.org/wiki/Liberal_Christianity","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ネオオーソドキシー神学","Neo-Orthodox Theology","Karl Barth's rejection of liberal theology and return to Reformation emphasis on divine transcendence","宗教学","Western_Europe",1919,"https://en.wikipedia.org/wiki/Neo-orthodoxy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"プロセス神学","Process Theology","Alfred North Whitehead's panentheist theology: God as co-creator with ongoing creation","宗教学","North_America",1929,"https://en.wikipedia.org/wiki/Process_theology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"エコフェミニスト神学","Ecofeminist Theology","Theological reflection connecting the domination of nature and women","宗教学","North_America",1980,"https://en.wikipedia.org/wiki/Ecofeminism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"宗教とセクシュアリティ","Religion and Sexuality","Study of how religious traditions regulate and construct sexuality","宗教学","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Religion_and_sexuality","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"礼拝学","Liturgical Studies","Scholarly study of Christian worship forms, rites, and their historical development","宗教学","Western_Europe",1900,"https://en.wikipedia.org/wiki/Liturgy","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"浄土真宗の神学","Jodo Shinshu Theology","Shinran's Mahayana Buddhist theology of other-power and faith in Amida Buddha","宗教学","East_Asia",1224,"https://en.wikipedia.org/wiki/Jodo_Shinshu","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"日蓮主義","Nichiren Buddhism","Japanese Buddhist movement founded by Nichiren emphasizing the Lotus Sutra","宗教学","East_Asia",1253,"https://en.wikipedia.org/wiki/Nichiren_Buddhism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ジナ教の五戒","Jain Vows","The five great vows of Jain monastics: ahimsa, satya, asteya, brahmacharya, aparigraha","宗教学","South_Asia",-600,"https://en.wikipedia.org/wiki/Jainism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"シク教","Sikhism","Monotheistic religion founded by Guru Nanak in the Punjab combining Hindu and Islamic elements","宗教学","South_Asia",1469,"https://en.wikipedia.org/wiki/Sikhism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"バハイ教","Bahai Faith","Monotheistic religion founded by Baha'u'llah emphasizing unity of religion and humanity","宗教学","West_Asia_North_Africa",1844,"https://en.wikipedia.org/wiki/Bah%C3%A1%27%C3%AD_Faith","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"カオダイ教","Caodaism","Vietnamese syncretic religion combining elements of Buddhism, Taoism, Confucianism, and Christianity","宗教学","East_Asia",1926,"https://en.wikipedia.org/wiki/Caodaism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"トーテミズム","Totemism","Religious and social system based on totemic relationships between humans and animals or plants","宗教学","Global_Synthesis",-5000,"https://en.wikipedia.org/wiki/Totemism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"タブーの宗教学","Religious Taboo","Study of sacred prohibitions in religious traditions: purity, pollution, and the holy","宗教学","Global_Synthesis",-3000,"https://en.wikipedia.org/wiki/Taboo","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"聖典解釈学","Sacred Text Hermeneutics","Study of methods for interpreting sacred scriptures across religious traditions","宗教学","Global_Synthesis",400,"https://en.wikipedia.org/wiki/Biblical_hermeneutics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"祈りの研究","Study of Prayer","Cross-cultural study of prayer as communication with the divine","宗教学","Global_Synthesis",1900,"https://en.wikipedia.org/wiki/Prayer","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"アニミズム","Animism","Belief that spirits or souls inhabit natural objects, central to many indigenous religions","宗教学","Global_Synthesis",-10000,"https://en.wikipedia.org/wiki/Animism","url_present","dua_wave_a2","active",now(),now()),
    # ===== 古典学 固有概念 新規 (~10) =====
    (uid(),"デモクリトス原子論","Democritus Atomism","Pre-Socratic atomic theory of matter as indivisible atoms moving in void","古典学","Western_Europe",-460,"https://en.wikipedia.org/wiki/Atomism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ソクラテスの問答法","Socratic Method","Maieutic method of questioning to reveal interlocutor's assumptions and arrive at truth","古典学","Western_Europe",-470,"https://en.wikipedia.org/wiki/Socratic_method","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"キケロのレトリック","Cicero's Rhetoric","Roman rhetorical theory in De Oratore, Brutus, and Orator","古典学","Western_Europe",-55,"https://en.wikipedia.org/wiki/Cicero","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ロンギノスの崇高論","Longinus on the Sublime","Classical treatise on the elevated style that transports readers to sublime heights","古典学","Western_Europe",100,"https://en.wikipedia.org/wiki/On_the_Sublime","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"プルタルコスの伝記学","Plutarch's Biographical Method","Parallel Lives as a genre of comparative biography for moral exemplification","古典学","Western_Europe",100,"https://en.wikipedia.org/wiki/Parallel_Lives","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"古代インド数学","Ancient Indian Mathematics","Vedic mathematics, zero, decimal notation, and Brahmagupta's contributions","古典学","South_Asia",-1500,"https://en.wikipedia.org/wiki/Indian_mathematics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"中国古典経書","Chinese Classical Canons","Four Books and Five Classics as foundation of Confucian education","古典学","East_Asia",-500,"https://en.wikipedia.org/wiki/Four_Books_and_Five_Classics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"イスラム黄金時代の学問","Islamic Golden Age Scholarship","Translation movement and scientific advances in Baghdad from 8th to 13th centuries","古典学","West_Asia_North_Africa",750,"https://en.wikipedia.org/wiki/Islamic_Golden_Age","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"エジプト神話","Egyptian Mythology","Ancient Egyptian religious myths including creation narratives and afterlife beliefs","古典学","West_Asia_North_Africa",-3100,"https://en.wikipedia.org/wiki/Egyptian_mythology","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"メソポタミア文学","Mesopotamian Literature","Epic of Gilgamesh, hymns to Inanna, and other Sumerian and Akkadian literary works","古典学","West_Asia_North_Africa",-2600,"https://en.wikipedia.org/wiki/Mesopotamian_mythology","url_present","dua_wave_a2","active",now(),now()),
    # ===== 美学・芸術理論 固有概念 新規 (~10) =====
    (uid(),"ミニマリズム美学","Minimalist Aesthetics","Aesthetic philosophy of Donald Judd and Robert Morris: pure objecthood against illusionism","美学・芸術理論","North_America",1965,"https://en.wikipedia.org/wiki/Minimalism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"身体美学","Somaesthetics","Richard Shusterman's program for integrating body practice into aesthetic theory","美学・芸術理論","North_America",1992,"https://en.wikipedia.org/wiki/Somaesthetics","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"コメディーの哲学","Philosophy of Comedy","Theories of humor and comedy from incongruity to superiority and relief theories","美学・芸術理論","Western_Europe",1790,"https://en.wikipedia.org/wiki/Humor","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ゲームの美学","Aesthetics of Games","Philosophical analysis of games as an art form and the aesthetics of play","美学・芸術理論","Global_Synthesis",2000,"https://en.wikipedia.org/wiki/Game_studies","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ストリートアートの美学","Aesthetics of Street Art","Philosophical questions about graffiti, Banksy, and art in public space","美学・芸術理論","Global_Synthesis",1970,"https://en.wikipedia.org/wiki/Street_art","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"音楽と感情","Music and Emotion","Philosophical analysis of how music expresses and arouses emotion","美学・芸術理論","Western_Europe",1800,"https://en.wikipedia.org/wiki/Music_and_emotion","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"ダンスの美学","Aesthetics of Dance","Philosophical analysis of dance as an art form: expression, abstraction, and the body","美学・芸術理論","Global_Synthesis",1950,"https://en.wikipedia.org/wiki/Dance","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"芸術の定義問題","Definition of Art Problem","The open question of what defines something as art: Weitz, Dickie, Levinson","美学・芸術理論","North_America",1956,"https://en.wikipedia.org/wiki/Definition_of_art","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"美的多元主義","Aesthetic Pluralism","View that there are multiple irreducible standards of aesthetic value","美学・芸術理論","Global_Synthesis",1990,"https://en.wikipedia.org/wiki/Aesthetic_pluralism","url_present","dua_wave_a2","active",now(),now()),
    (uid(),"演劇の美学","Aesthetics of Theatre","Philosophical analysis of theatrical performance, acting theory, and Brechtian theatre","美学・芸術理論","Western_Europe",1800,"https://en.wikipedia.org/wiki/Theatre_theory","url_present","dua_wave_a2","active",now(),now()),
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
    print(f"レコード総数: {len(RECORDS)}")
    print(f"inserted={inserted}, skipped={skipped}")
    print(f"総件数: {total} (目標5500)")
    con.close()

if __name__ == "__main__":
    main()
