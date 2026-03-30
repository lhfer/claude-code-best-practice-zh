# Skills Implementation

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/implementation/claude-skills-implementation.md>

## 这篇看什么

看这个仓库是怎么把“skill”做成两种不同角色的：

- 预加载给 agent 的 skill
- 在主流程里直接调用的 skill

## 两个代表

### `weather-fetcher`

这类 skill 更像“预装知识”：

- 告诉 agent 去哪里取数
- 告诉 agent 从响应里拿什么
- 不负责写文件

### `weather-svg-creator`

这类 skill 更像“动作单元”：

- 吃调用上下文里的输入
- 使用 supporting files
- 输出具体产物

## 这个仓库最值得抄的一点

`weather-svg-creator` 不把所有模板塞进 `SKILL.md`，而是拆到：

- `reference.md`
- `examples.md`

这非常适合中文团队，因为很多人第一次写 skill 最容易犯的错，就是把主文件写成一大坨说明书。

## 一句话

skill 的实现价值，不在“写多详细”，而在“主文件负责判断，参考文件负责细节”。
