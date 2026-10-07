# 设计与记录入口

## 当前阶段

已实现 Compose 环境及单元 1–3；本试验分支进一步实现单元 4 分布参数、单元 5 Generation、单元 6 InputBundle，贯通名义输入读取。单元 4–6 的关键选择由独立决策 agent 作出，是探索性结果，不代表用户接受最终设计。没有采样、具体场景生成或计算后端。

- [基础表示公开契约](contracts/primitives.md)：构造接口、字段语义、校验与可变性。
- [资源公开契约](contracts/resources.md)：包内路径解析、错误信息及 mesh、RobotModel、名义 Scene 的自动取得与共享。
- [机器人公开契约](contracts/robot-model.md)：统一 RobotModel、读取入口、缺失默认含义及校验范围。
- [场景公开契约](contracts/scene.md)：无前缀 frame、实例状态、规则引用、严格读取与 reader／context 职责。
- [分布公开契约](contracts/distributions.md)：独立多维均匀／高斯、零维、退化参数、维度和只读性。
- [Generation 公开契约](contracts/generation.md)：分量映射、命名中心、完整初始覆盖、序列与任务字段。
- [InputBundle 公开契约](contracts/input-bundle.md)：发现顺序、跨文件校验、公开资源快照和共享身份。
- [开发环境与运行命令](../docker/README.md)：固定版本、Compose 启动与验收入口。
- [当前设计](design.md)：已确认语义与未决选择。
- [Git 工作方式与提交信息](git-workflow.md)：探索分支、长期主线及英文提交约定。

## 讨论与方案

以下记录保留问题、备选方案、取舍和实施前方案；已确认的方案也不等于已经执行。

- [单元 4–6 自主决定](notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md)：信息包、备选、决定 D4-1／D5-1–3／D6-1–4、样例迁移与复议。严格隔离实现使用过滤后的单元 [5](notes/discussions/2026-09-30-unit-5-public-handoff.md)、[6](notes/discussions/2026-09-30-unit-6-public-handoff.md) 公开交接包。

- [读取后的领域表示讨论](notes/discussions/2026-09-22-input-domain-representations.md)：机器人、mesh、pose/frame 与场景形状的逐步取舍。
- [Generation 分布与作用关联](notes/discussions/2026-09-23-generation-distributions.md)：多维分布、分量映射及由目标属性确定的应用语义。
- [InputBundle 输入包方案](notes/discussions/2026-09-23-input-bundle.md)：共享资源、场景目录发现、命名与引用约定。
- [输入读取流程与对象协作](notes/discussions/2026-09-28-input-reading-flow.md)：从文件读取到 InputBundle 的运行步骤、职责与引用关系。
- [输入读取实现单元划分](notes/discussions/2026-09-29-input-implementation-units.md)：六个单元、依赖、资源管理边界与建议实现顺序。
- [单元 1：基础表示方案](notes/discussions/2026-09-29-unit-1-basic-representations.md)：数据类、Frame 位姿更新、校验边界与候选验收条件。
- [单元 2：机器人表示与读取方案](notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md)：合并后的 RobotModel、URDF 内容范围、缺失规则及资源接口。
- [单元 3：场景表示、读取与统一资源管理方案](notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md)：保留实施前方案；本轮结果见下方实施记录，手动添加接口及其规则仍留待后续讨论。
- [首轮实施方案：Compose 环境与基础表示](notes/discussions/2026-09-29-compose-and-unit-1-implementation.md)：环境组织、公开接口、执行顺序和验收入口。
- [实现单元与代码职责的区别](notes/discussions/2026-09-29-implementation-unit-and-responsibility.md)：任务交付范围、代码职责与契约隔离实验的区别。
- [输入输出方案](notes/discussions/2026-09-18-input-output-format.md)：完整方案、候选字段、样例和未决事项。
- [输出数据的有效性语义](notes/discussions/2026-09-21-output-validity-semantics.md)：联合初始状态、目标 IK 端点的保证及其边界。
- [首份输入样例](notes/discussions/2026-09-18-first-input-example.md)：UR7e、table＋mesh 的目标、原则与待讨论细节。
- [初始化记录](notes/discussions/2026-09-18-starting-point.md)：仓库建立时的背景、组织选择与协作目标。

## 实施过程与复盘

- [单元 4–6 自主试验总记录](notes/implementation/2026-09-30-autonomous-units-4-6-results.md)：集成验收、提交、agent 分工、用量、阅读边界与限制；分项见[单元 4](notes/implementation/2026-09-30-unit-4-results.md)、[资源快照](notes/implementation/2026-09-30-resource-snapshots-results.md)、[单元 5](notes/implementation/2026-09-30-unit-5-results.md)、[单元 6](notes/implementation/2026-09-30-unit-6-results.md)。[单元 5 准备停止记录](notes/implementation/2026-09-30-unit-5-preparation-stopped.md)保留一次阅读边界偏差，未隐去该过程。
- [首轮实现与验收记录](notes/implementation/2026-09-29-first-implementation-results.md)：Compose 环境与基础表示的完成范围、检查结果、阅读边界和限制。
- [单元 2 实现与验收记录](notes/implementation/2026-09-29-unit-2-implementation-results.md)：实际完成内容、真实输入验收、阅读边界及剩余限制。
- [暂时移除 Material](notes/implementation/2026-09-30-remove-material-support.md)：收缩外观支持范围、明确拒绝材质输入及回归结果。
- [单元 3 实现与验收记录](notes/implementation/2026-09-30-unit-3-implementation-results.md)：场景与统一资源管理、独立算例、真实输入验收、阅读边界与阶段统计。

## 样例与工具

- [UR7e 双臂桌面基准场景](../examples/ur7e_table/README.md)：独立输入包、分布和固定序列实例；有效性处理仍待讨论。
- [基准检查与历史结果](../tools/baseline_validation/ur7e_table/README.md)：布局依据、离散检查及验证边界。
- [模型准备](../tools/model_preparation/ur7e_2f85/README.md)：上游源材料和展开入口。

## 接下来讨论

- 评估自主试验的公开契约与分工是否值得接受；本分支结果尚未合并主线。
- 场景复制、随机采样、越界样本处理和实际生成仍未实现，不能将读取验收当作这些能力的验收。
- Python、YAML 与当前 URDF 读取已落实；计算后端依赖仍按后续实际需求讨论。

以上不是已排定的实现计划。先积累场景、问题和候选抽象，不要求一次决定完整架构。

## 怎样组织记录

`design.md` 用于理解现在采用什么；`notes/discussions/` 保存问题、备选方案、取舍和实施前方案，`notes/implementation/` 保存实际执行过程、验证结果、问题与复盘。按记录的主要目的分类，不按标题是否出现“实现”判断；讨论中的实际观察可以保留原文，并链接相关实施记录。

笔记按日期和主题命名，并保留当时的状态与上下文；方案落地后，通过链接关联实施记录，不将原方案改写成结果。重要决定增多后再建立 `decisions/`，保留被替代决定的理由及新记录链接。

每份笔记不必使用固定模板，但应让未来读者分清问题、依据、选择和未决事项。候选方案和历史记录不自动成为 agent 指令。

跨项目的协作方法继续在 `research-process` 中整理，本仓库记录具体代码情境和证据。
