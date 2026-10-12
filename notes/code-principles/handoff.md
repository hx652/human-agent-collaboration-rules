# 代码原则讨论成果交接

本轮交付按主题重组的候选规则稿、专项草稿、讨论原文及独立审查依据。正式规则和仓库 README 尚未改写；审查通过和本地提交不代表全部候选条文已经被采用。

## 交付内容

- [完整候选稿](topic-reorganization-draft.md)：五个主体主题及工具、记录两项配套主题，包含本轮对信息隔离、架构审查和问题追踪的修改。
- [重组方案](topic-reorganization-plan.md)：主题依据、原有条文去向、补充内容及拟修改范围。
- [上下文划分草稿](context-isolation-draft.md)和[问题追踪与修复草稿](problem-tracing-and-fix-draft.md)：相应主题的集中表述。完整候选稿通过主题归并承载这些含义。
- [讨论记录](README.md)、[原始对话摘录](review/source-dialogue.md)、[独立审查报告](review/independent-review.md)和[意见处理记录](review/resolution.md)：保留原意、确认状态及核查依据。

## 已明确的方向与采用边界

原始对话 U04、U09 明确要求按信息隔离安排上下文，边界可以细到类或方法，分工不能扩大可读取信息，也不机械地为每个函数创建实现者。

U09 对 A15 的两种视角解释评价为“基本没有问题”。U05、U10 要求按主题整理原则并提供预览；U06、U07、U11 要求将追踪与修复整理为原则，不变成固定操作步骤。U12、U13 要求架构审查和问题追踪直接表述为“使用全局视角”，不作为可选建议，也不刻意加上“必须”。

七个主题的完整组织、各专项草稿中的具体补充仍是待采用的候选表述。统一整合时应依据最终选定的采用范围更新正式规则，不能把本轮提交授权或独立审查结论当作对所有候选内容的逐项确认。正式采用后的链接位置和 README 简介调整见重组方案。

## 分支与依赖

工作目录：/home/fainic/.codex/worktrees/code-principles-discussion/human-agent-collaboration-rules。

主题分支：codex/code-principles-discussion。本轮新增内容均位于 notes/README.md 和 notes/code-principles/。

本分支起点为记录原则基础提交 410b9eee51b747be6d8b315e7c21f836d3384459，草稿引用的 rules/RECORDS.md 由该提交引入。记录主题后续的 190ad3c 和 3c2afb2 未包含在本分支中，应与该主题的交付一并考虑，保留其后续修订；本轮不通过复制旧规则覆盖其他主题成果。

本轮仅准备交接并执行本地提交，不合并、不推送，不删除分支或 worktree。最终提交号由交付答复提供。
