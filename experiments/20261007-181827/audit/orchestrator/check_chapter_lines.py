from pathlib import Path
import json,re
s=Path('/tmp/hac-20261007-181827');cfg=json.loads((s/'run_config.json').read_text())
completed={r['group'] for r in json.loads((s/'telemetry-summary.json').read_text()) if r['status']=='completed'}
results={}
for g in cfg['groups']:
 if g['group'] not in completed:continue
 p=Path(g['worktree'])/'INDEX.md';checks=[]
 for n,line in enumerate(p.read_text().splitlines(),1):
  m=re.search(r'\]\((sources/[^)]+)\)',line)
  if not m:continue
  f=p.parent/m.group(1);lines=f.read_text().splitlines()
  headings=re.findall(r'《([^》]+)》L(\d+)',line)
  if not headings:headings=re.findall(r'“([^”]+)”（L(\d+)(?:[–-]\d+)?）',line)
  if not headings:headings=re.findall(r'§(.+?)（L(\d+)）',line)
  if not headings and '|' in line:
   cell=line.rsplit('|',2)[-2]
   headings=re.findall(r'([^<>]+?)（L(\d+)）',cell)
  for title,num in headings:
   title=title.strip();i=int(num);actual=lines[i-1].lstrip('#').strip() if i<=len(lines) else ''
   checks.append({'source':m.group(1),'heading':title,'line':i,'matches':actual==title,'actual':actual,'index_line':n})
 ranges=[]; current=None
 for n,line in enumerate(p.read_text().splitlines(),1):
  m=re.search(r'\]\((sources/[^)]+)\)',line)
  if m:current=m.group(1)
  if current and (('关键章节' in line and not line.startswith('|')) or ('「' in line and line.startswith('|'))):
   count=len((p.parent/current).read_text().splitlines())
   for lo,hi in re.findall(r'L(\d+)[–-](\d+)',line):
    a,b=int(lo),int(hi);ranges.append({'source':current,'start':a,'end':b,'in_bounds':1<=a<=b<=count,'index_line':n})
 results[g['group']]={'checked':len(checks),'exact_heading_count':len(checks),'errors':[x for x in checks if not x['matches']],'range_count':len(ranges),'range_errors':[x for x in ranges if not x['in_bounds']],'checks':checks,'range_checks':ranges}
(s/'chapter-line-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({g:{'exact_headings':r['checked'],'errors':r['errors'],'ranges':r['range_count'],'range_errors':r['range_errors']} for g,r in results.items()},ensure_ascii=False))
