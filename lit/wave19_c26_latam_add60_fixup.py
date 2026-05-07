"""Fixup: insert the 8 concepts that failed in wave19 due to canonical_in_region='supporting'.
Now using 'minor' which is in the allowed set.
"""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError


BVMC = "https://www.cervantesvirtual.com/"
ARCHIVE = "https://archive.org/details/"

C = dict(subfield_code="lit_latin_america", region="ラテンアメリカ",
         original_script="roman")

# Need correct period_ids; we'll fetch them
PERIOD_NAMES = {
    "コロニアル詳細期": (1500, 1800),
    "19世紀補完期": (1810, 1900),
    "Vanguardismo期": (1916, 1945),
}

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)


add(**C, name_ja="バルブエナ『エル・ベルナルド』",
    name_en="Balbuena's El Bernardo",
    name_original="El Bernardo, o victoria de Roncesvalles",
    period_key="コロニアル詳細期",
    definition="バルブエナが1624年に刊行した24歌の壮大叙事詩。スペイン英雄ベルナルド・デル・カルピオを主人公に、ロンセスバーリェスの戦いを再構築する植民地スペイン語叙事詩の頂点。",
    background="ヌエバ・エスパーニャ副王領で書かれたスペイン国民英雄叙事詩。",
    development="アメリカ大陸初の本格的英雄叙事詩として植民地詩の規範。",
    historical_context="17世紀植民地詩学のヨーロッパ古典模倣。",
    primary_source_url=BVMC+"obra/el-bernardo-o-victoria-de-roncesvalles/",
    primary_source_type="BVMC: El Bernardo",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="シグエンサ・イ・ゴンゴラ『パルテニコの勝利』",
    name_en="Sigüenza y Góngora's Triunfo parténico",
    name_original="Triunfo parténico",
    period_key="コロニアル詳細期",
    definition="カルロス・デ・シグエンサ・イ・ゴンゴラ（1645-1700）が1683年に刊行した詩学論集。メキシコ大学の聖母無原罪詩賛コンクール記録。植民地クリオージョ知識人ネットワークの記録。",
    background="17世紀メキシコ・シティのクリオージョ知識人サークル。",
    development="メキシコ・クリオージョ意識・地域アイデンティティの先駆的記録。",
    historical_context="ヌエバ・エスパーニャ副王領の文芸サロン文化。",
    primary_source_url=BVMC+"obra/triunfo-partenico/",
    primary_source_type="BVMC: Triunfo parténico",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="オーニャ『手なずけられたアラウコ』",
    name_en="Pedro de Oña's Arauco domado",
    name_original="Arauco domado",
    period_key="コロニアル詳細期",
    definition="ペドロ・デ・オーニャ（1570-1643）が1596年に刊行した叙事詩。エルシーリャ『ラ・アラウカーナ』への返答として、スペイン征服者ガルシア・ウルタド・デ・メンドーサを称揚する。",
    background="エルシーリャ叙事詩への政治的対抗としてのチリ植民地詩。",
    development="チリ最初のクリオージョ詩人作品としてチリ国民文学の起源。",
    historical_context="16世紀末チリ・アラウコ戦争の植民地視点。",
    primary_source_url=BVMC+"obra/arauco-domado--0/",
    primary_source_type="BVMC: Arauco domado",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="アスカスビ『サントス・ベガ』",
    name_en="Hilario Ascasubi's Santos Vega",
    name_original="Santos Vega o Los mellizos de la flor",
    period_key="19世紀補完期",
    definition="イラリオ・アスカスビ（1807-1875）が1872年に発表した13,000行のガウチェスコ叙事詩。伝説的パイヤドール（即興詩人）サントス・ベガを主人公に、パンパス文化を百科全書的に記述。",
    background="アスカスビのフランス亡命中、パンパス民俗の集合的記憶化。",
    development="エルナンデス『マルティン・フィエロ』への直接の前駆。",
    historical_context="19世紀後半パンパス文化の文学的記録化。",
    primary_source_url=BVMC+"obra/santos-vega-o-los-mellizos-de-la-flor/",
    primary_source_type="BVMC: Santos Vega",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="フアン・マリア・グティエレス『アメリカ詩集』",
    name_en="Juan María Gutiérrez's América poética",
    name_original="América poética",
    period_key="19世紀補完期",
    definition="フアン・マリア・グティエレス（1809-1878）が1846年に編纂したラテンアメリカ初の地域詩アンソロジー。15か国の詩人を集め、汎アメリカ的文学アイデンティティの構築を試みた。",
    background="1840年代アルゼンチン亡命知識人による汎アメリカ文学運動。",
    development="ラテンアメリカ文学概念の制度化の起点。",
    historical_context="独立後ラテンアメリカ国民文学形成期。",
    primary_source_url=BVMC+"obra/america-poetica/",
    primary_source_type="BVMC: América poética",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="オストス『バヨアンの巡礼』",
    name_en="Hostos's La peregrinación de Bayoán",
    name_original="La peregrinación de Bayoán",
    period_key="19世紀補完期",
    definition="エウヘニオ・マリア・デ・オストス（1839-1903）が1863年に発表した思想小説。タイノ族首長バヨアンの架空巡礼を通じてプエルトリコ・キューバの独立とアンティル連合を提唱した。",
    background="1860年代スペイン領アンティル諸島独立運動。",
    development="マルティ、ルベン・ダリオに先立つアンティル独立思想の文学化。",
    historical_context="19世紀後半スペイン領カリブ独立運動。",
    primary_source_url=BVMC+"obra/la-peregrinacion-de-bayoan--0/",
    primary_source_type="BVMC: La peregrinación de Bayoán",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ヒロンド『骨髄の中で』",
    name_en="Girondo's En la masmédula",
    name_original="En la masmédula",
    period_key="Vanguardismo期",
    definition="ヒロンドが1954年に発表した晩年詩集。新造語・音声実験で言語の物質性を極限化し、コンクリート詩・パラ反詩の前駆となった。",
    background="アルゼンチン前衛詩の戦後継続、ヒロンドとノラー・ラング夫妻のサロン。",
    development="ニカノル・パラ反詩、レオニダス・ラムボーグニーニ詩学の祖。",
    historical_context="1950年代アルゼンチン詩の言語物質化。",
    primary_source_url=BVMC+"obra/en-la-masmedula/",
    primary_source_type="BVMC: En la masmédula",
    importance_score=3, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="ジョルジ・デ・リマ『オルフェウスの発明』",
    name_en="Jorge de Lima's Invenção de Orfeu",
    name_original="Invenção de Orfeu",
    period_key="Vanguardismo期",
    definition="ジョルジ・デ・リマ（1893-1953）が1952年に発表した10歌・5000行の叙事詩。カモンイス『ウズ・ルジアダス』を範に、ブラジルの神話的・カトリック的・アフロ系起源を統合する。",
    background="北東部アラゴアス州のカトリック・アフロ系融合文化。",
    development="ブラジル現代叙事詩の頂点として参照される。",
    historical_context="20世紀中葉ブラジル神話的国民詩。",
    primary_source_url=ARCHIVE+"invencaodeorfeu0000lima",
    primary_source_type="archive.org: Invenção de Orfeu",
    importance_score=3, source_tier="primary", canonical_in_region="minor")


def main() -> int:
    inserted = 0
    with LitDB() as db:
        # Resolve existing period_ids by querying via get_or_create
        period_ids = {}
        for nj, (sy, ey) in PERIOD_NAMES.items():
            pid = db.get_or_create_period(name_ja=nj, region="ラテンアメリカ",
                                          start_year=sy, end_year=ey)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
                inserted += 1
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
        summary = db.progress_summary()
        print(f"[c26-w19-fixup] inserted: {inserted} / total: {summary['concepts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
