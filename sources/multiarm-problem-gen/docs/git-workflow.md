# Git 工作方式与提交信息

## 探索分支与长期主线

`main` 保存当前已经接受、愿意继续以之为基础的项目状态，不要求项目已经成熟或功能完整。

尝试某项修改时，从当时的 `main` 建立围绕具体问题的分支。在分支中讨论、实现、验证并按需保存过程提交；形成值得保留的成果后，整理并集成到 `main`。

后续新的尝试从更新后的 `main` 建立新分支，不默认沿用上一轮探索分支。

```text
main 的状态 A
  └─ 新建尝试一分支
       ├─ 尝试
       ├─ 调整
       └─ 验证、整理 → 集成到 main

main 继续演进到状态 B
  └─ 新建尝试二分支
       ├─ 尝试
       └─ 验证、整理 → 集成到 main
```

分支围绕问题组织，不必对应一次对话。尝试可以跨多个 session，也可以在发现不合适后放弃。值得保留的认识记录到讨论笔记中，不要求所有试验代码进入主线。

## 何时提交与集成

探索阶段可以按需创建检查点，避免大量工作只存在于未提交状态中。

当已有改动构成一次清楚、可审阅的提交时，agent 可以主动建议提交并说明范围。建议不等于提交授权。

进入主线时，整理的不只是提交信息，还包括：

- 排除不准备保留的试验内容；
- 分离无关的逻辑变化；
- 明确最终行为、验证情况和重要限制；
- 保留有价值的设计理由或讨论链接。

以是否形成可理解、可验证的成果判断集成时机，不以文件数量或改动行数判断。一轮探索可以整理成一个或多个主线提交。

## 集成方式

暂不统一规定使用 merge、squash 还是整理后的提交，根据具体情况选择。

- 需要保留原始探索提交关系时，可以使用 merge。
- 希望主线只保留整理后的成果时，可以使用 squash，或先整理提交再集成。
- 不将多个不相关成果强行压成一个巨大提交。
- 使用 squash 后，下一轮尝试从更新后的 main 开始。
- 若需要长期保留原始探索代码，应明确保留相应分支或 tag，不依赖 reflog 作为永久档案。

集成后检查组合后的行为，没有文本冲突不等于没有语义冲突。

## Commit message 的语言

所有提交信息均使用英文，包括探索提交和主线提交的标题、正文及说明性 footer。

文件路径、代码标识符和链接保持原样。

## 探索提交

以清楚记录尝试和恢复工作为目的，不强制固定模板、分类前缀或严格标题长度。

示例：

```text
Try placing both arms along the same table edge
```

```text
Save the mesh preview prototype before adding labels
```

```text
Adjust target offsets; cross-arm reachability still unchecked
```

避免只有 `Update`、`Fix` 或 `WIP` 等无法区分内容的信息。未完成状态可以直接说明，不包装成已经完成的成果。

## 主线提交

以 Pro Git 的 Commit Guidelines 为基础，面向不了解本次对话的未来读者。

格式：

```text
Short summary of the change

Explain why the change is needed and describe the resulting behavior.
Include important limitations or references when useful.
```

约定：

- 标题使用祈使式，例如 `Add`、`Fix`、`Clarify`、`Remove`。
- 标题简短明确，尽量控制在约 50 个字符，不以机械截断牺牲清晰度；末尾不加句号。
- 标题与正文之间空一行；正文尽量在约 72 列换行。
- 简单变化可以只有标题。
- 正文解释动机、结果及必要取舍，不重复罗列全部 diff。
- 不直接拼接探索阶段的零碎提交信息作为主线说明。
- 暂不强制采用 Conventional Commits 的 `feat:`、`fix:` 等前缀。

示例：

```text
Add frames for non-robot scene objects

The preview showed target frames and TCPs but did not expose object
origins. Draw one XYZ frame from each scene object's pose and add a
separate visibility toggle.

These frames represent object origins, not mesh centers or local
collision-shape frames.
```

提交信息描述这次实际保存的内容，不把未实现计划或未执行验证写成事实。

## 操作边界

提交前检查差异和暂存范围，仅包含本次授权的内容。保护已有的用户修改，不混入无关工作。

提交、集成和推送分别按授权范围执行；不会因为允许在分支探索，就自动获得推送或改写共享历史的授权。

需要整理别人已经依赖的提交时，先协调，不擅自改写。

## 参考

- [Pro Git：Commit Guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
- [Pro Git：Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
- [GitHub：Pull request merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges)
- [Conventional Commits：允许在 squash 时整理提交信息](https://www.conventionalcommits.org/en/v1.0.0/#do-all-my-contributors-need-to-use-the-conventional-commits-specification)
