# macOS 安装

[返回 Day 0](README.md)

## 第 1 步：打开 Terminal

- 按 `Cmd + Space`
- 输入 `Terminal`
- 回车

## 第 2 步：确认 Homebrew

```bash
brew --version
```

如果提示 `command not found`，先安装 Homebrew：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 第 3 步：安装 Claude Code

```bash
brew install --cask claude-code
```

## 第 4 步：验证

```bash
claude --version
```

装好后回到 [README.md](README.md) 继续做登录和后续学习。
