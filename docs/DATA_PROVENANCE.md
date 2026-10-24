# Data provenance, authenticity and legal notice

## Canonical source

Sanjaya M; Setyo Nugroho K; Martianus Henry M; Pardamean B; Intanie Dewi V.
Indonesian Non-Blue-Chip Stocks: A Public Dataset of Daily Market Data and Tweets.
Mendeley Data, version 5, published 30 September 2026.
DOI: https://doi.org/10.17632/rkpkkd2mhf.5

Source page identifies licence **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
Reuse requires attribution, indicating modifications, and respecting non-commercial restrictions.
These licence terms do not necessarily override platform terms applicable to republishing social-media content.
For these reasons the public GitHub package excludes original tweet text and market source snapshots.
Original source availability is via the dataset DOI, not a second unofficial publisher.

## Byte-identical source versions used for the archived tables

| File | Observed records | Verified SHA-256 |
|---|---:|---|
| `Stock Market Data(2).csv` | 10,830 | `51c847f70cd310806b90a62dd551779e9ef43480a07714a5189fc884f43aaff6` |
| `Tweet Data - ID(2).csv` | 7,672 | `4c513609af0342ed968f3ee26381a823bf158ca2661ad2b8894c2989aa669deb` |

Matching **byte hashes** verifies exact source snapshots, not the underlying financial data vendor or tweet collection process.
Sourced data are not claimed to be collected independently by the study author(s).

## Key accounting checks

- Market panel covers 15 named tickers, 2022–2024, 10,830 original session rows.
- Tweet records: 7,672 total; 7,471 assigned to observed trading sessions, 201 unassigned/quarantined.
- Of the assigned posts, 2,562 belong to trading sessions in 2022–2023 and 4,909 to sessions in 2024.
- Fifteen posts published in December 2023 were assigned to 2 January 2024; these are **2024-side input records**.
- Analytical observations after feature warm-up and same-year target rules: 3,375 in 2022;
  3,570 in 2023; and 3,540 in 2024.

## Data privacy and scope

The provider reports that the tweet data were cleaned and anonymized. This repository
neither republishes full tweet text nor claims additional identification screening.
The source's selected stock universe is not a random sample of all IDX securities.

## How to obtain source data locally

Place source files under `data/raw/` using the names above. The notebook detects the
files by SHA-256; the filename by itself is not sufficient to pass the audit.
`data/raw/` is deliberately excluded by `.gitignore` to prevent publishing raw tweet text.
Do not force-add that folder when publishing with GitHub Desktop.
