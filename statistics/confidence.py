def paired_mean_ci(deltas, z=1.96):
    if not deltas: raise ValueError('non-empty deltas required')
    avg = sum(deltas) / len(deltas)
    if len(deltas) == 1: return {'mean': avg, 'low': avg, 'high': avg, 'n': 1}
    variance = sum((delta - avg) ** 2 for delta in deltas) / (len(deltas) - 1)
    se = (variance / len(deltas)) ** 0.5
    return {'mean': avg, 'low': avg - z * se, 'high': avg + z * se, 'n': len(deltas)}
