# Revision Log & Provenance Audit Trail

This repository adheres to the [Agent-Checkpoint Protocol](https://github.com/ainullm/agent-checkpoint). All historical modifications are synchronized across this log and `.snapshots/manifest.json`.

---

## [2026-10-06 21:20:00 +07:00] - Documentation Expansion: Usage Workflows & Storage Economics
* **Files Modified:** `README.md`, `README.id.md`
* **SemVer Impact:** `MINOR` (`v1.0.0` $\to$ `v1.1.0`)
* **Pre-Edit Snapshots:**
  * `.snapshots/README_v1.0.0.md`
  * `.snapshots/README.id_v1.0.0.md`
* **Rationale:**
  * Provided comprehensive, concrete developer workflows (Feature refactor, Emergency rollback, Trackback semantic diff, and Multi-file batch edits).
  * Added Git integration strategies distinguishing between Team Audit Trail (commit `.snapshots/`) and Local Scratchpad (`.gitignore` `.snapshots/`).
  * Added empirical storage economics modeling table across 4 developer personas (Casual, Full-time, Heavy pair programming, and Autonomous bot).
  * Documented 1-line retention and pruning commands for PowerShell and Bash.
