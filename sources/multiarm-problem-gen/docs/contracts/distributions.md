# 分布参数公开契约

本轮探索性实现依据 [D4-1](../notes/discussions/2026-09-30-autonomous-units-4-6-decisions.md#d4-1独立多维分布表示)，不表示用户已最终接受设计。

```python
from multiarm_problem_gen.distributions import (
    UniformDistribution,
    GaussianDistribution,
)

UniformDistribution(*, lower: tuple, upper: tuple)
GaussianDistribution(*, mean: tuple, stddev: tuple)
```

两个类型只表示分量独立的联合分布参数。没有采样 API、场景引用、文件或其他 I/O，也不计算概率、协方差或统计性质。

## 参数与维度

- 每对输入必须是等长 tuple；不接受 list、字符串或其他容器。
- 元素接受 int／float，拒绝 bool 和其他类型。数值必须能转换为有限 float；NaN、正负 Inf 及转换溢出的大整数非法。
- 保存为同名的 float tuple，保留输入顺序，不排序、合并或解释分量含义，不修改输入。
- `UniformDistribution` 每维要求 `lower <= upper`；相等表示确定值。
- `GaussianDistribution` 每维要求 `stddev >= 0`；零标准差表示确定值。
- 空 tuple 合法，表示零维。`dimension: int` 是向量长度导出的只读属性；一维无需特殊类型，没有显式 dimension 构造参数。
- 对象及参数只读，不能赋值、删除字段或原地修改参数。相等、哈希及序列化行为不在本契约保证范围内。

## 错误与示例

非法容器或元素类型抛出 `TypeError`；长度、数值范围或有限性不合法抛出 `ValueError`。错误消息指出相关字段；具体完整消息不保证稳定。

```python
uniform = UniformDistribution(lower=(2, -3.5, 7), upper=(4, -1, 7))
assert uniform.lower == (2.0, -3.5, 7.0)
assert uniform.upper == (4.0, -1.0, 7.0)
assert uniform.dimension == 3

gaussian = GaussianDistribution(mean=(5, -2), stddev=(0, 0.5))
assert gaussian.mean == (5.0, -2.0)
assert gaussian.stddev == (0.0, 0.5)
assert GaussianDistribution(mean=(), stddev=()).dimension == 0
```

通过参数验证只说明表示合法，不证明后续采样实现、统计性质、机器人状态可行性或场景有效性。
