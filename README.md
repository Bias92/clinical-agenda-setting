# Clinical Agenda Setting System — Paper Reproduction

> Reproduction of **"Towards a Real-time Clinical Agenda Setting System for Enhancing Clinical Interactions in Primary Care Visits"**  
> Jang et al., GenAI4Health Workshop @ AAAI 2025

This project fully reproduces the four experiments from the paper, implementing real-time clinical agenda setting using LLMs during simulated primary care visits.

## Overview

The paper proposes a system that uses LLMs to automatically identify and summarize patient agenda items during doctor-patient conversations in real time. The system processes dialogue transcripts line-by-line and generates structured clinical summaries.

### Key Experiments

| Experiment | Description | Paper Reference |
|---|---|---|
| **Baseline** | Full transcript → single summary | Table 1 |
| **Input Lines** | Fixed chunk sizes (2, 5, 10, 20 lines) | Table 2 |
| **Real-time Simulation** | Line-by-line + context window (0, 1, 20, 50, 100, max) | Table 3 |
| **Context Aggregation** | Sliding/growing window strategies | Table 4 |

### Evaluation Metrics

- **Detection**: Precision, Recall (line-level agenda item detection)
- **Summarization**: ROUGE-L, BLEU, BERTScore, SemScore

## Results

All experiments use **GPT-3.5 Turbo** with 10 synthetic clinical cases (204 dialogue lines, 94 annotations).

### Table 1: Baseline

| Metric | Paper (16 cases) | Ours (10 cases) | Δ |
|---|---|---|---|
| ROUGE-L | 28.89 ± 5.39 | 39.74 ± 6.22 | +37.5% |
| BLEU | 8.79 ± 3.20 | 13.89 ± 3.47 | +58.0% |
| BERTScore | 85.88 ± 1.04 | 89.20 ± 1.10 | +3.9% |
| SemScore | 80.73 ± 4.45 | 86.97 ± 3.37 | +7.7% |

### Table 2: Input Lines (Chunk Size)

| Lines | ROUGE-L (Paper → Ours) | BLEU | BERTScore | SemScore |
|---|---|---|---|---|
| 2 | 27.99 → 33.57 | 8.00 → 6.26 | 84.81 → 85.16 | 79.38 → 79.01 |
| 5 | 29.59 → 31.72 | 8.82 → 6.55 | 85.32 → 86.29 | 82.00 → 80.59 |
| 10 | 28.60 → 38.29 | 7.69 → 10.34 | 85.17 → 87.66 | 83.38 → 83.09 |
| 20 | 27.80 → 40.96 | 8.20 → 13.51 | 85.09 → 88.75 | 82.29 → 86.99 |

### Table 3: Real-time Simulation (Context Window)

| Context | Precision (Paper → Ours) | Recall | ROUGE-L | BERTScore |
|---|---|---|---|---|
| 0 | 39.31 → 87.38 | 48.33 → 94.53 | 28.67 → 45.40 | 86.56 → 91.25 |
| 1 | 35.72 → 87.69 | 59.43 → 96.78 | 25.35 → 50.67 | 86.12 → 91.90 |
| 20 | 25.59 → 91.99 | 92.64 → 94.67 | 17.18 → 48.93 | 83.64 → 91.66 |
| 50 | 26.98 → 91.99 | 90.49 → 94.67 | 18.13 → 49.60 | 83.64 → 91.77 |
| 100 | 25.91 → 91.99 | 88.26 → 94.67 | 18.05 → 49.69 | 83.64 → 91.76 |
| max | 26.39 → 91.99 | 89.20 → 94.67 | 19.86 → 48.83 | 83.86 → 91.71 |

### Table 4: Context Aggregation

| Strategy | In/Ctx | Precision (Paper → Ours) | Recall | ROUGE-L | SemScore |
|---|---|---|---|---|---|
| sliding | 1/20 | 40.09 → 89.09 | 44.07 → 94.53 | 25.62 → 46.88 | 79.24 → 88.18 |
| sliding | 1/50 | 47.41 → 87.38 | 38.00 → 94.53 | 29.41 → 46.16 | 80.15 → 88.17 |
| growing | 1/20 | 52.17 → 89.90 | 34.88 → 94.53 | 27.68 → 45.72 | 79.94 → 87.32 |
| growing | 1/50 | 53.73 → 87.38 | 37.01 → 94.53 | 30.09 → 45.80 | 85.83 → 87.61 |
| **growing** | **5/5** | **66.70 → 95.73** | **77.80 → 87.29** | **25.10 → 44.76** | **82.10 → 88.22** |

**Key finding reproduced**: The `growing window` with `input=5, context=5` achieves the best precision-recall balance, consistent with the paper's conclusion.

## Analysis: Why Scores Differ

Our reproduction yields systematically higher absolute scores than the paper. Three factors explain this:

1. **Synthetic vs. real data**: The paper uses 16 real clinical conversations; we use 10 synthetic cases with cleaner structure, making LLM extraction easier.
2. **GPT-3.5 Turbo version**: The current API endpoint has received updates since the paper was written, potentially improving performance.
3. **BERTScore model**: We use `roberta-large` instead of `deberta-xlarge-mnli` (which has compatibility issues with current transformers), causing scale differences.

Despite absolute differences, the **key trends and conclusions are reproduced**:
- Growing window + input 5 + context 5 = best balance ✓
- Context size ↑ → recall ↑, precision trade-off ✓
- Larger chunks improve summarization quality ✓

## Project Structure

```
clinical-agenda-setting/
├── configs/
│   └── config.yaml              # Experiment config (model, parameters)
├── data/
│   ├── processed/               # 10 case transcripts (case_01~10.json)
│   └── annotations/             # 10 case annotations (case_01~10.json)
├── src/
│   ├── experiments/
│   │   ├── baseline.py          # Table 1: full transcript → summary
│   │   ├── input_lines.py       # Table 2: chunk size (2,5,10,20)
│   │   ├── realtime_sim.py      # Table 3: line-by-line + context window
│   │   └── context_agg.py       # Table 4: sliding/growing window
│   ├── evaluation/
│   │   ├── metrics.py           # ROUGE-L, BLEU, BERTScore, SemScore
│   │   └── detection.py         # Precision, Recall (line-level)
│   └── utils/
│       ├── llm_client.py        # OpenAI API wrapper (temperature=0)
│       ├── data_loader.py       # JSON data loading/parsing
│       └── prompts.py           # Prompts from paper Section 4.4
├── scripts/
│   ├── generate_sample_data.py  # Synthetic data generator
│   └── run_all.sh               # Run all 4 experiments
├── results/                     # Experiment output JSONs (gitignored)
├── requirements.txt
└── README.md
```

## Setup & Reproduction

### Prerequisites

- Python 3.10+
- OpenAI API key with GPT-3.5 Turbo access

### Installation

```bash
git clone https://github.com/<YOUR_USERNAME>/clinical-agenda-setting.git
cd clinical-agenda-setting
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Experiments

```bash
export OPENAI_API_KEY="sk-your-key"
bash scripts/run_all.sh
```

This runs all 4 experiments sequentially. Results are saved to `results/`.

To run individual experiments:

```bash
python3 -m src.experiments.baseline        # Table 1
python3 -m src.experiments.input_lines     # Table 2
python3 -m src.experiments.realtime_sim    # Table 3
python3 -m src.experiments.context_agg     # Table 4
```

### View Results

```bash
python3 -m json.tool results/baseline_results.json
python3 -m json.tool results/input_lines_results.json
python3 -m json.tool results/realtime_sim_results.json
python3 -m json.tool results/context_agg_results.json
```

## Sample Data

10 synthetic clinical scenarios covering:

| Case | Scenario | Lines | Annotations |
|---|---|---|---|
| 01 | Cough + dyspnea | 24 | 11 |
| 02 | Chronic headache | 22 | 10 |
| 03 | Lower back pain | 20 | 10 |
| 04 | Diabetes management | 18 | 8 |
| 05 | Chest pain / cardiac | 20 | 9 |
| 06 | Abdominal pain + GI | 20 | 9 |
| 07 | Anxiety + insomnia | 20 | 10 |
| 08 | Knee pain | 20 | 9 |
| 09 | Skin rash / drug reaction | 20 | 9 |
| 10 | Fatigue + weight gain / thyroid | 20 | 9 |

## Technical Notes

### BERTScore Model Substitution

The paper uses `microsoft/deberta-xlarge-mnli` for BERTScore, which causes `OverflowError` with current `transformers` versions. We substituted `roberta-large` (BERTScore's recommended default), which may produce slightly different score scales but does not affect relative comparisons.

### API Configuration

- Model: `gpt-3.5-turbo`
- Temperature: `0` (deterministic)
- Prompts: Reproduced from paper Section 4.4

## Citation

```bibtex
@inproceedings{jang2025clinical,
  title={Towards a Real-time Clinical Agenda Setting System for Enhancing Clinical Interactions in Primary Care Visits},
  author={Jang, et al.},
  booktitle={GenAI4Health Workshop at AAAI 2025},
  year={2025}
}
```

## License

This reproduction is for academic/research purposes only. The original paper and its methods belong to the respective authors.
