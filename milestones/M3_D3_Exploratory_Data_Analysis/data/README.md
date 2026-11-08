# M3 / D3 — EDA Data Package
### Exact input and analysis ownership

**Status:** Done with reproducibility caveat  
**Target:** EBITDA Margin only  
**Coverage:** 38 quarterly observations, 2017–2026 Q2

## 1. Canonical input

[EDA_ANALYSIS_EBITDA_ONLY_38Q.csv](EDA_ANALYSIS_EBITDA_ONLY_38Q.csv)

Eight fields: Year; Calendar Quarter; EBITDA Margin; quarterly USD/INR mean; quarterly CPI mean; quarterly WPI mean; daily oil-benchmark quarterly mean; monthly oil-benchmark quarterly mean.

Net Income is not included as an EDA outcome. The panel does not contain passenger load factor, passenger yield, capacity, fuel consumption or route mix.

## 2. Notebook using this data

[Executed D3 EDA notebook](../02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)

The notebook has 34 cells, 14 executed code cells and 43 saved output records. See the M3 control and evidence README for the clean-rerun caveat. Preserved outputs should not be described as newly regenerated after a data-path change.

## 3. Source lineage

M2 owns raw statement and market workbooks, definitions and audit records: [M2 data package](../../M2_D2_Data_Audit/data/README.md). This CSV is a derived EDA input. It does not replace M2 sources or the active M4 model-ready dataset.

## 4. Use in EDA

The panel supports data quality checks, descriptive statistics, time trends, indicator relationships, exploratory hypothesis tests and calendar-quarter comparisons. These analyses are descriptive/exploratory; correlation does not establish causation or future forecast lift.

## 5. Limitations and interpretation

Only 38 observations are available. Time dependence, omitted operating drivers and unspecified oil-proxy units limit interpretation. Dated Brent is not aviation turbine fuel. Confirm the target denominator, fiscal-quarter conversion and point-in-time feature availability in M4.

## 6. Handoff

M4 must verify EBITDA and Revenue from Operations against the audited financial lines, establish one chronological quarter key, align the feature series, confirm publication/availability cutoffs and use time-ordered validation.