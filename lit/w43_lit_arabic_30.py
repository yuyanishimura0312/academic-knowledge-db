from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_arabic", region="南西アジア", period_id=None)

CONCEPTS = [
    # 1. 写本パラテクスト
    dict(**C, name_ja="イジャーザ余白の詩的署名",
         name_en="poetic signatures in ijaza margins",
         name_original="توقيعات الإجازة الشعرية", definition="伝授許可の余白に添えられる短詩署名の慣行。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="サマーア記録の聴講詩句",
         name_en="verse in sama hearing notes",
         name_original="أبيات السماع", definition="写本聴講記録に記される場面記念の短詩句。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="タムリク句の所有者韻文化",
         name_en="rhymed ownership notes",
         name_original="تملك مسجوع", definition="蔵書所有を押韻散文や短詩で記す写本文化。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ワクフ印周辺の祈願詩",
         name_en="votive verse around waqf stamps",
         name_original="أدعية الوقف الشعرية", definition="寄進印の周囲に書かれる蔵書保護の祈願詩。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="キラアー注記の発音押韻",
         name_en="rhymed pronunciation glosses",
         name_original="ضبط القراءة المسجوع", definition="朗読発音の注意を押韻句で覚えやすくする注記。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="紙背転用の詩学メモ",
         name_en="verso poetics notes",
         name_original="فوائد عروضية على الظهر", definition="紙背に残る韻律・比喩の学習用断片メモ。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),

    # 2. 地方口語詩・歌謡
    dict(**C, name_ja="ダルブーカ応答の即興ザジャル",
         name_en="darabukka-response zajal",
         name_original="زجل جواب الدربكة", definition="打楽器の合図に応じて詩句を即興する口語詩型。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ヒジャーズ婚礼マジュルール",
         name_en="Hijazi wedding majrur",
         name_original="مجرور الحجاز", definition="婚礼行列で掛け合われるヒジャーズ系舞踊歌。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ホーラン収穫アターバ",
         name_en="Hauran harvest ataba",
         name_original="عتابا الحوران", definition="収穫労働の掛け声から展開するシリア南部四行歌。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ヌビア婚礼サービル歌",
         name_en="Nubian-Arabic sabir songs",
         name_original="أغاني الصابر النوبية", definition="ヌビア系アラビア語婚礼で歌われる応答歌。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ジャウフ隊商ラッジャーズ",
         name_en="Jawf caravan rajaz chants",
         name_original="رجز قوافل الجوف", definition="隊商移動の歩調を整えるラジャズ調の掛け声。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="スワヒリ海岸アラブ系マディーフ",
         name_en="Swahili-coast Arabic madih",
         name_original="مدائح الساحل السواحيلي", definition="東アフリカ海岸共同体に残るアラビア語讃歌。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),

    # 3. 後期古典詩作法
    dict(**C, name_ja="タズミーン半句の権威借用",
         name_en="hemistich borrowing in tadmin",
         name_original="تضمين الشطر", definition="名句半行を埋め込み詩の権威を借りる技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="タフミース導入句の敬意表明",
         name_en="deferential openings in takhmis",
         name_original="استهلال التخميس", definition="五行化応作の冒頭で先行詩人へ敬意を示す型。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ムサンマト折返し句の固定化",
         name_en="fixed refrain in musammat",
         name_original="لازمة المسمط", definition="連節詩で反復句を固定し歌唱性を高める構成。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="タルジーア・バンドの詠嘆転調",
         name_en="exclamatory turn in tarjiband",
         name_original="تحول الترجيع", definition="反復節で嘆息や祈願へ声調を転じる詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="ムアッシャル十行節の縁語連鎖",
         name_en="associative chains in muashshar",
         name_original="ترابط المعشر", definition="十行節ごとに縁語を連鎖させる後期定型詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="バディーイヤ詩の修辞名列挙",
         name_en="rhetorical-term catalogues in badiiyya",
         name_original="مصطلحات البديعية", definition="讃詩内で修辞技法名を順に実演する詩形式。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 4. 近代出版・サロン
    dict(**C, name_ja="ナフダ新聞欄の韻文投書",
         name_en="verse letters in Nahda newspapers",
         name_original="رسائل شعرية صحفية", definition="新聞読者欄へ投稿された時事批評の韻文書簡。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="カイロ文芸サロンの即興タクリード",
         name_en="salon taqlid improvisation",
         name_original="تقليد صالوني مرتجل", definition="サロンで古典詩句を即興模倣する余興的作法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="女性雑誌の仮名詩壇",
         name_en="pseudonymous poetry columns in women's journals",
         name_original="منابر شعرية نسائية مستعارة", definition="女性雑誌で筆名詩人が交わした短詩投稿欄。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="マハジャル同人誌の署名翻訳詩",
         name_en="signed translation-poems in Mahjar journals",
         name_original="قصائد مترجمة موقعة", definition="移民同人誌で翻訳と創作の境界を曖昧にした詩。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="学校読本の愛国ナシード",
         name_en="patriotic nashid in school readers",
         name_original="نشيد وطني مدرسي", definition="近代学校読本に載る暗唱用の短い愛国歌。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="初期ラジオ戯曲の詩的幕間",
         name_en="verse interludes in early radio plays",
         name_original="فواصل شعرية إذاعية", definition="初期放送劇で場面転換を担った短い詩的幕間。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),

    # 5. 現代メディア・越境
    dict(**C, name_ja="難民ブログ小説の断片章",
         name_en="fragment chapters in refugee blog novels",
         name_original="فصول مدونة اللاجئ", definition="移動中の投稿断片を章構造に転じる小説形式。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="検閲回避の母音省略詩",
         name_en="vowel-omission anti-censorship poems",
         name_original="قصائد حذف الحركات", definition="母音記号や綴り崩しで検閲語をずらす詩技法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="WhatsApp哀悼カスィーダ",
         name_en="WhatsApp elegiac qasida",
         name_original="قصيدة رثاء واتساب", definition="訃報共有とともに拡散するスマホ時代の哀悼詩。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="インスタ詩の二言語キャプション",
         name_en="bilingual captions in Instagram poetry",
         name_original="تعليق شعري ثنائي اللغة", definition="画像詩に英語併記を添え読者圏を広げる手法。",
         importance_score=2, source_tier="tertiary", canonical_in_region="minor"),
    dict(**C, name_ja="ディアスポラ朗読会の記憶地図",
         name_en="memory maps in diaspora readings",
         name_original="خرائط الذاكرة في الأمسيات", definition="朗読会で故郷の地名を地図的に連ねる詩法。",
         importance_score=2, source_tier="secondary", canonical_in_region="minor"),
    dict(**C, name_ja="湾岸SF短編の石油後景",
         name_en="post-oil backdrop in Gulf SF stories",
         name_original="خلفية ما بعد النفط", definition="脱石油後の都市環境を短編SFの背景に置く設定。",
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
