# Skills in Large Monorepos

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-skills-for-larger-mono-repos.md>

## 先讲结论

在 monorepo 里，skill 最重要的不是“多”，而是“放对地方”。

上游这篇报告最有价值的一点，是把 skill discovery 说清楚了：

- 根目录 skill 负责共享能力
- 子目录 skill 负责局部能力
- Claude 会按你正在操作的目录动态发现它们

## 为什么这件事重要

因为 monorepo 最怕两种极端：

- 所有 skill 都堆在根目录，最后谁都不想看
- 每个 package 各写各的，没人知道从哪触发

## 实用建议

### 根目录 skill

适合放：

- 仓库通用规范
- 通用交付格式
- 共用的 review / explain / release 流程

### 子目录 skill

适合放：

- 某个 package 的框架约束
- 某个模块特有的工具链说明
- 与该目录强绑定的流程知识

## 这跟 `CLAUDE.md` 的区别

很多人会把 skill 和 memory 混成一回事。

更实用的区分：

- `CLAUDE.md` 解决“这里的通用工作方式是什么”
- skill 解决“遇到这种任务时，Claude 应该调用哪套知识或动作”

一个偏长期记忆，一个偏可调用能力。

## 中文团队怎么抄

如果你的仓库是 monorepo，第一版建议：

- 根目录保留少量高价值 skill
- 每个业务大目录只给 1 到 2 个 skill
- 先让触发条件写清楚，再扩数量

## 一句话判断

monorepo 里的好 skill 体系，不是铺满目录树，而是让 Claude 在正确的位置发现正确的 skill。
