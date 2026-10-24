# Methods, statistical claims, and limitations

## Design and estimands

The study asks whether text **availability** and **lexical content** carry separately measurable
predictive information for next-session **three-class** stock movement. This is an association/prediction
study, not a randomized causal intervention.

**Sample:** 15 securities, source 2022–2024, observed market sessions only. Eligible counts:
2022 = 3,375; 2023 = 3,570; 2024 = 3,540.

**Temporal design:** 2022 fitting and 2023 model selection, then 2022–2023 final fit,
2024 chronological test. The design is temporally out of sample but should **not** be
called a new independent market sample or independent external validation.

**Input design:** price and volume histories, calendar descriptors, archival tweet-presence
and counts, with train-fitted TF-IDF/SVD text representations. The source data are
third-party public records; the analyses are carried out on these records.

**Primary measures:** multiclass Macro-F1, balanced accuracy, log loss, multiclass Brier,
seven-bin top-label ECE and classwise recall. Higher Macro-F1 is not equivalent to
better calibrated probabilities.

**Matched lexical attribution:** Word / Character / Hybrid all extend the same
market + availability controls. The Extra Trees baseline changes estimator family
and is a descriptive nonlinear benchmark, **not** a causal attribution comparator.

## Key observed results on the same 3,540 observations in 2024

- Market Macro-F1: 0.440106
- Availability control Macro-F1: 0.477834
- Word Macro-F1: 0.476337
- Character Macro-F1: 0.482647
- Hybrid Macro-F1: 0.474165
- Extra Trees + Availability Macro-F1: 0.459374

Character minus availability: +0.004814 Macro-F1; paired date-block bootstrap,
2,000 replicates, block length 10 sessions, 95% CI about [-0.005534, +0.014047].
Holm p about 0.996 for the three prespecified lexical contrasts at this block length.
This supports no statistically established lexical superiority in the provided test.

Ticker-disjoint pooled Macro-F1 (3 folds of five held-out stocks):
Market 0.435706, Availability 0.467972, Character 0.470169.
This transfer design still draws from the same market source and time span.

## Scientific limitations and safeguards

1. **Scope**: 15 retrospectively selected, speculative/illiquid securities; no broad IDX population inference.
2. **Observation process**: absence of a tweet in the archive is not proof of zero public discussion.
3. **Target**: numerical-zero Flat category differs from economically non-trivial flat-return bands;
   zero-volume trading may dominate certain labels.
4. **Timestamp**: alignment uses supplied trading-session mapping; not an independently verified exchange audit.
5. **Dependence**: date-block resampling is conditional on already fitted predictions; it does not
   capture model-refitting or hyperparameter-selection uncertainty.
6. **Multiple testing**: Holm correction in Table 17 covers only the three lexical Macro-F1 contrasts
   for each block length; it does not retroactively correct every exploratory analysis.
7. **Cross-stock transfer**: ticker-disjoint folds are within the same dataset, not external validation.
8. **Potential temporal drift**: model scores worsen in the second half of 2024. Interpret average-period
   metrics with the observed within-year heterogeneity.
9. **Calibration**: top-label ECE depends on seven-bin definitions; assess log loss and Brier as well.
10. **Evidence**: this archive contains outputs and a runnable notebook, not a third-party reproduction
    certificate. Independent users must rerun it from the source files and verify differences.
11. **No profitability proof**: no execution costs, slippage, transaction constraints, or investable backtest.
12. **Research ethics**: source data contain social-media-derived text; follow original license and publisher
    privacy/usage requirements. No full tweet content is redistributed here.

## Output provenance

All 20 result CSVs and the 20 original 300-dpi plots are preserved byte-for-byte from the experiment ZIP (not chat-resized image previews)
and are accompanied by SHA-256 hashes. GitHub Actions verifies these stored artifacts.
The public repository's static audit cannot certify that the original code was executed as declared;
full computation reproducibility requires source downloads and running all notebook cells.

## Journal scope

Journal author's instructions: https://link.springer.com/journal/42979/submission-guidelines
A repository supports data/code transparency but does **not** itself guarantee publication,
novelty, ethical clearance, Q1 classification or acceptance.
