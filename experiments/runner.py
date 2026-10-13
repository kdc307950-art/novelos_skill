import json
from datetime import datetime, timezone
from pathlib import Path

def run_manifest(manifest: dict, output: Path):
    required = ('id', 'name', 'dataset', 'baseline', 'novelos_version', 'metrics')
    missing = [key for key in required if key not in manifest]
    if missing:
        raise ValueError('missing experiment fields: ' + ', '.join(missing))
    record = {**manifest, 'status': 'pending_human', 'started_at': datetime.now(timezone.utc).isoformat(), 'results': [], 'human_eval_required': True}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return record

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('manifest', type=Path)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    print(json.dumps(run_manifest(json.loads(args.manifest.read_text(encoding='utf-8')), args.out), ensure_ascii=False, indent=2))
