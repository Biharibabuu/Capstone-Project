# M2 / D2 — Data Package
### Source of truth for data provenance

**Status:** Done  
**Stewardship:** Raw source inventory, definitions, quality audit, source register and version approval.  
**Project target:** Next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.

## 1. Source files stored here

| File | Source contents | Purpose | Integrity |
|---|---|---|---|
| [CP(4).xlsx](raw/CP%284%29.xlsx) | Raw IndiGo IS, USD/INR, CPI, WPI, Dated Brent daily and monthly tabs | Immutable primary source export | SHA-256: 208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e |
| [CP Master Data(3).xlsx](raw/CP%20Master%20Data%283%29.xlsx) | Consolidated indicators and legacy financial-source tab | Reference workbook; financial source tab not approved due to two-quarter shift | SHA-256: 30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474 |
| [Final_Quarterly_Data(1).xlsx](processed/Final_Quarterly_Data%281%29.xlsx) | Quarterly panel plus calculation and quality sheets | D4-v1 historical benchmark; not the approved current EBITDA model table | Verify hash against the file manifest before use |

## 2. Source fields and meaning

| Data domain | Source ID / fields | Frequency | Use and caveat |
|---|---|---|---|
| Company statements | INDIGO IN; SALES_REV_TURN, EBITDA | Quarterly | Reconcile revenue to Revenue from Operations and EBITDA to reported statement; calculate sole project target |
| FX | USDINR REGN Curncy; PX_LAST | Monthly | Candidate currency indicator; apply availability cutoff |
| CPI | INFUTOTY Index; PX_LAST | Monthly | Verify exact series definition and units |
| WPI | INBGWPIY Index; PX_LAST | Monthly | Verify definition and historical base continuity |
| Oil | EUCRBRDT Index; PX_LAST | Daily / monthly | Dated Brent proxy, not Indian ATF or IndiGo realised fuel cost |

Net Income may remain in the untouched source statement for audit context. It is not the target or a predictor in this project.

## 3. Audit findings and treatment

- Raw IS is the financial source of record.
- The master workbook's Financial source tab is shifted by two quarters; do not use it for target labels.
- Rows marked Est are estimates, not realised outcomes.
- Observation date and public availability date differ; historical availability timestamps are incomplete.
- Dated Brent is a crude benchmark proxy only.
- Passenger load factor, yield, capacity and realised ATF costs are not in the supplied workbooks.

## 4. Handoff by milestone

| Consumer | Purpose | Rule |
|---|---|---|
| M3 / D3 | Build EDA panel | Use approved EBITDA analysis fields; record exact input hash and quarter labels |
| M4 / D4 | Build active forecasting table | Rebuild from actual IS, verify denominator, use fiscal quarters, document aggregation and point-in-time cutoffs |
| M5 / D5 | Freeze evaluation data | Use exact version used by selected M4 model |
| M6 / D6 | Runtime input contract | Use source definitions and schemas; no training workbook copy required |
| M7 / D7 | Final evidence | Cite versioned dataset IDs and hashes; respect redistribution rights |

## 5. Governance

Keep raw workbooks immutable. Record source, sheet, field, units, frequency, retrieval date, coverage, actual/estimate flag, availability date where known, rights status and checksum. Approve derived datasets only after reconciliation and quality review.

## 6. Audit records

- [D2 audit summary](../D2_Data_Audit_Summary.md)
- [Feasibility audit](../Data_Feasibility_Audit.md)
- [Package manifest](../Data_Package_Manifest.md)
- [Source register](../source_register.csv)
- [Collection tracker](../collection_tracker.csv)
- [Data dictionary](../IndiGo_Data_Dictionary.csv)