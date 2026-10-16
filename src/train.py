"""Training workflow placeholder for D4.

The feature list, target alignment and validation windows must be approved after D2
data audit and D3 EDA before model training is implemented. Candidate models include
a simple historical baseline, Ridge/Elastic Net and a nonlinear model if justified.
"""
from __future__ import annotations


def main() -> None:
    raise NotImplementedError(
        "Complete the D2 data audit and D3 EDA, then implement a time-ordered baseline "
        "and candidate-model comparison with MAE/RMSE and leakage checks."
    )


if __name__ == "__main__":
    main()
