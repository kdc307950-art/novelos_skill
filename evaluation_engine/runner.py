import json
from pathlib import Path

class EvaluationRunner:
    def __init__(self, model, scorer):
        self.model = model
        self.scorer = scorer

    def run(self, dataset):
        results = []
        for case in dataset:
            output = self.model(case)
            results.append({'id': case['id'], 'output': output, 'score': self.scorer(case, output), 'status': 'measured'})
        return results

    def run_jsonl(self, path: Path):
        cases = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        return self.run(cases)
