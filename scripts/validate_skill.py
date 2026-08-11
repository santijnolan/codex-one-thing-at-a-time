#!/usr/bin/env python3

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "one-thing-at-a-time"
SKILL_FILE = SKILL_DIR / "SKILL.md"
OPENAI_FILE = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) != 3:
        fail("SKILL.md frontmatter is not closed")

    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        fail("SKILL.md frontmatter must be a mapping")
    return data


def main() -> None:
    if not SKILL_FILE.is_file():
        fail(f"missing {SKILL_FILE.relative_to(ROOT)}")
    if not OPENAI_FILE.is_file():
        fail(f"missing {OPENAI_FILE.relative_to(ROOT)}")

    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    metadata = load_frontmatter(skill_text)

    if set(metadata) != {"name", "description"}:
        fail("frontmatter must contain only name and description")
    if metadata["name"] != SKILL_DIR.name:
        fail("frontmatter name must match the skill directory")
    if not isinstance(metadata["description"], str) or len(metadata["description"]) < 80:
        fail("description must explain behavior and triggering contexts")
    if "TODO" in skill_text:
        fail("SKILL.md still contains TODO text")

    private_markers = ("/Users/", "/home/", "file://")
    for marker in private_markers:
        if marker.lower() in skill_text.lower():
            fail(f"private or project-specific marker found: {marker}")

    openai_data = yaml.safe_load(OPENAI_FILE.read_text(encoding="utf-8"))
    interface = openai_data.get("interface") if isinstance(openai_data, dict) else None
    if not isinstance(interface, dict):
        fail("agents/openai.yaml must contain an interface mapping")

    for field in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(field), str) or not interface[field].strip():
            fail(f"interface.{field} must be a non-empty string")

    if "$one-thing-at-a-time" not in interface["default_prompt"]:
        fail("default_prompt must explicitly mention $one-thing-at-a-time")

    print("Skill package is valid.")


if __name__ == "__main__":
    main()
