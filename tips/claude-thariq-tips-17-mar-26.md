# Thariq：Anthropic 内部是怎么用 Skills 的

> 中文重编版
> 原始来源：
> - Thariq 原文：<https://x.com/trq212/status/2033949937936085378>
> - 上游整理：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-thariq-tips-17-mar-26.md>

## 这篇为什么重要

如果说 Boris 的内容更像“高频用户工作流”，那 Thariq 这篇更像：

> Anthropic 内部对 skill 这个能力边界的系统总结。

## 你最该记住的几个点

### 1. skill 不只是一个 markdown 文件

更准确地说，它是一个文件夹，可以带：

- 脚本
- 资产
- 示例
- 参考资料

### 2. skill description 是触发器，不是摘要

写 description 时，应该想的是：

- Claude 在什么场景下该触发它

而不是：

- 我想写一句多好看的简介

### 3. 好 skill 要做 progressive disclosure

不要把所有东西都塞进 `SKILL.md`。
主文件只保留高判断价值内容，重资料拆出去。

### 4. 要把 skill 当成可组合能力

不是一个 skill 解决所有问题，而是多个 skill 互相配合。

### 5. 要衡量 skill 是否真的被触发和被使用

做了 skill 不代表它真的在发挥作用。
触发率、误触发、没人用，都是要关心的。

## 对中文用户最实用的启发

- 别把 skill 做成“大而全说明书”
- 先解决触发条件，再解决内容完整度
- 能拆 supporting files 的，就不要都堆在主文件里

## 一句话总结

真正高级的 skill，不是写得最长，而是触发得准、边界清、能复用。
