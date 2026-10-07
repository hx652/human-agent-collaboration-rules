# 单元 6：InputBundle 实施与验收

本次是用户授权的探索性自主试验，依据[单元 6 公开交接包](../discussions/2026-09-30-unit-6-public-handoff.md)实施，不表示用户最终接受 D6 设计。单元 6 由独立实现 agent 完成；没有提交或推送。

## 完成范围

- 新增 `src/multiarm_problem_gen/bundles/`，公开 BundleReader、InputBundle 与既有 InputReadError；契约先于实现写入 [input-bundle.md](../../contracts/input-bundle.md)。
- 根配置仅接受非空 scene_directories；按声明顺序读取规范 Scene，按真实目录发现直属 generation 文件并排序。检查目录 ID、规范路径重复、scene/model ID 冲突及 generation.scene 引用身份。
- 每次 read 新建 context；只通过公开 resolve_file、get_scene 与资源快照协作。仅成功交付完整包；只读集合保留对象身份，未引入私有缓存访问、深冻结或场景复制。
- 新增 `tests/bundles/_fixtures.py` 与 `test_bundles.py`：独立构造小型 YAML／URDF／占位 mesh，不复用依赖内部测试或 fixture。
- 样例新增 bundle.yaml，README 增加完整包及 Generation 独立读取入口和旧 ID 迁移说明。scene.yaml 仅将 `ur7e_table_baseline` 改为 `tabletop`；实际 Git diff 为一行删除、一行新增，其他场景字段及真实几何、位姿、关节、模型、generation 参数未改。

共享 README、Docker、docs 入口以及既有场景测试的旧 ID 适配由主 agent 负责，不在本 agent 的修改范围内。

## 测试目的与依据

编写测试前已在交流中说明：以 D6 公开规则与依赖公开契约为预期依据，自建两场景、多 generation 算例检查声明顺序、文件名顺序、共享身份、只读快照、输入不变及失败后重试。反例用于发现漏扫、错误去重、相同 ID 掩盖不同 scene 身份、模型 ID 冲突、错误来源丢失和包外路径逃逸。

真实 UR7e 包及整体搬移副本检查路径迁移、双臂共享模型、mesh 关联、初始状态仍为 None 和输入字节不变。读取期间拦截 builtins.open、io.open、os.open 对 STL／DAE 文件的打开；此检查约束本次 Python 读取路径，不声称覆盖任意外部进程或所有可能的 I/O 绕过。文件哈希与复制在拦截范围外完成，用于比对和构造搬移输入。

首轮通过后，自审发现不可读文件和 generation 指向包内其他实际位置尚缺明确测试，因此在补充前再次说明目的，增加不可读文件、根目录别名、generation 规范路径及失败字节不变检查。没有因为失败削弱契约。

## 实际结果

本 agent 在既有 Docker dev 环境执行：

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
docker compose -f docker/compose.yaml exec -T dev python -m unittest discover -s tests/bundles -v
```

- 首轮 36 项通过，unittest 报告 0.494 秒。
- 补充后最终 40 项通过，unittest 报告 0.527 秒，无跳过。覆盖空资源集合、同名 generation 跨目录、仅后缀规则文件、未声明／嵌套／不匹配文件不读、损坏与缺失输入、不可读文件、匹配目录／坏链接、根类型、ID 冲突、各种路径别名和逃逸。
- `git diff --check` 无问题；样例 scene 差异已单独检查为仅上述 ID 一行变化。
- 主 agent 于 13:26:16 UTC 检查点报告全套 Docker 166 项通过：21 primitives、12 resources、15 robots、20 scenes、25 distributions、29 generation、40 bundles、4 integration；环境检查及 pip check 通过。这里明确为主 agent 报告，本 agent 未另读那些测试源码、也未重复执行依赖回归。

这些结果证明本轮输入读取的被测行为，不证明采样统计、随机状态有效性、FK／IK、无碰撞、规划、输出或生成流程；读取时的文件系统检查不防御并发替换。

## 契约、阅读与工具

公开契约足以完成本次实现，未遇到需返回决策者的契约缺口，未修改依赖职责。D6-1 公开资源快照使 bundle 能交付本次加载集合，无需遍历内部缓存。

实施阶段实际阅读：

- 本仓库 AGENTS.md、README.md、docs/README.md、docker/README.md；按协作起始规则还读取 research-process 的 overview.md、state.md、projects/README.md，未写入这些长期记录。
- D6 公开交接包；六份公开依赖契约 primitives、robot-model、scene、resources、distributions、generation；未展开契约里的原始综合决定链接或前序内部实施记录。
- UR7e 样例 README、scene.yaml、generation.yaml 与公开 robot.yaml。
- Serena 的 ResourceContext 和 read_generation 公开声明／docstring，include_body=false；未取依赖符号正文。
- 本 agent 新写的代码、测试、契约与样例改动，以及限定到上述样例的 Git diff。测试阶段读取自身 fixture／测试及工具输出；真实包由测试执行公开读取器，搬移与哈希过程访问资源字节，不把 URDF／mesh 内容输出给实现 agent。

Serena 首次按 `src/multiarm_problem_gen/resources` 定位失败（该目录不存在），随后只在 `resources.py` 定位公开声明成功；不曾因此整文件读取。首次普通 Docker 调用因 socket 权限拒绝，之后通过已授权的测试权限执行成功，没有切换宿主 Python 或安装依赖。主 agent 的消息包含公开结果、数量和边界，没有依赖内部实现摘要。

上述阅读与边界是 agent 根据本轮过程的自述，不是独立证明。已知上下文中没有依赖内部实现或内部测试内容；没有发现意外越界内容，未声称由此证明绝无越界。

## 用时与用量

使用 clock 工具 UTC 时间锚点记录墙钟时间，工具执行等待计入相应区间：

- 13:18:02—13:20:57：公开契约阅读、声明查询、分析、契约及实现写入，连续实现区间 2 分 55 秒。首次时间锚点前的启动阅读未单独计时，末尾自审与记录也不包含在该数值内。
- 13:20:57—13:26:25：以测试目的梳理、fixture／测试编写、两次 Docker 执行及结果检查为主，墙钟区间 5 分 28 秒；其间穿插简短实现自审与沟通，不能将此数值等同净测试用时。未发生测试发现后的实现代码修正。
- 13:26:25—13:27:51 为收尾记录和交接检查，墙钟 1 分 26 秒，归入实现记录工作。没有等待用户或任务暂停；Docker 权限执行的工具等待包含在上述测试区间。

实现／测试交替活动无法可靠精确累计，保留可核实区间并说明混合范围，不补造净用时。工具未提供本 agent 的 token 用量统计；输入、输出、实现和测试阶段 token 均为**不可用**，不按文字长度或账户额度反推。
