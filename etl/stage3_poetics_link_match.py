import sqlite3,re,json,collections
S="/private/tmp/claude-502/-Users-nishimura-/e6f250b7-e3ab-42b7-9376-7bf8d10c159f/scratchpad/"
B="/Volumes/Data/backup/moved-from-internal/projects/research/academic-knowledge-db/academic.db.backup-pre-poetics-migration-20260509-012048"
b=sqlite3.connect(f"file:{B}?immutable=1",uri=True)
c=sqlite3.connect("file:/Users/nishimura+/projects/research/academic-knowledge-db/academic.db?mode=ro",uri=True)
n=lambda s:re.sub(r'\s+',' ',(s or '').strip())
used=[r[0] for r in b.execute("select distinct concept_id from poetics_text_concept_link")]
old={}
for t in ('humanities_concept','arts_question'):
    for r in b.execute(f"select id,name_en,definition from {t} where id like 'cp_%'"): old[r[0]]=(t,n(r[1]),n(r[2]))
print(len(used),sum(u in old for u in used))
cur=collections.defaultdict(list)
for t in ('humanities_concept','arts_question'):
    for r in c.execute(f"select id,name_en,definition from {t}"): cur[n(r[1]).lower()].append((t,r[0],n(r[2])))
res={}
for u in used:
    if u not in old: res[u]=('unresolved','not in old',[]);continue
    t,ne,d=old[u]
    ms=cur.get(ne.lower(),[])
    same=[m for m in ms if m[2]==d and d]
    if len(same)==1: res[u]=('same',None,same)
    elif len(same)>1: res[u]=('candidate','multi-same',same)
    elif ms: res[u]=('candidate','name only',ms)
    else: res[u]=('unresolved','none',[])
print(collections.Counter(v[0] for v in res.values()), collections.Counter(v[1] for v in res.values()))
json.dump({k:[v[0],v[1],v[2],old.get(k)] for k,v in res.items()},open(S+'res.json','w'),ensure_ascii=False)
tg=collections.Counter(v[2][0][1] for v in res.values() if v[0]=='same'); print('dup targets',sum(1 for x in tg.values() if x>1))
