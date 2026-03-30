# claude-code-best-practice

> 给中国开发者的 Claude Code 中文参考仓。
> 基于上游 [`shanraisshan/claude-code-best-practice`](https://github.com/shanraisshan/claude-code-best-practice) fork，并做了中文化、本土化、学习路径重编。

[![Upstream](https://img.shields.io/badge/upstream-shanraisshan%2Fclaude--code--best--practice-0969da?style=flat)](https://github.com/shanraisshan/claude-code-best-practice)
[![License](https://img.shields.io/badge/license-MIT-2ea44f?style=flat)](LICENSE)
[![Chinese First](https://img.shields.io/badge/docs-Chinese%20first-ffb703?style=flat)](#推荐阅读顺序)
[![Keep Runtime in English](https://img.shields.io/badge/runtime-English%20unchanged-6c757d?style=flat)](LOCALIZATION_POLICY.md)
[![Sync Status](https://img.shields.io/badge/sync-v1%20in%20progress-8250df?style=flat)](SYNC_STATUS.md)
[![Validator](https://img.shields.io/badge/validator-protected%20runtime-2f855a?style=flat)](scripts/validate_localization.py)

## 这仓库是什么

这不是一个“把英文 README 机翻成中文”的仓库。

它更像一个适合中文读者的 Claude Code 学习入口，目标是把上游仓库里最有价值的部分，重新组织成你能快速读懂、愿意继续点下去、也敢拿去参考自己项目的版本。

如果你是下面两类人，这个 fork 是给你准备的：

- 常年混 GitHub、看仓库很挑的开发者：你想知道这仓库到底靠不靠谱，值不值得 star，结构干不干净，维护姿态稳不稳。
- 想认真学 Claude Code 的中文用户：你不想被术语、海外社区语境、直译腔和视觉噪音劝退，希望有一个真正“带你入门”的入口。

## 这仓库不是什么

- 不是 Claude Code 官方中文版。
- 不是“一键复制就能落地”的万能模板仓。
- 不是把 `.claude/` 里的运行时文件全部翻成中文的实验品。
- 不是对上游逐句逐段的忠实转录。

## 10 秒看懂

上游仓库真正厉害的地方，不是某一条 prompt 或某一个 agent，而是它把下面这些层分开设计了：

- `CLAUDE.md` / `rules`：决定 Claude 在这个仓里要遵守什么约束。
- `settings` / `hooks` / `MCP`：决定 Claude 有什么权限、连接什么工具、在什么事件上触发什么行为。
- `commands` / `agents` / `skills`：决定工作流如何被编排、自治和复用。
- `implementation` / `orchestration-workflow`：把概念落成可运行样例。
- `reports`：解释哪些概念容易混、哪些边界会漂移、哪些说法已经跟官方发生变化。

这份中文 fork 的核心任务，就是把这些层讲明白。

## 推荐阅读顺序

如果你是第一次认真看 Claude Code，建议按这个顺序读：

1. [README.md](README.md)
2. [Agents vs Commands vs Skills](reports/claude-agent-command-skill.md)
3. [Subagents Best Practice](best-practice/claude-subagents.md)
4. [Skills Best Practice](best-practice/claude-skills.md)
5. [Settings Best Practice](best-practice/claude-settings.md)
6. [Memory Best Practice](best-practice/claude-memory.md)
7. [Orchestration Workflow](orchestration-workflow/orchestration-workflow.md)

如果你已经会用一点 Claude Code，想直接看“怎么落地”：

1. [Commands Best Practice](best-practice/claude-commands.md)
2. [Global vs Project Settings](reports/claude-global-vs-project-settings.md)
3. [Skills in Monorepos](reports/claude-skills-for-larger-mono-repos.md)
4. [Subagents Implementation](implementation/claude-subagents-implementation.md)
5. [Skills Implementation](implementation/claude-skills-implementation.md)
6. [Commands Implementation](implementation/claude-commands-implementation.md)

如果你更在意“社区里的人到底怎么用它”，建议走这条路线：

1. [tips/README.md](tips/README.md)
2. [videos/README.md](videos/README.md)
3. [development-workflows/README.md](development-workflows/README.md)
4. [tutorial/README.md](tutorial/README.md)
5. [agent-teams/README.md](agent-teams/README.md)

## 核心概念速览

| 概念 | 一句话解释 | 从哪里开始读 |
|---|---|---|
| `Agent / Subagent` | 让 Claude 在独立上下文里自治做一件事，适合多步研究、隔离上下文、限制权限 | [best-practice/claude-subagents.md](best-practice/claude-subagents.md) |
| `Skill` | 可复用的知识或流程单元，可以自动触发，也可以手动调用，还能带 supporting files | [best-practice/claude-skills.md](best-practice/claude-skills.md) |
| `Command` | 用户明确触发的工作流入口，适合把一串固定动作收成 `/xxx` | [best-practice/claude-commands.md](best-practice/claude-commands.md) |
| `Settings` | 决定权限、模型、hooks、MCP、status line 等运行时行为的配置层 | [best-practice/claude-settings.md](best-practice/claude-settings.md) |
| `Memory` | Claude 读哪些记忆文件、怎么分层加载、根目录和子目录各放什么 | [best-practice/claude-memory.md](best-practice/claude-memory.md) |
| `MCP` | 给 Claude 接外部工具和数据源，不是越多越好，而是要克制地接高频能力 | [best-practice/claude-mcp.md](https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-mcp.md) |
| `Hooks` | 在 Claude 的生命周期事件上挂外部动作，比如通知、日志、格式化或保护逻辑 | [上游 Hooks 仓](https://github.com/shanraisshan/claude-code-hooks) |

## 第一批已经中文化的内容

### 中文入口与治理

- [LOCALIZATION_POLICY.md](LOCALIZATION_POLICY.md)
- [GLOSSARY.md](GLOSSARY.md)
- [SYNC_STATUS.md](SYNC_STATUS.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

### 核心知识层

- [best-practice/claude-subagents.md](best-practice/claude-subagents.md)
- [best-practice/claude-skills.md](best-practice/claude-skills.md)
- [best-practice/claude-commands.md](best-practice/claude-commands.md)
- [best-practice/claude-settings.md](best-practice/claude-settings.md)
- [best-practice/claude-memory.md](best-practice/claude-memory.md)

### 关键解释层

- [reports/README.md](reports/README.md)
- [reports/claude-agent-command-skill.md](reports/claude-agent-command-skill.md)
- [reports/claude-global-vs-project-settings.md](reports/claude-global-vs-project-settings.md)
- [reports/claude-skills-for-larger-mono-repos.md](reports/claude-skills-for-larger-mono-repos.md)
- [reports/claude-agent-memory.md](reports/claude-agent-memory.md)
- [reports/claude-usage-and-rate-limits.md](reports/claude-usage-and-rate-limits.md)
- [reports/claude-advanced-tool-use.md](reports/claude-advanced-tool-use.md)
- [reports/claude-in-chrome-v-chrome-devtools-mcp.md](reports/claude-in-chrome-v-chrome-devtools-mcp.md)
- [reports/claude-agent-sdk-vs-cli-system-prompts.md](reports/claude-agent-sdk-vs-cli-system-prompts.md)
- [reports/llm-day-to-day-degradation.md](reports/llm-day-to-day-degradation.md)

### 样例链路层

- [orchestration-workflow/orchestration-workflow.md](orchestration-workflow/orchestration-workflow.md)
- [implementation/claude-subagents-implementation.md](implementation/claude-subagents-implementation.md)
- [implementation/claude-skills-implementation.md](implementation/claude-skills-implementation.md)
- [implementation/claude-commands-implementation.md](implementation/claude-commands-implementation.md)

### 社区内容层

- [tips/README.md](tips/README.md)
- [videos/README.md](videos/README.md)
- [development-workflows/README.md](development-workflows/README.md)
- [tutorial/README.md](tutorial/README.md)
- [agent-teams/README.md](agent-teams/README.md)
- [changelog/README.md](changelog/README.md)
- [presentation/README.md](presentation/README.md)

## 中文化原则

这份 fork 只有一个核心原则：**执行层不乱动，说明层彻底重编。**

不会翻译的内容：

- 代码、命令、frontmatter、路径、配置键、环境变量、工具名、模型名。
- `.claude/`、`.codex/`、`.mcp.json` 中会影响运行行为的正文和配置。

会重编的内容：

- README
- best-practice
- reports
- implementation
- orchestration-workflow
- tips
- videos
- tutorial
- development-workflows
- agent-teams
- changelog
- presentation（仅可见文案）

详细规则见 [LOCALIZATION_POLICY.md](LOCALIZATION_POLICY.md)。

## 零功能漂移校验

这份 fork 不是“中文看起来更顺”，而是要做到：

> 中文化之后，原仓的执行层能力不能被我改坏。

为此仓库新增了两层保护：

- 受保护路径清单：[PROTECTED_RUNTIME_PATHS.txt](PROTECTED_RUNTIME_PATHS.txt)
- 本地校验脚本：[scripts/validate_localization.py](scripts/validate_localization.py)

提交前建议运行：

```bash
python3 scripts/validate_localization.py
```

## 如何跟上游同步

这件事很重要。GitHub 上最差的一类 fork，就是挂着“中文版”名号，但半年不跟上游、概念全漂移、链接全失效。

这份仓库默认把上游当成事实源。同步时请按下面做：

```bash
git remote add upstream https://github.com/shanraisshan/claude-code-best-practice
git fetch upstream
git checkout main
git merge upstream/main
```

然后：

1. 先更新 [SYNC_STATUS.md](SYNC_STATUS.md)。
2. 标出受影响模块。
3. 判断哪些是“直接同步”，哪些需要“中文重编”。
4. 最后再改 README 和中文说明文档。

## 作为一个好 fork，这里应该长什么样

### GitHub 老开发者会在意

- 首屏能看懂这仓库到底值不值得看。
- upstream、license、同步状态、贡献方式是否透明。
- 是否有清楚的术语表和翻译边界。
- 是否像一个维护过的仓，而不是一次性搬运。

### 想学 Claude 的中文小白会在意

- 第一次进来能不能知道自己先看什么。
- 术语是不是先讲人话，再给英文原名。
- 能不能分清什么能改、什么别乱改、什么只是示例。
- README 看完后，会不会真的愿意再点进去看 3 到 5 篇核心文档。

## 贡献方式

欢迎这几类贡献：

- 上游同步提醒
- 术语统一修正
- 中文表达润色
- 本土化建议
- 哪一节读起来“像翻译腔”的直接指出

请先看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 保留的上游资产

这份 fork 默认保留上游的这些优点：

- 原始运行样例
- `.claude/` / `.codex/` 的真实配置
- 天气工作流演示链路
- 大量对外引用和资料索引
- MIT 许可

如果你想看原汁原味的英文版，请直接去上游：

- 上游仓库：https://github.com/shanraisshan/claude-code-best-practice

如果你想先用中文把体系吃透，再回去读原仓，这里就是给你准备的入口。
