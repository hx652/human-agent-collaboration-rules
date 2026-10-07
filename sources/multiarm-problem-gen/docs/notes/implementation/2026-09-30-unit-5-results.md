# 单元 5：Generation 独立实现与验证

本轮为用户授权的探索性自主试验，不表示最终设计接受。实现 agent 从过滤后的[公开交接包](../discussions/2026-09-30-unit-5-public-handoff.md)独立实施 D5-1/2/3；没有继承先前停止 agent 的实现或测试，未读取其记录。主 agent 告知原 `generation.md` 仅为公开契约草稿，本 agent 按交接包重新编写，未读取该草稿。

## 完成范围

新增 `src/multiarm_problem_gen/generation/`，包含公开入口、只读领域表示、严格 YAML reader。公开 `read_generation`、Generation、SamplingBinding、GoalTolerance、Completion，并重导出 InputReadError。绑定保留顺序及场景对象身份；检查完整初始覆盖、分量重叠、异场景对象、目标种类、固定容差及完成条件。YAML 将轴和规划关节映射转为明确顺序，命名中心解析成数值；数值关节名 configuration 按 D5-3 消歧。越限分布参数不被裁剪或拒绝。名义 Scene 通过公开 context 共享，不修改 frame 或初始状态。

更新 `docs/contracts/generation.md`；新增 `tests/generation/test_generation.py`，小型 YAML/URDF 输入由测试自己写入临时目录，不借用依赖测试 fixture。未修改共享入口、真实样例或依赖实现；未提交或推送。

## 测试目的、依据与结果

编写测试前已在交流中明确三组目的：手算两关节输入验证轴及关节顺序、configuration 消歧、绑定和序列身份；严格非法输入验证漏校验、位置诊断和完整覆盖；真实双臂输入验证六维参数、四次访问及名义状态不变。独立预期来自公开交接包、公开依赖契约及手写输入常量，不从依赖实现或内部测试生成。

测试覆盖公开直接构造的类型／数值／关联限制、只读快照、拆分初始 binding、重叠／异场景拒绝、零关节与空场景、缺失可选分组、元数据、退化分布、越限参数、严格字段／重复键／null／非法映射键、文件与场景引用错误、依赖错误源保留、重复访问与跨臂共享。

在仓库既有 Docker Compose dev 环境执行，使用调用者 UID/GID；未改用宿主 Python：

```bash
export LOCAL_UID="$(id -u)"
export LOCAL_GID="$(id -g)"
docker compose -f docker/compose.yaml exec -T dev python -m unittest discover -s tests/generation -v
```

首轮 28 项通过，unittest 报告 0.874 秒。最终审阅发现非法控制字符会在 PyYAML 创建 loader 时就报错，原错误包装未覆盖该阶段；在自身 reader 修正，并补充控制字符及非法路径的独立输入检查。最终 29 项通过，unittest 报告 0.861 秒，退出码 0。真实示例得到 13 个 binding、两个六维初始分布及每臂四次访问；读取前后 scene/generation 输入字节、所有 frame.pose 身份及名义机器人 None 状态保持一致。

本 agent 未重复执行依赖回归；主 agent 提供的依赖验证状态仅作为交接信息，不当作本 agent 运行证据。`git diff --check` 对当时已有跟踪文件未报告错误；本单元新增文件仍未暂存，不能据此宣称该命令覆盖新增文件。

这些测试只证明所覆盖的读取与表示行为；不证明采样统计、碰撞、FK/IK、随机可行性或完整生成流程，也不是对所有非法 YAML 组合的穷举。

## 读取边界与用量

实现阶段实际请求并读取：

- 仓库 AGENTS.md、README.md、docs/README.md、docker/README.md：工作约定、公开入口及测试环境。合计 378 行；入口包含旧阶段说明，未循链接展开内部实施记录。
- docs/notes/discussions/2026-09-30-unit-5-public-handoff.md：56 行，仅 D5 公开摘录。
- docs/contracts/{primitives,robot-model,scene,resources,distributions}.md：267 行的公开依赖契约。首次合并返回有截断，随后重读 robot-model、scene、resources，重读请求合计 161 行；未取得依赖源码或内部测试。
- 真实 inputs/tabletop/{scene,generation}.yaml 和 resources/robots/ur7e_2f85/robot.yaml：475 行，用于格式与独立预期。未打开真实 URDF 或 mesh 内容。
- Git 状态／分支、以上文件行数；状态输出仅带其他工作的路径名称，没有读取其内容。自己的新增实现与测试内容来自本轮编写和测试返回。
- Serena initial_instructions 的工具文档：当前激活项目为 research-process。本轮不存在需定位的已有自身符号，故直接使用文件工具新增实现；没有执行 onboarding、全局搜索、记忆读取或依赖符号正文读取。

上述独立源文件合计 1176 行（去重文件行数，不是 token 估计；重复请求和工具说明另列）。测试阶段不新增依赖阅读；测试执行真实依赖但不主动提取其源码。主 agent 的交接提供了 API 摘要、依赖测试数量及先前 agent 停止情况，没有提供依赖内部实现摘要。agent 自述本轮未发现阅读越界；这不是独立审计证明。

计时采用 clock 工具 UTC 墙钟。首个计时点 13:09:09，此前启动阅读时间未被可靠记录；至 13:13:11 为可识别实现阶段 4 分 02 秒。13:13:11 起进入测试目的整理、测试编写和执行；13:17:29 最终审阅计时点到 13:17:45 有明确实现修正区间 16 秒。13:18:23 最终验证结果已取得。从首个计时点到最终验证为 9 分 14 秒，包含交流、执行、审阅及修正；最终记录编写未计入。测试与后段审阅／修正交替，完整实现累计和测试累计不可可靠分离，因此完整分项用时均为不可用，不补造精确总数。没有等待用户批准或任务暂停。工具未提供本 agent token 消耗统计，输入／输出及阶段 token 用量均不可用；不据文本长度或账户额度反推。

## 契约与局限

公开交接包与依赖契约足以完成本轮实现，未产生需要复议的新架构问题，也没有扩展依赖阅读。读取器只保留已确认任务字段，不提供采样、FK、场景复制、应用扰动或后端执行。共享场景仍具有公开可变能力，本模块只保证自身读取／构造不改它；调用者仍须遵守名义场景使用约定。公开对象 docstring 与输入校验标记已加入。后续 U6 可仅依赖公开 Generation 契约继续。
