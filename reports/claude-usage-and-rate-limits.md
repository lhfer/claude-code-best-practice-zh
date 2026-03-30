# Claude Code：使用量、速率限制与 Extra Usage

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-usage-and-rate-limits.md>

## 这篇报告解决什么问题

当你开始高频使用 Claude Code，迟早会遇到这些问题：

- 我还剩多少额度？
- 为什么突然慢了或被限了？
- 限额到了之后怎么继续干活？

## 你先记住 3 个命令

| 命令 | 用来干嘛 |
|---|---|
| `/usage` | 看当前计划额度和速率限制 |
| `/extra-usage` | 限额到了之后继续用，走按量付费溢出 |
| `/cost` | 看当前 session 的 token / 花费情况 |

## `/usage`

最适合在这些时候看：

- 你感觉 Claude 变慢了
- 你担心快触顶了
- 你要规划今天剩余工作量

## `/extra-usage`

它的意义不是“多一个按钮”，而是：

> 当订阅限额到了，不要让工作流直接中断。

但前提是你清楚：

- 这是额外计费
- 不是订阅内包含
- 应该有预算意识

## `/cost`

如果你是 API key 用户，这个命令尤其重要。

它最适合：

- 算一轮 session 到底花了多少
- 比较不同工作流的成本
- 看某个流程是不是在无意义烧 token

## 对中文用户最现实的建议

- 日常重度使用时，把 `/usage` 当健康检查命令
- 如果你在团队环境里，先想清楚谁可以开 `/extra-usage`
- 如果你在做复杂流程设计，别只看效果，也要看成本

## 一句话总结

高频使用 Claude Code 之后，配额管理不是财务问题，而是工作流问题。
