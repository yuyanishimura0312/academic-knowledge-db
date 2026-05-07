from lit_db_helper import LitDB


CONCEPTS = [
    # Homeric signs and scholia
    ("アリストニコスのディプレ注", "Aristonican diple notes", "Aristonicus", "latin", 199, "ホメロス異読を示すヴェネトゥスA系の注記記号"),
    ("アリスタルコスのオベロス判定", "Aristarchean obelos", "ὀβελός", "greek", 7, "ホメロス本文中の疑義行を標示する校訂記号"),
    ("ゼノドトス的アテテーシス", "Zenodotean athetesis", "ἀθέτησις", "greek", 7, "叙事詩の不真正行を排除するアレクサンドリア校訂"),
    ("bTショリアの寓意注", "bT scholia allegoresis", "scholia bT", "latin", 199, "ホメロス叙述を倫理寓意へ読むビザンツ注釈層"),
    ("ディディモスの異読集積", "Didymean variants", "Δίδυμος", "greek", 7, "ホメロス本文の先行校訂差を列挙する注釈素材"),
    ("ホメロス・ケントロン聖書再編", "Homeric cento gospel", "κέντρων", "greek", 198, "ホメロス句を縫合し聖書物語へ換骨する技法"),
    # Greek lyric and meter
    ("アルクマン・パルテネイオン間奏", "Alcman partheneion refrain", "παρθένειον", "greek", 5, "乙女合唱歌に挿入される反復的な舞唱句"),
    ("サッポー大サッポー詩形", "Greater Sapphic stanza", "sapphicum maius", "latin", 5, "サッポー断片に見える拡張サッポー格律"),
    ("コリンナのボイオティア方言叙述", "Corinna Boeotian diction", "Βοιωτικά", "greek", 5, "地方神話をボイオティア語形で語る叙述様式"),
    ("ステシコロス三部詩形", "Stesichorean triad", "τριάς", "greek", 5, "ストロペー・反ストロペー・エポードスの叙事的連鎖"),
    ("プラクシラ・アドニス逆説", "Praxilla Adonis paradox", "Πράξιλλα", "greek", 5, "瀕死の神が俗な美を惜しむ断片的笑劇性"),
    ("ティモテオス新ディテュランボス", "Timothean new dithyramb", "διθύραμβος", "greek", 6, "旋律拡張と語彙過剰で知られる後期合唱革新"),
    # Hellenistic microgenres
    ("ポセイディッポス石碑エピグラム", "Posidippus lithika epigrams", "λιθικά", "greek", 7, "宝石と石の効能を題材化する連作短詩群"),
    ("カリマコスの細道美学", "Callimachean narrow path", "λεπταλέη ἀτραπός", "greek", 7, "大叙事詩を避け精緻小品を称揚する詩学標語"),
    ("ヘロンダス靴屋ミミアンボス", "Herodas cobbler mime", "μιμίαμβος", "greek", 7, "市井の靴屋場面をイアンボスで写す小劇詩"),
    ("シミアス斧型図像詩", "Simmias axe poem", "πέλεκυς", "greek", 7, "詩行の長短で斧形を作るヘレニズム視覚詩"),
    ("フィリタス語彙難解詩学", "Philitas gloss poetics", "Φιλίτας", "greek", 7, "希少語の博識を詩的価値に変える小品詩学"),
    ("ニカンドロス毒薬教訓詩", "Nicander toxicology poem", "Θηριακά", "greek", 7, "毒蛇と解毒法を六脚韻で列挙する専門詩"),
    # Roman antiquarian and fragmentary poetics
    ("ネウィウス土着サトゥルニウス", "Naevius Saturnian epic", "Saturnius", "latin", 73, "ローマ固有韻律でポエニ戦争を歌う古層叙事"),
    ("エンニウス夢中ホメロス転生", "Ennian Homeric dream", "somnium", "latin", 73, "詩人がホメロス魂の継承を夢で告げる発端場面"),
    ("ルキリウス韻律混交諷刺", "Lucilian mixed-meter satire", "satura", "latin", 73, "ヘクサメター確立前の多韻律ローマ諷刺"),
    ("ラエウィウス恋愛語造詩", "Laevius erotic neologism", "Erotopaegnia", "latin", 73, "希少合成語で恋愛小品を飾る新詩人先駆"),
    ("ウェルギリウス補遺カタレプトン", "Appendix Vergiliana Catalepton", "Catalepton", "latin", 74, "ウェルギリウス周辺に帰された短詩集の偽作層"),
    ("プリスキアヌス引用断片", "Priscian quotation fragment", "Priscianus", "latin", 199, "文法書引用だけで伝わる失伝ラテン詩句"),
    # Late antique and Byzantine poetics
    ("ノンノス的ディオニュシアカ六脚韻", "Nonnian hexameter", "Νόννος", "greek", 198, "語尾配置を厳格化した後期ギリシア叙事韻律"),
    ("パウロス・シレンティアリオス円蓋描写", "Paulus Silentiarius dome ekphrasis", "ἔκφρασις", "greek", 199, "聖ソフィア大聖堂の円蓋光を詩化する描写"),
    ("コリキオス機械仕掛けエクフラシス", "Choricius automata ekphrasis", "Χορίκιος", "greek", 199, "ガザ弁論学校で機械装置を描写する演説小品"),
    ("ロマノス離句アクロスティック", "Romanos kontakion acrostic", "ἀκροστιχίς", "greek", 199, "コンタキオン各連頭字に署名や主題を織る技巧"),
    ("プロバ聖書ウェルギリウス百行詩", "Proban biblical Virgilian cento", "cento", "latin", 198, "ウェルギリウス句だけで聖書史を再構成する女性詩"),
    ("ツェツェス政治詩十二音節", "Tzetzes political verse", "πολιτικὸς στίχος", "greek", 199, "学識注解を十二音節口語韻律で連ねるビザンツ詩"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, name_original, original_script, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=original_script,
                subfield_code="lit_eu_classical",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
                skip_duplicates=False,
            )


if __name__ == "__main__":
    main()
