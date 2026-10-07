# Planning Algorithms §7.2：Multiple Robots

作者：Steven M. LaValle  
书籍：Planning Algorithms（2006）  
创建日期：2026-09-15  

## 原文入口（HTML）

- [书籍主页](https://lavalle.pl/planning/web.html)
- [§7.2 Multiple Robots](https://lavalle.pl/planning/node318.html)

## 一些笔记

为方便阅读，我将 §7.2 的内容整理为四组。以下是笔记的分组，不是原书新增的小节编号：

- **§7.2–7.2.1：问题定义与联合配置空间**——包括 [§7.2 的引言](https://lavalle.pl/planning/node318.html)和 [§7.2.1 Problem Formulation](https://lavalle.pl/planning/node319.html)，作为后续讨论的铺垫。
- **§7.2.2：优先级规划**——对应 [Prioritized planning](https://lavalle.pl/planning/node324.html)。
- **§7.2.2：固定路径协调**——对应 [Fixed-path coordination](https://lavalle.pl/planning/node325.html)。
- **§7.2.2：固定路线图协调与 Cube complex**——合并阅读 [Fixed-roadmap coordination](https://lavalle.pl/planning/node326.html)、[Cube complex](https://lavalle.pl/planning/node327.html) 和 [Planning on the cube complex](https://lavalle.pl/planning/node328.html)。

这里的笔记只是简单记录，整个§7.2的原文不长，需要时再回看即可

### §7.2–7.2.1：问题定义与联合配置空间

建立了这一节用到的记号规范和含义

§7.2.1中介绍了coupled configuration space，比较有趣的内容是这个空间中的障碍可以分两类:
- 由环境障碍而导致的
- 由机械臂间碰撞导致的
其中第二类具有cylindrical structure，即当联合状态中一对机器人碰撞时，其他机器人是否碰撞已经无关紧要了，所以会形成柱状结构，我认为这个现象产生于碰撞是两两之间的关系，同时只要一对碰撞，整个状态就会被标记为障碍状态

### §7.2.2：优先级规划（Prioritized planning）

没什么可说的

### §7.2.2：固定路径协调（Fixed-path coordination）

和我的研究方向紧密关联的部分，完整的描述了coordination space的概念

值得注意的是coordination space中的障碍也具有cylindrical structure

注意，整个协调空间的形状(障碍分布)是由每个机械臂的轨迹间的碰撞情况决定的

#### 交互示例：路径碰撞与协调空间障碍

[打开 HTML 页面（用浏览器查看）](../assets/path-collision-equivalence/index.html)

- **两机器人标签页**：A₁ 的两条镜像路径几何位置不同，但在统一进度参数下，与 A₂ 路径的两两碰撞关系逐点相同，因此产生相同的协调空间障碍分布。
- **三机器人标签页**：展示三条路径、两两碰撞区域及采样矩阵，并将连续碰撞区域沿剩余进度轴展开为柱体；三组柱体的并集构成完整三维协调空间中的障碍区域。可点击矩阵格查看对应关系，拖动立方体旋转视角。

这是 agent 构造的圆盘机器人教学示例，不是真实机械臂实验。连续障碍依据明确的路径插值与距离条件计算，不从稀疏采样矩阵直接推断。维护文件与具体限制见[资源说明](../assets/path-collision-equivalence/README.md)。

### §7.2.2：固定路线图协调与 Cube complex

最复杂的一部分，将coordination space推广到roadmap上

关于cube complex的部分还没有完全看懂。

#### Cube complex：我的理解与讨论记录

cube complex这个词是说由cube构成的complex

与 agent 讨论后完善的理解，保留在原讨论记录中：

- [完善表述：统一记号、方片拼接与跨片搜索](../inbox/2026-09-15-cube-complex-understanding.md#与%20agent%20讨论后的完善表述)
- [补充说明：路径拆分、基本方片及其与离散采样的区别](../inbox/2026-09-15-cube-complex-understanding.md#补充讨论：路径拆分与基本方片)
- [配套插图：路径网络、对应点、拼接与跨片路线](../inbox/2026-09-15-cube-complex-understanding.md#配套插图)

## 已有相关讨论

- [联合空间中的相对进度与多臂协调的基础](../inbox/2026-09-08-multi-arm-progress-and-coordination.md)
- [协调空间阅读导览](../inbox/2026-09-09-coordination-space-reading-guide.md)
- [Cube complex：原始理解与讨论后的完善表述](../inbox/2026-09-15-cube-complex-understanding.md)
- [Cube complex 配套插图与源文件](../assets/cube-complex/README.md)
