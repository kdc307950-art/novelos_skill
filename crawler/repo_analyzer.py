import argparse
import json
import math
import subprocess
from datetime import datetime, timezone
from pathlib import Path

def rank(record, now=None):
    now = now or datetime.now(timezone.utc)
    updated = datetime.fromisoformat(record['updatedAt'].replace('Z', '+00:00'))
    components = {
        'stars': min(math.log1p(record['stargazersCount']) / math.log1p(10000), 1),
        'forks': min(math.log1p(record['forksCount']) / math.log1p(2000), 1),
        'activity': 1 / (1 + max((now - updated).days, 0) / 365),
        'quality': record.get('dataset_quality', 0),
        'license': float(record.get('data_license_reviewed', False)),
    }
    weights = dict(stars=.20, forks=.15, activity=.20, quality=.30, license=.15)
    return round(100 * sum(components[k] * weights[k] for k in weights), 2)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    records = json.loads(a.input.read_text(encoding='utf-8'))
    for r in records:
        repo = json.loads(subprocess.check_output(['gh', 'api', 'repos/' + r['fullName']], encoding='utf-8'))
        r['repository_license'] = (repo.get('license') or {}).get('spdx_id', 'unknown')
        r['score'] = rank(r)
        r['review_status'] = 'candidate'
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(sorted(records, key=lambda r: -r['score']), ensure_ascii=False, indent=2), encoding='utf-8')
