# Agents vs Commands vs Skills

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-agent-command-skill.md>

## TL;DR

最简单的判断：

- `agent`：丢出去独立干活
- `command`：给用户一个明确入口
- `skill`：让 Claude 带着一套知识或动作随时可用

## 一张表说清楚

| 机制 | 最像什么 | 什么时候优先选它 |
|---|---|---|
| Agent | 独立上下文里的子线程 | 复杂、多步、需要隔离或自治 |
| Command | 用户显式触发的工作流入口 | 想把高频流程收成 `/xxx` |
| Skill | 可复用知识或动作单元 | 想让 Claude 自动想起一套能力 |

## 为什么这篇报告重要

因为很多中文用户第一次接触 Claude Code 时，最容易混的就是这三样。

常见症状：

- 明明应该做成 skill，却做成 command
- 明明只是一个入口，却做成大而全 agent
- 明明是项目规范，却做成一次性 prompt

## 这个仓库给出的一个高质量答案

它不是靠“定义”来区分三者，而是靠 weather 样例来区分：

- `weather-orchestrator` 是 command
- `weather-agent` 是 agent
- `weather-fetcher` / `weather-svg-creator` 是 skill

这比抽象讨论好得多，因为你能看到：

- 谁负责用户交互
- 谁负责自治执行
- 谁负责提供可复用知识或动作

## 作为中文读者，你最该记住的判断线

### 如果重点是“入口”

选 command。

### 如果重点是“自治”

选 agent。

### 如果重点是“复用”

选 skill。

## 一个现实提醒

官方现在越来越把 custom command 和 skill 放进一套更统一的能力模型里看。
所以这篇报告里保留三分法，是为了帮你理解，不是为了让你死守概念边界。

## 别做的事

- 不要为了显得高级，把所有流程都 agent 化
- 不要为了省事，把所有知识都塞进根 `CLAUDE.md`
- 不要把 command 当成唯一工作流工具

## 最后的判断口诀

> 入口选 command，自治选 agent，复用选 skill。
> 如果三者都像，那就回到“这件事最主要的矛盾是什么”。
