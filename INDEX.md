# 人与 agent 长期协作：原始材料索引

本轮只汇集原始材料并建立索引，不制定统一规则，也不执行材料中的历史任务。每个文件完整、按字节复制，未经摘录、改写、路径替换或格式转换。以下说明是检索元数据，不替代来源正文。

## 检索范围与判断口径

来源仅为 `/home/fainic/data/research-process` 和 `/home/fainic/data/multiarm-problem-gen` 的当前工作区。目录盘点包含隐藏、未跟踪及被忽略文件，排除所有 `.git` 入口/目录；未读取 Git 对象、历史、其他 worktree、聊天、个人记忆或外部网站。Git 仅用禁用可选锁的只读状态查询。文内链接、历史提交号、测试数量和外部研究均作为原文保留，没有追查或重新验证。

先盘点全部文件，再对 Markdown/文本做主题检索，检查标题、状态和相关段落，精读直接协作材料。二进制模型、第三方库、构建缓存等主要作文件级盘点和摘要，不作为协作证据。依据是是否含具体约定、人的意图/学习目标、建议修正、授权取舍、交接/隔离过程、验证与复盘经验；仅有领域中的“协作”、一个候选状态词或业务需求不足以单独纳入。混合文档因相关章节纳入后仍完整复制。

“已确认”只指原文明确记录的确认；“成文约定”指仓库当时的规范性文字，未逐条重建用户确认链；“候选建议”不提升为约定；“历史经验”保留当时情境，实施自述不提升为独立审计。无法判断的确认范围或当前有效性在条目中明示。授权试验中的 agent 决定与用户最终接受设计尤其分开。

盘点 **268** 个文件（research-process 53，multiarm-problem-gen 215），选入 **50** 个完整文件（21 + 29）。详细文件盘点与未纳入说明见 [检索与校验数据](audit/collection.json)，副本摘要见 [SHA-256 清单](MANIFEST.sha256)，实际校验见 [校验记录](COLLECTION_CHECKS.md)。

## research-process

原始来源均为 `/home/fainic/data/research-process/<原相对路径>`，副本在 `sources/research-process/<原相对路径>`。章节行号以完整副本为准。

### R01 · [AGENTS.md](sources/research-process/AGENTS.md)

- **原文状态：** 成文约定；逐条确认链未另行核实。
- **主题及纳入理由：** 跨 session、授权、证据、沟通、记录维护。长期协作约定的主要载体，涵盖候选更新、确认范围、原意与不确定性、独立判断及资源管理。
- **关键章节：** 开始工作（L9–16）；长期记录更新（L18–28）；内容组织与配套资源管理（L30–61）；维护与沟通（L63–76）。

### R02 · [README.md](sources/research-process/README.md)

- **原文状态：** 成文工作方式；关联已确认初始化记录。
- **主题及纳入理由：** 长期记录、使用循环、组织成本。说明记录本身的目标、审阅写入循环、保留过程及按实际需要拆分文档。
- **关键章节：** 目标（L1–7）；使用循环（L21–31）；维护（L33–49）。

### R03 · [overview.md](sources/research-process/overview.md)

- **原文状态：** 已采用工程原则；用户个人经验；研究事实含待核实项。
- **主题及纳入理由：** 实践反馈、避免脱离情境概括。保留先跑通再复盘的背景，明确个人提醒不应被扩大为普遍定律。
- **关键章节：** 工程原则与个人经历（L17–30）。

### R04 · [state.md](sources/research-process/state.md)

- **原文状态：** 历史状态：原文称第一版工作流已确认；部分进展已过时。
- **主题及纳入理由：** 跨 session 状态、未决问题。保存流程确认和暂缓多 agent 的历史阶段；“生成器尚未开始”不能覆盖后续实施记录。
- **关键章节：** 当前阶段、重点与下一步（L9–24）；待明确与暂不展开（L26–36）。

### R05 · [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md)

- **原文状态：** 根据已确认讨论整理的历史记录。
- **主题及纳入理由：** 实践反馈、写入授权、长期过程。保存工作方式的形成理由、用户原话语境和不依赖单次会话的目标。
- **关键章节：** 状态与来源（L3–5）；工程思路的演变与工作流目标（L16–40）。

### R06 · [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md)

- **原文状态：** 已确认并采用的组织决定。
- **主题及纳入理由：** 记录结构、替代方案、复查条件。同时保留顾虑、比较、选择理由和何时重新拆分的条件。
- **关键章节：** 确认状态（L3–4）；问题、比较、决定、边界、复查条件及落实（L6–43）。

### R07 · [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md)

- **原文状态：** 已确认原则；示例与同期其他建议未确认。
- **主题及纳入理由：** 渐进设计、best practice、探索自由。原文明示用户认可的两条原则，同时排除未确认的仓库、Git、目录建议。
- **关键章节：** 状态与背景（L5–11）；草稿纸积累线索（L13–29）；best practice 提供倾向（L31–51）。

### R08 · [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md)

- **原文状态：** 混合：用户目标、已确认原则、agent 候选建议和外部经验转述。
- **主题及纳入理由：** 学习目标、共同理解、Git、过程成本、可迁移经验。直接讨论长期协作；候选流程尚未整体确认，外部研究与论坛经验也不等于本项目结果。
- **关键章节：** 状态、目标及证据边界（L5–30）；实践适用边界（L50–71）；理解复杂度与协作摩擦（L100–120）；Git 与记录的候选方式（L122–161）；经验积累及未决事项（L163–199）。

### R09 · [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md)

- **原文状态：** 历史讨论经验；暂时理解与未决建议。
- **主题及纳入理由：** 保留认识变化、独立纠偏、范围控制。原文指出不能把讨论后认识倒写成最初认识，区分自制例子、未验证推断和未来需求。
- **关键章节：** 理解变化与新问题（L13–31）；理解风险、暂时理解与未决问题（L49–81）。

### R10 · [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md)

- **原文状态：** 历史讨论经验；agent 修正建议。
- **主题及纳入理由：** 准确表达、独立审阅。记录用户初始表述及 agent 不直接附和、拆分问题并修正表述的具体过程。
- **关键章节：** 讨论背景（L5–17）；对“暴力搜索、不理解时序”的修正（L40–54）；保留但尚未展开的改进想法（L96–107）。

### R11 · [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md)

- **原文状态：** 历史讨论经验；实验方案未定，无本次结果。
- **主题及纳入理由：** 研究直觉审阅、反证、证据边界。支持合理直觉同时明确其不足，不把常识写成新发现，也不预设实验必然支持用户想法。
- **关键章节：** 状态与用户意图（L5–13）；独立审查、实验含义与尚未决定（L15–37）。

### R12 · [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md)

- **原文状态：** 混合：用户原始理解、经审阅确认的完善表述、历史制作记录。
- **主题及纳入理由：** 保留原话、追加修正、共同理解。原始表述与后来确认的表述并存，体现理解演变的记录方式；技术图解仅作为过程背景。
- **关键章节：** 状态、用户原始及补充表述、完善表述入口（L5–19）；补充讨论背景与确认（L90–99）；配套插图后续制作状态（L131–155）。

### R13 · [inbox/2026-09-16-generator-scene-and-target-representation.md](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md)

- **原文状态：** 历史纠偏；已确认设计与未决方案并存。
- **主题及纳入理由：** 不扩大意图、候选不等于决定。明确记录用户要求补充“尚未确定”，而 agent 曾误补成完整方案，是意图解释的具体摩擦。
- **关键章节：** 尚未确定：最终数据与名义场景的组织（L50–64）。

### R14 · [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md)

- **原文状态：** 历史共同整理；用户原文与 agent 补充并存；无整篇统一确认声明。
- **主题及纳入理由：** 学习支持、分清作者、保留纠错。第一人称原文和明确标记的 agent 补充相邻，保留初始判断、依据与修正，不覆盖用户思考。
- **关键章节：** 联合空间中的进度表示及 agent 补充（L36–64）；从输入形式到空间占用的讨论与修正（L66–89）。

### R15 · [assets/README.md](sources/research-process/assets/README.md)

- **原文状态：** 成文维护约定；部分当时操作状态。
- **主题及纳入理由：** 附件归档、可再生成产物、稳定引用。说明长期资料、生成源文件、导出和外部资源边界，涉及跨会话维护。
- **关键章节：** 存放与引用、版本与导出、外部资源（L10–34）。

### R16 · [experiments/README.md](sources/research-process/experiments/README.md)

- **原文状态：** 成文指引；字段以“建议”表述，非全套已确认强制模板。
- **主题及纳入理由：** 证据记录、记录成本。有实际实验才建立记录，区分观察与猜测，避免为了流程提前填模板。
- **关键章节：** 全文（L1–15）。

### R17 · [inbox/README.md](sources/research-process/inbox/README.md)

- **原文状态：** 成文记录约定；逐条确认链未另行核实。
- **主题及纳入理由：** 零散想法、审阅写入、保留出处。想法不必变成任务，无需强制清空，整理与确认的边界清楚。
- **关键章节：** 全文（L1–12）。

### R18 · [projects/README.md](sources/research-process/projects/README.md)

- **原文状态：** 成文组织约定；项目状态为当时记录。
- **主题及纳入理由：** 跨项目导航、避免重复维护。明确按需拆分、代码细节留原仓库以及设备路径分离。
- **关键章节：** 组织约定（L13–19）。

### R19 · [references/README.md](sources/research-process/references/README.md)

- **原文状态：** 成文维护约定；文献及项目状态未在本轮重核。
- **主题及纳入理由：** 来源归属、个人理解与延伸。文末区分论文主张、个人理解与延伸想法，是来源记录的约定入口。
- **关键章节：** 维护（L39–42）。

### R20 · [references/stac-reading-notes.md](sources/research-process/references/stac-reading-notes.md)

- **原文状态：** 历史阅读与共同整理；论文主张和构造例子；待核实矛盾。
- **主题及纳入理由：** 归属标记、证据限制、不静默消解冲突。保存补充内容的作者、阅读边界和正文/表格矛盾的处理实例；不把技术内容当协作规则。
- **关键章节：** 实验设置的来源、解释边界与待核对冲突（L20–57）；schedule 构造示例声明（L71–74）；碰撞历史示例来源限制（L139–141）。

### R21 · [local-paths.md](sources/research-process/local-paths.md)

- **原文状态：** 本机成文提示；被忽略文件；路径尚未填写。
- **主题及纳入理由：** 环境可达性、同步边界。实际本地被忽略材料，提醒本机路径不等于云端可达；条目仍是占位状态。
- **关键章节：** 全文（L1–8）。

## multiarm-problem-gen

原始来源均为 `/home/fainic/data/multiarm-problem-gen/<原相对路径>`，副本在 `sources/multiarm-problem-gen/<原相对路径>`。章节行号以完整副本为准。

### M01 · [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md)

- **原文状态：** 成文协作约定；逐条用户确认链未另行核实。
- **主题及纳入理由：** 架构权限、实现隔离、测试、阅读记录、计量。最完整的项目协作约定，区分架构与局部自主权限、上下文污染、契约缺口和真实报告。
- **关键章节：** 工作入口、人与 agent、记录、验证、Git（L3–57）；架构决策与实现阅读边界（L59–104）；工具使用、缺口与意外读取（L106–133）；验证、阅读记录与时间/token 统计（L135–157）。

### M02 · [README.md](sources/multiarm-problem-gen/README.md)

- **原文状态：** 成文目标；授权探索的状态说明。
- **主题及纳入理由：** 学习目标、跨仓库分工、设计接受。说明用户参与架构、理解复杂度的目标，自主试验不代表最终设计接受。
- **关键章节：** 实施边界、设计与学习（L23–33）。

### M03 · [docs/README.md](sources/multiarm-problem-gen/docs/README.md)

- **原文状态：** 成文组织约定；历史及当前阶段区分。
- **主题及纳入理由：** 讨论/实施分开、决定不等于执行、候选非指令。保存方案、结果、复盘的分工及历史不改写的维护方式。
- **关键章节：** 讨论方案状态（L18–22）；实施与复盘入口（L39–45）；后续非排定计划与记录组织（L53–69）。

### M04 · [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md)

- **原文状态：** 成文工作约定；具体集成方式仍按情境选择。
- **主题及纳入理由：** 分支、逻辑提交、审阅、授权。记录探索与主线、检查点、英文提交、语义集成验证和不同 Git 操作的授权。
- **关键章节：** 探索、提交与集成（L3–51）；提交信息语言与质量（L53–115）；操作边界（L117–123）。

### M05 · [docker/README.md](sources/multiarm-problem-gen/docker/README.md)

- **原文状态：** 成文开发与验证入口；历史环境说明。
- **主题及纳入理由：** 可复现环境、范围隔离、验证证据。环境变更如何留存、固定版本不宣称最新版、仓库挂载不豁免阅读边界，都是协作支持条件。
- **关键章节：** 环境组织与版本来源（L40–67）；自主试验输入包入口与验收（L128–158）。

### M06 · [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md)

- **原文状态：** 历史组织决定与学习目标。
- **主题及纳入理由：** 仓库分工、渐进设计、迁移经验。记录项目为何这样组织；初期未引入自主多 agent 不等于永久禁止后续实验。
- **关键章节：** 背景、组织选择与学习协作目标（L5–21）；追溯入口及当时下一步（L23–33）。

### M07 · [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md)

- **原文状态：** 混合：已确认选择、agent 候选与追加确认；旧状态保留。
- **主题及纳入理由：** 最小完整样例、实际反馈、控制范围。展示通过实例发现设计问题，区分用户选择、agent 建议、未验证数值和后续决定。
- **关键章节：** 目标、选择与最小但完整（L7–30）；待明确与可视化反馈（L48–64）；用户问题及独立判断（L66–120）；追加确认状态（L122–124）。

### M08 · [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md)

- **原文状态：** 历史讨论和局部方案；含已确定语义与未定接口。
- **主题及纳入理由：** 共同设计、修正倾向、控制抽象。用户质疑提前解析和额外抽象，结合局部测量调整方案；测量未推广到所有模型。
- **关键章节：** 状态与讨论起点（L5–13）；从提前解析转向按需加载（L37–45）；规则澄清与后续边界（L93–101）。

### M09 · [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md)

- **原文状态：** 历史讨论方案；精确接口未确认。
- **主题及纳入理由：** 可理解的说明、过程讲解、避免过度设计。用户要求说明步骤和对象如何合作，而非仅列清单；术语与叙述随理解需要调整。
- **关键章节：** 从对象清单转向运行流程（L7–13）；运行流程与职责（L15–27）；边界与后续（L50–56）。

### M10 · [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md)

- **原文状态：** 候选任务划分；单元 1 已选择，其余粒度非全部定稿。
- **主题及纳入理由：** 任务粒度、依赖顺序、公开契约。区分独立交付单元与代码文件，按依赖及契约缺口决定范围。
- **关键章节：** 状态、划分及资源归属（L5–26）；建议实现顺序与开工边界（L43–53）。

### M11 · [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md)

- **原文状态：** 讨论澄清/候选建议；未作拆分决定。
- **主题及纳入理由：** 任务边界、代码职责、隔离实验。分成 class/文件不等于阅读隔离；任务粒度要对应真正想检验的边界。
- **关键章节：** 状态、问题澄清与隔离实验影响（L5–31）。

### M12 · [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md)

- **原文状态：** 已讨论方案；当时不代表实现授权。
- **主题及纳入理由：** 环境先行、契约先行、准备与执行分开。环境和实现分别交付验收，空测试集或只读环境探测不能算实现通过。
- **关键章节：** 状态及环境组织（L5–23）；环境验收边界（L41–41）；执行顺序、权限与就绪判断（L85–93）。

### M13 · [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md)

- **原文状态：** 已确认语义与候选接口混合；不是实现授权。
- **主题及纳入理由：** 用户纠偏、契约与内部自主、验收准备。记录 agent 初始建议被用户反馈修正，以及实现前需补足的精确信息。
- **关键章节：** 构造、引用与可变性变化（L31–49）；确认细则、验收及准备（L62–86）。

### M14 · [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md)

- **原文状态：** 历史讨论方案；写入不等于执行实现。
- **主题及纳入理由：** 契约先行、修改范围、不扩大“完整”。把完整支持限定于实际需求，明确内部自主与返回讨论的边界。
- **关键章节：** 状态、目标与修正（L3–13）；验收、实施范围与准备（L118–132）。

### M15 · [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md)

- **原文状态：** 实施前方案；已确认职责与候选字段并存。
- **主题及纳入理由：** 修正建议、未来接口不提前决定、允许范围。区分当前授权、未来讨论、读写范围和就绪判断，记录用户对管理与命名建议的纠偏。
- **关键章节：** 状态（L3–7）；本轮选择与保留方向（L90–96）；验收范围与实施准备判断（L119–143）。

### M16 · [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md)

- **原文状态：** 授权内 agent 探索决定；明确不是用户最终接受。
- **主题及纳入理由：** 决策/实施分工、信息包、复议、依赖修改。保存决策者边界、替代方案、复议及导致后续上下文污染的信息来源。
- **关键章节：** 状态、信息包与边界（L3–11）；阅读统计与资源补丁分工（L33–47）；阶段边界、D5-3 复议及 D6-4 信息混入（L134–160）。

### M17 · [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md)

- **原文状态：** 探索性决定的过滤交接包；非用户最终确认。
- **主题及纳入理由：** 独立上下文、过滤交接、公开范围。与中止记录配对，展示如何从综合决定提取供隔离实现使用的公开材料。
- **关键章节：** 交接目的与状态（L1–5）；公开约束及消歧决定（L26–56）。

### M18 · [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md)

- **原文状态：** 探索性决定的过滤交接包；非用户最终确认。
- **主题及纳入理由：** 公开交接、共享修改、依赖归属。依赖补丁由专属 agent 完成，共享入口与已有验收元数据由主 agent 维护。
- **关键章节：** 交接边界及资源补丁分工（L1–14）；最小迁移与验收边界（L45–58）。

### M19 · [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md)

- **原文状态：** 历史执行与验收记录；非本轮重验。
- **主题及纳入理由：** 环境误判、独立预期、权限、分开提交。记录网络错误排查、环境与实现分别验收、工具限制和自述并非独立审计。
- **关键章节：** 环境与基础表示验收（L13–43）；契约、阅读限制及交接（L45–70）。

### M20 · [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md)

- **原文状态：** 历史结果；Material 支持后来被收缩。
- **主题及纳入理由：** 保护已有改动、独立纠错、阅读限制。真实数量预期错误通过独立计数修正，原结果保留并链接后续删减。
- **关键章节：** 起点与已有变更（L7–9）；验证纠错及工具边界（L33–47）；历史能力限制（L49–56）。

### M21 · [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md)

- **原文状态：** 用户确认后的历史改动；非通用能力禁令。
- **主题及纳入理由：** 独立审查、消除无依据功能、授权范围。审查指出过度实现，用户确认后收缩公共接口，保留旧记录并链接修正。
- **关键章节：** 原因、同步契约、验证与未来边界（L3–19）。

### M22 · [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md)

- **原文状态：** 历史实施与复盘；自述/测试结果有范围限定。
- **主题及纳入理由：** 先明测试目的、失败归因、保留已有修改、计时。保存测试预期误用缓存的纠错、局部错误修复、输入字节保护和混合阶段统计。
- **关键章节：** 既有改动保护及测试目的（L14–28）；失败、修正与一致性（L43–49）；阅读边界、统计与契约局限（L51–86）。

### M23 · [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md)

- **原文状态：** 授权探索的历史结果；最终设计未接受。
- **主题及纳入理由：** 多 agent 分工、隔离修复、集成、证据归属、计时。总记录保留独立决策/实施、中止/重启、集成验证及并行时间统计。
- **关键章节：** 授权、初始验证、任务、交接修复、测试目的（L3–38）；验收事实、限制及自审（L40–69）；用量计时与交付（L71–93）。

### M24 · [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md)

- **原文状态：** 探索性补丁历史结果；非用户最终接受。
- **主题及纳入理由：** 专属修改范围、公开行为测试、交接事实归属。最小扩展记录区分自身结果与协调侧报告，保留无法可靠细分的时间边界。
- **关键章节：** 范围、目的、结果及实际阅读（L5–27）；时间与用量（L29–33）。

### M25 · [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md)

- **原文状态：** 探索实施历史结果；自述非独立审计。
- **主题及纳入理由：** 独立测试预期、职责、计时局限。单元测试与主任务回归分开，报告独立依据及有限验证能说明的范围。
- **关键章节：** 范围、独立预期及验证（L7–35）；阅读、计量与未决项（L37–61）。

### M26 · [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md)

- **原文状态：** 历史中止/失败经验；未实施也未测试。
- **主题及纳入理由：** 上下文污染、及时停止、不声称遗忘。综合决定携带内部断言导致上下文污染，保留实际产物、停止理由和计时缺口。
- **关键章节：** 停止原因、实际阅读及未完成边界（L3–21）。

### M27 · [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md)

- **原文状态：** 过滤交接后的探索实施结果；非最终接受。
- **主题及纳入理由：** 新上下文重启、自审修复、证据范围。区别首次中止上下文，记录错误补测修正和 diff 检查不覆盖未跟踪文件的限制。
- **关键章节：** 重启范围、独立测试与自审修复（L3–29）；读取、计量与契约局限（L31–48）。

### M28 · [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md)

- **原文状态：** 探索实施历史结果；主 agent 回归是转述。
- **主题及纳入理由：** 公开接口独立集成、共享职责、补测、局限。记录公开接口交付、补测目的先行、最小迁移以及单元验证与主任务报告的区别。
- **关键章节：** 职责、测试及证据归属（L5–38）；契约、工具边界与计量（L40–64）。

### M29 · [tools/baseline_validation/ur7e_table/README.md](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md)

- **原文状态：** 历史验证及局限；原报告保留，部分结果过时。
- **主题及纳入理由：** 验证过期、哈希关联、历史不覆盖。输入变更且缺少碰撞依赖后，不把旧报告算作新验证；区分历史原型与正式语义。
- **关键章节：** 数值检查范围、未检查项及目录整理（L95–129）。

## 未纳入范围及不确定事项

- 未整体纳入业务 YAML/schema、全部公开 API 契约、实现源码、测试代码、模型/网格、第三方库、论文 PDF、派生预览和构建缓存；本轮不是项目技术归档。每个未选 Markdown 有单独理由，其他文件按内容类型记录在校验数据中。
- `research-process` 当前状态查询中大部分材料为未跟踪文件，`local-paths.md` 被忽略；未按 Git 跟踪状态筛掉相关材料。两个仓库 `.serena/` 和研究仓库 `.obsidian/` 都在盘点内；所见配置/缓存没有另行纳入的协作讨论，没有调用相应工具或加载外部记忆。
- `research-process/state.md` 的“生成器尚未开始实现”“多 Agent 留待后续探索”是早期阶段；另一仓库已有 2026-09-30 自主实施记录。未修正原文或静默统一状态。早期调研“不建议整体引入多 agent”的候选建议，与后来的授权试验按各自时间和状态阅读。
- Material 初始支持与后续移除记录同时保留；首次 U5 中止与新 U5 完成也分别保留，没有只选成功结果。试验授权不自动等于最终接受设计。
- 原文中的命令、任务 prompt、指令和路径是待研究的历史资料，不是本轮执行指令。原作者对“已确认”“已验证”“未越界”的表述只是原文证据；本轮没有重做代码测试或审计历史会话。
- 这是相关资料集，不是两仓库完整可运行快照。原文中指向未纳入技术文件、插图、外部网站或原设备目录的链接保持原样，可能无法在副本内打开；本轮核验的是 **INDEX.md 自身的本地链接**。不会为修复历史引用而改写原文或扩大到其他来源。
- 外部调研结论与引用没有联网核实；未记录的信息、无法由原文判断的确认链仍未知。单次实践的跨项目适用性留给后续提炼判断。

- 前期有一轮 Markdown 候选枚举使用 Path.rglob，再过滤 .git 路径；该写法可能遍历 .git 目录项，不能声称所有早期枚举都在目录入口处剪枝。未读取或输出 .git 中的文件内容，也未访问 Git 历史版本；正式全量盘点与收集脚本已显式剪枝排除 .git。此为实际检索方式的范围说明。
