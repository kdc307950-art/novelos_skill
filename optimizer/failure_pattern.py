PATTERNS = {'missed_evidence': 'finding lacks a required source fact', 'overinterpretation': 'claim exceeds available evidence', 'continuity_miss': 'contradiction not detected', 'flat_character': 'decision ignores motivation or history', 'unsupported_score': 'score has no rubric or evidence'}

def classify(text):
    lower = text.lower()
    for name, description in PATTERNS.items():
        if any(term in lower for term in name.split('_')):
            return {'pattern': name, 'description': description, 'confidence': 0.4}
    return {'pattern': 'unknown', 'description': 'requires human review', 'confidence': 0.1}
