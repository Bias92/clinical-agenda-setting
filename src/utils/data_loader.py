"""
Data loader for clinical conversation transcripts and annotations.

Expected data format:

transcript file (data/processed/case_XX.json):
{
    "id": "case_01",
    "lines": [
        {"speaker": "Provider", "text": "So what brings you in here today?"},
        {"speaker": "Patient", "text": "I've been having chest pain for about a week."},
        ...
    ]
}

annotation file (data/annotations/case_XX.json):
{
    "id": "case_01",
    "annotations": [
        {
            "line_idx": 1,
            "type": "agenda_item",
            "summary": "Patient is experiencing chest pain for approximately one week."
        },
        {
            "line_idx": 5,
            "type": "detail",
            "summary": "Pain is rated 7 out of 10 on pain scale."
        },
        ...
    ]
}
"""

import json
import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class TranscriptLine:
    speaker: str  # "Provider" or "Patient"
    text: str


@dataclass
class Annotation:
    line_idx: int
    type: str  # "agenda_item" or "detail"
    summary: str


@dataclass
class ClinicalCase:
    id: str
    lines: list[TranscriptLine]
    annotations: list[Annotation]


def load_transcript(filepath: str) -> tuple[str, list[TranscriptLine]]:
    """Load a single transcript JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    lines = [TranscriptLine(speaker=l["speaker"], text=l["text"]) for l in data["lines"]]
    return data["id"], lines


def load_annotations(filepath: str) -> tuple[str, list[Annotation]]:
    """Load a single annotation JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    annotations = [
        Annotation(line_idx=a["line_idx"], type=a["type"], summary=a["summary"])
        for a in data["annotations"]
    ]
    return data["id"], annotations


def load_all_cases(
    transcript_dir: str, annotation_dir: str
) -> list[ClinicalCase]:
    """Load all clinical cases from directories."""
    cases = []
    transcript_dir = Path(transcript_dir)
    annotation_dir = Path(annotation_dir)

    for t_file in sorted(transcript_dir.glob("*.json")):
        case_id, lines = load_transcript(str(t_file))
        a_file = annotation_dir / t_file.name
        if a_file.exists():
            _, annotations = load_annotations(str(a_file))
        else:
            print(f"Warning: No annotation file for {case_id}")
            annotations = []
        cases.append(ClinicalCase(id=case_id, lines=lines, annotations=annotations))

    print(f"Loaded {len(cases)} clinical cases")
    return cases


def format_transcript(lines: list[TranscriptLine]) -> str:
    """Format transcript lines into a single string for baseline experiment."""
    return "\n".join(f"[{l.speaker}] {l.text}" for l in lines)


def chunk_lines(
    lines: list[TranscriptLine], chunk_size: int
) -> list[list[TranscriptLine]]:
    """Split transcript lines into fixed-size chunks for input_lines experiment."""
    return [lines[i : i + chunk_size] for i in range(0, len(lines), chunk_size)]


def get_ground_truth_for_line(annotations: list[Annotation], line_idx: int) -> Annotation | None:
    """Get ground truth annotation for a specific line index."""
    for a in annotations:
        if a.line_idx == line_idx:
            return a
    return None
