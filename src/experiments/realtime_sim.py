"""
Experiment 4.4: Real-time Simulation (Table 3)
LLM processes transcript line-by-line, maintaining a context window
of previous lines + summaries.

Paper results (GPT 3.5 Turbo):
    Context=0:  Precision=39.31, Recall=48.33, Rouge-L=28.67
    Context=1:  Precision=35.72, Recall=59.43
    Context=20: Precision=25.59, Recall=92.64
    → Trade-off: larger context → higher recall, lower precision
"""

import json
import argparse
from pathlib import Path
from tqdm import tqdm

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.utils.llm_client import LLMClient
from src.utils.data_loader import load_all_cases
from src.utils.prompts import REALTIME_SYSTEM_PROMPT, REALTIME_USER_PROMPT
from src.evaluation.metrics import SummarizationMetrics
from src.evaluation.detection import compute_detection_metrics
import numpy as np


def run_realtime_simulation(
    transcript_dir: str,
    annotation_dir: str,
    context_sizes: list = [0, 1, 20, 50, 100, "max"],
    model_name: str = "gpt-3.5-turbo",
    output_path: str = "results/realtime_sim_results.json",
):
    """Run real-time simulation with varying context window sizes."""

    cases = load_all_cases(transcript_dir, annotation_dir)
    if not cases:
        print("ERROR: No cases found.")
        return

    llm = LLMClient(model=model_name, temperature=0.0)
    all_results = {}

    for ctx_size in context_sizes:
        print(f"\n{'='*60}")
        print(f"Context size: {ctx_size}")
        print(f"{'='*60}")

        case_precisions = []
        case_recalls = []
        all_predictions = []
        all_references = []

        for case in tqdm(cases, desc=f"Context={ctx_size}"):
            # Build annotated line indices set
            annotated_lines = {a.line_idx for a in case.annotations}

            # Process line-by-line
            context_history = []  # list of (line_text, summary) pairs
            llm_outputs = []

            for i, line in enumerate(case.lines):
                # Build messages
                messages = [{"role": "system", "content": REALTIME_SYSTEM_PROMPT}]

                # Add context (previous lines + summaries)
                if ctx_size == "max":
                    # Use all previous lines that fit
                    context_to_use = context_history
                elif ctx_size == 0:
                    context_to_use = []
                else:
                    context_to_use = context_history[-ctx_size:]

                for prev_line, prev_summary in context_to_use:
                    messages.append({"role": "user", "content": prev_line})
                    messages.append({"role": "assistant", "content": prev_summary})

                # Add current line
                current_line = REALTIME_USER_PROMPT.format(
                    speaker=line.speaker, text=line.text
                )
                messages.append({"role": "user", "content": current_line})

                # Get LLM response
                summary = llm.conversation_call(messages)
                llm_outputs.append(summary)

                # Add to context history
                context_history.append((current_line, summary))

            # Detection metrics (line-level)
            y_true = [1 if i in annotated_lines else 0 for i in range(len(case.lines))]
            y_pred = [
                0 if s.strip().lower() in ("none", "none.") else 1
                for s in llm_outputs
            ]
            det_metrics = compute_detection_metrics(y_true, y_pred)
            case_precisions.append(det_metrics["precision"])
            case_recalls.append(det_metrics["recall"])

            # Summarization: collect detected summaries vs reference
            detected_summaries = [
                s for s in llm_outputs if s.strip().lower() not in ("none", "none.")
            ]
            prediction = " ".join(detected_summaries) if detected_summaries else "None"
            reference = " ".join(a.summary for a in case.annotations)
            all_predictions.append(prediction)
            all_references.append(reference)

        # Compute summarization metrics
        metrics = SummarizationMetrics()
        sum_results = metrics.compute_all(all_predictions, all_references)

        # Aggregate detection metrics
        precision_arr = np.array(case_precisions)
        recall_arr = np.array(case_recalls)

        result = {
            "precision": {"mean": float(np.mean(precision_arr)), "std": float(np.std(precision_arr))},
            "recall": {"mean": float(np.mean(recall_arr)), "std": float(np.std(recall_arr))},
        }
        for name, data in sum_results.items():
            result[name] = {"mean": data["mean"], "std": data["std"]}

        # Print (Table 3 format)
        print(f"\nContext={ctx_size} results:")
        print(f"  Precision:  {result['precision']['mean']:.2f} ± {result['precision']['std']:.2f}")
        print(f"  Recall:     {result['recall']['mean']:.2f} ± {result['recall']['std']:.2f}")
        for name in ["Rouge-L", "BLEU", "BERTScore", "SemScore"]:
            print(f"  {name}: {result[name]['mean']:.2f} ± {result[name]['std']:.2f}")

        all_results[str(ctx_size)] = result

    # Save
    output = {
        "experiment": "realtime_simulation",
        "model": model_name,
        "results_by_context_size": all_results,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript-dir", default="data/processed")
    parser.add_argument("--annotation-dir", default="data/annotations")
    parser.add_argument("--context-sizes", nargs="+", default=[0, 1, 20, 50, 100, "max"])
    parser.add_argument("--model", default="gpt-3.5-turbo")
    parser.add_argument("--output", default="results/realtime_sim_results.json")
    args = parser.parse_args()

    # Parse context sizes (handle "max" string)
    ctx_sizes = []
    for s in args.context_sizes:
        ctx_sizes.append("max" if str(s) == "max" else int(s))

    run_realtime_simulation(
        args.transcript_dir, args.annotation_dir,
        ctx_sizes, args.model, args.output,
    )
