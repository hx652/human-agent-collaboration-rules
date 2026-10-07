# 单元 2：机器人表示与读取方案

日期：2026-09-29

状态：整理本轮讨论及后续明确的接口方案，尚未实现。实施时先据此整理公开契约；本次文档写入不等于执行实现。依赖[基础表示公开契约](../../contracts/primitives.md)。

## 目标与本次修正

读取机器人配置与已展开 URDF，得到完整、可共享的 RobotModel。用户确认：文件分开便于表达和修改，但读取后应合并为统一表示，不必在内存中继续按文件划分。

因此，修正此前“RobotModel 引用独立 RobotConfig”的建议：不再对外交付单独的 RobotConfig，也不保存重复的原始配置／有效配置；有覆盖的字段保存合并后的有效值，未覆盖的沿用 URDF。源文件路径可用于诊断，不要求从模型完整还原两份原文件。同一 URDF 搭配不同配置仍是不同模型。

同时去掉 declared_mesh_scale：Geometry 只保存有效缩放；URDF 未写 mesh scale 时采用单位缩放，不再另存“是否显式填写”的记录。

## 运行流程与对象协作

公开入口：

```python
resources = ResourceContext(root=bundle_root)
model = read_robot_model(config_path=robot_config_path, resources=resources)
```

1. 读取配置，通过 ResourceContext 定位 URDF。
2. 创建 Link，解析惯性、visual／collision 条目及表面属性；mesh 引用交给 ResourceContext。
3. 创建 Joint，关联父子 Link 和 mimic 来源。
4. 将规划关节、TCP、固定值、命名配置和碰撞规则关联到已有模型对象，合并配置覆盖。
5. 检查结构、引用和参数，返回统一 RobotModel，不交付缺失关联的半成品。

读取器建立关联；模型对象保存结果，不自行打开文件。本阶段不加载 mesh 内容，不执行 FK／IK、碰撞、动力学或场景生成。

## 表示方案

下列职责沿用讨论，具体字段和辅助数据类仍需整理为公开契约。

| 表示 | 主要内容 |
|---|---|
| RobotModel | 模型标识、URDF 名称、根 Link、Link／Joint 查找关系；规划关节顺序、TCP、有效限制、固定关节值、命名配置、自碰撞规则 |
| Link | 名称、可选惯性信息、visual／collision 条目 |
| Joint | 类型、父子 Link、origin、运动轴、有效限制、动力学参数、mimic 关系 |
| visual 条目 | Geometry 引用及适用的外观信息 |
| collision 条目 | Geometry 引用及可选表面属性 |

有效关节限制保存在对应 Joint，由 RobotModel 的关节查找表统一访问，不重复维护同一有效值。模型及嵌套集合只读共享，不包含具体机器人实例的安装位姿或可变规划状态。

当前 UR7e＋夹爪 URDF 已有的内容全部解析并保留：结构、几何、质量、惯性坐标系与惯性张量、位置／速度／effort 限制、阻尼／摩擦、mimic，以及两处 collision.surface 的全部分组参数。surface 当前包括 mu1、mu2、kp、kd、soft_cfm、soft_erp、minDepth、maxVel。不要求保留 XML 排版、注释或数字原始字符串；新增尚不支持的元素或属性明确报错，不静默遗漏。

## 缺失信息与默认含义

已确认的规则：

- visual／collision 缺 origin 时直接补所属 Link 下的单位 Pose；不再为此增加 to_geometry() 转换步骤。
- mesh 缺 scale 时采用 Geometry 的单位缩放约定，不另存原始缺失状态。
- 其他可选信息缺失保存 None；必需信息缺失报错。
- 格式对缺失项规定的默认含义继续保留，在使用时统一解释。例如 mimic 的倍率／偏移缺失不改变其默认 1／0 的语义；统一通过有效值属性访问，例如 effective_origin、effective_multiplier、effective_offset；不改变原字段的 None 状态。
- 不存在惯性信息不等于零质量。已出现的惯性等结构，其必需子字段仍需完整。

Geometry 的局部位姿和缩放沿用单元 1 契约，mesh 仍以资源原点和轴向解释。

## 配置覆盖

配置显式字段覆盖 URDF 对应字段，未提供则沿用 URDF，不擅自限制为只能收紧。两处都没有的可选值保持缺失及其格式默认含义。模型不再要求调用者自行合并两份数据。

限位覆盖采用以下 YAML 形式：

```yaml
joint_limits:
  shoulder_pan_joint:
    lower: -3.0
    upper: 3.0
    velocity: 1.0
```

允许字段为 lower、upper、velocity、effort、acceleration，按字段覆盖；配置中的 null 报错，不作为删除已有值的指令。合并后的限制必须合法，固定关节值和命名配置按有效限制检查。现有配置中的碰撞排除原因、固定组件排除约定和 mimic 策略也应保留，不仅处理关节列表与限位。

## 资源公开接口

公开入口位于 `multiarm_problem_gen.resources`：

```python
ResourceContext(root: Path)
context.resolve_file(reference: Path, *, relative_to: Path) -> Path
context.get_mesh(path: Path) -> MeshResource
```

- root 为已存在的输入包根目录，构造时解析为规范化绝对路径；无需先实现 bundle.yaml 读取。
- relative_to 是包含引用的源文件路径，不是目录。reference 为文件内相对路径；读取器负责将输入字符串转成 Path。
- 允许 .. 在包内导航；解析符号链接后，实际目标必须仍在包内，且是存在、可读的文件。拒绝尚不支持的 URI 引用。
- get_mesh 接收已解析路径，根据后缀识别 STL／DAE，同一 context 内同一规范路径返回同一个 MeshResource；不加载 mesh 内容，不按内容去重。
- context 由外层创建和传入，生命周期对应一次输入包读取，不使用全局缓存。机器人模型缓存仍由后续输入包组织负责，不按 URDF 路径误合并不同配置。

## 机器人公开接口

入口位于 `multiarm_problem_gen.robots`：

```python
read_robot_model(*, config_path: Path, resources: ResourceContext) -> RobotModel
```

config_path 为包内机器人配置文件的绝对路径，读取器仍检查路径和文件有效性。成功返回完整模型，失败不返回半成品。

RobotModel 公开内容：

| 字段 | 约定 |
|---|---|
| model_id、urdf_name | 配置中的模型标识和 URDF 名称 |
| root_link | 根 Link 对象 |
| links、joints | 按名称查找的只读映射 |
| planning_joints | 按规划顺序排列的 Joint 元组 |
| tcp_link | TCP 对应的 Link |
| fixed_joint_positions | 已核对关节名称的固定值映射 |
| configurations | 命名配置映射；每份关节值按 planning_joints 顺序保存 |
| collision_policy | 排除对、原因、固定组件内部碰撞排除约定 |
| mimic_joint_policy | 已解析的 mimic 使用约定 |

Joint 的父子 Link、mimic 来源及碰撞排除对关联模型内已有对象。有效关节限制通过 `model.joints[name]` 访问。具体辅助数据表示的构造与查询签名在编码前写进公开契约，不重新引入 RobotConfig 或重复保存覆盖前值。

## 错误与验收

提供统一 InputReadError，包含 source_path、location、message；location 为 YAML 字段路径或 URDF 元素位置，message 包含原因及必要的引用名称／路径。读取器为底层校验错误补充来源再报告。公开接口被直接传入错误类型时仍使用 TypeError。

检查名称唯一、单一根、结构连通、父子和 mimic 无环、引用有效。规划关节独立且不重复；非规划活动关节具有固定值或 mimic 来源；参数、有效限制与配置自洽。

验收使用当前完整 URDF 及小型独立算例，覆盖全部字段和所属关系、缺失及默认含义、配置覆盖、资源复用、路径搬移、名称和结构错误。拒绝缺失必需值和包外引用；不静默丢弃未支持的内容。测试在 Compose 环境执行，确认读取不加载 mesh、不修改输入文件。

## 实施范围与准备

先整理 `docs/contracts/resources.md` 和 `docs/contracts/robot-model.md`，再实现最小资源接口及单元 2。只依据单元 1 的公开契约使用基础表示，不读取其内部实现或内部测试；可以运行其公开验收命令。

YAML 使用 PyYAML，XML 使用标准库 xml.etree.ElementTree；PyYAML 具体版本在环境准备中核实并锁定。修改范围为 resources／robots 的代码、对应测试与小型输入、公开契约、必要的依赖／Docker 配置和运行说明，以及本次实现记录。不能借此扩展 Scene、Generation、采样或计算后端，也不擅自修改单元 1 的契约。

当前 URDF 的全面支持已确认；其他关节类型和当前文件未出现的能力不因“完整”一词自动扩大。内部算法和文件拆分由实现 agent 决定；如果补充精确签名时遇到影响既有语义或职责边界的问题，先返回讨论。
