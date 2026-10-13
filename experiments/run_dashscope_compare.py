"""Run Qwen/Kimi on the same synthetic cases through DashScope OpenAI-compatible Chat Completions."""

import argparse
import json
import os
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'

def call_model(api_key, model, prompt):
    body_data = {'model': model, 'max_tokens': 2000 if model == 'kimi-k3' else 700, 'messages': [{'role': 'system', 'content': '你是 NovelOS 的小说编辑评测 Agent。只基于材料回答，区分事实、推断和建议，引用证据，不要声称精确留存率。输出简洁中文分析。'}, {'role': 'user', 'content': prompt}]}
    if model != 'kimi-k3': body_data['temperature'] = 0.2
    body = json.dumps(body_data, ensure_ascii=False).encode('utf-8')
    request = urllib.request.Request(BASE_URL, data=body, method='POST', headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'})
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=180) as response:
        payload = json.loads(response.read().decode('utf-8'))
    return payload, round((time.perf_counter() - started) * 1000)

def cases(root, limit):
    rows = []
    for path in sorted(root.rglob('*.jsonl')):
        for line in path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                rows.append(json.loads(line))
                if len(rows) >= limit: return rows
    return rows

def run(model, root, output, limit):
    key = os.environ.get('DASHSCOPE_API_KEY')
    if not key: raise RuntimeError('DASHSCOPE_API_KEY is not configured')
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = cases(root, limit)
    with output.open('w', encoding='utf-8') as stream:
        for case in rows:
            prompt = f"类别：{case.get('type')}\n上下文：{case.get('context','')}\n文本：{case.get('text','')}\n问题：{case.get('question','')}\n请给出判断、证据和修改建议。"
            record = {'case_id': case['id'], 'model': model, 'provider': 'Alibaba Cloud Model Studio', 'api_base': BASE_URL, 'started_at': datetime.now(timezone.utc).isoformat()}
            try:
                payload, duration = call_model(key, model, prompt)
                record.update({'duration_ms': duration, 'input_chars': len(prompt), 'output': payload['choices'][0]['message'].get('content', ''), 'usage': payload.get('usage', {}), 'status': 'completed', 'human_score': None, 'evaluation_status': 'pending_human'})
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode('utf-8', errors='replace')
                record.update({'status': 'failed', 'error': f'HTTP {exc.code}: {detail}', 'evaluation_status': 'blocked'})
            except Exception as exc:
                record.update({'status': 'failed', 'error': str(exc), 'evaluation_status': 'blocked'})
            stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    return len(rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--model', required=True); parser.add_argument('--input', type=Path, default=Path('dataset/literary_benchmark')); parser.add_argument('--out', type=Path, required=True); parser.add_argument('--limit', type=int, default=6); args = parser.parse_args(); print(f'processed {run(args.model, args.input, args.out, args.limit)} cases')
