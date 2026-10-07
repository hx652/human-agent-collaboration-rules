# 与 agent 合作开发：目标、调研与候选起点

日期：2026-09-18

状态：按用户要求整理两轮调研与讨论。用户目标和此前确认的原则与 agent 的研究判断分开记录；候选流程尚未整体确认为执行规范。本记录不是项目已实施成果。

## 1. 用户希望通过这个项目获得什么

用户报告代码库目前还是空的，希望利用数据生成器项目从起点探索“与 agent 合作开发”的经验和 best practice。

用户的原始目标：

> 1. 做好过程的记录，设计代码本质上是一个选择的问题，不一定有标准答案，所以做好记录就很重要
> 2. 我希望参与整个项目架构的设计，与agent讨论，让我能理解和管理complexity，避免整个项目一团乱麻，提升我的工程能力
> 3. 这个项目是尝试的过程，最终积累的经验和方法我希望能在更多项目使用，所以一开始就要有所设计。

因此，项目不仅需要推进软件实现，也需要支持用户形成理解、参与判断，并积累可以在其他项目继续检验的协作方法。最大化代码产出或自动化程度，不是唯一目标。

此前已经确认的原则见[渐进形成设计，以及如何使用 best practice](2026-09-18-evolving-design-and-best-practices.md)：草稿纸容纳例子、反例、候选抽象和小实验；best practice 提供默认倾向，同时保留表达与探索空间。

## 2. 调研范围与证据边界

第一轮关注受控研究、官方指导、Git 文档及公开仓库；第二轮按用户要求，从 Matt Pocock 的内容出发，扩展至个人博客、一手访谈、Reddit 和 Hacker News 讨论，并比较 AI 普及前后的工程实践。

- 受控研究提供特定任务和工具条件下的证据，不直接证明长期协作效果。
- 作者博客与技能文件用于理解具体方法，不将作者经验视为普遍定律。
- 论坛讨论用于发现摩擦、反例和不同使用情境，不用帖子数量或自报效率证明方法有效。
- 读取外部技能是调研，不代表安装或执行其中的指令。

当前没有充分证据证明某一种流程最适合“从空仓库开始，同时学习架构”的长期个人项目。以下建议是可试验的起点。

## 3. 第一轮研究带来的提醒

### 完成功能不等于形成理解

Anthropic 的研究让 52 名主要为初级工程师的参与者学习陌生 Python 库。AI 组即时测验平均为 50%，对照组为 67%；任务完成时间差异不显著。主动追问概念、检查理解的交互模式与较好测验表现相关，但该分析不是交互方式的因果实验，也不能回答长期能力变化。

对本项目的启发是：除了代码是否运行，还应关注用户能否解释关键选择、定位修改位置和理解错误原因。[研究原文](https://www.anthropic.com/research/AI-assistance-coding-skills)

### 感觉更快不等于实际效果更好

METR 的早期实验在熟悉成熟仓库的开发者和当时工具上发现任务耗时增加；后续研究又受到参与者、任务选择和计时方式的影响。不能把早期结论当成当前所有项目的规律，也不能仅凭流畅感评价合作效果。[2025 年实验](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)、[2026 年方法更新](https://metr.org/blog/2026-02-24-uplift-update/)

### 更多说明文件不必然更好

《Evaluating AGENTS.md》2026 年修订版中，自动生成上下文文件没有显著提高问题解决率，但增加了成本。研究主要覆盖 Python 问题解决，不足以推断所有文档、工具或学习情境。

应保留具体、有用的协作约定，避免自动堆积仓库概述和大量要求；这不是“AGENTS.md 无用”的结论。[论文 v2](https://arxiv.org/html/2602.11988v2)

## 4. Matt Pocock 的实践及适用边界

调研读取了其 workshop、技能源码及实际项目中的领域说明。Workshop 介绍了需求澄清、PRD、纵向任务和人在场或自主执行的路线；当前技能仓库则强调小型、可修改、可组合的技能，而不是一个框架接管所有过程。[Workshop](https://www.aihero.dev/ai-engineer-workshop-2026~dwnll)、[技能仓库](https://github.com/mattpocock/skills)

最值得借鉴的内容：

| 做法 | 对本项目的意义 |
|---|---|
| 共同语言 | 澄清名义场景、样本、目标 frame、访问、辅助 IK 等概念，减少误解扩散 |
| 深模块 | 从调用者需要知道多少事来判断接口，而不只看函数或文件大小 |
| 纵向小步 | 尽早贯通一条可运行、可验证的使用路径 |
| 行为测试 | 预期结果来自独立依据，避免测试照抄实现 |

其领域建模技能区分词汇表、实现设计和草稿，建议有内容时才创建文件；其实际项目也有对应的 `CONTEXT.md`。[领域建模技能](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)、[固定版本的项目实例](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md)

agent 判断：以下规定不宜直接照搬。

- **把设计树全部问完才开始**：可能导致无限前置规划。更适合澄清影响下一步的问题，其他未知明确保留或用原型回答。
- **每个测试边界都要求人工确认**：重要语义值得共同讨论，已确定语义下的常规检查不必反复审批。
- **将某套技能编排当成传统实践的唯一解释**：例如其当前 TDD 技能把重构放在审阅阶段，与常见的 red—green—refactor 循环不同，应理解为作者的工作选择。

依据：[grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)、[TDD 技能](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)、[传统 TDD 说明](https://martinfowler.com/bliki/TestDrivenDevelopment.html)。在线技能会变化，这里记录的是本次读取时的内容。

## 5. pre-AI 工程经验仍然指导什么

| 传统经验 | 仍然有效的目的 | agent 带来的变化 |
|---|---|---|
| 共同语言与领域建模 | 让名称、概念和理解一致 | 概念误解可能更快扩散为大量代码 |
| 高内聚、低耦合、隐藏细节 | 限制一次变化的影响范围 | 也影响 agent 完成任务所需的上下文 |
| 小步交付与反馈 | 尽早暴露错误假设 | 任务大小应受可理解、可验证范围限制 |
| 测试与重构 | 保护行为并改善结构 | 编写成本下降，低价值测试也更易膨胀 |
| DRY | 避免同一知识有矛盾的权威版本 | 文档、提示词、配置、技能也会重复知识 |
| 原型 | 低成本回答未知问题 | 更容易比较方案，也更容易让原型混入正式代码 |
| Git 与审阅 | 比较变化、保留恢复起点 | 理解和审阅速度可能跟不上代码产出 |
| 决定记录 | 保留理由及重新考虑的条件 | 同时服务跨 session 交接 |

### DRY 针对知识，不是机械消除相似代码

Hunt 和 Thomas 的原始访谈强调同一知识的权威表示，并讨论文档、构建配置和生成器中的重复。探索阶段的两个候选实现可以暂时相似；更应避免多份手工维护的格式规范彼此矛盾。[原始访谈](https://www.artima.com/articles/orthogonality-and-the-dry-principle)

### 区分原型和可保留的小实现

Tracer bullet 是贯通很薄的使用路径并持续生长；prototype 用于回答特定未知，通常不准备长期保留。[原作者访谈](https://www.artima.com/articles/tracer-bullets-and-prototypes)

例如，“比较两个 IK 库能否表达同一个 TCP”适合原型；“读入最小场景，生成目标并保存”适合可逐步扩展的小实现。这是 agent 提出的例子，不是已安排的任务。

### 抽象需要在具体情境中反复修正

Fowler、Rebecca Parsons 和 Unmesh Joshi 的讨论强调，从具体情境出发，在“要什么”和“怎样表示及实现”之间往返形成抽象。不能只让 agent 满足一个例子，也不能要求它先给出完整架构。[原始讨论](https://martinfowler.com/articles/convo-what-how.html)

## 6. 理解和管理 complexity 的候选方法

agent 建议用以下问题审阅候选抽象：

1. 它替调用者消除了什么重复理解？
2. 它隐藏的是实现细节，还是调用者必须知道的语义？
3. 修改一个规则，需要改多少不相关位置？
4. 删除这个抽象，会让系统更简单，还是把复杂度散回调用方？

深模块并不等于把整个系统包装成一个巨大入口；内部仍需能定位、解释和修改。也不以函数数量或代码行数直接判断设计质量。[Matt 的设计技能](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)

用户可以通过真实数据路径理解实现：输入经过哪些概念和模块，在哪里转换，在哪里生成结果。讲解应依据实际代码，而不是脱离代码编造叙述。重要模块也可以通过“明天增加一种变化，要改哪里”来讨论可修改性。[Linear walkthroughs 实践](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)

用户的学习目标意味着，某些实现和调试细节值得共同参与，不能全部当成应被自动化消除的成本。Kief Morris 关于由人设计和管理反馈循环的建议有启发，但不能完全替代这里的学习目标。[Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)

## 7. 论坛讨论暴露的摩擦

- 使用者报告结构化提问帮助发现需求缺口；但帖子同时提出的固定上下文长度阈值没有充分依据，不能一并采信。[Reddit 经验帖](https://www.reddit.com/r/vibecoding/comments/1v0zm6n/switched_my_ai_coding_workflow_after_watching/)
- 有人报告多轮测试审查和实现审查使小任务耗时很长；评论指出测试可能与实现耦合，形成另一份代码。这是流程成本的线索，不证明 TDD 或审阅无效。[Reddit 讨论](https://www.reddit.com/r/vibecoding/comments/1t2tkvw/am_i_overengineering_matt_pococks_ai_coding/)
- Hacker News 中同时存在积极委托与偏好小步配对工作的经验。项目熟悉程度、遗留复杂度、反馈条件和参与方式不同，不能归结为简单的“agent 有效或无效”。[实践交流](https://news.ycombinator.com/item?id=46292682)
- 有讨论指出，代码产出可以加速，而共同理解的形成未必同比加速。这是经验判断，对本项目的提醒是避免代码增长长期超过用户建立理解的速度。[讨论](https://news.ycombinator.com/item?id=46930565)

## 8. Git 的候选使用方式

倾向采用主分支加按问题组织的主题分支，暂不引入复杂的分支层级。

- 开始工作检查分支和已有差异，避免混入或覆盖无关工作。
- 分支围绕问题或试验，不必对应一次聊天。
- 提交围绕可解释的逻辑变化，不对应每次工具调用；探索中可保留检查点。
- 比较备选方案或并行修改时按需使用 worktree，注意它不隔离共享输出目录等外部资源。
- 合并后重新检查组合行为；没有文本冲突不等于没有语义冲突。
- 提交前检查实际暂存差异，说明验证与未决事项。
- 推送、合并及改写共享历史遵循明确授权，不因 agent 熟悉命令而放松判断。

Git 官方的逻辑提交和 worktree 用法可作为依据，但不要求提交越碎越好，也不要求每个小修改都提 PR。[提交建议](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)、[worktree](https://git-scm.com/docs/git-worktree)

Git 不是万能恢复机制：未保存进 Git 的内容并不都能找回，reflog 也不是永久备份。[撤销说明](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things)

代码历史与讨论记录互补：提交记录代码如何变化，笔记保留有学习价值的尝试和选择理由，当前设计说明表达现在采用什么。不要求所有失败尝试永久进入主分支，也不为了整理历史而丢掉重要过程。

## 9. 项目组织与信息记录的候选起点

先明确内容用途，不要求一开始创建所有文件。

| 内容 | 用途 |
|---|---|
| README | 项目用途和最小运行入口 |
| AGENTS | 必要协作规则、工作入口和文档导航 |
| 领域说明 | 术语及概念关系 |
| 当前设计说明 | 已实现的模块责任、数据流及重要约束 |
| 讨论笔记 | 问题、例子、反例、尝试和暂时方案 |
| 决定记录 | 重要取舍、理由、适用条件和替代关系 |

一种候选形式是 `docs/README.md`、`docs/design.md`、`docs/notes/`、`docs/decisions/`。领域说明初期可以只是设计文档中的一节，内容多了再拆。少量可运行 examples 和针对行为的 tests 逐步加入。

普通笔记不必强制套模板，能够说明问题、选择、依据和未决事项即可。重要取舍再提炼成短 ADR；不是每次命名和局部修改都写决定记录。[ADR 原始提议](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)、[Rust 对重要变化与普通修改的区分](https://github.com/rust-lang/rfcs/blob/master/README.md)

AGENTS 保持实用，不装入全部历史。Ruff 仓库的具体测试入口、环境限制和快照审阅要求，是实际例子；不需要照搬其整套规则。[Ruff 文件](https://github.com/astral-sh/ruff/blob/main/AGENTS.md)

草稿和历史记录是上下文，不自动成为执行指令。领域词汇也允许纠正，不能一旦命名就冻结概念。

代码版本相关记录放代码仓库；跨项目认识与协作经验放 `research-process`，通过链接关联，避免重复维护同一份方案。

## 10. 怎样积累可迁移的经验

agent 建议一开始设计记录方式，但不一开始宣称得到通用 best practice。

候选积累路径：

```text
具体问题 → 尝试一种合作方式 → 记录观察和代价
        → 在其他情境中再试 → 提炼为可复用方法
```

值得记录时，可简短保留：当时的问题、采用的合作方式、实际观察、代价、当前判断和适用条件。不要只留下脱离情境的口号。

不要求每个 session 都写实验报告。合作方式发生变化、出现意外或某种做法被重复验证时，记录更有价值。

同时观察：

- 软件功能是否推进；
- 用户是否更能解释关键选择、定位和修改代码；
- 误解、审阅、返工和恢复上下文的成本；
- 记录和流程本身是否开始造成负担。

不是以代码行数、技能数量、agent 数量或自动化程度评价合作效果。

## 11. 当前综合判断与未决事项

agent 的综合判断：pre-AI 工程经验并未失效，变化主要在成本与反馈速度。生成、试验和文档更便宜了，但判断什么值得保留、形成共同理解、维持清晰边界，仍需有意识地投入。

候选起点是：少量共同语言、按问题的小步工作、重要选择共同讨论、明确实现交给 agent，并在若干增量后同时回看软件和协作方式。当前不建议整体引入自主执行循环、多 agent 编排或完整流程平台；这是建议，不是已经采用的规则。

后续仍需讨论：

- 哪些设计变化应在实施前共同讨论；
- 用户希望在哪些部分深入阅读实现或参与调试；
- 第一项小工作选择什么；
- 文档和 Git 工作流的具体组织与授权；
- 何时复盘，怎样判断某种方法值得保留或删除。

## 相关本地记录

- [已确认的设计与 best practice 原则](2026-09-18-evolving-design-and-best-practices.md)
- [数据生成器方案](2026-09-18-generator-input-output-format.md)
- [项目入口](../projects/dataset-generator/README.md)
