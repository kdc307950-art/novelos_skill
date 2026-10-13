def score_output(case, output):
    """Transparent baseline scorer; human rubrics should override it for literary claims."""
    expected = case.get('expected_answer', '')
    text = str(output)
    return {'answer_overlap': round(sum(1 for token in expected.split() if token and token in text) / max(len(expected.split()), 1), 3), 'human_required': True}
