# AGENT-CHECKPOINT PROTOCOL v2.0 (Claude Code)
# Place this file as CLAUDE.md at your repository root.

## Autonomous Editing & Checkpointing Rules
Before modifying or rewriting any existing file:
1. ALWAYS archive the exact pre-edit file into `.snapshots/<filepath>/v<OLD_VERSION>.<ext>`.
2. RETENTION LIMIT: Keep at most 5 latest snapshots per file bucket. Prune older versions.
3. SEMVER IMPACT: Tag as MAJOR (breaking overhaul), MINOR (additive feature), or PATCH (small fix/refactor).
4. TOKEN-OPTIMIZED DUAL-LEDGER:
   - Update sharded index at `.snapshots/<filepath>/manifest.json`.
   - Append 1 line to `REVISION_LOG.md` table: `| <Date> | <Version> | <Impact> | <File> | <Snapshot> | <Rationale> |`
   - Never re-read historical `REVISION_LOG.md` entries into context.
5. EXCLUSION RULE: Strictly exclude binary weights (.pt, .onnx), datasets > 1 MB, and caches (node_modules, venv, __pycache__).
