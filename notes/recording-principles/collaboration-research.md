# 跨 Session 和多个 agent 协作的补充调研

调研日期：2026-10-11。两位 subagent 分别调查跨 Session 接续、多 agent 协作，主 agent 复核入选原始来源后整理。本文提供讨论依据，不是新的协作规则。

## 问题与范围

用户明确指出，跨 Session 延续和多个 agent 协作是形成记录后的好处。记录是达成这些目的的重要手段，但还希望了解社区采用的其他手段及其成功经验。

这里沿用本次讨论中“记录”的含义：人和 agent 可阅读的想法、过程、设计和经验文档。其他机制也可能保存信息；区别主要在承担的功能，而非是否使用文本文件。

需要区分中断的运行继续执行、新会话理解历史工作，以及多个 agent 相互配合。恢复步骤和工作产物，有助于继续行动，但不自动恢复当初的背景与判断。

## 跨 Session 接续的其他手段

### 持久保存运行状态

Grid Dynamics 为制造业客户开发研究助手时，遇到人工等待后的恢复和状态维护困难。迁入 Temporal 后，团队报告可以从长暂停接续，并删除大量自制重试逻辑。恢复依靠执行状态持久化；代价是重构步骤及其依赖。这是实施者发表于厂商网站的经验，无独立对照，不能据此判断所有框架的优劣。[Grid Dynamics，2025-09-29，State management transformation 与 Architectural decoupling](https://temporal.io/blog/prototype-to-prod-ready-agentic-ai-grid-dynamics)

社区也报告过恢复时重复执行已完成步骤的问题，并提供跨进程复测。它说明需要核实恢复语义，不能只看最后结果是否一致。本轮未自行复现，也不将个案泛化为全部版本的行为。[LangGraph #6792，2026-02-12 原帖及 2026-09-06 复测评论](https://github.com/langchain-ai/langgraph/issues/6792)

### 保存和恢复实际工作现场

Replit 将代码、文件系统和数据库共同纳入检查点，维护者还观察到 agent 利用历史恢复被重构掉的代码。这能减少按文字重建现场的负担，但未保存的讨论理由仍无法由快照直接恢复。原文的并行模拟部分属于未来方向，不计入成功证据。[Replit，2025-12-18，Versioning Agent Code Changes 与 Forkable Databases](https://frontier.replit.com/inside-replits-snapshot-engine/)

### 将部分经验转为可执行检查与按需上下文

一项十二周的工程案例将部分 agent 审查逐步转成静态、动态检查，并根据任务位置提供相关约束。这让后续工作可以复用已建立的检查和资料，分担反复提醒与核验。该研究由资深工程研究者主导，属于单项目预印本；检查通过但内容含义受损的案例也说明，其覆盖有限，不能代替人对目标和结果的判断。[Cheap Code, Costly Judgment，2026-07-04 版本，第 IV-B、V-B、VIII 节](https://arxiv.org/html/2607.01087v2)

## 多个 agent 协作的其他手段

### 明确责任归属与反馈路径

Cursor 的实验最初依靠共享文件自行领取任务，遇到锁争用和无人承担整体任务的问题；后来采用分层负责、明确任务范围及返回反馈的机制。系统可以持续运行，但产物仍是研究项目。这里的经验涉及调度和责任划分，不能用吞吐量代替质量，也不证明该组织方式适用所有任务。[Cursor，2026-02-05，Self-coordination 与 The final system design](https://cursor.com/blog/self-driving-codebases)

### 隔离工作并通过验证整合成果

Anthropic 的编译器实验采用独立容器、仓库副本和任务领取机制。多个 agent 曾反复撞上同一故障；作者引入 GCC 对照，将问题切成可独立验证的部分后才恢复并行推进。成果能构建 Linux 内核，但仍有局限。案例说明隔离、任务可分解性与外部验证共同发挥作用，不能单独归功于增加 agent。[Anthropic，2026-02-05，Running Claude in parallel、Make parallelism easy 与 Evaluation](https://www.anthropic.com/engineering/building-c-compiler)

### 主动咨询与独立审查

Cognition 的产品经验包括一位 agent 实现、另一位独立审查，再由实现者结合整体需求处理反馈；也尝试让 agent 主动向另一模型咨询。前者受益于独立上下文，后者可能需要充分共享背景，说明信息范围应按职责决定。作者同时报告，主 agent 不会判断何时求助会限制效果。这些是厂商自述，不构成通用最优方案。[Cognition，2026-04-22，Code-Review-Loop 与 Smart Friend](https://cognition.com/blog/multi-agents-working)

## 成功经验的适用边界

受控基准研究发现，可分解任务能从多 agent 协作中获益，而某些严格顺序依赖的任务反而退化。它支持考察任务依赖与协调成本，但不直接证明长期真实项目的效果，也不能据此规定所有项目的 agent 数量或组织形式。[Towards a Science of Scaling Agent Systems，2026-04-08 版本，第 4.2、5 节](https://arxiv.org/html/2512.08296v3)

科研领域另有一百一十五天的单研究者自观察，将会话、文件、工具、脚本和定时流程组合成持续工作环境，覆盖研究与教学工作。它证明该组合被持续使用，尚未证明节省人力或某项机制独立有效，也未提供经核实的完整恢复演练。[Persistent AI Agents in Academic Research，2026-05-26，第 2、4、6 节及附录](https://arxiv.org/html/2605.26870v1)

这批资料中，软件工程案例较具体，开放讨论与学习场景的直接证据仍较少。工程案例通常依赖可运行产物、明确测试或人的持续判断；不能把这些条件下的成功直接迁移为开放探索的统一流程。

## 对记录作用的理解

本轮调研形成的理解是：可读记录保留问题、讨论、理由和认识变化；运行状态与快照帮助恢复现场；分工、任务协调和通信组织当下协作；隔离和验证帮助检查、整合结果。它们解决不同困难，可以相互补充。

即使其他机制能减少状态复述和重复检查，也不能自动补回从未表达出来的背景或理由。反过来，写下了这些内容，也不等于任务已经被协调、环境已经恢复或结果已经验证。这一功能区分用于理解现有案例，尚未形成仓库规则。

## 检索与核验

主要检索词为 durable execution human-in-the-loop production、Replit snapshot engine、agent resume repeated tasks、persistent agents academic research、scaling autonomous coding coordination、building C compiler parallel agents、multi-agents actually working。

优先保留有具体实施、机制调整或失败过程的一手来源；功能存在、产物规模和持续使用时间均不单独作为协作成功证明。上述页面均已打开核验，未复现实验或审计实际部署。该轮是定向补充调研，不是系统综述。
