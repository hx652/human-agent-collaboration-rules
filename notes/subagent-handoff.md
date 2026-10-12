# Subagent 原则讨论成果交接

日期：2026-10-12。状态：独立审查、修复、复核及文稿验证已完成，供统一整合会话使用。

本分支整理 Subagent 使用原则的讨论稿及依据，供统一整合会话使用。正式规则 `rules/RULES.md` 尚未修改；本地提交保存本轮成果，不表示已经合并或采纳为统一规则。

## 工作位置与基线

- Worktree：`/home/fainic/.codex/worktrees/subagent-principles/human-agent-collaboration-rules`
- 分支：`codex/subagent-principles`
- 起点：`f36dc73ade86699d959da4f08b74b9703cd3ae21`，创建分支时的 `main`。
- 本轮成果不依赖 `codex/recording-principles` 或 `codex/code-principles-discussion` 的未合入内容。

## 交付内容

- [原则草稿](subagent-principles-draft.md)：积极使用、自主安排、上下文与任务引导、新建和复用、模型与推理强度选择、向用户说明安排，以及不同视角的整合。
- [讨论记录](2026-10-12-subagent-principles.md)：保留用户原话、后续澄清与草稿变化，区分用户理解、agent 提议和当前文字。
- [调研报告](subagent-research/README.md)、[来源索引](subagent-research/sources.md)和[调研安排](subagent-research/arrangement.md)：保留实践依据、证据层次、研究范围和限制。
- [原始对话摘录](subagent-review/original-messages.md)、[来源与版本](subagent-review/provenance.json)、[独立初审](subagent-review/review.md)、[修订复核](subagent-review/recheck.md)，以及触发用户后续澄清的[前次 Astra 审查](subagent-review/prior-astra-review.md)和[当时草稿](subagent-principles-astra-reviewed.md)。原始摘录仅包含本轮用户自然语言消息与相关 agent 最终回复，不收录工具轨迹或其他会话。

## 交接边界

原稿中面向 subagent 的任务知识与引导已按用户确认并入上下文安排，新建和复用时的判断另起自然段。用户此前关于 agent 自主委派的理解与这段执行任务的引导是不同层次，不能将此前审查中的讨论点再当作待修复遗漏。

统一整合时，应结合最新主线和其他原则分支处理正式规则位置与共同约定；本分支未改变通用的信息隔离边界。各分支可能同时增加 `notes/README.md` 导航项，合并时需保留各主题入口。

尚未执行正式规则整合、跨分支合并、推送或清理分支/worktree。它们不属于本次交付操作。

## 审查与验证

初审及复核由同一位 `gpt-6.1-sol / max`、`fork_turns=none` 审查者完成，直接对照原始用户表述和既有约定。初审未发现原则正文的实质问题；两项记录问题已据原文修正，并经复核关闭：补回前次审查节点，为用户原话提供来源定位。没有新增原意或范围取舍需要用户确认。

审查者没有继承主会话历史，但平台仍自动附带通用指令和记忆摘要；该限制在审查报告中保留，不将本次描述为严格零背景审查。初审报告的定位与哈希对应初审输入，复核报告说明了修订后的状态；历史意见不被改写成新的结论。

原始摘录共 15 条用户消息和 10 条 agent 最终回复，已逐条与 session 原始记录核对；最终讨论记录中的 13 个用户引用块均能在原文中找到。当前导航链接、文本格式和本轮变更范围检查通过；原则草稿、调研正文及来源索引保持已审版本，正式规则与分支基线一致。没有运行代码测试或复现实验。

## 提交组织

本轮按一个工作目的保存为一次本地提交，范围为草稿、讨论和调研依据、必要的原始摘录与审查记录，以及本交接说明，共 13 个文件。提交信息为 `Add researched Subagent principles discussion`。最终提交号由 Git 历史和交付回复提供，文档不预填自身提交哈希。
