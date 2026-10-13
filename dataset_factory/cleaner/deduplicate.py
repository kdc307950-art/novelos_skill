import hashlib
import re
import unicodedata

def normalize(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)).strip()

def fingerprint(record: dict) -> str:
    content = '\n'.join(str(record.get(key, '')) for key in ('text', 'context', 'question', 'expected_answer'))
    return hashlib.sha256(normalize(content).encode('utf-8')).hexdigest()

def keep_highest_quality(records):
    selected = {}
    for record in records:
        key = fingerprint(record)
        if key not in selected or record.get('quality_score', 0) > selected[key].get('quality_score', 0):
            selected[key] = record
    return list(selected.values())
