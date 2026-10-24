# Reproduce the recorded results

## First: static verification without raw source

```bash
python scripts/verify_repository.py
```

Verifies the published 20+20 artifact set and compares it with a checked-in SHA-256 manifest.
GitHub Actions automatically repeats this check on every push and pull request.
No private account, secret token, DOI download or raw tweet access is needed.

## Second: full model run using user-downloaded licensed originals

1. From https://doi.org/10.17632/rkpkkd2mhf.5 download the stock-market and Indonesian tweet source CSVs.
2. Save as `data/raw/Stock Market Data(2).csv` and `data/raw/Tweet Data - ID(2).csv`.
3. Verify SHA-256 values from `docs/DATA_PROVENANCE.md`.
4. Use Python 3.11–3.13 with packages in `requirements.txt`.
5. At repo root execute:

```bash
python -m pip install -r requirements.txt
python scripts/run_analysis.py
```

Or open the Jupyter notebook `notebooks/Source_Only_20PNG_20CSV.ipynb`
and run all cells. The notebook checks input shape, exact hashes, source keys,
target construction, and leakage-sensitive transformations.

Alternative source locations can be set through environment variables
`STOCK_MARKET_CSV` and `STOCK_TWEET_CSV` pointing to complete file paths.
Optional `STOCK_OUTPUT_DIR` overrides the **local** generated artifacts path.

## Outputs

Local model runs write generated files to `artifacts/`, not to the committed reference
`results/` folder. The final notebook cell produces `Q1_Results_20PNG_20CSV.zip`
with **exactly 20 CSV and 20 PNG** inside.
Do not copy newer experiments into committed `results/` without a new documented version,
code hash and analytical justification.

## Colab and Kaggle

Upload the notebook to Google Colab and upload the two source CSVs when prompted.
In Kaggle, attach the two source CSVs as notebook input files before execution.
The notebook automatically calls `google.colab.files.download` only in Colab.
In Kaggle it displays a clickable FileLink to the ZIP in `/kaggle/working/`.
It does not use a global JavaScript `download` function.

## Computational uncertainty

Library versions and optimization solvers can change small decimal digits and runtime.
The original Table 05 contains the original run's reported runtime metadata. Store
`python --version` and `python -m pip freeze` for each independent reproduction.
Static hash equality compares **reference artifacts only**; numerical matching under new
environments should use a prespecified tolerance rather than demanding identical ZIP hashes.

## Peer reviewer checklist

- [ ] Download datasets from the declared DOI and confirm the exact source version/licence.
- [ ] Confirm both SHA-256 hashes (do not bypass failed checks).
- [ ] Run all notebook cells sequentially; record local environment and seed.
- [ ] Inspect the output ZIP counts, 2022/2023/2024 split and sample exclusions.
- [ ] Recompute Macro-F1, log loss, Brier and contrasts on new predictions.
- [ ] Check that 2024 labels never inform preprocessing, selection, or model fitting.
- [ ] Inspect bootstrap interval, null included/excluded, adjusted p and cross-stock transfer.
- [ ] Report all deviations, including non-reproducible outcomes or licence restrictions.

See [`REEXECUTION_REPORT.md`](REEXECUTION_REPORT.md) for actual local replay diagnostics, including a calibration-bin sensitivity discrepancy.
