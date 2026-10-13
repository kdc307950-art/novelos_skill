def propose(mined):
    proposals = []
    for pattern, count in mined.get('by_pattern', {}).items():
        proposals.append({'pattern': pattern, 'count': count, 'action': 'add or strengthen a targeted prompt/rule only after regression evidence', 'approval': 'human_required'})
    return proposals
