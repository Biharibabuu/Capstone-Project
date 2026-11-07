# M3 / D3 — Review Notes and M4 Handoff

**Canonical input:** [EDA ANALYSIS(4).xlsx](01_INPUTS/EDA%20ANALYSIS%284%29.xlsx)  
**Canonical notebook:** [Executed D3 EDA](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)

## Dataset fields
The workbook contains 38 quarterly observations with Year, Quarter (Calendar), PAT Margin, EBITDA Margin, quarterly mean USD/INR, CPI, WPI, daily oil-benchmark and monthly oil-benchmark values. The SHA-256 is `0c2a79065faaee48cec6393f79ff330a98a9eb20c1add3e87e8a45dd7e1c0f46`.

The notebook selects EBITDA Margin as the only profitability outcome and excludes PAT Margin from its analytical frame. Its saved summary statistics for EBITDA Margin match the workbook.

## Hypothesis framework
- H1: USD/INR and EBITDA Margin association.
- H2: monthly oil-benchmark proxy and EBITDA Margin association.
- H3: CPI and EBITDA Margin association.
- H4: WPI and EBITDA Margin association.
- H5: EBITDA Margin differences across calendar-quarter groups.

The executed notebook reports five tests. Significant same-period Spearman associations appear for USD/INR (rho 0.554, p < 0.001) and WPI (rho -0.450, p = 0.005); the monthly oil proxy (p = 0.109), CPI (p = 0.605) and calendar-quarter group test (p = 0.125) are not statistically significant in this sample. Treat these as exploratory, not causal or predictive conclusions.

## Controls and limitations
1. Confirm EBITDA and Revenue line-item definitions and denominator against underlying company statements.
2. Exclude estimates/unavailable financial rows from realised outcomes where applicable.
3. Preserve chronological quarter ordering; use fiscal-quarter keys for modelling if required by the D1 design.
4. Separate observation dates from actual publication/availability dates.
5. Dated Brent is a crude benchmark proxy, not Indian ATF or IndiGo's realised fuel price.
6. No passenger count, load factor, yield, RPK/ASK, capacity or route-mix variables are present in this workbook.
7. D3 is EBITDA-focused whereas the overall capstone's D1/D4 target remains PAT Margin; obtain explicit scope approval.

## Handoff to M4
Use the exact input workbook version and its SHA-256 in any downstream experiment manifest. Do not silently substitute a refreshed quarterly dataset. Carry forward the small-sample, feature-availability and target-alignment limitations.
