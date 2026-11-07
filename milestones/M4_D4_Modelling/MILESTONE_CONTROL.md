# M4 / D4 — Modelling: Milestone Control

**Status:** D4-v1 executed and documented.

## Purpose
Compare a simple persistence baseline with candidate regression models for next-quarter PAT Margin using a fixed chronological train/validation/test design.

## Inputs
Final_Quarterly_Data(1).xlsx; worksheet Final_Quarterly_Data. SHA-256: 85bf9e7ee51860fa38892ba3cb3e24b74887645bb2570c096f6183e59a97670c. Do not replace this source in the D4-v1 record.

## Working record
src/d4_train.py, notebooks/D4_modeling_experiment.ipynb, tests/test_d4_train.py, requirements-d4.txt.

## Deliverable
reports/ANCP_T##_D4_v1.pdf.

## Evidence
The experiments folder contains 12 runs, candidate validation results, full metrics, eight locked-test predictions, data manifest and runtime environment.

## Result and exit gate
Persistence was selected because Ridge and Random Forest did not outperform it on validation. Locked-test MAE was 11.53 percentage points and RMSE 14.20 percentage points on eight quarters. D4-v1 is a completed benchmark checkpoint; D5 must add point-in-time controls, rolling-origin evaluation and uncertainty analysis before model selection for deployment.
