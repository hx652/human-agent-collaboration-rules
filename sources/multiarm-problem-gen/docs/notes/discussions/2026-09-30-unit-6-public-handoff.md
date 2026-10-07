# 单元 6 公开交接包

从独立决定 D6-1/2/3 摘取，供严格隔离实现阅读；不包含依赖内部或内部测试。探索性 agent 决定，不代表用户接受。共享入口和既有验收入口的元数据适配由主 agent 维护。

## D6-1：先补公开资源快照

由**独立 resources 实现 agent** 承担最小补丁：`ResourceContext.meshes: Mapping[Path, MeshResource]`、`robot_models: Mapping[Path, RobotModel]`、`scenes: Mapping[Path, Scene]` 三个只读属性。每次访问取得当时已成功登记资源的只读映射快照，键为规范绝对路径；保留资源引用身份，按首次成功登记顺序迭代。先前快照不随之后加载变化，不能赋值／删除属性或修改映射。直接 reader 的自身结果仍不登记；它通过 context 成功取得的依赖可见。失败加载不出现半成品，之前成功依赖仍可见。原有加载和路径契约不变，无手动登记／清空／替换 API。

**理由与排除方案：**InputBundle 需要准确交付本次加载集合；遍历 Scene 公开图收集易漏掉依赖资源，并重复表达资源管理逻辑。只读快照最小且使调用者不依赖缓存内部，拒绝公开可变字典或让 BundleReader 访问私有表。

**修改范围：**既有 resources 所属实现、其专属测试、`docs/contracts/resources.md`。由该 agent 读取自己的实现；其他 agent 只读此决定和更新后的公开契约。可与 U4 并行，但 U6 以此补丁完成为依赖。

**验收：**三类空快照；加载后的键、身份与顺序；同一路径复用不增条目；快照不可修改且不随后续加载变化；加载失败不登记半成品但保留已成功依赖；直接 reader 不登记自身；原资源测试回归。测试只证明集合与登记时序，不加载 mesh 内容。


## D6-2：输入包公开入口与严格发现

新增 `multiarm_problem_gen.bundles`，公开 `BundleReader`、`InputBundle`、现有 `InputReadError`：

```python
BundleReader()
reader.read(root: Path) -> InputBundle
# InputBundle 公开只读字段：
# root: Path
# meshes: Mapping[Path, MeshResource]
# robot_models: Mapping[Path, RobotModel]
# scenes: Mapping[str, Scene]
# generations: Mapping[Path, Generation]
```

InputBundle 的构造／交付入口仅承诺 BundleReader.read，不新增手工组装契约。每次 read 新建一个 ResourceContext，不保存跨次缓存；root 为规范绝对目录 Path。所有集合只读快照、资源与 scene 保留原对象身份；不进行深冻结或复制可变 Frame／实例。资源集合取 D6-1 公开快照；scenes 按 scene_id 查询，generations 按规范绝对 generation 文件路径查询。Generation 当前没有 ID，不臆造 generation_id；同名 generation.yaml 在不同场景目录是不同条目。InputBundle 不公开可变 context。

根文件固定 `bundle.yaml`，必需且仅有 `scene_directories`，为非空 YAML 字符串列表；不添加 schema_version 或自动扫描备用规则。重复键、未知字段、null、非字符串／空字符串条目拒绝。root 参数非 Path 为 TypeError；其他文件系统、YAML、重复及关联错误为 InputReadError，包含源文件与位置；读依赖失败保留依赖来源。成功才返回完整 InputBundle，失败不返回半成品，也不改输入文件。

**目录解析不扩展 context API：**将每个相对目录引用与 `scene.yaml` 拼接后，调用 `context.resolve_file(reference, relative_to=bundle_path)`。沿用包内 `..` 允许、绝对／URI／包外目标拒绝及符号链接规范化规则；不得访问 context 私有函数。解析后的 scene_path.parent 是实际场景目录，也是 generation 发现目录；它的末级目录名必须等于 scene.scene_id。符号链接别名不会另创目录身份；如果目录或 scene.yaml 经符号链接指向另一个包内目录，就以实际 scene 文件所在目录为准。

场景按 scene_directories 列表顺序读取；规范 scene_path 重复立即拒绝（包括重复文本、`..` 别名和符号链接）。不同规范场景路径使用同一 scene_id 也拒绝。每个实际场景目录只发现直属 `generation.yaml` 和 `generation_*.yaml`，不递归；两种模式取并集、按文件名字典序读取。匹配路径必须可读普通文件且规范后在包内，目录伪装成匹配名字也报错，不静默忽略；不匹配文件不读取。每个场景**至少一份**匹配的 generation，否则失败；不要求一定存在 generation.yaml。

每份 generation 通过公开 read_generation 读取，返回的 `generation.scene` 必须 `is` 此目录 context.get_scene(scene_path) 的对象；这校验显式引用指向本目录 scene 的规范文件身份。各 generation 规范路径不得重复（同目录／跨目录符号链接别名也拒绝）。输入包不自动合并多份生成规则，不给缺失初始分布补默认。

共享资源按规范路径复用；meshes 与 robot_models 的顺序沿用 context 首次成功登记顺序。不同配置路径若产生相同 model_id，**InputBundle 层拒绝模型 ID 冲突**；context 仍保持原有“不同路径不按 ID 合并”的契约，独立读模型仍可得到不同对象。mesh 没有 ID 冲突规则；不同路径即不同资源。不同场景复用同一配置路径的 model_id 不算冲突。相同对象实例 ID／frame ID 只需在各自 Scene 内唯一，不跨场景禁重。

**理由与排除方案：**严格枚举与至少一份规则，使一个已声明场景不会被静默忽略；generation 无既有 ID，路径是无需改格式的自然标识。拒绝排序场景目录（会丢失声明次序）、默默去重、按内容合并、全资源目录扫描及跨 context 缓存。不增加 resolve_directory API，现有公开文件解析足够完成本阶段发现。模型 ID 唯一性只约束完整包交付，避免未来按模型 ID 输出时出现歧义，不借此改变资源共享机制。

## D6-3：真实样例最小迁移与验收

为 `examples/ur7e_table` 新增 `bundle.yaml`：

```yaml
scene_directories:
  - inputs/tabletop
```

仅将 `inputs/tabletop/scene.yaml` 的 scene_id 从 `ur7e_table_baseline` 改为 `tabletop`，其他数值／几何／位姿／关节／模型／frame／generation 字段不变；更新样例 README 明确 bundle 入口与 generation 单独读取入口。理由：目录重命名会改变既有文件入口和工具路径，另建完整样例会复制真实模型资源。scene_id 是逻辑命名而非物理数据，改名影响按旧 ID 查找的调用者，文档必须注明；不去改写历史检查结果或 tools 原型。本迁移必须在实施时检查差异，证明没有混入真实数据变更。

**修改范围：**新 bundles 模块、其专属测试及小型测试资源、`docs/contracts/input-bundle.md`、上述样例两项输入／README、必要文档入口与实施记录。resources 扩展由 D6-1 的专属 agent 完成；U6 不修改其内部。只消费公开依赖契约，不读取依赖内部测试。

**验收：**多场景／多 generation 的确定顺序；同模型／mesh 共享身份；Generation.scene 身份；只读集合与绝对规范路径；缺根配置／缺目录或scene／缺generation／损坏依赖、目录名不等scene_id、scene/model ID 冲突、规范重复路径、未知字段／重复键／null、错误 generation.scene、绝对／URI／包外引用及符号链接逃逸；包内符号链接别名按规范身份处理；不加载未声明目录或无关资源。真实包完整读取、共享双臂 RobotModel 和 mesh、保留初始 None 状态；搬移整个真实输入包到临时目录后再次读取，核对路径全部迁移至新根且引用仍一致。输入文件不改、mesh 内容未被打开。相关依赖回归通过；不执行采样／场景复制／计算／输出，不宣称随机样本有效。
