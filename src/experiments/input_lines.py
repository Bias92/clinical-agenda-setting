"""
Experiment 4.3: Varying Number of Input Lines (Table 2)
GPT 3.5 Turbo processes fixed-size chunks of transcript lines.
Chunks + summaries are kept in context window.

Paper result (GPT 3.5 Turbo, 5 lines):
    Rouge-L: 29.59 ± 4.88 (best)
    BLEU:     8.82 ± 3.19 (best)
"""

import json
import argparse
from pathlib import Path
from tqdm import tqdm

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.utils.llm_client import LLMClient
from src.utils.data_loader import load_all_cases, chunk_lines, format_transcript
from src.utils.prompts import INPUT_LINES_SYSTEM_PROMPT, INPUT_LINES_USER_PROMPT
from src.evaluation.metrics import SummarizationMetrics


def run_input_lines(
    transcript_dir: str,
    annotation_dir: str,
    chunk_sizes: list[int] = [2, 5, 10, 20],
    model_name: str = "gpt-3.5-turbo",
    output_path: str = "results/input_lines_results.json",
):
    """Run input lines experiment with various chunk sizes."""

    cases = load_all_cases(transcript_dir, annotation_dir)
    if not cases:
        print("ERROR: No cases found.")
        return

    llm = LLMClient(model=model_name, temperature=0.0)
    all_results = {}

    for chunk_size in chunk_sizes:
        print(f"\n{'='*60}")
        print(f"Running with chunk_size={chunk_size}")
        print(f"{'='*60}")

        predictions = []
        references = []

        for case in tqdm(cases, desc=f"Chunk size {chunk_size}"):
            # Split into chunks
            chunks = chunk_lines(case.lines, chunk_size)
            case_summaries = []

            # Process each chunk — keep previous chunks + summaries in context
            messages = [{"role": "system", "content": INPUT_LINES_SYSTEM_PROMPT}]

            for chunk in chunks:
                chunk_text = "\n".join(f"[{l.speaker}] {l.text}" for l in chunk)
                user_msg = INPUT_LINES_USER_PROMPT.format(chunk=chunk_text)
                messages.append({"role": "user", "content": user_msg})

                summary = llm.conversation_call(messages)
                messages.append({"role": "assistant", "content": summary})

                if summary.strip().lower() not in ("none", "none."):
                    case_summaries.append(summary)

            # Combine all chunk summaries
            prediction = " ".join(case_summaries) if case_summaries else "None"
            predictions.append(prediction)

            ref_summary = " ".join(a.summary for a in case.annotations)
            references.append(ref_summary)

        # Evaluate
        metrics = SummarizationMetrics()
        results = metrics.compute_all(predictions, references)

        print(f"\nResults for chunk_size={chunk_size}:")
        for name, data in results.items():
            print(f"  {name}: {data['mean']:.2f} ± {data['std']:.2f}")

        all_results[str(chunk_size)] = {
            k: {"mean": v["mean"], "std": v["std"]} for k, v in results.items()
        }

    # Save
    output = {
        "experiment": "input_lines",
        "model": model_name,
        "results_by_chunk_size": all_results,
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nAll results saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript-dir", default="data/processed")
    parser.add_argument("--annotation-dir", default="data/annotations")
    parser.add_argument("--chunk-sizes", nargs="+", type=int, default=[2, 5, 10, 20])
    parser.add_argument("--model", default="gpt-3.5-turbo")
    parser.add_argument("--output", default="results/input_lines_results.json")
    args = parser.parse_args()

    run_input_lines(
        args.transcript_dir, args.annotation_dir,
        args.chunk_sizes, args.model, args.output,
    )
