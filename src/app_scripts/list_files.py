#!/usr/bin/env python3
import sys
import json
from pathlib import Path
from datetime import date

def list_files_in(dirpath: Path, patterns: list[str]) -> list[Path]:
    files = []
    for pat in patterns:
        files.extend(dirpath.glob(pat))
    return sorted(f for f in files if f.is_file())

def build_manifest(root: Path):
    proj = root.name
    today = date.today().strftime("%Y%m%d")

    if proj == "ai-building-blocks-agent":
        config = {
            "root":                   ["*.md"],
            "app":                    ["*.py"],
            "app/llm":                ["*.py"],
            "app/llm/routers":        ["*.py"],
            "retrievers":             ["*.py"],
            "scripts":                ["*.py"],
            "scripts/utils":          ["*.py"],
            "static":                 ["*.html"],
            "tools":                  ["*.py"],
        }
        outname = f"ai-building-blocks-agent-{today}.json"

    elif proj == "ai-building-blocks-database":
        config = {
            "root":                   ["*.md", "*.toml"],
            "scripts":                ["*.py"],
            "scripts/indexers":       ["*.py"],
            "scripts/utils":          ["*.py"],
        }
        outname = f"ai-building-blocks-database-{today}.json"

    else:
        sys.exit(f"⚠️  Unrecognized project folder: {proj}")

    manifest = []
    for rel_dir, patterns in config.items():
        dirpath = root if rel_dir == "root" else root / rel_dir
        for file in list_files_in(dirpath, patterns):
            try:
                content = file.read_text(encoding="utf-8")
            except Exception as e:
                content = f"<error reading file: {e}>"
            manifest.append({
                "path": str(file.relative_to(root)),
                "content": content
            })

    # write JSON
    with open(outname, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Wrote JSON manifest to {outname}")

if __name__ == "__main__":
    build_manifest(Path.cwd())
