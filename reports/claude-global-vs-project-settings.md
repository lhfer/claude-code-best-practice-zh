# Global vs Project Settings

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-global-vs-project-settings.md>

## 这篇报告回答一个关键问题

到底哪些东西应该放：

- `~/.claude/`
- 项目里的 `.claude/`
- 根目录的 `CLAUDE.md`
- 本地 `settings.local.json`

如果这一层搞不清，Claude Code 很容易被你自己配乱。

## 最简单的判断标准

### 放全局

当它属于：

- 你个人的长期习惯
- 跨项目通用偏好
- 不该进 git 的个人配置

### 放项目级

当它属于：

- 这个仓库的团队协作规则
- 这个项目共享的 hooks / settings / commands / skills
- 应该被版本控制追踪的配置

## 这个仓库为什么值得看

因为它不只是把 `.claude/` 当配置目录，而是把“全局和项目级的边界”当成一个必须单独讲清楚的主题。

这对中文团队尤其重要，因为最常见的混乱就是：

- 团队约束放进个人全局目录
- 个人偏好误提交进项目仓
- 想做项目级共享，结果改成了自己机器上的局部配置

## 你先记住这几条就够了

- `settings.local.json` 更像“我自己的项目内覆盖”
- `settings.json` 更像“团队共享默认值”
- `CLAUDE.md` 更像“项目级工作记忆”
- `~/.claude/` 更像“我的个人底座”

## 对中文 fork 的意义

这份中文仓也采用同样逻辑：

- 中文说明文档进仓
- 运行层配置保留英文
- 本地 `upstream` remote 是本地工作习惯，不是仓库文件
- 同步状态通过 [SYNC_STATUS.md](../SYNC_STATUS.md) 记录，而不是靠口头约定

## 一句话判断

凡是“团队应该一起看到、一起维护、一起同步”的，优先放项目级。
凡是“只是你自己想这么用”的，优先放全局或 local。
