from lit_db_helper import LitDB


CONCEPTS = [
    # 1. material text / editorial fiction
    ("割付崩壊小説", "typographic collapse fiction", 124, "組版の乱れを物語情報として読む実験小説。"),
    ("ページ番号逸脱叙述", "pagination deviance narrative", 124, "ページ番号の欠落や重複で時間順序を撹乱する叙述。"),
    ("校正記号物語", "proofmark fiction", 124, "校正記号や訂正指示が筋を動かすメタ小説技法。"),
    ("折丁迷宮構成", "signature labyrinth structure", 124, "折丁単位の錯綜で読書順を不安定化する構成。"),
    ("余白侵入叙述", "margin-invasion narrative", 124, "本文外の余白が語りの主戦場になる叙述法。"),
    ("凡例フェイク", "fake editorial apparatus", 124, "凡例や校訂方針を虚構化して権威をずらす装置。"),
    # 2. archive / document residue
    ("請求記号プロット", "call-number plot", 124, "図書館請求記号の連鎖が探索の筋を作る形式。"),
    ("廃棄文書叙述", "discarded-record narrative", 124, "廃棄済み文書の断片から物語を復元する構成。"),
    ("目録誤記フィクション", "catalogue-error fiction", 124, "目録の誤記や分類違いを事件化する小説形式。"),
    ("閲覧票アーカイヴ", "reading-slip archive", 124, "閲覧票や貸出票を記憶の証拠として扱う叙述。"),
    ("黒塗り脚注", "redacted footnote", 124, "検閲された脚注が不在の意味を生むメタ装置。"),
    ("版違い証言", "variant-edition testimony", 124, "異版差を証言の食い違いとして読む手法。"),
    # 3. European institutions / late bureaucratic satire
    ("補助金申請小説", "grant-application fiction", 131, "文化助成申請書の形式で芸術制度を風刺する小説。"),
    ("EU翻訳局寓話", "EU translation-office fable", 131, "多言語翻訳官僚制を寓話化する欧州小説の型。"),
    ("会議議事録叙述", "minutes-based narrative", 131, "議事録形式だけで対立と欠落を読ませる叙述。"),
    ("規格番号パロディ", "standard-number parody", 131, "規格番号や条項番号で文化の均質化を笑う技法。"),
    ("滞在許可メタ小説", "residence-permit metafiction", 131, "滞在許可書類が語りの資格を左右する小説。"),
    ("越境助成アイロニー", "cross-border funding irony", 131, "越境文化助成の言説を自己反省的に扱う形式。"),
    # 4. minor-language and translation niches
    ("自己字幕小説", "self-subtitling fiction", 131, "登場人物が自らの発話を別言語で字幕化する形式。"),
    ("方言グロス過剰", "dialect gloss excess", 124, "方言注釈の過多で翻訳可能性を疑わせる技法。"),
    ("小語彙索引小説", "minor-lexicon index novel", 131, "少数語彙の索引が共同体の記憶を担う小説。"),
    ("偽二言語版", "pseudo-bilingual edition", 124, "原文と訳文のずれを虚構の中心に置く版面設計。"),
    ("自動翻訳残響", "machine-translation residue", 131, "機械翻訳の誤差を文体資源にする現代的技法。"),
    ("失語翻訳者叙述", "aphasic-translator narrative", 125, "翻訳者の失語や欠語を語りの制約にする形式。"),
    # 5. autofiction / platform intimacy
    ("既読印自伝", "read-receipt autobiography", 125, "既読印や応答遅延で親密圏を記録する自伝形式。"),
    ("クラウド下書き小説", "cloud-draft fiction", 131, "同期された下書き履歴を物語時間として扱う小説。"),
    ("位置情報私小説", "geolocation autofiction", 125, "位置情報ログで自己記述を組み立てる私小説。"),
    ("削除済み投稿叙述", "deleted-post narrative", 131, "削除済み投稿の痕跡から主体を再構成する叙述。"),
    ("通知疲労リアリズム", "notification-fatigue realism", 131, "通知過多の注意散漫を日常描写の核にする文学。"),
    ("同期遅延プロット", "sync-lag plot", 131, "端末間の同期遅延が誤解と時間差を生む筋立て。"),
]


def main() -> None:
    with LitDB() as db:
        for name_ja, name_en, period_id, definition in CONCEPTS:
            db.insert_concept(
                name_ja=name_ja,
                name_en=name_en,
                subfield_code="lit_eu_postmodern",
                region="西欧",
                period_id=period_id,
                definition=definition,
                importance_score=2,
                source_tier="tertiary",
                canonical_in_region="marginal",
            )


if __name__ == "__main__":
    main()
