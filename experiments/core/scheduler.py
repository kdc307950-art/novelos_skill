from datetime import datetime, timezone

def schedule(manifests, max_parallel=1):
    return [{'id': item['id'], 'status': 'queued', 'scheduled_at': datetime.now(timezone.utc).isoformat(), 'max_parallel': max_parallel} for item in manifests]
