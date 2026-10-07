# InputBundle 表示与读取公开契约

本轮探索性实现依据[单元 6 公开交接包](../notes/discussions/2026-09-30-unit-6-public-handoff.md)的 D6-1/2/3，不代表用户最终接受设计。依赖[资源管理](resources.md)、[Scene](scene.md)和[Generation](generation.md)公开契约。

```python
from pathlib import Path
from multiarm_problem_gen.bundles import BundleReader, InputBundle, InputReadError

bundle = BundleReader().read(Path('examples/ur7e_table'))
scene = bundle.scenes['tabletop']
generation = bundle.generations[bundle.root / 'inputs/tabletop/generation.yaml']
assert generation.scene is scene
```

## 交付与身份

`BundleReader().read(root: Path) -> InputBundle` 是唯一承诺的构造／交付入口。每次调用创建新的 ResourceContext，无跨次缓存；成功才返回完整结果，失败不返回半成品、不写输入。非 Path 的 root 抛 TypeError；其他文件系统、YAML、重复与关联错误为 InputReadError，含 source_path、location、message。依赖读取失败保留其自身来源和位置。

InputBundle 公开只读字段：

| 字段 | 类型与含义 |
| --- | --- |
| root | 规范绝对目录 Path |
| meshes | Mapping[Path, MeshResource]，规范绝对 mesh 路径为键 |
| robot_models | Mapping[Path, RobotModel]，规范绝对机器人配置路径为键 |
| scenes | Mapping[str, Scene]，scene_id 为键 |
| generations | Mapping[Path, Generation]，规范绝对 generation 文件路径为键 |

集合为只读快照；字段不能赋值或删除。模型、mesh、scene 与 generation 关联保留对象身份，不深冻结或复制可变 frame／实例。资源集合仅取 context 的公开快照，按首次成功登记顺序；不公开可变 context。scenes 按声明顺序，generations 先按所属场景声明顺序、再按发现文件名字典序。Generation 没有 generation_id，同名文件在不同目录是不同条目。

## 根配置与发现

根文件固定为 `bundle.yaml`，必需且仅有 `scene_directories`，其值为非空字符串列表。拒绝重复键、未知字段、null、非法类型及空条目。不自动扫描备用目录、不递归、不扫描未声明目录或无关资源。

每项目录引用拼接 `scene.yaml` 后，通过公开 `resolve_file(..., relative_to=bundle_path)` 解析。引用相对根配置，允许包内 `..`；绝对路径、URI、缺失／不可读／非普通文件及符号链接解析后的包外目标均拒绝。规范 scene 路径重复（文本、`..`、符号链接别名）拒绝。

`scene_path.parent` 是实际场景目录，末级目录名必须等于读取结果的 scene_id；不同规范路径的 scene_id 冲突也拒绝。目录或 scene 文件符号链接以真实 scene 所在目录为准。在该目录发现直属 `generation.yaml` 与 `generation_*.yaml` 的并集，按文件名字典序读取，每景至少一份。匹配名字的目录、坏链接或不可读文件报错，不静默忽略；不匹配文件不读。

每个 generation 规范路径全包唯一。每份 generation 通过公开 read_generation 读取，`generation.scene is 本目录名义 scene` 必须成立；引用同一规范 scene 的别名合法，引用其他场景即使 ID 相同也不合法。不合并生成规则、不补初始分布默认值。

不同模型配置路径产生同一 model_id 时在 bundle 层拒绝；同配置跨场景共享合法。不改变 context 按路径共享的规则，不按 ID 合并模型，不限制不同 Scene 重用实例／frame ID，mesh 没有额外 ID 规则。

## 验证边界

在[Docker 环境](../../docker/README.md)运行 `python -m unittest discover -s tests/bundles -v`。检查发现规则、身份、只读集合、输入不变、失败重试、包内路径及真实包完整搬移。读取不打开 mesh 内容，不执行采样、场景复制、FK／IK、碰撞、规划或输出，不证明随机样本可行。文件系统检查只针对读取时状态，不承诺抵御并发文件替换。
