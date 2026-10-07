# 输入读取：运行流程与对象协作

日期：2026-09-28

状态：本轮讨论方案，尚未实现。Python 实现方向已明确；数据含义沿用此前讨论，以下读取组织与 class 协作作为设计方向，精确模块、接口和可变性仍待确认。

## 从对象清单转向运行流程

用户要求方案说明每一步做什么，以及 class 如何协作，而不是只列输入规定和参与对象。讨论使用“数据表示”称呼程序中的机器人、场景、分布等对象，不另引入难以理解的术语。

倾向将文件读取与数据表示分开：读取器解释文件、解析路径并建立跨文件关联；数据对象保存已解析的内容和关联，也可以具有自身相关的运算或检查方法。相比 Scene.from_yaml(path)，分开更适合本项目的多文件引用与资源共享，但不要求预建读取器继承体系。

选择 reader 的主要理由是：读取不只是把字段存进对象，还需要查找或复用资源、创建对象、解析引用并建立关联。这些工作跨越多个对象和文件，由 reader 组织更容易理解和管理，数据类则保存结果并表达自身行为。建立关联本身并不强制要求 reader，放在数据类中也能实现；这里是职责划分的取舍。依赖方向保持为 Generation 引用已建立的 Scene，读取 Scene 不需要反向读取 Generation。

## 运行流程与职责

以 `BundleReader.read(root: Path) -> InputBundle` 组织整个过程，维护本次读取的共享资源表。数据对象不自行打开输入文件。

| 步骤 | 工作及 class 协作 |
|---|---|
| ① 找到输入 | BundleReader 读取根配置，找到 scene、generation 文件，解析路径并建立读取范围。 |
| ② 建立机器人模型 | 遇到机器人配置时先查共享表，已有则复用，否则解析并创建 RobotModel。模型组织 Link、Joint；Joint 关联父子 Link；Link 的几何条目引用基本形状或共享 MeshResource。公共配置与 URDF 按已确认规则整合。 |
| ③ 建立场景 | 创建 Scene 中的 Frame 并连接父子关系。Object 引用自身 Frame 和几何列表；RobotInstance 引用共享 RobotModel 和安装 Frame。名义规划关节状态保持未指定。 |
| ④ 建立生成规则 | 根据已有 Scene 解析 Generation。创建分布和 SamplingBinding，将分布关联到具体 frame 或机器人实例，保存属性类别及有序分量映射；命名中心解析为数值，访问序列引用已有机器人和目标 frame。 |
| ⑤ 检查并交付 | BundleReader 完成引用、维度和必要状态等一致性检查，组织共享资源、scene、generation 并返回 InputBundle。失败时报告输入问题，不交付缺失关联的半成品。 |

②和③可交错执行：读取场景遇到机器人配置时再加载或复用模型，不要求先扫描全部资源。流程结束后不再需要重新解释 YAML／URDF 的路径和名称；mesh 文件仍由后续使用者按需加载。

## 一个协作例子

```text
InputBundle
├── 共享 RobotModel：UR7e＋夹爪
├── Scene
│   ├── arm_a：引用该 RobotModel 和安装 Frame A
│   ├── arm_b：引用该 RobotModel 和安装 Frame B
│   └── can_a：引用物体 Frame 和几何列表
│       └── 访问目标 Frame 以物体 Frame 为父
└── Generation：引用上面的 Scene
    ├── 位置扰动 binding
    │   ├── 引用二维均匀分布
    │   └── 关联 can_a 的 Frame、位置属性、[x, y]
    └── 初始状态 binding
        ├── 引用六维高斯分布
        └── 关联 arm_b、初始关节属性、有序关节列表
```

图中展示引用关系，不要求内部采用嵌套树存储。读取器建立关联，数据对象保存关联；分布只描述数值规律，binding 指定其目标，应用语义由目标属性固定决定。Generation 不复制 Scene；不同机械臂的实例状态不进入共享 RobotModel。

## 边界与后续

本阶段只读取和表示，不采样、不生成新场景、不加载 mesh 内容、不做运动学或碰撞计算。读取成功不代表场景无碰撞或目标可达。

BundleReader 负责组织，不意味着所有解析逻辑集中到一个大类；内部可以按职责拆成函数，是否形成独立读取器 class 留待模块边界讨论。不提前列出所有内部类、私有方法和辅助函数。

精确公开契约、对象可变性、错误规则及首版支持范围仍需确认，再进入实现。输入包组织见 [InputBundle 方案](2026-09-23-input-bundle.md)，数据表示见[此前讨论](2026-09-22-input-domain-representations.md)，分布关联见[Generation 讨论](2026-09-23-generation-distributions.md)。
