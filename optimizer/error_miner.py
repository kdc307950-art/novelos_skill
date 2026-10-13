from collections import Counter, defaultdict

def mine(results):
    """Group measured failures by agent and error pattern."""
    failures = [item for item in results if item.get('status') == 'failed' or item.get('passed') is False]
    by_agent = Counter(item.get('agent', 'unknown') for item in failures)
    by_pattern = Counter(item.get('failure_pattern', 'unspecified') for item in failures)
    return {'failure_count': len(failures), 'by_agent': dict(by_agent), 'by_pattern': dict(by_pattern), 'actions': ['add a focused regression case', 'compare prompt versions', 'require human review before changing defaults']}
