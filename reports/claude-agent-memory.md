# Claude Code 的 Agent Memory

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-agent-memory.md>

## 这篇报告回答什么

`memory` frontmatter 到底有什么用？

它的核心价值是：

> 让某个 agent 不再每次都从零开始。

## 它解决的问题

没有 memory 时，agent 每次调用都像第一次来这个仓库。

有了 memory 之后，它可以跨会话积累：

- 代码风格模式
- 常见问题
- review 经验
- 项目习惯

## 三种作用域

| Scope | 更适合什么 |
|---|---|
| `user` | 你个人跨项目的长期经验 |
| `project` | 这个项目团队应该共享的经验 |
| `local` | 只属于你自己的项目内经验 |

## 什么时候值得用

- code review agent
- 文档审校 agent
- 某类长期重复的质量检查 agent

## 什么时候别急着用

- 你只是做一次性任务
- agent 的边界还没稳定
- 你还没想清楚应该记住什么、不该记住什么

## 它和其他 memory 机制的区别

- `CLAUDE.md`：项目级共享工作记忆
- `rules`：路径级模块化约束
- `agent memory`：某个 agent 自己长期积累的经验

这三者不要混。

## 中文团队最有价值的用法

如果你有一个 review agent，最值得记住的是：

- 项目常见问题模式
- 反复被指出的约定
- 某些模块的历史坑

## 一句话总结

agent memory 最适合那些“会重复看同一类问题”的 agent。
如果任务不重复，memory 的收益就不会太大。
