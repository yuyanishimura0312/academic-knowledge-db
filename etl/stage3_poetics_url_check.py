"""Stage 3 (rite-editorial-renewal): re-check poetics source URLs into add-on table poetics_url_check.
alive = 2xx; dead = 404/410 only; everything else (403/429/5xx/timeout/DNS) = unreachable.
Resumable: URLs already in poetics_url_check are skipped. Existing columns are never touched.
Usage: python3 stage3_poetics_url_check.py [--limit N] [--workers 4]
"""
import sqlite3, sys, time, threading, urllib.request, urllib.error, urllib.parse, json, datetime, queue

DB = "/Users/nishimura+/projects/research/academic-knowledge-db/academic.db"
UA = "Mozilla/5.0 (compatible; ak-quality-worker url-check; contact esse.miratuku@gmail.com)"
args = sys.argv[1:]
limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
workers = min(4, int(args[args.index("--workers") + 1])) if "--workers" in args else 4

conn = sqlite3.connect(DB, timeout=60)
conn.execute("PRAGMA busy_timeout=60000")
conn.execute("""CREATE TABLE IF NOT EXISTS poetics_url_check(
 id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL, source_tables TEXT, row_count INTEGER,
 status TEXT NOT NULL CHECK(status IN('alive','dead','unreachable')),
 http_status INTEGER, final_url TEXT, error TEXT, method TEXT,
 alt_url TEXT, alt_checked_at TEXT, checked_at TEXT NOT NULL, checked_by TEXT)""")
conn.execute("CREATE INDEX IF NOT EXISTS idx_puc_url ON poetics_url_check(url)")
conn.commit()
rows = conn.execute("""select url, group_concat(t), sum(n) from (
 select source_url url,'poetics_text' t,count(*) n from poetics_text where source_url<>'' group by 1
 union all select source_url,'concept_original_source',count(*) from concept_original_source where source_url<>'' group by 1)
 group by url""").fetchall()
done = {r[0] for r in conn.execute("select url from poetics_url_check")}
todo = [r for r in rows if r[0] not in done]
import random
random.Random(20261104).shuffle(todo)  # interleave hosts so 4 workers are not serialized on one host
if limit:
    todo = todo[:limit]
print("total", len(rows), "done", len(done), "todo", len(todo), flush=True)

host_lock = {}
host_last = {}
glock = threading.Lock()


def throttle(host):
    with glock:
        l = host_lock.setdefault(host, threading.Lock())
    with l:
        w = host_last.get(host, 0) + 1.1 - time.time()
        if w > 0:
            time.sleep(w)
        host_last[host] = time.time()


def fetch(url):
    host = urllib.parse.urlparse(url).netloc
    last = None
    for method in ("HEAD", "GET"):
        throttle(host)
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                code = r.getcode()
                final = r.geturl()
                if method == "GET":
                    r.read(1024)
                return code, final, None, method
        except urllib.error.HTTPError as e:
            last = (e.code, None, "HTTPError %s" % e.code, method)
            if method == "HEAD" and e.code in (403, 405, 400, 404, 429, 500, 501, 503):
                continue  # confirm with GET (some servers mishandle HEAD); never decide dead from HEAD alone
            return last
        except Exception as e:
            last = (None, None, "%s: %s" % (type(e).__name__, str(e)[:120]), method)
            if method == "HEAD":
                continue
            return last
    return last


def classify(code):
    if code is None:
        return "unreachable"
    if 200 <= code < 300:
        return "alive"
    if code in (404, 410):
        return "dead"
    return "unreachable"


def wayback(url):
    throttle("archive.org-api")
    try:
        q = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
        with urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": UA}), timeout=20) as r:
            j = json.load(r)
        s = j.get("archived_snapshots", {}).get("closest")
        if s and s.get("available"):
            return s["url"]
    except Exception:
        pass
    return None


q = queue.Queue()
res = queue.Queue()
for r in todo:
    q.put(r)


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def work():
    while True:
        try:
            url, tabs, n = q.get_nowait()
        except queue.Empty:
            return
        code, final, err, m = fetch(url)
        st = classify(code)
        alt = altat = None
        if st == "dead":
            alt = wayback(url)
            altat = now()
        res.put((url, tabs, n, st, code, final, err, m, alt, altat, now()))


ths = [threading.Thread(target=work, daemon=True) for _ in range(workers)]
for t in ths:
    t.start()
cnt = 0
buf = []


def flush():
    global buf
    if buf:
        conn.executemany("insert into poetics_url_check(url,source_tables,row_count,status,http_status,final_url,error,method,alt_url,alt_checked_at,checked_at,checked_by) values(?,?,?,?,?,?,?,?,?,?,?,'ak-quality-worker stage3')", buf)
        conn.commit()
        buf = []


while any(t.is_alive() for t in ths) or not res.empty():
    try:
        buf.append(res.get(timeout=2))
        cnt += 1
    except queue.Empty:
        continue
    if len(buf) >= 100:
        flush()
        print("saved", cnt, flush=True)
flush()
print("finished", cnt)
