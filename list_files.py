#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import date

def list_files_in(dirpath: Path, patterns: list[str]) -> list[Path]:
    out: list[Path] = []
    for pat in patterns:
        out.extend(dirpath.glob(pat))
    return sorted(f for f in out if f.is_file())

def write_listing(project_root: Path, config: dict[Path, list[str]], out_name: str) -> None:
    with open(out_name, "w", encoding="utf-8") as f:
        for dirpath, patterns in config.items():
            # Print directory relative to the project root
            f.write(f"{dirpath.relative_to(project_root)}\n")
            for fn in list_files_in(dirpath, patterns):
                f.write(f"  {fn.relative_to(project_root)}\n")
            f.write("\n")
    print(f"Wrote file list to {out_name}")

def main():
    today = date.today().strftime("%Y%m%d")
    project_root = Path.cwd()
    proj = project_root.name

    # Detect layout
    if proj == "ai-building-blocks-agent":
        agent_root = project_root
        db_root = None
    elif proj == "ai-building-blocks-database":
        db_root = project_root
        agent_root = None
    elif proj == "suite-cisco-ai-building-blocks":
        # monorepo layout
        agent_root = project_root / "ai-building-blocks-agent"
        db_root    = project_root / "ai-building-blocks-database"
    else:
        sys.exit(f"⚠️  Unrecognized project folder: {proj}")

    # Agent service listing
    if agent_root:
        agent_cfg: dict[Path, list[str]] = {
            project_root:                ["*.md"],
            agent_root / "app":          ["*.py"],
            agent_root / "app" / "llm":  ["*.py"],
            agent_root / "app" / "routers":["*.py"],
            agent_root / "retrievers":   ["*.py"],
            agent_root / "scripts":      ["*.py"],
            agent_root / "static":       ["*.html"],
            agent_root / "tools":        ["*.py"],
        }
        write_listing(project_root, agent_cfg, f"ai-building-agent-{today}.txt")

    # Database project listing
    if db_root:
        db_cfg: dict[Path, list[str]] = {
            project_root:      ["*.md", "*.toml"],
            db_root / "scripts":          ["*.py"],
            db_root / "scripts" / "indexers": ["*.py"],
            db_root / "scripts" / "utils":    ["*.py"],
        }
        write_listing(project_root, db_cfg, f"ai-building-blocks-database-{today}.txt")

if __name__ == "__main__":
    main()
