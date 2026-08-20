#!/usr/bin/env python3
"""Scaffold a learned skill produced from an agent-watch session."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize_name(value: str) -> str:
    name = value.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"-{2,}", "-", name).strip("-")
    if not name:
        raise SystemExit("Skill name cannot be empty after normalization")
    if len(name) > 64:
        raise SystemExit("Skill name must be 64 characters or fewer")
    return name


def title_case(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a scaffold for a learned skill distilled from a watch session."
    )
    parser.add_argument("name", help="Desired skill name or title")
    parser.add_argument(
        "--path",
        default=str(Path.home() / ".codex" / "skills"),
        help="Root directory where the skill folder should be created",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files",
    )
    args = parser.parse_args()

    name = normalize_name(args.name)
    title = title_case(name)
    root = Path(args.path).expanduser().resolve()
    skill_dir = root / name
    refs_dir = skill_dir / "references"
    agents_dir = skill_dir / "agents"

    skill_md = f"""---
name: {name}
description: [TODO: Describe the exact learned method from the watch session, what this skill does, and when to use it.]
---

# {title}

Use this skill to apply the exact learned method captured from the source watch session.

Do not genericize the method.

## Workflow

1. Read `references/source-notes.md`.
2. Reconstruct the exact sequence, constraints, cues, and failure modes from the source.
3. Apply the method faithfully unless the user explicitly asks for adaptation.

## Rules

- Preserve source-specific terminology and sequencing.
- Prefer observed cues over generic advice.
- Keep the scope narrow and operational.
"""

    openai_yaml = f"""interface:
  display_name: "{title}"
  short_description: "Apply one learned method faithfully"
  default_prompt: "Use ${name} to apply the exact method learned from the source watch session instead of giving generic advice."
"""

    source_notes = """# Source Notes

## Source

- video or file:
- creator:
- date watched:

## Key timestamps

- 

## Sequence

1. 

## Critical cues

- 

## Mistakes to avoid

- 

## Terms and constraints worth preserving

- 
"""

    if skill_dir.exists() and not args.force:
        if any(skill_dir.iterdir()):
            raise SystemExit(
                f"Skill directory already exists and is not empty: {skill_dir}\n"
                "Use --force if you want to overwrite scaffold files."
            )

    skill_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)
    agents_dir.mkdir(parents=True, exist_ok=True)

    if args.force:
        (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
        (agents_dir / "openai.yaml").write_text(openai_yaml, encoding="utf-8")
        (refs_dir / "source-notes.md").write_text(source_notes, encoding="utf-8")
    else:
        write_if_missing(skill_dir / "SKILL.md", skill_md)
        write_if_missing(agents_dir / "openai.yaml", openai_yaml)
        write_if_missing(refs_dir / "source-notes.md", source_notes)

    print(skill_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
