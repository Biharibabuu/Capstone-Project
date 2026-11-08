# Project Data Hub
### IndiGo Profitability Intelligence System

**Current project target:** Next-quarter EBITDA Margin (%) = EBITDA / Revenue from Operations × 100.  
**Data governance owner:** M2 / D2 — Data Audit.  
**Active modelling consumer:** M4 / D4 — Modelling.

This folder is the project-wide source catalogue and shared data infrastructure. It does not replace milestone-specific data records. Every milestone identifies the exact file version, source hash, transformation and purpose it consumes.

## 1. Data ownership by milestone

| Milestone | Data responsibility | Canonical location |
|---|---|---|
| M1 / D1 — Charter | Defines target, required inputs and governance requirements; no analytical dataset | [M1 workspace](../milestones/M1_D1_Project_Charter/) |
| M2 / D2 — Data Audit | Owns original financial and macro/market source files, dictionary, source register, collection tracker, quality checks and version approval | [M2 data workspace](../milestones/M2_D2_Data_Audit/data/) |
| M3 / D3 — EDA | Owns exact EBITDA-only analysis input, EDA notebook, outputs, hypotheses and insight log | [M3 data workspace](../milestones/M3_D3_Exploratory_Data_Analysis/data/) |
| M4 / D4 — Modelling | Owns active model-ready dataset, target/features, chronological splits, derived features and experiment lineage | [M4 data workspace](../milestones/M4_D4_Modelling/data/) |
| M5 / D5 — Evaluation | Freezes M4 model/data version; owns backtest predictions, errors and evaluation records | [M5 inputs](../milestones/M5_D5_Model_Evaluation/01_INPUTS/) |
| M6 / D6 — Deployment | Consumes D5-approved model and feature contract; owns runtime schemas, refresh logs and monitoring | [M6 inputs](../milestones/M6_D6_Deployment_Monitoring/01_INPUTS/) |
| M7 / D7 — Final Communication | References final approved data/model versions; owns publication-ready tables, charts and evidence | [M7 inputs](../milestones/M7_D7_Final_Communication/01_INPUTS/) |

## 2. Repository data structure

| Folder | Role | Rule |
|---|---|---|
| raw/ | Original source exports | Immutable; provenance required; publish only where permitted |
| processed/ | Shared or historical derived datasets | Version, lineage, quality status and checksum required |
| templates/ | Header-only import templates | No observations; never mistake for collected data |
| examples/ | Sample/example data | Label examples clearly; do not mix with actuals |
| source_register.csv | Publisher, source ID, fields, units and limitations | Update when a source changes |
| collection_tracker.csv | Coverage, status, blockers and next action | Update on each acquisition/reconciliation cycle |
| DATA_COLLECTION_REGISTER.md | Readable source inventory and version history | Link to milestone-level data ownership |

## 3. Current source inventory

| Dataset | Source identifier / fields | Frequency | Intended use | Current status |
|---|---|---:|---|---|
| IndiGo financial statements | INDIGO IN; SALES_REV_TURN and EBITDA | Quarterly | EBITDA Margin = EBITDA / Revenue from Operations × 100 | Source workbook present; verify statement definitions and alignment |
| USD/INR | USDINR REGN Curncy, PX_LAST | Monthly | Currency/macro predictor | Collected; apply historical availability cutoffs |
| CPI indicator | INFUTOTY Index, PX_LAST | Monthly | Inflation predictor | Series definition and unit need verification |
| WPI indicator | INBGWPIY Index, PX_LAST | Monthly | Inflation predictor | Definition and base-series continuity need verification |
| Dated Brent | EUCRBRDT Index, PX_LAST | Daily and monthly | Crude-oil benchmark proxy | Not IndiGo's realised ATF price or fuel spend |

The source export contains actual financial periods through 30 June 2026 and later estimated rows. Estimated periods are not actual labels. The USD/INR export includes a 30 October 2026 observation; apply a historical availability cutoff at each forecast origin.

## 4. Derived dataset register

| Dataset | Milestone | Path | Status / use |
|---|---|---|---|
| Final_Quarterly_Data(1).xlsx | D4-v1 historical benchmark | processed/ | Immutable historical experiment input; known alignment/quarter-label limitations remain |
| Final_Quarterly_Data(3).xlsx | Candidate quarterly panel | Local candidate, not in repository | Not approved until reconciled to raw statement and market series |
| EDA_ANALYSIS_EBITDA_ONLY_38Q.csv | D3 EDA | M3/data/ | 38-quarter, eight-field EBITDA-only analysis extract |
| Current M4 model-ready table | D4 active modelling | M4/data/ | Not yet frozen; must be built from reconciled actuals with leakage controls |

The legacy D4-v1 run is historical evidence, not an approved EBITDA-margin model. Do not carry its metrics forward as current EBITDA model performance.

## 5. Data alignment and modelling rules

1. Target: EBITDA Margin (%) = EBITDA / Revenue from Operations × 100. Net Income is not the target or a model feature.
2. Rebuild financial outcomes from raw quarterly statement rows; do not use the legacy Financial source sheet documented as shifted by two quarters.
3. Use Indian fiscal quarters consistently: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar. Retain original source date.
4. Exclude estimated financial rows from realised target labels.
5. Separate observation dates from publication/availability dates; use only inputs available at each forecast origin.
6. Document daily/monthly-to-quarter aggregation rules and avoid redundant/collinear features without justification.
7. Do not bridge missing target quarters when creating one-quarter-ahead labels.
8. Every derived dataset records parent hashes, transformation version, row count, coverage, units and quality checks.
9. Do not publish licensed data unless redistribution is explicitly permitted.

## 6. File navigation

- [Raw sources and provenance](raw/README.md)
- [Processed datasets and version controls](processed/README.md)
- [Header-only mapping templates](templates/)
- [Data Collection Register](DATA_COLLECTION_REGISTER.md)
- [Source Register](source_register.csv)
- [Collection Tracker](collection_tracker.csv)
- [Milestone archive](../milestones/README.md)

## 7. Current data handoff

M2 owns source audit; M3 owns the EDA panel and outputs; M4 must construct and freeze the active EBITDA model table. M5–M7 consume approved, versioned upstream artifacts. Never silently replace a workbook or label an unreviewed dataset as model-ready.