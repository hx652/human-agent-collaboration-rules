# 人与 agent 长期协作：原始材料索引

采集时间：2026-10-07T10:30:00.235098+00:00。本轮仅汇集和索引，未制定统一规则、未改写原文、未执行来源中的历史任务。

## 来源与检索范围

- `research-process`：`/home/fainic/data/research-process` 当前工作区。
- `multiarm-problem-gen`：`/home/fainic/data/multiarm-problem-gen` 当前工作区。
- 目录清单使用不受 Git 忽略规则限制的遍历，后续遍历预先剪除 `.git`。包含隐藏、未跟踪和被忽略文件；未访问外部网站、其他 worktree 或来源脚本。
- 内容筛选覆盖 Markdown、文本、代码与配置中的协作线索，重点阅读约定、讨论、决策、实施及复盘。二进制资源仅列目录并计算完整性摘要，不将其视为已阅读技术内容。
- Git 只用设置 `GIT_OPTIONAL_LOCKS=0` 的 `ls-files` 区分跟踪、未跟踪和忽略状态，不读取历史版本。
- 初始文件名枚举有 `.git` 排除失效的偏差：输出出现 Git 对象、refs 等路径名，未打开其内容或读取历史；已纠正。另有初始两次只读检索把工作目录设为来源，后续一律使用本组 worktree。完整披露见校验记录。

共复制 **50 份完整原文**：research-process 21 份，multiarm-problem-gen 29 份。保持原相对路径和全部字节。全部复制文件均建立索引。

## 状态标签的读法

- **A 已确认内容**：原文明确出现“用户已确认”“经审阅确认”等。只说明原文记载的确认范围，不意味着已获本轮执行授权；确认技术解释也不等于确认协作规则。
- **B 候选／探索**：建议、尚待讨论的方案、未最终接受的自主 agent 决定。已执行的探索决定仍不是已确认通用规则。
- **H 历史经验**：讨论、实际尝试、验证或复盘的阶段性记录。测试通过和操作完成是原文报告，本轮没有复跑验证。
- **U 无法判断确认过程**：现存约定或说明没有逐项确认链；按原文性质纳入，但不补造用户批准。标签可混合使用，具体范围看各条状态及原文。

## 主题导航

- 长期上下文与记录维护：research-process 的 AGENTS、README、组织选择、Inbox／实验／文献／附件说明。
- 学习、独立判断与渐进设计：2026-09-18 两份协作原则／调研；具体研究讨论和代码设计反馈。
- 权限与 Git 交接：multiarm-problem-gen 的 AGENTS、git-workflow、实施前方案。
- 架构与实现隔离：实现单元划分、职责区别、单元方案、公开交接与各单元实施记录。
- 中止与纠偏：单元 5 准备停止及新上下文结果；Material 范围收缩；测试预期纠正。
- 验证与统计：首轮、单元 2–6、资源快照及自主试验总记录中的测试目的、阅读范围、用时和用量限制。

## research-process：原文清单

| 原文副本（原路径） | 原文状态 | 相关主题 | 纳入理由 | 关键章节／原文行号 |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/research-process/AGENTS.md) | U：现存协作约定；本文件未注明逐项确认过程 | 跨 session；权限；事实分层；沟通；附件管理 | 直接记录长期协作的读取入口、逐次写入授权、独立判断和资源维护。 | 《开始工作》L9；《长期记录更新》L18；《配套资源管理》L48；《维护与沟通》L63 |
| [README.md](sources/research-process/README.md) | U：现存工作流说明；确认细节需结合历史记录 | 记录循环；恢复上下文；渐进拆分 | 提供人审阅、agent 写入、Git 检查及记录演变的完整工作循环。 | 《使用循环》L21；《维护》L33 |
| [overview.md](sources/research-process/overview.md) | H/U：个人经历及当前原则；未逐条注明确认过程 | 实践反馈；避免过度规划；个人经验边界 | 保留先跑通再复盘的工程原则及个人提醒的原背景，避免将其当成普遍定律。 | 《工程原则》L17；《个人经历与提醒》L24 |
| [state.md](sources/research-process/state.md) | A/H：第一版工作流明确已确认；其余为当时阶段记录 | 状态与历史；先明确验证问题 | 记录工作流已确认和首轮测试需回答的问题；其中“尚未实现”等不代表两个来源仓库今天的共同状态。 | 《当前阶段》L9；《下一步》L20；《暂不展开》L33 |
| [projects/README.md](sources/research-process/projects/README.md) | U：现存组织约定；未注明逐项确认 | 跨项目记录；单一维护位置；本机路径 | 区分研究主线、项目入口、代码原仓库和设备路径，避免重复维护。 | 《组织约定》L13 |
| [projects/dataset-generator/README.md](sources/research-process/projects/dataset-generator/README.md) | H/U：项目阶段与未决问题；不是实现需求确认 | 首版范围；验收问题；候选与决定 | 具体展示项目入口如何明确首轮测试问题并声明待讨论事项不是确认需求。 | 《当前情况》L8；《待讨论》L12 |
| [projects/stop-n-go/README.md](sources/research-process/projects/stop-n-go/README.md) | H/U：用户报告与未验证事项 | 用户报告；证据范围；版本关联 | 明确复现只是用户报告，验证待补，不预先把潜在不足写成结论。 | 《当前情况》L7；《材料入口》L12 |
| [inbox/README.md](sources/research-process/inbox/README.md) | U：现存随手记录约定 | 保留原始想法；不强制任务化；确认写入 | 展示未成熟想法的记录方式、审阅写入和成熟后保留出处。 | 《随手记录》L1 |
| [experiments/README.md](sources/research-process/experiments/README.md) | B：原文明确为建议记录 | 实验记录；观察与猜测；产物引用 | 提供实验问题、实际结果、局限和版本配置的候选记录维度，明确无需提前填模板。 | 《实验记录》L1 |
| [references/README.md](sources/research-process/references/README.md) | U：维护约定；阅读完成状态未逐项核验 | 论文主张；个人理解；来源标注 | 纳入维护节区分论文主张、个人理解与延伸想法；不据入口存在认定阅读完成。 | 《维护》L39 |
| [assets/README.md](sources/research-process/assets/README.md) | U/H：资源维护说明及当时配置报告 | 附件；原件与导出；稳定链接；外部同步 | 完整记录长期资源目录、生成源文件、导出副本和外部文件同步的职责区别。 | 《存放与引用》L10；《版本与导出》L24；《外部资源》L30 |
| [local-paths.md](sources/research-process/local-paths.md) | U：本机说明；Git 忽略文件 | 设备边界；访问能力；路径不等于同步 | 被忽略但直接相关：说明设备各自维护及云端不能默认访问；现有条目均为待填状态。 | 《本机路径》L1 |
| [journal/2026-09-07-starting-point.md](sources/research-process/journal/2026-09-07-starting-point.md) | A/H：原文明示根据用户已确认讨论整理 | 实践反馈；记录本身的目标；审阅写入 | 保留工作流设计起点、个人阻碍和渐进完善理由。 | 《工程思路的演变》L16；《工作流目标》L28 |
| [journal/2026-09-07-record-organization.md](sources/research-process/journal/2026-09-07-record-organization.md) | A/H：原文明示用户已确认且初始化采用 | 组织比较；决定理由；复查条件 | 保留单文件与目录的比较、已采用决定和何时再拆分的条件。 | 《方案比较》L12；《当前决定》L19；《决策理由与复查条件》L32；《落实》L38 |
| [inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md](sources/research-process/inbox/2026-09-07-multi-arm-query-and-temporal-coordination.md) | H/B：原文为讨论想法；未形成需求或方案 | 澄清隐含假设；用户与 agent 归属；未决问题 | 技术内容承载实际协作案例：不把后来澄清倒写为最初认识，不把 agent 例子或风险当实证。 | 《理解变化：端点描述与执行时序》L13；《例子二：未经澄清的理解可能缩窄 planner 的能力范围》L49；《未决问题》L71 |
| [inbox/2026-09-08-multi-arm-progress-and-coordination.md](sources/research-process/inbox/2026-09-08-multi-arm-progress-and-coordination.md) | H/B：阶段性理解；改进想法未确定 | 独立审阅；修正概念；文献与推断边界 | 保留 agent 对“暴力搜索”的修正及对尚未验证改进想法的限制，作为讨论经验。 | 《二、对“暴力搜索、不理解时序”的修正》L40；《六、保留但尚未展开的改进想法》L96；《文献依据与阅读范围》L108 |
| [inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md](sources/research-process/inbox/2026-09-09-coordination-intuition-and-experimental-evidence.md) | H/B：经独立审查记录；没有实验结果，方案待讨论 | 独立判断；可证伪问题；结果解释边界 | 体现认可直觉同时限制主张、将直觉转成可观察问题，并允许实验否定预期。 | 《agent 的独立审查》L15；《“用实验验证想法”的含义与边界》L25；《尚未决定》L35 |
| [inbox/2026-09-15-cube-complex-understanding.md](sources/research-process/inbox/2026-09-15-cube-complex-understanding.md) | A/H：原文称完善表述经用户审阅确认；确认的是解释内容 | 保留原话；追加修正；例子来源；图示阶段 | 保留用户原始理解与确认后说明并列的具体做法；不将其中数学解释提升为协作规则。 | 《用户原始表述》L11；《与 agent 讨论后的完善表述》L19；《补充讨论：路径拆分与基本方片》L90 |
| [journal/2026-09-15-research-understanding-and-direction.md](sources/research-process/journal/2026-09-15-research-understanding-and-direction.md) | H/U：用户正文与 agent 补充；本文件未统一注明审阅状态 | 作者归属；纠正推断；保留思考演变 | 展示保留用户声音、用明确补充块修正未经证明结论，而非覆盖个人笔记。 | 《碰撞矩阵》L19；《联合空间中的进度表示》L36；《终于有点眉目》L66 |
| [inbox/2026-09-18-evolving-design-and-best-practices.md](sources/research-process/inbox/2026-09-18-evolving-design-and-best-practices.md) | A：原文明示两条原则讨论认可后保存；不是完整强制流程 | 渐进设计；工程偏好；共同语义；探索空间 | 直接相关的已确认原则及其适用边界，另有候选流程未确认的明确声明。 | 《1. 在草稿纸上积累线索，逐渐形成整体设计》L13；《2. best practice 提供倾向，保留表达与探索空间》L31 |
| [inbox/2026-09-18-agent-collaborative-development-research.md](sources/research-process/inbox/2026-09-18-agent-collaborative-development-research.md) | A/B/H：用户目标及前序原则、候选建议、外部经验分开；流程未整体确认 | 学习目标；证据分层；复杂度；Git；可迁移经验 | 核心协作调研原件，完整保留论据、来源及未决事项；本轮不访问或核验外部链接。 | 《1. 用户希望通过这个项目获得什么》L7；《2. 调研范围与证据边界》L21；《7. 论坛讨论暴露的摩擦》L115；《8. Git 的候选使用方式》L122；《10. 怎样积累可迁移的经验》L163；《11. 当前综合判断与未决事项》L187 |

## multiarm-problem-gen：原文清单

| 原文副本（原路径） | 原文状态 | 相关主题 | 纳入理由 | 关键章节／原文行号 |
| --- | --- | --- | --- | --- |
| [AGENTS.md](sources/multiarm-problem-gen/AGENTS.md) | U：现存项目约定；未逐条注明用户确认过程 | 授权；学习；职责；契约隔离；意外越界；验证统计 | 最直接的协作约定，完整保留常规协作与架构、实现分离两部分。 | 《人与 agent》L9；《记录》L21；《架构决策与自主权限》L67；《实现任务的阅读边界》L92；《契约缺口与异常处理》L120；《验证与记录》L135 |
| [README.md](sources/multiarm-problem-gen/README.md) | U/H：现存项目说明及探索阶段声明 | 学习与设计参与；跨仓库分工；已实现与接受分开 | 明确用户参与设计和跨项目经验归属，并声明自主实现不等于最终设计接受。 | 《设计与学习》L29；《仓库组织》L14 |
| [docs/README.md](sources/multiarm-problem-gen/docs/README.md) | U/H：现存记录组织说明；包含探索结果入口 | 讨论与实施分开；历史状态；候选非指令 | 说明如何分类记录、保留原方案并链接实施结果，是索引组织的原始证据。 | 《讨论与方案》L18；《实施过程与复盘》L39；《怎样组织记录》L61 |
| [docs/git-workflow.md](sources/multiarm-problem-gen/docs/git-workflow.md) | U：现存 Git 约定；确认过程未单独说明 | 探索主线；逻辑提交；授权；交接 | 完整保存分支、提交、集成和推送各自权限及历史保留的协作方式。 | 《探索分支与长期主线》L3；《何时提交与集成》L26；《集成方式》L41；《操作边界》L117 |
| [docker/README.md](sources/multiarm-problem-gen/docker/README.md) | U/H：现存验收说明及历史环境事实 | 环境可复现；就绪与启动；空测试；阅读边界 | 技术文档中有独特协作证据：空测试不能验收、容器挂载不解除阅读限制、固定版本不声称最新。 | 《Docker／Compose 开发环境》L1；《环境组织》L40；《固定版本与来源》L48；《自主试验：完整输入包入口与验收》L128 |
| [docs/design.md](sources/multiarm-problem-gen/docs/design.md) | A/B/H：原文已确认语义、候选抽象、实施补充混合 | 当前设计与过程；接受状态；未决事项 | 纳入开头实施补充与原段落并存，展示更新入口时保留旧过程、不把试验结果当最终接受。 | 《当前设计草稿》L1；《候选抽象与待验证的问题》L89；《未决事项》L101 |
| [docs/notes/discussions/2026-09-18-starting-point.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-starting-point.md) | H：初始化决定及协作目标；不是未来执行授权 | 学习参与；渐进组织；跨项目追溯 | 保留建仓时为何采用轻量记录组织、不引入完整自主工作流的上下文。 | 《本次组织选择》L11；《学习与协作目标》L17；《前序材料》L23 |
| [docs/notes/discussions/2026-09-18-first-input-example.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-18-first-input-example.md) | A/B/H：已确认方向、候选建议及同日追加混合 | 用户提问；独立判断；具体例子；范围控制 | 保留可视化暴露三个问题后的用户意见、agent 判断、后续确认方案，展示反馈驱动设计。 | 《“最小但完整”的含义》L24；《追加：基准场景与可视化暴露的三个问题》L58；《追加：问题 1、2 的方案》L122；《追加：问题 3 的方案》L166 |
| [docs/notes/discussions/2026-09-22-input-domain-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-22-input-domain-representations.md) | H/A/B：讨论取舍与部分确认；完整方案未统一定稿 | 用户纠正 agent；实测成本；按需抽象 | Mesh 由提前解析转为按需加载的讨论保留意见来源与实测开销边界，是具体协作反馈。 | 《从读取结果谈起》L9；《Mesh：从提前解析转向按需加载》L37；《Pose、Frame 与场景复用》L47；《后续计划》L99 |
| [docs/notes/discussions/2026-09-28-input-reading-flow.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-28-input-reading-flow.md) | H/B：讨论方案；精确接口与可变性待确认 | 解释数据流；降低术语负担；职责取舍 | 用户要求解释每步及对象如何协作，体现讲解方式怎样帮助理解复杂度。 | 《从对象清单转向运行流程》L7；《运行流程与职责》L15；《边界与后续》L50 |
| [docs/notes/discussions/2026-09-29-input-implementation-units.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-input-implementation-units.md) | H/A/B：划分依据；单元 1 已选择，粒度未全部定稿 | 任务范围；依赖契约；实施顺序 | 说明独立交付单位不是代码类或文件，并明确依赖接口应提前供给而非读取实现。 | 《划分方案》L7；《路径与共享资源的归属》L22；《建议实现顺序》L43 |
| [docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-implementation-unit-and-responsibility.md) | H/B：澄清与建议；未决定合并或拆分任务 | 任务粒度；职责分离；阅读隔离实验 | 直接区分代码职责边界与实现任务阅读边界，防止将拆文件误认为上下文隔离。 | 《问题与澄清》L7；《对契约隔离实验的影响》L25 |
| [docs/notes/discussions/2026-09-29-unit-1-basic-representations.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-1-basic-representations.md) | A/B/H：明确已确认语义与候选接口；不是实现授权 | 用户纠正；可变性；契约准备；局部自主 | 保留全不可变建议被用户修正、公开契约逐步明确及不预设计私有方法的具体过程。 | 《构造、引用与可变性》L31；《首次交付与验收》L68；《实现前还需补齐》L80 |
| [docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-compose-and-unit-1-implementation.md) | H/B：已讨论方案；原文明确不代表执行授权 | 先契约后实现；范围；环境验收；分阶段交付 | 明确方案就绪、权限和真正执行之间的区别，并说明不能将空测试当验收通过。 | 《执行顺序、权限与就绪判断》L85；《第一部分：统一 Docker／Compose 环境》L7 |
| [docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md) | A/B/H：确认接口方案；写入不等于实现执行 | 依赖隔离；修改范围；语义歧义回讨论 | 纳入其实施准备节限制依赖阅读、反对因“完整”扩大功能范围和局部自主的条件。 | 《错误与验收》L118；《实施范围与准备》L126 |
| [docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md) | A/B/H：确认职责与候选字段分开；仅方案不实施 | 测试目的；允许范围；就绪判断；契约歧义 | 具体展示如何给出实施范围、验收可说明什么、不能说明什么及返回讨论条件。 | 《本轮选择与保留方向》L90；《验收与允许修改范围》L119；《实施准备判断》L137 |
| [docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md) | B/H：已执行探索性 agent 决定；明确非用户最终接受 | 决策与实现分工；信息包；复议；污染披露 | 保存自主决策、排除方案及一条内部测试通过交接进入上下文的来源记录。 | 《信息包与边界》L5；《D6-1：先补公开资源快照》L39；《D5-3：mean 的 configuration 名称消歧》L140；《D6-4：既有真实样例测试的单字符串维护》L148 |
| [docs/notes/discussions/2026-09-30-unit-5-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-5-public-handoff.md) | B/H：探索性决定的公开摘录；明确非用户接受 | 过滤交接；公开契约；严格上下文 | 与停止记录对照，展示过滤依赖内部信息后的实际公开交接包。 | 《单元 5 公开交接包》L1；《D5-1：保留 YAML，公开统一作用关联》L5；《D5-3：mean 的 configuration 名称消歧》L47 |
| [docs/notes/discussions/2026-09-30-unit-6-public-handoff.md](sources/multiarm-problem-gen/docs/notes/discussions/2026-09-30-unit-6-public-handoff.md) | B/H：探索性决定的公开摘录；明确非用户接受 | 公开交接；共享文件归属；隔离边界 | 展示下一实现单元只接受公开决定，既有内部测试与共享入口由主 agent 维护。 | 《单元 6 公开交接包》L1；《D6-1：先补公开资源快照》L5；《D6-3：真实样例最小迁移与验收》L45 |
| [docs/notes/implementation/2026-09-29-first-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-first-implementation-results.md) | H：实际实施与验收自述；原文明示提交获确认 | 契约足够性；独立算例；工具失败；事实边界 | 记录环境限制、命令输出误读风险、限定阅读及自述不是独立无越界证明。 | 《契约是否足够》L45；《阅读范围与工具限制》L53；《交接》L68 |
| [docs/notes/implementation/2026-09-29-unit-2-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-29-unit-2-implementation-results.md) | H：实际实施记录；后续 Material 修正另有链接 | 错误预期修正；依赖隔离；原记录保留 | 保留独立计数纠正测试预期、保护已有变更和链接后续修改而不覆盖历史的案例。 | 《实际验证》L17；《契约与阅读边界》L39；《剩余边界与局部不足》L49 |
| [docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md) | H：授权探索完成；不表示最终设计接受 | 多 agent 分工；重启；集成；墙钟与用量；权限制约 | 自主试验总复盘，完整保留污染修复、公开交接、统一验收以及统计局限。 | 《任务与决定入口》L21；《主 agent 集成测试目的（编写前）》L34；《最终验收事实》L40；《用量与计时》L71；《本地交付状态》L91 |
| [docs/notes/implementation/2026-09-30-remove-material-support.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-remove-material-support.md) | H/A：用户确认特定接口收缩；不是通用新规则 | 独立审查；需求依据；收缩范围；历史修正 | 实际案例：审查发现过度支持后，用户确认收缩公共接口并保存旧验证记录。 | 《原因与变更》L5；《验证与边界》L13 |
| [docs/notes/implementation/2026-09-30-resource-snapshots-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-resource-snapshots-results.md) | H/B：探索补丁；明确非最终接受 | 专属范围；独立预期；交接非独证；工具回退 | 记录公开快照怎样支持隔离协作，以及测试目的、误差边界和混合阶段计时。 | 《范围与测试目的（编写测试前）》L5；《实际阅读与工具边界》L21；《时间与用量》L29 |
| [docs/notes/implementation/2026-09-30-unit-3-implementation-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-3-implementation-results.md) | H：用户授权范围内实际实施；保留前方案 | 测试依据；阅读分段；计时；契约判断 | 保留公开依赖足够性、未发生架构回议与自述证据限制，提供契约实验实例。 | 《测试目的与依据》L16；《阅读范围与工具边界》L51；《用时与 token》L69；《契约判断及剩余限制》L82 |
| [docs/notes/implementation/2026-09-30-unit-4-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-4-results.md) | H/B：探索实现；最终设计尚未接受 | 独立上下文；自主局部选择；测试目的；统计 | 记录自写独立算例、不读取其他模块实现、交接验证与自身验证分开。 | 《测试目的与独立依据》L14；《阅读范围与工具》L37；《时间、用量与未决项》L51 |
| [docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-preparation-stopped.md) | H：明确中止、没有实现与测试；不是验收结果 | 意外信息混入；诚实停止；干净重启；统计缺口 | 关键失败过程原件：内部断言经决定文件进入上下文，不宣称能忘记或继续算隔离成功。 | 《实际产物与停止原因》L5；《实际阅读》L11；《时间、用量与边界》L17 |
| [docs/notes/implementation/2026-09-30-unit-5-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-5-results.md) | H/B：过滤公开交接后的独立探索实现 | 独立重启；问题回归；依赖报告；统计不可用 | 与准备停止记录成对，保留重新实施、失败修正和未暂存文件不被差异检查覆盖的局限。 | 《测试目的、依据与结果》L11；《读取边界与用量》L31；《契约与局限》L46 |
| [docs/notes/implementation/2026-09-30-unit-6-results.md](sources/multiarm-problem-gen/docs/notes/implementation/2026-09-30-unit-6-results.md) | H/B：独立探索实施；明确非用户接受 | 职责分工；公开声明；验证范围；混合计时 | 具体展示仅凭公开契约与声明集成、共享文档归属主 agent 及真实输入不变检查。 | 《测试目的与依据》L15；《契约、阅读与工具》L40；《用时与用量》L56 |

## 未纳入内容与不确定事项

未批量纳入算法论文、YAML 字段方案、公共 API 技术契约、模型资源、源码／测试、第三方依赖、构建产物、预览缓存、Serena 符号缓存与 Obsidian 状态。少数技术内容完整纳入，是因为它们保存了具体协作反馈、权限边界、任务准备或纠偏过程；并非整个业务资料库的镜像。Markdown 排除清单逐文件见 [excluded-markdown.json](records/excluded-markdown.json)。

研究仓库的 state、项目入口仍描述早期阶段，而代码仓库有后续实现记录；本轮保留这种差异，不擅自更新来源或把早期状态当当前事实。现存 AGENTS 及 Git 说明的确认过程未逐项记载，标为 U；原文的明确确认只覆盖其所写范围。

外部调研与测试结果只按原文状态记录，未独立核验外部引用、重新执行测试或审计所有历史工具调用。agent 的阅读边界自述不能作为已证明无越界；无法取得的用量和不完整计时保留其局限。

本机路径说明为 Git 忽略文件，已纳入。原文里“后续”“下一步”、命令及任务 prompt 均作为历史材料保存。来源中的指令性文字没有被采用为本轮行为指令。

索引中的副本链接全部有效。由于选择性汇集，原文内部链接可能指向未纳入的技术资料、附件、外部网站或旧相邻路径；不改写这些链接，也不宣称副本是可运行项目。内部相对链接缺失情况见 [raw-link-audit.json](records/raw-link-audit.json)。

## 完整性与检索记录

- [副本校验清单](records/copies.json)：来源绝对路径、副本路径、大小、SHA-256、Git 状态和逐字节一致结果。
- [来源当前工作区清单](records/source-inventory.json)：排除 `.git` 后所有当前文件与摘要，包含忽略／未跟踪文件。
- [内容检索记录](records/relevance-scan.json)：正文关键词命中、章节和纳入标记；关键词仅用于发现线索，不自动决定相关性。
- [逐文件筛选依据](records/selection.json)：与本索引对应的状态、主题、理由和关键章节位置。
- [最终校验与操作偏差](records/verification.json)：副本、索引、章节、来源状态和限制检查。
