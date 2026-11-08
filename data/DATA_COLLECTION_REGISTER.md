# Data Collection Register
### IndiGo Profitability Intelligence System

**Last reviewed:** 8 November 2026  
**Data steward:** M2 / D2 — Data Audit  
**Primary project target:** Next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.

This register identifies the actual input workbooks, their tabs, source identifiers and downstream milestone use. It distinguishes original sources, derived analytical extracts and model snapshots. A workbook existing in GitHub does not by itself mean it is approved for modelling.

---

## 1. Source workbook inventory

### 1.1 Raw company and macro/market workbook — CP(4).xlsx

**Repository file:** [CP(4).xlsx](raw/CP%284%29.xlsx)  
**SHA-256:** `208fc66a69c548023c4591bb8b7b5ba41624cdfe56fdd757612cc7b5fd01879e`  
**Owning milestone:** M2 / D2 — Data Audit.

| Sheet | Dataset | Frequency | Bloomberg source / fields | Downstream usage |
|---|---|---|---|---|
| `IS` | IndiGo financial statements | Quarterly | `INDIGO IN`; `SALES_REV_TURN`, `EBITDA` | Source for EBITDA-margin construction. Exclude rows marked Est from realised targets. |
| `usd inr` | USD/INR exchange rate | Monthly | `USDINR REGN Curncy`; `PX_LAST`, `PX_BID` | Candidate currency predictor, subject to historical availability cutoff. |
| `cpi` | CPI inflation indicator | Monthly | `INFUTOTY Index`; `PX_LAST` | Candidate inflation predictor; exact series description/unit to be confirmed. |
| `wpi` | WPI inflation indicator | Monthly | `INBGWPIY Index`; `PX_LAST` | Candidate inflation predictor; verify base-series history. |
| `co new` | Dated Brent crude benchmark | Daily | `EUCRBRDT Index`; `PX_LAST` | Oil-market proxy, not Indian ATF or IndiGo's realised fuel cost. |
| `co new monthly` | Dated Brent crude benchmark | Monthly | `EUCRBRDT Index`; `PX_LAST` | Monthly representation of the same benchmark; assess redundancy with daily-derived mean. |

Actual financial period ends extend through 30 June 2026; later periods in the export are estimates, not actual outcomes. The monthly USD/INR workbook contains a 30 October 2026 observation; include it in historical forecasting only if availability by the forecast cutoff is verified.

### 1.2 Consolidated historical workbook — CP Master Data(3).xlsx

**Repository file:** [CP Master Data(3).xlsx](raw/CP%20Master%20Data%283%29.xlsx)  
**SHA-256:** `30220588fe96276662a8eeadf56ea6a583da71479e0e26923383c517cc8af474`  
**Owning milestone:** M2 / D2 — Data Audit.

The workbook consolidates historical series and includes a legacy `Financial source` sheet. That sheet was found to be shifted by two quarters relative to raw CP `IS`. It is retained as audit/reference evidence only and must not be used to construct the EBITDA-margin target.

---

## 2. Derived data and milestone allocation

| Artifact | Location | Owner / milestone | Status and purpose |
|---|---|---|---|
| `Final_Quarterly_Data(1).xlsx` | [data/processed](processed/Final_Quarterly_Data%281%29.xlsx) | M4 historical D4-v1 reference | Immutable D4-v1 benchmark snapshot. Do not assume it is the approved active EBITDA model table. |
| `EDA_ANALYSIS_EBITDA_ONLY_38Q.csv` | [M3 data](../milestones/M3_D3_Exploratory_Data_Analysis/data/EDA_ANALYSIS_EBITDA_ONLY_38Q.csv) | M3 / D3 | 38-quarter, eight-field EBITDA-only EDA input. |
| `Final_Quarterly_Data(3).xlsx` | Local candidate only | M2 review → M4 potential input | Not committed/approved; reconcile against raw financial and market sources first. |
| `m4_ebitda_model_panel_v1` | To be created under [M4 data](../milestones/M4_D4_Modelling/data/) | M4 / D4 | Required active model-ready table; not yet frozen. |
| D5 rolling-origin panel | To be created under M5 evidence | M5 / D5 | Evaluation folds, predictions and errors tied to exact selected M4 data/model version. |

## 3. Target and feature contract

| Variable | Role | Definition / source | Control |
|---|---|---|---|
| EBITDA Margin (%) | Sole primary target | EBITDA / Revenue from Operations × 100 | Verify source definitions and denominator; actual reported periods only. |
| USD/INR | Candidate predictor | Monthly `USDINR REGN Curncy` `PX_LAST` | Aggregate consistently; respect point-in-time availability. |
| CPI indicator | Candidate predictor | `INFUTOTY Index` `PX_LAST` | Verify series description and units. |
| WPI indicator | Candidate predictor | `INBGWPIY Index` `PX_LAST` | Verify definition and base continuity. |
| Dated Brent proxy | Candidate predictor | `EUCRBRDT Index` `PX_LAST`, daily/monthly | Proxy only; document frequency conversion and check redundancy. |

Net Income may remain in the original financial statement export for source audit/reconciliation. It is not the project's target or a model feature.

## 4. Milestone data flow

1. **M1 / D1:** establishes EBITDA-margin target, forecast horizon and data requirements.
2. **M2 / D2:** owns original files, data dictionary, source register, collection tracker, quality findings, hashes and approval status.
3. **M3 / D3:** creates and analyses the EBITDA-only 38-quarter EDA panel; documents hypotheses, outputs and limitations.
4. **M4 / D4:** builds a separate, reconciled one-quarter-ahead EBITDA model table from approved M2 sources and M3 handoff; owns features, splits and experiment lineage.
5. **M5 / D5:** freezes the exact M4 model/data vintage and creates rolling-origin evaluation folds, predictions and error measures.
6. **M6 / D6:** uses the D5-approved model and feature contract; owns runtime input snapshots, refresh logs and forecast records.
7. **M7 / D7:** references approved dataset versions and hashes in the final report, presentation and demonstration.

## 5. Data quality and approval requirements

Before a derived dataset is promoted to modelling use:
- Rebuild financial records from raw CP `IS`; do not use the shifted master financial tab.
- Verify the EBITDA and Revenue from Operations line definitions and units.
- Exclude financial periods marked Est from realised target labels.
- Use Indian fiscal quarters consistently: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar.
- Retain original observation dates and record publication/availability dates separately where available.
- Aggregate daily/monthly predictors using documented rules and only observations available at the forecast cutoff.
- Do not bridge missing target quarters when producing a one-quarter-ahead label.
- Record parent-source hashes, transformations, row counts, coverage, missingness, units, quality flags and reviewer approval.
- Confirm Bloomberg/institutional redistribution rights before committing new raw or derived source data.

## 6. Public validation references

- [IndiGo quarterly financial results](https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html)
- [RBI Reference Rate Archive](https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx)
- [MoSPI CPI Catalogue](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI)
- [Office of the Economic Adviser WPI Data](https://eaindustry.nic.in/download_data_2223.asp)
- [Bloomberg Terminal](https://professional.bloomberg.com/products/bloomberg-terminal/) — source access reference, not a public download URL.

## 7. Related records

- [Project Data Hub](README.md)
- [Source Register](source_register.csv)
- [Collection Tracker](collection_tracker.csv)
- [Raw data folder](raw/README.md)
- [Processed data folder](processed/README.md)
- [M2 data package](../milestones/M2_D2_Data_Audit/data/README.md)
- [M3 EDA input](../milestones/M3_D3_Exploratory_Data_Analysis/data/README.md)
- [M4 modelling data package](../milestones/M4_D4_Modelling/data/README.md)
- [Milestone archive](../milestones/README.md)
