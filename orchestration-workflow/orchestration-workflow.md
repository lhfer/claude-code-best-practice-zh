# Orchestration Workflow

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/orchestration-workflow/orchestration-workflow.md>

## 这篇为什么重要

整个上游仓库其实都在反复讲同一件事：

> Claude Code 不只是“会聊天”，而是可以被组织成工作流。

这篇就是那套工作流的最小可执行样例。

## 一张图讲清

```text
用户
  ↓
command：负责入口和编排
  ↓
agent：负责自治执行
  ↓
skill：负责复用知识或生成产物
```

## 用 weather 样例解释

- `/weather-orchestrator`
  - 问用户温度单位
  - 调 `weather-agent`
  - 再调 `weather-svg-creator`
- `weather-agent`
  - 带着 `weather-fetcher` 这套预加载知识去取数
- `weather-svg-creator`
  - 用已有上下文生成 SVG 和 markdown 输出

## 这个样例真正要教你的

不是怎么做天气卡片。

而是：

- 什么该放入口层
- 什么该放自治层
- 什么该放复用层

这三个层一旦分开，你后面再做：

- review 工作流
- spec 工作流
- 发布工作流
- 文档工作流

思路都会顺很多。

## 给中文读者的判断线

如果你在设计 Claude 工作流时脑子一团乱，可以先问自己这 3 个问题：

1. 用户是从哪里点火的
2. 哪一步应该丢给独立上下文自治完成
3. 哪部分知识或步骤值得沉淀成可复用 skill

这篇样例就是这 3 个问题的标准示范答案。
