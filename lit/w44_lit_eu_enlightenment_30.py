from lit_db_helper import LitDB


SUBFIELD = "lit_eu_enlightenment"
REGION = "西欧"

P_EARLY = 99
P_HIGH = 100
P_SENS = 101
P_LATE = 102
P_GOTHIC = 292


CONCEPTS = [
    # Cluster 1: clandestine print and bookselling
    dict(name_ja="禁書目録の伏字著者名", name_en="masked author names in banned catalogues", period_id=P_HIGH, definition="禁書目録で著者名を伏字化し探索欲を誘う販売符号。"),
    dict(name_ja="偽ジュネーヴ刊記", name_en="false Geneva imprint", period_id=P_HIGH, definition="検閲回避や権威付けに使われた虚偽のジュネーヴ刊記。"),
    dict(name_ja="港湾本箱の混載目録", name_en="mixed port book-crate inventory", period_id=P_HIGH, definition="密輸本を合法本と混ぜて記す港湾流通の目録技法。"),
    dict(name_ja="禁書読書会の貸出札", name_en="clandestine reading-society loan slips", period_id=P_HIGH, definition="地下読書会で禁書の貸借順を管理した小札の痕跡。"),
    dict(name_ja="押収本の切除表題紙", name_en="excised title pages in seized books", period_id=P_HIGH, definition="押収を恐れ表題紙だけを切り取る禁書所持の防衛策。"),
    dict(name_ja="地下版の価格暗号", name_en="price ciphers in clandestine editions", period_id=P_HIGH, definition="地下出版物の価格を記号で示す書籍商間の暗号慣行。"),
    # Cluster 2: periodicals and reader address
    dict(name_ja="月刊紙の架空地方通信", name_en="fictional provincial letters in monthlies", period_id=P_HIGH, definition="地方読者の声を装い都市世論を広域化する紙面形式。"),
    dict(name_ja="読者訂正欄の徳化演出", name_en="moralized reader correction column", period_id=P_HIGH, definition="誤植訂正を読者の注意深さと徳へ結びつける欄。"),
    dict(name_ja="道徳週刊紙の迷子寓話", name_en="lost-child allegory in moral weeklies", period_id=P_EARLY, definition="迷子譚で都市誘惑と家庭徳を説く短い寓話形式。"),
    dict(name_ja="婦人雑誌の匿名助言者", name_en="anonymous adviser in women's magazines", period_id=P_HIGH, definition="匿名助言者が恋愛・読書・家政を裁く雑誌上の声。"),
    dict(name_ja="紙上サロンの席次比喩", name_en="seating metaphors in print salons", period_id=P_HIGH, definition="紙面参加者をサロン席次に見立てる読者配置法。"),
    dict(name_ja="懸賞エッセイの年齢署名", name_en="age signatures in prize essays", period_id=P_HIGH, definition="投稿者年齢を署名に添え啓蒙的成長を競わせる形式。"),
    # Cluster 3: theatre, performance, and spectatorship
    dict(name_ja="涙劇のハンカチ所作", name_en="handkerchief gesture in tear drama", period_id=P_SENS, definition="涙を拭う小道具で観客共感を可視化する舞台所作。"),
    dict(name_ja="幕間販売の戯曲梗概", name_en="intermission sale of play synopses", period_id=P_HIGH, definition="幕間に梗概刷物を売り観劇理解と出版を結ぶ慣行。"),
    dict(name_ja="検閲官席への台詞目配せ", name_en="aside toward the censor's seat", period_id=P_HIGH, definition="検閲官の存在を意識した台詞や視線の二重演技。"),
    dict(name_ja="市民悲劇の鍵束小道具", name_en="key-ring prop in bourgeois tragedy", period_id=P_SENS, definition="家政権と監禁を示す鍵束が葛藤を駆動する小道具。"),
    dict(name_ja="喜劇終幕の涙声朗誦", name_en="tearful recitation in comic finales", period_id=P_SENS, definition="喜劇の和解場面を涙声の朗誦で徳化する演出。"),
    dict(name_ja="俳優便覧の役柄索引", name_en="role indexes in actor handbooks", period_id=P_HIGH, definition="俳優名声を役柄別に整理し観劇記憶を商品化する索引。"),
    # Cluster 4: epistolary and sentimental fiction devices
    dict(name_ja="書簡小説の未投函束", name_en="unsent letter bundles in epistolary fiction", period_id=P_SENS, definition="未投函書簡の束で沈黙と感情過多を示す装置。"),
    dict(name_ja="返書写しの筆跡差", name_en="handwriting contrast in copied replies", period_id=P_SENS, definition="写された返書の筆跡差で真正性と介入を示す技法。"),
    dict(name_ja="感傷小説の読後失神", name_en="post-reading fainting in sentimental fiction", period_id=P_SENS, definition="読書後の失神で共感の強度と身体化を描く場面。"),
    dict(name_ja="友情誓約の封蝋色", name_en="sealing-wax color in friendship vows", period_id=P_SENS, definition="封蝋の色で友情・嫉妬・喪を符号化する書簡細部。"),
    dict(name_ja="遺言補遺の徳試験", name_en="codicil virtue test", period_id=P_SENS, definition="遺言補遺で相続者の徳と感情を試す筋立て。"),
    dict(name_ja="女中伝聞の書簡挿入", name_en="maid hearsay inserted in letters", period_id=P_SENS, definition="女中の伝聞を挟み私的書簡の情報網を広げる技法。"),
    # Cluster 5: conjectural, exotic, and pseudo-documentary frames
    dict(name_ja="架空博物誌の分類欄外注", name_en="marginal taxonomy in fictional natural history", period_id=P_HIGH, definition="架空動植物を分類欄外注で実在らしく見せる技法。"),
    dict(name_ja="漂流記の緯度誤差注", name_en="latitude-error notes in castaway tales", period_id=P_HIGH, definition="漂流記に緯度誤差注を置き証言性と疑念を併置する。"),
    dict(name_ja="未開語彙表の風刺配列", name_en="satirical ordering of savage vocabularies", period_id=P_HIGH, definition="架空民族語彙表の配列で欧州価値を逆照射する形式。"),
    dict(name_ja="東洋書簡の暦法ずれ", name_en="calendar dislocation in Oriental letters", period_id=P_HIGH, definition="異暦のずれで欧州時間意識を相対化する書簡技法。"),
    dict(name_ja="月世界地図の白紙領域", name_en="blank zones on lunar maps", period_id=P_EARLY, definition="月世界地図の空白部で知識の限界と投機を示す装置。"),
    dict(name_ja="ゴシック写本の虫損ページ", name_en="worm-eaten pages in Gothic manuscripts", period_id=P_GOTHIC, definition="虫損ページで失われた過去と偽文献性を演出する技法。"),
]


def main() -> None:
    with LitDB() as db:
        inserted = 0
        for concept in CONCEPTS:
            assert len(concept["definition"]) <= 100
            before = db.find_concept(concept["name_ja"], REGION, concept["period_id"])
            db.insert_concept(
                name_ja=concept["name_ja"],
                name_en=concept["name_en"],
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=concept["period_id"],
                definition=concept["definition"],
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            if before is None:
                inserted += 1
        print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
