"""Wave 24: lit_eu_classical (subfield_id=1) +30 concepts.

5 thematic clusters x 6 = 30:
  1. Late Latin (Aulus Gellius, Macrobius, Sidonius, Ausonius, Claudian, Prudentius)
  2. Greek prose (Plutarch x2, Lucian x2, Heliodorus, Longus)
  3. Hellenistic poetry (Callimachus, Theocritus, Apollonius, Posidippus, Aratus, Lycophron)
  4. Greek tragedy late (Euripides x3, Sophocles x2, Aeschylus)
  5. Roman supplement (Quintilian, Tacitus x2, Suetonius, Lucretius, Catullus)
"""
from __future__ import annotations

from lit_db_helper import LitDB


def get_pid(db: LitDB, name_ja: str) -> int:
    row = db.conn.execute(
        "SELECT id FROM periods WHERE name_ja=? AND region='西欧'",
        (name_ja,),
    ).fetchone()
    if not row:
        raise RuntimeError(f"period not found: {name_ja}")
    return row["id"]


def main() -> None:
    with LitDB() as db:
        # Period IDs (region='西欧')
        p_classical = get_pid(db, "古典期（クラシック）")        # id=6
        p_hellenistic = get_pid(db, "ヘレニズム期")                # id=7
        p_late_rome = get_pid(db, "後期ローマ・教父期")          # id=198
        p_augustan = get_pid(db, "アウグストゥス時代")              # id=74
        p_roman_silver = get_pid(db, "帝政ローマ時代（白銀期）")  # id=75
        p_roman_late_rep = get_pid(db, "ローマ共和政後期")        # id=73

        concepts = [
            # ---- Cluster 1: Late Latin (period: 後期ローマ・教父期) ----
            dict(
                name_ja="アウルス・ゲッリウス『アッティカ夜話』補論",
                name_en="Aulus Gellius, Noctes Atticae (supplement)",
                name_original="Noctes Atticae",
                period_id=p_late_rome,
                definition="2世紀の博物学的雑録。古ラテン語法・文法・古典逸話を集成した教養百科。",
                importance_score=4,
            ),
            dict(
                name_ja="マクロビウス『サトゥルナリア』補論",
                name_en="Macrobius, Saturnalia (supplement)",
                name_original="Saturnalia",
                period_id=p_late_rome,
                definition="5世紀の対話形式雑録。ウェルギリウス論・古代祭儀・古典学知識の継承を担う。",
                importance_score=4,
            ),
            dict(
                name_ja="シドニウス・アポリナリス書簡・詩",
                name_en="Sidonius Apollinaris, Letters and Poems",
                name_original="Epistulae et Carmina",
                period_id=p_late_rome,
                definition="5世紀ガリアの貴族・司教の書簡詩集。古典的修辞でローマ末期社会を描写する。",
                importance_score=3,
            ),
            dict(
                name_ja="アウソニウス『モセラ』ほか",
                name_en="Ausonius, Mosella and other works",
                name_original="Mosella",
                period_id=p_late_rome,
                definition="4世紀ガリア出身詩人の地誌詩・教師讃。後期ラテン詩の自然描写の到達点。",
                importance_score=3,
            ),
            dict(
                name_ja="クラウディアヌス叙事詩",
                name_en="Claudian, epic poetry",
                name_original="De Raptu Proserpinae",
                period_id=p_late_rome,
                definition="4世紀末の宮廷詩人による異教的叙事詩。古典叙事詩伝統の最後の華。",
                importance_score=4,
            ),
            dict(
                name_ja="プルデンティウス『プシュコマキア』詳論",
                name_en="Prudentius, Psychomachia (detailed)",
                name_original="Psychomachia",
                period_id=p_late_rome,
                definition="諸徳と諸悪が魂を奪い合う寓意叙事詩。中世アレゴリー詩の祖型。",
                importance_score=5,
            ),

            # ---- Cluster 2: Greek prose (period: 古典期 or ヘレニズム期/帝政) ----
            dict(
                name_ja="プルタルコス『対比列伝・テセウス』",
                name_en="Plutarch, Life of Theseus",
                name_original="Βίος Θησέως",
                period_id=p_roman_silver,
                definition="アテネ建国王テセウスの伝記。神話と歴史の境界を扱う対比列伝の冒頭。",
                importance_score=4,
            ),
            dict(
                name_ja="プルタルコス『対比列伝・ペリクレス』",
                name_en="Plutarch, Life of Pericles",
                name_original="Βίος Περικλέους",
                period_id=p_roman_silver,
                definition="アテネ民主政指導者ペリクレスの伝記。古典期民主政理解の古典的源泉。",
                importance_score=5,
            ),
            dict(
                name_ja="ルキアノス『遍歴の哲学者売り』",
                name_en="Lucian, Philosophies for Sale",
                name_original="Βίων πρᾶσις",
                period_id=p_roman_silver,
                definition="諸学派の哲学者を奴隷市で競売する諷刺対話。哲学正典への風刺批評。",
                importance_score=4,
            ),
            dict(
                name_ja="ルキアノス『ヘルモティモス』",
                name_en="Lucian, Hermotimus",
                name_original="Ἑρμότιμος",
                period_id=p_roman_silver,
                definition="ストア派門人ヘルモティモスとの対話。哲学諸派選択の不可能性を諷刺。",
                importance_score=3,
            ),
            dict(
                name_ja="ヘリオドロス『エチオピア物語』詳論",
                name_en="Heliodorus, Aethiopica (detailed)",
                name_original="Αἰθιοπικά",
                period_id=p_roman_silver,
                definition="3世紀の最長ギリシア恋愛小説。in medias res構成で近代小説に影響。",
                importance_score=5,
            ),
            dict(
                name_ja="ロンゴス『ダフニスとクロエ』詳論",
                name_en="Longus, Daphnis and Chloe (detailed)",
                name_original="Ποιμενικά",
                period_id=p_roman_silver,
                definition="2世紀の田園恋愛小説。牧歌伝統と恋愛小説を融合し近代田園小説の祖型。",
                importance_score=5,
            ),

            # ---- Cluster 3: Hellenistic poetry ----
            dict(
                name_ja="カリマコス『アポロン讃歌』",
                name_en="Callimachus, Hymn to Apollo",
                name_original="Εἰς Ἀπόλλωνα",
                period_id=p_hellenistic,
                definition="アレクサンドリア祭儀讃歌。簡潔・洗練の詩学（leptotes）を提示。",
                importance_score=4,
            ),
            dict(
                name_ja="テオクリトス『田園詩第11歌』",
                name_en="Theocritus, Idyll 11 (Cyclops)",
                name_original="Εἰδύλλιον ΙΑʹ",
                period_id=p_hellenistic,
                definition="キュクロプスの片想いを描く牧歌。怪物の人間化と恋愛牧歌の起点。",
                importance_score=4,
            ),
            dict(
                name_ja="アポロニオス・ロディオス『アルゴナウティカ』第1巻",
                name_en="Apollonius Rhodius, Argonautica Book I",
                name_original="Ἀργοναυτικά Αʹ",
                period_id=p_hellenistic,
                definition="アルゴ船遠征叙事詩の発端。ホメロス模倣と心理描写を結ぶヘレニズム叙事詩。",
                importance_score=5,
            ),
            dict(
                name_ja="ポセイディッポス『ミラン・パピルス』",
                name_en="Posidippus, Milan Papyrus epigrams",
                name_original="Ἐπιγράμματα",
                period_id=p_hellenistic,
                definition="2001年公開の112篇エピグラム集。宝石・像・予兆を扱うヘレニズム小詩。",
                importance_score=3,
            ),
            dict(
                name_ja="アラトス『ファイノメナ』",
                name_en="Aratus, Phaenomena",
                name_original="Φαινόμενα",
                period_id=p_hellenistic,
                definition="星座と気象徴候の教訓詩。古代天文学詩の正典でキケロ・ウェルギリウスに影響。",
                importance_score=4,
            ),
            dict(
                name_ja="リュコフロン『アレクサンドラ』",
                name_en="Lycophron, Alexandra",
                name_original="Ἀλεξάνδρα",
                period_id=p_hellenistic,
                definition="カッサンドラの神託独白詩。難解語法でヘレニズム韜晦詩の極北。",
                importance_score=3,
            ),

            # ---- Cluster 4: Greek tragedy late ----
            dict(
                name_ja="エウリピデス『トロイアの女』",
                name_en="Euripides, Trojan Women",
                name_original="Τρῳάδες",
                period_id=p_classical,
                definition="陥落後の捕囚女性たちを描く悲劇。戦争と征服の暴力を告発する反戦劇の祖型。",
                importance_score=5,
            ),
            dict(
                name_ja="エウリピデス『ヘレネ』",
                name_en="Euripides, Helen",
                name_original="Ἑλένη",
                period_id=p_classical,
                definition="エジプトに匿われたヘレネ像と幻影論。神話の異本提示と悲喜劇的悲劇。",
                importance_score=4,
            ),
            dict(
                name_ja="エウリピデス『イオン』",
                name_en="Euripides, Ion",
                name_original="Ἴων",
                period_id=p_classical,
                definition="アテネ起源神話を扱う認知劇。アポロンとクレウサ、捨て子イオンの再会譚。",
                importance_score=4,
            ),
            dict(
                name_ja="ソフォクレス『アイアース』",
                name_en="Sophocles, Ajax",
                name_original="Αἴας",
                period_id=p_classical,
                definition="武具争奪に敗れた英雄アイアースの狂気と自死。英雄倫理の悲劇的破綻。",
                importance_score=5,
            ),
            dict(
                name_ja="ソフォクレス『トラキスの女たち』",
                name_en="Sophocles, Trachiniae",
                name_original="Τραχίνιαι",
                period_id=p_classical,
                definition="ヘラクレスとデーイアネイラの悲劇。誤った恋慕と毒衣による破滅。",
                importance_score=4,
            ),
            dict(
                name_ja="アイスキュロス『ペルシア人』",
                name_en="Aeschylus, Persians",
                name_original="Πέρσαι",
                period_id=p_classical,
                definition="サラミス海戦をペルシア宮廷視点から描く現存最古悲劇。歴史劇の祖。",
                importance_score=5,
            ),

            # ---- Cluster 5: Roman supplement ----
            dict(
                name_ja="クインティリアヌス『弁論家の教育』詳論",
                name_en="Quintilian, Institutio Oratoria (detailed)",
                name_original="Institutio Oratoria",
                period_id=p_roman_silver,
                definition="12巻の弁論家養成体系。修辞学・教育論の集大成でルネサンス教育の規範。",
                importance_score=5,
            ),
            dict(
                name_ja="タキトゥス『年代記』",
                name_en="Tacitus, Annals",
                name_original="Annales",
                period_id=p_roman_silver,
                definition="ティベリウスからネロまでのローマ帝政史。簡潔体と道徳的洞察の歴史叙述。",
                importance_score=5,
            ),
            dict(
                name_ja="タキトゥス『歴史』",
                name_en="Tacitus, Histories",
                name_original="Historiae",
                period_id=p_roman_silver,
                definition="69年内乱からドミティアヌス期の歴史。四皇帝の年と帝政危機を描く。",
                importance_score=4,
            ),
            dict(
                name_ja="スエトニウス『皇帝伝（ローマ皇帝伝）』",
                name_en="Suetonius, De Vita Caesarum",
                name_original="De Vita Caesarum",
                period_id=p_roman_silver,
                definition="カエサルからドミティアヌスまで12皇帝の伝記。逸話的伝記の古典的形式。",
                importance_score=5,
            ),
            dict(
                name_ja="ルクレティウス『事物の本性について』",
                name_en="Lucretius, De Rerum Natura",
                name_original="De Rerum Natura",
                period_id=p_roman_late_rep,
                definition="エピクロス自然哲学を韻律で説く6巻教訓詩。原子論と無神論的世界観を提示。",
                importance_score=5,
            ),
            dict(
                name_ja="カトゥッルス『歌集（カルミナ）』詳論",
                name_en="Catullus, Carmina (detailed)",
                name_original="Carmina",
                period_id=p_roman_late_rep,
                definition="新詩派代表の116篇詩集。レスビアへの愛・諷刺・神話詩を含むラテン抒情詩の起点。",
                importance_score=5,
            ),
        ]

        inserted = 0
        skipped = 0
        for c in concepts:
            assert len(c["definition"]) <= 100, f"def too long: {c['name_ja']} ({len(c['definition'])})"
            existing = db.find_concept(c["name_ja"], "西欧", c["period_id"])
            if existing:
                skipped += 1
                print(f"[skip] {c['name_ja']} (id={existing})")
                continue
            cid = db.insert_concept(
                name_ja=c["name_ja"],
                name_en=c["name_en"],
                name_original=c["name_original"],
                subfield_code="lit_eu_classical",
                region="西欧",
                period_id=c["period_id"],
                definition=c["definition"],
                source_tier="primary",
                canonical_in_region="major",
                importance_score=c["importance_score"],
            )
            inserted += 1
            print(f"[ok] id={cid} {c['name_ja']}")

        print(f"\nWave24 c01 result: inserted={inserted}, skipped={skipped}, total={len(concepts)}")


if __name__ == "__main__":
    main()
