import json,datetime
from pathlib import Path
rows=[]
def add(repo,items):
 for path,lines,reason in items:
  p=Path('/home/fainic/data')/repo/path
  assert p.is_file(),p
  rows.append({'source':repo+'/'+path,'category':'A','evidence_lines':lines,'reason':reason})
add('research-process',[
('AGENTS.md','9–28, 63–76','明确的跨 session、确认写入、独立判断、事实分层与 Git 授权约定'),
('README.md','21–49','session 使用循环、重要过程记录及渐进组织'),
('overview.md','17–30','实践反馈、个人提醒不泛化为普遍规律'),
('assets/README.md','10–34','稳定资源位置、可维护源文件、外部路径与同步的边界'),
('experiments/README.md','3–15','按需记录实验、注明版本、区分观察和猜测'),
('inbox/README.md','6–12','候选整理后确认写入、不强制清空、保留出处'),
('projects/README.md','13–19','项目与跨项目知识的维护归属'),
('references/README.md','39–42','区分论文主张、个人理解与延伸，注明来源'),
('journal/2026-09-07-record-organization.md','3–43','已确认组织选择、取舍与重新拆分条件'),
('journal/2026-09-07-starting-point.md','16–40','用户确认的实践反馈、跨 session 和更新授权经验'),
('inbox/2026-09-18-agent-collaborative-development-research.md','1–205','协作目标、候选流程、外部证据限制和非通用经验'),
('inbox/2026-09-18-evolving-design-and-best-practices.md','5–49','已认可的渐进设计和可调整工程偏好'),
('inbox/2026-09-16-generator-scene-and-target-representation.md','50–63','用户要求标记未决，agent 却补方案的具体纠正'),
('inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md','5, 15–37','独立审查研究直觉，区分验证目的和预设结论'),
('inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md','49–81','指出用户推断的条件，保留未确认的 agent 提议'),
('inbox/2026-09-08-multi-arm-progress-and-coordination.md','5–13, 40–53','agent 帮助修正概念判断的真实讨论'),
('inbox/2026-09-15-cube-complex-understanding.md','5, 11–23, 90–96','保留用户原始表述并追加已确认完善说明'),
('journal/2026-09-15-research-understanding-and-direction.md','23–32, 40–56, 70–87','用户原声与 agent 补充区分、依据与适用边界')])
add('multiarm-problem-gen',[
('AGENTS.md','9–157','自主权限、架构讨论、阅读隔离、测试目的、统计和证据规则'),
('docs/git-workflow.md','3–122','探索分支、提交和集成、分别授权及逻辑变化'),
('docs/README.md','39–69','实施与讨论分开，保留历史状态，候选不成为指令'),
('docs/notes/discussions/2026-09-18-starting-point.md','11–21','仓库组织、学习目标及单次经验不泛化'),
('docs/notes/discussions/2026-09-22-input-domain-representations.md','37–45','用户质疑 agent 过早加载与额外抽象，实测后限定结论'),
('docs/notes/discussions/2026-09-28-input-reading-flow.md','7–13, 50–56','用户纠正解释方式，以数据流支持理解，精确契约再实施'),
('docs/notes/discussions/2026-09-29-input-implementation-units.md','20, 43–53','任务粒度、依赖顺序、公开契约及修改范围'),
('docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md','7–31','任务交付边界与代码职责分离，独立隔离试验条件'),
('docs/notes/discussions/2026-09-29-unit-1-basic-representations.md','31–49, 80–86','用户纠正 agent 不可变建议；契约与局部实现自主权'),
('docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md','126–132','完整的含义不能自动扩大支持范围，语义歧义返回讨论'),
('docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md','85–93','契约先行、独立上下文交接、授权与实施就绪'),
('docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md','119–143','验收与允许修改范围，完善契约不等于扩大权限'),
('docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md','3–11, 33–37, 148–160','自主探索不等于用户接受，交接导致内部测试信息进入上下文'),
('docs/notes/discussions/2026-09-30-unit-5-public-handoff.md','1–3','经过过滤的公开交接包，探索性决定的状态'),
('docs/notes/discussions/2026-09-30-unit-6-public-handoff.md','1–7','公开交接包及协调者与实现者职责分配'),
('docs/notes/implementation/2026-09-29-first-implementation-results.md','45–70','契约充分性、读取自述不等于证明、明确 Git 交接'),
('docs/notes/implementation/2026-09-29-unit-2-implementation-results.md','33–43','独立计数修正测试预期、阅读范围和自述证据限制'),
('docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md','21–38, 63–93','独立角色、越界重启、集成独立验证及计时口径'),
('docs/notes/implementation/2026-09-30-remove-material-support.md','3–19','审查后收缩无需求依据的实现、明确授权与范围'),
('docs/notes/implementation/2026-09-30-resource-snapshots-results.md','5–33','公共契约作为测试依据、自述与独立证据、工具回退和用量'),
('docs/notes/implementation/2026-09-30-unit-3-implementation-results.md','14–18, 45–49, 51–86','保留已有修改、修正测试而非弱化契约、真实计时'),
('docs/notes/implementation/2026-09-30-unit-4-results.md','35–61','交接事实归属、有限验证、上下文和分段计时'),
('docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md','5–21','意外阅读依赖内部测试后停止，承认不可遗忘并重启'),
('docs/notes/implementation/2026-09-30-unit-5-results.md','3, 11–13, 27–48','过滤交接、测试预期独立、未暂存文件检查覆盖限制'),
('docs/notes/implementation/2026-09-30-unit-6-results.md','13–21, 40–64','主子职责、限定查询失败后的回退、计时不伪精确')])
assert len(rows)==43,len(rows)
rset={x['source'] for x in rows}
for repo in ['research-process','multiarm-problem-gen']:
 for p in sorted((Path('/home/fainic/data')/repo).rglob('*.md')):
  if '.git' in p.parts: continue
  rel=repo+'/'+p.relative_to(Path('/home/fainic/data')/repo).as_posix()
  if rel in rset:continue
  low=rel in {'research-process/journal.md','research-process/inbox/2026-09-14-todos-and-draft.md','research-process/references/stop-n-go-reading-notes.md','multiarm-problem-gen/tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md'}
  rows.append({'source':rel,'category':'C' if low else 'B','evidence_lines':None,'reason':'空文件、待办或第三方纯技术材料，当前未见明确协作经验' if low else '可能提供状态、契约、技术讨论或证据标注的背景；应结合该组索引中的具体纳入理由判断，不作为必收项或自动误收'})
data={'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'created_before_inspecting_group_products':True,'basis':'主调度者独立读取来源；未使用子 agent 的选材清单或产物。A 集合为高信号核查集，不声称是唯一真值或完整相关全集。','categories':{'A':'明确协作约定或包含具体协作过程/纠偏的高信号材料，检查遗漏','B':'相关性依赖纳入理由的背景或边界材料，不计为确定遗漏/误收','C':'当前未见明确协作内容，若收录需另行审查理由'},'rules':['整文件中存在相关协作段落，复制整文件产生技术内容不是自动误收。','不以复制文件数、篇幅或多数表决判断质量。','区分索引到副本的路径、文件内章节锚点、原始文件原有链接。','不把历史实施的已完成状态等同用户已接受该次设计。','字节/哈希由独立程序核查，语义与范围由原文和实际工具记录交叉检查。','其他非 Markdown 文件若被收录须检查具体证据；文件名扫描和文本匹配未见额外协作记录。'],'reference_files':rows}
Path('/tmp/hac-20261007-181827/review-reference.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'created':data['created_at_utc'],'A':sum(x['category']=='A' for x in rows),'B':sum(x['category']=='B' for x in rows),'C':sum(x['category']=='C' for x in rows)},ensure_ascii=False))
