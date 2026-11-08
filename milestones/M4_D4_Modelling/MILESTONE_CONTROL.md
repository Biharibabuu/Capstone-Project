# M4 / D4 — Modelling: Milestone Control

**Status:** IN PROGRESS — active modelling work targets EBITDA Margin.

## Purpose
Build and compare a simple persistence baseline and candidate regression models for next-quarter EBITDA Margin using a fixed chronological train/validation/test design.

## Adopted target
EBITDA Margin (%) = EBITDA / Revenue from Operations × 100. Use this target consistently in the active M4 experiment and all subsequent evaluation/application work.

## Inputs
The current EDA handoff is the 38-quarter EBITDA-focused panel in [M3](../M3_D3_Exploratory_Data_Analysis/01_INPUTS/EDA%20ANALYSIS%284%29.xlsx). Keep the exact input SHA-256 and version in each M4 experiment manifest. Do not silently substitute the newer, unapproved quarterly candidate workbook.

## Working record
src/d4_train.py, notebooks/D4_modeling_experiment.ipynb, tests/test_d4_train.py and requirements-d4.txt. The active experiment must be explicitly configured for EBITDA Margin.

## Legacy D4-v1 evidence
The existing D4-v1 report is a PAT-margin experiment. Its persistence/Ridge/Random Forest metrics and eight locked-test predictions are preserved as historical evidence only. They are not EBITDA-model results and must not be presented as performance on the adopted target.

## Current deliverable and exit gate
Produce a reproducible EBITDA-target modelling experiment with:
1. A pinned input dataset, hash and target-construction record.
2. A one-quarter-ahead supervised table without bridging missing quarters.
3. Persistence and seasonal-naive baselines.
4. Parsimonious candidate models with time-ordered validation.
5. Training-only preprocessing and forecast-date feature-availability controls.
6. Run configuration, metrics, predictions, residuals, tests, environment and report.

M4 is complete only after the EBITDA target, input hash, chronological splits, baseline comparison, candidate results, tests and reproducibility artifacts are documented. M5 then adds independent rolling-origin evaluation and uncertainty analysis.

## Target governance
The adopted project target is EBITDA Margin. The original D1 PDF's PAT-margin proposal has been superseded by the scope decision documented in [M1 Evaluation Record](../M1_D1_Project_Charter/EVALUATION_RECORD.md). EBITDA and EBITDAR are not interchangeable.
