from lit_db_helper import LitDB


REGION = "西欧"
SUBFIELD = "lit_eu_enlightenment"

P_EARLY = 99
P_HIGH = 100
P_SENS = 101
P_LATE = 102


CONCEPTS = [
    # Clandestine print micro-practices
    dict(name_ja="黙認特許本の半合法流通", name_en="tacit-permission book circulation", period_id=P_HIGH, definition="正式許可を避け黙認特許で流通した啓蒙期出版物。"),
    dict(name_ja="リブレール便覧の禁書記号", name_en="bookseller catalogue ban marks", period_id=P_HIGH, definition="書籍商目録で禁書性を符号化して示す販売慣行。"),
    dict(name_ja="押収目録の読書履歴化", name_en="seizure inventory as reading trace", period_id=P_HIGH, definition="押収本一覧から読者の禁書接触を復元する視角。"),
    dict(name_ja="密輸梱包の二重表題紙", name_en="double title-page smuggling", period_id=P_HIGH, definition="検閲通過用表題紙で本来の書名を隠す装丁技法。"),
    dict(name_ja="地下版余白の読者合印", name_en="reader marks in clandestine editions", period_id=P_HIGH, definition="禁書版の余白に残る貸借・共読の小記号。"),
    dict(name_ja="偽翻訳書名の検閲逃れ", name_en="pseudo-translation title evasion", period_id=P_HIGH, definition="翻訳書を装う書名で政治的批判性を隠す手法。"),
    # Periodical address and reader management
    dict(name_ja="購読者名簿の序文誇示", name_en="subscriber-list preface display", period_id=P_HIGH, definition="序文周辺に購読者名を掲げ権威と市場を示す慣行。"),
    dict(name_ja="週刊紙の架空投書連鎖", name_en="fictional letter chains in weeklies", period_id=P_HIGH, definition="架空読者の投書応酬で公共討議を演出する形式。"),
    dict(name_ja="紙上編集者の慈父口調", name_en="paternal editor voice", period_id=P_HIGH, definition="編集者が読者を教導する父性的語り口。"),
    dict(name_ja="道徳週刊紙の夢寓話欄", name_en="dream allegory in moral weeklies", period_id=P_EARLY, definition="夢の枠で悪徳批判を行う短い定期刊行物欄。"),
    dict(name_ja="広告欄の文学サロン化", name_en="advertising column salonization", period_id=P_HIGH, definition="新刊広告が読者共同体と文学趣味を演出する紙面。"),
    dict(name_ja="読者投票型懸賞詩", name_en="reader-voted prize poem", period_id=P_HIGH, definition="読者審査や懸賞で詩作参加を促す雑誌企画。"),
    # Stage, spectatorship, and censorship
    dict(name_ja="パルテールの拍手政治", name_en="parterre applause politics", period_id=P_HIGH, definition="平土間観客の拍手が上演評価と政治性を帯びる現象。"),
    dict(name_ja="初演報告の検閲婉曲語", name_en="censorial euphemism in premiere reports", period_id=P_HIGH, definition="上演評で検閲事項を婉曲に伝える批評語法。"),
    dict(name_ja="座席身分差の笑劇利用", name_en="seat-rank farce device", period_id=P_HIGH, definition="劇場内の座席序列を笑劇的葛藤に変える装置。"),
    dict(name_ja="舞台袖朗読の出版宣伝", name_en="wing reading as book promotion", period_id=P_HIGH, definition="上演前後の朗読で戯曲刊本の購入を促す慣行。"),
    dict(name_ja="涙劇幕間の徳談義", name_en="intermission virtue talk in tear drama", period_id=P_SENS, definition="幕間会話で感動を道徳判断へ変える観劇実践。"),
    dict(name_ja="俳優肖像版画の名声循環", name_en="actor print fame circulation", period_id=P_SENS, definition="俳優肖像版画が劇場外で人気と役柄を増幅する流通。"),
    # Epistolary and sentimental reading traces
    dict(name_ja="書簡小説の封緘演出", name_en="sealed-letter staging", period_id=P_SENS, definition="封印や開封場面で私密性と覗き読みを演出する技法。"),
    dict(name_ja="涙染みの真正性証明", name_en="tear stains as authenticity proof", period_id=P_SENS, definition="涙染みを感情の実在証拠として提示する感傷的装置。"),
    dict(name_ja="返書遅延の徳試験", name_en="delayed reply virtue test", period_id=P_SENS, definition="返書の遅れで忍耐・貞節・友情を試す筋立て。"),
    dict(name_ja="家庭読書会の交替朗読", name_en="rotating family reading aloud", period_id=P_SENS, definition="家族が章ごとに交替して読む感傷小説の受容形。"),
    dict(name_ja="余白感嘆符の共感競争", name_en="marginal exclamation sympathy rivalry", period_id=P_SENS, definition="余白の感嘆符で読者同士の共感量を競う痕跡。"),
    dict(name_ja="遺稿発見型書簡序", name_en="found-manuscript letter preface", period_id=P_SENS, definition="発見遺稿として書簡群の真正性を保証する序文形式。"),
    # Comparative fiction and conjectural devices
    dict(name_ja="中国賢人対話の欧州風刺", name_en="Chinese sage dialogue satire", period_id=P_HIGH, definition="中国賢人の仮面で欧州慣習を批判する対話形式。"),
    dict(name_ja="ペルシア旅人の貨幣観察", name_en="Persian traveller money observation", period_id=P_HIGH, definition="異邦人旅行者に信用経済を観察させる風刺技法。"),
    dict(name_ja="月世界旅行の測量脚注", name_en="lunar voyage measurement footnotes", period_id=P_EARLY, definition="架空旅行に測量脚注を添え信憑性を装う形式。"),
    dict(name_ja="自然児教育の実験日誌", name_en="natural child pedagogic diary", period_id=P_LATE, definition="自然児の成長を日誌風に記録する教育実験叙述。"),
    dict(name_ja="文明段階表の物語挿入", name_en="stadial table narrative insertion", period_id=P_HIGH, definition="社会発展段階表を物語中の説明として挿入する技法。"),
    dict(name_ja="翻訳注の習俗相対化", name_en="custom relativization in translation notes", period_id=P_HIGH, definition="翻訳注で欧州習俗を異文化比較にさらす方法。"),
]


def main() -> None:
    if len(CONCEPTS) != 30:
        raise ValueError(f"expected 30 concepts, got {len(CONCEPTS)}")
    with LitDB() as db:
        inserted = 0
        for concept in CONCEPTS:
            if len(concept["definition"]) > 100:
                raise ValueError(f"definition too long: {concept['name_ja']}")
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
                canonical_in_region="minor",
            )
            if before is None:
                inserted += 1
    print(f"inserted={inserted}")


if __name__ == "__main__":
    main()
