from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_arabic", region="南西アジア")

CONCEPTS = [
    # 1. ジャーヒリーヤ詩のミクロ技法
    dict(**C, period_id=16, name_ja="ラヒール部の雌ラクダ疲弊比喩",
         name_en="rahil she-camel exhaustion simile",
         name_original="تشبيه ناقة الرحيل", definition="旅立ち部で雌ラクダの疲弊を誇張する定型比喩。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=16, name_ja="アトラール涙痕の双数表現",
         name_en="dual wording of tears at the atlal",
         name_original="دموع الأطلال المثناة", definition="廃墟詠で二人の涙や眼を双数で反復する語法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=16, name_ja="ザイフ迎接の夜火モチーフ",
         name_en="guest-welcoming night fire motif",
         name_original="نار الضيف", definition="客を招く夜火を寛大さの証として詠む遊牧詩モチーフ。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=16, name_ja="ワフシュ狩猟譚の追跡連鎖",
         name_en="wild-game chase sequence in qasida",
         name_original="طرد الوحش", definition="野驢馬や羚羊の追跡を連鎖的に描くカスィーダ挿話。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=16, name_ja="カウム恥辱喚起のヒジャー定型",
         name_en="tribal shame provocation in hija",
         name_original="تعيير القوم", definition="敵部族の臆病や出自を列挙して辱める諷刺詩定型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=16, name_ja="アヤーム・アル＝アラブ詩挿入",
         name_en="Ayyam al-Arab poetic insertions",
         name_original="أشعار أيام العرب", definition="部族戦記の語りに挿入される戦場詩句の伝承層。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),

    # 2. 初期イスラーム・ウマイヤ朝のジャンル細部
    dict(**C, period_id=17, name_ja="クッサース説教の逸話詩引用",
         name_en="poetic citations in qussas preaching",
         name_original="استشهاد القصاص بالشعر", definition="説教師が教訓逸話へ古詩を挟む初期都市説教技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=17, name_ja="マウラ詩人の系譜自称",
         name_en="mawla poets' lineage self-fashioning",
         name_original="نسب شعراء الموالي", definition="被保護民詩人が部族帰属を詩中で演出する語り。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=17, name_ja="ウズリー恋愛詩の秘名戦略",
         name_en="secret naming in Udhri love poetry",
         name_original="الكناية في الغزل العذري", definition="恋人名を隠し部族規範と情熱を両立させる詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=17, name_ja="ヒジャーズ都市ガザルの巡礼場面",
         name_en="pilgrimage scenes in Hijazi urban ghazal",
         name_original="مشاهد الحج في الغزل الحجازي", definition="巡礼路や聖域での邂逅を恋愛詩へ転用する場面型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=17, name_ja="ナカーイドの系譜罵倒カタログ",
         name_en="genealogical insult catalogues in naqaid",
         name_original="هجاء الأنساب في النقائض", definition="応酬諷刺詩で相手氏族の祖先欠陥を列挙する技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=17, name_ja="預言者称揚詩のバルダ転位",
         name_en="burda transfer in prophetic praise",
         name_original="انتقال البردة في المديح النبوي", definition="外套授与逸話を称揚詩の権威づけに用いる伝承。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 3. アッバース朝アダブと書記文化
    dict(**C, period_id=18, name_ja="タルセル書簡の連鎖サジウ",
         name_en="chain saj in tarsil epistles",
         name_original="سجع الترسل المتسلسل", definition="公用書簡で短句押韻を連結する書記的散文技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=18, name_ja="ハマースィーヤート詞華集配列",
         name_en="arrangement of hamasiyyat anthologies",
         name_original="ترتيب الحماسيات", definition="勇壮詩句を徳目別に並べるアッバース期詞華集法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=18, name_ja="ムジュン酒宴詩の道化語り",
         name_en="buffoon narration in mujun drinking poems",
         name_original="نوادر المجون والخمر", definition="酒宴詩で道化や寄生客の声を混ぜる逸脱的語り。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=18, name_ja="カーティブ試験の即興書簡",
         name_en="improvised epistles in katib tests",
         name_original="ارتجال الكاتب", definition="書記候補の教養を測る即興書簡作成の逸話群。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=18, name_ja="ブハラー逸話の食卓倹約型",
         name_en="table-frugality type in Bukhala anecdotes",
         name_original="بخل المائدة", definition="吝嗇者譚で食卓の分配拒否を笑いへ変える型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=18, name_ja="ムファーハラ動植物対論",
         name_en="animal-plant boasting disputation",
         name_original="مفاخرة الحيوان والنبات", definition="動物や植物が優劣を競うアダブ的擬人対論。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 4. アンダルス・マグリブの局地詩学
    dict(**C, period_id=139, name_ja="ハルジャの女性声仮構",
         name_en="female voice fiction in kharja",
         name_original="صوت المرأة في الخرجة", definition="ムワッシャハ終句で女性恋歌の声を仮構する技法。",
         importance_score=3, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=139, name_ja="バルバル語混淆ザジャル断章",
         name_en="Berber-mixed zajal fragments",
         name_original="زجل ممزوج بالبربرية", definition="マグリブ口語詩にベルベル語句が混じる断片伝承。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=139, name_ja="リヤード庭園詩の水路描写",
         name_en="water-channel description in garden poems",
         name_original="وصف السواقي في الرياض", definition="アンダルス庭園詩で水路や噴水を精密に描く小詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=139, name_ja="ムルーク・アッタワーイフ宮廷即興",
         name_en="Taifa court improvisation",
         name_original="ارتجال ملوك الطوائف", definition="タイファ諸王宮廷で交わされた即興詩応酬の逸話。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=139, name_ja="シチリア亡命詩の島影記憶",
         name_en="island-memory in Sicilian exile poetry",
         name_original="حنين صقلية", definition="失われたシチリアを島影や海景で想起する亡命詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=139, name_ja="アンダルス・ナウバ歌詞伝承",
         name_en="Andalusi nuba lyric transmission",
         name_original="نصوص النوبة الأندلسية", definition="ナウバ組曲に保存されたムワッシャハ歌詞の口伝層。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 5. 近現代アラブ文学の細分潮流
    dict(**C, period_id=20, name_ja="マハジャル小雑誌の散文詩実験",
         name_en="prose-poem experiments in Mahjar little magazines",
         name_original="قصيدة النثر المهجرية", definition="移民系小雑誌で試みられた短い散文詩の初期形。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=20, name_ja="ナフダ学校劇の教訓合唱",
         name_en="moral chorus in Nahda school drama",
         name_original="الجوقة في المسرح المدرسي", definition="学校劇で生徒合唱が近代的教訓を唱える演出法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=21, name_ja="パレスチナ獄中小説の密書構造",
         name_en="secret-letter structure in Palestinian prison novels",
         name_original="بنية الرسائل السرية", definition="獄中の検閲回避を密書形式で物語化する小説技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=21, name_ja="イラク亡命詩の河川反転像",
         name_en="inverted river imagery in Iraqi exile poetry",
         name_original="صورة النهر في شعر المنفى", definition="チグリスやユーフラテスを喪失と帰還不能へ反転する詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=21, name_ja="ベイルート内戦小説の階段空間",
         name_en="stairwell space in Beirut civil-war novels",
         name_original="فضاء الدرج في رواية الحرب", definition="集合住宅の階段を狙撃や避難の境界として描く技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, period_id=21, name_ja="湾岸石油小説の仮設労働宿舎",
         name_en="labor-camp space in Gulf oil novels",
         name_original="معسكر العمال في رواية النفط", definition="石油開発下の労働宿舎を疎外の舞台にする小説空間。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
            db.insert_concept(**concept)
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=13"
        ).fetchone()[0]
    print(f"inserted={after - before}")


if __name__ == "__main__":
    main()
