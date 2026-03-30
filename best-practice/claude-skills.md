# Skills Best Practice

> 中文重编版
> 上游原文：<https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-skills.md>

## 先讲人话

skill 是 Claude Code 里最容易被低估、也最容易被用错的东西。

最简单的理解：

- command 更像“用户手动点火”的流程入口
- agent 更像“丢出去独立干活”的子线程
- skill 更像“Claude 随身带着的一段知识或一套可复用动作”

它不一定很重，但可以非常高频。

## skill 最强的地方

- Claude 可以按语义自动触发
- 你可以手动 `/skill-name`
- agent 可以预加载它
- 它可以带 supporting files
- 必要时可以 `context: fork`，把 skill 运行在子 agent 里

这几个特性叠在一起，skill 就从“提示词模板”升级成了“可复用能力单元”。

## 什么时候该用

- 你经常要重复解释同一类约束或流程
- 你想让 Claude 在合适的时候自动想到某件事
- 你有大段参考资料，不想每次都塞进主 prompt
- 你要给某个 agent 预装一套领域知识

## 这个仓库最值得抄的 skill 组织法

这个仓库的 weather 相关 skill 用的是很漂亮的一种结构：

```text
my-skill/
├── SKILL.md
├── reference.md
└── examples.md
```

为什么这套结构好：

- `SKILL.md` 保持短、聚焦、可读
- 细节放到 `reference.md`
- 预期输入输出放到 `examples.md`

这就是官方文档提到的 progressive disclosure 思路，用中文说就是：

> 主文件只放最有判断价值的东西，重资料按需再看。

## 两类 skill，要分清

### 1. 作为“知识注入”的 skill

这类 skill 更像：

- 规范
- 风格
- 领域知识
- 约束集合

Claude 自动触发它时，重点是“知道什么”。

### 2. 作为“动作单元”的 skill

这类 skill 更像：

- 部署步骤
- 生成某类产物
- 运行固定检查
- 整理某种输出

重点是“要怎么做”。

这个仓库里的 `weather-fetcher` 更偏知识注入，`weather-svg-creator` 更偏动作单元。

## 常见误区

### 误区 1：skill 就是短 prompt

不对。
真正高质量的 skill，应该明确：

- 什么时候触发
- 做到什么算完成
- 哪些资料要按需加载
- 哪些行为不要做

### 误区 2：把所有细节都塞进 SKILL.md

结果就是：

- skill 自己越来越重
- Claude 每次都吃一大段上下文
- 真正重要的判断信息反而被淹掉

### 误区 3：description 写成标题，而不是触发器

description 最重要的作用不是“给人看简介”，而是告诉 Claude：

> 什么场景下该调用我

## 面向中文用户的实战建议

如果你刚开始做 skill，第一批建议从这 3 类做起：

1. `explain-code`
2. `project-conventions`
3. `deliverable-writer`

先训练 Claude 在你常见的中文协作语境里表现更稳定，再考虑更重的 skill。

## 一句话判断

如果你想让 Claude 在很多地方都“自然想起同一套知识或动作”，skill 往往是最划算的抽象。
