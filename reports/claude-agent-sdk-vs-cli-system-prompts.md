# Claude Agent SDK vs Claude CLI：系统提示与输出一致性

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-agent-sdk-vs-cli-system-prompts.md>

## 先讲结论

同一句请求，经过：

- Claude Agent SDK
- Claude CLI（Claude Code）

**并不保证输出一样。**

原因不是“模型突然变了”，而是两边带给模型的系统提示、上下文和默认行为本来就不同。

## 为什么会不同

### Claude CLI / Claude Code

它默认带着更多“工程使用语境”：

- 工具说明
- 编码准则
- 安全规则
- 项目上下文
- CLAUDE.md / settings / hooks 等附加信息

### Agent SDK

默认更轻，更像一层可编程接口。

这意味着：

- CLI 更像“带很多默认行为的现成工作台”
- SDK 更像“你自己搭系统的底座”

## 这对中文用户意味着什么

如果你在 CLI 里试出来一个效果，再去 SDK 里复现，别假设它会天然一致。

你至少要考虑：

- 系统提示有没有对齐
- 工具有没有对齐
- 项目上下文有没有对齐
- 是否还有额外 preset

## 最重要的误区

### 误区：同模型 + 同用户输入 = 同输出

不是。

只要系统提示结构、工具上下文和采样条件不同，输出就可能明显不同。

## 什么时候该用 CLI

- 你想快速在真实工程环境里工作
- 你想直接利用现成交互和项目上下文

## 什么时候该用 SDK

- 你要自己编排 agent 系统
- 你要可编程控制流程
- 你要把 Claude 接进自己的应用或服务

## 一句话总结

CLI 和 SDK 不只是“同一模型的两个入口”，它们本身就是两种不同的产品形态。
