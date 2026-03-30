# 浏览器自动化 MCP 怎么选：Claude in Chrome vs Chrome DevTools MCP vs Playwright

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-in-chrome-v-chrome-devtools-mcp.md>

## 先讲结论

如果你想给 Claude 一个稳定、可复用、适合自动化测试的浏览器能力层：

- **首选：Playwright MCP**
- **次选：Chrome DevTools MCP**
- **场景型补充：Claude in Chrome**

## 为什么

### Playwright MCP

优点：

- 自动化测试语义成熟
- 跨页面流程更稳
- 更适合脚本化和重复验证

### Chrome DevTools MCP

优点：

- 对浏览器内部状态、console、network 观察更强
- 更像调试工具而不是测试框架

### Claude in Chrome

优点：

- 更贴近真实浏览器使用体验
- 对“让 Claude 直接在浏览器里操作”这件事很直观

局限：

- 更偏交互式辅助，不是最稳的自动化测试底座

## 怎么选

### 你主要做自动化测试

选 Playwright MCP。

### 你主要做浏览器调试

选 Chrome DevTools MCP。

### 你主要做“让 Claude 看见真实浏览器”

再考虑 Claude in Chrome。

## 对中文用户最有价值的启发

不要把“能控制浏览器”当成单一能力。
浏览器自动化至少分三类：

- 调试
- 测试
- 真实交互观察

不同 MCP 擅长的是不同层。

## 一句话总结

Playwright 更像稳定测试底座，DevTools 更像深调试利器，Claude in Chrome 更像贴近真实操作体验的辅助层。
