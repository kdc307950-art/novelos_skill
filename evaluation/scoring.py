"""Weighted story quality scoring."""

WEIGHTS = {"story": 0.30, "character": 0.25, "emotion": 0.20, "literary": 0.15, "commercial": 0.10}


def score(dimensions):
    missing = set(WEIGHTS) - set(dimensions)
    if missing:
        raise ValueError(f"missing dimensions: {', '.join(sorted(missing))}")
    for name, value in dimensions.items():
        if not 0 <= float(value) <= 10:
            raise ValueError(f"{name} must be between 0 and 10")
    return round(sum(float(dimensions[name]) * weight for name, weight in WEIGHTS.items()), 2)


def report(dimensions):
    return {"dimensions": {key: float(value) for key, value in dimensions.items()}, "weights": WEIGHTS, "overall": score(dimensions)}
