from lit_db_helper import LitDB


CONCEPTS = [
    # Underground print and clandestine reading
    ("地下写本の再筆写連鎖", "clandestine manuscript recopying", "禁書的テクストが筆写で変形しながら広がる過程。", 99),
    ("偽アムステルダム刊記", "false Amsterdam imprint", "検閲回避のため出版地をアムステルダムと偽る刊記慣行。", 99),
    ("禁書カタログの逆利用", "inverted use of forbidden catalogues", "禁書目録が読者の探索リストとして機能する現象。", 100),
    ("小冊子の綴じ合わせ読書", "pamphlet sammelband reading", "複数小冊子を合冊し論争的連関で読む実践。", 100),
    ("密輸本の港湾経路", "smuggled book port routes", "港湾商人網を通じた啓蒙書籍の非公式流通。", 100),
    ("読書協会の回覧規約", "reading society circulation rules", "会員制読書会で貸出順と閲覧期限を定める制度。", 100),
    # Periodical forms and urban observation
    ("傍観者紙の仮面語り", "spectator-paper masked narrator", "都市観察者の仮面で道徳批評を行う随筆技法。", 99),
    ("投書欄の擬似公共圏", "letter-column pseudo public sphere", "読者投稿を装い世論形成を演出する紙面構造。", 100),
    ("カフェ紙上対話", "coffeehouse print dialogue", "カフェ談義を紙面上の対話体へ移す啓蒙的形式。", 100),
    ("都市断章の番号配列", "numbered urban fragments", "都市観察を番号付き断章で蓄積する記述法。", 102),
    ("風俗素描の匿名観察者", "anonymous observer in sketches", "身分を隠す観察者が社会風俗を分類する語り。", 100),
    ("定期刊行物の連載寓話", "serial fable in periodicals", "新聞・雑誌で連載される短い道徳寓話形式。", 100),
    # Theater, performance, and stage controversy
    ("市民悲劇の父権審問場面", "paternal interrogation in bourgeois tragedy", "市民悲劇で父が娘の徳を問い詰める定型場面。", 101),
    ("涙の喜劇の和解卓", "reconciliation table in comedie larmoyante", "涙の喜劇で食卓が家族和解の舞台となる装置。", 101),
    ("俳優の冷淡な熱演", "cold enthusiasm of the actor", "情念を内面化せず計算で感動を生む演技観。", 100),
    ("観客涙の道徳証明", "spectator tears as moral proof", "観劇中の涙を徳性の証拠とみなす受容論。", 101),
    ("家庭内舞台の徳教育", "domestic stage moral pedagogy", "家庭劇を通じて子女の感情と徳を訓練する考え。", 101),
    ("検閲前読合せ台本", "pre-censorship reading script", "上演許可前に私的朗読で流通する劇台本。", 100),
    # Sentiment, pedagogy, and epistolary microforms
    ("涙の余白注記", "tear-marked marginal note", "感傷小説の余白に涙や動揺を記す読書痕跡。", 101),
    ("教育書簡の段階課題", "graded tasks in educational letters", "書簡形式で学習課題を段階的に与える構成。", 101),
    ("女教師語りの権威化", "authorization of governess narration", "女性教育者の語りを道徳的権威として立てる技法。", 101),
    ("孤児相続筋の感傷化", "sentimental orphan inheritance plot", "孤児の相続問題を涙と徳の試練として描く筋立て。", 101),
    ("友情書簡の徳競争", "virtue rivalry in friendship letters", "友人間書簡で互いの徳を競い合う感傷的構図。", 101),
    ("読者宛序文の感情契約", "affective pact in prefaces to readers", "序文で読者に同情的反応をあらかじめ求める約束。", 101),
    # Exoticism, conjecture, and comparative forms
    ("ペルー女書簡の文明反照", "Peruvian-letter civilizational reflection", "異文化女性の手紙で欧州社会を反照する技法。", 100),
    ("東洋枠物語の哲学実験", "Oriental frame as philosophical experiment", "東洋的枠で慣習・快楽・統治を仮想実験する形式。", 100),
    ("旅行記脚注の懐疑装置", "skeptical footnotes in travel writing", "旅行記の脚注で証言の信頼性を揺さぶる方法。", 100),
    ("未開社会の推測年表", "conjectural chronology of savage society", "未開社会を段階史として仮構する啓蒙的説明。", 100),
    ("島嶼ユートピアの人口計算", "population arithmetic in island utopias", "島の理想社会を人口・食糧計算で描く方法。", 100),
    ("翻訳者序の異国性調整", "foreignness modulation in translator prefaces", "翻訳序文で異国性の強弱を読者向けに調整する実践。", 100),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, definition, period_id in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_eu_enlightenment",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="minor",
            )
    print(f"inserted_or_skipped={len(CONCEPTS)}")


if __name__ == "__main__":
    main()
