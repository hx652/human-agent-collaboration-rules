# 机器人表示与读取公开契约

依据[单元 2 方案](../notes/discussions/2026-09-29-unit-2-robot-model-and-reading.md)，依赖[基础表示](primitives.md)与[最小资源接口](resources.md)。

```python
from multiarm_problem_gen.robots import read_robot_model, RobotModel, InputReadError
model = read_robot_model(config_path=absolute_config_path, resources=context)
```

config_path 为包内已存在、可读文件的绝对 Path，resources 为 ResourceContext。直接传入错误类型抛 TypeError；文件、格式、引用、数值和结构错误统一抛 InputReadError，包含 source_path、location、message。location 是 YAML 字段路径或带名称／序号的 XML 元素路径。成功才返回完整模型；失败可能留下 context 中已解析的 MeshResource，不交付半成品模型。不写输入，不加载 mesh，不执行运动学、碰撞或动力学。

## 只读表示

以下类均可从 `multiarm_problem_gen.robots` 导入。构造使用关键字参数，字段按表中名称读取；省略的可选参数默认 None，visuals/collisions 默认空元组。模型关系与数值校验由读取入口保证；直接构造数据记录不是另一个读取／验证入口。字段不可赋值或删除，集合使用元组和只读映射快照；不承诺相等性、哈希或序列化。

| 类型 | 构造字段与语义 |
|---|---|
| RobotModel | model_id: str, urdf_name: str, root_link: Link, links: Mapping[str, Link], joints: Mapping[str, Joint], planning_joints: tuple[Joint, ...], tcp_link: Link, config_path: Path, urdf_path: Path；可选 fixed_joint_positions: Mapping[str, float], configurations: Mapping[str, tuple[float, ...]], collision_policy: CollisionPolicy, mimic_joint_policy: str |
| Link | name: str；可选 inertial: Inertial；visuals: tuple[Visual, ...], collisions: tuple[Collision, ...] |
| Joint | name: str, type: str, parent: Link, child: Link；可选 origin: Origin, axis_xyz: tuple[float, float, float], limits: JointLimits, dynamics: JointDynamics, mimic: Mimic |
| Origin | 可选 xyz、rpy，均为三维 float 元组；保留属性缺失，effective_pose 返回单元 1 Pose |
| Inertial | mass: float, inertia: InertiaTensor；可选 origin: Origin；effective_origin 返回 Pose |
| InertiaTensor | ixx, ixy, ixz, iyy, iyz, izz: float，惯性坐标系中的对称张量分量 |
| JointLimits | 可选 lower, upper, velocity, effort, acceleration: float；仅保存配置合并后的值 |
| JointDynamics | 可选 damping, friction: float |
| Mimic | joint: Joint；可选 multiplier, offset: float，关联同一模型中的来源关节 |
| Visual | geometry: Geometry；可选 name: str |
| Collision | geometry: Geometry；可选 name: str, surface: Surface |
| Surface | 可选 friction: SurfaceFriction, contact: SurfaceContact |
| SurfaceFriction | 可选 ode: FrictionODE |
| FrictionODE | 可选 mu1, mu2: float |
| SurfaceContact | 可选 ode: ContactODE |
| ContactODE | 可选 kp, kd, soft_cfm, soft_erp, minDepth, maxVel: float；保留输入命名与分组 |
| CollisionPolicy | 可选 ur_disabled_pairs: tuple[CollisionExclusion, ...], ignore_internal_collisions_of_fixed_assemblies: bool |
| CollisionExclusion | links: tuple[Link, Link]；可选 reason: str |

root_link、tcp_link、planning_joints、Joint.parent/child、Mimic.joint 与碰撞排除对均引用模型查找表中的对象。configurations 按 planning_joints 顺序排列；fixed_joint_positions 按已经核验的关节名查询。没有 RobotConfig、覆盖前值副本、实例安装 pose 或可变关节状态。

## 缺失与默认

visual／collision 只在 Geometry 中保存有效 local_pose，缺 origin 为单位 Pose；mesh 缺 scale 使用单位缩放，不另存缺失标志。其他可选项缺失为 None，出现的空可选分组仍保留分组对象。

统一有效值属性不改变原字段：

- Origin.effective_pose：缺 xyz/rpy 分量组按零解释；URDF 固定轴 RPY 按 Rz(yaw) Ry(pitch) Rx(roll) 转成 xyzw 四元数。
- Joint.effective_origin、Inertial.effective_origin：缺 origin 返回单位 Pose。
- Joint.effective_axis_xyz：revolute 缺 axis 为 (1, 0, 0)；fixed 缺 axis 为 None；显式轴保留数值、不归一化，拒绝零向量。
- JointLimits.effective_lower/effective_upper：缺值按当前无版本 URDF 的 0 解释。effort/velocity 在出现的 URDF limit 中必需；acceleration 只来自配置，缺失没有默认数值。
- JointDynamics.effective_damping/effective_friction：缺属性按 0；Joint.effective_dynamics 在整个 dynamics 缺失时返回空 JointDynamics 供同样访问。
- Mimic.effective_multiplier/effective_offset：缺失按 1／0。

无 inertial 不代表零质量；surface 为当前文件使用的扩展，仅保留参数，不为其补充后端相关默认。配置可选字段缺失为 None，不猜测碰撞或 mimic 策略；有 mimic 时必须明确 `derive_from_urdf`。

## 输入范围和检查

YAML 必需字段：schema_version（`0.1-draft`）、model_id、urdf、root_link、planning_joints（可为空列表）、target_link。可选字段：joint_limits、fixed_joint_positions、mimic_joint_policy、configurations、collision_policy。显式 null 拒绝；未知字段、重复键、非法类型拒绝。仅支持 mimic_joint_policy=`derive_from_urdf`。命名配置形式为 `{name: {joint_positions: {joint_name: value}}}`，必须恰好覆盖规划关节。碰撞规则沿用现有 robot.yaml 的字段。

joint_limits 以关节名映射 lower/upper/velocity/effort/acceleration，按显式字段覆盖，允许放宽；不允许 null 删除。URDF 自身必需信息必须完整，再校验合并结果。位置下限不得大于上限；速度、effort、acceleration、阻尼、摩擦非负；数值有限且拒绝布尔值。质量非负，惯性对角线非负；本轮不作惯性张量物理可实现性证明。surface 参数非负，soft_erp 在 [0,1]。

URDF 支持当前文件使用的无版本 robot、link、fixed/revolute joint；origin、axis、limit、dynamics、mimic；inertial 的 mass 和全部六个 inertia 分量；visual/collision 的 mesh、box、sphere、cylinder；以及表中 surface 分组。geometry 必须恰有一种形状。出现的 inertial、几何和引用等结构的必需值不可省略。revolute 必须有 limit；仅 lower/upper 可缺并按格式默认解释。material（包括全局定义、visual 内定义及引用）、当前文件未出现的关节类型、URDF version 属性、transmission、gazebo、safety_controller 等不支持，元素、属性和非空多余文本均明确报错，不静默忽略。XML 注释和排版不保存，拒绝 DTD／实体声明。

检查 Link／Joint 名称唯一、单根、单父、连通、父子无环、mimic 无环及有效引用。规划关节必须是独立 revolute 且不重复；固定值仅适用于非规划、非 mimic 的 revolute；其他活动关节必须有固定值或 mimic 来源。固定值、命名配置及其可确定的 mimic 值按有效位置限制检查；不要求整个规划范围经 mimic 映射后都落在限位内。碰撞对不得同名或重复（顺序颠倒也算重复）。不展开固定组件碰撞对，不证明命名配置无碰撞或 TCP 可达。

## 验收入口

见 [Compose 命令](../../docker/README.md)。资源测试 `python -m unittest discover -s tests/resources -v`，机器人测试 `python -m unittest discover -s tests/robots -v`。真实输入为 `examples/ur7e_table/resources/robots/ur7e_2f85/robot.yaml` 和同目录 URDF；独立小输入位于 `tests/robots/fixtures/`。
