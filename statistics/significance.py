from math import erf, sqrt

def paired_normal_approx(deltas):
    """Approximate two-sided p; use a real statistical package for publication claims."""
    if len(deltas) < 2: raise ValueError('at least two paired observations required')
    avg = sum(deltas) / len(deltas)
    variance = sum((delta - avg) ** 2 for delta in deltas) / (len(deltas) - 1)
    if variance == 0: return {'mean': avg, 'z': 0.0 if avg == 0 else float('inf'), 'p_approx': 0.0 if avg else 1.0, 'method': 'degenerate'}
    z = avg / ((variance / len(deltas)) ** 0.5)
    cdf = 0.5 * (1 + erf(abs(z) / sqrt(2)))
    return {'mean': avg, 'z': z, 'p_approx': round(2 * (1 - cdf), 6), 'method': 'normal_approximation', 'publication_ready': False}
