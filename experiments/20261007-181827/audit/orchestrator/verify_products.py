import json,hashlib,re,urllib.parse,unicodedata,datetime,os,sys,csv
from pathlib import Path
sys.dont_write_bytecode=True
from snapshot_lib import manifest,git
stage=Path('/tmp/hac-20261007-181827')
config=json.loads((stage/'run_config.json').read_text())
ref=json.loads((stage/'review-reference.json').read_text())
refs={x['source']:x for x in ref['reference_files']}
initial={n:json.loads((stage/(n+'.initial.json')).read_text()) for n in ['research-process','multiarm-problem-gen']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def no_code(s):return re.sub(r'```.*?```',lambda m: ''.join('\n' if c=='\n' else ' ' for c in m.group(0)),s,flags=re.S)
def anchors(p):
 seen={};out=set()
 for line in p.read_text(errors='replace').splitlines():
  m=re.match(r'^\s{0,3}#{1,6}\s+(.*?)(?:\s+#+)?\s*$',line)
  if not m:continue
  s=m.group(1).lower().replace('`','').replace('*','');s=re.sub(r'<[^>]+>','',s)
  s=''.join(ch for ch in s if not unicodedata.category(ch).startswith(('P','S')) or ch in '-_');s=re.sub(r'\s','-',s)
  n=seen.get(s,0);seen[s]=n+1;out.add(s+(f'-{n}' if n else ''))
 return out
completed={r['group'] for r in json.loads((stage/'telemetry-summary.json').read_text()) if r['status']=='completed'}
reports=[]
for group in config['groups']:
 name=group['group'];wt=Path(group['worktree'])
 if name not in completed: continue
 if not (wt/'INDEX.md').exists(): continue
 m=manifest(wt);idx=(wt/'INDEX.md').read_text();clean=no_code(idx);selected=[];mismatches=[];copied=[]
 for path,v in m.items():
  if not path.startswith('sources/') or v['kind']=='directory':continue
  rel=path[len('sources/'):];repo,_,sub=rel.partition('/');src=Path('/home/fainic/data')/rel
  expected=initial.get(repo,{}).get('working_tree',{}).get(sub)
  check={'path':path,'source':str(src),'kind':v['kind'],'sha256':v.get('sha256'),'bytes':v.get('size'),'exists_in_initial_snapshot':expected is not None,'matches_initial_source':expected is not None and v.get('sha256')==expected.get('sha256') and v['kind']==expected['kind'],'matches_current_source':src.is_file() and v.get('sha256')==sha(src) and (wt/path).read_bytes()==src.read_bytes(),'category':refs.get(rel,{}).get('category','UNCLASSIFIED')}
  if not check['matches_initial_source'] or not check['matches_current_source']:mismatches.append(check)
  copied.append(check);selected.append(rel)
 links=[]
 for match in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]*>|[^)\s]+)(?:\s+"[^"]*")?\)',clean):
  target=match.group(1).strip('<>');u=urllib.parse.urlsplit(target)
  if u.scheme in ['http','https','mailto','data','app','codex']:continue
  part=urllib.parse.unquote(u.path);p=(wt/part).resolve() if part else wt/'INDEX.md';fragment=urllib.parse.unquote(u.fragment)
  inside=p==wt or wt in p.parents
  result={'target':target,'resolved_path':str(p),'exists':p.exists(),'inside_worktree':inside,'fragment':fragment or None,'index_line':idx.count('\n',0,match.start())+1}
  if fragment and p.suffix.lower()=='.md' and p.is_file():result['fragment_matches_gfm_approximation']=fragment in anchors(p)
  links.append(result)
 missing_index=[s for s in selected if ('sources/'+s) not in urllib.parse.unquote(idx)]
 aset={p for p,r in refs.items() if r['category']=='A'}
 report={'group':name,'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_commit':git(wt,'rev-parse','HEAD')['stdout'].strip(),'branch':git(wt,'symbolic-ref','--short','HEAD')['stdout'].strip(),'status':git(wt,'status','--porcelain=v2','--untracked-files=all'),'source_file_count':len(copied),'source_bytes':sum(x['bytes'] or 0 for x in copied),'counts_by_repository':{repo:sum(s.startswith(repo+'/') for s in selected) for repo in initial},'reference_A_total':len(aset),'reference_A_collected':len(aset&set(selected)),'reference_A_missing':sorted(aset-set(selected)),'category_counts':{c:sum(x['category']==c for x in copied) for c in ['A','B','C','UNCLASSIFIED']},'fidelity_mismatches':mismatches,'index_bytes':(wt/'INDEX.md').stat().st_size,'index_lines':len(idx.splitlines()),'index_links':links,'broken_index_links':[x for x in links if not x['exists']],'suspicious_fragments':[x for x in links if x.get('fragment_matches_gfm_approximation') is False],'copied_paths_not_literal_in_index':missing_index,'extra_files':sorted(p for p,v in m.items() if v['kind']!='directory' and not p.startswith('sources/') and p!='INDEX.md'),'copied_sources':copied,'product_manifest':m}
 reports.append(report)
(stage/'product-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
with (stage/'selection-matrix.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['source','review_category',*[r['group'] for r in reports]])
 sets={r['group']:{p['path'][8:] for p in r['copied_sources']} for r in reports}
 for p in sorted(set(refs)|set().union(*sets.values())):w.writerow([p,refs.get(p,{}).get('category','UNCLASSIFIED'),*[int(p in sets[r['group']]) for r in reports]])
print(json.dumps([{k:r[k] for k in ['group','source_file_count','counts_by_repository','reference_A_collected','reference_A_missing','category_counts','fidelity_mismatches','broken_index_links','suspicious_fragments','copied_paths_not_literal_in_index','extra_files']} for r in reports],ensure_ascii=False,indent=2))
