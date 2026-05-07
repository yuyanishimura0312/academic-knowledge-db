#!/usr/bin/env python3
"""Wave 38: lit_diaspora (subfield_id=20) extra 30 deep niche concepts."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_diaspora"
REGION = "横断"
PERIOD_ID = 274

CONCEPTS = [
    # 1: bureaucratic refuge and documentation
    ("庇護面接ナラティブ", "asylum interview narrative", "庇護審査の問答形式が記憶と自己呈示を規格化する語り。"),
    ("難民書類詩学", "refugee paperwork poetics", "申請書、ID、通行証を物語装置化するディアスポラ表現。"),
    ("不認定の語り", "refusal narrative", "難民申請却下や証言不信を中心に置く移民文学の語り。"),
    ("仮放免リアリズム", "parole realism", "収容と暫定解放の宙吊り生活を日常リアリズムで描く様式。"),
    ("翻訳された証言者", "translated witness", "通訳を介す証言で声の所有と信用が揺らぐ人物配置。"),
    ("ケースファイル小説", "case-file novel", "移民審査記録や法律文書を章立てに組み込む小説形式。"),
    # 2: labor, care, and remittance
    ("送金メロドラマ", "remittance melodrama", "海外送金が家族愛、負債、罪悪感を駆動する離散物語。"),
    ("ケアチェーン叙事", "care-chain narrative", "移民女性労働が複数家庭の世話を連鎖させる語り。"),
    ("留守宅の声", "left-behind voice", "移住者でなく残された家族の視点から離散を語る形式。"),
    ("出稼ぎ身体詩学", "migrant labor body poetics", "疲労、傷、介護動作に越境労働の記憶を刻む表現。"),
    ("帰還不能の稼ぎ手", "nonreturning breadwinner", "送金責務で帰郷できない稼ぎ手を中心にした人物類型。"),
    ("雇用主の家の小説", "employer-house novel", "住み込み労働者が他者の家庭内部から階級と人種を読む小説。"),
    # 3: minor archives and memory media
    ("スーツケース・アーカイブ", "suitcase archive", "携行品、写真、手紙を移動する家族アーカイブとして扱う技法。"),
    ("留守番電話の亡霊", "answering-machine ghost", "録音音声が不在者や死者の残響として働く離散的装置。"),
    ("レシピ帳の記憶", "recipe-book memory", "料理手順が母語、移住史、親族関係を保存する記憶媒体。"),
    ("送れなかった手紙", "unsent-letter motif", "宛先喪失や検閲により届かない手紙で離散を示すモチーフ。"),
    ("家庭ビデオ証言", "home-video testimony", "私的映像が公的歴史に対抗する証言媒体となる表現。"),
    ("名前変更の索引", "renaming index", "改名、発音矯正、綴り違いを索引的に並べる自己記録技法。"),
    # 4: port, camp, and threshold spaces
    ("空港拘束クロノトープ", "airport detention chronotope", "空港の非場所で時間が停止する越境文学の時空配置。"),
    ("難民キャンプ・ビルドゥング", "camp bildungsroman", "難民キャンプでの成長が教育、暴力、移動待機と絡む教養小説。"),
    ("港湾記憶圏", "port memory zone", "港を到着、追放、密航、交易の記憶が重なる場として描く概念。"),
    ("中継都市の詩学", "transit-city poetics", "最終目的地でない都市が仮住まいの感覚を形成する表現。"),
    ("国境待合室", "border waiting room", "越境前の待機空間を制度的宙吊りの象徴にする場面類型。"),
    ("隔離ホテル小説", "quarantine-hotel novel", "検疫や一時収容ホテルを移動停止の舞台にする小説形式。"),
    # 5: digital and dispersed kinship
    ("WhatsApp親族圏", "WhatsApp kinship sphere", "家族チャットが離散共同体の感情管理と監視を担う構造。"),
    ("ビデオ通話の家郷", "video-call homeland", "画面越しの家族空間が故郷感覚を代替する表現。"),
    ("移民GPS叙述", "migrant GPS narration", "位置情報や地図アプリが移動経路と不安を語る叙述法。"),
    ("デジタル弔問", "digital condolence", "遠隔の葬儀参加や追悼投稿で喪失を処理する離散儀礼。"),
    ("送金アプリの親密圏", "remittance-app intimacy", "送金通知や残高画面が家族関係を可視化する表現。"),
    ("プラットフォーム方言", "platform dialect", "SNSやチャット固有の略語混交が移民共同体語になる現象。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: definition too long"
            before = db.find_concept(name_ja, REGION, PERIOD_ID)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=PERIOD_ID,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if before is None and cid:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=20"
        ).fetchone()[0]
    print(f"inserted={inserted} total={total}")


if __name__ == "__main__":
    main()
