# Subagent 调研来源索引

访问日期：2026-10-12。下表为综合报告采用的主要一手来源；网页章节比抓取行号更适合后续定位。官方文档若无发布日期，明确记为未标；抓取日期不作为发布日期。主 agent 复核了关键主张，分工与方法见[调研安排](arrangement.md)。

## 官方机制与上下文模式

| 来源 | 日期 | 用途与定位 |
|---|---|---|
| [OpenAI Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 正文未标 | Why subagent workflows help、Triggering、Approvals and sandbox controls。核对隔离探索输出、触发和权限继承；属功能说明。 |
| [OpenAI Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents) | 正文未标 | Keep local context separate from model context。区分程序状态与模型实际输入。 |
| [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) | 正文未标 | 启动上下文、自动委派、conversation fork。由机制组打开核查；不同创建方式不能混同。 |
| [LangChain Organizing Context in a Multi-Agent Harness](https://www.langchain.com/blog/organizing-context-in-a-multi-agent-harness) | 2026-09-08 | Context modes、Choosing a context mode。为新上下文与 fork 提供当前设计说明；非效果实验。 |

## 工程经验与社区讨论

| 来源 | 日期 | 证据性质与定位 |
|---|---|---|
| [Anthropic How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | 2025-06-13 | 作者复盘与内部评测。Benefits、Prompt engineering 第 2、3 项及附录产物回传。具体评测任务与成本比较的基线不同。 |
| [LangChain Benchmarking Multi-Agent Architectures](https://www.langchain.com/blog/benchmarking-multi-agent-architectures) | 2025-06-10 | 同模型架构实验。Data、Experiments、Results、Improvements、Future work；无关域任务不等同于跨领域协作。 |
| [Cursor Scaling long-running autonomous coding](https://cursor.com/blog/scaling-agents) | 2026-01-14 | 作者工程实验。协调失败、planner/worker 分工、运行与经验段；没有等预算架构消融，产物仍有验收限制。 |
| [Cognition Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working) | 2026-04-22 | 作者实践更新。Code-Review-Loop、Smart Friend、What Actually Happened。审查与咨询采用不同上下文策略；对注意力或偏差的解释是作者观点。 |
| [deepagents issue #2512](https://github.com/langchain-ai/deepagents/issues/2512) | 2026-04-07 起 | 用户用例及维护者机制确认。重点看 mdrxy 的 06-05 评论和 hntrl 的 08-12 评论；区分文本摘要与完整非文本产物。 |
| [Claude Code issue #40339](https://github.com/anthropics/claude-code/issues/40339) | 2026-03-28 起 | 用户报告。作者说明证据尚不完整；05-07 因不活跃关闭。不能将评论附和当复现，也不能将关闭当修复。 |

## 研究证据

| 来源 | 采用版本 | 证据用途与限制 |
|---|---|---|
| [NoLiMa](https://arxiv.org/html/2502.05167v3) | v3，2025-07-09 | §3.1、§4.1–4.4、Table 3。长上下文关联检索实验，不能直接推出分工策略。 |
| [Debate or Vote](https://arxiv.org/html/2508.17536v2) | v2，2025-10-23 | §2–3、Table 1、Appendix A.1/H。同模型独立投票与交流对照；理论结论依赖假设，任务主要是答题。 |
| [When Debate Helps](https://arxiv.org/html/2610.04686v1) | v1，2026-10-03 | §4–5、Tables 1–2、Appendix A/C。互补候选与核验交流；新近预印本，尚未核验独立复现。 |
| [Towards a Science of Scaling Agent Systems](https://arxiv.org/html/2512.08296v3) | v3，2026-04-08 | §4–5、Appendix E/F。260 配置、六基准；新增软件任务样本有限，未单独随机比较上下文继承。 |
| [Kimi K2.5](https://arxiv.org/html/2602.02276v2) | v2，2026-08-07 | §3、§5.2、Table 6。训练后动态委派；关键路径约束不等于相同总 token 预算。 |

## 核验中处理的重要差别

- Anthropic 的 90.2% 属系统内部评测比较；15 倍 token 相对聊天。两者不能拼成同题、同模型的效率结论。
- Cognition 2025 年的 [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) 是历史设计主张。本报告同时查看 2026 年更新，不把旧文当成作者当前全部立场。
- Scaling v3 的样本和回归结果已修订。本报告采用 v3；17.2×/4.4×是轨迹级错误放大指标，不是失败概率倍数；87% 是评估框架的架构选择结果，不是通用 agent 自主决策准确率。
- 论文的正文由证据组核对。主 agent 另核对主要论文的版本、摘要及主结论；没有把逐项复现实验或对所有附录的独立复核记成已完成。
