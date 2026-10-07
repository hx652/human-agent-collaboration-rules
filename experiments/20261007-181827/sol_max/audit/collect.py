from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import os
import re
import stat
import sys

WORKTREE = Path('/home/fainic/data/human-agent-collaboration-rules-worktrees/20261007-181827/sol_max')
ROOTS = {
    'research-process': Path('/home/fainic/data/research-process'),
    'multiarm-problem-gen': Path('/home/fainic/data/multiarm-problem-gen'),
}
assert Path.cwd() == WORKTREE and WORKTREE.resolve() == WORKTREE
AUDIT = WORKTREE / 'audit'
assert AUDIT.resolve().is_relative_to(WORKTREE)

def write_json(name, data):
    target = AUDIT / name
    assert target.resolve().is_relative_to(WORKTREE)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def scan():
    result = {'captured_at_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'Current workspaces, hidden and ignored entries included; every .git entry excluded; no symlink traversal.', 'repositories': {}}
    for name, root in ROOTS.items():
        files = []
        for base, directories, filenames in os.walk(root, followlinks=False):
            directories[:] = sorted(d for d in directories if d != '.git' and not Path(base, d).is_symlink())
            for filename in sorted(filenames):
                if filename == '.git':
                    continue
                path = Path(base, filename)
                info = path.lstat()
                item = {'path': path.relative_to(root).as_posix(), 'size_bytes': info.st_size, 'mtime_ns': info.st_mtime_ns}
                if stat.S_ISREG(info.st_mode):
                    item.update(kind='regular', sha256=sha256(path.read_bytes()))
                elif stat.S_ISLNK(info.st_mode):
                    item.update(kind='symlink', target=os.readlink(path))
                else:
                    item['kind'] = 'other'
                files.append(item)
        result['repositories'][name] = {'root': str(root), 'files': sorted(files, key=lambda x: x['path'])}
    return result

def sections(text, wanted):
    lines = text.splitlines()
    headings = []
    fenced = False
    for i, line in enumerate(lines, 1):
        if line.startswith('```') or line.startswith('~~~'):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
        if match:
            headings.append({'title': match.group(2), 'level': len(match.group(1)), 'start_line': i})
    found = []
    for title in wanted:
        matches = [h for h in headings if h['title'] == title]
        if len(matches) != 1:
            raise ValueError('Heading not unique / absent: ' + repr(title))
        current = dict(matches[0])
        following = [h for h in headings if h['start_line'] > current['start_line'] and h['level'] <= current['level']]
        current['end_line'] = following[0]['start_line'] - 1 if following else len(lines)
        found.append(current)
    return found

baseline = json.loads((AUDIT / 'source-inventory.before.json').read_text(encoding='utf-8'))
spec = json.loads((AUDIT / 'selection-spec.json').read_text(encoding='utf-8'))
tracking = json.loads((AUDIT / 'current-file-tracking.json').read_text(encoding='utf-8'))
base_maps = {name: {x['path']: x for x in info['files']} for name, info in baseline['repositories'].items()}
manifest = []
payloads = []
for annotation in spec:
    name = annotation['repository']
    relative = Path(annotation['path'])
    assert not relative.is_absolute() and '..' not in relative.parts and '.git' not in relative.parts
    source = ROOTS[name] / relative
    assert source.resolve().is_relative_to(ROOTS[name]) and stat.S_ISREG(source.lstat().st_mode)
    data = source.read_bytes()
    assert sha256(data) == base_maps[name][relative.as_posix()]['sha256'], 'Source changed before copy: ' + str(source)
    key_sections = sections(data.decode('utf-8'), annotation['key_headings'])
    destination = WORKTREE / 'sources' / name / relative
    assert destination.resolve().is_relative_to(WORKTREE / 'sources')
    state = next((kind for kind, paths in tracking[name]['groups'].items() if relative.as_posix() in paths), 'unclassified')
    item = dict(annotation)
    item.update(original=str(source), copy=destination.relative_to(WORKTREE).as_posix(), size_bytes=len(data), sha256=sha256(data), tracking=state, key_sections=key_sections)
    manifest.append(item)
    payloads.append((destination, data))

# All content and heading checks pass before any source copy is created.
for destination, data in payloads:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    assert destination.read_bytes() == data
write_json('collected-manifest.json', manifest)

excluded_reasons = {
    ('research-process', 'journal.md'): '空文件，没有可索引内容。',
    ('research-process', 'inbox/2026-09-09-multi-arm-research-focus.md'): '研究关注点与业务范围；相关的人与 agent 澄清过程已在纳入的 09-07、09-08、09-09 讨论中保存。',
    ('research-process', 'inbox/2026-09-14-todos-and-draft.md'): '简短历史待办，无明确协作约定或实际尝试、决策、复盘；本轮不执行待办。',
    ('research-process', 'inbox/2026-09-17-generator-input-output-format.md'): '完整数据 schema 与样例为主要内容；协作中的范围误解与纠正在纳入的 09-16 记录中保存。',
    ('research-process', 'inbox/2026-09-18-generator-input-output-format.md'): '完整数据格式方案为主要内容；格式技术细节不整体归入协作经验。',
    ('research-process', 'references/stop-n-go-reading-notes.md'): '简短个人算法理解，没有明确的人与 agent 互动或协作方法证据。',
    ('multiarm-problem-gen', 'docs/notes/discussions/2026-09-18-input-output-format.md'): '完整输入输出字段与 YAML 样例；技术 schema 不整体纳入，相关协作澄清已有单独过程记录。',
    ('multiarm-problem-gen', 'tools/model_preparation/ur7e_2f85/README.md'): '模型构建与交付资源的技术入口；维护与历史追溯经验已由纳入的基准 README 和过程记录保存。',
    ('multiarm-problem-gen', 'tools/model_preparation/ur7e_2f85/resources-original.md'): '上游模型来源、许可证与旧资源路径快照；不是人与 agent 协作经验。',
    ('multiarm-problem-gen', 'tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md'): '上游厂商软件说明；与本项目人与 agent 协作无直接内容关联。',
}
def exclusion_reason(name, path):
    key = (name, path)
    if key in excluded_reasons:
        return excluded_reasons[key]
    parts = Path(path).parts
    if '.serena' in parts:
        return '本地工具配置／缓存；初始提示为空，未发现额外项目协作材料；缓存未反序列化。'
    if '.obsidian' in parts:
        return '编辑器界面和工作区配置，非讨论、决定或协作经验记录。'
    if 'vendor' in parts:
        return '上游依赖源码、模型、许可证或网格；不作为本项目协作规则材料。'
    if name == 'research-process' and 'assets' in parts:
        return '图形、教学页面、绘图实现或导出；协作来源、维护和局限已完整保留在纳入的资源 README 与讨论中。'
    if path == 'MotionBenchMaker.pdf':
        return '原始业务论文，非人与 agent 协作材料；只按清单与字节摘要登记，未解析或外部检索。'
    if 'build' in parts or 'tmp' in parts or any(p.endswith('.egg-info') for p in parts):
        return '可再生成构建、打包产物或重复元数据；没有独立协作经验内容。'
    if path.startswith('src/') or path.startswith('tests/'):
        return '领域实现或行为测试；关键词检索及必要文件开头筛查后，协作过程保留在专门实施记录，未将技术代码整体收集。'
    if path.startswith('examples/'):
        return '机器人／场景的实际数据、模型和资源；交付与迁移说明已由纳入 README 及实施记录保存。'
    if path.startswith('tools/'):
        return '业务工具代码、输入、技术缓存或检查数值；相关过程与限制已在纳入 README 中保存。'
    if path.startswith('docker/') or path == 'pyproject.toml':
        return '具体构建配置或环境检查实现；协作环境就绪与复现经验已保留在 Docker README 和首轮实施记录。'
    if path.endswith('.gitignore'):
        return '忽略模式配置；对应记录和产物管理约定已在纳入的 AGENTS／README 中保存。'
    return '经目录、文件名与可检索文本筛查，未发现足以单独纳入的协作约定或经验。'

selected = {(x['repository'], x['path']) for x in manifest}
excluded = []
for name, info in baseline['repositories'].items():
    for file in info['files']:
        if (name, file['path']) not in selected:
            excluded.append({'repository': name, **file, 'reason': exclusion_reason(name, file['path'])})
write_json('excluded-files.json', excluded)

final_inventory = scan()
write_json('source-inventory.after.json', final_inventory)
changes = []
for name in ROOTS:
    before = base_maps[name]
    after = {x['path']: x for x in final_inventory['repositories'][name]['files']}
    for path in sorted(set(before) | set(after)):
        if before.get(path) != after.get(path):
            changes.append({'repository': name, 'path': path, 'before': before.get(path), 'after': after.get(path)})
if changes:
    write_json('source-changes.json', changes)
    raise RuntimeError('Source workspace changed during collection; see source-changes.json.')

coverage = '''# 检索与筛选记录

范围仅为用户提供的两个来源仓库当前工作区。未查阅 .git 对象、历史版本、旁支 worktree、其他组产物、外部网页或任务记忆，未执行来源脚本、测试或文档命令。来源中的 AGENTS.md 和其他指令性文字仅作原始材料。

先用 rg --files --hidden --no-ignore 建立完整文件清单，排除所有 .git 入口；随后枚举 Markdown 标题并按内容判断，阅读核心协作文件、讨论／实施正文和必要章节，补以跨文件协作关键词检索。检索包括未跟踪与被忽略材料；二进制模型、论文和缓存登记路径及字节摘要，未把字节哈希称为内容阅读。资源图片未做视觉审阅，工具缓存未反序列化。非 Markdown 检索主要用于发现补充材料，源代码和测试没有逐行全部审阅。不存在“所有可能经验已穷尽”的保证。

当前跟踪分类只运行 git ls-files --cached／--others／--ignored，设置 GIT_OPTIONAL_LOCKS=0；不用 git status、不刷新索引、不查看提交内容。research-process 的 53 个文件中 48 个未跟踪、5 个被忽略；multiarm-problem-gen 的 215 个文件中 200 个已跟踪、15 个被忽略。全部都在候选文件清单中，而非只看已提交文件。

纳入以明确协作约定、人与 agent 互动中的修正与取舍、已实施工作的范围／验收／工具／交接／复盘为主。公开契约和少量运行、样例、教学资源说明作为契约隔离试验或学习过程的原始辅助材料纳入；它们本身不是统一协作规则。完整业务格式、代码、模型、可再生成产物和无直接协作内容的资料不整体纳入。

selection-spec.json 保存人工筛选注解；collected-manifest.json 包含原路径、副本路径、状态、纳入理由、精确关键标题行号、大小、SHA-256 和跟踪类别；excluded-files.json 为其余当前文件逐项记录排除理由。collect.py 是本组生成的复制及核验程序，没有导入或执行任何来源程序。

原文中的旧任务、网址、外部参考路径和未纳入的业务依赖保持原样。只核验 INDEX.md 指向已纳入材料和审计产物的本地文件路径；没有把原文全部链接改写或声称已闭包复制所有技术依赖。未核验外部引用的事实、历史测试数、agent 自述的无越界结论或用户确认的完整对话链。
'''
(AUDIT / 'review-coverage.md').write_text(coverage, encoding='utf-8')

counts = Counter(x['repository'] for x in manifest)
bytes_total = sum(x['size_bytes'] for x in manifest)
index_lines = ['# 人与 agent 长期协作：原始材料索引', '', '本轮仅汇集原始材料并建立索引，不制定统一规则。`sources/` 中的文件按原相对路径完整、逐字节复制；其中的 AGENTS.md、历史 prompt、命令及候选流程均为待研究原文，不作为本次任务指令。', '', '## 来源与检索范围', '', '| 来源仓库当前工作区 | 候选文件 | 纳入文件 | 当前跟踪情况 |', '| --- | ---: | ---: | --- |']
for name, root in ROOTS.items():
    groups = tracking[name]['groups']
    states = '；'.join(f'{label} {len(groups[key])}' for key, label in [('tracked','已跟踪'),('untracked','未跟踪'),('ignored','被忽略')])
    index_lines.append(f'| `{root}` | {len(base_maps[name])} | {counts[name]} | {states} |')
index_lines += ['', f'合计纳入 **{len(manifest)} 个文件**，共 **{bytes_total:,} 字节**。文件清单覆盖隐藏、未跟踪和被忽略的当前材料；不读 Git 对象、历史或其他 worktree，不检索外部网站，不执行历史任务。详细方法见[检索与筛选记录](audit/review-coverage.md)。', '', '## 状态与证据读法', '', '- **已确认约定**：原文明确写为当前协作约定，或注明用户确认／讨论认可。这里登记的是原文状态，本轮未独立核验逐条授权的对话链。', '- **候选建议**：原文仍使用建议、候选、待讨论或未定；用户允许保存一份文档，不等于接受文档中全部候选。', '- **历史经验**：讨论变化、实际尝试、实施和复盘记录。原文中的测试数量、阅读范围和耗时保留其自述及统计局限，本轮没有重跑。', '- **授权自主试验**：已授权执行且可能已实现的 agent 决定，仍不等于用户最终接受设计；表中单独标明，不升级为已确认长期约定。', '- **辅助材料／无法判断**：具体公开契约、运行入口、教学与项目背景用来理解协作情境；无法据原文判断确认程度的注明限制。领域技术语义不会自动变为协作规则。', '', '每个文件可同时含多类内容，表中的状态与关键章节按原文区分。章节行号是所复制当前文件的实际行号。', '', '## 主题入口', '', '| 相关主题 | 主要原始材料 |', '| --- | --- |', '| 长期记录、审阅与授权、跨 session 上下文 | [研究仓库协作约定](sources/research-process/AGENTS.md)、[第一版工作方式](sources/research-process/journal/2026-09-07-starting-point.md)、[组织决定](sources/research-process/journal/2026-09-07-record-organization.md) |', '| 用户学习、渐进设计、best practice 与流程成本 | [已确认的两条原则](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md)、[协作目标与候选调研](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) |', '| 独立判断、澄清原意、保留理解变化 | [研究直觉的独立审查](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md)、[不要代补未决方案的实例](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md)、[原始表述与完善版本](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) |', '| 架构与实现、任务粒度、契约及自主权限 | [代码仓库协作约定](sources/multiarm-problem-gen/AGENTS.md)、[任务与职责的区别](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md)、[实现单元划分](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) |', '| 独立决策、多 agent 交接及阅读污染 | [自主决定](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md)、[中止记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md)、[过滤后 U5 交接](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md)、[整轮结果](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) |', '| 测试目的、独立预期、真实统计与限制 | [单元 3 记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md)、[单元 5 记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md)、[历史基准检查边界](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) |', '| Git、交付范围、保留旧记录与必要修正 | [Git 工作约定](sources/multiarm-problem-gen/docs/git-workflow.md)、[接口收缩复盘](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md)、[文档组织说明](sources/multiarm-problem-gen/docs/README.md) |', '', '## 文件索引']
for name in ROOTS:
    index_lines += ['', '### ' + name, '', '原始来源：`' + str(ROOTS[name]) + '`。表内文件路径均相对于该仓库根目录；链接指向本组副本。', '']
    for kind in ['协作约定','讨论与决策','背景与历史经验','实施与复盘','辅助材料']:
        subset = [x for x in manifest if x['repository']==name and x['kind']==kind]
        if not subset:
            continue
        index_lines += ['#### ' + kind, '', '| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |', '| --- | --- | --- | --- |']
        for item in subset:
            key_refs = '；'.join(f'“{s["title"]}”（L{s["start_line"]}–{s["end_line"]}）' for s in item['key_sections'])
            cells = [f'[{item["path"]}]({item["copy"]})', item['status'], item['topics'] + '。' + item['reason'], key_refs]
            index_lines.append('| ' + ' | '.join(c.replace('|','\\|').replace('\n',' ') for c in cells) + ' |')
        index_lines.append('')
index_lines += ['## 尚未消除的不确定事项', '', '1. research-process 的 state.md 和项目入口仍写生成器尚未实现；代码仓库已有 09-29／09-30 后续实施记录。两者原样保留，研究侧旧快照不用于否定后续成果。', '2. docs/design.md 保留旧方案段落，并在顶部追加已实现与自主试验状态；当前公开契约与旧候选不能混为同一时点的决定。', '3. 单元 4–6 的 agent 决定、公开交接包和实施结果均明确不代表用户接受最终设计。本轮无法从当前文件确认其之后是否获接受；不查历史或聊天补结论。', '4. 越界中止、测试数量、无越界自述和用时统计是原始记录中的历史声明，没有独立工具日志闭包。本轮仅验证副本一致，不重新证明历史实验。', '5. 外部论文、博客、论坛和厂商链接保持原文；本轮没有访问或核验其最新内容，也不将调研中的候选流程当已确认规范。', '6. 来源中的技术依赖、模型、代码、图形和部分纯业务文档未全部收集；原文内引用保持原样，可能指向未纳入内容。INDEX 指向纳入副本及审计文件的本地路径已核验，未声称全部原文链接或外部路径都可用。', '', '## 检查与筛选记录', '', f'- {len(manifest)} 份副本均与当前原文逐字节一致，SHA-256 和大小逐项登记；关键标题均唯一匹配到原文实际行号。', '- 复制前后，两个来源共 268 个非 .git 当前文件的路径、种类、大小、内容摘要及修改时间一致；没有将来源权限或 Git 元数据作为写入目标。', '- 本轮未提交、合并或推送，未运行来源脚本、原测试、历史命令或外部检索。', '- [逐文件原文与副本清单](audit/collected-manifest.json)、[候选文件初始清单](audit/source-inventory.before.json)、[结束清单](audit/source-inventory.after.json)。', '- [人工筛选注解](audit/selection-spec.json)、[未纳入文件与原因](audit/excluded-files.json)、[当前跟踪分类](audit/current-file-tracking.json)、[检索范围与限制](audit/review-coverage.md)。', '- [本轮核验结果](audit/verification.json)。']
(WORKTREE / 'INDEX.md').write_text('\n'.join(index_lines) + '\n', encoding='utf-8')

index = (WORKTREE / 'INDEX.md').read_text(encoding='utf-8')
local_links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', index)
link_errors = []
for target in local_links:
    if target == 'audit/verification.json':
        continue
    path = WORKTREE / target.split('#',1)[0]
    if not path.is_file() or not path.resolve().is_relative_to(WORKTREE):
        link_errors.append(target)
actual_copies = sorted(p.relative_to(WORKTREE).as_posix() for p in (WORKTREE/'sources').rglob('*') if p.is_file())
expected_copies = sorted(x['copy'] for x in manifest)
assert actual_copies == expected_copies
checks = []
for item in manifest:
    original = Path(item['original']).read_bytes()
    copy = (WORKTREE/item['copy']).read_bytes()
    checks.append({'path': item['copy'], 'bytes_equal': original == copy, 'size_equal': len(copy)==item['size_bytes'], 'sha256_equal': sha256(copy)==item['sha256']})
assert not link_errors and all(all(v for k,v in c.items() if k!='path') for c in checks)
verification = {'verified_at_utc': datetime.now(timezone.utc).isoformat(), 'worktree': str(WORKTREE), 'selected_files': len(manifest), 'counts_by_repository': dict(counts), 'collected_bytes': bytes_total, 'per_file': checks, 'all_copies_match_original': True, 'inventory_scope_files': sum(len(x['files']) for x in baseline['repositories'].values()), 'source_inventory_and_bytes_and_mtime_unchanged': True, 'source_changes': changes, 'index_local_links_checked': len(local_links), 'index_broken_local_links': link_errors, 'index_sha256': sha256((WORKTREE/'INDEX.md').read_bytes()), 'key_headings_checked': sum(len(x['key_sections']) for x in manifest), 'unselected_files': len(excluded), 'original_links_not_claimed_valid': True, 'source_scripts_or_tests_executed': False, 'git_history_or_objects_read': False, 'commits_merges_pushes': False, 'external_sources_accessed': False, 'notes': ['Only source-workspace ls-files read; optional locks disabled.', 'Historical reports remain unverified claims; this run verifies collection only.', 'Source .git entries and symlink directory traversal excluded.']}
write_json('verification.json', verification)
assert (WORKTREE/'audit/verification.json').is_file()
print(json.dumps({k:verification[k] for k in ['selected_files','counts_by_repository','collected_bytes','all_copies_match_original','source_inventory_and_bytes_and_mtime_unchanged','index_local_links_checked','index_broken_local_links','key_headings_checked','unselected_files']},ensure_ascii=False))
