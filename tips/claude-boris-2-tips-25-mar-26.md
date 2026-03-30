# 为什么要 Squash Merge，以及为什么 PR 要更小

> 中文重编版
> 原始来源：
> - Boris 原帖：<https://x.com/bcherny/status/2038552880018538749>
> - 上游整理：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-boris-2-tips-25-mar-26.md>

## 这篇最核心的两个观点

### 1. 高速 AI 开发下，PR 越小越好

当产出速度上来后，大 PR 并不会显得“更高效”，反而会：

- 更难 review
- 更难回滚
- 更难定位问题

### 2. Squash merge 是更务实的默认选项

因为在高频 AI 辅助开发里，分支内会出现大量：

- fix lint
- retry
- 再试一次
- 小修小补

这些 commit 对主分支历史几乎没有信息价值。

## 对中文团队的启发

- AI 时代更要重视 PR 粒度
- “一个 PR = 一个可理解改动”比“保留所有中间提交”更重要
- 想让 review 真正跟上产出速度，小 PR 和 squash 几乎是标配

## 一句话总结

Claude 写得更快，不代表你可以把更多变化塞进一个 PR。
恰恰相反，越快越要把 PR 切小。
