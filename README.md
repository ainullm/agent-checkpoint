<div align="center">

# 🛡️ Agent-Checkpoint v2.0 (Turbo)

**Ultra-efficient, zero-data-loss file snapshotting, SemVer classification, and token-optimized dual-ledger audit trail for autonomous AI coding agents.**

[![Version: 2.0](https://img.shields.io/badge/Version-2.0%20Turbo-brightgreen.svg)]()
[![Token Overhead: -80%](https://img.shields.io/badge/Token%20Overhead--80%25-blueviolet.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![Cross Agent](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Windsurf%20%7C%20Copilot-orange.svg)]()

---

**Languages:**  
[English (Current)](./README.md) • [🇮🇩 Bahasa Indonesia](./README.id.md)

---

</div>

## ⚡ The Problem: Destructive In-Place AI Overwrites & Token Bloat

Autonomous AI coding agents (Cursor, Claude Code, Google Antigravity, Windsurf, GitHub Copilot, Aider) are accelerating software development. However, almost every agent shares two dangerous behaviors:
1. **Destructive Overwrites:** They overwrite files in-place without preserving history, wiping critical functions and edge cases.
2. **Context & Token Inefficiency:** Naive version tracking often forces the AI to re-read hundreds of past changelog lines, blowing up token costs on every edit.

---

## 💡 The Solution: Agent-Checkpoint v2.0 Turbo

**Agent-Checkpoint v2.0** solves both problems with an ultra-lightweight, zero-dependency protocol. It enforces pre-edit safety while introducing **Hierarchical Bucketing**, **Sliding Window Retention ($K \le 5$)**, and **Sharded Manifests** to cut token overhead by **80%**.

---

## 🌟 Key v2.0 Features

### 1. 🛡️ Absolute Safety (Zero Data Loss)
Before modifying any file, the agent copies its exact prior state to `.snapshots/<filepath>/v<OLD_VERSION>.<ext>`. Your working code is never permanently lost.

### 2. 📁 Hierarchical File Bucketing (Clean Storage)
No more flat folders filled with hundreds of files. Every tracked file receives its own isolated directory matching the project structure (e.g., `.snapshots/auth_service.py/`).

### 3. 🔄 Sliding Window Retention ($K = 5$ Max Versions)
Each file bucket retains at most **5 latest snapshot versions**. When version 6 is created, the oldest snapshot is automatically pruned. Your disk consumption remains strictly bounded and constant.

### 4. ⚡ 80% Token Reduction (Sharded Local Manifest)
Instead of reading a massive global manifest, the agent reads a tiny local index (`.snapshots/<filepath>/manifest.json`) consuming **less than 40 tokens** ($O(1)$ token overhead). Audit logs are streamed as compact 1-line tables into `REVISION_LOG.md` without re-reading past history.

---

## 🏗️ Architecture: v2.0 Turbo Pipeline

```mermaid
flowchart TD
    subgraph Trigger ["1. File Modification Trigger"]
        A["User Requests Edit / Refactor"] --> B{"File Exists?"}
        B -->|"No (New File)"| C["Register as v1.0.0 (Initial)"]
        B -->|"Yes"| D["Read Local Sharded Index\n.snapshots/<filepath>/manifest.json (< 40 tokens)"]
        D --> E["Classify SemVer Impact\n(MAJOR / MINOR / PATCH)"]
    end

    subgraph CoreEngine ["2. Bucketed Snapshot & Retention"]
        E --> F["Copy Active File to:\n.snapshots/<filepath>/v<OLD_VERSION>.<ext>"]
        F --> G{"Bucket Snapshots > 5?"}
        G -->|"Yes"| H["Prune Oldest Snapshot File"]
        G -->|"No"| I["Apply Modifications to Active File"]
        H --> I
    end

    subgraph DualLedger ["3. Token-Optimized Dual-Ledger"]
        I --> J["Update Sharded Index:\n.snapshots/<filepath>/manifest.json (~30 tokens)"]
        I --> K["Stream Append 1 Line to:\nREVISION_LOG.md (Compact Table)"]
    end

    subgraph Retrieval ["4. Trackback & Instant Rollback"]
        L["User: 'Rollback auth.py to v1.0.0'"] --> J
        J --> M["Restore Snapshot Over Active File in 3 Seconds"]
    end

    style J fill:#1b4332,color:#fff,stroke:#fff
    style K fill:#2d6a4f,color:#fff,stroke:#fff
```

---

## 🔰 Beginner's Quickstart (30-Second Setup)

Installation requires **zero configuration and no command-line tools**. It follows a simple drop-in pattern.

### Option 1: File Explorer / Drag-and-Drop (Easiest)
1. Open the [`adapters/`](./adapters) folder in this repository.
2. Select the single file matching your AI tool:
   * **Cursor IDE:** Copy [`.cursorrules`](./adapters/.cursorrules) to project root, or copy [`agent-checkpoint.mdc`](./adapters/agent-checkpoint.mdc) into `.cursor/rules/` (Cursor 0.40+)
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
  # Classic .cursorrules:
  curl -o .cursorrules https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/.cursorrules

  # Or Modern Cursor Rules (.cursor/rules/*.mdc):
  mkdir -p .cursor/rules && curl -o .cursor/rules/agent-checkpoint.mdc https://raw.githubusercontent.com/ainullm/agent-checkpoint/main/adapters/agent-checkpoint.mdc
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

## 🎮 Comprehensive Usage Guide & Real-World Workflows

Once the adapter rule is placed, **there are no special CLI commands or syntax to memorize**. You interact with your AI agent naturally. Here are the 4 standard usage workflows:

---

### Workflow 1: Everyday Feature Addition & Refactoring

**What You Ask Your Agent:**
> *"Refactor `auth_service.py` to support JWT refresh tokens, add rate limiting with Redis, and improve error logging."*

**What the Agent Does Automatically (Behind the Scenes):**
1. **Verifies File State:** Detects that `auth_service.py` already exists at version `v1.0.0`.
2. **Takes Pre-Edit Snapshot:** Copies `auth_service.py` $\to$ `.snapshots/auth_service_v1.0.0.py`.
3. **Triages SemVer Impact:** Evaluates the request. Because new features and parameters were introduced without breaking existing endpoints, it assigns `MINOR` ($\to$ `v1.1.0`).
4. **Applies Edits:** Overwrites `auth_service.py` with the new JWT and rate-limiting code.
5. **Synchronizes Dual-Ledger:**
   * Appends machine entry to `.snapshots/manifest.json`.
   * Appends human entry to `REVISION_LOG.md` detailing exact line ranges and architectural rationale.

---

### Workflow 2: Emergency Rollback (Fixing AI Hallucinations)

If an agent hallucinates, deletes essential business logic, or introduces breaking bugs across prompt iterations:

**What You Ask Your Agent:**
> *"The changes in `auth_service.py` broke our test suite. Please roll back `auth_service.py` to `v1.0.0`."*

**What the Agent Does:**
1. Looks up `v1.0.0` in `.snapshots/manifest.json`.
2. Restores `.snapshots/auth_service_v1.0.0.py` over `auth_service.py`.
3. Logs the rollback event in `REVISION_LOG.md` (e.g., `PATCH: Rolled back auth_service.py from v1.1.0 to v1.0.0 due to test failure`).
4. Your codebase is immediately returned to a clean, working state.

---

### Workflow 3: Deep Trackback & Semantic Diff Inspection

You return to your computer after an agent finished multiple autonomous edits:

**What You Ask Your Agent:**
> *"Trackback: Compare `data_pipeline.py` with the version before the vector optimization. What algorithmic bottlenecks and functions were modified?"*

**What the Agent Does:**
1. Loads the historical snapshot `.snapshots/data_pipeline_v1.0.0.py` and active `data_pipeline.py`.
2. Reads `REVISION_LOG.md` to retrieve the original intent.
3. Produces a concise, semantic Before vs After diff report highlighting modified functions and algorithmic complexity changes without manual git diffing.

---

### Workflow 4: Multi-File Batch Workflows (Composer & Agents)

When using Cursor Composer, Windsurf Cascade, or Claude Code on multi-file prompts:
> *"Implement a new billing checkout flow: update `routes.ts`, `stripe_client.py`, and `database.sql`."*

The protocol executes sequentially per target file:
* `.snapshots/routes_v1.0.0.ts`
* `.snapshots/stripe_client_v1.0.0.py`
* `.snapshots/database_v1.0.0.sql`

Each modified file receives its own independent pre-edit snapshot and synchronized entry in `manifest.json` and `REVISION_LOG.md`.

---

## 🤝 Git Integration Strategies: How to Handle `.snapshots/`

Agent-Checkpoint is designed to complement Git, not replace it. You can choose between two popular collaboration strategies:

```mermaid
flowchart LR
    subgraph StrategyA ["Strategy A: Team Audit Trail (Recommended for Open Source & Compliance)"]
        A1[Commit Active Code] --> A2[Commit REVISION_LOG.md]
        A2 --> A3[Commit .snapshots/ to Git]
    end

    subgraph StrategyB ["Strategy B: Local Micro-Safety (Recommended for Lean Repos)"]
        B1[Commit Active Code] --> B2[Commit REVISION_LOG.md]
        B2 --> B3[Add .snapshots/ to .gitignore]
    end

    style StrategyA fill:#132a13,color:#fff,stroke:#fff
    style StrategyB fill:#1f2421,color:#fff,stroke:#fff
```

* **Strategy A (Full Team Provenance):** Check `.snapshots/` into Git. Teammates pulling the repo can inspect what AI generated, run trackbacks on previous prompts, and review audit trails directly in pull requests.
* **Strategy B (Local Scratchpad):** Add `.snapshots/` to `.gitignore`, but keep `REVISION_LOG.md` committed. You retain 100% rollback protection on your local machine, while keeping remote Git repository size completely lean.

---

## 📂 Resulting Directory Layout (v2.0 Bucketed)

Once active, your project maintains an exceptionally clean, self-contained hierarchy:

```text
my-project/
├── .snapshots/                          # Isolated historical buckets
│   ├── auth_service.py/                 # Dedicated bucket per file
│   │   ├── manifest.json                # Sharded local registry (< 40 tokens read)
│   │   ├── v1.0.0.py                    # Retained snapshot (K <= 5 max)
│   │   └── v1.1.0.py
│   └── src/routes/api.ts/               # Nested paths preserved cleanly
│       ├── manifest.json
│       └── v1.0.0.ts
├── REVISION_LOG.md                      # Append-only compact Markdown table
├── auth_service.py                      # Active working file
└── src/routes/api.ts
```

---

## ⚡ Token Economics: 80% Overhead Reduction (v2.0)

A common concern with prompt-level agent safety is token burn. In **v2.0 Turbo**, we decoupled global registries into **sharded local indices** and **micro-log streams**:

| Action Per Single File Edit | Naive / v1.0 Protocol | **v2.0 Turbo Protocol** | Savings |
| :--- | :---: | :---: | :---: |
| **Context / Manifest Read** | ~500 tokens *(scans global manifest)* | **~30–40 tokens** *(sharded bucket index)* | **-92%** |
| **Changelog & Tool Output** | ~250 tokens *(verbose paragraphs)* | **~50–80 tokens** *(1-line compact table)* | **-75%** |
| **Total Token Overhead** | **~750 tokens** | **~100–120 tokens** | **~84% Cheaper** |
| **API Cost Per Edit (Sonnet 3.5)** | ~\$0.0053 (~Rp 80) | **~\$0.0009 (~Rp 14)** | **Negligible** |

---

## 💾 Storage Economics & Real-World Consumption Scenarios

With the **Sliding Window Retention ($K \le 5$)**, disk storage is mathematically bounded. Even if you edit a file 1,000 times, only the **5 latest snapshots are kept**.

### 📊 Real-World Usage Scenarios & Storage Math

Below is an empirical simulation assuming an average source code file size of **15 KB** (typical for 300–600 lines of Python, TypeScript, or Go):

| Developer Persona | Daily AI Edits | Avg File Size | Monthly Disk Usage | Yearly Disk Usage | % of 512 GB SSD |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 🧑‍💻 **Casual / Student Dev**<br>*(Part-time projects, homework, occasional scripts)* | ~2 edits/day<br>*(10/week)* | 15 KB | **~0.9 MB** | **~10.8 MB** | `0.002%` |
| 🚀 **Full-Time Software Engineer**<br>*(Active daily feature building, refactoring)* | ~30 edits/day | 15 KB | **~13.5 MB** | **~162 MB** | `0.031%` |
| ⚡ **Heavy AI Pair Programmer**<br>*(Cursor Composer power user, 10+ prompt sessions/day)* | ~100 edits/day | 15 KB | **~45.0 MB** | **~540 MB** | `0.105%` |
| 🤖 **Autonomous Multi-Agent Bot**<br>*(Continuous automated code generation & test loops)* | ~500 edits/day | 15 KB | **~225.0 MB** | **~2.7 GB** | `0.527%` |

> 💡 **Takeaway:** With $K=5$ retention, active projects naturally stabilize at **20 MB – 50 MB total disk usage indefinitely**.

---

### 🛡️ Why Disk Space Will Never Blow Up (3 Safety Pillars)

1. **Microscopic Plain-Text Footprint:** Code files compress and store efficiently. 100 snapshots of a 10 KB file take only 1 MB.
2. **📏 Smart 1 MB Cap on Tabular Data:** Small mock seeds (`.csv`, `.jsonl`, `.tsv`) $\le 1\text{ MB}$ are snapshotted. Datasets $> 1\text{ MB}$ are strictly skipped from raw duplication and logged via metadata only.
3. **🚫 Absolute Exclusion of Binary Bloat:** Heavy machine learning models (`.pt`, `.onnx`, `.safetensors`), binary archives (`.zip`, `.exe`), and dependency caches (`node_modules/`, `venv/`, `__pycache__/`) are **strictly excluded by policy**.

---

### 🧹 Maintenance & Pruning Guide (Freeing Space Anytime)

Because `.snapshots/` contains historical backups rather than runtime code, **pruning or deleting snapshots carries zero risk of breaking your application**.

#### 1. Delete Snapshots Older than 30 Days
* **PowerShell (Windows):**
  ```powershell
  Get-ChildItem -Path .snapshots -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) -and $_.Name -ne "manifest.json" } | Remove-Item
  ```
* **Bash / Zsh (Linux & macOS):**
  ```bash
  find .snapshots/ -type f ! -name "manifest.json" -mtime +30 -delete
  ```

#### 2. Keep Only the Last 5 Versions Per File
* **Bash / Zsh:**
  ```bash
  # Prunes older snapshot files while preserving manifest.json
  ls -t .snapshots/*_*.* 2>/dev/null | tail -n +15 | xargs -r rm --
  ```

#### 3. Complete Reset (Nuclear Clean)
If a project is finalized and you want to reclaim 100% of snapshot space:
```bash
# Deletes all snapshots and resets the machine ledger
rm -rf .snapshots && mkdir .snapshots && echo "[]" > .snapshots/manifest.json
```

---

## 🌐 Universal File Support (100+ Formats Supported)

Agent-Checkpoint is completely language-agnostic and filetype-agnostic:

* **Programming & Systems:** Python (`.py`), TypeScript (`.ts`, `.tsx`), JavaScript (`.js`, `.jsx`), Go (`.go`), Rust (`.rs`), C/C++ (`.c`, `.cpp`, `.h`, `.hpp`), C# (`.cs`), Java (`.java`), PHP (`.php`), Ruby (`.rb`), Swift (`.swift`), Kotlin (`.kt`), Dart (`.dart`), Scala (`.scala`), Shell (`.sh`, `.bash`, `.zsh`), PowerShell (`.ps1`, `.bat`), Lua (`.lua`), R (`.r`), Julia (`.jl`).
* **Web & Modern Frontend:** HTML (`.html`), CSS (`.css`), SCSS/SASS (`.scss`), Vue (`.vue`), Svelte (`.svelte`), XML (`.xml`), SVG (`.svg`).
* **Data Science & Research:** Jupyter Notebooks (`.ipynb`), Typst (`.typ`), LaTeX (`.tex`, `.bib`, `.sty`), Markdown (`.md`, `.mdx`), RestructuredText (`.rst`), AsciiDoc (`.adoc`), Plain text (`.txt`).
* **Diagrams & Visuals as Code:** Mermaid (`.mmd`, `.mermaid`), PlantUML (`.puml`), Graphviz (`.dot`), Draw.io XML (`.drawio`), Excalidraw JSON (`.excalidraw`).
* **API Schemas & Contracts:** Protobuf (`.proto`), GraphQL (`.graphql`, `.gql`), Prisma (`.prisma`), OpenAPI / Swagger (`.yaml`, `.json`), Apache Thrift (`.thrift`), FlatBuffers (`.fbs`).
* **Game Development & Shaders:** GLSL (`.glsl`, `.frag`, `.vert`), HLSL (`.hlsl`), WGSL (`.wgsl`), Godot GDScript (`.gd`, `.tscn`), Unreal Engine text configs (`.ini`).
* **Hardware & Embedded:** Verilog (`.v`, `.vh`), SystemVerilog (`.sv`), VHDL (`.vhd`), Assembly (`.asm`, `.s`), Arduino (`.ino`), CMake (`CMakeLists.txt`, `.cmake`).
* **DevOps, IaC & Policies:** Open Policy Agent Rego (`.rego`), CUE (`.cue`), Terraform (`.tf`), Kubernetes manifests, Dockerfile, Makefile, JSON, YAML, TOML, SQL (`.sql`).

---

## ⚠️ Known Boundaries (v1.0)

| Limitation | Technical Context | Recommended Mitigation |
| :--- | :--- | :--- |
| **1. Small Model Compliance** | The protocol relies on system prompt instructions. Tier-1 models (Claude 3.5/3.7, GPT-4o, Gemini 2.0 Pro) exhibit **~100% compliance**. Smaller local models (7B/8B) may occasionally omit a snapshot during very long conversation windows. | Use capable reasoning models for major refactoring tasks. |
| **2. Snapshot Sprawl** | If a single file is modified hundreds of times, `.snapshots/` accumulates individual files. Auto-pruning is not yet included in v1.0. | Plain-text files consume minimal storage (~10 MB/month), but periodic manual pruning of old patch versions is recommended using the scripts above. |
| **3. File Deletion & Renaming** | Version 1.0 targets file content edits (`modify`). Deleting a file via terminal (`rm`) is not yet intercepted automatically. | Confirm manual verification before instructing agents to execute permanent file deletions. |
| **4. Multi-File Batch Edits** | Modifying 10 files in a single prompt creates 10 individual log entries rather than a single unified changeset. | Refactor modules in focused, logical increments. |

---

## 📄 License & Community

Distributed under the [MIT License](./LICENSE) — free for personal, academic, and commercial use.

Contributions, pull requests, and feedback are welcome! ⭐ Leave a star if this protocol helps safeguard your workflow.

