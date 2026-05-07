from lit_db_helper import LitDB


MEIJI = 192
TAISHO = 193
SHOWA_PREWAR = 194
POSTWAR = 195
CONTEMPORARY = 196


CONCEPTS = [
    # 明治印刷・投稿圏
    ("新聞懸賞小説の落選評", "Rejected-entry notes in newspaper fiction contests", MEIJI, "落選作への短評が読者作者を訓練する新聞文芸欄。"),
    ("円本月報の読者近況欄", "Readers' columns in enpon inserts", MEIJI, "円本付録月報で読者層と全集消費を可視化する欄。"),
    ("婦人雑誌小説の読者相談接続", "Advice-column links in women's magazine fiction", MEIJI, "小説と相談欄が家庭倫理を相互補強する誌面構成。"),
    ("文芸誌目次の特集語反復", "Repeated keywords in literary magazine contents", MEIJI, "目次上の特集語反復が流派や問題圏を先取りする装置。"),
    ("駅売り小説誌の表紙惹句", "Cover teasers on station-sold fiction magazines", MEIJI, "駅売り雑誌の短い煽り文が通勤読書を誘導する形式。"),
    ("少年雑誌冒険小説の地図口絵", "Map frontispieces in boys' adventure fiction", MEIJI, "冒険小説冒頭の地図口絵が移動経路を物語化する技法。"),
    # 大正都市メディア
    ("新劇雑誌の上演台本抜粋", "Excerpted scripts in shingeki magazines", TAISHO, "新劇雑誌で戯曲断片が上演記憶を補う掲載慣行。"),
    ("カフェー女給小説の注文符牒", "Cafe waitress fiction order codes", TAISHO, "注文符牒や勘定語で女給労働を示す都市小説細部。"),
    ("探偵小説誌の読者犯人当て", "Culprit-guessing pages in detective magazines", TAISHO, "読者の推理投稿が探偵小説の遊戯性を拡張する欄。"),
    ("モダン都市小説の電車広告引用", "Streetcar ad quotations in modern city fiction", TAISHO, "電車内広告の引用で都市消費と視線を組み込む叙述。"),
    ("映画説明者文体の小説化", "Benshi narration style in fiction", TAISHO, "活動弁士風の語りを小説文体へ移すメディア混淆。"),
    ("百貨店機関誌の季節小説", "Seasonal fiction in department-store house magazines", TAISHO, "百貨店機関誌で催事と消費季節を結ぶ短篇小説。"),
    # 戦時統制と生活表記
    ("防空読本童話の灯火管制語彙", "Blackout vocabulary in air-defense readers", SHOWA_PREWAR, "防空読本童話で灯火管制語が生活規律を教える表現。"),
    ("満洲移民日記小説の天候欄", "Weather columns in Manchurian settler diary fiction", SHOWA_PREWAR, "開拓日記体で天候欄が労働と忍耐を正当化する形式。"),
    ("南方雑誌の現地語カタカナ注", "Katakana glosses in South Seas magazines", SHOWA_PREWAR, "南方誌面で現地語を片仮名注にして支配知へ変える技法。"),
    ("国民学校文集の勤労動員詩", "Labor-mobilization poems in national-school anthologies", SHOWA_PREWAR, "児童文集で勤労動員を詩語化する戦時教育表現。"),
    ("戦時紙芝居脚本の掛声反復", "Call repetitions in wartime kamishibai scripts", SHOWA_PREWAR, "紙芝居脚本の掛声反復が集団応答を促す宣伝形式。"),
    ("配給所場面の順番札描写", "Queue-ticket scenes in ration-shop fiction", SHOWA_PREWAR, "順番札や配給券で銃後の日常秩序を示す小説細部。"),
    # 戦後ローカル紙誌
    ("闇市小説の値段列挙", "Price lists in black-market fiction", POSTWAR, "闇市商品の値段列挙で敗戦直後の生活感覚を刻む叙述。"),
    ("復員手記の部隊番号伏字", "Masked unit numbers in demobilization memoirs", POSTWAR, "復員手記で部隊番号伏字が検閲と記憶の境界を示す。"),
    ("占領期ラジオドラマ脚本掲載", "Published radio-drama scripts under occupation", POSTWAR, "雑誌掲載脚本が放送と活字受容を接続する占領期形式。"),
    ("原爆詩集の献辞連鎖", "Dedication chains in atomic-bomb poetry books", POSTWAR, "献辞の連鎖で死者名と共同追悼を編む原爆詩集慣行。"),
    ("引揚港新聞の投稿短歌", "Tanka submissions in repatriation-port newspapers", POSTWAR, "引揚港新聞の投稿短歌が帰還者の一時共同体を作る。"),
    ("労働者文庫の読後会記録", "Reading-circle records in workers' paperbacks", POSTWAR, "労働者文庫の読後会記録が集団読書を資料化する欄。"),
    # 現代小流通・電子媒体
    ("コピー誌小説のホチキス装丁", "Stapled binding in photocopied fiction zines", CONTEMPORARY, "ホチキス装丁が少部数コピー誌の手作業性を示す物質性。"),
    ("テレクラ小説の会話ログ体", "Telephone-club fiction log style", CONTEMPORARY, "会話ログ形式で匿名通話の欲望と断絶を写す文体。"),
    ("メールマガジン連載小説", "Serial fiction in email newsletters", CONTEMPORARY, "配信時刻と返信欄が連載読書を作るメール媒体小説。"),
    ("匿名掲示板小説のID連鎖", "ID chains in anonymous-board fiction", CONTEMPORARY, "投稿IDの連鎖で作者性と群衆語りを揺らす形式。"),
    ("震災文学フリペの配布地図", "Distribution maps in disaster-literature free papers", CONTEMPORARY, "配布地図が震災後の地域読書圏を可視化する紙面。"),
    ("電子雑誌増刊の対談小説化", "Fictionalized dialogues in digital magazine extras", CONTEMPORARY, "電子増刊の対談体が批評と小説の境界を曖昧にする形式。"),
]


def main() -> None:
    assert len(CONCEPTS) == 30
    with LitDB("lit.sqlite") as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            assert len(definition) <= 100, name_ja
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_jp_modern",
                region="日本",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
