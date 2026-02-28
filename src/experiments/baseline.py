"""
Experiment 4.2: Baseline LLM Performance (Table 1)
Full clinical conversation → LLM → Summary of agenda items and details.

Paper result (GPT 3.5 Turbo):
    Rouge-L: 28.89 ± 5.39
    BLEU:     8.79 ± 3.20
    BERTScore: 85.88 ± 1.04
    SemScore:  80.73 ± 4.45
"""

import json
import argparse
from pathlib import Path
from tqdm import tqdm

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.utils.llm_client import LLMClient
from src.utils.data_loader import load_all_cases, format_transcript
from src.utils.prompts import BASELINE_SYSTEM_PROMPT, BASELINE_USER_PROMPT
from src.evaluation.metrics import SummarizationMetrics


def run_baseline(
    transcript_dir: str,
    annotation_dir: str,
    model_name: str = "gpt-3.5-turbo",
    output_path: str = "results/baseline_results.json",
):
    """Run baseline experiment: full transcript → LLM → summary."""

    # Load data
    cases = load_all_cases(transcript_dir, annotation_dir)
    if not cases:
        print("ERROR: No cases found. Please add data to data/processed/ and data/annotations/")
        return

    # Init LLM client
    llm = LLMClient(model=model_name, temperature=0.0)

    # Run experiment
    predictions = []
    references = []

    for case in tqdm(cases, desc="Baseline experiment"):
        # Format full transcript
        transcript_text = format_transcript(case.lines)

        # Get LLM summary
        user_prompt = BASELINE_USER_PROMPT.format(transcript=transcript_text)
        summary = llm.single_call(BASELINE_SYSTEM_PROMPT, user_prompt)
        predictions.append(summary)

        # Build reference summary from annotations
        ref_summary = " ".join(a.summary for a in case.annotations)
        references.append(ref_summary)

        print(f"\n[{case.id}] LLM Summary (first 200 chars): {summary[:200]}...")

    # Evaluate
    print("\nComputing evaluation metrics...")
    metrics = SummarizationMetrics()
    results = metrics.compute_all(predictions, references)

    # Print results (Table 1 format)
    print("\n" + "=" * 60)
    print("BASELINE RESULTS (Table 1 - GPT 3.5 Turbo)")
    print("=" * 60)
    for metric_name, metric_data in results.items():
        print(f"  {metric_name}: {metric_data['mean']:.2f} ± {metric_data['std']:.2f}")

    # Save results
    output = {
        "experiment": "baseline",
        "model": model_name,
        "num_cases": len(cases),
        "metrics": {k: {"mean": v["mean"], "std": v["std"]} for k, v in results.items()},
        "predictions": predictions,
        "references": references,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Baseline agenda-setting experiment")
    parser.add_argument("--transcript-dir", default="data/processed")
    parser.add_argument("--annotation-dir", default="data/annotations")
    parser.add_argument("--model", default="gpt-3.5-turbo")
    parser.add_argument("--output", default="results/baseline_results.json")
    args = parser.parse_args()

    run_baseline(args.transcript_dir, args.annotation_dir, args.model, args.output)
