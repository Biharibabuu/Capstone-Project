# M3 / D3 — Review Notes and M4 Handoff

**Canonical artifact:** [Executed D3 EDA notebook](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb).  
**Standalone EDA Analysis workbook:** removed from the milestone.

## Dataset represented by the notebook
The notebook reports 38 quarterly observations from 2017-03-31 to 2026-06-30. It selects EBITDA Margin as the only profitability outcome with USD/INR, CPI, WPI, daily oil-benchmark and monthly oil-benchmark quarterly means as candidate indicators.

## Principal results
- Mean EBITDA Margin 12.306%; median 15.000%; standard deviation 14.255 percentage points.
- H1 USD/INR: Spearman rho 0.554, p < 0.001.
- H2 monthly oil proxy: rho 0.264, p = 0.109.
- H3 CPI: rho -0.087, p = 0.605.
- H4 WPI: rho -0.450, p = 0.005.
- H5 calendar-quarter Kruskal–Wallis p = 0.125.

The observed significant USD/INR and WPI relationships are same-period rank associations. They are not causal conclusions and do not establish next-quarter predictive value.

## Reproducibility and data governance
The user requested removal of the separate EDA Analysis Excel workbook. The notebook is stored with its saved outputs, but its input code expects `EDA ANALYSIS(5).xlsx`, worksheet `Sheet1`; that exact input is not committed. A clean rerun therefore remains pending.

Do not substitute `Final_Quarterly_Data(4).xlsx` without reconciling its 2020 Q4 EBITDA Margin of -201.391218% against the prior EDA panel's -20.391218%. This discrepancy is material; it must be checked against raw quarterly financial source values and the approved EBITDA definition.

## M4 modelling controls
1. Preserve fiscal/quarter chronology and do not bridge missing quarters.
2. Use only predictors observable by the forecast cut-off.
3. Keep target-quarter EBITDA and revenue as label inputs, not predictors.
4. Compare persistence/seasonal-naive baselines with parsimonious challengers using chronological evaluation.
5. Record the exact approved input version, source hash and transformation lineage.
