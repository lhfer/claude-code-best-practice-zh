# GLOSSARY

这份词汇表只做一件事：让整仓中文表达稳定，不一会儿“代理”、一会儿“子智能体”、一会儿“子代理”。

## 术语表

| 英文 | 推荐中文 | 保留英文？ | 说明 |
|---|---|---|---|
| Agent / Subagent | agent / 子 agent | 是 | 这类词已经是产品概念，强翻反而别扭。正文里优先写“agent（子 agent）”。 |
| Skill | skill | 是 | 不建议翻成“技能卡”或“技能包”。 |
| Command | command / 命令 | 是 | 指 Claude Code 里的 slash command。 |
| Hook | hook | 是 | 可解释为“生命周期钩子”，但正文里保留 `hook` 更自然。 |
| Memory | memory / 记忆 | 是 | 讲概念时写“memory（记忆）”。 |
| Context | context / 上下文 | 是 | 中文正文常写“上下文”，首次出现保留英文。 |
| Context fork | context fork / 分叉上下文 | 是 | 不要翻成“上下文分裂”之类奇怪表达。 |
| Worktree | git worktree / 工作树 | 是 | 建议保留 `git worktree`。 |
| Plan Mode | plan mode / 规划模式 | 是 | 首次出现双写。 |
| MCP | MCP | 是 | 默认不展开全称，必要时说明是 Model Context Protocol。 |
| Runtime | 运行时 | 可选 | 用于区分“执行层”和“说明层”。 |
| Frontmatter | frontmatter | 是 | 常见于文档生态，保留英文更准确。 |
| Progressive disclosure | 渐进式披露 | 否 | 中文里可解释为“把重资料拆出去，按需加载”。 |
| Auto-invocation | 自动触发 | 否 | 用于说明 Claude 会不会自己调用某项能力。 |
| Fork | fork | 是 | GitHub 语境下不建议译成“派生副本”。 |
| Upstream | upstream / 上游 | 是 | 版本同步语境里保留。 |

## 推荐写法

- 第一次出现：`skill（可复用能力单元）`
- 第二次开始：`skill`
- 需要面向新手解释时：先用中文描述功能，再给术语

例如：

- 不推荐：`Subagent 是一个 autonomous actor in isolated context`
- 推荐：`subagent 是 Claude 在独立上下文里运行的一个子 agent，适合把复杂任务拆出去自治处理。`

## 不推荐写法

- 把 `skill` 统一翻成“技能”
- 把 `agent` 强翻成“智能体”并在全仓只用这个词
- 把 `hook` 翻成“挂钩程序”
- 把 `fork` 翻成“分叉仓库”并完全不提 GitHub 语义

## 术语更新规则

术语要改，请优先提 issue 或 PR，并说明：

- 为什么当前译法不够自然或不够准确
- 是否影响现有文档一致性
- 是否需要全仓批量替换
