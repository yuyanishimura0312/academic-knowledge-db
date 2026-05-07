from lit_db_helper import LitDB


CONCEPTS = [
    # 1. French realist micro-techniques
    ("パリ下宿屋の嗅覚的目録", "Olfactory boarding-house inventory", 120, "安下宿の匂いを社会階層の索引にする描写法。"),
    ("公証人文書の筋立て化", "Notarial document plotting", 120, "契約書や遺言状を小説の因果装置に変える手法。"),
    ("地方新聞投書のリアリズム", "Provincial newspaper letter realism", 120, "投書欄や噂記事を地方社会の声として組み込む技法。"),
    ("ブルジョワ室内の埃描写", "Dust in bourgeois interiors", 120, "家具の埃や摩耗で停滞した家計を示す細部。"),
    ("薬瓶ラベルの欲望記号", "Pharmacy-label desire sign", 120, "薬瓶やラベルを身体不安と消費欲の媒介にする細部。"),
    ("辻馬車運賃の階級標識", "Cab fare class marker", 120, "移動費の計算で人物の階級的限界を示す小道具。"),

    # 2. British provincial and institutional realism
    ("教区帳簿の叙事機能", "Parish ledger narrative function", 121, "教区記録を相続や扶助の物語証拠にする構成法。"),
    ("三巻本貸本屋の読者圧", "Triple-decker circulating-library pressure", 121, "貸本屋制度が章分量と婚姻筋に及ぼす制約。"),
    ("鉄道時刻表の偶然管理", "Railway timetable contingency", 121, "時刻表で遭遇と遅延を現実的に調整する手法。"),
    ("救貧院面会室の視線", "Workhouse visiting-room gaze", 121, "面会室の配置で貧困者の監視を可視化する場面設計。"),
    ("地方医師の症例語り", "Provincial doctor case narration", 121, "医師の症例口調を地域倫理の観察枠にする語り。"),
    ("駅馬車廃線の郷愁装置", "Disused coach-route nostalgia", 121, "廃れた交通路で地方共同体の時間差を示す細部。"),

    # 3. German, Swiss, and Austrian poetic realism microforms
    ("村境標石のノヴェレ機能", "Boundary-stone Novelle function", 173, "村境の標石を相続・禁忌・記憶の結節点にする技法。"),
    ("役場印章の小市民悲劇", "Municipal seal petty-bourgeois tragedy", 173, "印章や許認可が小市民の運命を左右する筋立て。"),
    ("林務官報告体リアリズム", "Forester-report realism", 173, "森林管理報告の文体で自然と所有を叙述する形式。"),
    ("堤防検分の共同体描写", "Dike-inspection community scene", 173, "堤防検分を村落秩序と責任の試金石にする場面。"),
    ("宿帳署名の身分偽装", "Inn-register identity disguise", 173, "宿帳の署名差異で身分偽装や帰属不安を示す細部。"),
    ("山岳測量図の運命線", "Alpine survey-map fate line", 173, "測量図の線を土地所有と悲劇的境界に重ねる象徴。"),

    # 4. Iberian and Italian naturalist local devices
    ("製塩場賃金表の自然主義", "Saltworks wage-table naturalism", 172, "賃金表を労働身体と家族崩壊の証拠にする描写。"),
    ("闘牛場座席表の階級配置", "Bullring seating hierarchy", 172, "闘牛場の席割りで都市階級の序列を可視化する技法。"),
    ("漁網修繕場の群集話法", "Net-mending collective speech", 171, "漁網修繕の場で共同体の噂を合唱的に示す話法。"),
    ("小作契約更新日の悲劇", "Tenancy-renewal-day tragedy", 171, "契約更新日を貧農一家の危機として組み立てる筋。"),
    ("修道院洗濯場の噂網", "Convent laundry rumor network", 172, "洗濯場の会話で宗教施設の俗世的情報網を描く技法。"),
    ("市電開通前夜の近代化不安", "Tramway-eve modernization anxiety", 172, "市電開通前夜を都市習俗の崩れとして描く場面型。"),

    # 5. Naturalist and symbolist threshold devices
    ("標本瓶越しの人物観察", "Specimen-jar character observation", 122, "標本瓶や実験室越しに人物を対象化する視覚装置。"),
    ("洗濯屋帳簿の遺伝記録化", "Laundry ledger heredity record", 122, "洗濯屋の帳簿を家系的汚れの記録へ転用する技法。"),
    ("鉱坑昇降籠の群衆焦点化", "Mine cage crowd focalization", 122, "昇降籠の密集を階級身体の共同焦点にする描写。"),
    ("温室ガラスのデカダンス視線", "Greenhouse-glass decadent gaze", 174, "温室ガラスを欲望と人工性の屈折面にする象徴。"),
    ("香水銘柄の反自然主義", "Perfume-brand anti-naturalism", 174, "香水名で身体描写を人工的記号へ逸らす技法。"),
    ("黄昏ランプの自由間接化", "Twilight lamp free-indirectness", 123, "灯火の変化で人物意識への滑り込みを支える細部。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_eu_realism",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
