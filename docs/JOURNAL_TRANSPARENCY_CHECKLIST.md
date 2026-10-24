# Journal alignment, audit scope, and disclosure checklist

**Target journal format:** SN Computer Science (Springer Nature), https://link.springer.com/journal/42979/submission-guidelines. This evidence repository is a companion to a separately submitted manuscript and does not imply journal acceptance or a Scopus quartile. Journal category rankings must be checked for the applicable indexing database and year. 

## What is publicly auditable here?

| Claim | Evidence in repository | What the evidence cannot establish |
|---|---|---|
| Original dataset version and population | `docs/DATA_PROVENANCE.md`, DOI and byte hashes | Original vendor or tweet collection completeness |
| Recorded sample split | Tables 01 and 03, documented code | Independent external sample |
| Model development choices | Tables 06–07; notebook code | Training identical across every software/platform version |
| Chronological test scoring | Table 08; other classwise tables | Future trading profitability or causal explanation |
| Lexical comparison uncertainty | Tables 16–17; Figures 18–19 | Certainty of superiority, full model-selection uncertainty |
| Stock-exclusion comparison | Tables 19–20; Figure 20 | Generalization to unseen markets or a new calendar year |
| Code and result integrity | `audit/evidence_manifest.json`, `scripts/verify_repository.py`, GitHub Actions | Independent retraining from third-party data |
| Local rerun | `docs/REEXECUTION_REPORT.md` | Perfect bitwise equivalence or an external verification certificate |

## Scientific interpretation controls

- All final numerical claims must be traceable to the 20 user-supplied CSV tables or the executable notebook output, not inferred from the plots alone.
- Distinguish `model development (2022–2023)` and `chronological evaluation (2024)`; never use the 2024 labels for supervised model fitting or hyperparameter choice.
- Report that 2024 Macro-F1 is 0.482647 for Character TF-IDF and 0.477834 for the matched Availability Control; their paired difference is 0.004814 with bootstrap 95% CI containing zero. Do **not** claim statistically established lexical superiority.
- Report log loss, Brier, per-class recalls and calibration alongside Macro-F1; score directions and rankings differ by metric.
- Explain the effect of market inactivity and the missingness mechanism; an empty tweet archive is not proof of no investor discussion.
- Stock-disjoint folds exclude five tickers per fold from labelled supervised fitting but are still within the same data collection and 2024 period.
- Explain that a static GitHub Actions success checks files/consistency only. A full independent reproduction requires the dataset, environment, and experimental code, and should report deviations.

## Pre-submission actions for the human authors

- [ ] Confirm manuscript author identities, affiliations, corresponding author, author contributions and conflict-of-interest statements outside this repository.
- [ ] Confirm the source data licensing and platform usage obligations before making the repository public.
- [ ] Verify access to the DOI and source-version checksums; give readers reproducible data-acquisition instructions.
- [ ] Run the notebook with the original dataset and record a `pip freeze` / Python version for each documented experimental release.
- [ ] Verify numerical statements against the 20 CSV files, not only figure annotations.
- [ ] Preserve experimental negative results and uncertainty intervals; do not change thresholds or split ex post to force significance.
- [ ] Verify cited bibliographic metadata and align the manuscript's Code Availability and Data Availability statements with the actual published URL/DOI.
- [ ] Follow the current journal requirements for data, ethics, declarations, copyright, supplementary material, and editable source files **through the journal submission system**. The manuscript and RIS are deliberately excluded from this GitHub archive, but the journal may still require a DOCX/LaTeX manuscript submitted separately.
- [ ] Clarify the actual contribution of assistance from AI coding/writing tools in accordance with the journal's policy and the authors' responsibilities.
- [ ] If deposit/preservation is needed, archive a specific GitHub release via an established archival service and only cite a DOI after issuance.

**Do not describe this repository as “Q1-certified”, a clinical-style external validation, or proof of investment profit.**
