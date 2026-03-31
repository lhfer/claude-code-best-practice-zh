# Windows 安装

[返回 Day 0](README.md)

## 第 1 步：安装 Node.js

1. 打开 <https://nodejs.org>
2. 点击 **Download Node.js (LTS)**
3. 下载 `.msi`
4. 双击运行并按默认选项安装

## 第 2 步：验证 Node.js

打开新的 PowerShell 或 Windows Terminal：

```powershell
node --version
npm --version
```

## 第 3 步：安装 Claude Code

```powershell
npm install -g @anthropic-ai/claude-code
```

如果遇到权限问题，用管理员权限打开终端再试。

## 第 4 步：验证

```powershell
claude --version
```

装好后继续做登录和后续学习。
