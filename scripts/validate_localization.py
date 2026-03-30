#!/usr/bin/env python3
from __future__ import annotations

import fnmatch
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_FILE = ROOT / "PROTECTED_RUNTIME_PATHS.txt"
SYNC_STATUS = ROOT / "SYNC_STATUS.md"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()


def git_lines(*args: str) -> list[str]:
    try:
        out = run("git", *args)
    except subprocess.CalledProcessError:
        return []
    return [line for line in out.splitlines() if line.strip()]


def merge_base() -> str:
    for ref in ("upstream/main", "origin/main"):
        try:
            return run("git", "merge-base", "HEAD", ref)
        except subprocess.CalledProcessError:
            continue
    return run("git", "rev-parse", "HEAD")


def changed_files() -> list[str]:
    base = merge_base()
    files = set(git_lines("diff", "--name-only", f"{base}...HEAD"))
    files.update(git_lines("diff", "--name-only"))
    files.update(git_lines("diff", "--cached", "--name-only"))
    return sorted(files)


def protected_patterns() -> list[str]:
    return [line.strip() for line in PROTECTED_FILE.read_text().splitlines() if line.strip()]


def is_protected(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value)


def bad_markdown_links(path: Path) -> list[str]:
    bad: list[str] = []
    text = path.read_text()
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            bad.append(target)
    return bad


def bad_html_assets(path: Path) -> list[str]:
    parser = AssetParser()
    parser.feed(path.read_text())
    bad: list[str] = []
    for target in parser.targets:
        if target.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            bad.append(target)
    return bad


def missing_sync_markers() -> list[str]:
    markers = [
        "tips",
        "videos",
        "tutorial",
        "development-workflows",
        "agent-teams",
        "changelog",
        ".claude/hooks/HOOKS-README.md",
        ".codex/hooks/HOOKS-README.md",
    ]
    text = SYNC_STATUS.read_text()
    return [item for item in markers if item not in text]


def main() -> int:
    files = changed_files()
    patterns = protected_patterns()
    errors: list[str] = []

    protected = [path for path in files if is_protected(path, patterns)]
    if protected:
        errors.append("Protected runtime paths changed:")
        errors.extend(f"  - {path}" for path in protected)

    for rel in files:
        path = ROOT / rel
        if not path.exists():
            continue
        if rel.startswith("output/pdf/") and path.suffix == ".md":
            continue
        if path.suffix == ".md":
            bad = bad_markdown_links(path)
            if bad:
                errors.append(f"Broken relative links in {rel}:")
                errors.extend(f"  - {target}" for target in bad)
        if path.suffix == ".html":
            bad = bad_html_assets(path)
            if bad:
                errors.append(f"Broken relative assets in {rel}:")
                errors.extend(f"  - {target}" for target in bad)

    missing = missing_sync_markers()
    if missing:
        errors.append("SYNC_STATUS.md is missing expected module markers:")
        errors.extend(f"  - {item}" for item in missing)

    if errors:
        print("Localization validation failed.\n")
        print("\n".join(errors))
        return 1

    print("Localization validation passed.")
    print(f"Checked {len(files)} changed file(s).")
    print("Protected runtime paths untouched, relative links valid, and sync markers present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
