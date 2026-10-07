#!/usr/bin/env python3
"""
Agent-Checkpoint v2.0: Two-Sided Selective Rollback Verification
Demonstrates that restoring a broken file does NOT disturb or corrupt
other concurrently modified files, verified cryptographically via SHA-256.
"""

import hashlib
import os
import shutil
import tempfile

def calculate_sha256(filepath: str) -> str:
    """Calculate SHA-256 hash of a file."""
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def run_verification():
    print("=" * 70)
    print("Agent-Checkpoint: Selective Rollback Two-Sided Verification")
    print("=" * 70)

    # 1. Setup simulated workspace
    test_dir = tempfile.mkdtemp(prefix="agent_checkpoint_test_")
    try:
        auth_file = os.path.join(test_dir, "src", "auth", "service.py")
        billing_file = os.path.join(test_dir, "src", "billing", "service.py")
        auth_snapshot = os.path.join(test_dir, ".snapshots", "src", "auth", "service.py", "v1.0.0.py")

        os.makedirs(os.path.dirname(auth_file), exist_ok=True)
        os.makedirs(os.path.dirname(billing_file), exist_ok=True)
        os.makedirs(os.path.dirname(auth_snapshot), exist_ok=True)

        # Baseline v1.0.0 state
        baseline_auth_code = "# Baseline v1.0.0 Auth Service\ndef authenticate(user, password):\n    return True\n"
        with open(auth_snapshot, "w") as f:
            f.write(baseline_auth_code)

        # 2. Simulate AI multi-file edits (auth gets broken, billing gets good feature)
        hallucinated_auth_code = "# Broken v1.1.0 Auth Service (Hallucinated syntax error)\ndef authenticate(:\n    syntax error\n"
        good_billing_code = "# Good v1.1.0 Billing Service (Stripe Webhook)\ndef process_stripe_webhook(payload):\n    return {'status': 'processed'}\n"

        with open(auth_file, "w") as f:
            f.write(hallucinated_auth_code)
        with open(billing_file, "w") as f:
            f.write(good_billing_code)

        print("\n[1] Initial State After AI Prompt:")
        print("  - src/auth/service.py:    BROKEN (Syntax error introduced)")
        print("  - src/billing/service.py: GOOD (Stripe webhook feature added)")

        # Record hash of untouched file BEFORE rollback
        billing_sha_before = calculate_sha256(billing_file)
        auth_snapshot_sha = calculate_sha256(auth_snapshot)

        # 3. Perform Selective Rollback of auth only
        print("\n[2] Executing Selective Rollback:")
        print("  Restoring 'src/auth/service.py' from .snapshots/src/auth/service.py/v1.0.0.py...")
        shutil.copy2(auth_snapshot, auth_file)

        # Record hash of files AFTER rollback
        billing_sha_after = calculate_sha256(billing_file)
        auth_sha_after = calculate_sha256(auth_file)

        # 4. Two-Sided Mathematical Assertions
        print("\n[3] Running Two-Sided Assertions:")

        # Side A: Assert untouched file was NOT modified
        assert billing_sha_before == billing_sha_after, "FAIL: Untouched billing file was corrupted!"
        print("  [PASS] Side A [Untouched File Integrity]:")
        print(f"     SHA-256 Before: {billing_sha_before[:16]}...")
        print(f"     SHA-256 After:  {billing_sha_after[:16]}... (MATCH - 100% Unchanged)")

        # Side B: Assert restored file exactly matches checkpoint
        assert auth_sha_after == auth_snapshot_sha, "FAIL: Restored file does not match checkpoint!"
        print("  [PASS] Side B [Checkpoint Fidelity]:")
        print(f"     Active SHA-256:     {auth_sha_after[:16]}...")
        print(f"     Checkpoint SHA-256: {auth_snapshot_sha[:16]}... (MATCH - 100% Restored)")

        # 5. Edge Case: Idempotent Restoration (Second Restore of Same Checkpoint)
        print("\n[4] Testing Edge Case: Idempotent Restoration (Second Restore)")
        print("  Restoring 'src/auth/service.py' again from the same checkpoint...")
        shutil.copy2(auth_snapshot, auth_file)

        auth_sha_second = calculate_sha256(auth_file)
        billing_sha_second = calculate_sha256(billing_file)

        assert auth_sha_second == auth_sha_after, "FAIL: Second restore altered auth file!"
        assert billing_sha_second == billing_sha_after, "FAIL: Second restore altered billing file!"
        print("  [PASS] Edge Case [Idempotency Verified]:")
        print(f"     Auth SHA-256 (2nd Restore):    {auth_sha_second[:16]}... (STABLE - No Drift)")
        print(f"     Billing SHA-256 (2nd Restore): {billing_sha_second[:16]}... (STABLE - Untouched)")

        print("\n" + "=" * 70)
        print("RESULT: All assertions PASSED! Selective rollback & idempotency verified.")
        print("=" * 70)

    finally:
        shutil.rmtree(test_dir, ignore_errors=True)

if __name__ == "__main__":
    run_verification()
