# M2 / D2 — Data Audit: Milestone Control

**Status:** COMPLETED for the 30-Oct-2026 data package; newer workbook receipts require reconciliation before approval.

## Purpose
Establish data provenance, definitions, coverage, frequency, units, quality, representativeness, source access and model-readiness limits.

## Inputs
Raw and derived workbook versions are listed in 01_INPUTS/README.md and docs/Data_Package_Manifest.md. D4-v1 is pinned to Final_Quarterly_Data(1).xlsx; do not overwrite it.

## Working record
D2_Data_Audit_Summary.md, Data_Feasibility_Audit.md, IndiGo_Data_Dictionary.csv, source_register.csv and collection_tracker.csv.

## Deliverables
D2 data audit, source feasibility assessment, data dictionary and versioned data package manifest.

## Evidence
Source IDs, field names, coverage, sheet inventories, checksums, quality-control decisions, estimate flags, financial alignment issue and known limitations.

## Exit gate for a new data version
Reconcile raw IS financial fields, correct fiscal-quarter mapping, retain actual/estimate status, verify units and availability dates, run data-quality checks, calculate SHA-256 and approve a dated dataset manifest. The older D2 package is documented; the newest candidate files are not automatically model-ready.
