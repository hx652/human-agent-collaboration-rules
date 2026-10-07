# 暂时移除 Material 支持

日期：2026-09-30。状态：按用户确认完成代码修改，尚未提交或推送。

## 原因与变更

独立代码审查指出，当前真实 URDF 没有 material，原实现加入颜色、纹理和全局材质引用的需求依据不足。用户确认暂时删去 Material；这是本次公共接口收缩的授权，不是对其他表示的重新设计。

删除 `Material` 类及公开导出、`Visual.material` 字段、全局材质表和颜色／纹理／引用解析。Visual 保留 geometry 与可选 name；Link.visuals／collisions 的只读 tuple 不变。读取器遇到全局 material、visual 内定义或引用时，通过既有未知元素检查抛出带文件及元素位置的 InputReadError，不静默丢弃。

同步[机器人公开契约](../../contracts/robot-model.md)，清理独立算例的材质和原材质成功／参数校验断言，新增三类 material 输入的拒绝检查。保留原有符号链接入口、非法编码和真实 URDF 全字段验收。原[单元 2 实现记录](2026-09-29-unit-2-implementation-results.md)保留当时结果，并链接本次修正。

## 验证与边界

起点为 `codex/robot-model-reading` 的 `b82d7f4`，工作区原先干净。现有 Compose dev 服务健康，执行 `python -m unittest discover -s tests/robots -v`：15 项全部通过，包含 material 拒绝的三个子算例，以及真实 UR7e 的完整字段和配置核对。当前真实输入仍完整读取，输入文件未改动；本轮未重跑未受修改影响的 resources／primitives 测试。

本次检查限定在机器人代码、对应测试、公开契约及关联文档。未读取 primitives 内部实现／内部测试或 tools 原型。Serena 符号查询因语言服务未初始化失败，按仓库允许的回退规则使用限定文件检查；没有扩大阅读范围。目标仓库本轮不在沙箱可写范围，通过任务授权内的提权执行修改及 Compose 验证。

除本次用户已确认的接口删减外，没有新增契约缺口。材质能力暂不支持；以后若有具体使用需求，再讨论表示和读取范围，不保留占位类或字段。
