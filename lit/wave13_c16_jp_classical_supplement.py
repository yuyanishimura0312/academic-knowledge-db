"""Wave 13 supplement — add more fourth_transform_tags and cross_domain.

Targets: fourth_transform_tags >= 18 (currently 5), cross_domain >= 14 (currently 9).
We add 14 more 4T tags and 6 more cross_domain links to selected wave13 concepts.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


# (name_ja, axis, status, rationale, related_ai_phenomenon)
EXTRA_4T = [
    ("萬葉集巻別構造論", "言語", "rethinking",
     "巻別段階編纂説は文学コーパスの段階的構築過程を理論化する古典的事例で、AIコーパス構築の段階性問題と理論的に響き合う。",
     "AI学習コーパスの段階的構築問題"),
    ("懐風藻の漢詩世界", "言語", "rethinking",
     "懐風藻は外国語（漢文）による国家文学の出発点を成し、AI多言語生成と国民文学の関係を再考する祖型となる。",
     "AI多言語生成と国民文学概念"),
    ("菅原道真『菅家文草』", "主体", "rethinking",
     "道真大宰府期の悲憤詩は失脚した知識人主体の声を文学化した古典的事例で、AI時代の周縁化された主体の声の再評価問題を再考する参照点となる。",
     "AI時代の周縁化主体の文学的再評価"),
    ("徒然草段別考", "受容", "rethinking",
     "徒然草の段別不連続な構造は近代以降フラグメント文学の祖型として再解釈され、AI生成短文集積の受容枠組みと響き合う。",
     "AI生成フラグメント集積の受容問題"),
    ("太平記の和漢混淆", "言語", "rethinking",
     "太平記の和漢混淆文は複数言語層の動的混淆を文体化する。LLMの多言語混淆生成の文学的祖型として再読される。",
     "LLM多言語混淆生成の文学的祖型"),
    ("北畠親房『神皇正統記』", "作者性", "rethinking",
     "神皇正統記は危機的状況下の歴史哲学的著述で、AI時代の歴史記述・国家叙述の作者性問題を再考する参照点となる。",
     "AI生成歴史叙述と国家アイデンティティ"),
    ("今昔物語集巻別構造", "受容", "rethinking",
     "三国構造の今昔物語集は世界規模の文化伝播経路を物語化した古典で、AI時代の越境的物語流通の祖型として再読される。",
     "AI時代の越境的物語流通"),
    ("無住『沙石集』", "言語", "rethinking",
     "沙石集の方便としての笑話は、難解な真理を平易な口語で伝達する技法を体系化した古典で、AI生成のレジスタ転換と理論的に共振する。",
     "AI生成のレジスタ転換と方便論"),
    ("とりかへばや物語", "受容", "rethinking",
     "性別越境の物語的肯定は近現代受容で再解釈され続けており、AI時代のジェンダー流動性受容の歴史的祖型を成す。",
     "AI時代のジェンダー流動性受容"),
    ("方丈記の災厄記述", "主体", "rethinking",
     "方丈記の隠遁者主体による災害証言は、当事者性と観察者性の境界を文学化する。AIによる災害ドキュメンタリーの主体性問題を再考する原型。",
     "AI災害ドキュメンタリーの主体性問題"),
    ("紫式部日記の女房世界", "受容", "rethinking",
     "紫式部日記の女房間批評は文学批評の制度化前夜の批評共同体を示し、AI時代の集団的批評・レビュー文化の祖型として再読される。",
     "AI時代の集団的批評文化"),
    ("御堂関白記の文体", "真正性", "rethinking",
     "御堂関白記の自筆原本（陽明文庫蔵）は権力中枢の自筆記録としての真正性を体現し、AI生成記録の真正性概念を再考する参照点となる。",
     "AI生成公的記録と真正性"),
    ("土佐日記の編年体破断", "作者性", "rethinking",
     "貫之の女性仮託は作者性とジェンダー越境の方法的実験で、AI時代のペルソナ生成・作者ジェンダー流動化の祖型となる。",
     "AIペルソナ生成と作者ジェンダー越境"),
    ("五山文学・義堂周信", "言語", "rethinking",
     "五山禅僧による外国語（漢詩文）での国家代表的著述は、AI多言語生成における言語選択と作者位置を再考する歴史的参照点となる。",
     "AI多言語生成と作者位置"),
]


# (name_ja, target_db, target_entity_name, description)
EXTRA_CD = [
    ("萬葉集巻別構造論", "PT",
     "コーパス段階編纂と詩学",
     "萬葉集巻別段階編纂説はコーパスの段階的成立を扱う古典的事例で、詩学コーパス論の中核研究対象となる。"),
    ("柿本人麻呂レクチエッ複合（挽歌・宮廷歌人論）", "PHIL",
     "古代王権儀礼と挽歌哲学",
     "人麻呂挽歌は古代日本の鎮魂哲学・王権儀礼思想の文学的具現で、東アジア政治哲学史に独自の位置を占める。"),
    ("徒然草段別考", "PT",
     "随想体・フラグメント詩学",
     "徒然草はフラグメント形式の詩学的成熟例で、現代物語論・断章形式論の中核参照点となる。"),
    ("太平記の和漢混淆", "PT",
     "和漢混淆文体論",
     "太平記の和漢混淆文は中世文体論の頂点で、文体論研究の中心対象として位置する。"),
    ("方丈記の災厄記述", "AN",
     "災害民族誌と当事者証言",
     "方丈記の災厄記述は古代観察者による災害民族誌の祖型で、人類学的災害研究の比較対象として重要。"),
    ("北畠親房『神皇正統記』", "PT",
     "中世歴史叙述詩学",
     "神皇正統記は中世歴史哲学詩学の中核作品で、近世水戸学・近代国学の歴史叙述論に直接継承された。"),
]


def main() -> int:
    f_added = cd_added = 0
    with LitDB() as db:
        # Build name -> id map for subfield 10
        rows = db.conn.execute(
            "SELECT id, name_ja FROM concepts WHERE subfield_id=10"
        ).fetchall()
        name_to_id = {r["name_ja"]: r["id"] for r in rows}

        for name, axis, status, rationale, ai in EXTRA_4T:
            cid = name_to_id.get(name)
            if cid is None:
                print(f"  [skip 4T] not found: {name}")
                continue
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai)
                f_added += 1
            except LitDBError as e:
                print(f"  [warn 4T] {name}: {e}")

        for name, tdb, tname, desc in EXTRA_CD:
            cid = name_to_id.get(name)
            if cid is None:
                print(f"  [skip CD] not found: {name}")
                continue
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=tdb, link_type="shared_concept",
                    target_entity_name=tname, description=desc)
                cd_added += 1
            except LitDBError as e:
                print(f"  [warn CD] {name}: {e}")

        print(f"[c16-w13-supp] +4T tags: {f_added}; +cross_domain: {cd_added}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
