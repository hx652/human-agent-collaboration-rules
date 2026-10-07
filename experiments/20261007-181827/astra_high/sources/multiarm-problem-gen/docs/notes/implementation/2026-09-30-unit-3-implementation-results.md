# 单元 3：场景与统一资源管理实施记录

日期：2026-09-30。依据[实施前方案](../discussions/2026-09-30-unit-3-scene-and-resource-context.md)及用户本次代码、测试、必要文档授权。原方案保留，不改写为结果。

## 完成范围

- 先整理 [Scene 公开契约](../../contracts/scene.md)和 [ResourceContext 扩展契约](../../contracts/resources.md)，再实现。构造／更新签名、字段及错误位置按方案具体化，没有增加新的领域职责。
- 新增 `scenes`：Scene、RobotInstance、Object、SceneRules、MountContact，以及严格的 `read_scene`。集合只读，关联保持引用身份；安装位姿仅在 Frame 中，规划关节状态支持 None／完整 tuple 整体替换、有效限位检查及失败保留旧值。
- 所有 frame 使用无前缀 ID，支持前向及跨类别父引用；检查统一名称空间、world 保留、引用存在和连通无环。内部按声明和父链组装，不要求 YAML 顺序与 frame 树一致。
- reader 支持 compound 的 box／sphere／cylinder／mesh、显式 frame 和安装接触规则；严格拒绝未知字段、重复键、null、非法类型／数值／引用。通过 context 取得依赖，不登记自身结果。
- ResourceContext 分别按规范文件路径共享 mesh、RobotModel 和名义 Scene；命中不调用 reader，未命中成功后登记。失败不登记半成品，成功依赖可保留。没有公开手动登记接口。
- 更新主 README、文档索引、Docker 使用与验收命令；在 design.md 追加同日实施状态，保留原有方案段落。

工作在原主题分支 `codex/unit-3-scene-design` 继续。开始时已有 AGENTS.md、docs/README.md、docs/design.md、scene.yaml 差异和未跟踪的方案文档；已保留，未重新迁移四处父名称。AGENTS.md 和 scene.yaml 的最终差异与开始快照一致，方案文档未编辑。未提交、合并或推送；research-process 记录未写入。

## 测试目的与依据

编写测试前在交流中说明了以下目的；预期来自已确认方案、公开依赖契约和独立输入，而不是按实现输出反推。

| 测试组 | 希望发现的问题与独立依据 | 保证边界 |
|---|---|---|
| 独立场景算例 | 小型 YAML／URDF 明确给出跨类别父链、前向引用、四类几何、单位默认、接触对象身份；反例覆盖重复／保留 ID、断链、环和严格输入检查 | 检查相对表示及关联，不计算世界位姿 |
| 规划状态 | 两关节实际树顺序 a→b，规划顺序 [b,a]；b 限位 [0,2]，a 限位 [-1,1]，独立预期 (1.5,-0.5) 合法、反序非法；另用公开构造验证有效缺省限位与空规划列表 | 只检查规划关节自身限位，不展开 mimic 或证明可行性 |
| 资源责任 | 公开 reader 调用计数验证 miss／hit／失败重试；实际 reader 验证直接读取不登记、不同路径不按相同 ID／URDF 合并、模型共享与场景状态独立 | 不增加线程安全、热更新、手动登记或替换语义 |
| 真实输入 | 方案给定 2 臂、7 物体、11 条环境几何、4 个显式 frame、2 个接触规则；样例已知安装位置及四处父关系 | 不验证 tools 原型、运动学、碰撞或 Generation |
| 读取边界 | 原输入和临时搬移副本均可读，禁止打开 STL／DAE 内容，逐文件内容比较与哈希复核 | 检查此次执行，不承诺文件系统并发替换安全 |

独立输入位于 `tests/scenes/fixtures/`，不复用 robots 内部测试或私有解析辅助函数。`shape.stl` 故意只是文本，用来验证资源描述与 mesh 内容加载的边界。

## 实际结果

在已运行且 healthy 的 Compose dev 容器内执行，环境检查确认 Python 3.13.15、固定工具版本、可编辑导入及 UID/GID 1000:1000；`pip check` 通过。

| 命令（容器内） | 最终结果 |
|---|---|
| `python -m unittest discover -s tests/scenes -v` | 20 tests，OK；含真实输入与搬移验收 |
| `python -m unittest discover -s tests/resources -v` | 5 tests，OK |
| `python -m unittest discover -s tests/primitives -v` | 21 tests，OK；仅执行，未读测试源码 |
| `python -m unittest discover -s tests/robots -v` | 15 tests，OK；仅执行，未读测试源码 |
| `python docker/check_environment.py` | PASS |
| `python -m pip check` | No broken requirements found |

合计 61 个测试方法，非空测试集；参数化子用例不另计数。完整宿主命令见 [Docker 说明](../../../docker/README.md)。新文档中的场景读取示例已单独执行：scene_id=`ur7e_table_baseline`，机器人／物体／全部 frame 数为 2／7／14，环境几何 11，接触条目 2，can_a_visit 的 parent.id 为 can_a，规划状态为 None。

首次场景测试为 19 项通过、1 项失败：路径诊断测试修改了 robot.yaml，但此前场景失败已按契约保留成功模型，测试错误地期待同一 context 重新解析文件。修正为文件变更后新建 context，随后全部通过；没有为此修改实现或弱化缓存契约，没有读取依赖内部代码。

收尾代码审阅另发现本轮 YAML loader 对显式 `!!map` 标记配序列节点缺少类型检查，可能泄漏 TypeError 或把空序列当映射处理。补充节点类型检查，并按文件错误统一为 InputReadError 的既定契约增加 `!!map [a]`、`!!map []` 反例；场景 20 项重新执行全部通过。这是本模块的局部错误处理修正，不是依赖契约缺口。

真实输入包 46 个文件在验收前后哈希一致；测试还逐字节比较原包及搬移副本。未修改真实输入和模型资源，未读取 mesh 为几何。最终范围检查确认 primitives、robots 及其测试、tools 没有工作区变更；`git diff --check` 通过。

## 阅读范围与工具边界

以下是本 agent 的阅读记录，结合工具输出供复核，不视为独立证明：

| 阶段 | 实际进入上下文的内容及用途 |
|---|---|
| 开始／实现 | research-process 的 overview.md、state.md、projects/README.md（用户协作约定要求的上下文）；目标仓库 AGENTS.md、README.md、docs/README.md、本次方案、docs/design.md；Git 分支／状态与原有四份已跟踪文件的差异 |
| 依赖契约 | docs/contracts/primitives.md、resources.md、robot-model.md；从文档取得构造、字段、有效限位和错误语义，没有读取 primitives／robots 的实现或内部记录 |
| 本任务代码与构建 | src/multiarm_problem_gen/resources.py、tests/resources/test_resources.py；pyproject.toml、docker/README.md、docker/compose.yaml；新建 scenes 实现与测试；Serena 对新建 model.py／reader.py 的符号概览 |
| 面向调用者的输入 | examples/ur7e_table/README.md、inputs/tabletop/scene.yaml；Docker 文档中的机器人读取示例。真实机器人与 mesh 文件经 reader／测试／哈希程序处理，没有把其内部资源内容输出作为实现参考 |
| 测试／收尾 | 本轮 fixtures、scenes 测试、资源测试及新文档；测试日志包括依赖回归的测试名称／简短描述，未展开依赖测试源码；环境检查只执行；范围核对只查看状态、差异及本轮代码的公开 import |

初始文件枚举看到 primitives／robots 的 `__init__.py` 路径名称，未读取内容。没有使用 Git 历史、跨模块引用查询、反编译或其他 agent 获取依赖内部信息；没有外部资料检索或子 agent。当前上下文未包含依赖内部实现摘要；按实际工具记录与本 agent 自查，未发现范围外实现进入上下文，不据此宣称已独立证明无越界。

Serena 可用：读取工具说明、从 research-process 切换到目标项目，用于新建模块的限定路径符号概览。resources.py 首次用文件读取完整查看（约百行，属负责范围），没有为重复获取内容再调用符号正文。未执行会扩大范围的 onboarding 或全仓库源码扫描。

宿主没有 `python` 命令，`python3` 为 3.10.12；正式测试使用仓库容器。首次 Compose 检查缺 LOCAL_UID／LOCAL_GID，补齐后默认沙箱无法访问 Docker socket；经工具权限升级获准后检查及执行容器命令，没有自动审批拒绝。未安装或修改环境依赖，未重建／停止容器。

## 用时与 token

计时使用 `clock.curr_time` 返回的 UTC 墙钟时间，并换算为 Asia/Shanghai。按实际活动阶段划分，包含阅读、分析、编写、交流及工具等待，不是 CPU 时间或人工有效工时；阶段边界存在工具调用粒度的误差。

- 17:03:58–17:10:33：实现阶段，6 分 35 秒，含初始材料／契约整理、实现与环境定位。
- 17:10:33–17:15:48：测试阶段，5 分 15 秒，含目的落实、测试编写、执行、测试预期修正和回归。本阶段没有实现行为修正；修正的是测试对缓存的预期。
- 17:15:48–17:20:27：实现收尾，4 分 39 秒，含文档、docstring、代码审阅、YAML 节点类型检查修正及范围核对。包含一次文档示例验收（工具报告进程墙钟约 0.12 秒），无法可靠将其准备／分析时间从此段细分，故标明混合边界，不虚构纯实现／纯测试秒数。
- 17:20:27–17:20:46：测试补充与重跑，19 秒。两次主要测试阶段累计 5 分 34 秒；两次实现阶段累计 11 分 14 秒（包含上述无法细分的文档示例验收）。
- 17:20:46–17:21:23：最终记录与交接整理，0 分 37 秒，单列，不纳入上述代码实现／测试累计。
- 没有等待用户答复或任务暂停；自动审批及工具往返等待包含在所在阶段，未单独可靠计量。统计截至本记录最后更新，后续最终答复时间未计入。

Token 统计：不可用。当前工具没有提供本任务输入／输出 token 消耗或阶段统计；命令输出的 token 长度不是模型用量，未据此或账户额度反推数字。

## 契约判断及剩余限制

公开依赖契约足以完成本轮范围，实际运行未发现阻塞性的契约缺口；没有因职责、数据语义、状态归属或依赖边界的新决定暂停并返回讨论。读取器的局部解析辅助代码独立实现，未复用 robots 私有函数；场景入口复用本轮负责的 resources 内部路径校验，未新增公开路径／登记接口。

名义 Scene 的可变 frame／实例状态仍依赖调用约定保护；无只读名义包装、复制或生成能力。世界根只在构造时检查，不修改基础 Frame 以阻止后续 pose 更新。状态校验不展开 mimic，不证明接触、碰撞或可达性。有关节环境物体、机器人内部 link frame、Generation、完整 InputBundle、目录发现、计算后端与手动登记规则仍在范围外。tools 对旧名称的兼容性未验证。无本轮已知未完成的功能性阻塞。
