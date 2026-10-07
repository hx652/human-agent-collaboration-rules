# 六组结果提交与归档对应

补充时间：2026-10-07T20:19:36+08:00。六个实验 worktree 的原始产物现已分别提交到各自实验分支，每个结果提交的唯一父提交都是共同基准 `729f74660446badc262d300eaf75d01b6d464271`。

这些提交由主调度者在实验结束后、按用户本次要求补做，不计入子 agent 当时的执行时间或 token；原 agent 输出没有修改。

| 组 | 独立结果 commit | 产物文件数（含索引、审计） | 对应归档 |
| --- | --- | ---: | --- |
| sol_high | `afc9118d1f720c52a5013d6e2ff7f29eb5382c7b` | 58 | [sol_high/](sol_high/INDEX.md) |
| sol_xhigh | `5743b90f001fdeb6deedc85831c52b8ec13833c9` | 78 | [sol_xhigh/](sol_xhigh/INDEX.md) |
| sol_max | `d07fe17ed297adacdebe97b5e642d27e2c147f0d` | 79 | [sol_max/](sol_max/INDEX.md) |
| astra_high | `964f436af72b742fd452693023da5b396601b9e8` | 59 | [astra_high/](astra_high/INDEX.md) |
| astra_xhigh | `8bd84ee9181229e3e9a96f7186af6e5d502f14b4` | 56 | [astra_xhigh/](astra_xhigh/INDEX.md) |
| astra_max | `f9283fd4b5643d29b0d3008bd29d697bd5405cc6` | 55 | [astra_max/](astra_max/INDEX.md) |

## 隔离与核验

- 每次操作均显式指定对应 worktree，核对分支名、仓库根目录和独立暂存区；六组提交期间，主线 HEAD 与暂存区均未变化。
- 各结果 commit 的根 Git tree 与其归档子目录的 Git tree 完全相同，涵盖文件路径、Git 文件模式和全部文件内容。
- 主线只保留 `experiments/20261007-181827/<组名>/` 下的归档副本及溯源记录；没有把任何实验分支合并或 cherry-pick 到主线。
- 主线正式材料的 `INDEX.md`、`sources/`、`collection/` 不从实验 worktree 覆盖；`.serena/` 保持原样。
- 六个 worktree 已无待提交文件，继续保留供审阅。既有日志中的未提交状态是实验当时的状态，没有为这次补提交回写原日志。

完整分支、worktree 路径、树 ID、父提交和时间见 [机器可读映射](audit/result-commits.json)；原执行配置及新增结果引用见 [RUN_CONFIG.json](RUN_CONFIG.json)。
