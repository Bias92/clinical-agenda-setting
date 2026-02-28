"""
Detection metrics for agenda items and details.
Implements Precision and Recall from Section 4.1 (Equations 1 & 2).
"""

import numpy as np


def compute_detection_metrics(
    y_true: list[int], y_pred: list[int]
) -> dict[str, float]:
    """
    Compute precision and recall for agenda/detail detection.

    Args:
        y_true: Ground truth labels (1 = annotated, 0 = not)
        y_pred: System predictions (1 = detected, 0 = not)

    Returns:
        dict with precision, recall values

    Paper equations (Section 4.1):
        Precision = Σ 1(ŷ_i=1 and y_i=1) / Σ 1(ŷ_i=1)
        Recall    = Σ 1(ŷ_i=1 and y_i=1) / Σ 1(y_i=1)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    true_positives = np.sum((y_pred == 1) & (y_true == 1))
    predicted_positives = np.sum(y_pred == 1)
    actual_positives = np.sum(y_true == 1)

    precision = true_positives / predicted_positives if predicted_positives > 0 else 0.0
    recall = true_positives / actual_positives if actual_positives > 0 else 0.0

    return {
        "precision": float(precision) * 100,
        "recall": float(recall) * 100,
        "true_positives": int(true_positives),
        "predicted_positives": int(predicted_positives),
        "actual_positives": int(actual_positives),
    }


def line_level_detection(
    llm_outputs: list[str], annotations: list[dict], num_lines: int
) -> tuple[list[int], list[int]]:
    """
    Convert LLM outputs and annotations to line-level binary labels.

    Args:
        llm_outputs: LLM response for each line (or "None" if no detection)
        annotations: List of annotation dicts with 'line_idx' field
        num_lines: Total number of lines in the transcript

    Returns:
        (y_true, y_pred) binary label lists
    """
    annotated_lines = {a["line_idx"] for a in annotations}

    y_true = [1 if i in annotated_lines else 0 for i in range(num_lines)]
    y_pred = [
        0 if (out.strip().lower() == "none" or out.strip().lower() == "none.") else 1
        for out in llm_outputs
    ]

    return y_true, y_pred
