# 单元 4–6 自主实现试验

状态：实现、最终验收与记录完成。用户授权范围内的探索性实现；不表示用户接受最终设计。

## 起点与边界

- 主 agent `/root`；开始时间 2026-09-30 12:58:08 UTC（北京时间 20:58:08）。
- 起始分支 `codex/unit-3-scene-design`，提交 `aa98559ecec51559dbcd2ce24e8853cf61263ffa`，工作区干净；目标分支原不存在，已从该提交创建 `codex/autonomous-units-4-6`。
- 用户明确授权方案、决定、代码、测试、文档及英文阶段性本地提交；不合并 main、不推送、不改写已有提交，不修改 AGENTS.md。
- 单元 4→5→6 分别由独立上下文实现 agent 承担；关键议题交独立决策 agent，先记录再执行。主 agent 负责协调、共享文档和最终集成验收。
- 不实现采样、生成场景或复制、FK／IK、碰撞、规划、输出数据集、有关节环境或内部 link frame。不改真实几何、位姿、关节数值和模型资源。

## 初始验证事实

当前执行环境可访问目标仓库和 research-process；后者无 HEAD、现有文件未跟踪，未修改。已读取其 overview.md、state.md、projects/README.md；其中进展是旧记录，不覆盖本仓库当前事实。

目标仓库已读取用户指定入口、四份讨论、单元 1–3 全部公开契约及真实 scene/generation 样例。Serena 已初始化并切换项目，未执行 onboarding 或加载全部历史。

`.git` 和 Docker socket 默认受环境限制；经工具提权执行用户已授权操作后，分支创建及环境检查成功。现有 Compose dev healthy，Python 3.13.15、固定工具、可编辑导入、UID/GID 检查通过。基线回归：primitives 21、resources 5、robots 15、scenes 20，共 **61** 项通过；pip check 通过。基线执行工具墙钟 2.966 秒（含 Compose 启动调用），不是完整测试阶段人工用时。

## 任务与决定入口

- 决策 agent `/root/design_decisions`，`fork_turns=none`；仅公共材料，独占[决定记录](../discussions/2026-09-30-autonomous-units-4-6-decisions.md)。交接提供用户边界、已验证事实、未知事项和合理备选，不提供前序实现内部摘要。
- 单元 4 `/root/unit4_distributions`，`fork_turns=none`，只负责 distributions 实现、专属测试和契约；D4-1 已记录后开工。
- 资源补丁 `/root/resource_snapshots`，`fork_turns=none`，只负责 resources 既有模块及专属测试／契约；D6-1 明确最小公开快照扩展后开工，可与单元 4 独立并行。
- 单元 4 已完成，Docker 25 项通过；资源补丁已完成，Docker 12 项通过（含原 5 项）；具体记录见各自实施记录。
- 单元 5 首个准备上下文 `/root/unit5_generation` 读取原决定文件时意外接收一条旧场景测试断言。已在写实现前停止，未写实现／测试；留下公开契约草稿和[停止记录](2026-09-30-unit-5-preparation-stopped.md)，不声称此前上下文仍纯粹隔离。
- 已抽取不含依赖内部测试的单元 [5](../discussions/2026-09-30-unit-5-public-handoff.md)、[6](../discussions/2026-09-30-unit-6-public-handoff.md) 公开交接包。新的 `/root/unit5_generation_clean` 以 `fork_turns=none` 独立开始单元 5，未继承停止上下文；可独立审阅／改写公开契约草稿，不读取旧准备记录。这是修复交接范围，不是更换决策者或隐藏已发生的越界。
- 主 agent 已按前述测试目的编写 `tests/integration/test_bundle_acceptance.py` 四项完整包验收，等待单元 6 完成后执行；不能将编写记为通过。
- 单元 5 `/root/unit5_generation_clean` 首轮 Docker 28 项通过后，单元 6 `/root/unit6_bundles` 才开工，`fork_turns=none`，只收到过滤后的公开决定、契约与验证结论，负责 bundles 及必要样例元数据迁移。U5 收尾发现非法 YAML 控制字符的异常包装遗漏，由原 U5 agent 补测修复，不改变契约。
- 主 agent 在 Docker 通过公开入口独立读取真实 Generation 两次：13 个 binding、双臂各 4 次访问、seed=42/count=10/status 完整保留；两次引用同一 Scene，所有 Frame.pose 引用和名义规划状态保持不变。工具命令墙钟 0.149 秒，UTC 完成检查点 13:18:18。
- 已保存阶段提交 `bbc5a16`（Add distribution parameters and resource snapshots）、`b6a4c64`（Add Generation representations and strict reader）。最终包与汇总记录提交见本分支 Git 历史；本文件不写自己的未来提交哈希。

## 主 agent 集成测试目的（编写前）

以公开契约和用户验收项为依据，最终从完整包入口验证关联，而不是复刻 reader 内部：真实输入的数量、命名中心及任务字段；两份 Generation 引用同一 Scene；多 Scene 共享模型／mesh；有序分量映射和访问序列身份；整包搬移后路径仍在新根下；成功和失败读取都不改输入文件或名义状态；mesh 内容不打开。独立小输入用于给出人工可核对的顺序、边界和失败预期。

将检查文件发现排序、重复规范路径、跨目录 Scene 引用、ID 冲突和缺失文件的失败行为。最终依据决策记录具体化案例，不在测试中自行决定领域语义。集成失败回交对应实现 agent；通过只说明读取、参数和引用组织符合本次契约，不说明采样、限位内样本概率、碰撞、可达性或规划可行性。

## 最终验收事实

2026-09-30 13:26:16 UTC（北京时间 21:26:16）的最终统一执行：Docker 环境检查通过，Python 3.13.15、固定工具与 UID/GID 符合仓库要求；pip check 通过。八组 **166 项**全部通过，每组数量非零。命令与真实包使用入口见 [Docker README](../../../docker/README.md#自主试验完整输入包入口与验收)。

| 测试组 | 数量 | 本次 unittest 执行秒数 |
| --- | ---: | ---: |
| primitives | 21 | 0.004 |
| resources | 12 | 0.018 |
| robots | 15 | 0.172 |
| scenes | 20 | 0.548 |
| distributions | 25 | 0.002 |
| generation | 29 | 0.831 |
| bundles | 40 | 0.508 |
| integration | 4 | 0.313 |

表内执行累计 2.396 秒；统一工具命令墙钟 6.557 秒含环境与 Compose 往返，不与 agent 活动时间重复相加。此前基线、各 agent 专属执行与主 agent 中间复查是重复验证，不把它们累计成更多不同用例。

主 agent 的四项集成实际验证：真实包一 Scene／一 Generation、13 个 binding、双臂六维与各四次访问、所有任务字段；临时搬移后的两 Scene／四 Generation 按声明及文件名次序交付，同 Scene 被多份规则引用、跨 Scene 共享模型与 mesh；另一次读取使用新 context；成功和失败读取均不改输入字节和名义状态；禁止 reader 打开 STL／DAE；缺 Generation 失败后补回输入可用同一 BundleReader 再读。单元 6 的 40 项另覆盖发现、重复规范路径、符号链接、ID 冲突、目录伪装、缺失、不可读、严格 YAML 和跨文件错误。无效／缺失根路径的额外公开入口检查也返回 InputReadError。

样例迁移校验以开工时 46 个文件的 SHA-256 与最终文件对比：原文件仅 README 和 scene.yaml 改变，新增 bundle.yaml，无删除；scene.yaml 的差异精确为 scene_id 从 ur7e_table_baseline 改成 tabletop。generation、模型、mesh、许可证与来源文件字节未变。比较用临时清单不是长期证据的唯一入口：原文件保存在明确 Git 基点，最终差异和本记录可重现该检查。依据 D6-4，主 agent 仅适配既有场景验收中的同一 ID 字符串，其他旧测试逻辑未改；迁移后 20 项场景测试通过。

主 agent 以 Serena 审阅 Generation 构造不变量、YAML decode／读取，以及 BundleReader 的组织／根配置解析等局部符号，并检查新增公开 docstring 和输入校验标记；没有代写单元实现，也未将这些内部内容交接给后续实现 agent。首次简单 docstring 扫描将私有类内部方法误列为公开项，按公开类边界修正检查后无缺失，不据误报改动代码。

## 结果、决定与限制

- 单元 4：[公开契约](../../contracts/distributions.md)、[实现与验证](2026-09-30-unit-4-results.md)。D4-1 允许零维和退化分量，禁止非有限参数，无采样 API。
- 单元 5：[公开契约](../../contracts/generation.md)、[实现与验证](2026-09-30-unit-5-results.md)。D5-1–3 保留 YAML，统一有序 binding、完整初始覆盖、命名中心消歧及任务字段。越限分布参数可以表示，不假装状态有效。
- 单元 6：[公开契约](../../contracts/input-bundle.md)、[实现与验证](2026-09-30-unit-6-results.md)。D6-1–4 通过公开资源快照组织共享资源，严格发现与关联，完成样例最小迁移及既有验收预期适配。
- 共享入口更新 README、docs/README、docs/design、docker/README；历史候选与过程保留，原 AGENTS.md 未改。研究记录仓库、tools 原型、模型和物理参数未改。
- 无范围内未完成实现或已知失败测试。最终设计是否接受仍由用户决定；采样、限位外状态处理、场景复制、运动学／碰撞／可达性／规划和数据集输出均未实现或验收。名义 Scene 仍有公开可变能力，本轮保证 reader 不修改它，不提供深冻结或并发文件替换保护。

## 用量与计时

- 实际额度重置次数：**0 / 1**。未调用重置操作；如需要唯一重置，先报告并请用户在产品中执行。
- 起始账户 codex 周窗口 usedPercent=41（约剩 59%），来源 get_usage_limits；这是账户额度，不能换算本试验 token 消耗。
- 主 agent 与各阶段 token 输入／输出：工具未提供，**不可用**。阶段交替且无可靠活动计时的部分不估算，最终保留实际任务墙钟与测试工具时间，二者不重复累计。
- 主 agent 不代替单元实现；后续发现的实现缺陷返回对应 agent 修复。
- 过程账户快照为 usedPercent=41、45、48；最后快照约剩 52%，不据差额反推本任务用量。实际重置仍为 **0 / 1**。

| agent／阶段 | 可取得的时间记录 | token |
| --- | --- | --- |
| `/root/design_decisions` | 首轮设计 5 分 34 秒；追加 D6-4 17 秒，区间不重叠。详见决定记录 | 不可用 |
| `/root/unit4_distributions` | 实现 96 秒；测试 123 秒；收尾另记，非完整任务总时长 | 不可用 |
| `/root/resource_snapshots` | 混合准备 48 秒；实现修改 21 秒；测试 86 秒；起步与收尾未完整计时 | 不可用 |
| `/root/unit5_generation`（已停止） | 可识别准备区间 94 秒；无实现代码／测试；不并入新 U5 的计时 | 不可用 |
| `/root/unit5_generation_clean` | 首个工具点至最终验证 9 分 14 秒；明确实现片段 242 秒及修正 16 秒，完整实现／测试分项不可用 | 不可用 |
| `/root/unit6_bundles` | 实现区间 2 分 55 秒；测试为主的混合区间 5 分 28 秒；收尾记录 1 分 26 秒；净分项不可用 | 不可用 |
| `/root` | 协调、材料阅读、独立集成测试编写、运行、局部审阅及记录交替；完整实现／测试分项不可用；未写单元实现 | 不可用 |

整轮开始 12:58:08 UTC，到最终记录检查点 13:28:36 UTC 的并行墙钟为 **30 分 28 秒**，包含协调、等待 agent、测试和记录，不包含随后保存提交的工具往返。累计 agent 时间另列：由于多个 agent 缺少完整起步／收尾与活动细分，**完整累计 agent 总时间不可用**；不将上述部分区间拼成完整总量，也不将子任务时间加到整轮墙钟。测试工具秒数仅为执行子集，不是开发阶段耗时。没有等待用户或执行额度重置。

## 本地交付状态

分支 `codex/autonomous-units-4-6`，基点保持 `aa98559ecec51559dbcd2ce24e8853cf61263ffa`。完成项按阶段保存为英文提交；最终提交包含包实现、集成验收、样例元数据、共享入口和本记录。提交前检查差异及暂存范围；未改写既有提交，未合并 main，未推送。最终提交后的工作区检查结果由主 agent 在交付消息报告，以免通过再次修改本文件制造新的未提交差异。
