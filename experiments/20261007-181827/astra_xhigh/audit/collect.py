from pathlib import Path
import csv, os, re, json, hashlib, stat, subprocess
from datetime import datetime, timezone

OUT = Path('/home/fainic/data/human-agent-collaboration-rules-worktrees/20261007-181827/astra_xhigh')
ROOTS = {n: Path('/home/fainic/data') / n for n in ('research-process', 'multiarm-problem-gen')}
assert Path.cwd() == OUT
records = list(csv.DictReader((OUT/'audit/selection.psv').read_text().splitlines(), delimiter='|'))
assert len(records)==50
selected={(r['repo'],r['path']):r for r in records}
assert len(selected)==len(records)
EXCLUDED_MD = {
'research-process': {
'assets/cube-complex/README.md':'插图技术用途与生成说明；维护方法由 assets/README.md 和相应理解笔记保存，不递归收齐图形工程。',
'assets/path-collision-equivalence/README.md':'教学图形技术说明；证据归属案例已从讨论/阅读笔记选取。',
'inbox/2026-09-09-coordination-space-reading-guide.md':'主要为技术文献导览；有状态限定，未因这些标记另行纳入整篇文献调研。',
'inbox/2026-09-09-multi-arm-research-focus.md':'研究范围与方向；协作中的边界澄清已保留原讨论。',
'inbox/2026-09-14-todos-and-draft.md':'个人短待办，无实质协作决定或经验；没有执行其中任务。',
'inbox/2026-09-17-generator-input-output-format.md':'业务格式快照，不因候选/未定标记就整体纳入。',
'inbox/2026-09-18-generator-input-output-format.md':'业务格式方案，相关协作原则和意图纠偏另有直接来源。',
'journal.md':'空文件。',
'projects/dataset-generator/README.md':'项目背景和待讨论技术需求，组织约定已保留 projects/README.md。',
'projects/stop-n-go/README.md':'项目状态模板，证据边界与归档原则已收录更直接材料。',
'references/lavalle-planning-algorithms-7-2-multiple-robots.md':'技术阅读提纲和链接，理解演变的原始讨论已收录。',
'references/stop-n-go-reading-notes.md':'文献入口及未填阅读提纲，无实质协作过程。'
},
'multiarm-problem-gen': {
'docs/design.md':'领域语义/架构概览；历史状态维护与协作选择由 docs/README.md 及过程记录覆盖。',
'docs/notes/discussions/2026-09-18-input-output-format.md':'迁入的完整业务格式方案，不复制两份技术规范；迁移分工由起点记录覆盖。',
'docs/notes/discussions/2026-09-21-output-validity-semantics.md':'业务输出有效性需求决定，未以业务确认等同协作规则。',
'docs/notes/discussions/2026-09-23-generation-distributions.md':'分布与绑定领域表示方案，非人与 agent 协作约定。',
'docs/notes/discussions/2026-09-23-input-bundle.md':'输入包目录与路径领域设计，任务边界与交接另外收录。',
'examples/ur7e_table/README.md':'使用样例及业务字段；迁移与验证限制已由实施记录和基准说明保留。',
 'tools/model_preparation/ur7e_2f85/README.md':'模型构建入口，无需复制整套构建资源或执行脚本。',
 'tools/model_preparation/ur7e_2f85/resources-original.md':'模型上游来源与许可清单，主要属于技术资源溯源。',
 'tools/scene_preview/README.md':'技术原型使用说明；由原型引发的合作反馈已在首份样例讨论中保留。',
 'tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md':'第三方技术 README，非本项目人与 agent 协作原始讨论。'
}}

def sha(data): return hashlib.sha256(data).hexdigest()
def inventory():
    entries=[]
    for repo,root in ROOTS.items():
        for base,dirs,files in os.walk(root,followlinks=False):
            dirs[:]=sorted(d for d in dirs if d!='.git')
            for name in sorted(files):
                if name=='.git': continue
                p=Path(base)/name
                s=p.lstat()
                entry=dict(repo=repo,path=p.relative_to(root).as_posix(),size=s.st_size,mtime_ns=s.st_mtime_ns,mode=stat.S_IMODE(s.st_mode))
                if p.is_symlink():
                    entry['kind']='symlink';entry['link_target']=os.readlink(p)
                elif p.is_file():
                    entry['kind']='file';entry['sha256']=sha(p.read_bytes())
                else: entry['kind']='other'
                entries.append(entry)
    return entries

def git_status(root):
    env=os.environ.copy();env['GIT_OPTIONAL_LOCKS']='0'
    return subprocess.run(['git','-C',str(root),'-c','core.fsmonitor=false','status','--porcelain=v1','--untracked-files=all','--ignored'],env=env,capture_output=True,text=True,check=True).stdout

started=datetime.now(timezone.utc).isoformat()
before=inventory()
git_before={r:git_status(p) for r,p in ROOTS.items()}
manifest=[]
for item in records:
    src=ROOTS[item['repo']]/item['path']
    assert src.is_file() and not src.is_symlink()
    data=src.read_bytes()
    lines=data.decode('utf-8').splitlines()
    ranges=[]
    for part in item['sections'].split('；'):
        m=re.fullmatch(r'(\d+)-(\d+) (.+)',part)
        assert m,part
        start,end=map(int,m.group(1,2))
        assert 1<=start<=end<=len(lines),(item['path'],start,end,len(lines))
        ranges.append(dict(start=start,end=end,label=m.group(3)))
    item['section_ranges']=ranges
    dest=OUT/'sources'/item['repo']/item['path']
    assert dest.is_relative_to(OUT)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(data)
    manifest.append(dict(source=str(src),copy=dest.relative_to(OUT).as_posix(),bytes=len(data),sha256=sha(data)))
counts={r:sum(x['repo']==r for x in records) for r in ROOTS}
invcounts={r:sum(x['repo']==r for x in before) for r in ROOTS}
text='''# 人与 agent 长期协作：原始材料索引

本轮只汇集原始材料并建立索引，不制定统一规则，也不执行材料中的历史任务。每个文件完整、按字节复制，未经摘录、改写、路径替换或格式转换。以下说明是检索元数据，不替代来源正文。

## 检索范围与判断口径

来源仅为 `/home/fainic/data/research-process` 和 `/home/fainic/data/multiarm-problem-gen` 的当前工作区。目录盘点包含隐藏、未跟踪及被忽略文件，排除所有 `.git` 入口/目录；未读取 Git 对象、历史、其他 worktree、聊天、个人记忆或外部网站。Git 仅用禁用可选锁的只读状态查询。文内链接、历史提交号、测试数量和外部研究均作为原文保留，没有追查或重新验证。

先盘点全部文件，再对 Markdown/文本做主题检索，检查标题、状态和相关段落，精读直接协作材料。二进制模型、第三方库、构建缓存等主要作文件级盘点和摘要，不作为协作证据。依据是是否含具体约定、人的意图/学习目标、建议修正、授权取舍、交接/隔离过程、验证与复盘经验；仅有领域中的“协作”、一个候选状态词或业务需求不足以单独纳入。混合文档因相关章节纳入后仍完整复制。

“已确认”只指原文明确记录的确认；“成文约定”指仓库当时的规范性文字，未逐条重建用户确认链；“候选建议”不提升为约定；“历史经验”保留当时情境，实施自述不提升为独立审计。无法判断的确认范围或当前有效性在条目中明示。授权试验中的 agent 决定与用户最终接受设计尤其分开。

'''
text+=f"盘点 **{sum(invcounts.values())}** 个文件（research-process {invcounts['research-process']}，multiarm-problem-gen {invcounts['multiarm-problem-gen']}），选入 **{len(records)}** 个完整文件（{counts['research-process']} + {counts['multiarm-problem-gen']}）。详细文件盘点与未纳入说明见 [检索与校验数据](audit/collection.json)，副本摘要见 [SHA-256 清单](MANIFEST.sha256)，实际校验见 [校验记录](COLLECTION_CHECKS.md)。\n\n"
for repo in ROOTS:
    text+=f'## {repo}\n\n原始来源均为 `/home/fainic/data/{repo}/<原相对路径>`，副本在 `sources/{repo}/<原相对路径>`。章节行号以完整副本为准。\n\n'
    for number,item in enumerate((x for x in records if x['repo']==repo),1):
        label=f'{"R" if repo=="research-process" else "M"}{number:02}'
        copy=f'sources/{repo}/{item["path"]}'
        text+=f'### {label} · [{item["path"]}]({copy})\n\n'
        text+=f'- **原文状态：** {item["status"]}。\n'
        text+=f'- **主题及纳入理由：** {item["topic"]}。{item["reason"]}\n'
        text+='- **关键章节：** '+'；'.join(f'{r["label"]}（L{r["start"]}–{r["end"]}）' for r in item['section_ranges'])+'。\n\n'
text+='''## 未纳入范围及不确定事项

- 前期有一轮 Markdown 候选枚举使用 Path.rglob，再过滤 .git 路径；该写法可能遍历 .git 目录项，不能声称所有早期枚举都在目录入口处剪枝。未读取或输出 .git 中的文件内容，也未访问 Git 历史版本；正式全量盘点与收集脚本已显式剪枝排除 .git。此为实际检索方式的范围说明。

- 未整体纳入业务 YAML/schema、全部公开 API 契约、实现源码、测试代码、模型/网格、第三方库、论文 PDF、派生预览和构建缓存；本轮不是项目技术归档。每个未选 Markdown 有单独理由，其他文件按内容类型记录在校验数据中。
- `research-process` 当前状态查询中大部分材料为未跟踪文件，`local-paths.md` 被忽略；未按 Git 跟踪状态筛掉相关材料。两个仓库 `.serena/` 和研究仓库 `.obsidian/` 都在盘点内；所见配置/缓存没有另行纳入的协作讨论，没有调用相应工具或加载外部记忆。
- `research-process/state.md` 的“生成器尚未开始实现”“多 Agent 留待后续探索”是早期阶段；另一仓库已有 2026-09-30 自主实施记录。未修正原文或静默统一状态。早期调研“不建议整体引入多 agent”的候选建议，与后来的授权试验按各自时间和状态阅读。
- Material 初始支持与后续移除记录同时保留；首次 U5 中止与新 U5 完成也分别保留，没有只选成功结果。试验授权不自动等于最终接受设计。
- 原文中的命令、任务 prompt、指令和路径是待研究的历史资料，不是本轮执行指令。原作者对“已确认”“已验证”“未越界”的表述只是原文证据；本轮没有重做代码测试或审计历史会话。
- 这是相关资料集，不是两仓库完整可运行快照。原文中指向未纳入技术文件、插图、外部网站或原设备目录的链接保持原样，可能无法在副本内打开；本轮核验的是 **INDEX.md 自身的本地链接**。不会为修复历史引用而改写原文或扩大到其他来源。
- 外部调研结论与引用没有联网核实；未记录的信息、无法由原文判断的确认链仍未知。单次实践的跨项目适用性留给后续提炼判断。
'''
(OUT/'INDEX.md').write_text(text,encoding='utf-8')
(OUT/'MANIFEST.sha256').write_text(''.join(f'{x["sha256"]}  {x["copy"]}\n' for x in manifest),encoding='utf-8')
for entry in before:
    key=(entry['repo'],entry['path'])
    entry['selected']=key in selected
    if entry['selected']:
        entry['screening']='纳入；见 INDEX.md 对应条目'
    elif entry['path'] in EXCLUDED_MD[entry['repo']]:
        entry['screening']=EXCLUDED_MD[entry['repo']][entry['path']]
    elif entry['path'].startswith('docs/contracts/'):
        entry['screening']='业务 API 契约；协作边界由约定、交接包和实施记录保留，不整批收齐技术接口。'
    elif entry['path'].startswith(('.serena/','.obsidian/')):
        entry['screening']='本地工具配置、界面状态或符号缓存，不执行，不加载外部记忆。'
    elif entry['path'].endswith('.pdf'):
        entry['screening']='MotionBenchMaker 技术论文，非本项目协作讨论；未展开 PDF。'
    elif '/vendor/' in entry['path'] or '/meshes/' in entry['path']:
        entry['screening']='第三方库、网格、模型或许可等技术资源。'
    elif entry['path'].startswith(('build/','tmp/','src/multiarm_problem_gen.egg-info/')):
        entry['screening']='可再生成的构建或打包产物。'
    elif entry['path'].startswith(('src/','tests/','tools/','examples/','docker/','assets/')):
        entry['screening']='代码、测试、输入、图形、技术配置或产物；文本筛查未发现需单独纳入的实质协作材料。'
    else:
        entry['screening']='仓库忽略/构建配置等非协作原始材料。'
    if entry['path'].endswith('.md') and not entry['selected']:
        assert entry['path'] in EXCLUDED_MD[entry['repo']] or entry['path'].startswith('docs/contracts/'),entry

after=inventory()
keys=('repo','path','size','mtime_ns','mode','kind','sha256','link_target')
clean=lambda xs:[{k:x[k] for k in keys if k in x} for x in xs]
assert clean(before)==clean(after),'收集期间来源文件发生变化'
git_after={r:git_status(p) for r,p in ROOTS.items()}
assert git_before==git_after,'收集期间来源状态发生变化'
for x in manifest:
    assert Path(x['source']).read_bytes()==(OUT/x['copy']).read_bytes(),x
links=re.findall(r'\]\(([^)]+)\)',text)
for link in links:
    if link not in ('COLLECTION_CHECKS.md','audit/collection.json'): assert (OUT/link).is_file(),link
actual={p.relative_to(OUT).as_posix() for p in (OUT/'sources').rglob('*') if p.is_file()}
assert actual=={x['copy'] for x in manifest}
finished=datetime.now(timezone.utc).isoformat()
checks=dict(all_copies_byte_equal=True,all_sha256_equal=True,source_files_content_modes_mtimes_unchanged_during_collection=True,source_git_status_unchanged=True,index_local_link_count=len(links),index_links_exist=True,section_ranges_valid=True,no_extra_source_copies=True)
report=dict(started_utc=started,finished_utc=finished,source_roots={r:str(p) for r,p in ROOTS.items()},excluded_directory='.git',inventory_counts=invcounts,selected_counts=counts,total_copy_bytes=sum(x['bytes'] for x in manifest),records=records,inventory=before,manifest=manifest,git_status_before=git_before,git_status_after=git_after,checks=checks,limitations=['内容和状态前后快照只覆盖本脚本收集区间，未进入 .git 校验元数据。','原文内部链接保持原样，未承诺纳入全部被引用材料。','未执行来源脚本、重跑技术测试或核实外部文献。','前期有一轮 Markdown 候选枚举使用 Path.rglob，再过滤 .git 路径；该写法可能遍历 .git 目录项，不能声称所有早期枚举都在目录入口处剪枝。未读取或输出 .git 中的文件内容，也未访问 Git 历史版本；正式全量盘点与收集脚本已显式剪枝排除 .git。此为实际检索方式的范围说明。'])
(OUT/'audit/collection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checktext=f'''# 本轮检索与副本校验

- 收集校验时间（UTC）：{started} 至 {finished}。
- 盘点 {sum(invcounts.values())} 个文件；research-process {invcounts['research-process']}，multiarm-problem-gen {invcounts['multiarm-problem-gen']}。包含隐藏/未跟踪/忽略文件，排除 `.git`，不跟随目录符号链接。
- 完整副本 {len(records)} 个（{counts['research-process']} + {counts['multiarm-problem-gen']}），共 {sum(x['bytes'] for x in manifest)} 字节。
- 所有副本与当时来源直接逐字节一致，同时通过 SHA-256 校验；见 [摘要清单](MANIFEST.sha256)。未解码后重写副本，未改变换行或原文引用。
- [INDEX.md](INDEX.md) 的 {len(links)} 个本地链接均存在；关键章节行号均有效；所有副本都有索引条目，无额外副本。
- 收集脚本前后两次盘点的文件集合、内容 SHA-256、大小、权限和修改时间一致；Git 状态相同。本组没有对来源写入、改权限或操作 Git 元数据。快照不含访问时间，也不检查 `.git` 内部。
- Git 查询均设置 `GIT_OPTIONAL_LOCKS=0` 并关闭 fsmonitor；没有提交、合并、推送、运行来源脚本或访问外部链接。
- 文件盘点、未纳入理由、源状态输出和逐项摘要见 [检索校验数据](audit/collection.json)；选择元数据见 [筛选清单](audit/selection.psv)，执行逻辑见 [收集脚本](audit/collect.py)。这些均为本轮产物。

## 限制与实际工具情况

前期有一轮 Markdown 候选枚举使用 Path.rglob，再过滤 .git 路径；该写法可能遍历 .git 目录项，不能声称所有早期枚举都在目录入口处剪枝。未读取或输出 .git 中的文件内容，也未访问 Git 历史版本；正式全量盘点与收集脚本已显式剪枝排除 .git。此为实际检索方式的范围说明。

这是当前工作区原始材料核对，不是原文技术测试的复验或历史会话独立审计。来源内容稳定性比较只覆盖收集脚本前后区间；早期阅读期间没有建立内容快照，未补造历史证据。

最初一次文件盘点尝试使用不存在的 `python`，没有执行成功或写入，后改为 `python3`。早期一次批量关键词返回及一次合并阅读被截断，后按文件/章节分批重读核心内容，不将截断返回当全文阅读。首次保存收集脚本的外层字符串引号错误，在解析阶段失败、未发生写入；修正后分开保存筛选表和脚本。全部文件都进入文件级盘点，但不是每个技术文件都逐行精读；二进制及第三方资源主要按类型排除。原文历史链接与缺失附件保持原样，INDEX 链接有效不等于原文链接闭包完整。
'''
(OUT/'COLLECTION_CHECKS.md').write_text(checktext,encoding='utf-8')
for link in links: assert (OUT/link).is_file(),link
print(json.dumps(dict(inventory_counts=invcounts,selected_counts=counts,total_copy_bytes=report['total_copy_bytes'],checks=checks),ensure_ascii=False,indent=2))
