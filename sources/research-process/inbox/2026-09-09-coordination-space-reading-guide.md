# 协调空间在多机械臂运动规划中的应用：阅读导览

日期：2026-09-09

状态：agent 调研整理，经用户确认写入，供后续逐步阅读。不是用户已完成阅读的清单，也不是已确定的实验或算法方案。

## 讨论背景

当前关注多机械臂之间随配置与运动进度变化的空间占用相互制约。讨论碰撞矩阵后，希望通过经典协调空间文献理解这种关系，寻找后续研究的启发。本篇只记录协调空间部分，问题实例生成与筛选的调研另待讨论。

## 1. 协调空间究竟固定了什么

设第 i 条机械臂的几何路径已给定为 q_i=p_i(s_i)，s_i∈[0,1]。此时每条臂原本高维的关节配置，可沿这条路径用一个进度变量描述。所有臂的进度组成 s=(s_1,…,s_n)，协调空间便是这些路径参数的乘积。发生机器人间碰撞的进度组合构成障碍区域，协调过程要寻找从起始进度到完成进度的无碰撞路线。LaValle 的教材 §7.2.2 给出了该构造，并指出时间在其中可以隐式表达。[1]

路径给定是这种降维的关键限制。两个七自由度机械臂可以得到二维协调空间，不意味着任意十四维运动规划都被无损压缩到二维；被省去的自由度由所选路径固定了。

协调路线不必只有一种。某些路线对应 A 先通过，另一些对应 B 先通过；在允许等待但禁止沿路径倒退的模型中，还应要求每个进度分量非递减。教材的一般定义允许非单调路线，因此“协调空间天然不允许倒退”是不准确的。几何上有路线，也不自动说明在额外速度、加速度、期限等要求下有可执行轨迹。[1]

对于固定机器人几何和通常的两两碰撞约束，碰撞区域可以用机器人对之间的关系描述。但每对分别找到的协调方案未必互相兼容。两两碰撞检测的可分解性，不能等同于多臂协调问题可以独立求解。

## 2. 经典与直接相关的阅读材料

### 2.1 LaValle：Planning Algorithms，§7.2.2，2006

这是最适合作为入口的材料。先读 Fixed-path coordination，再读相邻的 Fixed-roadmap coordination。前者固定每臂一条路径；后者允许在给定路线图中选择路线。阅读时重点理解图 7.9、进度变量与机器人配置的映射，以及由两两碰撞形成的柱状障碍。[1]

agent 的启发（未确认为方案）：可以把“不同阶段的空间占用相互影响”转化为兼容／不兼容的进度组合；它比给整个共享区域指定一个统一互斥锁更细致。但是否需要这种细致程度，应由实际问题决定。

### 2.2 O’Donnell 与 Lozano-Pérez：Deadlock-Free and Collision-Free Coordination of Two Robot Manipulators，ICRA 1989

经典双臂工作，针对路径可预先规划、但执行时长可能变化的情形，通过在路径中加入协调指令实现异步执行，并同时关注碰撞和互相等待形成的死锁。[2]

agent 的启发（未确认为方案）：协调可以约束“谁必须先经过某个位置”，不一定只能提前规定精确到秒的完整轨迹。它与当前关于分段运动、等待和放行的讨论十分接近。

阅读范围说明：原始扫描 PDF 的全文解析和截图访问受限，本次核实了原始论文被索引的正文段落和书目信息；未独立复核其全部算法细节与证明。

### 2.3 LaValle 与 Hutchinson：Optimal Motion Planning for Multiple Robots Having Independent Goals，IEEE TRA 1998

这项工作将每个机器人的独立目标／代价与 Pareto 最优协调联系起来，并讨论从分离规划到集中规划之间的路线图协调。作者主页提供正式期刊版和 PDF；1996 年另有同名会议版，不应混淆年份。[3]

agent 的启发（未确认为方案）：整体 makespan 相同，不代表各臂等待的分配相同。若后续实验发现某些机械臂承受了大部分等待，可以借此理解整体与个体代价的区别，而不必立刻增加新的优化目标。

阅读范围说明：本次核实作者提供的书目信息和研究概述；期刊 PDF 的文本抽取较差，没有据此报告具体实现性能。

### 2.4 Ghrist、O’Kane 与 LaValle：Computing Pareto Optimal Coordinations on Roadmaps，IJRR 2005

研究各机器人拥有独立路线图时的协调。§1.2 给出路线图乘积减去碰撞集合的定义；§2.1 的例子展示同一相交场景中不同的 Pareto 最优协调类别。其理论和算法有明确几何及运动假设，不能直接当作任意机械臂系统的通用保证。[4]

agent 的启发（未确认为方案）：碰撞区域的组织方式、可通过的协调路线类别，比碰撞格子的数量更有信息。建议先读 §1–2 的定义和例子，曲率相关证明可暂缓。

### 2.5 Akella 与 Peng：Time-Scaled Coordination of Multiple Manipulators，ICRA 2004

给定机械臂路径／轨迹，调整启动时间和速度曲线的整体时间缩放，并考虑动力学约束。论文使用混合整数规划和充分的碰撞规避条件，因此并非任意自由调速下的通用最优协调算法。[5]

agent 的启发（未确认为方案）：同一套碰撞几何在不同的允许动作下，会得到不同的可行性与代价。只延迟启动、允许中途暂停、允许调速，是不同协调问题。

### 2.6 Zhang 与 Pecora：Online and Scalable Motion Coordination for Multiple Robot Manipulators in Shared Workspaces，2023 在线发表／2024 卷期

直接相关材料。§IV 中将初始轨迹采样，公式 (19)–(20) 形成两机器人配置样本的碰撞矩阵；再分析给定路径上的协调情况并进行轨迹重规划。§V 推广到多臂。[6]

agent 的启发（未确认为方案）：矩阵可以用来观察阻挡与放行关系。须区分样本索引、路径进度和物理时间；数值采样及几何近似的可靠性也要单独检查。

### 2.7 Stop-N-Go 与 StAC：与当前 baseline 衔接

Stop-N-Go 的协调阶段给已有轨迹插入暂停；论文的返回初始配置假设参与可行退路的论证。其“给定轨迹下的优化”不能直接等同于整个运动规划问题的优化。[7]

StAC 在一组路径上多次尝试调度，并将碰撞信息反馈给路径生成。其 2026 年修订版 §III–IV 适合阅读调度与路径选择之间的关系。[8]

agent 的分析：两者可以放在协调空间视角下理解，但不应在未核对源码前宣称它们都显式建立了完整碰撞矩阵。一个方法利用进度关系，不意味着其存储结构就是二维表或高维网格。

## 3. 建议阅读顺序

第一轮按以下顺序阅读：

1. LaValle 教材的 Fixed-path coordination：先理解进度、配置映射和碰撞区域。
2. 1989 年双臂协调论文：理解执行时间变化时的等待、放行与死锁。
3. Zhang 与 Pecora：结合公式 (19)–(20)、图 6，理解碰撞矩阵的具体使用。

第二轮再看：

1. 2005 年 Pareto 协调论文的 §1–2：理解不同协调路线及完成时间权衡。
2. 2004 年时间缩放论文：理解允许的速度调整与动力学约束。
3. Stop-N-Go 与 StAC 的方法部分：比较固定轨迹上的协调和协调信息反馈给路径生成。

1998 年论文可作为独立目标与路线图协调的扩展阅读。复杂证明不必第一轮全部展开。

## 4. 保留的理解与问题

- 固定路径协调的降维以路径已经选定为前提，不等于保留了原始联合配置空间中的全部运动选择。
- 时间可以隐式表达；是否允许沿路径倒退、是否限制速度与加速度，需要另外明确。
- 两两碰撞关系可以分开检查，但协调方案需要全局一致。
- “各臂处于不同阶段”可以用连续相对进度理解，不要求算法先划分离散阶段。
- 不同协调路线可能对应不同先后安排；这些区别是否有助于解释现有方法的不足，仍需结合实际实例研究。
- 何时只调整进度已经足够，何时应改变路径，仍是待讨论的问题。

以上不构成已确认的新需求、评价指标或改进方案。

## 5. 文献入口

1. Steven M. LaValle. Planning Algorithms, 2006, §7.2.2. https://msl.cs.uiuc.edu/~lavalle/planning/node325.html
2. Patrick A. O’Donnell and Tomás Lozano-Pérez. Deadlock-Free and Collision-Free Coordination of Two Robot Manipulators. ICRA 1989, pp. 484–489. https://people.csail.mit.edu/tlp/publications/coordination-o-donnell.pdf
3. Steven M. LaValle and Seth A. Hutchinson. Optimal Motion Planning for Multiple Robots Having Independent Goals. IEEE Transactions on Robotics and Automation 14(6), 1998, pp. 912–925. https://lavalle.pl/papers/LavHut98b.pdf ; 作者书目：https://lavalle.pl/mulrob.html
4. Robert Ghrist, Jason M. O’Kane, and Steven M. LaValle. Computing Pareto Optimal Coordinations on Roadmaps. IJRR 24(11), 2005, pp. 997–1010. https://jokane.net/pubs/GhrOKaLav05.pdf
5. Srinivas Akella and Jufeng Peng. Time-Scaled Coordination of Multiple Manipulators. ICRA 2004. https://webpages.charlotte.edu/sakella/papers/icra04a.pdf
6. Shiyu Zhang and Federico Pecora. Online and Scalable Motion Coordination for Multiple Robot Manipulators in Shared Workspaces. TASE 21(3), 2024, pp. 2657–2676; online 2023. https://doi.org/10.1109/TASE.2023.3266889 ; 作者上传正文：https://www.researchgate.net/publication/370114687_Online_and_Scalable_Motion_Coordination_for_Multiple_Robot_Manipulators_in_Shared_Workspaces
7. Gidon Han, Jeongwoo Park, and Changjoo Nam. Stop-N-Go: Search-based Conflict Resolution for Motion Planning of Multiple Robotic Manipulators. 2024 preprint. https://arxiv.org/abs/2410.07606
8. Weihang Guo, Zachary Kingston, Kaiyu Hang, and Lydia E. Kavraki. Efficient Multi-Robot Motion Planning for Manifold-Constrained Manipulators by Randomized Scheduling and Informed Path Generation. 2026 revision. https://arxiv.org/abs/2412.00366

## 相关记录

- [联合空间中的相对进度与多臂协调的基础](2026-09-08-multi-arm-progress-and-coordination.md)
- [多机械臂空间占用与时序协调：当前关注点](2026-09-09-multi-arm-research-focus.md)
- [时序协调的直觉与实验验证的目的](2026-09-09-coordination-intuition-and-experimental-evidence.md)
