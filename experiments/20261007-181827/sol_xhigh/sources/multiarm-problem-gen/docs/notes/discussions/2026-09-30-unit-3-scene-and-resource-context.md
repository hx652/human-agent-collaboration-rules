# 单元 3：场景表示、读取与统一资源管理方案

日期：2026-09-30。

状态：依据本轮讨论保存的实施前方案，尚未实现。本次仅写入方案、评估实施准备情况并提供后续任务 prompt，不开始代码实现。已确认的职责与范围按下文执行；候选字段和签名在实施开始时具体化为公开契约，不将未来接口的未决规则当作决定。

依据：[实现单元划分](2026-09-29-input-implementation-units.md)、[领域表示讨论](2026-09-22-input-domain-representations.md)、[读取流程](2026-09-28-input-reading-flow.md)。已实现依赖见[基础表示](../../contracts/primitives.md)、[资源接口](../../contracts/resources.md)、[机器人模型](../../contracts/robot-model.md)契约。

## 目标与范围

单元 3 将一份 scene.yaml 读取为关联完整的 Scene，同时扩展 ResourceContext，统一管理路径、MeshResource、RobotModel 和名义 Scene。以现有双臂桌面样例为基线，支持基本形状、mesh、组合物体、安装 frame、显式命名 frame 和场景规则。

本轮暂缓有关节环境物体和机器人内部 link frame 引用。不实现场景复制、采样、世界位姿计算、FK／IK、碰撞计算、Generation 及完整 InputBundle 读取。资源管理能力提前交付，目录发现仍归单元 6。

## 场景表示与状态

候选公开字段如下；集合采用只读映射或元组，具体构造签名先整理到场景契约。

| 表示 | 主要字段与职责 |
|---|---|
| Scene | scene_id、world、frames、robots、objects、rules，组织完整场景 |
| RobotInstance | id、共享 model、安装 frame、planning_joint_positions |
| Object | id、自身 frame、collision_shapes（Geometry 元组） |
| SceneRules | environment_motion、allowed_mount_contacts |
| MountContact | 对具体 RobotInstance、该模型内 Link 和场景 Object 的引用 |

robots、objects 按实例 ID 查询，frames 包含全部场景 frame，直接按无前缀名称查询；同一对象经不同入口取得时保持引用身份一致。成员集合、身份和关联只读。安装 Frame 与模型 root_link 重合；机器人和物体位姿只存在对应 Frame 中，不另存 pose。

规划关节状态以 None 表示未指定，完整数值元组按 model.planning_joints 顺序表示已指定状态。名义场景读取后使用 None，不补零、不自动采用命名配置。状态允许整体替换，构造和更新检查维度、有限数值及规划关节有效限位，拒绝布尔值，失败保留原状态。固定关节值和 mimic 关系继续来自模型；本轮不展开完整关节状态，也不保证全部 mimic 限位、碰撞或可达性。

Frame.pose 沿用基础表示的整体替换能力。名义与具体场景复用表示，但可变 Frame 和实例状态必须独立；模型、Geometry 和 mesh 可以共享。场景复制功能留到生成阶段。

## Frame 关系

Frame 名称不添加类别前缀，声明、Frame.id、frames 查找键和引用使用同一个名称：

| 名称 | 含义 |
|---|---|
| world | 场景根坐标系 |
| can_a | 物体自身坐标系，直接使用物体 ID |
| arm_a | 机器人安装坐标系，直接使用机器人实例 ID |
| work_area | 显式命名的辅助或目标坐标系，直接使用其 ID |

输入 ID 为不含 / 的非空字符串。所有 frame 名称在 Scene 内统一唯一，因此机器人实例 ID、物体 ID、显式 frame ID 之间也不能重名；world 为根名称，其他声明不得占用。reader 不增加、去除或推断类别前缀，不为旧前缀建立别名。

2026-09-30 按用户要求先完成样例名称调整：scene.yaml 的四处 parent_frame 已从 object/can_a、object/can_b 改为 can_a、can_b，位姿和其他输入内容保持不变。后续实现直接使用该样例，不再执行迁移；这项输入调整不代表场景读取已经实现。原型工具对旧引用格式的依赖需要另行核对，不因本方案而宣称其兼容性已验证，也不自动扩大到原型代码修改。

物体、安装和显式 frame 可引用上述任意场景 frame。reader 支持前向引用，不要求文件按父子顺序排列；检查引用存在、无环，并全部连接到唯一 world。world 读取时为无父节点、单位位姿，按使用约定保持不变；不修改基础 Frame 契约增加特殊保护。

辅助与目标 frame 不分成不同类型，是否作为访问目标由 Generation 决定。机器人内部 Link 保留在 RobotModel 中，不复制成场景 frame 树；首版不支持对其 frame 的引用。

## ResourceContext 的统一管理

保留现有路径和 mesh 入口，拟增加模型与场景取得入口：

```python
context = ResourceContext(root=bundle_root)
context.resolve_file(reference, relative_to=source_path)
context.get_mesh(mesh_path)
context.get_robot_model(config_path)
context.get_scene(scene_path)
```

文件内相对引用以包含引用的文件为基准解析；取得入口接收包内绝对 Path。沿用现有路径规范化、可读普通文件及包内范围检查，允许包内 ..，拒绝绝对文件引用、URI 和解析符号链接后越出包的目标。

各类资源分别以规范化的 mesh 文件、机器人配置文件、scene 文件路径为键。同一 context、同类资源、同一路径返回同一对象；不同文件不按 ID 或内容合并。同一 URDF 配不同机器人配置属于不同模型。context 生命周期对应一次输入包读取，无全局缓存；本轮不提供热更新，输入修改后使用新 context 重新读取。

context 的场景表保存供多份 Generation 共用的名义 Scene。生成过程另建独立的具体场景，不修改名义 Scene，不将生成结果放入或替换这张共享表中的对象。目前这是使用契约，不增加只读包装。

## 自动取得、reader 与登记

本轮已确认采用 context 自动管理：

```text
context.get_scene(path)
  ├─ 已有对象：直接返回
  └─ 没有对象：
       调用 reader
       → 解析、构造和校验
       → 返回完整 Scene
       → context 登记并返回
```

读取失败不登记半成品 Scene；此前成功取得的依赖可以保留，不要求回滚全部资源。reader 只负责解析、构造和校验，返回对象，不隐式向 context 登记自身结果。它可以通过 context 取得模型、mesh 等依赖；取得依赖不等于登记自身结果。

候选场景底层入口为 `read_scene(*, scene_path: Path, resources: ResourceContext) -> Scene`，计划从 multiarm_problem_gen.scenes 导出。直接调用 reader 执行一次读取，不保证自身结果复用，也不登记自身结果；需要共享对象时，通过 context 的取得入口调用。现有 read_robot_model 保持同样的底层角色，模型自动复用由 context.get_robot_model 负责。

外层输入包读取器以后负责发现文件、组织调用和最终交付，不另建资源缓存。本轮不要求存在 bundle.yaml。

## 本轮选择与保留方向

agent 起初建议另设模型取得接口。用户希望 ResourceContext 承担路径解析和统一资源管理，包含 mesh、RobotModel 和供 Generation 使用的 Scene；方案据此调整，不另设模型资源管理接口。随后明确 context 自动加载并登记成功结果，reader 不登记自身结果，以及共享名义 Scene 与生成出的具体场景的边界。

用户随后要求 frame 名称不要前缀，替代此前的 object/、robot/、frame/ 分类前缀建议。场景中统一使用无前缀名称，沿用场景内 frame 名称唯一的要求，并相应允许上述样例引用迁移。

本轮不增加公开的手动登记接口。后续考虑由 context 提供接口，允许外部构造完成后显式添加对象；是否与自动加载入口并存，届时再确定。重复登记、替换已有对象及路径与对象的一致性规则均留待引入该接口时讨论，不预设拒绝、覆盖或其他策略。这些是未来讨论方向，不是本轮待实现能力或验收要求。

## 首版输入与校验

沿用现有 0.1-draft 样例，输入规则按以下方案整理为精确契约：

| 内容 | 规则 |
|---|---|
| 场景头部 | schema_version、scene_id、world_frame 必需；版本为 0.1-draft，world_frame 首版固定为 world |
| 成员列表 | robots、objects、frames 明确提供，可为空列表 |
| 机器人 | 实例 ID、配置引用、安装 pose 必需；名义输入不覆盖规划关节状态 |
| 物体 | 仅支持 compound，包含非空碰撞几何列表 |
| 几何 | box、sphere、cylinder、mesh；尺寸和缩放含义沿用基础表示 |
| 位姿 | 实例与显式 frame pose 必填，完整提供位置和四元数 |
| 默认值 | 几何 local_pose 可省略为单位位姿；mesh 缩放可省略为单位缩放 |
| 规则 | environment_motion 明确填写 static；allowed_mount_contacts 可省略为空 |

static 指任务执行期间环境不动，仍允许生成时扰动。安装接触条目关联机器人、该模型内的 Link 和场景 Object，检查有效引用及重复条目；表示后续允许忽略该 link—object 对的碰撞，不是整条臂的豁免，也不证明实际接触或建立安装运动约束。

未知字段、重复键、显式 null、非法类型、数值及引用报错。文件输入错误统一为包含 source_path、location、message 的 InputReadError；公开接口的直接类型错误使用 TypeError。数值表示沿用米、弧度、右手系、xyzw 四元数及基础表示的归一化规则；YAML 数值列表由 reader 转为基础表示要求的元组。

Scene 读取负责本文件结构和对象关联。Generation 的序列、采样覆盖，以及输入包目录名与 scene_id 的一致性分别留给单元 5、6；本轮不迁移现有 tabletop 目录或添加 bundle.yaml。

## 验收与允许修改范围

以下为待实施的测试目的，不是已执行结果：

| 目的 | 依据及主要检查 |
|---|---|
| 表达真实输入 | 现有样例的两臂、七个物体、十一条环境几何、四个显式 frame 和两条安装接触规则 |
| 建立关联 | 独立小算例的无前缀引用、前向引用、多层关系、跨类别重名、占用 world、缺失引用和环 |
| 自动管理责任 | 已有对象直接返回，未命中才读取，成功后登记，失败不保存半成品，直接 reader 调用不登记自身结果 |
| 共享与状态 | 同一路径复用、不同配置不误合并、不同 Scene 的实例状态独立；状态维度、顺序、限位、更新及失败保留原值 |
| 读取边界 | 不改输入、路径搬移后可读、不越出包、不加载 mesh 内容 |

通过后仅说明表示、读取和共享行为符合契约，不代表碰撞、可达性或生成流程完成。修改资源管理后运行现有基础表示、资源和机器人回归，测试数量非零；不要求读取依赖模块的内部测试。

允许实施范围拟为 src/multiarm_problem_gen/scenes/、现有 resources.py、tests/scenes/ 及其小型输入、tests/resources/、新增 docs/contracts/scene.md、修订 docs/contracts/resources.md，以及必要的 README、Docker 运行说明和实施记录。examples/ur7e_table/inputs/tabletop/scene.yaml 的名称调整已提前完成，后续实现保持真实输入及模型资源不变。不修改 primitives、robots 的实现或内部测试、tools 原型，不新增计算后端依赖。必要文档路径均相对于本仓库。

读取范围为本任务方案与架构约定、scenes 和 resources 的实现及测试、必要构建配置、真实输入及依赖公开契约。单元 1、2 只读取公开契约、声明和面向调用者的示例，不读内部实现、内部测试或描述其内部实现的记录；不从 robots 的私有读取辅助函数抽取或复用代码。可执行真实依赖及公开验收命令。按 AGENTS.md 记录实际阅读范围、实现和测试用时及可取得的 token 用量；不可取得的数据如实标明。

## 实施准备判断

agent 判断：可以开始实施，首步是把候选字段、构造与更新接口、默认和错误规则整理为精确场景契约及资源扩展契约，然后按契约实现。当前基础表示与机器人公开契约已提供所需对象、引用和有效限位；PyYAML 与既有 Compose 环境已有入口，没有发现必须先新增后端或读取其他模块内部实现的阻塞缺口。

具体字段拼写、构造签名及内部组织可在不改变上述语义和职责的前提下落实；涉及数据语义、状态归属、公共行为或依赖边界的新增决定仍须返回讨论，不能以“完善契约”为由自行扩大范围。未来显式添加接口不阻塞本轮。

本判断基于公开契约与当前仓库检查，不是本轮代码验收结果。本次没有运行新代码或修改现有已实现契约。用户随后提交实现 prompt 才开始相应实现任务；写入本方案本身不表示代码工作已获执行。
