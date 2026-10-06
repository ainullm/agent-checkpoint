# AGENT-CHECKPOINT PROTOCOL (Claude Code)
# Place this file as CLAUDE.md at your repository root.

## Autonomous Editing & Checkpointing Rules
Before modifying or rewriting any existing file:
1. ALWAYS archive the exact pre-edit file into `.snapshots/<filename>_v<OLD_VERSION>.<ext>`.
2. Determine Semantic Impact:
   - MAJOR: Breaking architecture/pipeline overhaul.
   - MINOR: Additive feature, new module, or new section.
   - PATCH: Small fix, refactor, or tuning.
3. Update `.snapshots/manifest.json` with version, timestamp, rationale, and changed points.
4. Append an entry to `REVISION_LOG.md` explaining WHY the modification was made.
5. EXCLUSION RULE: Strictly exclude binary weights (.pt, .onnx), large data (>1MB), and caches (node_modules, venv, __pycache__).
