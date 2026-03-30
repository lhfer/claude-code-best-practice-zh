# CLI Startup Flags Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-cli-startup-flags.md>

## 先讲人话

如果你已经开始把 Claude Code 真正纳入日常工作流，启动参数就不是“冷门小知识”，而是你怎么开工的入口层。

最常见的几类启动参数，其实分别在决定：

- 你要恢复哪个会话
- 你用哪个模型
- 你给 Claude 多大权限
- 它要以什么格式输出
- 它要带着什么 system prompt / agent / MCP / 插件起步

## 最值得先记住的几类参数

### 1. 会话管理

适合高频使用的：

- `--continue`
- `--resume`
- `--fork-session`
- `--remote`
- `--teleport`

这类参数决定你是从哪段上下文开始工作，而不是从零开新局。

### 2. 模型与配置

最重要的：

- `--model`
- `--fallback-model`
- `--betas`

如果你经常切场景，这些参数会比在会话里临时改更可控。

### 3. 权限与安全

重点是：

- `--permission-mode`
- `--allowedTools`
- `--disallowedTools`
- `--dangerously-skip-permissions`

真正的经验不是“把权限全开”，而是让启动方式就带着清楚的安全边界。

### 4. 输出与格式

最常用的是：

- `--print`
- `--output-format`
- `--json-schema`
- `--verbose`

如果你把 Claude Code 接到脚本、自动化或其他系统里，这一组尤其重要。

### 5. Agent / MCP / 目录

这类参数决定的是启动时环境：

- `--agent`
- `--agents`
- `--mcp-config`
- `--plugin-dir`
- `--add-dir`
- `--worktree`

## 对中文用户最实用的判断

### 如果你只是日常手动用

先掌握：

- `--continue`
- `--resume`
- `--model`
- `--permission-mode`

### 如果你开始做自动化或脚本接入

重点看：

- `--print`
- `--output-format`
- `--json-schema`
- `--max-turns`

### 如果你开始做多目录 / 多代理 / 多工具工作流

重点看：

- `--agent`
- `--mcp-config`
- `--plugin-dir`
- `--add-dir`
- `--worktree`

## 最容易犯的错

- 只会在会话里改设置，不会在启动层固定上下文
- 把危险权限参数当成效率捷径
- 不区分“交互式使用”和“脚本式使用”

## 一句话总结

启动参数不是冷门附录，它决定了 Claude Code 一开场就站在哪个工作流姿势里。
