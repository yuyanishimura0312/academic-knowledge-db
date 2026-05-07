from lit_db_helper import LitDB


SUBFIELD = "lit_jp_classical"
REGION = "東アジア"


def period_id(db: LitDB, name_ja: str) -> int:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region=?",
        (name_ja, REGION),
    ).fetchone()
    if not row:
        raise RuntimeError(f"missing period: {name_ja}")
    return row["id"]


def main() -> None:
    with LitDB() as db:
        p_jodai = period_id(db, "上代")
        p_chuko = period_id(db, "中古")
        p_chusei = period_id(db, "中世")
        p_kinsei = period_id(db, "近世")

        concepts = [
            # Cluster 1: 上代歌謡・祝詞の微細形式
            ("記歌の枕詞化地名", "Toponymic pillowing in Kojiki songs", "記歌枕詞地名", p_jodai, "記歌で地名が枕詞的に機能する局所的表現法。"),
            ("祝詞の称辞反復句", "Reiterated praise formulae in norito", "祝詞称辞反復", p_jodai, "祝詞で神名や徳目を畳みかける称辞の反復句。"),
            ("宣命体の訓読句切れ", "Kunten pauses in senmyo style", "宣命体訓読句切れ", p_jodai, "宣命体本文を訓読する際の独特な句読単位。"),
            ("風土記逸文の地名起源句", "Toponym etymon clauses in fudoki fragments", "風土記逸文地名起源句", p_jodai, "逸文風土記で地名由来を短く説明する定型句。"),
            ("人麻呂歌集略体歌", "Abbreviated-style poems in Hitomaro shu", "人麻呂歌集略体", p_jodai, "人麻呂歌集系歌に見える省略的表記の歌群。"),
            ("万葉巻十六戯笑譚歌", "Comic anecdotal poems in Man'yoshu 16", "巻十六戯笑譚歌", p_jodai, "万葉巻十六の笑話的場面を伴う戯歌群。"),
            # Cluster 2: 中古仮名日記・女房記録の手触り
            ("土佐日記船中時刻記法", "Shipboard time notation in Tosa Diary", "土佐日記船中時刻", p_chuko, "土佐日記の船旅場面で時刻を刻む記述法。"),
            ("蜻蛉日記贈答歌前書", "Headnotes to exchange poems in Kagero Diary", "蜻蛉日記贈答歌前書", p_chuko, "蜻蛉日記で贈答歌の事情を示す前書の型。"),
            ("紫式部日記消息文体", "Letter style in Murasaki Shikibu Diary", "紫式部日記消息文体", p_chuko, "紫式部日記に混在する消息文風の叙述単位。"),
            ("更級日記夢告場面", "Dream-oracle scenes in Sarashina Diary", "更級日記夢告", p_chuko, "更級日記で夢が信仰的指示として働く場面群。"),
            ("讃岐典侍日記臨終叙述", "Deathbed narration in Sanuki no Suke Diary", "讃岐典侍日記臨終", p_chuko, "堀河院臨終を近侍視点で記す看取りの叙述。"),
            ("成尋阿闍梨母集渡宋留守歌", "Stay-behind poems in Jojin's mother's collection", "成尋母集留守歌", p_chuko, "入宋した子を待つ母の留守居意識を詠む歌群。"),
            # Cluster 3: 王朝物語の巻・場面装置
            ("源氏物語夕顔巻物怪気配", "Spectral atmosphere in Yugao", "夕顔巻物怪気配", p_chuko, "夕顔巻で死を予兆する物怪的な気配の配置。"),
            ("源氏物語蛍巻物語論場面", "Narratology scene in Hotaru", "蛍巻物語論場面", p_chuko, "蛍巻で物語の虚構性を論じる会話場面。"),
            ("源氏物語総角巻八の宮遺言", "Hachi no Miya's testament in Agemaki", "総角巻八の宮遺言", p_chuko, "宇治十帖で娘たちの運命を縛る遺言場面。"),
            ("狭衣物語飛鳥井女君失踪", "Asukai lady disappearance in Sagoromo", "狭衣飛鳥井失踪", p_chuko, "狭衣物語で飛鳥井女君が物語線から消える局面。"),
            ("夜の寝覚中間欠巻問題", "Lacuna problem in Yoru no Nezame", "夜の寝覚欠巻問題", p_chuko, "夜の寝覚の中間部欠落をめぐる本文上の問題。"),
            ("我が身にたどる姫君後宮交錯", "Palace entanglement in Waga mi ni tadoru himegimi", "我が身後宮交錯", p_chuko, "後宮内の血縁と恋愛が複雑に絡む構成単位。"),
            # Cluster 4: 中世注釈・連歌・芸能の細部
            ("古今集毘沙門堂本注", "Bishamondo-bon Kokinshu glosses", "毘沙門堂本古今注", p_chusei, "毘沙門堂本系に伝わる古今集注釈の細部。"),
            ("俊頼髄脳病歌論", "Illness-poem poetics in Toshiyori zuino", "俊頼髄脳病歌論", p_chusei, "俊頼髄脳で病を詠む歌の可否を論じる箇所。"),
            ("袋草紙歌合判詞引用", "Utaawase verdict citations in Fukurozoshi", "袋草紙判詞引用", p_chusei, "袋草紙が歌合判詞を根拠として引用する方法。"),
            ("無名抄俊成逸話", "Shunzei anecdotes in Mumyo sho", "無名抄俊成逸話", p_chusei, "鴨長明が俊成像を伝える歌論的逸話群。"),
            ("連歌新式賦物規定", "Fushimono rules in renga shiki", "連歌新式賦物", p_chusei, "連歌式目で賦物の扱いを細かく定める規定。"),
            ("禅竹六輪一露観照語", "Contemplative terms in Rokurin ichiro", "六輪一露観照語", p_chusei, "禅竹能楽論で境地を示す観照的用語群。"),
            # Cluster 5: 近世版本・俳諧・戯作の局所技法
            ("俳諧七部集猿蓑切字配置", "Kireji placement in Sarumino", "猿蓑切字配置", p_kinsei, "猿蓑発句で切字が景の転換を作る配置法。"),
            ("芭蕉紀行文発句前後文", "Prose around hokku in Basho travelogues", "芭蕉紀行発句前後文", p_kinsei, "紀行文で発句の前後に置かれる散文の機能。"),
            ("西鶴本挿絵本文対応", "Text-image coupling in Saikaku editions", "西鶴本挿絵対応", p_kinsei, "西鶴版本で挿絵と本文が笑いを補強する関係。"),
            ("洒落本会話の地口連鎖", "Pun chains in sharebon dialogue", "洒落本地口連鎖", p_kinsei, "洒落本会話で地口が連続し人物造形を作る技法。"),
            ("黄表紙見返し広告文", "Front-matter ads in kibyoshi", "黄表紙見返し広告", p_kinsei, "黄表紙の見返しに置かれる宣伝的な版元文句。"),
            ("読本章回末評語", "End-of-chapter comments in yomihon", "読本章回末評語", p_kinsei, "読本の章回末に置かれる評語風の締め句。"),
        ]

        if len(concepts) != 30:
            raise RuntimeError("expected 30 concepts")

        inserted = 0
        for name_ja, name_en, name_original, period, definition in concepts:
            if len(definition) > 100:
                raise RuntimeError(f"definition too long: {name_ja}")
            before = db.find_concept(name_ja, REGION, period)
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script="kanji",
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None:
                inserted += 1

        print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
