# 人与 agent 长期协作：原始材料索引

本轮仅汇集原始材料并建立索引，不制定统一规则。`sources/` 中的文件按原相对路径完整、逐字节复制；其中的 AGENTS.md、历史 prompt、命令及候选流程均为待研究原文，不作为本次任务指令。

## 来源与检索范围

| 来源仓库当前工作区 | 候选文件 | 纳入文件 | 当前跟踪情况 |
| --- | ---: | ---: | --- |
| `/home/fainic/data/research-process` | 53 | 27 | 已跟踪 0；未跟踪 48；被忽略 5 |
| `/home/fainic/data/multiarm-problem-gen` | 215 | 42 | 已跟踪 200；未跟踪 0；被忽略 15 |

合计纳入 **69 个文件**，共 **406,672 字节**。文件清单覆盖隐藏、未跟踪和被忽略的当前材料；不读 Git 对象、历史或其他 worktree，不检索外部网站，不执行历史任务。详细方法见[检索与筛选记录](audit/review-coverage.md)。

## 状态与证据读法

- **已确认约定**：原文明确写为当前协作约定，或注明用户确认／讨论认可。这里登记的是原文状态，本轮未独立核验逐条授权的对话链。
- **候选建议**：原文仍使用建议、候选、待讨论或未定；用户允许保存一份文档，不等于接受文档中全部候选。
- **历史经验**：讨论变化、实际尝试、实施和复盘记录。原文中的测试数量、阅读范围和耗时保留其自述及统计局限，本轮没有重跑。
- **授权自主试验**：已授权执行且可能已实现的 agent 决定，仍不等于用户最终接受设计；表中单独标明，不升级为已确认长期约定。
- **辅助材料／无法判断**：具体公开契约、运行入口、教学与项目背景用来理解协作情境；无法据原文判断确认程度的注明限制。领域技术语义不会自动变为协作规则。

每个文件可同时含多类内容，表中的状态与关键章节按原文区分。章节行号是所复制当前文件的实际行号。

## 主题入口

| 相关主题 | 主要原始材料 |
| --- | --- |
| 长期记录、审阅与授权、跨 session 上下文 | [研究仓库协作约定](sources/research-process/AGENTS.md)、[第一版工作方式](sources/research-process/journal/2026-09-07-starting-point.md)、[组织决定](sources/research-process/journal/2026-09-07-record-organization.md) |
| 用户学习、渐进设计、best practice 与流程成本 | [已确认的两条原则](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md)、[协作目标与候选调研](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) |
| 独立判断、澄清原意、保留理解变化 | [研究直觉的独立审查](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md)、[不要代补未决方案的实例](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md)、[原始表述与完善版本](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) |
| 架构与实现、任务粒度、契约及自主权限 | [代码仓库协作约定](sources/multiarm-problem-gen/AGENTS.md)、[任务与职责的区别](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md)、[实现单元划分](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) |
| 独立决策、多 agent 交接及阅读污染 | [自主决定](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md)、[中止记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md)、[过滤后 U5 交接](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md)、[整轮结果](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) |
| 测试目的、独立预期、真实统计与限制 | [单元 3 记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md)、[单元 5 记录](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md)、[历史基准检查边界](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) |
| Git、交付范围、保留旧记录与必要修正 | [Git 工作约定](sources/multiarm-problem-gen/docs/git-workflow.md)、[接口收缩复盘](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md)、[文档组织说明](sources/multiarm-problem-gen/docs/README.md) |

## 文件索引

### research-process

原始来源：`/home/fainic/data/research-process`。表内文件路径均相对于该仓库根目录；链接指向本组副本。

#### 协作约定

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [AGENTS.md](sources/research-process/AGENTS.md) | 已确认约定：仓库现行声明；本轮未独立核验逐条确认链 | 长期协作；授权；上下文；独立判断；记录与资源管理。直接记录跨 session 工作入口、候选更新经审阅后写入、事实类别、沟通及 Git 边界，是明确协作约定原文。 | “目标”（L3–8）；“开始工作”（L9–17）；“长期记录更新”（L18–29）；“内容组织”（L30–47）；“配套资源管理”（L48–62）；“维护与沟通”（L63–76） |
| [README.md](sources/research-process/README.md) | 已确认约定／已采用工作流；跨设备同步为后续计划 | 协作循环；记录用途；渐进拆分。将 AGENTS 中的讨论、候选、审阅、写入循环落实为仓库入口，记录过程本身也是目标。 | “阅读入口”（L9–20）；“使用循环”（L21–32）；“维护”（L33–49） |
| [inbox/README.md](sources/research-process/inbox/README.md) | 记录方式的现行声明；逐条用户确认来源无法独立判断 | 零散想法；候选审阅；原始出处。明确想法不必变任务、不强制清空、用户确认后写入及成熟后仍保留原始出处。 | “随手记录”（L1–12） |
| [projects/README.md](sources/research-process/projects/README.md) | 项目组织的现行声明；项目关联仍为计划 | 跨项目记录；单一维护位置；渐进拆分。记录代码与详细实现留在原仓库、研究发现通过链接关联及设备路径单独维护的内容边界。 | “组织约定”（L13–19） |
| [experiments/README.md](sources/research-process/experiments/README.md) | 候选记录建议；逐条采用情况无法判断 | 测试目的；可复现信息；观察与原因猜测。保存实验记录的按需字段、实际观察与猜测的区分，不把建议模板认定为强制约定。 | “实验记录”（L1–15） |
| [references/README.md](sources/research-process/references/README.md) | 阅读与维护入口；不代表清单已全部详细阅读 | 来源；论文主张与个人理解。维护章节明确区分论文主张、个人理解和延伸想法；入口多处保留尚未完成的状态。 | “维护”（L39–42） |
| [assets/README.md](sources/research-process/assets/README.md) | 已采用资源组织方式；导出和同步计划按原文状态理解 | 附件维护；稳定路径；外部资源；再生成副本。记录维护源文件、主题分组、稳定引用与临时路径局限，体现长期协作中产物管理的现行方式。 | “存放与引用”（L10–23）；“版本与导出”（L24–29）；“外部资源”（L30–34） |

#### 讨论与决策

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md) | 原文注明用户已确认；同时保留个人历史经验与后续计划 | 长期记录；先实践后复盘；审阅授权。记录建立第一版工作流的目标与工程观念演变，包括不依赖单一 session 和不强求零散想法成体系。 | “工程思路的演变”（L16–27）；“工作流目标”（L28–40） |
| [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md) | 原文注明用户已确认且初始化已采用 | 文档组织；方案权衡；复查条件。保留单文件与目录的比较、采用理由、内容边界及何时重新拆分，而非只保存目录结果。 | “问题与顾虑”（L6–11）；“方案比较”（L12–18）；“当前决定”（L19–24）；“内容边界”（L25–31）；“决策理由与复查条件”（L32–37）；“落实”（L38–43） |
| [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md) | 已确认原则：原文注明用户认可补充；不是完整架构或强制流程 | 渐进设计；共同语义；工程偏好；探索自由。直接保留两段用户原话、经讨论认可的补充，以及哪些同期内容仍未确认。 | “背景”（L7–12）；“1. 在草稿纸上积累线索，逐渐形成整体设计”（L13–30）；“2. best practice 提供倾向，保留表达与探索空间”（L31–52） |
| [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) | 用户目标与此前原则已确认；调研判断和候选流程未整体确认为规范；外部主张本轮未核验 | 架构参与；学习；流程成本；Git；可迁移经验。最直接的协作调研材料，区分用户目标、研究证据、作者实践、论坛摩擦和 agent 候选建议。保留全部原文及原有证据边界。 | “1. 用户希望通过这个项目获得什么”（L7–20）；“2. 调研范围与证据边界”（L21–31）；“3. 第一轮研究带来的提醒”（L32–49）；“6. 理解和管理 complexity 的候选方法”（L100–114）；“7. 论坛讨论暴露的摩擦”（L115–121）；“8. Git 的候选使用方式”（L122–139）；“9. 项目组织与信息记录的候选起点”（L140–162）；“10. 怎样积累可迁移的经验”（L163–186）；“11. 当前综合判断与未决事项”（L187–200） |

#### 背景与历史经验

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [overview.md](sources/research-process/overview.md) | 用户经历与已采用工程原则；研究想法未全部确定 | 实践反馈；个人经验适用范围。保存先跑通流程再完善的原则，并明确个人提醒不能改写成普遍定律。 | “工程原则”（L17–23）；“个人经历与提醒”（L24–31） |
| [state.md](sources/research-process/state.md) | 历史阶段快照；部分工作流已确认；进度存在跨仓库时效差异 | 上下文恢复；计划与事实；状态冲突。保留研究仓库的旧进度与未决事项，用于辨认状态快照不能自动覆盖代码仓库后续事实。 | “当前阶段”（L9–13）；“当前重点”（L14–19）；“下一步”（L20–25）；“待明确”（L26–32）；“暂不展开”（L33–37） |
| [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md) | 用户原始理解与 agent 追加说明；不能把正文全部当已确认技术结论 | 共同理解；补充署名；修正误解；保留原意。多处明确分出 agent 补充，并保留用户原说法与后续纠正，是共同学习和记录理解变化的具体实例。 | “碰撞矩阵”（L19–35）；“联合空间中的进度表示”（L36–65）；“终于有点眉目”（L66–90） |
| [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md) | 讨论中的理解变化和候选问题；尚未形成需求或实现方案 | 澄清隐含假设；范围；例子来源；不倒写原认识。记录 agent 扩展用户原理解、用例说明额外假设、限制结论适用范围；不将这一讨论升格为新需求。 | “理解变化：端点描述与执行时序”（L13–20）；“新问题：到达之后发生什么”（L21–34）；“例子一：共享加工区域中的访问与撤离”（L35–48）；“例子二：未经澄清的理解可能缩窄 planner 的能力范围”（L49–62）；“未决问题”（L71–82） |
| [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md) | 阶段性理解；包含 agent 修正建议；无具体改进方案 | 独立审查；概念区分；证据与推断。保存对含混表述的修正和对尚未展开想法的限定，体现 agent 不顺着用户原判断直接下结论。 | “讨论背景”（L5–17）；“二、对“暴力搜索、不理解时序”的修正”（L40–54）；“五、这种结构支持时序协调，但不保证仅靠时序调整就能解决”（L84–95）；“六、保留但尚未展开的改进想法”（L96–107）；“文献依据与阅读范围”（L108–115） |
| [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md) | 用户意图与 agent 独立审查；具体实验方案未定、无实验结果 | 独立判断；可证伪问题；实验解释边界。直接记录独立审查如何限定用户研究直觉，并把展示例子、实验假设和已得结果分开。 | “用户的直觉与意图”（L7–14）；“agent 的独立审查”（L15–24）；““用实验验证想法”的含义与边界”（L25–34）；“尚未决定”（L35–38） |
| [inbox/2026-09-09-coordination-space-reading-guide.md](sources/research-process/inbox/2026-09-09-coordination-space-reading-guide.md) | 确认的是整理写入；阅读启发与阅读顺序是候选；外部事实本轮未核验 | 阅读范围透明；调研与执行区分；避免猜测实现。原文逐处标明未确认启发和文献访问限制，不以“已保存”表示用户已阅读或方案已采用。 | “讨论背景”（L7–10）；“2. 经典与直接相关的阅读材料”（L21–70）；“3. 建议阅读顺序”（L71–86）；“4. 保留的理解与问题”（L87–97） |
| [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) | 原文注明完善表述经用户审阅确认；原始表述与后续说明并列保存 | 保留原话；修正与作者区分；学习材料边界。完整保留用户两段原理解、agent 讨论后完善、追加概念说明和图示局限，是不改写历史理解的具体记录。 | “用户原始表述”（L11–14）；“用户补充表述：搜索”（L15–18）；“与 agent 讨论后的完善表述”（L19–89）；“补充讨论：路径拆分与基本方片”（L90–130）；“配套插图”（L131–155） |
| [inbox/2026-09-16-generator-scene-and-target-representation.md](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md) | 局部表示已确认；文件组织候选未确认；包含一次意图澄清 | 不要代用户补齐方案；确认粒度；未决事项。“尚未确定”一节明确记载用户要求补充未决事项，agent 却补方案后的纠正，具有直接协作教训。 | “当前情况”（L5–10）；“已确认：原始访问目标的定义”（L29–41）；“尚未确定：最终数据与名义场景的组织”（L50–64）；“其他待讨论事项”（L65–71）；“格式版本的含义”（L72–76） |
| [projects/dataset-generator/README.md](sources/research-process/projects/dataset-generator/README.md) | 旧项目快照；首版范围和验收仍待讨论 | 需求状态；入口；范围未确认。显式说明待讨论问题不代表已确认需求；与后续代码仓库成果保留时效差异。 | “当前情况”（L8–11）；“待讨论”（L12–19）；“材料入口”（L20–24） |
| [projects/stop-n-go/README.md](sources/research-process/projects/stop-n-go/README.md) | 用户报告已复现；验证范围未补齐 | 用户报告与验证事实；避免预设缺陷。把报告、验证结果与潜在不足分开，是证据类别在项目入口中的实际表达。 | “当前情况”（L7–11）；“材料入口”（L12–19） |

#### 辅助材料

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [references/stac-reading-notes.md](sources/research-process/references/stac-reading-notes.md) | 用户笔记与 agent 补充；论文内容与构造例子均未由本轮独立验证 | 署名与来源；构造例子；矛盾保留。作为共同学习的具体材料，标明 agent 补充依据及未核对范围，并保留正文与表格矛盾待核对的记录。纳入理由在证据表达而非算法本身。 | “实验设置”（L20–58）；“测量内容与解释边界”（L45–50）；“待核对：正文与表 I 不一致”（L51–58）；“schedule的过程”（L71–138）；“碰撞记录以及如何结合碰撞历史重规划”（L139–230）；“个人的理解”（L231–240） |
| [references/lavalle-planning-algorithms-7-2-multiple-robots.md](sources/research-process/references/lavalle-planning-algorithms-7-2-multiple-robots.md) | 个人阅读记录与教学示例；不能把 agent 示例当真实实验 | 个人理解；原始讨论出处；教学验证边界。保留个人未理解状态，通过链接关联完善表述而不覆盖原笔记，并标明教学示例的性质和限制。 | “交互示例：路径碰撞与协调空间障碍”（L44–52）；“Cube complex：我的理解与讨论记录”（L59–68）；“已有相关讨论”（L69–74） |
| [assets/cube-complex/README.md](sources/research-process/assets/cube-complex/README.md) | 归档、版本修正与生成方法记录；教学假设不是实验结果 | 用户与 agent 共创；版本；维护入口；产物限制。保留共同构图、v2 排版修正、源文件维护与验证限制的说明；绘图算法和图片本身不作为协作约定。 | “用途与来源”（L5–12）；“文件与维护入口”（L13–24）；“生成方法”（L25–37）；“记号与限制”（L38–44） |
| [assets/path-collision-equivalence/README.md](sources/research-process/assets/path-collision-equivalence/README.md) | agent 构造教学例子与开发检查自述；未做真实机器人实验 | 教学产物来源；验证层级；维护与复制入口。以完整原文保留教学例子的来源、局限和开发验证口径，避免从图形推断真实任务结果。 | “路径碰撞与协调空间：交互示例”（L1–33）；“标签页一：不同路径，相同障碍”（L5–14）；“标签页二：三机器人碰撞关系与完整协调空间”（L15–33） |
| [local-paths.md](sources/research-process/local-paths.md) | 被忽略的本机文件；位置项待填写、访问能力不能默认成立 | 本地与云端；同步边界；未跟踪材料。补足版本控制外的当前本地材料，原文明确路径不等于云端可访问或文件已同步。 | “本机路径”（L1–8） |


### multiarm-problem-gen

原始来源：`/home/fainic/data/multiarm-problem-gen`。表内文件路径均相对于该仓库根目录；链接指向本组副本。

#### 协作约定

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md) | 已确认约定：仓库现行声明；本轮未独立核验逐条确认链 | 架构参与；自主权限；阅读隔离；测试；记录；交接。直接汇集当前协作约定，尤其区分局部自主实现、架构确认、受限阅读、契约缺口、测试目的和真实统计。 | “人与 agent”（L9–20）；“记录”（L21–28）；“实现与验证”（L29–46）；“Git 与交接”（L47–58）；“架构决策与自主权限”（L67–76）；“从设计进入实现”（L77–91）；“实现任务的阅读边界”（L92–105）；“Serena 使用约定”（L106–119）；“契约缺口与异常处理”（L120–134）；“验证与记录”（L135–157） |
| [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md) | 仓库现行 Git 约定；集成方式未统一定死 | 授权；分支；提交；共享历史；逻辑审阅。保留 main 与探索分支的采用含义、提交建议不等于授权、语义冲突复核与集成方式的留白。 | “探索分支与长期主线”（L3–25）；“何时提交与集成”（L26–40）；“集成方式”（L41–52）；“主线提交”（L79–116）；“操作边界”（L117–124） |
| [README.md](sources/multiarm-problem-gen/README.md) | 当前入口与已实现范围声明；自主试验未获用户最终设计接受 | 学习与理解；两仓库记录边界；状态语义。说明用户架构参与和跨项目经验的保存位置，同时直接提示试验实现不代表最终设计接受。 | “仓库组织”（L14–28）；“设计与学习”（L29–33） |
| [docs/README.md](sources/multiarm-problem-gen/docs/README.md) | 当前文档组织声明与历史过程入口；方案不等于执行 | 当前设计与历史；记录分类；不执行历史任务。明确按内容目的分类讨论与实施，保留原方案并关联结果，而非将方案改写成已执行成果。 | “当前阶段”（L3–17）；“讨论与方案”（L18–38）；“实施过程与复盘”（L39–46）；“接下来讨论”（L53–60）；“怎样组织记录”（L61–69） |

#### 讨论与决策

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md) | 历史初始化记录；已采用文档组织；不代表已实现项目 | 学习目标；最简组织；跨仓库追溯。保存仓库起点、用户学习目标、讨论快照与正式代码文档的分工，以及不预设复杂流程。 | “本次组织选择”（L11–16）；“学习与协作目标”（L17–22）；“前序材料”（L23–30）；“下一步”（L31–33） |
| [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md) | 局部方向已确认；候选细节与之后追加的确认分阶段保留 | 最小但完整；实践暴露问题；范围；共同语义。记录用户查看实际样例后提出问题、agent 独立评判、后续取舍和修正；不是只保存输入配置。 | ““最小但完整”的含义”（L24–31）；“接下来需要明确”（L48–57）；“追加：基准场景与可视化暴露的三个问题”（L58–121）；“追加：问题 1、2 的方案”（L122–165）；“追加：问题 3 的方案”（L166–237） |
| [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md) | 讨论过程与局部方案；名称、字段不是完整接口定稿 | 具体反馈修正建议；减少抽象；模型与实例。Mesh 小节记录用户质疑提前加载和额外层后方案调整；其他节保留渐进澄清与未决细节。 | “从读取结果谈起”（L9–14）；“Mesh：从提前解析转向按需加载”（L37–46）；“Pose、Frame 与场景复用”（L47–54）；“场景规则的澄清”（L93–98）；“后续计划”（L99–103） |
| [docs/notes/discussions/2026-09-23-generation-distributions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-23-generation-distributions.md) | 讨论中的局部方案；首版范围未扩大为一般相关分布 | 共同语义；职责拆分；用户纠正；避免新增开关。保留用户如何纠正标量／多维及作用关联含义，以及确认部分语义后仍保留应用过程未知。 | “从扰动的职责拆分谈起”（L7–10）；“分布以多维联合分布表示”（L11–16）；“作用关联需要明确分量与含义”（L17–41）；“两个使用例子与边界”（L42–47） |
| [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md) | 读取组织为设计方向；精确模块、接口与可变性待确认 | 让用户理解数据流；通俗术语；不提前细化内部。记录用户要求从对象清单转为逐步运行流程及 agent 的说明调整；明确组织职责不意味着单个大类。 | “从对象清单转向运行流程”（L7–14）；“运行流程与职责”（L15–28）；“一个协作例子”（L29–49）；“边界与后续”（L50–56） |
| [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) | 任务划分依据；不表示所有接口和粒度已定稿 | 任务粒度；依赖契约；独立验收；提前交付公共接口。明确交付单元与 class／文件的区别，记录依赖顺序、资源接口前置及实现前范围和验收条件。 | “划分方案”（L7–21）；“路径与共享资源的归属”（L22–27）；“建议实现顺序”（L43–53） |
| [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md) | 澄清与候选建议；未决定是否拆开任务 | 任务范围与代码职责；契约隔离实验。直接讨论代码职责分离为何不自动构成 agent 阅读隔离，任务粒度需对应所验证的边界。 | “问题与澄清”（L7–24）；“对契约隔离实验的影响”（L25–31） |
| [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md) | 局部语义与可变性已确认；精确接口候选；本文件不授权实现 | 用户纠正；公开契约；局部自主；范围。保留从“全部不可变”经用户纠正改为 Frame 位姿可替换的讨论，明确实施前应补什么而不设计全部内部函数。 | “构造、引用与可变性”（L31–50）；“校验职责”（L51–67）；“首次交付与验收”（L68–79）；“实现前还需补齐”（L80–86） |
| [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md) | 讨论确认的接口方向；当时未实现；写方案不等于执行授权 | 文件与内存抽象；修正建议；范围词义；依赖阅读。保留用户要求统一表示后的方案修正，明确“完整支持”不能自动扩展到未出现能力，执行范围与内部自主选择分开。 | “目标与本次修正”（L7–14）；“错误与验收”（L118–125）；“实施范围与准备”（L126–132） |
| [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md) | 已讨论的实施前方案；不代表授权或实际完成；少量环境只读检查是当时观察 | 实施就绪；契约先行；环境验收；授权阶段。记录从设计进入实现的阅读、修改、验收及先后交付边界，明确空测试与方案写入不能冒充验收或代码授权。 | “第一部分：统一 Docker／Compose 环境”（L7–42）；“第二部分：单元 1 基础表示”（L43–84）；“执行顺序、权限与就绪判断”（L85–93） |
| [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md) | 已确认职责与范围；候选字段待具体化；实施前方案不是执行授权 | 架构修正；当前与未来范围；阅读边界；准备判断。记录用户纠正统一资源管理和去前缀选择，保留未来手动登记的未决规则及实现者可自主补充的边界。 | “本轮选择与保留方向”（L90–97）；“验收与允许修改范围”（L119–136）；“实施准备判断”（L137–143） |
| [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md) | 授权自主试验的 agent 决定；不代表用户接受最终设计；含已披露的内部测试信息混入 | 决策与实现分工；备选与理由；复议；污染来源。保留决策者信息包、依赖补丁分工、契约缺口修正及 D6-4 的内部断言来源，是完整试验决定而非通用规则。 | “信息包与边界”（L5–12）；“D4-1：独立多维分布表示”（L13–32）；“阅读、用量与时间”（L33–38）；“D6-1：先补公开资源快照”（L39–48）；“D5-3：mean 的 configuration 名称消歧”（L140–147）；“D6-4：既有真实样例测试的单字符串维护”（L148–160） |

#### 背景与历史经验

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [docs/notes/discussions/2026-09-21-output-validity-semantics.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-21-output-validity-semantics.md) | 已确认的是输出语义；尚未实现或验证全部要求 | 澄清自然语言；保证边界；需求与实现区分。用户“单独可达”的含义经讨论具体限定，记录端点、路径与多臂任务保证的区别，避免交接中扩大承诺。 | “讨论与确认”（L7–12）；“保证边界与未决事项”（L21–25） |
| [tools/baseline_validation/ur7e_table/README.md](sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) | 历史基准检查与后续说明；旧报告哈希已不匹配当前场景；本轮未执行 | 实践反馈；旧结果不覆盖；证据失效；验证范围。保留布局由实际检查修正、缺依赖时不宣称重验、旧报告原样保存且新结果另存的过程，技术参数作为原文上下文。 | “布局与参数依据”（L17–42）；“数值检查及其范围”（L95–120）；“目录整理说明（2026-09-21）”（L125–129） |

#### 实施与复盘

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md) | 历史实施与验收自述；当时两次提交获用户确认；本轮未重跑 | 授权执行；环境误诊；独立预期；阅读自述；交接。记录网络失败不能误说成版本不存在、不同验收口径、未读依赖内部及 agent 自述的证据局限。 | “基线与范围”（L5–12）；“环境验收（先于基础表示实现）”（L13–27）；“基础表示验收”（L28–44）；“契约是否足够”（L45–52）；“阅读范围与工具限制”（L53–67）；“交接”（L68–70） |
| [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md) | 历史实施结果；后续 Material 删减另记；测试及无越界均未由本轮独立证明 | 保护原改动；测试预期纠正；契约隔离；局部不足。记录手工数量预期错误后依据 XML 独立计数修正测试、对权限和工具问题的回退及后续修正链接。 | “起点与完成内容”（L7–16）；“实际验证”（L17–38）；“契约与阅读边界”（L39–48）；“剩余边界与局部不足”（L49–56） |
| [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md) | 原文注明接口删减经用户确认；是该次授权，不是整体重设计 | 独立审查；需求依据；范围收缩；历史不覆盖。独立审查发现扩展依据不足，用户确认收缩接口，旧实施结果保留并关联修正；体现必要回归和限定工具回退。 | “原因与变更”（L5–12）；“验证与边界”（L13–19） |
| [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md) | 历史实施与验证记录；阅读、用时和工具限制依记录自述 | 先明确测试目的；保护已有变更；计时；契约边界。保存测试目的的独立依据、缓存预期错误修正、工具边界和可取得统计；未把阅读自述或 token 长度当独立证据。 | “完成范围”（L5–15）；“测试目的与依据”（L16–29）；“实际结果”（L30–50）；“阅读范围与工具边界”（L51–68）；“用时与 token”（L69–81）；“契约判断及剩余限制”（L82–86） |
| [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) | 授权自主试验实施总记录；不代表用户接受最终设计；历史验收本轮未重跑 | 多 agent 分工；隔离失败修复；独立集成；时间与用量；授权。保存主 agent 协调、专属实现、决策回流、污染后重启、166 项历史验收口径和并行墙钟不能与部分子任务时间相加的限制。 | “起点与边界”（L5–12）；“初始验证事实”（L13–20）；“任务与决定入口”（L21–33）；“主 agent 集成测试目的（编写前）”（L34–39）；“最终验收事实”（L40–62）；“结果、决定与限制”（L63–70）；“用量与计时”（L71–90）；“本地交付状态”（L91–93） |
| [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md) | 独立上下文的历史实施自述；授权试验决定尚未最终接受 | 专属范围；预期依据；父 agent 信息；计时。明确自身验证与父 agent 提供结果的区别，记录上下文、测试限度和计时未涵盖起步／收尾。 | “完成内容”（L7–13）；“测试目的与独立依据”（L14–23）；“实际验证”（L24–36）；“阅读范围与工具”（L37–50）；“时间、用量与未决项”（L51–61） |
| [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md) | 授权试验的最小补丁；历史验证与阅读自述 | 公共缺口补丁；并行分工；模块边界；工具回退。记录由资源负责人补公共快照而避免调用方读私有缓存的实际补丁，以及混合活动无法精确拆分用时。 | “范围与测试目的（编写测试前）”（L5–12）；“执行结果”（L13–20）；“实际阅读与工具边界”（L21–28）；“时间与用量”（L29–33） |
| [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md) | 已发生的准备中止自述；未写实现或测试、未运行测试 | 间接越界；上下文污染；坦诚报告；独立重启。直接记录允许读取的决定文件夹带内部测试断言，看到后不能宣称忘掉，停止并移交过滤后的独立上下文。 | “实际产物与停止原因”（L5–10）；“实际阅读”（L11–16）；“时间、用量与边界”（L17–21） |
| [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md) | 过滤后独立实现的历史记录；不继承停止上下文；设计未获最终接受 | 过滤交接；独立测试输入；回交修复；统计限制。对照停止记录保留重启后的边界与结果，尤其测试发现实现修正归属、未暂存文件不被 diff 检查覆盖及完整分项用时不可用。 | “单元 5：Generation 独立实现与验证”（L1–48）；“测试目的、依据与结果”（L11–30）；“读取边界与用量”（L31–45）；“契约与局限”（L46–48） |
| [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md) | 独立实现历史结果；主 agent 回归结论明确属于交接信息 | 专属范围；实际验证；公开声明查询；计时与边界。保留实现者仅查询依赖公开声明、独立 fixture、最小元数据迁移及自身执行与主 agent 报告的区分。 | “完成范围”（L5–14）；“测试目的与依据”（L15–22）；“实际结果”（L23–39）；“契约、阅读与工具”（L40–55）；“用时与用量”（L56–64） |

#### 辅助材料

| 来源文件 | 原文状态与证据边界 | 相关主题与纳入理由 | 关键章节 |
| --- | --- | --- | --- |
| [docs/design.md](sources/multiarm-problem-gen/docs/design.md) | 混合时间快照：已确认语义、保留的旧方案、实施追加及自主试验并存 | 设计入口；状态更新；候选抽象；避免过时描述。纳入的是原文顶部的状态追加方式与候选／未决标记，用来理解历史段落不能被当作当前能力清单。 | “当前设计草稿”（L1–111）；“候选抽象与待验证的问题”（L89–100）；“未决事项”（L101–111） |
| [docs/notes/discussions/2026-09-23-input-bundle.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-23-input-bundle.md) | 讨论方案；原文明确当时未迁移样例 | 方案与执行分离；路径归属；任务范围。作为后续自主试验的架构交接背景，具体保留“当前命名冲突待迁移”的状态，便于追溯后续元数据变更。 | “从目录管理到输入包”（L7–12）；“如何发现场景与生成规则”（L13–18）；“路径、资源与实现边界”（L50–57） |
| [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md) | 授权自主决定的过滤公开交接；设计未获用户最终接受 | 上下文过滤；契约足够性；隔离交接。它是停止污染上下文后重启任务所用的实际过滤产物，技术内容为交接证据，不能当本轮实现指令。 | “单元 5 公开交接包”（L1–56）；“D5-1：保留 YAML，公开统一作用关联”（L5–25）；“D5-2：精确 YAML、顺序、参数与状态边界”（L26–46）；“D5-3：mean 的 configuration 名称消歧”（L47–56） |
| [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md) | 授权自主决定的过滤公开交接；设计未获用户最终接受 | 读写分工；依赖补丁；最小迁移；交接过滤。保留过滤交接如何公开依赖行为、限定 U6 范围并将旧内部测试维护留给主 agent 的实际做法。 | “单元 6 公开交接包”（L1–58）；“D6-1：先补公开资源快照”（L5–15）；“D6-3：真实样例最小迁移与验收”（L45–58） |
| [docs/contracts/primitives.md](sources/multiarm-problem-gen/docs/contracts/primitives.md) | 由已确认方案整理的公开依赖契约；不是新协作规则 | 公开行为；责任边界；独立验收。作为契约隔离实践实际使用的原始交接材料，保留构造与行为、职责、错误、验收入口的完整接口约束。 | “导入与构造”（L5–22）；“数值与错误”（L23–30）；“对象行为”（L31–48）；“职责边界”（L49–54）；“验收入口”（L55–63） |
| [docs/contracts/resources.md](sources/multiarm-problem-gen/docs/contracts/resources.md) | 已实现公开契约；公开快照扩展为自主试验结果，尚未最终接受 | 状态归属；公开快照；失败语义；不读私有缓存。作为 D6-1 缺口与补丁的对应公开产物纳入，技术约束支撑试验边界而非直接提炼通用规则。 | “统一资源管理公开契约”（L1–32） |
| [docs/contracts/robot-model.md](sources/multiarm-problem-gen/docs/contracts/robot-model.md) | 已确认单元方案的公开契约；包含后续授权 Material 收缩 | 契约可观察行为；默认；支持范围；验收。保留实现任务使用的原始依赖契约，以及与旧实施笔记变化关联的当前支持边界。 | “只读表示”（L12–38）；“缺失与默认”（L39–53）；“输入范围和检查”（L54–63）；“验收入口”（L64–66） |
| [docs/contracts/scene.md](sources/multiarm-problem-gen/docs/contracts/scene.md) | 已确认单元 3 方案的公开契约 | 职责；身份；状态；失败；阅读隔离依赖。它是后续 Generation 和 Bundle 独立实现使用的真实公共信息包，保留行为和不保证的能力。 | “公开入口与表示”（L5–29）；“Frame 名称与引用”（L30–35）；“YAML 输入”（L36–63） |
| [docs/contracts/distributions.md](sources/multiarm-problem-gen/docs/contracts/distributions.md) | 授权自主试验公开契约；原文明确用户未最终接受设计 | 参数表示与采样区分；公开交接。保留 D4-1 的实际公开契约，供核对前后交接和验收范围，不视作用户已接受的长期规则。 | “参数与维度”（L17–26）；“错误与示例”（L27–43） |
| [docs/contracts/generation.md](sources/multiarm-problem-gen/docs/contracts/generation.md) | 授权自主试验公开契约；原文明确用户未最终接受设计 | 契约边界；依赖隔离；验证保证。与过滤交接和干净上下文结果对应的原始产物，保留关联、错误和验证边界。 | “表示与关联”（L17–30）；“严格 YAML”（L31–46）；“验证边界”（L47–49） |
| [docs/contracts/input-bundle.md](sources/multiarm-problem-gen/docs/contracts/input-bundle.md) | 授权自主试验公开契约；原文明确用户未最终接受设计 | 公开快照；交付身份；路径归属；失败。与 U6 独立实施对应的完整公开产物，用于核对仅凭公共信息如何组织并交付结果。 | “交付与身份”（L15–30）；“根配置与发现”（L31–42）；“验证边界”（L43–45） |
| [docker/README.md](sources/multiarm-problem-gen/docker/README.md) | 当前验收入口和当时环境记录；依赖与历史验收结果本轮未运行核实 | 复现；就绪；完整命令；空测试；挂载与阅读权限。保存实际环境就绪条件、网络限制、复现版本和挂载整个仓库仍不放宽阅读边界的说明。 | “Docker／Compose 开发环境”（L1–158）；“环境组织”（L40–47）；“固定版本与来源”（L48–68）；“自主试验：完整输入包入口与验收”（L128–158） |
| [examples/ur7e_table/README.md](sources/multiarm-problem-gen/examples/ur7e_table/README.md) | 自主试验后的样例入口；名义输入读取不等于生成或可行性验收 | 可搬移交付；最小迁移；引用与状态。作为 D6-3 迁移与用户验收解释的文档证据纳入，保留旧 ID 的兼容影响和已实现能力边界。 | “内容与入口”（L5–51）；“样例内容与限制”（L52–58） |
| [tools/scene_preview/README.md](sources/multiarm-problem-gen/tools/scene_preview/README.md) | 预览原型与本机开发验证自述；不是生成器实现或碰撞验收 | 原型目的；证据依赖；旧报告校验；产物局限。是首份输入样例中“可视化暴露问题”的对应材料，保留历史报告不自动加载、哈希匹配局限与实际验证范围。 | “显示内容”（L17–28）；“文件”（L29–41）；“已验证与限制”（L42–47）；“可选开发材料”（L48–52） |

## 尚未消除的不确定事项

1. research-process 的 state.md 和项目入口仍写生成器尚未实现；代码仓库已有 09-29／09-30 后续实施记录。两者原样保留，研究侧旧快照不用于否定后续成果。
2. docs/design.md 保留旧方案段落，并在顶部追加已实现与自主试验状态；当前公开契约与旧候选不能混为同一时点的决定。
3. 单元 4–6 的 agent 决定、公开交接包和实施结果均明确不代表用户接受最终设计。本轮无法从当前文件确认其之后是否获接受；不查历史或聊天补结论。
4. 越界中止、测试数量、无越界自述和用时统计是原始记录中的历史声明，没有独立工具日志闭包。本轮仅验证副本一致，不重新证明历史实验。
5. 外部论文、博客、论坛和厂商链接保持原文；本轮没有访问或核验其最新内容，也不将调研中的候选流程当已确认规范。
6. 来源中的技术依赖、模型、代码、图形和部分纯业务文档未全部收集；原文内引用保持原样，可能指向未纳入内容。INDEX 指向纳入副本及审计文件的本地路径已核验，未声称全部原文链接或外部路径都可用。

## 检查与筛选记录

- 69 份副本均与当前原文逐字节一致，SHA-256 和大小逐项登记；关键标题均唯一匹配到原文实际行号。
- 复制前后，两个来源共 268 个非 .git 当前文件的路径、种类、大小、内容摘要及修改时间一致；没有将来源权限或 Git 元数据作为写入目标。
- 本轮未提交、合并或推送，未运行来源脚本、原测试、历史命令或外部检索。
- [逐文件原文与副本清单](audit/collected-manifest.json)、[候选文件初始清单](audit/source-inventory.before.json)、[结束清单](audit/source-inventory.after.json)。
- [人工筛选注解](audit/selection-spec.json)、[未纳入文件与原因](audit/excluded-files.json)、[当前跟踪分类](audit/current-file-tracking.json)、[检索范围与限制](audit/review-coverage.md)。
- [本轮核验结果](audit/verification.json)。
