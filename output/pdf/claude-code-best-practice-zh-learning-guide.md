# Claude Code 中文学习路径手册

## 这本手册适合谁

- 想系统学会 Claude Code 的中文开发者
- 已经在用 Claude Code，但感觉还停留在“想到啥问啥”的人
- 想把 Claude 接进项目、工作流和团队协作里的人

## 这本手册怎么读

- 如果你今天就想上手：先读第 1 章和第 2 章
- 如果你已经在用：重点读第 3 章到第 5 章
- 如果你在搭团队工作流：重点读第 4 章、第 6 章和附录

## 你学完会得到什么

- 搞清 `command / agent / skill / memory / settings / MCP / hooks` 的分工
- 知道怎么从“会用一点”走到“能真正落地工作流”
- 知道哪些做法值得直接抄，哪些只是参考样例
- 知道如何避免把中文化做成“好看但跑不起来”的假仓库

# 第 1 章：先把 Claude Code 跑起来

## 目标

先让工具可用，不要一开始就被配置细节拖住。

## 你要做的三件事

- 安装 Claude Code
- 验证安装
- 完成第一次登录

## 推荐阅读

- `tutorial/day0/README.md`
- `tutorial/day0/mac.md`
- `tutorial/day0/linux.md`
- `tutorial/day0/windows.md`

## 最重要的提醒

- 第一天先别急着折腾 `.claude/`
- 先跑起来
- 先体验默认行为
- 再回来做结构化配置

# 第 2 章：先建立核心脑图

## Claude Code 最重要的 7 个概念

- `Command`：用户显式触发的工作流入口
- `Agent / Subagent`：独立上下文里的自治执行者
- `Skill`：可复用知识或动作单元
- `Memory`：Claude 在项目里如何持续记住东西
- `Settings`：权限、模型、输出风格、hooks、MCP 的运行时控制面
- `Hooks`：生命周期事件触发的外部逻辑
- `MCP`：把 Claude 接到外部工具和数据源的协议层

## 一句话判断

- 入口看 `command`
- 自治看 `agent`
- 复用看 `skill`
- 长期记忆看 `memory`
- 运行边界看 `settings`

## 推荐阅读

- `reports/claude-agent-command-skill.md`
- `best-practice/claude-subagents.md`
- `best-practice/claude-skills.md`
- `best-practice/claude-memory.md`
- `best-practice/claude-settings.md`

# 第 3 章：项目怎么从“聊天式使用”变成“工程化使用”

## 先从 `CLAUDE.md` 开始

它不是“给模型看的大作文”，而是项目工作手册。

你应该放进去的通常是：

- 项目结构
- 构建/测试命令
- 关键约定
- 路径提示

不应该塞进去的通常是：

- 冗长 API 文档
- 大量一次性细节
- 高频变化信息

## 接着拆 `rules`

当根 `CLAUDE.md` 快要变长、开始包含路径特化约束时，就应该拆到 `.claude/rules/`。

## 然后补 `skills`

真正高质量的 skill，不是“多”，而是“触发准、边界清、支持渐进式披露”。

## 推荐阅读

- `best-practice/claude-memory.md`
- `best-practice/claude-skills.md`
- `best-practice/claude-commands.md`
- `best-practice/claude-settings.md`

# 第 4 章：工作流是 Claude Code 真正拉开差距的地方

## 最小工作流样例

这个仓库最值得读的一条链路是：

- Command -> Agent -> Skill

它通过 weather 示例，展示了：

- 入口如何和用户交互
- agent 如何自治取数
- skill 如何把结果变成产物

## 更大的工作流

### RPI

- Research
- Plan
- Implement

适合不想一上来就乱写的人。

### Cross-model workflow

- Claude Code 负责 plan / implement
- Codex 负责 QA / verify

适合多模型协作场景。

### Agent teams

多个独立 agent 会话按角色协作，适合更复杂的团队式工作流。

## 推荐阅读

- `orchestration-workflow/orchestration-workflow.md`
- `implementation/claude-commands-implementation.md`
- `implementation/claude-skills-implementation.md`
- `implementation/claude-subagents-implementation.md`
- `development-workflows/cross-model-workflow/cross-model-workflow.md`
- `development-workflows/rpi/rpi-workflow.md`
- `agent-teams/agent-teams-prompt.md`

# 第 5 章：Claude Code 真正高频会卡住你的地方

## 1. 权限

太保守会慢，太激进会危险。

## 2. 上下文

不理解 context window，就很难稳定做长任务。

## 3. 模型和 effort

不是永远选最强，而是让模型和任务匹配。

## 4. MCP

不是越多越好，而是接高频、刚需、能明显降低幻觉的那几类。

## 5. hooks

hooks 很强，但也最容易把系统复杂度拉爆。

## 推荐阅读

- `best-practice/claude-settings.md`
- `best-practice/claude-mcp.md`
- `.claude/hooks/HOOKS-README.md`
- `.codex/hooks/HOOKS-README.md`

# 第 6 章：社区里最值得抄的经验

## Boris 路线

重点在：

- plan mode
- 多 worktree 并行
- 小 PR
- squash merge
- 把高频流程收进 command / skill / agent

## Thariq 路线

重点在：

- skill 的触发条件
- skill 的 supporting files
- 渐进式披露
- skill 的可组合性

## 推荐阅读

- `tips/README.md`
- `tips/claude-boris-13-tips-03-jan-26.md`
- `tips/claude-boris-10-tips-01-feb-26.md`
- `tips/claude-boris-12-tips-12-feb-26.md`
- `tips/claude-thariq-tips-17-mar-26.md`
- `videos/README.md`

# 第 7 章：这仓库哪些能直接抄，哪些不要直接抄

## 值得直接抄的

- 学习路径设计
- 术语分层
- `README` 的入口导航
- 工作流样例
- 运行保护机制
- 同步检查脚本

## 先别直接抄的

- 过度个性化的 spinner / status line
- 还没完全中文化的 presentation 细枝末节
- 某些被重编得过于简短的长文，如果你需要深度细节，请对照上游

## 一句话原则

先抄“结构和思路”，再抄“具体配置”。

# 第 8 章：给中文读者的 7 天学习路径

## Day 1

- 跑起来 Claude Code
- 完成第一次登录

## Day 2

- 看懂 `command / agent / skill`

## Day 3

- 看懂 `CLAUDE.md / memory / rules`

## Day 4

- 看懂 `settings / permissions / hooks / MCP`

## Day 5

- 把 weather workflow 读通

## Day 6

- 看 `tips` 和 `videos`

## Day 7

- 选一个你自己的项目，把一个高频动作做成 command、skill 或 agent

# 附录：按目标挑文档

## 我只想快速学会

- `tutorial/day0/README.md`
- `reports/claude-agent-command-skill.md`
- `best-practice/claude-subagents.md`
- `best-practice/claude-skills.md`

## 我想搭自己的团队工作流

- `best-practice/claude-settings.md`
- `best-practice/claude-mcp.md`
- `development-workflows/rpi/rpi-workflow.md`
- `development-workflows/cross-model-workflow/cross-model-workflow.md`

## 我想做传播和分享

- `presentation/index.html`
- `tips/README.md`
- `videos/README.md`

## 我想继续深挖

- `reports/README.md`
- `reports/zh-fork-review-scorecard.md`
- upstream 原仓：<https://github.com/shanraisshan/claude-code-best-practice>
