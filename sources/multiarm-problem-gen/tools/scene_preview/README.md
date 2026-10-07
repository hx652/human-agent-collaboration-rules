# 简单场景预览原型

所有预览代码和前端依赖集中在本目录；不依赖生成器、ROS 运行节点或碰撞库，不修改场景资源。

## 启动

当前环境已有 numpy、scipy、PyYAML，从仓库根目录运行：

```bash
python3 tools/scene_preview/preview.py
```

浏览器打开 http://127.0.0.1:8765 ，Ctrl+C 停止服务。端口冲突时加 `--port 8766`。必须通过本地服务打开，不能直接双击 index.html；前端依赖随目录提供，运行时不访问 CDN。

其他环境可先在独立虚拟环境中安装 `requirements.txt`。只生成预览数据可使用 `--build-only`。修改场景后重新运行以刷新数据，然后刷新页面。

## 显示内容

- 读取 `examples/ur7e_table/inputs/tabletop/scene.yaml` 和引用的机器人配置、URDF，不依赖基准检查文件。
- 显示实际碰撞 STL mesh，而不是外观 DAE 或简化杆件。蓝色为 arm_a，橙色为 arm_b，深色为夹爪组件。
- 保留夹爪固定值、mimic 关系、URDF 中的局部几何位姿与 mesh 缩放。
- 显示基本几何体、球形 mesh 障碍、目标坐标轴和 TCP。
- 每个 `scene.objects` 实例显示一组 XYZ 坐标轴及物体名标签（不包含机械臂），默认开启，可独立切换；标签也受标签开关控制。坐标轴直接使用 YAML 对象 pose，不使用几何中心或 collision shape 的局部 pose；桌子的 frame 在世界原点。物体坐标轴穿透几何显示，便于看到位于物体内部的原点。
- 可单独切换每条臂的 home、up；显式传入 --validation 且报告输入哈希仍匹配时，也提供 IK 端点见证。
- 左键旋转、滚轮缩放、右键平移；提供俯视、初始视角和两臂复位按钮。

IK 见证只验证过另一臂处于 home 的特定端点。任意两种姿态的组合可能发生碰撞。预览不做碰撞检查、不规划轨迹，也不在姿态之间插值。哈希匹配只针对 validation.json 列出的输入，不替代完整资源验证。

## 文件

- `preview.py`：加载输入、解析 STL、计算正运动学、导出 scene.json 并启动只监听本机的静态服务。
- `index.html`、`viewer.js`：浏览器交互与 Three.js 渲染。
- `vendor/`：Three.js 0.160.1、同版 OrbitControls 及 MIT 许可证。
- `scene.json`：可再生成的缓存，已在本目录 .gitignore 排除。

前端依赖原始地址：

- https://unpkg.com/three@0.160.1/build/three.module.js
- https://unpkg.com/three@0.160.1/examples/jsm/controls/OrbitControls.js
- https://unpkg.com/three@0.160.1/LICENSE

## 已验证与限制

已在本机场景上验证加载两臂、11 个环境几何体、4 个目标 frame 和 18 个共享 STL；浏览器验证了实际渲染、姿态切换、俯视及标签开关。核对 IK 姿态的 TCP 与目标世界位置符合已有检查结果。

这是针对当前基准样例的小型原型，尚不覆盖任意输入 schema：环境对象和机器人基座以 world 为参考，机器人碰撞几何使用 STL；没有动画、拾取编辑或文件热更新。未执行完整的跨浏览器测试。

## 可选开发材料

默认使用机器人配置中的第一个命名姿态作为显示选择，不定义生成初始状态。可用 `--baseline tools/baseline_validation/ur7e_table/baseline.yaml` 显式指定显示姿态，用 `--validation tools/baseline_validation/ur7e_table/validation.json` 加载新检查报告。历史报告不会自动读取。

`--scene` 可指向仓库外搬移后的场景；未提供 baseline 或报告也能显示场景和命名姿态。此入口是预览原型，不代表已实现 generation 读取或采样。
