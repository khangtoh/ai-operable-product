# Changelog

All notable changes to the AI-Operable Product skill package are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and version numbers
follow [Semantic Versioning](https://semver.org/) applied to the skill package as a whole:

- **MAJOR** — a breaking change to the seven-primitive model, the AI-OPERABLE DONE criteria, the
  Default Output structure, or any `schemas/*.schema.json` contract (fields removed/renamed, required
  fields added, semantics changed). Consumers relying on prior output shape or reasoning steps would
  need to adapt.
- **MINOR** — backward-compatible additions: new reference material, templates, examples, evals,
  optional schema fields, or expanded guidance that doesn't change existing behavior or output shape.
- **PATCH** — wording clarifications, typo fixes, doc/README updates, and other changes that don't
  alter the skill's instructions, reasoning steps, or output contract.

`SKILL.md` (root) and `.claude/skills/ai-operable-product/SKILL.md` carry the same `version` in their
frontmatter and are bumped together — the project-level copy governs by deferring to the canonical
root file, so it always ships at the same version. `scripts/validate_package.py` checks that both
files and this changelog agree.

## [Unreleased]

## [1.0.0] - 2026-08-28

Baseline release. First tracked version of the package as it already existed prior to versioning
being introduced.

### Added
- Canonical `SKILL.md` defining the seven operating primitives (Outcome Intent, Journey Context,
  Workflow Map, Recovery Path, Policy Boundary, Safe Actions, Feedback Loop), the Mandatory Context
  Gate, the Required Input Contract, the phased construction flow, and the AI-OPERABLE DONE criteria.
- Project-level Claude Code skill entrypoint at `.claude/skills/ai-operable-product/SKILL.md`.
- Reference material under `references/` (operating primitives, product operating context, evidence
  fabric, product state, AI-OPERABLE DONE).
- JSON schemas under `schemas/` for product context, evidence source, and product state.
- YAML templates under `templates/` for product context, source inventory, and product state.
- Worked examples under `examples/` (Digital Lending, TD Promotion).
- Evaluation scenarios under `evals/scenarios.md`.
- Platform installation guides for ChatGPT and Claude under `platforms/`.
- `scripts/validate_package.py` structural validator.
