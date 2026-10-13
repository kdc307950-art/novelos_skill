from statistics import mean

def contribution(full_runs, ablated_runs):
    """Estimate contribution as full score minus matched ablation score."""
    by_case = {row['case_id']: row['score'] for row in ablated_runs}
    deltas = [row['score'] - by_case[row['case_id']] for row in full_runs if row['case_id'] in by_case]
    return {'matched_cases': len(deltas), 'mean_delta': mean(deltas) if deltas else None, 'status': 'measured' if deltas else 'pending'}
