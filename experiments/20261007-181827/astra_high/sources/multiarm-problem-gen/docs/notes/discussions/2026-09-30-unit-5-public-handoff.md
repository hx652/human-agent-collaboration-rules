# 单元 5 公开交接包

从独立决定 D5-1/2/3 摘取，供严格隔离实现阅读；不包含依赖内部或内部测试。原始决定与复议保存在 autonomous-units-4-6-decisions 同日记录。探索性 agent 决定，不代表用户接受。

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


## D5-3：mean 的 configuration 名称消歧

协调 agent 初审指出：公开 RobotModel 契约不保留 `configuration` 关节名，因此直接按键名识别命名中心会误拒绝合法显式中心。采用结构与值类型共同判别：**仅当 mean 恰有一个键 `configuration`，且该值为字符串时**按命名配置引用处理（字符串仍须非空且命名配置存在）；其他 mapping 按完整关节数值映射处理。

因此单规划关节恰名为 configuration 时，`mean: {configuration: 0.25}` 是合法显式中心，`mean: {configuration: home}` 是命名 home 中心；多关节中的 configuration 数值键也正常。bool／null／容器不会被转换成命名引用；走显式中心数值校验并拒绝。未知或额外字段仍按对应分支严格拒绝。此规则不增加保留关节名、不改变现有样例；验收加入上述两例及非法值，避免实现默默选择一种解释。

首轮审阅补充至 13:05:00 UTC（工具时间）：额外 55 秒用于 D5-3 消歧、直接构造边界澄清与文件检查；总墙钟 5 分 34 秒。新增决定文件 144 行（追加本句前的工具统计）；仅记录文件发生本 agent 写入，无代码、提交或测试产物。


直接构造 Generation 也排除安装 frame 的位姿 binding；仅本场景物体和显式 frame 可用。序列仅为本场景显式 frame。
