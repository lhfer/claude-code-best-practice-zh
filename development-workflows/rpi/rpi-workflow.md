# RPI Workflow

**RPI** = **R**esearch → **P**lan → **I**mplement

这条 workflow 的核心思想很朴素：

> 不要在需求还没想清楚时就开始写。

它把事情拆成 3 个阶段，每个阶段都有明确产物和验证门槛。

## 为什么值得学

RPI 最有价值的地方不是目录结构，而是阶段边界：

- 先研究能不能做
- 再规划怎么做
- 最后实现

这样能大幅降低下面这类浪费：

- 写到一半推倒重来
- UI 和后端各写各的
- 实现完才发现验收标准没定义

## 流程图

![RPI Workflow](rpi-workflow.svg)

## 目录结构

```text
rpi/{feature-slug}/
├── REQUEST.md
├── research/RESEARCH.md
├── plan/PLAN.md
├── plan/pm.md
├── plan/ux.md
├── plan/eng.md
└── implement/IMPLEMENT.md
```

## 三个阶段分别做什么

### Research

- 判断需求是否可行
- 判断是否值得做
- 先识别约束和风险

### Plan

- 把产品、体验、工程拆开
- 形成可执行的阶段计划

### Implement

- 按阶段落地
- 每阶段都要过验证

## 适合谁

- 需求不是一次性小修补
- 团队需要可追踪的中间产物
- 不想继续靠“边写边想”推进复杂功能

## 对中文团队最有价值的启发

- 先把 plan 变成工件，再让模型写代码
- 研究、规划、实现的职责不要混
- workflow 的价值不在“命令名”，而在“阶段门槛”
