# Hooks（Codex CLI）

这个目录是 Codex CLI hooks 的说明和资源层。

和 `.claude/hooks/` 一样，也要先分清两层：

- `HOOKS-README.md` 是说明层，可以中文化
- `config/`、`scripts/`、`sounds/` 是运行时层，不要乱改

## Codex 这边有几个 hook

当前主要是 3 个：

| Hook | 配置来源 | 作用 |
|---|---|---|
| `agent-turn-complete` | `config.toml` | agent 回合完成后触发 |
| `SessionStart` | `hooks.json` | 会话开始时注入上下文并播放声音 |
| `Stop` | `hooks.json` | 会话结束时触发 |

## 和 Claude Code 的区别

Codex hooks 明显更轻：

- 事件更少
- 配置更简单
- 更适合做轻量提示和上下文注入

## 运行方式

### `agent-turn-complete`

通过 `config.toml` 注册：

```toml
notify = ["python3", ".codex/hooks/scripts/hooks.py"]
```

### `SessionStart` / `Stop`

通过 `hooks.json` 注册：

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "python3 .codex/hooks/scripts/hooks.py --hook SessionStart"
      }
    ],
    "Stop": [
      {
        "command": "python3 .codex/hooks/scripts/hooks.py --hook Stop"
      }
    ]
  }
}
```

## 有什么用

- 会话开始时注入一点上下文
- 回合结束时给清晰反馈
- 让 Codex 和 Claude 的使用体验更接近

## 相关文件

- `config.toml`
- `hooks.json`
- `config/hooks-config.json`
- `scripts/hooks.py`
- `disableStopHook`: Set to `true` to disable the session stop sound
- `disableLogging`: Set to `true` to disable logging hook events to `.codex/hooks/logs/hooks-log.jsonl`

### Configuration Fallback

There are two configuration files:

1. **`.codex/hooks/config/hooks-config.json`** - The shared/default configuration that is committed to git
2. **`.codex/hooks/config/hooks-config.local.json`** - Your personal overrides (git-ignored)

The local config file (`.local.json`) takes precedence over the shared config, allowing each developer to customize their hook behavior without affecting the team.

#### Local Configuration (Personal Overrides)

Create or edit `.codex/hooks/config/hooks-config.local.json` for personal preferences:

```json
{
  "disableAgentTurnCompleteHook": true,
  "disableSessionStartHook": false,
  "disableStopHook": true,
  "disableLogging": true
}
```

### Logging

When logging is enabled (`"disableLogging": false`), hook events are logged to `.codex/hooks/logs/hooks-log.jsonl` in JSON Lines format. Each entry contains the full JSON payload received from Codex CLI.

## Testing

Run the test suite:
```bash
python3 -m unittest tests.test_hooks -v
```

## Future Extensibility

This project can be extended by:

1. Adding new entries to `HOOK_SOUND_MAP` in `hooks.py`
2. Adding corresponding sound files in `.codex/hooks/sounds/`
3. Adding toggle keys in `hooks-config.json`
4. Adding new hook entries in `hooks.json`
