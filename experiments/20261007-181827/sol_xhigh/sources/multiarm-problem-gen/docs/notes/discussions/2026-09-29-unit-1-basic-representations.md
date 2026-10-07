# 单元 1：基础表示方案

日期：2026-09-29

状态：用于准备独立实现任务的讨论方案，尚未实现。下文区分已确认语义、本轮确认的可变性方向，以及仍需确认的接口细节；不是实现授权。

## 目标与范围

提供 Pose、Frame、基本形状、MeshResource 和 Geometry，供机器人及场景表示使用。本单元不读取 YAML／URDF，不查找文件、不加载 mesh，不实现采样、运动学、碰撞或渲染后端。

数据类可以检查自身参数，但跨文件解析和对象关联由 reader 组织。相关背景见[读取流程与对象协作](2026-09-28-input-reading-flow.md)。

## Class 与主要内容

以下概念和几何含义沿用既有讨论；具体字段名及 Python 类型为候选公开接口。

| Class | 主要字段 | 含义 |
|---|---|---|
| Pose | position_xyz、quaternion_xyzw | 纯数值位姿，不保存父 frame 或分布 |
| Frame | id、parent: Frame 或 None、pose: Pose | 有身份的坐标系，pose 相对于父 frame；world 无父 frame |
| Box | size_xyz | 三个完整边长，中心为原点，边沿局部 x/y/z |
| Sphere | radius | 球心为原点 |
| Cylinder | radius、height | 中心为原点，轴线沿局部 z |
| MeshResource | path: pathlib.Path、format | 已定位资源的规范化绝对路径及格式，不保存网格内容 |
| Geometry | shape、local_pose、mesh_scale | shape 为基本形状或 MeshResource 引用；缩放仅对 mesh 适用 |

采用米、弧度、右手系，四元数顺序为 xyzw。数值向量使用固定长度 tuple。不额外建立 MeshGeometry 层。

Geometry.local_pose 表示几何坐标系在所属参考系中的位姿，所属参考系通常为物体或 link 坐标系。mesh 保留资源原点和轴向，不自动居中。列向量约定下，先局部缩放再变换：`p_parent = R @ (S @ p_mesh) + t`；缩放不改变 t。几何坐标系无需单独建立 Frame。

## 构造、引用与可变性

agent 起初建议全部对象不可变；用户指出 Frame 的 pose 需要可变。讨论后确认以下方向：

- Pose 是不可变数值对象；Frame 的 pose 可以整体替换，不修改 Pose 内部字段。
- Frame 的身份与父子关系暂不提供修改能力；替换 pose 后，引用同一 Frame 的对象看到新位姿。
- 名义场景与具体场景不能共享可变 Frame；可以共享不可变 Pose、机器人模型及 mesh 资源。新场景的关系复制在后续讨论，不在本单元实现。
- 暂不引入世界位姿缓存，也不增加缓存更新机制。

示意：

```python
frame.pose = new_pose          # 首次交付即支持整体替换 Pose
# 不通过 frame.pose.position_xyz = ... 修改 Pose 内部字段
```

基础形状、MeshResource、Geometry 构造后不可原地修改，多处使用可以共享；各 Geometry 保存各自的局部 pose 和缩放，不改写共享资源。调整局部位姿或缩放时创建新的 Geometry，仍可引用原资源。

后续讨论决定将 Frame.pose 的整体替换纳入首次交付，身份和父关系保持只读。赋值仅接受合法 Pose；非法赋值失败时保留原值。reader 可按父子依赖顺序创建 Frame；不要求输入文件按此顺序排列。

## 校验职责

| 本单元负责的自身检查 | reader／场景组装负责 |
|---|---|
| 数值维度、有限性，基本形状尺寸为正 | YAML／URDF 的字段解释与名称解析 |
| 四元数有效性 | 文件是否存在、可读，引用是否在包内 |
| mesh 缩放与几何类型匹配 | 相对路径解析为规范化绝对 Path |
| parent、shape 等参数类型正确 | 场景内 frame 标识唯一、引用无环且连接到 world |

MeshResource 可以检查 path 是绝对 Path，但不在构造中调用文件读取或路径解析来访问文件系统；规范化由 reader 保证。

后续讨论确认以下细则：

- 四元数接受分量有限、向量非零的输入并归一化；零四元数及非有限值被拒绝。不再采用此前建议的“接近单位长度才允许归一化”阈值。此取舍简化使用，但可能掩盖输入长度错误；不改变 xyzw 顺序约定。
- mesh 缩放首版仅接受有限正数，省略时使用 `(1, 1, 1)`；非 mesh 不接受 mesh 缩放。
- 非法类型使用 TypeError，非法数值使用 ValueError，错误信息指出具体字段。reader 再补充源文件和字段路径，不由本单元猜测来源。

## 首次交付与验收

首次交付包括构造、字段访问、自身参数检查及 Frame.pose 整体替换。暂不扩展 compose、inverse、世界位姿查询、mesh 加载或资源缓存。

验收依据公开行为：

- 合法对象能表达现有样例的几何和 frame 关系；错误维度、非有限数值及非法尺寸被拒绝。
- 两个 Geometry 引用同一 MeshResource，局部位姿与缩放分别保存，不修改共享资源。
- 构造不读取文件、不修改传入数据；不可变对象不暴露可原地修改的内部数值容器。
- 整体替换 pose 能被同一 Frame 的引用方观察到；共享旧 Pose 的其他 Frame 不受影响，身份与父关系不变；非法赋值不改变原 pose。
- 有限非零四元数被归一化，零值和非有限值被拒绝；mesh 默认单位缩放，非正或非有限缩放被拒绝。

## 实现前还需补齐

上述数值存储、校验规则、不可变性及 Frame 更新范围已确认。实现任务还需指定公开导入入口、允许修改范围和验收入口，并落实表中字段的精确类型与构造签名。实现 agent 自主决定不影响这些契约的内部组织；本轮不提前列出私有方法或辅助函数。

后续补充：[Compose 环境与基础表示实施方案](2026-09-29-compose-and-unit-1-implementation.md)已给出公开导入入口、构造参数、修改范围和 Compose 测试入口；进入实现时据此整理公开契约，并固定环境版本。

任务范围与代码职责的区别见[实现单元说明](2026-09-29-implementation-unit-and-responsibility.md)，基础概念来源见[领域表示讨论](2026-09-22-input-domain-representations.md)。
