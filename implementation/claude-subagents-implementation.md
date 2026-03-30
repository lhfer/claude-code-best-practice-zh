# Subagents Implementation

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/implementation/claude-subagents-implementation.md>

## 这篇看什么

这篇不是讲 subagent 的抽象概念，而是看这个仓库到底怎么把它落到文件里。

## 代表性样例

这个仓库用 `weather-agent` 做示范。

它的作用不是“展示一个复杂业务”，而是展示 subagent 最标准的一种职责：

- 不跟用户来回聊太多
- 自己根据预加载 skill 去完成一件自治任务
- 把结果交回主流程

## 这个样例为什么好

因为它边界非常清楚：

- 用户交互在 command
- 取数逻辑在 agent
- 生成结果文件在 skill

这让你能非常清晰地看见 subagent 在整个系统里的位置。

## 你真正该抄的不是天气本身

别抄：

- 迪拜
- 温度
- SVG 卡片

该抄的是：

- subagent 只负责一段自治职责
- skill 通过 `skills:` 预加载
- command 不直接越权替代 agent 干活

## 一句话

这个实现样例的价值，不在 weather，而在“职责切分的干净程度”。
