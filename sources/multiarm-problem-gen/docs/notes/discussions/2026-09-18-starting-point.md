# 仓库起点

日期：2026-09-18

## 背景

用户决定将原 `data_gen` 文件夹改名为 `multiarm-problem-gen`，初始化 Git 并写入初始内容。检查时目录内仅有 `MotionBenchMaker.pdf`，没有 Git 仓库。论文保留在本地根目录，按用户要求不提交至 Git；仓库仅保留[原文引用](https://arxiv.org/abs/2112.06402)。

初始文档来自此前数据格式和协作讨论；尚未选择实现语言或后端，也没有实现代码与可运行测试。

## 本次组织选择

README 提供项目入口，AGENTS 保存必要协作约定，`docs/design.md` 维护当前设计，`docs/notes/` 保存过程。暂不建立完整模块体系，也不引入自主执行循环或多 agent 流程。

`src/`、`tests/`、`examples/` 作为后续内容的位置，初始不写占位实现；Git 不跟踪空目录。代码相关设计以后在本仓库维护，研究记录仓库中已有方案保留为讨论快照。

## 学习与协作目标

用户希望参与架构选择、理解和管理复杂度，同时积累可迁移的协作经验。草稿允许包含问题、例子、反例和候选抽象；通过小实验和实际使用反馈逐渐形成设计。

best practice 提供倾向，不成为形式上的枷锁。共同语义需要明确，工程偏好可以调整。后续可结合具体问题记录合作方式、实际观察、代价及适用条件，不急于把单次经验变成通用规则。

## 前序材料

以下为同一设备上相邻研究记录仓库的相对链接；它们用于追溯，不是构建依赖。单独克隆本仓库时不保证存在：

- [数据组织与格式方案](../../../../research-process/inbox/2026-09-18-generator-input-output-format.md)
- [渐进设计与 best practice 原则](../../../../research-process/inbox/2026-09-18-evolving-design-and-best-practices.md)
- [agent 协作目标与调研](../../../../research-process/inbox/2026-09-18-agent-collaborative-development-research.md)

## 下一步

继续讨论机械臂配置与第一个具体使用场景，据此选择一个小实现或原型。当前不把候选抽象当作正式接口，也不将整体功能实现视为已经开始或完成。
