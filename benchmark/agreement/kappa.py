from collections import Counter

def cohens_kappa(first, second):
    if len(first) != len(second) or not first:
        raise ValueError('paired labels required')
    observed = sum(a == b for a, b in zip(first, second)) / len(first)
    labels = set(first) | set(second)
    expected = sum((first.count(label) / len(first)) * (second.count(label) / len(second)) for label in labels)
    return (observed - expected) / (1 - expected) if expected != 1 else 1.0

def fleiss_kappa(matrix):
    if not matrix or len(matrix) < 2:
        raise ValueError('at least two items required')
    reviewers = sum(matrix[0].values())
    proportions = {label: sum(row.get(label, 0) for row in matrix) / (len(matrix) * reviewers) for label in set().union(*matrix)}
    p_bar = sum((sum(value * (value - 1) for value in row.values()) / (reviewers * (reviewers - 1))) for row in matrix) / len(matrix)
    p_expected = sum(value * value for value in proportions.values())
    return (p_bar - p_expected) / (1 - p_expected) if p_expected != 1 else 1.0
