"""
Experiment 4.5: Real-time Simulation with Context Aggregation (Table 4)
Two aggregation strategies:
  1. Sliding window: context = concatenation of last K summaries (disjoint)
  2. Growing window: context = append last K summaries to existing context

Paper best result:
    Growing window, input=5, context=5: Precision=66.7, Recall=77.8
"""

import json
import argparse
from pathlib import Path
from tqdm import tqdm

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.utils.llm_client import LLMClient
from src.utils.data_loader import load_all_cases
from src.utils.prompts import (
    REALTIME_SYSTEM_PROMPT,
    REALTIME_USER_PROMPT,
    CONTEXT_AGG_CONTEXT_PREFIX,
)
from src.evaluation.metrics import SummarizationMetrics
from src.evaluation.detection import compute_detection_metrics
import numpy as np


def run_context_aggregation(
    transcript_dir: str,
    annotation_dir: str,
    configs: list[dict] = None,
    model_name: str = "gpt-3.5-turbo",
    output_path: str = "results/context_agg_results.json",
):
    """Run context aggregation experiments."""

    if configs is None:
        # Default configs from Table 4
        configs = [
            {"aggregation": "sliding_window", "input_size": 1, "context_size": 20},
            {"aggregation": "sliding_window", "input_size": 1, "context_size": 50},
            {"aggregation": "growing_window", "input_size": 1, "context_size": 20},
            {"aggregation": "growing_window", "input_size": 1, "context_size": 50},
            {"aggregation": "growing_window", "input_size": 5, "context_size": 5},
        ]

    cases = load_all_cases(transcript_dir, annotation_dir)
    if not cases:
        print("ERROR: No cases found.")
        return

    llm = LLMClient(model=model_name, temperature=0.0)
    all_results = []

    for cfg in configs:
        agg = cfg["aggregation"]
        input_size = cfg["input_size"]
        ctx_size = cfg["context_size"]

        print(f"\n{'='*60}")
        print(f"Aggregation={agg}, Input={input_size}, Context={ctx_size}")
        print(f"{'='*60}")

        case_precisions = []
        case_recalls = []
        all_predictions = []
        all_references = []

        for case in tqdm(cases, desc=f"{agg} in={input_size} ctx={ctx_size}"):
            annotated_lines = {a.line_idx for a in case.annotations}
            llm_outputs = []
            context_summary = ""  # aggregated context summary
            recent_summaries = []  # buffer of recent K summaries
            lines_since_update = 0

            for i, line in enumerate(case.lines):
                # Build user message (potentially multiple lines for input_size > 1)
                # For simplicity with input_size=1, process one line at a time
                current_line = REALTIME_USER_PROMPT.format(
                    speaker=line.speaker, text=line.text
                )

                # Build prompt with context
                if context_summary:
                    user_content = CONTEXT_AGG_CONTEXT_PREFIX.format(
                        context_summary=context_summary
                    ) + "\n" + current_line
                else:
                    user_content = current_line

                messages = [
                    {"role": "system", "content": REALTIME_SYSTEM_PROMPT},
                    {"role": "user", "content": user_content},
                ]

                summary = llm.conversation_call(messages)
                llm_outputs.append(summary)

                # Track summaries for aggregation
                if summary.strip().lower() not in ("none", "none."):
                    recent_summaries.append(summary)

                lines_since_update += 1

                # Update context every K lines
                if lines_since_update >= ctx_size and recent_summaries:
                    new_chunk = " ".join(recent_summaries[-ctx_size:])

                    if agg == "sliding_window":
                        context_summary = new_chunk
                    elif agg == "growing_window":
                        context_summary = (
                            (context_summary + " " + new_chunk).strip()
                            if context_summary
                            else new_chunk
                        )

                    recent_summaries = []
                    lines_since_update = 0

            # Detection metrics
            y_true = [1 if i in annotated_lines else 0 for i in range(len(case.lines))]
            y_pred = [
                0 if s.strip().lower() in ("none", "none.") else 1
                for s in llm_outputs
            ]
            det = compute_detection_metrics(y_true, y_pred)
            case_precisions.append(det["precision"])
            case_recalls.append(det["recall"])

            # Summarization
            detected = [s for s in llm_outputs if s.strip().lower() not in ("none", "none.")]
            all_predictions.append(" ".join(detected) if detected else "None")
            all_references.append(" ".join(a.summary for a in case.annotations))

        # Compute metrics
        metrics = SummarizationMetrics()
        sum_results = metrics.compute_all(all_predictions, all_references)

        precision_arr = np.array(case_precisions)
        recall_arr = np.array(case_recalls)

        result = {
            "config": cfg,
            "precision": {"mean": float(np.mean(precision_arr)), "std": float(np.std(precision_arr))},
            "recall": {"mean": float(np.mean(recall_arr)), "std": float(np.std(recall_arr))},
        }
        for name, data in sum_results.items():
            result[name] = {"mean": data["mean"], "std": data["std"]}

        print(f"\nResults:")
        print(f"  Precision:  {result['precision']['mean']:.2f} ± {result['precision']['std']:.2f}")
        print(f"  Recall:     {result['recall']['mean']:.2f} ± {result['recall']['std']:.2f}")
        for name in ["Rouge-L", "BLEU", "BERTScore", "SemScore"]:
            print(f"  {name}: {result[name]['mean']:.2f} ± {result[name]['std']:.2f}")

        all_results.append(result)

    # Save
    output = {
        "experiment": "context_aggregation",
        "model": model_name,
        "results": all_results,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript-dir", default="data/processed")
    parser.add_argument("--annotation-dir", default="data/annotations")
    parser.add_argument("--model", default="gpt-3.5-turbo")
    parser.add_argument("--output", default="results/context_agg_results.json")
    args = parser.parse_args()

    run_context_aggregation(
        args.transcript_dir, args.annotation_dir,
        model_name=args.model, output_path=args.output,
    )
