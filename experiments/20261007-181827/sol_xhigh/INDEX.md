# 人与 agent 长期协作原始材料索引

汇集时间：2026-10-07T10:33:47.853847+00:00。本轮仅汇集当前工作区原始材料并建立索引；副本按字节完整保存，未改写正文、制定统一规则或执行其中的历史任务。

## 来源与检索范围

| 仓库 | 只读来源根目录 | 当前工作区文件数（排除 .git） | 纳入文件数 |
| --- | --- | ---: | ---: |
| research-process | `/home/fainic/data/research-process` | 53 | 24 |
| multiarm-problem-gen | `/home/fainic/data/multiarm-problem-gen` | 215 | 31 |

共筛查 268 个当前工作区文件，其中 79 个 Markdown 文件；纳入 55 个完整 Markdown 原文件，合计 328,267 字节。目录清单、内容检索包含隐藏、未跟踪和被忽略材料。`research-process/local-paths.md` 属于被忽略文件，仍按相关内容纳入。

判断依据是内容是否直接说明人与 agent 的协作方式，或提供有价值的讨论、纠正、决定、实施和复盘证据。保留少量必要的验收与原型说明作为经验背景；未将所有业务技术文档、代码、接口规范和模型资源一并纳入。Markdown 逐文件筛查标题、状态与相关上下文，核心约定和实施记录阅读全文；部分材料只读取重点章节。非 Markdown 文本作关键词和上下文筛查；论文、网格、图像、缓存仅按类型与既有文档说明筛选及取哈希，未全部解析其内容。

检索与执行偏差见 [检索记录](audit/SCAN.md)。未使用其他组、外部网站、聊天历史、个人记忆或旁支 worktree；来源脚本和历史任务均未执行。

## 状态标签的含义

- **已载明约定**：源文件直接作为工作约定陈述；并不额外证明每条都能追溯到用户确认。原文明示确认时，逐条索引注明。
- **候选建议/计划**：原文称建议、候选、待讨论或尚未整体确认；不能作为已确认规则或执行授权。
- **历史经验/结果**：原文记载当时讨论、决定、纠正、实施或验证。本轮只保存其报告，没有重跑历史测试或独立验证其中所有事实。
- **授权探索中的 agent 决定**：探索实施已经获得当时授权，仍明确不表示用户接受最终设计；不能与已确认长期约定混同。
- **混合/确认不明**：同一文件同时包含多种状态，或原文没有充分说明作者及确认情况；依关键章节读取，不能整篇升格为规则。

## research-process：协作约定与记录组织

| 原始副本（原相对路径） | 相关主题 | 原文状态与证据层级 | 纳入理由 | 关键章节（原文件行号） |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/research-process/AGENTS.md) | 长期协作、读取边界、写入授权、独立判断 | 已载明协作约定；逐条确认过程未在本文件展开 | 直接规定跨 session 协作、事实分层、记录审批、附件与 Git 边界。 | 开始工作（L9）<br>长期记录更新（L18）<br>内容组织（L30）<br>配套资源管理（L48）<br>维护与沟通（L63） |
| [README.md](sources/research-process/README.md) | 使用循环、信息组织、维护成本 | 已载明工作方式；私有远程同步仍是计划 | 将讨论、候选更新、审阅、写入和提交串成明确循环，说明按需拆分。 | 使用循环（L21）<br>维护（L33） |
| [overview.md](sources/research-process/overview.md) | 实践反馈、工程原则、个人经历 | 当前记录的原则与历史提醒；非普遍定律 | 解释先跑通再复盘的起因，并保留用户个人表述的适用背景。 | 工程原则（L17）<br>个人经历与提醒（L24） |
| [state.md](sources/research-process/state.md) | 状态恢复、验证范围、待讨论事项 | 历史状态快照；原文称第一版工作流已确认 | 保留当前阶段与未决问题的分层；其中生成器未实现等状态已过时，不能覆盖另一仓库记录。 | 当前阶段（L9）<br>下一步（L20）<br>待明确（L26）<br>暂不展开（L33） |
| [local-paths.md](sources/research-process/local-paths.md) | 设备路径与云端访问 | 已载明本机路径管理方式；确认来源未说明 | 被 Git 忽略但直接说明设备分别维护、云端不能默认访问；路径项尚未填写。 | 本机路径（L1） |
| [assets/README.md](sources/research-process/assets/README.md) | 附件归档、维护入口、链接与同步 | 已载明资源管理方式；部分为当次范围说明 | 说明稳定名称、保留生成源文件、检查引用及路径不等于同步。 | 存放与引用（L10）<br>版本与导出（L24）<br>外部资源（L30） |
| [assets/cube-complex/README.md](sources/research-process/assets/cube-complex/README.md) | 产物来源、源文件维护、再生成检查 | 历史归档及维护说明；本轮未重新生成或验证 | 提供用户与 agent 构图、脚本和展示副本的关系，以及再生成后检查与教学假设的具体例子。 | 用途与来源（L5）<br>文件与维护入口（L13）<br>生成方法（L25）<br>记号与限制（L38） |
| [experiments/README.md](sources/research-process/experiments/README.md) | 实验记录与观察解释 | 候选记录建议，同时载明按需创建原则 | 明确问题、版本、设置、实际结果与原因猜测的区别，不提前填满模板。 | 实验记录（L1） |
| [inbox/README.md](sources/research-process/inbox/README.md) | 零散想法、成熟程度、原始出处 | 已载明记录约定；文件名方式为可选建议 | 说明不把每条想法变为任务、用户确认后写入与保留原始出处。 | 随手记录（L1） |
| [projects/README.md](sources/research-process/projects/README.md) | 跨项目上下文与文档归属 | 已载明组织约定；项目关联仍为计划 | 区分代码仓库与研究主线记录，按需要增加子文件并分别记录仓库入口和本机路径。 | 项目关联（L8）<br>组织约定（L13） |
| [projects/dataset-generator/README.md](sources/research-process/projects/dataset-generator/README.md) | 需求成熟度、验收前问题 | 历史项目快照及待讨论事项 | 明确待讨论内容不等于实现需求，记录首轮测试问题和验收方式尚未确定。 | 当前情况（L8）<br>待讨论（L12） |
| [projects/stop-n-go/README.md](sources/research-process/projects/stop-n-go/README.md) | 用户报告与验证事实 | 用户报告及待验证范围；不是已验证结论 | 保留复现报告的证据边界，并规定后续测试引用版本、数据和配置。 | 当前情况（L7）<br>材料入口（L12） |
| [references/README.md](sources/research-process/references/README.md) | 阅读状态、来源与个人理解 | 已载明维护偏好；阅读完成度为历史快照 | 明确入口不等于已完成阅读，区分论文主张、个人理解和延伸想法。 | 文献入口（L1）<br>维护（L39） |

## research-process：讨论、理解变化与协作研究

| 原始副本（原相对路径） | 相关主题 | 原文状态与证据层级 | 纳入理由 | 关键章节（原文件行号） |
| --- | --- | --- | --- | --- |
| [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md) | 方案比较、组织决策、复查条件 | 原文明示用户已确认且初始化采用 | 保留单文件与目录的权衡、内容边界、决定理由和重新拆分条件。 | 问题与顾虑（L6）<br>方案比较（L12）<br>当前决定（L19）<br>决策理由与复查条件（L32）<br>落实（L38） |
| [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md) | 协作目标、工程思路演变 | 原文明示根据用户已确认讨论整理；历史经验 | 记录先实践再完善框架的思路变化、协作与记录双重目标以及候选更新的确认流程。 | 工程思路的演变（L16）<br>工作流目标（L28） |
| [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md) | 用户草稿、agent 补充、理解修正 | 历史理解与补充；并非完整确认的研究结论 | 用户原文与标注 agent 的补充分开，保留对用户初始判断的修正和讨论来源。 | 我的研究方向（L9）<br>碰撞矩阵（L19）<br>联合空间中的进度表示（L36）<br>终于有点眉目（L66） |
| [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md) | 独立审阅、原始理解、未知需求 | 历史讨论经验与未决问题；未形成需求或方案 | 明确不倒写最初认识，区分 agent 构造例子、风险提醒和已有实现缺陷。 | 理解变化：端点描述与执行时序（L13）<br>例子二：未经澄清的理解可能缩窄 planner 的能力范围（L49）<br>未决问题（L71） |
| [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md) | 术语澄清、反对理由、证据边界 | 阶段性理解与历史修正；改进想法未确认 | 保留 agent 对“暴力搜索、不理解时序”的修正，说明表示能力不能替代实际行为证据。 | 讨论背景（L5）<br>二、对“暴力搜索、不理解时序”的修正（L40）<br>六、保留但尚未展开的改进想法（L96）<br>文献依据与阅读范围（L108） |
| [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md) | 独立判断、可反驳假设、实验边界 | 历史独立审阅；具体实验方案未定、无本次结果 | 将用户直觉与 agent 审查分开，指出实验可以支持、限制或否定预期，不能提前确认方案。 | 用户的直觉与意图（L7）<br>agent 的独立审查（L15）<br>“用实验验证想法”的含义与边界（L25）<br>尚未决定（L35） |
| [inbox/2026-09-14-todos-and-draft.md](sources/research-process/inbox/2026-09-14-todos-and-draft.md) | 草稿、整理与正式写入 | 候选计划；作者及是否经确认未标明 | 短原始材料说明先列 todo、写草稿、完善后再正式写入；不能当成执行授权。 | Todos（L3） |
| [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) | 保留用户原文、追加澄清、插图证据 | 原文明示完善表述经用户审阅确认；原始理解仍保留 | 展示原始表述与完善表述并存、追加说明不倒写历史、教学插图不等于实验结果。 | 用户原始表述（L11）<br>用户补充表述：搜索（L15）<br>与 agent 讨论后的完善表述（L19）<br>补充讨论：路径拆分与基本方片（L90）<br>配套插图（L131） |
| [inbox/2026-09-16-generator-scene-and-target-representation.md](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md) | 拒绝擅自补齐、候选与确认分层 | 混合：已确认表示方向、未决方案和历史纠正 | 用户要求标明尚未确定，agent 曾越过此意图补齐组织方案；原文明确这些示例不成为已确认设计。 | 当前情况（L5）<br>已确认：生成后保留的目标信息（L42）<br>尚未确定：最终数据与名义场景的组织（L50）<br>格式版本的含义（L72） |
| [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) | 协作目标、复杂度、Git、记录与迁移经验 | 用户目标及既有确认原则与 agent 判断混合；候选流程未整体确认 | 本轮最直接的协作调研材料，分别保留目标、研究证据限制、候选流程及怎样积累经验。 | 1. 用户希望通过这个项目获得什么（L7）<br>2. 调研范围与证据边界（L21）<br>6. 理解和管理 complexity 的候选方法（L100）<br>8. Git 的候选使用方式（L122）<br>9. 项目组织与信息记录的候选起点（L140）<br>10. 怎样积累可迁移的经验（L163）<br>11. 当前综合判断与未决事项（L187） |
| [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md) | 渐进设计、工程偏好、探索自由 | 原文明示两条原则及 agent 补充经讨论认可；不是强制流程 | 保留用户原始表述与认可补充，明确共同语义、工程偏好和探索表达的区别。 | 背景（L7）<br>1. 在草稿纸上积累线索，逐渐形成整体设计（L13）<br>2. best practice 提供倾向，保留表达与探索空间（L31） |

## multiarm-problem-gen：约定、文档入口与工作方式

| 原始副本（原相对路径） | 相关主题 | 原文状态与证据层级 | 纳入理由 | 关键章节（原文件行号） |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md) | 人参与架构、局部自主、契约隔离、验证与交接 | 已载明协作约定；逐条确认历史未全部展开 | 直接规定范围、授权、独立上下文、工具回退、契约缺口、越界处理、测试目的和诚实计量。 | 人与 agent（L9）<br>记录（L21）<br>实现与验证（L29）<br>Git 与交接（L47）<br>架构决策与自主权限（L67）<br>从设计进入实现（L77）<br>实现任务的阅读边界（L92）<br>Serena 使用约定（L106）<br>契约缺口与异常处理（L120）<br>验证与记录（L135） |
| [README.md](sources/multiarm-problem-gen/README.md) | 文档入口、当前能力、协作学习与归属 | 已载明协作目标；自主结果未最终接受 | 说明人与 agent 分工、学习目标、跨仓库文档归属，以及授权探索不代表最终设计接受。 | 从哪里开始（L7）<br>仓库组织（L14）<br>设计与学习（L29） |
| [docs/README.md](sources/multiarm-problem-gen/docs/README.md) | 过程分类、状态保留、跨任务交接 | 已载明记录方式；阶段状态和自主结果为历史材料 | 区分讨论方案和实际结果，链接过滤交接与中止记录，强调不把方案改写成结果或指令。 | 当前阶段（L3）<br>讨论与方案（L18）<br>实施过程与复盘（L39）<br>接下来讨论（L53）<br>怎样组织记录（L61） |
| [docs/design.md](sources/multiarm-problem-gen/docs/design.md) | 历史候选与实际契约、设计状态追加 | 混合：已确认语义、历史草稿、自主探索补充与未决事项 | 通过追加实施和自主试验状态保留历史，明确历史候选不能用于推断当前职责。 | 当前设计草稿（L1）<br>单元 3：场景与统一资源管理（L34）<br>候选抽象与待验证的问题（L89）<br>未决事项（L101） |
| [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md) | 探索与主线、逻辑提交、授权、语义集成 | 已载明 Git 工作约定；集成方式按情境选择 | 明确建议提交与授权的区别、探索成果整理、英文提交、组合行为与保护无关修改。 | 探索分支与长期主线（L3）<br>何时提交与集成（L26）<br>集成方式（L41）<br>Commit message 的语言（L53）<br>主线提交（L79）<br>操作边界（L117） |
| [docker/README.md](sources/multiarm-problem-gen/docker/README.md) | 可复现环境、可编辑产物、完整验收入口 | 已载明环境与验收入口；版本和执行事实本轮未重验 | 作为协作实施的配套材料，说明宿主权限、固定来源、挂载不取消阅读边界、非空测试与失败停止。 | 环境组织（L40）<br>固定版本与来源（L48）<br>自主试验：完整输入包入口与验收（L128） |

## multiarm-problem-gen：讨论、决定与公开交接

| 原始副本（原相对路径） | 相关主题 | 原文状态与证据层级 | 纳入理由 | 关键章节（原文件行号） |
| --- | --- | --- | --- | --- |
| [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md) | 初始化组织、协作学习、跨仓库追溯 | 历史组织选择及用户目标；下一步为候选方向 | 保留空仓库起点、记录与实现分属不同仓库、避免单次经验直接变通用规则。 | 背景（L5）<br>本次组织选择（L11）<br>学习与协作目标（L17）<br>前序材料（L23）<br>下一步（L31） |
| [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md) | 最小完整示例、用户反馈、范围与证据 | 混合：已确认方向、候选改造、追加讨论与观察 | 说明完整不意味着加入所有能力，用实际样例反馈澄清问题，候选参数与离散检查不能冒充验收。 | 目标（L7）<br>已确认的选择（L13）<br>“最小但完整”的含义（L24）<br>追加：基准场景与可视化暴露的三个问题（L58）<br>追加：问题 1、2 的方案（L122）<br>追加：问题 3 的方案（L166） |
| [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md) | 用户纠正抽象、按需加载、局部方案 | 历史讨论与局部方案；未完整定稿 | 用户对提前解析 mesh 和额外抽象提出质疑并改变方案，保留实际测量的适用范围与渐进设计过程。 | 从读取结果谈起（L9）<br>Mesh：从提前解析转向按需加载（L37）<br>Pose、Frame 与场景复用（L47）<br>后续计划（L99） |
| [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md) | 解释运行路径、共同语言、避免对象清单 | 历史设计讨论；精确接口与边界仍待确认 | 回应用户要求说明每一步与对象协作，使用易懂术语，不提前列所有私有方法。 | 从对象清单转向运行流程（L7）<br>运行流程与职责（L15）<br>一个协作例子（L29）<br>边界与后续（L50） |
| [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md) | 任务粒度、代码职责、隔离实验 | 候选任务划分的澄清；未决定合并或拆分任务 | 说明分文件或类不能自动构成上下文隔离，任务粒度应对应希望检验的契约边界。 | 问题与澄清（L7）<br>对契约隔离实验的影响（L25） |
| [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) | 独立交付、依赖顺序、契约先行 | 六单元候选划分；单元 1 已选定，其他粒度未定稿 | 把实现单元与文件或 class 分开，规定工作前明确契约、范围与验收，同时保留后续调整空间。 | 划分方案（L7）<br>路径与共享资源的归属（L22）<br>建议实现顺序（L43） |
| [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md) | 方案修正、准备与实现授权、内部自主 | 混合：已确认行为与候选接口；不是实现授权 | 用户纠正全不可变建议，后续讨论明确行为；强调已讨论方案仍需精确契约、范围和执行授权。 | 构造、引用与可变性（L31）<br>校验职责（L51）<br>首次交付与验收（L68）<br>实现前还需补齐（L80） |
| [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md) | 分阶段验收、授权与就绪判断 | 实施前方案；原文明示尚未执行、不是实现授权 | 区分环境与业务实现、空测试不算通过、公开契约先行、就绪不等于获准执行。 | 第一部分：统一 Docker／Compose 环境（L7）<br>第二部分：单元 1 基础表示（L43）<br>执行顺序、权限与就绪判断（L85） |
| [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md) | 用户改变表示、修改范围、契约隔离 | 已讨论的接口方案与已确认语义；写入不等于实施 | 保留用户修正分文件即分表示的建议，明确仅凭依赖公开契约实现、实际输入验收和不因完整而扩张。 | 目标与本次修正（L7）<br>错误与验收（L118）<br>实施范围与准备（L126） |
| [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md) | 用户取舍、未来功能、测试目的、实施边界 | 实施前方案；含已确认选择与候选签名，写入不是授权 | 逐项说明允许修改与阅读范围，区分提前完成输入迁移、未来讨论、就绪判断和代码验收。 | Frame 关系（L33）<br>本轮选择与保留方向（L90）<br>验收与允许修改范围（L119）<br>实施准备判断（L137） |
| [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md) | 独立决策、信息包、修改与验收、复议 | 授权探索中的 agent 决定；明确不是用户最终接受 | 保留备选与排除理由、依赖补丁分工、兼容迁移、计量限制，以及交接混入内部断言的原始来源。 | 信息包与边界（L5）<br>阅读、用量与时间（L33）<br>D6-1：先补公开资源快照（L39）<br>补充精度与阶段记录（L134）<br>D6-4：既有真实样例测试的单字符串维护（L148） |
| [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md) | 过滤交接、公开契约、范围与验收 | 探索性决定的公开摘录；不代表用户接受 | 作为重启隔离实现的具体交接产物，保留完整公开 D5 决定，不携带依赖内部测试。 | 单元 5 公开交接包（L1）<br>D5-1：保留 YAML，公开统一作用关联（L5）<br>D5-2：精确 YAML、顺序、参数与状态边界（L26）<br>D5-3：mean 的 configuration 名称消歧（L47） |
| [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md) | 过滤交接、职责分工、最小迁移 | 探索性决定的公开摘录；不代表用户接受 | 展示交接按任务过滤、共享维护由主 agent 承担、实现者不读取依赖内部测试。 | 单元 6 公开交接包（L1）<br>D6-1：先补公开资源快照（L5）<br>D6-2：输入包公开入口与严格发现（L16）<br>D6-3：真实样例最小迁移与验收（L45） |

## multiarm-problem-gen：实施、验收与复盘

| 原始副本（原相对路径） | 相关主题 | 原文状态与证据层级 | 纳入理由 | 关键章节（原文件行号） |
| --- | --- | --- | --- | --- |
| [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md) | 环境失败诊断、独立验收、真实阅读、交接 | 历史实施与验收记录；用户确认按两次提交保存 | 保留网络失败不等于版本不存在、安装与语法检查区别、契约充足性、工具回退和自述非独立证明。 | 基线与范围（L5）<br>环境验收（先于基础表示实现）（L13）<br>基础表示验收（L28）<br>契约是否足够（L45）<br>阅读范围与工具限制（L53）<br>交接（L68） |
| [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md) | 保护已有修改、独立测试预期、后续修正 | 历史实施结果；含后续移除 Material 的修正链接 | 记录手工计数错误修正测试预期、只运行而不读依赖测试、保留旧记录并追加修正。 | 起点与完成内容（L7）<br>实际验证（L17）<br>契约与阅读边界（L39）<br>剩余边界与局部不足（L49） |
| [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md) | 独立审查、范围收缩、接口授权、旧结果保留 | 原文明示用户确认接口收缩并完成修改；历史经验 | 实际例子说明缺少真实需求时删减抽象，同步契约与测试，同时不重写原实施结果。 | 原因与变更（L5）<br>验证与边界（L13） |
| [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md) | 目的先行、测试预期修正、范围保护、计量 | 历史实施与验收记录；阅读隔离是 agent 自述 | 记录缓存契约误解导致测试预期修正、局部 YAML 修复、保护已有改动和混合活动计时限制。 | 完成范围（L5）<br>测试目的与依据（L16）<br>实际结果（L30）<br>阅读范围与工具边界（L51）<br>用时与 token（L69）<br>契约判断及剩余限制（L82） |
| [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) | 协调与实现分工、重启、集成、计量限制 | 授权探索的历史实施结果；最终设计尚未接受 | 汇总独立上下文分工、意外交接越界后的重启、独立集成验收及并行墙钟不能当累计工时。 | 起点与边界（L5）<br>任务与决定入口（L21）<br>主 agent 集成测试目的（编写前）（L34）<br>最终验收事实（L40）<br>结果、决定与限制（L63）<br>用量与计时（L71）<br>本地交付状态（L91） |
| [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md) | 专属补丁、公开接口、交接事实、工具回退 | 探索性补丁历史结果；未最终接受设计 | 记录用公开快照修复依赖缺口、自建独立输入、交接基线非独立证据及不伪造完整计时。 | 范围与测试目的（编写测试前）（L5）<br>执行结果（L13）<br>实际阅读与工具边界（L21）<br>时间与用量（L29） |
| [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md) | 独立实现、自建预期、有限检查、用量 | 探索性实现历史结果；未最终接受设计 | 记录公开决定足够实现、测试不复制实现、有限 I/O 检查的证明边界、不可用 token 不反推。 | 测试目的与独立依据（L14）<br>实际验证（L24）<br>阅读范围与工具（L37）<br>时间、用量与未决项（L51） |
| [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md) | 意外越界、停止、过滤交接、诚实未完成 | 历史失败/中止记录；无实现与测试验收 | 保留未主动打开依赖测试但已见断言的实际偏差，不能声称能忘掉上下文，未运行不能报通过。 | 实际产物与停止原因（L5）<br>实际阅读（L11）<br>时间、用量与边界（L17） |
| [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md) | 新上下文、过滤包、错误修复、检查覆盖 | 探索性独立实现结果；未最终接受设计 | 与停止记录对照，保留新上下文不继承内部摘要、真实独立测试、跟踪差异检查不覆盖新文件的限制。 | 完成范围（L5）<br>测试目的、依据与结果（L11）<br>读取边界与用量（L31）<br>契约与局限（L46） |
| [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md) | 公开声明查询、最小迁移、共享维护、计量 | 探索性独立实施结果；主 agent 报告与自身验证分开 | 说明依赖只读公开信息、实现与集成维护分工、测试补充目的、工具回退和混合时间不能精确拆分。 | 完成范围（L5）<br>测试目的与依据（L15）<br>实际结果（L23）<br>契约、阅读与工具（L40）<br>用时与用量（L56） |
| [tools/baseline_validation/ur7e_table/README.md](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) | 历史检查版本、未重验、报告不覆盖、证据边界 | 历史数值检查与后续修正说明；不是完整规划验收 | 保留输入哈希过期、缺依赖未重新碰撞验证、检查见证与任务约束区别及新报告不覆盖旧报告。 | 数值检查及其范围（L95）<br>尚待讨论（L121）<br>目录整理说明（2026-09-21）（L125） |
| [tools/scene_preview/README.md](sources/multiarm-problem-gen/tools/scene_preview/README.md) | 原型与正式能力、实际 UI 验证、历史报告 | 原型使用和历史验证说明；有限范围 | 保留实际渲染检查与未覆盖任意 schema、旧报告不自动加载、预览不等于 generation 已实现。 | 文件（L29）<br>已验证与限制（L42）<br>可选开发材料（L48） |

## 关联阅读与不确定事项

- 写入与审批的原始规则：两个 `AGENTS.md`、研究仓库使用循环、已确认组织决策；当时的授权规则按各自原文保留，本轮不裁定统一方式。
- 渐进设计与人参与架构：已确认的设计原则 → 协作调研中的候选流程 → 生成器初始化记录及架构/实现约定。调研中的外部论文、博客和论坛链接未联网复核。
- 交接越界的完整链：自主决定记录 D6-4 → 单元 5 首个上下文中止记录 → 单元 5/6 公开交接包 → 后续单元 5 结果与自主试验总记录。不能只读后续成功结果而忽略已发生的偏差。
- 原方案与后续修正：单元 2 方案/实施 → 移除 Material；单元 3 方案 → 同日实施；历史草稿中的“尚未实现”与后续能力记录并存，不在副本中覆盖旧文。研究仓库 `state.md` 和项目入口明显保留较早状态。
- 实施记录中的测试数量、计时、token 不可用、阅读范围等都是源材料的报告。agent 自述并非独立审计证明，本轮亦没有重跑其代码。
- 原文件保留外链和全部原始相对引用；由于只复制相关材料，一些原文内部链接或插图引用不会在本资料集内存在。索引自身指向副本和审计文件的路径须有效，原文引用不会为修复路径而改写。
- 部分目录 README 和本机路径文件没有逐条确认记录；todo 草稿没有作者或确认标识，已在状态栏明确标注。学术/模型二进制附件未逐页或逐个内容解析，若后续聚焦其协作批注，需要另行筛查。

## 校验与排除记录

- [逐文件收集目录](audit/collection-catalog.json)：主题、状态、理由、关键章节、来源及副本路径。
- [副本清单与 SHA-256](audit/copy-manifest.json)；[可直接核对的摘要表](audit/copy-sha256.tsv)。
- [全部未纳入文件及理由](audit/exclusions.tsv)；[初始当前工作区清单](audit/initial-inventory.json)。
- [最终校验记录](audit/verification.json)：逐字节与 SHA-256 一致性、索引路径、章节标题、来源工作区内容/权限/修改时间、只读 Git 状态前后对比。
- [检索过程与限制](audit/SCAN.md)。

本索引只描述材料和证据状态，不将它们合成为新的协作规范。
