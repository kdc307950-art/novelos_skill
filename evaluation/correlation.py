"""Agreement metrics between model and human scores."""
from math import sqrt

def mae(model, human):
    if len(model) != len(human) or not model:
        raise ValueError('equal non-empty score lists required')
    return sum(abs(a - b) for a, b in zip(model, human)) / len(model)

def pearson(model, human):
    if len(model) != len(human) or len(model) < 2:
        raise ValueError('at least two paired scores required')
    am, ah = sum(model) / len(model), sum(human) / len(human)
    numerator = sum((a - am) * (b - ah) for a, b in zip(model, human))
    denominator = sqrt(sum((a - am) ** 2 for a in model) * sum((b - ah) ** 2 for b in human))
    return numerator / denominator if denominator else 0.0
