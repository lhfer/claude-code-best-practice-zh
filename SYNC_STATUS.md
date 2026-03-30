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
| `README.md` | 已中文化 | 中文主入口，已补社区层入口与校验说明 |
| `LOCALIZATION_POLICY.md` | 已中文化 | 中文 fork 治理文件 |
| `GLOSSARY.md` | 已中文化 | 统一术语 |
| `CONTRIBUTING.md` | 已中文化 | 面向中文贡献者 |
| `PROTECTED_RUNTIME_PATHS.txt` | 新增 | 受保护路径清单 |
| `scripts/validate_localization.py` | 新增 | 本地化校验脚本 |
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
| `tips/README.md` | 已中文化 | 社区经验索引 |
| `tips/*.md` | 已中文化 | 改为中文导读 / 摘要版 |
| `videos/README.md` | 已中文化 | 视频导读索引 |
| `videos/*.md` | 已中文化 | 改为中文导读版 |
| `tutorial/README.md` | 已中文化 | 中文 onboarding 入口 |
| `tutorial/day0/*` | 已中文化 | 命令保持英文，说明改中文 |
| `development-workflows/README.md` | 已中文化 | 工作流索引 |
| `development-workflows/**/*.md` | 已中文化 | 说明层改为中文 |
| `agent-teams/README.md` | 已中文化 | 团队编排索引 |
| `agent-teams/agent-teams-prompt.md` | 已中文化 | 仅提示词说明层 |
| `changelog/README.md` | 已中文化 | 维护者入口 |
| `changelog/**/*.md` | 已中文化 | 标题 / 导语 / 结构提示中文化 |
| `.claude/hooks/HOOKS-README.md` | 已中文化 | docs-only 文件 |
| `.codex/hooks/HOOKS-README.md` | 已中文化 | docs-only 文件 |
| `presentation/README.md` | 已中文化 | 演示层说明 |
| `presentation/index.html` | 已中文化 | 已翻译主要可见文案，结构 / 脚本 / 资源路径保持不变 |
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

- 继续扩展更多 `reports/` 的中文版本
- 评估是否补一个“适合中国团队怎么抄这个仓”的落地指南
