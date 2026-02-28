#!/bin/bash
# ============================================================
# Run all experiments for paper reproduction
# Usage: bash scripts/run_all.sh
# ============================================================

set -e

echo "============================================"
echo "Clinical Agenda Setting - Paper Reproduction"
echo "============================================"

# Check API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "ERROR: OPENAI_API_KEY not set"
    echo "Run: export OPENAI_API_KEY='sk-your-key'"
    exit 1
fi

# Generate sample data (skip if data already exists)
if [ ! -f "data/processed/case_01.json" ]; then
    echo ""
    echo "[Step 0] Generating sample data..."
    python scripts/generate_sample_data.py
fi

# Experiment 1: Baseline (Table 1)
echo ""
echo "[Step 1] Running Baseline experiment (Table 1)..."
python src/experiments/baseline.py \
    --transcript-dir data/processed \
    --annotation-dir data/annotations \
    --model gpt-3.5-turbo \
    --output results/baseline_results.json

# Experiment 2: Input Lines (Table 2)
echo ""
echo "[Step 2] Running Input Lines experiment (Table 2)..."
python src/experiments/input_lines.py \
    --transcript-dir data/processed \
    --annotation-dir data/annotations \
    --chunk-sizes 2 5 10 20 \
    --model gpt-3.5-turbo \
    --output results/input_lines_results.json

# Experiment 3: Real-time Simulation (Table 3)
echo ""
echo "[Step 3] Running Real-time Simulation (Table 3)..."
python src/experiments/realtime_sim.py \
    --transcript-dir data/processed \
    --annotation-dir data/annotations \
    --context-sizes 0 1 20 50 100 max \
    --model gpt-3.5-turbo \
    --output results/realtime_sim_results.json

# Experiment 4: Context Aggregation (Table 4)
echo ""
echo "[Step 4] Running Context Aggregation (Table 4)..."
python src/experiments/context_agg.py \
    --transcript-dir data/processed \
    --annotation-dir data/annotations \
    --model gpt-3.5-turbo \
    --output results/context_agg_results.json

echo ""
echo "============================================"
echo "All experiments complete!"
echo "Results saved in results/ directory"
echo "============================================"
