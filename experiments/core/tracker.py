import json
from pathlib import Path

class ExperimentTracker:
    def __init__(self, path: Path):
        self.path = path

    def append(self, event):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + '\n')
