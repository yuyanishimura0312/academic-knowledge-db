"""Phase 5: 教科書/サーベイ HTML 生成 (140エントリ MVP 版なので 16 章サーベイ形式)"""
import sqlite3
import datetime

DB = "/tmp/academic-build/academic-knowledge-db/academic.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("SELECT id, name_ja, name_en, definition, impact_summary, subfield, school_of_thought, era_start, key_researchers, key_works FROM business_development_bm_theory ORDER BY subfield, era_start")
all_entries = cur.fetchall()

sf_meta = [
    ('bmi_theory', 'ビジネスモデル理論・フレームワーク',
     'BM 概念の起源は Magretta (2002) の HBR 論文に遡る。Osterwalder & Pigneur (2010) の Business Model Canvas が実務界での標準言語となり、Zott & Amit (2010) のアクティビティ・システム視点が学術理論基盤を確立した。Massa, Tucci & Afuah (2017) のレビューは BM 研究の理論的成熟度に批判を投じ、Klang ら (2014) は概念の曖昧性を指摘して構成主義的再定義を試みた。'),
    ('bmi_process', 'BMIプロセス・動的能力',
     'BMI 研究は Chesbrough (2007) の SBL 論文で技術イノベーションから分離された。Casadesus-Masanell & Ricart (2010) の戦略-BM-戦術階層モデルが理論的支柱を提供し、Teece (2010) は動的能力理論と結合させた。Foss & Saebi (2017) の 15 年レビューが研究領域を体系化し、Markides (2013) は両利き経営文献との接続を模索する批判を展開した。'),
    ('digital_platform', 'デジタル・プラットフォームビジネスモデル',
     '理論基盤は Rochet & Tirole (2003) の二面市場理論に始まる。Eisenmann, Parker & Van Alstyne (2006) の HBR 論文が実務戦略を体系化し、Parker, Van Alstyne & Choudary (2016) の Platform Revolution が大衆化した。Cusumano, Gawer & Yoffie (2019) はプラットフォーム経済の規制・社会的影響に批判視点を持ち込んだ。ネットワーク効果・マルチホーミング・包囲戦略・ガバナンスが中心概念。'),
    ('alliance', '戦略的提携・パートナーシップ',
     'Gulati (1995) の社会ネットワーク論的アライアンス分析が起点。Dyer & Singh (1998) のリレーショナルビューが理論基盤を確立 (引用数 1万超)。Kale & Singh (2009) のレビューが現代研究を体系化し、Park & Ungson (2001) は経営的複雑性の観点から楽観論を批判した。コオペティション (Brandenburger-Nalebuff)、リアルオプション視点 (McGrath)、リソース依存理論 (Pfeffer-Salancik) が周辺の主要理論。'),
    ('corp_venture', 'コーポレートベンチャー・社内起業',
     'Burgelman (1983) の内部企業ベンチャープロセスモデルが起点。Block & MacMillan (1993) が実務フレーム、Garvin & Levesque (2006) が現代的応用、Hill & Birkinshaw (2008) が実証的失敗率を示して批判。アンビデクストラス組織 (O\'Reilly-Tushman)、ステージゲート (Cooper)、戦略的更新 (Agarwal-Helfat)、コーポレートアクセラレーター (Kohler) が周辺概念。Chesbrough (2002) の戦略的 vs 財務的 CV 類型は CVC 戦略の標準分類。'),
    ('market_entry', '新市場参入・成長戦略',
     'Ansoff (1957) の成長マトリクスが古典的起点。Porter (1980) の 5 forces が参入障壁分析を確立、Khanna & Palepu (2010) が新興市場制度的空隙論を発展させた。Prahalad (2005) の BoP 戦略は伝統的市場参入論への挑戦。参入モード選択 (Anderson-Gatignon 1986)、ボーン・グローバル (Knight-Cavusgil)、Beachhead 戦略 (Moore)、Land-and-Expand、アジャシエンシー戦略 (Zook) が現代の中心トピック。'),
    ('open_innov', 'オープンイノベーション・外部協創',
     'Chesbrough (2003) の Open Innovation が起点。Chesbrough, Vanhaverbeke & West (2006) が研究パラダイムを確立、Bogers ら (2017) が 7 領域での研究ランドスケープを整理した。Trott & Hartmann (2009) は概念新規性に疑問を投じる重要批判。Outside-In/Inside-Out プロセス、Crowdsourcing (Howe)、Innovation Intermediaries (Howells)、ユーザーイノベーション (von Hippel)、オープンビジネスモデルが中心。'),
    ('lean_startup', 'リーンスタートアップ・顧客開発',
     'Blank (2005) の顧客開発が起点。Ries (2011) のリーンスタートアップが大衆化 (書籍 100万部超)、Maurya (2016) がスケーリング期論を発展。Felin ら (2020) は CalMR で学術的批判を展開。MVP、Build-Measure-Learn、Pivot 類型 (10 種)、Lean Canvas、Validated Learning、Innovation Accounting、Concierge/Wizard of Oz MVP が中心概念。実務では極めて影響大、学術的検証は今後の課題。'),
    ('disruptive', '破壊的イノベーション・産業変革',
     'Christensen (1997) のイノベーターのジレンマが起点 (引用数 5万超)。Christensen & Raynor (2003) が解の処方箋を提供、Christensen, Raynor & McDonald (2015) HBR 論文で概念を再厳密化。Lepore (2014) The Disruption Machine が代表的批判。ローエンド破壊・新市場破壊・Job-to-be-Done、モジュラリティ理論 (Baldwin-Clark)、S-カーブ、Big Bang Disruption (Downes-Nunes) が中心概念群。'),
    ('subscription_saas', 'サブスクリプション・SaaSモデル',
     'Hagiu (2014) の MSP 戦略決定論文が学術基盤、Tzuo (2018) のサブスクリプション経済が大衆化、Mehta ら (2020) のカスタマーサクセスが運用論を確立。Iansiti & Lakhani (2017) のハブエコノミー批判が規制視点。LTV、CAC、チャーン、NRR、PLG、使用量ベース価格が中心メトリクス。実務先行で学術理論はキャッチアップ中。'),
    ('sustainable_bm', 'サステナビリティ・循環型ビジネスモデル',
     'Stubbs & Cocklin (2008) が概念化、Bocken ら (2014) が 8 アーキタイプで標準分類、Geissdoerfer ら (2018) が現代的レビュー、Hahn ら (2015) がトレードオフ視点で批判。Triple Bottom Line (Elkington)、サーキュラーエコノミー (Ellen MacArthur)、共有価値 (Porter-Kramer)、再生型ビジネス、ドーナツ経済学 (Raworth)、ステークホルダー理論 (Freeman) が中心概念。EU 政策と整合。'),
    ('channel_gtm', '販売チャネル・GTM戦略',
     'Stern (1969) の行動次元論が起点、Anderson & Coughlan (1987) が国際参入チャネル選択を取引コスト論で分析、Ailawadi & Farris (2017) がオムニチャネル管理を体系化、Webb (2002) が EC 時代のチャネル摩擦を批判的に分析。流通強度、ディスインターメディエーション/リインターメディエーション、チャネルパートナープログラム、カニバリゼーション、GTM デザインピラミッドが中心概念。'),
    ('b2b_enterprise', 'B2B・エンタープライズ営業開発',
     'Webster & Wind (1972) の組織購買行動モデルが理論基盤、Rackham (1988) の SPIN セリングが実証研究ベースの営業実務、Adamson, Dixon & Toman (2011) の Challenger Sale が現代的主流、Sheth & Sharma (2008) が関係性営業の限界を批判。ABM、ソリューション営業、MEDDIC、Value-Based Selling、Sales Enablement、RevOps が現代実務の中心。'),
    ('ma_corp_dev', 'M&A・コーポレートデベロップメント',
     'Haspeslagh & Jemison (1991) の統合 4 類型 (Preservation/Symbiosis/Absorption/Holding) が古典的フレーム、Capron (1999) が水平買収の長期業績を実証、King, Bauer & Schriber (2018) が現代レビュー、Cartwright & Schoenberg (2006) が 30 年研究で 50%+ の M&A 失敗率を示した。アクハイヤー、スピンオフ、CVC、買収プレミアム、SPAC が現代の中心トピック。'),
]

sf_entries = {}
for e in all_entries:
    sf_entries.setdefault(e[5], []).append(e)

now = datetime.datetime.now().strftime("%Y-%m-%d")

html = f"""<!DOCTYPE html>
<html lang="ja"><head>
<meta charset="UTF-8">
<title>事業開発・BMI 学術サーベイ (Phase 1 MVP)</title>
<style>
body{{font-family:-apple-system,'Hiragino Sans','Yu Gothic',sans-serif;max-width:920px;margin:0 auto;padding:32px;color:#1a202c;line-height:1.85}}
h1{{font-size:30px;border-bottom:3px solid #2c5282;padding-bottom:12px}}
h2{{font-size:22px;color:#2c5282;margin-top:48px;border-left:5px solid #2c5282;padding-left:12px}}
h3{{font-size:17px;color:#2d3748;margin-top:28px}}
p{{text-align:justify}}
.toc{{background:#f7fafc;border:1px solid #e2e8f0;padding:20px 28px;border-radius:8px;margin:24px 0}}
.toc ol{{margin:0;padding-left:24px}}
.toc li{{padding:3px 0}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin:16px 0}}
th,td{{border:1px solid #e2e8f0;padding:8px}}
th{{background:#edf2f7}}
.canon{{background:#fff8dc;border-left:4px solid #d69e2e;padding:14px 18px;margin:14px 0;border-radius:4px}}
.canon-title{{font-weight:bold;color:#744210;margin-bottom:8px}}
code{{background:#edf2f7;padding:2px 5px;border-radius:3px;font-size:13px}}
.metaline{{color:#718096;font-size:12px;margin-top:24px;padding-top:12px;border-top:1px solid #e2e8f0}}
</style></head><body>

<h1>事業開発・ビジネスモデル開発 学術サーベイ</h1>
<p style="color:#666;font-size:14px">Business Development & Business Model Innovation — Academic Knowledge Survey (Phase 1 MVP, {now} 時点)</p>

<h2>はじめに</h2>
<p>本書は事業開発 (Business Development) とビジネスモデルイノベーション (BMI) の学術領域を、戦略経営学・イノベーション・マネジメント・アントレプレナーシップの交差点に位置づけて 14 のサブフィールドに整理した知識基盤である。Phase 1 MVP として 140 概念・399 関係を体系化し、各サブフィールドに「創設者・転換点・現代的発展・主要批判」の 4 軸で必須理論を確保した。Phase 2 拡張で 5,000-10,000 件規模への scaling を予定する。</p>

<p>事業開発は実務的・応用的色彩が強い領域であり、学術文献と実務文献が交錯する。本書ではこの両軸を統合し、各サブフィールドで Magretta (2002)・Christensen (1997)・Chesbrough (2003)・Ries (2011)・Osterwalder & Pigneur (2010) のような節目となるアンカー文献を起点として知識を組織化した。</p>

<h2>目次</h2>
<div class="toc"><ol>
<li>はじめに</li>
"""

for i, (sf, name, _) in enumerate(sf_meta, start=1):
    html += f"<li>第 {i} 章: {name}</li>\n"

html += "<li>結語: 14 領域の統合的展望</li>\n"
html += "</ol></div>\n"

# 各章
for i, (sf, name, intro) in enumerate(sf_meta, start=1):
    html += f"<h2>第 {i} 章: {name}</h2>\n"
    html += f"<p>{intro}</p>\n"

    # canonical references
    canon = []
    for e in sf_entries[sf]:
        if e[6] in ('Foundational BM Theory','BMI Process Theory','Platform Economics','Relational View',
                    'Process Model','Disruption Theory','Open Innovation Theory','Lean Startup',
                    'Customer Development','Subscription Economy','Sustainable BM Foundation',
                    'Channel Behavior','Organizational Buying','Integration Typology','Growth Matrix'):
            canon.append(e)

    if canon:
        html += '<div class="canon"><div class="canon-title">基幹アンカー文献</div>\n<ul>\n'
        for c in canon[:3]:
            ja, en, df = c[1], c[2], c[3]
            html += f"<li><strong>{ja}</strong> ({en}) — {df[:120]}</li>\n"
        html += '</ul></div>\n'

    # 概念表
    html += "<h3>主要概念一覧</h3>\n<table>\n"
    html += "<tr><th>ID</th><th>名称</th><th>年代</th><th>学派</th></tr>\n"
    for e in sf_entries[sf]:
        html += f"<tr><td><code>{e[0]}</code></td><td>{e[1]} <em>({e[2]})</em></td><td>{e[7]}</td><td>{e[6]}</td></tr>\n"
    html += "</table>\n"

# 結語
html += """
<h2>結語: 14 領域の統合的展望</h2>
<p>14 のサブフィールドは独立した知識領域でありながら、相互に深く接続している。たとえばビジネスモデル理論 (第 1 章) は BMI プロセス (第 2 章) を媒介に動的能力論 (Teece) と接続し、それはオープンイノベーション (第 7 章) の Open BM 概念へと接続する。同様に、破壊的イノベーション (第 9 章) のジョブ理論はリーンスタートアップ (第 8 章) の顧客開発と整合し、サブスクリプション・SaaS (第 10 章) のプロダクトレッドグロースは B2B 営業 (第 13 章) の Account-Based Marketing と並走する。</p>

<p>サステナビリティ BM (第 11 章) はトリプルボトムライン以来の長い系譜を持ちつつ、近年は循環型・再生型ビジネスへと進化し、2020 年代に主流概念へと躍り出た。M&A (第 14 章) は Cartwright-Schoenberg (2006) が示した 50%+ の失敗率という冷厳な事実を踏まえ、文化的フィット・統合プロセスの理解が引き続き重要である。</p>

<p>現代の事業開発実務は、これら 14 領域の知識を統合的に活用することで、より高い再現性と精緻さを得る。本書は単なる用語集ではなく、戦略経営学とイノベーション・マネジメントが交錯する事業開発という応用領域の地図 (mapping) としての役割を意図している。Phase 2 では 5,000-10,000 件規模の概念ネットワークへの拡張、引用文献データベースとの cross-domain 接続、および分野固有の case-company マッピングが計画されている。</p>

<p class="metaline">
本書は AI ベースの自動知識構築パイプライン (academic-db-build) によって生成された Phase 1 MVP である。<br>
生成日: """ + now + """ | エントリ数: 140 | 関係数: 399 | サブフィールド数: 14<br>
本格スケール (5,000-10,000 件) への拡張、および学術検証 (Phase 6) を Phase 2 以降で実施予定。
</p>

</body></html>
"""

with open('/tmp/academic-build/business_development_bm_textbook.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"textbook written ({len(html)} chars)")
conn.close()
