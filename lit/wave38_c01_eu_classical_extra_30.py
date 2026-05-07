#!/usr/bin/env python3
"""Wave 38 cluster 1: lit_eu_classical extra 30 niche concepts."""

from lit_db_helper import LitDB


ROWS = [
    # 1: ヘレニズム詩
    ("テオクリトス『牧歌』第7歌", "Theocritus Idylls 7", "Εἰδύλλια Ζ", "greek", 7, "シミキダスの旅と詩競演を描く、牧歌詩の自己言及的中核篇。"),
    ("カリマコス『原因論』", "Callimachus Aetia", "Αἴτια", "greek", 7, "祭儀や習俗の由来を短詩連作で探る、学識詩学の代表作。"),
    ("アポロニオス『アルゴナウティカ』第4巻", "Apollonius Argonautica Book 4", "Ἀργοναυτικά Δ", "greek", 7, "メデイア逃避と帰路遍歴を描き、叙事詩に恋愛心理を導入する巻。"),
    ("ビオン『アドニス哀歌』", "Bion Lament for Adonis", "Ἐπιτάφιος Ἀδώνιδος", "greek", 7, "アドニスの死を嘆く牧歌的哀歌。神話的喪と官能を結ぶ。"),
    ("モスコス『エウロペ』", "Moschus Europa", "Εὐρώπη", "greek", 7, "ゼウスによるエウロペ誘拐を小叙事詩化したヘレニズム詩。"),
    ("アラトス『現象』", "Aratus Phaenomena", "Φαινόμενα", "greek", 7, "星座と天候徴候を歌う教訓詩。天文学知を叙事詩語で整える。"),
    # 2: 希悲喜劇細部
    ("メナンドロス『気むずかし屋』", "Menander Dyskolos", "Δύσκολος", "greek", 7, "クネモンの孤立と結婚筋を描く、新喜劇で唯一ほぼ完全な作品。"),
    ("ソフォクレス『ピロクテテス』", "Sophocles Philoctetes", "Φιλοκτήτης", "greek", 6, "孤島の傷病者と説得の倫理をめぐる、後期ソフォクレス悲劇。"),
    ("エウリピデス『アウリスのイピゲネイア』", "Euripides Iphigenia at Aulis", "Ἰφιγένεια ἐν Αὐλίδι", "greek", 6, "遠征開始の犠牲をめぐり、家族愛と軍事政治の衝突を描く。"),
    ("アリストパネス『アカルナイの人々』", "Aristophanes Acharnians", "Ἀχαρνεῖς", "greek", 6, "私人の単独講和を通じ、戦時アテナイを嘲笑する初期政治喜劇。"),
    ("アリストパネス『鳥』詳論", "Aristophanes Birds detailed", "Ὄρνιθες", "greek", 6, "雲中都市ネフェロコッキュギア建設を描く、空想的政治喜劇。"),
    ("アリストパネス『雲』詳論", "Aristophanes Clouds detailed", "Νεφέλαι", "greek", 6, "ソクラテス像と詭弁教育を風刺し、旧新教育の対立を劇化する。"),
    # 3: 羅後期詩細部
    ("ペルシウス『諷刺詩集』", "Persius Saturae", "Saturae", "latin", 75, "ストア倫理を濃密な文体で語る、ネロ期ラテン諷刺詩集。"),
    ("スタティウス『テーバイス』詳論", "Statius Thebaid detailed", "Thebais", "latin", 75, "テーバイ兄弟戦争を十二巻で描く、フラウィウス朝叙事詩。"),
    ("シリウス・イタリクス『プニカ』詳論", "Silius Italicus Punica detailed", "Punica", "latin", 75, "第二次ポエニ戦争を歌う、現存最長のラテン歴史叙事詩。"),
    ("ウァレリウス・フラックス『アルゴナウティカ』", "Valerius Flaccus Argonautica", "Argonautica", "latin", 75, "アルゴー遠征神話を帝政期ラテン叙事詩として再構成する。"),
    ("マルティアリス『エピグラム集』第6巻", "Martial Epigrams Book 6", "Epigrammata VI", "latin", 75, "ドミティアヌス期ローマ社会を短詩で刺すエピグラム集の一巻。"),
    ("ユウェナリス『諷刺詩』第10歌", "Juvenal Saturae 10", "Satura X", "latin", 75, "願望の危険を列挙し、健全な心身のみを祈れと説く諷刺詩。"),
    # 4: 古典文献学・修辞学
    ("デメトリオス『文体論』", "Demetrius On Style", "Περὶ ἑρμηνείας", "greek", 75, "四文体説で散文表現を分類する、古代修辞批評の基礎文献。"),
    ("偽ロンギノス『崇高論』", "Pseudo-Longinus On the Sublime", "Περὶ ὕψους", "greek", 75, "崇高を読者を高揚させる文体効果として論じる批評書。"),
    ("ヘルモゲネス『争点論』", "Hermogenes Stases", "Περὶ στάσεων", "greek", 198, "法廷弁論の争点分類を体系化した、後期古代修辞学の教本。"),
    ("クインティリアヌス『弁論家の教育』第10巻", "Quintilian Institutio 10", "Institutio Oratoria X", "latin", 75, "読むべきギリシア・ラテン作家を列挙し、模倣訓練を論じる巻。"),
    ("ドナトゥス『大文法』", "Donatus Ars maior", "Ars maior", "latin", 198, "品詞論を中心にラテン語文法教育を標準化した後期古代教本。"),
    ("セルウィウス『アエネーイス注解』", "Servius Aeneid Commentary", "In Vergilii Aeneida commentarii", "latin", 198, "ウェルギリウス本文に神話・文法・古事を注す古代注釈の代表。"),
    # 5: 後期古代詩
    ("ノンノス『ディオニュソス譚』", "Nonnus Dionysiaca", "Διονυσιακά", "greek", 198, "ディオニュソスの征服譚を四十八巻で歌う後期ギリシア叙事詩。"),
    ("クイントス『ポストホメリカ』", "Quintus Smyrnaeus Posthomerica", "Τὰ μεθ᾽ Ὅμηρον", "greek", 198, "『イリアス』後からトロイア陥落までを継ぐ後期叙事詩。"),
    ("トリフィオドロス『トロイア落城』", "Triphiodorus Sack of Troy", "Ἰλίου ἅλωσις", "greek", 198, "木馬計略と都市陥落を小叙事詩として圧縮する後期作品。"),
    ("ムーサイオス『ヘーローとレアンドロス』", "Musaeus Hero and Leander", "Τὰ καθ᾽ Ἡρὼ καὶ Λέανδρον", "greek", 198, "海峡を渡る恋人の悲恋を精緻な小叙事詩に仕立てる。"),
    ("コルートス『ヘレネー誘拐』", "Coluthus Rape of Helen", "Ἑλένης ἁρπαγή", "greek", 198, "パリス審判からヘレネー連行までを短叙事詩で描く。"),
    ("アウィエヌス『アラテア』", "Avienius Aratea", "Aratea", "latin", 198, "アラトス天文詩をラテン語で翻案した後期古代の教訓詩。"),
]


def main() -> None:
    with LitDB() as db:
        inserted = 0
        for name_ja, name_en, name_original, script, period_id, definition in ROWS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code="lit_eu_classical",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="primary",
                canonical_in_region="minor",
            )
            inserted += int(bool(cid))
    print(f"Processed {inserted} concepts")


if __name__ == "__main__":
    main()
