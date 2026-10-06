<div align="center">

# 🛡️ Agent-Checkpoint

**Zero-data-loss file snapshotting, SemVer classification, and dual-ledger audit trail for autonomous AI coding & research agents.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![Cross Agent](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Windsurf%20%7C%20Copilot-orange.svg)]()
[![SemVer](https://img.shields.io/badge/Versioning-SemVer%202.0-blueviolet.svg)]()

---

**Languages:**  
[English (Current)](./README.md) • [🇮🇩 Bahasa Indonesia](./README.id.md)

---

</div>

## ⚡ The Problem: Destructive In-Place AI Overwrites

Autonomous AI coding agents (Cursor, Claude Code, Google Antigravity, Windsurf, GitHub Copilot, Aider) are accelerating software development and scientific research. However, almost every agent shares a dangerous default behavior: **they overwrite files in-place without preserving history**.

* ❌ **Silent Regression:** An AI agent refactors a module and inadvertently drops a critical edge case, business constraint, or formula.
* ❌ **Zero Paper Trail:** You return to your workspace without knowing *why* specific architectural decisions or parameter changes were made.
* ❌ **Irreversible Hallucination:** A misunderstood prompt causes the agent to wipe out hours of draft writing, LaTeX formulas, or working code.
* ❌ **Git Micro-Commit Noise:** Developers feel forced to make dozens of messy Git commits just to maintain an undo safety net.

---

## 💡 The Solution: The Agent-Checkpoint Protocol

**Agent-Checkpoint** is an ultra-lightweight, zero-dependency protocol that installs in seconds. It enforces a simple, unbreakable rule on AI agents: **never touch an existing file without archiving its previous state first**, while automatically maintaining an audit ledger explaining *why* the change occurred.

---

## 🌟 Key Benefits

### 1. 🛡️ Absolute Safety (Zero Data Loss)
Before modifying any file, the agent copies its exact prior state into `.snapshots/`. Your working code and drafts are never permanently destroyed or overwritten.

### 2. 📝 Automatic Audit Trail (Living Engineering Journal)
The agent automatically maintains `REVISION_LOG.md`, detailing the **technical and architectural rationale** behind every modification. Ideal for:
* Team code reviews and pull request summaries.
* Post-mortem debugging without guessing what the AI changed overnight.
* Academic and enterprise compliance audit trails.

### 3. 🎯 Zero Dependency & 100% Private
* **No package managers:** Requires no `npm`, `pip`, Docker, or background daemon.
* **100% Local & Offline:** All snapshots and logs remain strictly on your local disk. Zero telemetry or external network calls.

### 4. 🔀 Deep Trackback & Time-Travel
Ask your AI at any time: *"Compare `auth_service.py` with the version before the refactor"* or *"Revert `auth_service.py` back to `v1.0.0`"*. The agent retrieves the snapshot and performs semantic diffs or restorations instantly.

---

## 🏗️ Architecture: Dual-Ledger System

```mermaid
flowchart TD
    subgraph Trigger ["1. File Modification Trigger"]
        A["User Requests Edit / Refactor"] --> B{"File Exists?"}
        B -->|"No (New File)"| C["Register as v1.0.0 (Initial)"]
        B -->|"Yes"| D["Classify SemVer Impact\n(MAJOR / MINOR / PATCH)"]
    end

    subgraph CoreEngine ["2. Snapshot & Execution"]
        D --> E["Copy Active File to:\n.snapshots/<filename>_v<OLD_VERSION>.<ext>"]
        E --> F["Apply Modifications to Active File"]
    end

    subgraph DualLedger ["3. Dual-Ledger Synchronization"]
        F --> G[".snapshots/manifest.json\n(Fast Machine Index for AI: < 5ms)"]
        F --> H["REVISION_LOG.md\n(Human-Readable Audit Trail)"]
    end

    subgraph Retrieval ["4. Trackback & Rollback"]
        I["User: 'Compare with previous version'"] --> G
        G --> J["Load Historical Snapshot vs Active File"]
        J --> K["Generate Semantic Diff & Audit Report"]
    end

    style G fill:#1b4332,color:#fff,stroke:#fff
    style H fill:#2d6a4f,color:#fff,stroke:#fff
```

---

## 🔰 Beginner's Quickstart (30-Second Setup)

Installation requires **zero configuration and no command-line tools**. It follows a simple drop-in pattern.

### Option 1: File Explorer / Drag-and-Drop (Easiest)
1. Open the [`adapters/`](./adapters) folder in this repository.
2. Select the single file matching your AI tool:
   * **Cursor IDE:** Copy [`.cursorrules`](./adapters/.cursorrules)
   * **Claude Code:** Copy [`CLAUDE.md`](./adapters/CLAUDE.md)
   * **Google Antigravity / Gemini CLI:**
     - **Project Scope:** Copy [`adapters/AGENTS.md`](./adapters/AGENTS.md) into your project root.
     - **Global Machine Scope (Recommended):** Append [`adapters/AGENTS.md`](./adapters/AGENTS.md) to `~/.gemini/AGENTS.md` (protects all projects automatically!).
     - **Native Skill Scope:** Copy [`SKILL.md`](./SKILL.md) to your Antigravity skills directory (`.agents/skills/agent-checkpoint/SKILL.md` or `~/.gemini/config/plugins/.../skills/agent-checkpoint/`).
   * **Windsurf (Cascade):** Copy [`.windsurfrules`](./adapters/.windsurfrules)
   * **GitHub Copilot:** Copy [`copilot-instructions.md`](./adapters/copilot-instructions.md) into your `.github/` folder
3. Paste the file into your project's root folder.
4. **Done!** Your AI is now governed by the Agent-Checkpoint protocol.

---

### Option 2: 1-Line Terminal Download (`curl`)
Run the command matching your editor inside your project root:

* **Cursor IDE:**
  ```bash
  curl -o .cursorrules https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/.cursorrules
  ```
* **Claude Code:**
  ```bash
  curl -o CLAUDE.md https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/CLAUDE.md
  ```
* **Google Antigravity / Gemini CLI:**
  ```bash
  # Project-specific:
  curl -o AGENTS.md https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/AGENTS.md

  # Or Global (protects all projects on your machine):
  # Linux/macOS:
  curl -s https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/AGENTS.md >> ~/.gemini/AGENTS.md
  # Windows PowerShell:
  Add-Content -Path "$HOME\.gemini\AGENTS.md" -Value (Invoke-RestMethod "https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/AGENTS.md")
  ```
* **Windsurf:**
  ```bash
  curl -o .windsurfrules https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/.windsurfrules
  ```

---

## 🎮 Day-to-Day Workflow (Zero Learning Curve)

Once the adapter is placed, **you do not need to memorize new commands**. Continue interacting with your AI agent normally:

### 1. Requesting Edits / Refactoring
Issue your standard instructions:
> *"Please refactor the login authentication in `auth_service.py` to support JWT refresh tokens and rate limiting."*

**Automatically in the background, your AI will:**
1. Backup your existing file to `.snapshots/auth_service_v1.0.0.py`.
2. Apply the requested changes to `auth_service.py` (bumping to `v1.1.0`).
3. Append technical rationale to `REVISION_LOG.md` and `.snapshots/manifest.json`.

---

### 2. Inspecting Differences (*Trackback*)
Inspect what was changed without manual diffing:
> *"Compare `auth_service.py` with the version before the latest refactor. What security logic and error handling changed?"*

The agent reads the snapshot and provides a side-by-side Before vs After analysis.

---

### 3. Reverting Changes (*Rollback*)
If an AI modification introduced issues:
> *"Revert `auth_service.py` back to `v1.0.0`."*

The agent safely restores the file from `.snapshots/` without corrupting your workspace history.

---

## 📂 Resulting Directory Layout

Once active, your project maintains an organized, self-documenting structure:

```text
my-project/
├── .snapshots/                          # Historical snapshots (auto-managed)
│   ├── manifest.json                    # Machine-readable registry (< 5ms read)
│   ├── auth_service_v1.0.0.py           # Preserved pre-edit snapshot
│   └── api_routes_v1.0.0.ts
├── REVISION_LOG.md                      # Human-readable engineering audit trail
├── auth_service.py                      # Active working file (v1.1.0)
└── api_routes.ts                        # Active working file
```

---

## ⚠️ Known Limitations

In the interest of software engineering transparency, version `v1.0` has the following known boundaries:

| Limitation | Technical Context | Recommended Mitigation |
| :--- | :--- | :--- |
| **1. Small Model Compliance** | The protocol relies on system prompt instructions. Tier-1 models (Claude 3.5/3.7, GPT-4o, Gemini 2.0 Pro) exhibit **~100% compliance**. Smaller local models (7B/8B) may occasionally omit a snapshot during very long conversation windows. | Use capable reasoning models for major refactoring tasks. |
| **2. Snapshot Sprawl** | If a single file is modified hundreds of times, `.snapshots/` accumulates individual files. Auto-pruning is not yet included in v1.0. | Plain-text files consume minimal storage (~10 MB/month), but periodic manual pruning of old patch versions is recommended. |
| **3. File Deletion & Renaming** | Version 1.0 targets file content edits (`modify`). Deleting a file via terminal (`rm`) is not yet intercepted automatically. | Confirm manual verification before instructing agents to execute permanent file deletions. |
| **4. Multi-File Batch Edits** | Modifying 10 files in a single prompt creates 10 individual log entries rather than a single unified changeset. | Refactor modules in focused, logical increments. |

---

## 🌐 Universal File Support & Smart Storage Guardrails

Agent-Checkpoint is **completely language-agnostic and filetype-agnostic**. The core rule is simple:  
> **"If it can be opened and edited in a text/code editor, Agent-Checkpoint protects it."**

### ✅ What Gets Automatically Snapshotted? (100+ Formats Supported)

* **Programming & Systems:** Python (`.py`), TypeScript (`.ts`, `.tsx`), JavaScript (`.js`, `.jsx`), Go (`.go`), Rust (`.rs`), C/C++ (`.c`, `.cpp`, `.h`, `.hpp`), C# (`.cs`), Java (`.java`), PHP (`.php`), Ruby (`.rb`), Swift (`.swift`), Kotlin (`.kt`), Dart (`.dart`), Scala (`.scala`), Shell (`.sh`, `.bash`, `.zsh`), PowerShell (`.ps1`, `.bat`), Lua (`.lua`), R (`.r`), Julia (`.jl`).
* **Web & Modern Frontend:** HTML (`.html`), CSS (`.css`), SCSS/SASS (`.scss`), Vue (`.vue`), Svelte (`.svelte`), XML (`.xml`), SVG (`.svg`).
* **Data Science & Research:** Jupyter Notebooks (`.ipynb`), Typst (`.typ`), LaTeX (`.tex`, `.bib`, `.sty`), Markdown (`.md`, `.mdx`), RestructuredText (`.rst`), AsciiDoc (`.adoc`), Plain text (`.txt`).
* **Diagrams & Visuals as Code:** Mermaid (`.mmd`, `.mermaid`), PlantUML (`.puml`), Graphviz (`.dot`), Draw.io XML (`.drawio`), Excalidraw JSON (`.excalidraw`).
* **API Schemas & Contracts:** Protobuf (`.proto`), GraphQL (`.graphql`, `.gql`), Prisma (`.prisma`), OpenAPI / Swagger (`.yaml`, `.json`), Apache Thrift (`.thrift`), FlatBuffers (`.fbs`).
* **Game Development & Shaders:** GLSL (`.glsl`, `.frag`, `.vert`), HLSL (`.hlsl`), WGSL (`.wgsl`), Godot GDScript (`.gd`, `.tscn`), Unreal Engine text configs (`.ini`).
* **Hardware & Embedded:** Verilog (`.v`, `.vh`), SystemVerilog (`.sv`), VHDL (`.vhd`), Assembly (`.asm`, `.s`), Arduino (`.ino`), CMake (`CMakeLists.txt`, `.cmake`).
* **DevOps, IaC & Policies:** Open Policy Agent Rego (`.rego`), CUE (`.cue`), Terraform (`.tf`), Kubernetes manifests, Dockerfile, Makefile, JSON, YAML, TOML, SQL (`.sql`).

---

### 🛡️ Smart Storage Guardrails (Zero-Bloat Guarantee)

To expand file flexibility without ever overwhelming your hard drive, the protocol enforces **Tiered Ingestion Rules**:

#### 1. 📏 Smart 1 MB Cap for Tabular Data
* Small mock data, test fixtures, and schema seeds (`.csv`, `.tsv`, `.jsonl`, `.ndjson`) are **automatically snapshotted ONLY if file size $\le 1\text{ MB}$**.
* If a dataset exceeds $1\text{ MB}$ (e.g., a 100 MB training dataset), the agent **skips raw file copying** and logs metadata only in `REVISION_LOG.md` (recording timestamp and filename without disk bloat).

#### 2. 🚫 Strict Binary Exclusions
The protocol strictly avoids archiving heavy binary assets and dependency caches:

| Category | Policy | Examples (Never Snapshotted) |
| :--- | :--- | :--- |
| **Heavy ML & AI Models** | 🚫 **Excluded** | Weights & checkpoints (`.pt`, `.pth`, `.onnx`, `.safetensors`, `.bin`, `.ckpt`) |
| **Large Data Files** | 🚫 **Excluded** | Heavy data ($> 1\text{ MB}$, `.parquet`, `.h5`, `.arrow`, `.feather`, large `.csv`) |
| **Compiled Binaries & Media** | 🚫 **Excluded** | Executables (`.exe`, `.dll`, `.so`), archives (`.zip`, `.tar.gz`), video/audio |
| **Dependency & Build Caches** | 🚫 **Excluded** | `node_modules/`, `venv/`, `.venv/`, `__pycache__/`, `target/`, `dist/`, `build/`, `.git/` |

**Storage Footprint:**  
Because plain-text source files are exceptionally small (typically 5 KB – 50 KB), even **500 active file edits per month** will consume only **~7.5 MB to 15 MB** of disk space. Negligible on modern hard drives.

---

## 📄 License & Community

Distributed under the [MIT License](./LICENSE) — free for personal, academic, and commercial use.

Contributions, pull requests, and feedback are welcome! ⭐ Leave a star if this protocol helps safeguard your workflow.
