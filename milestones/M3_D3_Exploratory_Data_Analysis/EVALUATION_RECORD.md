# M3 / D3 — EDA Evaluation Record

**Status:** Executed notebook uploaded; independent rerun and scope review pending.  
**Notebook:** 02_WORKING/ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb  
**Dataset referenced:** EDA ANALYSIS(5).xlsx, Sheet1 (not included in this repository).

## Scope
38 quarterly observations from 31-Mar-2017 to 30-Jun-2026. The profitability outcome is EBITDA Margin. Candidate indicators are quarterly-mean USD/INR, CPI, WPI, daily oil-benchmark mean and monthly oil-benchmark mean. Calendar-quarter categories are used.

## Values shown in the executed notebook
- Mean EBITDA Margin: 12.306%.
- Median EBITDA Margin: 15.000%.
- Standard deviation: 14.255 percentage points.
- H1 USD/INR: Spearman rho 0.554, p < 0.001, n = 38.
- H2 monthly oil proxy: rho 0.264, p = 0.109, n = 38.
- H3 CPI: rho -0.087, p = 0.605, n = 38.
- H4 WPI: rho -0.450, p = 0.005, n = 38.
- H5 calendar-quarter difference: Kruskal–Wallis p = 0.125, n = 38.

H1 and H4 show statistically significant exploratory rank associations in this sample; H2 and H3 do not; H5 shows no statistically significant quarter-group difference. The notebook warns that p-values are exploratory and the sample is small and time-dependent. These results do not establish causation or out-of-sample predictive value.

## Quality and limitations
The executed notebook reports 38 rows, no duplicate year-quarter combinations and no missing values across its transformed panel. It states that the workbook is already quarterly aggregated, so the raw daily/monthly records are not available in that workbook for independent aggregation checks. Passenger load factor, passenger yield, capacity, revenue, fuel consumption and explicit source metadata are absent. The exact oil benchmark identity and units are not verified.

## Target alignment
D1 and D4 define PAT Margin as the primary project target. This D3 notebook analyses EBITDA Margin. Do not represent these findings as validation of the PAT-margin forecast until the team approves the scope.

## Reproducibility
The notebook and 43 saved outputs are retained. The expected EDA ANALYSIS(5).xlsx input has not been uploaded, so a clean rerun cannot be verified. No separate D3 summary PDF/report was supplied.
