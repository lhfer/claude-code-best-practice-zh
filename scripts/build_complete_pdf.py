#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "pdf"
SOURCE_MD = OUTPUT_DIR / "claude-code-best-practice-zh-complete-handbook.md"
TARGET_PDF = OUTPUT_DIR / "claude-code-best-practice-zh-complete-handbook.pdf"


class HandbookDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = getattr(flowable, "style", None)
            text = flowable.getPlainText().strip()
            if not style or not text:
                return
            if style.name == "PartZH":
                key = slugify(text)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=0, closed=False)
            elif style.name == "FileZH":
                key = slugify(text)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=1, closed=False)


MANIFEST = [
    (
        "第 0 部分：如何使用这本手册",
        [],
    ),
    (
        "第 1 部分：安装与入门",
        [
            ROOT / "tutorial" / "README.md",
            ROOT / "tutorial" / "day0" / "README.md",
            ROOT / "tutorial" / "day0" / "mac.md",
            ROOT / "tutorial" / "day0" / "linux.md",
            ROOT / "tutorial" / "day0" / "windows.md",
        ],
    ),
    (
        "第 2 部分：核心概念与最佳实践",
        [
            ROOT / "best-practice" / "claude-subagents.md",
            ROOT / "best-practice" / "claude-skills.md",
            ROOT / "best-practice" / "claude-commands.md",
            ROOT / "best-practice" / "claude-memory.md",
            ROOT / "best-practice" / "claude-settings.md",
            ROOT / "best-practice" / "claude-mcp.md",
            ROOT / "best-practice" / "claude-cli-startup-flags.md",
        ],
    ),
    (
        "第 3 部分：关键解释与边界",
        [
            ROOT / "reports" / "claude-agent-command-skill.md",
            ROOT / "reports" / "claude-global-vs-project-settings.md",
            ROOT / "reports" / "claude-skills-for-larger-mono-repos.md",
            ROOT / "reports" / "claude-agent-memory.md",
            ROOT / "reports" / "claude-usage-and-rate-limits.md",
            ROOT / "reports" / "claude-advanced-tool-use.md",
            ROOT / "reports" / "claude-in-chrome-v-chrome-devtools-mcp.md",
            ROOT / "reports" / "claude-agent-sdk-vs-cli-system-prompts.md",
            ROOT / "reports" / "llm-day-to-day-degradation.md",
        ],
    ),
    (
        "第 4 部分：实现与样例",
        [
            ROOT / "orchestration-workflow" / "orchestration-workflow.md",
            ROOT / "implementation" / "claude-commands-implementation.md",
            ROOT / "implementation" / "claude-skills-implementation.md",
            ROOT / "implementation" / "claude-subagents-implementation.md",
            ROOT / "implementation" / "claude-agent-teams-implementation.md",
            ROOT / "implementation" / "claude-scheduled-tasks-implementation.md",
        ],
    ),
    (
        "第 5 部分：工作流与协作",
        [
            ROOT / "development-workflows" / "README.md",
            ROOT / "development-workflows" / "cross-model-workflow" / "cross-model-workflow.md",
            ROOT / "development-workflows" / "rpi" / "rpi-workflow.md",
            ROOT / "agent-teams" / "README.md",
            ROOT / "agent-teams" / "agent-teams-prompt.md",
        ],
    ),
    (
        "第 6 部分：社区经验与导读",
        [
            ROOT / "tips" / "README.md",
            ROOT / "tips" / "claude-boris-10-tips-01-feb-26.md",
            ROOT / "tips" / "claude-boris-12-tips-12-feb-26.md",
            ROOT / "tips" / "claude-boris-13-tips-03-jan-26.md",
            ROOT / "tips" / "claude-boris-15-tips-30-mar-26.md",
            ROOT / "tips" / "claude-boris-2-tips-10-mar-26.md",
            ROOT / "tips" / "claude-boris-2-tips-25-mar-26.md",
            ROOT / "tips" / "claude-thariq-tips-17-mar-26.md",
            ROOT / "videos" / "README.md",
            ROOT / "videos" / "claude-boris-lennys-podcast-19-feb-26.md",
            ROOT / "videos" / "claude-boris-pragmatic-engineer-04-mar-26.md",
            ROOT / "videos" / "claude-boris-ryan-peterman-15-dec-25.md",
            ROOT / "videos" / "claude-boris-y-combinator-17-feb-26.md",
            ROOT / "videos" / "claude-cat-every-29-oct-25.md",
        ],
    ),
    (
        "第 7 部分：哪些值得直接抄，哪些不要直接抄",
        [],
    ),
    (
        "第 8 部分：7 天学习路径与附录",
        [],
    ),
]


TITLE_MAP = {
    "tutorial/README.md": "教程入口",
    "tutorial/day0/README.md": "Day 0：第一天把 Claude Code 跑起来",
    "tutorial/day0/mac.md": "macOS 安装",
    "tutorial/day0/linux.md": "Linux 安装",
    "tutorial/day0/windows.md": "Windows 安装",
    "best-practice/claude-subagents.md": "Subagents 最佳实践",
    "best-practice/claude-skills.md": "Skills 最佳实践",
    "best-practice/claude-commands.md": "Commands 最佳实践",
    "best-practice/claude-memory.md": "Memory 最佳实践",
    "best-practice/claude-settings.md": "Settings 最佳实践",
    "best-practice/claude-mcp.md": "MCP 最佳实践",
    "best-practice/claude-cli-startup-flags.md": "CLI 启动参数最佳实践",
    "reports/claude-agent-command-skill.md": "Agents / Commands / Skills 边界解释",
    "reports/claude-global-vs-project-settings.md": "全局 vs 项目级设置",
    "reports/claude-skills-for-larger-mono-repos.md": "Monorepo 里的 Skills",
    "reports/claude-agent-memory.md": "Agent Memory 解释",
    "reports/claude-usage-and-rate-limits.md": "使用量、速率限制与 Extra Usage",
    "reports/claude-advanced-tool-use.md": "高级工具使用模式",
    "reports/claude-in-chrome-v-chrome-devtools-mcp.md": "浏览器自动化 MCP 选择",
    "reports/claude-agent-sdk-vs-cli-system-prompts.md": "Agent SDK vs CLI：系统提示与一致性",
    "reports/llm-day-to-day-degradation.md": "LLM 日常退化：神话 vs 现实",
    "orchestration-workflow/orchestration-workflow.md": "最小工作流样例：Command → Agent → Skill",
    "implementation/claude-commands-implementation.md": "Commands 实现样例",
    "implementation/claude-skills-implementation.md": "Skills 实现样例",
    "implementation/claude-subagents-implementation.md": "Subagents 实现样例",
    "implementation/claude-agent-teams-implementation.md": "Agent Teams 实现样例",
    "implementation/claude-scheduled-tasks-implementation.md": "Scheduled Tasks 实现样例",
    "development-workflows/README.md": "工作流入口",
    "development-workflows/cross-model-workflow/cross-model-workflow.md": "Cross-model workflow",
    "development-workflows/rpi/rpi-workflow.md": "RPI workflow",
    "agent-teams/README.md": "Agent Teams 入口",
    "agent-teams/agent-teams-prompt.md": "Agent Teams 提示词样例",
    "tips/README.md": "社区经验入口",
    "videos/README.md": "视频导读入口",
}

PART_INTROS = {
    "第 0 部分：如何使用这本手册": [
        "这本手册的目标，不是带你看懂这个仓库本身，而是带你学会 Claude Code 这套工作方式。",
        "如果你是第一次接触 Claude Code，建议从第 1 部分和第 2 部分开始。",
        "如果你已经在用 Claude Code，但想把它真正接进项目和团队协作，重点读第 3 到第 6 部分。",
    ],
    "第 1 部分：安装与入门": [
        "这一部分只解决一个问题：先把 Claude Code 真的跑起来。",
        "先别急着折腾配置、agent 或 workflow；把安装、验证和第一次登录走通，后面所有内容才有意义。",
    ],
    "第 2 部分：核心概念与最佳实践": [
        "这一部分负责建立 Claude Code 的基本脑图。",
        "如果 `command / agent / skill / memory / settings / MCP / hooks` 这些词你还没有清楚分层，先把这部分吃透。",
    ],
    "第 3 部分：关键解释与边界": [
        "这一部分回答的是“为什么要这样分层”和“最容易搞混的边界是什么”。",
        "如果你已经会用一点 Claude Code，但总觉得概念模模糊糊，这部分最有价值。",
    ],
    "第 4 部分：实现与样例": [
        "这一部分不是抽象概念，而是仓库里的真实落地样例。",
        "读到这里，你应该开始能把“知识层”映射到“文件怎么组织、工作流怎么跑”。",
    ],
    "第 5 部分：工作流与协作": [
        "这一部分聚焦于更大粒度的流程设计。",
        "从单条 prompt 到多阶段 workflow、多模型协作、多 agent 协作，都会在这里出现。",
    ],
    "第 6 部分：社区经验与导读": [
        "这一部分不是正式规范，而是高信号经验层。",
        "适合在你已经理解基本概念之后，看高手和产品团队是怎么把 Claude Code 真正用顺的。",
    ],
    "第 7 部分：哪些值得直接抄，哪些不要直接抄": [
        "这一部分是为了避免你把中文仓库当成“万能模板”。",
        "真正应该抄的是结构、方法和边界；不该盲抄的是过度个性化配置和仍在演进中的演示层。",
    ],
    "第 8 部分：7 天学习路径与附录": [
        "最后这一部分把前面的大量内容收敛成行动路径。",
        "如果你想把学习结果落回自己的项目里，这里最值得反复看。",
    ],
}

CUSTOM_PART_CONTENT = {
    "第 7 部分：哪些值得直接抄，哪些不要直接抄": """
## 值得直接抄的

- 学习路径设计
- `README` 入口导航
- 术语分层方式
- `command / agent / skill` 的职责切分
- 运行保护清单和本地校验脚本
- 工作流样例的拆法

## 先不要直接抄的

- 过度个性化的 spinner / status line 文案
- 仍在持续中文化的 presentation 细节
- 任何你自己都还没理解边界的运行时配置

## 一句话原则

先抄结构和方法，再抄具体配置。
""",
    "第 8 部分：7 天学习路径与附录": """
## 7 天学习路径

### Day 1

- 跑起来 Claude Code
- 完成第一次登录

### Day 2

- 搞懂 `command / agent / skill`

### Day 3

- 搞懂 `CLAUDE.md / memory / rules`

### Day 4

- 搞懂 `settings / permissions / hooks / MCP`

### Day 5

- 看懂最小工作流样例

### Day 6

- 看 `tips` 和 `videos`

### Day 7

- 在你自己的项目里，做出第一个真正可用的 command、skill 或 agent

## 附录：按目标挑内容

### 我只想快速学会

- `tutorial/day0/README.md`
- `reports/claude-agent-command-skill.md`
- `best-practice/claude-subagents.md`
- `best-practice/claude-skills.md`

### 我想搭自己的团队工作流

- `best-practice/claude-settings.md`
- `best-practice/claude-mcp.md`
- `development-workflows/rpi/rpi-workflow.md`
- `development-workflows/cross-model-workflow/cross-model-workflow.md`

### 我想继续深挖

- `reports/README.md`
- `reports/zh-fork-review-scorecard.md`
- upstream 原仓
""",
}


def register_fonts():
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleZH",
            parent=base["Title"],
            fontName="STSong-Light",
            fontSize=24,
            leading=32,
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "subtitle": ParagraphStyle(
            "SubtitleZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=11,
            leading=18,
            alignment=TA_CENTER,
            textColor=HexColor("#555555"),
            spaceAfter=14,
        ),
        "part": ParagraphStyle(
            "PartZH",
            parent=base["Heading1"],
            fontName="STSong-Light",
            fontSize=18,
            leading=24,
            textColor=HexColor("#111111"),
            spaceBefore=10,
            spaceAfter=8,
        ),
        "file": ParagraphStyle(
            "FileZH",
            parent=base["Heading2"],
            fontName="STSong-Light",
            fontSize=14,
            leading=20,
            textColor=HexColor("#1f4b99"),
            spaceBefore=8,
            spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "H2ZH",
            parent=base["Heading3"],
            fontName="STSong-Light",
            fontSize=12.5,
            leading=18,
            spaceBefore=6,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "BodyZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=10.5,
            leading=17,
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "BulletZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=10.5,
            leading=16,
        ),
        "quote": ParagraphStyle(
            "QuoteZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=10.5,
            leading=17,
            leftIndent=10 * mm,
            textColor=HexColor("#444444"),
            spaceBefore=2,
            spaceAfter=4,
        ),
        "meta": ParagraphStyle(
            "MetaZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=9.2,
            leading=14,
            textColor=HexColor("#666666"),
            spaceAfter=5,
        ),
        "code": ParagraphStyle(
            "CodeZH",
            parent=base["Code"],
            fontName="STSong-Light",
            fontSize=9.2,
            leading=13,
            leftIndent=6 * mm,
            rightIndent=3 * mm,
            backColor=HexColor("#f4f4f4"),
            borderPadding=6,
            spaceAfter=6,
        ),
        "toc": ParagraphStyle(
            "TOCZH",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=11,
            leading=18,
            textColor=HexColor("#1f4b99"),
            leftIndent=2 * mm,
            spaceAfter=3,
        ),
    }


def slugify(text: str) -> str:
    text = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-").lower()
    return text or "section"


def clean_lines(path: Path) -> list[str]:
    lines = path.read_text().splitlines()
    out: list[str] = []
    in_fence = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if idx == 0 and stripped.startswith("# "):
            continue
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if stripped in {"[Back to Day 0](README.md)", "[返回 Day 0](README.md)"}:
            continue
        if "回到根 README" in stripped or "head back to [README.md]" in stripped or "装好后回到 [README.md]" in stripped or "装好后再回到 [README.md]" in stripped:
            continue
        if stripped.startswith("> 中文重编版") or stripped.startswith("> 上游原文：") or stripped.startswith("> 上游整理：") or stripped.startswith("> 视频："):
            continue
        if stripped.startswith("<table") or stripped.startswith("</table>") or stripped.startswith("<tr>") or stripped.startswith("</tr>") or stripped.startswith("<td") or stripped.startswith("</td>"):
            continue
        if stripped.startswith("![Last Updated]") or stripped.startswith("[![") or stripped.startswith("<img ") or stripped.startswith("<p align=") or stripped.startswith("<a href="):
            continue
        if stripped.startswith("[![") or stripped.startswith("!["):
            continue
        if stripped.startswith("## Sources") or stripped.startswith("## Sources".lower()):
            continue
        if stripped.startswith("## Video Details") or stripped.startswith("## Transcript") or stripped.startswith("## Sources"):
            continue
        if stripped.startswith("## Table of Contents"):
            continue
        if stripped == "---":
            continue
        if path.relative_to(ROOT).as_posix() == "tutorial/README.md" and stripped == "- [day0/README.md](day0/README.md)":
            out.append("- Day 0：第一天把 Claude Code 跑起来")
            continue
        out.append(line)
    return out


def parse_blocks(lines: list[str]):
    buf: list[str] = []
    mode = "paragraph"
    in_fence = False
    fence_buf: list[str] = []
    for line in lines + [""]:
        stripped = line.rstrip("\n")
        if stripped.strip().startswith("```"):
            if not in_fence:
                if buf:
                    yield mode, buf
                    buf = []
                in_fence = True
                fence_buf = []
            else:
                yield "code", fence_buf
                in_fence = False
                fence_buf = []
            continue
        if in_fence:
            fence_buf.append(stripped)
            continue
        if stripped.startswith("## "):
            if buf:
                yield mode, buf
                buf = []
            yield "h2", [stripped[3:].strip()]
            mode = "paragraph"
        elif stripped.startswith("### "):
            if buf:
                yield mode, buf
                buf = []
            yield "h2", [stripped[4:].strip()]
            mode = "paragraph"
        elif re.match(r"^\d+\.\s+", stripped):
            if mode != "olist":
                if buf:
                    yield mode, buf
                    buf = []
                mode = "olist"
            buf.append(re.sub(r"^\d+\.\s+", "", stripped).strip())
        elif stripped.startswith("- "):
            if mode != "list":
                if buf:
                    yield mode, buf
                    buf = []
                mode = "list"
            buf.append(stripped[2:].strip())
        elif stripped.startswith("> "):
            if buf:
                yield mode, buf
                buf = []
            yield "quote", [stripped[2:].strip()]
            mode = "paragraph"
        elif stripped.startswith("|") and "|" in stripped[1:]:
            if mode != "table":
                if buf:
                    yield mode, buf
                    buf = []
                mode = "table"
            buf.append(stripped)
        elif not stripped.strip():
            if buf:
                yield mode, buf
                buf = []
            mode = "paragraph"
        else:
            if mode not in {"paragraph", "table"}:
                if buf:
                    yield mode, buf
                    buf = []
                mode = "paragraph"
            buf.append(stripped.strip())


def build_link_map():
    mapping = {}
    for _, files in MANIFEST:
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            mapping[rel] = (TITLE_MAP.get(rel, file.read_text().splitlines()[0].replace("# ", "").strip()), slugify(rel))
    return mapping


def inline_markup(text: str, link_map: dict[str, tuple[str, str]], current_rel: str | None = None) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", "", text)
    text = html.escape(text)
    def repl_link(match):
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            return label
        clean_target = target.split("#")[0]
        resolved_target = clean_target
        if current_rel and not clean_target.startswith("/"):
            resolved_target = str((Path(current_rel).parent / clean_target).as_posix()).replace("\\", "/")
            resolved_target = str(Path(resolved_target))
            resolved_target = resolved_target.replace("\\", "/")
        candidates = [clean_target, resolved_target]
        chosen = None
        for cand in candidates:
            if cand in link_map:
                chosen = cand
                break
        if chosen:
            mapped_title, anchor = link_map[chosen]
            shown = mapped_title if (label.endswith(".md") or "/" in label) else label
            return f"<link href='#{anchor}'>{shown}</link>"
        return label
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font face='Courier'>\1</font>", text)
    text = text.replace("&amp;rarr;", "&rarr;")
    text = text.replace("&amp;larr;", "&larr;")
    return text


def markdown_table_to_data(lines: list[str]):
    rows = []
    for idx, line in enumerate(lines):
        if idx == 1 and set(line.replace("|", "").replace("-", "").replace(":", "").strip()) == set():
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def assemble_source_markdown() -> str:
    out = [
        "# Claude Code 中文完整手册",
        "",
        "这是一份脱离 GitHub 仓库也能完整阅读的学习路径版手册。",
        "",
        "你会看到：",
        "- 入门安装与登录",
        "- 核心概念与最佳实践",
        "- 边界解释与深度报告",
        "- 样例实现与工作流",
        "- 社区经验与视频导读",
        "",
    ]
    for part_title, files in MANIFEST:
        out.extend([f"# {part_title}", ""])
        if part_title in PART_INTROS:
            out.extend(PART_INTROS[part_title])
            out.append("")
        if part_title in CUSTOM_PART_CONTENT:
            out.extend(CUSTOM_PART_CONTENT[part_title].strip().splitlines())
            out.append("")
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            title = clean_lines(file)
            file_title = TITLE_MAP.get(rel, file.read_text().splitlines()[0].replace("# ", "").strip())
            out.extend([f"## {file_title}", ""])
            out.extend(title)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def make_toc(paragraphs: list[tuple[str, str]]) -> list[Paragraph]:
    s = build_styles()
    toc = [Paragraph("目录", s["part"]), Spacer(1, 4 * mm)]
    for title, anchor in paragraphs:
        toc.append(Paragraph(f'<link href="#{anchor}">{html.escape(title)}</link>', s["toc"]))
    toc.append(PageBreak())
    return toc


def build_pdf():
    register_fonts()
    styles = build_styles()
    link_map = build_link_map()
    source = assemble_source_markdown()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SOURCE_MD.write_text(source)

    story = []
    story.append(Spacer(1, 18 * mm))
    story.append(Paragraph("Claude Code 中文完整手册", styles["title"]))
    story.append(
        Paragraph(
            "把这份中文 fork 中最值得学、最适合离线阅读的内容，按学习路径重新编排成一本可独立阅读的 PDF。",
            styles["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "适合：想系统入门、搭项目工作流、做团队分享，或者只想一份不依赖 GitHub 跳转的完整中文资料。",
            styles["subtitle"],
        )
    )
    story.append(PageBreak())

    toc_entries: list[tuple[str, str]] = []
    for part_title, files in MANIFEST:
        toc_entries.append((part_title, slugify(part_title)))
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            title = TITLE_MAP.get(rel, file.read_text().splitlines()[0].replace("# ", "").strip())
            toc_entries.append((f"  {title}", slugify(rel)))

    story.extend(make_toc(toc_entries))

    for part_title, files in MANIFEST:
        story.append(Paragraph(f'<a name="{slugify(part_title)}"/>{html.escape(part_title)}', styles["part"]))
        story.append(Spacer(1, 2 * mm))
        for intro in PART_INTROS.get(part_title, []):
            story.append(Paragraph(intro, styles["body"]))
        if part_title in PART_INTROS:
            story.append(Spacer(1, 2 * mm))
        if part_title in CUSTOM_PART_CONTENT:
            blocks = parse_blocks(CUSTOM_PART_CONTENT[part_title].strip().splitlines())
            for kind, content in blocks:
                if kind == "h2":
                    story.append(Paragraph(inline_markup(content[0], link_map, rel), styles["h2"]))
                elif kind == "paragraph":
                    story.append(Paragraph("<br/>".join(inline_markup(x, link_map, rel) for x in content), styles["body"]))
                elif kind == "quote":
                    story.append(Paragraph(inline_markup(content[0], link_map, rel), styles["quote"]))
                elif kind == "list":
                    items = [ListItem(Paragraph(inline_markup(item, link_map, rel), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="bullet", leftIndent=14))
                elif kind == "olist":
                    items = [ListItem(Paragraph(inline_markup(item, link_map, rel), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="1", leftIndent=14))
            story.append(Spacer(1, 4 * mm))
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            file_anchor = slugify(rel)
            file_title = TITLE_MAP.get(rel, file.read_text().splitlines()[0].replace("# ", "").strip())
            story.append(
                KeepTogether(
                    [
                        Paragraph(f'<a name="{file_anchor}"/>{html.escape(file_title)}', styles["file"]),
                    ]
                )
            )
            blocks = parse_blocks(clean_lines(file))
            for kind, content in blocks:
                if kind == "h2":
                    story.append(Paragraph(inline_markup(content[0], link_map), styles["h2"]))
                elif kind == "paragraph":
                    story.append(Paragraph("<br/>".join(inline_markup(x, link_map) for x in content), styles["body"]))
                elif kind == "quote":
                    story.append(Paragraph(inline_markup(content[0], link_map), styles["quote"]))
                elif kind == "list":
                    items = [ListItem(Paragraph(inline_markup(item, link_map), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="bullet", leftIndent=14))
                elif kind == "olist":
                    items = [ListItem(Paragraph(inline_markup(item, link_map), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="1", leftIndent=14))
                elif kind == "table":
                    data = markdown_table_to_data(content)
                    if data:
                        formatted = []
                        for row in data:
                            formatted.append([Paragraph(inline_markup(cell, link_map, rel), styles["body"]) for cell in row])
                        table = Table(data, hAlign="LEFT")
                        table = Table(formatted, hAlign="LEFT")
                        table.setStyle(
                            TableStyle(
                                [
                                    ("FONTNAME", (0, 0), (-1, -1), "STSong-Light"),
                                    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
                                    ("LEADING", (0, 0), (-1, -1), 12),
                                    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#f4f4f4")),
                                    ("GRID", (0, 0), (-1, -1), 0.25, HexColor("#cccccc")),
                                    ("PADDING", (0, 0), (-1, -1), 4),
                                ]
                            )
                        )
                        story.append(table)
                elif kind == "code":
                    story.append(Preformatted("\n".join(content), styles["code"]))
            story.append(Spacer(1, 6 * mm))

    def draw_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("STSong-Light", 9)
        canvas.setFillColor(HexColor("#666666"))
        canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"{canvas.getPageNumber()}")
        canvas.restoreState()

    doc = HandbookDocTemplate(
        str(TARGET_PDF),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Claude Code 中文完整手册",
        author="Codex",
    )
    doc.build(story, onFirstPage=draw_page_number, onLaterPages=draw_page_number)


if __name__ == "__main__":
    build_pdf()
