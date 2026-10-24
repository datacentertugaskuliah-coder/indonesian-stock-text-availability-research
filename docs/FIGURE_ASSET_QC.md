# Figure asset resolution and selection audit

The repository uses the **original PNG files inside** the earlier source-only notebook's
`Q1_Results_20PNG_20CSV.zip`, not resized image attachments displayed in chat.

Comparison of all 20 images found that **17 inline-upload previews differ byte-for-byte** from
the original notebook ZIP. These displayed images had been downscaled to approximately 2048 px
wide and lost the original DPI metadata. Three were byte-identical. For publication-quality
traceability and 300-dpi preservation, the 20 unmodified original PNGs were restored to
`results/figures/`. The study figures' underlying numerical CSV tables are unchanged.

`audit/evidence_manifest.json` stores the SHA-256 of each committed, original-size PNG.
The image resolution checker requires an explicit 300 DPI PNG pHYs tag.

The journal submission guidelines also request figure captions outside the figures.
The archived 20 figures are computational diagnostic outputs and may contain embedded titles.
Do not treat the archive images as final editorial artwork without checking figure formatting.
