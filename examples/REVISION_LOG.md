# Project Revision Log & Audit Trail

All modifications adhere to the [Agent-Checkpoint Protocol](../SKILL.md).

---

## [v1.1.0] - 2026-10-06 11:30:00 UTC
- **Target File:** `data_pipeline.py`
- **Change Type:** MINOR
- **Archived Snapshot:** `.snapshots/data_pipeline_v1.0.0.py`
- **Rationale:** Add z-score feature scaling to prevent gradient saturation in downstream models.
- **Key Changes Applied:**
  - Added strict typing annotations (`Tuple[pd.DataFrame, StandardScaler]`).
  - Integrated `sklearn.preprocessing.StandardScaler` over numeric features.
  - Returned fitted scaler alongside cleaned DataFrame for deployment pipeline reusability.

---

## [v1.0.0] - 2026-10-06 10:00:00 UTC
- **Target File:** `data_pipeline.py`
- **Change Type:** INITIAL
- **Archived Snapshot:** `-`
- **Rationale:** Initial baseline dataset loader.
- **Key Changes Applied:**
  - Initial creation of `load_dataset()` function.
  - Basic CSV loading with `pd.read_csv` and `dropna()`.

---
