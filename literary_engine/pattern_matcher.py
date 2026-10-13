"""Match a text summary against local literary mechanism records."""

from pathlib import Path
import json


def match(text: str, pattern_dir: Path):
    results = []
    for path in sorted(pattern_dir.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        terms = [record.get("pattern", ""), record.get("mechanism", "")]
        overlap = sum(1 for term in terms if term and any(token in text for token in term.split()))
        if overlap:
            results.append({"pattern_id": record.get("pattern_id", path.stem), "match_strength": overlap / len(terms), "mechanism": record.get("mechanism", "")})
    return results
