# 单元 1：基础表示公开契约

本契约整理自已确认的[基础表示方案](../notes/discussions/2026-09-29-unit-1-basic-representations.md)与[实施方案](../notes/discussions/2026-09-29-compose-and-unit-1-implementation.md)。仅覆盖构造、字段访问、自身校验和 Frame.pose 更新。

## 导入与构造

```python
from multiarm_problem_gen.primitives import (
    Pose, Frame, Box, Sphere, Cylinder, MeshResource, Geometry,
)

Pose(position_xyz=(0.0, 0.0, 0.0), quaternion_xyzw=(0.0, 0.0, 0.0, 1.0))
Frame(id=..., parent=..., pose=...)
Box(size_xyz=...)
Sphere(radius=...)
Cylinder(radius=..., height=...)
MeshResource(path=..., format=...)
Geometry(shape=..., local_pose=..., mesh_scale=None)
```

构造采用关键字参数；`...` 为必填参数的占位，不是默认值。字段按上述名称公开读取。

## 数值与错误

- 使用米、弧度、右手坐标系，四元数顺序为 xyzw。
- 数值分量接受 int 或 float，拒绝 bool、其他类型和非有限值；保存为 float。不能表示为有限 float 的输入拒绝为 ValueError。
- 向量接受指定长度的 tuple，保存为 float tuple；不接受 list 或其他容器，不修改调用者数据。
- 非法类型抛 TypeError；非法数值、长度或不支持的字符串取值抛 ValueError。错误信息包含字段名（分量错误可含下标）。
- 只读字段不可赋值或删除；具体异常子类不作为契约。不可变对象不暴露可原地修改的数值容器。

## 对象行为

| 对象 | 字段及保证 |
| --- | --- |
| Pose | position_xyz 为三维有限数值；quaternion_xyzw 为四维有限非零向量，构造时归一化。默认零平移、单位旋转。纯数值对象，不保存父 frame 或分布。 |
| Frame | id 为非空 str；parent 为已建立的 Frame 或 None；pose 为 Pose，表示相对 parent 的位姿。world 无 parent。id、parent 只读，pose 可整体替换为合法 Pose。 |
| Box | size_xyz 为三个正的完整边长；中心为原点，边沿局部 x/y/z。 |
| Sphere | radius 为正数；球心为原点。 |
| Cylinder | radius、height 为正数；中心为原点，轴线沿局部 z。 |
| MeshResource | path 为绝对 pathlib.Path；format 为字符串 stl 或 dae。不推断格式，不检查后缀，不读取、解析或检查文件存在性。路径规范化由 reader 保证。 |
| Geometry | shape 为 Box、Sphere、Cylinder 或 MeshResource；local_pose 为 Pose。mesh_scale 对 mesh 为三个有限正数，None 转为 (1.0, 1.0, 1.0)；基本形状仅接受 None 并保存 None。 |

Pose、Box、Sphere、Cylinder、MeshResource、Geometry 构造后不可原地修改。Geometry 保留传入 shape 和 local_pose 的引用；不同 Geometry 可共享资源，分别保存自身局部位姿和缩放。

Geometry.local_pose 表示几何坐标系在所属物体或 link 参考系中的位姿。mesh 保留资源原点和轴向，不自动居中。列向量下先缩放再变换：`p_parent = R @ (S @ p_mesh) + t`，缩放不改变 t。本单元仅表示这些数据，不执行变换计算。

Frame 保留 parent、pose 的引用。`frame.pose = new_pose` 成功后，引用同一 Frame 的调用者看到新 Pose；共享旧 Pose 的其他 Frame 不受影响。非法赋值抛 TypeError，且原 pose 保持不变。身份和父关系不变。不提供世界位姿缓存。

## 职责边界

构造没有文件访问或跨对象状态修改。场景内 frame 标识唯一、无环、连接到 world，以及文件可读性、包内引用和路径规范化由后续 reader／场景组装负责。本单元不因 id 为 world 而增加额外规则，不自动创建根 frame。

不提供输入读取、mesh 加载、资源缓存、采样、compose／inverse、世界位姿查询、运动学、碰撞或渲染。名义场景和具体场景不能共享可变 Frame；如何复制场景关系不在本契约范围。相等性、哈希及序列化不是本轮公开保证。

## 验收入口

按 [Docker 说明](../../docker/README.md)启动后：

```bash
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/primitives -v
```

测试覆盖合法构造、字段值与引用、错误类型／长度／数值、四元数归一化、不可变性、资源共享、Frame 更新与失败保留原值、构造无文件访问和输入不变。
