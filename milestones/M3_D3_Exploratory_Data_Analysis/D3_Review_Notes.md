# D3 — Review Notes for the New Executed EDA Notebook

**Review date:** 7 November 2026  
**Canonical artifact:** [Executed notebook](02_WORKING/ANCP_T%23%23_D3_EDA_New_Dataset_EXECUTED.ipynb)

## Source and run record
The uploaded notebook is Jupyter Notebook v4.5. It contains 34 cells (20 markdown, 14 code), 43 saved outputs and 14 execution counts. The notebook reports that it was run against EDA ANALYSIS(5).xlsx, worksheet Sheet1.

## Dataset schema and coverage stated in notebook
38 quarterly observations from 31 March 2017 to 30 June 2026. The notebook requires Year, Quarter (Calendar), EBITDA Margin, USD INR (Quarterly Mean), CPI inflation (Quarterly Mean), WPI inflation (Quarterly Mean), Oil benchmark(DAILY) (Quarterly Mean), and Oil benchmark(MONTHLY) (Quarterly Mean).

## Hypothesis results
| ID | Relationship | n | Statistic | p-value |
|---|---|---:|---:|---:|
| H1 | EBITDA Margin and USD/INR | 38 | Spearman rho 0.554 | <0.001 |
| H2 | EBITDA Margin and monthly oil proxy | 38 | Spearman rho 0.264 | 0.109 |
| H3 | EBITDA Margin and CPI | 38 | Spearman rho -0.087 | 0.605 |
| H4 | EBITDA Margin and WPI | 38 | Spearman rho -0.450 | 0.005 |
| H5 | EBITDA Margin across calendar quarters | 38 | Kruskal–Wallis | 0.125 |

## Interpretation controls
- Results are exploratory; the notebook warns about small sample size and time dependence.
- Do not interpret an observed correlation as causal.
- Same-quarter association is not a one-quarter-ahead forecasting test.
- The oil benchmark is a proxy; exact instrument and units are not verified by this workbook.
- The D3 outcome is EBITDA Margin, while the D1/D4 capstone target is PAT Margin.

## Outstanding actions
1. Supply EDA ANALYSIS(5).xlsx to 01_INPUTS and record its SHA-256.
2. Confirm data-use rights for the workbook and saved notebook outputs.
3. Re-run from a clean environment with the exact input.
4. Decide whether this is supplementary EBITDA analysis or whether PAT-margin EDA is also needed.
5. Review the D3 summary and modelling handoff before closure.
