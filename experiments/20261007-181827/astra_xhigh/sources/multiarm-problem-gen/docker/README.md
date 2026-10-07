# Docker／Compose 开发环境

在仓库根目录执行以下完整命令。需要可访问 Docker 服务的 Linux 用户，以及 Docker Compose；首次构建需要访问 Docker Hub 和 PyPI。无需宿主 Python 包。

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"

docker compose -f docker/compose.yaml up -d --build --wait
docker compose -f docker/compose.yaml exec dev python -c 'import multiarm_problem_gen; print(multiarm_problem_gen.__file__)'
docker compose -f docker/compose.yaml exec dev python docker/check_environment.py
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/primitives -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/resources -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/robots -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/scenes -v
docker compose -f docker/compose.yaml exec dev python -m pip check
docker compose -f docker/compose.yaml exec dev bash
# 退出交互 shell 后停止环境：
docker compose -f docker/compose.yaml down
```

`--wait` 等待可编辑安装完成、包可导入后返回；不把容器已启动视为就绪。环境阶段只检查导入；基础表示必须运行实际测试，空测试集不算验收。

本轮 Linux 主机上，默认 Docker 构建网络连接 PyPI 超时，但宿主可访问。遇到同样情况可使用下面的完整替代命令；`BUILD_NETWORK` 只影响镜像构建，不改变运行中服务的网络：

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
export BUILD_NETWORK=host
docker compose -f docker/compose.yaml up -d --build --wait
docker compose -f docker/compose.yaml exec dev python docker/check_environment.py
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/primitives -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/resources -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/robots -v
docker compose -f docker/compose.yaml exec dev python -m unittest discover -s tests/scenes -v
docker compose -f docker/compose.yaml exec dev python -m pip check
docker compose -f docker/compose.yaml down
```

## 环境组织

单一 CPU `dev` 服务，仓库挂载到 `/workspace`。Python 环境位于容器的 `/opt/venv`，HOME 位于 `/home/dev`，均可由匹配宿主 UID/GID 的用户写入；构建工具在镜像构建时安装。容器启动时使用预装工具，离线执行可编辑安装，不修改宿主 Python 环境。安装生成的 `src/*.egg-info/` 已忽略。

源代码通过正常包导入生效，无需 PYTHONPATH。保存代码后重新运行 Python／测试即可看到修改；已运行的 Python 进程不会自动重载模块。修改依赖、环境或 UID/GID 后重新执行构建和启动命令。容器内临时安装的包随容器重建丢弃，需保留的依赖应先写入包配置并固定版本。

`Dockerfile.dockerignore` 仅允许 Dockerfile 及忽略规则进入构建上下文；原型、模型、Git 历史和运行产物不传入构建。容器工作区挂载整个仓库，任务的阅读边界仍需遵守。

## 固定版本与来源

2026-09-29 核实，选定可复现版本，不声明它们均为最新版：

| 项目 | 固定值 |
| --- | --- |
| Python | [3.13.15](https://www.python.org/downloads/release/python-31315/)；包兼容声明为 >=3.10 |
| 基础镜像 | Docker Official Image `python:3.13.15-slim-bookworm` |
| 多架构索引 digest | `sha256:2325bb286ec344af3e5898cc224b5844e2707ac6e26b1632516fd3edc84a5e26` |
| 本轮 linux/amd64 manifest | `sha256:3e2de9c40ca4e3d73240059f9d48baff27908f10293e985a2f382a0378e6df4a` |
| pip | [26.0.1](https://pypi.org/project/pip/26.0.1/) |
| setuptools | [80.10.2](https://pypi.org/project/setuptools/80.10.2/) |
| wheel | [0.45.1](https://pypi.org/project/wheel/0.45.1/) |
| PyYAML | [6.0.3](https://pypi.org/project/PyYAML/6.0.3/)；机器人 YAML 读取依赖 |

镜像 digest 来自环境建立时的实际 `docker buildx imagetools inspect`；Dockerfile 使用 tag＋digest。未执行 apt 升级，操作系统包由镜像 digest 固定。构建工具安装与 pyproject.toml 的构建要求保持一致；PyYAML 同时固定于包依赖和镜像，XML 使用标准库 ElementTree，测试使用 unittest。环境检查核对 PyYAML 的实际安装版本，`pip check` 检查依赖一致性。

Docker Engine 和 Compose 属于宿主前置工具，本仓库不安装或强制锁定；本轮实际版本为 Engine 29.4.1、Compose v5.1.3。镜像固定不保证首次离线构建，也不保证未来上游始终保留下载产物。

验收结果和工具限制见[首轮实现记录](../docs/notes/implementation/2026-09-29-first-implementation-results.md)。

## 读取真实机器人输入

环境启动后，从仓库根目录执行以下完整示例。模型只含资源描述，不加载 mesh，不执行 FK、碰撞或动力学。资源 context 由调用者管理，每次输入包读取创建一个；相同 context 复用 mesh，并按机器人配置文件路径复用模型，不按 URDF 路径合并模型。下面的底层 reader 示例每次读取新模型；需要共享时使用 `resources.get_robot_model(config_path)`。

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
docker compose -f docker/compose.yaml exec -T dev python - <<'PY'
from pathlib import Path
from multiarm_problem_gen.resources import ResourceContext
from multiarm_problem_gen.robots import read_robot_model

root = Path('/workspace/examples/ur7e_table')
resources = ResourceContext(root)
model = read_robot_model(
    config_path=root / 'resources/robots/ur7e_2f85/robot.yaml',
    resources=resources,
)
print(model.model_id, len(model.links), len(model.joints))
print('Planning:', tuple(joint.name for joint in model.planning_joints))
print('TCP:', model.tcp_link.name)
print('Home:', model.configurations['home'])
print('Shoulder limits:', model.joints['shoulder_pan_joint'].limits)
PY
```

单元 2 的验收结果、覆盖范围与限制见[实现记录](../docs/notes/implementation/2026-09-29-unit-2-implementation-results.md)。

## 读取共享名义场景

环境启动后，从仓库根目录执行以下完整示例。无需 bundle.yaml；所有文件引用相对各自源文件解析。`get_scene` 共享成功读取的名义场景；底层 `read_scene` 不登记自身结果。输入文件变更后应新建 context。

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
docker compose -f docker/compose.yaml exec -T dev python - <<'PY'
from pathlib import Path
from multiarm_problem_gen.resources import ResourceContext

root = Path('/workspace/examples/ur7e_table')
resources = ResourceContext(root)
path = root / 'inputs/tabletop/scene.yaml'
scene = resources.get_scene(path)
assert resources.get_scene(path) is scene
assert scene.robots['arm_a'].model is scene.robots['arm_b'].model
print(scene.scene_id)
print('Robots / objects / frames:', len(scene.robots), len(scene.objects), len(scene.frames))
print('Environment geometry:', sum(len(obj.collision_shapes) for obj in scene.objects.values()))
print('Mount contacts:', len(scene.rules.allowed_mount_contacts))
print('Parent:', scene.frames['can_a_visit'].parent.id)
print('Planning state:', scene.robots['arm_a'].planning_joint_positions)
PY
docker compose -f docker/compose.yaml exec -T dev python -m unittest discover -s tests/scenes -v
```

预期为 2 个机器人、7 个物体、14 个 frame（含 world 和 4 个显式 frame）、11 条环境几何、2 条接触规则，父名称为 `can_a`，规划状态为 None。独立小输入位于 `tests/scenes/fixtures/`；场景测试同时验收真实输入与整体搬移后的副本，检查输入未改且 mesh 内容未打开。

共享名义 Scene 的 frame 和实例状态具有更新能力，但生成过程须另建独立状态，不能修改这个共享对象。当前未提供场景复制、生成或碰撞计算。`tools/` 原型对旧名称的兼容性未在本轮验证。详细结果见[单元 3 实施记录](../docs/notes/implementation/2026-09-30-unit-3-implementation-results.md)。

## 自主试验：完整输入包入口与验收

单元 4–6 的探索性接口见 [InputBundle 契约](../docs/contracts/input-bundle.md)和[试验记录](../docs/notes/implementation/2026-09-30-autonomous-units-4-6-results.md)。样例新增 bundle.yaml，scene_id 已从 ur7e_table_baseline 改为 tabletop；文件路径和真实物理参数不变。下列命令从仓库根目录执行，使用上文已启动的 dev 服务；每组应有非零测试数量，任一失败立即停止。

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
docker compose -f docker/compose.yaml exec -T dev python docker/check_environment.py || exit
for suite in primitives resources robots scenes distributions generation bundles integration; do
  docker compose -f docker/compose.yaml exec -T dev python -m unittest discover -s "tests/$suite" -v || exit
done
docker compose -f docker/compose.yaml exec -T dev python -m pip check || exit
docker compose -f docker/compose.yaml exec -T dev python - <<'PY'
from pathlib import Path
from multiarm_problem_gen.bundles import BundleReader

bundle = BundleReader().read(Path('/workspace/examples/ur7e_table'))
scene = bundle.scenes['tabletop']
generation = bundle.generations[bundle.root / 'inputs/tabletop/generation.yaml']
assert generation.scene is scene
assert scene.robots['arm_a'].model is scene.robots['arm_b'].model
assert all(robot.planning_joint_positions is None for robot in scene.robots.values())
print('Scenes / generations / models / meshes:',
      len(bundle.scenes), len(bundle.generations), len(bundle.robot_models), len(bundle.meshes))
print('Bindings / seed / sample count:', len(generation.bindings), generation.seed, generation.sample_count)
print('Sequences:', {robot: tuple(frame.id for frame in frames)
                     for robot, frames in generation.sequences.items()})
PY
```

本例为一个场景、一份 Generation、一个共享模型、13 个 binding，seed=42、sample_count=10，双臂各四次访问。status、固定访问容差和返回初始配置规则都保存在 Generation 中。分布参数合法不保证实际关节状态合法，高斯没有隐含截断；本入口不加载 mesh 内容、不采样、不检查碰撞或可达性。每次完整包读取使用新的 ResourceContext，同次读取按规范路径共享资源。
