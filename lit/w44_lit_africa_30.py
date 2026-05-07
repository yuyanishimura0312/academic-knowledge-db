from lit_db_helper import LitDB


CONCEPTS = [
    # 1. Sahara/Sahel manuscript micro-genres
    ("ティンブクトゥ蔵書票ワクフ詩", "Manuscript donor poems in Timbuktu waqf libraries.", 61),
    ("アガデス隊商余白歌", "Marginal caravan songs in Agadez manuscript notebooks.", 61),
    ("フータ・トロ女性アジャミ哀歌", "Pulaar Ajami elegies attributed to women in Futa Toro.", 61),
    ("タマシェク革袋写本恋歌", "Tuareg love poems preserved in leather satchel manuscripts.", 61),
    ("ハウサ市場価格クロニクル詩", "Hausa verse notes tying market prices to moral memory.", 61),
    ("カネム宮廷系譜カスィーダ", "Kanem court qasidas embedding dynastic genealogy.", 61),

    # 2. Coastal and island performance texts
    ("ラム島ウテンジ競作会", "Lamu Swahili utenzi contests judged by local reciters.", 61),
    ("ペンバ島マウリディ返歌", "Pemba mawlid response poems between rival devotional groups.", 61),
    ("マヨット・シマオレ出産祝歌", "Shimaore birth songs with improvised maternal praise.", 61),
    ("セーシェル・クレオール葬送ラメント", "Seychellois Creole laments circulated after funerals.", 61),
    ("ロドリゲス島セガ物語歌", "Rodriguan sega lyrics carrying serialized island narratives.", 61),
    ("リユニオン奴隷逃亡マロヤ詞", "Maloya lyrics remembering maroon flight on Reunion.", 61),

    # 3. Print, pamphlet, and newspaper niches
    ("ヨルバ語薬売りパンフ劇", "Yoruba medicine-seller pamphlet plays for market stalls.", 61),
    ("アサンテ葬儀プログラム詩", "Akan funeral-program poems printed for lineage rites.", 61),
    ("エウェ語裁判傍聴小説欄", "Ewe newspaper fiction shaped by courtroom spectatorship.", 61),
    ("ルオ語学校雑誌幽霊譚", "Luo school-magazine ghost tales from mission presses.", 61),
    ("ショナ語協同組合ニュース詩", "Shona cooperative newsletter poems on rural labor.", 150),
    ("ツワナ語鉄道時刻表風刺", "Tswana satires printed around railway timetable routines.", 61),

    # 4. Postwar radio, cassette, and stage circuits
    ("ラジオ・ベナン寓話朗読台本", "Radio Benin scripts adapting animal fables for broadcast.", 150),
    ("カンパラ婚礼カセット詩", "Kampala wedding cassette poems exchanged by families.", 150),
    ("ダルエスサラーム路上劇ビラ", "Dar street-theatre leaflets announcing improvised plays.", 150),
    ("ルサカ鉱山労働者ラジオ劇", "Zambian miner radio dramas about compound life.", 150),
    ("ブラザヴィル酒場朗読サークル", "Brazzaville barroom reading circles for unpublished prose.", 150),
    ("ビサウ独立後クレオール寸劇", "Post-independence Bissau Creole skits in civic campaigns.", 152),

    # 5. Digital and diaspora micro-circulation
    ("アスマラ離散Telegram詩", "Diasporic Tigrinya poems forwarded through Telegram groups.", 150),
    ("ダカールTikTokグリオ短詩", "Short griot praise verses adapted to Dakar TikTok clips.", 150),
    ("ヨハネスブルグSpoken Word字幕詩", "Subtitled Joburg spoken-word poems for online circulation.", 150),
    ("カサブランカWhatsAppハイク", "Darija haiku-like poems shared in Casablanca chats.", 150),
    ("ルアンダInstagramキンブンドゥ詩", "Kimbundu micro-poems posted by Luanda Instagram writers.", 152),
    ("ミネアポリス・ソマリSnap詩", "Somali diaspora snap poems circulating from Minneapolis.", 150),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, definition, period_id in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                subfield_code="lit_africa",
                region="グローバルサウス",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
