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
        [
            ROOT / "README.md",
        ],
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
]


TITLE_MAP = {
    "README.md": "项目首页与使用说明",
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


def inline_markup(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", "", text)
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<font face='Courier'>\1</font>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = text.replace("&amp;rarr;", "&rarr;")
    text = text.replace("&amp;larr;", "&larr;")
    return text


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
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            title = clean_lines(file)
            file_title = file.read_text().splitlines()[0].replace("# ", "").strip()
            out.extend([f"## {file_title}", f"> 来源：`{rel}`", ""])
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
        for file in files:
            rel = file.relative_to(ROOT).as_posix()
            file_anchor = slugify(rel)
            file_title = TITLE_MAP.get(rel, file.read_text().splitlines()[0].replace("# ", "").strip())
            story.append(
                KeepTogether(
                    [
                        Paragraph(f'<a name="{file_anchor}"/>{html.escape(file_title)}', styles["file"]),
                        Paragraph(f"来源：{html.escape(rel)}", styles["meta"]),
                    ]
                )
            )
            blocks = parse_blocks(clean_lines(file))
            for kind, content in blocks:
                if kind == "h2":
                    story.append(Paragraph(inline_markup(content[0]), styles["h2"]))
                elif kind == "paragraph":
                    story.append(Paragraph("<br/>".join(inline_markup(x) for x in content), styles["body"]))
                elif kind == "quote":
                    story.append(Paragraph(inline_markup(content[0]), styles["quote"]))
                elif kind == "list":
                    items = [ListItem(Paragraph(inline_markup(item), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="bullet", leftIndent=14))
                elif kind == "olist":
                    items = [ListItem(Paragraph(inline_markup(item), styles["bullet"])) for item in content]
                    story.append(ListFlowable(items, bulletType="1", leftIndent=14))
                elif kind == "table":
                    story.append(Preformatted("\n".join(content), styles["code"]))
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
