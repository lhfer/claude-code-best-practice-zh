# Cross-Model Workflow

> Claude Code + Codex 的协作工作流
> 参考：
> - <https://github.com/shanraisshan/claude-code-best-practice>
> - <https://github.com/shanraisshan/codex-cli-best-practice>

## 这条工作流在解决什么问题

不是在回答“Claude 和 Codex 谁更强”，而是在回答：

> 如果我两个都在用，应该怎么分工才最顺手？

这条 workflow 的答案是：

1. Claude Code 做 plan
2. Codex 做 QA review
3. Claude Code 负责实现
4. Codex 做最终 verify

## 一眼看懂

```text
PLAN      -> Claude Code
QA REVIEW -> Codex
IMPLEMENT -> Claude Code
VERIFY    -> Codex
```

## 每一步的职责

### 1. PLAN

在 Claude Code 里进入 plan mode。

目标：

- 把需求问清楚
- 形成 phased plan
- 明确测试门槛

### 2. QA REVIEW

让 Codex 读这份 plan，补：

- 漏掉的实现阶段
- 风险点
- 中间验证步骤

重点是“补强计划”，不是重写原计划。

### 3. IMPLEMENT

回到 Claude Code，按 phase 去实现。

### 4. VERIFY

最后再让 Codex 站在“审阅者”视角看结果有没有偏离计划。

## 对中文用户最重要的启发

- 多模型协作不是二选一
- 真正重要的是工位划分
- 让不同模型在不同阶段发力，往往比单模型硬顶更稳

## 参考图

![Cross-Model Workflow](assets/cross-model-workflow.png)
