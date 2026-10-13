import json
from pathlib import Path

def compare(baseline, novelos):
    dimensions = ['finding_count', 'evidence_accuracy', 'revision_value', 'literary_judgment']
    return {'dimensions': {name: {'baseline': baseline.get(name, 0), 'novelos': novelos.get(name, 0), 'delta': novelos.get(name, 0) - baseline.get(name, 0)} for name in dimensions}}

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('baseline', type=Path)
    p.add_argument('novelos', type=Path)
    args = p.parse_args()
    print(json.dumps(compare(json.loads(args.baseline.read_text()), json.loads(args.novelos.read_text())), ensure_ascii=False, indent=2))
