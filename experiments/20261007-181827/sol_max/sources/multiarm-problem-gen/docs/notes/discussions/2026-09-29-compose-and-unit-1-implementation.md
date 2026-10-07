# 首轮实施方案：Compose 环境与基础表示

日期：2026-09-29

状态：已讨论的两部分实施方案，尚未创建环境文件或实现代码，不代表已授权执行实现。基础行为见[单元 1 方案](2026-09-29-unit-1-basic-representations.md)。

## 第一部分：统一 Docker／Compose 环境

整个项目使用 Docker 管理开发与验证环境，通过 Compose 启动。相关文件集中存放：

```text
docker/
├── Dockerfile
├── Dockerfile.dockerignore
├── compose.yaml
└── README.md
```

- 单一 dev 服务，仓库挂载到 `/workspace`。构建上下文为仓库根目录，Dockerfile 位于 docker/；使用 Dockerfile.dockerignore 管理构建忽略项，避免将日志、Git 历史等无关内容发送到构建中。
- Python 兼容范围暂按 3.10+；实际环境固定具体版本和基础镜像 digest，安装工具及依赖固定版本，不以浮动 latest 作为复现依据。具体版本与 digest 在环境建立时核实并记录，当前尚未选定。
- 项目以可编辑方式安装，使用正常 Python 导入路径；修改源码无需重建镜像。环境配置或依赖变化时重新构建。项目依赖由 pyproject.toml 声明，所用版本随仓库记录。
- Linux 下通过 LOCAL_UID／LOCAL_GID 匹配宿主用户，保证工作区产物可由用户编辑。启动所需安装过程、可写环境目录应一并处理，不能依赖宿主已有 Python 包。
- 第一部分仅建立 CPU 开发与测试环境，不增加 GPU 或其他服务。单元 1 运行代码先只使用 Python 标准库，测试采用 unittest。

预期使用方式如下；配置完成后，从仓库根目录执行：

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"

docker compose -f docker/compose.yaml up -d --build

docker compose -f docker/compose.yaml exec dev \
  python -m unittest discover -s tests/primitives -v

docker compose -f docker/compose.yaml exec dev bash

docker compose -f docker/compose.yaml down
```

验收：可重新构建并启动；项目可导入；代码修改可直接生效；容器创建的工作区文件权限正常。环境阶段先做最小导入检查，单元 1 测试在第二部分完成后运行，不能把空测试集视为实现验收通过。

## 第二部分：单元 1 基础表示

```text
pyproject.toml
src/multiarm_problem_gen/
├── __init__.py
└── primitives/
    ├── __init__.py
    └── …
tests/primitives/
docs/contracts/primitives.md
```

实现 agent 自主安排内部文件。公开导入入口为：

```python
from multiarm_problem_gen.primitives import (
    Pose, Frame, Box, Sphere, Cylinder, MeshResource, Geometry,
)
```

接口以此前讨论的关键字参数形式整理为公开契约：

```python
Pose(position_xyz=(0.0, 0.0, 0.0),
     quaternion_xyzw=(0.0, 0.0, 0.0, 1.0))
Frame(id=..., parent=..., pose=...)
Box(size_xyz=...)
Sphere(radius=...)
Cylinder(radius=..., height=...)
MeshResource(path=..., format=...)
Geometry(shape=..., local_pose=..., mesh_scale=None)
```

省略号表示必填参数，不是运行默认值。数值向量接受规定长度的 tuple，内部保存 float tuple；数值分量接受 int／float，拒绝 bool 和非有限值。Frame.id 为非空字符串，parent 为已建立的 Frame 或 None；Frame.pose 可整体替换，id 和 parent 只读。

MeshResource.path 必须为绝对 pathlib.Path，构造不访问文件系统；format 首版为 `stl` 或 `dae`，不在构造时推断。Geometry.shape 为基本形状或 MeshResource，local_pose 为 Pose；mesh 的 None 缩放转为单位缩放，基本形状只接受 None。

其余行为沿用单元 1 方案：四元数归一化；Pose、形状、MeshResource、Geometry 不可变；参数和赋值失败的检查；无 mesh 加载或计算后端。class、公开方法和函数按 AGENTS.md 编写围绕职责、抽象和输入输出关系的 docstring。

验收在 Compose 环境执行，覆盖合法构造、错误类型与数值、四元数归一化、不可变性、资源共享、Frame.pose 更新可见性及失败后保留原值。检查构造过程无文件访问，不修改调用者数据。

## 执行顺序、权限与就绪判断

先把上述接口与单元 1 的行为整理到 docs/contracts/primitives.md，供独立上下文的实现 agent 使用；不再提前列出内部辅助函数。环境部分负责 Docker 文件、必要的 pyproject.toml、包骨架和运行说明；基础表示部分负责 primitives、对应测试及实现记录。依赖已有公开契约，不读取无关原型内部实现，不改变其他单元设计。

建议先交付环境，再实现基础表示，分别验收、分别建议提交。按此前 Git 约定，在设计基线集成 main 后建立实现分支；本次记录没有执行集成、创建分支或实现。

当前职责和行为足以进入实施准备，无需继续扩展架构。前置工作为公开契约整理，以及核实并固定 Python 具体版本、镜像 digest 和构建工具版本。若整理中发现新的架构或行为歧义，先返回讨论，不自行改变已确认语义。

本次实际检查：Docker 客户端与服务端均为 29.4.1，Compose 为 v5.1.3；Docker 服务经只读权限提升可访问。尚未构建镜像或运行容器，镜像下载、构建和测试是否成功仍需实际验证。
