# pairwise-hdr-output-gamut

## 领域

游戏、图形与多媒体

## 主题

HDR 输出与色域

## 说明

浮点交换链、显示器色域与亮度元数据。

初始状态下 `render/hdr_output_gamut.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
