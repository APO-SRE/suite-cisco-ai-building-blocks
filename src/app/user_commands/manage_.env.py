#!/usr/bin/env python3
from __future__ import annotations
###############################################################################
# manage_.env.py — interactive .env editor (headings, secrets, save/quit)
###############################################################################
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

from rich.console   import Console
from rich.table     import Table
from rich.prompt    import Prompt
from rich.panel     import Panel
from rich.traceback import install

from app.utils.paths import REPO_ROOT  # project helper

# ───────────────────────── configuration ────────────────────────────────────
ENV_PATH = (REPO_ROOT / ".env").resolve()
console  = Console()
install()

SECRET_RE  = re.compile(r"(KEY|TOKEN|SECRET|PASSWORD|API_KEY)$", re.I)
SECTION_RE = re.compile(r"#\s+([0-9]+(?:\.[0-9]+)*)\)\s*(.+)")
HR_79      = re.compile(r"^#{79}$")

# ───────────────────────── helpers ──────────────────────────────────────────
def load_env_raw() -> List[str]:
    return ENV_PATH.read_text(encoding="utf-8", errors="ignore").splitlines()

def save_env_raw(lines: List[str]) -> None:
    ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

def mask(k: str, v: str) -> str:
    """Hide secrets when displaying."""
    return "•••• (hidden)" if SECRET_RE.search(k) else v

def split_sections(lines: List[str]) -> dict[str, Tuple[int, int]]:
    """
    Return {section-title: (start, end)} based on '# 2.1) Title' markers.
    Keeps 'GLOBAL' for top-of-file content (before first marker).
    """
    spans, current, start = {}, "GLOBAL", 0
    for idx, ln in enumerate(lines):
        if HR_79.match(ln):
            continue
        m = SECTION_RE.match(ln)
        if m:
            spans[current] = (start, idx)
            current, start = f"{m.group(1)} {m.group(2)}", idx
    spans[current] = (start, len(lines))
    return spans

def extract_pairs(lines: List[str], start: int, end: int) -> List[Tuple[str, str, str, int, Optional[int]]]:
    """
    Return [(key, value, allowed, line_idx, allowed_line_idx), ...] within a section.
    - 'allowed' is any comment on the line(s) immediately preceding the KEY=VALUE line,
      if it begins with '# Allowed:'.
    - 'allowed_line_idx' is the index of that comment line in 'lines', or None if none exists.
    """
    pairs = []
    idx = start
    pending_allowed: Optional[str] = None
    pending_allowed_idx: Optional[int] = None

    while idx < end:
        raw = lines[idx].rstrip()
        stripped = raw.lstrip()
        # Detect an "Allowed" comment
        if stripped.startswith("#"):
            comment = stripped[1:].strip()
            if comment.lower().startswith("allowed:"):
                # Capture everything after "Allowed:"
                pending_allowed = comment[len("allowed:"):].strip()
                pending_allowed_idx = idx
                idx += 1
                continue
        # Now detect a KEY=VALUE line
        if "=" in stripped and not stripped.startswith("#"):
            k, v = stripped.split("=", 1)
            allowed = pending_allowed or ""
            allowed_idx = pending_allowed_idx
            pairs.append((k.strip(), v.strip(), allowed, idx, allowed_idx))
            # Reset pending_allowed
            pending_allowed = None
            pending_allowed_idx = None
        idx += 1

    return pairs

# ───────────────────────── edit-screen ──────────────────────────────────────
def edit_section(name: str, lines: List[str], start: int, end: int) -> None:
    pairs = extract_pairs(lines, start, end)
    dirty = False  # Track unsaved changes

    while True:
        console.clear()

        tbl = Table(title=f"[bold cyan]{name}[/bold cyan]")
        tbl.add_column("No.",    style="bold",         justify="right")
        tbl.add_column("Key",    style="bright_blue")
        tbl.add_column("Value")
        tbl.add_column("Allowed", style="dim")

        for n, (k, v, allowed, _, _) in enumerate(pairs, 1):
            tbl.add_row(str(n), k, mask(k, v), allowed or "-")

        console.print(tbl)

        legend = (
            "[bold cyan]E[/bold cyan]dit   "
            "[bold green]A[/bold green]dd   "
            "[bold red]D[/bold red]elete   "
            "[bold yellow]S[/bold yellow]ave   "
            "[bold magenta]B[/bold magenta]ack   "
            "[bold white]Q[/bold white]uit"
        )
        console.print(legend)

        cmd = Prompt.ask("Enter command (e/a/d/s/b/q)", default="b").lower()

        if cmd == "q":
            if dirty:
                confirm = Prompt.ask(
                    "[red]Unsaved changes will be lost. Quit anyway? (y/n)[/red]",
                    choices=["y", "n"], default="n"
                )
                if confirm == "n":
                    continue
            sys.exit(0)

        if cmd == "b":
            if dirty:
                confirm = Prompt.ask(
                    "[red]Unsaved changes will be lost. Go back anyway? (y/n)[/red]",
                    choices=["y", "n"], default="n"
                )
                if confirm == "n":
                    continue
            break

        if cmd == "s":
            save_env_raw(lines)
            console.print("[green]✔ Saved[/green]")
            dirty = False
            Prompt.ask("Press Enter to continue")
            continue

        if cmd in {"e", "d"}:
            row = Prompt.ask("Enter row number", default="")
            if not row.isdigit() or not 1 <= int(row) <= len(pairs):
                continue
            pos = int(row) - 1
            key, val, allowed, line_idx, allowed_idx = pairs[pos]

            if cmd == "d":
                # Comment out the KEY=VALUE line
                lines[line_idx] = "#" + lines[line_idx]
                # Comment out the "Allowed" line if present
                if allowed_idx is not None:
                    lines[allowed_idx] = "#" + lines[allowed_idx]
                pairs.pop(pos)
                dirty = True

            else:  # Edit
                field = Prompt.ask(
                    "Edit [b]K[/b]ey, [b]V[/b]alue, or [b]A[/b]llowed?",
                    choices=["k", "v", "a"], default="v"
                ).lower()

                if field == "k":
                    new_k = Prompt.ask("New key", default=key)
                    lines[line_idx] = f"{new_k}={val}"
                    pairs[pos] = (new_k, val, allowed, line_idx, allowed_idx)
                    dirty = True

                elif field == "v":
                    new_v = Prompt.ask(
                        "New value",
                        default=("" if SECRET_RE.search(key) else val),
                        password=bool(SECRET_RE.search(key)),
                    )
                    lines[line_idx] = f"{key}={new_v}"
                    pairs[pos] = (key, new_v, allowed, line_idx, allowed_idx)
                    dirty = True

                else:  # field == "a" (Allowed)
                    new_allowed = Prompt.ask(
                        "New allowed values (comma-separated)",
                        default=allowed
                    ).strip()
                    if allowed_idx is not None:
                        # Replace existing comment line
                        lines[allowed_idx] = f"# Allowed: {new_allowed}"
                    else:
                        # Insert a new comment line just above the KEY=VALUE
                        lines.insert(line_idx, f"# Allowed: {new_allowed}")
                        # Adjust all subsequent indices
                        for i in range(len(pairs)):
                            k_i, v_i, a_i, l_i, ai_i = pairs[i]
                            if l_i >= line_idx:
                                new_l = l_i + 1
                                new_ai = ai_i + 1 if ai_i is not None else line_idx
                                pairs[i] = (k_i, v_i, a_i, new_l, new_ai)
                        allowed_idx = line_idx
                        line_idx += 1
                    pairs[pos] = (key, val, new_allowed, line_idx, allowed_idx)
                    dirty = True

        elif cmd == "a":
            new_k = Prompt.ask("New key", default="")
            new_v = Prompt.ask("New value", password=bool(SECRET_RE.search(new_k)))
            new_allowed = Prompt.ask("Allowed values (comma-separated)", default="").strip()

            # Insert allowed comment if provided
            if new_allowed:
                lines.insert(end, f"# Allowed: {new_allowed}")
                allowed_line = end
                end += 1
            else:
                allowed_line = None

            # Insert the KEY=VALUE line
            lines.insert(end, f"{new_k}={new_v}")
            pairs.append((new_k, new_v, new_allowed, end, allowed_line))
            end += 1
            dirty = True

# ───────────────────────── main-menu ────────────────────────────────────────
BANNER = """
[bold magenta]
╔════════════════════════════════════════════════════════════╗
║              Cisco AI Building Blocks – .env Editor        ║
╚════════════════════════════════════════════════════════════╝
[/bold magenta]
DO NOT USE IN PRODUCTION! NOT SECURE!
"""

def main() -> None:
    console.clear()  # Clear screen before anything is printed
    lines    = load_env_raw()
    sections = split_sections(lines)

    while True:
        console.clear()
        console.print(BANNER)

        # We will build two separate lists of display‐strings:
        #   left_display  := everything whose "major" ≤ 3
        #   right_display := everything whose "major" ≥ 4
        #
        #   Headings (e.g. “1 PLATFORM-WIDE / GLOBAL SETTINGS”) become bright_white text.
        #   Non-headings get a running index, with [cyan]N[/] - section_title.

        left_display:  List[str] = []
        right_display: List[str] = []
        index_map:     dict[str, str] = {}
        last_left_major:  Optional[str] = None
        last_right_major: Optional[str] = None
        next_index = 1

        # First pass: determine which column each section belongs to
        for title in sections:
            if title == "GLOBAL":
                continue  # skip the top‐of‐file “GLOBAL” entry

            num_token = title.split()[0]  # e.g. '3.4' or '4.0'
            major_part = num_token.split(".")[0]
            # Major might not parse if SECTION_RE was too loose—but we skip if non-integer
            try:
                major = int(major_part)
            except ValueError:
                continue

            heading = ("." not in num_token) or num_token.endswith(".0")

            if major <= 3:
                # Left-column logic
                if last_left_major is not None and str(major) != last_left_major:
                    left_display.append("")  # blank line between major groups
                if heading:
                    pretty = " ".join(title.split()[1:])
                    left_display.append(f"[bold bright_white]{pretty}[/bold bright_white]")
                else:
                    idx = str(next_index)
                    index_map[idx] = title
                    left_display.append(f"[cyan]{idx}[/cyan] - {title}")
                    next_index += 1
                last_left_major = str(major)

            else:
                # Right-column logic
                if last_right_major is not None and str(major) != last_right_major:
                    right_display.append("")  # blank line between major groups
                if heading:
                    pretty = " ".join(title.split()[1:])
                    right_display.append(f"[bold bright_white]{pretty}[/bold bright_white]")
                else:
                    idx = str(next_index)
                    index_map[idx] = title
                    right_display.append(f"[cyan]{idx}[/cyan] - {title}")
                    next_index += 1
                last_right_major = str(major)

        # Now combine them row by row into a two-column Table
        max_rows = max(len(left_display), len(right_display))
        menu_table = Table.grid(padding=(0, 2))
        menu_table.add_column(ratio=1)
        menu_table.add_column(ratio=1)

        for i in range(max_rows):
            left_text  = left_display[i]  if i < len(left_display) else ""
            right_text = right_display[i] if i < len(right_display) else ""
            menu_table.add_row(left_text, right_text)

        # After both columns, append two blank lines and then the "[q] Quit" line
        menu_table.add_row("", "")
        menu_table.add_row("", "")
        menu_table.add_row("[white]Quit (q)[/white]", "")

        console.print(Panel(menu_table, title=".env sections", border_style="green"))

        choice = Prompt.ask("Select section (number) or 'q' to quit", default="").lower()
        if choice == "q":
            break
        if choice not in index_map:
            continue

        sel        = index_map[choice]
        start, end = sections[sel]
        edit_section(sel, lines, start, end)

# ───────────────────────── entry-point ───────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
