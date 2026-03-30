# Commands Implementation

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/implementation/claude-commands-implementation.md>

## 这篇看什么

看 command 在这个仓里到底承担什么角色。

## 代表性样例

`/weather-orchestrator`

它不是“万能命令”，而是一个非常标准的工作流入口：

1. 问用户一个必要问题
2. 调 agent 去取数
3. 调 skill 去生成结果
4. 汇总输出

## 为什么这个样例值得学

因为它让 command 做 command 该做的事：

- 组织流程
- 调度能力
- 兜住输出

而没有让 command 既像 agent 又像 skill，最后什么都沾一点。

## 一句话

如果你想知道“高质量 command 看起来应该像什么”，这个样例是很好的起点。
