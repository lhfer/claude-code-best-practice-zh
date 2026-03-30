# 中文 Fork 双角色审查与评分

基于 `2026-03-31` 的当前工作树，对 `lhfer/claude-code-best-practice-zh` 相对 upstream `shanraisshan/claude-code-best-practice` 的状态做一次双角色审查。

## A. 当前完成度快照

### 事实基线

- 本地 `HEAD`：`17e9ad53e31f0378ed197e3581af6eda012682f2`
- `upstream/main`：`7cde3f3232817c781b8ba0fd39cb2d707fd547c7`
- `ahead = 8`
- `behind = 0`

### 当前已完成到哪一层

| 层级 | 当前状态 |
|---|---|
| 首页入口层 | 已完成中文主入口，含学习路径、同步说明、校验入口 |
| 核心知识层 | `best-practice` 核心文档已基本中文化 |
| 解释报告层 | `reports` 已有中文入口，长文已完成一轮重编 |
| 样例实现层 | `implementation` 和 `orchestration-workflow` 已基本中文化 |
| 社区内容层 | `tips`、`videos`、`tutorial`、`development-workflows` 已有中文导读 |
| 演示传播层 | `presentation/index.html` 已从“关键标题中文”推进到“大部分讲述路径中文” |
| 维护治理层 | `CONTRIBUTING.md`、`LOCALIZATION_POLICY.md`、`GLOSSARY.md`、`SYNC_STATUS.md`、issue/PR 模板已建立 |
| 运行时保护层 | `PROTECTED_RUNTIME_PATHS.txt`、`scripts/validate_localization.py`、`scripts/check_upstream_sync.py` 已建立 |

### 运行安全判定

**通过。**

证据：

- `python3 scripts/validate_localization.py` 通过
- `python3 scripts/check_upstream_sync.py` 通过
- `behind = 0`
- 相对 upstream 的 `.claude/`、`.codex/`、`.mcp.json` 实际变更只落在 docs-only 文件：
  - `.claude/hooks/HOOKS-README.md`
  - `.codex/hooks/HOOKS-README.md`

结论：目前没有发现“因为中文化导致原仓执行层功能失效”的证据。

## B. 双角色评分表

## 总分

**82 / 100**

- GitHub 老开发者视角：**43 / 50**
- Claude 初学者视角：**39 / 50**
- 安全门槛：**通过**

### 1. GitHub 老开发者视角（43 / 50）

| 维度 | 分数 | 给分理由 |
|---|---:|---|
| 仓库首屏与定位 | 9/10 | 首页能快速讲清仓库是什么、和 upstream 的关系、为什么不是机翻仓 |
| 信息架构与导航 | 9/10 | README 已形成概念层、实现层、社区层、报告层的清晰入口 |
| 维护姿态 | 10/10 | upstream、license、sync 状态、贡献规则、issue/PR 模板、保护脚本都齐了 |
| 本土化质量 | 8/10 | 大部分内容已是重编，不是机翻；但部分长文压缩过猛，导致信息密度不如 upstream |
| 演示与传播层 | 7/10 | `tips`、`videos`、`presentation` 已有明显成型感，但 `presentation/index.html` 仍留有不少英文暴露点 |

### 2. Claude 初学者视角（39 / 50）

| 维度 | 分数 | 给分理由 |
|---|---:|---|
| 学习入口 | 9/10 | README 和 `tutorial/README.md` 已形成明确起点 |
| 术语解释 | 8/10 | 大部分核心术语都先讲了人话，再给英文术语 |
| 概念边界 | 8/10 | `best-practice` + `reports` 的组合已经能分清 command/agent/skill、memory/settings 等边界 |
| 学习路径连续性 | 8/10 | 从 README 走向 tutorial / reports / workflows / tips / videos 的路径是连贯的 |
| 阅读体验 | 6/10 | Markdown 主体已很自然，但 presentation 还存在较多中英混排，部分压缩过头的长文会让初学者少掉细节上下文 |

## C. 与 upstream 的关键差异

### 成功的重编

- **首页入口更适合中文用户**
  - 相比 upstream 的强展示型 README，中文版首页更像学习入口页。
- **治理层明显增强**
  - upstream 没有中文本土化治理；fork 新增了术语表、保护清单、同步状态和校验脚本。
- **社区内容更容易收藏传播**
  - `tips` 和 `videos` 从原始长文/转录，变成了中文导读层。

### 合理但有代价的重编

- **长文报告明显被压缩**
  - 例如：
    - `best-practice/claude-settings.md`：本地约 `112` 行，上游约 `918` 行
    - `reports/claude-agent-sdk-vs-cli-system-prompts.md`：本地约 `70` 行，上游约 `340` 行
    - `reports/llm-day-to-day-degradation.md`：本地约 `69` 行，上游约 `360` 行
  - 这让中文读者更容易快速理解，但也损失了不少原始细节、表格和论证层次。

### 目前仍不够好的地方

- `presentation/index.html` 还没有达到“整套演示稿几乎可以直接中文讲”的完成度。
- 一些演示层和 appendix 区域仍残留英文标签、命令提示语和解释句。
- README 顶部的 sync badge 仍然写着 `v1 in progress`，和当前覆盖程度相比偏保守，甚至略显过时。

## D. 问题清单

### P0

**无。**

当前没有发现会直接破坏运行时功能或明显误导执行层的证据。

### P1

1. **演示稿还没达到“直接拿去中文分享”的完成度**
   - 现象：`presentation/index.html` 仍残留较多英文表头、说明句、命令示例注释、appendix 文案。
   - 典型位置：
     - [presentation/index.html](../presentation/index.html):271
     - [presentation/index.html](../presentation/index.html):398
     - [presentation/index.html](../presentation/index.html):644
     - [presentation/index.html](../presentation/index.html):1453
   - 影响：传播层完成度不足，拉低 GitHub 老开发者和新手读者两边的观感。

2. **部分长文被压缩得太狠，和 upstream 相比信息损失明显**
   - 典型位置：
     - [best-practice/claude-settings.md](../best-practice/claude-settings.md)
     - [reports/claude-agent-sdk-vs-cli-system-prompts.md](claude-agent-sdk-vs-cli-system-prompts.md)
     - [reports/llm-day-to-day-degradation.md](llm-day-to-day-degradation.md)
   - 影响：对于想深读、对照官方或做进一步研究的人，中文版本会显得“更顺手，但不够厚”。

3. **README 的进度信号落后于真实完成度**
   - 位置：[README.md](../README.md):10
   - 现象：badge 仍是 `sync v1 in progress`，但实际覆盖已远超 v1。
   - 影响：仓库首屏的可信度和专业感被轻微拉低。

### P2

1. **演示稿存在不少中英混排，虽然不影响理解，但会影响沉浸感**
   - 典型位置：
     - [presentation/index.html](../presentation/index.html):570
     - [presentation/index.html](../presentation/index.html):783
     - [presentation/index.html](../presentation/index.html):1560
   - 说明：这些有些是示例代码块里的注释，有些是可见文案，优先级低于 P1，但值得继续清。

2. **社区层更像高质量导读，不是完整“平行中文版原文”**
   - 典型位置：
     - [tips/claude-boris-13-tips-03-jan-26.md](../tips/claude-boris-13-tips-03-jan-26.md)
     - [videos/claude-cat-every-29-oct-25.md](../videos/claude-cat-every-29-oct-25.md)
   - 说明：这不是错误，而是当前 fork 的策略选择；但对想逐条核对原文的人来说，会感觉“导读强，原文保真度一般”。

3. **部分英文术语保留策略还没在演示层完全统一**
   - 现象：`Agentic Engineering`、`TodoApp`、`Slash commands`、`MCP Servers` 等有些地方保留得自然，有些地方看起来像半翻译半直出。
   - 影响：对老开发者问题不大，但初学者会觉得风格略跳。

## E. 下一步修复顺序

1. **继续完成 `presentation/index.html` 的整套中文化**
   - 优先清理可见表头、说明句、appendix、例子注释。

2. **把 README 顶部的进度 badge 和当前完成度对齐**
   - 让首页信号和仓库真实状态一致。

3. **给被压缩过猛的长文做“扩展版”回填**
   - 优先是 `claude-settings`、`agent-sdk-vs-cli`、`llm-day-to-day-degradation`。

4. **统一 presentation 和 Markdown 层的术语风格**
   - 减少中英混排的跳跃感。

5. **补一个“导读版 vs 深度版”的阅读提示**
   - 明确告诉读者哪些文件是重编摘要，哪些更接近深度参考。

6. **定期跑 upstream 同步演练**
   - 让 `scripts/check_upstream_sync.py` 真正成为维护流程的一部分，而不是一次性脚本。
