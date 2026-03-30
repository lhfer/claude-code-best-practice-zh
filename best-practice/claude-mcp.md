# MCP Servers Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-mcp.md>

## 先讲人话

MCP 不是“Claude 变得更强”的抽象说法，而是：

> 让 Claude 接上外部工具、文档、浏览器、数据库和 API 的标准方式。

但真正的最佳实践不是“接越多越好”，而是：

> 只接你真的高频会用、而且能明显降低幻觉或人工切换成本的那几类。

## 这个仓库为什么值得看

因为它对 MCP 的态度很克制。

`.mcp.json` 里只放了少量高频项，而不是把 MCP 当收藏夹：

- Context7
- Playwright
- DeepWiki

这其实就是很成熟的判断：

- 研究层：Context7 / DeepWiki
- 浏览器验证层：Playwright

## 日常最值得先接的几类 MCP

### 1. 文档类

代表：Context7、DeepWiki

适合：

- 查库文档
- 查第三方 API
- 查仓库结构和 wiki

### 2. 浏览器 / 调试类

代表：Playwright、Chrome 相关 MCP

适合：

- 页面验证
- 自动化测试
- console / network 调试

### 3. 图形 / 说明类

代表：Excalidraw 这类

适合：

- 生成架构图
- 产出流程图

## 配置怎么理解

最关键的是三件事：

### 1. 放在哪一层

- 项目级：`.mcp.json`
- 用户级：`~/.claude.json`
- agent 级：agent frontmatter

### 2. 怎么控制启用

和 `.claude/settings.json` 配合：

- `enableAllProjectMcpServers`
- `enabledMcpjsonServers`
- `disabledMcpjsonServers`

### 3. 怎么配权限

MCP 工具最终还是要落到权限规则里，例如：

- `mcp__*`
- `mcp__context7__*`
- `mcp__playwright__browser_snapshot`

## 中文团队最值得抄的原则

- 先接高频 MCP，再接“看起来很酷”的 MCP
- 先解决文档真实性和浏览器可见性，再扩展更多玩法
- 不要让 MCP 数量本身变成上下文噪音

## 一句话总结

好的 MCP 策略不是“全都接”，而是“把最关键的外部能力稳稳接上”。
