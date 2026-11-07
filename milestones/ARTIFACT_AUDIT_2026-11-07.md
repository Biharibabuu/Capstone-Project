# Capstone file audit — 7 November 2026

**Repository:** Biharibabuu/Capstone-Project  
**Branch:** main  
**Scope:** 61 files indexed under the Project Library folder /Capstone Project/ compared with the GitHub tree.

## Current repository coverage
- **M1/D1:** charter and master plan are in GitHub.
- **M2/D2:** audit summary, feasibility audit, workbook manifest, dictionary, source register, tracker and 30-Oct workbook versions are in GitHub.
- **M3/D3:** source-only notebook and review notes are in GitHub; output-rich local exports are not public.
- **M4/D4:** report, training source, notebook, tests, 12-run log, candidate comparison, metrics, test predictions, data checksum and environment are in GitHub.
- **M5/D5:** plan only; rolling-origin report/backtest pending.
- **M6/D6:** backend, frontend and four market connectors exist; approved model integration and monitoring evidence pending.
- **M7/D7:** final report, model card, presentation and demo pending.

See [ARTIFACT_INVENTORY_2026-11-07.csv](ARTIFACT_INVENTORY_2026-11-07.csv) for every Library file's name, path, received date, size, milestone assignment and GitHub handling status.

## New 7-Nov workbook receipts
- CP(5).xlsx: 157,304 bytes; CP(4).xlsx already exists at same size, but byte identity is unverified.
- CP Master Data(4).xlsx: 71,747 bytes; CP Master Data(3).xlsx exists at same size, but byte identity is unverified.
- Final_Quarterly_Data(2).xlsx: 99,836 bytes versus D4-v1 input 99,448 bytes; not reconciled.
- EDA ANALYSIS(3).xlsx: 13,233 bytes; older repository copy is same size, identity unverified.
- Data Audit Report Team-K.pdf: audit narrative is represented by D2 Markdown files.
- Latest D3 notebook/HTML exports are output-rich; the source-only notebook is already public.
- Latest D4 PDF has a same-named report in M4; exact binary identity is not verified.
- M4 ZIP is not duplicated because individual report/code/notebook/tests/metrics are committed.

Older D1/D2/D3 PDFs, ZIPs, screenshots, charts, planning notes and workbook versions are individually listed in the CSV inventory.

## D4 reproducibility lock
D4-v1 uses data/processed/Final_Quarterly_Data(1).xlsx, worksheet Final_Quarterly_Data, SHA-256 85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c. It has 38 source rows, 2 excluded and 35 supervised examples; train/validation/test = 21/6/8. Persistence validation MAE/RMSE = 12.18/13.92 pp; locked-test MAE/RMSE = 11.53/14.20 pp. Ridge and Random Forest did not beat validation persistence. No trained ML artifact was selected.

Do not silently replace the D4-v1 input with Final_Quarterly_Data(2).xlsx.

## Why local files were not all uploaded
The Project Library did not provide an authorised raw-binary export path for newer Excel/PDF/DOCX/ZIP files in this session. Therefore I could not upload original binary copies. I did not reconstruct binaries from extracted text or claim same-size files are identical. They are inventoried with handling decisions.

The public repository's docs/Data_Package_Manifest.md records permission for the earlier 30-Oct four-workbook package; that does not automatically cover new workbook versions or output-rich exports. Confirm Bloomberg/institutional terms before publishing more data. This audit did not remove the earlier Bloomberg-derived files already in GitHub.

## Remaining gates
1. Reconcile 7-Nov versions and compute checksums.
2. Confirm public redistribution permission for any new Bloomberg-derived data.
3. Re-run D3 on approved reconciled data.
4. Complete D5 point-in-time and rolling-origin evaluation.
5. Integrate D5-approved logic into D6 and add monitoring/security evidence.
6. Complete D7 report, model card, presentation and demo.
