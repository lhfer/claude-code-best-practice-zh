# Scheduled Tasks Implementation

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/implementation/claude-scheduled-tasks-implementation.md>

## 这篇看什么

这篇展示的是：

> Claude Code 的 `/loop` 到底是怎么进入日常工作流的。

## `/loop` 的实际价值

它不是“定时器玩具”，而是：

- 定时提醒
- 周期性检查
- 轻量监控
- 自动重复某类 prompt

在个人工作流里非常实用。

## 样例里发生了什么

这里用的是：

```bash
/loop 1m "tell current time"
```

它会：

- 把 `1m` 解析成每 1 分钟
- 创建对应的 cron 任务
- 在会话里周期性触发

## 这篇最值得记住的几个事实

- 最小粒度是 1 分钟
- 任务会自动过期
- 任务是 session scoped 的
- 随时可以取消

也就是说，它很适合“短期循环任务”，不适合拿来当永久调度系统。

## 对中文用户最有价值的启发

如果你经常做这些事：

- 每隔几分钟看部署状态
- 周期性跑某个简单检查
- 定时提醒自己看一个变化结果

那 `/loop` 很可能比你想象中有用得多。

## 一句话总结

`/loop` 的最佳位置不是“云端任务系统”，而是“会话内的轻量自动化助手”。
