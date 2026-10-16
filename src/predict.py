"""Prediction workflow placeholder.

Inference must use the exact preprocessing and validated features from training.
The API remains disabled until a reproducible model artifact and metadata are registered.
"""
from __future__ import annotations


def predict_next_quarter(*args, **kwargs):
    raise NotImplementedError(
        "Prediction is not available until D4/D5 select and validate a model, "
        "and the training-compatible preprocessing pipeline is packaged."
    )
