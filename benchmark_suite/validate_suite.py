import argparse
import json
from collections import Counter
from pathlib import Path

def validate(root: Path):
    counts, errors, ids = Counter(), [], set()
    for path in sorted(root.glob('*.jsonl')):
        for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                for key in ('id', 'category', 'input', 'question', 'expected', 'status', 'source'):
                    if key not in row: raise ValueError('missing ' + key)
                if row['id'] in ids: raise ValueError('duplicate id')
                if row['status'] not in ('pending', 'verified', 'rejected'): raise ValueError('invalid status')
                ids.add(row['id']); counts[row['category']] += 1
            except (ValueError, json.JSONDecodeError) as exc:
                errors.append(f'{path}:{line_no}:{exc}')
    return {'total': sum(counts.values()), 'categories': dict(counts), 'errors': errors}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('directory', type=Path); args = parser.parse_args()
    result = validate(args.directory); print(json.dumps(result, ensure_ascii=False, indent=2)); raise SystemExit(bool(result['errors']))
