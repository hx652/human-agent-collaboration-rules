import os,sys,json,shutil,datetime,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
from snapshot_lib import manifest,git
stage=Path('/tmp/hac-20261007-181827');cfg=json.loads((stage/'run_config.json').read_text());archive=Path(cfg['archive'])
telemetry={r['group']:r for r in json.loads((stage/'telemetry-summary.json').read_text())};archived=[]
for g in cfg['groups']:
 r=telemetry.get(g['group'])
 if not r or r['status']!='completed':continue
 src=Path(g['worktree']);dst=archive/g['group']
 if not dst.exists():shutil.copytree(src,dst,symlinks=True,copy_function=shutil.copy2,ignore=lambda d,n: {'.git'} if Path(d)==src else set())
 before=manifest(src);after=manifest(dst)
 assert before==after,('Archive mismatch',g['group'])
 archived.append({'group':g['group'],'source_worktree':str(src),'archived_to':str(dst),'manifest_matches':True,'entries':len(before),'files':sum(v['kind']!='directory' for v in before.values()),'excluded':'.git administrative pointer only; all generated files, directories, symlinks and modes preserved'})
 (archive/'audit').mkdir(exist_ok=True)
 for k in ['actual_models','actual_reasoning_efforts','session_started_at_utc','finished_at_utc','wall_seconds','runtime_duration_ms','token_usage','agent_path','session_id','permissions_sha256','prompt_log_encrypted','normalized_prompt_sha256','tool_call_count','status']:
  g[k]=r.get(k)
(archive/'RUN_CONFIG.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
for name in ['review-reference.json','product-verification.json','selection-matrix.csv','telemetry-summary.json','sol_high-heading-check.json','chapter-line-verification.json','reviewer-findings.json']:
 p=stage/name
 if p.exists():shutil.copy2(p,archive/'audit'/name)
if (stage/'telemetry').exists():shutil.copytree(stage/'telemetry',archive/'audit'/'telemetry',dirs_exist_ok=True,copy_function=shutil.copy2)
(archive/'audit'/'archive-verification.json').write_text(json.dumps({'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'groups':archived},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(archived,ensure_ascii=False,indent=2))
