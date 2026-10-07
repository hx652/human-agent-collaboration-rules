# 原始材料筛选记录

整理日期：2026-10-07T19:52:43+08:00。本次审阅后纳入 47 份、排除 32 份 Markdown；另有 189 份非 Markdown 文件未纳入。没有待决定项。排除仅影响正式材料集，来源、六组档案与 worktree 均保留。

## 内容判断标准

1. 纳入直接的人与 agent 协作约定、共同工作目标、沟通纠偏、授权/职责/交接和实际验证复盘。

2. 不因出现 agent、协作、已确认等词，或被收录文档引用，就自动纳入。

3. 只有技术接口、业务格式、项目状态、普通工具说明或第三方资源，直接排除；有弱相关片段但无独立协作事件的背景材料，记录理由后筛除。

4. 包含明确协作证据的混合文件完整保留，避免以摘录重写其上下文；与技术内容所占比例分开判断。

5. 排除是本次材料集的选择，不删除来源、实验档案或 worktree。

6. 协作规则的现载状态、原文明示确认、候选、历史经验及未知边界分开标注。

## 五份边界材料的用户决定

用户答复原文：**“5 份全部排除”**。执行此选择，没有采用原先“只保留 StAC”建议。

| 文件 | 原先不确定的原因 | 最终处理 |
| --- | --- | --- |
| [research-process/references/stac-reading-notes.md](../experiments/20261007-181827/sol_max/sources/research-process/references/stac-reading-notes.md) | 区分用户正文与 agent 补充；注明正式论文依据、构造例子和未核验范围；保留正文与表格矛盾未决。 同时，正文大部分是算法解释；与已收录的讨论记录相比，这是共同阅读的成品，协作过程记录较少。 | 用户决定排除 |
| [research-process/references/lavalle-planning-algorithms-7-2-multiple-robots.md](../experiments/20261007-181827/sol_max/sources/research-process/references/lavalle-planning-algorithms-7-2-multiple-robots.md) | 保留用户未理解的状态，链接 agent 讨论后的解释，说明构造教学例子的证据边界。 同时，主体为技术阅读提纲；更直接的理解纠偏过程已完整收录于 09-15 讨论与 journal。 | 用户决定排除 |
| [research-process/inbox/2026-09-09-coordination-space-reading-guide.md](../experiments/20261007-181827/sol_max/sources/research-process/inbox/2026-09-09-coordination-space-reading-guide.md) | 明确保存导览不等于完成阅读；agent 启发和已确认方案分开。 同时，主体为文献推荐和技术启发，较少实际协作摩擦或处理过程；同类证据标注已由更直接记录覆盖。 | 用户决定排除 |
| [research-process/assets/cube-complex/README.md](../experiments/20261007-181827/sol_max/sources/research-process/assets/cube-complex/README.md) | 记录用户与 agent 构图、图形来源、维护源文件与导出关系、教学假设。 同时，主要是成果维护说明；讨论过程与资源维护约定已分别保存在已收录的讨论记录和 assets/README。 | 用户决定排除 |
| [research-process/assets/path-collision-equivalence/README.md](../experiments/20261007-181827/sol_max/sources/research-process/assets/path-collision-equivalence/README.md) | 明确例子由 agent 构造、并非书中实例或真实实验，并列出开发验证范围。 同时，主体为交互页面功能和技术说明，未记录具体协作决策或纠偏经过。 | 用户决定排除 |

## 未纳入 Markdown 的逐文件理由

下列路径以来源仓库名开头。链接优先指向保留的试验原件；没有被任何组收录的文件链接到只读来源。

| 文件 | 排除理由 |
| --- | --- |
| [multiarm-problem-gen/docs/contracts/distributions.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/distributions.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/generation.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/generation.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/input-bundle.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/input-bundle.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/primitives.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/primitives.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/resources.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/resources.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/robot-model.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/robot-model.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/contracts/scene.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/contracts/scene.md) | 具体业务 API 的字段、类型和行为契约。交接、契约缺口及隔离成败保留于讨论与实施记录；不把作为依赖的技术接口集合全部复制。 |
| [multiarm-problem-gen/docs/design.md](../experiments/20261007-181827/sol_high/sources/multiarm-problem-gen/docs/design.md) | 面向项目的技术设计入口。顶部历史状态追加具有参考作用，但未单独记录协作问题的处理；记录维护原则与实际追记过程已有直接材料，不再保留整份设计总览。 |
| [multiarm-problem-gen/docs/notes/discussions/2026-09-18-input-output-format.md](/home/fainic/data/multiarm-problem-gen/docs/notes/discussions/2026-09-18-input-output-format.md) | 业务数据格式方案；不因方案带确认/候选状态就把字段和格式全量纳入协作材料。 |
| [multiarm-problem-gen/docs/notes/discussions/2026-09-21-output-validity-semantics.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/notes/discussions/2026-09-21-output-validity-semantics.md) | 主要确定输出的运动学与碰撞保证，是领域语义决定；未展开独立的协作方法、权限或失误处理。 |
| [multiarm-problem-gen/docs/notes/discussions/2026-09-23-generation-distributions.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/notes/discussions/2026-09-23-generation-distributions.md) | 多维分布和作用关联的领域设计取舍；有人与 agent 对话，但未提供超出一般技术方案讨论的独立协作问题处理证据。 |
| [multiarm-problem-gen/docs/notes/discussions/2026-09-23-input-bundle.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/docs/notes/discussions/2026-09-23-input-bundle.md) | 输入包结构、路径与发现规则的领域方案；名称建议和未实施状态不足以单独纳入。任务交接和实施边界保留在专门记录中。 |
| [multiarm-problem-gen/examples/ur7e_table/README.md](../experiments/20261007-181827/sol_max/sources/multiarm-problem-gen/examples/ur7e_table/README.md) | 业务样例内容、调用和能力边界；实际最小迁移与验证过程已在单元 6 及总实施记录中保留。 |
| [multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md](../experiments/20261007-181827/sol_xhigh/sources/multiarm-problem-gen/tools/baseline_validation/ur7e_table/README.md) | 业务数值验证与工具说明；旧报告失效有参考价值，但没有具体人和 agent 的处理过程，相关验证归属与限制已有直接实施记录。 |
| [multiarm-problem-gen/tools/model_preparation/ur7e_2f85/README.md](/home/fainic/data/multiarm-problem-gen/tools/model_preparation/ur7e_2f85/README.md) | 模型准备命令与工具文件入口，属于业务工具说明。 |
| [multiarm-problem-gen/tools/model_preparation/ur7e_2f85/resources-original.md](/home/fainic/data/multiarm-problem-gen/tools/model_preparation/ur7e_2f85/resources-original.md) | 上游模型与许可证来源清单，属于业务资源溯源。 |
| [multiarm-problem-gen/tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md](/home/fainic/data/multiarm-problem-gen/tools/model_preparation/ur7e_2f85/vendor/ur_description/README.md) | 第三方机器人模型技术说明，不是本项目的人和 agent 协作记录。 |
| [multiarm-problem-gen/tools/scene_preview/README.md](../experiments/20261007-181827/sol_xhigh/sources/multiarm-problem-gen/tools/scene_preview/README.md) | 预览界面功能、依赖和操作说明；引发用户反馈的过程已在首份输入样例讨论中保留。 |
| [research-process/assets/cube-complex/README.md](../experiments/20261007-181827/sol_xhigh/sources/research-process/assets/cube-complex/README.md) | 用户决定排除（2026-10-07）：5 份全部排除。原评审：主要是成果维护说明；讨论过程与资源维护约定已分别保存在已收录的讨论记录和 assets/README。 |
| [research-process/assets/path-collision-equivalence/README.md](../experiments/20261007-181827/sol_max/sources/research-process/assets/path-collision-equivalence/README.md) | 用户决定排除（2026-10-07）：5 份全部排除。原评审：主体为交互页面功能和技术说明，未记录具体协作决策或纠偏经过。 |
| [research-process/inbox/2026-09-09-coordination-space-reading-guide.md](../experiments/20261007-181827/sol_max/sources/research-process/inbox/2026-09-09-coordination-space-reading-guide.md) | 用户决定排除（2026-10-07）：5 份全部排除。原评审：主体为文献推荐和技术启发，较少实际协作摩擦或处理过程；同类证据标注已由更直接记录覆盖。 |
| [research-process/inbox/2026-09-09-multi-arm-research-focus.md](/home/fainic/data/research-process/inbox/2026-09-09-multi-arm-research-focus.md) | 研究对象与未来研究问题；没有独立的协作约定或具体协作问题处理。相关独立审查过程已在相邻讨论记录中保留。 |
| [research-process/inbox/2026-09-14-todos-and-draft.md](../experiments/20261007-181827/sol_xhigh/sources/research-process/inbox/2026-09-14-todos-and-draft.md) | 个人待办与准备写草稿的计划，没有作者确认链或具体协作事件；不将普通待办提升为协作规则证据。 |
| [research-process/inbox/2026-09-17-generator-input-output-format.md](/home/fainic/data/research-process/inbox/2026-09-17-generator-input-output-format.md) | 输入输出字段、目录与数学语义的业务格式方案。候选标签本身不足以把整份格式定义纳入协作材料。 |
| [research-process/inbox/2026-09-18-generator-input-output-format.md](/home/fainic/data/research-process/inbox/2026-09-18-generator-input-output-format.md) | 业务数据格式修订快照；相关授权、未决事项误解和协作过程已由原讨论记录承载，技术规范不随之全量纳入。 |
| [research-process/journal.md](/home/fainic/data/research-process/journal.md) | 空文件，无可供判断的原始内容。 |
| [research-process/projects/dataset-generator/README.md](../experiments/20261007-181827/sol_high/sources/research-process/projects/dataset-generator/README.md) | 早期项目目标、待办和占位入口；不含独立协作事件或详细约定，组织原则保留于项目总索引。 |
| [research-process/projects/stop-n-go/README.md](../experiments/20261007-181827/sol_high/sources/research-process/projects/stop-n-go/README.md) | 早期复现状态与项目入口，含通用证据提示但没有展开实际协作问题；原始事实区分原则已在直接约定中保留。 |
| [research-process/references/lavalle-planning-algorithms-7-2-multiple-robots.md](../experiments/20261007-181827/sol_max/sources/research-process/references/lavalle-planning-algorithms-7-2-multiple-robots.md) | 用户决定排除（2026-10-07）：5 份全部排除。原评审：主体为技术阅读提纲；更直接的理解纠偏过程已完整收录于 09-15 讨论与 journal。 |
| [research-process/references/stac-reading-notes.md](../experiments/20261007-181827/sol_max/sources/research-process/references/stac-reading-notes.md) | 用户决定排除（2026-10-07）：5 份全部排除。原评审：正文大部分是算法解释；与已收录的讨论记录相比，这是共同阅读的成品，协作过程记录较少。 |
| [research-process/references/stop-n-go-reading-notes.md](/home/fainic/data/research-process/references/stop-n-go-reading-notes.md) | 论文链接和未填写的阅读提纲，没有协作过程内容。 |
| [research-process/state.md](../experiments/20261007-181827/sol_high/sources/research-process/state.md) | 早期项目进度快照，只报告工作流确认和暂缓计划，没有展开其协作做法；起点、组织决定与具体实施记录已保留。 |

## 其他未纳入文件

189 份非 Markdown 文件包括业务源码和测试、YAML／URDF、网格模型、图片及论文、第三方资源、构建产物、预览文件、Obsidian／Serena 配置与缓存。未因关键词或引用关系递归收录；具体路径、大小和摘要均在 [selection.json](selection.json)。二进制文件没有逐页或视觉审阅，业务代码没有逐行全审，不声称穷尽其潜在协作批注。

## 纳入理由与保真

正式索引按文件给出相关主题、状态、理由和章节。原文与说明分开存放，既不删节混合技术文档，也不将候选建议升格为确认规则。来源原件、归档副本和正式副本逐字节比较；来源与实验档案在本次操作前后分别比较。
