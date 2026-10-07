import json,shutil,sys,hashlib,datetime
from pathlib import Path
sys.dont_write_bytecode=True
from snapshot_lib import manifest,git
s=Path('/tmp/hac-20261007-181827');cfg=json.loads((s/'run_config.final.json').read_text());dst=Path(cfg['archive'])
assert all(g['status']=='completed' for g in cfg['groups'])
for f in ['REPORT.md','RUN_CONFIG.json']:
 source=s/('run_config.final.json' if f=='RUN_CONFIG.json' else f)
 shutil.copy2(source,dst/f)
for name in ['source-integrity-final.json','target-repository-verification.json','reviewer-findings.json','product-verification.json','selection-matrix.csv','chapter-line-verification.json','telemetry-summary.json','run-metrics.csv','scope-audit.json']:
 shutil.copy2(s/name,dst/'audit'/name)
for name in ['research-process','multiarm-problem-gen']:
 shutil.copy2(s/(name+'.final.json'),dst/'provenance'/(name+'.final.json'))
shutil.copytree(s/'telemetry',dst/'audit'/'telemetry',dirs_exist_ok=True,copy_function=shutil.copy2)
# Preserve orchestration code as execution evidence; it refers to the original staging path.
code=dst/'audit'/'orchestrator';code.mkdir(exist_ok=True)
for name in ['prepare.py','snapshot_lib.py','collect_telemetry.py','verify_products.py','check_chapter_lines.py','check_sources.py','summarize_scope.py','build_review_reference.py','archive_results.py','build_report.py','finalize_archive.py']:
 shutil.copy2(s/name,code/name)
# Verify raw archives again after copying all observer metadata.
comparisons=[]
for g in cfg['groups']:
 wt=Path(g['worktree']);a=dst/g['group'];m=manifest(wt);n=manifest(a);assert m==n,g['group']
 comparisons.append({'group':g['group'],'source_worktree':str(wt),'archived_to':str(a),'manifest_matches':True,'files':sum(v['kind']!='directory' for v in m.values()),'entries':len(m),'excluded':'.git administrative pointer only'})
(dst/'audit'/'archive-verification.json').write_text(json.dumps({'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'groups':comparisons},ensure_ascii=False,indent=2)+'\n')
# Final integrity list of the archive, with administrative output itself excluded.
lines=[]
for p in sorted(dst.rglob('*')):
 if p.is_file() and not p.is_symlink() and p.name!='ARCHIVE_SHA256SUMS.txt':lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(dst).as_posix())
(dst/'ARCHIVE_SHA256SUMS.txt').write_text('\n'.join(lines)+'\n')
print(json.dumps({'archive':str(dst),'raw_groups_verified':len(comparisons),'archived_regular_files':len(lines),'main_head':git(Path(cfg['target_repository']),'rev-parse','HEAD')['stdout'].strip(),'main_status':git(Path(cfg['target_repository']),'status','--porcelain=v2','--branch')['stdout'],'report_bytes':(dst/'REPORT.md').stat().st_size},ensure_ascii=False,indent=2))
