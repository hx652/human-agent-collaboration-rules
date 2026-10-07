# UR7e 双臂桌面输入包

本目录是可整体搬移的生成器输入样例。目录与路径组织已整理，YAML 字段仍为草稿；有效性处理等规则仍待确定。尚无正式生成器执行这些输入。

## 内容与入口

```text
ur7e_table/
├── README.md
├── bundle.yaml
├── inputs/tabletop/
│   ├── generation.yaml
│   └── scene.yaml
└── resources/
    ├── robots/ur7e_2f85/
    │   ├── robot.yaml
    │   ├── robot.urdf
    │   ├── meshes/{ur,robotiq}/
    │   └── licenses/
    ├── objects/ball/
    │   ├── ball.stl
    │   └── LICENSE
    └── sources.yaml
```

完整包读取入口为 [bundle.yaml](bundle.yaml)，它显式声明场景目录；BundleReader 只在声明目录内发现直属 `generation.yaml` 与 `generation_*.yaml`，按文件名字典序读取。不同场景可以共享 resources，同一场景可以配多份生成规则；读取不会合并规则或生成样本。

也可以独立选定 [generation.yaml](inputs/tabletop/generation.yaml) 读取，它显式引用 [scene.yaml](inputs/tabletop/scene.yaml)。下面代码在已安装本项目的 Python 环境中、从仓库根目录执行：

```python
from pathlib import Path
from multiarm_problem_gen.bundles import BundleReader
from multiarm_problem_gen.generation import read_generation
from multiarm_problem_gen.resources import ResourceContext

root = Path('examples/ur7e_table').resolve()
bundle = BundleReader().read(root)
assert bundle.generations[root / 'inputs/tabletop/generation.yaml'].scene is bundle.scenes['tabletop']

resources = ResourceContext(root)
generation = read_generation(
    generation_path=root / 'inputs/tabletop/generation.yaml', resources=resources,
)
```

为满足 bundle 的目录名约定，逻辑 scene_id 从 `ur7e_table_baseline` 改为 `tabletop`；按旧 ID 查找的调用者需更新。文件路径与真实几何、位姿、关节、模型和生成参数均未改变。

所有文件引用相对于包含该引用的文件所在目录解析，包括 URDF 中的 mesh 路径。输入包包含全部运行资源；不使用绝对路径、package:// 或包外资源引用。BundleReader 要求真实场景目录末级名称等于 scene_id；独立 Scene／Generation reader 没有此目录约束。机器人资源读取按显式引用进行。输出位置由运行时指定，不要求输入包包含 samples 目录。

机器人配置引用已展开 URDF；消费者无需 xacro 或 ROS 包定位。STL 碰撞网格和 DAE 外观资源均保留，外观文件的存在不表示当前工具支持渲染 DAE。来源、固定提交及包内资源哈希记录于 [sources.yaml](resources/sources.yaml)，许可证随资源保留；这些记录不是生成规则。

## 样例内容与限制

两台 UR7e 配 Robotiq 2F-85，夹爪闭合，桌面包含圆柱目标、方块和球形 mesh。各臂分别按固定顺序访问四个 frame；generation 提供场景扰动和初始关节分布示例。

返回初始配置时，每个规划关节的绝对误差不超过 0.001 rad；本例为有限转动关节。首版不提供 `dwell_time_s`，不要求最短访问停留时间，允许规划器为协调而等待，不额外规定到达速度。返回后保持的约定不变。非规划关节仍属于机器人状态，首版沿用 robot.yaml 中的固定夹爪值，不增加逐问题配置能力。以上是输入约定，不代表已经验证随机样本可行性。

模型准备材料位于仓库 tools/model_preparation/ur7e_2f85，基准检查与历史报告位于 tools/baseline_validation/ur7e_table，预览位于 tools/scene_preview；它们均不属于本输入包的运行依赖。详细布局依据和既有检查范围见仓库中的基准验证 README。
