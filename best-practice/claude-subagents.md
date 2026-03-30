# Subagents Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-subagents.md>

## 先讲人话

subagent 适合这样的任务：

- 这件事不是一句话能做完，而是要自己查、自己判断、自己跑几步。
- 你不想让中间过程把主对话上下文塞爆。
- 你希望它带着专门权限、专门记忆、专门 skill 去工作。

如果只是一个简单 prompt 模板，别急着上 subagent。
subagent 用得好是“隔离复杂度”，用不好就是“把每件小事都搞成多进程”。

## 什么时候该用

- 做多步研究
- 做带权限隔离的任务
- 把重度上下文任务拆出去
- 给某类任务一个长期稳定的人设和边界
- 让 agent 预加载特定 skill

典型例子：

- 代码审查 agent
- 文档整理 agent
- presentation 专用 agent
- 只负责取数的 weather / time agent

## 什么时候不该用

- 只是想把一句 prompt 存起来
- 只是想让用户手动触发一串固定步骤
- 这个任务更像 command 或 skill
- 任务简单到主线程直接做更快

## 你真正要理解的 5 个字段

| 字段 | 它决定什么 | 中文理解 |
|---|---|---|
| `description` | Claude 什么时候会想到调用它 | 不是功能介绍，而是触发条件 |
| `tools` | 它手里能用哪些工具 | agent 的能力边界 |
| `permissionMode` | 它遇到操作时有多大自主权 | 安全边界 |
| `skills` | 它启动时脑子里预装了什么 | 预加载知识 |
| `memory` | 它会把哪些经验留下来 | 长期记忆边界 |

## 常见误区

### 误区 1：subagent 越多越高级

不是。
好仓库的特征不是 agent 多，而是 agent 的边界清楚。

### 误区 2：description 写成“这是一个很厉害的 agent”

没用。
真正有效的写法应该告诉 Claude：

- 什么时候该调用
- 什么时候不该调用
- 这类任务它比主线程更合适在哪里

### 误区 3：什么都塞进一个 general agent

这样最容易把 agent 做成“第二个主线程”，结果上下文更乱、权限更大、行为更飘。

## 这个仓库里的代表性做法

### Weather Agent

这个仓库用 `weather-agent` 做了一个很经典的教学样例：

- command 负责与用户交互
- agent 负责自治取数
- skill 提供可复用知识

看这里：

- [implementation/claude-subagents-implementation.md](../implementation/claude-subagents-implementation.md)
- [orchestration-workflow/orchestration-workflow.md](../orchestration-workflow/orchestration-workflow.md)

### Presentation Curator

这个仓库还有一个很有代表性的设计：

- 对 `presentation/**` 目录的改动，不让主线程直接写
- 而是通过 rule 强制交给专门 agent

这比在 `CLAUDE.md` 里喊“请小心修改 presentation”要可靠得多。

## 面向中文用户的实战建议

如果你打算在自己项目里抄一套 subagent 体系，第一版建议只建 2 到 4 个：

1. `research-agent`
2. `review-agent`
3. `docs-agent`
4. 一个与你业务强相关的专用 agent

先把边界做清楚，再考虑扩张数量。

## 一句话判断

如果任务的核心矛盾是“复杂、多步、需要隔离”，优先想 subagent。
如果核心矛盾只是“重复执行”，优先想 command 或 skill。
