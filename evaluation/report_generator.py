import json
from pathlib import Path

def generate(run_result, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    report = {'title': 'NovelOS Evaluation Report', 'run': run_result, 'limitations': ['Synthetic and human-verified cases must be reported separately.', 'Aggregate scores do not prove causal superiority.']}
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return output
