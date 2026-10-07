import json,re
from pathlib import Path
s=Path('/tmp/hac-20261007-181827');rows=[]
for r in json.loads((s/'telemetry-summary.json').read_text()):
 if r['status']!='completed':continue
 calls=[json.loads(l) for l in (s/'telemetry'/r['group']/'tool-calls.jsonl').read_text().splitlines()];mentions=set();nested=set();communications=[]
 for x in calls:
  raw=x.get('input',x.get('arguments',''))
  mentions.update(re.findall(r'/human-agent-collaboration-rules-worktrees/20261007-181827/([a-z_]+)',raw))
  nested.update(re.findall(r'tools\.([A-Za-z0-9_]+)\s*\(',raw))
  if x['name'] in ['send_message','followup_task','spawn_agent']:
   try:a=json.loads(raw)
   except json.JSONDecodeError:a={}
   communications.append({'tool':x['name'],'timestamp':x['timestamp'],'target':a.get('target'),'task_name':a.get('task_name')})
 rows.append({'group':r['group'],'direct_tools':sorted({x['name'] for x in calls}),'nested_tools':sorted(nested),'mentioned_group_paths':sorted(mentions),'mentions_other_group_paths':bool(mentions-{r['group']}),'communications':communications,'subagent_spawn_calls':sum(x['name']=='spawn_agent' for x in calls),'tool_record_file':f'telemetry/{r["group"]}/tool-calls.jsonl','method':'Tool-call records inspected; lexical summaries support but do not replace review of shell commands. Absolute-path matching cannot prove absence of all possible indirect access.'})
(s/'scope-audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');print(json.dumps(rows,ensure_ascii=False,indent=2))
