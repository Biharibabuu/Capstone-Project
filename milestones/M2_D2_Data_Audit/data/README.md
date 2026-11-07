# M2 Data Folder — Source and Audit Data

This folder is the milestone-level data index. Canonical source workbooks are maintained once in the repository's shared data area to avoid uncontrolled duplicate copies.

## Canonical data locations

| Data class | Canonical repository location | Use |
|---|---|---|
| Raw source workbook | [data/raw/CP(4).xlsx](../../../data/raw/CP%284%29.xlsx) | Original Bloomberg source export, immutable |
| Raw master indicators | [data/raw/CP%20Master%20Data(3).xlsx](../../../data/raw/CP%20Master%20Data%283%29.xlsx) | Monthly/daily macro and market series |
| Derived quarterly workbook | [data/processed/Final_Quarterly_Data(1).xlsx](../../../data/processed/Final_Quarterly_Data%281%29.xlsx) | D4-v1 locked input snapshot; preserve checksum |
| EDA workbook | [data/processed/EDA%20ANALYSIS(2).xlsx](../../../data/processed/EDA%20ANALYSIS%282%29.xlsx) | Historical flat EDA input, not the authoritative target source |

## Supporting records

- [Data package manifest](../Data_Package_Manifest.md)
- [Source register](../../../data/source_register.csv)
- [Collection tracker](../../../data/collection_tracker.csv)
- [Data dictionary](../IndiGo_Data_Dictionary.csv)
- [Audit report](../D2_Data_Audit_Summary.md)

## Incoming versions and rights gate

Newer 7-Nov workbooks are listed in the audit inventory but are not promoted to approved/raw data. Reconcile their content and checksums against the canonical set and confirm redistribution permission before committing them. Do not overwrite D4-v1's locked input.

## Data folder convention

- `raw/`: unchanged source files with provenance and redistribution decision.
- `processed/`: reproducible derived datasets with source hashes and transformation code.
- `quarantine/`: unapproved, unreconciled or rights-pending files (do not use for modelling).
- Every file must appear in the manifest with version, owner, date, units, checksum and approval status.
