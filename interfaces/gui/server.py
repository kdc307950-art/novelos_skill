"""Dependency-free GUI API and static server."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
STATIC = Path(__file__).resolve().parent / 'static'

def project_status():
    storage = ROOT / 'memory' / 'storage'
    counts = {}
    for name in ('character', 'timeline', 'foreshadow', 'relationship', 'world'):
        try:
            value = json.loads((storage / f'{name}.json').read_text(encoding='utf-8'))
            counts[name] = len(value) if isinstance(value, list) else len(value)
        except (FileNotFoundError, json.JSONDecodeError):
            counts[name] = 0
    try:
        state = json.loads((storage / 'novel_state.json').read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        state = {}
    return {'mode': 'editor', 'counts': counts, 'story_phase': state.get('story_phase', 'setup'), 'current_arc': state.get('current_arc', '')}

class Handler(BaseHTTPRequestHandler):
    def send_payload(self, payload, status=200, content_type='application/json'):
        body = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/api/status':
            return self.send_payload(project_status())
        files = {'/': 'index.html', '/index.html': 'index.html', '/app.js': 'app.js', '/styles.css': 'styles.css'}
        if path in files:
            target = STATIC / files[path]
            content_type = 'text/html; charset=utf-8' if target.suffix == '.html' else 'text/css' if target.suffix == '.css' else 'application/javascript'
            return self.send_payload(target.read_bytes(), content_type=content_type)
        self.send_payload({'error': 'not_found'}, 404)

    def do_POST(self):
        if urlparse(self.path).path != '/api/analyze':
            return self.send_payload({'error': 'not_found'}, 404)
        length = int(self.headers.get('Content-Length', 0))
        payload = json.loads(self.rfile.read(length) or b'{}')
        text = payload.get('text', '')
        self.send_payload({'status': 'queued', 'mode': 'editor', 'chapter_id': payload.get('chapter_id', ''), 'summary': '分析任务已创建；接入 Runtime 后由选定 Agent 执行。', 'input_chars': len(text), 'next': ['continuity', 'character', 'structure']})

if __name__ == '__main__':
    print('NovelOS GUI: http://127.0.0.1:8765')
    ThreadingHTTPServer(('127.0.0.1', 8765), Handler).serve_forever()
