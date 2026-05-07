"""
LIT-DB Phase 2 — C37 Wave 7: Critical Theory
================================================================
Gender / Postcolonial / Ecocriticism (30 concepts).

Inserts 30 canonical concepts spanning 3 categories:
  A. Gender / feminist criticism (10)
  B. Postcolonial criticism (10)
  C. Ecocriticism / environmental humanities (10)

All entries are sourced via authoritative critical-theory sources:
  - Stanford Encyclopedia of Philosophy (SEP)
  - JSTOR canonical articles
  - Project MUSE
  - Critical Inquiry / PMLA / boundary 2 archives
  - Author's own canonical book chapters (Said, Spivak, Butler etc.)

source_tier='primary' — author's own canonical text directly cited.
source_tier='secondary' — SEP / authoritative encyclopedia / canonical
  scholarly synthesis.
source_tier='tertiary' — synthetic / movement-level concept names whose
  attestation rests on multiple secondary expositions.

Pattern: P3 (Theory-driven Concept Cartography).
"""
from __future__ import annotations

import sys

from lit_db_helper import LitDB, LitDBError


# ---------------------------------------------------------------
# Period seeding (theory-region anchored to 20th-21st century waves)
# ---------------------------------------------------------------

PERIODS_TO_SEED = [
    # name_ja, name_en, start, end, description
    ("第一・第二波フェミニズム期", "First/Second-Wave Feminism", 1900, 1979,
     "ウルフから60-70年代の第二波フェミニズム理論が確立する時期。"),
    ("ポスト構造主義以後の批評期", "Post-Structuralist Critical Theory", 1980, 1999,
     "シクスー・イリガライ・クリステヴァ・サイード・スピヴァク・バーバ・バトラーらが理論的中核を確立した時期。"),
    ("環境・脱植民地・ポストヒューマン期", "Environmental & Decolonial Theory",
     2000, 2025,
     "エコクリティシズム・ポストヒューマニズム・人新世文学・気候フィクションが理論前線を占める時期。"),
]


# ---------------------------------------------------------------
# Concept payload
# ---------------------------------------------------------------

CONCEPTS: list[dict] = []


def add(entry: dict) -> None:
    CONCEPTS.append(entry)


# ===============================================================
# CATEGORY A — Gender / feminist criticism (10)
# ===============================================================

add({
    "name_ja": "自分ひとりの部屋",
    "name_en": "A Room of One's Own",
    "name_original": "A Room of One's Own",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "第一・第二波フェミニズム期",
    "definition": "ヴァージニア・ウルフが1929年の同名エッセイで提示した命題。女性が小説を書くためには「金と自分ひとりの部屋」が必要だと論じ、文学創造を支える物質的条件と歴史的に女性に拒まれてきた知的空間の問題をフェミニズム文学批評の出発点に据えた。",
    "background": "1928年ケンブリッジでの講義に基づく。ガートン・ニューナム両女子学寮での講演をもとにする。",
    "development": "シクスー、ショウォルター、ギルバート＆グーバーらの第二波フェミニズム批評が直接の継承者。",
    "historical_context": "戦間期の女性参政権獲得直後、女性高等教育の制度的限界が依然として残る時期。",
    "primary_source_url": "https://gutenberg.net.au/ebooks02/0200791.txt",
    "primary_source_type": "Project Gutenberg Australia — Woolf full text",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "作者性", "status": "rethinking",
         "rationale": "「誰が書く資格を持つか」という問いはAI生成時代に「誰が／何が著者となりうるか」へと拡張され、ウルフの問題提起が新たな射程で再活性化される。",
         "related_ai_phenomenon": "AI著者性論争・ジェンダー化された訓練データ問題"},
    ],
})

add({
    "name_ja": "女性的エクリチュール",
    "name_en": "écriture féminine",
    "name_original": "écriture féminine",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "エレーヌ・シクスーが1975年の論文「メデューサの笑い」で提起した概念。女性身体に根ざした書記実践として、ファロセントリックな男性的言語秩序に亀裂を入れる「他なる」エクリチュールを構想する。本質主義との緊張を抱えつつ、身体・無意識・声の文学的記入を主題化する。",
    "background": "ラカン派精神分析とデリダ脱構築の交差点で形成。1968年五月革命後のフランス女性運動と並行する。",
    "development": "イリガライ「女性的話法」、クリステヴァ「セミオティック」と並び「フランス・フェミニズム」三本柱を構成。",
    "historical_context": "70年代パリの精神分析・差異の女性運動MLF。",
    "primary_source_url": "https://www.jstor.org/stable/3173239",
    "primary_source_type": "JSTOR — Cixous 'The Laugh of the Medusa' (Signs 1976)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「身体に根ざす言語」というシクスーの構想は、AIの脱身体的言語生成に対する批判軸として再浮上している。",
         "related_ai_phenomenon": "脱身体的LLM生成と身体性の問題"},
        {"axis": "主体", "status": "rethinking",
         "rationale": "ファロセントリックな主体に代わる「女性的主体」の構想は、AI主体性論議における人間中心主義批判と接続する。",
         "related_ai_phenomenon": "AI主体性論争"},
    ],
})

add({
    "name_ja": "女性的話法",
    "name_en": "parler-femme",
    "name_original": "parler-femme",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "リュス・イリガライが『一つではない女の性』（1977）で提起した概念。男性中心の象徴秩序のなかで「ひとつの性」しか存在しないとされてきた構造を批判し、女性的差異から発する話法・複数性の言語実践を構想する。鏡像論理ではなく流動・接触の論理を重視する。",
    "background": "ラカン精神分析からの離脱（パリ精神分析学校除籍）が直接の文脈。",
    "development": "差異派フェミニズムの中核となり、現代の差異の倫理（ヌスバウム、ブライドッティ）に継承される。",
    "historical_context": "70年代フランス精神分析運動内部の理論闘争。",
    "primary_source_url": "https://plato.stanford.edu/entries/luce-irigaray/",
    "primary_source_type": "SEP — Luce Irigaray entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「単一の象徴秩序」に対する複数性の話法は、LLMが訓練データで強化する標準言語規範への批判として再活性化する。",
         "related_ai_phenomenon": "LLMの言語規範強化バイアス"},
    ],
})

add({
    "name_ja": "アブジェクシオン（おぞましきもの）",
    "name_en": "abjection",
    "name_original": "abjection",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ジュリア・クリステヴァが『恐怖の権力』（1980）で提示した概念。主体形成の手前で排除されながら、排除しきれずに主体の境界を脅かし続ける「おぞましきもの」を指す。死体・体液・母体的なものなど、自己と他者の分離以前の領域を文学的に分析する装置となる。",
    "background": "ラカン精神分析の鏡像段階論への補足として、前-象徴的領域を理論化する企図。",
    "development": "ホラー文学批評（バーバラ・クリード）、フェミニズム身体論、現代の感染症文学批評まで展開。",
    "historical_context": "70-80年代パリの精神分析理論と文芸批評の交差。",
    "primary_source_url": "https://www.jstor.org/stable/jj.13133873",
    "primary_source_type": "JSTOR — Kristeva Powers of Horror (Columbia UP)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "主体の境界を脅かす「おぞましきもの」は、AI出力におけるアンキャニーバレー・幻覚現象との構造的類比を生む。",
         "related_ai_phenomenon": "AIの幻覚出力・アンキャニーバレー現象"},
    ],
})

add({
    "name_ja": "ガイノクリティシズム",
    "name_en": "gynocriticism",
    "name_original": "gynocriticism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "イレイン・ショウォルターが1979年の論文「フェミニスト詩学に向けて」で提唱した概念。男性正典への批判的読解にとどまらず、女性作家自身の伝統・主題・形式・キャリア構造を独自の対象として研究する批評枠組みを指す。フェミニズム批評の対象を女性作家文化に転換した。",
    "background": "70年代英米フェミニズム批評内部での「批判」から「構築」への転換。",
    "development": "ギルバート＆グーバー、トリル・モイ、現代の女性正典再構築運動の理論的基盤となる。",
    "historical_context": "アメリカ大学院での女性研究プログラム制度化期。",
    "primary_source_url": "https://www.jstor.org/stable/3177999",
    "primary_source_type": "JSTOR — Showalter 'Toward a Feminist Poetics'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "正典", "status": "rethinking",
         "rationale": "「女性独自の文学伝統」の再構築という方法は、AI訓練データの正典バイアス監査と直接連動する。",
         "related_ai_phenomenon": "AI訓練データのジェンダー正典バイアス"},
    ],
})

add({
    "name_ja": "屋根裏の狂女",
    "name_en": "The Madwoman in the Attic",
    "name_original": "The Madwoman in the Attic",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "サンドラ・ギルバートとスーザン・グーバーの共著（1979）が提示した枠組み。19世紀英米女性作家が、男性的正典の言語のなかで自己を表現する際に、しばしば狂女・分身・幽閉される女性像を「分身としての著者」として配置していたことを明らかにし、女性文学伝統の隠れた構造を可視化した。",
    "background": "ヴィクトリア朝小説（ブロンテ・ディキンソン等）の精読を通じた帰納的理論化。",
    "development": "後期サイード、ジーン・リース『サルガッソーの広い海』批評、ポストコロニアル・フェミニズム接合の出発点。",
    "historical_context": "70年代後半の英米フェミニズム批評の成熟期。",
    "primary_source_url": "https://yalebooks.yale.edu/book/9780300084580/the-madwoman-in-the-attic/",
    "primary_source_type": "Yale UP — Gilbert & Gubar canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "パフォーマティヴィティ",
    "name_en": "performativity",
    "name_original": "performativity",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ジュディス・バトラーが『ジェンダー・トラブル』（1990）で展開した中核概念。ジェンダーは内的本質ではなく、規範化された行為の反復によって遡及的に「実体」として構築されると論じる。J.L.オースティンの言語行為論を参照しつつ、ジェンダーの政治的攪乱可能性を理論化した。",
    "background": "フーコーの規律権力論、デリダの反復可能性論、ラカン派精神分析の交差点で形成。",
    "development": "クィア理論、トランスジェンダー理論、現代のアイデンティティ政治論の中核理論。",
    "historical_context": "80-90年代米国の文化戦争・クィア活動運動の高揚期。",
    "primary_source_url": "https://plato.stanford.edu/entries/feminism-gender/",
    "primary_source_type": "SEP — Feminist Perspectives on Sex and Gender",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「行為の反復による主体構築」というバトラーのモデルは、LLMが訓練データの統計的反復から「主体」効果を生み出す現象と構造的に類比される。",
         "related_ai_phenomenon": "AI主体性論争・LLMにおけるペルソナ効果"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "パフォーマティヴィティ",
         "description": "バトラーの理論は哲学DBにおける言語行為論・主体形成論と直接共有される。"},
    ],
})

add({
    "name_ja": "クィア理論（文学批評）",
    "name_en": "queer theory in literature",
    "name_original": "queer theory",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "1990年代初頭にイヴ・コソフスキー・セジウィック『クローゼットの認識論』、テレサ・デ・ラウレティス造語の流通を通じて確立した批評領域。性的アイデンティティの自然化を脱構築し、文学テクストにおけるホモソーシャル・クローゼット・カミングアウトの構造を分析する。",
    "background": "エイズ危機下の活動と学術的脱構築理論の合流。",
    "development": "リー・エデルマン『ノー・フューチャー』、ホセ・エステバン・ムニョス『クルージング・ユートピア』など反規範的時間論へ展開。",
    "historical_context": "90年代米国エイズ活動運動とアカデミックな脱構築理論の合流期。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctv11smk6r",
    "primary_source_type": "JSTOR — Sedgwick Epistemology of the Closet",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ポストフェミニズム",
    "name_en": "postfeminism",
    "name_original": "postfeminism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "1990年代以降に台頭した文化的傾向と、その批評的分析枠組み。フェミニズムの目的は達成されたとする想定のもとで、女性個人の「選択」「エンパワーメント」を消費文化が回収する状況を、アンジェラ・マクロビーらが批判的に理論化した。",
    "background": "新自由主義の市場化と第二波フェミニズム批判言説の交差。",
    "development": "ロザリンド・ギル『ポストフェミニスト感性』論、現代の#MeToo以後のフェミニズム再活性化までの理論的準備段階。",
    "historical_context": "90-2000年代のグローバル消費文化と新自由主義主体形成。",
    "primary_source_url": "https://www.jstor.org/stable/40338719",
    "primary_source_type": "JSTOR — McRobbie 'Post-Feminism and Popular Culture'",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "インターセクショナリティ",
    "name_en": "intersectionality",
    "name_original": "intersectionality",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "キンバリー・クレンショーが1989年の論文で提起した分析概念。人種・ジェンダー・階級などの抑圧軸が独立に作用するのではなく、交差点（intersection）において固有の経験を生成すると論じる。文学批評では黒人女性作家研究、第三世界フェミニズム批評の方法論的基盤となった。",
    "background": "米国の反差別法において黒人女性の経験が制度的に不可視化された問題から出発。",
    "development": "パトリシア・ヒル・コリンズの構造的不平等論、現代の批評的人種理論（CRT）の方法論的基盤。",
    "historical_context": "80-90年代米国の批判的人種理論運動。",
    "primary_source_url": "https://chicagounbound.uchicago.edu/uclf/vol1989/iss1/8/",
    "primary_source_type": "U. Chicago Legal Forum — Crenshaw 1989 OA archive",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "単一カテゴリ的主体性への批判は、AIシステムにおける単一属性ベースの公平性指標の限界批判と直結する。",
         "related_ai_phenomenon": "AIフェアネスの交差性問題"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "インターセクショナリティ",
         "description": "クレンショーの法理論的概念は哲学DBの社会哲学領域と直接共有される。"},
    ],
})


# ===============================================================
# CATEGORY B — Postcolonial criticism (10)
# ===============================================================

add({
    "name_ja": "オリエンタリズム",
    "name_en": "Orientalism",
    "name_original": "Orientalism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "エドワード・サイードが1978年の同名著作で展開した枠組み。西洋が「東洋（オリエント）」を本質的他者として表象する言説体系を、フーコーの言説権力論を応用して批判的に分析した。文学・歴史記述・学術言説を貫く認識論的暴力を主題化し、ポストコロニアル批評の出発点となった。",
    "background": "サイード自身のパレスチナ系米国人としての位置と、フーコー言説分析の応用。",
    "development": "バーバ、スピヴァク、ヤング、現代の脱植民地知識論まで継続的に応答される。サイード自身は『文化と帝国主義』（1993）で対位法的読解へ深化させた。",
    "historical_context": "70年代後半の冷戦末期における第三世界研究の理論的成熟期。",
    "primary_source_url": "https://www.jstor.org/stable/3343989",
    "primary_source_type": "JSTOR — Said canonical reception",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「他者表象の言説権力」という枠組みは、AI訓練データに刻まれたオリエンタリスト的表象の永続化問題として再活性化する。",
         "related_ai_phenomenon": "LLM訓練データの地域・人種バイアス"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "オリエンタリズム",
         "description": "サイードのフーコー応用は哲学DBの言説権力論と直接共有される。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "他者の表象",
         "description": "人類学DBの民族誌的他者表象論と接続する。"},
    ],
})

add({
    "name_ja": "ミミクリ／ハイブリディティ／第三空間",
    "name_en": "mimicry / hybridity / third space",
    "name_original": "mimicry / hybridity / third space",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ホミ・バーバが『文化の場所』（1994）で展開した三概念。植民地状況において被植民者は支配者を完全には模倣せず「ほとんど同じだが完全には同じでない（almost the same but not quite）」というずれを生み、両者の境界に「第三空間」が開かれ、ハイブリッドな新たな主体性が生成すると論じる。",
    "background": "ファノン精神分析、ラカン、デリダ脱構築の交差点での理論化。",
    "development": "ディアスポラ研究、トランスナショナル文学研究、現代の創造的ハイブリッド文化論まで展開。",
    "historical_context": "80-90年代英米アカデミーにおけるポストコロニアル批評の制度化期。",
    "primary_source_url": "https://www.jstor.org/stable/jj.7361341",
    "primary_source_type": "JSTOR — Bhabha 'The Location of Culture'",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「ほとんど同じだが完全には同じでない」模倣の構造は、AIが人間言語を模倣しつつ生む差異・幻覚との構造的類比を生む。",
         "related_ai_phenomenon": "AIの言語模倣と「人間ではない差異」"},
        {"axis": "翻訳", "status": "rethinking",
         "rationale": "第三空間における翻訳的主体性の生成は、AI翻訳が生む文化的ハイブリッド表現の理論的基盤となる。",
         "related_ai_phenomenon": "AI翻訳における文化的ハイブリッド化"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ハイブリディティ",
         "description": "バーバの理論は哲学DBにおけるアイデンティティ哲学と共有される。"},
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ハイブリディティ",
         "description": "人類学DBの文化接触論と直結する。"},
    ],
})

add({
    "name_ja": "サバルタン",
    "name_en": "subaltern",
    "name_original": "subaltern",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ガヤトリ・C・スピヴァクが1988年の論文「サバルタンは語ることができるか」で提起したカテゴリー。グラムシの「下層民」概念を継承しつつ、植民地社会・第三世界の被抑圧者、特にジェンダー化された下位主体が、支配的言説体系のなかでは構造的に「語る」位置を持ちえないことを論じた。",
    "background": "サバルタン研究学派（ラナジット・グハら）への批判的応答として展開。",
    "development": "現代の知識生産批判、脱植民地メソドロジー、AIの「声なき者」表象問題まで参照され続ける。",
    "historical_context": "80年代後半の南アジア研究と脱構築批評の合流。",
    "primary_source_url": "https://jan.ucc.nau.edu/~sj6/Spivak%20CanTheSubalternSpeak.pdf",
    "primary_source_type": "Spivak canonical essay (cited from open archive)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「構造的に語りえない者」の問題は、AI訓練データから排除された言語・声の構造的不可視化問題として再活性化する。",
         "related_ai_phenomenon": "LLM訓練データに含まれない少数言語・周縁声"},
        {"axis": "真正性", "status": "rethinking",
         "rationale": "「他者の声を代弁する」西洋知識人批判は、AIが少数派の「真正な声」を生成すると主張する現象の倫理批判と直結する。",
         "related_ai_phenomenon": "AIによる他者の声の合成と真正性問題"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "サバルタン",
         "description": "スピヴァクの概念は哲学DBの政治哲学・批判理論と直接共有される。"},
    ],
})

add({
    "name_ja": "黒い皮膚・白い仮面",
    "name_en": "Black Skin, White Masks",
    "name_original": "Peau noire, masques blancs",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "第一・第二波フェミニズム期",
    "definition": "フランツ・ファノンが1952年に著した精神分析的・現象学的著作。アンティーユの黒人主体が植民地文化のなかで白人的視線を内面化し、自己疎外・劣等コンプレックスを形成する過程を分析した。ポストコロニアル精神分析批評の創始的テクスト。",
    "background": "マルティニーク出身の精神科医ファノンが、フランス植民地教育のなかで形成された自身の経験を理論化。",
    "development": "サイード、バーバ、現代の脱植民地心理学・批判的人種理論の重要な源泉。",
    "historical_context": "戦後フランス植民地体制末期、アルジェリア独立闘争前夜。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctt81q8s",
    "primary_source_type": "JSTOR — Fanon canonical edition (Grove Press / Pluto)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ファノン",
         "description": "ファノンの精神分析は哲学DBの実存主義・批判的人種哲学と直結する。"},
    ],
})

add({
    "name_ja": "植民地主義論",
    "name_en": "Discourse on Colonialism",
    "name_original": "Discours sur le colonialisme",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "第一・第二波フェミニズム期",
    "definition": "エメ・セゼール（マルティニーク出身詩人・政治家）が1950年に発表した政治的著作。植民地主義をヨーロッパ近代文明の本質的構造として暴き、ナチズムをヨーロッパが他地域で実践してきた植民地暴力の本国回帰として位置づけた。ネグリチュード運動の理論的中核。",
    "background": "戦後フランスの植民地体制と知識人の沈黙への激烈な批判。",
    "development": "ファノン、サンゴール、現代の脱植民地批評の倫理的基盤として参照され続ける。",
    "historical_context": "戦後脱植民地化運動の初期、ネグリチュード運動の理論化期。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctt9qfkrm",
    "primary_source_type": "JSTOR — Césaire 'Discourse on Colonialism' (Monthly Review Press)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "精神の脱植民地化",
    "name_en": "Decolonising the Mind",
    "name_original": "Decolonising the Mind",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ケニア出身作家ングギ・ワ・ジオンゴが1986年に発表したエッセイ集。アフリカ作家が植民地言語（英語・フランス語）で書くことの矛盾を批判し、母語（彼自身はギクユ語）で書くことを脱植民地化実践として提起した。言語選択を文学倫理の根本問題として位置づける。",
    "background": "ンググギ自身の英語からギクユ語への執筆言語転換が背景。",
    "development": "現代のアフリカ文学論、世界文学論、「メタ言語的」批評の重要な源泉。",
    "historical_context": "80年代アフリカ独立後第二世代の言語的脱植民地化議論。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctv1bmzm9p",
    "primary_source_type": "JSTOR — Ngũgĩ canonical edition (James Currey)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "言語", "status": "rethinking",
         "rationale": "「植民地言語からの脱却」というンググギの問題は、英語中心のLLMが世界言語の認識的階層を再生産する現象として再浮上する。",
         "related_ai_phenomenon": "LLMの英語中心バイアスと言語的不平等"},
        {"axis": "受容", "status": "rethinking",
         "rationale": "母語選択の文学倫理は、AI翻訳・AI文学生成が母語文化に与える受容構造の変容と直結する。",
         "related_ai_phenomenon": "AI翻訳と母語文化の受容構造変化"},
    ],
})

add({
    "name_ja": "ネクロポリティクス",
    "name_en": "necropolitics",
    "name_original": "necropolitics",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "アシル・ンベンベが2003年論文「Necropolitics」（Public Culture誌）で提起した概念。フーコーの生権力論を継承しつつ、現代の主権権力は単に「生かす権力」ではなく、誰を死に晒し誰を死なせるかを決定する「死の権力」として機能すると論じた。植民地・難民・スラム・占領状態の分析装置。",
    "background": "アガンベン「ホモ・サケル」論、ファノン植民地暴力論との対話。",
    "development": "ガザ・難民・気候難民・パンデミック分析の理論的中核に。",
    "historical_context": "2000年代の対テロ戦争・難民危機・人道主義の批判。",
    "primary_source_url": "https://muse.jhu.edu/article/39984",
    "primary_source_type": "Project MUSE — Mbembe 'Necropolitics' (Public Culture 2003)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ネクロポリティクス",
         "description": "ンベンベの概念は哲学DBの生政治論・主権論と直接共有される。"},
    ],
})

add({
    "name_ja": "植民地的差異",
    "name_en": "colonial difference",
    "name_original": "colonial difference",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "ウォルター・ミニョーロが『ローカル・ヒストリーズ／グローバル・デザイン』（2000）で展開した概念。近代／植民地世界システムが認識論的階層を制度化し、特定の知（西洋・男性・人種化された知）を普遍化し、他の知を「ローカル」として周縁化する構造的差異を指す。脱植民地的選択肢の前提となる認識装置。",
    "background": "ラテンアメリカ脱植民地集団（modernity/coloniality group）の理論的核。",
    "development": "現代の「認識論的脱植民地化」運動、世界文学論、AI倫理の認識論批判まで参照される。",
    "historical_context": "2000年代ラテンアメリカ脱植民地的転回の理論成熟期。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctt7t9cp",
    "primary_source_type": "JSTOR — Mignolo Local Histories/Global Designs (Princeton UP)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "植民地的差異",
         "description": "ミニョーロの認識論批判は人類学DBの近代-植民地批判と共有される。"},
    ],
})

add({
    "name_ja": "ポストコロニアル理性",
    "name_en": "postcolonial reason",
    "name_original": "postcolonial reason",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ロバート・J・C・ヤングが『ポストコロニアリズム——歴史的入門』（2001）等で整序した概念。サイード・スピヴァク・バーバの三角形を超えて、ポストコロニアル批評を、植民地経験から発する固有の知の様式・批評理性として体系化する試み。マルクス主義・脱構築・反人種主義の交差を理論的に編成する。",
    "background": "ヤングの『White Mythologies』（1990）以降の系譜整理の集大成。",
    "development": "現代の世界文学論、グローバル批評、トランスナショナル文学研究の理論的整理基盤。",
    "historical_context": "2000年代のポストコロニアル批評の制度化と自己反省期。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctv2867pd",
    "primary_source_type": "JSTOR — Young Postcolonialism (Blackwell)",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ディアスポラ・アイデンティティ",
    "name_en": "diaspora identities",
    "name_original": "diaspora identities",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "スチュアート・ホールが1990年論文「文化的アイデンティティとディアスポラ」で展開した概念。ディアスポラ的アイデンティティは固定的本質ではなく、絶え間ない差異化と類似化のプロセスを通じて生成・変容するものであり、文学テクストはその構築の場として機能すると論じた。",
    "background": "ジャマイカ系英国人のホール自身の位置、バーミンガム文化研究センターの方法論的展開。",
    "development": "現代のトランスナショナル文学研究、ブラック・アトランティック論（ポール・ギルロイ）、移民文学批評の理論的基盤。",
    "historical_context": "80-90年代英国の多文化主義論争とブラック・カルチュラル・スタディーズ。",
    "primary_source_url": "https://www.jstor.org/stable/4538030",
    "primary_source_type": "JSTOR — Hall 'Cultural Identity and Diaspora' (1990)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "ディアスポラ",
         "description": "ホールの理論は人類学DBの移民・離散研究と直結する。"},
    ],
})


# ===============================================================
# CATEGORY C — Ecocriticism / environmental humanities (10)
# ===============================================================

add({
    "name_ja": "エコクリティシズム",
    "name_en": "ecocriticism",
    "name_original": "ecocriticism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "シェリル・グロトフェルティが1996年に編纂した『エコクリティシズム・リーダー』の序論で定義した批評領域。文学と物理的環境の関係を研究する批評で、文学が自然・場所・非人間的世界をどのように表象し、人間中心主義をいかに再生産・批判するかを主題化する。ASLE（文学環境学会）創設と並行して制度化された。",
    "background": "70-80年代環境運動と文学批評の合流、米国西部・自然書物伝統の再評価。",
    "development": "ローレンス・ビュエル、スコット・スロヴィック、現代のポストヒューマン・気候批評まで連続的に展開。",
    "historical_context": "90年代ASLE創設期（1992）と環境人文学の制度化。",
    "primary_source_url": "https://ugapress.org/book/9780820317816/the-ecocriticism-reader/",
    "primary_source_type": "U. Georgia Press — Glotfelty & Fromm (eds.) canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "人間中心主義への批判は、AI時代のポストヒューマン主体性論と直結する。",
         "related_ai_phenomenon": "ポストヒューマンAI主体性論"},
    ],
})

add({
    "name_ja": "エコクリティシズム・リーダー",
    "name_en": "The Ecocriticism Reader",
    "name_original": "The Ecocriticism Reader",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "シェリル・グロトフェルティとハロルド・フロムが1996年に編纂したアンソロジー。エコクリティシズムの「波」（第一波：自然書物再評価、第二波：環境正義）の理論的基礎テクストを集約し、批評領域の制度的成立を象徴する書物となった。グロトフェルティ序論は領域定義テクストとして引用され続ける。",
    "background": "ASLE設立（1992）から数年後の理論的成熟期に編集。",
    "development": "現代の環境人文学・第四波エコクリティシズム（人新世・気候）の出発点として参照される。",
    "historical_context": "90年代環境人文学の制度化と方法論的セルフ・デフィニション期。",
    "primary_source_url": "https://ugapress.org/book/9780820317816/the-ecocriticism-reader/",
    "primary_source_type": "U. Georgia Press canonical anthology",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "環境的想像力",
    "name_en": "The Environmental Imagination",
    "name_original": "The Environmental Imagination",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ローレンス・ビュエルが1995年に発表した著作。ヘンリー・D・ソローを中心に、環境テクストが場所・非人間性・生態系をどのように文学的に構築するかを分析し、エコクリティシズム理論の中核モデルを提供した。「環境テクスト」の四基準（非人間環境への言及、人間関心の脱中心化、人間の環境責任、自然の過程性）を提示した。",
    "background": "ビュエル自身のソロー研究の延長線上で形成。",
    "development": "ビュエルの後続著作『環境批評の未来』（2005）への発展、ポスト人新世エコクリティシズムへの批判的継承。",
    "historical_context": "90年代米国エコクリティシズム第一波の理論的頂点。",
    "primary_source_url": "https://www.hup.harvard.edu/books/9780674258624",
    "primary_source_type": "Harvard UP — Buell canonical edition",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "ディープ・エコロジー（文学批評）",
    "name_en": "deep ecology in literature",
    "name_original": "deep ecology",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "ノルウェーの哲学者アルネ・ネス（1973）が提起したディープ・エコロジー思想を、文学批評が分析・適用する枠組み。生命中心的平等、生態系内在的価値、人間例外主義の解体を文学テクストに見出し、自然書物・荒野文学・先住民文学批評の理論的基礎とする。",
    "background": "70年代環境哲学の文学批評への流入。",
    "development": "ゲイリー・スナイダー詩学、現代の生命中心エコクリティシズム、気候フィクション批評まで継承。",
    "historical_context": "80-90年代米国環境運動と文学批評の合流。",
    "primary_source_url": "https://plato.stanford.edu/entries/ethics-environmental/",
    "primary_source_type": "SEP — Environmental Ethics entry",
    "importance_score": 4,
    "source_tier": "secondary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "エコフェミニズム",
    "name_en": "ecofeminism",
    "name_original": "ecofeminism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "ポスト構造主義以後の批評期",
    "definition": "フランソワーズ・ドボンヌが1974年に造語した運動・批評枠組み。女性抑圧と自然搾取を構造的に同根のものとして分析し、家父長制と人間中心主義の連結を批判する。文学批評ではキャロリン・マーチャント『自然の死』、グレタ・ガード等が代表理論家。",
    "background": "70年代フランス・米国の女性運動と環境運動の合流。",
    "development": "ヴァル・プラムウッド批判的エコフェミニズム、現代の物質的フェミニズム（ステイシー・アライモ）まで展開。",
    "historical_context": "70-80年代エコ社会運動の批評理論化。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctt5vk5dt",
    "primary_source_type": "JSTOR — Plumwood Feminism and the Mastery of Nature",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "core",
})

add({
    "name_ja": "アニマル・スタディーズ（文学批評）",
    "name_en": "animal studies in literature",
    "name_original": "literary animal studies",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "1990年代後半以降、ジャック・デリダ『動物を追う、ゆえに我あり』、ケアリー・ウルフ等が形成した批評領域。文学テクストにおける人間／動物境界の構築・脱構築を分析し、種差主義（speciesism）の言説的構造を主題化する。クィア理論・脱植民地批評との接続が顕著。",
    "background": "デリダ後期の動物論、コーラ・ダイアモンド等の倫理哲学の文学批評への流入。",
    "development": "ドナ・ハラウェイ「伴侶種」論、現代のマルチスピーシーズ・エスノグラフィ文学批評まで展開。",
    "historical_context": "2000年代の動物倫理・種を超えた批評の制度化。",
    "primary_source_url": "https://muse.jhu.edu/book/68716",
    "primary_source_type": "Project MUSE — Wolfe Animal Rites (U. Chicago)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "ポストヒューマニズム",
    "name_en": "posthumanism",
    "name_original": "posthumanism",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "ケアリー・ウルフ『ポストヒューマニズムとは何か』（2010）、ロージ・ブライドッティ『ポストヒューマン』（2013）等が体系化した枠組み。啓蒙的「人間」概念の人種化・男性化・西洋化された前提を批判し、人間／非人間境界の脱構築から新たな主体性・倫理・批評方法論を構想する。",
    "background": "脱構築・ハラウェイのサイボーグ論・ラトゥール行為者ネットワーク理論の合流。",
    "development": "現代AI倫理、気候批評、デジタル人文学における中核理論として展開中。",
    "historical_context": "2010年前後の生命科学・AI技術発展と批評理論の応答期。",
    "primary_source_url": "https://www.jstor.org/stable/10.5749/j.ctttv8hq",
    "primary_source_type": "JSTOR — Wolfe What Is Posthumanism? (U. Minnesota)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "主体", "status": "rethinking",
         "rationale": "「人間」概念の脱構築は、AI時代における主体性カテゴリの再考の理論的基盤を提供する。",
         "related_ai_phenomenon": "AI主体性とポストヒューマン主体論"},
        {"axis": "創造性", "status": "rethinking",
         "rationale": "人間固有とされてきた創造性概念を、非人間的アクターを含む分散的プロセスとして再考する基盤を提供する。",
         "related_ai_phenomenon": "AIと創造性の再定義"},
    ],
    "cross_domain": [
        {"target_db": "PHIL", "link_type": "shared_concept",
         "target_entity_name": "ポストヒューマニズム",
         "description": "ウルフ・ブライドッティの理論は哲学DBのポストヒューマン哲学と直接共有される。"},
        {"target_db": "AI-Development", "link_type": "borrowed_from",
         "target_entity_name": "ポストヒューマン主体性",
         "description": "AI発展DBにおけるAI主体性論議の哲学的基盤。"},
    ],
})

add({
    "name_ja": "人新世文学",
    "name_en": "Anthropocene literature",
    "name_original": "Anthropocene literature",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "パウル・クルッツェンら（2000）の地質学的概念「人新世」を契機に、2010年代以降形成された批評領域。人間が地球システムの変動要因となった時代における文学の表象可能性・スケール問題（個人スケールと地質学的スケールの乖離）を主題化する。ディペシュ・チャクラバルティ「気候の歴史——四つのテーゼ」（2009）が代表的議論。",
    "background": "気候科学の知見と人文学的応答の接続。",
    "development": "アミタヴ・ゴーシュ『大いなる錯乱』（2016）、ロブ・ニクソン「ゆっくりとした暴力」、現代のクライ・フィ批評まで展開。",
    "historical_context": "2010年代の気候危機認識の人文学的転回。",
    "primary_source_url": "https://www.jstor.org/stable/10.1086/596640",
    "primary_source_type": "JSTOR — Chakrabarty 'The Climate of History' (Critical Inquiry 2009)",
    "importance_score": 5,
    "source_tier": "primary",
    "canonical_in_region": "core",
    "fourth_axes": [
        {"axis": "受容", "status": "rethinking",
         "rationale": "「人類規模の物語」を読む受容構造の問題は、AIが大規模時間スケールの叙述を生成する現象と接続する。",
         "related_ai_phenomenon": "AI生成による大規模スケール叙述"},
        {"axis": "物語", "status": "rethinking",
         "rationale": "個人スケールと地質学的スケールの不可通約性は、人間中心的物語形式を根本的に問い直す。",
         "related_ai_phenomenon": "AIによる非人間スケール叙述生成"},
    ],
    "cross_domain": [
        {"target_db": "AI-Development", "link_type": "parallel",
         "target_entity_name": "人新世とAI",
         "description": "AI発展DBの「技術圏（technosphere）」論と人新世概念は並行的に展開する。"},
    ],
})

add({
    "name_ja": "クライ・フィ（気候フィクション）",
    "name_en": "climate fiction (cli-fi)",
    "name_original": "cli-fi",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "ジャーナリスト／作家のダン・ブルームが2007-2008年頃に造語した語が学術的批評領域として制度化したジャンル／批評枠組み。気候変動を中心主題とする小説（キム・スタンリー・ロビンソン、マーガレット・アトウッド、リチャード・パワーズ等）と、それを分析する批評を含む。",
    "background": "アル・ゴア『不都合な真実』（2006）以降の気候言説の高揚と文学的応答。",
    "development": "アダム・トレクスラー『人新世フィクション』（2015）、現代の気候人文学の中核ジャンル。",
    "historical_context": "2010年代の気候危機の文化的可視化期。",
    "primary_source_url": "https://www.jstor.org/stable/j.ctt183q5n6",
    "primary_source_type": "JSTOR — Trexler Anthropocene Fictions (U. Virginia)",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
})

add({
    "name_ja": "環境人文学",
    "name_en": "environmental humanities",
    "name_original": "environmental humanities",
    "original_script": "roman",
    "subfield_code": "lit_theory",
    "region": "理論",
    "period_key": "環境・脱植民地・ポストヒューマン期",
    "definition": "2010年代に制度化された学際領域。エコクリティシズム・環境史・環境哲学・環境人類学を統合し、気候・生物多様性・人新世を人文学から分析する枠組み。学術誌『Environmental Humanities』（2012-）創刊が制度的画期。デボラ・バード・ローズ、トム・ファン・ドーレン等が中核理論家。",
    "background": "個別領域（エコクリティシズム等）の成熟と学際的合流の必要性。",
    "development": "現代の気候人文学、惑星人文学、デジタル環境人文学の総称的枠組みとして機能。",
    "historical_context": "2010年代の気候危機を契機とする人文学の学際的再編。",
    "primary_source_url": "https://read.dukeupress.edu/environmental-humanities",
    "primary_source_type": "Duke UP — Environmental Humanities journal",
    "importance_score": 4,
    "source_tier": "primary",
    "canonical_in_region": "major",
    "cross_domain": [
        {"target_db": "AN", "link_type": "shared_concept",
         "target_entity_name": "環境人類学",
         "description": "環境人文学は人類学DBの環境人類学領域と直接統合される。"},
    ],
})


# ---------------------------------------------------------------
# Relations payload (sequential after concepts inserted)
# ---------------------------------------------------------------
RELATIONS: list[tuple[str, str, str, str]] = [
    # A. Gender / feminist criticism internal
    ("自分ひとりの部屋", "ガイノクリティシズム", "influences",
     "ウルフの問題提起がショウォルターの女性作家中心批評の前提となる。"),
    ("自分ひとりの部屋", "屋根裏の狂女", "influences",
     "ウルフの女性作家論がギルバート＆グーバーの19世紀女性作家分析の出発点。"),
    ("ガイノクリティシズム", "屋根裏の狂女", "influences",
     "ショウォルターの方法論がギルバート＆グーバーの実践的批評を可能にした。"),
    ("女性的エクリチュール", "女性的話法", "influences",
     "シクスーとイリガライは「フランス・フェミニズム」を構成し相互に呼応する。"),
    ("女性的エクリチュール", "アブジェクシオン（おぞましきもの）", "influences",
     "シクスーとクリステヴァは身体・無意識への注目を共有しつつ展開する。"),
    ("パフォーマティヴィティ", "クィア理論（文学批評）", "influences",
     "バトラーのパフォーマティヴィティ理論がクィア理論の中核装置となった。"),
    ("クィア理論（文学批評）", "ポストフェミニズム", "criticizes",
     "クィア理論はポストフェミニズム的個人選択論を集合的政治の観点から批判する。"),
    ("インターセクショナリティ", "ガイノクリティシズム", "criticizes",
     "クレンショーの理論はガイノクリティシズムの単一カテゴリ的女性主体を批判する。"),
    ("インターセクショナリティ", "パフォーマティヴィティ", "influences",
     "交差性概念がバトラー後期の規範性論をより複雑な軸へと展開させた。"),

    # B. Postcolonial criticism internal
    ("オリエンタリズム", "ミミクリ／ハイブリディティ／第三空間", "influences",
     "サイードの言説権力論がバーバの植民地主体論の出発点となる。"),
    ("オリエンタリズム", "サバルタン", "influences",
     "サイードの他者表象論がスピヴァクのサバルタン論を理論的に準備した。"),
    ("オリエンタリズム", "ポストコロニアル理性", "influences",
     "サイードの『オリエンタリズム』がヤングのポストコロニアル理性整序の中軸。"),
    ("黒い皮膚・白い仮面", "ミミクリ／ハイブリディティ／第三空間", "influences",
     "ファノンの内面化分析がバーバのミミクリ概念の理論的源泉。"),
    ("黒い皮膚・白い仮面", "植民地主義論", "influences",
     "セゼールはファノンに直接的影響を与えた（ファノンはセゼールの教え子）。"),
    ("植民地主義論", "黒い皮膚・白い仮面", "influences",
     "セゼールの植民地批判はファノンの精神分析的展開の前提となる。"),
    ("精神の脱植民地化", "植民地的差異", "influences",
     "ンググギの言語論はミニョーロの認識論的階層批判と並行的展開。"),
    ("ネクロポリティクス", "サバルタン", "extends",
     "ンベンベはスピヴァクの「語りえなさ」を「死に晒される者」の問題へと拡張する。"),
    ("植民地的差異", "オリエンタリズム", "extends",
     "ミニョーロはサイードの言説論を認識論的階層論として拡張する。"),
    ("ディアスポラ・アイデンティティ", "ミミクリ／ハイブリディティ／第三空間", "influences",
     "ホールのディアスポラ論はバーバのハイブリディティ論と並行・相互参照する。"),

    # C. Ecocriticism internal
    ("エコクリティシズム", "エコクリティシズム・リーダー", "contains",
     "グロトフェルティ編アンソロジーがエコクリティシズム領域を制度化した。"),
    ("エコクリティシズム", "環境的想像力", "contains",
     "ビュエル『環境的想像力』がエコクリティシズム第一波の理論的頂点を成す。"),
    ("エコクリティシズム", "ディープ・エコロジー（文学批評）", "contains",
     "ディープ・エコロジー思想はエコクリティシズム第一波の哲学的源泉。"),
    ("エコクリティシズム", "エコフェミニズム", "extends",
     "エコフェミニズムはエコクリティシズムにジェンダー軸を導入する拡張派。"),
    ("エコクリティシズム", "アニマル・スタディーズ（文学批評）", "extends",
     "アニマル・スタディーズはエコクリティシズムの種境界批判への展開。"),
    ("ポストヒューマニズム", "アニマル・スタディーズ（文学批評）", "influences",
     "ポストヒューマニズムはアニマル・スタディーズの理論的基礎を提供する。"),
    ("ポストヒューマニズム", "人新世文学", "influences",
     "ポストヒューマニズムが人新世文学批評の主体論的基盤となる。"),
    ("人新世文学", "クライ・フィ（気候フィクション）", "contains",
     "クライ・フィは人新世文学の中核ジャンルを構成する。"),
    ("人新世文学", "環境人文学", "extends",
     "人新世文学は環境人文学の文学領域における中核展開。"),
    ("環境人文学", "エコクリティシズム", "extends",
     "環境人文学はエコクリティシズムを学際的に再編・拡張する。"),

    # Cross-category bridges (Gender × Postcolonial × Eco)
    ("インターセクショナリティ", "サバルタン", "influences",
     "クレンショーの交差性とスピヴァクのサバルタン論はジェンダー化された下位主体の問題を共有する。"),
    ("エコフェミニズム", "インターセクショナリティ", "influences",
     "エコフェミニズムは女性・自然・人種化された人々の抑圧を交差的に分析する。"),
    ("ポストヒューマニズム", "サバルタン", "influences",
     "ポストヒューマンの主体論はスピヴァクの主体批判を非人間まで拡張する。"),
    ("ポストヒューマニズム", "パフォーマティヴィティ", "influences",
     "バトラーのパフォーマティヴィティ論はポストヒューマン主体構築論の方法的源泉。"),
    ("ネクロポリティクス", "人新世文学", "influences",
     "ンベンベのネクロポリティクスは気候難民・環境的人種主義の批評的基盤。"),
    ("精神の脱植民地化", "環境人文学", "influences",
     "ンググギの言語的脱植民地化は環境人文学の認識論的脱植民地化と接続。"),
]


# ---------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------

def main() -> int:
    print(f"[wave7_c37_critical_theory] inserting {len(CONCEPTS)} concepts...")
    if len(CONCEPTS) != 30:
        print(f"  WARNING: expected 30 concepts, got {len(CONCEPTS)}")

    name_to_id: dict[str, int] = {}
    fourth_count = 0
    cd_count = 0
    relation_count = 0

    with LitDB() as db:
        # 1) Seed periods
        period_ids: dict[str, int] = {}
        for name_ja, name_en, sy, ey, desc in PERIODS_TO_SEED:
            pid = db.get_or_create_period(
                name_ja=name_ja, region="理論",
                start_year=sy, end_year=ey,
                name_en=name_en, description=desc,
            )
            period_ids[name_ja] = pid
            print(f"  period: {name_ja!r} -> id={pid}")

        # 2) Insert concepts
        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            period_key = entry.pop("period_key", None)
            if period_key:
                entry["period_id"] = period_ids[period_key]

            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid

            for axis_entry in fourth_axes:
                db.tag_fourth_transform(cid, **axis_entry)
                fourth_count += 1

            for cd in cross_domain:
                db.insert_cross_domain(
                    lit_entity_type="concept",
                    lit_entity_id=cid,
                    target_db=cd["target_db"],
                    link_type=cd["link_type"],
                    target_entity_id=cd.get("target_entity_id"),
                    target_entity_name=cd.get("target_entity_name"),
                    description=cd.get("description"),
                )
                cd_count += 1

        # 3) Insert relations
        for src_name, tgt_name, rtype, desc in RELATIONS:
            sid = name_to_id.get(src_name)
            tid = name_to_id.get(tgt_name)
            if not sid or not tid:
                print(f"  [warn] relation skipped: {src_name!r} -> {tgt_name!r}"
                      f" (sid={sid}, tid={tid})")
                continue
            db.insert_relation(
                source_type="concept", source_id=sid,
                target_type="concept", target_id=tid,
                relation_type=rtype,
                description=desc,
                confidence=4,
            )
            relation_count += 1

        # 4) Summary
        summary = db.progress_summary()
        print()
        print("[wave7_c37_critical_theory] inserted:")
        print(f"  concepts: {summary['concepts']}")
        print(f"  fourth_transform_tags: {summary['fourth_transform_tags']} "
              f"(this run: +{fourth_count})")
        print(f"  cross_domain: {summary['cross_domain']} "
              f"(this run: +{cd_count})")
        print(f"  relations: {summary['relations']} "
              f"(this run: +{relation_count})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
