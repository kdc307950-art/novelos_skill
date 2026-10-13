"""Validate published cases and report actual counts without evaluating models."""
import argparse
import json
from pathlib import Path
from collections import Counter
from .build_dataset import CATEGORIES
from .cleaner import text_hash

def validate(root):
    ids, hashes, groups = set(), set(), {}
    counts, errors, verified = Counter(), [], 0
    for category in CATEGORIES:
        for path in sorted((root / category).glob('*.jsonl')):
            for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                    for key in ['id','source','type','text','context','question','answer','labels','metadata','confidence','verified']:
                        if key not in r:
                            raise ValueError('missing ' + key)
                    if r['type'] != category or r['source'] not in ['github','synthetic','author_authorized']:
                        raise ValueError('invalid category/source')
                    if any(not isinstance(r[k], str) for k in ['id','text','context','question','answer']):
                        raise ValueError('text fields must be strings')
                    if not r['question'] or not r['answer'] or not r['id']:
                        raise ValueError('empty QA or ID')
                    if type(r['verified']) is not bool:
                        raise ValueError('verified must be boolean')
                    if r['confidence'] is not None and (type(r['confidence']) not in [int,float] or not 0 <= r['confidence'] <= 1):
                        raise ValueError('invalid confidence')
                    if not isinstance(r['labels'], dict) or any(type(v) not in [int,float] or not 0 <= v <= 10 for v in r['labels'].values()):
                        raise ValueError('invalid quality labels')
                    m = r['metadata']
                    if any(not m.get(k) for k in ['license','url','group_id','split','status']):
                        raise ValueError('missing provenance')
                    if m['split'] not in ['train','validation','test']:
                        raise ValueError('invalid split')
                    if m['status'] not in ['pending_review','reviewed','rejected']:
                        raise ValueError('invalid review status')
                    if r['verified'] and (m['status'] != 'reviewed' or r['confidence'] is None or any(not m.get(k) for k in ['annotation_id','reviewer','reviewed_at'])):
                        raise ValueError('verified case lacks human annotation')
                    group = (m.get('repo', m['url']), m['group_id'])
                    if group in groups and groups[group] != m['split']:
                        raise ValueError('group split leakage')
                    digest = text_hash('\n'.join(r[k] for k in ['text','context','question','answer']))
                    if r['id'] in ids or digest in hashes:
                        raise ValueError('duplicate case')
                    ids.add(r['id']); hashes.add(digest); groups[group] = m['split']
                    counts[category] += 1
                    verified += r['verified']
                except (ValueError, TypeError, KeyError) as exc:
                    errors.append(f'{path}:{number}: {exc}')
    return {'total': sum(counts.values()), 'categories': dict(counts), 'verified': verified, 'errors': errors}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('directory', type=Path)
    a = p.parse_args()
    result = validate(a.directory)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))
