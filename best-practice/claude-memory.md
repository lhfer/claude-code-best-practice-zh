# Memory Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-memory.md>

## 先讲人话

在 Claude Code 里，memory 最常见的误解是：

> “只要有一个巨长的 `CLAUDE.md`，Claude 就应该永远记得所有事。”

现实不是这样。

更实用的理解是：

- `CLAUDE.md` 是项目记忆入口
- `rules` 是可拆分的局部规则
- 子目录的 `CLAUDE.md` 是更细颗粒度的上下文

关键不是“写多长”，而是“放在哪一层”。

## root `CLAUDE.md` 该放什么

- 项目级工作方式
- 共享约束
- 哪些目录有特殊规则
- 回答问题时的优先信息源

不建议塞进去的：

- 冗长历史背景
- 一次性任务说明
- 很细的局部页面规范

## 子目录 `CLAUDE.md` 什么时候有用

当你的仓库是 monorepo，或者不同模块真的有明显不同的工作方式时，它就很有用。

上游最值得抄的一点，是把 memory 的加载方式讲得很清楚：

- 向上找祖先目录时会加载
- 向下的子目录 memory 是按需加载
- 兄弟目录不会无缘无故混进来

这件事对中文用户尤其重要，因为很多人会把所有说明都堆在根目录，最后谁都不爱看。

## 这个仓库怎么做的

根 [`CLAUDE.md`](../CLAUDE.md) 做了三件事：

1. 解释仓库是什么
2. 规定读这个仓时优先查哪里
3. 说明关键系统，比如 weather workflow、hooks、presentation rule

这就是一个比较好的项目级记忆写法：

- 有方向
- 不啰嗦
- 能约束 Claude 的行为

## 中文团队实战建议

建议把 memory 拆成三层：

### 层 1：根 `CLAUDE.md`

放团队共享规则和工作方式。

### 层 2：`.claude/rules/*.md`

放可复用、可拆分、路径相关的规则。

### 层 3：子目录 `CLAUDE.md`

放真正模块级的差异，不要乱建。

## 一句话判断

memory 的重点不是“写更多”，而是“让 Claude 在正确的层读到正确的东西”。
