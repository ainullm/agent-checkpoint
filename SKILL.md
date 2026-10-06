---
name: agent-checkpoint
description: >-
  Ultra-efficient, zero-data-loss pre-edit snapshotting, SemVer classification,
  and token-optimized dual-ledger audit trail (v2.0) for autonomous AI coding agents.
  Triggers on: agent-checkpoint, checkpoint, snapshot, audit trail, versioning, edit file,
  refactor, trackback, history, revision log, rollback, diff version.
---

# Agent-Checkpoint Protocol (v2.0 Turbo)

A universal, zero-dependency safety and provenance protocol for autonomous AI coding and research agents, optimized for **minimum token consumption** and **clean hierarchical storage**.

## Core Directives

1. **Zero Data Loss (Pre-Edit Archiving):** Never modify, refactor, or overwrite an existing file without archiving its exact prior state.
2. **Hierarchical File Bucketing (Clean Storage):**
   Every tracked file receives its own isolated directory inside `.snapshots/` matching its relative project path:
   ```text
   .snapshots/<relative_filepath>/
   ├── manifest.json            # Sharded local index (< 40 tokens read)
   ├── v1.0.0.<ext>             # Pristine pre-edit snapshot
   └── v1.1.0.<ext>
   ```
3. **Sliding Window Retention ($K = 5$ Versions Max):**
   To strictly bound disk space, each file bucket retains at most **5 latest snapshot versions**. When creating version 6, the agent automatically prunes the oldest physical snapshot file and updates the bucket's `manifest.json`.
4. **Token-Optimized Dual-Ledger Synchronization:**
   - **Sharded Local Index (`.snapshots/<filepath>/manifest.json`):** AI reads *only* this file's version state ($O(1)$ token overhead: ~30–50 tokens), avoiding global scans.
   - **Micro-Changelog Stream (`REVISION_LOG.md`):** Append-only compact table stream. **Never re-read previous log history** into context.
5. **Universal Scope & Guardrails:**
   - Full text/code coverage across 100+ extensions (`.py`, `.ts`, `.go`, `.rs`, `.cpp`, `.md`, `.json`, `.yaml`, etc.).
   - Tabular files (`.csv`, `.tsv`, `.jsonl`) are snapshotted ONLY if $\le 1\text{ MB}$. Files $> 1\text{ MB}$ log metadata only.
   - Strictly exclude binary models (`.pt`, `.onnx`, `.safetensors`), archives (`.zip`), and caches (`node_modules/`, `venv/`, `__pycache__/`, `.git/`).

---

## Standard Directory Layout

```text
[Project_Root]/
├── .snapshots/                          # Historical snapshots directory
│   ├── auth_service.py/                 # Isolated bucket per file
│   │   ├── manifest.json                # Local version registry (< 40 tokens)
│   │   ├── v1.0.0.py                    # Archived pre-edit snapshot
│   │   └── v1.1.0.py
│   └── src/routes/api.ts/               # Preserves nested structure
│       ├── manifest.json
│       └── v1.0.0.ts
├── REVISION_LOG.md                      # Append-only compact Markdown table
├── auth_service.py                      # Active working file
└── src/routes/api.ts
```

---

## Operating Procedures (SOP)

### Workflow 1: File Modification & Checkpointing (Fast-Path)

Whenever instructed to modify, refactor, or update an existing file:

1. **Step 1: Check Local Bucket (`.snapshots/<filepath>/manifest.json`)**
   - If bucket or file does not exist: treat as initial version (`v1.0.0`).
   - If exists: read latest version from the local `manifest.json` (< 40 tokens).

2. **Step 2: Classify SemVer Impact**
   - **MAJOR:** Breaking architectural shift, interface overhaul.
   - **MINOR:** Additive features, new endpoints/functions.
   - **PATCH:** Bug fix, refactor, parameter tuning, typo.

3. **Step 3: Capture Pre-Edit Snapshot & Apply Retention ($K \le 5$)**
   - Ensure directory `.snapshots/<filepath>/` exists.
   - Copy current active file to `.snapshots/<filepath>/v<OLD_VERSION>.<ext>`.
   - *Sliding Window Check:* If total snapshot files in bucket $> 5$, delete the oldest snapshot.

4. **Step 4: Apply Modification to Active File**
   - Apply user's requested edit on the active file.

5. **Step 5: Synchronize Dual-Ledger (Micro-Log Stream)**
   - Update `.snapshots/<filepath>/manifest.json`:
     ```json
     [
       {"version": "v1.1.0", "snapshot": "v1.0.0.py", "impact": "MINOR", "ts": "2026-10-07T03:45:00+07:00", "summary": "Added JWT refresh token"}
     ]
     ```
   - Append 1 line to `REVISION_LOG.md` without reading previous entries:
     ```markdown
     | 2026-10-07 03:45 | v1.1.0 | MINOR | auth_service.py | v1.0.0.py | Added JWT refresh token |
     ```

---

### Workflow 2: Deep Trackback & Semantic Diff

When requested to review or compare past revisions:
1. Read `.snapshots/<filepath>/manifest.json` to identify available snapshot versions.
2. Load target snapshot (e.g. `.snapshots/<filepath>/v1.0.0.<ext>`) and active file.
3. Present concise Before vs After comparison highlighting algorithmic or interface changes.

---

### Workflow 3: Instant Rollback / Recovery

When requested to revert or restore an earlier version:
1. Locate target snapshot in `.snapshots/<filepath>/v<TARGET_VERSION>.<ext>`.
2. Take safety snapshot of the *current* state (ensuring work-in-progress is never lost).
3. Overwrite active file with content from the snapshot.
4. Append 1-line rollback event to `REVISION_LOG.md`.
