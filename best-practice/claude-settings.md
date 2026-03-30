# Settings Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-settings.md>

## 这篇不做一件事

这不是上游那份 900 多行 settings 参考的逐项中文翻译。

如果你需要查完整字段，请直接看上游原文。
这篇中文版只做一件更重要的事：

> 帮你先建立“settings 到底该怎么分层理解”的脑图。

## 先讲人话

很多人以为 Claude Code 不听话，是 prompt 写得不够凶。

实际更常见的原因是：

- 该放在 `CLAUDE.md` 的东西放进了 prompt
- 该放在 settings 的东西写成了口头要求
- 该用 rule 或 hook 管的行为，放任模型自己记

settings 不是装饰项，而是运行时控制面。

## 你先只需要掌握 4 层

### 1. 权限层

关心：

- 什么工具默认允许
- 什么需要 ask
- 什么必须 deny

这是安全边界，不是体验小调料。

### 2. 行为层

关心：

- `outputStyle`
- `plansDirectory`
- model / effort
- status line

这是 Claude 在你项目里“表现成什么样”的基础。

### 3. 自动化层

关心：

- hooks
- MCP auto-enable
- env

这层决定 Claude 能不能接外部系统、在生命周期里做额外动作。

### 4. 分层优先级

你至少要知道：

- 全局设置和项目设置不是一回事
- `settings.local.json` 和 `settings.json` 不是一个用途
- managed settings 有更高优先级

## 这个仓库的 settings 值得怎么看

这个仓库的 `.claude/settings.json` 明显不是“保守企业默认值”，而是一个 power-user 预设。

它的特点是：

- 工具放得比较开
- 对高风险命令转 ask
- 把 hooks、status line、spinner、plansDirectory 都开出来了
- 让 `.mcp.json` 的 project servers 更容易启用

这说明它更像“能力展示 + 强个性化配置”，而不是“适合所有团队照抄”的基线。

## 哪些值得抄，哪些别急着抄

### 值得抄

- 权限分层思路
- `deny / ask / allow` 的基本结构
- 用 settings 管模型和输出风格，而不是全靠 prompt
- 用 settings 接 hooks 和 MCP

### 别急着抄

- 过度个性化的 spinner verbs
- 高风格化的 status line 文案
- 把所有可能的 hook 都先挂上
- 没想清楚就打开过多工具权限

## 给中文团队的实战建议

第一版 settings，建议只先管 4 件事：

1. 权限
2. 模型 / effort
3. output style
4. MCP / hooks 是否启用

别一上来就把每个花活都配上。

## 继续读哪里

- [reports/claude-global-vs-project-settings.md](../reports/claude-global-vs-project-settings.md)
- [best-practice/claude-memory.md](claude-memory.md)
- 上游完整 settings 参考：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-settings.md>
