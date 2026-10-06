# AGENT-CHECKPOINT PROTOCOL v2.0 (Antigravity / Gemini CLI)
# Add this section to your project's AGENTS.md or ~/.gemini/AGENTS.md

## FILE MODIFICATION & AUDIT TRAIL PROTOCOL
When modifying, refactoring, or updating existing files in this workspace:
1. BUCKETED PRE-EDIT SNAPSHOT: Before modifying any existing text, code, or document, copy its prior state to `.snapshots/<filepath>/v<OLD_VERSION>.<ext>`.
2. SLIDING WINDOW RETENTION: Retain at most 5 latest snapshots per file bucket. Automatically prune older snapshots.
3. IMPACT CLASSIFICATION: Classify change into MAJOR (architectural), MINOR (additive feature), or PATCH (bugfix/typo).
4. TOKEN-OPTIMIZED DUAL-LEDGER:
   - Update sharded local index at `.snapshots/<filepath>/manifest.json` (< 40 tokens).
   - Append 1 line to `REVISION_LOG.md` using the compact Markdown table without reading historical logs.
5. SAFETY EXCLUSIONS: Never snapshot heavy binary assets (models, datasets > 1 MB) or caches (`node_modules`, `venv`, `__pycache__`, `.git`).
