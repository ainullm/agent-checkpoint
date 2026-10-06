---
name: agent-checkpoint
description: >-
  Zero-data-loss file snapshotting, SemVer classification, and dual-ledger audit trail
  for autonomous AI coding & research agents.
  Triggers on: checkpoint, snapshot, audit trail, versioning, edit file, refactor,
  trackback, history, revision log, rollback, diff version.
---

# Agent-Checkpoint Protocol

A universal, zero-dependency audit and safety protocol for autonomous AI coding and research agents.

## Core Directives

1. **Zero Data Loss (Pre-Edit Archiving):** Never modify, refactor, or overwrite an existing file without archiving its exact prior state.
2. **Dual-Ledger Synchronization:**
   - **Machine Index (`.snapshots/manifest.json`):** Fast, compact JSON array enabling agents to discover past revisions and calculate diffs without token bloat.
   - **Human-Readable Audit Trail (`REVISION_LOG.md`):** Rich Markdown changelog detailing timestamps, SemVer impacts, rationale, and bullet-point changes.
3. **Safety & Storage Guardrails:**
   - **Always Snapshot:** Plain-text documents (`.md`, `.tex`, `.rst`, `.txt`), source code (`.py`, `.ts`, `.js`, `.go`, `.rs`, `.cpp`, `.sh`), configurations (`.json`, `.yaml`, `.yml`, `.toml`, `.env.example`).
   - **Never Snapshot (Strict Exclusion):**
     - Heavy binary assets (models `.pt`, `.pth`, `.onnx`, `.bin`, `.safetensors`, `.ckpt`)
     - Large datasets (`.csv > 5MB`, `.parquet`, `.h5`, `.zip`, `.tar.gz`)
     - Build artifacts & dependency caches (`node_modules/`, `venv/`, `.venv/`, `__pycache__/`, `dist/`, `build/`, `.git/`)

---

## Standard Directory Layout

```text
[Project_Root]/
├── .snapshots/                          # Historical snapshots directory
│   ├── manifest.json                    # Machine-readable registry (< 5ms parsing)
│   └── <filename>_v<OLD_VERSION>.<ext>  # Exact copy of previous state
├── REVISION_LOG.md                      # Human-readable audit log
├── <active_file_1>.<ext>                # Current working file
└── <active_file_2>.<ext>
```

---

## Operating Procedures (SOP)

### Workflow 1: File Modification & Checkpointing

Whenever instructed to modify, refactor, or update an existing file:

1. **Step 1: Check Current Version**
   - For new files: Register initial creation as `v1.0.0` (or `v0.1.0` if draft).
   - For existing files: Consult `.snapshots/manifest.json` for the latest recorded version.

2. **Step 2: Classify Version Bump (Semantic Impact)**
   - **MAJOR (`v(X+1).0.0`):** Paradigm shift, architectural overhaul, breaking API contract, or chapter restructuring.
   - **MINOR (`vX.(Y+1).0`):** New feature, new experimental methodology, added baseline, or new sub-section.
   - **PATCH (`vX.Y.(Z+1)`):** Bug fix, typo correction, parameter tuning, or styling cleanup.

3. **Step 3: Capture Snapshot**
   - Ensure `.snapshots/` exists.
   - Copy current active file to:
     `.snapshots/<filename_without_ext>_v<OLD_VERSION>.<ext>`

4. **Step 4: Apply Modification**
   - Perform the requested edit on the active file.

5. **Step 5: Synchronize Dual-Ledger**
   - **Append to `.snapshots/manifest.json`**:
     ```json
     {
       "version": "1.1.0",
       "file": "relative/path/to/file.ext",
       "snapshot": ".snapshots/file_v1.0.0.ext",
       "type": "MINOR",
       "timestamp": "ISO-8601 string",
       "rationale": "Clear scientific or engineering justification for the edit",
       "changes": [
         "Key modification point 1",
         "Key modification point 2"
       ]
     }
     ```
   - **Append to `REVISION_LOG.md`**:
     ```markdown
     ## [v1.1.0] - YYYY-MM-DD HH:MM:SS
     - **Target File:** `relative/path/to/file.ext`
     - **Change Type:** MINOR
     - **Archived Snapshot:** `.snapshots/file_v1.0.0.ext`
     - **Rationale:** [Scientific / engineering reason]
     - **Key Changes:**
       - [Bullet point 1]
       - [Bullet point 2]
     ---
     ```

---

### Workflow 2: Trackback & Deep Semantic Diff

When requested to review, inspect, or compare past revisions:

1. Read `.snapshots/manifest.json` to find the target version and its snapshot location.
2. Read the historical snapshot (`.snapshots/file_vX.Y.Z.ext`) and the active file.
3. Perform comparative analysis:
   - Identify behavioral regressions or removed invariants.
   - Verify if modifications align with the stated rationale.
   - Present a structured Before vs After summary table or Mermaid diagram.

---

### Workflow 3: Safe Rollback / State Recovery

When requested to revert or restore an earlier version:

1. Locate the target version snapshot in `.snapshots/`.
2. Take a safety backup of the *current* state as a PATCH bump (ensuring work-in-progress is never lost).
3. Overwrite the active file with the content of the historical snapshot.
4. Record the restoration event in `REVISION_LOG.md` and `manifest.json`.
