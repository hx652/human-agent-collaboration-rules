# 统一资源管理公开契约

入口：`multiarm_problem_gen.resources`。本接口为一次输入包读取服务，不要求先读取 bundle.yaml。

```python
ResourceContext(root: Path)
context.root: Path
context.meshes: Mapping[Path, MeshResource]
context.robot_models: Mapping[Path, RobotModel]
context.scenes: Mapping[Path, Scene]
context.resolve_file(reference: Path, *, relative_to: Path) -> Path
context.get_mesh(path: Path) -> MeshResource
context.get_robot_model(path: Path) -> RobotModel
context.get_scene(path: Path) -> Scene
InputReadError(*, source_path: Path, location: str, message: str)
```

`root` 构造时解析为已存在目录的规范绝对路径，公开只读。`relative_to` 是包内已存在、可读的源文件绝对路径；`reference` 必须是相对文件路径。允许包内 `..`；解析符号链接后仍须在 root 内，且为存在、可读的普通文件。绝对引用、URI（包括 `package://`、`file://`）及包外目标均拒绝。读取器将文件内字符串转成 Path。

三个取得入口均接受包内文件的绝对 Path，规范化并再次检查。`get_mesh` 的后缀不区分大小写，仅支持 STL／DAE，返回基础表示的 MeshResource，不打开或解析 mesh 内容。`get_robot_model` 按机器人配置文件路径共享 RobotModel；`get_scene` 按 scene 文件路径共享名义 Scene。各类资源分别管理；同一 context、同类资源、同一规范路径返回同一对象，不同路径不按 ID、URDF 或内容合并，不跨 context 缓存。root 与输入文件不被修改。

模型／场景已有对象时直接返回，不调用 reader；未命中时分别调用公开 `read_robot_model(config_path=path, resources=self)`、`read_scene(scene_path=path, resources=self)`，仅成功后登记。失败不登记半成品，已取得的依赖可以保留。直接调用 reader 不隐式登记其自身结果，依赖仍通过 context 取得。模型与场景契约见 [robot-model.md](robot-model.md)、[scene.md](scene.md)。

`meshes`、`robot_models`、`scenes` 是只读属性，每次访问返回当时已成功登记资源的只读映射快照。键为规范绝对 Path，分别按各类资源首次成功登记的顺序迭代；值保留取得入口返回的对象身份，不复制资源。相同规范路径的再次取得不增加条目或改变顺序。先前快照不受之后加载影响，包括原先为空的快照。不能赋值／删除属性，也不能增加、替换或删除快照条目；这只冻结集合，不额外冻结 Scene 的可变状态。

直接 reader 的自身结果不出现在对应集合；它通过 context 成功取得的依赖可以出现。失败的模型／场景不出现在集合中，失败之前成功取得的依赖仍可见。这些快照不提供手动登记、清空、替换或热更新能力，也不承诺跨线程的原子读取。

context 的生命周期对应一次输入包读取，无全局缓存和热更新；修改输入后创建新 context。共享表中的 Scene 是供多份 Generation 使用的名义场景；生成过程另建具体场景，不能修改名义场景或把生成结果放入该表。目前这是使用约定，不增加只读包装。本轮没有手动登记接口，不定义未来重复登记、替换和路径与对象一致性规则。

路径无效、缺失、不可读或格式不支持时抛 `InputReadError`（ValueError 子类），公开字段 `source_path`、`location`、`message` 用于诊断。资源独立调用的路径 location 为 `root`、`reference`、`relative_to`、`mesh`、`robot_model` 或 `scene`；读取器补充引用所在 YAML／XML 位置。依赖解析错误保留其源文件及位置。失败不返回资源，但不回滚之前已缓存的依赖。

公开调用传入非 Path（包括字符串），或 location/message 非字符串，抛 TypeError。文件系统检查针对读取时状态，不承诺抵御并发替换文件。无全局状态、mesh 内容加载、目录发现或打包操作。
