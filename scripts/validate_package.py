#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "SKILL.md",
    root / "README.md",
    root / "CHANGELOG.md",
    root / "schemas" / "product-context.schema.json",
    root / "schemas" / "evidence-source.schema.json",
    root / "schemas" / "product-state.schema.json",
    root / ".claude" / "skills" / "ai-operable-product" / "SKILL.md",
]
errors = []
for p in required:
    if not p.exists():
        errors.append(f"Missing: {p.relative_to(root)}")

skill = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md is missing YAML frontmatter")
if "name: ai-operable-product" not in skill:
    errors.append("SKILL.md missing expected name")
if "description:" not in skill:
    errors.append("SKILL.md missing description")

for schema_file in (root / "schemas").glob("*.json"):
    try:
        json.loads(schema_file.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"Invalid JSON {schema_file.name}: {e}")

# --- Versioning ---
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def frontmatter_version(text: str, label: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    frontmatter = text[4:end] if end != -1 else text[4:]
    m = re.search(r"^version:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    if not m:
        errors.append(f"{label} is missing a 'version' field in frontmatter")
        return None
    version = m.group(1).strip("'\"")
    if not SEMVER.match(version):
        errors.append(f"{label} version '{version}' is not valid semver (x.y.z)")
        return None
    return version

skill_copy_path = root / ".claude" / "skills" / "ai-operable-product" / "SKILL.md"
skill_copy = skill_copy_path.read_text(encoding="utf-8") if skill_copy_path.exists() else ""

root_version = frontmatter_version(skill, "SKILL.md")
copy_version = frontmatter_version(skill_copy, ".claude/skills/ai-operable-product/SKILL.md") if skill_copy else None

if root_version and copy_version and root_version != copy_version:
    errors.append(
        f"Version mismatch: SKILL.md is {root_version} but "
        f".claude/skills/ai-operable-product/SKILL.md is {copy_version}"
    )

changelog_path = root / "CHANGELOG.md"
if changelog_path.exists():
    changelog = changelog_path.read_text(encoding="utf-8")
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.MULTILINE)
    if not m:
        errors.append("CHANGELOG.md has no released version heading (## [x.y.z])")
    elif root_version and m.group(1) != root_version:
        errors.append(
            f"Version mismatch: SKILL.md is {root_version} but latest CHANGELOG.md "
            f"entry is {m.group(1)}"
        )

if errors:
    print("Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Package validation passed.")
