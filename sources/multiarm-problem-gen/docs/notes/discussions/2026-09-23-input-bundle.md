# InputBundle：输入包的组织与读取入口

日期：2026-09-23

状态：讨论与方案记录，尚未实现；未据此迁移当前样例。承接[领域表示](2026-09-22-input-domain-representations.md)及[分布与作用关联](2026-09-23-generation-distributions.md)的讨论。

## 从目录管理到输入包

用户希望单独表示输入目录，方便管理 mesh 资源、多个 scene 及对应的 generation。agent 建议命名为 InputBundle（输入包），并同时管理共享 RobotModel，避免多个场景分别解析同一模型。

局部方案：InputBundle 保存规范化绝对路径类型的根目录，以及 MeshResource、RobotModel、Scene、Generation 集合。每份 Generation 显式引用对应的 Scene；一份 Scene 可以对应多份 Generation。资源集合不意味着提前加载 mesh 内容。

## 如何发现场景与生成规则

用户提出根目录 YAML 指定需要加载的场景文件夹，并要求文件夹名称与 scene 名称一致。讨论具体化为：根配置叫 bundle.yaml，列出 scene_directories；场景目录末级名称必须等于 scene.yaml 的 scene_id，不一致时报错，不自动改名。

目录内部采用本轮示例中的约定：每个场景目录一份 scene.yaml，加载其直属的 generation.yaml 和 generation_*.yaml，不递归扫描。各份 generation 保留显式 scene 引用，并检查它指向本目录的 scene.yaml；这样 generation 仍可作为独立读取入口。

## 目录与配置示例

```text
my_input_bundle/
├── bundle.yaml
├── inputs/
│   ├── shared_table/
│   │   ├── scene.yaml
│   │   ├── generation.yaml
│   │   └── generation_dense.yaml
│   └── narrow_workspace/
│       ├── scene.yaml
│       └── generation.yaml
└── resources/
    ├── robots/ur7e_2f85/
    │   ├── robot.yaml
    │   ├── robot.urdf
    │   └── meshes/…
    └── objects/ball/ball.stl
```

bundle.yaml：

```yaml
scene_directories:
  - inputs/shared_table
  - inputs/narrow_workspace
```

shared_table/scene.yaml 中 `scene_id: shared_table`，机器人配置引用为 `../../resources/robots/ur7e_2f85/robot.yaml`。同目录的两份 generation 均使用 `scene: scene.yaml`，可指定不同采样分布、数量或访问序列。示例省略其余既有字段及许可证、来源说明，不改变它们的要求。

## 路径、资源与实现边界

- 只加载 bundle.yaml 列出的场景目录；路径相对于包含引用的文件解析，内部使用规范化绝对路径对象，不依赖当前工作目录。
- RobotModel 和 MeshResource 沿 scene 的引用发现并在包内共享，不扫描资源目录中的全部文件；mesh 仍按需加载。
- 所有运行资源位于包内，整包移动后引用仍成立。相对路径用于文件关联，内部不只保存相对路径字符串。
- 输入包管理关系不要求实现为嵌套树；集合容器和读取接口仍待确定。

当前样例场景目录是 inputs/tabletop，scene_id 为 ur7e_table_baseline，且尚无 bundle.yaml。落实本方案时需要统一目录名与 scene_id、增加根配置并调整相关入口；本轮只记录方案，不把迁移记为已完成。
