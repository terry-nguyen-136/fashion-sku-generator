# AGENTS.md — AI coding agent instructions

Purpose
- Help AI coding agents quickly understand this repo and follow project conventions.

Quick facts
- Tests: run with `pip install -r requirements.txt` then `pytest` from the repo root.
- Package layout: Python package under `src/`. Tests import `src.*`.
- Dependencies: see [requirements.txt](requirements.txt).

Type-checking guidance (Python Analysis Type Checking Mode)
- Follow repo configs if present: if `pyrightconfig.json`, `pyproject.toml`, `.pylintrc`, or other type-checker config files exist, obey them.
- Default behavior when no config is present (this repo): use `python.analysis.typeCheckingMode = "basic"`.
  - Rationale: this repo uses Pydantic models and has limited explicit type coverage; `basic` catches common issues without requiring full strict typing across all files.
  - When to use `strict`: only enable `strict` if you add comprehensive type annotations and update tests to cover type-heavy changes.
- How to run checks locally:
  - Install tools: `pip install pyright` (or use VS Code Pylance for editor checks).
  - Run `pyright` from repo root when present, or rely on VS Code `python.analysis.typeCheckingMode` setting for on-the-fly feedback.

Agent behavior rules
- Do not change global type-checker settings in the repo without explicit user approval.
- If you add a `pyrightconfig.json` or `mypy.ini`, update this file and explain the change in the PR description.
- Prefer small, well-tested changes. Run tests after editing code and before proposing `strict` mode.

Files to reference
- README: [README.md](README.md)
- Tests: [tests/test_sku_builder.py](tests/test_sku_builder.py)
- Sources: [src/models.py](src/models.py), [src/sku_builder.py](src/sku_builder.py)

Next suggestions
- Consider adding `pyrightconfig.json` if you want stricter, repo-wide type checking.
- Add a CI job that runs `pyright` and `pytest` to guard type and behavior regressions.
