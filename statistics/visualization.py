import json
from pathlib import Path

def write_summary(metrics, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({'status': 'descriptive', 'metrics': metrics, 'note': 'Use a plotted artifact and independent review for publication claims.'}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return output
