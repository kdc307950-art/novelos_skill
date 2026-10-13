def summarize(rows):
    result = {}
    for row in rows:
        name = row['agent']; result.setdefault(name, {'usage': 0, 'gains': [], 'errors': 0, 'latencies': []})
        item = result[name]; item['usage'] += 1; item['gains'].append(row.get('gain', 0)); item['errors'] += int(row.get('error', False)); item['latencies'].append(row.get('latency_ms', 0))
    for item in result.values():
        item['gain'] = sum(item['gains']) / len(item['gains']) if item['gains'] else None; item['error_rate'] = item['errors'] / max(item['usage'], 1); item['latency_ms'] = sum(item['latencies']) / len(item['latencies']) if item['latencies'] else None; del item['gains']; del item['errors']; del item['latencies']
    return result
