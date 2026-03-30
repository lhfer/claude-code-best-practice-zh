# Boris 的 13 条 Claude Code 日常工作流建议

> 中文重编版
> 原始来源：
> - Boris 原帖：<https://x.com/bcherny/status/2007179832300581177>
> - 上游整理：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-boris-13-tips-03-jan-26.md>

## 为什么这篇特别值得看

因为它最接近“一个真正高频用户每天怎么用 Claude Code”。

不是官方功能清单，也不是理想化教程，而是比较贴近日常工作的默认姿势。

## 13 条建议，压缩成中文版

1. **同时跑 5 个 Claude**
2. **不够就继续并行到网页端**
3. **复杂任务优先用更强模型和思考模式**
4. **团队共享一份 `CLAUDE.md`**
5. **在 PR 里用 @claude 反向更新规范**
6. **大多数 session 都从 plan mode 开始**
7. **把高频流程变成 slash command**
8. **把常见流程自动化给 subagent**
9. **用 PostToolUse hook 做自动格式化**
10. **别乱用 `--dangerously-skip-permissions`**
11. **MCP 让 Claude 真正接上你的工具**
12. **长任务交给后台 agent 验证**
13. **永远给 Claude 一个验证自己工作的办法**

## 对中文用户最重要的 3 条

如果你现在只想记 3 条，我建议是：

1. plan mode
2. shared `CLAUDE.md`
3. 给 Claude 一个验证路径

这 3 件事能直接把“vibe coding”拉向“工程化协作”。

## 适合谁看

- 想从“偶尔用”升级到“日常重度使用”的人
- 已经开始在团队里共享 Claude 工作方式的人
- 想知道高级用户默认姿势长什么样的人
