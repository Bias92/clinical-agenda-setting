"""
Evaluation metrics for summarization quality.
Implements: ROUGE-L, BLEU, BERTScore, SemScore (Section 4.1)
"""

import numpy as np
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from bert_score import score as bert_score_fn
from sentence_transformers import SentenceTransformer, util


class SummarizationMetrics:
    """All summarization quality metrics from the paper."""

    def __init__(
        self,
        bertscore_model: str = "roberta-large",
        semscore_model: str = "all-MiniLM-L6-v2",
    ):
        self.rouge = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
        self.smooth = SmoothingFunction().method1
        self.semscore_model = SentenceTransformer(semscore_model)
        self._bertscore_model = bertscore_model

    def rouge_l(self, prediction: str, reference: str) -> float:
        """ROUGE-L: Longest common subsequence F-score."""
        scores = self.rouge.score(reference, prediction)
        return scores["rougeL"].fmeasure * 100  # 논문은 백분율 스케일

    def bleu(self, prediction: str, reference: str) -> float:
        """BLEU: Modified n-gram precision with brevity penalty."""
        ref_tokens = reference.lower().split()
        pred_tokens = prediction.lower().split()
        if len(pred_tokens) == 0:
            return 0.0
        score = sentence_bleu(
            [ref_tokens], pred_tokens, smoothing_function=self.smooth
        )
        return score * 100

    def bertscore(self, predictions: list[str], references: list[str]) -> list[float]:
        """BERTScore: Contextual embedding similarity (batch)."""
        P, R, F1 = bert_score_fn(
            predictions,
            references,
            model_type=self._bertscore_model,
            verbose=False,
        )
        return (F1.numpy() * 100).tolist()

    def semscore(self, prediction: str, reference: str) -> float:
        """SemScore: Sentence-level semantic similarity."""
        emb_pred = self.semscore_model.encode(prediction, convert_to_tensor=True)
        emb_ref = self.semscore_model.encode(reference, convert_to_tensor=True)
        similarity = util.cos_sim(emb_pred, emb_ref).item()
        return similarity * 100

    def compute_all(
        self, predictions: list[str], references: list[str]
    ) -> dict[str, dict[str, float]]:
        """Compute all metrics and return mean ± std (like paper tables)."""
        n = len(predictions)
        rouge_scores = [self.rouge_l(p, r) for p, r in zip(predictions, references)]
        bleu_scores = [self.bleu(p, r) for p, r in zip(predictions, references)]
        bert_scores = self.bertscore(predictions, references)
        sem_scores = [self.semscore(p, r) for p, r in zip(predictions, references)]

        results = {}
        for name, scores in [
            ("Rouge-L", rouge_scores),
            ("BLEU", bleu_scores),
            ("BERTScore", bert_scores),
            ("SemScore", sem_scores),
        ]:
            arr = np.array(scores)
            results[name] = {
                "mean": float(np.mean(arr)),
                "std": float(np.std(arr)),
                "scores": scores,
            }
        return results
