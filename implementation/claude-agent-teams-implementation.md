# Agent Teams Implementation

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/implementation/claude-agent-teams-implementation.md>

## 这篇看什么

这篇不是在讲“多 agent 听起来多酷”，而是在讲：

> 当多个 Claude 会话像小团队一样协作时，仓库里应该长成什么样。

## 它和 subagent 的区别

最关键的一点：

- subagent 是单会话里的隔离上下文
- agent teams 是多个独立 Claude 会话协作

也就是说，agent teams 的粒度更大，协作感更强，维护成本也更高。

## 这个仓库里的样例

这里用的是一个 `time orchestration workflow`：

- command 负责编排
- agent 负责取时间
- skill 负责渲染 SVG

但更值得看的不是“时间卡片”本身，而是它怎么拆角色：

- Command Architect
- Agent Engineer
- Skill Designer

再通过共享任务清单去对齐数据契约。

## 这套实现最值得抄的地方

### 1. 角色拆分清楚

不是泛泛地说“你们几个并行干”，而是明确每个角色负责哪个文件、哪个接口。

### 2. 数据契约先对齐

这一点非常重要。
多 agent 协作最怕不是代码不会写，而是接口说不清楚。

### 3. 工作目录隔离

`agent-teams/.claude/` 的自包含设计很值得学，因为它不会污染仓库根部运行层。

## 一句话总结

agent teams 的实现价值不在于“并行”两个字，而在于：

> 角色、文件归属、数据契约和协作边界是否一开始就写清楚。
