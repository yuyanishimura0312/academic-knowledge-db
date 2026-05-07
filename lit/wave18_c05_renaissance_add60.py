"""LIT-DB Wave 18 — C05 Renaissance ADD 60 NEW concepts (subfield_id=3)."""
from __future__ import annotations
import sys
from lit_db_helper import LitDB, LitDBError

PERIODS = [
    ("イタリア・ルネサンス期", "Italian Renaissance", 1300, 1600,
     "ペトラルカ以降のイタリア俗語人文主義文学。"),
    ("スペイン黄金時代", "Spanish Golden Age (Siglo de Oro)", 1500, 1681,
     "ガルシラーソからカルデロンに至るスペイン文学黄金期。"),
    ("フランス・ルネサンス期", "French Renaissance", 1494, 1610,
     "ラブレー〜モンテーニュ〜ドービニェの仏俗語文学。"),
    ("テューダー・ジャコビアン期", "Tudor and Jacobean England", 1485, 1660,
     "シドニー〜ミルトンに至る英語文芸の最初の頂点。"),
    ("北方ルネサンス期", "Northern Renaissance", 1450, 1650,
     "エラスムス〜フォンデルらの独蘭語人文主義。"),
    ("バロック・後期ルネサンス期", "Late Renaissance / Baroque", 1580, 1700,
     "ゴンゴラ・マリーノ・スキュデリらバロック移行期。"),
]

LIBER = "https://www.liberliber.it/"
BVMC = "https://www.cervantesvirtual.com/"
FRANTEXT = "https://www.frantext.fr/"
GALLICA = "https://gallica.bnf.fr/"
GUTEN = "https://www.gutenberg.org/"
WSRC_IT = "https://it.wikisource.org/wiki/"
WSRC_ES = "https://es.wikisource.org/wiki/"
WSRC_FR = "https://fr.wikisource.org/wiki/"
WSRC_EN = "https://en.wikisource.org/wiki/"
WSRC_DE = "https://de.wikisource.org/wiki/"
WSRC_NL = "https://nl.wikisource.org/wiki/"
DBNL = "https://www.dbnl.org/"

CONCEPTS: list[dict] = []
def add(**e): CONCEPTS.append(e)
C = dict(subfield_code="lit_eu_renaissance", region="西欧", original_script="roman")

# ============== A: Italian Cinquecento extensions (12) ==============
add(**C, name_ja="ロレンツォ・デ・メディチ『カンツォニエーレ』",
    name_en="Lorenzo de'Medici Canzoniere",
    name_original="Canzoniere di Lorenzo de' Medici",
    period_key="イタリア・ルネサンス期",
    definition="ロレンツォ・イル・マニフィコ（1449-92）の俗語抒情詩集。ペトラルキスムをフィレンツェ宮廷に再導入し、新プラトン主義的恋愛詩を結晶化した。",
    background="メディチ統治期フィレンツェ宮廷文化、フィチーノ新プラトン主義サークル。",
    development="ポリツィアーノ・ベンボに継承され、ペトラルキスム規範化の前段階を成した。",
    historical_context="クァトロチェント末メディチ宮廷の文化的最盛期。",
    primary_source_url=LIBER+"libri/m/medici_lorenzo/",
    primary_source_type="Liber Liber: Lorenzo de'Medici",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="サンナザーロ『アルカディア』",
    name_en="Sannazaro Arcadia",
    name_original="Arcadia",
    period_key="イタリア・ルネサンス期",
    definition="ヤコポ・サンナザーロ（1458-1530）が1504年に完成した散文と詩の混在牧歌物語。古代田園牧歌をトスカーナ俗語で再生し、欧州パストラル小説の祖型を成した。",
    background="ナポリ・アラゴン宮廷文化、ウェルギリウス『牧歌』の俗語化志向。",
    development="モンテマヨール『ディアナ』、シドニー『アルカディア』、デュルフェ『アストレ』へ祖型を供給した。",
    historical_context="ナポリ王国の人文主義文化、印刷出版興隆期。",
    primary_source_url=LIBER+"libri/s/sannazaro_jacopo/",
    primary_source_type="Liber Liber: Arcadia",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ベンボ『アゾラーニ』",
    name_en="Bembo Asolani",
    name_original="Gli Asolani",
    period_key="イタリア・ルネサンス期",
    definition="ピエトロ・ベンボが1505年に発表した三巻の対話編。アーゾロ宮廷を舞台に新プラトン主義的恋愛論を俗語で展開し、宮廷恋愛論の規範を成した。",
    background="ヴェネツィア＝アーゾロ宮廷文化、フィチーノ的恋愛哲学の俗語化。",
    development="カスティリオーネ『宮廷人の書』、ペトラルキスム理論化に直接影響した。",
    historical_context="チンクェチェント初期の宮廷恋愛論ブーム。",
    primary_source_url=LIBER+"libri/b/bembo_pietro/",
    primary_source_type="Liber Liber: Gli Asolani",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アレティーノ『対話篇（六日間）』",
    name_en="Aretino Sei giornate / Ragionamenti",
    name_original="Sei giornate / Ragionamenti",
    period_key="イタリア・ルネサンス期",
    definition="ピエトロ・アレティーノが1534-36年に発表した対話形式作品。娼婦の対話を通じ近世ローマ・ヴェネツィアの社会風俗を諷刺し、近代諷刺対話の祖型となった。",
    background="ヴェネツィア印刷文化、近世イタリア娼婦・宮廷文化批判の興隆。",
    development="近代諷刺対話、リベルタン文学（ニコラ・ショリエ等）に系譜的影響を与えた。",
    historical_context="トリエント以前の検閲緩い印刷文化。",
    primary_source_url=LIBER+"libri/a/aretino_pietro/",
    primary_source_type="Liber Liber: Ragionamenti",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベルニ『恋するオルランド改作』",
    name_en="Berni's Rifacimento of Orlando Innamorato",
    name_original="Orlando Innamorato rifatto",
    period_key="イタリア・ルネサンス期",
    definition="フランチェスコ・ベルニ（1497頃-1535）が1541年遺稿刊行した、ボイアルド『恋するオルランド』のトスカーナ語改作。北部俗語版を規範トスカーナに改修し、ベンボ俗語論の実践となった。",
    background="ベンボ俗語規範化運動、トスカーナ語の汎イタリア化。",
    development="アリオスト後期受容に介在し、19世紀までの『恋するオルランド』流通版を成した。",
    historical_context="チンクェチェント中期言語規範化期。",
    primary_source_url=LIBER+"libri/b/berni_francesco/",
    primary_source_type="Liber Liber: Berni Rifacimento",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴァザーリ『芸術家列伝』",
    name_en="Vasari's Vite",
    name_original="Le vite de' più eccellenti pittori, scultori, e architettori",
    period_key="イタリア・ルネサンス期",
    definition="ジョルジョ・ヴァザーリ（1511-74）が1550初版・1568第二版で発表した美術家伝記集。俗語散文による近代芸術史記述の祖型を成し、ルネサンス芸術観の規範を構築した。",
    background="メディチ宮廷文化、人文主義者による芸術家社会的地位向上運動。",
    development="近代美術史学・芸術家伝記ジャンルの祖型を成し、欧州芸術言説全体の基盤となった。",
    historical_context="チンクェチェント中後期フィレンツェ宮廷文化。",
    primary_source_url=LIBER+"libri/v/vasari_giorgio/",
    primary_source_type="Liber Liber: Le Vite",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"AN","link_type":"shared_concept",
        "target_entity_name":"芸術家伝記ジャンル",
        "description":"ヴァザーリは近代芸術社会学・伝記研究の祖型を成す。"}])

add(**C, name_ja="チェッリーニ『自伝』",
    name_en="Cellini Vita",
    name_original="Vita di Benvenuto Cellini",
    period_key="イタリア・ルネサンス期",
    definition="ベンヴェヌート・チェッリーニ（1500-71）が1558-66年に執筆した俗語自伝（1728刊）。彫金家・彫刻家の波乱の生涯を一人称で語り、近代自伝文学の祖型の一つとなった。",
    background="フィレンツェ・ローマ・パリの宮廷工房文化、芸術家自意識の興隆。",
    development="ルソー『告白』、ゲーテによる独語訳（1796）を介し、近代自伝ジャンルへ祖型を供給した。",
    historical_context="チンクェチェント中後期の芸術家社会的地位上昇期。",
    primary_source_url=LIBER+"libri/c/cellini_benvenuto/",
    primary_source_type="Liber Liber: Vita di Cellini",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガリレオの俗語散文",
    name_en="Galileo as literary stylist",
    name_original="prosa volgare di Galileo",
    period_key="イタリア・ルネサンス期",
    definition="ガリレオ・ガリレイ（1564-1642）の『天文対話』(1632)『新科学対話』(1638)等の俗語対話散文。科学を俗語化し、明晰簡潔なトスカーナ散文の規範をもたらした。",
    background="メディチ宮廷文化、対抗改革期検閲の中での俗語選択。",
    development="近代イタリア科学散文・啓蒙散文の規範を成し、レオパルディ・カルドゥッチが文体的祖と称した。",
    historical_context="トリエント後対抗改革期、教皇庁とガリレオ対立。",
    primary_source_url=LIBER+"libri/g/galilei_galileo/",
    primary_source_type="Liber Liber: Galileo",
    importance_score=4, source_tier="primary", canonical_in_region="major",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"科学俗語化",
        "description":"ガリレオは近代科学を俗語化し哲学・文学・科学の境界を流動化させた。"}])

add(**C, name_ja="タッソ『アミンタ』",
    name_en="Tasso Aminta",
    name_original="Aminta",
    period_key="イタリア・ルネサンス期",
    definition="トルクァート・タッソが1573年に発表した牧歌劇。フェッラーラ宮廷で初演され、欧州パストラル劇の規範を成した。グァリーニ『忠実な羊飼い』へ直接影響。",
    background="フェッラーラ・エステ宮廷文化、サンナザーロ『アルカディア』からの牧歌的展開。",
    development="グァリーニ、フランス・スペイン牧歌劇、英国ジョンソン仮面劇に系譜的影響を与えた。",
    historical_context="チンクェチェント末宮廷祝祭文化。",
    primary_source_url=LIBER+"libri/t/tasso_torquato/",
    primary_source_type="Liber Liber: Aminta",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="タッソ『英雄詩論』",
    name_en="Tasso Discorsi del poema eroico",
    name_original="Discorsi del poema eroico",
    period_key="イタリア・ルネサンス期",
    definition="タッソが1594年に発表した英雄叙事詩論。アリストテレス詩学の対抗改革期再解釈で、統一性・キリスト教的崇高・歴史的真実性を統合した近世英雄詩学の規範。",
    background="トリエント公会議後イタリア詩学論争、自身の『解放されたエルサレム』論争。",
    development="ミルトン、後の欧州バロック叙事詩論の祖型を成した。",
    historical_context="対抗改革期イタリアの詩学規範化。",
    primary_source_url=LIBER+"libri/t/tasso_torquato/",
    primary_source_type="Liber Liber: Discorsi",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アリオスト『風刺詩集』",
    name_en="Ariosto Satire",
    name_original="Satire",
    period_key="イタリア・ルネサンス期",
    definition="ルドヴィコ・アリオストが1517-25年に執筆した7篇の三韻句法（terza rima）風刺詩。宮廷生活・自伝的省察を融合し、ホラティウス的諷刺をイタリア俗語に再生した。",
    background="フェッラーラ宮廷の苦渋、ホラティウス『書簡詩』の俗語化志向。",
    development="チンクェチェント風刺詩、近代欧州自伝風刺の祖型を成した。",
    historical_context="イタリア戦争期の宮廷文学者の自意識深化。",
    primary_source_url=LIBER+"libri/a/ariosto_ludovico/",
    primary_source_type="Liber Liber: Satire",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="フィチーノ書簡集",
    name_en="Ficino Epistolae as literature",
    name_original="Epistolae di Ficino",
    period_key="イタリア・ルネサンス期",
    definition="マルシリオ・フィチーノ（1433-99）が1474-94年に執筆したラテン語書簡集（1495刊）。新プラトン主義哲学を文学的書簡として展開し、ルネサンス書簡文学の規範を成した。",
    background="メディチ・プラトン・アカデミー、フィレンツェ人文主義書簡文化。",
    development="エラスムス書簡、欧州人文主義書簡文化の祖型を成した。",
    historical_context="クァトロチェント末メディチ統治下の哲学的書簡文化。",
    primary_source_url=GUTEN+"ebooks/56548",
    primary_source_type="Project Gutenberg: Ficino Letters",
    importance_score=3, source_tier="primary", canonical_in_region="major")

# ============== B: Spanish Golden Age extensions (15) ==============
add(**C, name_ja="『ラサリーリョ・デ・トルメスの生涯』（無名作）",
    name_en="Lazarillo de Tormes (anonymous)",
    name_original="La vida de Lazarillo de Tormes",
    period_key="スペイン黄金時代",
    definition="1554年に複数都市で同時刊行された無名作。盲人の少年ラサロが諸主人を遍歴する一人称悪漢自伝で、近代ピカレスク小説の起点となった。",
    background="16世紀前半カスティーリャ社会の貧困、エラスミアニズムの反偽善精神。",
    development="アレマン、ケベードらピカレスクへ祖型を供給し、近代散文小説形式の規範を成した。",
    historical_context="フェリペ2世初期スペインの社会階層変動と検閲制度形成。",
    primary_source_url=BVMC+"obra/lazarillo-de-tormes/",
    primary_source_type="BVMC: Lazarillo",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マテオ・アレマン『グスマン・デ・アルファラチェ』",
    name_en="Mateo Alemán Guzmán de Alfarache",
    name_original="Guzmán de Alfarache",
    period_key="スペイン黄金時代",
    definition="マテオ・アレマン（1547-1614頃）が1599-1604年に発表した二部構成のピカレスク。悪漢自伝に道徳説教を織り込み、ピカレスク形式を哲学化したベストセラーとなった。",
    background="フェリペ3世期スペインの宗教的内省と社会的危機。",
    development="ケベード『ブスコン』、グリンメルスハウゼン『ジンプリチシムス』への直接影響。",
    historical_context="17世紀初頭スペイン経済危機と道徳的・霊的内省ブーム。",
    primary_source_url=BVMC+"obra/guzman-de-alfarache/",
    primary_source_type="BVMC: Guzmán",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ケベード『ブスコン』",
    name_en="Quevedo El Buscón",
    name_original="Historia de la vida del Buscón",
    period_key="スペイン黄金時代",
    definition="ケベードが1604頃執筆・1626年刊行のピカレスク小説。コンセプティスモ的文体で悪漢ドン・パブロスの遍歴を描き、ピカレスク三部作の頂点を成した。",
    background="フェリペ3-4世期スペイン宮廷諷刺文化。",
    development="近代諷刺小説、特にディケンズ・ゴーゴリへ祖型を供給した。",
    historical_context="17世紀前半スペインの宮廷・知識人諷刺文化。",
    primary_source_url=BVMC+"obra/historia-de-la-vida-del-buscon/",
    primary_source_type="BVMC: El Buscón",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ケベード『夢』",
    name_en="Quevedo Sueños",
    name_original="Los Sueños",
    period_key="スペイン黄金時代",
    definition="ケベードが1605-22年に執筆した5篇の幻視諷刺散文（1627刊）。地獄・最後の審判・名声殿等を舞台に近世スペイン社会を諷刺し、バロック幻視文学を確立した。",
    background="ケベードの宮廷風刺、ルキアノス『真実の物語』の俗語的継承。",
    development="近代諷刺・幻視文学（スウィフト『ガリヴァー旅行記』等）への系譜的影響。",
    historical_context="フェリペ3-4世期スペイン社会の道徳的危機意識。",
    primary_source_url=BVMC+"obra/sueno-del-juicio-final/",
    primary_source_type="BVMC: Sueños",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ケベード『神の政治』",
    name_en="Quevedo Política de Dios",
    name_original="Política de Dios y gobierno de Cristo",
    period_key="スペイン黄金時代",
    definition="ケベードが1626年に発表したキリスト中心主義政治論。マキャヴェリ批判として聖書・キリスト像を君主鑑として展開し、対抗改革期スペイン政治散文の代表となった。",
    background="フェリペ4世オリバレス政権下、マキャヴェリズム反論論争。",
    development="サアヴェドラ・ファハルド等17世紀スペイン政治論に直接影響を与えた。",
    historical_context="三十年戦争期スペイン宮廷の政治神学化。",
    primary_source_url=BVMC+"obra/politica-de-dios/",
    primary_source_type="BVMC: Política de Dios",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="セルバンテス『模範小説集』",
    name_en="Cervantes Novelas Ejemplares",
    name_original="Novelas Ejemplares",
    period_key="スペイン黄金時代",
    definition="ミゲル・デ・セルバンテス（1547-1616）が1613年に発表した12篇の中編小説集。イタリア・ノヴェッラを範に、スペイン風俗・哲学・愛・正義を融合し、近代スペイン中編小説の祖型を成した。",
    background="ボッカッチョ・ノヴェッラ伝統のスペイン受容、宮廷物語文化。",
    development="後の欧州中編小説（フランス・モーパッサン、独ホフマン）へ祖型を供給した。",
    historical_context="フェリペ3世期スペイン宮廷文芸の成熟。",
    primary_source_url=BVMC+"obra/novelas-ejemplares/",
    primary_source_type="BVMC: Novelas Ejemplares",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="セルバンテス『ペルシレスとシヒスムンダ』",
    name_en="Cervantes Persiles y Sigismunda",
    name_original="Los trabajos de Persiles y Sigismunda",
    period_key="スペイン黄金時代",
    definition="セルバンテスが死後1617年に刊行された遺作。ヘリオドロス『エチオピア物語』を範に北欧・地中海を舞台にした遍歴ロマンスで、近世ロマンス・ジャンルの集大成となった。",
    background="古代ギリシア恋愛ロマンスの近世受容、対抗改革期巡礼文学。",
    development="後の欧州ロマンス、近代冒険小説に系譜的影響を与えた。",
    historical_context="セルバンテス晩年（1616没）の総合志向。",
    primary_source_url=BVMC+"obra/los-trabajos-de-persiles-y-sigismunda/",
    primary_source_type="BVMC: Persiles",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="セルバンテス『ガラテア』",
    name_en="Cervantes La Galatea",
    name_original="La Galatea",
    period_key="スペイン黄金時代",
    definition="セルバンテスが1585年に発表した牧歌物語。サンナザーロ・モンテマヨールを範に、田園的恋愛詩と散文を融合し、セルバンテス散文芸術の出発点となった。",
    background="モンテマヨール『ディアナ』のスペイン牧歌伝統、サンナザーロ『アルカディア』。",
    development="セルバンテスは『ドン・キホーテ』内でも『ガラテア』を自己言及し、後の欧州牧歌物語に影響。",
    historical_context="フェリペ2世期スペイン宮廷文芸サークル。",
    primary_source_url=BVMC+"obra/la-galatea/",
    primary_source_type="BVMC: La Galatea",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="セルバンテス『幕間劇集』",
    name_en="Cervantes Entremeses",
    name_original="Entremeses",
    period_key="スペイン黄金時代",
    definition="セルバンテスが1615年に発表した8篇の短い喜劇『幕間劇集』。コメディア・ヌエバ幕間に挿入される短劇形式で、近世スペイン民衆喜劇の精華を成した。",
    background="ロペ的コメディアの幕間慣行、民衆喜劇文化。",
    development="近代スペイン短劇（サイネテ）、後の欧州短編喜劇形式へ系譜的影響。",
    historical_context="フェリペ3世期マドリードの劇場文化。",
    primary_source_url=BVMC+"obra/entremeses/",
    primary_source_type="BVMC: Entremeses",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロペ・デ・ベガ『フエンテ・オベフナ』",
    name_en="Lope Fuente Ovejuna",
    name_original="Fuente Ovejuna",
    period_key="スペイン黄金時代",
    definition="ロペ・デ・ベガが1612-14頃執筆した三幕戯曲（1619刊）。村が領主の暴虐に集団的に抵抗する歴史劇で、集団主人公概念により近代政治演劇の祖型となった。",
    background="フェリペ3世期スペイン社会、農民暴動の歴史記憶。",
    development="20世紀ガルシア・ロルカ、ブレヒト、現代政治演劇に再評価された。",
    historical_context="17世紀前半スペイン宮廷劇場の社会主題化。",
    primary_source_url=BVMC+"obra/fuente-ovejuna/",
    primary_source_type="BVMC: Fuente Ovejuna",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ロペ『オルメドの騎士』",
    name_en="Lope El caballero de Olmedo",
    name_original="El caballero de Olmedo",
    period_key="スペイン黄金時代",
    definition="ロペが1620-25頃執筆した三幕戯曲（1641刊）。民謡を骨格に運命愛・予感を融合し、ロペ後期の悲喜混淆劇の代表作となった。",
    background="スペイン民謡・ロマンセ伝統と宮廷演劇の融合。",
    development="20世紀演劇研究で黄金時代演劇の象徴的作品として再評価された。",
    historical_context="フェリペ4世期マドリード劇場文化。",
    primary_source_url=BVMC+"obra/el-caballero-de-olmedo/",
    primary_source_type="BVMC: Olmedo",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ロペ『庭師の犬』",
    name_en="Lope El perro del hortelano",
    name_original="El perro del hortelano",
    period_key="スペイン黄金時代",
    definition="ロペが1613-15頃執筆した三幕喜劇（1618刊）。階層差ある男女の愛と機知を巡る宮廷喜劇で、コメディア・ヌエバ宮廷喜劇の頂点。",
    background="フェリペ3世期マドリード宮廷喜劇文化。",
    development="近世ヨーロッパ宮廷喜劇への祖型を成し、20世紀映画化（1996）でも再評価された。",
    historical_context="17世紀前半マドリード宮廷文化。",
    primary_source_url=BVMC+"obra/el-perro-del-hortelano/",
    primary_source_type="BVMC: El perro del hortelano",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ルイス・デ・アラルコン『嘘つき男』",
    name_en="Ruiz de Alarcón La verdad sospechosa",
    name_original="La verdad sospechosa",
    period_key="スペイン黄金時代",
    definition="フアン・ルイス・デ・アラルコン（1581頃-1639）が1619-21頃執筆した三幕喜劇。嘘癖の男の没落を描く道徳喜劇で、コルネイユ『嘘つき男』(1644)の直接的源泉となった。",
    background="メキシコ生まれ・スペイン宮廷活動のクリオーリョ作家、コメディア・ヌエバ伝統。",
    development="コルネイユ仏訳を介して仏国古典喜劇に直接影響、ゴルドーニ等にも系譜的影響。",
    historical_context="17世紀前半スペイン宮廷とニュー・スペインの文化交流。",
    primary_source_url=BVMC+"obra/la-verdad-sospechosa/",
    primary_source_type="BVMC: La verdad sospechosa",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ソル・フアナ『プリメロ・スエーニョ』",
    name_en="Sor Juana Primero Sueño",
    name_original="Primero Sueño",
    period_key="スペイン黄金時代",
    definition="ソル・フアナ・イネス・デ・ラ・クルス（1648-95）が1685頃執筆した975行の哲学詩。ゴンゴラ的バロック詩法で霊魂の知的昇天を描き、ヌエバ・エスパーニャ詩の頂点となった。",
    background="メキシコ修道院、宮廷詩文化、ゴンゴラ・クルテラニスモ受容。",
    development="20世紀パス『ソル・フアナ・イネス・デ・ラ・クルス論』により世界文学的評価確立。",
    historical_context="17世紀後半ヌエバ・エスパーニャの女性宗教知識人文化。",
    primary_source_url=BVMC+"obra/primero-sueno/",
    primary_source_type="BVMC: Primero Sueño",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"バロック認識論詩",
        "description":"ソル・フアナの哲学詩は近世女性哲学の重要事例として研究される。"}])

add(**C, name_ja="ソル・フアナ『ソル・フィロテア宛て返書』",
    name_en="Sor Juana Respuesta a Sor Filotea",
    name_original="Respuesta a Sor Filotea de la Cruz",
    period_key="スペイン黄金時代",
    definition="ソル・フアナが1691年に執筆した自伝的書簡。プエブラ司教の検閲に対し女性の知的権利を雄弁に擁護し、近世女性知識人の自伝・弁明文学の頂点を成した。",
    background="メキシコ教会階層との緊張、女性修道者の知的活動への規制強化。",
    development="20世紀フェミニスト批評で再評価され、ラテンアメリカ女性文学の祖型として確立された。",
    historical_context="17世紀末ヌエバ・エスパーニャ宗教権力と知的女性の対立。",
    primary_source_url=BVMC+"obra/respuesta-de-la-poetisa-a-la-muy-ilustre-sor-filotea-de-la-cruz/",
    primary_source_type="BVMC: Respuesta",
    importance_score=5, source_tier="primary", canonical_in_region="core")

# ============== C: French Renaissance extensions (10) ==============
add(**C, name_ja="ロンサール『恋愛詩集』",
    name_en="Ronsard Amours",
    name_original="Les Amours",
    period_key="フランス・ルネサンス期",
    definition="ピエール・ド・ロンサール（1524-85）が1552年初版で発表したカッサンドル・マリー・エレーヌに捧げる三大恋愛詩集。ペトラルキスムを仏俗語に移植し、仏抒情詩の規範を成した。",
    background="プレイヤード派詩学運動、ペトラルキスムの仏受容。",
    development="マレルブ古典主義、後の仏抒情詩・象徴主義詩への系譜的影響。",
    historical_context="アンリ2世期仏宮廷詩学黄金期。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71081k",
    primary_source_type="Gallica: Ronsard Amours",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="デュ・ベレー『悔恨詩集』",
    name_en="Du Bellay Les Regrets",
    name_original="Les Regrets",
    period_key="フランス・ルネサンス期",
    definition="ジョアシャン・デュ・ベレー（1522-60）が1558年に発表した191篇のソネット集。ローマ滞在の幻滅と望郷を抒情的・諷刺的に展開し、仏ソネット文学の頂点を成した。",
    background="ローマ教皇庁滞在経験、デュ・ベレーの『古代詩集』『フランス語の擁護と顕揚』との連動。",
    development="近代仏ソネット詩、特にボードレール『パリの憂鬱』への祖型的影響。",
    historical_context="アンリ2世期仏=伊文化交流とローマ批判の交差。",
    primary_source_url=FRANTEXT+"catalogue.php?id=dubellay",
    primary_source_type="Frantext: Les Regrets",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="モーリス・セーヴ『デリー』",
    name_en="Maurice Scève Délie",
    name_original="Délie, object de plus haulte vertu",
    period_key="フランス・ルネサンス期",
    definition="モーリス・セーヴ（1501頃-64頃）が1544年に発表した449篇のディザン詩集（10行詩）。リヨン派の哲学的・象徴的恋愛詩の頂点で、新プラトン主義恋愛論を仏語結晶化した。",
    background="リヨン派詩人サークル、フィチーノ新プラトン主義の仏受容。",
    development="20世紀ヴァレリー・ジュフ等によりモダニズム的に再評価された。",
    historical_context="16世紀中葉リヨンの印刷・文芸文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k1100506",
    primary_source_type="Gallica: Délie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョデル『捕えられたクレオパトラ』",
    name_en="Jodelle Cléopâtre captive",
    name_original="Cléopâtre captive",
    period_key="フランス・ルネサンス期",
    definition="エティエンヌ・ジョデル（1532-73）が1553年初演した仏初の人文主義悲劇。セネカ的悲劇形式を仏語に移植し、近代仏悲劇の起点となった。",
    background="プレイヤード派、セネカ悲劇の仏俗語化志向。",
    development="ガルニエ、ロベール・ガルニエら経由でコルネイユ・ラシーヌ仏古典悲劇へ祖型を供給。",
    historical_context="アンリ2世期仏宮廷の人文主義演劇試行期。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k1521133n",
    primary_source_type="Gallica: Cléopâtre captive",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ガルニエ仏人文主義悲劇",
    name_en="Garnier humanist tragedy",
    name_original="tragédies de Robert Garnier",
    period_key="フランス・ルネサンス期",
    definition="ロベール・ガルニエ（1545-90）が1568-83年に発表した『マルク・アントワーヌ』『イポリット』『セデシ』等の悲劇群。セネカ的修辞悲劇を成熟させ、仏古典悲劇の直接的先行を成した。",
    background="プレイヤード詩学、宗教戦争期の悲劇的世界観。",
    development="メアリ・ハーバート英訳を介し英国宮廷悲劇にも影響、コルネイユ・ラシーヌの直接前駆。",
    historical_context="フランス宗教戦争期の人文主義劇試行。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71098f",
    primary_source_type="Gallica: Garnier",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ラブレー『第四の書』",
    name_en="Rabelais Quart Livre",
    name_original="Le Quart Livre",
    period_key="フランス・ルネサンス期",
    definition="ラブレーが1552年に発表した『パンタグリュエル物語』第四巻。航海ロマンス形式で諸島を巡り、対抗改革期教会・スコラ哲学を諷刺した。",
    background="フランソワ1世末・アンリ2世初期の宗教論争激化。",
    development="近代航海諷刺文学（スウィフト『ガリヴァー旅行記』）への祖型的影響。",
    historical_context="16世紀中葉仏宗教戦争前夜の検閲環境。",
    primary_source_url=FRANTEXT+"catalogue.php?id=rabelais",
    primary_source_type="Frantext: Quart Livre",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カルヴァン『キリスト教綱要』仏版",
    name_en="Calvin Institution chrétienne (French)",
    name_original="Institution de la religion chrétienne",
    period_key="フランス・ルネサンス期",
    definition="ジャン・カルヴァン（1509-64）が1541年に自ら仏訳した『キリスト教綱要』。明晰な仏語神学散文の規範を成し、近代仏散文の出発点の一つとなった。",
    background="仏宗教改革、ジュネーヴ亡命、神学俗語化志向。",
    development="近代仏散文文体の規範を成し、ラ・ロシュフコー・パスカルへの祖型的影響を持つ。",
    historical_context="16世紀中葉仏宗教戦争前夜のプロテスタント文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k105024s",
    primary_source_type="Gallica: Institution chrétienne",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ペルネット・デュ・ギエ『詩集』",
    name_en="Pernette du Guillet Rymes",
    name_original="Rymes",
    period_key="フランス・ルネサンス期",
    definition="ペルネット・デュ・ギエ（1518頃-45）の遺稿詩集（1545刊）。リヨン派の女性詩人として、セーヴへの応答的恋愛詩を残し、近世仏女性詩の重要事例となった。",
    background="リヨン派詩人サークル、女性知識人文化。",
    development="ルイーズ・ラベと並び、近代仏女性詩史で再評価される重要事例。",
    historical_context="16世紀中葉リヨン女性知識人文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k71019q",
    primary_source_type="Gallica: Rymes",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ベロアルド・ド・ヴェルヴィル『成功の方法』",
    name_en="Béroalde de Verville Moyen de parvenir",
    name_original="Le Moyen de parvenir",
    period_key="フランス・ルネサンス期",
    definition="フランソワ・ベロアルド・ド・ヴェルヴィル（1556-1626）が1610-17頃刊行した諷刺対話集。ラブレー的多様性と対話形式で近世仏社会を諷刺し、リベルタン文学の祖型を成した。",
    background="アンリ4世期仏宮廷諷刺文化、ラブレー継承。",
    development="17世紀仏リベルタン文学（テオフィル・ド・ヴィオー、シラノ）への祖型的影響。",
    historical_context="アンリ4世期仏宮廷の自由主義的文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k68023g",
    primary_source_type="Gallica: Moyen de parvenir",
    importance_score=2, source_tier="primary", canonical_in_region="minor")

add(**C, name_ja="マルグリット・ド・ナヴァール『罪深き魂の鏡』",
    name_en="Marguerite Miroir de l'âme pécheresse",
    name_original="Miroir de l'âme pécheresse",
    period_key="フランス・ルネサンス期",
    definition="マルグリット・ド・ナヴァールが1531年に発表した宗教詩。福音主義的内省を仏俗語詩で展開し、エリザベス1世が少女時代に英訳した重要事例となった。",
    background="フランソワ1世期仏福音主義改革期、宗教論争。",
    development="エリザベス1世英訳を介し英国宗教詩文化にも影響、近世女性宗教詩の祖型。",
    historical_context="16世紀前半仏福音主義改革期、宮廷女性の宗教改革支援。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k710236",
    primary_source_type="Gallica: Miroir de l'âme pécheresse",
    importance_score=3, source_tier="primary", canonical_in_region="major")

# ============== D: English Tudor/Jacobean extensions (12) ==============
add(**C, name_ja="ワイアット＝サリーソネット",
    name_en="Wyatt and Surrey sonnets",
    name_original="Wyatt and Surrey lyrics in Tottel's Miscellany",
    period_key="テューダー・ジャコビアン期",
    definition="トマス・ワイアット（1503-42）とヘンリー・ハワード・サリー伯（1517-47）の宮廷詩。1557年『トテル詞華集』で初公刊され、英ペトラルキスム・ソネットの起点となった。",
    background="ヘンリー8世宮廷文化、ペトラルキスムの英受容。",
    development="エリザベス朝ソネット連作、シドニー・スペンサーへの直接的先駆。",
    historical_context="16世紀前半英宮廷の文化的イタリア化。",
    primary_source_url=GUTEN+"ebooks/16275",
    primary_source_type="Project Gutenberg: Tottel's Miscellany",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="シドニー『アストロフェルとステラ』",
    name_en="Sidney Astrophil and Stella",
    name_original="Astrophil and Stella",
    period_key="テューダー・ジャコビアン期",
    definition="フィリップ・シドニーが1581-83頃執筆した108篇のソネットと11篇の歌からなる連作（1591刊）。英最初のソネット連作で、後の英抒情詩の規範を成した。",
    background="エリザベス朝宮廷文化、ペトラルキスム英規範化志向。",
    development="スペンサー『アモレッティ』、シェイクスピア『ソネット集』への直接前駆。",
    historical_context="1580年代英宮廷詩学運動。",
    primary_source_url=GUTEN+"ebooks/1962",
    primary_source_type="Project Gutenberg: Astrophil and Stella",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="シドニー『アルカディア』",
    name_en="Sidney Arcadia",
    name_original="The Countess of Pembroke's Arcadia",
    period_key="テューダー・ジャコビアン期",
    definition="シドニーが1577-86年に執筆した散文ロマンス（1590新版刊）。サンナザーロ系パストラル散文を英語化し、英散文ロマンスの規範を成した。",
    background="シドニー宮廷文化、サンナザーロ・モンテマヨールの英受容。",
    development="リチャードソン『パメラ』、後の英散文小説への祖型的影響。",
    historical_context="エリザベス朝後期宮廷文化。",
    primary_source_url=GUTEN+"ebooks/1962",
    primary_source_type="Project Gutenberg: Arcadia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マーロウ『フォースタス博士』",
    name_en="Marlowe Doctor Faustus",
    name_original="The Tragical History of Doctor Faustus",
    period_key="テューダー・ジャコビアン期",
    definition="クリストファー・マーロウが1592頃発表した悲劇。ファウスト伝説の最初の英劇化で、ルネサンス的知識欲とその罰の主題を確立した。",
    background="ドイツ・ファウスト本（1587）の英受容、ルネサンス魔術文化。",
    development="ゲーテ『ファウスト』、近代ファウスト文学全体へ祖型を供給。",
    historical_context="エリザベス朝後期英宗教論争・魔術論争。",
    primary_source_url=GUTEN+"ebooks/779",
    primary_source_type="Project Gutenberg: Doctor Faustus",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="マーロウ『マルタ島のユダヤ人』",
    name_en="Marlowe Jew of Malta",
    name_original="The Jew of Malta",
    period_key="テューダー・ジャコビアン期",
    definition="マーロウが1589-90頃執筆の悲劇。マキャヴェリズム・反ユダヤ主義主題を統合し、シェイクスピア『ヴェニスの商人』への直接前駆となった。",
    background="エリザベス朝後期反スペイン・反ユダヤ主義文化、マキャヴェリ受容。",
    development="シェイクスピア『ヴェニスの商人』、後の悪役主役劇形式への影響。",
    historical_context="エリザベス朝後期英外交緊張期。",
    primary_source_url=GUTEN+"ebooks/901",
    primary_source_type="Project Gutenberg: Jew of Malta",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ジョンソン『錬金術師』",
    name_en="Jonson The Alchemist",
    name_original="The Alchemist",
    period_key="テューダー・ジャコビアン期",
    definition="ベン・ジョンソンが1610年初演の喜劇。錬金術詐欺師三人組のロンドン都市喜劇で、体液喜劇形式の頂点を成した。",
    background="ジャコビアン期ロンドン都市文化、錬金術ブーム。",
    development="王政復古期都市喜劇、近代英喜劇の祖型を成した。",
    historical_context="ジェームズ1世期ロンドン劇場・都市文化。",
    primary_source_url=GUTEN+"ebooks/4081",
    primary_source_type="Project Gutenberg: The Alchemist",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ジョンソン仮面劇",
    name_en="Jonson Masques",
    name_original="Jonson Masques",
    period_key="テューダー・ジャコビアン期",
    definition="ベン・ジョンソンがイニゴ・ジョーンズと1605-31年に協作した宮廷仮面劇群（『黒の仮面劇』『ハイメネ』『オベロン』等）。ジャコビアン宮廷祝祭文化を文学化した。",
    background="ジャコビアン期宮廷祝祭文化、イタリア宮廷祝祭の英受容。",
    development="ミルトン『コーマス』、後の英オペラ・宮廷祝祭への祖型。",
    historical_context="ジェームズ1世期宮廷祝祭文化。",
    primary_source_url=GUTEN+"ebooks/5341",
    primary_source_type="Project Gutenberg: Jonson Masques",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ハーリック『ヘスペリデス』",
    name_en="Herrick Hesperides",
    name_original="Hesperides",
    period_key="テューダー・ジャコビアン期",
    definition="ロバート・ハーリック（1591-1674）が1648年に発表した抒情詩集（約1400篇）。ジョンソン詩学を継承し、田園的・カヴァリエ的・古典的抒情を結晶化した。",
    background="チャールズ1世期英宮廷カヴァリエ詩文化。",
    development="近代英抒情詩・カヴァリエ詩学の祖型を成し、19世紀ロマン派により再評価された。",
    historical_context="清教徒革命期の宮廷詩人としての孤立。",
    primary_source_url=GUTEN+"ebooks/22421",
    primary_source_type="Project Gutenberg: Hesperides",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ヴォーン『シレックス・シンティランス』",
    name_en="Vaughan Silex Scintillans",
    name_original="Silex Scintillans",
    period_key="テューダー・ジャコビアン期",
    definition="ヘンリー・ヴォーン（1621-95）が1650-55年に二部刊行の宗教詩集。ハーバート『神殿』を継承し、神秘的自然観・幼年期回帰主題を確立した。",
    background="共和政期英国教会派の内省文化、ハーバート継承。",
    development="ワーズワース『序曲』、19世紀ロマン派幼年期詩学への系譜的祖型。",
    historical_context="共和政期英国教会派の文学的内省化。",
    primary_source_url=GUTEN+"ebooks/1397",
    primary_source_type="Project Gutenberg: Silex Scintillans",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ミルトン『コーマス』",
    name_en="Milton Comus",
    name_original="A Mask Presented at Ludlow Castle (Comus)",
    period_key="テューダー・ジャコビアン期",
    definition="ジョン・ミルトン（1608-74）が1634年初演の宮廷仮面劇。貞潔の擬人化と魔法主コーマスの試みを描き、ジョンソン仮面劇伝統の頂点となった。",
    background="ジャコビアン宮廷仮面劇伝統、清教徒倫理の劇化。",
    development="ミルトン後期叙事詩の倫理主題の前駆、近代英仮面劇の頂点。",
    historical_context="チャールズ1世期英宮廷文化。",
    primary_source_url=GUTEN+"ebooks/608",
    primary_source_type="Project Gutenberg: Comus",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="ミルトン『アレオパジティカ』",
    name_en="Milton Areopagitica",
    name_original="Areopagitica",
    period_key="テューダー・ジャコビアン期",
    definition="ミルトンが1644年に発表した出版自由擁護論。議会の出版検閲法に反対する古典的雄弁体散文で、近代言論自由論の祖型を成した。",
    background="清教徒革命期出版検閲制度、ミルトンの離婚論争経験。",
    development="近代欧米言論自由論（J.S.ミル『自由論』等）の祖型として継承された。",
    historical_context="清教徒革命期英出版自由論争。",
    primary_source_url=GUTEN+"ebooks/608",
    primary_source_type="Project Gutenberg: Areopagitica",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"言論自由論",
        "description":"アレオパジティカは近代政治哲学の言論自由論の祖型。"}])

# ============== E: Northern + cross-Renaissance (5) ==============
add(**C, name_ja="エラスムス『格言集』",
    name_en="Erasmus Adagia",
    name_original="Adagia",
    period_key="北方ルネサンス期",
    definition="エラスムスが1500-36年に増補刊行したラテン語格言集（最終版4151項目）。古典格言を注釈付きで収録し、北方人文主義の知的・文体規範を提供した。",
    background="北方人文主義の古典学術運動、印刷文化興隆。",
    development="近世欧州人文主義教育の規範教材、後のコモンプレイス・ブック文化の祖型。",
    historical_context="16世紀前半欧州印刷文化と古典学術の興隆。",
    primary_source_url=GUTEN+"ebooks/41068",
    primary_source_type="Project Gutenberg: Adagia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="エラスムス『対話集』",
    name_en="Erasmus Colloquia",
    name_original="Colloquia familiaria",
    period_key="北方ルネサンス期",
    definition="エラスムスが1518-33年に増補刊行したラテン語対話集。日常会話形式で諷刺・宗教批判・教育論を展開し、近代諷刺対話の祖型となった。",
    background="北方人文主義教育、ラテン語学習教材としての対話文化。",
    development="近世欧州諷刺対話、近代教育会話書（モロー、コメニウス）の祖型。",
    historical_context="宗教改革論争期の北方人文主義文化。",
    primary_source_url=GUTEN+"ebooks/14031",
    primary_source_type="Project Gutenberg: Colloquia",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="トマス・モア『ユートピア』",
    name_en="Thomas More Utopia",
    name_original="Utopia / De optimo rei publicae statu",
    period_key="北方ルネサンス期",
    definition="トマス・モア（1478-1535）が1516年に発表したラテン語政治哲学物語。理想国家ユートピアを描き、近代ユートピア文学・社会思想の祖型を成した。",
    background="北方人文主義、エラスムス交流、ヘンリー8世期英政治批判。",
    development="近代ユートピア文学（カンパネッラ、ベーコン、モリス、現代SF）への祖型を供給。",
    historical_context="16世紀前半英宗教改革前夜の人文主義政治論。",
    primary_source_url=GUTEN+"ebooks/2130",
    primary_source_type="Project Gutenberg: Utopia",
    importance_score=5, source_tier="primary", canonical_in_region="core",
    cross_domain=[{"target_db":"PHIL","link_type":"shared_concept",
        "target_entity_name":"ユートピア政治哲学",
        "description":"モア『ユートピア』は近代ユートピア政治哲学の祖型。"}])

add(**C, name_ja="フォンデル『アムステルダムのヘイスブレヒト』",
    name_en="Vondel Gysbreght van Aemstel",
    name_original="Gysbreght van Aemstel",
    period_key="北方ルネサンス期",
    definition="フォンデルが1637年に発表した蘭語悲劇。アムステルダム・スハウブルフ劇場開幕作で、中世アムステルダム史劇化により蘭オランダ国民演劇の規範となった。",
    background="オランダ黄金時代アムステルダム文化、新劇場開設。",
    development="蘭国民劇の規範を成し、20世紀まで毎年正月公演慣行が続いた。",
    historical_context="オランダ共和国黄金時代アムステルダム都市文化。",
    primary_source_url=DBNL+"tekst/vond001gysb01_01/",
    primary_source_type="DBNL: Gysbreght van Aemstel",
    importance_score=3, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="アンナ・バインス諷刺詩",
    name_en="Anna Bijns satirical poetry",
    name_original="Refereinen van Anna Bijns",
    period_key="北方ルネサンス期",
    definition="アンナ・バインス（1493-1575、アントウェルペン）が1528-67年に三巻刊行した蘭語レフラン詩。反ルター諷刺・宗教論争詩を女性の立場で展開し、近世蘭女性文学の頂点を成した。",
    background="アントウェルペン都市文化、対抗改革期蘭女性知識人文化。",
    development="近世蘭語抒情・諷刺詩、女性宗教詩文化の祖型。",
    historical_context="16世紀蘭宗教改革論争期。",
    primary_source_url=DBNL+"auteurs/auteur/bijn001/",
    primary_source_type="DBNL: Anna Bijns",
    importance_score=3, source_tier="primary", canonical_in_region="major")

# ============== F: Late Renaissance / Baroque transition (6) ==============
add(**C, name_ja="ゴンゴラ『孤独』",
    name_en="Góngora Soledades",
    name_original="Soledades",
    period_key="バロック・後期ルネサンス期",
    definition="ルイス・デ・ゴンゴラが1613年に発表した未完叙事詩。難解クルテラニスモ詩法の頂点で、自然・時間・主体の哲学詩を展開し、20世紀27年世代に再評価された。",
    background="フェリペ3世期コルドバ・マドリード詩文化、クルテラニスモ論争。",
    development="20世紀ガルシア・ロルカら27年世代によるゴンゴラ復権で世界文学化。",
    historical_context="17世紀前半スペイン宮廷詩学論争。",
    primary_source_url=BVMC+"obra/soledades/",
    primary_source_type="BVMC: Soledades",
    importance_score=5, source_tier="primary", canonical_in_region="core")

add(**C, name_ja="ゴンゴラ『ポリフェモとガラテア物語』",
    name_en="Góngora Polifemo",
    name_original="Fábula de Polifemo y Galatea",
    period_key="バロック・後期ルネサンス期",
    definition="ゴンゴラが1612年に発表した63オクターヴァの神話詩。オウィディウス神話をクルテラニスモ詩法で再生し、バロック神話詩の頂点を成した。",
    background="クルテラニスモ実験、オウィディウス神話の俗語結晶化。",
    development="近代スペイン詩・ラテンアメリカ詩への祖型、バロック詩学の規範。",
    historical_context="17世紀前半スペイン宮廷神話詩文化。",
    primary_source_url=BVMC+"obra/fabula-de-polifemo-y-galatea/",
    primary_source_type="BVMC: Polifemo",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マリーノ『アドーネ』",
    name_en="Marino Adone",
    name_original="L'Adone",
    period_key="バロック・後期ルネサンス期",
    definition="ジャンバッティスタ・マリーノ（1569-1625）が1623年に発表した20歌の神話叙事詩。アフロディテとアドニスの愛を題材に、伊バロック詩（マリニズモ）の頂点を成した。",
    background="ナポリ・パリ宮廷文化、コンチェッティスモ詩学。",
    development="マリニズモ運動を欧州バロック詩学に拡散、マリーノ追随者群を生んだ。",
    historical_context="17世紀前半伊・仏宮廷詩学。",
    primary_source_url=LIBER+"libri/m/marino_giovan_battista/",
    primary_source_type="Liber Liber: L'Adone",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="カルデロン『サラメアの市長』",
    name_en="Calderón El alcalde de Zalamea",
    name_original="El alcalde de Zalamea",
    period_key="バロック・後期ルネサンス期",
    definition="カルデロンが1640頃執筆の三幕戯曲。農民市長ペドロ・クレスポによる名誉と正義の劇で、黄金時代名誉劇の頂点となった。",
    background="フェリペ4世期スペイン名誉概念劇、ロペ伝統継承。",
    development="近代スペイン社会劇（ガルシア・ロルカ等）への祖型、20世紀映画化。",
    historical_context="17世紀中葉スペイン社会変動期の名誉概念再考。",
    primary_source_url=BVMC+"obra/el-alcalde-de-zalamea/",
    primary_source_type="BVMC: El alcalde de Zalamea",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="マドレーヌ・ド・スキュデリ『クレリー』",
    name_en="Madeleine de Scudéry Clélie",
    name_original="Clélie, histoire romaine",
    period_key="バロック・後期ルネサンス期",
    definition="マドレーヌ・ド・スキュデリ（1607-1701）が1654-60年に10巻で発表した古代ローマを舞台にする恋愛大河小説。プレシオジテ宮廷文化の頂点で、「テンドルの地図」で名高い。",
    background="ルイ14世期パリ・サロン文化、プレシオジテ運動。",
    development="近代仏小説・心理小説の祖型、後のラファイエット夫人『クレーヴの奥方』への影響。",
    historical_context="17世紀中葉仏宮廷サロン文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k82016p",
    primary_source_type="Gallica: Clélie",
    importance_score=4, source_tier="primary", canonical_in_region="major")

add(**C, name_ja="オノレ・デュルフェ『アストレ』",
    name_en="Honoré d'Urfé Astrée",
    name_original="L'Astrée",
    period_key="バロック・後期ルネサンス期",
    definition="オノレ・デュルフェ（1567-1625）が1607-27年に5部で発表した牧歌大河小説。サンナザーロ・モンテマヨール伝統を仏語結晶化し、17世紀仏宮廷読書文化の規範となった。",
    background="アンリ4世・ルイ13世期仏宮廷牧歌文化。",
    development="プレシオジテ小説、近代仏心理小説への祖型を供給。",
    historical_context="17世紀前半仏宮廷牧歌文化。",
    primary_source_url=GALLICA+"ark:/12148/bpt6k1102023t",
    primary_source_type="Gallica: L'Astrée",
    importance_score=4, source_tier="primary", canonical_in_region="major")


# ============================================================
# Extra fourth_transform tags & cross_domain (top-up)
# ============================================================
EXTRA_FOURTH = [
    ("『ラサリーリョ・デ・トルメスの生涯』（無名作）", "作者性", "rethinking",
     "無名性は近代著者像の擬制を相対化し、AI生成テキストの匿名作者性問題と通底する。",
     "AI生成における匿名作者性"),
    ("マテオ・アレマン『グスマン・デ・アルファラチェ』", "主体", "rethinking",
     "ピカロの一人称悪漢主体は擬似経験の文学的構築であり、AI一人称生成と理論的に共振する。",
     "AIによる擬似経験主体生成"),
    ("ケベード『ブスコン』", "言語", "rethinking",
     "コンセプティスモの濃密語彙圧縮はLLMの語彙過剰生成と構造的に並行する。",
     "AI生成の語彙圧縮"),
    ("セルバンテス『模範小説集』", "物語", "rethinking",
     "短編集の枠組はプロンプト連鎖による物語生成の祖型として読み直される。",
     "AIによる短編連鎖生成"),
    ("ソル・フアナ『ソル・フィロテア宛て返書』", "主体", "rethinking",
     "女性知識人の自己擁護はAI主体性論争（誰が書いているか）と共振する。",
     "AI生成における主体性擁護"),
    ("ソル・フアナ『プリメロ・スエーニョ』", "受容", "rethinking",
     "バロック認識論詩の難解さはAI生成テキストの解釈困難性と並行する古典参照点。",
     "AI生成テキストの認識論的難読性"),
    ("デュ・ベレー『悔恨詩集』", "主体", "rethinking",
     "幻滅・望郷の抒情主体はAI時代の擬制された記憶主体と理論的に通底する。",
     "AI生成における擬似記憶主体"),
    ("モーリス・セーヴ『デリー』", "言語", "rethinking",
     "象徴的・哲学的恋愛詩の難解さはAI生成テキストの象徴過剰と理論的に共振。",
     "AI生成の象徴過剰"),
    ("ミルトン『アレオパジティカ』", "受容", "rethinking",
     "出版自由論はAI生成テキスト規制論争の歴史的祖型として読み直される。",
     "AI生成テキストの規制論"),
    ("マーロウ『フォースタス博士』", "作者性", "rethinking",
     "知識欲とその罰の主題はAI開発倫理（プロメテウス的越境）の文学的祖型。",
     "AI開発の倫理的越境問題"),
    ("ジョンソン『錬金術師』", "真正性", "rethinking",
     "錬金術詐欺の劇化は擬似科学の真正性問題であり、AI生成の真正性論と並行。",
     "AI生成の真正性問題"),
    ("ハーリック『ヘスペリデス』", "言語", "rethinking",
     "古典的抒情の結晶化はAIによる古典様式生成の歴史的対応参照点。",
     "AIによる古典抒情様式生成"),
    ("ヴォーン『シレックス・シンティランス』", "主体", "rethinking",
     "幼年期回帰の内省主体はAI時代の擬制された内省主体生成と理論的に共振。",
     "AI生成における内省主体擬制"),
    ("ゴンゴラ『孤独』", "受容", "rethinking",
     "難解クルテラニスモはAI生成テキストの解釈論的困難性と古典的参照点を成す。",
     "AI生成の解釈論的難読性"),
    ("マリーノ『アドーネ』", "言語", "rethinking",
     "コンチェッティスモ過剰修辞はAI生成の修辞過剰と歴史的対応関係にある。",
     "AI生成の修辞過剰"),
    ("マドレーヌ・ド・スキュデリ『クレリー』", "物語", "rethinking",
     "サロン的長大物語生成はAIの長文物語生成と理論的に共振する古典参照点。",
     "AIによる長文物語生成"),
    ("オノレ・デュルフェ『アストレ』", "物語", "rethinking",
     "牧歌大河小説の連鎖構造はAIによる連続小説生成と古典的構造類比。",
     "AIによる連続小説生成"),
    ("トマス・モア『ユートピア』", "真正性", "rethinking",
     "理想社会の文学的構築はAIによる仮想社会シミュレーションの古典的祖型。",
     "AIによる仮想社会生成"),
    ("ヴァザーリ『芸術家列伝』", "作者性", "rethinking",
     "芸術家伝記の創出はAIが創作主体性をどう記録するかの問題と通底する。",
     "AI創作の作者性記録"),
    ("ガリレオの俗語散文", "言語", "rethinking",
     "科学俗語化はAIによる学術知識の平易化生成と歴史的に対応する。",
     "AIによる学術平易化生成"),
]

EXTRA_CD = [
    ("『ラサリーリョ・デ・トルメスの生涯』（無名作）", "AN", "shared_concept",
     "近世スペイン社会の階層・貧困",
     "無名作は近世スペイン社会の階層・貧困を一人称で記録する民族誌的祖型。"),
    ("マテオ・アレマン『グスマン・デ・アルファラチェ』", "PHIL", "shared_concept",
     "近世道徳哲学",
     "グスマンは近世スペイン道徳哲学の文学的展開として研究される。"),
    ("ケベード『神の政治』", "MG", "shared_concept",
     "近世政治神学",
     "ケベードの政治神学はマキャヴェリ批判の文学的展開として政治思想史研究の対象。"),
    ("セルバンテス『模範小説集』", "PT", "shared_concept",
     "近代中編小説形式",
     "模範小説集は近代欧州中編小説の祖型として物語論研究の中核。"),
    ("ソル・フアナ『プリメロ・スエーニョ』", "PHIL", "shared_concept",
     "バロック認識論",
     "ソル・フアナの哲学詩は近世女性哲学の重要事例として哲学史で研究される。"),
    ("ソル・フアナ『ソル・フィロテア宛て返書』", "AN", "shared_concept",
     "近世女性知識人の自伝・弁明",
     "近世ヌエバ・エスパーニャ女性知識人文化の人類学的事例として研究される。"),
    ("ロンサール『恋愛詩集』", "PT", "shared_concept",
     "ペトラルキスム抒情詩学",
     "ロンサール『恋愛詩集』は欧州抒情詩学の中心研究対象。"),
    ("カルヴァン『キリスト教綱要』仏版", "PHIL", "shared_concept",
     "近代神学・俗語化",
     "カルヴァン仏版は近代神学俗語化の重要事例として宗教哲学史で研究される。"),
    ("シドニー『アストロフェルとステラ』", "PT", "shared_concept",
     "英ソネット連作形式",
     "アストロフェルとステラは英抒情詩・物語論研究の中核。"),
    ("マーロウ『フォースタス博士』", "PHIL", "shared_concept",
     "ファウスト的越境主題",
     "ファウスト主題は近代知識倫理哲学の中心テーマ。"),
    ("ジョンソン仮面劇", "AN", "shared_concept",
     "近世宮廷祝祭文化",
     "ジョンソン仮面劇は近世宮廷祝祭文化の文化人類学的事例。"),
    ("ヴォーン『シレックス・シンティランス』", "PT", "shared_concept",
     "形而上派宗教詩",
     "ヴォーンは形而上派詩学・新批評の中心研究対象。"),
    ("ミルトン『コーマス』", "PHIL", "shared_concept",
     "倫理仮面劇",
     "コーマスは近世倫理哲学の文学的展開として研究される。"),
    ("ゴンゴラ『孤独』", "PT", "shared_concept",
     "バロック詩学の極致",
     "孤独はバロック詩学・現代詩学研究の中心対象。"),
    ("マドレーヌ・ド・スキュデリ『クレリー』", "AN", "shared_concept",
     "プレシオジテ宮廷サロン文化",
     "クレリーは近世仏宮廷サロン文化の人類学的事例。"),
    ("トマス・モア『ユートピア』", "MG", "shared_concept",
     "理想政治体制論",
     "ユートピアは近代政治・経営理論のユートピア的祖型。"),
    ("カルデロン『サラメアの市長』", "AN", "shared_concept",
     "近世名誉概念",
     "サラメアの市長は近世スペイン名誉文化の人類学的事例。"),
    ("オノレ・デュルフェ『アストレ』", "PT", "shared_concept",
     "牧歌大河小説形式",
     "アストレは近代欧州小説形式研究の中心対象。"),
]


def main() -> int:
    name_to_id: dict[str, int] = {}
    fourth_count = cd_count = 0
    with LitDB() as db:
        period_ids: dict[str, int] = {}
        for nj, ne, sy, ey, desc in PERIODS:
            pid = db.get_or_create_period(name_ja=nj, region="西欧",
                                          start_year=sy, end_year=ey,
                                          name_en=ne, description=desc)
            period_ids[nj] = pid

        for raw in CONCEPTS:
            entry = dict(raw)
            fourth_axes = entry.pop("fourth_axes", [])
            cross_domain = entry.pop("cross_domain", [])
            pkey = entry.pop("period_key", None)
            if pkey:
                entry["period_id"] = period_ids[pkey]
            try:
                cid = db.insert_concept(**entry)
            except LitDBError as e:
                print(f"  [error] {entry['name_ja']}: {e}")
                continue
            name_to_id[entry["name_ja"]] = cid
            for ax in fourth_axes:
                try:
                    db.tag_fourth_transform(cid, **ax)
                    fourth_count += 1
                except LitDBError as e:
                    print(f"  [warn] fourth tag failed for {entry['name_ja']}: {e}")
            for cd in cross_domain:
                try:
                    db.insert_cross_domain(
                        lit_entity_type="concept", lit_entity_id=cid,
                        target_db=cd["target_db"], link_type=cd["link_type"],
                        target_entity_id=cd.get("target_entity_id"),
                        target_entity_name=cd.get("target_entity_name"),
                        description=cd.get("description"))
                    cd_count += 1
                except LitDBError as e:
                    print(f"  [warn] cd failed for {entry['name_ja']}: {e}")

        for nm, axis, status, rationale, ai_phen in EXTRA_FOURTH:
            cid = name_to_id.get(nm)
            if cid is None:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE subfield_id=3 AND name_ja=?",
                    (nm,)).fetchone()
                if not row:
                    print(f"  [warn] extra fourth: not found: {nm}")
                    continue
                cid = row[0]
            try:
                db.tag_fourth_transform(cid, axis=axis, status=status,
                                        rationale=rationale,
                                        related_ai_phenomenon=ai_phen)
                fourth_count += 1
            except LitDBError as e:
                print(f"  [warn] extra fourth failed for {nm}: {e}")

        for nm, target_db, link_type, target_name, desc in EXTRA_CD:
            cid = name_to_id.get(nm)
            if cid is None:
                row = db.conn.execute(
                    "SELECT id FROM concepts WHERE subfield_id=3 AND name_ja=?",
                    (nm,)).fetchone()
                if not row:
                    print(f"  [warn] extra cd: not found: {nm}")
                    continue
                cid = row[0]
            try:
                db.insert_cross_domain(
                    lit_entity_type="concept", lit_entity_id=cid,
                    target_db=target_db, link_type=link_type,
                    target_entity_name=target_name, description=desc)
                cd_count += 1
            except LitDBError as e:
                print(f"  [warn] extra cd failed for {nm}: {e}")

        summary = db.progress_summary()
        print(f"[wave18-c05-add60] inserted: {len(name_to_id)} / total: {summary['concepts']}")
        print(f"[wave18-c05-add60] fourth_transform_tags +{fourth_count}; cross_domain +{cd_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
