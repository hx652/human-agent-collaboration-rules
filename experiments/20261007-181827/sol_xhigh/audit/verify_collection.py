#!/usr/bin/env python3
"""Verify this collection without running any source script or traversing .git."""
import os, json, hashlib, re, subprocess, datetime
from pathlib import Path
work=Path('/home/fainic/data/human-agent-collaboration-rules-worktrees/20261007-181827/sol_xhigh').resolve()
assert Path.cwd().resolve()==work
out=work/'audit'
roots={n:Path('/home/fainic/data')/n for n in ['research-process','multiarm-problem-gen']}
initial=json.loads((out/'initial-inventory.json').read_text())
manifest=json.loads((out/'copy-manifest.json').read_text())
catalog=json.loads((out/'collection-catalog.json').read_text())
exclusions=json.loads((out/'exclusions.json').read_text())
failures=[]; results=[]
for item in manifest:
 src=Path(item['source_path']); dst=work/item['copy_path']
 assert src.resolve().is_relative_to(roots[item['repository']].resolve())
 assert dst.resolve().is_relative_to(work)
 a=src.read_bytes(); b=dst.read_bytes()
 record={'copy_path':item['copy_path'],'byte_equal':a==b,'source_sha256':hashlib.sha256(a).hexdigest(),'copy_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'manifest_equal':len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']}
 results.append(record)
 if not record['byte_equal'] or not record['manifest_equal']: failures.append({'check':'copy','path':item['copy_path']})
current=[]
for repo,root in roots.items():
 for base,ds,fs in os.walk(root,followlinks=False):
  ds[:]=sorted(d for d in ds if d!='.git' and not Path(base,d).is_symlink())
  for name in sorted(fs):
   p=Path(base,name)
   if p.is_symlink(): failures.append({'check':'new_symlink','path':str(p)}); continue
   stat=p.stat(); raw=p.read_bytes()
   current.append({'repository':repo,'path':p.relative_to(root).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'mode':stat.st_mode,'mtime_ns':stat.st_mtime_ns})
(out/'final-inventory.json').write_text(json.dumps({'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_roots':[str(r) for r in roots.values()],'excluded':'.git directories; no symlink traversal','files':current},ensure_ascii=False,indent=2)+'\n')
old={(f['repository'],f['path']):f for f in initial['files']}; now={(f['repository'],f['path']):f for f in current}
added=sorted(set(now)-set(old)); removed=sorted(set(old)-set(now)); changed=[{'repository':k[0],'path':k[1],'fields':[f for f in ['bytes','sha256','mode','mtime_ns'] if old[k][f]!=now[k][f]]} for k in sorted(set(old)&set(now)) if old[k]!=now[k]]
if added or removed or changed: failures.append({'check':'source_snapshot','added':added,'removed':removed,'changed':changed})
git_checks=[]
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',PYTHONDONTWRITEBYTECODE='1')
for repo,root in roots.items():
 for label,args in [('status',['status','--short','--untracked-files=all']),('ignored',['ls-files','--others','--ignored','--exclude-standard']),('tracked',['ls-files','-z'])]:
  proc=subprocess.run(['git','-C',str(root),*args],cwd=work,env=env,capture_output=True,check=True)
  (out/f'{repo}-{label}-final.txt').write_bytes(proc.stdout)
  same=proc.stdout==(out/f'{repo}-{label}-initial.txt').read_bytes()
  git_checks.append({'repository':repo,'query':label,'unchanged':same,'git_optional_locks':'0'})
  if not same: failures.append({'check':'git_working_state','repository':repo,'query':label})
links=[]
index=(work/'INDEX.md').read_text()
for target in re.findall(r'\]\(([^)]+)\)',index):
 if re.match(r'^[a-z]+://',target,re.I) or target.startswith('#'): continue
 path=work/target.split('#',1)[0]
 okay=path.resolve().is_relative_to(work) and path.is_file()
 links.append({'target':target,'exists_as_file_inside_worktree':okay})
 if not okay: failures.append({'check':'index_link','target':target})
section_checks=[]
for entry in catalog:
 lines=(work/entry['copy_path']).read_text().splitlines()
 for sec in entry['key_sections']:
  n=sec['line']; line=lines[n-1] if 1<=n<=len(lines) else ''
  match=re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$',line)
  okay=bool(match and match.group(1)==sec['heading'])
  section_checks.append({'copy_path':entry['copy_path'],'heading':sec['heading'],'line':n,'matches':okay})
  if not okay: failures.append({'check':'key_section','path':entry['copy_path'],'line':n})
copy_paths=set()
for base,ds,fs in os.walk(work/'sources',followlinks=False):
 for name in fs: copy_paths.add((Path(base)/name).relative_to(work).as_posix())
expected={m['copy_path'] for m in manifest}
if copy_paths!=expected: failures.append({'check':'copied_file_set','extra':sorted(copy_paths-expected),'missing':sorted(expected-copy_paths)})
selected={(e['repository'],e['path']) for e in catalog}; rejected={(e['repository'],e['path']) for e in exclusions}
if selected&rejected or selected|rejected!=set(old): failures.append({'check':'inventory_disposition'})
index_source_links={t['target'] for t in links if t['target'].startswith('sources/')}
if index_source_links!=expected: failures.append({'check':'index_collection_coverage'})
repo_stats={}
for repo in roots:
 tracked=set((out/f'{repo}-tracked-initial.txt').read_bytes().decode().split('\x00')); ignored=set((out/f'{repo}-ignored-initial.txt').read_text().splitlines())
 allpaths=[f['path'] for f in initial['files'] if f['repository']==repo]
 repo_stats[repo]={'workspace_files':len(allpaths),'markdown_files':sum(p.endswith('.md') for p in allpaths),'tracked':sum(p in tracked for p in allpaths),'ignored':sum(p in ignored for p in allpaths),'untracked_not_ignored':sum(p not in tracked and p not in ignored for p in allpaths),'copied':sum(m['repository']==repo for m in manifest),'copied_bytes':sum(m['bytes'] for m in manifest if m['repository']==repo)}
report={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'success':not failures,'summary':{'workspace_files':len(old),'copied_files':len(manifest),'copied_bytes':sum(m['bytes'] for m in manifest),'excluded_files':len(exclusions),'byte_equal_copies':sum(r['byte_equal'] for r in results),'manifest_equal_copies':sum(r['manifest_equal'] for r in results),'index_local_links':len(links),'valid_index_links':sum(l['exists_as_file_inside_worktree'] for l in links),'key_sections':len(section_checks),'valid_key_sections':sum(s['matches'] for s in section_checks),'source_snapshot_unchanged':not added and not removed and not changed,'source_git_queries_unchanged':all(g['unchanged'] for g in git_checks),'scope_deviations_reported':'See audit/SCAN.md: two early .git path-traversal deviations, no object contents or historical versions used.'},'repositories':repo_stats,'copy_results':results,'index_links':links,'key_section_checks':section_checks,'git_queries':git_checks,'source_snapshot_changes':{'added':added,'removed':removed,'changed':changed},'failures':failures,'limits':['Historical tests and agent reports were not rerun or independently audited.','Source .git file contents were not fingerprinted; only read-only working-state queries were compared.','Original source-document links and binary academic/model content were not fully validated.','Source snapshot comparison begins after early enumeration corrections, not at the first task instruction.']}
(out/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'success':report['success'],'summary':report['summary'],'repositories':repo_stats,'failures':failures},ensure_ascii=False,indent=2))
raise SystemExit(0 if not failures else 1)
