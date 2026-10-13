"""Build a deduplicated review queue from one approved source file."""
import argparse
import hashlib
import json
from pathlib import Path
from .extractor import rows, extract
from .cleaner import normalize, text_hash, quality

CATEGORIES = ['01_Continuity', '02_Character', '03_Structure', '04_Literary', '05_Commercial', '06_Failure']

def build(input_path, mapping, metadata, category, out, min_chars=200):
    if category not in CATEGORIES:
        raise ValueError('unknown category')
    if metadata.get('status') != 'approved' or not metadata.get('data_license'):
        raise ValueError('data license approval required')
    accepted, seen, rejected = [], set(), {}
    for index, raw in enumerate(rows(input_path)):
        row = extract(raw, mapping)
        row = {k: normalize(str(v)) for k, v in row.items()}
        valid, reason = quality(row, min_chars)
        # Context-only hashing would discard different questions about one book.
        digest = text_hash('\n'.join(row.get(k, '') for k in ['text', 'context', 'question', 'answer']))
        if digest in seen:
            valid, reason = False, 'duplicate'
        if not valid:
            rejected[reason] = rejected.get(reason, 0) + 1
            continue
        seen.add(digest)
        group = str(raw.get(metadata.get('group_field', 'document_id'), digest))
        # Keep all questions from a book in the same split.
        bucket = int(hashlib.sha256(group.encode()).hexdigest()[:8], 16) % 10
        accepted.append({'id': 'NLD-' + digest[:20], 'source': 'github', 'type': category,
            **{k: row.get(k, '') for k in ['text', 'context', 'question', 'answer']},
            'labels': {}, 'confidence': None, 'verified': False,
            'metadata': {'license': metadata['data_license'], 'url': metadata['url'],
                'commit': metadata['commit'], 'original_row': index, 'group_id': group,
                'split': 'test' if bucket == 0 else 'validation' if bucket == 1 else 'train',
                'content_hash': digest, 'status': 'pending_review'}})
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        raise FileExistsError(out)
    out.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in accepted), encoding='utf-8')
    return {'accepted': len(accepted), 'rejected': rejected, 'verified': 0}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    p.add_argument('--mapping', type=Path, required=True)
    p.add_argument('--manifest', type=Path, required=True)
    p.add_argument('--category', choices=CATEGORIES, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--min-chars', type=int, default=200)
    a = p.parse_args()
    print(json.dumps(build(a.input, json.loads(a.mapping.read_text(encoding='utf-8')),
        json.loads(a.manifest.read_text(encoding='utf-8')), a.category, a.out, a.min_chars)))
