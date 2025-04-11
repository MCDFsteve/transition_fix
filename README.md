# Ren'Py 立绘转场修复补丁

这是一个用于修复 Ren'Py 游戏中角色立绘切换时转场效果会影响到对话框显示的问题的补丁。

## 功能说明

- 将对话框和立绘分别放在不同的层中
- 确保转场效果只应用于立绘层
- 不影响对话框的正常显示
- 保持原有的转场效果

## 使用方法

1. 将 `transition_fix.rpy` 文件放入你的 Ren'Py 游戏项目中
2. 文件会自动初始化并生效
3. 无需额外配置，立绘切换时的转场效果将只影响立绘层

## 技术细节

- 通过重写 `with_statement` 函数来控制转场效果
- 使用 `config.say_layer = "screens"` 确保对话框不受转场影响
- 转场效果被限制在 `master` 层中

## 作者

- 作者：irigaS
- 版本：1.0

## 注意事项

- 本补丁适用于 Ren'Py 游戏引擎
- 确保你的游戏项目中没有其他代码会影响到转场效果
- 如果遇到问题，请检查是否有其他代码与转场相关的设置冲突 