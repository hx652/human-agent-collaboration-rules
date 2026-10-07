import sys,json,datetime
from pathlib import Path
sys.dont_write_bytecode=True
from snapshot_lib import snapshot
s=Path('/tmp/hac-20261007-181827');tag=sys.argv[1] if len(sys.argv)>1 else 'final'
rows=[]
for name in ['research-process','multiarm-problem-gen']:
 before=json.loads((s/(name+'.initial.json')).read_text());after=snapshot(Path('/home/fainic/data')/name)
 (s/(name+'.'+tag+'.json')).write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n')
 changes={}
 for field in ['working_tree','git_metadata','git_state']:
  a=before[field] or {};b=after[field] or {}
  changes[field]={'added':sorted(set(b)-set(a)),'removed':sorted(set(a)-set(b)),'modified':[{'path':p,'before':a[p],'after':b[p]} for p in sorted(set(a)&set(b)) if a[p]!=b[p]]}
 row={'repository':name,'before_at_utc':before['captured_at_utc'],'after_at_utc':after['captured_at_utc'],'regular_file_count':sum(v['kind']=='file' for v in before['working_tree'].values()),'unchanged':all(not v for section in changes.values() for v in section.values()),'differences':changes}
 rows.append(row)
(s/('source-integrity-'+tag+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'repository':r['repository'],'unchanged':r['unchanged'],'regular_files':r['regular_file_count'],'change_counts':{k:{a:len(b) for a,b in v.items()} for k,v in r['differences'].items()}} for r in rows],ensure_ascii=False,indent=2))
