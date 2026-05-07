from lit_db_helper import LitDB


SUBFIELD = "lit_eu_realism"
REGION = "西欧"


CONCEPTS = [
    # 1. French provincial and small-press realism
    ("ラーメ『ラ・メゾン・デュ・シャ』", "Champfleury's cat-house satire", 120,
     "シャンフルーリの猫屋敷諷刺にみる室内リアリズムの極小例。"),
    ("デュランティ『ル・マルール・ダンリエット・ジェラール』", "Duranty's Henriette Gerard", 120,
     "デュランティの失敗家庭譚にみる反ロマン主義的家庭細部。"),
    ("ポール・アレクシ『マダム・ムーリ』", "Paul Alexis's Madame Meuriot", 120,
     "ゾラ周辺作家アレクシの寡婦表象を読む小自然主義作品。"),
    ("レオン・エニック『デヴエ』", "Leon Hennique's Devouee", 120,
     "メダン派エニックの献身女性像をめぐる短い自然主義実験。"),
    ("ユイスマンス『マルト』娼婦自然主義", "Huysmans's Marthe", 120,
     "ユイスマンス初期の娼婦描写にある反叙情的自然主義。"),
    ("第三共和政地方役人小説", "Third Republic provincial bureaucracy fiction", 120,
     "第三共和政期の地方役所を扱う忘却された行政リアリズム。"),
    # 2. British and Irish sub-regional realism
    ("キムリック・リアリズム短編", "Cymric realist short fiction", 121,
     "英語圏ウェールズ地方短編に残る炭鉱・礼拝堂の日常描写。"),
    ("ヴィクトリア朝牧師館扶養小説", "Victorian parsonage dependency fiction", 121,
     "牧師館内の扶養・相続を追う非正典ヴィクトリア朝家庭小説。"),
    ("リチャード・ジェフリーズ田園貧困記", "Richard Jefferies rural poverty", 121,
     "ジェフリーズ散文に出る農村労働者の物質的困窮描写。"),
    ("アイルランド地主屋敷リアリズム断片", "Irish Big House realist fragments", 121,
     "ビッグハウス没落を日常財政から描く小説断片群。"),
    ("スコットランド・キルヤード前史", "pre-Kailyard realism", 121,
     "キルヤード美化以前の村落貧困と宗派摩擦の写実。"),
    ("ヴィクトリア朝女中自伝風小説", "Victorian servant-girl pseudo-autobiography", 121,
     "センセーション小説周縁の家政労働を自然主義的に読む視角。"),
    # 3. Germanophone and Alpine minor realism
    ("ドロステ＝ヒュルスホフ『ユダヤ人のブナ』写本伝承", "Judenbuche manuscript tradition", 121,
     "『ユダヤ人のブナ』の口承・写本的素材化を問う小領域。"),
    ("オットー・ルートヴィヒ『森と荒野のあいだ』", "Otto Ludwig's Zwischen Himmel und Erde", 121,
     "ルートヴィヒの職人家庭悲劇における心理写実の縮図。"),
    ("ポルディ・ウィーン女中小説", "Poldi Viennese maid fiction", 121,
     "世紀末ウィーン下層女性奉公人を扱う忘却小説群。"),
    ("アルプス村落ノヴェレの土地台帳性", "Alpine novella cadastral realism", 121,
     "土地境界・登記・相続が筋を動かすアルプス村落ノヴェレ。"),
    ("低地ドイツ語リアリズム小説", "Low German realist fiction", 121,
     "標準ドイツ語外の方言で農村生活を写した小説伝統。"),
    ("ザール『インノツェンス』宮廷残滓", "Saar's Innocens court residue", 121,
     "ザール短編に残る宮廷秩序と市民写実の衝突。"),
    # 4. Iberian and Lusophone marginal naturalisms
    ("カタルーニャ農村自然主義小説", "Catalan rural naturalist novel", 121,
     "オレール周辺のカタルーニャ農村を生理・財産から読む潮流。"),
    ("ガリシア語コストゥンブリスモ写実", "Galician costumbrista realism", 121,
     "地方習俗記述が階層観察へ転じるガリシア語散文。"),
    ("ポルトガル小市民フィユトン", "Portuguese petty-bourgeois feuilleton", 121,
     "リスボン小市民生活を新聞連載形式で刻む写実小説群。"),
    ("マリア・アマリア・ヴァス『田園の女たち』", "Maria Amalia Vaz's rural women", 121,
     "女性編集者ヴァスの農村女性表象をめぐる周縁的写実。"),
    ("アンダルシア鉱山自然主義", "Andalusian mining naturalism", 121,
     "鉱山労働・疾病・会社支配を扱うスペイン自然主義の小系。"),
    ("ポルト・ボヘミア小説", "Porto bohemian fiction", 121,
     "ポルト文壇の貧困芸術家を描く短命な都市写実サブジャンル。"),
    # 5. Nordic, Dutch, and manuscript micro-debates
    ("デンマーク郷土司祭リアリズム", "Danish parish realism", 121,
     "地方牧師の家計・信仰・村政を描くデンマーク写実小説群。"),
    ("ノルウェー漁村自然主義", "Norwegian fishing-village naturalism", 121,
     "漁村の借財・嵐・身体労働を扱う北欧自然主義の小型系譜。"),
    ("スウェーデン女教師小説", "Swedish schoolmistress novel", 121,
     "女性教員の賃金と独身生活を描く北欧写実の周縁形式。"),
    ("フリースラント語農家小説", "Frisian farmhouse fiction", 121,
     "フリース語で農家相続と村落名誉を扱う地方リアリズム。"),
    ("オランダ植民地帰還者リアリズム", "Dutch colonial returnee realism", 121,
     "東インド帰還者の家計破綻を本国都市で描く写実小説群。"),
    ("北海沿岸方言写本小説", "North Sea dialect manuscript fiction", 121,
     "刊行前写本に残る沿岸労働と方言会話の写実的記録。"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            if len(definition) > 100:
                raise ValueError(f"definition too long: {name_ja}")
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code=SUBFIELD,
                region=REGION,
                period_id=period_id,
                definition=definition,
                importance_score=1,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )
    print(f"inserted {len(CONCEPTS)} concepts")


if __name__ == "__main__":
    main()
