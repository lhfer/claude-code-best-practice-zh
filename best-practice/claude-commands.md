# Commands Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-commands.md>

## 先讲人话

command 的核心价值不是“更酷的斜杠命令”，而是：

> 把你自己一天里会重复做的工作流，变成一个明确、可复用、可分享的入口。

比如：

- `/review-pr`
- `/release-check`
- `/spec-sync`
- `/techdebt`

这些东西如果天天要重复讲一遍，command 就比手打 prompt 更像工程方案。

## command 最适合解决什么问题

- 用户明确想手动触发某件事
- 这件事有固定顺序
- 需要调度 skill 或 agent
- 你不想让主对话永远带着这段长说明

command 是“入口”，不是“长期知识载体”。

## 这件事要特别说明

官方这两年的方向，已经越来越把“自定义 commands”和“skills”合并到一套能力模型里看。

也就是说：

- `.claude/commands/` 还可用
- 但在产品语义上，command 和 skill 的边界没有过去那么硬

这个仓库仍然保留了三分法：

- commands
- agents
- skills

这是为了教学更清楚。
中文读者在使用时要记住：

> 这套分类法很有帮助，但不是必须按字面理解成 3 个彼此绝缘的世界。

## 什么时候优先选 command

- 用户应该显式决定是否执行
- 流程有明确起点
- 你需要一个稳定入口调度其他能力
- 你希望这段说明不常驻在主上下文里

## 什么时候别急着上 command

- 只是想让 Claude 自动记住一条规范
- 只是想存一段经常会自动触发的知识
- 这件事本质上更像 skill

## 这个仓库里的代表性样例

`/weather-orchestrator` 非常适合做 command 入门样例，因为它刚好体现了 command 的 4 个职责：

1. 接收用户请求
2. 跟用户补一个必要参数
3. 调 agent 去干自治任务
4. 再调 skill 生成结果

看这里：

- [implementation/claude-commands-implementation.md](../implementation/claude-commands-implementation.md)
- [orchestration-workflow/orchestration-workflow.md](../orchestration-workflow/orchestration-workflow.md)

## 中文用户常见误区

### 误区 1：command 就是把 prompt 存起来

这是最初级的一层。
更好的 command 应该能：

- 组织用户交互
- 限定工具
- 调度 agent / skill
- 约束输出结果

### 误区 2：每件小事都做一个 command

结果就是 slash 菜单塞满，但没有学习路径，也没有优先级。

command 应该服务“高频工作流”，不是服务“每一个灵感”。

## 一句话判断

如果你脑子里想到的是“我想给某个工作流做一个明确入口”，那你想的多半就是 command。
