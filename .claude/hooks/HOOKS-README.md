# Hooks（Claude Code）

这个目录保存的是 Claude Code hooks 的说明、配置和声音素材。

要先分清两层：

- `HOOKS-README.md` 是说明层，可以中文化
- `config/`、`scripts/`、`sounds/` 是运行时层，不要为了翻译去乱改

## hooks 是什么

hooks 可以理解成：

> Claude Code 在某些生命周期事件发生时，顺手去跑一段外部逻辑。

常见用途：

- 播放提示音
- 记日志
- 自动格式化
- 在 session 开始或结束时做额外动作
- 对某些风险操作做保护

## 这个仓库的实现方式

这里用的是“单入口脚本 + 配置开关”的组织法：

- 入口脚本：`.claude/hooks/scripts/hooks.py`
- 配置文件：`.claude/hooks/config/hooks-config.json`
- 资源目录：`.claude/hooks/sounds/`
- 触发接入：`.claude/settings.json`

这套结构的优点是：

- 逻辑集中
- 配置集中
- 事件和声音资源统一管理

## 最值得先理解的几个事件

| Hook | 什么时候触发 |
|---|---|
| `PreToolUse` | 调工具前 |
| `PostToolUse` | 工具成功后 |
| `PostToolUseFailure` | 工具失败后 |
| `PermissionRequest` | 需要授权时 |
| `SessionStart` | 会话开始时 |
| `Stop` | Claude 回合结束时 |
| `SubagentStart` | 子 agent 启动时 |
| `SubagentStop` | 子 agent 结束时 |

完整事件列表请看官方：

- <https://code.claude.com/docs/en/hooks>

## 怎么执行

在这个仓里，hooks 通过 Python 入口脚本执行：

```json
{
  "type": "command",
  "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py"
}
```

## 怎么关掉

### 全部关掉

在 `.claude/settings.local.json` 里写：

```json
{
  "disableAllHooks": true
}
```

### 单独关某个 hook

改：

- `.claude/hooks/config/hooks-config.json`
- 或你自己的 `.claude/hooks/config/hooks-config.local.json`

## 对中文团队最重要的提醒

- hooks 很强，但也是最容易把仓库复杂度拉高的一层
- 第一版只接高价值事件
- 不要因为事件多，就全部挂上

## 相关文件

- 配置：`config/hooks-config.json`
- 脚本：`scripts/hooks.py`
- 资源：`sounds/`
  "disableSubagentStartHook": false,
  "disableSubagentStopHook": false,
  "disablePreCompactHook": false,
  "disablePostCompactHook": false,
  "disableElicitationHook": false,
  "disableElicitationResultHook": false,
  "disableSessionStartHook": false,
  "disableSessionEndHook": false,
  "disableSetupHook": false,
  "disableTeammateIdleHook": false,
  "disableTaskCompletedHook": false,
  "disableConfigChangeHook": false,
  "disableWorktreeCreateHook": false,
  "disableWorktreeRemoveHook": false,
  "disableInstructionsLoadedHook": false
}
```

**Configuration Options:**
- `disableLogging`: Set to `true` to disable logging hook events to `.claude/hooks/logs/hooks-log.jsonl` (useful to prevent log file growth)

#### Local Configuration (Personal Overrides)

Create or edit `.claude/hooks/config/hooks-config.local.json` for personal preferences:

```json
{
  "disableLogging": true,
  "disablePostToolUseHook": true,
  "disableSessionStartHook": true
}
```

In this example, logging is disabled, and the PostToolUse and SessionStart hooks are overridden locally. All other hooks will use the shared configuration values.

**Note:** Individual hook toggles are checked by the hook script (`.claude/hooks/scripts/hooks.py`). Local settings override shared settings, and if a hook is disabled, the script exits silently without playing any sounds or executing hook logic.

### Text to Speech (TTS)
website used to generate sounds: https://elevenlabs.io/
voice used: Samara X

## Agent Frontmatter Hooks

Claude Code 2.1.0 introduced support for agent-specific hooks defined in agent frontmatter files. These hooks only run within the agent's lifecycle and support a subset of hook events.

### Supported Agent Hooks

Agent frontmatter hooks support **6 hooks** (not all 16). The changelog originally mentioned only 3, but testing confirms 6 hooks actually fire in agent sessions:
- `PreToolUse`: Runs before the agent uses a tool
- `PostToolUse`: Runs after the agent completes a tool use
- `PermissionRequest`: Runs when a tool requires user permission
- `PostToolUseFailure`: Runs after a tool call fails
- `Stop`: Runs when the agent finishes
- `SubagentStop`: Runs when a subagent completes

> **Note:** The [v2.1.0 changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#210) only mentions 3 hooks: *"Added hooks support to agent frontmatter, allowing agents to define PreToolUse, PostToolUse, and Stop hooks scoped to the agent's lifecycle"*. However, testing with the `claude-code-voice-hook-agent` confirms that 6 hooks actually fire in agent sessions. The remaining 10 hooks (e.g., Notification, SessionStart, SessionEnd, etc.) do not fire in agent contexts.
>
> **Update (Feb 2026):** The [official hooks reference](https://code.claude.com/docs/en/hooks) now states *"All hook events are supported"* for skill/agent frontmatter hooks. This may mean support has expanded beyond the 6 hooks originally tested. Re-testing recommended to verify if additional hooks now fire in agent sessions.

### Agent Sound Folders

Agent-specific sounds are stored in separate folders:
- `.claude/hooks/sounds/agent_pretooluse/`
- `.claude/hooks/sounds/agent_posttooluse/`
- `.claude/hooks/sounds/agent_permissionrequest/`
- `.claude/hooks/sounds/agent_posttoolusefailure/`
- `.claude/hooks/sounds/agent_stop/`
- `.claude/hooks/sounds/agent_subagentstop/`

### Creating an Agent with Hooks

1. Create an agent definition file in `.claude/agents/`:

```markdown
---
name: my-agent
description: Description of what this agent does
hooks:
  PreToolUse:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PreToolUse
  PostToolUse:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PostToolUse
  PermissionRequest:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PermissionRequest
  PostToolUseFailure:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: PostToolUseFailure
  Stop:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: Stop
  SubagentStop:
    - type: command
      command: python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py --agent=my-agent
      timeout: 5000
      async: true
      statusMessage: SubagentStop
---

Your agent instructions here...
```

2. Add sound files to the agent sound folders:
   - `agent_pretooluse/agent_pretooluse.wav`
   - `agent_posttooluse/agent_posttooluse.wav`
   - `agent_permissionrequest/agent_permissionrequest.wav`
   - `agent_posttoolusefailure/agent_posttoolusefailure.wav`
   - `agent_stop/agent_stop.wav`
   - `agent_subagentstop/agent_subagentstop.wav`

### Example: Weather Fetcher Agent

See `.claude/agents/claude-code-voice-hook-agent.md` for a complete example of an agent with hooks configured.

### Hook Option: `once: true`

The `once: true` option ensures a hook only runs once per session:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "once": true
}
```

This is useful for hooks like `SessionStart`, `SessionEnd`, and `PreCompact` that should only trigger once.

> **Note:** The `once` option is for **skills only, not agents**. It works in settings-based hooks and skill frontmatter, but is not supported in agent frontmatter hooks.

### Hook Option: `async: true`

Hooks can run in the background without blocking Claude Code's execution by adding `"async": true`:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true
}
```

**When to use async hooks:**
- Logging and analytics
- Notifications and sound effects
- Any side-effect that shouldn't slow down Claude Code

This project uses `async: true` for all hooks since voice notifications are side-effects that don't need to block execution. The `timeout` specifies how long the async hook can run before being terminated.

### Hook Option: `statusMessage`

The `statusMessage` field sets a custom spinner message displayed to the user while the hook is running:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true,
  "statusMessage": "PreToolUse"
}
```

This project sets `statusMessage` to the hook event name on all hooks, so the spinner briefly shows which hook is firing (e.g., "PreToolUse", "SessionStart", "Stop"). This is most visible for synchronous hooks; for async hooks the message flashes briefly before the hook runs in the background.

## Hook Types

Claude Code supports four hook handler types. This project uses `command` hooks for all sound playback.

### `type: "command"` (used by this project)

Runs a shell command. Receives JSON input via stdin, communicates results through exit codes and stdout.

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/scripts/hooks.py",
  "timeout": 5000,
  "async": true
}
```

### `type: "prompt"`

Sends a prompt to a Claude model for single-turn evaluation. The model returns a yes/no decision as JSON (`{"ok": true/false, "reason": "..."}`). Useful for decisions that require judgment rather than deterministic rules.

```json
{
  "type": "prompt",
  "prompt": "Check if all tasks are complete. $ARGUMENTS",
  "timeout": 30
}
```

**Supported events:** PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, UserPromptSubmit, Stop, SubagentStop, TaskCompleted. **Command-only events (not supported for prompt/agent types):** ConfigChange, Elicitation, ElicitationResult, InstructionsLoaded, Notification, PostCompact, PreCompact, SessionEnd, SessionStart, Setup, SubagentStart, TeammateIdle, WorktreeCreate, WorktreeRemove.

### `type: "agent"`

Spawns a subagent with multi-turn tool access (Read, Grep, Glob) to verify conditions before returning a decision. Same response format as prompt hooks. Useful when verification requires inspecting actual files or test output.

```json
{
  "type": "agent",
  "prompt": "Verify that all unit tests pass. $ARGUMENTS",
  "timeout": 120
}
```

### `type: "http"` (since v2.1.63)

POSTs JSON to a URL and receives a JSON response, instead of running a shell command. Useful for integrating with external services or webhooks. HTTP hooks are routed through the sandbox network proxy when sandboxing is enabled.

```json
{
  "type": "http",
  "url": "http://localhost:8080/hooks/pre-tool-use",
  "timeout": 30,
  "headers": {
    "Authorization": "Bearer $MY_TOKEN"
  },
  "allowedEnvVars": ["MY_TOKEN"]
}
```

**Not supported for:** ConfigChange, Elicitation, ElicitationResult, InstructionsLoaded, Notification, PostCompact, PreCompact, SessionEnd, SessionStart, Setup, SubagentStart, TeammateIdle, WorktreeCreate, WorktreeRemove (command-only events). Headers support environment variable interpolation with `$VAR_NAME`, but only for variables explicitly listed in `allowedEnvVars`.

## Environment Variables

Claude Code provides these environment variables to hook scripts:

| Variable | Availability | Description |
|----------|-------------|-------------|
| `$CLAUDE_PROJECT_DIR` | All hooks | Project root directory. Wrap in quotes for paths with spaces |
| `$CLAUDE_ENV_FILE` | SessionStart only | File path for persisting environment variables for subsequent Bash commands. Use append (`>>`) to preserve variables from other hooks |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Plugin's root directory, for scripts bundled with a plugin |
| `$CLAUDE_CODE_REMOTE` | All hooks | Set to `"true"` in remote web environments, not set in local CLI |
| `${CLAUDE_SKILL_DIR}` | Skill hooks | Skill's own directory, for scripts bundled with a skill (since v2.1.69) |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | Override SessionEnd hook timeout in milliseconds. Prior to v2.1.74, SessionEnd hooks were killed after 1.5s regardless of configured `timeout`. Now respects the hook's `timeout` value, or this env var if set (since v2.1.74) |
| `session_id` (via stdin JSON) | All hooks | Current session ID, received as part of the JSON input on stdin (not an environment variable) |

### Common Input Fields (stdin JSON)

Every hook receives a JSON object on stdin containing these common fields, in addition to any hook-specific fields listed in the Options column above:

| Field | Type | Description |
|-------|------|-------------|
| `hook_event_name` | string | Name of the hook event that fired (e.g., `"PreToolUse"`, `"Stop"`) |
| `session_id` | string | Current session identifier |
| `transcript_path` | string | Path to the conversation transcript JSON file |
| `cwd` | string | Current working directory |
| `permission_mode` | string | Current permission mode: `default`, `plan`, `acceptEdits`, `dontAsk`, or `bypassPermissions` |
| `agent_id` | string | Unique subagent identifier. Present when the hook fires inside a subagent context (since v2.1.69) |
| `agent_type` | string | Agent type name (e.g. `Bash`, `Explore`, `Plan`, or custom). Present when using `--agent <name>` flag or inside a subagent (since v2.1.69) |

> **Note:** Hook-specific fields (e.g., `tool_name` for PreToolUse, `last_assistant_message` for Stop) are listed in the Options column of the [Hook Events Overview](#hook-events-overview---official-19-hooks) table above.

## Hooks Management Commands

Claude Code provides built-in commands for managing hooks:

- **`/hooks`** — Interactive hook management UI. View, add, and delete hooks without editing JSON files. Hooks are labeled by source: `[User]`, `[Project]`, `[Local]`, `[Plugin]`. You can also toggle `disableAllHooks` from this menu.
- **`claude hooks reload`** — Reload hooks configuration without restarting the session. Useful after editing settings files (since v2.0.47).

## MCP Tool Matchers

For `PreToolUse`, `PostToolUse`, and `PermissionRequest` hooks, you can match MCP (Model Context Protocol) tools using the pattern `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "mcp__memory__.*",
      "hooks": [{ "type": "command", "command": "echo 'MCP memory tool used'" }]
    }]
  }
}
```

Full regex is supported: `mcp__memory__.*` (all tools from memory server), `mcp__.*__write.*` (any write tool from any server).

### Per-Hook Matcher Reference

Matchers filter which events trigger a hook. Not all hooks support matchers — hooks without matcher support always fire.

| Hook | Matcher Field | Possible Values | Example |
|------|--------------|-----------------|---------|
| `PreToolUse` | `tool_name` | Any tool name: `Bash`, `Read`, `Edit`, `Write`, `Glob`, `Grep`, `mcp__*` | `"matcher": "Bash"` |
| `PermissionRequest` | `tool_name` | Same as PreToolUse | `"matcher": "mcp__memory__.*"` |
| `PostToolUse` | `tool_name` | Same as PreToolUse | `"matcher": "Write"` |
| `PostToolUseFailure` | `tool_name` | Same as PreToolUse | `"matcher": "Bash"` |
| `Notification` | `notification_type` | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` | `"matcher": "permission_prompt"` |
| `SubagentStart` | `agent_type` | `Bash`, `Explore`, `Plan`, or custom agent name | `"matcher": "Bash"` |
| `SubagentStop` | `agent_type` | `Bash`, `Explore`, `Plan`, or custom agent name | `"matcher": "Bash"` |
| `SessionStart` | `source` | `startup`, `resume`, `clear`, `compact` | `"matcher": "startup"` |
| `SessionEnd` | `reason` | `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other` | `"matcher": "logout"` |
| `PreCompact` | `trigger` | `manual`, `auto` | `"matcher": "auto"` |
| `PostCompact` | `trigger` | `manual`, `auto` | `"matcher": "manual"` |
| `Elicitation` | `mcp_server_name` | MCP server name | `"matcher": "my-mcp-server"` |
| `ElicitationResult` | `mcp_server_name` | MCP server name | `"matcher": "my-mcp-server"` |
| `ConfigChange` | `source` | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` | `"matcher": "project_settings"` |
| `UserPromptSubmit` | — | No matcher support | Always fires |
| `Stop` | — | No matcher support | Always fires |
| `TeammateIdle` | — | No matcher support | Always fires |
| `TaskCompleted` | — | No matcher support | Always fires |
| `WorktreeCreate` | — | No matcher support | Always fires |
| `WorktreeRemove` | — | No matcher support | Always fires |
| `InstructionsLoaded` | — | No matcher support | Always fires |
| `Setup` | — | No matcher support | Always fires |

## Known Issues & Workarounds

### Agent Stop Hook Bug (SubagentStop vs Stop)

**Bug Report:** [GitHub Issue #19220](https://github.com/anthropics/claude-code/issues/19220)

**Issue:** When defining a `Stop` hook in an agent's frontmatter, the `hook_event_name` passed to the hook script is `"SubagentStop"` instead of `"Stop"`. This contradicts the official documentation and breaks consistency with other agent hooks (`PreToolUse` and `PostToolUse`), which correctly pass their configured names.

| Hook | Defined As | Received As | Status |
|------|------------|-------------|--------|
| PreToolUse | `PreToolUse:` | `"PreToolUse"` | ✅ Correct |
| PostToolUse | `PostToolUse:` | `"PostToolUse"` | ✅ Correct |
| Stop | `Stop:` | `"SubagentStop"` | ❌ Inconsistent |

**Status:** The [official hooks reference](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents) now documents this as expected behavior: *"For subagents, Stop hooks are automatically converted to SubagentStop since that is the event that fires when a subagent completes."* This project handles it via the `AGENT_HOOK_SOUND_MAP` in `hooks.py`, which has a separate `SubagentStop` entry that maps to the `agent_subagentstop` sound folder.

### PreToolUse Decision Control Deprecation

The `PreToolUse` hook previously used top-level `decision` and `reason` fields for blocking tool calls. These are now **deprecated**. Use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason` instead:

| Deprecated | Current |
|-----------|---------|
| `"decision": "approve"` | `"hookSpecificOutput": { "permissionDecision": "allow" }` |
| `"decision": "block"` | `"hookSpecificOutput": { "permissionDecision": "deny" }` |

This does not affect this project since `hooks.py` uses async sound playback and does not use decision control.

## Decision Control Patterns

Different hooks use different output schemas for blocking or controlling execution. This project does not use decision control (all hooks are async sound playback), but for reference:

| Hook(s) | Control Method | Values |
|---------|---------------|--------|
| PreToolUse | `hookSpecificOutput.permissionDecision` | `allow`, `deny`, `ask` |
| PreToolUse | `hookSpecificOutput.autoAllow` | `true` — auto-approve future uses of this tool (since v2.0.76) |
| PermissionRequest | `hookSpecificOutput.decision.behavior` | `allow`, `deny` |
| PostToolUse, PostToolUseFailure, Stop, SubagentStop, ConfigChange | Top-level `decision` | `block` |
| TeammateIdle, TaskCompleted | `continue` + exit code 2 | `{"continue": false, "stopReason": "..."}` — JSON decision control added in v2.1.70 |
| UserPromptSubmit | Can modify `prompt` field | Returns modified prompt via stdout |
| WorktreeCreate | Non-zero exit + stdout path | Non-zero exit fails creation; stdout provides worktree path |
| Elicitation | `hookSpecificOutput.action` + `hookSpecificOutput.content` | `accept`, `decline`, `cancel` — control MCP elicitation response |
| ElicitationResult | `hookSpecificOutput.action` + `hookSpecificOutput.content` | `accept`, `decline`, `cancel` — override user response before sending to server |

### Universal JSON Output Fields

All hooks can return these fields via stdout JSON:

| Field | Type | Description |
|-------|------|-------------|
| `continue` | bool | If `false`, stops Claude entirely |
| `stopReason` | string | Message shown when `continue` is false |
| `suppressOutput` | bool | Hides stdout from verbose mode |
| `systemMessage` | string | Warning message shown to user |
| `additionalContext` | string | Context added to Claude's conversation |

## Hook Deduplication & External Changes

- **Hook deduplication:** Identical hook handlers defined in multiple settings locations run only once in parallel, preventing duplicate execution.
- **External change detection:** Claude Code warns when hooks are modified externally (e.g., by another process editing settings files) during an active session.
