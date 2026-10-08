# Security Policy

## 🛡️ Architecture & Security Model

Agent-Checkpoint is designed as a **zero-dependency, purely local protocol**:

1. **Zero Data Egress:** No code, diffs, or snapshot files are ever transmitted to any third-party server, cloud storage, or external API. Everything executes strictly on your local filesystem.
2. **Exclusion of Secrets & Credentials:**
   * Never store API keys, tokens, or credentials in tracked source code.
   * Add sensitive environment files (`.env`, `.env.local`, `credentials.json`, `*.pem`, `*.key`) to your `.gitignore`.
3. **Storage Bounding ($K \le 5$):**
   * Snapshots are strictly bounded to the 5 most recent versions per file.
   * Heavy binary model assets (`.pt`, `.onnx`, `.safetensors`, `.ckpt`) and tabular datasets $> 1\text{ MB}$ are excluded by policy to prevent accidental disk saturation.

---

## 🚨 Reporting a Vulnerability

If you discover a potential vulnerability, bug, or security risk regarding snapshot handling or data integrity:

1. Please do **not** open a public issue immediately.
2. Submit a private vulnerability report via GitHub Security Advisories or contact the maintainer directly.
3. We will respond promptly, evaluate the issue, and release a fix.
