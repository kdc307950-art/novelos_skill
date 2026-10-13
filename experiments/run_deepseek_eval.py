"""Run a small, reproducible DeepSeek V4.1 Flash pilot over synthetic cases."""

import argparse
import json
import os
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MODEL = 'deepseek-flash'
BASE_URL = 'https://api.deepseek.com/chat/completions'

def call_model(api_key, system, prompt, temperature=0.2, max_tokens=700):
    body = json.dumps({'model': MODEL, 'thinking': {'type': 'disabled'}, 'temperature': temperature, 'max_tokens': max_tokens, 'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}]}, ensure_ascii=False).encode('utf-8')
    request = urllib.request.Request(BASE_URL, data=body, method='POST', headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'})
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=180) as response:
        payload = json.loads(response.read().decode('utf-8'))
    return payload, round((time.perf_counter() - started) * 1000)

def load_cases(path, limit):
    rows = []
    for file_path in sorted(path.rglob('*.jsonl')):
        for line in file_path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                rows.append(json.loads(line))
                if len(rows) >= limit: return rows
    return rows

def run(input_dir, output, limit):
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key: raise RuntimeError('DEEPSEEK_API_KEY is not configured')
    cases = load_cases(input_dir, limit)
    system = '你是 NovelOS 的小说编辑评测 Agent。只基于给定材料回答，区分事实、推断和建议，引用证据，不要声称精确留存率。输出简洁中文分析。'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', encoding='utf-8') as stream:
        for case in cases:
            prompt = f"类别：{case.get('type')}\n上下文：{case.get('context','')}\n文本：{case.get('text','')}\n问题：{case.get('question','')}\n请给出判断、证据和修改建议。"
            started = datetime.now(timezone.utc).isoformat()
            try:
                payload, duration_ms = call_model(api_key, system, prompt)
                content = payload['choices'][0]['message']['content']
                usage = payload.get('usage', {})
                record = {'case_id': case['id'], 'model': MODEL, 'provider': 'DeepSeek', 'api_base': 'https://api.deepseek.com', 'started_at': started, 'duration_ms': duration_ms, 'input_chars': len(prompt), 'output': content, 'usage': usage, 'status': 'completed', 'human_score': None, 'evaluation_status': 'pending_human'}
            except Exception as exc:
                record = {'case_id': case['id'], 'model': MODEL, 'provider': 'DeepSeek', 'started_at': started, 'status': 'failed', 'error': str(exc), 'evaluation_status': 'blocked'}
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    return len(cases)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--input', type=Path, default=Path('dataset/literary_benchmark')); parser.add_argument('--out', type=Path, default=Path('experiments/runs/deepseek-v4.1-flash-pilot.jsonl')); parser.add_argument('--limit', type=int, default=6); args = parser.parse_args(); print(f'processed {run(args.input, args.out, args.limit)} cases')
