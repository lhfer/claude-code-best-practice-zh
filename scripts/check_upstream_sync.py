#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def try_run(*args: str) -> str | None:
    try:
        return run(*args)
    except subprocess.CalledProcessError:
        return None


def main() -> int:
    if not try_run("git", "remote", "get-url", "upstream"):
        print("No upstream remote configured.")
        return 1

    subprocess.check_call(["git", "fetch", "upstream", "main", "--quiet"], cwd=ROOT)

    local = run("git", "rev-parse", "HEAD")
    upstream = run("git", "rev-parse", "upstream/main")
    ahead = run("git", "rev-list", "--count", "upstream/main..HEAD")
    behind = run("git", "rev-list", "--count", "HEAD..upstream/main")

    print("Upstream sync check")
    print("===================")
    print(f"local   : {local}")
    print(f"upstream: {upstream}")
    print(f"ahead   : {ahead}")
    print(f"behind  : {behind}")

    if behind == "0":
        print("\nNo new upstream commits to sync.")
        return 0

    print("\nNew upstream commits:")
    log = run("git", "log", "--oneline", "--decorate", "--no-merges", "HEAD..upstream/main")
    print(log)

    print("\nChanged files since local HEAD:")
    diff = run("git", "diff", "--name-only", "HEAD..upstream/main")
    print(diff)
    return 0


if __name__ == "__main__":
    sys.exit(main())
