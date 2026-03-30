为一个“迪拜时间 SVG 卡片”工作流创建一支 agent team。
这个工作流遵循 **Command → Agent → Skill** 架构：

- command 负责编排流程与用户交互
- agent 负责取实时数据
- skill 负责把结果渲染成可视化产物

**重要要求：**

- 所有文件都必须创建在 `agent-teams/.claude/` 内
- **不要**写到仓库根部的 `.claude/`
- 这样这个示例才能保持自包含，并且能通过 `cd agent-teams && claude` 独立运行
- **不要**直接复制现成 weather workflow，要从零搭建一条 time workflow

请分配这 3 个角色：

1. **Command Architect**
   - 负责 `agent-teams/.claude/commands/time-orchestrator.md`
   - 通过 Agent tool 调 `time-agent`
   - 再通过 Skill tool 调 `time-svg-creator`
   - frontmatter 使用 `model: haiku`
   - 明确写出：顺序执行、正确工具使用、最终输出摘要
   - 和其他角色对齐数据契约：`{time, timezone, formatted}`

2. **Agent Engineer**
   - 负责：
     - `agent-teams/.claude/agents/time-agent.md`
     - `agent-teams/.claude/skills/time-fetcher/SKILL.md`
   - 用 Bash 获取 Dubai 当前时间：
     `TZ='Asia/Dubai' date '+%Y-%m-%d %H:%M:%S %Z'`
   - 返回 `time`、`timezone`、`formatted`
   - frontmatter 使用：
     - `tools: Bash`
     - `model: haiku`
     - `color: blue`
     - `maxTurns: 3`
   - 通过 `skills:` 预加载 `time-fetcher`

3. **Skill Designer**
   - 负责：
     - `agent-teams/.claude/skills/time-svg-creator/SKILL.md`
     - `reference.md`
     - `examples.md`
   - 接收 `time`、`timezone`、`formatted`
   - 生成 `agent-teams/output/dubai-time.svg`
   - 生成 `agent-teams/output/output.md`
   - **只使用调用上下文提供的时间，不重新取数**

## 团队协作要求

- 三个角色都要通过共享任务清单同步数据契约
- 契约固定为：`{time, timezone, formatted}`
- 可以并行启动，因为三部分基本独立，只需要在接口上对齐
