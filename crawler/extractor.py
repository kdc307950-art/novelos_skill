"""Extract explicit fields; never infer gold answers or scores."""
import csv
import json
import xml.etree.ElementTree as ET

def rows(path):
    suffix = path.suffix.lower()
    if suffix == '.csv':
        with path.open(encoding='utf-8-sig', newline='') as stream:
            yield from csv.DictReader(stream)
    elif suffix == '.jsonl':
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            if line.strip():
                yield json.loads(line)
    elif suffix == '.json':
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        yield from data if isinstance(data, list) else [data]
    elif suffix == '.txt':
        yield {'text': path.read_text(encoding='utf-8-sig')}
    elif suffix == '.xml':
        for node in ET.parse(path).getroot():
            yield {child.tag: ''.join(child.itertext()) for child in node}
    else:
        raise ValueError('unsupported input format')

def extract(row, mapping):
    return {target: row.get(source, '') for target, source in mapping.items()}
