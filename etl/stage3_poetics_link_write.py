import sqlite3,json,datetime
S="/private/tmp/claude-502/-Users-nishimura-/e6f250b7-e3ab-42b7-9376-7bf8d10c159f/scratchpad/"
res=json.load(open(S+'res.json'))
now=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
db=sqlite3.connect("/Users/nishimura+/projects/research/academic-knowledge-db/academic.db",timeout=120)
db.execute("pragma busy_timeout=120000")
same={k:v[2][0] for k,v in res.items() if v[0]=='same'}
cand={k:v for k,v in res.items() if v[0]=='candidate'}
db.execute("begin immediate")
db.execute("delete from poetics_link_resolved where method='name_en+definition'")
rows=[]
for lid,cid in db.execute("select id,concept_id from poetics_text_concept_link"):
    if cid in same:
        t,i,_=same[cid]; rows.append((lid,cid,t,i,'name_en+definition',now))
db.executemany("insert into poetics_link_resolved values (?,?,?,?,?,?)",rows)
db.execute("update poetics_link_status set status='resolved',checked_at=? where link_id in (select link_id from poetics_link_resolved where method='name_en+definition')",(now,))
db.execute("delete from poetics_link_candidate where method='old_backup_name_en_only'")
for k,v in cand.items():
    for t,i,_ in v[2]:
        nm=db.execute(f"select name_en,subfield from {t} where id=?",(i,)).fetchone()
        db.execute("insert or ignore into poetics_link_candidate values (?,?,?,?,?,?,?,?)",(k,t,i,'old_backup_name_en_only',len(v[2]),nm[0],nm[1],now))
db.commit()
print(len(rows))
print(db.execute("select status,count(*) from poetics_link_status group by 1").fetchall())
print(db.execute("select count(*) from v_poetics_link_usable").fetchone())
print(db.execute("select count(*),count(distinct link_id),count(distinct original_concept_id),count(distinct resolved_table||resolved_id) from poetics_link_resolved").fetchone())
print(db.execute("""select count(*) from poetics_link_resolved r where not exists (select 1 from humanities_concept h where r.resolved_table='humanities_concept' and h.id=r.resolved_id) and not exists (select 1 from arts_question a where r.resolved_table='arts_question' and a.id=r.resolved_id)""").fetchone())
print(db.execute("pragma quick_check").fetchone())
