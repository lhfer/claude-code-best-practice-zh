# claude-code-best-practice

> 一份给中文开发者的 Claude Code 实战参考仓。
> 帮你从“会用一点”走到“真的能把 Claude 接进项目、工作流和团队协作里”。

[![Upstream](https://img.shields.io/badge/upstream-shanraisshan%2Fclaude--code--best--practice-0969da?style=flat)](https://github.com/shanraisshan/claude-code-best-practice)
[![License](https://img.shields.io/badge/license-MIT-2ea44f?style=flat)](LICENSE)
[![Chinese First](https://img.shields.io/badge/docs-Chinese%20first-ffb703?style=flat)](#从哪里开始读)
[![Sync Status](https://img.shields.io/badge/sync-major%20content%20done-8250df?style=flat)](SYNC_STATUS.md)
[![Validator](https://img.shields.io/badge/validator-protected%20runtime-2f855a?style=flat)](scripts/validate_localization.py)
[![Learning PDF](https://img.shields.io/badge/pdf-learning%20guide-d97706?style=flat)](output/pdf/claude-code-best-practice-zh-learning-guide.pdf)
[![Complete PDF](https://img.shields.io/badge/pdf-complete%20handbook-b91c1c?style=flat)](output/pdf/claude-code-best-practice-zh-complete-handbook.pdf)

## 你来这个仓库能得到什么

- 少踩坑：少走 prompt、权限、上下文、工作流设计上的弯路
- 快上手：从安装、概念、样例到 workflow 都有清晰入口
- 能照抄：仓库里不只是讲概念，还有可运行样例和结构化实现思路
- 能进阶：当你不满足于“让 Claude 写两行代码”时，这里会告诉你怎么往工程化、团队化继续走

## PDF 下载

- [快速学习版 PDF](output/pdf/claude-code-best-practice-zh-learning-guide.pdf)
  适合第一次快速过一遍学习路径。
- [完整手册 PDF](output/pdf/claude-code-best-practice-zh-complete-handbook.pdf)
  适合脱离 GitHub 仓库、离线系统阅读。

## 这个仓库最适合谁

- 想认真学 Claude Code、但又不想被英文社区语境和术语门槛劝退的人
- 已经在用 Claude Code，但感觉还停留在“想到啥问啥”的阶段，想升级工作流的人
- 想把 `CLAUDE.md`、`skills`、`agents`、`commands`、`MCP`、`hooks` 真正接进项目的开发者和团队

## 从哪里开始读

### 如果你今天就想先跑起来

1. [先把 Claude Code 装好并登录](tutorial/day0/README.md)
2. [先看清这个仓能帮你什么](#你来这个仓库能得到什么)
3. [先搞懂 Command / Agent / Skill 怎么分工](reports/claude-agent-command-skill.md)

### 如果你是第一次系统理解 Claude Code

1. [Subagents 到底是什么，什么时候该用](best-practice/claude-subagents.md)
2. [Skills 到底是什么，怎么设计才好用](best-practice/claude-skills.md)
3. [Settings 真正该怎么理解，而不是只会抄配置](best-practice/claude-settings.md)
4. [Memory 和 CLAUDE.md 应该放什么](best-practice/claude-memory.md)
5. [完整看一遍最小工作流样例](orchestration-workflow/orchestration-workflow.md)

### 如果你已经会用一点，想直接看“怎么落地”

1. [Command 的实现样例](implementation/claude-commands-implementation.md)
2. [Skill 的实现样例](implementation/claude-skills-implementation.md)
3. [Subagent 的实现样例](implementation/claude-subagents-implementation.md)
4. [Agent Teams 的实现样例](implementation/claude-agent-teams-implementation.md)
5. [Scheduled Tasks 的实现样例](implementation/claude-scheduled-tasks-implementation.md)

### 如果你更关心“高手到底怎么用它”

1. [社区里的高频经验与建议](tips/README.md)
2. [长视频 / 播客的中文导读](videos/README.md)
3. [跨模型与结构化 workflow](development-workflows/README.md)
4. [多 agent 协作怎么玩](agent-teams/README.md)
5. [演示稿和分享材料](presentation/README.md)

## 核心概念速览

| 概念 | 一句话解释 | 从哪里开始读 |
|---|---|---|
| `Agent / Subagent` | 让 Claude 在独立上下文里自治做一件事，适合多步研究、隔离上下文、限制权限 | [best-practice/claude-subagents.md](best-practice/claude-subagents.md) |
| `Skill` | 可复用的知识或流程单元，可以自动触发，也可以手动调用，还能带 supporting files | [best-practice/claude-skills.md](best-practice/claude-skills.md) |
| `Command` | 用户明确触发的工作流入口，适合把一串固定动作收成 `/xxx` | [best-practice/claude-commands.md](best-practice/claude-commands.md) |
| `Settings` | 决定权限、模型、hooks、MCP、status line 等运行时行为的配置层 | [best-practice/claude-settings.md](best-practice/claude-settings.md) |
| `Memory` | Claude 读哪些记忆文件、怎么分层加载、根目录和子目录各放什么 | [best-practice/claude-memory.md](best-practice/claude-memory.md) |
| `MCP` | 给 Claude 接外部工具和数据源，不是越多越好，而是要克制地接高频能力 | [best-practice/claude-mcp.md](best-practice/claude-mcp.md) |
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
- [best-practice/claude-mcp.md](best-practice/claude-mcp.md)
- [best-practice/claude-cli-startup-flags.md](best-practice/claude-cli-startup-flags.md)

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
- [implementation/claude-agent-teams-implementation.md](implementation/claude-agent-teams-implementation.md)
- [implementation/claude-scheduled-tasks-implementation.md](implementation/claude-scheduled-tasks-implementation.md)

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
python3 scripts/check_upstream_sync.py
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
