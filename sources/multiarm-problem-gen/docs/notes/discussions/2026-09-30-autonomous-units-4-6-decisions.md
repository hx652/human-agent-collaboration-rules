# 单元 4—6 自主决策记录

日期：2026-09-30。状态：探索性实现决定；由独立决策 agent 作出，**不表示用户接受这些设计**。后续关键契约问题回到同一决策 agent 复议。

## 信息包与边界

- 任务标识：`/root/design_decisions`；实施协调：`/root`。分支 `codex/autonomous-units-4-6`，协调 agent 报告基点 `aa98559ecec51559dbcd2ce24e8853cf61263ffa` 正确；本 agent 实际核对分支且初始无差异。
- 本地工具环境可访问 `/home/fainic/data/multiarm-problem-gen` 和研究记录仓库；本 agent 只写本文件，不修改实现或提交。
- 用户固定边界：不采样、不复制或生成场景、不做 FK／IK／碰撞／规划／输出，不支持有关节环境或机器人 link frame；frame 无前缀；reader 不登记自身；context 命中即复用、成功后登记、失败不存半成品；共享名义 Scene 不改状态；运行引用在包内、不读取 mesh 内容；不改变样例真实几何、位姿、关节与模型资源；不扩张 tools 原型。
- 已验证公开契约允许空规划关节列表；context 当前没有公开资源集合访问器；现有样例没有 bundle.yaml，目录 tabletop 与 scene_id 不同。
- 协调 agent 报告 Docker dev healthy、Python 3.13.15，基线四组共 61 测试通过；本 agent 未独立运行这些测试。

## D4-1：独立多维分布表示

公开模块 `multiarm_problem_gen.distributions`：

```python
UniformDistribution(*, lower: tuple, upper: tuple)
GaussianDistribution(*, mean: tuple, stddev: tuple)
# 同名字段只读；dimension: int 只读，由向量长度导出。
```

两者均是分量独立的联合分布，无采样 API、场景引用或 I/O。相应参数必须是等长 tuple；接受 int／float，拒绝 bool、其他类型、非有限值及不能转成有限 float 的大整数；保存 float tuple，不改变输入。非法类型为 TypeError，非法长度／数值为 ValueError，错误指出字段。

允许零维 `()`，不另接受显式维度，因此没有负维度入口；一维是普通特例。每维 `lower <= upper`、`stddev >= 0`，允许退化成确定值。保留顺序，不排序、合并或推断分量含义。对象与参数不可原地修改；不承诺相等、哈希或序列化。

**理由与排除方案：**空规划关节列表已有合法的完整空状态，零维分布可自然表示它，避免下游制造特殊伪关节；退化参数能表达固定值而不引入第三种分布。拒绝严格正维度、严格区间和严格正标准差方案；拒绝显式维度重复保存及提前加入采样器。没有既有分布 API 兼容性负担。

**修改范围：**新的 distributions 模块、其专属测试、`docs/contracts/distributions.md` 及本轮必要文档入口；不读取其他模块内部。

**验收：**空／一／多维构造与维度；独立算例的顺序和值；退化合法；反界、负标准差、长度不匹配、bool、字符串、list、NaN／Inf／巨大整数失败；只读、输入不变、无文件访问和无采样入口。测试通过只证明参数表示契约，不证明采样分布或统计性质。

## 阅读、用量与时间

实际读取：研究仓库 `overview.md`、`state.md`、`projects/README.md`；目标仓库 `AGENTS.md`、`README.md`、`docs/README.md`、`docs/design.md`；四份指定讨论记录（实现单元、读取流程、Generation 分布、InputBundle）；现有四份 `docs/contracts/*.md`；样例 README、tabletop/scene.yaml、tabletop/generation.yaml。一轮合并工具输出截断了 resources／robot-model 契约，随后单独重读两份完整契约。未读取模块内部、内部测试或 tools 实现。父 agent 的信息包属于已有上下文，并非独立证据。

工具 UTC 起点：2026-09-30 12:59:26。目前阶段为阅读与设计；本 agent 没有实现／测试阶段。结束时补实际墙钟区间；token 用量不可用，不按文本长度估计。

## D6-1：先补公开资源快照

由**独立 resources 实现 agent** 承担最小补丁：`ResourceContext.meshes: Mapping[Path, MeshResource]`、`robot_models: Mapping[Path, RobotModel]`、`scenes: Mapping[Path, Scene]` 三个只读属性。每次访问取得当时已成功登记资源的只读映射快照，键为规范绝对路径；保留资源引用身份，按首次成功登记顺序迭代。先前快照不随之后加载变化，不能赋值／删除属性或修改映射。直接 reader 的自身结果仍不登记；它通过 context 成功取得的依赖可见。失败加载不出现半成品，之前成功依赖仍可见。原有加载和路径契约不变，无手动登记／清空／替换 API。

**理由与排除方案：**InputBundle 需要准确交付本次加载集合；遍历 Scene 公开图收集易漏掉依赖资源，并重复表达资源管理逻辑。只读快照最小且使调用者不依赖缓存内部，拒绝公开可变字典或让 BundleReader 访问私有表。

**修改范围：**既有 resources 所属实现、其专属测试、`docs/contracts/resources.md`。由该 agent 读取自己的实现；其他 agent 只读此决定和更新后的公开契约。可与 U4 并行，但 U6 以此补丁完成为依赖。

**验收：**三类空快照；加载后的键、身份与顺序；同一路径复用不增条目；快照不可修改且不随后续加载变化；加载失败不登记半成品但保留已成功依赖；直接 reader 不登记自身；原资源测试回归。测试只证明集合与登记时序，不加载 mesh 内容。

## D5-1：保留 YAML，公开统一作用关联

选择现有 `0.1-draft` YAML 组织，不增加第二套显式 binding 输入格式。现有样例可原样读取；内部公开表示为已解析的关联，不保留需要调用者重新解释的 YAML 名称。新增 `multiarm_problem_gen.generation`：

```python
read_generation(*, generation_path: Path, resources: ResourceContext) -> Generation
SamplingBinding(*, distribution, target, property, components)
GoalTolerance(*, position_distance_m, orientation_angle_rad)
Completion(*, return_to_initial_configuration, joint_tolerance_rad)
Generation(*, scene, bindings, sequences, seed, sample_count,
           visit_goal_type, goal_tolerance, completion, status=None)
```

同名字段公开只读。`bindings` 为 SamplingBinding tuple；`sequences` 为 `Mapping[str, tuple[Frame, ...]]` 只读快照，键是本场景机器人 ID。关联保留原对象身份，不复制、不修改 Scene、Frame、RobotInstance 或 RobotModel。集合不暴露可变容器；不承诺相等、哈希或序列化。公开直接构造同样检查下述结构、数值及关联不变量（不重复验证 RobotModel 内部）。类型错误 TypeError，非法数值／关联 ValueError。

`SamplingBinding.distribution` 仅为 D4-1 的两种分布；`property` 是明确类别字符串，只允许 `frame_position`、`frame_orientation`、`initial_joint_positions`，不提供应用方式开关。前两者 target 为 Frame，components 为非空、不重复的 tuple：位置选自 x/y/z，朝向选自 alpha/beta/gamma。初始状态 target 为 RobotInstance，components 为不重复规划关节名 tuple，可为零维（仅目标规划列表本身为空时）；distribution.dimension 必须等于 components 长度。Generation 校验 target 是其 scene 中的原对象，禁止 world；同一 target／property／component 重复绑定拒绝。直接构造可拆为多个不重叠的初始 binding，但每个机器人必须存在初始 binding，合计恰好覆盖全部规划关节；零规划关节机器人使用一个空 binding。

位姿 binding 仍限定均匀分布；初始状态支持均匀／高斯。初始值表示实际关节值，不能再加命名中心；位姿含义为此前确定的名义自身坐标增量和固定轴旋转参数，本阶段只表示，不应用。直接构造 bindings 保留调用者顺序；components 明确决定分布输出顺序。初始 binding 不修改 planning_joint_positions，读取后名义状态仍为 None。

**理由与排除方案：**显式 binding YAML 更灵活，但当前独立均匀／高斯及样例已经足够表达需求，迁移会增加字段与格式成本。保留输入结构与统一领域表示并不矛盾。暂不支持输入中自由拆分初始 binding，不添加基座扰动格式或分布复用名称表。

## D5-2：精确 YAML、顺序、参数与状态边界

顶层必需 `schema_version=0.1-draft`、`scene`、`seed`、`sample_count`、`initial_state_sampling`、`sequence_generation`、`visit_goal_type`、`goal_tolerance`、`completion`；可选 `status`、`scene_perturbations`、`target_perturbations`。后两者缺失为 `{}`；status 缺失保存 None，存在须非空字符串，仅作元数据，不限制词表、不推导有效性或执行策略。seed 为非负 int，sample_count 为正 int，均拒绝 bool；seed 必需且不另设随机后端范围上限，本轮不使用它。

scene 是相对文件引用，由 context 解析并 `get_scene` 取得。reader 只返回 Generation、不登记自身，且不同文件可引用同一 Scene。generation_path 只接受包内可读普通文件的绝对 Path，resources 须为 ResourceContext。公开调用类型错误 TypeError；文件、YAML、字段、数值、引用和一致性错误为现有 InputReadError，包含源文件／location／message；依赖错误保留原源文件与位置。全层拒绝未知字段、重复键、显式 null 和非法类型。数值遵循有限 int／float、拒 bool；YAML 映射键须字符串。

- `scene_perturbations` 为物体 ID → 属性分布的映射，仅引用 `scene.objects`。`target_perturbations` 为显式 frame ID → 属性分布；显式 frame 是 frames 中排除 world、所有物体与机器人安装 frame 后的成员。两类目标互斥，不接受前缀别名、未知目标或机器人基座。每个目标至少有 position/orientation 之一，属性不得为空。
- 位姿属性的分布必需且只允许 `type: uniform`、`independent: true`、lower、upper。lower/upper 为相同非空键集合，位置键选自 x/y/z、旋转键选自 alpha/beta/gamma；均匀 bounds 允许相等。YAML 的键顺序不定义分量顺序，reader 统一按上述标准轴顺序。binding 顺序为 scene_perturbations 后 target_perturbations 后 initial_state_sampling；各组目标按输入映射顺序，每个位姿目标 position 先于 orientation。
- `initial_state_sampling` 恰好覆盖场景所有机器人（无机器人时为 `{}`）。每个值必需 type、independent=true。uniform 另外且仅有 lower/upper 两个关节映射；gaussian 另外且仅有 mean/stddev。关节映射必须恰好覆盖 planning_joints，按模型规划关节顺序转换 tuple，与 YAML 键顺序无关；零关节时合法映射是 `{}`。
- gaussian mean 可为完整关节值映射，或且仅为 `{configuration: <非空命名配置名>}`。后者必须存在于该目标 model.configurations，解析为数值 tuple；不在 Generation 中保留待解析的命名引用。stddev 是完整规划关节映射，允许零。配置名不存在、错模型关节、缺失／额外关节均拒绝。
- 分布参数合法不等于采样状态合法：**不因 uniform bounds／gaussian mean 越过关节限位而拒绝或裁剪参数**，也不要求高斯支持集落入限位。命名配置合法性已由模型读取保证；显式中心只是分布参数。此决定使两类分布保持同一表示层边界，越界样本后续如何处理未决定，读取成功不能宣称样本有效。
- `sequence_generation` 仅 `type: fixed` 与 sequences。sequences 恰好覆盖所有机器人，每项为显式 frame ID 的 YAML 列表，按列表顺序保存原 Frame；允许空访问列表和重复访问（返回初始规则仍成立）。未知机器人／frame、world、实例安装／物体 frame 拒绝。同一 frame 跨臂或重复使用保留同一引用，不产生副本；不同臂同序号不表示同步。
- `visit_goal_type` 仅 `end_effector_pose`。goal_tolerance 必需且仅有 `position_distance_m=0.001` 与 `orientation_angle_rad=0.017453292519943295`。completion 必需且仅有 `return_to_initial_configuration=true` 与 `joint_tolerance_rad=0.001`。数值转换后须等于既定常量，不开放可配容差；不支持 false、额外保持／停留／到达速度开关。完成后停留在该样本实际初始配置，继续参与碰撞检测，是语义约定而非本轮计算。三个辅助表示构造也执行相同限定。

**兼容性：**现有 generation.yaml 全字段得以保留；原示例 status 仅表达未完成验证。严格拒绝旧样例未使用的新字段和基座扰动。固定容差沿用已确认首版语义；开放容差、采样拒绝／裁剪策略和新目标类别需后续单独决定。

**修改范围：**新 generation 模块、其专属测试、小型测试输入、`docs/contracts/generation.md` 与必要入口及实施记录；不改依赖模块内部、真实模型或样例数值。仅消费 distributions／scenes／robots／resources 的公开契约。

**验收：**手算映射验证轴及规划关节顺序、命名中心解析、目标和序列引用身份、部分位姿／完整初始覆盖、空规划与空场景、重复访问、跨臂共享、非同步语义；多份 generation 共享 Scene 且状态不改；覆盖所有严格错误与位置诊断、绑定重叠／异场景对象、参数越限仍可表示、退化分布、seed/count/status/容差/完成条件。读取真实样例并核对双臂六维、四次访问、具体名义输入不变。测试只证明读取／表示，不证明无碰撞、IK 或随机可行性。

## D6-2：输入包公开入口与严格发现

新增 `multiarm_problem_gen.bundles`，公开 `BundleReader`、`InputBundle`、现有 `InputReadError`：

```python
BundleReader()
reader.read(root: Path) -> InputBundle
# InputBundle 公开只读字段：
# root: Path
# meshes: Mapping[Path, MeshResource]
# robot_models: Mapping[Path, RobotModel]
# scenes: Mapping[str, Scene]
# generations: Mapping[Path, Generation]
```

InputBundle 的构造／交付入口仅承诺 BundleReader.read，不新增手工组装契约。每次 read 新建一个 ResourceContext，不保存跨次缓存；root 为规范绝对目录 Path。所有集合只读快照、资源与 scene 保留原对象身份；不进行深冻结或复制可变 Frame／实例。资源集合取 D6-1 公开快照；scenes 按 scene_id 查询，generations 按规范绝对 generation 文件路径查询。Generation 当前没有 ID，不臆造 generation_id；同名 generation.yaml 在不同场景目录是不同条目。InputBundle 不公开可变 context。

根文件固定 `bundle.yaml`，必需且仅有 `scene_directories`，为非空 YAML 字符串列表；不添加 schema_version 或自动扫描备用规则。重复键、未知字段、null、非字符串／空字符串条目拒绝。root 参数非 Path 为 TypeError；其他文件系统、YAML、重复及关联错误为 InputReadError，包含源文件与位置；读依赖失败保留依赖来源。成功才返回完整 InputBundle，失败不返回半成品，也不改输入文件。

**目录解析不扩展 context API：**将每个相对目录引用与 `scene.yaml` 拼接后，调用 `context.resolve_file(reference, relative_to=bundle_path)`。沿用包内 `..` 允许、绝对／URI／包外目标拒绝及符号链接规范化规则；不得访问 context 私有函数。解析后的 scene_path.parent 是实际场景目录，也是 generation 发现目录；它的末级目录名必须等于 scene.scene_id。符号链接别名不会另创目录身份；如果目录或 scene.yaml 经符号链接指向另一个包内目录，就以实际 scene 文件所在目录为准。

场景按 scene_directories 列表顺序读取；规范 scene_path 重复立即拒绝（包括重复文本、`..` 别名和符号链接）。不同规范场景路径使用同一 scene_id 也拒绝。每个实际场景目录只发现直属 `generation.yaml` 和 `generation_*.yaml`，不递归；两种模式取并集、按文件名字典序读取。匹配路径必须可读普通文件且规范后在包内，目录伪装成匹配名字也报错，不静默忽略；不匹配文件不读取。每个场景**至少一份**匹配的 generation，否则失败；不要求一定存在 generation.yaml。

每份 generation 通过公开 read_generation 读取，返回的 `generation.scene` 必须 `is` 此目录 context.get_scene(scene_path) 的对象；这校验显式引用指向本目录 scene 的规范文件身份。各 generation 规范路径不得重复（同目录／跨目录符号链接别名也拒绝）。输入包不自动合并多份生成规则，不给缺失初始分布补默认。

共享资源按规范路径复用；meshes 与 robot_models 的顺序沿用 context 首次成功登记顺序。不同配置路径若产生相同 model_id，**InputBundle 层拒绝模型 ID 冲突**；context 仍保持原有“不同路径不按 ID 合并”的契约，独立读模型仍可得到不同对象。mesh 没有 ID 冲突规则；不同路径即不同资源。不同场景复用同一配置路径的 model_id 不算冲突。相同对象实例 ID／frame ID 只需在各自 Scene 内唯一，不跨场景禁重。

**理由与排除方案：**严格枚举与至少一份规则，使一个已声明场景不会被静默忽略；generation 无既有 ID，路径是无需改格式的自然标识。拒绝排序场景目录（会丢失声明次序）、默默去重、按内容合并、全资源目录扫描及跨 context 缓存。不增加 resolve_directory API，现有公开文件解析足够完成本阶段发现。模型 ID 唯一性只约束完整包交付，避免未来按模型 ID 输出时出现歧义，不借此改变资源共享机制。

## D6-3：真实样例最小迁移与验收

为 `examples/ur7e_table` 新增 `bundle.yaml`：

```yaml
scene_directories:
  - inputs/tabletop
```

仅将 `inputs/tabletop/scene.yaml` 的 scene_id 从 `ur7e_table_baseline` 改为 `tabletop`，其他数值／几何／位姿／关节／模型／frame／generation 字段不变；更新样例 README 明确 bundle 入口与 generation 单独读取入口。理由：目录重命名会改变既有文件入口和工具路径，另建完整样例会复制真实模型资源。scene_id 是逻辑命名而非物理数据，改名影响按旧 ID 查找的调用者，文档必须注明；不去改写历史检查结果或 tools 原型。本迁移必须在实施时检查差异，证明没有混入真实数据变更。

**修改范围：**新 bundles 模块、其专属测试及小型测试资源、`docs/contracts/input-bundle.md`、上述样例两项输入／README、必要文档入口与实施记录。resources 扩展由 D6-1 的专属 agent 完成；U6 不修改其内部。只消费公开依赖契约，不读取依赖内部测试。

**验收：**多场景／多 generation 的确定顺序；同模型／mesh 共享身份；Generation.scene 身份；只读集合与绝对规范路径；缺根配置／缺目录或scene／缺generation／损坏依赖、目录名不等scene_id、scene/model ID 冲突、规范重复路径、未知字段／重复键／null、错误 generation.scene、绝对／URI／包外引用及符号链接逃逸；包内符号链接别名按规范身份处理；不加载未声明目录或无关资源。真实包完整读取、共享双臂 RobotModel 和 mesh、保留初始 None 状态；搬移整个真实输入包到临时目录后再次读取，核对路径全部迁移至新根且引用仍一致。输入文件不改、mesh 内容未被打开。相关依赖回归通过；不执行采样／场景复制／计算／输出，不宣称随机样本有效。

### 补充精度与阶段记录

D5-1 的“同样检查”包括 frame 目标类别：直接构造 Generation 也不接受机器人安装 frame 的位姿 binding；frame 位姿 target 只能为本场景物体 frame 或显式 frame。序列也仅引用本场景显式 frame。SamplingBinding 单独构造可以检查参数类别／维度，归属及安装 frame 排除由 Generation 检查。

首轮决定结束工具时间为 2026-09-30 13:04:05 UTC；自 12:59:26 起墙钟 4 分 39 秒，涵盖读取、分析、协调与决定记录写入，无法可靠拆分成各单元设计用时；无代码实现／测试执行／等待用户阶段。token 用量不可用。尚未验证这些新契约的实现可行性；后续实现若发现缺口应记录具体证据并交本 agent 复议，不把本记录改写成验收结果。

## D5-3：mean 的 configuration 名称消歧

协调 agent 初审指出：公开 RobotModel 契约不保留 `configuration` 关节名，因此直接按键名识别命名中心会误拒绝合法显式中心。采用结构与值类型共同判别：**仅当 mean 恰有一个键 `configuration`，且该值为字符串时**按命名配置引用处理（字符串仍须非空且命名配置存在）；其他 mapping 按完整关节数值映射处理。

因此单规划关节恰名为 configuration 时，`mean: {configuration: 0.25}` 是合法显式中心，`mean: {configuration: home}` 是命名 home 中心；多关节中的 configuration 数值键也正常。bool／null／容器不会被转换成命名引用；走显式中心数值校验并拒绝。未知或额外字段仍按对应分支严格拒绝。此规则不增加保留关节名、不改变现有样例；验收加入上述两例及非法值，避免实现默默选择一种解释。

首轮审阅补充至 13:05:00 UTC（工具时间）：额外 55 秒用于 D5-3 消歧、直接构造边界澄清与文件检查；总墙钟 5 分 34 秒。新增决定文件 144 行（追加本句前的工具统计）；仅记录文件发生本 agent 写入，无代码、提交或测试产物。

## D6-4：既有真实样例测试的单字符串维护

协调 agent 提供新验证事实：精确搜索旧 scene_id 发现 `tests/scenes/test_scenes.py:424` 存在唯一当前测试预期 `self.assertEqual(scene.scene_id, "ur7e_table_baseline")`。本决策 agent 未打开该模块内部测试；上述一条断言由信息包进入上下文，记录此来源，不把它算作纯公开契约材料。

决定由**主 agent** 将该断言的预期字符串单独改为 `tabletop`，归属为 D6-3 样例元数据迁移的集成验收维护，不是场景单元实现。不新建场景实现／维护子任务；U6 agent 仍不得读取或修改这个依赖内部测试。

修改严格限制为这条已定位断言的一处字符串，不删除断言、不放宽比较、不调整真实输入数值或其他测试逻辑。主 agent 检查精确替换与差异；若文件已变化、匹配不唯一或需要额外逻辑修改，返回决策，不扩大范围。可以执行完整场景测试组及相关集成回归，执行依赖测试不等于阅读其内部。

理由：预期旧逻辑 ID 已因授权的样例迁移而过时，同步新 ID 恢复验收对象一致性；新建 agent 会增加不必要交接，也不能带来额外领域判断。测试仍验证确定的 scene_id，未削弱契约。兼容性影响仍仅是按旧场景 ID 查找的调用者需要同步，不改变读取或物理语义。

本追加阶段开始工具时间为 2026-09-30 13:05:41 UTC；与首轮分开计时，中间空档不累计。无实现或测试执行，token 用量不可用。

本追加阶段结束工具时间 2026-09-30 13:05:58 UTC，墙钟 17 秒，活动为证据判断与决定写入；不重复计入首轮 5 分 34 秒，也不含随后写入本计时句的时间。
