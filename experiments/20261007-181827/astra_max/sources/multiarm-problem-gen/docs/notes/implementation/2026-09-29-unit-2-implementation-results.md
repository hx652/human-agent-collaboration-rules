# 单元 2：机器人表示与读取实现记录

日期：2026-09-29。依据已确认的[单元 2 方案](../discussions/2026-09-29-unit-2-robot-model-and-reading.md)实施；本文记录实际结果，不替代公开契约。

后续修正：用户于 2026-09-30 确认暂时移除 Material，详见[删减记录](2026-09-30-remove-material-support.md)。下文保留 2026-09-29 当时的实现与验证结果。

## 起点与完成内容

实际起点为 main 的 `a6f7d54`，比 origin/main 超前 12 个提交；已有 `docs/README.md` 修改及未跟踪的单元 2 方案。保留这两项设计输入，创建 `codex/robot-model-reading`；方案原文未修改。本轮未提交、合并或推送。

新增[资源契约](../../contracts/resources.md)与[机器人契约](../../contracts/robot-model.md)，随后实现 `multiarm_problem_gen.resources` 和 `multiarm_problem_gen.robots`。ResourceContext 规范化包内路径、检查文件与符号链接目标、复用 STL／DAE 描述，不加载内容。InputReadError 统一提供来源、位置与原因。

RobotModel 合并 YAML 和 URDF，有效限制只保存在 Joint；没有 RobotConfig 或覆盖前值副本。Link／Joint、TCP、规划顺序、mimic 与碰撞排除对关联模型内对象；嵌套结果只读。惯性张量、质量、位姿、动力学及 surface 分组全部保留。visual／collision 使用有效 Geometry.local_pose，mesh 使用有效缩放；其他可选项保持 None，通过 effective_* 属性解释格式默认。Origin 分开保留 xyz/rpy 的缺失，使当前适配器惯性 origin 省略 rpy 的情况也不会丢失。

读取器拒绝未知元素／属性、YAML 重复键与 null、无效引用、非法参数、结构环和配置冲突。检查命名配置及固定值可确定的 mimic 结果，不计算运动学。公开记录可以按契约构造，但跨对象及输入校验集中在 read_robot_model；直接拼装记录不能替代读取验收。

## 实际验证

现有 Compose 环境以 `BUILD_NETWORK=host` 重建，Python 3.13.15、PyYAML 6.0.3。PyYAML 已在 [PyPI 发布页](https://pypi.org/project/PyYAML/6.0.3/)核实并于 pyproject.toml、Dockerfile 固定；构建日志确认安装 CPython 3.13 Linux wheel。不声明所选版本为最新版。

| 检查 | 结果 |
|---|---|
| Compose 构建及就绪检查 | 通过 |
| docker/check_environment.py | 通过，含 PyYAML 版本、可编辑安装、源文件更新与 UID/GID 1000:1000 |
| tests/resources | 3 项通过 |
| tests/robots | 14 项通过，包含真实输入的两项完整核对及独立小算例；错误输入使用多组 subTest |
| 单元 1 的公开 unittest 验收命令 | 21 项通过；未阅读内部测试源文件 |
| pip check | 通过，无依赖冲突 |
| 新生产文件 Python 3.10 语法解析 | 通过；未在 Python 3.10 运行环境执行测试 |
| Docker 说明中的真实机器人读取示例 | 已执行通过，输出模型标识、数量、规划顺序、TCP、home 与限位 |
| 最终差异检查 | git diff --check 通过；examples、primitives、其测试与契约及 tools 无改动 |

真实验收直接读取当前 `examples/ur7e_table/resources/robots/ur7e_2f85/robot.yaml` 与 `robot.urdf`：25 个 Link、24 个 Joint、17 个 visual、17 个 collision、17 份惯性信息、5 条 mimic、2 处 surface、11 个碰撞排除对。XML 验收逐元素登记并核对全部属性，最后确认登记集合覆盖整棵 XML；旋转以独立旋转矩阵预期核对四元数，配置按规划顺序核对。测试确认模型中的关联对象身份一致。

真实读取期间只允许打开 YAML 与 URDF；独立算例使用刻意无效的 mesh 内容，禁止打开 mesh 仍能读取成功，搬移输入包后资源路径随之更新。真实输入读取前后字节一致；小算例搬移后的全部输入摘要一致。小算例另覆盖默认值与部分缺失、可放宽的字段覆盖、连续 mimic、固定值与命名配置有效限位、只读性、包外路径与符号链接、未知内容及结构错误。

过程中真实数量断言曾失败：agent 手工计为 26/25，源 XML 独立计数证实是 25/24；修正的是测试预期，不是模型。复核时还修正了配置入口使用包内符号链接时的 basename 处理，并新增回归。最终相关测试全部通过。命令与真实读取示例见 [Docker 说明](../../../docker/README.md)。

## 契约与阅读边界

单元 1 的公开契约足以完成本轮，无须修改其行为或读取内部实现。辅助记录签名、原始可选 Origin 分量与 effective_* 查询在本轮契约中具体化；未发现需要返回架构讨论的阻塞问题。无全局资源缓存、无机器人模型缓存，资源 context 的生命周期仍归外层。

读取范围为本任务 AGENTS.md、README、docs 入口、当前设计、指定方案、primitives 公开契约、Git 工作约定、环境配置、真实 YAML／URDF，以及本轮新增实现与测试。未读取 primitives 实现、内部测试源文件、描述其实现细节的首轮验收记录，亦未读取 tools 原型内部实现。公开验收输出进入上下文，属于允许的执行验证。agent 自述未发生范围外实现阅读，不将此表述为独立证明。

Serena 已初始化并切换到本项目，使用其符号概览检查本轮读取器；文件新增与限定范围检查使用本地工具。没有读取 Serena 记忆或运行全仓库 onboarding。另查阅 PyYAML 发布元数据与 [urdfdom 的默认值处理来源](https://github.com/ros/urdfdom/blob/1.0.4/urdf_parser/src/joint.cpp)，用于核实 limit／mimic 默认含义，没有引入 urdfdom 运行依赖。

当前桌面会话实际可访问此仓库。创建分支时 `.git` 的沙箱只读限制、Docker socket 的访问限制，均通过任务范围内的提权执行完成；没有要求丢弃改动或迁移工作区。宿主无 `python` 命令，少量文件／语法检查改用已有 `python3`；正式测试均在 Compose 内执行。

## 剩余边界与局部不足

- 支持当前无版本 URDF 的 fixed/revolute 子集；其他关节类型、版本扩展、transmission、gazebo 等明确拒绝，不能宣称通用 URDF 读取器。
- surface 保留现有分组值，不补后端默认，不做接触或动力学计算；惯性只作有限数及对角非负等基础检查，不证明物理可实现性。
- 命名配置与固定值检查位置限位及可确定的 mimic 链；不证明整个规划域满足所有 mimic 限位，不验证碰撞、可达性或 TCP 任务。
- 材质支持全局具名定义的引用和 visual 内自包含定义，纹理只保留包内路径。当前真实文件没有材质，相关行为仅由独立算例验证；未引用的全局材质不另设模型索引。
- 文件检查保证读取时包内约束，不提供并发文件替换防护；失败可留下 context 中已创建的资源描述，不返回半成品模型。
- 还没有 InputBundle／Scene／Generation 读取、采样或计算后端；这些不是本次未完成事项。没有在其他 Python 版本或其他平台重复验收。
