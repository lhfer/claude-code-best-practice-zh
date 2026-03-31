#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "output/pdf/claude-code-best-practice-zh-learning-guide.md"
TARGET = ROOT / "output/pdf/claude-code-best-practice-zh-learning-guide.pdf"
COVER_IMAGE = ROOT / "assets" / "pdf" / "claude-code-best-practice-cover.png"


def styles():
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleZH", parent=base["Title"], fontName="STSong-Light", fontSize=24, leading=32, alignment=TA_CENTER, spaceAfter=16
        ),
        "subtitle": ParagraphStyle(
            "SubtitleZH", parent=base["BodyText"], fontName="STSong-Light", fontSize=11, leading=18, alignment=TA_CENTER, textColor="#555555", spaceAfter=18
        ),
        "h1": ParagraphStyle(
            "H1ZH", parent=base["Heading1"], fontName="STSong-Light", fontSize=18, leading=24, spaceBefore=10, spaceAfter=8
        ),
        "h2": ParagraphStyle(
            "H2ZH", parent=base["Heading2"], fontName="STSong-Light", fontSize=14, leading=20, spaceBefore=8, spaceAfter=6
        ),
        "body": ParagraphStyle(
            "BodyZH", parent=base["BodyText"], fontName="STSong-Light", fontSize=10.5, leading=17, spaceAfter=6
        ),
        "bullet": ParagraphStyle(
            "BulletZH", parent=base["BodyText"], fontName="STSong-Light", fontSize=10.5, leading=16
        ),
        "quote": ParagraphStyle(
            "QuoteZH", parent=base["BodyText"], fontName="STSong-Light", fontSize=10.5, leading=17, leftIndent=10*mm, textColor="#444444", spaceBefore=4, spaceAfter=6
        ),
    }


def parse_markdown(text: str):
    lines = text.splitlines()
    buf = []
    mode = "paragraph"
    for line in lines + [""]:
        if line.startswith("# "):
            if buf:
                yield mode, buf
                buf = []
            yield "h1", [line[2:].strip()]
            mode = "paragraph"
        elif line.startswith("## "):
            if buf:
                yield mode, buf
                buf = []
            yield "h2", [line[3:].strip()]
            mode = "paragraph"
        elif line.startswith("- "):
            if mode != "list":
                if buf:
                    yield mode, buf
                    buf = []
                mode = "list"
            buf.append(line[2:].strip())
        elif line.startswith("> "):
            if buf:
                yield mode, buf
                buf = []
            yield "quote", [line[2:].strip()]
            mode = "paragraph"
        elif not line.strip():
            if buf:
                yield mode, buf
                buf = []
            mode = "paragraph"
        else:
            if mode != "paragraph":
                if buf:
                    yield mode, buf
                    buf = []
                mode = "paragraph"
            buf.append(line.strip())


def build():
    s = styles()
    story = []
    text = SOURCE.read_text()
    title_done = False
    for kind, content in parse_markdown(text):
        if kind == "h1" and not title_done:
            story.append(Spacer(1, 18 * mm))
            story.append(Paragraph(content[0], s["title"]))
            story.append(
                Paragraph(
                    "从入门、概念、项目配置、工作流，到团队落地的一本中文学习路径手册",
                    s["subtitle"],
                )
            )
            story.append(PageBreak())
            title_done = True
            continue
        if kind == "h1":
            story.append(Paragraph(content[0], s["h1"]))
        elif kind == "h2":
            story.append(Paragraph(content[0], s["h2"]))
        elif kind == "paragraph":
            story.append(Paragraph("<br/>".join(content), s["body"]))
        elif kind == "quote":
            story.append(Paragraph(content[0], s["quote"]))
        elif kind == "list":
            items = [ListItem(Paragraph(item, s["bullet"])) for item in content]
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=14))
    def draw_cover(canvas, doc):
        canvas.saveState()
        page_w, page_h = A4
        margin = 18 * mm
        avail_w = page_w - 2 * margin
        avail_h = page_h - 2 * margin
        from PIL import Image as PILImage
        with PILImage.open(COVER_IMAGE) as im:
            iw, ih = im.size
        scale = min(avail_w / iw, avail_h / ih)
        draw_w = iw * scale
        draw_h = ih * scale
        x = (page_w - draw_w) / 2
        y = (page_h - draw_h) / 2
        canvas.drawImage(str(COVER_IMAGE), x, y, width=draw_w, height=draw_h, preserveAspectRatio=True, mask='auto')
        canvas.restoreState()

    def draw_cover(cover_pdf: Path):
        c = Canvas(str(cover_pdf), pagesize=A4)
        page_w, page_h = A4
        margin = 18 * mm
        avail_w = page_w - 2 * margin
        avail_h = page_h - 2 * margin
        from PIL import Image as PILImage
        with PILImage.open(COVER_IMAGE) as im:
            iw, ih = im.size
        scale = min(avail_w / iw, avail_h / ih)
        draw_w = iw * scale
        draw_h = ih * scale
        x = (page_w - draw_w) / 2
        y = (page_h - draw_h) / 2
        c.drawImage(str(COVER_IMAGE), x, y, width=draw_w, height=draw_h, preserveAspectRatio=True, mask='auto')
        c.showPage()
        c.save()

    def build_body(path: Path):
        doc = SimpleDocTemplate(
            str(path),
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=18 * mm,
            bottomMargin=18 * mm,
            title="Claude Code 中文学习路径手册",
            author="Codex",
        )
        doc.build(story)

    with TemporaryDirectory() as td:
        body_pdf = Path(td) / "learning-body.pdf"
        build_body(body_pdf)
        if COVER_IMAGE.exists():
            cover_pdf = Path(td) / "learning-cover.pdf"
            draw_cover(cover_pdf)
            from pypdf import PdfReader, PdfWriter
            writer = PdfWriter()
            for src in [cover_pdf, body_pdf]:
                reader = PdfReader(str(src))
                for page in reader.pages:
                    writer.add_page(page)
            writer.add_metadata({"/Title": "Claude Code 中文学习路径手册", "/Author": "Codex"})
            with open(TARGET, "wb") as fh:
                writer.write(fh)
        else:
            TARGET.write_bytes(body_pdf.read_bytes())


if __name__ == "__main__":
    build()
