from lit_db_helper import LitDB


CONCEPTS = [
    # 1. paratextual micro-devices
    ("奥付語り手", "colophon narrator", 124, "奥付の刊行情報を語りの声へ転用するメタ装置。"),
    ("謝辞プロット", "acknowledgment plot", 124, "謝辞欄の人名連鎖で隠れた関係史を示す構成。"),
    ("正誤表小説", "errata fiction", 124, "正誤表が本文の真偽と事件順を更新する形式。"),
    ("禁帯出叙述", "non-circulating narrative", 124, "禁帯出資料の閲覧制限が筋を制御する小説。"),
    ("献辞暗号", "dedicatory cipher", 124, "献辞の頭字や順序が別筋を開くパラテクスト技法。"),
    ("図版キャプション迷宮", "caption labyrinth", 124, "図版キャプションだけで別の物語層を編む形式。"),
    # 2. archival forensics
    ("水濡れ文書叙述", "water-damaged document narrative", 124, "水損で読めない箇所を意味の核にする文書小説。"),
    ("保存箱年代記", "archive-box chronicle", 124, "保存箱番号の順で断片的年代記を組む形式。"),
    ("鉛筆消去証言", "erased-pencil testimony", 124, "消し跡や筆圧を証言の残存として読む叙述。"),
    ("複写ノイズ詩学", "photocopy-noise poetics", 124, "複写の汚れやズレを文体効果にする技法。"),
    ("封緘解除プロット", "unsealing plot", 124, "封緘資料の開封時期が読解を遅延させる構成。"),
    ("寄贈票メタ小説", "donation-slip metafiction", 124, "寄贈票の来歴情報が作者像を揺らす小説。"),
    # 3. EU document satire
    ("附属書寓話", "annex fable", 131, "附属書だけで制度的暴力を寓話化する形式。"),
    ("入札仕様書小説", "tender-spec fiction", 131, "公共入札仕様書の形式で文化制作を風刺する小説。"),
    ("監査報告叙述", "audit-report narrative", 131, "監査報告の語法で私的記憶を査定する叙述。"),
    ("多年度計画プロット", "multiannual-plan plot", 131, "EU式計画期間が人物の時間感覚を支配する筋。"),
    ("コンプライアンス悲喜劇", "compliance tragicomedy", 131, "遵守書類の過剰が倫理判断を空洞化する喜劇。"),
    ("評価指標パロディ", "indicator parody", 131, "成果指標の数値化で文学価値を笑う制度風刺。"),
    # 4. minor-language edition games
    ("小言語背表紙小説", "minor-language spine fiction", 131, "背表紙の小言語表記差が共同体境界を示す形式。"),
    ("訳注乗っ取り", "translator-note takeover", 124, "訳注が本文を侵食し語りの主導権を奪う技法。"),
    ("逐語訳フェイク", "fake literal translation", 124, "逐語訳を装い原文不在を露出させる版面設計。"),
    ("固有名詞未訳戦略", "untranslated-name strategy", 131, "固有名を訳さず残し権力関係を可視化する手法。"),
    ("発音表記過剰", "phonetic-overgloss fiction", 131, "発音表記の過多で読解を遅らせる小言語小説。"),
    ("対訳空欄叙述", "blank-facing-page narrative", 124, "対訳ページの空欄が翻訳不能性を物語る形式。"),
    # 5. platform residue autofiction
    ("二段階認証自伝", "two-factor autobiography", 125, "認証コードの履歴で自己の断片化を記録する自伝。"),
    ("下書き復元私小説", "draft-recovery autofiction", 125, "復元された下書き差分で親密圏を再構成する私小説。"),
    ("ミュート関係叙述", "muted-relation narrative", 125, "ミュート設定が交友関係の非対称性を示す叙述。"),
    ("キャッシュ記憶小説", "cached-memory fiction", 131, "キャッシュに残る旧版が記憶の層を作る小説。"),
    ("スクロール疲労文体", "scroll-fatigue style", 131, "終わらないスクロール感を文の反復で再現する文体。"),
    ("通知バッジ時間", "badge-count temporality", 131, "通知数の増減で時間経過と不安を示す形式。"),
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
