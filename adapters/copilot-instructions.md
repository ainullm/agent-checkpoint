# AGENT-CHECKPOINT PROTOCOL v2.0 (GitHub Copilot)
# Place this file at .github/copilot-instructions.md

Always adhere to the Agent-Checkpoint v2.0 protocol:
- Pre-Edit Bucketing: Copy the pre-edit file into `.snapshots/<filepath>/v<OLD_VERSION>.<ext>`.
- Sliding Window Retention: Retain maximum 5 latest versions per file bucket.
- SemVer Impact: Mark change as MAJOR (structural shift), MINOR (additive feature), or PATCH (refinement/fix).
- Dual-Ledger Trail: Maintain sharded index at `.snapshots/<filepath>/manifest.json` and append 1 line to `REVISION_LOG.md` table without reading old history.
- Safety: Exclude heavy binaries, models, datasets > 1 MB, and dependencies.
