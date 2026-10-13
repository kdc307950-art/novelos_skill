"""Download only exact, reviewed files at an immutable commit."""
import argparse
import hashlib
import json
import re
import subprocess
import base64
from pathlib import Path, PurePosixPath

def download(manifest, output):
    if manifest.get('status') != 'approved' or not manifest.get('data_license'):
        raise ValueError('file-level data license review is required')
    if not re.fullmatch(r'[0-9a-f]{40}', manifest['commit']):
        raise ValueError('pin a full commit SHA')
    output.mkdir(parents=True, exist_ok=True)
    receipt = []
    for name in manifest['files']:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or path.suffix.lower() not in {'.txt', '.json', '.jsonl', '.csv', '.xml'}:
            raise ValueError('invalid dataset file path: ' + name)
        endpoint = f"repos/{manifest['repo']}/contents/{name}?ref={manifest['commit']}"
        info = json.loads(subprocess.check_output(['gh', 'api', endpoint], encoding='utf-8'))
        if info.get('size', 0) > 20_000_000 or info.get('encoding') != 'base64':
            raise ValueError('file too large or unsupported content encoding')
        data = base64.b64decode(info['content'])
        target = output.joinpath(*path.parts)
        if target.exists():
            raise FileExistsError(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        receipt.append({'file': name, 'sha256': hashlib.sha256(data).hexdigest()})
    (output / 'receipt.json').write_text(json.dumps({'manifest': manifest, 'files': receipt}, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('manifest', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    download(json.loads(a.manifest.read_text(encoding='utf-8')), a.out)
