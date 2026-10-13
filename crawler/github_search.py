import argparse
import json
import subprocess
from pathlib import Path

QUERIES = ['novel analysis', 'literary analysis dataset', 'story evaluation',
           'narrative benchmark', 'long context benchmark', 'creative writing benchmark',
           'book QA dataset', 'fiction QA', 'computational literary studies', 'literary NLP']

def search(queries, limit=10):
    found = {}
    for query in queries:
        raw = subprocess.check_output(['gh', 'search', 'repos', query, '--limit', str(limit),
              '--json', 'fullName,url,description,stargazersCount,forksCount,updatedAt'], encoding='utf-8')
        for item in json.loads(raw):
            name = item['fullName']
            found.setdefault(name, {**item, 'queries': []})['queries'].append(query)
    return list(found.values())

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', action='append')
    p.add_argument('--limit', type=int, default=10)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    records = search(a.query or QUERIES, a.limit)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
