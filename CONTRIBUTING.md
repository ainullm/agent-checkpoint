# Contributing to Agent-Checkpoint

Thank you for your interest in improving **Agent-Checkpoint**! We welcome contributions from developers, researchers, and AI tooling engineers.

---

## 🛠️ How You Can Contribute

1. **Add New AI Agent Adapters:**
   If you use an AI coding tool or IDE extension not yet supported (e.g., Roo Code, Amazon Q, Continue, Aider), create an adapter in `adapters/` and submit a Pull Request.

2. **Improve Verification & Edge Cases:**
   Add new tests to `examples/verify_selective_rollback.py` covering corner cases (e.g., symlinks, nested submodules, Unicode paths).

3. **Documentation & Translations:**
   Help translate documentation into additional languages or clarify setup instructions.

---

## 🧪 Local Testing

Before submitting a Pull Request, ensure that all verification tests pass:

```bash
# Run two-sided integrity & idempotency test
python examples/verify_selective_rollback.py
```

Expected result: All assertions must pass with `exit code 0`.

---

## 📝 Pull Request Guidelines

1. Fork the repository and create your branch from `main`.
2. Keep adapter rules strictly aligned with the **v2.0 Turbo specifications** (< 40 tokens per sharded manifest, $K \le 5$ sliding window retention, dual-ledger sync).
3. If modifying core documentation, keep `README.md` and `README.id.md` synchronized.
4. Open a PR with a clear description of what was changed and why.
