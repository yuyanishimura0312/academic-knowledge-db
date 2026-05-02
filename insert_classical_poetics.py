#!/usr/bin/env python3
"""Insert classical poetics concepts, researchers, and relations into academic.db"""

import sqlite3
import uuid
import json
from datetime import datetime

DB_PATH = "academic.db"

def gen_id():
    return str(uuid.uuid4())

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")

    now = datetime.now().isoformat()

    # ========== RESEARCHERS ==========
    researchers = [
        {
            "id": "res_plato",
            "name_full": "Plato",
            "name_ja": "プラトン",
            "birth_year": -427,
            "death_year": -347,
            "nationality": "古代ギリシャ（アテナイ）",
            "primary_institution": "アカデメイア",
            "research_themes": "イデア論に基づく観念論的形而上学。現象世界の背後にある永遠不変のイデアの世界を主張。詩と芸術のミメーシス批判、教育論、政治哲学を展開。対話篇形式による哲学的探究の創始者。",
            "biography_brief": "アテナイの貴族家庭に生まれ、ソクラテスに師事。前387年にアカデメイアを創設し、40年にわたり哲学・数学・天文学を教授。アリストテレスを含む多くの弟子を育成。"
        },
        {
            "id": "res_aristotle",
            "name_full": "Aristotle",
            "name_ja": "アリストテレス",
            "birth_year": -384,
            "death_year": -322,
            "nationality": "古代マケドニア（スタギラ）",
            "primary_institution": "リュケイオン",
            "research_themes": "経験と観察に基づく実証的哲学の確立。形而上学、論理学、倫理学、政治学、自然学、詩学を体系化した「諸学の父」。プラトンのイデア論を批判しつつ独自の存在論を構築。",
            "biography_brief": "17歳でアカデメイアに入学し20年間プラトンに師事。アレクサンドロス大王の家庭教師を務めた後、前335年にリュケイオンを創設。逍遥学派を形成。"
        },
        {
            "id": "res_horace",
            "name_full": "Quintus Horatius Flaccus",
            "name_ja": "ホラティウス",
            "birth_year": -65,
            "death_year": -8,
            "nationality": "古代ローマ",
            "primary_institution": None,
            "research_themes": "ラテン抒情詩と風刺詩の大家。『詩論』でアリストテレスの理論をローマの実践に適応させ、詩作の規範を確立。「教えと楽しみ」の統合、デコールムの原則を提唱。",
            "biography_brief": "イタリア南部ヴェヌシアの解放奴隷の子として出生。内戦後マエケナスの庇護を得て詩作に専念。アウグストゥス期ローマの第一級詩人としてヴェルギリウスと並称される。"
        },
        {
            "id": "res_longinus",
            "name_full": "Pseudo-Longinus",
            "name_ja": "プセウド・ロンギノス",
            "birth_year": None,
            "death_year": None,
            "nationality": "ローマ帝国（1世紀）",
            "primary_institution": None,
            "research_themes": "文学批評と美学の統合。崇高性（hypsos）を精神の偉大さの表現として理論化。古典的な調和の美学を超えた新しい美的カテゴリーの確立。修辞学的技法と精神的高揚の関係を考察。",
            "biography_brief": "正体不明。当初3世紀のカッシウス・ロンギヌスに帰されたが、現在は1世紀の著者と推定。『崇高について』は10世紀写本から著者が「ディオニュシウスあるいはロンギヌス」と記載。"
        },
        {
            "id": "res_cicero",
            "name_full": "Marcus Tullius Cicero",
            "name_ja": "キケロ",
            "birth_year": -106,
            "death_year": -43,
            "nationality": "古代ローマ",
            "primary_institution": None,
            "research_themes": "ラテン修辞学の基礎確立。理想の弁論家像を「学識と政治経験を兼ね備え市民の利益に奉仕する指導者」と定義。五技法の統合、三文体論の発展。ギリシャ哲学のラテン語化。",
            "biography_brief": "ローマ南東部の騎士階級に生まれた。前63年にカティリナの陰謀を告発し「国父」の称号を受ける。共和制末期の最大の弁論家・政治家。前43年にマルク・アントニウスにより殺害。"
        },
        {
            "id": "res_quintilian",
            "name_full": "Marcus Fabius Quintilianus",
            "name_ja": "クインティリアヌス",
            "birth_year": 35,
            "death_year": 100,
            "nationality": "ローマ帝国（ヒスパニア）",
            "primary_institution": None,
            "research_themes": "修辞学教育の体系化。12巻『弁論家の教育』でキケロの思想を教育論に発展。完全な弁論家は徳の人であるべきという倫理的要求。トロポスとスケーマの分類体系を確立。",
            "biography_brief": "ヒスパニアのカラグリス出身。ローマで教育を受けた後、ウェスパシアヌス帝の下で国家給与を受ける最初のラテン修辞学教師となる。88年に引退後『弁論家の教育』を完成。"
        }
    ]

    for r in researchers:
        try:
            conn.execute("""
                INSERT OR IGNORE INTO researchers (id, name_full, name_ja, birth_year, death_year, nationality, primary_institution, research_themes, biography_brief, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (r["id"], r["name_full"], r["name_ja"], r["birth_year"], r["death_year"],
                  r["nationality"], r["primary_institution"], r["research_themes"], r["biography_brief"], now, now))
        except Exception as e:
            print(f"  Researcher {r['name_ja']}: {e}")

    print(f"Inserted {len(researchers)} researchers")

    # ========== CONCEPTS ==========
    concepts = [
        # --- Plato ---
        {
            "id": "cp_mimesis_critique",
            "name_ja": "ミメーシス（模倣）批判",
            "name_en": "Critique of Mimesis",
            "name_original": "μίμησις (mimēsis) κρίσις",
            "definition": "プラトンが『国家』第10巻で展開した芸術批判。芸術作品はイデアの模倣である現実世界をさらに模倣した「模倣の模倣」であり、真実から三段階離れた虚妄であると主張。詩や絵画は認識論的に劣り、魂の非理性的部分に訴えかけて人間を真理から遠ざけるとした。西洋芸術哲学の根本的出発点となった問題提起。",
            "impact_summary": "芸術の認識論的・倫理的正当性をめぐる2400年間の論争の出発点。アリストテレスの反論、ルネサンスの芸術擁護論、現代のフィクション論すべてがこの批判に応答している。",
            "subfield": "古典詩学",
            "school_of_thought": "プラトン哲学・イデア論",
            "era_start": -380,
            "era_end": None,
            "keywords_ja": "ミメーシス,模倣,イデア論,芸術批判,真実と虚構",
            "keywords_en": "mimesis,imitation,Theory of Forms,art criticism",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "芸術を無条件に肯定する態度に対し、表象と実在の乖離という根本問題を提起。芸術が真実を伝えるという素朴な信念を問い直す。",
            "reinterpretation_history": "アリストテレスがミメーシスを肯定的に再定義（前335年）。ルネサンス期に自然模倣と理想形式の問題として再解釈。現代ではボードリヤールのシミュラクル論が継承。",
            "cultural_context": "アテナイの演劇文化が社会に大きな影響力を持つ時代。ソフィストの修辞術と詩人の影響力に対する哲学的対抗として提出。",
            "originator": "res_plato",
            "year_proposed": -380,
            "founding_work": "プラトン『国家（Politeia）』第10巻"
        },
        {
            "id": "cp_poet_banishment",
            "name_ja": "詩人追放論",
            "name_en": "Banishment of Poets",
            "name_original": "τοὺς ποιητὰς ἐκβάλλειν",
            "definition": "プラトンが理想国家の構想において、模倣詩人を国家から追放すべきと主張した政治哲学的議論。詩人は真実を知らず、感情を煽り、市民の魂の非理性的部分を強化するため、教育的・政治的に有害であるとした。ただし神々への賛歌と善人の頌歌のみは許容される。",
            "impact_summary": "芸術と政治の関係、検閲の正当性をめぐる永続的な論争の原型。近代の芸術規制論・表現の自由論の思想的起源。",
            "subfield": "古典詩学",
            "school_of_thought": "プラトン哲学・政治哲学",
            "era_start": -380,
            "era_end": None,
            "keywords_ja": "詩人追放,検閲,芸術と政治,教育,理想国家",
            "keywords_en": "banishment of poets,censorship,art and politics,ideal state",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "芸術の自律性を自明視する近代的態度に対し、芸術が持つ政治的・教育的影響力の問題を提起。",
            "reinterpretation_history": "中世教会による世俗芸術への警戒に継承。近代では表現の自由と公共善の緊張として再解釈。シドニー『詩の擁護』が直接反論。",
            "cultural_context": "アテナイ民主制における詩人・劇作家の社会的影響力への懸念。ソフィストの弁論術が政治を操作する危険性の認識。",
            "originator": "res_plato",
            "year_proposed": -380,
            "founding_work": "プラトン『国家（Politeia）』第2-3巻・第10巻"
        },
        {
            "id": "cp_divine_inspiration",
            "name_ja": "霊感説（神的狂気）",
            "name_en": "Divine Inspiration (Poetic Madness)",
            "name_original": "θεία μανία (theia mania)",
            "definition": "プラトンが『イオン』『パイドロス』で展開した詩作の起源論。詩人は自らの技術や知識によってではなく、神的な霊感（エンスージアスモス）によって詩を生む。ムーサに憑依された詩人は磁石の連鎖のように聴衆に感動を伝達する。理性的認識とは異なる神的認識の通路としての詩。",
            "impact_summary": "ロマン主義の天才論・霊感論の古典的原型。シェリー、コールリッジらの想像力論に直接影響。創作における無意識・直感の役割をめぐる議論の起点。",
            "subfield": "古典詩学",
            "school_of_thought": "プラトン哲学",
            "era_start": -380,
            "era_end": None,
            "keywords_ja": "神的狂気,霊感,エンスージアスモス,ムーサ,創作の起源",
            "keywords_en": "divine madness,inspiration,enthusiasm,Muses,creative origin",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "創作を純粋に技術的・理性的過程とみなす態度に対し、非理性的・超越的次元の不可避性を示す。",
            "reinterpretation_history": "新プラトン主義が神秘主義的に継承。ルネサンスで「天才（ingenium）」概念に世俗化。ロマン主義で想像力論として復活。フロイトが無意識の創造性として心理学化。",
            "cultural_context": "古代ギリシャの宗教的世界観。デルフォイの神託、ディオニュソス祭での恍惚状態など、脱我的経験が文化的に認知されていた。",
            "originator": "res_plato",
            "year_proposed": -380,
            "founding_work": "プラトン『イオン（Ion）』『パイドロス（Phaedrus）』245a"
        },
        # --- Aristotle Poetics ---
        {
            "id": "cp_mimesis",
            "name_ja": "ミメーシス（模倣）",
            "name_en": "Mimesis (Imitation/Representation)",
            "name_original": "μίμησις (mimēsis)",
            "definition": "アリストテレスが『詩学』で再定義した芸術の基本原理。プラトンのミメーシス批判を反転させ、模倣を人間の自然な本性（学習の手段）として肯定。詩の模倣は単なる表面的コピーではなく、事物の本質的構造（蓋然性・必然性に基づく因果関係）を提示する知的営為。歴史が「起こったこと」を語るのに対し、詩は「起こり得ること」を語る点でより哲学的である。",
            "impact_summary": "西洋芸術理論の中心概念。リアリズム文学、演劇論、映画理論に至るまで「表象とは何か」という問いの基盤を形成。アウエルバッハ『ミメーシス』で20世紀文学批評の基軸に。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "ミメーシス,模倣,表象,本質的構造,蓋然性",
            "keywords_en": "mimesis,imitation,representation,essential structure,probability",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "芸術を真実から遠ざかるものとする見方に対し、芸術固有の真実へのアクセス方法を示す。個別的事実を超えた普遍的真実の表現としての芸術。",
            "reinterpretation_history": "中世アラビア哲学者が保存・注釈。ルネサンスで自然模倣と理想化の問題として再解釈。18世紀に「美しい芸術」概念に吸収。アウエルバッハ（1946年）が文学史の分析枠組みとして復活。",
            "cultural_context": "アテナイの演劇文化の中で、悲劇・喜劇・叙事詩が市民教育の重要な手段として機能していた時代。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第1-4章"
        },
        {
            "id": "cp_catharsis",
            "name_ja": "カタルシス（浄化）",
            "name_en": "Catharsis (Purgation/Purification)",
            "name_original": "κάθαρσις (katharsis)",
            "definition": "アリストテレスが悲劇の定義において導入した概念。悲劇は同情（エレオス）と恐怖（ポボス）の感情を喚起し、これらの感情の浄化（カタルシス）をもたらすとした。解釈は医学的浄化説（感情の排出）、道徳的浄化説（感情の適正化）、認知的明晰化説（感情を通じた理解の深化）に分かれ、2300年間論争が続く。",
            "impact_summary": "芸術の感情的効果に関する最も影響力のある理論。フロイトの精神分析、演劇療法、映画理論に至るまで広範に応用。芸術体験の治療的・教育的価値の理論的根拠。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "カタルシス,浄化,同情,恐怖,感情の浄化,悲劇",
            "keywords_en": "catharsis,purgation,pity,fear,emotional purification,tragedy",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "感情を理性の敵とみなすプラトン的態度に対し、感情体験を通じた精神の健全化という治療的機能を提示。",
            "reinterpretation_history": "ルネサンスでカステルヴェトロが観客の快楽として解釈。レッシングが道徳的効果として再定義（1767年）。ベルナイスが医学的浄化説を提唱（1857年）。フロイトがアブリアクション概念に応用。",
            "cultural_context": "古代ギリシャの演劇祭（大ディオニュシア祭）における市民全体の集団的感情体験。医学的概念（体液の浄化）からの借用。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第6章 1449b"
        },
        {
            "id": "cp_peripeteia",
            "name_ja": "ペリペテイア（逆転）",
            "name_en": "Peripeteia (Reversal of Fortune)",
            "name_original": "περιπέτεια (peripeteia)",
            "definition": "悲劇の筋立てにおいて、行為が意図した結果とは反対の方向に急転する展開。アリストテレスが複雑な筋（ペプレグメノス・ミュトス）の必須要素として規定。単なる偶然的変化ではなく、蓋然性と必然性に基づく因果的逆転でなければならない。『オイディプス王』で使者がオイディプスを安心させようとして逆に真実を暴く場面が典型例。",
            "impact_summary": "劇作法における転換点の理論化。シェイクスピアからハリウッド映画に至るプロット構成の基本原理。ストーリーテリングの普遍的構造要素として機能。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "逆転,プロット,転換点,因果的必然性,複雑な筋",
            "keywords_en": "peripeteia,reversal,plot,turning point,complex plot",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "物語の展開を偶然や恣意的な仕掛けで説明する態度に対し、逆転が持つ因果論的必然性と認知的衝撃の構造を明らかにする。",
            "reinterpretation_history": "ルネサンス詩学で三一律と結合。フライタークが五幕構成の転換点として位置づけ（1863年）。現代の脚本術（シド・フィールドのパラダイム）が継承。",
            "cultural_context": "アテナイの悲劇コンテスト（大ディオニュシア祭）において、観客の感情的反応を最大化する劇作技法として発展。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第11章 1452a"
        },
        {
            "id": "cp_anagnorisis",
            "name_ja": "アナグノリシス（認知・発見）",
            "name_en": "Anagnorisis (Recognition/Discovery)",
            "name_original": "ἀναγνώρισις (anagnōrisis)",
            "definition": "無知から知への転換。主人公が自身の真の身分や状況の真相を認識する瞬間。アリストテレスはペリペテイアと同時に生じるアナグノリシスを最も優れた劇的効果とした。六種類を分類し、最も高貴な形式は行為の内的論理から自然に生じるものとした。",
            "impact_summary": "推理小説・探偵物語の「真相の暴露」の構造的原型。心理劇における自己認識の瞬間の理論化。物語理論における情報の非対称性と開示の力学の基礎。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "認知,発見,無知から知へ,自己認識,真相暴露",
            "keywords_en": "anagnorisis,recognition,discovery,self-knowledge,revelation",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "物語の知的快楽を単なる情報の提供として扱う態度に対し、認識の転換がもたらす存在論的衝撃の構造を示す。",
            "reinterpretation_history": "テレンティウスらローマ喜劇で「取り違え」のモチーフとして展開。推理小説ジャンルの構造的基盤。現代ナラトロジーで「信頼できない語り手」の理論に発展。",
            "cultural_context": "ギリシャ悲劇における運命の力と人間の限界の認識。オイディプス神話に典型的な「知ることの恐怖」。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第11章・第16章"
        },
        {
            "id": "cp_hamartia",
            "name_ja": "ハマルティア（過ち）",
            "name_en": "Hamartia (Tragic Error/Flaw)",
            "name_original": "ἁμαρτία (hamartia)",
            "definition": "悲劇の主人公の転落を引き起こす判断の誤りまたは性格上の欠陥。道徳的堕落（悪徳）ではなく、善き人間が犯す過誤であることが重要。主人公は完全な善人でも完全な悪人でもなく、我々に似た人物でなければならない。「悲劇的欠陥」として知られるが、原義は「的を外す」こと。",
            "impact_summary": "悲劇のプロット論における主人公造形の基本原理。シェイクスピア悲劇、近代心理劇の登場人物設計の理論的基盤。道徳と運命の関係をめぐる倫理的議論の起点。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "ハマルティア,過ち,悲劇的欠陥,判断の誤り,転落",
            "keywords_en": "hamartia,tragic flaw,error,judgment,downfall",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "不幸を完全な悪徳か純粋な不運に帰する単純化に対し、善き人間が構造的に陥る過誤という中間領域を照らす。",
            "reinterpretation_history": "中世キリスト教文脈で「罪（sin）」と同一視。ブラッドリーが「性格的欠陥」説を主張（1904年）。現代では「判断の誤り」説が主流。",
            "cultural_context": "ギリシャ悲劇における人間の有限性と神々の力の非対称性。ヒュブリス（傲慢）との関連。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第13章 1453a"
        },
        {
            "id": "cp_mythos",
            "name_ja": "ミュトス（筋立て）",
            "name_en": "Mythos (Plot/Story Structure)",
            "name_original": "μῦθος (mythos)",
            "definition": "アリストテレスが悲劇の六要素の中で最も重要と位置づけた「出来事の配列」。単なる出来事の時系列的羅列ではなく、蓋然性と必然性に基づく因果的連鎖。始まり・中間・終わりを持つ有機的統一体であり、過不足なく完結する全体。悲劇の「魂」と称された。",
            "impact_summary": "物語構造論の出発点。プロップの物語形態学、グレマスの行為素モデル、フライタークの五幕構成すべてがミュトス概念の展開。プロット中心の劇作法の理論的基盤。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "筋立て,プロット,因果構造,有機的統一,出来事の配列",
            "keywords_en": "mythos,plot,causal structure,organic unity,arrangement of events",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "物語を「何が起きたか」の記録と見る態度に対し、出来事間の因果的必然性による構成という能動的設計の次元を示す。",
            "reinterpretation_history": "ロシア・フォルマリズムでファビュラ/シュジェート区分に発展。構造主義ナラトロジーで物語の深層構造分析に継承。",
            "cultural_context": "ギリシャの口承文化からテキスト文化への移行期。叙事詩の韻文的蓄積から戯曲の因果的構成への転換。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第6-7章"
        },
        {
            "id": "cp_six_elements",
            "name_ja": "悲劇の六要素",
            "name_en": "Six Elements of Tragedy",
            "name_original": "μέρη τραγῳδίας (merē tragōidias)",
            "definition": "アリストテレスが悲劇の構成要素として同定した六つの部分。重要度順に: (1)ミュトス（筋立て）、(2)エートス（性格）、(3)ディアノイア（思想）、(4)レクシス（語法・言語表現）、(5)メロス（歌曲）、(6)オプシス（視覚的装飾）。筋立てが最重要であり、性格は筋に従属する。",
            "impact_summary": "演劇批評・劇作法の分析枠組みとして2300年間使用。テキストvs.パフォーマンス、物語vs.スペクタクルの優先度論争の原型。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "六要素,悲劇の構造,ミュトス,エートス,ディアノイア,レクシス",
            "keywords_en": "six elements,tragedy structure,mythos,ethos,dianoia,lexis",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "演劇を未分化な総合芸術として扱う態度に対し、構成要素間の階層関係と各要素の固有の機能を析出。",
            "reinterpretation_history": "ルネサンス新古典主義で規範的に採用。ブレヒトが筋立ての優位を批判し叙事的演劇を提唱。現代演劇では六要素の相対化が進む。",
            "cultural_context": "古代ギリシャ悲劇が合唱隊の歌・対話・舞踊の複合芸術であった環境から、各要素を分析的に識別する必要があった。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第6章 1450a-b"
        },
        {
            "id": "cp_probability_necessity",
            "name_ja": "蓋然性と必然性",
            "name_en": "Probability and Necessity",
            "name_original": "τὸ εἰκὸς ἢ τὸ ἀναγκαῖον (to eikos ē to anankaion)",
            "definition": "アリストテレスが詩的真実の基準として導入した概念対。詩は「起こったこと」ではなく「起こり得ること」を蓋然性または必然性に基づいて語る。不可能だが説得力あることは、可能だが信じがたいことに勝る。これにより詩は歴史より「哲学的」であるとされた。",
            "impact_summary": "フィクションの認識論的正当化の基盤。「詩的真実」と「歴史的事実」の区別は、文学理論における虚構論の出発点。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "蓋然性,必然性,詩的真実,虚構の正当化,可能的なもの",
            "keywords_en": "probability,necessity,poetic truth,fictional justification,possible worlds",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "「事実に基づかないものは嘘」という素朴実在論に対し、虚構が把握する普遍的真実の認識論的価値を示す。",
            "reinterpretation_history": "中世でアヴェロエスがイスラム文脈で再解釈。ルネサンスで「ヴェリシミリチュード（真実らしさ）」として規範化。現代の可能世界意味論に影響。",
            "cultural_context": "ギリシャの歴史叙述（ヘロドトス、トゥキュディデス）と詩作の分業が明確化しつつあった時代。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第9章 1451a-b"
        },
        {
            "id": "cp_poetry_vs_history",
            "name_ja": "詩と歴史の区別",
            "name_en": "Poetry vs. History",
            "name_original": "ποίησις καὶ ἱστορία",
            "definition": "アリストテレスの最も有名な主張の一つ。詩は「起こり得ること」を普遍的に語り、歴史は「起こったこと」を個別的に語る。詩は歴史より哲学的（philosophōteron）である。なぜなら詩は普遍を語るのに対し、歴史は個別を語るからである。詩人の仕事は実際に起こったことを語ることではなく、起こり得ることを語ることにある。",
            "impact_summary": "文学と歴史の学問的区分の理論的基盤。ホワイト『メタヒストリー』に至る歴史叙述の詩学的分析の起点。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "詩と歴史,普遍と個別,虚構と事実,哲学的",
            "keywords_en": "poetry and history,universal and particular,fiction and fact",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "個別事実の集積が知識の本質であるとする態度に対し、虚構が持つ普遍的認識の独自の価値を示す。",
            "reinterpretation_history": "シドニー『詩の擁護』で中心的論拠として引用。ヘーゲルの芸術哲学で精神の自己展開として再解釈。ヘイデン・ホワイトが歴史叙述と詩の境界を問い直す。",
            "cultural_context": "ヘロドトスとトゥキュディデスによる歴史叙述の確立期。歴史と詩の社会的機能の分化。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第9章"
        },
        {
            "id": "cp_genre_theory",
            "name_ja": "ジャンル論（三区分）",
            "name_en": "Genre Theory (Tripartite Division)",
            "name_original": "εἴδη ποιήσεως",
            "definition": "アリストテレスが詩を模倣の手段（韻律・リズム・メロディ）、模倣の対象（優れた人物か劣った人物か）、模倣の様式（語りか演技か）の三つの基準で分類した体系。悲劇は優れた人物を演技で模倣し、喜劇は劣った人物を模倣し、叙事詩は優れた人物を語りで模倣する。",
            "impact_summary": "文学ジャンル論の出発点。ルネサンスの厳格なジャンル規範からロマン主義のジャンル混淆まで、すべてのジャンル議論の基準点。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "ジャンル,悲劇,喜劇,叙事詩,模倣の三基準",
            "keywords_en": "genre,tragedy,comedy,epic,modes of imitation",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "文学作品を個別的に評価する態度に対し、ジャンルという類型的枠組みの認知的機能を示す。",
            "reinterpretation_history": "ルネサンスで厳格なジャンル規範に発展。ロマン主義が混合ジャンルを擁護。バフチンが小説のジャンル論で根本的に再構成。",
            "cultural_context": "古代ギリシャにおける悲劇・喜劇・叙事詩・抒情詩の明確な社会的機能分化。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第1-3章"
        },
        {
            "id": "cp_tragedy_def",
            "name_ja": "悲劇の定義",
            "name_en": "Definition of Tragedy",
            "name_original": "ὅρος τραγῳδίας",
            "definition": "アリストテレスの有名な定義:「悲劇とは、重大で完結した一定の大きさを持つ行為の模倣であり、快い言葉で飾られ、それぞれ適切な場所に各種の装飾が施され、語り（叙述）によってではなく行為する人々（登場人物）によって演じられ、同情と恐怖を通じて、そうした感情の浄化を達成するものである」。悲劇論の全体がこの定義から展開される。",
            "impact_summary": "西洋演劇の基本定義。この定義の各要素（行為の模倣、完結性、適切な大きさ、感情の浄化）が独立した理論的探究の対象となった。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "悲劇の定義,行為の模倣,完結性,カタルシス,感情の浄化",
            "keywords_en": "definition of tragedy,imitation of action,completeness,catharsis",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "悲劇を単に「悲しい結末の物語」と素朴に理解する態度に対し、構造的・感情的・倫理的に規定された複合的概念を提示。",
            "reinterpretation_history": "ルネサンスで規範的定義として採用。ニーチェが『悲劇の誕生』でディオニュソス的次元から再構成。20世紀に「悲劇の死」論争。",
            "cultural_context": "ディオニュソス祭における悲劇コンテストの文化制度。悲劇が宗教的・政治的・教育的機能を担う社会的文脈。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第6章 1449b"
        },
        {
            "id": "cp_metaphor",
            "name_ja": "メタファー（隠喩）",
            "name_en": "Metaphor",
            "name_original": "μεταφορά (metaphora)",
            "definition": "アリストテレスが『詩学』と『弁論術』で体系化した比喩の理論。「あるものに別のものに属する名前を転用すること」と定義。種から類へ、類から種へ、種から種へ、比例関係による四種類を分類。メタファーの才能は教えることができない唯一の資質であり、天賦のものとした。後の認知言語学の「概念メタファー理論」の直接的起源。",
            "impact_summary": "修辞学・詩学・言語哲学・認知科学を横断する中心概念。リクールのメタファー論、ラコフ&ジョンソンの概念メタファー理論に至る。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学・修辞学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "隠喩,メタファー,比喩,名前の転用,概念的思考",
            "keywords_en": "metaphor,figurative language,transference,conceptual thinking",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "言語を字義的意味の伝達手段とみなす態度に対し、比喩的認知が人間の思考の本質的構造であることを示す。",
            "reinterpretation_history": "中世修辞学で装飾的修辞技法に矮小化。リチャーズ（1936年）が「相互作用理論」で復権。ブラック（1955年）が発展。ラコフ&ジョンソン（1980年）が認知的基盤を実証。",
            "cultural_context": "ギリシャの修辞術教育における言語技法の体系化。法廷弁論と演説における説得技法としての重要性。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学』第21章、『弁論術』第3巻第10-11章"
        },
        {
            "id": "cp_poetic_license",
            "name_ja": "詩的ライセンス（詩的自由）",
            "name_en": "Poetic License",
            "name_original": "ποιητικὴ ἄδεια",
            "definition": "アリストテレスが『詩学』第25章で論じた詩人の特権的自由。詩は科学的・道徳的正確さとは異なる独自の評価基準を持つ。不可能だが説得力あることは、可能だが信じがたいことに勝る。詩における「誤り」は、詩の本質的目的（感情の喚起と浄化）を損なうかどうかで判断される。",
            "impact_summary": "芸術の自律性論の古典的根拠。芸術を科学・道徳から独立した評価基準で判断すべきとする主張の原型。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "詩的自由,芸術の自律性,詩固有の評価基準,創作の許容範囲",
            "keywords_en": "poetic license,artistic autonomy,standards of poetry",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "科学的・道徳的に正しいかという外部基準で芸術を評価する態度に対し、詩固有の評価基準の存在を主張。",
            "reinterpretation_history": "18世紀以降「芸術のための芸術」運動が自律性論を急進化。カントの美学が「目的なき合目的性」として哲学化。",
            "cultural_context": "詩人批評家がホメロスの科学的・道徳的誤りを攻撃した時代的文脈への応答。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第25章"
        },
        # --- Horace ---
        {
            "id": "cp_decorum",
            "name_ja": "デコールム（適切さ）",
            "name_en": "Decorum (Propriety)",
            "name_original": "decorum / τὸ πρέπον (to prepon)",
            "definition": "ホラティウスが『詩論』で体系化した詩作の基本原則。登場人物の言動はその身分・年齢・職業に適切でなければならない。ジャンルと文体の適合、主題と表現の調和、部分と全体の統一を要求する包括的な美的規範。キケロの修辞学的デコールムを詩作に応用・発展させたもの。",
            "impact_summary": "新古典主義詩学の中心原理。17世紀フランス古典主義（ラシーヌ、コルネイユ）の劇作規範。社会的身分と言語表現の対応関係の理論化。",
            "subfield": "古典詩学",
            "school_of_thought": "ホラティウスの詩学・新古典主義",
            "era_start": -19,
            "era_end": None,
            "keywords_ja": "適切さ,デコールム,身分と言語,ジャンルと文体,調和",
            "keywords_en": "decorum,propriety,fitness,genre and style,harmony",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "表現の自由を無制限に肯定する態度に対し、社会的文脈における表現の適切さという規範的次元を提示。",
            "reinterpretation_history": "ルネサンスで厳格な規範に発展。17世紀フランス古典主義の中核原理に。ロマン主義が破壊。現代ではジャンル理論の文脈で部分的に復活。",
            "cultural_context": "アウグストゥス期ローマの秩序と調和の美学。社会的階層構造の文化的表現としての文学。",
            "originator": "res_horace",
            "year_proposed": -19,
            "founding_work": "ホラティウス『詩論（Ars Poetica）』第86-118行"
        },
        {
            "id": "cp_prodesse_delectare",
            "name_ja": "教えと楽しみ（prodesse et delectare）",
            "name_en": "Instruction and Delight",
            "name_original": "prodesse et delectare / aut prodesse aut delectare",
            "definition": "ホラティウスが詩の二重目的として定式化した原則。詩は教え（prodesse）と楽しみ（delectare）を両立させるべきであり、有用と快楽を混合する詩人が最大の評価を得る。アリストテレスのカタルシス概念をより実用的・教育的方向に再解釈したもの。芸術の社会的機能をめぐる議論の規範的基準。",
            "impact_summary": "ルネサンスから18世紀まで西洋文学理論の支配的原理。文学教育の正当化論拠。「芸術のための芸術」vs.「社会的責任」論争の起点。",
            "subfield": "古典詩学",
            "school_of_thought": "ホラティウスの詩学",
            "era_start": -19,
            "era_end": None,
            "keywords_ja": "教えと楽しみ,有用と快楽,詩の社会的機能,教育と娯楽",
            "keywords_en": "instruction and delight,utility and pleasure,social function of poetry",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "芸術を純粋な娯楽か純粋な教化のいずれかに二分する態度に対し、両者の不可分性を示す。",
            "reinterpretation_history": "シドニー『詩の擁護』が中心的論拠として採用。18世紀に「趣味」論と結合。唯美主義が教育的側面を否定。現代の「エデュテインメント」概念が世俗的に復活。",
            "cultural_context": "ローマ社会における詩のパトロネージ制度。マエケナス・アウグストゥスによる文化政策としての詩の奨励。",
            "originator": "res_horace",
            "year_proposed": -19,
            "founding_work": "ホラティウス『詩論（Ars Poetica）』第333-346行"
        },
        {
            "id": "cp_ut_pictura_poesis",
            "name_ja": "詩は絵のごとし（ut pictura poesis）",
            "name_en": "Ut Pictura Poesis (As is Painting so is Poetry)",
            "name_original": "ut pictura poesis",
            "definition": "ホラティウスが『詩論』で述べた詩と絵画の類比。本来は「ある詩は近くで見ると良く、ある詩は遠くから見ると良い」という鑑賞論だったが、後世では姉妹芸術論（詩と絵画は同等の芸術である）として拡大解釈された。レッシングの『ラオコーン』による批判まで、西洋芸術論を支配した原理。",
            "impact_summary": "ルネサンス芸術理論の基盤。レオナルド・ダ・ヴィンチの「パラゴーネ（芸術比較論）」、レッシング『ラオコーン』の時間芸術/空間芸術論の前提。比較芸術学の起源。",
            "subfield": "古典詩学",
            "school_of_thought": "ホラティウスの詩学・姉妹芸術論",
            "era_start": -19,
            "era_end": None,
            "keywords_ja": "詩画一致論,姉妹芸術,時間芸術と空間芸術,比較芸術学",
            "keywords_en": "ut pictura poesis,sister arts,time arts and space arts,comparative arts",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "各芸術ジャンルを完全に独立したものとして扱う態度に対し、異なる媒体間の構造的類似性と相互参照の可能性を示す。",
            "reinterpretation_history": "ルネサンスで詩画一致論として規範化。レッシング（1766年）が時間芸術vs空間芸術として批判的に再構成。現代のインターメディア論に発展。",
            "cultural_context": "古代ギリシャのシモニデスの格言「絵画は沈黙する詩であり、詩は語る絵画である」の系譜。ローマの壁画文化と文学の並行的発展。",
            "originator": "res_horace",
            "year_proposed": -19,
            "founding_work": "ホラティウス『詩論（Ars Poetica）』第361行"
        },
        # --- Longinus ---
        {
            "id": "cp_hypsos",
            "name_ja": "ヒュプソス（崇高）",
            "name_en": "Hypsos (The Sublime)",
            "name_original": "ὕψος (hypsos)",
            "definition": "ロンギノスが『崇高について』で理論化した美的カテゴリー。崇高とは聴衆を圧倒し、精神を高揚させる文学的表現の卓越した力。美（調和・均整）とは異なる独立した美的カテゴリーとして、驚嘆・畏怖・精神的高揚をもたらす。「崇高は偉大な精神の反響である」。技術的完成度ではなく、天才的な閃きから生まれる。",
            "impact_summary": "18世紀美学革命の直接的起源。バークの崇高論、カントの数学的/力学的崇高の分析、ロマン主義美学の「美を超えるもの」への志向すべてに影響。現代の「驚嘆（awe）」研究に継承。",
            "subfield": "古典詩学",
            "school_of_thought": "古代崇高論",
            "era_start": 100,
            "era_end": None,
            "keywords_ja": "崇高,ヒュプソス,偉大さ,精神の高揚,驚嘆",
            "keywords_en": "sublime,hypsos,greatness,elevation of spirit,awe",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "美を調和・均整・秩序に限定する古典主義的態度に対し、圧倒的な力・規模・深さという別種の美的価値を提示。",
            "reinterpretation_history": "1674年ボワロー訳で18世紀崇高論の基準テクストに。バーク（1757年）が恐怖との連関を分析。カント（1790年）が数学的/力学的崇高に二分。リオタール（1984年）がポストモダン崇高として再構成。",
            "cultural_context": "帝政ローマ初期の文化的衰退の診断。「現代の文学がなぜ崇高でないか」という問いへの応答を含む政治文化論。",
            "originator": "res_longinus",
            "year_proposed": 100,
            "founding_work": "プセウド・ロンギノス『崇高について（Peri Hypsous）』"
        },
        {
            "id": "cp_five_sources",
            "name_ja": "崇高の五源泉",
            "name_en": "Five Sources of Sublimity",
            "name_original": "πέντε πηγαὶ τοῦ ὕψους",
            "definition": "ロンギノスが体系化した崇高な文学を生む五つの根源。(1)偉大な思想を構想する力、(2)強烈で熱情的な感情、(3)思想と言語の形象の技法、(4)高貴な語彙、(5)威厳ある言語配列。最初の二つは天賦の才、残り三つは技術の習得による。天性と技術の補完関係を強調。",
            "impact_summary": "18世紀崇高論の直接的起点。天才と技術の関係をめぐる議論の枠組みを提供。ロマン主義の天才論に影響。",
            "subfield": "古典詩学",
            "school_of_thought": "古代崇高論",
            "era_start": 100,
            "era_end": None,
            "keywords_ja": "崇高の源泉,偉大な思想,天性と技術,感情と技法",
            "keywords_en": "sources of sublimity,great thoughts,nature and art,passion and technique",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "技術的完成度と創造的偉大性を同一視する態度に対し、二種の卓越性の差異を照らし出す。",
            "reinterpretation_history": "ボワロー訳（1674年）で再発見。バークが恐怖と崇高の連関を分析。カントが理性の超越として再構成。",
            "cultural_context": "帝政ローマ初期、カエキリウス・カラクテの著作への応答。修辞学的技巧の過度な重視への批判。",
            "originator": "res_longinus",
            "year_proposed": 100,
            "founding_work": "プセウド・ロンギノス『崇高について（Peri Hypsous）』第8-9章"
        },
        # --- Rhetoric ---
        {
            "id": "cp_ethos_pathos_logos",
            "name_ja": "エートス・パトス・ロゴス",
            "name_en": "Ethos, Pathos, Logos (Three Modes of Persuasion)",
            "name_original": "ἦθος, πάθος, λόγος",
            "definition": "アリストテレスが『弁論術』で体系化した説得の三つの手段。エートスは話者の人格的信頼性による説得、パトスは聴衆の感情への訴えによる説得、ロゴスは論理的推論による説得。三者は相互補完的であり、効果的な弁論には三要素の均衡が必要。",
            "impact_summary": "修辞学・コミュニケーション論の永続的基盤。広告・政治演説・プレゼンテーション理論のすべてに適用される普遍的な説得の分析枠組み。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス修辞学",
            "era_start": -350,
            "era_end": None,
            "keywords_ja": "説得の三要素,エートス,パトス,ロゴス,弁論術",
            "keywords_en": "three modes of persuasion,ethos,pathos,logos,rhetoric",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "説得を論理（ロゴス）のみで完結させようとする合理主義的態度に対し、信頼性と感情の不可欠な役割を示す。",
            "reinterpretation_history": "キケロがローマ修辞学に統合。中世にトリヴィウム教育の基盤に。現代のコミュニケーション理論・マーケティングで普遍的に応用。",
            "cultural_context": "アテナイ民主制における法廷弁論と政治演説の実践。弁論が市民生活の中心的技能であった社会。",
            "originator": "res_aristotle",
            "year_proposed": -350,
            "founding_work": "アリストテレス『弁論術（Rhetorica）』第1巻第2章"
        },
        {
            "id": "cp_three_genres_rhetoric",
            "name_ja": "三種の弁論術",
            "name_en": "Three Genres of Rhetoric",
            "name_original": "τρία γένη τῆς ῥητορικῆς",
            "definition": "アリストテレスが分類した弁論の三つのジャンル。(1)法廷弁論（ディカニコン）: 過去の行為の正不正を論じる、(2)議会弁論（シュンブーレウティコン）: 未来の行動の利害を論じる、(3)演示的弁論（エピデイクティコン）: 現在の称賛・非難を行う。各ジャンルは異なる時間軸と聴衆を想定する。",
            "impact_summary": "弁論と修辞の場面分類の永続的枠組み。近代の法学的議論、政治的討論、式辞の理論的基盤。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス修辞学",
            "era_start": -350,
            "era_end": None,
            "keywords_ja": "三種の弁論,法廷弁論,議会弁論,演示的弁論",
            "keywords_en": "three genres of rhetoric,judicial,deliberative,epideictic",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "弁論を一枚岩的に扱う態度に対し、目的・時間軸・聴衆による構造的差異を明らかにする。",
            "reinterpretation_history": "キケロが発展・精緻化。中世の説教術に応用。現代の修辞学でペレルマンが再評価。",
            "cultural_context": "アテナイ民主制における法廷（ディカステリオン）、民会（エクレシア）、祭典（パネギュリス）という三つの制度的場。",
            "originator": "res_aristotle",
            "year_proposed": -350,
            "founding_work": "アリストテレス『弁論術（Rhetorica）』第1巻第3章"
        },
        {
            "id": "cp_five_canons",
            "name_ja": "弁論術の五部門",
            "name_en": "Five Canons of Rhetoric",
            "name_original": "quinque partes artis rhetoricae",
            "definition": "修辞学の五つの基本技能。(1)インヴェンティオ（発想・論拠の発見）、(2)ディスポジティオ（配列・構成）、(3)エロクティオ（表現・文体）、(4)メモリア（記憶）、(5)プロヌンティアティオ（発声・身振り）。キケロとヘレンニウス修辞学書で体系化され、クインティリアヌスが教育課程として確立。",
            "impact_summary": "西洋教育課程の基礎。中世のトリヴィウム、ルネサンスの人文主義教育、現代のスピーチ教育に至る修辞教育の構造的枠組み。",
            "subfield": "古典詩学",
            "school_of_thought": "ローマ修辞学",
            "era_start": -86,
            "era_end": None,
            "keywords_ja": "五部門,インヴェンティオ,ディスポジティオ,エロクティオ,メモリア",
            "keywords_en": "five canons,inventio,dispositio,elocutio,memoria,pronuntiatio",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "コミュニケーションを即興的な行為とみなす態度に対し、説得の体系的な準備過程を五段階で明示。",
            "reinterpretation_history": "中世に説教術の枠組みとして継承。ルネサンスの人文主義教育で復活。現代のプレゼンテーション理論に応用。",
            "cultural_context": "ローマ共和制における法廷弁論と政治演説の実践的必要性。弁論術が市民教育の中核であった社会。",
            "originator": "res_cicero",
            "year_proposed": -86,
            "founding_work": "『ヘレンニウスへの修辞学（Rhetorica ad Herennium）』、キケロ『弁論家について（De Oratore）』"
        },
        {
            "id": "cp_tropos_schema",
            "name_ja": "トロポスとスケーマ（転義と修辞的形象）",
            "name_en": "Tropes and Schemes (Figures of Speech)",
            "name_original": "tropus et schema / τρόπος καὶ σχῆμα",
            "definition": "クインティリアヌスが『弁論家の教育』で精緻に分類した修辞技法の二大区分。トロポス（転義）は語義の転換（メタファー、メトニミー、シネクドキ等）、スケーマ（修辞的形象）は語句の配列・構文の変形（対句、反復、省略等）。両者の区別と体系的分類は後世の修辞学教育の基盤。",
            "impact_summary": "文学批評と修辞学の分析語彙の基礎。ド・マン、ジュネット等のポスト構造主義批評における修辞分析の前提。",
            "subfield": "古典詩学",
            "school_of_thought": "ローマ修辞学",
            "era_start": 95,
            "era_end": None,
            "keywords_ja": "トロポス,スケーマ,修辞技法,転義,文彩",
            "keywords_en": "tropes,schemes,figures of speech,rhetorical devices",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "言語表現を内容と形式に二分する単純化に対し、形式が意味を生成するメカニズムの精緻な分析を提供。",
            "reinterpretation_history": "中世修辞学で継承。ロマン主義が「自然な表現」を対置。ド・マンが修辞分析を脱構築批評の方法論に。ジュネットがナラトロジーに応用。",
            "cultural_context": "ローマ帝国期の修辞学教育制度。弁論家養成のための体系的教科書としての需要。",
            "originator": "res_quintilian",
            "year_proposed": 95,
            "founding_work": "クインティリアヌス『弁論家の教育（Institutio Oratoria）』第8-9巻"
        },
        {
            "id": "cp_three_styles",
            "name_ja": "三文体論",
            "name_en": "Three Styles (Genera Dicendi)",
            "name_original": "tria genera dicendi",
            "definition": "キケロが体系化した文体の三段階。(1)高文体（grandis/gravis）: 感情を動かす壮大な表現、(2)中文体（medius/moderatus）: 快い優雅な表現、(3)低文体（tenuis/subtilis）: 明瞭で簡潔な表現。各文体は弁論の目的（感動させる・楽しませる・教える）に対応する。デコールム原理と結合して、場面に適した文体選択の規範を形成。",
            "impact_summary": "中世の「ウェルギリウスの車輪」、ルネサンスの文体論、近代の文体論すべての出発点。レジスター（言語使用域）の理論的基盤。",
            "subfield": "古典詩学",
            "school_of_thought": "ローマ修辞学",
            "era_start": -46,
            "era_end": None,
            "keywords_ja": "三文体,高文体,中文体,低文体,文体選択",
            "keywords_en": "three styles,grand style,middle style,plain style,genera dicendi",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "文体を作者の個性の自然な発露とみなす態度に対し、目的と場面に応じた意識的な文体選択の技術を示す。",
            "reinterpretation_history": "中世「ウェルギリウスの車輪（rota Vergilii）」で図式化。ダンテ『俗語論』で検討。近代社会言語学のレジスター概念に発展。",
            "cultural_context": "ローマ社会の階層構造と弁論の場の多様性。法廷・元老院・市民集会それぞれに求められる異なる文体。",
            "originator": "res_cicero",
            "year_proposed": -46,
            "founding_work": "キケロ『弁論家（Orator）』第20-32章"
        },
        {
            "id": "cp_enthymeme",
            "name_ja": "エンテュメーマ（修辞的推論）",
            "name_en": "Enthymeme (Rhetorical Syllogism)",
            "name_original": "ἐνθύμημα (enthymēma)",
            "definition": "アリストテレスが弁論術の中核に位置づけた修辞的推論形式。論理学の三段論法に対応するが、厳密な論証ではなく蓋然的推論。前提の一つが省略されるのが特徴で、聴衆が暗黙の前提を自ら補完することで説得力が増す。弁論術における「証明の核心」とされた。",
            "impact_summary": "修辞的論証の理論。広告・政治演説・日常的議論における暗黙の前提の機能を分析する枠組み。トゥールミンの議論モデルの前身。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス修辞学",
            "era_start": -350,
            "era_end": None,
            "keywords_ja": "エンテュメーマ,修辞的推論,省略三段論法,蓋然的推論",
            "keywords_en": "enthymeme,rhetorical syllogism,probable reasoning,truncated syllogism",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "説得を厳密な論理的証明に限定する態度に対し、日常的推論における省略と暗黙の前提の効果を示す。",
            "reinterpretation_history": "中世スコラ学で形式論理学に統合。トゥールミンが議論モデルとして再構成（1958年）。現代の非形式論理学で再評価。",
            "cultural_context": "アテナイの法廷弁論における実践的需要。市民裁判員への説得に厳密な論証が不適切であった状況。",
            "originator": "res_aristotle",
            "year_proposed": -350,
            "founding_work": "アリストテレス『弁論術（Rhetorica）』第1巻第2章、第2巻第22-26章"
        },
        {
            "id": "cp_vir_bonus",
            "name_ja": "完全な弁論家（vir bonus dicendi peritus）",
            "name_en": "The Good Man Speaking Well",
            "name_original": "vir bonus dicendi peritus",
            "definition": "クインティリアヌスが定義した理想の弁論家像。「善き人にして弁論に熟達した者」。修辞学的技能と倫理的卓越性の不可分な統合を主張。弁論家は単に技術的に優れるだけでなく、道徳的に善い人物でなければならない。カトの定義を継承・発展させ、修辞教育を全人格の陶冶として位置づけた。",
            "impact_summary": "人文主義教育の理念的基盤。リベラルアーツ教育の根本理念。知識と徳の統合という教育哲学の原型。",
            "subfield": "古典詩学",
            "school_of_thought": "ローマ修辞学・教育哲学",
            "era_start": 95,
            "era_end": None,
            "keywords_ja": "善き弁論家,倫理と技術,全人教育,人文主義",
            "keywords_en": "vir bonus,good man speaking well,ethical rhetoric,humanism",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "技術的能力と倫理的品性を分離する態度に対し、真の卓越性は両者の統合にのみ存在することを主張。",
            "reinterpretation_history": "ルネサンスの人文主義教育で中心理念に。エラスムスが教養人の理想として継承。現代のリベラルアーツ教育理念に影響。",
            "cultural_context": "ローマ帝国期の修辞学校教育。弁論家養成が社会的エリート教育の中核であった時代。帝政下の言論制限と弁論家の倫理的責任。",
            "originator": "res_quintilian",
            "year_proposed": 95,
            "founding_work": "クインティリアヌス『弁論家の教育（Institutio Oratoria）』第12巻第1章"
        },
        {
            "id": "cp_ars_memoriae",
            "name_ja": "記憶術（ars memoriae）",
            "name_en": "Art of Memory (Ars Memoriae)",
            "name_original": "ars memoriae / τέχνη μνημονική",
            "definition": "シモニデスに帰される古代の記憶技法。場所法（method of loci）: 記憶すべき事項を想像上の建築空間の各場所に配置し、心の中でその空間を歩くことで想起する。キケロが『弁論家について』で紹介し、クインティリアヌスが詳細に記述。弁論術の五部門の一つ（メモリア）として制度化された。",
            "impact_summary": "中世・ルネサンスの記憶宮殿の伝統。現代の記憶術・認知科学における空間記憶と言語記憶の関係研究の起源。フランシス・イェイツの歴史的研究で再評価。",
            "subfield": "古典詩学",
            "school_of_thought": "古代修辞学・認知技法",
            "era_start": -500,
            "era_end": None,
            "keywords_ja": "記憶術,場所法,記憶宮殿,視覚的記憶,弁論準備",
            "keywords_en": "art of memory,method of loci,memory palace,visual memory",
            "status": "active",
            "source_reliability": "primary",
            "blind_spot_addressed": "記憶を受動的な蓄積と見る態度に対し、空間的・視覚的配置による能動的な記憶構成の技法を示す。",
            "reinterpretation_history": "中世で宗教的瞑想と結合。ルネサンスでブルーノらが宇宙的記憶術に発展。イェイツ『記憶術』（1966年）で学術的に復権。現代の認知心理学で空間認知と記憶の関係として研究。",
            "cultural_context": "口承文化から文字文化への移行期。書物が希少で、弁論家が長大な演説を暗記する必要があった社会。",
            "originator": "res_cicero",
            "year_proposed": -55,
            "founding_work": "キケロ『弁論家について（De Oratore）』第2巻第86章、クインティリアヌス『弁論家の教育』第11巻"
        },
        {
            "id": "cp_spoudaios",
            "name_ja": "スプーダイオスとパウロス（優れた人物と劣った人物）",
            "name_en": "Spoudaios and Phaulos (Noble and Base Characters)",
            "name_original": "σπουδαῖος καὶ φαῦλος",
            "definition": "アリストテレスが詩の模倣対象を区分するために用いた概念対。悲劇は「我々よりも優れた人物（スプーダイオス）」を模倣し、喜劇は「我々よりも劣った人物（パウロス）」を模倣する。これは道徳的優劣というよりも、社会的地位と行為の重大さの区分であり、ジャンル分類の基礎的基準。",
            "impact_summary": "文学ジャンルの階層論の起源。高貴なジャンルvs低俗なジャンルという区分がルネサンス・新古典主義まで支配的な評価基準に。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "人物の優劣,悲劇と喜劇,ジャンル階層,模倣対象",
            "keywords_en": "noble and base characters,tragedy and comedy,genre hierarchy",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "文学の民主化・大衆化を自明視する態度に対し、模倣対象の社会的地位がジャンルを規定するという構造を示す。",
            "reinterpretation_history": "中世で身分制と結合。ルネサンスで厳格なジャンル規範に。アウエルバッハが『ミメーシス』で文体混合の歴史を追跡。現代では解体済み。",
            "cultural_context": "古代ギリシャの社会的階層構造と演劇祭における悲劇と喜劇の制度的区分。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第2章"
        },
        {
            "id": "cp_epic_tragedy",
            "name_ja": "叙事詩と悲劇の比較",
            "name_en": "Epic vs. Tragedy Comparison",
            "name_original": "ἔπος καὶ τραγῳδία",
            "definition": "アリストテレスが『詩学』最終部で展開した二大ジャンルの比較論。両者はともに優れた人物の模倣だが、悲劇は演技による直接的表現で時間的制約があり、叙事詩は語りによる間接的表現で長大な展開が可能。アリストテレスは悲劇を叙事詩より優れたジャンルと結論づけ、より凝縮された形式でカタルシスを達成できるとした。",
            "impact_summary": "ジャンル間の優劣論争の原型。小説が台頭するまで叙事詩vs悲劇の比較が文学理論の中心的課題であった。",
            "subfield": "古典詩学",
            "school_of_thought": "アリストテレス詩学",
            "era_start": -335,
            "era_end": None,
            "keywords_ja": "叙事詩,悲劇,ジャンル比較,長さと凝縮,語りと演技",
            "keywords_en": "epic,tragedy,genre comparison,narrative vs performance",
            "status": "reinterpreted",
            "source_reliability": "primary",
            "blind_spot_addressed": "すべてのジャンルを等価とみなすフラットな態度に対し、形式的凝縮度と感情的効果の関係を問う。",
            "reinterpretation_history": "ルネサンスで叙事詩vs悲劇論争が活発化。近代の小説の台頭で議論の文脈が変化。バフチンが小説を「最も若いジャンル」として位置づけ。",
            "cultural_context": "ホメロスの叙事詩と三大悲劇詩人の作品が並行して享受された古代ギリシャの文化的環境。",
            "originator": "res_aristotle",
            "year_proposed": -335,
            "founding_work": "アリストテレス『詩学（Peri Poiētikēs）』第23-26章"
        }
    ]

    inserted = 0
    for c in concepts:
        originator = c.pop("originator")
        year_proposed = c.pop("year_proposed")
        founding_work = c.pop("founding_work")

        try:
            conn.execute("""
                INSERT OR IGNORE INTO humanities_concept
                (id, name_ja, name_en, name_original, definition, impact_summary, subfield,
                 school_of_thought, era_start, era_end, keywords_ja, keywords_en, status,
                 source_reliability, data_completeness, blind_spot_addressed,
                 reinterpretation_history, cultural_context, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (c["id"], c["name_ja"], c["name_en"], c["name_original"], c["definition"],
                  c["impact_summary"], c["subfield"], c["school_of_thought"], c["era_start"],
                  c.get("era_end"), c["keywords_ja"], c["keywords_en"], c["status"],
                  c["source_reliability"], 85, c["blind_spot_addressed"],
                  c["reinterpretation_history"], c["cultural_context"], now, now))
            inserted += 1

            # Link concept to researcher
            if originator:
                conn.execute("""
                    INSERT OR IGNORE INTO humanities_concept_researchers
                    (concept_id, researcher_id, role, year_associated, note)
                    VALUES (?, ?, 'originator', ?, ?)
                """, (c["id"], originator, year_proposed, founding_work))
        except Exception as e:
            print(f"  Error inserting {c['name_ja']}: {e}")

    print(f"Inserted {inserted} concepts")

    # ========== RELATIONS ==========
    relations = [
        # Plato -> Aristotle critical inheritance
        ("cp_mimesis_critique", "cp_mimesis", "critiques", "プラトンのミメーシス批判に対するアリストテレスの肯定的再定義。模倣を虚妄ではなく知的営為として再解釈。"),
        ("cp_mimesis", "cp_mimesis_critique", "reinterprets", "アリストテレスがプラトンのミメーシス批判を反転させ、模倣に認識論的価値を付与。"),
        ("cp_poet_banishment", "cp_prodesse_delectare", "opposes", "プラトンの詩人追放論にホラティウスの「教えと楽しみ」が間接的に応答。詩の社会的有用性を肯定。"),
        ("cp_divine_inspiration", "cp_catharsis", "opposes", "プラトンの非理性的霊感説に対し、アリストテレスは感情の理性的浄化としてのカタルシスを対置。"),

        # Aristotle internal structure
        ("cp_mythos", "cp_peripeteia", "enables", "ミュトス（筋立て）の構造が逆転（ペリペテイア）を因果的に生成する前提条件。"),
        ("cp_mythos", "cp_anagnorisis", "enables", "筋立ての因果的展開が認知（アナグノリシス）の瞬間を必然的にもたらす。"),
        ("cp_peripeteia", "cp_anagnorisis", "synthesizes", "最も優れた悲劇では逆転と認知が同時に生じ、最大の劇的効果を達成する。"),
        ("cp_hamartia", "cp_peripeteia", "enables", "主人公の過ち（ハマルティア）が逆転の因果的原因となる。"),
        ("cp_six_elements", "cp_mythos", "enables", "六要素体系の中でミュトスが最上位に位置づけられ、他の要素を統括する。"),
        ("cp_probability_necessity", "cp_mythos", "enables", "蓋然性と必然性の原理がミュトスの因果的構成を規定する基本法則。"),
        ("cp_tragedy_def", "cp_catharsis", "enables", "悲劇の定義がカタルシスを悲劇の目的として組み込み、概念的に前提する。"),
        ("cp_tragedy_def", "cp_six_elements", "enables", "悲劇の定義が六要素の分析的展開の出発点となる。"),
        ("cp_mimesis", "cp_tragedy_def", "enables", "ミメーシス概念が悲劇を「行為の模倣」と定義する基盤。"),
        ("cp_mimesis", "cp_genre_theory", "enables", "模倣の三基準（手段・対象・様式）がジャンル分類体系を基礎づける。"),
        ("cp_probability_necessity", "cp_poetry_vs_history", "enables", "蓋然性の原理が詩と歴史の区別を可能にする認識論的基盤。"),
        ("cp_genre_theory", "cp_spoudaios", "enables", "ジャンル分類がスプーダイオス/パウロスの区分に依拠する。"),
        ("cp_genre_theory", "cp_epic_tragedy", "enables", "ジャンル論が叙事詩と悲劇の比較の前提条件。"),
        ("cp_metaphor", "cp_tropos_schema", "derived_from", "アリストテレスのメタファー理論がクインティリアヌスのトロポス体系の基礎概念。"),

        # Aristotle rhetoric -> poetics
        ("cp_ethos_pathos_logos", "cp_six_elements", "enables", "弁論術の三要素が悲劇の六要素（性格=エートス、思想=ロゴス的、感情喚起=パトス的）に対応。"),
        ("cp_enthymeme", "cp_probability_necessity", "derived_from", "蓋然的推論としてのエンテュメーマが蓋然性の原理を共有する修辞学的形式。"),

        # Aristotle -> Horace
        ("cp_catharsis", "cp_prodesse_delectare", "reinterprets", "ホラティウスがアリストテレスのカタルシスを「教えと楽しみ」の二重目的として実用的に再解釈。"),
        ("cp_mimesis", "cp_ut_pictura_poesis", "extends", "ミメーシスの原理を視覚芸術との類比に拡張し、詩の視覚的表象性を強調。"),
        ("cp_genre_theory", "cp_decorum", "extends", "ジャンルの区分がデコールム原理と結合し、各ジャンルにふさわしい文体の規範に発展。"),

        # Cicero / Quintilian
        ("cp_ethos_pathos_logos", "cp_five_canons", "extends", "アリストテレスの三要素がローマ修辞学の五部門体系に統合・制度化される。"),
        ("cp_five_canons", "cp_ars_memoriae", "enables", "五部門の一つ（メモリア）として記憶術が修辞教育に制度化される。"),
        ("cp_three_styles", "cp_decorum", "enables", "三文体論がデコールム原理の具体的実現手段として機能。"),
        ("cp_five_canons", "cp_tropos_schema", "enables", "五部門のエロクティオ（表現）の中核としてトロポスとスケーマが位置づけられる。"),
        ("cp_five_canons", "cp_vir_bonus", "synthesizes", "技術的五部門と倫理的善の統合として完全な弁論家の理念が構築される。"),

        # Longinus
        ("cp_mimesis", "cp_hypsos", "extends", "ミメーシスの原理を超えて、模倣を超越する精神の高揚としての崇高を理論化。"),
        ("cp_catharsis", "cp_hypsos", "extends", "感情の浄化を超えて、精神の圧倒的高揚という別次元の美的経験を提唱。"),
        ("cp_five_sources", "cp_hypsos", "enables", "五源泉の分析が崇高の概念を体系化する枠組み。"),
        ("cp_ethos_pathos_logos", "cp_five_sources", "reinterprets", "説得の三要素を崇高の生成条件として再解釈。偉大な思想=ロゴス、強烈な感情=パトスの変容。"),

        # Cross-era influence markers
        ("cp_decorum", "cp_three_styles", "synthesizes", "ホラティウスのデコールムとキケロの三文体論が統合され、場面適応的文体選択の規範体系に。"),
    ]

    rel_count = 0
    for source, target, rel_type, desc in relations:
        try:
            conn.execute("""
                INSERT OR IGNORE INTO humanities_concept_relations
                (id, source_concept_id, target_concept_id, relation_type, relation_description, strength, is_confirmed, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (gen_id(), source, target, rel_type, desc, 8, 1, now))
            rel_count += 1
        except Exception as e:
            print(f"  Relation error {source}->{target}: {e}")

    print(f"Inserted {rel_count} relations")

    conn.commit()

    # Verification
    total = conn.execute("SELECT COUNT(*) FROM humanities_concept WHERE subfield='古典詩学'").fetchone()[0]
    total_res = conn.execute("SELECT COUNT(*) FROM researchers WHERE id LIKE 'res_%'").fetchone()[0]
    total_rel = conn.execute("""
        SELECT COUNT(*) FROM humanities_concept_relations
        WHERE source_concept_id LIKE 'cp_%' OR target_concept_id LIKE 'cp_%'
    """).fetchone()[0]

    print(f"\n=== Verification ===")
    print(f"Classical poetics concepts: {total}")
    print(f"New researchers: {total_res}")
    print(f"Classical poetics relations: {total_rel}")
    print(f"Total humanities_concept: {conn.execute('SELECT COUNT(*) FROM humanities_concept').fetchone()[0]}")

    conn.close()

if __name__ == "__main__":
    main()
