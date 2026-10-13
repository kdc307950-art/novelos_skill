import json
from collections import Counter
from pathlib import Path

def analyze(records):
    counts = Counter()
    for record in records:
        if record.get('status') != 'failed':
            continue
        counts[record.get('agent', 'unknown')] += 1
    return {'failure_count': sum(counts.values()), 'by_agent': dict(counts), 'next_action': 'add a focused regression case before changing a prompt'}

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    records = json.loads(args.input.read_text(encoding='utf-8'))
    args.out.write_text(json.dumps(analyze(records), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
