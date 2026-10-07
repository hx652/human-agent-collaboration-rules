# Generation 表示与读取公开契约

本轮探索性实现依据[单元 5 公开交接包](../notes/discussions/2026-09-30-unit-5-public-handoff.md)的 D5-1/2/3，不代表用户最终接受设计。依赖仅为 [分布](distributions.md)、[场景](scene.md)、[机器人](robot-model.md)、[基础表示](primitives.md)和[资源管理](resources.md)公开契约。

```python
from multiarm_problem_gen.generation import (
    Generation, SamplingBinding, GoalTolerance, Completion, read_generation,
)
read_generation(*, generation_path: Path, resources: ResourceContext) -> Generation
SamplingBinding(*, distribution, target, property, components)
GoalTolerance(*, position_distance_m, orientation_angle_rad)
Completion(*, return_to_initial_configuration, joint_tolerance_rad)
Generation(*, scene, bindings, sequences, seed, sample_count,
           visit_goal_type, goal_tolerance, completion, status=None)
```

## 表示与关联

同名字段公开只读，集合为 tuple 或只读映射快照；保留关联对象身份，不复制或修改 Scene、Frame、RobotInstance、RobotModel。不承诺相等、哈希或序列化。公开构造检查类型及下列不变量，类型错误 TypeError，非法值或关联 ValueError；不重复验证 RobotModel 内部。

SamplingBinding.distribution 是 UniformDistribution 或 GaussianDistribution。property 只允许 frame_position、frame_orientation、initial_joint_positions。位姿 target 为 Frame，仅支持均匀分布；components 为非空、不重复 tuple，位置来自 x/y/z，旋转来自 alpha/beta/gamma。初始 target 为 RobotInstance，components 为不重复规划关节名 tuple；仅零规划关节目标允许空 tuple。dimension 必须等于 components 长度。components 定义分布输出顺序，直接构造保留调用者顺序。

Generation.scene 为名义 Scene；bindings 为 SamplingBinding tuple，并按传入顺序保存。位姿 target 必须是本场景物体或显式 frame 原对象，禁止 world 和机器人安装 frame；初始 target 必须是本场景 RobotInstance 原对象。相同 target/property/component 不得重叠。每个机器人必须存在初始 binding，其分量合计恰好覆盖所有规划关节；直接构造允许不重叠拆分，零关节机器人须有一个空 binding。

sequences 是 Mapping[str, tuple[Frame, ...]] 快照，恰好覆盖本场景机器人，Frame 仅为本场景显式 frame。显式 frame 指 frames 排除 world、物体和机器人安装 frame。空序列、重复访问、跨臂共享目标合法，保留原对象；同序号不表示同步。

seed 必需非负 int，sample_count 必需正 int，拒绝 bool，不设置 seed 后端上限。status 缺失为 None，存在为非空 str，仅作元数据。visit_goal_type 仅 end_effector_pose。GoalTolerance 固定 position_distance_m=0.001、orientation_angle_rad=0.017453292519943295；Completion 固定 return_to_initial_configuration=True、joint_tolerance_rad=0.001。数值接受有限 int/float，拒 bool；转成 float 后须等于对应常量。

位姿表示名义自身坐标增量与固定轴旋转参数，不在本轮应用。初始分布数值是实际关节值，不再叠加命名中心。完成后返回该样本实际初始配置并继续参与碰撞检测，是后续执行语义，本轮没有该计算。参数可以越过关节限位，不裁剪、不拒绝高斯支持集；表示合法不等于状态有效。

## 严格 YAML

顶层必需 schema_version=0.1-draft、scene、seed、sample_count、initial_state_sampling、sequence_generation、visit_goal_type、goal_tolerance、completion；可选 status、scene_perturbations、target_perturbations。扰动分组缺失按 {}，status 缺失按 None。所有层级拒绝未知字段、重复键、显式 null、非字符串映射键和非法类型；数值有限且拒 bool。

- scene 相对包含引用的 generation 文件解析，通过 resources.get_scene 共享取得名义场景。reader 不登记自身结果。
- scene_perturbations 是物体 ID 到属性分布的映射；target_perturbations 是显式 frame ID 到属性分布的映射。每个目标至少有 position/orientation 之一，不支持机器人基座、world、前缀别名。
- 位姿属性必需且仅有 type=uniform、independent=true、lower、upper。两界为相同非空轴键集合，位置 x/y/z，旋转 alpha/beta/gamma；允许相等边界。reader 按标准轴顺序而非 YAML 键顺序组织分量。
- 初始分组恰好覆盖所有机器人。每项 type 与 independent=true 必需；uniform 另有且仅有 lower/upper，gaussian 另有且仅有 mean/stddev。关节映射恰好覆盖规划列表，reader 按模型规划顺序组织，零维为 {}。stddev 允许零。
- 仅 mean 恰为单键 configuration 且值为字符串时，解析为目标模型的命名配置；名称须非空且存在。其他 mean 按完整关节数值映射处理，因此同名规划关节 configuration 的数值合法。结果仅保留数值 tuple。
- sequence_generation 必需且仅有 type=fixed、sequences。sequences 恰好覆盖机器人，每项为显式 frame ID 列表，允许空列表和重复目标。
- goal_tolerance、completion 恰有上述固定字段和值，不开放新开关。

reader 的 binding 顺序为 scene_perturbations、target_perturbations、initial_state_sampling；组内目标按 YAML 映射顺序，位姿目标 position 先于 orientation。

generation_path 接受包内可读普通文件的绝对 Path；resources 为 ResourceContext。公开调用类型错误 TypeError；文件、YAML、字段、数值、引用或一致性错误为 InputReadError（可从本模块导入），包含 source_path/location/message。场景引用解析失败定位 generation 的 scene 字段；依赖读取失败保留依赖源文件和位置。成功才返回完整 Generation，不写输入，名义状态和 frames 保持原样。

## 验证边界

验收：`python -m unittest discover -s tests/generation -v`，在[仓库 Docker 环境](../../docker/README.md)执行。检查表示、严格读取、映射顺序、身份共享、状态不变和真实输入；不保证采样统计、随机可行性、FK/IK 或无碰撞。本轮没有采样、场景复制、运动学或执行 API。
