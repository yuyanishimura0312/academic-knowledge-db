from __future__ import annotations

from lit_db_helper import LitDB


C = dict(subfield_code="lit_theory", region="理論", period_id=None)

CONCEPTS = [
    # 1. 周縁韻文理論
    dict(**C, name_ja="ウェールズ・キンガネズ異声韻律論",
         name_en="Welsh cynghanedd heterophonic prosody",
         definition="子音照応と内韻を声部差として読むウェールズ詩学。"),
    dict(**C, name_ja="古アイルランド・ディベルガ即興句法",
         name_en="Old Irish diberg improvisational diction",
         definition="襲撃詩語の反復句を即興構成単位とみる微視詩学。"),
    dict(**C, name_ja="コルシカ・パデッラ即興応答論",
         name_en="Corsican padella improvised response theory",
         definition="掛け合い歌の返答遅延と声域交替を読む民衆詩論。"),
    dict(**C, name_ja="サルデーニャ・ムトゥ応酬韻論",
         name_en="Sardinian muttu responsorial rhyme theory",
         definition="即興四行詩の返歌構造と韻の拘束を扱う地方詩学。"),
    dict(**C, name_ja="フリジア頌歌の頭韻残存論",
         name_en="Frisian ode alliterative residue",
         definition="近世フリジア詩に残る古層頭韻を理論化する読解。"),
    dict(**C, name_ja="カレリア・ヨイク叙述声論",
         name_en="Karelian yoik narrative voice theory",
         definition="歌が人物を描写せず呼び出す声の機能を問う口承論。"),

    # 2. 忘れられた批評家・小著作
    dict(**C, name_ja="フアン・ウアルテ才質詩学",
         name_en="Juan Huarte ingenio poetics",
         definition="才質分類を詩作能力へ応用する初期近代スペイン詩論。"),
    dict(**C, name_ja="フラチュ・サレ沈黙読書論",
         name_en="Khachatur Sale silent reading theory",
         definition="アルメニア説教写本に見える沈黙読書の規範化。"),
    dict(**C, name_ja="ディミトリエ・カンテミール韻律分類",
         name_en="Dimitrie Cantemir metric taxonomy",
         definition="モルダヴィア学知が詩歌形式を音楽理論で分類する試み。"),
    dict(**C, name_ja="アントン・ピエタス地方文体論",
         name_en="Anton Pitas provincial style theory",
         definition="地方語散文の粗さを美質とする小規模文体論争。"),
    dict(**C, name_ja="アナスタシウス・グリュン検閲寓意論",
         name_en="Anastasius Grun censorship allegory",
         definition="検閲下の政治詩を寓意の迂回路として読む技法論。"),
    dict(**C, name_ja="ルクレツィア・マリネッラ女性弁護読法",
         name_en="Lucrezia Marinella defense reading",
         definition="女性弁護書を反引用の配置で読む初期近代批評法。"),

    # 3. 写本・校訂ミクロ論
    dict(**C, name_ja="エチオピア写本の句読点解釈論",
         name_en="Ethiopic manuscript punctuation hermeneutics",
         definition="ゲエズ写本の赤点と間隔を読解単位として扱う理論。"),
    dict(**C, name_ja="シリア語セルト欄外異読論",
         name_en="Syriac Serto marginal variant theory",
         definition="セルト体写本の欄外異読を共同注釈の痕跡とみる。"),
    dict(**C, name_ja="ベンガル・プンティ紙葉順序論",
         name_en="Bengali puthi folio order theory",
         definition="紙葉混乱を物語順序の可変性として読む写本論。"),
    dict(**C, name_ja="チベット木版本朱印異同論",
         name_en="Tibetan blockprint seal variation theory",
         definition="朱印・蔵書印の差異から読書共同体を復元する方法。"),
    dict(**C, name_ja="マヤ絵文書折本の継ぎ目読解",
         name_en="Maya codex fold-joint reading",
         definition="折本の継ぎ目を場面転換や暦注釈の手掛かりにする。"),
    dict(**C, name_ja="ジャワ・ロンタル紐穴配列論",
         name_en="Javanese lontar string-hole ordering",
         definition="ロンタル葉の紐穴と欠葉から詩章配列を推定する技法。"),

    # 4. サブジャンル変種の理論化
    dict(**C, name_ja="アルバニア・カンゲ英雄嘆歌型",
         name_en="Albanian kange heroic lament subtype",
         definition="英雄歌と葬送嘆歌が交差する短い口承叙事型。"),
    dict(**C, name_ja="ガリシア・コプラ巡礼諷刺型",
         name_en="Galician copla pilgrimage satire subtype",
         definition="巡礼歌が地方政治の諷刺へ転用される小ジャンル。"),
    dict(**C, name_ja="ベトナム・ハットノイ語り分岐論",
         name_en="Vietnamese hat noi narrative branching",
         definition="歌謡劇の挿話分岐を演者選択として読む形式論。"),
    dict(**C, name_ja="ラオス・ラム詩劇の掛詞場面論",
         name_en="Lao lam poetic drama pun-scene theory",
         definition="掛詞が場面転換を担うラム詩劇の局所構造論。"),
    dict(**C, name_ja="カシミール・ヴァーク短詩連鎖論",
         name_en="Kashmiri vak sequence theory",
         definition="独立短詩を連鎖読解するカシミール詩の配列論。"),
    dict(**C, name_ja="タミル・パッル農民風刺型",
         name_en="Tamil pallu peasant satire subtype",
         definition="農民・地主・妻の声を交差させる風刺歌謡劇の型。"),

    # 5. 理論的ミクロ論争
    dict(**C, name_ja="アラビア詩タブウ盗用閾値論",
         name_en="Arabic tabw plagiarism threshold debate",
         definition="許容模倣と盗用を分ける比喩単位をめぐる細分類論争。"),
    dict(**C, name_ja="サンスクリット・ドーシャ微瑕疵論",
         name_en="Sanskrit dosha minor-fault debate",
         definition="詩的欠点が趣味判断で免責される条件を問う議論。"),
    dict(**C, name_ja="漢文評点の圏点強度論争",
         name_en="Sinitic reading-mark intensity debate",
         definition="圏点や傍点の多寡を批評的価値表示とみるかの論争。"),
    dict(**C, name_ja="ヘブライ・ピユート脚韻逸脱論",
         name_en="Hebrew piyyut rhyme deviation debate",
         definition="脚韻逸脱を失敗か典礼的強調かで読む微小論争。"),
    dict(**C, name_ja="トルコ・ナズィーレ応作距離論",
         name_en="Turkish nazire distance debate",
         definition="応作詩が原詩からどの程度離れてよいかを問う議論。"),
    dict(**C, name_ja="古ノルド・ケニング過密論争",
         name_en="Old Norse kenning density debate",
         definition="ケニングの過密化を技巧か難解化かで評価する論争。"),
]


def main() -> None:
    with LitDB("lit.sqlite") as db:
        before = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=22"
        ).fetchone()[0]
        inserted = 0
        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
            existing = db.find_concept(concept["name_ja"], concept["region"], concept["period_id"])
            cid = db.insert_concept(
                **concept,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="minor",
            )
            if existing is None:
                inserted += 1
            print(cid, concept["name_ja"])
        after = db.conn.execute(
            "SELECT COUNT(*) FROM concepts WHERE subfield_id=22"
        ).fetchone()[0]
        print(f"inserted={inserted} before={before} after={after}")


if __name__ == "__main__":
    main()
