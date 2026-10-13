import json
from pathlib import Path

def export_verified(input_dir: Path, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(input_dir.rglob('*.jsonl')):
        for line in path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get('status') == 'verified' and row.get('verified') is True:
                    rows.append(row)
    output.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')
    return len(rows)
