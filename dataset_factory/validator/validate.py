import json
from pathlib import Path

REQUIRED = ('id', 'text', 'task', 'expected_answer', 'reasoning_summary', 'labels', 'source', 'license', 'confidence', 'status')

def validate_case(case):
    errors = [f'missing:{key}' for key in REQUIRED if key not in case]
    if case.get('status') == 'verified' and case.get('confidence') is None:
        errors.append('verified_without_confidence')
    if case.get('source') == 'github' and not case.get('license'):
        errors.append('github_case_without_license')
    if not isinstance(case.get('labels', {}), dict):
        errors.append('labels_not_object')
    return errors

def validate_jsonl(path: Path):
    errors = []
    for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if line.strip():
            try:
                errors.extend(f'{line_no}:{error}' for error in validate_case(json.loads(line)))
            except json.JSONDecodeError as exc:
                errors.append(f'{line_no}:invalid_json:{exc.msg}')
    return errors
