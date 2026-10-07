import json,datetime,hashlib,csv,sys
from pathlib import Path
s=Path('/tmp/hac-20261007-181827');cfg=json.loads((s/'run_config.json').read_text());order=[g['group'] for g in cfg['groups']]
ts={r['group']:r for r in json.loads((s/'telemetry-summary.json').read_text())};vs={r['group']:r for r in json.loads((s/'product-verification.json').read_text())};findings=json.loads((s/'reviewer-findings.json').read_text());heads=json.loads((s/'chapter-line-verification.json').read_text());integrity=json.loads((s/'source-integrity-final.json').read_text())
assert all(g in ts and ts[g]['status']=='completed' and g in vs and g in findings for g in order)
def dt(x):return datetime.datetime.fromisoformat(x.replace('Z','+00:00'))
def local(x):return dt(x).astimezone(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='milliseconds') if x else None
def elapsed(v):
 secs=round(v);return f'{secs//60}分{secs%60:02d}秒'
for g in cfg['groups']:
 r=ts[g['group']];assert r['actual_models']==[g['requested_model']] and r['actual_reasoning_efforts']==[g['requested_reasoning_effort']]
 for k in ['actual_models','actual_reasoning_efforts','session_started_at_utc','finished_at_utc','wall_seconds','runtime_duration_ms','token_usage','agent_path','session_id','permissions_sha256','initial_environment_messages_sha256','shared_runtime_components_sha256','normalized_prompt_sha256','tool_call_count','status']:g[k]=r.get(k)
 g['started_at_Asia_Shanghai']=local(r['session_started_at_utc']);g['finished_at_Asia_Shanghai']=local(r['finished_at_utc']);g['actual_configuration_matches_requested']=True
 g['prompt_plaintext_log_verification']='不可用：平台对 spawn 消息正文加密；保存的 assigned-prompt.txt 为调用时使用的正文，统一模板仅替换 worktree。'
cfg['completed_at_Asia_Shanghai']=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
cfg['scheduling']='先启动三个 Sol 组；每个组结束后依次用释放名额启动对应 Astra 组，最多三个子 agent 同时运行。第二批与第一批尾段重叠。'
cfg['telemetry_method']='来自各子 agent 运行日志 turn_context、task_complete 和 token_usage_record.thread_token_usage；不包含父调度者和平台自动审批器消耗。缓存输入是输入的子集，reasoning_output_tokens 是输出细分，不重复相加。'
cfg['unavailable_metrics']=['准确费用','纯思考/文件操作/等待审批的可靠分段净用时','提示消息加密日志的明文逐字复核']
assert len({r['permissions_sha256'] for r in ts.values()})==1
assert len({r['initial_environment_messages_sha256'] for r in ts.values()})==1
starts=[dt(ts[g]['session_started_at_utc']) for g in order];ends=[dt(ts[g]['finished_at_utc']) for g in order];span=(max(ends)-min(starts)).total_seconds();events=sorted([(dt(ts[g]['session_started_at_utc']),1) for g in order]+[(dt(ts[g]['finished_at_utc']),-1) for g in order]);n=peak=0
for _,d in events:n+=d;peak=max(peak,n)
assert peak<=3
cfg['observed_maximum_concurrent_subagents']=peak;cfg['six_runs_elapsed_seconds']=round(span,3)
(s/'run_config.final.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
rows=['# 人和 agent 协作材料汇集：六组单次对比',f'\n批次 `{cfg["batch"]}`，2026-10-07，时间均按 Asia/Shanghai。六组已完成，产物原样归档，各 worktree 保留。没有合并、推送或对组内结果作修补。',f'\n共同基准：`{cfg["base_commit"]}`。目标初始无文件、无提交；用独立空索引建立空提交。分支、路径、开始/结束时间及实际配置见 [RUN_CONFIG.json](RUN_CONFIG.json)。Sol 为 `gpt-6.1-sol`，Astra 为 `gpt-6-astra`；六组模型和推理强度均与要求一致。', '\n## 实际产物与耗时', '\n| 组（原样索引） | 文件数（研究 / 代码仓库） | 高信号材料覆盖 | 子任务墙钟 |', '| --- | ---: | ---: | ---: |']
for g in order:
 v=vs[g];counts=v['counts_by_repository'];rows.append(f'| [{g}]({g}/INDEX.md) | {v["source_file_count"]}（{counts["research-process"]} / {counts["multiarm-problem-gen"]}） | {v["reference_A_collected"]}/43 | {elapsed(ts[g]["wall_seconds"])} |')
rows+=['\n43 项是调度者在读取组内产物前，依据源文件建立的高信号核查集，不是唯一标准答案或完整相关全集。逐文件依据见 [review-reference.json](audit/review-reference.json)，全部选材差异见 [selection-matrix.csv](audit/selection-matrix.csv)。', '\n## 独立核查与差异', '\n'+('所有组副本与结束时原件逐字节一致，且 SHA-256 与开工快照一致，索引本地文件路径均有效。' if all(not vs[g]['fidelity_mismatches'] and not vs[g]['broken_index_links'] for g in order) else '发现保真或索引问题，见核验 JSON。')+'逐组检查来自实际文件和原文，未仅依据子 agent 自述。原文内部指向未收附件或业务资料的链接保持原样；这与 INDEX 自身路径失效分开判断。']
for g in order:
 f=findings[g];rows.append(f'\n- **{g}**：{f["summary"]}')
rows+=['\n各组对确认、候选、探索执行和历史结果均作区分。更细的状态标注、章节定位及范围审阅见 [reviewer-findings.json](audit/reviewer-findings.json) 和 [product-verification.json](audit/product-verification.json)。', '\n范围方面，未发现跨组读取、再次委派、执行历史任务或向来源写入。`sol_high`、`sol_xhigh` 初期枚举曾输出 `.git` 内路径名；部分其他组使用先递归后过滤的遍历方式。工具记录未见 Git 对象或历史正文进入选材过程，不能把这些偏差略去，也不将路径枚举扩大解释为历史内容污染。具体逐组记录见 [scope-audit.json](audit/scope-audit.json) 和评审记录。', '\n两个来源仓库的 268 个普通文件及所记录目录/权限/修改时间、内容摘要、Git 状态和 Git 元数据，结束核查均与初始快照一致。证据见 [来源完整性核查](audit/source-integrity-final.json)。归档与 worktree 的全部产物逐项一致，只排除 Git 管理指针 `.git`，见 [归档核验](audit/archive-verification.json)。', '\n## 实际 token 用量', '\n| 组 | 输入 token | 其中缓存输入 | 输出 token |', '| --- | ---: | ---: | ---: |']
for g in order:
 u=ts[g]['token_usage'];rows.append(f'| {g} | {u["input_tokens"]:,} | {u["cached_input_tokens"]:,} | {u["output_tokens"]:,} |')
rows+=['\n来源为每组运行日志最后一条 `token_usage_record.thread_token_usage`，逐次记录保存在 [audit/telemetry/](audit/telemetry/)。这是多次模型调用累计量，包含重复上下文；缓存已包含在输入中，不能再次相加。思考输出细分及总量保存在运行配置，不折算费用。父调度、独立核查和平台审批器用量不计入六组数据。', f'\n每组耗时从子任务会话创建到完成事件，含阅读、思考、文件操作和工具等待。最多三个子 agent 并发，空位释放后启动第二批；六组首个启动至最后完成的并行墙钟为 **{elapsed(span)}**，不等于六组耗时之和，也不包含此前准备和后续归档。', '\n## 对结果的使用限制', '\n本轮每个配置仅运行一次，未随机化顺序，评审不是盲评；共享机器、缓存、服务调度、选材边界和模型分词都会影响耗时与用量。43 项覆盖相同也不代表其余相关材料等价。应将这次结果用于观察具体遗漏、边界取舍和产物质量，不能当作稳定模型排名或推理强度的因果结论。', '\n六组使用 `fork_turns=none`、相同工具入口与权限配置，继承相同公共项目环境；统一任务见 [TASK.md](TASK.md)，执行约束见 [PROMPT_TEMPLATE.txt](PROMPT_TEMPLATE.txt)。隔离通过独立 worktree 和明确读写指令实现，平台没有提供按子 agent 绑定独立文件系统沙箱的接口。运行日志中的任务正文已加密，无法独立再读明文；保存的六份发出提示仅 worktree 绑定不同。纯活动净用时和准确费用不可用。']
(s/'REPORT.md').write_text('\n'.join(rows)+'\n')
with (s/'run-metrics.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['group','model','reasoning_effort','start_Asia_Shanghai','end_Asia_Shanghai','wall_seconds','source_files','A_collected','input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens','total_tokens'])
 for g in cfg['groups']:
  r=ts[g['group']];v=vs[g['group']];u=r['token_usage'];w.writerow([g['group'],r['actual_models'][0],r['actual_reasoning_efforts'][0],g['started_at_Asia_Shanghai'],g['finished_at_Asia_Shanghai'],r['wall_seconds'],v['source_file_count'],v['reference_A_collected'],*[u[k] for k in ['input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens','total_tokens']]])
print(json.dumps({'groups':len(order),'concurrency':peak,'span_seconds':span,'report_characters':len((s/'REPORT.md').read_text())},ensure_ascii=False))
