#!/usr/bin/env python3
"""Wave 40: add 30 hyper-niche concepts to lit_persian_turkish."""

from lit_db_helper import LitDB

SUBFIELD = "lit_persian_turkish"
REGION = "南西アジア"

P_EARLY = 250
P_MID = 47
P_LATE = 48
P_OTTOMAN = 49
P_TANZ = 50
P_MODERN = 51
P_PROSE = 141
P_HINDI = 142

CONCEPTS = [
    # Cluster 1: Ghaznavid and early Persian court microtraditions
    ("ウンスリー『ワーミクとアズラー』断片", "Unsuri Vamiq and Adhra fragments", P_EARLY, "ガズナ朝宮廷恋愛叙事詩の散逸部を伝える断片群。"),
    ("ファッルヒー・スィースターニー狩猟カスィーダ", "Farrukhi Sistani hunting qasidas", P_EARLY, "狩猟行幸を速度感ある比喩で飾るガズナ朝頌詩の小系譜。"),
    ("アスジャディー・マルヴァズィー頌詩断片", "Asjadi Marvazi panegyric fragments", P_EARLY, "三詩人逸話で知られるガズナ朝詩人の残存頌詩片。"),
    ("アブールファラジュ・ルーニー頌詩", "Abu'l-Faraj Runi panegyrics", P_EARLY, "ガズナ朝後期の宮廷称賛を凝縮した技巧的カスィーダ群。"),
    ("マスウード・サアド獄中詩ハブスィヤート", "Mas'ud Sa'd habsiyyat", P_EARLY, "投獄経験を宮廷詩語で訴える初期ペルシア獄中詩。"),
    ("ラーム・ショーディー音楽詩人伝承", "Ram Shadi musician-poet tradition", P_EARLY, "音楽家詩人として詩人列伝に残る初期ペルシア詩伝承。"),

    # Cluster 2: Persian prose, adab, and regional chronicles
    ("『ターリーフ・イ・シースターン』地方史", "Tarikh-i Sistan regional chronicle", P_PROSE, "シースターンの王統・地誌・英雄伝承を束ねる地方史書。"),
    ("ラーヴァンディー『心の安息』セルジューク史", "Ravandi Rahat al-sudur", P_PROSE, "セルジューク朝政治記憶を逸話と教訓で編むペルシア語史書。"),
    ("ニザーミー・アルーズィー『四つの談話』詩人論", "Nizami Aruzi Chahar Maqala poetics", P_PROSE, "書記・詩人・占星術師・医師を論じる宮廷職能散文。"),
    ("『バフティヤール・ナーメ』十宰相説話", "Bakhtiyar-nameh ten viziers tales", P_PROSE, "無実の王子を救う遅延型説話を重ねるペルシア枠物語。"),
    ("『ダールーブ・ナーメ』薬物詩学", "Darub-nameh pharmacological poetics", P_PROSE, "薬物知と比喩語彙が交差するペルシア語医薬散文。"),
    ("『ジャワーミウルヒカーヤート』逸話配列", "Jawami al-hikayat anecdote ordering", P_PROSE, "教訓逸話を主題別に大集成するアウフィーの散文百科。"),

    # Cluster 3: Timurid, Safavid, and Indo-Persian scholarly niches
    ("ダウラトシャー『詩人列伝』ティムール朝正典化", "Dawlatshah tazkira canonization", P_LATE, "詩人小伝を王朝秩序へ組み込むティムール朝文学史。"),
    ("ハーン・アルズー『灯火辞典』詩語論", "Khan Arzu Siraj al-lughat", P_HINDI, "インド・ペルシア語彙の正用を論じる詩語辞書学。"),
    ("ウルフィー・シーラーズィー難解カスィーダ", "Urfi Shirazi difficult qasidas", P_HINDI, "濃密な比喩でムガル宮廷詩の難解化を進めた頌詩群。"),
    ("ターリブ・アーモリー旅寓詩", "Talib Amuli travel allegory", P_HINDI, "移動経験を寓意的自己像へ変えるサブク・ヒンディー詩。"),
    ("アーザル『アーテシュカデ』詩人列伝", "Azar Atashkadeh tazkira", P_MODERN, "十八世紀ペルシア詩壇を地域別に整理する詩人列伝。"),
    ("リザー・クリー・ハーン『雄弁家集成』", "Riza Quli Khan Majma al-fusaha", P_MODERN, "カージャール期に古典詩人像を再編する大部詩人列伝。"),

    # Cluster 4: Ottoman manuscript genres and poetic microforms
    ("シェフレングィーズ都市美少年詩", "Ottoman sehrengiz city beloved poems", P_OTTOMAN, "都市の美少年列挙で地誌と恋愛詩を接続するジャンル。"),
    ("ヒリイェ預言者肖像詩", "Ottoman hilye prophetic portrait poetry", P_OTTOMAN, "預言者の身体美を文字で描く信仰的肖像詩。"),
    ("サーキーナーメ酒宴詩", "Ottoman saki-name wine-server poems", P_OTTOMAN, "酌人への呼びかけで酒宴・神秘・宮廷を結ぶ詩型。"),
    ("ガザヴァートナーメ戦役散文", "Ottoman gazavatname campaign prose", P_OTTOMAN, "聖戦と軍功を叙述するオスマン戦役記の散文形式。"),
    ("スルナーメ祝祭写本", "Ottoman surname festival manuscripts", P_OTTOMAN, "皇子割礼や婚礼を絵入りで記録する宮廷祝祭文学。"),
    ("ミュナシャアート書簡範例集", "Ottoman munshaat letter anthologies", P_OTTOMAN, "書記の修辞訓練に使われた公式書簡の範例集。"),

    # Cluster 5: Turkish late Ottoman and republican small movements
    ("セルヴェト・フュヌーン誌詩壇", "Servet-i Funun poetry circle", P_TANZ, "雑誌を拠点に象徴主義的語彙を育てたオスマン末期詩壇。"),
    ("フェジュル・アーティ宣言", "Fecr-i Ati manifesto", P_TANZ, "芸術の個性を掲げた短命な青年文学集団の宣言。"),
    ("ミッリ・エデビヤト言語単純化", "Milli Edebiyat language simplification", P_MODERN, "国民文学運動で口語トルコ語を文体規範へ押し出す方針。"),
    ("イキンジ・イェニ抽象詩", "Ikinci Yeni abstract poetry", P_MODERN, "意味の断裂と私的イメージを重んじる第二新詩の方法。"),
    ("マーヴィ運動社会詩", "Mavi movement social poetry", P_MODERN, "ガリプ後の詩に社会性と若い反抗を求めた雑誌派運動。"),
    ("ヒサール派伝統主義詩", "Hisar group traditionalist poetry", P_MODERN, "共和制期に古典韻律と国民的抒情の継承を掲げた詩派。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    inserted = 0
    skipped = 0
    with LitDB("lit.sqlite") as db:
        existing = {
            row["name_ja"]
            for row in db.conn.execute("SELECT name_ja FROM concepts")
        }
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: {len(definition)}"
            if name_ja in existing:
                skipped += 1
                print(f"[skip-name] {name_ja}")
                continue
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="secondary",
                canonical_in_region="marginal",
            )
            inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) AS c FROM concepts WHERE subfield_id = 14"
        ).fetchone()["c"]
    print(f"Inserted: {inserted}, Skipped: {skipped}, Subfield 14 total: {total}")


if __name__ == "__main__":
    main()
