# Cube complex 插图

归档日期：2026-09-15。当前展示版为 v2，已使用数学排版修正上下标。

## 用途与来源

用于说明完整路径如何拆成 roadmap 边、边对形成基本协调方片、公共边上的点如何对应，以及如何连续跨片。

关联笔记：[Cube complex：原始理解与讨论后的完善表述](../../inbox/2026-09-15-cube-complex-understanding.md)。

依据 LaValle 的 [Cube complex / 图 7.10](https://lavalle.pl/planning/node327.html) 与 [Planning on the cube complex](https://lavalle.pl/planning/node328.html)，由用户与 agent 讨论构图，agent 使用程序化绘图生成。不是原书图片的复制：本例使用三条在中间配置 J 相交的完整路径，以展示三张卡片在中央连接的效果。

## 文件与维护入口

| 图 | SVG | 内容 |
| --- | --- | --- |
| 1 | [路径网络](01-path-network.svg) | A 的三条完整路径与 B 的路径 f |
| 2 | [三个协调卡片](02-three-coordination-cards.svg) | 三组 path-pair，每张卡片分为两个基本方片 |
| 3 | [公共边与对应点](03-corresponding-boundaries.svg) | 三个点表示同一联合配置 |
| 4 | [中央拼接](04-glued-cards.svg) | 三张卡片沿中央公共边交汇 |
| 5 | [跨片路线](05-cross-card-route.svg) | 从 Q1 经过公共边进入 Q2 |

[draw_figures.py](draw_figures.py) 是维护源文件。修改布局或文字后重新生成 SVG；数学标签已经渲染为矢量轮廓，阅读端不需要 LaTeX 或原字体。直接编辑 SVG 的修改不会自动回到脚本。

## 生成方法

需要 Python 3、NumPy、Matplotlib、Pillow，以及可显示中文的字体。脚本自动查找常见中文字体；若未找到，可通过环境变量 CUBE_COMPLEX_FONT 指定本机字体文件。源文件没有绑定本次会话的输出路径。

以下命令从 research-process 根目录执行，不安装依赖。第一条更新 SVG；第二条还生成 exports/ 中的 PNG 和总览：

```bash
python3 assets/cube-complex/draw_figures.py
python3 assets/cube-complex/draw_figures.py --export-raster
```

可通过 --output-dir 指定其他生成目录。不同字体或库版本可能造成排版差异，重新生成后应检查文字、公共边、箭头与图注。

## 记号与限制

- p1、p2、p3 是经过 J 的完整配置路径，分别由 e_k^-、e_k^+ 两条边组成；每张卡片对应 p_k × f，包含两个基本方片。
- α 是整条路径的展示参数，约定 J 位于 α=0.5；基本方片的局部进度在 J 处分别为 1 或 0。参数不是物理时间。
- 线条示意配置路径，不是末端实际轨迹。片面夹角只是展示方式，没有物理角度含义；投影中的其他交叠不是额外连接。
- 图 5 的紫色路线用于说明连续跨片，未通过真实机械臂几何验证；图中“假定已通过碰撞检查”是教学假设，不是实验结果。
- 本组未绘制碰撞区域，不据此证明某个真实运动规划问题可解。
