# Separating text availability from lexical information in Indonesian stock prediction

[![Static evidence audit](https://img.shields.io/badge/audit-local%20%2B%20GitHub%20Actions-informational)](#evidence-integrity)

This repository is a **research reproducibility companion**, not the submitted manuscript.
It documents an observed-source, three-class, next-session price-movement study on 15 Indonesian equities
(2022–2024) and makes the training notebook, 20 study tables and 20 figures auditable.

**This archive contains NO manuscript DOCX, RIS references, original raw tweet text, or synthesized observations.**
It contains exactly 20 committed analysis CSV tables and 20 committed figure PNG files. The original
licensed source data must be obtained separately from the publisher's canonical version.

## Quick start: GitHub Desktop (Bahasa Indonesia)

**Mulai dari [`START_HERE_GITHUB_DESKTOP_ID.md`](START_HERE_GITHUB_DESKTOP_ID.md)** untuk panduan unggah ZIP ke GitHub Desktop, baik repositori baru maupun repositori yang sudah ada. Awali sebagai **private** hingga lisensi dan kelengkapan file selesai ditinjau.

**Checklist audit untuk reviewer:** [`docs/JOURNAL_TRANSPARENCY_CHECKLIST.md`](docs/JOURNAL_TRANSPARENCY_CHECKLIST.md). Dokumen ini membedakan pemeriksaan berkas, reproduksi komputasi, dan validasi ilmiah independen. The committed `results/` directory is a frozen reference set and a reproducible rerun is generated under ignored `artifacts/`.

## Source, attribution and reuse

**Sanjaya, M., Setyo Nugroho, K., Martianus Henry, M., Pardamean, B., & Intanie Dewi, V. (2026).**
*Indonesian Non-Blue-Chip Stocks: A Public Dataset of Daily Market Data and Tweets*. Mendeley Data,
version 5. https://doi.org/10.17632/rkpkkd2mhf.5

The publisher identifies the source licence as **CC BY-NC 4.0**. See
[`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md) before using or redistributing source data.
This repository does not claim ownership of the source dataset or an unrestricted licence for the code.

## Experimental design

| Scope | Training/development | Evaluation |
|---|---:|---:|
| Original observed market sessions | 7,275 in 2022–2023 | 3,555 in 2024 |
| Eligible observations | 6,945 | 3,540 |
| Distinct tickers | 15 | 15 |

- Target: next **observed** session's close-to-close movement, Down, Flat, Up (numerical-zero tolerance: 1e-10).
- Sequential development: 2022 fitting with 2023 hyperparameter validation; final 2022–2023 refit.
- Chronological evaluation: 2024. All 2024 target labels are excluded from the documented final fitting/tuning.
- Models: Market, Market + Availability, Word TF-IDF, Character TF-IDF, Hybrid TF-IDF, Extra Trees + Availability.
- Additional diagnostics: classwise scores, probability losses, 7-bin ECE, 2,000 date-block bootstrap resamples
  with 5/10/20-session blocks, lexical masking, and 3-fold five-stock-exclusion transfer evaluation.
- No forward-filled non-trading days are introduced as independent market observations.
- Splitting tweets is based on **assigned trading session**, not tweet publication year.

## Reproducing the experiment

1. Download the original **Stock Market Data** and **Tweet Data - ID** CSV files from the DOI above.
   Place these exact source CSV files as `data/raw/Stock Market Data(2).csv` and
   `data/raw/Tweet Data - ID(2).csv`. Their SHA-256 values **must** match the identifiers documented
   in [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md). If the publisher download has a different
   byte representation, do **not** bypass the assertion; audit that file's provenance first.
2. Open a terminal in the repository root. Run `python -m pip install -r requirements.txt`.
3. Open `notebooks/Source_Only_20PNG_20CSV.ipynb` in Jupyter and run all cells in order,
   **or** run `python scripts/run_analysis.py` from the repo root.
4. The run writes `artifacts/Q1_20PNG_20CSV/{tables,figures}` and
   `artifacts/Q1_Results_20PNG_20CSV.zip`. This generated folder is ignored by Git.
5. Compare computed values to `results/tables` using the audit instructions. Minor floating-point drift
   across dependency versions may occur; see [`docs/REEXECUTION_REPORT.md`](docs/REEXECUTION_REPORT.md)
   for an actual end-to-end replay and its recorded deviations.

For Colab or Kaggle, follow [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Repository layout

```text
notebooks/Source_Only_20PNG_20CSV.ipynb   executable research notebook
scripts/run_analysis.py                   local notebook runner
scripts/verify_repository.py              strict static integrity & evidence checker
results/tables/Table_01 ... Table_20       observed result tables (CSV)
results/figures/Figure_01 ... Figure_20    observed result plots (PNG)
audit/evidence_manifest.json              file hashes and sizes
docs/DATA_PROVENANCE.md                    primary source, hashes, licences
docs/METHODS_AND_LIMITATIONS.md            split, estimands, scope, limitations
docs/TABLE_FIGURE_INDEX.md                navigation for the 40 evidence items
docs/REPRODUCIBILITY.md                   input, execution, environment, review
docs/GITHUB_DESKTOP_ID.md                 GitHub Desktop step-by-step (Bahasa Indonesia)
data/raw/                                  ignored, local-only inputs
.github/workflows/evidence-audit.yml       automated artifact verification
```

## Evidence integrity

To validate **the archived evidence without source data**:

```bash
python scripts/verify_repository.py
```

The script validates counts, hashes, PNG structure and DPI metadata, annual sample counts,
class distribution, six model metrics, 2024 confusion-matrix rows, the primary bootstrap
contrast and three-fold holdout totals. GitHub Actions runs the same static validation on push.
**Passing this static audit does not independently retrain the models or certify scientific validity.**
Full experimental reproduction requires the original source and notebook.

## Main empirical result

The 2024 Macro-F1 of the Character TF-IDF model is **0.482647**, compared with
**0.477834** for Market + Availability. The difference, **+0.004814**, has a paired 10-session
block-bootstrap 95% interval **[-0.005534, +0.014047]**. Zero lies in this interval.
The reported model therefore does **not** establish significant lexical superiority.
Market-only yields the lowest observed multiclass log loss and Brier score among the six models.

Archived figure assets preserve the notebook ZIP originals at 300 dpi; see [`docs/FIGURE_ASSET_QC.md`](docs/FIGURE_ASSET_QC.md).

This repository is an evidence archive, **not** a certification of Scopus Q1 readiness,
external validation, causal impact, or trading profitability. See the limitations document.

## Publication and metadata status

Author names, affiliations, grant identifiers, ethics declarations, repository DOI and final
manuscript submission status are **not populated** here. The research team must verify these
before manuscript submission. Do not infer a journal's ranking from the publisher name.

## Notebook documentation update

The notebook contains expanded **English-language, review-oriented Markdown and code comments**
covering provenance, feature timing, leakage controls, matched comparisons, probability
metrics, bootstrap inference, lexical masking, ticker-disjoint evaluation and delivery.
The executable statistical algorithm and configuration are unchanged; only the Kaggle
download-link label was translated to English. This documentation-only revision does not
change the 20 archived CSV tables or 20 PNG figures.
