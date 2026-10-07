# 人与 agent 长期协作：原始材料索引

采集时间：2026-10-07T10:41:26.202364+00:00。本目录仅汇集材料和建立索引，没有改写来源、制定统一规则或执行历史任务。

## 来源与检索边界

| 来源仓库 | 当前工作区根路径 | 全部普通文件（不含 .git） | 纳入文件 |
| --- | --- | ---: | ---: |
| research-process | `/home/fainic/data/research-process` | 53 | 23 |
| multiarm-problem-gen | `/home/fainic/data/multiarm-problem-gen` | 215 | 30 |

共纳入 **53 份完整原文**，位于 `sources/<仓库名>/<原相对路径>`。逐字节复制，不重排、不删节、不改链接；每份索引行的来源由仓库根路径加原相对路径确定。

检索以当前文件系统为准，包含隐藏、未跟踪和被忽略文件。初始使用 rg 枚举，按 Markdown 标题、状态、相关段落筛选，再完整阅读重点讨论和实施记录；补查配置、非 Markdown 文本及文件分布。全量清单阶段显式排除 .git，未访问历史版本、外部链接或旁支 worktree。仅使用设置 `GIT_OPTIONAL_LOCKS=0` 的 `git ls-files` 区分跟踪／未跟踪／忽略状态，没有提交、合并、推送或运行来源脚本。

本轮不是逐行审计所有业务代码：源码、模型、图片、第三方依赖、构建产物仅用于文件类型与相关性筛查，不因被已收笔记引用就递归纳入。初期 Markdown 枚举用了 pathlib.rglob，在筛选文件时排除了 .git；该方式可能遍历 .git 目录名，但没有打开 Git 对象或读取历史内容。后续改用预先剪枝的工作区枚举。

## 状态与证据读法

- **已确认**只按原文明示的确认范围标注；“现有约定文本”表示原文以约定呈现，不能由文件名反推每项都有可核查的用户确认。
- **候选建议**、实施前方案、agent 探索决定分别保留。方案获保存、代码获授权、用户最终接受设计是不同状态。
- **历史经验**包括成功、失败、纠正、停止和工具限制。所载测试数量、阅读边界和计时是原记录报告，本轮只校验文件副本，未重做其测试，也未独立审计其自述。
- 一个文件可混合多种状态；行内说明仅标示协作相关证据，不把其中所有业务语义视作通用规则。无法确认现行效力或独立证据的内容保留不确定性。

## 建议查阅的材料链（导航，不是新规则）

1. 长期记录形成：research-process 的起点、组织方式、README 与 AGENTS；再读 09-18 的已确认原则和候选调研。
2. 保留原意与独立审查：09-07／09-08／09-09 的研究讨论、09-15 的原文加补充、09-16 的“尚未确定”误解。
3. 从设计进入实现：multiarm 的实现单元／职责澄清、单元 1–3 方案与相应结果；对照 Material 删减记录。
4. 自主协作异常链：自主决定 D6-4 → 单元 5 准备停止 → 过滤后的单元 5／6 交接包 → 新单元 5 实施与自主试验总记录。

## research-process 文件索引

下列链接均指向本组副本；章节后的 L 数为该完整原文的行号。

| 原相对路径／副本 | 原文状态与确认边界 | 相关主题 | 纳入理由 | 关键章节 |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/research-process/AGENTS.md) | 现有约定文本；逐项确认过程未独立核实 | 上下文、授权、沟通、记录、Git | 集中保存跨 session 协作边界；本轮仅作为材料，不执行其中要求 | §开始工作（L9）；§长期记录更新（L18）；§内容组织（L30）；§配套资源管理（L48）；§维护与沟通（L63） |
| [README.md](sources/research-process/README.md) | 现有工作方式说明；第一版确认见起点记录 | 长期过程记录与使用循环 | 说明讨论、候选更新、审阅写入的循环及拆分文档的条件 | §使用循环（L21）；§维护（L33） |
| [overview.md](sources/research-process/overview.md) | 现行原则表述＋个人历史经验；不是普遍定律 | 先实践再完善、保留个人背景 | 保留工程原则的目标与个人经历，避免把个人提醒抽成绝对规则 | §工程原则（L17）；§个人经历与提醒（L24） |
| [state.md](sources/research-process/state.md) | 历史状态；原文称第一版工作流已确认 | 状态更新与待决事项 | 体现阶段、重点和未知的区分，也保留与后续代码仓库进展不一致的原始状态 | §当前阶段（L9）；§下一步（L20）；§待明确（L26）；§暂不展开（L33） |
| [projects/README.md](sources/research-process/projects/README.md) | 现有组织约定；逐项确认过程未独立核实 | 跨仓库分工、入口与拆分 | 说明项目记录、研究主线和设备路径的归属，避免重复维护 | §组织约定（L13） |
| [projects/dataset-generator/README.md](sources/research-process/projects/dataset-generator/README.md) | 历史状态＋待讨论；非确认需求 | 需求、验收与状态区分 | 保留待讨论问题不自动成为实现需求的具体记录方式 | §当前情况（L8）；§待讨论（L12） |
| [projects/stop-n-go/README.md](sources/research-process/projects/stop-n-go/README.md) | 用户报告＋尚待验证 | 事实来源与结果边界 | 明确复现来自用户报告，并未预先确认潜在不足 | §当前情况（L7）；§材料入口（L12） |
| [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md) | 原文明示：用户已确认讨论；历史经验 | 工作流形成、实践反馈 | 记录先跑流程再复盘的演变、长期记录目标及当时暂缓事项 | §工程思路的演变（L16）；§工作流目标（L28） |
| [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md) | 原文明示：用户已确认并采用；历史决定 | 内容分层、方案比较与复查 | 同时保存顾虑、备选、决定理由、复查条件和实际落实 | §问题与顾虑（L6）；§方案比较（L12）；§当前决定（L19）；§决策理由与复查条件（L32）；§落实（L38） |
| [inbox/README.md](sources/research-process/inbox/README.md) | 现有记录约定；逐项确认过程未独立核实 | 保留未成熟想法、写入确认 | 说明零散想法不强制任务化、整理确认和保留原始出处 | §随手记录（L1） |
| [experiments/README.md](sources/research-process/experiments/README.md) | 候选记录建议＋现有边界表述 | 实验记录与观察／猜测区分 | 原文明确使用建议语气，不把建议字段提升为强制模板 | §实验记录（L1） |
| [references/README.md](sources/research-process/references/README.md) | 现有维护约定＋历史阅读状态 | 论文主张、个人理解与来源 | 保留文献记录的归因原则及未完成阅读的标识 | §维护（L39） |
| [assets/README.md](sources/research-process/assets/README.md) | 现有资源管理说明；包含当次未执行事项 | 长期资源、版本、路径与同步 | 说明资源维护入口、派生导出、稳定引用及链接不等于同步 | §存放与引用（L10）；§版本与导出（L24）；§外部资源（L30） |
| [local-paths.md](sources/research-process/local-paths.md) | 本机约定与未填写状态；是否已落实无法判断 | 设备边界、忽略文件 | 被忽略的本地材料中直接涉及云端访问和设备专属路径，故仍纳入 | §本机路径（L1） |
| [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md) | 原文明示：用户原则及 agent 补充经讨论认可 | 渐进设计、best practice 与探索空间 | 区分共同语义、工程偏好、探索表达；同期 Git 和目录建议明确未在此确认 | §背景（L7）；§1. 在草稿纸上积累线索，逐渐形成整体设计（L13）；§2. best practice 提供倾向，保留表达与探索空间（L31） |
| [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) | 混合：用户目标／此前确认原则＋候选建议；非整体规范 | 学习目标、复杂度、证据、Git、可迁移经验 | 直接面向长期人与 agent 合作；保留研究、博客、论坛证据界限和未决事项 | §1. 用户希望通过这个项目获得什么（L7）；§2. 调研范围与证据边界（L21）；§6. 理解和管理 complexity 的候选方法（L100）；§8. Git 的候选使用方式（L122）；§9. 项目组织与信息记录的候选起点（L140）；§10. 怎样积累可迁移的经验（L163）；§11. 当前综合判断与未决事项（L187） |
| [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md) | 历史讨论与理解变化；尚非需求或方案 | 独立审查、修正而不倒写原意 | 具体展示 agent 提出遗漏问题、修正风险判断，并区分构造例子与实验 | §理解变化：端点描述与执行时序（L13）；§例子二：未经澄清的理解可能缩窄 planner 的能力范围（L49）；§未决问题（L71） |
| [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md) | 阶段性理解与候选方向；历史讨论 | 概念澄清、保留未展开想法 | 保留对用户含混判断的修正、依据范围和未确认改进设想 | §讨论背景（L5）；§二、对“暴力搜索、不理解时序”的修正（L40）；§六、保留但尚未展开的改进想法（L96）；§文献依据与阅读范围（L108） |
| [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md) | 历史独立审查；无本次实验结果 | 研究直觉、证据与反证 | 具体说明 agent 不把直觉当新发现、不把实验意图当已成立结论 | §用户的直觉与意图（L7）；§agent 的独立审查（L15）；§“用实验验证想法”的含义与边界（L25）；§尚未决定（L35） |
| [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) | 原文明示：完善表述经用户审阅确认；历史学习过程 | 原始表达与 agent 补充分别保存 | 保留原始理解、修正后说明及插图教学假设的区分，非采纳业务算法规则 | §用户原始表述（L11）；§用户补充表述：搜索（L15）；§与 agent 讨论后的完善表述（L19）；§补充讨论：路径拆分与基本方片（L90）；§配套插图（L131） |
| [assets/cube-complex/README.md](sources/research-process/assets/cube-complex/README.md) | 历史制作／维护说明；教学假设非实验 | 素材出处、生成入口与验证限制 | 是长期资源管理在共同构图中的实际案例；只收说明，不递归收数学插图和生成程序 | §用途与来源（L5）；§文件与维护入口（L13）；§生成方法（L25）；§记号与限制（L38） |
| [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md) | 历史个人思考＋具名 agent 补充；局部研究选择 | 保留用户声音、在原文旁澄清 | 用户随意草稿与 agent 独立补充并存；补充明确修正“大概率无法求解”的未经验证判断 | §碰撞矩阵（L19）；§联合空间中的进度表示（L36）；§终于有点眉目（L66） |
| [inbox/2026-09-16-generator-scene-and-target-representation.md](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md) | 混合：已确认业务方向＋未决项；历史沟通偏差 | 不替用户补完未决方案 | 原文记录用户要求标注尚未确定，agent 却提出组织方案；用户随后纠正，候选未被确认为设计 | §当前情况（L5）；§尚未确定：最终数据与名义场景的组织（L50）；§其他待讨论事项（L65） |

## multiarm-problem-gen 文件索引

| 原相对路径／副本 | 原文状态与确认边界 | 相关主题 | 纳入理由 | 关键章节 |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md) | 现有约定文本；逐项确认过程未独立核实 | 架构／实现分离、自主权限、阅读边界、测试与计量 | 保存代码协作完整约定，包含异常、已有上下文、工具回退和如实记录的处理 | §人与 agent（L9）；§记录（L21）；§实现与验证（L29）；§Git 与交接（L47）；§架构决策与自主权限（L67）；§从设计进入实现（L77）；§实现任务的阅读边界（L92）；§Serena 使用约定（L106）；§契约缺口与异常处理（L120）；§验证与记录（L135） |
| [README.md](sources/multiarm-problem-gen/README.md) | 现有项目入口＋探索状态说明 | 学习目标、跨库职责 | 明示用户参与架构以及自主探索不等于最终接受，并指出经验与实现文档的分工 | §从哪里开始（L7）；§仓库组织（L14）；§设计与学习（L29） |
| [docs/README.md](sources/multiarm-problem-gen/docs/README.md) | 现有记录组织说明＋历史阶段入口 | 讨论／实施分开、状态与证据归属 | 解释如何保存方案与实际结果，包含失败交接入口及尚未接受的自主试验状态 | §当前阶段（L3）；§讨论与方案（L18）；§实施过程与复盘（L39）；§接下来讨论（L53）；§怎样组织记录（L61） |
| [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md) | 现有 Git 约定文本；逐项确认过程未独立核实 | 探索分支、检查点、集成与操作授权 | 涉及建议不等于授权、保护无关修改、逻辑提交和组合行为检查 | §探索分支与长期主线（L3）；§何时提交与集成（L26）；§集成方式（L41）；§Commit message 的语言（L53）；§操作边界（L117） |
| [docs/design.md](sources/multiarm-problem-gen/docs/design.md) | 混合：原文称已确认语义＋历史候选＋未最终接受的自主决定 | 当前入口与历史状态并存 | 保留追加状态说明而不抹去旧方案的真实样本；开头与单元 3 段落存在刻意保留的时间层次 | §当前设计草稿（L1）；§单元 3：场景与统一资源管理（L34）；§候选抽象与待验证的问题（L89）；§未决事项（L101） |
| [docker/README.md](sources/multiarm-problem-gen/docker/README.md) | 现有环境／验收说明；所载执行结果未重跑 | 可复现环境、就绪判断、真实验收 | 包含空测试集不算验收、容器挂载不解除阅读边界、固定版本和独立阶段入口等协作执行条件 | §Docker／Compose 开发环境（L1）；§环境组织（L40）；§固定版本与来源（L48）；§自主试验：完整输入包入口与验收（L128） |
| [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md) | 历史决定：原文明确用户决定初始化；后续仍待讨论 | 仓库组织、学习目标、经验迁移 | 把已有协作目标落实到代码仓库；记录不急于引入编排、不把一次经验变通用规则 | §本次组织选择（L11）；§学习与协作目标（L17）；§前序材料（L23）；§下一步（L31） |
| [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md) | 混合：已确认方向／候选建议／后续修正；历史过程 | 最小但完整、具体例子推动讨论 | 实际样例与可视化暴露新问题；保留从候选到确认的过程而不静默默认 | §目标（L7）；§已确认的选择（L13）；§“最小但完整”的含义（L24）；§追加：基准场景与可视化暴露的三个问题（L58）；§追加：问题 1、2 的方案（L122）；§追加：问题 3 的方案（L166） |
| [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md) | 历史讨论＋局部选择；非完整定稿接口 | 用户质疑、实际测量、删减抽象 | 具体记录 agent 提案被用户质疑后实测并调整，说明抽象如何逐步修正 | §从读取结果谈起（L9）；§Mesh：从提前解析转向按需加载（L37）；§Pose、Frame 与场景复用（L47）；§后续计划（L99） |
| [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md) | 历史讨论方案；精确契约待确认 | 用流程解释设计、避免术语负担 | 用户要求解释每一步及对象协作，记录表达方式与职责取舍的调整 | §从对象清单转向运行流程（L7）；§运行流程与职责（L15）；§边界与后续（L50） |
| [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) | 六单元方案未全部定稿；单元 1 已被用户选择 | 任务粒度、依赖与验收 | 明确独立交付单元不等于类／文件；任务前契约、修改范围、验收的具体应用 | §划分方案（L7）；§路径与共享资源的归属（L22）；§建议实现顺序（L43） |
| [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md) | 候选方案的历史澄清；未在此决定合拆任务 | 代码职责与上下文隔离 | 直接分析任务划分如何影响契约隔离实验，而非只按文件划分 | §问题与澄清（L7）；§对契约隔离实验的影响（L25） |
| [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md) | 混合：确认语义与可变性＋候选接口；不是实现授权 | 人参与设计、预先限定验收与权限 | 保留用户纠正全不可变提案、确认范围和实现前仍需补齐的信息 | §构造、引用与可变性（L31）；§校验职责（L51）；§首次交付与验收（L68）；§实现前还需补齐（L80） |
| [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md) | 已讨论实施方案；原文明确尚非执行授权 | 设计到独立实现、分阶段验收 | 给出公开契约先行、独立实现阅读范围、验收就绪判断和未实际执行的区分 | §第一部分：统一 Docker／Compose 环境（L7）；§第二部分：单元 1 基础表示（L43）；§执行顺序、权限与就绪判断（L85） |
| [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md) | 已确认方向＋待具体化接口；写入不等于实现授权 | 修正设计、范围控制、依赖契约 | 用户确认统一表示后修正旧建议；明确“完整”不自动扩大能力范围和局部自主边界 | §目标与本次修正（L7）；§错误与验收（L118）；§实施范围与准备（L126） |
| [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md) | 确认职责／范围＋候选签名＋未来未决；历史方案 | 就绪评估、允许修改与读取边界 | 保留用户纠正、提前调整样例与后续实现的区分，以及不能借完善契约扩大范围 | §本轮选择与保留方向（L90）；§验收与允许修改范围（L119）；§实施准备判断（L137） |
| [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md) | 探索性 agent 决定；明确非用户最终接受 | 独立决策、信息包、复议与交接污染 | 保存备选理由、最小依赖扩展、D5-3 消歧和 D6-4 内部断言进入信息包的来源 | §信息包与边界（L5）；§阅读、用量与时间（L33）；§D6-1：先补公开资源快照（L39）；§D5-3：mean 的 configuration 名称消歧（L140）；§D6-4：既有真实样例测试的单字符串维护（L148） |
| [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md) | 过滤后的探索性公开交接；非用户最终接受 | 交接材料过滤与隔离范围 | 与停止记录对读，保留实际交接包全文；其技术正文是该机制证据，不作为统一规则 | §单元 5 公开交接包（L1）；§D5-1：保留 YAML，公开统一作用关联（L5）；§D5-3：mean 的 configuration 名称消歧（L47） |
| [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md) | 过滤后的探索性公开交接；非用户最终接受 | 实现者与集成者责任分开 | 明示共享入口和旧验收元数据由主 agent 维护，保留依赖隔离的实际资料 | §单元 6 公开交接包（L1）；§D6-1：先补公开资源快照（L5）；§D6-3：真实样例最小迁移与验收（L45） |
| [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md) | 历史实施自述与所载验收；提交确认仅属当次 | 工具限制、真实验收、独立上下文限制 | 包括网络失败、非空验收、契约够用判断，明确并非另开上下文的双 agent 实验 | §环境验收（先于基础表示实现）（L13）；§基础表示验收（L28）；§契约是否足够（L45）；§阅读范围与工具限制（L53）；§交接（L68） |
| [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md) | 历史实施；后续 Material 修正另有记录 | 修正测试预期、验证边界与工具回退 | 记录手工数量错误被独立计数纠正，区分自述与证明，保留旧实现与后续修正 | §起点与完成内容（L7）；§实际验证（L17）；§契约与阅读边界（L39）；§剩余边界与局部不足（L49） |
| [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md) | 用户明确确认的当次删减＋历史实施 | 审查反馈、克制范围、历史修正 | 独立审查发现真实需求依据不足后授权收缩接口，原记录保留并链接修正 | §原因与变更（L5）；§验证与边界（L13） |
| [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md) | 历史实施自述与所载测试结果 | 独立预期、契约不弱化、计量诚实 | 错误缓存预期修正、局部缺陷补测、保持既有用户修改，以及无法精确拆分计时的说明 | §测试目的与依据（L16）；§实际结果（L30）；§阅读范围与工具边界（L51）；§用时与 token（L69）；§契约判断及剩余限制（L82） |
| [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) | 授权范围内探索历史；最终设计未接受 | 多 agent 分工、失败修复、集成与成本 | 联结决定、分项实施、上下文停止与重启、集成检查；整体数据不等于独立审计 | §起点与边界（L5）；§任务与决定入口（L21）；§主 agent 集成测试目的（编写前）（L34）；§最终验收事实（L40）；§结果、决定与限制（L63）；§用量与计时（L71） |
| [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md) | 历史异常／未完成准备；未执行测试 | 间接越界、及时披露、停止上下文 | 原决定含内部断言导致上下文污染，即使未主动打开依赖测试也不再宣称纯隔离 | §实际产物与停止原因（L5）；§实际阅读（L11）；§时间、用量与边界（L17） |
| [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md) | 探索性补丁历史；最终设计未接受 | 公开契约补丁、独立测试、混合计时 | 体现依赖缺口通过专属任务处理，交接验证与亲自验证分开、工具回退限定范围 | §范围与测试目的（编写测试前）（L5）；§执行结果（L13）；§实际阅读与工具边界（L21）；§时间与用量（L29） |
| [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md) | 探索性独立实施历史；最终设计未接受 | 专属任务范围、独立预期与交接 | 保存不改共享入口、主 agent 验证不算自身证据、计时与自述限制 | §完成内容（L7）；§测试目的与独立依据（L14）；§阅读范围与工具（L37）；§时间、用量与未决项（L51） |
| [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md) | 重启后的独立探索历史；最终设计未接受 | 过滤交接、自审回修、测量边界 | 保留新上下文未继承旧实现、真实样例核对、非法输入修复及新增文件检查限制 | §测试目的、依据与结果（L11）；§读取边界与用量（L31）；§契约与局限（L46） |
| [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md) | 独立探索实施历史；最终设计未接受 | 集成分工、限定读取、补测与边界 | 体现实现者与主 agent 分工、公开声明读取、真实搬移验证及未过度推断成功 | §完成范围（L5）；§测试目的与依据（L15）；§实际结果（L23）；§契约、阅读与工具（L40）；§用时与用量（L56） |
| [tools/baseline_validation/ur7e_table/README.md](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) | 历史检查及部分后续更新；未全部重验 | 旧报告失效、不可夸大验证、保留原结果 | 包含输入变化后旧哈希失效、缺依赖未重跑碰撞、历史原型不冒充新要求的具体证据 | §数值检查及其范围（L95）；§目录整理说明（2026-09-21）（L125） |

## 未纳入的 Markdown 材料

逐项保留理由，便于后续调整范围。排除只表示本轮相关性判断，不表示这些材料无价值。

| 来源 | 原相对路径 | 未纳入理由 |
| --- | --- | --- |
| research-process | `journal.md` | 空文件。 |
| research-process | `assets/path-collision-equivalence/README.md` | 主体为教学可视化使用说明；通用资源维护约定和具体来源／限制案例已收 assets 总入口与 cube-complex 说明。 |
| research-process | `inbox/2026-09-09-coordination-space-reading-guide.md` | 主体为领域文献导览；有来源／候选提示，但没有独立的协作流程变化或复盘，已收相关独立审查记录。 |
| research-process | `inbox/2026-09-09-multi-arm-research-focus.md` | 主体为研究关注点和业务选择；关键协作澄清已在 09-07、09-08、09-09 独立审查材料中保留。 |
| research-process | `inbox/2026-09-14-todos-and-draft.md` | 简短业务阅读待办与草稿意向，没有具体协作约定、决策理由或实践结果。 |
| research-process | `inbox/2026-09-17-generator-input-output-format.md` | 主体为领域格式与样例；未决／确认分层已有更直接协作材料，不收全部技术格式版本。 |
| research-process | `inbox/2026-09-18-generator-input-output-format.md` | 主体为领域格式与样例；版本保留方法已有起点／记录约定说明，不收全部技术格式版本。 |
| research-process | `references/lavalle-planning-algorithms-7-2-multiple-robots.md` | 主体为领域阅读笔记与材料导航；原始理解和补充写作方式已收对应讨论记录。 |
| research-process | `references/stac-reading-notes.md` | 主体为论文算法和实验设置笔记；虽有 agent 补充及证据限定，本轮不扩展成领域文献全集。 |
| research-process | `references/stop-n-go-reading-notes.md` | 论文元信息及空的阅读／个人理解栏目，缺少实质协作内容。 |
| multiarm-problem-gen | `docs/contracts/distributions.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/generation.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/input-bundle.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/primitives.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/resources.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/robot-model.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/contracts/scene.md` | 领域 API 技术契约；本轮收录交接机制、缺口处理和验证经验，不完整搬运契约集合。 |
| multiarm-problem-gen | `docs/notes/discussions/2026-09-18-input-output-format.md` | 主体为领域格式方案快照；跨库维护分工及候选状态已收仓库起点，不递归复制全部业务方案。 |
| multiarm-problem-gen | `docs/notes/discussions/2026-09-21-output-validity-semantics.md` | 主体为业务输出保证；并非协作规范，验收边界的实际处理已收实施记录。 |
| multiarm-problem-gen | `docs/notes/discussions/2026-09-23-generation-distributions.md` | 主体为分布及作用语义的局部设计；渐进讨论案例已有更直接的提案修正与流程解释材料。 |
| multiarm-problem-gen | `docs/notes/discussions/2026-09-23-input-bundle.md` | 主体为输入包组织与发现规则；协作层面已收实现单元、独立决策及公开交接包。 |
| multiarm-problem-gen | `examples/ur7e_table/README.md` | 主体为输入包调用与业务内容；样例迁移、复现和验证限制已在所收实施／基准记录中说明。 |
| multiarm-problem-gen | `tools/model_preparation/ur7e_2f85/README.md` | 主体为模型准备与来源文件位置；不将技术工具完整收为协作材料。 |
| multiarm-problem-gen | `tools/model_preparation/ur7e_2f85/resources-original.md` | 模型资源来源快照，不是人与 agent 工作方式证据。 |
| multiarm-problem-gen | `tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md` | 第三方上游技术说明，不是本项目协作约定或过程。 |
| multiarm-problem-gen | `tools/scene_preview/README.md` | 主体为原型使用说明；原型触发讨论的经过已收首份输入样例记录。 |

其他未纳入类别：业务源码和测试、YAML／URDF 输入、STL／DAE 模型、SVG／PNG 插图、论文 PDF、第三方 JS／许可证、wheel／build／egg-info、Serena 缓存与默认配置、Obsidian UI 状态。配置筛查中未发现另一个非空项目 prompt 或实质协作记忆；两份 Serena project.yml 的 initial_prompt 均为空。被忽略的 local-paths.md 因直接涉及访问和设备边界而已纳入。

## 不确定性与原文关系

- research-process 的 state 和项目入口仍有“尚未开始”等历史表述，与 multiarm 的后续实施记录不同；未替来源更新，也未据此认定代码尚未实现。
- docs/design.md 保留先“尚未实现”、后“实施补充”的时间层次；09-30 自主单元 4–6 的设计接受状态仍是未最终接受。
- 两个仓库的写入、架构和 Git 授权约定各有范围；本轮不调和差异，也不把某轮探索授权变成永久权限。
- 原文中的外部研究和链接没有联网核对；不据这些历史引文断言当前产品或研究结论。
- 为保持原样且避免把纯业务材料全部纳入，来源内部的链接／插图不保证在本副本集合内完整闭合。INDEX 的文件链接均已验证有效；原文内缺失引用单列在核验 JSON 中，没有修改原文补链。
- 非 Markdown 业务文件未全部逐行阅读，无法证明没有任何藏于代码注释中的协作经验；已进行关键词补查。

## 复制与核验

- [副本清单与 SHA-256](audit/manifest.json)：每个文件的原绝对路径、相对副本路径、字节数、来源 Git 状态和哈希。
- [全量工作区文件清单](audit/inventory.json)：两仓库当前普通文件、内容哈希与纳入状态，不含 Git 元数据。
- [核验结果](audit/verification.json)：逐字节比较、源文件采集前后哈希、INDEX 路径与关键章节定位检查，以及原文内部引用的缺失情况。
- [筛选元数据](audit/catalog.json)：逐文件主题、理由、状态与章节。
- [本轮采集与校验程序](audit/collect.py)：仅对指定 worktree 写入，不运行来源代码。
