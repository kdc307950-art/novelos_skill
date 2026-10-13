def compare(baseline, novelos, key='score'):
    pairs = []
    for case_id, base in baseline.items():
        if case_id in novelos:
            pairs.append((case_id, base.get(key, 0), novelos[case_id].get(key, 0)))
    return {'cases': len(pairs), 'baseline_mean': sum(p[1] for p in pairs) / len(pairs) if pairs else None, 'novelos_mean': sum(p[2] for p in pairs) / len(pairs) if pairs else None, 'pairs': pairs}
