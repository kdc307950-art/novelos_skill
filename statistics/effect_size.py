from math import sqrt

def cohens_d(a, b):
    if len(a) < 2 or len(a) != len(b): raise ValueError('paired non-empty samples required')
    mean_a, mean_b = sum(a) / len(a), sum(b) / len(b)
    variance = sum(((x - mean_a) - (y - mean_b)) ** 2 for x, y in zip(a, b)) / (len(a) - 1)
    if variance == 0:
        return float('inf') if mean_a != mean_b else 0.0
    return (mean_a - mean_b) / sqrt(variance)
