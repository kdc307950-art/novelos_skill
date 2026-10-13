import json
from pathlib import Path

DIMENSIONS = ('continuity', 'character', 'revision_value', 'literary')

def compare(baseline, novelos):
    result = {'cases': 0, 'dimensions': {dimension: {'baseline': [], 'novelos': []} for dimension in DIMENSIONS}}
    for case_id, base in baseline.items():
        if case_id not in novelos:
            continue
        result['cases'] += 1
        for dimension in DIMENSIONS:
            if dimension in base and dimension in novelos[case_id]:
                result['dimensions'][dimension]['baseline'].append(base[dimension])
                result['dimensions'][dimension]['novelos'].append(novelos[case_id][dimension])
    for dimension, values in result['dimensions'].items():
        if values['baseline']:
            values['baseline_mean'] = sum(values['baseline']) / len(values['baseline'])
            values['novelos_mean'] = sum(values['novelos']) / len(values['novelos'])
            values['delta'] = values['novelos_mean'] - values['baseline_mean']
    return result

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('baseline', type=Path)
    p.add_argument('novelos', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    result = compare(json.loads(a.baseline.read_text()), json.loads(a.novelos.read_text()))
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
