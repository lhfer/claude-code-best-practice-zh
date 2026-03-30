# Linux 安装

[返回 Day 0](README.md)

## 你需要什么

- `Node.js v18+`
- `npm`

## 推荐装法：走 Node 官方页面

最省心的方式是打开：

- <https://nodejs.org/en/download>

然后选择：

- `Linux`
- `fnm`
- `npm`
- 默认 LTS 版本

页面给出的命令通常类似这样：

```bash
curl -fsSL https://fnm.vercel.app/install | bash
source ~/.bashrc   # 或 source ~/.zshrc
fnm install 24
```

> 具体版本号以网页显示为准。

## 装完后验证 Node

```bash
node --version
npm --version
```

## 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

## 验证 Claude Code

```bash
claude --version
```

## 常见问题

- 如果 `claude` 找不到，先检查 npm 全局 bin 是否在 `PATH` 里
- 如果用系统包管理器装的 Node 太旧，换回官方 LTS 路线
- 在 WSL 里也可以按这份流程走
