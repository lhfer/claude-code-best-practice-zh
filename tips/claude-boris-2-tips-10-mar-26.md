# Code Review 与 Test Time Compute：Boris 的两条高信号建议

> 中文重编版
> 原始来源：
> - Boris 原帖：<https://x.com/bcherny/status/2031089411820228645>
> - 上游整理：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-boris-2-tips-10-mar-26.md>

## 这篇其实在讲两件事

### 1. Code Review

Claude Code 的代码审查价值，不是“省一个 reviewer”，而是：

- 多 agent 视角并行审查
- 能补到人眼容易漏掉的问题
- 当代码产出速度大幅增加后，review 成为新的瓶颈

### 2. Test Time Compute

同一个模型在不同上下文窗口里做交叉验证，本身就是一种额外算力投入。

换句话说：

> 不是只有训练时算力重要，验证时怎么算、开几个上下文，也很重要。

## 对中文团队最有价值的启发

- 当 AI 产出代码越来越快，review 会越来越成为瓶颈
- “多上下文交叉验证”是一种非常实用的防幻觉方法
- 即使是同一个模型，放在不同上下文里也能互相纠错

## 适合谁看

- 开始把 Claude 写出来的代码送进 PR 流程的人
- 正在 고민怎么提高代码审查质量的人
- 想理解“多个 context window 值不值得”的人
