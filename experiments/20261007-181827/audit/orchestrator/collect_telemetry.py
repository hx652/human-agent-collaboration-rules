import json,hashlib,datetime
from pathlib import Path
stage=Path('/tmp/hac-20261007-181827');root='01a115ce-1970-7450-9bda-9a25b0537e24'
config=json.loads((stage/'run_config.json').read_text());names={g['group'] for g in config['groups']}
def events(p):
 out=[]
 for l in p.read_text().splitlines():
  try:out.append(json.loads(l))
  except json.JSONDecodeError:pass
 return out
def sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
parent=next(Path('/home/fainic/.codex/sessions/2026/10/07').glob('*'+root+'.jsonl'))
launches={}
for e in events(parent):
 p=e.get('payload',{})
 if e.get('type')=='response_item' and p.get('type')=='function_call' and p.get('name')=='spawn_agent':
  a=json.loads(p['arguments']); name=a.get('task_name')
  if name in names: launches[name]={'timestamp':e['timestamp'],'arguments':a}
rows=[]
for f in Path('/home/fainic/.codex/sessions/2026/10/07').glob('*.jsonl'):
 with f.open() as h:
  try:meta=json.loads(h.readline()).get('payload',{})
  except (json.JSONDecodeError,AttributeError):continue
 source=meta.get('source'); sp=source.get('subagent',{}).get('thread_spawn',{}) if isinstance(source,dict) else {}
 group=sp.get('agent_path','').rsplit('/',1)[-1]
 if sp.get('parent_thread_id')!=root or group not in names:continue
 es=events(f); contexts=[e for e in es if e['type']=='turn_context'];ctx=contexts[-1]['payload'] if contexts else {}
 tr=[e for e in es if e['type']=='token_usage_record'];tc=[e for e in es if e['type']=='event_msg' and e['payload'].get('type')=='token_count'];done=[e for e in es if e['type']=='event_msg' and e['payload'].get('type')=='task_complete']
 calls=[{'timestamp':e['timestamp'],**{k:v for k,v in e['payload'].items() if k in ['type','call_id','name','namespace','input','arguments']}} for e in es if e['type']=='response_item' and e['payload'].get('type') in ['function_call','custom_tool_call']]
 finals=[{'timestamp':e['timestamp'],'payload':e['payload']} for e in es if e['type']=='response_item' and e['payload'].get('type')=='message' and e['payload'].get('role')=='assistant' and e['payload'].get('phase') in ['final','final_answer']]
 worlds=[e['payload'].get('state',{}) for e in es if e['type']=='world_state' and e['payload'].get('full')]
 world=worlds[0] if worlds else {}
 shared_hashes={k:sha(world[k]) for k in ['apps_instructions','environments','environments_instructions','host_skills','plugins_instructions','skills','permissions'] if k in world}
 envs=[e['payload']['content'] for e in es if e['type']=='response_item' and e['payload'].get('type')=='message' and e['payload'].get('role')=='user']
 permission={k:ctx.get(k) for k in ['cwd','workspace_roots','approval_policy','approvals_reviewer','sandbox_policy','permission_profile','disabled_plugin_ids']}
 launch=launches.get(group); sent=launch['arguments']['message'] if launch else None
 prompt=(stage/(group+'.prompt.txt')).read_text(); encrypted=bool(sent and sent.startswith('gAAAA')); normalized=prompt.replace(next(g['worktree'] for g in config['groups'] if g['group']==group),'{worktree}')
 end=done[-1]['timestamp'] if done else (finals[-1]['timestamp'] if finals else None);start=es[0]['timestamp']
 def dt(x):return datetime.datetime.fromisoformat(x.replace('Z','+00:00'))
 r={'group':group,'session_id':meta.get('id'),'agent_path':sp.get('agent_path'),'log_path':str(f),'log_sha256_at_capture':hashlib.sha256(f.read_bytes()).hexdigest(),'session_started_at_utc':start,'launch_requested_at_utc':launch['timestamp'] if launch else None,'turn_context_at_utc':contexts[0]['timestamp'] if contexts else None,'finished_at_utc':end,'wall_seconds':round((dt(end)-dt(start)).total_seconds(),3) if end else None,'runtime_duration_ms':done[-1]['payload'].get('duration_ms') if done else None,'actual_models':sorted({e['payload'].get('model') for e in contexts}),'actual_reasoning_efforts':sorted({e['payload'].get('effort') for e in contexts}),'runtime_permissions':permission,'permissions_sha256':sha(permission),'shared_runtime_components_sha256':shared_hashes,'initial_environment_messages_sha256':sha(envs),'initial_environment_message_count':len(envs),'spawn_configuration':{k:v for k,v in launch['arguments'].items() if k!='message'} if launch else None,'sent_prompt_matches_saved_prompt':None if encrypted else sent==prompt,'prompt_log_encrypted':encrypted,'normalized_prompt_sha256':hashlib.sha256(normalized.encode()).hexdigest() if normalized else None,'token_usage':tr[-1]['payload'].get('thread_token_usage') if tr else None,'token_usage_timestamp_utc':tr[-1]['timestamp'] if tr else None,'token_event_count':len(tr),'tool_call_count':len(calls),'complete_event_present':bool(done),'status':'completed' if done else 'running'}
 td=stage/'telemetry'/group;td.mkdir(parents=True,exist_ok=True)
 (td/'metadata.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 (td/'tool-calls.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in calls))
 (td/'token-usage.jsonl').write_text(''.join(json.dumps({'timestamp':e['timestamp'],'usage':e['payload'].get('usage'),'thread_token_usage':e['payload'].get('thread_token_usage')},ensure_ascii=False)+'\n' for e in tr))
 (td/'final-events.json').write_text(json.dumps({'final_responses':finals,'task_complete':[{'timestamp':e['timestamp'],'payload':e['payload']} for e in done]},ensure_ascii=False,indent=2)+'\n')
 (td/'assigned-prompt.txt').write_text(prompt)
 if (td/'sent-prompt.txt').exists():(td/'sent-prompt.txt').unlink()
 rows.append(r)
(stage/'telemetry-summary.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['group','status','actual_models','actual_reasoning_efforts','session_started_at_utc','finished_at_utc','wall_seconds','permissions_sha256','sent_prompt_matches_saved_prompt','normalized_prompt_sha256','tool_call_count']} for r in rows],ensure_ascii=False,indent=2))
