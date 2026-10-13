from collections import defaultdict

def analyze(pairs):
    """Return mean signed error and sample count by dimension.

    Pair records use {dimension, ai, human}; positive bias means AI scores higher.
    """
    grouped = defaultdict(list)
    for pair in pairs:
        grouped[pair['dimension']].append(float(pair['ai']) - float(pair['human']))
    result = {}
    for dimension, errors in grouped.items():
        result[dimension] = {'count': len(errors), 'mean_signed_error': round(sum(errors) / len(errors), 4), 'mean_absolute_error': round(sum(abs(error) for error in errors) / len(errors), 4)}
    return result
