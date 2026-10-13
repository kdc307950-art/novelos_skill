import json
from collections import Counter
from pathlib import Path

def progress(root: Path):
    counts = Counter()
    for path in root.rglob('*.jsonl'):
        for line in path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                row = json.loads(line)
                counts[(row.get('category', path.stem), row.get('status', 'missing'))] += 1
    return {'total': sum(counts.values()), 'by_category': {category: {status: count for (item, status), count in counts.items() if item == category} for category, _ in counts}, 'verified': sum(count for (category, status), count in counts.items() if status == 'verified'), 'pending': sum(count for (category, status), count in counts.items() if status == 'pending'), 'rejected': sum(count for (category, status), count in counts.items() if status == 'rejected')}

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('directory', type=Path)
    args = p.parse_args()
    print(json.dumps(progress(args.directory), ensure_ascii=False, indent=2))
