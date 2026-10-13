import json
from pathlib import Path

def write_report(result, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {'status': 'measured' if result.get('cases', 0) else 'pending', 'result': result, 'limitations': ['Automated overlap is not a literary judgment.', 'Human labels and model/version metadata are required for claims of superiority.']}
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return output
