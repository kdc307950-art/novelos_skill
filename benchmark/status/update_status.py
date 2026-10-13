import json
from pathlib import Path

def update(progress_path: Path, pending_dir: Path):
    data = json.loads(progress_path.read_text(encoding='utf-8'))
    counts = {key: {'total': value['total'], 'annotated': 0, 'progress': 0.0} for key, value in data['categories'].items()}
    for path in pending_dir.glob('*.jsonl'):
        category = path.stem.lower()
        if category not in counts: continue
        rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        annotated = sum(row.get('status') == 'verified' and row.get('verified') is True for row in rows)
        counts[category]['annotated'] = annotated
        counts[category]['progress'] = round(annotated / counts[category]['total'], 4)
    data['categories'] = counts
    data['human_verified'] = sum(item['annotated'] for item in counts.values())
    data['pending_review'] = data['total_cases'] - data['human_verified']
    progress_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return data

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(); parser.add_argument('--progress', type=Path, default=Path('benchmark/status/progress.json')); parser.add_argument('--pending', type=Path, default=Path('benchmark_suite/pending')); args = parser.parse_args(); print(json.dumps(update(args.progress, args.pending), ensure_ascii=False, indent=2))
