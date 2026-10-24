# Local replay audit (24 October 2026)

**Status:** End-to-end local replay **succeeded** using the two byte-identical source snapshots recorded
under `docs/DATA_PROVENANCE.md` and the packaged `notebooks/Source_Only_20PNG_20CSV.ipynb`
through `python scripts/run_analysis.py`.

## Execution checks

- Confirmed 10,830 stock market source rows, 7,672 tweets, 7,471 assigned sessions, 201 quarantined.
- Confirmed 6,945 eligible development observations and 3,540 eligible 2024 observations.
- Regularisation C = 1.0 selected from 2023, using the defined joint selection rule.
- Recomputed the six 2024 Macro-F1 values and bootstrap intervals, including Character TF-IDF
  Macro-F1 0.482647 and Availability Control 0.477834.
- Recomputed three stock-disjoint folds, each holding out five stocks.
- Created an output ZIP containing exactly 20 PNG (300 dpi) and 20 CSV files.

## Byte-level and numerical consistency

- **8 of 20 CSVs** were byte-identical to the committed reference set.
- **17 of 20 PNGs** were byte-identical to the notebook-original PNGs.
- The remaining tables show floating-point and optimization differences in probability scores and,
  in 2023 model development, small metric differences. Largest recorded absolute change in the
  2023 model-selection table was approximately **0.0005602** (accuracy); the chosen C stayed at 1.0.
- In Table 08, the largest absolute difference in recorded numeric model performance was about
  **0.0000004154** (log loss). The six reported 2024 Macro-F1 values matched.
- **Calibration exception:** a single example near a high-confidence bin threshold shifted between
  adjacent bins on reexecution. For a bin with 1–2 observations, this can yield a large relative
  change in that bin's observed accuracy, even though overall model diagnostics changed little.
  A per-bin curve should not be taken as a precise population calibration estimate.
- Regenerated Figures 06, 11 and 14 differed byte-for-byte; other figures matched.

These differences are documented, not hidden or rewritten. The archived `results/` remains the
user-supplied benchmark; local rerun outputs are saved separately in `artifacts/`, which Git ignores.

## Verification limits

A successful run of code on the same dataset is **technical reproducibility**, not external
replication or an independent prospective stock-market experiment. Changing package versions,
BLAS builds and hardware may affect floating-point and boundary-sensitive diagnostics.
The sample's economic significance, causal claims, source provenance and final journal eligibility
require additional expert assessment.

To inspect any rerun numerically, execute:

```bash
python scripts/compare_reproduction.py
```

from the repository root after a full local rerun. The comparator does not overwrite evidence.
