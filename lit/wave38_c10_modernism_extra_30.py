#!/usr/bin/env python3
"""Wave 38 C10: add 30 deep niche concepts to lit_eu_modernism."""

from lit_db_helper import LitDB

SUBFIELD_CODE = "lit_eu_modernism"
REGION = "西欧"

P_MOD = 22
P_LATE = 23
P_VIENNA = 233
P_BRIT_EDGE = 234

# 5 thematic clusters x 6 concepts.
# (name_ja, name_en, name_original, original_script, period_id, definition)
CONCEPTS = [
    # 1. Small magazines and publishing micro-scenes
    ("『エゴイスト』編集圏", "The Egoist circle", "The Egoist", "roman", P_BRIT_EDGE,
     "英モダニズムの連載、評論、女性編集を結ぶ小雑誌ネットワーク。"),
    ("『トランジション』多言語実験", "transition multilingual experiment", "transition", "roman", P_MOD,
     "ジョイス周辺の亡命雑誌が複数言語と活字実験を混交した場。"),
    ("『デル・シュトゥルム』詩画面", "Der Sturm page-poetics", "Der Sturm", "roman", P_MOD,
     "表現主義雑誌の紙面で詩、木版、宣言が衝突する構成法。"),
    ("『ノイエ・ルントシャウ』モダン", "Neue Rundschau modernism", "Die neue Rundschau", "roman", P_MOD,
     "ドイツ語圏の新文学を批評と翻訳で媒介した雑誌的モダン。"),
    ("『メルキュール・ド・フランス』象徴派残響", "Mercure de France after-symbolism", "Mercure de France", "roman", P_MOD,
     "象徴派後の批評圏が前衛と古典趣味を同居させた媒体。"),
    ("ホガース・プレス短冊本", "Hogarth Press pamphlet modernism", "Hogarth Press", "roman", P_BRIT_EDGE,
     "私家出版の小冊子が実験散文と批評を軽量に流通させた形式。"),

    # 2. Regional and language-edge avant-gardes
    ("スペイン・ウルトライスモ", "Spanish Ultraismo", "Ultraismo", "roman", P_MOD,
     "隠喩、速度、都市感覚を掲げたスペイン語前衛詩運動。"),
    ("クレアシオニスモ詩学", "Creationist poetics", "Creacionismo", "roman", P_MOD,
     "詩を自然模倣でなく自律的創造物とみなす前衛詩論。"),
    ("カタルーニャ前衛詩", "Catalan avant-garde poetry", "avantguarda catalana", "roman", P_MOD,
     "サルバト＝パパセイト周辺の都市、機械、海港詩の流れ。"),
    ("フィンランド・スウェーデン語モダニズム", "Finland-Swedish modernism", "finlandssvensk modernism", "roman", P_MOD,
     "セーデルグラン以後の北欧少数語による象徴主義後の詩革新。"),
    ("トゥレンカンタヤット世代", "Tulenkantajat generation", "Tulenkantajat", "roman", P_MOD,
     "1920年代フィンランドの都市性と国際主義を掲げた若い詩人群。"),
    ("デンマーク『ヘレティカ』圏", "Heretica circle", "Heretica", "roman", P_LATE,
     "戦後デンマークで実存、神話、宗教的モダニズムを論じた雑誌圏。"),

    # 3. Lesser-used prose lines
    ("リチャードソン『遍歴』時間", "Richardson Pilgrimage time", "Pilgrimage", "roman", P_BRIT_EDGE,
     "女性意識の微細な持続を長大連作で追う時間表現。"),
    ("メイ・シンクレア心理小説", "May Sinclair psychological novel", "May Sinclair", "roman", P_BRIT_EDGE,
     "内面分析と女性自立を結び意識の流れを理論化した小説系譜。"),
    ("ホープ・ミルリーズ『パリ』", "Hope Mirrlees Paris", "Paris: A Poem", "roman", P_MOD,
     "都市散歩、広告、音声を一日の詩面に重ねる長詩実験。"),
    ("ロナルド・ファーバンクの装飾会話", "Ronald Firbank ornate dialogue", "Ronald Firbank", "roman", P_MOD,
     "断片的会話とキャンプな装飾で物語を空洞化する散文技法。"),
    ("ローベルト・ヴァルザー小散文", "Robert Walser microscript prose", "Mikrogramme", "roman", P_MOD,
     "歩行、事務、縮小文字で近代主体を小さくずらす短散文。"),
    ("アルフレート・クービン『裏面』", "Alfred Kubin The Other Side", "Die andere Seite", "roman", P_VIENNA,
     "夢幻都市と崩壊する帝国感覚を幻想小説に折り込む作品。"),

    # 4. Vienna, Prague, and Central European minor forms
    ("カフェハウス・フェイユトン", "coffeehouse feuilleton", "Kaffeehaus-Feuilleton", "roman", P_VIENNA,
     "新聞小品が都市観察、風刺、会話知を圧縮する短文形式。"),
    ("チャンドス危機以後", "post-Chandos language crisis", "Chandos-Krise", "roman", P_VIENNA,
     "言語不信を沈黙、断章、事物凝視へ展開するドイツ語圏の問題系。"),
    ("プラハ・ドイツ語小説圏", "Prague German prose circle", "Prager deutsche Literatur", "roman", P_MOD,
     "多言語都市プラハの官僚制、不安、少数性を映す散文圏。"),
    ("カール・クラウス引用モンタージュ", "Karl Kraus quotation montage", "Zitatmontage", "roman", P_VIENNA,
     "新聞語の引用を再配置しメディア暴力を暴く風刺技法。"),
    ("ムイノナのグロテスク", "Mynona grotesque", "Mynona", "roman", P_MOD,
     "哲学的逆説と奇怪な身体変形で市民的常識を崩す短編様式。"),
    ("カネッティ『眩暈』群衆知", "Canetti Auto-da-Fe crowd knowledge", "Die Blendung", "roman", P_MOD,
     "蔵書狂と群衆心理を結び知識人の孤立を戯画化する小説。"),

    # 5. Formal devices below the canonical labels
    ("テレグラム文体", "telegram style", "Telegrammstil", "roman", P_MOD,
     "省略、名詞句、急速な切断で近代通信の速度を写す文体。"),
    ("目録都市詩", "catalogue city poem", "catalogue city poem", "roman", P_MOD,
     "看板、通り、商品名の列挙で都市経験を構成する詩形式。"),
    ("音声タイポグラフィ", "phonetic typography", "phonetic typography", "roman", P_MOD,
     "発音、叫び、雑音を活字配置で視覚化する前衛的表記法。"),
    ("映画的ワイプ叙述", "cinematic wipe narration", "cinematic wipe", "roman", P_MOD,
     "場面転換を映画のワイプのように滑らせる散文の切替技法。"),
    ("人称スリップ", "pronominal slippage", "pronominal slippage", "roman", P_MOD,
     "一人称、二人称、三人称が揺れ主体境界を不安定化する語り。"),
    ("注釈化された断章", "annotated fragment", "annotated fragment", "roman", P_LATE,
     "断章本文に脚注や自己注釈を重ね完成不能性を示す形式。"),
]


def main() -> None:
    inserted = 0
    with LitDB() as db:
        for name_ja, name_en, name_original, script, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, f"{name_ja}: definition too long"
            before = db.find_concept(name_ja, REGION, period_id)
            cid = db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                name_original=name_original,
                original_script=script,
                subfield_code=SUBFIELD_CODE,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=3,
                source_tier="secondary",
                canonical_in_region="minor",
            )
            if before is None and cid:
                inserted += 1
        total = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=6"
        ).fetchone()[0]
    print(f"inserted={inserted} total={total}")


if __name__ == "__main__":
    main()
