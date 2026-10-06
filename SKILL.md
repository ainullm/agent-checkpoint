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
3. **Universal Scope & Smart Storage Guardrails:**
   - **Full Text & Code Coverage (Always Snapshotted):**
     * Source Code & Scripts: Python (`.py`), TypeScript (`.ts`, `.tsx`), JavaScript (`.js`), Go (`.go`), Rust (`.rs`), C/C++ (`.c`, `.cpp`), Java, PHP, Ruby, Swift, Kotlin, Dart, Shell (`.sh`, `.ps1`), Lua, R, Julia.
     * Research & Notebooks: Jupyter Notebooks (`.ipynb`), Typst (`.typ`), LaTeX (`.tex`, `.bib`), Markdown (`.md`), RestructuredText (`.rst`).
     * Diagrams as Code: Mermaid (`.mmd`), PlantUML (`.puml`), Graphviz (`.dot`), SVG (`.svg`), Draw.io (`.drawio`), Excalidraw (`.excalidraw`).
     * API Schemas & Contracts: Protobuf (`.proto`), GraphQL (`.graphql`), Prisma (`.prisma`), OpenAPI (`.yaml`), Thrift (`.thrift`).
     * Graphics & Shaders: GLSL (`.glsl`), HLSL (`.hlsl`), WGSL (`.wgsl`), GDScript (`.gd`).
     * Hardware & Embedded: Verilog (`.v`, `.sv`), VHDL (`.vhd`), Assembly (`.asm`), Arduino (`.ino`), CMake.
     * Policies & Configs: OPA Rego (`.rego`), CUE (`.cue`), JSON, YAML, TOML, Dockerfile.
   - **Smart 1 MB Threshold for Tabular Data:**
     * Small data seeds/fixtures (`.csv`, `.tsv`, `.jsonl`) are snapshotted ONLY if file size $\le 1\text{ MB}$.
     * If file size $> 1\text{ MB}$, the agent logs the change metadata in `REVISION_LOG.md` and `manifest.json` (with `"snapshot": null, "reason": "exceeds_1mb_cap"`) without duplicating the raw file, strictly preventing disk bloat.
   - **Strict Exclusions (Never Snapshotted):**
     * Machine Learning weights & checkpoints (`.pt`, `.pth`, `.onnx`, `.bin`, `.safetensors`, `.ckpt`).
     * Large tabular data & binaries ($> 1\text{ MB}$, `.parquet`, `.h5`, `.arrow`, `.feather`).
     * Executables, libraries & archives (`.exe`, `.dll`, `.so`, `.zip`, `.tar.gz`, video/audio).
     * Dependency caches & build outputs (`node_modules/`, `venv/`, `.venv/`, `__pycache__/`, `target/`, `dist/`, `build/`, `.git/`).

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
