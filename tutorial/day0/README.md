# Day 0 — 第一天把 Claude Code 跑起来

这篇只做一件事：

> 带你把 Claude Code 安装好、验证好、能真正开始用。

## 第 1 步：按系统安装

请选择你的系统：

| 系统 | 指南 |
|----|-------|
| Windows | [windows.md](windows.md) |
| Linux | [linux.md](linux.md) |
| macOS | [mac.md](mac.md) |

装完后继续下一步。

---

## 第 2 步：验证安装

```bash
node --version
claude --version
```

你希望看到的是：

- `node --version` 至少是 `v18.x`
- `claude --version` 能正常返回版本号

---

## 第 3 步：第一次登录

<img src="assets/login.png" alt="Claude Code login screen" width="50%">

第一次运行：

```bash
claude
```

Claude Code 会让你选择登录方式。

### 方式 1：订阅账号

- 选择 **Claude.ai account**
- 浏览器会打开授权页
- 登录并授权
- 回到终端即可

### 方式 2：API Key

如果你的团队管理员已经邀请你，或者你自己有 key：

- 选择 **Anthropic API Key**
- 粘贴 `sk-ant-` 开头的 key
- 之后 Claude Code 会记住它

## 新手提醒

- 第一天先别急着折腾 `.claude/`
- 先把工具跑起来
- 先感受一轮默认体验
- 再继续读更系统的内容

---
