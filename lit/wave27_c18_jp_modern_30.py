#!/usr/bin/env python3
"""Wave27 C18: Add 30 concepts to subfield lit_jp_modern (id=11)."""
import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "lit.sqlite"

# period IDs: 9=大正期, 10=昭和戦前期, 11=戦後期, 12=現代
CONCEPTS = [
    # Cluster 1: 大正文学 (period 9 大正期 / 10 昭和戦前期)
    ("有島武郎『或る女』", "Aru Onna", "或る女", "kanji", 9,
     "有島武郎1919長篇。早月葉子の自我解放と破滅を描く白樺派的人間ドラマ。"),
    ("武者小路実篤『友情』", "Yujo", "友情", "kanji", 9,
     "武者小路実篤1919年作。三角関係を通じ友情と理想主義を描く白樺派代表作。"),
    ("志賀直哉『暗夜行路』", "Anya Koro", "暗夜行路", "kanji", 9,
     "志賀直哉1921-37年大長篇。出生の秘密と精神的彷徨を描く近代私小説の頂点。"),
    ("横光利一『機械』", "Kikai", "機械", "kanji", 10,
     "横光利一1930年作。第四人称的視点と機械論的人間観で新感覚派の到達点を示す。"),
    ("川端康成『伊豆の踊子』", "Izu no Odoriko", "伊豆の踊子", "kanji", 9,
     "川端康成1926年作。旅芸人一座との交流を抒情的に描く新感覚派初期代表作。"),
    ("堀辰雄『風立ちぬ』", "Kaze Tachinu", "風立ちぬ", "kanji", 10,
     "堀辰雄1936-38年作。サナトリウムでの婚約者との生と死をリリックに描く。"),

    # Cluster 2: 戦時戦後 (period 10/11)
    ("火野葦平『麦と兵隊』", "Mugi to Heitai", "麦と兵隊", "kanji", 10,
     "火野葦平1938年従軍記。徐州会戦体験を描き戦争文学ベストセラーに。"),
    ("中島敦『山月記』", "Sangetsuki", "山月記", "kanji", 10,
     "中島敦1942年作。唐代伝奇『人虎伝』に基づく自尊心と孤高の寓話。"),
    ("太宰治『走れメロス』", "Hashire Merosu", "走れメロス", "kanji", 10,
     "太宰治1940年作。シラーの民譚を翻案し友情と信義を描く短篇代表作。"),
    ("坂口安吾『堕落論』", "Daraku-ron", "堕落論", "kanji", 11,
     "坂口安吾1946年評論。戦後の虚脱に「堕ちきれ」と説く実存的人間観。"),
    ("三島由紀夫『金閣寺』", "Kinkakuji", "金閣寺", "kanji", 11,
     "三島由紀夫1956年作。実在の放火事件を題材に美と存在の関係を探究。"),
    ("安部公房『砂の女』", "Suna no Onna", "砂の女", "kanji", 11,
     "安部公房1962年作。砂丘集落に閉じ込められた男を通じ実存と日常を寓話化。"),

    # Cluster 3: 戦後派 (period 11)
    ("大江健三郎『個人的な体験』", "Kojinteki na Taiken", "個人的な体験", "kanji", 11,
     "大江健三郎1964年作。障害児の誕生に直面する父の実存的決断を描く。"),
    ("開高健『夏の闇』", "Natsu no Yami", "夏の闇", "kanji", 11,
     "開高健1971年作。ベトナム戦争帰りの作家の倦怠と再生への模索を描く。"),
    ("遠藤周作『沈黙』", "Chinmoku", "沈黙", "kanji", 11,
     "遠藤周作1966年作。江戸初期切支丹弾圧下の宣教師の信仰葛藤を描く。"),
    ("井伏鱒二『黒い雨』", "Kuroi Ame", "黒い雨", "kanji", 11,
     "井伏鱒二1965-66年作。広島原爆体験を姪の日記形式で描く原爆文学代表作。"),
    ("中上健次『枯木灘』", "Karekinada", "枯木灘", "kanji", 11,
     "中上健次1977年作。紀州被差別部落の血族叙事詩、秋幸三部作の中核。"),
    ("円地文子『女坂』", "Onnazaka", "女坂", "kanji", 11,
     "円地文子1949-57年作。明治家父長制下で耐える正妻の半生を描く女性文学。"),

    # Cluster 4: 1980s-90s (period 12 現代)
    ("村上春樹『ノルウェイの森』", "Norwegian Wood", "ノルウェイの森", "kanji", 12,
     "村上春樹1987年作。1960年代末を舞台に喪失と性愛を描き世界的ヒット。"),
    ("村上龍『コインロッカー・ベイビーズ』", "Coin Locker Babies", "コインロッカー・ベイビーズ", "kanji", 12,
     "村上龍1980年作。コインロッカーに棄てられた二人の少年の暴力的青春。"),
    ("山田詠美『ベッドタイムアイズ』", "Bedtime Eyes", "ベッドタイムアイズ", "kanji", 12,
     "山田詠美1985年作。黒人米兵との関係を描き恋愛文学に新感覚を導入。"),
    ("吉本ばなな『キッチン』", "Kitchen", "キッチン", "kanji", 12,
     "吉本ばなな1988年作。喪失と再生を台所のイメージで描き世界的人気を獲得。"),
    ("川上弘美『センセイの鞄』", "Sensei no Kaban", "センセイの鞄", "kanji", 12,
     "川上弘美2001年作。元国語教師との静謐な恋愛を居酒屋・四季と共に描く。"),
    ("多和田葉子『犬婿入り』", "Inu Mukoiri", "犬婿入り", "kanji", 12,
     "多和田葉子1993年芥川賞作。郊外の塾を舞台に民話的越境性と異邦人を描く。"),

    # Cluster 5: 21c (period 12 現代)
    ("川上未映子『乳と卵』", "Chichi to Ran", "乳と卵", "kanji", 12,
     "川上未映子2007年作。豊胸と初潮をめぐる女三人の対話、関西弁で身体を語る。"),
    ("村田沙耶香『コンビニ人間』", "Konbini Ningen", "コンビニ人間", "kanji", 12,
     "村田沙耶香2016年芥川賞作。社会規範への不適応とコンビニ労働の親和性。"),
    ("又吉直樹『火花』", "Hibana", "火花", "kanji", 12,
     "又吉直樹2015年芥川賞作。漫才師徳永と先輩神谷の友情と芸の探究を描く。"),
    ("平野啓一郎『マチネの終わりに』", "Matinee no Owari ni", "マチネの終わりに", "kanji", 12,
     "平野啓一郎2016年作。クラシックギタリストとジャーナリストの大人の恋愛。"),
    ("朝井リョウ『何者』", "Nanimono", "何者", "kanji", 12,
     "朝井リョウ2012年直木賞作。SNS時代の就活生の自意識と承認欲求を描く。"),
    ("古川日出男『聖家族』", "Sei Kazoku", "聖家族", "kanji", 12,
     "古川日出男2008年作。東北六県を舞台に擬似家族と神話的時間軸を編む大長篇。"),
]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    for name_ja, name_en, name_orig, script, pid, definition in CONCEPTS:
        try:
            cur.execute(
                """INSERT INTO concepts
                   (name_ja, name_en, name_original, original_script,
                    subfield_id, region, period_id, definition,
                    importance_score, source_tier, canonical_in_region)
                   VALUES (?, ?, ?, ?, 11, '東アジア', ?, ?, 3, 'A', 'JP')""",
                (name_ja, name_en, name_orig, script, pid, definition),
            )
            inserted += 1
        except sqlite3.IntegrityError as e:
            skipped += 1
            print(f"SKIP {name_ja}: {e}")
    conn.commit()
    conn.close()
    print(f"Inserted: {inserted} / Skipped: {skipped} / Total: {len(CONCEPTS)}")


if __name__ == "__main__":
    main()
