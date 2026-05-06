"""
LIT-DB Phase 6 Registry Helper

Adds the LIT-DB entry to ~/projects/apps/miratuku-news-v2/data/db-registry.json
under the 'conceptual' layer (alongside AN, SIF, AK, MG, MS, MPV academic DBs).

Usage:
    python phase6_register.py --dry-run   # show entry without writing
    python phase6_register.py --apply     # actually update registry
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent / "lit.sqlite"
REGISTRY_PATH = Path.home() / "projects/apps/miratuku-news-v2/data/db-registry.json"
DASHBOARD_PATH = Path.home() / "projects/apps/miratuku-news-v2/dashboards/lit.html"


def fetch_stats() -> dict:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cur = conn.cursor()
        stats = {}
        for tbl in ["concepts", "authors", "works", "movements", "relations",
                    "cross_domain", "fourth_transform_tags", "subfields"]:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            stats[tbl] = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT axis) FROM fourth_transform_tags")
        stats["axes_used"] = cur.fetchone()[0]
        return stats
    finally:
        conn.close()


def build_entry(stats: dict) -> dict:
    return {
        "id": "LIT",
        "name": "Literature Academic DB",
        "nameJa": "文学学術知識DB",
        "stat": (
            f"{stats['concepts']:,}概念 / "
            f"{stats['subfields']}サブフィールド / "
            f"{stats['cross_domain']:,}横断リンク"
        ),
        "description": (
            "枢軸時代→ルネサンス→産業革命→第四変容（AI社会）の今、文学が積み上げた概念を地域横断で再構造化するDB。"
            "西欧中心主義を解体し、東洋・非西欧圏（東アジア・南西アジア・グローバルサウス・周縁横断）に68.2%の規模配分。"
            "Poetics DB（PT）の上位包含層として作品・作家・運動を扱い、AI時代における作者性・創造性・物語・主体・正典・"
            "受容・翻訳・真正性・言語の9軸再考を全概念に紐づける。"
        ),
        "repo": "academic-knowledge-db",
        "dbId": "lit",
        "tables": 10,
        "rows": stats["concepts"],
        "storage": "SQLite",
        "update": "随時",
        "dashboard": "dashboards/lit.html",
        "agent": "/lit",
    }


def update_registry(entry: dict, dry_run: bool = True) -> None:
    if not REGISTRY_PATH.exists():
        print(f"registry not found: {REGISTRY_PATH}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    layers = data.get("layers", [])
    target_layer = next((l for l in layers if l.get("id") == "conceptual"), None)
    if not target_layer:
        print("conceptual layer not found", file=sys.stderr)
        sys.exit(1)

    dbs = target_layer.setdefault("databases", [])
    existing = next((d for d in dbs if d.get("id") == "LIT"), None)

    if existing:
        if dry_run:
            print("WOULD UPDATE existing LIT entry:")
            print(json.dumps(entry, ensure_ascii=False, indent=2))
        else:
            existing.update(entry)
            print("updated existing LIT entry")
    else:
        if dry_run:
            print("WOULD INSERT new LIT entry into 'conceptual' layer:")
            print(json.dumps(entry, ensure_ascii=False, indent=2))
        else:
            dbs.append(entry)
            print(f"appended LIT entry (now {len(dbs)} dbs in conceptual layer)")

    if not dry_run:
        from datetime import date
        data["updated"] = date.today().isoformat()
        REGISTRY_PATH.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {REGISTRY_PATH}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--apply", action="store_true",
                    help="apply changes to registry (otherwise dry-run)")
    args = ap.parse_args()

    stats = fetch_stats()
    print(f"current stats: concepts={stats['concepts']} subfields={stats['subfields']} "
          f"cross_domain={stats['cross_domain']} axes_used={stats['axes_used']}/9")
    print()

    entry = build_entry(stats)
    update_registry(entry, dry_run=not args.apply)

    if not args.apply:
        print()
        print("re-run with --apply to write changes")
    else:
        if not DASHBOARD_PATH.exists():
            print(f"\n[WARN] dashboard not yet generated: {DASHBOARD_PATH}")
            print("       run: python generate_lit_dashboard.py")


if __name__ == "__main__":
    main()
