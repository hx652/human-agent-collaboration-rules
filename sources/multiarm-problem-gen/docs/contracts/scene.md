# 场景表示与读取公开契约

依据[单元 3 方案](../notes/discussions/2026-09-30-unit-3-scene-and-resource-context.md)，依赖[基础表示](primitives.md)、[机器人模型](robot-model.md)和[资源管理](resources.md)。本契约覆盖名义场景读取、关联与实例状态，不包含复制、采样或计算后端。

## 公开入口与表示

从 `multiarm_problem_gen.scenes` 导入以下类、`read_scene` 和 `InputReadError`。构造均使用关键字参数：

```python
read_scene(*, scene_path: Path, resources: ResourceContext) -> Scene
Scene(*, scene_id, world, frames, robots, objects, rules)
RobotInstance(*, id, model, frame, planning_joint_positions=None)
Object(*, id, frame, collision_shapes)
SceneRules(*, environment_motion, allowed_mount_contacts=())
MountContact(*, robot, link, object)
```

字段按以上名称公开读取。`scene_id` 和实例／frame ID 为不含 `/` 的非空字符串。

- `Scene.world` 是无父节点、单位 Pose 的 `Frame(id="world")`。`frames: Mapping[str, Frame]` 包含 world、物体 frame、安装 frame 和显式 frame；`robots: Mapping[str, RobotInstance]`、`objects: Mapping[str, Object]` 按实例 ID 查询。
- 所有映射保存只读快照；几何与接触集合接受 tuple。身份、集合及关联不可赋值或删除。关联保留引用身份，不复制 Frame、模型或 Geometry。不承诺相等性、哈希或序列化。
- `RobotInstance.model` 为共享 RobotModel；`frame` 与 model.root_link 重合，是相对父 frame 的安装位姿。`Object.frame` 为物体自身参考系，`collision_shapes` 为非空 Geometry 元组。两者不另存 pose。
- `SceneRules.environment_motion` 仅为 `static`：任务执行期间环境不动，生成阶段仍可扰动。`allowed_mount_contacts` 为 MountContact 元组，条目中的 robot、link、object 分别引用本场景实例、该模型的 Link 和本场景物体；相同 robot/link/object 三元组不得重复。它仅表示后续可忽略该 link—object 碰撞，不豁免整条臂，不建立运动约束或证明实际接触。
- 直接构造检查类型、ID、集合成员及上述关联；Scene 检查映射键与 ID 一致、统一名称空间、frame 连通无环、成员及接触引用身份。错误类型为 TypeError，非法值或关联为 ValueError。它不重新验证 RobotModel 内部结构。

`robot.planning_joint_positions` 可整体赋值为 None 或完整数值 tuple，按 `model.planning_joints` 顺序。None 表示未指定；空规划列表的已指定值为 `()`。构造与赋值均检查长度、int/float（拒绝 bool）、有限数值及每个规划关节的 `limits.effective_lower/effective_upper`，保存 float tuple；失败保持旧状态。读取名义输入始终为 None，不补零，不采用命名配置。固定值及 mimic 关系仍在模型中，不展开完整状态，不保证全部 mimic 限位、碰撞或可达性。

`Frame.pose` 沿用基础表示的整体更新。world 仅在构造／读取时检查单位位姿，调用者按约定保持不变，不增加 Frame 特例保护。共享名义 Scene 供多份 Generation 使用；生成过程须另建独立可变 frame 和实例状态，本轮不提供复制能力。

## Frame 名称与引用

机器人和物体的 frame 直接使用实例 ID；显式 frame 使用自身 ID。名称不加前缀，声明、`Frame.id`、查找键和引用完全一致。三类声明在场景内统一唯一，均不得占用 `world`。reader 不迁移旧前缀或创建别名。

父引用可指向任意场景 frame，允许前向引用；必须存在、无环，最终连接到唯一 world。机器人内部 Link 不进入该名称空间，不支持内部 link frame 引用。

## YAML 输入

沿用 `examples/ur7e_table/inputs/tabletop/scene.yaml` 的 0.1-draft 字段组织：

| 位置 | 必需字段 | 可选字段／默认 |
|---|---|---|
| 顶层 | schema_version=`0.1-draft`、scene_id、world_frame=`world`、robots、objects、frames、environment_motion=`static` | allowed_mount_contacts=[] |
| robots[] | id、config、pose | 无；不接受规划关节状态覆盖 |
| objects[] | id、representation=`compound`、pose、collision_shapes（非空列表） | 无 |
| 实例 pose | reference_frame、position_xyz、quaternion_xyzw | 无 |
| frames[] | id、parent_frame、pose | 无 |
| 显式 frame pose／几何 local_pose | position_xyz、quaternion_xyzw | 无 |
| collision_shapes[] | geometry | local_pose 省略为单位 Pose |
| geometry（box） | type=`box`、size_xyz | 无 |
| geometry（sphere） | type=`sphere`、radius | 无 |
| geometry（cylinder） | type=`cylinder`、radius、height | 无 |
| geometry（mesh） | type=`mesh`、uri | scale_xyz 省略为 (1,1,1) |
| allowed_mount_contacts[] | robot、link、object | 无 |

robots、objects、frames 明确为列表，可空；其他数值向量为 YAML 列表，reader 转成 tuple 后遵循基础表示的长度、有限性、正值和四元数归一化规则。几何位置相对所属物体，mesh 保留资源原点；长度为米、角度为弧度、右手系、四元数为 xyzw。

所有层级拒绝未知字段、重复键、显式 null、非法类型与数值。文件引用相对包含引用的 scene 文件解析，遵循 context 的包内路径约束。reader 通过 context 取得模型与 mesh，不加载 mesh 内容。

`scene_path` 接受包内可读普通文件的绝对 Path；`resources` 为 ResourceContext。公开调用的参数类型错误为 TypeError；文件、YAML、数值、结构和引用错误为 InputReadError（ValueError 子类），含 source_path、location、message。依赖读取失败保留依赖自己的源文件与位置，场景引用路径错误定位到本 scene 的引用字段。成功才返回完整 Scene，不写输入。

直接 `read_scene` 每次读取并返回独立实例和 frame，不登记自身结果；依赖可在 context 中共享。需要共享名义 Scene 时使用 `context.get_scene(path)`：命中返回已有对象，未命中调用 reader，成功后登记；失败不登记半成品，此前成功取得的依赖可保留。

目录名与 scene_id 一致性、Generation 序列与覆盖、有关节物体、link frame 引用、世界位姿、FK／IK、碰撞和采样均不在本轮保证内。验收命令见 [Docker 说明](../../docker/README.md)。
