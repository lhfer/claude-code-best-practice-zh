# SYNC_STATUS

## Upstream 信息

- Upstream 仓库：`shanraisshan/claude-code-best-practice`
- Upstream 地址：<https://github.com/shanraisshan/claude-code-best-practice>
- 当前对齐 commit：`7cde3f3232817c781b8ba0fd39cb2d707fd547c7`
- 当前对齐日期：`2026-03-30`
- Fork 仓库：`lhfer/claude-code-best-practice`

## 当前策略

- 以 upstream 为事实源
- 中文 fork 负责“中文入口、中文解释、本土化组织”
- 运行时示例和配置保持英文原样

## 模块同步状态

| 模块 | 状态 | 说明 |
|---|---|---|
| `README.md` | 已中文化 | 作为中文主入口重写 |
| `LOCALIZATION_POLICY.md` | 新增 | 中文 fork 治理文件 |
| `GLOSSARY.md` | 新增 | 统一术语 |
| `CONTRIBUTING.md` | 新增 | 面向中文贡献者 |
| `best-practice/claude-subagents.md` | 已中文化 | v1 重编 |
| `best-practice/claude-skills.md` | 已中文化 | v1 重编 |
| `best-practice/claude-commands.md` | 已中文化 | v1 重编 |
| `best-practice/claude-settings.md` | 已中文化 | v1 重编 |
| `best-practice/claude-memory.md` | 已中文化 | v1 重编 |
| `reports/claude-agent-command-skill.md` | 已中文化 | v1 重编 |
| `reports/claude-global-vs-project-settings.md` | 已中文化 | v1 重编 |
| `reports/claude-skills-for-larger-mono-repos.md` | 已中文化 | v1 重编 |
| `implementation/` weather 相关说明 | 已中文化 | 仅说明层 |
| `orchestration-workflow/` 说明层 | 已中文化 | 仅说明层 |
| `tips/` 全量正文 | 待处理 | 先不逐篇翻译，优先保留原始来源 |
| `presentation/` | 待处理 | 暂不中文化执行层和视觉资产 |
| `.claude/` | 保持英文 | 运行时不翻译 |
| `.codex/` | 保持英文 | 运行时不翻译 |
| `.mcp.json` | 保持英文 | 运行时不翻译 |

## 同步时怎么记

建议每次同步都补一段：

```md
### 2026-xx-xx

- upstream commit:
- 受影响模块:
- 已同步:
- 待处理:
- 备注:
```

## 当前待办

- 给 `tips/` 做中文摘要索引，而不是逐篇机翻
- 增加更多中文 report
- 评估是否需要补一个“适合中国团队怎么抄这个仓”的落地指南
