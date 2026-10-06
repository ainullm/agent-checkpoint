# AGENT-CHECKPOINT PROTOCOL (Antigravity / Gemini CLI)
# Add this section to your project's AGENTS.md or ~/.gemini/AGENTS.md

## FILE MODIFICATION & AUDIT TRAIL PROTOCOL
When modifying, refactoring, or updating existing files in this workspace:
1. PRE-EDIT SNAPSHOT: Before modifying any existing text, code, or research document, copy its prior state to `.snapshots/<filename>_v<OLD_VERSION>.<ext>`.
2. IMPACT CLASSIFICATION: Classify the change into:
   - MAJOR: Paradigm shift, architectural overhaul, breaking API contract.
   - MINOR: New feature, new experimental methodology, added baseline.
   - PATCH: Bug fix, typo correction, parameter tuning, editorial cleanup.
3. DUAL-LEDGER LOGGING:
   - Synchronize `.snapshots/manifest.json` (fast machine index).
   - Append to `REVISION_LOG.md` (human-readable audit trail with rationale and bullet-point diffs).
4. SAFETY EXCLUSIONS: Never snapshot heavy binary assets (models, large datasets) or cache directories (`node_modules`, `venv`, `__pycache__`, `.git`).
5. DEEP TRACKBACK: When asked to review past changes or compare versions, read historical snapshots from `.snapshots/` and conduct comparative semantic analysis.
