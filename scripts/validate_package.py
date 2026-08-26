#!/usr/bin/env python3
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "SKILL.md",
    root / "README.md",
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

if errors:
    print("Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Package validation passed.")
