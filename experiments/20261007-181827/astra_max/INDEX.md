# 人与 agent 长期协作：原始材料索引

本轮仅收集原始文件并建立索引，没有制定统一规则，也没有将历史任务作为本轮指令执行。`sources/` 中每份文件均完整按字节复制，原有措辞、状态、链接及换行保留。索引中的说明属于本轮整理判断，不是对原文的改写。

## 来源与检索范围

采集日期：2026-10-07。仅检索以下两个仓库的**当前工作区**；使用包含隐藏、未跟踪和被忽略文件的清点与文本检索，未检索 Git 历史、其他 worktree 或外部网站，未运行来源脚本。Git 文件分类读取设置了 `GIT_OPTIONAL_LOCKS=0`。

| 来源根目录 | 当前普通文件 | Markdown | 完整收录 | 收录文件的 Git 分类 |
| --- | ---: | ---: | ---: | --- |
| `/home/fainic/data/research-process` | 53 | 33 | 20 | 19 未跟踪、1 被忽略 |
| `/home/fainic/data/multiarm-problem-gen` | 215 | 46 | 29 | 29 已跟踪 |
| 合计 | 268 | 79 | 49 | 29 已跟踪、19 未跟踪、1 被忽略 |

逐项来源为上述根目录加表中原相对路径，副本固定为 `sources/<仓库名>/<原相对路径>`。文件名链接均指向本组副本；[完整清单与初始 SHA-256](audit/workspace-inventory.json)、[逐文件筛选及来源元数据](audit/selection.json)、[覆盖与排除记录](audit/review-coverage.json)、[最终一致性与路径检查](audit/verification.json)用于复核。

## 状态如何阅读

- **已确认**：原文明确记载用户确认、审阅认可或已采用；只按该段原有范围理解。
- **现载约定**：来源文件以协作约定或工作入口方式发布。未看到每条确认的原始对话时，不补造逐条确认历史。
- **候选建议**：原文标明建议、草稿、待确认或未定稿；允许写入记录不等于授权执行或接受方案。
- **历史经验**：记录当时讨论、修正、实施、验证或中止。测试通过、隔离范围及用时均是来源记录所述，本轮没有重新执行或独立证明。
- **混合／无法判断**：一份文件可同时含上述内容；表中写明差别。不能按文件夹、标题或已经有代码就判定全部设计已被用户接受。

## 主题入口

以下仅为检索导航，不是新规则：

- 长期记录与跨 session：R01–R12；共同设计、学习与独立判断：R13–R20、M01–M03、M07–M10。
- 授权、范围和 Git：R01、R14、R20、M01、M04、M13–M16、M22。
- 实现任务粒度、公开契约和隔离：M11–M19；意外越界与重启：M17、M18、M24、M27–M29。
- 测试依据、事实归属与复盘：R08、R17、M20–M29；工具限制、用时与 token 边界：M20、M23–M29。

## 研究过程仓库

来源：`/home/fainic/data/research-process`。下列链接文字保留原相对路径，行号对应未经改写的副本。

| 编号与原相对路径 | 性质与确认状态 | 相关主题；纳入理由 | 关键章节／段落 |
| --- | --- | --- | --- |
| R01 [AGENTS.md](sources/research-process/AGENTS.md) | 现载约定；原文作为协作要求发布，逐条确认历史本轮无法复核。 | **跨 session 上下文、授权、事实分层、独立判断、资源与 Git**。直接记录长期协作的入口、写入边界、沟通方式及资料组织，是本轮原始约定材料。 | 「开始工作」L9–16；「长期记录更新」L18–28；「内容组织与配套资源管理」L30–61；「维护与沟通」L63–76 |
| R02 [README.md](sources/research-process/README.md) | 现载工作方式；使用循环与已确认的初始化记录对应。 | **长期连续性、审阅写入、当前状态与历史分工**。说明记录既服务后续协作，也保留过程本身；给出完整使用循环及按需拆分条件。 | 「开篇目标」L1–7；「使用循环」L21–31；「维护」L33–49 |
| R03 [overview.md](sources/research-process/overview.md) | 已确认起点原则的概览＋个人经历；确认依据见研究起点记录。 | **实践反馈、渐进设计、保留个人语境**。保留先跑通再复盘的工程取向，并限定个人提醒的含义，避免后续提炼成普遍断言。 | 「工程原则」L17–22；「个人经历与提醒」L24–30 |
| R04 [state.md](sources/research-process/state.md) | 历史状态快照；正文称第一版工作流已确认，生成器未开始等进展已落后于代码仓库。 | **上下文恢复、状态时效、先明确验证问题**。保存早期工作流状态及待明确事项，可与后续实施记录对照状态滞后；不是今日能力清单。 | 「当前阶段与当前重点」L9–18；「下一步与待明确」L20–31；「暂不展开」L33–36 |
| R05 [projects/README.md](sources/research-process/projects/README.md) | 现载组织约定；项目进展不作为本轮核验事实。 | **跨项目索引、实现资料归属、本机路径**。明确研究主线、项目入口、原代码仓库和设备路径的分工，减少跨仓库重复维护。 | 「组织约定」L13–19 |
| R06 [local-paths.md](sources/research-process/local-paths.md) | 现载设备边界说明＋旧占位状态；原文件被 Git 忽略。 | **本机与云端访问边界、同步假设**。文件虽被忽略仍有协作相关内容：设备路径分别维护，云端不能默认访问；其中路径尚未填写。 | 「全文：本机维护与访问边界」L1–8 |
| R07 [inbox/README.md](sources/research-process/inbox/README.md) | 现载记录约定。 | **未成熟想法、确认后写入、原始出处**。记录零散想法不强制变成任务或清空，并规定整理、确认与成熟后关联方式。 | 「全文」L1–12 |
| R08 [experiments/README.md](sources/research-process/experiments/README.md) | 现载记录边界＋候选记录要素；原文用“建议记录”，不等于强制模板。 | **实验问题、可追溯性、观察与猜测**。给出在实际实验发生后再记录、按证据区分观察和解释的方式，可用于后续协作规则提炼。 | 「创建时机与建议内容」L1–12；「事实和产物位置」L14–15 |
| R09 [assets/README.md](sources/research-process/assets/README.md) | 现载附件管理约定；“本次不安装”等表述仅指当时范围。 | **可维护附件、稳定引用、派生输出与外部资源**。保存长时协作所需的附件位置、生成源、版本与链接检查约定，避免只留会话临时产物。 | 「存放与引用」L10–22；「版本与导出」L24–28；「外部资源」L30–34 |
| R10 [references/README.md](sources/research-process/references/README.md) | 现载维护约定＋历史阅读状态；部分“待填写”描述可能陈旧。 | **证据来源、论文主张与个人理解**。其维护段明确区分论文主张、个人理解和延伸想法；作为研究协作中的记录边界材料收录。 | 「开篇状态与复现边界」L1–16；「维护」L39–42 |
| R11 [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md) | 已确认讨论的历史记录；开篇明确“根据用户已确认的讨论整理”。 | **实践驱动、长期记忆、候选更新、个人提醒**。保存第一版工作流的动机、确认方式及避免空想阻碍推进的个人经历，便于追溯约定来源。 | 「状态与来源」L3–5；「工程思路的演变」L16–26；「工作流目标」L28–40 |
| R12 [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md) | 已确认决定＋实际初始化经验；开篇明确用户确认、已采用。 | **组织取舍、复查条件、环境事实**。既记录单文件与目录的权衡，也说明何时再拆分，以及未创建仓库时不虚构迁移过程。 | 「问题与顾虑及方案比较」L6–17；「当前决定与内容边界」L19–30；「决策理由与复查条件、落实」L32–43 |
| R13 [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md) | 已确认的两条原则；原文明确不是完整架构或强制流程，其他同期建议未确认。 | **渐进设计、探索空间、共同语义与工程偏好**。保留用户原话及获认可的补充，清楚区分原则、工程偏好和探索表达，防止把例外一律审批化。 | 「状态与范围」L5–11；「在草稿纸上积累线索」L13–29；「best practice 提供倾向」L31–51 |
| R14 [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) | 混合：用户目标、此前已确认原则、agent 研究判断与候选建议；候选流程尚未整体确认。 | **学习目标、证据强度、复杂度、Git、过程记录、协作效果**。直接围绕人与 agent 长期开发协作展开；包含可迁移经验的候选积累方法与研究适用边界，不能全部提升为既定规则。 | 「用户希望获得什么、证据边界」L5–30；「不宜照搬的流程规定」L65–71；「理解和管理 complexity」L100–113；「Git 与信息记录的候选起点」L122–161；「经验积累与未决事项」L163–199 |
| R15 [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md) | 历史讨论与理解变化；原文明示尚未形成需求或实现方案。 | **不倒写原始认识、说明隐含假设、独立审查**。虽含领域背景，仍有明确协作经验：将讨论后认识与用户原始想法区分，标明 agent 构造例子及未获确认的新问题。 | 「理解变化：端点描述与执行时序」L13–19；「新问题：到达之后发生什么」L21–33；「未经澄清的理解与能力判断」L49–61；「未决问题」L71–81 |
| R16 [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md) | 历史审阅修正＋尚未展开的建议；只是阶段性理解。 | **不迎合含混判断、保留修正过程、推断范围**。记录 agent 对“暴力搜索、不理解时序”的独立纠正，以及不能将文献支持误写为已有实现缺陷的边界。 | 「讨论背景」L5–16；「对原判断的修正」L40–53；「保留但尚未展开的改进想法」L96–106；「文献依据与阅读范围」L108–115 |
| R17 [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md) | 历史独立审查＋待讨论实验建议；明确尚无本次实验结果。 | **独立判断、可证伪问题、证据局限、不扩张研究结论**。将用户直觉、agent 审查和实验能证明的范围分别记录，是避免顺从式研究与提前定结论的具体案例。 | 「用户的直觉与意图」L7–13；「agent 的独立审查」L15–23；「实验含义与边界、尚未决定」L25–37 |
| R18 [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) | 历史共同写作；补充表述经用户审阅确认，原始表述保留用于理解过程。 | **保留原话、补充与原文分层、教学例证边界**。明确并列用户原始表述、补充表述与 agent 完善说明，展示如何纠正理解而不覆盖原始过程。 | 「状态与用户原始表述」L5–17；「与 agent 讨论后的完善表述」L19–21；「补充讨论背景」L90–98；「配套插图与证据限制」L131–135 |
| R19 [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md) | 历史个人理解与 agent 补充并置；未见全篇逐条确认声明，不能整体视为约定。 | **学习过程、保留个人表达、补充署名与纠错**。原始叙述和标明 agent 的补充并存，明确修正“只有 start/goal 所以大概率无法求解”等尚未成立的判断。 | 「原始研究表达」L9–11；「碰撞矩阵及 agent 补充」L19–34；「表示能力与算法判断的修正」L53–64；「从输入形式到空间占用的讨论过程」L70–87 |
| R20 [inbox/2026-09-16-generator-scene-and-target-representation.md](sources/research-process/inbox/2026-09-16-generator-scene-and-target-representation.md) | 混合：已确认业务语义、未决结构与被澄清撤回的 agent 方案；后者未确认。 | **澄清用户意图、不补齐未授权方案、未知项显式化**。原文直接记录用户要求补充“尚未确定”，却被 agent 误解为要求补齐方案的事件，是协作范围误读的具体材料。 | 「当前情况与确认范围」L5–17；「尚未确定：最终数据与名义场景的组织」L50–63；「其他待讨论事项与示例版本」L65–76 |

## 生成器代码仓库

来源：`/home/fainic/data/multiarm-problem-gen`。下列链接文字保留原相对路径，行号对应未经改写的副本。

| 编号与原相对路径 | 性质与确认状态 | 相关主题；纳入理由 | 关键章节／段落 |
| --- | --- | --- | --- |
| M01 [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md) | 现载协作约定；逐条确认历史本轮无法复核，历史试验中的例外授权仍需按原记录识别。 | **自主权限、架构参与、公开契约、阅读隔离、验证、计时、Git**。完整记录人与 agent 分工及实现隔离要求；既含讨论边界，也明确已授权普通实现不重复审批。 | 「人与 agent、记录」L9–27；「实现与验证」L29–45；「Git 与交接」L47–57；「架构决策与自主权限」L67–75；「实现任务的阅读边界与 Serena」L92–118；「契约缺口与异常处理」L120–133；「验证与记录」L135–157 |
| M02 [README.md](sources/multiarm-problem-gen/README.md) | 现载协作定位＋探索性实现状态；明确单元 4–6 未获用户最终接受。 | **学习目标、共同设计、跨仓库文档归属**。说明项目不仅产出代码，还支持用户参与架构与管理复杂度，明确研究记录与代码记录的边界。 | 「仓库组织与探索状态」L14–27；「设计与学习」L29–33 |
| M03 [docs/README.md](sources/multiarm-problem-gen/docs/README.md) | 混合：现载组织约定、历史入口与自主试验未接受状态。 | **讨论与实施分开、保留旧方案、过程导航**。规定按内容目的区分讨论与实施，不把已确认方案视为执行结果，也不将候选材料变成 agent 指令。 | 「当前阶段」L3–16；「讨论与方案」L18–37；「实施过程与复盘」L39–45；「接下来讨论、怎样组织记录」L53–69 |
| M04 [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md) | 现载 Git 约定；AGENTS 明确要求遵循，非本次收集任务的操作授权。 | **探索分支、逻辑提交、集成、授权、历史保留**。保存有价值尝试、主线接受状态、提交建议与授权分离、英文说明和语义集成检查的具体约定。 | 「探索分支与长期主线」L3–24；「何时提交与集成、集成方式」L26–51；「Commit message 与主线提交」L53–115；「操作边界」L117–123 |
| M05 [docs/design.md](sources/multiarm-problem-gen/docs/design.md) | 混合：已确认语义、候选抽象、过往方案状态及后续实施补充；不能整篇当作当前能力清单。 | **文档时间层次、候选与已实现区分、演变追溯**。同一文件保留“尚未实现”原方案并追加已完成说明，是长期记录不覆盖历史、同时防止状态误读的实例。 | 「更新时间与三次补充」L3–9；「单元 3 设计与未决接口」L34–42；「候选抽象与未决事项」L89–111 |
| M06 [docker/README.md](sources/multiarm-problem-gen/docker/README.md) | 现载运行与验收说明＋历史网络限制；版本是当时固定值，不声明最新。 | **统一环境、完整命令、就绪与验收区别、可复现性**。是协作执行入口，明确非空测试、容器就绪、宿主环境与任务阅读边界，并保存实际环境限制的处理条件。 | 「启动及就绪、网络限制」L1–38；「环境组织」L40–46；「固定版本与来源」L48–67；「自主试验完整验收」L128–158 |
| M07 [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md) | 历史组织选择与学习协作目标；当时暂不引入自主循环或多 agent，不等于长期禁令。 | **初始化事实、跨仓库迁移、学习目标、渐进流程**。记录实际起点与用户决定，保存初始组织选择及不急于把单次经验变成通用规则的背景。 | 「背景」L5–9；「本次组织选择」L11–15；「学习与协作目标」L17–21；「前序材料与下一步」L23–33 |
| M08 [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md) | 混合：已确认样例方向、agent 候选建议、追加的实际观察及后续确认；按段落日期理解。 | **具体实例暴露问题、范围控制、先讨论未知字段**。从“最小但完整”到可视化暴露三个问题，留下用户提问、agent 独立判断和后续修正，展示渐进设计的实际过程。 | 「目标与已确认选择」L7–22；「最小但完整」L24–30；「样例后暴露问题的背景」L58–64；「问题 1 的独立判断」L66–80；「后续确认及修正」L122–144；「未决项与验证边界」L229–237 |
| M09 [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md) | 历史对话取舍＋尚未定稿的局部方案；开篇明确不是完整接口。 | **以使用场景修正抽象、用户质疑、实测依据**。保存提前加载 mesh 的建议如何因用户质疑与有限实测改变，以及去掉多余层次的讨论，体现共同管理复杂度。 | 「状态与从读取结果谈起」L5–13；「Mesh：从提前解析转向按需加载」L37–45；「Pose、Frame 与场景复用」L47–53；「场景规则的澄清与后续计划」L93–103 |
| M10 [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md) | 用户表达诉求＋讨论方案；精确接口、可变性及错误规则仍待确认。 | **以数据流讲清设计、通俗术语、避免只列对象**。直接记录用户要求逐步说明 class 如何协作，并据此形成流程与例子；“对象协作”是代码语义，纳入依据是背后的沟通改进。 | 「从对象清单转向运行流程」L7–13；「运行流程与职责」L15–27；「一个协作例子」L29–48；「边界与后续」L50–56 |
| M11 [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) | 候选任务划分＋用户已选择首单元；并非全部接口或任务粒度定稿。 | **任务粒度、依赖准备、交付验收、契约隔离**。将可独立交付的任务与代码文件区分，说明资源接口必须提前准备、依赖不等于读内部实现。 | 「状态与划分方案」L5–20；「路径与共享资源的归属」L22–26；「建议实现顺序」L43–53 |
| M12 [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md) | 解释性补充与条件建议；原文明示未决定表示与读取拆合。 | **代码职责与任务范围、隔离实验设计**。回应用户对任务划分的困惑，指出分 class 或文件本身不构成独立上下文实验。 | 「问题与澄清」L7–23；「对契约隔离实验的影响」L25–31 |
| M13 [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md) | 讨论方案与建议执行次序；明确不等于实现授权，末段仅是工具可访问性检查。 | **实施准备、公开契约、就绪标准、分阶段验收**。界定环境和基础表示两部分的责任与验收，明确空测试不能算通过、方案写入不能等同执行。 | 「状态与环境方案」L5–23；「环境验收边界」L41–41；「执行顺序、权限与就绪判断」L85–93 |
| M14 [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md) | 已确认语义和可变性＋候选公开接口；原文明示不是实现授权。 | **用户纠正候选设计、行为契约、内部自主**。记录全部不可变建议经用户指出需要 Frame 更新后被修正，及公开契约与内部组织的分工。 | 「状态与候选字段」L5–15；「构造、引用与可变性」L31–49；「首次交付与验收」L68–78；「实现前还需补齐」L80–86 |
| M15 [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md) | 已确认方向＋待具体化接口；写文档不等于执行实现。 | **减少重复表示、准备交接、完整一词的范围边界**。保留 RobotConfig 拆分建议被修正的过程，明确“完整支持当前输入”不授权扩展全部能力，及仅依赖公开契约的执行范围。 | 「状态、目标与本次修正」L5–13；「缺失信息与默认含义」L48–58；「实施范围与准备」L126–132 |
| M16 [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md) | 已确认职责与范围＋候选签名＋未来待议接口；当时仅授权记录方案和准备判断。 | **修正建议、当前与未来能力分开、实现授权、验收范围**。记录用户对资源归属和命名方案的调整，以及明确未来手动登记接口不应混入当前实现任务。 | 「状态与本轮范围」L5–13；「本轮选择与保留方向」L90–96；「验收与允许修改范围」L119–135；「实施准备判断」L137–143 |
| M17 [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md) | 已作出的探索性 agent 决定；明确不表示用户接受设计，关键缺口交同一决策者复议。 | **决策与实现分离、信息包、备选理由、权限归属、交接污染**。保存自主试验的完整决定、排除方案和返回讨论条件；D6-4 记录内部测试断言被转述进入上下文，是后续停止事件的来源。 | 「状态与信息包边界」L3–11；「D4-1 及阅读记录」L13–37；「D6-1 资源补丁分工」L39–47；「D5-3 名称消歧」L140–146；「D6-4 内部测试信息来源与限域维护」L148–160 |
| M18 [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md) | 历史交接材料；摘自探索性 agent 决定，不代表用户最终接受。 | **过滤信息包、公开契约、独立上下文、复议结果**。与完整决定及中止记录配对，保留修复阅读边界后实际提供给新上下文的信息包，而不只保留事后总结。 | 「交接用途与状态」L1–3；「D5-1 与 D5-2」L5–44；「D5-3 复议及边界补充」L47–56 |
| M19 [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md) | 历史交接材料；探索性 agent 决定，最终接受未定。 | **职责分工、最小公开扩展、共享文档维护、迁移验收**。保留过滤后的 U6 信息包及主 agent 维护共享入口的边界，可与完整决定中不应下传的 D6-4 对照。 | 「交接用途与主 agent 职责」L1–3；「D6-1 补丁职责与验收」L5–13；「D6-3 最小迁移与修改范围」L45–58 |
| M20 [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md) | 历史实施记录；正文记载用户确认分两次提交，本轮未重验其历史测试。 | **环境诊断、独立预期、验证层级、阅读自述、交接**。保留网络失败未被误判为版本不存在、安装验收与 zip 导入区分、同上下文不能冒充独立契约实验等具体经验。 | 「基线与范围」L3–11；「环境验收与网络限制」L13–26；「基础表示验收及限制」L28–43；「契约是否足够、阅读范围」L45–66；「交接」L68–70 |
| M21 [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md) | 历史实施自述；后续已确认移除 Material，原记录保留当时结果。 | **保护已有修改、独立算例、测试预期纠正、依赖阅读边界**。记载手工数量预期错误如何通过源 XML 独立计数修正，区分改测试预期与迁就实现，并保留后续修正链接。 | 「来源、后续修正与起点」L3–9；「实际验证」L17–37；「契约与阅读边界」L39–47；「剩余边界与局部不足」L49–56 |
| M22 [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md) | 用户已确认的接口收缩＋历史执行结果；授权仅覆盖此次删减。 | **审查后收缩范围、避免过度实现、旧记录不覆盖**。独立审查发现需求依据不足，用户确认删除；记录接口变化、测试调整与保留原历史的做法。 | 「原因与变更」L3–11；「验证与边界」L13–19 |
| M23 [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md) | 历史实施自述；以当次授权和公开方案为依据，原方案不改写为结果。 | **先定测试目的、错误预期纠正、源文件保护、阅读与时间统计**。给出独立测试依据、缓存预期错误与实现缺陷的不同处理，记录已有变更保护及无法细分的混合时间。 | 「完成范围与原有修改保护」L3–14；「测试目的与依据」L16–28；「实际结果与失败处理」L30–49；「阅读范围与工具边界」L51–67；「用时与 token、契约限制」L69–86 |
| M24 [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) | 历史探索性实施与汇总；原文明示最终设计是否接受仍由用户决定。 | **独立上下文、决定先行、失败重启、集成、证据归属、计量**。保存完整试验分工、U5 中止与重启、局部修复回交原 agent、主 agent 独立集成及用量统计限制。 | 「起点与边界、初始验证」L3–19；「任务与决定入口」L21–32；「集成测试目的及最终验收」L34–61；「结果、决定与限制」L63–69；「用量与计时、本地交付」L71–93 |
| M25 [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md) | 历史探索性补丁；不表示最终设计接受，协调者基线不是子任务独立证据。 | **专属修改范围、公开接口补齐、测试依据、工具回退**。展示由模块所属 agent 补充公开能力、后续模块仅消费契约的具体做法，并如实保留工具截断与计时缺口。 | 「范围与测试目的」L3–11；「执行结果与契约判断」L13–19；「实际阅读与工具边界」L21–27；「时间与用量」L29–33 |
| M26 [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md) | 历史探索性实现；D4-1 非用户最终接受的设计。 | **独立预期、局部职责、有限验证结论、交接证据**。专属实现与测试独立完成，明确协调者报告不算自身重验、有限 I/O 检查非形式化证明、参数验收非采样验收。 | 「授权状态与完成内容」L3–12；「测试目的与独立依据」L14–22；「实际验证与交接归属」L24–35；「阅读范围、时间与未决项」L37–61 |
| M27 [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md) | 历史失败／中止记录；没有代码或测试结果，契约草稿仍待核对。 | **意外信息越界、主动报告、停止与重新隔离、诚实计时**。保存未主动打开依赖文件却从允许材料接收到内部断言的事实，明确不能声称忘掉信息或仍满足纯公开隔离。 | 「实际产物与停止原因」L3–9；「实际阅读」L11–15；「时间、用量与未完成边界」L17–21 |
| M28 [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md) | 历史重启后的探索性实施；最终设计接受未定，隔离状况为 agent 自述。 | **干净上下文交接、独立测试、缺陷回修、检查范围诚实**。记录不继承停止上下文、重写公开草稿、测试后修正自身错误及 diff 检查不覆盖未暂存新增文件的限制。 | 「新上下文与完成范围」L3–9；「测试目的、结果及局限」L11–29；「读取边界与用量」L31–44；「契约与局限」L46–48 |
| M29 [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md) | 历史探索性实施；主 agent 汇总测试属于转述，不能算本 agent 独立验证。 | **共享文档责任、公开声明阅读、迁移最小化、测试目的与计时**。保存 U6 的修改边界、精确样例迁移、自审补测及仅取公开声明的工具使用经验，明确执行依赖不等于读源码。 | 「完成范围与共享入口责任」L3–13；「测试目的与依据」L15–21；「实际结果及归属」L23–38；「契约、阅读与工具」L40–54；「用时与用量」L56–64 |

## 未纳入的材料与不确定事项

筛选依据是文件是否直接给出协作约定、明确的人与 agent 讨论／纠正事件、任务交接或实施复盘。没有因含有“agent”“确认”“协作”等词就自动纳入，也没有为补齐原文链接而全量复制业务材料。

- 其余 30 份 Markdown 逐项列于覆盖记录：主要为纯业务输入输出格式、分布／输入包语义、七份 API 契约、文献技术笔记、模型准备与预览说明、项目占位入口及空日志。正文中的有限来源声明或业务方案确认不自动使整篇成为协作规则材料。
- 非 Markdown 文件没有纳入：实现及测试代码、场景／模型数据、第三方资源、论文 PDF、图片与导出、构建产物、缓存、编辑器与 Serena 默认配置。已清点隐藏、未跟踪和忽略项；其中 `research-process/local-paths.md` 因直接涉及设备访问边界而收录。
- R04 的生成器“尚未开始”、R06 的“尚未创建或待填写”等是旧状态；M05 同时保留历史方案和后续实施补充。索引不静默消除这些差异。
- R14 的调研流程仍是候选；M17–M19、M24–M29 的自主决定或成功实施不能当作用户已接受最终设计。M27 的中止与 M28 的新上下文必须分开看。
- “未发现越界”是记录者自述，不是独立审计证明；本次保留原文给出的计时缺口、token 不可用、他人验证转述及未验收能力，不补造证据。
- 副本中的原有相对链接、图片链接、外部链接和旧路径均未改写；有些指向本轮未选材料，阅读时可能不可达。**已核验的是本 INDEX 指向的全部副本与审计文件路径**，不承诺所选原文的传递链接闭包。完整源仓库仍是技术背景的查阅位置。
- 执行边界说明：早期文件数量统计和 Markdown 标题枚举使用 Path.rglob，文件访问前排除了 .git 路径，但未在目录遍历前剪枝，因此会枚举 .git 目录项；没有读取、展示或使用 Git 对象内容、历史版本或其他分支材料。正式清单与最终校验改为 os.walk 并预先排除 .git。若把目录项枚举本身计作进入 .git，本轮存在这一执行偏差。
- 未向外部资料求证原文引用、历史测试与历史授权；确认状态仅据当前工作区正文判断。二进制资产只按文件角色清点，没有做全文或视觉内容审阅。因此这是可复核的主题筛选集合，不是对全部协作经验穷尽性的证明。

## 本轮校验

收录时逐份与清点时的源文件 SHA-256 比较，并按字节比较副本；最终再次比较全部 49 份原文／副本、核对索引路径和章节行号，并复查 268 份来源文件是否相对初始清点发生内容变化。实际结果以 [verification.json](audit/verification.json) 为准。本轮没有提交、合并或推送。
