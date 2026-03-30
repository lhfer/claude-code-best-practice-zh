# Settings Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-settings.md>

## 先说这篇要解决什么

这篇不是逐项翻译上游那份 900 多行的 settings 大全，而是想先帮中文读者建立一个更靠谱的“设置脑图”：

- 哪些是运行时控制面
- 哪些是安全边界
- 哪些是团队共享项
- 哪些只是个性化外观

如果这张脑图没立住，后面你再看字段表，也很容易越看越乱。

## 先讲人话

很多人以为 Claude Code 不听话，是 prompt 不够狠。

更常见的现实是：

- 该放在 `CLAUDE.md` 的东西塞进 prompt
- 该放在 settings 的东西变成了口头要求
- 该用 hooks 或 rules 管的行为，被期待模型自己“记住”

所以 settings 不是装饰文件，而是**运行时控制面**。

## 你可以先把 settings 分成 5 层

### 1. 权限层

你主要在决定：

- 什么默认允许
- 什么需要 ask
- 什么必须 deny

这一层解决的是“安全边界”，不是“体验优化”。

### 2. 模型与输出层

你主要在决定：

- 默认模型
- effort
- outputStyle
- fast mode

这一层决定 Claude 在你项目里“表现成什么风格”。

### 3. 工具与集成层

你主要在决定：

- MCP
- hooks
- status line
- plugins

这一层决定 Claude 会接上哪些外部能力。

### 4. 项目共享层

你主要在决定：

- 什么配置应该跟着项目走
- 什么东西该进 git
- 团队成员打开项目时应该默认获得什么行为

### 5. 个性化层

比如：

- spinner 文案
- status line 花样
- 某些个人偏好的 local settings

这层重要，但绝对不该先于前 4 层。

## 最值得先理解的优先级

从中文团队实际使用角度，建议先把这个顺序记住：

1. **安全**
2. **一致性**
3. **可协作**
4. **自动化**
5. **个性化**

你先把权限边界、模型策略、团队共享约定想清楚，再去调 spinner verbs，长期效果会好很多。

## 这个仓库的 `.claude/settings.json` 在展示什么

它明显不是“保守企业默认值”，而是一个 power-user preset。

它展示了这些方向：

- 权限开得比较宽，但高风险命令转 ask
- hooks、status line、spinner、plansDirectory 一起配置
- project MCP 更容易启用
- 输出风格和会话体验也被一起纳入控制

这非常适合教学，因为能让读者快速看到 Claude Code 能管到哪里。
但它不等于“你团队该原样照抄”的默认基线。

## 哪些设置值得优先抄

### A. 权限结构

最值得学的是分层思路，不是具体 allowlist。

你至少要明确：

- 哪类命令永远不该自动放行
- 哪类命令可以 ask
- 哪类工具可以默认允许

### B. 模型与输出风格

如果你们团队对“Claude 回答要短还是要解释”没有共识，后面的协作会很痛苦。

### C. hooks / MCP 开关

不要只会装能力，还要会决定“哪些项目默认启用、哪些先别动”。

### D. 项目级 vs local 级

团队共享的是：

- `.claude/settings.json`

个人覆盖的是：

- `.claude/settings.local.json`

这两个界限不清，仓库会很快变脏。

## 哪些设置先别急着抄

- 纯风格化的 spinner 文案
- 高个性化的 status line 文案
- 没想清楚就把所有 hooks 都挂上
- 还没理解权限边界就打开过多工具

## 中文团队的实战落地建议

如果你今天要给团队起一版 settings，建议只先管下面这些：

### 第一版必须明确

- 权限规则
- 默认模型 / effort
- output style
- MCP 是否启用
- hooks 是否启用

### 第一版可以先不追求

- 好看的 status line
- 个性化 spinner
- 花哨的外观型设置

## 一个更实用的检查表

在你提交 settings 之前，问自己：

| 问题 | 如果回答不清楚，说明还不该提交 |
|---|---|
| 我们为什么允许这些工具？ | 权限边界没想清楚 |
| 这些设置是团队共享还是我个人偏好？ | 层级混了 |
| 如果新同事打开项目，会不会被惊到？ | 默认值过猛 |
| 这些 hooks / MCP 真的是高频需求吗？ | 自动化过度 |

## 一句话总结

好的 settings，不是“把所有功能都配出来”，而是：

> 让 Claude 在这个项目里安全、稳定、可协作地工作。

## 继续读哪里

- [reports/claude-global-vs-project-settings.md](../reports/claude-global-vs-project-settings.md)
- [best-practice/claude-memory.md](claude-memory.md)
- [best-practice/claude-mcp.md](claude-mcp.md)
- 上游完整 settings 参考：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-settings.md>
