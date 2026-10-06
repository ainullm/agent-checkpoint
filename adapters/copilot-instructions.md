# AGENT-CHECKPOINT PROTOCOL (GitHub Copilot)
# Place this file at .github/copilot-instructions.md

Always adhere to the Agent-Checkpoint protocol:
- Pre-Edit Snapshot: Before editing any existing file, copy the pre-edit file into `.snapshots/<filename>_v<OLD_VERSION>.<ext>`.
- SemVer Impact: Mark change as MAJOR (structural shift), MINOR (additive feature), or PATCH (refinement/fix).
- Dual-Ledger Trail: Maintain machine index at `.snapshots/manifest.json` and human audit log at `REVISION_LOG.md`.
- Safety: Exclude heavy binaries, models, datasets, and dependencies from `.snapshots/`.
