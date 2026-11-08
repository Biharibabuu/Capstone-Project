# M3 / D3 — EDA Evaluation Record

**Status:** Latest executed notebook uploaded; previous EDA workbook removed; clean rerun pending exact source input.  
**Notebook:** [ANCP_T##_D3_EDA_New_Dataset_EXECUTED.ipynb](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb).

## Notebook integrity
The latest notebook contains 34 cells (20 markdown and 14 code), 43 saved outputs and 14 execution counts. The executed outputs remain intact.

## Analysis dataset represented in the executed results
- 38 quarterly observations, 2017-03-31 through 2026-06-30.
- Eight selected analysis fields: Year, Quarter (Calendar), EBITDA Margin, USD/INR quarterly mean, CPI quarterly mean, WPI quarterly mean, daily oil-benchmark quarterly mean and monthly oil-benchmark quarterly mean.
- The notebook reports no missing values in its transformed 10-column analysis panel and zero duplicate Year–Quarter combinations.
- Descriptive EBITDA Margin statistics: mean 12.306%, median 15.000%, standard deviation 14.255 percentage points, min -36.667%, max 29.933%.

## Exploratory hypothesis results
| ID | Relationship / test | n | Statistic | p-value |
|---|---|---:|---:|---:|
| H1 | EBITDA Margin vs USD/INR (Spearman) | 38 | rho 0.554 | <0.001 |
| H2 | EBITDA Margin vs monthly oil proxy (Spearman) | 38 | rho 0.264 | 0.109 |
| H3 | EBITDA Margin vs CPI (Spearman) | 38 | rho -0.087 | 0.605 |
| H4 | EBITDA Margin vs WPI (Spearman) | 38 | rho -0.450 | 0.005 |
| H5 | EBITDA Margin across calendar quarters (Kruskal–Wallis) | 38 | — | 0.125 |

H1 and H4 show statistically significant same-period rank associations in this sample. H2 and H3 do not show statistically significant associations, and H5 does not show statistically significant quarter-group differences. These findings are exploratory, not causal, and do not establish next-quarter forecasting performance.

## Input-file status and source discrepancy
The previous standalone `EDA ANALYSIS(4).xlsx` has been removed from the M3 folder as requested. The current notebook references `EDA ANALYSIS(5).xlsx` / `Sheet1`; that exact workbook is not included in GitHub, so clean execution cannot yet be reproduced.

The available candidate `Final_Quarterly_Data(4).xlsx` was not substituted. In its `Final_Quarterly_Data` sheet, 2020 Q4 EBITDA Margin is -201.391218%, whereas the previous EDA panel reports -20.391218%. This 181 percentage-point discrepancy is material and needs source reconciliation before regenerating results. No value has been silently changed.

## Limitations
- 38 quarterly observations provide limited statistical power.
- Quarterly observations may be serially dependent.
- The oil benchmark identity and units are not fully established.
- Passenger demand, load factor, yield, passenger count, capacity, fuel consumption and route mix are absent.
- Same-quarter association is not a one-quarter-ahead forecast test.

## Handoff to M4
Use EBITDA Margin as the adopted project target. Before modelling, reconcile the 2020 Q4 value, confirm source definitions and publication timing, and build a chronological target-quarter dataset without leakage. Compare candidates to simple historical/seasonal baselines.
