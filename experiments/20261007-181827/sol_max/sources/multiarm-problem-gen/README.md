# multiarm-problem-gen

多机械臂运动规划问题生成器。

以名义场景和生成规则为输入，生成包含具体场景、目标 frame、机械臂初始状态和访问序列的数据。

## 从哪里开始

- [当前设计草稿](docs/design.md)：已确认的数据语义、候选抽象和未决事项。
- [讨论与文档入口](docs/README.md)：当前问题及过程记录。
- [协作约定](AGENTS.md)：人与 agent 的工作方式。
- [MotionBenchMaker: A Tool to Generate and Benchmark Motion Planning Datasets](https://arxiv.org/abs/2112.06402)：参考论文，原文不纳入本仓库。

## 仓库组织

```text
docs/       当前设计、讨论和决定的入口
src/        实现代码，内部结构按实际需要形成
tests/      行为测试与小型测试数据
examples/   最小可运行输入与使用例子
```

`examples/ur7e_table/` 提供含 `bundle.yaml` 的独立输入包；模型准备、数值检查和预览原型分别位于 `tools/` 下。`src/multiarm_problem_gen/` 已实现基础表示、统一资源管理、机器人与场景读取；本试验分支增加分布参数、Generation 和 InputBundle 读取，交付关联完整的名义输入。它不采样、不生成具体场景、不执行运动学、碰撞或规划。

开发、完整验收及读取示例见 [Docker／Compose 环境](docker/README.md)。公开接口与行为见[基础表示](docs/contracts/primitives.md)、[资源管理](docs/contracts/resources.md)、[机器人模型](docs/contracts/robot-model.md)、[场景](docs/contracts/scene.md)、[分布](docs/contracts/distributions.md)、[Generation](docs/contracts/generation.md)和[InputBundle](docs/contracts/input-bundle.md)契约。单元 4–6 是授权的自主探索，agent 决定不代表用户接受最终设计；[试验记录](docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md)保存实际验证、隔离边界与限制。

代码仓库与生成的数据集不是同一种结构。输出数据集中的 `resources/`、`inputs/`、`samples/` 不直接决定本仓库的代码目录；大型生成数据和日志放在仓库外，小型例子按需纳入版本管理。

## 设计与学习

本项目同时用于探索与 agent 合作开发。用户参与概念、架构和取舍讨论，agent 独立审阅意见并提供实现与验证支持。通过具体问题、例子、反例和小实验逐步形成设计，不要求一开始给出完整架构。

跨项目协作经验保存在独立的 `research-process` 记录仓库；本仓库维护与代码紧密相关的当前设计和过程，避免两处长期重复维护同一份实现文档。
